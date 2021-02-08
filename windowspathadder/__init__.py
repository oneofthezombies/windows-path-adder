from . import (
    error,
    windowspathadder
)


NotSupportError = error.NotSupportError
TryDecodeError = error.TryDecodeError
add_windows_path = windowspathadder.WindowsPathAdder()
