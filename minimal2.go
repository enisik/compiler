package main

import "fmt"

func main(){
    var a float64 =  -5
    var b = 3
    //var c = 1.2222222222 * 2
    //var d = 42
    //fmt.Println(a)
    //fmt.Println(b)
	//fmt.Println(c)
    //fmt.Println(d)

    if b >= 4 {
        if b <= 2 {
            fmt.Println(-a)
        } else {
            fmt.Println(b)
        }
    } else {
        fmt.Println(a)
    }
}