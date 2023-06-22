def createDict():
    
    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]

    my_dict = {}
    for res in d:
        if my_dict.setdefault(res[1]):
            my_dict[res[1]] = my_dict[res[1]] + " " + res[0]
        else:
            my_dict[res[1]] = res[0]
    for key, value in my_dict.items():
        print(key, ':', value)

if __name__ == '__main__' :
    createDict()
