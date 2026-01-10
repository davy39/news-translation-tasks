---
title: How to Use Mixins in Sass and Pass Arguments – With Code Examples
subtitle: ''
author: Nazanin Ashrafi
co_authors: []
series: null
date: '2021-12-02T18:45:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-arguments-to-mixins
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/sass-mixins.jpg
tags:
- name: Sass
  slug: sass
seo_title: null
seo_desc: 'Mixins are my favorite thing about Sass. They made my life so much easier,
  so I wanted to show you how they can do the same for you.

  Mixins can be a bit tricky to understand at first, but don''t worry. You''ll get
  the hang of it by practicing and will ...'
---

Mixins are my favorite thing about Sass. They made my life so much easier, so I wanted to show you how they can do the same for you.

Mixins can be a bit tricky to understand at first, but don't worry. You'll get the hang of it by practicing and will fall in love with mixins like I have.

Before I get started, let me show you what you will read in this article:

* What mixins are
    
* How to write mixins and include them in your code
    
* How and when to pass arguments
    

Now let's get to the point, shall we?

## What Are Mixins in Sass?

First, let's take a quick look at what a mixin is:

> "[Mixins](https://sass-lang.com/documentation/at-rules/mixin) allow you to define styles that can be re-used throughout your stylesheet. They make it easy to avoid using non-semantic classes like `.float-left`, and to distribute collections of styles in libraries." – Sass Docs

To put it simply, a mixin is a code block which allows you to write your styles in it and use it throughout the whole project. You can also think of it as a *reusable* component. It also helps you to write cleaner code without having to repeat yourself.

## How to Write a Mixin

This is how you write a mixin in Sass:

```scss
@mixin name {
    properties;
}
```

And here's how to include it in your code:

```scss
div {
    @include name;
}
```

Here's an example of using a mixin in your code:

```scss
@mixin circle {
    width: 200px;
    height: 200px;
    background: red;
    border-radius: 50%;
}

div {
   @include circle;
}
```

Now let's see what's happening in the above code:

1. First we define a mixin using the `@mixin` at-rule.
    
2. Then we give it a name – choose whatever you think will fit what you're gonna be using it for.
    
3. Add your CSS properties.
    
4. By simply using `@include` you pass it to the mixin block.
    

## Mixin Example

Now let's look at an example of a mixin in action.

Here's how to create a pink circle with a mixin:

```scss
@mixin circle {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: #ea0185 ;
}
```

```html
.circle {
    @include circle;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-18-19-27-24--1-.png align="left")

Now you might ask *"why should I use a mixin to create a pink circle? I could just give my element a class and style it."*

Mixins are reusable, remember? We use them when we know we'll be repeating ourselves a lot. So the whole point is to *avoid* repetition and keep the code clean.

## Passing Arguments

Now that we've seen how to write a mixin, let's move on to the next section. I want to divide this section into smaller parts:

* What are mixin arguments?
    
* When to pass arguments?
    
* How to pass arguments? + Examples.
    

### What Are Mixin Arguments?

An argument is the name of a variable which is separated by a comma.

### When Should You Pass Arguments to a Mixin?

I'll start this section with an example:

What if you were to create two different circles? Like a green circle and a pink circle?

You could create two separate mixins, one for the green one and one for the pink one:

```scss
// a mixin for the green circle
@mixin green-circle {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: green;
}

// and another mixin for the pink circle
@mixin pink-circle {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: pink;
}
```

But this isn't great because you're repeating your code. And we should stick to the DRY (Don't Repeat Yourself) principle, remember?

And that's where mixin arguments come in.

In a regular mixin (and by regular I mean a mixin when no argument is passed) you define some certain styles. But an argument allows you to define different styles by turning them into variables. It's like customizing each style for each element. Let's move on to the next section and see some examples.

### How to Pass Arguments to Mixins

We've seen what an argument is and when to use it. And now it's time to see how to pass the arguments:

```scss
@mixin name($argument,$argument) {
    property: $argument;
    property: $argument;

}
```

Here's an example:

```scss
@mixin circle2 ($width,$height,$color) {
    width: $width;
    height: $height;
    background: $color;
}
```

You can think of arguments as customizable variables that you can use in different situations to create different things without repeating yourself.

Like when you pass `$width` to the width property, you can define it in different situations. Maybe you need the width to be 50px in one place and 500px somewhere else.

Does that make sense? Let me break it down for you with another example.

Okay, back to our circles.

I want to make one big red circle and one small green circle (two different things) with just one mixin.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-22-21-25-44--1-.png align="left")

Now what properties do I need to make a circle?

```python
width, height and background-color, right?
```

Since we're building circles, the border-radius will be 50% in both situations. So I will leave it alone and won't pass any argument to it.

Now we're down to 3 properties:

1. width
    
2. height
    
3. background-color
    

That means we only need 3 arguments:

```scss
@mixin circle($width,$height,$color) {
    // We passed $width to the width property
    width: $width;
    
    // We passed $height to the height property
    height: $height;
    
    // And we passed $color to width background-color
    background: $color;
    
    // no argument for this property, beacuase it's gonna be the
    // same in both circles
    border-radius: 50%;
}
```

So now let's see how we can pass arguments to our mixin:

#### For the big red circle

```scss
.circle-red {

    // circle ($width,$height,$color);
   @include circle (350px,350px,red);
}
```

#### For the small green circle

```scss
.circle-green {

     // circle ($width,$height,$color);
    @include circle (200px,200px,green);
}
```

And here's the result:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-22-21-25-44--1--1.png align="left")

If you want some more info about passing arguments to mixins, here's a little video to help you out:

%[https://www.youtube.com/watch?v=0s-xjyXOtP4] 

Alright, back to our tutorial. As I said earlier, I didn't pass any arguments to the border-radius property because it's always gonna be 50% (in *this* case).

But if I were to make one square and one circle, then I would need to pass an argument to `border-radius` too:

```scss
@mixin circle($width,$height,$color,$radius) {
    width: $width;
    height: $height;
    background: $color;
    // passed argument to border-radius to have control over it 
    border-radius: $radius;
}

.square {
            // ($width,$height,$color,$radius)
    @include circle (350px,350px,red, 10px);
}

.circle {
            // ($width,$height,$color,$radius)
    @include circle (200px,200px,green, 50%);
}
```

Now we have a big red square and a small green circle:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-22-22-17-12--1-.png align="left")

Let's take a look at another example. This time let's try using a mixin on some text.

This is what I want to make, a green text with black background and red text with a transparent background:

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-from-2021-11-25-19-26-49--1-.png align="left")

First I created two h2 elements:

```html
<h2 class="text1">Text</h2>
<h2 class="text2">Text</h2>
```

We need `font-size, color, and background` properties here. Now I should pass arguments by turning them into variables.

```scss
@mixin text($font-size,$color,$bg-color) {

     // we pass the $font-size to font-size property
    font-size: $font-size;
    
    // we pass the $color to color property
    color: $color;
    
    // we pass the $bg-color to background property
    background: $bg-color;
}



.text1 {
          // ($font-size,$color,$bg-color)
    @include text(3rem,green , black)
}

.text2 {
          // ($font-size,$color,$bg-color)
    @include text(5em,red , transparent)
}
```

And there you have it.

**Quick tip:** Remember that *the order of arguments matters.*

It matters because the only way to know what value you meant to pass for each parameter is by using the correct order.

For example, if your arguments order is *$width, $height, $color*, passing them should be in order as well:

```scss
@mixin circle($width,$height,$color) {
    width: $width;
    height: $height;
    background: $color;
    border-radius: 50%;

}
```

```scss
.circle-red {
             // ($width,$height,$color)
    @include circle (350px,350px,red);
}
```

You can't pass color first followed by the width and height:

```python
.circle-red {
    @include circle (red,350px,350px);
}
```

Regarding this wrong order, we passed `$width` to width property, therefore the first value needs to be a number. So if you pass `$color` first, the value won't be recognized. That's why we have to pass arguments in order.

## Here's a quick review of what we've talked about in this article

* Mixins are reusable code blocks.
    
* We use them when we know we'll be repeating pieces of code a lot.
    
* This is how to we write a mixin:
    

```scss
@mixin name {
    properties;
}
```

* An argument is a name of a variable which is separated by a comma.
    
* Arguments allow you to define different styles.
    
* The order of arguments matters.
    
* This is how we pass arguments:
    

```scss
@mixin name($argument,$argument) {
    property: $argument;
    property: $argument;

}
```

And that's a wrap for this article – I hope you liked it and found it useful. 😊

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-113.png align="left")

*You can also connect with me on* [***twitter-***](https://twitter.com/nazanin_ashrafi)
