---
title: Qu'est-ce que Storybook et comment l'utiliser pour créer une bibliothèque de
  composants dans React ?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-09T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-storybook-and-how-can-i-use-it-to-create-a-component-libary-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/storybook.jpg
tags:
- name: components
  slug: components
- name: create-react-app
  slug: create-react-app
- name: Design Tools
  slug: design-tools
- name: Developer Tools
  slug: developer-tools
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Storybook
  slug: storybook
- name: tools
  slug: tools
seo_title: Qu'est-ce que Storybook et comment l'utiliser pour créer une bibliothèque
  de composants dans React ?
seo_desc: "Frameworks like React, Vue, and Angular all help developers create modular\
  \ systems using components, but that doesn't usually include a good way to see them\
  \ all from a higher point of view. \nSo how can we use Storybook to build libraries\
  \ and design s..."
---

Des frameworks comme React, Vue et Angular aident les développeurs à créer des systèmes modulaires utilisant des composants, mais cela n'inclut généralement pas une bonne façon de les voir tous d'un point de vue plus élevé.

Alors, comment pouvons-nous utiliser Storybook pour construire des bibliothèques et des systèmes de conception qui s'auto-documentent pendant que nous les construisons ?

* [Qu'est-ce que Storybook ?](#heading-qu-est-ce-que-storybook)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Initialisation d'une application](#heading-etape-0-initialisation-d-une-application)
* [Étape 1 : Installation de Storybook](#heading-etape-1-installation-de-storybook)
* [Étape 2 : Création d'un nouveau bouton](#heading-etape-2-creation-d-un-nouveau-bouton)
* [Étape 3 : Utilisation de notre nouveau composant Button](#heading-etape-3-utilisation-de-notre-nouveau-composant-button)
* [Répétition : Création d'un nouveau composant Header](#heading-repetition-creation-d-un-nouveau-composant-header)
* [Plus de fonctionnalités de Storybook](#heading-plus-de-fonctionnalites-de-storybook)

%[https://www.youtube.com/watch?v=VApXDsYO5Gg]

## Qu'est-ce que Storybook ?

[Storybook](https://storybook.js.org/) est un outil JavaScript qui permet aux développeurs de créer des systèmes d'interface utilisateur organisés, rendant à la fois le processus de construction et la documentation plus efficaces et plus faciles à utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/loneley-planet-storybook-example.jpg)
_[Backpack UI de Lonely Planet]( https://lonelyplanet.github.io/backpack-ui/?path=/story/cards--card-basic)_

Une fois que vous avez construit un composant, Storybook vous permet de créer un fichier "story" où vous pouvez importer votre composant et créer divers exemples de cas d'utilisation dans un bac à sable iFramé utilisant ce composant.

Cela fournit un environnement organisé et ciblé pour construire de nouveaux composants et travailler sur des composants existants.

## Que allons-nous construire ?

Nous allons initialiser une nouvelle application [React JS](https://reactjs.org/) en utilisant [Create React App](https://reactjs.org/docs/create-a-new-react-app.html).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-component-example.jpg)

Dans cette application, nous allons installer Storybook et créer quelques nouveaux composants qui nous aideront à apprendre comment créer de nouveaux composants sur lesquels nous pouvons travailler dans une story et ensuite les utiliser dans une application React.

## Étape 0 : Initialisation d'une application

Pour commencer, nous allons partir de zéro avec [Create React App](https://reactjs.org/docs/create-a-new-react-app.html). Cela nous aidera à nous concentrer sur la productivité dans Storybook plutôt que de passer par l'intégration dans une application actuelle.

Cela dit, si vous travaillez déjà avec une application créée avec Create React App qui n'est pas éjectée, vous devriez pouvoir suivre la partie 1 et au-delà de la même manière !

Alors, commençons par naviguer vers l'endroit où nous voulons créer notre nouvelle application et exécutons la commande Create React App :

```shell
npx create-react-app my-storybook

```

_Note : n'hésitez pas à remplacer `my-storybook` par le nom de répertoire de votre choix._

![Image](https://www.freecodecamp.org/news/content/images/2020/06/create-new-react-app.jpg)
_Initialisation avec Create React App_

Une fois que cela a fini de s'exécuter, vous pouvez naviguer vers le répertoire :

```shell
cd my-storybook

```

Et nous sommes prêts à partir !

## Étape 1 : Installation de Storybook

Storybook facilite heureusement le démarrage avec une installation standard de React. En particulier avec Create React App, Storybook détecte automatiquement que nous utilisons une application créée avec CRA et installe les dépendances et échafaudages pour nous.

### Initialisation de Storybook

Pour commencer l'installation de Storybook, exécutez :

```shell
npx -p @storybook/cli sb init

```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/initializing-storybook.jpg)
_Initialisation de Storybook dans une application React_

Si vous n'utilisez pas Create React App ou si cela n'a pas fonctionné, vous pouvez consulter leurs [guides disponibles dans leur documentation](https://storybook.js.org/docs/guides/guide-react/).

Après cela, toutes nos dépendances Storybook devraient être installées.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-finished-installing.jpg)
_Installation de Storybook terminée_

### Démarrage de Storybook

Nous sommes maintenant prêts à avancer ! Enfin, exécutez :

```shell
yarn storybook
# ou
npm run storybook

```

Et une fois que tout a fini de charger, Storybook ouvrira un nouvel onglet dans votre navigateur et vous devriez maintenant voir un message de bienvenue à l'intérieur de votre nouveau tableau de bord Storybook !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-welcome-page.jpg)
_Page de bienvenue de Storybook_

[Suivez avec le commit !](https://github.com/colbyfayock/my-storybook/commit/3e994096384e31cb540150c9f14f41758ef3a746)

## Étape 2 : Création d'un nouveau bouton

Si vous avez pris un moment pour explorer le tableau de bord, vous avez peut-être remarqué qu'il est préchargé avec un bouton disponible en démonstration.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-demo-button.jpg)
_Bouton de démonstration de Storybook_

Vous devriez également remarquer que si vous cliquez sur le bouton, vous voyez en réalité une action imprimée à l'intérieur de l'onglet Actions en bas. Cela montre l'événement capturé à partir du clic sur le bouton.

C'est simple, mais c'est bien pour avoir une bonne idée de ce à quoi s'attendre dans Storybook. Le seul problème est que cela est purement à des fins de démonstration, alors créons notre propre bouton pour le remplacer.

### Création d'un nouveau composant Button

Pour commencer, créons d'abord quelques répertoires :

* Sous `src`, créez un nouveau dossier appelé `components`
* Sous `components`, créez un nouveau dossier appelé `Button`

Une fois que vous avez créé ces dossiers, créez un nouveau fichier appelé `index.js` à l'intérieur de votre dossier `src/components/Button` et ajoutez-y :

```js
// À l'intérieur de src/components/Button/index.js

export { default } from './Button';

```

Cela importera le fichier suivant que nous avons créé appelé `Button.js`, ce qui nous permettra d'importer plus facilement nos fichiers avec `src/components/Button` au lieu de `/src/components/Button/Button`.

Ensuite, créons `Button.js` à côté de notre fichier `index.js` avec le contenu suivant :

```js
// À l'intérieur de src/components/Button/Button.js

import React from 'react';

const Button = ({ children, ...rest }) => {
  return (
    <button className="button" {...rest}>
      { children }
    </button>
  )
}

export default Button;

```

Ici, nous créons un nouveau composant appelé Button qui ajoute une classe `button` à l'élément et transmet les `children`. Nous déstructurons également le reste des props dans la variable `rest` et étalons cette valeur dans l'élément `<button>`.

Si vous avez suivi, vos fichiers devraient maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/button-reaect-component.jpg)
_Composant Button dans React_

### Utilisation de notre nouveau composant Button

Maintenant que nous avons notre composant Button, utilisons-le !

Ouvrez le fichier `src/stories/1-Button.stories.js` et remplacez la ligne qui importe `Button` par :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/updating-button-storybook-story.jpg)
_Mise à jour de la story Button Storybook_

Et une fois que vous avez enregistré, vous pouvez rouvrir votre onglet de navigateur avec votre tableau de bord Storybook, et vous pouvez maintenant voir un bouton qui ressemble principalement à l'original, mais il utilise les styles par défaut du navigateur pour l'élément `<button>`. Vous remarquerez même que si vous cliquez dessus, l'événement sera toujours enregistré sous l'onglet Actions.

### Stylisation de notre composant Button

Enfin, nous ne voulons probablement pas utiliser les styles par défaut du navigateur, alors rendons-le plus joli.

Dans notre répertoire `src/components/Button`, ajoutez un nouveau fichier `Button.css` et ajoutez le contenu suivant :

```css
/* À l'intérieur de src/components/Button/Button.css */

.button {
  color: white;
  font-weight: bold;
  background-color: blueviolet;
  border: none;
  padding: .8em 1em;
  border-radius: .2rem;
}

```

Cela applique quelques styles à notre classe `.button` comme ajouter une couleur de fond et changer la couleur de la police en blanc.

Mais si vous ouvrez Storybook, vous remarquerez qu'il ne s'est rien passé. Pour l'utiliser, nous devons l'importer dans notre composant.

À l'intérieur de `src/components/Button/Button.js`, ajoutez ce qui suit en haut sous l'import de React :

```js
import './Button.css';

```

Et une fois que vous avez enregistré cela et ouvert votre navigateur, vous devriez maintenant voir notre nouveau bouton avec nos styles mis à jour !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-button-storybook.jpg)
_Nouveau bouton dans Storybook_

[Suivez avec le commit !](https://github.com/colbyfayock/my-storybook/commit/e71e0e9e666adee0455b0b69118053c2f551ab68)

## Étape 3 : Utilisation de notre nouveau composant Button

Le but ultime de notre composant est de l'utiliser, n'est-ce pas ? Alors ajoutons-le à notre application.

### Passage à l'application React

Tout d'abord, nous devons soit démarrer notre application React dans un nouvel onglet de terminal, soit arrêter le processus Storybook et démarrer le processus React là. Pour démarrer l'application React en utilisant Create React App, exécutez :

```shell
yarn start
# ou
npm run start

```

Une fois que cela est chargé, nous devrions avoir notre application Create React App standard si vous me suivez :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-create-react-app.jpg)
_Nouvelle application Create React App_

### Importation et utilisation du nouveau bouton

Ensuite, à l'intérieur de `src/App.js`, importons notre nouveau Button en haut de la page :

```js
import Button from './components/Button';

```

Avec Button importé, nous pouvons l'utiliser. Ici, nous pouvons simplement l'ajouter n'importe où nous voulons dans la page. Je vais remplacer le lien Learn React par :

```jsx
<p>
  <Button>Bonjour, Storybook !</Button>
</p>

```

Et si nous enregistrons et rechargeons la page, nous devrions maintenant voir notre Button sur la page !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/create-react-app-with-new-button.jpg)
_Nouveau bouton dans Create React App_

[Suivez avec le commit](https://github.com/colbyfayock/my-storybook/commit/e6071aae5be281101d486c4cc7664bf6cacb4028)

## Répétition : Création d'un nouveau composant Header

La chose géniale avec Storybook et React (ou n'importe quel framework supporté) est que ce processus s'adapte à autant de composants que vous le souhaitez.

Alors, construisons un autre composant !

### Création de notre composant Header

Similaire à notre Button, commençons par créer l'ensemble des répertoires et fichiers qui nous donnent notre composant.

Puisque nous l'avons déjà fait une fois, je vais fournir le code sans expliquer ce qui se passe.

Commençons par relancer notre serveur Storybook avec :

```
yarn storybook
# ou 
npm run storybook

```

Créez un répertoire `Header` à l'intérieur du répertoire `src/components`.

Créez un fichier `index.js` à l'intérieur de `src/components/Header` avec le contenu suivant :

```js
// Dans src/components/Header/index.js

export { default } from './Header';

```

Créez un fichier `Header.js` à l'intérieur de `src/components/Header` avec le contenu suivant :

```jsx
// Dans src/components/Header/Header.js

import React from 'react';
import './Header.css';

const Header = ({ children }) => {
  return (
    <h2 className="header">
      { children }
    </h2>
  )
}

export default Header;

```

Créez un fichier `Header.css` à l'intérieur de `src/components/Header` avec le contenu suivant :

```css
/* Dans src/components/Header/Header.css */

.header {
  font-family: sans-serif;
  font-size: 2.5em;
  color: blueviolet;
  border-bottom: solid 5px aqua;
  padding-bottom: .2em;
  box-shadow: 0 5px 0 blueviolet;
}

```

Maintenant, si vous remarquez, si vous essayez d'ouvrir Storybook, encore une fois, rien ne se passera. Cette fois, nous devons créer un nouveau fichier story.

### Création d'un nouveau fichier Story

À l'intérieur de `src/stories`, ajoutez un nouveau fichier appelé `2-Header.stories.js` :

```jsx
// À l'intérieur de src/stories/2-Header.stories.js

import React from 'react';

import Header from '../components/Header';

export default {
  title: 'Header',
  component: Header,
};

export const Text = () => <Header>Bonjour Header</Header>;

```

Voici une explication de notre fichier story :

* Tout d'abord, nous importons notre composant – c'est assez standard chaque fois que nous voulons l'utiliser
* La première chose que nous exportons est un objet `default`. Avec Storybook, il s'attend à ce que l'export par défaut soit la configuration de notre story, donc ici nous lui fournissons un titre et nous passons le composant que nous utilisons pour cette story
* La deuxième et dernière chose que nous exportons est la constante `Text`. Avec Storybook, toute exportation non par défaut sera considérée comme une variation qui sera imbriquée sous le titre que vous fournissez dans l'export par défaut

Et si vous enregistrez ce fichier et ouvrez votre tableau de bord Storybook dans le navigateur, vous devriez maintenant voir le nouvel en-tête !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/new-header-storybook-story.jpg)
_Nouveau composant Header dans Storybook_

### Utilisation du composant Header

L'utilisation de notre composant est exactement la même que celle de notre composant Button, alors à l'intérieur de `src/App.js`, ajoutons notre Header.

Après avoir démarré votre serveur React, importez d'abord notre nouveau Header :

```js
// Dans src/App.js

import Header from './components/Header';

```

Ensuite, ajoutez-le en haut de la page :

```jsx
// Dans src/App.js

<Header>Mon Application</Header>

```

Et si vous ouvrez la page, nous verrons notre nouvel en-tête !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/create-react-app-with-header-and-button.jpg)
_Create React App avec les nouveaux composants Header et Button_

[Suivez avec le commit !](https://github.com/colbyfayock/my-storybook/commit/e1c59eccaf5f4146a2fe039dca8874609d615194)

## Ajout de plus de composants

Comme vous l'avez remarqué avec notre deuxième étape de répétition – l'ajout d'un nouveau composant est à peu près le même processus pour tout type de composant que nous voulons ajouter. Une fois que nous l'avons dans notre bibliothèque, nous pouvons le développer dans un environnement ciblé et ensuite l'importer dans notre application pour l'utiliser.

Vous pouvez maintenant utiliser cela pour gérer votre bibliothèque de composants et mieux maintenir un système entier pour votre projet !

## Plus de fonctionnalités de Storybook

Storybook ne s'arrête pas à l'ajout de composants, il offre la possibilité de configurer des [Addons](https://storybook.js.org/addons/) qui améliorent les capacités de base, ouvrant ainsi de nombreuses possibilités.

Voici quelques-uns de mes préférés...

### Story Source

Lors de la construction d'un système de composants, l'espoir est que les gens puissent facilement utiliser ces composants. Mais si vous n'avez pas de documentation, quelqu'un devrait ouvrir le fichier ou essayer de trouver un autre exemple d'utilisation.

Au lieu de cela, [Story Source](https://github.com/storybookjs/storybook/tree/master/addons/storysource) montre la source du code du fichier story que vous avez créé, permettant à quelqu'un parcourant votre tableau de bord Storybook d'obtenir un exemple directement avec la sortie du composant !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-source-demo.gif)
_Démonstration de Storybook Story Source_

### Storyshots

Si vous êtes un fan de tests automatisés, vous avez peut-être entendu parler de l'utilisation de [Jest](https://jestjs.io/) ou d'un autre outil pour ajouter des tests de snapshot à votre application.

[StoryShots](https://github.com/storybookjs/storybook/tree/master/addons/storyshots/storyshots-core) est un moyen d'ajouter facilement des tests de snapshot Jest à votre système de composants. Il crée des snapshots basés sur les stories que vous créez afin que vous puissiez vous assurer que vos composants ne changent pas fondamentalement (ou ne se cassent pas) pendant le développement.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/storybook-snapshot-example.jpg)
_Exemple de snapshot avec StoryShots_

## Quelle est votre partie préférée de Storybook ?

[Partagez avec moi sur Twitter !](https://twitter.com/colbyfayock)

## Continuez la conversation !

%[https://twitter.com/colbyfayock/status/1270392710260719616]

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f3ac Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e9f3fb Inscrivez-vous à ma newsletter</a>
    </li>
  </ul>
</div>