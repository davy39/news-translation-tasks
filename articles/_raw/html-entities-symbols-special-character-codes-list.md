---
title: HTML Entities – A List of HTML Space and other HTML Symbols and Special Character
  Codes
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-05-25T18:08:51.000Z'
originalURL: https://freecodecamp.org/news/html-entities-symbols-special-character-codes-list
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ad4740569d1a4ca280b.jpg
tags:
- name: HTML
  slug: html
- name: reference
  slug: reference
seo_title: null
seo_desc: 'Most ASCII characters have a special code you can use in HTML to make that
  character reliably appear.

  These HTML Entities are particularly helpful for, say, manually inserting whitespace
  into your HTML.

  Each of these codes starts with an ampersand an...'
---

Most ASCII characters have a special code you can use in HTML to make that character reliably appear.

These HTML Entities are particularly helpful for, say, manually inserting whitespace into your HTML.

Each of these codes starts with an ampersand and ends with a semicolon.

You can use these anywhere in your HTML to reliably create that character. It should render the same regardless of which language your users' browsers are set to.

Some of symbols these have easier-to-remember codes. For example, the Euro currency character (€) is `&euro;` 

Where possible, I've used these easier-to-remember codes instead of their numeric codes.

## How to Use the &nbsp; whitespace character code

For example, if you wanted to insert a whitespace character, you could do something like this:

```html
<span>Superpower:&nbsp;listening</span>
```

You can even insert several of these in a row to create make-shift text padding:

```html
<span>Superpower:&nbsp;&nbsp;&nbsp;listening</span>
```

## How to Make a Newline in HMTL using the &#13; newline character code

If you wanted to force a newline:

```html
<p>This is paragraph text and &#13; woops there is a new line.</p>
```

And yes, you can use several of these back-to-back, too:

```html
<p>This is paragraph text and &#13;&#13;&#13; woops there are several new lines.</p>
```

## A Full List of Commonly-Used HTML Entity Character Codes

Below is a nice ASCII-formatted table of the most commonly-used symbols and characters. It took me a while to assemble all of these get them looking good.

As a developer, when I search for these codes I often get results that are image-based. These are inaccessible to people with visual disabilities, and make it hard for everyone to copy-paste the codes.

So if you find this helpful, please link to it and share it with your friends so more people can benefit from it. ?

```

+----------+--------+-----------------------------+
|  &code   | symbol |         description         |
+----------+--------+-----------------------------+
| &#33;    | !      | exclamation point           |
| &#34;    | "      | double quotation mark       |
| &#35;    | #      | hash symbol (octothorpe)    |
| &#36;    | $      | dollar sign                 |
| &#37;    | %      | percentate sign             |
| &#38;    | &      | ampersand                   |
| &#39;    | '      | apostrophe                  |
| &#40;    | (      | left parenthesis            |
| &#41;    | )      | right parenthesis           |
| &#42;    | *      | asterisk                    |
| &#43;    | +      | plus sign                   |
| &#44;    | ,      | comma                       |
| &#45;    | -      | hyphen                      |
| &#46;    | .      | period                      |
| &#47;    | /      | forward slash               |
| &#48;    | 0      | the number 0                |
| &#49;    | 1      | the number 1                |
| &#50;    | 2      | the number 2                |
| &#51;    | 3      | the number 3                |
| &#52;    | 4      | the number 4                |
| &#53;    | 5      | the number 5                |
| &#54;    | 6      | the number 6                |
| &#55;    | 7      | the number 7                |
| &#56;    | 8      | the number 8                |
| &#57;    | 9      | the number 9                |
| &#58;    | :      | colon                       |
| &#59;    | ;      | semicolon                   |
| &#60;    | <      | less-than symbol            |
| &#61;    | =      | equals symbol               |
| &#62;    | >      | greater-than symbol         |
| &#63;    | ?      | question mark               |
| &#64;    | @      | at symbol                   |
| &#65;    | A      | uppercase A                 |
| &#66;    | B      | uppercase B                 |
| &#67;    | C      | uppercase C                 |
| &#68;    | D      | uppercase D                 |
| &#69;    | E      | uppercase E                 |
| &#70;    | F      | uppercase F                 |
| &#71;    | G      | uppercase G                 |
| &#72;    | H      | uppercase H                 |
| &#73;    | I      | uppercase I                 |
| &#74;    | J      | uppercase J                 |
| &#75;    | K      | uppercase K                 |
| &#76;    | L      | uppercase L                 |
| &#77;    | M      | uppercase M                 |
| &#78;    | N      | uppercase N                 |
| &#79;    | O      | uppercase O                 |
| &#80;    | P      | uppercase P                 |
| &#81;    | Q      | uppercase Q                 |
| &#82;    | R      | uppercase R                 |
| &#83;    | S      | uppercase S                 |
| &#84;    | T      | uppercase T                 |
| &#85;    | U      | uppercase U                 |
| &#86;    | V      | uppercase V                 |
| &#87;    | W      | uppercase W                 |
| &#88;    | X      | uppercase X                 |
| &#89;    | Y      | uppercase Y                 |
| &#90;    | Z      | uppercase Z                 |
| &#91;    | [      | left square bracket         |
| &#92;    | \      | backslash                   |
| &#93;    | ]      | right square bracket        |
| &#94;    | ^      | caret                       |
| &#95;    | _      | underscore                  |
| &#96;    | `      | backtick                    |
| &#97;    | a      | lowercase a                 |
| &#98;    | b      | lowercase b                 |
| &#99;    | c      | lowercase c                 |
| &#100;   | d      | lowercase d                 |
| &#101;   | e      | lowercase e                 |
| &#102;   | f      | lowercase f                 |
| &#103;   | g      | lowercase g                 |
| &#104;   | h      | lowercase h                 |
| &#105;   | i      | lowercase i                 |
| &#106;   | j      | lowercase j                 |
| &#107;   | k      | lowercase k                 |
| &#108;   | l      | lowercase l                 |
| &#109;   | m      | lowercase m                 |
| &#110;   | n      | lowercase n                 |
| &#111;   | o      | lowercase o                 |
| &#112;   | p      | lowercase p                 |
| &#113;   | q      | lowercase q                 |
| &#114;   | r      | lowercase r                 |
| &#115;   | s      | lowercase s                 |
| &#116;   | t      | lowercase t                 |
| &#117;   | u      | lowercase u                 |
| &#118;   | v      | lowercase v                 |
| &#119;   | w      | lowercase w                 |
| &#120;   | x      | lowercase x                 |
| &#121;   | y      | lowercase y                 |
| &#122;   | z      | lowercase z                 |
| &#123;   | {      | left curly brace            |
| &#124;   | |      | vertical bar                |
| &#125;   | }      | right curly brace           |
| &#126;   | ~      | tilde                       |
| &larr;   | ←      | left arrow                  |
| &uarr;   | ↑      | up arrow                    |
| &rarr;   | →      | right arrow                 |
| &darr;   | ↓      | down arrow                  |
| &harr;   | ↔      | left-right arrow            |
| &lArr;   | ⇐      | left double arrow           |
| &uArr;   | ⇑      | up double arrow             |
| &rArr;   | ⇒      | right double arrow          |
| &dArr;   | ⇓      | down double arrow           |
| &hArr;   | ⇔      | left-right double arrow     |
| &lsquo;  | ‘      | left single smart quote     |
| &rsquo;  | ’      | right single smart quote    |
| &ldquo;  | “      | left double smart quote     |
| &rdquo;  | ”      | right double smart quote    |
| &#8218;  | ‚      | single low quotation mark   |
| &#8222;  | „      | double low quotation mark   |
| &ndash;  | -      | en dash                     |
| &mdash;  | –      | em dash                     |
| &nbsp;   |        | nonbreaking space           |
| &iexcl;  | ¡      | inverted exclamation mark   |
| &sect;   | §      | section sign (used in law)  |
| &brvbar; | ¦      | broken vertical bar         |
| &copy;   | ©      | copyright symbol            |
| &reg;    | ®      | registered trademark symbol |
| &#8482;  | ™      | trademark sign              |
| &cent;   | ¢      | cent sign                   |
| &pound;  | £      | Pound Sterling sign         |
| &yen;    | ¥      | Yen sign                    |
| &euro;   | €      | Euro sign                   |
| &plusmn; | ±      | plus-or-minus sign          |
| &micro;  | µ      | micro symbol (mu)           |
| &183;    | ·      | middle dot character        |
| &deg;    | °      | degree sign                 |
| &sup1;   | ¹      | superscript one             |
| &sup2;   | ²      | superscript two (squared)   |
| &sup3;   | ³      | superscript three (cubed)   |
| &para;   | ¶      | paragraph sign              |
| &middot; | ·      | middle dot                  |
| &frac14; | ¼      | one quarter fraction        |
| &frac12; | ½      | one half fraction           |
| &frac34; | ¾      | three quarters fraction     |
| &iquest; | ¿      | inverted question mark      |
| &#8224;  | †      | dagger                      |
| &#8225;  | ‡      | double dagger               |
| &#8226;  | •      | bullet                      |
| &#8230;  | …      | ellipsis (three dots)       |
+----------+--------+-----------------------------+
```


