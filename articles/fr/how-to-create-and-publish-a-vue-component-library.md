---
title: Comment créer et publier une bibliothèque de composants Vue
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2020-07-22T20:21:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-publish-a-vue-component-library
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/trnava-university-BEEyeib-am8-unsplash.jpg
tags:
- name: components
  slug: components
- name: vue
  slug: vue
seo_title: Comment créer et publier une bibliothèque de composants Vue
seo_desc: "Component libraries are all the rage these days. They make it easy to maintain\
  \ a consistent look and feel across an application. \nI've used a variety of different\
  \ libraries in my career so far, but using a library is very different than knowing\
  \ exact..."
---

Les bibliothèques de composants sont très populaires ces jours-ci. Elles facilitent le maintien d'une apparence et d'une convivialité cohérentes dans une application. 

J'ai utilisé une variété de bibliothèques différentes dans ma carrière jusqu'à présent, mais utiliser une bibliothèque est très différent de savoir exactement ce qui entre dans la création de celle-ci. 

Je voulais une compréhension plus approfondie de la manière dont une bibliothèque de composants est construite, et je veux vous montrer comment vous pouvez obtenir une meilleure compréhension également.

Pour créer cette bibliothèque de composants, nous allons utiliser le package npm `vue-sfc-rollup`. Ce package est un utilitaire très utile lors du démarrage d'une bibliothèque de composants. 

Si vous avez une bibliothèque existante avec laquelle vous souhaitez utiliser cet utilitaire, reportez-vous à la [documentation](https://www.npmjs.com/package/vue-sfc-rollup) qu'ils fournissent. 

> Mise à jour de mai 2023 : vue-sfc-rollup est maintenant considéré comme obsolète. Le remplacement recommandé est Vite, spécifiquement la configuration de "construction de bibliothèque". 

Vous pouvez continuer à lire à des fins de pratique et d'éducation. Mais [voici une version mise à jour du tutoriel que vous pouvez suivre et qui utilise Vite](https://www.freecodecamp.org/news/how-to-create-and-publish-a-vue-component-library-update/).

Ce package crée un ensemble de fichiers pour démarrer le projet. Comme l'explique leur documentation, les fichiers qu'il crée incluent les éléments suivants (SFC signifie Single File Component) : 

* une configuration minimale de [rollup](https://rollupjs.org/)
* un fichier package.json correspondant avec des scripts de construction/développement et des dépendances
* un fichier babel.config.js et .browserslistrc minimal pour la transpilation
* un wrapper utilisé par rollup lors de l'empaquetage de votre SFC
* un échantillon SFC pour démarrer le développement
* un fichier d'utilisation échantillon qui peut être utilisé pour charger/tester votre composant/bibliothèque pendant le développement

L'utilitaire prend en charge à la fois les composants à fichier unique ainsi qu'une bibliothèque de composants. Il est important de noter cette phrase de la documentation : 

> En mode bibliothèque, il y a également un 'index' qui déclare les composants exposés dans le cadre de votre bibliothèque.

Tout cela signifie qu'il y a quelques fichiers supplémentaires générés dans le processus de configuration.

# Super, construisons la bibliothèque 

Tout d'abord, vous devrez installer `vue-sfc-rollup` globalement :

`npm install -g vue-sfc-rollup`

Une fois que cela est installé globalement, depuis la ligne de commande, allez dans le répertoire où vous souhaitez que votre projet de bibliothèque soit situé. Une fois que vous êtes dans ce dossier, exécutez la commande suivante pour initialiser le projet.

`sfc-init`

Choisissez les options suivantes dans les invites :

* **S'agit-il d'un composant unique ou d'une bibliothèque ?** Bibliothèque
* **Quel est le nom npm de votre bibliothèque ?** (celui-ci devra être unique sur npm. J'ai utilisé _brian-component-lib_)
* **Cette bibliothèque sera-t-elle écrite en JavaScript ou TypeScript ?** JavaScript (n'hésitez pas à utiliser TypeScript si vous savez ce que vous faites)
* **Entrez un emplacement pour sauvegarder les fichiers de la bibliothèque :** Il s'agit du nom du dossier que vous souhaitez donner à votre bibliothèque. Il sera par défaut le nom npm que vous lui avez donné ci-dessus, vous pouvez donc simplement appuyer sur entrée.

Une fois la configuration terminée, naviguez vers votre dossier et exécutez une installation npm.

```
cd chemin/vers/mon-composant-ou-bib

npm install
```

Une fois cela fait, vous pouvez ouvrir le dossier dans l'éditeur de votre choix.

Comme indiqué ci-dessus, un échantillon de composant Vue a été créé pour nous. Vous pouvez le trouver à l'intérieur du dossier `/src/lib-components`. Pour voir à quoi ressemble ce composant, vous pouvez exécuter `npm run serve` et naviguer vers [http://localhost:8080/](http://localhost:8080/)

Maintenant, ajoutons notre propre composant personnalisé. Créez un nouveau fichier Vue à l'intérieur du dossier `lib-components`. Pour cet exemple, je vais imiter le bouton utilisé dans les sections d'assignation de freeCodeCamp, je vais donc le nommer `FccButton.vue`

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-22-at-10.08.05-AM.png)
_C'est le composant bouton que nous allons construire_

Vous pouvez copier et coller ce code dans votre fichier :

```vue
<template>
  <button class="btn-cta">{{ text }}</button>
</template>

<script>
export default {
  name: "FccButton", // nom du composant vue
  props: {
    text: {
      type: String,
      default: "Entrez le texte du bouton ici"
    }
  },
  data() {}
};
</script>

<style>
.btn-cta {
  background-color: #d0d0d5;
  border-width: 3px;
  border-color: #1b1b32;
  border-radius: 0;
  border-style: solid;
  color: #1b1b32;
  display: block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  -ms-touch-action: manipulation;
  touch-action: manipulation;
  cursor: pointer;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 18px;
  line-height: 1.42857143;
}

.btn-cta:active:hover,
.btn-cta:focus,
.btn-cta:hover {
  background-color: #1b1b32;
  border-width: 3px;
  border-color: #000;
  background-image: none;
  color: #f5f6f7;
}
</style>
```

Vous pouvez voir que nous avons la section de modèle de base en haut avec la classe que nous voulons lui donner. Elle utilise également le texte que l'utilisateur passera. 

À l'intérieur de la balise script, nous avons le nom du composant et les props que le composant prendra. Dans ce cas, il n'y a qu'une seule prop appelée `text` qui a une valeur par défaut de "Exécuter les Tests". 

Nous avons également un peu de style pour lui donner l'apparence que nous voulons.

Pour voir à quoi ressemble le composant, nous devons l'ajouter au fichier `index.js` situé dans le dossier `lib-components`. Votre fichier index.js devrait ressembler à ceci :

```
/* eslint-disable import/prefer-default-export */
export { default as FccButton } from './FccButton';
```

Vous devrez également importer le composant dans le fichier `serve.vue` à l'intérieur du dossier `dev` pour qu'il ressemble à ceci :

```
<script>
import Vue from "vue";
import { FccButton } from "@/entry";

export default Vue.extend({
  name: "ServeDev",
  components: {
    FccButton
  }
});
</script>

<template>
  <div id="app">
    <FccButton />
  </div>
</template>

```

Vous devrez peut-être exécuter `npm run serve` à nouveau pour pouvoir voir le bouton, mais il devrait être visible lorsque vous naviguez vers [http://localhost:8080/](http://localhost:8080/) dans votre navigateur.

Nous avons donc construit le composant que nous voulions. Vous suivrez ce même processus pour tout autre composant que vous souhaitez construire. Assurez-vous simplement de les exporter dans le fichier `/lib-components/index.js` afin de les rendre disponibles depuis le package npm que nous allons publier.

# Publication sur NPM

Maintenant que nous sommes prêts à publier la bibliothèque sur NPM, nous devons passer par le processus de construction pour qu'elle soit empaquetée et prête à partir. 

Avant d'exécuter la commande de construction, je recommande de changer le numéro de version dans le fichier `package.json` pour qu'il soit `0.0.1` puisque c'est le tout premier événement de publication pour notre bibliothèque. Nous voudrons plus qu'un seul composant dans la bibliothèque avant de publier la version 'première' officielle. Vous pouvez en savoir plus sur la version sémantique [ici](https://docs.npmjs.com/about-semantic-versioning).

Pour ce faire, nous exécutons `npm run build`.

Comme le précise la documentation :

> L'exécution du script de construction résulte en 3 fichiers compilés dans le répertoire `dist`, un pour chacune des propriétés `main`, `module` et `unpkg` listées dans votre fichier package.json. Avec ces fichiers générés, vous êtes prêt à partir !

Avec cette commande exécutée, nous sommes prêts à publier sur NPM. Avant de le faire, assurez-vous d'avoir un compte sur NPM (que vous pouvez créer [ici](https://www.npmjs.com/) si nécessaire).

Ensuite, nous devrons ajouter votre compte à votre terminal en exécutant : 

`npm adduser`

### Comprendre package.json

Lorsque nous publions sur npm, nous utilisons le fichier package.json pour contrôler quels fichiers sont publiés. Si vous regardez le fichier `package.json` qui a été créé lorsque nous avons initialement configuré le projet, vous verrez quelque chose comme ceci :

```json
"main": "dist/brian-component-lib.ssr.js",
"browser": "dist/brian-component-lib.esm.js",
"module": "dist/brian-component-lib.esm.js",
"unpkg": "dist/brian-component-lib.min.js",
"files": [
    "dist/*",
    "src/**/*.vue"
],
```

La section sous `files` indique à npm de publier tout ce qui se trouve dans notre dossier `dist` ainsi que tous les fichiers `.vue` à l'intérieur de notre dossier `src`. Vous pouvez mettre à jour cela comme vous le souhaitez, mais nous allons le laisser tel quel pour ce tutoriel.

Parce que nous ne changeons rien avec le fichier package.json, nous sommes prêts à publier. Pour cela, nous devons simplement exécuter la commande suivante :

`npm publish`

![Image](https://www.freecodecamp.org/news/content/images/2020/07/hy.gif)
_Je suis si fier de vous !_

Et c'est tout ! Félicitations ! Vous avez maintenant publié une bibliothèque de composants Vue. Vous pouvez aller sur [npmjs.com](https://www.npmjs.com/) et la trouver dans le registre.