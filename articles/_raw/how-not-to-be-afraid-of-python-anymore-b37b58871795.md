---
title: How not to be afraid of Python anymore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T22:03:21.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-python-anymore-b37b58871795
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YOVsFZ95l6WcVFXf
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Neil Kakkar

  A dive into the language reference documentation

  For the first year or two when I started coding, I thought learning a language was
  all about learning the syntax. So, that’s all I did.

  Needless to say, I didn’t turn into a great develo...'
---

By Neil Kakkar

#### A dive into the language reference documentation

For the first year or two when I started coding, I thought learning a language was all about learning the syntax. So, that’s all I did.

Needless to say, I didn’t turn into a great developer. I was stuck. Then, one fine day, it just clicked. I realised I was doing this wrong. Learning the syntax should be the least of my concerns. What matters is everything else about the language. What exactly is all that? Read on.

This article is divided into three main subparts: The Data Model, the Execution model and the Lexical analysis.

This article is more an insight into how things work in Pythonland — in contrast to how to learn Python. You’ll find many how-to learning sources online.

What I didn’t find online was a single source of common ‘gotchas’ in Python. A source explaining how the language works. This attempts to solve that problem. I think I’ve come up short, there’s so much to it!

Everything here comes from the official documentation. I’ve condensed it — to the important points, reordered stuff and added my examples. All links point to the documentation.

Without further ado, here we go.

### Data Model

#### Objects, values and types

[Objects](https://docs.python.org/3.7/reference/datamodel.html#objects-values-and-types) are Python’s abstraction for data.

Every object has its unique fixed `identity`, a fixed `type` and a `value`.

‘Fixed’ means the `identity` and `type` of an `Object` can never change.

The `value` may change. Objects whose value can change are called **mutable** while objects whose value can’t change are called **immutable**.

The mutability is determined by `type` :

* Numbers, Strings and Tuples are immutable
* Lists and Dictionaries are mutable

The identity of objects can be compared via the `is` operator.

`id()` returns the `identity`

`type()` returns the `type`

> Note: The value of an immutable container object that contains a reference to a mutable object can change when the latter’s value is changed. However, the container is still considered immutable, because the collection of objects it contains cannot be changed. So, immutability is not strictly the same as having an unchangeable value.

This note made my head spin the first two times I read it.

Simple translation: Immutability is not the same as unchangeable value. In the example below, the `tuple` is `immutable`, while it’s `value` keeps changing (as the `list` changes).

Example:

```python
>>> t = ("a", [1]) # a tuple of string and list
>>> id(t)
4372661064
>>> t
('a', [1])
>>> type(t)
<class 'tuple'>
>>> t[1]
[1]
>>> t[1].append(2)
>>> t
('a', [1, 2])
>>> id(t)
4372661064
>>> type(t)
<class 'tuple'>
```

The tuple is immutable, even though it contains a mutable object, a list.

Compare this to a string, where changing the existing array changes the object (since strings are immutable).

```py
>>> x = "abc"
>>> id(x)
4371437472
>>> x += "d"
>>> x
'abcd'
>>> id(x)
4373053712
```

Here, the name , `x` is bound to another object of type string. This changes its id as well.

The original object, being immutable, stays immutable. The binding is explained in further detail below, which should make things clearer.

#### Built-in types

Python comes with several [built-in types](https://docs.python.org/3.7/reference/datamodel.html#the-standard-type-hierarchy):

#### None

The type is represented by a single object, hence a single value. The sole object with `type = NoneType`

```py
>>> type(None)
<class 'NoneType'>
```

#### Numbers

This is a collection of abstract base classes used to represent numbers. They can’t be instantiated, and `int`, `float` inherit from `numbers.Number`.

They are created by numeric literals and arithmetic operations. The returned objects are immutable, as we have seen. The following list of examples will make this clear:

```py
>>> a = 3 + 4
>>> type(a)
<class 'int'>
>>> isinstance(a, numbers.Number)
True
>>> isinstance(a, numbers.Integral)
True
>>> isinstance(3.14 + 2j, numbers.Real)
False
>>> isinstance(3.14 + 2j, numbers.Complex)
True
```

#### Sequences

These represent finite ordered sets indexed by non negative integers. Just like an array from other languages.

`len()` returns the length of sequences. When length is `n`, the index set has elements from `0...n-1` . Then the ith element is selected by `seq[i-1]`.

For a sequence `l`, you can select elements in between indexes using slicing: `l[i:j]`.

There are two types of sequences: mutable and immutable.

* Immutable sequences include: strings, tuples and bytes.
* Mutable sequences include: lists and byte arrays

#### Sets

These represent unordered, finite sets of unique, immutable objects. They can’t be indexed, but can be iterated over. `len()` still returns the number of items in the set.

There are two types of sets: mutable and immutable.

* A mutable set is created by `set()`.
* An immutable set is created by `frozenset()`.

#### Mappings

#### Dictionary

These represent finite sets of objects indexed by nearly arbitrary values. Keys can’t be mutable objects. That includes lists, other dictionaries and other objects that are compared by value, and not by object identity.

This means a `frozenset` can be a dictionary key too!

#### **Modules**

A module object is a basic organisational unit in Python. The namespace is implemented as a dictionary. Attribute references are lookups in this dictionary.

For a module `m`, the dictionary is read-only, accessed by `m.__dict__` .

It’s a regular dictionary so you can add keys to it!

Here’s an example, with the [Zen of Python](https://www.python.org/dev/peps/pep-0020/):

We are adding our custom function, `figure()` to the module `this`.

```
>>> import this as t
>>> t.__dict__
{'__name__': 'this', '__doc__': None, '__package__': '',
.....
.....
's': "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna
vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!",
'd': {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 
'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'},
'c': 97,
'i': 25
}
>>> def figure():
...   print("Can you figure out the Zen of Python?")
... 
>>> t.fig = figure
>>> t.fig()
Can you figure out the Zen of Python?
>>> t.__dict__
{'__name__': 'this', '__doc__': None, '__package__': '',
.....
.....
's': "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna
vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!",
'd': {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 
'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'},
'c': 97,
'i': 25
'fig': <function figure at 0x109872620>
}
>>> print("".join([t.d.get(c, c) for c in t.s]))
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Not very useful either, but good to know.

#### Operator Overloading

Python allows for [operator overloading](https://docs.python.org/3.7/reference/datamodel.html#special-method-names).

Classes have special function names — methods they can implement to use Python’s defined operators. This includes slicing, arithmetic operations and subscripting.

For example, `__getitem__()` refers to subscripting. Hence, `x[i]` is equivalent to `type(x).__getitem__(x,i)`.

Hence, to use the operator `[]` on a class `someClass` : you need to define `__getitem__()` in `someClass`.

```py
>>> class operatorTest(object):
...     vals = [1,2,3,4]
...     def __getitem__(self, i):
...         return self.vals[i]
... 
>>> x = operatorTest()
>>> x[2]
3
>>> x.__getitem__(2)
3
>>> type(x)
<class '__main__.OperatorTest'>
>>> type(x).__getitem__(x,2)
3
>>> OperatorTest.__getitem__(x,2)
3
```

Confused about why all of them are equivalent? That’s for next part — where we cover class and function definitions.

Likewise, the `__str__()` [function](https://docs.python.org/3.7/reference/datamodel.html#object.__str__) determines the output when the `str()` method is called on an object of your class.

For comparison operations, the special function names are:

* `object.__lt__(self, other)` for `<` (“less than”)
* `object.__le__(self, other)` for `≤` (“less than or equal to”)
* `object.__eq__(self, other)` for `==` (“equal to”)
* `object.__ne__(self, other)` for `!=` (“not equal to”)
* `object.__gt__(self, other)` for `>` (“greater than”)
* `object.__ge__(self, other)` for `≥` (“greater than or equal to”)

So for example, `x < y` is called as `x.__lt__`(y)

There are also [special functions for arithmetic operations](https://docs.python.org/3.7/reference/datamodel.html#emulating-numeric-types), like `object.__add__(self, other)`.

As an example, `x+y` is called as `x.__add__(y)`

Another interesting [function](https://docs.python.org/3.7/reference/datamodel.html#object.__iter__) is `__iter__()`.

You call this method when you need an iterator for a container. It returns a [new iterator object](https://docs.python.org/3.7/library/stdtypes.html#iterator-types) that can iterate over all the objects in the container.

For mappings, it should iterate over the keys of the container.

The iterator object itself supports two methods:

* `iterator.__iter__()` : Returns the object itself.

This makes `iterators` and the `containers` equivalent.

This allows the iterator and containers both to be used in `for` and `in` statements.

* `iterator.__next__()` : Returns the next item from the container. If there are no further items, raises the `StopIteration` exception.

```py
class IterableObject(object):    # The iterator object class
     vals = []
     it = 0
     def __init__(self, val):
         self.vals = val
         it = 0
 
     def __iter__(self):
         return self
 
     def __next__(self):
         if self.it < len(self.vals):
             index = self.it
             self.it += 1
             return self.vals[index]
         raise StopIteration
 
 class IterableClass(object):    # The container class
       vals = [1,2,3,4]
 
       def __iter__(self):
         return iterableObject(self.vals)
>>> iter_object_example = IterableObject([1,2,3])
>>> for val in iter_object_example:
...   print(val)
... 
1
2
3
>>> iter_container_example = IterableClass()
>>> for val in iter_container_example:
...  print(val)
... 
1
2
3
4
```

Cool stuff, right? There’s also a direct equivalent in Javascript.

[Context Managers](https://docs.python.org/3.7/reference/datamodel.html#with-statement-context-managers) are also implemented via operator overloading.

`with open(filename, 'r') as f`

`open(filename, 'r')` is a context manager object which implements

`object.__enter__(self)` and

`object.__exit__(self, exc_type, exc_value, traceback)`   
All the above three parameters are null when error is `None`.

```py
class MyContextManager(object):
    def __init__(self, some_stuff):
        self.object_to_manage = some_stuff
    def __enter__(self):
        print("Entering context management")
        return self.object_to_manage # can do some transforms too
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Successfully exited")
            # Other stuff to close
>>> with MyContextManager("file") as f:
...     print(f)
... 
Entering context management
file
Successfully exited
```

This isn’t useful — but gets the point across. Does that make it useful anyway?

![Image](https://cdn-media-1.freecodecamp.org/images/vJ7yWCli55L8Sn1i-cnzBNyjXJm8quKKcPRq)
_[Philosoraptor](https://www.google.co.uk/search?q=Philosoraptor" rel="noopener" target="_blank" title=")_

### Execution Model

A block is a piece of code executed as a unit in an execution frame.

Examples of blocks include:

* Modules, which are top level blocks
* Function body
* Class definition
* But NOT `for` loops and other control structures

Remember how everything is an `object` in Python?

Well, you have `names` bound to these `objects`. These `names` are what you think of as variables.

```py
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

Name binding, or assignment occurs in a block.

Examples of name binding — these are intuitive:

* Parameters to functions are bound to the names defined in the function
* Import statements bind name of module
* Class and function definitions bind the name to class / function objects
* Context managers: `with ... as f` : f is the name binding to the `...` object

Names bound to a block are local to that block . That means global variables are simply names bound to the module.

Variables used in a block without being defined there are free variables.

Scopes define visibility of a name in a block. The scope of a variable includes the block it is defined in, as well as all blocks contained inside the defining block.

Remember how for loops aren’t blocks? That’s why iteration variables defined in the loop are accessible after the loop, unlike in C++ and JavaScript.

```py
>>> for i in range(5):
...   x = 2*i
...   print(x, i)
... 
0 0
2 1
4 2
6 3
8 4
>>> print(x, i)    # outside the loop! x was defined inside.
8 4
```

When a name is used in a block, it is resolved using the nearest enclosing scope.

> Note: If a name binding operation occurs anywhere within a code block, all uses of the name within the block are treated as references to the current block. This can lead to errors when a name is used within a block before it is bound.

For example:

```
>>> name = "outer_scope"
>>> def foo():
...     name = "inner_function" if name == "outer_scope" \
                else "not_inner_function"
... 
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'name' referenced before assignment
```

This is a wonderful traceback, which should make sense now.

We have the top level block, the module — in which there’s another block, the function. Every binding inside the function has the function as its top level scope!

Hence, when you’re binding the name `name` to the object `"inner_function"` : before the binding you’re checking its value. The rule says you can’t reference it before the binding. Exactly the reason for the `UnboundLocalError`.

![Image](https://cdn-media-1.freecodecamp.org/images/3vBeauEpskRngPsPSWn2ww0KsgA3mNCGGzjl)
_Not this kind of **Execution Model**? [Source](https://myanimelist.net/featured/1195/Top_25_Badass_Anime_Warrior_Girls" rel="noopener" target="_blank" title=")_

### Lexical Analysis

Python lets you use [line joinings](https://docs.python.org/3.7/reference/lexical_analysis.html#explicit-line-joining). To explicitly continue lines, use a backslash.

Comments aren’t allowed after line joinings.

```py
if a < 10 and b < 10 \ # Comment results in SyntaxError
and c < 10: # Comment okay
    return True
else:
    return False
```

Implicitly, line joining occurs on its own when elements are inside braces. Comments here are allowed.

```py
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year
```

#### Indentation

The number of spaces / tabs in the [indentation](https://docs.python.org/3.7/reference/lexical_analysis.html#indentation) doesn’t matter, as long as it’s increasing for things that should be indented. The first line shouldn’t be indented.

The four spaces rule is a convention defined by [PEP 8: Style Guide](https://www.python.org/dev/peps/pep-0008/#string-quotes). It’s good practice to follow it.

```py
# Compute the list of all permutations of l.
def perm(l):
        # Comment indentation is ignored
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]     # Indentation level chosen
             p = perm(s)             # Must be same level as above
             for x in p:
              r.append(l[i:i+1] + x) # One space okay
    return r
```

There are a few reserved identifiers as well.

* `_` for import: functions / variables starting with `_` aren’t imported.
* `__*__` for system defined names, defined by implementation : we’ve seen a few of these. ( `__str__()`, `__iter__()`, `__add__()` )

Python also offers [Implicit String Literal concatenation](https://docs.python.org/3.7/reference/lexical_analysis.html#string-literal-concatenation)

```py
>>> def name():
...   return "Neil" "Kakkar"
...
>>> name()
'Neil Kakkar'
```

#### Format Strings

[String formatting](https://docs.python.org/3.7/reference/lexical_analysis.html#formatted-string-literals) is a useful tool in Python.

Strings can have `{ expr }` in the string literal where `expr` is an expression. The expression evaluation is substituted in place.

Conversions can be specified to convert the result before formatting.

`!r` calls `repr()`, `!s` calls `str()` and `!a` calls `ascii()`

```py
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}."  # repr() is equiv. to !r
"He said his name is 'Fred'."
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
# This is same as "{decf:10.4f}".format(decf=float(value))
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}"  # using date format specifier
'January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}"  # using hexadecimal format specifier
'0x400'
```

It’s a cleaner syntax to using `[str.format()](https://docs.python.org/3.7/library/stdtypes.html#str.format)`

### Summary

With this, we’ve covered the major pillars of Python. The object data model, execution model with its scopes and blocks and some bits on strings. Knowing all this puts you ahead of every developer who only knows the syntax. That’s a higher number than you think.

Other stories in this series:

* [How not to be afraid of Vim anymore](https://medium.freecodecamp.org/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae)
* [How not to be afraid of GIT anymore](https://medium.freecodecamp.org/how-not-to-be-afraid-of-git-anymore-fe1da7415286)

Enjoyed this? [Don’t miss a post again — subscribe to my mailing list!](http://neilkakkar.com/subscribe/)

