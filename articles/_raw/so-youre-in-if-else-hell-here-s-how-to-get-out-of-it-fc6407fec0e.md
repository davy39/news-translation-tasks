---
title: So you’re in if/else hell — here’s how to get out of it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-25T16:34:57.000Z'
originalURL: https://freecodecamp.org/news/so-youre-in-if-else-hell-here-s-how-to-get-out-of-it-fc6407fec0e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hEbJvltnslRrdEzjWQ7Img.jpeg
tags:
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@markusspiske?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Markus
  Spiske / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  What is ...'
---

By Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-245.png)
_Photo by [Unsplash](https://unsplash.com/@markusspiske?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Markus Spiske</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### What is this topic about?

If you are from a `javascript` background you might have heard the terms `callback hell` or `async/await hell`. It looks something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*13tInwUptNwGlHemJrxTig.png)
_The horror._

There is a similar situation with just using `if/else` as well. You might label this as developers being obsessive, or ignore it by thinking that this is kind of okay in some situations.

I beg to differ. As the saying goes…just pretend that whoever maintains your code next knows where you work and can come yell at you.

For the purpose of this article, I’ll demonstrate an example using ReactJS. The principle itself can be applied in Javascript or any language for that matter.

**Before we begin**, the `_<MyButton_` /> example may not be the best example to explain the if/else nested problem. But hopefully it’ll give you a good guideline as to what the problem is & how to avoid it.

Let’s paint a picture. You are given a button to implement in `React` & the button has 2 options for a theme, either `default` or `primary`. You think it’s simple & you write your `<MyButton` /> component:

```jsx
const MyButton = ({ theme, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = 'default-btn';
  } else if (theme === 'primary') {
    className = 'primary-btn';
  }
                   
  return (
    <button className={className}>{content}</button>
  );
}
```

Some time passes & another developer is given a task to add functionality for round corners for the button for both themes, default & primary. The developer who picks up the tasks is very big on using ternary operators. They end up doing something like below:

```jsx
const MyButton = ({ theme, rounded, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = rounded ? 'default-btn rounded' : 'default-btn';
  } else if (theme === 'primary') {
    className = rounded ? 'primary-btn rounded' : 'primary-btn';
  }
                   
  return (
    <button className={className}>{content}</button>
  );
}
```

Time passes & another developer is given a task to add a `hover` state for both the `default` & `primary` buttons. Now the other developer does not want to make changes in the already code implemented, fearing they might end up breaking something.

So they write a separate if statement:

```jsx
const MyButton = ({ theme, rounded, hover, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = rounded ? 'default-btn rounded' : 'default-btn';
  } else if (theme === 'primary') {
    className = rounded ? 'primary-btn rounded' : 'primary-btn';
  }
  
  if (hover) {
    className = className + ' hover';
  }
                   
  return (
    <button className={className}>{content}</button>
  );
}
```

So far so good …

#### This is where it gets interesting

Moving on, a final requirement comes in months later to add an animation when the user **hovers** over a button which has a **primary** theme & is of **rounded** type.

Now based on this requirement, the entire API structure changes the `<MyButto`n/> component. The developer working on the code ends up with logic like this:

```jsx
const MyButton = ({ theme, rounded, hover, animation, content }) => {
  let className = '';                
  if (theme === 'default') {
    className = rounded ? 'default-btn rounded' : 'default-btn';
    if (hover) {
      className = className + ' hover';
    }
  } else if (theme === 'primary') {
    if (rounded) {
      if (hover) {
        if (animation) {
           className = 'primary-btn rounded hover my-custom-animation';
        } else {
          className = 'primary-btn rounded hover';
        }
      } else {
        className = 'primary-btn rounded';
      }
    } else {
      if (hover) {
        className = 'primary-btn hover';
      } else {
        className = 'primary-btn';
      }
    }
  }

  return (
    <button className={className}>{content}</button>
  );
}
```

That got out of hand way too quickly …. didn’t it?

![Image](https://cdn-media-1.freecodecamp.org/images/1*XwM0kI6bX9utPF0VwT20Gg.gif)
_and you think to yourself, there was nothing you could have done :(_

In order to make this code simpler, we need to understand all the possible states that this code has. I have made a possibility chart of all the possible combinations at a certain time for the button.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mnWn59gP2Lwb7f3huo783A.png)
_All the possible combinations of values that &lt;MyButton /&gt; component can have at a time_

If this seems a bit complicated, you can try looking at this next chart for your understanding.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H5yLaIar39mkoVbzwJlLlQ.png)
_This is the same as the previous one, the FALSE values are omitted here for simplicity sake_

**The key thing when writing code is understanding the data flow of your code. Once you have a complete understanding of it, everything becomes simpler.**

#### Solution

Based on the above given criteria, I can write my code like this to simplify it.

```jsx
const MyButton = ({ theme, rounded, hover, animation, content }) => {
  const isThemeDefault = theme === 'default'
  const isThemePrimary = theme === 'primary';
  const isRounded = rounded === true;
  const isHover = hover === true;
  const isAnimated = animation === true;
  
  const isPrimaryAnimated = isThemePrimary && isAnimated;
  
  let className = isThemePrimary ? 'primary-btn' : 'default-btn';

  if (isRounded) {
    className = `${className} rounded`;
  }
  if (isHover) {
    className = `${className} hover`;
  }
  if (isPrimaryAnimated) {
    className = `${className} animated`;
  }
 
  return (
    <button className={className}>{content}</button>
  );
}
```

This code is now way more readable. Any developer who works on this code can easily extend its functionality & get on with their life, knowing that they have done a wonderful job with the code.

You can try playing with the code if you want, to see if it matches all the use cases.

%[https://codesandbox.io/s/0pl6xvqrnw?from-embed]

With the automata (finite state machines)-like coding approach:

* Code is more readable now
* Code is more maintainable

Feel free to share your thoughts. Thank you for reading.

You can also reach me out on twitter [**@adeelibr**](https://twitter.com/adeelibr)

> Reference & Inspiration: [Stack Exchange Forum](https://softwareengineering.stackexchange.com/questions/205803/how-to-tackle-a-branched-arrow-head-anti-pattern)

