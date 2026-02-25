from altair.utils.schemapi import SchemaBase, UndefinedType
from typing import Any, Literal, Sequence, Union

AltAxisValues = Union[
    Sequence[float],
    Sequence[str],
    Sequence[bool],
    Sequence[dict[str, Any]],
    Sequence[SchemaBase],
    UndefinedType,
]

AltFontWeight = Union[
    Literal["normal", "bold", "lighter", "bolder"],
    Literal[100, 200, 300, 400, 500, 600, 700, 800, 900],
    UndefinedType,
]
AltMarkSize = Union[float, UndefinedType]

AltMarkOrient = Union[Literal["horizontal", "vertical"], SchemaBase, UndefinedType]

# AltScaleDomain = Sequence[str | bool | dict[str, Any] | float | SchemaBase | None] | UndefinedType

# AltScaleRange = Sequence[str | dict[str, Any] | float | SchemaBase | Sequence[float]] | UndefinedType

# AltScaleZero = Union[bool | dict[Any, Any] | SchemaBase | UndefinedType]

AltTickCount = Union[
    Literal["millisecond", "second", "minute", "hour", "day", "week", "month", "year"],
    float,
    dict[Any, Any],
    SchemaBase,
    UndefinedType,
]
