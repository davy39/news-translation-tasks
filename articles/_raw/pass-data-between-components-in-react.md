---
title: How to Pass Data and Events Between Components in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-08T16:17:32.000Z'
originalURL: https://freecodecamp.org/news/pass-data-between-components-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/Colorful-Animal-Crossing-Icons-Icon-Set-2.png
tags:
- name: components
  slug: components
- name: crud
  slug: crud
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Nishant Kumar\nIf you're trying to implement CRUD operations using API\
  \ endpoints, you might find that it's hard to manage data across multiple components.\n\
  Or maybe you have a modal, but you want to trigger it from a different component.\
  \ \nWrapping y..."
---

By Nishant Kumar

If you're trying to implement CRUD operations using API endpoints, you might find that it's hard to manage data across multiple components.

Or maybe you have a modal, but you want to trigger it from a different component. 

Wrapping your head around how to tackle these scenarios can be difficult.

In this tutorial, I'll be showing you how you can do it.

## How to Pass Data Between a Parent Component and a Child Component

Firstly, let's pass data between a parent component and a child component. .

First, you'll need to create two components, one parent and one child.

```
import React from 'react'

export default function Parent() {
  return (
    <div>
      
    </div>
  )
}

```

```
import React from 'react'

export default function Child() {
    return (
        <div>
            
        </div>
    )
}

```

Next, you'll import the child component in the parent component and return it.

```
import React from 'react'
import Child from './Child';

export default function Parent() {
  return (
    <div>
      <Child/>
    </div>
  )
}
```

Then you'll create a function and a button to trigger that function. Also, you'll create a state using the _useState_ Hook to manage the data.

```
import React from 'react'
import Child from './Child';
import { Button } from 'semantic-ui-react';
import { useState } from 'react';
import './App.css';

export default function Parent() {
  const [data, setData] = useState('');
  
  const parentToChild = () => {
    setData("This is data from Parent Component to the Child Component.");
  }
  return (
    <div className="App">
      <Child/>
      
      <div>
        <Button primary onClick={() => parentToChild()}>Click Parent</Button>
      </div>
    </div>
  )
}

```

As you can see here, we are calling the _parentToChild_ function on the _Click Parent_ button click. When the Click Parent button is clicked, it will store the "This is data from Parent Component to the Child Component" in the _data_ variable. 

Now, let's pass that data state to our child components. You can do this using props.

Pass the data as props when you are calling the child component like this: 

```
<Child parentToChild={data}/>
```

Here, we are passing the data in the child component as _data**.**_

`data` is the data which we have to pass, and `parentToChild` is the name of the prop.

Next, it's time to capture the data in the child component. And it's very simple.

Here, there can be two cases. 

Case 1: If you are using a functional component, simply catch the parentToChild in the parameters. 

```
import React from 'react'

export default function Child({parentToChild}) {
    return (
        <div>
            {parentToChild}
        </div>
    )
}
```

Case 2: If you have a class component, then just use `this.props.parentToChild`. 

```
import React, { Component } from 'react'

export default class Child extends Component {
    render() {
        return (
            <div>
                {this.props.parentToChild}
            </div>
        )
    }
}
```

Either way, you will get the same results:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-06-132836.png)

When we click the `Click Parent` button, we will see the data as output on the screen. 

```
import React from 'react'
import Child from './Child';
import { Button } from 'semantic-ui-react';
import { useState } from 'react';
import './App.css';

export default function Parent() {
  const [data, setData] = useState('');
  
  const parentToChild = () => {
    setData("This is data from Parent Component to the Child Component.");
  }
  return (
    <div className="App">
      <Child parentToChild={data}/>
      
      <div className="child">
        <Button primary onClick={() => parentToChild()}>Click Parent</Button>
      </div>
    </div>
  )
}
```

Above you'll see the full code for `Parent Component`.

## How to Pass Data Between a Child Component and a Parent Component

This one is somewhat trickier. 

First, you need to create a function in the parent component called  `childToParent` and an empty state named `data`.

```
const [data, setData] = useState('');

const childToParent = () => {
   
}
```

Then, pass the `childToParent` function as a prop to the child component.

```
<Child childToParent={childToParent}/>
```

Now, in our child component, accept this function call as props and assign it to an onClick event. 

Also, declare a state which contains some data in the form of a string or a number.

Pass the data into the the `parentToChild` function as parameters. 

```
import React from 'react'
import { Button } from 'semantic-ui-react';

export default function Child({childToParent}) {
    const data = "This is data from Child Component to the Parent Component."
    return (
        <div>
            <Button primary onClick={() => childToParent(data)}>Click Child</Button>
        </div>
    )
}
```

Next, in the parent component, accept this data in the `childToParent` function as a parameter. Then set the data using the useState hook.

```
import './App.css';
import { useState } from 'react';
import Child from './Child';

function Parent() {
  const [data, setData] = useState('');
  
  const childToParent = (childdata) => {
    setData(childdata);
  }

  return (
    <div className="App">
      <div>
        <Child/>
      </div>
    </div>
  );
}

export default Parent;

```

Next, show that data variable in the return function.

```
import './App.css';
import { useState } from 'react';
import Child from './Child';

function Parent() {
  const [data, setData] = useState('');
  
  const childToParent = (childdata) => {
    setData(childdata);
  }

  return (
    <div className="App">
     {data}
      <div>
        <Child childToParent={childToParent}/>
      </div>
    </div>
  );
}

export default Parent;
```

The child data will overwrite the parent data when the `Click Child` button is clicked. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-06-134803.png)

Now, you can pass data from **Child to Parent** and **Parent to Child** like a pro.

### You can also pass events like onClick or OnChange 

Just call an alert method in the `childToParent` function and pass that function as a prop to the child component_._

```
import './App.css';
import Child from './Child';

function Parent() {
  const childToParent = () => {
    alert("This is an alert from the Child Component")
  }

  return (
    <div className="App">
      <div className="child">
        <Child childToParent={childToParent}/>
      </div>
    </div>
  );
}

export default Parent;
```

And in the child _c_omponent, accept the `childToParent` function as a prop. Then assign it to an onClick event on a button.

```
import React from 'react'
import { Button } from 'semantic-ui-react';

export default function Child({childToParent}) {
    return (
        <div>
            <Button primary onClick={() => childToParent()}>Click Child</Button>
        </div>
    )
}
```

Your function in the parent _c_omponent will be called out when you click the button in the child component and you will see this alert:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-2021-06-06-140405.png)

That's it!

You can [find the code on Github](https://github.com/nishant-666/Passing-data-in-React) if you want to experiment further.

> Well, that's all folks. Happy Learning.

