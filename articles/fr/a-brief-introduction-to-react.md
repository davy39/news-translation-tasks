---
title: Une brève introduction à React
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-05-01T15:48:29.032Z'
originalURL: https://freecodecamp.org/news/a-brief-introduction-to-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746109202328/e4b0f59b-a8d1-42de-9eff-b5413ced3b93.png
tags:
- name: React
  slug: reactjs
- name: Web Development
  slug: web-development
- name: JavaScript
  slug: javascript
seo_title: Une brève introduction à React
seo_desc: This tutorial introduces the basics of using React components in your web
  apps. React is a JavaScript library used to build user interfaces, especially for
  single-page applications where parts of the page need to update without a full page
  reload. It...
---

Ce tutoriel présente les bases de l'utilisation des composants [React](https://react.dev/) dans vos applications web. React est une bibliothèque JavaScript utilisée pour construire des interfaces utilisateur, en particulier pour les applications monopages où certaines parties de la page doivent être mises à jour sans rechargement complet de la page. Elle aide les développeurs à créer des composants interactifs et réutilisables qui gèrent leur propre état et répondent efficacement aux changements de données.

Ce guide suppose que vous avez une certaine expérience en programmation et que vous êtes à l'aise avec la lecture et l'écriture de JavaScript. Vous devriez comprendre les variables, les fonctions, les boucles, les objets et le fonctionnement de JavaScript dans le navigateur. Vous n'avez pas besoin de connaître React ou des outils de construction, car ceux-ci sont introduits au fur et à mesure.

### Comment ce guide fonctionne

Les trois leçons présentées ici sont tirées de mon livre gratuit de playbacks de code :
[An Introduction to Web Development from Back to Front](https://playbackpress.com/books/webdevbook/).

Ce livre est disponible gratuitement sur [Playback Press](https://playbackpress.com/books/). Le livre est un guide pratique du développement web moderne, couvrant tout, des fonctionnalités principales de JavaScript à la construction d'applications full-stack avec des outils comme Node, Express, SQLite, Mongo et GraphQL.

Chaque leçon est présentée sous forme de [code playback](https://markm208.github.io/), qui est une visite interactive du code montrant comment un programme évolue au fil du temps, accompagnée de mes explications sur ce qui se passe. Ce format vous aide à vous concentrer sur la logique derrière les changements de code.

Pour visualiser un playback, cliquez sur les commentaires dans le panneau de gauche. Chaque commentaire met à jour le code dans l'éditeur et met en évidence le changement. Lisez l'explication, étudiez le code et utilisez le tuteur IA intégré si vous avez des questions. Voici une courte vidéo montrant comment utiliser un code playback :

%[https://youtu.be/uYbHqCNjVDM]

Il existe de nombreuses autres excellentes ressources sur React. Après avoir terminé cette brève introduction, consultez le tutoriel officiel de l'équipe React : [https://react.dev/learn](https://react.dev/learn).

## **Table des matières**

* [Introduction à React : Votre premier composant](#heading-introduction-a-react-votre-premier-composant)

* [Créer une application React avec Vite](#heading-creer-une-application-react-avec-vite)

* [Connecter React à un backend réel avec Express](#heading-connecter-react-a-un-backend-reel-avec-express)

## **Introduction à React : Votre premier composant**

Cette première leçon introduit la construction d'interfaces utilisateur à l'aide de petits composants React réutilisables. Au lieu d'écrire du code pour mettre à jour directement le DOM, vous définissez à quoi l'interface utilisateur devrait ressembler, et React se charge de synchroniser le DOM avec vos données.

Le playback montre comment utiliser `ReactDOM.render` avec `React.createElement`, puis comment écrire le même composant en utilisant JSX. Au cours des trois leçons, je vais créer un site qui affiche quelques légendes de l'informatique (et un imposteur).

La leçon passe ensuite à la création d'un composant `CustomHeader` qui prend des propriétés ou `props`. Elle montre comment passer des données dans un composant et comment la déstructuration peut faciliter cela. À la fin, vous saurez comment écrire et réutiliser des composants simples qui peuvent être utilisés dans des applications React plus grandes.

**Visualisez le playback ici :** [**Basic React**](https://playbackpress.com/books/webdevbook/chapter/4/1)

## **Créer une application React avec Vite**

La leçon suivante montre comment créer un projet React moderne en utilisant [Vite](https://vite.dev/). Vite prend en charge la configuration en créant un dossier de projet, en installant les bibliothèques, en exécutant un serveur de développement et en préparant une version pour la production. Cela vous permet de sauter toute configuration manuelle et de commencer à construire votre application immédiatement.

Je vais développer l'application CS Legends de la première leçon, mais cette fois dans un répertoire de projet. Je vais séparer les composants dans différents fichiers et utiliser JSX. Le playback introduit également `useState` pour gérer les données dynamiques et montre comment passer des données et des gestionnaires d'événements entre les composants. Le résultat est une application front-end fonctionnelle avec une structure claire et un code réutilisable.

**Visualisez le playback ici :** [**Using Vite to Create a React App**](https://playbackpress.com/books/webdevbook/chapter/4/2)

## **Connecter React à un backend réel avec Express**

Cette dernière leçon étend l'application Vite + React en ajoutant un backend Express avec une base de données. Au lieu de stocker les données des légendes dans l'état local de React, l'application récupérera et mettra à jour les données en utilisant une API Express. Vous allez créer un deuxième dossier pour le serveur backend, le connecter à une base de données et écrire des routes pour obtenir et ajouter des données.

J'utilise le hook `useEffect` pour charger les données depuis le serveur Express lorsque l'application démarre. Vous allez également configurer le package `cors` pour permettre au frontend et au backend de communiquer entre eux pendant le développement. Une fois que tout fonctionne, l'application React est compilée en un bundle statique et est servie par le serveur Express. Le résultat est une application web full-stack, prête à être déployée.

**Visualisez le playback ici :** [**Using React and Express Together**](https://playbackpress.com/books/webdevbook/chapter/4/3)

## Conclusion

Ces trois leçons couvrent les bases, mais il y a beaucoup plus à apprendre. Si vous avez trouvé ce format utile, explorez le reste du livre pour voir comment des applications web complètes sont construites à partir de zéro en utilisant des outils et des frameworks modernes.

React n'est qu'une pièce du puzzle du développement web. Continuez à construire, continuez à lire et essayez les autres playbacks lorsque vous serez prêt à aller plus loin.

Si vous avez des commentaires sur les playbacks, j'adorerais avoir de vos nouvelles. Vous pouvez me contacter ici [mark@playbackpress.com](mailto:mark@playbackpress.com).

Si vous souhaitez soutenir mon travail et aider à garder Playback Press gratuit pour tous, envisagez de faire un don via [GitHub Sponsors](https://github.com/sponsors/markm208). J'utilise toutes les donations pour couvrir les coûts d'hébergement. Votre soutien m'aide à continuer à créer du contenu éducatif comme celui-ci. Merci !