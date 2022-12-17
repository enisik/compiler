package main

import "fmt"

func main() {
   var a int = 15

   for a < 20 {
      a = a + 1
      fmt.Println("value of a: %d\n")
   }
}