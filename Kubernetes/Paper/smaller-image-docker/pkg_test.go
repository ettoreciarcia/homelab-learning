package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
)

func TestHelloServer(t *testing.T) {
	// Create a mock request and response writer
	r, w := http.NewRequest("GET", "/path", nil), httptest.NewRecorder()

	// Call the function under test
	HelloServer(w, r)

	// Check the response status code
	if w.Result().StatusCode != http.StatusOK {
		t.Errorf("Unexpected status code: %d", w.Result().StatusCode)
	}

	// Check the response headers
	if w.Result().Header.Get("Content-Type") != "text/plain; charset=utf-8" {
		t.Errorf("Unexpected value for Content-Type header: %s", w.Result().Header.Get("Content-Type"))
	}

	// Check the response body
	if w.Body.String() != "Hello, path!" {
		t.Errorf("Unexpected output: %s", w.Body.String())
	}
	if !strings.Contains(w.Body.String(), "Hello") {
		t.Errorf("Expected 'Hello' in response body")
	}
	if !strings.Contains(w.Body.String(), "path") {
		t.Errorf("Expected 'path' in response body")
	}
}
