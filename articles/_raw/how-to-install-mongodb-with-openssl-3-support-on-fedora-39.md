---
title: How to Install MongoDB with OpenSSL 3 Support on Fedora 39
subtitle: ''
author: Matheus Alves dos Santos Freitas
co_authors: []
series: null
date: '2023-12-11T18:52:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-mongodb-with-openssl-3-support-on-fedora-39
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Post-image.jpg
tags:
- name: Linux
  slug: linux
- name: MongoDB
  slug: mongodb
seo_title: null
seo_desc: "In this tutorial, you will learn how to install MongoDB with support for\
  \ the latest version of OpenSSL on the Fedora Linux operating system. \nIf you already\
  \ have it installed, this tutorial will help you fix the mongosh OpenSSL configuration\
  \ error.\nT..."
---

In this tutorial, you will learn how to install MongoDB with support for the latest version of OpenSSL on the Fedora Linux operating system. 

If you already have it installed, this tutorial will help you fix the mongosh OpenSSL configuration error.

To follow along, you will need a terminal with root access and an internet connection to download the packages.

Here's what we'll cover:

* [The Core of the Problem](#heading-the-core-of-the-problem-1)
* [Workaround for Installing MongoDB](#heading-workaround-for-installing-mongodb-1)
* [Understanding the Mongosh OpenSSL Error](#heading-understanding-the-mongosh-openssl-error)
* [Work-Around for Fixing the Error on Existing MongoDB Installations](#work-around-for-fixing-the-error-on-existing-mongodb-installations)
* [How to Install MongoDB with OpenSSL 3 Support From Scratch](#heading-how-to-install-mongodb-with-openssl-3-support-from-scratch)
* [Conclusion](#heading-conclusion)

## The Core of the Problem

If you visit the official MongoDB documentation and look for instructions on how to install it on the Fedora Workstation OS, you won't find anything. But you can find instructions on how to install it on the Red Hat Enterprise Linux OS.

> "The Fedora project is the upstream, community distro of Red Hat® Enterprise Linux." ([Source: Red Hat](https://www.redhat.com/en/topics/linux/fedora-vs-red-hat-enterprise-linux))

In other words, Fedora and Red Hat Enterprise Linux are very similar.

> "The primary difference between community and enterprise distros is who decides what’s important to users. A community distro’s direction is set by contributors, who choose and maintain packages from the wide variety of open source options. The direction of an enterprise distro is set by a vendor, based on the needs of their customers." ([Source: Red Hat](https://www.redhat.com/en/topics/linux/fedora-vs-red-hat-enterprise-linux))

Now, you may think that you can install MongoDB on Fedora by following the tutorial for installing it on Red Hat. By the way, thattutorial is available at [Install MongoDB Community Edition on Red Hat or CentOS](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-red-hat/#install-mongodb-community-edition-on-red-hat-or-centos).

The problem is that it will not work – and to prove that, I will try to install it and show you what happens.

**Note**: I use the Node.js MongoDB Driver which, at the time I am writing this article, does not support the current MongoDB version (7.0). So I will try to install its previous version (6.0).

The required steps to install MongoDB on Fedora are as follows:

1. Configure the package management system
2. Install the MongoDB packages

To perform the first step, open your terminal, get root access, and type the following:

```text
# touch /etc/yum.repos.d/mongodb-org-6.0.repo
```

Now, open the file using your preferred text editor (I am using the Gnome Text Editor, because it's shipped with Fedora):

```text
# gnome-text-editor /etc/yum.repos.d/mongodb-org-6.0.repo
```

And paste in these lines:

```text
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

Save the file and close it.

The second step can be performed by running the following command:

```text
# dnf install -y mongodb-org

```

After running the command you will get an error similar to this:

```text
Fedora 39 - x86_64 - Updates                     34 kB/s |  46 kB     00:01    
MongoDB Repository                               63  B/s | 391  B     00:06    
Errors during downloading metadata for repository 'mongodb-org-6.0':
  - Status code: 404 for https://repo.mongodb.org/yum/redhat/39/mongodb-org/6.0/x86_64/repodata/repomd.xml (IP: 65.8.214.17)
Error: Failed to download metadata for repo 'mongodb-org-6.0': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
Ignoring repositories: mongodb-org-6.0
Last metadata expiration check: 0:00:02 ago on Thu 30 Nov 2023 09:15:21 AM -03.
No match for argument: mongodb-org
Error: Unable to find a match: mongodb-org

```

This is a `404` error, which means you need to change the `baseurl` of the file that configures the repo.

If you try to open the `baseurl` in your browser you will get a `404` error as well:

![Screenshot of the 404 error you will get if you visit the baseurl on a browser.](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-from-2023-11-30-17-05-28.png)
_`baseurl` `404` error_

This is the core of the problem.

## Workaround for Installing MongoDB

You can infer that in order to fix the problem you need to change the value assigned to the `baseurl`. The question becomes: what is the URL that leads to the page containing the packages?

The answers is offered by the official MongoDB documentation:

> "You can also download the `.rpm` files directly from the MongoDB repository. Downloads are organized by Red Hat / CentOS version (e.g. `7`), then MongoDB release version (e.g. `6.0`), then architecture (e.g. `x86_64`)." ([Source: MongoDB](https://www.mongodb.com/docs/v6.0/tutorial/install-mongodb-on-red-hat/#install-mongodb-community-edition))

Now, visiting the [MongoDB repository](https://repo.mongodb.org/yum/redhat/) will take you to this page:

![Screenshot of the MongoDB repository page. The title of the page reads "Index of RedHat". The page lists repositories with old versions of MongoDB, as well as repositories with newer versions for different RedHat OS versions.](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-from-2023-11-30-17-20-57.png)
_MongoDB repository page_

From here I navigated to the proper repo, selecting my preferred MongoDB version and system architecture. You should do the same.

I ended up with the following URL:

```text
https://repo.mongodb.org/yum/redhat/9Server/mongodb-org/6.0/x86_64/RPMS/
```

This URL leads to the repo where the packages of MongoDB 6.0 can be found for systems based on an x86_64 architecture.

This is what I found there:

![Screenshot of the MongoDB repo that contains the packages of its sixth version for systems based on an x86_64 architecture.](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-from-2023-11-30-17-27-37.png)
_MongoDB 6.0 packages for x86_64 systems_

After being sure the packages could be found, I updated the file that configures the repo. But the `baseurl` should point to the parent of `RPMS` directory, which resulted in the following URL:

```text
https://repo.mongodb.org/yum/redhat/9Server/mongodb-org/6.0/x86_64/
```

I ran:

```text
# gnome-text-editor /etc/yum.repos.d/mongodb-org-6.0.repo
```

Updated the `baseurl`:

```text
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9Server/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

And installed the packages:

```text
# dnf install -y mongodb-org
```

These are the packages that that were installed:

```text
Installed:
  mongodb-database-tools-100.9.3-1.x86_64                                       
  mongodb-mongosh-2.1.0-1.el8.x86_64                                           
  mongodb-org-6.0.12-1.el9.x86_64                                               
  mongodb-org-database-6.0.12-1.el9.x86_64                                     
  mongodb-org-database-tools-extra-6.0.12-1.el9.x86_64                         
  mongodb-org-mongos-6.0.12-1.el9.x86_64                                       
  mongodb-org-server-6.0.12-1.el9.x86_64                                       
  mongodb-org-tools-6.0.12-1.el9.x86_64                                         
  openssl-1:3.1.1-4.fc39.x86_64 
```

## Understanding the Mongosh OpenSSL Error

To confirm the installation of the database server, run this command:

```text
# mongod --version
```

You will get a message similar to this:

```text
db version v6.0.12
Build Info: {
    "version": "6.0.12",
    "gitVersion": "21e6e8e11a45dfbdb7ca6cf95fa8c5f859e2b118",
    "openSSLVersion": "OpenSSL 3.1.1 30 May 2023",
    "modules": [],
    "allocator": "tcmalloc",
    "environment": {
        "distmod": "rhel90",
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}
```

To confirm the installation of the shell, run this command:

```text
# mongosh --version
```

And this is the message you will get:

```text
mongosh: OpenSSL configuration error:
00899523A67F0000:error:030000A9:digital envelope routines:alg_module_init:unknown option:../deps/openssl/openssl/crypto/evp/evp_cnf.c:61:name=rh-allow-sha1-signatures, value=yes
```

Oops! There was an error.

I checked the installed OpenSSL version by running this command:

```text
# openssl version
```

And got this result:

```text
OpenSSL 3.1.1 30 May 2023 (Library: OpenSSL 3.1.1 30 May 2023)
```

With that, I discarded a possible mismatch between the installed and the required OpenSSL versions.

After some research, I discovered that:

> "There are two new PPA packages created from the mongosh source: In addition to mongodb-mongosh, mongodb-mongosh-shared-openssl11 and mongodb-mongosh-shared-openssl3 are also provided. These link against a system-installed dynamic OpenSSL library." ([Source: MongoDB Jira](https://jira.mongodb.org/browse/MONGOSH-1231?jql=text%20~%20%22mongodb-mongosh-shared-openssl3%22))

When I looked at the packages that were installed, I saw the _mongodb-mongosh_ package. So I knew I need to replace it with the _mongodb-mongosh-shared-openssl3_.

By the way,

> "The package name denotes that it’s the cut of mongosh compiled against openssl3." ― Jack Woehr

Now that we understand the problem, let's fix it.

## Workaround for Fixing the Error on Existing MongoDB Installations

If you already have MongoDB installed, these are the steps required to fix the problem:

1. Stop MongoDB
2. Remove the _mongodb-org_ package
3. Remove the _mongodb-mongosh_ package
4. Install the _mongodb-mongosh-shared-openssl3_ package
5. Enable MongoDB

You have to perform these steps in the correct order. If you try to install the _mongodb-mongosh-shared-openssl3_ package without uninstalling the _mongodb-mongosh_ package first, you will get a conflict error:

```text
Error: Transaction test error:
  file /usr/bin/mongosh from install of mongodb-mongosh-shared-openssl3-2.1.0-1.el8.x86_64 conflicts with file from package mongodb-mongosh-2.1.0-1.el8.x86_64
```

If you try to uninstall the _mongodb-mongosh_ package without uninstalling the _mongodb-org_ package first, you will get a dependency error:

```text
error: Failed dependencies:
	mongodb-mongosh is needed by (installed) mongodb-org-6.0.12-1.el9.x86_64
```

To stop MongoDB, run this command:

```
# systemctl stop mongod
```

**Note**: The command will output nothing if everything goes well.

To remove the _mongodb-org_ and the _mongodb-mongosh_ packages, run:

```text
# rpm -e mongodb-org mongodb-mongosh
```

**Note**: I am not using the `dnf` command as it would remove _mongodb-org_ and all of its dependencies.

You can also confirm that only the two packages were removed by running:

```text
# rpm -qa | grep mongodb-*
```

The output should be:

```text
mongodb-org-database-tools-extra-6.0.12-1.el9.x86_64
mongodb-database-tools-100.9.3-1.x86_64
mongodb-org-tools-6.0.12-1.el9.x86_64
mongodb-org-server-6.0.12-1.el9.x86_64
mongodb-org-mongos-6.0.12-1.el9.x86_64
mongodb-org-database-6.0.12-1.el9.x86_64
```

To install the _mongodb-org_ and the _mongodb-mongosh-shared-openssl3_ packages, run:

```
# dnf install -y mongodb-org mongodb-mongosh-shared-openssl3
```

Finally, to start MongoDB with your operating system, run:

```text
# systemctl start mongod
```

If you want to be sure the workaround worked, run:

```text
# mongod --version
```

And then this:

```text
# mongosh --version
```

Now, if you are concerned about destroying data, know that logs and databases will only be removed if you run the following commands:

```text
# rm -r /var/log/mongodb

```

And this:

```text
# rm -r /var/lib/mongo
```

One more thing: if you run `mongosh` and get the following error:

```text
MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017
```

restart your machine. It will solve the problem.

## How to Install MongoDB with OpenSSL 3 Support From Scratch

If you are installing MongoDB for the first time, you only have to perform two steps:

1. Configure the package management system
2. Install the MongoDB packages specifying them individually

You can perform the first step by following what I did on the [The Core of the Problem](#heading-the-core-of-the-problem-1) and [Workaround for Installing MongoDB](#heading-workaround-for-installing-mongodb-1) sections of this article.

However, to install the right packages you should replace this command:

```text
# dnf install -y mongodb-org
```

with this one:

```text
# dnf install -y mongodb-org mongodb-mongosh-shared-openssl3 openssl mongodb-org-database-tools-extra mongodb-database-tools mongodb-org-tools mongodb-org-server mongodb-org-mongos mongodb-org-database
```

You can confirm that all packages have been installed by running:

```text
# rpm -qa | grep mongodb-*
```

Which should output something similar to this:

```text
mongodb-org-database-tools-extra-6.0.12-1.el9.x86_64
mongodb-database-tools-100.9.3-1.x86_64
mongodb-org-tools-6.0.12-1.el9.x86_64
mongodb-org-server-6.0.12-1.el9.x86_64
mongodb-org-mongos-6.0.12-1.el9.x86_64
mongodb-org-database-6.0.12-1.el9.x86_64
mongodb-mongosh-shared-openssl3-2.1.0-1.el8.x86_64
mongodb-org-6.0.12-1.el9.x86_64
```

Keep in mind that the previous command will only output _mongodb-related_ packages. To confirm OpenSSL installation, run:

```text
# openssl version
```

You should get something like this:

```text
OpenSSL 3.1.1 30 May 2023 (Library: OpenSSL 3.1.1 30 May 2023)
```

The packages will be updated with your system as you can see in the screenshot below.

![Screenshot of the mongodb-mongosh-shared-openssl3 package being automatically updated with the operating system.](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-from-2023-12-05-01-26-14.png)
_`mongodb-mongosh-shared-openssl3` update_

## Conclusion

Package updates are important, because they bring in new functionality and/or increase applications security. But they can also cause headaches when they case errors like the one we dealt with in this article.

Although you might be tempted to roll back the update to get rid of the problem, don't do that. Try to solve it instead.

Paying attention to error messages, reading official documentation, and researching the Web will most likely be enough for solving the majority of the problems you come across.

Besides, knowing how different commands affect the way packages are installed/uninstalled on your operating system can salve you time and data (if you are on a metered connection).

If this article was useful to you, bookmark it and share it with your friends. You can can also follow me on [Twitter](https://twitter.com/matheus4lvesfcc).

See you in the next one!

