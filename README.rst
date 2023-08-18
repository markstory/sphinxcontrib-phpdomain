PHP Domain for Sphinx
#####################

:author: Mark Story <mark at mark-story.com>
:author: Michael Voříšek

About
=====

A domain for sphinx >= 1.3 that provides language support for PHP.

PHP Domain supports following objects:

* Global variable
* Global function
* Constant
* Namespace

  * Function
  * Class

* Class

  * Class constant
  * Instance methods
  * Static methods
  * Properties

.. note::

   This domain expresses methods and attribute names like this::

      Class::method_name
      Class::$attribute_name

   You address classes/functions in namespaces using \\ syntax as you would in PHP::

        Package\Subpackage\Class

See `Usage Example`_ in the documentation for information about how to use it.

.. _`Usage Example`: https://markstory.github.io/sphinxcontrib-phpdomain/usage.html

URLs
====

:PyPI: https://pypi.python.org/pypi/sphinxcontrib-phpdomain
:Documentation: https://markstory.github.io/sphinxcontrib-phpdomain/

Install
=======

You can install the phpdomain using pip::

   pip install -U sphinxcontrib-phpdomain

