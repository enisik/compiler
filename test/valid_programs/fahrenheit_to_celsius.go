package main
import "fmt"

func main() {
    var ftemp float64=0
    var ctemp float64=0
    ctemp= (ftemp - 32) / 1.8
    fmt.Println("Temperature in Celsius:")
    fmt.Println(ctemp)
}