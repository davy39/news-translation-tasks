---
title: How to Pick a Font – An In-Depth Guide for Developers
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2023-09-13T11:18:31.000Z'
originalURL: https://freecodecamp.org/news/things-to-consider-when-picking-fonts
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/markus-spiske-f81ym3dE5N4-unsplash.jpg
tags:
- name: fonts
  slug: fonts
- name: performance
  slug: performance
- name: UI Design
  slug: ui-design
seo_title: null
seo_desc: 'Fonts are not always free. If you''re fetching a font that is not already
  on your user''s phone or computer, they will have to download it. And this will
  impact performance.

  In documents and subtitles, embedding fonts can easily increase the file size ...'
---

Fonts are not always free. If you're fetching a font that is not already on your user's phone or computer, they will have to download it. And this will impact performance.

In documents and subtitles, embedding fonts can easily increase the file size tenfold. As for the web, here are some popular fonts and their potential network impact:

| Font | Size | Wi-Fi | Regular 4G/LTE | Regular 3G |
| --- | --- | --- | --- | --- |
| [Roboto](https://fonts.google.com/specimen/Roboto) | 168.3 KB | 0.05 s | 0.36 s | 1.90 s |
| [Montserrat](https://fonts.google.com/specimen/Montserrat) | 198.0 KB | 0.05 s | 0.42 s | 2.21 s |
| [Inter](https://fonts.google.com/specimen/Inter) | 309.8 KB | 0.08 s | 0.64 s | 3.40 s |
| [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) | 556.2 KB | 0.15 s | 1.13 s | 6.03 s |
| [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) | 187.9 KB | 0.05 s | 0.40 s | 2.10 s |

The estimated network speeds and latency are taken from [Throttling - Firefox Source Docs](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/throttling/index.html).

On the modern web, we've normalized fetching fonts from client-side, or embedding fonts in resources that are served to users. While this may be tempting, it actually makes very little sense for most use-cases.

This isn't suggesting to never use external fonts. Just a reminder that fonts aren't free, and that it's a good idea to review if it's worth packaging or fetching external fonts when it's avoidable.

Instead, I'd recommend you consider an expansive font selection, featuring typefaces available across operating systems. There are times we should fetch external fonts, but it shouldn't be the default attitude in everything that we build.

In short, you may just need an arbitrary typeface to show arbitrary text on your website. That's fine. But it's worth sticking to the wide array of typefaces already installed on the client's operating system.

In other words… only fetch an external font when it actually enhances the user experience!

## Why?

Given the number of typefaces available on all operating systems, there are likely many suitable options for your use-case.

There's no need to specifically fetch Roboto, Inter, or another font that's similar enough to the preinstalled options.

This is particularly relevant to corporate websites, blogs, forums, and web applications.

The user is there to consume content or get a task done. Unless you're looking to be creative, the average user doesn't know, and doesn't care, what typeface it has so long as it's legible.

Meanwhile, they may care for other things impacted by your font choices…

### Performance

Whether we're talking about embedding fonts in offline documents, or fetching fonts on the web, it increases the overall size and load time of resources.

Typefaces can be upwards of 160 KB per font face. The impact of this can be significant on slower networks or old mobile devices.

Particularly on the web, you'd derive more value building a lightening fast user experience, than fetching a typeface the user didn't ask for.

Until the typeface has finished fetching, sites can choose to block rendering or swap, which neither is ideal.

Font swapping is when the font changes shortly after visiting the site, leading to a flicker and an increase in [Cumulative Layout Shift](https://web.dev/cls/).

![Image](https://www.freecodecamp.org/news/content/images/2023/09/mdn-font-swap.gif align="left")

*A demo of blocking and font swapping on the MDN website. I refreshed with the cache disabled on a high-spec laptop connected to Wi-Fi with no throttling.*

![Image](https://www.freecodecamp.org/news/content/images/2023/09/out.gif align="left")

*A demo of the MDN website using Nimbus Sans, based on Helvetica, instead of external fonts. I refreshed under the same conditions.*

Dropping external fonts is pretty simple, but can improve load time, reduce bandwidth usage, and avoid font swapping, which all improve your [Core Web Vitals](https://web.dev/vitals/) and SEO.

### Privacy

When fetching fonts from a third-party server such as Google Fonts, client information is leaked to the third party. This includes the [IP Address](https://developer.mozilla.org/en-US/docs/Glossary/IP_Address), [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), and [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer), among other headers.

Every website that loads a typeface from Google Fonts, has given Google the potential to track the visitor. The domain you visited, the time you accessed it, what browser and operating system you're on, etc. They can form a timeline of the websites you visit from the fonts alone.

Google states that they do not track or store this information. However, given the nature of the internet, they inevitably must receive it.

Germany has actually ruled that websites that load Google Fonts are violating GDPR:

%[https://thehackernews.com/2022/01/german-court-rules-websites-embedding.html] 

This problem can be avoided by self-serving fonts. If you're going to use an external font, please consider this.

However, also know that some users [disable custom fonts](https://support.mozilla.org/en-US/kb/change-fonts-and-colors-websites-use#w_custom-fonts) or [block third-party fonts](https://github.com/gorhill/uBlock/wiki/Per-site-switches#no-remote-fonts), so you should still specify at least a generic family name regardless.

> "You should always include at least one generic family name in a `font-family` list, since there's no guarantee that any given font is available. This lets the browser select an acceptable fallback font when necessary.‌‌‌‌‌‌‌‌" (Source: [MDN Documentation for font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#try_it))

### Familiarity

Users are familiar with the experience of their operating system.

Maybe not how it works under the hood, or even how to perform simple operations, but they do encounter the welcome screen, context menus, and their preinstalled applications regularly.

It's safer to stick with typefaces the user already has access to because these are the typefaces the user is already accustomed to reading from.

This argument is in a similar vein to why it's a good idea to use the system date picker, color picker, or modal/dialog boxes instead of creating custom ones.

Users are familiar with their system!

From my experience, often one of the following occurs:

* The user couldn't tell that an external font was used, making it largely redundant. Most non-specialists experience this everyday, it's hard to even tell that websites are using different fonts from each other unless you're conscious of it.
    
* The user was able to tell, and thus has a different reading experience than what they're used to. The potential for disruption depends on the needs of the user, but that risk is often unnecessary.
    

Unless you have a reason to change it, it's best to stick with what the user is familiar with.

## Who else does this?

Wikipedia is the most notable example, and they even have a page elaborating on the topic: [Meta page on Wikipedia's use of typography](https://en.wikipedia.org/wiki/Wikipedia:Typography).

Some of the most popular sites don't fetch a single font on their landing page, in favor of using system fonts only:

| Site | Font Selector |
| --- | --- |
| Facebook | `SFProDisplay-Regular, Helvetica, Arial, sans-serif` |
| Instagram | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` |
| Cloudflare | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif` |
| Wikipedia | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, Helvetica, Arial, sans-serif` |
| Reddit | `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", sans-serif` |
| Bing | `"Segoe UI", Segoe, Tahoma, Arial, Verdana, sans-serif` |

You can verify for yourself by inspecting the site with your browser's development tools.

There are no outgoing network requests for fonts, and the `font-family` properties are set to system fonts only.

## Exceptions

There are times loading and embedding fonts does make sense, particularly if the look and feel you're after is significantly different from common system fonts:

* You're targeting an environment that doesn't have typefaces available.
    
* To fit with existing branding, like an in-house font.
    
* A creative or unique design, especially relevant for gaming and artsy sites.
    
* Icon fonts like [OpenMoji](https://openmoji.org/), but note that most clients come with emojis already.
    
* A website that's literally for distributing, displaying, and testing fonts.
    

## Consequences

If you apply a local font stack, your text content may not look pixel-for-pixel identical across clients. However, success should be measured by the user experience.

It is important for the site to feel familiar, but there are more significant changes between clients already, like the human-interface, resolutions, and DPI.

Compared to this, it's fine if the arch of the `a` has a slightly different radius, or the tick on the `l` is a few pixels longer. In fact, this is unlikely to go noticed, so it is unlikely to impact the user experience at all.

Users would sooner have qualms with the difference in speed or a flicker, before the difference between similar typefaces.

Another argument is that allowing different typefaces may make the layout difficult to manage. Glyphs can have different widths, and therefore take up varying space.

However, modern sites should be following [responsive design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design), so you should be taking the time to make the pages fluid anyway.

To minimize impact, you can use [web safe fonts](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals#web_safe_fonts).

If you dislike how limiting that is, pick a typeface included with your operating system, and find similar typefaces on other operating systems.

Even better if you can pick [metrically compatible typefaces](https://en.wikipedia.org/wiki/Typeface#metrics).

### Comparison

Let's visit a website and see what it's like to disable downloadable fonts.

I'll also replace all font selectors, to use Helvetica.

Note, my computer does not actually have Helvetica installed, so my operating system automatically translates this to Nimbus Sans, which is based on Helvetica. Nimbus Sans is preinstalled on [Debian](https://www.debian.org/).

In the case of MDN, is the second version really so undesirable that we need to load a 325 KB font, given the penalties and demonstrations raised above? Ultimately, this one is down to user preference, so I'll let you decide.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1.png align="left")

*MDN, with the Inter typeface fetched from client-side.*

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-1.png align="left")

*MDN, with the font-family overridden to use Helvetica.*

On the flip side, that doesn't mean to never fetch fonts. There are examples where the aesthetic may be more valuable to the user experience than the performance penalty.

Let's look at [Framasoft](https://framasoft.org/). They went for a more creative look and feel, also featuring a lot of [David Revoy's](https://www.davidrevoy.com/) illustrations.

To use Tovari Sans was a design choice which enhances the user experience, and isn't easily replaceable with a local font stack.

If we were to take that font away, the page feels inconsistent and unpolished. Even if we cleaned up the CSS, we'd still be detracting from the theme of the website.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-2.png align="left")

*Framasoft, with the Tovari Sans typeface fetched from client-side.*

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-4.png align="left")

*Framasoft, with the font-family overridden to use Helvetica.*

## Resources

Whether you want to go local, or just need to specify some fallback fonts, here are some helpful resources for picking out your font stack:

* [List of typefaces included with Apple operating systems](https://developer.apple.com/fonts/system-fonts/)
    
* [List of typefaces included with Windows](https://learn.microsoft.com/en-us/typography/fonts/windows_11_font_list#introduction)
    
* [Core typefaces included with ChromeOS](https://en.wikipedia.org/wiki/Croscore_fonts)
    
* [Documentation for web safe fonts](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals#web_safe_fonts)
    

## Cross-Platform Font Stacks

There are countless articles and resources available online that feature predefined font lists you can use. These are referred to as "*font stacks*".

In particular, I'd like to highlight a resource by [Dan Klammer](https://danklammer.com/), a designer and web developer who created [Modern Font Stacks](https://modernfontstacks.com/) ([GitHub repository](https://github.com/system-fonts/modern-font-stacks)), a website that helps you pick out native font stacks for your project.

Modern Font Stacks proposes a list of fonts for a variety of styles like Neo-Grotesque (a style of sans-serif) or Monospace Code (a style of monospace) and offers a visualization of how it will look across operating systems. It runs through a description of each stack, the CSS to use it, metadata like the weights available, and which of the fonts you personally have installed.

Some font classifications don't explicitly include a font from every operating system that exists, but remember that the generic font family (`sans-serif`, `serif`, `monospace`, `cursive`, and so on.) at the end will have you covered.

If you like the stack, you can run with it. But don't feel constrained either, you can also use it as a starting point and tweak the font stack to your needs.

I've included images from the GitHub repository (at the time of writing), featuring proposed font stacks for two of the most common styles used on the internet today:

![Image](https://www.freecodecamp.org/news/content/images/2024/05/neo-grotesque.png align="left")

*Base font stack proposed by Modern Font Stacks for the Neo-Grotesque style, a type of sans-serif font.*

![Image](https://www.freecodecamp.org/news/content/images/2024/05/monospace-code.png align="left")

*Base font stack proposed by Modern Font Stacks for the Monospace Code style, a type of monospace font.*

## Conclusion

In the end, the user experience is what matters most. Sometimes that means prioritizing visual design, other times that means prioritizing performance.

I hope this was worth your time, and that with the knowledge you can make an informed decision when choosing fonts for your next project.

Feedback and questions welcome, you can hit me up on [GitHub](https://github.com/SethFalco), [Mastodon](https://fosstodon.org/@sethi), or [LinkedIn](https://www.linkedin.com/in/sethfalco/)!
