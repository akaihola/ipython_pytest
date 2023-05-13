import os
import shlex
import sys
from argparse import ArgumentParser
from contextlib import nullcontext
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import ContextManager, List, Tuple, cast

from IPython.core import magic
from pytest import main as pytest_main

TEST_MODULE_NAME = '_ipytesttmp'


def parse_arguments(line: str) -> Tuple[str, List[str]]:
    parser = ArgumentParser()
    parser.add_argument("path", nargs="?")
    args, unknown = parser.parse_known_args(shlex.split(line))
    return args.path, unknown


def pytest(line: str, cell: str) -> None:
    path, unknown_args = parse_arguments(line)
    working_directory = (
        nullcontext(path) if path else cast(ContextManager[str], TemporaryDirectory())
    )
    with working_directory as root:
        oldcwd = os.getcwd()
        os.chdir(root)
        tests_module_path = '{}.py'.format(TEST_MODULE_NAME)
        try:
            Path(tests_module_path).write_text(cell)
            os.environ['COLUMNS'] = '80'
            pytest_main(unknown_args + [tests_module_path])
            if TEST_MODULE_NAME in sys.modules:
                del sys.modules[TEST_MODULE_NAME]
        finally:
            os.chdir(oldcwd)


def load_ipython_extension(ipython):
    magic.register_cell_magic(pytest)
