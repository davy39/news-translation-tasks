---
title: How to Learn the Linux Terminal as a Beginner – Tips and Examples
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-11-07T21:25:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-linux-terminal-as-a-beginner
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/10.-Linux-basic-commands---Brief.png
tags:
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "In 2017, I bought a new laptop and switched to Linux. I started off with\
  \ Ubuntu (but jumped to Elementary later), as most people suggested it was beginner\
  \ friendly. \nPeople also suggested that I should get used to using the keyboard\
  \ and terminal over..."
---

In 2017, I bought a new laptop and switched to Linux. I started off with Ubuntu (but jumped to [Elementary](https://elementary.io/) later), as most people suggested it was beginner friendly. 

People also suggested that I should get used to using the keyboard and terminal over a mouse to enjoy the ultimate power of Linux. 

So I started learning various terminal commands and keyboard shortcuts. The fact that I could type pretty fast was a cherry on the cake. 

In this article, I'll walk you through the experiences I had learning to handle file and folder operations in Linux. 

## Prerequisites

Before starting to use terminal, you need to get familiar with two commands. They'll come in handy for whatever operations you're trying to do. 

They are the `cd` and `ls` commands. 

* `**cd**` is a command that lets you navigate to a path or a different folder in terminal
* `**ls**` is a command that lets you list all the files and folders in a directory

## How I Started Learning Some Basic Linux Commands

I love downloading and reading files and books from the internet. But I used to have a bad habit of downloading all the files into the `Downloads` folder. 

One day I was in a hurry to search a document, because I had to give a presentation. But opening and searching through the long list of files in my `Downloads` folder was really frustrating for me as it had 1000+ files. 

I wanted to find a shortcut to identify the file. The only clue I had was that it's a PDF document. So, I planned to copy all the PDF files to another temporary folder. 

### How to copy only PDF files from one folder to another

`cp` is the command to copy the files. Thankfully the Linux terminal supports `regex` almost everywhere. So, my work became quite simple. Here's the code to copy the pdf files into another folder:

```bash
cp <file(s)_to_copy> <destination_folder>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-252.png)
_How to copy only the pdf files from one folder to another?_

From the above screenshot, you may be confused about the `mkdir Temp_PDF_Files` command. You use the `mkdir` command to create a new directory.    
  
Some of you might also be confused with `_./_*.pdf` in the `cp` command. Basically, in the programming world we call this a **Regex**. Regex stands for **Regular Expression,** and we use them to filter items by matching patterns. In our case, it's the files ending with the `.pdf` extension

After running the command, there were fewer than 50 PDF files. I was able to find the file in couple of minutes. 

So as you can see, it's always advisable to categorize your downloaded files. 

Cool, I was done with my presentation. But, I wanted the file to be named properly, so that I could find it more quickly in the future. 

### How to rename a file in Linux

I Googled to learn how to do this, but I was amazed to see the same answer everywhere, which I felt was not right. It was the `mv` command, which I ideally used to move a file/directory from one path to another. 

After digging down further, I found that it was the same `mv` command to rename the file. 

```bash
mv <existing_file_name> <new_file_name>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-253.png)
_How to rename a file in Linux?_

I finished renaming the file. But, I didn't want the temporary folder which I'd created to copy all the PDF files. 

### How to delete a folder completely in Linux (including it's files and sub-folders)

Before getting into this, I copied the renamed file to a safe place which I could remember easily in the future. I was bit nervous as I was about to delete the entire folder. I usually get this feeling whenever I delete anything. 

You can delete files and folders with `rm -rf` command which I'd used many times before. 

```bash
rm -rf <folder_name>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-254.png)
_How to delete a folder completely in Linux?_

But be careful as it's a **dangerous** command. It won't ask for any confirmation before deleting the folder. Recovering a folder deleted with this command is almost impossible. 

## How to Create and Read Files in Linux

People usually get stressed out when they're late, and this is worse for important meetings or online classes. This happened to me – and it led me to a great experience of learning about handling file operations via the terminal. 

It was a bright morning and my online class had already started – and I was delayed by 2 minutes. I wanted to start taking notes, but I had put my notebook and pen somewhere the night before and couldn't remember exactly where. 

The very next thing that came to my mind was to open Google Docs. But that site would take some time to load. 

"Why don't I create a text file on my machine and start taking notes? ", was the question that hit my mind next. 

### How to create a file in Linux

I remembered that one of my friends told me that you can use the `touch` command to create a file instantly. But, I hadn't tried that out yet. So I did:

```bash
touch notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-266.png)
_touch - Linux command to create a file_

But... But... But...  

This command creates a file and does not open this file in edit mode so you can start taking notes. This is where you can use your favorite text editor to open a file. 

**vim** and **nano** are the two well-known text editors available in Linux. 

**vim** is an advanced and powerful text editor you can use to perform **complex file operations** and it's what many Linux System Administrators use.

**nano**, on the other hand, is a simple text editor which you can use to perform **simple file operations**.

I was using nano, so I ran the command `nano notes.txt`. This opens up the text file in edit mode instantly. I started taking notes from the session. 

Finally, I reached the end of class, but I didn't know to save the file. I didn't dare try any commands before getting a backup of my notes. So, I picked up my mobile and took a snap of my notes. 

After a quick Google search, I found that the command was "CTRL + X" to save the file (which will prompt Yes / No to save the file, and hitting "Y" and pressing "Enter" will save it). 

After saving the file, I was curious to check if I had saved it correctly. 

### How to read the contents of a file in Linux

After doing a Google search, I found that there are multiple ways to read a file. `cat`, `head`, and `tail` are a few commands you can use to read a file, and they each have their own use cases. 

* The `**cat**` command displays the entire contents of the file
* The `**head**` command displays the few lines at the top of the file usually used to check if you're about to open the correct file
* And the `**tail**` command displays the bottom few lines of the file usually used to read logs from any process.

Here's an example of the `cat` command:

```bash
cat notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-268.png)
_Reading contents on my notes file with **cat** command_

And here's the output of the `**head**` and `**tail**` commands:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-269.png)
_Output of **head** command displaying top few lines of notes file_

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-270.png)
_Output of **tail** command displaying last few lines of notes file_

### How to read the contents of a file with line numbers in Linux

One day, one of my colleagues asked me, "Hey! Do you know how to display the contents of a file with their line numbers in the terminal? "

I hadn't came across any such commands explicitly available for this. I knew I could write a script that reads the file line by line, and then print them on the console by pre-pending line numbers for each line.

He wanted to explore that option.

We both started to work our way through this problem. Interestingly, in the middle, we found a single and straightforward command. 

Yes – I'm talking about the `nl` command. You use it like this:

```bash
nl notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-271.png)
_`nl` command shows contents of file with line numbers_

That's amazing, isn't it? As you can see from the code above, the `nl` command shows the contents of the file with line numbers.

## Linux Commands I Learned from My Team

My team and I used to sit together and work as a group. We would ask questions about any random technical stuff and tried to explore solutions for any issues that came up. So I wanted to quickly summarize some of the things I learned from my colleagues here. 

Most of them revolve around a lot of file utility commands available in Linux which most people are unaware of. During our development time, we come across multiple scenarios that had to do with handling files. 

My colleague **Naras** asked this question: 

### What's a command to find the properties of a file? 

Well, the `stat` command displays the properties of the file such as name, size, permissions, created by the user, created and updated date and time, and so on. It looks like this: 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-272.png)
_`stat` - Terminal command to display the properties of the file_

### Is there a command to find number of words in a file? 

It was an awesome question from **Udhaya.** 

Yes. But, not just words – you can also count lines and bytes using the `wc` command. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-273.png)
_`wc` command displays number of lines, words and bytes of a file_

The above displayed file has 23 lines and 121 words. Its size is 809 bytes. 

### Can you find the type of the document with a command? 

Few weeks back, I encountered an extraordinary question from **Kumar**:

"Most documents are created with their extension. But recently I found that some PDF documents are not created with .pdf extension. Do we have a command to find the type of document? "

Yes we do. The `file` command displays the type of the document, like this:

```bash
file notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-275.png)
_`file` command displaying the type of `notes.txt` file_

To answer his question, here's the proof showing the type as PDF document before and after removing the extension from the file name:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-274.png)
_`file` command displaying file type without the extension_

### How can I find the occurrences of a word in a file? 

My colleague **Divad** asked if we could find all the lines where a particular word was available in a file.

And I realized that this was possible with the `grep` command.

So what's `grep`? 

`**grep**` stands for **G**lobal search for **R**egular **E**xpression and **P**rint out. It's basically a searching tool which matches with a Regex pattern and prints them. 

```bash
grep -i "Linux" notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-276.png)
_`**grep**` command displays lines containing **Linux** from **notes.txt** file_

The `**-i**` flag indicates to perform **case insensitive** search. To perform **case sensitive** search, **remove** the `-i` flag from the command. 

### What if I want to find all the lines that don't contain a particular word? 

**Raman** raised the question, "What if I want to find all the lines that does not contain the given word?"

It's possible using the same `grep` command but by applying the `-v` argument, like this: 

```bash
grep -v "Linux" notes.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-277.png)
_`**grep -v**` command displays lines not containing the word **Linux** from the **notes.txt** file_

As you can see, by discussing our questions and working things out together, we learned a lot.

# Conclusion

In this article, I've shared my experience using Linux when I was a beginner. I hope you enjoyed reading this article. 

You can connect with me [here](https://www.linkedin.com/in/arunachalamb/). 

You can follow me on [Instagram](https://www.instagram.com/5minslearn/), [Twitter](https://twitter.com/5minslearn), [LinkedIn](https://www.linkedin.com/in/5minslearn/) and [Medium](https://5minslearn.medium.com/). 


