# Merge Sort
# Python
# Porter L

def mergeSort(Arr): 
    if len(Arr) > 1: 
        mid = len(Arr) // 2 # dividing point
        left = Arr[:mid] 
        right = Arr[mid:]

        mergeSort(left) # sort left
        mergeSort(right) # sort right
        x = y = z = 0
          
        while x < len(left) & y < len(right): 
            if left[x] < right[y]: 
                Arr[z] = left[x] 
                x+= 1
            else: 
                Arr[z] = right[y] 
                y+= 1
            z+= 1

        while x < len(left): 
            Arr[z] = left[x] 
            x+= 1
            z+= 1
          
        while y < len(right): 
            Arr[z] = right[y] 
            y+= 1
            z+= 1
    return Arr

# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = mergeSort(test_array)
    print(test_array) # sorted