---
title: How I discovered the C++ algorithm library and learned not to reinvent the
  wheel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-discovered-the-c-algorithm-library-and-learned-not-to-reinvent-the-wheel-2398a34e23e3
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_dKpcV4KXSuBhWQLUsNm1gA-1.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By M Chowdhury

  The other day out of curiosity, I looked into the C++ algorithm library. And found
  out quite a good number of cool features!

  This literally amazed me.

  Why? I mean I have mostly written C++ throughout my university life. And it was
  part...'
---

By M Chowdhury

The other day out of curiosity, I looked into the C++ algorithm library. And found out quite a good number of cool features!

This literally amazed me.

Why? I mean I have mostly written C++ throughout my university life. And it was particularly because of my love-hate relationship with [competitive programming](https://en.wikipedia.org/wiki/Competitive_programming).

And very unfortunately, I had never really taken advantage of this amazing library C++ has offered us.

Gosh I felt so naïve!

So I decided it was time to stop being naive and get to know the usefulness of C++ algorithms — at least at a higher level. And as an old man once said, _sharing knowledge is power —_ so here I am.

**_Disclaimer_**_: I have heavily used features from C++11 and beyond. If you are not quite familiar with newer editions of the language, the code snippets I have provided here might seem a bit clumsy. On the other hand, the library we discuss here is far more self-sufficient and elegant than anything I have written below. Feel free to find mistakes and point them out. And also, I could not really consider many of C++17 additions in this post, as most of its features are yet to be brought into life in GCC._

So without further ado, let’s begin!

1. `**all_of any_of none_of**`

These functions simply look for whether `**all**`_,_ `**any**` or `**none**` of the elements of a container follows some specific property defined by you. Check the example below:

```c++
std::vector<int> collection = {3, 6, 12, 6, 9, 12};

// Are all numbers divisible by 3?
bool divby3 = std::all_of(begin(collection), end(collection), [](int x) {
    return x % 3 == 0;
});
// divby3 equals true, because all numbers are divisible by 3

// Is any number divisible by 2?
bool divby2 = std::any_of(begin(collection), end(collection), [](int x) {
    return x % 2 == 0;
});
// divby2 equals true because 6, 12 divisible by 2

// Is no number divisible by 6?
bool divby6 = std::none_of(begin(collection), end(collection), [](int x) {
    return x % 6 == 0;
});
// divby6 equals false because 6, 12 divisible by 6
```

Notice how in the example, the _specific property_ is passed as a lambda function.

So `**all_of, any_of, none_of**` look for some specific property in your `**collection**`. These functions are pretty much self explanatory on what they are supposed to do. Along with the introduction of **lambdas** in C++11, they are pretty handy to use.

2. `**for_each**`

I have always been so accustomed to using age-old `**for**` loop that this cute thing never crossed my sight. Basically, `**for_each**` applies a function to a range of a container.

```c++
std::vector<int> collection = {2,4,4,1,1,3,9};

// notice that we pass x as reference!
std::for_each(begin(collection), end(collection), [] (int &x) {
    x += 26;
});
```

If you are a JavaScript developer, the above code should ring a bell.

3. `**count count_if**`

Pretty much like the functions described in the beginning, `**count**` and `**count_if**` both look for specific properties in your given collection of data.

```
std::vector<int> collection={1, 9, 9, 4, 2, 6};

// How many 9s are there in collection?
int nines = std::count(begin(collection), end(collection), 9);
// How many elements of the collection are even?
int evens = std::count_if(begin(collection), end(collection), [](int x) {
    return x % 2 == 0;
});
// nines equals 2, evens equals 3
```

And a result, you receive the **count** that matches your given value, or has the given property that you provide in the form of a lambda function.

4. `**find_if**`

Say you want to find the first element in your collection satisfying a particular property. You can use `**find_if**`.

```c++
std::vector<int> collection = {1, 2, 0, 5, 0, 3, 4};

// itr contains the iterator to the first element following the specific property
auto itr = std::find_if(begin(collection), end(collection), [](int x) {
    return x % 2==0; // the property
});
```

Remember, as shown in the above example, you will get the **iterator** to the **first element** that matches your given property. So what if you want to find all the elements that match the property using `**find_if**`?

![Image](https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/0_C0IjBIkmmXBEqCEk.jpeg)
_An abstract art to look at if you are getting bored. ([Unsplash](https://unsplash.com/@steve_j?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener noopener noopener">Steve Johnson</a> on <a href="https://unsplash.com/?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener noopener noopener))_

5. `**generate**`

This function essentially changes the values of your collection, or a range of it, based on the **generator** you provide. The generator is a function of the form   
`**T f();**` where `**T**` is a compatible type with our collection.

```
std::vector<int> collection={1, 2, 0, 5, 0, 3, 4};

int counter=0;

// notice that we are capturing counter by reference
std::generate(begin(collection), end(collection), [&]() {
    return counter++;
});

// collection gets replaced by values starting from 0
// modified collection = {0,1,2,3,4,5,6}
```

In the above example, notice that we are actually changing our collection _in-place_. And the generator here is the lambda function we provided.

6. `**shuffle**`

From the standard of C++17, `**random_shuffle**` has been removed. Now we prefer `**shuffle**` which is more effective, given that it takes advantage of the header `**random**`.

```c++
std::vector<int> collection = {1, 2, 13, 5, 12, 3, 4};

std::random_device rd;
std::mt19937 rand_gen(rd());
std::shuffle(begin(collection), end(collection), rand_gen);
```

Note that we are using [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister), a pseudo-random number generator introduced in C++11.

Random number generators have become far more mature in C++ with the introduction of `**random**` library and inclusion of better methods.

7. `**nth_element**`

This function is quite useful, given that it has an interesting complexity.

Say you want to know the _n-th_ element of your collection if it was sorted, but you do not want to sort the collection to make an **_O(n log(n))_** operation.

What would you do?

Then `**nth_element**` is your friend. It finds the desired element in **_O(n)_**_._

```c++
std::vector<int> collection = {1, 2, 13, 5, 12, 3, 4};

auto median_pos = collection.begin() + collection.size() / 2;
std::nth_element(begin(collection), median_pos, end(collection));

// note that the original vector will be changed due to the operations
// done by nth_element
```

Interestingly, `**nth_element**` may or may not make your collection sorted. It will just do whatever order it takes to find the n-th element. Here is an interesting discussion on [StackOverflow](https://stackoverflow.com/questions/10352442/whats-the-practical-difference-between-stdnth-element-and-stdsort).

And also, you can always add your own comparison function (like we added lambdas in previous examples) to make it more effective.

8. `**equal_range**`

So let’s say you have a sorted collection of integers. You want to find the range in which all the elements have a specific value. For example:

```c++
// sorted collection
std::vector<int> collection={1, 2, 5, 5, 5, 6, 9, 12};

// we are looking for a range where all elements equal to 5
auto range = std::equal_range(begin(collection), end(collection), 5);

// the required range is printed like this
std::cout << (range.first - begin(collection)) << " " <<
  			 (range.second - begin(collection)) << std::endl;
```

In this code, we are looking for a **range** in the `**vector**` that holds all `**5**`. The answer is `**(2~4)**`.

Of course we can use this function for our own custom property. You need to ensure that the property you have aligns with the order of the data. See [this article for reference](https://en.cppreference.com/w/cpp/algorithm/equal_range).

Finally, `**lower_bound**` and `**upper_bound**` both can help you to achieve the same that you achieved using `**equal_range**`.

9. `**merge inplace_merge**`

Imagine you have two sorted collections (what a fun thing to imagine, right?), you want to merge them, and you also want the merged collection to remain sorted. How would you do that?

You can just add the second collection to the first one and sort the result again which adds an extra **O(log(n))** factor. Instead of that, we can just use `**merge**`.

```c++
std::vector<int> c1 = {1, 2, 5, 5, 5, 6, 9, 12};
std::vector<int> c2 = {2, 4, 4, 5, 7, 15};

std::vector<int> result; // contains merged elements
std::merge(begin(c1), end(c1), begin(c2), end(c2), std::back_inserter(result));

// result = {1, 2, 2, 4, 4, 5, 5, 5, 5, 6, 7, 9, 12, 15}
```

On the other hand, do you remember when implementing _merge sort,_ we need to merge two sides of our array? `**inplace_merge**` can be conveniently used for that.

Look at this tiny _merge sort_ based on the example given in [cppreference](https://en.cppreference.com/w/cpp/algorithm/inplace_merge):

```c++
void merge_sort(auto l, auto r)
{
    if(r - l > 1)
    {
        auto mid = l+(r-l)/2;
        merge_sort(l, mid);
        merge_sort(mid, r);
        std::inplace_merge(l, mid, r);
    }
}

std::vector<int> collection = {2, 4, 4, 1, 1, 3, 9};
merge_sort(begin(collection), end(collection));
```

How cool is that!

![Image](https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/0_zgexhkawrSJNYfNM.jpeg)
_Speaking of cool, here is a cool guy. ? ([Unsplash](https://unsplash.com/@davealmine?utm_source=medium&amp;utm_medium=referral" rel="photo-creator noopener noopener noopener noopener">Dawid Zawiła</a> on <a href="https://unsplash.com/?utm_source=medium&amp;utm_medium=referral" rel="photo-source noopener noopener noopener noopener))_

10. `**minmax minmax_element**`

`**minmax**` returns the minimum and maximum of the given two values, or the given list. It returns a pair and it can also provide the functionality of your own comparison method. `**minmax_element**` does the same for your container.

```c++
int a = 9, b = 12;

// out.first contains the minimum element, out.second is the maximum one
auto out = std::minmax(a, b);

std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};
auto result = std::minmax_element(begin(collection), end(collection));

// you can also add compare function as the third argument
// (result.first - collection.begin()) is the index of the minimum element
// (result.second - collection.begin()) is the index of the maximum element
```

11. `**accumulate partial_sum**`

`**accumulate**` does what it says, it _accumulates_ values of your collection in the given range, using the initial value and a binary operation function. See for yourself:

```c++
std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};

// Note that we are providing 0 as the initial value, as it should be.
// std::plus<int>() tells that the function should do sums
int sum = std::accumulate(begin(collection), end(collection), 0, std::plus<int>());

// What would happen if initial value was 0 instead of 1 in this call?
int prod = std::accumulate(begin(collection), end(collection), 1, std::multiplies<int>());

// You can also use your custom binary operation.
int custom = std::accumulate(begin(collection), end(collection), 0, [](int x, int y) {
    return x+y;
});
```

So how is the value of `**custom**` calculated?

At the beginning, accumulate takes the initial value (0) to the argument `**x**`, the first value in the collection (6) to argument `**y**`, does the operation, then assigns it to the accumulated value. In the second call, it passes the accumulated value to `**x**` and the next element in the collection to `**y**`, and thus proceeds.

`**partial_sum**` does things much like accumulate, but it also keeps the result of first `**n**` terms in a destination container.

```c++
std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};
std::vector<int> sums, mults;

// contains the partial sum of collection in result
std::partial_sum(begin(collection), end(collection), std::back_inserter(sums));

// contains the partial product
std::partial_sum(begin(collection), end(collection), std::back_inserter(mults), std::multiplies<int>());
```

And of course as you expected, you can use your own custom operation.

12. `**adjacent_difference**`

You want to find the adjacent differences in your values, you can simply use this function.

```c++
std::vector<int> collection = {6, 5, 3, 2, 1, 4, 6, 7};
std::vector<int> diffs;
std::adjacent_difference(begin(collection), end(collection), std::back_inserter(diffs));
// The first element of diffs will be same as the first element of collection
```

Pretty simple, right?

But it can do much more. Look at this:

```c++
std::vector<int> fibs(10, 1);
std::adjacent_difference(begin(fibs), end(fibs) - 1, begin(fibs) + 1, std::plus<>{});
```

What do these two lines do? They find the first 10 Fibonacci numbers! Do you see how? ?

---

So that was it for today. Thanks for reading! I hope you learned something new.

I would definitely like to bring some new stuff for ya’ll again in near future.

Cheers!

