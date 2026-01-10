---
title: Using the Let’s Encrypt Certbot to get HTTPS on your Amazon EC2 NGINX box
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-01T06:29:11.000Z'
originalURL: https://freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Cd2NBjQD8Luwbu1Z23n5QQ.png
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Karan Thakkar

  Let’s Encrypt is a new Certificate Authority which provides free SSL certificates
  (up to a certain limit per week). It came out of beta around a month back and is
  supported by a wide array of browsers.

  Certbot is the official Let’s E...'
---

By Karan Thakkar

Let’s Encrypt is a new _Certificate Authority_ which provides free SSL certificates (up to a certain limit per week). It came out of beta around a month back and is supported by a [wide array of browsers](https://community.letsencrypt.org/t/which-browsers-and-operating-systems-support-lets-encrypt/4394).

**Certbot** is the official Let’s Encrypt client, developed by the [Electronic Frontier Foundation](https://www.eff.org/). It makes automatically fetching and deploying SSL/TLS certificates for your web server a relatively straight forward process.

Lets get started.

### **Step #1**

Make sure that you have opened up ports 80 (HTTP) and 443 (HTTPS) in your instance **Security Group** to public. Certbot will use this to establish connections while generating your certificates.

Note that I spent far too much time to figure out why I couldn’t generate a certificate, while the only issue was that I hadn’t opened up port 443 in my EC2 instance Security Group.

![Image](https://cdn-media-1.freecodecamp.org/images/K0p2kFeBVDFczsI2Xh4PwHf7YJCLRaThGpDn)
_**Inbound** settings in EC2 Security Group_

### Step #2

Setup your domain’s **CNAME Record** to point to the **public DNS** of your EC2 instance.

![Image](https://cdn-media-1.freecodecamp.org/images/IMIqPlaLo5Voda4d8iwhE1ox27vrr19CPemW)
_**Public DNS** value in your EC2 instance description_

![Image](https://cdn-media-1.freecodecamp.org/images/dRD-X8-N9a7wnq9Z81WtxO1sIV4B8V4cfMm0)
_This setting would point **api.mydomain.com** to my EC2 instance_

### Step #3

Install Certbot on your instance. Based on your operating system and server, you can find out how to install it on [Certbot’s homepage](https://certbot.eff.org). For NGINX on **Ubuntu 14.04**, use [this](https://certbot.eff.org/#ubuntutrusty-nginx).

```
wget https://dl.eff.org/certbot-auto
chmod a+x certbot-auto
```

Run this command in your home directory:

```
/home/ubtuntu
```

### Step #4

Stop any existing servers running on the port 80 and 443, since those are used by Certbot to verify your domain and generate certificates.

You can restart those servers once you have finished generating the certificates.

### **Step #5**

Run the following command to generate certificates for your domain:

```
./certbot-auto certonly --standalone -d xyz.yourdomain.com
```

You can generate certificates for multiple domains using this approach.

### **Step #6**

Change your NGINX configuration in **/etc/nginx/nginx.conf** to [enable SSL](http://nginx.org/en/docs/http/configuring_https_servers.html):

```
http {
  ##
  # Logging Settings
  ##
  
  access_log /var/log/nginx/access.log;
  error_log /var/log/nginx/error.log;
  
  server {
    listen 80;
    server_name xyz.yourdomain.com;
    location / {
      # Redirect any http requests to https
      return 301 https://$server_name$request_uri;
    }
  }
  
  server {
    listen 443 ssl;
    server_name xyz.yourdomain.com;
    ssl_certificate /etc/letsencrypt/live/xyz.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/xyz.yourdomain.com/privkey.pem;
    add_header Strict-Transport-Security “max-age=31536000”;
    location / {
      proxy_pass http://127.0.0.1:3000;
    }
  }
  
}
```

The [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/Security/HTTP_strict_transport_security) (HSTS) header ensures that any internal links that are not HTTPS will [automatically be routed](https://loune.net/2016/01/https-with-lets-encrypt-ssl-and-nginx) to the HTTPS version during a HTTPS session.

### **Step #7**

Lastly, reload your NGINX configuration:

```
sudo service nginx reload
```

Congratulations! Your site **xyz.example.com** is now successfully running on HTTPS.

**NOTE**: Let’s Encrypt certificates are only valid for 3 months after issue. So every 3 months, renewal is required. Here’s how you can automate this [using a cron job](https://loune.net/2016/01/https-with-lets-encrypt-ssl-and-nginx/).

If this post helped you, hit the heart button below. ? And if it didn’t, please leave a comment to tell me how I can make it better.

PS: Thanks to [Narendra N Shetty](https://www.freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76/undefined) for proofreading and giving suggestions.

![Image](https://cdn-media-1.freecodecamp.org/images/lcR6uQdCciRYcGIs1Pl2XihJOQeYci-1axVE)

[Karan Thakkar](https://twitter.com/geekykaran) is the Frontend Lead at [Crowdfire](https://www.freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76/undefined) — _Your super-smart marketing sidekick_. His [article](https://bit.ly/hackingtwitter) has been previously [featured](https://bit.ly/geekyonhuffpo) on [The Huffington Post](https://www.freecodecamp.org/news/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76/undefined). He likes trying out new technologies in his spare time and has built [Tweetify](https://karanjthakkar.com/projects/tweetify) (using React Native) and [Show My PR’s](https://showmyprs.com) (using Golang).

Other articles written by him:

[**How I grew from 300 to 5k followers in just 3 weeks**](https://blog.markgrowth.com/how-i-grew-from-300-to-5k-followers-in-just-3-weeks-2436528da845)  
[_#GrowthHacking my Twitter account for @Crowdfire Twitter Premier League_blog.markgrowth.com](https://blog.markgrowth.com/how-i-grew-from-300-to-5k-followers-in-just-3-weeks-2436528da845)[**An Illustrated Guide for Setting Up Your Website Using Github & Cloudflare**](https://medium.freecodecamp.org/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465)  
[_Easy to Setup, Instant Deploy, Free HTTPS, HTTP2/SPDY Suport, Custom Redirect, Browser Cache Expiration, HTTP Secure…_medium.freecodecamp.org](https://medium.freecodecamp.org/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465)

