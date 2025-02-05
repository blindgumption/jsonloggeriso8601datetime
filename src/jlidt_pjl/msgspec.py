"""JSON Formatter using [`msgspec`](https://github.com/jcrist/msgspec)"""

### IMPORTS
### ============================================================================
## Future
from __future__ import annotations

## Standard Library
from typing import Any

## Installed
import msgspec.json

## Application
from . import core
from . import defaults as d


### FUNCTIONS
### ============================================================================
def msgspec_default(obj: Any) -> Any:
    """msgspec default encoder function for non-standard types"""
    if d.use_exception_default(obj):
        return d.exception_default(obj)
    if d.use_traceback_default(obj):
        return d.traceback_default(obj)
    if d.use_enum_default(obj):
        return d.enum_default(obj)
    if d.use_type_default(obj):
        return d.type_default(obj)
    return d.unknown_default(obj)


### CLASSES
### ============================================================================
class MsgspecFormatter(core.BaseJsonFormatter):
    """JSON formatter using [`msgspec.json.Encoder`](https://jcristharif.com/msgspec/api.html#msgspec.json.Encoder) for encoding."""

    def __init__(
        self,
        *args,
        json_default: core.OptionalCallableOrStr = msgspec_default,
        **kwargs,
    ) -> None:
        """
        Args:
            args: see [BaseJsonFormatter][jlidt_pjl.core.BaseJsonFormatter]
            json_default: a function for encoding non-standard objects
            kwargs: see [BaseJsonFormatter][jlidt_pjl.core.BaseJsonFormatter]
        """
        super().__init__(*args, **kwargs)

        self.json_default = core.str_to_object(json_default)
        self._encoder = msgspec.json.Encoder(enc_hook=self.json_default)
        return

    def jsonify_log_record(self, log_record: core.LogRecord) -> str:
        """Returns a json string of the log record."""
        return self._encoder.encode(log_record).decode("utf8")
