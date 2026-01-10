---
title: Apprenez la propriété CSS Box-Shadow en codant un beau bouton ✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-06-30T18:49:49.000Z'
originalURL: https://freecodecamp.org/news/css-box-shadow-property-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/FCC-Thumbnail.png
tags:
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: Web Design
  slug: web-design
seo_title: Apprenez la propriété CSS Box-Shadow en codant un beau bouton ✨
seo_desc: 'Today we''re gonna learn how to use CSS''s box-shadow property to make
  beautiful website components. Along the way, we''ll create a button and get hands-on
  experience using this property. Let''s get started. 🎖️

  Table of Contents


  Why you should use the ...'
---

Aujourd'hui, nous allons apprendre à utiliser la propriété **box-shadow** de CSS pour créer de beaux composants de site web. En cours de route, nous allons **créer un bouton** et acquérir une expérience pratique de l'utilisation de cette propriété. Commençons. 🎖️

# Table des matières 

* [**Pourquoi** vous devriez utiliser la propriété CSS box-shadow](#heading-pourquoi-utiliser-la-propriete-css-box-shadow)
* [La **syntaxe** de la propriété box-shadow](#heading-la-syntaxe-de-la-propriete-box-shadow)
* [Comment faire un **bouton** en utilisant la propriété box-shadow](#heading-comment-ajouter-une-ombre-portée-à-un-bouton)
* [Ressources supplémentaires](#heading-ressources-supplementaires) 
* [Qu'est-ce que **inset** dans la propriété CSS **Box shadow** ?](#heading-quest-ce-que-inset-dans-la-propriete-css-box-shadow)

## **Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :**

%[https://youtu.be/4Clc-Bb5sY4]

# Pourquoi utiliser la propriété CSS box-shadow ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-1.png)

**L'attention aux petits détails** distingue un bon site web d'un site web excellent. Si vous souhaitez ajouter ces petits détails à votre site web, vous devriez définitivement utiliser cette propriété ainsi que de nombreuses autres propriétés.

Regardons quelques exemples. 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Page-1--1-.png)
_**Un design de site web**_

Portez une attention particulière aux composants de boutons dans l'image ci-dessus. Vous verrez que nous avons quelques ombres portées. ☝

Examinons ces boutons encore plus en détail : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-27.png)
_**Bouton sans la propriété box-shadow**_

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-28.png)
_**Bouton utilisant la propriété box-shadow**_

Vous pouvez constater que ce dernier semble plus dynamique et intéressant, car il a plus **d'attention aux détails**. Cela s'appelle un **effet d'ombre portée**. Voyons comment nous pouvons l'implémenter dans notre code.

# **Installation du projet**

### HTML

Écrivez ce code à l'intérieur de la balise body : 👋

```html
<div class="box-1"> Un Bouton </div>
```

### CSS

Effacez les paramètres par défaut de votre navigateur comme ceci :

```css
*{
   margin: 0px;
   padding: 0px;
   box-sizing: border-box;
   font-family: sans-serif;
}
```

Maintenant, créons un bouton avec le code suivant : 👋

```css
.box-1{
   margin: 100px 0 0 100px;
   height: 80px;
   width: 200px;
   border: 2px solid black;
   border-radius: 8px;
   font-size: 40px;

   display: grid;
   place-content: center;
}

```

Nous sommes prêts, maintenant commençons à coder !

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-2.png)

# La syntaxe de la propriété box-shadow

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-3-1.png)
_**Tous les paramètres de la propriété box-shadow**_

Voici la syntaxe de la propriété box-shadow : 👋

```css
box-shadow: offset-x | offset-y | blur-radius | spread-radius | color ;
```

Examinons chaque partie plus en détail.

## Comment utiliser Offset-x dans la propriété box-shadow

Vous utiliserez la propriété offset-x pour déplacer l'ombre à gauche et à droite le long de l'axe X. Voici une démonstration pour vous montrer à quoi cela ressemble : 👋

![Image](https://media.giphy.com/media/Mzxh8CdUTaxgzzj9ml/giphy.gif)
_**Nous pouvons déplacer l'ombre à gauche et à droite**_

Pour recréer ces résultats, écrivez le code suivant dans votre CSS : 👋

```css
/* offset-x | offset-y | color */
.box-1{
   box-shadow: -50px 0px rgba(0,0,0,0.5);
}

/*Ou, vous pouvez écrire*/

.box-1{
   box-shadow: 50px 0px rgba(0,0,0,0.5);
}
```

## Comment utiliser Offset-y dans la propriété box-shadow

Vous utiliserez la propriété offset-y pour déplacer l'ombre vers le haut et vers le bas le long de l'axe Y. Voici une démonstration de à quoi cela ressemble : 👋

![Image](https://media.giphy.com/media/Ss9Qnrq9PFBpAfVLk8/giphy.gif)
_**Nous pouvons déplacer l'ombre en haut et en bas**_

Pour recréer ces résultats, écrivez ce qui suit dans votre CSS : 👋

```css
/* offset-x | offset-y | color */
.box-1{
   box-shadow: 0px -50px rgba(0,0,0,0.5);
}

/*Ou, vous pouvez écrire*/

.box-1{
   box-shadow: 0px -50px rgba(0,0,0,0.5);
}
```

### Comment combiner offset-x et offset-y

Écrivez le code suivant dans votre CSS : 👋

```css
.box-1{
   box-shadow: 10px 10px rgba(0,0,0,0.5);
}
```

Voici le résultat avec l'ombre de la boîte s'affichant à droite et en bas du bouton : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6-1.png)
_**Notre bouton avec une ombre de boîte**_

## Comment utiliser blur-radius dans la propriété box-shadow

La propriété blur-radius va flouter **la couleur** autour de notre bouton, comme ceci : 👋

![Image](https://media.giphy.com/media/5fRA7jzOwtmXnT57Ne/giphy.gif)
_**Expérimentation avec le rayon de flou**_

Pour dupliquer les résultats, écrivez ce qui suit dans votre CSS : 👋

```css
/* offset-x | offset-y | blur-radius | color */

.box-1{
/* jouez avec 👋 ceci */
   box-shadow: 0 0 50px rgba(0,0,0,0.8);
}
```

## Comment utiliser spread-radius dans la propriété box-shadow

Cette valeur étale notre ombre autour de notre bouton, comme ceci : 👋

![Image](https://media.giphy.com/media/FfVw2vxOonQAjkFc7B/giphy.gif)
_**Expérimentation avec le rayon de propagation**_

Recréons les résultats avec le code CSS suivant :

```css
/* offset-x | offset-y | blur-radius | spread-radius | color */

.box-1{
/*  jouez avec 👋 ceci */
   box-shadow: 0 0 0 50px rgba(0,0,0,0.5);
}

```

# Comment ajouter une ombre portée à un bouton

Mettons ensemble ce que nous avons appris jusqu'à présent et ajoutons un effet d'ombre portée à notre bouton : 👋

```css
.box-1{
   box-shadow: 8px 10px 10px 1px rgba(0,0,0,0.5);
}
```

Le résultat ressemble à ceci : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--1--1.png)
_**Le résultat**_

# Ressources supplémentaires 

* [[GetCssScan](https://getcssscan.com/css-box-shadow-examples)] - Pour obtenir des ombres de boîte prêtes à l'emploi
* [[keyframes.app](https://keyframes.app/animate/)] - pour tester et pratiquer ces propriétés en temps réel
* [flatuicolors](https://flatuicolors.com/) - Belles palettes de couleurs

## ✨ Conseil Bonus ✨

# Qu'est-ce que Inset dans la propriété CSS box-shadow ?

Il existe un mot-clé nommé `inset` que vous pouvez utiliser avec la propriété box-shadow. Cela place l'ombre à l'intérieur de notre bouton au lieu de l'étaler autour de l'extérieur. Écrivez ce code CSS pour expérimenter avec : 👋

```css
.box-1{
   box-shadow: inset 8px 10px 10px 1px rgba(0,0,0,0.5);
}
```

Voici le résultat : 👋

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Frame-6--2--4.png)
_**Effet du mot-clé inset**_

# Conclusion

Maintenant, vous pouvez utiliser en toute confiance la propriété box-shadow pour ajouter non seulement des **ombres portées**, mais aussi pour ajouter plus **d'attention aux détails** à vos projets.

Voici votre médaille pour avoir lu jusqu'à la fin. ❤️

### Les suggestions et critiques sont grandement appréciées ❤️

![](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

* **YouTube[ / Joy Shaheb](https://youtube.com/c/joyshaheb)**
* **LinkedIn[ / JoyShaheb](https://www.linkedin.com/in/joyshaheb/)**
* **Twitter[ / JoyShaheb](https://twitter.com/JoyShaheb)**
* **Instagram[ / JoyShaheb](https://www.instagram.com/joyshaheb/)**

# Crédits

* [Young Girl](https://www.freepik.com/free-vector/young-girl-thinking-face-wondering-cartoon-illustration_11652601.htm#page=1&query=worried%20illustration&position=31)
* [Cute Kat](https://www.freepik.com/free-vector/cute-cat-playing-with-box-cartoon_13747509.htm?query=happy%20illustration), [Unicorn cat](https://www.freepik.com/free-vector/kawaii-cat-unicorn-character-collection_5481560.htm)