package main

import "testing"

func TestHello(t *testing.T) {
	got := Hello()
	want := "Hello, world."

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}

func TestSum(t *testing.T) {
	got := Sum(2, 1)
	want := 3

	if got != want {
		t.Errorf("got %d want %d", got, want)
	}
}
