---
title: Comment récupérer des données d'API dans React
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2023-12-14T10:18:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-fetch-api-data-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Effective-Ways-for-Retrieving-API-Data-in-React-and-Python--1-.png
tags:
- name: api
  slug: api
- name: React
  slug: react
seo_title: Comment récupérer des données d'API dans React
seo_desc: 'When developing applications, you often need to get data from an API. This
  lets you deliver dynamic and often-updated content within your application.

  You''ll want to retrieve this data as you may need to interact with external services,
  communicate w...'
---

Lors du développement d'applications, vous avez souvent besoin de récupérer des données à partir d'une API. Cela vous permet de fournir un contenu dynamique et souvent mis à jour au sein de votre application.

Vous voudrez récupérer ces données car vous pourriez avoir besoin d'interagir avec des services externes, de communiquer avec un serveur distant ou d'accéder à une base de données.

Dans cet article, je vais vous montrer différentes méthodes pour récupérer des données en utilisant React comme exemple.

## Prérequis

* Installer [Node.js](https://nodejs.org/en)
* Assurez-vous d'avoir au moins une compréhension de base de [React.js](https://react.dev/).
* Un éditeur de texte

## Qu'est-ce qu'une API ?

API signifie Application Programming Interface (Interface de Programmation d'Application). Elle permet l'échange d'informations et de fonctionnalités entre différents systèmes, comme entre un site web et un serveur ou entre différentes applications logicielles.

Vous pouvez imaginer une API comme un serveur de restaurant. Vous n'allez pas dans la cuisine pour préparer votre repas lorsque vous dînez au restaurant. Au lieu de cela, vous informez le serveur de vos préférences, et il transmettra votre commande à l'équipe de cuisine. L'équipe de cuisine prépare la nourriture et la rend au serveur, qui vous la livre ensuite à votre table.

Une API fonctionne comme un serveur pour les applications logicielles. C'est un ensemble de règles qui permet à un programme d'en demander un autre pour quelque chose dont il a besoin. Elle sert de pont pour que les applications logicielles communiquent et interagissent.

### Pourquoi les API sont-elles importantes dans le développement web ?

Il y a plusieurs raisons pour lesquelles les API sont importantes dans le développement web. Passons en revue certaines d'entre elles ci-dessous :

* Les applications web ont besoin d'API pour obtenir des données de diverses sources, comme des bases de données ou des sites web.
* Les API sont une option évolutive pour gérer des volumes élevés de données ou de requêtes.
* Les développeurs utilisent des API pour exploiter des fonctionnalités et des services existants. Cela leur évite de réinventer la roue.
* Elles maintiennent la sécurité en garantissant que seuls les individus ou programmes autorisés peuvent les utiliser.
* Une API rend un site web ou une application mobile plus agréable à utiliser en intégrant des données.

## Qu'est-ce qu'une requête Hypertext Transfer Protocol (HTTP) ?

Lorsqu'un navigateur web ou une application mobile envoie un message à un serveur, on appelle cela une requête `HTTP`. Une requête `HTTP` consiste à demander au serveur des données spécifiques ou une action et à obtenir une réponse. Le serveur répond en interagissant avec les pages web et les services.

L'utilisation d'API dans le développement de logiciels rend les choses plus flexibles et efficaces. Elle renforce également la sécurité et permet à différents systèmes logiciels de bien fonctionner ensemble.

### Types de requêtes HTTP

Nous utilisons diverses méthodes de requête `HTTP`, telles que `get`, `post`, `put` et `delete`, pour obtenir et stocker des données dans notre base de données. Mais les requêtes les plus courantes sont les requêtes `get` et `post`.

Discutons de la signification de ces méthodes de requête `HTTP` :

* **GET :** Cette méthode récupère des données d'un point de terminaison (endpoint) spécifique. Considérez cela comme une demande d'information.
* **POST :** Cette méthode envoie des données à un point de terminaison spécifique. Par exemple, vous pouvez envoyer un message ou soumettre un formulaire. L'information sera ajoutée à la base de données.
* **PUT :** Cette méthode est utilisée pour mettre à jour un enregistrement ou une valeur de donnée à un point de terminaison désigné. Vous apportez des modifications à des informations existantes.
* **DELETE :** Cette méthode efface des données d'un point de terminaison spécifique. C'est comme jeter des choses inutiles.

Une façon largement adoptée de vérifier les API est de passer par le navigateur.

![Obtenir une réponse d'une API](https://www.freecodecamp.org/news/content/images/2023/12/image-35.png)
_Obtenir une réponse d'une API_

Pour en savoir plus sur les façons d'obtenir des données, consultez cet article : [Getting Started with Application Programming Interfaces (APIs)](https://ijaycent.hashnode.dev/getting-started-with-application-programming-interface-api).

## Comment récupérer des données dans React

Il existe différentes manières de récupérer des données dans React. Avant de commencer, commençons par écrire du code boilerplate React ou par créer un modèle dans notre éditeur.

Voici la commande pour faire cela :

```js
npx create-react-app ./ ou npx create-vite@latest ./
```

![création d'un modèle pour notre projet](https://www.freecodecamp.org/news/content/images/2023/12/image-36.png)
_création d'un modèle pour notre projet_

Après cela, tapez la commande suivante :

```js
npm run dev
```

Cela lancera le serveur de développement.

Dans l'image ci-dessus, vous remarquerez que j'ai ajouté un point (.) immédiatement après la commande.

C'est un raccourci pratique pour créer le modèle dans le répertoire actuel.

## Différentes manières de récupérer des données dans React

### 1. Utiliser la méthode stale-while-revalidate (SWR)

Cette méthode est utilisée pour récupérer des données depuis un serveur et est utilisée dans React. Elle gère tous les problèmes qui peuvent survenir lors de l'obtention des données et vous aide à gérer leur stockage. `SWR` inclut `useState()` et `useEffect()`, il n'est donc pas nécessaire de les importer.

#### Les avantages de SWR

1. `SWR` accélère le temps de chargement de votre application en affichant des données plus anciennes tout en récupérant les dernières informations.
2. Il réduit la charge du serveur en minimisant le nombre de requêtes.
3. Même s'il y a une mauvaise connexion, ou pas de connexion du tout, SWR peut toujours afficher les données précédemment récupérées.
4. SWR gère l'acquisition et la maintenance des données sans utiliser de code sophistiqué.
5. Il sait quoi faire si quelque chose ne va pas pendant la collecte des données.
6. Vous pouvez modifier le fonctionnement de SWR pour mieux l'adapter à votre application.
7. Il offre une approche cohérente pour collecter et sauvegarder des données dans toute votre application.

#### Comment utiliser `SWR` pour obtenir des données

* Dans votre application, créez un fichier.
* Installez ensuite le package [SWR](https://swr.vercel.app/) dans votre application avec la commande suivante :

```js
npm i swr
```

* Importez `useSWR`, qui est un hook qui possède à la fois `useState()` et `useEffect()`, dans votre application.
* Définissez ensuite une variable constante en haut appelée `fetcher` et assignez-lui une fonction.

Cette fonction est capable de recevoir n'importe quel nombre d'arguments, désignés par la syntaxe `...args`.

La fonction ressemble à ceci :
`const fetcher = (...args) => fetch(...args).then(res => res.json())`

Voici à quoi devrait ressembler `Swr.jsx` :

```javascript
import useSWR from 'swr';

// Importer useSWR depuis le package swr

// fonction créée pour gérer la requête API
const fetcher = (...args) => fetch(...args).then((res) => res.json());

const Swr = () => {
  const {
    data: countries,
    error,
    isValidating,
  } = useSWR('https://restcountries.com/v2/all', fetcher);

  // Gère l'état d'erreur et de chargement
  if (error) return <div className='failed'>échec du chargement</div>;
  if (isValidating) return <div className="Loading">Chargement...</div>;

  return (
    <div>
      {countries &&
        countries.map((country, index) => (
          <img key={index} src={country.flags.png} alt='flag' width={100} />
        ))}
    </div>
  );
};

export default Swr;

```

Voyons ce qui se passe dans le code ci-dessus :

* La première chose que nous avons faite a été d'importer la bibliothèque `SWR`.
* Ensuite, nous avons défini une fonction pour gérer la requête API.
* En retour, nous avons utilisé la méthode `map()` pour itérer à travers la liste des nations.
* Nous avons mis une ligne `&&` pour nous assurer que s'il n'y a pas de problèmes et que les données ont été correctement reçues (ce qui signifie que la variable `countries` n'est pas nulle ou indéfinie), il procédera au mappage des données et affichera un élément `image` pour chaque nation.
* Enfin, nous avons exporté le composant vers la racine de l'application `App.jsx` ou `Index.jsx` afin qu'il puisse être visualisé dans le navigateur.

Voici le résultat :

![Utilisation de Swr](https://www.freecodecamp.org/news/content/images/2023/12/chrome_0YIvgfhfCl.gif)
_Le résultat de l'utilisation de Swr_

### 2. Utiliser la méthode JavaScript `Fetch()`

La méthode `fetch()` est bien connue pour récupérer des données à partir d'API. Elle est reconnue comme l'approche la plus simple et la plus utilisée.

#### Les avantages de l'utilisation de la méthode `fetch()`

1. La méthode `fetch()` facilite l'obtention d'informations sur Internet en utilisant JavaScript.
2. Elle vous permet d'envoyer des détails supplémentaires au serveur, comme qui vous êtes ou quel type de données vous souhaitez.
3. Elle est conçue pour bien fonctionner dans la plupart des navigateurs web récents.
4. La méthode `fetch()` prend en charge différentes méthodes `HTTP`. Ces méthodes incluent get, post, put et delete. Elles vous donnent de la flexibilité dans l'interaction avec les API.
5. La méthode `fetch()` est une méthode JavaScript native. Vous pouvez l'utiliser sans bibliothèques ou dépendances externes. Cela la rend légère et efficace.

#### Comment utiliser `fetch()` pour obtenir des données

* Dans votre application, créez un fichier.
* Importez ensuite `useState()` pour la [gestion d'état dans React.](https://ijaycent.hashnode.dev/simplify-your-react-programming-effortlessly-with-these-8-amazing-hooks)
* Ensuite, importez `[useEffect](https://www.freecodecamp.org/news/react-useeffect-absolute-beginners/)()`, car il fera en sorte que les données de l'API soient rendues.

Voici à quoi devrait ressembler le fichier `Fetch.jsx` :

```javascript

import { useState, useEffect } from 'react';
const Fetch = () => {
  const [photos, setPhotos] = useState([]);
  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/photos')
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log(data);
        setPhotos(data);
      });
  }, []);
  return (
    <div>
      
      {photos.map((photo) => (
        <img key={photo.id} src={photo.url} alt={photo.title} width={100} />
      ))}
    </div>
  );
};
export default Fetch;
```

À l'intérieur de `useEffect()`, nous récupérons nos données en envoyant une requête avec la clé API. La réponse revient en JSON (JavaScript Object Notation).

Dans l'instruction de retour, nous traitons les photos reçues en utilisant une fonction [`map()`](https://www.w3schools.com/jsref/jsref_map.asp) pour itérer à travers chaque élément.

Dans notre scénario spécifique, nous ne sommes intéressés que par les photos. Nous les rendons dans le navigateur en les affichant dans le fichier principal de l'application, ou racine. Le fichier principal pourrait être `App.jsx` ou `Index.js`.

Voici à quoi ressemble le fichier `App.jsx` :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-38.png)
_La racine de l'application_

Et voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-39.png)
_utilisation de fetch()_

### 3. Utiliser la bibliothèque `React Query`

`React Query`, également connu sous le nom de `TanStack Query`, est utile pour gérer les données dans les applications React. La différence entre les deux noms est la version.

L'utilisation de React Query est facile et rend la gestion des données dans votre application presque automatique, comme si elle s'occupait des choses pour vous. Par exemple, la récupération, la mise en cache, la synchronisation et la mise à jour des états du serveur dans vos applications.

#### Avantages de la méthode `React Query`

1. Les données récupérées à partir des API sont mises en cache par `React Query`. Vous pouvez récupérer les mêmes données du cache à nouveau. Cela gagne du temps en évitant une nouvelle requête réseau.
2. Le programme peut automatiquement re-récupérer les données lorsque des conditions spécifiques sont remplies. Ces conditions incluent le regain de focus ou l'écoulement d'un temps défini.
3. `React Query` propose des mises à jour optimistes qui peuvent mettre à jour l'interface utilisateur. Il montre le résultat attendu d'une mutation sans confirmation du serveur. Une expérience utilisateur plus fluide est ainsi obtenue.
4. Il est conçu pour fonctionner avec React, en utilisant son architecture basée sur les composants pour permettre une intégration fluide.
5. `React Query` inclut des DevTools qui offrent des aperçus sur l'état des requêtes, des mutations et du cache. Ces outils aident au débogage et à l'optimisation des performances.

#### Comment utiliser `React Query` pour obtenir des données

Pour commencer, utilisez cette commande pour installer la bibliothèque React-Query (TanStack Query) dans votre application :

```js
npm i @tanstack/react-query
```

Pour faire fonctionner les choses, utilisez `QueryClientProvider` de `@tanstack/react-query`.

Enveloppez votre application, qui est le composant `Main.jsx`, avec celui-ci et passez `queryClient` comme prop. Il provient automatiquement du `QueryClient` initialisé.

Voici à quoi devrait ressembler le fichier [`Main.jsx`](https://www.freecodecamp.org/news/p/2cdb9f65-0c70-4a9c-832b-b073c0a83856/Main.jsx) :

```javascript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>
)
```

Maintenant que nous avons fait cela, nous pouvons récupérer les données :

* Dans votre application, créez un fichier.
* Importez le hook de `@tanstack/react-query` en haut de votre fichier :

```js
import { useQuery } from '@tanstack/react-query';
```

* Le hook `useQuery` est défini avec deux paramètres cruciaux sous forme d'objet. Ces paramètres sont `queryFn` et `queryKey`.
* `queryFn` gère la récupération des données depuis le point de terminaison.
* `queryKey` sert d'identifiant unique pour les données obtenues.

Comme mentionné précédemment, `React Query` simplifie et gère les états de chargement et les erreurs. Vous n'avez pas besoin d'un hook `useState()` séparé.

```javascript
import { useQuery } from '@tanstack/react-query';
const Query = () => {
  const { data: comments, isLoading, error } = useQuery({
    queryFn: () =>
      fetch('https://jsonplaceholder.typicode.com/comments?_limit=10').then(
        (res) => res.json()
      ),
    queryKey: ['comments'],
  });
  
  // Afficher un message de chargement pendant la récupération des données
  if (isLoading) {
    return <h2>Chargement...</h2>;
  }
  
  // pour gérer l'erreur
  if (error) {
    return <div className="error">Erreur : erreur lors de la récupération</div>
  }
  
  return (
    <div>
      <h1 className='title'>Adresses e-mail des utilisateurs</h1>
      {comments.map((comment) => (
        <h2 key={comment.id} className="users">
          {comment.id}.  
            {comment.email}
        </h2>
      ))}
    </div>
  );
};
export default Query;
```

Voici le résultat :

![Le résultat du point de terminaison](https://www.freecodecamp.org/news/content/images/2023/12/chrome_bj4mya9YSt-1.gif)
_Le résultat du point de terminaison_

  
Comme mentionné précédemment, `useQuery()` gère les états de chargement et d'erreur tant qu'il est défini.

Lorsque votre service internet est mauvais, le navigateur peut afficher ces conditions car il n'a pas pu obtenir les données.

Voici un exemple :

![État de chargement et d'erreur](https://www.freecodecamp.org/news/content/images/2023/12/chrome_iPqmAfOUXF.gif)
_État de chargement et d'erreur_

### 4. Utiliser la bibliothèque `Axios`

Axios est un package de bibliothèque tierce que nous pouvons ajouter à notre programme pour récupérer des informations à partir d'une API. Parce qu'Axios est utilisé à la fois dans les navigateurs web et dans le JavaScript côté serveur, il est utile pour un large éventail de tâches.

#### Avantages de la bibliothèque `Axios`

1. Axios est simple et facile à comprendre. C'est un moyen clair et direct d'obtenir des données d'une API.
2. Il est conçu pour bien fonctionner dans la plupart des navigateurs web récents.
3. Vous n'avez pas besoin d'ajouter quoi que ce soit de plus à votre code pour utiliser Axios. Il est prêt à l'emploi en tant que partie de JavaScript.

#### Comment utiliser la bibliothèque Axios pour obtenir des données

* Dans votre application, créez un fichier.
* Installez le package [`Axios`](https://www.npmjs.com/package/axios) dans votre application comme ceci :

```js
npm i axios
```

* Importez la bibliothèque `Axios` dans votre application.
* Importez `useState()`, qui [permet la gestion d'état dans React.](https://ijaycent.hashnode.dev/simplify-your-react-programming-effortlessly-with-these-8-amazing-hooks)
* Importez ensuite `[useEffect](https://www.freecodecamp.org/news/react-useeffect-absolute-beginners/)()` qui facilite le rendu des données de l'API.

Voici à quoi devrait ressembler le fichier [`Axios.jsx`](https://www.freecodecamp.org/news/p/2cdb9f65-0c70-4a9c-832b-b073c0a83856/Axios.jsx) :

```javascript
import { useEffect, useState } from 'react'
import axios from 'axios'
const Axios = () => {
  const [meals, setMeals] = useState([])
  useEffect(() => {
    axios.get('https://www.themealdb.com/api/json/v1/1/random.php')
      .then((res) => {
        setMeals(res.data.meals);
      })
  }, [])
  
  return (
    <div>
      {meals.map((meal) => (
      <img key={meal.idMeal} src={meal.strMealThumb} alt={meal.strMeal} width={400}/>
      ))}
    </div>
  )
}
```

À l'intérieur de `useEffect()`, nous récupérons nos données en envoyant une requête avec la clé API. La réponse revient en JSON (JavaScript Object Notation).

Nous utilisons une fonction `map()` dans l'instruction de retour. La fonction `map()` nous aide à traiter les repas. Elle itère à travers chaque information.

Dans notre scénario spécifique, nous ne sommes intéressés que par les images de chaque repas.

Pour les afficher dans le navigateur, nous les rendons à la racine de l'application, qui pourrait être `App.jsx` ou `Index.js`.

Voici le résultat :

![code](https://www.freecodecamp.org/news/content/images/2023/12/chrome_NB3f9HtpPL.gif)
_utilisation de la bibliothèque axios (Résultat)_

### 5. Utiliser le hook personnalisé `useFetch` de react-fetch-hook

Un hook personnalisé dans React est une fonction JavaScript. Il est réutilisable et exploite les hooks intégrés de React. Le but est d'encapsuler et de partager la logique entre plusieurs composants. Cela favorise la modularité et la maintenabilité du code.

Un hook personnalisé nous permet de réutiliser la logique de récupération dans divers composants de notre application.

Dans React, les hooks personnalisés sont souvent nommés selon une convention, telle que `useFetch`. Typiquement, tout hook personnalisé suit un modèle de nommage qui commence par le mot-clé `use`.

#### Avantages d'un hook personnalisé

1. Les hooks personnalisés facilitent la réutilisation de la logique entre plusieurs composants.
2. Les hooks personnalisés rendent le code lisible, concis et maintenable en extrayant la logique complexe.
3. Les hooks personnalisés vous permettent de tester le code indépendamment, en vous assurant qu'ils fonctionnent comme prévu avant de les utiliser dans des composants.
4. Les hooks personnalisés vous permettent de construire des fonctionnalités plus importantes avec moins de code. Ils évitent la complexité dans votre code principal.

#### Comment obtenir des données en utilisant un hook personnalisé

* Ouvrez le terminal dans votre application.
* Tapez cette commande pour installer le package requis.

```js
npm install react-fetch-hook

```

* Une fois l'installation terminée, accédez au début du fichier de votre application. Ajoutez la ligne suivante pour importer le hook `useFetch` :

```js
import useFetch from "react-fetch-hook";
```

Maintenant, vous pouvez utiliser le hook `useFetch` pour interagir avec une API.

1. Créez des variables pour suivre les erreurs, les états de chargement et les données en utilisant la déstructuration.
2. Dans votre application, effectuez des appels API en utilisant le hook `useFetch`. Mettez à jour les variables.

Exemple de code :

```javascript
import useFetch from "react-fetch-hook";

const UseFetch = () => {
  const { data: posts, isLoading, error } = useFetch('https://jsonplaceholder.typicode.com/posts');

  // Afficher un message de chargement pendant la récupération des données
  if (isLoading) {
    return <h2>Chargement...</h2>;
  }

  // Gérer l'erreur
  if (error) {
    return <div className="error">Erreur : erreur lors de la récupération</div>;
  }

  return (
    <div>
      <h1 className='title'>Articles des utilisateurs</h1>
      {posts.map((post) => (
        <div key={post.id} className="card">
          <h2 className='users'>{post.title}</h2>
          <p>{post.body}</p>
        </div>
      ))}
    </div>
  );
};

```

Voici le résultat :

![Données appelées en utilisant le hook personnalisé](https://www.freecodecamp.org/news/content/images/2023/12/chrome_Rx7VMtOqLZ.gif)
_Données appelées en utilisant le hook personnalisé_

## 

## Conclusion

Cet article traite des différentes manières et outils pour récupérer des données d'API dans React. Comprendre ces méthodes vous aidera à créer des applications avancées.

L'utilisation de React pour construire des applications dynamiques et obtenir des données à partir d'API est vitale. De nombreuses applications dépendent des données des API, les développeurs doivent donc connaître les meilleures et les plus rapides façons d'obtenir ces données.

Que vous soyez un développeur débutant ou expérimenté, chaque méthode a ses avantages. Ces avantages peuvent améliorer vos compétences en programmation. Ils peuvent également vous aider à créer des applications fiables qui utilisent des données.

Si vous avez trouvé ce tutoriel utile, n'hésitez pas à le partager avec d'autres développeurs. Ils pourraient également le trouver intéressant. Vous pouvez également rester informé de mes derniers projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples) et [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/).

Merci d'avoir lu 💖

### Ressource

* [API publiques que les développeurs peuvent utiliser dans leur projet](https://ijaycent.hashnode.dev/public-apis-developers-can-use-in-their-projects)