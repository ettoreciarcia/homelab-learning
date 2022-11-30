package main

import "fmt"

func Hello() string {
	return "Hello, world."
}

func Sum(a, b int) int {
	return a + b
}

func main() {
	fmt.Println(Hello())
}
