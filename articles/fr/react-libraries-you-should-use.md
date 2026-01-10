---
title: Les meilleures bibliothèques React que vous devriez utiliser aujourd'hui
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-08T18:34:32.000Z'
originalURL: https://freecodecamp.org/news/react-libraries-you-should-use
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/react-libraries-you-should-be-using.png
tags:
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
seo_title: Les meilleures bibliothèques React que vous devriez utiliser aujourd'hui
seo_desc: "Let's take a look at five React libraries that serve as a great addition\
  \ to any React project you're looking to build in 2021 and beyond. \nI chose these\
  \ libraries because not only do they help us build functional and impressive-looking\
  \ applications, ..."
---

Examinons cinq bibliothèques React qui constituent un excellent ajout à tout projet React que vous souhaitez construire en 2021 et au-delà. 

J'ai choisi ces bibliothèques non seulement parce qu'elles nous aident à construire des applications fonctionnelles et impressionnantes, mais aussi parce qu'elles nous permettent de le faire plus rapidement, plus facilement et avec moins de code.

Dans ce guide, je vais vous montrer comment démarrer et utiliser chacune de ces bibliothèques à partir de zéro et les intégrer dans vos projets dès aujourd'hui.

## 1. React Query

Récupérer des données avec React est généralement un processus qui implique beaucoup de code.

Vous devez souvent utiliser le hook `useEffect` en combinaison avec `useState` pour gérer les données récupérées. Cela nécessite beaucoup de code boilerplate que nous devons écrire dans chaque composant dans lequel nous voulons récupérer des données. 

React Query peut vous aider à réduire le code que vous écrivez lors de la réalisation de requêtes réseau avec React. Tout ce code React que nous devions écrire auparavant peut être remplacé par le hook `useQuery`. À partir de celui-ci, nous obtenons toutes les données dont nous avons besoin sans avoir à déclarer une variable d'état :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/react-query.gif)

Cependant, faciliter la récupération des données ne couvre qu'une petite partie de ce que fait React Query. Ce qui en fait une bibliothèque très puissante, c'est qu'elle met en cache (sauvegarde) les requêtes que nous faisons. Ainsi, dans de nombreux cas, si nous avons déjà demandé des données, nous n'avons pas besoin de faire une autre requête, nous pouvons simplement les lire depuis le cache. 

Cela est extrêmement utile car cela réduit la répétition dans notre code, diminue la charge que nous mettons sur notre API et nous aide à gérer l'état global de notre application. Si vous choisissez une bibliothèque pour commencer à l'ajouter à vos projets aujourd'hui parmi cette liste, choisissez React Query. 

## 2. Ant Design

En ce qui concerne la création d'applications React impressionnantes, il existe de nombreuses bibliothèques de composants utiles qui nous permettent de styliser rapidement nos applications à l'aide de composants pré-faits. 

Il existe de nombreuses bibliothèques de composants, mais peu sont aussi sophistiquées et bien conçues qu'une appelée Ant Design. Si vous pouvez penser à un type de composant à inclure dans l'interface et le design de votre application React, Ant Design l'a presque certainement :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/antd.gif)

L'utilisation d'une bibliothèque de composants comme Ant Design accélère notre temps de développement en réduisant la quantité de styles souvent peu fiables que nous devons écrire nous-mêmes. 

De plus, ces composants pré-faits fournissent des fonctionnalités qu'il serait souvent redondant de créer nous-mêmes, comme une modale ou une infobulle commune. Dans la plupart des cas, nous devrions opter pour la solution fiable et éprouvée plutôt que de tenter de réinventer la roue.

Si vous pensez à construire une application aujourd'hui et que vous cherchez une bibliothèque de composants solide, choisissez Ant Design. Elle possède pratiquement toutes les fonctionnalités dont vous auriez besoin dans une bibliothèque de composants, ainsi qu'une grande personnalisation qui sert à toute fonctionnalité d'application que vous pourriez envisager d'implémenter. 

## 3. Zustand

En ce qui concerne la gestion de l'état, les développeurs React se voient souvent proposer deux choix familiers : Redux ou React Context. 

Redux a été la bibliothèque tierce de référence que les développeurs React utilisent pour gérer l'état. Mais avec l'arrivée de React Context dans la version 16 de React, nous avons une manière plus facile de gérer l'état en le passant autour de notre arbre de composants. 

Si vous cherchez une bibliothèque avec toute la fonctionnalité et la puissance de Redux, avec la simplicité de React Context, regardez la bibliothèque Zustand. Elle est incroyablement facile à démarrer, comme vous pouvez le voir dans l'exemple ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/zustand.gif)

Elle implique l'utilisation de la fonction `create` pour créer un objet d'état dédié qui peut inclure toutes les valeurs d'état et fonctions pour mettre à jour cet état selon nos besoins. Tout cela peut être créé en quelques lignes de code. 

De plus, il n'est pas nécessaire d'utiliser un fournisseur de contexte pour passer votre état à vos composants d'application. Tout ce que vous avez à faire est de créer une tranche d'état, d'appeler cet état créé comme un hook, et de recevoir les variables d'état et fonctions que vous avez déclarées sur l'objet dans vos composants React. 

Essayez Zustand la prochaine fois que vous chercherez une solution d'état plus complexe comme Redux pour votre application – vous allez l'adorer.

## 4. React Hook Form

En ce qui concerne la construction de formulaires dans React, vous savez probablement à quel point il peut être fastidieux d'effectuer des tâches de base comme la validation des entrées, ainsi que la gestion de l'état du formulaire et des erreurs. 

Peut-être la bibliothèque de formulaires la plus conviviale disponible aujourd'hui est React Hook Form. Toutes les fonctionnalités dont vous avez besoin dans une bibliothèque de formulaires sont fournies dans un seul hook simple, appelé `useForm`, et vous permettent de créer des formulaires aussi sophistiqués que vous le souhaitez. 

Il prend en charge la gestion de notre état de formulaire en interne, nous donne des helpers faciles pour afficher les erreurs pour l'entrée appropriée, et applique des règles de validation sans aucune bibliothèque externe telle que Yup – ainsi que la gestion de la soumission de notre formulaire :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/react-hook-form.gif)

En ce qui concerne la construction de formulaires fonctionnels, vous voulez une bibliothèque qui est facile à utiliser et qui n'ajoute pas trop de code à vos composants. Selon ces deux critères, React Hook Form est probablement la meilleure bibliothèque de formulaires React disponible.

## 5. React Responsive

Il n'y a aucun doute – chaque application React devrait être créée pour les utilisateurs sur différents appareils et doit être responsive. Cela signifie qu'elle doit ajuster les styles et l'apparence en fonction de la taille de l'écran ou de l'appareil que vos utilisateurs utilisent. 

Bien que les media queries aient généralement été utilisées dans les feuilles de style CSS pour masquer et afficher différents éléments, la meilleure bibliothèque basée sur React pour gérer la visibilité ou les styles des composants React est React Responsive. 

Elle nous donne un hook `useMediaQuery` pratique qui nous permet de passer des conditions très précises pour déterminer si les utilisateurs sur un certain type d'écran utilisent un certain appareil. Ensuite, ils pourront ajuster notre interface utilisateur en conséquence :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/react-responsive.gif)

Pour rendre toute application React responsive sans utiliser de CSS, assurez-vous de consulter la bibliothèque React Responsive.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*