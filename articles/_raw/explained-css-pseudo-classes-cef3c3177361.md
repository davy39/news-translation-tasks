---
title: How CSS pseudo-classes work, explained with code and lots of diagrams
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-06T06:24:33.000Z'
originalURL: https://freecodecamp.org/news/explained-css-pseudo-classes-cef3c3177361
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FypLaInuQOolvpO95NtBIQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nash Vail

  Let’s be honest — there are times when CSS can really hurt your brain. It’s hard
  enough to center an element inside its parents.

  Today, we’re going to make sense of an even more challenging aspect of CSS: pseudo-classes.


  Obligatory Fami...'
---

By Nash Vail

Let’s be honest — there are times when CSS can really hurt your brain. It’s hard enough to center an element inside its parents.

Today, we’re going to make sense of an even more challenging aspect of CSS: pseudo-classes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZPlE0Td0GCO2mt3Ivrmp5g.gif)
_Obligatory Family Guy CSS gif_

The pseudo-classes I’ll cover here come in two flavors.

* *-of-type selectors
* *-child selectors

You may be thinking, “But I’m here to learn pseudo-classes. Why are we talking about selectors?” Well, these are basically the same thing, and I will use these terms interchangeably.

Pseudo-classes are sometimes hard to grasp, mainly because they’re presented in an abstract way. So I’ll take a different approach here and help you understand these by drawing a DOM tree.

#### The Markup and The Tree

First, take a look at this block of HTML. I’ll use this code in all my examples.

```
<body>  <div class=”main”>     <a href=”#”>Inner Link 1</a>     <a href=”#”>Inner Link 2</a>     <ul>       <a href=”#”>Inner Inner Link 1</a>       <li>         <a href=”#”>List Item 1</a>       </li>       <li>         <a href=”#”>List Item 2</a>       </li>     </ul>     <a href=”#”>Inner Link 3</a>  </div>  <a href=”#”>Outer Link 1</a>  <a href=”#”>Outer Link 2</a></body>
```

Now I’m going to convert this code into something more visual and more intuitive: a tree.

The following body element has 3 children, _.main_ and two _anchor_ elements.

```
<body>  <div class=”main”>   ...  </div>  <a href=”#”>Outer Link 1</a>  <a href=”#”>Outer Link 2</a></body>
```

Here’s what the relation between _body_ and its three children looks like when you is represent it as a tree:

![Image](https://cdn-media-1.freecodecamp.org/images/1*0J4m0pNfNUUe-JE9dPIbHw.png)
_Fig. 1_

One thing to keep in mind is that the order in which children are placed in the tree is important. Children located top to bottom in code are placed left to right in the tree.

Next, let’s look at the _.main_ div:

```
<div class=”main”>   <a href=”#”>Inner Link 1</a>   <a href=”#”>Inner Link 2</a>   <ul>     ...   </ul>   <a href=”#”>Inner Link 3</a></div>
```

.main has 4 children. The first two are _anchor_ elements then an _ul_ and then again an anchor elements.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b1bt8tsEPJ7L1jJNkSB1WQ.png)
_Fig . 2_

Similarly, we step down each level of nesting and draw the complete tree out of the HTML code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xn3NJH7ajQ0t-nSQWkr2HA.png)
_Fig. 3 — Tree representation of the HTML code_

In order for this article to bear any fruit for you, it’s important that you understand this tree.

“Ha ha nice pun there!” “Thanks!” Increment the pun counter to 1, and let’s move to our very first pseudo-class.

### Pseudo-class #1 :only-of-type

All pseudo-classes follow the same format:

```
what-you-want-to-select:filter { /* styles */ }
```

_what-you-want-to-select_ can be used to select anything that exists as a collection in the DOM. Here, allow me to go ahead and show you an example:

```
a:only-of-type {   border: 2px solid black;}
```

In the code snippet shown above, _what-you-want-to-select_ are anchor elements (the _a_ tag), and the _filter_ is _only-of-type._ We’ll see in a moment what this selector does.

First, I’ve setup a [codepen](http://codepen.io/nashvail/pen/VKkXLB) for if you’re too lazy to create a tester project. You’re welcome, friend!

You can follow along, see the changes, get confused, then come back to this article for the explanation. You do your part, I’ll do mine.

Here’s me doing my part, explaining the code shown above. We’ll start by selecting everything that there is, and then eventually filter down.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uBjIeeXnjBgkB2GApFiiGQ.png)
_Fig. 4 — selecting everything_

Notice how the selection has been done? Each section in the tree (numbered 1 to 5) has elements with a common parent. The parent of Section 1 is _body_, the parent of Section 2 is ._main,_ and so on. **Once again, notice that each section corresponds to a level deeper in code nesting**.

Next, since anchor elements are _what-you-want-to-selec_t, we’ll do just that:

![Image](https://cdn-media-1.freecodecamp.org/images/1*bxFbXy1QDeGf-84KSJNxDg.png)
_Fig. 5 — selecting just the anchor elements_

We’ve selected all the anchor element in each of the sections and numbered them consecutively left to right. And I mentioned, the order — left to right — is important.

This is where _what-you-want-to-select_ part ends and the filtering begins.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WwCVWx4UKJ5bdPUV1e4vXQ.png)
_Fig. 6 — Selecting only-of-type anchor elements._

_only-of type t_raverses each section and selects only those anchor elements that are the only anchor element in their respective section. Notice how sections 3, 4, and 5 are the only sections with anchor elements? As figure 6 shows, these are the ones that get selected and declared when a style gets applied.

### Pseudo-class #2 :first-of-type

Let’s fast forward to the part where we end selecting all the “_what-you-want-to-select_”s (anchor elements in our case).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bxFbXy1QDeGf-84KSJNxDg.png)
_Fig. 7 — Selecting just the anchor elements._

The filter _first-of-type_ translates to selecting in each of the sections only the first occurrence of the anchor element.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PJExtAelKm7-Xdt31Dw6cA.png)
_Fig. 8 — Selecting first-of-type anchor elements._

Here’s what the code that accomplishes this looks like:

```
a:first-of-type {   border: 2px solid black;}
```

In case you forgot the hard work I did for you setting up the CodePen, here’s the [link](http://codepen.io/nashvail/pen/VKkXLB) again to check out what the code renders in a browser.

### Pseudo-class #3 :last-of-type

If you can’t tell by the name, _last-of-type_ is the exact opposite of _first-of-type._ Which therefore means in each section of the tree, instead of selecting the first occurrence, select the last ones.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dWlzrEMXkZueTDY52sGLzg.png)
_Fig. 9 — :last-of-type selections_

“What about the sections with just one anchor element?”, not very glad you asked that question. It’s quite simple to see if a section has just one anchor element, it obviously passes the _only-of-type_ filter, but not only that. Since there are no anchor elements preceding or following that particular tag it passes both _first-of-type_ and _last-of-type_ filters as well (e.g _a_ tags Section 4 and 5).

### Pseudo-class #4 :nth-of-type(number/an + b/even/odd)

And now we finally bite into the juicy part of the article, there’s simple CSS with some fifth grade Math toppings, hope you enjoy savouring it.

Let’s declare the following style to begin with.

```
a:nth-of-type(1) {   border: 2px solid black;}
```

It looks a little cryptic but is quite simple really. To read the selector simply take the number from the parentheses and replace _nth_ in the selector name with that number’s **ordinal** form. That’s another fancy English word for you, to be honest though…

Alright coming back, _a:nth-of-type(1)_ can be therefore read as _a:first-of-type_ and no surprise it works exactly like _a:first-of-type_ and results in the elements getting selected as shown below; just the anchor elements which are first of their types in their respective section.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PJExtAelKm7-Xdt31Dw6cA.png)
_Fig. 10 — Do people even read these?_

Well that is fine and dandy, but let’s try something different here.

```
a:nth-of-type(0) {   border: 2px solid black;}
```

If you guessed it right, which I am sure you didn’t, no anchor elements get selected in this case. As the numbering of types (and children as we’ll see) in each section starts from 1 and not 0, there is no “0” anchor elements in any of the sections and therefore _a:zeroth-of-type_ selects nothing. And so will be the case for _a:nth-of-type(5)_ or _a:nth-of-type(6/7/8)_ because there are no _a:fifth-of-type_ or _a:sixth/seventh/eighth-of-type_ in any of the sections_._

But if we went ahead and used…

```
a:nth-of-type(2) {   border: 2px solid black;}
```

… quite clearly sections 1 and 2 have a _second-of-type_ anchor elements and hence those are the ones that get selected.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o7aTc-EJF53N7bAHs2Ssxg.png)
_Fig. 11 — :nth-of-type(2) or read as :second-of-type_

Similarly, just to reinforce the point here, if we went ahead and declared the following style,

```
a:nth-of-type(3) {   border: 2px solid black;}
```

it will select the third anchor elements in the second section as section 2is the only section with a :_third-of-type_ anchor element.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ob0gZ_tJhflq73RCzbyFkw.png)
_Fig. 12 — :nth-of-type(3) or read as :third-of-type_

Quite simple isn’t it? But numbers aren’t the only thing that you can pass into _:nth-of-type(…),_ this bloke is more powerful that that, you can also pass in formulas of form _(a*n) + b_ (or for brevity _an + b_)_._ Where _a_ and _b_ are constants and _n_ is a value >= 0. How did you like the Math topping sir? don’t worry it’ll all make sense in a second.

Consider the following style

```
a:nth-of-type(n) {  border: 2px solid black; }
```

The formula that’s passed in the selector above is _(1 * n) + 0 [= n]_ , _a_ is 1, b is 0 and _n_ is well, n. What happens next is, starting from 0 the numerical value of _n_ is incrementally plugged into the formula and selection is made. Therefore _a:nth-of-type(n)_ basically translates to

```
a:nth-of-type(0) {  border: 2px solid black; } // n = 0a:nth-of-type(1) {  border: 2px solid black; } // n = 1a:nth-of-type(2) {  border: 2px solid black; } // n = 2a:nth-of-type(3) {  border: 2px solid black; } // n = 3a:nth-of-type(4) {  border: 2px solid black; } // n = 4
```

```
...
```

Hence this results in all the anchor elements getting selected.

Let’s consider one more example

```
a:nth-of-type(2n + 1) {  border: 2px solid black; }
```

Starting from 0 and incrementally plugging values of _n_ in the formula generates the following selectors.

```
// n = 0 implies (2 * 0) + 1 = 1a:nth-of-type(1) { border: 2px solid black; }
```

```
// n = 1 implies (2 * 1) + 1 = 3a:nth-of-type(3) { border: 2px solid black; }
```

```
// n = 2 implies (2 * 2) + 1 = 5 - No selections since no fifth-of-type present in any of the sectionsa:nth-of-type(5) { border: 2px solid black; }...
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QrQj3hZlegF3D-kv7yB0gA.png)
_Fig 13 — nth-of-type(2n+1) selections_

Other than numbers and formulas that generate numbers_,_ you can pass in either _even_ or _odd_ strings_. even_ selects all the even occurrences of an element of particular type in a section i.e _:second-of-type_ _:fourth-of-type_ _:sixth-of-type_ e.t.c and on the other hand obviously _:nth-of-type(odd)_ selects all the odd occurrences i.e _:first-of-type, :third-of-type, :fifth-of-type_ e.t.c

### Pseudo-class #5 :nth-last-of-type(number/an + b/even/odd)

This selector functions exactly like the previous one, but with one little difference. See for yourself…

```
a:nth-last-of-type(1) {  border: 2px solid black; }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*8iEbmV82IuBJ7jyYiyx_AA.png)
_Fig. 14 — nth-last-of-type(1)_

Notice how in each level numbering of anchor types is done from right to left instead of normal left to right. That is the only difference. _last-of-type_ accepts numbers and formulas and even/odd just like _nth-of-type_ except when selection is made the last type is treated as first, second last as second, third last as third and so on…

With that we come to an end of *_-of-type_ selectors. Hope it was a fun ride for you, we started with _only-of-type_ then moved to _first-of-type_, _last-of-type_ and took a huge dip into _nth-of-type(…)_ and _nth-last-of-type(..)._ If in case somewhere in the middle you lost your grip and fell off I encourage you play around with this pen and re read the explanation.

Alright, time to hop on to the next one in this less visited corner of the CSS theme park. Another category of pseudo selectors/classes we’re going to delve into are *_-child_ classes. With a clear understanding of how *_-of-type_ selectors work grasping the concept behind *_-child_ selectors should be a cinch for you. “Cinch? What’s that? Is it a unit of measurement?” No ya dumbass, it means an extremely easy task. Anyways, let’s start with our very first _*-child selector,_ :_only-child_.

### Child pseudo-class #1 :only-child

Consider the following style.

```
a:only-child {   border: 2px solid black;}
```

Now that’s the very definition of self explanatory and straightforward. The selector says to select all the anchor elements, given that the anchor element should be the only child of its parent, or, to put in other words select all the anchor elements whose parent has just one child and that one child is an anchor element.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bNZeHcGUOqswsJDMQFszzw.png)
_Fig. 15 — a:only-child selections_

I had a friend who was never his mother’s favorite, and he was an only child. Just wanted to plug that in there, anyways, notice that in contrast with _*-of-type_ selectors we are no longer numbering types, but children, starting of course from 1 (and not 0). When compared with _only-of-type,_ the anchor element in section 3 is not selected as its parent (_ul_) has 3 children therefore even though it (the anchor element in level 3) is an _only child of type ‘a’_ of its parent, its not the only child, there are 2 _li_s as well.

### Child pseudo-class #2 :first-child

Consider the following style declaration.

```
a:first-child {   border: 2px solid black;}
```

It simply says, select all the anchor element, but with one condition in mind, the anchor element should be the first child of its parent. That’s it, no further explanation needed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qLx7ELzLcCUWHY9xakrsfg.png)
_Fig. 16 — a:first-child selections_

For if you are a little confused as of why the _a_ in section 1 wasn’t selected it’s because the first child in section 1 (whose parent is _body_) is _.main_, the first _a_ in section 1 is the second child and couldn’t pass the _first-child_ filter, that is the exact reason why the poor bloke ended up not being selected and was given a big hashtag fuck off. Let’s continue to the next one.

### Child pseudo-class #3 :last-child

This is the part where selectors should start to get self explanatory and you should start thinking I am dumb trying to explain them to you. [But my name is not blurryface and I don’t care what you think](http://genius.com/6273352). “Nice twenty one pilots reference there” yeah I know, thanks. Now, look at the following style declaration.

```
a:last-child {   border: 2px solid black;}
```

_what-you-want-to-select_ ? “Anchor elements.” And the _filter_ you want to use? _last-child._ That quite simply translates to select those anchor elements which are the last child of their parent. Or, in other words select anchor elements whose parent finally decided it wasn’t fun anymore and stopped after that bloke was born. Below is what the tree looks like with _:last-child_ selections.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PfU4UZ2kZvgWZlG-Pav05w.png)
_Fig. 16 — :last-child selections._

### Child pseudo-class #4 :nth-child(number/an+b/even/odd)

I hope you were able to digest the Math topping you got served last time, because it’s about to happen again only this time on a slightly different crust.

Now, I would like you to take all your attention and laser point it to the following example.

```
a:nth-child(1) {  border: 2px solid black; }
```

It’s all the same as _:nth-of-type,_ I would have linked to that section of the article here but Medium policies don’t allow that, if you want a refresher, you will have to scroll up to that section. Leaving Medium policies aside which might change in future, what hasn’t changed is the process of decrypting _nth-selectors ._

Just like with _:nth-of-type,_ in the selector name take the number in parentheses and replace “_nth”_ with that number’s ordinal form. Therefore the selector shown in example is equivalent to _a:first-child_ and works exactly the same; i.e selects all the anchor elements, given that they are the first child of their parent.

That should nail the similarity between the two _nth-selectors (nth-of-type_ and _nth-child),_ but we will anyways go ahead and take a look at another example.

```
a:nth-child(2n - 1) {  border: 2px solid black; }
```

We begin by incrementally plugging in values of _n_ starting from 0 into the formula, which makes us realize that the selector shown above is basically equivalent to the ones shown below.

```
// n = 0 implies (2 * 0) - 1 = 0 - 1 = -1a:nth-child(-1) { border: 2px solid black; }  | No selections
```

```
// n = 1 implies (2 * 1) - 1 = 2 - 1 = 1a:nth-child(1) { border: 2px solid black; }
```

```
// n = 2 implies (2 * 2) - 1 = 4 - 1 = 3a:nth-child(3) { border: 2px solid black; }
```

```
// n = 3 implies (2 * 3) - 1 = 6 - 1 = 5a:nth-child(5) { border: 2px solid black; } | No selections further...
```

As it is, if the selector gets numbers out of bounds (like -1, 5, 6… in the case above) fed into it, it just ignores them. Following is how the tree looks with _a:nth-child(2n-1)_ applied.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aXGTeApzv5e1c7CJdk-pvg.png)
_Fig. 17 — :nth-child(2n-1) selections._

Folks at CSS Tricks have a very informative article called [Useful :nth-child Recipes](https://css-tricks.com/useful-nth-child-recipies/) you should check it out and put your knowledge of :_nth-child_ to test_._ I challenge you m8.

With that we will move to the last selector of this article which punningly is _:nth-last-child._ Holy shit! why is “punningly” a word even?

### Child pseudo-class #5 :nth-last-child(number/an + b/even/odd)

This selector works exactly like _:nth-child_ except that it starts selecting elements from the opposite direction just like that annoying high school teacher who would ask questions to the class starting from the peaceful folks seated at the last benches. God I hated him. If you look at the trees drawn so far, the children are numbered left to right in each section, but this selector bloke sees the tree like so

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ChjMydCcmDb9TgFrY4htg.png)
_Fig. 18_

The children in each section are numbered right to left. So if we go ahead and apply the following style

```
a:nth-last-child(1) {  border: 2px solid black; }
```

the anchor elements will get selected as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XBmBun1e7jY0aaHsBlZHlg.png)

Quite straightforward isn’t it? This selector also very comfortably accepts formulas (of form an + b) and _even/odd_ strings, the selections though, are made from the opposite end.

OK, this is where our journey together ends. You can pay for your ticket by tweeting this article to your developer buddies.

I hope you enjoyed reading this and learned something new, including some shiny new English words.

This is Nash signing off. I’ll see you in the next article. Follow me on [Twitter](http://twitter.com/NashVail) to keep in touch. I tweet about dev-related stuff. A lot.

#### Looking for more? I publish regularly on my [blog at nashvail.me.](https://nashvail.me) See you there, have a good one!

![Image](https://cdn-media-1.freecodecamp.org/images/1*JZ2patu496gPkJOYXhb9MA.png)

