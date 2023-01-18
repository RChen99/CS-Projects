print("Algorithms file loaded.")

def quick_sort(arr):
# Automatically returns the list if size less than 2
    if len(arr) < 2:
        return arr

# Sets a point and sorts number into three lists base on condition
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)

def merge_sorted(arr1, arr2):
    sorted_arr = []
    i, j, = 0, 0
# Iterates through the list and appends the smaller number
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

# Appends the remainding value/values to the list
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]

# Breaks the list down till it is only one item
    else:
        middle = len(arr)//2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])
        return merge_sorted(l1,l2)

def insertion_sort(arr):
# Sets range at index 1 and length of the list
    for key in range(1, len(arr)):
# Sets key to the smaller number
        if arr[key] < arr[key-1]:
            j = key
# Decrements through the index by inserting the smaller number into previousn index
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1

def selection_sort(arr):
# Designate a number as a marker
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
# Switches number with the marked number if number is less than marked number
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1

def bubble_sort(arr):
# Sets a flag to only run loop if list is not sorted
    swap_happened = True
    while swap_happened:
        for num in range(len(arr)-1):
            swap_happened = False # Stops loop from running
            if arr[num] > arr[num+1]:
                swap_happened = True # Starts loop again
                arr[num], arr[num+1] = arr[num+1], arr[num]