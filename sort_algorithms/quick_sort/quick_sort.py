# Quick Sort
# Python
# Porter L

def partition(Arr,low,high): 
    i = (low - 1)
    pivot = Arr[high]
  
    for j in range(low, high): 
        if Arr[j] < pivot: 
            i = i + 1 
            Arr[i], Arr[j] = Arr[j], Arr[i] 
  
    Arr[i+1], Arr[high] = Arr[high], Arr[i+1] 
    return (i + 1) 
  
def quickSort(Arr,low,high): 
    if low < high: 
        p = partition(Arr, low, high) 
        quickSort(Arr, low, p-1) 
        quickSort(Arr, p+1, high) 
    return Arr


# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = quickSort(test_array, 0, len(test_array) - 1)
    print(test_array) # sorted