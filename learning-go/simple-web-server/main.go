package main

import (
	"fmt"
	"log"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/hello" {
		http.Error(w, "404 not found.", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "Method is not supported.", http.StatusNotFound)
		return
	}

	fmt.Fprintf(w, "Hello! This is the first version of my web application!")
}

func main() {
	http.HandleFunc("/hello", helloHandler) // Update this line of code

	fmt.Printf("Starting server at port 4000\n")
	if err := http.ListenAndServe(":4000", nil); err != nil {
		log.Fatal(err)
	}
}
