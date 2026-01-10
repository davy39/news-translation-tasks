---
title: Comment créer un clone de Yelp Full-Stack avec React & GraphQL (Édition Dune)
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
seo_title: Comment créer un clone de Yelp Full-Stack avec React & GraphQL (Édition
  Dune)
seo_desc: 'By Sezgi Ulucam


  I must not fear. Fear is the mind-killer. Fear is the little-death that brings total
  obliteration. I will face my fear. I will permit it to pass over me and through
  me. And when it has gone past I will turn the inner eye to see its p...'
---

Par Sezgi Ulucam

> Je ne connaîtrai pas la peur. La peur tue l'esprit. La peur est la petite mort qui conduit à l'oblitération totale. J'affronterai ma peur. Je lui permettrai de passer sur moi et au travers de moi. Et lorsqu'elle sera passée, je tournerai mon œil intérieur vers son chemin. Là où la peur est passée, il n'y aura plus rien. Seul je resterai.
> \- « Litanie contre la peur », Frank Herbert, Dune

Vous vous demandez peut-être : « Quel est le rapport entre la peur et une application React ? » Tout d'abord, il n'y a rien à craindre dans une application React. En fait, dans cette application particulière, nous avons banni la peur. N'est-ce pas sympathique ?

Maintenant que vous êtes prêt à être sans peur, discutons de notre application. C'est un mini clone de Yelp où, au lieu de donner leur avis sur des restaurants, les utilisateurs évaluent des planètes de la série classique de science-fiction, [Dune](https://en.wikipedia.org/wiki/Dune_(franchise)). (Pourquoi ? Parce qu'un nouveau film Dune va sortir... mais revenons au point principal.)

Pour construire notre application Full-Stack, nous utiliserons des technologies qui nous facilitent la vie.

1. [React](https://reactjs.org/) : Framework front-end intuitif et compositionnel, parce que nos cerveaux aiment composer les choses.
2. [GraphQL](https://graphql.org/) : Vous avez peut-être entendu parler des nombreuses raisons pour lesquelles GraphQL est génial. De loin, la plus importante est la **productivité et le bonheur du développeur**.
3. [Hasura](http://hasura.io/) : Configurez une API GraphQL auto-générée au-dessus d'une base de données Postgres en moins de 30 secondes.
4. [Heroku](https://heroku.com/) : Pour héberger notre base de données.

## Et comment GraphQL m'apporte-t-il du bonheur ?

Je vois que vous êtes sceptique. Mais vous changerez probablement d'avis dès que vous aurez passé un peu de temps avec GraphiQL (le terrain de jeu GraphQL).

Utiliser GraphQL est un jeu d'enfant pour le développeur front-end, comparé aux anciennes méthodes des points de terminaison REST encombrants. GraphQL vous offre un point de terminaison unique qui écoute tous vos problèmes... je veux dire, vos requêtes. C'est un tel auditeur que vous pouvez lui dire exactement ce que vous voulez, et il vous le donnera, rien de moins et rien de plus.

Vous vous sentez enthousiasmé par cette expérience thérapeutique ? Plongeons dans le tutoriel pour que vous puissiez l'essayer dès que possible !

👇 [**Voici le repo**](https://github.com/hasura/yelp-clone-react) si vous souhaitez coder en même temps.

# **P**artie **1 : R**echerche

%[https://www.youtube.com/watch?v=lrYo_n-9LM8]

## **É**tape **1 : D**éploiement sur Heroku

La première étape de tout bon voyage est de s'asseoir avec un thé chaud et de le siroter calmement. Une fois cela fait, nous pouvons déployer sur Heroku depuis le [site Hasura](http://hasura.io/). Cela nous permettra de configurer tout ce dont nous avons besoin : une base de données Postgres, notre moteur GraphQL Hasura et quelques collations pour le voyage.

![black-books.png](https://draftin.com/images/73048?token=L5lFsg6SzmNzsdweEfn9uOLF6qJwkU1loz9LvhE-2PP7sFmiI9nZZ6z87S0pZZZ1xikaO2Z_6GyGPxOzyt170p8)
_Pas du tout une référence à Dune_

## Étape 2 : Créer la table des planètes

Nos utilisateurs veulent donner leur avis sur des planètes. Nous créons donc une table Postgres via la console Hasura pour stocker les données de nos planètes. À noter, la maléfique planète Giedi Prime, qui attire l'attention avec sa cuisine non conventionnelle.

![Table des planètes](https://www.freecodecamp.org/news/content/images/2020/05/p1-s2-1.png)

Pendant ce temps, dans l'onglet GraphiQL : Hasura a auto-généré notre schéma GraphQL ! Amusez-vous avec l'Explorer ici 👇

![Explorer GraphiQL](https://www.freecodecamp.org/news/content/images/2020/05/p1-s2-schema-1.png)

## **É**tape **3 : C**réer l'application React

Nous aurons besoin d'une UI pour notre application, nous créons donc une application React et installons quelques bibliothèques pour les requêtes GraphQL, le routage et les styles. (Assurez-vous d'avoir [Node](https://nodejs.org/) installé au préalable.)

```bash
> npx create-react-app melange
> cd melange
> npm install graphql @apollo/client react-router-dom @emotion/styled @emotion/core
> npm start
```

## **É**tape **4 : C**onfiguration d'Apollo Client

[Apollo Client](https://www.apollographql.com/docs/react/v3.0-beta) nous aidera pour nos requêtes réseau GraphQL et la mise en cache, afin d'éviter tout ce travail fastidieux. Nous effectuons également notre première requête et listons nos planètes ! Notre application commence à prendre forme.

```js
import React from "react";
import { render } from "react-dom";
import { ApolloProvider } from "@apollo/client";
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";
import Planets from "./components/Planets";

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: "[VOTRE POINT DE TERMINAISON HASURA GRAPHQL]",
  }),
});

const App = () => (
  <ApolloProvider client={client}>
    <Planets />
  </ApolloProvider>
);

render(<App />, document.getElementById("root"));
```

Nous testons notre requête GraphQL dans la console Hasura avant de la copier-coller dans notre code.

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

  if (loading) return <p>Chargement ...</p>;
  if (error) return <p>Erreur :(</p>;

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

## **É**tape **5 : S**tyliser la liste

Notre liste de planètes est bien sympathique, mais elle a besoin d'un petit relooking avec [Emotion](https://emotion.sh/) (voir le [repo](https://github.com/hasura/yelp-clone-react) pour les styles complets).

![Liste stylisée des planètes](https://www.freecodecamp.org/news/content/images/2020/05/p1-s5-style-1.png)

## **É**tape **6 : F**ormulaire de recherche et état

Nos utilisateurs veulent rechercher des planètes et les classer par nom. Nous ajoutons donc un formulaire de recherche qui interroge notre point de terminaison avec une chaîne de recherche, et transmettons les résultats à `Planets` pour mettre à jour notre liste de planètes. Nous utilisons également les [React Hooks](https://reactjs.org/docs/hooks-reference.html) pour gérer l'état de notre application.

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

  if (loading) return <p>Chargement ...</p>;
  if (error) return <p>Erreur :(</p>;

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
      <Button onClick={onSearch}>Rechercher</Button>
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
    uri: "[VOTRE POINT DE TERMINAISON HASURA GRAPHQL]",
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

## **É**tape **7 : S**oyez fier

Nous avons déjà implémenté notre liste de planètes et nos fonctionnalités de recherche ! Nous contemplons avec amour notre travail, prenons quelques selfies ensemble, et passons aux avis.

![Liste des planètes avec recherche](https://www.freecodecamp.org/news/content/images/2020/05/pt1-s7-finito.png)

# **P**artie **2 : A**vis en direct

%[https://www.youtube.com/watch?v=3kzXxc1XvRw]

## **É**tape **1 : C**réer la table des avis

Nos utilisateurs visiteront ces planètes et écriront des avis sur leur expérience. Nous créons une table via la console Hasura pour nos données d'avis.

![Table des avis](https://www.freecodecamp.org/news/content/images/2020/05/p2-s1-reviews-table-2.png)

Nous ajoutons une clé étrangère de la colonne `planet_id` vers la colonne `id` de la table `planets`, pour indiquer que les `planet_id` des `reviews` doivent correspondre aux `id` des `planets`.

![Clés étrangères](https://www.freecodecamp.org/news/content/images/2020/05/p2-s1-foreign-key-2.png)

## **É**tape **2 : S**uivre les relations

Chaque planète a plusieurs avis, tandis que chaque avis concerne une seule planète : une relation un-à-plusieurs. Nous créons et suivons cette relation via la console Hasura, afin qu'elle puisse être exposée dans notre schéma GraphQL.

![Suivi des relations](https://www.freecodecamp.org/news/content/images/2020/05/p2-s2-track-2.png)

Maintenant, nous pouvons interroger les avis pour chaque planète dans l'Explorer !

![Requête des avis sur les planètes](https://www.freecodecamp.org/news/content/images/2020/05/p2-s3-explorer-3.png)

## **É**tape **3 : C**onfiguration du routage

Nous voulons pouvoir cliquer sur une planète et voir ses avis sur une page séparée. Nous configurons le routage avec React Router et listons les avis sur la page de la planète.

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
    uri: "[VOTRE POINT DE TERMINAISON HASURA GRAPHQL]",
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

  if (loading) return <p>Chargement ...</p>;
  if (error) return <p>Erreur :(</p>;

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

  if (loading) return <p>Chargement ...</p>;
  if (error) return <p>Erreur :(</p>;

  return <List>{renderPlanets(newPlanets || data.planets)}</List>;
};

export default Planets;
```

## **É**tape **4 : C**onfiguration des abonnements (subscriptions)

Nous installons de nouvelles bibliothèques et configurons Apollo Client pour prendre en charge les abonnements. Ensuite, nous transformons notre requête d'avis en un abonnement afin qu'elle puisse afficher les mises à jour en direct.

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

const GRAPHQL_ENDPOINT = "[VOTRE POINT DE TERMINAISON HASURA GRAPHQL]";

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

  if (loading) return <p>Chargement ...</p>;
  if (error) return <p>Erreur :(</p>;

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

![Page de planète avec avis en direct](https://www.freecodecamp.org/news/content/images/2020/05/p2-s5-finale-2.png)

## **É**tape **5 : F**aites la danse du ver des sables

Nous avons implémenté les planètes avec des avis en direct ! Faites une petite danse pour fêter ça avant de passer aux choses sérieuses.

![Danse du ver](https://www.freecodecamp.org/news/content/images/2020/05/worm-dance.gif)

# **P**artie **3 : L**ogique métier

%[https://www.youtube.com/watch?v=picA-ORNNH8]

## **É**tape **1 : A**jouter le formulaire de saisie

Nous voulons un moyen de soumettre des avis via notre UI. Nous renommons notre formulaire de recherche en un `InputForm` générique et l'ajoutons au-dessus de la liste des avis.

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

  if (loading) return <p>Chargement ...</p>;
  if (error) return <p>Erreur :(</p>;

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
        buttonText="Envoyer"
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

## **É**tape **2 : T**ester la mutation d'avis

Nous utiliserons une mutation pour ajouter de nouveaux avis. Nous testons notre mutation avec GraphiQL dans la console Hasura.

![Mutation d'insertion d'avis dans GraphiQL](https://www.freecodecamp.org/news/content/images/2020/05/p3-s2-test-mutation-2.png)

Et nous la convertissons pour qu'elle accepte des variables afin de pouvoir l'utiliser dans notre code.

![Mutation d'insertion d'avis avec variables](https://www.freecodecamp.org/news/content/images/2020/05/p3-s2-variables-2.png)

## **É**tape **3 : C**réer l'action

Les [Bene Gesserit](https://en.wikipedia.org/wiki/Bene_Gesserit) nous ont demandé de ne pas autoriser (_tousse_ censurer _tousse_) le mot « fear » (peur) dans les avis. Nous créons une action pour la logique métier qui vérifiera la présence de ce mot chaque fois qu'un utilisateur soumet un avis.

![Bouton « Derive action »](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-derive-action-2.png)

À l'intérieur de notre action fraîchement créée, nous allons dans l'onglet « Codegen ».

![Onglet « Codegen »](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-codegen-2.png)

Nous sélectionnons l'option nodejs-express et copions le code boilerplate du gestionnaire (handler) ci-dessous.

![Code boilerplate pour nodejs-express](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-express-2.png)

Nous cliquons sur « Try on Glitch », ce qui nous amène à une application express minimaliste, où nous pouvons coller notre code de gestionnaire.

![Collage de notre code de gestionnaire dans Glitch](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-glitch-2.png)

De retour dans notre action, nous définissons l'URL de notre gestionnaire sur celle de notre application Glitch, avec la route correcte provenant de notre code de gestionnaire.

![URL du gestionnaire](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-handler-url-2.png)

Nous pouvons maintenant tester notre action dans la console. Elle s'exécute comme une mutation classique, car nous n'avons pas encore de logique métier vérifiant le mot « fear ».

![Test de notre action dans la console](https://www.freecodecamp.org/news/content/images/2020/05/p3-s3-test-action-2.png)

## **É**tape **4 : A**jouter la logique métier

Dans notre gestionnaire, nous ajoutons une logique métier qui vérifie la présence de « fear » dans le corps de l'avis. S'il est sans peur (fearless), nous exécutons la mutation comme d'habitude. Sinon, nous renvoyons une erreur inquiétante.

![Logique métier vérifiant « fear »](https://www.freecodecamp.org/news/content/images/2020/05/p3-s4-biz-logic-3.png)

Si nous exécutons l'action avec « fear » maintenant, nous obtenons l'erreur dans la réponse :

![Test de notre logique métier dans la console](https://www.freecodecamp.org/news/content/images/2020/05/p3-s4-error-2.png)

## **É**tape **5 : O**rdonner les avis

L'ordre de nos avis est actuellement sens dessus dessous. Nous ajoutons une colonne `created_at` à la table `reviews` afin de pouvoir les classer du plus récent au plus ancien.

```js
reviews(order_by: { created_at: desc })
```

## **É**tape **6 : A**jouter la mutation d'avis

Enfin, nous mettons à jour la syntaxe de notre action avec des variables, et nous la copions-collons dans notre code en tant que mutation. Nous mettons à jour notre code pour exécuter cette mutation lorsqu'un utilisateur soumet un nouvel avis, afin que notre logique métier puisse vérifier sa conformité (_ahem_ obéissance _ahem_) avant de mettre à jour notre base de données.

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

  if (loading) return <p>Chargement ...</p>;
  if (error) return <p>Erreur :(</p>;

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
        buttonText="Envoyer"
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

Si nous soumettons un nouvel avis incluant « fear » maintenant, nous obtenons notre erreur inquiétante, que nous affichons dans le champ de saisie.

![Test de notre action via l'UI](https://www.freecodecamp.org/news/content/images/2020/05/p3-s6-test-final-ui-2.png)

## Étape 7 : On l'a fait ! 🎉

Félicitations pour avoir construit une application React & GraphQL Full-Stack !

![High five](https://www.freecodecamp.org/news/content/images/2020/05/high-five.gif)

# Que réserve l'avenir ?

![spice_must_flow.jpg](https://draftin.com/images/73049?token=kxAhFBHMt0pOLjXmaJQRIXSqFGtjWxb-WBuwPn2cjwPgL0mQP8TxoV4mqiQwXBotJ4cdCCRbehNabJMt2l9pvLA)

Si seulement nous avions un peu de mélange d'épice, nous le saurions. Mais nous avons construit tellement de fonctionnalités en si peu de temps ! Nous avons couvert les requêtes GraphQL, les mutations, les abonnements, le routage, la recherche et même la logique métier personnalisée avec les actions Hasura ! J'espère que vous vous êtes amusé à coder avec moi.

Quelles autres fonctionnalités aimeriez-vous voir dans cette application ? Contactez-moi sur Twitter, et je ferai d'autres tutoriels ! Si vous êtes inspiré pour ajouter des fonctionnalités vous-même, n'hésitez pas à [les partager](https://twitter.com/sez) – j'adorerais en entendre parler :)