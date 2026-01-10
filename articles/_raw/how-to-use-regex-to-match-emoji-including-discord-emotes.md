---
title: How to Use RegEx to Match Emoji – Discord Emotes Regular Expression Tutorial
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2022-07-13T23:04:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-regex-to-match-emoji-including-discord-emotes
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-roman-odintsov-6898861.jpg
tags:
- name: discord
  slug: discord
- name: emoji
  slug: emoji
- name: Regex
  slug: regex
- name: unicode
  slug: unicode
seo_title: null
seo_desc: "Emoji are special Unicode characters that render pictographs. But these\
  \ characters can be very tricky to identify with regular expressions (RegEx). \n\
  I was recently working on a Discord bot that had to detect the number of emotes\
  \ in a given message. T..."
---

Emoji are special Unicode characters that render pictographs. But these characters can be very tricky to identify with regular expressions (RegEx). 

I was recently working on a Discord bot that had to detect the number of emotes in a given message. Today I'll share my process with you, including the newer JavaScript RegEx feature that finally solved the issues I was having.

## How Unicode Emoji Work

The Unicode Consortium defines specific character codes for each emoji. They even maintain a [helpful emoji chart](https://unicode.org/emoji/charts/full-emoji-list.html) as a reference. As an example, `U+1F600` corresponds to the 😀 emoji.

Some emoji consist of multiple Unicode characters. This is most common with the flag emoji, which consists of the "regional indicators" that make up the country's two-letter country code. 

This means the United States flag, 🇺🇸, consists of the two Unicode characters `U+1F1FA` and `U+1F1F8`, which correspond to the regional indicators `U` and `S`.

> As a fun fact, it is up to the operating system to determine **how** to render an emoji. If you are on Windows, for example, you won't see a flag above. You'll see `US`.

## What are Discord Emotes?

One of Discord's many features is allowing communities to upload their own custom emotes. These emotes are identified by a name, and are used with the syntax `:emote_name:`.

However, the way they are identified by the client/API is different. Each emote has a unique ID, and they're sent in the message content as `<:emote_name:1234567890>`, or `<a:emote_name:1234567890>` for animated emotes.

You can see this in Discord by putting a backslash `\` before the emote and sending it. It will render something like this:

![A Discord message showing an emote's raw value `<:NaomiGrin:938275644092063784>`](https://www.freecodecamp.org/news/content/images/2022/07/image-162.png)

## How to Match Emoji and Emotes with RegEx

My original approach had two different RegEx phrases.

I was using `/(<a?)?:\w+:(\d{18}>)?/g` to catch the Discord emotes. This RegEx was successfully picking up Discord emotes, which was great! 

I paired it with `/:[^:\s]*(?:::[^:\s]*)*:/g` to match the Unicode emoji, which only partially worked. The problem here was that I was seeing some emotes being counted twice – because the Discord RegEx was matching them. And others were being missed entirely.

So, with RegEx being what it is, I tried to make it more complex. `<:[^:\s]+:\d+>|<a:[^:\s]+:\d+>|(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff]|\ufe0f)/g` was a bit more successful in matching the built-in emoji, but still wasn't perfect. This RegEx was designed to match unicode characters specifically.

I played around with trimming whitespace, using the word boundary `\b` character, and a few other tweaks, before finally giving up and doing some research. 

And then I discovered [Unicode Property Escapes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Unicode_Property_Escapes). This RegEx feature allows you to add the `u` flag to your RegEx, unlocking the Unicode Properties denoted with the `\p` character.

With some additional research, I was able to find the [Emoji Character properties](https://unicode.org/reports/tr51/#Emoji_Properties) – specifically, the `Extended_Pictograph` property. This enabled me to update the RegEx to a final, functional value:

```js
/<a?:.+?:\d{18}>|\p{Extended_Pictographic}/gu
```

The `\p{Extended_Pictographic}` property seems to match Unicode emotes as well as character modifiers (often used for skin tones in emoji).

## Conclusion

This RegEx is currently running in my production code and hasn't shown any issues yet. 

Hopefully this article has helped you. If you are interested in exploring Unicode Property Escapes further, the Unicode Consortium offers a [full list](https://www.unicode.org/Public/UCD/latest/ucd/PropertyValueAliases.txt) of the available values.

Happy Coding!

