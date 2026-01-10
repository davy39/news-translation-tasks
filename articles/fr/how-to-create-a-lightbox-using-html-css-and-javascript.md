---
title: Comment créer une Lightbox avec HTML, CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-26T22:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-lightbox-using-html-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/nikita-kachanovsky-bLY5JqP_Ldw-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment créer une Lightbox avec HTML, CSS et JavaScript
seo_desc: 'Introduction

  A lightbox is a combination of two components, a modal and a slide show. Here you
  will construct a simple lightbox using HTML, CSS and JavaScript.

  The lightbox will be contained in the modal, which will be triggered by some JavaScript,
  f...'
---

### **Introduction**

Une lightbox est une combinaison de deux composants, une [fenêtre modale](https://en.wikipedia.org/wiki/Modal_window) et un diaporama. Ici, vous allez construire une lightbox simple en utilisant `HTML`, `CSS` et `JavaScript`.

La lightbox sera contenue dans la fenêtre modale, qui sera déclenchée par du `JavaScript`, à partir des [gestionnaires d'événements](https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Event_handlers) dans le balisage `HTML`. Vous allez créer des styles qui fourniront un état avec `CSS` et un comportement avec `JavaScript`. Vous trouverez également une liste de référence des méthodes que vous utilisez et d'autres informations utiles liées à ce tutoriel, en bas de page.

#### **Nos Images**

Les images que nous allons utiliser sont fournies par [Pexels](https://www.pexels.com/), une galerie de photos libres de droits qui vous permet de fournir des images de haute qualité à vos projets rapidement, gratuitement et généralement sans attribution nécessaire.

#### **Montrez-moi juste le code !**

Un exemple en direct peut être trouvé [ici - CodePen/Lightbox](https://codepen.io/rdev-rocks/pen/KXNzvo) et un brouillon complet du code est près du bas.

### **Étape 1. Le Balisage**

Le balisage, ou `HTML`, fournit la structure pour la lightbox.

```html
<!-- Voici votre point d'accès pour votre utilisateur, un aperçu des images que vous souhaitez afficher. 
     Vous utilisez le gestionnaire d'événements onclick="" pour exécuter les méthodes que vous allez définir dans le
     JavaScript près du bas -->

<div class="row">
  <div class="col">
     <img src="https://static.pexels.com/photos/385997/pexels-photo-385997.jpeg" onclick="openLightbox();toSlide(1)" class="hover-shadow preview" alt="Voiture jouet sur la route." />
  </div>
  <div class="col">
     <img src="https://static.pexels.com/photos/574521/pexels-photo-574521.jpeg" onclick="openLightbox();toSlide(2)" class="hover-shadow preview" alt="Voiture jouet explorant hors route." />
  </div>
  <div class="col">
     <img src="https://static.pexels.com/photos/386009/pexels-photo-386009.jpeg" onclick="openLightbox();toSlide(3)" class="hover-shadow preview" alt="Voiture jouet dans la ville." />
  </div>
</div>

<!-- Voici votre lightbox, elle est contenue dans une fenêtre modale. Ici, vous fournissez toutes les images,
     les contrôles et un autre ensemble d'images d'aperçu sous forme de points. Les points montrent à votre utilisateur
     quelle image est actuellement active. Notez que vous utilisez des entités (par exemple, &times;), plus d'informations
     à leur sujet en bas. -->
     
<div id="Lightbox" class="modal">
  <span class="close pointer" onclick="closeLightbox()">&times;</span>
  <div class="modal-content">
    <div class="slide">
        <img src="https://static.pexels.com/photos/385997/pexels-photo-385997.jpeg" class="image-slide" alt="Voiture jouet sur la route." />
    </div>
    <div class="slide">
        <img src="https://static.pexels.com/photos/574521/pexels-photo-574521.jpeg" class="image-slide" alt="Voiture jouet explorant hors route." />
    </div>    
    <div class="slide">
        <img src="https://static.pexels.com/photos/386009/pexels-photo-386009.jpeg" class="image-slide" alt="Voiture jouet dans la ville." />
    </div>
  
    <a class="previous" onclick="changeSlide(-1)">&#10094;</a>
    <a class="next" onclick="changeSlide(1)">&#10095;</a>
  
    <div class="dots">
      <div class="col">
        <img src="https://static.pexels.com/photos/385997/pexels-photo-385997.jpeg" class="modal-preview hover-shadow" onclick="toSlide(1)" alt="Voiture jouet sur la route" />
      </div>
      <div class="col">
        <img src="https://static.pexels.com/photos/574521/pexels-photo-574521.jpeg" class="modal-preview hover-shadow" onclick="toSlide(2)" alt="Voiture jouet explorant hors route." />
      </div>
      <div class="col">
        <img src="https://static.pexels.com/photos/386009/pexels-photo-386009.jpeg" class="modal-preview hover-shadow" onclick="toSlide(3)" alt="Voiture jouet dans la ville." />
      </div>
    </div>
  </div>
</div>
```

### **Étape 2. Style avec CSS**

Le `CSS` vous fournit différents états pour votre lightbox. Des choses comme la visibilité, le positionnement et les effets de survol.

Votre feuille de style devrait ressembler à ceci :

```css
/* Ici, vous fournissez une "réinitialisation" des bonnes pratiques, lisez plus à ce sujet en bas ! :) */

html {
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}

body {
  margin: 0;
}

/* Vous définissez le style de vos aperçus ici, vous utilisez flex pour afficher les images 
   "de manière responsive". */

.preview {
  width: 100%;
}

.row {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.row > .col {
  padding: 0 8px;
}

.col {
  float: left;
  width: 25%;
}

/* Maintenant, vous voulez définir à quoi ressemblera la lightbox. Notez que vous avez le display
   à none. Vous ne voulez pas qu'elle s'affiche jusqu'à ce que l'utilisateur clique sur l'un des aperçus. 
   Vous allez changer cette propriété d'affichage avec JavaScript ci-dessous. */
   
.modal {
  display: none;
  position: fixed;
  z-index: 1;
  padding: 10px 62px 0px 62px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: black;
}

.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
  padding: 0 0 0 0;
  width: 80%;
  max-width: 1200px;
}

/* Même chose avec vos diapositives, vous définissez l'affichage à none, car vous voulez choisir laquelle 
   est affichée à la fois. */

.slide {
  display: none;
}

.image-slide {
  width: 100%;
}

.modal-preview {
  width: 100%;
}

.dots {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

/* Vous voulez que les aperçus soient un peu transparents pour montrer qu'ils sont "inactifs". 
   Vous ajoutez ensuite une classe .active ou :hover pour animer les sélections pour votre utilisateur lorsqu'
   il interagit avec vos contrôles et votre contenu cliquable.
 */

img.preview, img.modal-preview {
  opacity: 0.6;
}

img.active,
.preview:hover,
.modal-preview:hover {
  opacity: 1;
}

img.hover-shadow {
  transition: 0.3s;
}

.hover-shadow:hover {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
} 

.close {
  color: white;
  position: absolute;
  top: 10px;
  right: 25px;
  font-size: 35px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #999;
  text-decoration: none;
  cursor: pointer;
}

.previous,
.next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -50px;
  color: white;
  font-weight: bold;
  font-size: 20px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
  -webkit-user-select: none;
}

.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

.previous:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}
```

### **Étape 3. JavaScript**

Maintenant, passons aux choses sérieuses ! Votre JavaScript devrait ressembler à ceci :

```javascript
// Initialisez ici et exécutez showSlide() pour donner un état par défaut à votre lightbox.

let slideIndex = 1;
showSlide(slideIndex);

// Vous fournissez la fonctionnalité pour votre contenu cliquable, qui est 
// vos aperçus, points, contrôles et le bouton de fermeture.

function openLightbox() {
  document.getElementById('Lightbox').style.display = 'block';
}

function closeLightbox() {
  document.getElementById('Lightbox').style.display = 'none';
};

// Notez que vous attribuez de nouvelles valeurs ici à notre slideIndex.

function changeSlide(n) {
  showSlide(slideIndex += n);
};

function toSlide(n) {
  showSlide(slideIndex = n);
};

// Voici la logique de votre lightbox. Elle décidera quelle diapositive afficher 
// et quel point est actif.

function showSlide(n) {
  const slides = document.getElementsByClassName('slide');
  let modalPreviews = document.getElementsByClassName('modal-preview');

  if (n > slides.length) {
    slideIndex = 1;	
  };
  
  if (n < 1) {
    slideIndex = slides.length;
  };

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  };
  
  for (let i = 0; i < modalPreviews.length; i++) {
    modalPreviews[i].className = modalPreviews[i].className.replace(' active', '');
  };
  
  slides[slideIndex - 1].style.display = 'block';
  modalPreviews[slideIndex - 1].className += ' active';
};
```

Et voilà ! Maintenant, assemblez tout le code. Vous devriez maintenant avoir une lightbox fonctionnelle.

### **Tout le Code**

```html
<body>
  <style>
    html {
      box-sizing: border-box;
    }
    
    *, *:before, *:after {
      box-sizing: inherit;
    }
    
    body {
      margin: 0;
    }
    
    .preview {
      width: 100%;
    }
    
    .row {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
    
    .row > .col {
      padding: 0 8px;
    }
    
    .col {
      float: left;
      width: 25%;
    }
    
    .modal {
      display: none;
      position: fixed;
      z-index: 1;
      padding: 10px 62px 0px 62px;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: black;
    }
    
    .modal-content {
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: center;
      margin: auto;
      padding: 0 0 0 0;
      width: 80%;
      max-width: 1200px;
    }
    
    .slide {
      display: none;
    }
    
    .image-slide {
    	width: 100%;
    }
    
    .modal-preview {
    	width: 100%;
    }
    
    .dots {
    	display: flex;
    	flex-direction: row;
    	justify-content: space-between;
    }
    
    img.preview, img.modal-preview {
      opacity: 0.6;
    }
    
    img.active,
    .preview:hover,
    .modal-preview:hover {
      opacity: 1;
    }
    
    img.hover-shadow {
      transition: 0.3s;
    }
    
    .hover-shadow:hover {
      box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    } 
    
    .close {
      color: white;
      position: absolute;
      top: 10px;
      right: 25px;
      font-size: 35px;
      font-weight: bold;
    }
    
    .close:hover,
    .close:focus {
      color: #999;
      text-decoration: none;
      cursor: pointer;
    }
    
    .previous,
    .next {
      cursor: pointer;
      position: absolute;
      top: 50%;
      width: auto;
      padding: 16px;
      margin-top: -50px;
      color: white;
      font-weight: bold;
      font-size: 20px;
      transition: 0.6s ease;
      border-radius: 0 3px 3px 0;
      user-select: none;
      -webkit-user-select: none;
    }
    
    .next {
      right: 0;
      border-radius: 3px 0 0 3px;
    }
    
    .previous:hover,
    .next:hover {
      background-color: rgba(0, 0, 0, 0.8);
    }
  </style>
  <div class="row">
    <div class="col">
       <img src="https://static.pexels.com/photos/385997/pexels-photo-385997.jpeg" onclick="openLightbox();toSlide(1)" class="hover-shadow preview" alt="Voiture jouet sur la route." />
    </div>
    <div class="col">
       <img src="https://static.pexels.com/photos/574521/pexels-photo-574521.jpeg" onclick="openLightbox();toSlide(2)" class="hover-shadow preview" alt="Voiture jouet explorant hors route." />
    </div>
    <div class="col">
       <img src="https://static.pexels.com/photos/386009/pexels-photo-386009.jpeg" onclick="openLightbox();toSlide(3)" class="hover-shadow preview" alt="Voiture jouet dans la ville" />
    </div>
  </div>
  
  <div id="Lightbox" class="modal">
  
    <span class="close pointer" onclick="closeLightbox()">&times;</span>
    <div class="modal-content">
      <div class="slide">
        <img src="https://static.pexels.com/photos/385997/pexels-photo-385997.jpeg" class="image-slide" alt="Voiture jouet sur la route." />
      </div>
      <div class="slide">
        <img src="https://static.pexels.com/photos/574521/pexels-photo-574521.jpeg" class="image-slide" alt="Voiture jouet explorant hors route." />
      </div>    
      <div class="slide">
        <img src="https://static.pexels.com/photos/386009/pexels-photo-386009.jpeg" class="image-slide" alt="Voiture jouet dans la ville." />
      </div>
    
      <a class="previous" onclick="changeSlide(-1)">&#10094;</a>
      <a class="next" onclick="changeSlide(1)">&#10095;</a>
          
      <div class="dots">
        <div class="col">
          <img src="https://static.pexels.com/photos/385997/pexels-photo-385997.jpeg" class="modal-preview hover-shadow" onclick="toSlide(1)" alt="Voiture jouet sur la route." />
        </div>
        <div class="col">
          <img src="https://static.pexels.com/photos/574521/pexels-photo-574521.jpeg" class="modal-preview hover-shadow" onclick="toSlide(2)" alt="Voiture jouet explorant hors route." />
        </div>
        <div class="col">
          <img src="https://static.pexels.com/photos/386009/pexels-photo-386009.jpeg" class="modal-preview hover-shadow" onclick="toSlide(3)" alt="Voiture jouet dans la ville" />
        </div>
      </div>
    </div> 
  </div>
  
  <script>
    let slideIndex = 1;
    showSlide(slideIndex);
    
    function openLightbox() {
      document.getElementById('Lightbox').style.display = 'block';
    };
    
    function closeLightbox() {
      document.getElementById('Lightbox').style.display = 'none';
    };
    
    function changeSlide(n) {
      showSlide(slideIndex += n);
    };
    
    function toSlide(n) {
      showSlide(slideIndex = n);
    };
    
    function showSlide(n) {
      const slides = document.getElementsByClassName('slide');
      let modalPreviews = document.getElementsByClassName('modal-preview');
    
      if (n > slides.length) {
        slideIndex = 1;	
      };
      
      if (n < 1) {
        slideIndex = slides.length;
      };
    
      for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
      };
      
      for (let i = 0; i < modalPreviews.length; i++) {
        modalPreviews[i].className = modalPreviews[i].className.replace(' active', '');
      };
      
      slides[slideIndex - 1].style.display = 'block';
      modalPreviews[slideIndex - 1].className += ' active';
    };
  </script>
</body>
```

### **Plus d'Informations :**

#### **HTML**

[Fenêtre modale](https://en.wikipedia.org/wiki/Modal_window) - Une fenêtre pop-up

[Gestionnaires d'événements](https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Event_handlers) - Propriétés HTML qui écoutent les événements utilisateur.

[Entité](https://developer.mozilla.org/en-US/docs/Glossary/Entity) - Une chaîne qui représente un caractère réservé en HTML.

#### **CSS**

[box-sizing:](https://css-tricks.com/box-sizing/) - Une propriété CSS3 qui contrôle la manière dont le navigateur rend le contenu en fonction de la hauteur et de la largeur.

[Flex-box](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox) - Une nouvelle technologie qui aide à positionner le contenu HTML de manière responsive.

[:hover](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover) - Un pseudo-sélecteur qui est déclenché lorsque l'utilisateur survole un élément lorsque cette classe lui est assignée.

#### **JavaScript**

[let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) - Une variable à portée de bloc.

[const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) - Une constante à portée de bloc.

[getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) - Une méthode de document qui retourne une référence à un élément HTML.

[getElementsByClassName()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName) - Une méthode de document qui retourne un tableau de références au HTML ayant des classes correspondantes.

[+=](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment_Operators) - Un opérateur d'assignation qui ajoutera des nombres ou concaténera des chaînes.

#### **Ressources :**

[Exemple en direct](https://codepen.io/rdev-rocks/pen/KXNzvo?editors=1111) - Un CodePen qui démontre le code ci-dessus.

[Flex-Box Interactive](https://codepen.io/enxaneta/full/adLPwv) - Un CodePen interactif qui montre le comportement de flex-box.

[Pexels](https://www.pexels.com/) - Une galerie de photos libres de droits.

[MDN](https://developer.mozilla.org/en-US/) - Un excellent endroit pour des informations sur le web.

[W3School - Lightbox](https://www.w3schools.com/howto/howto_js_lightbox.asp) - Ce code a été inspiré d'ici. Merci W3Schools !