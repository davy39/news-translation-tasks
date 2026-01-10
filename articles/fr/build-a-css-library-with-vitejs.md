---
title: Comment créer une bibliothèque CSS avec Vite.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-15T16:47:22.000Z'
originalURL: https://freecodecamp.org/news/build-a-css-library-with-vitejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-markus-spiske-3872166.jpg
tags:
- name: CSS
  slug: css
- name: Libraries
  slug: libraries
- name: projects
  slug: projects
seo_title: Comment créer une bibliothèque CSS avec Vite.js
seo_desc: "By Ali Haydar\nBuilding a CSS library might seem like something you'd do\
  \ out of pure curiosity, just to learn and explore. But it can be so much more than\
  \ that. \nI've seen custom-built CSS libraries used everywhere from big organisations\
  \ to scrappy yo..."
---

Par Ali Haydar

Créer une bibliothèque CSS peut sembler être quelque chose que vous feriez par pure curiosité, juste pour apprendre et explorer. Mais cela peut être bien plus que cela. 

J'ai vu des bibliothèques CSS personnalisées utilisées partout, des grandes organisations aux jeunes startups dynamiques.

## Qu'est-ce qu'une bibliothèque CSS ?

Vous pouvez penser à une bibliothèque CSS comme à un thème que vous pouvez utiliser dans plusieurs projets. C'est utile si vous ne voulez pas répéter le style à chaque fois ou copier-coller votre code. C'est également utile si vous voulez être cohérent dans vos applications web (ce qui est bon pour votre marque).

Ainsi, une bibliothèque/thème CSS partagé augmentera votre efficacité et votre vitesse de développement, et cela peut vous aider à développer votre produit tout en maintenant la cohérence. Cela peut également faire partie d'un système de design plus complet [design system](https://www.robertcreative.com/blog/what-is-a-design-system).

L'accent de cet article sera davantage sur la création de la bibliothèque CSS plutôt que sur son style. Le résultat sera une bibliothèque avec un concept similaire à [bootstrap](https://getbootstrap.com/), où vous pouvez utiliser des classes CSS et styliser l'élément HTML associé.

Alors, comment pouvons-nous créer ce type de bibliothèque, et quels outils devons-nous utiliser ?

Voici un résumé de ce que nous allons créer :

- Créer une bibliothèque avec Vite, pas une application web
- Gérer les actifs statiques utilisés dans votre fichier CSS
- Utiliser SASS au lieu de CSS lors de la création de la bibliothèque
- Packager la bibliothèque avec npm

## Comment configurer le projet

Nous allons utiliser [Vite](https://vitejs.dev/) pour créer notre bibliothèque CSS. Ensuite, nous la packagerons avec npm, et enfin, nous l'utiliserons dans un nouveau projet front-end.

Vite est un serveur de développement et un outil de construction qui rend la mise en œuvre de projets web rapide et fluide.

Suivez ces étapes pour commencer :

- Exécutez `npm init @vitejs/app`
- Entrez un nom de projet
- Sélectionnez un framework (Vanilla, Vue, React, etc.) – ici, nous choisirons "vanilla" car nous nous concentrons sur CSS

L'entrée du projet est index.html. Nous pouvons utiliser ce fichier pour tester ce que nous créons. Mais il ne sera pas inclus dans la bibliothèque que nous créons.

### Comment mettre à jour le code de base

Tout d'abord, nettoyons le code de base existant.

Nous mettrons à jour le fichier HTML pour inclure un bouton et une div avec un logo en arrière-plan comme ceci :

  ```
  <!DOCTYPE html>
  <html lang="fr">
    <head>
      <meta charset="UTF-8" />
      <link rel="icon" type="image/svg+xml" href="favicon.svg" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Vite App</title>
    </head>
    <body>
      <div id="app">
        <div class="logo"></div>
        <button class="tomato">Cliquez-moi</button>
      </div>
      <script type="module" src="/src/main.ts"></script>
    </body>
  </html>
  ```

Ensuite, sous le répertoire "src", supprimez le contenu du fichier main.ts, en gardant la première ligne qui importe `style.css`

Ensuite, dans le fichier `style.css`, ajoutez le code suivant :

  ```
  .tomato {
  background-color: tomato;
  }
  .logo {
  background: url(/logo.png) no-repeat;
  height: 300px;
  }
  ```

Nous devons copier le fichier logo.png sous le dossier racine du projet (n'hésitez pas à utiliser une autre image au lieu de logo.png et à changer la hauteur en conséquence).

## Comment créer notre bibliothèque CSS

Avant de créer une build, lançons l'application localement. Dans votre terminal :

- Naviguez jusqu'au dossier racine de votre projet
- Exécutez `npm install` pour installer les dépendances du projet
- Exécutez `npm run dev` pour démarrer le serveur local

Ouvrez l'application dans votre navigateur : http://localhost:3000 (généralement, c'est sur le port 3000 sauf si ce port est déjà utilisé par une autre application).

Maintenant, il est temps de créer le projet, tapez simplement `npm run build`. Cela créera un dossier `dist` avec les fichiers suivants :

![dist-folder-1](https://www.freecodecamp.org/news/content/images/2021/09/dist-folder-1.png)

### Comment configurer la build

Le dossier généré ressemble à une build pour une application web qui doit être hébergée et servie. Mais nous cherchons à créer une bibliothèque à la place. Nous devons donc ajouter quelques configurations pour y parvenir :

Au niveau racine de votre projet, créez un nouveau fichier `config.vite.js` :

  ```
  import { defineConfig } from "vite";
  import path from "path";

  module.exports = defineConfig({
  build: {
      lib: {
      entry: path.resolve(__dirname, "src/main.ts"),
      name: "MyCssLib",
      },
  },
  });

  ```

Exécutez `npm run build` à nouveau. Remarquez la nouvelle structure du dossier dist :

![dist-folder-2](https://www.freecodecamp.org/news/content/images/2021/09/dist-folder-2.png)

Dans ce cas, nous n'avons plus de fichier HTML dans le bundle, et nos styles sont toujours dans un fichier styles.css. Mais vous verrez ici que le fichier logo que nous référençons dans notre fichier CSS n'est plus là.

Ce qui s'est passé ici, c'est que Vite a intégré les actifs en tant qu'URL de données base64. Ainsi, l'utilisation de ce nouveau fichier CSS fonctionnera toujours correctement – similaire à la référence du fichier d'actif :

![inline-css-url](https://www.freecodecamp.org/news/content/images/2021/09/inline-css-url.png)

C'est cool, mais cela peut poser un problème dans les grands projets où le fichier CSS peut devenir très volumineux s'il contient plusieurs actifs référencés.

### Comment gérer les actifs

Vite offre une manière simple de gérer les actifs, où vous conservez le même fichier et le chemin référencé dans CSS fonctionne toujours.

À la racine de votre projet, créez un dossier `public` et déplacez le fichier `logo.png` dedans. L'application web locale reconnaîtra toujours le logo (vérifiez que cela fonctionne toujours sur http://localhost:3000).

Exécutez `npm run build` à nouveau. Le nouveau dossier dist ressemblera à ceci :

![dist-folder-3](https://www.freecodecamp.org/news/content/images/2021/09/dist-folder-3.png)
  
Remarquez que le fichier logo est toujours là au niveau racine. Si vous ouvrez le fichier CSS, il référencera ce même fichier logo. 

Il est pratique ici d'avoir un dossier assets pour contenir tous vos actifs. Vous pouvez créer ce dossier sous le répertoire `public`. N'oubliez pas de mettre à jour le chemin vers les actifs dans votre fichier CSS (de `/logo.png` à `/assets/logo.png` dans ce cas).

### Comment utiliser SASS pour le style

Les développeurs utilisent souvent [SASS](https://sass-lang.com/) pour le style car il offre beaucoup de flexibilité et d'organisation. Vite gère SASS directement. Vérifions cela :

Installez SASS en exécutant `npm install sass`. Sous le dossier "src", changez le nom du fichier `style.css` en `style.scss`

Ensuite, ajoutez quelques modifications SASS au fichier `style.scss`. Par exemple, utilisez une variable de couleur :

  ```
  $color: tomato;

  .tomato {
  background-color: $color;
  }
  ```

Ensuite, vous mettrez à jour le fichier "main.ts" pour pointer vers `style.scss` au lieu de `style.css`.

Exécutez `npm run build` pour créer une nouvelle build, et vérifiez le fichier "style.css" qui a été généré dans le dossier "dist" – il a le CSS correct :

  ```
  .tomato{background-color:tomato}
  ```

## Comment packager la bibliothèque

Maintenant, il est temps de packager la bibliothèque (ce qui a été généré dans le dossier dist). Nous allons utiliser npm pour cela.

Tout d'abord, vous devez mettre à jour le fichier "package.json" pour inclure une nouvelle propriété appelée `files`. Selon la [documentation npm](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#files), le champ `files` est un tableau de motifs de fichiers qui décrit les entrées à inclure lorsque votre package est installé en tant que dépendance. 

Nous devons seulement packager le fichier CSS généré, donc l'entrée supplémentaire dans le fichier "package.json" sera `files: [dist/style.css]`.

Ensuite, vous exécuterez `npm pack`. Cela créera un nouveau fichier. Dans ce cas, "vite-CSS-lib-0.0.0.tgz".

### Comment utiliser le package

Commencez par créer un nouveau projet (que vous pouvez faire de la même manière que nous avons commencé avec Vite). Une fois terminé, suivez ces étapes :

- Installez le package nouvellement créé : `npm install <path-to-lib>/vite-css-lib-0.0.0.tgz`
- Dans votre fichier "main.js", importez le fichier CSS : `import 'node_modules/vite-css-lib/dist/style.css`
- Dans votre fichier "index.html", ajoutez un bouton avec une classe "tomato" : `<button class="tomato">Submit</button>`

Lancez votre application. Elle devrait avoir un bouton avec une couleur de fond tomate.

## Choses à améliorer dans la bibliothèque

Bien sûr, ce n'est pas un produit fini – il peut toujours être amélioré.

Vous pouvez commencer par exporter les fichiers SASS plutôt qu'un fichier CSS compilé afin que les applications dépendant de votre bibliothèque puissent utiliser SASS directement. Vous pouvez faire cela via un plugin Vite/Rollup : `https://vitejs.dev/guide/api-plugin.html`

De plus, lorsque vous packagez la bibliothèque avec npm, tout ce qui se trouve dans package.json sera inclus dans le package. Vous pouvez nettoyer le fichier package.json pour arrêter d'inclure des scripts/dépendances inutiles. Vous pouvez lire plus sur [comment faire cela ici](https://stackoverflow.com/questions/48802204/npm-publish-removing-scripts-from-package-json).

Enfin, configurez un bundle avec un fichier JS qui exporte le fichier CSS créé pour permettre l'importation de la bibliothèque sans avoir à référencer node_modules/lib/style.css.

J'espère que cet article a été utile. Comment amélioreriez-vous ce processus ? Comment créeriez-vous une bibliothèque CSS ?