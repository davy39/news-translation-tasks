---
title: How to Deploy a Node.js App – From Server Setup to Production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-01T21:39:43.000Z'
originalURL: https://freecodecamp.org/news/deploy-nodejs-app-server-to-production
coverImage: https://cdn-media-2.freecodecamp.org/w1280/603a54d9a675540a22924662.jpg
tags:
- name: deployment
  slug: deployment
- name: nginx
  slug: nginx
- name: node
  slug: node
- name: servers
  slug: servers
seo_title: null
seo_desc: 'By Yiğit Kemal Erinç

  In this tutorial, we are going to learn everything we need to know before deploying
  a Node app to a production server.

  We will start by renting a server on Digital Ocean. Then we''ll configure this server,
  connect to it, install N...'
---

By Yiğit Kemal Erinç

In this tutorial, we are going to learn everything we need to know before deploying a Node app to a production server.

We will start by renting a server on Digital Ocean. Then we'll configure this server, connect to it, install Nginx and configure it, pull or create our Node app, and run it as a process. 

As you can see, there is a lot to do and it will be an action-packed tutorial. So let's get started without wasting any time.

You should have some basic knowledge on how the Terminal works and how to work in Vi/Vim before getting started. If you are not familiar with basic commands, I would advise you to read up on them a bit. 

I will run the commands in MacOS. If you want to follow this tutorial in Windows, you can use Powershell or some other Unix emulator of your choice.

Although I will use Node.js as the platform of our example application, most of the steps are the same for any web application.

## Why Digital Ocean?

I choose Digital Ocean because it is cheap and the interface is really easy to use, compared to the likes of AWS. Also, a $100 credit is included in the GitHub student pack so you do not have to pay anything for a couple of months. It is ideal for deploying a course or hobby project.

It has a concept called Droplets, which is basically your share of a server. You can think of the server as an apartment in which you own or rent a flat.

Droplets work with the help of Virtual Machines which run on the server. So a Droplet is your Virtual Machine on a shared server. Since it is a VM, its CPU and memory share can be easily increased, usually by throwing more money at your provider.

## How to Create a Digital Ocean Project

![This image has an empty alt attribute; its file name is image-3.png](https://erinc.io/wp-content/uploads/2021/02/image-3.png)

I am assuming that you have already signed up and logged in to Digital Ocean before proceeding. We should first create a project that will contain our droplets. Let's click on the new project button on the left side menu. It will ask you to name your project.

![This image has an empty alt attribute; its file name is Screen-Shot-2021-02-22-at-13.35.06.png](https://erinc.io/wp-content/uploads/2021/02/Screen-Shot-2021-02-22-at-13.35.06.png)

Enter whatever name you want. It will also ask you if you want to move any resources, but for now just click Skip – we will create the droplet later.

## How to Create a Droplet on Digital Ocean

Let's create our droplet by clicking the Get Started button.

![This image has an empty alt attribute; its file name is image-4-1024x593.png](https://erinc.io/wp-content/uploads/2021/02/image-4-1024x593.png)

After clicking the button, it will ask us to choose a VM image.

![This image has an empty alt attribute; its file name is Screen-Shot-2021-02-22-at-13.12.43-1024x567.png](https://erinc.io/wp-content/uploads/2021/02/Screen-Shot-2021-02-22-at-13.12.43-1024x567.png)
_Choosing an Image_

On this page, I will select Ubuntu 20.04 since it is the latest LTS version at the time I am writing this post. LTS means "Long Term Support". It is best to go with the LTS version for actual projects, because the provider guarantees that it will be supported and maintained for a long time. This means you will not have problems in the long run.

I have chosen Ubuntu, and would recommend it to you since it is the most commonly used Linux distribution. This means it's also the easiest to find answers to your future questions.

You can also choose to have a Dedicated CPU if you need it. If you are building your own startup or any business project, I would recommend reading this [post](https://www.digitalocean.com/docs/droplets/resources/choose-plan/) which contains detailed instructions about how to pick the right option for you.

I will go with the cheapest option in this case. 

Then you will need to select a Datacenter region. You should pick the one that is closest to you to minimize network delay.

![This image has an empty alt attribute; its file name is image-2-1024x519.png](https://erinc.io/wp-content/uploads/2021/02/image-2-1024x519.png)
_Select a Datacenter_

Next let's select SSH Keys as the Authentication Method, since it is much more secure than basic password authentication. 

![This image has an empty alt attribute; its file name is image-5-1024x459.png](https://erinc.io/wp-content/uploads/2021/02/image-5-1024x459.png)
_Authentication Method_

To connect to the server we need to generate a new SSH key on our own device and add it to Digital Ocean.

## How to Generate an SSH Key

I will generate the key on my macOS device. If you are using Windows you can refer to [this](https://phoenixnap.com/kb/generate-ssh-key-windows-10) article. Open your terminal and move into the ssh folder:

```
cd ~/.ssh
```

Then create your SSH key:

```
ssh-keygen
```

If your computer says that it does not know this command, you should install it via brew.

![This image has an empty alt attribute; its file name is image-7-1024x140.png](https://erinc.io/wp-content/uploads/2021/02/image-7-1024x140.png)

It will ask you to name the file and enter a passphrase. Do not enter a name, just press enter and go with the defaults. You should have these files generated. I have named mine digital-ocean-ssh in this screenshot, so do not get confused by that.

```
❯ lsid_dsa      id_rsa      known_hosts
```

Our public key is the `id_dsa` and the `id_rsa` is our private key. If you forget which one is private, you can always print one of them to see.

## How to Add Your SSH Key to Digital Ocean

Now we want to copy our public key and upload it to Digital Ocean so they will know which key to use in authentication.

![This image has an empty alt attribute; its file name is image-9-1024x149.png](https://erinc.io/wp-content/uploads/2021/02/image-9-1024x149.png)

Copy this whole key including the ssh-rsa part.

Click on "New SSH Key":

![This image has an empty alt attribute; its file name is image-10.png](https://erinc.io/wp-content/uploads/2021/02/image-10.png)

Paste the key in the textbox that appears after you click the button and you should see your SSH key.

![This image has an empty alt attribute; its file name is image-11.png](https://erinc.io/wp-content/uploads/2021/02/image-11.png)

## How to Connect to the Server

We will use the terminal to connect to our server with SSH. You can also take a look at Termius for a nice interface if you want.

Run this command in your terminal after replacing the IP_ADDRESS with your server's IP address (you can look it up from Digital Ocean's panel).

```
ssh root@IP_ADDRESS
```

If everything goes well, now you should be in the server's terminal. We have successfully connected to server. If there is any error, you can debug it by running the command with the "-v" option or "-vv" for even more verbosity.

## How to Set Up the Server

We need to do some initial setup before deploying the Node app to the server.

### Update and Upgrade Software

We want to update the server's software to make sure we are using the latest versions. 

Many servers are vulnerable to attacks because they are using older versions of software with known vulnerabilities. Attackers can search for the vulnerabilities in those software and try to exploit them in order to gain access to your server. 

You can update Ubuntu's software using the **"apt update"** command.

```
apt updateHit:1 https://repos.insights.digitalocean.com/apt/do-agent main InReleaseGet:2 http://mirrors.digitalocean.com/ubuntu focal InRelease [265 kB]      Hit:3 http://mirrors.digitalocean.com/ubuntu focal-updates InRelease                Get:4 http://security.ubuntu.com/ubuntu focal-security InRelease [109 kB]Hit:5 http://mirrors.digitalocean.com/ubuntu focal-backports InReleaseFetched 374 kB in 1s (662 kB/s)                          Reading package lists... DoneBuilding dependency tree       Reading state information... Done96 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

If you read the message, it says that "96 packages can be upgraded". We have installed the new software packages but we have not upgraded our software to those versions yet. 

To do that, let's run another command:

```
apt upgrade
```

Type y when it prompts you and it will upgrade the software.

### Create a User

We have connected to the server as the root user (the user with the highest privileges). Being the root is dangerous and can open us up to vulnerabilities. 

Therefore we should create a new user and not run commands as root. Replace `$username` with a username of your choice.

```
whoamiroot
```

```
adduser $username
```

You need to enter a password for the user. After that point, it will ask a bunch of questions, so just input y until the prompting is over.

The new user has been created but we also need to add this new user to the "sudo" group so that we can perform any action we need.

```
usermod -aG sudo $USERNAME
```

We add group with the `-aG` (add group) option, and we add the group name `sudo` to our username.

We are still root, so let's switch our user to the newly created user, using the `su` (switch user) command.

```
su $USERNAME
```

After this point, if you run **`whoami`** command, you should see your username. You can confirm the existence of the sudo group by running this command:

```
sudo cat /var/log/auth.log
```

Only superusers can view this file and OS will ask for your user password after you run this command.

### Copy the SSH Key

We have successfully created the user but we have not enabled SSH login for this new user yet. 

Therefore, we have to copy the public key that we previously created on our local computer and paste it into this user's SSH folder so SSH can know which key should it use to authenticate our new user.

```
mkdir -p ~/.ssh
```

The `-p` argument creates the directory if it does not exist.

```
vi ~/.ssh/authorized_keys
```

We will use vi or vim to create a file and call it **`authorized_keys`**.

Copy your public key (`id_dsa` file) then press "i" to go into insert mode. Then just paste it into this file with CMD + V.

Press esc to quit insert mode, type **:wq** to save and quit.

If you have any problems about using Vim-Vi, you can check out [one of the many tutorials](https://www.freecodecamp.org/news/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae/) that explain how to use it.

### Connect to Server as New User

Now we should be able to connect to the server without any problems using ssh. You can use this command to connect, just remember to insert your username and `IP_ADDRESS`.

```
ssh $USERNAME@IP_ADDRESS
```

If you are having any problems at this point, you should just delete the droplet and start over. It does not take a lot of time to start over but debugging server problems can be difficult.

### How to Disable Root Login

It is a good practice to disable Root login as a security precaution, so let's do that now.

It can be useful to change the file permission just in case so that we won't run into problems regarding permissions in the future.

```
chmod 644 ~/.ssh/authorized_keys
```

Let's now open our `sshd_config` file:

```
sudo vi /etc/ssh/sshd_config
```

Find this line and change the yes to no in the same way we did earlier with vi.

```
PermitRootLogin no
```

Save and quit vi.

## How to Install Node.js and Git

We can now go ahead and install Node.js and Git:

```
sudo apt install nodejs npm
```

```
sudo apt install git
```

We are now ready to create a Node app and run it. You can either pull your Node project from Github or create a Node app here just to test if it works.

Move to a directory of your choice and create an **"app.js"** file:

```
sudo vi app.js
```

You can paste the following snippet into your **app.js** file:

```
const express = require('express');const app = express();const port = 3000;app.get('/', (req, res) => {        res.send('Hello World');});app.listen(port, () => console.log(`Example app listening on port ${port}!`));
```

Now we can run it with the command:

```
node app.js
```

You should see "Example app listening on port 3000!" on your terminal.

We can confirm that it is working by sending a request to our server:

```
GET http://IP_ADDRESS:3000/
```

Send this request either from an HTTP client like Postman or your browser and you should see the "Hello World" message.

At this point, you should notice that something is wrong: Regular users do not know how to send requests to port 3000.

We should redirect the requests that come to our web server from our IP to port 3000. We can accomplish this with the help of Nginx.

![This image has an empty alt attribute; its file name is image-16.png](https://erinc.io/wp-content/uploads/2021/02/image-16.png)

## How to Install and Configure Nginx

We will use Nginx as a Reverse Proxy to redirect the requests to our Node app.

![This image has an empty alt attribute; its file name is image-14-1024x531.png](https://erinc.io/wp-content/uploads/2021/02/image-14-1024x531.png)
_Nginx as a Reverse Proxy_

Let's install Nginx:

```
sudo apt install nginx
```

Start the Nginx service:

```
sudo service nginx start
```

We can test to see if it is working by sending a request to our server's IP address from the browser. Type your server's IP address to your browser and you should see this:

![This image has an empty alt attribute; its file name is image-15-1024x231.png](https://erinc.io/wp-content/uploads/2021/02/image-15-1024x231.png)

It is important to know that Nginx serves from **"/var/www/html"** by default and you can find this HTML file in that directory as well.

I also advise you to create a folder under "/var/www", call it app, and move your Node app to that folder so it will be easy to find.

### How to Configure the Nginx Reverse Proxy

We will edit the Nginx config file to configure a reverse proxy:

```
sudo vi /etc/nginx/sites-available/default
```

In this file you need to find the location / block and change it as follows:

```
location / {                # First attempt to serve request as file, then                # as directory, then fall back to displaying a 404.                proxy_pass http://127.0.0.1:3000/;        }
```

The `proxy_pass` directive proxies the request to a specified port. We give the port that our Node application is running on.

Let's restart Nginx so the changes can take effect:

```
sudo service nginx reload
```

After this step, we should be able to see the message when we send a request to our server. Congratulations, we have completed the minimum number of steps to deploy a Node app! 

![This image has an empty alt attribute; its file name is Screen-Shot-2021-02-24-at-01.10.33-1024x67.png](https://erinc.io/wp-content/uploads/2021/02/Screen-Shot-2021-02-24-at-01.10.33-1024x67.png)

But I still advise you to complete the following bonus step as well, as I believe it's quite important.

If you can't see the hello world message, you can check if your app and Nginx are running and restart them.

## How to Run your App as a Process

We do not want to start our application manually every time something goes wrong and our app crashes. We want it to restart on its own. Also, whenever the server starts, our app should start too. 

To make this happen, we can use PM2. Let's install PM2 and configure it.

```
sudo npm i -g pm2
```

We are installing pm2 globally by using the "-g" option so that it will be accessible from every folder.

```
pm2 start app.js
```

This makes sure that the app will restart if it exits due to an error.

Let's save the current process list.

```
pm2 save
```

We also need to convert it to a daemon that runs whenever the system starts:

```
pm2 startup systemd
```

![This image has an empty alt attribute; its file name is image-17.png](https://erinc.io/wp-content/uploads/2021/02/image-17.png)

As a reminder, in this tutorial, I'm using the commands for Ubuntu. If you are using any other Linux distro, you should replace `systemd` in this command.

We can confirm that the service is getting restarted by rebooting the server and sending a request without running app.js by hand:

```
sudo reboot
```

After sending a request as we did earlier, you should be able to see the hello world message.

## Conclusion

In this tutorial we started from scratch, rented a server for ourselves, connected to it, and configured it in a way that it serves our Node.js app from port 80. 

If you have followed along and were able to complete all steps, congratulations! You can be proud of yourself, as this was not the easiest topic :). I hope that you have learned a lot. Thank you for your time.

I am planning to explore this topic further by connecting the server to a domain name, then connecting it to CircleCI for continuous integration. I'll also go through the required steps to make your Node.js/React app production ready. This post had already gotten long enough, though, so those topics are reserved for another post :)

If you have enjoyed reading and want to get informed about my future posts, you can subscribe to my [personal blog](https://erinc.io/). You can see my previous posts there if you are interested in reading more. I usually write about web development-related topics.  

