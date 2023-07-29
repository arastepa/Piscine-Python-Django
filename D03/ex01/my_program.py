from local_lib.path import Path

def my_program():
    try:
        directory_path = Path('myfolder')

        if not directory_path.isdir():
            directory_path.mkdir()

        file_path = directory_path / 'hello.py'

        if not file_path.isfile():
            file_path.touch()

        with file_path.open(mode='w') as f:
            f.write("hello world!")

        with file_path.open() as f:
            print(f.read())
    except Exception as e:
        print(e)



if __name__ == '__main__':
    my_program()