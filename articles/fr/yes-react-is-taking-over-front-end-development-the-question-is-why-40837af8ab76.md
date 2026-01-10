---
title: Oui, React domine le développement front-end. La question est pourquoi.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-30T23:20:42.000Z'
originalURL: https://freecodecamp.org/news/yes-react-is-taking-over-front-end-development-the-question-is-why-40837af8ab76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3IUcek7o2S5aJnFAgtP5Gg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Oui, React domine le développement front-end. La question est pourquoi.
seo_desc: 'By Samer Buna


  Update: This article is now part of my book “React.js Beyond The Basics”.

  Read the updated version of this content and more about React at jscomplete.com/react-beyond-basics.


  Here are a few reasons why React has become so popular so q...'
---

Par Samer Buna

> **Mise à jour :** Cet article fait maintenant partie de mon livre « React.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur React sur [**_jscomplete.com/react-beyond-basics_**](https://jscomplete.com/g/why-react)_._

Voici quelques raisons pour lesquelles React est devenu si populaire si rapidement :

* Travailler avec l'API DOM est difficile. React donne essentiellement aux développeurs la capacité de travailler avec un navigateur virtuel qui est plus convivial que le navigateur réel. Le navigateur virtuel de React agit comme un agent entre le développeur et le navigateur réel.
* React permet aux développeurs de décrire de manière déclarative leurs interfaces utilisateur et de modéliser l'état de ces interfaces. Cela signifie qu'au lieu de trouver des étapes pour décrire les transactions sur les interfaces, les développeurs décrivent simplement les interfaces en termes d'état final (comme une fonction). Lorsque des transactions se produisent sur cet état, React se charge de mettre à jour les interfaces utilisateur en fonction de celui-ci.
* React n'est que du JavaScript, il y a une très petite API à apprendre, juste quelques fonctions et comment les utiliser. Après cela, vos compétences en JavaScript sont ce qui fait de vous un meilleur développeur React. Il n'y a pas de barrières à l'entrée. Un développeur JavaScript peut devenir un développeur React productif en quelques heures.

Mais il y a bien plus que cela. Essayons de couvrir toutes les raisons derrière la popularité croissante de React. L'une des raisons est son Virtual DOM (l'algorithme de réconciliation de React). Nous allons travailler sur un exemple pour montrer la valeur pratique réelle de disposer d'un tel algorithme à votre commande.

La définition officielle de React indique qu'il s'agit d'une _bibliothèque JavaScript pour construire des interfaces utilisateur_. Il est important de comprendre les deux parties différentes de cette définition :

1. React est une _bibliothèque JavaScript_. Ce n'est pas un framework. Ce n'est pas une solution complète et nous aurons souvent besoin d'utiliser plus de bibliothèques avec React pour former une solution quelconque. React ne suppose rien sur les autres parties dans une solution complète. Il se concentre sur une seule chose, et sur le fait de bien faire cette chose.
2. La chose que React fait vraiment bien est la deuxième partie de la définition : _construire des interfaces utilisateur_. Une interface utilisateur est tout ce que nous mettons devant les utilisateurs pour qu'ils interagissent avec une machine. Les interfaces utilisateur sont partout, des simples boutons d'un micro-ondes au tableau de bord d'une navette spatiale. Si le dispositif avec lequel nous essayons d'interagir peut comprendre JavaScript, nous pouvons utiliser React pour décrire une interface utilisateur pour celui-ci.

Puisque les navigateurs Web comprennent JavaScript, nous pouvons utiliser React pour décrire les interfaces utilisateur Web. J'aime utiliser le mot _décrire_ ici parce que c'est ce que _nous_ faisons essentiellement avec React, nous lui disons simplement ce que nous voulons et React construira les interfaces utilisateur réelles, en notre nom, dans le navigateur Web. Sans React ou des bibliothèques similaires, nous devrions construire manuellement les interfaces utilisateur avec les API Web natives et JavaScript.

Lorsque vous entendez l'énoncé que « React est déclaratif », c'est exactement ce que cela signifie, nous décrivons les interfaces utilisateur avec React et lui disons ce que nous voulons (pas comment le faire). React se chargera du « comment » et traduira nos descriptions déclaratives (que nous écrivons dans le langage React) en interfaces utilisateur réelles dans le navigateur. React partage ce simple pouvoir déclaratif avec HTML lui-même, mais avec React, nous pouvons être déclaratifs pour les interfaces HTML qui représentent des données dynamiques, pas seulement des données statiques.

React a trois concepts de design principaux qui alimentent sa popularité :

#### 1 — L'utilisation de composants réutilisables, composables et étatiques

Dans React, nous décrivons les interfaces utilisateur en utilisant des composants. Vous pouvez penser aux composants comme à des fonctions simples (dans n'importe quel langage de programmation). Nous appelons des fonctions avec une certaine entrée et elles nous donnent une certaine sortie. Nous pouvons réutiliser des fonctions selon les besoins et composer des fonctions plus grandes à partir de plus petites.

Les composants sont exactement les mêmes ; nous appelons leur entrée « propriétés » et « état », et la sortie d'un composant est une description d'une interface utilisateur (qui est similaire au HTML pour les navigateurs). Nous pouvons réutiliser un seul composant dans plusieurs interfaces utilisateur, et les composants peuvent contenir d'autres composants.

Contrairement aux fonctions pures cependant, un composant React complet peut avoir un état privé pour contenir des données qui peuvent changer avec le temps.

#### 2 — La nature des mises à jour réactives

Le nom de React est l'explication simple de ce concept. Lorsque l'état d'un composant (l'entrée) change, l'interface utilisateur qu'il représente (la sortie) change également. Ce changement dans la description de l'interface utilisateur doit être reflété dans le dispositif avec lequel nous travaillons.

Dans un navigateur, nous devons régénérer les vues HTML dans le Document Object Model (DOM). Avec React, nous n'avons pas besoin de nous soucier de _comment_ refléter ces changements, ou même de gérer _quand_ apporter les changements au navigateur ; React va simplement _réagir_ aux changements d'état et mettre à jour automatiquement le DOM lorsque nécessaire.

#### 3 — La représentation virtuelle des vues en mémoire

Avec React, nous écrivons du HTML en utilisant JavaScript. Nous nous appuyons sur la puissance de JavaScript pour générer du HTML qui dépend de certaines données, plutôt que d'améliorer le HTML pour qu'il fonctionne avec ces données. L'amélioration du HTML est ce que font habituellement les autres frameworks JavaScript. Par exemple, Angular étend le HTML avec des fonctionnalités comme les boucles, les conditionnelles, et autres.

Lorsque nous recevons simplement les données du serveur (en arrière-plan, avec AJAX), nous avons besoin de quelque chose de plus que le HTML pour travailler avec ces données. C'est soit utiliser un HTML amélioré, soit utiliser la puissance de JavaScript lui-même pour générer le HTML. Les deux approches ont des avantages et des inconvénients. React adopte cette dernière, avec l'argument que les avantages sont plus forts que les inconvénients.

En fait, il y a un avantage majeur qui peut faire pencher la balance pour cette approche à lui seul ; utiliser JavaScript pour rendre le HTML facilite pour React le maintien d'une représentation virtuelle du HTML en mémoire (qui est communément connue sous le nom de _The Virtual DOM_). React utilise le Virtual DOM pour rendre un arbre HTML virtuellement d'abord, et ensuite, chaque fois qu'un état change et que nous obtenons un nouvel arbre HTML qui doit être pris dans le DOM du navigateur, au lieu d'écrire tout le nouvel arbre, React n'écrira que la différence entre le nouvel arbre et l'arbre précédent (puisque React a les deux arbres en mémoire). Ce processus est connu sous le nom de _Tree Reconciliation_, et je pense que c'est la meilleure chose qui soit arrivée dans le développement Web depuis AJAX !

Dans l'exemple suivant, nous allons nous concentrer sur ce dernier concept et voir un exemple pratique simple du processus de réconciliation d'arbre et la grande différence qu'il fait. Nous allons écrire le même exemple HTML deux fois, d'abord en utilisant les API Web natives et JavaScript vanilla, puis nous verrons comment décrire le même arbre HTML avec React.

Pour nous concentrer purement sur ce dernier concept, nous n'utiliserons pas de composants, et nous simulerons une opération de changement d'état en utilisant un minuteur JavaScript. Nous n'allons pas non plus utiliser JSX, bien que l'utilisation de JSX rendrait le code beaucoup plus simple. J'utilise JSX tout le temps lorsque j'écris React, mais travailler directement avec l'API React dans cet exemple vous aidera, je l'espère, à mieux comprendre ce concept.

#### Exemple de l'algorithme de réconciliation de React

Pour suivre cet exemple, vous avez besoin d'un navigateur et d'un éditeur de code. Vous pouvez en fait utiliser un terrain de jeu de codage en ligne, mais j'utiliserai des fichiers locaux et les testerai directement dans un navigateur (nous n'avons pas besoin d'un serveur web) :

Nous allons commencer cet exemple à partir de zéro. Créez un nouveau répertoire, et lancez votre éditeur préféré là :

```
mkdir react-democd react-demoatom .
```

Créez un fichier `index.html` dans ce répertoire, et mettez un modèle HTML standard dedans. Incluez dans ce modèle un fichier `script.js` et mettez une instruction `console.log` dans ce script pour tester que l'inclusion fonctionne :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>React Demo</title>
  </head>
  <body>
    <script src="script.js"></script>
  </body>
</html>
```

Ouvrez le fichier `index.html` dans votre navigateur et assurez-vous de pouvoir voir le modèle vide sans problèmes, et que vous pouvez voir dans l'onglet Console des outils de développement le message de test `console.log` que vous avez mis dans `script.js` :

```
open index.html # Sur Mac
explorer index.html # Sur Windows
```

Maintenant, apportons la bibliothèque React elle-même, que nous pouvons inclure depuis le [site web de Reactjs](https://facebook.github.io/react/docs/installation.html). Copiez les scripts `react` et `react-dom`, et incluez-les dans `index.html` :

```html
<script src="https://unpkg.com/react@15/dist/react.js"></script> <script src="https://unpkg.com/react-dom@15/dist/react-dom.js"></script>
```

Nous incluons ici deux scripts différents pour une raison importante : La bibliothèque `React` elle-même peut être utilisée sans navigateur. Pour utiliser React avec un navigateur, nous avons besoin de la bibliothèque `ReactDOM`.

Lorsque nous actualisons le navigateur maintenant, nous devrions voir `React` et `ReactDOM` disponibles dans la portée globale :

![Image](https://cdn-media-1.freecodecamp.org/images/1*g5-fvPYO0bTelGckK9RWzA.png)
_Image capturée dans Chrome_

Avec cette configuration simple, nous pouvons maintenant accéder aux API `React` et `ReactDOM`, et bien sûr, nous avons également accès aux API Web natives et à JavaScript que nous allons utiliser en premier.

Pour insérer du HTML dynamiquement dans le navigateur, nous pouvons simplement utiliser du JavaScript pur et l'API Web DOM elle-même. Créons un élément `div` pour héberger notre contenu HTML JavaScript et donnons-lui l'id `"js"`. Dans l'élément body de `index.html`, juste avant la balise `script`, ajoutez :

```
<div id="js"></div>
```

Maintenant dans `script.js`, attrapons cet nouvel élément `div` par son id et mettons-le dans une constante. Nommons cette constante `jsContainer`. Nous pouvons utiliser `document.getElementById` pour attraper le `div` depuis HTML :

```js
jsContainer.innerHTML = `
  <div class="demo">
    Hello JS
  </div>
`;
```

Pour contrôler le contenu de ce `div`, nous pouvons utiliser l'appel setter `innerHTML` sur l'élément `div` directement. Nous pouvons utiliser cet appel pour fournir n'importe quel modèle HTML que nous voulons insérer dans le DOM. Insérons un élément `div` avec une classe "demo" et la chaîne "Hello JS" comme contenu :

```js
jsContainer.innerHTML = `  <div class="demo">    Hello JS  </div>`;ReactDOM.render(
  /* TODO: Version React du modèle HTML */,
  reactContainer
)
```

Assurez-vous que cela fonctionne dans le navigateur. Vous devriez voir la ligne "Hello JS" sur l'écran maintenant.

Cette div de démonstration est notre interface utilisateur jusqu'à présent. C'est une interface très simple. Nous affichons simplement un texte pour que l'utilisateur le voie.

`document.getElementById` et `element.innerHTML` font en fait partie de l'API Web DOM native. Nous communiquons directement avec le navigateur ici en utilisant les API supportées de la plateforme Web. Lorsque nous écrivons du code React, cependant, nous utilisons l'API React à la place, et nous laissons React communiquer avec le navigateur en utilisant l'API Web DOM.

React agit comme notre _agent_ pour le navigateur, et nous devons _principalement_ communiquer uniquement avec React, notre agent, et non avec le navigateur lui-même. Je dis principalement parce qu'il y a des cas où nous devons encore communiquer avec le navigateur, mais ceux-ci sont rares.

Pour créer la même interface utilisateur que nous avons jusqu'à présent mais avec l'API React cette fois, créons un autre élément `div` et donnons-lui un id de `"react"`. Dans `index.html`, juste sous l'élément `div#js`, ajoutez :

```
<div id="react"></div>
```

Maintenant, dans `script.js`, créez une nouvelle constante de conteneur pour le nouveau `div` :

```
const reactContainer = document.getElementById("react");
```

Ce conteneur sera le seul appel que nous ferons à l'API web native. ReactDOM a besoin de ce conteneur pour savoir où héberger notre application dans le DOM.

Avec le conteneur react identifié, nous pouvons maintenant utiliser la bibliothèque ReactDOM pour `render` la version React du modèle HTML dans ce conteneur :

```js
ReactDOM.render(
  /* TODO: Version React du modèle HTML */,
  reactContainer
)
```

Ce que nous allons faire ensuite est votre première étape vers la véritable compréhension de la bibliothèque React. Vous souvenez-vous quand je vous ai dit qu'avec React nous écrivons du HTML en utilisant JavaScript ? C'est exactement ce que nous allons faire ensuite.

Pour écrire notre interface utilisateur HTML simple, nous allons utiliser des appels JavaScript vers l'API React, et à la fin de l'exemple, vous aurez une meilleure image de la raison pour laquelle nous le faisons.

Au lieu de travailler avec des chaînes (comme nous l'avons fait dans l'exemple JavaScript natif ci-dessus), dans React, nous travaillons avec des _objets_. Toute chaîne HTML sera représentée comme un objet en utilisant un appel `React.createElement` (qui est la fonction centrale de l'API React).

Voici l'interface utilisateur HTML équivalente que nous avons jusqu'à présent avec React :

```
ReactDOM.render(
    React.createElement(
      "div",
      { className: "demo" },
      "Hello React"
    ),
    reactContainer
  );
```

`React.createElement` a plusieurs arguments :

* Le premier argument est la balise HTML, qui est `div` dans notre exemple.
* Le deuxième argument est un objet qui représente les attributs que nous voulons que cette balise ait. Pour correspondre à l'exemple JS natif, nous avons utilisé `{ className: "demo" }` qui se traduit par `class="demo"`. Remarquez comment nous avons utilisé `className` au lieu de `class` dans les attributs parce qu'avec React, c'est tout JavaScript qui correspond à l'API Web, pas HTML lui-même.
* Le troisième argument est le contenu de l'élément. Nous y avons mis une chaîne "Hello React".

Nous pouvons tester cela maintenant. Le navigateur devrait rendre à la fois "Hello JS" et "Hello React". Ajoutons un style aux divs de démonstration sous forme de boîte, en utilisant ce CSS, juste pour que nous puissions diviser visuellement l'écran. Dans `index.html` :

```
<style media="screen">
  .demo {
    border: 1px solid #ccc;
    margin: 1em;
    padding: 1em;
  }
</style>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*TwcqWtECXp6OA0mowRcvEA.png)
_Image capturée dans Chrome_

Nous avons maintenant deux nœuds, l'un étant contrôlé avec l'API Web DOM directement, et l'autre étant contrôlé avec l'API React (qui utilise à son tour l'API Web DOM). La seule différence majeure entre les façons dont nous construisons ces deux nœuds dans le navigateur est que dans la version JS nous avons utilisé une chaîne pour représenter le contenu, tandis que dans la version React nous avons utilisé des appels JavaScript purs et représenté le contenu avec un objet au lieu d'une chaîne.

Peu importe à quel point l'interface utilisateur HTML va devenir compliquée, lorsque vous utilisez React, chaque élément HTML sera représenté avec un objet JavaScript en utilisant un appel `React.createElement`.

Ajoutons maintenant quelques fonctionnalités supplémentaires à notre interface utilisateur simple. Ajoutons une zone de texte pour lire l'entrée de l'utilisateur.

Pour imbriquer des éléments dans notre modèle HTML, c'est simple dans la version JS car ce n'est que du HTML. Par exemple, pour faire en sorte que la `div` de démonstration rende un élément `<input/>`, nous l'ajoutons simplement au contenu :

```
jsContainer.innerHTML = `
  <div class="demo">
    Hello JS
    <input />
  </div>
`;
```

Nous pouvons faire la même chose avec React en ajoutant plus d'arguments après le 3ème argument pour `React.createElement`. Pour correspondre à ce que nous avons fait dans l'exemple JS natif, nous pouvons ajouter un 4ème argument qui est un autre appel `React.createElement` qui rend un élément `input` (rappelons que chaque élément HTML est un objet) :

```js
ReactDOM.render(
  React.createElement(
    "div",
    { className: "demo" },
    "Hello React",
    React.createElement("input")
  ),
  reactContainer
);
```

_À ce stade, si vous vous demandez ce que nous faisons et pensez « cela complique un processus simple », vous avez tout à fait raison ! Mais il y a une très bonne raison à ce que nous faisons. Continuez à lire._

Ajoutons également un horodatage dans les deux versions. Dans la version JS, mettons l'horodatage dans un élément de paragraphe. Nous pouvons utiliser un appel à `new Date()` pour afficher un horodatage simple :

```js
jsContainer.innerHTML = `
  <div class="demo">
    Hello JS
    <input />
    <p>${new Date()}</p>
  </div>
`;
```

Pour faire la même chose dans React, nous ajoutons un 5ème argument à l'élément `div` de niveau supérieur. Ce nouvel argument est un autre appel `React.createElement`, cette fois en utilisant une balise `p`, sans attributs, et la chaîne `new Date()` pour le contenu :

```js
ReactDOM.render(
  React.createElement(
    "div",
    { className: "demo" },
    "Hello React",
    React.createElement("input"),
    React.createElement(
      "p",
      null,
      new Date().toString()
    )
  ),
  reactContainer
);
```

Les versions JS et React rendent toujours le même HTML dans le navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fLaNHWXUJh4ICEvMXByvwg.png)
_Image capturée dans Chrome_

Comme vous pouvez le voir, jusqu'à présent, utiliser React est en fait beaucoup plus difficile que la méthode native simple et familière. Qu'est-ce que React fait si bien que cela vaut la peine d'abandonner le HTML familier et d'avoir à apprendre une nouvelle API pour écrire ce qui peut être simplement écrit en HTML ? La réponse ne concerne pas le rendu de la première vue HTML, mais ce que nous devons faire pour mettre à jour une vue existante dans le DOM.

Alors, faisons une opération de mise à jour sur le DOM que nous avons jusqu'à présent. Faisons simplement en sorte que l'horodatage s'actualise chaque seconde.

Nous pouvons facilement répéter un appel de fonction JavaScript dans un navigateur en utilisant l'API de minuterie Web `setInterval`. Alors, mettons toutes nos manipulations de DOM pour les versions JS et React dans une fonction, appelons-la `render`, et utilisons-la dans un appel `setInterval` pour la répéter chaque seconde.

Voici le code final complet dans `script.js` :

```js
const jsContainer = document.getElementById("js");
const reactContainer = document.getElementById("react");
const render = () => {
  jsContainer.innerHTML = `
    <div class="demo">
      Hello JS
      <input />
      <p>${new Date()}</p>
    </div>
  `;
  ReactDOM.render(
    React.createElement(
      "div",
      { className: "demo" },
      "Hello React ",
      React.createElement("input"),
      React.createElement(
        "p",
        null,
        new Date().toString()
      )
    ),
    reactContainer
  );
}
setInterval(render, 1000);
```

Lorsque nous actualisons le navigateur maintenant, la chaîne d'horodatage devrait s'actualiser chaque seconde dans les deux versions. Nous mettons maintenant à jour notre interface utilisateur dans le DOM.

_C'est le moment où React va potentiellement vous épater._ Si vous essayez de taper quelque chose dans la zone de texte de la version JS, vous ne pourrez pas. C'est tout à fait attendu car nous jetons essentiellement tout le nœud DOM à chaque tick et le régénérons. Cependant, si vous essayez de taper quelque chose dans la zone de texte qui est rendue avec React, vous pouvez certainement le faire !

Bien que tout le code de rendu React soit dans notre minuteur, React ne change que le paragraphe de l'horodatage et non tout le nœud DOM. C'est pourquoi la zone de texte n'a pas été régénérée et nous avons pu y taper.

Vous pouvez voir les différentes façons dont nous mettons à jour le DOM visuellement si vous inspectez les deux nœuds DOM dans un panneau d'éléments des outils de développement Chrome. Les outils div Chrome mettent en évidence les éléments HTML qui sont mis à jour. Vous verrez comment nous régénérons toute la div "js" à chaque tick, tandis que React régénère intelligemment uniquement le paragraphe avec la chaîne d'horodatage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9RGpVv6Mwjl6LApR7vsYqA.gif)
_Image capturée dans Chrome_

React dispose d'un algorithme de _diffing_ intelligent qu'il utilise pour ne régénérer dans son nœud DOM que ce qui doit réellement être régénéré, tout en gardant le reste tel quel. Ce processus de diffing est possible grâce au DOM virtuel de React et au fait que nous avons une représentation de notre interface utilisateur en mémoire (parce que nous avons écrit en JavaScript).

En utilisant le DOM virtuel, React conserve la dernière version du DOM en mémoire et lorsqu'il a une nouvelle version du DOM à prendre dans le navigateur, cette nouvelle version du DOM sera également en mémoire, donc React peut calculer la différence entre les nouvelles et les anciennes versions (dans notre cas, la différence est le paragraphe de l'horodatage).

React instruira ensuite le navigateur de mettre à jour uniquement le diff calculé et non tout le nœud DOM. Peu importe le nombre de fois où nous régénérons notre interface, React n'apportera au navigateur que les nouvelles mises à jour "partielles".

Non seulement cette méthode est beaucoup plus efficace, mais elle supprime également une grande couche de complexité pour la façon dont nous _pensons_ à la mise à jour des interfaces utilisateur. Le fait que React effectue tous les calculs sur le fait de savoir si nous devons mettre à jour le DOM ou non nous permet de nous concentrer sur la réflexion sur nos données (état) et sur la façon de décrire une interface utilisateur pour celles-ci.

Nous gérons ensuite les mises à jour de nos données selon les besoins sans nous soucier des étapes nécessaires pour refléter ces mises à jour sur l'interface utilisateur réelle dans le navigateur (parce que nous savons que React fera exactement cela et le fera de manière efficace !)

Merci d'avoir lu ! Vous pouvez consulter le code source de ma démonstration [ici](https://github.com/jscomplete/react-virtual-dom-demo/tree/master/demo), et vous pouvez voir la démonstration en cours d'exécution [ici](https://jscomplete.github.io/react-virtual-dom-demo/demo/).

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)