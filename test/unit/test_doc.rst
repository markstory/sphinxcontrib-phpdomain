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
    :returntype: boolean

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

        Set the time. See :php:func:`setDate()` for changing the date.

        :param int $hour: The hour
        :param int $minute: The minute
        :param int $second: The second

    .. php:method:: public static getLastErrors()

        Returns the warnings and errors

        :returns: array Returns array containing info about warnings and errors.

    .. php:const:: ATOM

        Y-m-d\TH:i:sP

    .. php:attr:: testattr

        Value of some attribute

.. php:class:: OtherClass

    Another class

.. php:method:: update($arg = '', $arg2 = [], $arg3 = [])

    Update something.

.. php:attr:: nonIndentedAttribute

    This attribute wasn't indented

.. php:const:: NO_INDENT

    This class constant wasn't indented

.. php:staticmethod:: OtherClass::staticMethod()

    A static method.

Exceptions
==========

.. php:exception:: InvalidArgumentException

    Throw when you get an argument that is bad.

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

    .. php:attr:: testattr

        Value of some attribute

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

.. php:global:: strpos($needle, $haystack)

    Position of needle in haystack


Test Case - Global symbols with no namespaces
---------------------------------------------

:php:global:`$global_var`

:php:global:`$other_global_var`

:php:const:`SOME_CONSTANT`

:php:func:`in_array`

:php:func:`strpos`

:php:class:`DateTime`

:php:func:`DateTime::setTime()`

:php:func:`DateTime::getLastErrors()`

:php:func:`DateTime::setDate()`

:php:func:`DateTime::ATOM`

:php:func:`DateTime::$testattr`

:php:func:`OtherClass::update`

:php:attr:`OtherClass::$nonIndentedAttribute`

:php:const:`OtherClass::NO_INDENT`

:php:func:`OtherClass::staticMethod`

:php:exc:`InvalidArgumentException`

:php:interface:`DateTimeInterface`

:php:func:`DateTimeInterface::setTime()`

:php:func:`~DateTimeInterface::setDate()`

:php:func:`DateTimeInterface::ATOM`

:php:func:`DateTimeInterface::$testattr`

:php:func:`OtherInterface`

:php:trait:`LogTrait`

:php:func:`LogTrait::log()`

Test Case - Prefix less links
-----------------------------

The following links should not be prefixed with a classname.

:php:func:`~DateTime::setDate()`

:php:attr:`~DateTime::$testattr`


Namespaced elements
===================

.. php:namespace:: LibraryName

.. php:function:: namespaced_function($one[, $two])

    A function in a namespace

    :param string $one: First parameter.
    :param string $two: Second parameter.

.. php:const:: NS_CONST

       A constant in a namespace

.. php:exception:: NamespaceException

    This exception is in a namespace.

.. php:class:: LibraryClass

    A class in a namespace

    .. php:method:: LibraryClass::instanceMethod($foo)

        An instance method

    .. php:const:: TEST_CONST

        Test constant

    .. php:attr:: property

        A property!

.. php:staticmethod:: LibraryClass::staticMethod()

    A static method in a namespace

.. php:class:: NamespaceClass

    A class in the namespace, no indenting on children

.. php:method:: firstMethod($one, $two)

    A normal instance method.

.. php:attr:: property

    A property

.. php:const:: NAMESPACE_CONST

    Const on class in namespace

.. php:staticmethod:: namespaceStatic($foo)

    A static method here.

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

:php:ns:`LibraryName`

:php:func:`namespaced_function()`

:php:const:`NS_CONST`

:php:class:`LibraryClass`

:php:func:`LibraryClass::instanceMethod`

:php:func:`LibraryClass::staticMethod()`

:php:attr:`LibraryClass::$property`

:php:const:`LibraryClass::TEST_CONST`

:php:class:`LibraryName\\OtherClass`

:php:class:`LibraryName\\ThirdClass`

:php:class:`NamespaceClass`

:php:func:`NamespaceClass::firstMethod`

:php:attr:`NamespaceClass::$property`

:php:interface:`LibraryName\\LibraryInterface`

:php:exc:`LibraryName\\NamespaceException`

:php:trait:`TemplateTrait`

:php:trait:`LibraryName\\TemplateTrait`

:php:func:`LibraryName\\TemplateTrait::render()`

Test Case - Links with prefix trimming
--------------------------------------

All of the following links should not be prefixed with a namespace.

:php:interface:`~LibraryName\\LibraryInterface`

:php:class:`~LibraryName\\LibraryClass`

:php:trait:`~LibraryName\\TemplateTrait`

:php:exc:`~LibraryName\\NamespaceException`

All of the following links should not be prefixed with a classname.

:php:func:`~LibraryClass::instanceMethod`

:php:const:`~LibraryClass::TEST_CONST`

:php:attr:`~LibraryClass::$property`


Test Case - global access
-------------------------

:php:class:`DateTime`

:php:func:`DateTime::setTime()`

:php:global:`$global_var`

:php:const:`SOME_CONSTANT`

:php:const:`LibraryName\\LibraryClass::TEST_CONST`

:php:const:`LibraryName\\NS_CONST`

:php:interface:`DateTimeInterface`

:php:func:`DateTimeInterface::setTime()`

:php:attr:`LibraryName\\LibraryClass::$property`

Should not be prefixed with classname.

:php:attr:`~LibraryName\\LibraryClass::$property`


Any Cross Ref
=============

:any:`LibraryName\\NS_CONST`

:any:`DateTimeInterface::setTime()`

Nested namespaces
=================

.. php:namespace:: LibraryName\SubPackage

.. php:exception:: NestedNamespaceException

    In a package

.. php:class:: SubpackageClass

    A class in a subpackage

.. php:interface:: SubpackageInterface

    A class in a subpackage

Test Case - Test subpackage links
---------------------------------

:php:ns:`LibraryName\\SubPackage`

:php:class:`SubpackageClass`

:php:class:`LibraryName\\SubPackage\\SubpackageClass`

:php:interface:`SubpackageInterface`

:php:class:`LibraryName\\SubPackage\\SubpackageInterface`

:php:exc:`LibraryName\\SubPackage\\NestedNamespaceException`

:php:func:`LibraryName\\namespaced_function`

Return Types
============

.. php:namespace:: OtherLibrary

.. php:class:: ReturningClass

    A class to do some returning.

    .. php:method:: returnClassFromSameNamespace()

        :returns: An object instance of a class from the same namespace.
        :returntype: OtherLibrary\\ReturnedClass

    .. php:method:: returnClassFromOtherNamespace()

        :returns: An object instance of a class from another namespace.
        :returntype: LibraryName\\SubPackage\\SubpackageInterface

    .. php:method:: returnClassConstant()

        :returns: The value of a specific class constant.
        :returntype: LibraryName\\NamespaceClass::NAMESPACE_CONST

    .. php:method:: returnGlobalConstant()

        :returns: The value of a specific global constant.
        :returntype: SOME_CONSTANT

    .. php:method:: returnExceptionInstance()

        :returns: An instance of an exception.
        :returntype: InvalidArgumentException

    .. php:method:: returnScalarType()

        :returns: A scalar string type.
        :returntype: string

    .. php:method:: returnUnionType()

        :returns: Any of a whole bunch of things specified with a PHP 8 union type.
        :returntype: int|string|OtherLibrary\\ReturnedClass|LibraryName\\SubPackage\\SubpackageInterface|null

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

    .. php:staticmethod:: values() -> string[]

        Returns an array of the values of all the cases on this enum.

    .. php:const:: Roses() : Hearts

        An alias for :php:case:`Example\\Advanced\\Suit::Hearts`.

    .. php:const:: Bells : Diamonds

        An alias for :php:case:`Example\\Advanced\\Suit::Diamonds`.

    .. php:const:: Acorns : Clubs

        An alias for :php:case:`Example\\Advanced\\Suit::Clubs`.

    .. php:const:: Shields : Spades

        An alias for :php:case:`Example\\Advanced\\Suit::Spades`.

Enumeration Links
-----------------

Links to Basic Enumeration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:php:enum:`Example\\Basic\\Suit`

:php:case:`Example\\Basic\\Suit::Hearts`

:php:case:`Example\\Basic\\Suit::Diamonds`

:php:case:`Example\\Basic\\Suit::Clubs`

:php:case:`Example\\Basic\\Suit::Spades`

Links to Backed Enumeration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:php:enum:`Example\\Backed\\Suit`

:php:case:`Example\\Backed\\Suit::Hearts`

:php:case:`Example\\Backed\\Suit::Diamonds`

:php:case:`Example\\Backed\\Suit::Clubs`

:php:case:`Example\\Backed\\Suit::Spades`

Links to Advanced Enumeration Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:php:enum:`Example\\Advanced\\Suit`

:php:case:`Example\\Advanced\\Suit::Hearts`

:php:case:`Example\\Advanced\\Suit::Diamonds`

:php:case:`Example\\Advanced\\Suit::Clubs`

:php:case:`Example\\Advanced\\Suit::Spades`

:php:meth:`Example\\Advanced\\Suit::color`

:php:meth:`Example\\Advanced\\Suit::values`

:php:const:`Example\\Advanced\\Suit::Roses`

:php:const:`Example\\Advanced\\Suit::Bells`

:php:const:`Example\\Advanced\\Suit::Acorns`

:php:const:`Example\\Advanced\\Suit::Shields`
