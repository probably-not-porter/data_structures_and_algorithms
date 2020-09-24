# Heap Sort
# Python
# Porter L

def heapify(Arr, x, y): # create heap
    largest = y
    left = 2 * y + 1 
    right = 2 * y + 2

    if (left < x and Arr[y] < Arr[left]): 
        largest = left 

    if (right < x and Arr[largest] < Arr[right]): 
        largest = right 

    if (largest != y): 
        Arr[y],Arr[largest] = Arr[largest],Arr[y]
        heapify(Arr, x, largest) 
  
def heapSort(Arr): 
    x = len(Arr) 

    for y in range(x//2 - 1, -1, -1):
        heapify(Arr, x, y) 

    for y in range(x-1, 0, -1): 
        Arr[y], Arr[0] = Arr[0], Arr[y] 
        heapify(Arr, y, 0) 
        
    return Arr
  
# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = heapSort(test_array)
    print(test_array) # sorted
