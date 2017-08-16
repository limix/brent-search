from .bracket import bracket
from .brent import brent
from .optimize import minimize


def test():
    import os
    p = __import__('brent_search').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main(['-q', '--doctest-modules'])
    finally:
        os.chdir(old_path)

    if return_code == 0:
        print("Congratulations. All tests have passed!")

    return return_code


__all__ = ["test", "bracket", "brent", "minimize"]
