---
title: How I applied lessons learned from a failed technical interview to get 5 job
  offers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-16T08:25:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-applied-lessons-learned-from-a-failed-technical-interview-to-get-5-job-offers-656fcf58034d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4_aEIqKHhYy0FF3b2RuB6g.jpeg
tags:
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Fredrik Strand Oseberg

  It was almost like a dream. I had taken 6 months off to go all in on coding and
  moving to Australia with my girlfriend, when I finally returned to Norway — and
  a job.

  It almost went without a hitch. I had it all. I’ll start ...'
---

By Fredrik Strand Oseberg

It was almost like a dream. I had taken 6 months off to go all in on coding and moving to Australia with my girlfriend, when I finally returned to Norway — and a job.

It almost went without a hitch. I had it all. I’ll start by providing you a bit of my entrepreneurial background.

I spent the last 6 months tirelessly working on my portfolio and personal projects. Most notably, I created [CryptoDasher](https://cryptodasher.com/), a tool for tracking Crypto currencies and portfolio values in real time. I also submitted an entry to a [web design contest](https://fredrikoseberg.github.io/loopringv2/) for a Chinese blockchain company called [Loopring](https://loopring.org/).

I felt ready. I applied for a frontend developer job with a large consulting company in Norway, and I caught their attention — or at least I thought so.

After passing a home assignment and first round interview, I was invited for the technical interview.

The main event.

I was nervous.

How do you prepare for the technical interview? I asked myself. I asked around and searched the internet like crazy. I watched mock interviews on YouTube. Here are some of the resources I used:

* [Cracking the front-end interview](https://medium.freecodecamp.org/cracking-the-front-end-interview-9a34cd46237) (freeCodeCamp Medium Article)
* David Shariff’s take on [Preparing for a Front-End Web Development Interview in 2017](http://davidshariff.com/blog/preparing-for-a-front-end-web-development-interview-in-2017/)
* [10 Interview Questions Every JavaScript Developer Should Know](https://medium.com/javascript-scene/10-interview-questions-every-javascript-developer-should-know-6fa6bdf5ad95)
* [Toptal’s list of JavaScript interview questions](https://www.toptal.com/javascript/interview-questions)
* [Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/)
* [Pramp - a tool for mock interviewing with others](https://www.pramp.com/)
* [Github Frontend developer questions collection](https://github.com/h5bp/Front-end-Developer-Interview-Questions)
* [YouTube JS mock interview #1](https://www.youtube.com/watch?v=UdiXLzBie9g)
* [YouTube JS mock interview #2](https://www.youtube.com/watch?v=057Rs6CgJnY&t=3142s)

I spent hours and hours slaving over this material, trying to prepare myself as best as I could. I wouldn’t feel good about myself if I didn’t do all I could before the interview, as I’m sure you understand.

The day of the interview arrived.

I had been home for 4 days. After a 36 hour flight from Australia, I was still waking up at 5 AM in the morning each day.

That day I woke at 4 AM.

Still scared, but curiously, excited as well.

I met the interviewer in the lobby of the company, and we went up to their offices.

We had a nice chat and started connecting immediately. I’m good at soft skills, so I was hoping to demonstrate that strength early on. We met up with another interviewer shortly and proceeded to the meeting room.

The beginning of the interview went very well. We each introduced ourselves, and they started asking me some questions about my background. I was asked what I thought was the most difficult part about beginning to code, what kind of technology I’d like to learn, what kind of technology I’d like to teach others, and what I find exciting about it.

At this point I felt the interview was going great. I was curious to learn more about the company and I felt I connected with my interviewers.

Then the technical part began.

First, I was asked to explain my code from the home assignment. The assignment was to create pagination for a dataset, and display it in a list. I had written it using React, and I started to go through the code. As we walked through the code, my interviewers would ask me questions about it. I’ll try to outline the questions below and what I think the interviewers were after.

**Do you know what unit testing is? What part of the code could be unit tested?**

In all honesty, I think I answered this wrongly. A unit test is a piece of code that verifies that a unit or a specific part of the source code performs its intended purpose without unwanted side effects. I don’t remember what I answered, but I might have mixed it up with integration testing. I did have some knowledge of unit testing and TDD before the interview, but in the heat of the moment it may have eluded me.

After some discussion back and forth, I concluded that I could test the pagination function, as it was responsible for most of the logic in the program.

**How would you improve the program?**

I found this question slightly confusing. When I delivered the home assignment (weeks ago), I was asked to include a list of things I could improve about the program. Assuming the interviewer already knew about those, I struggled to find other areas of improvement than those I had already included.

It soon became clear to me that the interviewer was interested in hearing about the things that I had already mentioned in my email, and so I started mentioning all those points - error handling, mobile optimization, user feedback while Ajax call is loading, and page management in the event of a large dataset.

**Do you know what BEM is? Is that BEM you are using in your code?**

I answered that I knew what BEM is. It’s a naming convention for working on CSS projects and stands for Block, Element, Modifier. I also answered that I was inspired by BEM in my CSS class naming, but that it wasn’t exactly BEM, as it didn’t follow all of the BEM rules.

**How would you make this site mobile friendly?**

CSS Media queries. That’s the main one here. They wanted to know that I knew how to work with media queries to make sites responsive.

So far. So good. I felt I answered the questions fairly competently, although I needed to discuss the questions somewhat before understanding what exactly the interviewer was getting at.

### The coding challenge

Then they asked me to extend the functionality. I was asked to implement a sorting mechanism that would take the paginated dataset and rearrange them by name and numbers. I was given a few minutes to think about the problem.

I asked some clarifying questions, like whether or not I was supposed to use the built in JavaScript sort function, or build my own (as we’ll see later, this was a big mistake). The paginated data exists as an array of objects where each object has a data array with 20 objects that represent each item in the list. I came up with the following algorithm:

1. Combine each pagination objects data array into a new array.
2. Sort the new array
3. Paginate the sorted array and set the state of the component to the newly sorted array.

It was a good algorithm. And I was quick to figure out what to do. The only problem now was implementing it. Here’s where I made mistakes.

First of all, I spent way to long finding out how to combine the arrays. I’ll admit, I think some of the pressure of the situation got to me here. Because I did all sorts of weird stuff when I could have solved it with a simple reduce. In fairness, I wasn’t as comfortable with reduce then as I am now.

```js
// What I should have done
const pageData = pages.reduce((startingValue, page) => startingValue.concat(page.data), [])
// What I ended up doing
const pages = this.state.pages;
const pageData = [];
pages.forEach(page => pageData = pageData.concat(page.data));
```

Now that I had an array with all the data, I needed to write the logic to sort it. As my experience in programming has been largely based around building my own projects, it had been a long time since I had anything to do with the JavaScript sort function. I had to look it up, and I spent some time checking MDN and examples on stack overflow to really understand it before I implemented it.

I got the sorting working, partially. I got stuck here for a while. Most of the names in the array were sorted correctly, however at the top there were some names that were out of order. At this point, I was trying to keep calm, but in my mind I was freaking out. I was trying to wrap my head around why it was not sorting correctly. And I was stuck here for longer than I’d like to admit.

After some discussion and prodding from the interviewers. I finally remembered that strings are sorted by their ASCII values. Uppercase letters are valued from 65 - 90 and lowercase letters are valued from 97 - 122. The top results that were not sorted correctly had an uppercase first letter, which had the effect of sorting them first, since their ASCII value is lower than lowercase letters. **It is a mistake I will never make again.**

When the issue was identified, I immediately solved it with using .toLowerCase() on the names being sorted.

Now only one thing remained.

Passing the sorted data into the pagination function.

Here too, I hit a snag.

The pagination function expected an Ajax response and passed each item to a formatData function that picked apart the relevant pieces and returned a new object. However, when I tried to pass the new array of objects that was sorted into this function, it would no longer have the original property names and the function would throw an error.

I spent some time working on this before I figured out that I had to move the formatData out of the pagination function and perform it on the response data before the data was passed to the pagination function.

Once this and some more minor changes were done, the code was finally working. It had taken some time, but eventually I solved it.

At this point the coding part of the technical interview was over.

And I was feeling drained.

We concluded the interview with some more chatting. They told me more about their company, and I asked some questions before we parted ways.

However, the interview didn’t stop there.

I contemplated the interview, reflected over what I did wrong, went to sleep and then went to work.

The next day I spent three hours improving the solution, and then I sent this email:

> _Hi interview X and interviewer Y._

> _I’d like to thank you for agreeing to speak with me yesterday. I’ve thought a lot about the solution and I decided to work a little bit on improving it today. I’ve provided the code of an enhanced version of what we worked on yesterday. This is what I’ve done:_

> _I expanded the sorting functionality to be able to reverse the result if it’s pressed a second time._

> _I expanded sorting functionality to all titles._

> _I added icons to sorting headers._

> _I refactored the pagination function, learned the basics of unit testing, and used Jest to test the functionality of it._

> _I added query string support for the pagination so that reload and linking would show the correct data when visiting a different page._

> _I added media query styling to make the component mobile friendly._

> _I added a loader to be shown while the API call is happening_

> _I added error handling, with an opportunity for the user to re-initiate the API call._

> _I changed the sorting function on mobile to work with a select box._

> _I fixed the error where an anchor tag was enclosing an li tag._

> _It might have been slightly overkill, but I was inspired and I wanted to improve the solution._

> _Best regards,_

> _Fredrik Strand Oseberg_

It wasn’t enough. But at least I did all I could. Some time later I received this email:

> _Hi!_

> _We’d like to thank you for some nice interview rounds, but we have to conclude that we do not offer you the position, because you didn’t aspire to our expectations in the technical part._

> _We like your background and believe that you can fit well into our community, so we’re giving you a detailed feedback on your technical interview, hoping that you’ll apply to us again once you gain some more programming experience._

### Where did I go wrong?

Well, luckily I got a detailed feedback report. So let’s take a look at it and I’ll discuss it with you.

#### Piece of Feedback #1: “Spends too much time finding out how to combine arrays. Searches the internet first instead of checking documentation for JavaScript (for example: “js array doc” would give w3schools or mdn, where the functions are listed), and uses the examples wrongly (array.concat returns a new array). No one remembers everything in the APIs, so being comfortable with using documentation for JS or a library is important.”

**Takeaway:** Interviewers want to see you reach for MDN (or other relevant documentation) first. They want to see that you can find and read documentation and implement it based upon the information found there.

#### Piece of Feedback #2: “In the sorting assignment the candidate first suggests a weird manual algorithm. Luckily he chooses to use the built-in sort function in JavaScript, but is unsure of how this works and must check documentation repeatedly.”

**Takeaway:** Be absolutely clear in your communication. In this case, I asked the interviewers about whether or not I should use the built-in JavaScript sort function or not, to clarify the boundaries/limitations of the task at hand, and to demonstrate that I didn’t jump into coding without knowing the terms under which I operated. Unfortunately, I think this was misinterpreted as me suggesting to use my own sorting algorithm, when I didn’t intend to do so unless that was specifically what they wanted out of the task.

This ended up having the opposite effect of what I wanted to convey. Make sure that you communicate clearly what your questions intend to uncover. Because they might make perfect sense to you, but can be perceived otherwise by your interviewers.

#### Piece of Feedback #3: “When the code works, the text is sorted “case sensitive”, a classic scenario.”

Unfortunately the candidate spends a long time before the problem is understood, but once it’s identified it’s corrected immediately.

**Takeaway:** Speed is of the essence. Bugs will always appear when writing programs, but try to solve them as quickly as you can. Find the essence of the problem, and turn to documentation quickly if you can not figure it out.

#### Piece of Feedback 4: “Spent some time to understand why formatData had to be moved out of pagination under refactor.”

**Takeaway:** Again, speed is of the essence.

#### Piece of Feedback #5: “A lot of foreach loops, where array.map or array.reduce could have been used. It would be beneficial to learn more about functional programming.”

**Takeaway:** Learn array.map, array.filter and array.reduce, and learn them well. I’ve been delving into functional programming on the back of this, and it’s a daunting task. But you don’t need to learn it all now, just make sure you get the basics down.

#### Piece of Feedback #**6: I’d like the candidate to have more knowledge about unit-testing.**

**Takeaway:** This seems fairly obvious, but let’s write it out a few times just for good measure: Testing is important. Testing is important. Testing is important. Learn it. Incorporate it. Use it.

The rest of the document is praise. I won’t go into that much detail, because it’s not that important. But here is the gist of it:

* He uses his editor well
* He uses the debugger in Chrome (knowing advanced debugging tools is important)
* He checks that things work before moving on (using console.log)
* He tries to split the code up into lesser logical parts
* He uses variables with names instead of comments, this makes the code more readable.
* He knows React well
* Earlier projects are impressive
* Possesses other positive qualities than programming (design/visual)

### What could I have done differently in preparation?

Hindsight is 20/20. But when you get a no, you’ll inevitably spend some time thinking about what you could have done differently.

#### Go through the home assignment code more thoroughly.

I spent too much time working on my JavaScript knowledge. I should have gone through my own code even more than I did. Even though I wrote it, when a few weeks pass between the time of writing and the interview, you need to go back and refresh your memory. I wish I’d spent more time on this than on obscure JavaScript questions.

#### Do more practical JavaScript assignments.

I did a lot of theoretical work leading up to the interview. I wish now that I had spent more time, or at least mixed in, practical assignments. Solve algorithms on [Hackerrank](https://www.hackerrank.com/) or [Code Wars](https://www.codewars.com/). Or build common frontend components like a sorted list, dropdown menus, pagination, and so on.

### Interview wrap up

How do I feel after my first technical interview? Honestly, it was a great experience. I’m very grateful to the interviewers that I talked to for giving me such a detailed feedback, and allowing me to correct my mistakes before my next interview. And even though I didn’t get this job, I’m one step closer to getting my first frontend developer job.

I’ve also learned that interviews are a fickle thing. Perhaps if I had built a sorting mechanism in my own projects, or if I had gotten a different assignment closer to something I had done before, it would’ve gone differently.

My biggest strength is that I have spent a lot of time learning JavaScript over the past year, and I am able to learn and adopt new ideas quickly now. Unfortunately, I don’t think I was able to demonstrate this knowledge this time. I didn’t get to:

* Show them my knowledge about the JavaScript prototype chain, and how it allows for effortless and memory efficient sharing of methods between objects.
* Talk about closures and how JavaScript inner functions have the ability to close over variables in the outer scope and access them at a later time after the outer function has returned - and how this prevents garbage collection.
* Share my knowledge of JavaScript scope, and how JavaScript checks each level of it’s local scope all the way up to the global scope to find variables.
* Share my knowledge of conversion and how === checks for equality without type conversion and == checks for equality and type conversion.
* Talk about hoisting and how functions **statements** and variables (except let and const) are hoisted to the top in JavaScript, allowing preceding code to use them.
* Talk about the this keyword, and how the value of this entirely depends on the invocation (call site) of the function.

I **sort** of **(pun intended)** wish that I had.

### The road to success

Now, it would be easy for me to say to myself: “I’m not good enough. I need to spend 3 - 4 months learning more, and then try again.”

I didn’t.

I decided to apply to as many jobs as I possibly could in two weeks. I applied to the biggest IT firms in Norway.

I aimed for the sky.

Two weeks after, I was done with going through interviews with several companies, and I had another technical interview.

### Second round of preparation

If there is one thing I learned from my first technical interview, it’s that preparation is key. It helps by thinking of the technical interview as an exam, and take the necessary steps to ensure you pass.

Exams, like interviews, are faulty in that they fail to encompass the full knowledge spectrum of the candidate. So what can you do?

**Broaden your knowledge spectrum.**

Be bulletproof. Be Neo.

For me, I used advanced memory techniques to memorise the answers to over 100 frontend interview questions in 8 hours. [The questions can be found in this repository](https://github.com/h5bp/Front-end-Developer-Interview-Questions).

How I did this is beyond the scope of this article, but if you are curious about how it works, leave a comment below and I’ll write another article about it.

Furthermore, I spent time on practical examples on [Code Wars](https://www.codewars.com/) and [Hackerrank](http://hackerrank.com/). As well as spending time actually building things.

### Technical Interview #2

Rich on lessons from my last failed interview, I had done my due diligence.

This interview was focused more around a discussion of front end concepts. It was a comprehensive interview, and I felt that the interviewers really wanted to map my knowledge and learn my strengths and weaknesses.

The interview lasted around two hours this time, and I really appreciated that the interviewers did their due diligence so thoroughly as well.

Here’s a list of all the topics we covered:

* JS, CSS and HTML broad strokes
* Document structure
* Project structure
* Git
* Performance
* Security
* Accessability
* SEO
* Responsive web design

The coding challenge was based on vanilla Javascript. I was challenged to add a simple class to a div using vanilla Javascript. Now, if you’ve spent time in JS using mainly frameworks, you might not be familiar with the classList API. Fortunately, I had spent most of my time doing all the freeCodeCamp projects with vanilla JS. This is what it looks like:

```js
const btn = document.querySelector('.btn');
const menu = document.querySelector('.menu');
function addClassNameToDiv() {
 if (!menu.classList.contains('new-class')) {
     menu.classList.add('new-class');
 } else {
     menu.classList.remove('new-class');
 }
}
btn.addEventListener('click', addClassNameToDiv)
```

Alternatively, you could use the classList.toggle(‘new-class’) to make it into a one liner. I was also asked to extend it to close the menu if you click outside of the dropdown menu:

```
window.addEventListener('click', () => menu.classList.remove('new-class'));
```

**Takeaways from the coding challenge:**

* Shorter is better, as long as it’s always readable.
* Performance wise, it’s better to put query selectors outside of an event listeners callback function (called just one time instead of every time the listener fires).
* Performance wise, getElementById and getElementByClassName are more performant than querySelector

The next day, I was called up by the manager. I’d passed the interview, and they wanted to extend me an offer.

I could have stopped here. I could have said: “I passed one technical, that is good enough”.

I did the opposite.

I called every company I was talking to at the time and told them I had an offer on the table, and asked if we could expedite the process, as I now had time constraints to consider.

Interviews, and especially technical interviews, are tough mental ordeals. You’re on all the time on display, all the time expected to perform and exceed expectations. It’s hard. So why did I do this?

**Four reasons.**

1. I wanted to prove to myself that it wasn’t luck.
2. I wanted to be respectful to everyone I had been interviewing with and give them a fair chance.
3. I wanted to make sure I found the right fit and best community for me to be in and grow as a developer.
4. You guys. This community has helped me so much, and I wanted to help garner as much information as possible from the technical interview, so that you may learn from my mistakes and prepare accordingly.

I am humbled by the help and support I have received from freeCodeCamp, and I wanted to give back.

### Technical Interview #3

After getting in touch with the other companies and explaining that I had an offer on the table from a top tier firm, a lot of companies were keen to rush me through. In one week I conducted several interviews, and I had more technical interviews to get through.

Here’s a roundup of some of the interview questions from my third technical interview:

* How did you get into React? Why did you get into it? What is good about it?
* How does Redux work? What does the API consist of? What is immutability? What is good about immutability?
* How would you redesign our web page?
* How do you feel about working with deeper layers of the application? For example backend?
* Do you do your own testing? What is a unit test?
* What is a good user experience for you?
* How do you test user experience?

The coding challenge in this interview was based around CSS. I was given a piece of paper with some CSS rules on it that looked like this:

```js
<div id="menu" class="dropdown-menu"></div> // HTML Element
// CSS Rules
#menu {
   color: black;
}
.dropdown-menu {
   color: green;
}
div {
   color: blue;
}
```

My task was to explain what I saw. I immediately identified the HTML element and told the interviewers that the id and class on the element could be used in CSS to select the HTML element. From there, I explained that CSS is cascading, meaning that normally the last rule will apply. However, in this case the selectors have different weighting. The order of weighting goes like this: id > class > element.

Which means, in the example above, the color black will be applied to the HTML element.

### **Technical Interview #4**

This is the last technical interview I had. And while it was still nerve racking, by now I was used to it. Here’s a rundown of what we talked about:

* Draw up a basic website. Identify the components.
* How would you make it responsive?
* How would you center the text vertically and horizontally?
* What is the CSS box model? What is the difference between content box and border box?
* What is the difference between double and triple equals?
* What is good about React?
* What is the benefit of array.forEach over a for loop? Are there cases where you might need to use a for loop?

The coding challenge was to build a wordwrap function of varying degrees of difficulty. Imagine you can only fit 20 characters on a screen, and if you go above it, you have to start on a new line.

My original solution to this question involved splitting the string, using a counter and the modulus operator to determine whether the count was 20, then inserting a newline character into the array and joining the string.

The task was then increased in difficulty to only allow full words to be on a single line. Meaning that if one word caused the total count to exceed 20, you needed to insert a newline character before that word.

I didn’t solve this all the way in the interview, but I was on the right track. I used MDN when I was uncertain, and I was making good progress.

And that was enough.

I couldn’t put it down though, so if you’re interested, here is the solved version:

```js
function wordWrap(str) {
 let totalCount = 0;
 const arr = str.split(' '), formattedStr = [];
 
 arr.forEach((word, index) => {
  totalCount += word.length;
  if (totalCount >= 20) {
     formattedStr.push('\n', word, ' ');
     totalCount = word.length;
  } else {
     formattedStr.push(word, ' ');
  }
 });
 return formattedStr.join('');
}
```

### **Conclusion**

If you made it all the way here, congrats. This was a long one. I did my best to make it as informative as possible, hoping that it may help someone like you.

The end result of this landed me in a situation I never thought I’d be in. At the end, I had 5 offers on the table to choose from. One large company even made me an offer “blind”, based on me having an offer from a competitor. I ended up choosing the company where I first passed the technical, as I believed it would be the best fit for me.

The technical interview can be a tough mental ordeal. You’re going to be challenged, you’re going to be taken out of your comfort zone, and that is a good thing. It helps you grow. It makes you better.

And if you prepare, you will be ready for it.

So from my own experience, don’t shy away from the technical interview. Don’t put it off because you failed one. Don’t think that it’s the end-all measure of you as a developer. It’s not. It’s merely the least broken tool that company’s have to measure your productivity.

Apply for jobs. Prepare well. Attend technical interviews. Learn from mistakes. Repeat.

If you do this, I guarantee you, you will succeed.

I’m rooting for you.

