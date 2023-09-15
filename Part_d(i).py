from json import load, dump
from MergeInsertionSort import mergeInsertionSort, mergeSort
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import copy

def mergeInsertSortWithTime(S_value, array):
    start = timer()
    for arr in array:
        kcs_mergeInsertSort = mergeInsertionSort(S_value, arr, 0, len(arr)-1)
    end = timer()
    time_taken = end - start
    temp.append(time_taken)
    temp.append(kcs_mergeInsertSort)


def mergeSortWithTime(array):
    start = timer()
    for arr in array:
        kcs_mergeSort = mergeSort(arr, 0, (len(arr)-1))
    end = timer()
    time_taken = end - start
    temp.append(time_taken)
    temp.append(kcs_mergeSort)


def hist_graph(arr_S, arr_mergeSort, arr_mergeInsertSort, y_title):
    X_axis = np.arange(len(arr_S))


    plt.bar(X_axis + 0.2, arr_mergeSort, 0.4, label='MergeSort')
    plt.bar(X_axis - 0.2, arr_mergeInsertSort, 0.4, label='MergeInsertSort')

    plt.xticks(X_axis, arr_S)
    plt.xlabel("S")
    plt.ylabel(y_title)
    plt.title("Test")
    plt.legend()
    plt.show()


with open("data10000.txt", 'r') as file:
    dataset = load(file)

result = []

for S in range(1,20):
    temp = []
    temp.append(S)
    arrCopy = copy.deepcopy(dataset)
    mergeInsertSortWithTime(S, arrCopy)

    arrCopy = copy.deepcopy(dataset)
    mergeSortWithTime(arrCopy)

    result.append(temp)


arr_S = []
arr_timeMergeSort = []
arr_kcsMergeSort = []
arr_timeMergeInsertSort = []
arr_kcsMergeInsertSort = []

for array in result:
    arr_S.append(array[0])

    arr_timeMergeInsertSort.append(array[1])
    arr_kcsMergeInsertSort.append(array[2])

    arr_timeMergeSort.append(array[3])
    arr_kcsMergeSort.append(array[4])

hist_graph(arr_S, arr_timeMergeSort, arr_timeMergeInsertSort, "Time taken")
hist_graph(arr_S, arr_kcsMergeSort, arr_kcsMergeInsertSort, "Key Comparisons")

with open("result_d_test.txt", 'w') as file:
    dump(result, file)