---
title: Python Open File – How to Read a Text File Line by Line
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-09-13T14:00:03.000Z'
originalURL: https://freecodecamp.org/news/python-open-file-how-to-read-a-text-file-line-by-line
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/alex-chumak-zGuBURGGmdY-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "In Python, there are a few ways you can read a text file. \nIn this article,\
  \ I will go over the open() function, the read(), readline(), readlines(), close()\
  \ methods, and the with keyword.\nWhat is the open() function in Python?\nIf you\
  \ want to read a t..."
---

In Python, there are a few ways you can read a text file. 

In this article, I will go over the `open()` function, the `read()`, `readline()`, `readlines()`, `close()` methods, and the `with` keyword.

## What is the open() function in Python? 

If you want to read a text file in Python, you first have to open it.

This is the basic syntax for Python's `open()` function:

```py
open("name of file you want opened", "optional mode")
```

### File names and correct paths

If the text file and your current file are in the same directory ("folder"), then you can just reference the file name in the `open()` function. 

```py
open("demo.txt")
```

Here is an example of both files being in the same directory:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-1.49.16-AM.png)

If your text file is in a different directory, then you will need to reference the correct path name for the text file. 

In this example, the `random-text` file is inside a different folder then `main.py`:

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-2.00.27-AM.png)

In order to access that file in the `main.py`, you have to include the folder name with the name of the file.

```py
open("text-files/random-text.txt")
```

If you don't have the correct path for the file, then you will get an error message like this:

```py
open("random-text.txt")
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-2.03.33-AM.png)

It is really important to keep track of which directory you are in so you can reference the correct path name. 

### Optional Mode parameter in `open()`

There are different modes when you are working with files. The default mode is the read mode. 

The letter `r` stands for read mode. 

```py
open("demo.txt", mode="r")
```

You can also omit `mode=` and just write `"r"`.

```py
open("demo.txt", "r")
```

There are other types of modes such as `"w"` for writing or `"a"` for appending.  I am not going to go into detail for the other modes because we are just going to focus on reading files. 

For a complete list of the other modes, please read through the [documentation](https://docs.python.org/3/library/functions.html#open). 

### Additional parameters for the `open()` function in Python

The `open()` function can take in these optional parameters. 

* buffering
* encoding
* errors
* newline
* closefd
* opener

To learn more about these optional parameters, please read through the [documentation](https://docs.python.org/3/library/functions.html#open). 

## What is the readable() method in Python? 

If you want to check if a file can be read, then you can use the `readable()` method. This will return a `True` or `False`.

This example would return `True` because we are in the read mode:

```py
file = open("demo.txt")
print(file.readable())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.36.37-AM.png)

If I changed this example, to `"w"` (write) mode, then the `readable()` method would return `False`:

```py
file = open("demo.txt", "w")
print(file.readable())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.36.18-AM.png)

## What is the read() method in Python? 

The `read()` method is going to read all of the content of the file as one string. This is a good method to use if you don't have a lot of content in the text file. 

In this example, I am using the `read()` method to print out a list of names from the `demo.txt` file:

```py
file = open("demo.txt")
print(file.read())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-2.43.59-AM.png)

This method can take in an optional parameter called size. Instead of reading the whole file, only a portion of it will be read.

If we modify the earlier example, we can print out only the first word by adding the number 4 as an argument for `read()`. 

```py
file = open("demo.txt")
print(file.read(4))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.01.30-AM.png)

If the size argument is omitted, or if the number is negative, then the whole file will be read. 

## What is the close() method in Python? 

Once you are done reading a file, it is important that you close it. If you forget to close your file, then that can cause issues.

This is an example of how to close the `demo.txt` file:

```py
file = open("demo.txt")
print(file.read())
file.close()
```

### How to use the `with` keyword to close files in Python

One way to ensure that your file is closed is to use the `with` keyword. This is considered good practice, because the file will close automatically instead of you having to manually close it. 

Here is how to rewrite our example using the `with` keyword:

```py
with open("demo.txt") as file:
    print(file.read())
```

## What is the readline() method in Python? 

This method is going to read one line from the file and return that.

In this example, we have a text file with these two sentences:

```txt
This is the first line
This is the second line
```

If we use the `readline()` method, it will only print the first sentence of the file. 

```py
with open("demo.txt") as file:
    print(file.readline())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-3.57.14-AM.png)

This method also takes in the optional size parameter. We can modify the example to add the number 7 to only read and print out `This is`:

```py
with open("demo.txt") as file:
    print(file.readline(7))
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-4.08.03-AM.png)

## What is the readlines() method in Python? 

This method will read and return a list of all of the lines in the file. 

In this example, we are going to print out our grocery items as a list using the `readlines()` method. 

```py
with open("demo.txt") as file:
    print(file.readlines())
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-4.19.23-AM.png)

## How to use a for loop to read lines from a file in Python

An alternative to these different read methods would be to use a `for loop`.

In this example, we can print out all of the items in the `demo.txt` file by looping over the object. 

```py
with open("demo.txt") as file:
    for item in file:
        print(item)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-13-at-4.27.49-AM.png)

## Conclusion

If you want to read a text file in Python, you first have to open it.

```py
open("name of file you want opened", "optional mode")

```

If the text file and your current file are in the same directory ("folder"), then you can just reference the file name in the `open()` function. 

If your text file is in a different directory, then you will need to reference the correct path name for the text file. 

The `open()` function takes in the optional mode parameter. The default mode is the read mode. 

```py
open("demo.txt", "r")
```

If you want to check if a file can be read, then you can use the `readable()` method. This will return a `True` or `False`.

```py
file.readable()
```

The `read()` method is going to read all of the content of the file as one string.

```py
file.read()
```

Once you are done reading a file, it is important that you close it. If you forget to close your file, then that can cause issues.

```py
file.close()
```

One way to ensure that your file is closed is to use the `with` keyword.

```py
with open("demo.txt") as file:
    print(file.read())
```

The `readline()` method is going to read one line from the file and return that.

```py
file.readline()
```

The `readlines()` method will read and return a list of all of the lines in the file.

```py
file.readlines()
```

An alternative to these different read methods would be to use a `for loop`.

```py
with open("demo.txt") as file:
    for item in file:
        print(item)
```

I hope you enjoyed this article and best of luck on your Python journey.   


  

