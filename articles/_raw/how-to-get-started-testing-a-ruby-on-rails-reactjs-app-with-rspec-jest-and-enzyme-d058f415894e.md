---
title: 'How to get started: testing a Ruby-on-Rails / ReactJS app with RSpec, Jest
  and Enzyme'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-03T17:55:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-testing-a-ruby-on-rails-reactjs-app-with-rspec-jest-and-enzyme-d058f415894e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KnkP0HAL3iL6tyTQo7jVZw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Jest
  slug: jest
- name: React
  slug: react
- name: Ruby
  slug: ruby
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Holly Atkinson

  I recently made a simple ideas board web app using ReactJS, Ruby-on-Rails and PostgreSQL.
  Below, I’ll walk you through the initial steps I took to set up basic unit tests
  for one of the features of my app, adding a new idea.


  _Photo...'
---

By Holly Atkinson

I recently made a simple ideas board web app using ReactJS, Ruby-on-Rails and PostgreSQL. Below, I’ll walk you through the initial steps I took to set up basic unit tests for one of the features of my app, adding a new idea.

![Image](https://cdn-media-1.freecodecamp.org/images/yToemQSqCMdhO5ADFrrEyf8WwRNFKWl2Zq69)
_Photo by [Unsplash](https://unsplash.com/photos/awU3XEzdU94?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Dan DeAlmeida</a> on <a href="https://unsplash.com/search/photos/ideas?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Note: I’m not going to discuss the _scope_ of tests in this post; rather, my focus is on understanding how to install some of the _dependencies_ in order to be able to get started with writing the tests.

### Background: ideas board set up

I used Node package manager to manage my project’s dependencies. If you’d like to code along, you’ll need to make sure you have Node installed on your computer.

_Project features_

**In Rails**

Models: Idea

Relationships: none

**In React**

Components: Navbar, IdeasContainer, Idea

### **Getting started with RSpec**

I used RSpec to test the Rails part of my ideas board web app. To get started:

1. I added the gem ‘rspec-rails’, ‘~> 3.8’ to my gemfile.
2. I then ran `bundle` in my terminal window (making sure I was in the Rails directory).

3. Next, in my Rails directory, I created a new folder called `spec`. And then, another new folder inside that one called `requests`.

4. I created a new file called `ideas_spec.rb`. You can replace the name `ideas_spec` with the name of whichever model you want to test, making sure to include the `_spec` part to denote that it's a test file.

5. At the top of my ideas_spec.rb file, I added the following text:

`require ‘rails_helper’`

6. Then, in the same file, I included code describing the first test I wanted to run:

```ruby
describe “add an idea”, :type => :request dodescribe “add an idea”, :type => :request do
before do
 post ‘/api/v1/ideas’
end
it ‘returns a created status’ do
  expect(response).to have_http_status(201)
end
end
```

7. To run my test, I typed `rspec` in my terminal window, making sure I was in my rails project directory.

If you’ve been following along, RSpec should run at this point and your first test should pass!

### **Getting started with Jest**

I was pleasantly surprised to find out that the testing framework Jest is included with create-react-app! However, I also wanted to use Enzyme, a testing utility, for which I needed to install some dependencies.

1. To start off, I created a new folder called `_tests_` in my app’s `src` directory.
2. In my client-side directory, I ran the following commands:

```
npm i -D react-test-renderer
```

```
npm install --save-dev jest-enzyme
```

```
npm install --save-dev enzyme enzyme-adapter-react-16
```

3. To configure Enzyme, I created a file in `src` called `setupTests.js` and included the following:

```js
const Enzyme = require('enzyme');
const EnzymeAdapter = require('enzyme-adapter-react-16');
Enzyme.configure({ adapter: new EnzymeAdapter() });
```

4. Inside my `_tests_` folder, I created a new file, called `App.tests.js`

5. I included the following text at the top of this file to import my components and all the testing functionality I wanted for _all_ my tests:

```js
import React from 'react';
import App from '../App';
import Idea from '../components/Idea';
import IdeasContainer from '../components/IdeasContainer';
import { create, update } from 'react-test-renderer';
import '../setupTests';
import { shallow, mount, render } from 'enzyme';
import { shallowToJson } from 'enzyme-to-json';
```

6. Underneath, I included my _first_ unit test:

```ruby
describe('Idea', () => {
  it('should render a new idea correctly', () => {
    const output = shallow(
      <Idea
      key="mockKey"
      idea={"1", "Test", "Test"}
      onClick={"mockFn"}
      delete={"mockFn2"}
      />
    );
    expect(shallowToJson(output)).toMatchSnapshot();
  });
});
```

7. I ran `rails s` in the server side directory and then `npm start` in the client side directory to start my ideas board on localhost:3001.

8. To run my first test, I typed the following into my terminal window (making sure I was in the client directory):

```
npm run test
```

If you’ve been following along, Jest should run at this point, your test should pass — and you’re in a great place now to write more tests!

For more information on the ideas board project, my repo can be found [here](https://github.com/atkinsonholly/tracr).

If you made it this far, thanks for reading! I hope my post helped you get started with setting up your tests.

