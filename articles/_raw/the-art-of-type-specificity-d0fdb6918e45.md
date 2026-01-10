---
title: How to Master the Art of Type Specificity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-16T03:13:56.000Z'
originalURL: https://freecodecamp.org/news/the-art-of-type-specificity-d0fdb6918e45
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KpUxhS8eOuejt0oaNggepQ.jpeg
tags:
- name: best practices
  slug: best-practices
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jeff M Lowery

  Do more specific definitions result in less flexibility?

  In this post I will try to avoid the debate about strong/static vs. weak/dynamic
  types (what more could possibly be said?), or even schema vs. schema less data structures.
  Inst...'
---

By Jeff M Lowery

_Do more specific definitions result in less flexibility?_

In this post I will try to avoid the debate about **strong/static** vs. **weak/dynamic** types (what more could possibly be said?), or even **schema** vs. **schema less** data structures. Instead, I want to focus on the degree of granularity of type definitions: what are the effects and trade-offs?

On the one end of the spectrum, very generic definitions encompass **potential** properties and behavior of objects. On the other end, you have a rich hierarchy of types, of which some are only subtly different from some other.

I will touch upon duck typing, SQL table-per-type (TPT) and table-per-type-hierarchy (TPH) concepts, and parameterized APIs.

When you think of generic types you might think of the Document Object Model (DOM), schemaless XML or YAML, literal objects in JavaScript, or NoSQL database documents. These are broadly generic, in that there are minimal constraints on structure, relations, and content.

Instead, let’s discuss user-defined types. They may or may not be enforced by the program language or a schema, but there will be constraints, assumed or otherwise, in the code that deals with them. Let’s use **Vehicle** as an analogy.

### Vehicle

A vehicle is a broad concept. Even if we confine discussion to wheeled vehicles, that covers everything from tricycles to semi-trucks. Could you encompass the spectrum of properties and behaviors of those tricycles, cars, and semis in one type? Yeah, you **could**. Clearly, that’s going to present some problems when handling Vehicle instances in the program code.

#### The Vehicle Type

Possible properties and methods of a Vehicle:

* tires  
* number  
* type [pneumatic, other]
* seats  
* number  
* padded [boolean]
* steering [wheel, handlebars]
* engine   
* type [none, gas, diesel]  
* number of cylinders [only if type is gas or diesel]
* drive()
* fuel()
* lights[on|high|off]

With even this minimal set of properties, the Vehicle type covers a huge domain and presents some challenges, data integrity being one of them. If my Vehicle is a trike, I don’t have an engine. If I don’t have an engine, the property `number of cylinders` is meaningless. If I have a trike with no engine, but `number of cylinders > 0`, is that an error?

I can fuel a car or truck, but not a tricycle. What happens if `fuel()` is called on a tricycle instance? Throw an Error? It is possible that some application logic is confused, but can the request be handled gracefully as a no-op?

The one perceived advantage to Vehicle is that it is flexible. If we instead split up Vehicle into subclasses **MotorVehicle** and **PedalVehicle**, we might put the following in MotorVehicle but not PedalVehicle:

* steering [wheel]
* engine   
* type [gas, diesel]  
* number of cylinders
* fuel()
* lights[on|high|off]

This seemingly makes sense. It is conceivable, though, that a tricycle has lights. It may not have an gas or diesel engine (not a kid’s trike, anyway), but it _could_ have an electric engine. If these cases arise, then there’s some refactoring to do.

In some languages or data management systems, you can define interfaces, and compose concrete types that fulfill those interfaces. So, you might have IEnginedVehicle, which might have related interfaces IElectricVehicle and InternalCumbustionVehicle (which in turn might be broken down into IGasVehicle and IDieselVehicle).

Interfaces are cheap to define, and good at annotation concepts, but they’re not a complete solution. Some interfaces can be incompatible with others: can a truck be both an ice cream truck and a pizza delivery truck? I suppose, if you want cold pizza or warm ice cream.

Aside from that, more specificity boxes you in, and requires you to have some foreknowledge of the all types of vehicles you will encounter.

It’s the **exceptions** that are going to get you as time marches on.

For this reason, especially when the domain is broad and in flux, it can be tempting to define vehicle entities less specifically, initially. You want to be open to anything that comes down the pike (pardon the pun).

#### Coding against generic types

On the coding side, there can be no assumptions about what Vehicle is. You must check every property for existence. Methods that exist may be meaningless for the specific entity that is represented by Vehicle. Your best bet is to have your code assume nothing. That makes testing a challenge, though. How can you possibly encompass all reasonable Vehicle configurations in your tests?

On the other hand, you have a pretty flexible system; that is, if no assumptions creep into your code (more about this in “**Why a duck**?”).

Too much specificity requires constant adjustments to the type model, including decisions of what the taxonomy of inheritance is, what property goes at what level, and potential difficulty in changes to the model when they affect not just code at the data layer, but the presentation layer as well. If you get it way wrong (due to rushed analysis), you have a lot of continuous rework.

#### Types and their properties

If you buy a [grab box of stuff](https://mcphee.com/products/super-awesome-surprise-box) from an online novelty store, you can expect a box. You have a vague idea of what it contains, but you won’t know until you open it and sort out each item one-by-one. The burden is on you, the client, and there are limited assumptions you can make (one might hope for a rubber chicken, but no guarantee!).

A first aid kit has a narrower range of possibilities as to what it contains. It’s a more specific type of object, and you can make assumptions as to its content and proceed accordingly. It’s going to contain gauze and bandages. It will have antiseptic, and probably pain relievers. For stuff that it **might** contain, you at least have a better idea what to look for.

### Why a duck?

Duck typing operates by incidence rather than declaration. Program logic revolves around interrogation of an object: “By the way, do you have property A? Do you have method B?…”.

Actions are performed based on responses to the interrogation. If it walks like a duck, quacks like a duck and has feathers, then it is probably a duck. Logic that is based on duck typing really doesn’t care, duck or no, because it assumes nothing; it operates on what it finds.

Yet assumptions will creep into any software logic that thinks it’s getting what it expects. Perhaps as much as 50% of software maintenance involves fixing incorrect assumptions or refining the ones that are there.

#### **Duck typing and the first responder**

Say I have a fire in my kitchen and call an emergency number. The first responder has a badge, helmet, and arrives in a vehicle with siren and flashing lights. Yay! The fireman! My house is saved. I command, pointing to the kitchen: “Put out that fire!”

The policeman looks at me quizzically.

I did all my duck typing interrogation, but reached the wrong assumption. Maybe the city recently decided policemen should respond to fire alarms if nearby, to aid the firemen.

I now have to add to my list of questions: “Do you put out fires?”

#### Of properties, discriminators, and named types

Duck typing is extremely flexible, but your code must deal with each object as if it could be anything. Instead of interrogating all properties, though, you can add a special **discriminator** property that identifies the type of object your code is receiving. One interrogation, and you're off to the races. Of course, the object has to have the correct discriminator value.

A named type is less likely to cause you problems, as types are assigned at object creation. In a weakly typed language, such as Javascript, things may not be as they seem, but you’re somewhat safer assuming.

Still, discriminators or types don’t really address the problem of specificity. The good old Object type doesn’t say much about its instances. It is a type, it does make some guarantees, but doesn’t do much by itself.

You can pass an object literal to a method, but the method must either 1) assume what it is getting, or 2) be prepared to find out.

Maintaining code that handles generic types can be an exercise in aggravation: while you can see what the client code _might_ do, to know what it _will_ do requires the specifics of the data it is handling.

A debugger helps, but if your breakpoint is buried far down in the call stack, or is in response to a callback, good luck! You may have some heavy excavating to do to know how you got where you are, logic-wise.

### Table-per-Type and Table-per-Type-Hierarchy

Relational databases run into this issue as well. If a table represents a type of thing, [are all rows in the table type-homogenous](http://blog.devart.com/table-per-type-vs-table-per-hierarchy-inheritance.html)? Or could each row reflect a more specific type, and the table represents a supertype of those things?

In the first case (table-per-type, or TPT), each column in each row is guaranteed to contain a valid value (NULL may be valid). Your code can anticipate query results that are consistent in their uniformity.

In the second case, some columns or column values may be valid for some types (rows) but not for others. This is table-per-type-hierarchy, or TPH.

A TPH table is a loosely defined type. The integrity of column values in each row is up to program logic. If I have a table called Vehicle containing data for all vehicles in my domain, then the column “oil weight” isn’t going to be applicable for rows representing tricycles.

The burden is now on the client code to understand the various possible types of vehicles in the Vehicle table, and perform logic accordingly. This is very similar to the case of a duck typed object, where properties may or may not be applicable for each instance of the generic type.

### Schema, anyone?

Does a schema (or other type system) take care of this problem? Well, no. As just shown, a TPH schema in a relational database can represent a super-type entity, but the rows may each define more specific entities. A discriminator column value can help sort out the subtype of each row, but it has to be checked in program logic.

The main benefit of using TPH is avoiding a huge schema with many tables, and lessening the number of joins required to pull together data for a type instance. There are always trade-offs to any approach.

### Parameter lists and options

Method parameters are another issue. The most common case is where parameter type is defined by order of occurrence:

```js
function circle(int x, int y, double radius){…}
```

or

```js
function circle(Position xy, double radius){…}
```

Arguments defined this way are locked-in: you can’t pass a boolean to radius, for instance. In JavaScript, there are no typed parameters, so most functions assume the type based on order of occurrence.

Not only is the type of parameter known (by declaration) or assumed (by convention), the number of parameters dictates how the method is called.

I always feel a slight annoyance whenever I want to dump some formatted JSON to the console, and have to type `JSON.stringify(obj, **null**, 4)`. That second argument, which is seldom used, is for the [replacer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) parameter.

#### **Options**

In JavaScript, you can pass an object literal as an argument, and this is often used as a named parameter list. Named parameters are more flexible than an argument list, and for more complex methods they can be very useful.

```js
function circle(options) {
    const {x, y, radius, ...rest} = options;
    if (rest.linewidth) {...}
    if (rest.fillColor) {...}
    ...
}
```

Flexible, yes, but a lot of interrogation. Plus, the arguments `x, y`, and `radius` are assumed to be there. Best practice seems to be to mix the type-specific parameter list with the more “generic” object literal:

```js
function circle(x, y, radius, options){...}
```

Where options is typically understood to refer to an [object whose properties are documented](https://lodash.com/docs/4.17.4#debounce).

### What to do?

Few practices in software are wholly good or bad (GOTO being the exception[[?](http://echochamber.me/viewtopic.php?t=43199)]). A rigid, type-rich system will no doubt prevent some coding errors, even if those types are not strongly enforced by the language or database. Code that uses specific types is more readable.

On the other hand, a stringent type hierarchy represents metadata that has to be maintained, and oftentimes the client knows what it is requesting and knows what it will receive. Dotting every “i” and crossing every “t” just for the sake of data transfer between two internal methods at times seems like bookkeeping work.

There is no right answer, and most programmers use types of varying (or no) specificity. A lot depends on the domain. If you’re writing code for a financial system, it would seem you’d want a rich and rigid set of type definitions; however, I understand some financial systems are [written in MUMPS](https://en.wikipedia.org/wiki/MUMPS#Current_users_of_MUMPS_applications), so what do I know?

