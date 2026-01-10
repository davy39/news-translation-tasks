---
title: How to Fuzz Hidden Directories and Files with Ffuf
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-01-19T14:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-fuzz-hidden-directories-files-with-ffuf
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-7.47.41-PM.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: penetration testing
  slug: penetration-testing
seo_title: null
seo_desc: 'Fuzzing is a technique used to test the security of a web application.
  It helps you find vulnerabilities you may not have discovered through other testing
  methods. Fuzzing also improves the overall quality and stability of a web application.

  In this ...'
---

Fuzzing is a technique used to test the security of a web application. It helps you find vulnerabilities you may not have discovered through other testing methods. Fuzzing also improves the overall quality and stability of a web application.

In this article, we will look at what Fuzzing is in detail. You'll also learn about a popular fuzzing tool called FFUF, and we'll go through a step-by-step guide on how to use it to test a web application. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-34.png)

Whether you’re a seasoned pentester or just getting started, this article will give you the information you need to start using fuzzing to improve your web application pentesting skills.

## What is Fuzzing?

First, let’s define what fuzzing is. Fuzzing, in general, is a technique for finding vulnerabilities in software. We do this by providing unexpected or twisted input to the program.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-35.png)
_How Fuzzing works_

A simple example would be to generate a list of random file names and use fuzzing to see if they exist on the website. Another example would be to fuzz a login form with random inputs to see if we can crash the web application.

During a fuzzing test, we bombard the software with a large number of randomly generated inputs. We then observe the software to see how it handles these inputs.

If there are any unusual behaviors or errors, it means there is a vulnerability in the software. We can use fuzzing to test for a wide variety of vulnerabilities, including input validation issues, access control problems, and other types of security weaknesses.

## What is Ffuf?

FFUF (Fuzz Faster U Fool) is a tool that automates the process of fuzzing. Ffuf is designed for security professionals to find vulnerabilities in web applications.

Ffuf does this by sending a large number of requests to a target with various payloads. Ffuf then analyzes the responses and tells us what worked and what didn’t.

We can use Ffuf to test for a wide variety of vulnerabilities, including input validation issues, access control problems, and other types of security weaknesses. 

FFUF is also fast and flexible, allowing us to specify the inputs to use for fuzzing and the parameters for the requests sent to the target web application.

Ffuf is also extensively used in bug-bounty hunting, so if you plan to become a bug-bounty hunter, you will be using Ffuf on a daily basis.

## How to Install Ffuf

Now that you know what Ffuf is, let’s see how to install and work with it.

If you are using Kali or Parrot, Ffuf comes pre-installed. Since Ffuf is written in the Go programming language, you should first install Go before installing Ffuf. 

[Here is the link to install Go](https://go.dev/doc/install) if you don't have it installed.

Once you have installed Go, you can install FFuf by running the command:

```
go install github.com/ffuf/ffuf@latest.
```

Once you install Ffuf, you can check the installation using the help command. You can also use the help command as a reference while working with Ffuf.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-36.png)
_FFUF options_

## How to Use Ffuf to Find Hidden Files & Directories

First, let's see how to find some hidden files on a website. We are going to provide two inputs to Ffuf, one is the URL and the other is a wordlist.

```
ffuf  -u <http://target.com/FUZZ> -w <wordlist>
```

If you don’t know what a wordlist is, [you can find a video here](https://www.youtube.com/watch?v=3gXu3rdH7jw&t=18s&ab_channel=StealthSecurity). A wordlist is just a list of words, in this case, a list of file names we are looking for on the website.

Here is a simple wordlist we can use.

```
index.html
root.html
admin.html
admin
root
upload
assets
favicon.ico
style.css
public
```

You can see that the target URL has the FUZZ placeholder. This placeholder will be replaced with the words in the wordlist. 

For example, if we have index.html in the wordlist, the URL will become [target.com/index.html](http://target.com/index.html). Ffuf will then hit this URL and tell us whether the file exists or not based on the website’s response.

Here is a sample response from Ffuf on running it on a target:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-37.png)
_Fuzzing for hidden files and directories_

This is how Ffuf works: it takes in a wordlist and tries to enumerate the target for the words in the wordlist. Let's see a couple more ways of using Ffuf.

## How to Fuzz POST Requests with Ffuf

FFuf also allows you to specify different request methods and customize headers. This is useful when you are fuzzing APIs and individual web application endpoints.

For example, you can send a POST request with a custom header and a JSON payload.

```
ffuf -X POST
-H "Content-Type: application/json"
-d '{"key": "FUZZ"}' -w wordlist.txt
-u <http://target.com/endpoint>
```

## How to Use Filters and Saving Results with Ffuf

When scanning large web applications, the results can be overwhelming. With Ffuf, you can also use various filters and options to narrow down the results.

For example, to only show responses with a status code of 200, you can use the `-sc` flag.

```
ffuf -w wordlist.txt -u <http://target.com/FUZZ> -sc 200
```

You can also save the scan results to a text file. This can then be imported into other tools like Metasploit or Burpsuite. You can use the `-of` flag to save the results to a text file.

```
ffuf -w wordlist.txt -u <http://target.com/FUZZ> -of results.txt
```

## Ffuf Documentation

Here are some more things Ffuf can do:

* Ability to scan directories recursively
* Advanced response filtering
* Support for GET, POST, and other HTTP methods
* Support for TLS/SSL connections
* Performance optimization for speeding up scans
* Output formatting for easy parsing
* Integration with other tools such as Burp Suite

These are just a few examples of using FFuf, but there are many more options and features available. I encourage you to check out the [awesome documentation](https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html) put together by Codingo.

## Summary

Fuzzing is a technique for testing software by providing it with invalid, unexpected, or random data inputs. This is to make the software behave in an unexpected or insecure way.

Ffuf is a popular tool used for performing web application fuzzing. Whether you’re a pentester or just looking to improve the security of your web apps, this article will give you the knowledge you need to get started with fuzzing using ffuf.

Hope you enjoyed this article. You can find more about my articles and videos on [my website](https://www.manishmshiva.com/).

