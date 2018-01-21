============================
Brent-search's documentation
============================

:Date: |today|
:Version: |version|

You can get the source and open issues `on Github.`_

.. _on Github.: https://github.com/limix/brent-search

-------
Install
-------

The recommended way of installing it is via `conda`_

.. code-block:: bash

  conda install -c conda-forge brent-search

An alternative way would be via pip

.. code-block:: bash

  pip install brent-search

.. _conda: http://conda.pydata.org/docs/index.html

--------
Examples
--------

.. doctest::

  >>> from brent_search import bracket
  >>> def f(x):
  ...     return (x-2)**2
  >>>
  >>> (x0, x1, x2, f0, f1, f2), e = bracket(f)
  >>> print("{:.2f}".format(x0))
  1.25
  >>> print("{:.2f}".format(x1))
  2.50
  >>> print("{:.2f}".format(x2))
  5.00
  >>> print("{:.2f}".format(f0))
  0.56
  >>> print("{:.2f}".format(f1))
  0.25
  >>> print("{:.2f}".format(f2))
  9.00

Functions
---------

.. automodule:: brent_search

  .. autofunction:: bracket
  .. autofunction:: brent
  .. autofunction:: minimize
