# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest
.PHONY: comparehtml

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean      clean up test build artifacts"
	@echo "  html       to make standalone HTML files"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  comparehtml compare build/html with snapshots (for test regressions)"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."


# get all test cases
test_sources = $(shell find . -name '*.rst')
# replace .rst with .html
test_html = $(notdir $(test_sources:.rst=.html))

$(BUILDDIR)/html/%.result: $(BUILDDIR)/html/%
	# create 'result' xml files from the generated html, but only capture role=main
	# to keep fixtures easier to manage.
	xmllint $(BUILDDIR)/html/$* --xpath '//div[@role="main"]' | xmllint --format - > $(BUILDDIR)/html/$*.result

compareresult-%:
	# compare test_doc.html and test_doc.html.result
	diff -u $* $(BUILDDIR)/html/$*.result

# generate dependency lists to contain iteration
generateresults: $(foreach build_html, $(test_html), $(BUILDDIR)/html/$(build_html).result)
compareresults: $(foreach build_html, $(test_html), compareresult-$(build_html))

# run from ci tooling
comparehtml: generateresults compareresults

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."
