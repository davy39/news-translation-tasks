---
title: What is boilerplate and why do we use it? Necessity of coding style guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-02T16:14:41.000Z'
originalURL: https://freecodecamp.org/news/whats-boilerplate-and-why-do-we-use-it-let-s-check-out-the-coding-style-guide-ac2b6c814ee7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hrjnxp5fCjg2Hxv8IrImcg.png
tags:
- name: boilerplate
  slug: boilerplate
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Meet Zaveri

  In Information Technology, a boilerplate is a unit of writing that can be reused
  over and over without change. By extension, the idea is sometimes applied to reusable
  programming, as in “boilerplate code.”

  Legal agreements, including s...'
---

By Meet Zaveri

In Information Technology, a boilerplate is a unit of writing that can be reused over and over without change. By extension, the idea is sometimes applied to reusable programming, as in “boilerplate code.”

Legal agreements, including software and hardware terms and conditions, make abundant use of boilerplates.

For instance, a lawyer may give you a five page contract to sign, but most of the contract is boilerplate — meaning it’s the same for everyone who gets that contract, with only a few lines changed here and there.

In computer programming, **boilerplate code** or **boilerplate** refers to sections of code that have to be included in many places with little or no alteration. It is often used when referring to languages that are considered _verbose_, i.e. the programmer must write a lot of code to do minimal jobs.

For example, in web development, simple boilerplate for HTML would look like this:

```
<!DOCTYPE html>                       <html class="no-js" lang="">                           <head>                                 <meta charset="utf-8">                                 <meta http-equiv="x-ua-compatible" content="ie=edge">         <title></title>                                 <meta name="description" content="">                           <meta name="viewport" content="width=device-width, initial- scale=1, shrink-to-fit=no"> <link rel="stylesheet" href="css/main.css"></head>                           <body>                                 <p>Hello world! This is HTML5 Boilerplate.</p>               <script src="js/vendor/modernizr-{{MODERNIZR_VERSION}}.min.js>     </script>
```

```
 </body></html>
```

You can view the whole repository here :

[**h5bp/html5-boilerplate**](https://github.com/h5bp/html5-boilerplate)  
[_html5-boilerplate - A professional front-end template for building fast, robust, and adaptable web apps or sites._github.com](https://github.com/h5bp/html5-boilerplate)

In the 1890s, boilerplate was actually cast or stamped in metal ready for the printing press and distributed to newspaper presses and firms around the United States. Until the 1950s, thousands of newspapers received and used this kind of boilerplate from the nation’s largest supplier, the Western Newspaper Union. Some companies also sent out press releases as boilerplate so that they had to be printed as written.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QQnxLRyGkTqHamqONvrftA.png)

Most professional web developers have created a collection of assets and snippets of code that they reuse on projects to accelerate development. There are some universal or near universal patterns that all websites share in common. Rather than continuously rebuild these, most developers start by copying the code they used for a similar project and then start modifying it.

Some developers recognize the value of these boilerplate starter templates and take the time to make the boilerplate more generic and share them online for others to use.

This is not only limited to web development. It is used beyond in AI/ML as there are more growing frameworks and libraries.

#### Necessary characteristics of boilerplate for large projects (production ready)

* Good and Readable Documentation ?
* Code structure with a deeper abstraction level
* Follows Proper Coding Standard
* Has CLI tool (for rapid prototyping and setup)
* Scalable ?
* Easy testing tools
* Necessary API modules
* Support for Internationalization and Localization ?
* Code Splitting
* Server and Client code for setup
* Proper Navigation and Routing Structure ?

After all these minimum specs, you should start editing and altering the code in order to build your project.

There are some Big Tech Companies who even build their own boilerplate. They use it for respective and similar projects throughout time.

A perfect example for this would be react.js’s boilerplate:

[**react-boilerplate/react-boilerplate**](https://github.com/react-boilerplate/react-boilerplate)  
[_react-boilerplate - :fire: A highly scalable, offline-first foundation with the best developer experience and a focus…_github.com](https://github.com/react-boilerplate/react-boilerplate)

#### Boilerplate for smaller projects(Scaffolding)

These type of boilerplates are generally kind of “Starter Kits” or in professional way it is called “Scaffolding”. Their main target users are novice developers or new early adopters.

It focuses on fast prototyping by creating the elements which are necessary only for new projects. These require less functionality and are not scalable over time and project.

Their code structure is not much expanded, and doesn’t involve deeper abstraction layer as users only need to build core features. This eliminates the need for extra utilities.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lfaRa-3SmkzcN2cuy3MCYw.png)
_Code structure_

The simplest example is Facebook’s create-react-app boilerplate:

[**facebookincubator/create-react-app**](https://github.com/facebookincubator/create-react-app)  
[_create-react-app - Create React apps with no build configuration._github.com](https://github.com/facebookincubator/create-react-app)

### What’s the difference between a boilerplate and a template?

As [Joachim Pense](https://www.quora.com/profile/Joachim-Pense) clearly states, **boilerplate** is something that you copy and paste and just add to a document. It comes up most often in contracts where language is used and reused, spelling out things like conditions and caveats.

Writers use **templates as models**, sometimes with negative effects. In broad terms, a template is a model or pattern used to create new objects. In writing, it is a **standardized form of something like a resume** that writers can use to flesh out their own versions.

Unlike boilerplates, templates are adapted for a particular use. The problem arose for me when students used Word templates for their resumes, and they all ended up looking the same.

Both templates and boilerplates can make business writing stilted and artificial if used unwisely.

### Style Guide for writing code

Regardless of whether you’re using boilerplate or not, there are some standards followed by companies for writing code . One of them is **Style Guide.** It attempts to explain the basic styles and patterns that are used in various companies or organizations. It’s generally a rule that employees must adopt the coding style guide of their company.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHZwgapkhk1bMWHilZa6vw.png)

The Style Guide describes tons of rules for writing code, like indentation of tabs and spaces, naming of variables and functions, writing necessary comments, formatting, source file structures, using proper method of data structures, avoiding hoisting, scoping, control statements and a lot more.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hxP11Dbe9ksYpK5c8_nU3g.png)

Programming styles commonly deal with the visual appearance of source code with the goal of readability. Software has long been available that formats source code automatically, leaving coders to concentrate on naming, logic, and higher techniques.

As a practical point, using a computer to format source code saves time, and it is possible to then enforce company-wide standards without [debates](https://en.wikipedia.org/wiki/Flaming_(Internet)#Holy_Wars). (Source — Wiki).

These are some common debates like: **Tabs v Spaces Holy war**, **choosing the perfect Code IDE**, and so on. The interesting thing is that you can get involved in these debates which mostly happen on [**Reddit**](https://www.reddit.com/r/programming/comments/2ban9r/the_great_white_space_debate/)**.** You can also participate in some of the [**stackoverflow**](https://stackoverflow.com/) Q&A’s.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rjETUMQ62xAZegCSAglE6Q.png)
_source — [https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/](https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/" rel="noopener" target="_blank" title=")_

For web developers, the most common style guide for JS is **Airbnb’s javascript style guide.** It’s open source and everyone can contribute.

[**airbnb/javascript**](https://github.com/airbnb/javascript)  
[_javascript - JavaScript Style Guide_github.com](https://github.com/airbnb/javascript)

If anyone is in doubt as to why Javascript needs a style guide, then read this issue’s second answer by [Harrison Shoff](https://twitter.com/hshoff), who is programmer at **Airbnb** .

[**Why does JavaScript need a style guide? · Issue #102 · airbnb/javascript**](https://github.com/airbnb/javascript/issues/102)  
[_One of my favorite parts about the JavaScript community is that people choose to write it in so many different ways…_github.com](https://github.com/airbnb/javascript/issues/102)

Here are some style guides for some of today’s more popular languages:

[**DotNet Code Formatter**](https://github.com/dotnet/codeformatter)

[**Java: Google-Java-Format**](https://github.com/google/google-java-format)

[**Javascript Standard Style**](https://standardjs.com) **(different from airbnb’s javascript)**

[**PHP Coding Standards Fixe**r](http://cs.sensiolabs.org)

[**Python: Google’s YAPF**](https://github.com/google/yapf/)

[**Ruby: Rubocop**](http://rubocop.readthedocs.io/en/latest/)

#### More from Boilerplate: Concept for OOP

In [object-oriented programs](https://en.wikipedia.org/wiki/Object-oriented_programming), classes are often provided with methods for [getting and setting](https://en.wikipedia.org/wiki/Mutator_method) instance variables. The definitions of these methods can frequently be regarded as boilerplate.

Although the code will vary from one class to another, it is sufficiently stereotypical in structure that it would be better generated automatically than written by hand.

For example, in the following [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) class representing a pet, almost all the code is boilerplate except for the [declarations](https://en.wikipedia.org/wiki/Declaration_(computer_science)) of _Pet_, _name_, and _owner_:

```
public class Pet {    private String name;    private Person owner;
```

```
public Pet(String name, Person owner) {        this.name = name;        this.owner = owner;    }
```

```
public String getName() {        return name;    }
```

```
public void setName(String name) {        this.name = name;    }
```

```
public Person getOwner() {        return owner;    }
```

```
public void setOwner(Person owner) {        this.owner = owner;    }}
```

Boilerplate definition is becoming more global in many other programming languages nowadays. It comes from OOP and hybrid languages that were once procedural but have become OOP. They now have the same goal of repeating the code you build with a model/template/class/object, so they adopt this term. You make a template, and the only things you do for each instance of a template are the individual parameters.

This part is what we call boilerplate. You simply re-use the code you made a template of, but with different parameters.

#### Boilerplate as an API

Since you’re simply re-using the template code with different parameters, this implies that we could build reusable API’s that only need a change of inputs and outputs.

### Conclusion

“Boilerplate code” is any seemingly repetitive code that shows up again and again in order to get a result that seems like it ought to be much simpler.

I wrote this article because I was recently instructed by a Team Lead to learn about the many varieties of boilerplate that might be suitable for our project. So I had to go on a search for the perfect boilerplate.

Any type of feedback will be appreciated! Hustle On!

