# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        print(i)
    
    return merged_arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 334, 7889, 322, 98, 4532, 567, 7654]
arr2 = [245, 4567, 2123456, 678765, 3, 7, 543, 345, 765, 2, 89]
my_arr = []

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # checks if the list is less then or equal to 1
    if len(arr) <= 1:
        return arr
    else:
        # `//` operator means floor division or round 
        # down to the nearest whole
        mid = len(arr) // 2

        # splits the list into to seperate lists
        left = arr[:mid]
        right = arr[mid:]

        # after they are split, they are sent to be 
        # split until they are single elements
        merge_sort(left)
        merge_sort(right)

        # passing in both, right and left arrays 
        # into the `merge` function to merge all 
        # elements together
        merge(left, right)

merge_sort(arr1)

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
