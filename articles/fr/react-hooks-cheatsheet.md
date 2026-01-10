---
title: 'React Hooks Cheat Sheet: Les 7 Hooks que vous devez connaître'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-02-08T15:28:32.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/react-hooks-cheatsheet-2021.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: 'React Hooks Cheat Sheet: Les 7 Hooks que vous devez connaître'
seo_desc: 'This new tutorial will show you everything you need to know about React
  Hooks from scratch.

  I''ve put this cheatsheet together to help you become knowledgeable and effective
  with React Hooks as quickly as possible.

  Plus, this tutorial is also an inter...'
---

Ce nouveau tutoriel vous montrera tout ce que vous devez savoir sur les React Hooks à partir de zéro.

**J'ai assemblé cette feuille de triche pour vous aider à devenir compétent et efficace avec les React Hooks le plus rapidement possible.**

De plus, ce tutoriel est également un guide vidéo interactif qui vous montrera des exemples pratiques de l'utilisation de chaque hook en 30 secondes ou moins.

Chaque exemple s'appuie sur le précédent et inclut de nombreux modèles et meilleures pratiques qui vous aideront à construire des applications avec React Hooks pour les années à venir.

## Vous voulez votre propre copie ?

**[Cliquez ici pour télécharger la feuille de triche au format PDF](https://reedbarger.com/resources/react-hooks-2021)** (cela prend 5 secondes).

Voici 3 avantages rapides que vous obtenez lorsque vous téléchargez la version téléchargeable :

* Vous obtiendrez des tonnes de fragments de code copiables pour une réutilisation facile dans vos propres projets.
* C'est un excellent guide de référence pour renforcer vos compétences en tant que développeur React et pour les entretiens d'embauche.
* Vous pouvez prendre, utiliser, imprimer, lire et relire ce guide littéralement n'importe où que vous aimez.

Il y a beaucoup de choses intéressantes à couvrir, alors commençons :

### Table des matières :

1. [Hook useState](#heading-1-usestate-hook)
2. [Hook useEffect](#heading-2-useeffect-hook)
3. [Hook useRef](#heading-3-useref-hook)
4. [Hook useCallback](#heading-4-usecallback-hook)
5. [Hook useMemo](#heading-5-usememo-hook)
6. [Hook useContext](#heading-6-usecontext-hook)
7. [Hook useReducer](#heading-7-usereducer-hook)

## 1. Hook useState

### useState pour créer des variables d'état

Le hook useState nous permet de créer des variables d'état dans un composant de fonction React.

> L'état nous permet d'accéder et de mettre à jour certaines valeurs dans nos composants au fil du temps

Lorsque nous créons une variable d'état, nous devons lui fournir une valeur par défaut (qui peut être de n'importe quel type de données).

Nous obtenons cette variable d'état comme première valeur dans un tableau, que nous pouvons déstructurer et déclarer avec `const`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usestate-min.gif)

### Mettre à jour les variables d'état

useState nous donne également une fonction de setter pour mettre à jour l'état après sa création.

Pour mettre à jour notre variable d'état, nous passons la fonction de setter la nouvelle valeur que nous voulons pour notre état.

> Lorsque vous déclarez votre fonction de setter, dans la plupart des cas, vous la préfixerez avec le mot "set"

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-2-usestate-min.gif)

### Peut être utilisé une ou plusieurs fois

useState peut être utilisé une ou plusieurs fois dans un seul composant.

Parfois, vous voudrez créer plusieurs variables d'état et d'autres fois, vous voudrez peut-être utiliser une seule variable avec un objet (voir ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-3-usestate-min.gif)

### Mettre à jour l'état en fonction de la valeur précédente

Si le nouvel état dépend de l'état précédent, nous pouvons prendre la variable d'état précédente et appliquer les modifications que nous voulons faire.

Par exemple, comme dans l'exemple ci-dessous, ajouter 1 à la valeur actuelle de `years` pour l'incrémenter.

Pour garantir que la mise à jour est effectuée de manière fiable, nous pouvons utiliser une fonction dans la fonction de setter qui nous donne l'état précédent correct.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-4-usestate-min.gif)

### Gérer l'état avec un objet

Vous pouvez utiliser un objet avec useState, ce qui vous permet de gérer des valeurs individuelles sous forme de paires clé-valeur.

Comme le montre l'exemple ci-dessous, lorsque vous mettez à jour l'état avec un objet, vous devez étendre l'état précédent. 

Pourquoi ? Parce que toutes les propriétés autres que celle que vous mettez à jour ne seront pas incluses dans le nouvel état.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-5-usestate-min.gif)

## 2. Hook useEffect

### useEffect pour effectuer des effets de bord

useEffect nous permet d'effectuer des effets de bord dans les composants de fonction.

> Les effets de bord sont lorsque nous devons atteindre le monde extérieur. Comme la récupération de données à partir d'une API ou le travail avec le DOM.

Les effets de bord sont des actions qui peuvent changer l'état de notre composant de manière imprévisible (qui ont causé des 'effets de bord').

useEffect accepte une fonction de rappel (appelée la fonction 'effect'), qui s'exécutera par défaut à chaque fois que le composant est réaffiché.

Dans l'exemple ci-dessous, nous interagissons avec le DOM pour changer les propriétés de style du corps du document :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-useeffect-min.gif)

### Exécuter à nouveau lorsqu'une valeur change

useEffect nous permet d'effectuer des effets de manière conditionnelle avec le tableau de dépendances.

Le tableau de dépendances est le deuxième argument passé à useEffect. 

Si l'une des valeurs du tableau change, la fonction d'effet s'exécute à nouveau.

Si aucune valeur n'est incluse dans le tableau de dépendances, useEffect ne s'exécutera qu'au montage et au démontage du composant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-2-useeffect-min.gif)

### Se désabonner en retournant une fonction

useEffect nous permet de nous désabonner des écouteurs que nous avons pu créer en retournant une fonction à la fin.

Nous voulons nous désabonner de certains événements, comme un écouteur d'événements, car lorsque le composant est démonté (c'est-à-dire que l'utilisateur va à une page différente), React peut tenter de mettre à jour un état qui n'existe plus, provoquant une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-3-useeffect-min.gif)

### Récupérer des données à partir d'une API

useEffect est le hook à utiliser lorsque vous souhaitez faire une requête HTTP (notamment une requête GET lorsque le composant est monté).

Notez que la gestion des promesses avec la syntaxe plus concise `async/await` nécessite la création d'une fonction séparée.

C'est parce que la fonction de rappel d'effet ne peut pas être asynchrone. 

Dans l'exemple ci-dessous, nous résolvons notre promesse (retournée par `fetch`) avec une série de rappels `.then()` pour obtenir nos données.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-4-useeffect-min.gif)

## 3. Hook useRef

### useRef pour référencer les éléments React

Les refs sont un attribut spécial disponible sur tous les composants React. Ils nous permettent de créer une référence à un élément/composant donné lorsque le composant est monté.

useRef nous permet d'utiliser facilement les refs React. Ils sont utiles (comme dans l'exemple ci-dessous) lorsque nous voulons interagir directement avec un élément, par exemple pour effacer sa valeur ou le mettre au focus, comme avec une entrée.

Nous appelons useRef (en haut d'un composant) et attachons la valeur retournée à l'attribut ref de l'élément pour le référencer.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-useref-min.gif)

## 4. Hook useCallback

### useCallback empêche les rappels d'être recréés

useCallback est un hook utilisé pour améliorer les performances de nos composants.

> Les fonctions de rappel sont le nom des fonctions qui sont "rappelées" dans un composant parent.

L'utilisation la plus courante est d'avoir un composant parent avec une variable d'état, mais vous voulez mettre à jour cet état à partir d'un composant enfant. 

Que faites-vous ? Vous passez une fonction de rappel à l'enfant depuis le parent. Cela nous permet de mettre à jour l'état dans le composant parent.

useCallback mémorise nos fonctions de rappel, afin qu'elles ne soient pas recréées à chaque réaffichage. L'utilisation correcte de useCallback peut améliorer les performances de notre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usecallback-min.gif)

## 5. Hook useMemo

### useMemo peut améliorer les opérations coûteuses

useMemo est très similaire à useCallback et aide à améliorer les performances. Mais au lieu d'être pour les rappels, il est pour stocker les résultats d'opérations coûteuses.

> useMemo nous permet de mémoriser, ou de nous souvenir du résultat d'opérations coûteuses lorsqu'elles ont déjà été faites pour certaines entrées.

La mémorisation signifie que si un calcul a déjà été fait avec une entrée donnée, il n'est pas nécessaire de le refaire, car nous avons déjà le résultat stocké de cette opération.

useMemo retourne une valeur à partir du calcul, qui est ensuite stockée dans une variable.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usememo-min.gif)

## 6. Hook useContext

### useContext nous aide à éviter le Prop Drilling

Dans React, nous voulons éviter le problème suivant de création de plusieurs props pour passer des données sur deux niveaux ou plus à partir d'un composant parent.

> Dans certains cas, il est acceptable de passer des props à travers plusieurs composants, mais il est redondant de passer des props à travers des composants qui n'en ont pas besoin.

Le contexte est utile pour passer des props à plusieurs niveaux de composants enfants à partir d'un composant parent et pour partager l'état à travers notre arbre de composants d'application.

Le hook useContext supprime le motif de props de rendu inhabituel qui était requis dans la consommation de React Context auparavant. 

Au lieu de cela, useContext nous donne une fonction simple pour accéder aux données que nous avons fournies sur la prop `value` du Context Provider dans n'importe quel composant enfant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usecontext-min.gif)

## 7. Hook useReducer

### useReducer est (un autre) outil puissant de gestion d'état

useReducer est un hook pour la gestion d'état, beaucoup comme useState, et repose sur une sorte de fonction appelée un réducteur.

> Les réducteurs sont des fonctions simples, prévisibles (pures) qui prennent un objet d'état précédent et un objet d'action et retournent un nouvel objet d'état.

useReducer peut être utilisé de nombreuses manières similaires à useState, mais est plus utile pour gérer l'état à travers plusieurs composants qui peuvent impliquer différentes opérations ou "actions".

Vous aurez besoin d'utiliser useReducer moins que useState dans votre application. Mais il est très utile comme moyen puissant de gérer l'état dans les petites applications, plutôt que d'avoir à utiliser une bibliothèque de gestion d'état tierce comme Redux.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/clip-1-usereducer-min.gif)

## Vous voulez garder ce guide pour référence future ?

**[Téléchargez une version PDF complète de cette feuille de triche ici.](https://reedbarger.com/resources/react-hooks-2021)**

Profitez-en !

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*