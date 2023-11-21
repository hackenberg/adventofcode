import pytest


def skip(*values): return pytest.param(*values, marks=pytest.mark.skip)
def xfail(*values): return pytest.param(*values, marks=pytest.mark.xfail)


