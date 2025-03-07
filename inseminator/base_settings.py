from typing import Any, Union

try:
    # try to get BaseSettings from pydantic@v2
    from pydantic_settings import BaseSettings as BaseSettingsV2
except ImportError:
    BaseSettingsV2 = None

try:
    # try to get BaseSettings from pydantic@V2 in backward compatibility module
    from pydantic.v1 import BaseSettings as BaseSettingsV1FromV2
except ImportError:
    BaseSettingsV1FromV2 = None

try:
    # try to get BaseSettings for pydantic@v1
    from pydantic import BaseSettings as BaseSettingsV1
except ImportError:
    BaseSettingsV1 = None


BaseSettings = Union[BaseSettingsV2, BaseSettingsV1FromV2, BaseSettingsV1]


def is_settings_subclass(obj: Any) -> bool:
    """Check if obj is a subclass of BaseSettings.

    This works around incompatibility with Python <3.10 for simply calling `issubclass(obj, BaseSettings)`,
    which breaks with `TypeError: Subscripted generics cannot be used with class and instance checks`.
    """
    if BaseSettingsV2 and issubclass(obj, BaseSettingsV2):
        return True
    if BaseSettingsV1FromV2 and issubclass(obj, BaseSettingsV1FromV2):
        return True
    if BaseSettingsV1 and issubclass(obj, BaseSettingsV1):
        return True
    return False
