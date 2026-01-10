---
title: Learn JavaScript Operators – Logical, Comparison, Ternary, and More JS Operators
  With Examples
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-08-14T15:44:58.000Z'
originalURL: https://freecodecamp.org/news/javascript-operators
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/JS-EVERY-OPERATOR.png
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
seo_title: null
seo_desc: 'JavaScript has many operators that you can use to perform operations on
  values and variables (also called operands)

  Based on the types of operations these JS operators perform, we can divide them
  up into seven groups:


  Arithmetic Operators

  Assignment...'
---

JavaScript has many operators that you can use to perform operations on values and variables (also called operands)

Based on the types of operations these JS operators perform, we can divide them up into seven groups:

1. [Arithmetic Operators](#heading-arithmetic-operators)
2. [Assignment Operators](#heading-assignment-operators)
3. [Comparison Operators](#heading-comparison-operators)
4. [Logical Operators](#heading-logical-operators)
5. [Ternary Operators](#heading-ternary-operator)
6. [The `typeof` Operator](#heading-the-typeof-operator)
7. [Bitwise Operators](#heading-bitwise-operators)

In this handbook, you're going to learn how these operators work with examples. Let's start with arithmetic operators.

## Arithmetic Operators

The arithmetic operators are used to perform mathematical operations like addition and subtraction.

These operators are frequently used with number data types, so they are similar to a calculator. The following example shows how you can use the `+` operator to add two variables together:

```js
let x = 3;
let y = 8;

console.log(x + y); // 11
```

Here, the two variables `x` and `y` are added together using the plus `+` operator. We also used the `console.log()` method to print the result of the operation to the screen.

You can use operators directly on values without assigning them to any variable too:

```js
console.log(2 + 1); // 3
console.log(4 + 1); // 5
```

In JavaScript, we have 8 arithmetic operators in total. They are:

1. Addition `+`
2. Subtraction `-`
3. Multiplication `*`
4. Division `/`
5. Remainder `%`
6. Exponentiation `**`
7. Increment `++`
8. Decrement `--`

Let's see how these operators work one by one.

### 1. Addition operator

The addition operator `+` is used to add two or more numbers together. You've seen how this operator works previously, but here's another example:

```js
console.log(7 + 2); // 9
console.log(2.3 + 1.5); // 3.8
```

You can use the addition operator on both integer and floating numbers.

### 2. Subtraction operator

The subtraction operator is marked by the minus sign `−` and you can use it to subtract the right operand from the left operand.

For example, here's how to subtract 3 from 5:

```js
let x = 5;
let y = 3;

console.log(x - y); // 2
```

### 3. Multiplication operator

The multiplication operator is marked by the asterisk `*` symbol, and you use it to multiply the value on the left by the value on the right of the operator.

```js
console.log(5 * 2); // 10
console.log(3 * 3); // 9
```

### 4. Division operator

The division operator `/` is used to divide the left operand by the right operand. Here are some examples of using the operator:

```js
console.log(10 / 2); // 5
console.log(9 / 3); // 3
```

### 5. Remainder operator

The remainder operator `%` is also known as the modulo or modulus operator. This operator is used to calculate the remainder after a division has been performed.

A practical example should make this operator easier to understand, so let's see one:

```js
console.log(10 % 3);
```

The number 10 can't be divided by 3 perfectly. The result of the division is 3 with a remainder of 1. The remainder operator simply returns that remainder number.

If the left operand can be divided with no remainder, then the operator returns 0.

This operator is commonly used when you want to check if a number is even or odd. If a number is even, dividing it by 2 will result in a remainder of 0, and if it's odd, the remainder will be 1.

```js
console.log(1 % 2); // 1
console.log(2 % 2); // 0
console.log(3 % 2); // 1
console.log(4 % 2); // 0
```

### 6. Exponentiation operator

The exponentiation operator is marked by two asterisks `**`. It's one of the newer JavaScript operators and you can use it to calculate the power of a number (based on its exponent).

For example, here's how to calculate 10 to the power of 3:

```js
console.log(10 ** 3); // 1000
```

Here, the number 10 is multiplied by itself 3 times (10 _ 10 _ 10)

The exponentiation operator gives you an easy way to find the power of a specific number.

### 7. Increment operator

The increment `++` operator is used to increase the value of a number by one. For example:

```js
let x = 5;

x++;

console.log(x); // 6
```

This operator gives you a faster way to increase a variable value by one. Without the operator, here's how you increment a variable:

```js
let x = 5;

x = x + 1;

console.log(x); // 6
```

Using the increment operator allows you to shorten the second line. You can place this operator before or next to the variable you want to increment:

```js
let x = 5;

// Place the operator next to the variable (postfix)
x++;

// Place the operator before the variable (prefix)
++x;
```

Both placements shown above are valid. The difference between prefix (before) and postfix (after) placements is that the prefix position will execute the operator after that line of code has been executed.

Consider the following example:

```js
let x = 5;
let y = 5;

console.log(x++); // 5
console.log(x); // 6

console.log(++y); // 6
console.log(y); // 6
```

Here, you can see that placing the increment operator next to the variable will print the variable as if it has not been incremented.

When you place the operator before the variable, then the number will be incremented before calling the `console.log()` method.

### 8. Decrement operator

The decrement `--` operator is used to decrease the value of a number by one. It's the opposite of the increment operator:

```js
let x = 5;

x--;

console.log(x); // 4
```

Please note that you can only use increment and decrement operators on a variable. An error occurs when you try to use these operators directly on a number value:

```js
console.log(5--);
```

**Output:**

```txt
Uncaught SyntaxError: Invalid left-hand side expression in postfix operation
```

You can't use increment or decrement operator on a number directly.

### Arithmetic operators summary

Now you've learned the 8 types of arithmetic operators. Excellent! Keep in mind that you can mix these operators to perform complex mathematical equations.

For example, you can perform an addition and multiplication on a set of numbers:

```js
console.log(5 + 2 * 3); // 11
```

The order of operations in JavaScript is the same as in mathematics. Multiplication, division, and exponentiation take a higher priority than addition or subtraction (remember that acronym PEMDAS? Parentheses, exponents, multiplication and division, addition and subtraction – there's your order of operations).

You can use parentheses `()` to change the order of the operations. Wrap the operation you want to execute first as follows:

```js
console.log((5 + 2) * 3); // 21
```

When using increment or decrement operators together with other operators, you need to place the operators in a prefix position as follows:

```js
let x = 5;
console.log(2 + ++x); // 2 + 6 = 8
```

This is because a postfix increment or decrement operator will not be executed together with other operations in the same line, as I have explained previously.

Let's try some exercises. Can you guess the result of these operations?

```js
console.log(5 * 3 - 2);
console.log((3 * 6) % 2);
console.log(5 + 7 - 1);
console.log((4 + 9) * 4);

let x = 5;
console.log(++x);
console.log(x++ / 3);
```

And that's all for arithmetic operators. You've done a wonderful job learning about these operators.

Let's take a short five-minute break before proceeding to the next type of operators.

## Assignment Operators

The second group of operators we're going to explore is the assignment operators.

Assignment operators are used to assign a specific value to a variable. The basic assignment operator is marked by the equal `=` symbol, and you've already seen this operator in action before:

```js
let x = 5;
```

After the basic assignment operator, there are 5 more assignment operators that combine mathematical operations with the assignment. These operators are useful to make your code clean and short.

For example, suppose you want to increment the `x` variable by 2. Here's how you do it with the basic assignment operator:

```js
let x = 5;

x = x + 2;
```

There's nothing wrong with the code above, but you can use the addition assignment `+=` to rewrite the second line as follows:

```js
let x = 5;

x += 2;
```

There are 7 kinds of assignment operators that you can use in JavaScript:

| Name                      | Operation example | Meaning      |
| ------------------------- | ----------------- | ------------ |
| Assignment                | `x = y`           | `x = y`      |
| Addition assignment       | `x += y`          | `x = x + y`  |
| Subtraction assignment    | `x -= y`          | `x = x - y`  |
| Multiplication assignment | `x *= y`          | `x = x * y`  |
| Division assignment       | `x /= y `         | `x = x / y`  |
| Remainder assignment      | `x %= y`          | `x = x % y`  |
| Exponentiation assignment | `x **= y`         | `x = x ** y` |

The arithmetic operators you've learned in the previous section can be combined with the assignment operator except the increment and decrement operators.

Let's have a quick exercise. Can you guess the results of these assignments?

```js
let x = 3;

x += 2 * 3;
console.log(x);

x -= 3;
console.log(x);

x %= 2;
console.log(x);
```

Now you've learned about assignment operators. Let's continue and learn about comparison operators.

## Comparison Operators

As the name implies, comparison operators are used to compare one value or variable with something else. The operators in this category always return a boolean value: either `true` or `false`.

For example, suppose you want to compare if a variable's value is greater than 1. Here's how you do it:

```js
let x = 5;

console.log(x > 1); // true
console.log(x > 7); // false
```

The greater than `>` operator checks if the value on the left operand is greater than the value on the right operand.

There are 8 kinds of comparison operators available in JavaScript:

| Name                  | Operation example | Meaning                                                                          |
| --------------------- | ----------------- | -------------------------------------------------------------------------------- |
| Equal                 | `x == y`          | Returns `true` if the operands are equal                                         |
| Not equal             | `x != y`          | Returns `true` if the operands are not equal                                     |
| Strict equal          | `x === y`         | Returns `true` if the operands are equal and have the same type                  |
| Strict not equal      | `x !== y`         | Returns `true` if the operands are not equal, or have different types            |
| Greater than          | `x > y`           | Returns `true` if the left operand is greater than the right operand             |
| Greater than or equal | `x >= y`          | Returns `true` if the left operand is greater than or equal to the right operand |
| Less than             | `x < y `          | Returns `true` if the left operand is less than the right operand                |
| Less than or equal    | `x <= y`          | Returns `true` if the left operand is less than or equal to the right operand    |

Here are some examples of using comparison operators:

```js
console.log(9 == 9); // true

console.log(9 != 20); // true

console.log(2 > 10); // false

console.log(2 < 10); // true

console.log(5 >= 10); // false

console.log(10 <= 10); // true
```

The comparison operators are further divided in two types: relational and equality operators.

The relational operators compare the value of one operand relative to the second operand (greater than, less than)

The equality operators check if the value on the left is equal to the value on the right. They can also be used to compare strings like this:

```js
console.log("ABC" == "ABC"); // true

console.log("ABC" == "abc"); // false

console.log("Z" != "A"); // true
```

String comparisons are case-sensitive, as shown in the example above.

JavaScript also has two versions of the equality operators: loose and strict.

In strict mode, JavaScript will compare the values without performing a type coercion. To enable strict mode, you need to add one more equal `=` symbol to the operation as follows:

```js
console.log("9" == 9); // true
// strict equal
console.log("9" === 9); // false

console.log("1" != 1); // false
// strict not equal
console.log("1" !== 1); // true
```

Since type coercion might result in unwanted behavior, you should use the strict equality operators anytime you do an equality comparison.

## Logical Operators

Logical operators are used to check whether one or more expressions result in either `true` or `false`.

There are three logical operators available in JavaScript:

| Name        | Operation example | Meaning                                                         |
| ----------- | ----------------- | --------------------------------------------------------------- | --- | --------------------------------------------------------------------- |
| Logical AND | `x && y`          | Returns `true` if all operands are `true`, else returns `false` |
| Logical OR  | `x || y`  | Returns `true` if one of the operands is `true`, else returns `false` |
| Logical NOT | `!x`              | Reverse the result: returns `true` if `false` and vice versa    |

These operators can only return Boolean values. For example, you can determine whether '7 is greater than 2' and '5 is greater than 4':

```js
console.log(7 > 2 && 5 > 4); // true
```

These logical operators follow the laws of mathematical logic:

1. `&&` AND operator – if any expression returns `false`, the result is `false`
2. `||` OR operator – if any expression returns `true`, the result is `true`
3. `!` NOT operator – negates the expression, returning the opposite.

Let's do a little exercise. Try to run these statements on your computer. Can you guess the results?

```js
console.log(true && false);

console.log(false || false);

console.log(!true);
```

These logical operators will come in handy when you need to assert that a specific requirement is fulfilled in your code.

Let's say a `happyLife` requires a job with `highIncome` and `supportiveTeam`:

```js
let highIncome = true;
let supportiveTeam = true;
let happyLife = highIncome && supportiveTeam;

console.log(happyLife); // true
```

Based on the requirements, you can use the logical AND operator to check whether you have both requirements. When one of the requirements is `false`, then `happyLife` equals `false` as well.

## Ternary Operator

The ternary operator (also called the conditional operator) is the only JavaScipt operator that requires 3 operands to run.

Let's imagine you need to implement some specific logic in your code. Suppose you're opening a shop to sell fruit. You give a $3 discount when the total purchase is $20 or more. Otherwise, you give a $1 discount.

You can implement the logic using an `if..else` statement as follows:

```js
let totalPurchase = 15;

let discount;

if (totalPurchase >= 20) {
  discount = 3;
} else {
  discount = 1;
}
```

The code above works fine, but you can use the ternary operator to make the code shorter and more concise as follows:

```js
let totalPurchase = 15;

let discount = totalPurchase >= 20 ? 3 : 1;
```

The syntax for the ternary operator is `condition ? expression1 : expression2`.

You need to write the `condition` to evaluate followed by a question `?` mark. 

Next to the question mark, you write the expression to execute when the condition evaluates to `true`, followed by a colon `:` symbol. You can call this `expression1`.

Next to the colon symbol, you write the expression to execute when the condition evaluates to `false`. This is `expression2`.

As the example above shows, the ternary operator can be used as an alternative to the `if..else` statement.

## The `typeof` Operator

The `typeof` operator is the only operator that's not represented by symbols. This operator is used to check the data type of the value you placed on the right side of the operator.

Here are some examples of using the operator:

```js
let x = 5;
console.log(typeof x) //  'number'

console.log(typeof "Nathan") // 'string'

console.log(typeof true) // 'boolean'

console.log(typeof null) // 'object'

console.log(typeof [1, 2, 3]) // 'object'

console.log(typeof {}) // 'object'

console.log(typeof undefined) // 'undefined'
```

The `typeof` operator returns the type of the data as a string. The 'number' type represents both integer and float types, the string and boolean represent their respective types.

Arrays, objects, and the `null` value are of object type, while `undefined` has its own type.

## Bitwise Operators

Bitwise operators are operators that treat their operands as a set of binary digits, but return the result of the operation as a decimal value.

These operators are rarely used in web development, so you can skip this part if you only want to learn practical stuff. But if you're interested to know how they work, then let me show you an example.

A computer uses a binary number system to store decimal numbers in memory. The binary system only uses two numbers, 0 and 1, to represent the whole range of decimal numbers we humans know.

For example, the decimal number 1 is represented as binary number 00000001, and the decimal number 2 is represented as 00000010.

I won't go into detail on how to convert a decimal number into a binary number as that's too much to include in this guide. The main point is that the bitwise operators operate on these binary numbers.

If you want to find the binary number from a specific decimal number, you can Google for the "decimal to binary calculator".

There are 7 types of bitwise operators in JavaScript:

1. AND `&`
2. OR `|`
3. XOR `^`
4. NOT `~`
5. Left Shift `<<`
6. Right Shift `>>`
7. Zero-fill Right Shift `>>>`

Let's see how they work.

### 1. Bitwise AND operator

The bitwise operator AND `&` returns a 1 when the number 1 overlaps in both operands. The decimal numbers 1 and 2 have no overlapping 1, so using this operator on the numbers return 0:

```js
// 1 = 00000001
// 2 = 00000010
// ------------
//     00000000 = 0

console.log(1 & 2); // 0
```

### 2. Bitwise OR operator

On the other hand, the bitwise operator OR `|` returns all 1s in both decimal numbers.

```js
// 1 = 00000001
// 2 = 00000010
// ------------
//     00000011 = 3

console.log(1 | 2); // 3
```

The binary number 00000011 represents the decimal number 3, so the OR operator above returns 3.

### Bitwise XOR operator

The Bitwise XOR `^` looks for the differences between two binary numbers. When the corresponding bits are the same, it returns 0:

5 = 00000101

```js
// 5 = 00000101
// 7 = 00000111
// ------------
//     00000010 = 2

console.log(5 ^ 7); // 2
```

### Bitwise NOT operator

Bitwise NOT `~` operator inverts the bits of a decimal number so 0 becomes 1 and 1 becomes 0:

```js
// 5 = 00000101
// ------------
//     11111010 = -6

console.log(~5); // -6
```

### Bitwise Left Shift operator

Bitwise Left Shift `<<` shifts the position of the bit by adding zeroes from the right.

The excess bits are then discarded, changing the decimal number represented by the bits. See the following example:

```js
console.log(5 << 2);

// 5 = 00000101
// ------------ << Shift to the left by 2
//     00010100 = 20
```

The right operand is the number of zeroes you will add to the left operand.

### Bitwise Right Shift operator

Bitwise Right Shift `>>` shifts the position of the bits by adding zeroes from the left. It's the opposite of the Left Shift operator:

```js
console.log(5 >> 2); // 1

// 5 = 00000101
// ------------ >> Shift to the right by 2
//     00000001 = 1
```

### Bitwise Zero-fill Right Shift operator

Also known as Unsigned Right Shift operator, the Zero-fill Right Shift `>>>` operator is used to shift the position of the bits to the right, while also changing the sign bit to `0`.

This operator transforms any negative number into a positive number, so you can see how it works when passing a negative number as the left operand:

```js
console.log(-70 >> 1); // -35
console.log(-70 >>> 1); // 2147483613

console.log(5 >> 1); // 2
console.log(5 >>> 1); // 2
```

In the above example, you can see that the `>>` and `>>>` operators return different results. The Zero-fill Right Shift operator has no effect when you use it on a positive number.

Now you've learned how the bitwise operators work. If you think they are confusing, then you're not alone! Fortunately, these operators are scarcely used when developing web applications.

You don't need to learn them in depth. It's enough to know what they are.

## Conclusion

In this tutorial, you've learned the 7 types of JavaScript operators: Arithmetic, assignment, comparison, logical, ternary, typeof, and bitwise operators.

These operators can be used to manipulate values and variables to achieve a desired outcome.

Congratulations on finishing this guide!

If you enjoyed this article and want to take your JavaScript skills to the next level, I recommend you check out my new book _Beginning Modern JavaScript_ [here](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

The book is designed to be easy to understand and accessible to anyone looking to learn JavaScript. It provides a step-by-step gentle guide that will help you understand how to use JavaScript to create a dynamic application.

Here's my promise: _You will actually feel like you understand what you're doing with JavaScript._

Until next time!

