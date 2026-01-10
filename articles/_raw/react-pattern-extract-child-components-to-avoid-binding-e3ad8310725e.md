---
title: 'React Pattern: Extract Child Components to Avoid Binding'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-04T13:55:44.000Z'
originalURL: https://freecodecamp.org/news/react-pattern-extract-child-components-to-avoid-binding-e3ad8310725e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zISOb74W7PriWKX0y7biKg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: React Native
  slug: react-native
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cory House

  Here’s a common scenario in React: You’re mapping over an array, and you need each
  item to call a click handler and pass some relevant data.

  Here’s an example. I’m iterating over a list of users and passing the userId to
  delete to the d...'
---

By Cory House

Here’s a common scenario in React: You’re mapping over an array, and you need each item to call a click handler and pass some relevant data.

Here’s an example. I’m iterating over a list of users and passing the userId to delete to the deleteUser function on line 31.

```js
import React from 'react';

class App extends React.Component {
  constructor() {
    this.state = {
      users: [
        { id: 1, name: 'Cory' }, 
        { id: 2, name: 'Meg' }
      ]
    };
  }
  
  deleteUser = id => {
    this.setState(prevState => {
      return { users: prevState.users.filter( user => user.id !== id)}
    })
  }

  render() {
    return (
      <div>
        <h1>Users</h1>
        <ul>
        { 
          this.state.users.map( user => {
            return (
              <li key={user.id}>
                <input 
                  type="button" 
                  value="Delete" 
                  onClick={() => this.deleteUser(user.id)} 
                /> 
                {user.name}
              </li>
            )
          })
        }
        </ul>
      </div>
    );
  }
}

export default App;
```

Here’s a [working example on Codesandbox](https://codesandbox.io/s/0OP2Yq87). (which is awesome ?)

### So What’s the Problem?

I’m using an arrow function in the click handler. This means **every time render runs, a new function is allocated**. In many cases, this isn’t a big deal. But if you have child components, they’ll re-render even when data hasn’t changed because each render allocates a new function.

**Bottom line**: Avoid declaring arrow functions or binding in render for optimal performance. My team uses [this ESLint rule](https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/jsx-no-bind.md) to help alert us to this issue.

### What’s the Solution?

So how do you avoid binding and arrow functions in render? One option is to extract a child component. Here, I’ve extracted the list item to UserListItem.js:

```js
import React from 'react';
import PropTypes from 'prop-types';

class UserListItem extends React.Component {
  onDeleteClick = () => {
    // No bind needed since we can compose 
    // the relevant data for this item here
    this.props.onClick(this.props.user.id);
  }

  // No arrow func in render! ?
  render() {
    return (
      <li>
        <input 
          type="button" 
          value="Delete" 
          onClick={this.onDeleteClick} 
        /> 
        {this.props.user.name}
      </li>
    );
  }
}

UserListItem.propTypes = {
  user: PropTypes.object.isRequired,
  onClick: PropTypes.func.isRequired
};

export default UserListItem;
```

Then, the parent component’s render gets simpler, and no longer needs to contain an arrow function. It passes the relevant context for each list item down via props in the new “renderUserListItem” function.

```js
import React from 'react';
import { render } from 'react-dom';
import UserListItem from './UserListItem';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [{ id: 1, name: 'Cory' }, { id: 2, name: 'Sherry' }],
    };
  }

  deleteUser = id => {
    this.setState(prevState => {
      return { users: prevState.users.filter(user => user.id !== id) };
    });
  };

  renderUserListItem = user =>
    <UserListItem key={user.id} user={user} onClick={this.deleteUser} />;

  render() {
    return (
      <div>
        <h1>Users</h1>
        <ul>
          {this.state.users.map(this.renderUserListItem)}
        </ul>
      </div>
    );
  }
}

render(<App />, document.getElementById('root'));
```

Note that instead of using an arrow function in render while mapping, we’re calling a new function declared outside of render on line 19. No more function allocations on each render. ?

Here’s a [working example of this final refactor](https://codesandbox.io/s/jqQ0AlQlW).

### Yay or Yuck?

This pattern improves performance by eliminating redundant function allocations. So it’s most useful when this situation applies to your component:

1. Render is called frequently.
2. Rendering children is expensive.

Admittedly, extracting a child component as I’ve suggested above is extra work too. It requires more moving parts, and more code. So if you’re not having performance issues, it’s arguably a premature optimization ?.

So you have two options: Either allow arrows and binds everywhere (and deal with perf issues if they pop up), or forbid them for optimal performance and consistency.

**Bottom-line:** I recommend disallowing arrows and binds in render. Here’s why:

1. You have to disable the [useful ESLint rule](https://github.com/yannickcr/eslint-plugin-react/blob/master/docs/rules/jsx-no-bind.md) I suggested above to allow it.
2. Once you disable a linting rule, people are likely to copy this pattern and start disabling other linting rules. An exception in one place can quickly become the norm…

%[https://twitter.com/housecor/status/839511073279598594?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F839511073279598594%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

So I find extracting child components a useful pattern to avoid binding in render.

Have another way you like to handle this? Chime in via the comments!

### Looking for More on React? ⚛

I’ve authored [multiple React and JavaScript courses](http://bit.ly/psauthorpageimmutablepost) on Pluralsight ([free trial](http://bit.ly/pstrialimmutablepost)). My latest, “[Creating Reusable React Components](http://bit.ly/psreactcomponentsimmutablepost)” just published! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*BkPc3o2d2bz0YEO7z5C2JQ.png)

[Cory House](https://twitter.com/housecor) is the author of [multiple courses on JavaScript, React, clean code, .NET, and more on Pluralsight](http://pluralsight.com/author/cory-house). He is principal consultant at [reactjsconsulting.com](http://www.reactjsconsulting.com), a Software Architect at VinSolutions, a Microsoft MVP, and trains software developers internationally on software practices like front-end development and clean coding. Cory tweets about JavaScript and front-end development on Twitter as [@housecor](http://www.twitter.com/housecor).

