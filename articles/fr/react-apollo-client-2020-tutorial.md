---
title: Le didacticiel React + Apollo pour 2020 (exemples concrets)
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2020-07-04T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/react-apollo-client-2020-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/React
seo_title: Le didacticiel React + Apollo pour 2020 (exemples concrets)
---

Apollo-2020-Cheatsheet.png
étiquettes:
- name: '2020'
  slug: '2020'
- name: Apollo GraphQL
  slug: apollo
- name: client apollo
  slug: apollo-client
- name: aide-mémoire
  slug: aide-mémoire
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Didacticiel
  slug: didacticiel
seo_title: null
seo_desc: 'Si vous souhaitez créer des applications avec React et GraphQL, Apollo est la bibliothèque
  que vous devriez utiliser.

  J'ai rassemblé une aide-mémoire complète qui passe en revue tous les concepts de base
  de la bibliothèque Apollo, vous montrant comment l'utiliser avec React de bout en bout.'
---

Si vous souhaitez créer des applications avec React et GraphQL, Apollo est la bibliothèque que vous devriez utiliser.

J'ai rassemblé une aide-mémoire complète qui passe en revue tous les concepts de base de la bibliothèque Apollo, vous montrant comment l'utiliser avec React de bout en bout.

### Vous voulez votre propre copie ?

Vous pouvez obtenir l'aide-mémoire PDF **[ici](https://reedbarger.com/resources/react-apollo-2020/)** (cela prend 5 secondes).

Voici quelques gains rapides en obtenant la version téléchargeable :

- ✅ Référence rapide à consulter comme et quand vous le souhaitez
- ✅ Des tonnes d'extraits de code utiles basés sur des projets réels
- ✅ Lisez ce guide hors ligne, où vous voulez. Dans le train, à votre bureau, en faisant la queue — n'importe où.

### Préférez-vous les leçons vidéo ?

Une grande partie de cette aide-mémoire est basée sur l'application construite dans le cours intensif React + GraphQL 2020.

Si vous voulez des leçons vidéo plus pratiques, ainsi que voir comment créer des applications avec React, GraphQL et Apollo, vous pouvez regarder le cours [ici](https://bit.ly/2020-react-graphql).

> Note : Cette aide-mémoire suppose une familiarité avec React et GraphQL. Si vous avez besoin d'un rappel rapide sur GraphQL et comment l'écrire, une excellente ressource est le [site officiel de GraphQL](https://graphql.org/learn/).

## Table des matières

### Pour commencer

- [Qu'est-ce qu'Apollo et pourquoi en avons-nous besoin ?](#heading-questce-quapollo-et-pourquoi-en-avons-nous-besoin)
- [Configuration du client Apollo](#heading-configuration-du-client-apollo)
- [Création d'un nouveau client Apollo](#heading-creation-dun-nouveau-client-apollo-configuration-de-base)
- [Fournir le client aux composants React](#heading-fournir-le-client-aux-composants-react)
- [Utilisation directe du client](#heading-utilisation-directe-du-client)
- [Écriture de GraphQL dans les fichiers .js avec gql](#heading-ecriture-doperations-graphql-dans-les-fichiers-js-gql)

### Hooks principaux d'Apollo React

- [Hook useQuery](#heading-hook-usequery)
- [Hook useLazyQuery](#heading-hook-uselazyquery)
- [Hook useMutation](#heading-hook-usemutation)
- [Hook useSubscription](#heading-hook-usesubscription)

### Recettes essentielles

- [Définition manuelle de la politique de récupération](#heading-definition-manuelle-de-la-politique-de-recuperation)
- [Mise à jour du cache après une mutation](#heading-mise-a-jour-du-cache-apres-une-mutation)
- [Nouvelle exécution des requêtes avec useQuery](#heading-nouvelle-execution-des-requetes-avec-usequery)
- [Nouvelle exécution des requêtes avec useMutation](#heading-nouvelle-execution-des-requetes-avec-usemutation)
- [Accès au client avec useApolloClient](#heading-utilisation-du-client-avec-useapolloclient)

### Qu'est-ce qu'Apollo et pourquoi en avons-nous besoin ?

Apollo est une bibliothèque qui réunit deux technologies incroyablement utiles pour créer des applications web et mobiles : React et GraphQL.

React a été conçu pour créer de grandes expériences utilisateur avec JavaScript. GraphQL est un nouveau langage très simple et déclaratif pour récupérer et modifier des données plus facilement et efficacement, qu'elles proviennent d'une base de données ou même de fichiers statiques.

Apollo est le lien qui unit ces deux outils. De plus, il facilite grandement le travail avec React et GraphQL en nous offrant de nombreux hooks React personnalisés et des fonctionnalités qui nous permettent à la fois d'écrire des opérations GraphQL et de les exécuter avec du code JavaScript.

Nous aborderons ces fonctionnalités en profondeur tout au long de ce guide.

### Configuration de base du client Apollo

Si vous commencez un projet avec un modèle React comme Create React App, vous devrez installer les dépendances de base suivantes pour démarrer avec Apollo Client :

```bash
// avec npm :
npm i @apollo/react-hooks apollo-boost graphql

// avec yarn :
yarn add @apollo/react-hooks apollo-boost graphql
```

`@apollo/react-hooks` nous offre des hooks React qui améliorent l'exécution de nos opérations et le travail avec le client Apollo.

`apollo-boost` nous aide à configurer le client ainsi qu'à analyser nos opérations GraphQL.

`graphql` prend également en charge l'analyse des opérations GraphQL (avec gql).

### Configuration du client Apollo + abonnements

Pour utiliser tous les types d'opérations GraphQL (requêtes, mutations et abonnements), nous devons installer des dépendances plus spécifiques par rapport à `apollo-boost` :

```bash
// avec npm :
npm i @apollo/react-hooks apollo-client graphql graphql-tag apollo-cache-inmemory apollo-link-ws

// avec yarn :
yarn add @apollo/react-hooks apollo-client graphql graphql-tag apollo-cache-inmemory apollo-link-ws
```

`apollo-client` nous donne le client directement, au lieu de `apollo-boost`.

`graphql-tag` est intégré dans `apollo-boost`, mais n'est pas inclus dans `apollo-client`.

`apollo-cache-inmemory` est nécessaire pour configurer notre propre cache (ce que `apollo-boost` fait automatiquement, en comparaison).

`apollo-link-ws` est nécessaire pour communiquer via websockets, ce que les abonnements nécessitent.

### Création d'un nouveau client Apollo (configuration de base)

La configuration la plus simple pour créer un client Apollo consiste à instancier un nouveau client et à fournir uniquement la propriété `uri`, qui sera votre endpoint GraphQL :

```jsx
import ApolloClient from "apollo-boost";

const client = new ApolloClient({
  uri: "https://votre-endpoint-graphql.com/api/graphql",
});
```

`apollo-boost` a été développé afin de rendre les choses comme la création d'un client Apollo aussi faciles que possible. Ce qu'il manque pour le moment, cependant, c'est le support des abonnements GraphQL via une connexion websocket.

Par défaut, il exécute les opérations via une connexion http (comme vous pouvez le voir à travers notre uri fourni ci-dessus).

En bref, utilisez `apollo-boost` pour créer votre client si vous avez seulement besoin d'exécuter des requêtes et des mutations dans votre application.

Il configure un cache en mémoire par défaut, ce qui est utile pour stocker nos données d'application localement. Nous pouvons lire et écrire dans notre cache pour éviter d'avoir à exécuter nos requêtes après la mise à jour de nos données. Nous aborderons comment faire cela un peu plus tard.

### Création d'un nouveau client Apollo (+ configuration des abonnements)

Les abonnements sont utiles pour afficher plus facilement le résultat des changements de données (via des mutations) dans notre application.

En général, nous utilisons les abonnements comme une sorte de requête améliorée. Les abonnements utilisent une connexion websocket pour "s'abonner" aux mises à jour et aux données, permettant aux nouvelles données ou aux données mises à jour d'être immédiatement affichées à nos utilisateurs sans avoir à réexécuter des requêtes ou à mettre à jour le cache.

```jsx
import ApolloClient from "apollo-client";
import { WebSocketLink } from "apollo-link-ws";
import { InMemoryCache } from "apollo-cache-inmemory";

const client = new ApolloClient({
  link: new WebSocketLink({
    uri: "wss://votre-endpoint-graphql.com/v1/graphql",
    options: {
      reconnect: true,
      connectionParams: {
        headers: {
          Authorization: "Bearer votrejetonauth",
        },
      },
    },
  }),
  cache: new InMemoryCache(),
});
```

### Fournir le client aux composants React

Après avoir créé un nouveau client, le transmettre à tous les composants est essentiel afin de pouvoir l'utiliser dans nos composants pour effectuer toutes les opérations GraphQL disponibles.

Le client est fourni à l'ensemble de l'arborescence des composants en utilisant le contexte React, mais au lieu de créer notre propre contexte, nous importons un fournisseur de contexte spécial de `@apollo/react-hooks` appelé `ApolloProvider`. Nous pouvons voir comment il diffère du contexte React régulier en raison de sa propriété spéciale, `client`, spécialement conçue pour accepter le client créé.

Notez que toute cette configuration doit être effectuée dans votre fichier index.js ou App.js (là où vos routes sont déclarées) afin que le fournisseur puisse envelopper tous vos composants.

```jsx
import { ApolloProvider } from "@apollo/react-hooks";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={App} />
          <Route exact path="/new" component={NewPost} />
          <Route exact path="/edit/:id" component={EditPost} />
        </Switch>
      </BrowserRouter>
    </ApolloProvider>
  </React.StrictMode>,
  rootElement
);
```

### Utilisation directe du client

Le client Apollo est la partie la plus importante de la bibliothèque en raison du fait qu'il est responsable de l'exécution de toutes les opérations GraphQL que nous voulons effectuer avec React.

Nous pouvons utiliser le client créé directement pour effectuer toute opération que nous souhaitons. Il dispose de méthodes correspondant aux requêtes (`client.query()`), aux mutations (`client.mutate()`) et aux abonnements (`client.subscribe()`).

Chaque méthode accepte un objet et ses propres propriétés correspondantes :

```jsx
// exécution de requêtes
client
  .query({
    query: GET_POSTS,
    variables: { limit: 5 },
  })
  .then((response) => console.log(response.data))
  .catch((err) => console.error(err));

// exécution de mutations
client
  .mutate({
    mutation: CREATE_POST,
    variables: { title: "Hello", body: "World" },
  })
  .then((response) => console.log(response.data))
  .catch((err) => console.error(err));

// exécution d'abonnements
client
  .subscribe({
    subscription: GET_POST,
    variables: { id: "8883346c-6dc3-4753-95da-0cc0df750721" },
  })
  .then((response) => console.log(response.data))
  .catch((err) => console.error(err));
```

L'utilisation directe du client peut être un peu délicate, cependant, car en faisant une requête, il retourne une promesse. Pour résoudre chaque promesse, nous avons besoin soit de rappels `.then()` et `.catch()` comme ci-dessus, soit d'attendre chaque promesse au sein d'une fonction déclarée avec le mot-clé `async`.

### Écriture d'opérations GraphQL dans les fichiers .js (gql)

Remarquez ci-dessus que je n'ai pas spécifié le contenu des variables `GET_POSTS`, `CREATE_POST` et `GET_POST`.

Ce sont les opérations écrites dans la syntaxe GraphQL qui spécifient comment effectuer la requête, la mutation et l'abonnement respectivement. Ce sont ce que nous écririons dans n'importe quelle console GraphiQL pour obtenir et modifier des données.

Le problème ici, cependant, est que nous ne pouvons pas écrire et exécuter des instructions GraphQL dans des fichiers JavaScript (.js), comme notre code React doit vivre.

Pour analyser les opérations GraphQL, nous utilisons une fonction spéciale appelée un littéral de modèle étiqueté pour nous permettre de les exprimer en tant que chaînes de caractères JavaScript. Cette fonction est nommée `gql`.

```jsx

// si vous utilisez apollo-boost
import { gql } from "apollo-boost";
// sinon, vous pouvez utiliser un package dédié graphql-tag
import gql from "graphql-tag";

// requête
const GET_POSTS = gql`
  query GetPosts($limit: Int) {
    posts(limit: $limit) {
      id
      body
      title
      createdAt
    }
  }
`;

// mutation
const CREATE_POST = gql`
  mutation CreatePost($title: String!, $body: String!) {
    insert_posts(objects: { title: $title, body: $body }) {
      affected_rows
    }
  }
`;

// abonnement
const GET_POST = gql`
  subscription GetPost($id: uuid!) {
    posts(where: { id: { _eq: $id } }) {
      id
      body
      title
      createdAt
    }
  }
`;
```

### Hook useQuery

Le hook `useQuery` est probablement le moyen le plus pratique d'effectuer une requête GraphQL, étant donné qu'il ne retourne pas une promesse qui doit être résolue.

Il est appelé en haut de tout composant fonctionnel (comme tous les hooks devraient l'être) et reçoit en premier argument requis une requête analysée avec `gql`.

Il est préférable de l'utiliser lorsque vous avez des requêtes qui doivent être exécutées immédiatement, lorsqu'un composant est rendu, comme une liste de données que l'utilisateur souhaiterait voir immédiatement lorsque la page se charge.

`useQuery` retourne un objet à partir duquel nous pouvons facilement déstructurer les valeurs dont nous avons besoin. Lors de l'exécution d'une requête, il y a trois valeurs principales que nous devrons utiliser dans chaque composant dans lequel nous récupérons des données. Ce sont `loading`, `error` et `data`.

```jsx
const GET_POSTS = gql`
  query GetPosts($limit: Int) {
    posts(limit: $limit) {
      id
      body
      title
      createdAt
    }
  }
`;

function App() {
  const { loading, error, data } = useQuery(GET_POSTS, {
    variables: { limit: 5 },
  });

  if (loading) return <div>Chargement...</div>;
  if (error) return <div>Erreur !</div>;

  return data.posts.map((post) => <Post key={post.id} post={post} />);
}
```

Avant de pouvoir afficher les données que nous récupérons, nous devons gérer le moment où nous chargeons (quand `loading` est défini sur true) et où nous tentons de récupérer les données.

À ce moment-là, nous affichons une div avec le texte "Chargement" ou un indicateur de chargement. Nous devons également gérer la possibilité qu'il y ait une erreur lors de la récupération de notre requête, comme s'il y a une erreur réseau ou si nous avons fait une erreur en écrivant notre requête (erreur de syntaxe).

Une fois que nous avons terminé le chargement et qu'il n'y a pas d'erreur, nous pouvons utiliser nos données dans notre composant, généralement pour les afficher à nos utilisateurs (comme nous le faisons dans l'exemple ci-dessus).

Il y a d'autres valeurs que nous pouvons déstructurer à partir de l'objet que `useQuery` retourne, mais vous aurez besoin de `loading`, `error` et `data` dans pratiquement chaque composant où vous exécutez `useQuery`. Vous pouvez voir une liste complète de toutes les données que nous pouvons obtenir de useQuery [ici](https://www.apollographql.com/docs/react/api/react-hooks/#result).

### Hook useLazyQuery

Le hook `useLazyQuery` offre une autre façon d'effectuer une requête, qui est destinée à être exécutée à un moment donné après le rendu du composant ou en réponse à un changement de données donné.

`useLazyQuery` est très utile pour les choses qui se produisent à n'importe quel moment inconnu, comme en réponse à une opération de recherche de l'utilisateur.

```jsx
function Search() {
  const [query, setQuery] = React.useState("");
  const [searchPosts, { data }] = useLazyQuery(SEARCH_POSTS, {
    variables: { query: `%${query}%` },
  });
  const [results, setResults] = React.useState([]);

  React.useEffect(() => {
    if (!query) return;
    // la fonction d'exécution de la requête ne retourne pas une promesse
    searchPosts();
    if (data) {
      setResults(data.posts);
    }
  }, [query, data, searchPosts]);

  if (called && loading) return <div>Chargement...</div>;

  return results.map((result) => (
    <SearchResult key={result.id} result={result} />
  ));
}

```

`useLazyQuery` diffère de `useQuery`, tout d'abord, par ce qui est retourné par le hook. Il retourne un tableau que nous pouvons déstructurer, au lieu d'un objet.

Puisque nous voulons effectuer cette requête à un moment donné après le montage du composant, le premier élément que nous pouvons déstructurer est une fonction que vous pouvez appeler pour effectuer cette requête lorsque vous le choisissez. Cette fonction de requête est nommée `searchPosts` dans l'exemple ci-dessus.

La deuxième valeur déstructurée dans le tableau est un objet, que nous pouvons utiliser pour la déstructuration d'objet et à partir duquel nous pouvons obtenir toutes les mêmes propriétés que nous avons obtenues de `useQuery`, telles que `loading`, `error` et `data`.

Nous obtenons également une propriété importante nommée `called`, qui nous indique si nous avons réellement appelé cette fonction pour effectuer notre requête. Dans ce cas, si `called` est vrai et `loading` est vrai, nous voulons retourner "Chargement..." au lieu de nos données réelles, car nous attendons que les données soient retournées. C'est ainsi que `useLazyQuery` gère la récupération des données de manière synchrone sans aucune promesse.

Notez que nous passons à nouveau les variables requises pour l'opération de requête en tant que propriété, variables, au deuxième argument. Cependant, si nous en avons besoin, nous pouvons passer ces variables sur un objet fourni à la fonction de requête elle-même.

### Hook useMutation

Maintenant que nous savons comment exécuter des requêtes paresseuses, nous savons exactement comment travailler avec le hook `useMutation`.

Comme le hook `useLazyQuery`, il retourne un tableau que nous pouvons déstructurer en ses deux éléments. Dans le premier élément, nous obtenons une fonction, que dans ce cas, nous pouvons appeler pour effectuer notre opération de mutation. Pour l'élément suivant, nous pouvons à nouveau déstructurer un objet qui nous retourne `loading`, `error` et `data`.

```jsx
import { useMutation } from "@apollo/react-hooks";
import { gql } from "apollo-boost";

const CREATE_POST = gql`
  mutation CreatePost($title: String!, $body: String!) {
    insert_posts(objects: { body: $body, title: $title }) {
      affected_rows
    }
  }
`;

function NewPost() {
  const [title, setTitle] = React.useState("");
  const [body, setBody] = React.useState("");
  const [createPost, { loading, error }] = useMutation(CREATE_POST);

  function handleCreatePost(event) {
    event.preventDefault();
    // la fonction de mutation ne retourne pas non plus une promesse
    createPost({ variables: { title, body } });
  }

  return (
    <div>
      <h1>Nouveau Post</h2>
      <form onSubmit={handleCreatePost}>
        <input onChange={(event) => setTitle(event.target.value)} />
        <textarea onChange={(event) => setBody(event.target.value)} />
        <button disabled={loading} type="submit">
          Soumettre
        </button>
        {error && <p>{error.message}</p>}
      </form>
    </div>
  );
}
```

Contrairement aux requêtes, cependant, nous n'utilisons pas `loading` ou `error` pour rendre quelque chose conditionnellement. Nous utilisons généralement `loading` dans des situations comme lorsque nous soumettons un formulaire pour l'empêcher d'être soumis plusieurs fois, afin d'éviter d'exécuter la même mutation inutilement (comme vous pouvez le voir dans l'exemple ci-dessus).

Nous utilisons `error` pour afficher ce qui ne va pas avec notre mutation à nos utilisateurs. Si, par exemple, certaines valeurs requises pour notre mutation ne sont pas fournies, nous pouvons facilement utiliser ces données d'erreur pour afficher conditionnellement un message d'erreur dans la page afin que l'utilisateur puisse, espérons-le, corriger ce qui ne va pas.

Par rapport au passage de variables au deuxième argument de `useMutation`, nous pouvons accéder à quelques rappels utiles lorsque certaines choses se produisent, comme lorsque la mutation est terminée et lorsqu'il y a une erreur. Ces rappels sont nommés `onCompleted` et `onError`.

Le rappel `onCompleted` nous donne accès aux données de mutation retournées et il est très utile de faire quelque chose lorsque la mutation est terminée, comme aller à une page différente. Le rappel `onError` nous donne l'erreur retournée lorsqu'il y a un problème avec la mutation et nous donne d'autres motifs pour gérer nos erreurs.

```jsx
const [createPost, { loading, error }] = useMutation(CREATE_POST, {
  onCompleted: (data) => console.log("Données de la mutation", data),
  onError: (error) => console.error("Erreur lors de la création d'un post", error),
});
```

### Hook useSubscription

Le hook useSubscription fonctionne exactement comme le hook useQuery.

useSubscription retourne un objet que nous pouvons déstructurer, qui inclut les mêmes propriétés, loading, data et error.

Il exécute notre abonnement immédiatement lorsque le composant est rendu. Cela signifie que nous devons gérer les états de chargement et d'erreur, et seulement ensuite afficher/utiliser nos données.

```jsx
import { useSubscription } from "@apollo/react-hooks";
import gql from "graphql-tag";

const GET_POST = gql`
  subscription GetPost($id: uuid!) {
    posts(where: { id: { _eq: $id } }) {
      id
      body
      title
      createdAt
    }
  }
`;

// où id provient des paramètres de route -> /post/:id
function PostPage({ id }) {
  const { loading, error, data } = useSubscription(GET_POST, {
    variables: { id },
    // shouldResubscribe: true (par défaut: false)
    // onSubscriptionData: data => console.log('nouvelles données', data)
    // fetchPolicy: 'network-only' (par défaut: 'cache-first')
  });

  if (loading) return <div>Chargement...</div>;
  if (error) return <div>Erreur !</div>;

  const post = data.posts[0];

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}
```

Tout comme useQuery, useLazyQuery et useMutation, useSubscription accepte `variables` en tant que propriété fournie sur le deuxième argument.

Il accepte également, cependant, certaines propriétés utiles telles que `shouldResubscribe`. Il s'agit d'une valeur booléenne, qui permettra à notre abonnement de se réabonner automatiquement, lorsque nos props changent. Cela est utile lorsque nous passons des variables à notre hub d'abonnement props que nous savons changer.

De plus, nous avons une fonction de rappel appelée `onSubscriptionData`, qui nous permet d'appeler une fonction chaque fois que le hook d'abonnement reçoit de nouvelles données. Enfin, nous pouvons définir la `fetchPolicy`, qui par défaut est 'cache-first'.

### Définition manuelle de la politique de récupération

Ce qui peut être très utile avec Apollo, c'est qu'il vient avec son propre cache, qu'il utilise pour gérer les données que nous interrogeons à partir de notre endpoint GraphQL.

Cependant, parfois, nous constatons que, en raison de ce cache, les choses ne sont pas mises à jour dans l'interface utilisateur de la manière que nous souhaitons.

Dans de nombreux cas, nous ne le faisons pas, comme dans l'exemple ci-dessous, où nous éditons un post sur la page d'édition, puis après avoir édité notre post, nous naviguons vers la page d'accueil pour le voir dans une liste de tous les posts, mais nous voyons les anciennes données à la place :

```jsx
// route : /edit/:postId
function EditPost({ id }) {
  const { loading, data } = useQuery(GET_POST, { variables: { id } });
  const [title, setTitle] = React.useState(loading ? data?.posts[0].title : "");
  const [body, setBody] = React.useState(loading ? data?.posts[0].body : "");
  const [updatePost] = useMutation(UPDATE_POST, {
    // après la mise à jour du post, nous allons à la page d'accueil
    onCompleted: () => history.push("/"),
  });

  function handleUpdatePost(event) {
    event.preventDefault();
    updatePost({ variables: { title, body, id } });
  }

  return (
    <form onSubmit={handleUpdatePost}>
      <input
        onChange={(event) => setTitle(event.target.value)}
        defaultValue={title}
      />
      <input
        onChange={(event) => setBody(event.target.value)}
        defaultValue={body}
      />
      <button type="submit">Soumettre</button>
    </form>
  );
}

// route : / (page d'accueil)
function App() {
  const { loading, error, data } = useQuery(GET_POSTS, {
    variables: { limit: 5 },
  });

  if (loading) return <div>Chargement...</div>;
  if (error) return <div>Erreur !</div>;

  // post mis à jour non affiché, toujours voir les anciennes données
  return data.posts.map((post) => <Post key={post.id} post={post} />);
}
```

Cela n'est pas seulement dû au cache Apollo, mais aussi aux instructions pour les données que la requête doit récupérer. Nous pouvons changer la manière dont la requête est récupérée en utilisant la propriété `fetchPolicy`.

Par défaut, la `fetchPolicy` est définie sur 'cache-first'. Elle va essayer de regarder le cache pour obtenir nos données au lieu de les obtenir depuis le réseau.

Une façon simple de résoudre ce problème de ne pas voir les nouvelles données est de changer la politique de récupération. Cependant, cette approche n'est pas idéale d'un point de vue performance, car elle nécessite de faire une requête supplémentaire (utiliser le cache directement ne le fait pas, car il s'agit de données locales).

Il existe de nombreuses options différentes pour la politique de récupération listées ci-dessous :

```jsx
{
  fetchPolicy: "cache-first"; // par défaut
  /*
    cache-and-network
    cache-first
    cache-only
    network-only
    no-cache
    standby
  */
}
```

Je ne vais pas entrer dans les détails de ce que chaque politique fait exactement, mais pour résoudre notre problème immédiat, si vous voulez toujours qu'une requête obtienne les dernières données en les demandant depuis le réseau, nous définissons `fetchPolicy` sur 'network-first'.

```jsx
const { loading, error, data } = useQuery(GET_POSTS, {
  variables: { limit: 5 },
  fetchPolicy: "network-first"
});
```

### Mise à jour du cache après une mutation

Au lieu de contourner le cache en changeant la politique de récupération de `useQuery`, essayons de résoudre ce problème en mettant à jour manuellement le cache.

Lors de l'exécution d'une mutation avec `useMutation`, nous avons accès à un autre rappel, connu sous le nom de `update`.

`update` nous donne un accès direct au cache ainsi qu'aux données qui sont retournées par une mutation réussie. Cela nous permet de lire une requête donnée à partir du cache, de prendre ces nouvelles données et d'écrire les nouvelles données dans la requête, ce qui mettra ensuite à jour ce que l'utilisateur voit.

Travailler avec le cache manuellement est un processus délicat que beaucoup de gens tendent à éviter, mais il est très utile car il économise du temps et des ressources en évitant d'avoir à effectuer la même requête plusieurs fois pour mettre à jour le cache manuellement.

```jsx
function EditPost({ id }) {
  const [updatePost] = useMutation(UPDATE_POST, {
    update: (cache, data) => {
      const { posts } = cache.readQuery(GET_POSTS);
      const newPost = data.update_posts.returning;
      const updatedPosts = posts.map((post) =>
        post.id === id ? newPost : post
      );
      cache.writeQuery({ query: GET_POSTS, data: { posts: updatedPosts } });
    },
    onCompleted: () => history.push("/"),
  });

  // ...
}
```

Nous voulons d'abord lire la requête et obtenir les données précédentes. Ensuite, nous devons prendre les nouvelles données. Dans ce cas, pour trouver le post avec un id donné et le remplacer par les données `newPost`, sinon avoir les données précédentes, puis écrire ces données dans la même requête, en veillant à ce qu'elles aient la même structure de données qu'avant.

Après tout cela, chaque fois que nous éditons un post et sommes redirigés vers la page d'accueil, nous devrions voir ces nouvelles données de post.

### Nouvelle exécution des requêtes avec useQuery

Supposons que nous affichons une liste de posts en utilisant une requête `GET_POSTS` et que nous en supprimons un avec une mutation `DELETE_POST`.

Lorsque l'utilisateur supprime un post, que voulons-nous qu'il se passe ?

Naturellement, nous voulons qu'il soit supprimé de la liste, à la fois des données et de ce qui est affiché aux utilisateurs. Lorsque la mutation est effectuée, cependant, la requête ne sait pas que les données ont changé.

Il existe plusieurs façons de mettre à jour ce que nous voyons, mais une approche consiste à réexécuter la requête.

Nous pouvons le faire en récupérant la fonction `refetch` que nous pouvons déstructurer à partir de l'objet retourné par le hook `useQuery` et en la passant à la mutation pour qu'elle soit exécutée lorsqu'elle est terminée, en utilisant la fonction de rappel `onCompleted` :

```jsx
function Posts() {
  const { loading, data, refetch } = useQuery(GET_POSTS);

  if (loading) return <div>Chargement...</div>;

  return data.posts.map((post) => (
    <Post key={post.id} post={post} refetch={refetch} />
  ));
}

function Post({ post, refetch }) {
  const [deletePost] = useMutation(DELETE_POST, {
    onCompleted: () => refetch(),
  });

  function handleDeletePost(id) {
    if (window.confirm("Êtes-vous sûr de vouloir supprimer ce post ?")) {
      deletePost({ variables: { id } });
    }
  }

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      <button onClick={() => handleDeletePost(post.id)}>Supprimer</button>
    </div>
  );
}
```

### Nouvelle exécution des requêtes avec useMutation

Notez que nous pouvons également utiliser le hook `useMutation` pour réexécuter nos requêtes via un argument fourni à la fonction de mutation, appelé `refetchQueries`.

Il accepte un tableau de requêtes que nous voulons réexécuter après qu'une mutation soit effectuée. Chaque requête est fournie dans un objet, comme nous le ferions pour client.query(), et se compose d'une propriété query et d'une propriété variables.

Voici un exemple minimal pour réexécuter notre requête `GET_POSTS` après la création d'un nouveau post :

```jsx
function NewPost() {
  const [createPost] = useMutation(CREATE_POST, {
    refetchQueries: [
      { 
        query: GET_POSTS, 
        variables: { limit: 5 } 
      }
    ],
  });

  // ...
}
```

### Utilisation du client avec useApolloClient

Nous pouvons obtenir l'accès au client dans tous nos composants avec l'aide d'un hook spécial appelé useApolloClient. Nous exécutons ce hook en haut de notre composant fonctionnel et nous obtenons le client lui-même.

```jsx
function Logout() {
  const client = useApolloClient();
  // client est le même que ce que nous avons créé avec new ApolloClient()

  function handleLogout() {
    // gérer la déconnexion de l'utilisateur, puis effacer les données stockées
    logoutUser();
    client.resetStore().then(() => console.log("déconnecté !"));
    /* Soyez conscient que .resetStore() est asynchrone */
  }

  return <button onClick={handleLogout}>Déconnexion</button>;
}
```

Et à partir de là, nous pouvons exécuter toutes les mêmes requêtes, mutations et abonnements.

Notez qu'il existe de nombreuses autres fonctionnalités qui accompagnent les méthodes qui accompagnent le client. En utilisant le client, nous pouvons également écrire et lire des données vers et depuis le cache qu'Apollo configure (en utilisant `client.readData()` et `client.writeData()`).

Travailler avec le cache Apollo mérite son propre cours intensif. Un grand avantage de travailler avec Apollo est que nous pouvons également l'utiliser comme un système de gestion d'état pour remplacer des solutions comme Redux pour notre état global. Si vous souhaitez en savoir plus sur l'utilisation d'Apollo pour gérer l'état global de l'application, vous pouvez [consulter le lien suivant](https://www.apollographql.com/docs/react/data/local-state/).

J'ai tenté de rendre cette aide-mémoire aussi complète que possible, bien qu'elle laisse encore de côté de nombreuses fonctionnalités d'Apollo qui méritent d'être étudiées.

Si vous souhaitez en savoir plus sur Apollo, assurez-vous de consulter la [documentation officielle d'Apollo](https://www.apollographql.com/docs/react/).

### Télécharger l'aide-mémoire

Vous voulez une référence rapide de tous ces concepts ?

[![Aide-mémoire React et Apollo 2020](https://dev-to-uploads.s3.amazonaws.com/i/7herw99hu78t8gspo88d.png)](https://reedbarger.com/resources/react-apollo-2020/)
*Cliquez pour obtenir l'aide-mémoire PDF complète*

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*