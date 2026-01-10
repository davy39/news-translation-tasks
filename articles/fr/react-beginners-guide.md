---
title: Le guide du débutant React pour 2022
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-01-10T21:15:23.000Z'
originalURL: https://freecodecamp.org/news/react-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-10-at-3.24.37-PM.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Le guide du débutant React pour 2022
seo_desc: 'So you''re ready to dive into learning React, but you still have some lingering
  questions, such as:


  How should I create my React projects?

  What tools should I add to my React app?

  Do I need to learn JavaScript first before learning React?

  Where shoul...'
---

Vous êtes prêt à plonger dans l'apprentissage de React, mais vous avez encore quelques questions en suspens, telles que :

* _Comment dois-je créer mes projets React ?_
* _Quels outils dois-je ajouter à mon application React ?_
* _Dois-je d'abord apprendre JavaScript avant d'apprendre React ?_
* _Où dois-je déployer mes projets ?_

Si vous cherchez des réponses à l'une de ces questions (ou plus), ce guide simple et complet a été fait pour vous.

Il vous donnera tout ce dont vous avez besoin pour commencer à apprendre et à utiliser React, sans avoir à assembler des dizaines de tutoriels pour débutants obsolètes.

[Cliquez ici](https://www.reactbootcamp.com/cheatsheets) pour télécharger l'aide-mémoire au format PDF.

Il inclut toutes les informations essentielles de cet article sous forme de guide PDF pratique.

Commençons !

## Table des matières

* [Qu'ai-je besoin d'installer sur mon ordinateur pour utiliser React ?](#heading-quest-ce-que-je-dois-installer-sur-mon-ordinateur)
* [Comment dois-je créer mes projets React ?](#heading-comment-creer-mes-projets-react)
* [Quels concepts React dois-je vraiment apprendre ?](#heading-quels-concepts-react-dois-je-vraiment-apprendre)
* [Dois-je apprendre toutes les fonctionnalités de React ?](#heading-dois-je-apprendre-toutes-les-fonctionnalites-react)
* [Dois-je apprendre JavaScript avant React ?](#heading-dois-je-apprendre-javascript-avant-react)
* [Quelles bibliothèques React dois-je utiliser ?](#heading-quelles-bibliothèques-react-dois-je-utiliser)
* [Où dois-je déployer mes projets React ?](#heading-ou-deployer-mes-projets-react)
* [Où dois-je apprendre React ?](#heading-ou-apprendre-react)

## Qu'ai-je besoin d'installer sur mon ordinateur ?

Pour construire des projets React à grande échelle sur votre ordinateur, il y a quelques outils essentiels dont chaque développeur a besoin :

* [Node / NPM](https://nodejs.org) (je recommande d'installer la version "LTS")
* Un bon éditeur de code (je recommande [Visual Studio Code](https://code.visualstudio.com))
* Git (installez-le sur [Git-SCM.com](https://git-scm.com/) et créez un compte gratuit sur [Github.com](https://github.com))

**Node** est défini comme un environnement d'exécution JavaScript. Lorsqu'il est combiné avec un gestionnaire de paquets comme **NPM** (que vous obtenez en même temps que Node), il sert d'outil puissant pour gérer facilement les bibliothèques dans vos projets React.

Sans Node et NPM, si vous vouliez ajouter une nouvelle bibliothèque JavaScript à votre projet React (comme [day.js](https://day.js.org/), une bibliothèque utilisée pour formater les dates), vous devriez ajouter manuellement un ensemble de balises `<script>` et les gérer vous-même.

Avec Node et NPM (ou un autre gestionnaire de paquets comme Yarn), nous pouvons simplement exécuter une commande pour installer n'importe quelle bibliothèque JavaScript que nous aimons. Pour installer day.js, nous exécuterions :

```bash
npm install dayjs
```

Et NPM récupérera automatiquement le code de cette bibliothèque et l'ajoutera à notre dossier `node_modules` ✨

**Note** : Node / NPM n'est pas requis pour créer un projet React. Mais il vous permet d'utiliser des outils utiles comme [Create React App](https://create-react-app.dev/) et [Next.js](https://nextjs.org) qui rendent la gestion de vos applications React beaucoup plus facile.

Un bon éditeur de code est également essentiel pour pouvoir :

* Gérer facilement tous les fichiers et dossiers dans notre projet React
* Fournir une coloration syntaxique pour styliser notre code et le rendre plus facile à lire
* Exécuter des commandes pour développer, tester et construire notre projet en utilisant un terminal intégré
* Installer des extensions pour fournir des fonctionnalités supplémentaires utiles

**Visual Studio Code** (ou [VSCode](https://code.visualstudio.com)) fait tout cela et possède de excellents paramètres par défaut pour le développement React, en plus d'être entièrement gratuit.

Enfin, **Git** et **GitHub** sont essentiels pour sauvegarder les modifications que vous apportez à vos projets React. Git vous donne un "contrôle de version", un nom sophistiqué pour un outil qui vous permet de sauvegarder votre code et de restaurer les sauvegardes précédentes si nécessaire.

GitHub est également essentiel car il nous permet de sauvegarder tout notre code à distance, c'est-à-dire sur notre compte GitHub. Vous pouvez sauvegarder votre code et les modifications que vous y avez apportées avec Git, puis "pousser" toutes ces modifications vers votre compte GitHub.

En conséquence, GitHub sert à la fois de sauvegarde utile pour tout le travail que nous avons effectué sur nos projets React et d'une manière essentielle pour que les autres voient notre code et y apportent des modifications également.

## Comment dois-je créer mes projets React ?

Si vous commencez un nouveau projet React, vous n'aurez jamais besoin de créer vos propres fichiers, dossiers et fichier package.json (où vous listez toutes les bibliothèques de votre projet).

Il existe trois excellents outils qui vous aideront à générer immédiatement un nouveau projet React avec une seule commande.

* Create React App
* Vite
* Next.js

Une fois que vous avez installé Node / NPM (voir le début de l'article), vous pouvez utiliser l'un de ces outils pour créer un nouveau projet React avec les commandes suivantes :

```bash
# pour Create React App
npx create-react-app mon-application-react

# pour Vite
npm init vite@latest mon-application-react --template react 

# pour Next.js
npx create-next-app
```

**Create React App** est une méthode bien établie et fiable pour créer un nouveau projet React et vous donne des outils et scripts essentiels pour exécuter, développer et construire votre projet pour le déploiement.

Create React App utilise Babel et Webpack pour transpiler et bundler votre code (en bref, pour le rendre exécutable dans le navigateur).

De plus, il fournit de excellents outils de développement comme ESLint pour "lint" votre code, ou pour vous informer des problèmes dans le code que vous avez écrit au fur et à mesure que vous l'écrivez.

**Vite**, en revanche, utilise un bundler différent de Create React App. Au lieu d'utiliser Webpack, il utilise un bundler appelé ESBuild, qui est des ordres de grandeur plus rapide.

En bref, Vite (français pour "rapide" ou "rapidement"), est une alternative plus récente et plus rapide à Create React App.

Sachez que l'un de ces outils est différent des autres, à savoir **Next.js**.

Il est worth de mentionner que Next.js est un _framework_ React, ce qui signifie qu'il s'agit d'une méthode "tout compris" pour construire des applications React et inclut une tonne de fonctionnalités qui ne font pas partie de React lui-même.

La raison pour laquelle j'ai inclus Next.js est qu'il s'agit probablement du moyen le plus rapide et le plus facile de créer une application React. Une fois que vous connaissez les bases de React, vous verrez comment les fonctionnalités de Next vous permettent de construire des applications React plus complètes, plus rapidement.

Mais que faire si vous voulez quelque chose de plus petit sans avoir à créer des dossiers, des fichiers et installer des dépendances sur votre ordinateur ?

**Note** : les dossiers node_modules peuvent souvent contenir littéralement des milliers de dossiers pour les dépendances et les dépendances peer de vos projets, ce qui peut collectivement prendre plusieurs gigaoctets d'espace sur votre ordinateur !

Une excellente façon de lancer un projet React est de le faire dans le navigateur, et il existe un certain nombre de services gratuits qui vous permettent de le faire instantanément. ⚠️

Deux services de sandbox qui peuvent créer des projets React dans le navigateur incluent :

* [CodeSandbox](https://codesandbox.io)
* [Stackblitz](https://stackblitz.com)

Ceux-ci sont parfaits à utiliser lorsque vous suivez un tutoriel ou si vous voulez tester un peu de code à la volée.

J'ai trouvé que la façon la plus rapide de créer un nouveau projet React est d'aller à l'adresse [react.new](https://react.new). C'est vrai – vous pouvez créer un tout nouveau projet React en quelques secondes sans exécuter une seule commande !

## Quels concepts React dois-je vraiment apprendre ?

React a une tonne de nouveaux concepts qui nous donnent une nouvelle façon de penser à la construction d'applications sur le web et en général.

Si vous n'avez pas d'expérience dans la construction d'applications React de première main, comment savez-vous quels concepts et fonctionnalités de la bibliothèque vous aurez besoin ?

La bonne chose est que vous n'aurez pas besoin de tous. En fait, lorsque vous commencez à construire des projets React, vous constaterez que vous utilisez les mêmes fonctionnalités pour 90 % de votre travail.

Pour quelqu'un qui travaille dans React quotidiennement, ceux-ci incluent :

* JSX
* Composants (spécifiquement les composants de fonction)
* Props et état
* Listes, clés et événements
* Hooks React principaux, principalement `useState`, `useEffect`
* Contexte React, y compris `useContext`
* Comment écrire des hooks React personnalisés

Il est également essentiel de connaître les bases du fonctionnement de React et les problèmes qu'il a été créé pour résoudre. Ces concepts incluent :

* Rendu et re-rendu (surtout en sachant ce qui peut causer un re-rendu)
* Fonctions pures
* Effets secondaires
* Immuabilité

Enfin, je crois qu'il vaut la peine de se familiariser au moins avec les composants de classe React. Avec les hooks, nous avons largement basculé vers l'utilisation de composants de fonction. Cependant, vous rencontrerez des composants de classe, surtout si vous travaillez sur une base de code plus ancienne.

Si vous voulez une liste complète, j'ai résumé tous les principaux concepts React que je crois que chaque développeur devrait connaître dans une aide-mémoire pratique. Vous pouvez la trouver ici :

[L'aide-mémoire React (+ Exemples du Monde Réel)](https://www.freecodecamp.org/news/react-cheatsheet-with-real-world-examples/)

## Dois-je apprendre toutes les fonctionnalités / concepts / hooks React ?

Non, vous n'avez pas besoin. Concentrez-vous sur les principaux concepts que je mentionne dans la question ci-dessus.

En fait, de nombreux hooks et fonctionnalités React sont rarement utilisés même parmi les développeurs les plus experts. Le simple fait qu'ils existent ne signifie pas que vous allez en avoir besoin et vous n'avez pas besoin de passer autant de temps à apprendre chaque concept React.

Par exemple, j'utilise React quotidiennement et je peux compter sur les doigts d'une main le nombre de fois où j'ai eu besoin du hook `useLayoutEffect` (un hook React plus obscur).

## Dois-je apprendre JavaScript avant React ?

Puisque React est fondamentalement une bibliothèque JavaScript qui se targue d'être "juste JavaScript", si vous allez apprendre React, vous devrez éventuellement devenir bon en JavaScript également.

J'ai personnellement appris JavaScript avant d'essayer d'apprendre React et je crois que cela m'a grandement aidé. Bien que beaucoup d'autres aient affirmé qu'il est possible de simplement "commencer" avec React, vous êtes finalement plongé dans un monde rempli de JavaScript.

Cela dit, plus vous devenez bon en JavaScript, meilleur vous deviendrez dans la construction de choses en React. Vous pouvez apprendre les deux simultanément et, en fin de compte, tous les développeurs React apprennent encore JavaScript, pour ainsi dire.

En bref, vous pouvez commencer à apprendre React sans être le meilleur en JavaScript, cependant, ne vous amusez pas avec l'idée que vous pouvez entièrement reporter l'apprentissage de JavaScript.

Si vous voulez savoir exactement quelles compétences JavaScript vous utiliserez en tant que développeur React, assurez-vous de consulter cet article :

[Les compétences JavaScript dont vous avez besoin pour React](https://www.freecodecamp.org/news/javascript-skills-you-need-for-react-practical-examples/)

## Quelles bibliothèques React dois-je utiliser ?

Il existe des milliers de bibliothèques React qui peuvent être utilisées dans vos projets React.

React est une bibliothèque non opinionnée, pas un framework. Beaucoup des outils qui seront nécessaires pour construire vos projets ne sont simplement pas disponibles dans React.

React ne fournit pas sa propre solution pour écrire des styles, animer des composants, gérer l'état global de l'application, ou créer des routes ou des pages.

Pour construire un projet React significatif, vous devrez vous familiariser avec diverses bibliothèques pour vous donner la fonctionnalité dont vous avez besoin.

Je pourrais écrire une série d'articles sur les bibliothèques React que je crois être les meilleures et pourquoi, mais voici ma liste personnelle :

* Pour la gestion d'état, utilisez **Zustand** (Redux est toujours bon avec Redux Toolkit)
* Pour le style, utilisez **TailwindCSS**
* Pour le routage, utilisez **React Router** (React Location est également prometteur)
* Pour la récupération de données, utilisez **React Query**
* Pour les formulaires, utilisez **React Hook Form**

Si vous voulez une liste des bibliothèques qui valent la peine d'être utilisées pour la plupart de vos projets React, consultez cet article :

[5 bibliothèques React dont chaque projet a besoin](https://www.freecodecamp.org/news/5-react-libraries-every-project-needs/)

## Où dois-je déployer mes projets React ?

Heureusement, ma réponse à cette question est similaire aux autres – il existe de nombreuses excellentes options pour déployer votre projet React.

Si vous déployez un projet React qui a été créé en utilisant l'outil Create React App ou avec l'outil de construction Vite, votre projet construit consistera en des fichiers HTML, CSS et JavaScript simples.

Cela signifie que votre projet peut être déployé sur n'importe quel service capable d'héberger des actifs statiques comme ceux-ci, tels que :

* [Surge](https://surge.sh/)
* [Github Pages](https://pages.github.com/)
* Même un bucket AWS S3 peut héberger votre site React

Il existe de nombreuses options parmi lesquelles choisir, mais je vous recommande vivement de déployer votre application sur l'un de ces services :

* [Netlify](https://netlify.com)
* [Vercel](https://vercel.com) (meilleur pour Next.js)
* [Cloudflare Pages](https://pages.cloudflare.com)

J'ai utilisé tous ces services de manière extensive pour héberger mes propres projets React et chacun offre une excellente expérience développeur.

La plus grande commodité de tous ces services est que vous pouvez instantanément utiliser des projets stockés sur votre compte GitHub, et chaque fois que vous poussez un nouveau changement, votre site est reconstruit et déployé avec ces changements.

Il est worth de noter que chacun de ces trois services vient avec un niveau gratuit généreux, donc vous n'avez pas à payer quoi que ce soit pour mettre votre application React sur le web.

Leurs niveaux gratuits viennent avec une mise en garde, cependant. Netlify et Vercel imposent tous deux une limite de bande passante de 100 Go par mois sur leur plan gratuit. Si votre site web a moins de 100 000 visiteurs par mois et ne consiste pas en beaucoup d'actifs lourds tels que des images et des vidéos de grande taille, vous ne devriez pas vous inquiéter d'atteindre cette limite.

Parmi ces trois, Cloudflare a le plan gratuit le plus généreux disponible parmi les fournisseurs d'hébergement statique avec une bande passante illimitée.

Si vous êtes intéressé à déployer vos applications React sur Cloudflare Pages, j'ai écrit un guide entier que vous pouvez consulter ici :

[Comment déployer automatiquement vos applications React avec Cloudflare Pages](https://www.freecodecamp.org/news/how-to-auto-deploy-your-react-apps-with-cloudflare-pages/)

## Où dois-je apprendre React ?

Il existe une tonne de ressources pour apprendre React de nos jours. Tellement qu'il est difficile de déterminer lesquelles sont à jour et utiles.

La meilleure chose que vous puissiez faire est de trouver un tutoriel utile et de le suivre jusqu'à la fin, au lieu d'essayer d'en prendre plusieurs à la fois.

> "L'homme qui court après deux lièvres n'en attrape aucun."

Si vous commencez tout juste, ne cherchez pas plus loin que le **curriculum React de freeCodeCamp**. Assurez-vous de tirer parti de tous les liens que j'ai partagés dans chaque section également. Ces deux ressources vous mèneront loin.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le seul cours que j'aurais souhaité avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*