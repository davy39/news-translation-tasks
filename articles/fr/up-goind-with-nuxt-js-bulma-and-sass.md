---
title: Démarrage avec Nuxt.js, Bulma et Sass
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-15T11:09:27.000Z'
originalURL: https://freecodecamp.org/news/up-goind-with-nuxt-js-bulma-and-sass
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca202740569d1a4ca51f3.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Bulma
  slug: bulma
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
- name: General Programming
  slug: programming
- name: Sass
  slug: sass
- name: vue
  slug: vue
seo_title: Démarrage avec Nuxt.js, Bulma et Sass
seo_desc: 'By Eduardo Vedes

  TL;DR: Overcome Nuxt.js, Bulma and Sass shenanigans with this quick article to help
  you start developing your next App in less than 10 minutes.

  Hi everyone ❤️! Few days ago I found myself struggling a bit to put Nuxt.js, Bulma
  and Sa...'
---

Par Eduardo Vedes

**TL;DR: Surmontez les difficultés de Nuxt.js, Bulma et Sass avec cet article rapide pour vous aider à commencer à développer votre prochaine application en moins de 10 minutes.**

Salut à tous f497! Il y a quelques jours, j'ai eu un peu de mal à faire fonctionner correctement **Nuxt.js**, **Bulma** et **Sass**, et les informations que j'ai trouvées sur Google n'ont pas été très utiles.

La plupart des configurations que j'ai trouvées ne fonctionnaient pas, car elles étaient obsolètes ou n'expliquaient pas très bien comment procéder. J'ai donc approfondi un peu ce sujet et décidé d'écrire un article pour vous aider à faire de même en moins de 10 minutes.

Amusons-nous et mettons les mains dans le cambouis tout en assimilant quelques concepts nécessaires pour cela.

## 1. Échafaudage de Nuxt.js

De nos jours, pour commencer rapidement avec Nuxt.js, nous utilisons un outil d'échafaudage appelé **[create-nuxt-app](https://github.com/nuxt/create-nuxt-app)**. Assurez-vous d'avoir **[npx](https://www.npmjs.com/package/npx)** installé sur votre machine.

Ouvrons un terminal et exécutons : `npx create-nuxt-app nuxt-bulma-sass`, où `nuxt-bulma-sass` est le nom du projet que nous échafaudons pour les besoins de cet article.

**create-nuxt-app** vous posera quelques questions avant de créer l'échafaudage. Pour les besoins de cet article, j'ai choisi la configuration suivante :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/bulma2.png)
_Questions d'initialisation de create-nuxt-app_

L'étape suivante consiste à changer de répertoire pour accéder à notre dossier de projet :

`cd nuxt-bulma-sass`

et à lancer le projet avec : `yarn run dev`. (vous pouvez également utiliser npm si vous préférez)

À ce stade, notre projet est en cours d'exécution :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/bulma3.png)

Et si nous ouvrons notre navigateur sur localhost:3000, nous obtiendrons cet écran :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.29.05.png)
_localhost:3000 pages/index.vue_

À ce stade, nous avons donc la page pages/index.vue à l'écran, qui est la première page à être rendue dans votre projet par défaut.

Remplaçons le contenu de ce fichier par le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon1.png)

Si nous inspectons notre page dans le navigateur, nous voyons que **bulma** est installé car la section est formatée selon celui-ci.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.45.03.png)

Facile comme bonjour.

Ajoutons une classe et choisissons quelques couleurs :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon-2.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.47.55.png)

Et si nous voulons imbriquer ._hello-nuxt_ à l'intérieur de ._edo-theme_ ? Nous allons avoir besoin de SASS pour pouvoir le faire.

## 2. Ajout de Sass

Pour ajouter Sass à notre projet, nous devons arrêter notre application en cours d'exécution (Ctrl+c) et faire ce qui suit :

`yarn add node-sass sass-loader --dev`

Ce sont les deux packages nécessaires en tant que dépendances de développement pour pouvoir avoir Sass dans notre modèle de base.

Notez que nous l'ajoutons en tant que dépendance de développement car nous en avons seulement besoin pendant le développement et au moment de la construction. Après cela, **Sass** est transformé en **CSS** et nous n'en avons plus besoin.

Voici un aperçu de mon package.json pour que vous puissiez vérifier :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-09.57.38.png)
_package.json avec sass ajouté au projet_

D'accord tout le monde f497, à ce stade, nous sommes en mesure d'imbriquer les classes que nous voulions.

Relançons notre modèle de base : `yarn run dev` et faisons les ajustements nécessaires ?

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--1-.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-10.05.23.png)

Super ! Nous avons déjà fait beaucoup aujourd'hui ! Allez prendre un café f375, je vous attends ici ?

D'accord, abstraisons un peu les choses et créons ce fichier _~/assets/scss/main.scss_ et mettons-y quelques classes et variables :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon-1.png)
_nouveau ~/assets/scss/main.scss_

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--1--1.png)

Bien ! Ça marche !

Maintenant, nous avons deux problèmes : 

1. Nous devons importer main.scss dans chacune de nos pages/composants, ce qui n'est pas idéal. Nous voulons l'importer une seule fois et l'avoir disponible dans tous nos "sacs" <style>
2. Nous ne pouvons pas utiliser les variables sass de bulma (essayez de changer la **background-color** de la classe .edo-theme de **$edo** à **$primary**. Nous voulons avoir les variables sass de bulma afin de les remplacer et de créer de nouveaux thèmes à partir de là.

Alors... que faire si nous voulons utiliser les [variables sass de bulma](https://bulma.io/documentation/overview/colors/) ? 

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-10.13.31.png)
_variables sass de bulma (doc couleurs)_

## 3. Voici la partie difficile qui m'a pris un certain temps à comprendre.

Bulma est importé dans l'échafaudage create-nuxt-app. Lorsque vous exécutez `yarn run dev`, il y a ce dossier .**nuxt** caché dans votre dossier **nuxt-bulma-sass**.

Si vous regardez App.js là-bas :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/nuxt2.png)

Vous verrez que bulma est importé depuis les node-modules lorsque vous lancez l'environnement de développement.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/nuxt-bulma.png)
_.nuxt/App.js_

Donc, importer bulma lors du lancement de l'échafaudage nuxt.js n'est pas correct si nous voulons remplacer les variables sass de bulma.

Ne désespérez pas, vous n'avez pas à jeter votre projet. Le spectacle doit continuer ?

## 4. Utiliser Bulma de la bonne manière ?

Comment intégrer bulma dans notre modèle de base de la manière dont nous avons besoin ? 

Commençons par commenter @nuxtjs/bulma dans la section modules du **nuxt.config.js** (conservez-le dans le package.json car ce qu'il fait là est d'installer bulma, ce serait la même chose, AFAIK, que de faire `yarn add bulma`).

Arrêtez votre environnement d'exécution et faites `yarn run dev` à nouveau.

Si vous regardez dans _./nuxt/App_, vous verrez qu'il n'importe plus bulma.

Donc, ce que nous devons faire maintenant, c'est d'aller dans notre fichier main.scss et de l'importer dans la dernière ligne du fichier.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--4-.png)

_J'ai également importé bulma/sass/utilities/_all.sass_ pour que nous ayons les variables sass avec les couleurs là.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-11.12.24.png)
_dossier /bulma/sass/utilities_

Bien sûr, plus tard, vous pouvez l'améliorer en important exactement ce dont vous avez besoin. Mais c'est une autre histoire pour un autre article ?

Eh bien, vérifiez votre navigateur et voyez-le fonctionner.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-14-at-11.19.16.png)

## 5. Yeah! Ça marche bébé!

**Maintenant, le dernier problème !** Nous ne voulons pas l'importer dans notre échafaudage <style> chaque fois que nous voulons l'utiliser. Nous voulons qu'il soit disponible globalement partout dans le modèle de base.

La solution à cela est d'importer un package appelé **[@nuxtjs/style-resources](https://www.npmjs.com/package/@nuxtjs/style-resources).** 

Ce package vous permet de partager des variables, des mixins, des fonctions dans tous les fichiers. Plus besoin d'importer dans votre balise <style> de chaque composant ou page.

Arrêtez simplement votre environnement de développement et faites :

`yarn add @nuxjs/style-resources` Note : n'essayez pas de l'installer en tant que dépendance de développement car cela ne fonctionnera pas correctement.

De plus, ouvrez votre fichier nuxt.config.js et ajoutez '@nuxtjs/style-resources' à votre clé/valeur de modules.

Vous devez également ajouter _styleResources_. Vérifiez comment le mien est après cela ?

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--5-.png)

Faites `yarn run dev` à nouveau et... pas d'erreurs... mais...

**Les classes CSS ne sont plus importées.**

**FML** ??f52c

## 6. Dernier ajustement

**Que se passe-t-il ici ?** 

À partir du moment où vous importez et utilisez _@nuxt/style-resources_, vous ne pouvez plus importer de styles réels depuis le main.scss simplement parce qu'ils n'existeront pas dans la construction réelle.

Donc, pour résoudre ce problème :

Arrêtez à nouveau l'exécution du modèle de base et ouvrez votre nuxt.config.js :

Ajoutez le chemin main.scss au tableau css global, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/carbon--6-.png)

De cette manière, nous nous assurons que les styles css globaux sont également importés dans le scope de nos templates.

À partir de ce stade, bien sûr, vous pouvez établir un modèle architectural pour vos fichiers css, créer des fichiers de variables, de fonctions et de mixins indépendants et composer des éléments avec quelques @imports supplémentaires.

Dans l'objet styleResources, vous avez la possibilité d'inclure plus de fichiers selon vos besoins dans votre modèle de base.

Encore une fois, cela dépasse le cadre de cet article qui était de vous montrer comment vous libérer de ces petites complexités que nuxt et ses écosystèmes introduisent dans le flux de notre application.

## J'espère que vous avez apprécié ! f497

## Soyez fort et continuez à coder ?

## 7. Dernier point mais non des moindres

Vous pouvez cloner mon dépôt et jouer avec.

[https://github.com/evedes/nuxt-bulma-sass](https://github.com/evedes/nuxt-bulma-sass)

Un grand merci à [@ruiposse](https://twitter.com/ruiposse) pour avoir révisé cet article et pour m'avoir mentoré dans l'écosystème vue. f497

## 8. Bibliographie

01. [Nuxtjs.org](https://nuxtjs.org/)

02. [Nuxt Style Resources](https://github.com/nuxt-community/style-resources-module)

03. [Bulma.io](https://bulma.io/)

04. Quelques heures autour de google à s'énerver et à voir des gens également frustrés par cela ?

---

Hey ! Je suis Edo, un ingénieur frontend dédié à la stack JavaScript. De nos jours, je travaille principalement avec React, Vue et tout l'écosystème autour. 

Si vous avez aimé cet article, vous pouvez en lire plus [ici](https://www.freecodecamp.org/news/author/evedes/).