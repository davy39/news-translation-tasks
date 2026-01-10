---
title: 'JavaScript Loops: Label Statement, Continue Statement, and Break Statement
  Explained'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-04T22:27:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-loops-label-statement-continue-statement-and-break-statement-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cca740569d1a4ca3436.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "Label Statement\nThe Label Statement is used with the break and continue\
  \ statements and serves to identify the statement to which the break and continue\
  \ statements apply. \nWe'll talk more about the break and continue statements below.\n\
  Syntax\nlabelname..."
---

## **Label Statement**

The **Label Statement** is used with the `break` and `continue` statements and serves to identify the statement to which the `break` and `continue` statements apply. 

We'll talk more about the `break` and `continue` statements below.

### **Syntax**

```javascript
labelname:
  statements
```

### **Usage**

Without the use of a `labeled` statement the `break` statement can only break out of a loop or a `switch` statement. Using a `labeled` statement allows `break` to jump out of any code block.

#### **Example**

```javascript
foo: {
  console.log("This prints:");
  break foo;
  console.log("This will never print.");
}
console.log("Because execution jumps to here!")
/* output
This prints:
Because execution jumps to here! */
```

When used with a `continue` statement the `labeled` statement allows you to skip a loop iteration, the advantage comes from being able to jump out from an inner loop to an outer one when you have nested loop statements. Without the use of a `labeled` statement you could only jump out of the existing loop iteration to the `next iteration of the same loop.`

#### **Example**

```javascript
// without labeled statement, when j==i inner loop jumps to next iteration
function test() {
  for (var i = 0; i < 3; i++) {
    console.log("i=" + i);
    for (var j = 0; j < 3; j++) {
      if (j === i) {
        continue;
      }
      console.log("j=" + j);
    }
  }
}

/* output
i=0 (note j=0 is missing)
j=1
j=2
i=1
j=0 (note j=1 is missing)
j=2
i=2
j=0
j=1 (note j=2 is missing)
*/

// using a labeled statement we can jump to the outer (i) loop instead
function test() {
  outer: for (var i = 0; i < 3; i++) {
    console.log("i=" + i);
    for (var j = 0; j < 3; j++) {
      if (j === i) {
        continue outer;
      }
      console.log("j=" + j);
    }
  }
}

/*
i=0 (j only logged when less than i)
i=1
j=0
i=2
j=0
j=1
*/
```

## **Break statement**

The **break** statement terminates the current loop, `switch` or `label` statement and transfers program control to the statement following the terminated statement.

```text
break;
```

If the **break** statement is used in a labeled statement, the syntax is as follows:

```text
break labelName;
```

### Examples

The following function has a **break** statement that terminates the `while` loop when **i** is 3, and then returns the value **3 * x**.

```text
function testBreak(x) {
  var i = 0;

  while (i < 6) {
    if (i == 3) {
      break;
    }
    i += 1;
  }

  return i * x;
}
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/C7VM/0)

In the following example, the counter is set up to count from 1 to 99; however, the **break** statement terminates the loop after 14 counts.

```text
for (var i = 1; i < 100; i++) {
  if (i == 15) {
    break;
  }
}
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/C7VO/0)

## Continue statement

The **continue** statement terminates execution of the statements in the current iteration of the current or labeled loop, and continues execution of the loop with the next iteration.

```text
continue;
```

If the **continue** statement is used in a labeled statement, the syntax is as follows:

```text
continue labelName;
```

In contrast to the **break** statement, **continue** does not terminate the execution of the loop entirely; instead:

* In a `while` loop, it jumps back to the condition.
* In a `for` loop, it jumps to the update expression.

### Examples

The following example shows a `while` loop that has a **continue** statement that executes when the value of **i** is 3. Thus, **n** takes on the values 1, 3, 7, and 12.

```text
var i = 0;
var n = 0;

while (i < 5) {
  i++;

  if (i === 3) {
    continue;
  }

  n += i;
  console.log (n);
}
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/C7hx/0)

In the following example, a loop iterates from 1 through 9. The statements between **continue** and the end of the `for` body are skipped because of the use of the **continue** statement together with the expression `(i < 5)`.

```text
for (var i = 1; i < 10; i++) {
    if (i < 5) {
        continue;
    }
    console.log (i);
}
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Run Code](https://repl.it/C7hs/0)

