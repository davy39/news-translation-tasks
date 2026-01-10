---
title: How to Install the AWS Elastic Beanstalk CLI on a Mac
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2021-01-14T16:34:19.000Z'
originalURL: https://freecodecamp.org/news/install-elastic-bean-cli-on-mac
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5ff9a7b475d5f706921cae6e.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: data
  slug: data
- name: deployment
  slug: deployment
seo_title: null
seo_desc: "Elastic Beanstalk is an orchestration service that allows users on the\
  \ AWS platform to deploy web applications easily. It caters to any setup you might\
  \ need to run an application in the cloud. \nOrchestration simply means that it\
  \ automates the workflo..."
---

Elastic Beanstalk is an orchestration service that allows users on the AWS platform to deploy web applications easily. It caters to any setup you might need to run an application in the cloud. 

Orchestration simply means that it automates the workflow processes that occurs in order to deliver resources as a service on the cloud.

In this tutorial, we will be walking through the simple steps to set Elastic Beanstalk up locally. Setting it up locally means that we will be able to interact directly with AWS from the terminal and push our deployed applications to the cloud via the commands provided by EB .

## Benefits of Elastic Beanstalk

Elastic Beanstalk allows your data to persist after the elastic cloud compute instance is terminated. Data stored on the volume are still accessible.

Also, it helps you avoid component failure by offering high availability and durability. 

## How to Install the Elastic Beanstalk CLI

The Elastic Beanstalk CLI is a command line interface that allows users to create, setup, and manage processes on Elastic Beanstalk.

To install EB in our local environment, we need to check out the open-source [aws-elastic-beanstalk-cli-setup](https://github.com/aws/aws-elastic-beanstalk-cli-setup) project. There we'll find installation guides to help with the process.

### Step 1:

Clone the repository into our local environment. If you don't have a Github account, you can sign up [here](https://www.freecodecamp.org/news/p/8ffef46d-0fe6-4768-8ccd-f8743b0008d1/github.com).

```github
git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git
```

### Step 2:

In this section we have to download zlib and configure it. Zlib is a library used for compression and decompression. EB leverages this feature when it needs to compress and decompress data (strings, structured in-memory content, or files).

```brew
brew install zlib openssl readline
CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib"
```

### Step 3:

Once the installation is done, we'll export and setup paths for the environment variables for zlib. Run the following in the command line:

```
$ export LDFLAGS=$LDFLAGS:-L/usr/local/opt/zlib/lib
$ export CPPFLAGS=$CPPFLAGS:-I/usr/local/opt/zlib/include
$ export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:~/usr/local/opt/zlib/lib/pkgconfig
```

To view if the paths were correctly set, run this command:

```
$ echo $LDFLAGS $CPPFLAGS $PKG_CONFIG_PATH
```

### Step 4: 

Back in our terminal where we pulled the repository, we need to run the bundled installer with the code below:

```
$ ./aws-elastic-beanstalk-cli-setup/scripts/bundled_installer
```

Once the process is complete you'll see an output that looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-09-at-14.33.22.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-09-at-14.33.34.png)

### Step 5:

To complete the installation process, we need to add `eb` and `python` to our environment path as well. We can do this by running this code in the terminal:

```
$ echo 'export PATH="/Users/user/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
$ echo 'export PATH=/Users/user/.pyenv/versions/3.7.2/bin:$PATH' >> /Users/user/.bash_profile && source /Users/user/.bash_profile
```

Once we are done adding the paths, we can now try to initialize an Elastic Beanstalk and see if we get a list of selected regions. Run this in the terminal:

```
$ eb init
```

And you should see the following:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-09-at-14.44.03.png)

Voilà! We have a list of regions that we can choose from and we can add our credentials from an S3 bucket on AWS. We can also run other EB commands such as `eb create`, `eb deploy`, and a lot more.

### References

* [AWS Elastic Beanstalk Developer Guide](https://docs.amazonaws.cn/en_us/elasticbeanstalk/latest/dg/awseb-dg.pdf)
* [Compression with zlib](https://www.zlib.net/)

