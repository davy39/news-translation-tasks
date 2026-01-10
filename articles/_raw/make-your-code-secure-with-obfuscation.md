---
title: What is Code Obfuscation? How to Disguise Your Code to Make it More Secure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T18:05:58.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-secure-with-obfuscation
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/code-obfuscation-woman-coder.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: "By Andrej Kovacevic\nIn the earliest days of computing, developers didn't\
  \ have to worry about networks. They could just focus on making sure their software\
  \ served its intended purpose and didn't crash too often. \nAnd the average person\
  \ who came into c..."
---

By Andrej Kovacevic

In the earliest days of computing, developers didn't have to worry about networks. They could just focus on making sure their software served its intended purpose and didn't crash too often. 

And the average person who came into contact with that software wasn't a threat. Most users wouldn't even bother reading the [user manuals](https://manualsbrain.com/en/) shipped in the software's box, let alone scouring the code for vulnerabilities.

Then, the internet came along and changed everything.

Almost overnight, computer networks became interconnected. And as the complexity grew, so too did the odds that someone would find their way into those networks who didn't belong there. 

And more often than not, those people would have the skills needed to exploit flawed code.

And that brings us to today. It's a time of unprecedented cybersecurity threats. And news of cyber-attacks seems to come daily.

In response, network managers deploy increasingly [sophisticated defensive systems](https://www.cynet.com/xdr-security/understanding-xdr-security-concepts-features-and-use-cases/) to harden their networks against intruders. And they now expect software developers to go the extra mile to secure their code to prevent unauthorized access.

And yet, the hardening of computer code still isn't taught much in coding schools. But it's becoming a must in modern application development. 

To help remedy that, in this article I'll explain what code obfuscation is. And I'll also give you an overview of the six most crucial code obfuscation techniques in use today to get you started on the path to writing more secure software.

## What is Code Obfuscation?

As its name suggests, code obfuscation refers to a series of programming techniques designed to disguise elements of a program's code. It's the primary way that programmers can defend their work against unauthorized access or alteration by hackers or intellectual property thieves. 

And most importantly, code obfuscation techniques may alter the structure and methods a program uses to operate, but they never alter a program's output.

The trouble is, many code obfuscation techniques can add to a program's overhead and increase execution time. 

For that reason, it's critical to understand which techniques are relatively penalty-free and which can cause performance issues. Once you know the costs, it is possible to balance protection and performance in a real-world application.

Here are the six most-used code obfuscation techniques employed today.

## 1. Remove Superfluous Data

The first code hardening technique that should be applied in every case is to get rid of everything in your code that's not necessary.

Doing this will streamline your codebase and reduce the attack surface you're defending. 

This means removing redundant functions, debugging information, and as much metadata as possible. In short – anything that might give an attacker a roadmap that could lead them to a vulnerability.

## 2. Transform the Data

The next thing to do is to transform the data that your code processes to render it unrecognizable. 

Tactics like replacing values with expressions, altering the format of the data storage you use, or even [using binary versions](https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050915X00329/1-s2.0-S1877050915032780/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCA8%2FbMNDwcr1XOpo7DeKQbXz83LMbSk24ZV4X8rpilJAIhAMsqbvQN5HTdd4zWOOXRcppnOAGYNVu6C5uAYw5uTykJKrQDCGUQAxoMMDU5MDAzNTQ2ODY1IgwV2aDE0qbSu9kgEtoqkQNrSQrQUa0Ja52RXLYbP8r9sekXFQ0TAfCAtrkTNTsiB%2FLgqZqmG%2BwY0Kz%2BJaud%2BDxrauuZZSE1dSTLcm6vNrlpabyNmPrIG%2BtY6INcm80IfLxpaTdfsTSPXXMrXykzY%2BXqDnQmfqGJ59rtulshtpTckzFN9HpY%2BrSdWWvXLklaiZdWVhz%2BxnG6jN%2F1wL%2FXwybqOBaKbmkremuUj09B1lUN32dOUe5qRnIGrf8qYyATGnbZHoMT5kz7Sq3P7F0Fy5yW7UjQVPSu2ABitFgXZVoUwRchriev6Aki6UBJ0mSxrUUHmNrXSvk5jETjuYMm8q0U3N%2B9xrYx27PPsWomPqlCOKGVlBaPoZmAmqo0BLamet3eY2Rp%2Bk0%2BPQNRqZQa8yhTDzfnRWYxJl7uLILFWe%2FjlRmILnxq%2BjmItjt6SjRaAlc7noGEv%2BNjN3AEpDC%2FcqACzJVqndzDS9V71FxSWN7klUdd4QUGLocw54pGHq1r7wuTgodPJjqnrIFmvB0iV296BFNtyj2fQjJcoeq0XlMPhDCssab9BTrqAaw64rV02aRHt4lBwTwoJJiSEDf%2Bt%2FiOQqAU%2FV%2FcX7eMhzYZKteQE52uUCMH0BO6g2L2a9MKOiRlZ6ryvpJac90eb7X9mvnvMbNcDWv3xxhfNRmlSOUDX48tLpbhKVzqncl8aZZJIPlXWKlHYOeIYLasptLMrU%2FzbqJjrOrFBqiazYHtPMI6XS1JeaUD8DmCEdGIJ9CYTLJiRyKD9dGiznGfZ%2F1L9A9zFZt%2FsDc6MybWNxTAHd3hrmvoF7zB2hNY6%2FTDdYmQv2TpAPw%2FzqbvheXrzjjIwDuQyn2mcNNz2i2U83N0uCCcbDsOvw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20201109T195727Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYXEEHGGB3%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=11d88d2c5915b160162922c34b6771ae59e987e847cb44a383faa6fcc111caa7&hash=2dbe5efcb60f98ccf53ef748c7791766189f5422149ec208f49987fac4baa432&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1877050915032780&tid=spdf-2b92f167-2272-4886-a286-4077d881be1a&sid=a173bdc61ca7a346b139b114192a80c41b85gxrqa&type=client) of your code's numbers all add complexity. And that complexity will make it difficult for anyone reverse-engineering your code to get anything useful out of it.

For example, you might use string encryption to make plain text strings in your code unreadable. String encryption can use simple base64 encoding, which would turn this code:

```js
String s = "Hello World";
Into:
String s = new String(decryptString("SGVsbG8gV29ybGQ="));
```

Although it isn't hard for an experienced programmer to spot what's going on here, having to deal with decrypting numerous strings is time-consuming and frustrating. 

And when combined with some of the other code obfuscation techniques, data transformations are an effective first line of defense.

## 3. Use Process Order Obfuscation

One of the challenging requirements of obfuscating code is that you still need your code to work as intended when you're done. 

But there's nothing that says you have to execute your code in any logical order. If you mix up your code's order of operations, you can still achieve the right result – but make it far harder for a third party to understand what your code is doing. 

The only caveat is that you have to be careful not to create too many meaningless loops and dead ends because you may accidentally slow down your code's execution time.

As an example, take a look at the following snippet, which calculates the sum and average of 100 numbers:

```js
int i=1, sum=0, avg=0
while (i = 100)
{
sum+=i;
avg=sum/i;
i++;
}int i=1, sum=0, avg=0
while (i = 100)
{
sum+=i;
avg=sum/i;
i++;
}
```

By adding a conditional variable, it's possible to disguise what the code is doing. This is because an analysis of the function would require knowledge of what's being input into it to begin with. 

In the following snippet, the conditional variable 'random' creates a more complex code structure that makes it far harder to decipher:

```js
int random = 1;
while (random != 0)
{
switch (random)
{
Case 1:
{
i=0; sum=1; avg=1;
random = 2;
break;
}
case 2:
{
if (i = 100)
random = 3;
else random = 0;
break;
}
case 3:
{
sum+=i;avg=sum/i ; i++;
random = 2;
break;
}
}
}
```

## 4. Try Debug Obfuscation

Sometimes, a determined attacker can learn all kinds of useful information about your code by examining its debug information. 

And in some cases, they might find the keys to unraveling some of the other obfuscation techniques you're using. 

So wherever possible, it's a good idea to remove access to debugging information. And when that's not an option, masking any identifying information in the debugging report is essential.

## 5. Use Address Randomization

For almost thirty years, errors related to memory handling have been the most common software vulnerabilities hackers exploit – even though every programmer knows that the problem persists. 

And it's not just among beginners. Around [70% of the vulnerabilities in Google's Chrome](https://www.zdnet.com/article/chrome-70-of-all-security-bugs-are-memory-safety-issues/) web browser stem from memory errors.

The reality is, it's all but impossible to prevent all memory programming errors, especially if you're using [languages like C and C++](https://neosmart.net/blog/2018/modern-c-isnt-memory-safe/). But what you can do is include some memory randomization features in your code that will help. 

At execution, if your code and data's virtual addresses get assigned random values, it gets much harder to find and exploit any unpatched vulnerabilities.

Plus, it adds another benefit, too. It makes it so that even a successful hack of your code is difficult – if not impossible – to replicate. That alone makes it much less likely that an attacker will waste their time trying to hack your software.

## 6. Rotate the Obfuscated Code

As much as the above techniques work to frustrate attackers, they're far from a perfect defense. Anyone with enough time and skills will still find a way to defeat them. But that brings us to one of the most essential obfuscation techniques of all.

Since all obfuscation techniques aim to increase the complexity of an attacker's work, anything you can do to set them back to square one is a great defensive measure. So, to keep your code protected, use the internet to your advantage.

You can issue periodic updates that rotate the nature and specifics of the obfuscation techniques you're using. Every time you do, all the work someone may have been putting into cracking your software becomes a waste of time. 

If you rotate your obfuscation tactics often enough, it won't be worth it for anyone to try and keep up an analysis long enough to succeed.

## Security Through Obscurity

The bottom line here is that there's no such thing as 'unhackable' code. No matter how hard a programmer tries, there's always going to be a vulnerability somewhere. Not that you shouldn't keep trying, though.

But in the real world, your code doesn't have to be perfect. It just has to be hard enough to crack that nobody in their right mind would bother trying. And for those who aren't in their right mind, it just has to be complicated and time-consuming enough to keep them at bay.

And that's just what the six tactics above can help you accomplish. But remember, no defense comes without a cost. When deploying these options, make sure to weigh the execution-time penalties they may create against the benefits they provide. 

If you're working on something especially sensitive, throwing every possible curveball might be worth it. But if you're writing a quote of the day generator – maybe don't worry as much.

However you choose to proceed, though, don't ever forget to take the time to harden your code in one way or another. It's just the right way to do things in a world filled with cybersecurity threats around every corner.

_Featured photo by ThisIsEngineering from Pexels._

