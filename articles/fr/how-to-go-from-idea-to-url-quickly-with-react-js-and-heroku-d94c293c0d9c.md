---
title: Comment passer rapidement de l'idée à l'URL avec React.js et Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-29T20:37:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-go-from-idea-to-url-quickly-with-react-js-and-heroku-d94c293c0d9c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jkZododShDg7lPnGsLnAig.jpeg
tags:
- name: Heroku
  slug: heroku
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment passer rapidement de l'idée à l'URL avec React.js et Heroku
seo_desc: 'By Tom Schweers

  When I was first starting out as a developer, the one thing that I wanted to do
  was get a web application live. I wanted it online for the world to see. I didn’t
  care about how it looked, what features it had, or even if anyone would ...'
---

Par Tom Schweers

Lorsque j'ai commencé en tant que développeur, la seule chose que je voulais faire était de mettre une application web en ligne. Je voulais qu'elle soit accessible au monde entier. Peu m'importait son apparence, ses fonctionnalités ou même si quelqu'un la verrait ou l'utiliserait. Mon seul désir était de comprendre l'ensemble du processus de bout en bout. Je voulais savoir comment un ensemble de fichiers et de dossiers se transformait en une application vivante et fonctionnelle sur Internet.

N'ayant pas de formation en ingénierie, je n'avais aucune idée de comment tout cela fonctionnait. Tout ce que je savais, c'était coder quelques trucs dans [JSFiddle](https://jsfiddle.net/) ou quelque chose de similaire. Je savais comment créer de jolies petites fonctionnalités front-end pour mes clients. Mon expérience réelle se limitait à la configuration d'applications SaaS, ce qui est de la programmation au sein d'une application préconstruite. Naturellement, je voulais aller plus loin…

![Image](https://cdn-media-1.freecodecamp.org/images/bCLG403cH58CiDpN0wgid7HrpjABMOQX9oSW)
_Inception (2010)_

En résumé, j'écris cet article pour ceux d'entre vous qui se trouvent dans une situation similaire. Pour quelqu'un qui veut une méthode simple et facile pour mettre son application en ligne. Cela vous permet de vous concentrer sur le développement des fonctionnalités, et non sur l'infrastructure.

### Pour commencer

Il existe de nombreuses [boilerplates](https://stackoverflow.com/questions/3992199/what-is-boilerplate-code). Selon mon expérience, elles peuvent être un peu trop compliquées, surtout pour les développeurs novices. J'ai essayé le starter app de Vue.js, l'application MEAN stack, et même [create-react-app](https://github.com/facebook/create-react-app). Toutes ont nécessité quelques ajustements pour atteindre un point où je serais à l'aise pour commencer le développement réel de mon application. Cependant, j'ai trouvé que create-react-app de Facebook était le plus facile à configurer. Ma boilerplate était initialement dérivée de celle-ci.

#### React-Boilerplate

J'ai initialement créé [react-boilerplate](https://github.com/tomschweers/react-boilerplate) juste pour moi. Ensuite, j'ai pensé que si d'autres la trouvaient utile, ce serait encore mieux. Donc, si vous suivez ce guide, naviguez vers le lien ci-dessus qui vous mènera à mon dépôt GitHub.

La première chose (et la plus facile) que vous pouvez faire ici est de faire défiler jusqu'en bas de la page et de cliquer sur le bouton **Deploy to Heroku**.

![Image](https://cdn-media-1.freecodecamp.org/images/kfyJ0NCfbSN1fgmrbenZBJTG3Q80tWwJCgYC)

Heroku vous demandera d'abord de créer un compte si vous n'en avez pas déjà un. Allez-y et faites-le, vous ne le regretterez pas (et c'est gratuit). Après cela, vous obtiendrez un écran vous invitant à créer une nouvelle application.

![Image](https://cdn-media-1.freecodecamp.org/images/Q6wMpXwEXMxKlO4QFGjeyZyDqBEkTW81AJIl)

Saisissez un nom pour votre application. Le nom doit être unique sur l'ensemble de la plateforme Heroku, et non seulement sur votre compte. Ensuite, cliquez sur **Deploy app**.

#### Heroku

Si vous n'êtes pas familier avec Heroku, il s'agit d'une application PaaS qui s'occupe de tout ce qui se passe en coulisses pour vous. Heroku rend les processus de déploiement, de configuration, de mise à l'échelle, d'optimisation et de gestion des applications aussi simples et directs que possible.

> Heroku est une plateforme cloud qui permet aux entreprises de créer, livrer, surveiller et mettre à l'échelle des applications - nous sommes le moyen le plus rapide de passer de l'idée à l'URL, en contournant tous ces maux de tête d'infrastructure.

En suivant les instructions ci-dessus, vous venez de déployer avec succès une application sur Internet. Pour voir votre application, allez dans l'onglet **_Settings_** et faites défiler jusqu'à la section **_Domains and certificates_**. Vous y verrez un lien vers votre application en direct.

![Image](https://cdn-media-1.freecodecamp.org/images/4nrfdfqHZOVOcDx8fdcITkWRjSyhFtFkH3qr)

#### Fonctionnalités de l'application

Maintenant, vous auriez pu faire cela avec n'importe quelle application de démarrage [boilerplate]. En utilisant [react-boilerplate](https://github.com/tomschweers/react-boilerplate), vous avez quelques fonctionnalités notables prêtes à l'emploi. Je voulais inclure le strict minimum pour que ce soit facile à comprendre, mais suffisamment pour pouvoir commencer rapidement sur de futures idées.

1. La structure des dossiers est organisée et facile à comprendre. L'application a été construite spécifiquement pour lancer un projet rapidement. Il n'y a pas trop de bloat et la structure des composants est logique. Plus d'informations sur la construction de composants ci-dessous.
2. [**React-Sidebar**](https://github.com/balloob/react-sidebar). Ce menu latéral est réactif, moderne et optimisé pour la navigation mobile. Ouvrez l'[application de démonstration](https://react-boilerplate-sidenav.herokuapp.com/) sur votre téléphone et essayez de faire glisser le menu fermé avec votre doigt ; alternativement, vous pouvez appuyer à l'extérieur du menu. C'est de loin la meilleure barre latérale que j'ai trouvée pour React.js.
3. [**React-FontAwesome**](https://github.com/FortAwesome/react-fontawesome). Ce package vous fournit de belles icônes SVG scalables et gratuites pour votre application React.js. Consultez mon [site web personnel](https://www.tomschweers.com/) pour voir quelques-unes d'entre elles en direct dans le coin supérieur droit. J'ai ajouté le package à la boilerplate, mais il n'importe aucune icône. Tout ce que vous avez à faire est de décommenter le code dans le fichier App.js pour commencer à importer.
4. [**Depcheck**](https://github.com/depcheck/depcheck). Il s'agit d'un outil en ligne de commande utilisé pour scanner votre application à la recherche de dépendances inutilisées. Il vous indiquera quels packages ne sont pas utilisés afin que vous puissiez les supprimer. Je trouve cela extrêmement utile lors de l'expérimentation avec des packages JavaScript. Mon esprit sporadique importera des packages toute la journée, les abandonnant une fois que je réalise qu'ils ne font pas exactement ce que je veux.

![Image](https://cdn-media-1.freecodecamp.org/images/5np5eecjCC4F67vJmLv2Yu6D6BSrBoLLVCim)
_Site de démonstration React Boilerplate_

Et c'est tout ! Consultez le README.md dans mon dépôt pour plus d'informations sur les fonctionnalités ou comment les configurer.

#### Téléchargement du code

Heroku fournit un moyen très simple d'obtenir le code source de l'application que vous venez de déployer. Il vous suffit de suivre les instructions dans l'onglet **_Deploy_** à l'intérieur de votre application en utilisant le CLI Heroku.

![Image](https://cdn-media-1.freecodecamp.org/images/C2IitCM3kgKrBFigp4KJHvTm7XJaqI-FLtnL)

Alternativement, si vous préférez ne pas utiliser le CLI Heroku, vous pouvez cloner ou télécharger le dépôt [react-boilerplate](https://github.com/tomschweers/react-boilerplate) directement depuis GitHub et créer un nouveau dépôt vous-même. Ensuite, changez la **_Méthode de déploiement_** en **_GitHub_** et recherchez votre nouveau dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/kYAHF8up8D1cpfnmnvxz1n-CDnKrbTyqWTyY)

Vous pouvez également activer les déploiements automatiques. Lorsque vous poussez des commits vers votre dépôt, votre site Heroku se mettra à jour automatiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/vmSzWgtYh4nrG1SRGko8dUkKeHoaAe5NeU7E)

#### Ajout de pages et de composants

À ce stade, vous devriez avoir votre propre dossier de fichiers connecté à votre application Heroku. La création de pages et de composants est vraiment simple et je vais vous montrer comment faire. Ce tutoriel suppose que vous connaissez les bases de [ES6](http://es6-features.org/#Constants) et de [React.js](https://reactjs.org/). Les captures d'écran sont de mon éditeur de texte - [Visual Studio Code](https://code.visualstudio.com/) (fortement recommandé).

Tout d'abord, naviguez vers le fichier **_Home.js_**.

![Image](https://cdn-media-1.freecodecamp.org/images/V10TFQtfUVIyZc1IuXn8FVUO9XmvZmWt31ic)

Ici, vous pouvez apporter des modifications à votre page d'accueil. Comme vous pouvez le voir, j'importe un composant **_Clock_** comme exemple. Je garde les petits composants qui constituent les pages de l'application dans le dossier **_subcomponents_**. 

![Image](https://cdn-media-1.freecodecamp.org/images/uH0KutnL7CC2858tLqdq5vikk9qKZEYgmXAD)

Les sous-composants sont les blocs de construction réutilisables de vos pages. Placez les boutons, les tableaux, les graphiques, les animations, les formulaires et autres composants réutilisables dans ce dossier. Construisez vos pages dans le dossier **_pages_** et importez-les dans **_MainRouter.js_**. 

![Image](https://cdn-media-1.freecodecamp.org/images/uBPSU-y84ZAO5Mgy0hdOnGOuFpTJyH2bnqaa)

Ce fichier est ce qui route vos fichiers **_pages_** vers les chemins d'URL spécifiés. Vous pouvez nommer vos chemins d'URL comme vous le souhaitez, j'ai simplement ajouté quelques chemins d'exemple pour démontrer. Après cela, ajoutez des liens vers vos pages dans le fichier **_SideBarContent.js_** afin que vos utilisateurs puissent naviguer entre elles.

![Image](https://cdn-media-1.freecodecamp.org/images/w4fsEPuSniRckp7BOthlir0JE873iMnCWN2i)

Et c'est tout !

Ces liens apparaîtront maintenant dans la navigation de la barre latérale de votre application et seront routés vers les pages que vous avez spécifiées ci-dessus. Pour ajouter une nouvelle page à votre application, vous n'avez besoin que de suivre ces trois étapes simples. Les fichiers **_App.js_** et **_SideBarPanel.js_** n'ont pas besoin d'être modifiés et vous pouvez vous concentrer sur la construction du contenu réel de votre application.

### Conclusion

Vous disposez maintenant d'une application de développement entièrement fonctionnelle avec une navigation et un routage optimisés pour le bureau et le mobile. Vous pouvez maintenant construire des composants et des pages sans vous soucier de la structure de l'application. Montrez votre application web à n'importe qui en lui envoyant simplement le lien Heroku personnalisé.

L'étape suivante consiste à configurer un nom de domaine personnalisé et à préparer l'application pour le trafic réel. Faites-moi savoir dans les commentaires si vous avez trouvé ce tutoriel utile ou si vous avez des questions.