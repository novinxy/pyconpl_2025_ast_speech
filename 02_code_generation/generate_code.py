import ast
import json
from pathlib import Path

schema = json.loads(Path('schema.json').read_text())


def generate_class_ast(class_name: str, fields: dict):
    body = []
    for name, type_ in fields.items():
        column = ast.AnnAssign(
                target=ast.Name(id=name),
                annotation=ast.Subscript(value=ast.Name(id='Mapped'), slice=ast.Name(id=type_)),
                simple=1
            )
        if name == 'id':
            column.value = ast.Call(
                func=ast.Name(id='mapped_column'),
                args=[],
                keywords=[ast.keyword(arg='Primary_key', value=ast.Constant(value=True)),]
            )

        body.append(column)

    return ast.ClassDef(
        name=class_name,
        bases=[ast.Name(id='Base')],
        keywords=[],
        body=body,
        decorator_list=[]
    )


def schema_to_ast(schema):
    return [generate_class_ast(name, fields) for name, fields in schema.items()]


tree = ast.Module(body=schema_to_ast(schema), type_ignores=[])
tree = ast.fix_missing_locations(tree)

print(ast.unparse(tree))
