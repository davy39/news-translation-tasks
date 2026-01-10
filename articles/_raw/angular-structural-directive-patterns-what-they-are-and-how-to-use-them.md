---
title: Angular Structural Directive Patterns – What They Are and How to Use Them
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-08-18T15:21:47.000Z'
originalURL: https://freecodecamp.org/news/angular-structural-directive-patterns-what-they-are-and-how-to-use-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-pawe--l-1320737.jpg
tags:
- name: Angular
  slug: angular
seo_title: null
seo_desc: 'There are two types of  directives in Angular. Attribute directives modify
  the appearance or behavior of DOM elements. Structural directives add or remove
  elements from the DOM.

  Structural directives are one of the most powerful features of Angular, ...'
---

There are two types of  directives in Angular. **Attribute directives** modify the appearance or behavior of DOM elements. **Structural directives** add or remove elements from the DOM.

Structural directives are one of the most powerful features of Angular, and yet they’re frequently misunderstood. 

If you’re interested in learning more about structural directives, read on to find out what they are, why they’re helpful, and how to use them effectively in your projects today.

## What You'll Learn

In this tutorial, you will learn about Angular structural directive patterns. You will learn what they are and how to use them. 

By the end of this post, you will have a better understanding of these directives and how to use them in your own projects.

## What Are Angular Structural Directives?

Angular structural directives are directives that change the structure of the DOM. They can add, remove, or replace elements. Structural directives have a `*` in front of their names. 

In Angular, there are three standard structural directives:

* `*ngIf` – conditionally includes a template depending on the value of an expression returned by a Boolean.
* `*ngFor` – makes it simple to iterate over an array.
* `*ngSwitch` – renders each matching view.  

Here's an example of a structural directive. The syntax looks like this:

```
 <element ng-if="Condition"></element>

```

The condition must analyse to true or false.

```html
<div *ngIf="worker" class="name">{{worker.name}}</div>
```

Angular generates a `<ng-template>` element and applies the `*ngIf` directive to it. This transforms it into a property binding in square brackets, for example `[ngIf]`. The remainder of the `<div>`, including its class attribute, is then inserted within the `<ng-template>`:

Here's an example:

```html
<ng-template [ngIf]="worker">
  <div class="name">{{worker.name}}</div>
</ng-template>
```

## How Do Angular Structural Directives Work?

To use structural directives, you add an element with the directive in your HTML template. The element will then be added, removed, or replaced based on the condition or expression you set in the directive.

### Examples of structural directives

Let's start by adding some simple starter HTML code.

Your `app.component.html` file should contain the following code:

```html
<div style="text-align:center">
  <h1>
    Welcome 
  </h1>
</div>
<h2> <app-illustrations></app-illustrations></h2>
```

### How to use the `*ngIf` directive

You use `*ngIf` to display or remove an element based on the condition given. `ngIf` is quite similar to `if-else` used in other programming languages.

If the expression evaluates to false, the `*ngIf` directive removes the HTML element. If the `if` statement returns true, a duplicate of the Element is added to the DOM.

**Example of `*ngIf`:**

First create component illustrations in your Angular starter app. Then open your illustration component `HTML` file and add the following code:

```html
<h1>
	<button (click)="toggleOn =!toggleOn">ng-if illustration</button>
  </h1>
  <div *ngIf="!toggleOn">
  <h2>Hello </h2>
  <p>Good morning to you,click the button to view</p>
  </div>
  <hr>
  <p>Today is Monday and this is a dummy text element to make you feel better</p>
  <p>Understanding the ngIf directive with the else clause</p>
```

Then add the following boolean variable in the `.ts` file:

```html
toggleOn: boolean=true;
```

We have a div tag that holds the greetings. If the value of the toggleOn is false, the ngIf directive is displayed. After that, we added some dummy paragraphs.

The toggle allows you to demonstrate `*ngif` by hiding and showing the `divs`.

The full code to the illustration can be found [here](https://github.com/gatwirival/Structural-directives/tree/main/ngif-illustration) .

### How to use the `*ngFor` directive

We use the `*ngfor` directive to iterate through the values **​**of an array. This is similar to a for loop in other programming languages or frameworks.

**Example of `*ngFor`:**

Generate an Angular app using `ng new myapp` then create component illustrations. Open the `HTML` file and add the following code:

```
<ul>

    <li *ngFor="let wok of workers">{{ wok }}</li>

</ul>
```

Then add the code below to your illustration component TypeScript file:

```ts
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-illustrations',
  templateUrl: './illustrations.component.html',
  styleUrls: ['./illustrations.component.css']
})
export class IllustrationsComponent implements OnInit {
  workers: any = [

    'worker 1',

    'worker 2',

    'worker 3',

    'worker 4',

    'worker 5',

  ]

  constructor() { }

  ngOnInit(): void {
  }

}
```

We have an unordered list, where we use a for loop to iterate through the array of elements. So the additional property `*ngFor` was used with the element. It accepts an array and renders each element until it reaches the last value in the collection.

The full code to the illustration can be found [here](https://github.com/gatwirival/Structural-directives/tree/main/ngfor-illustration) .

### How to use the `*ngSwitch` directive

We use `ngSwitch` to render the element according to a single condition followed by the different case statements. The `*ngSwitch` directive is similar to the switch case.

**Example of *ngSwitch:**

```html
<div [ngSwitch]="Myshopping">
  <p *ngSwitchCase="'cups'">cups</p>
  <p *ngSwitchCase="'veg'">Vegetables</p>
  <p *ngSwitchCase="'clothes'">Trousers</p>
  <p *ngSwitchDefault>My Shopping</p>
</div>
```

Then add the following string variable in the `.ts` file:

```
  Myshopping: string = '';

```

We have a variable called `Myshopping` with a default value, which is used in the template to render certain elements that meet the conditions.

When the condition remains true, the relevant elements are rendered in the DOM and the rest of the elements are ignored.

The full code to the illustration can be found [here](https://github.com/gatwirival/Structural-directives/tree/main/ngfor-illustration) .

If there are no matches, the view with the NgSwitchDefault directive is rendered as shown with our code's output.

## When Should You Use Angular Structural Directives?

If you want to add or remove an element from the DOM, you would use a structural directive. You can also use them to change the CSS styles of an element, or to add event listeners. You can even use them to create new elements that were not previously there! 

The best rule is: _If you're thinking about manipulating the DOM, then it's time for a structural directive._

## Conclusion

Structural directives are an important part of Angular, and you can use them in a number of ways.  

Hopefully, this tutorial has given you a better understanding of how to use these directives and when to use each pattern.

