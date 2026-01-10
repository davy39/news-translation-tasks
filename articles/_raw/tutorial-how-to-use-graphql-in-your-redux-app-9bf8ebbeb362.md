---
title: How to use GraphQL in your Redux app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-22T06:17:24.000Z'
originalURL: https://freecodecamp.org/news/tutorial-how-to-use-graphql-in-your-redux-app-9bf8ebbeb362
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ItpcYJftmpYtiCk1GxO8bQ.png
tags:
- name: GraphQL
  slug: graphql
- name: Node.js
  slug: nodejs
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Howon Song

  Fetching and managing data in Redux requires too much work. As Sashko Stubailo points
  out:


  Unfortunately the patterns for asynchronously loading server data in a Redux app
  aren’t as well established, and often involve using external he...'
---

By Howon Song

Fetching and managing data in Redux requires too much work. As [Sashko Stubailo](https://www.freecodecamp.org/news/tutorial-how-to-use-graphql-in-your-redux-app-9bf8ebbeb362/undefined) [points out](https://medium.com/apollo-stack/apollo-client-graphql-with-react-and-redux-49b35d0f2641#.mf2w6kh2j):

> Unfortunately the patterns for asynchronously loading server data in a Redux app aren’t as well established, and often involve using external helper libraries, like [redux-saga](https://github.com/yelouafi/redux-saga). You need to write custom code to call your server endpoints, interpret the data, normalize it, and insert it into the store — all while keeping track of various error and loading states.

By the end of this tutorial, you will have learned how to solve this problem by letting the Apollo Client fetch and manage data for you. You will no longer have to write multiple action dispatchers, reducers, and normalizers to fetch and sync data between your front end and your back end.

But before starting the tutorial, make sure that:

* You know the basics of GraphQL queries — if you’re entirely new to GraphQL, you should come back after doing this [tutorial](https://learngraphql.com/).
* You have some experience working with React/Redux — if not, you should come back after doing [react tutorial](https://facebook.github.io/react/docs/getting-started.html) and [redux tutorial](http://redux.js.org/docs/introduction/Motivation.html).

In this tutorial, we will go through 6 sections together.

1. Setting up server environment (quick)
2. Setting up redux boilerplate app
3. Adding GraphQL client (Apollo Client)
4. Fetching data with GraphQL query
5. Fetching even more data
6. Next steps

#### 1. Setting up server environment

First, we need a GraphQL server. The easiest way to have a running server is completing this awesome [tutorial](https://medium.com/apollo-stack/tutorial-building-a-graphql-server-cddaa023c035#.9f3v0r5ix).

If you are feeling lazy, you can just clone my [repo](https://github.com/woniesong92/apollo-starter-kit.git), which is almost the same server you’d get if you did the tutorial yourself. The server supports GraphQL queries to fetch data from a SQLite DB.

Let’s run it and see if it’s working correctly:

```
$ git clone https://github.com/woniesong92/apollo-starter-kit$ cd apollo-starter-kit$ npm install$ npm start
```

The server should be running at [http://localhost:8080/graphql](http://localhost:8080/graphql). Navigate to that page and see if you get a working GraphiQL interface with results like this:

![Image](https://cdn-media-1.freecodecamp.org/images/d3InQW6BYBXEZxgqjmSctEAYBvFezLSShkdq)

GraphiQL lets you test different queries and immediately see what response you get from the server. If we don’t want an author’s last name and a fortune cookie message in a response, we can update the query like below:

![Image](https://cdn-media-1.freecodecamp.org/images/pigA9zhd8bbXB0ZUSnh0qW1h9dr2Spo80MzE)

And that’s exactly how we like it. We confirmed that our server is running fine and returning good responses, so let’s start building the client.

#### 2. Setting up redux boilerplate app

For simplicity, we will use a [redux boilerplate](https://github.com/davezuko/react-redux-starter-kit) so we can get all the setup (e.g. Babel, webpack, CSS, etc.) for free. I like this boilerplate because its setup is easy to follow and is client-side only — which makes it perfect for this tutorial.

```
$ git clone https://github.com/woniesong92/react-redux-starter-kit.git$ cd react-redux-starter-kit$ npm install$ npm start
```

Let’s navigate to [http://localhost:3000/](http://localhost:3000/) to see if the client server is running.

![Image](https://cdn-media-1.freecodecamp.org/images/9I6YDSNjFPPbWb0E7QngMQIgO4v14SgHKNvI)

Yay! The client is running. It’s time for us to start adding a GraphQL client. Again, our goal is to easily fetch data from the server and render it in the landing page (HomeView) without much effort by using GraphQL queries.

#### 3. Adding GraphQL client (Apollo Client)

Install the packages apollo-client, react-apollo, and graphql-tag.

```
$ npm install apollo-client react-apollo graphql-tag --save
```

Then, open the file src/containers/AppContainer.js, the root of our Redux app. This is where we pass down the redux store to child components, using the Provider from react-redux.

```
import React, { PropTypes } from 'react'import { Router } from 'react-router'import { Provider } from 'react-redux'
```

```
class AppContainer extends React.Component {  static propTypes = {    history: PropTypes.object.isRequired,    routes: PropTypes.object.isRequired,    routerKey: PropTypes.number,    store: PropTypes.object.isRequired  }
```

```
render () {    const { history, routes, routerKey, store } = this.props
```

```
return (      <Provider store={store}>        <div>          <Router history={history} children={routes} key={routerKey} />        </div>      </Provider>    )  }}
```

```
export default AppContainer
```

We have to initialize an ApolloClient and replace the Provider from react-redux with ApolloProvider from react-apollo.

```
import React, { Component, PropTypes } from 'react'import { Router } from 'react-router'import ApolloClient, { createNetworkInterface, addTypename } from 'apollo-client'import { ApolloProvider } from 'react-apollo'
```

```
const client = new ApolloClient({  networkInterface: createNetworkInterface('http://localhost:8080/graphql'),  queryTransformer: addTypename,})
```

```
class AppContainer extends Component {  static propTypes = {    history: PropTypes.object.isRequired,    routes: PropTypes.object.isRequired,    store: PropTypes.object.isRequired  }
```

```
render () {    const { history, routes } = this.props
```

```
return (      <ApolloProvider client={client}>        <div>          <Router history={history} children={routes} />        </div>      </ApolloProvider>    )  }}
```

```
export default AppContainer
```

That’s it! We just added a GraphQL client to a plain Redux app that easily.

Let’s go ahead and try our first GraphQL query.

#### 4. Fetching data with GraphQL queries

Open src/views/HomeView.js

```
import React from 'react'import { connect } from 'react-redux'import { bindActionCreators } from 'redux'
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
// This is where you usually retrieve the data stored in the redux store (e.g posts: state.posts.data)const mapStateToProps = (state, { params }) => ({
```

```
})
```

```
// This is where you usually bind dispatch to actions that are used to request data from the backend. You will call the dispatcher in componentDidMount.const mapDispatchToProps = (dispatch) => {  const actions = {}
```

```
  return {    actions: bindActionCreators(actions, dispatch)  }}
```

```
export default connect(  mapStateToProps,  mapDispatchToProps)(HomeView)
```

HomeView is a conventional Redux container (smart component). To use GraphQL queries instead of action dispatchers to fetch data, we will make some changes together.

1. Remove mapDispatchToProps() and mapStateToProps() completely.

```
import React from 'react'import { connect } from 'react-redux'import { bindActionCreators } from 'redux'
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
  render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
export default connect({
```

```
})(HomeView)
```

2. Add mapQueriesToProps() and define a GraphQL query that will fetch the author information. Notice how this is the exactly the same query that we tested in the beginning using the GraphIQL interface on the server.

```
import React from 'react'import { connect } from 'react-redux'import { bindActionCreators } from 'redux'
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
  render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
// NOTE: This will be automatically fired when the component is rendered, sending this exact GraphQL query to the backend.const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          author(firstName:"Edmond", lastName: "Jones"){            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({
```

```
})(HomeView)
```

3. Replace connect from react-redux with connect from react-apollo and pass mapQueriesToProps as argument. Once mapQueriesToProps is connected to ApolloClient, the query will automatically fetch the data from the backend when HomeView is rendered, and pass the data down through props.

```
import React from 'react'import { connect } from 'react-apollo' // NOTE: different connect!import gql from 'graphql-tag' // NOTE: lets us define GraphQL queries in a template language
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
render () {    return (      <div className='home'>        <h1>Hello World</h1>      </div>    )  }}
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          author(firstName:"Edmond", lastName: "Jones"){            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

4. Render the data that’s passed down from the props:

```
import React from 'react'import { connect } from 'react-apollo' // NOTE: different connect!import gql from 'graphql-tag' // NOTE: lets us define GraphQL queries in a template language
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
  render () {    const author = this.props.data.author    if (!author) {      return <h1>Loading</h1>    }
```

```
    return (      <div>        <h1>{author.firstName}'s posts</h1>        {author.posts && author.posts.map((post, idx) => (          <li key={idx}>{post.title}</li>        ))}      </div>    )  }}
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          author(firstName:"Edmond", lastName: "Jones"){            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

If all went well, your rendered HomeView should look like below:

![Image](https://cdn-media-1.freecodecamp.org/images/E2gXbodtbyO-a59P8MJKn6g0P1WeiKGeh9of)

To fetch and render the data we wanted, we didn’t have to write any action dispatcher, reducer, or normalizer. All we had to do on the client was to write a single GraphQL query!

We successfully achieved our initial goal. But that query was quite simple. What if we wanted to display all authors instead of just one author?

#### 5. Fetching even more data

In order to fetch and display all authors, we have to update our GraphQL query and render method:

```
import React from 'react'import { connect } from 'react-apollo' // NOTE: different connect!import gql from 'graphql-tag' // NOTE: lets us define GraphQL queries in a template language
```

```
export class HomeView extends React.Component {  constructor(props) {    super(props)  }
```

```
render () {    const authors = this.props.data.authors    if (!authors) {      return <h1>Loading</h1>    }
```

```
    return (      <div>        {authors.map((author, idx) => (          <div key={'author-'+idx}>            <h1>{author.firstName}'s posts</h1>            {author.posts && author.posts.map((post, idx) => (              <li key={idx}>{post.title}</li>            ))}          </div>        ))}      </div>    )  }}
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          authors {            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

However, once you refresh your browser HomeView page, you will notice that you have an error in your console:

_ApolloError {graphQLErrors: Array[1], networkError: undefined, message: “GraphQL error: Cannot query field “authors” on type “Query”. Did you mean “author”?”}_

Ah, right! In our GraphQL server, we didn’t really define how to fetch _authors_.

Let’s go back to our server and see what we have. Open the file apollo-starter-kit/data/resolvers.js

```
import { Author, FortuneCookie } from './connectors';
```

```
const resolvers = {  Query: {    author(_, args) {      return Author.find({ where: args });    },    getFortuneCookie() {      return FortuneCookie.getOne()    }  },  Author: {    posts(author) {      return author.getPosts();    },  },  Post: {    author(post) {      return post.getAuthor();    },  },};
```

```
export default resolvers;
```

Looking at Query resolver, we notice that our GraphQL server only understands _author_ and _getFortuneCookie_ queries now. We should teach it how to “resolve” the query _authors._

```
import { Author, FortuneCookie } from './connectors';
```

```
const resolvers = {  Query: {    author(_, args) {      return Author.find({ where: args });    },    getFortuneCookie() {      return FortuneCookie.getOne()    },    authors() { // the query "authors" means returning all authors!      return Author.findAll({})    }  },  ...};
```

```
export default resolvers;
```

We are not done yet. Open the file apollo-starter-kit/data/schema.js

```
const typeDefinitions = `...
```

```
type Query {  author(firstName: String, lastName: String): Author  getFortuneCookie: String}schema {  query: Query}`;
```

```
export default [typeDefinitions];
```

This Schema makes it clear what kind of queries the server should expect. It doesn’t expect _authors_ query yet so let’s update it.

```
const typeDefinitions = `...
```

```
type Query {  author(firstName: String, lastName: String): Author  getFortuneCookie: String,  authors: [Author] // 'authors' query should return an array of                     // Author}schema {  query: Query}`;
```

```
export default [typeDefinitions];
```

Now that our GraphQL server knows what the “authors” query means, let’s go back to our client. We already updated our query so we don’t have to touch anything.

```
export class HomeView extends React.Component {
```

```
...
```

```
const mapQueriesToProps = ({ ownProps, state }) => {  return {    data: {      query: gql`        query {          authors {            firstName            posts {              title            }          }        }      `    }  }}
```

```
export default connect({  mapQueriesToProps})(HomeView)
```

With this query we expect to get all authors with their first names and posts. Go ahead and refresh the browser to see if we are getting the right data.

![Image](https://cdn-media-1.freecodecamp.org/images/IO6Xv-2NVPI1eCan85UgeJZghfpDF-Ouj7Ec)

If everything went well, your HomeView page will look like above.

#### 6. Next steps

This tutorial only explores a small part of GraphQL and leaves out a lot of concepts such as updating data on the server or using a different backend server (e.g. Rails).

While I work to introduce these in subsequent tutorials, you can read Sashko’s [post](https://medium.com/apollo-stack/apollo-client-graphql-with-react-and-redux-49b35d0f2641#.iqsgdstls) or the [Apollo Client Doc](http://docs.apollostack.com/apollo-client/) to better understand what’s going on under the hood (for example, what happened when we replaced Provider with ApolloProvider?).

Digging into the source code of [GitHunt](https://github.com/apollostack/GitHunt), a full-stack Apollo Client and Server example app, also seems a great way to learn.

If you have feedback, please leave it in the comment. I will try my best to be helpful :)

