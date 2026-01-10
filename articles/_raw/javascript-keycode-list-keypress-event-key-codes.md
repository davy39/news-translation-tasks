---
title: JavaScript Keycode List – Keypress Event Key Codes for Enter, Space, Backspace,
  and More
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-01-08T19:15:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-keycode-list-keypress-event-key-codes
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/freeCodeCamp-Cover.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "JavaScript keyboard events help you capture user interactions with the\
  \ keyboard. \nLike many other JavaScript events, the KeyboardEvent interface provides\
  \ all the required properties and methods for handling every keystroke a user makes\
  \ using the keyb..."
---

JavaScript keyboard events help you capture user interactions with the keyboard. 

Like many other JavaScript events, the `KeyboardEvent` interface provides all the required properties and methods for handling every keystroke a user makes using the keyboard.

There have been many articles written about how they work and how to use them. At the same time, [W3.org](https://www.w3.org/TR/uievents/#events-keyboardevents) keeps updating the specification by introducing new properties, deprecating existing ones, and marking certain code as legacy.  

Because of this, it is essential for web developers to keep learning about the `KeyboardEvent` interface to know what exactly they should use and what's no longer relevant.

In this article, we will learn about:

* The KeyboardEvent interface.
* The keyboard event types we need to focus on.
* The keyboard event types we may not ever need.
* Which properties you need in practice and how different browsers handle them.
* What is deprecated, and what's in use.
* A playground to try things out as we learn.
* Finally, the current list of key codes for reference and future use.

Hope you enjoy it.

# The KeyboardEvent interface and the event types

The KeyboardEvent interface provides information using the defined constants, properties, and a single method (as of January 2021). It extends the `UIEvent` interface which eventually extends the `Event` interface.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/keyboardevent_hierarchy.png)
_KeyboardEvent Hierarchy_

There are primarily three keyboard event types, `keydown`, `keypress` and, `keyup`. We can get contextual information about these events from the `KeyboardEvent` interface's properties and methods. 

You can add each of these event types to an HTML element or `document` object using the `addEventListener` method. Here is an example of listening to a `keydown` event on an element whose id is, 'type-here':

```js
let elem = document.getElementById('type-here');

elem.addEventListener("keydown", function (event) {
    // The parameter event is of the type KeyboardEvent
  	addRow(event);
});
```

Alternatively, you can use the handler methods like, `onKeydown(event)`, `onKeyup(event)`, `onKeypress(event)` with the element to handle keyboard events. Here is an example of handling a `keyup` event on an input element:

```html
<input type="text" id="type-here" onkeyup="doSomething(event)">
```

If you print the `event` object in the browser's console, you will see all its properties and methods along with the ones it inherits from the `UIEvent` and `Event` interfaces.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/event_info.png)
_I have pressed the key, `a` while handling the `keyup` event_

# Try This Interactive Keyboard Event Playground

Before we go any further, how about a playground to explore all the keyboard events, their properties, characteristics, and so on? I think it will be awesome to use it alongside this article and beyond. 

Just focus your cursor anywhere in the app embedded below, and type any key to see the contextual information about it. 

You can also filter out the events you want by unchecking the checkboxes at the top. So give it a try:

%[https://stackblitz.com/edit/js-keycodes?embed=1&file=index.html&hideExplorer=1&hideNavigation=1&view=preview]

> If you have any issues in accessing the playground above, you can access this tool directly here: [https://keyevents.netlify.app/](https://keyevents.netlify.app/)  
>   
> And you can find the source code of the demo from here: [https://github.com/atapas/js-keyevents-demo](https://github.com/atapas/js-keyevents-demo)

# keydown, keypress, keyup - which one should you use?

The keyboard events are:

* `keydown`: It fires when any key is pressed down.
* `keypress`: It fires only when a key that produces a [character value](https://www.w3.org/TR/uievents/#character-value) is pressed down. For example, if you press the key `a`, this event will fire as the key `a` produces a character value of `97`. On the other hand, this event will not fire when you press the `shift` key as it doesn't produce a character value. 
* `keyup`: It fires when any key is released.

If all three events are attached to a DOM element, the firing order would be:

1. First, keydown
2. Next, keypress (with the condition stated above)
3. Last, keyup

Among these events, the most used Keyboard event is (or, should be) `keydown` because:

* The `keydown` event has the maximum coverage of keys to produce the contextual information. The `keypress` event works only for a subset of the keys. You can't capture the Alt, Ctrl, Shift, Meta, and other similar key events with a keypress. This also means that we can not fire the keypress event with key combinations like `Ctrl Z`, `Shift Tab`, and so on.
* Moreover, [the `keypress` event](https://www.w3.org/TR/uievents/#event-type-keypress) has been deprecated. This is a big enough reason to avoid it.
* While both `keydown` and `keyup` events cover all the keys and are well supported by most browsers, there are a few differences that push `keydown` ahead of `keyup`. The keydown event fires before the browser processes the key, whereas the keyup event fires after the browser processes the key. If you cancel a keydown event (say, using `event.preventDefault()`), the browser's action will be canceled too. In case of the keyup event, the browser's action will not be canceled even when you have canceled the event.

In the example below, we are using `event.preventDefault()` when a `keydown` or `keyup` event fires. The bowser's action to write the key characters into the textbox will not be performed in the case of `keydown` but it will continue to happen for `keyup`.

%[https://stackblitz.com/edit/js-key-down-up-test?devtoolsheight=33&embed=1&file=index.html]

With all that explanation, the `keydown` event is a clear winner and should become the most popular (used) key event type. 

# How to use the KeyboardEvent properties in practice

This is the billion dollar question! The shortest answer is, it depends. But on what? It depends on:

* The browser support for your application
* How legacy is your application code is and how much are you willing to refactor?

But before we get there, let's see a preview of some of the the useful properties and methods of the `KeyboardEvent` interface.

| Proprty/Method | Description | Deprecated/Outdated | 
|-------------   |-------------|--------------------|
| altKey         | Returns a boolean(true/false). The value is `true` when `Alt` key is pressed.                   | No |
| ctrlKey        | Returns a boolean(true/false). The value is `true` when `Control` key is pressed.                   | No |
| shiftKey         | Returns a boolean(true/false). The value is `true` when `Shift` key is pressed.                   | No |
| metaKey         | Returns a boolean(true/false). The value is `true` when any of the `Meta` keys are pressed.                   | No |
| code         | Code value of the Physical Key. | No |
| key         | The actual value of the key pressed. | No |
| getModifierState() method | Returns a boolean(true/false). The value `true` indicates the `on` state of these keys, `CapsLock`, `NumLock`, `Alt`, `Control`, `Shift`, `Meta`, etc.| No |
| charCode         | Returns the Unicode value. This has been deprecated and we should use the `key` property instead. | Yes |
| keyCode         | Returns the neumeric code of the pressed value. This has been deprecated and we should use the `key` property instead. | Yes |
| which         | Returns the neumeric code of the pressed value. This has been deprecated and we should use the `key` property instead. | Yes |

The last three properties are deprecated and you should use the `key` property instead. The `key` property has the [widest browser support](https://caniuse.com/?search=Keyboardevent.key). 

It is supported on:

* Microsoft Edge: Version >= 79
* Firefox: Version >= 29
* Google Chrome: Version >= 51
* Safari: Version >= 10.1

So as long as you are not using any of the older browsers, the `event.key` property should be enough for you to identify a key. In case you have to support an older browser, a better fallback would be the `event.which` property.

```js
window.addEventListener("keydown", function (event) {
  
  if (event.key !== undefined) {
    // Handle the event with KeyboardEvent.key
  } else if (event.which !== undefined) {
    // Handle the event with KeyboardEvent.which
  }
});
```

If your code uses any of the deprecated properties and you have an opportunity to refactor that code, it is always better to go for it.

## Modifier Keys

The modifier keys are the special keys on your keyboard that modify the default behavior of the other keys. `Control`, `Shift`, and `Alt` are some modifier keys. When a modifier key is combined with another key, you can expect a different action to occur. 

For example, if you press the key `z`, it is supposed to return the key and code for the letter z. If you combine it with the modifier `Control` and press `Control z`, you will likely get an `Undo` operation. Let's see it with some more examples in the next section.

The properties, `event.altKey`, `event.ctrlKey`, `event.shiftKey`, and so on help detect if a modifier key has been pressed.

## Key Combinations

We can combine multiple keys and perform actions based on the key combinations. The code snippet below shows how to combine the `Control` and `z` key to define an action:

```js
document
  .getElementById("to_focus")
  .addEventListener("keydown", function(event) {
    if (event.ctrlKey && event.key === "z") {
      // Do Something, may be an 'Undo' operation
    }
});
```

Here is another example that demos a few more key combinations. Please give it a try:

%[https://stackblitz.com/edit/js-key-combinations?embed=1&file=index.js&hideExplorer=1&view=preview]

# A Full List of Key Event Values

The table below shows a list of keys with the `event.which`, `event.key` and `event.code` values.

| Key Name    | event.which | event.key | event.code | Notes 
|-------------|---------------------|-----------|------------|------|
| backspace   | 8                   | Backspace | Backspace |
| tab         | 9                   | Tab       | Tab |
| enter       | 13                  | Enter     | Enter |
| shift(left) | 16                  | Shift     | ShiftLeft | `event.shiftKey` is true |
| shift(right)| 16                  | Shift     | ShiftRight | `event.shiftKey` is true |
| ctrl(left)  | 17                  | Control   | ControlLeft | `event.ctrlKey` is true |
| ctrl(right) | 17                  | Control   | ControlRight | `event.ctrlKey` is true |
| alt(left)   | 18                  | Alt       | AltLeft | `event.altKey` is true |
| alt(right)  | 18                  | Alt       | AltRight | `event.altKey` is true |
| pause/break | 19                  | Pause     | Pause |
| caps lock   | 20                  | CapsLock  | CapsLock |
| escape      | 27                  | Escape    | Escape |
| space       | 32                  |           | Space   | The `event.key` value is a single space.
| page up     | 33                  | PageUp    | PageUp |
| page down   | 34                  | PageDown  | PageDown |
| end         | 35                  | End       | End |
| home        | 36                  | Home      | Home |
| left arrow  | 37                  | ArrowLeft | ArrowLeft |
| up arrow    | 38                  | ArrowUp   | ArrowUp |
| right arrow | 39                  | ArrowRight | ArrowRight |
| down arrow  | 40                  | ArrowDown  | ArrowDown |
| print screen| 44                  | PrintScreen  | PrintScreen |
| insert      | 45                  | Insert    | Insert |
| delete      | 46                  | Delete    | Delete |
| 0 | 48 | 0 | Digit0 | 
| 1 | 49 | 1 | Digit1 |
| 2 | 50 | 2 | Digit2 |
| 3 | 51 | 3 | Digit3 |
| 4 | 52 | 4 | Digit4 |
| 5 | 53 | 5 | Digit5 |
| 6 | 54 | 6 | Digit6 |
| 7 | 55 | 7 | Digit7 |
| 8 | 56 | 8 | Digit8 |
| 9 | 57 | 9 | Digit9 |
| a | 65 | a | KeyA |
| b | 66 | b | KeyB |
| c | 67 | c | KeyC |
| d | 68 | d | KeyD |
| e                | 69  | e | KeyE |
| f                | 70  | f |KeyF |
| g                | 71  | g | KeyG |
| h                | 72  | h | KeyH |
| i                | 73  | i | KeyI |
| j                | 74  | j | KeyJ |
| k                | 75  | k | KeyK |
| l                | 76  | l | KeyL |
| m                | 77  | m | KeyM |
| n                | 78  | n | KeyN |
| o                | 79  | o | KeyO |
| p                | 80  | p | KeyP |
| q                | 81  | q | KeyQ |
| r                | 82  | r | KeyR |
| s                | 83  | s | KeyS |
| t                | 84  | t | KeyT |
| u                | 85  | u | KeyU |
| v                | 86  | v | KeyV |
| w                | 87  | w | KeyW |
| x                | 88  | x | KeyX |
| y                | 89  | y | KeyY |
| z                | 90  | z | KeyZ |
| left window key  | 91  | Meta | MetaLeft | `event.metaKey` is true |
| right window key | 92  | Meta | MetaRight | `event.metaKey` is true |
| select key (Context Menu) | 93 | ContextMenu | ContextMenu |
| numpad 0         | 96  | 0 | Numpad0 |
| numpad 1         | 97  | 1 | Numpad1 |
| numpad 2         | 98  | 2 | Numpad2 |
| numpad 3         | 99  | 3 | Numpad3 |
| numpad 4         | 100 | 4 | Numpad4 |
| numpad 5         | 101 | 5 | Numpad5 |
| numpad 6         | 102 | 6 | Numpad6 |
| numpad 7         | 103 | 7 | Numpad7 |
| numpad 8      | 104 | 8 | Numpad8 |
| numpad 9      | 105 | 9 | Numpad9 |
| multiply      | 106 | * | NumpadMultiply |
| add           | 107 | + | NumpadAdd |
| subtract      | 109 | - | NumpadSubtract |
| decimal point | 110 | . | NumpadDecimal |
| divide        | 111 | / | NumpadDivide |
| f1            | 112 | F1 | F1 |
| f2            | 113 | F2 | F2 |
| f3            | 114 | F3 | F3 |
| f4            | 115 | F4 | F4 |
| f5            | 116 | F5 | F5 |
| f6            | 117 | F6 | F6 |
| f7            | 118 | F7 | F7 |
| f8            | 119 | F8 | F8 |
| f9            | 120 | F9 | F9 |
| f10           | 121 | F10 | F10 |
| f11           | 122 | F11 | F11 |
| f12           | 123 | F12 | F12 |
| num lock      | 144 | NumLock | NumLock |
| scroll lock   | 145 | ScrollLock | ScrollLock |
| audio volume mute   | 173 | AudioVolumeMute |  | ⚠️ The `event.which` value is 181 in Firefox. Also FF provides the code value as, `VolumeMute` |
| audio volume down   | 174 | AudioVolumeDown |  | ⚠️ The `event.which` value is 182 in Firefox. Also FF provides the code value as, `VolumeDown` |
| audio volume up   | 175 | AudioVolumeUp |  | ⚠️ The `event.which` value is 183 in Firefox. Also FF provides the code value as, `VolumeUp` |
| media player   | 181 | LaunchMediaPlayer |  | ⚠️ The ️`event.which` value is 0(no value) in Firefox. Also FF provides the code value as, `MediaSelect` |
| launch application 1 | 182 | LaunchApplication1 |  | ⚠️ The ️`event.which` value is 0(no value) in Firefox. Also FF provides the code value as, `LaunchApp1` |
| launch application 2 | 183 | LaunchApplication2 | | ⚠️ The ️`event.which` value is 0(no value) in Firefox. Also FF provides the code value as, `LaunchApp2` |
| semi-colon    | 186 | ; | Semicolon | ⚠️ The `event.which` value is 59 in Firefox |
| equal sign    | 187 | = | Equal | ⚠️ The `event.which` value is 61 in Firefox |
| comma         | 188 | , | Comma |
| dash          | 189 | - | Minus | ⚠️ The `event.which` value is 173 in Firefox |
| period        | 190 | . | Period |
| forward slash | 191 | / | Slash |
| Backquote/Grave accent  | 192 | ` | Backquote |
| open bracket  | 219 | [ | BracketLeft |
| back slash    | 220 | \ | Backslash |
| close bracket | 221 | ] | BracketRight |
| single quote  | 222 | ' | Quote |


Please Note:

- `event.which` has been deprecated(or outdated)
- The `event.code` value is the same for small letters(a) and capital letters(A). Hoever the `event.key` value represents the actual letter.
- The `event.which` value is different in Firefox(FF) and other browsers for the keys, `equal(=)`, `semicolon(;)`, and `dash/minus(-)`

# How about the Virtual Keyboard?

So what about virtual keyboards, like using our mobile phones or tablets or any other input devices? 

The [specification says](https://w3c.github.io/uievents/#code-virtual-keyboards) that if the virtual keyboard has a similar key layout and functionality to a standard keyboard, then it must result in an appropriate code attribute. Otherwise, it is not going to return the right value.

# In Summary

To Summarize:

* You can use the `KeyboardEvent` to capture user interactions using a Keyboard.
* There are primarily three key events, `keydown`, `keypress`, and `keyup`.
* We should use the `keydown` event type as much as possible as it satisfies most of the use-cases.
* The `keypress` event type has been deprecated.
* The `event.which` property has been deprecated. Use `event.key` wherever possible.
* If you have to support an older browser, use appropriate fallback for key detection.
* We can combine multiple keys and perform operations.
* The virtual keyboard supports these events as long as the layout and functions are similar to the standard keyboard.

That's all for now. Thank you for reading this far! Let's connect. You can @ me on [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary) with comments or feel free to follow.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/keytype.gif)
_From https://giphy.com/_


