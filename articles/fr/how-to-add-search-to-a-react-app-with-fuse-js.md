---
title: Comment ajouter une recherche à une application React avec Fuse.js
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-05-26T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-search-to-a-react-app-with-fuse-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/fusejs-1.jpg
tags:
- name: fuse.js
  slug: fuse-js
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: json
  slug: json
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
- name: search
  slug: search
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment ajouter une recherche à une application React avec Fuse.js
seo_desc: Search is a powerful way help people visiting your site find the content
  that's most important to them. But often it's really challenging to figure out the
  rules and logic to make that happen. In this article, we'll see how can we can use
  fuse.js to ...
---

La recherche est un moyen puissant d'aider les personnes visitant votre site à trouver le contenu qui est le plus important pour elles. Mais souvent, il est vraiment difficile de déterminer les règles et la logique pour y parvenir. Dans cet article, nous verrons comment utiliser fuse.js pour ajouter une recherche à nos applications.

* [Qu'est-ce que fuse.js ?](#heading-quest-ce-que-fusejs)
* [Pourquoi la recherche est-elle importante ?](#heading-pourquoi-la-recherche-est-elle-importante)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Initialisation de notre application](#heading-etape-0-initialisation-de-notre-application)
* [Étape 1 : Installation de Fuse.js](#heading-etape-1-installation-de-fusejs)
* [Étape 2 : Création d'une nouvelle instance de recherche Fuse](#heading-etape-2-creation-dune-nouvelle-instance-de-recherche-fuse)
* [Étape 3 : Configuration de la recherche dynamique basée sur l'entrée utilisateur](#heading-etape-3-configuration-de-la-recherche-dynamique-basee-sur-lentree-utilisateur)

%[https://www.youtube.com/watch?v=GZl-yEz4_qw]

## Qu'est-ce que fuse.js ?

[Fuse.js](https://fusejs.io/) est une bibliothèque JavaScript qui fournit des capacités de recherche floue pour les applications et les sites web. Elle est agréable et facile à utiliser dès la sortie de la boîte, mais inclut également des options de configuration qui vous permettent d'ajuster et de créer des solutions puissantes.

## Pourquoi la recherche est-elle importante ?

Que vous soyez un créateur de contenu ou que vous essayiez de vendre un produit avec votre site web, il est important d'aider vos visiteurs à trouver ce qu'ils cherchent.

Si vous construisez un site web d'e-commerce, vous voulez que quelqu'un puisse facilement trouver vos figurines en vinyle de Bender plutôt que de devoir fouiller tout le catalogue d'abord.

## Que allons-nous construire ?

Nous allons commencer par un exemple de base de Create React App. Il inclura des informations sur les personnages sous forme de données structurées pour l'une de mes émissions préférées, Futurama, qui sont simplement affichées dans une liste HTML.

Avec cette liste, nous allons utiliser fuse.js pour fournir des capacités de recherche côté client, ce qui nous permettra de démontrer la recherche du personnage que nous cherchons par son nom et d'autres détails.

## Étape 0 : Initialisation de notre application

Pour commencer, nous allons avoir besoin de contenu avec lequel travailler. J'ai commencé par construire une liste de personnages de Futurama sous forme de données JSON structurées que j'ai mises dans une liste avec une nouvelle application Create React App.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-demo.jpg)
_Démo de recherche de personnages de Futurama_

Vous remarquerez également que j'ai déjà ajouté une entrée pour notre recherche. Elle n'est pas encore fonctionnelle, mais nous l'utiliserons pour commencer.

Si vous souhaitez commencer au même point, j'ai créé une branche avec mon dépôt de démonstration que vous pouvez cloner localement pour suivre le projet avec moi !

```shell
git clone --single-branch --branch start git@github.com:colbyfayock/my-futurama-characters.git

```

[Branche Git "start"](https://github.com/colbyfayock/my-futurama-characters/tree/start)

Ou [suivez le commit](https://github.com/colbyfayock/my-futurama-characters/commit/20d4e42aaf69e214b63e684e012cd2f8c95d427b).

## Étape 1 : Installation de Fuse.js

La première chose que nous voulons faire est d'ajouter Fuse.js à notre application. Dans votre projet, exécutez :

```shell
yarn add fuse.js
# ou
npm install --save fuse.js

```

Cela enregistrera la dépendance dans notre projet afin que nous puissions l'utiliser dans notre projet.

Ensuite, nous voulons importer la dépendance dans notre application afin de pouvoir commencer à construire avec elle. En haut de votre fichier, dans notre cas `src/App.js` si vous suivez avec moi dans un nouveau projet Create React App, ajoutez :

```js
import Fuse from 'fuse.js';

```

Si vous voulez tester si cela fonctionne, vous pouvez `console.log(Fuse)` et voir notre classe `Fuse` que nous utiliserons pour créer nos capacités de recherche.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/fusejs-class.jpg)
_Classe fuse.js importée_

Et avec cela, nous sommes prêts à commencer !

[Suivez le commit](https://github.com/colbyfayock/my-futurama-characters/commit/54720daffa6ff415997c319b12f8f44d7ec8b748)

## Étape 2 : Création d'une nouvelle instance de recherche Fuse

Pour utiliser Fuse.js, nous voulons d'abord créer une nouvelle instance.

En haut de votre composant, ajoutez :

```js
const fuse = new Fuse(characters, {
  keys: [
    'name',
    'company',
    'species'
  ]
});

```

Ce que cela fait :

* Crée une nouvelle instance de Fuse
* Passe notre tableau d'objets `characters`
* Spécifie les 3 clés dans nos données que nous voulons rechercher

Ensuite, pour effectuer la recherche, nous pouvons ajouter :

```js
const results = fuse.search('bender');

```

Et si nous affichons les résultats dans la console, nous pouvons voir :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/basic-fusejs-search-results.jpg)
_Résultats de recherche de base avec fuse.js_

Vous remarquerez que nous avons plus de résultats que notre ami Bender. Fuse.js fournit une "recherche floue" ce qui signifie qu'il essaie de vous aider au cas où vous ne seriez pas sûr de ce que vous cherchez ou si vous faites une faute de frappe dans votre requête.

Pour avoir une idée de comment cela fonctionne, ajoutons l'option `includeScore` à notre recherche :

```js
const fuse = new Fuse(characters, {
  keys: [
    'name',
    'company',
    'species'
  ],
  includeScore: true
});

```

Maintenant, nous pouvons voir l'attribut `score` dans notre objet de résultats.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/fusejs-search-results-with-score.jpg)
_Résultats de recherche Fuse.js avec score_

Vous remarquerez que notre premier résultat a un score très bas. Avec fuse.js, un score plus bas signifie qu'il est plus proche d'une correspondance exacte.

Un score de 0 indique une correspondance parfaite, tandis qu'un score de 1 indique une non-correspondance complète.

Cela signifie qu'il est extrêmement probable que le premier résultat soit ce que nous cherchons, mais il n'est pas confiant dans les autres.

Ainsi, avec nos résultats, nous voulons les connecter à notre interface utilisateur. Si vous remarquez que notre sortie de tableau est différente de ce que nous mappons pour la liste HTML, créons une nouvelle variable que nous pouvons changer :

```js
const results = fuse.search('bender');
const characterResults = results.map(character => character.item);

```

Ce que cela fait est de créer un nouveau tableau en utilisant la méthode [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) qui n'inclura que la propriété `item` de chaque objet de tableau.

Ensuite, si nous remplaçons notre map `characters` à l'intérieur de notre liste par `characterResults.map` :

```jsx
<ul className="characters">
  {characterResults.map(character => {
    const { name, company, species, thumb } = character;

```

Nous pouvons maintenant voir que notre page n'affiche que les résultats pour "bender" !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-filtered-results.jpg)
_Démo avec résultats filtrés_

[Suivez le commit !](https://github.com/colbyfayock/my-futurama-characters/commit/adbf30a872fa134cfca4e142ba479877b9665e9a)

## Étape 3 : Configuration de la recherche dynamique basée sur l'entrée utilisateur

Maintenant que nous avons une recherche codée en dur qui fonctionne, nous voulons que quelqu'un puisse utiliser l'entrée de recherche pour rechercher !

Pour y parvenir, nous allons utiliser le hook `useState` et écouter les changements du champ `input`, ce qui créera dynamiquement une recherche pour nos données.

Tout d'abord, importez le hook `useState` de React :

```js
import React, { useState } from 'react';

```

Ensuite, utilisons ce hook pour créer une instance d'état :

```js
const [query, updateQuery] = useState('');

```

Ici, nous créons un nouvel état de `query` que nous pouvons mettre à jour avec `updateQuery` qui par défaut est une chaîne vide (`''`).

Avec cela, disons à notre entrée de recherche d'utiliser cette valeur `query` comme sa valeur :

```jsx
<input type="text" value={query} />

```

À ce stade, rien ne devrait être différent, car nous utilisons une requête vide.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-filtered-results.jpg)
_Démo avec résultats filtrés - rien n'a changé_

Maintenant, ajoutons un gestionnaire d'événements à notre entrée que nous pouvons utiliser pour mettre à jour notre état :

```jsx
<input type="text" value={query} onChange={onSearch} />

```

Et nous voulons créer cette fonction pour pouvoir l'utiliser :

```js
function onSearch({ currentTarget }) {
  updateQuery(currentTarget.value);
}

```

Cela mettra à jour notre `query` avec la valeur de l'entrée chaque fois qu'elle change.

Maintenant que notre `query` contiendra ce que nous voulons rechercher, nous pouvons mettre à jour notre instance de recherche :

```js
const results = fuse.search(query);

```

Et maintenant, si vous rechargez la page, elle est vide ! ?

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-no-results.jpg)
_Démo sans résultats_

C'est parce que par défaut, Fuse voit notre requête vide et ne la fait correspondre à rien. Si nous recherchons maintenant quelque chose comme `slurms`, nous pouvons voir notre recherche se mettre à jour dynamiquement avec des résultats !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-results.jpg)
_Démo avec résultats pour "slurms"_

Si nous voulions corriger cela afin que tous nos résultats s'affichent lorsqu'il n'y a pas de requête, nous pouvons le faire avec une instruction `if` ou dans mon exemple, un ternaire, qui affichera tous les personnages s'il n'y a pas de requête :

```js
const characterResults = query ? results.map(character => character.item) : characters;

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-demo.jpg)
_Démo avec tous les résultats_

Et avec cela, nous avons notre recherche de base !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-results-query.jpg)
_Démo avec résultats filtrés pour "zoidberg"_

[Suivez le commit !](https://github.com/colbyfayock/my-futurama-characters/commit/1b8918fc56f31517686a6c73f1969787728736ac)

## Que puis-je faire ensuite ?

### Ajuster votre recherche

Fuse.js vient avec de nombreuses options que vous pouvez utiliser pour ajuster votre recherche comme vous le souhaitez. Vous voulez seulement montrer des résultats fiables ? Utilisez l'option `threshold` ! Vous voulez des requêtes sensibles à la casse ? Utilisez l'option `isCaseSensitive` !

[https://fusejs.io/api/options.html](https://fusejs.io/api/options.html)

### Définir la requête par défaut avec les paramètres d'URL

Parfois, vous voulez que quelqu'un puisse lier à un ensemble particulier de résultats. Pour ce faire, nous pourrions vouloir ajouter un nouveau paramètre d'URL comme `?q=bender`.

Pour que cela fonctionne, vous pouvez récupérer ce paramètre d'URL avec JavaScript et utiliser cette valeur pour définir notre état `query`.

## Rejoignez la conversation !

%[https://twitter.com/colbyfayock/status/1265298322891378688]

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e8f3fb Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>