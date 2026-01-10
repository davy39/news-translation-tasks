---
title: Boost your React with State Machines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-14T19:39:46.000Z'
originalURL: https://freecodecamp.org/news/boost-your-react-with-state-machines-1e9641b0aa43
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8c333d_YNEHG4q3UDb1wTA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jean-Paul Delimat

  Mixing React and state machines is a great productivity boost for you as a developer.
  It also improves the usually shaky developers/designers collaboration.

  The state machine concept is very simple: a component can be in one stat...'
---

By Jean-Paul Delimat

Mixing React and state machines is a great productivity boost for you as a developer. It also improves the usually shaky developers/designers collaboration.

The state machine concept is very simple: a component can be in one state at a time and has a finite number of states.

How is this helpful in UI development you say?

### The problem

Let us consider a simple text edition component like the very poorly styled one below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qH9LyaKS94HYKOfvhR1jGw.png)

The possible “states” of the such a component are (from left to right):

* Display value
* Edit value
* Save in progress
* Saving error

A straightforward shape for the component model has 5 properties:

```js
state: {
  processing: true, // Will be true when saving is in progress
  error: null,      // Will be not null when a save error occurs
  value: null,      // The read only display value
  edition: false,   // Are we in edit mode?
  editValue: null,  // The currently edited but not saved value
}
```

The proper combinations of the properties will give us the 4 states we have identified above.

The problem is that there are actually 2⁵ = 32 possible combinations for the state. This means there are 28 wrong ways to use the state properties.

One typical error on the component above is to not reset the error after a successful save. So the end user will save, get a `“Something went wrong”` error message, correct the error, save again and go to display mode. So far so good. Except when going to edit mode again … the error message is still there. True story. I’ve seen this done several times by inexperienced developers.

Our component is as simple as it gets and yet it evinces a sad truth:

Operating on raw state properties means the component robustness relies solely on the correct use of the properties meaning … for each developer modifying the code … through the whole project lifecycle.

We all know how this ends!

### The solution

Consider a different approach using “state machines”. The states would be:

```js
state: {
  display: {
    processing: false,
    error: null,
    value: “Awesome”,
    edition: false,
    editValue: null,
  },
  saving: {
    processing: true,
    error: null,
    value: “Awesome”,
    edition: true, // Keep the edit view active until save is finished
    editValue: “Awesome Edit”, 
  },
  edit: {
    processing: false,
    error: null,
    value: “Awesome”,
    edition: true,
    editValue: “Awesome Editing”,
  },
  save_error: {
    processing: false,
    error: “Value should be at least 4 characters”,
    value: “Awesome”,
    edition: true, // Keep the edit box open
    editValue: “Awe”,
  }
}
```

This is more verbose than the first approach but it provides many benefits:

* One can see all the states of the component by just looking at the state machine. States have logical names and usage of each raw property is self-documented. New developers in the team will feel at home right away.
* The convention on how to extend the component is clear: create a new state and set the raw properties appropriately. No one in their right mind would dare to use raw `setState()` when there is a state machine implemented in the component.
* The last but not the least, the handover process with the UI/UX team becomes as smooth as it can be. You need a visual design for each state of your machine, and maybe some animations for the transitions. That’s it. Clear and easily trackable.

A minimalistic working version of the example above would be:

```js
import React, {Component, PropTypes} from 'react';

export default class InputStateMachine extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
        this.goToState = this.goToState.bind(this);
        this.save = this.save.bind(this);

        this.state = {
            name: 'display',
            machine: this.generateState('display', props.initialValue)
        };
    }

    generateState(stateName, stateParam) {

        const previousState = this.state ? {...this.state.machine} : {};

        switch(stateName) {
            case 'display':
                return {
                    processing: false,
                    error: null,
                    value: stateParam || previousState.value,
                    editing: false,
                    editValue: null,
                };
            case 'saving':
                return {
                    processing: true,
                    error: null, // Reset any previous error
                    value: previousState.value,
                    editing: true, // Keep the edit view active until save is finished
                    editValue: previousState.editValue,
                };
            case 'edit':
                return {
                    processing: false,
                    error: null,
                    value: previousState.value,
                    editing: true,
                    editValue: stateParam,
                };
            case 'save_error':
                return {
                    processing: false,
                    error: stateParam,
                    value: previousState.value,
                    editing: true, // Keep the edit box open
                    editValue: previousState.editValue,
                };
            case 'loading': // Same as default
            default:
                return {
                    processing: true,
                    error: null,
                    value: null,
                    editing: false,
                    editValue: null,
                };
        }
    }

    goToState(stateName, stateParam)  {
        this.setState({
            name: stateName,
            machine: this.generateState(stateName, stateParam)
        });
    }

    handleSubmit(e) {
        this.goToState('edit', e.target.value);
    };

    save(valueToSave) {
        this.goToState('saving');

        // Simulate saving the data ...
        setTimeout(() => this.goToState('display', valueToSave), 2000);
    };

    render() {
        const {processing, error, value, editing, editValue} = this.state.machine;

        if(processing) {
            return <p>Processing ...</p>
        } else if(editing) {
            return (
                <div>
                    <input type="text" onChange={this.handleSubmit} value={editValue || value} />
                    {error && <p>Error: {error}</p>}
                    <button onClick={() => this.save(editValue)}>Save</button>
                </div>
            );
        } else {
            return (
                <div>
                    <p>{value}</p>
                    <button onClick={() => this.goToState('edit', value)}>Edit</button>
                </div>
            );
        }
    }
}
```

Usage is:

```js
<InputStateMachine initialValue="Hello" />

```

There is a bit of boilerplate code to write when using state machines:

* Create a utility method that sets the state name and content. Keep track of the current state name to ease debugging.
* Keep the method that generates your state pure and use it to initialize your state in the constructor
* Destructure `this.state.machine` instead of `this.state` in your render method
* State may need parameters which can be difficult to handle. As a rule of thumb, if your state generation requires more than 3 parameters then your component should not use the state machine pattern

Some libraries aim to solve this boilerplate issue but the overhead is so small that it does not really deserve a new dependency on your project.

### Conclusion

The state machine pattern is a good way to improve your UI components readability and development process from visual design to maintenance.

Careful though! Do not go all in and apply this to all the components you have! Your app needs to remain flexible and handle emergent complexities. The number of states can quickly explode for higher level components and state machines are of no benefit in that case.

Do use the pattern on your library of standard/base components though! This is the part of the application that will live the longest. Eventually, each developer in the team will touch it and benefit from the guidance and robustness provided by the state machine.

Thanks for reading!

