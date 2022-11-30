//go app
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, world.")

	//find all pair number in array
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(findPair(arr, 10)) //[1,9]
}
