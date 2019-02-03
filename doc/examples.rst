Examples
========

Often the first step of a function optimisation is to find an interval within which a
solution is believed to exist.
The following example shows how :func:`brent_search.bracket` can be used to attain that
task.

.. doctest::

  >>> from brent_search import bracket
  >>> def f(x):
  ...     return (x-2)**2
  >>>
  >>> (x0, x1, x2, f0, f1, f2), e = bracket(f)
  >>> print("Left point: {:.2f}".format(x0))
  Left point: 1.25
  >>> print("Best point: {:.2f}".format(x1))
  Best point: 2.50
  >>> print("Right point: {:.2f}".format(x2))
  Right point: 5.00
  >>> print("{:.2f}".format(f0))
  0.56
  >>> print("{:.2f}".format(f1))
  0.25
  >>> print("{:.2f}".format(f2))
  9.00

The :func:`brent_search.brent` function can then be applied to find a minimum within
the interval.

.. doctest::

  >>> from brent_search import brent
  >>> (x, fx, exit_code) = brent(f, x0, x2, x1, f1)
  >>> print("({:.1f}, {:.1f}, {})".format(x, fx, exit_code))
  (2.0, 0.0, 6)

