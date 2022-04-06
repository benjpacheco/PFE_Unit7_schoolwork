import shelve
shelf = shelve.open('cpi')
cpi = shelf['cpi']
shelf.close()

def pctIncrease(begin, end):
    return 100*(end/begin-1)

print('       Percent increase in CPI')
print('             (Jan-Jan)')
print('      1 year  5 years 10 years')

pattern1 = '{0:d}  {1:6.1f}'
pattern2 = '{0:9.1f}'

for year in range(1914, 2009):
    currentCPI = cpi[year][1]
    pct = pctIncrease(cpi[year-1][1], currentCPI)
    print(pattern1.format(year, pct), end='')
    if year-5 >= 1913:
        pct = pctIncrease(cpi[year-5][1], currentCPI)
        print(pattern2.format(pct), end='')
    if year-10 >= 1913:
        pct = pctIncrease(cpi[year-10][1], currentCPI)
        print(pattern2.format(pct), end='')
    print()
