---
title: "Un premier regard sur Bun 1.0 \x13 L'alternative \x0E Node.js"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-15T07:58:01.000Z'
originalURL: https://freecodecamp.org/news/a-quick-look-at-bun-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant--2-.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: "Un premier regard sur Bun 1.0 \x13 L'alternative \x0E Node.js"
seo_desc: 'By Nishant Kumar

  A wise man once told me, "When you start eating Bun, Node.js will feel bland".

  But why is that relevant? JavaScript got way faster with a new JavaScript runtime
  called Bun, which is now production-ready with its version 1.0 release.

  ...'
---

Par Nishant Kumar

Un homme sage m'a dit un jour : "Quand tu commences  manger Bun, Node.js te semblera fade".

Mais pourquoi est-ce pertinent ? JavaScript est devenu bien plus rapide avec un nouveau runtime JavaScript appel Bun, qui est maintenant pr
t pour la production avec sa version 1.0.

Mais comment et pourquoi est-il plus rapide que Node.js ? Beaucoup de questions viennent  l'esprit.

Je rpondrai  certaines de ces questions dans cet article. Et je le ferai rapidement car je suis maintenant plus rapide, tout comme mon pote JavaScript, qui cuit dans le four avec Bun 1.0.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant--3-.gif)

Bun est un outil tout-en-un rapide pour executer, construire, tester et dboguer JavaScript et TypeScript, d'un seul fichier  une application full-stack.

Voici quelques choses que nous pouvons faire avec Bun.

## Executez votre code plus rapidement avec Bun

Maintenant, nous n'avons plus besoin d'outils comme `npm`, `pnpm` ou `yarn` car Bun est 17 fois plus rapide. Jetez un il aux donnes ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/266451126-23cbde35-b859-41b5-9480-98b88bf40c44.png)

Bun ne prend que 0,36 seconde pour compiler votre code, alors qu'il faut environ 6,44 secondes avec pnpm, 10,58 secondes avec npm et 12,08 secondes avec yarn.

## Bun supporte le rechargement  chaud

Bun supporte le rechargement  chaud ds la sortie de la bote, donc vous n'avez pas besoin d'outils comme Nodemon. Il rafrachira automatiquement le serveur lors de l'execution de code JavaScript ou TypeScript.

Vous pouvez remplacer `npm run` par `bun run` pour conomiser plus de 150 ms  chaque fois que vous executez une commande.

Voici le graphique complet :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-14-at-7.17.45-PM-1.png)

D'aprs le graphique ci-dessus, l'utilisation de `npm` prend environ 176 ms pour s'executer, `yarn` prend environ 131 ms. Dans le cas de `pnpm`, cela prend 259 ms. Cependant, cela prend environ 7 ms dans le cas de `Bun`. C'est rapide, n'est-ce pas ?

## Bun en tant que bundler JavaScript

Bun est galement un bundler JavaScript avec des performances de premire classe et une API de plugin compatible ESBuild, donc nous n'avons pas besoin de choses comme :

* ESBuild
* Webpack
* Parcel, .parcelrc
* Rollup, rollup.config.js

![Image](https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant--2-.gif)

Bun supporte maintenant Next.js, Remix, Nuxt, Astro, SvelteKit, Nest, SolidStart et Vite.

### Bun a une compatibilit ESM et CommonJS

Une autre grande fonctionnalit de Bun est que nous pouvons utiliser les modules ES et CommonJs ensemble dans le mme fichier, ce qui n'tait pas possible dans Node.js.

Vous pouvez utiliser `import` et `require()` dans le mme fichier :

```javascript
import lodash from "lodash";
const _ = require("underscore");
```

En outre, Bun a un support intgr pour les API standard du Web disponibles dans les navigateurs, telles que `fetch`, ainsi que des API Bun supplementaires comme `Bun.file()` pour lire un fichier de manire paresseuse et `Bun.Write()` pour crire un fichier dans le systme de fichiers local, ce qui est beaucoup plus simple que Node.js.

#### Exemple de `Bun.file()`

```javascript
const file = Bun.file("package.json");
const contents = await file.text();
```

Le code ci-dessus lira le contenu d'un fichier `package.json` et transfrera son contenu dans une nouvelle variable appele `contents`.

#### Exemple de `Bun.write()`

```javascript
await Bun.write("index.html", "<html/>");
await Bun.write("index.html", Buffer.from("<html/>"));
await Bun.write("index.html", Bun.file("home.html"));
await Bun.write("index.html", 
await fetch("https://example.com/"));
```

Dans le code ci-dessus, `Bun.write()` crira la chane `"<html/>"`, ou copiera le contenu du fichier `home.html` dans le fichier `index.html`. Si nous devons recuprer des donnes, il recuprera les rsultats d'une API web externe et crira le contenu dans un fichier `index.html`.

## Pourquoi Bun est-il si rapide ?

Bun est rapide car il utilise le moteur JavaScriptCore, tandis que Node.js utilise le moteur JavaScript V8. Le premier a t optimis pour un temps de dmarrage plus rapide.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant.png)

Si vous voulez que les choses aillent plus vite, vous devriez envisager de remplacer Node.js par Bun.

## Comment commencer avec Bun

Vous pouvez installer Bun sur les systmes MacOS et Linux en utilisant npm :

```javascript
npm install -g bun
```

Maintenant, vous tes pr
t. Pour installer un package npm, faites ceci :

```javascrpt
bun install <package-name>
```

Pour dmarer une application Next.js, faites ceci :

```javascript
bun run dev
```

Tout ce que vous avez  faire est de remplacer `npm` par `bun`.

Cependant, Bun n'est pr
t pour la production que sur les systmes d'exploitation MacOS et Linux. La version Windows est encore experimentale. Pour l'instant, seul le runtime JavaScript est support pour Windows, et non le gestionnaire de paquets, le bundler ou le test runner. Vous pouvez en lire plus  ce sujet [ici](https://bun.sh/docs/installation#windows).

## Conclusion

Cet article montre comment vous pouvez utiliser Bun comme alternative  Node.js et accelrer votre temps de dveloppement.

Vous pouvez galement consulter ma vido sur **[The Node.js killer is here

Bun 1.0 First Look](https://youtu.be/q5UKY_dCmh4?si=satm6TAv6Zmh5OCn)**.

Merci d'avoir lu !