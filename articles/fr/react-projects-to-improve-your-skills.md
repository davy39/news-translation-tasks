---
title: 8 projets React à construire en 2023
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-01-05T00:22:40.000Z'
originalURL: https://freecodecamp.org/news/react-projects-to-improve-your-skills
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/8-react-projects.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: 8 projets React à construire en 2023
seo_desc: "If you want to be good at React, building projects is one of the best ways\
  \ to do it. \nI have put together eight different projects that will not only show\
  \ you what's possible to make with React, but give you some inspiration on what\
  \ apps to make. \nAd..."
---

Si vous voulez devenir bon avec React, construire des projets est l'une des meilleures façons de le faire. 

J'ai rassemblé huit projets différents qui vous montreront non seulement ce qu'il est possible de faire avec React, mais qui vous donneront également de l'inspiration pour les applications à créer. 

De plus, je vais vous donner tous les outils dont vous avez besoin pour construire efficacement chaque projet de la liste. 

Commençons !

## Application Todo

Si vous voulez commencer à construire des projets, il n'y a pas de meilleur point de départ qu'une simple application todo. 

Une application todo présentera une fonctionnalité CRUD de base, ce qui signifie que vous pouvez créer, lire, mettre à jour et supprimer des todos. Les todos peuvent être remplacés par tout type de contenu que vous souhaitez. En fait, de nombreuses applications que nous utilisons au quotidien pourraient être considérées comme des applications todo glorifiées. 

L'avantage de construire une application todo est que l'ensemble de l'application peut être réalisé en peu de temps. Si vous pouvez construire une application todo sans aucun tutoriel pour vous guider, c'est un bon test pour évaluer votre maîtrise de React. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-03-at-12.37.07-PM.png)
_TodoMVC todo app_

Les applications todo sont un excellent projet pour commencer car vous n'avez besoin d'aucune bibliothèque tierce pour les construire. Vous pouvez rendre votre application todo aussi complexe que vous le souhaitez, ce qui vous aidera à devenir confiant avec les concepts que vous souhaitez apprendre. Vous voulez ajouter une authentification ou une base de données à votre application ? N'hésitez pas à le faire ! Vous pouvez vraiment la rendre aussi simple ou complexe que vous le souhaitez.

### Stack à utiliser

* Application React basique
* Fonctionnalités principales de React (State, Context, etc.)
* C'est tout !

## Blog Personnel

Un cran au-dessus de l'application todo de base, un site web de blog. 

Si vous souhaitez écrire en **Markdown**, qui est un style populaire d'écriture et de mise en forme de texte, votre blog consistera probablement en un certain nombre de fichiers Markdown (.md). 

Si vous souhaitez que le contenu soit inclus localement dans le projet pour le rendre un peu plus difficile, vous pourriez essayer de le récupérer à partir d'une source externe comme un CMS (système de gestion de contenu) tel que Sanity ou Contentful. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screen-Shot-2023-01-03-at-1.11.07-PM.png)
_Next Blog Starter Kit (https://next-blog-starter.vercel.app/)_

Dans tous les cas, ce blog va consister en des pages statiques, donc vous pouvez utiliser n'importe quel générateur de site statique que vous aimez. 

Un bon choix de framework pour ce blog pourrait être **Next.js** ou **Gatsby**. Les deux sont idéaux pour créer des sites web basés sur du texte comme des blogs car ils sont des frameworks rendus côté serveur et vous offrent un meilleur référencement. Cela est comparé à une application React traditionnelle rendue côté client (une application créée avec Create React App, par exemple). 

Notre stack consistera en l'un de ces frameworks React plus un transformateur pour convertir notre contenu markdown en HTML lorsque notre site est construit. Un bon choix pour transformer notre contenu markdown est le package npm `remark`. 

Si vous voulez créer un blog encore plus impressionnant, avec du contenu dynamique, alors vous pouvez envisager d'utiliser **MDX**. MDX est très similaire au markdown simple, mais il vous permet également d'inclure vos propres composants React personnalisés dans le markdown. 

Pour utiliser MDX, vous pourriez utiliser un package comme `next-mdx-remote` si vous utilisez Next.js. Le package `mdx-js/mdx` fonctionne également très bien.

### Stack à utiliser

* Next.js/Gatsby
* Markdown ou MDX (`remark` ou `mdx-js/mdx`)
* CMS (Contentful ou Sanity)

Juste une petite note : pour chacun de ces projets, je ne parlerai pas du style. Je préfère personnellement utiliser du CSS simple sous la forme de TailwindCSS. Vous pouvez vous rendre sur le site de Tailwind pour voir comment le configurer facilement pour le framework React que vous utilisez.

## Application E-commerce

L'étape suivante après notre projet de blog est une application e-commerce. 

Elle présente de nombreuses fonctionnalités similaires à notre blog, y compris le fait que la plupart du contenu sera largement statique et inchangé. 

Une fois de plus, les données peuvent être sourcées localement ou récupérées à partir d'un CMS au moment de la construction. Ce qui est différent avec une application e-commerce, c'est qu'elle nous permet de nous aventurer dans le travail avec un serveur d'une sorte ou d'une autre. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-15.png)
_Next.js E-commerce App_

Si vous voulez que vos clients achètent un article via Stripe, par exemple, vous pourriez vouloir configurer un **webhook** qui recevra un événement de Stripe lorsque votre client aura acheté un article particulier. Cela est essentiel pour gérer des choses comme votre inventaire de produits. 

Pour écrire très facilement du code côté serveur, vous pourriez utiliser une route API afin de ne pas avoir à configurer un projet Node.js complet. Cette fonction traiterait différents événements qui ont lieu lors du passage à la caisse ou après celui-ci. 

De plus, si vous ne voulez pas avoir à toucher du code côté serveur, vous pouvez éviter entièrement le package npm `stripe` et utiliser simplement **Stripe checkout** ou un **lien de paiement Stripe**. 

À l'avenir, chaque projet que nous allons aborder impliquera un serveur d'une sorte ou d'une autre. Presque toutes les applications que vous utilisez ont un backend et un frontend. React sera toujours le frontend de notre application, mais sachez que pour chacun de ces projets, vous pouvez très facilement configurer un serveur pour votre application afin de gérer des choses comme la communication avec une base de données lorsque vous avez un framework comme Next.js. 

Next.js inclut un type spécial de page appelé **route API**, qui vous permet de faire des choses côté serveur telles que l'authentification, les webhooks, la lecture et l'écriture dans une base de données, et bien plus encore. De plus, nous aborderons certaines solutions comme Firebase qui ne nécessitent pas du tout de créer un backend !

### Stack à utiliser

* Next.js
* Stripe (en utilisant les routes API pour les webhooks)
* CMS (Contentful ou Sanity pour stocker les produits)

## Application de News/Communauté (Clone de Reddit)

Un clone de Reddit centré sur le partage de liens ou de posts très simples est une bonne étape au-dessus de notre application todo. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-3e6d6becfc.gif)
_Clone de Reddit, construit avec React_

Nous créons, mettons à jour et supprimons toujours des données, mais cette fois-ci, elles seront sauvegardées dans une base de données. Nous pourrions permettre aux utilisateurs d'ajouter différents types de contenu, comme une vidéo, un lien ou un court post. Nous pouvons utiliser Firebase pour notre projet afin de commencer, ce qui nous donnera la **base de données Firestore**. 

Notre base de données Firestore consistera en une collection simple qui sauvegardera tous les posts individuels qu'un utilisateur a créés. Nous pouvons la développer davantage en permettant à d'autres utilisateurs d'ajouter des commentaires et des likes aux posts. 

Une application encore plus développée inclurait une authentification. Heureusement, **Firebase Auth** la rend très facile. Nous pouvons également ajouter des likes aux commentaires individuels et des réponses aux commentaires pour nos fils de discussion. 

Nous pourrions utiliser n'importe quel framework React pour cela. Un bon choix serait celui utilisant un modèle **Vite**. Pour nos posts individuels, nous aurions besoin de routes dynamiques pour récupérer des posts individuels en fonction de leur identifiant. Un bon choix pour cela serait React Router.

### Stack à utiliser

* React (initialisé avec Vite)
* React Router (installer `react-router-dom`)
* Base de données Firestore (de Firebase)
* Firebase Auth

## Application de Chat (Clone de Discord)

Pour ajouter à notre application Reddit, nous pourrions en faire quelque chose comme Discord en affichant des messages en temps réel. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-bd75470d3f.gif)
_Clone de Discord, construit avec React_

Si nous changeons les posts en fils de discussion, nous avons maintenant une application de chat où c'est une conversation continue. 

Comme le clone de Reddit, les utilisateurs peuvent toujours ajouter n'importe quel type de média qu'ils aiment. Une bonne touche serait d'ajouter des aperçus de liens afin que lorsque l'utilisateur partage un lien, comme une vidéo YouTube, les autres utilisateurs puissent obtenir une petite carte qui affiche ce qui est réellement lié avec une image avant que l'utilisateur ne clique dessus. Il existe une bibliothèque appelée `react-tiny-link` qui vous permet de faire cela.

Nous pouvons toujours utiliser Firebase pour ce projet. C'est un bon cas d'utilisation pour la base de données en temps réel de Firebase afin de ne pas avoir à actualiser ou recharger la page pour voir les nouveaux messages. 

De plus, nous pouvons ajouter différents rôles à nos utilisateurs dans Discord. Dans la vraie application Discord, il y a des modérateurs avec des contrôles plus importants sur les autres utilisateurs. Une fonctionnalité exemple serait d'ajouter une fonction de bannissement pour retirer un utilisateur d'un canal ou d'une communauté donné.

### Stack à utiliser

* React (initialisé avec Vite)
* React Router (installer `react-router-dom`)
* `react-tiny-link`
* Base de données en temps réel de Firebase
* Firebase Auth

## Application de Messagerie (Clone de WhatsApp)

Une variante de ce type d'application en temps réel serait une application de messagerie comme celle de WhatsApp. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-4e59d05ac0.gif)
_Clone de WhatsApp, fait avec React_

Cette application serait un peu plus limitée dans le sens où les conversations sont généralement faites avec une seule personne, bien que ce ne soit pas obligatoire. Au lieu de parler dans des canaux, vous aurez différentes options pour parler avec une personne ou une autre à la fois. 

Une bonne touche serait d'ajouter des notifications lorsque quelqu'un vous envoie un message. C'est un autre exemple d'application qui nécessiterait une fonctionnalité de données en temps réel de votre base de données. Firebase est toujours une bonne option pour cela. 

Si Firebase devient ennuyeux, vous pourriez essayer Supabase, qui est une alternative très compétitive avec également des fonctionnalités de base de données en temps réel, mais qui est soutenue par Postgres au lieu de Firestore.

### Stack à utiliser

* React (initialisé avec Vite)
* React Router (installer `react-router-dom`)
* Supabase

## Application de Réseau Social (Clone de Twitter)

Et si, au lieu d'avoir une application où une personne parle directement avec une autre personne dans un espace très confiné, vous voulez l'inverse, où tout le monde peut interagir avec tout le monde ! 

Un excellent exemple de ce type d'application serait Twitter. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/twitter-gif.gif)
_Clone de Twitter, fait avec React_

Twitter est une application qui nécessite un fil d'actualité ainsi qu'une page de tendances dans le fil d'actualité d'un utilisateur. L'utilisateur pourra voir tous les posts des personnes qu'il suit. Mais sur la page des tendances, il verra tous les posts les plus populaires sur l'ensemble du site. 

Pour pouvoir déterminer quels posts sont les plus populaires, vous ajouterez la possibilité de "liker" (aimer) un post donné ainsi que de le re-partager, ce qui permet à un post d'être ajouté ou associé à un autre utilisateur. Enfin, vous voudrez permettre aux utilisateurs de répondre directement à d'autres posts (comme la fonctionnalité "quote tweet" de Twitter). 

Et une autre fonctionnalité fondamentale qui pourrait être ajoutée à chaque application que nous avons couverte jusqu'à présent est la recherche. Dans notre clone de Twitter, les utilisateurs voudraient probablement pouvoir rechercher différents utilisateurs à suivre ainsi que des posts en fonction de leur contenu. 

Un inconvénient de Firebase est qu'il ne dispose pas des meilleurs outils pour la recherche et qu'il n'est pas facile d'effectuer des requêtes basées sur un certain mot-clé. C'est l'une des instances où **Supabase** serait une alternative supérieure.

### Stack à utiliser

* React (initialisé avec Vite)
* React Router (installer `react-router-dom`)
* Supabase ou Firebase

## Application de Partage de Vidéos (Clone de YouTube/TikTok)

Le dernier projet amusant de cette liste est une application de partage de vidéos comme YouTube ou TikTok. 

Les deux applications ont des fonctionnalités très similaires, YouTube se concentrant principalement sur le contenu vidéo long format et TikTok consistant principalement en des vidéos super-courtes de moins d'une minute. 

Les deux plateformes utilisent une fonctionnalité de défilement infini, que vous fassiez défiler des vidéos suggérées ou recommandées. TikTok lui-même est arguably juste un grand fil d'actualité à défilement infini. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ezgif-4-b958b9f166.gif)
_Clone de Tiktok, fait avec React_

Ce qui serait le plus difficile à implémenter pour ces deux plateformes est l'algorithme. Vous pourriez aller très loin dans la construction d'une application qui repose simplement sur les utilisateurs suivant d'autres utilisateurs et ayant une page d'accueil avec les vidéos les plus populaires. Vos utilisateurs se verraient d'abord suggérer des vidéos des personnes qu'ils suivent, puis les vidéos populaires du site. 

La fonctionnalité la plus essentielle pour TikTok et YouTube est le streaming vidéo. Pour permettre aux utilisateurs de télécharger leur propre contenu, vous avez besoin d'un service qui inclut une API de téléchargement. Certains bons choix dans ce domaine sont **Cloudflare Stream**, Video.js ou Mux. 

Tous ces outils vous fournissent un lecteur vidéo ainsi qu'une API, qui gérera le téléchargement de vidéos qui pourraient ensuite être publiées sur le site. 

Je construirais personnellement cette application en utilisant mon propre serveur et ma propre base de données. Je choisirais probablement **Prisma** comme ORM (mappage objet-relationnel) pour interagir avec la base de données, qui serait une base de données **MySQL** gérée par Planetscale.

### Stack à utiliser

* Next.js (avec des routes API pour interagir avec la base de données)
* Le package `next-auth` (pour ajouter Google Auth, parmi d'autres fournisseurs d'authentification)
* Cloudflare stream ou Video.js (comme notre lecteur vidéo et pour héberger nos vidéos)
* Prisma (comme notre ORM)
* MySQL (géré par Planetscale)

## Devenez un Développeur React Professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul. 

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*