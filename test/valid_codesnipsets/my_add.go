package main

import "fmt"

func main() {
	//MyAdd()
	//MyAdd(2)
	MyAdd(1,2)
	//MyAdd(1,2,3)
}

func MyAdd(a int, b int) int
{
	var c int = 0
	c = a+b
	return c
}