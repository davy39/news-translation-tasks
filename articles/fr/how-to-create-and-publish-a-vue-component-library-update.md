---
title: Comment créer et publier une bibliothèque de composants Vue – Mise à jour
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2023-05-30T20:11:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-publish-a-vue-component-library-update
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-pixabay-159711.jpg
tags:
- name: components
  slug: components
- name: vite
  slug: vite
- name: vue
  slug: vue
seo_title: Comment créer et publier une bibliothèque de composants Vue – Mise à jour
seo_desc: 'Back in 2020, I wrote a post about building a Vue Component library. Since
  then the package I used has been deprecated, and the recommended way to build a
  library/package is to use Vite.

  Getting Started

  I started off the project by running npm create...'
---

En 2020, j'ai [écrit un article](https://www.freecodecamp.org/news/how-to-create-and-publish-a-vue-component-library/) sur la création d'une bibliothèque de composants Vue. Depuis, le package que j'utilisais a été obsolète, et la méthode recommandée pour construire une bibliothèque/package est d'utiliser Vite.

## Installation

J'ai commencé le projet en exécutant `npm create vite@latest` et en nommant mon projet `brian-component-lib` pour rester cohérent avec mon précédent article. J'ai également choisi d'utiliser TypeScript et Vue lorsque ces options sont apparues.

## Le Composant

Le composant que j'ai construit est un clone des boutons utilisés sur freeCodeCamp.org

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-160.png align="left")

*Composant bouton que nous construisons*

Voici le code pour ce composant. Notez qu'il utilise TypeScript et le format `script setup` disponible dans Vue 3.

```js
<script setup lang="ts">

defineProps<{ text: string }>()

</script>

<template>
  <button class="btn-cta">{{ text }}</button>
</template>

<style scoped>
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

Ensuite, nous devons exposer ce composant dans la bibliothèque. Nous le faisons en l'exportant depuis un fichier `index.ts`.

```js
import FccButton from "./components/FccButton.vue";

export { FccButton };
```

## Configuration

Avec le code du composant prêt à l'emploi, nous devons nous assurer que Vite et le fichier `package.json` sont correctement configurés.

Vite offre de nombreuses options lors de la construction du code. Nous nous intéressons au ["Mode Bibliothèque"](https://vitejs.dev/guide/build.html#library-mode).

```js
import { defineConfig } from "vite";
import { resolve } from "path";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: {
    lib: {
      // src/indext.ts est l'endroit où nous avons exporté le(s) composant(s)
      entry: resolve(__dirname, "src/index.ts"),
      name: "BrianComponentLibrary",
      // le nom des fichiers de sortie lorsque la construction est exécutée
      fileName: "brian-component-lib",
    },
    rollupOptions: {
      // assurez-vous d'externaliser les dépendances qui ne doivent pas être regroupées
      // dans votre bibliothèque
      external: ["vue"],
      output: {
        // Fournir des variables globales à utiliser dans la construction UMD
        // pour les dépendances externalisées
        globals: {
          vue: "Vue",
        },
      },
    },
  },
});
```

Voici le fichier `package.json`. Nous devons nous assurer que nous avons les propriétés nécessaires pour pointer vers nos fichiers construits. Pour plus d'informations sur ce que fait chaque propriété, vous pouvez survoler dans VS Code.

```json
{
  "name": "brian-component-lib",
  "version": "1.0.0",
  "type": "module",
  "files": ["dist"],
  "main": "./dist/brian-component-lib.umd.cjs",
  "module": "./dist/brian-component-lib.js",
  "exports": {
    ".": {
      "import": "./dist/brian-component-lib.js",
      "require": "./dist/brian-component-lib.umd.cjs"
    },
    "./style.css": "./dist/style.css"
  },
  "types": "./dist/index.d.ts",
  "scripts": {
    "dev": "vite",
    "build": "vite build && vue-tsc --emitDeclarationOnly",
    "types": "vue-tsc ",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.2.47"
  },
  "devDependencies": {
    "@types/node": "^20.2.5",
    "@vitejs/plugin-vue": "^4.2.3",
    "typescript": "^5.0.2",
    "vite": "^4.3.9",
    "vue-tsc": "^1.4.2"
  }
}
```

Pour que `vue-tsc --emitDeclarationOnly` fonctionne lors de la construction, nous devons ajouter les propriétés suivantes à la section `compilerOptions` du fichier tsconfig.json :

```javascript
"outDir": "dist",
"declaration": true,
```

Nous devons également supprimer la propriété `noEmit: true`. Cela permettra à nos types d'être disponibles dans le package, afin qu'un projet utilisant TypeScript avec Vue ne nous crie pas dessus pour ne pas avoir déclaré de types.

J'ai également ajouté cette ligne pour m'assurer que mes fichiers `App.vue` et `main.ts` ne sont pas inclus dans les fichiers construits de la bibliothèque de composants.

`"exclude": ["src/App.vue", "src/main.ts"],`

## Tester la Bibliothèque

Nous pouvons maintenant exécuter `npm run build` et ensuite tester notre bibliothèque. Pour ce faire, ouvrez un projet Vue (vous pouvez ouvrir un projet Vue 3 actuel que vous avez, ou en créer un vide).

À l'intérieur du fichier package.json du projet que vous venez d'ouvrir, ajoutez ce qui suit aux dépendances :

`"brian-component-lib": "file:../brian-component-library"`

Assurez-vous que le chemin de fichier que vous mettez pointe vers le dossier correct où se trouve la bibliothèque de composants.

Exécutez `npm install` et vous devriez maintenant avoir la bibliothèque de composants dans votre `node_modules`.

Importez le composant dans l'une des pages pour tester qu'il fonctionne.

Remarque : Vous devrez également importer le CSS car il est construit dans son propre fichier pendant le processus de construction.

```js
<script setup lang="ts">
import { FccButton } from 'brian-component-lib'
import "brian-component-lib/style.css"
</script>

<template>
    <FccButton text="Run the Tests" />
</template>
```

Vous devriez maintenant voir le bouton lorsque vous exécutez le projet.

## Comment Publier sur NPM

Si vous ne vous êtes pas connecté à NPM dans votre terminal, vous pouvez le faire en exécutant la commande `npm adduser`.

Ensuite, exécutez simplement la commande `npm publish` et le package devrait être publié et mis à disposition sur NPM.

## Conclusion

Vite rend assez facile la publication d'une bibliothèque de composants. J'espère que cela a aidé. [Faites-le moi savoir sur Twitter](https://twitter.com/the_brianb) si c'est le cas ou si vous aimeriez voir autre chose de ma part à l'avenir.

Vous pouvez voir le dépôt pour ce code ici : [https://github.com/briancbarrow/vue-component-library-2023](https://github.com/briancbarrow/vue-component-library-2023)