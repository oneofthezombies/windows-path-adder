from datetime import datetime
from pathlib import Path
from typing import List
import subprocess
import platform
import re
from . import error


_DEFAULT_PRINT = print
_WINDOWS_PATH_PATTERN = re.compile(r'    PATH    (?P<type>.+)    (?P<value>.+)*')


def _print(message):
    _DEFAULT_PRINT(f'** {message}', flush=True)


def _command(*args, **kwargs):
    _print(' '.join(args))
    return subprocess.run(*args, **kwargs)


def _try_decode(byte_string: bytes, encodings: List[str] = ['utf-8', 'cp949', 'ansi']) -> str:
    for encoding in encodings:
        try:
            return byte_string.decode(encoding)
        except UnicodeDecodeError:
            continue
    raise error.TryDecodeError(byte_string, encodings)


class WindowsPathAdder:
    def __call__(self, new_path: str):
        current_platform = platform.system()
        if current_platform != 'Windows':
            raise error.NotSupportError(current_platform)

        current_type = 'REG_SZ'
        current_path = None

        completed_process = _command(['reg', 'query', 'HKCU\\Environment', '/v', 'PATH', '/f'], capture_output=True)
        if completed_process.returncode == 0:
            stdout = _try_decode(completed_process.stdout)
            _print(stdout)
            match = _WINDOWS_PATH_PATTERN.search(stdout)
            if match:
                current_type = match.group('type')
                current_path = match.group('value')
                if current_path:
                    current_path = current_path.strip()
                    _print(f'current PATH: {current_path}')
                else:
                    _print('environment variable PATH is empty.')

        elif completed_process.returncode == 1:
            _print('environment variable PATH does not exist.')
            _print(_try_decode(completed_process.stderr))

        else:
            completed_process.check_returncode()

        resolved_new_path = str(Path(new_path).resolve().absolute())
        _print(f'resolve new path. [{resolved_new_path}]')

        if current_path:
            if resolved_new_path in current_path:
                _print(f'[{resolved_new_path}] exists in [{current_path}].')
                _print(f'do not add to PATH.')
                return

        if current_path:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            backup_key = f'PATH_{timestamp}'
            _print(f'backup PATH. [{current_path}] to [{backup_key}]')
            _command(['reg', 'add', 'HKCU\\Environment', '/t', current_type, '/v', backup_key, '/d', current_path, '/f']).check_returncode()

        path = f'{resolved_new_path};{current_path}' if current_path else resolved_new_path
        _command(['reg', 'add', 'HKCU\\Environment', '/t', current_type, '/v', 'PATH', '/d', path, '/f']).check_returncode()
