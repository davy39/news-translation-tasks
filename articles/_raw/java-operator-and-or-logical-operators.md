---
title: Java Operator – &, && (AND) || (OR) Logical Operators
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-08T18:38:13.000Z'
originalURL: https://freecodecamp.org/news/java-operator-and-or-logical-operators
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/logic.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "We use operators in most programming languages to perform operations on\
  \ variables. \nThey are divided into various categories like arithmetic operators,\
  \ assignment operators, comparison operators, logical operators, and so on. \nIn\
  \ this article, we wil..."
---

We use operators in most programming languages to perform operations on variables. 

They are divided into various categories like arithmetic operators, assignment operators, comparison operators, logical operators, and so on. 

In this article, we will be talking about the bitwise **AND** operator, and the **AND** (`&&`) and **OR** (`||`) logical operators. 

## How to use the bitwise`AND` operator

The symbol `&` denotes the bitwise **AND** operator. It evaluates the binary value of given numbers. The binary result of these numbers will be returned to us in base 10. 

When the `&` operator starts its operation, it will evaluate the value of characters in both numbers starting from the left.

Let's look at an example to help you understand better:

```java
System.out.println(10 & 12);
// returns 8
```

Let's break it down.

The binary value of 10 is 1010

The binary value of 12 is 1100

Here is something you should have in mind before we start the operation:

* 1 and 0 => 0
* 0 and 1 => 0
* 1 and 1 => 1
* 0 and 0 => 0

So let's carry out the operation.

The first character for 10 is 1 and the first character for 12 is also 1 so:

1 and 1 = 1.

We move on to the second characters – 0 for 10 and 1 for 12:

1 and 0 = 0.

For the third characters – 1 for 10 and 0 for 12:

1 and 0 = 0.

For the fourth characters – 0 for 10 and 0 for 12:

0 and 0 = 0.

Now let's combine all the returned characters. We would have 1000.

The binary value 1000 in base 10 is 8 and that is why our operation returned 8.

## How to use the logical `AND` operator

Note that we use logical operators to evaluate conditions. They return either `true` or `false` based on the conditions given.

The symbol `&&` denotes the **AND** operator. It evaluates two statements/conditions and returns true only when both statements/conditions are true.

Here is what the syntax looks like:

```txt
statment1/condition1 && statemnt2/condition2
```

As you can see above, there are two statements/conditions separated by the operator. The operator evaluates the value of both statements/conditions and gives us a result – true or false.

Here is an example:

```java
System.out.println((10 > 2) && (8 > 4));
//true
```

The operation will return `true` because both conditions are true – 10 is greater than 2 **and** 8 is greater than 4. If either one of the conditions had an untrue logic then we would get `false`.

To better understand the `&&` operator, you should know that both conditions must be true to get a value of `true`. 

Here is another example that returns `false`:

```java
System.out.println((2 > 10) && (8 > 4));
// false
```

Here, 2 is not greater than 10 but 8 is greater than 4 – so we get a `false` returned to us. This is because one of the conditions is not true.

* If both conditions are true => `true`
* If one of the two conditions is false => `false`
* If both conditions are false => `false`

## How to use the logical `OR` operator

We use the symbol `||` to denote the **OR** operator. This operator will only return `false` when both conditions are false. This means that if both conditions are true, we would get `true` returned, and if one of both conditions is true, we would also get a value of `true` returned to us.

Here is the syntax:

```txt
statment1/condition1 || statemnt2/condition2
```

Let's go over a few examples.

```
System.out.println((6 < 1) || (4 > 2));  
// true
```

This returns `true` because one of conditions is true.

* If both conditions are true => `true`
* If one of the conditions is true => `true`
* If both conditions are false => `false`

## Conclusion

In this article, we learned how to use the bitwise `&` operator in Java and how the operation is carried out to give us a result. 

We also learned how to use the **`&&`** and **`||`** logical operators in Java. We learned what value each operation returns based on the conditions involved in the operation. 

Happy Coding!

