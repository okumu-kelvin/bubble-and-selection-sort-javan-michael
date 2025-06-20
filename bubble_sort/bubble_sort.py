def bubble_sort(unsorted_list):
    # It Creates a copy of the list to avoid modifying the original data
    arr = unsorted_list.copy()
    n = len(arr)

    # Outer loop runs n times to ensure the entire list is sorted
    for i in range(n):
        # Inner loop compares adjacent elements and "bubbles" the largest to the end
        for j in range(0, n - i - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the sorted copy of the list
    return arr

