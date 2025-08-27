import ast
import json
from pathlib import Path

schema = json.loads(Path('schema.json').read_text())


def generate_class_ast(class_name: str, fields: dict):
    return ast.ClassDef(
        name=class_name,
        bases=[],
        keywords=[],
        body=[],
        decorator_list=[]
    )

def schema_to_ast(schema):
    return [generate_class_ast(name, fields) for name, fields in schema.items()]


tree = ast.Module(body=schema_to_ast(schema), type_ignores=[])
tree = ast.fix_missing_locations(tree)

print(ast.unparse(tree))
