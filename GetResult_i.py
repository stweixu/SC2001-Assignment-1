from json import load, dump
from MergeInsertionSort import mergeInsertionSort

def runMergeInsertionSort(filename):
    with open(filename, 'r') as file:
        dataset = load(file)

    for array in dataset:
        result.append(mergeInsertionSort(S, array, 0, len(array) - 1))


def outputFile(inputList, result, inputFileName, keyCompFileName):
    with open(keyCompFileName, 'w') as file:
        dump(result, file)
    with open(inputFileName, 'w') as file:
        dump(inputList, file)


S = 10
result = []
input_size_list = []
    ## SMALL DATA ##
for i in range (1000,30000, 1000):
    file_name = "small_data" + str(i) + ".txt"
    runMergeInsertionSort(f'data{i}.txt')
    input_size_list.append(i)
outputFile(input_size_list, result, "small_input_c_i.txt", "result_c_i_small.txt")

    ##EVENLY SPREAD DATA##
interval = int((10**7-30000)/40) ##40 interval
for i in range(30000, 10**7+1, interval):
    runMergeInsertionSort(f'data{i}.txt')
    input_size_list.append(i)
outputFile(input_size_list, result, "full_input_c_i.txt", "result_c_i_full.txt")