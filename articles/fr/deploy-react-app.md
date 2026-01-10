---
title: Comment déployer votre application React en utilisant Cloudflare Pages, Vercel
  et Netlify
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-11-28T21:30:24.000Z'
originalURL: https://freecodecamp.org/news/deploy-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/mugshotbot.com_customize_color-pink-image-9129875b-mode-dark-pattern-none-theme-two_up-url-https___gifcoins.io.png
tags:
- name: deployment
  slug: deployment
- name: React
  slug: react
seo_title: Comment déployer votre application React en utilisant Cloudflare Pages,
  Vercel et Netlify
seo_desc: "You have been working on a React application and now you're ready to actually\
  \ push it to the web. What services do you use to publish your site and make it\
  \ live to the world? \nWhether you're ready to release your website as a finished\
  \ product or you ..."
---

Vous avez travaillé sur une application React et vous êtes maintenant prêt à la publier sur le web. Quels services utilisez-vous pour publier votre site et le rendre accessible au monde entier ?

Que vous soyez prêt à lancer votre site web en tant que produit fini ou que vous soyez en cours de développement, couvrons 3 des meilleures (et gratuites !) façons de déployer votre application React dès maintenant.

## Comment déployer une application React avec Cloudflare Pages

L'une des nouvelles façons de déployer votre application React est avec Cloudflare Pages.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.41.27-PM.png)
_Cloudflare Pages_

Environ 20 % de tous les sites web utilisent Cloudflare pour diverses raisons, souvent pour des fonctionnalités gratuites telles que leur mitigation DDoS (attaque par déni de service).

Au cours des dernières années, il est entré dans l'espace de déploiement avec Pages. Les sites web hébergés sur Cloudflare Pages sont servis depuis le réseau edge de Cloudflare, qui est l'une des façons les plus rapides de servir votre site web aux utilisateurs dans le monde entier.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.47.53-PM.png)
_Le réseau edge de Cloudflare est l'un des plus rapides_

Pour commencer à utiliser Cloudflare Pages, tout ce dont vous avez besoin est un compte Cloudflare (gratuit).

Vous pouvez déployer votre site sur Pages en sélectionnant un dépôt Git depuis votre compte GitHub. Alternativement, vous pouvez pousser directement un dossier qui inclut toutes les ressources de votre site.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.20.19-PM.png)
_Options pour déployer sur Cloudflare Pages_

Ensuite, choisissez le framework que vous utilisez. Pages inclut des options pour React ainsi que Next.js.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.22.29-PM.png)
_Préréglages de framework pour Cloudflare Pages_

Pour terminer votre déploiement, il vous suffit de cliquer sur le bouton Deploy. Ensuite, votre site sera déployé sur leur réseau edge en quelques minutes !

Cloudflare Pages inclut des analyses web intégrées. Mais le meilleur avantage de déployer sur Cloudflare Pages est que vous pouvez déployer un nombre illimité de sites avec une bande passante illimitée gratuitement.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-1.04.33-PM.png)
_Tarification Cloudflare_

Il existe des niveaux Pro et Business, mais ceux-ci sont destinés aux clients qui souhaitent avoir plus de builds simultanés (pour construire plusieurs sites à la fois), plus de builds de sites par mois, et plus de domaines personnalisés.

## Comment déployer une application React avec Vercel

Vercel est une plateforme de déploiement construite par les mêmes personnes responsables du framework Next.js.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-1.10.53-PM.png)
_Plateforme de déploiement Vercel_

En conséquence, Vercel est optimisé pour les projets construits avec Next.js. Cependant, tout framework React que vous choisissez est supporté, y compris Create React App et Gatsby.

Parmi toutes les plateformes de déploiement, Vercel a les déploiements les plus rapides. Une application Next.js de taille moyenne se construit en un peu plus d'une minute.

Ce qui est puissant avec Vercel, c'est qu'ils ont un grand nombre d'intégrations qui rendent très facile la connexion avec une multitude d'autres services que vous utilisez probablement déjà ou que vous pourriez vouloir utiliser.

Les intégrations incluent des bases de données comme MongoDB ou PlanetScale ainsi que des outils CMS, des outils de surveillance et des outils de développement.

Comme Cloudflare Pages, Vercel inclut également un CDN mondial pour votre projet afin de livrer rapidement le contenu et les actifs de votre site, ainsi que des déploiements basés sur Git et des analyses intégrées.

Les analyses Vercel surveillent les performances de votre site web ainsi que le nombre d'utilisateurs sur votre site web de jour en jour.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-1.28.24-PM.png)
_Analyses Vercel_

Vercel a une interface minimale et propre pour gérer vos projets, qui est plus sophistiquée que celle de Cloudflare Pages.

Cependant, la tarification de Vercel peut être coûteuse si vous avez un projet commercial ou si vous utilisez plus de 100 gigaoctets de bande passante par mois. Dans ce cas, vous devez passer à leur plan Pro, qui est de 20 $ par mois.

## Comment déployer une application React avec Netlify

Netlify est une plateforme très similaire à Vercel, avec un certain nombre de fonctionnalités exclusives, telles que les formulaires et l'authentification.

Vercel et Netlify supportent tous les frameworks React, sont optimisés pour Next.js, ont un CDN intégré et les déploiements sont effectués via Git.

Netlify a un tableau de bord et une interface utilisateur tout aussi sophistiqués. Comme Vercel, Netlify propose un grand nombre d'intégrations à ajouter instantanément à votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.33.09-PM.png)
_Intégrations Netlify_

Netlify, cependant, a certaines fonctionnalités telles que Netlify Analytics qui sont facturées séparément. De plus, Netlify propose un service de formulaires qui vous permet de recevoir des soumissions de formulaires sans aucun code côté serveur ou JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screen-Shot-2022-11-24-at-12.34.20-PM.png)
_Formulaires Netlify_

Il inclut également d'autres solutions telles que l'authentification avec un service appelé Netlify Identity, qui est utile si vous souhaitez authentifier les utilisateurs sur votre site statique.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/premium-netlify-features.jpg)
_Fonctionnalités premium de Netlify_

Il propose également de nouvelles fonctionnalités comme le split-testing qui vous permettent de tester une fonctionnalité contre une autre sur votre site web.

En ce qui concerne la tarification, vous pouvez utiliser Netlify gratuitement même si vous avez un produit commercial. Si vous dépassez leur limite de 100 Go de la version gratuite, vous devrez passer à la version pro pour obtenir 1 To de bande passante.

Si vous voulez un accès illimité à des fonctionnalités telles que Netlify Forms et Identity, Netlify vous coûtera 99 $ par mois, ce qui inclut également 1,5 téraoctets de bande passante par mois. En bref, Netlify est très compétitif avec Vercel avec certaines fonctionnalités exclusives qui ont un prix.

## Merci d'avoir lu !

Espérons que cet article vous a donné un bon aperçu de ces différentes méthodes de déploiement afin que vous puissiez déployer votre application React en un rien de temps.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*