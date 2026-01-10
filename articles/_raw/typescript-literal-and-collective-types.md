---
title: TypeScript Literal and Collective Types
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-12-07T15:55:33.000Z'
originalURL: https://freecodecamp.org/news/typescript-literal-and-collective-types
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Literal-Types-vs-Collective-Types--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'TypeScript offers us a level of "safety" in our code by adding static types.

  We can guarantee that certain properties or functions are present in our code by
  making them conform to types.

  This can hugely reduce the amount of client-side errors you mi...'
---

TypeScript offers us a level of "safety" in our code by adding static types.

We can guarantee that certain properties or functions are present in our code by making them conform to types.

This can hugely reduce the amount of client-side errors you might have in your website, because it reduces human error bugs like calling functions on the wrong objects, for example.

TypeScript does this by utilising **Collective Types** and **Literal Types**.

So, what's the difference?

# Collective Types in TypeScript

**Collective Types** are a concept that are familiar to most developers who work with TypeScript. For example:

`const addOne = (numb: number) => num + 1;` 

This code uses **Collective Types**.

**Collective Types** are types like `number`, `string`, `boolean` or `number[]`.

These types encompass a huge amount of variables present – the `number` type for example can cover: 1, 2, 3, 4, 5...and so on.

But TypeScript also offers us sub-types on these **Collective Types** that are stricter.

# Literal Types in TypeScript

You can also use _values_ as types, so `let eleven: 11 = 11` is totally valid TypeScript code.

When I first saw this, I thought it looked a little weird.

But it is used heavily, and can really make your code more readable.

You can start to construct enum-like types, and strictly only allow certain values to be assigned, for example:

`type Door = 'open' | 'closed' | 'ajar'`

The `Door` type can now be used throughout your code – with a stricter set of values than the `string` type would have allowed.

If the `|` in the above code is unclear, it is a [Union Type](https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html) – and essentially means `OR`. Any type that conforms to `Door` can only be `open` OR `closed` OR `ajar`.

# Conclusion

**Literal Types** are sub-types of **Collective Types**. 

We can say all Literal Types are Collective Types – but not all Collective Types are Literal Types. To make that clearer, we could say the **Literal Type** `11` is a `number` but not all `number` types are `11`.

I hope the difference between the two types is clearer now, and if you need to constrict types strictly, you can make use of **Literal Types**.

I tweet my articles [here](https://twitter.com/kealanparr) if you would like to read more.

