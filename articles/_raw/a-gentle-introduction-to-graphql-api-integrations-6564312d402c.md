---
title: A gentle introduction to GraphQL API integrations
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-gentle-introduction-to-graphql-api-integrations-6564312d402c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A6Cr5WakyAJjuES53YXBow.jpeg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Hugo Di Francesco

  GraphQL is a great alternative to REST (or other HTTP API designs). This is a quick
  introduction to the core concepts around consuming a GraphQL API.

  To see some examples consuming a GraphQL API:


  In Python, see Python GraphQL cl...'
---

By Hugo Di Francesco

GraphQL is a great alternative to REST (or other HTTP API designs). This is a quick introduction to the core concepts around _consuming_ a GraphQL API.

To see some examples consuming a GraphQL API:

* In Python, see [Python GraphQL client requests example using gql](https://codewithhugo.com/python-graphql-client-requests-example-using-gql/)
* In JavaScript [browser and Node, see last week’s Code with Hugo newsletter](https://codewithhugo.com/javascript-graphql-client-requests-in-node-and-the-browser-using-graphql.js/)

### What is GraphQL and what problems does it solve?

GraphQL is [“a query language for your API”](https://graphql.org/).

In plain English, it makes the client define what (nested) data it needs.

If we compare it to [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) approaches:

* the “pure” REST approach is to return IDs (or resource links) for any associations (or nested resources).
* The less pure approach is to expand all the nested stuff.

The first situation leads to having to make lots of calls to fetch all the data. The second leads to huge payloads and slow load times.

In GraphQL, the client states in the request what it wants expanded, renamed or whatever else in the response.

It has some nice side-effects, for example less need to version your API since the client defines what it wants and GraphQL has a way to deprecate fields.

### Schema

[GraphiQL](https://github.com/graphql/graphiql), “An in-browser IDE for exploring GraphQL.” is available by navigating to the endpoint in your browser. It’s possible to generate the schema using the GraphQL CLI (requires Node + npm 5+):

```
npx graphql-cli get-schema --endpoint $BASE_URL/api/graphql --no-all -o schema.graphql
```

### Queries

#### GraphQL query concepts

#### Fields

What we would like returned in the query, see [the GraphQL documentation for “fields”](https://graphql.org/learn/queries/#fields/). The GraphQL query for that returns the fields `name`, `fleeRate`, `maxCP`, `maxHP`, is the following:

```graphql
{
  pokemon(name: "Pikachu") {
    name
    fleeRate
    maxCP
    maxHP
  }
}
```

#### Arguments

How we are going to filter the query data down, see [the GraphQL documentation for “arguments”](https://graphql.org/learn/queries/#arguments). To get the names of the first 10 pokemon we use `pokemons (first: 10) { FIELDS }`to see the output [here](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons%20(first%3A%2010)%20%7B%0A%20%20%20%20name%0A%20%20%20%20fleeRate%0A%20%20%20%20maxCP%0A%20%20%20%20maxHP%0A%20%20%7D%0A%7D%0A):

```graphql
{
  pokemons (first: 10) {
    name
    fleeRate
    maxCP
    maxHP
  }
}
```

#### Aliases

Aliases give us the ability to rename fields. (See [the GraphQL documentation for “aliases”](https://graphql.org/learn/queries/#aliases)). We’re actually going to use it to map fields in the query eg. from camel to snake case:

```graphql
{
  pokemon(name: "Pikachu") {
    evolution_requirements: evolutionRequirements {
      amount
      name
    }
  }
}
```

Running this query ([here](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20evolution_requirements%3A%20evolutionRequirements%20%7B%0A%20%20%20%20%20%20amount%0A%20%20%20%20%20%20name%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A)) gives us the following, where the `evolutionRequirements` is what we’ve aliased it to.

```graphql
{
  "data": {
    "pokemon": {
      "evolution_requirements": {
        "amount": 50,
        "name": "Pikachu candies"
      }
    }
  }
}
```

#### Fragments

The definition of fields to be expanded on a type. It’s a way to keep the queries DRY and in general split out the field definitions that are repeated, re-used or deeply nested, see [the GraphQL documentation for fragments](https://graphql.org/learn/queries/#fragments). It’s going to mean that instead of doing ([see](https://graphql-pokemon.now.sh/?query=%0A%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20id%0A%20%20%20%20number%0A%20%20%20%20weight%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%20%20height%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D) [the query in action here](https://graphql-pokemon.now.sh/?query=%0A%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20weight%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%20%20height%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)):

```graphql
{
  pokemon(name: "Pikachu") {
    weight {
      minimum
      maximum
    }
    height {
      minimum
      maximum
    }
  }
}
```

We can for example run this ([query](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20id%0A%20%20%20%20number%0A%20%20%20%20weight%20%7B...FullPokemonDimensions%7D%0A%20%20%20%20height%20%7B...FullPokemonDimensions%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPokemonDimensions%20on%20PokemonDimension%20%7B%0A%20%20minimum%0A%20%20maximum%0A%7D) [here](https://graphql-pokemon.now.sh/?query=%0A%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20weight%20%7B...FullPokemonDimensions%7D%0A%20%20%20%20height%20%7B...FullPokemonDimensions%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPokemonDimensions%20on%20PokemonDimension%20%7B%0A%20%20minimum%0A%20%20maximum%0A%7D)):

```graphql
{
  pokemon(name: "Pikachu") {
    weight {...FullPokemonDimensions}
    height {...FullPokemonDimensions}
  }
}
fragment FullPokemonDimensions on PokemonDimension {
  minimum
  maximum
}
```

The output is equivalent:

```graphql
{
  "data": {
    "pokemon": {
      "weight": {
        "minimum": "5.25kg",
        "maximum": "6.75kg"
      },
      "height": {
        "minimum": "0.35m",
        "maximum": "0.45m"
      }
    }
  }
}
```

### Running a GraphQL query

A GraphQL query can be run over POST or GET, it consists of:

#### POST (recommended)

* Required headers: `Content-Type: application/json`
* Required JSON body parameter: `query: { # insert your query }`

**Raw HTTP request**

```
POST / HTTP/1.1
Host: graphql-pokemon.now.sh
Content-Type: application/json
{
        "query": "{ pokemons(first: 10) { name } }"
}
```

**cURL**

```
curl -X POST \
  https://graphql-pokemon.now.sh/ \
  -H 'Content-Type: application/json' \
  -d '{
        "query": "{ pokemons(first: 10) { name } }"
    }'
```

#### GET

* Required query param: `query`

**raw HTTP request**

```
GET /?query={%20pokemons(first:%2010)%20{%20name%20}%20} HTTP/1.1
Host: graphql-pokemon.now.sh
```

**cURL**

```
curl -X GET 'https://graphql-pokemon.now.sh/?query={%20pokemons%28first:%2010%29%20{%20name%20}%20}'
```

### Top-level queries

There are 2 types of queries on the [GraphQL Pokemon API](https://graphql-pokemon.now.sh/) at the moment:

* First X pokemon: get all items (with whatever fields are defined in the query)
* Single Pokemon by name: get a single item by its slug (with whatever fields are defined in the query)
* Single Pokemon by id: get a single item by its slug (with whatever fields are defined in the query)

#### First X Pokemon

Queries of the form ([see it in action in GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons(first%3A%205)%20%7B%0A%20%20%20%20name%0A%20%20%7D%0A%7D)):

```graphql
{
  pokemons(first: 5) {
    name
    # other fields
  }
}
```

#### Single Pokemon by name

Queries of the form ([see it in action in GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20name%0A%20%20%20%20classification%0A%20%20%7D%0A%7D)):

```graphql
{
  pokemon(name: "Pikachu") {
    name
    classification
    # other fields
  }
}
```

> _Note the double quotes (`""`) around the argument value_

#### Single Pokemon by id

Queries of the form ([see it in action in GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(id%3A%20%22UG9rZW1vbjowMjU%3D%22)%20%7B%0A%20%20%20%20name%0A%20%20%20%20classification%0A%20%20%7D%0A%7D)):

```graphql
{
  pokemon(id: "UG9rZW1vbjowMjU=") {
    name
    classification
    # other fields
  }
}
```

> _Note the double quotes (`""`) around the argument value_

### Sample queries

#### Get some Pokemon to create strengths/weakness/resistance classification

Query ([see it in GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons(first%3A%20100)%20%7B%0A%20%20%20%20name%0A%20%20%20%20image%0A%20%20%20%20maxHP%0A%20%20%20%20types%0A%20%20%20%20weaknesses%0A%20%20%20%20resistant%0A%20%20%7D%0A%7D)):

```graphql
{
  pokemons(first: 100) {
    name
    image
    maxHP
    types
    weaknesses
    resistant
  }
}
```

#### Get Pokemon and evolutions expanded for physical stats and attacks

Query ([see it in GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20...PokemonWithAttack%0A%20%20%20%20...FullPhysicalStats%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20...FullPhysicalStats%0A%20%20%20%20%20%20...PokemonWithAttack%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20PokemonWithAttack%20on%20Pokemon%20%7B%0A%20%20name%0A%20%20attacks%20%7B%0A%20%20%20%20fast%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20type%0A%20%20%20%20%20%20damage%0A%20%20%20%20%7D%0A%20%20%20%20special%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20type%0A%20%20%20%20%20%20damage%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPhysicalStats%20on%20Pokemon%20%7B%0A%20%20height%20%7B%20...FullDimension%20%7D%0A%20%20weight%20%7B%20...FullDimension%20%7D%0A%7D%0A%0Afragment%20FullDimension%20on%20PokemonDimension%20%7B%0A%20%20minimum%0A%20%20maximum%0A%7D)):

```graphql
{
  pokemon(name: "Pikachu") {
    ...PokemonWithAttack
    ...FullPhysicalStats
    evolutions {
      ...FullPhysicalStats
      ...PokemonWithAttack
    }
  }
}
fragment PokemonWithAttack on Pokemon {
  name
  attacks {
    fast {
      name
      type
      damage
    }
    special {
      name
      type
      damage
    }
  }
}
fragment FullPhysicalStats on Pokemon {
  height { ...FullDimension }
  weight { ...FullDimension }
}
fragment FullDimension on PokemonDimension {
  minimum
  maximum
}
```

#### Get selected Pokemon as named fields with their evolution names

Query ([see it in GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pikachu%3A%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20...FullPokemon%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20...FullPokemon%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20bulbasaur%3Apokemon(name%3A%20%22Bulbasaur%22)%20%7B%0A%20%20%20%20...FullPokemon%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20...FullPokemon%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPokemon%20on%20Pokemon%20%7B%0A%20%20name%0A%7D%0A)).

We can rename top-level queries using aliases. That’s helpful if we want to do the following:

```graphql
{
  pikachu: pokemon(name: "Pikachu") {
    ...FullPokemon
    evolutions {
      ...FullPokemon
    }
  }
  bulbasaur:pokemon(name: "Bulbasaur") {
    ...FullPokemon
    evolutions {
      ...FullPokemon
    }
  }
}
fragment FullPokemon on Pokemon {
  name
}
```

If you want to learn how to integrate with a GraphQL API:

- In Python, see [Python GraphQL client requests example using gql](https://codewithhugo.com/python-graphql-client-requests-example-using-gql/)  
- In JavaScript [browser and Node, see last week’s Code with Hugo newsletter](https://codewithhugo.com/javascript-graphql-client-requests-in-node-and-the-browser-using-graphql.js/)

Read more of my articles on my website, [Code With Hugo](https://codewithhugo.com).

