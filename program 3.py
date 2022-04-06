def pctIncrease(begin, end):
    return 100*(end/begin-1)

def increaseByPct(begin, pct):
    return begin+begin*pct/100

def totalPct(pct):
    startValue = 175.1
    value = startValue
    for year in range(5):
        value = increaseByPct(value, pct)
    return pctIncrease(startValue, value)

def goalSeek(lowLimit, highLimit, target, maxError=.01):

    error = maxError + 1

    while error > maxError:
        guess = (lowLimit+highLimit)/2
        result = totalPct(guess)
        error = abs(result-target)
        if result > target:
            highLimit = guess
        if result < target:
            lowLimit = guess
            
    return guess

print(goalSeek(-100, 100, 13.2))
print(goalSeek(-100, 100, 13.2, .000001))
