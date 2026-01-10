---
title: Shodan – What to Know About the Internet’s Most Dangerous Search Engine
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-09-10T17:43:12.373Z'
originalURL: https://freecodecamp.org/news/shodan-what-to-know-about-the-internets-most-dangerous-search-engine
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725990169364/3181020e-abd0-4943-a461-830c2a416035.png
tags:
- name: hacking
  slug: hacking
- name: '#cybersecurity'
  slug: cybersecurity-1
- name: ethicalhacking
  slug: ethicalhacking
seo_title: null
seo_desc: 'Shodan is a search engine that discovers devices connected to the internet.
  In this article, we’ll look at why it’s both a valuable tool and a potential threat.

  When you hear the term “search engine,” your mind likely jumps to Google, Bing,
  or Yahoo....'
---

Shodan is a search engine that discovers devices connected to the internet. In this article, we’ll look at why it’s both a valuable tool and a potential threat.

When you hear the term “search engine,” your mind likely jumps to Google, Bing, or Yahoo. These platforms are familiar to most of us, helping us find websites, images, and news.

But there’s another search engine out there, one that most people have never heard of. And it’s a lot more powerful and dangerous. It’s called [Shodan](https://www.shodan.io/).

Shodan is a database of online devices, many of which are not meant to be public. The scary thing about Shodan is that it can have one of your devices, too.

Let’s look at what Shodan is, how it works, and why it’s both a valuable tool and a potential threat.

### What is Shodan?

Shodan is a search engine that discovers devices connected to the internet. This includes everything from simple webcams and routers to complex industrial control systems.

Traditional search engines index websites. Shodan scans the internet for devices and lists them based on their IP addresses, open ports, and other publicly available data.

Shodan works by scanning the internet using specific protocols to identify connected devices. It collects all information about the device.

These include IP addresses, open ports, and even the software versions in use. This data is then made searchable by allowing users to query the database. You can look for specific types of devices or vulnerabilities using Shodan’s UI or the CLI tool.

Let’s look at how you can use Shodan both via the web interface and the command line.

### How to Use the Shodan Web Interface

Go to [shodan.io](https://www.shodan.io) and create an account. While some searches are possible without an account, you’ll need to log in to access most features.

Also, you will need a premium account to find most devices, and the results of the free plan are very limited.

![Shodan home page](https://cdn.hashnode.com/res/hashnode/image/upload/v1726210817675/e3c7f492-7b0d-4914-be7a-6cf8dc26524a.png align="left")

On the homepage, you will see a simple search bar. You can type in general queries like “default password” or “webcam” to see what Shodan can find.

For example, typing “default password” will list devices with default settings. They are vulnerable to unauthorized access.

Shodan also allows you to filter results with specific parameters. For example:

* **Search for specific devices**: If you’re looking for webcams, you might type “webcam country:US”. This query will return webcams located in the United States.
    
* **Search by IP address:** To see details about a specific IP, type the IP address into the search bar.
    
* **Search by port:** To find devices with a specific port open, use a query like “port:22”. This will find devices with SSH (port 22) exposed to the Internet.
    

After executing a search, Shodan will present a list of matching devices. Each result includes the IP address, open ports, and the software on the device.

For example, a search for “port:22” might find SSH servers and their configuration details.

![Shodan search results](https://cdn.hashnode.com/res/hashnode/image/upload/v1726210856807/253a6a4c-e418-4a8f-ad3d-553a4a339686.png align="left")

### How to Use the Shodan Command-Line Interface (CLI)

For advanced users, Shodan provides a command-line interface (CLI). It lets you search and automate tasks.

**Note: API usage may be limited based on your account and you might have to pay to use it.**

Before you can use the CLI, you will need to install it. You can do this using Python’s package manager, pip. Open your terminal and type the following.

```plaintext
pip install shodan
```

Once installed, you can see if it works by trying the help command.

```plaintext
shodan -h
```

![Shodan help](https://cdn-images-1.medium.com/max/1600/1*j-AeWDwmtsLvczJEj1U2yQ.png align="left")

Now you have to add your Shodan CLI with your API key. You can find your API key on your [Shodan account page](https://account.shodan.io/). To set it up, use the following command:

```plaintext
shodan init YOUR_API_KEY
```

Now you can start searching. Here’s an example of a basic search:

```plaintext
shodan search "default password"
```

This command will return devices with “default password” in their banners. This often indicates poor security practices.

You can search for devices with specific characteristics as before:

```plaintext
shodan search "port:80 country:US"
```

This command finds web servers (port 80) located in the United States.

To get detailed information about a specific IP address, use this command:

```plaintext
shodan host 8.8.8.8
```

It will return all known data about the specified IP. This includes open ports and detected services.

To see more commands or debug CLI issues, [here is the official documentation from Shodan](https://help.shodan.io/command-line-interface/0-installation).

### The Good, the Bad, and the Dangerous

Shodan is a double-edged sword. It’s a powerful tool for cybersecurity professionals. It also poses significant risks if used with bad intent.

Security teams use Shodan to find exposed devices within their networks. It allows them to patch vulnerabilities before someone can exploit them.

Researchers can track vulnerabilities or malware by monitoring devices on Shodan.

Unfortunately, Shodan can also be a hacker’s dream. Hackers can use Shodan to locate devices exposed to the Internet. These include webcams, servers, and even industrial control systems.

A worrying fact about Shodan is its ability to find industrial control systems. An Industrial Control System (ICS) controls and monitors industrial processes. It’s the “brain” behind machines in factories, power plants, and water treatment plants.

Shodan has found thousands of unsecured, internet-connected industrial control systems (ICS). In some cases, these systems had no password or used default credentials.

Shodan has also indexed thousands of security cameras, database servers, and IoT devices. These raise serious privacy and security concerns. All these can be easily exploited if not properly secured.

To protect your own devices, you must understand Shodan. You need to know how it works and what it can find.

So, how can you prevent Shodan from exposing your devices?

**1\. Change Default Credentials**: Always change the default usernames and passwords on your devices.

2\. **Use Strong Passwords**: Avoid weak passwords. Use a mix of letters, numbers, and symbols, and consider using a password manager.

3\. **Disable Unnecessary Services**: If your device has services you don’t use, disable them. This reduces the number of potential vulnerabilities.

## Conclusion

Shodan is a powerful tool. It’s a reminder that any device connected to the internet is potentially exposed. It offers useful insights for cybersecurity experts but also an opportunity for cybercriminals.

Knowing what Shodan can do should make you take cybersecurity seriously. In a world where everything is connected, your security is only as strong as your weakest device. Stay informed, stay updated, and most importantly, stay safe.

*Join the* [***Stealth Security newsletter***](https://www.stealthsecurity.sh/) *for more articles on offensive and defensive cybersecurity. To learn how to build a career in Cybersecurity, check out* [***The Hacker's Handbook***](https://book.stealthsecurity.sh/)*.*
