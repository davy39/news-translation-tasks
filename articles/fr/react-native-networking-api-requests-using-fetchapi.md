---
title: React Native Networking – Comment effectuer des requêtes API dans React Native
  en utilisant FetchAPI
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2023-01-20T19:35:24.000Z'
originalURL: https://freecodecamp.org/news/react-native-networking-api-requests-using-fetchapi
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-276502--1-.jpg
tags:
- name: api
  slug: api
- name: computer networking
  slug: computer-networking
- name: React Native
  slug: react-native
seo_title: React Native Networking – Comment effectuer des requêtes API dans React
  Native en utilisant FetchAPI
seo_desc: 'APIs, or application program interfaces, are essential mechanisms for businesses
  in all industries. They allow for a secure exchange of data between two different
  systems, such as a web application and a database.

  Think of when you are using a mobile...'
---

Les API, ou interfaces de programmation d'applications, sont des mécanismes essentiels pour les entreprises de tous les secteurs. Elles permettent un échange sécurisé de données entre deux systèmes différents, tels qu'une application web et une base de données.

Imaginez que vous utilisez une application mobile pour commander de la nourriture dans un restaurant. Le menu du restaurant, les prix et les informations de commande pourraient tous être stockés dans une base de données gérée par une application back-end.

Pour permettre à l'application mobile d'accéder aux données, l'application doit effectuer une requête API vers l'application back-end. La requête inclura des informations telles que l'emplacement du restaurant, les éléments du menu et la commande souhaitée.

L'application back-end répondra ensuite avec les informations demandées. L'application mobile peut alors utiliser les données pour créer une interface conviviale pour commander de la nourriture.

Les requêtes API peuvent également être utilisées pour mettre à jour la base de données avec de nouvelles données, offrant un moyen pour l'application de sauvegarder et de stocker de nouvelles informations. Vous pouvez également configurer des événements d'abonnement dans l'application. Par exemple, lorsqu'un abonnement d'un utilisateur est sur le point d'expirer, une requête API est envoyée à un système de notification pour les alerter.

Dans ce tutoriel, vous apprendrez à effectuer des requêtes GET, POST, PUT et DELETE vers des API dans une application React Native en utilisant FetchAPI. Vous pouvez accéder au code complet de ce tutoriel [ici](https://snack.expo.dev/@ubahthebuilder/b61a85).

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin de seulement deux choses :

* Une compréhension de base de React Native

* [Expo Snack](https://snack.expo.dev/)

Expo Snack est un environnement de développement en ligne pour React Native qui vous permet essentiellement d'exécuter des applications React Native dans votre navigateur web. Cela élimine la difficulté de configurer votre environnement React Native local à partir de zéro.

## Installation de l'application

Allez sur [Expo Snack](https://snack.expo.dev/) pour initialiser un nouveau projet React Native, puis allez dans le fichier App.js et effacez le contenu du fichier.

Commencez par importer React, les hooks useState et useEffect de React ainsi que les composants Text, View et StyleSheet de React Native.

```js
import React,{useState, useEffect} from 'react';
import { Text, View, StyleSheet } from 'react-native';
```

Ensuite, définissez une fonction de composant App. À l'intérieur du corps de la fonction, nous définissons l'état des données sur un tableau vide, l'état de chargement sur vrai, puis nous retournons un simple texte "Hello World" pour l'instant.

```js
export default function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  return (
    <View>
      <Text>Hello World</Text>
    </View>
  );
}
```

Plus tard, lorsque nous récupérerons les données de l'API JSONPlaceholder (voir la section suivante), nous remplirons l'état des données avec celles-ci et rendrons les données du composant App sous forme de texte.

## L'API avec laquelle nous allons travailler

L'API à partir de laquelle nous allons récupérer nos données est [JSONPlaceholder](https://jsonplaceholder.typicode.com/). Il s'agit d'une API fictive gratuite à des fins de test et de prototypage.

L'API est livrée avec 6 ressources courantes que vous pouvez lire, modifier, mettre à jour ou supprimer en effectuant des requêtes API.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/https___jsonplaceholder.typicode.com_posts-1.png align="left")

*Tableau de 100 objets de publication*

Ici, chaque publication est un objet avec quatre propriétés : userId, id, title et body. Il y a 100 objets dans le tableau.

Vous pouvez :

* créer une nouvelle publication en effectuant une requête POST vers cette API (c'est-à-dire ajouter un nouvel objet)

* lire une publication spécifique en effectuant une requête GET vers cette API (c'est-à-dire lire un objet)

* mettre à jour une publication existante en effectuant une requête PUT vers cette API (c'est-à-dire modifier un objet)

* supprimer une publication existante en effectuant une requête DELETE vers cette API (c'est-à-dire supprimer un objet)

Commençons par effectuer des requêtes GET dans notre application React Native.

## Comment effectuer une requête GET dans React Native

Une requête API GET est un type de requête API utilisé pour récupérer des données à partir d'un serveur. La requête est envoyée via une méthode HTTP GET et les données sont retournées sous la forme d'un objet JSON ou XML.

Effectuons une requête GET dans notre application React Native. Tout d'abord, stockez l'URL à laquelle vous souhaitez effectuer la requête dans une variable (collez ce code sous la déclaration des variables d'état) :

```js
const url = "https://jsonplaceholder.typicode.com/posts"
```

Ensuite, utilisez la méthode fetch pour exécuter la requête API vers l'URL. Enveloppez le fetch à l'intérieur de useEffect (ce hook nous permet d'effectuer des effets secondaires dans notre code, par exemple des appels API) :

```js
useEffect(() => {
  fetch(url)
    .then((resp) => resp.json())
    .then((json) => setData(json))
    .catch((error) => console.error(error))
    .finally(() => setLoading(false));
}, []);
```

Alors, que se passe-t-il ici à l'intérieur de `useEffect` ? Tout d'abord, nous effectuons un appel GET à l'URL. Une fois les données retournées, nous les analysons en JSON avec `resp.json()`, et dans le bloc `then` suivant, nous appelons `setData` pour mettre à jour l'état avec le post.

En cas d'erreur, la méthode `catch` s'exécutera (ce qui enregistre l'erreur dans la console). Enfin, nous définissons l'état de chargement sur `false`.

Enfin, nous rendons le post obtenu à partir de l'API :

```js
<View style={styles.container}>
  {loading ? (
    <Text>Chargement...</Text>
  ) : (
    data.map((post) => {
      return (
        <View>
          <Text style={styles.title}>{post.title}</Text>
          <Text>{post.body}</Text>
        </View>
      );
    })
  )}
</View>;
```

Ainsi, si la requête API est encore en cours, nous affichons le texte "Chargement" sur notre application. Une fois les données récupérées, nous parcourons le tableau et rendons le titre et le texte de chaque post.

Pour le styliser un peu, collez la feuille de style suivante sous App :

```js
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    backgroundColor: "#ecf0f1",
    padding: 8,
  },
  title: {
    fontSize: 30,
    fontWeight: "bold",
  },
});
```

Voici le résultat lorsque les posts sont retournés par l'API.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/vigorous-carrot---Snack.png align="left")

*Apparence finale*

Comme vous pouvez le voir, nous avons réussi à récupérer la liste des posts à partir de l'API et à rendre chacun d'eux dans notre application React Native.

Maintenant, si vous souhaitez récupérer une ressource spécifique (comme un post spécifique) plutôt qu'une collection de ressources comme une liste de posts, tout ce que vous avez à faire est d'ajouter l'ID de la ressource à l'URL comme ceci :

```js
const url = "https://jsonplaceholder.typicode.com/posts/1"
```

Si nous effectuons une requête GET vers le point de terminaison de l'API ci-dessus, le serveur ne nous renverra que le post avec un ID de 1.

Passons à d'autres types de requêtes.

## Comment effectuer une requête POST dans React Native

Une requête API POST est un type de requête API utilisé pour créer ou mettre à jour une ressource sur un serveur web.

Elle envoie des données au serveur sous la forme d'un corps de requête qui contient généralement des informations telles que le titre, la description et d'autres détails pertinents. Si les données sont acceptées, le serveur répond avec un code de succès et la ressource est créée ou mise à jour.

Lors de l'envoi d'une requête POST avec FetchAPI, vous devez spécifier la méthode comme 'POST'. Voici un exemple de POST vers le serveur fictif depuis notre application React Native :

```js
fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    userId: 55,
    id: 101,
    title: "Titre du post",
    body: "Corps du post",
  }),
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log(JSON.stringify(responseData));
  })
  .done();
```

La valeur de la propriété body doit toujours être un objet JSON avec des valeurs de chaîne JSON (d'où l'appel à `JSON.stringify`).

Une fois que le serveur a terminé le traitement de la requête, il envoie une réponse pour vous indiquer si la ressource a été créée sur le serveur ou non (et pourquoi elle a échoué).

## Comment effectuer une requête PUT dans React Native

Si une requête POST est utilisée pour créer une nouvelle ressource sur un serveur, une requête PUT est utilisée pour mettre à jour une ressource spécifique sur ce serveur.

Dans une requête PUT, vous devez spécifier l'ID de la ressource que vous souhaitez mettre à jour sur le serveur ainsi que les nouvelles valeurs. Voici un exemple qui met à jour le titre et le corps du premier post sur le serveur :

```js
fetch("https://jsonplaceholder.typicode.com/posts/1", {
  method: "PUT",
  body: JSON.stringify({
    userId: 55,
    id: 101,
    title: "Nouveau titre du post",
    body: "Nouveau corps du post",
  }),
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log(JSON.stringify(responseData));
  })
  .done();
```

Similaire à une requête POST, le serveur envoie une réponse pour vous indiquer si la ressource a été mise à jour sur le serveur ou non (et pourquoi elle a échoué).

## Comment effectuer une requête DELETE dans React Native

Comme vous l'avez peut-être deviné, une requête DELETE est utilisée pour supprimer une ressource spécifique d'un serveur.

Dans une requête DELETE, vous spécifiez uniquement l'ID de la ressource que vous souhaitez supprimer sur le serveur :

```js
fetch("https://jsonplaceholder.typicode.com/posts/1", {
  method: "DELETE",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log(JSON.stringify(responseData));
  })
  .done();
```

Une fois que le serveur a terminé le traitement de la requête, il envoie une réponse pour vous indiquer si la ressource a été supprimée sur le serveur ou non (et pourquoi elle a échoué).

## Comment intégrer d'autres API tierces à React Native

Les API tierces sont créées et maintenues par des organisations autres que le développeur principal de l'application. Elles sont utilisées pour fournir un accès à certaines sources de données externes afin que les développeurs puissent les incorporer dans leurs applications.

Avec l'utilisation généralisée de React Native pour le développement d'applications mobiles, les API tierces peuvent être facilement intégrées pour créer des applications puissantes et riches en fonctionnalités.

L'un des principaux avantages de l'utilisation des API tierces est qu'elles sont souvent mises à jour fréquemment, ce qui signifie que les développeurs peuvent rapidement accéder aux dernières fonctionnalités et sources de données. Cela peut être particulièrement utile lors du développement d'applications mobiles, car elles nécessitent souvent un accès aux dernières fonctionnalités et sources de données.

De plus, vous pouvez également utiliser des API tierces pour ajouter des fonctionnalités qui sont difficiles ou impossibles à créer en interne, car cela nécessite des ressources humaines, financières et temporelles substantielles.

Par exemple, il existe des API complexes pour la [connexion Facebook](https://developers.facebook.com/docs/facebook-login/web/), le [traitement des paiements](https://stripe.com/docs/api), le [rapport météo](https://openweathermap.org/api), l'[intégration de l'infrastructure d'achats intégrés](https://adapty.io/blog/react-native-in-app-purchases-implementation-tutorial), et ainsi de suite.

## Conclusion

Ce tutoriel vous a guidé à travers les étapes de l'envoi de requêtes API dans React Native en utilisant la bibliothèque Fetch intégrée.

J'espère que vous avez apprécié cela autant que j'ai aimé l'écrire. Passez une excellente semaine.