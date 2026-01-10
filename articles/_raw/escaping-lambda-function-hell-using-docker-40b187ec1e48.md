---
title: How to claw your way out of AWS Lambda function hell using the power of Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-17T21:58:27.000Z'
originalURL: https://freecodecamp.org/news/escaping-lambda-function-hell-using-docker-40b187ec1e48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HlfWIN7pNtK3ffZ-ll1cZQ.png
tags:
- name: Alexa
  slug: alexa
- name: AWS
  slug: aws
- name: Docker
  slug: docker
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Liz Rice

  When you’re building Lambda functions, it’s easy to get trapped in an “Invalid ELF
  header” nightmare. The problem is that your binaries are built for the wrong platform.
  Here’s what’s going on, and how you can fix it easily using Docker.

  ...'
---

By Liz Rice

When you’re building Lambda functions, it’s easy to get trapped in an “Invalid ELF header” nightmare. The problem is that your binaries are built for the wrong platform. Here’s what’s going on, and how you can fix it easily using Docker.

When most people get started with Lambda functions, they’ll use the online editor in the console to input their code. This is fine for your first example or two, but pretty soon you’ll want to do something wild and crazy like, y’know, import a library.

Over the past few weekends I’ve been working on [my first Alexa skill for an Amazon Echo](https://hackernoon.com/my-first-alexa-custom-skill-6a198d385c84#.qfxjk23ov) and I’ve reached that point where I want to use some third party code to add some additional functionality.

![Image](https://cdn-media-1.freecodecamp.org/images/vktAeFvMs7ITPSm0PgNVUG6EWPSvDRoG7Xfu)
_Your options for supplying the code for your Lambda function, as seen in the AWS Console_

The online editor simply lets you edit a single file. If you want to refer to other files — including imported libraries — you can upload them in a ZIP file (Amazon call this a [deployment package](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html)). But if you‘re working on a Mac or a Windows computer, there’s a catch.

When you use pip to install Python libraries on your laptop, it gives you binaries (.so files) that are built to run on your machine. But when the Lambda function runs in the AWS cloud it is going to be running on Linux — and binaries built for Mac (these are often called ‘darwin’ builds) or Windows won’t run on Linux (and vice versa).

If you upload the Mac version, you’ll see “invalid ELF header” logs when you try to test your Lambda function.

![Image](https://cdn-media-1.freecodecamp.org/images/q0v1xD6yQw0OfdQsiZVo3Fgzlm1jTvAzNUqA)
_Invalid ELF header indicates it’s the wrong binary format for the platform_

So you’re going to need Linux versions of those library files. But what if you don’t have a Linux box to hand?

You could grab yourself an EC2 instance from Amazon (or a droplet on Digital Ocean, or any Linux VM of your preference) but to my mind that’s quite a performance, and could even cost you a little bit of money (especially if you forget to take the EC2 box down again when you don’t need it).

I think the easiest solution is to use Docker.

### The Docker approach

With [Docker](http://docker.com) you can very easily can run a Linux container locally on your Mac, install the Python libraries within the container so they are automatically in the right Linux format, and zip up the files ready to upload to AWS. You’ll need [Docker for Mac (or Windows)](https://www.docker.com/products/docker) installed first.

Spin up an Ubuntu container that can see the Lambda code you want to upload.

```
docker run -v <directory with your code>:/working -it --rm ubuntu
```

* The `-v`flag makes your code directory available inside the container in a directory called “working”.
* The `-it`flag means you get to interact with this container.
* The `--rm` flag means Docker will remove the container when you’re finished.
* `ubuntu` is the name of an official container image containing, you guessed it, Ubuntu. If this container image isn’t already on your machine, Docker will download it for you.

You should now be inside the container at a shell prompt looking something like this:

```
root@c1996f32a397:/#
```

Install pip and zip:

```
$ apt-get update$ apt-get install python-pip$ apt-get install zip
```

Move into the working directory (you should be able to see your Lambda function code here):

```
$ cd working
```

Use pip to get the library/ies you’re interested in. You can use the -t flag to tell pip to put the libraries here in the current directory, which will be more convenient later as it’s where the AWS deployment package wants them to be:

```
$ pip install -t . <library>
```

If you’re very curious, you can take a look to see what this installs. In my own case I installed the `editdistance` library, which gave me the following additional directories and files.

```
editdistance:__init__.py __init__.pyc _editdistance.h bycython.so def.h
```

```
editdistance-0.3.1.dist-info:DESCRIPTION.rst INSTALLER METADATA RECORD WHEEL metadata.json top_level.txt
```

You can see that bycython.so file? This is the correct, Linux version of the binary that AWS was objecting to when I hit the Invalid ELF header (shown in the error log screenshot above).

Create the ZIP file with your Lambda code (in my case, a single file called lambda_function.py) and the libraries (for me, the two editdistance directories and their contents.

```
$ zip linux-lambda.zip lambda_function.py
```

```
$ zip -r linux-lambda.zip edit*
```

The `-r` flag on zip tells it to recursively add the contents of directories.

Now you have an archive file called linux-lambda.zip which is ready to upload to AWS. And because the directory is mounted from the host (your Mac) into the container, you can simply upload the file into the console.

Back in the terminal type `exit` to quit the container, and it will be as if it never existed, except for the existence of the linux-lambda.zip file, which is still available on the host.

Upload the ZIP file in the console, save it and try running a test. Invalid ELF header error no more!

If this article helps you out, please hit the ? button to make it easier for other people to find it. If you really like it, why not go bananas and share it too?

I’ve written a few other posts about what I’m learning as I write my first Alexa skill, like this one where I [add database storage capabilities to my Lambda function](https://hackernoon.com/my-alexa-skill-with-storage-5adb1d097b88#.d0a1a7xha). If you find them useful, you might be interested in a book I’m writing called [Adventures with Alexa](http://leanpub.com/adventureswithalexa). Pick your own price!

