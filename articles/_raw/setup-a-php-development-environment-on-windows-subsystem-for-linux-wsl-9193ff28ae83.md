---
title: How to set up a PHP development environment on Windows Subsystem for Linux
  (WSL)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T15:43:04.000Z'
originalURL: https://freecodecamp.org/news/setup-a-php-development-environment-on-windows-subsystem-for-linux-wsl-9193ff28ae83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hgWsj4pEYwb8sdp3UQDlTw.jpeg
tags:
- name: Linux
  slug: linux
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: 'By András Magyar

  PHP development on Windows has some disadvantages. But, Microsoft now offers a great
  option for PHP developers who work on Windows: The Windows Subsystem for Linux (WSL).
  WSL is a compatibility layer for running Linux binary executab...'
---

By András Magyar

PHP development on Windows has some disadvantages. But, Microsoft now offers a great option for PHP developers who work on Windows: The Windows Subsystem for Linux (WSL). WSL is a compatibility layer for running Linux binary executables (in ELF format) natively on Windows 10. Microsoft says:

> “This is primarily a tool for developers — especially web developers and those who work on or with open source projects”.

We can run a Linux environment directly on Windows without the overhead of a virtual machine.

**Note:** This article is not only for the Windows Insiders. These methods will work on the latest stable releases of Windows 10 as well.

In this tutorial, we will set up a LAMP stack (Ubuntu 16.04, Apache, PHP 7.1, MariaDB) on WSL for development. You can set up other stacks (for example, a LEMP stack) with similar methods.

### Prerequisites

Before you begin this guide, you will need the following:

* A 64-bit version of Windows 10 with the [Creators Update](https://support.microsoft.com/en-us/help/4028685/windows-get-the-windows-10-creators-update) or later.
* familiarity with Linux/bash (If you would like to get familiar with the command-line, you can read [this DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal)).

### Step 1: installing bash on Windows

First, you will need WSL installed on your computer.

You can install more Linux distributions from the Microsoft Store (Ubuntu, openSUSE, SUSE Linux Enterprise Server 12). But, in this tutorial, we will set up the LAMP stack on Ubuntu, **so you need to select Ubuntu**.

Microsoft has a great tutorial on how to install WSL, [please follow the instructions of the article](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

If you have successfully installed Bash on Ubuntu on Windows, let’s install and configure a simple LAMP stack for development.

### Step 2: installing an Apache HTTP server

We want to install the latest stable version of Apache, but official Ubuntu repositories don’t contain the latest release.

We need to add a PPA for Apache packages. A Personal Package Archive (PPA) is a repository that allows third-party developers to build and distribute packages for Ubuntu. Ondřej Surý’s PPA offers the latest Apache/PHP packages for Ubuntu.

To add the PPA, run the following command in the WSL bash:

```
sudo add-apt-repository ppa:ondrej/apache2
```

Once the PPA is configured, update the local package index:

```
sudo apt-get update
```

Install Apache:

```
sudo apt-get install apache2
```

Create a project folder for your web applications. This folder should be outside of the WSL filesystem. I recommend you to use your Documents folder.

The following command will create a server folder inside your Documents directory. Please replace **YOUR WINDOWS USERNAME** with your Windows username.

```
sudo mkdir /mnt/c/Users/YOUR WINDOWS USERNAME/Documents/server
```

Create a symbolic link to the selected folder.

```
sudo ln -s /mnt/c/Users/YOUR WINDOWS USERNAME/Documents/server /var/www/devroot
```

Open the Apache default virtual host configuration file:

```
sudo nano /etc/apache2/sites-enabled/000-default.conf
```

Modify the document root to “/var/www/devroot”, which points to your project folder outside of WSL’s filesystem. Set `ServerName` to `localhost` (if the port 80 is reserved by a Windows application, replace 80 with an unused port):

```
<VirtualHost *:80>        ServerName localhost        ServerAdmin webmaster@localhost        DocumentRoot  /var/www/devroot      <Directory /var/www/>        Options Indexes FollowSymLinks        AllowOverride All        Require all granted      </Directory>        ErrorLog ${APACHE_LOG_DIR}/error.log        CustomLog ${APACHE_LOG_DIR}/access.log combined</VirtualHost>
```

When you are finished, save the file by pressing Ctrl-O, and hit Enter to confirm. Exit with Ctrl-X.

Open your favorite Windows editor/IDE, and create an “index.html” file in your project folder (C:\Users\ **YOUR WINDOWS USERNAME**\Documents\server) with the following content:

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="utf-8">  <title>It works!</title></head>&lt;body>  <h1>It works!</h1></body></html>
```

Start the Apache HTTP server:

```
sudo service apache2 start
```

Open [http://localhost/](http://localhost/) in your browser and you should see the “It works” title.

Don’t forget to enable Apache modules that are necessary for you. For example, you can enable mod_rewrite:

```
sudo a2enmod rewritesudo service apache2 restart
```

### Step 3: installing the MariaDB server

Add a repo that contains the latest MariaDB packages:

```
sudo apt-get install software-properties-common
```

```
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
```

```
sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ams2.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu xenial main'
```

Install MariaDB:

```
sudo apt-get updatesudo apt-get install mariadb-server
```

You will be prompted to create a root password during the installation. Choose a secure password and remember it, because you will need it later.

Start MariaDB:

```
sudo service mysql start
```

Run the following script (this changes some of the less secure default options):

```
mysql_secure_installation
```

### Step 4: installing PHP

Add PPA for the latest PHP:

```
sudo add-apt-repository ppa:ondrej/phpsudo apt-get update
```

Install PHP 7.1 packages:

```
sudo apt-get install php7.1 libapache2-mod-php7.1 php7.1-mcrypt php7.1-mysql php7.1-mbstring php7.1-gettext php7.1-xml php7.1-json php7.1-curl php7.1-zip
```

We have to restart Apache:

```
sudo service apache2 restart
```

Create an info.php file in your project folder with the following content:

```
<?phpphpinfo();
```

Open [http://localhost/info.php](http://localhost/info.php) in your browser. If PHP works correctly, you should see the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1q-zAJXFIrM9FsQmnkgSLwfMJgVTolUpKY0Y)

### Step 5: installing phpMyAdmin

phpMyAdmin is a free and open source administration tool for MySQL and MariaDB.

With phpMyAdmin, you can easily create/manage your databases using a web interface.

```
sudo apt-get install phpmyadmin
```

* When the first prompt appears, press Space, Tab, and then Enter to select Apache.
* Select yes when asked to use dbconfig-common to set up the database.
* Provide your MariaDB root password
* Choose a password for the phpMyAdmin application itself

Enable the necessary PHP extensions:

```
sudo phpenmod mcryptsudo phpenmod mbstring
```

Restart Apache:

```
sudo service apache2 restart
```

Now you can access phpMyAdmin on the following URL: [http://localhost/phpmyadmin/](http://localhost/phpmyadmin/)  
You can login using the root username and the root password you set up during the MariaDB installation.

### Step 6: installing Composer

Composer is a package manager for PHP. It allows you to install/update the libraries your project depends on. If you are a PHP developer you probably use composer.

Visit [Composer’s download page](https://getcomposer.org/download/) and follow the instructions in the Command-line installation section. After Composer has installed successfully, you can install it globally:

```
sudo mv composer.phar /usr/local/bin/composer
```

Now it can be run from any location by typing:

```
composer
```

![Image](https://cdn-media-1.freecodecamp.org/images/eRZmxz7jyQxXn1Z7RlegrHDn1M4E6kgB6Gml)

### Step 7: installing Git:

Git is a version control system which is primarily used for source code management. [Learn more about Git here](https://git-scm.com/doc).

You can install it by running the following command:

```
sudo apt-get install git
```

Before you use Git (and if you aren’t familiar with it), please read the “How To Set Up Git” section from the [How To Install Git on Ubuntu 16.04 tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-16-04).

### Step 8: automatically start LAMP on WSL (optional)

Background tasks are currently not supported on WSL. When you close Bash your services (Apache and MariaDB) will stop.

**Note for Windows Insiders:** Background tasks are now supported on WSL starting with Windows Insider Build 17046 (for more details, you can read the following blog post: [Background Task Support in WSL](https://blogs.msdn.microsoft.com/commandline/2017/12/04/background-task-support-in-wsl/)), but the auto start of services is still not available.

Unfortunately, automatically starting your services is a bit difficult.

Let’s configure autostarting!

We need to start the services without typing your password.

**Before you get started with this**, please take a look at the following tutorial [How To Edit the Sudoers File on Ubuntu and CentOS](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos).

Run the following command:

```
sudo visudo -f /etc/sudoers.d/services
```

Copy and paste the following to the editor and then save:

```
%sudo ALL=(root) NOPASSWD: /usr/sbin/service *%wheel ALL=(root) NOPASSWD: /usr/sbin/service *
```

This enables us to start the services (like Apache and MariaDB) without using our password.

Start Command Prompt (not the bash) as administrator and run:

```
SchTasks /Create /SC ONLOGON /TN "Start WSL LAMP" /TR "c:\Windows\System32\bash.exe -c 'sudo service apache2 start; sudo service mysql start; cd ~; bash'"
```

The above command creates a task that runs automatically when you login to Windows. It does the following:

* Starts Apache
* Starts MariaDB
* Changes the directory to your home directory

**Don’t forget: when you close the terminal window, services will stop and you should restart them manually!**

### Step 9: add test domains (optional)

When you work on more web applications, multiple test domains will be helpful. For example, if you are working on myapp.com, you can access the local development version on [http://myapp.t](http://myapp.dev)est/ instead of [http://localhost/myapp](http://localhost/myapp).

In the following, you can replace “myapp” with your web application’s name.  
Create a folder in your projects directory for your web application:

```
sudo mkdir /mnt/c/Users/YOUR WINDOWS USERNAME/Documents/server/myapp
```

Add the virtual host file to Apache:

```
sudo nano /etc/apache2/sites-available/myapp.test.conf
```

Save the following configuration to the new file (don’t forget to replace myapp with your application’s name).

```
<VirtualHost *:80>
```

```
ServerName myapp.test
```

```
ServerAdmin webmaster@localhost DocumentRoot /var/www/devroot/myapp
```

```
<Directory /var/www/> Options Indexes FollowSymLinks AllowOverride All Require all granted </Directory>
```

```
ErrorLog ${APACHE_LOG_DIR}/error.log CustomLog ${APACHE_LOG_DIR}/access.log combined
```

```
</VirtualHost>
```

Enable the new site:

```
sudo a2ensite myapp.test
```

Restart Apache:

```
sudo service apache2 restart
```

Finally, start Notepad or your favorite editor/IDE on Windows with admin privileges (**Run as administrator**) and open the **hosts** file. It is located in the **c:\windows\system32\drivers\etc** folder.

Add the following line to the end of the file and save it:

```
127.0.0.1 myapp.test
```

Now you can access your web application on the [http://myapp.test/](http://myapp.test/) domain.  
You can also add more test domains with the same method.

#### Conclusion

WSL does not replace Vagrant or Docker, and it is experimental. Automatically starting services is currently not supported on WSL, and this is one of the biggest problems with it at this moment. However, the Windows Subsystem for Linux is a great option for developers to use a native Linux shell on Windows. I think you should give it a try!

