---
title: These common mistakes will lead to immortal bugs. Learn how to avoid them.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T23:25:53.000Z'
originalURL: https://freecodecamp.org/news/these-common-mistakes-will-lead-to-immortal-bugs-learn-how-to-avoid-them-eee79ee43cd5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*_tDOnN79K8WqoVD0
tags:
- name: bugs
  slug: bugs
- name: Life Lesson
  slug: life-lesson
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
- name: WeChat
  slug: wechat
seo_title: null
seo_desc: 'By David Yu

  Didn’t we already fix that?

  The question that you or your teammate would ask after the product manager posts
  a snapshot of the bug.

  This whole event feels like a Deja Vu. You try to retrace the time you fixed that
  bug in the commits, but ...'
---

By David Yu

**_Didn’t we already fix that?_**

The question that you or your teammate would ask after the product manager posts a snapshot of the bug.

This whole event feels like a Deja Vu. You try to retrace the time you fixed that bug in the commits, but what’s the point?

The reality is if you don’t get to the root cause of the bug, it will come back like the Hydra of Lerna.

![Image](https://cdn-media-1.freecodecamp.org/images/m8XUwZGMf2YTjk5zY2UhvOKC8qrJ2D5JEkIA)
_Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Hercules_and_the_Hydra_of_Lerna-_Hercules_grasps_his_club_with_both_hands_and_confronts_the_seven-headed_hydra,_from_the_series_%27The_Labors_of_Hercules%27_MET_DP832529.jpg" rel="noopener" target="_blank" title=")_

Here are some patterns that lead to immortal bugs.

### Hardcoding a value

When we’re doing front-end development, we often use dummy data to build out the user interface quickly. That’s fine.

The problem is having dummy data at multiple locations. Then it’s easy to forget one or two when you push your code.

Here are some tips:

* Use a single variable for your dummy data and share it across different components
* Write a comment like `// TODO: remove later` to allow easy search later
* Don’t rely on backend data to always be the same

```
// ? 
```

```
<img src={require(`./assets/${backendData.fileName}.png`)} />
```

```
// This will break if fileName is an unexpected string
```

```
// ? 
```

```
let img;
```

```
try {
```

```
  img = require(`./assets/${backendData.fileName}.png`)
```

```
} catch(e) {  // Catch error if file doesn't exist
```

```
}<img src={img} />
```

```
// ? 
```

```
<img src={backendData.imgUrl} />
```

### Let’s Refactor Later

Your codebase will only grow larger and larger as you work on it. Your client or your boss won’t know the negative effect of not refactoring the code, because everything looks fine on the surface.

Plus, it’s always more satisfying to write something new and show it to other people. “Hey, check out what it can do now.”

So how do we know when to refactor the code?

According to [Refactor Guru](http://2018-10-28	14:00	21:00	2018-10	¥300.00	7:00:00	-¥2,100.00	David	Front-End	Bug fixes: speaker/headphone control. Countdown timer based on start_time plus duration. Update call status from in_progress to ended), follow the Rule of Three

1. When you are doing something for the first time, just get it done.
2. When you are doing something similar for the second time, cringe at having to repeat but do the same thing anyway.
3. When you are doing something for the third time, start refactoring.

### Keep everything in one file

This goes along with code refactor. When the project is fresh, it’s difficult to predict how large a feature will become.

In the past, I had a file that grew into thousands of lines of code. Refactoring that code is like performing surgery, delicate, but rewarding at the end.

Most people have a principle of how their project is structured. Separation of files by pages, features, dev. or production, private or public method, MVC model, etc.

How to structure a project folder is a large discussion by itself. I will save that for another article.

### Don’t write specs for API

“Wait, why don’t the pictures show up anymore?” the product manager asks the front-end developers.

“Wait, why doesn’t the data have the picture_url anymore?” The front-end developer checks the console for network response.

“Oh yea, now the pictures come in three sizes. large_pic_url, med_pic_url, small_pic_url.” The back-end developer heard the discussion and jumped in.

Sounds familiar?

Everyone is trying to do their job. But synergy won’t happen in the silo. It’s everyone’s job to communicate what’s needed.

Here are some simple solutions to start.

* Before building an API, start with a JSON file of the data that both front-end and back-end developers have access to.
* When the API is completed, generate the document with [https://github.com/apidoc/apidoc](https://github.com/apidoc/apidoc)
* Notify of breaking changes before deployment

There are more sophisticated approaches to writing specs and handling documentation. And I would love to hear about what approach your team uses in the comment section.

### Merge code without reading conflicts

Breaking things is less of a worry since you can always revert back to the previous commit.

It’s your or your teammate’s code disappearing during the process that’s the problem.

This often happens when you want to “save time” and move forward.

When in doubt, get in contact with the developer who made the commit that conflicts with yours.

When you mess up, `git merge --abort` or `git-reset --hard`.

When it breaks beyond repair, remove the project and clone it again.

Think twice when doing `git push -f`.

### Fix a reusable component without testing

Reusable components are the magical trick up every developer’s sleeve. Like when the client pitches you the wireframe that contains the same date picker across several pages.

In your mind, you think, “I am going to make an awesome date picker component. Write less code. Do more.”

A few months later, the client says, “I want the date picker in this page to explode with fireworks and on other pages, different kittens to represent months”. Now you need the date picker to be more dynamic than it was.

Then after you make the changes, you discover that fireworks are coming out of the kittens.

If you are on a larger team, you can defer quality assurance to a different team.

But if there is no such functionality in your organization, you will have to do a global search for your component’s name to see what your component affects.

Make a note to yourself of those files. Test those file visually and functionally depending on what they do.

### Anytime you say, “It’s fine for now”

You know you will have to go back to it later. The key is “don’t forget”

When you decide between speed of development and stability of the software, we must be careful not to always put speed as a top priority. It’s similar to driving a car without ever checking the condition of the car.

You can decide a ratio between speed and quality assurance. Maybe it’s two speedy iterations and one quality assurance iteration, whichever makes sense for your team.

### Conclusion

* Avoid hardcoding a value if you can. If you have to, leave a note for yourself.
* Refactor when you’re doing the same thing for the third time.
* Split code and refactor often
* Front-end and back-end engineers must work together to agree on the data being passed around.
* If merge conflicts does not make sense to you, double check with the person who wrote the commit.
* When making changes to a reusable component, test for the location(s) where it’s being used.
* Find a healthy balance between speed and quality for your team.

### While we’re here…

If you want to reach the 1 billion users of WeChat, you have to understand it first. Here’s a [**free glossary**](https://pages.convertkit.com/b2469604dd/0c671fdd2d) to get started.

