---
title: Iteration in Golang – How to Loop Through Data Structures in Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-26T22:44:22.000Z'
originalURL: https://freecodecamp.org/news/iteration-in-golang
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/How-to-perform-iteration-in-Golang-1.png
tags:
- name: data structures
  slug: data-structures
- name: Go Language
  slug: go
- name: golang
  slug: golang
- name: Loops
  slug: loops
seo_title: null
seo_desc: 'By Ubaydah Abdulwasiu

  In programming, iteration (commonly known as looping) is a process where a step
  is repeated n number of times until a specific condition is met.

  Just like every other programming language, Golang has a way of iterating through
  d...'
---

By Ubaydah Abdulwasiu

In programming, iteration (commonly known as looping) is a process where a step is repeated n number of times until a specific condition is met.

Just like every other programming language, Golang has a way of iterating through different data structures and data types like structs, maps, arrays, strings, and so on.

In this article you will learn:

* How to loop through arrays
* How to loop through strings
* How to loop through maps
* How to loop through structs

## How to Loop Through Arrays and Slices in Go

Arrays are powerful data structures that store similar types of data. You can identify and access the elements in them by their index.

In Golang, you can loop through an array using a `for` loop by initialising a variable i at 0 and incrementing the variable until it reaches the length of the array.

They syntax is shown below:

```go
for i := 0; i < len(arr); i++ {
    // perform an operation
}
```

As an example, let's loop through an array of integers:

```go
package main

import (
	"fmt"
)

func main() {
	numbers := []int{7, 9, 1, 2, 4, 5}

	for i := 0; i < len(numbers); i++ {
		fmt.Println(numbers[i])

	}
}
```

In the code above, we defined an array of integers named `numbers` and looped through them by initialising a variable `i` . We then printed out the value of each index of the array while incrementing `i` .

The code above outputs the following:

```
7
9
1
2
4
5
```

We can also loop through an array using the `range` keyword which iterates through the entire length of an array. 

The syntax is shown below:

```go
for index, arr := range arr {
  // perform an operation	
}
```

For example:

```go
package main

import (
	"fmt"
)

func main() {
	arr := []string{"a", "b", "c", "d", "e", "f"}

	for index, a := range arr {
		fmt.Println(index, a)
	}

}
```

In the code above, we defined an array of strings and looped through both its index and value using the `for..range` keyword. 

The `for...range` is more simpler in syntax and easier to understand. You use it to iterate different data structures like arrays, strings, maps, slices, and so on. 

This outputs the following: 

```
0 a
1 b
2 c
3 d
4 e
5 f
```

Assuming we were to ignore the index and simply print out the elements of the array, you just replace the `index` variable with an underscore.

For example:

```go 
package main

import (
	"fmt"
)

func main() {
	arr := []string{"a", "b", "c", "d", "e", "f"}

	for _, a := range arr {
		fmt.Println(a)
	}

}
```

In the code above, we modified the previous example and replaced the `index` variable with an underscore. We did this to ignore the index and output the elements of the array instead.

This outputs the following:

```
a
b
c
d
e
f
```

## How to Loop Through Strings in Go

Strings in programming are immutable – this means you can't modify them after you create them. They're ordered sequences of one or more characters (like letters, numbers, or symbols) that can either be a constant or a variable.

In Golang, [strings](https://golangbot.com/strings/) are different from other languages like Python or JavaScript. They are represented as a [UTF-8 sequence of bytes](https://naveenr.net/unicode-character-set-and-utf-8-utf-16-utf-32-encoding/) and each element in a string represents a byte.

You loop through strings using the `for...range` loop or using a regular loop. 

For example:

```go
package main

import (
	"fmt"
)

func main() {
	word := "Ab$du"

	for index, a := range word {
		fmt.Println(index, string(a))
	}
}
```

In the code above, we defined a string containing different characters and looped through its entries. Strings are represented as bytes in Golang, which is why we needed to convert each value to the type `string` when printing them out. 

This outputs:

```
0 A
1 b
2 $
3 d
4 u
```

If we hadn't converted each entry to a string, Golang would print out the byte representation instead.

For example:

```go
package main

import (
	"fmt"
)

func main() {
	word := "Ab$du"

	for index, a := range word {
		fmt.Println(index, a)
	}
}
```

The outputs:

```
0 65
1 98
2 36
3 100
4 117
```

We can also iterate through the string by using a regular `for loop`.

```go
package main

import (
	"fmt"
)

func main() {
	word := "ab$du"

	for i := 0; i < len(word); i++ {
		fmt.Println(i, string(word[i]))
	}
}
```

## How to Loop Through Maps in Go

In Golang, a map is a data structure that stores elements in key-value pairs, where keys are used to identify each value in a map. It is similar to dictionaries and hashmaps in other languages like Python and Java.

You can iterate through a `map` in Golang using the `for...range` statement where it fetches the index and its corresponding value. 

For example:

```go
package main

import (
	"fmt"
)

func main() {
	books := map[string]int{
		"maths":     5,
		"biology":   9,
		"chemistry": 6,
		"physics":   3,
	}
	for key, val := range books {
		fmt.Println(key, val)
	}
}
```

In the code above, we defined a map storing the details of a bookstore with type `string` as its key and type `int` as its value. We then looped through its keys and values using the `for..range` keyword. 

Iterating through a map in Golang doesn't have any specified order, and we shouldn't expect the keys to be returned in the order we defined when we looped through.

This code outputs:

```
physics 3
maths 5
biology 9
chemistry 6
```

If we don't want to specify the values and return just the keys instead, we simply don't define a value variable and define a key variable only.

For example:

```go
package main

import (
	"fmt"
)

func main() {
	books := map[string]int{
		"maths":     5,
		"biology":   9,
		"chemistry": 6,
		"physics":   3,
	}
	for key := range books {
		fmt.Println(key)
	}
}
```

This outputs the following:

```
maths
biology
chemistry
physics
```

Likewise, if we aren't interested in the keys of a map, we use an underscore to ignore the keys and define a variable for the value.

For example:

```go
package main

import (
	"fmt"
)

func main() {
	books := map[string]int{
		"maths":     5,
		"biology":   9,
		"chemistry": 6,
		"physics":   3,
	}
	for _, val := range books {
		fmt.Println(val)
	}
}
```

This outputs:

```
5
9
6
3
```

## How to Loop Through Structs in Go

Struct is a data structure in Golang that you use to combine different data types into one. Unlike an array, a struct can contain integers, strings, booleans and more – all in one place.

Unlike a map, where we can easily loop through its keys and values, looping through a struct in Golang requires that you use a package called `reflect`. This allows us you modify an object with an arbitrary type.

For example, let's create a struct and loop through it:

```go
package main

import (
	"fmt"
	"reflect"
)

type Person struct {
	Name   string
	Age    int
	Gender string
	Single bool
}

func main() {
	ubay := Person{
		Name:   "John",
		Gender: "Female",
		Age:    17,
		Single: false,
	}
	values := reflect.ValueOf(ubay)
	types := values.Type()
	for i := 0; i < values.NumField(); i++ {
		fmt.Println(types.Field(i).Index[0], types.Field(i).Name, values.Field(i))
	}
}
```

This outputs:

```
0 Name John
1 Age 17
2 Gender Female
3 Single false
```

In the code above, we defined a `struct` named `Person` with different attributes and created a new instance of the `struct`. We then used the `reflect` package to get the values of the `struct` and its `type`.  

By using the regular `for` loop, we incremented the initialised variable `i` until it reached the length of the struct. 

We use the `NumField` method to get the total number of fields in the struct. The `types.Field(i).Index` method returns the index of each key in a struct. The `types.Field(i).Name` method returns the field name for each key in the struct. And the `values.Field(i)` returns the value for each key in the struct.

You can learn more about the reflect package in this article:

%[https://medium.com/capital-one-tech/learning-to-use-go-reflection-822a0aed74b7]

## Conclusion 

In this article, we have explored how to perform iteration on different data types in Golang. 

While you can loop through arrays, maps, and strings using a `for` loop or `for..range` loop, structs require an additional package called `reflect` to loop through their keys and values.

I hope this article helps you understand iteration in Golang better.

Thanks for reading.


