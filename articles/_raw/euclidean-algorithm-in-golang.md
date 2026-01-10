---
title: How the Euclidean Algorithm Works – with Code Examples in Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-08T20:18:08.000Z'
originalURL: https://freecodecamp.org/news/euclidean-algorithm-in-golang
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-skitterphoto-1019470.jpg
tags:
- name: algorithms
  slug: algorithms
- name: golang
  slug: golang
- name: Mathematics
  slug: mathematics
seo_title: null
seo_desc: "By Otavio Ehrenberger\nThe Euclidean Algorithm is a well-known and efficient\
  \ method for finding the greatest common divisor (GCD) of two integers. The GCD\
  \ is the largest number that can divide both integers without leaving a remainder.\
  \ \nThe algorithm ..."
---

By Otavio Ehrenberger

The Euclidean Algorithm is a well-known and efficient method for finding the greatest common divisor (GCD) of two integers. The GCD is the largest number that can divide both integers without leaving a remainder. 

The algorithm is named after the ancient Greek mathematician Euclid, who presented it in his book "Elements" around 300 BCE.

You can use this algorithm to solve [Diophantine equations](https://en.wikipedia.org/wiki/Diophantine_equation), to tackle the [shortest-vector problem](https://en.wikipedia.org/wiki/Lattice_problem) which is the foundation of [lattice-based cryptography](https://en.wikipedia.org/wiki/Lattice-based_cryptography), and also to detect common patterns of pixels in images. This is, among other things, applied to optimize rendering processes and detect different objects in images.

## How Does the Euclidean Algorithm Work?

Here's a step-by-step explanation of how the Euclidean Algorithm works:

Start with two positive integers, a and b, where a >= b. If a < b, simply swap their values. Note that this is meant for a convenient mathematical demonstration, as the implementation also works for a < b.

Divide a by b and find the remainder, r (use the modulo operation, represented as a % b). If r is 0, the GCD is b, and the algorithm terminates.

If r is not 0, set a to b and b to r. Then, repeat step 2.

The algorithm continues to iterate until the remainder is 0. At that point, the last non-zero remainder is the GCD of the original two numbers. 

The Euclidean Algorithm works because the GCD of two numbers remains unchanged when the larger number is replaced by its remainder when divided by the smaller number.

### Example of Euclidean Algorithm

Here's an example to illustrate the algorithm:

Let's find the GCD of 30 and 9:

a = 30, b = 9

Calculate the remainder: r = a % b = 30 % 9 = 3 (since 3 is not 0, continue to step 3)

Update the values: a = 9, b = 3

Calculate the new remainder: r = a % b = 9 % 3 = 0 (r is now 0)

The GCD of 30 and 9 is 3.

## Why Does the Euclidean Algorithm Work?

The greatest common divisor of two integers is the largest positive integer that divides both of them without leaving a remainder. So the algorithm is based on the following key property:

**If `a` and `b` are two integers, then the GCD of `a` and `b` is the same as the GCD of `b` and `a % b`, where `%` represents the modulo operator (the remainder after division)**.

Mathematically, the key property of the algorithm can be justified using the division algorithm:

Let `a` and `b` be two positive integers, such that `a >= b`. We can write the division algorithm as:

`a = bq + r`, where `q` is the quotient and `r` is the remainder.

Now, let `d` be a common divisor of `a` and `b`. Then, `a = d * m1` and `b = d * m2` for some integers `m1` and `m2`. We can rewrite the division algorithm as:

`d * m1 = (d * m2) * q + r`.

Rearranging the equation, we get:

`r = d * (m1 - m2 * q)`.

Since `d` is a factor of both `a` and `b`, and `r` can also be written as a multiple of `d`, we can conclude that `d` is also a divisor of `r`. This means that the GCD of `a` and `b` is also a divisor of `r`. So, we can replace `b` with `r` and keep finding the GCD using this algorithm until `b` becomes 0.

The Euclidean Algorithm is particularly useful due to its efficiency and simplicity, making it easy to implement in computer algorithms and programming languages.

Let's see some different ways to implement it in Go:

## Recursive Implementation of the Euclidean Algorithm in Go

This implementation of the Euclidean Algorithm in Golang is a recursive version that finds the GCD of two integers. Let's go through it step by step:

The function is defined as `GCD(a, b int) int`. It takes two integer inputs, `a` and `b`, and returns an integer output.

The base case of the recursion is checked with `if b == 0`. If `b` is 0, the function returns the value of `a` as the GCD.

If `b` is not 0, a temporary variable `tmp` is created and assigned the value of `a`. This temporary variable is used to store the value of `a` before updating its value in the next step.

The values of `a` and `b` are updated as follows:

* `a` is assigned the current value of `b`.
* `b` is assigned the value of the remainder when `tmp` (the previous value of `a`) is divided by the new value of `a` (which was `b` before the update).

The function calls itself recursively with the updated values of `a` and `b` as input, `return GCD(a, b)`.

The algorithm continues to call itself recursively until the base case is reached, that is `b` becomes 0. At this point, the function returns the GCD, which is the value of `a`.

```go
// Recursive approach:
func GCD(a, b int) int {
	if b == 0 {
		return a
	}
	tmp := a
	a = b
	b = tmp % a
	return GCD(a, b)
}

```

For example, let's say we want to find the GCD of 56 and 48:

First call: GCD(56, 48)

* Since `b` (48) is not 0, update `a` and `b`:
* `a` becomes 48
* `b` becomes 56 % 48 = 8
* The function calls itself with the new values: GCD(48, 8)

Second call: GCD(48, 8)

* Since `b` (8) is not 0, update `a` and `b`:
* `a` becomes 8
* `b` becomes 48 % 8 = 0
* The function calls itself with the new values: GCD(8, 0)

Third call: GCD(8, 0)

* Now, `b` (0) is 0, so the function returns `a` (8) as the GCD.

## Iterative Implementation of the Euclidean Algorithm in Go

This implementation of the Euclidean Algorithm in Golang is an iterative version using a loop to find the GCD of two integers. Let's go through the code step by step:

The function is defined as `GCD(a, b int) int`. It takes two integer inputs, `a` and `b`, and returns an integer output.

A loop is used to iterate as long as `b` is not equal to 0. The loop condition is `b != 0`. Note that this `for` loop construction in Go is essentially a `while` loop in many other languages.

Inside the loop, the values of `a` and `b` are updated simultaneously using a tuple assignment: `a, b = b, a%b`. This line does the following:

* `a` is assigned the current value of `b`.
* `b` is assigned the value of the remainder when `a` is divided by `b`.

When the loop exits (that is, `b` becomes 0), the value of `a` is returned as the GCD.

The algorithm iterates until the remainder (`b`) is 0, at which point the GCD is the last non-zero remainder, which is the value of `a`.

```go
func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

```

For example, let's say we want to find the GCD of 100 and 64:

Initialize `a` as 100 and `b` as 64. Check the loop condition: `b` (64) is not 0.

Inside the loop, update `a` and `b`:

* `a` becomes 64
* `b` becomes 100 % 64 = 36  
Check the loop condition again: `b` (36) is not 0.

Inside the loop, update `a` and `b`:

* `a` becomes 36
* `b` becomes 64 % 36 = 28  
Check the loop condition again: `b` (28) is not 0.

Inside the loop, update `a` and `b`:

* `a` becomes 28
* `b` becomes 36 % 28 = 8  
Check the loop condition again: `b` (8) is not 0.

Inside the loop, update `a` and `b`:

* `a` becomes 8
* `b` becomes 28 % 8 = 4  
Check the loop condition again: `b` (4) is not 0.

Inside the loop, update `a` and `b`:

* `a` becomes 4
* `b` becomes 8 % 4 = 0  
Check the loop condition again: Now, `b` (0) is 0, so the loop exits.

The function returns the value of `a` (4) as the GCD.

## Testing the Solutions

These tests were created by Jon Calhoun in his free [Go Algorithms](https://courses.calhoun.io/courses/cor_algo) course. Assuming you defined your `GCD` function in a file named `gcd.go`, place these tests in a file named `gcd_test.go`. Read below to see how the tests will work:

The function `TestGCD` is defined, taking a single parameter `t *testing.T`. The `*testing.T` is a pointer to a `testing.T` object that provides methods for reporting test failures and logging additional information.

An array of anonymous structs is defined, called `tests`. Each struct has three fields: `a`, `b`, and `want`. These structs represent test cases, where `a` and `b` are input values for the GCD function, and `want` is the expected result (correct GCD).

Several test cases are defined in the `tests` array, covering different scenarios.

A `for` loop iterates through the `tests` array. In each iteration, a single test case (struct) is assigned to the variable `tc`.

The `t.Run` function is called to run a subtest for the current test case. The first argument is a formatted string that describes the test case (using the input values `tc.a` and `tc.b`). The second argument is an anonymous function that takes a `*testing.T` parameter, similar to the main test function.

Inside the subtest function, the GCD function is called with the input values `tc.a` and `tc.b`, and the result is assigned to the `got` variable.

The `got` result is compared to the expected result `tc.want`. If they are not equal, the `t.Fatalf` function is called to report the test failure and provide an error message with the incorrect result and the expected result.

This test function helps ensure that the GCD function works correctly for various input values and edge cases. Running this test function with the `go test` command will execute all the test cases and report any failures, which can help identify potential issues with the GCD function implementation.

```go

import (
	"fmt"
	"testing"
)

func TestGCD(t *testing.T) {
	tests := []struct {
		a, b int
		want int
	}{
		{10, 5, 5},
		{25, 5, 5},
		{30, 15, 15},
		{30, 9, 3},
		{100, 9, 1},
		{
			2 * 2 * 3 * 3 * 5,
			2 * 3 * 5 * 7 * 13,
			2 * 3 * 5,
		}, {
			2 * 2 * 3 * 3 * 13,
			2 * 3 * 5 * 7 * 13,
			2 * 3 * 13,
		}, {
			2 * 3 * 5 * 7 * 11 * 13 * 17 * 19,
			3 * 3 * 7 * 7 * 11 * 11 * 17 * 17,
			3 * 7 * 11 * 17,
		},
	}
	for _, tc := range tests {
		t.Run(fmt.Sprintf("(%v,%v)", tc.a, tc.b), func(t *testing.T) {
			got := GCD(tc.a, tc.b)
			if got != tc.want {
				t.Fatalf("GCD() = %v; want %v", got, tc.want)
			}
		})
	}
}

```

Run the tests, creating different cases as you wish:

```bash
go test -v # verbose flag

```

## Conclusion

Hope you had a good time learning about the Euclidean algorithm and its implementation in Go. 

If you are interested in how these clever tricks work, take a look at the field of Number Theory in mathematics, which is particularly focused on the properties of integers, especially involving prime numbers.

