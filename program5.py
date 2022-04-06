import shelve

def pctIncrease(begin, end):
    return 100*(end/begin-1)

def increaseByPct(begin, pct):
    return begin+begin*pct/100

def makeTotalPct(startValue, years):
    def totalPct(pct):
        value = startValue
        for year in range(years):
            value = increaseByPct(value, pct)
        return pctIncrease(startValue, value)
    return totalPct

def goalSeek(function, lowLimit, highLimit, target, maxError=.01):

    error = maxError + 1

    while error > maxError:
        guess = (lowLimit+highLimit)/2
        result = function(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
            
    return guess

def printAnnualized(year, n):
    pattern = '{0:9.1f}'
    if year-n >= 1913:
        pct = pctIncrease(cpi[year-n][1], currentCPI)
        totalPct = makeTotalPct(cpi[year-n][1], n)
        annual = goalSeek(totalPct, -100, 100, pct, .0001)
        print(pattern.format(annual), end='')    

shelf = shelve.open('cpi')
cpi = shelf['cpi']
shelf.close()

print('       Percent increase in CPI')
print('             (Jan-Jan)')
print('      1 year  5 years 10 years')

pattern = '{0:d}  {1:6.1f}'

for year in range(1914, 2009):
    currentCPI = cpi[year][1]
    pct = pctIncrease(cpi[year-1][1], currentCPI)
    print(pattern.format(year, pct), end='')
    printAnnualized(year, 5)
    printAnnualized(year, 10)
    print()
