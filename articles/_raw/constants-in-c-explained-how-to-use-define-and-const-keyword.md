---
title: 'Constants in C Explained – How to Use #define and the const Qualifier to Define
  Constants'
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-26T21:13:20.000Z'
originalURL: https://freecodecamp.org/news/constants-in-c-explained-how-to-use-define-and-const-keyword
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/andrew-coop-9F5IWESAxL4-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'When you''re programming, there are times when you''ll want the values
  of certain variables to remain unchanged. In the C language, you''ll likely define
  them as constants.

  You can define constants in C in a few different ways. In this tutorial, you''ll
  ...'
---

When you're programming, there are times when you'll want the values of certain variables to remain unchanged. In the C language, you'll likely define them as constants.

You can define constants in C in a few different ways. In this tutorial, you'll learn how to use `#define` and the `const` qualifier to define them.

Let's get started.

## How to Use `#define` to Define Constants in C

One of the common ways to define constants in C is to use the `#define` preprocessor directive, as shown below:

```c
#define <VAR_NAME> <VALUE>
```

In the above syntax:

* `<VAR_NAME>` is a placeholder for the name of the constant. 
* It's recommended that you name constants in the _uppercase_, as it helps differentiate them from other variables defined in the program.
* `<VALUE>` is a placeholder for the value that `<VAR_NAME>` takes.
* `#define` is a preprocessor directive. 
* Before the compilation of the program, the preprocessor replaces all occurrences of `<VAR_NAME>` with `<VALUE>`.

In C, the preprocessors process the source code ahead of compilation to produce the expanded source code. This is illustrated below.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-59.png)
_C Preprocessor_

It's a good practice to include the definition of all _constants_ after the header files in your program, as shown below:

```c
#include <stdio.h>

#define CONSTANT_1 VALUE_1
#define CONSTANT_2 VALUE_2
//

int main()
    {
        //statements here
    }
```

▶ In the next section, you'll see an example using `#define` to declare C constants.

### How to Declare Constants Using `#define` Example

Consider the following code snippet, where you have two constants `STUDENT_ID` and `COURSE_CODE`.

```c
#include <stdio.h>
#define STUDENT_ID 27
#define COURSE_CODE 502

int main()
{
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID,COURSE_CODE);

    return 0;
}


# Output
Student ID: 27 is taking the class 502

```

In this example:

* The preprocessor replaces `STUDENT_ID` and `COURSE_CODE` by 27, and 502, respectively. So the body of the `main()` function will now be:

```c
int main()
{
    printf("Student ID: %d is taking the class %d\n", 27, 502);

    return 0;
}
```

* As the `printf()` function can print out formatted strings, the two occurrences of the format specifiers `%d` (for decimal integers) are replaced by 27 and 502.

> Although `#define` lets you define constants, you should be careful _not to redefine_ them elsewhere in the program.

For example, the code below, you've redefined `STUDENT_ID`. And it will compile and execute without errors.

```c
#include <stdio.h>
#define STUDENT_ID 27
#define STUDENT_ID 207 //redefinition of a #define constant.
#define COURSE_CODE 502

int main()
{
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID,COURSE_CODE);

    return 0;
}

```

Depending on your compiler, you may get a warning that you're trying to _redefine_ an already-defined constant.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-76.png)

And the value in the most recent definition will be used. 

Notice how the redefined value of `207` has been used as the `STUDENT_ID`, overwriting the previously defined value `27`.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-77.png)

So you now know that the `#define` constants are in some sense not true constants as you can always redefine them.

Head on to the next section to learn about the `const` qualifier.

## How to Use the `const` Qualifier to Define Constants in C

In C, `<data_type> <var_name> = <value>` is the syntax to declare a variable `<var_name>` of type `<data_type>`, and to assign it the value `<value>`.

To make `<var_name>` a constant, you only need to add the `const` qualifier to this statement as follows:

```c
const <data_type> <var_name> = <value>;
```

> Adding the `const` keyword in the definition of the variable ensures that its value remains unchanged in the program. 

The `const` qualifier makes the variable _read-only._ And trying to modify it elsewhere in the program will throw errors during compilation.

▶ Head on to the next section to modify the previous example using `const`.

### How to Declare Constants Using `const` Qualifier Example

From the previous example, you have the constants `STUDENT_ID` and `COURSE_CODE`. Now you'll define them as constants using the `const` qualifier.

* Since they're both integers, you can define them to be of the `int` data type, taking the intended values: `27` and `502`. 
* Include the qualifier `const` in the respective definitions.

This is shown in the code snippet below:

```c
#include <stdio.h>

int main()
{
    const int STUDENT_ID = 27;
    const int COURSE_CODE = 502;
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID, COURSE_CODE);

    return 0;
}

# Output
Student ID: 27 is taking the class 502

```

You can see that the code works as expected.

> In C, you cannot redefine an existing variable. 

For example, if `int my_var = 2` is the first definition, your program won't compile successfully if you try redefining `my_var` as `int my_var = 3`.

> However, you can always reassign values of a variable.

This means that if `int my_var = 2` is the definition, you can assign a different value to `my_var` using a simple assignment statement like `my_var = 3`.

Let's now try modifying the `const` variable `STUDENT_ID`.

```c
#include <stdio.h>

int main()
{
    const int STUDENT_ID = 27;
    STUDENT_ID = 207; // modifying a true constant: NOT POSSIBLE
    const int COURSE_CODE = 502;
    printf("Student ID: %d is taking the class %d\n", STUDENT_ID, COURSE_CODE);

    return 0;
}


```

You'll see that the program doesn't compile successfully. 

And the error message reads: `error: assignment of read-only variable 'student_id'` meaning that you can only read the value of `STUDENT_ID` and not assign a value to it.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-82.png)

Thus the `const` qualifier renders a _true constan_t that's immune to changes, and cannot be altered during the execution of the program.

## Conclusion

In this tutorial, you've learned how to define constants:

* using the `#define` preprocessor directive with the syntax `#define <VAR_NAME> <VALUE>`, and
* using the `const` qualifier to render variables to be _read-only_.

Hope you found this tutorial helpful. Happy coding!😄

