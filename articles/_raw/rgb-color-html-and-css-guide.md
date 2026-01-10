---
title: RGB Color – HTML and CSS Guide
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-19T19:00:35.000Z'
originalURL: https://freecodecamp.org/news/rgb-color-html-and-css-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/alice-dietrich-FwF_fKj5tBo-unsplash.jpg
tags:
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: 'Choosing the right color for your web design project is a serious endeavour.
  A color scheme can often make or break a site''s overall appearance.

  Different colors create a different feel for your designs. The right choice of colors
  can make your desig...'
---

Choosing the right color for your web design project is a serious endeavour. A color scheme can often make or break a site's overall appearance.

Different colors create a different feel for your designs. The right choice of colors can make your designs and creations look clean, aesthetically pleasing, and modern. But the wrong colors can make a project look garish, hard on the eyes, and can be difficult for users to interact with.

The color of the border (`border`), the background (`background-color`), or of the foreground (`color`) – the text and text decorations on the page – have a huge impact, so you should put in some effort to get them right.


![Image](https://www.freecodecamp.org/news/content/images/2021/07/rhondak-native-florida-folk-artist-_Yc7OtfFn-0-unsplash.jpg)
_Image from [Unsplash](https://unsplash.com/)_

CSS lets you use of a wide variety of different colors and color systems. They range from named colors, to hex colors, rgb() colors, hsl colors and more.

## How to Use Colors in HTML

The easiest way to apply color to your HTML elements is to write your HTML in a `.html` file. Then in that file you just link your `.css` stylesheet with all the colors and styles you specify. 

This makes your code easier to read and *sepates concerns*, which is considered a best practise.

We can have a file, `about.html`, with some HTML code like this: 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- link to our css styles -->
    <link rel="stylesheet" href="style.css">
    <title>About Me</title>
</head>
<body>
     <section class="intro">
     <h2>About Me</h2>
     </section>
</body>
</html>
```

Then in our `style.css` we can add the following:

```css

.intro {
 /* changes color of  background */
  background-color: rgb(232, 206, 191);
  max-width: 620px;
  height: 100px;
  padding: 5px;
  margin: 70px auto;
}

h2 {
/* changes color of text   */
  color: rgb(79, 72, 70);
  text-align:center;
}
```

These styles look something like this when we load them in the browser:

![Screenshot-2021-07-19-at-3.36.33-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-19-at-3.36.33-PM.png)

In this example, we used `rgb` color values to change the colors on the page.   

This article primarily covers the `rgb()` color model. It makes some comparisons with `named colors` and `hex colors`, weighing the pros and cons of each, and discusses some differences and similarities between these different color systems.

## What are Named Colors in CSS?

Named colors are English words, known as *keyword colors*. And they're pretty straightforward to use. 

In your CSS file, you declare the property you want to target and alter. You then use one of the set and specified color names.

```css

h2 {
    color: cyan;
    }
```

The code above will make every `h2` element in your HTML have a text color value of `cyan`.

There are approximately 140 named colors that modern browsers support. So your choices are relatively limited and there is not much variety available. 

With named colors, we are not able to harness the true power of CSS. So let's look at some other options.

## Numerically Named Color Systems

In this case, colors are described with a number system. This allows you to make the most of the whole spectrum of colors available. 

Most computer screens use a mix of red, green, and blue colors combined together.

Both `hex colors` and `rgb()` colors use a combination of red, green, and blue to create different hues. They work in the same way – the only differences are the numeric systems they use and their syntax.

So let's look at each system in a bit more depth.

## What are Hexadecimal Colors in CSS?

Computers count in the hexadecimal counting system compared to we humans who use the decimal counting system.

This system is comprised of alphanumeric values which include these characters : `0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f`.

A hex color starts with a `#` to denote that it is indeed a hex color and is then followed by `6` of the characters mentioned above. 

These numbers and letters represent the amount of `red, green, and blue` in the color.

Converting the keyword color, `cyan`, from earlier to it's equivalent hex color value would be:

```css

h2 {
    #00ffff;
    }
```

The first pair (`00`) represents the amount of red. The next pair (`ff`) represents the amount of green. And the last one (`ff`) represents the amount of blue.

The minimum value hex colors can use is `00` which is fully off, and the maxiumum value is `ff` which is fully on.

The color white in hex is `#FFFFFF` or `FFF` for its shorthand notation and the color black is `#000000` or `#000`.

## What is The RGB Color Model?

Generally, `hex` colors and `rgb` colors are identical – they just use a different numeric system and syntax (but the colors are exactly the same).

It really just comes down to personal preference which one you choose to use.

`RGB` is an acronym that stands for `Red Green Blue`.

Instead of using six hexadecimal characters like we did for the hex color values, with RGB each parameter pair defines the intensity and brightness of each color (red, green, and blue), with an integer number ranging from `0-255` or a percantage ranging from (0% - 100%).

It expresses colors in terms of the amount of red, green, and blue they are made up of and uses a human counting system in comparisson to hex colors that speak computer language.

The number is a code to represent how dark or bright the color is.

The minimum value of `0` represents that none of the color is being shown, so it is at its darkest. On the other hand, the maximum value of `255` represents that the full amount of color and the full intensity is on display.


### RGB Color Syntax

The general look of an `rgb` declaration is `rgb(red,green,blue);`

RGB has the following syntax:

* the keyword `rgb` followed by a set of parentheses `()`
* three numeric decimal values sepated by commas inside the parentheses (which represent the three colors), 
* and finally it ends with a semicolon.

Make sure you don't leave any spaces between anything.

Taking again the `cyan` example, the equivalent `rgb` code is:

```css

h2 {
    color:  rgb(0,255,255);
    }
```
 
The color red is not showing whereas green and blue are at their brightest and at their max. 

- White is `rgb(255,255,255)` 
- Black is `rgb(0,0,0)`
- Red is  `rgb(255,0,0)`
- Green is `rgb(0,255,0)`
- Blue is `rgb(0,0,255)`

### Lots of Options with RGB

With RGB, each value is mixed in with the rest and together they create a wide range of hues. You can even create new color combinations, making it the designer's dream. 

In the `rgb` color system, there are three values you can use, and each value can be one of 256 possible values.

That makes for 256 * 256 * 256 = 16,777,216 color options in total to choose from!

### RGB Opacity

By default all `rgb` colors are fully opaque.

We have the ability to make colors more transparent by changing the opacity with the `rgba()` selector.

The `rgb` part stays the same, but the fourth value, `a` ,stands for `alpha`. 

We can give `a` a number that is either `0` or `1` to describe how opaque we want our color to be. `0` is totally see-through and trasnparent and `1` is totally opaque.

We'll use the `cyan` example again, but this time we'll make it have half opacity.

```css

h2 {
    color:  rgba(0,255,255,0.5);
    }
```


In CSS there is also the `opacity` selector. 

We'll use the previous HTML and add the `opacity` selector to our `section` element with a class `.intro` in our CSS:

```css
.intro {
    background-color: rgb(232, 206, 191);
    max-width: 620px;
    height: 100px;
    padding: 5px;
    margin: 70px auto;
    opacity: 0.3;
    }
```

Notice that this makes the whole tag transparent, including the background, the heading, the heading's backgorund – everything.

![Screenshot-2021-07-19-at-4.21.54-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-19-at-4.21.54-PM.png)

The power of `rgba()` is that it allows us to make just the background see-through, for example, or we can make just the heading transparent. It will not affect the whole tag and all the content inside it.

Now if we remove the line from above and we update the `background-color` selector to ` background-color: rgb(232, 206, 191,0.3);`, we see that it doesn't affect the heading:

![Screenshot-2021-07-19-at-4.25.18-PM](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-19-at-4.25.18-PM.png)

## Conclusion

I hope this has given you a good overview of the RGB color model, its syntax, and how it works. We also briefly compared it to other color models in CSS.

I hope you found this of value and thank you for reading.

Happy coding!




