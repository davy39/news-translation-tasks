---
title: How to make the impossible possible in CSS with a little creativity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T16:19:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-the-impossible-possible-in-css-with-a-little-creativity-bd96bb42b29d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xPfQM8antkW3PhlH
tags:
- name: creativity
  slug: creativity
- name: CSS
  slug: css
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Facundo Corradini

  If you ever used CSS sibling selectors, you know there’s only two. The + sibling
  combinator selects the first match that comes immediately after, and the ~ subsequent-sibling
  combinator matches all the ones that come after.But th...'
---

By Facundo Corradini

If you ever used [CSS sibling selectors,](https://www.w3.org/TR/selectors-3/#adjacent-sibling-combinators) you know there’s only two. The `+` sibling combinator selects the first match that comes immediately after, and the `~` subsequent-sibling combinator matches all the ones that come after.  
But there’s no way to select what came before. Either parent selectors or previous siblings selectors are simply not a thing.

I know you want it, you know I want it, but the harsh truth is that they don’t exist (and probably never will). There are a million posts about the whys. There are even proposals on how to implement them. But we are stuck in the unidirectional processing of CSS rules, most likely to protect us from our “lack of expertise” getting us stuck in re-flows and even infinite loops.

Luckily, as with most CSS limitations, **we can fake it**.

The first thing to consider is why we want previous siblings to begin with.   
Two cases come to mind:

1. We need to select all siblings of a certain element, and the `~` subsequent sibling combinator is only selecting the ones that come after.
2. We need to select only siblings that came before

### 1. Selecting all siblings

Sometimes we need to select both previous and next siblings. To do that, we can actually select the parent and use some tricks around it.

For instance, to select all spans in the following structure when we hover any of them, we could just use the child selector on the parent’s hover. We make sure to disable the `pointer-events` from the parent and reset it back on the children. So whatever action we want to happen will only fire when we enter the child and not the parent itself.

If you need to select all siblings _except_ the one being hovered, you can combine the previous technique with the `:not` selector to exclude it.

A typical use case for this is menus:

The code above will turn down the opacity of all `<`li> ele**ment**s but the one being hovered.

Furthermore, you could use filters such as type and nth selectors to be extra precise on the siblings that you want to affect.

With some styling, it should work like this:

**Please note**: If you’re gonna run the `pointer-events:none` approach, bear in mind it can mess with stacking (might allow you to select elements that are “below” in the stacking order). It also won’t work in IE10 and below, apart from the implication that you might need the pointer events for something else. So be extra careful when using it.

### 2. Selecting what came before

For this use case, we can reverse the order on the HTML, then sort it back in CSS, and use the `~` subsequent sibling combinator or `+` adjacent sibling selector. This way we’ll be selecting the next siblings, but it’ll look like we are selecting previous ones.

There are multiple ways to do this. The simplest and probably oldest is changing the writing direction of our container:

If your elements need to display actual text, you can always reverse it back:

But that can get out of hand in many ways. Luckily the modern CSS toolbox makes it much simpler and safer. We can just use Flexbox on the container and reverse the order with `flex-direction:row-reverse`:

The best thing about the Flexbox approach is that we don’t mess with the writing direction. We don’t need to reset the children, and everything is much more predictable.

### Using “previous siblings” to create a CSS-Only stars rating system

Semantically, a rating system can be thought of as just a simple list of radio buttons with their corresponding labels. That comes in handy, as it will allow us to use the `:checked` pseudo-selector to modify the siblings.

So let’s start from there:

As we discussed previously, elements are in reverse order to allow for a “previous sibling” selector. Notice we are using the unicode “white star” character (U+2606) to represent the empty stars.

Let’s display them side by side, in the correct (reverse) order:

Now hide the radio buttons themselves, no one wants to see that:

And apply some styling to the star characters:

The only truly important line there is the `position:relative`. It will allow us to absolute position a filled star (U+2605) pseudo element on top of it, which will be initially hidden.

When we hover over a star, the filled star pseudo element should become visible for it and all _previous_ siblings.

Same thing for the selected rating, by matching all labels that come _before_ the checked radio button:

**Remember** that using the !important flag is **exactly the opposite** of a good practice. I do so here as there’s no other way to achieve the added functionality discussed in the next section without it.

Last but not least, we need to “remember” the current rating, just in case the user wants to change it. For instance, if they had selected five stars, and for whatever reason want to change it to four, we should display stars 1 to 4 as filled and the fifth as semi-transparent when hovering over the fourth.

That can be achieved by changing the opacity of the _previous_ siblings of the checked input when hovering over the container:

That’s also why we needed the `opacity:1 !important` in the initial hovering declaration. Otherwise this last rule would have won the specificity contest and applied a semi-transparent fill to everything.

And there we have it, a cross-browser, fully functional CSS-only stars rating system using “previous siblings” selectors.

As you can see, just because “it’s impossible” doesn’t mean you shouldn’t try. Programming is about pushing the limits. So whenever you hit the wall, just push a little harder. Or I guess finding your way around it might be a better analogy?… anyway, you know what I mean. Keep on hacking!

### A note on accessibility

**The previous snippet is a simplification in order to make it easy to understand.** It is **not** something I would recommend to use on production due to many accessibility limitations.

In order to make the snippet a little more accessible, first thing would be to hide the radio buttons with pretty much any technique other than `display:none` to make them focusable. We should also add some focus ring on the whole stars snippet when any element inside is focused, via the pseudo-selector `:focus-within`.

The identical “☆” labels makes no sense for screen readers, so best approach will be to have a `<sp`an> inside the label with “n Stars” text, that will be hidden from sighted users .

Also the reverse HTML source + `display:row-reverse` approach makes keyboard rating awkward, as it doesn’t get reversed back. [Flexbox and keyboard accessibility](https://tink.uk/flexbox-the-keyboard-navigation-disconnect/) is quite a messy topic, but closest thing to a solution for that one is adding `aria-flowto`tag to each element, which at least fixes the issue for some screen readers + browser combinations.

For a more accessible snippet (using an alternative technique of modifying next siblings to look empty instead of trying to asses previous ones) check [Patrick Cole](https://www.freecodecamp.org/news/how-to-make-the-impossible-possible-in-css-with-a-little-creativity-bd96bb42b29d/undefined)’s, as we discussed in the answers below.

