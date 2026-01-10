---
title: What is An ACL? Access Control Lists Explained
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2023-04-14T14:43:14.000Z'
originalURL: https://freecodecamp.org/news/a-deep-dive-into-access-control-lists
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/towfiqu-barbhuiya-FnA5pAzqhMM-unsplash.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: computer networking
  slug: computer-networking
- name: Security
  slug: security
seo_title: null
seo_desc: 'In computing, access control is the concept of limiting or regulating a
  person or machine''s access to certain information or resources.

  One of the major mechanisms you use to do that is an access control list (ACL).
  An ACL is a set of rules for allow...'
---

In computing, access control is the concept of limiting or regulating a person or machine's access to certain information or resources.

One of the major mechanisms you use to do that is an access control list (ACL). An ACL is a set of rules for allowing or denying access to certain resources. Resources in this case may be files, networks, or devices.

In this article, we'll talk about what access control lists really are, and how you can use them. We're going to deal with:

* Filesystem ACLs and Network ACLs
    
* Firewalls and stateful packet filtering
    
* ACLs in Cloud Networking (Azure NSG, AWS SG, AWS NACL)
    
* ACLs in DNS (BIND9)
    
* ACLs in core networking (Cisco ACL types, Huawei ACL types)
    

## Prerequisites

To understand this article, you need a basic understanding of networking, firewalls, and cloud computing. You may particularly need to understand basic of [IP addressing](https://www.linkedin.com/pulse/ip-addressing-chidiadi-anyanwu) and [DNS](https://www.linkedin.com/pulse/dns-deep-dive-chidiadi-anyanwu/) concepts.

## Types of Access Control Lists

When we talk about ACLs, many people just think of networks. But in fact, there are two types of ACLs:

* File system ACLs
    
* Networking ACLs
    

Filesystem ACLs help operating systems know what the user access privileges are for different files or directories in the system. NFSv4 ACLs and POSIX ACLs are examples of filesystem ACL types.

Networking ACLs are applied on interfaces and you use them to allow or deny traffic from certain sources or to certain destinations. This is what I'll be focusing on in this article.

## Structure Of An ACL Rule

An ACL is like a group of rules identified by a name or number. An ACL rule usually has a priority number, the criteria (source address, destination address, and so on) and the allow/deny statement.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Cisco-ACL-structure.png align="left")

*Cisco ACL structure*

## Firewalls and ACLs

A firewall is a security device or software that monitors the traffic going in and out of a device or network, and filters out unwanted or malicious traffic.

Until stateful packet inspection, ACLs were the major mechanism through which firewalls worked. With ACLs, packets are allowed and denied based on properties specified in the rules.

ACLs are stateless. You must create an inbound rule and a corresponding outbound rule, or else packets from one side might be blocked.

With stateful packet inspection (also known as dynamic packet filtering), you could then create security policies for a type of traffic. The firewall would establish a session whenever a packet is allowed, so that any response to that packet is allowed even though there was no specific policy to allow it.

This makes things easier and more efficient than using ACLs that are uni-directional. But it also means that more computing resources are utilized by the firewall and the network is slowed down.

Now, firewalls are a lot more complex than that with deep packet inspection (DPI), Intrusion Detection System (IDS)/Intrusion Prevention System (IPS) capabilities, and even antivirus capabilities, but those are outside the scope of this article.

Let's explore some networking situations where ACLs are used.

## ACLs in Cloud Networking

The major cloud service providers (CSPs) provide forms of ACLs or firewall capabilities for their customers to use in their cloud infrastructure.

For example, in Microsoft Azure, we have what is called Network Security Groups (NSG) and in AWS, we have Security Groups (SG) and the Network Access Control List (NACL). These are all implementations of ACL-like security.

### AWS

An AWS security group determines what traffic is allowed to and from the resources attached to that security group. It consists of a list of inbound and outbound rules, and is stateful.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot--320--1.png align="left")

*Default AWS Security Group*

An AWS Network Access Control List is another list of rules but at the subnet level. The rules consist of the rule number, type, protocol, port range, source, destination and allow/deny fields. A NACL can be applied more than one subnet, but a subnet cannot be attached to more than one NACL.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot--319--nacl-3-1.png align="left")

*Inbound rules for AWS NACL*

### Azure

An Azure Network Security Group is a kind of firewall feature that works both at the subnet level and the network interface card (NIC) of the resources in your VNet. It is basically also a list of ACL rules consisting of priority number, name, port, protocol, source and destination.

Here, you can use IP addresses, service tags, or application security groups (ASGs) in the source and destination fields. NSGs are stateful.

Both the Azure NSG and the AWS NACL rules are very similar to the ACL rules used in core networking. Also, you cannot really refer to AWS Security Groups and Azure NSGs as ACLs because they're not stateless.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Microsoft-NSG-rules-image.png align="left")

*Azure NSG*

## ACLs in DNS

[DNS servers help resolve domain names to IP addresses](https://www.linkedin.com/pulse/dns-deep-dive-chidiadi-anyanwu/). If they accept and respond to requests from every device around them, it will impact their performance and make them susceptible to DDoS attacks. So, DNS administrators use ACLs to determine who can send DNS requests to the servers.

For example, in a BIND9 server, such an ACL will be defined in the named.conf file, and would look like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot--308--1.png align="left")

*An ACL in BIND9*

## ACLs in Core Networking

This is a bit more complex than the other contexts we discussed above. ACLs on network devices are configured on the interfaces, and are used in many different scenarios. There are also different types of ACLs. By network devices, I mean devices like routers, switches, firewalls, access controllers, and so on.

Generally, these ACLs are identified by their names or ACL numbers, and their rules follow the format:

*permit/deny criteria*

For Cisco devices, there are two major types of IPv4 ACLs:

* Standard access lists
    
* Extended access lists
    

### Standard ACLs

These ACLs permit or deny traffic based on only the source IP address.

```python
R1(config)#access-list 10 permit 192.168.17.0 0.0.0.255
```

The rule above tells the router to permit packets from the *192,168,17,0/24* subnet. Note that *0.0.0.255* is not a subnet mask. It is a wildcard that tells the device to which extent it must match the address you entered. *255* means any number goes while *0* means it must match exactly.

So here, the network part *192.168.17* must be exactly the same in whatever packet, while the last octet (the host part) can be whatever. You can learn more about IP addressing [here](https://www.linkedin.com/pulse/ip-addressing-chidiadi-anyanwu).

### Extended ACLs

These ACLs permit or deny traffic based on what is known in networking as the 5-tuple (source address, destination address, source port, destination port, transport layer protocol).

```python
R2(config)#access-list 100 permit tcp 10.1.1.0 0.0.0.255 host 10.2.2.2 eq 80
```

The command above tells the router to permit any packet using the TCP transport layer protocol, coming from the 10.1.1.0/24 network to port 80 ([HTTP](https://www.linkedin.com/pulse/http-network-protocol-chidiadi-anyanwu/)) of the host, 10.2.2.2.

The term 5-tuple in networking probably originated from mathematics. A tuple means a record/row. 5-tuple means a row with five columns – an ordered list of 5 elements.

The five elements we're mostly concerned with in networking when dealing with packets are the IP addresses (source and destination), port numbers (source and destination), and transport layer protocol. So, they're usually referred to as 5-tuple.

ACL numbers 1 - 99 and 1300 - 1999 denote standard ACLs while numbers 100 - 199 and 2000 - 2699 denote extended ACLs.

Many other vendors follow this pattern, but Huawei doesn't.

For Huawei devices, there are 5 types of IPv4 ACLs:

* Basic ACLs ( ACL numbers 2000 - 2999)
    
* Advanced ACLs (ACL numbers 3000 - 3999)
    
* Layer 2 ACLs (ACL numbers 4000 - 4999)
    
* User-defined ACLs (ACL numbers 5000 - 5999)
    
* User ACLs (ACL numbers 6000 - 6999)
    

**Basic ACL:** Permits or denies traffic based on source address. The ACL number ranges from 2000 - 2999.

**Advanced ACL:** Permits or denies traffic based on the 5-tuple (source IP address, destination IP address, source port, destination port, and protocol type).

**Layer 2 ACL:** Permits or denies traffic based on information in the frame header (source MAC address, destination MAC address, layer 2 protocol type).

**User-defined ACL:** Permits or denies traffic based on packet headers, offsets, character string masks, and user defined character strings.

**User ACL:** Permits or denies traffic based on source and destination IP addresses or user control list (UCL) groups, source and destination ports, and IPv4 protocol types.

```python
acl 3500                                                
 rule 0 deny tcp source 10.1.1.0 0.0.0.255 destination 192.168.0.9 0 destination-port eq 80                                                                
 rule 5 allow tcp source 10.1.1.0 0.0.0.255 destination 192.168.0.9 0 destination-port eq telnet
```

### Implicit deny

It is also important to note that even if you do not add any rule at the end of your ACL, the last rule there is always a deny rule. It is not shown, so it is implicit. But it is there. It denies any packet that does not match any rule in your ACL.

### A Few Things To Know

ACL rules are executed sequentially, so if you have rule 3 and rule 5, rule 3 gets executed first.

It is always a good practice to create rules at intervals (rule 10, rule 20, rule 30) rather than just serially (rule 1, rule 2, rule 3). The reason is that you may want to add a rule in-between two existing rules, and you want the system to execute it in that particular order. It saves stress if there was space for that from the beginning.

## Conclusion

Access control is critical to security. Digitally, ACLs have been the go-to mechanism for quick and easy access control. Though other methods like role-based access control (RBAC) and attribute-based access control (ABAC) have emerged, ACL still has its place in access control.

Thanks for reading. If you enjoyed this article, please share it so others can see it too.

You can also [connect with me on LinkedIn](https://linkedin.com/in/chidiadi-anyanwu).
