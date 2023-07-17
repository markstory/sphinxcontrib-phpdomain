Simple NS
=========

.. php:namespace:: Foo

.. php:method:: X::simplify()

.. php:class:: A

.. php:method:: simplify()

Cross linking::

- :php:meth:`X::simplify`
- :php:meth:`A::simplify`

NS can be redeclared
====================

.. php:namespace:: Foo\Bar

.. php:method:: X::simplify()

.. php:class:: A

.. php:method:: simplify()

.. php:namespace:: Bar

.. php:class:: A

.. php:method:: simplify()

Cross linking::

- :php:meth:`X::simplify`
- :php:meth:`A::simplify`

Leading ``\`` implies absolute class name
=========================================

.. php:method:: \X::simplify()

.. php:method:: X2::simplify()

.. php:class:: \A

.. php:method:: simplify()

.. php:class:: A2

.. php:method:: simplify()

Cross linking::

- :php:meth:`X::simplify`
- :php:meth:`A::simplify`

- :php:meth:`\X::simplify`
- :php:meth:`\A::simplify`

- :php:meth:`X2::simplify`
- :php:meth:`A2::simplify`
