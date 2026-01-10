---
title: How to develop your React superpowers with the Render Props Pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-24T19:02:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-your-react-superpowers-with-the-render-props-pattern-b74e68c6d053
coverImage: https://cdn-media-1.freecodecamp.org/images/0*SkjBUognKSY8KiNG
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eduardo Vedes

  Hey everybody! This time I’m going to tell you about this great superpower called
  “render props”.

  The term “render prop” refers to a technique for sharing code between React components
  using a prop whose value is a function.

  The conc...'
---

By Eduardo Vedes

Hey everybody! This time I’m going to tell you about this great **superpower** called **“render props”**.

The term **“render prop”** refers to a technique for sharing code between React components using a prop whose value is a function.

The concept involved is also known as **“children as a function”** or **“child as a function”**. The components that implement this pattern can be called **“render prop components”**.

This is one of the advanced patterns in React that is a must to master in your daily life as a programmer.

So, I hope your JavaScript is in shape because this is an awesome, super cool pattern to implement!

Let’s get started:

![Image](https://cdn-media-1.freecodecamp.org/images/G3S9a2SFCGj1WJku6iQOXr2U1RzOpBvr1AT6)
_Temperature component_

What do we have here ?? Let’s decode!

We have a component that receives children as a prop (it destructures it from props) and returns it as a function, with arguments. Here, children are returned with the integer 30.

Just to make sure we are on the same page, the code above is the same as writing:

![Image](https://cdn-media-1.freecodecamp.org/images/m1VCbXfI6k411uj9oiMyUsgJ5quZgrgXjAv9)
_Temperature component receiving generic props_

Or in a more elaborated class Component:

![Image](https://cdn-media-1.freecodecamp.org/images/UjXx9CvadH2O2UBQEa6MCXzRG3luRLBDP-t2)
_Temperature class component example._

OK! Let’s get back to where we were coming from.

To invoke this component we write a function as children:

![Image](https://cdn-media-1.freecodecamp.org/images/ezNH-u5L4kntGNE3TT2F8ab6c4gDnbxg8udS)

Okay, let’s improve the code a bit.

![Image](https://cdn-media-1.freecodecamp.org/images/vJ3jNJGa-4dFN-Uz-e-poU7U3JSdsFLRec05)
_Temperature and main App component_

I always use a little bit of bootstrap styling to make my examples simple, clean and a little bit polished.

Keep in mind that children are whatever exists inside the <Temperature> </Temperature> invocation.

The Temperature component is totally transparent about what children are, it just renders them passing 30 as an integer.

So the result we have in the browser is this:

![Image](https://cdn-media-1.freecodecamp.org/images/Qiml1WaNrlpdyKIExuzDlWK3PjTo6vqd296V)
_render of the components_

Let’s say something about the weather! ?

![Image](https://cdn-media-1.freecodecamp.org/images/qhL9Wvw-4BLdVpJ8zJDCHxZl5bYFrePZenNU)
_function to say something about the weather_

![Image](https://cdn-media-1.freecodecamp.org/images/wrjNkS4582AgA0Q7CyeF-M5zpqX4nYSELxor)
_My brain is melting!!!_

Okay! Nice feature you say!

But why is this a nice feature? Let’s keep your brain cool! ?

We have separated the controller from the view! Now we have a component called Temperature which is able to receive temperatures from an API “far far away” and render its children, whichever they are, passing the temp value into them.

Make sure you understand this great benefit and superpower! The temperature Component doesn’t know its children in advance. It only knows that independent of the children it will render them and pass them the temperature value.

Of course we could make use of composition and encapsulate the children logic into another component, for example the ShowTemperature in Celsius.

Let’s do it.

![Image](https://cdn-media-1.freecodecamp.org/images/3tymqxQamDuMCADbxZcMgLE6tEgInKkNenlj)
_encapsulate ShowTemperatureInCelsius_

And that’s it! Why is this kewl? Because now I’m going to reuse the same thingies and do a ShowTemperatureInFahrenheit!

![Image](https://cdn-media-1.freecodecamp.org/images/O3Hrc8R-rsZw-VyFyPPDQjmURIkakRiforfS)
_ShowTemperatureInFahrenheit and App Component refactoring_

Yeah! That’s so nice! We’ve encapsulated the render stuff into components using composition. We could keep going making a new ShowTemperature component to be invoked inside ShowTemperatureInCelsius or ShowTemperatureInFahrenheit.

![Image](https://cdn-media-1.freecodecamp.org/images/QKg5UuoS3onEzVo9c2LScbJELTMOLjKRlA3t)
_My brain is melting and my brain is not melting at the same time! This is Quantum Physics!_

But if we want to apply the render props pattern again to show different colors that we get from user preferences, for example?

Let’s try it.

![Image](https://cdn-media-1.freecodecamp.org/images/cFXHJgi8f3TzdZQE5tGoWGkX7TrPTmcF3Jsb)
_Colors component_

![Image](https://cdn-media-1.freecodecamp.org/images/0VVn4YeeD7n7Zd35n5H5R7Btcsx0hci0IndL)
_Temps is red or temp is black ?_

Okay mates, this is a great tool but… “With great power comes great responsibility”.

If we do one or two more render prop components we’ll deep dive into a callback hell sooner than we might expect!

When we need to extract something or get some other props that come mixed in in the React cascade flow, we’re going to start to get confused and the code will become messy and not explicit or declarative anymore.

So…how can we avoid this?

Well… maybe you already thought of this. Render props is very similar in purpose to HOC (Higher Order Components).

Actually, we can use one or the other for almost the same purpose. A lot of ink has already been spent on that subject.

If you don’t know anything about HOCs, you can read my article about the container pattern [here](https://medium.freecodecamp.org/react-superpowers-container-pattern-20d664bdae65) where I show you how to do a simple HOC.

I promise to write an article about HOCs in the nearly future, because it’s also a pattern that deserves some attention.

So, just as a test let’s evolve our Color abstraction to a HOC:

![Image](https://cdn-media-1.freecodecamp.org/images/3yEmQhNe-WaHeS-k6Aou3GMPrLCtm8SDFVcj)
_withColor HOC (Higher Order Component)_

Nice! The same result! We’ve done a Javascript function that receives a Component and returns a class which renders the WrappedComponent with the desired prop we can get somewhere else!

This is kind of a silly example but I think it helps point out the difference between these two patterns.

So… when should you use the former or the latter?

Well, everything comes with a cost. I’d dare say that I find HOC to be much cleaner than render props.

The problem is that HOCs cut the composition flow a little that makes React so great. Also in some circumstances they aren’t so performant and they tend to trigger more renders in your components — so beware of this caveat.

As a rule of thumb, I usually try to use render props because it’s a win-win pattern that prioritises composition.

If you find that you’re falling into a callback hell, then switch to HOC as a second step.

If you know, for instance, React Router, you easily have the feeling why **withRouter** is an **HOC** and **<Switch/> or <Router/>** are render props components. It depends a lot in which context you’re working and how you want the code to be expressive and fluid.

If you don’t know React Router, keep everything I told you in mind. Then, while you’re writing some code, try these patterns until you decide easily which is better according to the context or objective.

Last but not least, you can play a little bit around with the code in my GitHub repo [here](https://github.com/evedes/renderprops-pattern).

And that’s it everybody! ? ? I hope you’ve enjoyed this small introduction to render props. For more information please check the Bibliography below!

### Bibliography

1. [React Documentation](https://reactjs.org/docs/getting-started.html)
2. [reactpatterns.com](https://reactpatterns.com)

Thank you very much!

evedes, Nov 2018

