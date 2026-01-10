---
title: HTML Div – Qu'est-ce qu'une balise Div et comment la styliser avec CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-07T15:08:40.000Z'
originalURL: https://freecodecamp.org/news/html-div-what-is-a-div-tag-and-how-to-style-it-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/divTag.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: HTML Div – Qu'est-ce qu'une balise Div et comment la styliser avec CSS
seo_desc: 'The HTML division tag, called "div" for short, is a special element that
  lets you group similar sets of content together on a web page. You can use it as
  a generic container for associating similar content.

  The div tag is one of the most used tags an...'
---

La balise de division HTML, appelée "div" en abrégé, est un élément spécial qui vous permet de regrouper des ensembles similaires de contenu sur une page web. Vous pouvez l'utiliser comme un conteneur générique pour associer du contenu similaire.

La balise `div` est l'une des balises les plus utilisées et ne semble pas près de disparaître malgré l'introduction des éléments sémantiques (ces éléments vous permettent d'utiliser plusieurs balises comme conteneur).

Dans ce tutoriel, je vais vous montrer les différentes choses que vous pouvez faire avec la balise `div`, comment utiliser plusieurs divs dans le même fichier HTML sans vous perdre, et comment la styliser.

## Quand utiliser la balise `div`

La balise `div` est polyvalente – vous pouvez l'utiliser pour faire plusieurs choses sur une page web. Vous l'utiliserez principalement dans les mises en page web et l'art CSS, mais elle est super flexible.

En fin de compte, vous l'utiliserez presque toujours pour styliser ce qu'elle contient ou manipuler ces éléments avec JavaScript.

### 1. Utiliser `div` dans les mises en page web

Vous utiliserez principalement la balise `div` pour regrouper du contenu similaire afin de pouvoir le styliser facilement. Un excellent exemple est l'utilisation de div pour regrouper différentes sections d'une page web. Vous pouvez rassembler l'en-tête, la navigation, les sections et le pied de page d'une page dans une balise div individuelle pour qu'ils puissent être stylisés ensemble.

Plus tard dans ce tutoriel, je vous montrerai comment créer une mise en page web avec plusieurs balises `div` sans vous perdre.

Div elle-même n'a pas d'effet direct sur la présentation du contenu sauf si vous la stylisez.

### 2. Utiliser `div` dans l'art CSS

Avec la balise div, vous pouvez créer diverses formes et dessiner n'importe quoi car elle est facile à styliser.

- Comment faire un carré avec la balise `div`

Pour faire un carré avec la balise `div`, vous devez d'abord définir une balise div vide et lui attacher un attribut de classe dans le HTML. Dans le CSS, sélectionnez le div avec l'attribut de classe, puis définissez une hauteur et une largeur égales.

```html
<div class="square"></div>
```

```css
 body {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
      background-color: #f1f1f1;
    }
.square {
      background-color: #2ecc71;
      width: 200px;
      height: 200px;
    }
```

![square](https://www.freecodecamp.org/news/content/images/2021/09/square.png)

- Comment faire un cercle avec la balise `div`

Vous pouvez faire un cercle avec la balise `div` en codant une div vide dans le HTML, en définissant une hauteur et une largeur égales dans le CSS, puis un `border-radius` de 50%.

```html
<div class="circle"></div>
```

```css
  body {
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
      background-color: #f1f1f1;
    }

    .circle {
      background-color: #2ecc71;
      width: 200px;
      height: 200px;
      border-radius: 50%;
    }
```
![circle](https://www.freecodecamp.org/news/content/images/2021/09/circle.png)

- Comment faire le drapeau nigérian avec CSS

Faire le drapeau nigérian avec la balise `div` n'est pas si difficile. Le drapeau est une forme rectangulaire avec les couleurs vert, blanc et vert.

Pour le faire, définissez 3 balises `div` et attachez différentes classes, puis stylisez-les de manière appropriée dans le CSS.

```html
<div class="naija-flag">
    <div class="first-green"></div>
    <div class="white"></div>
    <div class="second-green"></div>
</div>
```

```css
.naija-flag {
  display: flex;
}
.first-green {
  height: 100px;
  width: 60px;
  background-color: green;
}
.white {
  height: 100px;
  width: 60px;
  background-color: white;
}
.second-green {
  height: 100px;
  width: 60px;
  background-color: green;
}
```
![naija-flag](https://www.freecodecamp.org/news/content/images/2021/09/naija-flag.png)

## Comment styliser la balise `div`

Comme nous l'avons discuté ci-dessus, la balise div est très facile à styliser. C'est l'une des raisons pour lesquelles de nombreux développeurs l'utilisent pour regrouper du contenu similaire.

La balise div accepte presque toutes les propriétés CSS sans problème. Regardons quelques exemples maintenant.

### 1. Comment appliquer les propriétés de police avec `div`

Vous pouvez appliquer les propriétés CSS telles que `font-size`, `font-family`, `font-weight` et `font-style` sur du contenu regroupé avec la balise `div` :

```html
<div class="font-properties">
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate quo
        ullam modi alias assumenda, itaque libero? Quas quidem sint illo.
      </p>
      <p>
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus
        ipsam eaque rem dicta, quos quas ipsum.
      </p>
</div>
```

```css
body {
      max-width: 900px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      height: 100vh;
      background-color: #f1f1f1;
    }

.font-properties {
      font-family: cursive, sans-serif;
      font-size: 1.3rem;
      font-weight: bolder;
      font-style: italic;
    }
```

![font](https://www.freecodecamp.org/news/content/images/2021/09/font.png)

### 2. Comment appliquer la couleur avec la balise Div

Vous pouvez appliquer les propriétés CSS `color` et `background-color` sur du contenu regroupé avec la balise `div` :

```html
<div class="color-properties">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate quo
    ullam modi alias assumenda, itaque libero? Quas quidem sint illo.
  </p>
  <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus
    ipsam eaque rem dicta, quos quas ipsum.
  </p>
</div>
```

```css
.color-properties {
  color: white;
  background-color: #2ecc71;
}
```
![color](https://www.freecodecamp.org/news/content/images/2021/09/color.png)

### 3. Comment styliser les textes avec la balise Div

Vous pouvez appliquer les propriétés CSS `text-transform` et `text-decoration` sur une balise `div` comme ceci :

```html
<div class="text-properties">
  <p>
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate quo
    ullam modi alias assumenda, itaque libero? Quas quidem sint illo.
  </p>
  <p>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Necessitatibus
    ipsam eaque rem dicta, quos quas ipsum.
   </p>
</div>
```

```css
.text-properties {
    text-transform: uppercase;
    text-decoration: underline;
  }
```

![text](https://www.freecodecamp.org/news/content/images/2021/09/text.png)

### 4. Comment créer un effet d'ombre avec la balise Div

Vous pouvez créer un effet d'ombre avec la balise `div` avec la propriété box-shadow :

```html
<div class="box-shadow">
      <p>
        Avant de payer pour apprendre la programmation, consultez freeCodeCamp.org
        <br />
        Les curricula HTML, CSS et JavaScript vous mèneront de zéro à héros
        en développement web.
      </p>
      <p>
        Il y a un curriculum Python qui vous donnera une connaissance considérable
        en Python <br />
        Et un prochain curriculum en science des données.
      </p>
</div>
```

```css
.box-shadow {
      font-family: cursive, sans-serif;
      background-color: #2ecc71;
      color: white;
      padding: 10px;
      border-radius: 4px;
      box-shadow: 2px 2px 20px 23px #7fecad;
    }
```

Que se passe-t-il dans le CSS ci-dessus ?

J'ai pu créer l'effet d'ombre avec la propriété CSS box-shadow.

- La première valeur (2px) représente le décalage sur l'axe x (offset-x)
- La seconde (un autre 2px) représente le décalage sur l'axe y (offset-y)
- Les 20px suivants sont pour le rayon de flou, c'est-à-dire à quel point vous voulez que l'ombre soit floue.
- La valeur 23px est le rayon de propagation (à quel point vous voulez que l'ombre se propage)
- La dernière valeur est la couleur de l'ombre – dans ce cas, #7fecad.

Le résultat ressemble à ceci :
![box-shadow](https://www.freecodecamp.org/news/content/images/2021/09/box-shadow.png)

## Comment utiliser plusieurs éléments Div sans se perdre

Les balises Div sont couramment utilisées pour regrouper du contenu similaire. Dans les anciennes et même certaines nouvelles pages web, vous trouverez des divs partout, malgré le fait que les balises sémantiques soient recommandées pour l'accessibilité et un meilleur référencement.

Puisque les balises `div` sont encore très courantes, je recommande de leur appliquer des attributs de classe et d'identifiant afin de pouvoir manipuler des éléments div individuels avec ces attributs.

Je vais vous montrer comment mettre cela en pratique en créant une mise en page web de base.

La première section que vous voudrez créer est l'en-tête, contenant le logo et la barre de navigation :

```html
 <div class="header">
      <h2 class="logo">freeCodeCamp</h2>

      <ul class="nav">
        <li><a href="">Accueil</a></li>
        <li><a href="">À propos</a></li>
        <li><a href="">Services</a></li>
        <li><a href="">Contact</a></li>
      </ul>
</div>
```


Avant de styliser la barre de navigation, j'ai fait quelques réinitialisations CSS pour que les choses s'alignent correctement et s'affichent bien :

```css
* {
   margin: 0;
   padding: 0;
   box-sizing: border-box;
 }

.hero,
.about,
.services,
.contact {
  max-width: 1000px;
  margin: 0 auto;
  margin-bottom: 20px;
}
```

Dans l'extrait de code ci-dessus :

- J'ai supprimé la marge et le remplissage par défaut
- J'ai défini une largeur maximale pour les sections principales afin qu'elles ne s'étendent pas sur toute la largeur pour une meilleure UX
- J'ai défini une marge en bas de chaque section pour leur donner un peu d'espace
- J'ai défini une marge à 0 en haut et en bas, auto à gauche et à droite pour les centrer.

Pour styliser la barre de navigation de manière appropriée, je vais prendre la balise `div` conteneur avec son attribut de classe, `header`. Je vais lui donner un affichage de `flex`, ainsi que quelques autres propriétés pour la disposer correctement. Je vais également prendre la `div` enveloppant la barre de navigation (élément `ul`) par sa classe et la disposer avec Flexbox.

```css
.header {
      padding: 0 70px;
      display: flex;
      align-content: center;
      justify-content: space-between;
      margin-top: 20px;
      margin-bottom: 20px;
    }

.nav {
      display: flex;
      align-content: center;
      justify-content: center;
      gap: 60px;
      list-style-type: none;
    }

.nav li a {
      text-decoration: none;
      color: black;
      font-size: 1.2rem;
    }
```

Pour les sections restantes à part le pied de page, le HTML et les styles sont génériques :

```html
<div class="hero">
      <h1>Section Hero</h1>
</div>
<div class="about">
      <h1>À propos de nous</h1>
</div>
<div class="services">
      <h1>Nos Services</h1>
</div>
<div class="contact">
      <h1>Contactez-nous</h1>
</div>
<div class="footer">
      <p>&copy; 2021 Tous droits réservés</p>
</div>
```

```css
.hero {
      background-color: #eee;
      height: 200px;
    }

.hero h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.about {
      background-color: #eee;
      height: 200px;
    }

.about h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.services {
      background-color: #eee;
      height: 200px;
    }

.services h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.contact {
      background-color: #eee;
      height: 200px;
    }

.contact h1 {
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 6;
    }

.footer {
      background-color: #777;
      height: 40px;
    }

.footer p {
      margin: 0 auto;
      line-height: 1.7;
    }
```


J'ai donné aux sections individuelles une couleur de fond grisâtre et une hauteur de 200px. J'ai positionné les balises h1 à l'intérieur au centre avec Flexbox et appliqué une `hauteur de ligne` de 1.5 à chacune d'elles.

Enfin, j'ai donné au pied de page une couleur de fond gris plus foncé pour le distinguer, et centré le contenu avec une `hauteur de ligne` de 1.7.

La mise en page résultante ressemble à ceci :![layout](https://www.freecodecamp.org/news/content/images/2021/09/layout.gif)


## Conclusion

La balise div HTML est couramment utilisée par les développeurs web partout.

Gardez simplement à l'esprit que vous devriez généralement utiliser le HTML sémantique à la place de la balise div sauf si aucune d'entre elles (les balises sémantiques) ne correspond vraiment au contenu à regrouper. Cela est dû au fait que les balises sémantiques sont meilleures pour l'accessibilité et le référencement.

En bref, la balise div reste utile et n'est pas près de disparaître, alors n'hésitez pas à l'utiliser lorsque cela est nécessaire.

Merci d'avoir lu et passez un bon moment.