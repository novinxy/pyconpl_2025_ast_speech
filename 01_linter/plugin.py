import ast
from typing import NamedTuple


class ErrorInfo(NamedTuple):
    line_number: int
    offset: int
    msg: str
    cls: type


class Visitor(ast.NodeVisitor):

    def __init__(self) -> None:
        self.errors: list[ErrorInfo] = []

    def visit_FunctionDef(self, node: ast.FunctionDef):
        for default in node.args.defaults:
            if isinstance(default, ast.List):
                self.errors.append(
                    ErrorInfo(node.lineno, node.col_offset,  "PC25001 Always fail on", type(self))
                    )

        self.generic_visit(node)


class PyConPlugin:
    name = 'pycon_plugin'
    version = '0.0.0'

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self):
        visitor = Visitor()
        visitor.visit(self._tree)

        yield from visitor.errors
