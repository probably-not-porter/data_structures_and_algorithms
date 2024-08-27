#include <stdio.h>

void swap(int *a, int *b) // Swap two items
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void printArray(int output[], int s)
{
    int i;
    for (i=0; i < s; i++)
        printf("%d ", output[i]);
    printf("\n");
}


int main() // Example
{
    int arr[] = {2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3};
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr, n); // unsorted 
    selectionSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n); // sorted
    return 0;
          