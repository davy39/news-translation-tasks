---
title: How to Secure your Network Connections Using OpenVPN
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-08T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/securing-your-network-connections-using-openvpn
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/openvpn.png
tags:
- name: Linux
  slug: linux
- name: OpenVPN
  slug: openvpn
- name: Security
  slug: security
seo_title: null
seo_desc: 'They tell us we live in a hyper-mobile world. Not that I’d know: I rarely
  leave my home office. But of course I only get to enjoy the comforts of my home
  office because all the server resources I could possibly need are available remotely.

  Apparently...'
---

They tell us we live in a hyper-mobile world. Not that I’d know: I rarely leave my home office. But of course I only get to enjoy the comforts of my home office because all the server resources I could possibly need are available remotely.

Apparently I’m not alone. Almost everyone whose work touches IT will access their professional tools from remote locations from time to time. And given that the public networks through which you access those remote locations are by their nature insecure, you’re going to want to carefully control those connections.

Website encryption is about making sure that the data consumed by your remote clients is reliably transferred and invisible to anyone who might be lurking on the connecting network. VPNs, by sharp contrast, focus on making sure that the data consumed by your remote clients is reliably transferred and invisible to anyone who might be lurking on the connecting network. Do you see the difference? Neither do I.

In fact, there are all kinds of technologies devoted to securing network communication, and the principle of _defence in depth_ teaches us that you should never rely on just one. So here’s where you’ll learn about _adding new_ layers of protection for your remote activities. Specifically, using encryption to build a virtual private network (VPN) tunnel to permit secure and invisible remote connections.

## Building an OpenVPN tunnel

My [Linux in Action book](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9) - from which this article is excerpted - talks a lot about encryption. SSH and SCP can protect data transferred through remote connections (chapter 3), file encryption can protect data at rest (chapter 8), and TLS/SSL certificates can protect data in transit between websites and client browsers (chapter 9). But sometimes your requirements demand protection across a broader range of connections, because sometimes you’ve got different kinds of work to do.

F’rinstance? Some members of your team need to work from the road using public WiFi hotspots. It’s definitely not smart to assume that random WiFi access points are secure, but your people do need a way to connect with company resources. VPNs to the rescue.

A properly designed VPN tunnel provides a direct connection between remote clients and a server in a way that hides data as it’s transferred across an insecure network. But so what? You’ve already seen lots of tools that can do that using encryption. The real value of a VPN is that once you’ve opened a tunnel, it’s possible to connect remote networks as though they’re all together locally. In a way, you’re circumventing that dodgy coffee shop hot spot.

Using such an extended network, admins can get their work done on their servers no matter where they might happen to be. But more importantly, as you can see in the figure, a company with resources spread through multiple branch offices can make them all both visible and accessible to all the teams who need them…wherever they are.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-19.png)
_Tunnel connecting remote private connections through a public network_

The mere existence of a tunnel alone doesn’t guarantee security. But one of a number of encryption standards can be incorporated into the design, making things a great deal better. Tunnels built with the open source OpenVPN package use the same TLS/SSL encryption you’ve already seen in use elsewhere. OpenVPN is not the only available choice for tunnelling, but it is among the best known, and it’s widely assumed to be a bit faster and likely more secure than the alternative Layer 2 Tunnel Protocol using IPsec encryption.

So that your team can safely connect with each other from out on the road or between multiple campuses, you’re going to build an OpenVPN server to permit sharing both applications and access to the server’s local network environment. To make it work, it should be sufficient to fire up two VMs or containers. One to play the role of a server/host and the other of the client.

Building a VPN involves quite a few steps, so taking a few moments to think about the big picture of how this is going to work will probably be worthwhile.

## Configuring an OpenVPN server

Before getting started, here’s a helpful tip. If you’re going to follow along with this process on your own — and I strongly recommend that you do — you’ll probably find yourself working with multiple terminal windows open on your desktop, each logged into a different machine. Take it from me: at some point you’re going to enter a command into the wrong window and totally mess up your environment.

You can use the hostname command to change the machine name displayed on the command line to something that will visually remind you where you are. Once that’s done, you’ll need to exit the server and log back in again for the new setting to take effect.

```
ubuntu@ubuntu:~# hostname OpenVPN-Server
ubuntu@ubuntu:~$ exit 
<Host Workstation>$ ssh ubuntu@10.0.3.134
ubuntu@OpenVPN-Server:~# 
```

Following that approach to assign appropriate names to each of the machines you’re working with should help you keep track of where you are.

## Prepare your server for OpenVPN

Installing OpenVPN on your server requires two packages: openvpn and, to manage the encryption key-generation process, easy-rsa. CentOS users should, if necessary, first install the epel-release repository the way you did back in chapter 2. To give you an easy way to test access to a server application, you could also install the Apache webserver (apache2 for Ubuntu and httpd on CentOS).

While you’re setting up your server, you might as well do it right and activate a firewall that blocks all ports besides 22 (SSH) and 1194 (the default OpenVPN port). This example illustrates the way that will work on Ubuntu’s ufw, but I’m sure you still remember CentOS’ firewalld from chapter 9.

```
ufw enable
ufw allow 22
ufw allow 1194
```

To permit internal routing between network interfaces on the server you’ll need to uncomment a single line (net.ipv4.ip_forward=1) in the /etc/sysctl.conf file. This will allow remote clients to be redirected as needed once they’re connected. To load the new setting, run sysctl -p.

```
nano /etc/sysctl.conf
sysctl -p
```

The server environment is now all set up, but there’s still a way to go before you’re ready to flip the switch.

## Generate encryption keys

When you installed OpenVPN, a /etc/openvpn/ directory was automatically created, but there isn’t a whole lot in it just yet. However, both the openvpn and easy-rsa packages come with sample template files that you can use as a base for you configuration. To jump start the certification process, copy the easy-rsa template directory from /usr/share/ to /etc/openvpn/ and then change to the new easy-rsa/ directory.

```
cp -r /usr/share/easy-rsa/ /etc/openvpn
cd /etc/openvpn/easy-rsa
```

The first file you’ll work with is called simply vars, and contains environment variables that easy-rsa will use when it generates its keys. You will want to edit the file to substitute your own values for the sample defaults that are already there. Here’s what my file would look like:

```
export KEY_COUNTRY=”CA”
export KEY_PROVINCE=”ON”
export KEY_CITY=”Toronto”
export KEY_ORG=”Bootstrap IT”
export KEY_EMAIL=”info@bootstrap-it.com”
export KEY_OU=”IT”
```

Running the vars file will pass its values to the shell environment from where they’ll be incorporated into the contents of your new keys. When that’s done, the script will encourage you to run the clean-all script to delete any existing contents in the /etc/openvpn/easy-rsa/keys/ directory.

```
cd /etc/openvpn/easy-rsa/
. ./vars 
NOTE: If you run ./clean-all, I will be doing a rm -rf on /etc/openvpn/easy-rsa/keys
```

Naturally, your next step will be to run that clean-all script…followed by build-ca that will use the pkitool script to create your root certificate. You’ll be asked to confirm the identification settings provided by vars.

```
./clean-all
./build-ca
Generating a 2048 bit RSA private key
```

Next, the build-key-server script, since it uses the same pkitool script along with the new root certificate, will ask you the same confirmation questions to generate a key pair. The keys will be given names based on the argument you pass — which, unless you’re running multiple VPNs on this machine, would normally be server, as in this example.

```
./build-key-server server
[…]
Certificate is to be certified until Aug 15 23:52:34 2027 GMT (3650 days)
Sign the certificate? [y/n]:y
1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated
```

OpenVPN will use parameters generated using the Diffie-Hellman algorithm (by running build-dh) to negotiate authentication for new connections. The file that will be created here does not need to remain secret, but must have been generated using the build-dh script against the RSA keys that are currently active. If you create new RSA keys at some time in the future, you’ll also need to update the Diffie-Hellman file.

```
build-dh
```

Your server-side keys will now have been written to the /etc/openvpn/easy-rsa/keys/ directory, but OpenVPN doesn’t know that. By default OpenVPN will lookfor them in /etc/openvpn/, so copy them over.

```
cp /etc/openvpn/easy-rsa/keys/server* /etc/openvpn
cp /etc/openvpn/easy-rsa/keys/dh2048.pem /etc/openvpn
cp /etc/openvpn/easy-rsa/keys/ca.crt /etc/openvpn
```

## Prepare client encryption keys

As you’ve already seen, TLS encryption uses matching key pairs, one installed on the server and the other on a remote client. That means you’re going to need client keys, and our old friend pkitool is just the thing to cook some up. This example, run while still in the /etc/openvpn/easy-rsa/ directory, passes client as an argument to generate files called client.crt and client.key.

```
./pkitool client
```

The two client files, along with the original ca.crt file that’s still in the keys/ directory, will now have to be securely transferred to your client. Because of their ownership and permissions, this might be a bit complicated. The simplest approach is to manually copy the contents of the source file (and nothing but those contents) in a terminal running on your PC’s desktop (by highlighting the text, right-clicking over it, and selecting copy from the menu) and then pasting it into a new file of the same name you create in a second terminal logged into your client.

But anyone can cut and paste. Instead, think like an admin — especially since you won’t always have access to a GUI where cutting and pasting is possible. Instead, copy the files to your user’s home directory (so a remote scp operation can access them) and then use chown to change the ownership of the files from root to your regular, non-root user so that remote scp action can work. Make sure your files are all settled and comfy for now…you’ll move them over to the client a bit later.

```
cp /etc/openvpn/easy-rsa/keys/client.key /home/ubuntu/
cp /etc/openvpn/easy-rsa/keys/ca.crt /home/ubuntu/
cp /etc/openvpn/easy-rsa/keys/client.crt /home/ubuntu/
chown ubuntu:ubuntu /home/ubuntu/client.key
chown ubuntu:ubuntu /home/ubuntu/client.crt
chown ubuntu:ubuntu /home/ubuntu/ca.crt
```

With a full set of encryption keys ready for action, you’ll need to tell your server how you want to build your VPN. That’s done using the server.conf file.

## Configure server.conf file

How are you supposed to know what the server.conf file should look like? Well, remember the easy-rsa directory template you copied over from /usr/share/? Well there are more goodies where that came from. The OpenVPN installation left a compressed template configuration file which you can copy over to /etc/openvpn/.

I’ll use the fact that the template is compressed to introduce you to a useful tool: zcat. You’re already know about printing a file’s text contents to the screen with cat, but what if the file is compressed using gzip? Of course, you could always decompress the file and cat will then be happy to print it, but that’s one or two steps too many. Instead, as you’ve probably already guessed, you can use zcat to load the decompressed text into memory all in one step. In our case, rather than print it to the screen, you’ll redirect the text to a new file called server.conf.

```
zcat \
 /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz
 > /etc/openvpn/server.conf
cd /etc/openvpn
```

Leaving out the extensive and helpful documentation that comes with the file, here’s how it might look once you’re done editing. Note that a semicolon (;) tells OpenVPN _not_ to read and execute the line that follows.

```
port 1194
# TCP or UDP server?
proto tcp
;proto udp
;dev tap
dev tun
ca ca.crt
cert server.crt
key server.key # This file should be kept secret
dh dh2048.pem
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
push “route 10.0.3.0 255.255.255.0”
keepalive 10 120
comp-lzo
port-share localhost 80 
user nobody 
group nogroup
persist-key
persist-tun
status openvpn-status.log
log openvpn.log 
;log-append openvpn.log
verb 3 
```

Let’s work through some of those one at a time.

* By default, OpenVPN works over port 1194. You can change that — perhaps to further obscure your activities, or avoid conflicts with other active tunnels. But, because it will require the least coordination between clients, 1194 is normally your best choice.
* OpenVPN can use either the Transmission Control Protocol (TCP) or User Datagram Protocol (UDP) for data transmissions. TCP might be a little bit slower, but it’s more reliable and more likely to get along with applications running at either end of the tunnel.
* You specify dev tun when you want to create a simpler and more efficient IP tunnel that transfers data content and nothing much else. If, on the other hand, you’ll need to connect multiple network interfaces (and the networks they represent) by creating an _ethernet bridge_, then you’ll have to select dev tap. If you haven’t a clue what all that means, go with tun.
* The next four lines pass OpenVPN the names of the three server authentication files and the dh2048 parameters file you created earlier.
* The server line sets the subnet range and netmask that will be used for assigning IP addresses to clients when they log in.
* The optional push “route 10.0.3.0 255.255.255.0” setting will allow remote clients to access private subnets “behind” the server. Making this work will also require network configuration on to server itself to ensure that the private subnet is aware of the OpenVPN subnet (10.8.0.0).
* port-share localhost 80 allows client traffic coming in on port 1194 to be rerouted to a local web server listening on port 80. This will be useful in our case since we’re going to use a web server to test our VPN. This will only work when proto is set to tcp.
* The user nobody and group nogroup lines should be enabled by removing the semicolons. Forcing remote clients to work as nobody and nogroup ensures that their sessions on the server will be unprivileged.
* log sets current log entries to overwrite old entries every time OpenVPN starts up, while log-append appends new entries to the existing log file. The openvpn.log itself will be written to the /etc/openvpn/ directory.

In addition, it is also very common to add client-to-client to the config file so multiple clients will be able to see each other in addition to the OpenVPN server.

Once you’re satisfied with your configuration, you’re ready to fire up the OpenVPN server.

```
systemctl start openvpn
```

Running ip addr to list your server’s network interfaces should now include a reference to a new interface called tun0. This will have been created by OpenVPN for the use of incoming clients.

```
ip addr
[…]
4: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc […]
 link/none 
 inet 10.8.0.1 peer 10.8.0.2/32 scope global tun0
 valid_lft forever preferred_lft forever
```

It is _possible_ that you’ll need to reboot the server before everything will fully function. Next stop: the client computer.

## Configuring an OpenVPN client

Traditionally, tunnels are built with at least two ends (otherwise we prefer calling them caves). Having OpenVPN properly configured on the server directs traffic into and out of the tunnel at that end. But you’ll need some kind of software running on the client side as well.

> _In this section I’m going to focus on manually configuring a Linux computer of one sort or another to act as an OpenVPN client. But that’s not the only way you might want to consume the service. OpenVPN itself maintains client apps that can be installed and used on Windows or Mac desktop/laptops, or Android and iOS smart phones and tablets. See the [https://openvpn.net](https://openvpn.net/) web site for details._

The OpenVPN package will need to be installed on the client machine, as it was on the server — although there’s no need for easy-rsa over here, because the keys you’ll use already exist. You will need to copy the client.conf template file over to the /etc/openvpn/ directory that the installation just created. This time, for some reason, the file won’t be compressed, so a regular cp will do the job just fine.

```
apt install openvpn
cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf \
 /etc/openvpn/
```

Most of the settings in your client.conf file will be fairly obvious: they’ll need to match the values used by the server. As you can see from the sample file below, one that’s unique is remote 192.168.1.23 1194 — which points the client to the server’s IP address. Again, make sure you use your server’s actual address. You should also force your client to verify the authenticity of the server certificate to prevent a possible man-in-the-middle attack. One way to do this is by adding the remote-cert-tls server line.

```
client 
;dev tap
dev tun
proto tcp
remote 192.168.1.23 1194 
resolv-retry infinite
nobind
user nobody
group nogroup
persist-key
persist-tun
ca ca.crt
cert client.crt
key client.key
comp-lzo
verb 3
remote-cert-tls server 
```

Now you can move to the /etc/openvpn/ directory and pull those certification keys from the server. You will obviously substitute your server’s actual IP address or domain name for the one in the example.

```
cd /etc/openvpn
scp ubuntu@192.168.1.23:/home/ubuntu/ca.crt . 
scp ubuntu@192.168.1.23:/home/ubuntu/client.crt .
scp ubuntu@192.168.1.23:/home/ubuntu/client.key .
```

Nothing exciting is likely to happen until you start up OpenVPN on the client. Because you’ll need to pass a couple of arguments, you’ll pull the trigger from the command line. — tls-client tells OpenVPN that you’ll be acting as a client and connecting via TLS encryption while — config points to your config file.

```
openvpn — tls-client — config /etc/openvpn/client.conf
```

Read the command output carefully to make sure you’re connected properly. If something does go wrong the first time, it’s probably either due to a setting mismatch between the server and client configuration files or perhaps a network connectivity/firewall issue. Here are some troubleshooting steps:

* Carefully read the output from the OpenVPN operation on the client — it will often contain valuable hints to exactly what it couldn’t do and why.
* Check for error-related messages in the openvpn.log and openvpn-status.log files in the /etc/openvpn/ directory on the server.
* Check OpenVPN-related and timely messages in the system logs on both the server and client (journalctl -ce will print out a screenfull of the most recent entries).
* Confirm that you’ve got an active network connection between the server and client (see chapter 14 for details).

_This article is excerpted from my_ [_Manning “Linux in Action” book_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9)_. There’s lots more fun_ [_where this came from_](https://bootstrap-it.com/index.php/books/)_,_ including a hybrid course called [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) that’s made up of more than two hours of video and around 40% of the text of Linux in Action. _Who knows…you might also enjoy my_ [_Learn Amazon Web Services in a Month of Lunches_](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27)_._

