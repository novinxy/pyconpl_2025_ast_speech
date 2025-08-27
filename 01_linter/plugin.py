import ast
from typing import NamedTuple


class ErrorInfo(NamedTuple):
    line_number: int
    offset: int
    msg: str
    cls: type


class PyConPlugin:
    name = 'pycon_plugin'
    version = '0.0.0'

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self):
        yield ErrorInfo(0, 0, "PC25001 Always fail on", type(self))
