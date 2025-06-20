def bubble_sort(unsorted_list):
    # It creates a copy of the list and does not modify the data
    arr = unsorted_list.copy()
    n = len(arr)

    # The outer loop will run "n" times to make sure list is sorted
    for i in range(n):
        # Inner loop compares adjacent elements and "bubbles" the largest to the end
        for j in range(0, n - i - 1):
            # If the current element is greater than the next they are swapped
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Returns the sorted copy of the list
    return arr

