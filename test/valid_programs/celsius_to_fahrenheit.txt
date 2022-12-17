package main

import "fmt"

func main() {
    var ftemp float64 = 0
    var ctemp float64 = 24
    ftemp = (ctemp*1.8)+32

    fmt.Println("Temperature in Fahrenheit: %.2f",ftemp)
}
