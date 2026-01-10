---
title: Job Scheduling in RHEL – cron and at Explained with Examples
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-01-29T14:06:44.000Z'
originalURL: https://freecodecamp.org/news/job-scheduling-in-rhel
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Frame-1000004567.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: Efficiently executing tasks at designated times or in response to certain
  events is essential in RHEL's job scheduling process. With the help of various tools
  and utilities, you can easily coordinate and automate job scheduling, eliminating
  the need ...
---

Efficiently executing tasks at designated times or in response to certain events is essential in RHEL's job scheduling process. With the help of various tools and utilities, you can easily coordinate and automate job scheduling, eliminating the need for manual intervention.

Some common tools for job scheduling in RHEL include:

* cron: A time-based job scheduler in Unix-like operating systems. Users can schedule repetitive tasks by creating entries in the crontab file, specifying when and how frequently these tasks should run.
    
* at: The `at` command allows users to schedule one-time jobs to be executed at a specified time in the future.
    

## **Table Of Contents**

Here's what we'll cover in this comprehensive guide:

* [What is a deamon](#heading-what-is-a-deamon)?
    
* [What is systemctl](#heading-what-is-systemctl)?
    
* [Job Scheduling using at](#heading-job-scheduling-using-at)
    
* [Job Scheduling using crontab](#heading-job-scheduling-using-crontab)
    
* [Practical Exercises](#practical-exercise)
    
* [Wrapping Up](#heading-wrapping-up)
    

## What is a Deamon?

In Red Hat Enterprise Linux (RHEL) and other Unix-like operating systems, a "daemon" is a background process that runs continuously, typically providing specific services or functionality to the operating system or applications.

Daemons are frequently responsible for handling various tasks such as hardware management, responding to network requests, executing scheduled tasks, and facilitating communication between different software components.

These tasks do not typically require direct user involvement and are usually carried out without user intervention.

Common examples of daemons include web servers (like Apache or NGINX), database servers (such as MySQL or PostgreSQL), and system services (like cron for scheduling tasks or systemd for managing various system services).

## What is `systemctl`?

Systemctl is an essential in Red Hat Enterprise Linux (RHEL) that empowers users to control and oversee their systemd system and service manager with ease.

This command-line utility offers a seamless way to interface with the systemd init system, which plays a crucial role in booting the operating system, supervising services, and managing a range of system functionalities.

Let's take a closer look at what this tool can do:

### Service Management

#### Starting and Stopping Services

* `systemctl start service_name` initiates a service. Here's an example:
    

```bash
systemctl start atd
```

The above command `systemctl start atd` is used in Linux systems to start the `atd` (which stands for "AT Daemon") service using the `systemctl` utility.

* `systemctl stop service_name` stops a service. Here's an example:
    

```bash
systemctl stop atd
```

By running `systemctl stop atd`, you're instructing the system to stop the `atd` service. As a result, any tasks or jobs scheduled to run using the `at` command will not be processed until the service is started again.

#### Enabling and Disabling Services

* `systemctl enable service_name` sets a service to start automatically at boot. Here's an example:
    

```bash
systemctl enable crond
```

This code sets the `crond` service to start automatically every time the system boots up. This ensures that the cron service, responsible for handling scheduled tasks, is active and ready to execute commands at their specified times without requiring manual intervention after each system restart.

* `systemctl disable service_name` prevents a service from starting automatically at boot. Here's an example:
    

```bash
systemctl disable crond
```

Executing above command removes the configuration that enables the `crond` service to start up automatically when the system boots. As a result, after a system reboot, the `crond` service will not be initiated automatically. Users will need to manually start the service if they want to use cron for scheduling tasks.

### Viewing Service Status

#### Checking Service Status

* `systemctl status service_name` displays the current status and information about a service. Here's an example:
    

```bash
systemctl status crond
```

This provides information about whether the `crond` service is running, stopped, or encountering any issues. It typically includes details such as whether the service is active or inactive, when it was last started or stopped, and any error messages or warnings related to its operation.

#### Displaying All Services

* `systemctl list-units --type=service` lists all active services. Here's an example:
    

```bash
systemctl list-units --type=service
```

This provides a comprehensive list of all services—both active and inactive—managed by `systemd` on the system. This output includes information such as the unit name, load status, active status (whether it's running or not), and description of each service.

All possible Service Management `systemctl` commands are listed below. You can explore all of them on your own to get a better understanding of how they work.

```bash
systemctl start <service>: Starts a service.

systemctl stop <service>: Stops a service.

systemctl restart <service>: Restarts a service.

systemctl reload <service>: Reloads configuration for a service without stopping it.

systemctl status <service>: Displays the current status and information about a service.

systemctl enable <service>: Enables a service to start automatically at boot.

systemctl disable <service>: Disables a service from starting automatically at boot.

systemctl is-active <service>: Checks if a service is currently running.

systemctl is-enabled <service>: Checks if a service is enabled to start at boot.

systemctl is-failed <service>: Checks if a service has failed.
```

### System Control

#### Rebooting and Shutting Down

* `systemctl reboot` restarts the system. Here's an example:
    

```bash
systemctl reboot
```

This shuts down the operating system, terminating all running processes and services, and then starts the boot process again. It brings the system back to a fresh start.

* `systemctl poweroff` shuts down the system. Here's an example:
    

```bash
systemctl poweroff
```

This triggers a series of actions that include shutting down all running services and processes in an orderly manner, saving any necessary data, and finally turning off the system.

#### Suspending and Hibernating

* `systemctl suspend` puts the system into a suspend state. Here's an example:
    

```bash
systemctl suspend
```

This triggers the system to enter a suspended state. In this state, the system effectively halts most operations, including the CPU and other hardware components, to conserve power.

But it keeps the current system state in memory (RAM) so that when it's resumed, the system can quickly return to its previous state without a full boot-up process.

* `systemctl hibernate` puts the system into hibernation. Here's an example:
    

```bash
systemctl hibernate
```

It saves everything you're doing on your computer onto the hard drive and then turns off the computer completely. When you start it up again, it brings back exactly what you were working on before, just like you left it. This is different from "suspend," which keeps your work in a low-power mode but still on.

### Viewing System Information

#### Displaying System Logs

* `journalctl` views system logs and journal entries. Here's an example:
    

```bash
journalctl
```

This displays logs that include system messages, kernel messages, service logs, and other events recorded by the system.

* `journalctl -u <unit>` displays logs for a specific unit. Here's an example:
    

```bash
journalctl -u crond
```

You'll see logs that are related to the `crond` service specifically. This includes messages, errors, or other information logged by the `crond` daemon, which is responsible for managing scheduled tasks using the cron job scheduler.

* `journalctl --since=<time>` shows logs since a specific time. Here's an example:
    

```bash
journalctl --since "2024-01-01 08:00:00"
```

This retrieves and displays system logs that have been generated or recorded after January 1st, 2023, at 8:00 AM. This helps in narrowing down the logs to view system events or messages that occurred from that specific point in time onwards, and can help you troubleshoot or analyze recent system activity.

These commands of `systemctl` are enough to start a job scheduling module. You can always explore more `systemctl` commands on your own.

## Job Scheduling using `at`

The `at` command is used for scheduling one-time tasks or commands that will be carried out at a designated future time. This feature is especially useful for automating tasks that you need to complete at a later time, so you don't have to remember to do them later.

To use `at`, you'll need to check the following:

* Ensure that the `at` daemon (`atd`) is running for `at` jobs to execute. You can use the `systemctl` command to check if `atd` is running or not. If not, you can use `systemctl` to start it (and you can see how to do that in the `systemctl` section in this tutorial).
    
* Permissions might be restricted for non-admin users to use `at`, depending on system settings.
    
* If you are manipulating something in a file, make sure you have Read-Write-Execute permission for that same file.
    

### Syntax of `at`

```bash
at <time>
```

### Examples of using the `at` command

Let's see how the `at` command works in practice with a few examples.

First, here's how you can display a message at a specific time:

```bash
at 15:35
```

Now let's say you need to give commands that will run automatically at 15:35:

```bash
echo "Meeting in 30 minutes" >> sample.txt
```

Press `Ctrl + D` to finish entering commands and schedule the job. This will print "Meeting in 30 minutes" in sample.txt file at 15:35.

Perhaps you have a script named `backup.sh` and you want it to run at 2 AM. Here's how you'd do that:

```bash
at -f backup.sh 02:00
```

This code schedules the `backup.sh` script to run at 2:00 AM. The contents of `backup.sh` will be executed as if they were entered directly into the terminal at that specified time.

You can also use the following command to see a list of pending `at` jobs:

```bash
atq
```

The `atq` command helps you view and manage a list of pending `at` jobs, letting you easily reference scheduled tasks and their execution times.

Here's some example output of the `atq` command:

```bash
10	Wed Jan 12 03:00:00 2023 a user123
```

* The first column represents the job number.
    
* The second column shows the scheduled execution time for each job.
    
* The third column denotes the priority level ('a' in this case).
    
* 'a' is usually the default priority level assigned to `at` jobs, and as the letters move down the alphabet ('b', 'c', 'd', and so forth), the priority level decreases.
    
* The fourth column displays the username of the user who scheduled the job (if available).
    

Here's how to remove a job:

```bash
atrm 10
```

The above code removes the `at` job with the ID number '3' from the `at` queue, preventing it from being executed at its scheduled time. You can find job Id by `atq` command. Job Id is in the 1st column of output.

### `at.allow` and `at.deny`

The files `at.allow` and `at.deny` are used to control access for users to schedule jobs using `at`. These files are typically located in `/etc/` in RHEL.

The `at.allow` file specifies the list of users who are allowed to use the `at` command to schedule jobs. If this file exists, only users listed in it can schedule `at` jobs. If the file doesn't exist, it behaves as if it's empty, allowing all users unless restricted by `at.deny`.

The `at.deny` file specifies the list of users who are denied access to use the `at` command. If this file exists and a user is listed in it, that user won't be able to schedule `at` jobs.

If both `at.allow` and `at.deny` exist, `at.allow` takes precedence. If neither exists, only the superuser (root) can schedule `at` jobs.

#### Managing Access – summary and recap

* If `at.allow` exists, only users listed in this file can use `at`.
    
* If `at.deny` exists but `at.allow` doesn't, users not listed in `at.deny` can use `at`.
    
* If neither `at.allow` nor `at.deny` exists, by default, only the superuser (root) can use `at`.
    

#### Examples of `at.allow` and `at.deny`

Let's say you want to restrict `at` usage to specific users:

Create an `at.allow` file like this:

```bash
sudo touch /etc/at.allow 
sudo echo "user1" >> /etc/at.allow 
sudo echo "user2" >> /etc/at.allow
```

This allows only `user1` and `user2` to schedule `at` jobs.

Alternatively, you can use the `at.deny` file like this:

```bash
sudo touch /etc/at.deny 
sudo echo "user3" >> /etc/at.deny
```

This denies access to `user3` from using `at`.

## Job Scheduling using `crontab`

Cron enables users to schedule recurring actions and commands at specific times, dates, or intervals. This powerful job scheduler stores all the scheduling information in a special file known as the `crontab`.

### Basic crontab Commands

* `crontab -e`: Opens the user's crontab file in an editor to add or edit cron jobs.
    
* `crontab -l`: Lists the user's cron jobs.
    
* `crontab -r`: Removes all of the user's cron jobs.
    

A few things to note about `crontab`:

* Each user can have their own `crontab`.
    
* The `cron` daemon (`crond`) must be running for cron jobs to execute.
    
* Always use absolute paths for scripts and commands within cron jobs.
    

### `crontab` Format

The `crontab` file has five fields followed by the command/script to execute. Here's what it looks like:

```bash
* * * * * command_to_execute
- - - - -
| | | | |
| | | | +----- Day of the week (0 - 7) (Sunday is 0 or 7)
| | | +------- Month (1 - 12)
| | +--------- Day of the month (1 - 31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
```

If you forgot the `crontab` format, you can always run `cat /etc/crontab` command and it will display the format for you.

### Examples of using `crontab`

#### Run a script every hour

```bash
crontab -e
```

The above command will open the editor with Vim or any other you have set. In that editor, you'll write the job based on the `crontab` format just like below:

```bash
0 * * * * /path/to/script.sh
```

* `0` represents the minute field. In this case, it's set to `0`, indicating that the cron job will trigger when the minute is `0`, that is at the start of every hour.
    
* `*` (asterisks) indicates that every possible value for that field is valid. So, `* * * * *` means the job will run every minute of every hour, every day, every month, and every day of the week.
    
* Putting it all together, the cron job `0 * * * * /path/to/script.sh` signifies that the script located at `/path/to/script.sh` will run every hour at the beginning of the hour (when the minute is `0`).
    

#### Run a command at specific times

First run `crontab -e`.

```bash
0 15 * * * command_to_execute
```

* `0` represents the minute field. In this case, it's set to `0`, indicating that the cron job will trigger at the start of the hour.
    
* `15` represents the hour field. It's set to `15`, which means the job will execute at the 15th hour of the day, that is 3:00 PM.
    

`* * * * *`: The asterisks denote every possible value for each time-related field. In this case:

* `*` for the day of the month and month fields means it applies to every day of every month.
    
* `*` for the day of the week field means it applies to every day of the week.
    
* `command_to_execute` represents the command or script that will be executed at the specified time. This placeholder should be replaced with the actual command you want to run at 3:00 PM daily.
    

#### Run a job every weekday

First do `crontab -e`.

```bash
0 9 * * 1-5 command_to_execute
```

The above code specifies that the `command_to_execute` will run at 9:00 AM from Monday to Friday. This cron job is useful for scheduling tasks that should only run on weekdays at a specific time.

#### Run a job every 15 minutes

First do `crontab -e`.

```bash
*/15 * * * * command_to_execute
```

This specifies that the `command_to_execute` will run at 0, 15, 30, and 45 minutes past every hour, every day, every month, and every day of the week. This cron job is useful for scheduling tasks that need to be executed in regular intervals, in this case, every 15 minutes.

### `cron.allow` and `cron.deny`

You use these `cron.allow` and `cron.deny` files to control which users are allowed to use the `cron` service to schedule periodic jobs. These files are typically located in `/etc/` in RHEL.

The `cron.allow` file specifies the list of users who are allowed to use the `cron` service to schedule jobs using `crontab`. If this file exists, only users listed in it can create `crontab` entries. If the file doesn't exist, it behaves as if it's empty, allowing all users unless restricted by `cron.deny`.

The `cron.deny` file specifies the list of users who are denied access to use the `cron` service. If this file exists and a user is listed in it, that user won't be able to create `crontab` entries. If both `cron.allow` and `cron.deny` exist, `cron.allow` takes precedence. If neither exists, only the superuser (root) can create `crontab` entries.

#### Managing access – summary

* If `cron.allow` exists, only users listed in this file can create `crontab` entries.
    
* If `cron.deny` exists but `cron.allow` doesn't, users not listed in `cron.deny` can create `crontab` entries.
    
* If neither `cron.allow` nor `cron.deny` exist, by default, only the superuser (root) can create `crontab` entries.
    

#### Example of using `cron.allow` and `cron.deny`

Let's say you want to restrict `cron` usage to specific users.

Create a `cron.allow` file:

```bash
sudo touch /etc/cron.allow 
sudo echo "user1" >> /etc/cron.allow 
sudo echo "user2" >> /etc/cron.allow
```

This allows only `user1` and `user2` to create `crontab` entries.

Alternatively, you can use the `cron.deny` file:

```bash
sudo touch /etc/cron.deny 
sudo echo "user3" >> /etc/cron.deny
```

This denies access to `user3` from creating `crontab` entries.

## Practical Exercises

### Service Management with `systemctl`

* Review the current status of system services using `systemctl`.
    
* Start, stop, enable, or disable a service to understand their functionalities.
    

### Scheduling Immediate Tasks with `at`

* Use `at` command to schedule an immediate one-time task (e.g., echoing a message, executing a command) to run a few minutes from the current time.
    
* Check the access permissions for `at` commands by understanding the functionality of `at.allow` and `at.deny`.
    

### Setting Up `at.allow` and `at.deny`

* Create an `at.allow` file to specify users allowed to use `at` by listing usernames (if it doesn't exist).
    
* Create an `at.deny` file to restrict users from using `at` by listing usernames (if necessary).
    
* Try to schedule an `at` task using different user accounts to observe the effect of these files.
    

### Recurring Tasks with `cron`

* Open the crontab using `crontab -e`.
    
* Schedule a task to run at a specific time each day or week using `cron`.
    
* Check the access permissions for `cron` commands by understanding the functionality of `cron.allow` and `cron.deny`.
    

### Setting Up `cron.allow` and `cron.deny`

* Create a `cron.allow` file to specify users allowed to use `cron` by listing usernames (if it doesn't exist).
    
* Create a `cron.deny` file to restrict users from using `cron` by listing usernames (if necessary).
    
* Attempt to modify or create a `cron` job using different user accounts to observe the effect of these files.
    

### Observation and Verification

* Monitor the status of scheduled tasks using respective commands (`atq`, `crontab -l`).
    
* Validate access restrictions and permissions for `at` and `cron` commands by observing user attempts and access denials.
    

### Cleanup and Exploration

* Remove or modify the access control files (`at.allow`, `at.deny`, `cron.allow`, `cron.deny`) and observe the changes in command accessibility.
    
* Explore additional `systemctl`, `at`, and `cron` commands to deepen your understanding of task scheduling and access control.
    

## **Wrapping Up**

Thank you for exploring the world of Red Hat Enterprise Linux (RHEL) administration with me today. You can dive deeper into the realm of Linux expertise and stay tuned for more insightful content in my future tutorials.

You can follow me on:

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
