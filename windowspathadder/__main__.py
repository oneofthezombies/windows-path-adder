if __name__ == '__main__':
    import sys
    from . import (add_windows_path, windowspathadder)
    if len(sys.argv) == 2:
        add_windows_path(sys.argv[1])
    else:
        windowspathadder._print(f'there must be 1 additional argument. args: [{sys.argv}]')
