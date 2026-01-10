---
title: How to Build Great HTML Form Controls
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-05T17:43:37.000Z'
originalURL: https://freecodecamp.org/news/perfect-html-input
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/HTML-Blog-Cover.png
tags:
- name: forms
  slug: forms
- name: HTML
  slug: html
seo_title: null
seo_desc: 'By Austin Gil

  Today I''m going to show you all the things to consider when building the perfect
  HTML input. Despite its seemingly simple nature, there''s actually a lot that goes
  into it.

  How to Make the Control

  Well, we need to start somewhere. Might ...'
---

By Austin Gil

Today I'm going to show you all the things to consider when building the perfect HTML input. Despite its seemingly simple nature, there's actually a lot that goes into it.

## How to Make the Control 

Well, we need to start somewhere. Might as well start with the control itself.

HTML offers three different form controls to choose from: `[<input>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input)`, `[<textarea>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)`, and `[<select>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)`. Today, we'll use `<input>`, but the same rules will apply to the others.

```html
<input />
```

## How to Make `<input>` Work

Inputs are generally used to capture user data. To do so, they should be placed within a  `[<form>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)`  element, but that's not quite enough. When the form is submitted, it won't know how to label the input's data.

For a form to include an input's data when the form is submitted, the input needs a `[name](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#name)` attribute. You don't need state management or data binding. Just a `name`.

```html
<input name="data" />
```

## How to Make the Input Accessible

Now that we've made the robots happy, it's time to focus on the humans.

Every input also needs a label, both for clarity and for accessibility. There are a few options:

*  Add a `[<label>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)` element with a `[for](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label#attr-for)` attribute and assign it to the input's `[id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id)` (explicit label).
* Wrap the input with a `<label>` element (implicit label).
* Add an `[aria-label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)` attribute to the input.
* Add an `[aria-labeledby](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-labelledby)` attribute to the input and assign it to the `id` of another element.

Of all these options, the most reliable is an explicit label as it works across the most browsers, assistive technologies, and voice-control interfaces. Implicit labels do not work in Dragon Speech Recognition. ARIA attributes are finicky. 

The `[placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#placeholder)` and `[title](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/title)` attributes are not proper labels.

I recommend not wrapping everything in a `<label>` tag because:

1. It's prone to include more content than what would be considered the label. This results in a poor experience for screen-reader users.
2. It's common to add styles to the input's wrapper element. These styles may conflict with the default behavior of a `<label>`.

In general, I prefer using a `[<div>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)` to isolate the control.

```html
<div>
    <label for="input-id">Label</input>
    <input id="input-id" name="data" />
</div>
```

If you ever want an input that does not show the label, don't remove the label from the HTML. Instead, hide it with CSS or use a less reliable option. Keep the label in the markup and visually hide it with a `class` with these styles. These styles keep it accessible to assistive technology, while also visually removing it:

```css
.visually-hidden {
  position: absolute;
  overflow: hidden;
  clip: rect(0 0 0 0);
  width: 1px;
  height: 1px;
  margin: -1px;
  border: 0;
  padding: 0;
}
```

Note that it's still generally advised to include a visible label to avoid any confusion. A `placeholder` should not serve as a label.

## How to Choose a Type (or Not)

In addition to the different tags listed above, you can change the control's behavior by setting an input's `[type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types)` attribute. For example, if you wanted to accept a user's email, you can set the `type` attribute to "email". 

Input types can change the behavior or appearance of the UI. Here are just a few examples:

* The "[number](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number)" type changes behavior by preventing non-number value entries.
* The "[color](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/color)" type changes the UI by adding a button that opens a color picker.
* The "[date](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date)" type improves the data entry experience by offering a date-picker.
* The "[email](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email)" type enforces built-in constraint validation on form submission. 

However, some input types may be [false friends](https://en.wikipedia.org/wiki/False_friend).

Consider an input that asks for a US zip code. Only numerical entries are valid, so it might make sense to use a "number" `type`. However, one issue with the "number" input is that it adds a scroll event feature such that a user can scroll up on the input to increment the value or down to decrement it.

For a zip code input, it's possible that a user clicks on the input, enters their zip code, then tries to scroll down the page. This would decrement the value they entered, and it's very easy for the user to miss that change. As a result, the number they entered could be wrong.

In this case, it may be better to avoid the `type` attribute completely and use a `[pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#pattern)` such as `[0-9]*` if you want to limit the input to only numeric values. In fact, the "number" type is [often more problematic than it's worth](https://technology.blog.gov.uk/2020/02/24/why-the-gov-uk-design-system-team-changed-the-input-type-for-numbers/).

## Be Descriptive

Since we've briefly touched on constraint validation, it's a good time to mention descriptions. 

Although HTML has built-in validation attributes and there are several more robust JavaScript validation libraries, there is another effective approach to getting users to fill in proper data that can be less annoying.

Tell them exactly what it is you want.

Some form controls like "name" or "email" may be obvious, but for those that are not, provide a clear description for what you need. 

For example, if you are asking users to create a new password, tell them what the requirements are **before** they try to submit the form. And don't forget about assistive technology users.

We can associate an input with a description through visual proximity as well as using the `[aria-describedby](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby)` attribute.

```html
<div>
    <label for="password">Password</input>
    <input id="password" name="password" type="password" aria-describedby="password-requirements" />
    <p id="password-requirements">Please create a new password. Must contain at least 8 characters, one uppercase letter, one lowercase letter, and one special character.</p>
</div>
```

Descriptions are also an effective place to put any validation feedback messages.

## Be Flexible

When creating inputs, it's often tempting to add constraints for the acceptable values to ensure the user only sends good data. But being too strict can lead to a poor user experience.

For example, if you ask the user to enter a phone number, consider that there are several different acceptable formats:

* 8008675309
* 800 867 5309
* 800-867-5309
* 800.867.5309
* (800) 867-5309
* +1 (800) 867-5309
* 001 800 867 5309

All of the above represent the same phone number. Ideally, a user would be able to enter any of these formats and still be able to submit the form without issue.

If you want your input to only send number characters, it's possible to allow the user to type in whatever format they want. Then you can use JavaScript to add an event handler to the `blur` event, and remove any unwanted characters (space, dash, period, and so on) from the input's value. This would leave only the numbers.

## Make it Easy

If you've ever filled out a form using a mobile device, you may have noticed that your phone's keyboard looks different on different inputs. 

For a basic text input you see the standard keyboard, for email inputs you may see the @ symbol more conveniently placed, and for number inputs you may see the keyboard replaced with a number pad.

In many cases, the browser will choose a more appropriate keyboard to show users if the input `type` is set. But as we saw above, it's often better to use just a basic text input.

We can still offer a nicer user experience to mobile users by asking the browser to show specific keyboards despite the input missing a `type` attribute. We can accomplish this with the `[inputmode](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#inputmode)` attribute which accepts eight different options.

* text (default value)
* none
* decimal
* numeric
* tel
* search
* email
* url

Want to give it a try? Head over to [inputmodes.com](https://inputmodes.com/) on your mobile device. It's pretty cool.

## Continue Learning

That's over a thousand words I had to say about creating form controls. I hope you found it useful. 

If you would like to continue learning, I wrote a five-part series on how to build better HTML forms:

* [Part 1: Semantics](https://austingil.com/how-to-build-html-forms-right-semantics/)
* [Part 2: Accessibility](https://austingil.com/how-to-build-html-forms-right-accessibility/)
* [Part 3: Custom Styles](https://austingil.com/build-html-forms-right-styling/)
* [Part 4: User Experience](https://austingil.com/build-html-forms-right-user-experience/)
* [Part 5: Security](https://austingil.com/how-to-build-html-forms-right-security/)

If you liked this article, please [share it](https://twitter.com/share?via=heyAustinGil). It's one of the best ways to support me. You can also [sign up for my newsletter](https://austingil.com/newsletter/) or [follow me on Twitter](https://twitter.com/heyAustinGil) if you want to know when new articles are published.

