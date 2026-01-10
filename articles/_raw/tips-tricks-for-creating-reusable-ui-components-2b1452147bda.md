---
title: Tips & tricks for creating reusable UI components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T18:29:17.000Z'
originalURL: https://freecodecamp.org/news/tips-tricks-for-creating-reusable-ui-components-2b1452147bda
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NSN1a2xVtV1exzcD8fpzhA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software architecture
  slug: software-architecture
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Gabriel Colombo

  In this article I want to share some tips and tricks I use while building our core
  frontend library using Ember.js. Having no contact with it before, it has been a
  great learning opportunity. I hope you guys enjoy it! Please note, ...'
---

By Gabriel Colombo

In this article I want to share some tips and tricks I use while building our core frontend library using Ember.js. Having no contact with it before, it has been a great learning opportunity. I hope you guys enjoy it! Please note, the code used to exemplify the ideas in the article contains just enough information to get the point across. It also uses some Ember.js terminology, but the concepts are meant to be framework-agnostic.

### The objectives

To put it simply, the requirements for building the library are the following:

1. It must be productive.
2. It must be maintainable.
3. It must be consistent.

### The approaches

#### Minimize business logic

One of most frequent problems I encounter on projects are components that contain way too much logic in them. Thus, performing tasks that are, theoretically, out of their scope.

Before implementing any functionality, it is good to outline some of the duties the component is responsible for.

Imagine we’re building a button component.

I would like to be able to:

* Inform which type of button it is — Primary or regular
* Inform the content displayed inside the button (Icon and text)
* Disable or enable the button
* Perform some action upon click

Having this little outline, pull apart the different parts involved in the process of building this component. Try to identify where things could be placed.

1 — The type and content are component-specific, so they can be placed into the component file.

Since the type is — to some extent — required, let’s add a verification in case no value was provided.

```
const type = get(this, 'type');
```

```
const types = {  primary: 'btn--primary',  regular: 'btn--regular',}
```

```
return (type) ? types[type] : types.regular;
```

I like mapping the properties into an object because it allows things to scale without much effort — in case we need a danger button or anything like it.

2 — The disabled state can be found on different components like an input. In order to avoid repetition, this behavior can be moved into a module or any shared structure — folks call it a _mixin_.

3 — The click action can be found in different components. So it can also be moved to another file and should contain no logic inside it — simply calling the callback provided by the developer.

This way we can have an idea what cases our component needs to address while helping to outline a base architecture that supports expansion.

#### Separate reusable UI state

Certain UI interactions are common among different components, like:

* Enable/disable — _eg. buttons, inputs_
* Expand / Shrink — _eg. collapse, drop-down lists_
* Show / hide — _Pretty much everything_

These properties are often used just to control visual state — hopefully.

Maintain a consistent nomenclature throughout different components. All actions related to a visual state can be moved to a mixin.

```
/* UIStateMixin */
```

```
disable() {  set(this, ‘disabled’, true);
```

```
  return this;},
```

```
enable() {  set(this, 'disabled', false');
```

```
  return this;},
```

Each method is only responsible for toggling a particular variable and returns the current context for chaining, like:

```
button  .disable()  .showLoadingIndicator();
```

This approach can be extended. It can accept different contexts and control external variables instead of using internal ones. For example:

```
_getCurrentDisabledAttr() {  return (isPresent(get(this, 'disabled')))    ? 'disabled'            /*  External parameter  */    : 'isDisabled';         /*  Internal variable   */},
```

```
enable(context) {  set(context || this, this._getCurrentDisabledAttr(), false);
```

```
  return this;}
```

#### Abstracting base functionalities

Every component contains certain routines. These routines must be performed regardless of the component’s purpose . For example, verifying a callback before triggering it.

These default methods can be also moved to their own mixins, like so:

```
/* BaseComponentMixin */
```

```
_isCallbackValid(callbackName) {  const callback = get(this, callbackName);    return !!(isPresent(callback) && typeof callback === 'function');},
```

```
_handleCallback(callback, params) {  if (!this._isCallbackValid(callback)) {    throw new Error(/* message */);  }
```

```
  this.sendAction(callback, params);},
```

And then included in the components.

```
/* Component */
```

```
onClick(params) {  this._handleCallback('onClick', params);}
```

This keeps your base architecture consistent. It also allows expansion and even integration with third-party software. But please, don’t be a [_philosophizing abstracter_](https://www.quora.com/What-are-the-growth-stages-of-a-programmer/answer/Andreas-Blixt).

#### Composing components

Avoid rewriting functionality as much as you can. Specialization can be achieved. It can be done through composition and grouping. As well as tweaking smaller components together in order to create new components.

For example:

```
Base components: Button, dropdown, input.
```

```
Dropdown button => button + dropdownAutocomplete => input + dropdownSelect => input (readonly) + dropdown
```

This way, each component has its own duties. Each handles its own state and parameters while the wrapper component handles its specific logic.

_Separation of concerns at its finest._

#### Splitting concerns

When composing more complex components, there is the possibility of splitting concerns. You can split concerns between different parts of a component

Let’s say we’re building a select component.

```
{{form-select binding=productId items=items}}
```

```
items = [  { description: 'Product #1', value: 1 },  { description: 'Product #2', value: 2 }]
```

Internally, we have a simple input component and a drop-down.

```
{{form-input binding=_description}}
```

```
{{ui-dropdown items=items onSelect=(action 'selectItem')}}
```

Our main task is to present the description to the user, but it has no meaning to our application — the value does.

When selecting an option, you split the object, sending the description down to our input through an internal variable while pushing the value up to the controller, updating the bound variable.

This concept can be applied to components where the bound value must be transformed, like a number, autocomplete or select field. Datepickers can also implement this behavior. They can unmask the date before updating the bound variable while presenting the masked value to the user.

The risks get higher as the transformations increase in complexity. By excessive logic or having to support events — so think it through before implementing this approach.

#### Presets vs New Components

Sometimes it is necessary to optimize components and services in order to facilitate development. These are delivered in the form of presets or new components.

Presets are parameters. When informed, they set predefined values on the component, simplifying its declaration. However, new components are usually more specialized versions of base components.

The hard part is to know when to implement presets or create new components. I use the following guidelines when making this decision:

**When to create presets**

1 — Repetitive usage patterns

There are times when a particular component is reused in various places with the same parameters. In these cases, I like to favor presets over new components, especially when the base component has an excessive number of parameters.

```
/* Regular implementation */
```

```
{{form-autocomplete    binding=productId    url="products"            /*   URL to be fetched         */    labelAttr="description"   /*   Attribute used as label   */    valueAttr="id"            /*   Attribute used as value   */    apiAttr="product"         /*   Param sent on request     */}}
```

```
/* Presets */
```

```
{{form-autocomplete    preset="product"    binding=productId}}
```

The values from the preset are only set if the parameter has not been informed, keeping its flexibility.

```
/* Naive implementation of the presets module */
```

```
const presets = {  product: {    url: ‘products’,    labelAttr: ‘description’,    valueAttr: ‘id’,    apiAttr: ‘product’,  }, }
```

```
const attrs = presets[get(this, ‘preset’)];
```

```
Object.keys(attrs).forEach((prop) =&gt; {  if (!get(this, prop)) {    set(this, prop, attrs[prop]);  }});
```

This approach reduces the knowledge required to customize your component. Concurrently, it is facilitating maintenance by allowing you to update default values in a single place.

2 — Base component is too complex

When the base component you’d use to create a more specific component accepts too many parameters. Thus, creating it would generate some problems. For example:

* You’d have to inject most — if not all — the parameters from the new component to the base component. As more and more components derive from it, any updates on the base component would reflect a huge amount of changes. Thus, leading to higher bug incidence.
* As more components are created, the harder it gets to document and memorize the different nuances. This is especially true for new developers.

**When to create new components**

1 — Extending functionality

It is viable to create a new component when extending functionality from a simpler component. It helps you prevent leaking component-specific logic to another component. This is particularly useful while implementing extra behavior.

```
/* Declaration */
```

```
{{ui-button-dropdown items=items}}
```

```
/* Under the hood */
```

```
{{#ui-button onClick=(action 'toggleDropdown')}}  {{label}} <i class="fa fa-chevron-down"></i>  {{/ui-button}}
```

```
{{#if isExpanded}}  {{ui-dropdown items=items}}{{/if}}
```

The example above utilizes the button component. This extends its layout to support a fixed icon while including a drop-down component and its visibility state.

2 — Decorating parameters

There is another possible reason for creating new components. This is when it is necessary to control parameter availability or decorate default values.

```
/* Declaration */
```

```
{{form-datepicker onFocus=(action 'doSomething')}}
```

```
/* Under the hood */
```

```
{{form-input onFocus=(action '_onFocus')}}
```

```
_onFocus() {  $(this.element)    .find('input')    .select();                 /* Select field value on focus */
```

```
  this._handleCallback('onFocus'); /* Triggers param callback */}
```

In this example, it was provided to the component a function meant to be called when the field is focused.

Internally, instead of passing the callback straight to the base component, it passes an internal function. This performs a particular task (selecting the field value) and then calls the callback provided.

It is not redirecting all the parameters accepted by the base input component. This helps to control the scope of certain functionalities. It also avoids unnecessary validations.

In my case, the onBlur event was replaced by another event — onChange. This triggers when the user either fills the field or selects a date on the calendar.

### Conclusion

When building your components, consider your side as well as whoever is using that component in their daily life. This way, everyone wins.

> The best result comes from everyone in the group doing what is best for himself and the group — John Nash

Also, don’t be ashamed to ask for feedback. You’ll always find something that can be worked on.

To sharpen your software engineering skills even more, I recommend following [Eric Elliott](https://www.freecodecamp.org/news/tips-tricks-for-creating-reusable-ui-components-2b1452147bda/undefined)’s series “_Composing Software”._ It’s awesome!

Well, I hope you enjoyed the article. Please take these concepts, turn into your own ideas and share it with us!

Also, feel free to reach out to me on twitter [@gcolombo_](https://twitter.com/gcolombo_)! I’d love to hear your opinion and even work together.

Thanks!

