---
title: How I made a LinkedIn contact adding bot - and actually got a few interviews
  with it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T15:33:06.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-a-linkedin-contact-adding-bot-and-actually-got-a-few-interviews-with-it-37a6f5f85d4d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TAOB-11BmEzHS-1b
tags:
- name: bots
  slug: bots
- name: career advice
  slug: career-advice
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By YK Sugi

  On LinkedIn, there’s a section that’s titled, “People you may know.” It’s under
  the My Network tab.


  This is the page that suggests people you might want to connect with.

  You can click these Connect buttons to send connection requests to t...'
---

By YK Sugi

On LinkedIn, there’s a section that’s titled, “People you may know.” It’s under the **My Network** tab.

![Image](https://cdn-media-1.freecodecamp.org/images/0*TAOB-11BmEzHS-1b)

This is the page that suggests people you might want to connect with.

You can click these **Connect** buttons to send connection requests to the people in this list.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OlQUSAu7j9W1waNDevacKg.png)

A few years ago, I found this page, and I started randomly adding people there. I would just click on the connect button on every single person I found on this page.

I just figured it might be useful to have a lot of connections on LinkedIn to get the kinds of jobs I wanted to get, for example, software engineer internships.

But after a while, it became a little bit cumbersome to keep clicking on these connect buttons manually.

So, I decided to make a little bot to click these buttons for me.

This is an article about how I made this bot, what happened as a result, and what I learned from it.

### How I made the bot

#### The tools I used

I made this simple bot to add random people on LinkedIn with **JavaScript** and [**Greasemonkey**](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/).

Greasemonkey is a Firefox add-on that helps you manage custom JavaScript code.

With it, you can set things up so that a certain set of code runs automatically when you open a certain URL.

You can also store some data in Greasemonkey. I used this feature to keep track of the number of people I added with this bot. That way, I was able to keep track of this number consistently even when I closed the browser or refreshed the page.

#### The code I used

Unfortunately, I did not keep the code I used to create my bot after I used it.

So, in this article, I’ll do my best to recreate it as closely as possible.

Initially, to create this bit of code, I used Google Chrome. Later, I switched to Firefox to use Greasemonkey, which I mentioned earlier. I chose to use Chrome initially just because I was more used to it.

Now, let’s together go through how I would recreate this code today. In this article, just to keep it simple, I’m only going to show you the core functionality of this bot - adding people. So, I’m going to skip the part about using Greasemonkey to store data persistently here.

Please let me know in the comments if you’d like me to cover that part in a separate article.

#### Step 0: JavaScript basics

In case you’re not too familiar with JavaScript, let’s quickly go over some JavaScript basics here.

We’re going to use Google Chrome here, but you can use any browser you’d like to use.

First, open any website, let’s say, Google.com.

Then, you’ll need to open the browser’s JavaScript console there.

On Google Chrome, you can do it in a few different ways.

The way I usually do it is the following:

* Right click anywhere on the page.
* Then, click **Inspect** out of the menu that’s popped up.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RnSqub0Ljw3asxj5hi-UBg.png)

* When you click it, a window like the following should show up.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EdFB6fMXV9FLv9x-TQZFRw.png)

* Then, click the **Console** tab there to show the JavaScript console.
* Once you click the **Console** tab, you should see the JavaScript console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ExR9I9a7O6yfk4-5JB3Dxg.png)

This is where you can type in any JavaScript code to test it. You can use the code you enter to interact with the page that’s open in your browser.

For example, try typing in the following code in the console and press Enter.

```
selected = document.querySelector('body');
```

This selects the **body** tag in the page that’s open on the browser. Then, it assigns it to a new variable called **selected**.

In Chrome and Firefox, there is a shorthand for:

```
selected = document.querySelector('body');
```

Instead, you can just write:

```
selected = $('body');
```

[This code is equivalent to the one above.](https://stackoverflow.com/questions/22244823/what-is-the-dollar-sign-in-javascript-if-not-jquery)

I’m going to use this shorthand notation with the dollar sign throughout this article to keep our code short and simple.

Also, don’t worry about it if you don’t know the basics of HTML and JavaScript yet. I’ll try my best to write this article so it’s easy to understand even for beginners.

If you’re not interested in the code I’m going to show you, you can also just skip to the sections about what happened and what I learned from this experience at the end.

Now, let’s walk through our bot’s code, step by step.

#### Step 1: Find the target element

First, you’ll need to write the bit of code that finds the buttons that you want to click.

First, log in to LinkedIn. Then, go to the My Network tab. It’s currently at [https://www.linkedin.com/mynetwork/](https://www.linkedin.com/mynetwork/) (July, 2018).

You should be able to find the **People you may know** section there.

Then, on Chrome, right click on the “connect” button on one of the recommended people there. Then, click **Inspect**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QNH8JeKcFlNNcSRDlJ7k3g.png)

Once you do so, the element that you just clicked on will be highlighted in the developer window.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1s3975-NyQ4UEE4_RjGmvg.png)

This is the HTML code that’s highlighted in blue here:

```
<span aria-hidden=”true”>Connect</span>
```

This is a **span** tab that shows the text: **Connect**. What we really want to click on is not this one, but its parent element, which is a button.

You can find it right above the span element that we selected.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mFx3ou-b4BjE9iTQz00sCw.png)

Let’s now examine this button element:

```
<button data-control-name=”invite” class=”button-secondary-small” data-ember-action=”” data-ember-action-1596=”1596" data-is-animating-click=”true”> <span aria-hidden=”true”>Connect</span> <span class=”visually-hidden”> Invite Azul Pinochet Barros to connect </span></button>
```

There’s a bunch of stuff here, but here’s the important part:

```
<button data-control-name=”invite” ...> <span aria-hidden=”true”>Connect</span> ...</button>
```

Basically, this is a button element whose attribute, **data-control-name**, is “invite”.

In our script, all we need to do is select elements like this and click them.

You can select these elements with this piece of code:

```
selected = $(“button[data-control-name=invite]”);
```

This reads as, select all the button elements whose data-control-name is “invite”.

> _NOTE: It looks like LinkedIn’s website uses jQuery. So, the notation above is actually a jQuery selector, [not a helper function defined by Chrome](https://stackoverflow.com/questions/22244823/what-is-the-dollar-sign-in-javascript-if-not-jquery). Confusingly, their behaviours are slightly different ?_

Anyway, once you run this code in your Chrome console, you should be able to see that the correct elements have been selected.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gkmjHPk7wCgX5BsoXIWb9w.png)
_This is how you can make sure that the correct elements have been selected._

Now, with this piece of code - `selected = $("button[data-control-name=invite]");` - your browser finds multiple button elements and puts them in an array. To pick the first one, you can just select the first element in this array like so:

```
toClick = $("button[data-control-name=invite]")[0];
```

Then, you can click it with this:

```
toClick.click();
```

If it goes through, you should see a confirmation window popping up.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mGV1IV56IA17NFDx6JfAEA.png)
_A confirmation window that shows up when you click one of the **connect** buttons_

#### Step 2: Loop through multiple target elements

Now, the next step is to loop through multiple target elements to click so we can add multiple people.

After some experimentation, I realized that there’s a simpler way to select multiple buttons and loop through them than the one I showed earlier.

Here’s how I would do it.

First, use Inspect Element to analyze the structure of this page a bit more. Then, you should be able to see that the **people you may know** is just an unordered list.

You should be able to find code that looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*EgTc1y_-qQXvC_UcJw2UGQ.png)

The parent element is a `ul` (unordered list) element. Its children are `li` (list item) elements.

Each `li` element represents each of the **people you may know** cards you see on the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XnIgeADO5OUKj3YFlQ1ePw.png)

By selecting these `li` elements instead of selecting the buttons directly, it actually becomes easier to go through multiple people.

You can select this `ul` element, the parent of the `li` elements, like this:

```
ul = $('ul.mn-pymk-list__cards')[0];
```

This says, select the `ul` element with the class `ul.mn-pymk-list__cards`. We need to add `[0]` at the end because the raw result is an array containing a single element.

Then, you can select the first `li` element (the first person’s card) under the `ul` element like this:

```
firstLi = ul.querySelector('li');
```

We don’t need to add `[0]` at the end of this statement because the querySelector() function only returns one element.

Then, out of `firstLi`, you can select the button that we need to click like this:

```
buttonToClick = firstLi.querySelector("button[data-control-name=invite]");
```

After clicking this button with `buttonToClick.click()`, we should remove this `li` element so we can go to the next `li` element (the next person’s card). We can do that with this:

```
ul.removeChild(firstLi);
```

Putting them all together, and putting everything in a while loop, you’ll get something like this:

```
ul = $('ul.mn-pymk-list__cards')[0];firstLi = ul.querySelector('li');while(firstLi){ // do this while firstLi still exists.  buttonToClick = firstLi.querySelector("button[data-control-name=invite]");  ul.removeChild(firstLi);  firstLi = ul.querySelector('li');}
```

This code should work, but it has several issues.

1. We add people _really_ fast with this, so it’s going to be hard to know what’s going on when you run this code.
2. We are not keeping track of how many people we’ve added.
3. We are assuming that `buttonToClick` is always the correct button to click. Sometimes this button has the text “Invite” instead of “Connect”. We don’t want to click on too many of those “Invite” buttons.

#### Step 3: Refine our code

I’ve fixed all of the issues I mentioned above and put together a relatively simple piece of code below.

It’s also [here](https://gist.github.com/ykdojo/aea4cf27fec4bbb5a175e11bae39cb2d) on Gist. Perhaps it’s easier to read there.

```
// this function allows us to stop our code for |ms| milliseconds.function sleep(ms) {  return new Promise(resolve => setTimeout(resolve, ms));}
```

```
// I've put our main code into this function.async function addPeople() {  ul = $('ul.mn-pymk-list__cards')[0];  firstLi = ul.querySelector('li');  count = 0; // this is the count of how many people you've added  while(firstLi && count < 100){ // stop after adding 100 people    buttonToClick = firstLi.querySelector("button[data-control-name=invite]");    // make sure that this button contains the text "Connect"    if (buttonToClick.innerText.includes("Connect")){      buttonToClick.click();      count += 1;      console.log("I have added " + count + " people so far.");    }    ul.removeChild(firstLi);    await sleep(1000); // stop this function for 1 second here.    firstLi = ul.querySelector('li');  }}
```

```
addPeople();
```

If you examine this code carefully, you should be able to notice the couple of changes I’ve made:

1. I’ve put our code into an _async_ function called addPeople(). In this function, every time we add someone, we pause for 1 second with the sleep() function. More about this pattern [here](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep).
2. I added a `count` variable to keep track of how many people we’ve added.
3. I added this if statement: `if (buttonToClick.innerText.includes("Connect"){...}`. This way, we can make sure that the button we’re clicking contains the word “Connect” inside it.

With these changes, when I run this code, it looks like this:

#### Step 4: Make further improvements!

On top of what I showed above, I had a few more functionalities when I actually used my bot to add a bunch of people on LinkedIn.

First of all, I used Greasemonkey, which I mentioned earlier, to keep track of the total number of people I’ve added.

Also, to avoid being detected as a bot by LinkedIn, I added a few things:

1. I randomized the order in which I added people.
2. I randomized the amount of time I waited every time I added a new person.

I’ll leave all of these as exercise problems for you to solve in case you’re interested in solving them ?

### What happened

With my script, I ended up adding 2000+ connections. Then, if I remember correctly, about 400 of them added me back.

As a result, I went from about 300 connections to 700+ connections within a week or so!

Then, after a while, I got banned by LinkedIn from adding any more people. I didn’t know that I could get banned! I was scared for a bit, but the ban lifted after 2 months or so.

More importantly, I was able to land a few interviews from those 400+ new connections. One of the interviews was with this company called Palantir.

Here’s a screenshot of the message I received from them:

![Image](https://cdn-media-1.freecodecamp.org/images/1*u7fIRKAxBAk8rJTFeqyrXw.png)

### What I learned from this experience

I thought what I was doing was pretty silly at the time, but I ended up learning a lot from this experience.

#### Takeaway #1

First of all, through this experience, I realized that LinkedIn actually works for getting jobs. I was able to get a few job interviews with my bot, after all.

Then, after a while, I also realized that adding thousands of random people was not the most efficient way to use LinkedIn. With that kind of approach, you end up adding a lot of people you don’t need to add.

So, after that experience, I changed my approach to a more focused one.

With my new approach, I would only add recruiters of the companies I wanted to work at. Then, I would only send messages to the people who added me back.

It turned out to be a much more focused, effective strategy to use LinkedIn. With this new strategy, I was able to get a few more job interviews with multiple tech companies, including Yelp and Xamarin. This time, I didn’t have to add thousands of new connections to achieve this result ?

NOTE: I talk more about this strategy in [this article](https://medium.freecodecamp.org/here-are-4-best-ways-to-apply-for-software-engineer-jobs-and-exactly-how-to-use-them-a644a88b2241), just in case you’re curious about it.

#### Takeaway #2

Having fun is the best way to hone your programming skills!

Through this particular project, I was able to hone my JavaScript skills. What I learned included:

* How to set a timed interval between function executions
* How to select certain HTML elements with JavaScript
* How to store data locally with Greasemonkey

I learned these things through this project, and it didn’t feel like studying at all because it was so much fun.

#### Takeaway #3

From this experience, I’ve learned that it sometimes pays to do something weird. So, don’t be afraid of being a little bit mischievous and adventurous if you have any inclination to do so.

Even after this little experiment, I continued to do weird things for fun.

For example, when I was interning at Microsoft, I ran a little experiment where I “stole” a bunch of employee passwords. I did that by sending out a phishing email. It was supposed to be a huge give-away raffle with prizes like Xbox and Surface laptops. It was my hackathon project there.

I also started a [programming-education YouTube channel](https://www.youtube.com/csdojo), and eventually decided to [work on it full-time and quit my full-time software engineer job](https://medium.freecodecamp.org/why-i-left-my-100-000-job-at-google-60b5cf4ebefe).

Perhaps all of these things seemed a little bit weird to other people. But every time I went through each of these experiences, I learned something new, and I had tons of fun along the way. I would say the last one even made my career.

So again, don’t be afraid of trying something strange just for fun! You might learn something valuable along the way.

#### Okay, that’s it for this article.

This was supposed to be sort of a fun article, but I usually write about more serious stuff.

For example, I have articles about [writing your software engineer resume](https://medium.freecodecamp.org/heres-the-resume-i-used-to-get-a-job-at-google-as-a-software-engineer-26516526f29a), [the best ways to apply for software engineer jobs](https://medium.freecodecamp.org/here-are-4-best-ways-to-apply-for-software-engineer-jobs-and-exactly-how-to-use-them-a644a88b2241), and [how to get a job at a top tech company](https://medium.freecodecamp.org/how-to-get-a-software-engineer-job-at-google-and-other-top-tech-companies-efa235a33a6d).

Feel free to check them out. They are all here on Medium.

Also, as always, if you have any questions about this or anything else, please feel free to let me know in a comment below or on [Instagram](https://www.instagram.com/ykdojo/) or [Twitter](https://twitter.com/ykdojo) (@ykdojo on both).

Thank you for reading this article!

