---
title: 'HTML/CSS : Aventures sur l''axe Z'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-05T20:17:29.000Z'
originalURL: https://freecodecamp.org/news/z-axis-html-css-z-index-layout-adventures-2419cefdc2ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4sV2vVFkeY-A9ZIZh_AUtw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'HTML/CSS : Aventures sur l''axe Z'
seo_desc: 'By Daniel Robinson

  Let’s jump straight to exploration and adventure.

  We start with three circles: each is a div filled in with “█” characters (ink blotches),
  so we can study the ordering of a divs contents separate from backgrounds and borders.
  The s...'
---

Par Daniel Robinson

Passons directement à l'exploration et à l'aventure.

Nous commençons avec trois cercles : chacun est une div remplie de caractères « █ » (taches d'encre), afin que nous puissions étudier l'ordre du contenu des divs séparément des arrière-plans et des bordures. Le HTML initial ressemble à ceci :

```
<body> <div id="one" class="circle"> ██████<br/>██████<br/>██████<br/>██████<br/>██████ </div> <div id="two" class="circle"> ██████<br/>██████<br/>██████<br/>██████<br/>██████ </div> <div id="three" class="circle"> ██████<br/>██████<br/>██████<br/>██████<br/>██████ </div></body>
```

Et le CSS :

```
.circle { width: 72px; height: 72px; overflow: hidden; line-height: 16px; border-radius: 100%; box-sizing: border-box;}
```

```
#one { margin-left: 27px; color: red;}
```

```
#two { margin-top: -36px; color: blue;}
```

```
#three { margin-top: -72px; margin-left: 56px; color: green;}
```

Ce HTML/CSS produit la première image ci-dessus. Trois cercles se chevauchent dans l'ordre où ils ont été définis. Bien. Ajoutons quelques bordures :

```
div {   border: 6px solid black;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/bpgUMIsMOCbHV4e2FSrl2IwwtqoKp4-i2rBk)
*Les bordures sont à l'arrière avec le contenu empilé à l'avant.*

Peut-être que cela vous surprend. Les bordures sont derrière même si le contenu reste à l'avant. Les bordures sont-elles également empilées ? Une touche de couleur :

```
#two {  border-color: grey;}
```

```
#three {  border-color: white;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/KQgZWKWh3mXCB8gl2wV69W8kGMPqS08qmz4c)
*L'ordre d'empilement des bordures est le même que l'ordre d'empilement du contenu, mais indépendant.*

Oui, l'ordre des divs dans le HTML décide de l'ordre des bordures les unes par rapport aux autres, et du contenu les uns par rapport aux autres, mais l'ordre entre les bordures et le contenu est : les bordures passent derrière le contenu.

Voici des plunkers pour les exemples jusqu'à présent : [début](https://plnkr.co/edit/osQgt6?p=preview), [bordures noires](https://plnkr.co/edit/THwgYG?p=preview), [bordures colorées](https://plnkr.co/edit/ZHSxBZ?p=preview).

Jusqu'à présent, les trois divs ont eu le type de positionnement par défaut : static. Positionnons-les (code complet dans le [plunker](https://plnkr.co/edit/REXUce?p=preview)) :

```
div {   border: 6px solid black;   position: relative;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/9f-qY5FHhEEfEp6M8oxvDTkHclby8lZ8Bzj4)
*Juste au moment où vous aviez compris que les bordures étaient 'séparées' ?*

Ok, donc les éléments 'positionnés' (valeur de position ≠ static) sont empilés ensemble : contenu, bordures et tout. Prochaine expérience ! ([plunker](https://plnkr.co/edit/REXUce?p=preview)) :

```
div {   border: 6px solid black;}
```

```
#one { position: relative; /* positionner uniquement la première div */}
```

![Image](https://cdn-media-1.freecodecamp.org/images/yn6jdF08eBLiaIVPrlM70vEpFFKFNKDzDZgx)
*Le cercle rouge est 'positionné', les autres ne le sont pas. Les éléments positionnés sont les plus 'hauts'.*

Bien, donc les éléments positionnés passent devant les éléments non positionnés. L'ordre basé uniquement sur les propriétés de mise en page a un certain nombre de cas. En voici un autre ([plunker](https://plnkr.co/edit/vpp2zN?p=preview)) :

```
#one { margin-left: 24px; color: red;}
```

```
#two { margin-top: -36px; margin-right: -20px; border-color: grey; color: blue; float: left;  /* la partie importante */}
```

```
#three { margin-top: -36px; border-color: white; color :green;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/jwcYwP4FX8mW-5TqgF4mVWvfHGAU9jK5vlQG)

Ici, le cercle bleu a été flotté à gauche, les deux autres cercles ne sont pas positionnés. La bordure et le contenu de la div deux se situent ensemble entre les bordures et les contenus respectifs des autres cercles. Un élément flottant agit beaucoup comme un élément positionné, où sa bordure et son contenu sont positionnés ensemble, sauf qu'il n'est pas au-dessus.

Sautons l'acte contenu+bordure pour un moment et jetons un coup d'œil au HTML imbriqué. [Ce codepen](http://codepen.io/designerzone/pen/YXVwGm) nous fait avancer rapidement.

```
<div class="black"></div><div class="gray">  <div class="lime"></div> <div class="yellow"></div> </div><div class="blue"></div>
```

```
(Le CSS définit uniquement les couleurs d'arrière-plan, les tailles de boîte et les marges)
```

![Image](https://cdn-media-1.freecodecamp.org/images/21zKGf0Xt5T1vdRc89prt2pZvTlY8bheJVe2)

Comme on pourrait s'y attendre, le HTML imbriqué crée un empilement par rapport à l'élément parent.

Concentrons-nous sur la partie imbriquée — réintroduisons les bordures et les contenus, mais ajoutons également les arrière-plans au mélange. Je vais expliquer le diagramme ci-dessous, mais voir le [plunker](https://plnkr.co/edit/rbKxnq?p=preview) pour le HTML/CSS complet :

![Image](https://cdn-media-1.freecodecamp.org/images/v4Zgb92swTz69uupPWM8F3Ghl-TZBUcqu9JK)

Nos divs circulaires d'avant sont devenues des carrés imbriqués. Le jaune est l'arrière-plan de la div externe, et le cramoisi en bas à droite est l'arrière-plan de la div interne interne (div trois).

La deuxième div n'a pas d'arrière-plan. Le débordement est autorisé. Dans un contexte imbriqué sans positionnement, les bordures sont à l'arrière dans l'ordre de l'imbrication.

Nous voyons également que les arrière-plans sont envoyés à l'arrière avec eux et sont également dans l'ordre de l'imbrication : le cramoisi est derrière le bleu mais au-dessus du jaune.

La première ligne de caractères verts a été supprimée pour vous montrer cet effet. Si nous ajoutons un positionnement à cela, nous obtenons un effet similaire à celui que nous avons eu avec les cercles — tout cet enfoncement de bordure/arrière-plan disparaît ([plunker](https://plnkr.co/edit/zChij4?p=preview)) :

```
div {  position: relative;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/Kh4k0qpf4wWXzpm8P2m8by7I8SYlbHToB35r)

Dans un contexte imbriqué avec positionnement, les enfants passent au-dessus des parents : bordures, arrière-plans, contenus et tout.

Si nous combinons tous les cas jusqu'à présent, nous pouvons générer la plupart des scénarios d'ordre des éléments avec juste des positions, des flottements et la structure HTML. Eh bien, du moins visuellement. Qu'en est-il de la capture d'événements ? Considérez ce qui suit :

```
<div id="one"></div><div id="two"></div><div id="three"></div>
```

```
div {  /* toutes les divs se chevauchent à 100% */  position: absolute;   top: 0;  bottom: 0;  left: 0;  right: 0;   background-color: white;}
```

```
#three {   background-color: lightblue;}
```

```
document.getElementById('one')  .addEventListener('mouseover',logTarget)
```

```
document.getElementById('two')  .addEventListener('mouseover',logTarget)
```

```
document.getElementById('three')  .addEventListener('mouseover',logTarget)
```

```
function logTarget(e){   console.log(e.target);}
```

Si vous déplacez votre souris dans la fenêtre du navigateur, quels événements _mouseover_ pensez-vous qui se déclencheront ?

Et si nous mettons à jour le HTML comme suit ?

```
<div id="one">  <div id="two">   <div id="three"></div>  </div></div>
```

Oui. Exactement. Avec le HTML en série, vous obtenez un événement. Avec l'imbriqué, vous en obtenez trois*. Malgré le fait que visuellement, la troisième div colorée couvre complètement les deux autres divs dans chaque cas, pour la capture d'événements, ce n'est pas le cas dans le cas imbriqué. Voir les plunkers [ici](https://plnkr.co/edit/Y7SMTtHqm2lga0to5g84?p=preview) et [ici](https://plnkr.co/edit/Rvb0zaEvCCQO87BRdjeb?p=preview).

*Trois événements avec une cible de la troisième div — elle est toujours au-dessus, donc la cible de l'événement mouseover s'applique à elle.

Jusqu'à présent, nous avons exploré l'ordre d'empilement naturel — l'ordre purement défini par la structure HTML et les propriétés de mise en page standard telles que position et float.

Nous avons vu que pour le contenu des éléments flottant < non positionné < positionné. Cependant, les éléments non positionnés ont leurs bordures/arrière-plans ordonnés tout à l'arrière, tandis que les éléments flottants et positionnés amènent les leurs avec eux. Nous avons également considéré l'ordre à la fois visuellement et par rapport à la capture d'événements.

Et si nous sortions de l'ordre d'empilement naturel en utilisant z-index ?

La propriété CSS z-index affecte les éléments positionnés. Nous avons vu que les éléments positionnés viennent à l'avant et amènent toutes leurs bordures et arrière-plans, mais autre que cela, ils étaient ordonnés dans l'ordre où ils étaient définis en HTML. Le z-index fournit simplement un moyen de sortir de ce contexte d'ordre HTML. Donc le premier exemple évident ([plunker](https://plnkr.co/edit/EPHDqI?p=preview)) :

```
div { width: 80px; height: 80px; position: relative; line-height: 16px; box-sizing: border-box;}
```

```
#one { background-color: red; z-index: 1;}
```

```
#two { background-color: blue; top: -80px;}
```

```
<body>  <div id="one"></div>  <div id="two"></div></body>
```

![Image](https://cdn-media-1.freecodecamp.org/images/wowe4g8Y5H0GDN5lH9rOarha8KnGOqPH7FsN)
*Nous verrions normalement la boîte bleue puisqu'elle a été définie en second, mais la rouge a un z-index de 1 ;*

Ensuite, c'est similaire avec le cas imbriqué, sauf que vous devez appliquer un négatif à l'élément enfant (nous verrons pourquoi bientôt) pour le même ([plunker](https://plnkr.co/edit/UQmeiD?p=preview)) :

```
.box { position: relative; width: 80px; height: 80px;}
```

```
#one { background-color: red;}
```

```
#two { background-color: blue; z-index: -1;} 
```

```
<div id="one" class="box">  <div id="two" class="box"></div></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/HwOiJR7sZH1l2TwRrDGvUuSmYmgkzf51vAXu)
*#two a été enfoncé derrière #one*

Si nous ajoutons également un z-index au parent :

```
#one { background-color: red;  z-index: 1;}
```

```
#two { background-color: blue; z-index: -1;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/MTxbJXh1a6ZHR-kn-CqQJgixV-TD2eA-SRBE)
*Erm huh ?*

Le z-index de l'enfant est « ignoré » dans ce cas. Cela peut devenir plus clair avec cet exemple ([plunker](https://plnkr.co/edit/9WpdxB?p=preview)) :

```
.box { position: absolute; width: 80px; height: 80px;}
```

```
#one { background-color: red; z-index: 2;}
```

```
#two { height: 60px; width: 60px; background-color: green; z-index: 1;}
```

```
#three {  background-color: blue;}
```

```
<div id="one" class="box"> <div id="two" class="box"></div> <div id="three" class="box"></div></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/XIKrwN3m-LxcLV6c7lqkQCNA1N2Fl5TKeasL)

L'imbrication avec l'utilisation du z-index crée un nouveau contexte d'empilement. Donc #one est à '2' par rapport à ses éléments frères, tandis que #two et #three sont à '1' et '0' respectivement l'un par rapport à l'autre, à l'intérieur de #one.

Cela peut prêter à confusion dans des situations comme celle-ci ([plunker](https://plnkr.co/edit/e27KLU?p=preview)) :

```
.box { position: absolute; width: 80px; height: 80px;}
```

```
#one { background-color: red; z-index: 2;}
```

```
#two { width: 100px; position: relative; z-index: 4;}
```

```
#three {  margin-top: 80px; background-color: blue; z-index: 2;}  <div id="one" class="box">  <div id="two" class="box">    Texte à l'intérieur de deux    Texte à l'intérieur de deux    Texte à l'intérieur de deux    Texte à l'intérieur de deux    Texte à l'intérieur de deux    Texte à l'intérieur de deux    Texte à l'intérieur de deux    Texte à l'intérieur de deux  </div></div><div id="three" class="box"></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/4OYl73Te9hvQjp9oq6xnyM8wyOYUBaUDdRY1)

Malgré le fait que le texte à l'intérieur de deux ait un z-index de 4, il est toujours derrière le carré bleu qui a un z-index de 2. Pourquoi ? Parce qu'il s'agit d'un z-index de 4, à l'intérieur d'un contexte d'empilement qui a un z-index de 2. Ensuite, parce que la troisième div est définie après la première div et est également à z-index 2, elle passe au-dessus. Bien sûr, si nous l'ajustons pour avoir un z-index à 1, il passe en dessous ([plunker](https://plnkr.co/edit/3LsRJv?p=preview)) :

```
#three {  margin-top: 80px; background-color: blue; z-index: 1;  /* était 2, maintenant 1 */}
```

![Image](https://cdn-media-1.freecodecamp.org/images/v6LalxTUbug41Oj8PixY5ZtRAulZCBmoBkmm)

Z-index n'est pas la seule propriété à créer un nouveau contexte sur le parent. L'opacité en est une autre :

```
#one { background-color: red; opacity: 0.99;}
```

```
#two { width: 100px; position: relative; z-index: 1;}
```

```
#three {  margin-top: 80px; background-color: blue;}
```

```
(même HTML que ci-dessus)
```

![Image](https://cdn-media-1.freecodecamp.org/images/4Mj-28L8aqjJbzjk-Vv2wfpgb8ZFRpvc3jhK)

À ce stade, [http://philipwalton.com/articles/what-no-one-told-you-about-z-index/](http://philipwalton.com/articles/what-no-one-told-you-about-z-index/) devrait commencer à être assez clair.

[https://www.smashingmagazine.com/2009/09/the-z-index-css-property-a-comprehensive-look/](https://www.smashingmagazine.com/2009/09/the-z-index-css-property-a-comprehensive-look/) est également une bonne lecture.

Parce qu'il y a une telle interaction massive de règles en cours, l'ordre de la pile peut devenir un peu ingérable, mais il est vrai que le premier article dit : les règles ne sont pas si difficiles à comprendre, elles ne sont simplement pas nécessairement ce à quoi on pourrait s'attendre.

La création de nouveaux contextes de pile est quelque chose avec lequel un développeur doit travailler pour obtenir le résultat souhaité dans les situations d'empilement vertical.

J'espère que vous avez eu une aventure en faisant défiler les couches de cet article.