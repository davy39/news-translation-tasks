---
title: Comment créer une navbar responsive avec un menu basculant en utilisant Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T10:44:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-responsive-navbar-with-a-toggle-menu-using-flexbox-3438e1d08783
coverImage: https://cdn-media-1.freecodecamp.org/images/0*duHsALHgV9KMBanO.
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer une navbar responsive avec un menu basculant en utilisant
  Flexbox
seo_desc: 'By Charlie Waite

  During a recent project, my team had to remove all traces of Bootstrap. This meant
  the extremely useful responsive navbar was going to have to be created from scratch.
  I’m relatively new to CSS, and have always relied on Bootstrap na...'
---

Par Charlie Waite

Lors d'un projet récent, mon équipe a dû supprimer toutes les traces de Bootstrap. Cela signifiait que la navbar responsive extrêmement utile devait être créée à partir de zéro. Je suis relativement nouveau en CSS et j'ai toujours compté sur les navbars de Bootstrap pour leur simplicité, alors je me suis porté volontaire pour cette tâche. Voici ce que j'ai appris et fait tout au long du processus.

Dans cet article, je supposerai que vous avez des connaissances de base en HTML, CSS et JavaScript — vous savez comment lier une feuille de style à votre HTML ou appliquer les styles dans une balise `<style>` — et vous savez comment importer un fichier JavaScript dans votre page.

_J'ai eu des élitistes défensifs critiquer ma façon de faire les choses, surtout avec le menu basculant étant `position: absolute` — si vous avez de meilleures façons de faire cela, alors s'il vous plaît répondez ci-dessous et nous pouvons améliorer cela pour les milliers de personnes qui le lisent !_

### Commencer

Tout d'abord, j'ai commencé avec un peu de HTML basique pour la mise en page :

```html
<div class="Navbar">
  <div class="Navbar__Link Navbar__Link-brand">
    Titre du site
  </div>
  <div class="Navbar__Link">
    Lien
  </div>
  <div class="Navbar__Link">
    Lien
  </div>
  <div class="Navbar__Link">
    Lien
  </div>
  <div class="Navbar__Link">
    Lien
  </div>
  <div class="Navbar__Link">
    Lien
  </div>
</div>
```

Vous pouvez utiliser n'importe quelle convention de nommage pour les classes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3tYOXMsOAdUXGmcXmOt50g.png)

Maintenant, cela ne nous donne pas encore grand-chose. Ce n'est qu'une simple liste d'éléments. Mais avec une seule ligne de CSS, nous voyons la puissance de Flexbox.

```css
.Navbar {
  display: flex;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*dK5IrDcMRW00HPZ-wX6cBw.png)
_Les divs de la navbar sont maintenant alignées horizontalement_

Une ligne de code, et nous avons déjà nos éléments de navigation alignés horizontalement en haut de la page.

Maintenant, ajoutons deux éléments `nav` à notre HTML afin que nous puissions avoir certains éléments à gauche et à droite de la navbar :

```html
<div class="Navbar">
  <nav class="Navbar__Items">
    <div class="Navbar__Link Navbar__Link-brand">
      Titre du site
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
  </nav>
  <nav class="Navbar__Items Navbar__Items--right">
    <div class="Navbar__Link">
      Lien
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
  </nav>
</div>
```

Et un peu de style basique sur notre classe `Navbar` qui enveloppe tous les autres éléments :

```css
.Navbar {
  background-color: #46ACC2;
  display: flex;
  padding: 16px;
  font-family: sans-serif;
  color: white;
}
```

Bien sûr, vous pouvez choisir votre propre schéma de couleurs, police et remplissage.

Maintenant, notre navbar ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ulTsKdXWB72DtxfDLuzl9A.png)

Oups, maintenant cela a l'air un peu mieux, mais nous ne pouvons pas avoir nos éléments de navigation affichés verticalement. Avant de continuer, essayez de deviner ce que nous allons faire ensuite...

Maintenant, notre `display:flex` dans la classe `.Navbar` n'est plus responsable de ces éléments. Il est maintenant responsable de leurs conteneurs `<nav>`. Nous voulons que les deux soient alignés horizontalement.

Alors, nous changeons aussi la classe `.Navbar__Items` :

```css
.Navbar__Items {
  display:flex;
}
```

Maintenant, ajoutons un peu de remplissage à nos liens pour rendre cela un peu plus joli :

```css
.Navbar__Link {
  padding-right: 8px;
}
```

Maintenant, notre navbar ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DTgVCsT7tQlQ5Qgk5mQpSQ.png)

Nous y arrivons. Mais nous voulons aussi que le deuxième `<nav>` soit aligné à droite. Comme vous l'avez peut-être remarqué — j'ai ajouté une classe supplémentaire à la deuxième balise `<nav>` .Navbar__Items--right.

Ajoutons simplement un `margin-left:auto` à cette classe :

```css
.Navbar__Items--right {
  margin-left:auto;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*wDWAi7RCETK64FeP4yLNEA.png)
_Après avoir ajouté le margin-left au deuxième nav_

![Image](https://cdn-media-1.freecodecamp.org/images/1*wzj25OyMsvenI7APSxBDCg.png)
_Sur mobile_

Comme vous pouvez le voir, c'est maintenant beaucoup mieux. Nous avons déjà une navbar entièrement responsive. Mais...

Que se passe-t-il si chaque élément de navigation avait un texte plus long ? Que se passe-t-il s'il y avait plus d'éléments ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*TRNh6xHheH7t5I3sUxLI0A.png)
_Exemple de noms de liens plus longs_

Comme vous pouvez le voir, ce n'est pas ce que nous voulons. Nous voulons soit rendre tous les éléments de navigation sur une seule ligne pour la cohérence, soit les ranger dans un menu que l'utilisateur peut basculer.

Nous opterons pour cette dernière solution, car elle est beaucoup plus propre et nous n'aurons pas à nous soucier de l'utilisateur ayant du mal à lire le texte de chaque élément de navigation.

### `flex-direction`

Avec un élément dont l'affichage est flex, il existe également une règle pour la direction dans laquelle nous voulons que les éléments s'alignent. Par défaut, c'est `row`, qui aligne tous les éléments soigneusement le long de l'axe des x.

Dans notre cas, nous aimerions un petit menu vertical en haut de notre page. Essayons de changer la `flex-direction` sur `.Navbar` et `.Navbar__Items` en `column` — cela aligne tous les éléments du menu le long de l'axe des y — lorsque la largeur de l'écran est de 768px ou moins.

Et supprimons ce `margin-left` du deuxième `<nav>` :

```css
@media only screen and (max-width: 768px) {
  .Navbar__Items,
  .Navbar {
    flex-direction: column;
  }
  .Navbar__Items--right {
    margin-left: 0;
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rmC0cKnio5Cg9W2CA1luPQ.png)
_Navbar à une largeur d'écran de 768px ou moins_

Mais maintenant, les éléments de navigation sont toujours visibles, ce qui prend une quantité significative d'espace à l'écran.

Dans notre requête média, ajoutons une deuxième règle pour `.Navbar__Items` afin qu'ils ne soient pas visibles :

```css
@media only screen and (max-width: 768px) {
  .Navbar__Items,
  .Navbar {
    flex-direction: column;
  }
  .Navbar__Items {
    display:none;
  }
  .Navbar__Items--right {
    margin-left:0;
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*8ipupgzJ6_ersFfTgVvm6w.png)
_À quoi ressemble la navbar sur mobile maintenant_

### Le bouton basculant

Pour le bouton basculant, je vais utiliser une icône fournie par [Font Awesome](https://fontawesome.com/). Si vous décidez de faire de même, suivez simplement les instructions sur leur site pour intégrer les icônes dans votre projet. Vous pouvez utiliser n'importe quel ensemble d'icônes que vous voulez, ou vous pouvez utiliser du texte simple si vous le souhaitez.

Maintenant, ajoutons cette icône à notre HTML :

```html
<div class="Navbar">
   <div class="Navbar__Link Navbar__Link-brand">
      Titre du site
    </div>
    <div class="Navbar__Link Navbar__Link-toggle">
      <i class="fas fa-bars"></i>
    </div>
  <nav class="Navbar__Items">
    <div class="Navbar__Link">
      Lien plus long
    </div>
    <div class="Navbar__Link">
      Lien plus long
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
  </nav>
  <nav class="Navbar__Items Navbar__Items--right">
    <div class="Navbar__Link">
      Lien
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
  </nav>
</div>
```

J'ai mis en gras la nouvelle addition. Vous remarquerez que ce basculement ne va pas dans l'une des balises `nav` mais se trouve à l'extérieur avec le titre du site. Cela a du sens.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GkN1E6ZKm7W93FKDqTiWBQ.png)
_Icône de menu ajoutée_

Bien sûr, ce n'est pas là où nous voulons qu'elle soit. Et pire encore, elle est visible sur les résolutions de bureau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*K5ygf98rpZNXLxQcjsJkXw.png)

Corrigeons cela. Faisons ce que nous avons fait avec `.Navbar__Items` sur mobile pour l'icône de menu sur le bureau :

```css
.Navbar__Link-toggle {
  display: none;
}
```

Maintenant, ajoutons quelques règles à la même classe dans notre requête média :

```css
.Navbar__Link-toggle {
  align-self: flex-end;
  display: initial;
  position: absolute;
  cursor: pointer;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*5jybOok3eVV03DHWKitL3g.png)
_À quoi ressemble la navbar sur mobile avec le menu basculant_

Maintenant, nous avons presque terminé ici. Nous avons l'apparence souhaitée. Mais nous devons ajouter une fonctionnalité de basculement à l'icône du menu.

Dans votre JavaScript, ajoutez :

```html
function classToggle() {
  const navs = document.querySelectorAll('.Navbar__Items')
  
  navs.forEach(nav => nav.classList.toggle('Navbar__ToggleShow'));
}

document.querySelector('.Navbar__Link-toggle')
  .addEventListener('click', classToggle);
```

Maintenant, enfin, ajoutez `Navbar__ToggleShow` avec la règle `display:flex` à votre requête média.

Maintenant, nous avons une navbar entièrement responsive avec un menu basculant. Avec Flexbox, c'est vraiment aussi simple !

![Image](https://cdn-media-1.freecodecamp.org/images/1*k0-kcRuPaA4LeuxzcIlJMg.gif)

### Le code final

#### HTML :

```html
<div class="Navbar">
   <div class="Navbar__Link Navbar__Link-brand">
      Titre du site
    </div>
    <div class="Navbar__Link Navbar__Link-toggle">
      <i class="fas fa-bars"></i>
    </div>
  <nav class="Navbar__Items">
    <div class="Navbar__Link">
      Lien plus long
    </div>
    <div class="Navbar__Link">
      Lien plus long
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
  </nav>
  <nav class="Navbar__Items Navbar__Items--right">
    <div class="Navbar__Link">
      Lien
    </div>
    <div class="Navbar__Link">
      Lien
    </div>
  </nav>
</div>
```

#### CSS :

```css
.Navbar {
  background-color: #46ACC2;
  display: flex;
  padding: 16px;
  font-family: sans-serif;
  color: white;
}

.Navbar__Link {
  padding-right: 8px;
}

.Navbar__Items {
  display: flex;
}

.Navbar__Items--right {
  margin-left:auto;
}

.Navbar__Link-toggle {
  display: none;
}

@media only screen and (max-width: 768px) {
  .Navbar__Items,
  .Navbar {
    flex-direction: column;
  }
    
.Navbar__Items {
    display:none;
  }
    
.Navbar__Items--right {
    margin-left:0;
  }
    
.Navbar__ToggleShow {
    display: flex;
  }
    
.Navbar__Link-toggle {
    align-self: flex-end;
    display: initial;
    position: absolute;
    cursor: pointer;
   } 
}
```

#### JS :

```js
function classToggle() {
  const navs = document.querySelectorAll('.Navbar__Items')
  
  navs.forEach(nav => nav.classList.toggle('Navbar__ToggleShow'));
}

document.querySelector('.Navbar__Link-toggle')
  .addEventListener('click', classToggle);
```

Lisez plus sur Flexbox à l'adresse suivante :

[**Concepts de base de flexbox**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)
[_Le module de boîte flexible, généralement appelé flexbox, a été conçu comme un modèle de mise en page unidimensionnel, et comme un…_](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)

Et où j'ai appris les bases de Flexbox moi-même :

[**Je viens de lancer un cours complet gratuit sur Flexbox où vous pouvez construire des projets de manière interactive**
_Après le succès du cours sur CSS Grid que j'ai lancé avec freeCodeCamp en décembre (plus de 14 000 étudiants jusqu'à présent !) Je…_](https://www.freecodecamp.org/news/i-just-launched-a-free-full-length-flexbox-course-where-you-can-build-projects-interactively-1860e3d3c4af/)

Suivez-moi sur [Twitter](https://twitter.com/CharlieCW90) ou [GitHub](https://github.com/charliearlie).