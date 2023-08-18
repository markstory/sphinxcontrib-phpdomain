Reference
#########

.. highlight:: rst

The PHP domain provides the following directives. 
Most directives are similar to Python's.

Directives
==========

Each directive populates the index, and or the namespace index.

.. rst:directive:: .. php:namespace:: name

   This directive declares a new PHP namespace.  It accepts nested
   namespaces by separating namespaces with ``\``.  It does not generate
   any content like :rst:dir:`php:class` does.  It will however, generate 
   an entry in the namespace/module index.
   
   It has ``synopsis`` and ``deprecated`` options, similar to :rst:dir:`py:module`
  
.. rst:directive:: .. php:global:: name

   This directive declares a new PHP global variable.

.. rst:directive:: .. php:function:: name(signature)

   Defines a new global/namespaced function outside of a class.  You can use 
   many of the same field lists as the python domain.  However, ``raises`` 
   is replaced with ``throws``

.. rst:directive:: .. php:const:: name

   This directive declares a new PHP constant, you can also used it nested 
   inside a class directive to create class constants.
   
.. rst:directive:: .. php:exception:: name

   This directive declares a new Exception in the current namespace. The 
   signature can include constructor arguments.

.. rst:directive:: .. php:interface:: name

   Describe an interface.  Methods and constants belonging to the interface 
   should follow or be nested inside this directive.

.. rst:directive:: .. php:trait:: name

   Describe a trait.  Methods beloning to the trait should follow or be nested
   inside this directive.

.. rst:directive:: .. php:enum:: name [ : type ]

   Describes an enum. Cases, methods, and constants belonging to the enum
   should be inside this directive's body::

        .. php:enum:: Suit

            In playing cards, a suit is one of the categories into which the
            cards of a deck are divided.

            .. php:case:: Hearts

                Hearts is one of the four suits in playing cards.

            .. php:case:: Diamonds

                Diamonds is one of the four suits in playing cards.

            .. php:case:: Clubs

                Clubs is one of the four suits in playing cards.

            .. php:case:: Spades

                Spades is one of the four suits in playing cards.

            .. php:method:: color() -> string

                Returns "Red" for hearts and diamonds and "black" for clubs
                and spades.

            .. php:const:: Roses : Hearts

                An alias for :php:case:`Suit::Hearts`.

   You may describe a backed enum by specifying the optional enum type and
   case values::

        .. php:enum:: Suit : string

            In playing cards, a suit is one of the categories into which the
            cards of a deck are divided.

            .. php:case:: Hearts : 'H'

            .. php:case:: Diamonds : 'D'

            .. php:case:: Clubs : 'C'

            .. php:case:: Spades : 'S'

.. rst:directive:: .. php:case:: name [ : value ]

   Describes an enum case. If describing a backed enum case, you may also
   provide the case value. See :rst:dir:`php:enum` for examples.

.. rst:directive:: .. php:class:: name

   Describes a class.  Methods, attributes, and constants belonging to the class
   should be inside this directive's body::

        .. php:class:: MyClass
        
            Class description
        
           .. php:method:: method($argument)
        
           Method description


   Attributes, methods and constants don't need to be nested.  They can also just 
   follow the class declaration::

        .. php:class:: MyClass
        
            Text about the class
        
        .. php:method:: methodName()
        
            Text about the method
        

   .. seealso:: :rst:dir:`php:method`
                :rst:dir:`php:attr`
                :rst:dir:`php:const`

.. rst:directive:: .. php:method:: name(signature)

   Describe a class method, its arguments, return value, and exceptions::
   
        .. php:method:: instanceMethod($one, $two)
        
            :param string $one: The first parameter.
            :param string $two: The second parameter.
            :returns: A description of what this returns.
            :returntype: LibraryName\\LibraryClass
            :throws: InvalidArgumentException
        
           This is an instance method.

.. rst:directive:: .. php:attr:: name

   Describe an property/attribute on a class.

Cross Referencing
=================

The following roles refer to php objects and are links are generated if a 
matching directive is found:

.. rst:role:: php:ns

   Reference a namespace. Nested namespaces need to be separated by two \\ due 
   to the syntax of ReST::
   
      .. php:ns:`LibraryName\\SubPackage` will work correctly.

.. rst:role:: php:func

   Reference a PHP function either in a namespace or out. If the function is in
   a namespace, be sure to include the namespace, unless you are currently 
   inside the same namespace.

.. rst:role:: php:global

   Reference a global variable whose name has ``$`` prefix.
   
.. rst:role:: php:const

   Reference either a global constant, or a class constant.  Class constants should
   be preceded by the owning class::
   
        DateTime has an :php:const:`DateTime::ATOM` constant.

.. rst:role:: php:class

   Reference a class; a name with namespace can be used. If you include a namespace,
   you should use following style::
   
     :php:class:`LibraryName\\ClassName`

.. rst:role:: php:meth

   Reference a method of a class/interface/trait::
   
     :php:meth:`DateTime::setDate`

.. rst:role:: php:attr

   Reference a property on an object::
   
      :php:attr:`ClassName::$propertyName`

.. rst:role:: php:exc

   Reference an exception.  A namespaced name may be used.

.. rst:role:: php:interface

   Reference an interface.  A namespaced name may be used.

.. rst:role:: php:trait

   Reference a trait. A namespaced name may be used.

.. rst:role:: php:enum

   Reference an enum. A namespaced name may be used::

     :php:enum:`Example\\Suit`

.. rst:role:: php:case

   Reference an enum case. A namespace name may be used::

     :php:case:`Example\\Suit::Hearts`
