import sys

def getKey(myDict: dict, value):
    for key, val in myDict.items():
        if val.upper() == value:
            return key

def getValue(myDict: dict, k):
    for key, val in myDict.items():
        if (key.upper() == k):
            return val

def all_in():
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
    arr = sys.argv[1].split(',')
    for x in arr:
        x = x.strip()
        if x == "":
            continue
        val = getValue(states, x.upper())
        city = getKey(capital_cities,x.upper())
        if val:
            print(getValue(capital_cities, val), "is the capital of", x)
        elif city:
            print(x, "is the capital of", getKey(states,city))
        else:
            print(x, "is neither a capital city nor a state")

if __name__ == '__main__':
    all_in()