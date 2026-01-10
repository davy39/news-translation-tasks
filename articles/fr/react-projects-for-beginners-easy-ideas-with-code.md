---
title: Projets React pour débutants en 2023 – Idées amusantes avec code
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-01-10T17:53:44.000Z'
originalURL: https://freecodecamp.org/news/react-projects-for-beginners-easy-ideas-with-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/7-react-projects-beginners.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Projets React pour débutants en 2023 – Idées amusantes avec code
seo_desc: 'You''re ready to start making simple projects with React, but you don''t
  know what to make. Where should you start?

  I have created seven unique and fun React projects for you to make, all of which
  will teach you essential React concepts that you need t...'
---

Vous êtes prêt à commencer à créer des projets simples avec React, mais vous ne savez pas quoi faire. Par où commencer ?

J'ai créé sept projets React uniques et amusants pour vous, qui vous enseigneront tous les concepts essentiels de React que vous devez connaître en 2023.

Contrairement à d'autres projets recommandés qui nécessitent l'utilisation de plusieurs bibliothèques tierces, tous ces projets n'utilisent que la bibliothèque principale de React. Chacun d'eux utilise la dernière version de React (18) et aucun framework CSS.

Mon objectif en créant ce guide est de vous montrer que vous n'avez pas besoin d'une tonne de code et de bibliothèques spéciales pour commencer à construire des choses cool avec React.

Commençons !

## 1. Carousel d'images

Le premier projet React de notre liste est un slider ou carousel d'images.

### Résultat final

%[https://codesandbox.io/s/runtime-field-xp5sol]

### Comment vous allez le construire

Notre carousel doit permettre à l'utilisateur de cliquer sur le bouton arrière ou avant pour aller à l'image précédente ou suivante.

Les images seront stockées dans un simple tableau. Nous verrons comment utiliser l'état pour stocker l'image actuelle. Ensuite, nous mettrons à jour cet état pour passer à l'image précédente ou suivante, selon le bouton sur lequel l'utilisateur a cliqué.

Si l'utilisateur a parcouru toutes les images, vous découvrirez comment revenir au début du tableau, pour lui permettre de parcourir à nouveau les images. Si vous ne souhaitez pas utiliser d'images, vous pourriez également utiliser du texte pour créer un carousel de témoignages qui fait défiler les avis pour un produit donné.

Enfin, si vous souhaitez passer votre carousel au niveau supérieur, essayez d'ajouter une transition amusante en utilisant CSS pour animer l'image lors de son changement.

### Concepts React que vous allez apprendre

* useState (stockage et mise à jour de l'état)
* Conditionnels (ternaires)
* Listes, clés et .map()

## 2. FAQ/Accordéon

Un autre type courant de composant qui peut utiliser l'état est un composant accordéon, qui peut à la fois révéler et masquer du texte.

### Résultat final

%[https://codesandbox.io/s/determined-hoover-22hclm]

### Comment vous allez le construire

Vous apprendrez à basculer l'état pour vous assurer que chaque accordéon s'ouvre et se ferme après chaque pression sur le bouton. Vous apprendrez également des conditionnels simples tels que l'opérateur et (&&) qui n'affichera le contenu de l'accordéon que lorsque l'état de l'accordéon indiquera qu'il est ouvert.

Enfin, nous créerons une section FAQ (questions fréquemment posées) entière en affichant plusieurs composants accordéon. Pour ce faire, nous apprendrons à transmettre les données de chaque accordéon dans le composant en utilisant les props.

### Concepts React que vous allez apprendre

* Basculer l'état avec useState
* Conditionnels (&&)
* Transmettre des données aux composants via les props
* Afficher plusieurs composants avec `.map()`

## 3. Générateur de citations

L'utilisation d'API externes et la réalisation de requêtes HTTP sont une partie essentielle de toute application React. Pour apprendre à faire des requêtes HTTP dans React, nous allons créer un générateur de citations aléatoires.

### Résultat final

%[https://codesandbox.io/s/zen-diffie-x61ywc]

### Comment vous allez le construire

Notre générateur de citations devra utiliser le hook useEffect pour effectuer un "effet secondaire" afin de récupérer les citations d'une API externe. Après avoir récupéré nos citations, nous les mettrons dans l'état local de notre application, que nous appellerons `quotes`.

Nous prendrons ensuite ce tableau de citations et utiliserons une fonction pour sélectionner un élément aléatoire dans ce tableau. Ensuite, nous le mettrons dans une autre variable d'état appelée simplement `quote`, qui pourra alors être affichée à notre utilisateur.

Nous voulons également ajouter un bouton "Nouvelle citation" au-dessus de chaque citation qui effectuera la même opération – obtenir une nouvelle citation aléatoire de notre tableau `quotes` et la mettre dans `quote`.

Enfin, la citation n'est pas chargée dans l'état. Nous veillerons donc à utiliser l'opérateur de chaînage optionnel (?) pour vérifier en toute sécurité notre objet avant d'essayer d'obtenir une valeur de cette citation dans l'état pour nous assurer que notre application ne génère pas d'erreur.

### Concepts React que vous allez apprendre

* useEffect (pour effectuer des effets secondaires)
* Requêtes HTTP avec Fetch API
* Opérateur de chaînage conditionnel (?)

## 4. Liste de courses

Ensuite, nous verrons comment construire une liste de courses où les utilisateurs peuvent ajouter de nouveaux articles à la liste qu'ils aimeraient obtenir du magasin et supprimer des articles de la liste.

### Résultat final

%[https://codesandbox.io/s/modest-feistel-zsttc9]

### Comment la construire

Ce projet vous apprendra à ajouter de nouveaux éléments à un tableau dans notre état local en utilisant l'opérateur de propagation de tableau. De plus, vous apprendrez à supprimer n'importe quel élément que nous aimons en utilisant la fonction `filter` en JavaScript.

Ce projet vous familiarisera également avec la saisie de valeurs dans un champ de formulaire et la récupération de ces valeurs lorsque le formulaire est soumis. Vous le ferez en utilisant le gestionnaire d'événements `onSubmit`.

Une façon amusante d'améliorer ce projet serait de permettre à nos utilisateurs de double-cliquer sur chaque élément de notre liste pour le barrer en plus de pouvoir le supprimer.

### Concepts React que vous allez apprendre

* Mise à jour des listes avec useState
* Opérateur de propagation de tableau JavaScript et fonctions `filter`
* Formulaires et entrées dans React
* Gestionnaire d'événements `onSubmit`

## 5. Recherche d'utilisateurs GitHub

Dans ce projet, nous utiliserons la valeur d'une entrée pour rechercher des utilisateurs sur GitHub en utilisant leur nom d'utilisateur ou leur email.

### Résultat final

%[https://codesandbox.io/s/mutable-sky-iesdhc]

### Comment le construire

Vous stockerez d'abord la valeur tapée dans l'entrée dans une valeur d'état appelée `query`. Après cela, vous effectuerez une requête HTTP à un point de terminaison de l'API GitHub pour récupérer le profil des utilisateurs qui utilise à nouveau l'API fetch du navigateur. L'URL de la requête utilisera la valeur d'entrée.

Une fois les résultats récupérés, nous verrons comment afficher toutes les informations pertinentes telles que leur nom, leur avatar et un lien pour accéder à leur profil.

Une bonne façon d'étendre ce projet serait d'essayer de permettre la fonctionnalité de recherche au fur et à mesure que l'utilisateur tape, au lieu de devoir soumettre le formulaire d'abord. Assurez-vous d'utiliser une fonction de débogage pour vous assurer de ne pas faire trop de requêtes à l'API GitHub et obtenir une réponse d'erreur 429 (trop de requêtes).

## 6. Lecteur vidéo

React peut également être utilisé pour travailler avec l'élément vidéo HTML et basculer entre différentes vidéos.

%[https://codesandbox.io/s/gifted-dirac-r6m0ns]

### Comment le construire

Dans notre projet, nous permettrons aux utilisateurs de basculer entre plusieurs vidéos différentes en utilisant une entrée radio. Nous verrons non seulement comment travailler avec les entrées radio dans les formulaires dans React, mais aussi comment transmettre des props à nos deux composants, `Menu` et `Video`.

En particulier, nous apprendrons à transmettre des fonctions pour mettre à jour l'état dans les composants parents depuis le composant enfant. Ce modèle est appelé "remonter l'état" et est un modèle très important à connaître dans React.

Une façon amusante d'améliorer ce projet serait d'ajouter un bouton pour étendre la fonctionnalité du lecteur vidéo. Par exemple, pour ajouter des boutons pour contrôler si la vidéo est en boucle, si la vidéo se lance automatiquement, et plus encore.

### Concepts React que vous allez apprendre

* Entrées radio dans React
* Transmission de fonctions en tant que props
* Remonter l'état dans React

## 7. Calculatrice d'IMC

Enfin, nous construirons une calculatrice simple d'IMC (indice de masse corporelle) qui utilisera le poids et la taille d'une personne pour calculer leur indice de masse corporelle sous forme de nombre.

%[https://codesandbox.io/s/festive-water-c70hv3]

### Comment la construire

Nous utiliserons quelques entrées de type range pour permettre à nos utilisateurs de sélectionner leur poids et leur taille sur une échelle glissante.

L'indice de masse corporelle est calculé en fonction des valeurs de poids et de taille stockées. Notre objectif sera de calculer et d'afficher instantanément leur indice de masse corporelle, selon les valeurs stockées dans les variables d'état `weight` et `height`.

Pour ce faire, nous utiliserons le hook `useMemo` de React pour calculer cette valeur de manière performante chaque fois que l'une de ces deux valeurs change.

### Concepts React que vous allez apprendre

* Entrées de type range dans React
* useMemo (pour effectuer des calculs de manière performante)

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*