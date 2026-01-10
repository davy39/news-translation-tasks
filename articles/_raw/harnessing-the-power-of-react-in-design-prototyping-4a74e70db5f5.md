---
title: Harnessing the power of React in design prototyping
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T05:32:49.000Z'
originalURL: https://freecodecamp.org/news/harnessing-the-power-of-react-in-design-prototyping-4a74e70db5f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vXbwcj_3ZK_oVij0DIFQtg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Linton Ye

  An interview with Jack Hallahan, a designer who uses React


  In today’s sea of design prototyping tools, React might be an unintuitive choice.

  The process of creating a prototype is supposed to be fast and visual. After all,
  the purpose o...'
---

By Linton Ye

#### An interview with Jack Hallahan, a designer who uses React

![Image](https://cdn-media-1.freecodecamp.org/images/08Oq80eS4XQHZdq4MrbXpuqFtpHhsDzjNzFb)

In today’s sea of design prototyping tools, React might be an unintuitive choice.

The process of creating a prototype is supposed to be fast and visual. After all, the purpose of creating prototypes is to spend as as little time as possible testing different design options before making a decision. Conventionally, coding (and therefore React) is considered slow and difficult as a prototyping tool.

Jack Hallahan is a product designer based in London, UK. He’s one of the designers who knows how to harness the power of code to streamline their design processes.

Intrigued by Jack’s inspiring [post](https://medium.com/geckoboard-under-the-hood/react-js-for-design-prototyping-ec29cfa81b0f), I emailed him and wanted to know more. Jack was nice enough to have a chat with me, which I can’t wait to share with you!

Here’s what we talked about:

* How did Jack learn React as a designer? What were his biggest struggles?
* When is a good time to use React for design prototyping?
* Why is React the right tool? How does it compare to visual prototyping tools?
* What React related tools does he use in his design process?
* Jack’s suggestions to designers on how to learn React

Interested in hearing the story of a fellow designer? Keep reading ?! My questions are i_talicized._ Jack’s responses follow in regular type.

### On Using React As a Design Prototyping Tool

#### Finding the right prototyping tool

**_Linton:_** _How do you use React in your workflow? What’s the story behind using React as a prototyping tool?_

**Jack:** Something that we’ve struggled with for a while at our company is finding the right prototyping tool for the sort of work that we’re doing.

Many user experiences are more-or-less a linear user journey. An example is an onboarding flow, checkout, or account registration. There may be small decisions along the way, but they can be handled by prototyping for a “happy path” and then considering edge-cases. We can use tools like Marvel to make it quite high fidelity and test that with users.

However, what I needed to prototype was not a linear user journey.

#### Prototyping a non-linear user journey

Our product is a business tool that allows customers to get their data from their business, for example their sales team performance data. It then creates a visual dashboard to put up on the TV in the office so that everyone can see the data all the time.

People use it to design data visualizations and to design dashboards. There are a lot of options that a user might have to go through in order to get the data they need and configure it in the right way to be viewed. It also has to handle data. Data come in different shapes and sizes. If we design a new data visualization, it has to be robust enough to handle different types of data, different schemas, different numbers from one digit to six digits.

**Configuring a data-visualization is an example of a non-linear path.** There are many options, all of which can be chosen in different combinations. Every combination will result in a different visualization. Seeing the preview of the chart change is a visual confirmation that the user’s decisions are having the intended effect. Because the outcome is very visual, a lower fidelity would not have been able to validate as thoroughly.

There wasn’t really a tool that allowed us to prototype **a complete user journey**. I have also tried prototyping this with Axure RP in the past, which allows for some conditional logic, however it soon got out-of-hand.

I put aside other tools and invested my time into building something in React, and it really paid off.

For me, the advantage of React is that it fills a gap that we had in our prototyping toolkit. **That gap was interfaces that allow you to configure something in a non-linear way, and interfaces that handle data**.

#### Example prototypes

_Can you give us some examples of non-linear user journies?_

The first prototype was used to test the interaction design with users, as well as validating the options available to users: could they create a theme that suited their brand?

Configuring a theme wasn’t a linear journey. It needed to be quite visual. It’s high fidelity because it introduced some new interaction patterns we needed to be confident about. Because the outcome is very visual, a lower fidelity would not have been able to validate as thoroughly.

![Image](https://cdn-media-1.freecodecamp.org/images/BXVH-kAeHZ60dBkFoPlyklzSBFRZKEQzuw-E)

Another example is this table widget prototype. It is high fidelity only in the table visualization. The form on the left is more-or-less un-styled. In fact the table is very similar to the markup and styling used to create the same thing in our production code. The prototype was create to figure out those things in detail — alignment, padding, hover states, font sizes, truncation, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/Cf0pV3GmhGMaKzCSt2Co2gws1HwWuMETr95g)

#### Why is React the right tool?

**Managing multiple paths and handling data are the natural power of code.**

Because React is JavaScript, if you want to make changes to the way that data is displayed, like doing some rounding or if you want to sort it, you can do that. You can’t do that in simple visual tools.

[With visual tools] If you want to create a prototype to test the experience of doing something such as sorting the table, you have to create a couple of screens that look like the user flow and hope that the user’s going to click on the right button. If they don’t, you’d have to say, oops, sorry, we didn’t design that bit, let’s just get back to the right path.

In comparison, React allows me to create more robust prototypes to handle data with a complete user journey. The user could explore different options, rather than just an on-rail experience where the user has to click the right button every time.

One of those things is the idea of a component having state. The app knows the current state that it’s in, and you can do something to the interface to update the state. And then that state can be passed down to children. You can update a component over here by clicking something over there very easily. And then you can go back and undo it and it doesn’t affect the things down the line.

**High-fidelity prototypes by default**

Fidelity is something you get by default when prototyping with code. Of course your button may not be styled until you add CSS, but even an un-styled button element looks and works like a button in the browser. It looks real and works as expected because it is real. You get things like cursor: pointer, hover and active states, the ability to highlight and copy text, real form elements like fields you can type in and radio buttons you can toggle, all without having to draw them or style them in any way.

In the end, we had something that was close to a finished experience. We had all the logic to handle someone changing the color or uploading a logo. And the interface was able to be in any state in any time and not be broken. So I could test it with users without worrying about going to some sort of broken state and trying to recover from that.

#### Comparison with visual prototyping tools

_Do you use other prototyping tools? When do you use them?_

Yes, I create lower-fidelity static sketches before moving to React. Typically I would sketch on paper and also make some quick images in Sketch, possibly even using a tool like Marvel to string them together. I can explore more ideas and make changes faster in these tools — they are better for “divergent” design, and React is best for “convergent” design — no longer exploring but rather deciding, validating, and iterating.

_Can you comment on the speed of creating prototypes in React compared to visual prototyping tools?_

React has a fairly steep learning curve, but it can be surprisingly quick once you get the hang of it. However it’s simply overkill for a lot of prototypes and I wouldn’t recommend it for things that other tools can do well. I find it enjoyable to spend an afternoon coding and considering the fidelity and “robustness” of the prototypes like those above. I think it’s pretty fast!

#### Workflow

_How does the developer handoff happen after the prototypes you create are approved?_

We don’t have a concept of handoff here. Our workflow is agile with design and dev closely coupled. Our engineers are used to dealing with design concepts in many different formats, sometimes static mockups, detailed prototypes, or just sketches. It really depends on the work. We break down the design in planning to uncover anything that needs further exploration, and we often “pair” together to implement a design.

_Do the devs directly use your components, or write the code from scratch, or somewhere in-between?_

No, none of my code is used in our production app. When building a prototype I don’t need to worry about maintainability, reusability, or scalability. The code is bad, basically, but it does the job I need it to do. Our frontend app is complex with Redux, tests, component APIs, etc. It’s not worth trying to use my code for that job.

#### React related tools

_What React related tools are you using in your design process?_

[**create-react-app**](https://github.com/facebook/create-react-app)

![Image](https://cdn-media-1.freecodecamp.org/images/yTsTuWbCFXr8VMloSZj02o-w5HkvWYWxRD5y)

The number one tool that helped me get off the ground with React was Facebook’s create-react-app. The startup boilerplate app that is just ready to go, pre-configured, and has lots of great features built in.

Before that, it was difficult to find a good template project on Github to start with. I didn’t know what was good, what I needed, and what I didn’t need. Things like Webpack were a complete mystery to me, and still are. So create-react-app was so easy. It had a lot of great things built in and it’s just gotten better at the time.

The other thing that comes along with create-react-app is a quick way to share to GitHub pages. Since it’s all hosted for free, I can very easily get a URL, send it to my colleagues, and they can access it or send it to users who might be on the other side of the world.

Apart from that, I’ve installed things like Lint and a prettier in my code editor which just helps to keep things neat and easy to look for errors, and the React Chrome extension tool.

[**Tachyons**](http://tachyons.io/) **for styling**

![Image](https://cdn-media-1.freecodecamp.org/images/lnPIMFd-L3UXldLwnSgdo-3qLh3XFOi3Fb0c)

Tachyons is a different approach to CSS than what most people are used to. It’s been called functional CSS or atomic CSS. Basically it’s a library of classes that have a very specific purpose like applying one single style.

It creates this design-as-you-go mindset. You’re more or less writing inline styles — saying “I want the font to be big, and the corners to be rounded. I want it to have a shadow and the background to be green.” You don’t have to go and give it a semantic name and then go and write a bunch of styles that match up to that element. If you’re confident with how CSS works, it just cuts down the amount of juggling that you have to do to get something styled.

[**React Storybook**](https://github.com/storybooks/storybook)

![Image](https://cdn-media-1.freecodecamp.org/images/cSJ7nmA6QbfSPL7yqbiNUfexSKi3v-1DuhEH)

We use React Storybook as a component library. It’s a shared resource between design and development. We’re continuing to improve it, but I can already see how Storybook can be a great bridge for designers and front-enders working on a React app.

At the moment, when we’ve designed a component we want to reuse, it will be added to Storybook by an engineer. We can then refer to Storybook when designing new interfaces. We can check what components we have that are ready to use, which ones might need changing, and discover if we need to design and build something new.

In the future, it would be great to have Storybook as a source-of-truth for both designers and the front-end team. We could use React-Sketchapp to have a version of each component that can be used by designers in Sketch. I haven’t had a chance to properly try React-Sketchapp. The Airbnb design team is doing some amazing work, but we’re not yet at the scale where this becomes crucial.

### On Learning React as A Designer

_How did you learn React? Did you have any prior programming experience?_

I have been working in digital design for a while. I have obviously become pretty familiar with HTML and CSS. I’ve been building websites and basic things for a long time. JavaScript is something that I had often flirted with, but I had never quite jumped in the deep end. I’ve used a little bit of jQuery, but for the most part it was a mystery.

We have an innovation day every two weeks. Anyone in the product and engineering team can use that time to work on a personal project that’s not usual project work. So, it’s a great opportunity to level up and broaden my skill set.

I started off doing a couple of JavaScript tutorials through Codecademy to get my head around some of the basics. And the reason I looked at React was more curiosity than anything. The engineers were using it. I had been learning about some of the core concepts, such as components and state. I went searching for a few tutorials and I’m working my way through a couple of little projects, following blog posts for the instructions. Eventually I started to figure out how it was working.

Once I had those very basic concepts done, I tried to use them to build real projects. That led me to learn more and become a bit more confident with it.

_What were the biggest struggles when you were learning React and how did you overcome them?_

The React ecosystem is notoriously complex. It can be hard for a beginner to create a safe place to experiment without battling the build tools constantly. I spent ages trying to find the right starter project, but I didn’t really know what I was looking for. A colleague pointed me at create-react-app when it was gaining some traction, and from that point I’ve relied on it for all my React projects.

I think most folks will stumble over JSX from time to time, I still do if I’m switching between React and html for different projects. I haven’t found any tricks here — you just need to memorize the differences, but luckily there aren’t too many.

It took me a while to build the right mental model about how React works and fits together. And the fact I was almost a complete beginner with JavaScript didn’t help. It was as though small bits were becoming clear but there were still too many gaps to see the big picture. I remember struggling for a long time to make a child component update its parent’s state.

Even now I would still consider myself a beginner — I would have to Google even basic things. But I’m better at knowing what to google to find the answers, and how the new knowledge will fit with the things I’m more familiar with.

_When learning a new technology, an important milestone is knowing what to google and what questions to ask. From that point on, learning tends to become self-reinforcing. Everything you learn in the process will build up your new foundation to learn the next concept. But to get to that point, you’d need to learn enough of the basics to get around._

_It’s a lot like learning a new (human) language, you’d need to know the alphabets and build up enough vocabulary. Then, you can start looking up words in a dictionary, reading and talking to people from which you’ll learn new words and new expressions._

_The initial effort might seem tedious but it’s a must. The good news is that you’ll know it when you get there, like Jack did. Helping you overcome the initial hurdles is also my main goal when creating the React course for designers at [learnreact.design](https://learnreact.design/?utm_source=medium&utm_campaign=jack-interview&utm_content=middle)._

_Any suggestions to fellow designers on learning React or learning to code in general?_

You can read as many tutorials as you want. You can do a class or watch a video, but unless you actually try to build something on your own, you’re not really gonna get the pieces together in your mind. So it started clicking for me when I started building things that were beyond the tutorials.

Take what you’ve done in a tutorial or a class, add something to it. Or think of something that might have some similarities to what you’ve just been learning. If the example was a product profile on an e-commerce website, then you can try to create a user profile on a social network. You can do that in React and think about the sort of things that would need to go into that interface. Just start from scratch and build it yourself. And that’s where you realize what you know and what you don’t know.

As you get better, as you learn more, you’ll also learn how to solve the problems that you’re going to encounter more easily.

So when you first start out, you’ll see console errors and you have no idea what they mean or how to fix them, it’s very scary and you need someone to hold your hand. But at some point, you stop being scared by an error and you think, “OK, I don’t know what this is now, but I know what to google to figure out how to fix it”. Or, “I roughly know where it is in the app that it’s happening, so I’ll go and try to debug it”.

You learn how to fix your errors and if you want to do something new, you learn the path that you might take to get there. I struggled, to begin with. But by building real things, I got to that point where I was more able to be self-reliant in solving my own problems and learning the next thing.

### Final Note (from me, not Jack)

I’m really impressed and inspired by Jack’s drive to explore and use whatever tools he has to solve design problems at hand. With this mindset, he was not afraid to enter new territories and pick up new tools along the way.

Personally, I think every designer should have this attitude towards new technologies. No matter if it’s React, blockchain, or voice-based interfaces. We should be open to experiment with them and be ready to embrace them in our design process.

What do you think? Let me know in the comments!

_I’d like to thank Jack for his time chatting with me, and providing high quality answers to my endless follow-up questions (so that I could just copy and paste ?)!_

Don’t forget to check out my React course tailored for designers: [learnreact.design](https://learnreact.design/?utm_source=medium&utm_campaign=jack-interview&utm_content=bottom). ?

