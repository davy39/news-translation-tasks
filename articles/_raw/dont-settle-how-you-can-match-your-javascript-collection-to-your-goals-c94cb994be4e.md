---
title: 'Don’t settle: how you can match your JavaScript collection to your goals'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-13T19:02:14.000Z'
originalURL: https://freecodecamp.org/news/dont-settle-how-you-can-match-your-javascript-collection-to-your-goals-c94cb994be4e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2kLrLgDZjAt0P_xNrM1qtg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Joe Morgan

  I loved JavaScript even when the world hated it. But I always had a hard time justifying
  collections. Objects are kind of a key-value store, but not really. And they were
  horrible if you needed to sort or loop. Arrays were easier to loo...'
---

By Joe Morgan

I loved JavaScript even when the world hated it. But I always had a hard time justifying collections. Objects are kind of a key-value store, but not really. And they were horrible if you needed to sort or loop. Arrays were easier to loop over, but clunky if you needed to pull out a specific value without an index.

The sad truth is that most of the time developers would just grab whatever collection popped into their head first. Then torture it with conversions to get whatever they needed.

It was painful.

Things are different now. There are more collection types. There are more methods. There are better techniques and even one-line expressions to switch between collection types. Why then does it seem like we are still just guessing when we pick a collection type?

I speak regularly about [JavaScript and code quality](https://www.youtube.com/watch?v=cT7TMzZ3Cnw&list=PL_G_ImM6b7_e9WnnY1Hmy-culcW40LX1b&index=21). I’ve [written books](https://pragprog.com/book/es6tips/simplifying-javascript) about new syntax. But I find that most developers, even experienced ones, don’t put much thought into their collection choice.

Time to end that. Not only do we have Arrays and Objects. We also have Maps, Sets, WeakMaps, and WeakSets.

So which should you choose? Each collection has ups and downs. But in general, there are three big factors that should influence your choice:

* **Iterable**: Can you loop over the collection directly and access each member one at a time?
* **Keyed**: Can you find a value using a special key without worrying about the other collection members?
* **Destructurable**: Can you pull pieces of the collection into variables quickly and easily?

Each collection type is strong in some areas and weak in others. There are other advantages and disadvantages, but these are the big three for most code.

### Arrays

Arrays are probably the most flexible collection. That makes them a great point to start exploring collections.

Here’s a list of my grade school teachers (names changed to protect the innocent).

```
const myTeachers = ['Cooper', 'Simes', 'Butler'];
```

Arrays preserve order which is great since this is the correct order of my first, second, and third grade teachers. Since the order is meaningful and I happen to know the meaning, I can use **destructuring** to pull out the items into variables.

```
const [firstGrade, secondGrade, ...others] = myTeachers.
```

Destructuring is a quick way to pull information out of a collection into separate variables. It can also create subsets of information. The variable`firstGrade` has the value of`Cooper` . The next variable, `secondGrade` is `Simes` . The last variable is a little different, using the three dots `...` we are saving the rest of the variables, one in this case, as a separate array. That means `others` is also an array: `['Butler']` . In this case, the `...` is a rest pattern. We’re saving the rest of the of values after all.

Back to my collection of teachers. Let’s say you don’t care about the order they taught me, you are more interested in an alphabetized list. Now, before you sort the array, remember, sorting is a mutating function, so the action will change the original array. And since the order matters, you don’t want to make a permanent change. Fortunately, it’s not a big problem since you can create a new array with the spread operator: `[...myTeachers]` .

The reason you can use the spread operator is that arrays have a built-in iterator which allows you to act on a collection one at a time. In other words, arrays are **iterable**. The spread operator takes those items and creates a new list one at a time. Putting the whole thing in square brackets creates a new array. The iterable property is also what lets you do nice things like loop using `for...of` or run a function on each item of the array as you would do with the `.map` and `.reduce` methods.

Back to sorting. Now that you can make a new array, you don’t have to worry about the mutations. The sort function is a one-liner.

```
const sortedTeachers = [...myTeachers].sort();
```

Since arrays are destructurable and iterable, you can pull out information easily or access each item one at a time. Seems pretty great, right? Of course, arrays are not perfect. Suppose you didn’t know the order of the array, but you did want my second-grade teacher. Now you have a problem. Since arrays are not keyed, you can’t just pull out the information you need. The best you could do is create a complicated array of pairs — an array containing two items — along with an array method to find the one you want.

```
export const myTeacherPairs = [['first', 'Cooper'], ['second', 'Simes'], ['third', 'Butler']];
```

```
return teachers.find(teacherPair => teacherPair[0] === 'second');
```

This is a little clunky. An array of pairs is super important and you’ll see more of them later, but this is a pretty inefficient way to handle data lookups.

The problems are that the collection is not **keyed**. Arrays are good at lots of things, but key-value stores are not one. So you’re in a bind. You like the destructuring properties and the iterables. But retrieving key-value information is not simple. This is usually when developers turn to objects. But before that here’s a summary of arrays:

✅ Destructurable

✅ Iterable

❌ Keyed

### Objects

Most JavaScript developers instinctively reach for an object as soon as they need to store key-value pairs. Objects in JavaScript can get pretty complex. For the sake of this example, think of them as a simple way to pass data around. No functions. No `this` keyword. Just key-value pairs.

Start off by rewriting my array of teachers into an object:

```
const teachers = {  first: "Cooper",  second: "Simes",  third: "Butler",};
```

If you needed to find just my second-grade teacher and didn’t care about the other parts of the object, you can pull it out directly: `teachers.second` . Even better, you can pull the value directly into a variable with destructuring. It’s a simple assignment as long as the variable matches the object key.

```
const { second } = teachers;
```

Destructuring is probably the biggest reason to use objects when passing around data. You can easily collect multiple values in an object and then pass it to another function where you can pull the information out again.

```
function getSecondGradeInfo({ second }) {  const school = "Lakin";  return {    school,    teacher: second  }}
```

Things start to fall apart when you want to iterate over the object. You either have to convert some part of the object to an array or you have to use a `for...in` loop.

```
Object.keys(teachers).map(grade => `${grade}:${teachers[grade]}`).join(' ');
```

```
let myTeacher = '';for(const grade in teachers) {  myTeacher += ` ${grade}:${teachers[grade]}`;}
```

Things are getting a little messy already. You either have to iterate over keys or you have to mutate a variable. Worse still, objects don’t guarantee order. You can never trust your `for...in` loop to give the results in the sequence you want.

All of these problems come from an object’s lack of an iterable property. `Object.keys` and `for...in` both use the iterator that comes from converting keys to an array.

Beyond that, there are other problems with objects. There are limited key options. You can’t use [numbers](http://speakingjs.com/es5/ch17.html#object_literals) as keys, for example. They aren’t as [performant](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Keyed_collections_Maps_Sets_WeakMaps_WeakSets) as other collections. But for the most part, they are good for passing data around without a lot of loops.

To summarize:

✅ Destructurable

❌ Iterable

✅ Keyed

### Maps

Maps are a new collection type for JavaScript. They are a proper key-value store. Which is just a way of saying they were designed specifically for that purpose. Unlike objects, you still have to explicitly create a new instance:

```
const teachers = new Map();
```

After that, you set each item by passing a key then a value as arguments.

```
teachers.set('first', 'Cooper').set('second', 'Simes').set('third', 'Butler);
```

To retrieve a value, you call the `get()` method along with the key name.

```
teachers.get('second'); // Simes
```

This might look a little familiar already. It’s not much different than`localStorage.setItem(key, value` which you may have used to store data between visits to a webApp.

As key-value stores, maps are pretty great. They take a wider [variety of keys](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#Objects_and_maps_compared). And while an objects lookup time is linear, a Map’s lookup time will be [logarithmic](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Keyed_collections_Maps_Sets_WeakMaps_WeakSets).

But the biggest advantage is that they have a built-in iterable. That means you can do things like access key-value pairs directly:

```
let myTeachers = '';for([grade, name] of teachers) {  myTeachers += ` ${grade}:${name}`;}
```

A few things to say about that. It may look like you are destructuring the map at the start of the for loop. You actually aren’t. When you iterate over a map, you get back a pair with the key and the value. So you’re actually destructuring an array.

Next, you may notice that you’re still mutating a variable. That’s not so great. Fortunately, since a map is an iterable, you can use the spread operator to convert the map to an array of pairs. That means

```
[...teachers]
```

will become

```
[  ['first', 'Cooper'],  ['second', 'Simes'],  ['third', 'Butler'],]
```

With the map converted to an array, you can now map the items to create your string.

```
[...teachers].map(([grade, name]) => `${grade}:${name}`).join();
```

That means that you have access to all the array methods in three short characters.

Oh, and since it’s iterable, the order is preserved. If you add your first-grade teacher at the beginning, you’ll get it at the beginning.

So what are the disadvantages? The biggest is the lack of direct destructuring. You can’t pull a value out without either calling the `get()`method or by converting to an array. That means passing data between functions gets a little wordier. You also can’t represent maps as a JSON string. So you won’t pull maps from an API anytime soon.

Still, if you have data that you know you’ll want to loop over while still retaining the ability to pull data quickly with a key, maps are your best best.

To summarize:

❌ Destructurable

✅ Iterable

✅ Keyed

### Moving Between

You probably noticed one frustrating pattern. There’s no one collection that can do it all.

Fortunately, that’s not as big of a problem as you may think.

You’ve already seen that you can convert a map to an array with the spread operator. You can also go the other way and convert an array to the map, by passing it into the constructor.

You can also speed up the initial creation process by passing an array of pairs:

```
const myTeachers = [  ['first', 'Cooper'],  ['second', 'Simes'],  ['third', 'Butler'],]const teachers = new Map(myTeachers);
```

At this point, when you have a map, you essentially have access to both the properties of an array and the properties of a map with only a slight conversion.

Objects are getting better. With `Object.entries()` you can create an array of pairs from an object.

```
const teachers = {  first: "Cooper",  second: "Simes",  third: "Butler",};
```

```
const myTeachers = Object.entries(teachers);
```

```
myTeachers[0]// ['first', 'Cooper']
```

That means when you have an object, you have access to array methods with a simple conversion. Going back, though, is a little harder. There’s currently a [proposal](https://github.com/tc39/proposal-object-from-entries) for `Object.fromEntries()` that will take an array of pairs and create an object. But that’s still a little bit away.

However, once it’s here, you won’t be locked into any particular collection type. And that’s the best news of all. Once you can move easily and quickly between collections, you can start to leverage the best features of each. Destructuring values when it’s convenient, iterating when you need to.

In other words, you can look at the data you have and the code you need and pick the appropriate collection type. If another function needs a different type, write a simple conversion. No more guessing. No more frustrations. You can match your collection to your goals not your code to your collection.

