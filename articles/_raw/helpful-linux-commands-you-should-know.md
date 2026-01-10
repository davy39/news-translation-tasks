---
title: Helpful Linux Commands You Should Know
subtitle: ''
author: Rahul
co_authors: []
series: null
date: '2023-07-03T20:36:49.000Z'
originalURL: https://freecodecamp.org/news/helpful-linux-commands-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/gabriel-heinzer-4Mw7nkQDByk-unsplash.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Ever feel like you’ve mastered the basics of Linux and are ready to level
  up your skills? Well, good news – there are many powerful commands that you might
  not know about.

  In this article, I''ll introduce you to some lesser-known Linux commands that w...'
---

Ever feel like you’ve mastered the basics of Linux and are ready to level up your skills? Well, good news – there are many powerful commands that you might not know about.

In this article, I'll introduce you to some lesser-known Linux commands that will help you become a more productive and effective developer.

Whether you’re looking to boost your productivity, tighten system security, or just want to show off your Linux chops to fellow devs, these commands have you covered.

## Chroot: Run Commands With a Different Root Directory

Ever wanted to run commands in a different root directory? The chroot command allows you to do just that.

Chroot, short for “_change root_,” lets you run commands with a different root directory. So if you wanted to test out software in a contained environment or build a minimal Linux system, chroot is your friend.

To use chroot, first you’ll need to set up a directory to act as the new root. Then you run the chroot command, passing it the path to that directory. For example, to chroot into **/home/testdir,** you’d run:

```bash
chroot /home/testdir
```

After that, any commands you run will be relative to / in the `/home/testdir directory`. So you could install packages, run shell scripts, compile programs, and so on. When you’re done, just exit the chroot with `exit`.

Chroot creates an isolated environment, so any changes you make won’t affect the rest of your system. It’s a handy **tool for testing and development or for emergency recovery**. Once you get familiar with chroot, you’ll find all sorts of uses for it.

## Crontab: Schedule Tasks to Run Automatically

Crontab is a handy Linux command that lets you schedule tasks to run automatically at specific times. You’ll wonder how you ever lived without it!

To get started, open the crontab file with `crontab -e`. This will open your default text editor where you can create schedule entries, called [cron jobs](https://www.freecodecamp.org/news/cron-jobs-in-linux/). Each entry has five-time fields – minute, hour, day of month, month, day of week, followed by the command to run.

For example, `0 0 * * * /home/user/daily_script.sh` would run the **daily_script.sh** script at midnight every day. You can also do `30 8 * * 1-5 /home/user/work_script.sh` to run **work_script.sh** at 8:30am every weekday.

Crontab allows a ton of flexibility. You can schedule jobs to run:

* Minutely, hourly, daily, weekly, monthly or yearly
* At a specific minute/hour
* On certain days of the week/month
* With wildcards to run, for example every 3 hours or every Monday and Thursday

The possibilities are endless! You can schedule backup scripts, system maintenance, email reports and so much more.

## Df: Check Disk Space Usage

Ever run out of disk space and wonder where it all went? The `df` command is here to help. df stands for “_disk free_” and shows you exactly how much space is used and available on your Linux system.

### Check Usage for All Mounted Filesystems

To see an overview of disk space usage for all mounted drives and partitions, simply run:

```bash
df -h
```

The `-h` flag formats the output in human-readable format, showing sizes in GB and MB instead of bytes. The output will show:

* Filesystem: The drive or partition name
* Size: Total space
* Used: Space currently in use
* Available: Free space still available
* Use%: Percentage of space used

This gives you a quick snapshot of where you have space and where it's running low.

### Check Usage for a Specific Filesystem

To check space on a specific drive or partition, pass its mount point to df:

`df -h /home`

This will show usage stats just for your /home partition.

Keeping an eye on disk usage with df and related tools is important for any Linux system administrator. No one wants to run out of space unexpectedly.

## Dmesg: View Kernel Messages

Ever wonder what’s happening behind the scenes in your Linux system? The **dmesg** command lets you peek under the hood and view messages from the kernel, the core of your operating system.

When your Linux system boots up, the kernel initializes hardware, loads drivers, starts services, and performs other startup tasks. The **dmesg** command displays the messages that get logged during this process so you can see what’s going on.

To view the kernel messages, just open your terminal and run the dmesg command. You'll see pages and pages of status **updates**, **diagnostics**, **errors**, and more as your system came to life. Skim through to check for any issues, or search for specific keywords like the name of your Wi-Fi adapter or other hardware components.

The **dmesg** output can also provide clues to solving any problems you're having. For example, if your network isn’t working, **check dmesg for error messages related to your Ethernet or wireless card**. You may spot something like “error initializing network device eth0” that points you to a driver issue.

The `dmesg` command is a handy diagnostic tool for any Linux system administrator or power user. It offers an inside look at your Linux system and can help uncover the source of both major malfunctions and minor annoyances. Ps: you can feel like a hacker.

## Grep: Search for Patterns in Files

The grep command allows you to search for patterns in files and text. It’s ideal when you need to find something specific in a sea of data.

Say you have a massive log file full of information, but you only want to see the lines containing the word “error.” Just run:

```bash
grep error log.txt
```

This will print only the lines in log.txt that contain the word “error.”

You can also use grep to search for patterns rather than just words. For example, to find all lines in a file that start with “A” followed by a number, use:

```bash
grep ^A[0-9] log.txt
```

The `^A` anchors the match to the start of the line, and [0-9] matches any digit.

Grep has many more advanced features as well. You can use:

* Regex patterns for complex searches
* `-i` to ignore case
* `-v` to invert the search and show lines that _don’t_ match
* `-c` to just get a count of matches
* `-r` to recursively search all files in a directory

The next time you need to search through files, don’t do it manually—let grep do the work for you.

## Head/Tail: View the First/Last Part of a File

Have you ever needed to quickly check just the first or last few lines of a long file? The head and tail commands are perfect for that.

The `head` command shows you the first 10 lines of a file by default. You can specify how many lines you want to see by using the `-n` flag, like `head -n 5 filename` to show the first 5 lines.

The `tail` command shows you the last 10 lines of a file by default. Again, use the `-n` flag to specify how many lines you want to see, like `tail -n 20 filename` to show the last 20 lines.

Both `head` and `tail` are useful when you want to do a quick check of the start or end of a long file without having to scroll through the entire thing. Some other uses of these commands:

* Checking log files for recent errors or warnings
* Viewing email headers
* Previewing configuration files
* And more!

Give `head` and `tail` a try – you'll be amazed at how much simpler they make tasks you do all the time.

## Ps: List Running Processes

The Ps command allows you to see info about the processes running on your system. This includes programs, commands, and daemons that are currently active. Using Ps is a quick way to get an overview of what your Linux system is doing at the moment and the system resources each process is using.

To see a basic list of running processes, enter:

```bash
ps aux

```

This will show you:

* A: All processes
* U: User
* X: Processes without terminals

The output will contain info like:

* **USER**: The owner of the process
* **PID**: The process ID
* **%CPU**: The CPU usage
* **%MEM**: The memory usage
* **VSZ**: The virtual memory usage
* **TTY**: The terminal associated with the process
* **STAT**: The process state (Running, Sleeping, Zombie, and so on.)
* **START**: The start time of the process
* **TIME**: The CPU time used
* **COMMAND**: The command that started the process

You can also filter the Ps output by:

* Username: `ps aux | grep root`
* Process name: `ps aux | grep cron`
* PID: `ps aux | grep 555`

The Ps command allows you to quickly check in on what your system is doing and ensure there are no runaway or zombie processes hogging resources. For any Linux user, `Ps` is an indispensable tool for system monitoring and troubleshooting.

## Rsync: Sync Files and Folders

As a Linux user, you’ve probably found yourself needing to sync files and folders between locations. Maybe you have files on your desktop you need to transfer to your laptop, or you want to backup your most important folders to an external drive. The rsync command makes syncing and backing up your files a breeze.

Rsync is a fast and versatile file copying tool. It can copy and sync files and folders locally or remotely over SSH. It’s smart enough to only transfer the differences between two locations, saving time and bandwidth.

To use rsync, open your terminal and enter the command:

```bash
rsync [options] source destination
```

* The source is the location of the files you want to copy. This could be a folder on your desktop or a remote server.
* The destination is where you want to copy the files. This could be an external drive mounted on your system or a folder on another server.
* Options allow you to specify items like:
* `-a`: Archive mode which preserves permissions, timestamps, group, owner and symlinks
* `-v`: Verbose output so you can see what’s being copied
* `-z`: Compression to speed up transfers over slow networks
* -h: Human-readable sizes (e.g. 1K, 234M, 2G)

Rsync is a must-have tool for any Linux user. Once you get the hang of it, you’ll be syncing and backing up your files with confidence. 

For broad reading please refer to [RSync Examples – Rsync Options and How to Copy Files Over SSH](https://www.freecodecamp.org/news/rsync-examples-rsync-options-and-how-to-copy-files-over-ssh/).

## The Powerful Pipe Viewer (pv)

Ever wanted to see the progress of data through a pipe? The `pv` command allows you to do just that. It's a pipe viewer that shows you the progress of data through a pipeline.

Say you have a large file that you want to compress, like a video or backup file. Rather than staring at a blinking cursor while gzip does its thing, you can see the progress with pv. Just pipe the data through pv, then to gzip:

```bash
cat mylargefile.mp4 | pv | gzip > mylargefile.mp4.gz
```

`pv` will display the throughput and estimated time remaining as your data is compressed. It's a simple way to get feedback on long-running commands.

You can also use `pv` to see [throughput](https://www.techtarget.com/searchnetworking/definition/throughput#:~:text=Throughput%20is%20a%20measure%20of,and%20network%20systems%20to%20organizations.) and transfer rates of data over the network. For example, when copying a file with `scp` or `rsync`, add `pv` to the pipeline:

```bash
rsync -avz myfiles user@host:/backup | pv
```

Now you'll see the progress of your files copying over the network. pv gives you information like:

* Transferred bytes
* Transfer rate
* ETA
* Progress
* And more

It's a handy tool to give you more insight into what's happening in those long-running terminal commands.

## mtr: Network Diagnostics

Have you ever needed to diagnose network issues but didn’t have access to expensive tools? mtr is a simple but powerful Linux network diagnostic tool. It combines the functionality of the ‘traceroute’ and ‘ping’ programs in a single network diagnostic tool.

`mtr` sends [ICMP](https://www.freecodecamp.org/news/traceroute-and-ping/) echo requests to test the network connectivity between the host `mtr` runs on and a user-specified destination host. It prints the response times and packet loss statistics for each router along the path. This allows you to quickly pinpoint network issues.

To use mtr, open a terminal and enter:

```bash
mtr [domain name or IP address]
```

For example, to trace the route to google.com, enter:

```bash
mtr google.com
```

mtr will start tracing the route and printing results that update in real time. It will show:

* The IP address and hostname of each router along the path
* The percentage of packet loss for each router
* The response times in milliseconds for each router

The output will continue to update until you press Ctrl+C to stop the trace.

mtr is a simple but useful tool for any Linux network administrator. It can save you hours of troubleshooting time when the network goes down by helping you identify the source of latency or packet loss.

## jq: Parse JSON

Ever come across a messy JSON file and wish you had an easy way to parse through it? Meet jq, a command line tool that lets you filter and analyze JSON data with ease.

jq works like a filter. You pass it JSON data on stdin, and it passes the filtered/transformed data to stdout. 

For example, say you have a JSON file called `data.json` with an array of objects. You can filter it to only show objects where `name` is equal to `John` like this:

```bash
cat data.json | jq '.[] | select(.name == "John")'
```

This will print only the John objects to the console.

jq supports many more filters than just `select()`, here are a few more useful ones:

* `.key`: Access a key from objects
* `.[10:]`: Show elements from index 10 onwards
* `.[10:15]`: Show elements from index 10 to 15
* `length`: Print the length of an array
* `map(.)`: Apply a filter to each element of an array
* `group_by(.key)`: Group objects by a key

With jq, you can manipulate JSON data in pretty much any way you want right from the command line. `jq` may seem niche, but JSON is used everywhere on the web, so being able to analyze and transform it efficiently is a useful skill.

## tac: View Config Files in Reverse

Have you ever made a mistake while editing a config file and saved the changes, only to realize you preferred the previous version? The `tac` command allows you to quickly view config files in reverse, so you can see what the file looked like before your edits.

Tac simply prints files in reverse order, line by line. To view a file called `config.txt` in reverse, run:

```bash
tac config.txt
```

This will print the last line of the file first, then the second last line, and so on until it reaches the first line.

* Use tac when you want to **quickly view a log file in reverse** to see the latest entries first.
* Tac can also be useful when **editing config files through the command line**. If you make a mistake, run tac to see what the file looked like before so you can revert your changes.

Tac is a simple but useful utility to have in your Linux toolkit.

## perf: Analyze CPU Performance

If you've ever wondered why your Linux system seems slower over time, the perf command can help you figure it out. Perf is a profiling tool in Linux that can analyze the performance of your CPU to help identify any bottlenecks.

To get started, run the basic `perf list` command to see a list of the events you can monitor. There are hundreds! Some of the most useful ones for profiling CPU performance are:

* `cpu-clock`: Measure the CPU clock cycles
* `task-clock`: Measure the time spent on task execution
* `cache-misses`: Count the number of cache misses
* `branch-misses`: Count the number of branch prediction misses

Pick an event you want to monitor, then run a command like:

```bash
perf stat -e cpu-clock sleep 5
```

This will run the `sleep 5` command and measure the `cpu-clock` event while it's running. Perf will then give you a summary of the stats for that event.

To get more detailed profiling info, use the `perf record` command. For example, to profile a script called `script.sh`, run:

```bash
perf record script.sh
```

This will run the script and record the profiling data. You can then view the results with:

```bash
perf report
```

This gives you an interactive report to analyze the results. You'll see things like:

* The percentage of time spent in each function
* The actual time spent in each function
* The number of calls to each function

Using perf, you have a powerful tool to optimize the performance of your Linux system. Perf really is an amazing (if underused) tool.

## Conclusion

So there you have it, some helpful Linux commands that will make you feel like a power user in no time. 

With these tricks up your sleeve, you'll be zipping around Linux like a pro. The next time you're stuck or frustrated, give one of these a shot. You might just surprise yourself with what you can accomplish.

Linux is an incredibly powerful operating system if you know how to speak its language. Consider this your starter guide to becoming fluent.

I am [Rahul](https://rahul.biz/), 19, Hustler. I am building [Fueler.io](https://fueler.io/register?referral_token=94329340-3e14-4e1e-83fa-bd5e1992) a platform for generalists to create proof of work profile and land opportunities. Let’s connect on [Twitter](https://twitter.com/rahul_wip).  

