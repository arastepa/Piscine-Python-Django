pip --version

pip install --upgrade --force-reinstall git+https://github.com/jaraco/path.py.git --target local_lib 2>&1 > install.log

python3 my_program.py