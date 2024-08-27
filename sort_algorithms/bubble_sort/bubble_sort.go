// Bubble Sort
// Golang
// Porter L

package main
import ("fmt")

func bubbleSort(Arr []int) []int {
	for x := 0; x < len(Arr); x++ {
		for y := 1; y < len(Arr)-x; y++ {
			if Arr[y] < Arr[y-1] {
				Arr[y], Arr[y-1] = Arr[y-1], Arr[y]
			}
		}
	}
	return Arr
}

// Example
func main() {
	test_array := []int{2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3}
	fmt.Println(test_array) // unsorted
	test_array = bubbleSort(test_array)
	fmt.Println(test_array) // sorted
}
