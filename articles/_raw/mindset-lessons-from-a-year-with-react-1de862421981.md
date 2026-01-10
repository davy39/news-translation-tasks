---
title: The most important lessons I’ve learned after a year of working with React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-30T16:36:41.000Z'
originalURL: https://freecodecamp.org/news/mindset-lessons-from-a-year-with-react-1de862421981
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TheYckj9udF4qLjoJW8sjg.png
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
seo_desc: 'By Tomas Eglinskas

  Starting out with a new technology can be quite troublesome. You usually find yourself
  in a sea of tutorials and articles, followed by millions of personal opinions. And
  every single one states that they found the “right and perfec...'
---

By Tomas Eglinskas

Starting out with a new technology can be quite troublesome. You usually find yourself in a sea of tutorials and articles, followed by millions of personal opinions. And every single one states that they found the **“right and perfect way.”**

This leaves us debating whether our chosen tutorial will be a waste of time or not.

Before diving into the ocean, we must understand the underlying concepts of a technology. Then we need to develop a technology-based mindset. If we are starting to learn React, we first have to think in React. Only later on we can start mixing various mindsets into one.

In this article we’ll be covering some lessons I learned regarding this mindset from my personal experiences with React. We’ll go over the days at work and nights with personal projects and even the talk I gave at a local JavaScript event.

So let’s go!

### React is evolving, so you must be up to date

If you remember the initial announcement of version 16.3.0, you’ll remember how excited everyone was.

Here are some of the changes and improvements we received:

* Official Context API
* createRef API
* forwardRef API
* StrictMode
* Component Lifecycle Changes

The React Core team and all the contributors are doing a great job trying to improve the technology we all adore. And in version 16.4.0 we received [Pointer Events](https://reactjs.org/blog/2018/05/23/react-v-16-4.html).

Further changes are surely coming, and it’s only a matter of time: Async Rendering, Caching, version 17.0.0 and many others not yet known.

So if you want to be at the top, you have to be up to date with things that are happening in the community.

Know how things work and why they are being developed. Learn what problems are being solved and how development is being made easier. It’ll really help you out.

### Don’t be afraid to split your code into smaller chucks

React is component-based. So you should leverage this concept and not be afraid to split bigger pieces into smaller ones.

Sometimes a simple component can be made of 4–5 lines of code, and in some cases, it is totally fine.

Make it so that if a new person jumps in, they won’t need days to understand how everything works.

```
// isn't this easy to understand?
```

```
return (  [   <ChangeButton    onClick={this.changeUserApprovalStatus}    text="Let’s switch it!"   />,   <UserInformation status={status}/>   ]);
```

You don’t have to make components that all have complex logic built-in. They can be only visual. If this improves code readability and testing, and reduces further code smells, it’s a great win for everyone on the team.

```
import ErrorMessage from './ErrorMessage';
```

```
const NotFound = () => (  <ErrorMessage    title="Oops! Page not found."    message="The page you are looking for does not exist!"    className="test_404-page"  />);
```

In the above example, the properties are static. So we can have a pure component which is responsible for the website’s error message `Not Found`, and nothing more.

Also, if you don’t like having CSS classes as class names everywhere, I would recommend using styled components. This can improve readability quite a lot.

```
const Number = styled.h1`  font-size: 36px;  line-height: 40px;  margin-right: 5px;  padding: 0px;`;//..
```

```
<Container>  <Number>{skipRatePre}</Number>  <InfoName>Skip Rate</InfoName></Container>
```

If you’re afraid of creating more components because of polluting your folders with files, rethink how you structure your code. I have been using the [fractal structure](https://hackernoon.com/fractal-a-react-app-structure-for-infinite-scale-4dab943092af) and it’s awesome.

### Don’t stick to the basics — become advanced

You might think sometimes that you don’t understand something enough to move on to the advanced stuff. But often times you shouldn’t worry about it too much — take up the challenge and prove yourself wrong.

By taking up the advanced topics and pushing yourself, you can understand more of the basics and how they are used for bigger things.

There are many patterns which are yours to explore:

* Compound Components
* High Order Components
* Render Props
* Smart/Dumb Components
* many others (try out Profiling)

Explore them all, and you’ll know why and where they are used. You’ll become more comfortable with React.

```
// looks like magic?// it's not that hard when you just try
```

```
render() {  const children = React.Children.map(this.props.children,   (child, index) => {      return React.cloneElement(child, {        onSelect: () => this.props.onTabSelect(index)    });     });   return children;}
```

Also, don’t be afraid to try something new at your work — within certain boundaries, of course! Don’t just experiment on personal projects.

People will ask questions, and that is normal. Your task is to defend your work and decisions with strong arguments.

Your aim should be to solve an existing problem, make further development easier, or just clean some pasta in the code. Even if your suggestions are rejected, you’ll go home knowing more than by sitting silent.

### Don’t over-complicate things

This might sound like a counter argument, but it’s different. In life, and everywhere, we must have balance. We shouldn’t over-engineer to show off. We must be practical. Write code which is easy to understand and fulfills its purpose.

If you don’t need Redux, but you want to use it because everyone uses without knowing it’s true purpose, don’t. Have an opinion and don’t be afraid to stand up for yourself if others push you.

Sometimes you might think that by leveraging the latest technologies and writing complex code you’re saying to the world:  
“I’m not a junior, I am becoming a mid/senior. Look what can I do!”

To be honest, that was my mindset in the beginning of my developer journey. But over time you understand that the code which was written without showing off or because “it works” is easier to live with.

1. Co-workers can work on your projects and you’re not the only person who’s responsible for developing / fixing / testing &**lt;insert tas**k>.
2. The team can understand what others did without sitting through a long meeting. A couple of minutes is enough to discuss.
3. When your colleague goes out for a two week vacation, you can take over their task. And you won’t have to work on it for 8 hours, because it can be done in an hour.

People respect people who make other people’s lives easier. Thus if your goal is to gain respect, move up the ranks, and improve, aim to code for the team and not yourself.

You’ll become everyone’s favorite team player.

### Refactor, refactor and refactor — it’s normal

You will change your mind dozens of times, although the project manager will change theirs more often. Others will criticize your work, and you will criticize it. As a result, you’ll have to change your code many, many times.

But don’t worry, it’s a natural learning process. Without faults and errors we cannot improve.

The more times we fall down, the easier it becomes to get back up.

But here’s a hint: make sure you test your current software. Smoke, unit, integration, snapshot — don’t be shy of them.

Everyone has faced or will face a scenario when a test could have saved precious time.

And if you, like many people, think that they are a waste of time, just try thinking a little different.

1. You won’t have to sit with your colleague explaining how things work.
2. You won’t have to sit with your colleague explaining why things broke.
3. You won’t have to fix bugs for your colleague.
4. You won’t have to fix bugs which were found after 3 weeks.
5. You will have time to do stuff you want.

And these are quite big benefits.

### If you love it, you’ll thrive

Over the previous year, my goal was to get better at React. I wanted to give a talk about it. I wanted others to enjoy it with me.

I could sit all night coding non-stop, watching various talks and enjoying every minute of it.

The thing is, if you want something, somehow everyone starts helping you. And last month, I gave my first React talk to a crowd of 200 people.

During this year period I became stronger and more comfortable with React — the various patterns, paradigms, and inner workings. I can have advanced discussions and teach others about topics that I was afraid to touch.

And today I still feel the same excitement and enjoyment I felt a year ago.

Therefore I would recommend everyone to ask themselves: “Do you enjoy what you do?”

If not, continue looking for that special piece which you can talk about for hours, learn about every night, and be happy.

Because we have to find something that is closest to our hearts. Success cannot be forced, it must be achieved.

If I could go back a year in time, this is what would I say to myself to prepare before the big journey ahead.

Thank you for reading!

If you found this article helpful, ???.

