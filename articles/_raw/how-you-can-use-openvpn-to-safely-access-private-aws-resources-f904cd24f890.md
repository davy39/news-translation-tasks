---
title: How you can use OpenVPN to safely access private AWS resources
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2018-06-12T22:49:42.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-use-openvpn-to-safely-access-private-aws-resources-f904cd24f890
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MgRSD6yOMt1f4JpfGBrfOg.jpeg
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: vpn
  slug: vpn
seo_title: null
seo_desc: 'This article was adapted from part of my new Pluralsight course, “Connecting
  On-prem Resources to your AWS Infrastructure.”

  Do you sometimes need to connect to resources you’ve got running on Amazon Web Services?
  Accessing your public EC2 instances u...'
---

_This article was adapted from part of my new Pluralsight course, “[Connecting On-prem Resources to your AWS Infrastructure](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton).”_

Do you sometimes need to connect to resources you’ve got running on Amazon Web Services? Accessing your public EC2 instances using SSH and encrypting your S3 data is, for all intents and purposes, secure enough. But what about getting into a back-end RDS database instance or working with AWS-based data that’s not public? There are all kinds of reasons why admins keep such resources out of reach of the general public. But if you can’t get at them when you need, what good are they likely to do you?

So you’ll need to find a safe and reliable way around the ACLs and security groups protecting your stuff. One solution I cover in [my “Connecting On-prem Resources to your AWS Infrastructure” course on Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) is Direct Connect. But if Direct Connect’s price tag is a budget-buster for your company, then some kind of VPN tunnel might do the trick.

### What’s a Virtual Private Network?

Virtual Private Networks (VPNs) are often used to allow otherwise restricted network activity or anonymous browsing. But that’s not what this article is about.

A VPN is a point-to-point connection that lets you move data securely between two sites across a public network. Effectively, a tunnel can be designed to combine two geographically separated private sites into one single private network. In our context, that would mean connecting your local office network with the AWS VPC that’s hosting your private resources.

There are two ways to do this:

* A managed VPN Connection built on top of an AWS Virtual Private Gateway
* Using your own VPN.

This article will focus on the do it yourself method.

#### The OpenVPN Access Server

As the name suggests, [OpenVPN](https://openvpn.net/) is an open source project, and you’re always able to download the free community edition and set things up on your own VPN server. But the OpenVPN company also provides a [purpose-built OpenVPN Access Server as an EC2 AMI](https://openvpn.net/index.php/access-server/on-amazon-cloud.html) which comes out of the box with AWS-friendly integration and automated configuration tools.

From what I can see, launching the AMI within your AWS VPC and opening it up for controlled remote connections has pretty much become the “right” way to get this job done.

What does it cost? If you’re only testing things out and don’t plan to access the VPN using more than two connections at a time, then the AMI itself is free. You’ll still be on the hook for the regular costs of an EC2 instance, but if your account is still eligible for the Free Tier, then you can get that for free, too.

Once you put your VPN into active production, the license you purchase will depend on how many concurrent connections you’ll need. [This page](https://docs.openvpn.net/getting-started/software-license-pricing/) has the details you’ll need.

Here’s what we’re going to do in this guide:

* Select, provision, and launch an Ubuntu AMI with OpenVPN Access Server pre-installed into my VPC
* Access the server using SSH and configure the VPN
* Set up an admin user
* Set up a local machine as an OpenVPN client and connect to a private instance in my AWS VPC

Ready?

### Launching an OpenVPN Access Server

From the EC2 dashboard — and making sure we’re in the right AWS region — launch an instance to act as our VPN server. Rather than using one of the Quick Start AMIs, I’ll click on the AWS Marketplace tab and search for “openvpn access server”. OpenVPN provides a number of official images that are tied to licenses offering escalating numbers of connected clients.

I’m going to go with this Ubuntu image that works through a “Bring Your Own License” arrangement. As I wrote earlier, we won’t actually need a license for what we’re going to be doing.

![Image](https://cdn-media-1.freecodecamp.org/images/XTboqBVguN8FTVoSwQrnrGZuCkC97Y0vtyUu)
_OpenVPN Access Server AMIs available from the AWS Marketplace_

Selecting the AMI opens a popup telling us how much this image will cost us per hour using various instance types and EBS storage choices. Those are only regular AWS infrastructure costs, however, and don’t include license fees.

![Image](https://cdn-media-1.freecodecamp.org/images/HRL623PHVls25j6yVZW80nurh7rWJIDv3mSq)
_OpenVPN Access Server AMI costs — billed directly by AWS_

When it comes to instance type, I’ll downgrade to a t2.micro to keep it within the free tier. A busy production server might require a bit more power.

Because I’m going to want to start up a second instance in the same subnet in a few minutes, I’ll select, say, “us-east-1b” from the Configure Instance Details page, and make a note for later.

![Image](https://cdn-media-1.freecodecamp.org/images/6R-q7kO9yezjWvSf99cER4Xh4bA3zs5azISg)
_Choose a subnet and note for later_

Now the Security Group page is where the OpenVPN AMI settings really shine. We’re presented with a security group that opens up everything we’ll need. Port 22 is for SSH traffic into the server, 943 is the port we’ll use to access the admin GUI, 443 is TLS-encrypted HTTP traffic, and OpenVPN will listen for incoming client connections on port 1194.

![Image](https://cdn-media-1.freecodecamp.org/images/-h1D6QojwaZIVezNitxZDgaZqiLCbwFJ3FjS)
_The Security Group that comes with the OpenVPN AMI_

**Note**: If practical, it would normally be a good idea to tighten those rules so only requests from valid company IP address ranges are accepted, but this will be fine for short-term testing.

From here, I’ll review my settings, confirm that I’ve got the listed SSH encryption key, and pull the trigger.

Once the instance is launched, I’ll be shown important login information — including the fact that the user account we’ll use to SSH into the server is called openvpnas — and a Quick Start guide. I’ll also receive an email containing links to the same information.

Back in the EC2 instances console, while the new machine finishes booting, we’re shown our public IP address. If we would ever need to reboot the instance, there’s no guarantee that we’d get that same IP again, which could cause a reasonable amount of mayhem. So it’s a good idea to assign the instance an Elastic IP.

To do that, I’ll click Elastic IPs and then Allocate new address. Note the new address and close the page. Now, with that address selected, click Actions, and “Associate Address”. I’ll click once in the Instance box and my OpenVPN instance — with its helpful tag — is listed. I only need to select it, click “Associate” and I’m done. From now on, that will be the permanent public IP for accessing our server.

![Image](https://cdn-media-1.freecodecamp.org/images/rQJ5leTI2CTmKdeHxJ8dacPyBz4ueo19IiFe)
_Associate your new Elastic IP address with your instance_

### Accessing the server

I’ll paste the public IP address into the terminal as part of my SSH command that calls the key pair I set for this instance.

```
ssh -i KeyPairName.pem openvpnas@<PublicIPAddress>
```

If you’re accessing from a Windows or macOS machine, things might work a bit differently, but the documentation will give you all the help you’ll need.

Before I leave the Instances console, however, I’ll perform one more important function. With the OpenVPN instance selected, I’ll click Actions and then Networking and then “Change Source/Dest checking”. I’ll make sure that checking is disabled. Nothing much will be possible unless I do this.

Now over to my SSH session. As soon as it begins, I’m confronted by the OpenVPN EULA license agreement, and then the setup wizard. If you need to change a setting later you can always run the wizard again using this command:

```
sudo ovpn-init — ec2.
```

Most of the wizard’s defaults will work fine, but it’s worth quickly explaining what’s happening. Here are the questions and some color commentary where necessary:

```
primary Access Server node? yes [You’d answer no if you were setting up a backup or failover node.]
specify the network interface and IP address to be used by the Admin Web UI [1 — For all interfaces; can be changed to static later.]
specify the port number for the Admin Web UI [default]
specify the TCP port number for the OpenVPN Daemon [default]
Should client traffic be routed by default through the VPN? [no--That’s   not the kind of VPN we’re building here. What we’re doing is only about getting remote clients safely and securely into our VPC. The same applies to client DNS traffic.]
Should client DNS traffic be routed by default through the VPN? [no] 
Use local authentication via internal DB? [no — can be useful, but we’ll use Linux/AWS authentication for simplicity.]
Should private subnets be accessible to clients by default? [yes — that’s the whole point of the VPN, after all.]
login to the Admin UI as “openvpn”? [yes]
Provide OpenVPN Access Server license key [Unnecessary for testing.]
```

When the wizard completes, I’m shown some connection information and advised to install the network time daemon NTP. That won’t be necessary on this Ubuntu box, as it’s already installed and running by default.

As I mentioned earlier, I will need to give the openvpn user a password so I can use it to log into the web GUI. I do that as sudo with the passwd command.

```
sudo passwd openvpn
```

That’s all the server-side stuff we’ll need. Now I’m going to use a browser to log into the web GUI. I use our server’s public IP address with the secure https prefix, followed by slash and admin.

```
https://<PublicIPAddress>/admin
```

You’ll get a “Your connection is not private” warning because we’re using a self-signed certificate rather than one provided by a Certificate Authority.

![Image](https://cdn-media-1.freecodecamp.org/images/s-fDsz3rKP9Pf7JqKYbPfyAlhUl4YHfSBz1m)
_This is normal when using self-signing certificates_

That’s not a problem for us, since we’re only exposing our VPN to select users from within our company, and they should be able to trust our certificate. So I’ll click through the warning, sign in, and agree to the EULA .

Feel free to spend some time exploring the features provided by the OpenVPN admin console on your own.

![Image](https://cdn-media-1.freecodecamp.org/images/VtQgAuVOfhbLTYII1HOdxO5cJiyQo44JSomR)
_The OpenVPN admin console_

### Setting up a VPN client

Right now, however, I’m going to open the client UI page using the web access address we were shown before, but this time without the slash admin. This is nothing more than a login screen where you can authenticate using the same openvpn user as before. (You can always create new users back in the admin console.)

Behind the login screen, there’s just this set of links with directions for installing the OpenVPN client app on any of those platforms. The final link, however, is called “Yourself.”

![Image](https://cdn-media-1.freecodecamp.org/images/GFJB-8yTJ0xVtQ1AXnsD1W0DApG3I6JVVXgz)
_The OpenVPN client page_

Clicking it will prompt you to download and save a file called client.ovpn. This file contains the configuration settings to match the server and the actual keys we’ll use to authenticate. You definitely want to treat this file with care so it doesn’t fall into the wrong hands. That would include not sending it through plain email across unencrypted connections.

I’ll open the file locally and copy the contents. Then, in a shell within a Linux virtual machine running in my local network, I’ll create a new file called client.ovpn and paste the contents in. If you had clicked through to the “OpenVPN for Linux” link in the client UI earlier, you would have seen that the only additional step necessary was to install OpenVPN using the Apt package manager — or Yum if you’re on a CentOS or Red Hat machine. Well that’ll take just one command. When it’s done its job, we’ll be all set.

```
nano client.ovpnsudo apt updatesudo apt install openvpn
```

Next we’ll open the VPN connection. As root — using sudo — I’ll type openvpn with the config flag pointing to the client.ovpn configuration file I just created.

```
sudo openvpn — config client.ovpn
```

When prompted to authenticate, use the openvpn account along with the password you created for it back on the server.

Now I’ll open a second shell session on my local client so I can try to ssh in to the OpenVPN server using its _local_ IP address — something that would be impossible without a working VPN connection.

First though, run ip a to list all the network interfaces active on this machine.

```
ip a
```

Besides your local network, you should also see one called tun0. This interface was created by OpenVPN and will usually lie within the 172.16.x.x range.

I’ll ssh into the remote server using my private key — which, of course, needs to exist locally — and the server’s _private_ IP address. If it works, you’ll have yourself a VPN!

```
ssh -i KeyPairName.pem openvpnas@<PrivateIPAddress>
```

Finally, I’ll demonstrate that the VPN, as it’s currently configured, will allow us access to other private resources within our Amazon VPC. This could be useful if, for instance, you’ve got a database instance running in the VPC that you can’t expose to the public network.

I’m going to launch a standard Ubuntu EC2 instance but I _won’t_ give it a public IP. I’ll specify the same us-east-1b subnet we used for the OpenVPN server to keep things simple. The security group I’ll use will permit SSH access through port 22 but nothing else.

Once that’s running, I’ll note its private IP address and head back to my local client. Once I’m sure the instance is fully launched, I’ll ssh in using the same private key, the “ubuntu” username — since that’s the default for normal Ubuntu EC2 instances — and the private address I just copied.

Again. If it works, you’ll have a fully-configured VPN connection into your AWS private resources. Savor the moment.

Don’t forget to shut down all your servers and release your Elastic IP address when you’re done using them. You don’t want to incur costs unnecessarily.

_This article was adapted from part of my new Pluralsight course, “[Connecting On-prem Resources to your AWS Infrastructure](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton).” There’s lots more where that came from at my [Bootstrap IT site](https://bootstrap-it.com), including links to my book, Linux in Action, and a hybrid course called [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) that’s made up of more than two hours of video and around 40% of the text of Linux in Action._

