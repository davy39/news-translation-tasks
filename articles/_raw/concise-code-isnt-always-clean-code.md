---
title: Concise Code Isn't Always Clean Code – and Here's Why
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-23T23:29:37.000Z'
originalURL: https://freecodecamp.org/news/concise-code-isnt-always-clean-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/Code-Photography-Images-02.jpg
tags:
- name: best practices
  slug: best-practices
- name: clean code
  slug: clean-code
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
seo_title: null
seo_desc: "By Kenny Dubroff\nAs developers, we want to write code that works, is readable,\
  \ efficient, concise, and if possible, reusable. \nWhen a lot of us think of clean\
  \ code, we probably fall into the trap of thinking that less code is better code.\
  \ While this ..."
---

By Kenny Dubroff

As developers, we want to write code that works, is readable, efficient, concise, and if possible, reusable. 

When a lot of us think of clean code, we probably fall into the trap of thinking that less code is better code. While this is often the case, it's not always so. 

If I can get the job done in a way that other developers can follow behind me and immediately (or at least easily) understand what I’ve done, that’s what I’ll do. 

## So, What Is Clean Code?

These days it’s much more important that you and I can read the code efficiently than the device can (in _most cases_)_._

When I write code, my first objective is always to get the job done. Following that, I write code for human readability, then runtime complexity, then conciseness. Finally, if I can, I make the code easily reusable. 

If I must write code in such a way that it’s no longer easily human readable in order to satisfy a complexity/time or re-usability requirement, you can be sure that it will be very well documented.

## An Example of What I Consider Clean Code

I was recently given a challenge to find a sole odd number in an array of even numbers, or vice-versa. I was given an array of Integers as the input, and I didn't know whether or not it contained odd or even numbers. There would definitely be a minimum of 3 values in the array and only one of them would be odd/even.

### This was my solution:

```swift
func findOutlier(_ array: [Int]) -> Int {
  //since we're guaranteed to have 3 values, grab the first 3
  let parityArr = [
      array[0],
      array[1],
      array[2]
  ]
  //track any odd or even numbers found in parityArr || O(1) - (technically O(n) but we know the input won't grow)
  var odd = 0
  var even = 0
  for num in parityArr {
     //number is even
     if num % 2 == 0 {
         even += 1
     //number is odd
     } else {
         odd += 1
     } 
  }
  //track and test whether there were more odd or even numbers in the array
  var isEven = false
  if even > odd {
      isEven = true
  }  
  //return the first match that's an outlier based on the array containing more even or more odd numbers || O(n) - we don't know the input size 
  if isEven {
      return array.first(where: ({ $0 % 2 != 0 }))!
  } else {
      return array.first(where: ({ $0 % 2 == 0 }))!
  }
}
```

If you’ll notice, I left notes that included the runtime complexity, or how efficiently an algorithm scales — even though that’s probably pretty obvious if you care about that sort of thing. I also left notes on what the input size was of a given operation (even though again, it’s pretty obvious).

## When To Be Concise and When To "Write It Out"

There are instances where concise code can reduce compilation time, or runtime execution, or a number of other things. Again though, my chief concern is whether or not the next developer can read it, follow along easily, and work with it.

### How Can Being Too Concise Affect Readability?

In my return for instance, I could've made this line `return array.first(where: ({ $0 % 2 != 0 }))!` into a for loop where I returned the first match. But it would be doing the exact same thing, and because of the way this is named, I think it's just as readable. 

But maybe you don't understand closure syntax, or your coworker doesn't. That's OK - spell it out. I chose not to, because this appears just as readable to me yet is more concise.

`return array.first(where: { ...` "written out" is:

```swift
for num in array {
    if num %2 !=0 {
        return num
    }
}
```

There are a few opportunities to make the code in this example more concise, and still remain readable for the majority of developers.

As such, I could've also made this block:

```swift
var isEven = false
if even > odd {
    isEven = true
}
```

Look more like this:

`var isEven = even > odd`

The return block noted above could be made into a 1-line check using the ternary operator, but there seem to be an increasing number of developers that aren’t familiar with the ternary operator. I think an if/else block is more readable in most cases as well:

```swift
if isEven {
    return array.first(where: ({ $0 % 2 != 0 }))!
} else {
    return array.first(where: ({ $0 % 2 == 0 }))!
}
```

`return isEven ? array.first(where: {$0 %2 != 0}) : array.first(where: {$0 %2 == 0})`

Personally, I just find both of those concise one line statements to be a little less easily readable - especially where the ternary operator is involved.

At any rate, I was pretty satisfied with my solution – it passed all of the unit tests, it was pretty efficient, and it was human readable. But when I saw other people’s solutions, at first I was a little ashamed of my rudimentary one…

A lot of them were using filter, a lot of them were using the ternary operator. Most of them were a lot more concise. 

### An Example of Being Too Concise

The top-rated answer was 2 lines of code that I had a hard time reading at first – but that code will definitely get the job done. It may be more efficient than my solution in some cases, and it is obviously very concise:

```swift
func findOutlier(_ array: [Int]) -> Int {
    let odd = array.filter{$0 % 2 != 0}
    return odd.count > 1 ? array.filter{$0 % 2 == 0}[0] : odd[0]
}
```

Both of those examples meet the first criteria of writing clean (or really, any) code - they work. They're both also concise, though my solution could be more concise. At first glance, I thought the more concise solution was great. It’s elegant, it’s efficient, and it’s… concise. 

Then I started to break up the return into an if/else and realized my solution is probably more efficient most of the time. I’m only ever iterating over the whole array once, and only if the parity outlier is the final number in the array. 

It's still a good solution, but I wouldn't say it's _great_ (or as many on the site noted - a best practice).

In the case of a majority even array in the concise solution, it would be filtered twice. Once to create the array called odd (which could also be named better)  — that’s the entire array being iterated over. Then again if it turns out not to be a majority odd array. 

This is no big deal if there are only 3 numbers. But given an array of 10,000 numbers, you’re looking at a chunk of time where your user is left waiting for something to compute that doesn’t need to be computed.

Another thing to note about my solution vs the concise solution is that my answer is returned as soon at it’s found in the array. 

Let’s say the input array was odd, and the even number was the first number in the array. In my solution, it would be computed and returned almost immediately, while in the concise solution, we’d be waiting for the entire array to be filtered before returning the answer.

### A Note on Re-usability

I touched on re-usability early on, but we haven't talked about it much. Code that's reusable means you can use it in more than just one situation. 

This is one of the chief concerns of writing clean code, but only when it applies. We can do this by using parameters in functions that are flexible for different use cases, and other things that go along the lines of being able to use our code somewhere else without any or much modification.

**But how can writing reusable code affect readability?**  
I could've made this whole function generic. It would still meet the criteria, and would make it more reusable. We would be able to check any numeric type for example, but that wasn't in the scope of this project, and doing so would make it less readable if you aren't familiar with generic syntax.

## Keeping It Clean Avoids Pitfalls

One of the pitfalls of writing code that’s a little too concise is that it’s difficult to account for edge cases. This is because it makes it more difficult to to see the “moving pieces” at a glance.

I’m definitely not saying my solution is perfect. I can already see one way I could make it more efficient (we could skip the final O(n) operation in some cases) and still remain readable. 

But the point is, I can come back to this code at any time in the near or distant future, easily see how it's working, and how I can make it better.

Just remember, there’s a lot that goes into writing clean code. Clean doesn’t **just** mean concise! Write your code so other developers can work with it — every human that works on it will thank you.


