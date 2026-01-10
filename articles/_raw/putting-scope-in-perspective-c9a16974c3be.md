---
title: Putting Scope in Perspective
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-04T08:31:56.000Z'
originalURL: https://freecodecamp.org/news/putting-scope-in-perspective-c9a16974c3be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bagtQodHCv1PGtuEX5fMNA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: women in tech
  slug: women-in-tech
seo_title: null
seo_desc: 'By Tiffany White

  In JavaScript, lexical scope deals with where your variables are defined, and how
  they will be accessible — or not accessible — to the rest of your code.

  There are two terms to think about when talking about scope: local and global. ...'
---

By Tiffany White

In JavaScript, _lexical scope_ deals with where your variables are defined, and how they will be accessible — or not accessible — to the rest of your code.

There are two terms to think about when talking about scope: local and global. These two terms are important to understand, because one can be more dangerous than the other when declaring variables and executing your code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_9SDjff_XSe6Kl_LSJrsKg.jpeg)

#### Global Scope

A variable is globally scoped if you declare it outside of all of your functions. For example:

```
//global variable, i.e. global scopevar a = "foo";
```

```
function myFunction() {  var b = "bar";  console.log(a+b);}
```

```
myFunction();
```

When a variable is in the global scope, it can be accessed by all the code in the same JavaScript file. In this example, I’m accessing the variable _a_ in my console.log statement, inside the _myFunction_ function.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QmksMiei1KJbztSbeb6cCA.jpeg)

#### Local Scope

Local variables only exist inside functions. They are scoped to that individual function.

You can think of local variables as as any variables that fall between an opening and closing curly brace.

These local variables can’t be accessed by code outside of the function to which they belong.

Take a look at this code:

```
//global variable, i.e. global scopevar a = "foo";
```

```
function myFunction() {  //local variable, or local scope  var b = "bar";  console.log(a+b);}
```

```
function yourFunction() {  var c = "JavaScript is fun!";  return c;  console.log(c);}
```

```
myFunction();yourFunction();
```

Notice how the variables are each declared inside separate functions. They are both local variables, in local scope, and can’t be accessed by one other.

For instance, I can’t return _b_ in _yourFunction,_ because _b_ belongs to _myFunction._ _b_ can’t be accessed by _yourFunction,_ and vice versa.

If I were to try to return the value of _b_ when calling _yourFunction_, I’d get “_error: b is not defined._” Why? Because _b_ doesn’t belong to _yourFunction. b_ is outside of _yourFunction_’s scope.

When adding nested conditionals, scope gets even more hairy. But I’ll leave that for another time.

But for now, remember the difference between global scope and local scope. And the next time you get a “_is not defined_” error, check the variable’s scope.

_This post also appears at [https://twhite96.github.io](https://twhite96.github.io)_

