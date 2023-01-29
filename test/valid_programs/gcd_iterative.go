package main

import "fmt"

func main(){
    fmt.Println(gcd_iterative(42,2))
}

func gcd_iterative(a int, b int) int {
    var c int = 0
	for b != 0 {
        c = b
        b =  a%b
        a = c
	}
	return a
}