---
title: How to Write Benchmark Tests for Your Golang Functions
subtitle: ''
author: Pedro
co_authors: []
series: null
date: '2024-09-23T14:37:10.472Z'
originalURL: https://freecodecamp.org/news/how-to-write-benchmark-tests-for-your-golang-functions
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726668982641/58540086-9f98-4ac9-8c8a-84ef45e27875.png
tags:
- name: golang
  slug: golang
- name: Golang developer
  slug: golang-developer
- name: Testing
  slug: testing
- name: Benchmark
  slug: benchmark
seo_title: null
seo_desc: 'Hello Gophers 👋

  Let me start by asking you a question: How would you test the performance of a piece
  of code or a function in Go? Well, you could use benchmark tests.

  In this tutorial, I will show you how to use an awesome benchmarking tool that’s
  b...'
---

Hello Gophers 👋

Let me start by asking you a question: How would you test the performance of a piece of code or a function in Go? Well, you could use **benchmark** tests.

In this tutorial, I will show you how to use an awesome benchmarking tool that’s built into the Golang testing package.

Let’s go.

## What Are Benchmark Tests?

In Go, [benchmark tests](https://pkg.go.dev/testing#hdr-Benchmarks) are used to measure the performance (speed and memory usage) of functions or blocks of code. These tests are part of the Go testing framework and are written in the same files as unit tests, but they are specifically for performance analysis.

## Example Use Case: Fibonacci Sequence

For this example, I'll be using the classic Fibonacci Sequence, which is determined by:

```plaintext
if (x < 2) 
   F(0) = 1
   F(2) = 2
else 
   F(x) = F(x-1) + F(x-2)

In practice, the sequence is:
1, 1, 2, 3, 5, 8, 13, etc.
```

This sequence is important because it appears in various parts of mathematics and nature as well, as shown below:

![Fibonacci sequence in a spiral (like a snail shell)](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v6fqdlmiqjob46joyfpz.png align="left")

There are several ways to implement this code, and I'll be picking two of them for our benchmark testing: the recursive and iterative methods. The main objective of the functions is to provide a *position* and return the Fibonacci number at that position.

### Recursive Method

```go
// main.go
func fibRecursive(n uint) uint {
	if n <= 2 {
		return 1
	}
	return fibRecursive(n-1) + fibRecursive(n-2)
}
```

The function above is a recursive implementation of calculating the Fibonacci sequence. Now I’ll break it down step by step for you as a beginner in Go.

Here’s your function for calculating the Fibonacci numbers:

```go
func fibRecursive(n uint) uint {
	if n <= 2 {
		return 1
	}
	return fibRecursive(n-1) + fibRecursive(n-2)
}
```

#### 1\. **Function:**

```go
func fibRecursive(n uint) uint
```

* `func`: This keyword defines a function in Go.
    
* `fibRecursive`: This is the name of the function. It’s called `fibRecursive` because it calculates Fibonacci numbers using recursion.
    
* `n uint`: The function takes a single argument, `n`, which is of type `uint` (an unsigned integer). This represents the position of the Fibonacci sequence that we want to calculate.
    
* `uint`: The function returns a `uint` (unsigned integer) because Fibonacci numbers are non-negative integers.
    

#### 2\. **Base Stage:**

```go
if n <= 2 {
    return 1
}
```

* The `if` statement checks if `n` is less than or equal to 2.
    
* In the Fibonacci sequence, the 1st and 2nd numbers are both 1. So, if `n` is 1 or 2, the function returns 1.
    
* This is called the **base stage,** and it stops the recursion from going infinitely deep.
    

#### 3\. **Recursive Stage:**

```go
return fibRecursive(n-1) + fibRecursive(n-2)
```

* If `n` is greater than 2, the function calls itself twice:
    
    * `fibRecursive(n-1)`: This will calculate the Fibonacci number for the position just before `n`.
        
    * `fibRecursive(n-2)`: This will calculate the Fibonacci number for two positions before `n`.
        
* The function then adds these two results together, because every Fibonacci number is the sum of the two preceding numbers.
    

For more theory on recursion, check out these [articles](https://www.freecodecamp.org/news/tag/recursion/).

### Iterative Method

```go
// main.go

func fibIterative(position uint) uint {
	slc := make([]uint, position)
	slc[0] = 1
	slc[1] = 1

	if position <= 2 {
		return 1
	}

	var result, i uint
	for i = 2; i < position; i++ {
		result = slc[i-1] + slc[i-2]
		slc[i] = result
	}

	return result
}
```

This code implements an **iterative** approach to calculate the Fibonacci sequence in Go, which is different from the **recursive** approach. Here’s a breakdown of how it works:

#### 1\. **Function:**

```go
func fibIterative(position uint) uint
```

* `func`: This keyword declares a function in Go.
    
* `fibIterative`: The name of the function suggests that it calculates Fibonacci numbers using iteration (a loop).
    
* `position uint`: The function takes one argument, `position`, which is an unsigned integer (`uint`). This represents the position of the Fibonacci sequence you want to calculate.
    
* `uint`: The function returns an unsigned integer (`uint`), which will be the Fibonacci number at the specified position.
    

#### 2\. **Creating a Slice (Array-like structure):**

```go
slc := make([]uint, position)
```

* `slc` is a slice (a dynamic array in Go) that is created with the length of `position`. This slice will store Fibonacci numbers at each index.
    

#### 3\. **Initial Values for Fibonacci Sequence:**

```go
slc[0] = 1
slc[1] = 1
```

* The first two Fibonacci numbers are both `1`, so the first two positions in the slice (`slc[0]` and `slc[1]`) are set to `1`.
    

#### 4\. **Early Return for Small Positions:**

```go
if position <= 2 {
	return 1
}
```

* If the input `position` is `1` or `2`, the function directly returns `1`, because the first two Fibonacci numbers are always `1`.
    

#### 5\. **Iterative Loop:**

```go
var result, i uint
for i = 2; i < position; i++ {
	result = slc[i-1] + slc[i-2]
	slc[i] = result
}
```

* The loop starts from `i = 2` and runs until it reaches the `position`.
    
* In each iteration, the Fibonacci number at index `i` is calculated as the sum of the two previous Fibonacci numbers (`slc[i-1]` and `slc[i-2]`).
    
* The result is stored both in `result` and in the slice `slc[i]` for future calculations.
    

#### 6\. **Returning the Result:**

```go
return result
```

* Once the loop finishes, the variable `result` holds the Fibonacci number at the desired position, and the function returns it.
    

This is a more *efficient* approach to calculating Fibonacci numbers compared to recursion, especially when `position` is large, because **it doesn’t repeat unnecessary calculations** and we are proving by using benchmark tests***.*** Let’s prove it.

## How to Run the Benchmark Tests

Now, for the benchmark tests, let’s write some test. First, you will need to create a **maintest.go** file. In it, using Golang's [documentation](https://pkg.go.dev/testing@go1.22.3#hdr-Benchmarks) on benchmark tests, you can create the functions to be tested as follows:

```go
// main_test.go

// Benchmark for Iterative Function
func BenchmarkFibIterative(b *testing.B) {
	for i := 0; i < b.N; i++ { 
		fibIterative(uint(10))
	}
}
// Benchmark for Recursive Function
func BenchmarkFibRecursive(b *testing.B) {
	for i := 0; i < b.N; i++ {
		fibRecursive(uint(10))
	}
}
```

Let's run the test for position 10 and then increase appropriately. To run the benchmark tests, you simply run the command `go test -bench=NameoftheFunction`.

If you want to know more about this command, check [here](https://pkg.go.dev/testing@go1.22.3#Benchmark). Let’s check the function for **position 10**:

```go
func BenchmarkFibIterative(b *testing.B) {
	for i := 0; i < b.N; i++ { 
		fibIterative(uint(10))
	}
}
```

```go
go test -bench=BenchmarkFibIterative
Results:
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibIterative-8         27715262                42.86 ns/op
PASS
ok      playground      2.617s
```

Let’s analyze with the help of this image:

![visit https://www.practical-go-lessons.com/chap-34-benchmarks](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/484ap11qw8d81b43gg0v.png align="left")

According to the image, we have 8 cores for the tests, and no time limit (it will run until completion). It took **27\_715\_262 iterations** and **1.651 seconds** to complete the task.

```go
func BenchmarkFibRecursive(b *testing.B) {
	for i := 0; i < b.N; i++ {
		fibRecursive(uint(10))
	}
}
```

```go
go test -bench=BenchmarkFibRecursive
Results:
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibRecursive-8          6644950               174.3 ns/op
PASS
ok      playground      1.819s
```

Using the same image to analyze the result, in this case it took **6\_644\_950 iterations** and **1.819 seconds** to complete the task we have:

| Fibonacci’s Function | Position | Iterations | Time to run (s) |
| --- | --- | --- | --- |
| Iterative | 10 | 27\_715\_262 | 1.651 |
| Recursive | 1**0** | 6\_644\_950 | 1.819 |

The **benchmark results** show that the iterative approach is significantly more efficient than the recursive approach for calculating the Fibonacci sequence.

For position 10, the iterative function ran approximately **27.7 million iterations** in **1.651 seconds**, while the recursive function managed only **6.6 million iterations** in **1.819 seconds**. The iterative method outperformed the recursive method both in terms of iterations and time, highlighting its efficiency.

To proven even further this, let’s try with the **position 40** (4 times the previous value):

```go
// Results for the Iterative Function
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibIterative-8          9904401               114.5 ns/op
PASS
ok      playground      1.741s

// Results for the Recursive Function
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibRecursive-8                4         324133575 ns/op
PASS
ok      playground      3.782s
```

| Fibonacci’s Function | Position | Iterations | Time to run (s) |
| --- | --- | --- | --- |
| Iterative | 40 | 9\_904\_401 | 1.741 |
| Recursive | 40 | 4 | 3.782 |

The benchmark results clearly highlight the efficiency difference between the iterative and recursive approaches for calculating Fibonacci again.

The **iterative function** completed approximately **9.9 million iterations** with an average execution time of **114.5 nanoseconds per operation**, finishing the benchmark in **1.741 seconds**. In stark contrast, the **recursive function** only completed **4 iterations** with an average execution time of **324,133,575 nanoseconds per operation** (over 324 milliseconds per call), taking **3.782 seconds** to finish.

These results demonstrate that the recursive approach is far less efficient due to repeated function calls and recalculations, making the iterative method vastly superior in both speed and resource usage, especially as input size increases.

Just out of curiosity, I tried **position 60** and it literally crashed the test:

```go
// Results for the Iterative Function
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibIterative-8          7100899               160.9 ns/op

// Results for the Recursive Function
SIGQUIT: quit
PC=0x7ff81935f08e m=0 sigcode=0

goroutine 0 gp=0x3bf1800 m=0 mp=0x3bf26a0 [idle]:
runtime.pthread_cond_wait(0x3bf2be0, 0x3bf2ba0)
...
```

## Conclusion

If your production code is running slowly or is unpredictably slower, you can use this technique, combined with [**pprof**](https://pkg.go.dev/runtime/pprof) or other tools from the built-in testing package, to identify and test where your code is performing poorly and work on how to optimize it.

Remember: Code that is beautiful to the eyes is not necessarily more performant.

### Reference

* Recursive & Iterative functions to Fibonacci’s sequence [here](https://gist.github.com/pedrobertao/a31466b3287f165f22d05f0fb2b066f2).
    
* Benchmark testing [here](https://gist.github.com/pedrobertao/d435d9f1b0915cbc1cb54bc385f45104).
    

### Homework

This [article](https://www.meccanismocomplesso.org/en/the-fibonacci-series-three-different-algorithms-compared/) explains why for some small numbers, the recursive strategy is better. Can you find a better way to improve the recursive function? (Tip: use Dynamic Programming).
