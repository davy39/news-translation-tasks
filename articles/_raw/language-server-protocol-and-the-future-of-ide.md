---
title: How the Language Server Protocol Affects the Future of IDEs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-02T15:19:25.000Z'
originalURL: https://freecodecamp.org/news/language-server-protocol-and-the-future-of-ide
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/screely.png
tags:
- name: ide
  slug: ide
- name: programming languages
  slug: programming-languages
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: "By Mehul Mohan\nThe release of Visual Studio Code single-handedly impacted\
  \ the developer ecosystem in such a way that there's no going back now. It's open\
  \ source, free, and most importantly, a super powerful tool. \nBut with VSCode,\
  \ Microsoft gave life..."
---

By Mehul Mohan

The release of Visual Studio Code single-handedly impacted the developer ecosystem in such a way that there's no going back now. It's open source, free, and most importantly, a super powerful tool. 

But with VSCode, Microsoft gave life to another super important thing back in 2016, which is less well-known. It is called Language Server Protocol.

# What is Language Server Protocol?

Language Server Protocol (LSP) is a protocol or a way of talking to language servers (just like HTTP or FTP). 

Language servers are special programs that run on regular servers. They take in the meta state of editor in which you're coding (for example, where your cursor is currently inside the editor, which token you're hovering over right now), and return a set of actions/instructions – what token should appear next, what should happen when you CMD/Ctrl-click that token, and so on.

This communication happens using a set of rules defined by the protocol. Language Server Protocol could be thought of as a trimmed down version of HTTP and communicates only on JSON-RPC.

# Why is LSP required?

You see those fancy autosuggestion and error messages popping up in VSCode all the time? And how, just by adding a simple extension from the VSCode marketplace, you get all that IntelliSense power for a completely different language like C, Python, Java, and so on? That comes from LSP.

Support for autocompletion and IntelliSense for HTML/CSS/JavaScript comes baked into VSCode (just like PyCharm comes baked in with Python support). However, the same support for other languages can be implemented using Language Server Protocol for those languages.

![LSP in Monaco editor](https://dev-to-uploads.s3.amazonaws.com/i/pn5c0n3zus769e5fadbk.gif)

# What is JSON-RPC?

JSON-RPC stands for JSON Remote Procedure Call. It is an architecture (similar to how REST is an architecture) but with the fundamental unit being a procedure call rather than an API endpoint in the case of REST.

Here's a simple payload for JSON-RPC:

```sh
// Request
curl -X POST —data '{
  "jsonrpc": "2.0",
  "method": "runThisFunction",
  "params": [ "some-param", 2 ],
  "id": 1
}'
// Response
{
  "jsonrpc": "2.0",
  "result": "codedamn",
  "id": 1
}

```

In this example we're sending a JSON encoded payload following RPC specification. If the server is configured to handle JSON-RPC correctly, it will execute the method `runThisFunction` with the passed parameters and return the result in the form as shown.

# LSP + JSON-RPC

LSP uses JSON-RPC to communicate to remote server. It follows this:

```sh
Content-Length: <bytes of JSON>\r\n\r\n<json-payload>

```

To write an example, it'll be like this:

```sh
Content-Length: 78

{"jsonrpc":"2.0","method":"runThisFunction","params":["some-param",2],"id":1}

```

The LSP requires you to pass the `Content-Length` header followed by 2 `CRLF` tokens `\r\n`. When the running language servers like `ccls` receive this, they'll respond with an appropriate message:

![ccls server](https://dev-to-uploads.s3.amazonaws.com/i/7zxtfv0a4c15mqxdl2mr.png)

Of course, in the example above, you can see that `ccls` says that there is no method called `runThisFunction`. But you can see that the remote server also responds with a `Content-Length` header with a JSON-RPC specification.

# Why does all this matter?

With the introduction of a formal protocol LSP, Microsoft reduced the famous `M x N` problem to an `M + N` problem.

M = Different languages (C, C++, PHP, Python, Node, Swift, Go, etc.)  
N = Different editors (VSCode, Eclipse, Notepad++, Sublime Text, etc.)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-02-at-8.30.21-PM.png)

Previously, for M editors to support N languages, you need M*N solutions. That is, every editor had to implement native support for every language differently.

With the introduction of LSP, the editor only needed to implement support for the Language Server Protocol. Once it did, anyone who makes a language server (following the LSP standards) can be seamlessly integrated with the editor, without the editor ever intelligently "knowing" what language it is working with!

# The future of IDEs

As more and more languages come out with their language servers, people will have more ability to choose the editor they like best. 

No longer will you have to stick to only XCode for Swift development, or PyCharm for Python. Not only this, but LSPs can also be implemented straight into JavaScript to support IntelliSense in the browser like I'm doing at [codedamn](https://codedamn.com), a platform for developers to learn and grow! It's an exciting time to be alive!

Peace,  
Mehul

