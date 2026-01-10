---
title: Variable Scope in C – Local and Global Scope Explained
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-09-08T16:40:21.000Z'
originalURL: https://freecodecamp.org/news/scope-of-variables-in-c-local-and-global-scope-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Scope-of-variables-in-c.png
tags:
- name: c programming
  slug: c-programming
- name: variables
  slug: variables
seo_title: null
seo_desc: 'In programming, you''ll often have to deal with the scope of a variable.
  The scope of a variable determines whether or not you can access and modify it inside
  a specific block of code.

  In this tutorial, you''ll learn about variable scope in the C progr...'
---

In programming, you'll often have to deal with the scope of a variable. The scope of a variable determines whether or not you can access and modify it inside a specific block of code.

In this tutorial, you'll learn about variable scope in the C programming language. You'll see some code examples to help you understand the differences between local and global variables.

## What is the Scope of a Variable?

Before going ahead to learn about local and global variable scope, let's understand what _scope_ means. 

> In simple terms, scope of a variable is its _lifetime_ in the program.

This means that the scope of a variable is the block of code in the entire program where the variable is declared, used, and can be modified. 

In the next section, you'll learn about local scope of variables

## Local Scope of Variables in C – Nested Blocks 

In this section, you'll learn how local variables work in C. You'll first code a couple of examples, and then you'll generalize the scoping principle.

▶ Here's the first example:

```c
#include <stdio.h>

int main() 
{
    int my_num = 7;
    {
        //add 10 my_num
        my_num = my_num +10;
        //or my_num +=10 - more succinctly
        printf("my_num is %d",my_num);
    }
    
    return 0;
}

```

Let's understand what the above program does. 

In C, you delimit a block of code by `{}` . The opening and closing curly braces indicate the beginning and the end of a block, respectively.

* The `main()` function has an integer variable `my_num` that's initialized to 7 in the _outer_ block.
* There's an _inner_ block that tries to add 10 to the variable `my_num`.

Now, compile and run the above program. Here's the output:

```
//Output

my_num is 17
```

You can see the following:

* The inner block is able to access the value of `my_num` that's declared in the outer block, and modify it by adding 7 to it. 
* The value of `my_num` is now 17, as indicated in the output.

## Local Scope of Variables in C – Nested Blocks Example 2

▶ Here's another related example:

```c
#include <stdio.h>

int main() 
{
    int my_num = 7;
    {
        int new_num = 10;
    } 
    printf("new_num is %d",new_num); //this is line 9
    return 0;
}
```

* In this program, the `main()` function has an integer variable `my_num` in the _outer_ block.
* Another variable `new_num` is initialized in the _inner_ block. The inner block is nested inside the outer block.
* We're trying to access and print the value of inner block's `new_num` in the _outer_ block.

If you try compiling the above code, you'll notice that it doesn't compile successfully. And you'll get the following error message:

```
Line   Message
9      error: 'new_num' undeclared (first use in this function)
```

> This is because the variable `new_num` is declared in the _inner_ block and its _scope_ is limited to the inner block. In other words, it is _local_ to the inner block and _cannot_ be accessed from the _outer_ block.

Based on the above observations, let's write down the following generic principle for local scoping of variables:

```
{
	/*OUTER BLOCK*/
    
      {
    	
        
        //contents of the outer block just before the start of this block
        //CAN be accessed here
        
        /*INNER BLOCK*/
        
        
      }
     
       //contents of the inner block are NOT accessible here
 }
```

## Local Scope of Variables in C – Different Blocks

In the previous example, you learned how variables inside the nested inner block cannot be accessed from outside the block. 

In this section, you'll understand the local scope of variables declared in different blocks.

```c
#include <stdio.h>

int main()
{
    int my_num = 7;
    printf("%d",my_num);
    my_func();
    return 0;
}

void my_func()
{
    printf("%d",my_num);
}
```

In the above example,

* The integer variable `my_num` is declared inside the `main()` function.
* Inside the `main()` function, the value of `my_num` is printed out.
* There's another function `my_func()` that tries to access and print the value of `my_num`.
* As program execution starts with the `main()` function, there's a call to `my_func()` inside the `main()` function.

▶ Now compile and run the above program. You'll get the following error message:

```
Line   Message
13     error: 'my_num' undeclared (first use in this function)
```

If you notice, on `line 13`, the function `my_func()` tried accessing the `my_num` variable that was declared and initialized inside the `main()` function.

> Therefore, the scope of the variable `my_num` is confined to the `main()` function, and is said to be _local_ to the `main()` function.

We can represent this notion of local scope generically as follows:

```
{

	/*BLOCK 1*/
    // contents of BLOCK 2 cannot be accessed here
    
}


{

	/*BLOCK 2*/
    // contents of BLOCK 1 cannot be accessed here
    
}

```

## Global Scope of Variables in C

So far, you've learned about local scope of C variables. In this section, you'll learn how you can declare global variables in C.

▶ Let's start with an example.

```c
#include <stdio.h>
int my_num = 7;

int main()
{
    printf("my_num can be accessed from main() and its value is %d\n",my_num);
    //call my_func
    my_func();
    return 0;
}

void my_func()
{
  printf("my_num can be accessed from my_func() as well and its value is %d\n",my_num);
}

```

In the above example,

* The variable `my_num` is declared outside the functions `main()` and `my_func()`.
* We try to access `my_num` inside the `main()` function, and print its value.
* We call the function `my_func()` inside the `main()` function.
* The function `my_func()` also tries to access the value of `my_num`, and print it out.

This program compiles without any error, and the output is shown below:

```
//Output
my_num can be accessed from main() and its value is 7
my_num can be accessed from my_func() as well and its value is 7
```

In this example, there are two functions – the `main()` and `my_func()`. 

However, the variable `my_num` is _not local_ to any function in the program. Such a variable that is _not local_ to any function is said to have _global_ scope and is called a _global_ variable.

This principle of global scope of variables can be summarized as shown below:

```
//all global variables are declared here
function1()
	{
    
    // all global variables can be accessed inside function1
    
    }
function2()
	{
    
    // all global variables can be accessed inside function2
     
    }
    
```

## Wrapping Up

In this tutorial, you've learned the differences between local and global scope. This is an introductory tutorial on variable scope in C. 

In C, there are certain access modifiers to control the level of access that the variables have. You can change access by using the corresponding keywords when you declare variables. 

See you all in the next tutorial. Until then, happy coding!

