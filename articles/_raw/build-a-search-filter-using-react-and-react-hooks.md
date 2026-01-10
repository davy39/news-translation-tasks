---
title: How to Build a Search Filter using React and React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-17T17:56:15.000Z'
originalURL: https://freecodecamp.org/news/build-a-search-filter-using-react-and-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/How-to-Build-a-Weather-Application-using-React--23-.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: search
  slug: search
seo_title: null
seo_desc: 'By Nishant Kumar

  When you send a GET request to an API, you get the response data back from the server.
  But sometimes managing this data can be a problem.

  In this blog post, I will show you how to create a search filter in React. It will
  search for a...'
---

By Nishant Kumar

When you send a GET request to an API, you get the response data back from the server. But sometimes managing this data can be a problem.

In this blog post, I will show you how to create a search filter in React. It will search for a particular term in the data using functional components and React hooks. 

## How to Make a GET Request to an API

First of all, let's make a GET request to an API which will fetch some data from the server. You can use any server you want to get the data, but in this article I'll use {JSON} Placeholder to fetch the users list.

In this example, we have cards which show the names and emails of different users. We also have a search input box which we'll use to search for a particular user.

```
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Input } from 'semantic-ui-react'
export default function Posts() {
    const [APIData, setAPIData] = useState([])
    useEffect(() => {
        axios.get(`https://jsonplaceholder.typicode.com/users`)
            .then((response) => {
                setAPIData(response.data);
            })
    }, [])

    return (
        <div style={{ padding: 20 }}>
            <Input icon='search'
                placeholder='Search...'
            />
            <Card.Group itemsPerRow={3} style={{ marginTop: 20 }}>
                {APIData.map((item) => {
                    return (
                        <Card>
                            <Card.Content>
                                <Card.Header>{item.name}</Card.Header>
                                <Card.Description>
                                    {item.email}
                                </Card.Description>
                            </Card.Content>
                        </Card>
                    )
                })}
            </Card.Group>
        </div>
    )
}

```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-202008.png)
_Getting the List of Users and a Search Input at the top_

And if you don't know how to handle GET API calls in React, follow my blog on [React CRUD Operations](https://www.freecodecamp.org/news/how-to-perform-crud-operations-using-react/) or my video on [React CRUD Operations](https://youtu.be/-ZMP8ZladIQ) where I show you how to handle API calls in React.

## How to Get Search Input from the Search Input Box

Now, let's get our search query from the search input box.

Create a state for the search input.

```
const [searchInput, setSearchInput] = useState('');
```

Here, `searchInput` is a string, and we'll use `setSearchInput` to set the search input.

Now, we'll create a function that will handle our search functionality.

```
const searchItems = () => {
        
}
```

And bind this function to the search input via the `onChange` event.

```
<Input icon='search'
                placeholder='Search...'
                onChange={() => searchItems()}
            />
```

So, whenever we type something in the input field, the `searchItems` will run.

Now, we need to pass the input value to the `searchItems` function.

```
<Input icon='search'
                placeholder='Search...'
                onChange={(e) => searchItems(e.target.value)}
            />
```

Next, let's receive the search query into the function and set the `searchInput` state to this value using `setSearchInput` that we created previously.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
    }
```

You can check this whether it is working on not by consoling `searchValue`.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-203750.png)

As you can see, I am typing my name here and it is showing up in the console.

## How to Filter Items Based on the Search Results

Now, we are going to filter out our APIData using the filter method.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        APIData.filter((item) => {
            return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
        })
    }
```

In this function `searchTerm`, you can see that we are using the `filter` method to filter out APIData state, which contains the data coming from the server.

We are also using `Object.values` to get the values from the object item. 

Then, we are converting the values into a string using the `join(' ')` method.

Next, we are changing that string values into lowercase using the `toLowerCase` method. 

And lastly, we are checking if this string includes our search input that we typed into the search bar. We also convert it to lowercase to make sure that if we type our term in uppercase, it converts the string to lowercase to make the search more effective.

Then, we return the whole query.

Now we need to set this filtered array into a variable.

```
const filteredData = APIData.filter((item) => {
return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
})
```

Let's check the above functionality by consoling it. So, search a user name and you will see that you get the data for that username in particular.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-211709.png)
_Getting the search item into the console_

Now, we need a state where we can store the filtered data. So, let's create one.

```
const [filteredResults, setFilteredResults] = useState([]);
```

Create one state that will contain our filtered data.

Then set this state to `filteredData` in the `searchItems` function using `setFilteredResults`.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        const filteredData = APIData.filter((item) => {
            return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
        })
        setFilteredResults(filteredData)
    }
```

## How to Show the Filtered Results in the User Interface

Now, let's show these filtered results in our main UI.

First we need to write some code that checks if our search input is empty, and if so, shows all the data. Otherwise it will filter them according to the search input.

```
const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        if (searchInput !== '') {
            const filteredData = APIData.filter((item) => {
                return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
            })
            setFilteredResults(filteredData)
        }
        else{
            setFilteredResults(APIData)
        }
    }
```

We also need this check in the return part of the application.

So, if the search term's length is greater than 1, we will show filtered data. Otherwise we will show all the data which is stored in the API Data state.

```
<Card.Group itemsPerRow={3} style={{ marginTop: 20 }}>
                {searchInput.length > 1 ? (
                    filteredResults.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                ) : (
                    APIData.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                )}
            </Card.Group>
```

Now, if we search some username in the search field, we will get that specific user's data.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-212917.png)
_Getting the search input's results in the UI_

And if we remove the name, we will get all the data.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-213037.png)
_Getting all the data if the search input is empty_

Here is all the code for your reference:

```
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Input } from 'semantic-ui-react'
export default function Posts() {
    const [APIData, setAPIData] = useState([])
    const [filteredResults, setFilteredResults] = useState([]);
    const [searchInput, setSearchInput] = useState('');
    useEffect(() => {
        axios.get(`https://jsonplaceholder.typicode.com/users`)
            .then((response) => {
                setAPIData(response.data);
            })
    }, [])

    const searchItems = (searchValue) => {
        setSearchInput(searchValue)
        if (searchInput !== '') {
            const filteredData = APIData.filter((item) => {
                return Object.values(item).join('').toLowerCase().includes(searchInput.toLowerCase())
            })
            setFilteredResults(filteredData)
        }
        else{
            setFilteredResults(APIData)
        }
    }

    return (
        <div style={{ padding: 20 }}>
            <Input icon='search'
                placeholder='Search...'
                onChange={(e) => searchItems(e.target.value)}
            />
            <Card.Group itemsPerRow={3} style={{ marginTop: 20 }}>
                {searchInput.length > 1 ? (
                    filteredResults.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                ) : (
                    APIData.map((item) => {
                        return (
                            <Card>
                                <Card.Content>
                                    <Card.Header>{item.name}</Card.Header>
                                    <Card.Description>
                                        {item.email}
                                    </Card.Description>
                                </Card.Content>
                            </Card>
                        )
                    })
                )}
            </Card.Group>
        </div>
    )
}

```

Now there you have it, a fully functional search filter in React using React hooks.

We often handle this functionality from the back end side by passing search query parameters in the API endpoint. But it's important to know how to handle it from the front end side too.

You can also check my YouTube video on [Building a Search Filter using React and React Hooks](https://youtu.be/8YsQmvJ9UZE) if you'd like to supplement this article.

> That's all folks. Happy Learning.

