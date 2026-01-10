---
title: Setting a Static IP in Ubuntu – Linux IP Address Tutorial
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2023-03-02T21:24:59.000Z'
originalURL: https://freecodecamp.org/news/setting-a-static-ip-in-ubuntu-linux-ip-address-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/setting-static-ip-ubuntu.png
tags:
- name: computer network
  slug: computer-network
- name: Linux
  slug: linux
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: "In most network configurations, the router DHCP server assigns the IP address\
  \ dynamically by default. If you want to ensure that your system IP stays the same\
  \ every time, you can force it to use a static IP. \nThat's what we will learn in\
  \ this article..."
---

In most network configurations, the router DHCP server assigns the IP address dynamically by default. If you want to ensure that your system IP stays the same every time, you can force it to use a static IP. 

That's what we will learn in this article. We will explore two ways to set a static IP in Ubuntu.

Static IP addresses find their use in the following situations:

* Configuring port forwarding.
* Configuring your system as a server such as an FTP server, web server, or a media server.

**Pre-requisites:**

To follow this tutorial you will need the following:

* Ubuntu installation, preferably with a GUI.
* `sudo` rights as we will be modifying system configuration files.

## How to Set a Static IP Using the Command Line

In this section, we will explore all the steps in detail needed to configure a static IP.

### Step 1: Launch the terminal

You can launch the terminal using the shortcut `Ctrl+ Shift+t`. 

### Step 2: Note information about the current network

We will need our current network details such as the current assigned IP, subnet mask, and the network adapter name so that we can apply the necessary changes in the configurations.

Use the command below to find details of the available adapters and the respective IP information.

```bash
ip a
```

The output will look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-14.png)

For my network, the current adapter is `eth0`. It could be different for your system

* **Note the current network adapter name**

As my current adapter is `eth0`, the below details are relevant.

```bash
6: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:df:c3:ad brd ff:ff:ff:ff:ff:ff
    inet 172.23.199.129/20 brd 172.23.207.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fedf:c3ad/64 scope link
       valid_lft forever preferred_lft forever
```

It is worth noting that the current IP `172.23.199.129` is dynamically assigned. It has `20` bits reserved for the netmask. The broadcast address is `172.23.207.255`.

* **Note the subnet**

We can find the subnet mask details using the command below:

```bash
ifconfig -a
```

Select the output against your adapter and read it carefully.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-15.png)
_IP is `172.23.199.129` and subnet mask is `255.255.240.0`_

Based on the class and subnet mask, the usable host IP range for my network is: `172.23.192.1 - 172.23.207.254`.

Subnetting is a vast topic. For more info on subnetting and your usable IP ranges, check out this [article](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/).

### Step 3: Make configuration changes

[Netplan](https://netplan.io/) is the default network management tool for the latest Ubuntu versions. Configuration files for Netplan are written using YAML and end with the extension `.yaml`.

Note: Be careful about spaces in the configuration file as they are part of the syntax. Without proper indentation, the file won't be read properly.

* Go to the `netplan` directory located at `/etc/netplan`.

`ls` into the `/etc/netplan` directory.

If you do not see any files, you can create one. The name could be anything, but by convention, it should start with a number like `01-` and end with `.yaml`. The number sets the priority if you have more than one configuration file. 

I'll create a file named `01-network-manager-all.yaml`. 

Let's add these lines to the file. We'll build the file step by step.

```bash
network:
 version: 2
```

The top-level node in a Netplan configuration file is a `network:` mapping that contains `version: 2` (means that it is using network definition version 2).

Next, we'll add a renderer, that controls the overall network. The renderer is `systemd-networkd` by default, but we'll set it to `NetworkManager`.

Now, our file looks like this:

```bash
network:
 version: 2
 renderer: NetworkManager
```

Next, we'll add `ethernets` and refer to the network adapter name we looked for earlier in step#2. Other device types supported are `modems:`, `wifis:`, or `bridges:`.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
```

As we are setting a static IP and we do not want to dynamically assign an IP to this network adapter, we'll set `dhcp4` to `no`.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
     dhcp4: no
```

Now we'll specify the specific static IP we noted in step #2 depending on our subnet and the usable IP range. It was `172.23.207.254`.

Next, we'll specify the gateway, which is the router or network device that assigns the IP addresses. Mine is on `192.168.1.1`.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
     dhcp4: no
     addresses: [172.23.207.254/20]
     gateway4: 192.168.1.1
```

Next, we'll define `nameservers`. This is where you define a DNS server or a second DNS server. Here the first value is  `8.8.8.8` which is Google's primary DNS server and the second value is `8.8.8.4` which is Google's secondary DNS server. These values can vary depending on your requirements.

```bash
network:
 version: 2
 renderer: NetworkManager
 ethernets:
   eth0:
     dhcp4: no
     addresses: [172.23.207.254/20]
     gateway4: 192.168.1.1
     nameservers:
         addresses: [8.8.8.8,8.8.8.4]
```

### Step 4: Apply and test the changes 

We can test the changes first before permanently applying them using this command:

```bash
sudo netplan try

```

If there are no errors, it will ask if you want to apply these settings.

Now, finally, test the changes with the command `ip a` and you'll see that the static IP has been applied.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-17.png)
_Static IP applied_

## How to Set a Static IP Using the GUI

It is very easy to set a static IP through the Ubuntu GUI/ Desktop. Here are the steps:

* Search for `settings`.
* Click on either Network or Wi-Fi tab, depending on the interface you would like to modify.
*  To open the interface settings, click on the gear icon next to the interface name.
* Select “Manual” in the IPV4 tab and enter your static IP address, Netmask and Gateway. 
* Click on the `Apply` button.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-16.png)
_Manually setting a static IP using Ubuntu Desktop._

* Verify by using the command `ip a`

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-18.png)
_Static IP updated via GUI_

## Conclusion

In this article, we covered two methods to set the static IP in Ubuntu. I hope you found the article useful.

What’s your favorite thing you learned from this tutorial? Let me know on [Twitter](https://twitter.com/hira_zaira)!

You can read my other posts [here](https://www.freecodecamp.org/news/author/zaira/).

