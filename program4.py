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

totalPct = makeTotalPct(175.1, 5)
totalPct2 = makeTotalPct(154.4, 10)

print(goalSeek(totalPct, -100, 100, 13.2, .0001))
print(goalSeek(totalPct2, -100, 100, 28.4, .0001))
