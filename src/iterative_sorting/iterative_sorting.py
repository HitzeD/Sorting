# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):

        smallest_index = i
        temp = arr[i]
        j = i 

        # for j in range(i, len(arr)):
        #     if arr[smallest_index] > arr[j]:
        #         smallest_index = arr[j]
        
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp
        
        while j < len(arr):
            if (arr[smallest_index] > arr[j]):
                smallest_index = j
            j += 1
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    print(arr)
    return arr

a = [5, 2, 8, 7, 3]
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# selection_sort(a)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):

        small = i
        temp = arr[i]
        j = i

        for j in range(i, len(arr)):
            if(arr[i] > arr[j]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    print(arr)
    return arr

# bubble_sort(a)
bubble_sort(arr1)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr