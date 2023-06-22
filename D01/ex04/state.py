import sys

def getKey(myDict: dict, value):
    for key, val in myDict.items():
        if val == value:
            return key 

def capital_city():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return
    city = sys.argv[1]
    key = getKey(capital_cities, city);
    if not key:
        print('Unknown city')
        return
    other = getKey(states,key)
    if not other:
        print('Unknown state')
        return
    print(other)

if __name__ == '__main__':
    capital_city()