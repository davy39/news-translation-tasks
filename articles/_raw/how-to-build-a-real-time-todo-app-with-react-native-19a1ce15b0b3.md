---
title: How to build a real-time todo app with React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-01T18:27:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-real-time-todo-app-with-react-native-19a1ce15b0b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e2uBLw946pDyqjdV5xAJpQ.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Divyanshu Maithani

  A todo app touches on all the important parts of building any data-driven app, including
  the Create, Read, Update and Delete (CRUD) operations. In this story I’ll be building
  a todo app with one of the most popular mobile framew...'
---

By Divyanshu Maithani

A todo app touches on all the important parts of building any data-driven app, including the **C**reate, **R**ead, **U**pdate and **D**elete (CRUD) operations. In this story I’ll be building a todo app with one of the [most popular mobile frameworks](https://stateofjs.com/2017/mobile/results/), **React Native**.

I’ll be using [**ReactiveSearch Native**](https://github.com/appbaseio/reactivesearch/tree/dev/packages/native), an open-source library which provides React Native UI components and simplifies building data-driven apps.

Here’s what I’ll be building in this story:

![Image](https://cdn-media-1.freecodecamp.org/images/1*bbDAbPL1rYl2k5fPFDtFHg.png)
_Todo App_

Check out the app on [snack](https://snack.expo.io/@dhruvdutt/todo) or on [expo](https://expo.io/@dhruvdutt/todos).

### What is React Native?

Here’s what the [docs](https://facebook.github.io/react-native/) say:

> React Native lets you build mobile apps using only JavaScript. It uses the same design as React, letting you compose a rich mobile UI from declarative components.

Even if you’re just getting started with React or React Native, you should be able to follow along with this story and build your very own real-time todo app.

### Why use ReactiveSearch? ⚛

[ReactiveSearch](https://github.com/appbaseio/reactivesearch) is an open-source React and React Native UI components library for Elasticsearch which I’ve co-authored with [some awesome people](https://github.com/appbaseio/reactivesearch/graphs/contributors). It provides a variety of React Native components that can [connect to any Elasticsearch](https://opensource.appbase.io/reactive-manual/native/getting-started/reactivebase.html#connect-to-elasticsearch) cluster.

I’ve written another story on [Building a GitHub Repo Explorer with React and Elasticsearch](https://medium.freecodecamp.org/building-a-github-repo-explorer-with-react-and-elasticsearch-8e1190e59c13) which you may check out for a brief overview of Elasticsearch. Even if you’ve had no experience with Elasticsearch you should be able to follow along with this story fine.

### Setting things up ⚒

We will be using the [React Native version](https://opensource.appbase.io/reactivesearch/native) of the library here.

Before we start building the UI, we’ll need to create a datastore in Elasticsearch. ReactiveSearch works with any Elasticsearch index and you can easily [use it with your own dataset](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*7be2L3leZOfV6hwRIcB9Mg.png)
_View my app dataset [here](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAALwAAAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFs4RH-_LaQFp2SlHxdkdiaJMgDx8HsBmHrHmxFLRm7V1uYmmy_j7CIuOAUjTBNw0KgomWuYOXFddgJRsGIU7fsxTMJHKDeitU2LeOk2yVyC7H5mdOvPQ84QV-WGxMqxGGV7LjU-urZhg0CpMqTT3OZQPUib0tK7qbmGxGDnUaoY_1q4GKLDtvfIuD4EF0ZJHcCe_vWVP-1QtnZklZNaGFkoid1LOlZWFaH_-wziAA&amp;editable=false" rel="noopener" target="_blank" title="). You can also clone this to your own app_

For brevity, you can use [my dataset](https://opensource.appbase.io/dejavu/live/#?input_state=XQAAAAJuAAAAAAAAAAA9iIqnY-B2BnTZGEQz6wkFs4RH-_LaQFp2SlHxdkdiaJMgDx8HsBmHrHmxFLRm7V1uYmmy_j7CIuOAUjTBNw0KgomWuYOXFddgJRsGIU7fsxTMJHKDeitU2LeOk2yVyC7H5mdPqXB8pzL_9FBmAA) directly or create one for yourself using [appbase.io](https://appbase.io/) which lets you create a hosted Elasticsearch index (aka app).

All the todos are structured in the following format:

```js
{
  "title": "react-native",
  "completed": true,
  "createdAt": 1518449005768
}
```

### The starter project

Before we get started, I would recommend installing [yarn](https://yarnpkg.com/lang/en/docs/install/). On Linux it can be done simply by adding the yarn repository and running the install command via your package manager. On Mac, you should install [Homebrew](https://brew.sh/) first to make things simpler. [Here](https://yarnpkg.com/lang/en/docs/install/) are the yarn installation docs for more detail. The next thing which you may install is [watchman](https://facebook.github.io/watchman/docs/install.html). Its a file watching service which will help the react-native packager to run smoothly.

I’ve setup the starter project with [create-react-native-app](https://github.com/react-community/create-react-native-app) in a GitHub branch [here](https://github.com/appbaseio-apps/todos-native/tree/base). You may [download a zip](https://github.com/appbaseio-apps/todos-native/archive/base.zip) or clone the base branch by running the following command: ?

```
git clone -b base https://github.com/appbaseio-apps/todos-native
```

* Next install the dependencies and start the packager:

```
cd todos-native && yarn && yarn start
```

* After the packager starts, you may run the app on your phone using the [Expo](https://expo.io/) app or using an Android or IOS emulator:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vTzfrdAPwha5GKpkzxaOeQ.png)
_Base setup with all tabs. Clone from [here](https://github.com/appbaseio-apps/todos-native/tree/base" rel="noopener" target="_blank" title=")._

### Diving into code ?

Once you have cloned the code from the [base branch](https://github.com/appbaseio-apps/todos-native/tree/base), you should see a directory structure like below:

```
navigation
├── RootComponent.js         // Root component for our app
├── MainTabNavigator.js      // Tab navigation component
screens
├── TodosScreen.js           // Renders the TodosContainer
components        
├── Header.js                // Header component         
├── AddTodo.js               // Add todo input        
├── AddTodoButton.js         // Add todo floating button
├── TodoItem.js              // The todo item         
├── TodosContainer.js        // Todos main container api
├── todos.js                 // APIs for performing writes
constants                    // All types of constants used in app
types                        // Todo type to be used with prop-types
utils                        // Streaming logic goes here
```

Let’s breakdown what the base setup comes with:

#### 1. Navigation

* All the necessary configurations for connecting to Elasticsearch are at `constants/Config.js`.
* We’re using [TabNavigator](https://reactnavigation.org/docs/tab-navigator.html) from [react-navigation](https://reactnavigation.org/) for showing the **All**, **Active** and **Completed** todos screen. This is rendered by the `navigation/RootComponent.js`. You’ll notice the `RootComponent` wraps everything inside the `[ReactiveBase](https://opensource.appbase.io/reactive-manual/getting-started/reactivebase.html)` component from ReactiveSearch. This component provides all the necessary data to the child ReactiveSearch components. You can connect your own Elasticsearch index here by just updating the configurations in `constants/Config.js`.

The navigation logic is present in `navigation/MainNavigator.js`. Lets go over how it works. [Here](https://reactnavigation.org/docs/tab-based-navigation.html) are the docs for tab navigation if you wish to reference anything.

```js
import React from 'react';
import { MaterialIcons } from '@expo/vector-icons';
import { TabNavigator, TabBarBottom } from 'react-navigation';

import Colors from '../constants/Colors';
import CONSTANTS from '../constants';
import TodosScreen from '../screens/TodosScreen';

const commonNavigationOptions = ({ navigation }) => ({
    header: null,
    title: navigation.state.routeName,
});

// we just pass these to render different routes
const routeOptions = {
    screen: TodosScreen,
    navigationOptions: commonNavigationOptions,
};

// different routes for all, active and completed todos
const TabNav = TabNavigator(
    {
        [CONSTANTS.ALL]: routeOptions,
        [CONSTANTS.ACTIVE]: routeOptions,
        [CONSTANTS.COMPLETED]: routeOptions,
    },
    {
        navigationOptions: ({ navigation }) => ({
            // this tells us which icon to render on the tabs
            tabBarIcon: ({ focused }) => {
                const { routeName } = navigation.state;
                let iconName;
                switch (routeName) {
                    case CONSTANTS.ALL:
                        iconName = 'format-list-bulleted';
                        break;
                    case CONSTANTS.ACTIVE:
                        iconName = 'filter-center-focus';
                        break;
                    case CONSTANTS.COMPLETED:
                        iconName = 'playlist-add-check';
                }
                return (
                    <MaterialIcons
                        name={iconName}
                        size={28}
                        style={{ marginBottom: -3 }}
                        color={focused ? Colors.tabIconSelected : Colors.tabIconDefault}
                    />
                );
            },
        }),
        // for rendering the tabs at bottom
        tabBarComponent: TabBarBottom,
        tabBarPosition: 'bottom',
        animationEnabled: true,
        swipeEnabled: true,
    },
);

export default TabNav;
```

* The `TabNavigator` function accepts two arguments, the first being the route configurations and the second being the `TabNavigator` configurations. In the above snippet, we’re passing the configurations for showing a tab navigation bar at the bottom and setting different icons for each tab.

#### 2. TodosScreen and TodosContainer

The `TodosScreen` component in `screens/TodosScreen.js` wraps our main `TodosContainer` component in `components/TodosContainer.js` where we’ll be adding various components for the app. The `TodosContainer` will show filtered data, based on whether we’re on the **All**, **Active,** or **Completed** tab.

#### 3. APIs for Creating, Updating and Deleting todos

The APIs for CUD operations on Elasticsearch are present in `api/todos.js` . It contains three simple methods `add`, `update` and `destroy` which work with any Elasticsearch index as specified in `constants/Config.js`. An important point to keep in mind is that each todo item we create will have a unique `_id` field. We can use this `_id` field for updating or deleting an existing todo.

For our app, we’ll just need three methods for adding, creating or deleting todos. However, you can find a detailed explanation about the API methods at the [docs](http://docs.appbase.io/javascript/api-reference.html).

### Building the components and UI ?

Lets start adding some components to complete the functionality of the app.

#### 1. Adding Todos

We’ll use `[Fab](https://docs.nativebase.io/Components.html#fabs-def-headref)` from `[native-base](http://docs.nativebase.io/)` to render a floating button for adding todos.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C1-bdZSvCajaJ-dtSsWcjg.png)

```js
const AddTodoButton = ({ onPress }) => (
  <Fab
      direction="up"
      containerStyle={{}}
      style={{ backgroundColor: COLORS.primary }}
      position="bottomRight"
      onPress={onPress}
  >
      <Icon name="add" />
  </Fab>
);
```

Now you can use this component in `components/TodosContainer.js`.

```javascript
import AddTodoButton from './AddTodoButton';
...
export default class TodosContainer extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        ...
        <AddTodoButton />
      </View>
    );
  }
}
```

Once we’ve added the button, we’ll see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vWdtqKsk0gZzMC4UO35IGg.png)
_After adding the AddTodoButton_

Now, when someones clicks on this button, we’ll need to show the input for adding a todo. Lets add the code for this in `components/AddTodo.js`.

```js
class AddTodo extends Component {
  constructor(props) {
    super(props);
    const { title, completed, createdAt } = this.props.todo;
    this.state = {
      title,
      completed,
      createdAt,
    };
  }

  onSubmit = () => {
    if (this.state.title.length > 0) this.props.onAdd(this.state);
    return null;
  };

  setStateUtil = (property, value = undefined) => {
    this.setState({
      [property]: value,
    });
  };

  render() {
    const { title, completed } = this.state;
    const { onBlur } = this.props;
    return (
      <View
        style={{
          flex: 1,
          width: '100%',
          flexDirection: 'row',
          alignItems: 'center',
          paddingRight: 10,
          paddingBottom: 5,
          paddingTop: 5,
        }}
      >
        <CheckBox checked={completed} onPress={() => this.setStateUtil('completed', !completed)} />
        <Body
          style={{
            flex: 1,
            justifyContent: 'flex-start',
            alignItems: 'flex-start',
            paddingLeft: 25,
          }}
        >
          <TextInput
            style={{ width: '90%' }}
            placeholder="What needs to be done?"
            autoFocus
            underLineColorAndroid="transparent"
            underlineColor="transparent"
            blurOnSubmit
            onSubmitEditing={this.onSubmit}
            onChangeText={changedTitle => this.setStateUtil('title', changedTitle)}
            value={title}
            autoCorrect={false}
            autoCapitalize="none"
            onBlur={onBlur}
          />
        </Body>
        <TouchableOpacity
          onPress={() => this.props.onCancelDelete}
          style={{ paddingLeft: 25, paddingRight: 15 }}
        >
          <Ionicons
            name="ios-trash-outline"
            color={`${title.length > 0 ? 'black' : 'grey'}`}
            size={23}
          />
        </TouchableOpacity>
      </View>
    );
  }
}
```



The main components used here are `[TextInput](https://facebook.github.io/react-native/docs/textinput.html)`, `[Checkbox](http://docs.nativebase.io/Components.html#checkbox-headref)` and `[Ionicons](https://expo.github.io/vector-icons/)` with straightforward props. We’re using `title` and `completed` from the `state`. We’ll be passing the props `todo`, `onAdd`, `onCancelDelete` and `onBlur` from the `components/TodosContainer.js`. These will help us in adding new todos or resetting the view if you wish to cancel adding todos.

Now we can update `components/TodosContainer.js` with the required changes for rendering `AddTodo` component:

```js
...
import AddTodoButton from './AddTodoButton';
import AddTodo from './AddTodo';
import TodoModel from '../api/todos';
...

// will render todos based on the active screen: all, active or completed
export default class TodosContainer extends React.Component {
  state = {
    addingTodo: false,
  };

  componentDidMount() {
    // includes the methods for creation, updation and deletion
    this.api = new TodoModel('react-todos');
  }

  render() {
    return (
      <View style={styles.container}>
        <Header />
        <StatusBar backgroundColor={COLORS.primary} barStyle="light-content" />
        <ScrollView>
          {this.state.addingTodo ? (
            <View style={styles.row}>
              <AddTodo
                onAdd={(todo) => {
                  this.setState({ addingTodo: false });
                  this.api.add(todo);
                }}
                onCancelDelete={() => this.setState({ addingTodo: false })}
                onBlur={() => this.setState({ addingTodo: false })}
              />
            </View>
          ) : null}
        </ScrollView>
        <AddTodoButton onPress={() => this.setState({ addingTodo: true })} />
      </View>
    );
  }
}
```

The `AddTodo` component is rendered inside a `[ScrollView](https://facebook.github.io/react-native/docs/scrollview.html)` component. We also pass an `onPress` prop to the `AddTodoButton` to toggle the state and conditionally display the `AddTodo` component based on `this.state.addingTodo`. The `onAdd` prop passed to `AddTodo` also creates a new todo using the `add` API at `api/todos.js`.

After clicking the add button, we’ll see the input for adding a todo like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*VrlfuWW4tdj0TTrGjSfDSw.png)
_Adding a todo_

#### 2. Displaying Todos

After you finish adding a todo, it’s added into Elasticsearch (which we configured in `constants/Config.js`). All this data can be viewed in realtime by using [ReactiveSearch Native](https://github.com/appbaseio/reactivesearch/tree/dev/packages/native) components.

There are over 10 native [UI components](https://opensource.appbase.io/reactive-manual/native/getting-started/componentsindex.html) that the library provides. For our todo app, we will primarily utilize the [ReactiveList](https://opensource.appbase.io/reactive-manual/native/components/reactivelist.html) component to show the state of todos.

Lets add the `ReactiveList` component and get our todos displaying. We’ll add this component in `components/TodosContainer.js` and the necessary methods for it to work. Here’s how the `ReactiveList` will be used:

```js

...
import { ReactiveList } from '@appbaseio/reactivesearch-native';
...

export default class TodosContainer extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Header />
        <StatusBar backgroundColor={COLORS.primary} barStyle="light-content" />
        <ScrollView>
          <ReactiveList
            componentId="ReactiveList"
            defaultQuery={() => ({
              query: {
                match_all: {},
              },
            })}
            stream
            onAllData={this.onAllData}
            dataField="title"
            showResultStats={false}
            pagination={false}
          />
          ...
        </ScrollView>
        <AddTodoButton onPress={() => this.setState({ addingTodo: true })} />
      </View>
    );
  }
}
```

We haven’t added the `onAllData` method yet, but let’s understand a bit about the props that we have used here:

* `componentId` — unique identifier for the component.
* `defaultQuery`: the query to be applied initially for the list. We’ll use `match_all` to show all the todos in default case.
* `stream`: whether to stream new result updates or just show historical results. By setting this to `true`, we now also listen for the live Todo updates. We’ll add the streaming related logic later.
* `onAllData` — a callback function which receives the list of current todo items and the streaming (new todos and any updates) and returns a React component or JSX to render. Here’s how the syntax looks like:

```js
<ReactiveList
  onAllData(todos, streamData) {
    // return the list to render
  }
  ...
/>
```

You can read more about all of these props in detail on the ReactiveList’s [docs page](https://opensource.appbase.io/reactive-manual/result-components/reactivelist.html).

To see something, we’ll need to return a JSX or React component from `onAllData` callback. For this, we will use React Native’s [FlatList](https://facebook.github.io/react-native/docs/flatlist.html) which is composed of [Text](https://facebook.github.io/react-native/docs/text.html) components. In the next step we’ll add our custom `TodoItem` component.

```js
...
import { ScrollView, StyleSheet, StatusBar, FlatList, Text } from 'react-native';
import CONSTANTS from '../constants';
...

export default class TodosContainer extends React.Component {
  ...
  onAllData = (todos, streamData) => {
    // filter data based on "screen": [All | Active | Completed]
    const filteredData = this.filterTodosData(todos);

    return (
      <FlatList
        style={{ width: '100%', top: 15 }}
        data={filteredData}
        keyExtractor={item => item._id}
        renderItem={({ item: todo }) => (
            <Text>{todo.title}</Text>
        )}
      />
    );
  };

  filterTodosData = (todosData) => {
    const { screen } = this.props;

    switch (screen) {
      case CONSTANTS.ALL:
        return todosData;
      case CONSTANTS.ACTIVE:
        return todosData.filter(todo => !todo.completed);
      case CONSTANTS.COMPLETED:
        return todosData.filter(todo => todo.completed);
    }

    return todosData;
  };

  render() {
    ...
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kobdkvtn9oZY7qvF9pzK0Q.png)
_Integrating ReactiveList with onAllData_

#### 3. Adding TodoItem(s)

Next, we’ll create a separate component **TodoItem** for showing each todo which will contain all necessary markups for a todo item like the [CheckBox](https://docs.nativebase.io/Components.html#checkbox-headref), [Text](https://facebook.github.io/react-native/docs/text.html), and a delete [Icon](https://docs.nativebase.io/Components.html#icon-def-headref). This goes in `components/TodoItem.js`:

```js
class TodoItem extends Component {
  onTodoItemToggle = (todo, propAction) => {
    propAction({
      ...todo,
      completed: !todo.completed,
    });
  };

  render() {
    const { todo, onUpdate, onDelete } = this.props;

    return (
      <View style={styles.row}>
        <View
          style={{
            flex: 1,
            width: '100%',
            flexDirection: 'row',
            alignItems: 'center',
            paddingRight: 10,
            paddingVertical: 5,
          }}
        >
          <TouchableOpacity
            onPress={() => this.onTodoItemToggle(todo, onUpdate)}
            style={{
              flex: 1,
              width: '100%',
              flexDirection: 'row',
            }}
          >
            <CheckBox
              checked={todo.completed}
              onPress={() => this.onTodoItemToggle(todo, onUpdate)}
            />
            <Body
              style={{
                flex: 1,
                justifyContent: 'flex-start',
                alignItems: 'flex-start',
                paddingLeft: 25,
              }}
            >
              <Text
                style={{
                  color: todo.completed ? 'grey' : 'black',
                  textDecorationLine: todo.completed ? 'line-through' : 'none',
                }}
              >
                {todo.title}
              </Text>
            </Body>
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() => onDelete(todo)}
            style={{ paddingLeft: 25, paddingRight: 15 }}
          >
            <Ionicons
              name="ios-trash-outline"
              color={`${todo.title.length > 0 ? 'black' : 'grey'}`}
              size={23}
            />
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}
```

This component gets the `todo` from its props along with `onDelete` and `onUpdate` which are used to update and delete the todo item respectively. We’re using these at the necessary places using the `onPress` prop of the components we’re using.

Next, we can `import` and use the `TodoItem` component in our `onAllData` in `components/TodosContainer.js`. We’ll pass the `todo` as a prop along with the API methods for `update` and `destroy` which will be used by `TodoItem` component.

```js
class TodosContainer extends Component {
  ...
  onAllData = (todos, streamData) => {
    ...
    return (
      <FlatList
        ...
        renderItem={({ item: todo }) => (
          <TodoItem 
            todo={todo}
            onUpdate={this.api.update} 
            onDelete={this.api.destroy}
          />
        )}
      />
    );
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*46QMtTpPsof09oOBwvrELA.png)
_After adding TodoItem in TodosContainer_

#### 4. Streaming Data Updates

You might have noticed that the todos are displaying fine, except you’re unable to view updated todos without refreshing the app. In this final step, we’re going to fit that missing part of the puzzle.

In the previous section, we added an `onAllData` method for the `ReactiveList` component. The second parameter of `onAllData` receives streaming updates which we’re going to utilize to always keep the todos updated. Here’s how the updated `onAllData` method will look like in `components/TodosContainer.js`.

```js
import Utils from '../utils';
...

export default class TodosContainer extends React.Component {
  ...
  onAllData = (todos, streamData) => {
    // merge streaming todos data along with current todos
    const todosData = Utils.mergeTodos(todos, streamData);

    // filter data based on "screen": [All | Active | Completed]
    const filteredData = this.filterTodosData(todosData);

    return (
      <FlatList
        style={{ width: '100%', top: 15 }}
        data={filteredData}
        keyExtractor={item => item._id}
        renderItem={({ item: todo }) => (
            <TodoItem todo={todo} onUpdate={this.api.update} onDelete={this.api.destroy} />
        )}
      />
    );
  };
  ...
}
```

The `mergeTodos` method is present in `utils/index.js`. Here’s how it works:

```js
class Utils {
  static mergeTodos(todos, streamData) {
    // generate an array of ids of streamData
    const streamDataIds = streamData.map(todo => todo._id);

    return (
      todos
        // consider streamData as the source of truth
        // first take existing todos which are not present in stream data
        .filter(({ _id }) => !streamDataIds.includes(_id))
        // then add todos from stream data
        .concat(streamData)
        // remove todos which are deleted in stream data
        .filter(todo => !todo._deleted)
        // finally sort on the basis of creation timestamp
        .sort((a, b) => a.createdAt - b.createdAt)
    );
  }
}

export default Utils;
```

The `streamData` receives an array of todo objects when they’re created, deleted, or updated. If an object is updated, it contains a `_updated` key set to `true`. Similarly, if an object is deleted, it contains a `_deleted` key set to `true`. If an object is created, it contains neither of the two. Using these points, we’ve added the `mergeTodos` function.

With this, you should be able to see the changes to todo items in realtime! If you have an additional device/emulator running the same app, both will stream new updates too. ?

### Useful links

1. Todos app [demo](https://snack.expo.io/@dhruvdutt/todo), [expo link](https://expo.io/@dhruvdutt/todos), [starter project](https://github.com/appbaseio-apps/todos-native/tree/base) and [final source code](https://github.com/appbaseio-apps/todos-native)
2. [ReactiveSearch GitHub repo](https://github.com/appbaseio/reactivesearch) ⭐️
3. ReactiveSearch [docs](https://opensource.appbase.io/reactive-manual/native)

Hope you enjoyed this story. If you have any thoughts or suggestions, please let me know and have fun!

---

You may follow me on [twitter](https://twitter.com/divyanshu013) for latest updates. I've also started posting more recent posts on my personal [blog](https://divyanshu013.dev/).

_Special thanks_ to [Dhruvdutt Jadhav](https://www.freecodecamp.org/news/how-to-build-a-real-time-todo-app-with-react-native-19a1ce15b0b3/undefined) for helping me with this story and the Todos app.

