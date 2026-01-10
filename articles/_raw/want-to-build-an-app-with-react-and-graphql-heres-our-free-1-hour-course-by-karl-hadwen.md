---
title: Want to build an app with React and GraphQL? Here's our free 1-hour course
  by Karl Hadwen
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-18T20:00:00.000Z'
originalURL: https://freecodecamp.org/news/want-to-build-an-app-with-react-and-graphql-heres-our-free-1-hour-course-by-karl-hadwen
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-09-at-18.33.24.png
tags:
- name: GraphQL
  slug: graphql
- name: React
  slug: react
- name: Scrimba
  slug: scrimba
seo_title: null
seo_desc: 'By Per Harald Borgen

  If you''ve ever wondered how to connect React.js & GraphQL, then Scrimba''s hot
  one hour course is for you! The course jumps right into using a wide range of technologies
  to build a fast application with a concise amount of code - ...'
---

By Per Harald Borgen

If you've ever wondered how to connect React.js & GraphQL, then Scrimba's hot [one hour course](https://scrimba.com/course/greactgraphql?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) is for you! The course jumps right into using a wide range of technologies to build a fast application with a concise amount of code - what's not to love?

## Why learn React and GraphQL?

GraphQL has a faster build and iteration time than REST APIs and reduces the amount of data sent from the server. This means faster and more responsive apps - a must for any React developer.

## Intro to the instructor

This course is brought to you by Karl Hadwen - a JavaScript and React developer with over ten years of experience. Karl also runs a [YouTube channel](https://www.youtube.com/channel/UC1DUQiZduv_yNZy0O7n_iHA) teaching React, JavaScript, and GraphQL, so he's just the person to help you level up your React and GraphQL skills.

## What's covered in the course?

In this course, we'll learn how to build a fun front-end application that uses React, GraphQL, and Apollo to display Pokemon characters, facts and images! The course is interactive and to-the-point, meaning you'll build something like this in no time:

[![Pokemon app UI](https://dev-to-uploads.s3.amazonaws.com/i/m93x4nidm7dfqsnaohbm.png)](https://scrimba.com/p/pdqXpfD/ckRd6NU9?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Click the image to access the course._

In true Scrimba tradition, Karl's course is jam-packed with interactive coding challenges to help you apply your knowledge and embed your learning, so head over [to Scrimba](https://scrimba.com/course/greactgraphql?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) now and read on to find out more.

## Welcome to the course

In [the first scrim](https://scrimba.com/p/pdqXpfD/ckRd6NU9?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), Karl introduces us to the technologies we'll use in the course, which are:

- React
- GraphQL
- Apollo
- CSS
- the Pokemon open API.

## Installing our dependencies & creating our skeleton project

[![Apollo, GraphQL and React dependencies added to the project](https://dev-to-uploads.s3.amazonaws.com/i/an3cm74ty42qt0e4ptsm.png)](https://scrimba.com/p/pdqXpfD/ckRdVWSD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Click the image to access the course._

Now it's time to [start our project](https://scrimba.com/p/pdqXpfD/ckRdVWSD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article). First things first, we install the Apollo, GraphQL and React dependencies. Next up, we build up the files and folders we need for our project:

```js
import React from "react";
import { render } from "react-dom";
import { App } from "./App";

render(<App />, document.getElementById("root"));
```

## Giving our application life!

Now it's time to give our application life by adding to our app file and hitting the GraphQL server:

```js
export function App() {
	const client = new ApolloClient({
		uri: "https://graphql-pokemon.now.sh",
	});

	return <p>I am a Pokemon</p>;
}
```

[This scrim](https://scrimba.com/p/pdqXpfD/c8qgp9TZ?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) takes us through the following steps to allow our user to interact with our application:

- setting up the Apollo client
- building the `ApolloProvider` and passing in the client as a prop
- adding our `<main>` tag and `PokemonsContainer`

## Let's talk about GraphQL

[![fields which can be returned from pokemon open API](https://dev-to-uploads.s3.amazonaws.com/i/trsebt5rtu5zyetzn40b.png)](https://scrimba.com/p/pdqXpfD/cmmdmvc6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Click the image to access the course._

[This scrim](https://scrimba.com/p/pdqXpfD/cmmdmvc6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) takes a look at [the GraphQL server](https://graphql-pokemon.now.sh/) that we'll be using in our app. The great thing about GraphQL is that it allows us to request just the fields we need from the object, unlike REST which sends all the information available. Karl shows us this in action by walking us through building and running our first GraphQL query.

## Using our container component to map over our Pokemons!

In [the next scrim](https://scrimba.com/p/pdqXpfD/c4MGWJf8?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), we build out our main container so we can loop over our Pokemons.

Karl kicks us of by showing us how to get the data from the Pokemon API:

```js
const { data: { pokemons = [] } = {} } = useQuery(GET_POKEMONS, {
	variables: { first: 9 },
});
```

Next, it's time for an interactive challenge: passing two props, the key and `pokemon`. Head over to [the course](https://scrimba.com/p/pdqXpfD/c4MGWJf8?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) to give the challenge a try for yourself.

## Adding a GraphQL query and creating our Pokemon component!

[![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/09rwvu8lyfclzw1yv46o.png)](https://scrimba.com/p/pdqXpfD/cND38EfL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Click the image to access the course._

In [this scrim](https://scrimba.com/p/pdqXpfD/cND38EfL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), we start by building our graphQL query:

```js
import gql from "graphql-tag";

export const GET_POKEMONS = gql`
	query pokemons($first: Int!) {
		pokemons(first: $first) {
			id
			name
			image
			maxHP
			maxCP
			attacks {
				special {
					name
					damage
				}
			}
		}
	}
`;
```

Next, Karl gives us the bare bones of our Pokemon component:

```js
export function Pokemon({ pokemon }) {
	return <p>{pokemon.name}</p>;
}
```

Our challenge now is to build up the Pokemon component so it displays all the information retrieved from the API. Click through [to the course](https://scrimba.com/p/pdqXpfD/cND38EfL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) now to give it a try.

## Finishing our Pokemon component

[Next up,](https://scrimba.com/p/pdqXpfD/cVnyLyfW?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) Karl talks us through how to map over up to three of a Pokemon's multiple attacks:

```js
{
	pokemon.attacks.special.slice(0, 3).map((attack) => <span></span>);
}
```

We also have a mini-challenge of adding a key within our `pokemon__attacks` div. [Click through](https://scrimba.com/p/pdqXpfD/cVnyLyfW?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) now to give it a try.

## Let's style our application!

[![Styled Pokemon component](https://dev-to-uploads.s3.amazonaws.com/i/3lsg12e2b8dc0uwmjhe7.png)](https://scrimba.com/p/pdqXpfD/c8qgEqUV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Click the image to access the course._

Now that we've created our app, it's time to style it. In [this bumper scrim](https://scrimba.com/p/pdqXpfD/c8qgEqUV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), Karl talks us through styling all the elements of our Pokemon app and gives us a few CSS challenges along the way. Of course, Karl's suggested styles are his personal preference - you could style your app however you like!

```css
.container .pokemon {
	width: 49%;
	background-color: #fff;
	background-clip: border-box;
	border: 1px solid rgba(0, 0, 0, 0.125);
	border-radius: 0.25rem;
	box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
	overflow: hidden;
	margin-bottom: 20px;
}
```

## Responsively styling our application

[![responsively styled app on extra small screen](https://dev-to-uploads.s3.amazonaws.com/i/tbtvim617msylhr92ld3.png)](https://scrimba.com/p/pdqXpfD/c2K7EgUa?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Click the image to access the course._

In [the last scrim](https://scrimba.com/p/pdqXpfD/c2K7EgUa?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) of the course, we find out how to responsively style our app with media queries:

```css
@media (max-width: 800px) {
	.container .pokemon {
		width: 100%;
	}
}

@media (max-width: 400px) {
	.container .pokemon__attacks,
	.container .pokemon__meta {
		flex-wrap: wrap;
	}

	.container .pokemon__meta span,
	.container .pokemon__attacks span,
	.container .pokemon {
		width: 100%;
	}

	.container .pokemon__meta span {
		margin-bottom: 10px;
	}
}
```

Now that's done, our app looks great across all browser sizes.

Well done for completing the course - you've created and styled a fully working React app that hits a GraphQL server, which is a great achievement!

Hopefully, you've learned a lot throughout this course and you'll have a chance to apply your new knowledge to other applications soon. In the meantime, why not head over to [Scrimba](https://scrimba.com?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) to see what other courses are on offer? You could even catch 'em all :)

Whatever you decide to learn next, happy programming!


%[https://www.youtube.com/watch?v=w04_SuqvpzY]


