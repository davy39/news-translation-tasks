---
title: Nextjs pour tous — avec quelques connaissances de base de React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-20T21:38:53.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-next-js-for-everyone-507d2d90ab54
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uIepZ6YWTubeVxD5n5kkyg.png
tags:
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Nextjs pour tous — avec quelques connaissances de base de React
seo_desc: 'By Said Hayani

  With some basic React and JavaScript knowledge, you’ll be on your way

  Next.js is a JavaScript framework created by Zeit. It lets you build server-side
  rendering and static web applications using React. It’s a great tool to build your
  n...'
---

Par Said Hayani

#### Avec quelques connaissances de base de React et JavaScript, vous serez sur la bonne voie

**Next.js** est un framework JavaScript créé par [Zeit](https://zeit.co/). Il vous permet de construire des applications web avec rendu côté serveur et des sites web statiques en utilisant React. C'est un excellent outil pour construire votre prochain site web. Il possède de nombreuses fonctionnalités et avantages, qui peuvent faire de Nextjs votre première option pour construire votre prochaine application web.

Vous n'avez besoin d'aucune configuration de webpack ou similaire pour commencer à utiliser Next.js. Il vient avec sa propre configuration. Tout ce dont vous avez besoin est d'exécuter `npm run dev` et de commencer à construire votre application ?.

Dans cet article, nous allons explorer les grandes fonctionnalités et astuces de Next.js, et comment commencer à construire votre prochain site web avec celui-ci.

**Cet article suppose que vous avez quelques connaissances de base de React et JavaScript.**

Voici quelques grands sites web construits avec Next.js :

* [Syntaxt.fm](https://syntax.fm/)
* [npmjs](https://www.npmjs.com/)
* [material-ui.io](https://material-ui.com/)
* [expo.io](https://expo.io/)
* [codemenitor.io](https://www.codementor.io/)

J'ai même utilisé Nextjs pour construire mon site web personnel [saidhayani.me](https://www.saidhayani.me/) — vous pouvez obtenir le code source sur GitHub [ici](https://github.com/hayanisaid/said-hayani-nextjs).

### Commencer avec Next.js

Pour commencer avec Next.js, vous devez avoir node.js installé sur votre machine et c'est tout. Next.js est comme toute autre application node.js — vous avez besoin de npm ou Yarn pour installer les dépendances.

Commençons et créons un projet Next.js.

Tout d'abord, nous devons créer un dossier et lui donner un nom de notre choix. Je vais le nommer `nextjs-app`.

Vous pouvez facilement faire cela avec cette ligne de commande :

![Image](https://cdn-media-1.freecodecamp.org/images/1*k8DzCXqZwRaY64Bhli5-yQ.png)

```
mkdir nextjs-app
```

Après avoir créé le dossier nextjs-app, ouvrez-le dans le terminal. Exécutez `npm init` pour créer le fichier `package.json`.

Ensuite, nous devons installer nos dépendances.

Installation de Next.js

* avec Yarn, tapez

```
yarn add next
```

* avec npm, tapez :

```
npm i next --save
```

Ensuite, nous devons installer React car Next.js utilise React. La première ligne ci-dessous utilise Yarn pour l'installation.

```
yarn add react react-dom
```

```
// avec npm
```

```
npm i react react-dom --save
```

Après cela, vous devez créer deux dossiers nécessaires : `pages` et `static`. Next.js ne fonctionnera pas sans eux !!

![Image](https://cdn-media-1.freecodecamp.org/images/1*s3N5eZcSSSgRdBiaMQeCRA.png)

```
mkdir pages static
```

Vous **devez** avoir cette structure après avoir exécuté ces commandes :

```
nextjs-app  -pages  -static  -package.json
```

Et ensuite, vous pouvez simplement exécuter `npm next dev` et ouvrir `[http://localhost:3000/](http://localhost:3000/)` dans votre navigateur.

La page `NotFound` s'affichera car nous n'avons encore aucune page !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hv_4BaqTnrlriZ8Q3zk5ZQ.png)

Alors créons une page `home` et un point d'entrée `index.js`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IwZ5Ahr9egJ8KHF5HnLfHQ.png)

```
touch index.js home.js
```

Et ensuite, vous pouvez écrire un composant React normal. Comme je l'ai dit ci-dessus, Next.js est pour construire des applications React.

Voici à quoi ressemble notre fichier `home.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*He5fQw-VgeY5Gjo2RFGckw.png)

Et voici notre fichier `index.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*AgGKp-WdRTwb3bOuqljcug.png)

Next.js dispose d'une fonctionnalité de rechargement en direct. Tout ce que vous avez à faire est de changer et d'enregistrer, et Next.js compilera et rechargera l'application automatiquement pour vous.

**Note** : Next.js est comme tout autre outil de rendu côté serveur, nous devons définir la page par défaut de notre application, dans notre cas, c'est `index.js`.

Vous verrez ce changement dans le navigateur après avoir exécuté `npm next dev` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QuQK1J5P0Rc4S-0BhllNmg.png)

Félicitations ! Nous venons de créer une application Next.js avec quelques étapes simples. Ces instructions pour créer une application Next.js sont décrites dans la [documentation officielle de Next.js](https://nextjs.org/learn/basics/getting-started/first-page).

#### Mon alternative

Je n'utilise généralement pas cette méthode. J'utilise plutôt l'outil CLI [create-next-app](http://import React from ) qui fait tout cela pour moi en une seule ligne.

```
npx create-next-app my-app
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*W5KCIFWP7yMHI-zaeVcmPA.png)

Vous pouvez consulter la documentation [ici](https://github.com/segmentio/create-next-app) pour explorer d'autres fonctionnalités.

### Créer des configurations personnalisées pour Next.js

Parfois, vous pourriez vouloir ajouter des dépendances ou des packages supplémentaires à votre application Next.js.

Next.js vous donne la possibilité de personnaliser votre configuration en utilisant un fichier `next-config.js`.

Par exemple, vous pourriez vouloir ajouter la prise en charge de sass à votre application. Dans ce cas, vous devez utiliser le package [next-sass](https://github.com/zeit/next-plugins/tree/master/packages/next-sass) **et** vous devez l'ajouter au fichier `next-config.js` comme dans l'exemple ci-dessous :

Tout d'abord, installez `next-sass` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5XSEx8DH0851FNzMxDx5LQ.png)

```
yarn add @zeit/next-sass
```

Ensuite, incluez-le dans le fichier `next-config.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YN_aoR5dzlnMyG2xVHJcww.png)

Et ensuite, vous pouvez créer et écrire votre code sass et l'importer dans votre composant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kde4wjR-EpoNHc1c4JTb8g.png)

Importation du fichier sass dans notre composant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yv1cTBXPeONqaV-CS1OZ2A.png)

Et voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VYfSkK1fIZKu75-2P8s4Bw.png)

Wow, n'était-ce pas **super facile** d'ajouter la prise en charge de sass à notre application Next.js ?

À ce stade, nous avons simplement couvert la partie installation et configuration. Maintenant, parlons des fonctionnalités de Next.js !

### Les fonctionnalités

Next.js vient avec un ensemble de grandes fonctionnalités comme le rendu côté serveur, les routeurs et le chargement paresseux.

#### Rendu côté serveur

Next.js effectue le rendu côté serveur par défaut. Cela optimise votre application pour les moteurs de recherche. De plus, vous pouvez intégrer tout middleware tel que [express.js](https://expressjs.com/) ou [Hapi.js](https://hapijs.com/), et vous pouvez exécuter toute base de données telle que MongoDB ou MySQL.

En parlant d'optimisation pour les moteurs de recherche, Next.js vient avec un composant `Head` qui vous permet d'ajouter et de créer des balises méta dynamiques. C'est ma fonctionnalité préférée — vous pouvez créer des balises méta personnalisées et dynamiques. Cela rend votre site web capable d'être indexé par les moteurs de recherche comme Google. Voici un exemple de composant `Head` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mnIJGBgF59r1YjX5jXu8IA.png)

Et vous pouvez importer et utiliser le composant `Head` dans n'importe quelle autre page :

![Image](https://cdn-media-1.freecodecamp.org/images/1*liF5bNPAQ_j7gA9funSGTg.png)

Génial !

**Note** : Avec Next.js, vous **n'avez pas** besoin d'importer React car Next.js le fait pour vous.

#### Générer un site web statique avec Next.js

En plus du rendu côté serveur, vous pouvez toujours compiler et exporter votre application en tant que site web statique HTML et la déployer sur un hébergement de site web statique comme une page GitHub ou [netlify](https://www.netlify.com/). Vous pouvez en apprendre davantage sur la création d'un site web statique avec Next.js [ici dans la documentation officielle](https://nextjs.org/learn/excel/static-html-export/setup).

#### Routeurs

C'est une autre des grandes fonctionnalités de Next.js. Lorsque vous utilisez [create-react-app](https://github.com/facebook/create-react-app), vous devez généralement installer [react-router](https://github.com/ReactTraining/react-router) et créer sa configuration personnalisée.

Next.js vient avec ses propres routeurs avec zéro configuration. Vous n'avez besoin d'aucune configuration supplémentaire de vos routeurs. Il suffit de créer votre page à l'intérieur du dossier `pages` et Next.js s'occupera de toute la configuration du routage.

Allons-y et créons une navigation personnalisée pour tout clarifier !

Pour naviguer entre les pages, Next.js dispose de la méthode `Link` pour gérer la navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*D54h6wnKX9fCS0AU34tVLA.png)

Créons les pages `blog.js` et `contact.js` :

`blog.js`

![Image](https://cdn-media-1.freecodecamp.org/images/1*f6_vaaPs1Okfj8vZ9Fhk8g.png)

Et voici la page `contact.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5lWCDzAUWed2NlsGpTC5EQ.png)

Et maintenant, nous devons être capables de naviguer entre ces pages ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*7WYZeRb92PAwqthLo0xqHg.gif)

Wow, c'est si facile et super génial.

#### Chargement paresseux

Le chargement paresseux permet à votre application de fournir une meilleure expérience utilisateur. Parfois, la page peut prendre du temps à charger. L'utilisateur peut abandonner votre application si le chargement prend plus de 30 secondes.

La façon d'éviter cela est d'utiliser une astuce pour indiquer à l'utilisateur que la page est en cours de chargement, par exemple en affichant un spinner. Le chargement paresseux ou le fractionnement de code est l'une des fonctionnalités qui vous permettent de gérer et de contrôler le chargement lent afin que vous ne chargiez que le code nécessaire dans votre page.

Next.js vient avec sa propre méthode de fractionnement de code. Il nous fournit une méthode, appelée `dynamic`, pour charger notre composant, comme dans l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ib835M7Ih-RY1kRBOUnXFA.png)

Vous pouvez trouver le code source de ces exemples sur [GitHub](https://github.com/hayanisaid/nextjs-intro-example)

C'est tout. J'espère que c'est suffisant et j'espère que cet article vous donne une idée claire de Next.js et de ses fonctionnalités. Vous pouvez en apprendre davantage sur d'autres fonctionnalités dans la [documentation officielle](https://nextjs.org/docs/).

Si vous avez d'autres ajouts à cet article, vous pouvez laisser un commentaire ci-dessous et si vous aimez cet article, n'hésitez pas à applaudir ? et à partager.

Discuter sur [Twitter](https://twitter.com/SaidHYN)?.



> Au fait, j'ai récemment travaillé avec un groupe solide d'ingénieurs logiciels pour l'une de mes applications mobiles. L'organisation était excellente, et le produit a été livré très rapidement, beaucoup plus rapidement que d'autres entreprises et freelances avec lesquels j'ai travaillé, et je pense que je peux honnêtement les recommander pour d'autres projets. Envoyez-moi un email si vous voulez entrer en contact — [said@devsdata.com](mailto:said@devsdata.com).