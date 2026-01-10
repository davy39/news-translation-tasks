---
title: Propriétés du modèle de boîte CSS – Expliqué avec des exemples ✨
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-07-22T17:31:57.000Z'
originalURL: https://freecodecamp.org/news/css-box-model-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/FCC-Thumbnnail--2--1.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Propriétés du modèle de boîte CSS – Expliqué avec des exemples ✨
seo_desc: "Today we're gonna learn how to use the CSS box model with examples. This\
  \ will help you make pixel perfect websites and will teach you to use the box-sizing,\
  \ margin, padding, and border properties more accurately. \nWe're also going to\
  \ see some practic..."
---

Aujourd'hui, nous allons apprendre à utiliser le **modèle de boîte CSS** avec des exemples. Cela vous aidera à créer des sites web pixel perfect et vous apprendra à utiliser les propriétés box-sizing, margin, padding et border plus précisément. 

Nous allons également voir quelques cas d'utilisation pratiques pour ces propriétés. Commençons 💡

## Table des matières

* **[Pourquoi apprendre le modèle de boîte CSS ?](#heading-pourquoi-apprendre-le-modèle-de-boîte-css)**
* [Diagramme du modèle de boîte CSS](#heading-diagramme-du-modèle-de-boîte-css)
* [La propriété Padding](#heading-la-propriété-padding)
* [La propriété Border](#heading-la-propriété-border)
* [La propriété Margin](#heading-la-propriété-margin)
* [La propriété **box-sizing**](#heading-la-propriété-box-sizing)
* [Content-box **VS** Border-box](#heading-quelle-est-la-différence-entre-content-box-et-border-box-en-css)

![Sujets abordés : diagramme du modèle de boîte, padding, border, margin, box-sizing et raccourcis](https://www.freecodecamp.org/news/content/images/2021/07/Frame-7--2-.png)
_**Sujets abordés**_

### Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/WJ8Yoi04XvQ]

## Pourquoi apprendre le modèle de boîte CSS ?

![Pourquoi apprendre le modèle de boîte CSS ?](https://www.freecodecamp.org/news/content/images/2021/07/YT-Thumbnail.png)

Le modèle de boîte CSS comprend les propriétés **box-sizing, padding** et **margin**. Si vous ne les utilisez **pas**, votre site web ressemblera à ceci 👋

![Un site web sans margin ni padding](https://www.freecodecamp.org/news/content/images/2021/07/Page-1-1.png)
_**Un site web sans margin ni padding**_

Mais si vous utilisez correctement les propriétés du modèle de boîte, votre site web ressemblera à ceci 👋

![Même image du site web avec padding et bonne utilisation des autres propriétés du modèle de boîte](https://www.freecodecamp.org/news/content/images/2021/07/Page-1--1-.png)
_**Un site web utilisant les propriétés du modèle de boîte**_

Beaucoup plus visuellement attrayant, n'est-ce pas ? Si vous voulez créer votre site web avec des calculs précis, comme celui ci-dessus 👆 alors ce sujet est pour vous. Apprendre le modèle de boîte CSS est l'une des nombreuses façons qui vous aideront à créer des **sites web pixel perfect.**

Cet article parlera de la façon d'utiliser ces propriétés :

* Padding
* Margin
* Border
* box-sizing

## Comment utiliser les propriétés du modèle de boîte CSS

Regardons quelques exemples où nous pouvons utiliser les propriétés du modèle de boîte CSS. Nous allons disséquer le site web montré ci-dessus. 👆

Examinons de plus près la **navbar**. Vous pouvez remarquer la différence entre l'exemple qui utilise la propriété padding et celui qui ne l'utilise pas : 

![Avant et après d'une navbar avec et sans padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-47.png)
_**Éléments de la navbar utilisant la propriété padding**_

Maintenant, examinons de plus près la **section de contenu ainsi que les boutons**. Encore une fois, vous remarquerez la différence – celui de droite utilise également la propriété **padding**. 

![Avant et après du contenu avec et sans padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-48.png)
_**Une section de contenu utilisant la propriété padding**_

## Diagramme du modèle de boîte CSS

Pensez au modèle de boîte CSS comme à un **oignon**. Il a **4 couches** :

* **1ère** couche : Contenu
* **2ème** couche : Padding
* **3ème** couche : Border
* **4ème** couche : Margin

### 1ère couche du modèle de boîte : Contenu

En HTML, **tout se comporte comme une boîte**. Insérons du contenu avec une image de chaton. 👋

![Image de chat mignon pour démontrer le contenu dans le modèle de boîte](https://www.freecodecamp.org/news/content/images/2021/07/Frame-1--1--1.png)
_**1ère couche du modèle de boîte : contenu**_

### 2ème couche du modèle de boîte : Padding

La couche suivante du modèle de boîte CSS est la couche **padding**. Elle enveloppe notre contenu comme ceci 👋

![Même image de chat mignon ci-dessus avec du padding autour](https://www.freecodecamp.org/news/content/images/2021/07/Frame-2-2.png)
_**2ème couche du modèle de boîte : padding**_

### 3ème couche du modèle de boîte : Border

La couche suivante du modèle de boîte CSS est la couche **border**. Elle enveloppe notre contenu + padding comme ceci 👋 

![Une bordure autour de l'image du chat ci-dessus](https://www.freecodecamp.org/news/content/images/2021/07/Frame-3--1-.png)
_**La ligne pointillée noire est la bordure**_

### 4ème couche du modèle de boîte : Margin

La couche suivante et finale du modèle de boîte CSS est la couche **margin**. Elle enveloppe notre contenu + padding + bordure comme ceci 👋

![Margin à l'extérieur de l'image du chat](https://www.freecodecamp.org/news/content/images/2021/07/Margin.png)
_**Région grise est la Margin**_

Très bien, voyons comment ces propriétés fonctionnent dans un projet.

## Comment configurer le projet

![Codons ensemble](https://www.freecodecamp.org/news/content/images/2021/07/Frame-8.png)

Ce tutoriel est **bon pour tout le monde, y compris les débutants.** Si vous voulez coder en même temps, suivez ces étapes. 

### HTML

Ouvrez VS Code ou [Codepen.io](http://codepen.io/) et écrivez ce code 👋 à l'intérieur de la **balise body** :

```html
<div class="box-1"> Box-1 </div>
```

### CSS

Effacez les styles par défaut de notre navigateur 👋

```css
* {
  margin: 0px;
  padding: 0px;
  font-family: sans-serif;
}

```

Maintenant, stylisons notre boîte 👋

```css
.box-1 {
  width: 300px;
  background-color: skyblue;
  font-size: 50px;
}
```

Nous sommes prêts, commençons à coder ! ✨

![Chien buvant un bubble tea](https://www.freecodecamp.org/news/content/images/2021/07/Frame-9.png)

## La propriété Padding

Mais d'abord, discutons des **utilisations pratiques** de la propriété padding. Ensuite, nous verrons comment utiliser cette propriété.

Généralement, j'utilise le padding pour mettre de l'espace entre les contenus. Regardez cette **navbar** 👋

![Navbar avec padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-47-1.png)
_**Éléments de la navbar utilisant la propriété padding**_

Voici un autre exemple pour vous – regardez le contenu ci-dessous, avec deux boutons 👋

![Contenu avec padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-48-1.png)
_**Section de contenu utilisant la propriété padding**_

### Comment utiliser la propriété padding en CSS

Voici le **raccourci** des quatre propriétés de padding :

* padding-top
* padding-right
* padding-bottom
* padding-left

![Raccourci de padding](https://www.freecodecamp.org/news/content/images/2021/07/Frame-10.png)
_**Raccourci de la propriété padding**_

Et rappelez-vous, le padding est l'espace que vous ajoutez au-dessus de votre **contenu principal** :

![Image de chat montrant le padding](https://www.freecodecamp.org/news/content/images/2021/07/Padding.png)
_**2ème couche du modèle de boîte : Padding**_

Ajoutons du padding à notre contenu. **La zone colorée en rouge est le padding 👋**

![La zone colorée en rouge est le padding](https://www.freecodecamp.org/news/content/images/2021/07/bmnmmmmm.gif)
_**La zone colorée en rouge est le padding**_

Pour recréer les résultats ci-dessus, ✍ écrivez ce code dans votre CSS : 👋

```css
// Padding ajouté en haut, à droite, à gauche, en bas de .box-1

.box-1{
   padding : 100px;
}
```

Ouvrons notre console de développement et **allons dans la section computed** :

![Image de la console de développement du modèle de boîte et du padding](https://www.freecodecamp.org/news/content/images/2021/07/a.png)
_**Modèle de boîte CSS calculé**_

Tout au milieu se trouve notre **contenu** qui fait **300px** de large. Regardez autour de notre contenu, nous avons ajouté un **padding de 100px** tout autour.

Essayons d'ajouter du padding à un seul côté de notre contenu (uniquement le côté droit) :

![Image montrant le padding-right](https://www.freecodecamp.org/news/content/images/2021/07/Frame-11--1-.png)
_**Propriété padding-right**_

Pour recréer les résultats ci-dessus, ✍ écrivez ce code dans votre CSS : 👋

```css
.box-1{
   padding: 0 100px 0 0;
}

// Ou vous pouvez utiliser 👋

.box-1{
   padding-right: 100px;
}
```

Maintenant, ouvrez la section computed sur votre console de développement 👋

![Image de la console de développement montrant le padding-right](https://www.freecodecamp.org/news/content/images/2021/07/s.png)
_**Modèle de boîte CSS calculé**_

Regardez ✍ – le padding de 100px n'a été ajouté que sur le **côté droit** de notre contenu comme nous l'avons spécifié.

## La propriété Border

Vous utiliserez couramment la propriété border **lors de la création de boutons**. Voici une démonstration GIF 👋

![Image montrant le survol d'une souris sur des boutons pour démontrer la propriété border](https://media.giphy.com/media/iUTNdCt5RVTXlD7ARq/giphy.gif)
_**Boutons utilisant la propriété border**_

Remarquez comment une **bordure de couleur blanche** apparaît autour du bouton lorsque je survole le bouton avec la souris.

### Comment utiliser la propriété border en CSS

Et rappelez-vous, la **border** est l'espace ajouté au-dessus de notre **contenu principal + padding** : **👋**

![Image de chat avec une ligne pointillée noire comme bordure](https://www.freecodecamp.org/news/content/images/2021/07/Border.png)
_**La ligne pointillée noire est la bordure**_

Il y a trois entrées cruciales de la propriété border :

* taille de la bordure
* style de la bordure : **solid / dotted/ dashed**
* couleur de la bordure

![Syntaxe de la propriété border](https://www.freecodecamp.org/news/content/images/2021/07/Frame-23.png)
_**Syntaxe de la propriété border**_

Il y a trois styles de propriété border comme je l'ai listé ci-dessus. Dans cet exemple, nous utiliserons le style **dashed** :

![Une boîte avec du contenu, du padding et une ligne pointillée noire comme bordure](https://www.freecodecamp.org/news/content/images/2021/07/Frame-22.png)

Pour recréer les résultats ci-dessus, écrivez ce code dans votre CSS : 👋

```css
.box-1 {
  width: 300px;
  font-size: 50px;
  padding: 50px;
  border: 10px dashed black;
}

```

Ouvrons notre console et voyons les calculs du modèle de boîte :

![Image du modèle de boîte calculé dans la console de développement](https://www.freecodecamp.org/news/content/images/2021/07/dxcxcvbxc-1.png)
_**Modèle de boîte CSS calculé**_

Maintenant, regardez l'image ci-dessus✍ – une bordure de 10px est ajoutée tout autour de notre **contenu + padding**.

## La propriété Margin

Généralement, j'utilise la propriété **margin** pour mettre un **espace blanc** entre mon contenu et l'écran principal sur la mise en page de bureau (grands écrans). Regardez ce GIF : 👋

![Ajout de margin à un site web](https://www.freecodecamp.org/news/content/images/2021/07/rea.gif)
_**Ajout de margin à un site web**_

Remarquez que j'ajoute la margin aux bords gauche et droit de mon site web ci-dessus 👆 

Voici un autre exemple GIF d'**un cas d'utilisation** de la propriété margin : 👋

![Ajout de margin à un site web](https://www.freecodecamp.org/news/content/images/2021/07/reammmmm.gif)
_**Ajout de margin à un site web**_

### Comment utiliser la propriété margin en CSS

Voici le **raccourci** pour les quatre propriétés de la propriété margin :

* margin-top
* margin-right
* margin-bottom
* margin-left

![Raccourci de la propriété margin](https://www.freecodecamp.org/news/content/images/2021/07/Frame-12.png)
_**Raccourci de la propriété margin**_

Et rappelez-vous, **margin** est l'espace ajouté au-dessus de notre **contenu principal + padding + border** :

![Image de chat avec une margin grise](https://www.freecodecamp.org/news/content/images/2021/07/Margin-1.png)
_**La région grise est la margin**_

Ajoutons une margin à notre contenu. **Le contenu est repoussé en raison de la Margin** dans ce GIF :👋

![Contenu repoussé en raison de la margin](https://www.freecodecamp.org/news/content/images/2021/07/agid.gif)
_**Contenu repoussé en raison de la margin**_

Pour recréer les résultats ci-dessus, écrivez ce code dans votre CSS : 👋

```css
.box-1 {
  padding: 50px;
  border: 10px dashed black;
  
  margin: 50px;
}
```

Nous pouvons vérifier les calculs à nouveau : 👋

![Image de la console de développement montrant une margin](https://www.freecodecamp.org/news/content/images/2021/07/klkjkj.png)
_**Modèle de boîte CSS calculé**_

Regardez, une margin de 50px a été ajoutée tout autour de notre **contenu + padding + border**.

Essayons d'ajouter une **margin** à un seul côté de notre contenu (uniquement le côté gauche) :

![La propriété margin-left](https://www.freecodecamp.org/news/content/images/2021/07/Frame-22--2-.png)
_**La propriété margin-left**_

Pour recréer les résultats ci-dessus, écrivez ce code dans votre CSS 👋

```css
.box-1 {
  padding: 50px;
  border: 10px dashed black;
  
  margin-left: 50px;
}
```

Sur la console, nous pouvons voir qu'une **margin de 50px** a été appliquée uniquement sur le **côté gauche** 👋

![Image de la console de développement montrant la propriété margin-left](https://www.freecodecamp.org/news/content/images/2021/07/vbnvbnbnbv.png)
_**Modèle de boîte CSS calculé**_

## Faites une pause !

Jusqu'à présent, tout va bien ✍ – faites une pause ! Vous le méritez 💡

![Chien buvant un bubble tea](https://www.freecodecamp.org/news/content/images/2021/07/Frame-24--1-.png)

## La propriété Box-sizing

Cette propriété définit comment notre margin, padding et borders seront calculés. Il existe trois types de calculs (vous pouvez les appeler valeurs) :

* border-box
* padding-box
* content box

### Note :

Nous ne allons pas discuter de **box-sizing: padding-box**, car seul Firefox le supporte et il n'est pas très utilisé.

## Quelle est la différence entre content-box et border-box en CSS ?

Les deux, border-box et content-box, fonctionnent de la même manière. Regardez ces images :👋

![Boîtes utilisant la valeur border-box](https://www.freecodecamp.org/news/content/images/2021/07/Frame-15.png)
_**Boîtes utilisant la valeur border-box**_

![Boîtes utilisant la valeur content-box](https://www.freecodecamp.org/news/content/images/2021/07/Frame-17.png)
_**Boîtes utilisant la valeur content-box**_

Alors, quelle est la principale différence ici ? La différence est notable lorsque nous ajoutons une margin, une border ou un padding à nos boîtes. 

Lorsque nous utilisons **box-sizing: content-box**, qui est la valeur par défaut, elle **ajoutera** une margin, un padding et des borders **à l'extérieur de la boîte**, comme ceci : 👋

![Padding, appliqué à l'extérieur de la boîte](https://www.freecodecamp.org/news/content/images/2021/07/abcdefg.gif)
_**Padding appliqué à l'extérieur de la boîte**_

Vous pouvez voir les calculs ici aussi : 👋

![Calculs avec content-box](https://www.freecodecamp.org/news/content/images/2021/07/Frame-19.png)
_**Calculs avec content-box**_

Ce qui signifie que les choses peuvent échapper à tout contrôle et vous verrez des calculs inattendus. Cela signifie qu'il est **difficile de créer des sites web responsives.** Utilisez toujours la propriété **box-sizing: border-box** à la place.

Mais lorsque nous utilisons la propriété **box-sizing: border-box**, elle **ajoutera** une margin, un padding et des borders **à l'intérieur de la boîte**, comme ceci :👋

![Padding appliqué à l'intérieur de la boîte](https://www.freecodecamp.org/news/content/images/2021/07/c-box.gif)
_**Padding appliqué à l'intérieur de la boîte**_

La propriété **box-sizing: border-box** nous montre les calculs **EXACTS** de nos éléments HTML, ce qui signifie que cette valeur est **idéale pour créer des sites web responsives.**

Vous pouvez également expérimenter avec les valeurs ✍ – suivez simplement ce code : 👋

```css
* {
  box-sizing: border-box;
}

/* Ou, écrivez 👋 */

* {
  box-sizing: content-box;
}
```

## Conclusion

Félicitations ! Vous pouvez maintenant créer des **sites web pixel perfect.** Non seulement cela, mais lorsque vous codez, vous pouvez comprendre pourquoi votre contenu se comporte étrangement.

Voici votre médaille pour avoir lu jusqu'à la fin ❤️

## Suggestions & Critiques sont grandement appréciées ❤️

![Mains qui applaudissent et une médaille d'or](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube [/ Joy Shaheb](https://youtube.com/c/joyshaheb)**

**LinkedIn [/ JoyShaheb](https://www.linkedin.com/in/joyshaheb/)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**

## Crédits

* [Images de Freepik](https://www.freepik.com/collection/css-box-model-vectors/2187534)