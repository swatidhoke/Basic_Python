#academic_support@interviewKickstart.com
# sorting
# recursion 
# trees
# graphs 
# Dynamic programming
'''
# Sorting Algorithum practice 
# 1. Bubble sort
# 2. Selection sort 
# 3. Decrease and conquer- Insertion sort
# 4. Divide and concqer- Merge sort
# 5. Divide and concqer- Quick Sort
# 6. Heap Sort

Time and Space Complexity of Various Sorting Algorithms

| Sorting Algorithm  | Best Case Time | Average Case Time | Worst Case Time | Space Complexity | Stable? |
|--------------------|---------------|-------------------|----------------|------------------|---------|
| Bubble Sort       | O(n)          | O(n²)            | O(n²)         | O(1)             | Yes     |
| Selection Sort    | O(n²)         | O(n²)            | O(n²)         | O(1)             | No      |
| Insertion Sort    | O(n)          | O(n²)            | O(n²)         | O(1)             | Yes     |
| Merge Sort       | O(n log n)     | O(n log n)       | O(n log n)    | O(n)             | Yes     |
| Quick Sort       | O(n log n)     | O(n log n)       | O(n²)         | O(log n) (avg.)  | No      |
| Heap Sort        | O(n log n)     | O(n log n)       | O(n log n)    | O(1)             | No      |
| Counting Sort    | O(n + k)       | O(n + k)         | O(n + k)      | O(k)             | Yes     |
| Radix Sort       | O(nk)          | O(nk)            | O(nk)         | O(n + k)         | Yes     |
| Bucket Sort      | O(n + k)       | O(n + k)         | O(n²)         | O(n + k)         | Yes     |

'''
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

def bubble_sort(arr):
    """ Bubble Sort: Repeatedly swaps adjacent elements if they are in the wrong order. """
    n = len(arr)
    logging.info(f"Starting Bubble Sort on {arr}")
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
                logging.info(f"Swapped {arr[j]} and {arr[j+1]}: {arr}")
        if not swapped:
            break  # Optimization: Stop if no swaps occurred
    logging.info(f"Bubble Sort completed: {arr}")
    return arr

def selection_sort(arr):
    """ Selection Sort: Finds the smallest element and swaps it with the first element. """
    n = len(arr)
    logging.info(f"Starting Selection Sort on {arr}")
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap elements
        logging.info(f"Swapped {arr[i]} and {arr[min_idx]}: {arr}")
    logging.info(f"Selection Sort completed: {arr}")
    return arr

def insertion_sort(arr):
    """ Insertion Sort: Builds the sorted array one item at a time. """
    logging.info(f"Starting Insertion Sort on {arr}")
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:  
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = temp
        logging.info(f"Inserted {temp} into position {j+1}: {arr}")
    logging.info(f"Insertion Sort completed: {arr}")
    return arr

def quick_sort(arr):
    """ Quick Sort: Uses a pivot element to divide and conquer sorting. """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Pivot elements
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    logging.info(f"Pivot {pivot}: Left {left}, Middle {middle}, Right {right}")
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """ Merge Sort: Recursively divides the array and merges sorted subarrays. """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        logging.info(f"Dividing {arr} into {left_half} and {right_half}")
        merge_sort(left_half)
        merge_sort(right_half)

    # Merging two sorted halves
    i = j = 0
    sorted_arr = []
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1

    sorted_arr.extend(left_half[i:])  # Append remaining elements
    sorted_arr.extend(right_half[j:]) 

    logging.info(f"Merged into {sorted_arr}")
    return sorted_arr


def sort_array(arr, method="quick_sort"):
    """
    Sorts an array using the specified sorting method.
    
    :param arr: List of numbers to be sorted.
    :param method: Sorting algorithm to use. Options: 'bubble_sort', 'selection_sort', 
                   'insertion_sort', 'quick_sort', 'merge_sort'.
    :return: Sorted list.
    """
    sorting_algorithms = {
        "bubble_sort": bubble_sort,
        "selection_sort": selection_sort,
        "insertion_sort": insertion_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort
    }

    if method in sorting_algorithms:
        logging.info(f"Sorting using {method}")
        return sorting_algorithms[method](arr.copy())  # Use copy to prevent modifying original array
    else:
        raise ValueError("Invalid sorting method. Choose from: " + ", ".join(sorting_algorithms.keys()))

# Example Usage
arr = [64, 25, 12, 22, 11]
logging.info("Original Array: " + str(arr))

print("Bubble Sort:", sort_array(arr, "bubble_sort"))
print("Selection Sort:", sort_array(arr, "selection_sort"))
print("Insertion Sort:", sort_array(arr, "insertion_sort"))
print("Quick Sort:", sort_array(arr, "quick_sort"))
print("Merge Sort:", sort_array(arr, "merge_sort"))
