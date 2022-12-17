package main
import "fmt"

func main () {
    var n int = 42
    var b bool = false
    b = mybool()
    if b {
        n = 5
    } else {
        n= 13
        return
    }
}

func mybool() bool {
    return true
}