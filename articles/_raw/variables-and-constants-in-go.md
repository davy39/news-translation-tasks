---
title: What are Variables and Constants in Go? Explained With Examples
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2024-08-19T07:26:50.337Z'
originalURL: https://freecodecamp.org/news/variables-and-constants-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724052347929/f54eba57-fa4b-4b81-821e-41826d592933.jpeg
tags:
- name: Go
  slug: go-cjffccfnf0024tjs1mcwab09t
- name: beginner
  slug: beginner
seo_title: Variables and Constants in Go
seo_desc: 'Variables and constants are fundamental concepts in most programming languages.
  They are the building blocks for storing and managing data.

  In this article, we''ll take a look at how variables and constant work in Go.

  Table of contents:


  What are Vari...'
---

Variables and constants are fundamental concepts in most programming languages. They are the building blocks for storing and managing data.

In this article, we'll take a look at how variables and constant work in Go.

## Table of contents:

* [What are Variables?](#heading-what-are-variables)
    
* [How to Create a Variable](#heading-how-to-create-a-variable-in-go)
    
* [Explicit Declaration](#heading-explicit-declaration)
    
* [Shorthand Variable Declaration](#heading-shorthand-variable-declaration)
    
* [Multiple Variable Declarations](#heading-multiple-variable-declarations)
    
* [Zero Values](#heading-zero-values)
    
* [What is a Variable Scope](#heading-what-is-a-variable-scope)
    
* [Naming Conventions in Go](#heading-naming-conventions-in-go)
    
* [What are Constants in Go](#heading-what-are-constants-in-go)
    
* [How to Declare Constants in Go](#heading-how-to-declare-constants-in-go)
    
* [Type of Constants in Go](#heading-types-of-constants-in-go)
    
* [That's a Wrap](#heading-thats-a-wrap)
    

## What are Variables ?

A variable is a storage location identified by a name (or identifier) that holds a value. This value can change (or vary) during a program's execution. This is why it's called a variable.

For example:

```go
myName := “temitope”

fmt.Println(myName)

myName:= ”oyedele”

fmt.Println(myName)
```

We created a variable with an identifier of `myName` which holds a string value.

If you noticed, we changed the value to another string, and we can do that multiple times because variables are allowed to do that.

Variables allow you to store data, which can be of different types, such as integers, floating-point numbers, strings, or objects.

## How to Create a Variable in Go

There are two primary ways to create a variable in Go, explicit declaration and shorthand declaration.

### Explicit Declaration

This is the traditional way to create a variable in Go. It works by using the `var` keyword and declaring the variable’s type, making your code more readable and clear.

```go
package main

import "fmt"

func main() {

	var age int = 25

	var name string = "Temitope"

	var height float64 = 5.7

	fmt.Println(age, name, height)

}
```

You can see that, for each variable, we declared its datatype before assigning a value to it.

```plaintext
output:
25 Temitope 5.7
```

The `var` keyword and data type can also be used without having an initial value:

```go
package main

import "fmt"

func main() {
	var age int
	var name string
	var height float64

	age = 25
	name = "Temitope"
	height = 5.7

	fmt.Println(age, name, height)
}
```

This way, the variables are declared first without an initial value. They are then assigned values later in the code. You'll still have the same output as the first.

### Shorthand Variable Declaration

The shorthand variable declaration syntax (`:=`) is a more concise way to declare variables. This method allows you to declare and initialize a variable in a single line without explicitly stating its type, as the type is inferred from the value assigned.

```go
package main

import "fmt"

func main() {

	age := 25

	name := "Temitope"

	height := 5.7

	fmt.Println(age, name, height)

}
```

Here, each variable was declared alongside its value, with Go inferring the datatype. For example, `age` was declared and initialized with a value of 25, and Go inferred its type as `int`. `name` was declared with the value "Temitope", and Go inferred its type as `string`. Lastly, `height` was declared with 5.7, and Go inferred its type as `float64`.

```plaintext
output:
25 Temitope 5.7
```

One of the drawbacks of the shorthand variable declaration is that you can only use it inside of a function.

## Multiple Variable Declarations

You can declare and initialize multiple variables on the same line by separating each variable with a comma. This approach is simple and straightforward. it is commonly used when the variables are related or when you want to initialize them together. For example:

```go
package main

import "fmt"

func main() {

	var age, height int = 25, 180

	var name, city string = "Temitope", "New York"

	fmt.Println(age, height)

	fmt.Println(name, city)
}
```

Here, the variable `age` and `height` are both declared as integers and initialized with the values 25 and 180, respectively. Variable `name` and `city` are also both declared as strings and initialized with "Temitope" and "New York":

```plaintext
Output:
25 180
Temitope New York
```

You can also declare multiple variables in a block like so:

```go
package main

import "fmt"

func main() {

	var (
		age int = 25

		name string = "Temitope"

		height int = 180

		city string = "New York"
	)

	fmt.Println(age, name, height, city)

}
```

Here, the variables `age`, `name`, `height`, and `city` are declared within a single var block, with each variable getting its own line.

```plaintext
Output:
25 Temitope 180 New York
```

### Zero Values

When variables are declared without being initialized, they are assigned zero values by default. These values differ depending on the type of variable. Below is an example of how you can declare default values:

```go
package main

import "fmt"

func main() {

	var intValue int

	var floatValue float64

	var boolValue bool

	var stringValue string

	var ptrValue *int

	var sliceValue []int

	var mapValue map[string]int

	fmt.Println("Zero values:")

	fmt.Println("int:", intValue)

	fmt.Println("float64:", floatValue)

	fmt.Println("bool:", boolValue)

	fmt.Println("string:", stringValue)

	fmt.Println("pointer:", ptrValue)

	fmt.Println("slice:", sliceValue)

	fmt.Println("map:", mapValue)

}
```

In the code above, here’s what’s going to happen:

* The integer `intValue` will be given the zero value 0.
    
* The floating-point number `floatValue` will be given the zero value 0.
    
* The Boolean `boolValue` will be given the zero value `false`.
    
* The string `stringValue` will be given the zero value "" (empty string).
    
* The pointer `ptrValue`, slice `sliceValue`, and map `mapValue` will all be given the zero value `nil`.
    

Output:

```plaintext
Output:
Zero values:
int: 0
float64: 0
bool: false
string: 
pointer: <nil>
slice: []
map: map[]
```

### What is a Variable Scope?

Variables can be declared either globally or locally. The scope of a variable determines where it can be accessed and modified within your code.

Global variables are declared outside of any function, typically at the top of a file, and they can be accessed by any function within the same package.  Here’s an example:

```go
package main

import "fmt"

var globalCounter int = 0

func incrementCounter() {

	globalCounter++

}

func main() {

	fmt.Println("Initial Counter:", globalCounter)

	incrementCounter()

	fmt.Println("After Increment:", globalCounter)

}
```

In the above example, `globalCounter` is the global variable, and it is accessible by both the `incrementCounter` function and the `main` function.

Also, the value of `globalCounter` persists across function calls. This means that whatever change is made to it in one function affects its value in other parts of the program.

Local variables, on the other hand, are declared within a function or a block and are only accessible within that specific function or block. They are created when the function or block is executed and destroyed once it is completed. For example:

```go
package main

import "fmt"

func incrementCounter() {

	localCounter := 0

	localCounter++

	fmt.Println("Local Counter:", localCounter)

}

func main() {

	incrementCounter()

	incrementCounter()

}
```

In the code above, we have the `localCounter` as the local variable inside the `incrementCounter` function. Each time `incrementCounter` is called, a new `localCounter` is created, initialized to 0, and incremented.

The value of `localCounter` does not persist between function calls, so it cannot affect any part of a program when a change is made to the function.

## Naming Conventions in Go

Proper naming of variables is crucial for writing clean, readable, and maintainable code. Go has some specific conventions and rules for naming variables. Below are some of them:

* **Use descriptive names:**  Use names that clearly describe the purpose or content of the variable. For example, instead of using vague names like x or y, use names like `age`, `totalPrice`, or `userName` that clearly convey what the variable represents.
    
* **Use CamelCase for Multi-Word Names:** In Go, it's common practice to use camelCase for variable names that consist of multiple words. The first word is lowercase, and the first letter of each subsequent word is capitalized.
    
* **Avoid Using Underscores:** Unlike some other languages, Go prefers camelCase over using underscores to separate words in variable names. Stick to camelCase to adhere to Go’s idiomatic style.
    
* **Use Short Names for Short-Lived Variables:** For short-lived variables, such as loop counters or indices, it's acceptable to use short names like i, j, or k.
    

## What are Constants in Go?

Constants are immutable values defined at compile time that cannot be modified throughout the program's execution. They are useful for defining values that are known ahead of time and will remain the same.

Imagine you're building an online store where the standard shipping fee is always $10. You can declare it as a constant, so you can use it throughout your program whenever shipping charges need to be applied. If the shipping rates change, you only need to update the value in one place.

## How to Declare Constants in Go

You can declare constants using the `const` keyword, followed by the name, the type (optional if the value implies the type), and the value of the constant. Here’s how:

```go
package main

import "fmt"

func main() {

	const pi float64 = 3.14159

	const greeting string = "Hello, World!"

	fmt.Println("Pi:", pi)

	fmt.Println("Greeting:", greeting)

}
```

If you try to change a constant after being declared, then you’ll get a compile-time error.

## Types of Constants in Go

Constants can be categorized as either typed or untyped. Both types of constants serve the same purpose. They provide fixed, immutable values throughout the program. However, they differ in how Go handles their types and how flexible they are when used.

Untyped constants are not assigned a type unless they are used in a context that requires a type. When you declare an untyped constant, Go will infer the type at the point where the constant is used. This makes untyped constants more flexible because they can be used in a number of settings without requiring type conversion.

```go
package main

import "fmt"

const gravity = 9.81

func main() {

	var height int = 10

	var acceleration float64 = gravity * float64(height)

	fmt.Println("Acceleration:", acceleration)

}
```

Here, `gravity` is the untyped constant. This means Go can infer its type based on how it is used. When `gravity` is used in a calculation with a `float64`, Go will automatically treat it as a `float64`.

Unlike untyped constants, the typed constants have an explicitly declared type. This means they can only be used in contexts that match that type or can be converted to a compatible type. Typed constants are stricter, ensuring that the value is always treated as the specific type it was declared with.

```go
package main

import "fmt"

const speedOfLight int = 299792458

func main() {

	var distance int = speedOfLight * 2

	fmt.Println("Distance:", distance)

}
```

Here, `speedOfLight` is the typed constant with the type `int`.

It can only be used in operations with other `int` values or converted explicitly to a different type.

## That’s a Wrap

In this article, we took a look at what variables and constants are and how to declare them in Go.

Variables and constants are critical tools in programming. They allow developers to efficiently manage and manipulate data. When you understand how to use them, you can improve the quality of your code. 

Please share if you found this helpful.
