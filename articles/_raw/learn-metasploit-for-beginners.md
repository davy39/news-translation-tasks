---
title: Metasploit for Beginners — A Guide to the Powerful Exploitation Framework
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-01-22T00:12:40.389Z'
originalURL: https://freecodecamp.org/news/learn-metasploit-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737504731562/ebce2299-d90e-4b17-a1b0-15b4dbe6d844.png
tags:
- name: metasploit
  slug: metasploit
- name: cybersecurity
  slug: cybersecurity
- name: Msfconsole
  slug: msfconsole
- name: payloads
  slug: payloads
- name: Exploitation
  slug: exploitation
- name: exploit
  slug: exploit
- name: pentesting
  slug: pentesting
seo_title: null
seo_desc: 'If you’re starting your journey into penetration testing, you’ve likely
  heard of Metasploit.

  Metasploit is one of the most versatile tools in cybersecurity. It helps simplify
  vulnerability testing and exploitation.

  Metasploit helps us find and fix we...'
---

If you’re starting your journey into penetration testing, you’ve likely heard of [Metasploit](https://www.metasploit.com/).

Metasploit is one of the most versatile tools in cybersecurity. It helps simplify vulnerability testing and exploitation.

Metasploit helps us find and fix weaknesses before malicious actors exploit them. In this tutorial, you’ll learn what Metasploit is, why it’s useful, and how to use it.

## **What is Metasploit?**

Metasploit is an open-source framework for penetration testing.

You can use it to find vulnerabilities, exploit them, and get access to the target.

Metasploit provides a collection of exploits, payloads, and helper tools. It’s often called the “Swiss army knife” for pen testers.

Instead of writing your own scripts to exploit vulnerabilities, Metasploit gives you pre-built modules to automate a lot of your work.

A module is a piece of code that performs an action. These actions can include scanning, exploitation, or anything that helps to simplify a pen-test.

## **Why is Metasploit Useful for Penetration Testers?**

Pentesters try to attack networks, applications, and systems to check their security. Metasploit helps make this job easier in several ways.

First, it simplifies exploitation. Metasploit has a large library of exploits that allows us to attack known weaknesses in software and systems quickly.

Next, it helps with reconnaissance and scanning. Metasploit’s scanning tools gather information about a target, such as open ports, running services, and likely vulnerabilities.

After breaking in, Metasploit provides post-exploitation features. Tools like Meterpreter let pentesters keep access, collect data, and test defenses further.

Metasploit is also very flexible. We can build or change modules to fit our specific needs.

In short, Metasploit lets us do complete security tests, from finding vulnerabilities to exploiting them.

## **What Are Metasploit Auxiliaries?**

Auxiliary modules are helper tools within Metasploit that perform tasks other than exploitation.

They’re used for reconnaissance, scanning, brute-forcing and more. These flexible modules can help you gather valuable information about a target.

For example, an auxiliary module can scan a network for open ports, check for vulnerable services, or attempt a brute-force login on an application.

Here is a sample list of auxiliaries from metasploit:

![Metasploit auxiliaries](https://cdn.hashnode.com/res/hashnode/image/upload/v1737559559020/41a5d517-4f98-4c5c-bd7f-0e9e3dfb4977.png align="center")

You can see that Metasploit has a range of auxiliaries, from scanners to brute-force modules, which help reveal and exploit security gaps.

## **What Are Metasploit Exploits?**

Exploits are scripts or programs that take advantage of vulnerabilities in systems.

They help an attacker gain access or perform malicious activities. Metasploit’s library includes hundreds of exploits, covering a wide range of platforms and services.

For example, if a target system is running an outdated version of Samba, Metasploit may have an exploit specifically designed to exploit that vulnerability.

## **What Are Metasploit Payloads?**

Payloads are scripts that run on the target system after an exploit has been successfully executed.

They determine what happens next — whether you open a reverse shell, add a backdoor, or perform another post-exploitation task.

There are two main types of payloads:

1. **Single Payloads**: These perform one task, such as creating a user account on the target.
    
2. **Staged Payloads**: These download a larger payload in stages, allowing for more complex actions.
    

One of the most commonly used payloads is `windows/meterpreter/reverse_tcp`, which gives you a command shell on the target system.

Pen testers and security experts use exploits to uncover weak points in networks and systems. By testing these gaps in a controlled way, they can find faults before attackers do. Once found, these flaws are fixed or patched to prevent harm. This approach helps protect data and keeps systems more secure.

## **What is Metasploit Meterpreter?**

Meterpreter is an advanced, interactive payload within Metasploit. It allows you to interact with the target system after exploiting it.

Meterpreter is loaded directly into the target's memory, making it stealthier than traditional payloads.

Using Meterpreter, you can gather details about the operating system, transfer files between the attacker and target, and even execute commands directly on the target machine.

You can also set up a persistent backdoor to maintain access even after a system reboot.

Meterpreter is a powerful tool for post-exploitation activities, giving you complete control over the compromised system.

## **How to Work with** `msfconsole`

Let's get some hands-on experience with Metasploit.

`msfconsole` is the command-line interface (CLI) for Metasploit. It’s the main way to interact with the framework.

Metasploit is pre-installed in Kali Linux. If you are using Kali Linux, you can find the [installation instructions here](https://docs.rapid7.com/metasploit/installing-the-metasploit-framework/).

After installing Metasploit, launch the console by typing:

```plaintext
msfconsole
```

Once it loads, you’ll see a prompt like this

![msfconsole](https://cdn.hashnode.com/res/hashnode/image/upload/v1736776944033/519269c1-9124-4467-9257-4cbe693be0df.png align="center")

This is where you’ll type commands to interact with Metasploit. Let’s try some basic commands to get you started.

### Metasploit commands

1. `help`: If you’re unsure about what to do, start by typing `help`. This displays a list of available commands along with brief descriptions. For example:
    

![metasploit help command](https://cdn.hashnode.com/res/hashnode/image/upload/v1736776984407/182a0f3c-0fb2-4880-85cf-cbd0baff6538.png align="center")

2. `search`: The search command helps us to find specific modules, such as exploits or auxiliaries (helper modules). For example, if you’re looking for modules related to scanning, you’d type:
    

```plaintext
msf6 > search scanner
```

![Metasploit search](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777096451/63c0087f-80dd-42a1-98c7-9459f53b7f5a.png align="center")

Metasploit will display all modules that match the keyword scanner.

3. `info`: You can use the `info` command to learn more about a module, including its options and how it works. For example:
    

```plaintext
msf6 > info auxiliary/scanner/portscan/tcp
```

![Metasploit info command output](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777131375/c89a1e64-f96e-4fff-9f36-4dd5c1e7f20d.png align="center")

4. `use`: To use an exploit or an auxiliary, we can simply type `use` along with the module name. Let's use the scanning module `auxiliary/scanner/portscan/tcp` which will scan for open TCP ports in a server.
    

```plaintext
msf6> use auxiliary/scanner/portscan/tcp
```

5. `options`: Once you have loaded a module with the `use` command, you can see the list of options using the `options` command. it will give you the list of options you can set for that module.
    

![Metasploit options command](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777161123/5e2b44bb-08ee-4489-a1c0-8d78070710b5.png align="center")

For example, the RHOSTS parameter is used to set the target IP address for scanning. [`scanme.nmap.org`](http://scanme.nmap.org) lets us run port scans on that server, so let's use that to run a scan.

Let’s grab the IP address of the server. We will issue a simple ping command to get the IP address of the server.

![Ping command](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777193985/3c71c4b8-ab74-46bc-a613-3115b97eef6f.png align="center")

We can see that the IP address of the server is 45.33.32.156 (it can change when you run the ping command). Now let’s use this IP as our input for RHOSTS parameter. We will use the `set` command to set the IP address.

```plaintext
msf6 auxiliary(scanner/portscan/tcp)> set RHOSTS 45.33.32.156
```

6. `run`: To run a module, we use the `run` command. Now that we have set the target IP address, let's run the module to see if any ports are open.
    

![Metasploit port scan](https://cdn.hashnode.com/res/hashnode/image/upload/v1736777226150/9bab8d7b-9efb-4573-bcc9-1c355a468bf4.png align="center")

As you can see, we have found 3 ports — 22,80 and 9929. Tools like Nmap are better for in-depth port scanning, but Metasploit offers modules for almost every segment of a cybersecurity audit.

7. `exit`: When you’re done using Metasploit, simply type `exit` to leave the console.
    

The `msfconsole` is user-friendly once you get the hang of these basic commands. Take your time exploring and experimenting with the help of the `help` command.

## **Conclusion**

Metasploit is one of the most powerful tools in a penetration tester’s toolkit.

As you grow more familiar with Metasploit, you’ll unlock its full potential and gain deeper insights into how attackers exploit systems — and how you can defend against them. Keep learning, stay curious, and always use Metasploit responsibly!

Join our [**Weekly Newsletter**](https://www.stealthsecurity.sh/) for more tutorials on Ethical Hacking. For video tutorials on cybersecurity, check out our [**Youtube Channel**](https://www.youtube.com/@stealthsecurity_sh).
