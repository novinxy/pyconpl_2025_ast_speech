import ast


# say_hello = lambda: print("Hello world")

generated_function = ast.Module(
    body=[
        ast.Assign(
            targets=[ast.Name(id="say_hello", ctx=ast.Store())],
            value=ast.Lambda(
                args=ast.arguments(
                    posonlyargs=[],
                    args=[],
                    kwonlyargs=[],
                    kw_defaults=[],
                    defaults=[]
                ),
                body=ast.Call(
                    func=ast.Name(id="print", ctx=ast.Load()),
                    args=[
                        ast.Constant(value="Hello world")
                    ],
                    keywords=[]
                ),
            ),
        ),
    ],
    type_ignores=[],
)

obj = compile(ast.fix_missing_locations(generated_function), "<ast>", mode="exec")
exec(obj)

say_hello()
