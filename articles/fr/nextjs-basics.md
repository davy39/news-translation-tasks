---
title: "Tutoriel Next.js Basics \x13 Rendering c\x14t\x1E serveur, Sites statiques,\
  \ APIs REST, Routing, et plus"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-16T21:07:01.000Z'
originalURL: https://freecodecamp.org/news/nextjs-basics
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/nextjs-featured-image--1-.png
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: "Tutoriel Next.js Basics \x13 Rendering c\x14t\x1E serveur, Sites statiques,\
  \ APIs REST, Routing, et plus"
seo_desc: "By Said Hayani\nNextjs is JavaScript framework that helps you build web\
  \ applications using Reactjs. It offers a ton of features and tools that make building\
  \ a complete app simpler and easier. \nNextjs provides a great developer experience\
  \ in many areas..."
---

Par Said Hayani

[Nextjs](https://nextjs.org/docs/) est un framework JavaScript qui vous aide  construire des applications web en utilisant Reactjs. Il offre une tonne de fonctionnalits et d'outils qui rendent la construction d'une application complte plus simple et plus facile. 

Nextjs offre une excellente exprience dveloppeur dans de nombreux domaines. Il a galement simplifi de nombreuses fonctionnalits qui taient compliques par le pass, comme le rendering ct serveur, la gnration de sites web statiques, et le travail avec les APIs REST.

Dans cet article, je vais vous guider  travers les fonctionnalits de [Nextjs](https://nextjs.org/) que j'utilise personnellement le plus. 

## Comment configurer et installer Nextjs

Vous pouvez excuter et construire une application web entire avec zro configuration avec Nextjs. C'est super facile  utiliser  vous pouvez simplement bootstrapper une application **Nextjs** complte avec une seule commande, comme ceci:

```
yarn create next-app
```

Ensuite, il vous suffit d'excuter `yarn dev` et votre application est prte!

### Ajouter une configuration personnalise  l'application Nextjs

Nextjs vous permet d'ajouter une configuration personnalise pour [webpack](https://webpack.js.org/). Vous pouvez galement ajouter et intgrer des plugins. 

Parfois, vous pourriez avoir besoin d'ajouter un plugin pour grer le traitement des images ou pour supporter un package qui n'est pas support par Nextjs par dfaut, comme le traitement CSS par exemple.  

Pour cela, vous pouvez crer `next.config.js` dans le rpertoire racine de l'application. L'exemple ci-dessous vous montre comment ajouter un plugin pour charger des fichiers d'environnement.

```
require("dotenv").config();
const webpack = require("webpack");
module.exports = {

  webpack: (config) => {
    config.plugins.push(new webpack.EnvironmentPlugin(process.env));
    return config;
  },
};
```

## Comment intgrer vos outils prfrs

Il est simple d'ajouter des outils comme TypeScript, Firebase, ou AWS. Nextjs offre galement de nombreux modles pour chaque cas dans son [dpt GitHub](https://github.com/vercel/next.js/tree/canary/examples). Consultez-les pour voir ceux que vous souhaitez utiliser. 

### Ajouter Firebase  Nextjs

Par exemple, si vous souhaitez ajouter Firebase directement, vous pouvez excuter la commande suivante:

```shell
yarn create next-app --example with-firebase with-firebase-app
```

Cela bootstrappera une application Nextjs avec Firebase pr-configur et installera les packages dont Firebase a besoin pour fonctionner. Vous pouvez consulter l'exemple complet [ici](https://github.com/vercel/next.js/tree/canary/examples/with-firebase).

### Ajouter le support TypeScript

Une seule commande suffit pour ajouter le support TypeScript  Nextjs:

```shell
touch tsconfig.json
```

Cela crera un fichier `tsconfig.json` pour le compilateur TypeScript. Nextjs dtectera automatiquement le fichier et gnrera une configuration TypeScript par dfaut pour vous. Vous pouvez ajouter votre configuration personnalise plus tard, assurez-vous simplement d'ajouter une extension `ts`  vos composants afin que le compilateur puisse interprter vos fichiers comme des fichiers TypeScript.

## Rendering ct serveur

Le rendering ct serveur aide au [**SEO**](https://en.wikipedia.org/wiki/Search_engine_optimization) de votre site. Donc si la recherche est l'une de vos priorits, alors Nextjs est un bon choix pour vous.

Nextjs vous offre de meilleures options quant  la faon de rendre votre application. Par exemple, vous pouvez activer ou dsactiver le rendering ct serveur pour chaque page. 

Si vous utilisez `getServerSideProps`, cela rend la page par dfaut ct serveur et vous donne accs aux props ct serveur.

## Sites web et composants statiques

Vous pouvez exporter votre application en tant que site statique, et l'hberger sur un outil d'hbergement web statique comme Netlify.

 La commande `next export` gnrera un composant statique pour vous.

Pour construire et exporter l'application en tant que HTML statique, excutez la commande suivante:

```
next build && next export
```

Consultez la documentation officielle de [Nextjs](https://nextjs.org/docs/advanced-features/static-html-export) pour explorer plus d'options lors de l'exportation en HTML.

## Routing

Le routing est intgr avec **Nextjs**  vous n'avez pas besoin d'utiliser de bibliothque tierce pour le grer. Il propose galement deux approches diffrentes, le routing dynamique et les routes impriales (prdfinies).

Les routes dynamiques vous permettent de crer des slugs et des chemins dynamiques. Imaginez que vous avez un blog et que vous souhaitez afficher les dtails de chaque article. Au lieu de crer plusieurs pages (prdfinies) pour chaque article, vous utiliseriez une page dynamique et rutilisable. 

Le routing dynamique peut tre implment de la manire suivante:

* Dans le dossier **pages**, crez un dossier qui sera utilis pour rendre le chemin dynamique. Nous pouvons l'appeler `page`. 
* Pour le rendre dynamique, nous pouvons simplement ajouter une barre oblique et un paramtre, comme ceci:  `page/[pid]`. Le paramtre doit tre  l'intrieur de deux crochets. 
* Ensuite, nous creons un fichier `index.js`  l'intrieur du dossier `page/[pid]`. Il contient le code suivant:

```jsx
import React from 'react'
import {useRouter, Router} from 'next/router'
import {route} from 'next/dist/next-server/server/router'

export default function pid() {
  const router = useRouter()
  const {pid} = router.query
  return <div>Page id :{pid}</div>
}
```

`http://localhost:3000/page/2` est un exemple de chemin. Nous pouvons galement utiliser `route.query` pour accder  tous les paramtres comme dans l'exemple ci-dessus.

## Comment construire une API REST

En plus des autres fonctionnalits, vous pouvez construire des endpoints d'API REST au sein de votre application Nextjs et les consommer au sein de la mme application ou de toute autre application.

L'exemple ci-dessous est une petite dmo d'un endpoint simple qui retourne une liste d'articles.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/RES-API-nextjs.png)

Si vous utilisez `nextjs 9.5.2` ou une version ultrieure, il est livr avec un dossier `api` par dfaut, gnralement dans le dossier **pages**.

Voici un exemple d'utilisation d'un endpoint qui retourne une rponse `json`.

`/api/posts`

```js
// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

const posts = [
  {
    id: 1,
    name: 'Nextjs est gnial'
  },
  {
    id: 2,
    name: 'Utiliser TypeScript avec Nextjs'
  },
  {
    id: 3,
    name: 'GraphQL Vs REST'
  },
  {
    id: 4,
    name: 'Bridging in React Native'
  }
]
export default (req, res) => {
  res.statusCode = 200
  res.json(posts)
}
```

Et si vous allez sur `https://localhost:5000/api/posts`, cela retournera une rponse JSON des articles.

## Fonctionnalits supplmentaires

### Modules CSS

Nextjs supporte les modules CSS par dfaut. Vous pouvez crer directement un module CSS avec la commande `style.module.css` et l'importer dans n'importe quel composant comme ceci:

```jsx
import styles from './style.module.css'

```

Vous pouvez galement utiliser le CSS dans JS comme vous pouvez le faire dans React.

```jsx
<div style={{
  width:300 
}>
   Card
</div>
```

 Je vous recommande de consulter [nextjs.org](https://nextjs.org/docs/) pour en savoir plus sur les fonctionnalits supplmentaires.

Le code source des exemples utiliss dans ce blog peut tre trouv [sur GitHub](https://github.com/hayanisaid/nextjs-all-in-one).

_Vous devriez me suivre sur Twitter, et vous abonner  ma_ [_Liste de diffusion_](https://subscribi.io/subscribe/5f63b2b306cb71c069272c47)_._

> Bonjour, je m'appelle Said Hayani. J'ai cr [subscribi.io](https://subscribi.io/) pour aider les crateurs, les blogueurs et les influenceurs  dvelopper leur audience grce  la newsletter.