---
title: Comprendre les événements DOM et les écouteurs d'événements JavaScript
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-01-10T20:38:04.000Z'
originalURL: https://freecodecamp.org/news/dom-events-and-javascript-event-listeners
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/DOM-events-feature-image.png
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: Comprendre les événements DOM et les écouteurs d'événements JavaScript
seo_desc: 'JavaScript code in the browser uses an event-driven programming pattern.
  What this means is that when a specific DOM event happens in the browser, a piece
  of code will be executed as a response to that action.

  In this article, I will help you see and...'
---

Le code JavaScript dans le navigateur utilise un modèle de programmation piloté par événements. Cela signifie que lorsqu'un événement DOM spécifique se produit dans le navigateur, un morceau de code sera exécuté en réponse à cette action.

Dans cet article, je vais vous aider à voir et à comprendre comment écouter et répondre aux événements DOM en utilisant JavaScript.

Si vous avez besoin d'un rappel sur le DOM, j'ai écrit un article qui explique [ce qu'est le DOM et comment JavaScript interagit avec lui](https://www.freecodecamp.org/news/introduction-to-the-dom/).

## Qu'est-ce que les événements DOM et pourquoi sont-ils utiles ?

Les événements DOM sont des signaux exposés par le navigateur que vous pouvez utiliser pour exécuter un morceau de code JavaScript.

Ces événements DOM se produisent lorsque l'utilisateur interagit avec l'application que nous avons créée, comme cliquer sur un bouton ou taper des lettres dans un champ de saisie.

En tant que développeur web, vous pouvez instruire JavaScript pour qu'il écoute un événement spécifique et fasse quelque chose en réponse à cet événement.

Par exemple :

* Lorsque **un bouton** est cliqué, **changer le** texte **d'**un paragraphe.
* Lorsque **un formulaire est soumis**, **faire une requête POST en utilisant l'API Fetch.**

Dans cet article, je vais vous aider à voir et à comprendre comment écouter et répondre aux événements DOM en utilisant JavaScript.

## Comment écouter les événements DOM

Pour écouter un événement, vous devez attacher un écouteur d'événement à un élément en utilisant la méthode `addEventListener()`.

La méthode `addEventListener()` accepte deux paramètres :

1. Le `type` d'événement à écouter
2. Une fonction à exécuter lorsque l'événement est déclenché

```js
Element.addEventListener(type, function);
```

Revenons à l'exemple, supposons que vous souhaitez changer le texte d'un paragraphe lorsqu'un élément `button` est cliqué. Voici comment faire :

```html
<body>
  <p id="myParagraph">Ceci est un paragraphe d'exemple</p>
  <button id="changeText">Changer le texte</button>
  <script>
    const button = document.querySelector('#changeText');

    function newText(event) {
      const p = document.querySelector('#myParagraph');
      p.innerText = 'Le texte a été changé';
    }

    button.addEventListener('click', newText);
  </script>
</body>
```

Pour insérer du code JavaScript dans le document HTML, nous devons utiliser la balise `script` comme montré ci-dessus.

L'élément bouton est sélectionné en utilisant la méthode `document.querySelector()`, puis la méthode `addEventListener()` est appelée sur l'élément. Cela signifie que vous attachez un écouteur d'événement au bouton.

Tout d'abord, vous spécifiez le `type` d'événement à écouter, qui est un événement `click` dans ce cas. Ensuite, vous spécifiez la fonction à exécuter lorsque cet événement se produit.

Dans le code ci-dessus, la fonction `newText` sera exécutée lorsque l'événement `click` est déclenché.

L'écouteur d'événement enverra également un objet `event`, qui contient des informations sur l'événement qui a été déclenché. C'est pourquoi il y a un paramètre `event` dans la fonction `newText` ci-dessus.

Vous pouvez logger l'événement dans la console pour voir ses détails :

```js
function newText(event) {
  console.log(event);
}
```

Si vous cliquez à nouveau sur le bouton, vous verrez la sortie suivante :

![Journal de l'objet événement](https://www.freecodecamp.org/news/content/images/2024/01/event-log-example-1.png)
_Un exemple de journal de l'objet événement_

Selon ce que vous souhaitez faire lorsque l'événement est déclenché, vous devrez peut-être utiliser les informations contenues dans l'objet `event`.

Ici, tout ce que nous voulons faire est de changer le texte du paragraphe, donc l'objet `event` n'est pas nécessaire. Nous verrons un exemple d'utilisation de l'objet `event` plus tard, lors de la gestion des événements clavier.

Il existe de nombreux événements que vous pouvez écouter dans le navigateur. Voici quelques-uns des événements les plus courants dont vous pourriez avoir besoin lors du développement d'une application web :

<table class="table" style="box-sizing: inherit; border-spacing: 0px; border-collapse: collapse; background-color: transparent; width: 760px; max-width: 100%; margin-bottom: 20px;"><tbody style="box-sizing: inherit;"><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Événement</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">L'événement est déclenché</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">click</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque vous appuyez et relâchez le bouton principal de la souris. Utilisé pour suivre les boutons et les éléments cliquables</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">mousemove</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque vous déplacez le curseur de la souris</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">mouseover</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque vous déplacez le curseur de la souris sur un élément. C'est comme l'état de survol CSS</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">mouseout</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque votre curseur de souris se déplace à l'extérieur des limites d'un élément</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">dblclick</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque vous cliquez deux fois</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">DOMContentLoaded</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque le contenu du DOM est entièrement chargé</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">keydown</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque vous appuyez sur une touche de votre clavier</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">keyup</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque vous relâchez une touche de votre clavier</td></tr><tr style="box-sizing: inherit;"><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">submit</td><td style="box-sizing: inherit; padding: 8px; line-height: 1.42857; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Lorsque un formulaire est soumis</td></tr></tbody></table>

Si vous souhaitez lire la liste complète des types d'événements DOM, vous pouvez [visiter cette page](https://en.wikipedia.org/wiki/DOM_event).

Les événements DOM sont divisés en plusieurs catégories. Ici, nous allons simplement examiner deux des événements les plus courants que vous pourriez utiliser dans votre projet : les événements clavier et souris.

## Événements clavier

Pour le clavier, vous pouvez suivre les événements `keydown` et `keyup`, qui s'exécutent lorsque vous appuyez et relâchez une touche, respectivement.

Pour vous montrer un exemple, exécutez le code suivant à partir de la console :

```js
document.addEventListener('keydown', event => {
  console.log(`Une touche est pressée : ${event.key}`);
});

document.addEventListener('keyup', event => {
  console.log(`Une touche est relâchée : ${event.key}`);
});
```

Une fois que vous avez exécuté le code ci-dessus, appuyez sur une touche de votre clavier lentement, puis relâchez-la lentement.

Vous devriez voir une sortie de journal comme suit :

![Journal des événements clavier](https://www.freecodecamp.org/news/content/images/2024/01/keydown-event-1.png)
_Journal des événements keydown et keyup_

Remarquez comment le journal 'keydown' apparaît dès que vous appuyez sur une touche, et le journal 'keyup' n'apparaît que lorsque vous relâchez la touche.

Les événements clavier sont généralement attachés à l'objet `document` plutôt qu'à un élément spécifique, car l'ensemble du site web doit être en mesure d'écouter cet événement.

## Événements souris

Outre les événements clavier, le DOM fournit également un moyen de suivre les événements souris.

Les événements souris les plus courants que vous pouvez suivre sont :

* `mousedown` – le bouton de la souris a été pressé
* `mouseup` – le bouton de la souris a été relâché
* `click` – un événement de clic
* `dblclick` – un événement de double clic
* `mousemove` – lorsque la souris est déplacée sur l'élément
* `contextmenu` – lorsque le menu contextuel est ouvert, par exemple sur un clic du bouton droit de la souris

Encore une fois, vous pouvez tester ces événements en ajoutant un écouteur d'événement directement à l'objet `document` :

```js
document.addEventListener('mousedown', event => {
  console.log(`La souris est pressée`);
});

document.addEventListener('mouseup', event => {
  console.log(`La souris est relâchée`);
});
```

Exécutez le code ci-dessus, puis cliquez n'importe où dans le navigateur. Vous devriez voir les événements `mousedown` et `mouseup` enregistrés, respectivement.

## Comment supprimer les écouteurs d'événements

Pour supprimer un écouteur d'événement attaché à un élément, vous devez appeler la méthode `removeEventListener()`, en passant le `type` de l'événement et la `fonction` que vous avez passée à la méthode `addEventListener()` comme suit :

```js
button.removeEventListener('click', newText);
```

Le code ci-dessus est suffisant pour supprimer l'écouteur d'événement 'click' de l'élément `button`. Remarquez comment vous devez appeler la méthode `removeEventListener()` sur l'élément tout en passant la fonction `newText` à la méthode.

Pour supprimer correctement un écouteur d'événement, vous devez avoir une référence à la fonction attachée à l'événement. Si vous passez une fonction anonyme à la méthode `addEventListener()`, alors cet événement ne peut pas être supprimé :

```js
button.addEventListener('click', function (event) {
  alert('Le bouton de sauvegarde est cliqué');
});
```

Sans le nom de la fonction comme dans l'exemple ci-dessus, vous ne pourrez pas supprimer l'écouteur d'événement.

## Comment écouter les événements en utilisant les attributs HTML

Outre l'utilisation de la méthode `addEventListener()`, vous pouvez également écouter les événements en ajoutant l'attribut `on[eventname]` à vos éléments HTML.

Par exemple, supposons que vous souhaitez écouter un clic sur un bouton. Vous pouvez ajouter l'attribut `onclick` à votre bouton comme suit :

```html
<body>
  <button onclick="handleClick()">Cliquez-moi !</button>
  <script>

    function handleClick(event) {
      alert('Le bouton est cliqué !');
    }
  </script>
</body>
```

Dans l'élément bouton ci-dessus, nous ajoutons la propriété `onclick` et lui passons la fonction `handleClick()`.

Lorsque nous cliquons sur le bouton, la fonction `handleClick()` sera exécutée.

Vous pouvez également ajouter l'attribut `onclick` en utilisant JavaScript comme suit :

```html
<body>
  <button id="myBtn">Cliquez-moi !</button>
  <script>
    const myBtn = document.querySelector('#myBtn');
    myBtn.onclick = handleClick;

    function handleClick(event) {
      alert('Le bouton est cliqué !');
    }
  </script>
</body>
```

Ici, nous attribuons une référence à la fonction `handleClick` à la propriété `onclick` en utilisant JavaScript.

Pour supprimer l'attribut onclick, vous pouvez attribuer la propriété à null :

```js
const myBtn = document.querySelector('#myBtn');
myBtn.onclick = null;
```

## Lequel devez-vous utiliser ?

Comme vous pouvez le voir, il existe deux façons d'écouter les événements DOM : la méthode `addEventListener()` et l'attribut HTML `on[eventname]`. Lequel devez-vous utiliser ?

La réponse est que la méthode `addEventListener()` peut être utilisée lorsque vous avez besoin de plus d'extensibilité, et que `on[eventname]` peut être utilisé lorsque vous préférez que les choses soient simples.

Lors du développement d'applications web, le fichier `.html` ne doit servir que de structure à la page, tandis que le fichier `.js` doit définir tout comportement que l'application web peut avoir.

Pour rendre votre application plus facile à maintenir et à étendre, JavaScript doit avoir accès aux éléments HTML, mais aucun élément HTML ne doit pouvoir exécuter des fonctions JavaScript. C'est pourquoi `addEventListener()` devrait être la méthode recommandée.

Mais `addEventListener()` ne vient pas sans coût : vous échangez l'extensibilité contre la verbosité, rendant votre code assez encombrant à lire.

Lorsque vous utilisez l'attribut `on[eventname]`, vous n'avez besoin que de spécifier le nom de la fonction dans votre élément HTML :

```html
<body>
  <button onclick="handleClick()">Cliquez-moi !</button>
  <script>

    function handleClick(event) {
      alert('Le bouton est cliqué !');
    }
  </script>
</body>
```

Mais lorsque vous utilisez la méthode `addEventListener()`, vous devez interroger l'élément dont vous avez besoin, appeler la méthode, puis spécifier l'événement et la fonction de rappel à exécuter :

```html
<body>
  <button id="myBtn">Cliquez-moi !</button>
  <script>
    const myBtn = document.querySelector('#myBtn');
    myBtn.addEventListener('click', handleClick);

    function handleClick(event) {
      alert('Le bouton est cliqué !');
    }
  </script>
</body>
```

Comme vous pouvez le voir ci-dessus, il y a deux lignes supplémentaires que vous n'avez pas besoin d'écrire lorsque vous utilisez l'attribut `on[eventname]`.

Bien que cela puisse sembler insignifiant, ce sera un problème sérieux lorsque vous travaillerez sur une application à grande échelle avec de nombreux fichiers HTML et JS.

De plus, la méthode `addEventListener()` vous permet également d'attacher plusieurs écouteurs au même élément comme suit :

```html
<body>
  <button id="myBtn">Cliquez-moi !</button>
  <script>
    const myBtn = document.querySelector('#myBtn');

    myBtn.addEventListener('click', handleClick);

    myBtn.addEventListener('click', handleClickTwo);

    function handleClick() {
      console.log('Exécuté depuis la fonction handleClick');
    }

    function handleClickTwo() {
      console.log('Exécuté depuis la fonction handleClickTwo');
    }
  </script>
</body>
```

Lorsque vous cliquez sur le bouton ci-dessus, JavaScript exécutera les deux écouteurs d'événements.

Cela n'est pas possible avec la propriété `onclick` car vous ne pouvez attribuer qu'une seule fonction comme référence à la fois :

```html
<body>
  <button id="myBtn">Cliquez-moi !</button>
  <script>
    const myBtn = document.querySelector('#myBtn');

    myBtn.onclick = handleClick;
      
    // lorsque vous attribuez une nouvelle fonction à onclick,
    // l'ancienne fonction est écrasée

    myBtn.onclick = handleClickTwo;

    function handleClick() {
      console.log('Exécuté depuis la fonction handleClick');
    }

    function handleClickTwo() {
      console.log('Exécuté depuis la fonction handleClickTwo');
    }
  </script>
</body>
```

Mais je n'ai jamais rencontré de situation où j'avais besoin d'écouter le même événement deux fois, donc cet avantage pourrait ne pas être utile du tout.

## Conclusion

Les événements DOM exposés par le navigateur vous permettent de répondre aux actions de l'utilisateur de manière appropriée.

Ce modèle d'utilisation des écouteurs d'événements pour effectuer des tâches spécifiques est connu sous le nom de programmation pilotée par événements, et vous utiliserez beaucoup ce modèle lors du développement d'une application web en utilisant JavaScript.

Il existe deux façons d'écouter les événements : en utilisant la méthode JavaScript `addEventListener()` et les attributs HTML `on[eventname]`. Chacune a ses avantages et ses inconvénients, il est donc bon d'être familier avec les deux.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://codewithnathan.com/beginning-modern-javascript).

[![](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://codewithnathan.com/beginning-modern-javascript)

Le livre est conçu pour être facile pour les débutants et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application web dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine fois !