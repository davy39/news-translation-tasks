---
title: How to Clear Input Values of Dynamic Form in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-clear-input-values-of-dynamic-form-in-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a92740569d1a4ca2665.jpg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'There''s a lot to consider when working on a React application, especially
  when they involve forms. Even if you''re able to create a submit button and update
  your app''s state the way you want, clearing the forms can be difficult.

  Say your application h...'
---

There's a lot to consider when working on a React application, especially when they involve forms. Even if you're able to create a submit button and update your app's state the way you want, clearing the forms can be difficult.

Say your application has dynamic forms like this:

```jsx
import React from "react";
import ReactDOM from "react-dom";
import Cart from "./Cart";

import "./styles.css";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Items: [
        {
          name: "item1",
          description: "item1",
          group: "groupA",
          dtype: "str"
        },
        {
          name: "item2",
          description: "item2",
          group: "groupA",
          dtype: "str"
        },
        {
          name: "item3",
          description: "item3",
          group: "groupB",
          dtype: "str"
        },
        {
          name: "item4",
          description: "item4",
          group: "groupB",
          dtype: "str"
        }
      ],
      itemvalues: [{}]
    };
    this.onChangeText = this.onChangeText.bind(this);
    this.handleReset = this.handleReset.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.findFieldIndex = this.findFieldIndex.bind(this);
    this.trimText = this.trimText.bind(this);
  }

  onChangeText = e => {
    const valuesCopy = [...this.state.itemvalues];
    //debugger;

    // get data-group value
    const itemvalue = e.target.dataset.group;

    if (!valuesCopy[0][itemvalue]) {
      valuesCopy[0][itemvalue] = [];
    }

    const itemvalues = valuesCopy[0][itemvalue];
    const index = this.findFieldIndex(itemvalues, e.target.name);

    if (index < 0) {
      valuesCopy[0][itemvalue] = [
        ...itemvalues,
        { [e.target.name]: e.target.value.split(",").map(this.trimText) }
      ];
    } else {
      // update the value
      valuesCopy[0][itemvalue][index][e.target.name] = e.target.value
        .split(",")
        .map(this.trimText);
    }

    // console.log(itemsCopy);

    this.setState({ itemvalues: valuesCopy });
  };
  findFieldIndex = (array, name) => {
    return array.findIndex(item => item[name] !== undefined);
  };
  trimText(str) {
    return str.trim();
  }

  handleReset = () => {
    this.setState({
      itemvalues: [{}]
    });
  };

  handleSubmit = () => {
    console.log(this.state.itemvalues);
  };

  render() {
    return (
      <Cart
        Items={this.state.Items}
        handleSubmit={this.handleSubmit}
        handleReset={this.handleReset}
        onChangeText={this.onChangeText}
      />
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));

```

```jsx
import React from "react";
import Form from "./Form";

const Cart = props => {
  return (
    <div>
      <Form Items={props.Items} onChangeText={props.onChangeText} />

      <button onClick={props.handleSubmit}>Submit</button>
      <button onClick={props.handleReset}>Reset</button>
    </div>
  );
};

export default Cart;

```

```jsx
import React from "react";

const Form = props => {
  return (
    <div>
      {props.Items.map((item, index) => (
        <input
          name={item.name}
          placeholder={item.description}
          data-type={item.dtype}
          data-group={item.group}
          onChange={e => props.onChangeText(e)}
          key={index}
        />
      ))}
    </div>
  );
};
export default Form;

```

And simple input boxes are rendered to the page:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-56.png)

When a user enters text into one of the input boxes, it's saved to the application state in groups like this:

```
Itemvalues:
  0:
    groupA: 
            item1: itemvalue1
            item2: itemvalue2
    groupB: 
            item3: itemvalue3
            item4: itemvalue4
```

It's pretty complicated, but you managed to get that working.

In `handleReset`, you're able to set `itemvalues` back to a null state when the "Reset" button is pressed:

```js
handleReset = () => {
  this.setState({
    itemvalues: [{}]
  });
};
```

But the problem is that the text is not cleared from all of the input boxes:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-16-21-32.gif)

You've already handled storing the actual text in the state, so here's a simple way to clear the text from all input boxes.

## How to clear the values all inputs

At the top of `handleReset`, use `document.querySelectorAll('input')` to select all the input elements on the page:

```js
handleReset = () => {
  document.querySelectorAll('input');
  this.setState({
    itemvalues: [{}]
  });
};
```

`document.querySelectorAll('input')` returns a `NodeList`, which is a bit different than an array, so you can't use any useful array methods on it.

To turn it into an array, pass `document.querySelectorAll('input')` to `Array.from()`:

```js
handleReset = () => {
  Array.from(document.querySelectorAll('input'));
  this.setState({
    itemvalues: [{}]
  });
};
```

Now all you have to do is iterate through each of the inputs and set its `value` attribute to an empty string. The `forEach` method is a good candidate for this:

```js
handleReset = () => {
  Array.from(document.querySelectorAll("input")).forEach(
    input => (input.value = "")
  );
  this.setState({
    itemvalues: [{}]
  });
};
```

Now when a user presses the "Reset" button, the value of every input is cleared, too:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-16-21-42.gif)

