---
title: Algorithms in Javascript - Binary Search Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-15T09:44:40.000Z'
originalURL: https://freecodecamp.org/news/the-working-developers-guide-to-algorithms
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-19-at-15.25.42.png
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: Scrimba
  slug: scrimba
seo_title: null
seo_desc: 'By Per Harald Borgen

  If you want to gain new problem-solving skills and level up your Computer Science
  knowledge, look no further than Scrimba''s free one-hour course, The Working Developer''s
  Guide To Algorithms. It was designed for those who don''t ha...'
---

By Per Harald Borgen

If you want to gain new problem-solving skills and level up your Computer Science knowledge, look no further than Scrimba's free one-hour course, [The Working Developer's Guide To Algorithms](https://scrimba.com/course/galgorithmsguide?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article). It was designed for those who don't have a background in Computer Science and feel they would benefit from learning to think algorithmically.

## What does the course do?

Our guide takes you through how to craft six different binary search algorithms. In classic Scrimba style, it contains a bunch of challenges along the way, so you'll gain the muscle memory you need to improve your skills as a software developer and work better with algorithms going forward.

You'll learn:

- Binary Search
- Big O notation
- Imperative code
- Recursion
- Tail recursion
- Array splitting
- Array view
- Partition

Each algorithm is taught in three stages:

- **Walkthrough:** Jonathan introduces the algorithm conceptually.
- **Implementation:** We get our hands dirty by crafting our own versions of the algorithm.
- **Solution:** Jonathan shows us his implementation for comparison.

## Prerequisites

You'll get the most out of this course if you have a good understanding of Javascript and are ideally already working as a developer or are a Bootcamp graduate. 

If you're not there yet, check out Scrimba's great free tutorials [Introduction to JavaScript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) and [Introduction to ES6+](https://scrimba.com/course/gintrotoes6?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article).

## Intro to the instructor

Jonathan Lee Martin is a software developer, web educator, speaker, and author. He helps other developers achieve their professional and personal goals through writing, speaking, immersive Bootcamps, workshops, and online tutorials. 

With clients including companies such as NASA and HP, he's just the person to take you through the learning journey. So let's get started!

## Binary Search

[![Graph of Sweeper vs Splitter searches.](https://dev-to-uploads.s3.amazonaws.com/i/iphh9m8t8a0jgq94w926.png)](https://scrimba.com/p/pk57XHz/cPJqarfK?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article)
_Click the image to access the course._

In [the first cast](https://scrimba.com/p/pk57XHz/cPJqarfK?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), Jonathan introduces to the concepts of **Big-O notation** and **binary search**, the algorithm we'll be working with.

**Big-O notation** is a means of describing the worst-case performance of an algorithm. A Big O of O(n) says that if an array has a length of n elements, the run time will be proportional to n. In other words, an array of seven entries will take 7 lookups in the worst case, just as an array of 7 million entries will take 7 million entries in the worst case. We can also say this algorithm's runtime is linear, as illustrated in the graph above.

**Binary search** is one of several strategies for answering the question "Where does this element appear in a list?"

When answering the question, there are two main approaches:

- **Sweeper**: Checking through each item in the list until the correct item is found.
- **Splitter** / **Binary Search**: Splitting the list in half, checking whether you have gone too far or not far enough to locate the item, searching either right or left side respectively and repeating until the item is located.

We can think of these approaches in terms of checking an old-school paper phone book. The sweeper approach would involve looking through each and every entry from the start until the correct one is located. The splitter approach is the one most people would use - opening the book randomly and seeing whether you need to go forwards or back until the entry is located.

Binary Search is more efficient than the sweeper approach, particularly for larger lists. But it only works when the list has already been sorted. 

While the sweeper approach has a linear runtime (see graph above) and Big O of O(n), the splitter approach has a sub-linear runtime and a Big O of O(log n).

## Imperative

[In the first challenge cast](https://scrimba.com/p/pk57XHz/czkBGrtD?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), Jonathan encourages us to get our hands dirty by implementing binary search in a traditional style, that is with a Big O of O(n), using a fixed amount of memory and loops.

Jonathan provides us with a test suite we can use to ensure our solution is successful and encourages us to try the challenge ourselves before checking out his implementation. No spoilers here, so head over to the cast to give it try yourself.

While this solution is short and close to the original formulation of binary search, you've probably noticed that the solution was difficult to write and not the best solution from a software craftsmanship point of view. Read on to find out ways to level up the solution...

## Recursion

[In this cast](https://scrimba.com/p/pk57XHz/c2Pr87c4?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), we look at improving our binary search by implementing a new version with a few constraints. While our solution should still have a Big O of O(n), it should not use loops and must use recursion. All variables should be initialized with the `const` operator so they can't be mutated.

Jonanthan kicks us off with a skeleton version of the solution and then encourages us to try the challenge on our own:

```js
let binarySearchWithRecursion = (array, element, compare = defaultCompare) => {
	return -1;
};

export default binarySearchWithRecursion;
```

If you've completed this challenge, you've probably seen that this solution is a lot easier to read but is quite verbose. In the worst case, it can also result in infinite recursion. Continue with the course to see whether there are ways of streamlining the solution...

## Tail Recursion

The challenge for [the next cast](https://scrimba.com/p/pk57XHz/ceMQgZTB?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) is to improve our previous implementation by reducing duplication.

Jonathan warns us that the solution will look worse than the previous two solutions, however, it sets us up for some better optimizations further down the line. Head over to the course now to try the challenge for yourself and see Jonathan's solution.

## Array Splitting

If you completed the previous challenge, you may have felt that we're still passing a lot of extra information into our binary search via recursion. [This cast](https://scrimba.com/p/pk57XHz/cEKyndHw?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) looks at a way of cleaning that up called **array splitting**.

We can think of array splitting in terms of our phone book example from earlier - whenever we decide that half the phone book is irrelevant, we just tear it off and throw it away. Similarly, our next solution should disregard any parts of the array which don't include our desired entry.

To help us achieve this, Jonathan starts us off with some skeleton code:

```js
let binarySearchWithArraySplitting = (
	array,
	element,
	compare = defaultCompare
) => {
	return -1;
};
```

Then, as usual, he gives us free rein to try to the solution for ourselves before walking us through his own implementation.

Although this is an elegant method of binary search, because it involves making a copy of part of the array, it no longer has a Big O of O(n) and has a higher memory usage and slower run time. Continue with the course to find out whether there is a way to regain a higher performance with a similar code solution...

## Array View

[In this cast](https://scrimba.com/p/pk57XHz/cmdvdnhb?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article), we look for ways of merging the higher performance of our previous solutions with the elegance of array splitting. To do this, we create an array-like object that responds to the same methods as an array. We'll then inject this object in place of the original array.

Jonathan gets us started by initializing a function `ArrayView` which returns an object that expects three arguments: `array`, `start` and `end`. When invoked, `ArrayView` should return an object with four methods, `length`, `toArray`, `slice` and `get`.

```js
export let ArrayView = (
    array,
    start = 0,
    end = array.length,
) => ({
    length: end - start,
    toArray: () => array.slice(start, end),
    slice: () => ,
    get: () => ,
});

let binarySearchWithArrayView = (array, ...args) =>
    binarySearchWithArraySplitting(ArrayView(array), ...args)
```

Our challenge is to implement the `slice` and `get` methods of `ArrayView` without making a copy of the original array. Click through to try it out and then view Jonathan's walkthrough.

Although this solution produces better, more readable code, it is longer than some of our previous solutions. Continue with the course to find out if we can retain the benefits of `ArrayView` while lifting even more of the logic out of binary search code...

## Array Partition

In [the final challenge cast](https://scrimba.com/p/pk57XHz/c8rZqEsV?utm_source=dev.to&utm_medium=referral&utm_campaign=galgorithmsguide_launch_article) of the course, Jonathan gives us a goal of extracting some of the cryptic bounce logic in our previous version into a data structure.

For this, we need a simple data structure which returns the middle, left or right part of an array. To start us off, Jonathan sets up a function `ArrayPartition`:

```js
export let ArrayPartition = (array, pivot) => ({
	left: () => array.slice(0, pivot),
	middle: () => array.get(pivot),
	right: () => array.slice(pivot + 1, array.length),
});
```

Next, Jonathan sets up a new version of binary search called `binarySearchWithPartition`, which has a starting signature the same as `binarySearchWithArraySplitting`:

```js
let binarySearchWithPartition = (array, element, compare = defaultCompare) => {
	if (array.length === 0) {
		return -1;
	}
	const middle = Math.floor(array.length / 2);
	const comparison = compare(element, array.get(middle));

	if (comparison === 0) {
		return middle;
	}

	//bounce logic
	const [left, right] =
		comparison === -1 ? [0, middle - 1] : [middle + 1, array.length];
	//end of bounce logic

	const subIndex = binarySearchWithArraySplitting(
		array.slice(left, right),
		element,
		compare
	);

	return subIndex === -1 ? -1 : left + subIndex;
};

let binarySearchWithPartitionAndView = (array, ...args) =>
	binarySearchWithPartition(ArrayView(array), ...args);
```

Our challenge now is to rewrite `binarySearchWithPartition` with none of the `bounce` logic highlighted above, instead of creating an array partition and making calls to its left, middle and right methods.

Head over to the course now to try the challenge for yourself. As Jonathan points out, this challenge is tricky, so it's ok to skip to his solution if you get stuck for too long but give it a go first on your own.

## Wrap-Up

You've made it to the end of the course - great work! We've covered several approaches to binary search, all with their own benefits and drawbacks, and we've built some great muscle memory for working effectively with algorithms. 

Now that you've seen six different approaches to binary search, you'll probably notice it pop up in many different places in programming.

Jonathan's full course featuring 10 algorithms will be coming out at the end of the year, but in the meantime, I hope you can put your newfound binary search skills to good use.

Happy coding :)

%[https://www.youtube.com/watch?v=v684EuCrPAM]


