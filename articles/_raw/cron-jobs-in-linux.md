---
title: How to Automate Tasks with cron Jobs in Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-11-19T20:34:59.000Z'
originalURL: https://freecodecamp.org/news/cron-jobs-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Cron-jobs-Linux--1-.png
tags:
- name: automation
  slug: automation
- name: Linux
  slug: linux
seo_title: null
seo_desc: "If you're working in IT, you might need to schedule various repetitive\
  \ tasks as part of your automation processes. \nFor example, you could schedule\
  \ a particular job to periodically execute at specific times of the day. This is\
  \ helpful for performing ..."
---

If you're working in IT, you might need to schedule various repetitive tasks as part of your automation processes. 

For example, you could schedule a particular job to periodically execute at specific times of the day. This is helpful for performing daily backups, monthly log archiving, weekly file deletion to create space, and so on.

And if you use Linux as your OS, you'll use something called a cron job to make this happen.

## What is a cron?

Cron is a job scheduling utility present in Unix like systems. The crond daemon enables cron functionality and runs in background. The cron reads the **crontab** (cron tables) for running predefined scripts.

By using a specific syntax, you can configure a cron job to schedule scripts or other commands to run automatically.

For individual users, the cron service checks the following file: **/var/spool/cron**/crontabs 

![Content of /var/spool/cron/crontabs ](https://www.freecodecamp.org/news/content/images/2021/11/image-53.png)
_Contents of /var/spool/cron/crontabs_

### What are cron jobs in Linux?

Any task that you schedule through crons is called a cron job. Cron jobs help us automate our routine tasks, whether they're hourly, daily, monthly, or yearly.

Now, let's see how cron jobs work.

## How to Control Access to crons

In order to use cron jobs, an admin needs to allow cron jobs to be added for users in the '/etc/cron.allow' file. 

If you get a prompt like this, it means you don't have permission to use cron.

![Cron job addition denied for user John.](https://www.freecodecamp.org/news/content/images/2021/11/image-51.png)
_Cron job addition denied for user John._

To allow John to use crons, include his name in '/etc/cron.allow'. This will allow John to create and edit cron jobs.

![Allowing John in file cron.allow](https://www.freecodecamp.org/news/content/images/2021/11/image-52.png)
_Allowing John in file cron.allow_

Users can also be denied access to cron job access by entering their usernames in the file '/etc/cron.d/cron.deny'.

## How to Add cron Jobs in Linux

First, to use cron jobs, you'll need to check the status of the cron service. If cron is not installed, you can easily download it through the package manager. Just use this to check:

```bash
# Check cron service on Linux system
sudo systemctl status cron.service
```

### Cron job syntax

Crontabs use the following flags for adding and listing cron jobs.

* `**crontab -e**`: edits crontab entries to add, delete, or edit cron jobs.
* `**crontab -l**`: list all the cron jobs for the current user.
* `**crontab -u username -l**`: list another user's crons.
* `**crontab -u username -e**`: edit another user's crons.

When you list crons, you'll see something like this:

```bash
# Cron job example
* * * * * sh /path/to/script.sh
```

In the above example,

* * *  * * * represents minute(s) hour(s) day(s) month(s) weekday(s), respectively.

<table>
<thead>
<tr>
<th></th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minutes</td>
<td>0-59</td>
<td>Command would be executed at the specific minute.</td>
</tr>
<tr>
<td>Hours</td>
<td>0-23</td>
<td>Command would be executed at the specific hour.</td>
</tr>
<tr>
<td>Days</td>
<td>1-31</td>
<td>Commands would be executed in these days of the months.</td>
</tr>
<tr>
<td>Months</td>
<td>1-12</td>
<td>The month in which tasks need to be executed.</td>
</tr>
<tr>
<td>Weekdays</td>
<td>0-6</td>
<td>Days of the week where commands would run. Here, 0 is Sunday.</td>
</tr>
</tbody>
</table>

* `sh` represents that the script is a bash script and should be run from `/bin/bash`.
* `/path/to/script.sh` specifies the path to script.

Below is the summary of the cron job syntax.

```bash
*   *   *   *   *  sh /path/to/script/script.sh
|   |   |   |   |              |
|   |   |   |   |      Command or Script to Execute        
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |
|   |   |   | Day of the Week(0-6)
|   |   |   |
|   |   | Month of the Year(1-12)
|   |   |
|   | Day of the Month(1-31)  
|   |
| Hour(0-23)  
|
Min(0-59)
```

## Cron job examples

Below are some examples of scheduling cron jobs.

<table>
<thead>
<tr>
<th>Schedule</th>
<th>Scheduled value</th>
</tr>
</thead>
<tbody>
<tr>
<td>5 0 * 8 *</td>
<td>At 00:05 in August.</td>
</tr>
<tr>
<td>5 4 * * 6</td>
<td>At 04:05 on Saturday.</td>
</tr>
<tr>
<td>0 22 * * 1-5</td>
<td>At 22:00 on every day-of-week from Monday through Friday.</td>
</tr>
</tbody>
</table>

It is okay if you are unable to grasp this all at once. You can practice and generate cron schedules with the [crontab guru](https://crontab.guru/).

### How to set up a cron job

In this section, we will look at an example of how to schedule a simple script with a cron job.

1. Create a script called `date-script.sh` which prints the system date and time and appends it to a file. The script is shown below:

![Script for printing date.](https://www.freecodecamp.org/news/content/images/2021/11/image-67.png)
_Script for printing date._

2.  Make the script executable by giving it execution rights.

```bash
chmod 775 date-script.sh
```

3.  Add the script in the crontab using `crontab -e`.

Here, we have scheduled it to run per minute.

![Adding a cron job in crontab every minute.](https://www.freecodecamp.org/news/content/images/2021/11/image-68.png)
_Adding a cron job in crontab every minute._

4.  Check the output of the file `date-out.txt`. According to the script, the system date should be printed to this file every minute.

![Output of our cron job.](https://www.freecodecamp.org/news/content/images/2021/11/image-65.png)
_Output of our cron job._

## How to Troubleshoot crons

Crons are really helpful, but they might not always work as intended. Fortunately, there are some effective methods you can use to troubleshoot them. 

1. **Check the schedule.**

First, you can try verifying the schedule that's set for the cron. You can do that with the syntax you saw in the above sections.

2. **Check cron logs.**

First you need to check if the cron has run at the intended time or not. You can verify this from the cron logs located at `var/log/cron`. In some distros, logs can be found at `/var/log/syslog`

If there is an entry in these logs at the correct time, it means the cron has run according to the schedule you set.

Below are the logs of our cron job example. Note the first column which shows the timestamp. The path of the script is also mentioned at the end of the line.

![Cron job logs](https://www.freecodecamp.org/news/content/images/2021/11/image-69.png)
_Cron job logs._

**3. Redirect cron output to a file.**

You can redirect a cron's output to a file and check the file for any possible errors.

```bash
# Redirect cron output to a file
* * * * * sh /path/to/script.sh &> log_file.log
```

## Wrapping up

Automating tasks, like with cron jobs, reduces the repetitive work you need to do. It also lets machines auto heal and work around the clock without human intervention. 

Automation in Linux heavily relies on cron jobs, so you should definitely learn crons and experiment with them.

Thank you for reading until the end. Feedback is always welcome.

If you found this article helpful, do share it with your friends.

Let's connect on [Twitter](https://twitter.com/hira_zaira)!


