---
title: How to style your webpage or markdown like a Medium article — or however you
  want
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T19:32:27.000Z'
originalURL: https://freecodecamp.org/news/style-webpage-or-markdown-like-medium-article-using-html-css-sass-bootstrap-c6f9e64c0955
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L8PQs8ubyxZVIr1EC-cZ6Q.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By ryanwhocodes

  If you love Medium’s style, then you can style your webpages or markdown files (converted
  to HTML) to give them the visual flavor of a Medium article. This tutorial will
  cover:


  Converting markdown to HTML

  Choosing custom fonts

  Stylin...'
---

By ryanwhocodes

If you love Medium’s style, then you can style your webpages or markdown files (converted to HTML) to give them the visual flavor of a Medium article. This tutorial will cover:

* [Converting markdown to HTML](https://medium.com/p/c6f9e64c0955#92d4)
* [Choosing custom fonts](https://medium.com/p/c6f9e64c0955#32e6)
* [Styling with CSS and Sass](https://medium.com/p/c6f9e64c0955#e6f1)
* [Manage layouts and spacing](https://medium.com/p/c6f9e64c0955#ec02)
* [Add a navbar and user caption](https://medium.com/p/c6f9e64c0955#8ae1)
* [Taking it further](https://medium.com/p/c6f9e64c0955#84be)

To give you an overview of how the design would look before and after the style has been applied, have a look at the images below.

* The original Readme (below left)
* With added style and hosted on Github pages (below right)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NU7xgo7GBaVWeVHSieqXuA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XDN6scmU6mLMt0jTsxfxVA.png)
_View the respective pages at: [https://ryandav.github.io/link-formatter/](https://github.com/ryandav/link-formatter/" rel="noopener" target="_blank" title="">https://github.com/ryandav/link-formatter/</a> and <a href="https://ryandav.github.io/link-formatter/" rel="noopener" target="_blank" title=")_

### Converting markdown to HTML

There are numerous ways to convert a markdown file, such as a Readme, into HTML. One way is to use a static site generator, such as [Middleman](https://middlemanapp.com/) or [Jekyll](https://jekyllrb.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*DNJmqdEG6f_hzJ2ryp1Xrw.png)
_Get started with Middleman at [https://middlemanapp.com](https://middlemanapp.com/" rel="noopener" target="_blank" title=")_

[Middleman](https://middlemanapp.com/) is based on [Ruby](https://www.ruby-lang.org/en/) and inspired by the design of [Ruby on Rails](https://rubyonrails.org/). It integrates with markdown parser gems, such as [Redcarpet](https://github.com/vmg/redcarpet). Once you’ve [started a site](https://middlemanapp.com/basics/install/), include `redcarpet` in your Gemfile, then add the following to the `config.rb` of your project:

```
set :markdown_engine, :redcarpetset :markdown,    :fenced_code_blocks => true,    :smartypants => true,    tables: true,    with_toc_data: true
```

Next, ensure that your markdown files are [within the project source folder](https://middlemanapp.com/basics/directory-structure/), then [serve](https://middlemanapp.com/basics/development-cycle/) or [build](https://middlemanapp.com/basics/build-and-deploy) the site to render them as HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZcyIABeCHl31RBlyAl-3w.png)
_Get started with Jekyll at [https://jekyllrb.com/](https://jekyllrb.com/" rel="noopener" target="_blank" title=")_

[Jekyll](https://jekyllrb.com/) has builtin integration with [Github pages](https://pages.github.com/), and so can be convenient if you want something hosted on Github with minimal design and setup. Once you have [set up your site](https://jekyllrb.com/docs/quickstart/), you can simply include your markdown files and they will be converted to HTML during the build process.

For more on this, have a look at the article [Convert an HTML site to Jekyll](https://jekyllrb.com/tutorials/convert-site-to-jekyll/).

Once you have created the HTML files, take a look at the code. This will show you which HTML tags are used in your page, which you can target for your styling.

### Choosing custom fonts

You can find similar fonts to Medium on sites like [Google fonts](https://fonts.google.com/). Find a sans-serif font for your headings and a serif font for the body text. Below are a few suggestions:

* Headings: [**Open Sans**](https://fonts.google.com/specimen/Open+Sans) (bold)
* Body: [**Lora**](https://fonts.google.com/specimen/Lora)

The quickest way to add them is through a link in your HTML head or CSS file. However, hosting the fonts locally means you can be independent of an external download service. One great tool is the [Google Webfont Helper](https://google-webfonts-helper.herokuapp.com/fonts), which not only provides font downloads but also the CSS to load them into your stylesheets. Now you can add the fonts for the headings and body elements to your stylesheet.

```
h1, h2, h3, h4, h5, h6 {  font-family: 'Open Sans', sans-serif;}
```

```
p, ul, li, a {    font-family: 'Lora', serif;}
```

### Styling with CSS and Sass

Vanilla CSS is a good choice for small web pages and sites. For larger projects, a CSS pre-compiler, such as [Sass](https://sass-lang.com/), means you can build your CSS with features such as [partials and shared variables](https://sass-lang.com/guide).

![Image](https://cdn-media-1.freecodecamp.org/images/1*L--IdXLwdPI9H2pgvc_ZmA.png)
_Get started with Sass at [https://sass-lang.com/guide](https://sass-lang.com/guide" rel="noopener" target="_blank" title=")_

If you want to define all your key values in one file that is shared across your other stylesheets, then a common way of doing this is to create a `_variables.scss` file. For example:

```
$primary-foreground-color: white;$body-font-size: 20px;$font-small: 14px;...
```

Then include the variables in other files: `font-size: $body-font-size;`

Create your Sass file and add the fonts and layouts. The great thing about Sass is you can load them using [partials](https://sass-lang.com/guide), so you can have an SCSS file called `site`, then import all the partials for fonts, variables, layouts and other parts of your web page.

```
# site.css.scss
```

```
@import "fonts/lora";@import "fonts/playfair_display";@import "fonts/open_sans";
```

```
@import "variables";
```

```
@import 'layout';
```

### Manage layouts and spacing

A simple way to manage page layouts is to add margin or padding to your elements in a stylesheet.

```
p {    margin: 25px;}
```

```
https://www.w3schools.com/Css/css_margin.asp
```

Alternatively you may wish to write your own classes or use one of the frameworks. This post covers [Bootstrap](https://getbootstrap.com), but the principles can easily be applied with other approaches.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S_3OIHV9vU4zzeco1346Ug.png)
_Bootstrap has excellent documentation to show you how to use its layout classes and components._

**Spacing between headers and paragraphs:** Bootstrap has some handy spacing classes to easily add different amounts of padding or margin to elements.

> _The classes are named using the format `{property}{sides}-{size}` for `xs` and `{property}{sides}-{breakpoint}-{size}` for `sm`, `md`, `lg`, and `xl`._  
> _- [Spacing · Bootstrap](https://getbootstrap.com/docs/4.1/utilities/spacing/)_

The numbering system goes from 0 to 5, so for example you can add a large margin on the top of a header or paragraph by using the `.mt-4` class, which refers to **margin top size 4**_._

```
h1, h3 {  @extend .mt-4 ;  @extend .mb-2 ;}
```

```
h5 {  @extend .my-3 ;}
```

```
p {  @extend .mb-4 ;}
```

For more on @extend and other Sass concepts, check out the [Sass Guide](https://sass-lang.com/guide).

**Setting the maximum width of text body:** Unless you really want text to span the entire width of a browser window, creating a `div` with a class that has a style set to a maximum width can manage this.

```
.center-content-740px {  max-width: 740px;  margin: 0 auto;}
```

### Add a navbar and user caption

If you want to include these pages within a larger website, then consider styling a layout page that includes a [navbar](https://getbootstrap.com/docs/4.1/components/navbar/), footer, and possibly some sidebars and social media links.

Then you can include your webpage content or converted markdown files within this layout structure to produce a website with your own Medium-inspired design.

Here is a [Codepen](https://codepen.io/ryanwhocodes/pen/oyNOVO) with HTML and CSS you can use to get started with your own navbar and user caption → → →

### Take it further

See how you can continue to add more of your own personality and brand to your website’s design. Why not try customizing your own social media links, nav bars, fonts choices, layouts, and color schemes? If you like the way that Medium presents its menus, then take a look into [popovers](https://getbootstrap.com/docs/4.0/components/popovers/) and [tooltips](https://getbootstrap.com/docs/4.0/components/tooltips/). Even if you like the idea of your website being inspired by Medium, the ultimate goal is to make it your own.

#### More from [ryanwhocodes](https://www.freecodecamp.org/news/style-webpage-or-markdown-like-medium-article-using-html-css-sass-bootstrap-c6f9e64c0955/undefined)

* [How you can make a progressive web app in an hour](https://medium.freecodecamp.org/how-you-can-make-a-progressive-web-app-in-an-hour-7e36d560610e)
* [How you can add Bootstrap to your Ruby on Rails project](https://medium.freecodecamp.org/add-bootstrap-to-your-ruby-on-rails-project-8d76d70d0e3b)
* [How to make a cross-browser extension using JavaScript and browser APIs](https://medium.freecodecamp.org/how-to-make-a-cross-browser-extension-using-javascript-and-browser-apis-355c001cebba)

