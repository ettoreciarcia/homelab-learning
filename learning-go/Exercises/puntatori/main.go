package main

import "fmt"

func main() {
	fmt.Println("Hello World")
	x1 := 10
	var indirizzo *int
	fmt.Println("Value x1", x1)
	fmt.Println("Pointer x1 =", &x1)
	indirizzo = &x1
	fmt.Println("Indirizzo add (indirizzo)", indirizzo)
	fmt.Println("Indirizzo add (*indirizzo)", *indirizzo)
}
