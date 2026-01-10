---
title: Découvrez Next.js et écrivez des applications React côté serveur facilement
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-04-04T10:55:09.000Z'
originalURL: https://freecodecamp.org/news/discover-next-js-and-write-server-side-react-apps-the-easy-way-cc920dea2d9d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*PoTjNPCEp_E0AIrM.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Découvrez Next.js et écrivez des applications React côté serveur facilement
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Introduction

  Working on a modern JavaScript application powered by React is awesome until you
  realize that there are a couple problems related to rendering all the content on
  the clie...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

### Introduction

Travailler sur une application JavaScript moderne alimentée par [React](https://flaviocopes.com/react/) est génial jusqu'à ce que vous réalisiez qu'il y a quelques problèmes liés au rendu de tout le contenu côté client.

Premièrement, la page prend plus de temps à devenir visible pour l'utilisateur. Cela est dû au fait qu'avant que le contenu ne se charge, tout le JavaScript doit se charger, et votre application doit s'exécuter pour déterminer ce qu'il faut afficher sur la page.

Deuxièmement, si vous construisez un site web public, vous avez un problème de SEO de contenu. Les moteurs de recherche s'améliorent pour exécuter et indexer les applications JavaScript, mais il est bien mieux si nous pouvons leur envoyer du contenu au lieu de les laisser le découvrir.

La solution à ces deux problèmes est le **rendu côté serveur**, également appelé **pré-rendu statique**.

Next.js est un framework React qui nous permet de faire tout cela de manière très simple, mais il n'est pas limité à cela. Il est présenté par ses créateurs comme un **outil de chaîne de construction à configuration zéro, à commande unique pour les applications React**.

Il fournit une structure commune qui vous permet de construire facilement une application frontend React, et il gère transparemment le rendu côté serveur pour vous.

### Fonctionnalités principales

Voici une liste non exhaustive des principales fonctionnalités de Next.js :

* **Rechargement à chaud du code** : Next.js recharge la page lorsqu'il détecte un changement enregistré sur le disque.
* **Routage automatique** : toute URL est mappée au système de fichiers (aux fichiers placés dans le dossier `pages`), et vous n'avez besoin d'aucune configuration (vous avez des options de personnalisation, bien sûr).
* **Composants à fichier unique** : en utilisant [styled-jsx](https://github.com/zeit/styled-jsx), complètement intégré et développé par la même équipe, il est facile d'ajouter des styles limités au composant.
* **Rendu côté serveur** : vous pouvez (optionnellement) rendre les composants React côté serveur avant d'envoyer le HTML au client.
* **Compatibilité avec l'écosystème** : Next.js s'intègre bien avec le reste de l'écosystème JavaScript, Node et React.
* **Fractionnement automatique du code** : les pages sont rendues avec uniquement les bibliothèques et le JavaScript dont elles ont besoin, pas plus.
* **Préchargement** : le composant `Link`, utilisé pour lier différentes pages, prend en charge une propriété `prefetch` qui précharge automatiquement les ressources de la page (y compris le code manquant en raison du fractionnement du code) en arrière-plan.
* **Composants dynamiques** : vous pouvez importer des modules JavaScript et des composants React dynamiquement [ici](https://github.com/zeit/next.js#dynamic-import).
* **Exportations statiques** : en utilisant la commande `next export`, Next.js vous permet d'exporter un site entièrement statique à partir de votre application.

### Installation

Next.js prend en charge toutes les principales plateformes : Linux, macOS, Windows.

Un projet Next.js est facilement démarré avec [npm](https://flaviocopes.com/npm/) :

```
npm install --save next react react-dom
```

ou avec [Yarn](https://flaviocopes.com/yarn/) :

```
yarn add next react react-dom
```

### Premiers pas

Créez un fichier `package.json` avec ce contenu :

```
{  "scripts": {    "dev": "next"  }}
```

Si vous exécutez cette commande maintenant :

```
npm run dev
```

le script générera une erreur se plaignant de ne pas trouver le dossier `pages`. C'est la seule chose dont Next.js a besoin pour fonctionner.

Créez un dossier `pages` vide et exécutez à nouveau la commande. Ensuite, Next.js démarrera un serveur sur `localhost:3000`.

Si vous allez à cette URL maintenant, vous serez accueilli par une page 404 conviviale, avec un design propre et agréable.

![Image](https://cdn-media-1.freecodecamp.org/images/46w-nQian7G9HGh6t3OUSvSDx1YoUVd7BjUm)

Next.js gère également d'autres types d'erreurs, comme les erreurs 500, par exemple.

### Créer une page

Dans le dossier `pages`, créez un fichier `index.js` avec un simple composant fonctionnel React :

```
export default () => (  <div>    <p>Hello World!</p>  </div>)
```

Si vous visitez `localhost:3000`, ce composant sera automatiquement rendu.

Pourquoi est-ce si simple ?

Next.js utilise une structure de pages déclarative, basée sur la structure du système de fichiers.

En termes simples, les pages sont à l'intérieur d'un dossier `pages`, et l'URL de la page est déterminée par le nom du fichier de la page. Le système de fichiers est l'API des pages.

Ouvrez la source de la page, `View -> Developer -> View` Source avec Chrome.

Comme vous pouvez le voir, le HTML généré par le composant est envoyé directement dans la source de la page. Il n'est pas rendu côté client, mais il est rendu côté serveur.

L'équipe Next.js voulait créer une expérience de développement pour les pages rendues côté serveur similaire à celle que vous obtenez lorsque vous créez un projet PHP de base (où vous déposez simplement des fichiers PHP et vous les appelez, et ils apparaissent comme des pages). En interne, bien sûr, tout est très différent, mais la facilité d'utilisation apparente est claire.

### Ajouter une deuxième page

Créons une autre page, dans `pages/contact.js`

```
export default () => (  <div>    <p>      <a href="my@email.com">Contactez-nous !</a>    </p>  </div>)
```

Si vous pointez votre navigateur vers `localhost:3000/contact`, cette page sera rendue. Comme vous pouvez le voir, cette page est également rendue côté serveur.

### Rechargement à chaud

Remarquez comment vous n'avez pas eu à redémarrer le processus `npm` pour charger la deuxième page. Next.js le fait pour vous en arrière-plan.

### Rendu côté client

Le rendu côté serveur est très pratique pour le premier chargement de votre page pour toutes les raisons que nous avons vues ci-dessus. Mais lorsqu'il s'agit de naviguer à l'intérieur du site web, le rendu côté client est essentiel pour accélérer le chargement de la page et améliorer l'expérience utilisateur.

Next.js fournit un composant `Link` que vous pouvez utiliser pour construire des liens. Essayez de lier les deux pages ci-dessus.

Changez `index.js` en ce code :

```
import Link from 'next/link'
```

```
export default () => (  <div>    <p>Hello World!</p>    <Link href="/contact">      <a>Contactez-moi !</a>    </Link>  </div>)
```

Maintenant, retournez dans le navigateur et essayez ce lien. Comme vous pouvez le voir, la page de contact se charge immédiatement, sans actualisation de la page.

C'est la navigation côté client qui fonctionne correctement, avec un support complet pour l'**API History**. Cela signifie que le bouton de retour de votre utilisateur ne se cassera pas.

Si vous faites maintenant un `cmd-click` sur le lien, la même page de contact s'ouvrira dans un nouvel onglet, maintenant rendue côté serveur.

### Pages dynamiques

Un bon cas d'utilisation pour Next.js est un blog. C'est quelque chose que tous les développeurs savent comment cela fonctionne, et c'est un bon exemple simple de la façon de gérer les pages dynamiques.

Une page dynamique est une page qui n'a pas de contenu fixe, mais qui affiche plutôt certaines données basées sur certains paramètres.

Changez `index.js` en :

```
import Link from 'next/link'
```

```
const Post = (props) => (  <li>    <Link href={`/post?title=${props.title}`}>      <a>{props.title}</a>    </Link>  </li>)
```

```
export default () => (  <div>    <h2>Mon blog</h2>    <ul>      <li>        <Post title="Yet another post" />        <Post title="Second post" />        <Post title="Hello, world!" />      </li>    </ul>  </div>)
```

Cela créera une série de posts et remplira le paramètre de requête de titre avec le titre du post :

![Image](https://cdn-media-1.freecodecamp.org/images/OmO6AVGki0BPyh0lmJrfk6r20EyMQ8tFFDl9)

Maintenant, créez un fichier `post.js` dans le dossier `pages`, et ajoutez :

```
export default (props) => (  <h1>{props.url.query.title}</h1>)
```

Maintenant, en cliquant sur un post unique, le titre du post sera rendu dans une balise `h1` :

![Image](https://cdn-media-1.freecodecamp.org/images/-x4uwlsufzhq6TAnuDHNckHvniGIBnYoVNLB)

Vous pouvez utiliser des URLs propres sans paramètres de requête. Le composant Link de Next.js nous aide en acceptant un attribut `as`, que vous pouvez utiliser pour passer un slug :

```
import Link from 'next/link'
```

```
const Post = (props) => (  <li>    <Link as={`/${props.slug}`} href={`/post?title=${props.title}`}>      <a>{props.title}</a>    </Link>  </li>)
```

```
export default () => (  <div>    <h2>Mon blog</h2>    <ul>      <li>        <Post slug="yet-another-post" title="Yet another post" />        <Post slug="second-post" title="Second post" />        <Post slug="hello-world" title="Hello, world!" />      </li>    </ul>  </div>)
```

### CSS-in-JS

Next.js fournit par défaut une prise en charge pour [styled-jsx](https://github.com/zeit/styled-jsx), qui est une solution CSS-in-JS fournie par la même équipe de développement. Mais vous pouvez utiliser n'importe quelle bibliothèque que vous préférez, comme [Styled Components](https://flaviocopes.com/styled-components/).

### Exporter un site statique

Une application Next.js peut facilement être exportée en tant que site statique. Cela peut ensuite être déployé sur l'un des hôtes de sites statiques super rapides, comme [Netlify](https://flaviocopes.com/netlify/) ou [Firebase Hosting](https://flaviocopes.com/firebase-hosting/), sans avoir besoin de configurer un environnement Node.

Le processus vous oblige à déclarer les URLs qui composent le site, mais c'est [un processus simple](https://github.com/zeit/next.js/#static-html-export).

### Déploiement

Il est facile de créer une copie de l'application prête pour la production sans les cartes sources ou d'autres outils de développement qui ne sont pas nécessaires dans la version finale.

Au début de ce tutoriel, vous avez créé un fichier `package.json` avec ce contenu :

```
{  "scripts": {    "dev": "next"  }}
```

qui était la façon de démarrer un serveur de développement en utilisant `npm run dev`.

Maintenant, ajoutez simplement le contenu suivant à `package.json` :

```
{  "scripts": {    "dev": "next",    "build": "next build",    "start": "next start"  }}
```

et préparez votre application en exécutant `npm run build` et `npm run start`.

### Now

L'entreprise derrière Next.js fournit un service d'hébergement génial pour les applications Node.js, appelé [**Now**](https://zeit.co/now).

Bien sûr, ils intègrent leurs deux produits afin que vous puissiez déployer des applications Next.js de manière transparente, [une fois que vous avez installé Now](https://zeit.co/download), en exécutant la commande `now` dans le dossier de l'application.

En arrière-plan, Now configure un serveur pour vous, et vous n'avez pas à vous soucier de quoi que ce soit — il suffit d'attendre que l'URL de votre application soit prête.

### Zones

Vous pouvez configurer plusieurs instances Next.js pour écouter différentes URLs. Pourtant, l'application pour un utilisateur externe semblera simplement être alimentée par un seul serveur : [https://github.com/zeit/next.js/#multi-zones](https://github.com/zeit/next.js/#multi-zones)

### Plugins

Next.js dispose d'une liste de plugins [ici](https://github.com/zeit/next-plugins).

### Lire plus sur Next.js

Je ne peux pas décrire toutes les fonctionnalités de ce framework génial, et le principal endroit pour en savoir plus sur Next.js est [le fichier readme du projet sur GitHub](https://github.com/zeit/next.js/blob/canary/readme.md).

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)