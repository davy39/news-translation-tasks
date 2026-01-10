---
title: How to Troubleshoot Your Network on Linux – OSI Model Troubleshooting Guide
subtitle: ''
author: Nitheesh Poojary
co_authors: []
series: null
date: '2024-03-25T17:34:59.000Z'
originalURL: https://freecodecamp.org/news/how-troubleshoot-network-on-linux
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/taylor-vick-M5tzZtFCOfs-unsplash.jpg
tags:
- name: Linux
  slug: linux
- name: network
  slug: network
seo_title: null
seo_desc: 'In the world of networking, you may find yourself troubleshooting problems
  such as difficulty connecting to other computers or to SSH, problems with IP tables,
  or being unable to access websites.

  However, have you ever attempted to troubleshoot your ...'
---

In the world of networking, you may find yourself troubleshooting problems such as difficulty connecting to other computers or to SSH, problems with IP tables, or being unable to access websites.

However, have you ever attempted to troubleshoot your network by applying the OSI Model? Through the use of a bottom-to-top methodology that is based on the Open Systems Interconnection (OSI) architecture, we will uncover the complexities of network troubleshooting, providing you with the knowledge and tools that are essential for effectively addressing a wide variety of networking difficulties.

## What is the OSI Model (Open Systems Interconnection)?

The Open Systems Interconnection (OSI) model is a conceptual framework that categorizes the functions of network communications into seven distinct levels. To put it simply, the OSI standardizes how various computer systems can communicate with one another.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-24-at-15.28.35.png)
_seven layers of the OSI model_

## How to Troubleshoot a Website by Applying the OSI Model Principles

Consider the following example of troubleshooting a website hosted on your server that is not working. We'll use Linux as our operating system. I believe that the divide and rule is a better technique for debugging. 

The OSI model is one method for efficiently breaking down an issue so that you can methodically simplify the environment in order to discover a solution and conquer it.

### Physical Layer

As I previously stated, when it comes to debugging, it is usually preferable to begin from the bottom. The physical layer is the bottom layer in the OSI Model. The key components in this layer consist of ethernet cables, hubs, and switches. At this level, you should check the power supply and the status of devices, as well as examine interface statistics.

* The "ifconfig" tool provides a detailed overview of all the ethernet cards present in your system.
* In addition, you have a choice of using the "IP link show" commands. If the result shows "down," it suggests that layer1 is not functioning.
* Sometimes, ethernet connections may be physically connected to the server but not activated by default. To enable, use the command below.

```bash
IP link set eth0 up
```

* If you're looking for more detailed information, the ethtool utility can be quite helpful. This utility provides the ability to query and modify settings. It allows you to adjust parameters such as speed, port, auto-negotiation, PCI locations, and checksum offload.

### Data Link Layer

The data link layer enables the transmission of data between two devices that are connected to the same network. There are two components in this layer. The first component is the medium access control (MAC) layer, which includes the operation of hardware addressing and access control. 

The second layer is the logical link layer, which enables the creation of a logical connection between different media. A common issue in this layer is the inability of two servers to establish connectivity. Tools such as ping, traceroute, arp, macof, and Wireshark are utilized for testing the data link layer.

This may help in verifying correct transmission and reception of data frames among devices within the same network group.

### Network Layer

The network layer's job is to make it easy for data to move between two networks. Network devices that work at Layer 3 of the OSI model are routers. A router's main job is to make it easier for networks to talk to each other. Working with IP addresses is part of this layer. 

In this stage, you should mostly look for problems with IP addresses. You can type "ip -br address show" to see the address. You can see if your network card has been given an IP address. You might not be getting dynamic IP addresses from DHCP if you use it to get them.

One common problem that often comes is the lack of an upstream gateway for a specific route or the absence of a default route. When an IP packet is transmitted to a different network, it needs to be directed to a gateway for additional processing. 

Understanding the routing of packets to their final destinations is crucial for the gateway. The routing table contains the list of gateways for various routes and can be managed using the “ip route” commands. We can also check connectivity by sending pings to the default gateway or beyond gateway.

### Transport Layer

Protocols like Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are used by the transport layer to control network traffic between systems and make sure that data flows efficiently. 

The transport layer is in charge of sending data packets, looking for errors, controlling the flow of data, and putting them in the right order. You may run into problems in this layer, like ports that aren't listening. Your service might not start because the port is already being used. You can see what ports are open by running "commad "netstat -antlp | grep "LISTEN"".

One problem that often occurs is related to remote connectivity. Consider a scenario where your local system is unable to establish a connection with a distant port, specifically HTTP on port 80.  The `telnet` command tries to create a TCP connection with the specified host and port. This capability is ideal for conducting remote TCP connectivity testing. 

To check a remote UDP port, you can utilize the "netcat" utility.

### Session Layer

This layer is responsible for facilitating the initiation and termination of communication between the two devices (for example: authentication). The period of time during which communication is initiated and terminated is referred to as the session. 

In this layer you should be investigating credentials, certificates of the servers, the session ID and cookies of the clients

### Presentation Layer

The presentation layer of the OSI model is responsible for formatting and transforming data in a way that allows it to be presented to the user. 

SSL or TLS encryption methods are key parts of this layer. Here, you should be examining for encryption and decryption issues.

### Application Layer

The system takes input from the user and transmits output back to the user. The Bellow Protocols function at this level. 

You should verify the configuration files on your server for any wrong settings. Additionally, it is essential to look at the log files on the servers to get more detailed information about the issues.

* File Transfer Protocol (FTP)
* Simple Mail Transfer Protocol (SMTP)
* Secure Shell (SSH)
* Internet Message Access Protocol (IMAP)
* Domain Name Service (DNS)
* Hypertext Transfer Protocol (HTTP).

## **Conclusion**

Troubleshooting network issues in Linux can be a daunting task, but by applying the principles of the OSI model, you can systematically diagnose and resolve problems with greater efficiency. 

Starting from the bottom layer and working your way up, we've explored various tools and techniques tailored to each level of the OSI model.

Beginning with the physical layer, we inspected hardware components and used tools like `ifconfig` and `ip link show` to verify connectivity. Moving up to the data link layer, we focused on MAC addresses and used utilities like `ping` and `Wireshark` for testing. At the network layer, we delved into IP addressing and routing, employing commands such as `ip route` and `ping` to diagnose issues.

Transitioning to the transport layer, we addressed TCP and UDP related problems, utilizing commands like `netstat` and `telnet` to check for open ports and establish connections. Further up the stack, we discussed the importance of session management and encryption at the session and presentation layers respectively.

Finally, at the application layer, we examined specific protocols like FTP, SMTP, SSH, and HTTP, emphasizing the significance of configuration files and log analysis in resolving issues.

