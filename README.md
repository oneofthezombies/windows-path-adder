# windows-path-adder

in windows
```shell
echo %PATH%
# C:\foo;D:\boo

python -m windowspathadder "D:/new/path"
# or python -m windowspathadder "D:\new\path"

echo %PATH%
# D:\new\path;C:\foo;D:\boo

# the previous path is backed up with timestamp.
echo %PATH_{timestamp}%
# C:\foo;D:\boo
```