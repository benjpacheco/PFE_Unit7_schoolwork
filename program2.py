
def pctIncrease(begin, end):
    return 100*(end/begin-1)

def increaseByPct(begin, pct):
    return begin+begin*pct/100

startValue = 175.1
while True:
    value = startValue
    pct = float(input('Enter percent: '))
    for year in range(5):
        value = increaseByPct(value, pct)
    print('Total increase:', pctIncrease(startValue, value))
    print()
