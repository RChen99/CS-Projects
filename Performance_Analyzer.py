# Imports functions from the Analyzer Demo
from Analyzer_Demo import quick_sort, merge_sort, insertion_sort, selection_sort, bubble_sort
import random # Imports random module
import time # Imports time module

# Creates list size and sets the range of the numbers generated
def generate_random_numbers(size, max_val):
    rand_list = []
    for num in range(size):
        rand_list.append(random.randint(1,max_val))
    return rand_list

# Gets the value of elapsed time for each sorts
def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    run_time = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {run_time:.5f} ")

# Asks for user input for Analyzer
size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))
runs = int(input("How times do you want to run? "))

# How many times the Analyzer will be run
for num in range(runs):
    print(f"Run: {num+1}")
    l = generate_random_numbers(size, max)
    if size > 20000:
        print("Insertion Sort, Selection Sort, and Bubble Sort will not be runned, runtime too long.")
        analyze_func(quick_sort, l)
        analyze_func(merge_sort, l)
        print("Python's built_in sort: ")
        analyze_func(sorted, l)
        print("-" * 50)

    else:
        analyze_func(quick_sort, l)
        analyze_func(merge_sort, l)
        analyze_func(insertion_sort, l.copy())
        analyze_func(selection_sort, l.copy())
        analyze_func(bubble_sort, l.copy())
        print("Python's built_in sort: ")
        analyze_func(sorted, l)
        print("-" * 50)
