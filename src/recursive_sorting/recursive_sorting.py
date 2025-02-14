# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    l = 0
    r = 0
    for i in range( 0, elements ):
        if l >= len(arrA):
            merged_arr[i] = arrB[r]
            r += 1
        elif r >= len(arrB):
            merged_arr[i] = arrA[l]
            l += 1
        elif arrA[l] < arrB[r]:
            merged_arr[i] = arrA[l]
            l += 1
        else:
            merged_arr[i] = arrB[r]
            r += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len( arr ) > 1:
        middle = len(arr) // 2
        left = merge_sort( arr[ 0 : middle ] )
        right = merge_sort(arr[ middle : len(arr) ] )
        arr = merge( left, right )
    return arr

print(merge_sort([3, 4, 1, 8, 3, 2]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
