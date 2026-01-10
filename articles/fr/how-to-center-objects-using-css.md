---
title: Comment centrer n'importe quoi en CSS en utilisant Flexbox et Grid ✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-06-11T20:40:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-objects-using-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/FCC--center.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
seo_title: Comment centrer n'importe quoi en CSS en utilisant Flexbox et Grid ✨
seo_desc: 'Today I''m gonna show you how you can center and align your content with
  CSS. Along the way, we''ll look at various alignment techniques. So, let''s get
  started! 🥇

  Table of Contents ->


  How to Use Flexbox to

  center anything horizontally

  center anything...'
---

Aujourd'hui, je vais vous montrer comment **centrer et aligner** votre contenu avec CSS. En cours de route, nous examinerons diverses **techniques d'alignement**. Alors, commençons ! 💡

## Table des matières ->
* Comment utiliser **Flexbox** pour
   * [centrer n'importe quoi horizontalement](#heading-comment-centrer-nimporte-quoi-horizontalement-en-utilisant-flexbox)
   * [centrer n'importe quoi verticalement](#heading-comment-centrer-nimporte-quoi-verticalement-en-utilisant-flexbox)
   * [centrer à la fois horizontalement et verticalement](#heading-comment-centrer-une-div-horizontalement-et-verticalement-en-utilisant-flexbox)
* Comment utiliser **Grid** pour
   * [centrer n'importe quoi horizontalement](#heading-comment-centrer-nimporte-quoi-horizontalement-en-utilisant-css-grid)
   * [centrer n'importe quoi verticalement](#heading-comment-centrer-nimporte-quoi-verticalement-en-utilisant-css-grid)
   * [centrer à la fois horizontalement et verticalement](#heading-comment-centrer-une-div-horizontalement-et-verticalement-en-utilisant-css-grid)
* [La propriété Transform et position](#heading-comment-utiliser-la-propriete-css-position-pour-centrer-nimporte-quoi)
* [La propriété Margin](#heading-comment-utiliser-la-propriete-margin-pour-centrer-nimporte-quoi)
* [**Ressources supplémentaires**](#heading-ressources-supplementaires)
* [Conclusion](#heading-conclusion)

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-73.png)
_Méthodes_

## Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/RTEzXS_CT5w]

## Mais.... Attendez une minute !

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-35--3-.png)

Tout d'abord, comprenons :

* Axe principal
* Axe transversal

## Qu'est-ce que l'axe principal en CSS ?

Vous pouvez également l'appeler :

* **Axe-X**
* Axe principal
* Ligne horizontale

La ligne de **gauche** à **droite** est l'axe principal.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-71.png)
_Axe principal_

## Qu'est-ce que l'axe transversal en CSS ?

Vous pouvez également l'appeler :

* **Axe-Y**
* Axe transversal
* Ligne verticale

La ligne de **haut** en **bas** est l'axe transversal.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-72.png)
_Axe transversal_

# Installation du projet

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-54.png)

Pour expérimenter avec toutes les propriétés et valeurs, écrivez le code suivant dans votre éditeur de code.

### HTML

Écrivez ce code à l'intérieur de la balise body :

```html
<div class="container">

   <div class="box-1"> </div>
    
</div>
```

### CSS

Effacez les styles **par défaut** du navigateur afin que nous puissions travailler plus précisément :

```css
*{
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
```

Sélectionnez la classe **.container** et définissez-la à 100vh. Sinon, nous ne pouvons pas voir notre résultat sur l'**axe vertical** :

```css
.container{
   height: 100vh;
}
```

Stylisez la classe **.box-1** comme ceci :

```css
.box-1{
   width: 120px;
   height: 120px;
   background-color: skyblue;
   border: 2px solid black;
}
```

Nous sommes prêts, maintenant commençons à coder !

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-3--5-.png)

## Comment utiliser Flexbox pour centrer n'importe quoi

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Thumbnail-hashnode.png)

Nous pouvons utiliser Flexbox pour aligner notre contenu `div` à la fois le long de l'axe X et Y. Pour cela, nous devons écrire la propriété `display: flex;` à l'intérieur de la classe `.container` :

```css
.container{
   display: flex;
   
   height: 100vh;
}
```

Nous allons expérimenter avec ces 2 propriétés :

* `justify-content`
* `align-items`

## Comment centrer n'importe quoi horizontalement en utilisant Flexbox

Nous pouvons utiliser la propriété **justify-content** pour cela en utilisant ces valeurs 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Justify-content-1.png)
_**valeurs de la propriété justify-content de flexbox**_

Pour expérimenter avec les valeurs, écrivez le code suivant 👋

```css
.container{
   display: flex;
   height: 100vh;
   
 /* Changez les valeurs pour expérimenter 👋*/
   justify-content: center;
}
```

Le résultat ressemblera à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--2-.png)
_résultat de justify-content flexbox_

## Comment centrer n'importe quoi verticalement en utilisant Flexbox

Nous pouvons utiliser la propriété **`align-items`** pour cela en utilisant ces valeurs 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/align-items-1.png)
_**valeurs de la propriété align-items de Flexbox**_

Pour expérimenter avec les valeurs, écrivez le code suivant 👋

```css
.container{
   height: 100vh;
   display: flex;
   
 /* Changez les valeurs 👋 pour expérimenter*/
   align-items: center;
}

```

Le résultat ressemble à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-7--4-.png)
_Résultat de align-items flexbox_

## Comment centrer une div horizontalement et verticalement en utilisant Flexbox

Ici, nous pouvons combiner les propriétés **`justify-content`** et **`align-items`** pour aligner une div à la fois horizontalement et verticalement.

Écrivez les codes suivants 👋

```css
.container{
   height: 100vh;
   display: flex;
   
/* Changez les valeurs 👋 pour expérimenter*/
   align-items: center;
   justify-content: center;
}
```

Le résultat ressemble à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-8--1-.png)
_Centrer une div horizontalement et verticalement_

Vous pouvez consulter cette [feuille de triche](https://www.freecodecamp.org/news/css-flexbox-tutorial-with-cheatsheet/) pour en savoir plus sur les différentes propriétés de Flexbox.

## Comment utiliser CSS Grid pour centrer n'importe quoi

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-70.png)

Nous pouvons utiliser **grid** pour aligner notre contenu `div` à la fois le long de l'axe X et Y. Pour cela, nous devons écrire la propriété `display: grid;` à l'intérieur de la classe `.container` :

```css
.container{
   display: grid;
   
   height: 100vh;
}
```

Nous allons expérimenter avec ces 2 propriétés :

* `justify-content`
* `align-content`

**Alternativement**, vous pouvez utiliser ces 2 propriétés :

* `justify-items`
* `align-items`

## Comment centrer n'importe quoi horizontalement en utilisant CSS Grid

Nous pouvons utiliser la propriété **`justify-content`** pour cela en utilisant ces valeurs 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/justify-content-1--1-.png)
_**valeurs de la propriété justify-content de Grid**_

Écrivez le code suivant 👋

```css
.container{
   height: 100vh;
   display: grid;

  /* Changez les valeurs 👋 pour expérimenter*/
   justify-content: center;
}
```

Le résultat ressemble à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--2--1.png)
_**résultat de justify-content grid**_

## Comment centrer n'importe quoi verticalement en utilisant CSS Grid

Nous pouvons utiliser la propriété **`align-content`** pour cela en utilisant ces valeurs 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/align-content-1.png)
_Valeurs de la propriété align-content de CSS grid_

Écrivez le code suivant 👋

```css
.container{
   height: 100vh;
   display: grid;
   
  /* Changez les valeurs 👋 pour expérimenter*/
   align-content: center;
}
```

Le résultat ressemblera à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-7--4--1.png)
_résultat de align-content grid_

## Comment centrer une div horizontalement et verticalement en utilisant CSS Grid

Ici, nous pouvons combiner les propriétés **`justify-content`** et **`align-content`** pour aligner une div à la fois horizontalement et verticalement.

Écrivez le code suivant 👋

```css
.container{
   height: 100vh;
   display: grid;
    
/* Changez les valeurs 👋 pour expérimenter*/
   align-content: center;
   justify-content: center;
}
```

Le résultat ressemble à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-8--1--1.png)
_Centrer une div horizontalement et verticalement avec Grid_

## Méthode alternative

Vous pouvez également utiliser les propriétés **`justify-items`** et **`align-items`** pour dupliquer les mêmes résultats :

```css
.container{
   height: 100vh;
   display: grid;
    
/* Changez les valeurs 👋 pour expérimenter*/
   align-items: center;
   justify-items: center;
}
```

## La propriété place-content dans CSS Grid

Ceci est le **raccourci** de 2 propriétés de CSS Grid->

* `justify-content`
* `align-content`

Suivez 👋

```css
.container{
   height: 100vh;
   display: grid;
   
   place-content: center;
}
```

Nous obtenons le même résultat 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-8--1--2.png)
_Centrer une div horizontalement et verticalement_

Consultez cette [feuille de triche](https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet) pour découvrir la différence entre les diverses propriétés de Grid.

## Faites une pause !

Jusqu'à présent, tout va bien – faites une pause.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-67--1-.png)

## Comment utiliser la propriété CSS Position pour centrer n'importe quoi

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-12-1.png)

Ceci est une combinaison de ces propriétés ->

* `position`
* `top, left`
* `transform, translate`

Écrivez le code suivant 👋

```css
.container{
   height: 100vh;
   position: relative;
}
```

Avec ceci :

```css
.box-1{
   position: absolute;
   
   width: 120px;
   height: 120px;
   background-color: skyblue;
   border: 2px solid black;
}
```

## D'abord... Comprendre le point central d'une div

Par défaut, ceci est le point central d'une div 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-9.png)
_**Point central par défaut d'une div**_

C'est pourquoi nous voyons ce comportement étrange 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-8--2-.png)
_**La boîte n'est pas au centre exact**_

Remarquez que la boîte n'est pas au **centre exact** dans l'image ci-dessus. 👀

En écrivant cette ligne 👋

```css
transform: translate(-50%,-50%);

```

Nous résolvons le problème 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-10--2-.png)
_**Nouveau point central de notre div**_

Et nous obtenons ce résultat 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-11--1-.png)
_**La boîte est au point central exact**_

## Qu'est-ce que la propriété Translate en CSS ?

Translate est le raccourci de 3 propriétés ->

* `translateX`
* `translateY`
* `translateZ`

## Comment centrer une div horizontalement en utilisant la propriété CSS Position

Nous allons utiliser la propriété `left` à l'intérieur de la classe ``.box-``. Suivez 👋

```css
.box-1{
/* autres codes sont ici*/	

   left: 50%;
   transform: translate(-50%);
}
```

Et nous obtenons ce résultat 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--2--2.png)
_**résultat de la propriété left et transform**_

## Comment centrer une div verticalement en utilisant la propriété CSS Position

Nous allons utiliser la propriété `top` à l'intérieur de la classe ``box-``. Suivez 👋

```css
.box-1{
/* Autres codes sont ici*/	

   top: 50%;
   transform: translate(0,-50%);
}
```

Et nous obtenons ce résultat 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-7--4--2.png)
_**résultat de la propriété top et transform**_

## Comment centrer une div horizontalement et verticalement en utilisant la propriété CSS position

Pour obtenir ce résultat, nous allons combiner ces propriétés ensemble ->

* `top, left`
* `transform, translate`

Suivez 👋

```css
.box-1{
/*Autres codes sont ici */	

   top: 50%;
   left: 50%;
   transform: translate(-50%,-50%);
}
```

Et nous obtenons ce résultat 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-8--1--3.png)
_résultat de la propriété position et transform_

## Comment utiliser la propriété margin pour centrer n'importe quoi

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-73--2-.png)

La propriété margin est le raccourci de 4 propriétés

* `margin-**top**`, `margin-**bottom**`
* `margin-**left**`, `margin-**right**`

Écrivez ce code pour le configurer 👋

```css
.container{
   height: 100vh;
   
   display: flex;
}

.box-1{
   width: 120px;
   height: 120px;
   background-color: skyblue;
   border: 2px solid black;
}
```

## Comment centrer une div horizontalement en utilisant la propriété CSS margin

Nous allons utiliser la propriété `margin` à l'intérieur de la classe `.box-1`. Écrivez le code suivant 👋

```css
.box-1{
 //Autres codes sont ici 
   
  margin: 0px auto;	
}
```

Le résultat ressemble à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--2--3.png)
_****résultat de** la propriété CSS margin**_

## Comment centrer une div verticalement en utilisant la propriété CSS margin

Nous allons utiliser la propriété `margin` à l'intérieur de la classe `.box-1`. Écrivez le code suivant 👋

```css
.box-1{
 //Autres codes sont ici 
   
  margin: auto 0px;	
}
```

Le résultat ressemble à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-7--4--3.png)
_****résultat de** la propriété CSS margin**_

## Comment centrer une div horizontalement et verticalement en utilisant la propriété CSS margin

Nous allons utiliser la propriété `margin` à l'intérieur de la classe ``.box-``. Écrivez le code suivant 👋

```css
.box-1{
 //Autres codes sont ici 
   
  margin: auto auto;	
}
```

Le résultat ressemble à ceci 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-8--1--4.png)
_**Résultat de la propriété CSS margin**_

## Ressources supplémentaires

* [Tutoriel complet sur Flexbox avec feuille de triche](https://www.freecodecamp.org/news/css-flexbox-tutorial-with-cheatsheet/)
* [Tutoriel complet sur CSS Grid avec feuille de triche](https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/)

# Crédits

* [uncorns](https://www.flaticon.com/packs/unicorn-4), [kitty](https://www.flaticon.com/packs/kitty-avatars-3)
* [artist](https://www.freepik.com/free-vector/collection-people-enjoying-their-free-time_4931926.htm#position=7), [kat](https://www.freepik.com/free-vector/cute-cat-unicorn-play-box-cartoon-icon-illustration_12567355.htm#position=0)

# Conclusion

Maintenant, vous pouvez **aligner ou centrer** votre contenu en utilisant l'une de ces quatre méthodes en CSS.

Voici votre **médaille** pour avoir lu jusqu'à la fin ❤️

## Suggestions et critiques sont grandement appréciées ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube / [Joy Shaheb](https://www.youtube.com/c/JoyShaheb)**

**LinkedIn / [Joy Shaheb](https://www.linkedin.com/in/joyshaheb/)**

**Twitter / [JoyShaheb](https://x.com/JoyShaheb)**

**Instagram / [JoyShaheb](https://www.instagram.com/joyshaheb/)**