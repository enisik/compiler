package main

import "fmt"

func main() {
	printHello(3)
}

func printHello(a int) {
	fmt.Println("Hello")
	fmt.Println(a)
}