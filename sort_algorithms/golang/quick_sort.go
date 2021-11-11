// Quick Sort
// Golang
// Porter L

package main
import ("fmt")

func partition(Arr []int, low, high int) (int){
	x := low - 1
	pivot := Arr[high]

	for y := low; y < high; y++ {
		if Arr[y] < pivot {
			x++
			Arr[x], Arr[y] = Arr[y], Arr[x]
			
		}
	} 
	Arr[x+1], Arr[high] = Arr[high], Arr[x+1]
	return x+1
}

func quickSort(Arr []int, low, high int) []int {
	if low < high {
		var p int
		p = partition(Arr, low, high)
		Arr = quickSort(Arr, low, p-1)
		Arr = quickSort(Arr, p+1, high)
	}
	return Arr
}

// Example
func main() {
	test_array := []int{2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3}
	fmt.Println(test_array) // unsorted
	test_array = quickSort(test_array, 0, len(test_array) - 1)
	fmt.Println(test_array) // sorted
}