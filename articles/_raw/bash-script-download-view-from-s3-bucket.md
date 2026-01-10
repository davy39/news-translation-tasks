---
title: How to use a Bash script to manage downloading and viewing files from an AWS
  S3 bucket
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-03-02T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/bash-script-download-view-from-s3-bucket
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/code-coding-computer-data-574077.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: Script
  slug: script
seo_title: null
seo_desc: "As you can read in this article, I recently had some trouble with my email\
  \ server and decided to outsource email administration to Amazon's Simple Email\
  \ Service (SES). \nThe problem with that solution was that I had SES save new messages\
  \ to an S3 buck..."
---

As you can [read in this article](https://www.freecodecamp.org/news/aws-simple-email-service-email-server/), I recently had some trouble with my email server and decided to outsource email administration to Amazon's Simple Email Service (SES). 

The problem with that solution was that I had SES save new messages to an S3 bucket, and using the AWS Management Console to read files within S3 buckets gets stale really fast. 

So I decided to write a Bash script to automate the process of downloading, properly storing, and viewing new messages.

While I wrote this script for use on my Ubuntu Linux desktop, it wouldn't require too much fiddling to make it work on a macOS or Windows 10 system through [Windows SubSystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

Here's the complete script all in one piece. After you take a few moments to look it over, I'll walk you through it one step at a time.

```bash
#!/bin/bash
# Retrieve new messages from S3 and save to tmpemails/ directory:
aws s3 cp \
   --recursive \
   s3://bucket-name/ \
   /home/david/s3-emails/tmpemails/  \
   --profile myaccount

# Set location variables:
tmp_file_location=/home/david/s3-emails/tmpemails/*
base_location=/home/david/s3-emails/emails/

# Create new directory to store today's messages:
today=$(date +"%m_%d_%Y")
[[ -d ${base_location}/"$today" ]] || mkdir ${base_location}/"$today"

# Give the message files readable names:
for FILE in $tmp_file_location
do
   mv $FILE ${base_location}/${today}/email$(rand)
done

# Open new files in Gedit:
for NEWFILE in ${base_location}/${today}/*
do
   gedit $NEWFILE
done
```

We'll begin with the single command to download any messages currently residing in my S3 bucket (by the way, I've changed the names of the bucket and other filesystem and authentication details to protect my privacy). 

```bash
aws s3 cp \
   --recursive \
   s3://bucket-name/ \
   /home/david/s3-emails/tmpemails/  \
   --profile myaccount
```

Of course, this will only work if you've already installed and configured the AWS CLI for your local system. Now's the time [to do that](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) if you haven't already.

The _cp_ command stands for "copy," _--recursive_ tells the CLI to apply the operation even to multiple objects, _s3://bucket-name_ points to my bucket (your bucket name will obviously be different), the /home/david... line is the absolute filesystem address to which I'd like the messages copied, and the _--profile_ argument tells the CLI which of my multiple AWS accounts I'm referring to.

The next section sets two variables that will make it much easier for me to specify filesystem locations through the rest of the script.

```bash
tmp_file_location=/home/david/s3-emails/tmpemails/*
base_location=/home/david/s3-emails/emails/
```

Note how the value of the _tmp_file_location_ variable ends with an asterisk. That's because I want to refer to the _files within_ that directory, rather than the directory itself.

I'll create a new permanent directory within the .../emails/ hierarchy to make it easier for me to find messages later. The name of this new directory will be the current date. 

```bash
today=$(date +"%m_%d_%Y")
[[ -d ${base_location}/"$today" ]] || mkdir ${base_location}/"$today"
```

I first create a new shell variable named _today_ that will be populated by the output of the _date +"%m_%d_%Y"_ command. _date_ itself outputs the full date/timestamp, but what follows (_"%m_%d_%Y"_) edits that output to a simpler and more readable format.

I then test for the existence of a directly using that name - which would indicate that I've already received emails on that day and, therefore, there's no need to recreate the directory. If such a directory does _not_ exist (||), then _mkdir_ will create it for me. If you don't run this test, your command could return annoying error messages.

Since Amazon SES gives ugly and unreadable names to each of the messages it drops into my S3 bucket, I'll now dynamically rename them while, at the same time, moving them over to their new home (in the dated directory I just created). 

```bash
for FILE in $tmp_file_location
do
   mv $FILE ${base_location}/${today}/email$(rand)
done
```

The _for...do...done_ loop will read each of the files in the directory represented by the _$tmp_file_location_ variable and then move it to the directory I just created (represented by the _$base_location_ variable in addition to the current value of $_today_). 

As part of the same operation, I'll give it its new name, the string "_email_" followed by a random number generated by the _rand_ command. You may need to install a random number generator: that'll be _apt install rand_ on Ubuntu. 

An earlier version of the script created names differentiated by shorter, sequential numbers that were incremented using a _count=1...count=$((count+1))_ logic within the _for_ loop. That worked fine as long as I didn't happen to receive more than one batch of messages on the same day. If I did, then the new messages would overwrite older files in that day's directory. 

I guess it's mathematically possible that my _rand_ command could assign overlapping numbers to two files but, given that the default range _rand_ uses is between 1 and 32,576, that's a risk I'm willing to take.

At this point, there should be files in the new directory with names like email3039, email25343, etc. for each of the new messages I was sent. 

Running the _tree_ command on my own system shows me that five messages were saved to my 02_27_2020 directory, and one more to 02_28_2020 (these files were generated using the older version of my script, so they're numbered sequentially). 

There are currently no files in _tmpemails -_ that's because the mv command moves files to their new location, leaving nothing behind.

```bash
$ tree
.
├── emails
│   ├── 02_27_2020
│   │   ├── email1
│   │   ├── email2
│   │   ├── email3
│   │   ├── email4
│   │   ├── email5
│   └── 02_28_2020
│       └── email1
└── tmpemails
```

The final section of the script opens each new message in my favorite desktop text editor (Gedit). It uses a similar _for...do...done_ loop, this time reading the names of each file in the new directory (referenced using the "_today_" command) and then opening the file in Gedit. Note the asterisk I added to the end of the directory location.

```bash
for NEWFILE in ${base_location}/${today}/*
do
   gedit $NEWFILE
done
```

There's still one more thing to do. If I don't clean out my S3 bucket, it'll download all the accumulated messages each time I run the script. That'll make it progressively harder to manage. 

So, after successfully downloading my new messages, I run this short script to delete all the files in the bucket:

```bash
#!/bin/bash
# Delete all existing emails 

aws s3 rm --recursive s3://bucket-name/ --profile myaccount
```


