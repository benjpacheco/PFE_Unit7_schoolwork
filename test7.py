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


def makePoly(A, B, C, D):
    def P(x):
        return A*x**3+B*x**2+C*x+D
    return P

entries = []

pattern = '{0:8.2f}{1:8.2f}{2:8.2f}{3:8.2f} = {4:8.2f} at {5:8.2f}'


with open('poly.txt') as polynomials:
    for line in polynomials:
        if line[0] != '#':
           lines = line.split('\n')
           entries.append(lines)

for entry in entries:
    lines2 = entry[0].split(' ')
    linesWithNoEmptySpace = []
    for line in lines2:
        if (line != ''):
            linesWithNoEmptySpace.append(line)

    P1 = makePoly(float(linesWithNoEmptySpace[0]), float(linesWithNoEmptySpace[1]), float(linesWithNoEmptySpace[2]), float(linesWithNoEmptySpace[3]))

    root = goalSeek(P1, float(linesWithNoEmptySpace[5]), float(linesWithNoEmptySpace[6]), float(linesWithNoEmptySpace[4]))

    print(pattern.format(float(linesWithNoEmptySpace[0]), float(linesWithNoEmptySpace[1]), float(linesWithNoEmptySpace[2]), float(linesWithNoEmptySpace[3]), float(linesWithNoEmptySpace[5]), root))

    
