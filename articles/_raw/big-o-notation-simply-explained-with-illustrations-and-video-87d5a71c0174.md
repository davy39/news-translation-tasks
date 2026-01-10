---
title: Big O Notation — Simply explained with illustrations and video
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2018-08-21T18:58:28.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation-simply-explained-with-illustrations-and-video-87d5a71c0174
coverImage: null
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Illustration (and most in this article) by Adit Bhargava

  Big O notation is used to communicate how fast an algorithm is. This can be important
  when evaluating other people’s algorithms, and when evaluating your own! In this
  article, I’ll explain what...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/0*Z0GAhU_e8tTBnm_C.jpg)
_Illustration (and most in this article) by Adit Bhargava_

Big O notation is used to communicate how fast an algorithm is. This can be important when evaluating other people’s algorithms, and when evaluating your own! In this article, I’ll explain what Big O notation is and give you a list of the most common running times for algorithms using it.

### Algorithm running times grow at different rates

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qd-Lmu7Xyy30i30dA4RnSg.gif)
_My son explains big ‘O’ notation._

My son Judah has a lot of toys. In fact, he has acquired a _billion_ toys! You’d be surprised how quickly a kid can get that many toys if he’s the first grandchild on both sides of the family. ??

Anyway, Judah has a problem. When his friends visit and want to play with a specific toy, it can take FOREVER to find the toy. So he wants to create a search algorithm to help him find a specific toy as quick as possible. He is trying to decide between two different search algorithms: simple search and binary search. (Don’t worry if you are not familiar with these algorithms.)

The algorithm chosen needs to be both fast and correct. On one hand, binary search is faster. And Judah often only has about 3_0 seconds_ before his friend gets bored looking for a toy. On the other hand, a simple search algorithm is easier to write, and there is less chance of bugs being introduced. It sure would be embarrassing if his friend found bugs in his code! To be extra careful, Judah decides to time both algorithms with a list of 100 toys.

Let’s assume it takes 1 millisecond to check one toy. With simple search, Judah has to check 100 toys, so the search takes 100 ms to run. On the other hand, he only has to check 7 toys with binary search (log2 100 is roughly 7, don’t worry if this math is confusing since it isn’t the main point of this article), so that search takes 7 ms to run. But really, the list will have a billion toys. If it does, how long will simple search take? How long will binary search take?

![Image](https://cdn-media-1.freecodecamp.org/images/0*B1gUpMQDoauyYBht.jpg)

### Running time for simple search vs. binary search, with a list of 100 elements

Judah runs binary search with 1 billion toys, and it takes 30 ms (log2 1,000,000,000 is roughly 30). “32 ms!” he thinks. “Binary search is about 15 times faster than simple search, because simple search took 100 ms with 100 elements, and binary search took 7 ms. So simple search will take 30 × 15 = 450 ms, right? Way under the 30 seconds it takes for my friend to get bored.” Judah decides to go with simple search. Is that the right choice?

No. Turns out, Judah was wrong and lost a friend for life. ? The run time for simple search with 1 billion items will be 1 billion ms, which is 11 days! The problem is, the run times for binary search and simple search d_on’t grow at the same rate._

![Image](https://cdn-media-1.freecodecamp.org/images/0*GsE3ava8DELYKPhs.jpg)

Run times grow at very different speeds! As the number of items increases, binary search takes a little more time to run, but simple search takes a _lot_ more time to run. So as the list of numbers gets bigger, binary search suddenly becomes a _lot_ faster than simple search.

So Judah was wrong about binary search always being 15 times faster than simple search. If there are 1 billion toys, it’s more like 33 million times faster.

It is very important to know how the running time increases as the list size increases. That’s where Big O notation comes in.

Big O notation tells you how fast an algorithm is. For example, suppose you have a list of size _n_. Simple search needs to check each element, so it will take _n_ operations. The run time in Big O notation is O(_n_).

Where are the seconds? There are none — Big O doesn’t tell you the speed in seconds. _Big O notation lets you compare the number of operations._ It tells you how fast the algorithm grows.

Let’s do another example. Binary search needs log _n_ operations to check a list of size _n_. What’s the running time in Big O notation? It’s O(log _n_). In general, Big O notation is written as follows.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8IeDKdt-A5ED-hNe.jpg)

This tells you the number of operations an algorithm will make. It’s called Big O notation because you put a “big O” in front of the number of operations.

#### Big O establishes a worst-case run time

![Image](https://cdn-media-1.freecodecamp.org/images/0*UK86o6VxxJcGHxVw.png)

Suppose you’re using simple search to look for a user in your user database. You know that simple search takes O(_n_) time to run, which means in the worst case, you’re algorithm will have to look through every user in the database. In this case, you’re looking for a user with the name ‘aardvark213’. This is the first user in the list. So your algorithm didn’t have to look at every entry — it found it on the first try. Did the algorithm take O(_n_) time? Or did it take O(1) time because it found the person on the first try?

Simple search still takes O(_n_) time. In this case, the algorithm found what it was looking for instantly. That’s the best-case scenario. But Big O notation is about the _worst-case_ scenario. So you can say that, in the _worst case_, the algorithm will have to look through every user in the database once. That’s O(_n_) time. It’s a reassurance — you know that simple search will never be slower than O(_n_) time.

### Some common Big O run times

![Image](https://cdn-media-1.freecodecamp.org/images/1*G3c_ADXB8Klbi8XiRvhhqQ.png)
_From [xkcd](https://xkcd.com/399/" rel="noopener" target="_blank" title="). If you don’t get the joke, learn more about the traveling salesman problem in my course from Manning Publications. :)_

Here are five Big O run times that you’ll encounter a lot, sorted from fastest to slowest:

* O(log _n_), also known as _log time._ Example: Binary search.
* O(_n_), also known as _linear time_. Example: Simple search.
* O(_n_ * log _n_). Example: A fast sorting algorithm, like quicksort.
* O(_n_2). Example: A slow sorting algorithm, like selection sort.
* O(_n_!). Example: A really slow algorithm, like the traveling salesperson.

### Visualizing different Big O run times

![Image](https://cdn-media-1.freecodecamp.org/images/1*KQByBDNVa547MN6VXVWu9A.png)

Suppose you’re drawing a grid of 16 boxes, and you can choose from 5 different algorithms to do so. If you use the first algorithm, it will take you O(log _n_) time to draw the grid. You can do 10 operations per second. With O(log _n_) time, it will take you 4 operations to draw a grid of 16 boxes (log 16 base 2 is 4). So it will take you 0.4 seconds to draw the grid. What if you have to draw 1,024 boxes? It will take you log 1,024 = 10 operations, or 1 second to draw a grid of 1,024 boxes. These numbers are using the first algorithm.

The second algorithm is slower: it takes O(_n_) time. It will take 16 operations to draw 16 boxes, and it will take 1,024 operations to draw 1,024 boxes. How much time is that in seconds?

Here’s how long it would take to draw a grid for the rest of the algorithms, from fastest to slowest:

![Image](https://cdn-media-1.freecodecamp.org/images/0*B42QL_XBJgDGfIFd.jpg)

There are other run times, too, but these are the five most common.

This is a simplification. In reality you can’t convert from a Big O run time to a number of operations this neatly, but this is good estimation.

### Conclusion

Here are the main takeaways:

* Algorithm speed isn’t measured in seconds, but in growth of the number of operations.
* Instead, we talk about how quickly the run time of an algorithm increases as the size of the input increases.
* Run time of algorithms is expressed in Big O notation.
* O(log _n_) is faster than O(_n_), but it gets a lot faster as the list of items you’re searching grows.

And here is a video that covers a lot of what is in this article and more.

I hope this article brought you more clarity about Big O notation. This article is based on a lesson in my video course from Manning Publications called [Algorithms in Motion](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293). The course is based on the _amazing_ book [Grokking Algorithms](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a) by Adit Bhargava. He’s the one who drew all the fun illustrations in this article.

If you learn best through books, [get the book](https://www.amazon.com/gp/product/1617292230/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=bcar08-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=1617292230&linkId=83471c93327ff24766dd812f9799f95a)! If you learn best through videos, consider [buying my course](https://www.manning.com/livevideo/algorithms-in-motion?a_aid=algmotion&a_bid=9022d293). You can get 39% off my course by using the code ‘**39carnes**’.

