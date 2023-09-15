import numpy as np
import matplotlib.pyplot as plt
from json import load, dump

def graph(title, x_label, y_label, x, y):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.scatter(x, y)
    plt.show()

def loadFile(filename):
    with open(filename, 'r') as file:
        dataset = load(file)
    return dataset

##c.i FULL INPUT##
key_comp_i = loadFile("result_c_i_full.txt")
input_size_i = loadFile("full_input_c_i.txt")
graph("S = 10", "Input Size", "Key Comparisons", input_size_i, key_comp_i)

##c.i SMALL INPUT##
key_comp_i_zoomed = loadFile("result_c_i_small.txt")
input_size_i_zoomed = loadFile("small_input_c_i.txt")
graph("S = 10", "Input Size", "Key Comp", input_size_i_zoomed, key_comp_i_zoomed)

##c.ii##
key_comp_ii = loadFile("result_c_ii.txt")
S_array_ii = loadFile("S_array.txt")
graph("Input size = 3x10e5", "S", "Key Comparisons", S_array_ii, key_comp_ii)