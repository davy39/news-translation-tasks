---
title: How to change the state of a child component from its parent in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T19:12:01.000Z'
originalURL: https://freecodecamp.org/news/react-changing-state-of-child-component-from-parent-8ab547436271
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Zpf89dyMkJnfprjM
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Johny Thomas

  We will be building a simple React app which shows the real name of a superhero
  on a button click.

  Let’s get started.

  First, we will create a Superhero component with a name attribute in state. This
  component will render that name fir...'
---

By Johny Thomas

We will be building a simple React app which shows the real name of a superhero on a button click.

Let’s get started.

First, we will create a `Superhero` component with a `name` attribute in state. This component will render that `name` first.

![Image](https://cdn-media-1.freecodecamp.org/images/dXk6uX7LQOfLuMWqTAqOZSd7obn-GESaMUkA)

Now let’s create a function `changeName()` in the `Superhero` component. This function will change the name in state to the actual name of the superhero.

![Image](https://cdn-media-1.freecodecamp.org/images/-3-r39-jq60PNryomLCF7ShV4sHJEOhBBDtl)

Now we have the `Superhero` component which shows the superhero name and a function which updates the name to his real name.

The complete Superhero component will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/yHRO4tad52gX20O9uRC38b-oSgiRe5VK9f6m)

Now let’s create the `App` component which will render this `Superhero` component and a button. When we click the button it shows the real superhero name.

![Image](https://cdn-media-1.freecodecamp.org/images/vlplStkM5jX8jKzIgUuOZB3ezux7mORUNvMy)

We have added a function `handleClick()` which will get called when the user clicks the button. We need to figure out a way to update the state of the child component, that is the `Superhero` component.

We have created a function `changeName()` in the `Superhero` component. This function will show the real name of the superhero. If we can call this function from the `App` component, our work is done. So we will call this function.

Here is where **refs** come to our rescue.

Let’s create a ref of the `Superhero` component in the `App` component. Here is the code for doing that.

![Image](https://cdn-media-1.freecodecamp.org/images/gYY7kDmcNbMT1flktY70lOgXYmqRZAjRErUN)

Here we have created a ref using `React.createRef()` method and attached the ref to the `Superhero` component using the `ref` attribute.

Now we will be able to refer the `Superhero` node using `this.superheroElement.current`. We will also be able to call the `changeName()` function in the `Superhero` component using `this.superheroElement.current.changeName()`.

Let’s update our `handleClick()` function in our `App` component to call the `changeName()` function.

Our `handleClick()` function will look like this.

![Image](https://cdn-media-1.freecodecamp.org/images/Qx7hBSPn7YlzdtGpDSC7Dcr4bP6wR5CKGFOr)

You can check out the complete code in the below sandbox.

[**CodeSandbox**](https://codesandbox.io/embed/4r16r1oxj4)  
[_CodeSandbox is an online editor tailored for web applications._codesandbox.io](https://codesandbox.io/embed/4r16r1oxj4)

Now we have learned how to update the state of a child component from a parent component ?. I hope this was helpful.

