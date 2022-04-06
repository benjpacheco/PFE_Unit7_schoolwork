import urllib.request, shelve

url = 'http://nancymcohen.com/csci133/cpiai.txt'
file = urllib.request.urlopen(url)
lines = file.readlines()
file.close()

cpi = {}
for line in lines:
    items = line.decode().split()
    if len(items) > 0 and items[0].isdigit():
        cpi[int(items[0])] = [float(item) for item in items[:13]]

shelf = shelve.open('cpi')
shelf['cpi'] = cpi
shelf.close()


