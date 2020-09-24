// Bubble Sort
// Golang
// Porter L

package main
import ("fmt")

func bubbleSort(data []int) []int {
	for i := 0; i < len(data); i++ {
		for j := 1; j < len(data)-i; j++ {
			if data[j] < data[j-1] {
				data[j], data[j-1] = data[j-1], data[j]
			}
		}
	}
	return data
}

// Example
func main() {
	test_array := []int{2,7,22,71,5,3,11,9,7,5,4,3,56,3,23,43,97,3}
	fmt.Println(test_array) // unsorted
	test_array = bubbleSort(test_array)
	fmt.Println(test_array) // sorted
}
