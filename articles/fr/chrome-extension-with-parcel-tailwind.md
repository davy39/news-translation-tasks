---
title: Comment créer une extension Chrome – un tutoriel de développement de plugin
  navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-25T19:04:48.000Z'
originalURL: https://freecodecamp.org/news/chrome-extension-with-parcel-tailwind
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/emile-perron-xrVDYZRGdw4-unsplash.jpg
tags:
- name: chrome extension
  slug: chrome-extension
- name: plugins
  slug: plugins
- name: tailwind
  slug: tailwind
seo_title: Comment créer une extension Chrome – un tutoriel de développement de plugin
  navigateur
seo_desc: 'By Marouane Rassili

  Building a Chrome extension can be overwhelming. It''s different than building a
  web app in that you don''t want to put too much JavaScript overhead on the browser
  since your extension will be run along with the website you''re visit...'
---

Par Marouane Rassili

Créer une extension Chrome peut être intimidant. C'est différent de la création d'une application web dans le sens où vous ne voulez pas ajouter trop de surcharge JavaScript au navigateur, car votre extension sera exécutée en même temps que le site web que vous visitez. Vous ne bénéficiez pas non plus des avantages de la compilation et du débogage disponibles avec les bundlers et frameworks actuels.

Lorsque j'ai décidé de créer une extension Chrome, j'ai constaté que le nombre de posts et d'articles sur le sujet est assez limité. Et il y a encore moins d'informations lorsque vous souhaitez utiliser l'une des nouvelles technologies comme TailwindCSS.

Dans ce tutoriel, nous allons découvrir comment créer une extension Chrome en utilisant Parcel.js pour la compilation et le suivi, et TailwindCSS pour le style. Nous parlerons également de la manière de séparer votre style de celui du site web pour éviter les conflits CSS – mais nous y reviendrons plus tard.

**Il existe quelques types d'extensions Chrome dignes d'être mentionnés :**

- **Scripts de contenu** : Le premier type d'extension Chrome est le plus courant. Il s'exécute dans le contexte d'une page web et peut être utilisé pour modifier son contenu. C'est le type d'extension que nous allons créer.
- **Popup** : Les extensions basées sur des popups utilisent l'icône de l'extension à droite de la barre d'adresse pour ouvrir une popup qui peut contenir n'importe quel contenu HTML que vous souhaitez.
- **Interface d'options** : Vous l'avez deviné ! Il s'agit d'une interface pour personnaliser les options d'une extension. Elle est accessible en cliquant avec le bouton droit sur l'icône de l'extension et en sélectionnant "options" ou en naviguant vers la page de l'extension depuis la liste des extensions Chrome `chrome://extensions`
- **Extension DevTools** : "Une extension DevTools ajoute des fonctionnalités aux Chrome DevTools. Elle peut ajouter de nouveaux panneaux d'interface utilisateur et barres latérales, interagir avec la page inspectée, obtenir des informations sur les requêtes réseau, et plus encore". -[Documentation Google Chrome](https://developer.chrome.com/extensions/devtools)

Dans ce tutoriel, nous allons créer une extension Chrome en utilisant uniquement des scripts de contenu en affichant du contenu sur la page web et en interagissant avec le DOM.

## Comment bundler votre extension Chrome en utilisant Parcel.js V2

Parcel.js est un bundler d'applications web sans configuration. Il peut utiliser n'importe quel type de fichier comme point d'entrée. Il est simple à utiliser et fonctionnera pour tout type d'application, y compris les extensions Chrome.

Tout d'abord, créez un nouveau dossier appelé `demo-extension` (assurez-vous d'avoir `yarn` ou `npm` installé, je vais utiliser `yarn` pour ce post) :

`$ mkdir demo-extension && cd demo-extension && yarn init -y`

Ensuite, nous allons installer Parcel comme une dépendance locale :

`$ yarn add -D parcel@next`

Maintenant, créez un nouveau répertoire appelé `src` :

`$ mkdir src`


### Ajout d'un fichier manifest

Chaque extension de navigateur a besoin d'un fichier manifest. C'est ici que nous définissons la version et les métadonnées de notre extension, mais aussi les scripts utilisés (contenu, arrière-plan, popup, etc.) et les permissions si nécessaire.

Vous pouvez trouver le schéma complet dans la documentation de Chrome : https://developer.chrome.com/extensions/manifest

Allons-y et ajoutons un nouveau fichier dans `src` appelé `manifest.json` avec ce contenu :

```json
{
  "name": "Extension de démonstration",
  "description": "Une extension construite avec Parcel et TailwindCSS.",
  "version": "1.0",
  "manifest_version": 2,
}
```

Maintenant, avant d'entrer dans plus de détails sur le fonctionnement des extensions Chrome et le type de choses que vous pouvez faire avec elles, nous allons configurer [TailwindCSS](https://tailwindcss.com/)


### Comment utiliser TailwindCSS avec votre extension Chrome

TailwindCSS est un framework CSS qui utilise des classes utilitaires de bas niveau pour créer des composants d'interface utilisateur visuels réutilisables mais aussi personnalisables.

Tailwind peut être installé de deux manières, mais la manière la plus courante de l'utiliser est via son package NPM :

`$ yarn add tailwindcss`

Ajoutez également `autoprefixer` et `postcss-import` :

`$ yarn add -D autoprefixer postcss-import`

Vous avez besoin de ces outils pour ajouter des préfixes de fournisseurs à vos styles et pour pouvoir écrire une syntaxe comme `@import "tailwindcss/base"` pour importer directement les fichiers Tailwind depuis `node_modules`, respectivement.

Maintenant que nous l'avons installé, créons un nouveau fichier à la racine de notre répertoire et appelons-le `postcss.config.js`. Il s'agit du fichier de configuration pour PostCSS et il contiendra, pour l'instant, ces lignes :

```js
module.exports = {
  plugins: [
    require("postcss-import"),
    require("tailwindcss"),
    require("autoprefixer"),
  ],
};
```

*L'ordre des plugins est important ici !*

C'est tout ! C'est tout ce dont vous avez besoin pour commencer à utiliser TailwindCSS dans votre extension Chrome.

Créez un fichier appelé `style.css` dans votre dossier `src` et incluez les fichiers Tailwind :

```css
@import "tailwindcss/base";
@import "tailwindcss/utilities";
```

### Supprimer le CSS inutilisé en utilisant PurgeCSS

Assurons-nous également de n'importer que les styles que nous utilisons en activant la capacité de purge de Tailwind.

Créez un nouveau fichier de configuration Tailwind en exécutant :

`$ npx tailwindcss init` : cela créera un nouveau fichier `tailwind.config.js`.

Pour supprimer le CSS inutilisé, nous allons ajouter nos fichiers sources au champ purge comme ceci :

```js
module.exports = {
  purge: [
    './src/**/*.js', 👈
  ],
  theme: {},
  variants: {},
  plugins: [],
}
```

Maintenant, notre CSS sera purgé et les styles inutilisés seront supprimés lorsque vous construirez pour la production.

### Comment activer le rechargement à chaud dans votre extension Chrome

Une dernière chose avant d'ajouter du contenu à notre extension : activons le rechargement à chaud.

Chrome ne recharge pas les fichiers sources lorsque vous apportez de nouvelles modifications – vous devez cliquer sur le bouton "Recharger" sur la page des extensions. Heureusement, il existe un package NPM qui fait le rechargement à chaud pour nous.

`$ yarn add crx-hotreload`

Pour l'utiliser, nous allons créer un nouveau fichier appelé `background.js` dans notre dossier `src` et importer `crx-hotreload`

```js
import "crx-hotreload";
```

Enfin, pointez vers `background.js` dans `manifest.json` afin qu'il puisse être servi avec notre extension (le rechargement à chaud est désactivé en production par défaut) :

```json
{
  "name": "Extension de démonstration",
  "description": "Une extension construite avec Parcel et TailwindCSS.",
  "version": "1.0",
  "manifest_version": 2,
  "background": { 👈
    "scripts": ["background.js"]
  },
}
```

Assez de configuration. Construisons un petit formulaire de script dans notre extension.

#### Types de scripts dans une extension Chrome

Comme mentionné au début de ce post, dans les extensions Chrome, il existe quelques types de scripts que vous pouvez utiliser.

Les *scripts de contenu* sont des scripts qui s'exécutent dans le contexte de la page web visitée. Vous pouvez exécuter n'importe quel code JavaScript qui est par ailleurs disponible dans n'importe quelle page web régulière (y compris l'accès/la manipulation du DOM).

Un script d'arrière-plan, en revanche, est l'endroit où vous pouvez réagir aux événements du navigateur, et il a accès aux API de l'extension Chrome.

### Ajout d'un script de contenu

Créez un nouveau fichier appelé `content-script.js` sous le dossier `src`.

Ajoutons ce formulaire HTML à notre nouveau fichier :

```js
import cssText from "bundle-text:../dist/style.css";

const html =
`
<style>${cssText}</style>

<section id="popup" class="font-sans text-black z-50 w-full fixed top-0 right-0 shadow-xl new-event-form bg-white max-w-sm border-2 border-black p-5 rounded-lg border-b-6">
  <header class="flex mb-5 pl-1 items-center justify-between">
    <span class="text-2xl text-black font-extrabold">Nouvel événement !</span>
  </header>
  <main class="event-name-input mb-6">
    <div class="mb-6">
      <label
        for="event-name"
        class="font-bold pl-1 block mb-1 text-black text-xl"
        >
      Nom de l'événement
      </label>
      <div class="duration-400 flex bg-white border-black border-2 rounded-lg py-4 px-4 text-black text-xl focus-within:shadow-outline">
        <input
          id="event-name"
          name="event-name"
          type="text"
          placeholder="web.dev LIVE"
          class="font-medium w-full focus:outline-none"
          />
      </div>
    </div>
    </div>
    <div class="mb-6">
      <label
        for="event-date"
        class="font-bold pl-1 block mb-1 text-black text-xl"
        >
      Date
      </label>
      <div class="event-date-input duration-400 border-black flex bg-white border-2 rounded-lg py-4 px-4  text-xl focus-within:shadow-outline">
        <input
          id="event-date"
          name="event-date"
          type="date"
          class="font-medium w-full focus:outline-none"
          />
      </div>
    </div>
    <div class=" mb-8">
    <label
      for="event-time-input"
      class="font-bold pl-1 block mb-1  text-xl"
      >
    Heure
    </label>
    <div class="inline-flex items-center">
      <input
        id="event-time-input"
        type="time"
        value="17:30"
        class="border-black mr-4 lowercase duration-400 w-auto bg-white text-xl border-2  rounded-lg px-4 py-4 focus:outline-none focus:shadow-outline"
        />
      <div class="inline-flex flex-col">
        <span class="text-xl font-bold">Casablanca</span>
        <span class="text-base font-normal">Afrique</span>
      </div>
    </div>
  </main>
  <footer>
  <button 
    class="duration-400 bg-green-400 text-xl py-4 w-full rounded-lg border-2 border-b-6 leading-7 font-extrabold border-black focus:outline-none focus:shadow-outline"
    >
  Enregistrer
  </button>
  </footer
</section>
`

const shadowHost = document.createElement("div");
document.body.insertAdjacentElement("beforebegin", shadowHost);
const shadowRoot = shadowHost.attachShadow({ mode: 'open' });

shadowRoot.innerHTML = html
```

Styliser une extension de navigateur n'est pas aussi simple que vous pourriez le penser, car vous devez vous assurer que les styles du site web ne sont pas affectés par vos propres styles.

Pour les séparer, nous allons utiliser quelque chose appelé le *Shadow DOM*. Le Shadow DOM est une technique puissante d'encapsulation des styles. Cela signifie que le style est limité à l'arbre Shadow. Par conséquent, rien ne fuit vers la page web visitée. De plus, les styles externes ne remplacent pas le contenu du Shadow DOM, bien que les variables CSS puissent encore être accessibles.

Un *shadow host* est n'importe quel élément DOM auquel nous souhaitons attacher notre arbre Shadow. Une *Shadow Root* est ce qui est retourné par `attachShadow` et son contenu est ce qui est rendu.

**Attention**, la seule façon de styliser le contenu d'un arbre Shadow est d'inclure les styles en ligne. Parcel V2 a une nouvelle fonctionnalité intégrée où vous pouvez importer le contenu d'un bundle et l'utiliser comme texte compilé dans vos fichiers JavaScript. Ensuite, Parcel le remplacera au moment de l'emballage.

Nous avons fait exactement cela avec notre bundle `style.css`. Maintenant, nous pouvons inclure le CSS automatiquement dans le Shadow DOM au moment de la construction.

Maintenant, nous devons informer le navigateur de ce nouveau fichier, allons-y et incluons-le en ajoutant ces lignes à notre manifest :

```json
{
  "name": "Extension de démonstration",
  "description": "Une extension construite avec Parcel et TailwindCSS.",
  "version": "1.0",
  "manifest_version": 2,
  "background": {
    "scripts": ["background.js"]
  },
  👋
  "content_scripts": [
    {
      "matches": ["<all_urls>"],
      "js": ["content-script.js"],
    }
  ]
}
```

Pour servir notre extension, nous allons ajouter quelques scripts à notre `package.json` :

```json
  "scripts": {
    "prebuild": "rm -rf dist .cache .parcel-cache",
    "build:tailwind": "tailwindcss build src/style.css -c ./tailwind.config.js -o dist/style.css",
    "watch": "NODE_ENV=development yarn build:tailwind && cp src/manifest.json dist/ && parcel watch --no-hmr src/{background.js,content-script.js}",
    "build": "NODE_ENV=production yarn build:tailwind && cp src/manifest.json dist/ && parcel build src/{background.js,content-script.js}",
  }
```

Enfin, vous pouvez exécuter `yarn watch`, aller sur `chrome://extensions`, et vous assurer que le *Mode Développeur* est activé en haut à droite de la page. Cliquez sur "Charger l'extension décompressée" et sélectionnez le dossier `dist` sous `demo-extension`.

- *Si vous obtenez cette erreur : `Error: Bundles must have unique filePaths`, vous pouvez simplement la corriger en supprimant le champ `main` dans votre `package.json`*

## Comment publier votre extension sur le Chrome Web Store

Avant d'aller plus loin, ajoutons un nouveau script NPM qui nous aidera à compresser les fichiers de l'extension comme requis par Chrome.

```json
  "scripts": {
    "prebuild": "rm -rf dist .cache",
    "build:tailwind": "tailwindcss build src/style.css -c ./tailwind.config.js -o dist/style.css",
    "watch": "NODE_ENV=development yarn build:tailwind && cp src/manifest.json dist/ && parcel watch --no-hmr src/{background.js,content-script.js}",
    "build": "NODE_ENV=production yarn build:tailwind && cp src/manifest.json dist/ && parcel build src/{background.js,content-script.js}",
    "zip": "zip -r chrome-extension.zip ./dist" 👈
  }
```

Si vous n'avez pas encore installé `zip`, veuillez le faire :
- MacOS : `brew install zip`
- Linux : `sudo apt install zip`
- Pour Windows, vous pouvez utiliser la commande powershell `Compress-Archive` de manière similaire : `powershell Compress-Archive -Path .\\dist\\ -Destination .\\chrome-extension.zip`

Maintenant, tout ce que vous avez à faire est de vous rendre sur le [Tableau de bord des développeurs du Chrome Web Store](https://chrome.google.com/webstore/devconsole/register) pour configurer votre compte et publier votre extension ?


- *Vous pouvez trouver la démonstration complète de ce tutoriel hébergée sur mon compte GitHub [ici](https://github.com/mrassili/extension-demo)*

## Conclusion

En fin de compte, les extensions Chrome ne sont pas si différentes des applications web. Aujourd'hui, vous avez appris à développer une extension en utilisant les dernières technologies et pratiques en matière de développement web.

Espérons que ce tutoriel vous a aidé à accélérer un peu le développement de votre extension !

Si vous avez trouvé cela utile, veuillez en parler sur Twitter et me suivre à [@marouanerassili](https://twitter.com/marouanerassili).

Merci !