---
title: 5 bibliothèques React que chaque projet devrait utiliser en 2021
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-07-09T20:06:31.000Z'
originalURL: https://freecodecamp.org/news/5-react-libraries-every-project-needs
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/5-libraries-every-react-project-needs.png
tags:
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Web Development
  slug: web-development
seo_title: 5 bibliothèques React que chaque projet devrait utiliser en 2021
seo_desc: "There are literally 100s of great React libraries to choose from, but which\
  \ libraries do you need most for your React projects? \nIn this article, we're going\
  \ to break down five libraries you need for your React projects.\nEach of them will\
  \ cover virtu..."
---

Il existe littéralement des centaines de bibliothèques React formidables parmi lesquelles choisir, mais quelles bibliothèques avez-vous le plus besoin pour vos projets React ?

Dans cet article, nous allons décomposer cinq bibliothèques dont vous avez besoin pour vos projets React.

Chacune d'elles couvrira pratiquement tous les outils majeurs dont vous avez besoin, et nous aborderons également celles qui sont les meilleures à choisir en 2021 et au-delà.

Plongeons directement dans le vif du sujet !

## 1. Un Create-React-App plus rapide

Si vous souhaitez créer un projet React, vous utilisez probablement un outil comme Create-React-App.

Bien que Create-React-App reste un outil incroyable et vous permet de créer un projet React en exécutant une seule commande, il existe un nouveau concurrent que vous devriez connaître appelé **Vite**.

Create-React-App utilise Webpack sous le capot pour construire notre code React pour le développement. Mais des outils de construction ont émergé qui rivalisent avec Webpack en termes de vitesse.

Vite est l'un de ces outils de construction qui utilise un bundler plus rapide appelé esbuild. En bref, il utilise les modules ES natifs du navigateur pour une expérience de développement plus rapide.

_À quel point Vite est-il plus rapide ?_ Voyez par vous-même !

Voici une comparaison rapide du démarrage d'un projet Vite (à droite) par rapport à un projet Create-React-App (à gauche).

<video controls width="800">
    <source src="https://reedbarger.nyc3.digitaloceanspaces.com/vite-react.mp4" type="video/mp4">
    Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

Vite est beaucoup plus rapide que Create-React-App lors de l'exécution de React en développement.

Si vous êtes parfois agacé par le temps que Create-React-App peut prendre pour démarrer, assurez-vous de vérifier Vite.

En plus de cela, je vous recommande vivement l'outil **Create-Next-App**.

Cela nous permet de créer un projet Next.js très rapidement. Et oui, Next.js est un framework, mais c'est un framework React qui nécessite beaucoup moins de dépendances. En fait, il ne nécessite que les dépendances React, React DOM et Next.

_Assurez-vous de vérifier **Vite** et **Create Next App** lors de la création de votre prochain projet React._

## 2. Une (meilleure) bibliothèque de récupération de données

En ce qui concerne pratiquement toute application React, nous devons gérer un certain état du serveur.

Cela signifie que nous récupérons des données depuis un serveur externe (comme une API) et que nous intégrons ces données dans notre application, qui sont ensuite combinées avec l'état local que nous avons dans les composants de notre application.

De nombreux développeurs React, quel que soit leur niveau de compétence, peuvent avoir du mal à comprendre comment gérer l'état du serveur avec leur état local. La plupart des développeurs recourent à une bibliothèque comme Redux comme solution.

Au cours de l'année écoulée, quelques bibliothèques ont émergé qui facilitent grandement la gestion de l'état du serveur dans nos composants React. Ce sont **React Query** et **SWR**.

Elles nous aident à récupérer des données en nous fournissant des hooks personnalisés très utiles. Mais ce qui est le plus important à leur sujet, c'est qu'elles ont leur propre cache interne.

Ce cache intégré nous permet d'intégrer très facilement des données externes avec notre application. Nous attribuons à chaque requête une clé personnalisée. Pour lire ou mettre à jour les données que nous avons récupérées, nous devons simplement référencer cette clé !

Voici un exemple simple de la façon dont vous pouvez utiliser React Query. Nous récupérons les données des posts depuis une API, dont nous attribuons la valeur à la clé personnalisée "posts".

![Image](https://www.freecodecamp.org/news/content/images/2021/07/react-query.gif)

En plus d'améliorer notre gestion d'état, la récupération de données est beaucoup plus facile. Elles incluent de nombreux outils qui nous permettent de faire des choses comme relancer des requêtes, créer des requêtes paginées, des requêtes infinies, et bien plus encore.

En bref, si vous récupérez des données dans votre application React à travers plusieurs composants, utilisez définitivement l'une de ces nouvelles bibliothèques de récupération de données.

_Si vous cherchez la bibliothèque de récupération de données la plus approfondie et sophistiquée, utilisez **React Query**. **SWR** est également un excellent choix, bien qu'avec une liste d'outils légèrement plus petite._

## 3. Une bibliothèque de gestion d'état ultra-simple

En ce qui concerne la gestion de l'état global de l'application, Redux a toujours été le choix de prédilection.

Il a aidé les développeurs React à séparer les valeurs d'état en une seule valeur d'objet partagé, qui peut être lue et mise à jour dans n'importe quel composant de notre application.

Cependant, Redux vient avec un certain bagage conceptuel. Pour configurer correctement Redux et gérer notre état, nous devons comprendre et écrire des actions, des réducteurs et des sélecteurs séparés.

Il existe de nouveaux concurrents à Redux qui cherchent à nous offrir pratiquement tous les avantages de la bibliothèque sans aucune des difficultés. Ce sont les bibliothèques **Zustand** et **Jotai**.

Elles sont toutes deux très similaires, et ce qui est puissant à leur sujet, c'est qu'elles ont été créées avec une approche basée sur les hooks pour travailler avec l'état. Cela signifie que, une fois que vous avez créé votre store, vous pouvez lire n'importe quelle de ses valeurs en l'appelant comme un hook.

Voici un exemple rapide de la façon de créer et d'utiliser un store Zustand comme un hook pour créer une application de compteur simple.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/zustand.gif)

Zustand et Jotai simplifient la gestion d'état grâce au fait que vous n'avez pas besoin de séparer votre store en actions, réducteurs et sélecteurs.

Si vous souhaitez mettre à jour l'état, écrivez une fonction dans votre store pour le faire et utilisez-la dans votre composant. Si vous souhaitez sélectionner une partie de votre état, utilisez votre store comme un hook et récupérez la propriété de l'objet d'état que vous souhaitez. C'est aussi simple que cela !

De plus, vous n'avez pas besoin de bibliothèques supplémentaires pour effectuer des opérations asynchrones (contrairement à Redux, qui nécessite Redux Thunk ou Redux Saga).

Enfin, vous n'avez pas besoin d'envelopper tout votre arbre de composants avec un fournisseur de contexte, donc il n'y a pratiquement aucune configuration requise, autre que la création de votre store et son utilisation dans vos composants.

_En bref, si vous avez des difficultés à comprendre Redux ou si vous voulez plus de liberté dans votre gestion d'état, vérifiez **Zustand** ou **Jotai**._

## 4. Une bibliothèque de composants puissante

React a été conçu pour créer des interfaces utilisateur impressionnantes. Par conséquent, nous avons besoin de bibliothèques qui nous aident à atteindre cet objectif.

Il existe des tonnes de bibliothèques de composants qui nous fournissent des composants bien conçus et personnalisés, prêts à l'emploi. Cependant, avec toute cette diversité, lesquelles choisir ?

Si vous souhaitez pouvoir construire des applications qui ont une belle apparence et sont tout aussi fonctionnelles, vous pouvez consulter des bibliothèques extensives et bien maintenues comme **Ant Design**, **Material UI** et **Chakra UI**.

Toutes ces bibliothèques ont une tonne de composants et même des bibliothèques d'icônes dédiées. Mais ce qui est peut-être le plus important à leur sujet, c'est qu'elles ont une syntaxe intuitive qui nous permet de construire des composants attrayants plus facilement.

Voici un exemple rapide de construction d'une interface utilisateur simple avec Ant Design.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/antd.gif)

La plupart des développeurs choisissent des bibliothèques de composants pour leur apparence et les composants qu'elles proposent, mais les meilleures bibliothèques incluent également des outils supplémentaires qui rendent nos applications plus fonctionnelles.

Voici un exemple de hook personnalisé (`useClipboard`) de Chakra UI qui nous permet de copier du texte dans le presse-papiers de nos utilisateurs.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-09-at-2.27.58-PM.png)

Je les ai sélectionnés non seulement parce que je les trouve visuellement attrayants, mais aussi parce qu'ils ont une grande variété de composants qui conviendront à pratiquement tous les cas d'utilisation que vous avez.

La pire chose qui puisse arriver est que vous ayez une bibliothèque de composants une fois que vous êtes à mi-chemin de la construction de votre application et que vous réalisiez qu'elle n'a pas tous les outils dont vous avez besoin.

_Consultez les bibliothèques de composants **Ant Design**, **Material UI** ou **Chakra UI** pour votre prochain projet. Ou utilisez une bibliothèque CSS-in-JS comme **Emotion** ou **Styled Components** si vous êtes intéressé par l'écriture de styles à la main._

## 5. Une bibliothèque de formulaires basée sur les hooks

Chaque application React que vous construisez aura probablement un formulaire. Inutile de dire que construire des formulaires est une corvée !

Non seulement vous devez créer le formulaire lui-même, mais vous devez également ajouter des éléments délicats comme la validation des entrées et la gestion des erreurs.

_Les meilleures bibliothèques de formulaires que vous pouvez utiliser en 2021 sont **React Hook Form** et **Formik**._

Avec l'aide de leurs hooks intégrés, elles rendent incroyablement facile la création de formulaires réutilisables et fonctionnels. Même des formulaires qui ont des conditions complexes, telles que des champs qui dépendent les uns des autres ou qui nécessitent une validation asynchrone.

Il est à noter que Formik a changé en ce sens que nous n'avons plus besoin d'utiliser le modèle traditionnel de props de rendu qu'il utilisait précédemment.

Avec Formik, vous pouvez utiliser un hook personnalisé du package Formik appelé `useFormik` qui nous permet de construire nos formulaires avec l'aide d'un hook personnalisé du même nom.

Voici un formulaire de base fait avec `useFormik`.

```js
 import React from 'react';
 import { useFormik } from 'formik';
 
 const SignupForm = () => {
   const formik = useFormik({
     initialValues: {
       username: '',
       email: '',
     },
     onSubmit: values => {
       alert(JSON.stringify(values, null, 2));
     },
   });
   return (
     <form onSubmit={formik.handleSubmit}>
       <label htmlFor="name">Nom d'utilisateur</label>
       <input
         id="username"
         name="username"
         type="text"
         onChange={formik.handleChange}
         value={formik.values.username}
       />
       <label htmlFor="email">Adresse e-mail</label>
       <input
         id="email"
         name="email"
         type="email"
         onChange={formik.handleChange}
         value={formik.values.email}
       />
       <button type="submit">Soumettre</button>
     </form>
   );
 };

```

Il est à noter que la seule chose dont vous pourriez avoir besoin en plus de ces bibliothèques est une bibliothèque de validation.

Formik et React Hook Form sont conçus pour s'intégrer très facilement avec des bibliothèques de validation comme la bibliothèque Yup. Comment faire est très bien expliqué dans leur documentation.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*