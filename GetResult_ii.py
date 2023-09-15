from json import load, dump
from MergeInsertionSort import mergeInsertionSort


with open('data30000.txt.txt', 'r') as file:
    dataset = load(file)

S_array = []
result = []

for S in range(0,50):
    for array in dataset:
        copyArray = array.copy()
        result.append(mergeInsertionSort(S, copyArray, 0, len(array) - 1))
        S_array.append(S)
        print(S)


with open('result_c_ii.txt', 'w') as file:
    dump(result, file)

with open('S_array.txt', 'w') as file:
    dump(S_array, file)
