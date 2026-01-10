---
title: Understanding Asynchronous JavaScript Callbacks Through Household Chores
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-16T08:55:08.000Z'
originalURL: https://freecodecamp.org/news/understanding-asynchronous-javascript-callbacks-through-household-chores-e3de9a1dbd04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VUwszg-nhLvQ4uN5iqBLag.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Stephen Mayeux

  If you’ve ever done the laundry, you can understand how callbacks work.

  The other day I read Kevin Kononenko’s brilliantly funny and easy-to-understand
  guide to MVC frameworks. He explains the Model-View-Controller paradigm through
  ...'
---

By Stephen Mayeux

#### If you’ve ever done the laundry, you can understand how callbacks work.

The other day I read [Kevin Kononenko](https://www.freecodecamp.org/news/understanding-asynchronous-javascript-callbacks-through-household-chores-e3de9a1dbd04/undefined)’s brilliantly funny and easy-to-understand guide to MVC frameworks. He explains the [Model-View-Controller paradigm through ordering drinks at a bar](https://medium.freecodecamp.com/model-view-controller-mvc-explained-through-ordering-drinks-at-the-bar-efcba6255053#.9bjays8jc), and it has been one of my favorite programming explanations I think ever!

I really appreciated it because it was written without an air of pretension or elitism, and it made me wonder why a lot of other experienced coders can’t help newbies without the _l337er-than-thou_ attitude?

I teach English in South Korea at the moment, and we teachers have to think like Kevin all the time. Nowadays it is really frowned upon to explicitly explain grammatical concepts, so good teachers try to contextualize the target language (i.e. the grammar or vocabulary they want to teach) with stories, film, music, and images.

This teaching methodology was influenced by British linguists in the 1980s, which has informed modern foreign language pedagogy today. Maybe the same thing is happening right now for coding education!

Kevin is going to be a hard act to follow, but I would like to explain how asynchronous callbacks work in JavaScript through the context of doing common household chores.

#### Synchronous Honey-Do List

Shout out to my wife who has been doing double her share of the chores at home while I learn to code. I owe her big time!

I usually help out around the house on Sundays, and her honey-do list for me looks like this:

1. Do the laundry
2. Give dog a bath
3. Sort the recycling
4. Balance the budget
5. Figure out what we’re doing for dinner.

**Technical aside:** At the core, JavaScript is a synchronous programming language, meaning it runs one line of code at a time. It cannot move on to the next line of code until the current line has finished executing. Consider this example:

```
function syncChores() {  console.log('Do the laundry');  console.log('wash the dog');  console.log('sort the recycling');}
```

```
syncChores();
```

```
/* Output appears in the same order it was written:
```

```
   Do the laundry   wash the dog   sort the recycling
```

```
*/
```

Now imagine if I did my chores synchronously in real life. What would happen? What would that look like?

If you go back to my list, you will see that doing the laundry is the first item. It takes about 35 minutes for a typical wash cycle to finish and an additional 45 minutes for a load of laundry to dry. So for 80 minutes, I am just sitting on my lazy butt, not doing any other chores, as I synchronously wait for the laundry to finish.

Here’s what that looks like with pseudocode:

```
function doLaundry() {  startWashCycle();  switchToDryer();  foldAndIronClothes();}
```

```
function washDog() {  // imagine some dog-washing code here}
```

```
function sortRecycling() {  // and imagine some sorting code here}
```

```
doLaundry();// Now wait a full 80 minutes before completing other functions
```

```
// Now I can finally wash my dog!washDog();sortRecycling();
```

Not very efficient, is it? In real life, busy adults would tackle these chores asynchronously, meaning they would start the laundry, continue doing other tasks on the lists, and go back to the laundry when the wash cycle has finished.

This action of going back to the laundry when it’s ready is analogous to the JavaScript **callback function**, and our washing machines quite literally call us back with some alarm or buzzer! This allows us to go on and do other chores and then continue with the laundry chore when it is ready for us.

#### Asynchronous Honey-Do List

Let’s do the chores again, this time asynchronously. What would that look like in pseudocode?

```
function doLaundry(callback) {  // imagine initial code that kicks off wash cycle  // takes 80 minutes to complete wash cycle
```

```
  callback(err, cleanLaundry);}
```

```
doLaundry(function(err, cleanLaundry) {  // sometimes our washing machines break down  // better handle that possible error
```

```
  if (err) throw err;
```

```
  // if no errors, switch to dryer after wash is complete
```

```
  // Tada! Our call back alerting us that washing is complete!
```

```
  switchToDryer(cleanLaundry);
```

```
});
```

```
// as we wait, JavaScript will run this stuff now!
```

```
washDog();
```

```
// still time for more chores!
```

```
sortRecycling();
```

```
// the following will be undefined because it is not yet ready
```

```
console.log(cleanLaundry);
```

```
// Now the laundry is ready! // Let's go back and switch clothes to the dryer
```

```
// The clothes are drying. Let's continue doing more chores.// Tanya will be impressed with my productivity!
```

```
balanceBudget();
```

Like Kevin’s article, this was only meant to clear up the concept of callbacks. If you want a more practical guide, check out [Callback Hell](http://callbackhell.com).

#### Your Turn

It helps if you can apply abstract concepts to real situations. Can you think about what you do at home, school, or work that resembles synchronous and asynchronous code? Write them in the comments below!

