---
title: Qu'est-ce que le Document Object Model ? Le DOM pour les débutants
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-01-10T15:14:00.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-the-dom
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/dom-introduction-feature-image-1.png
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le Document Object Model ? Le DOM pour les débutants
seo_desc: 'In this article, I''m going to explain to you how the DOM works so that
  you have a clear picture of why JavaScript is needed to develop a web application.

  First, let''s recap what we know about HTML, CSS, and JavaScript.

  How HTML, CSS, and JavaScript w...'
---

Dans cet article, je vais vous expliquer comment fonctionne le DOM afin que vous ayez une image claire de pourquoi JavaScript est nécessaire pour développer une application web.

Tout d'abord, faisons un récapitulatif de ce que nous savons sur HTML, CSS et JavaScript.

## Comment fonctionnent HTML, CSS et JavaScript

Lorsque vous souhaitez construire une application web, vous créez un document HTML rempli de HTML, CSS et JavaScript.

Ces trois technologies sont utilisées ensemble comme une équipe, chacune jouant un rôle différent dans la construction de ce que vous voyez dans votre navigateur web.

HTML est un langage de balisage utilisé pour définir la structure et le contenu de la page. Les balises que nous utilisons comme `<head>`, `<body>` et `<button>` ont des significations, et le navigateur traitera ces balises, rendant le contenu du document à l'écran.

![9 just html](https://www.freecodecamp.org/news/content/images/2024/01/9-just-html.png)
_À quoi ressemble un site web avec uniquement HTML_

Mais le HTML seul produit une page très ennuyeuse et générique. CSS a été créé pour nous permettre de changer la façon dont les balises HTML sont représentées dans le navigateur.

En utilisant CSS, vous pouvez faire en sorte qu'un bouton soit affiché dans une couleur de votre choix, ou une zone de texte avec une bordure arrondie, les rendant plus attrayants et modernes.

![9 html and css](https://www.freecodecamp.org/news/content/images/2024/01/9-html-and-css-1.png)
_Un site web stylisé avec CSS semble attrayant et moderne_

HTML et CSS sont de grands partenaires, mais même alors, une page web est toujours juste une chose passive. Une fois que le navigateur traite le contenu et le rend, vous ne pouvez pas modifier la page de quelque manière que ce soit.

Vous ne pouvez pas changer la couleur de fond et de texte de la page (comme passer en mode sombre, par exemple). Vous ne pouvez pas créer des animations cool, activer le microphone ou la webcam, ou récupérer des données d'un autre site web pour les afficher sur la page après un clic.

JavaScript est le langage de programmation qui est supporté par le navigateur, et il comble cette lacune laissée ouverte par HTML et CSS.

En bref, JavaScript donne vie aux sites web statiques, les rendant dynamiques. Il permet à un site web d'interagir avec l'utilisateur, de répondre à ses actions et de mettre à jour dynamiquement le contenu sans nécessiter de rechargement de la page.

## Le DOM expliqué

Alors, comment se fait-il que JavaScript puisse faire des choses que HTML et CSS ne peuvent pas faire ? Eh bien, la réponse est que JavaScript peut manipuler le Document Object Model, ou le DOM en abrégé.

Le DOM est une structure hiérarchique composée d'objets qui constituent une page web. Les navigateurs web exposent ensuite ce DOM afin que vous puissiez changer la structure, le style et le contenu de la page en utilisant JavaScript.

Par exemple, supposons que vous avez le contenu HTML suivant dans votre document :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Hello World!</h1>
  <p>This is a paragraph element</p>
</body>
</html>
```

Le graphe DOM généré par le document HTML ci-dessus est le suivant. Je vais expliquer ce que signifie le graphe ci-dessous :

![9 dom example](https://www.freecodecamp.org/news/content/images/2024/01/9-dom-example.png)
_Exemple de l'arbre DOM_

Le DOM ressemble à une structure d'arbre avec un ensemble de nœuds connectés. Ces nœuds sont des objets auxquels vous pouvez accéder en utilisant JavaScript. Le nœud `html` et ses enfants sont le contenu de votre document.

Pour l'instant, concentrons-nous sur les objets `window` et `document`.

## L'objet Window

L'objet `window` est la racine de l'arbre DOM, et cet objet est utilisé pour instruire le navigateur d'effectuer des tâches comme :

* Afficher une boîte d'alerte ou une invite
* Enregistrer des messages ou des erreurs dans la console
* Accéder au stockage local du navigateur
* Accéder à l'objet document

Vous pouvez accéder à l'objet window depuis la console en tapant `window` et en appuyant sur Entrée. Le navigateur répondra en vous montrant les méthodes et propriétés de l'objet comme suit :

![9 window](https://www.freecodecamp.org/news/content/images/2024/01/9-window.png)
_Propriétés et méthodes de l'objet Window_

L'objet `window` fournit à la fois des objets enfants et des méthodes auxquels vous allez accéder pour manipuler une page web.

Par exemple, la `window` a l'objet `console` que vous pouvez utiliser pour enregistrer un message dans la console.

Tapez le code ci-dessous dans la console et appuyez sur Entrée :

```js
window.console.log('Hello World!');
```

Vous verrez la chaîne 'Hello World!' enregistrée dans la console.

L'objet `window` est un objet global, vous pouvez donc l'omettre lorsque vous appelez son objet enfant. Pour accéder à l'objet `console`, tapez simplement console comme suit :

```js
console.log('Hello World!');
```

Il en va de même lorsque vous accédez à l'objet `document`. Vous pouvez écrire `document.propertyOrMethod` au lieu de `window.document.propertyOrMethod`.

Je ne vais pas trop approfondir l'objet `window`, car en tant que développeur web, vous allez interagir davantage avec l'objet `document` dans votre routine quotidienne.

## L'objet Document

L'objet `document` est le point d'entrée pour tous les éléments HTML que vous écrivez dans votre document. Cet objet est également ce qui donne son nom au Document Object Model.

Il n'est pas appelé Window Object Model parce que nous allons principalement travailler avec l'objet Document plutôt qu'avec l'objet Window.

![9 dom example html](https://www.freecodecamp.org/news/content/images/2024/01/9-dom-example-html.png)
_L'objet Document est l'enfant de l'objet Window_

À partir de l'objet document, vous pouvez récupérer toutes les données liées au contenu HTML en utilisant JavaScript.

Par exemple, vous pouvez obtenir le titre du document en utilisant la propriété `document.title`, et l'URL en utilisant `document.URL`. Le référent est disponible dans `document.referrer`, le domaine dans `document.domain`.

Pour le document HTML lui-même, vous pouvez accéder à l'ensemble du nœud d'élément HTML en utilisant `document.documentElement`, à l'en-tête du document en utilisant la propriété `document.head`, ou au corps en utilisant `document.body`.

Vous pouvez essayer d'accéder à ces éléments depuis la console comme montré ci-dessous :

![9 document properties](https://www.freecodecamp.org/news/content/images/2024/01/9-document-properties.png)
_Propriétés documentElement, head et body de l'objet Document_

Vous pouvez voir la documentation de toutes les propriétés et méthodes de l'objet document [ici](https://developer.mozilla.org/en-US/docs/Web/API/Document) (notez que cela peut être écrasant au début).

Bien sûr, vous pouvez faire beaucoup plus que simplement lire les données de votre document. J'ai écrit un autre article qui vous montre [comment manipuler le DOM en utilisant JavaScript](https://www.freecodecamp.org/news/javascript-document-object-model-explained/).

## Résumé

Le DOM est une structure en forme d'arbre générée à partir du fichier HTML que nous avons créé et chargé dans le navigateur.

Le navigateur expose ensuite ce DOM comme un ensemble d'objets JavaScript auxquels nous pouvons accéder, tels que les objets `window` et `document`.

C'est une pièce importante de la technologie qui vous permet de programmer le navigateur web pour effectuer des tâches spécifiques ou changer votre contenu HTML.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://codewithnathan.com/beginning-modern-javascript).

[![](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://codewithnathan.com/beginning-modern-javascript)

Le livre est conçu pour être facile pour les débutants et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide étape par étape qui vous aidera à comprendre comment utiliser JavaScript pour créer une application web dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !