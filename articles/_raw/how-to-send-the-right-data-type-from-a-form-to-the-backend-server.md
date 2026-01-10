---
title: How to Convert react-dropdown-select's Default Value from Array to String
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-10T21:30:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-the-right-data-type-from-a-form-to-the-backend-server
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/1641660058245.jpg
tags:
- name: forms
  slug: forms
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: "By Caleb Olojo\nWeb forms play an important role on many sites on the internet,\
  \ and they're something you should know how to build as a web developer. \nFrom\
  \ good ol' login forms to signup forms and survey forms (or whatever they're called\
  \ these days),..."
---

By Caleb Olojo

Web forms play an important role on many sites on the internet, and they're something you should know how to build as a web developer. 

From good ol' login forms to signup forms and survey forms (or whatever they're called these days), their main purpose is to receive data and send them to a backend server where they're stored.

In this article, we're going to see how we can convert the data gotten from a form from one type to another with JavaScript. But, before you read this article any further, you should have an understanding of the following:

* The basics of React.js
* How to preserve form state in React.js
* How to create controlled input components

Also, in this article, we'll be covering:

* How to send the form data that you obtain to a backend server through an API
* How to get the exact value of a label in the `options` array of the react-dropdown-select package.

Now that you know what you need to get started with this article, let's dive in.

## Getting Started

We'll be building a simple form with React in this article so we can understand how the process works. To do that we'll be using [Next.js](https://nextjs.org) to bootstrap our application. If you're new to Next.js, you can take a look at their documentation [here](https://nextjs.org/docs/getting-started).

Now let's get all the dependencies that we'll be needing in this project. Since it is a Next.js project, let's start by setting up a next-app:

```
npx create-next-app name-of-your-app

```

The command above will install all important dependencies that we need in a Next.js app function. The next dependencies that we need in this project are:

*  **xios** for data fetching, and 
* **styled-components** to style the app.

The command below does that for us:

```
npm install styled-components react-dropdown-select axios --save-dev

```

A typical Next.js project structure is different from that of [create-react-app](https://create-react-app.dev). To keep this article concise, we won't be going over the full application structure – we'll only be focusing on what applies to us. 

That being said, let's take a look at the app structure below: 

```
|__pages
|   |-- _app.js
|   |-- index.js
|__src
|   |__components
|   |    |__role
|   |    |   |__style
|   |    |     |-- role.styled.js
|   |    |__index.js        
|   |
|   |__containers
|   |    |__dropdown-select 
|   |        |-- index.js
|   
|__
```

## Overview of the app structure

In the last section, we got the required dependencies for this project. In this section, we'll be looking at the project structure and the function that each file performs.

The pages directory is where all the routing of the app takes place. This is an out-of-the-box feature of Nextjs. It saves you the stress of hard-coding your independent routes.

`pages/api`: this API directory enables you to have a backend for your Next.js app. inside the same codebase. This means you don't have to go through the common way of creating separate repositories for your REST or GraphQL APIs and deploying them on backend hosting platforms like Heroku, and so on.

With the API directory, every file is treated as an API endpoint. If you look at the API folder, you'll notice that we have a file called user.js in it. That file becomes an endpoint, which means an API call can be performed using the path to the file as the base URL.

`pages/_app.js` is where all our components get attached to the DOM. If you take a look at the component structure, you’ll see that all the components are passed as pageProps to the Component props too.

It is like the index.js file when using Create-React-App. The only difference here is that you are not hooking your app to the DOM node called “root”

```javascript
React.render(document.getElementById("root"), <App />)
```

`index.js` is the default route in the pages folder. That is where we'll be doing most of the work in this project. When you run the command below, it starts up a development server and the contents of index.js are rendered on the web page.

`components/role` is the component file that houses the dropdown select component and its style

And lastly, `containers/dropdown-select` is where we're building the form component.

## How to Build the Form and Manage State

Now that we have seen some of the basic functions of the folders/files in the app, let's start building the form component. We won't be focusing on writing the styles in this article.

The code snippet below shows the basic structure of the form component without the state variables. We'll take a step-by-step approach to understanding what is going on in the snippet.

```javascript
import React from "react";
import styled from "styled-components";
import { InputGroup } from "../../components/role/style/role.styled";
import Role from "../../components/role";
import axios from "axios";

const AuthForm = styled.form`
	...
`;

const DropDownSelect = () => {
  return (
    <AuthForm onSubmit="">
      <h2>Register an Account...</h2>
      <InputGroup>
        <label htmlFor="email">Email address</label>
        <input
          name="email"
          id="email"
          type="email"
          placeholder="Enter email address"
          className="inputs"
        />
      </InputGroup>
      <InputGroup>
        <label htmlFor="password">Create password</label>
        <input
          name="password"
          id="password"
          type="password"
          placeholder="Create password"
          className="inputs"
        />
      </InputGroup>
      <Role />
   </AuthForm>
  );
};

export default DropDownSelect;

```

The component above doesn't have any means of tracking the input that the user types into the form fields, and we do not want that. To get that sorted out, we'll make use of React's `useState()` hook to monitor the state

Let's start by creating the state variables. You'll notice that we have three input fields in the component, so that means we'll have to create three state variables.

```js
 const [email, setEmail] = React.useState("");
 const [password, setPassword] = React.useState("");
 const [role, setRole] = React.useState();
```

But we need a way to track the state of the data we're sending to the backend server, so we need another state variable to monitor the status of our asynchronous data fetching (POST) request. 

A very popular pattern in the React ecosystem is to create a loading component that'll indicate this process.

```js
const [loading, setLoading] = React.useState(false);
```

Now that we have this in place we can set up our input fields to be controlled using the `onChange()` prop.

```js
<input
  name="email"
  id="email"
  type="email"
  placeholder="Enter email address"
  className="inputs"
  value={email}
  onChange={(e) => setEmail(e.target.value)}
/>
```

The process is then repeated for the remaining input fields. But, there's a catch. You'll notice that we already imported the `<Role />` component and we already passed some pre-defined props to the component. Let's take a look at the component itself before we go too deep.

## The Role Component

This component utilizes the `react-dropdown-select` package for its functionality, it takes in an array of values into its properties. 

The least required prop is the `options` prop which receives an array of objects with `label` and `value` keys

```js
const options = [
   { label: "Manager", value: "Manager" },
   { label: "Worker", value: "Worker" }
]

```

Let's have a look at the component below: 

```javascript
import React from "react";
import { InputGroup } from "./style/role.styled";
import Select from "react-dropdown-select";
import propTypes from "prop-types";

const Role = ({ userRole, roleChange }) => {
  const options = [
    { label: "Worker", value: "Worker" },
    { label: "Manager", value: "Manager" },
  ];

  return (
    <React.Fragment>
      <InputGroup>
        <label htmlFor="fullname">Role</label>
        <Select
          value={userRole}
          options={options}
          placeholder="Please select your role"
          required={true}
          dropdownPosition="top"
          className="select"
          color="#ff5c5c"
          onChange={roleChange}
        />
      </InputGroup>
    </React.Fragment>
  );
};

export default Role;

Role.propTypes = {
  ...
};

```

I mentioned before that the `<Role />` component has its own custom props, and you can see that above. 

The component takes in two props: `userRole` that tracks the input based on the option that user selects, and the `roleChange` prop that gets passed as a value to the `onChange()` property of the `<Select />` component.

The `<Select />` component has various props that you can pass to it. From the `dropdownPosition` prop that specifies where the options menu is positioned on the page, to the `color` prop that affects the style of the items in the options menu, and so on. You can take a look at some of them [here](https://www.npmjs.com/package/react-dropdown-select).

We made an import statement that brings in the React `"prop-types"` module at the top of this component's file. We'll be using this module to validate the type of data that is passed into this component.

```javascript
Role.propTypes = {
  userRole: propTypes.array.isRequired,
  roleChange: propTypes.func.isRequired,
};
```

From snippet above, we stated that the type of data that will be passed into `userRole` as a value must be of a JavaScript array data-type and `roleChange` is required to be a function. Anything other than these will result in an error.

## How to Use the Role Component

Now that we have gone through the `<Role />` component and learned how it works, let's take a look at how we can use it in the app below:

```javascript
import React from "react";
import styled from "styled-components";
import { InputGroup } from "../../components/role/style/role.styled";
import Role from "../../components/role";

const AuthForm = styled.form`
 ...  
`;

const DropDownSelect = () => {
  const [role, setRole] = React.useState();
  
  return (
    <AuthForm onSubmit={handleSignUp}>
      <h2>Register an Account...</h2>
      // previous details    
      <Role
        userRole={role}
        roleChange={(role) => setRole(role.map((role) => role.value))}
      />
   </AuthForm>
  );
};

export default DropDownSelect;

```

The snippet above shows how the `<Role />` component is being used. You can see the custom props in use too. `userRole` is assigned the `role` state value.

You may have been wondering why we did not assign any value to the `role` state value we declared it. Well, that's because the `<Select />` component from **react-dropdown-select** has a default data-type value of an array, so there's no need to set an array in the `useState()` hook.

The `roleChange` prop looks totally different from the previous way we have been using the **onChange** prop in the input fields. Here, we had to place the items we needed into a separate array, so that we're able to get the exact data when the user selects an option.

```javascript
roleChange={(role) => setRole(role.map((role) => role.value))}
```

If you can recall, we had an array called `options` which had key value pairs of `label` and `value`. The snippet above helps us place the `value` key into an entirely new array since that is what we need, and this is possible with the inbuilt `map()` method of JavaScript.

When the user clicks on any option, we'll be getting an array containing just one item that was selected. Say, for example, the user clicks on the "Worker" option, the value that is stored in form state is: `['Worker']`.

But we do not want this data type to be sent to the server – we want a string instead. How then do we fix this, you might ask? We'll see how we can do that in the next section.

## How to Send the Form Data to the Server

In the previous sections, learned about the structure of a Next.js app and how to build and manage state in a React form. 

In this section, we'll be sending the data that we obtained from the form to the backend server via an API.

```javascript
import React from "react";
import styled from "styled-components";
import { InputGroup } from "../../components/role/style/role.styled";
import Role from "../../components/role";
import axios from "axios";

const AuthForm = styled.form`
  ...
`;

const DropDownSelect = () => {
  ...
  const [loading, setLoading] = React.useState(false);

  const handleSignUp = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const response = await axios({
        method: "POST",
        url: "https://your-api-endpoint.com",
        data: {
          email,
          password,
          role: role.toString(),
        },
        headers: {
          "Content-Type": "application/json",
        },
      });
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <AuthForm onSubmit={handleSignUp}>
      <h2>Register an Account...</h2>
	  // form feilds
      <button className="btn">{loading ? "Registering" : "Register"}</button>
    </AuthForm>
  );
};

export default DropDownSelect;
```

We'll be focusing on the asynchronous data call function, `handleSignup`, which we'll be using to send the data to the server through the API endpoint.

```javascript
const handleSignUp = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const response = await axios({
        method: "POST",
        url: "https://your-api-endpoint.com",
        data: {
          email,
          password,
          role: role.toString(),
        },
        headers: {
          "Content-Type": "application/json",
        },
      });
    } catch (error) {
      console.log(error);
    }
  };
```

The initial value of the `loading` state was set to be `false`, but in the `try` block, it is `true`. This means that, if the asynchronous data call is going on, the loading value should be `true`. If not, it should be `false`.

We mentioned before that we do not want to send an array data type as an input value to the server. Instead we want a string. We do this by using the native string method [`toString()`] of JavaScript to transform this data type.

```javascript
data: {
  role: role.toString()
}
```

The `loading` state value can be seen in action below. We're using a ternary operator to check if the loadin state variable is true. If Yes, the text in button will be **"Registering"**. If No, the text remains unchanged.

```javascript
<button className="btn">{loading ? "Registering" : "Register"}</button>
```

You can play with the snippet below to confirm if the result is accurate or not.

```javascript
const options = [
   { label: "Worker", value: "Worker" },
   { label: "Manager", value: "Manager" }
]

// create a new array with the key value that you want
const mappedOptions = options.map(option => option.value)
console.log(mappedOptions) // ['Worker', 'Manager']

// convert the mapped option array to a string value
const mappedOptionsToString = mappedOptions.toString()
console.log(mappedOptionsToString)
```

## Conclusion

If your backend API lets you send an array data-type as a value from an input field, you can use what you have learnt here, because the react-dropdown-select package allows you to do that. 

But in scenarios where the value that is required from your input field is a string, then you can consider using the native `toString()` method of JavaScript as you wish.

Here's the [link](https://exdemo.netlify.app/demo/dropdown) to the deployed demo app and a GIF that shows you what it looks like with all the styles applied:

![Image](https://www.freecodecamp.org/news/content/images/2022/01/ezgif.com-gif-maker--1-.gif)

Thank you for reading this article. If you've found it helpful, kindly share it with your peers.

