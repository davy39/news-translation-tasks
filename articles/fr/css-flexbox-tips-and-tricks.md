---
title: Astuces et conseils pour CSS Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-30T17:55:00.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-tips-and-tricks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e5f740569d1a4ca3cc0.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
seo_title: Astuces et conseils pour CSS Flexbox
seo_desc: 'CSS Flexbox allows you to easily format your HTML like you never knew was
  possible. With Flexbox you can align vertically and horizontally, easily. Like the
  sound of that? Yeah, so do I.

  Flexbox is also super useful when you''re creating the general l...'
---

CSS Flexbox vous permet de formater facilement votre HTML comme vous ne l'aviez jamais imaginé. Avec Flexbox, vous pouvez aligner verticalement et horizontalement, facilement. Ça vous plaît ? Oui, à moi aussi.

Flexbox est également super utile lorsque vous créez la mise en page générale de votre site web ou de votre application. Il est facile à apprendre, bien supporté (dans tous les navigateurs modernes) et est agréable à utiliser – sans compter qu'il ne faut pas longtemps pour maîtriser les bases.

Alors, plongeons-nous directement et apprenons-en plus.

## **Flexbox**

Voici une liste des propriétés Flexbox qui peuvent être utilisées pour positionner des éléments en CSS :

### **CSS qui peut être appliqué à un conteneur**

```text
display: flexbox | inline-flex;
flex-direction: row | row-reverse | column | column-reverse;
flex-wrap: nowrap | wrap | wrap-reverse;
flex-flow: <'flex-direction'> || <'flex-wrap'>
justify-content: flex-start | flex-end | center | space-between | space-around;
align-items: flex-start | flex-end | center | baseline | stretch;
align-content: flex-start | flex-end | center | space-between | space-around | stretch;
```

### **CSS qui peut être appliqué aux éléments dans un conteneur**

```text
order: <integer>;
flex-grow: <number>; /* par défaut 0 */
flex-shrink: <number>; /* par défaut 1 */
flex-basis: <length> | auto; /* par défaut auto */
flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
align-self: auto | flex-start | flex-end | center | baseline | stretch;
```

Maintenant, vous avez votre boîte à outils. Mais vous pourriez demander « Que fais-je avec mes outils, et comment les utiliser ? » Eh bien, laissez-moi vous montrer.

### **Display Flex**

`display: flex;` dit simplement à votre navigateur : « Hé, j'aimerais utiliser Flexbox avec ce conteneur, s'il te plaît. » Cela initialisera cette boîte en tant que conteneur Flex et appliquera certaines propriétés Flex par défaut.

Voici à quoi ressemble notre conteneur sans `display: flex;` :

![CSS playground no flex properties](https://discourse-user-assets.s3.amazonaws.com/original/2X/8/8f20f30d24cba9a7f56bf950a3f23d37d356ca51.png)

Après avoir ajouté `display: flex;` nous obtenons ce qui suit – vous pouvez voir que les propriétés Flex par défaut sont appliquées, ce qui donne ceci :

![CSS playground display flex default style](https://discourse-user-assets.s3.amazonaws.com/original/2X/6/66404664f9177ae748be00f769faf67d5956034d.png)

### **Flex Direction**

`flex-direction:` nous permet de contrôler comment les éléments dans le conteneur sont affichés. Voulez-vous les aligner de gauche à droite, de droite à gauche, de haut en bas ou de bas en haut ? Vous pouvez faire tout cela facilement en définissant la direction Flex du conteneur.

Flexbox applique les lignes comme valeur par défaut pour la direction. Voici à quoi elles ressemblent toutes :

`flex-direction: row;`

![flex-direction: row; example](https://discourse-user-assets.s3.amazonaws.com/original/2X/9/951cc993820547efa28e70dca905f5531a4488d5.png)

`flex-direction: row-reverse;`

![flex-direction: row-reverse example](https://discourse-user-assets.s3.amazonaws.com/original/2X/c/cf738aaf83f29eccdb461e91b775b10e41b92389.png)

`flex-direction: column;`

![flex-direction: column example](https://discourse-user-assets.s3.amazonaws.com/original/2X/7/7ef77565bc07ee86fd3033a531dd76b49709cf7e.png)

`flex-direction: column-reverse;`

![flex-direction: column-reverse example](https://discourse-user-assets.s3.amazonaws.com/original/2X/e/ec9a1ec064bf0027fa61016ca620df14d9bd47a9.png)

### **Flex Wrap**

Par défaut, Flexbox essaiera de faire tenir tous les éléments dans une seule ligne. Mais vous pouvez changer cela avec la propriété flex-wrap. Cela vous permet de choisir si les éléments vont déborder ou non.

Il y a 3 propriétés pour `flex-wrap:` :

`flex-wrap: nowrap` est la valeur par défaut et essaiera de tout faire tenir dans une seule ligne de gauche à droite.

`flex-wrap: wrap` permet aux éléments de créer plusieurs lignes de gauche à droite.

`flex-wrap: wrap-reverse` permet aux éléments d'être sur plusieurs lignes mais les affiche de droite à gauche cette fois.

### **Flex Flow**

Flex flow combine l'utilisation de `flex-wrap` et `flex-direction` en une seule propriété. Il est utilisé en définissant d'abord la direction puis le wrap.

`flex-flow: column wrap;` est un exemple de comment utiliser cela.

### **Justify Content**

`justify-content` est une propriété qui aligne les éléments dans le conteneur le long de l'axe principal (cela change en fonction de la manière dont le contenu est affiché).

Il y a plusieurs options pour cela. Cela nous permet de remplir tout espace vide dans les lignes mais nous laisse définir comment nous voulons le « justifier ».

Voici nos options lorsque nous justifions notre contenu : `flex-start | flex-end | center | space-between | space-around;`.

### **Align Items**

Align items nous permet d'aligner les éléments le long de l'axe transversal. Cela permet de positionner le contenu de nombreuses manières différentes en utilisant justify content et align items ensemble.

`align-items: flex-start | flex-end | center | baseline | stretch;`

### **Align Content**

Cela sert à aligner les éléments avec plusieurs lignes. C'est pour l'alignement sur l'axe transversal et n'aura aucun effet sur le contenu qui est sur une seule ligne.

`align-content: flex-start | flex-end | center | space-between | space-around | stretch;`

## Autres ressources sur Flexbox et Grid

### Articles et cours

[The Ultimate CSS Flex Cheatsheet](https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/)

[Full CSS Video Course (Includes Flexbox and Grid)](https://www.freecodecamp.org/news/full-css-course-flexbox-grid/)

[A Visual Guide to CSS Flexbox](https://www.freecodecamp.org/news/do-you-even-flex-box-c16449cfca96/)

[How to Create an Image Gallery with CSS Grid](https://www.freecodecamp.org/news/how-to-create-an-image-gallery-with-css-grid-e0f0fd666a5c/)

### Jeux et applications

[Flexbox Defense](http://www.flexboxdefense.com/) est un jeu web qui enseigne flexbox de manière amusante.

[Flexbox Froggy](http://flexboxfroggy.com/) est également un jeu web qui enseigne flexbox de manière amusante.

[Flexbox in 5](http://flexboxin5.com/) est une application web qui vous permet de voir comment flexbox fonctionne avec quelques contrôles simples.

[Flexyboxes](http://the-echoplex.net/flexyboxes/) est une application qui vous permet de voir des exemples de code et de changer les paramètres pour voir comment flexbox fonctionne visuellement.

[Flexbox Patters](http://www.flexboxpatterns.com/) est un site web qui montre de nombreux exemples de flexbox.

### Vidéos

[Flexbox Essentials](https://www.youtube.com/watch?v=G7EIAgfkhmg)

[Flexbox Practical Examples](https://www.youtube.com/watch?v=H1lREysgdgc)

[What The Flexbox?!](https://www.youtube.com/watch?v=Vj7NZ6FiQvo&list=PLu8EoSxDXHP7xj_y6NIAhy0wuCd4uVdid)