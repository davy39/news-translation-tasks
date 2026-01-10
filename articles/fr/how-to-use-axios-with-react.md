---
title: 'Comment utiliser Axios avec React : Le guide définitif (2021)'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-07-13T07:36:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-axios-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/how-to-use-axios-with-react.png
tags:
- name: axios
  slug: axios
- name: hooks
  slug: hooks
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
seo_title: 'Comment utiliser Axios avec React : Le guide définitif (2021)'
seo_desc: "In this guide, you will see exactly how to use Axios.js with React using\
  \ tons of real-world examples featuring React hooks. \nYou'll see why you should\
  \ use Axios as a data fetching library, how to set it up with React, and perform\
  \ every type of HTTP r..."
---

Dans ce guide, vous verrez exactement comment utiliser Axios.js avec React en utilisant de nombreux exemples concrets mettant en vedette les hooks React. 

Vous verrez pourquoi vous devriez utiliser Axios comme bibliothèque de récupération de données, comment le configurer avec React, et comment effectuer chaque type de requête HTTP avec celui-ci.

Ensuite, nous aborderons des fonctionnalités plus avancées comme la création d'une instance Axios pour la réutilisabilité, l'utilisation de async-await avec Axios pour la simplicité, et comment utiliser Axios comme un hook personnalisé.

Commençons tout de suite !

### **Vous voulez votre propre copie ? 📄**

**[Cliquez ici pour télécharger l'aide-mémoire au format PDF](https://reedbarger.com/resources/react-axios-2021)** (cela prend 5 secondes).

Il inclut toutes les informations essentielles ici sous forme de guide PDF pratique.

## Table des matières

* [Qu'est-ce qu'Axios ?](#heading-qu-est-ce-qu-axios)
* [Pourquoi utiliser Axios dans React ?](#heading-pourquoi-utiliser-axios-dans-react)
* [Comment configurer Axios avec React](#heading-comment-configurer-axios-avec-react)
* [Comment faire une requête GET (Récupérer des données)](#heading-comment-faire-une-requete-get)
* [Comment faire une requête POST (Créer des données)](#heading-comment-faire-une-requete-post)
* [Comment faire une requête PUT (Mettre à jour des données)](#heading-comment-faire-une-requete-put)
* [Comment faire une requête DELETE (Supprimer des données)](#heading-comment-faire-une-requete-delete)
* [Comment gérer les erreurs avec Axios](#heading-comment-gerer-les-erreurs-avec-axios)
* [Comment créer une instance Axios](#heading-comment-creer-une-instance-axios)
* [Comment utiliser la syntaxe Async-Await avec Axios](#heading-comment-utiliser-la-syntaxe-async-await-avec-axios)
* [Comment créer un hook personnalisé `useAxios`](#heading-comment-creer-un-hook-personnalise-useaxios)

## Qu'est-ce qu'Axios ?

Axios est une bibliothèque cliente HTTP qui vous permet de faire des requêtes à une URL donnée :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-12-at-1.14.41-PM.png)

Il peut s'agir d'une API externe ou de votre propre serveur backend Node.js, par exemple.

En faisant une requête, vous attendez de votre API qu'elle effectue une opération selon la requête que vous avez faite.

Par exemple, si vous faites une requête GET, vous vous attendez à recevoir des données à afficher dans votre application.

## Pourquoi utiliser Axios dans React

Il existe un certain nombre de bibliothèques différentes que vous pouvez utiliser pour faire ces requêtes, alors pourquoi choisir Axios ? 

Voici **cinq raisons** pour lesquelles vous devriez utiliser Axios comme client pour faire des requêtes HTTP : 

1. Il a de bonnes valeurs par défaut pour travailler avec des données JSON. Contrairement à des alternatives comme l'API Fetch, vous n'avez souvent pas besoin de définir vos en-têtes. Ou d'effectuer des tâches fastidieuses comme convertir le corps de votre requête en une chaîne JSON.
2. Axios a des noms de fonctions qui correspondent à toutes les méthodes HTTP. Pour effectuer une requête GET, vous utilisez la méthode `.get()`.
3. Axios fait plus avec moins de code. Contrairement à l'API Fetch, vous n'avez besoin que d'un seul callback `.then()` pour accéder à vos données JSON demandées.
4. Axios a une meilleure gestion des erreurs. Axios génère des erreurs 400 et 500 pour vous. Contrairement à l'API Fetch, où vous devez vérifier le code de statut et générer l'erreur vous-même. 
5. Axios peut être utilisé sur le serveur ainsi que sur le client. Si vous écrivez une application Node.js, sachez qu'Axios peut également être utilisé dans un environnement séparé du navigateur. 

## Comment configurer Axios avec React

Utiliser Axios avec React est un processus très simple. Vous avez besoin de trois choses :

1. Un projet React existant
2. Installer Axios avec npm/yarn
3. Une URL d'API pour faire des requêtes

Le moyen le plus rapide de créer une nouvelle application React est d'aller sur [react.new](https://react.new).

Si vous avez un projet React existant, vous devez simplement installer Axios avec npm (ou tout autre gestionnaire de paquets) :

```bash
npm install axios
```

Dans ce guide, vous utiliserez l'API JSON Placeholder pour obtenir et modifier les données des posts.

Voici une liste de toutes les différentes routes auxquelles vous pouvez faire des requêtes, ainsi que la méthode HTTP appropriée pour chacune :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-10-at-12.21.28-PM.png)

Voici un exemple rapide de toutes les opérations que vous allez effectuer avec Axios et votre URL d'API — récupérer, créer, mettre à jour et supprimer des posts :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/axios-react.gif)

## Comment faire une requête GET

Pour récupérer des données, faites une requête GET.

Tout d'abord, vous allez faire une requête pour des posts individuels. Si vous regardez l'URL, vous obtenez le premier post de l'URL `/posts` :

```js
import axios from "axios";
import React from "react";

const baseURL = "https://jsonplaceholder.typicode.com/posts/1";

export default function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setPost(response.data);
    });
  }, []);

  if (!post) return null;

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}
```

Pour effectuer cette requête lorsque le composant est monté, vous utilisez le hook `useEffect`. Cela implique d'importer Axios, d'utiliser la méthode `.get()` pour faire une requête GET à votre URL, et d'utiliser un callback `.then()` pour obtenir toutes les données de la réponse.

La réponse est retournée sous forme d'objet. Les données (qui dans ce cas est un post avec les propriétés `id`, `title`, et `body`) sont placées dans un état appelé `post` qui est affiché dans le composant. 

Notez que vous pouvez toujours trouver les données demandées à partir de la propriété `.data` dans la réponse.

## Comment faire une requête POST

Pour créer de nouvelles données, faites une requête POST. 

Selon l'API, cela doit être effectué sur l'URL `/posts`. Si vous regardez le code ci-dessous, vous verrez qu'il y a un bouton pour créer un post :

```js
import axios from "axios";
import React from "react";

const baseURL = "https://jsonplaceholder.typicode.com/posts";

export default function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(`${baseURL}/1`).then((response) => {
      setPost(response.data);
    });
  }, []);

  function createPost() {
    axios
      .post(baseURL, {
        title: "Hello World!",
        body: "This is a new post."
      })
      .then((response) => {
        setPost(response.data);
      });
  }

  if (!post) return "No post!"

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      <button onClick={createPost}>Create Post</button>
    </div>
  );
}
```

Lorsque vous cliquez sur le bouton, il appelle la fonction `createPost`.

Pour faire cette requête POST avec Axios, vous utilisez la méthode `.post()`. En tant que deuxième argument, vous incluez une propriété d'objet qui spécifie ce que vous voulez que le nouveau post soit.

Une fois de plus, utilisez un callback `.then()` pour obtenir les données de la réponse et remplacer le premier post que vous avez obtenu par le nouveau post que vous avez demandé.

Cela est très similaire à la méthode `.get()`, mais la nouvelle ressource que vous voulez créer est fournie en tant que deuxième argument après l'URL de l'API.

## Comment faire une requête PUT

Pour mettre à jour une ressource donnée, faites une requête PUT.

Dans ce cas, vous allez mettre à jour le premier post.

Pour ce faire, vous allez à nouveau créer un bouton. Mais cette fois, le bouton appellera une fonction pour mettre à jour un post :

```js
import axios from "axios";
import React from "react";

const baseURL = "https://jsonplaceholder.typicode.com/posts";

export default function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(`${baseURL}/1`).then((response) => {
      setPost(response.data);
    });
  }, []);

  function updatePost() {
    axios
      .put(`${baseURL}/1`, {
        title: "Hello World!",
        body: "This is an updated post."
      })
      .then((response) => {
        setPost(response.data);
      });
  }

  if (!post) return "No post!"

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      <button onClick={updatePost}>Update Post</button>
    </div>
  );
}
```

Dans le code ci-dessus, vous utilisez la méthode PUT d'Axios. Et comme avec la méthode POST, vous incluez les propriétés que vous voulez voir dans la ressource mise à jour.

Encore une fois, en utilisant le callback `.then()`, vous mettez à jour le JSX avec les données qui sont retournées.

## Comment faire une requête DELETE

Enfin, pour supprimer une ressource, utilisez la méthode DELETE.

Par exemple, nous allons supprimer le premier post.

Notez que vous n'avez pas besoin d'un deuxième argument pour effectuer cette requête :

```js
import axios from "axios";
import React from "react";

const baseURL = "https://jsonplaceholder.typicode.com/posts";

export default function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(`${baseURL}/1`).then((response) => {
      setPost(response.data);
    });
  }, []);

  function deletePost() {
    axios
      .delete(`${baseURL}/1`)
      .then(() => {
        alert("Post deleted!");
        setPost(null)
      });
  }

  if (!post) return "No post!"

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      <button onClick={deletePost}>Delete Post</button>
    </div>
  );
}
```

Dans la plupart des cas, vous n'avez pas besoin des données qui sont retournées par la méthode `.delete()`.

Mais dans le code ci-dessus, le callback `.then()` est toujours utilisé pour s'assurer que votre requête est résolue avec succès.

Dans le code ci-dessus, après qu'un post est supprimé, l'utilisateur est averti qu'il a été supprimé avec succès. Ensuite, les données du post sont effacées de l'état en les réinitialisant à leur valeur initiale `null`.

De plus, une fois qu'un post est supprimé, le texte "No post" est affiché immédiatement après le message d'alerte.

## Comment gérer les erreurs avec Axios

Qu'en est-il de la gestion des erreurs avec Axios ? 

Que se passe-t-il s'il y a une erreur lors de la requête ? Par exemple, vous pourriez transmettre les mauvaises données, faire une requête à la mauvaise URL, ou avoir une erreur réseau.

Pour simuler une erreur, vous allez envoyer une requête à une URL d'API qui n'existe pas : `/posts/asdf`.

Cette requête retournera un code de statut `404` :

```js
import axios from "axios";
import React from "react";

const baseURL = "https://jsonplaceholder.typicode.com/posts";

export default function App() {
  const [post, setPost] = React.useState(null);
  const [error, setError] = React.useState(null);

  React.useEffect(() => {
    // invalid url will trigger an 404 error
    axios.get(`${baseURL}/asdf`).then((response) => {
      setPost(response.data);
    }).catch(error => {
      setError(error);
    });
  }, []);
  
  if (error) return `Error: ${error.message}`;
  if (!post) return "No post!"

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}
```

Dans ce cas, au lieu d'exécuter le callback `.then()`, Axios va générer une erreur et exécuter la fonction de callback `.catch()`.

Dans cette fonction, nous prenons les données d'erreur et les plaçons dans l'état pour alerter notre utilisateur de l'erreur. Donc si nous avons une erreur, nous allons afficher ce message d'erreur.

Dans cette fonction, les données d'erreur sont placées dans l'état et utilisées pour alerter les utilisateurs de l'erreur. Donc si une erreur survient, un message d'erreur est affiché.

Lorsque vous exécutez ce code, vous verrez le texte, "Error: Request failed with status code 404".

## Comment créer une instance Axios

Si vous regardez les exemples précédents, vous verrez qu'il y a une `baseURL` que vous utilisez comme partie de l'URL pour que Axios effectue ces requêtes.

Cependant, il devient un peu fastidieux de continuer à écrire cette `baseURL` pour chaque requête. Ne pourriez-vous pas simplement faire en sorte qu'Axios se souvienne de la `baseURL` que vous utilisez, puisque cela implique toujours une URL similaire ? 

En fait, vous pouvez. Si vous créez une instance avec la méthode `.create()`, Axios se souviendra de cette `baseURL`, ainsi que d'autres valeurs que vous pourriez vouloir spécifier pour chaque requête, y compris les en-têtes : 

```js
import axios from "axios";
import React from "react";

const client = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com/posts" 
});

export default function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    client.get("/1").then((response) => {
      setPost(response.data);
    });
  }, []);

  function deletePost() {
    client
      .delete("/1")
      .then(() => {
        alert("Post deleted!");
        setPost(null)
      });
  }

  if (!post) return "No post!"

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      <button onClick={deletePost}>Delete Post</button>
    </div>
  );
}
```

La seule propriété dans l'objet de configuration ci-dessus est `baseURL`, à laquelle vous passez l'URL.

La fonction `.create()` retourne une nouvelle instance, qui dans ce cas est appelée `client`.

Ensuite, vous pouvez utiliser toutes les mêmes méthodes que précédemment, mais vous n'avez plus besoin d'inclure la `baseURL` en tant que premier argument. Vous devez simplement référencer la route spécifique que vous voulez, par exemple, `/`, `/1`, et ainsi de suite.

## Comment utiliser la syntaxe Async-Await avec Axios

Un grand avantage de l'utilisation des promesses en JavaScript (y compris les applications React) est la syntaxe async-await.

Async-await vous permet d'écrire un code beaucoup plus propre sans les fonctions de callback `then` et `catch`. De plus, le code avec async-await ressemble beaucoup à du code synchrone, et est plus facile à comprendre.

Mais comment utiliser la syntaxe async-await avec Axios ?

Dans l'exemple ci-dessous, les posts sont récupérés et il y a toujours un bouton pour supprimer ce post :

```js
import axios from "axios";
import React from "react";

const client = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com/posts" 
});

export default function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    async function getPost() {
      const response = await client.get("/1");
      setPost(response.data);
    }
    getPost();
  }, []);

  async function deletePost() {
    await client.delete("/1");
    alert("Post deleted!");
    setPost(null);
  }

  if (!post) return "No post!"

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      <button onClick={deletePost}>Delete Post</button>
    </div>
  );
}
```

Cependant, dans `useEffect`, il y a une fonction `async` appelée `getPost`.

La rendre `async` vous permet d'utiliser le mot-clé `await` pour résoudre la requête GET et définir ces données dans l'état à la ligne suivante sans le callback `.then()`. 

Notez que la fonction `getPost` est appelée immédiatement après avoir été créée.

De plus, la fonction `deletePost` est maintenant `async`, ce qui est une exigence pour utiliser le mot-clé `await` qui résout la promesse qu'elle retourne (chaque méthode Axios retourne une promesse à résoudre).

Après avoir utilisé le mot-clé `await` avec la requête DELETE, l'utilisateur est averti que le post a été supprimé, et le post est défini à `null`.

Comme vous pouvez le voir, async-await nettoie considérablement le code, et vous pouvez l'utiliser avec Axios très facilement.

## Comment créer un hook personnalisé `useAxios`

Async-await est un excellent moyen de simplifier votre code, mais vous pouvez aller encore plus loin.

Au lieu d'utiliser `useEffect` pour récupérer des données lorsque le composant est monté, vous pourriez créer votre propre hook personnalisé avec Axios pour effectuer la même opération en tant que fonction réutilisable.

Bien que vous puissiez créer ce hook personnalisé vous-même, il existe une très bonne bibliothèque qui vous donne un hook personnalisé `useAxios` appelé use-axios-client.

Tout d'abord, installez le package :

```
npm install use-axios-client
```

Pour utiliser le hook lui-même, importez `useAxios` depuis use-axios-client en haut du composant. 

Puisque vous n'avez plus besoin de `useEffect`, vous pouvez supprimer l'import React :

```js
import { useAxios } from "use-axios-client";

export default function App() {
  const { data, error, loading } = useAxios({
    url: "https://jsonplaceholder.typicode.com/posts/1"
  });

  if (loading || !data) return "Loading...";
  if (error) return "Error!";

  return (
    <div>
      <h1>{data.title}</h1>
      <p>{data.body}</p>
    </div>
  ) 
}
```

Maintenant, vous pouvez appeler `useAxios` en haut du composant de l'application, passer l'URL à laquelle vous voulez faire une requête, et le hook retourne un objet avec toutes les valeurs dont vous avez besoin pour gérer les différents états : `loading`, `error` et les données résolues `data`.

Au cours de l'exécution de cette requête, la valeur `loading` sera vraie. Si une erreur survient, vous voudrez afficher cet état d'erreur. Sinon, si vous avez les données retournées, vous pouvez les afficher dans l'interface utilisateur.

L'avantage des hooks personnalisés comme celui-ci est qu'ils réduisent considérablement le code et le simplifient dans l'ensemble. 

Si vous cherchez une récupération de données encore plus simple avec Axios, essayez un hook personnalisé `useAxios` comme celui-ci.

## Qu'est-ce qui suit ?

Félicitations ! Vous savez maintenant comment utiliser l'une des bibliothèques clientes HTTP les plus puissantes pour alimenter vos applications React. 

J'espère que vous avez beaucoup appris de ce guide.

[Souvenez-vous que vous pouvez télécharger ce guide au format PDF pour le conserver comme référence future.](https://reedbarger.com/resources/react-axios-2021)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*