---
title: 'How to manage Ubuntu Snaps: the stuff no one tells you'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-19T13:23:00.000Z'
originalURL: https://freecodecamp.org/news/managing-ubuntu-snaps
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/lego.svg
tags:
- name: Linux
  slug: linux
- name: 'snaps '
  slug: snaps
- name: System administration
  slug: system-administration
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: Canonical’s Snaps are definitely the real deal. The secure and portable
  Linux package management system is more than a geeky tool for showing off your tech
  creds. Just consider the growing list of companies that have already bought in and
  are providi...
---

[Canonical’s Snaps](https://snapcraft.io/) are definitely the real deal. The secure and portable Linux package management system is more than a geeky tool for showing off your tech creds. Just consider the [growing list](https://snapcraft.io/store) of companies that have already bought in and are providing their desktop software through snaps, including Blender, Slack, Spotify, Android Studio, and Microsoft’s (Microsoft!) Visual Studio Code. And don’t forget that the real growth of the snap system is in the world of IoT devices and servers rather than desktops.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-138.png)
_The snapcraft.io site: where snap developers and users meet_

But as the popularity of snaps grows — some new Linux distros come with the snapd service installed by default — you might be forgiven for wondering how you’re supposed to make them work. Don’t get me wrong: there are all kinds of web-based guides for finding, installing, and removing snaps. And there are places developers can go for help building their applications as snaps. But right now I’m talking about _configuring_ their behavior or _troubleshooting_ when things go wrong.

Just for the record, you search for new snaps to install using something like:

```
snap find aws
```

When you find a package you like, you install it using:

```
snap install aws-cli
```

Oh, and you delete ‘em with remove.

```
snap remove aws-cli
```

There. You can’t say I never taught you anything. But that’s not what this article is about. What we are going to talk about is real management stuff, like changing configurations or troubleshooting things that broke.

## Understanding the snap file system

Well, how’s that going to be different from the way you’d normally do it on Linux? Configuration files are usually going to be in _/etc/_, processes will reveal their deepest secrets through _systemctl_, and logs will find their way to _/var/log/_.

Not so fast there, pilgrim. That’s not always how things work in Snapland. You see, a snap is really nothing more than a single compressed file (named using the _.snap_ extension) containing the entire file system needed for running a package. These files are never actually decompressed and “installed,” but are mounted dynamically at run time and exposed to the user as a virtual environment.

This means that the resources used by a program might not actually exist on the host system. Thus, for example, the Nextcloud snap creates its own versions of Apache and MySQL for its backend. So if, say, you want to configure a new virtual host in _/etc/apache2/sites-available/_ or create a new MySQL user the traditional way, you’re out of luck.

The advantages of this approach are significant: installation and setup will generally be much smoother and you’re far less likely to run into dependency issues and conflicts. But it also at least appears to mean that you get less access to the vital organs that power your software.

So, then, where does everything snappy happen? Take a look through your host file system for yourself: you’ll probably find more snap directories than you can shake a stick at (should you be so inclined). Here are the directories the snap install process probably created:

/snap/  
/var/snap/  
/var/lib/snapd/  
/home/username/snap/

That many? What for? Let’s go through those one at a time. Feel free to poke around your own Linux machine to see all this for yourself.

The actual _.snap_ files are kept in the _/var/lib/snapd/snaps/_ directory. When running, those files will be mounted within the root directory _/snap/_. Looking over there — in the /snap/core/ subdirectory — you’ll see what looks like a regular Linux file system. It’s actually the virtual file system that’s being used by active snaps.

```
ls /snap/core/current
bin   dev  home  lib64  meta  opt   root  sbin  srv  tmp  var
boot  etc  lib   media  mnt   proc  run   snap  sys  usr  writable
```

And here’s a subdirectory containing (read-only) configuration files used by the Nextcloud snap. That’ll only be there, of course, if you’ve installed Nextcloud (_snap install nextcloud_).

```
ls /snap/nextcloud/current/conf/
httpd.conf  mime.types  ssl.conf
```

Ok. Now what about _/var/snap/_? Very much like traditional inhabitants of _/var/_, the files within _/var/snap/_ contain various forms of user data and log files — the kind of data that’s generated and consumed by applications during operations. This example shows directories for data used by some desktop-related snaps, including the AWS CLI and the Slack team communication tool. (OK, technically speaking, the AWS CLI isn’t a desktop tool.)

```
ls /var/snap
aws-cli  core18           gnome-system-monitor  gnome-calculator
brave    gnome-3-26-1604  gnome-characters      gtk-common-themes
core     gnome-3-28-1804  gnome-logs            slack
```

Dive deep into the subdirectories within _/var/snap/_on your machine and see what you can discover.

That leaves just the _~/snap_ directory that exists in a user’s home directory on at least some Linux file systems. It’ll contain directories using some of the names you’ll see in /var/snap. What’s going on in there?

```
ls ~/snap
aws-cli  brave  gnome-calculator  slack
```

As far as I can tell, these directories are meant to store versioned data related to settings used by your user account.

## Snap administration tools

So far I’ve shown you how to find various classes of data kept in configuration files (within _/var/snap/_), virtual file systems (_/snap/_), and collections of user settings (_~/snap_). I also showed you where _not_ to look — _/var/lib/snapd/_ — which is where the .snap files themselves live; nothing to see here, move along now.

Now what about actual administration? This is a bit more complicated. Some snaps — like Nextcloud — expose a fully-featured admin interface. I talk about that in [my Administrating Nextcloud as a Snap article](https://www.freecodecamp.org/news/snapd-nextcloud/). But it seems that the simplicity of snaps sometimes means that there just isn’t much hands-on configuration that’s possible.

However, that’s not always the case. But first, you’ll need to know about _snap services_. Some more complex applications require multi-layer software stacks. Nextcloud, for instance, creates and manages its own versions of Apache, MySQL, PHP, and Redis. Each one of those “layers” is, in snap terms, called a service.

If any snaps installed on your machine have their own services, you’ll be able to list them along with their status using this snapd command:

```
snap services
Service                    Startup  Current   Notes
nextcloud.apache           enabled  active    -
nextcloud.mdns-publisher   enabled  active    -
nextcloud.mysql            enabled  active    -
nextcloud.nextcloud-cron   enabled  active    -
nextcloud.nextcloud-fixer  enabled  inactive  -
nextcloud.php-fpm          enabled  active    -
nextcloud.redis-server     enabled  active    -
nextcloud.renew-certs      enabled  active    -
```

You can also control the run and startup status of a service. This example will stop Nextcloud’s Apache service and ensure that it doesn’t launch when the system reboots (although, just remember that this will disable Nextcloud — you probably don’t want to do that):

```
snap stop --disable nextcloud.apache
```

You can also use systemctl to manage snap service processes:

```
systemctl status snap.nextcloud.apache
```

If your snap includes at least one service, you can view its logs using snapd:

```
snap logs nextcloud
```

You can also specify a particular service:

```
snap logs nextcloud.mysql
```

For some snaps (like Nextcloud), snapd makes useful configurations available from the command line. You can display available settings using _snap get_:

```
snap get nextcloud
Key        Value
mode       production
nextcloud  {...}
php        {...}
ports      {...}
private    {...}
```

Drop down a level by adding the name of a specific setting. This example shows us that Nextcloud is currently listening on only ports 80 (HTTP) and 443 (HTTPS).

```
snap get nextcloud ports
Key          Value
ports.http   80
ports.https  443
```

You could change a setting using the _set_ command. This one would tell Nextcloud to listen on port 8080 for insecure HTTP requests instead of 80.

```
snap set nextcloud ports.http=8080
```

Snapd also offers some system-wide configuration settings that are [described here](https://docs.snapcraft.io/system-options/87), documentation of [environment variables is maintained here](https://docs.snapcraft.io/environment-variables/7983), and information on [keeping your snaps updated can be found here](https://docs.snapcraft.io/keeping-snaps-up-to-date/7022).

All that’ll get you started when things need fixing. So get to it.

_Looking for more? You might enjoy my_ [_books and Pluralsight courses_](https://bootstrap-it.com/) _on Linux, AWS, and Docker-related topics._

