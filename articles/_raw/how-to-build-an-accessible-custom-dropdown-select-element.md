---
title: How to Build an Accessible Custom Dropdown Select Element
subtitle: ''
author: Elizabeth Lola
co_authors: []
series: null
date: '2024-01-04T17:06:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-accessible-custom-dropdown-select-element
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/a11y-select.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Sometimes you might want to use a different select element to match your\
  \ style based on the theme of your design. Or perhaps the default design is different\
  \ on separate browsers and you want uniformity. \nBut when designing this new element,\
  \ you might..."
---

Sometimes you might want to use a different select element to match your style based on the theme of your design. Or perhaps the default design is different on separate browsers and you want uniformity. 

But when designing this new element, you might forget to consider the accessibility of the component. 

Typically, default elements are accessible – and if you plan to replace them with custom designs, you should ensure it works as well as the default.

In this tutorial, I'll show you how to build a custom dropdown with a step by step example.

## Prerequisites

To follow along with this tutorial, you should have:

1. **Basic HTML knowledge:** Understand how HTML elements and attributes work.
2. **Basic JavaScript knowledge:** Familiarity with basic JavaScript concepts like functions, event handling, and DOM manipulation is helpful.
3. **Understanding of ARIA:** While the tutorial explains ARIA roles and attributes, having a basic understanding of accessibility concepts can be beneficial.

## Here's What We'll Cover:

1. [Default Select Features](#heading-default-select-features)
2. [How to Figure Out Which ARIA Attributes Are Required](#heading-how-to-figure-out-which-aria-attributes-are-required)
3. [How to Set Up the HTML](#heading-how-to-set-up-the-html)
4. [The CSS](#heading-the-css)
5. [The JavaScript](#heading-the-javascript)  
– [Toggle dropdown visibility](#heading-toggle-dropdown-visibility)  
– [How to close the dropdown](#heading-closing-the-dropdown-using-the-esc-key)  
– [Dropdown keyboard interaction](#heading-dropdown-keyboard-interaction)  
– [How to fix the option visibility issue](#heading-fixing-option-visibility-issue)  
– [How to highlight options on alphanumeric keypress](#heading-highlighting-options-on-alphanumeric-key-press)  
– [How to enhance screenreader functionality](#heading-enhancing-screen-reader-functionality)
6. [Wrapping Up](#heading-wrapping-up)

## Default Select Features

Since the default select attribute is accessible, let's look at some of the features that makes it accessible:

* The select element visibly indicates when it's active or selected, typically through a change in appearance.
* The element opens on click or key press (SPACE, UP, and DOWN Arrow)
* While the dropdown is open, users can move through the available options by pressing the UP or DOWN arrow keys.
* Entering alphanumeric keys when the dropdown is open highlights the option that matches the entered letters. If there's no match, nothing changes.
* Clicking on an option or pressing SPACE or ENTER when an option is highlighted selects that option, updates the select value, and closes the dropdown.
* If the dropdown is open, pressing the ESC key closes it, providing a quick way to cancel the selection or close the dropdown.
* When the select element is focused when using a screen reader, the screen reader announces that it's a select element and provides information about the currently selected value for accessibility.

Using this information, let's build a custom dropdown.

## How to Figure Out Which ARIA Attributes Are Required

While some elements' roles and accessible names are obvious, there are some that aren't. Whenever I need to find the appropriate role or ARIA-attibute for a component, I check out the [W3 accessible names](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/#accessiblenameguidancebyrole) guide. 

In this case, I know the custom dropdown should have a `role="options"` but I don't know what role to assign the parent elements. 

So to start, I locate the option **Accessible Name Guidance by Role** list. You can see that the Option is pointing to a combobox pattern.

![Option list in the Accessible Name Guidance by Role table](https://www.freecodecamp.org/news/content/images/2023/12/image-74.png)
_The option in the table is showing a combobox._

  
The next thing I need to do is to read more on the combobox. According to t[his MDN page](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/combobox_role#examples) I understand that a combobox is a component that combines an input type element with a dropdown list and allows users to select from a list of options presented in the dropdown.

That sounds exactly like what the select element does. The combobox also needs to have an `[aria-expanded](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-expanded)` attribute and a connecting popup element which will contain the list of options. According to the MDN page:

> The popup element associated with a `combobox` can be either a [`listbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/listbox_role), [`tree`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/tree_role), [`grid`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/grid_role), or [`dialog`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/dialog_role) element.

In this example, we'll be using a `listbox` element.

The combobox element needs to have an `aria-contols` and `aria-haspopup` attributes, the value of these attributes will be the ID of the `listbox` element. 

## How to Set Up the HTML

From the information gathered we will need a `combobox`, `listbox`, and `option` to setup our HTML.

In this example, the HTML will look like this:

```html
<form>
  <label for="select">Custom Select box</label>
  <button
     role="combobox"
     id="select"
     value="Select"
     aria-controls="listbox"
     aria-haspopup="listbox"
     tabindex="0"
     aria-expanded="false">
    Select</button>
  <ul role="listbox" id="listbox">
   <li role="option">Option 1</li>
   <li role="option">Option 2</li>
   <li role="option">Option 3</li>
  </ul>
</form>
```

In the code above, the button has a `role="combobox"` and according to the MDN combobox article the `[aria-expanded](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-expanded)` attribute is required when working with a combobox. The `aria-controls` points to the id of the listbox which is `listbox`. This associates the listbox with the combobox. 

## The CSS

You can style the dropdown anyhow you want based on your requirements. Here's a sample style for my component:

```scss
.form {
  margin: 1.2rem 0;
  position: relative;
  #announcement {
    opacity: 0;
  }
  label {
    display: block;
    padding: .7rem .8rem;
    width: 65%;
    margin: 0 auto;
    text-align: left;
    font-size: .75rem;
  }
  button,
  ul{
    display: block;
    padding: .7rem .8rem;
    width: 60%;
    margin: 0 auto;
    text-align: left;
    background: white;
    border: 0;
    font-size: 1rem;
  }
  button{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    
    &::before {
      font-family: "Font Awesome 5 Free";
      content: "\f107";
      vertical-align: middle;
      font-weight: 900;
      position: absolute;
      right: .8rem;
    }

    &:focus-visible {
      outline: 0;
      box-shadow: 0 0 5px 2px rgba(251, 146, 60, 0.7) inset;
    }
  }
  ul {
    color: #3f403b;
    position: absolute;
    left: 0;
    right: 0;
    top: 4.8rem;
    max-height: 10rem;
    overflow-y: auto;
    list-style-type: none;
    padding: 0;
    margin-top: .1rem;
    opacity: 0;
    transform: scale(1,0);
    transform-origin: top left;
    transition: all .3s ease-in;
    pointer-events: none;
    z-index: 2;
    &.active {
      opacity: 1;
      transform: scale(1,1);
      pointer-events: auto;
    }
    li {
      padding: .6rem .5rem;
      border-top: 1px solid #e6e6e6;
      cursor: pointer;
      transition: all .3s ease-in;
      position: relative;
      &::before {
        font-family: "Font Awesome 5 Free";
        content: "\f00c";
        vertical-align: middle;
        font-weight: 900;
        position: absolute;
        right: .8rem;
        opacity: 0;
        transition: opacity .300s ease-out;
      }
      &:hover, &.current {
        background: #e6e6e6;
      }
      &.active {
        box-shadow: 0 0 0 2px rgba(251, 146, 60, 0.7);
      }
      &.active::before {
        opacity: 1;
      }
    }
  }
}

```

In the code above, I have hidden the listbox element and added an active class that shows it. I have also added a current class that styles the highlighted option and an active class that styles the selected option.

This is how it looks:

![Downdown list with options](https://www.freecodecamp.org/news/content/images/2023/12/image-80.png)
_The current state and active state of an option_

## The Javascript

It's easier to break down the features and work on them one at a time, and that's what we'll do here.

### Toggle Dropdown Visibility

Clicking the combobox or pressing the `Space` or `Enter` keys on the keyboard (when the button is focused) should toggle the dropdown visibility:

```js
const elements = {
  button: document.querySelector('[role="combobox"]'),
  dropdown: document.querySelector('[role="listbox"]'),
}; // I like to group all my elements into one objects 🤓.
let isDropdownOpen = false;

const toggleDropdown = () => {
  elements.dropdown.classList.toggle('active');
  isDropdownOpen = !isDropdownOpen;
  elements.button.setAttribute('aria-expanded', isDropdownOpen.toString()); // update the aria-expanded state
};

const handleKeyPress = (event) => {
   event.preventDefault();
  const { key } = event;
  const openKeys = ['Enter', ' '];

  if (openKeys.includes(key)) {
    toggleDropdown();
  }
};

elements.button.addEventListener('keydown', handleKeyPress);
elements.button.addEventListener('click', toggleDropdown);
```

In the code above we've created a toggleable dropdown button that responds to both keyboard and mouse interactions. The `toggleDropdown` function adds an `active` class to the dropdown.

### Closing the Dropdown: Using the Esc Key

Pressing the Esc key or clicking outside the dropdown element should close the dropdown:

```js
// previous code

// update handleKeyPress function 
const handleKeyPress = (event) => {
    event.preventDefault();
  const { key } = event;
  const openKeys = ['Enter', ' '];
    
  if (!isDropdownOpen && openKeys.includes(key) || (isDropdownOpen && key === 'Escape')) {
    toggleDropdown();
    
  }
};

const handleDocumentInteraction = (event) => {
  const isClickInsideButton = elements.button.contains(event.target);
  const isClickInsideDropdown = elements.dropdown.contains(event.target);

  if (isClickInsideButton || (!isClickInsideDropdown && isDropdownOpen)){
    toggleDropdown();
  }
};


elements.button.addEventListener('keydown', handleKeyPress);
// elements.button.addEventListener('click', toggleDropdown);
document.addEventListener('click', handleDocumentInteraction);
```

While it might seem like the `handleKeyPress` and `handleDocumentInteraction` functions could be combined for simplicity, we'll keep them separate as these functions will handle more tasks later in the article.

In the code above we have updated the `handleKeyPress` function to check for `Escape` and also introduced a `handleDocumentInteraction` function to close the dropdown if there's a click outside the dropdown element.

### Dropdown Keyboard Interaction

Pressing the `UP` or `DOWN` arrow keys should open the dropdown. When the dropdown is open, these keys should allow navigation through the options, moving the selection up or down. Also, clicking on an option or pressing the `Space` or `Enter` keys while an option is focused should update the button's displayed value. This behavior aims to replicate the interaction of a standard select element.

```js
const elements = {
  button: document.querySelector('[role="combobox"]'),
  dropdown: document.querySelector('[role="listbox"]'),
  options: document.querySelectorAll('[role="option"]'), // add the options elements
};
let isDropdownOpen = false;
let currentOptionIndex = 0;

const toggleDropdown = () => {
  elements.dropdown.classList.toggle('active');
  isDropdownOpen = !isDropdownOpen;
  elements.button.setAttribute('aria-expanded', isDropdownOpen.toString());

  if (isDropdownOpen) {
    focusCurrentOption();
  } else {
    elements.button.focus(); // focus the button when the dropdown is closed just like the select element
  }
};

const focusCurrentOption = () => {
  const currentOption = elements.options[currentOptionIndex];

  currentOption.classList.add('current');
  currentOption.focus();

  elements.options.forEach((option, index) => {
    if (option !== currentOption) {
      option.classList.remove('current');
    }
  });
};

const handleKeyPress = (event) => {
  event.preventDefault();
  const { key } = event;
  const openKeys = ['ArrowDown', 'ArrowUp', 'Enter', ' '];

  if (!isDropdownOpen && openKeys.includes(key)) {
    toggleDropdown();
    
  } else if (isDropdownOpen) {
    switch (key) {
      case 'Escape':
        toggleDropdown();
        break;
      case 'ArrowDown':
        moveFocusDown();
        break;
      case 'ArrowUp':
        moveFocusUp();
        break;
      case 'Enter':
      case ' ':
        selectCurrentOption();
        break;
      default:
        break;
    }
  }
};

const handleDocumentInteraction = (event) => {
  const isClickInsideButton = elements.button.contains(event.target);
  const isClickInsideDropdown = elements.dropdown.contains(event.target);

  if (isClickInsideButton || (!isClickInsideDropdown && isDropdownOpen)) {
    toggleDropdown();
  }

  // Check if the click is on an option
  const clickedOption = event.target.closest('[role="option"]');
  if (clickedOption) {
    selectOptionByElement(clickedOption);
  }
};


const moveFocusDown = () => {
  if (currentOptionIndex < elements.options.length - 1) {
    currentOptionIndex++;
  } else {
    currentOptionIndex = 0;
  }
  focusCurrentOption();
};

const moveFocusUp = () => {
  if (currentOptionIndex > 0) {
    currentOptionIndex--;
  } else {
    currentOptionIndex = elements.options.length - 1;
  }
  focusCurrentOption();
};

const selectCurrentOption = () => {
  const selectedOption = elements.options[currentOptionIndex];
  selectOptionByElement(selectedOption);
};

const selectOptionByElement = (optionElement) => {
  const optionValue = optionElement.textContent;

  elements.button.textContent = optionValue;
  elements.options.forEach(option => {
    option.classList.remove('active');
    option.setAttribute('aria-selected', 'false');
  });

  optionElement.classList.add('active');
  optionElement.setAttribute('aria-selected', 'true');
};

elements.button.addEventListener('keydown', handleKeyPress);
document.addEventListener('click', handleDocumentInteraction);
```

In the updated code, we've added keyboard navigation and option selection. Here's the breakdown:

1. The `elements` object now includes a reference to the option elements with the role "option."
2. The dropdown can also be opened with keys like `ArrowDown`, `ArrowUp`, `Space` or `Enter`
3. When the dropdown is open, `Escape` closes the dropdown, `ArrowDown` moves focus down the options, `ArrowUp` moves it up, and `Enter` or `Space` selects the current option.
4. Clicking an option or using keyboard input selects the option.
5. The selected option is displayed in the button, and the aria-selected state of the option is updated.
6. `active` class is now added to the selected option

### Fixing Option Visibility Issue

This looks good so far – but if you're following along and you test this code, you'll notice an issue: if an option is out of view and the down arrow is pressed the option isn't shown. 

To fix this, you can use the `scrollIntoView` method to ensure that the current option is scrolled into view when it is focused. Add it to the `focusCurrentOption` like this:

```js
const focusCurrentOption = () => {
  const currentOption = elements.options[currentOptionIndex];

  currentOption.classList.add('current');
  currentOption.focus();

  // Scroll the current option into view
  currentOption.scrollIntoView({
    block: 'nearest',
  });

  elements.options.forEach((option, index) => {
    if (option !== currentOption) {
      option.classList.remove('current');
    }
  });
};

// rest of code
```

Also when the user selects an option, the dropdown should close, the same way the select element works. Call the `toggleDropdown` function in the `selectOptionByElement` function like this:

```js
const selectOptionByElement = (optionElement) => {
  const optionValue = optionElement.textContent;

  elements.button.textContent = optionValue;
  elements.options.forEach(option => {
    option.classList.remove('active');
    option.setAttribute('aria-selected', 'false');
  });

  optionElement.classList.add('active');
  optionElement.setAttribute('aria-selected', 'true');

  toggleDropdown(); // close the dropdown once an option is selected
  
};
```

### Highlighting Options on Alphanumeric Key Press

Pressing an alphanumeric keys should highlight the option that starts with said character. And if the same character is pressed again then the next option should be highlighted and so on.

```js
let lastTypedChar = '';
let lastMatchingIndex = 0;

// update the handleKeyPress function

const handleKeyPress = (event) => {
  event.preventDefault();
  const { key } = event;
  const openKeys = ['ArrowDown', 'ArrowUp', 'Enter', ' '];

  if (!isDropdownOpen && openKeys.includes(key)) {
    toggleDropdown();
    
  } else if (isDropdownOpen) {
    switch (key) {
      case 'Escape':
        toggleDropdown();
        break;
      case 'ArrowDown':
        moveFocusDown();
        break;
      case 'ArrowUp':
        moveFocusUp();
        break;
      case 'Enter':
      case ' ':
        selectCurrentOption();
        break;
      default:
        // Handle alphanumeric key presses for mini-search
        handleAlphanumericKeyPress(key);
        break;
    }
  }
};


// previous code

const handleAlphanumericKeyPress = (key) => {
  const typedChar = key.toLowerCase();
  
  if (lastTypedChar !== typedChar) {
    lastMatchingIndex = 0;
  }

  const matchingOptions = Array.from(elements.options).filter((option) =>
    option.textContent.toLowerCase().startsWith(typedChar)
  );

  if (matchingOptions.length) {
    if (lastMatchingIndex === matchingOptions.length) {
      lastMatchingIndex = 0;
    }
    let value = matchingOptions[lastMatchingIndex]
    const index = Array.from(elements.options).indexOf(value);
    currentOptionIndex = index;
    focusCurrentOption();
    lastMatchingIndex += 1;
  }
  lastTypedChar = typedChar;
};

// rest of the code
```

Running the code and testing it with both mouse and keyboard inputs should result in the expected behavior. 

### Enhancing Screen Reader Functionality

The last functionality I'm addressing in this article is the screen reader functionality.

For screen reader users, selecting an option should announce the selected option, Just like the default HTML select element. Update the HTML to have a div that will contain the content to be announced, like this:

```html
<form>
  <label for="select">Custom Select box</label>
  <button
     role="combobox"
     id="select"
     value="Select"
     aria-controls="listbox"
     aria-haspopup="listbox"
     tabindex="0"
     aria-expanded="false">
    Select</button>
  <div id="announcement" aria-live="assertive" role="alert" style="opacity:0;"></div> <!-- The screen reader will announce the content in this element  -->
  <ul role="listbox" id="listbox">
   <li role="option">Option 1</li>
   <li role="option">Option 2</li>
   <li role="option">Option 3</li>
  </ul>
</form>
```

Then use JavaScript to update the value in the alert:

```js
// previous code
const selectOptionByElement = (optionElement) => {
  const optionValue = optionElement.textContent;

  elements.button.textContent = optionValue;
  elements.options.forEach(option => {
    option.classList.remove('active');
    option.setAttribute('aria-selected', 'false');
  });

  optionElement.classList.add('active');
  optionElement.setAttribute('aria-selected', 'true');

  toggleDropdown();
  announceOption(optionValue); // Announce the selected option
};

const announceOption = (text) => {
  elements.announcement.textContent = text;
  elements.announcement.setAttribute('aria-live', 'assertive');
  setTimeout(() => {
    elements.announcement.textContent = '';
    elements.announcement.setAttribute('aria-live', 'off');
  }, 1000); // Announce and clear after 1 second (adjust as needed)
};

// rest of code
```

In the code above, I've added an `announceOption` function. The function is called whenever a user selects an option. The use of the _assertive_ value in the `aria-live` attribute signals to the screen reader to interrupt its current announcement and promptly announce the updated value.

Now when you test this with a screenreader, the screen reader announces the selected option as expected.

Here's a working example of the custom select on [Codepen](https://codepen.io/leezee/pen/abXPjvM):

%[https://codepen.io/leezee/pen/abXPjvM]

## Wrapping Up

There's room for improvement in these features, such as adding multiple select options, autocomplete, and enhancing the overall look. Yet, my intention is for this article to be a helpful guide, encouraging you to keep accessibility in mind when building a component.

If you're looking for a package to use you should consider using [React-Select](https://react-select.com/home)  or [Vue3-select](https://www.npmjs.com/package/vue3-select).

Thank you so much for reading this article, if you found it helpful consider sharing. Happy coding!

You can connect with me on [Linkedin](https://www.linkedin.com/in/elizabeth-meshioye/) or [Github](https://github.com/Lezette)

### Resources used in this article:

* [MDN Combobox roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/combobox_role)
* [W3 ARIA practices](https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/#accessiblenameguidancebyrole)

