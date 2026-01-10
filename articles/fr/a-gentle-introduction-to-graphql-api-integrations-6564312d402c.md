---
title: Une introduction en douceur aux intégrations d'API GraphQL
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
seo_title: Une introduction en douceur aux intégrations d'API GraphQL
seo_desc: 'By Hugo Di Francesco

  GraphQL is a great alternative to REST (or other HTTP API designs). This is a quick
  introduction to the core concepts around consuming a GraphQL API.

  To see some examples consuming a GraphQL API:


  In Python, see Python GraphQL cl...'
---

Par Hugo Di Francesco

GraphQL est une excellente alternative à REST (ou à d'autres conceptions d'API HTTP). Voici une brève introduction aux concepts clés autour de la _consommation_ d'une API GraphQL.

Pour voir des exemples de consommation d'une API GraphQL :

* En Python, voir [Exemple de requêtes client Python GraphQL utilisant gql](https://codewithhugo.com/python-graphql-client-requests-example-using-gql/)
* En JavaScript [navigateur et Node, voir la newsletter Code with Hugo de la semaine dernière](https://codewithhugo.com/javascript-graphql-client-requests-in-node-and-the-browser-using-graphql.js/)

### Qu'est-ce que GraphQL et quels problèmes résout-il ?

GraphQL est [un langage de requête pour votre API](https://graphql.org/).

En termes simples, il permet au client de définir les données (imbriquées) dont il a besoin.

Si nous le comparons aux approches [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) :

* L'approche REST pure consiste à retourner des IDs (ou des liens de ressources) pour toute association (ou ressource imbriquée).
* L'approche moins pure consiste à développer toutes les données imbriquées.

La première situation conduit à devoir effectuer de nombreux appels pour récupérer toutes les données. La seconde conduit à des charges utiles énormes et à des temps de chargement lents.

Avec GraphQL, le client indique dans la requête ce qu'il souhaite développer, renommer ou autre chose dans la réponse.

Cela a quelques effets secondaires intéressants, par exemple, moins besoin de versionner votre API puisque le client définit ce qu'il veut et GraphQL a un moyen de déprécier les champs.

### Schéma

[GraphiQL](https://github.com/graphql/graphiql), Un IDE dans le navigateur pour explorer GraphQL. est disponible en naviguant vers le point de terminaison dans votre navigateur. Il est possible de générer le schéma en utilisant le CLI GraphQL (nécessite Node + npm 5+) :

```
npx graphql-cli get-schema --endpoint $BASE_URL/api/graphql --no-all -o schema.graphql
```

### Requêtes

#### Concepts de requête GraphQL

#### Champs

Ce que nous aimerions voir retourné dans la requête, voir [la documentation GraphQL pour les champs](https://graphql.org/learn/queries/#fields). La requête GraphQL qui retourne les champs `name`, `fleeRate`, `maxCP`, `maxHP`, est la suivante :

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

Comment nous allons filtrer les données de la requête, voir [la documentation GraphQL pour les arguments](https://graphql.org/learn/queries/#arguments). Pour obtenir les noms des 10 premiers pokémons, nous utilisons `pokemons (first: 10) { FIELDS }` pour voir le résultat [ici](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons%20(first%3A%2010)%20%7B%0A%20%20%20%20name%0A%20%20%20%20fleeRate%0A%20%20%20%20maxCP%0A%20%20%20%20maxHP%0A%20%20%7D%0A%7D%0A) :

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

#### Alias

Les alias nous donnent la possibilité de renommer les champs. (Voir [la documentation GraphQL pour les alias](https://graphql.org/learn/queries/#aliases)). Nous allons en fait l'utiliser pour mapper les champs dans la requête, par exemple, de camelCase à snake_case :

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

L'exécution de cette requête ([ici](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20evolution_requirements%3A%20evolutionRequirements%20%7B%0A%20%20%20%20%20%20amount%0A%20%20%20%20%20%20name%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A)) nous donne ce qui suit, où `evolutionRequirements` est ce que nous avons aliasé :

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

La définition des champs à développer sur un type. C'est un moyen de garder les requêtes DRY et, en général, de séparer les définitions de champs qui sont répétées, réutilisées ou profondément imbriquées, voir [la documentation GraphQL pour les fragments](https://graphql.org/learn/queries/#fragments). Cela signifie que, au lieu de faire ([voir](https://graphql-pokemon.now.sh/?query=%0A%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20id%0A%20%20%20%20number%0A%20%20%20%20weight%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%20%20height%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D) [la requête en action ici](https://graphql-pokemon.now.sh/?query=%0A%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20weight%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%20%20height%20%7B%0A%20%20%20%20%20%20minimum%0A%20%20%20%20%20%20maximum%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)) :

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

Nous pouvons par exemple exécuter ceci ([requête](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20id%0A%20%20%20%20number%0A%20%20%20%20weight%20%7B...FullPokemonDimensions%7D%0A%20%20%20%20height%20%7B...FullPokemonDimensions%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPokemonDimensions%20on%20PokemonDimension%20%7B%0A%20%20minimum%0A%20%20maximum%0A%7D) [ici](https://graphql-pokemon.now.sh/?query=%0A%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20weight%20%7B...FullPokemonDimensions%7D%0A%20%20%20%20height%20%7B...FullPokemonDimensions%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPokemonDimensions%20on%20PokemonDimension%20%7B%0A%20%20minimum%0A%20%20maximum%0A%7D)) :

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

La sortie est équivalente :

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

### Exécuter une requête GraphQL

Une requête GraphQL peut être exécutée via POST ou GET, elle se compose de :

#### POST (recommandé)

* En-têtes requis : `Content-Type: application/json`
* Paramètre JSON requis dans le corps : `query: { # insérez votre requête }`

**Requête HTTP brute**

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

* Paramètre de requête requis : `query`

**Requête HTTP brute**

```
GET /?query={%20pokemons(first:%2010)%20{%20name%20}%20} HTTP/1.1
Host: graphql-pokemon.now.sh
```

**cURL**

```
curl -X GET 'https://graphql-pokemon.now.sh/?query={%20pokemons%28first:%2010%29%20{%20name%20}%20}'
```

### Requêtes de niveau supérieur

Il existe 2 types de requêtes sur l'[API GraphQL Pokemon](https://graphql-pokemon.now.sh/) pour le moment :

* Les X premiers pokémons : obtenir tous les éléments (avec les champs définis dans la requête)
* Un seul Pokémon par nom : obtenir un seul élément par son slug (avec les champs définis dans la requête)
* Un seul Pokémon par ID : obtenir un seul élément par son slug (avec les champs définis dans la requête)

#### Les X premiers Pokémon

Requêtes de la forme ([voir en action dans GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons(first%3A%205)%20%7B%0A%20%20%20%20name%0A%20%20%7D%0A%7D)) :

```graphql
{
  pokemons(first: 5) {
    name
    # autres champs
  }
}
```

#### Un seul Pokémon par nom

Requêtes de la forme ([voir en action dans GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20name%0A%20%20%20%20classification%0A%20%20%7D%0A%7D)) :

```graphql
{
  pokemon(name: "Pikachu") {
    name
    classification
    # autres champs
  }
}
```

> _Notez les guillemets doubles (`""`) autour de la valeur de l'argument_

#### Un seul Pokémon par ID

Requêtes de la forme ([voir en action dans GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(id%3A%20%22UG9rZW1vbjowMjU%3D%22)%20%7B%0A%20%20%20%20name%0A%20%20%20%20classification%0A%20%20%7D%0A%7D)) :

```graphql
{
  pokemon(id: "UG9rZW1vbjowMjU=") {
    name
    classification
    # autres champs
  }
}
```

> _Notez les guillemets doubles (`""`) autour de la valeur de l'argument_

### Exemples de requêtes

#### Obtenir certains Pokémon pour créer une classification des forces/faiblesses/résistances

Requête ([voir dans GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemons(first%3A%20100)%20%7B%0A%20%20%20%20name%0A%20%20%20%20image%0A%20%20%20%20maxHP%0A%20%20%20%20types%0A%20%20%20%20weaknesses%0A%20%20%20%20resistant%0A%20%20%7D%0A%7D)) :

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

#### Obtenir des Pokémon et des évolutions développées pour les statistiques physiques et les attaques

Requête ([voir dans GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20...PokemonWithAttack%0A%20%20%20%20...FullPhysicalStats%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20...FullPhysicalStats%0A%20%20%20%20%20%20...PokemonWithAttack%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20PokemonWithAttack%20on%20Pokemon%20%7B%0A%20%20name%0A%20%20attacks%20%7B%0A%20%20%20%20fast%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20type%0A%20%20%20%20%20%20damage%0A%20%20%20%20%7D%0A%20%20%20%20special%20%7B%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20type%0A%20%20%20%20%20%20damage%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPhysicalStats%20on%20Pokemon%20%7B%0A%20%20height%20%7B%20...FullDimension%20%7D%0A%20%20weight%20%7B%20...FullDimension%20%7D%0A%7D%0A%0Afragment%20FullDimension%20on%20PokemonDimension%20%7B%0A%20%20minimum%0A%20%20maximum%0A%7D)) :

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

#### Obtenir des Pokémon sélectionnés en tant que champs nommés avec leurs noms d'évolution

Requête ([voir dans GraphiQL](https://graphql-pokemon.now.sh/?query=%7B%0A%20%20pikachu%3A%20pokemon(name%3A%20%22Pikachu%22)%20%7B%0A%20%20%20%20...FullPokemon%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20...FullPokemon%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20bulbasaur%3Apokemon(name%3A%20%22Bulbasaur%22)%20%7B%0A%20%20%20%20...FullPokemon%0A%20%20%20%20evolutions%20%7B%0A%20%20%20%20%20%20...FullPokemon%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A%0Afragment%20FullPokemon%20on%20Pokemon%20%7B%0A%20%20name%0A%7D%0A)).

Nous pouvons renommer les requêtes de niveau supérieur en utilisant des alias. C'est utile si nous voulons faire ce qui suit :

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

Si vous souhaitez apprendre à intégrer une API GraphQL :

- En Python, voir [Exemple de requêtes client Python GraphQL utilisant gql](https://codewithhugo.com/python-graphql-client-requests-example-using-gql/)
- En JavaScript [navigateur et Node, voir la newsletter Code with Hugo de la semaine dernière](https://codewithhugo.com/javascript-graphql-client-requests-in-node-and-the-browser-using-graphql.js/)

Lisez plus de mes articles sur mon site web, [Code With Hugo](https://codewithhugo.com).