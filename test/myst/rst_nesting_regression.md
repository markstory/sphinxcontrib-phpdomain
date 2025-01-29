```{eval-rst}
Nested method Regression
========================

Test nested methods to ensure page generation doesn't hard fail.

.. php:method:: Largo_Byline::populate_variables()

      Set us up the vars

          - 'post_id': an integer post ID
          - 'exclude_date': boolean whether or not to include the date in the byline

      :param array $args: Associative array containing following keys:

   .. php:method:: Largo_Byline::generate_byline()

      this creates the byline text and adds it to $this->output

      :see: $output $reates this
```
