---
title: The best way to bind event handlers in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T15:52:39.000Z'
originalURL: https://freecodecamp.org/news/the-best-way-to-bind-event-handlers-in-react-282db2cf1530
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2dTkg7JieJTEhRasDst0-A.jpeg
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
seo_desc: 'By Charlee Li

  Binding event handlers in React can be tricky (you have JavaScript to thank for
  that). For those who know the history of Perl and Python, TMTOWTDI (There’s More
  Than One Way To Do It) and TOOWTDI (There’s Only One Way To Do It) should b...'
---

By Charlee Li

Binding event handlers in React can be tricky (you have JavaScript to thank for that). For those who know the history of Perl and Python, TMTOWTDI (There’s More Than One Way To Do It) and TOOWTDI (There’s Only One Way To Do It) should be familiar words. Unfortunately, at least for event binding, JavaScript is a TMTOWTDI language, which always makes developers confused.

In this post, we will explore the common ways of creating event bindings in React, and I’ll show you their pros and cons. And most importantly, I will help you find the “Only One Way” — or at least, my favorite.

This post assumes that you understand the necessity of binding, such as why we need to do `this.handler.bind(this)`, or the difference between `function() { console.log(this); }` and `() => { console.log(this)`; }. If you get confused about these question[s, Saurabh Misra had an amazing p](https://medium.freecodecamp.org/this-is-why-we-need-to-bind-event-handlers-in-class-components-in-react-f7ea1a6f93eb)ost explaining them.

### Dynamic binding in render()

The first case commonly used is calling `.bind(this)` in the `render()` function. For example:

```
class HelloWorld extends Component {  handleClick(event) {}  render() {    return (      <p>Hello, {this.state.name}!</p>      <button onClick={this.handleClick.bind(this)}>Click</button>    );  }}
```

Of course this will work. But think about one thing: What happens if `this.state.name`changes?

You might say that changing `this.state.name` will cause the component to re-`render()` . Good. The component will render to update the name part. But will the button be rendered?

Consider the fact that React uses the Virtual DOM. When render occurs, it will compare the updated Virtual DOM with the previous Virtual DOM, and then only update the changed elements to the actual DOM tree.

In our case, when `render()` is called, `this.handleClick.bind(this)` will be called as well to bind the handler. This call will generate a **brand-new handler**, which is completely different than the handler used when `render()` was called the first time!

![Image](https://cdn-media-1.freecodecamp.org/images/u0GzKJdrXoomFQqomNjOV3UecQV8tHrTj9UM)
_Virtual DOM for dynamic binding. Elements in Blue will be re-rendered._

As in the above diagram, when `render()` was called previously, `this.handleClick.bind(this)` returned `funcA` so that React knew `onChange` was `funcA`.

Later, when `render()` is called again, `this.handleClick.bind(this)` returned `funcB` (note it returns a new function every time being called). This way, React knows that `onChange` is no longer `funcA`, which means that `button` needs to be re-rendered.

One button may not be a problem. But what if you have 100 buttons rendered within a list?

```
render() {  return (    {this.state.buttons.map(btn => (      <button key={btn.id} onChange={this.handleClick.bind(this)}>        {btn.label}      </button>    ))}  );}
```

In the above example, any button label change will cause all the buttons to be re-rendered, since all buttons will generate a new `onChange` handler.

### Bind in constructor()

An old school way is to do the binding in the constructor. Nothing fancy:

```
class HelloWorld extends Component {  constructor() {    this.handleClick = this.handleClickFunc.bind(this);  }  render() {    return (<button onClick={this.handleClick}/>);  }}
```

This way is much better than previous one. Calling `render()` will not generate a new handler for `onClick`, so the `<butt`on> will not be re-rendered as long as the button does not change.

![Image](https://cdn-media-1.freecodecamp.org/images/iTs98nwnYdvxE2fFoO5N1Rzcg-u-cD7LL9g1)
_Virtual DOM for binding in constructor. Elements in Blue will be re-rendered._

### Bind with the Arrow Function

With ES7 class properties (currently supported with [Babel](https://babeljs.io/docs/plugins/transform-class-properties/)), we can do bindings at the method definition:

```
class HelloWorld extends Component {  handleClick = (event) => {    console.log(this.state.name);  }  render() {    return (<button onClick={this.handleClick}/>)  }}
```

In the above code, `handleClick` is an assignment which is equivalent to:

```
constructor() {  this.handleClick = (event) => { ... }；}
```

So once the component is initialized, `this.handleClick` will never change again. This way, it ensures that `<butt`on> won’t get re-rendered. This approach is probably the best way of doing bindings. It’s simple, easy to read, and most importantly, it works.

### Dynamic binding with the Arrow Function for multiple elements

Using the same arrow function trick, we can use the same handler for multiple inputs:

```
class HelloWorld extends Component {  handleChange = name => event => {    this.setState({ [name]: event.target.value });  }  render() {    return (      <input onChange={this.handleChange('name')}/>      <input onChange={this.handleChange('description')}/>    )  }}
```

At first glance, this looks pretty amazing due to its simplicity. However, if you consider carefully, you’ll find that it has the same problem as the first approach: every time `render()` is called both`<inp`ut> will be re-rendered.

Indeed I do think this approach is smart, and I don’t want to write multiple `handleXXXChange` for each field either. Luckily, this type of “multi-use handler” is less likely to appear inside a list. This means that there will be only a couple of `<inp`ut> components that get re-rendered, and there probably won’t be a performance issue.

Anyway, the benefits it brings to us are much greater than the performance loss. Therefore, I would suggest that you use this approach directly.

In case those performance issues becoming significant, I would suggest caching the handlers when doing the bindings (but this will make the code less readable):

```
class HelloWorld extends Component {  handleChange = name => {    if (!this.handlers[name]) {      this.handlers[name] = event => {        this.setState({ [name]: event.target.value });      };    }    return this.handlers[name];    }   render() {    return (      <input onChange={this.handleChange('name')}/>      <input onChange={this.handleChange('description')}/>    )  }}
```

### Conclusion

When doing event bindings in React, we must check very carefully whether the handlers are generated dynamically. Usually this is not a problem when the affected components appear only once or twice. But when event handlers appear in a list, this can results in severe performance issues.

#### Solutions

* Use Arrow Function binding whenever possible
* If you must generate bindings dynamically, consider caching the handlers if the bindings become a performance issue

Thanks for reading! I hope this post was helpful. If you find this post useful, please share it with more people by recommending it.

_Update:_

[Omri Luzon](https://www.freecodecamp.org/news/the-best-way-to-bind-event-handlers-in-react-282db2cf1530/undefined) and [Shesh](https://www.freecodecamp.org/news/the-best-way-to-bind-event-handlers-in-react-282db2cf1530/undefined) mentioned `lodash-decorators` and `react-autobind` packages for more convenient bindings. Personally I am not a big fan of automatically doing anything (I am always trying to keep things such bindings minimal) but auto bind is absolutely a great way of writing clean code and saving more efforts. The code would be like:

```
import autoBind from 'react-autobind';class HelloWorld() {  constructor() {    autoBind(this);  }
```

```
  handleClick() {    ...  }  render() {    return (<button onClick={this.handleClick}/>);  }}
```

Since `autoBind` will handle the bindings automatically, it is not necessary to use arrow function trick ( `handleClick = () =>` {} ) to do the binding, and in t`he rende`r() functio`n, this.handleCl`ick can be used directly.

