---
title: How to self-host a Hugo web app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T18:10:07.000Z'
originalURL: https://freecodecamp.org/news/my-latest-self-hosted-hugo-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Self-hosted-Hugo.png
tags:
- name: containerization
  slug: containerization
- name: FreeBSD
  slug: freebsd
- name: Hugo
  slug: hugo
- name: self hosting
  slug: self-hosting
seo_title: null
seo_desc: 'By Jared Wolff

  After hosting with Netlify for a few years, I decided to head back to self hosting.
  There are a few reasons for that, but the main reasoning was that I had more control
  over how things worked.

  In this post, I''ll show you my workflow fo...'
---

By Jared Wolff

After hosting with Netlify for a few years, I decided to head back to self hosting. There are a few reasons for that, but the main reasoning was that I had more control over how things worked.

In this post, I'll show you my workflow for deploying my [Hugo](https://gohugo.io) generated site ([www.jaredwolff.com](https://www.jaredwolff.com)). 

Instead of using what most people would go for, I'll be doing all of this using a FreeBSD Jails-based server. Plus I'll show you some tricks I've learned over the years on bulk image resizing and more.

Let's get to it.

## Where to host?


If you want to host your own service, you'll need a server. That's where a VPS provider like Digital Ocean or Vultr comes in. I've been a fan and have used Digital Ocean for a while now.

To set up a new server here are some steps:


1. Login to Digital Ocean. If you don’t have Digital Ocean and would like to support this blog click [here](https://m.do.co/c/9574d3846a29) to create an account.
2. Go to `Account Settings` -> `Security` and make sure you have an SSH key setup.
3. Create a new FreeBSD droplet. Make sure you use the UFS version ![Create Droplet](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.41.21_AM.png) ![Choose FreeBSD 12.1 UFS](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.43.21_AM.png)
4. Make sure you select the $5 a month plan. For simple installs, this is more than enough! ![$5 Plan](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.44.13_AM.png)
1. Make sure your SSH key is selected ![Select SSH key](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.45.26_AM.png)
1. Finally click that green **Create Droplet** button! ![Create droplet](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.45.24_AM.png)
5. SSH in once you’re done: `ssh root@<yourserverip>`

## Setting up your FreeBSD server with Bastille

![images/bastille.png](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/bastille.png)

Up until recently, everything was running on a Docker based platform using [Exoframe](https://github.com/exoframejs/exoframe). It was easy and almost brainless. 

The downside was that Docker takes up wayyyy too many resources. Plus managing files within a Docker container is as much or more work than hosting it natively. Oh, and have you checked how much space Docker has been using on your machine lately? On my development machine its was about 19GB of space. ?

So what's the alternative?

FreeBSD Jails using Bastille.

I've been playing with Bastille for a few months now. The more I use it, the more it makes 100% sense.

Bastille allows you to create (now) portable lightweight FreeBSD based jails. These jails are "containers" that have virtually no overhead. There's no daemon (the operating system is the "daemon"!). Plus, jails are secure compared to the can of worms that Docker is. Yes, you may have to compile and port some utilities. Most though are already supported in FreeBSD's package manager `pkg`.

In this section you'll learn how to get a jail running with `caddy` so you can securely host your site.

Let's keep the momentum going!

Once you get the IP address for your server, you should login:

    ssh root@123.456.789.10

You should get a MOTD message and an `sh` prompt. Woo!

    FreeBSD 12.1-RELEASE-p2 GENERIC

    Welcome to FreeBSD!
    ...

    #

Let's install a few important bits using `pkg` (FreeBSD's package manager):

    pkg install restic rsync bastille

We'll be using `restic` for backups, `rsync` for transferring files and `bastille` for jail setup.

You also have to set up some static routes in your `pf.conf`. Here's an example of mine:

```shell
ext_if="vtnet0"

# Caddy related
caddy_addr=10.10.2.20

set block-policy return
scrub in on $ext_if all fragment reassemble
set skip on lo

table <jails> persist
nat on $ext_if from <jails> to any -> $ext_if

# container routes
rdr pass inet proto tcp from any to port 80 -> $caddy_addr port 8880
rdr pass inet proto tcp from any to port 443 -> $caddy_addr port 4443

# Enable dynamic rdr (see below)
rdr-anchor "rdr/*"

block in all
pass out quick modulate state
antispoof for $ext_if inet
pass in inet proto tcp from any to any port ssh flags S/SA keep state
```

This is a standard `pf.conf` file for `bastille`.  Make sure you edit `caddy_addr` to the IP you chose.

Now let's start the firewall. You will get kicked out of your `ssh` session:

```
sysrc pf_enable="YES"
service pf start
```

Then let's get some `bastille` configuration out of the way:

```
# set up bastille networking
sysrc cloned_interfaces+=lo1
sysrc ifconfig_lo1_name="bastille0"
service netif cloneup

# bootstrap the base jail and start bastille
bastille bootstrap 12.1-RELEASE update
sysrc bastille_enable="YES"
service bastille start
```

This will set up your networking, and fetch the latest default base jail you'll use later.

Next, let's set up the jail:

```
bastille create caddy 12.1-STABLE 10.10.2.20
bastille start caddy
```

Then install `caddy`

```
#install the binary
fetch https://github.com/caddyserver/caddy/releases/download/v1.0.4/caddy_v1.0.4_freebsd_amd64.tar.gz
tar xvf caddy_v1.0.4_freebsd_amd64.tar.gz caddy
bastille cp caddy caddy /usr/local/bin/
rm caddy

#create the caddy user
bastille cmd caddy pw useradd caddy -m -s /usr/sbin/nologin

#install ca root file
bastille pkg caddy install ca_root_nss
```

When installing `ca_root_nss` , `pkg` will have to initialize. Accept the prompts. Once you're done here we'll move on to the next step!

Once installation is complete, we should also configure `caddy` to start on boot. The easiest way to do that is use this `rc.d` script:

```sh
#!/bin/sh

# $FreeBSD: head/net/caddy/files/caddy.in 452063 2017-10-14 12:58:24Z riggs $
#
# PROVIDE: caddy
# REQUIRE: LOGIN
# KEYWORD: shutdown
#
# Add the following lines to /etc/rc.conf.local or /etc/rc.conf
# to enable this service:
#
# caddy_enable (bool):	Set to NO by default.
#				Set it to YES to enable caddy.
# caddy_user (user):		Set user to run caddy.
#				Default is "caddy".
# caddy_group (group):	Set group to run caddy.
#				Default is "caddy".
# caddy_conf (path):		Path to caddy configuration file.
#				Default is /usr/local/etc/caddyfile.conf

. /etc/rc.subr

name=caddy
rcvar=caddy_enable

load_rc_config $name

: ${caddy_enable:="NO"}
: ${caddy_user:="caddy"}
: ${caddy_group:="caddy"}
: ${caddy_conf:="/usr/local/etc/caddyfile.conf"}
: ${caddy_log:="/home/caddy/caddy.log"}
: ${caddy_env:="CADDYPATH=/home/caddy/"}
: ${caddy_https_port:="4443"}
: ${caddy_http_port:="8880"}

pidfile="/var/run/caddy.pid"
procname="/usr/local/bin/caddy"
command="/usr/sbin/daemon"
command_args="-f -p ${pidfile} /usr/bin/env ${caddy_env} ${procname} -agree -http-port ${caddy_http_port}  -https-port ${caddy_https_port} -conf=${caddy_conf} -log=${caddy_log} ${caddy_args}"
extra_commands="reload"

start_precmd=caddy_startprecmd
reload_cmd=caddy_reloadcmd

caddy_startprecmd()
{
      if [ ! -e ${pidfile} ]; then
              install -o ${caddy_user} -g ${caddy_group} /dev/null ${pidfile};
      fi
}

caddy_reloadcmd()
{
      kill -s USR1 $(cat ${pidfile})
}

run_rc_command "$1"
```

Remove the `caddy` executable if you haven't already. Then create a new file with `vi`. This will be your `rc.d` script!

```
vi caddy
```

Then paste the contents of the above script in there, save and exit.

Make sure the file is executable by using `chmod` and copy to the Caddy container.

```
chmod +x caddy
bastille cp caddy caddy /usr/local/etc/rc.d/
```

Finally, we'll need a Caddyfile. Here's an example of one:

```
stage.jaredwolff.com {
  tls hello@jaredwolff.com
  log /home/caddy/stage.jaredwolff.com.log
  root /var/www/stage.jaredwolff.com/
  gzip
  log stderr
}
```

`log` refers to this site specific access log.

`root` refers to where the root `public` folder is on your machine. In my case it's the common `/var/www/<name of site>`. Set your paths and remember them. We'll need them later!

To have Caddy generate certs for this subdomain, you'll have to set the *tls* option. An email is all that's needed.

For more on the Caddyfile structure [check out the documentation.](https://caddyserver.com/docs/caddyfile)

Make a file called `caddyfile.conf` and copy it to `/usr/local/etc/` in your Caddy container:

```
vi caddyfile.conf
# Paste your caddyfile contents and save
bastille cp caddy caddyfile.conf /usr/local/etc/
```

You should now redirect your DNS to the server IP. That way Caddy can generate/fetch the correct certificates. Then you can start Caddy with:

```
bastille service caddy caddy start
```

You can check the log at `/usr/home/caddy/caddy.log` to make sure that your domain provisioned correctly.

***Side note:*** Getting setup with SSL certs is tough at first, especially if you're migrating from another server. Your site will have to go down for a little bit while you switch your DNS settings and start `caddy`. 

(That's if you're using standard `caddy` 1.0. You can also use the DNS provider [plugins here](https://github.com/caddyserver/dnsproviders) which make things a little easier.)

Now that we have `caddy` up and running it's time to copy our `hugo` generated assets over using `rsync`. We're off to the next step!

## *Make* building and deploying easy

![images/make.png](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/make.png)

I spend a ton of time writing C code, and that means I spend tons of time using Makefiles. For many, `make` (or `gmake` for GNU make) is the bane of their existence. 

For building and deploying, `make` makes it easy to create reusable recipes. That way you know you can deploy with confidence every time.

My Makefile borrows from the one that [Victoria Drake had posted](https://victoria.dev/blog/a-portable-makefile-for-continuous-delivery-with-hugo-and-github-pages/) not too long ago. I changed it up a bit to match my needs. 

Let's take a tour and see what's inside:

```Makefile
.POSIX:

HUGO_VERSION := 0.66.0

OPTIMIZED_DIR := optimized
CONTENT_DIR := content
DEST_DIR := public

SERVER := 123.456.789.10
USER := user
```

The first section contains all the variables that I use to tell the functions later on what to do. It also has a reference to the `.POSIX` target. This means that the Makefile will be as portable between different versions of `make`.

Then, I popped in some logic to determine whether I'm deploying to *stage* or *production:*

```Makefile
# Set the place where it's deployed to.
ifdef PRODUCTION
$(info Building for production. ?)
TARGET := www
else
$(info Building for development. ?)
BASEURL := --baseURL "https://stage.jaredwolff.com"
TARGET := stage
endif
```

By default, recipes below will use the development workflow. To use the production workflow, you can invoke `make` like this:

```Makefile
PRODUCTION=1 make build
```

This does add some extra friction to the deploy process. It's a good step though. That way you're sure the deploy is going to the right place!

```Makefile
# Full path
DEPLOY_DIR := /usr/local/bastille/jails/caddy/root/path/to/$(TARGET).jaredwolff.com
```
Using the `TARGET` variable above, I then define the path to my server assets. I'm using Bastille to organize my jails, so the path is extra long. (yea, lengthly long) This allows us to use `rsync` to deploy the files with ease.

Now here come the fun bits. To do a full bulk resize, I'm using the `wildcard` functionality of the Makefile.

```Makefile
IMAGES := \
$(wildcard $(CONTENT_DIR)/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/images/*.JPG) \
$(wildcard $(CONTENT_DIR)/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.JPG) \
```

In this case it will create a huge space delimited list of every image that is within my content directory. The biggest drawback of this method is that it's not space tolerant. An easy fix to this is to make sure that all my photos do not have spaces.

Here's a quick and dirty bash command. You can use to rename files that have spaces and replace them with '_' characters:

```Makefile
for f in *\ *; do mv "$f" "${f// /_}"; done
```

Next, we rename these entries so the prefix is now the target directory. This will be useful when we want to resize:

```Makefile
OPTIMIZED_IMAGES := \
$(subst $(CONTENT_DIR)/,$(OPTIMIZED_DIR)/,$(IMAGES))
```

Now check out the `optimize` recipe:

```Makefile
.PHONY: optimize
optimize: build $(OPTIMIZED_IMAGES)
@echo "? Optimizing images"
rsync -r $(OPTIMIZED_DIR)/ $(DEST_DIR)/
du -sh $(CONTENT_DIR)/
du -sh $(DEST_DIR)/

$(OPTIMIZED_IMAGES):
convert -strip -compress JPEG -resize '730>' $(subst $(OPTIMIZED_DIR)/,$(CONTENT_DIR)/,$@) $@
```

It first calls the `build` recipe and then also the `$(OPTIMIZED_IMAGES)` recipe. The later will optimize the image using the `convert` command from [Imagemagick](https://imagemagick.org/script/convert.php). In this case I'm only resizing files that are larger than 730px wide. Change yours accordingly so you can reap the benefits of an [optimized site.](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/)

After resizing, the recipe uses `rsync` to copy the files from the `OPTIMIZED_DIR` to `DEST_DIR.`

If we take a look at the `build` recipe, I first building the assets. Then, I copy the photos from the `content` dir to `optimized` dir. The nice thing is that `rsync` will only move files that have changed. Thus it doesn't have to copy the files over and over and over again every time you build.

Finally, the `deploy` recipe.

```Makefile
.PHONY: deploy
deploy:
@echo rsync to $(DEPLOY_DIR)
@rsync -r --del public/ $(USER)@$(SERVER):$(DEPLOY_DIR)/
@echo making restic snapshot
@scp scripts/backup.sh $(USER)@$(SERVER):/root/backup.sh
@ssh $(USER)@$(SERVER) sh /root/backup.sh $(DEPLOY_DIR)
@echo "? Site is deployed!"
```

You can see again that I'm using rsync to sync the contents of `public/` to the server. Make sure you set the `USER` , `SERVER` and `DEPLOY_DIR`. In my case `DEPLOY_DIR` comes out to `/usr/local/bastille/jails/caddy/root/var/www/www.jaredwolff.com`

When you do finally get a successful deploy you can double check everything is in the correct place. Then once everything looks good you can start up your caddy server using:

```
bastille service caddy caddy start
```

`deploy` will also do something extra handy here. It will deploy my `restic` backup script and run it. I'll talk about this more in the backup section.

All in all, here's the full Makefile:

```Makefile
.POSIX:

HUGO_VERSION := 0.66.0

OPTIMIZED_DIR := optimized
CONTENT_DIR := content
DEST_DIR := public

SERVER := 155.138.230.8
USER := root

# Set the place where it's deployed to.
ifdef PRODUCTION
$(info Building for production. ?)
TARGET := www
else
$(info Building for development. ?)
BASEURL := --baseURL "https://stage.jaredwolff.com"
TARGET := stage
endif

# Full path
DEPLOY_DIR := /usr/local/bastille/jails/caddy/root/var/www/$(TARGET).jaredwolff.com

IMAGES := \
$(wildcard $(CONTENT_DIR)/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/images/*.JPG) \
$(wildcard $(CONTENT_DIR)/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.JPG) \

OPTIMIZED_IMAGES := \
$(subst $(CONTENT_DIR)/,$(OPTIMIZED_DIR)/,$(IMAGES))

.PHONY: all
all: build optimize

.PHONY: clean
clean:
rm -rf public/
rm -rf optimized/

.PHONY: serve
serve:
@hugo serve -D

.PHONY: ssh
ssh:
@ssh $(USER)@$(SERVER)

.PHONY: build
build:
@echo "? Generating site"
hugo --gc --minify -d $(DEST_DIR) $(BASEURL)
rsync -av --del -f"+ */" -f"- *" $(CONTENT_DIR)/ $(OPTIMIZED_DIR)/

.PHONY: optimize
optimize: build $(OPTIMIZED_IMAGES)
@echo "? Optimizing images"
rsync -r $(OPTIMIZED_DIR)/ $(DEST_DIR)/
du -sh $(CONTENT_DIR)/
du -sh $(DEST_DIR)/

$(OPTIMIZED_IMAGES):
convert -strip -compress JPEG -resize '730>' $(subst $(OPTIMIZED_DIR)/,$(CONTENT_DIR)/,$@) $@

.PHONY: deploy
deploy:
@echo rsync to $(DEPLOY_DIR)
@rsync -r --del public/ $(USER)@$(SERVER):$(DEPLOY_DIR)/
@echo making restic snapshot
@scp scripts/backup.sh $(USER)@$(SERVER):/root/backup.sh
@ssh $(USER)@$(SERVER) sh /root/backup.sh $(DEPLOY_DIR)
@echo "? Site is deployed!"
```

There are a few other handy nuggets in there you may want to use.  `clean`, `serve` and `ssh` have been very helpful when testing and connecting.

In the end you'll have a two step deploy process. The first generates your site with optimized images. The second is deploying to a server for static hosting.

## Incremental Backup

![images/Backup.png](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Backup.png)

After discovering [Restic](https://restic.net) I've been sold on how handy it has been for all my incremental backup needs. In the case of my server, I'm using to back up the root folder of my site. That way, if I need to roll back, I can do so with a few short steps.

Here's how you can set up a local `restic` repo.

### Setting it up

Initializing the repo is simple. The most important part is making sure you **don't lose/forget your password!**

```
    # restic init -r /root/backups
    enter password for new repository:
    enter password again:
    created restic repository 32e14c7052 at /root/backups

    Please note that knowledge of your password is required to access
    the repository. Losing your password means that your data is
    irrecoverably lost.
```

Set the `RESTIC_PASSWORD` environment variable to avoid entering your password. To make it permanent you'll have to place `export RESTIC_PASSWORD="Your password here!"` within the `.profile` file in `/root/`.

### Backing Up

Invoking `restic` over SSH is tough. So our next best bet?

Transfer a (very brief) shell script to the server and run it after a deploy. Here's the contents of what I'm using today:

```sh
#!/bin/sh
export RESTIC_PASSWORD="Your password here!"
restic backup $1 -r /root/backups/
```

***Side note:*** As I sit here and look at this script, for security reasons you can replace "Your password here!" with $2 which is the second argument to the script. That way you don't need to commit/push the password stored in a static file!

This first sets your backup password. Then it runs `restic` using the first command line argument as the path. So, to run a backup with this script, it would look something like this:

```
./backup.sh /path/to/your/public/folder/
```

**Note:** you do need to initialize your `restic` backup *before* you start backing up. It will barf at you otherwise!

In my case I'm placing the incremental backups on a different folder of my machine. That way they're easily accessible and *fast*.

### Viewing your backups

To view your backups you can run the following command:

    # restic snapshots -r /root/backups -g paths -c
    enter password for repository:
    repository e140b5e4 opened successfully, password is correct
    snapshots for (paths [/usr/local/bastille/jails/caddy/root/var/www/www.jaredwolff.com]):
    ID        Time                 Host         Tags
    --------------------------------------------------
    d3328066  2020-03-10 00:30:58  vultr.guest
    f3360819  2020-03-10 04:03:03  vultr.guest
    231dd134  2020-03-10 04:44:00  vultr.guest
    3c1be26a  2020-03-10 04:56:19  vultr.guest
    e96c947c  2020-03-10 05:03:00  vultr.guest
    34c3682a  2020-03-10 14:01:37  vultr.guest
    fbccdb8c  2020-03-10 14:04:26  vultr.guest
    9ce11146  2020-03-10 15:38:49  vultr.guest
    046b3da3  2020-03-10 15:47:06  vultr.guest
    9c28d4bc  2020-03-10 15:48:25  vultr.guest
    469dc228  2020-03-10 15:48:54  vultr.guest
    6f78af72  2020-03-10 17:00:21  vultr.guest
    29ad17b2  2020-03-10 20:18:23  vultr.guest
    ed22ce1f  2020-03-10 20:20:24  vultr.guest
    9c8c1b03  2020-03-11 13:56:40  vultr.guest
    b6cfcfec  2020-03-11 14:08:14  vultr.guest
    e8546005  2020-03-11 14:27:22  vultr.guest
    49a134fe  2020-03-17 00:47:58  vultr.guest
    c0beb283  2020-03-18 20:44:52  vultr.guest
    --------------------------------------------------

You can use this list to determine if you need to roll back a deploy.

### Restoring

Restoring from a backup, especially in a live environment, needs to be quick. After viewing your backups you can restore a specific backup by using its *ID*.

```
restic restore d3328066
```

This will restore the files back to the backup made on *2020-03-10 00:30:58.* Awesome. Plus it won't overwrite every single file. It will only apply the differences from the current state and the stored state.

## Conclusion

We've covered a ton of ground in this post. You've learned how to:

- Deploy your own server using Vultr
- Use Bastille to create Container-like Jails
- Set up Caddy to serve static file assets with TLS
- Deploy the files using a fairly simple Makefile and `rsync`
- Back up after every deploy using `restic`

In the end we have a robust, secure and simple platform for hosting static files and services. 

Stay tuned as there are more posts like this coming your way soon! In the meantime check out my [other posts.](https://www.jaredwolff.com/blog/) 

Thanks for reading and see you next time! ?

**You can find other articles like this at [www.jaredwolff.com.](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/)**



