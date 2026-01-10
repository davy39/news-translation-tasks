---
title: 'Data Structures 101: Arrays — A Visual Introduction for Beginners'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2019-02-12T16:29:51.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-arrays-a-visual-introduction-for-beginners-7f013bcc355a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*plaTqL5DDa2MgqeK-0EClg.png
tags:
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Get to know the data structures that you use every day.

  👋 Welcome! Let’s Start with some Vital Context. Let me ask you this:✅ Do you listen
  to music on your smartphone?✅ Do you keep a list of contacts on your phone?✅ Have
  you ever seen a leaderboard...'
---

### Get to know the data structures that you use every day. 

👋 Welcome! Let’s Start with some Vital Context. Let me ask you this:   
✅ Do you listen to music on your smartphone?  
✅ Do you keep a list of contacts on your phone?  
✅ Have you ever seen a leaderboard during a competition?

**If your answer is “yes” to any of these questions, then it’s almost certain that you’ve used arrays and you didn’t even know it! 😃** Arrays are very powerful data structures that store **lists of elements.** They have endless applications. They are very important in the world of computer science.

In this article, you will learn the pros and cons of arrays, their structure, operations, and use cases.

**Let’s begin! **👍****

### 🔎 Deep Dive Into the Basic Structure of Arrays

To understand how they work, it’s very helpful to visualize your computer’s memory as a grid, just like the one below. Each piece of information is stored in one of those small elements (squares) that make the grid.

![Image](https://cdn-media-1.freecodecamp.org/images/uxNDqnrhHuS197WjrTeak8WQq2QZKAJD5xp4)

**Arrays** take advantage of this “grid” structure to **store** **lists of related information in** **adjacent memory locations** to guarantee extreme efficiency for finding those values. 🔳🔳🔳🔳

**You can think of arrays like this:**

![Image](https://cdn-media-1.freecodecamp.org/images/HjKZtf6JKxcrH8t51iRrId-4lTqjOlGtICip)

**Their elements are next to each other in memory.** If you need to access more than one of them, the process is extremely optimized because your computer already knows where the value is located.

Awesome, right? Let’s learn how this works behind the scenes! 😃

#### 📚 Classification

Arrays are classified as **Homogeneous Data Structures** because they store **elements of the same type**.

They can store numbers, strings, boolean values (true and false), characters, objects, and so on. But **once you define the type of values that your array will store,** **all its elements must be of that same type. You can’t “mix” different types of data.**

![Image](https://cdn-media-1.freecodecamp.org/images/sbk9-CGxQ5VKddqpz9S12GxpR26I8f8e0hj6)

![Image](https://cdn-media-1.freecodecamp.org/images/oS1i6uyY71HPvrPCVEqEVDpscFgyeUCAwlPN)

### 👀 Reading Values — The Magic Begins!

The amazing power of arrays comes from their **efficiency to access values**. This is achieved thanks to its grid-like structure. Let’s take a look at this in more detail.🔍

**When you create an array, you:**  
- Assign it to a variable. 👈  
- Define the type of elements that it will store. 🎈  
- Define its size (the maximum number of elements). 📚

![Image](https://cdn-media-1.freecodecamp.org/images/xzGLFN8ymKFdxyZWHk4YInJ6cyQQHxUJiJQX)

**💡** **Note:** The name that you assign to this variable is very important because you will use it later in your code to access values and to modify the array.

But how can you tell the computer which particular value you would like to access? This is where indices take a vital role!

#### 1️⃣ Indices

**You use what it’s called an “index”** (“indices” in plural) to access a value in an array. This is a number that refers to the location where the value is stored.

As you can see in the diagram below, the first element in the array is referred to using index 0. As you move further to the right, the index increases by one for each space in memory.

![Image](https://cdn-media-1.freecodecamp.org/images/TuWNHRYkAgpBEjuszG9DElXUIAf8Osw2z--7)

**💡** **Note:** I know that it seems strange at first to start counting from 0 instead of 1, but this is called [Zero-Based Numbering](https://en.wikipedia.org/wiki/Zero-based_numbering). It’s very common in computer science.

**The general syntax to access an element is:** `**<ArrayVariable>[<index>]**`

**For example:**  
If your array is stored in the variable `**myArray**` and you want to access the first element (at index 0), you would use `**myArray[0]**`

![Image](https://cdn-media-1.freecodecamp.org/images/Yu9nSlzmHkZV4e7f7sulFIamSwWONw4wNcpg)

#### 2️⃣ Memory

Now that you know how to access values, let’s see how arrays are stored in your computer’s memory. **When you define the size of the array, all of that space in memory is “reserved” from that moment on** for future values that you may want to insert.

**💡 Note:** If you do not fill the array with values, that space will be kept reserved and empty until you do.

**For Example:**  
Let’s say that you define an array of size 5 but only insert one value. All that remaining space will be empty and “reserved” in memory, waiting for future assignments.

![Image](https://cdn-media-1.freecodecamp.org/images/7Hoys8sq0RuDF4-Rgr4WRD4RrImGhtQmzR9P)

This is key because arrays are extremely efficient in accessing values because all the elements are stored in contiguous spaces in memory. **This way, the computer knows exactly where to look to find the information you requested.**

**But…** there is a downside to it 😞 because this is **not memory-efficient**. You are reserving memory for future operations that may not occur. **This is why arrays are recommended in situations when you know beforehand how many elements you are going to store.**

### 🔧 Operations — Behind the Scenes!

Now that you know what arrays are when they are used, and how they store elements, we will dive into their operations like insertion and removal.

#### 1️⃣ Insertion — Welcome!

Let’s say that we have an array of size 6 and there’s still an empty space. We want to insert an element “e” at the beginning of the array (index 0), but this place is already taken by the element “a.” What should we do?

![Image](https://cdn-media-1.freecodecamp.org/images/JX8sviJCpwXkWT6mZ4fDIwzSNFDUZ0C8LfrP)

**To insert into arrays**, we move all the elements located to the right of the insertion site, one index to the right. Element “a” will now be at index 1, element “b” will be at index 2 and so on…

![Image](https://cdn-media-1.freecodecamp.org/images/8KFz74m1v5dPBzXGr5IXAvt3a5XFbzL78gVs)

**💡** **Note:** You will need to create a variable to keep track of the last index that contains elements. In the diagram above, the array is filled up to index 4 before the insertion. This way, you can determine if the array is full and what index you should use to insert an element at the end.

After doing this, our element is successfully inserted. 👏

![Image](https://cdn-media-1.freecodecamp.org/images/VqmOSyTnIvPWbkw9p1PIhenPthaxd3bHxzvS)

#### ⚠️ Wait a minute! What Happens if the Array is Full?

What do you think will happen if the **array is full and you try to insert** an element? 😱

![Image](https://cdn-media-1.freecodecamp.org/images/IlI473xQSRYYCMjlcF0YMSOs-Kca2hqqupGk)

**In this case, you need to create a new, larger array and manually copy all the elements into this new array.** This operation is **very expensive, time-wise.** Imagine what would happen if you had an array with millions of elements! That could take a very long time to complete. ⏳

![Image](https://cdn-media-1.freecodecamp.org/images/P2q2OaohnsEPDa3KMu3e6eOJaPpw-bpufH95)

**💡** **Note:** The only exception to this rule, when insertion is very fast, is when you insert an element at the **end** of the array (at the index located to the right of the last element) and there is still space available. This is done in constant time O(1).

#### 2️⃣ Deletion— Bye, Bye!

Now let’s say that you want to delete an element from the array.

![Image](https://cdn-media-1.freecodecamp.org/images/yG5HNXTX7Xj7aXAstjEMU2VNWHkEZXtG9q5z)

To maintain the efficiency of random access (being able to access the array through an index extremely fast) the elements must be stored in contiguous spaces of memory. **You can’t just delete the element and leave that space empty.**

![Image](https://cdn-media-1.freecodecamp.org/images/bd9KRk22FyVVrW3RJEKvCd8y-VAJQodeABOD)

You should move the elements that come after the element that you want to delete one index the left.

![Image](https://cdn-media-1.freecodecamp.org/images/G13PaxPTyIQRCBJdh2Ioup-4jM-qlDMnTVd7)

And finally, you have this resulting array 👇. As you can see, “b” has been successfully deleted.

![Image](https://cdn-media-1.freecodecamp.org/images/85yhQ9XK19hJ2paBhkb9Cf0-8v52DO0igncc)

**💡 Note:** Deletion is very efficient when you remove the **last** element. Since you need to create a variable to keep track of the last index that contains elements (in the diagram above, index 3), you can directly remove that element using the index.

#### 3️⃣ Finding an Element

You have three options to find an element in an array:

* **If you know where it’s located**, use the index.
* **If you don’t know where it’s located and your data is sorted**, you can use algorithms to optimize your search, such as Binary Search.
* **If you don’t know where it’s located and your data is not sorted**, you will need to search through every element in the array and check if the current element is the element you are looking for (please see the sequence of diagrams below).

![Image](https://cdn-media-1.freecodecamp.org/images/hlrl4kdBl3eM8cT7DXJX7rItWeHzTvrretfG)

![Image](https://cdn-media-1.freecodecamp.org/images/nFz0jZQu4dtAqv4fauEE-7zVqxtGlKVVfKew)

![Image](https://cdn-media-1.freecodecamp.org/images/hxcwNp-VfOem0psPkl26HCLrILCR1mlrdpku)

![Image](https://cdn-media-1.freecodecamp.org/images/dEd3ArmSERT63fk95KSlKwwCqdwjvUBAOQen)

### 👋 In Summary…

* **Arrays are extremely powerful data structures** that store elements of the same type. The type of elements and the size of the array are fixed and defined when you create it.
* **Memory is allocated immediately** after the array is created and it’s empty until you assign the values.
* Their **elements are located in contiguous locations in memory**, so they can be accessed very efficiently (random access, O(1) = constant time) using **indices**.
* **Indices start at 0**, not 1 like we are used to.
* **Inserting elements** at the beginning or in the middle of the array involves moving elements to the right. If the array is full, creating a new, larger array (which is not very efficient). Inserting at the end of the array is very efficient, constant time O(1).
* **Removing elements** from the beginning or from the middle of the array involves moving all the elements to the left to avoid leaving an empty space in memory. This guarantees that the elements are stored in contiguous spaces in memory. Removing at the end of the array is very efficient because you only delete the last element.
* **To find an element**, you need to check the entire array until you find it. If the data is sorted, you can use algorithms such as Binary Search to optimize the process.

> _“Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning.”_  
>   
> _— Albert Einstein_

#### 👋 Thank you!

I really hope that you liked my article. ❤️  
**Follow me on** [Twitter](https://twitter.com/Estefania_CN_) to find more articles like this one. 😃

