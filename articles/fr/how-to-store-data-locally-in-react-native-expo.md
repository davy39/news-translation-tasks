---
title: Comment stocker des données localement dans React Native Expo
subtitle: ''
author: John Caleb
co_authors: []
series: null
date: '2024-05-13T11:42:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-store-data-locally-in-react-native-expo
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/local-storage-in--react-native-expo--1-.png
tags:
- name: localstorage
  slug: localstorage
- name: React Native
  slug: react-native
seo_title: Comment stocker des données localement dans React Native Expo
seo_desc: "React Native has grown in popularity as a mobile application development\
  \ tool because of its ability to create cross-platform applications using familiar\
  \ JavaScript and React principles. \nWhen building mobile applications, one common\
  \ requirement is t..."
---

React Native a gagné en popularité en tant qu'outil de développement d'applications mobiles grâce à sa capacité à créer des applications multiplateformes en utilisant des principes JavaScript et React familiers. 

Lors de la création d'applications mobiles, une exigence courante est la capacité à sauvegarder des données localement sur l'appareil. C'est là que le stockage local entre en jeu. [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), fourni par React Native Expo, est une solution simple mais puissante pour sauvegarder des données localement dans vos applications React Native Expo.

Dans ce tutoriel, nous allons discuter des fondamentaux du stockage local, présenter Async Storage et démontrer comment l'intégrer correctement dans les projets React Native Expo.

## Table des matières

* [Prérequis](#heading-prerequis)
* [Qu'est-ce que le stockage local ?](#heading-quest-ce-que-le-stockage-local)
* [Qu'est-ce qu'Async Storage ?](#heading-quest-ce-que-async-storage)
* [Comment commencer avec Async Storage](#heading-comment-commencer-avec-async-storage)
* [Comprendre les méthodes d'Async Storage](#heading-comprendre-les-methodes-dasync-storage)
* [Utilisation avancée et bonnes pratiques](#heading-utilisation-avancee-et-bonnes-pratiques)
* [Conclusion](#heading-conclusion)

## Prérequis

* Connaissance de React Native et JavaScript.
* Node.js et npm (ou yarn) installés.

## Qu'est-ce que le stockage local ?

Le stockage local est un composant essentiel du développement d'applications mobiles, permettant aux développeurs de stocker des données sur l'appareil de l'utilisateur. Contrairement à d'autres options de stockage telles que les bases de données, le stockage local utilise une technique de stockage simple basée sur des paires clé-valeur.

Les développeurs peuvent l'utiliser pour sauvegarder de petites quantités de données qui restent stockées même lorsque le programme est fermé ou que l'appareil est redémarré. Cela en fait une solution idéale pour stocker les préférences utilisateur, les jetons d'authentification et d'autres informations importantes.

Le stockage local est essentiel pour améliorer la vitesse des applications car il élimine le besoin de récupérer des données depuis des serveurs distants régulièrement.

## Qu'est-ce qu'Async Storage ?

Async Storage est un système de stockage clé-valeur fourni par React Native Expo qui permet de gérer le stockage local dans les applications mobiles. Il offre un système de stockage clé-valeur simple qui permet aux développeurs de stocker et de récupérer des données de manière asynchrone. 

Contrairement aux méthodes de stockage synchrones, Async Storage permet de sauvegarder et de récupérer des données sans interrompre le thread principal, ce qui entraîne une expérience utilisateur plus fluide.

## Comment commencer avec Async Storage

Pour utiliser Async Storage dans votre projet React Native Expo, assurez-vous qu'Expo est installé. Si vous n'avez pas encore configuré un projet React Native Expo, vous pouvez le faire en installant Expo CLI :

```bash
$ npm install -g expo-cli
```

Créez un nouveau projet Expo :

```bash
$ expo init MyProject
$ cd MyProject
```

Pour ajouter Async Storage à votre projet, exécutez la commande suivante :

```js
$ expo install @react-native-async-storage/async-storage
```

Le package `@react-native-async-storage/async-storage` est une version maintenue par la communauté d'AsyncStorage. Une fois installé, vous pouvez configurer un fichier pour gérer les méthodes d'AsyncStorage telles que `setItem()`, `updateItem()`, `deleteItem()`, et autres. Ce fichier serait importé chaque fois que vous souhaitez effectuer un appel au stockage local. 

Dans cet exemple, nous allons créer un dossier nommé `utils` à la racine de notre projet, puis créer le fichier `AsyncStorage.js` pour gérer ces méthodes :

![Structure de fichier Async Storage](https://www.freecodecamp.org/news/content/images/2024/05/-4611C08C-3557-460A-A7CC-BFD754BD13F7-.png.jpg)
_Structure de fichier Async Storage_

Dans le fichier `AsyncStorage.js`, vous pouvez définir les méthodes AsyncStorage comme ceci :

```js
// utils/AsyncStorage.js

import AsyncStorage from '@react-native-async-storage/async-storage';

export const setItem = async (key, value) => {
  try {
    await AsyncStorage.setItem(key, JSON.stringify(value));
  } catch (error) {
    console.error('Erreur lors de la définition de l\'élément :', error);
  }
};

export const getItem = async (key) => {
  try {
    const value = await AsyncStorage.getItem(key);
    return value != null ? JSON.parse(value) : null;
  } catch (error) {
    console.error('Erreur lors de la récupération de l\'élément :', error);
    return null;
  }
};

export const removeItem = async (key) => {
  try {
    await AsyncStorage.removeItem(key);
  } catch (error) {
    console.error('Erreur lors de la suppression de l\'élément :', error);
  }
};

export const mergeItem = async (key, value) => {
  try {
    await AsyncStorage.mergeItem(key, JSON.stringify(value));
  } catch (error) {
    console.error('Erreur lors de la fusion de l\'élément :', error);
  }
};

export const clear = async () => {
  try {
    await AsyncStorage.clear();
  } catch (error) {
    console.error('Erreur lors du vidage d\'AsyncStorage :', error);
  }
};

export const getAllKeys = async () => {
  try {
    return await AsyncStorage.getAllKeys();
  } catch (error) {
    console.error('Erreur lors de la récupération de toutes les clés :', error);
    return [];
  }
};

export const getAllItems = async () => {
  try {
    const keys = await AsyncStorage.getAllKeys();
    const items = await AsyncStorage.multiGet(keys);
    return items.reduce((accumulator, [key, value]) => {
      accumulator[key] = JSON.parse(value);
      return accumulator;
    }, {});
  } catch (error) {
    console.error('Erreur lors de la récupération de tous les éléments :', error);
    return {};
  }
};
```

Dans la section suivante, nous allons expliquer et décomposer la signification de ces fonctions AsyncStorage dans le fichier AsyncStorage.js.

## Comprendre les méthodes d'Async Storage

En séparant les fonctions AsyncStorage dans leur propre fichier, vous pouvez les gérer et les réutiliser facilement dans votre projet React Native Expo. Cette approche modulaire améliore la maintenance et la lisibilité du code.

Dans la section précédente, nous avons créé le fichier `AsyncStorage.js` et ajouté plusieurs fonctions. 

Dans les sections suivantes, nous allons parler de ces méthodes et de la manière de les utiliser efficacement.

### `setItem()`

Cette méthode est essentielle pour stocker des données localement sur l'appareil. Elle permet aux développeurs de stocker des paires clé-valeur dans AsyncStorage, où la clé sert d'identifiant unique et la valeur représente les données à stocker.

```js
await AsyncStorage.setItem('username', 'freeCodeCamp');
```

### `getItem()`

La méthode `getItem()` retourne la valeur associée à une clé donnée depuis le stockage local. Elle envoie un paramètre/clé, qui est l'identifiant unique des données demandées. Et elle retourne la valeur associée à la clé fournie, ou null si aucune valeur n'est trouvée pour la clé donnée.

```js
const username = await AsyncStorage.getItem('username');
```

Dans ce scénario, la valeur pour la clé `username` est récupérée depuis le stockage local. Cette valeur obtenue, `freeCodeCamp`, est ensuite placée dans la variable username, la rendant disponible pour une utilisation ultérieure dans l'application.

### `removeItem()`

Cette fonction supprime l'objet avec la clé fournie du stockage local. Elle est utile lorsque vous souhaitez supprimer une donnée spécifique qui n'est plus nécessaire.

```js
await AsyncStorage.removeItem('username');
```

Dans cet exemple, l'objet identifié par la clé `username` est supprimé du stockage local.

### `mergeItem()`

La méthode `mergeItem()` combine la valeur d'une clé existante avec la valeur fournie en entrée. Si la clé n'existe pas, elle fonctionne de manière similaire à `setItem()`, créant une nouvelle paire clé-valeur.

```js
await AsyncStorage.mergeItem('user', JSON.stringify({ name: 'John' }));
```

### `clear()`

La méthode `clear()` supprime tous les éléments du stockage local. Elle est utile lorsque vous souhaitez supprimer toutes les données locales, par exemple lorsque vous vous déconnectez d'un utilisateur ou réinitialisez l'état de l'application.

```js
await AsyncStorage.clear();
```

### `getAllKeys()`

La fonction `getAllKeys()` retourne toutes les clés conservées dans le stockage local. Elle est utile lorsque vous devez parcourir toutes les clés ou effectuer des opérations basées sur les clés dans le stockage local.

```js
const keys = await AsyncStorage.getAllKeys();
```

### `multiGet()`

La fonction `multiGet()` obtient plusieurs paires clé-valeur depuis le stockage local en utilisant un tableau de clés fourni.

```js
const data = await AsyncStorage.multiGet(['username', 'email']);
```

Dans cet exemple, les valeurs pour les clés `username` et `email` sont récupérées depuis le stockage local.

## Utilisation avancée et bonnes pratiques

Bien qu'AsyncStorage offre une interface simple pour le stockage local, il existe plusieurs bonnes pratiques à considérer :

1. **Sérialisation des données** : Lorsque vous stockez des types de données complexes tels que des objets ou des tableaux, n'oubliez pas de les sérialiser en format chaîne en utilisant `JSON.stringify()` avant de les stocker et de les désérialiser en utilisant `JSON.parse()` lors de la récupération.
2. **Gestion des erreurs** : Implémentez une gestion robuste des erreurs pour gérer élégamment les échecs qui peuvent survenir lors des opérations d'Async Storage.
3. **Considérations de sécurité** : Soyez conscient de la sensibilité des données stockées localement et implémentez des mesures de sécurité appropriées telles que le chiffrement pour les informations sensibles.

## Conclusion

En conclusion, l'intégration du stockage local dans vos projets React Native Expo est essentielle pour développer des applications mobiles robustes et réactives. Async Storage simplifie le processus de stockage et de récupération des données sur l'appareil, offrant une expérience utilisateur cohérente et permettant des fonctionnalités hors ligne. 

En suivant les étapes fournies dans cet article, vous pouvez utiliser Async Storage pour améliorer les fonctionnalités de stockage local de vos applications.

N'oubliez pas, si vous avez des questions ou si vous voulez simplement dire bonjour, n'hésitez pas à me contacter sur [X(Twitter)](https://twitter.com/thejohncaleb) ou sur mon [site web](https://thejohncaleb.netlify.app/contact). :)