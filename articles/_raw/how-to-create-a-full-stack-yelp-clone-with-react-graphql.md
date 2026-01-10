---
title: How to Create a Full-Stack Yelp Clone with React & GraphQL (Dune World Edition)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-05T19:05:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-full-stack-yelp-clone-with-react-graphql
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/article-cover.png
tags:
- name: Apps
  slug: apps-tag
- name: full stack
  slug: full-stack
- name: GraphQL
  slug: graphql
- name: React
  slug: react
seo_title: null
seo_desc: 'By Sezgi Ulucam


  I must not fear. Fear is the mind-killer. Fear is the little-death that brings total
  obliteration. I will face my fear. I will permit it to pass over me and through
  me. And when it has gone past I will turn the inner eye to see its p...'
---

By Sezgi Ulucam

> I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.
> \- "Litany Against Fear," Frank Herbert, Dune

You may be wondering, "What does fear have to do with a React app?" First of all, there's nothing to fear in a React app. In fact, in this particular app, we banned fear. Isn't that nice?

Now that you're ready to be fearless, let's discuss our app. It's a mini Yelp clone where instead of reviewing restaurants, users review planets from the classic sci-fi series, [Dune](https://en.wikipedia.org/wiki/Dune_(franchise)). (Why? Because there's a new Dune movie coming out... but back to the main point.)

To build our full-stack app, we'll use technologies that make our lives easy.

1. [React](https://reactjs.org/): Intuitive, compositional front-end framework, because our brains like to compose things.
2. [GraphQL](https://graphql.org/): You may have heard many reasons why GraphQL is awesome. By far, the most important one is **developer productivity and happiness**.
3. [Hasura](http://hasura.io/): Set up an auto-generated GraphQL API on top of a Postgres database in under 30 seconds.
4. [Heroku](https://heroku.com/): To host our database.

## And GraphQL gives me happiness how?

I see you're a skeptical one. But you'll most likely come around as soon as you spend some time with GraphiQL (the GraphQL playground). 

Using GraphQL is a breeze for the front-end developer, compared to the old ways of clunky REST endpoints. GraphQL gives you a single endpoint that listens to all your troubles... I mean queries. It's such a great listener that you can tell it exactly what you want, and it will give it to you, nothing less and nothing more.

Feeling psyched about this therapeutic experience? Let's dive into the tutorial so you can try it ASAP!

?? [**Here's the repo**](https://github.com/hasura/yelp-clone-react) if you'd like to code along.

# **P**art **1: S**earch

%[https://www.youtube.com/watch?v=lrYo_n-9LM8]

## **S**tep **1: D**eploy to Heroku

The first step of every good journey is sitting down with some hot tea and sipping it calmly. Once we've done that, we can deploy to Heroku from the [Hasura website](http://hasura.io/). This will set us up with everything we need: a Postgres database, our Hasura GraphQL engine, and some snacks for the journey.

![black-books.png](https://draftin.com/images/73048?token=L5lFsg6SzmNzsdweEfn9uOLF6qJwkU1loz9LvhE-2PP7sFmiI9nZZ6z87S0pZZZ1xikaO2Z_6GyGPxOzyt170p8)
_Not at all a Dune reference_

## Step 2: Create planets table

Our users want to review planets. So we create a Postgres table via the Hasura console to store our planet data. Of note is the evil planet, Giedi Prime, which has been drawing attention with its unconventional cuisine.

![Planets table](https://www.freecodecamp.org/news/content/images/2020/05/p1-s2-1.png)

Meanwhile in the GraphiQL tab: Hasura has auto-generated our GraphQL schema! Play around with the Explorer here ??

![GraphiQL Explorer](https://www.freecodecamp.org/news/content/images/2020/05/p1-s2-schema-1.png)

## **S**tep **3: C**reate React app

We'll need a UI for our app, so we create a React app and install some libraries for GraphQL requests, routing, and styles. (Make sure you have [Node](https://nodejs.org/) installed first.)

```bash
> npx create-react-app melange
> cd melange
> npm install graphql @apollo/client react-router-dom @emotion/styled @emotion/core
> npm start
```

## **S**tep **4: S**et up Apollo Client

[Apollo Client](https://www.apollographql.com/docs/react/v3.0-beta) will help us with our GraphQL network requests and caching, so we can avoid all that grunt work. We also make our first query and list our planets! Our app is starting to shape up.

```js
import React from "react";
import { render } from "react-dom";
import { ApolloProvider } from "@apollo/client";
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";
import Planets from "./components/Planets";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "[YOUR HASURA GRAPHQL ENDPOINT]",
  }),
});

const App = () => (
  <ApolloProvider client={client}>
    <Planets />
  </ApolloProvider>
);

render(<App />, document.getElementById("root"));
```

We test our GraphQL query in the Hasura console before copy-pasting it into our code.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/p1-s4-test-query-2.png)

```js
import React from "react";
import { useQuery, gql } from "@apollo/client";

const PLANETS = gql`
  {
    planets {
      id
      name
      cuisine
    }
  }
`;

const Planets = ({ newPlanets }) => {
  const { loading, error, data } = useQuery(PLANETS);

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  return data.planets.map(({id, name, cuisine}) => (
  	<div key={id}>
      <p>
      	{name} | {cuisine}
      </p>
    </div>
  ));
};

export default Planets;
```

## **S**tep **5: S**tyle list

Our planet list is nice and all, but it needs a little makeover with [Emotion](https://emotion.sh/) (see [repo](https://github.com/hasura/yelp-clone-react) for full styles).

![Styled list of planets](https://www.freecodecamp.org/news/content/images/2020/05/p1-s5-style-1.png)

## **S**tep **6: S**earch form & state

Our users want to search for planets and order them by name. So we add a search form that queries our endpoint with a search string, and pass in the results to `Planets` to update our planet list. We also use [React Hooks](https://reactjs.org/docs/hooks-reference.html) to manage our app state.

```js
import React, { useState } from "react";
import { useLazyQuery, gql } from "@apollo/client";
import Search from "./Search";
import Planets from "./Planets";

const SEARCH = gql`
  query Search($match: String) {
    planets(order_by: { name: asc }, where: { name: { _ilike: $match } }) {
      name
      cuisine
      id
    }
  }
`;

const PlanetSearch = () => {
  const [inputVal, setInputVal] = useState("");
  const [search, { loading, error, data }] = useLazyQuery(SEARCH);

  return (
    <div>
      <Search
        inputVal={inputVal}
        onChange={(e) => setInputVal(e.target.value)}
        onSearch={() => search({ variables: { match: `%${inputVal}%` } })}
      />
      <Planets newPlanets={data ? data.planets : null} />
    </div>
  );
};

export default PlanetSearch;
```

```js
import React from "react";
import { useQuery, gql } from "@apollo/client";
import { List, ListItem } from "./shared/List";
import { Badge } from "./shared/Badge";

const PLANETS = gql`
  {
    planets {
      id
      name
      cuisine
    }
  }
`;

const Planets = ({ newPlanets }) => {
  const { loading, error, data } = useQuery(PLANETS);

  const renderPlanets = (planets) => {
    return planets.map(({ id, name, cuisine }) => (
      <ListItem key={id}>
        {name} <Badge>{cuisine}</Badge>
      </ListItem>
    ));
  };

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  return <List>{renderPlanets(newPlanets || data.planets)}</List>;
};

export default Planets;
```

```js
import React from "react";
import styled from "@emotion/styled";
import { Input, Button } from "./shared/Form";

const SearchForm = styled.div`
  display: flex;
  align-items: center;
  > button {
    margin-left: 1rem;
  }
`;

const Search = ({ inputVal, onChange, onSearch }) => {
  return (
    <SearchForm>
      <Input value={inputVal} onChange={onChange} />
      <Button onClick={onSearch}>Search</Button>
    </SearchForm>
  );
};

export default Search;
```

```js
import React from "react";
import { render } from "react-dom";
import { ApolloProvider } from "@apollo/client";
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";
import PlanetSearch from "./components/PlanetSearch";
import Logo from "./components/shared/Logo";
import "./index.css";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "[YOUR HASURA GRAPHQL ENDPOINT]",
  }),
});

const App = () => (
  <ApolloProvider client={client}>
    <Logo />
    <PlanetSearch />
  </ApolloProvider>
);

render(<App />, document.getElementById("root"));
```

## **S**tep **7: B**e proud

We've already implemented our planet list and search features! We lovingly gaze upon our handiwork, take a few selfies together, and move on to reviews.

![Planet list with search](https://www.freecodecamp.org/news/content/images/2020/05/pt1-s7-finito.png)

# **P**art **2: L**ive reviews

%[https://www.youtube.com/watch?v=3kzXxc1XvRw]

## **S**tep **1: C**reate reviews table

Our users will be visiting these planets, and writing reviews about their experience. We create a table via the Hasura console for our review data.

![Reviews table](https://www.freecodecamp.org/news/content/images/2020/05/p2-s1-reviews-table-2.png)

We add a foreign key from the `planet_id` column to the `id` column in the `planets` table, to indicate that `planet_id`s of `reviews` have to match `id`'s of `planets`.

![Foreign keys](https://www.freecodecamp.org/news/content/images/2020/05/p2-s1-foreign-key-2.png)

## **S**tep **2: T**rack relationships

Each planet has multiple reviews, while each review has one planet: a one-to-many relationship. We create and track this relationship via the Hasura console, so it can be exposed in our GraphQL schema.

![Tracking relationships](https://www.freecodecamp.org/news/content/images/2020/05/p2-s2-track-2.png)

Now we can query reviews for each planet in the Explorer!

![Querying planet reviews](https://www.freecodecamp.org/news/content/images/2020/05/p2-s3-explorer-3.png)

## **S**tep **3: S**et up routing

We want to be able to click on a planet and view its reviews on a separate page. We set up routing with React Router, and list reviews on the planet page.

```js
import React from "react";
import { render } from "react-dom";
import { ApolloProvider } from "@apollo/client";
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import PlanetSearch from "./components/PlanetSearch";
import Planet from "./components/Planet";
import Logo from "./components/shared/Logo";
import "./index.css";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "[YOUR HASURA GRAPHQL ENDPOINT]",
  }),
});

const App = () => (
  <BrowserRouter>
    <ApolloProvider client={client}>
      <Logo />
      <Switch>
        <Route path="/planet/:id" component={Planet} />
        <Route path="/" component={PlanetSearch} />
      </Switch>
    </ApolloProvider>
  </BrowserRouter>
);

render(<App />, document.getElementById("root"));
```

```js
import React from "react";
import { useQuery, gql } from "@apollo/client";
import { List, ListItem } from "./shared/List";
import { Badge } from "./shared/Badge";

const PLANET = gql`
  query Planet($id: uuid!) {
    planets_by_pk(id: $id) {
      id
      name
      cuisine
      reviews {
        id
        body
      }
    }
  }
`;

const Planet = ({
  match: {
    params: { id },
  },
}) => {
  const { loading, error, data } = useQuery(PLANET, {
    variables: { id },
  });

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  const { name, cuisine, reviews } = data.planets_by_pk;

  return (
    <div>
      <h3>
        {name} <Badge>{cuisine}</Badge>
      </h3>
      <List>
        {reviews.map((review) => (
          <ListItem key={review.id}>{review.body}</ListItem>
        ))}
      </List>
    </div>
  );
};

export default Planet;
```

```js
import React from "react";
import { useQuery, gql } from "@apollo/client";
import { Link } from "react-router-dom";
import { List, ListItemWithLink } from "./shared/List";
import { Badge } from "./shared/Badge";

const PLANETS = gql`
  {
    planets {
      id
      name
      cuisine
    }
  }
`;

const Planets = ({ newPlanets }) => {
  const { loading, error, data } = useQuery(PLANETS);

  const renderPlanets = (planets) => {
    return planets.map(({ id, name, cuisine }) => (
      <ListItemWithLink key={id}>
        <Link to={`/planet/${id}`}>
          {name} <Badge>{cuisine}</Badge>
        </Link>
      </ListItemWithLink>
    ));
  };

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  return <List>{renderPlanets(newPlanets || data.planets)}</List>;
};

export default Planets;
```

## **S**tep **4: S**et up subscriptions

We install new libraries and set up Apollo Client to support subscriptions. Then, we change our reviews query to a subscription so it can show live updates.

```bash
> npm install @apollo/link-ws subscriptions-transport-ws
```

```js
import React from "react";
import { render } from "react-dom";
import {
  ApolloProvider,
  ApolloClient,
  HttpLink,
  InMemoryCache,
  split,
} from "@apollo/client";
import { getMainDefinition } from "@apollo/client/utilities";
import { WebSocketLink } from "@apollo/link-ws";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import PlanetSearch from "./components/PlanetSearch";
import Planet from "./components/Planet";
import Logo from "./components/shared/Logo";
import "./index.css";

const GRAPHQL_ENDPOINT = "[YOUR HASURA GRAPHQL ENDPOINT]";

const httpLink = new HttpLink({
  uri: `https://${GRAPHQL_ENDPOINT}`,
});

const wsLink = new WebSocketLink({
  uri: `ws://${GRAPHQL_ENDPOINT}`,
  options: {
    reconnect: true,
  },
});

const splitLink = split(
  ({ query }) => {
    const definition = getMainDefinition(query);
    return (
      definition.kind === "OperationDefinition" &&
      definition.operation === "subscription"
    );
  },
  wsLink,
  httpLink
);

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: splitLink,
});

const App = () => (
  <BrowserRouter>
    <ApolloProvider client={client}>
      <Logo />
      <Switch>
        <Route path="/planet/:id" component={Planet} />
        <Route path="/" component={PlanetSearch} />
      </Switch>
    </ApolloProvider>
  </BrowserRouter>
);

render(<App />, document.getElementById("root"));
```

```js
import React from "react";
import { useSubscription, gql } from "@apollo/client";
import { List, ListItem } from "./shared/List";
import { Badge } from "./shared/Badge";

const PLANET = gql`
  subscription Planet($id: uuid!) {
    planets_by_pk(id: $id) {
      id
      name
      cuisine
      reviews {
        id
        body
      }
    }
  }
`;

const Planet = ({
  match: {
    params: { id },
  },
}) => {
  const { loading, error, data } = useSubscription(PLANET, {
    variables: { id },
  });

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  const { name, cuisine, reviews } = data.planets_by_pk;

  return (
    <div>
      <h3>
        {name} <Badge>{cuisine}</Badge>
      </h3>
      <List>
        {reviews.map((review) => (
          <ListItem key={review.id}>{review.body}</ListItem>
        ))}
      </List>
    </div>
  );
};

export default Planet;
```

![Planet page with live reviews](https://www.freecodecamp.org/news/content/images/2020/05/p2-s5-finale-2.png)

## **S**tep **5: D**o a sandworm dance

We've implemented planets with live reviews! Do a little dance to celebrate before getting down to serious business.

![Worm dance](https://www.freecodecamp.org/news/content/images/2020/05/worm-dance.gif)

# **P**art **3: B**usiness logic

%[https://www.youtube.com/watch?v=picA-ORNNH8]

## **S**tep **1: A**dd input form

We want a way to submit reviews through our UI. We rename our search form to be a generic `InputForm` and add it above the review list.

```js
import React, { useState } from "react";
import { useSubscription, gql } from "@apollo/client";
import { List, ListItem } from "./shared/List";
import { Badge } from "./shared/Badge";
import InputForm from "./shared/InputForm";

const PLANET = gql`
  subscription Planet($id: uuid!) {
    planets_by_pk(id: $id) {
      id
      name
      cuisine
      reviews(order_by: { created_at: desc }) {
        id
        body
        created_at
      }
    }
  }
`;

const Planet = ({
  match: {
    params: { id },
  },
}) => {
  const [inputVal, setInputVal] = useState("");
  const { loading, error, data } = useSubscription(PLANET, {
    variables: { id },
  });

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  const { name, cuisine, reviews } = data.planets_by_pk;

  return (
    <div>
      <h3>
        {name} <Badge>{cuisine}</Badge>
      </h3>
      <InputForm
        inputVal={inputVal}
        onChange={(e) => setInputVal(e.target.value)}
        onSubmit={() => {}}
        buttonText="Submit"
      />
      <List>
        {reviews.map((review) => (
          <ListItem key={review.id}>{review.body}</ListItem>
        ))}
      </List>
    </div>
  );
};

export default Planet;
```

## **S**tep **2: T**est review mutation

We'll use a mutation to add new reviews. We test our mutation with GraphiQL in the Hasura console.

![Insert review mutation in GraphiQL](https://www.freecodecamp.org/news/content/images/2020/05/p3-s2-test-mutation-2.png)

And convert it to accept variables so we can use it in our code.

![Insert review mutation with variables](https://www.freecodecamp.org/news/content/images/2020/05/p3-s2-variables-2.png)

## **S**tep **3: C**reate action

The [Bene Gesserit](https://en.wikipedia.org/wiki/Bene_Gesserit) have requested us to not allow (_cough_ censor _cough_) the word "fear" in the reviews. We create an action for the business logic that will check for this word whenever a user submits a review.

!["Derive action" button](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-derive-action-2.png)

Inside our freshly minted action, we go to the "Codegen" tab.

!["Codegen" tab](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-codegen-2.png)

We select the nodejs-express option, and copy the handler boilerplate code below.

![Boilerplate code for nodejs-express](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-express-2.png)

We click "Try on Glitch," which takes us to a barebones express app, where we can paste our handler code.

![Pasting our handler code in Glitch](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-glitch-2.png)

Back inside our action, we set our handler URL to the one from our Glitch app, with the correct route from our handler code.

![Handler URL](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-handler-url-2.png)

We can now test our action in the console. It runs like a regular mutation, because we don't have any business logic checking for the word "fear" yet.

![Testing our action in the console](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-test-action-2.png)

## **S**tep **4: A**dd business logic

In our handler, we add business logic that checks for "fear" inside the body of the review. If it's fearless, we run the mutation as usual. If not, we return an ominous error.

![Business logic checking for "fear"](https://www.freecodecamp.org/news/content/images/2020/05/p3-s4-biz-logic-3.png)

If we run the action with "fear" now, we get the error in the response:

![Testing our business logic in the console](https://www.freecodecamp.org/news/content/images/2020/05/p3-s4-error-2.png)

## **S**tep **5: O**rder reviews

Our review order is currently topsy turvy. We add a `created_at` column to the `reviews` table so we can order by newest first.

```js
reviews(order_by: { created_at: desc })
```

## **S**tep **6: A**dd review mutation

Finally, we update our action syntax with variables, and copy paste it into our code as a mutation. We update our code to run this mutation when a user submits a new review, so that our business logic can check it for compliance (_ahem_ obedience _ahem_) before updating our database.

```js
import React, { useState } from "react";
import { useSubscription, useMutation, gql } from "@apollo/client";
import { List, ListItem } from "./shared/List";
import { Badge } from "./shared/Badge";
import InputForm from "./shared/InputForm";

const PLANET = gql`
  subscription Planet($id: uuid!) {
    planets_by_pk(id: $id) {
      id
      name
      cuisine
      reviews(order_by: { created_at: desc }) {
        id
        body
        created_at
      }
    }
  }
`;

const ADD_REVIEW = gql`
  mutation($body: String!, $id: uuid!) {
    AddFearlessReview(body: $body, id: $id) {
      affected_rows
    }
  }
`;

const Planet = ({
  match: {
    params: { id },
  },
}) => {
  const [inputVal, setInputVal] = useState("");
  const { loading, error, data } = useSubscription(PLANET, {
    variables: { id },
  });
  const [addReview] = useMutation(ADD_REVIEW);

  if (loading) return <p>Loading ...</p>;
  if (error) return <p>Error :(</p>;

  const { name, cuisine, reviews } = data.planets_by_pk;

  return (
    <div>
      <h3>
        {name} <Badge>{cuisine}</Badge>
      </h3>
      <InputForm
        inputVal={inputVal}
        onChange={(e) => setInputVal(e.target.value)}
        onSubmit={() => {
          addReview({ variables: { id, body: inputVal } })
            .then(() => setInputVal(""))
            .catch((e) => {
              setInputVal(e.message);
            });
        }}
        buttonText="Submit"
      />
      <List>
        {reviews.map((review) => (
          <ListItem key={review.id}>{review.body}</ListItem>
        ))}
      </List>
    </div>
  );
};

export default Planet;
```

If we submit a new review that includes "fear" now, we get our ominous error, which we display in the input field.

![Testing our action via the UI](https://www.freecodecamp.org/news/content/images/2020/05/p3-s6-test-final-ui-2.png)

## Step 7: We did it! ?

Congrats on building a full-stack React & GraphQL app!

![High five](https://www.freecodecamp.org/news/content/images/2020/05/high-five.gif)

# What does the future hold?

![spice_must_flow.jpg](https://draftin.com/images/73049?token=kxAhFBHMt0pOLjXmaJQRIXSqFGtjWxb-WBuwPn2cjwPgL0mQP8TxoV4mqiQwXBotJ4cdCCRbehNabJMt2l9pvLA)

If only we had some spice melange, we would know. But we built so many features in so little time! We covered GraphQL queries, mutations, subscriptions, routing, searching, and even custom business logic with Hasura actions! I hope you had fun coding along.

What other features would you like to see in this app? Reach out to me on Twitter, and I'll make more tutorials! If you're inspired to add features yourself, please [do share](https://twitter.com/sez) – I'd love to hear about them :)

