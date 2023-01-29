package main

import "fmt"

func main() {
    for true || !false {
        if false {

        } else {
            fmt.Println("foo")
            return
        }
    }
}