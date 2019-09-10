# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Set current index for outside loop
        cur_idx = i
        # Using the cur_idx element to compare to other elements in the array left -> right to see if it's larger
        for j in range(i+1, len(arr)):
            if arr[cur_idx] > arr[j]: 
                # Set our cur_idx to the index of the element we're moving
                cur_idx = j
        # Swap elements
        arr[i], arr[cur_idx] = arr[cur_idx], arr[i]
        
    return arr

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             

print(selection_sort([2, 4, 1, 6, 9, 3, 2, 6, 8, 1, 2, 6]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Loop through arr
    for i in range(len(arr)-1, 0, -1):
        # Loop through arr again and compare elements beside each other
        for j in range(i):
            # If arr[j] is larger, swap its position with arr[j+1]
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([9, 4, 2, 8, 7, 2, 5, 8, 5, 7]))

# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr