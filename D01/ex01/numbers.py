def getContent():
    file = open('numbers.txt', 'r')
    content = file.read()
    modified = content.replace(',',' ')
    modified = modified.split(' ');
    for res in modified:
        print(res.strip())
    file.close()
if __name__ == '__main__' :
    getContent()
