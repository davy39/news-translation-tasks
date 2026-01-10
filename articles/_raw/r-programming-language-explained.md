---
title: R Programming Language Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/r-programming-language-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d09740569d1a4ca358a.jpg
tags:
- name: R Programming
  slug: r-programming
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: R is an open source programming language and software environment for statistical
  computing and graphics. It is one of the primary languages used by data scientists
  and statisticians alike. It is supported by the R Foundation for Statistical Computin...
---

R is an open source programming language and software environment for statistical computing and graphics. It is one of the primary languages used by data scientists and statisticians alike. It is supported by the R Foundation for Statistical Computing and a large community of open source developers. Since R utilized a command line interface, there can be a steep learning curve for some individuals who are used to using GUI focused programs such as SPSS and SAS so extensions to R such as RStudio can be highly beneficial. Since R is an open source program and freely available, there can a large attraction for academics whose access to statistical programs are regulated through their association to various colleges or universities.

## **Installation**

The first thing you need to get started with R is to download it from its [official site](https://www.r-project.org/) according to your operating system.

## **Popular R Tools and Packages**

* [RStudio](https://www.rstudio.com/products/rstudio/) is an integrated development environment (IDE) for R. It includes a console, syntax-highlighting editor that supports direct code execution, as well as tools for plotting, history, debugging and workspace management.
* [The Comprehensive R Archive Network (CRAN)](https://cran.r-project.org/) is a leading source for R tools and resources.
* [Tidyverse](https://www.tidyverse.org/) is an opinionated collection of R packages designed for data science like ggplot2, dplyr, readr, tidyr, purr, tibble.
* [data.table](https://github.com/Rdatatable/data.table/wiki) is an implementation of base `data.frame` focused on improved performance and terse, flexible syntax.
* [Shiny](https://shiny.rstudio.com/) framework for building dashboard style web apps in R.

## Data Types in R

### Vector

It is a sequence of data elements of the same basic type. For example:

```text
> o <- c(1,2,5.3,6,-2,4)                             	 # Numeric vector
> p <- c("one","two","three","four","five","six")    	 # Character vector
> q <- c(TRUE,TRUE,FALSE,TRUE,FALSE,TRUE)                # Logical vector
> o;p;q
[1]  1.0  2.0  5.3  6.0 -2.0  4.0
[1] "one"   "two"   "three" "four"  "five"  "six"
[1]  TRUE  TRUE FALSE  TRUE FALSE
```

### Matrix

It is a two-dimensional rectangular data set. The components in a matrix also must be of the same basic type like vector. For example:

```text
> m = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
> m
>[,1] [,2] [,3]
[1,] "a"  "a"  "b" 
[2,] "c"  "b"  "a"
```

### Data Frame

It is more general than a matrix, in that different columns can have different basic data types. For example:

```text
> d <- c(1,2,3,4)
> e <- c("red", "white", "red", NA)
> f <- c(TRUE,TRUE,TRUE,FALSE)
> mydata <- data.frame(d,e,f)
> names(mydata) <- c("ID","Color","Passed")
> mydata
```

### Lists

It is an R-object which can contain many different types of elements inside it like vectors, functions and even another list inside it. For example:

```text
> list1 <- list(c(2,5,3),21.3,sin)
> list1
[[1]]
[1] 2 5 3
[[2]]
[1] 21.3
[[3]]
function (x)  .Primitive("sin")
```

## Functions in R

A function allows you to define a reusable block of code that can be executed many times within your program.

Functions can be named and called repeatedly or can be run anonymously in place (similar to lambda functions in python).

Developing full understanding of R functions requires understanding of environments. Environments are simply a way to manage objects. An example of environments in action is that you can use a redundant variable name within a function, that won’t be affected if the larger runtime already has the same variable. Additionally, if a function calls a variable not defined within the function it will check the higher level environment for that variable.

### **Syntax**

In R, a function definition has the following features:

1. The keyword `function`
2. a function name
3. input parameters (optional)
4. some block of code to execute
5. a return statement (optional)

```text
# a function with no parameters or returned values
sayHello() = function(){
  "Hello!"
}

sayHello()  # calls the function, 'Hello!' is printed to the console

# a function with a parameter
helloWithName = function(name){
  paste0("Hello, ", name, "!")
}

helloWithName("Ada")  # calls the function, 'Hello, Ada!' is printed to the console

# a function with multiple parameters with a return statement
multiply = function(val1, val2){
  val1 * val2
}
  
multiply(3, 5)  # prints 15 to the console
```

Functions are blocks of code that can be reused simply by calling the function. This enables simple, elegant code reuse without explicitly re-writing sections of code. This makes code both more readable, makes for easier debugging, and limits typing errors.

Functions in R are created using the `function` keyword, along with a function name and function parameters inside parentheses.

The `return()` function can be used by the function to return a value, and is typically used to force early termination of a function with a returned value. Alternatively, the function will return the final printed value.

```text
# return a value explicitly or simply by printing
sum = function(a, b){
  c = a + b
  return(c)
}

sum = function(a, b){
  a + b
}


result = sum(1, 2)
# result = 3
```

You can also define default values for the parameters, which R will use when a variable is not specified during function call.

```text
sum = function(a, b = 3){
  a + b
}

result = sum(a = 1)
# result = 4
```

You can also pass the parameters in the order you want, using the name of the parameter.

```text
result = sum(b=2, a=2)
# result = 4
```

R can also accept additional, optional parameters with ’…’

```text
sum = function(a, b, ...){
  a + b + ...
}

sum(1, 2, 3) #returns 6
```

Functions can also be run anonymously. These are very useful in combination with the ‘apply’ family of functions.

```text
# loop through 1, 2, 3 - add 1 to each
sapply(1:3,
       function(i){
         i + 1
         })
```

### **Notes**

If a function definition includes arguments without default values specified, values for those values must be included.

```text
sum = function(a, b = 3){
a + b
}

sum(b = 2) # Error in sum(b = 2) : argument "a" is missing, with no default
```

Variables defined within a function only exist within the scope of that function, but will check larger environment if variable not specified

```text
double = function(a){
a * 2
}

double(x)  # Error in double(x) : object 'x' not found


double = function(){
a * 2
}

a = 3
double() # 6
```

### In-built functions in R

* R comes with many functions that you can use to do sophisticated tasks like random sampling.
* For example, you can round a number with the `round()`, or calculate its factorial with the `factorial()`.

```r
> round(4.147)
[1] 4
> factorial(3)
[1] 6
> round(mean(1:6))
[1] 4
```

* The data that you pass into the function is called the function’s argument.
* You can simulate a roll of the die with R’s `sample()`function. The `sample()` function takes two arguments:a vector named x and a number named size. For example:

```r
> sample(x = 1:4, size = 2)
[] 4 2
> sample(x = die, size = 1)
[] 3
>dice <- sample(die, size = 2, replace = TRUE)
>dice
[1] 2 4
>sum(dice)
[1] 6
```

* If you’re not sure which names to use with a function, you can look up the function’s arguments with args.

```r
> args(round)
[1] function(x, digits=0)
```

## **Objects in R**

R allows to save the data by storing it inside an R object.

### What’s an object?

It is just a name that you can use to call up stored data. For example, you can save data into an object like a or b.

```r
> a <- 5
> a
[1] 5
```

### How to create an Object in R?

1. To create an R object, choose a name and then use the less-than symbol, `<`, followed by a minus sign, `-`, to save data into it. This combination looks like an arrow, `<-`. R will make an object, give it your name, and store in it whatever follows the arrow.
2. When you ask R what’s in a, it tells you on the next line. For example:

```r
> die <- 1:6
> die
[1] 1 2 3 4 5 6
```

1. You can name an object in R almost anything you want, but there are a few rules. First, a name cannot start with a number. Second, a name cannot use some special symbols, like `^, !, $, @, +, -, /, or *`:
2. R also understands capitalization (or is case-sensitive), so name and Name will refer to different objects.
3. You can see which object names you have already used with the function `ls()`.

## More Information:

* [Learn R programming language basics in just 2 hours with this free course on statistical programming](https://www.freecodecamp.org/news/r-programming-course/)
* [An introduction to web scraping using R](https://www.freecodecamp.org/news/an-introduction-to-web-scraping-using-r-40284110c848/)
* [An introduction to aggregates in R: a powerful tool for playing with data](https://www.freecodecamp.org/news/aggregates-in-r-one-of-the-most-powerful-tool-you-can-ask-for-4dd14eafff1f/)

