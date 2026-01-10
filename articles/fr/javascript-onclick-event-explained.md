---
title: Événement Onclick en JavaScript Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-14T20:01:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-onclick-event-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb2740569d1a4ca3e93.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Événement Onclick en JavaScript Expliqué
seo_desc: "The onclick event in JavaScript lets you as a programmer execute a function\
  \ when an element is clicked.\nButton Onclick Example\n<button onclick=\"myFunction()\"\
  >Click me</button>\n\n<script>\n  function myFunction() {\n    alert('Button was\
  \ clicked!');\n  }\n..."
---

L'événement `onclick` en JavaScript permet au programmeur d'exécuter une fonction lorsqu'un élément est cliqué.

## Exemple de Bouton Onclick

```javascript
<button onclick="myFunction()">Cliquez ici</button>

<script>
  function myFunction() {
    alert('Le bouton a été cliqué !');
  }
</script>
```

Dans l'exemple simple ci-dessus, lorsqu'un utilisateur clique sur le bouton, il verra une alerte dans son navigateur affichant `Le bouton a été cliqué !`.

## Ajout dynamique de onclick

L'événement `onclick` peut également être ajouté par programmation à n'importe quel élément en utilisant le code suivant dans l'exemple ci-dessous :

```javascript
<p id="foo">cliquez sur cet élément.</p>

<script>
  var p = document.getElementById("foo"); // Trouver l'élément paragraphe dans la page
  p.onclick = showAlert; // Ajouter la fonction onclick à l'élément
    
  function showAlert(event) {
    alert("Événement onclick déclenché !");
  }
</script>
```

### **Note**

Il est important de noter qu'avec onclick, nous ne pouvons ajouter qu'une seule fonction d'écoute. Si vous souhaitez en ajouter plusieurs, utilisez simplement addEventListener(), qui est la méthode préférée pour ajouter des écouteurs d'événements.

Dans l'exemple ci-dessus, lorsqu'un utilisateur clique sur l'élément `paragraph` dans le `html`, il verra une alerte affichant `Événement onclick déclenché`.

## Empêcher l'action par défaut

Cependant, si nous attachons `onclick` à des liens (la balise `a` de HTML), nous pourrions vouloir empêcher l'action par défaut de se produire :

```javascript
<a href="https://guide.freecodecamp.org" onclick="myAlert()">Guides</a>

<script>
  function myAlert(event) {
    event.preventDefault();
    alert("Le lien a été cliqué mais la page ne s'est pas ouverte");
  }
</script>
```

Dans l'exemple ci-dessus, nous avons empêché le comportement par défaut de l'élément `a` (ouvrir le lien) en utilisant `event.preventDefault()` à l'intérieur de notre fonction de rappel `onclick`.

[MDN](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onclick)

### Autres Ressources

[jQuery .on() Event Handler Attachment](https://api.jquery.com/on/)