---
title: Comment gérer la gestion des événements en JavaScript (exemples et tout)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-19T18:14:18.000Z'
originalURL: https://freecodecamp.org/news/event-handling-in-javascript-with-examples-f6bc1e2fff57
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dhtbZon7OPebZuUO9-yyjw.jpeg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment gérer la gestion des événements en JavaScript (exemples et tout)
seo_desc: 'By Honey Thakuria

  In this blog, I will try to make clear the fundamentals of the event handling mechanism
  in JavaScript, without the help of any external library like Jquery/React/Vue.

  I will be explaining the following topics in this article:


  The d...'
---

Par Honey Thakuria

Dans ce blog, je vais essayer de clarifier les fondamentaux du mécanisme de gestion des événements en JavaScript, sans l'aide d'une bibliothèque externe comme Jquery/React/Vue.

Je vais expliquer les sujets suivants dans cet article :

1. Les objets **document** et **window**, et l'ajout d'**Event Listeners** à ceux-ci.
2. La méthode **Event.preventDefault()** et son utilisation.
3. La méthode **Event.stopPropagation()** avec un exemple.
4. **Comment supprimer** un event **listener** d'un élément.

### Les objets **document** et **window** avec **Event Listeners**

L'objet Window représente l'onglet. Si vous lisez ce blog sur votre navigateur, alors votre onglet actuel représente l'objet Window.

L'objet window a accès à des informations telles que la barre d'outils, la hauteur et la largeur de la fenêtre, les invites et les alertes. Voyons comment nous pouvons ajouter un écouteur d'événement (mousedown) à l'objet window et analyser certaines de ses propriétés.

#### **Comment ajouter l'écouteur sur l'objet window**

La méthode **addEventListener** est la manière préférée d'ajouter un écouteur d'événement à **window**, **document** ou tout autre **élément** dans le DOM.

Il existe une autre méthode appelée "on" propriété onclick, onmouseover, etc. Mais elle n'est pas aussi utile, car elle ne permet pas d'ajouter plusieurs écouteurs d'événements sur le même élément. Les autres méthodes le permettent.

Un objet **event** est passé en argument (optionnel) au gestionnaire qui contient toutes les informations liées à l'événement (dans notre cas, mousedown) sur la fenêtre.

Ouvrez les outils de développement (Inspecter l'élément) sur cette page et copiez-collez le code suivant dans le panneau de la console et appuyez sur Entrée.

```js
window.addEventListener("mousedown",function(event){
 alert("window");
 console.log(event);
});
```

Après cela, vous pouvez aller dans n'importe quelle section de l'onglet actuel et **cliquer droit** pour voir la console et les informations liées à cet événement, comme montré ci-dessous dans la capture d'écran.

**Note** : Si vous allez dans un autre onglet et cliquez droit, alors cet événement ne sera pas déclenché car il appartient uniquement à cet onglet (objet Window).

![Image](https://cdn-media-1.freecodecamp.org/images/OkOuvlALsx7sPyDl7NJ2AfcjV7yCSoVpN2TK)

#### Les détails de l'événement mousedown

Dans les lignes suivantes, je vais expliquer certaines des propriétés importantes capturées correspondant à l'événement **mousedown** que nous venons de réaliser.

**button** : Comme il s'agissait de l'événement mousedown, il vous indiquera le bouton que vous avez cliqué. Pour la souris, les boutons gauche, milieu et droit correspondent respectivement à 0, 1 et 2. Si vous cliquez sur le bouton droit, vous pouvez voir la valeur 2.

**clientX** et **clientY** : Position relative par rapport au coin supérieur gauche de la zone de contenu (Viewport). Analysez simplement la valeur de ces propriétés avec l'endroit où vous avez cliqué, et vous pouvez voir comment elles sont liées. Même si vous faites défiler la page vers le bas, ces propriétés restent les mêmes. ScreenX et ScreenY font référence au coin supérieur gauche de l'écran (moniteur).

**altkey / ctrlkey** : Si vous gardez l'une de ces touches enfoncée pendant que vous effectuez votre opération de clic droit, alors vous pouvez voir que ces valeurs sont vraies. Sinon, elles sont fausses comme dans notre cas.

**target** : Il correspond à l'élément sur lequel vous avez effectué l'action. Quel que soit l'élément sur lequel vous avez cliqué, vous pouvez voir les informations correspondant à cette propriété dans la console.

#### **Qu'est-ce qu'un objet document** ?

Le document contient ce qui se trouve à l'intérieur de la fenêtre interne. L'objet **document** est la racine de chaque nœud dans le DOM. Si vous chargez une page HTML dans le navigateur, alors le document représente cette page entière.

### La méthode **Event.preventDefault()** et son utilisation

Parfois, nous ne voulons pas qu'un élément HTML se comporte de la manière dont il est censé se comporter par défaut. Dans un tel cas, nous pouvons utiliser cette méthode.

**Exemple** : Cliquer sur l'élément d'ancrage fera rediriger le navigateur vers cette page par défaut. Essayons d'éviter cela.

```html
<html>

<body>

  <a href="https://google.com/">Google</a>

  <script>
    let link = document.querySelector("a"); // C'est la méthode pour accéder au premier élément correspondant
    link.addEventListener("click", function(event) {
      console.log("Redirection arrêtée");
      event.preventDefault();
    });
  </script>
</body>

</html>
```

Vous pouvez créer un fichier HTML et vérifier ce code.

### La méthode **Event.stopPropagation()**

**Les événements se propagent vers l'extérieur.** Il existe certains cas, comme lorsque vous avez des éléments imbriqués et que vous effectuez un événement sur un enfant et qu'il finit par effectuer une action sur le parent également, que vous souhaitez éviter. Dans de tels cas, cette méthode est utile.

Cela semble un peu confus, mais j'espère que l'exemple ci-dessous vous éclairera.

Imaginez que vous avez un bouton à l'intérieur d'un paragraphe et que vous avez attaché un événement mousedown aux deux. Vous souhaitez réaliser les cas d'utilisation suivants :

1. Si vous cliquez droit sur le bouton, alors il devrait montrer qu'il a été cliqué et ne pas se propager à l'élément parent (c'est-à-dire le paragraphe).
2. Si vous cliquez gauche sur le bouton, alors il devrait se propager vers l'extérieur normalement et déclencher également l'écouteur d'événement du paragraphe.

Solution :

```html
<html>

<body>
  <p id="demo"> Hello Ho<button id="button12"> Button2 </button> </p>
  <script>
    // Écouteur d'événement sur le bouton et sa logique
    document.getElementById("button12").addEventListener("mousedown", function(event) {
      alert("bouton cliqué");
      if (event.button == 2) // Clic droit
        event.stopPropagation();
    });
    // Écouteur d'événement sur l'élément paragraphe avec sa logique :
    document.getElementById("demo").addEventListener("mousedown", function(event) {
      alert("Paragraphe cliqué");
    });
  </script>
</body>

</html>
```

### **Suppression** d'un **event listener** d'un élément

Pour supprimer un écouteur d'événement d'un élément, nous devons appeler la méthode **removeEventListener** avec le nom de l'événement et le nom de la fonction.

**Note** : lorsque des fonctions anonymes sont passées, elles n'ont pas de mappage mémoire. Nous devons donc définir ces fonctions à l'extérieur du rappel et les référencer ici dans le rappel removeEventListener.

```js
Document.getElementbyId("id_name").removeEventListener("click",fn_name)
```

Si vous avez atteint ce point, vous devriez avoir une compréhension décente de la manière dont les Event Listeners fonctionnent en JavaScript.

Si, en travaillant avec votre bibliothèque/Framework préféré, vous êtes bloqué dans la partie Gestion des Événements, alors ces bases devraient vous aider à résoudre le problème.