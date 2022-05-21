package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	fmt.Println("Hello World")

	mydata := []byte("Questa è la stringa che vogliamo scrivere sul file")

	// the WriteFile method returns an error if unsuccessful
	err := ioutil.WriteFile("myfile.txt", mydata, 0777)
	// handle this error
	if err != nil {
		// print it out
		fmt.Println(err)
	}

	data, err := ioutil.ReadFile("myfile.txt")
	if err != nil {
		fmt.Println(err)
	}

	fmt.Print(string(data))

}
