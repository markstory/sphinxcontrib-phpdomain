# Simple NS

:::{php:namespace} Foo
:::

:::{php:class} A
:::

:::{php:method} simplify()
:::

## Cross linking

- {php:meth}`A::simplify`

# NS can be changed

:::{php:namespace} Foo\Bar
:::

:::{php:class} A
:::

:::{php:method} simplify()
:::

:::{php:namespace} Bar
:::

:::{php:class} A
:::

:::{php:method} simplify()
:::

## Cross linking

- {php:meth}`A::simplify`
- {php:meth}`\Foo\Bar\A::simplify`
- {php:meth}`\Bar\A::simplify`

# NS must not be guessed

:::note
These cross references must not have a link as the target methods are not defined.
:::

- {php:meth}`\A2::simplify`

:::{php:namespace} Bar2
:::

- {php:meth}`A::simplify`
