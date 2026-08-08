from __future__ import annotations

import dis
import io
import types


def disassemble_source(source: str, filename: str = "<source>") -> str:
    code = compile(
        source,
        filename,
        "exec",
        dont_inherit=True,
        optimize=0,
    )

    output = io.StringIO()

    def walk(code_obj: types.CodeType, depth: int = 0):
        output.write(
            f"{'    ' * depth}=== {code_obj.co_name} ===\n"
        )

        dis.dis(code_obj, file=output)
        output.write("\n")

        for const in code_obj.co_consts:
            if isinstance(const, types.CodeType):
                walk(const, depth + 1)

    walk(code)

    return output.getvalue()