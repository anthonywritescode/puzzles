from __future__ import annotations

from typing import Callable

from mypy.plugin import Plugin
from mypy.plugin import FunctionContext
from mypy.types import Instance
from mypy.types import LiteralType
from mypy.types import Type


class CustomPlugin(Plugin):
    def _require_only_literals(self, func: FunctionContext) -> Type:
        # invalid signature, but already handled
        if len(func.arg_types) != 1 or len(func.arg_types[0]) != 1:
            return func.default_return_type

        tp = func.arg_types[0][0]
        if (
                not isinstance(tp, Instance) or
                not isinstance(tp.last_known_value, LiteralType)
        ):
            func.api.fail('expected string literal for argument 1', func.context)
            return func.default_return_type

        # already handled by signature
        # if f'{tp.type.module_name}.{tp.type.name}' != 'builtins.str':

        return func.default_return_type

    def get_function_hook(
            self,
            name: str,
    ) -> Callable[[FunctionContext], Type] | None:
        if name == 't.somefunc':
            return self._require_only_literals
        else:
            return None


def plugin(version: str) -> type[Plugin]:
    return CustomPlugin
