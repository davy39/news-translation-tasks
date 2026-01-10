---
title: Angular NgClass Example – How to Add Conditional CSS Classes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-07T15:01:26.000Z'
originalURL: https://freecodecamp.org/news/angular-ngclass-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/angular-ngclass-article.jpg
tags:
- name: Angular
  slug: angular
- name: CSS
  slug: css
seo_title: null
seo_desc: 'By Xing Liu

  ngClass is a directive in Angular that adds and removes CSS classes on an HTML element.
  In this article, we are talking about ngClass in Angular only, not ng-class in angular.js.

  Prerequisites – What is Property Binding?

  Two things we hav...'
---

By Xing Liu

`ngClass` is a [directive in Angular](https://angular.io/api/common/NgClass) that adds and removes CSS classes on an HTML element. In this article, we are talking about `ngClass` in Angular only, not `ng-class` in angular.js.

## Prerequisites – What is Property Binding?

Two things we have to understand first are [property binding](https://angular.io/guide/property-binding) and [interpolation](https://angular.io/guide/interpolation) in Angular. Let's take the `placeholder` attribute of `input` as an example. 

Consider the following code:

```html
<!-- Normal HTML -->
<input placeholder="some text">

<!-- Interpolation -->
<input placeholder="{{ variable }}">
<!-- Property Binding -->
<input [placeholder]="variable">
```

Given that we have `variable = 'some text'` defined in the component, then all the above code will do **exactly the same thing**.

I would consider interpolation (`{{ }}`) as an `eval`. And property binding is just a less verbose way to achieve the same thing. Personally, I use property binding as much as I can.

## What is ngClass in Angular? The Basics

When it comes to `ngClass`, it supports three types of expression "return values": `String`, `Array`, and `Object`. Here is an example from the [official documentation](https://angular.io/api/common/NgClass#description):

```html
<div [ngClass]="'first second'">
<div [ngClass]="['first', 'second']">
<div [ngClass]="{first: true, second: true, third: true}">
<div [ngClass]="{'first second': true}">
```

All `div` elements above have two classes: `first` and `second`. Note that in the official documentation, there is a pair of single quotes in each of the object keys in the third example. But neither `first` nor `second` has a dash or space in it. So we can feel free to remove the quotes. 

In the fourth example, however, since the key is `first second` (which has a space in between) we need to add the single quotes.

Just a heads up – the value of `ngClass` doesn't have to be a literal, as shown above. Keep in mind that property binding evaluates its expression. So as long as the expression can be interpreted as `String/Array/Object`, we are good to go.

## How to Use ngClass in Angular

So what is an expression? Normally, an `expression` is something that represents a value, and a `statement` would do something without a return value. You're likely familiar with `if` statements, which are responsible for the control flow. Note that `if` statements don't have a return value. 

On the other hand, say, `num + 10` is an expression (given that `num` has a value like `1`) and it has a "return value" of `11`. 

In ECMAScript, assignment is also considered to be an `expression` and it does have a "return value". But we can't put an assignment expression in the property binding in Angular, which will throw an error saying that "Bindings cannot contain assignments".

That being said, all the following `[ngClass]`es are valid:

```html
<!-- Given that val="foo", the class of the following div would be "foofoo" -->
<div [ngClass]="val + val">

<!-- Given that val="foo", the class of the following div would be "foo" -->
<div [ngClass]="[val]">

<!-- Given that func is a function that returns "foo", the class of the following div would be "foo" -->
<div [ngClass]="func()">
```

## How to Use Angular ngClass with a Simple Condition

We can't write an `if` statement in `ngClass`, due to the fact that it is a statement. But we can't use a ternary operator since this is an expression. 

For example, if we want the text in a table cell to have a class of `red` when its value is larger than `10`, and if not it should have a class of `green`, here is the code:

```html
<td [ngClass]="val > 10 ? 'red' : 'green'">{{ val }}</td>
```

And if we want to toggle a class based on a condition, we could make one of the expressions an empty string. 

For example, if we want to add an `error` class in a form when it is invalid, and to remove the `error` class when it is valid, we could do this:

```html
<input type="text" [ngClass]="control.isInvalid ? 'error' : ''" />
```

But there is a less verbose way. Remember `ngClass` also supports an object as a value:

```
<input type="text" [ngClass]="{ error: control.isInvalid }" />
```

Another way to achieve the same thing is to use [class binding](https://angular.io/guide/attribute-binding#binding-to-a-single-css-class). This is ideal for a single class:

```html
<input type="text" [class.error]="control.isInvalid" />
```

## How to Work with Object Literals and ngClass 

When we use object literals, the `key` represents the `class` that we are going to configure for the element, while the `value` represents whether the class should be applied to the element. 

Note that the `key` will be applied only when the `value` is `[truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)`. In the above example, if `coltrol.isInvalid` is one of `false`, `undefined`, `''`, and so on, then the class of `error` will **not** apply to the element.

One more thing to note is that the [computed property name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names) syntax is not yet supported. But there is an [open issue](https://github.com/angular/angular/issues/13855) in the Angular official GitHub repo.

## Angular ngClass and Complex Conditions

What if the condition is more than just `true/false`? Say we need different class names when `val` is `0-5`, `6-10` and `>= 11`, which you can easily represent with an `if/else` statement:

```typescript
if (val >= 0 && val <= 5) {
  return 'low';
} else if (val >= 6 && val <= 10) {
  return 'medium';
} else {
  return 'high'
}
```

As mentioned above, we can't use an `if/else` statement in `ngClass`. But wait, `function` is a valid expression with a return value, and we can use an `if/else` statement in a `function`:

```typescript
class MyComponent {
  getClassOf(val) {
    if (val >= 0 && val <= 5) {
      return 'low';
    } else if (val > 5 && val <= 10) {
      return 'medium';
    } else {
      return 'high'
    }
  }
}
```

```html
<td [ngClass]="getClassOf(val)">{{ val }}</td>
```

So far so good. But I'd like to point out that this is actually not ideal. Long story short, due to how `ChangeDetection` works in Angular, the above function `getClassOf` might run multiple times, even when _we_ consider it unnecessary. 

That is way beyond the topic of this article, but you may check out [this article](https://medium.com/showpad-engineering/why-you-should-never-use-function-calls-in-angular-template-expressions-e1a50f9c0496) if you'd like to know more.

We can still achieve the same result without using a `function`. With an object literal it looks like this:

```html
<td [ngClass]="{ low: val >= 0 && val <=5, medium: val > 5 && val <= 10, high: val > 10}">
  {{ val }}
</td>
```

Looks a bit verbose. Consider that there will be only one class applied to the element, so if we can transform our `val` first, that's ideal:

```typescript
type ClassName = 'low' | 'medium' | 'high';

class MyComponent {
  className: ClassName = 'low';
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes.val) {
      className = mapValToClass(changes.val.currentValue);
    }
  }
  
  private mapValToClass(val: number): ClassName {
    if (val >= 0 && val <= 5) {
      return 'low';
    } else if (val > 5 && val <= 10) {
      return 'medium';
    } else {
      return 'high'
    }
  }
}
```

And all we need to do in the template is:

```html
<td [ngClass]="className"></td>
```

There are some cases when we can use array. Consider the following mapping relationship:

```
{
  1: 'first-element',
  2: 'second-element',
  3: 'third-element',
}
```

This means that for a `val` that is `1`, the class of the element will be `first-element`. When we see consecutive numbers such as `1`, `2` and `3`, then we can consider using an array. This is because by subtracting `1` from each value, we get `0`, `1` and `2`, which are just the indices of an array:

```typescript
type Val = 1 | 2 | 3;

class MyComponent {
  classArr = ['first-element', 'second-element', 'third-element'];
  val: Val = 1;
}
```

```html
<td [ngClass]="classArr[val - 1]"></td>
```

A fun fact is that in ECMAScript, an array is just an object with quite a few extra properties and methods. So you can do the above with an object as well:

```typescript
type Val = 1 | 2 | 3;

class MyComponent {
  classMap = {
    1: 'first-element',
    2: 'second-element',
    3: 'third-element',
  }
  val: Val = 1;
}
```

```html
<td [ngClass]="classMap[val]"></td>
```

Note that you can also achieve the above with nested ternary operators, which is something I always try to avoid.

## [ngClass] vs [class] in Angular

Before we wrap up, one thing worth mentioning is `[class]` notation. This is available starting from `[Ivy](https://angular.io/guide/ivy)`, which was introduced in Angular 9 as the default compiler and runtime.

The `[class]` is almost backward-compatible with `[ngClass]`, with some discrepancies:

1. `[ngClass]="{'a b': true}"` does work, but `[class]="{'a b': true}"` won't work. See [this open issue](https://github.com/angular/angular/issues/40623).
2. The value of `[class]` is not "deepwatched". See [here](https://hackmd.io/jzDc7hIDTdWtQblv2TbL9A).

## Conclusion

Thanks for reading! Hopefully now you know how `ngClass` works and can use it with confidence.

