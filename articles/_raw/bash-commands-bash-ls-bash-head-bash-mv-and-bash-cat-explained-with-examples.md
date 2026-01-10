---
title: 'Bash Commands: Bash ls, Bash head, Bash mv, and Bash cat Explained with Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T22:27:00.000Z'
originalURL: https://freecodecamp.org/news/bash-commands-bash-ls-bash-head-bash-mv-and-bash-cat-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e1a740569d1a4ca3b5c.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Bash ls

  ls is a command on Unix-like operating systems to list contents of a directory,
  for example folder and file names.

  Usage

  cat [options] [file_names]


  Most used options:


  -a, all files and folders, including ones that are hidden and start with ...'
---

## **Bash ls**

`ls` is a command on Unix-like operating systems to list contents of a directory, for example folder and file names.

### **Usage**

```bash
cat [options] [file_names]
```

Most used options:

* `-a`, all files and folders, including ones that are hidden and start with a `.`
* `-l`, list all files in long format
* `-G`, enable colorized output

### **Example:**

List files in `freeCodeCamp/guide/`

After cloning the main [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) repo, here is the output after running `ls` in the `freeCodeCamp` directory:

```bash
api-server                 docker-compose.yml  public
change_volumes_owner.sh    Dockerfile.tests    README.md
client                     docs                sample.env
CODE_OF_CONDUCT.md         HoF.md              search-indexing
config                     lerna.json          SECURITY.md
CONTRIBUTING.md            LICENSE.md          server
curriculum                 node_modules        tools
docker-compose-shared.yml  package.json        utils
docker-compose.tests.yml   package-lock.json
```

## More bash commands

### Bash Head

`head` is used to print the first ten lines (by default) or any other amount specified of a file or files. `cat`, on the other hand, is used to read a file sequentially and print it to the standard output (that is, it prints out the entire contents of the file). 

That is not always necessary, though – perhaps you just want to check the contents of a file to see if it is the correct one, or check that it is indeed not empty. The `head` command allows you to view the first N lines of a file.

If more than on file is called, then the first ten lines of each file is displayed, unless a specific number of lines are specified. Choosing to display the file header is optional using the option below.

### **Usage**

```bash
head [options] [file_name(s)]
```

Most used options:

* `-n N`, prints out the first N lines of the file(s)
* `-q`, doesn’t print out the file headers
* `-v`, always prints out the file headers

### **Example**

```bash
head file.txt
```

Prints the first ten lines of file.txt (default)

```bash
head -n 7 file.txt
```

Prints the first seven lines of file.txt

```bash
head -q -n 5 file1.txt file2.txt
```

Prints the first 5 lines of file1.txt, followed by the first 5 lines of file2.txt

## **Bash mv**

This bash command moves files and folders.

```text
mv source target
mv source ... directory
```

The first argument is the file you want to move, and the second is the location to move it to.

Commonly used options:

* `-f` to force move them and overwrite files without checking with the user.
* `-i` to prompt confirmation before overwriting files.

## **Bash Cat**

`cat` is one of the most frequently used commands in Unix operating systems.

`cat` is used to read a file sequentially and print it to the standard output. The name comes from the way it can con**cat**enates files.

### **Usage**

```bash
cat [options] [file_names]
```

Most used options:

* `-b`, number non-blank output lines
* `-n`, number all output lines
* `-s`, squeeze multiple adjacent blank lines
* `-v`, display nonprinting characters, except for tabs and the end of line character

### **Example**

Print the content of file.txt:

```bash
cat file.txt
```

Concatenate the content of the two files and display the result in terminal:

```bash
cat file1.txt file2.txt
```

## More info on Bash:

### What is Bash?

[Bash](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/) (short for Bourne Again SHell) is a Unix shell, and a command language interpreter. A shell is simply a macro processor that executes commands. It’s the most widely used shell packaged by default for most Linux distributions, and a successor for the Korn shell (ksh) and the C shell (csh).

Many things that can be done in the GUI of a Linux operating system can be done via the command line. Some examples are:

* Editing files
* Adjusting the volume of the operating system
* Fetching web pages from the internet
* Automating work you do every day

You can read more about bash [here](https://www.gnu.org/software/bash/), via the [GNU Documentation](https://www.gnu.org/software/bash/manual/html_node/index.html#SEC_Contents), and via the [tldp guide](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html#toc10).

## **Using bash on the command line (Linux, OS X)**

You can start using bash on most Linux and OS X operating systems by opening up a terminal. Let’s consider a simple hello world example. Open up your terminal, and write the following line (everything after the $ sign):

```text
zach@marigold:~$ echo "Hello world!"
Hello world!
```

As you can see, we used the echo command to print the string “Hello world!” to the terminal.

## **Writing a bash script**

You can also put all of your bash commands into a .sh file, and run them from the command line. Say you have a bash script with the following contents:

```text
#!/bin/bash
echo "Hello world!"
```

This script only has two lines. The first indicates what interpreter to use to run the file (in this case, bash). The second line is the command we want to use, `echo`, followed by what we want to print, here, "Hello world!"

It’s worth noting that first line of the script starts with `#!`. It is a special directive which Unix treats differently.

#### **Why did we use #!/bin/bash at the beginning of the script file?**

That is because it is a convention to let the interactive shell know what kind of interpreter to run for the program that follows. 

The first line tells the operating system that the file should be executed by the program at `/bin/bash`, the standard location of the Bourne shell on almost every Unix or Unix-like system. By adding `#!/bin/bash` at the beginning of the script, it tells the OS to use the shell at that specific path to execute all the following commands in the script.

`#!` goes by many names such as "hash-bang", "she-bang", "sha-bang", or "crunch-bang". Note that this first line is only considered if the script is an executable.

For example, if `myBashScript.sh` is executable, the command `./myBashScript.sh` will cause the OS will look at the first line figure out which interpreter to use. In this case it would be `#!/bin/bash`.

On the other hand, if you run `bash myBashScript.sh`, then the first line is ignored since the OS already knows to use bash.

To make `myBashScript.sh` executable, simply run `sudo chmod +x myBashScript.sh`. Then run the following command to execute the script:

```text
zach@marigold:~$ ./myBashScript.sh
Hello world!
```

Sometimes the script won’t be executed, and the above command will return an error. It is due to the permissions set on the file. To avoid that, use:

```text
zach@marigold:~$ chmod u+x myBashScript.sh
```

And then execute the script.

