"""
Sphinx PHP domain.

The PHP domain. Based off of the rubydomain by SHIBUKAWA Yoshiki

:copyright: Copyright 2016 by Mark Story
:license: BSD, see LICENSE for details.
"""

import re
import inspect

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import _
from sphinx.domains import Domain, ObjType, Index
from sphinx.directives import ObjectDescription
from sphinx.util import logging
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import Field, GroupedField, TypedField
from sphinx import __version__ as sphinx_version


def log_info(fromdocnode, message: str):
    """
    Log informative message. Should have no effect on exit code.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"[phpdomain] {message}", location=fromdocnode)


def log_warning(fromdocnode, message: str):
    """
    Log warning. Should set exit code to non-zero.
    """
    logger = logging.getLogger(__name__)
    logger.warning(f"[phpdomain] {message}", location=fromdocnode, type="phpdomain")


def throw_if_false(fromdocnode, value, message: str):
    """
    Log warning if the value is not true and throw ValueError. Should set exit code to non-zero.
    """
    if not value:
        log_warning(fromdocnode, message)
        raise ValueError


php_sig_re = re.compile(
    r"""
    ^
    (public\ |protected\ |private\ )? # visibility
    (final\ |abstract\ |static\ )?    # modifiers
    ((?:\\?(?!\d)\w+)\:\:)?           # class name
    (\$?(?:\\?(?!\d)\w+)+) \s*        # thing name
    (?:
        \((.*)\)                      # optional: arguments
        (?: \s* -> \s* (.*))?         # return annotation
    )?
    (?: \s* : \s* (.*))?              # backed enum type / case value
    $                                 # and nothing more
    """,
    re.VERBOSE,
)


NS = "\\"

separators = {
    "global": None,
    "namespace": NS,
    "function": NS,
    "interface": NS,
    "class": None,
    "trait": None,
    "enum": None,
    "exception": None,
    "method": "::",
    "const": "::",
    "attr": "::$",
    "staticmethod": "::",
    "case": "::",
}

php_separator = re.compile(r"(\w+)?(?:[:]{2})?")


def _pseudo_parse_arglist(signode, arglist):
    # type: (addnodes.desc_signature, unicode) -> None
    """
    "Parse" a list of arguments separated by commas.
    Arguments can have "optional" annotations given by enclosing them in
    brackets.  Currently, this will split at any comma, even if it's inside a
    string literal (e.g. default argument value).

    This function comes from sphinx.domains.python.
    """
    paramlist = addnodes.desc_parameterlist()
    stack = [paramlist]
    try:
        for argument in arglist.split(","):
            argument = argument.strip()
            ends_open = ends_close = 0
            while argument.startswith("["):
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                argument = argument[1:].strip()
            while argument.startswith("]"):
                stack.pop()
                argument = argument[1:].strip()
            while argument.endswith("]") and not argument.endswith("[]"):
                ends_close += 1
                argument = argument[:-1].strip()
            while argument.endswith("["):
                ends_open += 1
                argument = argument[:-1].strip()
            if argument:
                stack[-1] += addnodes.desc_parameter(argument, argument)
            while ends_open:
                stack.append(addnodes.desc_optional())
                stack[-2] += stack[-1]
                ends_open -= 1
            while ends_close:
                stack.pop()
                ends_close -= 1
        if len(stack) != 1:
            raise IndexError
    except IndexError:
        # if there are too few or too many elements on the stack, just give up
        # and treat the whole argument list as one argument, discarding the
        # already partially populated paramlist node
        signode += addnodes.desc_parameterlist()
        signode[-1] += addnodes.desc_parameter(arglist, arglist)
    else:
        signode += paramlist


def php_rsplit(fullname):
    items = [item for item in php_separator.findall(fullname)]
    return "".join(items[:-2]), "".join(items[1:-1])


class PhpObject(ObjectDescription):
    """
    Description of a general PHP object.
    """

    option_spec = {
        "noindex": directives.flag,
        "noindexentry": directives.flag,
        "nocontentsentry": directives.flag,
        "module": directives.unchanged,
    }

    doc_field_types = [
        TypedField(
            "parameter",
            label=_("Parameters"),
            names=("param", "parameter", "arg", "argument"),
            typerolename="obj",
            typenames=("paramtype", "type"),
        ),
        TypedField(
            "variable",
            label=_("Variables"),
            rolename="obj",
            names=("var", "ivar", "cvar"),
            typerolename="obj",
            typenames=("vartype",),
        ),
        GroupedField(
            "exceptions",
            label=_("Throws"),
            rolename="exc",
            names=("throws", "throw", "exception", "except"),
            can_collapse=True,
        ),
        Field(
            "returnvalue",
            label=_("Returns"),
            has_arg=False,
            names=("returns", "return"),
        ),
        Field(
            "returntype",
            label=_("Return type"),
            has_arg=False,
            names=("rtype", "returntype"),
            bodyrolename="obj",
        ),
    ]

    def get_signature_prefix(self, sig):
        """
        May return a prefix to put before the object name in the signature.
        """
        return ""

    def needs_arglist(self):
        """
        May return true if an empty argument list is to be generated even if
        the document contains none.
        """
        return False

    def handle_signature(self, sig, signode):
        """
        Transform a PHP signature into RST nodes.
        Returns (fully qualified name of the thing, classname if any).

        If inside a class, the current class name is handled intelligently:
        * it is stripped from the displayed name if present
        * it is added to the full name (return value) if not present
        """
        m = php_sig_re.match(sig)
        if m is None:
            throw_if_false(signode, False, "Invalid signature")

        visibility, modifiers, name_prefix, name, arglist, retann, enumtype = m.groups()

        if not name_prefix:
            name_prefix = ""

        # determine namespace and class name (if applicable), as well as full name
        namespace = self.options.get(
            "namespace", self.env.temp_data.get("php:namespace")
        )
        separator = separators[self.objtype]

        classname = self.env.temp_data.get("php:class")
        # Method declared as Class::methodName
        if not classname and "::" in name_prefix:
            classname = name_prefix.rstrip("::")

        if self.objtype == "global" or self.objtype == "function":
            add_module = False
            namespace = None
            classname = None
            fullname = name
        else:
            add_module = True
            if name_prefix:
                classname = classname.rstrip("::")
                fullname = name_prefix + name

            # Currently in a class, but not creating another class,
            elif classname and not self.objtype in [
                "class",
                "exception",
                "interface",
                "trait",
                "enum",
                "function",
            ]:
                if not self.env.temp_data["php:in_class"]:
                    name_prefix = classname + separator

                fullname = classname + separator + name
            else:
                classname = ""
                fullname = name

            # A leading \ means the name is fully qualified
            # and should not inherit the current namespace.
            if fullname.startswith(NS) and namespace:
                add_module = False
                name = name[1:]
                fullname = fullname[1:]
                namespace = None

        signode["namespace"] = namespace
        signode["class"] = self.class_name = classname
        signode["fullname"] = fullname

        if visibility:
            signode += addnodes.desc_annotation(visibility, visibility)

        sig_prefix = self.get_signature_prefix(sig)

        if modifiers and not (sig_prefix and "static" in sig_prefix):
            signode += addnodes.desc_annotation(modifiers, modifiers)

        if sig_prefix:
            signode += addnodes.desc_annotation(sig_prefix, sig_prefix)

        if name_prefix:
            if namespace and not self.env.temp_data["php:in_class"]:
                name_prefix = namespace + NS + name_prefix
            signode += addnodes.desc_addname(name_prefix, name_prefix)

        elif add_module and self.env.config.add_module_names:
            if self.objtype == "global":
                nodetext = ""
                signode += addnodes.desc_addname(nodetext, nodetext)
            else:
                namespace = self.options.get(
                    "namespace", self.env.temp_data.get("php:namespace")
                )

                if namespace and not self.env.temp_data.get("php:in_class", False):
                    nodetext = namespace + NS
                    signode += addnodes.desc_addname(nodetext, nodetext)

        signode += addnodes.desc_name(name, name)

        if not arglist:
            if self.needs_arglist():
                # for callables, add an empty parameter list
                signode += addnodes.desc_parameterlist()
            if retann:
                signode += addnodes.desc_returns(retann, retann)
            elif enumtype:
                signode += addnodes.desc_returns(enumtype, enumtype)
            return fullname, name_prefix

        _pseudo_parse_arglist(signode, arglist)

        if retann:
            signode += addnodes.desc_returns(retann, retann)
        elif enumtype:
            signode += addnodes.desc_returns(enumtype, enumtype)
        return fullname, name_prefix

    def _object_hierarchy_parts(self, sig_node: addnodes.desc_signature):
        if "fullname" not in sig_node:
            return ()
        namespace = sig_node.get("namespace")
        fullname = sig_node["fullname"]

        if isinstance(namespace, str):
            return (namespace, *fullname.split("::"))
        else:
            return tuple(fullname.split("::"))

    def _toc_entry_name(self, sig_node: addnodes.desc_signature) -> str:
        if not sig_node.get("_toc_parts"):
            return ""

        config = self.env.app.config
        objtype = sig_node.parent.get("objtype")
        if config.add_function_parentheses and objtype in {"function", "method"}:
            parens = "()"
        else:
            parens = ""
        *parents, name = sig_node["_toc_parts"]
        if config.toc_object_entries_show_parents == "domain":
            return sig_node.get("fullname", name) + parens
        if config.toc_object_entries_show_parents == "hide":
            return name + parens
        if config.toc_object_entries_show_parents == "all":
            if (
                objtype in {"method", "const", "attr", "staticmethod", "case"}
                and len(parents) > 0
            ):
                name = parents.pop() + "::" + name
            return "\\".join(parents + [name + parens])
        return ""

    def get_index_text(self, namespace, name):
        """
        Return the text for the index entry of the object.
        """
        raise NotImplementedError("must be implemented in subclasses")

    def _is_class_member(self):
        return self.objtype.startswith("method") or self.objtype.startswith("attr")

    def add_target_and_index(self, name_cls, sig, signode):
        if self.objtype == "global":
            namespace = None
        else:
            namespace = self.options.get(
                "namespace", self.env.temp_data.get("php:namespace")
            )
        if self._is_class_member():
            if signode["class"]:
                prefix = namespace and namespace + NS or ""
            else:
                prefix = namespace and namespace + NS or ""
        else:
            prefix = namespace and namespace + NS or ""
        fullname = prefix + name_cls[0]

        # note target
        if fullname not in self.state.document.ids:
            signode["names"].append(fullname)
            signode["ids"].append(fullname)
            signode["first"] = not self.names
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata["php"]["objects"]
            if fullname in objects:
                self.state_machine.reporter.warning(
                    "duplicate object description of %s, " % fullname
                    + "other instance in "
                    + self.env.doc2path(objects[fullname][0]),
                    line=self.lineno,
                )
            objects[fullname] = (self.env.docname, self.objtype)

        if "noindexentry" not in self.options:
            indextext = self.get_index_text(namespace, name_cls)
            if indextext:
                self.indexnode["entries"].append(
                    ("single", indextext, fullname, fullname, None)
                )


class PhpGloballevel(PhpObject):
    """
    Description of an object on global level (global variables).
    """

    def get_index_text(self, namespace, name_cls):
        if self.objtype == "global":
            return _("%s (global variable)") % name_cls[0]
        else:
            return ""


class PhpNamespacelevel(PhpObject):
    """
    Description of an object on namespace level (functions, constants).
    """

    def needs_arglist(self):
        return self.objtype == "function"

    def get_signature_prefix(self, sig):
        """
        Adds class prefix for constants created inside classes
        """
        if self.objtype == "const":
            return _("constant ")
        if self.class_name and self.class_name != "":
            return self.class_name + "::"

    def get_index_text(self, namespace, name_cls):
        if self.objtype == "function":
            if not namespace:
                return _("%s() (global function)") % name_cls[0]
            return _("%s() (function in %s)") % (name_cls[0], namespace)
        elif self.objtype == "const" and self.class_name != "":
            return _("%s (class constant)") % (name_cls[0])
        elif self.objtype == "const":
            if not namespace:
                return _("%s (global constant)") % (name_cls[0])
            return _("%s (constant in %s)") % (name_cls[0], namespace)
        else:
            return ""


class PhpClasslike(PhpObject):
    """
    Description of a class-like object
    (classes, interfaces, traits, enums).
    """

    def get_signature_prefix(self, sig):
        return self.objtype + " "

    def get_index_text(self, namespace, name_cls):
        if self.objtype == "class":
            if not namespace:
                return _("%s (class)") % name_cls[0]
            return _("%s (class in %s)") % (name_cls[0], namespace)
        elif self.objtype == "interface":
            if not namespace:
                return _("%s (interface)") % name_cls[0]
            return _("%s (interface in %s)") % (name_cls[0], namespace)
        elif self.objtype == "trait":
            if not namespace:
                return _("%s (trait)") % name_cls[0]
            return _("%s (trait in %s)") % (name_cls[0], namespace)
        elif self.objtype == "enum":
            if not namespace:
                return _("%s (enum)") % name_cls[0]
            return _("%s (enum in %s)") % (name_cls[0], namespace)
        elif self.objtype == "exception":
            return name_cls[0]
        else:
            return ""

    def after_content(self):
        self.env.temp_data["php:in_class"] = False

    def before_content(self):
        self.env.temp_data["php:in_class"] = True
        if self.names:
            self.env.temp_data["php:class"] = self.names[0][0]


class PhpClassmember(PhpObject):
    """
    Description of a class member (methods, properties).
    """

    def get_signature_prefix(self, sig):
        if self.objtype == "attr":
            return _("property ")
        if self.objtype == "staticmethod":
            return _("static ")
        if self.objtype == "case":
            return _("case ")
        return ""

    def needs_arglist(self):
        return self.objtype == "method"

    def get_index_text(self, namespace, name_cls):
        name, cls = name_cls

        if (
            self.objtype.endswith("method")
            or self.objtype == "attr"
            or self.objtype == "case"
        ):
            try:
                clsname, propname = php_rsplit(name)
            except ValueError:
                propname = name
                clsname = None

        if self.objtype.endswith("method"):
            if namespace and clsname is None:
                return _("%s() (in namespace %s)") % (name, namespace)
            elif namespace and self.env.config.add_module_names:
                return _("%s() (%s\\%s method)") % (propname, namespace, clsname)
            else:
                return _("%s() (%s method)") % (propname, clsname)
        elif self.objtype == "attr":
            if namespace and clsname is None:
                return _("%s (in namespace %s)") % (name, namespace)
            elif namespace and self.env.config.add_module_names:
                return _("%s (%s\\%s property)") % (propname, namespace, clsname)
            else:
                return _("%s (%s property)") % (propname, clsname)
        elif self.objtype == "case":
            if namespace and clsname is None:
                return _("%s enum case") % (name)
            elif namespace and self.env.config.add_module_names:
                return _("%s (%s\\%s enum case)") % (propname, namespace, clsname)
            else:
                return _("%s (%s enum case)") % (propname, clsname)
        else:
            return ""


class PhpNamespace(Directive):
    """
    Directive to start a new PHP namespace, which is similar to module.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "synopsis": lambda x: x,
        "noindex": directives.flag,
        "deprecated": directives.flag,
    }

    def run(self):
        env = self.state.document.settings.env
        namespace = self.arguments[0].strip()
        noindex = "noindex" in self.options
        env.temp_data["php:namespace"] = namespace
        env.temp_data["php:class"] = None
        env.domaindata["php"]["namespaces"][namespace] = (
            env.docname,
            self.options.get("synopsis", ""),
            "deprecated" in self.options,
        )

        targetnode = nodes.target("", "", ids=["namespace-" + namespace], ismod=True)
        self.state.document.note_explicit_target(targetnode)
        ret = [targetnode]

        # the synopsis isn't printed; in fact, it is only used in the
        # modindex currently
        if not noindex:
            indextext = _("%s (namespace)") % namespace
            inode = addnodes.index(
                entries=[
                    ("single", indextext, "namespace-" + namespace, namespace, None)
                ]
            )
            ret.append(inode)
        return ret


class PhpCurrentNamespace(Directive):
    """
    This directive is just to tell Sphinx that we're documenting
    stuff in namespace foo, but links to namespace foo won't lead here.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env
        namespace = self.arguments[0].strip()
        if namespace == "None":
            env.temp_data["php:namespace"] = None
        else:
            env.temp_data["php:namespace"] = namespace
        return []


class PhpXRefRole(XRefRole):
    """
    Provides cross reference links for PHP objects
    """

    def process_link(self, env, refnode, has_explicit_title, title, target):
        if not has_explicit_title:
            if title.startswith("::"):
                title = title[2:]
            target = target.lstrip("~")  # only has a meaning for the title

            # If the first char is ~ don't display the leading namespace & class.
            if title.startswith("~"):
                m = re.search(r"(?:.+[:]{2}|(?:.*?\\{1,2})+)?(.*)\Z", title)
                if m:
                    title = m.group(1)

        refnode["php:namespace"] = env.temp_data.get("php:namespace")
        refnode["php:class"] = env.temp_data.get("php:class")

        return title, target


class PhpNamespaceIndex(Index):
    """
    Index subclass to provide the PHP namespace index.
    """

    name = "modindex"
    localname = _("PHP Namespace Index")
    shortname = _("namespaces")

    def generate(self, docnames=None):
        content = {}
        # list of prefixes to ignore
        ignores = self.domain.env.config["modindex_common_prefix"]
        ignores = sorted(ignores, key=len, reverse=True)
        # list of all namespaces, sorted by name
        namespaces = sorted(
            self.domain.data["namespaces"].items(), key=lambda x: x[0].lower()
        )
        # sort out collapsable namespaces
        prev_namespace = ""
        num_toplevels = 0
        for namespace, (docname, synopsis, deprecated) in namespaces:
            if docnames and docname not in docnames:
                continue

            for ignore in ignores:
                if namespace.startswith(ignore):
                    namespace = namespace[len(ignore) :]
                    stripped = ignore
                    break
            else:
                stripped = ""

            # we stripped the whole namespace name?
            if not namespace:
                namespace, stripped = stripped, ""

            entries = content.setdefault(namespace[0].lower(), [])

            package = namespace.split(NS)[0]
            if package != namespace:
                # it's a subnamespace
                if prev_namespace == package:
                    # first subnamespace - make parent a group head
                    entries[-1][1] = 1
                elif not prev_namespace.startswith(package):
                    # subnamespace without parent in list, add dummy entry
                    entries.append([stripped + package, 1, "", "", "", "", ""])
                subtype = 2
            else:
                num_toplevels += 1
                subtype = 0

            qualifier = deprecated and _("Deprecated") or ""
            entries.append(
                [
                    stripped + namespace,
                    subtype,
                    docname,
                    "namespace-" + stripped + namespace,
                    "",
                    qualifier,
                    synopsis,
                ]
            )
            prev_namespace = namespace

        # apply heuristics when to collapse modindex at page load:
        # only collapse if number of toplevel namespaces is larger than
        # number of subnamespaces
        collapse = len(namespaces) - num_toplevels < num_toplevels

        # sort by first letter
        content = sorted(content.items())

        return content, collapse


class PhpDomain(Domain):
    """
    PHP language domain.
    """

    name = "php"
    label = "PHP"
    object_types = {
        "function": ObjType(_("function"), "func", "obj"),
        "global": ObjType(_("global variable"), "global", "obj"),
        "const": ObjType(_("const"), "const", "obj"),
        "method": ObjType(_("method"), "meth", "obj"),
        "class": ObjType(_("class"), "class", "obj"),
        "attr": ObjType(_("attribute"), "attr", "obj"),
        "exception": ObjType(_("exception"), "exc", "obj"),
        "namespace": ObjType(_("namespace"), "ns", "obj"),
        "interface": ObjType(_("interface"), "interface", "obj"),
        "trait": ObjType(_("trait"), "trait", "obj"),
        "enum": ObjType(_("enum"), "enum", "obj"),
        "case": ObjType(_("case"), "case", "obj"),
    }

    directives = {
        "function": PhpNamespacelevel,
        "global": PhpGloballevel,
        "const": PhpNamespacelevel,
        "class": PhpClasslike,
        "method": PhpClassmember,
        "staticmethod": PhpClassmember,
        "attr": PhpClassmember,
        "case": PhpClassmember,
        "exception": PhpClasslike,
        "interface": PhpClasslike,
        "trait": PhpClasslike,
        "enum": PhpClasslike,
        "namespace": PhpNamespace,
        "currentmodule": PhpCurrentNamespace,
        "currentnamespace": PhpCurrentNamespace,
    }

    roles = {
        "func": PhpXRefRole(fix_parens=False),
        "global": PhpXRefRole(),
        "class": PhpXRefRole(),
        "exc": PhpXRefRole(),
        "meth": PhpXRefRole(fix_parens=False),
        "attr": PhpXRefRole(),
        "const": PhpXRefRole(),
        "ns": PhpXRefRole(),
        "obj": PhpXRefRole(),
        "interface": PhpXRefRole(),
        "trait": PhpXRefRole(),
        "enum": PhpXRefRole(),
        "case": PhpXRefRole(),
    }

    initial_data = {
        "objects": {},  # fullname -> docname, objtype
        "namespaces": {},  # namespace -> docname, synopsis
    }
    indices = [
        PhpNamespaceIndex,
    ]

    def clear_doc(self, docname):
        for fullname, (fn, _l) in list(self.data["objects"].items()):
            if fn == docname:
                del self.data["objects"][fullname]
        for ns, (fn, _x, _x) in list(self.data["namespaces"].items()):
            if fn == docname:
                del self.data["namespaces"][ns]

    def merge_domaindata(self, docnames, otherdata):
        for fullname, (fn, objtype) in otherdata["objects"].items():
            if fn in docnames:
                self.data["objects"][fullname] = (fn, objtype)
        for namespace, data in otherdata["namespaces"].items():
            if data[0] in docnames:
                self.data["namespaces"][namespace] = data

    def resolve_any_xref(self, env, fromdocname, builder, target, node, contnode):
        for typ in self.roles:
            resolve = self.resolve_xref(
                env, fromdocname, builder, typ, target, node, contnode
            )
            if resolve:
                return [("php:%s" % typ, resolve)]
        return []

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):
        if typ == "ns" or typ == "obj" and target in self.data["namespaces"]:
            docname, synopsis, deprecated = self.data["namespaces"].get(
                target, ("", "", "")
            )
            if not docname:
                return None
            else:
                title = "%s%s" % (synopsis, (deprecated and " (deprecated)" or ""))
                return make_refnode(
                    builder,
                    fromdocname,
                    docname,
                    "namespace-" + target,
                    contnode,
                    title,
                )
        else:
            namespace = node.get("php:namespace")
            clsname = node.get("php:class")
            searchorder = node.hasattr("refspecific") and 1 or 0
            name, obj = self.find_obj(
                env, node, namespace, clsname, target, typ, searchorder
            )
            if not obj:
                return None
            else:
                return make_refnode(builder, fromdocname, obj[0], name, contnode, name)

    def find_obj(
        self, env, fromdocnode, namespace, classname, name, type, searchorder=0
    ):
        """
        Find a PHP object for "name", using the given namespace and classname.
        """
        # strip parenthesis
        if name[-2:] == "()":
            name = name[:-2]

        if not name:
            return None, None

        objects = self.data["objects"]

        newname = None
        if searchorder == 1:
            if (
                namespace
                and classname
                and namespace + NS + classname + "::" + name in objects
            ):
                newname = namespace + NS + classname + "::" + name
            elif namespace and namespace + NS + name in objects:
                newname = namespace + NS + name
            elif namespace and namespace + NS + name in objects:
                newname = namespace + NS + name
            elif classname and classname + "::" + name in objects:
                newname = classname + "." + name
            elif classname and classname + "::$" + name in objects:
                newname = classname + "::$" + name
            elif name in objects:
                newname = name
        else:
            if name in objects:
                newname = name
            elif classname and classname + "::" + name in objects:
                newname = classname + "::" + name
            elif classname and classname + "::$" + name in objects:
                newname = classname + "::$" + name
            elif namespace and namespace + NS + name in objects:
                newname = namespace + NS + name
            elif (
                namespace
                and classname
                and namespace + NS + classname + "::" + name in objects
            ):
                newname = namespace + NS + classname + "::" + name
            elif (
                namespace
                and classname
                and namespace + NS + classname + "::$" + name in objects
            ):
                newname = namespace + NS + classname + "::$" + name
            # special case: object methods
            elif (
                type in ("func", "meth")
                and "::" not in name
                and "object::" + name in objects
            ):
                newname = "object::" + name
        if newname is None:
            return None, None
        return newname, objects[newname]

    def get_objects(self):
        for ns, info in self.data["namespaces"].items():
            yield (ns, ns, "namespace", info[0], "namespace-" + ns, 0)
        for refname, (docname, type) in self.data["objects"].items():
            yield (refname, refname, type, docname, refname, 1)


def setup(app):
    app.add_domain(PhpDomain)

    return {"version": sphinx_version, "parallel_read_safe": True}
