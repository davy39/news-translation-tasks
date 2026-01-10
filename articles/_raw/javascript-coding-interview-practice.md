---
title: JavaScript Coding Interview Practice – Sample Interview Questions and Solutions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-31T17:39:28.000Z'
originalURL: https://freecodecamp.org/news/javascript-coding-interview-practice
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/david-goggins-quotes-about-hard-work.jpeg
tags:
- name: coding interview
  slug: coding-interview
- name: interview
  slug: interview
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Damla Erkiner

  David Goggins is an ultramarathon runner, a public speaker, a retired navy SEAL,
  and the author of the book ''Can''t Hurt Me: Master Your Mind and Defy the Odds''.
  He''s one of my role models because of his physical strength and mental r...'
---

By Damla Erkiner

David Goggins is an ultramarathon runner, a public speaker, a retired navy SEAL, and the author of the book '[**Can't Hurt Me: Master Your Mind and Defy the Odds**](https://www.amazon.com/Cant-Hurt-Me-Master-Your/dp/1544512287)'. He's one of my role models because of his physical strength and mental resilience. 

You might say: "Wait a second! We get it. This person is obviously the epitome of success. But he has non-technical skills. So why is he relevant to JavaScript coding interviews?" 

Well, if you're ready, let's explore this together.

### Rocky Balboa As a Mentor

In response to a question, David says, 'The Rocky Movie changed my life." In [that pep talk](https://www.youtube.com/watch?v=dse1afiGbx4&t=193s), he refers to [this scene](https://www.youtube.com/watch?v=25NmudB2fqg) (min 1.30-1.42) where the fictional character, Rocky - despite being beaten up badly by his opponent in the final boxing round - refuses to give up no matter what. 

David describes that particular moment as the time when Rocky - initially depicted as an underdog by the screenwriter - overcomes all the odds and strikes awe in his rival.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-280.png)
_[Illustration Source](https://www.amazon.com/Eye-Tiger-Rocky/dp/B004GY1FTQ)_



Let's admit it. Being a good programmer is not that easy. And especially if you are at the beginning of your career, technical job interviews can be seriously daunting. In short, it might be nice to reach David's (and Rocky's) mindset. 

With that kind of drive and confidence, you're much less likely to consider giving up regardless of the types of challenges you face in your wonderful yet difficult journey of getting a developer job.

## Why Coding Interviews Are Difficult

During coding interviews, you are expected to fix coding problems with some theoretical knowledge. But the caveat is you must do that in real time, which sometimes scares new developers off. 

There are several types of coding interviews. But the most challenging one is probably a whiteboard interview. In these types of interviews, you have to code in front of a future employer / a senior software developer.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-319.png)
_[Illustration by HackerRank</nr-sentence>](https://www.hackerrank.com/blog/virtual-whiteboarding-for-system-design-interviews/"><nr-sentence class="nr-s20" id="nr-s20" page="0)_

These interviews can be extra stressful because you are typically not allowed to have a computer to google any unknown concepts or to get some code snippets from the internet. You are only given a marker to solve the question on a whiteboard as the name suggests.

### Do Interviews Reflect What You'll Do in Your Job?

Not necessarily. So why are they holding these scary coding interviews? Well, the reason is to test your problem solving skills in general. At times, finding the correct answer may not even be that important. 

What matters is how you reach that conclusion / solution and which algorithms you prefer to use along the way. In other words, your ability to function well under stress is being tested by tech companies. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-329.png)
_[Image Source</nr-sentence>](https://www.reddit.com/r/ProgrammerHumor/comments/l6wnvt/interview_vs_job/"><nr-sentence class="nr-s30" id="nr-s30" page="0)_

Let's face it. You'll come across lots of stressful situations in your future job, and how you deal with certain issues is especially crucial. Therefore, your future employer naturally wants to witness firsthand whether you are the right fit for the job. 

## What is the Purpose of This Tutorial?

In this post, I'll walk you through some popular JavaScript interview concepts through examples. I'll also do my best to show you what recruiters / interviewers might actually be looking for in a candidate while they code in front of them. 

To simply put, we'll examine some models and try to solve the related puzzles together. 

By the end of this tutorial, you'll hopefully have an idea about a number of important array methods. But most importantly, you'll unlock how to approach some coding challenges in the best way possible.

## What Exactly is the Memory Palace Method?

Before we start, just be aware that in the sample data down below, I've used some late celebrities' names intentionally so that all those details can be catchy in the long run. 

An ancient technique called [the Memory Palace](https://www.wired.co.uk/article/memory-palace-technique-explained) clearly says that the weirder the details, the easier it is to remember them – and a made-up story / creating context is even more effective. 

If you try to visualise the related situation vividly and associate the given programming concepts with some bizarre details in your mind, you might feel less stressed and confused when you see a similar problem next time. This is because it might be easier for you to create specific links and as such remember things easily. This is how our brains work. 

Well, even the fictional figure '[Sherlock Holmes](https://www.smithsonianmag.com/arts-culture/secrets-sherlocks-mind-palace-180949567/)', the smartest guy on the planet, benefits from this method when solving complicated crimes – so why shouldn't we?

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-321.png)
_[Illustration by Savanahcat</nr-sentence>](https://www.deviantart.com/savanahcat/art/Mind-Palace-387601041"><nr-sentence class="nr-s43" id="nr-s43" page="0)_

## How to Approach Coding Problems

In our imaginary interview, you'll see that four extraordinary musicians from the past are listed as passengers on a flight. We have their food choices and the number of connecting flights they need to take after their incredible performances on stage in different parts of the world.

Let's say just for the sake of argument our phenomenal figures (Freddie Mercury, Amy Winehouse, Kurt Cobain, and Michael Jackson) are about to fly from different destinations to Los Angeles just to be able to dine out together at a swanky restaurant, as they enjoy each other's company so much. 

After all, this is our own private memory palace, so we can absolutely do whatever we want to do in our minds. Remember unusual details will stick better. That's why I'm trying to add more to spice things up. 

This method explicitly suggests describing every single detail with some vivid adjectives so that you can associate them with the things you plan to learn in the long run. 

[Scientists](https://www.medicalnewstoday.com/articles/memory-loss#:~:text=Short%2Dterm%20memory%20is%20the,from%20a%20longer%20time%20ago.) say short term memory and long term memory function very differently. To put it simply, we need a way to put all those core concepts (not necessarily the syntax) about programming in our long term memory. That's why it can be nice to benefit from the memory palace method in our journey.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-326.png)
_[Image Source</nr-sentence>](https://www.nme.com/news/music/producer-goes-viral-for-mixing-nirvana-and-michael-jackson-songs-with-drill-beats-2747204"><nr-sentence class="nr-s56" id="nr-s56" page="0)_

Plus, I feel like you get to picture this unusual scenario with a smile on your face. Well, wouldn't it be great if these awesome souls could have seen that they are now helping us / the programming community as the guests of a freeCodeCamp article? 

### Sample Interview Questions

Let's get back to the real life now though. Remember you're still in the interview and as you see below, three questions in a row are waiting for you.

```js

// Main Question: Get the passengers' names using the data provided 
// Bonus Part (a)- Return vegetarians/vegans
// Bonus Part (b)- Sort passengers by the number of connected flights in descending order

```

### The Data

To solve the puzzles, you're expected to use the data inside the following array of objects in practical ways. 

You'll certainly need to come up with the right algorithms and try to find the most effective solution that can satisfy the interviewer. 

```js

const passengers = [
  {
    id: 1,
    passengerName: "Freddie Mercury",
    isVegetarianOrVegan: false,
    connectedFlights: 2,
  },
  {
    id: 2,
    passengerName: "Amy Winehouse",
    isVegetarianOrVegan: true,
    connectedFlights: 4,
  },
    {
    id: 3,
    passengerName: "Kurt Cobain",
    isVegetarianOrVegan: true,
    connectedFlights: 3,
  },
     {
    id: 3,
    passengerName: "Michael Jackson",
    isVegetarianOrVegan: true,
    connectedFlights: 1,
  },
];
```

The above questions are in fact not that hard. But, how we'll handle them is a great opportunity to compare alternative solutions for a single problem. At the end of the day, quality is what counts for recruiters / interviewers. 

### Interview Question 1: How to Get Passengers' Names 

Let's get the passengers' names as requested. The first solution is through a ['for loop'](https://www.freecodecamp.org/news/javascript-for-loop-how-to-loop-through-an-array-in-js/) method. So we first need to use an empty array to push the passengers' names right inside it at the end of the loop. 

Below, `[i]` represents the current passenger and we simply loop through the 'passengers' array to access the names of the passengers. Then, we need to lock them up in our empty array / passengerNames.

```js

const passengerNames = [];
for (let i = 0; i < passengers.length; i++) {
    passengerNames.push(passengers[i].passengerName)
}
console.log("passengers", passengerNames);

```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-331.png)
_<nr-sentence class="nr-s81" id="nr-s81" page="0">RESULT - using 'for loop'</nr-sentence>_

Alright, we solved the puzzle, but is it enough? Or might the interviewers expect you to come up with a better solution?

### Alternative Solution #1:

We can reach the desired result by using the '[forEach](https://www.freecodecamp.org/news/javascript-foreach-how-to-loop-through-an-array-in-js/)' function as well. This solution is even a bit better than the previous one because there is no index expression in this one. 

```js
                 
const passengerNames = [];
passengers.forEach((passenger) => {
    passengerNames.push(passenger.passengerName);
})
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-332.png)
_<nr-sentence class="nr-s89" id="nr-s89" page="0">RESULT - using 'forEach'</nr-sentence>_

To benefit from 'forEach', we need [a callback function](https://www.freecodecamp.org/news/what-is-a-callback-function-in-javascript-js-callbacks-example-tutorial/). With this arrangement, we are able to reach every passenger in the list. However, just like in the previous solution, we first need an empty array to push the items / passengers' names. 

Even though the result is the same, this piece of code is shorter. Writing neater codes is what is – in fact – expected from you. 

In other words, not only the solution matters, but also how you reach it is being evaluated by the recruiters. For this reason, it is a good idea to plan your action rather than writing the first idea in your mind on the whiteboard.

### Alternative Solution 2:

Here comes the best solution. We can also utilise the '[map](https://www.freecodecamp.org/news/javascript-map-how-to-use-the-js-map-function-array-method/)' function to tackle the same problem. Let's see how.

```js

const passengerNames = passengers.map((passenger) => passenger.passengerName); 
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-333.png)
_<nr-sentence class="nr-s103" id="nr-s103" page="0">RESULT - using 'map'</nr-sentence>_

The map function also loops through the array and returns a new array for every item in the list. With this set-up, we simply return a single element, not an object. 

The result will again be the same in the console, but your code will even be better than the first and second one because this time, we don't need to create an empty array before the actual task. 

Here is the food for thought on this topic. Those who say 'less is more' have a point when it comes to writing codes. 

### Interview Question 2: How to Get Vegetarian/Vegan Singers 

Let's now take a look at the next challenge. The new task asks us to obtain only the vegetarian / vegan singers from the passengers' list by also keeping the first argument in the main question section. 

### How to Solve With a 'For Loop'

Again, we can use the same old 'for loop' for this one as well. All we need to do is to check whether there are any vegetarian / vegan singers in our passenger list through an 'if' statement inside our existing function.

```js

const passengerNames = [];
for (let i = 0; i < passengers.length; i++) {
    if(passengers[i].isVegetarianOrVegan) {
    passengerNames.push(passengers[i].passengerName)
    }
}
console.log(passengerNames);

```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-334.png)
_<nr-sentence class="nr-s117" id="nr-s117" page="0">RESULT - using 'for loop'</nr-sentence>_

We do that with the `isVegetarianOrVegan` property in our object. Basically, what we say is this: if the relevant statement is true (if there are any vegan / vegetarian passengers in the list), just push those items into our new array. The result will give us three singers' names as those are listed as  'vegetarian or vegan' in the data part. 

### How to Solve with 'forEach'

As a matter of fact, the 'forEach' function handles the problem similarly. But once again, it has too many lines of codes as you see below, so it isn't the ideal version. 

```js

const passengerNames = [];
passengers.forEach((passenger) => {
      if (passenger.isVegetarianOrVegan)
        passengerNames.push(passenger.passengerName);
});

console.log(passengerNames);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-335.png)
_<nr-sentence class="nr-s126" id="nr-s126" page="0">RESULT / 'forEach'</nr-sentence>_

### How to Solve with 'Filter' & 'Map'

To come up with the best option, this time, we will use two different methods. The '[filter](https://www.freecodecamp.org/news/javascript-array-filter-tutorial-how-to-iterate-through-elements-in-an-array/)' and the 'map' functions will – in a way – collaborate to create better logic when solving the given problem. Let's examine the following code snippet closely now.

```js

const passengerNames = passengers.filter((passenger) => passenger.isVegetarianOrVegan).map((passenger) => passenger.passengerName);

console.log(passengerNames);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-336.png)
_<nr-sentence class="nr-s133" id="nr-s133" page="0">RESULT / 'filter' + 'map'</nr-sentence>_

With the filter method, we only get the vegetarian / vegan passengers from our array in the first place. If it finds some non-vegetarian / vegan passengers (like our beloved 'Freddie'), it will get rid of them automatically. 

Briefly, the first part of the equation, the 'filter' method will simply work through 'yes' or 'no' model. 

Then, the 'map' function will come in, eventually giving us a brand new array showing the vegetarian / vegan passengers only. 

This final solution will prove your future employer that you genuinely know what you're doing and you are really taking the right steps to be a hotshot developer.

### Interview Question #3: How to Sort Passengers by Connecting Flights

The last section asks us to sort the list of our super cool passengers by the number of the connecting flights they'll take to eventually reach LA. Let's see who has more and as such, will be pretty exhausted. 

Spoiler alert! Amy with four connecting flights in total might be a bit sleepy in the get-together at that fancy restaurant. But there is no doubt that she will somehow rock where ever she goes. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-322.png)
_[Image Source](https://variety.com/2022/music/global/amy-winehouse-freddie-mercury-john-lennon-tupac-shakur-bbc-studios-sales-1235196177/)_

Anyway, what we need for this task is to know how the '[sort](https://www.freecodecamp.org/news/javascript-array-sort-tutorial-how-to-use-js-sort-methods-with-code-examples/)' function operates.

Primarily, it compares items one by one and returns something as a result. In our case, it will be the number of connected flights. But how does it make that comparison? What is the logic behind that?

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-343.png)
_[Source Code: MDN</nr-sentence>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort"><nr-sentence class="nr-s149" id="nr-s149" page="0)_

The above lines of code are pretty clear in general. Thanks to the 'sort' function, we list those months in alphabetical order. 

Well, here comes the big question. How does the code / system know that 'a' is the first letter of the alphabet and as such, the list starts with the 'd' letter (December)?

The reason is that the 'sort function' lists things in ascending order by default. But can't we change this setting? Perhaps, we need to list items in descending order. Of course, we can. 

Let's see how. To achieve what we want, we may utilise 'a' and 'b' letters as parameters leading to different directions.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-338.png)
_[Source Code: MDN</nr-sentence>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort"><nr-sentence class="nr-s160" id="nr-s160" page="0)_

Simultaneously, we can benefit from the assistance of three numbers: -1,+1, 0 as seen above. When sorting items in descending or ascending order or finding the equal values, they can be quite handy. 

### Tricky Bit of the 'Sort' Function

In the following example, the list is sorted in ascending order. Why is it like that? Here is the reason. When we return those 'a' and 'b' parameters, we use this order:  'a - b' . That gives us ascending values by default. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-339.png)
_[Source Code: MDN</nr-sentence>](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort"><nr-sentence class="nr-s169" id="nr-s169" page="0)_

However, if we swap them and say 'b - a', the list will be seen in descending order this time. That's the tricky bit when it comes to the 'sort' function.

In the above example, the first version (regular function) and the second one (arrow function) are in essence the same, but just be aware that [arrow functions](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) came with [ES6](https://www.freecodecamp.org/news/these-are-the-features-in-es6-that-you-should-know-1411194c71cb/). 

Although arrow functions help developers to write less code, you cannot use them everywhere. (Read [this](https://www.freecodecamp.org/news/when-and-why-you-should-use-es6-arrow-functions-and-when-you-shouldnt-3d851d7f0b26/) to find out when to use them.)

### Testing Our New Knowledge

Shall we now analyse the situation of our passengers through our new perspective? We know that the last task asks us to sort the number of flights in descending order. But the following set-up does the opposite. 

It can only give us the list in ascending order. Why? It's simply because of the pre-defined order (passenger1.connectedFlights - passenger2.connectedFlights) as in the case of a - b example.

```js

 const numberOfFlights = passengers.sort(
  (passenger1, passenger2) =>
    passenger1.connectedFlights -  passenger2.connectedFlights 
); 
console.log(numberOfFlights);

```

Once we swap the order (passenger2.connectedFlights - passenger1.connectedFlights) as you see in the following code snippet, our problem will be solved and the list will come in descending order. 

```js

 const numberOfFlights = passengers.sort(
  (passenger1, passenger2) =>
    passenger2.connectedFlights -  passenger1.connectedFlights 
); 
console.log(numberOfFlights);

```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-342.png)
_<nr-sentence class="nr-s189" id="nr-s189" page="0">RESULT - Descending Order by the Number of Connected Flights / Michael is the luckiest :-)</nr-sentence>_

### Can We Also Use 'for loop' or 'forEach'?

Well, yes and no. Both would be low-level solutions for this question. 

We should keep in mind that the sort function mutates an array. This is a kind of side effect which changes the original array and that might be a problem if we use 'for loop' or 'forEach' as a solution. 

There are of course [ways](http://www.buginit.com/javascript/javascript-sort-without-mutating-array/) to avoid mutation in the sort function, but in our example, it will lead to more lines of codes, which is not practical at all.

## Wrapping Up

We've started the article with David Goggins, the symbol of resilience and grit, so let's end it with his inspiring presence and ideas. 

If you happen to read this modern day hero's book or listen to one of those famous podcast episodes (For example, [this one](https://www.youtube.com/watch?v=5tSTk1083VY)) where he was a guest speaker, you'll immediately understand that he wasn't born that way. Rather, his secret lies in the fact that he never gives up, against all odds. 

Coding interviews are tough, but if you keep going after your goals by visualising the scene of success in your mind over and over again, it will -  sooner or later - be yours. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-328.png)
_[Image Source](https://castromarina.info/david-goggins-inspirational-quotes)_

Many thanks for reading this post. If you've liked this article, one of the best ways to support me is to share it. Should you have any questions or comments, you can always contact me via [LinkedIn](https://www.linkedin.com/in/damla-erkiner-000b76227/). I'll be more than happy to help you out with your queries.

Happy coding!

**“Knowledge is power.” – Francis Bacon**

