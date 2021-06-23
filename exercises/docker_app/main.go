package main

import (
	"fmt"
	"net/http"
)

func helloWorld(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello Udacity")
}

func getStatus(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Application Status")
}

func main() {
	http.HandleFunc("/", helloWorld)
	http.HandleFunc("/status", getStatus)
	http.ListenAndServe(":6112", nil)
}
