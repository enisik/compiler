package main

import "fmt"
/*
  Go program for
  Calculate GCD of two numbers using recursion
*/

func main() {
	
	// Test Cases
	gcd(15, 20)
	gcd(24, 75)
	gcd(45, 30)
	gcd(21, 49)
	gcd(16, 40)
}


// Recursively find GCD of two given number
func findGCD(first int, second int) int {
	if first == 0 {
		return second
	}
	// recursively call findGCD
	return findGCD(second % first, first)
}
func gcd(n1 int, n2 int) {
	// Get GCD of two number
	var result int = findGCD(n1, n2)
	fmt.Println("Numbers")
	fmt.Println(n1)
	fmt.Println(n2)
	fmt.Println("GCD")
	fmt.Println(result)
}