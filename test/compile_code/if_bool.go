package main

import "fmt"

func main() {
	var b bool = false
    if b || false {
		fmt.Println(b)
	} else {
		fmt.Println("Bye World!")
	}

}
