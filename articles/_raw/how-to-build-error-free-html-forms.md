---
title: How to Build Error-Free HTML Forms
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2023-07-17T18:47:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-error-free-html-forms
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/FCC-Blog-Cover-4.png
tags:
- name: error
  slug: error
- name: forms
  slug: forms
- name: HTML
  slug: html
seo_title: null
seo_desc: "After taking some coding courses, I decided that it was time to put my\
  \ knowledge to good use and do a coding project. \nLike most newbies, I went to\
  \ Google to find some inspiration. As I scrolled through the internet, I stumbled\
  \ upon Skillcrush’s list..."
---

After taking some coding courses, I decided that it was time to put my knowledge to good use and do a coding project. 

Like most newbies, I went to Google to find some inspiration. As I scrolled through the internet, I stumbled upon [Skillcrush’s list of HTML and CSS projects for beginners](https://skillcrush.com/blog/html-css-projects/). 

Number 5 piqued my interest, so I googled some images on how HTML forms should look. I thought “Oh I can do this. This looks easy!” But this project turned out to be a bit harder than I thought. 

In this article, I will show you three things I have learned in surviving, I mean making HTML forms error-free. Let’s get started! 😀

## Tip #1: Make Sure the Labels and Inputs Match.

When I first started creating HTML forms, I would often use the following methods for creating email input fields:

```html
<label id="text"> Your Email</label>
<input type="text" id="text" name="text"> 
```

I would often use `text` as the label and id's attribute because I thought it was the correct method. 

This all changed when I started using [WAVE’s accessibility checker](https://wave.webaim.org/extension/) to learn how to make my code more accessible. When I ran my form through the checker, it pointed out that the email input did not have a properly associated label, and that can cause screen readers to have difficulty presenting it to users with disabilities.

So, I googled a few sources and found [”HTML Inputs and Labels: A Love Story” by Amber Wilson](https://css-tricks.com/html-inputs-and-labels-a-love-story/). Through reading this article, I learned that it’s best to use specific names in the `id` attribute. 

With a new feeling of confidence, I started using this approach. Here’s an example:

%[https://codepen.io/CB_ID2/pen/MWPPmBG]

In the code snippet above, I used `email` as the label and input’s `id` attribute. When I ran it through the accessibility checker, there were no red Xs.  

While this victory was sweet, I wanted to learn more ways to ensure that labels and inputs were accessible. So I went to Google and found this [HTML Forms attributes article](https://www.w3schools.com/html/html_forms_attributes.asp). Through reading, I learned that you can add other attributes like `placeholder`, which demonstrates how the user should present their contact information.  

Through these experiences, I realized that creating harmonious labels and inputs for a form is like constructing a sandwich. You want to make sure that your flavors work well together and use the best features of your oven (or whatever appliance you use) to make your sandwich nice and toasty. 

Now before we start getting hungry, let’s move on to my next tip. :) 

## **Tip #2:  Be More Semantic When Creating a Button**

Formatting your form’s buttons is crucial to the efficiency of your HTML form. Buttons are the main way that your user’s information is sent to your desired destination. 

When I first started creating HTML forms, I used to create buttons like this:

```html
<input type="submit">
```

Like the labels and inputs, I would get a red x on WAVE’s accessibility checker. In the results, it mentioned that a `value` attribute was missing, which makes it difficult for the screen reader to detect the button. 

With that in mind, I decided to do what most beginners do when creating this feature: 

```html
<button> Submit</button>
```

When I ran the code in the WAVE accessibility checker again, it passed a few tests. But something inside me told me that my previous solution was ok too and that I just needed to find a way to add a `value` attribute to it.  

With a new thirst for knowledge, I went to Google and found this [article on how to create accessible form components](https://www.w3.org/WAI/tutorials/forms/labels/#labeling-buttons). In the section about buttons, they recommend using the following methods to make this element semantic:   

```html
<input type="Submit" value="Submit">
<button type="Submit">Submit</button>
```

When I ran the first snippet into the accessibility checker, I received no red Xs. The same result occurred when I ran the second code snippet through the accessibility checker.  

At first, I didn't know which one to pick because both approaches made the form accessible. But something inside me told to go with what I truly wanted. So, I took a deep breath and chose the following code line:

%[https://codepen.io/CB_ID2/pen/Rwedeme]

I decided to go with the second code snippet because it's more explicitly labeled, which makes it easier for screen readers to scan. It's also easier to remember, and is the method that I often use for creating buttons. 

Think of it as deciding to go with the brand of bread you’ve always used for your sandwiches instead of picking a different one. As cliché as this saying sounds, sometimes simplicity is best.  

Before you start getting hungry again, there is just one more suggestion for making your HTML forms error-free.

## **Tip #3:  Pick the Best CSS Framework Based on Your Needs**

When I first started creating the style for my forms, I used to force myself to use CSS frameworks like Flexbox. At the time, my feelings of imposter syndrome were at an all-time high due to seeing other people creating great forms with those frameworks. I felt that if I started using them too, I would get those same designs. 

At first, I was happy with using Flexbox as it made things like centering content easier as shown in the snippet below:

%[https://codepen.io/CB_ID2/pen/mdzoQrg]

Unfortunately, I still wasn't satisfied in the end. I found that the design did not come to fruition as I envisioned.  

To combat this feeling, I went to Google to find something to help me solve my dilemma. When I was about to give up, I stumbled upon the article, [“How to style forms with CSS: A beginner’s guide” by Supun Kavinda](https://blog.logrocket.com/how-to-style-forms-with-css-a-beginners-guide/).

My heart leaped with joy when it pointed out that you can use vanilla CSS to create beautiful designs. For example, to make the texts’ input fields look more presentable, I could do this:

```css
input[type=text]{
padding: 10px;
} 
```

With newfound confidence, I gave vanilla CSS another chance, and I can honestly say I was so happy with this decision. Here’s the final result:

%[https://codepen.io/CB_ID2/pen/NWOOQXQ]

I wanted to keep my design simple, so I used basic elements like `text-align`  property to center my form's content. 

If I had to pick something that exemplifies this experience, it would be like a sandwich cut into two triangle slices. Simple yet effective.  

Overall, sometimes, it’s best to go back to the basics before moving on to something more challenging. 

## **Conclusion**

There it is folks, my three tips on how to make your HTML forms error-free. 

I know creating HTML forms can be frightening in the beginning. But with these tips, confidence, and some imagination, you can HTML forms that wow your viewers. Now go forth and be great! :)   


  

