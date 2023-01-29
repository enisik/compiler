package main

import "fmt"

func main() {
    var a bool = false
    var b bool = a && true
    a = b || true
    b = b == false
    a = b != a
}