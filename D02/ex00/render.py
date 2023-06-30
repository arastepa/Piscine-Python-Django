import sys, re, os

def render():
    if (len(sys.argv) != 2):
        return
    format = re.findall('\.template$', sys.argv[1])
    if not format:
        print("wrong format")
        return
    if not os.path.isfile('settings.py'):
        print("settings file does not exist")
        return
    file1 = open('settings.py', 'r')
    my_dict = {}
    while True:
        line = file1.readline()
        if not line:
            break
        my_dict[line.split('=')[0].strip()] = line.split('=')[1].strip().strip('"')
    file1.close()
    if not os.path.isfile(sys.argv[1]):
        print("template file does not exist")
        return
    file2 = open(sys.argv[1],'r')
    content = "".join(file2.readlines())
    file2.close()
    content = content.format(
        name = my_dict['name'],
        title = my_dict['title'],
        surname = my_dict['surname'],
        age = my_dict['age'],
        profession = my_dict['profession']
    )
    pattern = re.compile(r"^(.*?)\.")
    match = pattern.search(sys.argv[1])
    if (match):
        new = open(match.group(1) + ".html", 'w')
        new.write(content)
        new.close()
    else:
        print("not matching file")
if __name__ == '__main__':
    render()