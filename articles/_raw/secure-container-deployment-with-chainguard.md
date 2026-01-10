---
title: How to Secure Your Container Deployments with Chainguard
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2024-04-05T01:46:19.000Z'
originalURL: https://freecodecamp.org/news/secure-container-deployment-with-chainguard
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/frank-mckenna-tjX_sniNzgQ-unsplash.jpg
tags:
- name: containers
  slug: containers
- name: Security
  slug: security
- name: virtualization
  slug: virtualization
seo_title: null
seo_desc: "You don't need to convince me that containers are absolutely the best thing\
  \ to come out of the virtualization revolution. I use containers of one flavor or\
  \ another just about every day. \nBut the beauty of template-it-once-and-deploy-it-everywhere\
  \ com..."
---

You don't need to convince me that containers are absolutely the best thing to come out of the virtualization revolution. I use containers of one flavor or another just about every day. 

But the beauty of template-it-once-and-deploy-it-everywhere comes with a cost: what if a single layer within that template contains a security vulnerability? And if there was a vulnerability tucked away down there, how would you even know? 

In this article, I'll to show you how to use Chainguard (and Docker Scout) to manage security for all your images.

You can watch the video version of this article here:

%[https://youtu.be/ao1Upn3Yooo]

When you build your software infrastructure on a physical server the traditional way, you'll manually acquire and install each element of the stack one piece at a time. The odds are that you'll be pulling the latest version of everything straight from the official source. And you'll at the very least be thinking about each layer. 

But most modern containers are built from complicated templates. It's easy to just copy and paste the code and fire it up. It's very possible that you might not even be _aware_ of all the software that's powering your application. And even if you are, it would easily take you hours of research into each and every element to figure out where you stand.

That's the problem that [Chainguard](https://www.chainguard.dev/) exists to solve. Chainguard provides [hundreds of well-maintained custom versions of many of the most popular container images out there](https://images.chainguard.dev/?category=featured). 

Of course, you're free to pull, say, the official MariaDB image into your Dockerfile, but going with the Chainguard version instead will be a far safer choice. That's because Chainguard is constantly analyzing their image layers for vulnerabilities and building images that are as up-to-date and secure as possible.

Let's find out how all of this actually works in the real world. Before we get started with building new images, I should tell you how we're going to visualize each image's vulnerabilities so we can quantify the Chainguard advantage. 

First though, I should explain that infrastructure vulnerabilities are generally defined using the [Common Vulnerabilities and Exposures – or CVE – system](https://www.cve.org/) based on the National Vulnerability Database maintained by the US government's NIST. There are hundreds of thousands of CVE definitions that have been identified and categorized by the CVE system, with each one rated by severity. The existence of this database – along with a number of important related tools – allows us to automate our security assessments. 

Docker Scout is one of those tools. [This page](https://docs.docker.com/scout/install/) gives you installation instructions for using Scout on Docker Engine, but it should run out of the box if you're using Docker Desktop. The `curl` command will simply download the `install-scout` Bash script that'll make everything happen.

```bash
curl -fsSL https://raw.githubusercontent.com/docker/scout-cli/main install.sh -o install-scout.sh
```

## How to Choose the Right Image

I created a Dockerfile that'll pull the official MariaDB image from Docker Hub:

```
FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=my_root_password
ENV MYSQL_DATABASE=my_database

ENV MYSQL_USER=my_user
ENV MYSQL_PASSWORD=my_user_password
```

We'll pretend that the image will be used for a multi-tiered deployment, so we'll create a root database and password, and a new user account with it's own password. There might be an application tier instance that'll use those credentials to access the database at some point. 

Either way, I'll build the image the usual way, giving it the name `mariadb_standard`. 

```
docker build -t mariadb_standard .
```

There's another Dockerfile that's exactly the same as the first one, except that we're pulling the special Chainguard image of MariaDB. 

```

FROM chainguard/mariadb

ENV MYSQL_ROOT_PASSWORD=my_root_password
ENV MYSQL_DATABASE=my_database

ENV MYSQL_USER=my_user
ENV MYSQL_PASSWORD=my_user_password
```

That image came from Docker Hub, but we could have just as easily pulled it from Chainguard's own repo:

```
docker pull cgr.dev/chainguard/mariadb:latest
```

Build this image the same way you did for the official image.  When you scan the two images, here's what you'll see:

```
$ docker images
REPOSITORY         TAG       IMAGE ID       CREATED       SIZE
mariadb_cg         latest    50a484d1ded3   7 days ago    556MB
mariadb_standard   latest    67949ccf8eb5   6 weeks ago   405MB
```

The Chainguard image is, as you can see, quite larger. But note how it's actually a whole lot more recent. 

## How to Scan Your Image

Now it's time to put `docker scout` to work. Here's how that'll work. I'll point Scout to the `mariadb_standard` image first:

```
$ docker scout qv mariadb_standard
```

`qv`, by the way, is short for `quickview`. 

Here's what the output should look like:

![Image](https://www.freecodecamp.org/news/content/images/2024/04/scan1.png)
_docker scout output_

The standard image is made up of three layers, beginning with the Ubuntu 23.10, then Ubuntu 22.04 long term support release, and then MariaDB on top. Ubuntu has 10 Low and 9 Medium vulnerabilities. Alarmingly, the MariaDB layer has 2 Critical and 28 High problems. 

This should be enough to keep an admin up at night. And sorting through all of those to figure out which are show stoppers and which aren't such a big deal for your environment will take you a lot of time.

Now I'll run Scout against the Chainguard image: 

![Image](https://www.freecodecamp.org/news/content/images/2024/04/scan2.png)

First off, we can see that there's only one layer here. I suspect that's one way that Chainguard maintains control over their images. Those two Critical vulnerabilities are still there, but there are only 5 High severity and no Medium or Low at all. 

If you wanted, you could dive deeper to display all the individual vulnerabilities. Here's the command to do that with an excerpt of the output:

```
$ docker scout cves local://mariadb_cg
    ✗ CRITICAL GHSA-xfg6-62px-cxc2 [OWASP Top Ten 2017 Category A9 - Using Components with Known Vulnerabilities]
      https://scout.docker.com/v/GHSA-xfg6-62px-cxc2
      Affected range : <42.2.8                                         
      Fixed version  : 42.7.2, 42.6.1, 42.5.5, 42.4.4, 42.3.9, 42.2.8  
      CVSS Score     : 10.0                                            
      CVSS Vector    : CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H    
    
    ✗ CRITICAL CVE-2024-1597 [Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')]
      https://scout.docker.com/v/CVE-2024-1597
      Affected range : <42.2.28                                      
      Fixed version  : 42.2.28                                       
      CVSS Score     : 10.0                                          
      CVSS Vector    : CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H 
```

We can research each of those using the standard CVE tools and databases to understand them better. But it'll be a whole lot easier than it would have been researching all 28 High severity vulnerabilities in the standard MariaDB image.

## Conclusion

So if you're worried about container image security – and you'd better be – then Docker Scout is an excellent tool for maintaining visibility in your stacks. And Chainguard's cleaner images can give you a significant head start.

_There's more IT goodness in the form of books, courses, and videos available at [my Bootstrap IT site](https://bootstrap-it.com)._


