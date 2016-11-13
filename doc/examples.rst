Examples
--------

.. doctest::

  >>> from brent_search import bracket
  >>> def f(x):
  ...     return (x-2)**2
  >>>
  >>> bracket(f)
  ((1.2499997019767761, 2.499999701976776, 4.999999701976776, 0.5625004470349246, 0.24999970197686494, 8.999998211860746), 1)