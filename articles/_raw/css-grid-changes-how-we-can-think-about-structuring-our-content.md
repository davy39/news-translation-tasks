---
title: How CSS Grid Changes the Way We Think About Structuring Our Content
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-27T15:56:00.000Z'
originalURL: https://freecodecamp.org/news/css-grid-changes-how-we-can-think-about-structuring-our-content
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/marmoset-1567019547013.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: grid layout
  slug: grid-layout
- name: HTML
  slug: html
seo_title: null
seo_desc: 'By Kevin Powell

  CSS Grid changes how we can think about document structures

  Anyone who has even dabbled a little in creating websites knows that <div>s are
  an essential building block for controlling our layouts.

  HTML5 introduced new semantic element...'
---

By Kevin Powell

# CSS Grid changes how we can think about document structures

Anyone who has even dabbled a little in creating websites knows that `<div>`s are an essential building block for controlling our layouts.

HTML5 introduced new semantic elements to help, and while they are a fantastic addition to the language, they’re a little bit like the garnish on our `<div>` soup.

![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566407449963_div-soup.jpg)

With grid, we no longer have to rely on `<div>`s to create the structure of our page, or even a more complex component. The structure is literally defined by the parent and not how the content is organized within in.

This means we can have nice, simple markup that sticks to the content itself without a reliance on organizing it through the use of `<div>`s. 

## Grid might be complicated, but so is flexbox

  
I’ve heard a lot of people complain that grid is too complicated and that flexbox gets the job done. **I’d argue that they are comfortable with flexbox and don’t want to bother learning grid because of that**.

At the end of the day, Grid does introduce a boatload of new properties and values, so yes, there is a learning curve. But flexbox is plenty complicated as well. 

Can you tell me the benefits of flex-basis over setting a width? Or really, how flexbox calculates the widths of flex items if we haven’t explicitly set them? 

For example, if you showed the below example to someone who had never used flexbox, how do you explain the fact that it’s the same markup and the same CSS for both sets of columns? To make it even worse the second column in both has a width: 50%. Clearly that width of 50% isn’t really setting it to 50%.

%[https://codepen.io/kevinpowell/pen/WNeRbjg]

“Well, it starts off with flex items shrinking if there isn’t enough room, so even though we set the width to 50%, it doesn’t have the space, so it shrinks down to squeeze in because the other div requires more space. The 50% is more of its ideal size than what it will actually be. 

“So in the top example, the first div’s content being so long is causing a problem because, as a flex item, by default, it wants to shrink to fit its content. In this case that item has a lot of content so…”

**So yes, flexbox is awesome and does a great job at creating layouts, but please don’t tell me that it’s simple**. As soon as you get out of perfect examples, it’s often far from intuitive and sometimes it can be downright strange.

Grid is complicated in that there are _a lot_ of new properties and values, but they gives us a lot more control than flexbox does. 

In this article I’d like to look at how that extra layer of control helps simplify our markup and let us write less code, and that’s without even learning how to use a bunch of its fancy features.

## The limitations of flexbox

  
Even if we take a simple component and build it with flexbox, because it only acts in 1-dimension at a time (the flex items are either rows or columns, they cannot be both), we’re left with a lot of divs to break things up into rows, which can then be split into columns.

For example, if we’re working on a card that looks like this:  


![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566998781330_Screen+Shot+2019-08-28+at+9.26.01+AM.png)

  
It’s not a complicated layout but we still need to organize our content in a pretty specific way to get it to work.  


![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566999564535_flex-overlay.jpg)

The yellow and orange boxes there are needed, so that when we place a display: flex; on the .card itself (the red box), it will create two columns. So to structure everything, we get markup that looks something like this:

```html
<div class="card">  
    <div class="profile-sidebar">
        <!-- profile image and social list here --> 
    </div>
    <div class="profile-body">
        <!-- name, position, description here -->
    </div>
</div>
```

It’s not overly complicated by any means, and once you understand how flexbox works, it relatively straight forward.

When we put a `display: flex` on the `.card`, we'll get our two columns, and then we need to go into those and start styling them up. 

Here is a working example with all the styling on it:

%[https://codepen.io/kevinpowell/pen/rNBjaqV]

The thing is, **by having to create columns of content, we’re getting a little more complicated in the markup, and we’re also limiting ourselves** as we’ve forced different pieces of content to be grouped together.

## Simplifying everything with CSS Grid

  
Because grid is 2-dimensional, meaning that it allows us to create rows _and_ columns at the same time, that means that our grid container (where we declare display: grid) has full control over the layout inside of it. 

We used to _require_ <div>s to do that, like in the above example with flexbox. With grid, we can remove the <div> s completely.

```html
<div class="card"> <img src="https://i.pravatar.cc/125?image=3" alt="" class="profile-img">
  <ul class="social-list"> ... </ul>
  <h2 class="profile-name">Ramsey Harper</h2>
  <p class="profile-position">Graphic Designer</p>
  <p class="profile-info">Lorem ipsum ...</p>
</div>
```

From a markup point-of-view, doesn’t this make a lot more sense?

We have a `.card` and then we place the content of that component in there. We don’t need to worry about breaking down how it will be structured, we just place the content that we need and move on from there.

### Structuring the layout

Just like when we used flexbox for this, we still need to break the layout down, though because of how grid works, it looks a little different. 

This is one place where people might argue grid is more complicated, but really I'm just drawing boxes around each peices of content, and then extending those lines.  


![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1566999543180_grid-overlay.jpg)

  
With flexbox, we created two divs that would act as our columns. When using grid, we instead set up the entire grid on the parent itself, and then we can tell the children where they belong on that grid.

To set up the grid, we can do something like this:

```css
.card {  
    display: grid;
    grid-template-columns: 1fr 3fr;
}
```

The `fr` unit is unique to grid, and is a fraction of the available space. Using it like this is very much like setting the two columns up in flexbox and giving them widths of `25%` and `75%` respectively. 

### Placing the items on the grid

Maybe it’s because I used floats to create layouts for years, but it always feels like a little bit of magic when the different elements just end up where we want them to be! 

We could use `grid-row` and `grid-column` on each element to place it where we want, but the more and more I use grid, the more I fall in love with taking the time to set up `grid-template-areas` and place my items into those areas. 

The setup is a little bit longer, but the payoff really hits home when we make things responsive (we’ll get there soon).

So first, on the `.card` we need to setup the `grid-template-areas` and then we can assign all the children onto those areas:

```css
.card {
  ...
  display: grid;
  grid-template-columns: 1fr 3fr;
  grid-column-gap: 2em;
  grid-template-areas:
      "image name"
      "image position"
      "social description";
}


.profile-name     { grid-area: name; }
.profile-position { grid-area: position; }
.profile-info     { grid-area: description; }
.profile-img      { grid-area: image; }
.social-list      { grid-area: social; }
```

  
Check it out here if you’d like to see it all in action:

%[https://codepen.io/kevinpowell/pen/wvwdVyJ]

## It’s so straight forward

One of the things I love about using `grid-template-areas` are that it’s _so_ easy for someone else to look at this code and immediately understand what is going on.

If someone shows you something that’s been setup using `grid-row` and `grid-column` using the numbers and spans, it’s easy enough to count things and figure out where they’ll end up. For simple layouts or for a quick span 3 here and there I think it’s fine to use them, **but it’s so nice to look at _only_ the CSS of a parent element and immediately understand what that entire layout is going to look like**.

### It’s easier to know the actual size of an element when using grid

In that very first example where we set the width of one of the flex items to 50%, it wasn’t really 50%. If you understand why that is, that’s great, but it can still be annoying at times. It’s easy enough to get around, but when using grid, it’s _much_ less of an issue.

Because we are defining the complete layout, we’re also defining exactly how much space we want items to take up. 

And sure, we get `minmax()` and `fr` which muddy the water a little as they allow for more flexible sizing (like we are using in our above example), but even then, we still have full control over that flexibity, and it’s all being controlled by the parent rather than having to set some things on the parent and others on the children.

## Limited changes

  
Looking at our above example, we can’t change that layout to look like this without changing the markup:

![Image](https://paper-attachments.dropbox.com/s_81FBDAACE1729CFAB134F728BBD90343A8252037DFE26F8EB672CB6AB63DDAD8_1567000172227_Screen+Shot+2019-08-28+at+9.49.09+AM.png)

We’ve constrained ourselves because of how we had to group things together in `<div>`s. We had to use those `<div>`s in order to get the layout to work, but we’re stuck now. 

**With the flat markup of our grid, anything is possible**! And as an added bonus, because we set everything up using grid-template-areas, making these changes is super easy!

```css
.card {
  /* old layout 
  grid-template-areas:
      "image name"
      "image position"
      "social description"; */
   
  /* updated layout */
  grid-template-areas:
      "image name"
      "image position"
      "image social"
      ". description";
}
```

By playing with the `grid-template-areas` like this, it shifts the social icons to where we want them to be so quickly and easily (the `.` in the last part indicates and empty cell).

## This makes life so easy when dealing with media queries

As I mentioned a few times now, one of the places where this pays off. We can completely control our layout with with our parent:

```css
.card {
  /* setup for small screens */
  display: grid;
  grid-template-columns: 1fr;
  grid-column-gap: 2em;
  grid-template-areas: 
      "name" 
      "image" 
      "social" 
      "position" 
      "description";
}
.profile-name     {  grid-area: name;}
.profile-position {  grid-area: position; }
.profile-info     {  grid-area: description; }
.profile-img      {  grid-area: image; }
.social-list      {  grid-area: social; } 


/* rearanging the layout for large screens */

@media (min-width: 600px) {
  .card {
    text-align: left;
    grid-template-columns: 1fr 3fr;
    grid-template-areas: 
        "image name" 
        "image position" 
        "social description";
  }
  .profile-name::after {
    margin-left: 0;
  }
}

```

The below pen has the entire thing styled up. Dive in there, play with the grid-areas, and see how easy it is to completely change the layout!

%[https://codepen.io/kevinpowell/pen/BaBRXvZ]

## Flexbox still has its place

  
I do find myself turning to grid more and more, but I do think that flexbox still has its place. If I have a logo and navigation next to one another, it’s nice to simply do something like this and know that they are where I want them to be:  
`.header {  display: flex;  justify-content: space-between;}`

The same for the `<ul>` we use for a navigation to simply get the items next to one another, or as you might have noticed in the card example we were looking at, it’s perfect for the `.social-list`.

For simple components where we don’t need a more complex layout, it works really well. But I find myself moving more and more toward grid, sometimes because of really needing it, other times because I want to use `minmax()` or use `fr` units.

But at the end of the day, I think the best thing about the grid is how we can simplify our markup so much. 

We still need to use the humble `<div>`, but thanks to grid, we don’t have to rely on filling up our markup with them anymore.

## Conclusion

As great as flexbox is, it’s not simpler than grid. It does certain things really well, but grid allows us, when working on more complex layouts, to have much more control. That control is amplified when dealing with responsive design when making changes in media queries. 

With flexbox, our one big change is changing the flex-direction. With grid, we can completely redesign a component quickly and easily.

There is a lot more to both flexbox and grid. Each one has its purpose, but if you feel like you’re not sure which one to pick, or if you’re struggling to figure out responsive design in general, I’ve recently released a course that dives into responsive design over on Scrimba called **[The Responsive Web Design Bootcamp](https://scrimba.com/g/gresponsive)**. 

It includes a deep dive into both Grid and Flexbox, as well as a full module devoted to how to start thinking responsively as well. In all, it has over 170 lessons, with 15+ hours of content, organized across 6 modules. So if you’d like to keep diving into the responsive world of CSS, you can [check it out here](https://scrimba.com/g/gresponsive).

