---
title: Python Create File – How to Append and Write to a Text File
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-07T16:44:25.000Z'
originalURL: https://freecodecamp.org/news/python-create-file-how-to-append-and-write-to-a-text-file
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/s-migaj-ocUAiaMTCM0-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'In coding, files are used to store data. Then you can easily access that
  data at any point.

  Reading, writing, and editing files in Python is a common task, since the language
  provides us with built-in functions that allow us to do so.

  In this article...'
---

In coding, files are used to store data. Then you can easily access that data at any point.

Reading, writing, and editing files in Python is a common task, since the language provides us with built-in functions that allow us to do so.

In this article, I'll create a simple project where I'll write to, append to, and then finally at the end read from a text file in Python to show you how it's done.

You can follow along with me and go through the same steps I do.

Let's get started!

## How to set up the project's structure

The first step is to set up the project's directory structure.

Choose a place where you want to create a new directory and follow the  steps below. 

I am creating the project in my home directory.

```bash
#this command moves you into your home directory if you're not there already
cd 

#create a new directory and give it a name
mkdir python_text

#move into the directory you just created
cd python_text

#create two empty files in the same directory: one text file and one to hold your Python scripts
touch text.txt scripts.py

#open Visual Studio Code to edit
code .
```

At the moment, the text file is empty:

![Screenshot-2021-09-02-at-11.17.28-AM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-11.17.28-AM.png)

Let's add something to it.

## How to write to text files in Python

The best practice for writing to, appending to, and reading from text files in Python is using the `with` keyword.

The general syntax looks like this:

```
with open("path_to_and_name_of_file","mode") as variable_name:
    variable_name.write('What I want to write goes here')
```

Breakdown:

- You first start off with the `with` keyword.
- Next, you open the text file. The `open()` function returns a file object and takes in two parameters: The path to the file and the name of the file itself that you want to open. The file in this example is in the same directory as the Python script, so the path is simple. The second parameter is the mode in which the file will be opened. To write to files, the mode is `w` for `write`.
- Then we have the `as` keyword.
- Next, the variable name acts as a temporary storage place for the text contents you are going to store.
- The `.write()` method is used for writing in the text file and adding in the string contents you want.

So, to add some text to the text file, in `scripts.py` add:

```python
with open("text.txt","w") as file:
    file.write("I am learning Python!\n")
    file.write("I am really enjoying it!\n")
    file.write("And I want to add more lines to say how much I like it")
```

To add the text on different lines, like I have done in the example above, you have to explicitly add in the newline character,`\`, yourself.

Open the built-in terminal in Visual Studio Code (`Control ~`) and run the code by typing: `python3 scripts.py`.

Check out `text.txt` and it should have the following added to it:

![Screenshot-2021-09-02-at-6.51.51-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-6.51.51-PM.png)

It's important to note that each time you use the `.write()` method and run your code, any text you previously had will be overwritten. 

Let's say I already had some dummy text in my `text.txt` file when I first created it:

![Screenshot-2021-09-02-at-7.03.03-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.03.03-PM.png)

If I run the previous code:

```python
with open("text.txt","w") as file:
    file.write("I am learning Python!\n")
    file.write("I am really enjoying it!\n")
    file.write("And I want to add more lines to say how much I like it")
```

It will now look like this:

![Screenshot-2021-09-02-at-7.04.23-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.04.23-PM.png)

I have lost all my previous data.


## How to append a text file in Python

Appending works similarly to writing.

But this time, you open the text file for appending, with the parameter for the mode in the `open()` function being `a` for `append` :

```
with open("text.txt","a") as file:
    file.write("What I want to add on goes here")
```

Whatever goes in the `.write()` method will be added to the end of the text file.

So, to add some more text to `text.txt` you add the follwoing:


```python
with open("text.txt","a") as file:
    file.write("I am adding in more lines\n")
    file.write("And more…")
```

After running the code again, `text.txt` should now look like this:

![Screenshot-2021-09-02-at-7.15.51-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.15.51-PM.png)

The previous text doesn't get erased.

The new text gets added immediately after the old, and you again have to explicitly add in a newline character:

```python
with open("text.txt","a") as file:
    file.write("\n")
    file.write("I am adding in more lines\n")
    file.write("And more…")
```

![Screenshot-2021-09-02-at-7.18.15-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-02-at-7.18.15-PM.png)

## How to read from a file in Python

To read from a file, you again use the `with` keyword and the `open()` function with two arguments: the first one is the path to and name of the file, and the second one is the mode in which the file will be opened. 

For opening text files, the mode is `r` for `read`.

Then, the `print()` function prints to the console and take as arguments the variable name with the `read()` function.

```python
with  open('text.txt','r') as file:
    print(file.read())
```

Output:

![Screenshot-2021-09-07-at-1.44.04-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-07-at-1.44.04-PM.png)

To read from a file in Python, you could also create a `for` loop to loop through each line from the text file:

```python
with open("text.txt","r") as file:
    for line in file:
        print(line)
```

Output:

![Screenshot-2021-09-07-at-1.46.25-PM](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-07-at-1.46.25-PM.png)

With this way, each line is printed out separately.

## Conclusion

This article showed you some simple examples of how to write, edit, and read from files in Python.

If you want to learn more about the Python programming language, freeCodeCamp has a free [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/) where you start from the basics and move to the more complex aspects of the language. At the end, you'll build five projects to put to practice what you have learned.

Thanks for reading and happy learning!



