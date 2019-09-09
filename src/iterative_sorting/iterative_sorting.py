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
                                            # ANOTHER SOLUTION
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



# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
    # loop through the list with i
    for i in range(0, len(arr) - 1):
        # create a temp variable for later
        # initialize j in relation to i (start of the list)
        temp = arr[i]
        j = i
        # loop through again fo each number to compare it to each one
        for j in range(i, len(arr)):
            if(arr[i] > arr[j]):
                # temp holds the element temporarily
                temp = arr[j]
                # assigning j(smaller number) to the position in i
                arr[j] = arr[i]
                # now move i into the temp spot
                arr[i] = temp
    print(arr)
    return arr

bubble_sort(a)
# bubble_sort(arr1)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr