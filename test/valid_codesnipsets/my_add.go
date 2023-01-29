package main

import "fmt"

func main() {
	fmt.Println(MyAdd(1,1))
	fmt.Println(MyAdd(2,2))
	fmt.Println(MyAdd(1,2))
	fmt.Println(MyAdd(-4,5))
}

func MyAdd(a int, b int) int
{
	var c int = 0
	c = a+b
	return c
}