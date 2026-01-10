---
title: What is FTP? File Transfer Protocol and FTP Server Meaning
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-21T01:01:16.000Z'
originalURL: https://freecodecamp.org/news/what-is-ftp-file-transfer-protocol-and-ftp-server-meaning
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/thisisengineering-raeng-zBLtU0zbJcU-unsplash--1-.jpg
tags:
- name: computer network
  slug: computer-network
- name: Security
  slug: security
seo_title: null
seo_desc: "FTP stands for File Transfer Protocol. This is a network/communication\
  \ protocol for transferring files between computers over a TCP/IP (Transmission\
  \ Control Protocol/Internet Protocol) network. \nExamples of TCP/IP networks are:\n\
  \nHTTP (Hypertext Trans..."
---

FTP stands for File Transfer Protocol. This is a network/communication protocol for transferring files between computers over a TCP/IP (Transmission Control Protocol/Internet Protocol) network. 

Examples of TCP/IP networks are:

* HTTP (Hypertext Transfer Protocol).
* HTTPS (Hypertext Transfer Protocol Secure).
* FTP (File Transfer Protocol).

## How Does File Transfer Protocol Work?

To transfer files between computers using FTP, you have to visit an FTP server (I'll explain what an FTP server is below).  

Depending on the type of server you visit, you may be required to enter a username and password in order to access the files in the server. Server connections that do not require any sort of authentication before accessing the files are referred to as anonymous FTP.

When the user has successfully visited/logged in to an FTP server, they can either download or upload files on the server.

There are two general ways of gaining access to an FTP server:

* Through a web browser. You can do this by typing the address of the server in your browser. This address could look this: ftp.myftpfiles.com or https://www.myftpfiles.com. Once you are on the server, you can then interact with files uploaded to the server by the owner.
* Through an FTP client. We'll discuss FTP clients in the next section.

## What Is an FTP Client?

An FTP client is software that creates a connection between the computer requesting access and the server where the files are stored.

There are numerous FTP client software available for use. They provide a graphical user interface (GUI) which we can interact with. 

Below, we'll see what an FTP client looks like and how we can use it. We'll be making use of [FileZilla](https://filezilla-project.org/).

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--270--1.png)

In the image above, there are different text fields. The `Host` text field is where the address of the server is typed in. 

The `Username` and `Password` text field are for servers that require authentication before granting access. 

The `Port` text field is usually 21. This is a dedicated port for FTPs.

Once you've filled the necessary text fields, you can then click `Quickconnect` to connect to the server.

On the left side of the software is the `local site` which is my computer with a list of the existing directories. 

On the right is the `Remote site` which is where all the information and files in a server will be shown.

## What Is an FTP Server?

An FTP server is basically the computer where all the files are uploaded initially. Every server has an FTP address which a user can visit over a TCP/IP through a browser or an FTP client. 

The server allows the visitor to download and upload files.

## Are FTP Servers Secure?

Although a lot of FTP servers require authentication, they are not secure as the protocol lacks encryption. This makes it more likely that the files stored on an FTP server could be accessed by a third and unwanted party.

The most preferred and more secure protocol to FTP is the SFTP which stands for Secure File Transfer Protocol. Just like HTTP and HTTPS.

SFTP is more secure because the data stored on the server is encrypted. 

Other alternatives include:

* FTPS (File Transfer Protocol Secure).
* HTTPS (Hypertext Transfer Protocol Secure).
* AS2 (Applicability Statement 2).

## Advantages of Using FTP

Here are some of the advantages of using FTP:

* Faster transfer of files.
* Supported by numerous hosts.
* Supports transfer of large files.
* Ability to schedule transfers.
* Transfers can be resumed when interrupted.

## Disadvantages of Using FTP

Here are some of the disadvantages of using FTP:

* FTP servers lack security.
* Major browsers like Chrome and Firefox no longer support FTP.
* User credentials and files are not encrypted.
* Some servers may contain harmful files.

## Conclusion

In this article, we talked about the File Transfer Protocol which enables us to transfer files between computers over a network.

We saw what an FTP client and FTP server are. We also talked about why FTP servers are insecure and other secure alternatives we can make use of.

Lastly, we saw the advantages and disadvantages of using FTP.

Thank you for reading!

