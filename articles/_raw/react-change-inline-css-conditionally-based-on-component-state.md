---
title: React - Change Inline CSS Conditionally Based on Component State
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/react-change-inline-css-conditionally-based-on-component-state
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a95740569d1a4ca267a.jpg
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'If you''re having trouble with freeCodeCamp''s Change Inline CSS Conditionally
  Based on Component State challenge, you''re probably not alone.

  In this challenge, you need to add code to change some inline CSS conditionally
  based on the state of a React ...'
---

If you're having trouble with freeCodeCamp's [Change Inline CSS Conditionally Based on Component State](https://www.freecodecamp.org/learn/front-end-libraries/react/change-inline-css-conditionally-based-on-component-state) challenge, you're probably not alone.

In this challenge, you need to add code to change some inline CSS conditionally based on the state of a React component.

When you first go to the challenge, here's the code you'll see:

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line

    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};

```

Notice that an inline style object, `inputStyle`, has already been declared with some default styling.

Your goal in this challenge is to update `inputStyle` so the border of the input is `3px solid red` when there are more than 15 characters in the input. Note that the text in the input box is saved in the component's state as `input`:

```jsx
...
this.state = {
  input: ''
};
...
```

## Close, but not quite

Imagine that, after reading the description and instructions, you come up with this:

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    if(this.state.input > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

But when you try to submit this, it doesn't pass all the tests. Let's take a closer look at what's going on.

## Solutions

### Using an `if` statement

Declaring `char` is fine, but take a closer look at the `if` condition:

```jsx
if(this.state.input > char) {
  inputStyle = {
    border:'3px solid red'
  }
}  
```

Remember that `this.state.input` is the value of the input box and is a string. For example, it could be "testing testing 1, 2, 3".

If you enter "testing testing 1, 2, 3" into the text box and lot `this.state.input` to the console:

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    console.log(this.state.input);
    if(this.state.input > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

You'll see `testing testing 1, 2, 3` in the console.

Further, if you log `this.state.input > char` to the console, you'll see that it evaluates to `false`:

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    console.log(this.state.input > char);
    if(this.state.input > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

Simply put, you can't compare a string (`this.state.input`) directly to `char`, which is a number.

Instead, call the `.length` on `this.state.input` to get the length of the string and compare that to `count`:

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    if(this.state.input.length > char) {
      inputStyle = {
        border:'3px solid red'
      }
    }  
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};
```

Since the length of the string "testing testing 1, 2, 3" is 23 characters long (including spaces and commas), the border of the input box will turn red:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-53.png)

### Using a ternary operator

A [ternary or conditional operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) is like a one line `if...else` statement, and can help shorten your code significantly.

Go back to your solution and remove everything except the `char` variable:

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line

    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};

```

Now take the condition you used in your earlier `if` statement and use it as the first part of the ternary condition: `this.state.input.length > char ?  :  ;`

Everything between `?` and `:` indicates what happens if the earlier statement is true. You can just copy the code that was inside your `if` statement before: `this.state.input.length > char ? inputStyle = { border:'3px solid red' } :  ;`

Now you need to handle the `else` portion of the ternary operator, which is everything between `:` and `;`. 

While you didn't use an `else` statement in your first solution, you effectively used `inputStyle` as-is. So just use `inputStyle` the way it's declared earlier in your code: `this.state.input.length > char ? inputStyle = { border:'3px solid red' } : inputStyle;`

Your whole solution should look like this:

```jsx
class GateKeeper extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      input: ''
    };
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ input: event.target.value })
  }
  render() {
    let inputStyle = {
      border: '1px solid black'
    };
    // change code below this line
    const char = 15;
    this.state.input.length > char ? inputStyle = { border:'3px solid red' } : inputStyle;
    // change code above this line
    return (
      <div>
        <h3>Don't Type Too Much:</h3>
        <input
          type="text"
          style={inputStyle}
          value={this.state.input}
          onChange={this.handleChange} />
      </div>
    );
  }
};

```

And that's it – you should be able to pass the challenge! Now go forth and conditionally style React components to your heart's content.

