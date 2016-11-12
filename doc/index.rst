Brent-search's documentation
============================

You can get the source and open issues `on Github.`_

.. toctree::
    :caption: Table of contents
    :name: mastertoc
    :maxdepth: 1

Install
-------

The recommended way of installing it is via `conda`_

.. code-block:: bash

  conda install -c conda-forge brent_search

An alternative way would be via pip

.. code-block:: bash

  pip install brent_search

Examples
--------

.. doctest::

  >>> from brent_search import bracket
  >>> def f(x):
  ...     return (x-2)**2
  >>>
  >>> bracket(f)
  ((1.2499997019767761, 2.499999701976776, 4.999999701976776, 0.5625004470349246, 0.24999970197686494, 8.999998211860746), 1)

Functions
---------

.. automodule:: brent_search

  .. autofunction:: bracket
  .. autofunction:: brent
  .. autofunction:: minimize

.. _on Github.: https://github.com/Horta/brent-search
.. _conda: http://conda.pydata.org/docs/index.html
