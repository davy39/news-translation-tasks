---
title: 'Comment récupérer des données dans React : Guide pratique + Exemples'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-12T20:39:03.000Z'
originalURL: https://freecodecamp.org/news/fetch-data-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/how-to-fetch-data-in-react.png
tags:
- name: api
  slug: api
- name: data
  slug: data
- name: React
  slug: react
seo_title: 'Comment récupérer des données dans React : Guide pratique + Exemples'
seo_desc: 'There are many ways to fetch data from an external API in React. But which
  one should you be using for your applications in 2021?

  In this tutorial, we will be reviewing five of the most commonly used patterns to
  fetch data with React by making an HTT...'
---

Il existe de nombreuses façons de récupérer des données depuis une API externe dans React. Mais laquelle devriez-vous utiliser pour vos applications en 2021 ?

Dans ce tutoriel, nous allons passer en revue cinq des méthodes les plus couramment utilisées pour récupérer des données avec React en effectuant une requête HTTP vers une API REST.

Nous allons non seulement couvrir comment récupérer des données, mais aussi comment gérer au mieux les états de chargement et d'erreur lors de la récupération de nos données.

Commençons !

> Pour tous ces exemples, nous allons utiliser un endpoint de l'API populaire JSON Placeholder, mais vous pouvez utiliser votre propre API (comme une API Node avec Express) ou toute autre API publique.

### Vous voulez votre propre copie ?


**[Cliquez ici pour télécharger le guide pratique au format PDF](https://reedbarger.com/resources/react-fetch-data-2021)** (cela prend 5 secondes).

Il contient toutes les informations essentielles ici sous forme de guide PDF pratique.

## 1. Comment récupérer des données dans React en utilisant l'API Fetch

La manière la plus accessible de récupérer des données avec React est d'utiliser l'API Fetch.

L'API Fetch est un outil intégré dans la plupart des navigateurs modernes sur l'objet window (`window.fetch`) et nous permet de faire des requêtes HTTP très facilement en utilisant les promesses JavaScript.

Pour faire une simple requête GET avec fetch, nous devons simplement inclure l'URL de l'endpoint vers lequel nous voulons faire notre requête. Nous voulons faire cette requête une fois que notre composant React est monté.

Pour ce faire, nous faisons notre requête dans le hook useEffect, et nous veillons à fournir un tableau de dépendances vide comme deuxième argument, afin que notre requête ne soit faite qu'une seule fois (en supposant qu'elle ne dépend d'aucune autre donnée dans notre composant).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/clip-1-fetch-min.gif)

Dans le premier callback `.then()`, nous vérifions si la réponse était correcte (`response.ok`). Si c'est le cas, nous retournons notre réponse pour la passer au callback suivant, puis nous la convertissons en données JSON, car c'est le type de données que nous allons recevoir de notre API d'utilisateurs aléatoires.

Si ce n'est pas une réponse correcte, nous supposons qu'il y a eu une erreur lors de la requête. En utilisant fetch, nous devons gérer les erreurs nous-mêmes, donc nous lançons `response` comme une erreur pour qu'elle soit gérée par notre callback `catch`.

Ici, dans notre exemple, nous mettons nos données d'erreur dans l'état avec `setError`. Si une erreur survient, nous retournons le texte "Erreur !".

> Notez que vous pouvez également afficher un message d'erreur à partir de l'objet d'erreur que nous avons mis dans l'état en utilisant `error.message`.

Nous utilisons le callback `.finally()` comme fonction qui est appelée lorsque notre promesse est résolue avec succès ou non. Dans ce callback, nous définissons `loading` sur false, afin que nous ne voyions plus notre texte de chargement.

Au lieu de cela, nous voyons soit nos données sur la page si la requête a été effectuée avec succès, soit qu'il y a eu une erreur lors de la requête.

## 2. Comment récupérer des données dans React en utilisant Axios

La deuxième approche pour faire des requêtes avec React est d'utiliser la bibliothèque `axios`.

Dans cet exemple, nous allons simplement réviser notre exemple Fetch en installant d'abord `axios` en utilisant npm :

```bash
npm install axios
```

Ensuite, nous allons l'importer en haut de notre fichier de composant.

Ce que axios nous permet de faire, c'est d'utiliser la même syntaxe de promesse que fetch, mais au lieu d'utiliser notre premier callback then pour déterminer manuellement si la réponse est correcte et lancer une erreur, axios s'en charge pour nous.

De plus, cela nous permet dans ce premier callback d'obtenir les données JSON à partir de `response.data`.

Ce qui est pratique avec l'utilisation de axios, c'est qu'il a une syntaxe beaucoup plus courte qui nous permet de réduire notre code et il inclut de nombreux outils et fonctionnalités que Fetch n'a pas dans son API.

Toutes ces raisons font qu'il est devenu la bibliothèque HTTP de référence pour les développeurs React.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/clip-2-axios-min.gif)

## 3. Comment récupérer des données dans React en utilisant la syntaxe async / await

Avec ES7, il est devenu possible de résoudre les promesses en utilisant la syntaxe `async / await`.

L'avantage de cela est qu'il nous permet de supprimer nos callbacks `.then()`, `.catch()` et `.finally()` et de simplement obtenir nos données résolues de manière asynchrone comme si nous écrivions du code synchrone sans promesses.

En d'autres termes, nous n'avons pas à nous fier aux callbacks lorsque nous utilisons async / await avec React.

Nous devons être conscients du fait que lorsque nous utilisons `useEffect`, la fonction d'effet (le premier argument) ne peut pas être rendue asynchrone.

Si nous regardons l'erreur de linting que React nous donne [si nous utilisons Create React App](https://reedbarger.com/create-react-app-10-steps) pour construire notre projet, nous serons informés que cette fonction ne peut pas être asynchrone pour éviter les conditions de course.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/clip-3-async-await-min.gif)

En conséquence, au lieu de rendre cette fonction asynchrone, nous pouvons simplement créer une fonction asynchrone séparée dans notre composant, que nous pouvons appeler de manière synchrone. C'est-à-dire, sans le mot-clé `await` avant elle.

Dans cet exemple, nous créons une fonction asynchrone appelée `getData`. En l'appelant de manière synchrone dans useEffect, nous pouvons récupérer nos données comme nous l'attendons.

## 4. Comment récupérer des données dans React en utilisant un Hook React personnalisé (useFetch)

Avec le temps, vous pouvez réaliser qu'il devient un peu fastidieux et chronophage de continuer à écrire le hook useEffect avec tout son code standard dans chaque composant dans lequel vous souhaitez récupérer des données.

Pour réduire notre code réutilisé, nous pouvons utiliser un hook personnalisé comme une abstraction spéciale, que nous pouvons écrire nous-mêmes à partir d'une bibliothèque tierce (comme nous le faisons ici, en utilisant la bibliothèque `react-fetch-hook`).

Un hook personnalisé qui fait notre requête HTTP nous permet de rendre nos composants beaucoup plus concis. Tout ce que nous avons à faire est d'appeler notre hook en haut de notre composant.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/clip-4-usefetch-min.gif)

Dans ce cas, nous obtenons toutes les données, le chargement et l'état d'erreur dont nous avons besoin pour pouvoir utiliser la même structure pour notre composant qu'auparavant, mais sans avoir à utiliser `useEffect`. De plus, nous n'avons plus besoin d'écrire de manière impérative comment résoudre notre promesse à partir de notre requête GET chaque fois que nous voulons faire une requête.

## 5. Comment récupérer des données dans React en utilisant la bibliothèque React Query

L'utilisation de hooks personnalisés est une excellente approche pour écrire des requêtes HTTP beaucoup plus concises afin d'obtenir nos données et tous leurs états associés. Mais une bibliothèque qui élève vraiment la récupération de données avec des hooks à un niveau supérieur est React Query.

React Query ne nous permet pas seulement d'utiliser des hooks personnalisés que nous pouvons réutiliser dans nos composants de manière concise, mais il nous offre également une multitude d'outils de gestion d'état pour pouvoir contrôler quand, comment et à quelle fréquence nos données sont récupérées.

En particulier, React Query nous donne un cache, que vous pouvez voir ci-dessous à travers les React Query Devtools. Cela nous permet de gérer facilement les requêtes que nous avons faites selon une clé que nous spécifions pour chaque requête.

Pour les requêtes ci-dessous, notre requête pour nos données d'utilisateurs aléatoires est identifiée par la chaîne 'random-user' (fournie comme premier argument à `useQuery`).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/clip-5-react-query-min.gif)

En référençant cette clé, nous pouvons faire des choses puissantes telles que refetch, valider ou réinitialiser nos différentes requêtes.

> Si nous nous appuyons sur notre solution de hook personnalisé ou useEffect, nous allons refetch nos données chaque fois que notre composant est monté. Dans la plupart des cas, cela est inutile. Si notre état externe n'a pas changé, nous ne devrions idéalement pas avoir à montrer l'état de chargement chaque fois que nous affichons notre composant.

React Query améliore considérablement notre expérience utilisateur en essayant de servir nos données à partir de son cache d'abord, puis en mettant à jour les données en arrière-plan pour afficher les changements si l'état de notre API a changé.

Il nous donne également un arsenal d'outils puissants pour mieux gérer nos requêtes en fonction de la manière dont nos données changent à travers notre requête.

Par exemple, si notre application nous permettait d'ajouter un utilisateur différent, nous pourrions vouloir refetch cette requête, une fois l'utilisateur ajouté. Si nous savions que la requête était modifiée très fréquemment, nous pourrions vouloir spécifier qu'elle devrait être actualisée toutes les minutes ou lorsque l'utilisateur se concentre sur son onglet de fenêtre.

En bref, React Query est la solution de référence non seulement pour faire des requêtes de manière concise, mais aussi pour gérer efficacement et efficacement les données qui sont retournées pour nos requêtes HTTP à travers les composants de notre application.

## Vous voulez garder ce guide pour référence future ?


**[Cliquez ici pour télécharger le guide pratique au format PDF](https://reedbarger.com/resources/react-fetch-data-2021)**.

Voici 3 avantages rapides que vous obtenez lorsque vous téléchargez la version PDF :

* Vous obtiendrez des tonnes de snippets de code copiables pour une réutilisation facile dans vos propres projets.
* C'est un excellent guide de référence pour renforcer vos compétences en tant que développeur React et pour les entretiens d'embauche.
* Vous pouvez prendre, utiliser, imprimer, lire et relire ce guide littéralement où vous le souhaitez.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*