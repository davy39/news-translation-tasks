---
title: How to Manage Linux Processes
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-02-03T00:07:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-linux-processes
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/BB---How-to-manage-processes-in-Linux-.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "We all follow certain processes to achieve our goals. Similarly, every\
  \ system has its own processes to accomplish tasks. \nEvery program or command that\
  \ executes in a Linux system is called a process.\nIn this tutorial, let's explore\
  \ processes and how ..."
---

We all follow certain processes to achieve our goals. Similarly, every system has its own processes to accomplish tasks. 

Every program or command that executes in a Linux system is called a process.

In this tutorial, let's explore processes and how we can manage them in Linux.

# What is a Linux Process?

A process is theoretically called a program in execution. It's basically a task that a system is currently working on. 

Every action you take on the system will result in a new process. For example, opening a browser initiates a process.

In simple words, a process is an instance of a program. The user action is transformed into a command and a new process will be created upon the execution of the command.

Processes work according to a parent-child hierarchy. As the name of the hierarchy implies, a process initiated from a command/program is called the parent process and the produced process of a parent process is called the child process.

## Types of Linux Processes

Processes are classified into 2 types in Linux Distributions:

1. Foreground Processes
2. Background Processes

### Foreground processes

A process that requires the user to start it using a Terminal command or Program is called a foreground process. This means that foreground processes require an input trigger from a user. So every foreground process is manually triggered.

Whenever a process is running in the foreground, the other processes should wait until the current process completes. 

The best example to demonstrate this is via the `sleep` command. The `sleep` command does not allow the user to interact with the terminal until a given number of seconds has passed.

```
sleep 10
```

![Image](https://lh6.googleusercontent.com/Utfn4bYW2zEfEniaJ4QpFXeMIC9Cru1Ex-2OyRKAk2iGo9b7UBhnEspS3STn7HNOHyfSr081dWR1YgIRYGzkAH5UhfceLH3Xt5RofCs-B71b125bJtKi8vKqRC-IsGWM6N2TVpCapSvkdFclakrqq2LY1zfn4kq2ECAaoL8LAApPoM3ZLKeJahVVCF4qQw)
_`sleep` terminal command running on foreground and blocks user input_

We should wait for 10 seconds to access the terminal to run another command.

### Background Processes

A process that runs independently on user input is called a background process. Unlike the foreground processes, we can run multiple processes at the same time in a background process. 

To run a process in the background, place an ampersand (&) at the end of the command that you use to start the process.

Here's a quick example to demonstrate that:

Let's execute the `sleep` command in a background process. It'll run in the background and gives the terminal back to us to run other commands. 

![Image](https://lh4.googleusercontent.com/99ky8Jj_UgNSPmaxJC1k7KOQdfbN-_hhRh31cfAxpyxECAvJFHJjuHSrRF03epnMcUn14p_-w6I4obtRHBLPmIefL8CWT14hYr4_7WI6H3t6lzOCQWJWtajR_MVFfSiP986loc_qhxToalcOttf99gr6pyGJDgGU80hu3sMkJpJLLNu-VgbKugMiNrqnqQ)
_Sample Terminal command for a background process_

```
sleep 10 &
```

Now we can see that the above command runs in the background. It created a process with the `PID` ( 19003 ). So we can run another command simultaneously (`pwd` command). 

## How to Change a Foreground Process to a Background Process

If we start a process in the foreground and would like to place it in the background, we can do it using the `bg` command. Let's see how to change the foreground process to the background.

If a process is running, press the key `CTRL+Z`. This command will suspend the current process.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-372.png)
_Foreground process output_

Then run the `bg` command. It takes a process id as an argument and places the process into the background. If the argument is empty it will place the currently suspended process in the background.

```
bg <process_id>
```

```
bg
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-373.png)
_Foreground process to background process output_

We can see the suspended command ( `sudo apt update`) resuming in background.

# How to List Linux Processes

Before we go over how to do this, you should know why you might need to know a list of processes. Here are a few reasons:

1. To know which process consumes more time.
2. To know which process takes more memory and CPU usage.
3. To know the triggered command for a running process.

To see the processes that are running currently, we can use `ps` (Process Status) command:

```
ps
```

![Image](https://lh3.googleusercontent.com/J0zD8uwiQQbCmoI7kCWQu8MCcoXIfQ9jhpOBnuq3G6xd7qkDxhpRhNGdS7OsLNYuZwllm0eTfsZWNCpr-tlvac38QSduFblom0flRKFg72mmzdN-iEQcv9scx6vu_yjWpRAlIJGays6Y1rfwJpcB3lamtZow6fCIO8gMKTQ8zhcK3XNpA6AKmKcaZcdViA)
_`ps` command showing the list of running processes_

To list the summary of all processes of every logged-in user, we can use the `w` command. This command is the combination of the `who`, `uptime` and `ps -a` commands in Linux.

```
w
```

![Image](https://lh3.googleusercontent.com/ws5Ip77K3CiODb9gfhjRSP5VQgaegkcabCw_rFcREWfHCnBDYlevoosQagnJ4tNfIG__yAV2OIG_BjzPWdTPx9WF4tMF2PfdTixR0aYu-7oo6vFUASwz-ZiHYxamFJU_nHpKNOlRMsVIthGrVMJtTXATBybJBlHBuTld4F-94PXVOlWJhashtH_f9bkDcg)
_`w` command displaying the list of processes of all users_

## How to List the Processes in Tree View

When a program/command runs, it initiates a main process called the parent process. The parent process may depend on some other command/program which will create a child process. 

Here's an example screenshot. 

![Image](https://lh5.googleusercontent.com/Dwa-k101f5l6-Sy3ec8BotbvFggPF4x_UjXdmWpc_YB7AsFb_iKXT-RAjzwA3GhXQI3wa5hdwRBr8hL3eUh4TnyKft_LCPgC0XYDOtLEYeRRBKBGrjZNw3m9irt3XUkaV_7y86LXdRNCssT_Qa1eclk)
_Child processes of the parent (firefox) process_

In the above screenshot, Firefox is the parent process and the other processes are its child processes. 

Let's explore how to list the process in a tree-like structure. 

`pstree` is a Linux command to list the currently running process of all users in a tree-like structure. It is used as a more visual alternative to the `ps` command.

```
pstree
```

![Image](https://lh6.googleusercontent.com/g1gTo5zkfs92067V3p01xndG6c3XOHPjpHJAZTeT1U4wP1DDLopuxPKlgunnTpFDGZwl5BFIbFuaN5oJoRtiSi9xJcKcQihn_hhNth8R_FKpOdjm-VlQzwO7435ZTmCb2GLXILPO444ZwMxz0ZQVRk4)
_`pstree` command listing processes in tree view_

As we can see, the running processes are in tree form. This can be useful to visualize the processes. 

Adding the `-p` flag with the command will display each branch with its process id.

```
pstree -p
```

![Image](https://lh6.googleusercontent.com/elX0V2qolKRLEhXmJuPc549_YdTr80Vz5t60XRucXDrYC3_LFKKRDlB_-kP_uJSYvepwX3n6_XQ8jLvzMohI76-gfhSPDO7eD1KEexqRqEfw49K4E2ZpPodobGvnPA0paKsGXHdxDQ1CjVpfTOSduGI)
_Terminal command displaying the list of processes in tree view with PID_

To list the child process(es) of a particular process, pass the process id as an argument to the `pstree` command. 

```
pstree 3149
```

![Image](https://lh5.googleusercontent.com/L_OeZYxLZCDFFxMqelMfvxXWc2g3eKbKlt4EPV1bPfUBGZ5-STfSv9gxSEOksHsWuufeniSgbGS1-w5DL9uzEuQhWRMb7MOXuKpIn3Nr40wBJbDQkOnswClwvLhY0f9o-fuxV_OUwUqY6gDIc6koa0Q)
_Listing processes in tree view for a particular process_

Earlier, I mentioned that `pstree` command lists the processes from all the users. Passing the username along with the `pstree` command lists only the processes run by the user. 

```
pstree root
```

![Image](https://lh6.googleusercontent.com/zTEM4mk9LXPrkBs3KoJ4Y8eBzuH3blStmsX-bgk1ohMwad8LF6hsAXwzSx_aF1vDqE-SdyhhaBWQrNyeuRNN_QHCrU5SY2TFDjnfB1cKbROiBsEBQmLuiXrGPV53ZKJqUGaM6TIYosf3TT1Uk1py-Po)
_Listing processes in tree view for a particular user_

The above screenshot shows the processes running by the `root` user.

## How to See the Processes of a Particular Program

Many developers may have faced the following scenario:

While working on web development projects, we use browsers like Chrome, Firefox, and others to verify the output with different browsers. 

Some developers will keep on opening the tabs and never close the opened ones. Due to heavy load (if 150+ tabs are opened) browsers will not respond sometimes 😣 leading to the system hanging up. The worst part could be that we won't be able to close the browser 😂. 

Unlike Windows, we don't have Task Manager in Linux to kill the browser. 

This problem can be solved easily in Linux too. Let's see how a Linux expert handles this scenario. 

We know that every program (including the browser) runs as a process. So then you just have to find the process id and kill it.

Let’s see how to find the process id of a command/program you need.

In my system, Chrome is running, Now we can get the PIDs of Chrome by running the following command: 

```
pidof chrome
```

![Image](https://lh3.googleusercontent.com/TUL8R945bAnPXPIZ61Cs6VKzDVLAoRiOGbfZWD-x4u_Jzja72eGqGTXJjC14lhNqa4uF2-jKT3ttOtBJ6f-rbaxqGtEQoI2yPPwanl1ieftWpqMTMFGCn11pfRl2q3s98rehfm0-X7353cJ5KkoM1j2zLxk1CKAM6X-4NMxr_14M0WWdStMC9QhfqbbRrg)
_Terminal command to find process id of chrome_

## How to Kill a Process

There is a command called `kill` in Linux that is used to kill any process by passing the PID ( Process id ) or Process Name. 

Here's the syntax of the `kill` command:

```
kill <pid/processname>
```

Let’s store the PID of Chrome and kill it using the kill command:

```
a=$(pidof chrome)
kill $a
```

![Image](https://lh5.googleusercontent.com/KJP27zaj4YOe4BlWlDQskMlX5ymEUfdcATwD-yyD6LpORFMrV7uTC-E8AlvbmQXpTYNKnytLhAmBgORLpCYCRHeTVnjU9lQfIISxcmFpUJtY13rnnPJT5sdYBz3oPkgr9MnXjqx8F8wdU_bAZTM6EhffPLIA9GhD8lrI3o4ysM-QWZdDLptnyEeadAM9HA)
_Terminal command to kill a process_

The above command will kill the Chrome web browser.

## How to List All Processes

We can see all the Linux processes using the `top` command. It shows real-time updates of each process for all users.

```
top
```

![Image](https://lh6.googleusercontent.com/aDFrfxMKy6yydKH81T7o4S-Z5cV552h0qTq34UH_oUuzj-Oml8CQVlzc2rrBUMNCawgMTxxePSFiI0uCTAHWVUMqaxe__JIGJFCbTn8TRoYWqzoDFxeUfmLHH4tphdUr8DYGyLPx-1vfEP-ZaMzfSlLvcNx-qaGTqxSc9JepmJRmbE5Crd6EI52sOt6JRQ)
_Terminal command displaying all the process in real-time_

Let's understand the heading to understand the underlying data. 

* PID represents a Unique process ID.
* USER represents the Username of the owner of the task.
* PR represents the Priority of the process. Lower the number, higher the priority.
* NI represents a Nice Value of task. A Negative nice value implies higher priority, and a positive Nice value means lower priority.
* VIRT represents the total virtual memory used by the task.
* RES represents RAM Usage of a process in kilobytes.
* SHR represents Shared Memory Size ( Kb ) used by a process.
* S represents the Status of the process:  
- **D:** Uninterruptible sleep  
- **R:** Running  
- **S:** Sleeping  
- **T:** Traced (stopped)  
- **Z:** Zombie
* CPU represents the CPU usage.
* MEM represents the memory usage of task.
* TIME represents the CPU Time.
* COMMAND represents the command that used to start the process.

To display specific user processes we should use the flag `-u`:

```
top -u <username>
```

To look at the processes run by the user `gogosoon`, run the following command:

```
top -u gogosoon
```

![Image](https://lh4.googleusercontent.com/yDIUnMQBUbjn9xRm0E3pv7yITR_0Kx5bZrxL1L1jrm3dBa_9qidIG_uBpllEZp33BetqHcl6un4lRJR-BI8iXQL7QJE0eI4Q-4BI8vDhXT7arh7m5KPXAlCLMJEQoCCX0uL6RgA5elm3rjkDRVVanBk_djmIGtHbD-Xkf63HVjbtmmhdC39cx8AOANBHyg)
_Terminal output of all process started by user `gogosoon`_

You might be confused about seeing the command line output 😆. It'll be a bit hard to debug the processes in real time. 

Here comes the handy GUI tool to handle the processes in Linux. But we have to install this manually. This will work more like task manager in Windows.

```
sudo apt install gnome-system-monitor
```

After installing, just type the name of the software in terminal:

```
gnome-system-monitor
```

This will open all the processes in a new window with a decent GUI:

![Image](https://lh3.googleusercontent.com/_fiYn6xqNuqSEBnqVTkEWhOVPYKoFUxqCkEdE427eWJEsY7WTx1OwuD7p09PG0sZFqrhqdNpYCoM4vhDR7qNB1pe8-uvZVigTUJ0E6BxyU8lgoRzORm4HlihLVsHk1bXgMo0rwHyaGBoajQDb6WQU25NdDRO-U82sYrMg5kxJx7bJrxYKV5yrdlAN2xMcQ)
_Gnome-System-Monitor_

When we right-click on any process it will show the actions like kill, stop, end, and so on.

The Resources tab shows the following utilities:

1. CPU History
2. Memory and Swap History
3. Network History

![Image](https://lh3.googleusercontent.com/0IB18GszrBCvE8827Ml5XuxtXlMZFVbgs5PcZkEN99BIeVjO2BOaULR55yjlbLrYA-i9qURCF4JC8mpxOkZ4_HZLGTDjRUnW5jHdfKzoEBToSYvm95bs5FnQvHYgGYbhPalFXq8D2DONHZGlWM-g1XACnt_FxpN4q7Wr8DUogBsPeuMXXMluIw01z9YbFA)
_CPU History graph_

![Image](https://lh5.googleusercontent.com/xSO96ReEMCKtAgc11bigR6jwThKyjlk0Fz8oZt6hXh5ld4Rt9WWIEtZ-TOrZJ0tQFfx-lnCnH3vJjTBjzfFEulCzcAJgJqeDh8XrK3Ul9iH9Yant3FAbtmWMx5A9FyGcvHydw2nL-JBTGoWcaxUUkoTAiFMgiIuDQW4PVuMYjswFJPERQManNjiADfQ61A)
_Memory and Swap History Graph_

![Image](https://lh4.googleusercontent.com/Vo_9BWdfg0i_mtnCOUennGxyXwqPP_EgaiGwK8Wli7SHAGXQdtbUzu4BElWCvNkpxLLan7y3NGnlaCICiMwnRJ513_gOntCbPwT9w87husha2v6TeDPw-ey0-F_t3wnq7qlN3q9IpScjaR5BDFHRiWd1ywaSSeV_xEl1FC0cotqXcytTl0vYwciJrQc6fQ)
_Network History Graph_

These graphs will be useful to determine the load in your system. 

## Conclusion

In this article, you have learned the basics of processes in Linux. I hope you now understand how they work a bit better. I recommend you all try these commands in your system.  

To learn more about Linux, subscribe to my email newsletter at my [site](https://5minslearn.gogosoon.com/?ref=fcc_linux_processes) and follow me on social media. 


