---
title: Comment créer un sélecteur de mode sombre avec Tailwind CSS et Flowbite
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-09T16:11:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-dark-mode-switcher-with-tailwind-css-and-flowbite
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-30-at-13.16.28-1.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Flowbite
  slug: flowbite
- name: HTML
  slug: html
- name: tailwind
  slug: tailwind
seo_title: Comment créer un sélecteur de mode sombre avec Tailwind CSS et Flowbite
seo_desc: 'By Zoltán Szőgyényi

  Dark mode is starting to become a requirement rather that a nice-to-have feature
  like it was back in the day. It gives users the option to choose a theme that''s
  comfortable for them, whether they''re working during the day or at ni...'
---

Par Zoltán Szőgyényi

Le mode sombre commence à devenir une exigence plutôt qu'une fonctionnalité agréable à avoir comme c'était le cas autrefois. Il donne aux utilisateurs la possibilité de choisir un thème qui leur convient, qu'ils travaillent de jour ou de nuit.

Si vous ne l'avez pas encore entendu, Tailwind CSS est l'un des frameworks CSS à la croissance la plus rapide aujourd'hui grâce à son approche utility-first.

Mais même si Tailwind a un assez bon guide d'intégration du mode sombre, il n'y a pas d'explication claire sur la façon de construire un élément de commutateur pour le basculer. En plus de cela, Tailwind n'inclut aucun composant réel qui supporte le mode sombre.

C'est là que Flowbite intervient. Flowbite est une bibliothèque qui fournit des composants et des éléments interactifs sur Tailwind CSS. Et à partir de la version 1.2, il supporte le mode sombre.

Donc, c'est ce que je veux vous montrer aujourd'hui – comment construire un élément de [commutateur de mode sombre Tailwind CSS](https://flowbite.com/docs/customize/dark-mode/), et comment travailler avec les composants Flowbite.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/2021-11-29-16.04.49-1.gif)
_Flowbite - Commutateur de mode sombre Tailwind CSS_

Avant de plonger dans le tutoriel, assurez-vous d'avoir déjà un projet Tailwind CSS configuré. Vous devriez également [installer Flowbite en tant que plugin](https://flowbite.com/docs/getting-started/quickstart/) afin de pouvoir utiliser ses composants en mode sombre.

## Commencer

Si vous avez déjà un projet Tailwind CSS configuré, vous pouvez passer à la partie où vous devez installer Flowbite en tant que plugin. Sinon, suivez les instructions ici sur la façon d'installer Tailwind CSS en premier.

### Comment installer Tailwind CSS

La manière la plus populaire d'utiliser Tailwind CSS est de l'installer en tant que plugin PostCSS. Pour cela, nous devons installer trois packages différents en utilisant NPM :

```shell
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
```

Après cela, vous devriez créer un fichier appelé `postcss.config.js` et ajouter le code suivant à l'intérieur :

```js
// postcss.config.js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  }
}
```

Maintenant, ouvrez votre terminal et exécutez la commande suivante :

```shell
npx tailwindcss init
```

Cela créera un fichier `tailwind.config.js` vide que nous utiliserons plus tard pour inclure Flowbite en tant que plugin.

Ensuite, vous devriez créer un nouveau fichier CSS que vous pouvez appeler `styles.css` et ajouter le code suivant à l'intérieur :

```css
/* ./your-css-folder/styles.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Après avoir compilé le code en utilisant PostCSS, les directives injectées (base, components, utilities) seront disponibles en tant que styles dans le fichier CSS final.

Enfin, tout ce que vous avez à faire est de compiler le CSS en utilisant Tailwind CLI en exécutant la commande suivante :

```shell
npx tailwindcss -o tailwind.css
```

Un fichier `tailwind.css` nouvellement créé sera disponible dans votre projet et vous devriez inclure celui-ci dans vos modèles HTML pour avoir accès aux styles.

Maintenant, vous avez une configuration Tailwind CSS fonctionnelle localement sur votre ordinateur. Si vous souhaitez en savoir plus sur ce processus, consultez le [guide d'installation de Tailwind CSS](https://tailwindcss.com/docs/installation).

### Comment installer Flowbite

Nous devons installer Flowbite pour avoir accès à toutes les fonctionnalités des composants et au support de la version sombre. Heureusement, le processus de configuration est très simple puisqu'il s'agit d'un plugin Tailwind CSS.

Commençons par l'installer via NPM :

```bash
npm i flowbite
```

Ensuite, exigez-le en tant que plugin dans le fichier `tailwind.config.js` :

```javascript
module.exports = {

    plugins: [
        require('flowbite/plugin')
    ]

}
```

Enfin, assurez-vous d'inclure également le fichier JavaScript quelque part avant la fermeture de la balise `<body>` :

```html
<script src="../path/to/flowbite/dist/flowbite.bundle.js"></script>
```

### Comment activer le mode sombre dans Tailwind CSS

La première chose à comprendre est comment fonctionne le mode sombre dans Tailwind CSS. Il existe deux façons de le configurer :

* en utilisant l'option `media`
* en utilisant l'option `class`

La principale différence est que l'option `media` ne prendra en compte que la préférence de schéma de couleurs de votre navigateur, qui est en fait définie par le système d'exploitation.

L'option `class` ne recherchera qu'une classe `.dark` appliquée à la balise principale `<html>`. C'est ce que la plupart des sites web utilisent car, avec cette méthode, les utilisateurs peuvent définir manuellement leur préférence.

Nous allons nous en tenir à l'option `class`, car elle donne aux utilisateurs un meilleur contrôle sur leurs préférences de thème.

Commençons par ajouter ce qui suit au fichier `tailwind.config.js` :

```javascript
module.exports = {
  darkMode: 'class',
  // ...
}

```

Cela configure Tailwind pour utiliser l'option `class` pour le mode sombre.

Ensuite, ajoutez un script à l'élément `<head>` de la page. Cela vérifie une préférence utilisateur précédente dans `localStorage`, et utilise le schéma de couleurs du navigateur comme sauvegarde :

```html
<script>
  // Il est préférable de l'inclure en ligne dans `head` pour éviter le FOUC (flash de contenu non stylisé) lors du changement de pages ou de thèmes
  if (
    localStorage.getItem('color-theme') === 'dark' ||
    (!('color-theme' in localStorage) &&
      window.matchMedia('(prefers-color-scheme: dark)').matches)
  ) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
</script>
```

La raison pour laquelle nous ajoutons ce script à la balise `<head>` et non avant la balise de fermeture `<body>` est que nous voulons éviter un effet de scintillement lors de la définition de la page en mode sombre ou clair.

## Comment construire le commutateur de mode sombre

Maintenant que Tailwind est configuré, nous devons construire l'élément avec lequel les utilisateurs interagiront pour changer le thème du mode sombre au mode clair.

Pour ce faire, nous allons utiliser un élément `<button>` de base de la [bibliothèque de composants de Flowbite](https://flowbite.com/docs/components/buttons/), et utiliser deux icônes interchangeables.

Ajoutez le code HTML suivant à votre page. Je recommande d'ajouter l'élément quelque part en haut à droite de la barre de navigation, car c'est l'endroit naturel où les utilisateurs regardent lorsqu'ils veulent changer le schéma de couleurs :

```html
<button
  id="theme-toggle"
  type="button"
  class="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5"
>
  <svg
    id="theme-toggle-dark-icon"
    class="w-5 h-5 hidden"
    fill="currentColor"
    viewBox="0 0 20 20"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"
    ></path>
  </svg>
  <svg
    id="theme-toggle-light-icon"
    class="w-5 h-5 hidden"
    fill="currentColor"
    viewBox="0 0 20 20"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
      fill-rule="evenodd"
      clip-rule="evenodd"
    ></path>
  </svg>
</button>

```

Les deux objets SVG sont des icônes, et seule l'une d'entre elles est affichée en fonction du thème actif. Et il y a trois identifiants pour les trois objets :

* `#theme-toggle` pour l'élément principal du commutateur de mode sombre
* `#theme-toggle-dark-icon` pour l'icône de lune qui sera affichée lorsque le thème actif est clair
* `#theme-toggle-light-icon` pour l'icône de soleil qui sera affichée lorsque le thème actif est sombre

## Comment gérer le commutateur de mode sombre avec JavaScript

La dernière chose que nous devons faire est de gérer les événements de clic de l'élément du commutateur de mode sombre et de mettre à jour le `localStorage` et les icônes à l'intérieur de l'élément.

Ajoutez le code suivant dans votre fichier JavaScript principal :

```javascript
var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

// Changer les icônes à l'intérieur du bouton en fonction des paramètres précédents
if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
}

var themeToggleBtn = document.getElementById('theme-toggle');

themeToggleBtn.addEventListener('click', function() {

    // basculer les icônes à l'intérieur du bouton
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');

    // si défini via le stockage local précédemment
    if (localStorage.getItem('color-theme')) {
        if (localStorage.getItem('color-theme') === 'light') {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        }

    // si NON défini via le stockage local précédemment
    } else {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('color-theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('color-theme', 'dark');
        }
    }
    
});
```

La première partie du code changera l'icône qui est affichée en fonction de la préférence précédente, soit via le `localStorage`, soit via le schéma de couleurs du navigateur.

La deuxième partie du code gère les événements de clic sur l'élément de commutateur lui-même et définit le `localStorage` en fonction du thème qui a été sélectionné.

### Comment utiliser le commutateur de mode sombre dans la barre de navigation

Nous n'avons pas encore terminé car nous devons trouver un endroit pour positionner le commutateur de mode sombre – et quel meilleur endroit pour le faire que la barre de navigation.

Heureusement, Flowbite propose de nombreux excellents [composants de barre de navigation](https://flowbite.com/docs/components/navbar/) parmi lesquels nous pouvons choisir et positionner le bouton de commutateur de mode sombre à l'intérieur.

Prenons l'exemple de la barre de navigation avec le bouton et changeons-le avec notre propre commutateur de mode sombre :

```html
<nav class="bg-white border-gray-200 px- bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-800">
  <div class="container mx-auto flex flex-wrap items-center justify-between">
  <a href="#" class="flex">
    <svg class="h-10 mr-3" viewBox="0 0 52 72" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1.87695 53H28.7791C41.5357 53 51.877 42.7025 51.877 30H24.9748C12.2182 30 1.87695 40.2975 1.87695 53Z" fill="#76A9FA"></path><path d="M0.000409561 32.1646L0.000409561 66.4111C12.8618 66.4111 23.2881 55.9849 23.2881 43.1235L23.2881 8.87689C10.9966 8.98066 1.39567 19.5573 0.000409561 32.1646Z" fill="#A4CAFE"></path><path d="M50.877 5H23.9748C11.2182 5 0.876953 15.2975 0.876953 28H27.7791C40.5357 28 50.877 17.7025 50.877 5Z" fill="#1C64F2"></path></svg>
      <span class="self-center text-lg font-semibold whitespace-nowrap dark:text-white">FlowBite</span>
  </a>
  <div class="flex md:order-2">
      
      <!-- Commutateur de mode sombre -->
          <button
      id="theme-toggle"
      type="button"
      class="text-gray-500 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-700 rounded-lg text-sm p-2.5"
    >
      <svg
        id="theme-toggle-dark-icon"
        class="w-5 h-5 hidden"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"
        ></path>
      </svg>
      <svg
        id="theme-toggle-light-icon"
        class="w-5 h-5 hidden"
        fill="currentColor"
        viewBox="0 0 20 20"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"
          fill-rule="evenodd"
          clip-rule="evenodd"
        ></path>
      </svg>
    </button>
    <!-- Fin du commutateur de mode sombre -->
      
      <button data-collapse-toggle="mobile-menu-4" type="button" class="md:hidden text-gray-500 hover:bg-gray-100focus:outline-none focus:ring-2 focus:ring-gray-200 rounded-lg text-sm p-2 inline-flex items-center dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="mobile-menu-4" aria-expanded="false">
      <span class="sr-only">Ouvrir le menu principal</span>
      <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
      <svg class="hidden w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
    </button>
  </div>
  <div class="hidden md:flex justify-between items-center w-full md:w-auto md:order-1" id="mobile-menu-4">
    <ul class="flex-col md:flex-row flex md:space-x-8 mt-4 md:mt-0 md:text-sm md:font-medium">
      <li>
        <a href="#" class="bg-blue-700 md:bg-transparent text-white block pl-3 pr-4 py-2 md:text-blue-700 md:p-0 rounded dark:text-white" aria-current="page">Accueil</a>
      </li>
      <li>
        <a href="#" class="text-gray-700 hover:bg-gray-50 border-b border-gray-100 md:hover:bg-transparent md:border-0 block pl-3 pr-4 py-2 md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">À propos</a>
      </li>
      <li>
        <a href="#" class="text-gray-700 hover:bg-gray-50 border-b border-gray-100 md:hover:bg-transparent md:border-0 block pl-3 pr-4 py-2 md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Services</a>
      </li>
      <li>
        <a href="#" class="text-gray-700 hover:bg-gray-50 border-b border-gray-100 md:hover:bg-transparent md:border-0 block pl-3 pr-4 py-2 md:hover:text-blue-700 md:p-0 md:dark:hover:text-white dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Contact</a>
      </li>
    </ul>
  </div>
  </div>
</nav>
```

Le résultat final devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-03-at-11.25.15.png)
_Commutateur de mode sombre (mode clair)_

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-03-at-11.25.43.png)
_Commutateur de mode sombre (mode sombre)_

Maintenant, chaque fois qu'un utilisateur clique sur le bouton, toute la mise en page changera de sombre à clair et vice-versa. C'est tout le code dont vous avez besoin pour créer un commutateur de mode sombre en utilisant Tailwind CSS et Flowbite.

## Composants Flowbite en mode sombre

Dans ce tutoriel, je voudrais également vous montrer certains des composants de Flowbite qui supportent déjà le mode sombre et comment vous pouvez les utiliser dans votre projet Tailwind CSS.

Après la [sortie de Flowbite v1.2](https://flowbite.com/docs/getting-started/changelog/), une fonctionnalité importante a été ajoutée à cette bibliothèque de composants open source : une intégration complète du mode sombre pour tous les composants et plugins.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-30-at-14.18.40.png)
_Flowbite - Composant Tailwind CSS en mode sombre_

Cela peut vous aider énormément lorsqu'il s'agit de construire une interface utilisateur avec Tailwind CSS où vous devez également supporter le mode sombre. Les composants de Flowbite fonctionneront avec le mode sombre dès la sortie de la boîte grâce aux classes `.dark:{*}`.

Un bon exemple serait le [composant modal](https://flowbite.com/docs/components/modal/) qui change complètement d'apparence lors du passage du mode clair au mode sombre :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-30-at-14.21.32.png)
_Flowbite - Modale Tailwind CSS (mode clair)_

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screenshot-2021-11-30-at-14.21.25.png)
_Flowbite - Modale Tailwind CSS (mode sombre)_

J'ai déjà écrit un article sur la façon d'utiliser [Flowbite ici sur freeCodeCamp](https://www.freecodecamp.org/news/tailwind-css-components-flowbite/) et vous pouvez le consulter pour en savoir plus sur la façon d'utiliser les composants de cette bibliothèque.

## Conclusion

J'espère que ce tutoriel vous a aidé dans votre parcours avec Tailwind CSS et Flowbite en ce qui concerne la création d'une version sombre pour votre site web. C'est formidable de voir les projets open source évoluer et rendre le web meilleur.

Faites-moi savoir sur Twitter quel schéma de couleurs vous préférez lors de la navigation sur les sites web : mode sombre ou mode clair ?