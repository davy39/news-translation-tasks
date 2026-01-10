---
title: Comment créer un diaporama avec HTML, CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-slideshow
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e44740569d1a4ca3c37.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment créer un diaporama avec HTML, CSS et JavaScript
seo_desc: "A web slideshow is a sequence of images or text that consists of showing\
  \ one element of the sequence in a certain time interval.\nFor this tutorial you\
  \ can create a slideshow by following these simple steps:\nWrite some markup\n \
  \ <!DOCTYPE html>\n  <html..."
---

Un diaporama web est une séquence d'images ou de texte qui consiste à afficher un élément de la séquence à intervalles de temps réguliers.

Pour ce tutoriel, vous pouvez créer un diaporama en suivant ces étapes simples :

### **Écrire le balisage**

```html
  <!DOCTYPE html>
  <html lang="fr">
    <head>
      <meta charset="UTF-8">
      <title>Diaporama</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <div id="slideshow-example" data-component="slideshow">
        <div role="list">
          <div class="slide">
            <img src="" alt="">
          </div>
          <div class="slide">
            <img src="" alt="">
          </div>
          <div class="slide">
            <img src="" alt="">
          </div>
        </div>
      </div>
    <script src="slideshow.js"></script>
    </body>
  </html>
```

## Écrire les styles pour masquer les diapositives et n'en afficher qu'une seule

Pour masquer les diapositives, vous devez leur donner un style par défaut. Cela dictera que vous n'affichez qu'une seule diapositive si elle est active ou si vous souhaitez l'afficher.

```css
  [data-component="slideshow"] .slide {
    display: none;
  }

  [data-component="slideshow"] .slide.active {
    display: block;
  }
```

## Changer les diapositives à intervalles de temps réguliers

La première étape pour changer les diapositives affichées consiste à sélectionner le ou les conteneurs de diapositives, puis leurs diapositives.

Lorsque vous sélectionnez les diapositives, vous devez parcourir chaque diapositive et ajouter ou supprimer une classe active en fonction de la diapositive que vous souhaitez afficher. Ensuite, il suffit de répéter le processus à intervalles de temps réguliers.

Gardez à l'esprit que lorsque vous supprimez une classe active d'une diapositive, vous la masquez en raison des styles définis dans l'étape précédente. Mais lorsque vous ajoutez une classe active à la diapositive, vous écrasez le style `display:none` par `display:block`, de sorte que la diapositive s'affichera pour les utilisateurs.

```js
  var slideshows = document.querySelectorAll('[data-component="slideshow"]');
  
  // Appliquer à tous les diaporamas que vous définissez avec le balisage écrit
  slideshows.forEach(initSlideShow);

  function initSlideShow(slideshow) {

    var slides = document.querySelectorAll(`#${slideshow.id} [role="list"] .slide`); // Obtenir un tableau de diapositives

    var index = 0, time = 5000;
    slides[index].classList.add('active');  
    
    setInterval( () => {
      slides[index].classList.remove('active');
      
      // Parcourir chaque diapositive en incrémentant l'index
      index++;
      
      // Si vous avez parcouru toutes les diapositives, réinitialiser l'index pour afficher la première diapositive et recommencer
      if (index === slides.length) index = 0; 
      
      slides[index].classList.add('active');

    }, time);
  }
```

#### **[Exemple Codepen suivant ce tutoriel](https://codepen.io/AndresUris/pen/rGXpvE)**