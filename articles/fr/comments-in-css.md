---
title: Exemple de commentaire CSS – Comment commenter en CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T21:57:00.000Z'
originalURL: https://freecodecamp.org/news/comments-in-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d7b740569d1a4ca3800.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: Design
  slug: design
- name: style
  slug: style
seo_title: Exemple de commentaire CSS – Comment commenter en CSS
seo_desc: 'Comments are used in CSS to explain a block of code or to make temporary
  changes during development. The commented code doesn’t execute.

  Both single and multi-line comments in CSS begin with /* and end with */, and you
  can add as many comments to you...'
---

Les commentaires sont utilisés en CSS pour expliquer un bloc de code ou pour apporter des modifications temporaires pendant le développement. Le code commenté ne s'exécute pas.

Les commentaires, qu'ils soient sur une seule ligne ou sur plusieurs lignes en CSS, commencent par `/*` et se terminent par `*/`, et vous pouvez ajouter autant de commentaires que vous le souhaitez à votre feuille de style. Par exemple :

```css
/* Ceci est un commentaire sur une seule ligne */
.group:after {
  content: "";
  display: table;
  clear: both;
}

/*
  Ceci est
  un commentaire
  sur plusieurs lignes
*/
```

Vous pouvez également rendre vos commentaires plus lisibles en les stylisant :

```css
/*
***
* SECTION POUR LE STYLE H2
***
* Un paragraphe avec des informations
* qui seraient utiles pour quelqu'un
* qui n'a pas écrit le code.
* Les astérisques autour du paragraphe
* aident à le rendre plus lisible.
***
*/
```

## Organiser le CSS avec des commentaires

Dans les projets plus importants, les fichiers CSS peuvent rapidement devenir volumineux et difficiles à maintenir. Il peut être utile d'organiser votre CSS en sections distinctes avec une table des matières pour faciliter la recherche de certaines règles à l'avenir :

```css
/*
*  TABLE DES MATIÈRES CSS
*
*  1.0 - Réinitialisation
*  2.0 - Polices
*  3.0 - Globaux
*  4.0 - Palette de couleurs
*  5.0 - En-tête
*  6.0 - Corps
*    6.1 - Curseurs
*    6.2 - Imagerie
*  7.0 - Pied de page
*/

/*** 1.0 - Réinitialisation ***/

/*** 2.0 - Polices ***/

/*** 3.0 - Globaux ***/

/*** 4.0 - Palette de couleurs ***/

/*** 5.0 - En-tête ***/

/*** 6.0 - Corps ***/
h2 {
  font-size: 1.2em;
  font-family: "Ubuntu", serif;
  text-transform: uppercase;
}

/*** 5.1 - Curseurs ***/

/*** 5.2 - Imagerie ***/

/*** 7.0 - Pied de page ***/
```

## Un peu plus sur le CSS : **Syntaxe et sélecteurs CSS**

Lorsque nous parlons de la syntaxe du CSS, nous parlons de la manière dont les éléments sont disposés. Il existe des règles sur ce qui va où, à la fois pour que vous puissiez écrire du CSS de manière cohérente et pour qu'un programme (comme un navigateur) puisse l'interpréter et l'appliquer correctement à la page.

Il existe deux principales façons d'écrire du CSS.

### **CSS en ligne**

Détails sur la spécificité CSS : [CSS Tricks](https://css-tricks.com/specifics-on-css-specificity/)

Le CSS en ligne applique un style à un seul élément et à ses enfants, jusqu'à ce qu'un autre style remplaçant le premier soit rencontré.

Pour appliquer du CSS en ligne, ajoutez l'attribut "style" à un élément HTML que vous souhaitez modifier. À l'intérieur des guillemets, incluez une liste de paires clé/valeur séparées par des points-virgules (chaque paire étant séparée par un deux-points) indiquant les styles à définir.

Voici un exemple de CSS en ligne. Les mots "One" et "Two" auront une couleur de fond jaune et une couleur de texte rouge. Le mot "Three" a un nouveau style qui remplace le premier, et aura une couleur de fond verte et une couleur de texte cyan. Dans l'exemple, nous appliquons des styles aux balises `<div>`, mais vous pouvez appliquer un style à n'importe quel élément HTML.

```html
<div style="color:red; background:yellow">
  One
  <div>
    Two
  </div>
  <div style="color:cyan; background:green">
    Three
  </div>
</div>
```

### **CSS interne**

Bien qu'écrire un style en ligne soit un moyen rapide de modifier un seul élément, il existe une méthode plus efficace pour appliquer le même style à de nombreux éléments de la page en une seule fois.

Le CSS interne a ses styles spécifiés dans la balise `<style>`, et il est intégré dans la balise `<head>`.

Voici un exemple qui a un effet similaire à l'exemple "en ligne" ci-dessus, sauf que le CSS a été extrait dans sa propre section. Les mots "One" et "Two" correspondront au sélecteur `div` et seront en texte rouge sur fond jaune. Les mots "Three" et "Four" correspondront également au sélecteur `div`, mais ils correspondent également au sélecteur `.nested_div` qui s'applique à tout élément HTML faisant référence à cette classe. Ce sélecteur plus spécifique remplace le premier, et ils finissent par apparaître en texte cyan sur fond vert.

```html
<style type="text/css">
  div { color: red; background: yellow; }
  .nested_div { color: cyan; background: green; }
</style>

<div>
  One
  <div>
    Two
  </div>
  <div class="nested_div">
    Three
  </div>
  <div class="nested_div">
    Four
  </div>
</div>
```

Les sélecteurs présentés ci-dessus sont extrêmement simples, mais ils peuvent devenir assez complexes. Par exemple, il est possible d'appliquer des styles uniquement aux éléments imbriqués, c'est-à-dire à un élément qui est un enfant d'un autre élément.

Voici un exemple où nous spécifions un style qui ne doit être appliqué qu'aux éléments `div` qui sont des enfants directs d'autres éléments `div`. Le résultat est que "Two" et "Three" apparaîtront en texte rouge sur fond jaune, mais "One" et "Four" resteront inchangés (et probablement en texte noir sur fond blanc).

```html
<style type="text/css">
  div > div { color: red; background: yellow; }
</style>

<div>
  One
  <div>
    Two
  </div>
  <div>
    Three
  </div>
</div>
<div>
  Four
</div>
```

### **CSS externe**

Tout le style a son propre document qui est lié dans la balise `<head>`. L'extension du fichier lié est `.css`