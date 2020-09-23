# Bubble Sort
# Python
# Porter L

def bubbleSort(Arr): 
    length = len(Arr) 
    for x in range(length-1): 
        for y in range(0, length-x-1): 
            if (Arr[y] > Arr[y+1]): 
                Arr[y], Arr[y+1] = Arr[y+1], Arr[y] 
    return Arr

# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = bubbleSort(test_array)
    print(test_array) # sorted