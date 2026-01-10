---
title: How to Build Your Own Linux Dotfiles Manager from Scratch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T19:16:38.000Z'
originalURL: https://freecodecamp.org/news/build-your-own-dotfiles-manager-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/download--10-.png
tags:
- name: GitHub
  slug: github
- name: Linux
  slug: linux
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: "By Bhupesh Varshney\nAs a new linux ? user, you might realize that there\
  \ are a bunch of configuration files present in your system. These special files\
  \ are called \"dotfiles\". \nIn this tutorial we will learn how to make a dotfiles\
  \ manager and create a ..."
---

By Bhupesh Varshney

As a new linux ? user, you might realize that there are a bunch of configuration files present in your system. These special files are called "dotfiles". 

In this tutorial we will learn how to make a dotfiles manager and create a backup of these files on GitHub.

**What are these .dotfiles you may ask? And why do we need them?**

Dotfiles are usually associated with specific programs installed on your system and are used to customize those programs/software.

For example, if you have [zsh](http://zsh.sourceforge.net/FAQ/) as your default shell your will have a `.zshrc` file in your HOME directory.
Some other examples include:

1. `.vimrc`: this bad boi is used for configuring your VIM Editor.
2. `.bashrc`: available by default, used for changing bash settings.
3. `.bash_aliases`: this file is generally used to store your command aliases.
4. `.gitconfig`: stores configurations related to Git.
5. `.gitmessage`: Used to provide a commit messsage template while using `git commit`.

These **.dotfiles** change over time as you start customizing linux according to your needs.

Creating a back-up of these files is necessary if in some case you mess up something ? and want to go back to a previous stable state. That's where VCS (Version Control Software) comes in. 

Here, we will learn how to automate this task by writing a simple shell script and storing our dotfiles on GitHub.

<figure>
	<img alt="lets do it rock" src="https://media.giphy.com/media/efPA2YD9BFWS30GJ5v/giphy.gif">
	<figcaption>Source : giphy.com</figcaption>
</figure>


## Contents
* [First Steps, Visualizing the script](#heading-first-steps)
* [Getting Dependencies](#heading-getting-dependencies)
* [Start Coding, Module by Module](#heading-start-coding)
* [Jazzing ?? up our script](#heading-jazzing-up-our-script)
* [The End Result](#heading-the-end-result)
* [Summary, Take Aways](#heading-summary)


## First Steps

Oh before we move any further, let's name our script: **dotman**, (dot)file (man)ager.
Do you like it ? ?

Before we write our first line of code, we need to lay out our requirements and design for how our shell script should work.

### Our Requirements

We are going to make dotman simple & easy to use. It should be able to:

1. _Find dotfiles present inside our system ?._
2. _Differentiate between files present in our git repository to those on our system._
3. _Update our dotfiles repo (either push to remote or pull from it)._
4. _Be easy to use (we don't want 5 different arguments in a single script)._

### Lets Visualize
<!---Insert flowchart here -->

![dotman-flowchart](https://drive.google.com/uc?export=view&id=1TQgnRGEcpMF4VKYI8aEIJv9sD6XvWOwv)

## Getting Dependencies

1. `Git`
We need Git, because we may want to go back to a previous version of our dotfile. Plus we are going to store our dotfiles in a VCS Host (GitHub/GitLab/Bitbucket/Gittea).
Don't have Git Installed? Go through the [following](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) guide to learn how to install it according to your system.

2. `Bash`
This is going to be available on your Linux/Unix/MacOS machines by default.
Verify this by checking the version `bash --version`.
It should be something like this. Don't worry about the version too much, as our script will work fine for Bash >=3.

  ```bash
  GNU bash, version 4.4.20(1)-release (i686-pc-linux-gnu)
  Copyright (C) 2016 Free Software Foundation, Inc.
  License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

  This is free software; you are free to change and redistribute it.
  There is NO WARRANTY, to the extent permitted by law.
  ```


## Start Coding

So now we have everything setup. Fire up your favorite editor/IDE.

<figure>
	<img alt="coder chimpanzee" src="https://media.giphy.com/media/QNFhOolVeCzPQ2Mx85/giphy.gif">
	<figcaption>Source: giphy.com</figcaption>
</figure>

We need to declare a [she bang](https://en.wikipedia.org/wiki/Shebang_(Unix)) to indicate we are going to invoke an interpreter for execution.
In the start of the script include this line:

```bash
#!/usr/bin/env bash

```

The command (program) `env` is executed as a new process which then calls the command that was provided as an argument. 

In our case `bash` is automatically started by the env process. That is its `env` responsibility to find where is `bash` on our system and substitute its path in the script.
You could replace `bash` with, for example, `python` or `ruby`.

Now just change file permissions to make our script executable.
```bash
chmod +x dotman.sh
```

We will be using the functional style of programming in this script, that is every piece of the task is going to be inside some _function()_.
Let's follow the flow chart we visualized above and write our first function, `init_check()`.

We are going to rely only on 2 inputs from the user:
1. `DOT_DEST`: the location of repository in your local system.
2. `DOT_REPO`: the url to the remote dotfile repo.

These 2 variables must be present inside your default shell config (`.bashrc` for e.g). We will learn how to do this later in this tutorial.

```bash
init_check() {
	# Check wether its a first time use or not
	if [[ -z ${DOT_REPO} && -z ${DOT_DEST} ]]; then
	    # show first time setup menu
		# initial_setup
	else
		# repo_check
	    # manage
	fi
}
```

The `-z` option is used to check whether a variable is set or not (that is, if its available to our script or not). If it is not, then we are going to invoke our `initial_setup()` function. Otherwise we will check if the repository is cloned and is present inside the `DOT_DEST` folder.

Now let's code the `initial_setup` function:

```bash
initial_setup() {
	echo -e "\n\nFirst time use, Set Up d○tman"
	echo -e "....................................\n"
	read -p "Enter dotfiles repository URL : " -r DOT_REPO

	read -p "Where should I clone $(basename "${DOT_REPO}") (${HOME}/..): " -r DOT_DEST
	DOT_DEST=${DOT_DEST:-$HOME}
	if [[ -d "$HOME/$DOT_DEST" ]]; then
		# clone the repo in the destination directory
		if git -C "${HOME}/${DOT_DEST}" clone "${DOT_REPO}"; then
			add_env "$DOT_REPO" "$DOT_DEST"
			echo -e "\ndotman successfully configured"
			goodbye
		else
			# invalid arguments to exit, Repository Not Found
			echo -e "\n$DOT_REPO Unavailable. Exiting"
			exit 1
		fi
	else
		echo -e "\n$DOT_DEST Not a Valid directory"
		exit 1
	fi
}
```

Pretty basic, right? Now, let's go through this together and understand what's happening.

- The `read` startement is a shell bulitin which is used to take input from the terminal. The `-p` option specifies a prompt before taking an input. 
- The next line after read is called a [Parameter Expansion](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html), If the user doesn't input DOT_DEST then the default value is assigned as `/home/username/` (If DOT_DEST is unset or null, the expansion of $HOME is substituted) Otherwise, the value entered by user is substituted.
- The `-d` inside the if statement checks whether the directory exists (or technically) the directory user provided is actually a valid path in our system or not.
- The `-C` option is used in git to clone the repository to a user-specified path.

Now let's see how to export environment variables in the function `add_env()`.

```bash
add_env() {
	# export environment variables
	echo -e "\nExporting env variables DOT_DEST & DOT_REPO ..."

	current_shell=$(basename "$SHELL")
	if [[ $current_shell == "zsh" ]]; then
		echo "export DOT_REPO=$1" >> "$HOME"/.zshrc
		echo "export DOT_DEST=$2" >> "$HOME"/.zshrc
	elif [[ $current_shell == "bash" ]]; then
		# assume we have a fallback to bash
		echo "export DOT_REPO=$1" >> "$HOME"/.bashrc
		echo "export DOT_DEST=$2" >> "$HOME"/.bashrc
	else
		echo "Couldn't export DOT_REPO and DOT_DEST."
		echo "Consider exporting them manually".
		exit 1
	fi
	echo -e "Configuration for SHELL: $current_shell has been updated."
}
```

Running `echo $SHELL` in your terminal will give you the path for your default shell.
The `basename` command is used to print the "Name" of our SHELL (that is, the actual name without any leading /).

```bash
> echo $SHELL
/usr/bin/zsh
> basename $SHELL
zsh
```

- The `export` is a well-used statement: it lets you export :) environment variables.
- `>>` is called a redirection operator, that is the output of the statement **echo "export DOT_DEST=$2"** is directed (appended) to the end of `zshrc` file.


Now, once the user has completed the first time setup we need to show them the "manager" options.

![manage-menu-flowchart](https://drive.google.com/uc?export=view&id=1TJC7-umrI6JuNAZHFVzGawFz9FQGvBq3)

```bash
manage() {
	while :
	do
		echo -e "\n[1] Show diff"
		echo -e "[2] Push changed dotfiles to remote"
		echo -e "[3] Pull latest changes from remote"
		echo -e "[4] List all dotfiles"
		echo -e "[q/Q] Quit Session"
		# Default choice is [1]
		read -p "What do you want me to do ? [1]: " -n 1 -r USER_INPUT
		# See Parameter Expansion
		USER_INPUT=${USER_INPUT:-1}
		case $USER_INPUT in
			[1]* ) show_diff_check;;
			[2]* ) dot_push;;
			[3]* ) dot_pull;;
			[4]* ) find_dotfiles;;
			[q/Q]* ) exit;;
			* )     printf "\n%s\n" "Invalid Input, Try Again";;
		esac
	done
}
```

- You are already familiar with `read`. The `-n 1` option specifies what length of input is allowed, in our case the user can only input one character amongst 1, 2, 3, 4, q and Q.

Now we have to find all dotfiles in our HOME directory.

```bash
find_dotfiles() {
	printf "\n"
	readarray -t dotfiles < <( find "${HOME}" -maxdepth 1 -name ".*" -type f )
	printf '%s\n' "${dotfiles[@]}"
}
```

The function is divided into 2 parts:
1. `find`
The find command you guessed right, searches for files and directories in our system. Let's understand it part by part.
- The `-type f` options specifies that we only want to search for regular files and not directories, character or block, or device files.
- The `-maxdepth` option tells find to descend at most 1 level (a non-negative integer) levels of directories below the starting-points. You could search sub-directories by replacing 1 with 2, 3 etc.
- `-name` takes a pattern(glob) for searching. For example you can search for all `.py` files: `-name ".py"`.

2. `readarray` (also a synonym for `mapfile`)
reads lines from the standard input into the indexed array variable `dotfiles`.
The `-t` option removes any trailing delimiter (default newline) from each line read.

> Note: If you have an older version of Bash (<4), `readarray` might not be present as a builtin. We can achieve the same functionality by using a `while` loop instead.

```bash
while read -r value; do
    dotfiles+=($value)
done < <( find "${HOME}" -maxdepth 1 -name ".*" -type f )
```


We are now going to make one of the most important functions in our script, `diff_check`.

```bash
diff_check() {

	if [[ -z $1 ]]; then
		declare -ag file_arr
	fi

	# dotfiles in repository
	readarray -t dotfiles_repo < <( find "${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")" -maxdepth 1 -name ".*" -type f )

	# check length here ?
	for (( i=0; i<"${#dotfiles_repo[@]}"; i++))
	do
		dotfile_name=$(basename "${dotfiles_repo[$i]}")
		# compare the HOME version of dotfile to that of repo
		diff=$(diff -u --suppress-common-lines --color=always "${dotfiles_repo[$i]}" "${HOME}/${dotfile_name}")
		if [[ $diff != "" ]]; then
			if [[ $1 == "show" ]]; then
				printf "\n\n%s" "Running diff between ${HOME}/${dotfile_name} and "
				printf "%s\n" "${dotfiles_repo[$i]}"
				printf "%s\n\n" "$diff"
			fi
			file_arr+=("${dotfile_name}")
		fi
	done
	if [[ ${#file_arr} == 0 ]]; then
		echo -e "\n\nNo Changes in dotfiles."
		return
	fi
}

show_diff_check() {
	diff_check "show"
}
```

Our goal here is to find the dotfiles already present in the repository and compare them with the one available in our HOME directory.

- The `declare` keyword lets us create variables. The `-a` option is used to create arrays and `-g` tells declare to make the variables available "globally" inside the script.
- `${#file_arr}` gives us the length of the array.

The next important command is `diff` which is used to compare files line-by-line. For example:
```bash
> echo -e "abc\ndef\nghi" >> fileA.txt
> echo -e "abc\nlmn\nghi" >> fileB.txt
> cat fileA.txt
abc
def
ghi
> cat fileB.txt
abc
lmn
ghi
> diff -u fileA.txt fileB.txt
--- fileA.txt	2020-07-17 16:24:16.138172662 +0530
+++ fileB.txt	2020-07-17 16:24:26.686075270 +0530
@@ -1,3 +1,3 @@
 abc
-def
+lmn
 ghi
```

The `dot_push()` function.

```bash
dot_push() {
	diff_check
	echo -e "\nFollowing dotfiles changed : "
	for file in "${file_arr[@]}"; do
		echo "$file"
		cp "${HOME}/$file" "${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")"
	done

	dot_repo="${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")"
	git -C "$dot_repo" add -A
	
	echo -e "Enter Commit Message (Ctrl + d to save):"
	commit=$(</dev/stdin)

	git -C "$dot_repo" commit -m "$commit"
	
	# Run Git Push
	git -C "$dot_repo" push
}
```

We are overwriting files here by copying them to our dotfile repo using the `cp` command.

And finally the `dot_pull()` function:

```bash
dot_pull() {
	# pull changes (if any) from the host repo
	echo -e "\nPulling dotfiles ..."
	dot_repo="${HOME}/${DOT_DEST}/$(basename "${DOT_REPO}")"
	echo -e "\nPulling changes in $dot_repo\n"
	git -C "$dot_repo" pull origin master
}
```

## Jazzing ?? up our script

Up until now we have achieved what we initially visualized.
But you know what, something's missing ....... ?

**Colors**

<figure>
	<img alt="Colorful cat rainbow waves" src="https://media1.tenor.com/images/83bc087deefaf265255b9a6196915e8a/tenor.gif">
	<figcaption>Source: tenor.com</figcaption>
</figure>

There are a lot of ways to do that, but the popular one is using [escape sequences](https://wiki.bash-hackers.org/scripting/terminalcodes). But we are going to use a tool called `tput` which is a human friendly interface to output colors according to the user's terminal. It is available by default in Linux/MacOS.
Here is a short demo.

To print text in **bold**
```bash
echo "$(tput bold)This$(tput sgr0) word is bold"
```
To change background color.
```bash
echo "$(tput setab 10)This text has green background$(tput sgr0)"
```
To change foreground color
```bash
echo "$(tput setaf 10)This text has blue color$(tput sgr0)"
```
You can also combine attributes.
```bash
echo "$(tput smul)$(tput setaf 10) This text is underlined & green $(tput rmul)$(tput sgr0)"
```

Let me leave this task with you: add your favorite colors in the script.
Read [this](http://linuxcommand.org/lc3_adv_tput.php) guide to learn and explore more about tput.

## The End Result

I hope you are still with me at the point. But it's the end :( and we have a nice looking dotfile manager now.

<figure>
	<img alt="Happy and excited kermit" src="https://media.giphy.com/media/DYH297XiCS2Ck/giphy.gif">
	<figcaption>Source: giphy.com</figcaption>
</figure>

Now just run the script (if you haven't already) to see it in action.

```bash
./dotman.sh
```

You can see my version of [**dotman**](https://github.com/Bhupesh-V/dotman/blob/master/dotman.sh) if you need a reference. Feel free to create any issues if you have any questions about this tutorial or [email](mailto:varshneybhupesh@gmail.com) them to me directly.

[![Bhupesh-V/dotman - GitHub](https://gh-card.dev/repos/Bhupesh-V/dotman.svg?fullname=)](https://github.com/Bhupesh-V/dotman)

I have made it available as a template so you can use it to hack your own version of dotman.

## Summary

Let's summarize some important things we learned in this tutorial.

1. Use `basename /path/to/dir/file/` to get the filename from a path.
2. Use `git -C /path/to/clone/to clone https://repo.url` to clone the repository to a different directory from the current working directory.
3. `echo $SHELL` can be used to determine what is your default shell.
4. Use `find` to search for files and folders in your Linux system.
5. The `diff` command is used to compare 2 files. Similar to `git diff`.
6. Arrays declared inside a function are only accessible inside that function. Use the `-g` option to make them global, for example `declare -ag file_arr`.
7. `tput` can be used to display colorized text on terminal.

If you liked this tutorial, you can read more of my stuff at [my blog](https://bhupesh-v.github.io). You can also connect with me on [Twitter](https://twitter.com/bhupeshimself).

Happy Learning ?



