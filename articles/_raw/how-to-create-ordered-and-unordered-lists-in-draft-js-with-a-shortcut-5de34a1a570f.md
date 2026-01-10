---
title: How to create ordered and unordered lists in Draft.js with a shortcut
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-14T17:40:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-ordered-and-unordered-lists-in-draft-js-with-a-shortcut-5de34a1a570f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*CrE6mvHFmfzE8Nzz
tags:
- name: DraftJS
  slug: draftjs
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrey Semin

  We at Propeller have encountered many differences between Draft.js and popular text
  editors. We also found some issues like controlling list depth and multiline items
  in lists. The biggest difference is the inability to use shortcuts ...'
---

By Andrey Semin

We at [Propeller](https://www.propellercrm.com/) have encountered many differences between Draft.js and popular text editors. We also found some issues like controlling list depth and multiline items in lists. The biggest difference is the inability to use shortcuts to start a list by default. Surprisingly enough you need to implement this logic yourself.

As always, there is a [plugin](https://www.npmjs.com/package/draft-js-list-shortcut-plugin) available to add support for the shortcuts you use. I also want to refer to [draft-js-autolist-plugin](https://github.com/icelab/draft-js-autolist-plugin) as a source of inspiration. For some reason, this plugin didn’t work when we tried it. So we’ve come up with our own solution which is now presented in this post.

### The problem

Open Google Docs, Word365, or whatever editor you use. Try to type `*` and then type `space`. Boom! You’ve started an unordered list. Nice feature to have, right?

![Image](https://cdn-media-1.freecodecamp.org/images/1*2mOm_bMFavV3jy2g3a-wvA.gif)

If we try the exact same trick with the default Draft.js configuration, we will get nothing but plain text.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ExCt2l6cP0BUhRjq036IKg.gif)

Let’s change it!

### Solution

To implement this feature, we need to keep track of the last three pressed buttons. Why three? Well, that’s because the longest character combination we need to support is `1. + space` which is exactly three presses.

To start, let’s implement the logic to store these presses. Here we would use a simple array named `history`. This array will store the value of the key that was pressed. We definitely don’t want to process any key presses with modifiers like `shift`, `alt` and so on. We can use Draft.js built-in`KeyBindingUtil.hasCommandModifier` function to perform the check for any modifier.

Draft.js exposes a `keyDown` event for us in the `keyBindingFn` prop function. We are going to check if we need to start a list here. If so, we need to return a so called`DraftEditorCommand`, which is a string. Also, to benefit from OS-level commands we need to add a `getDefaultKeyBinding` function call as a fall-through case.

We need to check if the currently pressed key is a `space`. If so we would run our checks against the `history` array. We check if we have a suitable set of previously pressed keys — `*` for an unordered list and `1.` for an ordered one. If we find a match, we return a command(string) to be processed later.

Now we need to implement the `handleKeyCommand` prop function and pass it to the editor. The logic is pretty simple. If we get one of our custom commands, we check if we should start a list on the current block. So here is a skeleton of the `handleKeyCommand` function.

To check if we are good to start a list, we check if the currently selected block satisfies all three of the following rules:

* The block type is `unstyled`
* The block has a `depth` of 0
* the block has `*` or `1.` as a text

Let’s wrap it up with the code:

Now we’re able to catch the exact case where Draft.js needs to start a list! Now it’s a time to implement the `startList` function.

First of all, we need to map our custom commands to a particular list style. This means we need to start an unordered list for the `start-unoredered-list` command.

We start an ordered list for the `start-ordered-list` command. Next, we need to update the styling of the block to the selected type. To do it we would use the `toggleBlockType` function of `RichUtils` module, which comes as a part of Draft.js.

Next we need to replace the shortcut text we’ve entered with an empty string. To do it we need to call the `replaceText` method of the `Modifier` module. This method requires a selection range to determine what should be replaced. We need to get the selection out of the block and update it to have `focusOffset` value equal to block length. This combination means we want to replace the whole text we’ve entered.

Great! Now we need to update our local editor state with the new state we get from the `startList` function. So let’s bring it all together!

OK! We’re almost done! But there is one more moment we need to handle. In some cases when one of our custom commands fire, we should not start a list based on the output of the `shouldStartList` function. We need to process the insertion of the space manually.

For implementation details of the `getSelectedBlock` method, check out [my previous post](https://medium.com/p/800fb3a6714c) on this Draft.js topic!

To do this we may want to use a method called `insertText` of the `Modifier` module. Obviously enough, it is used to build a new content state with the provided text inserted into it. As always, we need to provide the current content state, current selection state and the text we want to insert (a single space in our case).

We need to add a call to this function to our `handleKeyCommand` function. So here is the final version of it:

![Image](https://cdn-media-1.freecodecamp.org/images/1*KB28XT74Srehykb3VRSOyw.gif)
_We’ve added support of lists shortcuts. Good work!_

If you’ve read this post all the way through, you may also want to check out [my previous post](https://medium.com/p/800fb3a6714c) about Draft.js enchantment. You may want to apply it to your project as well.

