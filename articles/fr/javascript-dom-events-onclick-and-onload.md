---
title: 'Événements DOM JavaScript : Onclick et Onload'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T22:43:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-dom-events-onclick-and-onload
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dab740569d1a4ca38fa.jpg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_title: 'Événements DOM JavaScript : Onclick et Onload'
seo_desc: 'In the early days of the internet, web pages were truly static – there
  were only text and images. Sure, sometimes that image was an animated gif, but it
  was still just an image.

  With the advent of JavaScript, it became increasingly possible to create...'
---

Dans les premiers jours d'Internet, les pages web étaient vraiment statiques – il n'y avait que du texte et des images. Bien sûr, parfois cette image était un gif animé, mais c'était toujours juste une image.

Avec l'avènement de JavaScript, il est devenu de plus en plus possible de créer des pages interactives qui répondraient à des actions comme cliquer sur un bouton ou avoir une animation de défilement.

Il existe un certain nombre d'événements DOM (Document Object Model) que vous pouvez écouter en JavaScript, mais `onclick` et `onload` sont parmi les plus courants.

## **Événement Onclick**

L'événement `onclick` en JavaScript vous permet d'exécuter une fonction lorsqu'un élément est cliqué.

### **Exemple**

```javascript
<button onclick="myFunction()">Cliquez-moi</button>

<script>
  function myFunction() {
    alert('Le bouton a été cliqué !');
  }
</script>
```

Dans l'exemple simple ci-dessus, lorsqu'un utilisateur clique sur le bouton, il verra une alerte dans son navigateur affichant `Le bouton a été cliqué !`.

### **Ajout dynamique de `onclick`**

L'exemple ci-dessus fonctionne, mais est généralement considéré comme une mauvaise pratique. Au lieu de cela, il est préférable de séparer le contenu de la page (HTML) de la logique (JS).

Pour ce faire, l'événement `onclick` peut être ajouté par programmation à n'importe quel élément en utilisant le code suivant dans l'exemple suivant :

```javascript
<p id="foo">cliquez sur cet élément.</p>

<script>
  const p = document.getElementById("foo"); // Trouver l'élément paragraphe dans la page
  p.onclick = showAlert; // Ajouter la fonction onclick à l'élément
    
  function showAlert(event) {
    alert("Événement onclick déclenché !");
  }
</script>
```

### **Note**

Il est important de noter qu'en utilisant `onclick`, nous ne pouvons ajouter qu'une seule fonction d'écoute. Si vous souhaitez en ajouter plus, utilisez simplement `addEventListener()`, qui est la méthode préférée pour ajouter des événements.

Dans l'exemple ci-dessus, lorsqu'un utilisateur clique sur l'élément `paragraph` dans le `html`, il verra une alerte affichant `Événement onclick déclenché`.

### **Empêcher l'action par défaut**

Cependant, si nous attachons `onclick` à des liens (la balise `a` de HTML), nous pourrions vouloir empêcher l'action par défaut de se produire :

```javascript
<a id="bar" href="https://guide.freecodecamp.org">Guides</a>

<script>
  const link = document.getElementById("bar"); // Trouver l'élément lien
  link.onclick = myAlert; // Ajouter la fonction onclick à l'élément

  function myAlert(event) {
    event.preventDefault();
    alert("Le lien a été cliqué mais la page ne s'est pas ouverte");
  }
</script>
```

Dans l'exemple ci-dessus, nous avons empêché le comportement par défaut de l'élément `a` (ouvrir le lien) en utilisant `event.preventDefault()` à l'intérieur de notre fonction de rappel `onclick`.

## **Événement Onload**

L'événement `onload` est utilisé pour exécuter une fonction JavaScript immédiatement après qu'une page a été chargée.

### **Exemple :**

```javascript
const body = document.body;
body.onload = myFunction;

function myFunction() {
  alert('La page a fini de charger');
}

```

Ce qui peut être raccourci en :

```js
document.body.onload = function() {
  alert('La page a fini de charger');
}

```

Dans l'exemple ci-dessus, dès que la page web a été chargée, la fonction `myFunction` sera appelée, montrant l'alerte `La page a fini de charger` à l'utilisateur.

L'événement `onload` est généralement attaché à l'élément `<body>`. Ensuite, une fois que le `<body>` de la page a été chargé, ce qui inclut toutes les images, et les fichiers CSS et JS, votre script s'exécutera.

#### **Plus d'informations :**

Ce ne sont là que deux des nombreux événements DOM que vous pouvez manipuler avec JavaScript, mais ils sont parmi les plus couramment utilisés.

Mais parfois, vous n'avez pas besoin d'écouter les événements DOM du tout, et vous voulez utiliser un événement basé sur le temps comme un compte à rebours. Pour un tutoriel rapide sur les événements de timing, consultez [cet article](https://www.freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval).