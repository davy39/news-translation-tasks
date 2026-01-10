---
title: Comment créer un site de documentation moderne avec VitePress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-16T17:01:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-modern-documentation-site-with-vitepress
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/How-to-build-a-modern-documentation-site-with-vitepress-by-Victor-Eke.png
tags:
- name: documentation
  slug: documentation
- name: JavaScript
  slug: javascript
- name: Software Engineering
  slug: software-engineering
- name: vite
  slug: vite
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: Comment créer un site de documentation moderne avec VitePress
seo_desc: "By Victor Eke\nDocumentation is a crucial aspect of software development.\
  \ But developers often neglect it because it can be a hassle to maintain. This is\
  \ why it's important to use tools that help simplify this process. \nIn this tutorial,\
  \ you'll learn ..."
---

Par Victor Eke

La documentation est un aspect crucial du développement logiciel. Mais les développeurs la négligent souvent car elle peut être fastidieuse à maintenir. C'est pourquoi il est important d'utiliser des outils qui aident à simplifier ce processus. 

Dans ce tutoriel, vous apprendrez à créer rapidement un site de documentation complet en utilisant un outil moderne appelé VitePress.

## Qu'est-ce que VitePress ?

[VitePress](https://vitepress.vuejs.org/) est un générateur de site statique simple et performant construit sur [Vite](https://vitejs.dev) qui vous permet de créer des documentations en quelques minutes. Il est alimenté par [Vuejs](https://vuejs.org/) et Vite avec des composants personnalisables intégrés. 

VitePress alimente certains sites de documentation populaires comme Vuejs, [Vitest](https://vitest.dev/), [faker.js](https://faker.js/dev), et Vite lui-même.

## Prérequis

Pour suivre ce tutoriel, vous devez avoir une compréhension de base des éléments suivants :

* La syntaxe [Markdown](https://daringfireball.net/projects/markdown/)
* Une compréhension de base de NPM et Vite

Voici une capture d'écran de ce que vous allez construire à la fin de ce tutoriel :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/final-works-2.png)

Vous voulez l'essayer ? Consultez la [démo en direct](http://adocs.vercel.app/). De plus, le code source de ce projet peut être trouvé sur [GitHub](https://github.com/Evavic44/adocs).

## Étape 1 : Créer un nouveau projet

Si vous avez déjà un dossier créé, vous pouvez passer cette étape et continuer à la suivante. Sinon, utilisez la commande suivante pour créer un dossier de projet et vous y déplacer.

```bash
mkdir nom-du-projet
cd nom-du-projet

```

Ensuite, vous devez initialiser le projet avec votre gestionnaire de paquets préféré. J'utiliserai NPM pour le reste de ce guide.

```js
npm init
// ou utilisez cette commande si vous voulez ignorer toutes les questions
npm init -y

```

Si vous avez utilisé la première commande, vous serez invité à répondre à certaines questions, alors complétez-les comme il se doit. 

Après une opération réussie, vous devriez avoir un fichier `package.json` dans votre répertoire racine. C'est ici que la dépendance de développement VitePress sera installée.

## Étape 2 : Installer VitePress

L'étape suivante consiste à ajouter VitePress et Vue comme dépendances de développement à votre projet, comme ceci :

```bash
npm install --dev vitepress vue
```

Vous avez installé avec succès VitePress et Vue et les avez ajoutés comme dépendances de développement. Maintenant, vous pouvez commencer à créer vos fichiers de documentation respectifs. 

Mais avant de le faire, je pense qu'il est essentiel d'expliquer comment fonctionne VitePress.

## Comment fonctionne VitePress ?

VitePress utilise des fichiers Markdown `.md` pour son balisage, qui sont automatiquement convertis en HTML statique. Pour que cela fonctionne, un dossier spécial appelé `docs` est créé dans le répertoire racine.

Ce dossier se comporte de manière similaire au dossier `pages` dans NextJS, où tout fichier `.js` créé dans le répertoire est automatiquement traité comme une page web. Dans ce cas, un fichier appelé `index.md` sera traité comme `index.html` et servira de racine pour votre modèle de documentation.

Maintenant que vous comprenez comment cela fonctionne, vous pouvez créer vos fichiers de documentation respectifs.

## Étape 3 : Créer les fichiers de documentation respectifs

Vous pouvez créer le dossier docs et le fichier `index.md` manuellement, ou vous pouvez le faire avec le terminal comme un hacker.

```bash
mkdir docs && echo '# Bonjour VitePress' > docs/index.md
```

Cette commande crée simplement un dossier appelé `docs` et ajoute un fichier `index.md` contenant un élément `h1` qui dit "Bonjour le monde". 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/create-respective-files.png)

Avec cela, vous pouvez démarrer votre environnement de développement pour voir ce qui a été créé jusqu'à présent.

## Étape 4 : Démarrer votre environnement de développement

Pour exécuter vos docs localement, vous devez ajouter les scripts suivants à l'intérieur du fichier `package.json`. Copiez simplement le code ci-dessous et remplacez l'objet `"script"` par celui-ci :

```js
// package.json
"scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:serve": "vitepress serve docs"
  },
```

Enfin, le site de documentation peut être servi sur un serveur local en exécutant la commande suivante :

```bash
npm run docs:dev

```

Cela démarrera un serveur de développement avec rechargement à chaud à l'adresse `http://localhost:5173`, et vous pourrez le visiter pour voir votre site de documentation.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/boot-dev-server.png)

Tout ce que vous avez eu à faire était d'ajouter le balisage et VitePress a géré l'apparence à partir de son moteur de modèle. Dans la prochaine session, vous apprendrez comment vous pouvez personnaliser les docs pour les adapter à vos besoins.

## Comment personnaliser vos docs avec VitePress

Tout d'abord, créez un dossier `.vitepress` à l'intérieur du répertoire docs que vous avez créé précédemment. C'est ici que tous les fichiers spécifiques à VitePress seront placés. 

À l'intérieur de ce nouveau répertoire, vous avez besoin d'un fichier `config.js`. Encore une fois, vous pouvez utiliser la commande de terminal comme suit :

```bash
mkdir .vitepress && touch .vitepress/config.js
```

Pour tester ce fichier de configuration, vous pouvez commencer par changer le titre méta et la description de votre site de documentation. Copiez ce balisage et collez-le dans le fichier `config.js` :

```js
// .vitepress/config.js
export default {
  title: 'Adocs',
  description: 'Un modèle de docs génial construit par moi'
}
```

Si vous vérifiez les outils de développement, vous devriez voir les changements dans le titre méta et la description.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/title-and-description.png)

### Comment mettre à jour le titre et le logo

Pour changer le titre du logo et ajouter une image, copiez le balisage ci-dessous et collez-le dans un nouvel objet appelé `themeConfig` à l'intérieur du même fichier `config.js`. Cela écrasera le titre actuel et ajoutera un logo à votre site de documentation.

```js
// config.js
export default {
  themeConfig: {
    logo: "/logo.svg",
    siteTitle: "Adocs",
  },
};

```

Pour la source de l'image, vous pouvez passer une URL d'image ou spécifier le chemin d'une image locale. Pour le faire localement, assurez-vous de placer l'image dans le répertoire `public`.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/logo-and-title.png)

Notez que les fichiers dans le répertoire public sont servis à la racine. Donc au lieu de ../public/logo.svg, utilisez simplement /logo.svg.

### Comment personnaliser la barre de navigation

Personnaliser la `Navbar` est également un processus assez simple. À l'intérieur de votre fichier `themeConfig`, collez le balisage ci-dessous. Ici, nous avons un objet qui contient deux propriétés : le texte d'ancrage `text`, et le chemin `link` définit l'URL.

```js
// .vitepress/config.js
{  
  // ...
   nav: [
    { text: "À propos", link: "/about" },
    { text: "Contact", link: "/contact" },
    { text: "Guide", link: "/guide" },
    { text: "Configs", link: "/configs" },
    { text: "Journal des modifications", link: "https://github.com/..." },
  ],
  // ...     
}
```

Essentiellement, naviguer vers [localhost:5173/about](http://localhost:5173/about) devrait vous emmener à une page à propos (bien que nous ne l'ayons pas encore créée).

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/navigaiton-menu.png)

Les liens de navigation peuvent également être des menus déroulants. Pour en ajouter un, remplacez simplement une des propriétés `links` par l'objet items qui contient un tableau de liens.

```js
// .vitepress/config.js
{
  text: "Journal des modifications",
  items: [
   { text: "v0.0.1", link: "/item-1" },
   { text: "v0.0.2", link: "/item-2" },
   { text: "v0.0.3", link: "/item-3" },
  ],
},

```

Maintenant, le journal des modifications deviendra un menu déroulant avec les liens respectifs que vous passez à l'intérieur.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/dropdown-menu.png)

### Comment ajouter des icônes sociales

Les menus de navigation ont généralement des icônes sociales que les visiteurs peuvent utiliser pour visiter vos plateformes sociales. Pour les ajouter, définissez un nouvel objet appelé `socialLinks` à l'intérieur de `themeConfig` et passez simplement l'icône sociale et le lien vers lequel vous voulez qu'elle navigue.

```js
// .vitepress/config.js
socialLinks: [
  { icon: "github", link: "https://github.com/Evavic44/adocs" },
  { icon: "twitter", link: "https://twitter.com/victorekea" },
  { icon: "discord", link: "..." },
]

```

Par défaut, seulement 8 icônes (Discord, Facebook, GitHub, Instagram, LinkedIn, Slack, Twitter, et YouTube) sont fournies. Si vous voulez ajouter une icône personnalisée, utilisez la propriété SVG pour définir une image svg. Vous pouvez obtenir des icônes gratuites sur [icones.js.org](https://icones.js.org/).

Par exemple, voici un extrait de l'icône `apple`. 

```js
{
  icon: {
    svg: '<svg role="img" width="26.01" height="32" viewBox="0 0 256 315"><path d="M213.803 167.03c.442 47.58 41.74 63.413 42.197 63.615c-.35 1.116-6.599 22.563-21.757 44.716c-13.104 19.153-26.705 38.235-48.13 38.63c-21.05.388-27.82-12.483-51.888-12.483c-24.061 0-31.582 12.088-51.51 12.871c-20.68.783-36.428-20.71-49.64-39.793c-27-39.033-47.633-110.3-19.928-158.406c13.763-23.89 38.36-39.017 65.056-39.405c20.307-.387 39.475 13.662 51.889 13.662c12.406 0 35.699-16.895 60.186-14.414c10.25.427 39.026 4.14 57.503 31.186c-1.49.923-34.335 20.044-33.978 59.822M174.24 50.199c10.98-13.29 18.369-31.79 16.353-50.199c-15.826.636-34.962 10.546-46.314 23.828c-10.173 11.763-19.082 30.589-16.678 48.633c17.64 1.365 35.66-8.964 46.64-22.262"/></svg>',
    },
  link: "https://www.apple.com/",
},
```

Pour les icônes SVG personnalisées, assurez-vous d'ajouter la propriété `role="img"` à la balise `svg`, car cela permet à la chaîne de la convertir correctement.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/social-icons.png)

### Comment ajouter une barre latérale

VitePress est également livré avec des composants intégrés comme les menus de la barre latérale. Pour ajouter une barre latérale, créez un objet appelé `sidebar` et à l'intérieur, ajoutez des objets imbriqués qui prennent trois valeurs : le titre imbriqué, la fonctionnalité pliable (par défaut définie sur true), et les liens imbriqués.

```js
// .vitepress/config.js
sidebar: [
    {
      text: "Section A",
      collapsible: true,
      items: [
        { text: "Introduction", link: "/introduction" },
        { text: "Premiers pas", link: "/getting-started" },
      ],
    },
    {
      text: "Section B",
      collapsible: false,
      items: [
        { text: "Introduction", link: "/introduction" },
        { text: "Premiers pas", link: "/getting-started" },
      ],
    },
    {
      text: "Section C",
      collapsible: true,
      items: [
        { text: "Introduction", link: "/introduction" },
        { text: "Premiers pas", link: "/getting-started" },
      ],
    },
  ],

```

En ajoutant `collapsible: "true"` à l'objet de la barre latérale, cela montre un bouton bascule pour masquer/afficher chaque section. Vous pouvez créer autant de sections que vous le souhaitez.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sidebar-2.png)

Vous pouvez voir que la section B n'est pas pliable, et nous avons ce joli bouton de page suivante en bas de la page.

### Comment configurer le routage des pages

Comme expliqué précédemment, VitePress convertit automatiquement chaque fichier `.md` à l'intérieur de la racine du répertoire docs en HTML statique accessible dans la barre d'adresse. Par exemple, `index.md` est converti en `index.html`, et `about.md` en `about.html`, et ainsi de suite. 

Puisque vous avez créé vos liens de navigation et que vous les avez pointés vers leurs URL respectives, vous pouvez accéder à ces pages facilement en les créant.

```
docs/
├── .vitepress/
│   └── config.js
├── public/
│   └── logo.svg
├── about.md
├── contact.md
├── guide.md
├── configs.md
└── get-started.md
```

Créez ces fichiers à l'intérieur de votre dossier docs et ajoutez un simple balisage à l'intérieur pour voir comment cela fonctionne. Cette page est en markdown de base, donc toutes vos syntaxes markdown comme les liens, les blocs de code, les titres, etc., fonctionnent ici.

Juste à des fins de test, copiez ce contenu markdown et collez-le à l'intérieur de l'un des fichiers `.md` que vous venez de créer :

```md
# À propos

Bienvenue sur la page à propos.

Ce markdown supporte les éléments html comme la balise `p` couplée avec des styles en ligne

<p style="color: #ff7340; border: 1px solid rgba(255, 135, 23, 0.25); border-radius:5px; padding: 1rem;">Lorem Ipsum est simplement un texte factice de l'industrie de l'impression et de la composition. Lorem Ipsum est le texte factice standard de l'industrie depuis les années 1500.</p>

Même les extraits de code satiriques avec surlignage de syntaxe sont également supportés. 😅

```js
const lang = prompt("Quel est votre langage de programmation préféré ?");

(lang === "JavaScript") | (lang === "javascript") | (lang === "js")
  ? alert("JavaScript pour le monde ! 🚀🏡")
  : alert(`Nous ne permettons pas de tels langages ici 💩`);
```

Bien sûr, les images ne sont pas laissées de côté.

<img src="/logo.svg" alt="logo adocs">
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/page-routing-2.gif)

Super ! Vous avez configuré les docs, ajouté un menu de navigation avec une fonctionnalité de menu déroulant, ajouté une barre latérale, et personnalisé les liens pour naviguer vers différentes pages. Ensuite, travaillons sur la page d'accueil.

## Comment personnaliser la page d'accueil

Tout comme chaque autre composant, VitePress nous fournit un balisage pour construire la page d'accueil. Je l'ai divisé en trois parties : Hero, fonctionnalités, et section de pied de page.

### La section Hero

Tout d'abord, nous allons commencer par la section hero. Remplacez le texte Hello World dans la page `index.md` par le balisage suivant :

```yml
# docs/index.md
---
layout: home

hero:
  name: Adocs
  text: Modèle de docs statique construit avec VitePress.
  image:
    src: /logo-big.svg
    alt: Logo Adocs
  tagline: Un modèle gratuit à utiliser pour créer des docs pour vos projets
  actions:
    - theme: brand
      text: Commencer
      link: /get-started
    - theme: alt
      text: Voir sur GitHub
      link: https://github.com/evavic44/adocs-template
---

```

### La section des fonctionnalités

De plus, vous pouvez ajouter une section des fonctionnalités après la section hero. Il suffit de coller le code ci-dessous sous les objets hero :

```yml
# /docs/index.md
---
link: https://github.com/evavic44/adocs-template

features:
  - icon: ⚡
    title: Adocs, l'expérience développeur qui ne peut pas être battue
    details: Lorem ipsum...
  - icon: 🎉
    title: La puissance de Vue rencontre Markdown
    details: Lorem ipsum...
  - icon: 🔥
    title: Simple et minimal, toujours
    details: Lorem ipsum...
  - icon: 🎀
    title: Stylé et cool
    details: Lorem ipsum...
---

```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/hero-redesign.png)

### La section du pied de page

Vous pouvez ajouter un message de pied de page en bas de la page, mais cela n'apparaîtra que dans la page d'accueil.

Selon la documentation [_VitePress_](https://vitepress.vuejs.org/guide/theme-footer#footer) :

> Notez que le pied de page ne sera pas affiché lorsque la barre latérale est visible.

Pour ajouter le composant de pied de page, allez dans le fichier `config.js` et collez le balisage à l'intérieur de l'objet `themeConfig` :

```js
// .vitepress/config.js
 footer: {
   message: "Publié sous la licence MIT.",
   copyright: "Copyright © 2022-présent Adocs",
 },
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/footer-2.png)

En plus du balisage, vous pouvez également personnaliser les composants en utilisant du CSS personnalisé pour changer des choses comme la famille de polices, les couleurs, la mise en page, etc.

## Comment ajouter du CSS personnalisé

Le thème CSS par défaut est personnalisé en remplaçant les variables CSS de niveau racine. Si vous le souhaitez, vous pouvez consulter [la liste complète des variables CSS personnalisables](https://github.com/vuejs/vitepress/blob/main/src/client/theme-default/styles/vars.css). 

Pour commencer, créez un répertoire `.vitepress/theme`, et à l'intérieur de ce dossier de thème, ajoutez un fichier `index.js` et `custom.css`. Si vous avez suivi jusqu'à présent, vous pouvez utiliser la commande de terminal ci-dessous pour faire cela rapidement :

```bash
mkdir docs/.vitepress/theme && touch docs/.vitepress/theme/index.js && touch docs/.vitepress/theme/custom.css
```

Si vous rencontrez des problèmes avec la commande de terminal, créez simplement les fichiers manuellement et passez à l'étape suivante.

Voici un aperçu de la structure du dossier :

```bash
docs/
├── .vitepress/
│   ├── config.js
│   └── theme/
│       ├── index.js
│       └── custom.css
├── public/
│   └── logo.svg
├── about.md
├── contact.md
├── guide.md
├── configs.md
└── get-started.md
```

Après avoir créé ces fichiers, à l'intérieur du fichier `.vitepress/theme/index.js`, collez les commandes d'importation :

```js
// .vitepress/theme/index.js
import DefaultTheme from "vitepress/theme";
import "./custom.css";

export default DefaultTheme;

```

### Thème de couleur

Les couleurs sont contrôlées par les variables CSS. Vous pouvez simplement les remplacer par les couleurs de votre choix.

Notez que cette couleur a une disposition pour le mode clair et sombre. Assurez-vous donc de les changer en conséquence.

Voici un exemple de mes couleurs personnalisées :

```css
/* .vitepress/theme/custom.css */

:root {
  --vp-c-brand: rgb(255, 115, 64);
  --vp-c-brand-light: rgb(255, 87, 25);
  --vp-c-brand-lighter: rgb(255, 115, 64);
  --vp-c-brand-dark: #FF622D;
  --vp-c-brand-darker: rgb(226, 60, 0);

  --vp-c-sponsor: #fd1d7c;
}

```

Si vous ne voyez pas les effets immédiatement, essayez d'arrêter le serveur et de le redémarrer.

En plus des thèmes de couleur, vous pouvez également remplacer d'autres choses comme la famille de polices, la typographie, la mise en page, les points de rupture, etc.

### Comment utiliser des polices personnalisées

Vous pouvez importer des [polices Google](https://fonts.google.com/) à l'intérieur du fichier CSS pour remplacer la famille de polices par défaut.

```css
@import url(https://fonts.googleapis.com/css?family=Space+Mono:regular,italic,700,700italic);
@import url(https://fonts.googleapis.com/css?family=Space+Grotesk:regular,italic,700,700italic);

:root {
  --vp-c-brand: #ff7340;
  --vp-c-brand-light: #ff5719;
  --vp-c-brand-lighter: #ff7340;
  --vp-c-brand-lighter: rgba(255, 135, 23, 0.25);
  --vp-c-brand-dark: #ff622d;
  --vp-c-brand-darker: #e23c00;

  --vp-c-sponsor: #fd1d7c;

  /* Typographie */
  --vp-font-family-base: "Space Grotesk", "Inter var experimental", "Inter var",
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu,
    Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;

  /* Police des extraits de code */
  --vp-font-family-mono: "Space Mono", Menlo, Monaco, Consolas, "Courier New",
    monospace;
}

```

Avec la variable `--vp-font-family-base`, vous pouvez changer la police principale et `--vp-font-family-mono`, la police pour les extraits de code.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/final-works.png)

Vous avez personnalisé avec succès le thème et changé la famille de polices en utilisant CSS. Bien qu'il y ait plus à faire en matière de style, à ce stade, j'espère qu'il est clair comment vous pouvez personnaliser vos docs avec CSS. 

Discutons de l'hébergement dans la section suivante.

## Comment héberger votre site de documentation

Vous pouvez publier ou héberger votre site de documentation sur différentes plateformes comme [Netlify](https://netlify.com), [Vercel](https://vercel.com), [AWS Amplify](https://aws.com), et ainsi de suite.

Tout d'abord, exécutez la commande de construction :

```bash
npm run docs:build

```

Cela devrait créer un nouveau dossier `dist` qui contient tous les fichiers statiques de vos docs. 

En décidant du service d'hébergement à utiliser, vous pouvez choisir l'une des options que j'ai mentionnées précédemment, mais nous utiliserons Vercel dans ce guide. De plus, n'hésitez pas à regarder d'autres alternatives de votre choix. 

Si vous n'avez pas de compte Vercel, suivez ce guide pour [en créer un et configurer votre fournisseur Git](https://vercel.com/docs/concepts/get-started/deploy) avant de passer à l'étape suivante.

En supposant que vous avez configuré avec succès votre compte et téléchargé votre site de documentation sur Vercel, accédez à **project > settings > build and deploy settings**, et collez les commandes suivantes dans leurs champs respectifs :

* Commande de construction : `npm run docs:build` 
* Répertoire de sortie : `docs/.vitepress/dist`

![Image](https://www.freecodecamp.org/news/content/images/2022/11/deploy-settings-vercel.png)

Après avoir modifié les paramètres, enregistrez-les et déployez votre site !

## Conclusion

Dans ce tutoriel, vous avez configuré un site de documentation complet et l'avez personnalisé en utilisant CSS et les composants intégrés de VitePress. 

Gardez simplement à l'esprit que ce tutoriel ne couvre qu'une partie de ce qui est possible avec VitePress. Pour en savoir plus, consultez la [documentation de VitePress](https://vitepress.vuejs.org).

### Lectures supplémentaires

Voici quelques éléments non couverts dans cet article que je pense également valables à explorer :

* [Conteneurs personnalisés](https://vitepress.vuejs.org/guide/markdown#custom-containers)
* [Utilisation de Vue dans le markdown](https://vitepress.vuejs.org/guide/using-vue#using-vue-in-markdown)
* [Section Équipe](https://vitepress.vuejs.org/guide/theme-team-page)
* [Publicités Carbon](https://vitepress.vuejs.org/guide/theme-carbon-ads)

### Ressources

* [Démo en direct](https://adocs.vercel.app)
* [Dépôt GitHub](https://github.com/Evavic44/adocs)

Si vous êtes un fan de l'open source comme moi ou si vous aimez entendre parler de tels projets cool, suivez-moi sur mes réseaux sociaux pour ne pas manquer mon prochain article. Santé. 🍷

[GitHub](https://github.com/evavic44) | [Twitter](https://twitter.com/victorekea) | [Blog](https://eke.hashnode.dev) | [Portfolio](https://victoreke.com)