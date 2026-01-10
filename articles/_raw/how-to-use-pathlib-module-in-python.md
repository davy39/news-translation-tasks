---
title: Python Path – How to Use the Pathlib Module with Examples
subtitle: ''
author: Rochdi Khalid
co_authors: []
series: null
date: '2022-05-10T13:59:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pathlib-module-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pathlib-cover-freecodecamp.jpg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: null
seo_desc: "Each operating system has different rules for constructing file paths.\
  \ For example, Linux uses forward slashes for paths, while Windows uses backslashes.\
  \ \nThis small difference can cause issues if you are working on a project and you\
  \ want other devel..."
---

Each operating system has different rules for constructing file paths. For example, Linux uses forward slashes for paths, while Windows uses backslashes. 

This small difference can cause issues if you are working on a project and you want other developers who come from different operating systems to expand your code. 

Fortunately, if you're coding in Python, the Pathlib module does the heavy lifting by letting you make sure that your file paths work the same in different operating systems. Also, it provides functionalities and operations to help you save time while handling and manipulating paths.

## Prerequisites

Pathlib comes as default with Python >= 3.4. However, if you are using a version of Python lower than 3.4, you won't have access to this module.

## How Does Pathlib Work?

To understand how you can construct a basic path using Pathlib, let's create a new Python file called `example.py` and put it inside a particular directory.

Open the file, and type the following content:

```python
import pathlib

p = pathlib.Path(__file__)
print(p)

```

In this example, we import the Pathlib module. Then, we create a new variable called `p` to store the path. Here, we use the Path object from Pathlib with a built-in variable in Python called **__file__** to refer to the file path we are currently writing in it `example.py`.

If we print `p`, we will get the path to the file we are currently in:

```
/home/rochdikhalid/dev/src/package/example.py
```

As shown above, Pathlib creates a path to this file by putting this particular script in a Path object. Pathlib contains many objects such as `PosixPath()` and `PurePath()`, which we will learn more about in the following sections.

Before we jump into this, Pathlib divides the filesystem paths into two different classes that represent two types of path objects: **Pure Path** and **Concrete Path**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/pathlib-diagram.png)
_PurePath() classes_

The pure path provides utilities to handle and manipulate your file path without making writing operations, while the concrete path allows you to manipulate and do writing operations on your file path. 

In other words, a concrete path is a subclass of a Pure path. It inherits manipulation from the parent class and adds input/output operations that do system calls.

## Pure paths in Python

Pure paths manipulate a file path on your machine even if it belongs to a different operating system. 

For example, let's say you are on Linux and you want to use a Windows file path. Here, Pure path class objects will help you get the path working on your machine with some basic operations like creating child paths or accessing individual parts of a path. 

But pure paths won't be able to mimic some other operations like creating a directory or a file because you are not actually in that operating system.

### How to use pure paths

As you can see in the diagram above, pure paths consist of three classes that handle any file system path on your machine:

**PurePath()** is the root node that provides handling operations to every path object in Pathlib. 

When you instantiate `PurePath()`, it creates two classes to handle Windows paths and non-Windows paths. `PurePath()` creates a generic path object "agnostic path", regardless of the operating system you are running on.

```python
In [*]: pathlib.PurePath('setup.py')                                            
Out[*]: PurePosixPath('setup.py')

```

PurePath() in the example above creates a `PurePosixPath()` because we assumed we are running on a Linux machine. But if you instantiate it on Windows you will get something like `PureWindowsPath('setup.py')`.

**PurePosixPath()** is the child node of PurePath() implemented for non-Windows file system paths.

```python
In [*]: pathlib.PurePosixPath('setup.py')                                            
Out[*]: PurePosixPath('setup.py')

```

You will not get any error if you instantiate `PurePosixPath()` on Windows because too simply this class doesn't make system calls.

**PureWindowsPath()** is the child node of PurePath() implemented for Windows file system paths.

```python
In [*]: pathlib.PureWindowsPath('setup.py')                                     
Out[*]: PureWindowsPath('setup.py')

```

The same applies to `PureWindowsPath()` since this class doesn't provide system calls, so instantiating it will not raise any error for other operating systems.

### Pure path properties

Each subclass in **`PurePath()`** provides the following properties:

**PurePath().parent** outputs the parent of the path:

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').parent                     
Out[*]: PurePosixPath('/src/goo/scripts')

```

In the example above, we are using the `.parent` property to get the path of the logical parent of `**main.py**`.

**PurePath().parents[]** outputs the ancestors of the path:

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
		p.parents[0]               
Out[*]: PurePosixPath('/src/goo/scripts')

In [*]: p.parents[1]                
Out[*]: PurePosixPath('/src/goo')

```

You should always specify the ancestor index in the square brackets as seen above. In Python 3.10 and above, you can use slices and negative index values.

**PurePath().name** provides the name of the last component of your path:

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').name                      
Out[*]: 'main.py'

```

In this example, the final path component is `main.py`. So, the `.name` property outputs the name of the file `main.py` which is **main** with its suffix **.py**.

On the other hand, **PurePath().suffix** provides the file extension of the last component of your path:

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').suffix                    
Out[*]: '.py'

```

Compared to the `.name` property, the `.suffix` property outputs the file extension and excludes the file name.

**PurePath().stem** outputs only the name of the final component of your path without the suffix:

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').stem                      
Out[*]: 'main'

```

As seen above, the `.stem` property excludes the suffix of the final component `main.py` and provides only the name of the file.

### Pure path methods

Each subclass of `PurePath()` provides the following methods:

**PurePath().is_absolute()** checks whether your path is absolute or not:

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.is_absolute()

Out[*]: True

In [*]: o = pathlib.PurePath('scripts/main.py')
        o.is_absolute()

Out[*]: False

```

Note that the absolute path consists of a root and drive name. In this case, `PurePath()` doesn't allow us to know the drive's name. 

If you use `PureWindowsPath()`, you can represent an absolute path that contains a drive name like `PureWindowsPath('c:/Program Files')`.

**PurePath().is_relative()** checks whether the path belongs to the other given path or not:

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.is_relative_to('/src')

Out[*]: True

In [*]: p.is_relative_to('/data')

Out[*]: False

```

In this example, the given path `/src` is a part of or belongs to the path `p`, while the other given path `/data` raises `False` because it has no relative relationship with the path `p`.

**PurePath().joinpath()** concatenates the path with the given arguments (child paths):

```python
In [*]: p = pathlib.PurePath('/src/goo')
        p.joinpath('scripts', 'main.py')

Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

Note that there is no need to add slashes in your given arguments, as the `.joinpath()` method handles this for you.

**PurePath().match()** checks whether the path matches a given pattern:

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').match('*.py')
Out[*]: True

In [*]: pathlib.PurePath('/src/goo/scripts/main.py').match('goo/*.py')
Out[*]: True

In [*]: pathlib.PurePath('src/goo/scripts/main.py').match('/*.py')
Out[*]: False

```

Based on the examples above, the pattern should match the path. If the given pattern is absolute, the path must be absolute too.

**PurePath().with_name()** changes the name of the final component with its suffix:

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.with_name('app.js')
Out[*]: PurePosixPath('/src/goo/scripts/app.js')

In [*]: p
Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

The `.with_name()` method doesn't change the name of the last component permanently. Also, if the given path doesn't contain a name, an error occurs as mentioned in the [official documentation](https://docs.python.org/3/library/pathlib.html#methods-and-properties).

**PurePath().with_stem()** changes only the name of the final component of the path:

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.with_stem('app.py')
Out[*]: PurePosixPath('/src/goo/scripts/app.py')

In [*]: p
Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

This is similar to the `.with_name()` method. The `.with_stem()` changes the name of the last component temporarily. Also, if the given path doesn't contain a name, an error will occur.

**PurePath().with_suffix()** temporarily changes the suffix or the extension of the final component of your path:   

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.with_suffix('.js')
Out[*]: PurePosixPath('/src/goo/scripts/main.js')

```

If the name of the given path contains no suffix, the `.with_suffix()` method adds the suffix for you:

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main')
        p.with_suffix('.py')
Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

But, if we don't include the suffix and we keep the argument empty `''`, the current suffix will be removed.

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main')
        p.with_suffix('')
Out[*]: PurePosixPath('/src/goo/scripts/main')

```

Some methods like `.with_stem()`, and `.is_relative_to()` have been added recently to Python 3.9 and above. So, if you call these methods using Python 3.8 or lower, an attribute error is raised.

## Concrete Paths in Python

Concrete Paths allows you to handle, manipulate, and do writing operations on different filesystem paths. 

In the other words, this type of path object helps you to create for example a new file, a new directory, and do other input/output operations while not being in that operating system.

### How to use concrete paths

Concrete paths handle any file system path and make system calls on your machine. Those path objects are the child paths of the pure paths and consist of three subclasses like the pure ones:

**Path()** is the child node of `PurePath()`, it provides handling operations with the ability to do writing operations on your path. 

When you instantiate `Path()`, it creates two classes to handle Windows paths and non-Windows paths. Like `PurePath()`, `Path()` also creates a generic path object "agnostic path", regardless of the operating system you are running on.

```python
In [*]: pathlib.Path('setup.py')                                            
Out[*]: PosixPath('setup.py')

```

`Path()` in the example above creates a `PosixPath()` because we assume we are running on a Linux machine. But if you instantiate it on Windows you will get something like `WindowsPath('setup.py')`

**PosixPath()** is the child node of `Path()` and `PurePosixPath()`, implemented to handle and manipulate non-Windows file system paths.

```python
In [*]: pathlib.PosixPath('setup.py')                                            
Out[*]: PosixPath('setup.py')

```

You will get an error if you instantiate `PosixPath()` on a Windows machine because you cannot make system calls while running on a different operating system.

**WindowsPath()** is the child node of `Path()` and `PureWindowsPath()` implemented for Windows file system paths.

```python
In [*]: pathlib.WindowsPath('setup.py')                                     
Out[*]: WindowsPath('setup.py')

```

The same applies to `WindowsPath()` since you are running on a different operating system – so instantiating it will raise an error.

### Properties of concrete paths

Since the concrete path is the subclass of the pure path, you can do everything with concrete paths using the `PurePath()` properties. This means that we can use, for example, the `.with_suffix` property  to add a suffix to a concrete path:

```python
In [*]: p = pathlib.Path('/src/goo/scripts/main')
        p.with_suffix('.py')
Out[*]: PosixPath('/src/goo/scripts/main.py')

```

Or, you can check if a given path is relative to the original path:

```python
In [*]: p = pathlib.Path('/src/goo/scripts/main.py')
        p.is_relative_to('/src')

Out[*]: True

```

Always remember that concrete paths inherit handling operations from the pure paths and add writing operations that do system calls and input/output configurations.

### Methods of concrete path

Each subclass of `Path()` provides the following methods to handle paths and do system calls:

**Path().iterdir()** returns the content of a directory. Let's say we have the following folder that contains the following files:

```
data
	population.json
	density.json
	temperature.yml
	stats.md
	details.txt

```

To return the content of `/data` directory, you can use `.iterdir()` method here:

```python
In [*]: p = pathlib.Path('/data')

        for child in p.iterdir():
        	print(child)

Out[*]: PosixPath('/data/population.json')
         PosixPath('/data/density.json')
         PosixPath('/data/temprature.yml')
         PosixPath('/data/stats.md')
         PosixPath('/data/details.txt')

```

The `.iterdir()` method creates an iterator that lists the files randomly.

**Path().exists()** checks whether the file/directory exists in a current path. Let's use the directory of the previous example (our current directory is `/data`):

```python
In [*]: p = pathlib.Path('density.json').exists()
        p
Out[*]: True

```

The **.exists()** method returns `True` because the given file exists in the `data` directory. The method returns `False` if the file doesn't exist.

```python
In [*]: p = pathlib.Path('aliens.py').exists()
        p
Out[*]: False

```

The same applies to directories, the method returns `True` if the given directory exists and returns `False` if it does not.

**Path().mkdir()** creates a new directory at a given path:

```python
In [*]: p = pathlib.Path('data')
        directory = pathlib.Path('data/secrets')
        directory.exists()
Out[*]: False

In [*]: directory.mkdir(parents = False, exist_ok = False)
        directory.exists()
Out[*]: True

```

According to the official documentation, the `.mkdir()` method takes three arguments. We will focus only at the moment on `parents` and `exist_ok`. 

Both arguments are set to `False` as default. The `parent` raises a FileNotFound error in case of a missing parent, while the `exist_ok` raises a FileExists error if the given directory already exists.

In the example above, you can set the arguments to `True` to ignore the mentioned errors and update the directory.

We can also create a new file at a given path using the `Path().touch()` method:

```python
In [*]: file = pathlib.Path('data/secrets/secret_one.md')
        file.exists()
Out[*]: False

In [*]: file.touch(exist_ok = False)
        file.exists()
Out[*]: True

```

The same logic applies to the `.touch()` method. Here, the `exist_ok` can be set to `True` to ignore the FileExists error and update the file.

**Path().rename()** renames the file/directory at a given path. Let's take an example using our directory `/data`:

```python
In [*]: p = pathlib.Path('density.json')
        n = pathlib.Path('density_2100.json')
        p.rename(n)
Out[*]: PosixPath('density_2100.json')

```

If you assign a non existing file to the method, it raises a FileNotFound error. The same applies to directories.

**Path().read_text()** returns the content of a file in string format:

```python
In [*]: p = pathlib.Path('info.txt')
        p.read_text()

Out[*]: 'some text added'

```

Also, you can use the `**write_text()**` method to write a content in a file:

```python
In [*]: p = pathlib.Path('file.txt')
        p.write_text('we are building an empire')

Out[*]: 'we are building an empire'

```

Note that the **`.write_text()`** method has been added to Python 3.5 and was updated recently in Python 3.10 to have some additional parameters.

## Important note

You might ask yourself why you need to use Windows file system paths – because every package should be compatible with other operating systems, not Windows only. 

You're right if the goal is to make an OS-agnostic path. But, sometimes we can't do this due to some settings that are unique to Windows or Posix systems. That's why those objects are available to help developers deal with those use cases. 

Some packages target problems only present in the Windows ecosystem, and Python accommodates those use cases in this library.

## What next?

Hopefully, this tutorial helps you learn how and why to use Pathlib and how it is useful to handle and manipulate filesystem paths. 

It would be great to play around with what you learned and turn things into a real project. If you have any questions, feel free to connect and hit me up at any time on [LinkedIn](https://www.linkedin.com/in/rochdi-khalid/). 

Also, you can take a look at my channel on [YouTube](https://www.youtube.com/channel/UCF8iZXSsjgc8kE8hITp5rdQ) where I share videos on what I'm learning and building with code.

See you in the next tutorial, and keep moving forward!

### References

There is a lot to know. In this blog post, I covered the basics you need to use Pathlib in your project. 

The official documentation highlights more methods and properties that you can apply to your filesystem paths:

* [Pathlib — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)


