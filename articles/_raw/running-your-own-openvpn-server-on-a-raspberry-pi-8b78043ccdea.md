---
title: How to run your own OpenVPN server on a Raspberry PI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-22T10:14:17.000Z'
originalURL: https://freecodecamp.org/news/running-your-own-openvpn-server-on-a-raspberry-pi-8b78043ccdea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WEXV6clyYAztJhQ97TtYNw.png
tags:
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: vpn
  slug: vpn
seo_title: null
seo_desc: 'By Denis Nuțiu


  My Raspberry, serving as an OpenVPN server

  Hello everyone!

  In this short article I will explain how to setup your own VPN (Virtual Private
  Network) server on a Raspberry PI with OpenVPN. After we setup the server, we will
  setup an obf...'
---

By Denis Nuțiu

![Image](https://cdn-media-1.freecodecamp.org/images/aShx3zgBveeNtJo-SyE1AF5Zs4UquT2lNpR6)
_My Raspberry, serving as an OpenVPN server_

Hello everyone!

In this short article I will explain how to setup your own VPN (Virtual Private Network) server on a Raspberry PI with OpenVPN. After we setup the server, we will setup an obfuscation server in order to disguise our traffic indicating that we’re using a VPN. This will help us evade some form of censorship.

### Why use a VPN?

First, let’s talk about why you may want to use a VPN server:

1. Avoid man in the middle attacks. If you have a malicious user on your local network — even your roommate — that person is able to monitor your unencrypted traffic and tamper with it.
2. Hide your internet activity from your ISP (Internet Service Provider) or University, in my case.
3. Unblock services. My University blocks all UDP (User Datagram Protocol) packets. This means that I cannot use any application that communicates via UDP. I can’t use my email client, play games, or even use Git!

I decided to setup a VPN on my home internet using a Raspberry Pi. This way I can connect to my home network while I’m at the University. If you need a VPN server in another country, you can buy a 5$/month virtual private server from [DigitalOcean](https://m.do.co/c/22f012126c25). You can use my referral link in order to get $10 off — that’s two months of free VPN. But you don’t have to use it if you don’t want to.

### Installing OpenVPN

This step is really easy, because we will use a shell script to do it for you. So you just have to “press” next and finish.

The installation will take a long time, depending on the key-size you chose. On my Raspberry Pi 3 Model B, it took about 3 hours.

Please go this repository and then follow the instructions

[**Angristan/OpenVPN-install**](https://github.com/Angristan/OpenVPN-install)  
[_OpenVPN-install - Set up your own OpenVPN server on Debian, Ubuntu, Fedora CentOS, and Arch Linux_github.com](https://github.com/Angristan/OpenVPN-install)

If you don’t know the IP address of your server, just put `0.0.0.0` . I’ve chosen `443` for the port and **TCP** (Transmission Control Protocol) for the protocol.

**Note**: This is very important because my university only allows **TCP/80** and **TCP/443** ports, the rest are pretty much blocked. Also Obfsproxy only works with TCP, so make sure you chose **TCP**!

After the script has finished, you’ll get an **.ovpn** file. It can be imported in your favourite VPN client, and everything should work out of the box.

#### Testing the connection

Import the .ovpn file in your VPN client and change the ip `0.0.0.0` to the local ip of your Raspberry PI. Depending on your network configuration it may be of the form`192.168.*.*` .

_Note: This will only work if you are connected to the same WiFi as the Pi is._

![Image](https://cdn-media-1.freecodecamp.org/images/RwesiNeDbzJfYs6cuC7KtJ0IWIuHExaale8S)
_Viscosity successfully connected to my VPN server._

**I’ve configured my router so the PI always gets a reserved IP address. You may have to check out your router settings if you want to do something similar.**

If the connection is successful, congratulations, you now have a VPN server! But, you cannot access it from outside… yet.

If you only want an OpenVPN server without the obfuscation proxy, then you can skip to **Port Forwarding**.

### Obfuscation **Proxy Install**

Obfs4 is a scrambling proxy. It disguises your internet traffic to look like noise. Somebody who snoops on your traffic won’t actually know what you’re doing, and it will protect you from active probing attacks which are used by the Great Firewall of China.

_Note: This method won’t work if your adversary allows only whitelisted traffic :(_

#### Let’s install the proxy server now.

0. Install the required package:

```
apt-get update && apt-get install obfs4proxy
```

1. Create a directory that will hold the configuration.

```
sudo mkdir -p /var/lib/tor/pt_state/obfs4
```

2. Create the configuration file.

```
sudo nano /var/lib/tor/pt_state/obfs4/obfs4.config
```

In the configuration file, you will paste the following things:

```
TOR_PT_MANAGED_TRANSPORT_VER=1TOR_PT_STATE_LOCATION=/var/lib/tor/pt_state/obfs4TOR_PT_SERVER_TRANSPORTS=obfs4TOR_PT_SERVER_BINDADDR=obfs4-0.0.0.0:444TOR_PT_ORPORT=127.0.0.1:443
```

**TOR_PT_SERVER_BINDADDR** is the address on which the proxy will listen for new connections. In my case it is it `0.0.0.0:444` — why 444 and not 443? Well, because I don’t want to change the OpenVPN server configuration which is currently listening on 443. Also, I will map this address later to 443 using Port Forwarding.

**TOR_PT_ORPORT** should point to the OpenVPN server. In my case, my server runs on `127.0.0.1:443`

3. Create a SystemD service file.

```
sudo nano /etc/systemd/system/obfs4proxy.service
```

Then paste the following contents into it:

```
[Unit]Description=Obfsproxy Server[Service]EnvironmentFile=/var/lib/tor/pt_state/obfs4/obfs4.configExecStart=/usr/bin/obfs4proxy -enableLogging true -logLevelStr INFO[Install]WantedBy=multi-user.target
```

4. Start the Obfuscation proxy.

Now, make sure that OpenVPN is running and run the following commands in order to start the proxy and enable it to start on boot.

```
sudo systemctl start obfs4proxysudo systemctl enable obfs4proxy
```

5. Save the cert KEY

After the service has started, run the following command and save the cert KEY.

```
cat /var/lib/tor/pt_state/obfs4/obfs4_bridgeline.txt
```

The key is of the form `Bridge obfs4 <IP ADDRESS>:<PORT> <FIN**GER**PRINT> c`ert=KEY iat-mode=0 . You will need it when you’re connecting to the VPN.

6. Testing the connections.

Open up your VPN client and change the ip from 443 to 444 in order to connect to the proxy instead of the OpenVPN server.

After that, find the Pluggable Transport option in your OpenVPN client and see if it supports **obfs4**.

![Image](https://cdn-media-1.freecodecamp.org/images/k2ce9ab0OAcKCXASAkmIU6GyYVKLr7L1odm1)
_Viscosity supports different Obfuscation methods such as: obfs2, obfs3, obfs4 and ScrambleSuit_

If everything works, then you’re all set! Congratulations! Only a few more things to tweak before using this VPN from the outside world.

### **Port Forwarding**

In order to access the OpenVPN server from the outside world we need to unblock the ports, because they are most likely blocked. As you remember, I have reserved my PI’s IP address on my router to always be `192.168.1.125` so it doesn’t change if the PI disconnects or if the router reboots.

This way I have defined the following rules in my Port Forwarding table:

![Image](https://cdn-media-1.freecodecamp.org/images/NqZZFwzTrUAyzVuAHAHDly0Dpoe3zSO24N-i)
_TL-WR841N’s Port Forwarding settings page._

The outside port **443** will point to the obfuscation’s server port **444.** If you don’t have an obfuscation server, then leave **443->4**43.

The port 25 will point to the PI’s SSH port 22. This is only for my own convenience.

In case I want to access the OpenVPN server directly without the obfuscation proxy, I have created a rule **444->**443

The service port is the **OUTSIDE** port that will be used with your **PUBLIC** IP address. To find your public IP, use a service like whatsmyip.com.

The internal port is the **INSIDE** port. It can be used only when you are connected to the network.

_Note: The first rule is saying redirect all the connections from **PUBLIC_IP:443** to **192.168.1.125:444**_

#### Testing

1. Find your public IP and replace your old IP with the public IP in the .ovpn file or in the VPN client.
2. Connect to the VPN.

That’s it.

### **Dynamic DNS**

In most cases, your IP will change because it’s a dynamic IP. A way to overcome this is to create a small program on the PI that saves your IP and sends you an email every day or so. You may also store the IP in an online database such as Firebase.

My router has Dynamic DNS setting. This way I can use a service provider like NoIP and get a domain like `example.no-ip.com` that will always point to my public IP address.

![Image](https://cdn-media-1.freecodecamp.org/images/d-BrxA5r4qqvGgqjRzuSXGnMGcAncBIKUlu8)
_TL-WR841N DDNS settings page_

#### Other Resources:

* [A Childs Garden Of Pluggable Transports](https://trac.torproject.org/projects/tor/wiki/doc/AChildsGardenOfPluggableTransports)
* V[iscosity-Obsfurcation/](https://www.sparklabs.com/support/kb/article/setting-up-an-obfuscation-server-with-obfsproxy-and-viscosity/)
* [https://www.pluggabletransports.info/transports/](https://www.pluggabletransports.info/transports/)

If you have any questions hit me up on [Twitter](https://twitter.com/denisnutiu).

