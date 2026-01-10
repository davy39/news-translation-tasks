---
title: CSS rules that will make your life easier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T15:08:28.000Z'
originalURL: https://freecodecamp.org/news/css-rules-to-live-by-962a051e1eb2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*KEpWDREymV7FDijB
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Nick Gard

  After years of writing and maintaining a couple of very large web projects and numerous
  smaller ones, I have developed some heuristics for writing maintainable CSS. I have
  used BEM, SMACSS, and CSS Modules for naming, though this article...'
---

By Nick Gard

After years of writing and maintaining a couple of very large web projects and numerous smaller ones, I have developed some heuristics for writing maintainable CSS. I have used BEM, SMACSS, and CSS Modules for naming, though this article is not about naming, per se. (I tend to use a mix of atomic classes and BEM-ish naming.) This article is more about the properties and values I use or avoid.

> My StyleLint config: [https://github.com/NickGard/css-utils/blob/master/stylelint.config.json](https://github.com/NickGard/css-utils/blob/master/stylelint.config.json)

#### Colors

A pet peeve of mine is an over-abundance of color values in a web project. A large, long-lived project I worked on a few years ago had over 300 unique colors declared across 40-some CSS files. A third of these were shades of grey. Brand colors were repeated with slight differences of hue. Many of these colors differed by literally imperceptible values, like `#3426D1` and `#3426D2`. The solution to this is to either use atomic color classes or variables (in SCSS or CSS) for the accepted brand colors.

Limiting the number of accepted colors has the added benefit of making it simple to ensure that the background and foreground colors meet the WCAG2.0 Color Contrast guidelines.

Another bug-prone practice is using alpha-channel colors, usually by declaring the color with `rgba()` or `hsla()` functions. A color created this way with an alpha channel value of anything other than `1` is semi-opaque. The perceived color now changes depending on what is in the _background_. Usually, the desired color is what this one looks like over a white background, so you can use a hex value instead. Some preprocessor functions, like SASS’s `lighten()`, will generate a semi-opaque color, so stick to hard-coded values or variables.

#### Typography

All properties that affect or are affected by the font should be declared _once_ together. Right after declaring any `@font-face` rules, I like to add atomic classes for the font that change the `font-size` (via `rem`) and include `line-height`, `letter-spacing`, and `word-spacing` that are appropriate for that combination of font and size. After that, no `font-*` or `text-*` (with the exception of `text-overflow`) property should be used in any ruleset.

Declaring these properties once in conjunction with the font-face ensures that the copy on the site always looks right. Adjusting the `line-height` instead of `padding` or `margin` will create bugs when the text wraps. Adjusting `font-weight` separately from the font declaration runs the risk of creating a [faux bold font](https://alistapart.com/article/say-no-to-faux-bold/). Changing `font-style` on a font that doesn’t support it creates a faux oblique.

Lastly, avoid setting font sizes in anything other than `rem` units. Using `em` causes problems when nesting elements because `em` is a scalar multiple of the _current_ `font-size`. Using `px` (or any other “fixed” measurement) risks creating copy that is difficult to read **and** [impossible for the user to adjust](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size#Pixels). Allow the user (or the user’s browser) to set the `font-size` to what is right for them by not declaring a `font-size` on the `body` or `html` element and only using `rem`.

#### Spacing

On a content-first site, spacing should complement copy. Any static measurement, like `padding: 4px`, looks wrong at _some_ font size. A dynamic measurement responsive to font sizes, like `padding: .5em`, looks right at every font size.

Use `em` for spacing properties.

#### Grid

[CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) is [_very_ well supported](https://caniuse.com/#search=grid) (back to IE10!) and allows the arranging of content in two dimensions without added container elements like Bootstrap’s `row` or `col` grid elements. Designers often work in 12-column grids and CSS frameworks tend to follow suit but grids, like all spacing, should complement copy, not constrain it. Grids should be written ad hoc, not in a pre-determined format without context. Do not bloat your CSS with a “grid framework.”

#### Text alignment

`text-align` is often used to align things other than text. This is not the right tool for the job. Use flexbox for this kind of alignment. Using the values `left` and `right` doesn’t always work with languages that are right-to-left or vertical (some browsers map these values to the flow-relative `start` and `end`, but not all). Using the value `justify` on text can cause problems in some languages with digraphs, and [it can cause problems for people with dyslexia](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align#Accessibility_concerns). Every use case for `text-align` is better solved by flexbox, so use that instead. Always.

#### Outlines

Outlines on focused elements are how browsers natively communicate which element is receiving input. The default outlines are usually prominent enough to be useful to every user, including those needing high contrast. The default outline is usually overwritten (or removed) because it doesn’t fit with the site’s design. Unless you are _replacing_ the focused `outline` style with some other prominent and accessible focus indicator, **do not remove or nullify the outline property**.

#### Focus & Hover

As mentioned above, beware changing `:focus` styling because it acts as an indicator for which element is currently receiving input. Adding styles to an element on `:hover` is often a nice touch, but do not use that pseudo-selector to show additional copy unless you do the same for `:focus` (and, of course, if the element is _focusable_). It is usually, but not always, a good idea to use both the `:hover` and `:focus` pseudo-selectors for the same ruleset. (Adding the `:focus` selector to the hover styles for a button can result in a pressed button looking “stuck” on.)

#### Opacity

Setting the `opacity` of an element to `0` does not actually hide it from accessibility tools. The element still takes up room in the flow of the document and its copy is still read by screen-readers. The only two use-cases that reasonably call for the use of the `opacity` property is when transitioning an element into view (transition quickly from `0` to `1`) and when styling a dialog overlay (so the content below is somewhat visible). Beware of “stacked” semi-opaque overlays. The opacity level is multiplicative, so the content below two overlays each with `opacity: 50%` is shown as if it is below a single element with `opacity: 25%`.

#### Selectors

Stick to using class and class-like selectors. Using id, type, and universal selectors come with headaches. In CSS specificity, id selectors will always win against any other selector, but `[id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)` [attributes are supposed to be unique](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id) (per page) so they’re not useful for applying reusable styles.

Selector performance in modern browsers is a negligible concern, so despite what you may have heard about the universal selector (`*`) not being performant, my real concern with its use is that it is too general for almost every use-case. Using some selector like `.my-class >`; * will eventually lead to opting out some child, so you might as well add classes to the elements you wish to style and target them directly.

A similar argument can be made for not using type selectors, like `div`, `main`. They tend to match too many elements and usually require more details to be useful, such as `div.some-class`. Compound selectors like this have a higher specificity than a single class selector, a bug-generating problem addressed below.

Stick to class (`.class`), attribute (`[attribute]`), and pseudo-class (`:focus`) selectors. They all have the same level of specificity.

#### Specificity

At the opposite end of the spectrum of selectors being too general (like using `*`) are selectors being too specific. Both cases cause problems. An overly-specific selector breeds even more specific selectors or the dreaded `!important` declarations. Each successive selector becomes a new hurdle to overcome when making styling changes, and following this path leads to the ever-growing fragile stylesheets we all dread working with.

CSS has a naturally increasing specificity — the order of the rulesets. This is part of [the cascade in Cascading Style Sheets](https://medium.com/@ntgard/cascades-in-css-e79f8c0f4df2). With this in mind, we can write rulesets in ascending order of “importance” without increasing the selector specificity level. For example:

```
.btn {  color: black;}.btn--primary {  color: green;}.btn--primary--light {  color: white;}
```

In this example, each single-class-selector is more specific than its predecessor, eliminating the need to declare a ruleset for `.btn.btn--primary` or `.btn.btn--primary--light`.

The fix is to stick to single class selectors as much as possible, written in order of increasing “importance,” and avoid using `!important` declarations.

#### Text-transform

For sites that support languages other than English, using `text-transform` will probably cause problems. [There are several cases where browsers replace a character with an incorrect version for the upper- or lower-case transformations](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform#Browser_compatibility). The fix is never to use `text-transform` and instead rely on an accurately capitalized copy.

#### Z-index

If any `z-index` rule is included in a stylesheet, there will eventually be two other rules that declare `z-index: 9999;` and `z-index: 99999;`. Attempting to use atomic classes or variables to limit the number of acceptable z-indexes will not only fail to curb developers from using `calc()` and SCSS math to modify the value for their use-case, but will miss the target entirely because of how stacking contexts work.

It has been my experience that most, if not all, uses of `z-index` can be replaced by restructuring the HTML to use the natural stacking context (elements lower on the page are higher in the context) or by [adding a property to the element or its parent to force a new stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).

Avoid `z-index` at all costs.

#### Pseudo-elements

Using the pseudo-elements `::before` and `::after` is not only helpful, but it’s often fun! Many stylistic tricks rely on the use of these two pseudo elements and, as long as there is no copy in them (via their `content` property), they are considered semantic. The issue with putting copy in these elements is that whether or not they are read by accessibility devices varies across browsers and devices. It is better to not deal with that discrepancy by avoiding placing a copy in them.

The pseudo-elements `::first-letter` and `::first-line` do not work like you probably think they should. They only target the first letter/line in a block-level element. There are also issues with the `::first-line` selector incorrectly targeting double-byte characters (such as Japanese Kana) and [digraphs](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-letter#Browser_compatibility).

Manipulating the styles of selected text or placeholder text via `::selection` and `::placeholder`, respectively, often leads to trouble. With `::placeholder`, the concern is simple: [you shouldn’t be using placeholders](https://www.nngroup.com/articles/form-design-placeholders/). This is especially true for anything of importance, such as input labels or hints. By including `::placeholder` styles, you encourage developers, designers, and authors to use them, much to the frustration of your users.

Modifying selection styles, usually `color` and `background-color`, leads to more subtle but insidious bugs. While the [default selection colors](https://stackoverflow.com/a/16094931) are not consistent across browsers or devices and they do not always provide an acceptable contrast with your site’s text color, users sometimes overwrite them for accessibility reasons. Changing the colors, in this case, could either not work (because of the user’s accessibility CSS trumps yours) or it could interfere with their style sheets (if you use `!important`). Using this pseudo-element to try to guarantee an accessible contrast could end up disrupting the experience for the very people you wish to help.

(Though I’ve forgotten many of the details of this bug, I ran into an issue years ago where Chrome’s auto-translated text was rendered invisible because it relied on `::selection` styling which I had modified.)

#### Transitions & Animations

Transitioning or animating properties other than `opacity` and `transform` causes the browser to repaint or reflow the page. This may not seem like a problem on a high-end developer machine, but it will cause stuttering on low-end laptops and phones. Bad animation is worse than no animation.

#### Prefers Reduced Motion

Writing animations that are helpful, beautiful, and _safe_ is not a simple undertaking. With the advent of the media query `prefers-reduced-motion`, we can help make our pages safer for people with vestibular disorders, and less annoying for the rest of us. While adding this media query is not a silver bullet, it helps. I’ve written the nested rule to be opt-out, meaning that **all** CSS animations get stopped unless the author includes the class `safe-animation` on the element.

```
/* https://github.com/mozdevs/cssremedy/issues/11#issuecomment-462867630 */@media (prefers-reduced-motion: reduce) {  *:not(.safe-animation),  *:not(.safe-animation)::before,  *:not(.safe-animation)::after {    animation-duration: 0.01s !important;    animation-iteration-count: 1 !important;    transition-duration: 0s !important;    scroll-behavior: auto !important;  }}
```

#### Reset extensions

My go-to CSS reset is a modified form of the [Meyers reset](https://meyerweb.com/eric/tools/css/reset/). There are a few rules I remove from the reset, though. I don’t like to remove list icons from `ol` and `ul` elements. I find that doing so encourages developers to use those elements in non-semantic ways, like grouping items that are physically proximate but not ontologically proximate. I also remove the rule setting the `line-height` on the `body` to `1`. Setting attributes that affect, or are affected by, the font _separately_ from setting the font is a bug waiting to happen.

Some additions I make to the reset file are below. I do not like to include a `.hidden` atomic class in my CSS because there is a better option that will work even if the CSS doesn’t load — the `hidden` attribute. The default browser behavior of setting `display: none` on hidden elements can be overwritten, even accidentally, so I include a rule to enforce it.

```
body {  /* more intuitive sizing */  box-sizing: border-box;}*, ::before, ::after {  box-sizing: inherit;}i, cite, em, var, dfn, address {  /* prevent faux italic */  font-style: normal;}b, h1, h2, h3, h4, h5, h6, strong, th {  /* prevent faux bold */  font-weight: normal;}[hidden] {  /* enforce accessible semantics */  display: none !important;}
```

> My Reset: [https://github.com/NickGard/css-utils/blob/master/reset.css](https://github.com/NickGard/css-utils/blob/master/reset.css)

Another utility that I often find necessary is a `visually-hidden` class. While I use `aria-label` more often for invisible screen-readable text, I usually include the following rule somewhere:

```
/* https://a11yproject.com/posts/how-to-hide-content/ */.visually-hidden {  position: absolute !important;  height: 1px;  width: 1px;  overflow: hidden;  clip: rect(1px, 1px, 1px, 1px);}
```

#### BEMish naming

I can’t end this article without at least one comment on naming conventions. I like the BEM naming because it reads well. `<button class="btn--primary"` /> tells me exactly what kind of button it is. My one break from the Official BEM™ methodology is that I like t**o u**se one class on an element (with the possible exception of atomic classes). It offends my sensibilities t`o see <button class="btn btn--pr`imary" /> because the second class already tells me the styles extend fr`om` the base btn ruleset. This a**lso creates two reasons for a li**ne to change, which is a red flag.

In my CSS, this looks like this:

```
.btn, .btn--primary {  /* base button styles */}.btn--primary {  /* primary button overrides */  /* has naturally higher specificity */}
```

In SCSS, you can achieve this same effect using `@extend`.

#### Conclusion

These have been my rules of thumb for several years now and have helped me maintain large codebases with many contributors. It’s not perfect and I’m always adjusting it (`prefers-reduced-motion` is new) but I hope that by sharing it, it will help others.

