// Insertion Sort
// Golang
// Porter L

package main
import ("fmt")

func insertionSort(Arr []int) []int {
	for x := 0; x < len(Arr); x++ {
		var key = Arr[x]
		var y = x - 1
		for y >= 0 && key < Arr[y] {
			Arr[y + 1] = Arr[y]
			y = y - 1
		}
		Arr[y+1] = key
	}
	return Arr
}

// Example
func main() {
	test_array := []int{2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3}
	fmt.Println(test_array) // unsorted
	test_array = insertionSort(test_array)
	fmt.Println(test_array) // sorted
}