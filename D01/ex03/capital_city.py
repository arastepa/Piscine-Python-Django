import sys

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
    state = sys.argv[1]
    value = states.get(state)
    if not value:
        print('Unknown state')
        return
    other = capital_cities.get(value)
    if not other:
        print('Unknown state')
        return
    print(other)

if __name__ == '__main__':
    capital_city()