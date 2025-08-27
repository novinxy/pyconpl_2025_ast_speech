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
