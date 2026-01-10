---
title: 'JSX de React vs modèles de Vue : un duel sur le front-end'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-18T16:43:18.000Z'
originalURL: https://freecodecamp.org/news/reacts-jsx-vs-vue-s-templates-a-showdown-on-the-front-end-b00a70470409
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QH4RGlNwXUFnJSytytvb6A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: 'JSX de React vs modèles de Vue : un duel sur le front-end'
seo_desc: 'By Cristian Vega

  React.js and Vue.js are two of the most popular JavaScript libraries on the planet.
  They''re both powerful and relatively easy to pick up and use.

  Both React and Vue:


  use a virtual DOM

  provide reactive view components

  maintain a focu...'
---

Par Cristian Vega

React.js et Vue.js sont deux des bibliothèques JavaScript les plus populaires au monde. Elles sont toutes deux puissantes et relativement faciles à apprendre et à utiliser.

React et Vue :

* utilisent un DOM virtuel
* fournissent des composants de vue réactifs
* maintiennent un focus sur un aspect du développement. Dans ce cas, la vue.

Avec autant de similitudes, vous pourriez penser qu'elles sont deux versions différentes d'une même chose.

Eh bien, il y a une différence majeure entre ces deux bibliothèques : la manière dont elles vous permettent, en tant que développeur, de créer vos composants de vue, et par conséquent, votre application.

React utilise JSX, un terme inventé par l'équipe React, pour rendre le contenu sur le DOM. Alors, qu'est-ce que JSX ? Basiquement, JSX est une fonction de rendu JavaScript qui vous aide à insérer votre HTML directement dans votre code JavaScript.

Vue adopte une approche différente et utilise des modèles similaires à HTML. Utiliser des modèles Vue revient à utiliser JSX en ce sens qu'ils sont tous deux créés en utilisant JavaScript. La principale différence est que les fonctions JSX ne sont jamais utilisées dans le fichier HTML réel, tandis que les modèles Vue le sont.

### **JSX de React**

Examinons plus en détail comment fonctionne JSX. Supposons que vous avez une liste de noms que vous souhaitez afficher sur le DOM. Une liste de nouvelles recrues que votre entreprise a récemment embauchées.

Si vous utilisiez du HTML simple, vous devriez d'abord créer un fichier index.html. Ensuite, vous ajouteriez les lignes de code suivantes.

```html
<ul>
  <li> John </li>
  <li> Sarah </li>
  <li> Kevin </li>
  <li> Alice </li>
<ul>
```

Rien de spectaculaire ici, juste du code HTML simple.

Alors, comment feriez-vous la même chose en utilisant JSX ? La première étape serait de créer un autre fichier index.html. Mais au lieu d'ajouter le HTML complet comme vous l'avez fait auparavant, vous n'ajouterez qu'un simple élément `div`. Cet élément `div` sera le conteneur où tout votre code React sera rendu.

Le `div` devra avoir un ID unique pour que React sache où le trouver. Facebook tend à favoriser le mot-clé root, alors restons avec cela.

```
<div id=root></div>
```

Maintenant, passons à l'étape la plus importante. Créer le fichier JavaScript qui contiendra tout le code React. Appelez celui-ci app.js.

Maintenant que tout cela est prêt, passons à l'événement principal. Afficher toutes les nouvelles recrues sur le DOM en utilisant JSX.

Vous devriez d'abord créer un tableau avec les noms des nouvelles recrues.

```
const names = ['John', 'Sarah', 'Kevin', 'Alice'];
```

À partir de là, vous devriez créer un élément React qui rendra dynamiquement la liste entière des noms. Cela sans que vous ayez à afficher manuellement chacun d'eux.

```js
const displayNewHires = (
  <ul>
    {names.map(name => <li>{name}</li> )}
  </ul>
);
```

Le point clé à noter ici est que vous n'avez pas à créer des éléments `<li>` individuels. Vous n'avez besoin de décrire comment vous voulez qu'ils apparaissent qu'une seule fois et React s'occupera du reste. C'est assez puissant. Bien que vous n'ayez que quelques noms, imaginez avoir une liste de centaines de milliers ! Vous pouvez voir comment cela serait une approche bien meilleure. Surtout si les éléments `<li>` sont plus complexes que ceux utilisés ici.

Le dernier morceau de code nécessaire pour rendre le contenu à l'écran est la fonction principale ReactDom render.

```js
ReactDOM.render(
  displayNewHires,
  document.getElementById('root')
);
```

Ici, vous dites à React de rendre le contenu de `displayNewHires` à l'intérieur du `div` avec un élément root.

Voici à quoi votre code React final devrait ressembler :

```js
const names = ['John', 'Sarah', 'Kevin', 'Alice'];
const displayNewHires = (
  <ul>
    {names.map(name => <li>{name}</li> )}
  </ul>
);
ReactDOM.render(
  displayNewHires,
  document.getElementById('root')
);
```

Une chose importante à garder à l'esprit ici est que tout ceci est du code React. Cela signifie qu'il sera tout compilé en JavaScript classique. Voici à quoi cela ressemblerait finalement :

```js
'use strict';
var names = ['John', 'Sarah', 'Kevin', 'Alice'];
var displayNewHires = React.createElement(
  'ul',
  null,
  names.map(function (name) {
    return React.createElement(
      'li',
      null,
      name
    );
  })
);
ReactDOM.render(displayNewHires, document.getElementById('root'));
```

C'est tout. Vous avez maintenant une application React simple qui affichera une liste de noms. Rien d'extraordinaire, mais cela devrait vous donner un aperçu de ce dont React est capable.

### **Modèles Vue.js**

En gardant l'exemple précédent, vous allez à nouveau créer une application simple qui affichera une liste de noms sur le navigateur.

La première chose que vous devez faire est de créer un autre fichier index.html vide. À l'intérieur de ce fichier, vous allez ensuite créer un autre `div` vide avec un id de root. Gardez à l'esprit cependant, que root n'est qu'une préférence personnelle. Vous pouvez appeler l'id comme vous le souhaitez. Vous devez simplement vous assurer qu'il correspond plus tard lorsque vous synchronisez le html avec votre code JavaScript.

Ce div fonctionnera comme dans React. Il indiquera à la bibliothèque JavaScript, dans ce cas Vue, où chercher dans le DOM lorsqu'elle voudra commencer à faire des changements.

Une fois cela fait, vous allez créer un fichier JavaScript qui contiendra tout le code Vue. Appelez-le app.js, pour rester cohérent.

Maintenant que vos fichiers sont prêts, voyons comment Vue affiche les éléments sur le navigateur.

Vue utilise une approche de type modèle lorsqu'il s'agit de manipuler le DOM. Cela signifie que votre fichier HTML ne contiendra pas seulement un `div` vide, comme dans React. Vous allez en fait écrire une bonne partie de votre code dans votre fichier HTML.

Pour vous donner une meilleure idée, rappelez-vous ce qu'il faut pour créer une liste de noms en utilisant du HTML simple. Un élément `<ul>` avec quelques éléments `<li>` à l'intérieur. Dans Vue, vous allez faire presque la même chose, avec seulement quelques changements ajoutés.

Créez un élément `<ul>`.

```html
<ul>
</ul>
```

Ajoutez maintenant un élément `<li>` vide à l'intérieur de l'élément `<ul>`.

```html
<ul>
  <li>
  </li>
</ul>
```

Rien de nouveau pour l'instant. Changez cela en ajoutant une directive, un attribut personnalisé Vue, à votre élément `<li>`.

```html
<ul>
  <li v-for='name in listOfNames'>
  </li>
</ul>
```

Une directive est la manière de Vue d'ajouter des fonctionnalités JavaScript directement dans le HTML. Elles commencent toutes par v- et sont suivies de noms descriptifs qui vous donnent une idée de ce qu'elles font. Dans ce cas, il s'agit d'une boucle for. Pour chaque nom dans votre liste de noms, `listOfNames`, vous voulez copier cet élément `<li>` et le remplacer par un nouvel élément `<li>` avec un nom de votre liste.

Maintenant, le code n'a besoin que d'une dernière touche. Actuellement, il affichera un élément `<li>` pour chaque nom dans votre liste, mais vous ne lui avez pas réellement dit d'afficher le nom réel sur le navigateur. Pour corriger cela, vous allez insérer une syntaxe de type moustache à l'intérieur de votre élément `<li>`. Quelque chose que vous avez peut-être vu dans d'autres bibliothèques JavaScript.

```html
<ul>
  <li v-for='name in listOfNames'>
    {{name}}
  </li>
</ul>
```

Maintenant, l'élément `<li>` est complet. Il affichera maintenant chaque élément à l'intérieur d'une liste appelée listOfNames. Gardez à l'esprit que le mot name est arbitraire. Vous auriez pu l'appeler item et cela aurait servi le même but. Tout ce que le mot-clé fait est servir de placeholder qui sera utilisé pour itérer sur la liste.

La dernière chose que vous devez faire est de créer l'ensemble de données et d'initialiser réellement Vue dans votre application.

Pour ce faire, vous devrez créer une nouvelle instance Vue. Instanciez-la en l'assignant à une variable appelée app.

```
let app = new Vue({
});
```

Maintenant, l'objet va prendre quelques paramètres. Le premier étant le plus important, le paramètre `el` (element) qui indique à Vue où commencer à ajouter des choses au DOM. Tout comme vous l'avez fait avec votre exemple React.

```js
let app = new Vue({
  el:'#root',
});
```

L'étape finale est d'ajouter les données à l'application Vue. Dans Vue, toutes les données passées dans l'application seront faites en tant que paramètre de l'instance Vue. De plus, chaque instance Vue ne peut avoir qu'un seul paramètre de chaque type. Bien qu'il y en ait assez, vous n'avez besoin de vous concentrer que sur deux pour cet exemple, `el` et `data`.

```js
let app = new Vue({
  el:'#root',
  data: {
    listOfNames: ['Kevin', 'John', 'Sarah', 'Alice']
  }
});
```

L'objet data acceptera un tableau appelé `listOfNames`. Maintenant, chaque fois que vous voulez utiliser cet ensemble de données dans votre application, vous n'avez besoin de l'appeler qu'en utilisant une directive. Simple, non ?

Voici l'application finale :

#### **HTML**

```html
<div id="root">
  <ul>
    <li v-for='name in listOfNames'>
      {{name}}
    </li>
  </ul>
</div>
```

#### **JavaScript**

```js
new Vue({
  el:"#root",
  data: {
    listOfNames: ['Kevin', 'John', 'Sarah', 'Alice']
  }
});
```

### **Conclusion**

Vous savez maintenant comment créer deux applications simples en utilisant React et Vue. Elles offrent toutes deux une quantité robuste de fonctionnalités, bien que Vue tende à être plus facile à utiliser. De plus, gardez à l'esprit que Vue permet l'utilisation de JSX, bien que ce ne soit pas la méthode préférée de mise en œuvre.

Dans tous les cas, ce sont deux bibliothèques puissantes et vous ne pouvez pas vous tromper en utilisant l'une ou l'autre.

Si vous voulez en savoir plus sur le développement web, consultez mon site à l'adresse [juanmvega.com](https://juanmvega.com) pour des vidéos et des articles sur les dernières normes et frameworks JavaScript !