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

def insertion_sort(list):

# mark first element as sorted (starting the list at index 1 rather than 0)
# for each unsorted element X
    for i in range(1, len(list)):

        # extract the element X
        temp = list[i]

        # j = lastSortedIndex down to 0
        j = i
        print(f"\nCur_Index: {i}\nTemp: {temp}\nJ: {j}\n")
        # if current element j > x
        while j > 0 and temp < list[j - 1]:
            # move sorted element to the right by one
            list[j] = list[j - 1]
            # change j
            j -= 1
            break
        
        list[j] = temp
        
    return list

selection_sort(a)
# insertion_sort(a)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr