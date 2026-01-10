---
title: Composants HTML réutilisables – Comment réutiliser un en-tête et un pied de
  page sur un site web
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-02T02:37:00.000Z'
originalURL: https://freecodecamp.org/news/reusable-html-components-how-to-reuse-a-header-and-footer-on-a-website
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c986b740569d1a4ca19f5.jpg
tags:
- name: components
  slug: components
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
seo_title: Composants HTML réutilisables – Comment réutiliser un en-tête et un pied
  de page sur un site web
seo_desc: 'Imagine you''re building a site for a client, a small mom-and-pop store,
  that only has two pages.

  That''s not a lot. So when you finish working on the landing page and start on the
  contact page, you just create a new HTML file and copy over all the cod...'
---

Imaginez que vous construisez un site pour un client, une petite boutique familiale, qui ne comporte que deux pages.

Ce n'est pas beaucoup. Donc, lorsque vous avez terminé de travailler sur la page d'accueil et que vous commencez sur la page de contact, vous créez simplement un nouveau fichier HTML et copiez tout le code de la première page.

L'en-tête et le pied de page sont déjà bien en place, et tout ce que vous avez à faire est de changer le reste du contenu.

Mais que se passe-t-il si votre client veut 10 pages ? Ou 20 ? Et s'il demande des modifications mineures à l'en-tête et au pied de page tout au long du développement.

Soudain, toute modification, aussi petite soit-elle, doit être répétée dans tous ces fichiers.

C'est l'un des principaux problèmes que des outils comme React ou Handlebars.js résolvent : tout code, en particulier des éléments structurels comme un en-tête ou un pied de page, peut être écrit une fois et facilement réutilisé dans tout un projet.

Jusqu'à récemment, il n'était pas possible d'utiliser des composants en HTML et JavaScript vanilla. Mais avec l'introduction des Web Components, il est possible de créer des composants réutilisables sans utiliser des outils comme React.

## Qu'est-ce que les Web Components ?

Les Web Components sont en fait une collection de plusieurs technologies différentes qui vous permettent de créer des éléments HTML personnalisés.

Ces technologies sont :

* **[Modèles HTML](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_templates_and_slots)** : Fragments de balisage HTML utilisant des éléments `<template>` qui ne seront pas rendus tant qu'ils ne sont pas ajoutés à la page avec JavaScript.
* **[Éléments personnalisés](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)** : API JavaScript largement supportées qui vous permettent de créer de nouveaux éléments DOM. Une fois que vous avez créé et enregistré un élément personnalisé en utilisant ces API, vous pouvez l'utiliser de manière similaire à un composant React.
* **[Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM)** : Un DOM plus petit et encapsulé qui est isolé du DOM principal et rendu séparément. Tous les styles et scripts que vous créez pour vos composants personnalisés dans le Shadow DOM n'affecteront pas les autres éléments du DOM principal.

Nous allons approfondir chacune de ces technologies un peu plus tout au long du tutoriel.

## Comment utiliser les modèles HTML

La première pièce du puzzle est d'apprendre à utiliser les modèles HTML pour créer du balisage HTML réutilisable.

Regardons un exemple simple de message de bienvenue :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="style.css" rel="stylesheet" type="text/css" />
    <script src="index.js" type="text/javascript" defer></script>
  </head>
  <body>
    <template id="welcome-msg">
      <h1>Bonjour, le monde !</h1>
      <p>Et tous ceux qui l'habitent</p>
    </template>
  </body>
<html>

```

Si vous regardez la page, ni les éléments `<h1>` ni `<p>` ne sont rendus. Mais si vous ouvrez la console de développement, vous verrez que les deux éléments ont été analysés :

![La console de développement montrant l'élément de modèle de message de bienvenue.](https://www.freecodecamp.org/news/content/images/2020/10/image-50.png)

Pour rendre réellement le message de bienvenue, vous devrez utiliser un peu de JavaScript :

```js
const template = document.getElementById('welcome-msg');

document.body.appendChild(template.content);

```

![Le navigateur montrant l'élément de modèle de message de bienvenue, et le contenu réel du message de bienvenue.](https://www.freecodecamp.org/news/content/images/2020/10/image-51.png)

Même si c'est un exemple assez simple, vous pouvez déjà voir comment l'utilisation de modèles facilite la réutilisation du code dans une page.

Le principal problème est que, au moins avec l'exemple actuel, le code du message de bienvenue est mélangé avec le reste du contenu de la page. Si vous souhaitez modifier le message de bienvenue plus tard, vous devrez modifier le code dans plusieurs fichiers.

Au lieu de cela, vous pouvez intégrer le modèle HTML dans le fichier JavaScript, de sorte que toute page incluant le JavaScript affichera le message de bienvenue :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="style.css" rel="stylesheet" type="text/css" />
    <script src="index.js" type="text/javascript" defer></script>
  </head>
  <body>
      
  </body>
<html>

```

```js
const template = document.createElement('template');

template.innerHTML = `
  <h1>Bonjour, le monde !</h1>
  <p>Et tous ceux qui l'habitent</p>
`;

document.body.appendChild(template.content);

```

Maintenant que tout est dans le fichier JavaScript, vous n'avez pas besoin de créer un élément `<template>` – vous pourriez tout aussi facilement créer un `<div>` ou un `<span>`.

Cependant, les éléments `<template>` peuvent être associés à un élément `<slot>`, ce qui vous permet de faire des choses comme changer le texte des éléments à l'intérieur du `<template>`. C'est un peu en dehors du cadre de ce tutoriel, donc vous pouvez en lire plus sur les éléments `<slot>` [sur MDN](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_templates_and_slots#Adding_flexibility_with_slots).

## Comment créer des éléments personnalisés

Une chose que vous avez peut-être remarqué avec les modèles HTML est qu'il peut être difficile d'insérer votre code au bon endroit. Le message de bienvenue précédent a simplement été ajouté à la page.

S'il y avait déjà du contenu sur la page, par exemple, une image de bannière, le message de bienvenue apparaîtrait en dessous.

En tant qu'élément personnalisé, votre message de bienvenue pourrait ressembler à ceci :

```html
<welcome-message></welcome-message>

```

Et vous pouvez le placer où vous voulez sur la page.

Avec cela en tête, examinons les éléments personnalisés et créons nos propres éléments d'en-tête et de pied de page similaires à React.

### Installation

Pour un site de portfolio, vous pourriez avoir un code de base qui ressemble à ceci :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <main>
      <!-- Le contenu de votre page -->
    </main>
  </body>
<html>

```

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%;
}

body {
  color: #333;
  font-family: sans-serif;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1 0 auto;
}

```

Chaque page aura le même en-tête et pied de page, il est donc logique de créer un élément personnalisé pour chacun d'eux.

Commençons par l'en-tête.

### Définir un élément personnalisé

Tout d'abord, créez un répertoire appelé `components` et à l'intérieur de ce répertoire, créez un nouveau fichier appelé `header.js` avec le code suivant :

```js
class Header extends HTMLElement {
  constructor() {
    super();
  }
}

```

C'est simplement une `Class` ES5 déclarant votre composant personnalisé `Header`, avec la méthode `constructor` et le mot-clé spécial `super`. Vous pouvez en lire plus sur ceux-ci [sur MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes).

En étendant la classe générique `[HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)`, vous pouvez créer n'importe quel type d'élément que vous souhaitez. Il est également possible d'étendre des éléments spécifiques comme `[HTMLParagraphElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLParagraphElement)`.

### Enregistrer votre élément personnalisé

Avant de pouvoir commencer à utiliser votre élément personnalisé, vous devrez l'enregistrer avec la méthode `customElements.define()` :

```js
class Header extends HTMLElement {
  constructor() {
    super();
  }
}

customElements.define('header-component', Header);

```

Cette méthode prend au moins deux arguments.

Le premier est un `DOMString` que vous utiliserez lors de l'ajout du composant à la page, dans ce cas, `<header-component></header-component>`.

Le suivant est la classe du composant que vous avez créée précédemment, ici, la classe `Header`.

Le troisième argument optionnel décrit quel élément HTML existant votre élément personnalisé hérite des propriétés, par exemple, `{extends: 'p'}`. Mais nous n'utiliserons pas cette fonctionnalité dans ce tutoriel.

### Utiliser les rappels de cycle de vie pour ajouter l'en-tête à la page

Il existe quatre rappels de cycle de vie spéciaux pour les éléments personnalisés que nous pouvons utiliser pour ajouter le balisage de l'en-tête à la page : `connectedCallback`, `attributeChangeCallback`, `disconnectedCallback`, et `adoptedCallback`.

Parmi ces rappels, `connectedCallback` est l'un des plus couramment utilisés. `connectedCallback` s'exécute chaque fois que votre élément personnalisé est inséré dans le DOM.

Vous pouvez en lire plus sur les autres rappels [ici](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements#Using_the_lifecycle_callbacks).

Pour notre exemple simple, `connectedCallback` suffit pour ajouter un en-tête à la page :

```js
class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <style>
        nav {
          height: 40px;
          display: flex;
          align-items: center;
          justify-content: center;
          background-color:  #0a0a23;
        }

        ul {
          padding: 0;
        }
        
        a {
          font-weight: 700;
          margin: 0 25px;
          color: #fff;
          text-decoration: none;
        }
        
        a:hover {
          padding-bottom: 5px;
          box-shadow: inset 0 -2px 0 0 #fff;
        }
      </style>
      <header>
        <nav>
          <ul>
            <li><a href="about.html">À propos</a></li>
            <li><a href="work.html">Travail</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </nav>
      </header>
    `;
  }
}

customElements.define('header-component', Header);

```

Ensuite, dans `index.html`, ajoutez le script `components/header.js` et `<header-component></header-component>` juste au-dessus de l'élément `<main>` :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="style.css" rel="stylesheet" type="text/css" />
    <script src="components/header.js" type="text/javascript" defer></script>
  </head>
  <body>
    <header-component></header-component>
    <main>
      <!-- Le contenu de votre page -->
    </main>
  </body>
<html>

```

Et votre composant d'en-tête réutilisable devrait être rendu sur la page :

![Le navigateur avec le composant d'en-tête.](https://www.freecodecamp.org/news/content/images/2020/10/image-54.png)

Maintenant, ajouter un en-tête à la page est aussi simple que d'ajouter une balise `<script>` pointant vers `components/header.js`, et d'ajouter `<header-component></header-component>` où vous le souhaitez.

Notez que, puisque l'en-tête et son style sont insérés directement dans le DOM principal, il est possible de le styliser dans le fichier `style.css`.

Mais si vous regardez les styles de l'en-tête inclus dans `connectedCallback`, ils sont assez généraux et peuvent affecter d'autres styles sur la page.

Par exemple, si nous ajoutons Font Awesome et un composant de pied de page à `index.html` :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
    <link href="style.css" rel="stylesheet" type="text/css" />
    <script src="components/header.js" type="text/javascript" defer></script>
    <script src="components/footer.js" type="text/javascript" defer></script>
  </head>
  <body>
    <header-component></header-component>
    <main>
      <!-- Le contenu de votre page -->
    </main>
    <footer-component></footer-component>
  </body>
<html>

```

```js
class Footer extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    this.innerHTML = `
      <style>
        footer {
          height: 60px;
          padding: 0 10px;
          list-style: none;
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #dfdfe2;
        }
        
        ul li {
          list-style: none;
          display: inline;
        }
        
        a {
          margin: 0 15px;
          color: inherit;
          text-decoration: none;
        }
        
        a:hover {
          padding-bottom: 5px;
          box-shadow: inset 0 -2px 0 0 #333;
        }
        
        .social-row {
          font-size: 20px;
        }
        
        .social-row li a {
          margin: 0 15px;
        }
      </style>
      <footer>
        <ul>
          <li><a href="about.html">À propos</a></li>
          <li><a href="work.html">Travail</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
        <ul class="social-row">
          <li><a href="https://github.com/my-github-profile"><i class="fab fa-github"></i></a></li>
          <li><a href="https://twitter.com/my-twitter-profile"><i class="fab fa-twitter"></i></a></li>
          <li><a href="https://www.linkedin.com/in/my-linkedin-profile"><i class="fab fa-linkedin"></i></a></li>
        </ul>
      </footer>
    `;
  }
}

customElements.define('footer-component', Footer);

```

Voici à quoi ressemblerait la page :

![Le navigateur avec les composants d'en-tête et de pied de page.](https://www.freecodecamp.org/news/content/images/2020/10/image-55.png)

Le style du composant de pied de page remplace le style de l'en-tête, changeant la couleur des liens. C'est un comportement attendu pour CSS, mais il serait bien que le style de chaque composant soit limité à ce composant et n'affecte pas d'autres éléments sur la page.

Eh bien, c'est exactement là que le Shadow DOM excelle. Ou ombre ? En tout cas, le Shadow DOM peut faire cela.

### Comment utiliser le Shadow DOM avec des éléments personnalisés

Le Shadow DOM agit comme une instance séparée et plus petite du DOM principal. Plutôt que d'agir comme une copie du DOM principal, le Shadow DOM est plus comme un sous-arbre juste pour votre élément personnalisé. Tout ce qui est ajouté à un Shadow DOM, en particulier les styles, est limité à cet élément personnalisé particulier.

D'une certaine manière, c'est comme utiliser `const` et `let` plutôt que `var`.

Commençons par refactoriser le composant d'en-tête :

```js
const headerTemplate = document.createElement('template');

headerTemplate.innerHTML = `
  <style>
    nav {
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color:  #0a0a23;
    }

    ul {
      padding: 0;
    }
    
    ul li {
      list-style: none;
      display: inline;
    }
    
    a {
      font-weight: 700;
      margin: 0 25px;
      color: #fff;
      text-decoration: none;
    }
    
    a:hover {
      padding-bottom: 5px;
      box-shadow: inset 0 -2px 0 0 #fff;
    }
  </style>
  <header>
    <nav>
      <ul>
        <li><a href="about.html">À propos</a></li>
        <li><a href="work.html">Travail</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
`;

class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    
  }
}

customElements.define('header-component', Header);

```

La première chose que vous devez faire est d'utiliser la méthode `.attachShadow()` pour attacher une racine d'ombre à votre élément de composant d'en-tête personnalisé. Dans `connectedCallback`, ajoutez le code suivant :

```js
...
class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadowRoot = this.attachShadow({ mode: 'closed' });
  }
}

customElements.define('header-component', Header);

```

Remarquez que nous passons un objet à `.attachShadow()` avec une option, `mode: 'closed'`. Cela signifie simplement que le Shadow DOM du composant d'en-tête est inaccessible depuis le JavaScript externe.

Si vous souhaitez manipuler le Shadow DOM du composant d'en-tête plus tard avec JavaScript en dehors du fichier `components/header.js`, changez simplement l'option en `mode: 'open'`.

Enfin, ajoutez `shadowRoot` à la page avec la méthode `.appendChild()` :

```js
...

class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadowRoot = this.attachShadow({ mode: 'closed' });

    shadowRoot.appendChild(headerTemplate.content);
  }
}

customElements.define('header-component', Header);

```

Et maintenant, puisque les styles du composant d'en-tête sont encapsulés dans son Shadow DOM, la page devrait ressembler à ceci :

![Le navigateur avec le composant d'en-tête Shadow DOM et le composant de pied de page régulier.](https://www.freecodecamp.org/news/content/images/2020/10/image-56.png)

Et voici le composant de pied de page refactorisé pour utiliser le Shadow DOM :

```js
const footerTemplate = document.createElement('template');

footerTemplate.innerHTML = `
  <style>
    footer {
      height: 60px;
      padding: 0 10px;
      list-style: none;
      display: flex;
      flex-shrink: 0;
      justify-content: space-between;
      align-items: center;
      background-color: #dfdfe2;
    }

    ul {
      padding: 0;
    }
    
    ul li {
      list-style: none;
      display: inline;
    }
    
    a {
      margin: 0 15px;
      color: inherit;
      text-decoration: none;
    }
    
    a:hover {
      padding-bottom: 5px;
      box-shadow: inset 0 -2px 0 0 #333;
    }
    
    .social-row {
      font-size: 20px;
    }
    
    .social-row li a {
      margin: 0 15px;
    }
  </style>
  <footer>
    <ul>
      <li><a href="about.html">À propos</a></li>
      <li><a href="work.html">Travail</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <ul class="social-row">
      <li><a href="https://github.com/my-github-profile"><i class="fab fa-github"></i></a></li>
      <li><a href="https://twitter.com/my-twitter-profile"><i class="fab fa-twitter"></i></a></li>
      <li><a href="https://www.linkedin.com/in/my-linkedin-profile"><i class="fab fa-linkedin"></i></a></li>
    </ul>
  </footer>
`;

class Footer extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadowRoot = this.attachShadow({ mode: 'closed' });

    shadowRoot.appendChild(footerTemplate.content);
  }
}

customElements.define('footer-component', Footer);

```

Mais si vous vérifiez sur la page, vous remarquerez que les icônes Font Awesome sont maintenant manquantes :

![Le navigateur montrant les versions Shadow DOM des composants d'en-tête et de pied de page.](https://www.freecodecamp.org/news/content/images/2021/09/missing-fa-icons-1.png)

Maintenant que le composant de pied de page est encapsulé dans son propre Shadow DOM, il n'a plus accès au lien CDN Font Awesome dans `index.html`.

Examinons rapidement pourquoi c'est le cas et comment faire fonctionner Font Awesome à nouveau.

## Encapsulation et le Shadow DOM

Bien que le Shadow DOM empêche les styles de vos composants d'affecter le reste de la page, certains styles globaux peuvent encore s'infiltrer dans vos composants.

Dans les exemples ci-dessus, cela a été une fonctionnalité utile. Par exemple, le composant de pied de page hérite de la déclaration `color: #333` qui est définie dans `style.css`. Cela est dû au fait que `color` est l'une des quelques propriétés héritables, avec `font`, `font-family`, `direction`, et plus encore.

Si vous souhaitez empêcher ce comportement et styliser chaque composant complètement à partir de zéro, vous pouvez le faire avec quelques lignes de CSS :

```css
:host {
  all: initial;
  display: block;
}
```

`:host` est un pseudo-sélecteur qui sélectionne l'élément qui héberge le Shadow DOM. Dans ce cas, c'est votre composant personnalisé.

Ensuite, la déclaration `all: initial` réinitialise toutes les propriétés CSS à leur valeur initiale. Et `display: block` fait de même pour la propriété `display`, et la réinitialise à la valeur par défaut du navigateur, `block`.

Pour une liste complète des propriétés CSS héritables, consultez cette [réponse sur Stack Overflow](https://stackoverflow.com/questions/5612302/which-css-properties-are-inherited).

## Comment utiliser Font Awesome avec le Shadow DOM

Maintenant, vous pourriez vous demander, si `font`, `font-family` et d'autres propriétés CSS liées aux polices sont des propriétés héritables, pourquoi Font Awesome ne se charge-t-il pas maintenant que le composant de pied de page utilise le Shadow DOM ?

Il s'avère que, pour des éléments comme les polices et autres ressources, ils doivent être référencés à la fois dans le DOM principal et le Shadow DOM pour fonctionner correctement.

Heureusement, il existe quelques méthodes simples pour résoudre ce problème.

Note : Toutes ces méthodes nécessitent toujours que Font Awesome soit inclus dans `index.html` avec l'élément `link` comme dans les extraits de code ci-dessus.

### #1 : Lien vers Font Awesome dans votre composant

La méthode la plus directe pour faire fonctionner Font Awesome dans votre composant Shadow DOM est d'inclure un `link` vers celui-ci dans le composant lui-même :

```js
const footerTemplate = document.createElement('template');

footerTemplate.innerHTML = `
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
  <style>
    footer {
      height: 60px;
      padding: 0 10px;
      list-style: none;
...
```

Une chose à noter est que, bien qu'il semble que vous fassiez charger Font Awesome deux fois par le navigateur (une fois pour le DOM principal et une autre pour le composant), les navigateurs sont suffisamment intelligents pour ne pas récupérer la même ressource à nouveau.

Voici l'onglet réseau montrant que Chrome ne charge Font Awesome qu'une seule fois :

![L'onglet réseau de la console de développement montrant que Font Awesome ne se charge qu'une seule fois.](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-from-2021-09-12-14-53-01.png)

### #2 : Importer Font Awesome dans votre composant

Ensuite, vous pouvez utiliser `@import` et `url()` pour charger Font Awesome dans votre composant :

```js
const footerTemplate = document.createElement('template');

footerTemplate.innerHTML = `
  <style>
    @import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css");

    footer {
      height: 60px;
      padding: 0 10px;
      list-style: none;
...
```

Notez que l'URL doit être la même que celle que vous utilisez dans `index.html`.

### #3 : Utiliser JavaScript pour charger dynamiquement Font Awesome dans votre composant

Enfin, la méthode la plus DRY pour charger Font Awesome dans votre composant est d'utiliser un peu de JavaScript :

```js
...
class Footer extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    // Interroger le DOM principal pour FA
    const fontAwesome = document.querySelector('link[href*="font-awesome"]');
    const shadowRoot = this.attachShadow({ mode: 'closed' });

    // Charger FA dans le composant de manière conditionnelle
    if (fontAwesome) {
      shadowRoot.appendChild(fontAwesome.cloneNode());
    }

    shadowRoot.appendChild(footerTemplate.content);
  }
}

customElements.define('footer-component', Footer);
```

Cette méthode est basée sur [cette réponse sur Stack Overflow](https://stackoverflow.com/a/55360574), et fonctionne assez simplement. Lorsque le composant se charge, si un élément `link` pointant vers Font Awesome existe, il est cloné et ajouté au Shadow DOM du composant :

![La console de développement montrant que Font Awesome a été ajouté dynamiquement au composant Shadow DOM.](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-from-2021-09-12-19-31-19.png)

## Code final

Voici à quoi ressemble le code final dans tous les fichiers, en utilisant la méthode #3 pour charger Font Awesome dans le composant de pied de page :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
    <link href="style.css" rel="stylesheet" type="text/css" />
    <script src="components/header.js" type="text/javascript" defer></script>
    <script src="components/footer.js" type="text/javascript" defer></script>
  </head>
  <body>
    <header-component></header-component>
    <main>
      <!-- Le contenu de votre page -->
    </main>
    <footer-component></footer-component>
  </body>
<html>

```

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  height: 100%;
}

body {
  color: #333;
  font-family: sans-serif;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1 0 auto;
}

```

```js
const headerTemplate = document.createElement('template');

headerTemplate.innerHTML = `
  <style>
    nav {
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color:  #0a0a23;
    }

    ul {
      padding: 0;
    }
    
    ul li {
      list-style: none;
      display: inline;
    }
    
    a {
      font-weight: 700;
      margin: 0 25px;
      color: #fff;
      text-decoration: none;
    }
    
    a:hover {
      padding-bottom: 5px;
      box-shadow: inset 0 -2px 0 0 #fff;
    }
  </style>
  <header>
    <nav>
      <ul>
        <li><a href="about.html">À propos</a></li>
        <li><a href="work.html">Travail</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
`;

class Header extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadowRoot = this.attachShadow({ mode: 'closed' });

    shadowRoot.appendChild(headerTemplate.content);
  }
}

customElements.define('header-component', Header);

```

```js
const footerTemplate = document.createElement('template');

footerTemplate.innerHTML = `
  <style>
    footer {
      height: 60px;
      padding: 0 10px;
      list-style: none;
      display: flex;
      flex-shrink: 0;
      justify-content: space-between;
      align-items: center;
      background-color: #dfdfe2;
    }

    ul {
      padding: 0;
    }
    
    ul li {
      list-style: none;
      display: inline;
    }
    
    a {
      margin: 0 15px;
      color: inherit;
      text-decoration: none;
    }
    
    a:hover {
      padding-bottom: 5px;
      box-shadow: inset 0 -2px 0 0 #333;
    }
    
    .social-row {
      font-size: 20px;
    }
    
    .social-row li a {
      margin: 0 15px;
    }
  </style>
  <footer>
    <ul>
      <li><a href="about.html">À propos</a></li>
      <li><a href="work.html">Travail</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <ul class="social-row">
      <li><a href="https://github.com/my-github-profile"><i class="fab fa-github"></i></a></li>
      <li><a href="https://twitter.com/my-twitter-profile"><i class="fab fa-twitter"></i></a></li>
      <li><a href="https://www.linkedin.com/in/my-linkedin-profile"><i class="fab fa-linkedin"></i></a></li>
    </ul>
  </footer>
`;

class Footer extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const fontAwesome = document.querySelector('link[href*="font-awesome"]');
    const shadowRoot = this.attachShadow({ mode: 'closed' });

    if (fontAwesome) {
      shadowRoot.appendChild(fontAwesome.cloneNode());
    }

    shadowRoot.appendChild(footerTemplate.content);
  }
}

customElements.define('footer-component', Footer);

```

## En conclusion

Nous avons couvert beaucoup de choses ici, et vous avez peut-être déjà décidé d'utiliser React ou Handlebars.js à la place.

Ce sont deux excellentes options !

Néanmoins, pour un projet plus petit où vous n'aurez besoin que de quelques composants réutilisables, une bibliothèque entière ou un langage de modélisation pourrait être excessif.

Espérons que vous avez maintenant la confiance nécessaire pour créer vos propres composants HTML réutilisables. Maintenant, allez-y et créez quelque chose de grand (et réutilisable).