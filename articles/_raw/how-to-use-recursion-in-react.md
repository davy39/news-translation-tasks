---
title: How to Use Recursion in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-09T18:55:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-recursion-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/How-to-Build-a-Weather-Application-using-React--39-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Recursion
  slug: recursion
seo_title: null
seo_desc: "By Nishant Kumar\nSometimes you'll need to print records from an array,\
  \ but the array is too big and nested. \nLet's say we have a family tree, or a folder\
  \ structure. We have multiple arrays nested inside arrays, and it goes on and on.\
  \ It's so big and ..."
---

By Nishant Kumar

Sometimes you'll need to print records from an array, but the array is too big and nested. 

Let's say we have a family tree, or a folder structure. We have multiple arrays nested inside arrays, and it goes on and on. It's so big and deep that it's not possible to map each and every child array inside its parent.

It looks something like this:

```
export const familyTree = {
  //Grandfather
  name: "John",
  age: 90,
  children: [
    {
      name: "Mary",
      age: 60,
    },
    {
      name: "Arthur",
      age: 60,
      children: [
        {
          name: "Lily",
          age: 35,
          children: [
            {
              name: "Hank",
              age: 60,
            },
            {
              name: "Henry",
              age: 57,
            },
          ],
        },
        {
          name: "Billy",
          age: 37,
        },
      ],
    },
    {
      name: "Dolores",
      age: 55,
    },
  ],
};

```

In the above example, we have a family tree. If the parent has children, it will be inside an array called **Children**. If that **Child** has **Children**, it will inside their **Children** Array.

This example is a little bit simple, but let's say we have lots and lots and lots of family members. Maybe even so that it's difficult to count. 

In this case, to represent our family tree effectively we will use something called **Recursion**. Recursion simply means calling the same function inside itself, or rendering a component inside the same component.

What will happen is, the function or the component will be called as long as we have the data. So, let's try to implement **Recursion** in this case.

## Here's What the Code Looks like Without Recursion

So, we have the data, as you can see above. Let's print all the family members name in our UI.

Create a component called **Family.** 

```
import "./App.css";
import { familyTree } from "./data";
import Family from "./Family";

function App() {
  return (
    <div>
      <Family familyTree={familyTree} />
    </div>
  );
}

export default App;

```

We are also importing the array which is **familyTree**. Then, we are passing the data as **familyTree** in the **Family** component as props.

Now, in the Family component, let's receive the props and destructure it.

```
import React from "react";

export default function Family({ familyTree }) {
  return <div style={{ paddingLeft: 10 }}></div>;
}

```

Now, we will create a function that will expand the family tree by clicking on the Parent's name. We'll also create a state that will toggle its value when the function runs.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return <div style={{ paddingLeft: 10 }}></div>;
}

```

Now, let's map the familyTree array and extract the data from it.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span>{familyTree.name}</span>
      {familyTree.children.map((child) => {
        return (
          <div style={{ paddingLeft: 10 }}>
            <span>{child.name}</span>
          </div>
        );
      })}
    </div>
  );
}

```

We are also mapping the first array (which is inside the children array) inside the parent **John**. This basically means all the children of **John** will be printed.

Now, let's add the function trigger. If we click the name of the parent, let's say **John**, the function **expand** will run and it will toggle the value of **isVisible** State.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {familyTree.children.map((child) => {
        return (
          <div style={{ paddingLeft: 10 }}>
            <span>{child.name}</span>
          </div>
        );
      })}
    </div>
  );
}

```

Now, let's hide the values from the mapped array, and only show them when the **isVisible** is true.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <span>{child.name}</span>
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

If you click the parent's name, and it will toggle their children and show this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-06-223357.png)

Now let's say Mary has some children, or Arthur has some children. And their children have children, and it goes on. We can map each array inside an array to get the whole family tree in the list. The code will look something like this. 

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>

      {isVisible ? (
        familyTree?.children?.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <span onClick={expand}>{child.name}</span>
              {child?.children?.map((subChild) => {
                return (
                  <div style={{ paddingLeft: 10 }}>
                    <span onClick={expand}>{subChild?.name}</span>
                    {subChild.children?.map((subChildInner) => {
                      return (
                        <div style={{ paddingLeft: 10 }}>
                          <span onClick={expand}>{subChildInner?.name}</span>
                          {subChildInner.children?.map((subChildInner2) => {
                            return (
                              <div>
                                <span>{subChildInner2.name}</span>
                              </div>
                            );
                          })}
                        </div>
                      );
                    })}
                  </div>
                );
              })}
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```



And the output will be this.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-09-233108.png)

But we cannot just keep mapping each and every child array which is inside their parent array. The entire code can look ugly and the process can become hectic. 

It is so confusing that I was stuck here too for some time. 

In this case, we will use **Recursion**. So, let's implement it.

## How to Use Recursion Instead

Now, let's do the same thing using Recursion. Our code would be much cleaner now.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <span>{child.name}</span> *
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

So, at the place of **span** tag (at the place we are printing the child's name from the first level parent array), we will call the **Family** Component again. 

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <Family />
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Just like this. But you'll see the **Family** component is receiving a prop, which is **familyTree.** We have to pass it as well. 

So, what can we pass that will satisfy the value of the **familyTree** prop?

Open and see the array where we are getting our data. We have a top level there, which is **John**. Now, we are mapping the Children array inside John, which is giving us his three children, and we are showing them in our UI.

Now if you click **Mary**, it will show the children inside **Mary,** because Mary is now the parent. 

So, to go further into the array, we have to pass the **child** from the array when we mapped, as the prop familyTree.

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree.children.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <Family familyTree={child}/>
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

Just like this. Make sure the names of the props are the same in both places.

But we will run into a problem as soon as we click **Mary**. Because Mary has no children and no children array inside. So, we cannot map an empty array or an array that doesn't exist. We will get an error and the page will go blank.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-06-224638.png)

So, we will have the skip those with no children arrays inside. 

One simple way to do it is to use a question mark ('?'). This is known as Optional Chaining. If the value or any property is undefined, it will skip it. [Read more about Optional Chaining in this article](https://www.freecodecamp.org/news/how-the-question-mark-works-in-javascript/).

```
import React, { useState } from "react";

export default function Family({ familyTree }) {
  const [isVisible, setIsVisible] = useState(false);
  const expand = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div style={{ paddingLeft: 10 }}>
      <span onClick={expand}>{familyTree.name}</span>
      {isVisible ? (
        familyTree?.children?.map((child) => {
          return (
            <div style={{ paddingLeft: 10 }}>
              <Family familyTree={child} />
            </div>
          );
        })
      ) : (
        <></>
      )}
    </div>
  );
}

```

So, we have added a question mark when we are mapping the array. If we click the Parent with no children, we will get no errors.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-06-225211.png)

And we can display the whole Family Tree like this. If the Parent has a Child, it will expand. If the Parent has no Children, it will do nothing.

And that's how we implement **Recursion in React.**

## Conclusion

Let me repeat what we are doing. We are simply mapping an array with children inside of it, and some of those children have sub-children, and it can go on.

So, we have used **recursion** to automate the process of mapping the array by itself. We are simply calling the same Family component inside it when we are mapping the array so that it calls itself and prints everything again. It will go on until we have nothing left, or an empty array.

That is the power of recursion.

If you want to see the video version of this, visit my video on [Recursion in React](https://youtu.be/1Qq_0rJUEos) on my Channel [Cybernatico](https://www.youtube.com/c/CybernaticoByNishant).

Also check the code on [Github](https://github.com/nishant-666/React-Interview-Questions/tree/master/recursion-in-react) if you like.

Thanks for reading. God Bless.

