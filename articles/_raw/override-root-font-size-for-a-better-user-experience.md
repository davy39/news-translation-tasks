---
title: How to Override Root Font Size to Create a Better User Experience
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-23T15:14:55.000Z'
originalURL: https://freecodecamp.org/news/override-root-font-size-for-a-better-user-experience
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/root-font-size-article-image.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: user experience
  slug: user-experience
- name: ux design
  slug: ux-design
seo_title: null
seo_desc: "By Damla Erkiner\nBack in the day, web developers, front-end engineers,\
  \ and UI designers had a bit of an easier job. This is because they weren't expected\
  \ to rearrange their code and designs to fit so many different screen sizes. \n\
  But in today's world..."
---

By Damla Erkiner

Back in the day, web developers, front-end engineers, and UI designers had a bit of an easier job. This is because they weren't expected to rearrange their code and designs to fit so many different screen sizes. 

But in today's world, if you make a decision that doesn't take responsive design techniques into consideration it can be doomed to failure. 

After all, no one wants to visit a web site to stare at weird shapes, distorted images, and illegible text. 

People's time is precious and limited, particularly in today's fast-paced world. A poor user experience in the form of non-responsive web design can really harm a business or brand in the blink of an eye. 

This is why every developer should treat their products and websites like gemstones in their portfolio. These are literally a part of your personal brand and you don't want to ruin it with bad designs.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/responsive-webdesign-vs-non-responsive-webdesign.png)
_[Illustration by Forty One](https://www.fortyone.io/en/responsive-webdesign.html)_

If you want to guarantee a hassle-free user experience, as a web developer or designer you're supposed to adopt certain practices that require you to play around with the layout. In this way, every single page you compose looks sophisticated and is user-friendly regardless of the screen size. 

This process of creating responsive designs is deeply connected to [content architecture](https://www.madcapsoftware.com/blog/content-architecture-what-it-is-and-why-its-important/#:~:text=What%20is%20Content%20Architecture%3F,can%20affect%20the%20content%20architecture.). 

There are various techniques you can use to make your website's potential users smile – or at least not feel frustrated – when they look at their screens. 

Those may involve using media queries, CSS Flexbox, or CSS Grid. That being said, this article will primarily consider a method that is popular among experienced web developers. 

## Why Should You Adjust the Root Font Size?

In a nutshell, this technique targets the root font-size and it also has to do with why you choose 'rem' units with this set-up. If you're already curious about it, let's dive right into it.

First and foremost, you should know that the standard root font-size of browsers is 16px. This fixed value is in 'px' units by default. But 'rem' units compared to 'px' are capable of creating more responsive websites. You can read more about that in [this article](https://www.aleksandrhovhannisyan.com/blog/use-rems-for-font-size/). 

So if we try to convert px values into rem, we'll need to do some math. Suppose we want to set the font-size of an element to 4px, but we also want it to be as responsive as possible. To turn it into a 'rem' value, we need to divide it into 16px and the result will be 0.25rem. [An online converter](https://nekocalc.com/px-to-rem-converter) exists for this purpose as well.

Everything would be fine and dandy if we had a way to turn every 'px' value into a 'rem' figure more easily, now that rem is considered to be more responsive. Here is how our dreams can come true.

In lieu of dealing with such cumbersome calculations, we can set the root (HTML) font-size to 62.5%. In this case, you can make all the other calculations automatically through the system. 

## How to Change Root Font Size

Let's delve into the details to better grasp the situation. When the root font/HTML size is 100%, the font-size is 16px by default. But, if you set it to 62.5%, the new root value will be 10px. 

Now, 10px (1rem) is way too tiny and is a recipe for disaster in terms of good user experience. So we should set it to 1.6rem (16x) again in the body. Everything looks the same on the surface. But still, this time, the new rem set-up will be more responsive than that of the 'px' version.

Now we're able to translate all the values into rem units. The tricky bit here is the root size calculation in the HTML section. Now, whatever size we pick for the body will be re-shaped in accordance with the pre-defined value in the root/HTML. To put it simply, the new percentage value '62.5%' in the root/html section ensures the smooth transformation of 'px' into 'rem'.

## Why We Prefer the 'Percentage' Expression

At this point, you might be asking yourself why we opt for the percentage expression (62.5%) along with 'rem' units. Why bother? Isn't the 'px' version supposed to be the same? Well, not so much. 

As [some developers on Quora](https://www.quora.com/Why-is-the-CSS-technique-html-font-size-62-5-used-to-set-the-base-font-size-to-10px-Why-not-just-simply-say-html-font-size-10px) suggest, percentage-based values can scale more smoothly compared to fixed numbers. This means that not only are rem units important, but also the percentage preference in the root/HTML part matters a lot in this particular set-up.

The most effective part regarding the figure '62.5%' in the root is that even if the visitor alters the font size of the browser, they'll be able to view the page properly thanks to the related CSS set-up. 

Also, it poses no threats in terms of accessibility because we also set the font-size of the body as 1.6rem in addition to the 62.5% arrangement in the root/HTML section. This way, we ensure that those two numbers go hand in hand no matter what the screen size is.

## Why Accessibility is Important

It's important to elaborate on the accessibility issue. I believe it should be of the utmost importance to web developers and designers from all walks of life.

[Research](https://websitesetup.org/websites-for-visually-impaired/) shows that the number of visually impaired individuals is gradually on the rise, and there are many reasons for this. But one thing is for sure: in an era of cutting-edge technological advancements, everyone should be able to enjoy the internet and access information through certain accessibility measures. And applying proper responsive design techniques is definitely one of those. 

## What is Bruce Lawson's Significant Message?

I remember watching [an excellent talk by Bruce Lawson](https://www.youtube.com/watch?v=tgXbbOirY8o), an expert when it comes to web standards. During a virtual free bootcamp organised by [Class Central](https://www.classcentral.com/) and freeCodeCamp last year, he was a guest speaker. He explained very clearly why we as web developers are responsible for keeping everyone included and making sure that no one else is left out when coding and/or designing a website.

%[https://www.youtube.com/watch?v=tgXbbOirY8o]

## Shall We Test Our New Set-up?

Let's be more specific and come up with an imaginary scenario. Suppose a visually-impaired user wants to visit the webpage you've designed. To be able to see everything more clearly, they decide to make some adjustments t0 the browser's font-size in advance. For example they might set it to 18px, a bit bigger than the standard size (16px). 

It is now time to examine the following code snippet closely to witness the functionality of the HTML and body-oriented set-up from the perspective of this individual.

```css
html {
    font-size: 62.5%;
}
body {
    font-size: 1.6rem;
}
```

As the developer of this webpage, you chose '62.5%' for the HTML and '1.6rem' for the body as the initial font size. But remember that the browser's font-size determined by the above user is now 18px, not 16px anymore. How is it going to work out? Will this person be upset and leave the page feeling frustrated or will they keep surfing the webpage without trouble?

Here's the answer. Once the browser's font-size is chosen as 18px by the user, the font-size will instantly be re-calculated as 11.25px (18px * 62.5%) by the system. As a result, the value for the body will be 18px (1.6rem * 11.25px) just the way it is requested by that specific user. So this person will not be negatively affected by the situation just because they wish to see the font-size bigger than the standard version. 

The good news is that all of these will be re-calculated automatically. And thanks to the percentage and rem-oriented set-up, the text on the webpage will be more responsive and user-friendly. 

## More Experiments 

To further see the possible effects of this setup, let's now take a look at how the font-sizes of the following elements/main containers will work out for our user.

```css
html {
    font-size: 62.5%;
}
body {
    font-size: 1.6rem;
}
header {
    font-size: 3rem;
}
section {
    font-size: 2.5rem;
}
footer {
    font-size: 2.8rem;
}
```

In line with the new HTML size (62.5% * 18px = 11.25px), the re-calculated value of the header element's font-size will be 33.75px (3rem * 11.25px ). The one for the section element will roughly be 28px (2.5rem * 11.25px). And finally, the font-size of the footer will be 31.5px (11.25px * 2.8rem) from the perspective of our imaginary user. 

In other words, with the new arrangement involving the font-size of the HTML and body, everything else will be handled smoothly under the hood without you as the developer having to perform separate calculations for every single element.

## Is This Method Bullet-Proof?

Despite the fact that the method that uses the root size '62.5%', since it's specifically a percentage value and the rem-based preference in the body section gives us a chance to play around with the general font-size dynamically, it is also not risk-free and you should use it cautiously (see [this article](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/) for more info). 

For instance, it may lead to [some problems](https://css-tricks.com/forums/topic/62-5-font-size/) when 'em' values are preferred instead of 'rem' values. Plus, this technique only resizes text. So you'll need to use some other tricks (for example, when dealing with the size of the images). 

That said, overriding the root font-size is still a widespread practice preferred by [many developers](https://www.aleksandrhovhannisyan.com/blog/62-5-percent-font-size-trick/) around the world and it can be handy if used carefully. 

## Wrapping Up

All in all, the concepts of accessibility, responsive web design, maintainable and scalable code, and web performance are fundamental in creating a solid user experience. 

Perhaps in the future, someone will come up with a better way to handle this. I just wanted to share with you the pros and cons of adjusting the root font size. 

Even if you are not planning to use it at all, one of your teammates might go for it. So it is always a good idea to be aware of the arguments for and against it.

Thank you for reading. If you've liked this article, one of the best ways to support me is to share it. Should you have any questions or comments, you can always contact me via [LinkedIn](https://www.linkedin.com/in/damla-erkiner-000b76227/). I'll be more than happy to help you out with your queries.

Happy coding!

**“Knowledge is power.” – Francis Bacon**






