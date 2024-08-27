// Selection Sort
// Golang
// Porter L

package main
import ("fmt")

func selectionSort(Arr []int) []int {
	for x := 0; x < len(Arr); x++ {
		var min_index = x
		for y := x+1; y < len(Arr); y++ {
			if Arr[min_index] > Arr[y] {
				min_index = y
			}
		}
		var b = Arr[x]
		Arr[x] = Arr[min_index]
		Arr[min_index] = b
	}
	return Arr
}

// Example
func main() {
	test_array := []int{2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3}
	fmt.Println(test_array) // unsorted
	test_array = selectionSort(test_array)
	fmt.Println(test_array) // sorted
}