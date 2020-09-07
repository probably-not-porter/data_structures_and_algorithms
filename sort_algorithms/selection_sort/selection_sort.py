# Selection Sort
# Python
# Porter L

def selectionSort(Arr):
    for x in range(len(Arr)): # Iterate through each element
        min_index = x
        for y in range(x+1, len(Arr)): # for each element, check to see if there is a smaller one
            if Arr[min_index] > Arr[y]: # smaller value found right of min_index
                min_index = y
        Arr[x], Arr[min_index] = Arr[min_index], Arr[x] # swap elements
    return Arr

# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = selectionSort(test_array)
    print(test_array) # sorted