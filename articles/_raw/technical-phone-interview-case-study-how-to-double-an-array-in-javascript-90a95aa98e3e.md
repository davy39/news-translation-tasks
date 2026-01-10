---
title: 'Technical phone interview case study: How to double an array in JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-17T17:17:24.000Z'
originalURL: https://freecodecamp.org/news/technical-phone-interview-case-study-how-to-double-an-array-in-javascript-90a95aa98e3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aAXkqX-3cNpp0EGaXCplFg.jpeg
tags:
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: jobs
  slug: jobs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jane Philipps

  Technical phone screens are a crucial step in the technical interview process. Often,
  whether or not you pass the technical phone screen will dictate whether you’ll be
  invited for an on-site interview.

  Technical phone screens can be ...'
---

By Jane Philipps

Technical phone screens are a crucial step in the technical interview process. Often, whether or not you pass the technical phone screen will dictate whether you’ll be invited for an on-site interview.

Technical phone screens can be tough because you must think out loud while working through a problem without having the benefit of being there in person with your interviewer. When you’re interviewing with someone over the phone or video, it can be difficult for your entire presence to come through. Usually, you’ll be working in a shared editor, so while you’re working through a problem, the interviewer will only be able to hear you and see what you’re typing. Many people find it more difficult to communicate in this way than in person.

The good news is technical phone screens are something you can practice and get better at. Just like any skill, the more you do them, the better you’ll get. Eventually you will start to see results, as you’ll be invited to interview on-site with more and more companies.

Though all technical phone interviews are different, most will require you to think on your feet. So the best way to prepare is simply to practice working through questions. You can walk through them on your own by talking them out, and you can also practice with a friend. If you’re practicing on your own, you could even record yourself so you can listen back on the recording and see if how you explained your thought process made sense.

Finally, you can practice by interviewing with companies! When I was last interviewing for a new role, I started by finding companies that I was interested in, but wouldn’t be upset about if I didn’t pass the technical phone screen. This way, I still felt pressure to prepare, but I expected to fail a few times first. It was then less disappointing when I didn’t move on to the next stage.

In this post, I will walk through a question I received in a technical phone screen to give you a framework for approaching these types of interviews. I hope this is helpful, and I welcome your comments and feedback!

Let’s dive in.

### The question

This was an actual question that I received from an interviewer. I like this question, because there are several ways to solve it. The way you solve it reflects your programming style and helps the interviewer gauge whether or not you’d be a fit for the position.

Here’s the sample interview question:

```
Given an array, write a function that doubles the array.Example: given [1,2,3,4,5], your function should return [1,2,3,4,5,1,2,3,4,5].You could call it like so: myArray.double().
```

### Answering the question

Here are my five steps for approaching a problem during a technical phone screen:

**1. Clarify the question**

**2. Think of small test cases, including edge cases**

**3. Pseudo-code your solution (optional)**

**4. Translate your pseudo-code into actual code**

**5. Test your solution using the test cases you came up with earlier**

#### 1. Clarify the question

The first thing you should do when given an interview question like this is ask clarifying questions.

In this case, the question is relatively straightforward: I understand that I need to write a function that takes in an array and returns an array that has been manipulated. Understanding the input and ouput of a function results in what is often considered a [function signature](https://developer.mozilla.org/en-US/docs/Glossary/Signature/Function).

#### 2. Think of small test cases, including edge cases

Next, you’ll want to think of some smaller examples, which will serve as your test cases later:

```
// What happens when the given array is empty?[] => []
```

```
// What happens when the given array has only 1 element?[1] => [1,1]
```

```
// What happens when the given array has only 2 elements?[1,2] => [1,2,1,2]
```

```
// What happens when the given array has N elements?[1...N] => [1,2,3,4,5...N,1,2,3,4,5...N]
```

Thinking about these cases before you start coding will help you look for and establish patterns for what you’re trying to solve. It’ll also help you think about space or time complexity, which may come as a follow up question later. This also helps make sure that you’ve sufficiently understood the question, as it gives your interviewer a chance to correct any misconceptions.

#### 3. Pseudo-code your solution (optional)

Now that you’ve clarified the problem and thought of a few sample test cases, it’s time to think through the actual solution. This is where pseudo-coding can come in handy. If you’re not familiar with pseudo-coding, it’s the idea of writing out what you want to do in plain language or simplified code syntax before writing out the working code. It’s a way to help you organize your thoughts before jumping right into the code.

Pseudo-coding can be incredibly effective in terms of helping you stay on track during your interview. I personally like to do it, because it helps me stay organized. If I ever get stuck, I can refer back to the steps I’ve written in pseudo-code to get back on track.

I once had a phone interview where I wrote the steps in pseudo-code before writing the actual code. The interviewer was able to help guide me by pointing to the step in my pseudo-code that I needed to take next. In this case, the interviewer also mentioned that he had never seen anyone do that before, and was incredibly impressed. So, pseudo-coding also has the benefit of showing your interviewer that you’re organized and impressing them with those skills!

So, going back to the question at hand, here is some pseudo-code you could write:

```
// Define a function that takes in an array// Loop over the array// Push each element from the array back into the array// Return the array
```

#### 4. Translate your pseudo-code into actual code

Now that you’ve written pseudo-code, it’s time to do some coding. For this question, the first (incorrect) solution I came up with looked like this:

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {
```

```
  for (var i = 0; i &lt; array.length; i++) {    array.push(array[i]);  }
```

```
  return array;
```

```
}
```

```
double(array);
```

Now, this seems pretty straightforward, right? However, there’s a small trick to this question that I only discovered by coding up my solution and trying to run it. That brings me to the final step!

#### 5. Test your solution using the test cases you came up with earlier

If you’re an experienced programmer, you might easily spot the bug in my solution above. But it wasn’t until I ran my code that I realized I had created a dreaded [infinite loop](https://en.wikipedia.org/wiki/Infinite_loop)!

Why does this create an infinite loop? The `array.length` that I was using to know when my `for` loop would stop was dynamically increasing as I was pushing new elements into the array! So, when the `for` loop started, `array.length` was equal to 5. But after the first iteration of the `for` loop, `array.length` was equal to 6, and on and on ad infinitum.

However, there is a simple change that will make this solution work:

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {
```

```
  var length = array.length;
```

```
  for (var i = 0; i &lt; length; i++) {    array.push(array[i]);  }
```

```
  return array;
```

```
}
```

```
double(array);=&gt; [1,2,3,4,5,1,2,3,4,5]
```

RUNTIME: O(n) = linear

With this change, I’m declaring a variable called `length` inside the scope of the function and then using that as the delimiter for my `for` loop. Even though my array size is now changing, the `for` loop still stops after the 5th iteration, because the length variable does not change when `array.length` changes.

Now I can test my code with the edge cases I came up with ealier and see that the results are as expected:

```
// Passing in an empty array yields an empty array correctly:[] => []
```

```
// Passing in an array with only 1 element yields the correct array with 2 elements:[1] => [1,1]
```

```
// Passing in an array with only 2 elements yields the correct array with 4 elements:[1,2] => [1,2,1,2]
```

```
// Passing in an array with 10 elements yields the correct array with 20 elements:[1,2,3,4,5,6,7,8,9,10] => [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
```

### Alternate solutions

The above is one way to solve this question, but there are a couple of other alternatives as well. Remember when I introduced the question above with the suggestion of calling the function by writing something like `myArray.double()`? If you’re familiar with object oriented programming, you may recognize this syntax. In this case, the general idea is that you would actually add an array method called `double` using the prototype chain, that you would then be able to call.

Here’s an example of how I could do that using the `for` loop structure from my original solution:

```
Array.prototype.double = function() {  var length = this.length;
```

```
  for (var i = 0; i &lt; length; i++) {    this.push(this[i]);  }
```

```
  return this;}
```

```
var myArray = [1,2,3,4,5];
```

```
myArray.double();=&gt; [1,2,3,4,5,1,2,3,4,5]
```

By defining the function using the JavaSacript prototype chain, I don’t actually have to pass anything into it because I have access to the array that the method is being called on with `this`. To learn more about the `this` keyword, read the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this).

Now, these solutions are great, but what about answering this question without using a `for` loop? One way is to use the built in JavaScript method `forEach`. This is the same idea as a `for` loop, but instead of us telling the program how to execute our code (imperative programming) we’re going to tell it what the result is (declarative programming). You can read more about imperative vs. declarative programming [here](https://tylermcginnis.com/imperative-vs-declarative-programming/).

Here’s an example of the same solution using `forEach`:

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {
```

```
  array.forEach(function(value) {    array.push(value);  });
```

```
  return array;}
```

```
double(array);=&gt; [1,2,3,4,5,1,2,3,4,5]
```

RUNTIME: O(n) = linear

Finally, here’s another solution to this problem, which I found with a few quick Google searches.

There is also a built in array method called `concat` that you can use:

```
var array = [1,2,3,4,5];
```

```
var double = function(array) {  var doubled = array.concat(array);
```

```
  return doubled;}
```

```
double(array);=&gt; [1,2,3,4,5,1,2,3,4,5]
```

RUNTIME: O(n) = linear

**NOTE:** If you’re wondering about Google searching during your phone screen, here’s my take after participating in more than a dozen technical phone screens: usually it’s completely acceptable.

Technical phone screens are often scheduled for 45 mins to 1 hour. Some of that time is reserved for the interviewer to ask questions about your experience, while some is also reserved for you to ask questions. The time you spend coding can be anywhere from 30–45 mins based on the company and interviewer.

In many cases, your interviewer will be able to help you with quick tips and small hints if you have a general idea about how to do something but need to look up the specifics. For example, I once had an interviewer who knew the regex I needed off the top of their head to perform a specific function, so I didn’t need to spend time figuring it out. This allowed the interview to continue more seamlessly.

However, I’ve also had experiences where an interviewer has asked me to refactor my original solution in a different way and explicitly said it was fine to look up documentation. This is usually the case, because many developers spend time daily reading or referencing docs. Being able to follow that same pattern in a technical phone interview is a good sign.

However, Googling for a solution during your interview can also be a time sink, especially if you’re not searching with just the right phrase (this is where the more you search, the better you will become).

For this specific example, if I had already known about JavaScript’s concat method, it might have come to mind when I was confronted with this problem. Then, Googling to remind myself of how concat worked would have been acceptable.

But if I had instead spent time Googling how to double an array before even trying to think through the problem myself, this might have been a red flag for the interviewer. Technical phone screens are a good way for an interviewer to get a sense of how you think, and it really depends what they are looking for in terms of the position they’re hiring for.

On the other hand, some companies will explicitly tell you that you’re not allowed to use Google for help, so in those cases, it’s best not to. Of course, if you’re unsure at all, ask your interviewer.

### Conclusion

Why am I showing you all of these examples? As you can see, there is not just one single way to approach this problem. There are several approaches you can take, and how you approach the problem all depends on a combination of what your background is and how you think about problem solving. For me, I often gravitate toward loops since `for` loops were one of the original programming concepts I learned. But someone who’s used `concat` before might think of that right off the bat.

I thought this problem was a good example, because it seems relatively simple at first. However, there are ways to get tripped up (as you saw with my infinite loop above), and there are several solutions that demonstrate various levels of specific knowledge. Still, you could also solve this with a solid idea written in pseudo-code and some Googling.

Keep in mind that you won’t always pass technical phone interviews, but the more you do them, the better you will get. And, if you learned something from the interview, even if it was something small, it was probably worth your time.

### One final tip

Always remember to thank your interviewer via email preferably by the end of the same business day that you interviewed with them. Even if the company isn’t your top choice, someone took time out of their busy schedule to interview you, so it’s important to thank them. And, if you learned something new, a quick thank you email is a great way to reiterate that.

What has your experience been like with technical phone interviews? Do you love them? Do you hate them? What has been the most interesting problem that you’ve been asked to solve? Leave a comment below or let me know by emailing me at [jane [at ] fullstackinterviewing [dot ] com](mailto:jane@fullstackinterviewing.com).

Did you like this article? Are you interested in landing your dream job in software development? [Sign up for my mailing list](https://www.fullstackinterviewing.com/fcc-case-study.html).

