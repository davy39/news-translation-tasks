---
title: How to Replace Bash with Python as Your Go-To Command Line Language
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T18:33:37.000Z'
originalURL: https://freecodecamp.org/news/python-for-system-administration-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9daf740569d1a4ca390c.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Jillian Rowe

  I have a bit of a love and hate relationship with bash. I spend a lot of time in
  the terminal, and bash is my default "programming language". Sometimes I tell people
  that find, grep and xargs run their infrastructure, and they laugh a...'
---

By Jillian Rowe

I have a bit of a love and hate relationship with bash. I spend a lot of time in the terminal, and bash is my default "programming language". Sometimes I tell people that find, grep and xargs run their infrastructure, and they laugh and laugh until they realize I'm serious. 

Picking up some Python is a perfect choice for system administrators. It's also great for anyone who has to deal with anything in a terminal but doesn't want to use bash, or has needs that are too complex for bash. Once a task goes beyond

```bash
find $(pwd) -name "*.txt" | xargs -I {} echo "do stuff with {}"
```

it's time to break out the Python! 

There are a lot of benefits to using Python as your go to command line language. 

* Python has lots of nice libraries to help out with pretty much anything. That includes dealing with system operations, reading files, listing directories, writing for loops, checking for exit codes, and so on.
* Autocomplete with IDEs. Seriously. Who wants to have to memorize anything?
* Robust testing suite if that's your thing (and if it's not, you should consider making it your thing).
* The iPython console. It's wonderful. It's amazing. **I LOVE IT.**
* Python is available on most systems, and if it's not you can get it with [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
* Robust error checking with try and catch blocks.
* If you work on different operating systems you can use Python libraries that will deal with all that under the hood.
* Even if you have no programming ability Python is an easy language to get started with.

## Let's get Started

To get started, first off you'll need to either have Python installed or install it with Miniconda.

### Check if you have iPython installed

```
which python
which ipython
```

If both of these are successful, you're in business! If you have Python, but not iPython, you will have to install it. You could install it as a system package, but I really recommend that you just install it with Miniconda.

### Install Miniconda

Grab the installer for your OS [here](https://docs.conda.io/en/latest/miniconda.html). I suggest getting the Python3 installation. 

Then it's just a simple installation.

```
bash Miniconda3-latest-Linux-x86_64.sh
```

Follow the prompts and you'll have Miniconda3 installed. Once you have it installed you'll want to run an update, because this is tech and of course you want to run an update. ;-)

```
conda update conda
conda config --add channels conda-forge
conda update -y --all
conda install -y ipython
```

### Troubleshooting 

If you have trouble installing any packages here are some tips.

* Run `conda clean --all` and try again.
* Make sure you're using the correct channel.
* Run `conda update -y --all`
* Try to install as little as possible to your global conda space. Instead create environments for different tasks and projects, which we will get into next.

### Create Environments with Conda

If you've ever used virtualenv, pipenv (is that a thing?), Rbenv, plenv, anyenv or any of the other various envs that have popped up over the years, this will sound very familiar to you. The idea is that different projects should have their own isolated software environments.

```
conda create -n my-project ipython package1 package2 package2
```

*If you're like me and like to have iPython readily availabe make sure you install it to any new environments!*


## Python Libraries for System Administration

Before we get into the examples let's just list some handy packages along with their docs. 

My go to package is the [os](https://docs.python.org/3/library/os.html) package. You can use it to list directories, check if files exist, check if symlinks exist, make directories, run system commands, get and set environmental variables, and more. It's great!

My second package for running system commands that don't exist as handy python libraries is the [subprocess](https://docs.python.org/3/library/subprocess.html) module. 

The [shutil](https://docs.python.org/3/library/shutil.html) has file operations that aren't in the os library.

The [pprint](https://docs.python.org/3/library/pprint.html) library prints out complex data structures with nice indentation.

The [pytest](https://docs.pytest.org/en/latest/) library let's you test your Python code, because let's face it, nothing ever works correctly the first (few) times. 

## How Do I Execute my Code?

Finally! Code!

![Screenshot-2019-12-13-10.33.52](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.33.52.png)

When you're using Python for system administration you can dive straight into the iPython console, or write scripts and then execute them with `python name-of-script.py`. 

If you prefer to write your scripts you have so many choices, and it's truly a matter of personal preference. I use [PyCharm](https://www.jetbrains.com/pycharm/), which is paid, but [Visual Studio Code](https://code.visualstudio.com/) and [Atom](https://atom.io/) are equally excellent free choices. 

I find that it depends on what I'm working on. Sometimes I just open up the iPython console and start typing, and other times I need something more robust with tests and whatnot.

If you're using either the iPython console or any of the editors I listed above, you will have autocomplete. Autocomplete is awesome! With iPython simply start typing your function and press tab to get a list of potential functions you may want.

![Screenshot-2019-12-13-10.49.07](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.49.07.png)

I cannot express how much I love autocomplete. ;-)

## Get Help

You can go to any of the doc pages for any library, but if you know the name of either the library or the function you can bring it up in iPython.

![Screenshot-2019-12-13-10.55.14](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.55.14.png)

![Screenshot-2019-12-13-10.55.55](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-13-10.55.55.png)

You can bring up the help menu in most IDEs and text editors too, but that will be specific to your editor.

## Examples

First you will need to import your packages

```
import os
import subprocess
import shutil
from pprint import pprint
```

Here are some examples of common file and directory operations.

```
# Get your current working directly
# This returns a string
my_cwd = os.getcwd()
print(my_cwd)
```

```
# List the contents of a directory
# This returns a list
dir_list = os.listdir()
for item in dir_list:
    print(item)
```

```
# Get the Absolute Path name of a file (file + current working dir)
os.path.abspath('some-file')
```

```
#Get the basename - returns file
os.path.basename('/path/to/file')
```

```
# Split a directory path - platform independent
os.path.split(os.getcwd())
# Out[17]: ('/Users', 'jillian')
```

```
# Check if a path exists
os.path.exists('/path/on/filesystem')
```

```
# Check if a path is a symlink
os.path.islink()
```

Move files and directories around

```
# Copy a directory
# cp -rf
shutil.copytree('src', 'dest')
```

```
# Copy a file
# cp -rf
shutil.copyfile('file1', 'file2')
```

```
# Move a directory
# mv
shutil.move('src', 'dest')
```

Not everything is going to be available through python libraries, such as installing system libraries, so run a few system commands!

```
# Run an arbitrary system command
command = "echo 'hello'"
result = subprocess.run(command.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#Print the stdout and stderr
print(result.stdout)
print(result.stderr)
```

Write to files!

```
# Write to a file (and create it if it doesn't exist)
# echo "hello" > hello.txt
f= open("hello.txt","w+")
f.write("hello!")
f.close()
```

```
# Append to a file
# echo "hello" >> hello.txt
f = open("hello.txt", "a+")
f.write("hello again!")
f.close()
```



## Write some tests!

Tests mostly work by using a function called assert, which is essentially saying make sure this is true and if not die loudly.

```
def test_system_command():
    """Test the exit code of a system command"""
    command = "echo 'hello'"
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE)
    assert result.returncode == 0
```

Put this function in a file called `test_my_code.py` and run as `pytest test_my_code.py`.

## Wrap Up

That's it for my main tips and tricks for using Python as your go-to bash replacement. The next time you need to write a loop in bash, consider breaking out the iPython console and seeing what you can come up with instead!


