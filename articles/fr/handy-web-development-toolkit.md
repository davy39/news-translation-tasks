---
title: 10 outils populaires de développement web que tout programmeur devrait connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-06T19:37:00.000Z'
originalURL: https://freecodecamp.org/news/handy-web-development-toolkit
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/screely-1586183781361.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: web
  slug: web
- name: Web Development
  slug: web-development
seo_title: 10 outils populaires de développement web que tout programmeur devrait
  connaître
seo_desc: 'By Mehul Mohan

  Are you planning to get into web development? Take a tool with you, it''s scary
  out there. Let''s take a look at some common web development tools that''ll help
  you speed up your workflow and be a better web developer.

  Note that your mile...'
---

Par Mehul Mohan

Prévoyez-vous de vous lancer dans le développement web ? Prenez un outil avec vous, c'est effrayant là-bas. Jetons un coup d'œil à quelques outils courants de développement web qui vous aideront à accélérer votre flux de travail et à devenir un meilleur développeur web.

Notez que votre expérience peut varier considérablement. Cet article liste simplement les solutions les plus populaires disponibles. Vous devez encore les intégrer dans vos projets et en apprendre davantage à leur sujet.

Cela étant dit, voici une liste des outils/packages les plus courants que j'utilise régulièrement dans mes flux de travail.

## #1 VSCode 💻

VSCode n'a pas besoin d'introduction. C'est un éditeur de code beau et puissant qui supporte les extensions, le terminal intégré, les extraits de code, les thèmes, les raccourcis, le SSH distant, et bien plus encore - selon vos besoins.

Fonctionnant sur electron, il est compatible multi-OS et est constamment amélioré par Microsoft en tant que [projet open source](https://github.com/microsoft/vscode). VSCode vient avec un ensemble riche d'outils, IntelliSense via le protocole Language Server, et des corrections/fixes rapides tout au long de l'année.

![VSCode](https://code.visualstudio.com/assets/home/home-screenshot-mac-2x.png)


Obtenez VSCode maintenant depuis le site officiel [VSCode](https://code.visualstudio.com/).

## #2 Webpack 📦

Webpack se présente comme un bundler de modules, mais en réalité, il est beaucoup plus extensible que cela. Vous pouvez attacher une pléthore de plugins et ajuster sa configuration pour le rendre plus robuste et adapté à vos besoins.

Webpack 4 arrive comme un **bundler de modules sans configuration** - cela signifie que vous pouvez commencer avec Webpack presque immédiatement ! Vous n'avez qu'à télécharger le module en utilisant `npm i webpack` et puis exécuter `npx webpack` dans votre répertoire. Voici comment configurer la configuration zéro avec webpack :

%[https://www.youtube.com/watch?v=g9_91gUHy6k]

## #3 Cypress 🧪

Cypress est un excellent outil de test e2e qui peut effectivement lancer une fenêtre Chrome headless ou complète pour exécuter des tests réels de votre code. Il peut interagir avec du code asynchrone de manière très intuitive. Par exemple, il attend que les ressources se chargent/deiennent disponibles, contrairement à Selenium, qui est une technologie assez ancienne conçue pour les tests automatisés de sites principalement statiques. Voyons comment Cypress fonctionne à travers une courte vidéo :

%[https://vimeo.com/237527670]

Les tests Cypress sont très simples et conviviaux à écrire, et il fait tout le travail lourd hors de la boîte (comme lancer une instance Chrome, des événements clavier appropriés, des émetteurs d'événements fiables, vous l'appelez). Obtenez Cypress [ici](https://www.cypress.io/).

## #4 TypeScript 📝

Écrire du JavaScript simple ? Cela peut être vraiment douloureux de trouver des bugs et des erreurs subtils sans un linting approprié. Pour le rendre encore plus puissant avec une meilleure vérification des types et une autocomplétion des modules, prenez TypeScript avec vous.

TypeScript est un sur-ensemble de JavaScript qui se transpile en JavaScript avant l'exécution. Cela signifie que vous obtenez JavaScript qui s'exécute comme avant, mais avec l'avantage supplémentaire de développement de coder JS de manière plus 'stricte'.

Il ne serait pas faux de dire que TypeScript permet vraiment une maintenance utile de la base de code JavaScript et rend le refactoring facile. Vous pouvez commencer à apprendre TypeScript à travers leur [documentation officielle](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html).

## #5 Sentry 🚨

Sentry est un service de rapport d'erreurs pour la production. Bien des fois, surtout sur le front-end, vos utilisateurs peuvent rencontrer des plantages ou des bugs inattendus.

J'utilise personnellement Sentry pour [codedamn](https://codedamn.com), et j'ai corrigé quelques bugs méchants et causes de plantages qui étaient rares et qui étaient arrivés à des utilisateurs très spécifiques lors d'actions très spécifiques prises sur la plateforme.

En bonus, Sentry existe sur beaucoup de plateformes, et n'est pas seulement restreint aux environnements d'exécution JavaScript. Cela signifie que Sentry peut être utilisé avec presque n'importe quelle pile technologique populaire.

Sentry envoie la trace complète de la pile/informations sur le bug directement dans votre tableau de bord afin que vous puissiez corriger ce bug méchant lors du prochain cycle de publication. Lisez à propos de [Sentry ici](https://sentry.io).

%[https://player.vimeo.com/video/340759078]

## #6 Git 🌿

Git est la baguette magique de tout grand projet. Git est un système de contrôle de version (VCS) qui vous permet de construire votre logiciel de manière incrémentielle, tout en maintenant une diff complète des builds précédents. Cela signifie que vous ne perdez aucun historique et pouvez facilement revenir au dernier point de travail.

Non seulement cela, vous pouvez créer une branche et travailler sur quelque chose de complètement différent, sans affecter le projet original. Ce concept est appelé branches dans git. Il y a tellement plus à apprendre sur git. J'adore cette série de thenewboston sur git. Jetez un coup d'œil :

%[https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAKWClAD_iKpNC0bGHxGhcx]

La solution la plus populaire pour héberger les dépôts git est GitHub. Il offre des dépôts publics et privés gratuits. Vous pouvez en apprendre plus sur git [ici](https://git-scm.com/).

## #7 Babel 🐠

Babel vous permet d'écrire des fonctionnalités JavaScript de pointe, mais ensuite de les transpiler pour les navigateurs dans un standard que ces navigateurs connaissent et ont implémenté depuis des années.

Utiliser Babel avec Webpack est une combinaison très puissante qui vous permet d'utiliser des fonctionnalités de pointe et ensuite de les bundler/minifier ensemble. Cela offre la meilleure expérience pour les développeurs lors du développement d'applications ainsi que pour servir des builds minifiées aux utilisateurs pour la vitesse et la performance.

Par exemple, vous pouvez écrire du code ES2020 dans Babel et le laisser transpiler en version ES2015 pour le livrer aux navigateurs. Cela rend l'écriture de JavaScript vraiment amusante et pratique car cela vous permet d'utiliser JavaScript du futur ! Apprenez-en plus sur Babel [ici](https://babeljs.io/).

## #8 Material UI ⭐

Material UI est une spécification de Google sur la façon dont les mises en page doivent être créées. Sur la base de Material UI, il existe de nombreuses bibliothèques de composants disponibles pour un certain nombre de frameworks comme Angular, React ou React Native. Certaines bibliothèques de composants incluent :

1. [Material UI - React](https://material-ui.com/)
2. [React Native paper](https://callstack.github.io/react-native-paper/)
3. [Vuetify](https://github.com/vuetifyjs/vuetify)
4. [Angular Materials](https://github.com/angular/components)

Cela facilite le processus de construction de nombreux composants manuellement pour les développeurs. Et en même temps, cela leur fournit des composants rapides et bien conçus. Apprenez-en plus sur Material UI [ici](https://material-ui.com/).

## #9 Joi 🛡️

La validation des données est une partie importante de toute application. Cela est dû au fait que vous ne pouvez jamais faire confiance aux données provenant d'un utilisateur. Pour les applications à grande échelle avec plusieurs points de terminaison pour atteindre le serveur backend, il peut devenir très délicat de gérer tous les cas limites.

Joi est une bibliothèque très pratique qui vous aide à valider toutes les données entrantes via un schéma prédéfini strict. Joi vous permet de construire des schémas pour les tableaux, les objets et même les valeurs qu'ils doivent accepter.

Si l'entrée échoue, il vous permet également de personnaliser les messages d'erreur. Plus de tracas avec `obj && typeof obj === 'string'` dans votre code ! Utiliser le schéma de Joi n'est pas seulement sûr mais rend également votre code beaucoup plus lisible pour les autres développeurs. Apprenez-en plus sur Joi [ici](https://github.com/hapijs/joi).

## #10 Docker 🐳

Configurer Docker pour le développement vient avec son propre ensemble de défis (parlant d'expérience). Mais une fois fait, cela vaut l'investissement. Partiellement parce que vous supprimez les erreurs "ça-marche-sur-ma-machine".

Mais aussi, exécuter du code en bac à sable a un autre avantage. Dans l'éventualité malheureuse où votre application web est piratée ou mise hors ligne, le conteneur Docker s'assurerait que l'attaque est contenue à ce conteneur particulier et qu'aucun autre service n'est affecté (sauf, bien sûr, si votre conteneur a des règles de sécurité médiocres).

Vous pouvez commencer avec Docker aujourd'hui ! Commencez avec cette playlist :

%[https://www.youtube.com/watch?v=avsJnrdN-YU&list=PLYxzS__5yYQlzv9_z1eZmZY8dzMlQFbaH&index=2&t=0s]

# Conclusion

Le web est vaste, et si vous commencez tout juste, cela peut être accablant ! Obtenez de l'aide de la part d'autres développeurs qui ont été dans vos chaussures. Vous pouvez même me contacter sur [twitter](https://twitter.com/mehulmpt) / [instagram](https://instagram.com/mehulmpt) et vous connecter. Je serai heureux de vous aider.

Souhaitez-vous apprendre le développement web et d'autres langages de programmation d'une manière complètement nouvelle ? Rendez-vous sur une [nouvelle plateforme pour les développeurs](https://codedamn.com) sur laquelle je travaille pour l'essayer aujourd'hui !