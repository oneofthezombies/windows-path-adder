from pathlib import Path
import subprocess
import shutil


outputs = ['build', 'windows_path_adder.egg-info', 'dist']
for output in outputs:
    po = Path(output)
    if po.exists():
        shutil.rmtree(str(po))

subprocess.run(['python3', 'setup.py', 'sdist', 'bdist_wheel']).check_returncode()
subprocess.run(['python3', '-m', 'twine', 'upload', 'dist/*']).check_returncode()
