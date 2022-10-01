import math

def dominoPiling(m,n):
    if(m < 1 or n < 1):
        return 0
    bord_area = m * n
    maxDominos = math.floor(bord_area / 2)
    return maxDominos

input = input().split()
dominoParams = []

for element in input:
    numElement = int(element)
    dominoParams.append(numElement)

print(dominoPiling(dominoParams[0], dominoParams[1]))
