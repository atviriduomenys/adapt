from pathlib import Path
from shutil import rmtree, copytree
from subprocess import run

modules = [
    'main',
    'module1',
    'module4',
    'module5',
    'module6',
    'module7',
    'module9',
    'module10',
    'module11',
    'module12',
    'module13',
]

base_dir = Path()
build_dir = base_dir / 'build'

print('Build all modules...')
for module in modules:
    run(['yarn', 'run', 'grunt', 'build'], cwd=base_dir / module)

if build_dir.exists():
    print('Remove build diredtory...')
    rmtree(build_dir)

for module in modules:
    src = base_dir / module / 'build'
    dst = build_dir if module == 'main' else build_dir / module
    print(f'Copy build directory of {module} to {dst}...')
    copytree(src, dst)
