---
title: How to block unproductive websites and boost your productivity using JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T16:56:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-block-unproductive-websites-and-boost-your-productivity-using-javascript-20534011cccc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9-xBdZXdd_FT1X-DTTX75A.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Madhav Bahl

  Tired of wasting your time on various unproductive websites? Why not make a script
  which would help you limit the time you spend on these websites?

  Does this sound familiar…?


  Just another day, scrolling through my Social Media feed an...'
---

By Madhav Bahl

Tired of wasting your time on various unproductive websites? Why not make a script which would help you limit the time you spend on these websites?

Does this sound familiar…?

> Just another day, scrolling through my **Social Media** feed and watching memes. I found that it had been been 4 hours since I’d been sitting at the same position and “Doing Nothing”. I hated it! I had to do something about it. It came into my mind, why not make some script which would help me limit the amount of time I spend on these websites?

![Image](https://cdn-media-1.freecodecamp.org/images/0*bIF5jb6o8DpD_JvS.jpg)
_Stop scrolling through your feed, and do something xD (source: [https://www.writerswrite.com/writingmemes/](https://www.writerswrite.com/writingmemes/" rel="noopener" target="_blank" title="))_

How about making a script which would block all these websites? The script allows you to use them only at some specific given hours of a day. Sounds legit! Let’s do it. :-)

Yes, I know there are many easy methods to block any website. Just download some Chrome plugin, or rather any software which would do this for us. Well yeah, quite easy! But come on, we are developers, we don’t do these things! When we need something, we develop scripts for it rather than using some random trick to do the work…right?!

If you want to download the script directly, you can do so from [here](https://github.com/MadhavBahlMD/Control-Yourself/blob/master/JavaScript/blocker.js).

### Let’s Get Started!

Unlike my other tutorial articles, you won’t need any directory structure or a dev environment set up for this project. All you need is NodeJS installed on your system and a good text editor. You can make this script using any language of your choice which supports file handling. I chose JavaScript because I love it!

![Image](https://cdn-media-1.freecodecamp.org/images/0*Fhqu52MS8kbjNWKY.png)
_**I ❤️ JavaScript!** (source: [https://brendaneich.com/2015/06/from-asm-js-to-webassembly/](https://brendaneich.com/2015/06/from-asm-js-to-webassembly/" rel="noopener" target="_blank" title="))_

### The Background Idea

The idea behind this blocker we are going to make is very simple. There is a file named `hosts`. We can add the URL of any website and the URL of a website to which we want to redirect the former website to. Something like this:

```
127.0.0.1    www.facebook.com
```

Now, whenever we try to open Facebook, it will be redirected to 127.0.0.1 (localhost) automatically. This will indirectly block the website.

The hosts file which I am talking about is present in `C:\Windows\System32\drivers\etc\hosts` if you use Windows. If you are a Mac or Linux user, the location of that file is: `/etc/hosts`.

### Let’s Modify The File…

Before starting the code, let’s try to modify the file and see if it works. Please note that only the user with administrator rights can modify this file. If you are on Windows you can right click on that file and open as administrator. If you are using Linux, you can use the sudo command. I am using nano to open the file, you can use any other editor of your choice.

```
sudo nano /etc/hosts
```

After you type this command, it will ask you to enter your password. You can enter it and open your file. Let’s try it out :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*0MXqMMIcuM34PF780gIO-w.gif)

Alright, so we appended our “to be blocked” website in the hosts file, now let’s check it out whether it worked or not. To check it, go to any web browser, and go to that website.

![Image](https://cdn-media-1.freecodecamp.org/images/0*l-CTDo6vZEcLlSUu.png)
_Yippee! It worked :3_

Now that we’ve checked that our concept is correct, let’s code the blocker.

### 1. Setting up the variables

As I said earlier, there is no need of huge directory structuring or setting up of a dev environment. All you need to do is make a JavaScript file (say, `blocker.js`) and start coding.

First of all, we need to import `fs` (file system) Node module through which we will be making changes to our hosts file. You can read the complete documentation of fs [here](https://nodejs.org/api/fs.html).

```
const fs = require('fs');
```

Now, we will need to initialize 3 variables:

1. **filePath** — To store the path of hosts file
2. **redirectPath** — For the redirection path (here, localhost)
3. **websites** — Array of websites to be blocked

Also, we will be making a variable named `delay`. This variable will store the value of time duration (in milliseconds) after which our script will repeat itself. Basically the idea is to keep the script running all the time to check whether it is the time to block/unblock the websites. To keep it running we will be using `setInterval()` method in JavaScript. We can also use `while (true) {}` to make an infinite loop.

Right now we are keeping the time after which the function repeats itself constant (say, 10 seconds). But, this script can be made smarter by setting the value of delay equal to the time difference between current time and time at which the state of script (block/unblock) has to be changed. Doing this is much more easier than what it feels like — so I want you (the reader) to do it yourself, and drop me a [mail](http://www.madhavbahl.tech/), I would love to hear from you ?

```
const filePath = "/etc/hosts";const redirectPath = "127.0.0.1";let websites = [ "www.someRandomWebsite.com","anotherWebsite.com" ];let delay = 10000;
```

**Note*** If you are a Windows user, store this in the filePath variable: C:\Windows\System32\drivers\etc\hosts

### 2. The blocker function

We will now make a blocker function. We call it from the setInterval method to keep it running after every given time interval.

```
let blocker = () => {    ....    ....};
```

**Now we will fill the code inside our blocker function.**

#### Inside blocker: Getting current time

First of all we need to get the current time, and then check whether it is the time to block the website or unblock it.

```
let date = new date();let hours = date.getHours();if(hours >= 14 && hours < 18) {    console.log('Time to block websites');    ....    ....} else {    console.log('Time to unblock websites');    ....    ....}
```

#### Inside blocker: Inside If — The If condition is true

Now we need to read the hosts file and convert the fetched data to string (the `readFile()` function will return the buffer data which needs to be converted into string).

After reading the file, we need to check whether the each website and redirect path is present in the hosts file or not. If it is present, then we can ignore it. Otherwise, we need to append `redirectPath websiteURL` to it which will look something like this:

```
127.0.0.1    www.someRandomWebsite
```

To implement this, we will use a for loop. The loop will iterate through each URL in the websites array and check whether it exists inside the file. To do this, we will use `indexOf()` method of strings. If the value is greater than zero, i.e. the given website is present inside the hosts file, we can simply ignore. Otherwise, if the value is not greater than zero, we need to append the redirectPath and website URL (separated by space) to the file.

```
fs.readFile(filePath, (err, data) => {    fileContents = data.toString();    for(let i=0;i<websites.length;i++) {        let addWebsite = "\n" + redirectPath + " " + websites[i];        if (fileContents.indexOf(addWebsite) < 0) {            console.log('Website not present in hosts file');            fs.appendFile(filePath, addWebsite, (err) => {                if (err)  return console.log(err);                console.log('File Updated Successfully');            });        } else {            console.log('Website is present');        }    }});
```

#### Inside blocker: Inside Else — If condition is false

If the condition is false, we need to check whether the websites in the list are there in the hosts file. If they are present we need to delete them.

For deleting, we will use a simple trick. We will read the file line by line. We create an empty string and check whether the current line contains any of the websites present in the list. If yes, we simply ignore it. Otherwise we will add that line to the string we initialized. After checking the last line, we will simply replace the current content of the file by this completeContent string.

The code to do so is very easy. First initialize an empty string (`completeContent`). Then read the file line by line. Follow the steps given in the code below. Then replace the file’s content by completeContent variable.

```
// Initialize the empty stringlet completeContent = '';
```

```
// Read the file line by linefs.readFileSync(filePath)    .toString()    .split()    .forEach((line) => {        ....        ....        ....        // Do the below given procedure to update completeContent });
```

```
// Replace the file contents by `completeContent` variablefs.writeFile(filePath, completeContent, (err) => {    if (err) {        return console.log('Error!', err);    }});
```

Now that we have access to each line, we can check whether this line contains any website by using a flag and a for loop. We set the flag to 1 (or true) and then run a loop to iterate through the list of websites. If the line contains the current website (we will check it using `string.indexOf(substring)` method), reset the flag to 0 and break the current loop. Outside the loop we check, if the flag is 1 (or true) we append the current line into the `completeContent` variable.

**Please also note** that if the flag is 1, we also check that whether the current line is last line or not. If it is not the last line, we append the current line into the `completeContent` string along with a `"\n"` so that the next line will be appended into `completeContent` from a new line (or with a line break). Follow along the following code inside the forEach() of above code block.

```
let flag = 1;for (let i=0; i<websites.length; i++) {    if (line.indexOf(websites[i]) >= 0) { // line contains website        flag = 0;        break;    }}
```

```
if(flag == 1) {    if (line === '')           completeContent += line;    else         completeContent += line + "\n";}
```

### 3. Running the code for the blocker function

Here is the code for the blocker function just in case you were confused with the distributed code in section 2:

Now, for running this function continuously, we can go for `while (true) {}` as an infinite loop. Inside it we can give some time delay so that it doesn't occupy the processor continuously.

Or, a better option is to use the `setInterval()` function. This keeps repeating the blocker function after a specific interval of time. But, `setInterval()` will run for the first time after the specified delay. Therefore we will have to call the blocker function once before the setInterval function.

```
blocker();setInterval(blocker, delay);
```

### 4. All Done! Let’s check our script

Time to run our script. To run the script, open the present working directory in a terminal and type in the following command:

```
sudo node blocker.js
```

If you are a Windows user, you can open the command prompt as administrator, go to the project directory, and then run the command:

```
node blocker.js
```

Please note that just for checking purposes, I am blocking `facebook.com`. Here is the test run:

![Image](https://cdn-media-1.freecodecamp.org/images/1*3csxXZL_6AjyODUwXucfbw.gif)
_Yuss! We Made It ❤_

### 5. The Final Step...

#### For Mac and Linux

You can schedule this script to run whenever someone starts the system using crontab. Cron is a time-based job scheduler in Unix-like computer operating systems. You can read more about cron [here](https://opensource.com/article/17/11/how-use-cron-linux).

So we will be adding our command through which we run the script (`sudo node blocker.js`) in the cron table. Doing this is very simple: open the terminal using `ctrl+alt+t`, then open crontab using `sudo crontab -e`. This command will open the cron table.

**Note** that we used `sudo crontab`, not `crontab`. This is will enable us to modify the cron table.

Once you have it open, add this line at the end (replace `path-to-script` with the path of your project directory):

```
@reboot node /path-to-script/blocker.js
```

That’s it! Doing this will run your script every time system reboots.

#### For Windows

The script can be scheduled to run every time the system starts in Windows also. [Here](https://www.howtogeek.com/138159/how-to-enable-programs-and-custom-scripts-to-run-at-boot/) is a very good article which tells how to do so.

### Where to go from here?

Are you an open source enthusiast? Want to contribute to this project?   
I am starting a new Open Source project named **“Control-Yourself”** which will be a desktop application made using [Electron](https://electronjs.org/). The features will include:

* taking inputs from users about which times they want to block which websites
* tracking the time a user spends watching social media websites
* a Pomodoro timer
* and a todo list application with daily progress report of productivity.

Check out the [repository](https://github.com/MadhavBahlMD/Control-Yourself), and add a comment “interested” on the issue you are interested to work on.

Now, let me give you the complete code with proper comments which will help you understand the code:

**Complete Code (blocker.js)**

### That’s it

Have you found the article helpful?

[Subscribe to TheLeanProgrammer](http://madhavbahl.tech/subscribe/) to be the first one to get notified from me for future updates.

![Image](https://cdn-media-1.freecodecamp.org/images/1*L-3kS5mz7jp4e8zV8WLoLQ.png)

Feel free to reach out to me anytime if you want to discuss something :D

I would be more than happy if you send your feedback or suggestions, or if you ask questions. Moreover, I love to make new friends — so just drop me a mail.

> Thanks a lot for reading till end. You can contact me in case if you need any assistance:  
> Email: madhavbahl10[at]gmail[dot]com  
> Web: [http://madhavbahl.tech/](http://madhavbahl.ml/)  
> Github: [https://github.com/MadhavBahlMD](https://github.com/MadhavBahlMD)  
> LinkedIn: [https://www.linkedin.com/in/madhavba_hl/_](https://www.linkedin.com/in/madhavbahl/)

