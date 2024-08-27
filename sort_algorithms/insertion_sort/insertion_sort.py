# Insertion Sort
# Python
# Porter L

def insertionSort(Arr): 
    for x in range(1, len(Arr)): 
        key = Arr[x] 
        y = x-1
        while y >= 0 and key < Arr[y] : 
            Arr[y + 1] = Arr[y] 
            y -= 1
        Arr[y + 1] = key 
    return Arr

# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = insertionSort(test_array)
    print(test_array) # sorted