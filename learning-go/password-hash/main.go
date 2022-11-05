package main

import (
	"fmt"

	"golang.org/x/crypto/bcrypt"
)

func HashPassword(password string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), 14)
}

func main() {
	password := "secret"

	hash, _ := HashPassword(password) //ignore error for semplicity

	fmt.Println("This is your hashed password: ", hash)
}
