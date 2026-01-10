---
title: Mistakes you’ve probably made in your coding task for a job interview
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-03T16:11:33.000Z'
originalURL: https://freecodecamp.org/news/mistakes-youve-probably-made-in-your-coding-task-for-a-job-interview-28e6db6a68ad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RGs1JM8T1Dmoqa23oe01Iw.png
tags:
- name: GitHub
  slug: github
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Michael Lazarski

  You got this task from that company you want to work for! You are hyped and you
  immediately start to work on it. After a long night of coding, you are done and
  you think you implemented the best thing ever!

  So you send the task ba...'
---

By Michael Lazarski

You got this task from that company you want to work for! You are hyped and you immediately start to work on it. After a long night of coding, you are done and you think you implemented the best thing ever!

So you send the task back to the company. After some time you get an email from that company. You are confident that you aced it and they are sending you a draft of the contract!

Then you read the E-Mail and you can’t believe what you are seeing. It’s just a thank you E-Mail and that they decided to go with someone else.

What went wrong and how could you improve? Let’s dig into it!

#### Mistake 1: you did not read the task carefully enough

Sometimes just one word can change the meaning of the task completely. Perhaps you did not catch the word responsive the first time, or you just think that you got it but you don’t get what the task is really about.

So read the task a few more times to really understand it.

#### Mistake 2: you started implementing the task without fully understanding the task

So you have fixed mistake 1 but you’re still having questions? Ask the person you are in contact with. It’s not bad to ask! It’s the opposite as it shows the company that you care about a good product and that you don’t want to waste their time.

If they react negatively, then I would stay far away from that company because this is the first sign of a toxic environment where nobody can ask anything.

#### Mistake 3: you are not using Git (or any other version control system)

Please! Please! Don’t send a 60 Mb ZIP file via E-Mail with the complete `node_modules` Folder. OSX does not like to unzip node_modules, so the person who will review your code will not even get a chance to look at your code.

Use Git instead. If you don’t know Git then this is the best chance to learn it because a lot of companies use Git. Sooner or later you will have to learn it.

#### Mistake 4: you didn’t write good commit messages

You are now using Git, good. Don’t do everything in one commit. Companies will look at your `git log` to read the commit messages. You have to remember you will work in a team, and in a team good commit messages matter. It’s important for the other team members, and for you in 2 weeks when you have to find a commit or understand what happened in that part of the application. So commit often and write good short messages.

#### Mistake 5: you forgot the .gitignore file

This comes back to mistake number 3. If you don’t have a .gitignore file everything in that directory will be added to Git. So again you will send the complete insides of your `node_moudes`. Nobody wants your `node_modules`.

Here is a good collection of gitignore files: [https://github.com/github/gitignore](https://github.com/github/gitignore)

#### Mistake 5: you are sending a Zip file via E-Mail

I mean as a developer you have to know GitHub, right? So use it! Put your code on GitHub and send the GitHub link to your contact person. Your contact person will be very thankful for that.

* No corporate spam filter will remove the zip file.
* Yes even in 2019 E-Mail’s have a file size limit and you may be just hit that limit
* It is easier to have a first look at the code without downloading a zip file.
* It is easier to share with other developers in the company. Usually, more than one developer will look at your code.

#### Mistake 6: you don’t have a README.md file or it is not good

Github will render the README.md file and it will be shown on the main page of your repo. Write some meaningful content in it. For example, the task name or explain what this task does, maybe add the dependencies…and this brings me to my next point.

#### Mistake 7: you didn’t write instructions on how to start your task

Yes, I can go the package.json file and have a look at your scripts and if they are meaningful I can figure out which of them is the right one to do or maybe not. So please write down in the README.md how to set up and start your task so I can run it.

#### Mistake 8: you did not include a working link to your task

“But why should I do that when you just told me that I should write instructions on how to run it?” is what you are asking yourself right now. To make reviewing your task as frictionless as it can be, so the reviewer is not annoyed that they had to figure out for one hour how to see if your code is actually doing what was mentioned in the task.

Put a working version anywhere on the internet where you can give the reviewer a link. Heroku, GitHub pages, AWS or Azure are just a few which also have free services for doing that.

#### Mistake 9: not removing old/unneeded files from the task

Don’t be that developer that has an `_old` folder somewhere in the git repository. As a reviewer of your code. What should I do with this folder? Should I look into it or maybe don't? Why is it there? I don't even know what to say. So please remove all unneeded and old files from your code.

#### Mistake 10: you didn’t write a nice E-Mail with the link to your GitHub repo

Don’t just send an empty E-Mail with a link. This can be viewed as very rude. I mean on the other side is also sitting someone human. Write at least: Hello X, how are you? I hope everything is fine. Here is the link to my finished task [THE LINK]. Have a nice day. Best wishes, Michael.

### Mistake 11: Don’t say something is easy

“Javascript is easy and not hard”. I don’t know why people say this but it is a common thing. You can replace Javascript with anything you want. Everything is easy and also hard at the same time. Driving a car is easy but driving a Formula 1 car is hard.

Why does this matter? It shows the interviewer that there is some kind of elitism in your mind. What do I mean by that? It’s the same thing when people who are new to programming are asking: “What is the best way to do XYZ?”. There is neither the best way or one way. There is not such a thing as the best programming language to use or to learn.

So if you learned C++ you now look down on Javascript developers, that shows that you feel like you are in some elite squad. It just means that you learned one tool from your toolbelt. You now can use the Claw Hammer but not the Sledgehammer. Yes, it will be easier to now learn the Sledgehammer but both hammers have their own pros and cons.

So please don’t say that things are easy. Most probably they seem easy because you don’t fully understand them.

#### Mistake 12: you don’t write tests if the job specs say you have to know how to test

It’s always a plus to show that you can write tests. They don’t have to be perfect. You don’t have to have 100% code coverage. Just write some simple tests that are testing your core functionality and you probably have a big plus point.

#### Mistake 13: not splitting your code into smaller files

If you send one big file with 2000 lines of code it is hard to review that.  
As someone who has to check your code, it is hard to see what is happening in this file and how the code flows. Probably you also have to scroll from top to bottom. Better try to split your code into smaller files. This will also be important later for work. Nobody wants code that only you understand but none of your team members. Please split it up. It’s so much easier to review.

#### Mistake 14: you don’t have code comments or you just write what the next line does

This one I see people do even after some years of working as a developer. Comments like: `// Loops through an array` and the next line is `Array.forEach()`. Yeah hello, Captain Obvious. It would be better if you would describe what this loop does in a more abstract way. `// preparing data for sending it via AJAX` or something in this direction. So people know what the intent of the code is.

#### Mistake 15: your code is all over the place

```
const array = [ 1, 2];
```

```
array.forEach((a ) =>{ a = a+ 1;
```

```
console.log(a) ; });
```

This is really hard to read and also shows that you are working very carelessly. Today we have tools like `eslint` and `prettier`. Every bigger editor and IDE has this build in or you just need to install a plugin/extension. So please use it.

#### Mistake 16: you are not naming your variables properly

```
const b = true;const a = [];
```

This is not easy to read and not helpful to understand what `b` is.  
Way better naming could be:

```
const isReady = true;const listOfPersons = [];
```

Again these are just examples and every team will have its own way of naming things. Of course, you can not guess that style, but just do what you feel is a meaningful name and stick to one style.

#### Mistake 17: you are just commenting out old code

I have seen this often and I still don’t understand why people are doing this. You have a file with 100 lines of code and 70 lines are just old code which is commented out and 30 lines of an actual implementation.

Should I read the old code? Should this show me that you did it the first time wrong and then reimplemented it? Nobody is perfect and writes the first time the perfect code. So please delete this code. If I want to see if you refactored the code I should see it in the git commits with git commit messages where I can understand what you did.

#### Mistake 18: you did not check if your code is still running

This happens all the time. You get one E-Mail from an interviewee on Sunday evening. You go to work on Monday and start to check the code and suddenly you get a second E-Mail with some updates in the code. You also get a promise that this time it really works.

So please, before you send your code. Stop the program, clean the cache, install the dependencies and start it again. If it then still works then you can say that you’re ready.

#### Mistake 19: you changed something and did not check if it is still running

For our full-stack developers, we have a task where they need to save variables in a database. They can choose the database, the schema and how to save the variables. We just say this has to be saved. This is where people change the code and don’t check if after the changes it still really saves to the database. For example, they change the schema or they just try it with a small file, etc.

Again before you send your task back, check if all functions are still working as they should and try to break stuff. Nobody is saying that you need to catch every edge case but at least the most common things a user can do.

#### Mistake 20: you did not prepare for the coding interview

Some time has passed between sending the task and the actual interview, maybe a week or more. Do you really still remember what you have done in that task? Like why did you solve this task in that way and what was your thinking when you implemented your task?

One of the goals of this entire process is not to see how good you are as a programmer but whether you fit the team and if you a team player. It’s more about your soft skills than your coding skills. Please read your own code before you go to the interview part.

These are just a few examples I have seen. Do you have more? Comment down below!

Maybe you want me to review your code? Or give you some tips on how to help you? Just contact me on any of my social media accounts and I can try to help you. Of course, I can not do the task for you but I can help with everything else!

**Thanks for reading!**

**Say Hello!** [Instagram](https://www.instagram.com/lampewebdev/) | [Twitter](https://twitter.com/lampewebdev) | [LinkedIn](http://(https://www.linkedin.com/in/michael-lazarski-25725a87) | [dev.to](https://dev.to/lampewebdev)

