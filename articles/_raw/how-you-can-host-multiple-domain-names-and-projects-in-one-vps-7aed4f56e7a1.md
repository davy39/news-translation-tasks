---
title: How to host multiple domain names and projects on one server
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-29T16:50:07.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FT9uL7NRg2iep6-e
tags:
- name: nginx
  slug: nginx
- name: General Programming
  slug: programming
- name: servers
  slug: servers
- name: 'tech '
  slug: tech
- name: Web Hosting
  slug: web-hosting
seo_title: null
seo_desc: 'By BinHong Lee

  NGINX is one magical tool


  _Photo by [Unsplash](https://unsplash.com/@imgix?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">imgix on <a href="https://unsplash.com?utm_source=medium&utm_medium=referral"
  re...'
---

By BinHong Lee

#### NGINX is one magical tool

![Image](https://cdn-media-1.freecodecamp.org/images/0*FT9uL7NRg2iep6-e)
_Photo by [Unsplash](https://unsplash.com/@imgix?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">imgix</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

I own multiple domain names, and each one hosts a different side project. For the longest time, everything that required ‘hosting’ was hosted on Heroku. But their free tier can be quite limited, it can also get costly quickly if you are paying for each separate project. So instead, I decided to explore putting all of them together using NGINX (recommended to me by [Jane Manchun Wong](https://www.freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1/undefined)).

### Required Resources

#### Virtual Private Server (VPS)

You’ll need a virtual server such as [DigitalOcean](https://www.freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1/undefined) or EC2 by [AWS](https://www.freecodecamp.org/news/how-you-can-host-multiple-domain-names-and-projects-in-one-vps-7aed4f56e7a1/undefined). Personally I uses [Vultr](https://www.vultr.com/?ref=7358373) (here’s the [non-referral link](http://vultr.com/)) which costs me about $2.50 / month.

#### Domain Names

You will need to register a few domain names. Assuming that you probably already have them, make sure your domain names are pointing at the name servers of your VPS. There should be a DNS section in your domain name service dashboard where you can select “custom DNS” or something similar. If you are not sure what the nameservers of your VPS are, you should be able to find that info easily through a simple search of “nameserver” + VPS service name.

### Setting up NGINX

#### Installation and basic setup

_Reference from [How To Install Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04)_

Run the following commands through SSH-ing into the VPS. It will install NGINX, set firewall rules allowing it, and set NGINX to autostart on boot.

#### Configuration setup

_Reference from [Host Multiple Domains on One Server/IP with Apache or nginx](https://geekflare.com/multiple-domains-on-one-server-with-apache-nginx/)_

The default virtual.conf location should be at /etc/nginx/conf.d/virtual.conf. I recommend backing up the default file before making any changes. (If it doesn’t exist, you can just create it.) Edit the file to look something like the following:

Here are a few things to look at:

* _server_ block — Each of these should represent each different domain or subdomain in use.
* _root_ — This is the location where the (HTML) files are loaded from.
* _server_name_ — (sub)domain name(s) that should load these specific files.
* _proxy_redirect_ — in cases where you are redirecting a specific subdomain to an active server, you will want to add this and put the IP location after it. (For local servers, either [_http://127.0.0.1:port_](http://127.0.0.1:port) or [_http://localhost:port_](http://localhost:port) should work as intended.)

```
sudo systemctl restart nginx
```

After you are done, restart the server so the new configurations will be loaded and applied.

### Cloning and linking

Now remember, since you have your directory pointing at /opt/htdocs/_websiteName_, your initial thought might be to clone your projects into these folders. This can work, but it’s not ideal since many operations in these folders require root access to really do anything.

Instead, you can clone them into your user folder or anywhere else like you normally would, and then create a soft link to connect the path to your repository folder. Something like this:

```
git clone git@github.com:binhonglee/binhonglee.github.io ~/websitesudo ln -s ~/website /opt/htdocs/binhong
```

Of course, when you are cloning a Node.js static site folder (ReactJS, Angular or Vue.js), you will want to install (`npm install`) and build (`npm run-script build`) them. Then link the _./build_ folder instead of the base level of the cloned repository. (Similarly for Jekyll sites, but use the _./_output_ folder instead.) As for active servers, just make sure your server is running on the same port as it is listed in the configuration file.

### Set up HTTPS with certbot

Thanks to Let’s Encrypt, you can now get free and easy HTTPS certificates. With the introduction of certbot, everything just got even easier!

_Reference from [How To Secure Nginx with Let’s Encrypt on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)_

Just run the above for all your domain and subdomain names and certbot will take care of everything. If you were to renew the certs, you can run the following so the certbot will help you renew your SSL certificate.

```
sudo certbot renew --dry-run
```

### Updating everything

Now that you have everything up and running, you might be thinking, well there seems to be an awful lot to remember if/when I need to update something. Unfortunately, that’s kinda true, but we can always make it easier by adding a script that does it for us.

Here is how one would look:

Thanks for reading! Let me know if you have any questions in the comments below.

### About me

At the time of writing, I work at Apple Inc. in the role of Siri Language Engineer as an Independent Contractor through AdvantisGlobal. I spend a lot of my free time experimenting and building new things with technologies I find fun and interesting. Follow my exploration journey [here](https://binhong.me/blog) or on [GitHub](https://github.com/binhonglee).

### Other References

* [nginx proxy pass redirects ignore port](https://serverfault.com/questions/363159/nginx-proxy-pass-redirects-ignore-port) on [serverfault](https://serverfault.com)
* [Continue SSH background task/jobs when closing SSH](https://superuser.com/questions/632205/continue-ssh-background-task-jobs-when-closing-ssh) on [superuser](https://superuser.com/)

