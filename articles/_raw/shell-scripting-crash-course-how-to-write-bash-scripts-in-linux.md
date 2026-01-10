---
title: Shell Scripting for Beginners – How to Write Bash Scripts in Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-31T19:26:38.000Z'
originalURL: https://freecodecamp.org/news/shell-scripting-crash-course-how-to-write-bash-scripts-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/remove-key-val.gif
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: shell script
  slug: shell-script
seo_title: null
seo_desc: 'Shell scripting is an important part of process automation in Linux. Scripting
  helps you write a sequence of commands in a file and then execute them.

  This saves you time because you don''t have to write certain commands again and
  again. You can perfo...'
---

Shell scripting is an important part of process automation in Linux. Scripting helps you write a sequence of commands in a file and then execute them.

This saves you time because you don't have to write certain commands again and again. You can perform daily tasks efficiently and even schedule them for automatic execution.

You can also set certain scripts to execute on startup such as showing a particular message on launching a new session or setting certain environment variables.

The applications and uses of scripting are numerous, so let's dive in.

In this article, you will learn:

1. What is a bash shell?
    
2. What is a bash script and how do you identify it?
    
3. How to create your first bash script and execute it.
    
4. The basic syntax of shell scripting.
    
5. How to see a system's scheduled scripts.
    
6. How to automate scripts by scheduling via cron jobs.
    

The best way to learn is by practicing. I highly encourage you to follow along using [Replit](https://replit.com/~). You can access a running Linux shell within minutes.

## Introduction to the Bash Shell

The Linux command line is provided by a program called the shell. Over the years, the shell program has evolved to cater to various options.

Different users can be configured to use different shells. But most users prefer to stick with the current default shell. The default shell for many Linux distros is the GNU Bourne-Again Shell (bash). Bash succeeded the Bourne shell (`sh`).

When you first launch the shell, it uses a startup script located in the `.bashrc` or `.bash_profile` file which allows you to customize the behavior of the shell.

When a shell is used interactively, it displays a `$` when it is waiting for a command from the user. This is called the shell prompt.

`[username@host ~]$`

If shell is running as root, the prompt is changed to `#`. The superuser shell prompt looks like this:

`[root@host ~]#`

Bash is very powerful as it can simplify certain operations that are hard to accomplish efficiently with a GUI. Remember that most servers do not have a GUI, and it is best to learn to use the powers of a command line interface (CLI).

## What is a Bash Script?

A bash script is a series of commands written in a file. These are read and executed by the bash program. The program executes line by line.

For example, you can navigate to a certain path, create a folder and spawn a process inside it using the command line.

You can do the same sequence of steps by saving the commands in a bash script and running it. You can run the script any number of times.

## How Do You Identify a Bash Script?

### File extension of `.sh`.

By naming conventions, bash scripts end with a `.sh`. However, bash scripts can run perfectly fine without the `sh` extension.

### Scripts start with a bash bang.

Scripts are also identified with a `shebang`. Shebang is a combination of `bash #` and `bang !` followed the the bash shell path. This is the first line of the script. Shebang tells the shell to execute it via bash shell. Shebang is simply an absolute path to the bash interpreter.

Below is an example of the shebang statement.

```bash
#! /bin/bash
```

The path of the bash program can vary. We will see later how to identify it.

### Execution rights

Scripts have execution rights for the user executing them.

An execution right is represented by `x`. In the example below, my user has the `rwx` (read, write, execute) rights for the file `test_script.sh`

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-98.png align="left")

### File colour

Executable scripts appear in a different colour from rest of the files and folders.

In my case, the scripts with execution rights appear as green.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-99.png align="left")

## How to Create Your First Bash Script

Let's create a simple script in bash that outputs `Hello World`.

### Create a file named hello\_world.sh

```bash
touch hello_world.sh
```

### Find the path to your bash shell.

```bash
which bash
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-100.png align="left")

In my case, the path is `/usr/bin/bash` and I will include this in the shebang.

### Write the command.

We will `echo` "hello world" to the console.

Our script will look something like this:

```bash
#! /usr/bin/bash
echo "Hello World"
```

Edit the file `hello_world.sh` using a text editor of your choice and add the above lines in it.

### Provide execution rights to your user.

Modify the file permissions and allow execution of the script by using the command below:

```bash
chmod u+x hello_world.sh
```

`chmod` modifies the existing rights of a file for a particular user. We are adding `+x` to user `u`.

### Run the script.

You can run the script in the following ways:

`./hello_world.sh`

`bash hello_world.sh`.

**Here's the output:**

![Two ways to run scripts](https://www.freecodecamp.org/news/content/images/2022/03/image-160.png align="left")

*Two ways to run scripts*

## The Basic Syntax of Bash Scripting

Just like any other programming language, bash scripting follows a set of rules to create programs understandable by the computer. In this section, we will study the syntax of bash scripting.

### How to define variables

We can define a variable by using the syntax `variable_name=value`. To get the value of the variable, add `$` before the variable.

```bash
#!/bin/bash
# A simple variable example
greeting=Hello
name=Tux
echo $greeting $name
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-104.png align="left")

Tux is also the name of the Linux mascot, the penguin.

![Hi, I am Tux.](https://www.freecodecamp.org/news/content/images/2022/03/image-119.png align="left")

*Hi, I am Tux.*

### Arithmetic Expressions

Below are the operators supported by bash for mathematical calculations:

| Operator | Usage |
| --- | --- |
| + | addition |
| \- | subtraction |
| \* | multiplication |
| / | division |
| \*\* | exponentiation |
| % | modulus |

Let's run a few examples.

![Note the spaces, these are part of the syntax](https://www.freecodecamp.org/news/content/images/2022/03/image-108.png align="left")

*Note the spaces, these are part of the syntax*

Numerical expressions can also be calculated and stored in a variable using the syntax below:

`var=$((expression))`

Let's try an example.

```bash
#!/bin/bash

var=$((3+9))
echo $var
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-109.png align="left")

Fractions are not correctly calculated using the above methods and truncated.

For **decimal calculations**, we can use `bc` command to get the output to a particular number of decimal places. `bc` (Bash Calculator) is a command line calculator that supports calculation up to a certain number of decimal points.

`echo "scale=2;22/7" | bc`

Where `scale` defines the number of decimal places required in the output.

![Getting output to 2 decimal places](https://www.freecodecamp.org/news/content/images/2022/03/image-110.png align="left")

*Getting output to 2 decimal places*

### How to read user input

Sometimes you'll need to gather user input and perform relevant operations.

In bash, we can take user input using the `read` command.

```bash
read variable_name
```

To prompt the user with a custom message, use the `-p` flag.

`read -p "Enter your age" variable_name`

**Example:**

```bash
#!/bin/bash

echo "Enter a numner"
read a

echo "Enter a numner"
read b

var=$((a+b))
echo $var
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-111.png align="left")

### Numeric Comparison logical operators

Comparison is used to check if statements evaluate to `true` or `false`. We can use the below shown operators to compare two statements:

| Operation | Syntax | Explanation |
| --- | --- | --- |
| Equality | num1 -eq num2 | is num1 equal to num2 |
| Greater than equal to | num1 -ge num2 | is num1 greater than equal to num2 |
| Greater than | num1 -gt num2 | is num1 greater than num2 |
| Less than equal to | num1 -le num2 | is num1 less than equal to num2 |
| Less than | num1 -lt num2 | is num1 less than num2 |
| Not Equal to | num1 -ne num2 | is num1 not equal to num2 |

**Syntax**:

```bash
if [ conditions ]
    then
         commands
fi
```

**Example**:

Let's compare two numbers and find their relationship:

```bash
read x
read y

if [ $x -gt $y ]
then
echo X is greater than Y
elif [ $x -lt $y ]
then
echo X is less than Y
elif [ $x -eq $y ]
then
echo X is equal to Y
fi
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-112.png align="left")

### Conditional Statements (Decision Making)

Conditions are expressions that evaluate to a boolean expression (`true` or `false`). To check conditions, we can use `if`, `if-else`, `if-elif-else` and nested conditionals.

The structure of conditional statements is as follows:

* `if...then...fi` statements
    
* `if...then...else...fi` statements
    
* `if..elif..else..fi`
    
* `if..then..else..if..then..fi..fi..` (Nested Conditionals)
    

**Syntax**:

```bash
if [[ condition ]]
then
	statement
elif [[ condition ]]; then
	statement 
else
	do this by default
fi
```

To create meaningful comparisons, we can use AND `-a` and OR `-o` as well.

The below statement translates to: If `a` is greater than 40 and `b` is less than 6.

`if [ $a -gt 40 -a $b -lt 6 ]`

**Example**: Let's find the triangle type by reading the lengths of its sides.

```bash
read a
read b
read c

if [ $a == $b -a $b == $c -a $a == $c ]
then
echo EQUILATERAL

elif [ $a == $b -o $b == $c -o $a == $c ]
then 
echo ISOSCELES
else
echo SCALENE

fi
```

**Output**:

Test case #1

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-113.png align="left")

Test case #2

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-114.png align="left")

Test case #3

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-115.png align="left")

### Looping and skipping

For loops allow you to execute statements a specific number of times.

#### Looping with numbers:

In the example below, the loop will iterate 5 times.

```bash
#!/bin/bash

for i in {1..5}
do
    echo $i
done
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Looping-with-numbers.png align="left")

#### Looping with strings:

We can loop through strings as well.

```bash
#!/bin/bash

for X in cyan magenta yellow  
do
	echo $X
done
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Looping-with-strings.PNG align="left")

#### While loop

While loops check for a condition and loop until the condition remains `true`. We need to provide a counter statement that increments the counter to control loop execution.

In the example below, `(( i += 1 ))` is the counter statement that increments the value of `i`.

**Example:**

```bash
#!/bin/bash
i=1
while [[ $i -le 10 ]] ; do
   echo "$i"
  (( i += 1 ))
done
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-153.png align="left")

### Reading files

Suppose we have a file `sample_file.txt` as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-151.png align="left")

We can read the file line by line and print the output on the screen.

```bash
#!/bin/bash

LINE=1

while read -r CURRENT_LINE
	do
		echo "$LINE: $CURRENT_LINE"
    ((LINE++))
done < "sample_file.txt"
```

**Output:**

![Lines with line number printed](https://www.freecodecamp.org/news/content/images/2022/03/image-152.png align="left")

*Lines with line number printed*

### How to execute commands with back ticks

If you need to include the output of a complex command in your script, you can write the statement inside back ticks.

#### Syntax:

var= commands

**Example**: Suppose we want to get the output of a list of mountpoints with `tmpfs` in their name. We can craft a statement like this: `df -h | grep tmpfs`.

To include it in the bash script, we can enclose it in back ticks.

```bash
#!/bin/bash

var=`df -h | grep tmpfs`
echo $var
```

Output:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-118.png align="left")

### How to get arguments for scripts from the command line

It is possible to give arguments to the script on execution.

`$@` represents the position of the parameters, starting from one.

```bash
#!/bin/bash

for x in $@
do
    echo "Entered arg is $x"
done
```

Run it like this:

`./script arg1 arg2`

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-155.png align="left")

## How to Automate Scripts by Scheduling via cron Jobs

Cron is a job scheduling utility present in Unix like systems. You can schedule jobs to execute daily, weekly, monthly or in a specific time of the day. Automation in Linux heavily relies on cron jobs.

Below is the syntax to schedule crons:

```bash
# Cron job example
* * * * * sh /path/to/script.sh
```

Here, `*` represents minute(s) hour(s) day(s) month(s) weekday(s), respectively.

Below are some examples of scheduling cron jobs.

| SCHEDULE | SCHEDULED VALUE |
| --- | --- |
| 5 0 \* 8 \* | At 00:05 in August. |
| 5 4 \* \* 6 | At 04:05 on Saturday. |
| 0 22 \* \* 1-5 | At 22:00 on every day-of-week from Monday through Friday. |

You can learn about cron in detail in this [blog](https://www.freecodecamp.org/news/cron-jobs-in-linux/) post.

## How to Check Existing Scripts in a System

### Using crontab

`crontab -l` lists the already scheduled scripts for a particular user.

![My scheduled scripts](https://www.freecodecamp.org/news/content/images/2022/03/image-103.png align="left")

*My scheduled scripts*

### Using the find command

The `find` command helps to locate files based on certain patterns. As most of the scripts end with `.sh`, we can use the find script like this:

```bash
find . -type f -name "*.sh"
```

Where,

* `.` represents the current directory. You can change the path accordingly.
    
* `-type f` indicates that the file type we are looking for is a text based file.
    
* `*.sh` tells to match all files ending with `.sh`.
    

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-159.png align="left")

If you are interested to read about the find command in detail, check [my other post](https://www.freecodecamp.org/news/how-to-search-for-files-from-the-linux-command-line/).

## **Wrapping up**

In this tutorial we learned the basics of shell scripting. We looked into examples and syntax which can help us write meaningful programs.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

[Work vector created by macrovector - www.freepik.com](https://www.freepik.com/vectors/work)
