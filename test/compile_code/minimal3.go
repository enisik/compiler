package main

import "fmt"

func main() {
    var i float64 = 10

    for i >= 0 {
        fmt.Println(i)
        i = i - 1.0
    }
}
