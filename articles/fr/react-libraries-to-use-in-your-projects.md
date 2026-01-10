---
title: Bibliothèques React à utiliser dans vos projets en 2024
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-02-02T18:42:15.000Z'
originalURL: https://freecodecamp.org/news/react-libraries-to-use-in-your-projects
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/react-libraries-2024.png
tags:
- name: Libraries
  slug: libraries
- name: React
  slug: react
seo_title: Bibliothèques React à utiliser dans vos projets en 2024
seo_desc: 'If you''re building applications with React, you should learn how to use
  some helpful libraries that''ll make it easier to add the features you need.

  For example, to add features like authentication or styling, you''ll need to find
  a good third-party li...'
---

Si vous construisez des applications avec React, vous devriez apprendre à utiliser certaines bibliothèques utiles qui faciliteront l'ajout des fonctionnalités dont vous avez besoin.

Par exemple, pour ajouter des fonctionnalités comme l'authentification ou le style, vous devrez trouver une bonne bibliothèque tierce pour la gérer.

Dans ce guide complet, je vais vous montrer toutes les bibliothèques que je recommande d'utiliser en 2024 pour construire des applications React rapides et fiables avec facilité.

## Table des matières

* [Framework React](#heading-framework-react)
* [Gestionnaire de paquets](#heading-gestionnaire-de-paquets)
* [Bibliothèques CSS et UI](#heading-bibliothèques-css-et-ui)
* [Gestion d'état](#heading-gestion-détat)
* [Récupération de données](#heading-récupération-de-données)
* [Routing](#heading-routing)
* [Authentification](#heading-authentification)
* [Base de données et ORM](#heading-base-de-données-et-orm)
* [Dates et heures](#heading-dates-et-heures)
* [Formulaires](#heading-formulaires)
* [Glisser-déposer](#heading-glisser-déposer)
* [Applications mobiles](#heading-applications-mobiles)
* [Déploiement](#heading-déploiement)
* [TypeScript](#heading-le-1-bibliothèque-à-connaître)
* [Devenir un développeur React professionnel](#heading-devenir-un-développeur-react-professionnel)

## 🏠 Framework React

Tout d'abord, comment créons-nous même notre application React en 2024 ?

Si vous voulez un projet React rendu côté client, [votre meilleur choix est **Vite**](https://www.freecodecamp.org/news/how-to-create-a-react-app-in-2024/), qui a remplacé l'outil déprécié Create React App.

Si vous êtes intéressé par la création d'un projet React rendu côté serveur ou full-stack, **Next.js** est le framework React full-stack le plus complet et populaire. 

La version 13 de Next.js a introduit le routeur d'applications, qui nous a donné des fonctionnalités comme les composants serveur et les actions serveur. Ceux-ci nous permettent de récupérer des données et de rendre nos composants React sur le serveur.

Si certaines des fonctionnalités de Next.js sont trop complexes ou si vous ne comprenez pas comment les utiliser, une excellente alternative full-stack pour créer des sites dynamiques et statiques est **[Remix](https://remix.run/)**.

Si vous créez une application que vous voulez charger rapidement et servir largement du contenu statique, un autre excellent choix est **[Astro](https://www.freecodecamp.org/news/learn-the-astro-web-framework/)**. Astro vous permet d'utiliser React aux côtés d'autres frameworks comme Vue et Svelte (ce qui signifie qu'il est "agnostique de framework") et est conçu pour envoyer la plus petite quantité de JavaScript nécessaire au client, ce qui entraîne des temps de chargement très rapides.

## 📦 Gestionnaire de paquets

Pour installer toutes les bibliothèques listées dans ce guide, vous allez avoir besoin de quelque chose appelé un gestionnaire de paquets.

Si vous avez Node.js installé, ce qui est nécessaire pour exécuter un projet React localement sur votre ordinateur, vous pouvez simplement utiliser **NPM**, qui reste un excellent choix en 2024. Il existe d'autres alternatives à NPM, notamment Yarn et PNPM.

La nouvelle alternative, qui devient rapidement très populaire dans le monde JavaScript, est **[Bun](https://www.freecodecamp.org/news/learn-bun-a-faster-node-js-alternative/)**. Bun est à la fois un runtime JavaScript comme Node ainsi qu'un gestionnaire de paquets et est commercialisé comme une alternative plus rapide à Node et NPM.

## 🎨 Bibliothèques CSS et UI

Maintenant que vous avez configuré votre projet et installé vos bibliothèques, comment allez-vous styliser vos projets React ?

Tous les frameworks que j'ai mentionnés ci-dessus incluent un support CSS de base. Il est parfaitement acceptable en 2024 si vous souhaitez vous en tenir à styliser vos projets React avec du **CSS simple**.

Vous pouvez utiliser des feuilles de style CSS ou des modules CSS, mais peut-être le choix le plus populaire en ce moment en termes de style pur est d'utiliser **[Tailwind CSS](https://www.freecodecamp.org/news/learn-tailwind-css/)**. Tailwind CSS nécessite quelques étapes de configuration, mais il vous permet de chaîner des classes pré-faites pour ajouter rapidement des styles directement dans vos fichiers de composants.

**[ShadCN](https://ui.shadcn.com/)** est une bibliothèque UI très populaire pour 2024 qui combine Tailwind CSS avec une bibliothèque de composants appelée Radix UI. Les bibliothèques de composants comme Radix vous permettent d'ajouter facilement des composants sans les coder vous-même. 

ShadCN est devenu populaire grâce au meilleur contrôle qu'il offre sur l'apparence de vos composants avec l'aide de Tailwind CSS.

Il existe également de nombreuses autres bibliothèques de composants fonctionnels très populaires. **Material UI** reste populaire, ainsi que d'autres comme **Mantine** et **Chakra UI**. Celui que vous choisissez dépend vraiment de l'apparence que vous souhaitez donner à votre application finale. Je vous recommande d'essayer plusieurs de ces bibliothèques UI et de voir celle que vous préférez.

## 📝 Gestion d'état

React dispose d'outils intégrés tels que [useState](https://www.freecodecamp.org/news/learn-react-usestate-hook-in-10-minutes/) et [useReducer](https://www.freecodecamp.org/news/usereducer-hook-react/) pour gérer l'état de votre application dans les applications de base. Si vous utilisez Next.js, [la gestion d'état a été déplacée vers l'URL](https://www.freecodecamp.org/news/how-to-use-urls-for-state-management-in-react/) lors de l'utilisation de composants serveur. Malgré ces options, vous pourriez avoir besoin d'une manière de gérer l'état de manière plus précise.

Vous pourriez avoir beaucoup de morceaux d'état et vouloir un meilleur contrôle sur la manière dont les mises à jour d'état rendent vos composants. Si c'est le cas, vous pouvez opter pour une bibliothèque de gestion d'état dédiée.

Des bibliothèques telles que **Zustand**, **Recoil** et **Jotai**, qui sont toutes très similaires, vous permettent de gérer l'état simplement en déclarant des propriétés et des méthodes sur un objet. Cela reste finalement la manière la plus simple de gérer la gestion d'état dans les composants de votre application.

Si je devais choisir une bibliothèque de gestion d'état pour tous mes projets React en 2024, je choisirais **[Zustand](https://www.npmjs.com/package/zustand)**. Il prend presque aucun temps pour apprendre à l'utiliser. Il ne vous oblige pas non plus à ajouter un composant fournisseur à votre application, ce qui le rend très pratique à utiliser dans n'importe quel composant que vous aimez.

## 🐕 Récupération de données

La gestion d'état et la récupération de données vont souvent de pair. Si vous construisez une application React rendue côté client, vous aurez probablement besoin d'une bibliothèque de récupération de données.

La meilleure façon de récupérer des données à partir d'un serveur dans une application React en 2024 reste React Query ou **Tanstack Query** comme il est maintenant appelé. TanStack Query vous donne un contrôle fin non seulement sur la récupération de données, quand les récupérer et les récuperer, la mise en cache, le tout via des hooks personnalisés pratiques, ainsi que la possibilité de modifier ou de muter des données très facilement.

Une autre alternative solide est **SWR**, qui offre également un hook personnalisé pour gérer les requêtes et les mutations, mais il est beaucoup plus simple en termes de ce qu'il offre. Vous ne pouvez pas vous tromper en choisissant l'un ou l'autre et en récupérant des données et en effectuant vos requêtes HTTP avec l'API fetch.

[Voici un article](https://www.freecodecamp.org/news/how-to-fetch-api-data-in-react/) qui vous guide à travers certaines des méthodes les plus populaires de récupération de données dans React (y compris Tanstack Query et SWR).

## 🧭 Routing

Si vous utilisez un framework comme Next.js, Remix ou Astro, votre routage est déjà pris en charge. Tous incluent des moyens intégrés de créer des routes ou des pages dans votre projet.

Avec une application React rendue côté client telle qu'une application créée avec Vite ou Create React App, vous devrez choisir une bibliothèque de routage. **[React Router](https://www.freecodecamp.org/news/learn-react-router-6-full-course/)** reste le choix le plus populaire. Il prend en charge tous vos besoins de routage. Il est également très avancé grâce à ses fonctionnalités de chargement de données avec la propriété `loader`. La propriété `loader` vous permet de récupérer des données pour une route donnée sans utiliser une bibliothèque externe comme React Query.

Une bibliothèque émergente qui semble avoir des fonctionnalités tout aussi bonnes est **[Tanstack Router](https://tanstack.com/router/latest)**. Le Tanstack Router a été conçu pour être entièrement type-safe et offrir de bonnes valeurs par défaut pour la récupération de données, tout comme React Router version 6 le fournit.

Bien que Tanstack Router soit un peu plus récent, vous ne pouvez pas vous tromper avec l'un ou l'autre choix, et c'est un parfait complément si vous utilisez déjà Tanstack Query ou SWR dans vos applications.

## 🔐 Authentification

Bien que l'authentification soit quelque chose qui est géré par le côté serveur de nos projets, il est utile de savoir quelles bibliothèques s'intègrent le mieux avec les projets React, à la fois sur le client et le serveur.

En 2024, [**Supabase a émergé**](https://www.freecodecamp.org/news/learn-supabase-open-source-firebase-alternative/) comme une solution d'authentification très robuste et offre une intégration facile avec les applications React, à la fois sur le serveur, par exemple, dans un projet Next.js, et sur le client. Dans les années passées, Firebase était choisi pour des raisons similaires, mais il est plus difficile à intégrer du côté serveur.

Si vous utilisez Next.js, vous avez un grand nombre d'options disponibles telles que **NextAuth**, **Clerk** et le nouveau venu **Lucia**. Il est dommage qu'il n'existe pas actuellement de bibliothèque d'authentification intégrée pour Next.js, mais peut-être qu'à l'avenir il y en aura une.

En attendant, je vais personnellement utiliser Supabase et je vous recommande vivement de les consulter également via leur documentation.

## 🗄️ Base de données et ORM

Tout comme l'authentification, votre base de données est quelque chose qui parlera et devrait largement parler à votre code côté serveur.

Des bases de données comme Supabase et Firebase ne nécessitent pas que vous ayez un serveur. Vous pouvez obtenir et modifier des données directement dans le client, et vous pouvez ajouter des règles de sécurité dans votre tableau de bord pour vous assurer que certains types de requêtes sont autorisés ou non selon le statut d'authentification et le rôle des utilisateurs.

En dehors de ces deux options, si vous utilisez un serveur traditionnel ou un framework full-stack, il existe d'innombrables options. En 2024, la préférence générale est clairement pour les bases de données SQL comme MySQL ou PostgreSQL plutôt que pour les bases de données NoSQL comme MongoDB ou Firebase.

Avec votre base de données, pour communiquer avec votre base de données, vous utiliserez soit du SQL simple, soit un ORM qui vous permet d'utiliser un langage de requête personnalisé. Les options populaires pour les ORM incluent **Prisma** ou **Drizzle**. Tous deux vous permettent de générer du code type-safe afin que vous sachiez quelles données seront retournées et tous deux s'intègrent très bien avec les bases de données SQL ou NoSQL de votre choix.

## ⏰ Dates et heures

Lorsque vous travaillez avec JavaScript, il est toujours recommandé d'avoir une bibliothèque de dates. Le constructeur de dates de JavaScript est imprévisible et pratiquement impossible à utiliser de manière fiable avec des choses comme les fuseaux horaires.

Il existe de nombreuses options, mais je tends à me tourner vers **date-fns** ou **day.js**. Tous deux sont des bibliothèques très petites mais extensives qui vous permettent de manipuler les dates JavaScript soit dans le navigateur, soit sur le backend. Vous ne pouvez pas vous tromper avec l'un ou l'autre.

## 📋 Formulaires

Vous n'aurez peut-être pas besoin d'une bibliothèque de formulaires dans la plupart des cas si vous construisez simplement une application avec un formulaire d'inscription simple, utiliser la propriété `required` sur vos entrées est généralement tout ce dont vous avez besoin.

Si vous construisez quelque chose de plus complexe et que vous avez beaucoup de formulaires, **[React Hook Form](https://www.freecodecamp.org/news/how-to-create-forms-in-react-using-react-hook-form/)** est une bibliothèque de formulaires complète qui vous permet de valider les entrées de formulaire et d'afficher des erreurs avec très peu de code.

D'autres bibliothèques de formulaires, telles que Formik et React Final Form, vous donneront la même fonctionnalité, mais React Hook Form est un peu meilleur car il a une API plus moderne basée sur les hooks et nécessite généralement moins de code.

## ☂️ Glisser-déposer

Lorsque vous ajoutez du glisser-déposer à votre application, vous avez presque certainement besoin d'une bibliothèque tierce. Le choix le plus populaire dans le passé a été React Beautiful DnD. À partir de 2024, il ne reçoit plus de mises à jour régulières.

À l'avenir, un remplacement solide pour le glisser-déposer est d'utiliser **[DnD Kit](https://dndkit.com/)**. Il est léger, très flexible, et la documentation inclut de nombreux exemples très utiles couvrant tous les cas d'utilisation que vous pourriez avoir lors de la mise en œuvre du glisser-déposer.

## 📱 Applications mobiles

Si vous souhaitez créer une application mobile, la bibliothèque pour le faire pour les développeurs React a toujours été [React Native](https://www.freecodecamp.org/news/react-native-full-course-android-ios-development/). Il existe des bibliothèques passionnantes qui repoussent les limites de React Native pour s'étendre au web.

[**Expo** est un outil similaire à Vite](https://expo.dev/), mais pour créer des applications mobiles React. Il dispose de fonctionnalités intéressantes comme le rafraîchissement rapide, et avec Expo Go, vous pouvez facilement exécuter votre projet sur votre propre appareil pendant que vous le développez. Expo facilite la prise de votre base de code mobile et son déploiement sur le web.

C'est l'objectif final d'autres projets tels que **[Tamagui](https://tamagui.dev/)**, que vous devriez également consulter si vous souhaitez créer une véritable application native qui fonctionne sur Android, iOS et le web.

Si vous avez une application React que vous avez déjà écrite pour fonctionner dans le navigateur, le moyen le plus rapide de la faire fonctionner comme une application native et de la lancer sur l'Apple App Store ou le Google Play Store est d'utiliser **[Capacitor.js](https://capacitorjs.com/)**.

## 🚀 Déploiement

Il existe plus de moyens que jamais de déployer votre application React. [Vercel est probablement la plateforme la plus facile](https://www.freecodecamp.org/news/deploy-react-app/) pour déployer votre application React, qu'elle soit rendue côté client ou côté serveur. Ils supportent presque tous les frameworks auxquels vous pouvez penser, y compris les langages non-JavaScript. Ils ont un plan hobby généreux, et les concurrents dans le même espace incluent Netlify et Cloudflare Pages.

Cloudflare Pages peut être un peu plus difficile à configurer, surtout si vous avez un projet React full-stack, mais c'est le plus généreux en termes de prix parmi toutes ces options. Si vous ne craignez pas de payer pour un serveur, vous pouvez utiliser quelque chose comme Railway ou Render, qui est idéal pour déployer si vous avez un serveur séparé de votre application React.

## ✨ Le #1 Bibliothèque à connaître

Enfin, la bibliothèque essentielle numéro un que vous devriez connaître si vous êtes un développeur React en 2024 est [TypeScript](https://www.freecodecamp.org/news/learn-typescript-beginners-guide/). Tous les frameworks que j'ai mentionnés incluent des options pour construire une application React avec TypeScript.

TypeScript est un outil qui vous permet de détecter les erreurs de type dans votre code JavaScript pour vous aider à prévenir les erreurs d'exécution. Vous pouvez construire tous vos projets React avec juste JavaScript, mais à un moment donné, vous allez soit voir les avantages d'utiliser TypeScript vous-même, soit regarder une base de code qui contient TypeScript.

Je vous recommande vivement de prendre le temps d'apprendre TypeScript. C'est l'outil le plus essentiel, le plus demandé à connaître en tant que développeur React et peut grandement améliorer la qualité globale de votre code.

## 🏆 Devenir un développeur React professionnel

Vous cherchez la ressource ultime pour apprendre React de A à Z ?

✨ **[Présentation : Le React Bootcamp](https://www.thereactbootcamp.com)**

Le bootcamp propose toutes les ressources pour vous aider à réussir avec React :

* 🎬 200+ vidéos approfondies
* 🧩 100+ défis pratiques React
* 🏗️ 5+ projets de portfolio impressionnants
* 📝 10+ fiches de référence React essentielles
* 🧪 Un bootcamp Next.js complet
* 🎥 Une série complète de vidéos animées

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même.

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)  
_Cliquez pour commencer_