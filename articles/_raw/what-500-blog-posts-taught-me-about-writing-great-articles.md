---
title: What 500+ blog posts taught me about writing great articles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-31T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-500-blog-posts-taught-me-about-writing-great-articles
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/writing-technical-articles-banner.png
tags:
- name: Blogging
  slug: blogging
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
seo_title: null
seo_desc: "By Burke Holland\nI've written a lot of blog posts. Somewhere north of\
  \ 500 to be exact. All of them are technical. \nAbout two dozen of them are actually\
  \ good. \nThe rest are just a meandering hot mess of grammatical errors, code snippets\
  \ that don't wor..."
---

By Burke Holland

I've written a lot of blog posts. Somewhere north of 500 to be exact. All of them are technical. 

About two dozen of them are actually good. 

The rest are just a meandering hot mess of grammatical errors, code snippets that don't work and a never-ending misuse of "it's" vs "its". Why can't I get that right?! Its not that complicated.

BUT. I'm not here to talk about my failures. That's what therapy is for. I'm here to talk about the dozen or so roses that bloomed in a literary field of feces. These are the tips that you need to write the best technical articles.

### Write for the beginner  

To date, my most popular article on Medium (by views) is, "Here's how you can actually use Node environment variables".  

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-46.png)

When I was writing the post, I wondered if I was the last person alive who didn't fully understand environment variables. Clearly I'm not. The takeaway from this is that **if you think something is too simple to write about, you should probably write about it**.

Over-estimating the audience is the most common mistake you can make when writing technical articles. You don't need to dissect a compiler or invent a framework to have something to talk about. [Lea Verou](https://twitter.com/LeaVerou) did an entire talk on 1 CSS property. ONE. And it's one of the best presentations I have ever seen.

%[https://www.youtube.com/watch?v=b9HGzJIcfDE]

Pick simple topics and then dive into them. There are far more people interested in learning how to trim strings than there are people who are interested in having a structured argument on how to solve the [Dining Philosopher's problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem). 

Note that I'm judging the popularity of articles based on views. There's some conjecture about whether or not this is a good measure of success. After all, good clickbait will get you views. There are sites with an entire business model based on this, and we don't hold them in particularly high esteem. 

Another measurement we could look at is "Read Ratio". The above article has a "Read Ratio" of 25%. One quarter of the people who visited the article actually read it. The higher the percentage, the better. It turns out that the easiest way to increase that percentage is to just write shorter posts. Take a look... 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-47.png)

These are throw-away posts that are only 2 or 3 paragraphs long. Lazy writing. Me just throwing turds in the air so that I can say I wrote something that week. 

We seem to be in a culture that is obsessed with this target. Make shorter content! People will read it! Yeah, they'll read it, but kind of the same way they read road signs; flying down the 1 billion lane highway of the internet, stuffing their face with Combos and retaining virtually none of what they see.

Read % is not a good target. It encourages everyone to just throw turds, and what goes up, must come down.

A better measurement, I think, is the "Reads" metric. How many people actually read the article? Now we don't know how Medium calculates this, but [they attest](https://help.medium.com/hc/en-us/articles/215108608-Your-stats) that it's "how many viewers have read the entire story". By that metric, a new post emerges as the top dog.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-48.png)

"You should never ever run directly against Node in production. Maybe."

Which brings me to the second insight for writing successful technical articles...

### Question the status quo

While working on a demo with a friend, he mentioned to me in an off-handed way that you should never run directly against Node in production. Well I didn't know that. I had never heard that before. So I decided to research it to see if he was right. As it turns out, he was right. But he was also wrong. The answer, like everything in life, is, "it depends".

Programming ideology is littered with absolutes. Never use ternary statements. Never open a hyperlink in the same window. Never push to production on a Friday at 5 PM. Never build a website that doesn't work on mobile. Never do "Select *" from a database. Never force push into a Github repo. And never ever should you take any of those things at face value. 

Programming is black and white. Reality is not. The second that you hear someone make an absolute statement, that's a good time for a blog post. You may find that absolute is absolutely wrong. I once heard that you should never put JavaScript in HTML. Then some guy named [Jordan](https://twitter.com/jordwalke?lang=en) said, "yeah, but you can put HTML in JavaScript", and today we have [React](https://reactjs.org/).

Shake it up. Reader's want an original opinion and everyone likes a renegade.

The paradox of absolutes is that as much as people like you to question existing ones, they also like it when you make your own.

### Speak in absolutes

If we continue down the list of the most popular posts, we get to "The greatest Visual Studio Code setup in the world".

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-50.png)

This one has a far lower view count because it's posted in my personal publication. As a side note, don't try and create your own blog or publication. That's like trying to create your own magazine or TV channel. You can do it, but it's way easier to just go where the readers already are.

Also note that even though this article has far less views than the next highest one (41K vs 113K), it only has 4K less reads (24K vs 28K).

This article makes an outlandish allegation - that my personal VS Code setup is the best in the world. This is an extremely subjective claim, and likely not even close to being accurate. But it's great for a blog post because it makes the reader think, "Oh yeah!? I'll be the judge of that, buddy!". 

Anytime you make an absolute statement, you are inviting people to come and see if it can stand up under scrutiny. Developers really can't help themselves. Seeing if things stand up under scrutiny is kind of what we do.

Many of these people are going to disagree with you. That's OK. In fact, it's healthy. Let people like things, but also let them **not** like things. There are going to be people who don't like that I said to use absolutes. They are going to say that you should never use absolutes, which is itself an absolute statement. See? You can't win, so don't be afraid when at least half of your readers leave comments like this...

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-51.png)

Feel the burn. And its got 432 claps - by far the most of any comment on that article. That's fine. Let those people disagree or not like your writing style. You can please some of the people some of the time.

The only article that I've ever had go to #1 on Hacker News uses a similar strategy...

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-53.png)

Everything? It's ruined _everything?!_ Of course not. Every0ne knows that DC actually ruined everything when they made, "Aquaman". Now, see, you want to take issue with that statement. See how that works? 

The other thing that we can glean for the top three posts, is that they all cover pretty popular technologies - Node and VS Code. That's a trend that continues in the stats.

### Write about popular technologies

If I keep looking through the list, the next several posts are about either React, or VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-52.png)

Writing about popular technologies is gonna get you readers. This one is kind of a no-brainer, but it bears repeating: **writing about popular technologies is going to get you readers**. Writing about an obscure product or technology that nobody has heard of is gonna feel like you threw a party and nobody showed up. Not that that's ever happened to me. Twice.

For me, writing about whatever is "hot" always feels like dunking on a six foot goal. It's too easy and nobody is impressed when you topple your four year old's [Fisher- Price Grow-To-Basketball](https://www.amazon.com/Fisher-Price-L5807-Grow-to-Pro-Basketball/dp/B0063IKACQ) toy. But the fact remains that talking about subjects that people are interested in is simply better than talking about ones they aren't. That shouldn't be an earth shattering revelation.

The trick is to figure out how to use those things to leverage what you actually want to say in an article. 

For instance, I work on Azure at Microsoft. If I want to write an article about best practices for running Node apps on Azure, I could do it and then call it "Best practices for running Node on Azure". There is a name for an article like that. It's called, "documentation".

Instead, I wrote an article titled, "You should never ever run Node apps in production. Maybe." This article benefits **all** Node developers while still conveying the ideas for how to best run Node apps on Azure. Since I'm no longer scoped to just "Azure", I get to write to all Node devs and you don't have to be using Azure to benefit from the content.

### All click bait is not created equal

Good titles draw people in. They have to. The sheer volume of information that we consume daily requires you to say something to get people's attention. 

Unfortunately, people have abused this concept by optimizing for the "Views" or "Read Percentage" metric; putting turds behind a title designed just to get your click.

We call this, "Clickbait".

Clickbait is bad. It's bad because the title is salacious, but the content is weak. This is pure deception, and we hate it. Nobody likes being lied to. Thanks to people abusing titles for clicks, we've gotten to the point where any title which grabs your interest is considered "clickbait". Except it isn't.

Your content is only as good as the title that it sits behind. If the title doesn't get people to stop and take notice, it really doesn't matter how good your content is, does it? As long as you are putting substance in your content, don't be afraid to bravely draw people in with strong titles. Of all the titles I've come up with, here are some of my favorites...



* Oauth has ruined everything
* [Save 15% or more on car insurance by switching to plain JavaScript](https://css-tricks.com/save-15-car-insurance-switching-plain-javascript/)
* [How to increase your page size by 1500% with Vue and Webpack](https://css-tricks.com/how-to-increase-your-page-size-by-1500-with-webpack-and-vue/)
* [You should never ever run Node.js in production. Maybe.](https://medium.com/free-code-camp/you-should-never-ever-run-directly-against-node-js-in-production-maybe-7fdfaed51ec6)
* [The best CLI is the one you don't have to install](https://www.infoq.com/articles/azure-cloud-shell/)

So how do you write better headlines? In the first iteration of the freeCodeCamp style guide, Quincy recommended the [CoSchedule Headline Analyzer](https://coschedule.com/headline-analyzer) tool. I've used this site many many times. It helps you to write better titles by giving your headline a "score". 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-71.png)

This tool can be a little frustrating to use. It will tell you that you need more "common" words or "emotional" phrases, but it doesn't tell you what those things are. It's a bit of an exercise, but I've found the tool to be useful in so much as it forces me to create dozens of iterations of a title and I always end up with a better one than the one I started with.

For my last tip, I have no data. I have no charts to show you or stats to back me up. My last tip is just hard-learned from the trenches of life.

### Be vulnerable

The psychologist Robert Glover once said, "Human beings are attracted to each other's rough edges".

One of the most engaging things you can do for your reader is to simply be you. If you don't understand something, say so. If a concept is confusing, point that out. If you are afraid to write about something because you think you might be doing it wrong, write it. Your honesty is what ultimately makes a terrific blog post.

Put yourself out there. Show people how you solved a problem and ask them how they would do it. You are going to be wrong. All the time. That's life. And the thing is, people **love** that.

One of the first articles that I wrote for CSS Tricks was covering a pretty simple issue in React where I needed some content to be dynamically rendered. I was new to React, so I wasn't sure how everyone else was doing it.

So [I asked people](https://css-tricks.com/solve-rendering-puzzle-react/).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-72.png)

This article has more comments than any article I have ever written. It is not a long article. It does not provide any sort of revelation. It also exposes my naivety as a React developer. But more importantly, **it connects with people**. Why? Because everyone has things that they don't know that they think everyone else already knows. They are just waiting for someone to step out and say so. Once you do, they will too. 

Yes, you are going to get the "everyone knows this" comments. But that's false. Everyone doesn't know it. After all, you didn't know. And that voice in your head that tells you that you're the only one? That's your ego. In short, pride keeps you from being authentic, and that ultimately keeps you from connecting with your readers.

### The fine line between being interesting and being offensive

A word of caution: there is a fine line between writing interesting content and just being a jerk. It's quite easy to swing from being insightful into just being mean. I should know. I've done it.

If I say "OAuth has ruined everything", I am taking shots at the people who created that spec. There is a thinking, feeling human on the other end of every technology you use. In the case of OAuth, the creator himself had already made worse statements it, so I felt comfortable that I wasn't simply smearing his work in public. 

Even still, I took a big risk doing that. That's expected. You are going to have to assume some amount of risk to write great content, either because you are being vulnerable, because you are questioning the status quo, or because you are simply being honest. But you **don't** have to be a jerk. That part is optional and the internet is not exactly lacking in negative content.

### Write On

The most important thing of all is to just write. None of these tips are any good if you don't write anything. For a lot of people, that's the hardest part. Just know that the more you do it, the easier it gets. It's kind of like playing the guitar.

I'll leave you with this inspiration. This is Alexandr Misko. My guess is he didn't just pick up a guitar one day and play like this. It took a lot of practice. Writing is no different. If you do it enough, you might just become the Alexandr Misko of blogging.

%[https://www.youtube.com/watch?v=EMxiuq_tMq0]


