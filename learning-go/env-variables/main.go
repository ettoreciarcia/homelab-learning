package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Printf("Database Password: %s", os.Getenv("TESTENV"))
	for _, pair := range os.Environ() {
		fmt.Println(pair)
	}
}
