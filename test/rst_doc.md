```{eval-rst}
Acceptance tests for PHPdomain
##############################

Globals
=======

.. php:global:: $global_var

    A global variable

.. php:const:: SOME_CONSTANT

    A global constant

.. php:const:: VALUE

    A global constant

.. php:function:: in_array(needle, haystack)

    Checks for needle in haystack.

    :param needle: The element to search for.
    :param array haystack: The array to search.
    :returns: Element exists in array.
    :returntype: bool

Classes
=======

.. php:class:: DateTime

    Datetime class

    .. php:method:: setDate($year, $month, $day)

        Set the date in the datetime object

        :param int $year: The year.
        :param int $month: The month.
        :param int $day: The day.

    .. php:method:: setTime($hour, $minute[, $second])

        Set the time

        :param int $hour: The hour
        :param int $minute: The minute
        :param int $second: The second

    .. php:method:: public static getLastErrors()

        Returns the warnings and errors

        :returns: array Returns array containing info about warnings and errors.

    .. php:const:: ATOM

        Y-m-d\TH:i:sP

    .. php:property:: testprop

        Value of some property

.. php:class:: OtherClass

    Another class

.. php:method:: update($arg = '', $arg2 = [], $arg3 = [])

    Update something.

.. php:property:: nonIndentedProperty

    This property wasn't indented

.. php:const:: NO_INDENT

    This class constant wasn't indented

.. php:method:: OtherClass2::update($arg = '')

    A method without explicitly declared class block.

Interfaces
==========

.. php:interface:: DateTimeInterface

    Datetime interface

    .. php:method:: setDate($year, $month, $day)

        Set the date in the datetime object

        :param int $year: The year.
        :param int $month: The month.
        :param int $day: The day.

    .. php:method:: setTime($hour, $minute[, $second])

        Set the time

        :param int $hour: The hour
        :param int $minute: The minute
        :param int $second: The second

    .. php:const:: ATOM

        Y-m-d\TH:i:sP

    .. php:property:: testprop

        Value of some property

.. php:interface:: OtherInterface

    Another interface

Traits
======

.. php:trait:: LogTrait

    A logging trait

    .. php:method:: log($level, $string)

        A method description.

More globals after classes
==========================

.. php:global:: $other_global_var

    A global variable

.. php:function:: strpos($needle, $haystack)

    Position of needle in haystack


Test Case - Global symbols with no namespaces
---------------------------------------------

:php:global:`$global_var`

:php:global:`$other_global_var`

:php:const:`SOME_CONSTANT`

:php:function:`in_array`

:php:function:`strpos`

:php:class:`DateTime`

:php:method:`DateTime::setTime()`

:php:method:`DateTime::getLastErrors()`

:php:method:`DateTime::setDate()`

:php:const:`DateTime::ATOM`

:php:property:`DateTime::$testprop`

:php:method:`OtherClass::update`

:php:property:`OtherClass::$nonIndentedProperty`

:php:const:`OtherClass::NO_INDENT`

:php:method:`OtherClass2::update()`

:php:interface:`DateTimeInterface`

:php:method:`DateTimeInterface::setTime()`

:php:method:`~DateTimeInterface::setDate()`

:php:const:`DateTimeInterface::ATOM`

:php:property:`DateTimeInterface::$testprop`

:php:interface:`OtherInterface`

:php:trait:`LogTrait`

:php:method:`LogTrait::log()`

Test Case - Prefix less links
-----------------------------

The following links should not be prefixed with a classname.

:php:method:`~DateTime::setDate()`

:php:property:`~DateTime::$testprop`


Namespaced elements
===================

.. php:namespace:: LibraryName

.. php:function:: namespaced_function($one[, $two])

    A function in a namespace

    :param string $one: First parameter.
    :param string $two: Second parameter.

.. php:const:: NS_CONST

       A constant in a namespace

.. php:class:: LibraryClass

    A class in a namespace

    .. php:method:: LibraryClass::instanceMethod($foo)

        An instance method

    .. php:const:: TEST_CONST

        Test constant

    .. php:property:: property

        A property!

.. php:class:: NamespaceClass

    A class in the namespace, no indenting on children

.. php:method:: firstMethod($one, $two)

    A normal instance method.

.. php:property:: property

    A property

.. php:const:: NAMESPACE_CONST

    Const on class in namespace

.. php:method:: NamespaceClass2::update($foo)

    A method without explicitly declared class block in a namespace

.. php:class:: final LibraryClassFinal

    A final class

.. php:method:: public firstMethod($one, $two)

    A public instance method.

.. php:method:: protected secondMethod($one, $two)

    A protected instance method.

.. php:method:: private thirdMethod($one, $two)

    A private instance method.

.. php:method:: static fourthMethod($one, $two)

    A static method.

.. php:method:: protected final fifthMethod($one, $two)

    A protected final method.

.. php:class:: abstract LibraryClassAbstract

    An abstract class

.. php:interface:: LibraryInterface

    A interface in a namespace

    .. php:method:: instanceMethod($foo)

    An instance method

.. php:trait:: TemplateTrait

    A trait in a namespace

    .. php:method:: render($template)

    Render a template.


Test Case - not including namespace
-----------------------------------

Within a namespace context you don't need to include the namespace in links.

:php:namespace:`LibraryName`

:php:function:`namespaced_function()`

:php:const:`NS_CONST`

:php:class:`LibraryClass`

:php:function:`LibraryClass::instanceMethod`

:php:property:`LibraryClass::$property`

:php:const:`LibraryClass::TEST_CONST`

:php:class:`OtherClass`

:php:class:`NamespaceClass`

:php:function:`NamespaceClass::firstMethod`

:php:property:`NamespaceClass::$property`

:php:const:`NamespaceClass::NAMESPACE_CONST`

:php:method:`NamespaceClass2::update()`

:php:class:`LibraryClassFinal`

:php:method:`LibraryClassFinal::firstMethod`

:php:method:`LibraryClassFinal::secondMethod`

:php:method:`LibraryClassFinal::thirdMethod`

:php:method:`LibraryClassFinal::fourthMethod`

:php:method:`LibraryClassFinal::fifthMethod`

:php:interface:`LibraryInterface`

:php:function:`LibraryInterface::instanceMethod`

:php:trait:`TemplateTrait`

:php:method:`TemplateTrait::render()`

Test Case - Links with prefix trimming
--------------------------------------

All of the following links should not be prefixed with a namespace.

:php:interface:`~LibraryInterface`

:php:class:`~LibraryClass`

:php:trait:`~TemplateTrait`

All of the following links should not be prefixed with a classname.

:php:function:`~LibraryClass::instanceMethod`

:php:const:`~LibraryClass::TEST_CONST`

:php:property:`~LibraryClass::$property`


Test Case - global access
-------------------------

:php:class:`\\DateTime`

:php:function:`\\DateTime::setTime()`

:php:global:`$global_var`

:php:const:`SOME_CONSTANT`

:php:function:`in_array()`

:php:property:`\\LibraryName\\LibraryClass::$property`

:php:property:`~\\LibraryName\\LibraryClass::$property` Should not be prefixed with classname.

:php:const:`\\LibraryName\\LibraryClass::TEST_CONST`

:php:const:`\\LibraryName\\NS_CONST`

:php:interface:`\\DateTimeInterface`

:php:function:`\\DateTimeInterface::setTime()`

Any Cross Ref
=============

:any:`LibraryName\\NS_CONST`

:any:`DateTimeInterface::setTime()`

Nested namespaces
=================

.. php:namespace:: LibraryName\SubPackage

.. php:class:: SubpackageClass

    A class in a subpackage

.. php:interface:: SubpackageInterface

    A class in a subpackage

Test Case - Test subpackage links
---------------------------------

:php:namespace:`LibraryName\\SubPackage`

:php:namespace:`\\LibraryName\\SubPackage`

:php:class:`SubpackageClass`

:php:class:`\\LibraryName\\SubPackage\\SubpackageClass`

:php:interface:`SubpackageInterface`

:php:class:`\\LibraryName\\SubPackage\\SubpackageInterface`

Return Types
============

.. php:namespace:: OtherLibrary

.. php:class:: ReturningClass

    A class to do some returning.

    .. php:method:: returnClassFromSameNamespace()

        :returns: An object instance of a class from the same namespace.
        :returntype: ReturnedClass

    .. php:method:: returnClassFromOtherNamespace()

        :returns: An object instance of a class from another namespace.
        :returntype: \\LibraryName\\SubPackage\\SubpackageInterface

    .. php:method:: returnClassConstant()

        :returns: The value of a specific class constant.
        :returntype: \\LibraryName\\NamespaceClass::NAMESPACE_CONST

    .. php:method:: returnGlobalConstant()

        :returns: The value of a specific global constant. # TODO link is not working without "\\"
        :returntype: SOME_CONSTANT

    .. php:method:: returnScalarType()

        :returns: A scalar string type.
        :returntype: string

    .. php:method:: returnUnionType()

        :returns: Any of a whole bunch of things specified with a PHP 8 union type.
        :returntype: int|string|ReturnedClass|\\LibraryName\\SubPackage\\SubpackageInterface|null

.. php:class:: ReturnedClass

    A class to return.

Enums
=====

Basic Enumerations
------------------

.. php:namespace:: Example\Basic

.. php:enum:: Suit

    In playing cards, a suit is one of the categories into which the cards of a
    deck are divided.

    .. php:case:: Hearts
    .. php:case:: Diamonds
    .. php:case:: Clubs
    .. php:case:: Spades

Backed Enumerations
-------------------

.. php:namespace:: Example\Backed

.. php:enum:: Suit : string

    In playing cards, a suit is one of the categories into which the cards of a
    deck are divided.

    .. php:case:: Hearts : 'H'
    .. php:case:: Diamonds : 'D'
    .. php:case:: Clubs : 'C'
    .. php:case:: Spades : 'S'

Advanced Enumerations
---------------------

.. php:namespace:: Example\Advanced

.. php:enum:: Suit : string

    In playing cards, a suit is one of the categories into which the cards of a
    deck are divided.

    .. php:case:: Hearts : 'H'
    .. php:case:: Diamonds : 'D'
    .. php:case:: Clubs : 'C'
    .. php:case:: Spades : 'S'

    .. php:method:: color() -> string

        Returns "red" for hearts and diamonds, "black" for clubs and spades.

    .. php:method:: static values() -> string[]

        Returns an array of the values of all the cases on this enum.

    .. php:const:: Roses() : Hearts

        An alias for :php:case:`Suit::Hearts`.

    .. php:const:: Bells : Diamonds

        An alias for :php:case:`Suit::Diamonds`.

    .. php:const:: Acorns : Clubs

        An alias for :php:case:`Suit::Clubs`.

    .. php:const:: Shields : Spades

        An alias for :php:case:`Suit::Spades`.

Enumeration Links
-----------------

Links to Basic Enumeration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:php:enum:`\\Example\\Basic\\Suit`

:php:case:`\\Example\\Basic\\Suit::Hearts`

:php:case:`\\Example\\Basic\\Suit::Diamonds`

:php:case:`\\Example\\Basic\\Suit::Clubs`

:php:case:`\\Example\\Basic\\Suit::Spades`

Links to Backed Enumeration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:php:enum:`\\Example\\Backed\\Suit`

:php:case:`\\Example\\Backed\\Suit::Hearts`

:php:case:`\\Example\\Backed\\Suit::Diamonds`

:php:case:`\\Example\\Backed\\Suit::Clubs`

:php:case:`\\Example\\Backed\\Suit::Spades`

Links to Advanced Enumeration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:php:enum:`Suit`

:php:case:`Suit::Hearts`

:php:case:`Suit::Diamonds`

:php:case:`Suit::Clubs`

:php:case:`Suit::Spades`

:php:method:`Suit::color`

:php:method:`Suit::values`

:php:const:`Suit::Roses`

:php:const:`Suit::Bells`

:php:const:`Suit::Acorns`

:php:const:`Suit::Shields`
```
