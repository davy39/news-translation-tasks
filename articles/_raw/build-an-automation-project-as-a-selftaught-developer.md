---
title: How I Built an IT Automation Project as a Self-Taught Software Developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-23T14:55:00.000Z'
originalURL: https://freecodecamp.org/news/build-an-automation-project-as-a-selftaught-developer
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Python-2.jpg
tags:
- name: automation
  slug: automation
- name: projects
  slug: projects
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: "By Kushal Bhatia\nI have always been obsessed with how technologies work,\
  \ namely computers. But my passion was hindered by a voice in my head that echoed\
  \ time and time again – \"you are not smart enough to study computer science.\"\
  \ \nI thought I needed t..."
---

By Kushal Bhatia

I have always been obsessed with how technologies work, namely computers. But my passion was hindered by a voice in my head that echoed time and time again – "**you are not smart enough to study computer science."** 

I thought I needed to be highly skilled in quantitative mathematics and be a genius to even consider a computational endeavor, let alone pursue a full-time career in Software Development. 

That all changed in March 2020. I was laid off from my job as a Business Development Manager at a leading Data Analytics and Marketing Automation startup, due to the Coronavirus pandemic. 

It was then that I decided to embark on a journey to finally pursue my dreams of becoming a Software Developer. 

You see, I graduated from the University of California, Los Angeles in 2012 with a Bachelor of Arts in Political Science, assured that I would go on to law school and become a lawyer. 

Since then, I have worked for a number of startups holding numerous roles, including Technical Account Coordinator and Business Development Manager. I even dabbled in the high-powered world of Finance, working as an Investment Banking Analyst for a few years. 

But none of these jobs even remotely appealed to me, and I knew I needed a change for good.

## Roadmap to Becoming a Software Developer

I started my Software Development Journey by using two websites: [freeCodeCamp](https://www.freecodecamp.org/) and [The Odin Project](https://www.theodinproject.com/). Through them I learned HTML, CSS, Git, Bash and Github. 

This was my first real entry into the unique world of technology, where I built mini projects, such as re-creating the Google Homepage. I would use Bash commands, then push my Git changes to GitHub. It was fascinating to see something tangible come to life with just a few lines of code! 

Because HTML and CSS are markup and styles languages, I had to learn a true Programming Language. After thorough research online (mostly Reddit), I decided on Java or Python. I chose the latter.

I began to read two introductory books on Python which really got me excited about this beautiful language. They were _Automate the Boring Stuff with Python_ by [Al Sweigart](https://twitter.com/AlSweigart) and _Python Crash Course_ by [Eric Matthes](https://twitter.com/ehmatthes). 

These two authors are as brilliant as they are hilarious, and I thoroughly enjoyed going through each chapter, completing the requisite assignments.

I knew the basics at this point, but I wanted to learn how to build with this newfound knowledge. 

So I enrolled in a five course specialization on Coursera called _[Python for Everybody Specialization](https://www.coursera.org/specializations/python)_ by the great Charles Severance, aka [Dr. Chuck](https://twitter.com/drchuck). This was exactly what I need to bridge the gap, between beginner and intermediate Python. 

That specialization took me almost two months to complete. I learned SQL, Internet Protocols, JSON, XML, and a variety of Python libraries, including _[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)_ and _[Urllib](https://urllib3.readthedocs.io/en/latest/)_ (used for web scraping). 

Dr. Chuck is an absolute legend in the world of technology, and it's no surprise that his courses are amongst the most enrolled in on Coursera. 

At this point, I had enough knowledge in HTML, CSS, SQL and Python to confidently say that I was an Intermediate Software Developer. 

![Image](https://www.freecodecamp.org/news/content/images/2020/10/cover.jpeg)
_Time to create a meaningful project!_

## How (and Why) I Built my IT Automation Project 

At this point, though, I realized that I had not created anything meaningful that would catch the eyes of potential employers. Nothing that I could post on GitHub, that would be cloned hundreds of times, forked thousands of times. In a sense, my open-source presence was non-existent. 

I sifted through the internet, searching for project ideas in Python. Sure, I could have created a web-scraper or another boring Twitter bot, but I wanted to build something that was different. 

Racking my brain, I thought back to my previous job as a Business Development Manager. There, I was tasked with the arduous and mundane job of finding duplicate accounts on our Salesforce CRM (there were over a million records!). 

How I wished I could have written a simple script to make my computer do the work in minutes, instead of weeks.

Then it came to me – why don't I build a utility that would go through all of the files on my computer and look for duplicates? The average person likely has a ton of files on their computer, many of which are created multiple times and completely forgotten about. 

Ideas started to pour out. I thought of many use cases for industries such as Finance and Healthcare that could definitely utilize something like this to go through their records in no time. 

I decided to jump into VS Code, create a .py file, and name it duplicate_files. It was finally time to wear my Software Designer hat and construct my masterpiece.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screen-Shot-2020-10-22-at-2.50.59-PM-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screen-Shot-2020-10-22-at-2.55.32-PM.png)
_Snippet of my Duplicate Files Utility on GitHub_

## Building the Duplicate Files Utility

One of the hardest parts about designing your project is deciding what libraries you want to use. 

* I knew that I wanted to access the files on my computer, so I added the OS library. 
* I knew that I wanted to find the unique hash of each file to differentiate them, so I chose the hashlib library. 
* I knew that I wanted users to provide their own arguments when running this utility, so I picked the argparse library. 
* And of course, I wanted to time the total processing time of the utility, so I added the time library.

Another difficult part about designing your project is deciding what data structures work best. After some trial and error, I chose two dictionaries and one list (that would apply user-ignored directories across Windows, macOS, and Linux). 

It was extremely important to me that this did in fact encompass **"A simple yet powerful program that searches for unique duplicate hashed files on your Windows, mac0S or Linux computer"**. 

Which I why I wanted to use the basic building blocks Python had to offer - loops, conditionals and **FUNCTIONS**. I didn't use any complex Object-Oriented Programming that you might see in other projects. This program simply has three major functions, that's it!

I wrapped up my design by adding a README file, and also included a .gitignore file every time I pushed my changes to GitHub. I thoroughly tested this program via the VS Code Debugger (editing the launch.JSON file), as well as on multiple computers that had all of the major operating systems. 

In fact, this program was run on a Windows machine, where the given path had a 6GB file inside. The program seemed to stop temporarily when it reached that file, then continued and finished in blazing fast time. 

In that example, the path had 100,000 files, and finished in five minutes. Months ago, I was amazed with how something I wrote in basic HTML and CSS was displayed on a website. 

After running this program present-day, I am truly fascinated with the speed and complexity with which computers can run when given just a few lines of code!

![Image](https://www.freecodecamp.org/news/content/images/2020/10/naval.jpg)
_Naval Ravikant, one of my idols_

## Conclusion

It has been an incredibly difficult, yet rewarding 8 months (and counting) learning how to become a Software Developer. 

For a while, I thought about attending a bootcamp. I even considered a Master's program in Computer Science. 

But with the excellent free and open-source materials available on the Internet, I felt confident that I could learn on my own. 

I want to give a huge shoutout to [Quincy Larson](https://twitter.com/ossia) for motivating me to start my journey on freeCodeCamp. I also want to say thank you to Al Sweigart, Eric Matthes, Charles Severance, and Guido van Rossum, who either directly or indirectly were instrumental in aiding me throughout my journey thus far.

I hope this post accomplishes two things: 

1. That I motivate others out there who are either unsure about what they want to do in terms of a career, or are simply scared, to go out and start coding!
2. That an employer will take a chance on me, so that I can achieve one of my biggest dreams of becoming a Software Developer (albeit a self-taught one).

To conclude: One of my biggest idols, _[Naval Ravikant](https://twitter.com/naval)_, a renowned Computer Programmer, Investor, and Modern-Day Philosopher, has a quote that has always resonated with me. 

> "Learn to sell. Learn to build. If you can do both, you will be unstoppable." 

Well, I've built a career on selling in the Finance and Technology industries, and now I have learned to build. **I WILL BE UNSTOPPABLE.**

You can find me on _[Twitter](https://twitter.com/Kushal_Bhatia),_ _[LinkedIn](https://www.linkedin.com/in/kushalbhatia)_ and _[GitHub](https://github.com/kushalbhatia)._

