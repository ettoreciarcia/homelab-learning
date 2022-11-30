package main

import (
	"fmt"
	"math/rand"
)

func main() {
	//for_loop()
	test()
}

func for_loop() {
	for i := 0; i < 10; i++ {
		random()
	}
}

func random() {
	fmt.Println("My favorite number is", rand.Intn(10))
}

func test() {
	var bool = false
	if bool {
		fmt.Println("A = 0")
	}

}
