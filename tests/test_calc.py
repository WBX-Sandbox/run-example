import platform

import pytest

from calc import add, mean


def test_add():
    assert add(2, 3) == 5


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_runs_in_a_microvm():
    # the job runs on Linux inside a WBX Sandbox microVM, not on the GitHub runner
    assert platform.system() == "Linux"
