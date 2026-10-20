import runpy
from unittest.mock import patch


def test_main_entry_point():
    with patch("builtins.input", return_value="exit"):
        runpy.run_module("calculator", run_name="__main__")

def test_main_import():
    runpy.run_module("calculator.__main__", run_name="calculator.__main__")