---
title: How to create a Django server running uWSGI, NGINX and PostgreSQL on AWS EC2
  with Python 3.6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-26T18:38:32.000Z'
originalURL: https://freecodecamp.org/news/django-uwsgi-nginx-postgresql-setup-on-aws-ec2-ubuntu16-04-with-python-3-6-6c58698ae9d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RoxYjB7zefsqzjUMLLaprQ.png
tags:
- name: AWS
  slug: aws
- name: Django
  slug: django
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sumeet Kumar

  Getting a server up and running for a new project every time might be time-consuming
  or difficult for new developers. So I thought I’d write a step-by-step guide that
  will ease the deployment process.

  If you’re in no mood to read, you...'
---

By Sumeet Kumar

Getting a server up and running for a new project every time might be time-consuming or difficult for new developers. So I thought I’d write a step-by-step guide that will ease the deployment process.

**If you’re in no mood to read, you can copy paste each step as described (replace values) and get your server up and running ?**

#### Prerequisites:

1. Amazon Linux EC2 instance up and running with the associated key pair (_ssh access to it_).
2. **Port 22, 80** must be open for this instance.
3. Django application that you want to deploy.
4. Database settings are configured to use PostgreSQL.
5. _requirements.txt_ is present in your app, having dependencies list to install.
6. Git repository for your Django app.

### SSH & update ubuntu instance

You need to ssh into your EC2 instance, so make sure you have **port 22** open for your instance and then do a update/upgrade.

```
ssh -i path-to-your-key.pem ubuntu@your-aws-instance-public-ip

sudo apt-get update && sudo apt-get upgrade -y
```

### Installing Python3.6.x on AWS EC2 (ubuntu 16.04)

We will download the **tar.xz** file from official site and than manually install it. Before that we need to install some required dependencies.

#### Building and installing dependencies

```
sudo apt install build-essential checkinstall

sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev
```

#### Downloading & manually installing required Python version

```
cd /opt && sudo wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tar.xz

sudo tar -xvf Python-3.6.6.tar.xz

cd Python-3.6.6/

sudo ./configure

sudo make && sudo make install
```

#### Removing downloaded file

```
sudo rm -rf Python-3.6.6.tar.xz
```

#### Check Python version

```
python3 -V
> Python 3.6.6
```

### Setting up Ubuntu user for our application

Django itself is very secure framework, I agree. But web applications are still vulnerable. It is good practice to run your application as system users with limited privileges which has limited access to resources on your server. So in this section, we will be adding a new user & permission group to our EC2 instance.

#### Adding ubuntu system group ‘groupname’ [webapps in my case] and assign a user ‘username’ [bunny in my case] to this group

```
sudo groupadd --system webapps
sudo useradd --system --gid webapps --shell /bin/bash --home /webapps/project_name bunny
```

Note: I am assuming “**project_name**” is the name that you might have used during “**django-admin startproject <na**me>”

#### Create a directory to store your application

Create a directory to store your application in /webapps/project_name/. Change the owner of that directory to your application user bunny:

```
sudo mkdir -p /webapps/project_name/

sudo chown bunny /webapps/project_name/
```

#### Allow limited access to other group users to application directory

```
sudo chown -R bunny:users /webapps/project_name

sudo chmod -R g+w /webapps/project_name
```

#### Now you can switch to your user

```
sudo su - bunny

// your console will switch to something like this
bunny@ip-172-31-5-231:~$
```

To switch back to **sudo** user, just do `**ctrl+d**` and it’ll kill the user terminal.

### Installing and configuring PostgresSQL

#### Installing PostgreSQL & creating database

```
sudo apt install postgresql postgresql-contrib

sudo su - postgres

postgres@ip-172-31-5-231:~$ psql

postgres=# CREATE DATABASE database_name;
```

#### Changing default password for postgres while in **psql** terminal

```
postgres=# \password
```

### Deploy Django app on EC2 instance via Git in virtual environment

Deploying your app using a virtual environment allows your app and its requirements to be handled separately. It is good practice to keep your app isolated.

Using the environment concept is handy when you are deploying more than one Django app on a single instance to keep them and their dependencies isolated from each other.

We will be creating a [virtual environment](https://docs.python.org/3.6/library/venv.html) in our system user (_bunny_) directory. Before that we will be installing git as a _sudo_ user.

#### Installing Git and pulling your code from git repo

```
sudo apt-get install git

sudo su - bunny

// change to your repo https or ssh link
bunny@ip-172-31-5-231:~$ git remote add origin 

git@github.com:<user>/<user-repo>.git

bunny@ip-172-31-5-231:~$ git pull origin <branch_name>
```

Note that we haven’t cloned our complete repo here. Instead we manually set our git link and only pulled the branch that we want to deploy to this instance. You may have a different instance for your development, beta, or production ready web app corresponding to each branch on git.

#### Creating virtual environment using Python3.6 in current directory

```
bunny@ip-172-31-5-231:~$ python3.6 -m venv .
bunny@ip-172-31-5-231:~$ source bin/activate
(project_name)bunny@ip-172-31-5-231:~$ pip install -r requirements.txt
```

At this point, we have successfully set up our project. Now we need to run some **manage.p_y_** command. This will require that we are in the directory where our manage.py is present, or every time we need to give a path to it:

```
(project_name)bunny@ip-172-31-5-231:~$ python <path-to->manage.py migrate

(project_name)bunny@ip-172-31-5-231:~$ python <path-to->manage.py createsuperuser

(project_name)bunny@ip-172-31-5-231:~$ python <path-to->manage.py collectstatic
```

Note: `collectstatic` command requires that the STATIC configuration is setup properly. We are not discussing that here, though, as it is not in the scope of this tutorial.

```
(project_name)bunny@ip-172-31-5-231:~$ python <path-to->manage.py runserver 0.0.0.0:8000
```

This will start up the development server on port `8000`. **Assuming port 8000 is also open for your instance, you can visit your server's domain name or IP address followed by `8000` in your browser.**

```
http://your_server_domain_or_public_IP:8000
```

```
http://your_server_domain_or_public_IP:8000/admin
```

**Note: Don’t forget to add your domain or IP to ALLOWED_HOST in your settings.py**

### Setting up the uWSGI Application Server

Now that we’ve got our project set up and ready to go, we can configure uWSGI to serve our app to the web instead of the lightweight development server provided by Django.

**If you’re thinking of running the runserver command on a screen, drop it. The dev server with Django is terribly lightweight, highly insecure, and not scalable.**

You can install uWSGI either in virtualenv or globally and configure it accordingly.

In this tutorial, we’ll be installing uWSGI in _virtualenv_. Before we can install uWSGI, we need the Python development files that the software relies on.

#### Installing uWSGI along with its dependencies

```
sudo apt-get install python3-dev
```

```
sudo su - bunny
```

```
bunny@ip-172-31-5-231:~$ source bin/activate
```

```
(project_name)bunny@ip-172-31-5-231:~$ pip install uwsgi
```

Let’s run the server using uWSGI. This command does the same thing a _manage.py runserver_ would do. You need to replace values accordingly to successfully test with this command.

```
(project_name)bunny@ip-172-31-5-231:~$ uwsgi --http :8000 --home <path-to-virtualenv> --chdir <path-to-manage.py-dir> -w <project-name>.wsgi
```

#### Creating uWSGI configuration file

Running uWSGI from the command line is only useful for testing. For actual deployment, we will create a **_._ini** file somewhere in our system user directory. This file will contain all the configuration for handling a heavy request load, and can be tweaked accordingly.

Later in this tutorial, we will run uWSGI behind NGINX. NGINX is highly compatible with uWSGI and has built-in support for interacting with uWSGI.

#### Create a directory **conf** in your system user directory where you will store **uwsgi.ini**

```
(project_name)bunny@ip-172-31-5-231:~$ mkdir conf
```

```
(project_name)bunny@ip-172-31-5-231:~$ cd conf
```

```
(project_name)bunny@ip-172-31-5-231:~$ nano uwsgi.ini
```

Copy the below code from the gist and save it I think the comments are explanatory enough for each option.

**NOTE: `updateMe` is supposed to be you project name. It is the same name you gave above while creating the system user directory, so update accordingly.**

```
[uwsgi]

# telling user to execute file
uid = bunny

# telling group to execute file
gid = webapps

# name of project you during "django-admin startproject <name>"
project_name = updateMe

# building base path to where project directory is present [In my case this dir is also where my virtual env is]
base_dir = /webapps/%(project_name)

# set PYTHONHOME/virtualenv or setting where my virtual enviroment is
virtualenv = %(base_dir)

# changig current directory to project directory where manage.py is present
chdir = %(base_dir)/src/

# loading wsgi module
module =  %(project_name).wsgi:application

# enabling master process with n numer of child process
master = true
processes = 4

# enabling multithreading and assigning threads per process
# enable-threads  = true
# threads = 2

# Enable post buffering past N bytes. save to disk all HTTP bodies larger than the limit $
post-buffering = 204800

# Serialize accept() usage (if possibie).
thunder-lock = True


# Bind to the specified socket using default uwsgi protocol.
uwsgi-socket = %(base_dir)/run/uwsgi.sock

# set the UNIX sockets’ permissions to access
chmod-socket = 666

# Set internal sockets timeout in seconds.
socket-timeout = 300

# Set the maximum time (in seconds) a worker can take to reload/shutdown.
reload-mercy = 8

# Reload a worker if its address space usage is higher than the specified value (in megabytes).
reload-on-as = 512

# respawn processes taking more than 50 seconds
harakiri = 50

# respawn processes after serving 5000 requests
max-requests = 5000

# clear environment on exit
vacuum = true

# When enabled (set to True), only uWSGI internal messages and errors are logged.
disable-logging = True

# path to where uwsgi logs will be saved
logto = %(base_dir)/log/uwsgi.log

# maximum size of log file 20MB
log-maxsize = 20971520

# Set logfile name after rotation.
log-backupname = %(base_dir)/log/old-uwsgi.log

# Reload uWSGI if the specified file or directory is modified/touched.
touch-reload = %(base_dir)/src/

# Set the number of cores (CPUs) to allocate to each worker process.
# cpu-affinity = 1

# Reload workers after this many seconds. Disabled by default.
max-worker-lifetime = 300
```

I am trying to make everything easy with clear explanations. Cross check paths, directory name, and other inputs that you are required to replace.

We need to create the log file and run directory where our socket file will be created, that we just mentioned in our uwsgi.ini:

```
(project_name)bunny@ip-172-31-5-231:~$ mkdir log
```

```
(project_name)bunny@ip-172-31-5-231:~$ mkdir run
```

```
(project_name)bunny@ip-172-31-5-231:~$ touch log/uwsgi.log
```

Make sure to change permissions for these two so that every group or user can write or execute files in these directories:

```
$ sudo chmod 777 /webapps/updateMe/run
```

```
$ sudo chmod 777 /webapps/updateMe/log
```

Now let’s try running the server using **uwsgi.ini** that we just created.

```
(project_name)bunny@ip-172-31-5-231:~$ uwsgi --ini /webapps/updateMe/conf/uwsgi.ini
```

If everything up until now is setup correctly, then it should be running. If not, then you need to go back to check for anything you missed (like the path/project name, etc).

To check any uswgi log you can **cat** or **tail** uwsgi.log:

```
(project_name)bunny@ip-172-31-5-231:~$ tail log/uwsgi.log
```

#### Create a systemd Unit File for uWSGI

At this point if everything is cool, you can even run this command in [screen](http://manpages.ubuntu.com/manpages/bionic/en/man1/screen.1.html) and detach it — but again, this is not a good practice at all. Instead we will create a system service and let **systemd** (Ubuntu’s service manager) take care of it.

#### Switch back to sudo user

```
$ sudo nano /etc/systemd/system/uwsgi.service
```

and copy paste code from the below gist. Don’t forget to update and crosscheck names/path that suit your app:

```
[Unit]
Description=uWSGI instance to serve updateMe project
After=network.target

[Service]
User=bunny
Group=webapps
WorkingDirectory=/webapps/project_name/src
Environment="PATH=/webapps/project_name/bin"
ExecStart=/webapps/project_name/bin/uwsgi --ini /webapps/project_name/conf/uwsgi.ini
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

After you save the above file and close it, you can run following commands:

**Reload systemctl daemon to reload systemd manager configuration and recreate the entire dependency tree**

```
$ sudo systemctl daemon-reload
```

**Enable uwsgi service to start on system reboot**

```
$ sudo systemctl enable uwsgi
```

**Start uwsgi service**

```
$ sudo service uwsgi start
```

**Restart uwsgi service**

```
$ sudo service uwsgi restart
```

**Check uwsgi service status**

```
$ sudo service uwsgi status
```

Take a deep breath here if everything ran smoothly. We just finished setting up most hectic part of this tutorial, so you should be proud.

Next we will setup NGINX, and then we’ll be done! I know this is taking a bit of time, but believe me — once done, you will be as happy as I will be after publishing this tutorial.

### Setting Up NGINX on EC2 for uWSGI

NGINX is a lightweight server, and we’ll use it as a reverse proxy.

**We could let uWSGI run directly on port 80, but NGINX has a lot more [benefits](https://serverfault.com/questions/590819/why-do-i-need-nginx-when-i-have-uwsgi/590833#590833) which makes it desirable.** Also NGINX natively includes [support](https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html) for uWSGI.

#### Enough talk, let’s install NGINX on our instance

```
$ sudo apt-get install nginx
```

Now when you go to **http://your-public-ip-or-address**, you will see a Nginx welcome page. This is because NGINX is listening to port 80 according to its default configuration.

NGINX has two directories, **sites-available** and **sites-enabled,** that need our attention. **sites-available** stores all conf files for all available sites on that particular instance. **sites-enabled** stores the symbolic link for each enabled site to the sites-available directory.

By default, there is only one conf file named default that has basic setup for NGINX. You can either modify it or create a new one. In our case, I am going to delete it:

```
$ sudo rm -rf /etc/nginx/sites-available/default
```

```
$ sudo rm -rf /etc/nginx/sites-enabled/default
```

Let’s create our **nginx-uwsgi.conf** file to connect the browser request to the uwsgi server we are running in site-available:

```
$ sudo nano /etc/nginx/sites-available/nginx-uwsgi.conf
```

and copy the following code from the gist below:

```
upstream updateMe_dev {
    server unix:/webapps/updateMe/run/uwsgi.sock;
}

server {
    listen 80;
    server_name your-IP-or-address-here;
    charset utf-8;

    client_max_body_size 128M;

    location /static {
    # exact path to where your static files are located on server 
    # [mostly you won't need this, as you will be using some storage service for same]
        alias /webapps/updateMe/static_local;
    }

    location /media {
    # exact path to where your media files are located on server 
    # [mostly you won't need this, as you will be using some storage service for same]
        alias /webapps/updateMe/media_local;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass updateMe_dev;
        uwsgi_read_timeout 300s;
        uwsgi_send_timeout 300s;
    }

    access_log /webapps/updateMe/log/dev-nginx-access.log;
    error_log /webapps/updateMe/log/dev-nginx-error.log;
}
```

#### Create symbolic link into sites-enabled directory for same

```
$ sudo ln -s /etc/nginx/sites-available/nginx-uwsgi.conf /etc/nginx/sites-enabled/nginx-uwsgi.conf
```

That’s all, we’re almost there, about to finish up…

#### Reload systemctl daemon

```
$ sudo systemctl daemon-reload
```

#### Enable nginx service on system reboot

```
$ sudo systemctl enable nginx
```

#### Start Nginx service

```
$ sudo service nginx start
```

Test Nginx. It should return OK, Successful as a part of the result.

```
$ sudo nginx -t
```

If NGINX fails, you can check its last error-log or access-log on the path specified by us in its conf.

```
$ tail -f /webapps/updateMe/log/nginx-error.log
```

```
$ tail -f /webapps/updateMe/log/nginx-access.log
```

#### Restart Nginx Service

```
$ sudo service nginx restart
```

#### Check Nginx Service status

```
$ sudo service nginx status
```

You should now be able to reach your app at [**http://your-public-ip-or-address**](http://your-public-ip-or-address)

Well this is the end of this lengthy tutorial. I hope you got what you expected from it. Thanks for bearing with me.

PS: uWSGI + NGINX + Django is highly customizable to meet any large scale requirements. That being said, core optimization still lies at application level. How you code and make use of Django ORM or Raw SQL query, etc. will help you further.

