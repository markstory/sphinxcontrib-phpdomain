# Invalid domain type

:::{php:namespacee} Foo
:::

# In-class type without class

:::{php:method} x()
:::

# Not In-class type with class

:::{php:class} A::A
:::

# Invalid signature

:::{php:method} x();
:::

# Unresolved references

- {php:class}`Foo\Aa`

- {php:meth}`Foo\A::simplifyy`

:::{php:namespace} Foo
:::

- {php:meth}`Foo\A::simplify`

:::{php:namespace} Fooo
:::

- {php:meth}`Foo\A::simplify`
