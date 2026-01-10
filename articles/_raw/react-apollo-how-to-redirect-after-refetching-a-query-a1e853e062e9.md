---
title: 'React + Apollo: How to Redirect after Refetching a Query'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T04:42:56.000Z'
originalURL: https://freecodecamp.org/news/react-apollo-how-to-redirect-after-refetching-a-query-a1e853e062e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*z-LROfr9BoiuMhlra-_OZQ.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jun Hyuk Kim

  GraphQL is hot, and for a good reason. In short, it is a query language that allows
  you to ask for exactly what you need from your API. This cuts any unnecessary data
  transfer that may occur with different methodologies.

  I was working...'
---

By Jun Hyuk Kim

[GraphQL](https://graphql.org/) is hot, and for a good reason. In short, it is a query language that allows you to ask for _exactly_ what you need from your API. This cuts any unnecessary data transfer that may occur with different methodologies.

I was working on a project where I was using a GraphQL back-end. I decided to use React and Apollo Client as my front-end to communicate with my GraphQL back-end. I was having some difficulty figuring out how to refetch my query, and then have my page redirected to the main page with the updated data. Here’s where things started to get a little bit tricky.

The problem, for me, was figuring out how the mutation was actually called, and what was returned. We can access the mutation after connecting it via the `graphql(mutation)(*YourComponent*)` through `this.props.mutate()`. This function returns a Promise. We can chain `.then()` functions to call functions after the mutation. The mutate function can also take in variables for the mutation. A full example would be something like this:

```
this.props.mutate({  variables:{    title: this.state.title,    content: this.state.content  }})
```

This would mean that our mutation is taking in two variables, called title and content. They are passed into our mutation when we send it to our back-end server. Let’s say our mutation is adding a note, with a title and content. To make things clear, I’ll include a simple example of what our mutation would look like:

```
const mutation = gql`  mutation AddNote($title: String, $content: String){    addNote(title:$title, content:$content){      title      content    }  }}`
```

```
// Our component should also be connected to Apollo client, so // something like this
```

```
export default graphql(mutation)(Component)
```

So, what happens after this function occurs? Our back-end receives the information, and the mutation occurs. However, our front-end doesn’t know that the mutation occurred. It doesn’t refetch the query that we previously fetched (in our case, maybe something like fetchAllNotes). This is where the mutate function gets pretty handy. We can pass in a variable called `refetchQueries`, which will refetch any queries we ask for.

```
this.props.mutate({  variables:{    title: this.state.title,    content: this.state.content  },  refetchQueries:[{    query: fetchAllNotes  }]}).then(() => this.props.history.push('/notes'))
```

In this case, we’re telling the Apollo client to refetch the `fetchAllNotesquery` after the mutation occurs. Then redirecting the user to the `/notes` directory (React-Router). Remember that our mutate function returns a Promise? This should all work, right? Well… by design, the Apollo team made it so that `refetchQueries` would happen **at the same time** as the `.then` statement. This means that the .then statement can occur before `refetchQueries`. This can lead to the component needing the updated info to not being updated.

In this specific case, what would happen is our user will be redirected _before_ the `refetchQueries` occurs. The information will not be updated. This is tricky because the mutate function returns a Promise. The Apollo team made it by _design_ so that `refetchQueries` can happen alongside any `.then` statements. So, how do we deal with this?

The Apollo team realized that this could potentially be a problem. They came out with a [solution](https://github.com/apollographql/apollo-client/pull/3169), which allows for the `refetchQueries` to take in a variable that would allow for it to return a Promise, and thus happen before any `.then` statements. Our code would look something like this:

```
this.props.mutate({  variables:{    title: this.state.title,    content: this.state.content  },  refetchQueries:[{    query: fetchAllNotes,    variables:{      awaitRefetchQueries: true    }  }]}).then(() => this.props.history.push('/notes'))
```

If this worked for you, woohoo! Looks like the fix worked! However, this did not work for me personally. Also, because it is only available on the more recent versions of Apollo Client, it will not be available in older versions of Apollo Client.

I had to do a bit of problem-solving with React component life cycles to make sure my component would correctly render the updated data. The fix itself is pretty short and pretty straightforward! On my Notes component, which renders the notes and is connected to the `fetchAllNotes` query by the `graphql` function, I added a quick fix to make sure my data was correctly rendered.

```
componentDidUpdate(prevProps){  if(prevProps.data.notes && prevProps.data.notes.length !==     this.props.data.notes.length){    // Logic to update component with new data  }}
```

Basically, we’re saying that when the component updates, we want to see if the notes query was previously completed (checking if `prevProps.data.notes` exists) and if the length of the data changed. This allows for our React component to update the information once the refetch query is complete.

Everything should work now! Hopefully the `awaitRefetchQueries` variable worked for you and becomes more known, which is a much more elegant solution. However, it’s pretty difficult to find examples/documentation of how to use `awaitRefetchQueries` properly. For now, having good understanding of React component life cycles is enough to help you go around the “Gotchas” of Apollo + React!

Please feel free to leave any feedback or questions in the comments, and I’ll do my best to help. I’m in no way an expert, but I would love to problem solve with you and help figure it out!

