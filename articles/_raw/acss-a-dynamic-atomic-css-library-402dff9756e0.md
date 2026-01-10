---
title: How to write better CSS in teams with ACSS — A dynamic Atomic CSS library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T15:37:06.000Z'
originalURL: https://freecodecamp.org/news/acss-a-dynamic-atomic-css-library-402dff9756e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LJj4hmOES-c0DYj4Kwg89A.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: UI
  slug: ui
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By kushagra gour

  Writing good Cascading Style Sheets (CSS) is difficult and it becomes more difficult
  in a team where multiple developers write CSS.

  Through this article, I attempt to introduce you to an approach to writing (or not
  writing…we’ll see)...'
---

By kushagra gour

Writing good Cascading Style Sheets (CSS) is difficult and it becomes more difficult in a team where multiple developers write CSS.

Through this article, I attempt to introduce you to an approach to writing (or not writing…we’ll see) CSS. This approach solves almost all the issues one faces today with poorly written CSS in teams.

But first, let me set down some base conditions on which my article holds true.

#### A few conditions this article assumes:

1. You are working in a team where multiple developers write CSS.
2. Guidelines are hard to enforce unless there are automated tools.
3. Designers are free birds. Redesigns happen.

Under these conditions, **I am going to present a silver bullet solution that solves almost all the problems we face due to bad CSS** (Remember, CSS isn’t bad. Badly written CSS is). Let’s go through those problems to start with.

> **Disclaimer**: I am not, in any way, an affiliate of the solution described in this article. I am just a developer who has felt the pain of bad CSS in a team and wants to share with fellow developers, my thoughts on how to overcome that. This article may sound promotional, but it is just because I am very excited to bring this forth everyone.

### Problem #1: Naming classes is difficult

**_Developer 1 (while coding)_**_: Looks like a header to me, let me use `.header`selector for it._

**_Developer 2 (in the pull request)_**_:_ T_his isn’t a header. It looks like a title to me. Moreover, we cannot call it just ‘header’ as that element isn’t generic enough. Let’s call it `.panel-header` or better `.panel-title` ._

Coming up with names and that are also meaningful names is the most difficult problem to solve. It is also the most difficult apsect to learn because you cannot have guidelines for what is a “meaningful” name. You can only give examples of what is not meaningful, and that can only help so far. Additionally, it’s not just about ‘being meaningful’. Classes in CSS also need to ensure they don’t conflict with other class names in future as a new developer may use the same or similar name for his class.

#### **Solutions available:**

* [**BEM**](https://en.bem.info/methodology/) **—** naming conventions like BEM exist to solve this problem to some extent. But in the end it’s a guideline (we all know how easy it is to follow guidelines). BEM might prevent you from going completely ad-hoc but you still need to come up with an initial class name for your components.
* **Atomic classes** — another common approach these days to go completely atomic with atomic classes. Small classes that do just one thing. Eg. [Tachyons](http://tachyons.io/). Mix and match them to get what you need. This is a good step towards “skipping naming” altogether, but what if in future there exists no class for a particular thing? How do I customize existing atomic classes according to my design? Do all classes always load on my page whether or not I use them? We need something more.

### Problem #2: Selector strengths

Another thing CSS developers need to be constantly aware of is that the specificity in their CSS doesn’t go haywire. If you have long complex selectors, your CSS becomes unpredictable and difficult to maintain and debug.Harry Roberts has written a lot of articles on [why that is bad](https://csswizardry.com/2014/10/the-specificity-graph/) and [what you can do to fix that](https://csswizardry.com/2014/07/hacks-for-dealing-with-specificity/).

#### **Solutions available:**

The best solution to this problem is to simply restrict your selectors to one class. No chaining, no nesting, no IDs. The above mentioned BEM naming and atomic classes both result in single class selectors in your CSS and hence help in solving this issue.

### Problem #3: What about unused CSS?

CSS is render blocking, hence its very important to load only the critical CSS of a page synchronously and the rest, asynchronously. For the same reason, it also becomes important to prevent your CSS from creating bloat by stripping unused CSS.

#### **Solutions available:**

[Many](https://github.com/purifycss/purifycss) [tools](https://github.com/giakki/uncss) boast of extracting out used CSS of a page. But with single page apps coming in, this has become more difficult than ever. I am not sure how reliable or efficient they are, but that still needs an extra post-processing over your CSS.

### Problem #4: Refactoring

**_Developer 1_**_: This CSS has become quite messy. I think we should refactor it._

**_Developer 2_**_: Do you think this selector you are modifying might also be getting used on page X? Did you check?_

**_Developer 1_**_: Oh damn! You are correct…I missed that. That page X is too critical to touch. Do you know why that developer used the same class on both pages?_

**_Developer 2_**_: No idea. He left the company. Let’s just leave the CSS as it is :(_

I have nothing more to say here. That dialogue explains it all.

If I am to summarize above problems, I would say that writing good (scalable, readable, maintainable) CSS is definitely possible. However, doing so in a huge team is extremely difficult. Even if you try to make it right in a team, it would require a constant effort of someone to enforce all the best practices.

> In a team, the most non-obvious but perfect solution would be — to stop writing CSS!

“Wait, what are you saying? That’s not possible!”. You might be thinking so, but let me introduce you to something.

### The all-in-one solution — ACSS (Atomizer)

[**ACSS**](https://acss.io/) (derived from Atomic CSS) is a component-based framework for styling through atomic classes developed at Yahoo! And [**Atomizer**](https://github.com/acss-io/atomizer) is a tool that actually facilitates that. I’ll explain more. But before that, let me show you how you do styling in ACSS.

> To follow along with the code samples in this article, I suggest you [**install Web Maker**](https://webmakerapp.com/) (a front-end playground that supports writing ACSS without any build setup) on Chrome browser.

Now say you have a button that needs to be styled with usual padding, background, color etc properties. This is how it would look like in ACSS:

```
<button class="Bgc(blue) C(white) P(10px) D(ib) Cur(p) Bgc(red):h"> I am a button</button>
```

**One suggestion — make no judgment by the first look at this syntax.** Keep reading, give it time, discuss, and then decide. The classes on the `button` tag might look different but you would agree they are guessable to a large extent about what they do. It’s a button with _blue_ `**b**ack**g**round-**c**olor` , _white_`**c**olor` , _10px_ `**p**adding` , _inline-block_ `**d**isplay` , _pointer_ `**cur**sor` and changed to _red_`background-color` on hover.

If you have installed [Web Maker](https://webmakerapp.com) already, open it by clicking the Web Maker icon in your Chrome browser’s top-right side. Paste the above HTML in the HTML code pane and select **Atomic CSS** as the mode in CSS code pane. As soon as you do this, you’ll see some automatic CSS generated in the CSS code pane, like so:

![Image](https://cdn-media-1.freecodecamp.org/images/ofvqCkgGZfOvyZSKW80YnZViuXAr9DRH4rzw)

The CSS you see is generated by the _Atomizer_ tool I mentioned above. Basically, it reads HTML (or any file), detects ACSS classes from them and generates CSS for those detected classes. So you write just HTML with appropriate classes you want to use and CSS is auto-generated!

Now that we know how you do styling in ACSS, let’s see how it’s the best CSS methodology your team can have.

#### Inline, but not inline ?

As you can see we are always writing classes inline on the tags. That is what I meant by inline styling. But please don’t confuse it with [**the “inline styles”**](https://www.codecademy.com/articles/html-inline-styles)**.**Unlike inline styles, our inline classes translate to actual CSS classes in a cachable stylesheet. So basically we are getting the same power as inline styles (writing things quickly) but still get completely valid atomic CSS as output.

#### No more naming! ?

My absolute favorite advantage. You’ll never ever have to think a nice, semantic, and non-conflicting name for a class.

A very famous saying goes:

> There are only two hard things in Computer Science: cache invalidation and naming things. — **Phil Karlton**

#### Super easy updates and refactoring

Go to the HTML and change classes to update some styling. Remove any class from anywhere without the fear of breaking anything elsewhere.

#### Not a byte of unused CSS ?

Since Atomizer generates CSS from the classes you have actually used, you never have unused CSS in your stylesheet. Isn’t that the crazy performance we have all been looking for? There is also a tool where you can check how much a website can benefit from ACSS — [https://atomize-io.herokuapp.com/](https://atomize-io.herokuapp.com/)

#### No guidelines for new developers ?

All you need to give a new developer as part of your CSS onboarding is a [syntax guide for ACSS](https://acss.io/guides/syntax.html) and a class reference link — [https://acss.io/reference](https://acss.io/reference). This is a page where you can easily search the ACSS class for any property:value. Even this convention embeds in your memory as you keep using it.

Also, there is a nifty little [Visual Code extension](https://marketplace.visualstudio.com/items?itemName=pankaj-parashar.atomizer) by [Pankaj Parashar](https://twitter.com/pankajparashar) that auto-suggests these classes right in the editor. So even the reference isn’t required with that extension. Developer onboarding is done!

Apart from these advantages, there are several more goodies that ACSS comes with.

* We generally keep using same old property/value pairs across an app. Thus the [**generated stylesheet essentially stops growing after a certain point**](https://medium.com/@johnpolacek/by-the-numbers-a-year-and-half-with-atomic-css-39d75b1263b4). Because each unique property/value pair comes once in the final stylesheet.
* Because of the above point, you could actually use the **same stylesheet across your suite of multiple products** as it would never be so big. Same cached CSS stylesheet for all products!
* Pull request that feels like a dream. **Imagine pull requests where you don’t see any .css files. No more checking classes for meaningfulness or specificity conflicts**. Because you know correct atomic CSS, which should be present, would be generated. Won’t that be a wonderland?

### Myth busting

Lots of myths have developed regarding ACSS across the Internet. This is because of shallow evaluation of the framework and judgment at first sight.

#### It’s same as inline styling. It’s bad!

No, it’s not. We have already seen above. It’s definitely as powerful as inline styling but inherits no cons from it.

#### It’s hard to write all those same set of classes over and over.

Yes, it is. ACSS says it’s a component based framework. If you are not templating each of your components and are already duplicating HTML, say to create a button every time, ACSS isn’t for you.

For example you should be creating buttons using an abstracted button component like so:

```
<MyButton primary>Hello World</MyButton>
```

which should get compiled into something like:

```
<button type="button" class="D(ib) P(20px) Cur(p) Bgc(blue) Bgc(red):h">Hello World</button>
```

#### The classes make no sense at all

I agree they are different and might look repulsive at first sight. But every atomic class framework comes with its own convention of naming things. And trust me, ACSS has the best of the naming convention. [Read more about why they chose such naming](https://github.com/thierryk/ACSS-QA/blob/master/why-atomizer-did-not-use-more-readable-class-names.md).

I would like to quote a paragraph from one of [Harry Robert’s article](https://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/):

> A common argument against BEM is that it’s ugly; I dare say that if you shy away from code based _purely_ on its looks then you’re often missing the point. Unless the code becomes unnecessarily difficult to maintain, or genuinely more difficult to read, then perhaps you _do_ need to think twice before using it, but if it ‘just looks odd’ but has a valid purpose, then it should definitely be fully considered before writing it off. — **Harry Roberts**

But here we are, using BEM to make our code bases sane.

#### I won’t be able to do X thing in ACSS

You’ll be amazed to see [what all is possible](https://github.com/thierryk/ACSS-QA/) by mere classes provided in ACSS. Pseudo-elements, flexbox, media queries, you name it. And the convention they came up with to do all these things is simply brilliant! Though there might be certain things not possible yet in ACSS, like CSS Grids, you can always [open an issue or contribute to Atomizer](https://github.com/acss-io/atomizer/issues).

### In the end

I would request you give ACSS a try if you understand the pain of writing and managing CSS in a team. And remember, using ACSS doesn’t mean you cannot write plain CSS. Tools should be used where they work best. If there is something you feel plain CSS would be more appropriate for, you should definitely use it.

Also, ACSS isn’t alone taking this approach. There are similar alternatives like [Blowdry CSS](http://blowdrycss.readthedocs.io/en/latest/), [Cell CSS](http://cellcss.com/) etc, each bringing their own style of achieving the same thing.

If you have any questions regarding ACSS, you can ping [Thierry Koblentz](https://twitter.com/thierrykoblentz), the man himself from ACSS team, on [Twitter](https://twitter.com/thierrykoblentz). [Ask a question at the FAQ compilation](https://github.com/thierryk/ACSS-QA/) he maintains or [join the Atomizer group on Gitter](https://gitter.im/acss-io/atomizer). Or put in the comments of this article.

Finally, I would like to thank [Thierry Koblentz](https://twitter.com/thierrykoblentz) and [Jitendra Vyas](https://twitter.com/jitendravyas) for reviewing this article.

If you like this article, show your love by clapping?? on the article. Also fo[llow me on Twitter,](https://twitter.com/intent/follow?screen_name=chinchang457) where I share more front-end articles and side-projects of mine.

### More to read

* [https://www.smashingmagazine.com/2013/10/challenging-css-best-practices-atomic-approach/](https://www.smashingmagazine.com/2013/10/challenging-css-best-practices-atomic-approach/) — by Thierry Koblentz
* Atomizer GitHub repo — [https://github.com/acss-io/atomizer](https://github.com/acss-io/atomizer)
* ACSS documentation — [https://acss.io/quick-start.html](https://acss.io/quick-start.html)
* ACSS FAQs compiled by Thierry — [https://github.com/thierryk/ACSS-QA](https://github.com/thierryk/ACSS-QA)
* ACSS playground — [https://webmakerapp.com](https://webmakerapp.com)

