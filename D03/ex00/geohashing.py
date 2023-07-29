import sys, antigravity

def geohash():
    if len(sys.argv) != 4:
        print("wrong number of arguments")
        return
    try:
        latitude = float(sys.argv[1])
    except Exception as e:
        return print("can't convert to float")
    try:
        longitude = float(sys.argv[2])
    except Exception as e:
        return print("can't convert to float")
    try:
        date = sys.argv[3].encode('utf-8')
    except Exception as e:
        return print("can't convert to utf8")
    print (antigravity.geohash(latitude, longitude, date))

if __name__ == '__main__':
    geohash()