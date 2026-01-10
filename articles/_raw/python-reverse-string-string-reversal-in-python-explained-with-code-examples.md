---
title: Python Reverse String – String Reversal in Python Explained with Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-11-10T16:40:09.000Z'
originalURL: https://freecodecamp.org/news/python-reverse-string-string-reversal-in-python-explained-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/designecologist-sYI_WSHEsXU-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "When you're working with Python strings, there are times when you'll have\
  \ to reverse them, and work with their reversed copies instead. \nBut since Python\
  \ strings are immutable, you cannot modify or reverse them in place.\nIn Python,\
  \ there are a few di..."
---

When you're working with Python strings, there are times when you'll have to reverse them, and work with their reversed copies instead. 

But since Python strings are _immutable_, you cannot modify or reverse them in place.

In Python, there are a few different ways you can do this. And this tutorial will teach you how you can use string slicing, built-in methods, and recursion to reverse strings.

### 🎯 What You'll Learn

* [Using **Recursion** to Reverse Strings](#heading-how-to-reverse-python-strings-using-recursion): You'll learn about how recursion works, and the intuition behind reversing strings using recursion.
* [Using  **String Slicing** to Reverse Strings](#heading-how-to-reverse-python-strings-using-string-slicing): You'll learn a much easier way to reverse Python strings.
* [Using **Built-In Methods**](#heading-how-to-reverse-python-strings-using-the-reversed-and-the-join-methods): You'll learn yet another easy and intuitive way to reverse strings in Python.

So let's get started.

## How to Reverse Python Strings Using Recursion

Before learning how to use recursion to reverse strings, let's start by understanding how recursion works.

> Recursion is a powerful programming paradigm. To solve the problem of interest, a recursive function **calls itself** repeatedly, until a **base case** is reached.

Well, this is what you’ll have likely read about recursion before.

Let’s rephrase that definition in plain language now.

### Recursion in Plain English

Suppose you’ve created a function to solve a problem.

* The function is designed such that every time it’s called, it _calls itself_ again.
* These are called _recursive_ function calls.
* Each recursive function call does the same small amount of work.
* And this goes on until there’s no work left to do. And the function doesn’t have to call itself any longer – this is called the **base case**.

### How to Use Recursion to Reverse Strings

Let's now discuss the motivation behind reversing strings intuitively. And to do this, consider the string `"code"`.

**Problem:** Reverse the string `"code"`.

![Image](https://lh5.googleusercontent.com/9EzNJgPbbGbmddk3f_t55PSDTr7cP5fgdXJjCX9B_hPkP1GHzOq58PR3wkZPRSdU5_O7SC4g8tZOQVjlNx6Ya9jc00aeqgXP-fvGHECpU7lF64AWYraIz25u-6JbmvTXQCkI1HY_)

Let's forget recursion for a while, and start with what you know.

> The first letter in the original string will be the last letter in the reversed string, yes?

* So pull out the first letter – `"c"` here – and push it to the very end.
* You're now left with the string `"ode"`. And the problem has reduced to reversing this substring `"ode"` [as `"c"` is already in the right place]

![Image](https://lh4.googleusercontent.com/V4oyw-hYeZWzSzu0JULaKLzHynBWgQCAB-GJrEU6sb8j5u9OKY7DRIvDbYEw-2MrWY-rNcFmVYbkSQMfQyx6AjYG7j-flGQktEEwoZpO1H0Fl1Hkwq0MN2UpiPl3QYclrDWN91oU)

* You can do the very same task of pulling out the first letter yet again, now `"o"`. And push it to the last slot available on the right.
* Now that `"c"` and `"o"` have been taken care of, you're left with the problem of reversing the substring `"de"`.

![Image](https://lh3.googleusercontent.com/IfSSH94VWA90ZxOSGqKUYBRUqFwT_nLY3W7vFJ4_jYdTIbUIQ17FabArbDqVv9cZ2jVdKoJTh0IFhKnoACscgipWLpL3iwfoeRV8FuFIABVPriynIqJabAccqr-UJHpScXBmuJQ9)

* Do it a couple more times – pull out `"d"` first, and then `"e"`.

![Image](https://lh5.googleusercontent.com/LDgbioxKdX1Mey1FpzF20KnWnCAVNIQZFWTczaB-IDiKhHOWudo5Wnx8qg5XyiBnA0r5UVwERxVYodPtcvSM39Irn7kJvMZ5X8UzdpVDwTfhKsr0uxNPadgMTCpmEy4qcgaQsiC2)

* You're now left with reversing `""` – an empty string. 

![Image](https://lh5.googleusercontent.com/sGHYP70tsai5P6CQdiJk5u8qOLEXNzq0Ab5q8r3mmO5HFJslYCSii17tw3khyo2SQuDBhdlpq05FZ7kvO2AOj65QGJdV_YK9E2aqN6VHx7E1YHETR-phtSJeTUchquxLpd-bCfjO)

* This is when you've put `"e"`, `"d"`, `"o"`, and `"c"` in the correct positions, and you don't have to do it any longer. In the context of recursion, you've reached the _base case_.

**What did you do here?** 

1. In each step, you did the same task of pulling out the first letter in each subsequent substring. 
2. And you reduced the problem to reversing a string that's one letter shorter than it was before.

**When did you stop?** 

When the string was _empty –_ you didn't have any more letters to pull out.

The illustration below sums up what we've done:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-30.png)
_Intuition behind String Reversal (Image by the author)_

Now that you've gotten the hang of how string reversal really works using recursion, let's write some code.

### Understanding the Recursion Call Stack

Here's the Python function `reverseString()` that does exactly what you learned in the previous section.

The function `reverseString()` takes in `any_string` and returns the reversed copy of `any_string`.

```python
def reverseString(any_string):
  if any_string == "":
    return any_string
  else:
    return reverseString(any_string[1:]) + any_string[:1]
```

You'll have to understand how the recursive calls get pushed onto the stack when you call the function `reverseString()`.

```python
reverseString("code")

# Output
'edoc'
```

* Say, you call the function `reverseString()` with `"code"` as the argument. This in turn makes a call to `reverseString()` with `"ode"` as the argument.
* And this call makes a call to `reverseString()` yet again with `"de"` as the argument.
* This continues until a call is finally made to `reverseString()` with an empty string `""` as the argument.

For every function call, an activation record is created in the stack section of your computer's memory.  
  
And every subsequent function call's activation record is pushed onto the top of the stack.

This is explained in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-28.png)
_Call Stack (Image by the author)_

* You know that when the call is made with `""`, the function returns `""` concatenated with `"e"` which is just `"e"`. And its activation record gets popped off the stack.
* The next call returns `"ed"`, and the next returns `"edo"`. And the activation record that's popped off the stack finally returns `"edoc"` which is the reversed string. 

Note that the activation record corresponding to each of the recursive calls gets popped off the stack once the values are returned – as shown in the call that returned `"e"`.

For the sake of readability, I've omitted the ❌ in the illustration below. And the return values from the previous call have been indicated in _green_ inside the call stack.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-29.png)
_Return values from the recursive calls (Image by the author)_

You can now call `reverseString()` with any valid Python string. Here are a few more examples.

```python
reverseString("Python")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-17.png)

```python
reverseString("Python Reverse String")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-16.png)

Well, that required quite a bit of effort. 😓 But I hope you're now able to understand recursive calls better. 😊

In the next two sections, you'll see easier ways to reverse strings. Let's go. ✅

## How to Reverse Python Strings Using String Slicing 

You might as well reverse Python strings using _string slicing_. And you can slice through Python strings just the way you'd slice through Python lists.

### Python String Slicing Explained

`<string>[start: stop: step]` returns a slice of the string – starting at the index `start`, extending all the way up to `stop - 1`, in steps of `step`.

Here are a few points about strings worth recollecting:

* `<string>` is any valid Python string.
* The `start` index is _optional_. If you don't specify it, by _default,_ the slice starts at the beginning of `<string>` (at index `0`).
* The `stop` index is also _optional_. If you don't specify it, by _default,_ the slice extends up to the end of `<string>`.
* The _optional_ `step` argument gives context on how you'd like to slice through `<string>`.
*  Let's set `step = 2`. Now, the the slice would start from `start` and go up to `stop - 1` , including every second character in the string.

Putting it all together, `<string>[:::]` returns a copy of the entire string.

Can you see why this is correct?🤔

Without the `start` index, the slice begins at index `0`.

Without the `end` index, the slice extends up to the last character in the string.

Without the `step` argument, the slice includes all characters in the string.

* You can also set _negative_ values for `step`. And negative values will return string slices starting from the _end_ of the string.
* Set `step = -1` : This returns a slice of the string starting _from_ the **last** character, extending up _to_ the **first** character. And it also includes every character.

Wait, isn't this exactly the reversed string? 🙂 Yes, it is.

So `<string>[::-1]` returns a reversed copy of the string. ✅

```python
any_string = "Python"

rev_string = any_string[::-1]

print(rev_string)

# Output
nohtyP
```

Head over to the next section to learn yet another way to reverse strings.

## How to Reverse Python Strings Using the `reversed()` and the `join()` Methods

Let's start by looking at what Python's `reversed()` method does.

> Python's built-in `reversed()` function returns a reverse iterator over the values of a given sequence.

```python
any_string = "Python"
```

Given a string like `any_string`, you can use the `reversed()` method to get the characters in the reversed order.

This is shown below:

```python
for char in reversed(any_string):
  print(char)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-13.png)

Now that you have all your characters in the reversed order, you need to put them together into a string.

And Python's `join()` method lets you do just that.

`<sep>.join(<these>)` joins `<these>` into a string with `<sep>` as the separator.

* Here, `<these>` are the characters in the reversed order. 
* But what should `<sep>` be? Well, you don't need any separator – you only want all the characters to go into the string at the right indices.
* So what should you do then? Just insert a `""` in the `<sep>` field, as shown:

```python
"".join(reversed(any_string))

```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-19.png)

Just be careful _not_ to insert a space between the opening and closing `"`.

If you do the following:

```python
" ".join(reversed(any_string))

```

You'll get a string where the characters are separated by a whitespace, and this isn't what you want.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-18.png)

In this section, you've learned yet another Pythonic way to reverse Python strings.

## Conclusion

Congratulations on making it this far! 🎉

To summarize, you've learned:

* how to recursively reverse a string – go on until you have an _empty string_ or have only _one character_ left (this would work fine too, as one character reversed is itself),
* how to use `<string>[::-1]` to get a reversed copy of  `<string>`, and
* how to use `"".join(reversed(<string>))` to get a reversed copy of `<string>`.

Hope you found this tutorial helpful and interesting. Happy coding! 😄

