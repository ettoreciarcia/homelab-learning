package main

import (
	"fmt"

	"log"
	"net/http"
	"os"
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

	os.Setenv("FOO", "1")
	fmt.Println("FOO: ", os.Getenv("FOO"))
	fmt.Println("TEST:", os.Getenv("TEST"))

	var PORT = os.Getenv("PORT")

	fmt.Printf("Starting server at port %v:\n", PORT)
	if err := http.ListenAndServe(":4000", nil); err != nil {
		log.Fatal(err)
	}

}
