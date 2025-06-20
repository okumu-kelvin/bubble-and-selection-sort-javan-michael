def selection_sort(arr):
    # Creates a copy to preserve the original list
    unsorted = arr.copy()
    n = len(unsorted)

    # Loop through the entire list "n" times
    for i in range(n):
        # Assumes that the current index has the minimum value
        min_index = i

        # Looks for a smaller value in the remaining unsorted part
        for j in range(i + 1, n):
            if unsorted[j] < unsorted[min_index]:
                min_index = j

        # Swaps the found minimum value with the value at the current index
        unsorted[i], unsorted[min_index] = unsorted[min_index], unsorted[i]

    # Returns the sorted list
    return unsorted
