---
title: Tutoriel CSS Flexbox avec une fiche mémo des propriétés Flexbox 🎖️
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2021-04-28T19:33:57.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-tutorial-with-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/FCC--Thumbnail-1.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: Web Design
  slug: web-design
seo_title: Tutoriel CSS Flexbox avec une fiche mémo des propriétés Flexbox 🎖️
seo_desc: 'In this article, I''ll teach you CSS Flexbox basics so you can make your
  own responsive sites. I''ll explain how each of Flexbox''s properties work, and
  I''ll give you a cheatsheet that covers everything you can do with Flexbox. Let''s
  Go 🎖️

  Table of Con...'
---

Dans cet article, je vais vous enseigner les bases du **CSS Flexbox** afin que vous puissiez créer vos propres sites responsive. J'expliquerai comment fonctionne chacune des propriétés de Flexbox, et je vous donnerai une fiche mémo qui couvre tout ce que vous pouvez faire avec Flexbox. C'est parti 🎖️

# Table des matières

* [Architecture Flexbox](#heading-architecture-flexbox)
* [flex-direction](#heading-la-propriete-flex-direction)
* [justify-content](#heading-la-propriete-justify-content)
* [align-content](#heading-la-propriete-align-content)
* [align-items](#heading-la-propriete-align-items)
* [align-self](#heading-la-propriete-align-self)
* [flex - grow | shrink | wrap | basis](#heading-les-proprietes-flex-grow-shrink-wrap-basis)
* [Raccourcis](#heading-proprietes-flexbox-raccourcies)
* [Conclusion](#heading-conclusion)

### Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/7YUR0Igl9eU]

# Tout d'abord, qu'est-ce que Flexbox ? 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Frame-4--2-.png)

Quand on construit une maison, on a besoin d'un plan. De la même manière, nous avons besoin d'un plan lorsque nous créons des sites web. Et Flexbox est ce plan.

Le modèle Flexbox nous permet de **disposer le contenu** de notre site web. De plus, il nous aide à créer les structures nécessaires pour concevoir des **sites web responsive** pour de multiples appareils. 

Voici une démo que j'ai créée en utilisant Flexbox comme plan principal.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Frame-35--1-.png)

Ce projet fait [partie de cet article](https://www.freecodecamp.org/news/learn-css-media-queries-by-building-projects/).

# Architecture Flexbox

Alors, comment fonctionne l'architecture Flexbox ? Les flex-items [Contenus] sont répartis le long de l'axe principal (main axis) et de l'axe transversal (cross axis). Et, selon la propriété flex-direction, la position de la mise en page change entre les lignes (rows) et les colonnes (columns).

![Flex Box model Architecture](https://dev-to-uploads.s3.amazonaws.com/i/hy2oqjvsbk60ef92nktg.png)

# Graphique Flexbox

Ce graphique contient toutes les propriétés et valeurs possibles que vous pouvez utiliser lorsque vous travaillez avec Flexbox. Vous pouvez vous y référer lors de vos projets et expérimenter différentes valeurs.

![Flex Box property Value Chart](https://dev-to-uploads.s3.amazonaws.com/i/gv3jyh4xt4fbwtq1qejn.png)

# Comment configurer le projet

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jphj7d3c3oh6dvx40ogy.png)

Pour ce projet, vous devez connaître un peu de HTML, de CSS et savoir utiliser VS Code. Suivez-moi pendant que nous réalisons les tâches suivantes :

1. Créez un dossier nommé "Project-1" et ouvrez VS Code
2. Créez les fichiers `index.html` et `style.css`
3. Installez Live Server et lancez-le.

Ou bien, vous pouvez simplement ouvrir [Codepen](https://codepen.io/) et commencer à coder.

À la fin de ce tutoriel, vous serez capable de réaliser des mises en page de sites web précises et esthétiques.

## HTML

En HTML, écrivez ces lignes de code à l'intérieur de la balise body 👇

```html
<div class="container">
    <div class="box-1"> A </div>
    <div class="box-2"> B </div>
    <div class="box-3"> C </div>
</div>

```

## CSS

Ciblez la classe `.container` et toutes les boîtes. Ensuite, stylisez les boîtes pour qu'elles se ressemblent toutes, comme ceci : 👇

**Note :** n'oubliez pas de définir la hauteur du conteneur.

```css
.container{
   height : 100vh;
}

[class ^="box-"]{
    width: 140px;
    height: 140px;
    background-color: skyblue;
    border: 2px solid black;

// Pour mieux voir la lettre
    font-size: 65px;
}

```

## Mais attendez....

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cq8exwor5aiciu2j6jwu.png)

Avant de commencer, vous devez comprendre la relation entre les classes parentes et enfants.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wzq3w0bys78fveqb9z0z.png)

Flexbox s'applique sur la **classe parente**, pas sur les classes enfants.

Ici, la classe `.container` est le **parent** et nos classes `.box-*` sont nos **enfants**.

Appliquez donc le `display: flex` à l'intérieur de la classe `.container`. Et placez les lettres au centre de la boîte comme ceci :

```css
.container{
    display : flex;
    height : 100vh;

// Pour ajouter de l'espace entre les boîtes
    gap : 25px;
}
[class ^="box-"]{
// Le code de l'étape précédente est ici

// Placer le texte au centre 
    display : flex;
    justify-content : center;
    align-items : center;
}

```

Et... nous sommes prêts ! Commençons à coder. 😊

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e4ufu718jzjopwn66ik8.png)

# La propriété flex-direction

Cette propriété nous permet de définir la direction et l'orientation dans lesquelles nos flex-items doivent être répartis à l'intérieur du flex-container.

![Flex Direction](https://dev-to-uploads.s3.amazonaws.com/i/n2ggh6yy4sbgltrx2i40.png)

![Flex Direction](https://dev-to-uploads.s3.amazonaws.com/i/6m9fg4n5a114q1va3b9p.png)

Pour recréer ces résultats, écrivons ces lignes dans notre CSS :

**Veuillez noter** que nous les écrirons à l'intérieur de la classe `.container`.

```css
.container{
//le code de l'étape de configuration est ici

// Modifiez la valeur 👇 ici pour voir les résultats
    flex-direction : row;
}

```

# La propriété justify-content

Cette propriété dispose les flex-items le long de l'**AXE PRINCIPAL** à l'intérieur du flex-container.

![justify content](https://dev-to-uploads.s3.amazonaws.com/i/a5lhkhbhi7hxwjgyvl5x.png)

![justify content](https://dev-to-uploads.s3.amazonaws.com/i/1vyg5nf1w7plistni582.png)

Pour recréer ces résultats, écrivez ces lignes dans votre CSS :

```css
.container{
//le code de l'étape de configuration est ici

// Modifiez la valeur 👇 ici pour voir les résultats
    justify-content: flex-start;
}

```

# La propriété align-content

Cette propriété dispose les flex-items le long de l'**AXE TRANSVERSAL** à l'intérieur du flex-container. C'est similaire à **justify-content**.

![align content](https://dev-to-uploads.s3.amazonaws.com/i/nqvvc2rhf0vx3czy0rnr.png)

![align content](https://dev-to-uploads.s3.amazonaws.com/i/zeet3705rsmz77v66x3c.png)

Veuillez noter que sans la propriété **flex-wrap**, cette propriété ne fonctionne pas. Voici une démo :

```css
.container{

// Modifiez la valeur 👇 ici pour voir les résultats
    align-content: center;

// sans cette ligne, align-content ne fonctionnera pas
    flex-wrap: wrap;
}

```

# La propriété align-items

Cette propriété répartit les flex-items le long de l'**Axe Transversal**.

![align items](https://dev-to-uploads.s3.amazonaws.com/i/kt25wxicd7vm8ddtmq0l.png)

Pour recréer ces résultats, écrivons le code suivant en CSS :

```css
.container{
//le code de l'étape de configuration est ici

// Modifiez la valeur 👇 ici pour voir les résultats
    align-items: flex-end;
}

```

# La propriété align-self

Cette propriété fonctionne sur les classes enfants. Elle positionne l'élément sélectionné le long de l'**Axe Transversal**.

![align self](https://dev-to-uploads.s3.amazonaws.com/i/383cxj4ippb21vjq31q2.png)

Au total, nous avons 6 valeurs :

* flex-start
* flex-end
* center
* baseline
* stretch
* auto

Pour recréer les résultats, sélectionnez n'importe quel `.box-*` et écrivez le code suivant :

```css
.box-2{
// Modifiez la valeur 👇 ici pour voir les résultats
     align-self : center;
}

```

## Faites une pause

Tout va bien jusqu'ici. Faites une pause !

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Frame-45.png)

# Les propriétés flex - grow | shrink | wrap | basis

Les propriétés dont nous allons discuter maintenant fonctionneront lors du redimensionnement de la fenêtre. Plongeons dans le vif du sujet.

### flex-grow

Cette propriété augmente la taille d'un flex-item en fonction de la largeur du flex-container.

### flex-shrink

Cette propriété aide un flex-item à rétrécir en fonction de la largeur du flex-container. C'est l'opposé de flex-grow.

![flex grow flex shrink flex wrap](https://dev-to-uploads.s3.amazonaws.com/i/z094e3wehsoe8z6lsxnz.png)

Pour obtenir ces résultats, suivez-moi.

**Veuillez noter** que flex-grow et flex-shrink fonctionnent sur les classes enfants. Nous allons donc cibler toutes nos boîtes comme ceci :

```css
.box-1{
    flex-grow: 1;
}
.box-2{
    flex-grow: 5;
}
.box-3{
    flex-grow: 1;
}

```

Redimensionnez la fenêtre et vous verrez les résultats.

Pour dupliquer le résultat de flex-shrink, écrivez le code suivant :

**Veuillez noter** que vous devez d'abord supprimer la propriété flex-wrap, sinon cela ne fonctionnera pas.

```css
.box-1{
    flex-shrink: 1;
}
.box-2{
    flex-shrink: 5;
}
.box-3{
    flex-shrink: 1;
}

```

Maintenant, redimensionnez la fenêtre et vous verrez les résultats.

### flex-wrap

Cette propriété vous aide à définir le nombre de flex-items que vous voulez sur une ligne ou un rang.

![flex wrap flex grow flex shrink](https://dev-to-uploads.s3.amazonaws.com/i/fux9qc05e6rtat192vlm.png)

Cela fonctionne sur la classe parente `.container`. Écrivez donc le code suivant :

```css
.container{
    //les autres codes sont ici 
  
// Modifiez la valeur 👇 ici pour voir les résultats
    flex-wrap : wrap;
}

```

### flex-basis

C'est similaire à l'ajout d'une largeur (width) à un flex-item, mais en plus flexible. `flex-basis: 10em`, par exemple, fixera la taille initiale d'un flex-item à 10em. Sa taille finale dépendra de l'espace disponible, de flex-grow et de flex-shrink.

# Propriétés Flexbox raccourcies

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/eayovne50iwxx8ll5e01.png)

### Le raccourci flex 

C'est le raccourci pour les propriétés **flex-grow**, **flex-shrink** et **flex-basis** combinées.

![flex flex basis](https://dev-to-uploads.s3.amazonaws.com/i/onoxj7gs9xj4wuf87kjl.png)

Vous pouvez essayer cela en écrivant le code suivant :

**Veuillez noter** que cela ne fonctionne que sur les classes enfants :

```css
.box-2{
    flex : 2 1 30em;
}

```

### flex-flow

C'est le raccourci pour les propriétés **flex-direction** et **flex-wrap** :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/awniqyrepbha5jdquwxh.png)

Vous pouvez essayer cela en écrivant le code suivant :

**Veuillez noter** que cela ne fonctionne que sur la classe parente.

```css
.container{
    flex-flow : row wrap;
}

```

## place-content

C'est le raccourci pour les propriétés justify-content et align-content :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/72yaytxgighz0cjskp2e.png)

Dupliquons les résultats :

**Veuillez noter** que cela fonctionne sur la classe parente.

```css
.container{
    place-content : center flex-end;
}

```

## Plus de ressources 

Si vous voulez **exercer** vos connaissances sur Flexbox, vous pouvez [lire cet article que j'ai écrit](https://www.freecodecamp.org/news/learn-flexbox-build-5-layouts/) où vous **construirez cinq mises en page responsive en utilisant Flexbox**. Voici une démo :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Frame-5--2--1.png)

# Conclusion

Voici votre médaille pour avoir lu jusqu'au bout ❤️

### Les suggestions et les critiques sont grandement appréciées ❤️

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/usxsz1lstuwry3jlly4d.png)

**YouTube [/ Joy Shaheb](https://www.youtube.com/c/joyshaheb)**

**Twitter [/ JoyShaheb](https://twitter.com/JoyShaheb)**

**Instagram [/ JoyShaheb](https://www.instagram.com/joyshaheb/)**

## Crédits

   * [unicorn pack](https://www.flaticon.com/packs/unicorn-4), [Kitty Avatars](https://www.flaticon.com/packs/kitty-avatars-3)

   * [cat-1](https://www.flaticon.com/free-icon/cat_1864514?term=kitty&page=1&position=12&page=1&position=12&related_id=1864514&origin=search), [cat-2](https://www.flaticon.com/free-icon/cat_3629088?related_id=3629088), [dog](https://www.flaticon.com/free-icon/shiba_1623792?term=dog&related_id=1623792), [rabbit](https://www.flaticon.com/free-icon/rabbit_1807972?term=rabbit&page=1&position=13&page=1&position=13&related_id=1807972&origin=search)

   * [Astronaut](https://www.freepik.com/free-vector/cute-astronaut-holding-coffee-cup-cartoon-illustration-science-food-drink-icon-concept-flat-cartoon-style_10479412.htm#position=0), [unicorn cup](https://www.vecteezy.com/vector-art/668079-little-pony-in-coffee-cup), [rainbow cat](https://www.vecteezy.com/vector-art/668109-rainbow-cat-unicorn-mermaid)

   * [CSS Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

![Credits](https://dev-to-uploads.s3.amazonaws.com/i/uzo5e477tn0sc4oz3mec.png)