---
title: How to do Apollo HOC mutations the right way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-04T06:39:43.000Z'
originalURL: https://freecodecamp.org/news/do-apollo-hoc-mutations-goodly-bb4effdbee94
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C1932-kODhSC6ibR7kUxNA.jpeg
tags:
- name: apollo client
  slug: apollo-client
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Lachlan Young

  Chances are, like many people, you’re coming to Apollo and GraphQL from a REST API
  background. Yet as you begin to explore the working examples of this stack and the
  different ways to implement it, you will no doubt be tripped up on ...'
---

By Lachlan Young

Chances are, like many people, you’re coming to Apollo and GraphQL from a REST API background. Yet as you begin to explore the working examples of this stack and the different ways to implement it, you will no doubt be tripped up on a multitude of differences, whether it’s Apollo’s Libraries, or the entire ‘get your data as you want it’ mentality around GraphQL and Apollo’s render components.

What I want to do in this article is help address two of the key issues when writing a mutation. This primarily targets HOC implementations, however it is more or less the same for the render components, tweaking object keys to props instead.

Specifically, we will be jumping straight into the optimisticResponse along with the update parameters of your HOC mutation. It is my hope that this will make you more aware of what options you have when it comes to implementing a mutation as a prop function.

**Important:** If you are only just getting started with Apollo, I wholeheartedly implore you to implement their render components that they released around version 2.1. HOCs are soft deprecated and as such, are missing a lot of their documentation, as mentioned by a few people [here](https://github.com/apollographql/apollo-client/issues/3253).

### Optimistic Response

optimisticResponse is the way we manage if our app is online or not along with the status of our requests to the DB.

If we mutate our database without a connection, the optimistic response allows it to exist with variables that we reasonably expect.

**For example**, if we assume that we will add this user to the db:

```
{    userId: 123,    firstName: "Lachlan",    lastName: "Young",    status: "Hungry"}
```

We would want to update our user details with the above data. However, because of the way our mutations work (and this is specifically for HOCs but can be applied to Render components too), there is a lifecycle to the mutation, going from loading, to success/fail/can’t connect.

If at any point the mutation fails but does not error, your Apollo client knows that this was because of something other than a bad object. By this I mean it takes into account your offline status, the status of the request, and it will instead render that user to the user details component, because it assumes it is valid. Therefore your client is being optimistic.

When you connect to the internet again or reach your DB, it will update the response with the valid data. Inside of that response you can handle stuff like userId’s which you generate on the client, therefore updating my hardcoded id of 123, to a UUID.

If we weren’t online we could still see and interact with the request as expected and any changes would be queued to then mutate the server upon reconnecting.

That’s an optimistic response.

### Update

As for how to handle the response from the database, you actually have access to a property called **update**, and for HOCs it looks like this:

```
update: (proxy, { data: { myDetails } }) => {    try {        // Read the data from our cache for this query.        const data = proxy.readQuery({             query: gql`${GET_MY_DETAILS}`        });
```

```
        // Add our new request from the mutation to the end.        data.getMyDetails.push(myDetails);
```

```
        // Write our data back to the cache.        proxy.writeQuery({             query: gql`${GET_MY_DETAILS}`,            data        });    } catch (err) {        console.log('Error updating the cahche: ', err.message);    }}
```

Essentially this comes after the optimisticResponse field in the mutation. It directly handles what happens after you receive a response, taking it from the top it has `proxy` and `data` as it’s two arguments. `Proxy` is quite literally our client, however for some configurations you may be better served referencing it as the cache. `Data` is the response from the mutation. I’ve deconstructed it, in this case, to explain the myDetails object further.

**myDetails** consists of everything in the user object above, but the id will now be a valid UUID instead of 123. We then use the apolloClient’s methods for reading and writing and read the details we have saved in our cache. From there we add our new details and re-write them to the cache. This way after I navigate back to my details from the input page, my new details will instantly be available because they are the point of truth in the cache.

### Additional Information

As of writing this, all the render props documented [here](https://www.apollographql.com/docs/react/api/react-apollo.html#mutation-props), or seen below for longevitiy, can be applied to your HOC mutation. As I mentioned in the introduction to this article, the HOC documentation has indeed been deprecated. However, the options given below can all be implemented as keys to the HOC object.

![Image](https://cdn-media-1.freecodecamp.org/images/ZSBBl-U4RRMGxZ6RavWDiL0RRlvTi5-h92MP)
_Mutation Props **4/12/2018**_

Thank you very much for reading. You can usually see me floating around the Apollo Slack in either the #React-Apollo or #Apollo-Client channels. To register for the slack and get more specific advice, click [here](https://www.apollographql.com/slack/).

