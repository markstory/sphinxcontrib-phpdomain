# Simple NS

:::{php:namespace} Foo
:::

:::{php:class} A
:::

:::{php:method} simplify()
:::

## Cross linking

- {php:method}`A::simplify`

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

- {php:method}`A::simplify`
- {php:method}`\Foo\Bar\A::simplify`
- {php:method}`\Bar\A::simplify`

# Leading `\` implies absolute class name

:::{php:class} \A
:::

:::{php:method} simplify()
:::

:::{php:class} A2
:::

:::{php:method} simplify()
:::

## Cross linking

- {php:meth}`A::simplify`
- {php:meth}`\A::simplify`
- {php:meth}`A2::simplify`
- {php:meth}`\Bar\A2::simplify`

# NS must not be guessed

:::note
These cross references must not have a link as the target methods are not defined.
:::

- {php:method}`\A2::simplify`

:::{php:namespace} Bar2
:::

- {php:method}`A::simplify`
