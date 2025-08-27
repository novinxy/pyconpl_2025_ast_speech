from pathlib import Path
import ast

class Visitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node: ast.FunctionDef):
        for default in node.args.defaults:
            if isinstance(default, ast.List):
                print("Do not use List for default arguments")

        self.generic_visit(node)


source_code = Path('code_with_problems.py').read_text()
node = ast.parse(source_code)

Visitor().visit(node)
