```{eval-rst}
Top Level Namespace
###################

namespace ``Imagine\Draw``

.. php:namespace:: Imagine\Draw

.. php:class:: DrawerInterface

Instance of this interface is returned by :php:meth:`\\Imagine\\Image\\ImageInterface::draw`.

.. php:method:: arc(PointInterface $center, BoxInterface $size, $start, $end, Color $color)

    Draws an arc on a starting at a given x, y coordinates under a given start and end angles

    :param \\Imagine\\Image\\PointInterface $center: Center of the arc. 
    :param \\Imagine\\Image\\BoxInterface $size: Size of the bounding box.
    :param int $start: Start angle.
    :param int $end: End angle.
    :param \\Imagine\\Image\\Color $color: Line color.

    :throws: \\Imagine\\Exception\\RuntimeException

    :returns: DrawerInterface

Re-used namespace
=================

.. php:currentmodule:: LibraryName

No indexing errors or links should point to this namespace.

.. php:class:: ThirdClass

    Another class in a currentmodule block

.. php:currentnamespace:: LibraryName

No indexing errors or links should point to this namespace.

.. php:class:: OtherClass

    Another class in a reused namespace
```
