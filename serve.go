package main

// Simple Go program to preview the site locally before publishing.

import (
	"log"
	"net/http"
)

func main() {
	log.Fatal(http.ListenAndServe("localhost:8000", http.FileServer(http.Dir("site/"))))
}
