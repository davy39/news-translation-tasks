---
title: Comment j'ai réduit 250 Ko de CSS inutilisé avec PurgeCSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T14:42:35.000Z'
originalURL: https://freecodecamp.org/news/how-i-dropped-250kb-of-dead-css-weight-with-purgecss-28821049fb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UHrztp4ppPEPiHl_Zwo2Mg.jpeg
tags:
- name: Utility First
  slug: utility-first
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: tailwind
  slug: tailwind
- name: technology
  slug: technology
seo_title: Comment j'ai réduit 250 Ko de CSS inutilisé avec PurgeCSS
seo_desc: 'By Sarah Dayan

  I’m a big advocate for utility-first CSS. After trying several methods over the
  years, it’s what I’ve found to be the best, most maintainable and scalable way of
  writing CSS to this day.

  When my coworker Clément Denoix and I built api-...'
---

Par Sarah Dayan

Je suis [une grande défenseuse du CSS utilitaire](https://frontstuff.io/in-defense-of-utility-first-css). Après avoir essayé plusieurs méthodes au fil des ans, c'est ce que j'ai trouvé être **la meilleure, la plus maintenable et la plus scalable façon d'écrire du CSS à ce jour**.

Lorsque mon collègue [Clément Denoix](https://github.com/clemfromspace) et moi avons construit [api-search.io](https://www.api-search.io/), j'ai décidé d'utiliser [Tailwind CSS](https://tailwindcss.com/) pour le styliser. Tailwind CSS est une bibliothèque agnostique en termes de thème, entièrement personnalisable et basée sur les utilitaires.

![Image](https://cdn-media-1.freecodecamp.org/images/MilXaM3nNEeiZFyTo-R1O4tkdjjh-spHRRGS)

L'objectif principal d'une bibliothèque est de vous donner accès à un large ensemble d'outils à utiliser à volonté. Le problème est que, puisque vous utilisez généralement seulement un sous-ensemble de celle-ci, **vous vous retrouvez avec beaucoup de règles CSS inutilisées dans votre build final**.

Dans mon cas, non seulement j'ai chargé l'intégralité de la bibliothèque Tailwind CSS, mais j'ai également ajouté plusieurs variantes à certains modules. Cela a fini par faire peser le fichier CSS final minifié **259 Ko** (avant GZip). C'est assez lourd lorsque l'on considère que le site web est une simple application monopage avec un design minimal.

Vous ne voulez pas charger chaque utilitaire à la main lorsque vous en avez besoin. Ce serait une tâche longue et fastidieuse. Un meilleur scénario est d'avoir tout à votre disposition pendant le développement et **de supprimer automatiquement ce que vous n'avez pas utilisé pendant l'étape de build**.

En JavaScript, nous appelons cela [tree-shaking](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking). Maintenant, grâce à [PurgeCSS](https://www.purgecss.com/), **vous pouvez faire de même avec votre base de code CSS**.

PurgeCSS analyse vos fichiers de contenu et votre CSS, puis fait correspondre les sélecteurs ensemble. Si PurgeCSS ne trouve aucune occurrence d'un sélecteur dans le contenu, il le supprime du fichier CSS.

Pour la plupart, **cela peut fonctionner directement**. Cependant, il y a certaines zones dans n'importe quel site web qui peuvent nécessiter un peu plus de réflexion avant de laisser PurgeCSS faire sa magie.

### Division de mon CSS

Le projet contient trois fichiers CSS principaux :

* Une réinitialisation CSS appelée [normalize.css](https://github.com/necolas/normalize.css), incluse dans Tailwind CSS.
* [Tailwind CSS](https://tailwindcss.com/), la partie la plus substantielle de ma base de code CSS.
* Du CSS personnalisé, principalement pour styliser les composants [InstantSearch](https://community.algolia.com/react-instantsearch/) auxquels je ne pouvais pas ajouter de classes.

PurgeCSS ne peut pas détecter que je dois conserver des sélecteurs tels que `.ais-Highlight`, **car les composants qui l'utilisent n'apparaissent dans le DOM qu'à l'exécution**. Il en va de même pour `normalize.css` : je m'appuie sur lui pour réinitialiser les styles du navigateur, mais beaucoup des composants associés ne seront jamais correspondants car ils sont générés en JavaScript.

Dans le cas des classes commençant par `.ais-`, nous pouvons les trier avec [whitelisting](https://frontstuff.io/how-i-dropped-250-kb-of-dead-css-weight-with-purgecss#whitelisting-runtime-classes). Maintenant, en ce qui concerne les styles de réinitialisation, les sélecteurs sont un peu plus difficiles à suivre. De plus, la taille de `normalize.css` est assez insignifiante et n'est pas destinée à changer. Donc, dans ce cas, j'ai décidé d'ignorer complètement le fichier. Par conséquent, **j'ai dû diviser les styles avant d'exécuter PurgeCSS**.

Ma configuration CSS initiale ressemblait à ceci :

* Un fichier `tailwind.src.css` avec trois directives `@tailwind` : `preflight`, `components` et `utilities`.
* Un fichier `App.css` avec mes styles personnalisés.
* Un script npm dans `package.json` pour construire Tailwind CSS juste avant de démarrer ou de construire le projet. Chaque fois que ce script s'exécute, il génère un fichier `tailwind.css` dans `src`, qui est chargé dans le projet.

La directive `@tailwind preflight` charge `normalize.css`. Je ne voulais pas que PurgeCSS le touche, alors je l'ai déplacé dans un fichier séparé.

```
// tailwind.src.css @tailwind components;
```

```
@tailwind utilities;/* normalize.src.css */ @tailwind preflight;
```

Ensuite, j'ai modifié mon script `tailwind` existant dans `package.json` pour construire `normalize.src.css` séparément.

```
{  "scripts": {    "tailwind": "npm run tailwind:normalize && npm run tailwind:css",    "tailwind:normalize": "tailwind build src/normalize.src.css -c tailwind.js -o src/normalize.css",    "tailwind:css": "tailwind build src/tailwind.src.css -c tailwind.js -o src/tailwind.css"  }}
```

Enfin, j'ai chargé `normalize.css` dans le projet.

```
// src/index.js
```

```
...import './normalize.css'import './tailwind.css'import App from './App'...
```

Maintenant, je peux exécuter PurgeCSS sur `tailwind.css` sans craindre qu'il ne supprime des règles nécessaires.

### Configuration de PurgeCSS

PurgeCSS existe en plusieurs versions : une interface de ligne de commande, une API JavaScript, des wrappers pour Webpack, Gulp, Rollup, et ainsi de suite.

Nous avons utilisé [Create React App](https://github.com/facebook/create-react-app) pour démarrer le site web, donc Webpack est venu [préconfiguré et caché](https://github.com/facebook/create-react-app#get-started-immediately) derrière [react-scripts](https://www.npmjs.com/package/react-scripts). Cela signifie que je ne pouvais pas accéder aux fichiers de configuration de Webpack à moins d'exécuter `npm run eject` pour les récupérer et les gérer directement dans le projet.

Ne pas avoir à gérer Webpack soi-même a de nombreux avantages, donc l'éjection n'était pas une option. Au lieu de cela, j'ai décidé d'utiliser un fichier de configuration personnalisé pour PurgeCSS, et un script npm.

J'ai d'abord créé un `purgecss.config.js` à la racine du projet :

```
module.exports = {  content: ['src/App.js'],  css: ['src/tailwind.css']}
```

* La propriété `content` prend un tableau de fichiers à analyser pour faire correspondre les sélecteurs CSS.
* La propriété `css` prend un tableau de feuilles de style à purger.

Ensuite, j'ai modifié mes scripts npm pour exécuter PurgeCSS :

```
{  "scripts": {    "start": "npm run css && react-scripts start",    "build": "npm run css && react-scripts build",    "css": "npm run tailwind && npm run purgecss",    "purgecss": "purgecss -c purgecss.config.js -o src"  }}
```

* J'ai ajouté un script `purgecss` qui prend mon fichier de configuration et génère la feuille de style purgée dans `src`.
* J'ai fait en sorte que ce script s'exécute chaque fois que nous démarrons ou construisons le projet.

Tailwind CSS utilise des caractères spéciaux, donc si vous utilisez PurgeCSS directement, il peut supprimer des sélecteurs nécessaires. Heureusement, PurgeCSS nous permet d'utiliser un [extracteur personnalisé](https://www.purgecss.com/extractors#creating-an-extractor), qui est une fonction qui liste les sélecteurs utilisés dans un fichier. Pour Tailwind, j'ai dû créer un [extracteur personnalisé](https://tailwindcss.com/docs/controlling-file-size/) :

```
module.exports = {  ...  extractors: [    {      extractor: class {        static extract(content) {          return content.match(/[A-z0-9-:\/]+/g) || []        },        extensions: ['js']      }    }  ]}
```

### Whitelisting des classes générées à l'exécution

**PurgeCSS ne peut pas détecter les classes qui sont générées à l'exécution**, mais il vous permet de définir une liste blanche. Les classes que vous ajoutez à la liste blanche restent dans le fichier final quoi qu'il arrive.

Le projet utilise [React InstantSearch](https://community.algolia.com/react-instantsearch/), qui génère des composants avec des classes qui commencent toutes par `ais-`. Heureusement, PurgeCSS supporte les motifs sous forme d'expressions régulières.

```
module.exports = {  ...  css: ['src/tailwind.css', 'src/App.css'],  whitelistPatterns: [/ais-.*/],  ...}
```

Maintenant, si j'oublie de supprimer une classe que je n'utilise plus de `App.css`, elle sera retirée du build final, mais mes sélecteurs InstantSearch resteront intacts.

### Nouveau build, CSS plus léger

Avec cette nouvelle configuration, **mon fichier CSS final est passé de 259 Ko à... 9 Ko !** C'est assez significatif dans le contexte d'un projet entier, surtout puisque de nombreux pays ont encore des connexions Internet lentes et instables, et de plus en plus de personnes naviguent sur leur téléphone en déplacement.

L'accessibilité, c'est aussi s'adapter aux personnes ayant des connexions à faible bande passante. Il n'est pas acceptable de ne pas essayer d'aider vos utilisateurs avec un Internet plus lent, surtout si ce que vous leur faites télécharger est du code mort.

Cela vaut la peine de prendre un moment pour optimiser votre build. 💡

_Publié à l'origine sur [frontstuff.io](https://frontstuff.io/how-i-dropped-250-kb-of-dead-css-weight-with-purgecss)._