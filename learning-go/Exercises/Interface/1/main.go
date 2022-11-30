package main

import "fmt"

//in Go we cannot define class but we can define methods available for some structure

type Persona struct {
	nome    string
	cognome string
}

func (p Persona) sayHello() {
	fmt.Println("Ciao " + p.nome + p.cognome)
}

func main() {
	fmt.Println("Hello World!")

	var io = Persona{"Ettore", "Ciarcia"}
	io.sayHello()
}
