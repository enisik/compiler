package main

import "fmt"

func main() {
	var b bool = 3 > 2
    if b || false {
		fmt.Println(b)
	} else {
		fmt.Println("Bye World!")
	}

}
