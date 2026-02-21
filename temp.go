package main

import "fmt"

func main() {
	numbers := []int{10, 20, 30, 40, 50}

	// 1. Off-by-one error (ArrayIndexOutOfBoundsException)
	for i := 0; i < len(numbers); i++ {
		fmt.Println("Number:", numbers[i])
	}

	// 2. NullPointerException
	text := "hello"
	if text != "" {
		fmt.Println("Text length:", len(text))
	}

	// 3. Infinite loop (logical bug)
	count := 0
	for count < 5 {
		fmt.Println("Count:", count)
		count++
	}

	// 4. Division by zero
	a := 10
	b := 2
	if b != 0 {
		fmt.Println("Result:", a/b)
	}

	// 5. Wrong string comparison (logical bug)
	s1 := "hello"
	s2 := "hello"

	if s1 == s2 {
		fmt.Println("Strings are equal")
	} else {
		fmt.Println("Strings are NOT equal")
	}
}
