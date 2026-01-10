---
title: Python String.Replace() – Function in Python for Substring Substitution
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-01-24T16:59:25.000Z'
originalURL: https://freecodecamp.org/news/python-string-replace-function-in-python-for-substring-substitution
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/sarah-dorweiler-QeVmJxZOv3k-unsplash-1.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In this article you''ll see how to use Python''s .replace() method to perform
  substring substiution.

  You''ll also see how to perform case-insensitive substring substitution.

  Let''s get started!

  What does the .replace() Python method do?

  When using the .r...'
---

In this article you'll see how to use Python's `.replace()` method to perform substring substiution.

You'll also see how to perform case-insensitive substring substitution.

Let's get started!

## What does the `.replace()` Python method do?

When using the `.replace()` Python method, you are able to replace every instance of one specific character with a new one. You can even replace a whole string of text with a new line of text that you specify.

The `.replace()` method returns a copy of a string. This means that the old substring remains the same, but a new copy gets created – with all of the old text having been replaced by the new text.

### How does the `.replace()` Python method work? A Syntax Breakdown

The syntax for the `.replace()` method looks like this:

```python
string.replace(old_text, new_text, count)
```

Let's break it down:

- `old_text` is the first required parameter that `.replace()` accepts. It's the old character or text that you want to replace. Enclose this in quotation marks.
- `new_text` is the second required parameter that `.replace()` accepts. It's the new character or text which you want to replace the old character/text with. This parameter also needs to be enclosed in quotation marks.
- `count` is the *optional* third parameter that `.replace()` accepts. By default, `.replace()` will replace **all** instances of the substring. However, you can use `count` to specify the number of occurrences you want to be replaced.

## Python `.replace()` Method Code Examples

### How to Replace All Instances of a Single Character

To change **all** instances of a single character, you would do the following:

```python
phrase = "I like to learn coding on the go"

# replace all instances of 'o' with 'a'
substituted_phrase = phrase.replace("o", "a" )

print(phrase)
print(substituted_phrase)

#output

#I like to learn coding on the go
#I like ta learn cading an the ga
```

In the example above, each word that contained the character `o` is replaced with the character `a`.

In that example there were four instances of the character `o`. Specifically, it was found in the words `to`, `coding`, `on`, and `go`.

What if you only wanted to change two words, like `to` and `coding`, to contain `a` instead of `o`? 

### How to Replace Only a Certain Number of Instances of a Single Character

To change only two instances of a single character, you would use the `count` parameter and set it to two:

```python
phrase = "I like to learn coding on the go"

# replace only the first two instances of 'o' with 'a'
substituted_phrase = phrase.replace("o", "a", 2 )

print(phrase)
print(substituted_phrase)

#output

#I like to learn coding on the go
#I like ta learn cading on the go
```

If you only wanted to change the first instance of a single character, you would set the `count` parameter to one:

```python
phrase = "I like to learn coding on the go"

# replace only the first instance of 'o' with 'a'
substituted_phrase = phrase.replace("o", "a", 1 )

print(phrase)
print(substituted_phrase)

#output

#I like to learn coding on the go
#I like ta learn coding on the go
```

### How to Replace All Instances of a String

To change more than one character, the process looks similar.

```python
phrase = "The sun is strong today. I don't really like sun."

#replace all instances of the word 'sun' with 'wind'
substituted_phrase = phrase.replace("sun", "wind")

print(phrase)
print(substituted_phrase)

#output

#The sun is strong today. I don't really like sun.
#The wind is strong today. I don't really like wind.
```

In the example above, the word `sun` was replaced with the word `wind`.

### How to Replace Only a Certain Number of Instances of a String

If you wanted to change only the first instance of `sun` to `wind`, you would use the `count` parameter and set it to one.

```python
phrase = "The sun is strong today. I don't really like sun."

#replace only the first instance of the word 'sun' with 'wind'
substituted_phrase = phrase.replace("sun", "wind", 1)

print(phrase)
print(substituted_phrase)

#output

#The sun is strong today. I don't really like sun.
#The wind is strong today. I don't really like sun.
```

## How to Perform Case-Insensitive Substring Substitution in Python

Let's take a look at another example.

```python

phrase = "I am learning Ruby. I really enjoy the ruby programming language!"

#replace the text "Ruby" with "Python"
substituted_text = phrase.replace("Ruby", "Python")

print(substituted_text)

#output

#I am learning Python. I really enjoy the ruby programming language!
```

In this case, what I really wanted to do was to replace all instances of the word `Ruby` with `Python`. 

However, there was the word `ruby` with a lowercase `r`, which I would also like to change.

Because the first letter was in lowercase, and not uppercase as I specified with `Ruby`, it remained the same and didn't change to `Python`.

The `.replace()` method is *case-sensitive*, and therefore it performs a case-sensitive substring substitution.

In order to perform a *case-insensitive* substring substitution you would have to do something different.

You would need to use the `re.sub()` function and use the `re.IGNORECASE` flag.

To use `re.sub()` you need to:

- Use the `re` module, via `import re`.
- Speficy a regular expression `pattern`.
- Mention with what you want to `replace` the pattern.
- Mention the `string` you want to perform this operation on.
- Optionally, specify the `count` parameter to make the replacement more precise and specify the maximum number of replacements you want to take place.
- The `re.IGNORECASE` flag tells the regular expression to perform a case-insensitive match.

So, all together the syntax looks like this:

```python
import re

re.sub(pattern, replace, string, count, flags) 
```

Taking the example from earlier:

```python
phrase = "I am learning Ruby. I really enjoy the ruby programming language!"
```

This is how I would replace both `Ruby` and `ruby` with `Python`:

```python
import re

phrase = "I am learning Ruby. I really enjoy the ruby programming language!"

phrase = re.sub("Ruby","Python", phrase, flags=re.IGNORECASE)

print(phrase)

#output

#I am learning Python. I really enjoy the Python programming language!
```

## Wrapping up

And there you have it - you now know the basics of substring substitution. Hopefully you found this guide helpful.

To learn more about Python, check out freeCodeCamp's [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/). 

You'll start from the basics and learn in an interacitve and beginner-friendly way. You'll also build five projects at the end to put into practice and help reinforce what you learned.

Thanks for reading and happy coding!



