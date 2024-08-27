# Radix Sort
# Python
# Porter L

def countingSort(Arr, exponent): 
    n = len(Arr) 
    output = [0] * (n)
    count = [0] * (10) 

    for x in range(0, n): 
        index = (Arr[x]/exponent) 
        count[ int((index)%10) ] += 1

    for x in range(1,10): 
        count[x] += count[x-1] 

    x = n-1
    while x>=0: 
        index = (Arr[x]/exponent) 
        output[ count[ int((index)%10) ] - 1] = Arr[x] 
        count[ int((index)%10) ] -= 1
        x -= 1

    x = 0
    for x in range(0,len(Arr)): 
        Arr[x] = output[x] 
  
def radixSort(Arr): 
    largest = max(Arr) 
    exponent = 1
    while largest/exponent > 0: 
        countingSort(Arr,exponent) 
        exponent *= 10
    return Arr

# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = radixSort(test_array)
    print(test_array) # sorted