
# Bucket Sort
# Python
# Porter L

import insertion_sort as iSort  
              
def bucketSort(Arr):
    max_value = max(Arr)
    size = max_value/len(Arr)
    buckets_list = []


    for x in range(len(Arr)): # create buckets
        buckets_list.append([]) 

    for y in range(len(Arr)):
        z = int (Arr[y] / size)
        if (z != len (Arr)):
            buckets_list[z].append(Arr[y])
        else:
            buckets_list[len(Arr) - 1].append(Arr[y])

    for z in range(len(Arr)): # use previously implemented insertion sort 
        iSort.insertionSort(buckets_list[z])
            
    Arr_out = []
    for x in range(len (Arr)): # combine buckets into final output
        Arr_out = Arr_out + buckets_list[x]
    return Arr_out

# Example
if __name__=='__main__': 
    test_array = [2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3]
    print(test_array) # unsorted
    test_array = bucketSort(test_array)
    print(test_array) # sorted