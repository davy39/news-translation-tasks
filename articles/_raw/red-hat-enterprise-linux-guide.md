---
title: Red Hat Enterprise Linux – Essential RHEL Concepts and Commands to Know
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-03T15:54:20.000Z'
originalURL: https://freecodecamp.org/news/red-hat-enterprise-linux-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/red-hat-enterprise-linux-guide-cover.jpg
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Welcome to the fundamental world of Red Hat Enterprise Linux (RHEL)! In
  order to be an effective Linux user, you''ll need to learn and truly understand
  some essential concepts and commands.

  Let''s dive into the core aspects of RHEL administration to he...'
---

Welcome to the fundamental world of Red Hat Enterprise Linux (RHEL)! In order to be an effective Linux user, you'll need to learn and truly understand some essential concepts and commands.

Let's dive into the core aspects of RHEL administration to help you understand these key topics that form the backbone of day-to-day operations. The only prerequisites are a desire to learn Linux and a willingness to code along at home and complete the exercises at the end.

## Table Of Contents

Here's what we'll cover in this comprehensive guide:

* [What is RHEL?](#heading-what-is-rhel)
    
* [No Need to Set Up Linux Locally](#heading-no-need-to-set-up-linux-locally)
    
* [Understanding Upstream & Downstream](#heading-understanding-upstream-amp-downstream)
    
* [Essential RHEL Command Line Tools and Functions](#heading-essential-rhel-command-line-tools-and-functions)
    
* [How the Linux File System Works](#heading-how-the-linux-file-system-works)
    
* [Text Editors](#heading-text-editors)
    
* [Practical Exercises](#heading-practical-exercises)
    
* [Wrapping Up](#heading-wrapping-up)
    

## What is RHEL?

RHEL is a popular member of the Linux distribution family. It stands out for its strong reliability, stability, and security capabilities.

Created by Red Hat, RHEL is specifically designed for enterprise usage, striking a helpful balance between innovative technologies and a commitment to dependability, extensive support, and seamless compatibility.

RHEL is a solid choice for businesses, organizations, and developers seeking a reliable operating system for high-priority tasks. It offers a robust base for server setups, data centers, cloud computing, and business applications, and is often a go-to option for mission-critical workloads.

## No Need to Set Up Linux Locally

You don't need to set up Linux on your system to follow this guide. Instead, you can practice whatever you learn here on an interactive online platform.

You can visit [this website](https://killercoda.com/playgrounds/scenario/ubuntu) to access a Linux playground where you can execute commands and explore Linux without installation.

## Understanding Upstream & Downstream

### Upstream

Upstream represents the original or source software from which derivatives or distributions are derived. For Red Hat Enterprise Linux (RHEL), Fedora serves as its primary source for updates and features.

RHEL integrates developments from Fedora's open-source platform into its enterprise-level distribution. Changes initiated within Fedora are systematically integrated into RHEL as part of its upstream progression.

Software upstream commonly includes the latest, experimental features and developments driven by the community. It forms the base for related projects, functioning as a testing area for trying out new functions

### Downstream

Downstream refers to distributions or versions derived from the upstream source. These distributions typically incorporate modifications, adjustments, and additional features tailored to specific needs.

CentOS, a widely-used version that comes after RHEL, uses RHEL's code but without its branding and exclusive parts, providing a no-cost alternative.

Likewise, distributions such as Oracle Linux are also built from RHEL's codebase, but they make their changes and packaging adjustments.

Downstream serve different groups of users by taking the main features from the original source and tweaking them to fit specific needs, like stability, support, or particular uses.

## Essential RHEL Command Line Tools and Functions

By learning the fundamental commands I outline below, you can navigate and manage your Linux environment with ease. These commands act as the foundation for a deeper understanding of Linux systems, and they'll empower you to expand your expertise and knowledge further.

### `echo`

The `echo` command is used to show text or variables as output. It's a straightforward yet robust tool often used in scripting and working with command-line interfaces.

##### Syntax:

```bash
echo [OPTIONS] [STRING]
```

##### Examples:

Displaying text:

```bash
echo "Hello, World!"
```

This will print given text as it is on a user's screen.

Displaying variables:

```bash
name="John"
echo "Hello, $name"
```

We can directly declare a variable and assign a value to that variable. We can use `$` in front of the variable name to print it using the `echo` command.

Escape Sequences:

Escape sequences are combinations of characters that are used to represent certain special characters or actions within strings. These sequences typically start with a backslash `\` followed by a specific character or sequence of characters.

When the compiler or interpreter encounters an escape sequence within a string, it interprets it as a special instruction rather than a literal character.

* `\n`: Represents a newline character. When this sequence is encountered within a string, it signifies a line break.
    
* `\t`: Represents a tab character. It's used to create horizontal tabs or spaces within a string.
    
* `\`: Represents a single backslash character. Since the backslash is an escape character itself, using `\` allows you to include a literal backslash in a string.
    
* `\"` : Represents a double quote or a single quote character respectively within a string. These are useful when you want to include quotes within a string that is itself enclosed in quotes.
    

We need to use the `-e` option along with the `echo` command to enable escape sequences. `-e` enables the interpretation of backslash escapes.

##### Examples:

Printing a new sentence on a new line:

```bash
echo -e "This is a new line.\nThis is another line."
```

Now both lines will be on a separate line rather than continuing one after another. You can try using other options from above.

### `whoami`

whoami is used to display the username of the current user who is logged in to the system.

##### Example

```bash
whoami
```

Running `whoami` in a terminal will output the username of the current user. For instance, if you're logged in as "Kedar," it will display `Kedar`. It serves a specific purpose of showing the current user's identity and doesn't have additional options or variations.

### `cat`

The cat command is used primarily to read, create, concatenate, and display the content of files. Its name is derived from "concatenate," which means to link things together.

##### Syntax:

```bash
cat [OPTIONS] [FILE(s)]
```

##### Examples:

Displaying file content:

```bash
cat filename.txt
```

This will display the contents of filename.txt in the terminal.

Concatenating multiple files:

```bash
cat file1.txt file2.txt > combined.txt
```

This code concatenates file1.txt and file2.txt and redirects their content to combined.txt.

Creating or appending to a file:

The output of `cat` can be redirected using `>` (create/overwrite) or `>>` (append) to store the content into a file.

To create a new file and add content to it, try this command:

```bash
cat > newfile.txt
```

This will allow you to type content into the terminal, and pressing Ctrl + D will save it to newfile.txt.

To append content to an existing file, try this:

```bash
cat >> existingfile.txt
```

Similar to the previous command, this allows you to add content to existingfile.txt.

Display line numbers along with the content:

We can show line number along with content using `-n` option with cat.

```bash
cat -n filename.txt
```

Display a dollar sign ($) at the end of each line:

We can show a `$` at end of each line along with content using the `-E` option with `cat` like this:

```bash
cat -E filename.txt
```

### `touch`

The touch command is used to create new, empty files or update the timestamps of existing files without changing their content.

##### Syntax:

```bash
touch [OPTIONS] [FILE(s)]
```

##### Examples:

Creating a new file:

```bash
touch newfile.txt
```

This command creates a new file named newfile.txt. If the file already exists, it updates the timestamp to the current time.

Creating multiple files:

```bash
touch file1.txt file2.txt file3.txt
```

This creates multiple files (file1.txt, file2.txt, file3.txt) simultaneously.

Also, we can create files with changing numbers or letters dynamically. We need to give the range of letters or numbers in curly braces:

```bash
touch file{1..3}.txt
```

This will create `file1.txt`, `file2.txt` and `file3.txt`.

### `ls`

The `ls` command is used to list files and directories in a specified location.

##### Syntax:

```bash
ls [OPTIONS] [DIRECTORY/PATH_OF_DIRECTORY]
```

##### Examples:

List files in the current directory:

```bash
ls
```

This command lists all files and directories in the current working directory.

List files in a specific directory:

```bash
ls /custom/path
```

Replace /custom/path with the actual path to list files and directories in that specific directory.

List hidden files:

```bash
ls -a
ls -a /custom/path
```

The `-a` option shows all files, including hidden ones (those starting with a dot, for example .hiddenfile).

List all details of directory/files:

```bash
ls -l /custom/path
```

This provides a detailed, long listing format that gives more information about directories and files. You will learn more about the details which `ls -l` provides in an upcoming article.

Display Directory/File size:

```bash
ls -h /custom/path
```

Displays file sizes in a human-readable format (e.g., kilobytes, megabytes).

Show modified files first:

```bash
ls -t /custom/path
```

This command sorts files by modification time, showing the newest files first.

We can also use these options together like this:

```bash
ls -la /custom/path
```

This will list all files and directory along with hidden files (-a) and details information of files and directories (-l).

### `date`

The date command is used to display or set the system date and time.

##### Syntax:

```bash
date [OPTIONS]
```

##### Examples:

Displaying the current date and time:

```bash
date
```

This will display the current date and time of your system.

Setting the date and time:

```bash
date MMDDhhmm[[CC]YY][.ss]
```

* MM: Month (01-12)
    
* DD: Day (01-31)
    
* hh: Hour (00-23)
    
* mm: Minute (00-59)
    
* CC: Century (optional, for years earlier than 2000)
    
* YY: Year (optional, 00-99)
    
* .ss: Seconds (optional, 00-61)
    

This command will let you set whatever date and time you want on your system.

Customizing date output:

```bash
date +"%A, %B %d, %Y"
```

Options

* %A = Full weekday name (for example, Sunday)
    
* %B = full month name (for example, January)
    
* %d = day of month (for example, 01)
    
* %Y = year
    

This will display `Saturday, December 16, 2023`. You can find more options for date using the `man date` command.

**Note**: If you want to find in-depth information about any command, use `man your_command` to get more information.

### `cal`

The `cal` command is used to display a calendar for a specified month or year.

##### Syntax:

```bash
cal [OPTIONS] [MONTH] [YEAR]
```

##### Examples:

Displaying the current month's calendar:

```bash
cal
```

This command displays the calendar for the current month.

Displaying a specific month and year:

```bash
cal 12 2023
```

This command displays the calendar for December 2023.

Displaying a specific year:

```bash
cal 2023
```

Displaying Julian days:

"Julian days" refers to a simple way of counting days. Instead of using dates like January 1st or February 15th, Julian days just count the number of days that have passed since a specific starting point. This starting point is called the Julian Day Number (JDN), which began on January 1st, 4713 BC in the Julian calendar.

For example, January 1st, 4713 BC is Julian day 0. Each day after that is counted as Julian day 1, 2, 3, and so on. It's like a continuous count of days without worrying about months or years. It's a handy way for scientists, astronomers, and other professionals to keep track of time because it's a straightforward system of counting days.

```bash
cal -j 12 2023
```

This command displays the calendar for December 2023 along with the corresponding Julian days.

### `mkdir`

You use this command to create new directories, organizing the file system structure efficiently. `mkdir` stands for `Make Directory`.

##### Syntax:

```bash
mkdir [OPTIONS] DIRECTORY_NAME(s)
```

##### Examples:

Creating a single directory:

```bash
mkdir new_directory
```

This command creates a new directory named new\_directory in the current working directory.

Creating multiple directories:

```bash
mkdir dir1 dir2 dir3
```

This command creates multiple directories named dir1, dir2, and dir3 in the current working directory.

We can also make this command little bit more intresting. We can create n numbers of directories if you want them in a sequence of numbers (or letters) – like dir1, dir2, dir3, and so on – with the following syntax.

```bash
mkdir dir{1..5}
```

Now this will create dir1 up to dir5. We can also replace numbers with letters.

Creating nested directories:

```bash
mkdir -p parent/child/grandchild
```

The `-p` option creates nested directories. In this example, it creates a directory structure: parent → child → grandchild.

### `pwd`

The pwd command stands for "print working directory." It displays the current directory path where you're located within the file system.

##### Example:

```bash
pwd
```

### `cd`

The cd command is used to change the current working directory. cd stands for `Change Directory`.

##### Syntax:

```bash
cd [DIRECTORY_PATH]
```

##### Examples:

Changing to a specific directory:

```bash
cd /path/to/directory
```

This command changes the current directory to given path – for example, /path/to/directory.

Moving to a parent directory:

```bash
cd ..
```

`..` refers to the parent directory, so this command moves one level up from the current directory.

Returning to the home directory:

```bash
cd
```

Typing `cd` without any arguments takes you to your home directory.

Switch to the previous directory:

```bash
cd -
```

This will take you to the previous directory that you were working on.

### `cp`

The `cp` command is used to copy files and directories from one location to another.

##### Syntax:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

##### Examples:

Copying a file to another location:

```bash
cp file.txt /path/to/destination/
```

This command copies file.txt to the specified destination directory (/path/to/destination/).

Copying multiple files to a directory:

```bash
cp file1.txt file2.txt file3.txt /path/to/destination/
```

This command copies multiple files (file1.txt, file2.txt, file3.txt) to the specified destination directory.

Copying a directory and its contents:

```bash
cp -r directory1 /path/to/destination/
```

The `-r` (or `-R`) option is used to copy directories recursively. This command copies directory1 and its contents to the specified destination.

### `mv`

The `mv` command is used to move or rename files and directories from one location to another.

##### Syntax:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

##### Examples:

Moving a file to another location:

```bash
mv file.txt /path/to/destination/
```

This command moves file.txt to the specified destination directory (/path/to/destination/). If the destination is a file name, it renames file.txt to that name.

Renaming a file:

```bash
mv old_name.txt new_name.txt
```

This command renames old\_name.txt to new\_name.txt.

Options:

* `-i`: Prompts before overwriting existing files.
    
* `-u`: Moves only when the source is newer than the destination file or when the destination file is missing.
    

### `nl`

The `nl` command is used to add line numbers to files or text that's provided as input. It reads text from a file or standard input and by default numbers all the lines in the output, making it easier to reference and work with specific lines within the content.

##### Syntax:

```bash
nl [OPTIONS] [FILE]
```

##### Examples:

Numbering lines in a file:

```bash
nl filename
```

This command numbers all the lines in the specified file (`filename`) and outputs the result.

Numbering non-empty lines only:

```bash
nl -ba filename
```

This command numbers only non-empty lines (the `-b` option specifies the numbering style, where `a` denotes non-empty lines).

### `head`

The `head` command outputs the beginning section of files or input streams.

##### Syntax:

```bash
head [OPTIONS] [FILE(s)]
```

##### Example:

Displaying the first n lines of a file:

```bash
head -n 10 filename
```

This command displays the first 10 lines of the specified file.

### `tail`

The `tail` command displays the end section of files or input streams.

##### Syntax:

```bash
tail [OPTIONS] [FILE(s)]
```

##### Example:

Displaying the last n lines of a file:

```bash
tail -n 10 filename
```

This command displays the last 10 lines of the specified file.

### `grep`

The `grep` command in Linux is a powerful utility used for searching text patterns within files or input streams. Its primary function is to scan a specified file or standard input line by line and print lines that match a specified pattern.

##### Syntax:

```bash
grep [OPTIONS] PATTERN [FILE(s)]
```

##### Examples:

Searching for a specific pattern in a file:

```bash
grep "pattern" filename
```

This command searches for the word "pattern" in the specified file (`filename`) and displays the lines containing that pattern.

Case-insensitive search in a file:

```bash
grep -i "pattern" filename
```

This command searches for "pattern" in the specified file (`filename`) regardless of whether it's in uppercase or lowercase.

Searching for multiple patterns in a file:

```bash
grep -e "pattern1" -e "pattern2" filename
```

This command searches for both "pattern1" and "pattern2" in the specified file (`filename`) and displays lines containing either of these patterns. You can also use different files for different pattern matching.

### `wc`

The `wc` command stands for "word count," but its functionality extends beyond counting words. It's a versatile command-line utility used to count the number of lines, words, and characters in files or standard input streams.

##### Syntax:

```bash
wc [OPTIONS] [FILE(s)]
```

##### Examples:

Counting lines in a file:

```bash
wc -l filename
```

This command displays the number of lines in the specified file (`filename`).

Counting words in a file:

```bash
wc -w filename
```

This shows the count of words in the specified file.

Counting lines, words, and characters simultaneously:

```bash
wc filename
```

By default, this command displays the count of lines, words, and characters in the specified file.

##### Options and flags for `wc`:

* `-l`: Displays the number of lines.
    
* `-w`: Shows the count of words.
    
* `-m`: Outputs the count of characters.
    
* `-c`: Provides byte counts (equivalent to `-m` in most cases).
    
* `-L`: Displays the length of the longest line.
    
* `-h`: Provides human-readable output (e.g., `1.2K` for 1200).
    

### `cut`

The `cut` command in Linux is used to extract specific sections (columns or portions) of text from files or input streams based on delimiters like characters or fields.

##### Syntax:

```bash
cut [OPTIONS] [FILE(s)]
```

##### Examples:

Extracting specific columns from a file:

```bash
cut -d',' -f 1,3 filename.txt
```

This command extracts the first and third columns from a CSV file (`filename.txt`) where columns are delimited by a comma (`-d','` specifies the delimiter).

Selecting a range of characters from a file:

```bash
cut -c 1-5 filename.txt
```

This command extracts characters 1 to 5 from each line of the specified file (`filename.txt`).

You can always find more options for any command using `man you_command`. This give give proper documentation for that specified command. `man stands for manual.`

Now that you've learned some commonly used RHEL commands, make sure to practice using them. You can start by working through the below exercise.

## How the Linux File System Works

In Linux, the root directory `/` acts as the top level directory in the system hierarchy. It contains various subdirectories, each serving a specific function and storing the necessary system files.

Here is an overview of the primary directories in RHEL and their functions within the root directory:

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Frame-1000004540.svg align="left")

*Linux File System*

Let's go over the function and purpose of each of these directories.

### `/bin` (Binary)

* Function: contains essential executable binaries (commands) accessible to all users.
    
* Purpose: contains fundamental system commands like `ls`, `cp`, `mv`, `rm`, and so on.
    

### `/boot`

* Function: holds files necessary for booting the operating system.
    
* Purpose: contains boot loader files, kernel images, and configuration files required during system boot-up.
    

### `/dev` (Device)

* Function: represents device files.
    
* Purpose: provides access to physical and virtual devices such as hard drives, USB devices, terminals, and more.
    

### `/etc` (Etcetera)

* Function: stores system-wide configuration files.
    
* Purpose: contains configuration files for various applications, services, and system settings.
    

### `/home`

* Function: houses user home directories.
    
* Purpose: each user typically has a subdirectory within `/home` that contains their personal files, settings, and data.
    

### `/lib` and `/lib64`

* Function: contains libraries required by programs at runtime.
    
* Purpose: stores shared library files used by system binaries and applications.
    

### `/mnt` (Mount)

* Function: provides a mount point for temporarily mounting external devices.
    
* Purpose: used for mounting external storage devices such as USB drives, network shares, or additional file systems.
    

### `/opt` (Optional)

* Function: reserved for optional or third-party software.
    
* Purpose: often used to install large, self-contained software packages that don’t conform to the standard Linux file system hierarchy.
    

### `/proc` (Process)

* Function: virtual file system providing information about system processes.
    
* Purpose: offers a way to interactively examine and manipulate the system's internal state.
    

### `/root`

* Function: home directory for the superuser (root).
    
* Purpose: contains the root user's files, settings, and configuration files.
    

### `/sbin` (System Binary)

* Function: stores essential system administration binaries.
    
* Purpose: contains commands crucial for system administration, often requiring administrative privileges.
    

### `/srv` (Service)

* Function: intended for data related to services provided by the system.
    
* Purpose: used for storing data and files used by various services running on the system.
    

### `/tmp` (Temporary)

* Function: directory for temporary files.
    
* Purpose: contains temporary files created by various system processes and users. Files here are typically deleted on system reboot.
    

### `/usr` (Unix System Resources)

* Function: holds user-related programs, libraries, and documentation.
    
* Purpose: contains a vast majority of user-accessible applications, system utilities, libraries, and documentation.
    

### `/var` (Variable)

* Function: stores variable data such as logs, spool files, and temporary files.
    
* Purpose: contains data that varies frequently, including system logs, mail, print queues, and more.
    

## Text Editors

There are various terminal-based text editors, each with its own strengths and functionalities. But Vim stands out among these editors due to its unparalleled versatility and robust feature set.

Vim's strength lies in its powerful modal editing, offering distinct modes for navigation, insertion, and executing commands, enabling swift and efficient text manipulation.

Additionally, Vim's syntax highlighting, support for multiple programming languages, and powerful search and replace capabilities make it a preferred choice for programmers and system administrators alike.

### vim

Vim is a popular text editor among Linux users especially within the command line interface. Vim stands for "Vi IMproved" and is an enhanced version of the classic `vi` editor. It offers extensive features for editing, viewing, and manipulating text or code files.

In this section, we will delve into the world of Vim and how to use it in Linux. My goal is to acquaint you with some practical commands and features within Vim to help you easily manipulate text.

Here's how to open Vim in Linux:

```bash
vim [OPTIONS] [FILE(s)]
```

### Modes in Vim:

In Vim, modes act as different operational states that dictate how you can engage with the editor. The key modes – Normal, Insert, and Visual – play a significant role in your editing process.

You'll start in Normal mode when you open Vim. From there, you can easily navigate, move the cursor, and execute commands. Switching to Insert mode give you a direct means of inputting and altering text. And Visual mode lets you select and manipulate text blocks.

These modes are critical in streamlining various editing tasks, and can help you become more efficient and accurate. Learning how to use and transition between these modes give you versatile control over text editing and makes you much more productive within the Vim environment.

* **Normal Mode:** Default mode for navigation and executing commands.
    
* **Insert Mode:** For typing and editing text.
    
* **Visual Mode:** For selecting and manipulating blocks of text.
    

### Editing in Insert Mode:

Picture yourself opening a document in Vim, eager to insert new information. Simply hit the `i` key, and Vim will know you're ready to type at the current cursor position.

A notification at the bottom will alert you with -- INSERT -- signifying that you are officially in insert mode. Now you can input your desired additions. When you're done, hit the 'Esc' key to return to the default mode where you can then navigate and execute commands.

* Press `i` to enter insert mode and start typing.
    
* Press `Esc` to exit insert mode and return to command mode.
    

### Saving and Exiting Vim:

Imagine that you've made some alterations to your document and now you're ready to save them before exiting Vim. Simply type `:wq` (which represents "write and quit") and hit 'Enter' to securely save your changes and leave Vim.

But what if you've made changes that you don't want to keep? In this situation, enter `:q!` and press 'Enter' to instruct Vim to quit without saving any modifications made since your last save.

By typing `:wq` and `:q!`, depending on your needs, you can confidently add content to your document and ensure that your work is either securely saved or discarded. These actions, paired with your ability to navigate Vim's different modes, make for a seamless and efficient editing experience.

* To save changes and exit, type `:wq` (write and quit) and press Enter.
    
* To exit without saving changes, type `:q!` and press Enter.
    

### How to Edit Commands

Before you enter any command, press `esc` so that you are out of any mode that you were in.

In the editor, commands preceded by a colon (for example, `:w`) are utilized to carry out various actions, such as saving files. To save any modifications you've made, simply type `:w` and hit the 'Enter' key.

Similarly, commands like `dd` are designed for tasks such as erasing a line. To delete a line, make sure you are in the appropriate mode (Normal mode), then type `dd` by pressing the 'd' key twice in rapid succession. If you happen to find yourself in a different mode, simply press the 'esc' key to return to Normal mode.

#### Insert mode example:

* `i`: Enter insert mode before the cursor.
    

```bash
vim example.txt
```

* Use the arrow keys or 'h', 'j', 'k', 'l' to navigate to the end of the first line.
    
* Press 'i' to enter insert mode.
    
* Type your new sentence.
    
* Press 'Esc' to exit insert mode.
    

#### Deleting and changing text:

* `dw`: Delete from the cursor to the end of the word.
    
* `dd`: Delete entire line.
    

```bash
vim example.txt
```

* Move the cursor to the line you want to delete.
    
* Press `dd`.
    

#### Copy, cut, and paste:

* `yy`: Copy (yank) current line.
    
* `yw`: Copy from the cursor to the end of the word.
    
* `p`: Paste after the cursor.
    
* `P`: Paste before the cursor.
    

```bash
vim example.txt
```

* To copy a line: Move the cursor to the line you want to copy and press `yy`.
    
* To cut (delete) a line: Move the cursor to the line you want to cut and press `dd`.
    
* To paste the copied or cut line: Move the cursor to the desired location and press `p` to paste after the cursor or `P` to paste before the cursor.
    

#### Searching:

* `/pattern`: Search forward for "pattern".
    
* `?pattern`: Search backward for "pattern".
    
* `n`: Move to the next search result.
    
* `N`: Move to the previous search result.
    

```c
vim example.txt
```

* To search for a word like "example": Press `/` and then type `example` followed by `Enter`.
    
* To move to the next occurrence: Press `n`.
    
* To move to the previous occurrence: Press `N`.
    

#### Replace:

* `:%s/old/new/g`: Replace "old" with "new" globally in the entire file.
    
* `:s/old/new/g`: Replace "old" with "new" on the current line.
    
* `:s/old/new/gc`: Replace "old" with "new" with confirmation.
    

```bash
vim example.txt
```

* To replace all occurrences of "oldword" with "newword": Type `:%s/oldword/newword/g` and press `Enter`.
    

#### Saving:

* `:w`: Save changes.
    
* `:wq` or `ZZ`: Save changes and quit.
    
* `:x`: Save changes and quit (same as `:wq`).
    

```bash
vim example.txt
```

* To save changes made to the file: Type `:w` and press `Enter`.
    

#### Quitting:

* `:q`: Quit (only if there are no unsaved changes).
    
* `:q!`: Quit without saving changes.
    

```bash
vim example.txt
```

* To exit without saving changes: Type `:q!` and press `Enter`.
    
* To save changes and quit: Type `:wq` or `ZZ` and press `Enter`.
    

### Practical Exercises

Now, to help you practice what you've learned, here are some exercises for you.

Let's say that you've been tasked with organizing and manipulating files and directories on a newly provisioned Red Hat Enterprise Linux system. Use the terminal to complete the following tasks:

#### Essential Command Line Tools & Functions:

* Use `echo` to display your name and a greeting message using variables and escape sequences.
    
* Use `whoami` to print the current user's name.
    
* Create a file named `example.txt` and display its contents using `cat`.
    
* Use `touch` to create three files: `file1.txt`, `file2.txt`, and `file3.txt`.
    
* Experiment with `ls` command variations: `-a`, `-l`, `-h`, `-t`, and combinations.
    
* Use `date` to display the current date and then customize the output to a specific format.
    

#### Linux File System Exploration:

* Use `mkdir` to create directories: `/bin`, `/boot`, `/home`, `/etc`, etc., and explain their functionalities in a document.
    
* Navigate to `/var` and list its contents.
    
* Use `pwd` to print the current directory path.
    

#### Text Editing with Vim:

* Create a file `sample.txt`.
    
* Open `sample.txt` using `vim`.
    
* Practice inserting text, deleting lines, copying and pasting, and saving changes.
    

#### File Operations:

* Copy `sample.txt` to a newly created directory `/tmp` using `cp`.
    
* Move `sample.txt` to the `/var` directory using `mv`.
    
* Remove `sample.txt` from the current directory using `rm`.
    

#### Inspecting File System Information:

* Use `ls -l` to view detailed information of a file in `/usr/bin`.
    
* Explain the output and file permissions in a document.
    

#### Basic Searches and Text Manipulation:

* Use `grep` to search for a specific word in a file.
    
* Perform a search-and-replace operation in `example.txt` using `sed`.
    

#### Advanced File Management:

* Create nested directories `/opt/program/scripts` using `mkdir -p`.
    
* Move `file1.txt` and `file2.txt` into `/opt/program` directory.
    

#### Reflection and Documentation:

* Reflect on your experience with each command in a document, explaining its usage and outcomes.
    
* Document any challenges faced and their solutions.
    
* Summarize the importance of each concept and command learned.
    

Remember, while performing these exercises, ensure you're in the correct directory and double-check commands involving file deletion or modification to prevent unintended actions.

#### Review Questions:

1. What command creates a new directory? Execute it.
    
2. How do you create multiple files at once? Demonstrate this.
    
3. What command moves files from one location to another? Move `file1.txt` and `file3.txt` to `folderA`.
    
4. How can you display the current date and time? Show the output.
    
5. Which command lists the contents of a directory in detail? Use it for the `RHCSA_Practice` directory.
    
6. Explain the purpose of creating nested directories.
    
7. What command renames a file? Rename `file2.txt` to `important_file.txt`.
    
8. How can you display only the hidden files in a directory? Show the hidden files in your current directory.
    

## Wrapping Up

Thank you for exploring the world of Red Hat Enterprise Linux (RHEL) administration with me today. You can dive deeper into the realm of Linux expertise and stay tuned for more insightful content in my future tutorials.

You can follow me on:

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
