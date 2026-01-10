---
title: How to Set Up a VPN Server at Home for Free
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-15T20:19:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-vpn-server-at-home
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/grey-and-black-macbook-pro-showing-vpn-2064586--1-.jpg
tags:
- name: Security
  slug: security
- name: self hosting
  slug: self-hosting
- name: vpn
  slug: vpn
seo_title: null
seo_desc: 'By Yehuda Clinton

  In this article, I''m going to guide you, step-by-step, through the process of setting
  up a WireGuard VPN on a Linux server. It will let you access secure internet resources
  from insecure places like coffee shops.

  But why a VPN? And ...'
---

By Yehuda Clinton

In this article, I'm going to guide you, step-by-step, through the process of setting up a WireGuard VPN on a Linux server. It will let you access secure internet resources from insecure places like coffee shops.

## But why a VPN? And why WireGuard?

Whenever you connect to, say, your bank's website from a remote location, you risk exposing password and other sensitive information to anyone listening on the network. 

Hopefully, of course, the bank website itself will be encrypted, which means that the key data flowing between the bank and your PC or smartphone will be unreadable to anyone listening along the way. 

And what about if you're connecting from your home or office? With a VPN, you can be reasonably sure that those data elements not obscured by regular encryption won't be seen by the wrong people.

But what if you're connecting through a public WiFi router at an airport or coffee shop? Are you sure the network hasn't been compromised or that there aren't hackers watching unnoticed?

To counter this very real threat, you can open a connection on your laptop or phone to a VPN server. This way all your data transfers take place through a virtual tunnel. Every part of your sensitive connections will be invisible to anyone on the local network you're connecting from.

WireGuard is the newest of the three big players in the open source VPN world, with the other two being IPsec and OpenVPN. 

WireGuard is built to be simpler, faster, and more flexible than the others. It's the new kid on the block, but it's quickly picked up some important friends. At the urging of Linux creator Linus Torvalds himself, WireGuard was recently incorporated into the Linux kernel.

# Where to build your VPN server?

Sure, you can always put together a VPN server at home and configure port forwarding through your ISP's router. But it'll often make more practical sense to run it in the cloud. 

Don't worry. I assure you that this way will be a lot closer to a quick and painless "set it and forget it" configuration. And it's highly unlikely that whatever you build at home would be as reliable – or secure – as the infrastructure provided by the big cloud providers like AWS. 

However, if you do happen to have a professionally secured internet server lying around the house (or you're willing to take a chance with a spare Raspberry Pi you've got lying around) then it'll work just about the same way.

Thanks to WireGuard, whether in the cloud or on a physical server, making your own home VPN has never been easier. The whole setup can be done in half an hour.

# Getting ready

Get your cloud instance up and running, perhaps using a [tutorial from here](https://www.freecodecamp.org/news/administrating-aws-resources-productively-using-the-aws-cli/).

Make sure port **51820** is open to your server. This is done with _Security groups_ on AWS and a _VPC network firewall_ on Google Cloud.

With modern Debian/Ubuntu releases, Wireguard is available to be installed from the package managers like this:

```
sudo apt install wireguard

```

Or with yum, from the EPEL repository:

```
sudo yum install kmod-wireguard wireguard-tools

```

# Step one: create the encryption keys

In any directory on the server where you want to create files containing the public and private keys, use this command:

```
umask 077; wg genkey | tee privatekey | wg pubkey > publickey

```

Do the same for the client in a different directory or on your local machine. Just make sure you will be able to distinguish between the different key sets later. 

For quick setup you can use an [online key generator](https://www.wireguardconfig.com). However I suggest doing it manually the first time. Make sure that files were created with key hashes in them as you will be using them in the next step.

# Step two: create the server config

You need to make a _.conf_ file in the /etc/wireguard directory. You can even have multiple VPNs running at the same time using different ports. 

Paste the following code in to the new file:

```
sudo nano /etc/wireguard/wg0.conf

```

```
[Interface]
Address = 10.0.0.1/24
ListenPort = 51820
# use the server PrivateKey
PrivateKey = GPAtRSECRETLONGPRIVATEKEYB0J/GDbNQg6V0s=

# you can have as many peers as you wish
# remember to replace the values below with the PublicKey of the peer

[Peer]
PublicKey = NwsVexamples4sBURwFl6HVchellou6o63r2B0s=
AllowedIPs = 10.0.0.2/32

[Peer]
PublicKey = NwsexampleNbw+s4sBnotFl6HrealxExu6o63r2B0s=
AllowedIPs = 10.0.0.3/32

```

### Start up the VPN

```
sudo systemctl start wg-quick@wg0

```

If you don't have systemd (which might be true if your instance is running Amazon Linux) you could use `sudo wg-quick up wg0`.

# Step three: create the client config

First install Wireguard on your client machine, either the same way on Linux or through an app store if you're using Windows, macOS, Android, or iPhone. 

If you used an online-key-generator or QR script in Step One, then you can connect your phone by taking a picture of the QR code.

Once WireGuard is installed on the client, configure it using these values:

```
# Replace the PrivateKey value with the one from your client interface
[Interface]
Address = 10.0.0.2/24
ListenPort = 51820
PrivateKey = CNNjIexAmple4A6NMkrDt4iyKeYD1BxSstzer49b8EI=

#use the VPN server's PublicKey and the Endpoint IP of the cloud instance
[Peer]
PublicKey = WbdIAnOTher1208Uwu9P17ckEYxI1OFAPZ8Ftu9kRQw=
AllowedIPs = 0.0.0.0/0
Endpoint = 34.69.57.99:51820

```

There are many optional add-ons that you might want depending on your use-case, such as specifying DNS or pre-shared keys for an extra layer of security.

Start up the client in same way as the server if you are on Linux or through the application itself on other systems.

# Test your VPN

Type "my ip" in your browser to discover your public IP address. If the IP you get is different from the address your computer had before starting the VPN, then you were successful!

(And if you forgot what it was before, try `sudo systemctl stop wg-quick@wg0`, checking and starting it again.)

# Troubleshooting Guide

Make sure your server is configured for IP forwarding. Check the /etc/sysctl.conf file, or run:

```
echo 1 > /proc/sys/net/ipv4/ip_forward

```

Your connection dies often? Add this to the peer section of the client configuration:

```
PersistentKeepalive = 25

```

Not sure why it's not working? Try `sudo tcpdump -i eth` on the server while trying to use the client.

## Thanks for reading this guide. 

If you want to dive deeper, consider taking [my paid Manning course on WireGuard VPN](https://www.manning.com/liveproject/secure-business-infrastructure-with-a-custom-vpn?a_aid=bootstrap-it&a_bid=b9d7d398&chan=VPN).

