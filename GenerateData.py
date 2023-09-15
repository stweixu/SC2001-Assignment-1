from random import sample
from json import dump

def generatedata(size, name):
    dataset = []
    maxNum = size * 10 - 1
    array = sample(range(1, maxNum), size)
    dataset.append(array)

    with open(name, 'w') as file:
        dump(dataset, file)


## GENERATE SMALL DATA [1000, 30000] ##
for i in range(1000, 30000, 1000):
    file_name = "data" + str(i) + ".txt"
    generatedata(i, file_name)

## GENERATE EVENLY SPREAD DATA ##
interval = int((10**7-30000)/40) #40 data point
for i in range(30000, 10**7+1, interval):
    file_name = "data" + str(i) +".txt"
    generatedata(i, file_name)
