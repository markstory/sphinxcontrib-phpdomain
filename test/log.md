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

- {php:method}`Foo\A::simplifyy`

:::{php:namespace} Foo
:::

- {php:method}`Foo\A::simplify`

:::{php:namespace} Fooo
:::

- {php:method}`Foo\A::simplify`
