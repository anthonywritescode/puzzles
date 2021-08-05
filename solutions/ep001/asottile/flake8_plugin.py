from __future__ import annotations

import ast
from typing import Any
from typing import Generator

WAT001 = 'WAT001 expected 1 arg'
WAT002 = 'WAT002 expected a string literal'


class Plugin:
    name = __name__
    version = '0'

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type[Any]], None, None]:
        for node in ast.walk(self._tree):
            if (
                    not isinstance(node, ast.Call) or
                    not isinstance(node.func, ast.Name) or
                    not node.func.id == 'somefunc'
            ):
                continue

            if len(node.args) != 1 or node.keywords:
                yield node.lineno, node.col_offset, WAT001, type(self)
            elif not isinstance(node.args[0], ast.Str):
                yield node.lineno, node.col_offset, WAT002, type(self)
