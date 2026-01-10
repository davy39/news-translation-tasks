---
title: Le manuel Next.js – Apprendre Next.js pour les débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-11-19T08:15:52.000Z'
originalURL: https://freecodecamp.org/news/the-next-js-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Group-1.png
tags:
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: Next.js
  slug: nextjs
- name: React
  slug: reactjs
seo_title: Le manuel Next.js – Apprendre Next.js pour les débutants
seo_desc: 'I wrote this tutorial to help you quickly learn Next.js and get familiar
  with how it works.

  It''s ideal for you if you have zero to little knowledge of Next.js, you have used
  React in the past, and you are looking forward diving more into the React ec...'
---

J'ai écrit ce tutoriel pour vous aider à apprendre rapidement Next.js et à vous familiariser avec son fonctionnement.

Il est idéal pour vous si vous avez peu ou pas de connaissances sur Next.js, si vous avez utilisé React dans le passé, et si vous souhaitez approfondir l'écosystème React, en particulier le rendu côté serveur.

Je trouve Next.js un outil génial pour créer des applications Web, et à la fin de cet article, j'espère que vous serez aussi excité que moi à ce sujet. Et j'espère qu'il vous aidera à apprendre Next.js !

[Note : vous pouvez télécharger une version PDF / ePub / Mobi de ce tutoriel pour le lire hors ligne](https://flaviocopes.com/page/nextjs-handbook/)

## Index

1. [Introduction](#heading-introduction)
2. [Les principales fonctionnalités fournies par Next.js](#heading-les-principales-fonctionnalités-fournies-par-nextjs)
3. [Next.js vs Gatsby vs `create-react-app`](#heading-nextjs-vs-gatsby-vs-create-react-app)
4. [Comment installer Next.js](#heading-comment-installer-nextjs)
5. [Voir la source pour confirmer que le SSR fonctionne](#heading-voir-la-source-pour-confirmer-que-le-ssr-fonctionne)
6. [Les bundles de l'application](#heading-les-bundles-de-lapplication)
7. [Qu'est-ce que cette icône en bas à droite ?](#heading-quest-ce-que-cette-icône-en-bas-à-droite)
8. [Installer les React DevTools](#heading-installer-les-react-devtools)
9. [Autres techniques de débogage que vous pouvez utiliser](#heading-autres-techniques-de-débogage-que-vous-pouvez-utiliser)
10. [Ajouter une deuxième page au site](#heading-ajouter-une-deuxième-page-au-site)
11. [Lier les deux pages](#heading-lier-les-deux-pages)
12. [Contenu dynamique avec le routeur](#heading-contenu-dynamique-avec-le-routeur)
13. [Préchargement](#heading-préchargement)
14. [Utiliser le routeur pour détecter le lien actif](#heading-utiliser-le-routeur-pour-détecter-le-lien-actif)
15. [Utiliser `next/router`](#heading-utiliser-nextrouter)
16. [Alimenter les composants avec des données en utilisant `getInitialProps()`](#heading-alimenter-les-composants-avec-des-données-en-utilisant-getinitialprops)
17. [CSS](#heading-css)
18. [Remplir la balise head avec des balises personnalisées](#heading-remplir-la-balise-head-avec-des-balises-personnalisées)
19. [Ajouter un composant wrapper](#heading-ajouter-un-composant-wrapper)
20. [Routes API](#heading-routes-api)
21. [Exécuter du code côté serveur ou côté client](#heading-exécuter-du-code-côté-serveur-ou-côté-client)
22. [Déployer la version de production](#heading-déployer-la-version-de-production)
23. [Déployer sur Now](#heading-déployer-sur-now)
24. [Analyser les bundles de l'application](#heading-analyser-les-bundles-de-lapplication)
25. [Chargement paresseux des modules](#heading-chargement-paresseux-des-modules)
26. [Où aller à partir d'ici](#heading-où-aller-à-partir-dici)

## Introduction

Travailler sur une application JavaScript moderne alimentée par React est génial jusqu'à ce que vous réalisiez qu'il y a quelques problèmes liés au rendu de tout le contenu côté client.

Premièrement, la page prend plus de temps à devenir visible pour l'utilisateur, car avant que le contenu ne se charge, tout le JavaScript doit se charger, et votre application doit s'exécuter pour déterminer ce qu'il faut afficher sur la page.

Deuxièmement, si vous construisez un site web public, vous avez un problème de SEO de contenu. Les moteurs de recherche s'améliorent pour exécuter et indexer les applications JavaScript, mais c'est beaucoup mieux si nous pouvons leur envoyer du contenu au lieu de les laisser le découvrir.

La solution à ces deux problèmes est le **rendu côté serveur**, également appelé **pré-rendu statique**.

[Next.js](https://nextjs.org) est un framework React pour faire tout cela de manière très simple, mais il ne se limite pas à cela. Il est présenté par ses créateurs comme un **outil de chaîne de construction zéro-configuration, à commande unique pour les applications React**.

Il fournit une structure commune qui vous permet de construire facilement une application frontend React, et gère transparemment le rendu côté serveur pour vous.

## Les principales fonctionnalités fournies par Next.js

Voici une liste non exhaustive des principales fonctionnalités de Next.js :

### Rechargement à chaud du code

Next.js recharge la page lorsqu'il détecte un changement enregistré sur le disque.

### Routage automatique

Toute URL est mappée au système de fichiers, aux fichiers placés dans le dossier `pages`, et vous n'avez besoin d'aucune configuration (vous avez bien sûr des options de personnalisation).

### Composants en un seul fichier

En utilisant `styled-jsx`, complètement intégré et construit par la même équipe, il est trivial d'ajouter des styles limités au composant.

### Rendu côté serveur

Vous pouvez rendre les composants React côté serveur, avant d'envoyer le HTML au client.

### Compatibilité avec l'écosystème

Next.js s'intègre bien avec le reste de l'écosystème JavaScript, Node et React.

### Fractionnement automatique du code

Les pages sont rendues avec uniquement les bibliothèques et le JavaScript dont elles ont besoin, pas plus. Au lieu de générer un seul fichier JavaScript contenant tout le code de l'application, l'application est automatiquement divisée par Next.js en plusieurs ressources différentes.

Le chargement d'une page ne charge que le JavaScript nécessaire à cette page particulière.

Next.js fait cela en analysant les ressources importées.

Si seulement une de vos pages importe la bibliothèque Axios, par exemple, cette page spécifique inclura la bibliothèque dans son bundle.

Cela garantit que le premier chargement de votre page est aussi rapide que possible, et seuls les futurs chargements de pages (s'ils sont jamais déclenchés) enverront le JavaScript nécessaire au client.

Il y a une exception notable. Les imports fréquemment utilisés sont déplacés dans le bundle JavaScript principal s'ils sont utilisés dans au moins la moitié des pages du site.

### Préchargement

Le composant `Link`, utilisé pour lier différentes pages, prend en charge une propriété `prefetch` qui précharge automatiquement les ressources de la page (y compris le code manquant en raison du fractionnement de code) en arrière-plan.

### Composants dynamiques

Vous pouvez importer des modules JavaScript et des composants React de manière dynamique.

### Exportations statiques

En utilisant la commande `next export`, Next.js vous permet d'exporter un site entièrement statique à partir de votre application.

### Support TypeScript

Next.js est écrit en TypeScript et offre donc un excellent support pour TypeScript.

## Next.js vs Gatsby vs `create-react-app`

Next.js, [Gatsby](https://flaviocopes.com/gatsby/), et [`create-react-app`](https://flaviocopes.com/react-create-react-app/) sont des outils incroyables que nous pouvons utiliser pour alimenter nos applications.

Commençons par dire ce qu'ils ont en commun. Ils ont tous React sous le capot, alimentant toute l'expérience de développement. Ils abstraient également [webpack](https://flaviocopes.com/webpack/) et toutes ces choses de bas niveau que nous devions configurer manuellement dans le bon vieux temps.

`create-react-app` ne vous aide pas à générer facilement une application rendue côté serveur. Tout ce qui vient avec (SEO, vitesse...) n'est fourni que par des outils comme Next.js et Gatsby.

**Quand Next.js est-il meilleur que Gatsby ?**

Ils peuvent tous deux aider avec le **rendu côté serveur**, mais de 2 manières différentes.

Le résultat final avec Gatsby est un générateur de site statique, sans serveur. Vous construisez le site, puis vous déployez le résultat du processus de construction de manière statique sur Netlify ou un autre site d'hébergement statique.

Next.js fournit un backend qui peut rendre côté serveur une réponse à une requête, vous permettant de créer un site web dynamique, ce qui signifie que vous le déployez sur une plateforme qui peut exécuter Node.js.

Next.js _peut_ également générer un site statique, mais je ne dirais pas que c'est son cas d'utilisation principal.

Si mon objectif était de construire un site statique, j'aurais du mal à choisir et peut-être que Gatsby a un meilleur écosystème de plugins, y compris beaucoup pour le blogging en particulier.

Gatsby est également fortement basé sur [GraphQL](https://flaviocopes.com/graphql/), quelque chose que vous pourriez vraiment aimer ou non en fonction de vos opinions et besoins.

## Comment installer Next.js

Pour installer Next.js, vous devez avoir Node.js installé.

Assurez-vous d'avoir la dernière version de Node. Vérifiez en exécutant `node -v` dans votre terminal, et comparez-le à la dernière version LTS listée sur [https://nodejs.org/](https://nodejs.org/).

Après avoir installé Node.js, vous aurez la commande `npm` disponible dans votre ligne de commande.

Si vous avez des problèmes à ce stade, je vous recommande les tutoriels suivants que j'ai écrits pour vous :

* [Comment installer Node.js](https://flaviocopes.com/node-installation/)
* [Comment mettre à jour Node.js](https://flaviocopes.com/how-to-update-node/)
* [Une introduction au gestionnaire de paquets npm](https://flaviocopes.com/npm/)
* [Tutoriel sur les shells Unix](https://flaviocopes.com/shells/)
* [Comment utiliser le terminal macOS](https://flaviocopes.com/macos-terminal/)
* [Le shell Bash](https://flaviocopes.com/bash/)

Maintenant que vous avez Node, mis à jour à la dernière version, et `npm`, nous sommes prêts !

Nous pouvons choisir 2 routes maintenant : utiliser `create-next-app` ou l'approche classique qui implique d'installer et de configurer une application Next manuellement.

### Utiliser create-next-app

Si vous êtes familier avec [`create-react-app`](https://flaviocopes.com/react-create-react-app/), `create-next-app` est la même chose - sauf qu'il crée une application Next au lieu d'une application React, comme son nom l'indique.

Je suppose que vous avez déjà installé Node.js, qui, à partir de la version 5.2 (il y a plus de 2 ans au moment de l'écriture), est livré avec la commande [`npx`](https://flaviocopes.com/npx/) incluse. Cet outil pratique nous permet de télécharger et d'exécuter une commande JavaScript, et nous l'utiliserons comme ceci :

```bash
npx create-next-app

```

La commande demande le nom de l'application (et crée un nouveau dossier pour vous avec ce nom), puis télécharge tous les paquets dont elle a besoin (`react`, `react-dom`, `next`), définit le `package.json` à :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-14-at-16.46.47.png)

et vous pouvez immédiatement exécuter l'application d'exemple en exécutant `npm run dev` :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-14-at-16.46.32.png)

Et voici le résultat sur [http://localhost:3000](http://localhost:3000) :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-14-at-16.47.17.png)

C'est la manière recommandée de démarrer une application Next.js, car elle vous donne une structure et un code d'exemple avec lequel jouer. Il y a plus que cette simple application d'exemple par défaut ; vous pouvez utiliser l'un des exemples stockés à [https://github.com/zeit/next.js/tree/canary/examples](https://github.com/zeit/next.js/tree/canary/examples) en utilisant l'option `--example`. Par exemple, essayez :

```bash
npx create-next-app --example blog-starter

```

Ce qui vous donne une instance de blog immédiatement utilisable avec la coloration syntaxique :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-14-at-17.13.29.png)

### Créer manuellement une application Next.js

Vous pouvez éviter `create-next-app` si vous souhaitez créer une application Next à partir de zéro. Voici comment : créez un dossier vide où vous le souhaitez, par exemple dans votre dossier personnel, et allez dedans :

```sh
mkdir nextjs
cd nextjs

```

et créez votre premier répertoire de projet Next :

```sh
mkdir firstproject
cd firstproject

```

Maintenant, utilisez la commande `npm` pour l'initialiser en tant que projet Node :

```sh
npm init -y

```

L'option `-y` indique à `npm` d'utiliser les paramètres par défaut pour un projet, en remplissant un fichier `package.json` d'exemple.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-16.59.21.png)

Maintenant, installez Next et React :

```sh
npm install next react react-dom

```

Votre dossier de projet devrait maintenant contenir 2 fichiers :

* `package.json` ([voir mon tutoriel à ce sujet](https://flaviocopes.com/package-json/))
* `package-lock.json` ([voir mon tutoriel sur package-lock](https://flaviocopes.com/package-lock-json/))

et le dossier `node_modules`.

Ouvrez le dossier du projet en utilisant votre éditeur préféré. Mon éditeur préféré est [VS Code](https://flaviocopes.com/vscode/). Si vous l'avez installé, vous pouvez exécuter `code .` dans votre terminal pour ouvrir le dossier actuel dans l'éditeur (si la commande ne fonctionne pas pour vous, voir [ceci](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line))

Ouvrez `package.json`, qui contient maintenant ce contenu :

```json
{
  "name": "firstproject",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies":  {
    "next": "^9.1.2",
    "react": "^16.11.0",
    "react-dom": "^16.11.0"
  }
}

```

et remplacez la section `scripts` par :

```json
"scripts": {
  "dev": "next",
  "build": "next build",
  "start": "next start"
}

```

pour ajouter les commandes de construction de Next.js, que nous allons utiliser bientôt.

Astuce : utilisez `"dev": "next -p 3001",` pour changer le port et exécuter, dans cet exemple, sur le port 3001.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-17.01.03.png)

Maintenant, créez un dossier `pages`, et ajoutez un fichier `index.js`.

Dans ce fichier, créons notre premier composant React.

Nous allons l'utiliser comme exportation par défaut :

```js
const Index = () => (
  <div>
    <h1>Page d'accueil</h1>
  </div>
)

export default Index

```

Maintenant, en utilisant le terminal, exécutez `npm run dev` pour démarrer le serveur de développement Next.

Cela rendra l'application disponible sur le port 3000, en local.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-11.24.02.png)

Ouvrez [http://localhost:3000](http://localhost:3000) dans votre navigateur pour le voir.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-11.24.23.png)

## Voir la source pour confirmer que le SSR fonctionne

Vérifions maintenant que l'application fonctionne comme nous nous y attendons. C'est une application Next.js, donc elle devrait être **rendue côté serveur**.

C'est l'un des principaux arguments de vente de Next.js : si nous créons un site en utilisant Next.js, les pages du site sont rendues sur le serveur, qui envoie du HTML au navigateur.

Cela présente 3 avantages majeurs :

* Le client n'a pas besoin d'instancier React pour rendre, ce qui rend le site plus rapide pour vos utilisateurs.
* Les moteurs de recherche indexeront les pages sans avoir besoin d'exécuter le JavaScript côté client. Quelque chose que Google a commencé à faire, mais a ouvertement admis être un processus plus lent (et vous devriez aider Google autant que possible, si vous voulez bien vous classer).
* Vous pouvez avoir des méta-balises pour les réseaux sociaux, utiles pour ajouter des images de prévisualisation, personnaliser le titre et la description pour toutes vos pages partagées sur Facebook, Twitter et ainsi de suite.

Regardons le code source de l'application. 
En utilisant Chrome, vous pouvez faire un clic droit n'importe où dans la page, et appuyer sur **Afficher le code source de la page**.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-11.33.10.png)

Si vous regardez le code source de la page, vous verrez le snippet `<div><h1>Page d'accueil</h1></div>` dans le `body` HTML, ainsi qu'un ensemble de fichiers JavaScript - les bundles de l'application.

Nous n'avons pas besoin de configurer quoi que ce soit, le SSR (rendu côté serveur) fonctionne déjà pour nous.

L'application React sera lancée sur le client, et sera celle qui alimentera les interactions comme le clic sur un lien, en utilisant le rendu côté client. Mais le rechargement d'une page la rechargera depuis le serveur. Et en utilisant Next.js, il ne devrait y avoir aucune différence dans le résultat à l'intérieur du navigateur - une page rendue côté serveur devrait ressembler exactement à une page rendue côté client.

## Les bundles de l'application

Lorsque nous avons regardé le code source de la page, nous avons vu un ensemble de fichiers JavaScript chargés :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-11.34.41.png)

Commençons par mettre le code dans un [formateur HTML](https://htmlformatter.com/) pour le formater correctement, afin que nous, humains, puissions mieux le comprendre :

```html
<!DOCTYPE html>
<html>

<head>
    <meta charSet="utf-8" />
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1" />
    <meta name="next-head-count" content="2" />
    <link rel="preload" href="/_next/static/development/pages/index.js?ts=1572863116051" as="script" />
    <link rel="preload" href="/_next/static/development/pages/_app.js?ts=1572863116051" as="script" />
    <link rel="preload" href="/_next/static/runtime/webpack.js?ts=1572863116051" as="script" />
    <link rel="preload" href="/_next/static/runtime/main.js?ts=1572863116051" as="script" />
</head>

<body>
    <div id="__next">
        <div>
            <h1>Page d'accueil</h1></div>
    </div>
    <script src="/_next/static/development/dll/dll_01ec57fc9b90d43b98a8.js?ts=1572863116051"></script>
    <script id="__NEXT_DATA__" type="application/json">{"dataManager":"[]","props":{"pageProps":{}},"page":"/","query":{},"buildId":"development","nextExport":true,"autoExport":true}</script>
    <script async="" data-next-page="/" src="/_next/static/development/pages/index.js?ts=1572863116051"></script>
    <script async="" data-next-page="/_app" src="/_next/static/development/pages/_app.js?ts=1572863116051"></script>
    <script src="/_next/static/runtime/webpack.js?ts=1572863116051" async=""></script>
    <script src="/_next/static/runtime/main.js?ts=1572863116051" async=""></script>
</body>

</html>

```

Nous avons 4 fichiers JavaScript déclarés pour être préchargés dans le `head`, en utilisant `rel="preload" as="script"` :

* `/_next/static/development/pages/index.js` (96 LOC)
* `/_next/static/development/pages/_app.js` (5900 LOC)
* `/_next/static/runtime/webpack.js` (939 LOC)
* `/_next/static/runtime/main.js` (12k LOC)

Cela indique au navigateur de commencer à charger ces fichiers dès que possible, avant que le flux de rendu normal ne commence. Sans ceux-ci, les scripts seraient chargés avec un délai supplémentaire, et cela améliore les performances de chargement de la page.

Ensuite, ces 4 fichiers sont chargés à la fin du `body`, ainsi que `/_next/static/development/dll/dll_01ec57fc9b90d43b98a8.js` (31k LOC), et un extrait JSON qui définit certains paramètres par défaut pour les données de la page :

```html
<script id="__NEXT_DATA__" type="application/json">
{
  "dataManager": "[]",
  "props": {
    "pageProps":  {}
  },
  "page": "/",
  "query": {},
  "buildId": "development",
  "nextExport": true,
  "autoExport": true
}
</script>

```

Les 4 fichiers de bundle chargés implémentent déjà une fonctionnalité appelée fractionnement de code. Le fichier `index.js` fournit le code nécessaire pour le composant `index`, qui sert la route `/`, et si nous avions plus de pages, nous aurions plus de bundles pour chaque page, qui ne seront chargés que si nécessaire - pour fournir un temps de chargement plus performant pour la page.

## Qu'est-ce que cette icône en bas à droite ?

Avez-vous vu cette petite icône en bas à droite de la page, qui ressemble à un éclair ?

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-13.21.42.png)

Si vous passez la souris dessus, elle dira "Page pré-rendue" :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-13.21.46.png)

Cette icône, qui n'est _visible qu'en mode développement_, vous indique que la page est éligible pour l'optimisation statique automatique, ce qui signifie essentiellement qu'elle ne dépend pas de données qui doivent être récupérées au moment de l'invocation, et qu'elle peut être pré-rendue et construite en tant que fichier HTML statique au moment de la construction (lorsque nous exécutons `npm run build`).

Next peut déterminer cela par l'absence de la méthode `getInitialProps()` attachée au composant de la page.

Lorsque c'est le cas, notre page peut être encore plus rapide car elle sera servie statiquement en tant que fichier HTML plutôt que de passer par le serveur Node.js qui génère la sortie HTML.

Une autre icône utile qui peut apparaître à côté, ou à la place sur les pages non pré-rendues, est un petit triangle animé :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-14-at-14.56.21.png)

C'est un indicateur de compilation, et il apparaît lorsque vous enregistrez une page et que Next.js compile l'application avant que le rechargement à chaud du code ne se déclenche pour recharger le code dans l'application automatiquement.

C'est une très bonne façon de déterminer immédiatement si l'application a déjà été compilée et si vous pouvez tester une partie sur laquelle vous travaillez.

## Installer les React DevTools

Next.js est basé sur React, donc un outil très utile que nous devons absolument installer (si vous ne l'avez pas déjà fait) est les React Developer Tools.

Disponibles pour [Chrome](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) et [Firefox](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/), les React Developer Tools sont un instrument essentiel que vous pouvez utiliser pour inspecter une application React.

Maintenant, les React Developer Tools ne sont pas spécifiques à Next.js mais je veux les présenter car vous n'êtes peut-être pas à 100% familier avec tous les outils que React fournit. Il est préférable d'approfondir un peu les outils de débogage plutôt que de supposer que vous les connaissez déjà.

Ils fournissent un inspecteur qui révèle l'arborescence des composants React qui construit votre page, et pour chaque composant, vous pouvez aller vérifier les props, l'état, les hooks, et bien plus encore.

Une fois que vous avez installé les React Developer Tools, vous pouvez ouvrir les outils de développement du navigateur habituels (dans Chrome, c'est un clic droit dans la page, puis cliquez sur `Inspecter`) et vous trouverez 2 nouveaux panneaux : **Composants** et **Profiler**.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-14.26.12.png)

Si vous déplacez la souris sur les composants, vous verrez que dans la page, le navigateur sélectionnera les parties qui sont rendues par ce composant.

Si vous sélectionnez un composant dans l'arborescence, le panneau de droite vous montrera une référence au **composant parent**, et les props qui lui sont passés :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-14.27.05.png)

Vous pouvez facilement naviguer en cliquant sur les noms des composants.

Vous pouvez cliquer sur l'icône en forme d'œil dans la barre d'outils des Developer Tools pour inspecter l'élément DOM, et également, si vous utilisez la première icône, celle avec l'icône de la souris (qui se trouve commodément sous l'icône DevTools similaire), vous pouvez survoler un élément dans l'interface utilisateur du navigateur pour sélectionner directement le composant React qui le rend.

Vous pouvez utiliser l'icône `bug` pour journaliser les données d'un composant dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-14.31.25.png)

C'est assez génial car une fois que vous avez les données imprimées là, vous pouvez faire un clic droit sur n'importe quel élément et appuyer sur "Stocker comme variable globale". Par exemple, ici, je l'ai fait avec la prop `url`, et j'ai pu l'inspecter dans la console en utilisant la variable temporaire qui lui a été assignée, `temp1` :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-14.40.22.png)

En utilisant les **Source Maps**, qui sont chargées par Next.js automatiquement en mode développement, à partir du panneau Composants, nous pouvons cliquer sur le code `<>` et les DevTools basculeront vers le panneau Source, nous montrant le code source du composant :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-14.41.33.png)

L'onglet **Profiler** est encore plus génial, si possible. Il nous permet d'**enregistrer une interaction** dans l'application, et de voir ce qui se passe. Je ne peux pas encore montrer d'exemple, car il faut au moins 2 composants pour créer une interaction, et nous n'en avons qu'un pour l'instant. J'en parlerai plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-14.42.24.png)

J'ai montré toutes les captures d'écran en utilisant Chrome, mais les React Developer Tools fonctionnent de la même manière dans Firefox :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-14.45.20.png)

## Autres techniques de débogage que vous pouvez utiliser

En plus des React Developer Tools, qui sont essentiels pour construire une application Next.js, je veux souligner 2 façons de déboguer les applications Next.js.

La première est évidemment `console.log()` et tous les autres outils de l'[API Console](https://flaviocopes.com/console-api/). La manière dont les applications Next fonctionnent fera qu'une instruction de journalisation fonctionnera dans la console du navigateur OU dans le terminal où vous avez démarré Next en utilisant `npm run dev`.

En particulier, si la page se charge depuis le serveur, lorsque vous pointez l'URL vers elle, ou que vous appuyez sur le bouton d'actualisation / cmd/ctrl-R, toute journalisation de la console se produit dans le terminal.

Les transitions de page suivantes qui se produisent en cliquant sur la souris feront que toute journalisation de la console se produira à l'intérieur du navigateur.

Rappelez-vous simplement si vous êtes surpris par des journaux manquants.

Un autre outil qui est essentiel est l'instruction `debugger`. L'ajout de cette instruction à un composant mettra en pause le rendu du navigateur de la page :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-15.10.32.png)

Vraiment génial car maintenant vous pouvez utiliser le débogueur du navigateur pour inspecter les valeurs et exécuter votre application ligne par ligne.

Vous pouvez également utiliser le débogueur VS Code pour déboguer le code côté serveur. Je mentionne cette technique et [ce tutoriel](https://github.com/Microsoft/vscode-recipes/tree/master/Next-js) pour le configurer.

## Ajouter une deuxième page au site

Maintenant que nous avons une bonne compréhension des outils que nous pouvons utiliser pour nous aider à développer des applications Next.js, continuons à partir de l'endroit où nous avons laissé notre première application :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-13.21.42-1.png)

Je veux ajouter une deuxième page à ce site web, un blog. Il sera servi dans `/blog`, et pour l'instant, il contiendra simplement une page statique, tout comme notre premier composant `index.js` :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-15.39.40.png)

Après avoir enregistré le nouveau fichier, le processus `npm run dev` déjà en cours d'exécution est déjà capable de rendre la page, sans avoir besoin de le redémarrer.

Lorsque nous accédons à l'URL [http://localhost:3000/blog](http://localhost:3000/blog), nous avons la nouvelle page :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-15.41.39.png)

et voici ce que le terminal nous a dit :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-15.41.03.png)

Maintenant, le fait que l'URL soit `/blog` dépend uniquement du nom du fichier et de sa position sous le dossier `pages`.

Vous pouvez créer une page `pages/hey/ho`, et cette page s'affichera sur l'URL [http://localhost:3000/hey/ho](http://localhost:3000/hey/ho).

Ce qui n'a pas d'importance, pour les besoins de l'URL, c'est le nom du composant à l'intérieur du fichier.

Essayez d'aller voir le code source de la page, lorsqu'elle est chargée depuis le serveur, elle listera `/_next/static/development/pages/blog.js` comme l'un des bundles chargés, et non `/_next/static/development/pages/index.js` comme dans la page d'accueil. Cela est dû au fractionnement automatique du code, nous n'avons pas besoin du bundle qui sert la page d'accueil. Juste le bundle qui sert la page du blog.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-16.24.53.png)

Nous pouvons également simplement exporter une fonction anonyme depuis `blog.js` :

```js
export default () => (
  <div>
    <h1>Blog</h1>
  </div>
)

```

ou si vous préférez la syntaxe de fonction non-fléchée :

```js
export default function() {
  return (
    <div>
      <h1>Blog</h1>
    </div>
  )
}

```

## Lier les deux pages

Maintenant que nous avons 2 pages, définies par `index.js` et `blog.js`, nous pouvons introduire des liens.

Les liens HTML normaux au sein des pages sont faits en utilisant la balise `a` :

```html
<a href="/blog">Blog</a>

```

Nous ne pouvons pas faire cela dans Next.js.

Pourquoi ? Nous pouvons techniquement le faire, bien sûr, car c'est le Web et sur le Web, les choses ne se cassent jamais (c'est pourquoi nous pouvons encore utiliser la balise `<marquee>`. Mais l'un des principaux avantages de l'utilisation de Next est que, une fois qu'une page est chargée, les transitions vers d'autres pages sont très rapides grâce au rendu côté client.

Si vous utilisez un lien `a` simple :

```js
const Index = () => (
  <div>
    <h1>Page d'accueil</h1>
    <a href='/blog'>Blog</a>
  </div>
)

export default Index

```

Maintenant, ouvrez les **DevTools**, et en particulier le **panneau Réseau**. La première fois que nous chargeons `http://localhost:3000/`, nous obtenons tous les bundles de la page chargés :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-16.26.00.png)

Maintenant, si vous cliquez sur le bouton "Conserver le journal" (pour éviter d'effacer le panneau Réseau), et cliquez sur le lien "Blog", voici ce qui se passe :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-16.27.16.png)

Nous avons obtenu tout ce JavaScript depuis le serveur, encore ! Mais... nous n'avons pas besoin de tout ce JavaScript si nous l'avons déjà. Nous aurions juste besoin du bundle de la page `blog.js`, le seul qui est nouveau pour la page.

Pour résoudre ce problème, nous utilisons un composant fourni par Next, appelé Link.

Nous l'importons :

```js
import Link from 'next/link'

```

et ensuite nous l'utilisons pour envelopper notre lien, comme ceci :

```js
import Link from 'next/link'

const Index = () => (
  <div>
    <h1>Page d'accueil</h1>
    <Link href='/blog'>
      <a>Blog</a>
    </Link>
  </div>
)

export default Index

```

Maintenant, si vous réessayez ce que nous avons fait précédemment, vous pourrez voir que seul le bundle `blog.js` est chargé lorsque nous passons à la page du blog :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-04-at-16.35.18.png)

et la page s'est chargée si rapidement qu'avant, le spinner habituel du navigateur sur l'onglet n'est même pas apparu. Pourtant, l'URL a changé, comme vous pouvez le voir. Cela fonctionne de manière transparente avec l'API [History](https://flaviocopes.com/history-api/) du navigateur.

C'est le rendu côté client en action.

Et si vous appuyez maintenant sur le bouton de retour ? Rien n'est chargé, car le navigateur a toujours l'ancien bundle `index.js` en place, prêt à charger la route `/index`. Tout est automatique !

## Contenu dynamique avec le routeur

Dans le chapitre précédent, nous avons vu comment lier la page d'accueil à la page du blog.

Un blog est un excellent cas d'utilisation pour Next.js, que nous continuerons à explorer dans ce chapitre en ajoutant des **articles de blog**.

Les articles de blog ont une URL dynamique. Par exemple, un article intitulé "Hello World" pourrait avoir l'URL `/blog/hello-world`. Un article intitulé "My second post" pourrait avoir l'URL `/blog/my-second-post`.

Ce contenu est dynamique et peut provenir d'une base de données, de fichiers markdown ou autre.

Next.js peut servir du contenu dynamique basé sur une **URL dynamique**.

Nous créons une URL dynamique en créant une page dynamique avec la syntaxe `[]`.

Comment ? Nous ajoutons un fichier `pages/blog/[id].js`. Ce fichier gérera toutes les URL dynamiques sous la route `/blog/`, comme celles que nous avons mentionnées ci-dessus : `/blog/hello-world`, `/blog/my-second-post` et plus.

Dans le nom du fichier, `[id]` entre crochets signifie que tout ce qui est dynamique sera mis dans le paramètre `id` de la **propriété query** du **routeur**.

D'accord, c'est un peu trop de choses à la fois.

Qu'est-ce que le **routeur** ?

Le routeur est une bibliothèque fournie par Next.js.

Nous l'importons depuis `next/router` :

```js
import { useRouter } from 'next/router'

```

et une fois que nous avons `useRouter`, nous instancions l'objet routeur en utilisant :

```js
const router = useRouter()

```

Une fois que nous avons cet objet routeur, nous pouvons en extraire des informations.

En particulier, nous pouvons obtenir la partie dynamique de l'URL dans le fichier `[id].js` en accédant à `router.query.id`.

La partie dynamique peut également être juste une portion de l'URL, comme `post-[id].js`.

Alors, appliquons toutes ces choses en pratique.

Créez le fichier `pages/blog/[id].js` :

```js
import { useRouter } from 'next/router'

export default () => {
  const router = useRouter()

  return (
    <>
      <h1>Article de blog</h1>
      <p>ID de l'article : {router.query.id}</p>
    </>
  )
}

```

Maintenant, si vous allez sur le routeur `http://localhost:3000/blog/test`, vous devriez voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-05-at-16.41.32.png)

Nous pouvons utiliser ce paramètre `id` pour récupérer l'article d'une liste d'articles. D'une base de données, par exemple. Pour garder les choses simples, nous ajouterons un fichier `posts.json` dans le dossier racine du projet :

```js
{
  "test": {
    "title": "test post",
    "content": "Hey some post content"
  },
  "second": {
    "title": "second post",
    "content": "Hey this is the second post content"
  }
}

```

Maintenant, nous pouvons l'importer et rechercher l'article à partir de la clé `id` :

```js
import { useRouter } from 'next/router'
import posts from '../../posts.json'

export default () => {
  const router = useRouter()

  const post = posts[router.query.id]

  return (
    <>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </>
  )
}

```

Le rechargement de la page devrait nous montrer ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-05-at-16.44.07.png)

Mais ce n'est pas le cas ! Au lieu de cela, nous obtenons une erreur dans la console, et une erreur dans le navigateur aussi :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-05-at-18.18.17.png)

Pourquoi ? Parce que... pendant le rendu, lorsque le composant est initialisé, les données ne sont pas encore là. Nous verrons comment fournir les données au composant avec getInitialProps dans la prochaine leçon.

Pour l'instant, ajoutez une petite vérification `if (!post) return <p></p>` avant de retourner le JSX :

```js
import { useRouter } from 'next/router'
import posts from '../../posts.json'

export default () => {
  const router = useRouter()

  const post = posts[router.query.id]
  if (!post) return <p></p>

  return (
    <>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </>
  )
}

```

Maintenant, les choses devraient fonctionner. Initialement, le composant est rendu sans les informations dynamiques `router.query.id`. Après le rendu, Next.js déclenche une mise à jour avec la valeur de la requête et la page affiche les informations correctes.

Et si vous regardez le code source, il y a cette balise `<p>` vide dans le HTML :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-05-at-18.20.58.png)

Nous allons bientôt corriger ce problème qui échoue à implémenter le SSR et qui nuit à la fois aux temps de chargement pour nos utilisateurs, au SEO et au partage social comme nous l'avons déjà discuté.

Nous pouvons compléter l'exemple du blog en listant ces articles dans `pages/blog.js` :

```js
import posts from '../posts.json'

const Blog = () => (
  <div>
    <h1>Blog</h1>

    <ul>
      {Object.entries(posts).map((value, index) => {
        return <li key={index}>{value[1].title}</li>
      })}
    </ul>
  </div>
)

export default Blog

```

Et nous pouvons les lier aux pages individuelles des articles, en important `Link` depuis `next/link` et en l'utilisant dans la boucle des articles :

```js
import Link from 'next/link'
import posts from '../posts.json'

const Blog = () => (
  <div>
    <h1>Blog</h1>

    <ul>
      {Object.entries(posts).map((value, index) => {
        return (
          <li key={index}>
            <Link href='/blog/[id]' as={'/blog/' + value[0]}>
              <a>{value[1].title}</a>
            </Link>
          </li>
        )
      })}
    </ul>
  </div>
)

export default Blog

```

## Préchargement

J'ai mentionné précédemment comment le composant `Link` de Next.js peut être utilisé pour créer des liens entre 2 pages, et lorsque vous l'utilisez, Next.js **gère transparemment le routage frontal** pour nous, donc lorsqu'un utilisateur clique sur un lien, le frontal se charge d'afficher la nouvelle page sans déclencher un nouveau cycle de requête et de réponse client/serveur, comme cela se produit normalement avec les pages web.

Il y a une autre chose que Next.js fait pour vous lorsque vous utilisez `Link`.

Dès qu'un élément enveloppé dans `<Link>` apparaît dans la fenêtre visible (ce qui signifie qu'il est visible pour l'utilisateur du site web), Next.js précharge l'URL vers laquelle il pointe, tant qu'il s'agit d'un lien local (sur votre site web), rendant l'application super rapide pour le spectateur.

Ce comportement n'est déclenché qu'en **mode production** (nous en parlerons plus en détail plus tard), ce qui signifie que vous devez arrêter l'application si vous l'exécutez avec `npm run dev`, compiler votre bundle de production avec `npm run build` et l'exécuter avec `npm run start` à la place.

En utilisant l'inspecteur de réseau dans les DevTools, vous remarquerez que tous les liens au-dessus de la ligne de flottaison, au chargement de la page, commencent le préchargement dès que l'événement `load` a été déclenché sur votre page (déclenché lorsque la page est entièrement chargée, et se produit après l'événement `DOMContentLoaded`).

Toute autre balise `Link` non dans la fenêtre visible sera préchargée lorsque l'utilisateur fait défiler et qu'elle

Le préchargement est automatique sur les connexions haut débit (connexions Wifi et 3g+), sauf si le navigateur envoie l'en-tête HTTP [`Save-Data`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Save-Data).

Vous pouvez vous désinscrire du préchargement des instances individuelles de `Link` en définissant la prop `prefetch` sur `false` :

```jsx
<Link href="/a-link" prefetch={false}>
  <a>Un lien</a>
</Link>

```

## Utiliser le routeur pour détecter le lien actif

Une fonctionnalité très importante lors de la gestion des liens est de déterminer quelle est l'URL actuelle, et en particulier d'assigner une classe au lien actif, afin que nous puissions le styliser différemment des autres.

Cela est particulièrement utile dans l'en-tête de votre site, par exemple.

Le composant `Link` par défaut de Next.js offert dans `next/link` ne fait pas cela automatiquement pour nous.

Nous pouvons créer un composant Link nous-mêmes, et nous le stockons dans un fichier `Link.js` dans le dossier Components, et nous importons celui-ci au lieu du `next/link` par défaut.

Dans ce composant, nous importons d'abord React depuis `react`, Link depuis `next/link` et le hook `useRouter` depuis `next/router`.

À l'intérieur du composant, nous déterminons si le nom du chemin actuel correspond à la prop `href` du composant, et si c'est le cas, nous ajoutons la classe `selected` aux enfants.

Nous retournons finalement ces enfants avec la classe mise à jour, en utilisant `React.cloneElement()` :

```js
import React from 'react'
import Link from 'next/link'
import { useRouter } from 'next/router'

export default ({ href, children }) => {
  const router = useRouter()

  let className = children.props.className || ''
  if (router.pathname === href) {
    className = `${className} selected`
  }

  return <Link href={href}>{React.cloneElement(children, { className })}</Link>
}

```

## Utiliser `next/router`

Nous avons déjà vu comment utiliser le composant Link pour gérer le routage de manière déclarative dans les applications Next.js.

C'est vraiment pratique pour gérer le routage dans JSX, mais parfois vous devez déclencher un changement de routage de manière programmatique.

Dans ce cas, vous pouvez accéder directement au routeur Next.js, fourni dans le package `next/router`, et appeler sa méthode `push()`.

Voici un exemple d'accès au routeur :

```js
import { useRouter } from 'next/router'

export default () => {
  const router = useRouter()
  //...
}

```

Une fois que nous obtenons l'objet routeur en invoquant `useRouter()`, nous pouvons utiliser ses méthodes.

Il s'agit du routeur côté client, donc les méthodes ne doivent être utilisées que dans le code orienté frontal. Le moyen le plus simple de s'en assurer est d'envelopper les appels dans le hook React `useEffect()`, ou à l'intérieur de `componentDidMount()` dans les composants React avec état.

Ceux que vous utiliserez probablement le plus sont `push()` et `prefetch()`.

`push()` nous permet de déclencher un changement d'URL de manière programmatique, dans le frontal :

```js
router.push('/login')

```

`prefetch()` nous permet de précharger une URL de manière programmatique, utile lorsque nous n'avons pas de balise `Link` qui gère automatiquement le préchargement pour nous :

```js
router.prefetch('/login')

```

Exemple complet :

```js
import { useRouter } from 'next/router'

export default () => {
  const router = useRouter()

  useEffect(() => {
    router.prefetch('/login')
  })
}

```

Vous pouvez également utiliser le routeur pour écouter les [événements de changement de route](https://nextjs.org/docs#router-events).

## Alimenter les composants avec des données en utilisant getInitialProps

Dans le chapitre précédent, nous avions un problème avec la génération dynamique de la page de l'article, car le composant nécessitait certaines données au préalable, et lorsque nous avons essayé d'obtenir les données depuis le fichier JSON :

```js
import { useRouter } from 'next/router'
import posts from '../../posts.json'

export default () => {
  const router = useRouter()

  const post = posts[router.query.id]

  return (
    <>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </>
  )
}

```

nous avons obtenu cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-05-at-18.18.17-1.png)

Comment résoudre ce problème ? Et comment faire fonctionner le SSR pour les routes dynamiques ?

Nous devons fournir au composant des props, en utilisant une fonction spéciale appelée `getInitialProps()` qui est attachée au composant.

Pour ce faire, nous nommons d'abord le composant :

```js
const Post = () => {
  //...
}

export default Post

```

puis nous ajoutons la fonction à celui-ci :

```js
const Post = () => {
  //...
}

Post.getInitialProps = () => {
  //...
}

export default Post

```

Cette fonction reçoit un objet comme argument, qui contient plusieurs propriétés. En particulier, ce qui nous intéresse maintenant, c'est que nous obtenons l'objet `query`, celui que nous avons utilisé précédemment pour obtenir l'identifiant de l'article.

Nous pouvons donc l'obtenir en utilisant la syntaxe de _déstruction d'objet_ :

```js
Post.getInitialProps = ({ query }) => {
  //...
}

```

Maintenant, nous pouvons retourner l'article depuis cette fonction :

```js
Post.getInitialProps = ({ query }) => {
  return {
    post: posts[query.id]
  }
}

```

Et nous pouvons également supprimer l'import de `useRouter`, et nous obtenons l'article depuis la propriété `props` passée au composant `Post` :

```js
import posts from '../../posts.json'

const Post = props => {
  return (
    <div>
      <h1>{props.post.title}</h1>
      <p>{props.post.content}</p>
    </div>
  )
}

Post.getInitialProps = ({ query }) => {
  return {
    post: posts[query.id]
  }
}

export default Post

```

Maintenant, il n'y aura pas d'erreur, et le SSR fonctionnera comme prévu, comme vous pouvez le voir en vérifiant le code source :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-05-at-18.53.02.png)

La fonction `getInitialProps` sera exécutée côté serveur, mais aussi côté client, lorsque nous naviguons vers une nouvelle page en utilisant le composant `Link` comme nous l'avons fait.

Il est important de noter que `getInitialProps` reçoit, dans l'objet de contexte qu'il reçoit, en plus de l'objet `query`, ces autres propriétés :

* `pathname` : la section `path` de l'URL
* `asPath` - Chaîne du chemin réel (y compris la requête) affichée dans le navigateur

qui, dans le cas de l'appel à `http://localhost:3000/blog/test`, donneront respectivement :

* `/blog/[id]`
* `/blog/test`

Et dans le cas du rendu côté serveur, il recevra également :

* `req` : l'objet de requête HTTP
* `res` : l'objet de réponse HTTP
* `err` : un objet d'erreur

`req` et `res` vous seront familiers si vous avez fait du codage Node.js.

## CSS

Comment styliser les composants React dans Next.js ?

Nous avons beaucoup de liberté, car nous pouvons utiliser n'importe quelle bibliothèque que nous préférons.

Mais Next.js est livré avec [`styled-jsx`](https://github.com/zeit/styled-jsx) intégré, car c'est une bibliothèque construite par les mêmes personnes qui travaillent sur Next.js.

Et c'est une bibliothèque assez cool qui nous fournit du CSS scopé, ce qui est génial pour la maintenabilité car le CSS n'affecte que le composant auquel il est appliqué.

Je pense que c'est une excellente approche pour écrire du CSS, sans avoir besoin d'appliquer des bibliothèques ou des préprocesseurs supplémentaires qui ajoutent de la complexité.

Pour ajouter du CSS à un composant React dans Next.js, nous l'insérons à l'intérieur d'un extrait dans le JSX, qui commence par

```js
<style jsx>{`

```

et se termine par

```js
`}</style>

```

À l'intérieur de ces blocs étranges, nous écrivons du CSS simple, comme nous le ferions dans un fichier `.css` :

```js
<style jsx>{`
  h1 {
    font-size: 3rem;
  }
`}</style>

```

Vous l'écrivez à l'intérieur du JSX, comme ceci :

```js
const Index = () => (
  <div>
		<h1>Page d'accueil</h1>

		<style jsx>{`
		  h1 {
		    font-size: 3rem;
		  }
		`}</style>
  </div>
)

export default Index

```

À l'intérieur du bloc, nous pouvons utiliser l'interpolation pour changer dynamiquement les valeurs. Par exemple, ici nous supposons qu'une prop `size` est transmise par le composant parent, et nous l'utilisons dans le bloc `styled-jsx` :

```js
const Index = props => (
  <div>
		<h1>Page d'accueil</h1>

		<style jsx>{`
		  h1 {
		    font-size: ${props.size}rem;
		  }
		`}</style>
  </div>
)

```

Si vous souhaitez appliquer du CSS globalement, non limité à un composant, vous ajoutez le mot-clé `global` à la balise `style` :

```jsx
<style jsx global>{`
body {
  margin: 0;
}
`}</style>

```

Si vous souhaitez importer un fichier CSS externe dans un composant Next.js, vous devez d'abord installer `@zeit/next-css` :

```bash
npm install @zeit/next-css

```

et ensuite créer un fichier de configuration à la racine du projet, appelé `next.config.js`, avec ce contenu :

```js
const withCSS = require('@zeit/next-css')
module.exports = withCSS()

```

Après avoir redémarré l'application Next, vous pouvez maintenant importer du CSS comme vous le faites normalement avec les bibliothèques ou composants JavaScript :

```js
import '../style.css'

```

Vous pouvez également importer directement un fichier SASS, en utilisant la bibliothèque [`@zeit/next-sass`](https://github.com/zeit/next-plugins/tree/master/packages/next-sass) à la place.

## Remplir la balise head avec des balises personnalisées

À partir de n'importe quel composant de page Next.js, vous pouvez ajouter des informations à l'en-tête de la page.

Cela est pratique lorsque :

* vous souhaitez personnaliser le titre de la page
* vous souhaitez modifier une balise meta

Comment pouvez-vous faire cela ?

À l'intérieur de chaque composant, vous pouvez importer le composant `Head` depuis `next/head` et l'inclure dans la sortie JSX de votre composant :

```js
import Head from 'next/head'

const House = props => (
  <div>
    <Head>
      <title>Le titre de la page</title>
    </Head>
    {/* le reste du JSX */}
  </div>
)

export default House

```

Vous pouvez ajouter n'importe quelle balise HTML que vous souhaitez voir apparaître dans la section `<head>` de la page.

Lors du montage du composant, Next.js s'assurera que les balises à l'intérieur de `Head` sont ajoutées à l'en-tête de la page. De même, lors du démontage du composant, Next.js se chargera de supprimer ces balises.

## Ajouter un composant wrapper

Toutes les pages de votre site se ressemblent plus ou moins. Il y a une fenêtre chrome, une couche de base commune, et vous voulez simplement changer ce qu'il y a à l'intérieur.

Il y a une barre de navigation, une barre latérale, et ensuite le contenu réel.

Comment construire un tel système dans Next.js ?

Il y a 2 façons. L'une consiste à utiliser un [Composant d'Ordre Supérieur](https://flaviocopes.com/react-higher-order-components/), en créant un composant `components/Layout.js` :

```js
export default Page => {
  return () => (
    <div>
      <nav>
        <ul>....</ul>
      </hav>
      <main>
        <Page />
      </main>
    </div>
  )
}

```

Dans celui-ci, nous pouvons importer des composants séparés pour l'en-tête et/ou la barre latérale, et nous pouvons également ajouter tout le CSS dont nous avons besoin.

Et vous l'utilisez dans chaque page comme ceci :

```js
import withLayout from '../components/Layout.js'

const Page = () => <p>Voici une page !</p>

export default withLayout(Page)

```

Mais j'ai trouvé que cela fonctionne uniquement pour des cas simples, où vous n'avez pas besoin d'appeler `getInitialProps()` sur une page.

Pourquoi ?

Parce que `getInitialProps()` n'est appelé que sur le composant de la page. Mais si nous exportons le Composant d'Ordre Supérieur withLayout() depuis une page, `Page.getInitialProps()` n'est pas appelé. `withLayout.getInitialProps()` le serait.

Pour éviter de compliquer inutilement notre base de code, l'approche alternative consiste à utiliser des props :

```js
export default props => (
  <div>
    <nav>
      <ul>....</ul>
    </hav>
    <main>
      {props.content}
    </main>
  </div>
)

```

et dans nos pages, nous l'utilisons maintenant comme ceci :

```js
import Layout from '../components/Layout.js'

const Page = () => (
  <Layout content={(
    <p>Voici une page !</p>
  )} />
)

```

Cette approche nous permet d'utiliser `getInitialProps()` depuis notre composant de page, avec le seul inconvénient d'avoir à écrire le JSX du composant à l'intérieur de la prop `content` :

```js
import Layout from '../components/Layout.js'

const Page = () => (
  <Layout content={(
    <p>Voici une page !</p>
  )} />
)

Page.getInitialProps = ({ query }) => {
  //...
}

```

## Routes API

En plus de créer des **routes de page**, ce qui signifie que les pages sont servies au navigateur en tant que pages Web, Next.js peut créer des **routes API**.

C'est une fonctionnalité très intéressante car cela signifie que Next.js peut être utilisé pour créer un frontend pour des données qui sont stockées et récupérées par Next.js lui-même, en transférant du JSON via des requêtes fetch.

Les routes API vivent sous le dossier `/pages/api/` et sont mappées à l'endpoint `/api`.

Cette fonctionnalité est _très_ utile lors de la création d'applications.

Dans ces routes, nous écrivons du code Node.js (plutôt que du code React). C'est un changement de paradigme, vous passez du frontend au backend, mais de manière très transparente.

Supposons que vous avez un fichier `/pages/api/comments.js`, dont le but est de retourner les commentaires d'un article de blog en JSON.

Supposons que vous avez une liste de commentaires stockée dans un fichier `comments.json` :

```json
[
  {
    "comment": "First"
  },
  {
    "comment": "Nice post"
  }
]

```

Voici un exemple de code, qui retourne au client la liste des commentaires :

```js
import comments from './comments.json'

export default (req, res) => {
  res.status(200).json(comments)
}

```

Il écoutera sur l'URL `/api/comments` pour les requêtes GET, et vous pouvez essayer de l'appeler en utilisant votre navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-07-at-11.14.42.png)

Les routes API peuvent également utiliser le **routage dynamique** comme les pages, utiliser la syntaxe `[]` pour créer une route API dynamique, comme `/pages/api/comments/[id].js` qui récupérera les commentaires spécifiques à un identifiant de publication.

À l'intérieur de `[id].js`, vous pouvez récupérer la valeur `id` en la recherchant dans l'objet `req.query` :

```js
import comments from '../comments.json'

export default (req, res) => {
  res.status(200).json({ post: req.query.id, comments })
}

```

Voici le code ci-dessus en action :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-07-at-11.59.53.png)

Dans les pages dynamiques, vous devriez importer `useRouter` depuis `next/router`, puis obtenir l'objet routeur en utilisant `const router = useRouter()`, et ensuite nous pourrions obtenir la valeur `id` en utilisant `router.query.id`.

Côté serveur, tout est plus simple, car la requête est attachée à l'objet de requête.

Si vous faites une requête POST, tout fonctionne de la même manière - tout passe par cette exportation par défaut.

Pour séparer POST de GET et d'autres méthodes HTTP (PUT, DELETE), recherchez la valeur `req.method` :

```js
export default (req, res) => {
  switch (req.method) {
    case 'GET':
      //...
      break
    case 'POST':
      //...
      break
    default:
      res.status(405).end() //Méthode Non Autorisée
      break
  }
}

```

En plus de `req.query` et `req.method` que nous avons déjà vus, nous avons accès aux cookies en référençant `req.cookies`, au corps de la requête dans `req.body`.

Sous le capot, tout cela est alimenté par [Micro](https://github.com/zeit/micro), une bibliothèque qui alimente les microservices HTTP asynchrones, créée par la même équipe qui a construit Next.js.

Vous pouvez utiliser n'importe quel middleware Micro dans nos routes API pour ajouter plus de fonctionnalités.

## Exécuter du code uniquement côté serveur ou côté client

Dans vos composants de page, vous pouvez exécuter du code uniquement côté serveur ou côté client, en vérifiant la propriété `window`.

Cette propriété n'existe que dans le navigateur, vous pouvez donc vérifier

```js
if (typeof window === 'undefined') {

}

```

et ajouter le code côté serveur dans ce bloc.

De même, vous pouvez exécuter du code côté client uniquement en vérifiant

```js
if (typeof window !== 'undefined') {

}

```

Astuce JS : Nous utilisons l'opérateur `typeof` ici car nous ne pouvons pas détecter qu'une valeur est indéfinie de manière différente. Nous ne pouvons pas faire `if (window === undefined)` car nous obtiendrions une erreur d'exécution "window is not defined"

Next.js, en tant qu'optimisation au moment de la construction, supprime également le code qui utilise ces vérifications des bundles. Un bundle côté client n'inclura pas le contenu enveloppé dans un bloc `if (typeof window === 'undefined') {}`.

## Déployer la version de production

Le déploiement d'une application est toujours laissé pour la fin dans les tutoriels.

Ici, je veux l'introduire tôt, juste parce qu'il est si facile de déployer une application Next.js que nous pouvons nous y plonger maintenant, puis passer à d'autres sujets plus complexes plus tard.

Rappelez-vous dans le chapitre "Comment installer Next.js" je vous ai dit d'ajouter ces 3 lignes à la section `script` du `package.json` :

```json
"scripts": {
  "dev": "next",
  "build": "next build",
  "start": "next start"
}

```

Nous avons utilisé `npm run dev` jusqu'à présent, pour appeler la commande `next` installée localement dans `node_modules/next/dist/bin/next`. Cela a démarré le serveur de développement, qui nous a fourni des **source maps** et du **rechargement à chaud du code**, deux fonctionnalités très utiles pour le débogage.

La même commande peut être invoquée pour construire le site web en passant le flag `build`, en exécutant `npm run build`. Ensuite, la même commande peut être utilisée pour démarrer l'application de production en passant le flag `start`, en exécutant `npm run start`.

Ces 2 commandes sont celles que nous devons invoquer pour déployer avec succès la version de production de notre site localement. La version de production est hautement optimisée et ne contient pas de source maps et d'autres choses comme le rechargement à chaud du code qui ne seraient pas bénéfiques pour nos utilisateurs finaux.

Alors, créons un déploiement de production de notre application. Construisez-le en utilisant :

```bash
npm run build

```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-13.46.31.png)

La sortie de la commande nous indique que certaines routes (`/` et `/blog` sont maintenant pré-rendues en HTML statique, tandis que `/blog/[id]` sera servi par le backend Node.js.

Ensuite, vous pouvez exécuter `npm run start` pour démarrer le serveur de production localement :

```bash
npm run start

```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-13.47.01.png)

Visiter [http://localhost:3000](http://localhost:3000) nous montrera la version de production de l'application, localement.

## Déployer sur Now

Dans le chapitre précédent, nous avons déployé l'application Next.js localement.

Comment la déployer sur un vrai serveur web, afin que d'autres personnes puissent y accéder ?

L'une des manières les plus simples de déployer une application Next est via la plateforme **Now** créée par [Zeit](https://zeit.co), la même entreprise qui a créé le projet Open Source Next.js. Vous pouvez utiliser Now pour déployer des applications Node.js, des sites web statiques, et bien plus encore.

Now rend l'étape de déploiement et de distribution d'une application très, très simple et rapide, et en plus des applications Node.js, ils prennent également en charge le déploiement de Go, PHP, Python et d'autres langages.

Vous pouvez le considérer comme le "cloud", car vous ne savez pas vraiment où votre application sera déployée, mais vous savez que vous aurez une URL où vous pourrez l'atteindre.

Now est gratuit pour commencer, avec un plan gratuit généreux qui inclut actuellement 100 Go d'hébergement, 1000 invocations de fonctions [serverless](https://www.freecodecamp.org/news/serverless/) par jour, 1000 builds par mois, 100 Go de bande passante par mois, et un emplacement [CDN](https://www.freecodecamp.org/news/cdn/). La [page de tarification](https://zeit.co/pricing) aide à se faire une idée des coûts si vous avez besoin de plus.

La meilleure façon de commencer à utiliser Now est d'utiliser l'interface de ligne de commande officielle Now :

```bash
npm install -g now

```

Une fois la commande disponible, exécutez

```bash
now login

```

et l'application vous demandera votre email.

Si vous n'êtes pas encore inscrit, créez un compte sur [https://zeit.co/signup](https://zeit.co/signup) avant de continuer, puis ajoutez votre email au client CLI.

Une fois cela fait, depuis le dossier racine du projet Next.js, exécutez

```bash
now

```

et l'application sera instantanément déployée sur le cloud Now, et vous recevrez l'URL unique de l'application :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-14.21.09.png)

Une fois que vous exécutez le programme `now`, l'application est déployée sur une URL aléatoire sous le domaine `now.sh`.

Nous pouvons voir 3 URL différentes dans la sortie donnée dans l'image :

* [https://firstproject-2pv7khwwr.now.sh](https://firstproject-2pv7khwwr.now.sh)
* [https://firstproject-sepia-ten.now.sh](https://firstproject-sepia-ten.now.sh)
* [https://firstproject.flaviocopes.now.sh](https://firstproject.flaviocopes.now.sh)

Pourquoi autant ?

La première est l'URL identifiant le déploiement. Chaque fois que nous déployons l'application, cette URL changera.

Vous pouvez tester immédiatement en modifiant quelque chose dans le code du projet, et en exécutant `now` à nouveau :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-15.08.11.png)

Les 2 autres URL ne changeront pas. La première est une URL aléatoire, la seconde est le nom de votre projet (qui par défaut est le dossier de projet actuel, votre nom de compte et ensuite `now.sh`.

Si vous visitez l'URL, vous verrez l'application déployée en production.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-14.21.43.png)

Vous pouvez configurer Now pour servir le site sur votre propre domaine ou sous-domaine personnalisé, mais je ne vais pas approfondir cela pour l'instant.

Le sous-domaine `now.sh` est suffisant pour nos besoins de test.

## Analyser les bundles de l'application

Next nous fournit un moyen d'analyser les bundles de code qui sont générés.

Ouvrez le fichier package.json de l'application et dans la section scripts ajoutez ces 3 nouvelles commandes :

```json
"analyze": "cross-env ANALYZE=true next build",
"analyze:server": "cross-env BUNDLE_ANALYZE=server next build",
"analyze:browser": "cross-env BUNDLE_ANALYZE=browser next build"

```

Comme ceci :

```json
{
  "name": "firstproject",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "next",
    "build": "next build",
    "start": "next start",
    "analyze": "cross-env ANALYZE=true next build",
    "analyze:server": "cross-env BUNDLE_ANALYZE=server next build",
    "analyze:browser": "cross-env BUNDLE_ANALYZE=browser next build"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "next": "^9.1.2",
    "react": "^16.11.0",
    "react-dom": "^16.11.0"
  }
}

```

puis installez ces 2 packages :

```bash
npm install --dev cross-env @next/bundle-analyzer

```

Créez un fichier `next.config.js` à la racine du projet, avec ce contenu :

```js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true'
})

module.exports = withBundleAnalyzer({})

```

Maintenant exécutez la commande

```bash
npm run analyze

```

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-16.12.40.png)

Cela devrait ouvrir 2 pages dans le navigateur. Une pour les bundles client, et une pour les bundles serveur :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-16.11.14.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-16.11.23.png)

C'est incroyablement utile. Vous pouvez inspecter ce qui prend le plus de place dans les bundles, et vous pouvez également utiliser la barre latérale pour exclure des bundles, pour une visualisation plus facile des plus petits :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-16.14.12.png)

## Chargement paresseux des modules

Pouvoir analyser visuellement un bundle est génial car nous pouvons optimiser notre application très facilement.

Supposons que nous devons charger la bibliothèque Moment dans nos articles de blog. Exécutez :

```bash
npm install moment

```

pour l'inclure dans le projet.

Maintenant, simulons le fait que nous en avons besoin sur deux routes différentes : `/blog` et `/blog/[id]`.

Nous l'importons dans `pages/blog/[id].js` :

```jsx
import moment from 'moment'

...

const Post = props => {
  return (
    <div>
      <h1>{props.post.title}</h1>
      <p>Publié le {moment().format('dddd D MMMM YYYY')}</p>
      <p>{props.post.content}</p>
    </div>
  )
}

```

Je n'ajoute que la date d'aujourd'hui, à titre d'exemple.

Cela inclura Moment.js dans le bundle de la page du blog, comme vous pouvez le voir en exécutant `npm run analyze` :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-17.56.14.png)

Voyez que nous avons maintenant une entrée rouge dans `/blog/[id]`, la route à laquelle nous avons ajouté Moment.js !

Il est passé de ~1kB à 350kB, ce qui est assez important. Et c'est parce que la bibliothèque Moment.js elle-même fait 349kB.

La visualisation des bundles client montre maintenant que le plus gros bundle est celui de la page, qui était auparavant très petit. Et 99% de son code est Moment.js.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-17.55.50.png)

Chaque fois que nous chargeons un article de blog, tout ce code sera transféré au client. Ce qui n'est pas idéal.

Une solution serait de chercher une bibliothèque de plus petite taille, car Moment.js n'est pas connu pour être léger (surtout hors de la boîte avec toutes les locales incluses), mais supposons pour les besoins de l'exemple que nous devons l'utiliser.

Ce que nous pouvons faire à la place, c'est séparer tout le code Moment dans un **bundle séparé**.

Comment ? Au lieu d'importer Moment au niveau du composant, nous effectuons une importation asynchrone à l'intérieur de `getInitialProps`, et nous calculons la valeur à envoyer au composant. 
Rappelez-vous que nous ne pouvons pas retourner d'objets complexes à l'intérieur de l'objet retourné par `getInitialProps()`, donc nous calculons la date à l'intérieur :

```js
import posts from '../../posts.json'

const Post = props => {
  return (
    <div>
      <h1>{props.post.title}</h1>
      <p>Publié le {props.date}</p>
      <p>{props.post.content}</p>
    </div>
  )
}

Post.getInitialProps = async ({ query }) => {
  const moment = (await import('moment')).default()
  return {
    date: moment.format('dddd D MMMM YYYY'),
    post: posts[query.id]
  }
}

export default Post

```

Voyez cet appel spécial à `.default()` après `await import` ? Il est nécessaire pour référencer l'exportation par défaut dans une importation dynamique (voir [https://v8.dev/features/dynamic-import](https://v8.dev/features/dynamic-import))

Maintenant, si nous exécutons `npm run analyze` à nouveau, nous pouvons voir ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screen-Shot-2019-11-06-at-18.00.22.png)

Notre bundle `/blog/[id]` est à nouveau très petit, car Moment a été déplacé dans son propre fichier de bundle, chargé séparément par le navigateur.

## Où aller à partir d'ici

Il y a beaucoup plus à savoir sur Next.js. Je n'ai pas parlé de la gestion des sessions utilisateur avec la connexion, du serverless, de la gestion des bases de données, et ainsi de suite.

Le but de ce manuel n'est pas de vous enseigner tout, mais plutôt de vous introduire, progressivement, à toute la puissance de Next.js.

La prochaine étape que je recommande est de lire attentivement la [documentation officielle de Next.js](https://nextjs.org/docs) pour découvrir toutes les fonctionnalités et fonctionnalités dont je n'ai pas parlé, et de jeter un coup d'œil à toutes les fonctionnalités supplémentaires introduites par les [plugins Next.js](https://github.com/zeit/next-plugins), dont certains sont assez incroyables.

Vous pouvez me rejoindre sur Twitter [@flaviocopes](https://twitter.com/flaviocopes).

Consultez également mon site web, [flaviocopes.com](https://flaviocopes.com/).

[Note : vous pouvez télécharger une version PDF / ePub / Mobi de ce tutoriel pour le lire hors ligne](https://flaviocopes.com/page/nextjs-handbook/)