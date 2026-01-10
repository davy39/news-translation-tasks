---
title: Ternary Operator in C Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T17:00:00.000Z'
originalURL: https://freecodecamp.org/news/c-ternary-operator
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9db2740569d1a4ca3922.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'Programmers use the ternary operator for decision making in place of longer
  if and else conditional statements.

  The ternary operator take three arguments:


  The first is a comparison argument

  The second is the result upon a true comparison

  The third i...'
---

Programmers use the **ternary operator** for decision making in place of longer **if** and **else** conditional statements.

The ternary operator take three arguments:

1. The first is a comparison argument
2. The second is the result upon a true comparison
3. The third is the result upon a false comparison

It helps to think of the ternary operator as a shorthand way or writing an if-else statement. Here’s a simple decision-making example using **if** and **else**:

```c
int a = 10, b = 20, c;

if (a < b) {
    c = a;
}
else {
    c = b;
}

printf("%d", c);
```

This example takes more than 10 lines, but that isn’t necessary. You can write the above program in just 3 lines of code using a ternary operator.

### **Syntax**

`condition ? value_if_true : value_if_false`

The statement evaluates to `value_if_true` if `condition` is met, and `value_if_false` otherwise.

Here’s the above example rewritten to use the ternary operator:

```c
int a = 10, b = 20, c;

c = (a < b) ? a : b;

printf("%d", c);
```

Output of the example above should be:

```c
10
```

`c` is set equal to `a`, because the condition `a < b` was true.

Remember that the arguments `value_if_true` and `value_if_false` must be of the same type, and they must be simple expressions rather than full statements.

Ternary operators can be nested just like if-else statements. Consider the following code:

```c
int a = 1, b = 2, ans;
if (a == 1) {
    if (b == 2) {
        ans = 3;
    } else {
        ans = 5;
    }
} else {
    ans = 0;
}
printf ("%d\n", ans);
```

Here's the code above rewritten using a nested ternary operator:

```c
int a = 1, b = 2, ans;
ans = (a == 1 ? (b == 2 ? 3 : 5) : 0);
printf ("%d\n", ans);
```

The output of both sets of code above should be:

```c
3
```


