package main

import "fmt"

func main(){
    var a int =  -5
    var c = 3 + 4
    var d = a + 12

    a = c + a
	a = a / 2
    a = d % 2
	fmt.Println(a)
}