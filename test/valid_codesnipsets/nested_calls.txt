package main

import "fmt"

func main() {
	fmt.Println(MyAdd(MyAdd(1,2),MyAdd(3,4)))
}

func MyAdd(a int, b int) int
{
	var c int = 0
	c = a+b
	return c
}