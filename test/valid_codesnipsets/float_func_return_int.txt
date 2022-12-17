package main

import "fmt"

func main() {
	var a float64 = floaty()
	fmt.Println(a)
}

func floaty() float64 {
	return 42
}