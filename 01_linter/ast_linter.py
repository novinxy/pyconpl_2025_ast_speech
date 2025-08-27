from pathlib import Path
import ast

class Visitor(ast.NodeVisitor):
    def visit(self, node: ast.AST):
        self.generic_visit(node)


source_code = Path('code_with_problems.py').read_text()
node = ast.parse(source_code)

Visitor().visit(node)
