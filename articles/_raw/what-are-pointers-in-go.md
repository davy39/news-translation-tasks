---
title: What are Pointers in Go? A Guide for JavaScript Devs
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2023-04-24T22:07:19.000Z'
originalURL: https://freecodecamp.org/news/what-are-pointers-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/kaleb-tapp-J59wWPn09BE-unsplash.jpg
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Coming from a language like JavaScript, pointers can be kind of confusing
  at first. Here I will break it down so that they are easier to understand.

  What Are Pointers in Go?

  Just like in JavaScript, Go has variables which are locations in memory that...'
---

Coming from a language like JavaScript, pointers can be kind of confusing at first. Here I will break it down so that they are easier to understand.

## What Are Pointers in Go?

Just like in JavaScript, Go has variables which are locations in memory that store a value. 

In both languages, that value can be manipulated by assigning it a new value, or by performing operations on it. No matter what you do to that variable, it's still stored in a specific place in memory.

Pointers are another type of variable. Instead of storing a value that you will use, they store the _memory address_ of another variable. It is "pointing to" the location of the variable.

**It is not the actual data of that variable**. It is just the address of the variable it points to.

### Pointer Syntax

A pointer is defined using the `*` syntax. So to declare a pointer variable, the code would look like this:

```go
var x *int

```

This sets `x` as a pointer to an `int` value.

If you want to set a variable as a pointer to another value, you intialize it with the `&` operator.

```go
normalInt := 5
// pointerInt is set as a pointer to normalInt
pointerInt = &normalInt

normalString := "hello world"
// pointerString is set as a pointer to normalString
pointerString = &normalString

```

In order to access the underlying value of the pointer, we use the `*` operator.

```go
fmt.Println(*pointerInt) // read pointerInt through the pointer
*pointerInt = 10 // set pointerInt through the pointer

```

Here's a drawing that illustrates the concept of pointers:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Pasted-image-20230421202803.png)

### Watch for `nil` Pointers

When dereferencing a pointer, if it hasn't been pointed to anything then the program will panic. It is good practice to check a pointer to see if it is `nil` before trying to dereference it.

### Why Pointers?

When a function takes in an argument, the value of the argument is copied into the function. The function then can manipulate the copy of the variable. 

By using pointers, we can make more efficient programs. It allows us to manipulate the data the pointer references without copying it multiple times throughout the program.

While this does improve the efficiency of the program, you want to be careful when using them. It is perfectly fine to use normal variables as arguments to functions and return new values from the functions.

One place where pointers are useful is with Receivers.

### Pointer Receivers

Instead of receiving just a value, methods can receive a pointer. This allows the method to modify the value that to which the receiver points. Since methods often need to modify their receiver, pointer receivers are more common than value receivers.

```go
type ball struct {
	color string
}

func (b *ball) setColor(color string) {
	b.color = color
}

func main() {
	b := ball{
		color: "white",
	}
	b.setColor("blue")
	fmt.Println(b.color)
	// prints "blue"
}

```

Without the pointer receiver, `setColor` would not be able to modify the `color` value of the ball.

```go
type ball struct {
	color string
}

func (b ball) setColor(color string) {
	b.color = color
}

func main() {
	b := ball{
		color: "white",
	}
	b.setColor("blue")
	fmt.Println(b.color)
	// prints "white"
}

```

## Conclusion

Pointers are an essential concept in Go programming. Although they can be confusing at first, they are an important tool for making efficient programs. 

Hopefully this brief explanation will helps clear up any confusion.

