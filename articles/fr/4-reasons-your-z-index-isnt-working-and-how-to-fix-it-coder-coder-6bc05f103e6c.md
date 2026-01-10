---
title: 4 raisons pour lesquelles votre z-index ne fonctionne pas (et comment le corriger)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-25T16:38:07.000Z'
originalURL: https://freecodecamp.org/news/4-reasons-your-z-index-isnt-working-and-how-to-fix-it-coder-coder-6bc05f103e6c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nm4AWKx-ezJBFLGShJCVAw.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 4 raisons pour lesquelles votre z-index ne fonctionne pas (et comment le
  corriger)
seo_desc: 'By Jessica Chan

  Z-index is a CSS property that allows you to position elements in layers on top
  of one another. It’s super useful, and honestly a very important tool to know how
  to use in CSS.

  Unfortunately, z-index is one of those properties that do...'
---

Par Jessica Chan

Z-index est une propriété CSS qui vous permet de positionner des éléments en couches les uns sur les autres. C'est super utile, et honnêtement un outil très important à savoir utiliser en CSS.

Malheureusement, z-index est l'une de ces propriétés qui ne se comportent pas toujours de manière intuitive. Cela semble simple au premier abord : un nombre de z-index plus élevé signifie que l'élément sera au-dessus des éléments avec des nombres de z-index plus bas. Mais il y a des règles supplémentaires qui compliquent les choses. Et vous ne pouvez pas toujours tout corriger en définissant le z-index à 999999 ! ?

Cet article expliquera en détail quatre des raisons les plus courantes pour lesquelles z-index ne fonctionne pas pour vous, et exactement comment vous pouvez le corriger.

Nous allons passer en revue quelques exemples de code réels et les résoudre. Après avoir lu cet article, vous serez en mesure de comprendre et d'éviter ces pièges courants de z-index !

%[https://www.youtube.com/watch?v=qYi-OLf5q5g]

Examinons la première raison :

### 1. Les éléments dans le même contexte de superposition s'afficheront dans l'ordre d'apparition, avec les éléments ultérieurs au-dessus des éléments précédents.

Dans notre premier exemple, nous avons une mise en page relativement simple qui comprend 3 éléments principaux :

* Une image d'un chat
* Un bloc blanc avec du texte
* Une autre image du même chat

Voici le balisage HTML pour cela :

```html
<div class="cat-top"></div> 

<div class="content__block"> Meow meow meow... </div> 

<div class="cat-bottom"></div>
```

Dans cette mise en page, nous voulons idéalement que le bloc de texte blanc soit au-dessus des deux chats.

Pour essayer d'y parvenir, nous avons ajouté des marges négatives au CSS pour les deux images de chat, afin qu'elles chevauchent un peu le bloc blanc :

```css
.cat-top { 
   margin-bottom: -110px; 
} 

.cat-bottom { 
   float: right; 
   margin-top: -120px; 
}
```

Cependant, cela ressemble à ceci :

<iframe height="600" width="800" style="width: 100%;" scrolling="no" title="Z-index: #1: set position, #2: natural stacking order, #3: CSS properties" src="//codepen.io/thecodercoder/embed/XQEyeX/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/thecodercoder/pen/XQEyeX/'>Z-index: #1: set position, #2: natural stacking order, #3: CSS properties</a> by Jessica
  (<a href='https://codepen.io/thecodercoder'>@thecodercoder</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

Le premier chat est effectivement positionné sous le bloc de contenu blanc, comme nous le voulons. Mais la deuxième image de chat est positionnée au-dessus du bloc !

Pourquoi cela se produit-il ?

La raison de ce comportement est due à l'**ordre de superposition naturel** sur la page web. Ces directives déterminent essentiellement quels éléments seront au-dessus et lesquels seront en dessous.

Même si les éléments n'ont pas leur z-index défini, il y a une raison à ceux qui seront au-dessus.

Dans notre cas, aucun des éléments n'a de valeur de z-index. Leur ordre de superposition est donc déterminé par leur ordre d'apparition. Selon cette règle, les éléments qui apparaissent plus tard dans le balisage seront au-dessus des éléments qui les précèdent.

(Vous pouvez lire plus de directives sur l'ordre de superposition sur le réseau des développeurs Mozilla [ici](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).)

Dans notre exemple avec les chats et le bloc blanc, ils obéissent à cette règle. C'est pourquoi le premier chat est sous l'élément de bloc blanc, et le bloc blanc est sous le deuxième chat.

D'accord, l'ordre de superposition est bien et bon, mais comment corriger le CSS pour que le deuxième chat soit sous le bloc blanc ?

Examinons la deuxième raison :

### 2. L'élément n'a pas sa position définie

L'une des autres directives qui déterminent l'ordre de superposition est de savoir si un élément a sa position définie ou non.

Pour définir la position d'un élément, ajoutez la propriété CSS `position` à autre chose que `static`, comme `relative` ou `absolute`. (Vous pouvez en lire plus à ce sujet dans [cet article](https://coder-coder.com/css-position-layout/) que j'ai écrit.)

Selon cette règle, les éléments positionnés s'afficheront au-dessus des éléments non positionnés.

Ainsi, définir le bloc blanc pour qu'il soit `position: relative`, et laisser les deux éléments de chat non positionnés placera le bloc blanc au-dessus des chats dans l'ordre de superposition.

Voici à quoi cela ressemblera - vous pouvez également jouer avec le Codepen ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/NlDhNhhBXrXmR35aZCt4XCGbfBCt4bRPLHzK)

Hourra !

Maintenant, la prochaine chose que nous voulons faire est de faire tourner le chat du bas à l'envers, en utilisant la propriété `transform`. De cette façon, les deux chats seront sous le bloc blanc, avec seulement leurs têtes qui dépassent.

Mais faire cela peut causer plus de confusion liée au `z-index`. Nous aborderons le problème et la solution dans la prochaine partie.

### 3. La définition de certaines propriétés CSS comme l'opacité ou la transformation placera l'élément dans un nouveau contexte de superposition.

Comme nous venons de le mentionner, nous voulons retourner le chat du bas à l'envers. Pour y parvenir, nous ajouterons `transform: rotate(180deg)`.

```css
.cat-bottom { 
   float: right; 
   margin-top: -120px; 
   transform: rotate(180deg); 
}
```

Mais cela fait que le chat du bas est affiché au-dessus du bloc blanc à nouveau !

![Image](https://cdn-media-1.freecodecamp.org/images/GTJjexmzYUkJa37hDuIUALqGngUjSl0wxFcE)

_Qu'est-ce qui se passe ici ??_

Vous ne rencontrerez peut-être pas souvent ce problème, mais un autre aspect de l'ordre de superposition est que certaines propriétés CSS comme `transform` ou `opacity` placeront l'élément dans son propre nouveau [contexte de superposition](https://www.w3.org/TR/css-color-3/#transparency).

Cela signifie que l'ajout de `transform` à l'élément `.cat-bottom` le fait se comporter comme s'il avait un `z-index` de 0. Même s'il n'a pas du tout sa `position` ou son `z-index` défini ! (W3.org a une documentation informative mais [plutôt dense](https://www.w3.org/TR/css-color-3/#transparency) sur le fonctionnement de cela avec la propriété `opacity`)

Rappelons que nous n'avons jamais ajouté de valeur `z-index` au bloc blanc, seulement `position: relative`. Cela suffisait pour positionner le bloc blanc au-dessus des chats non positionnés.

Mais puisque l'élément `.bottom-cat` agit comme s'il était positionné relativement avec `z-index: 0`, le transformer l'a positionné au-dessus du bloc blanc.

La solution à cela est de définir `position: relative` et de définir explicitement `z-index` au moins sur le bloc blanc. Vous pourriez aller plus loin et définir `position: relative` et un `z-index` plus bas sur les éléments de chat, juste pour être extra prudent.

```css
.content__block { 
   position: relative; 
   z-index: 2; 
} 

.cat-top, .cat-bottom { 
   position: relative; z-index: 1; 
}
```

À mon avis, faire cela résoudra la plupart, sinon tous les problèmes de base de z-index.

Maintenant, passons à notre dernière raison pour laquelle votre `z-index` ne fonctionne pas. Celle-ci est un peu plus complexe, car elle implique des éléments parents et enfants.

### 4. L'élément est dans un contexte de superposition inférieur en raison du niveau de z-index de son parent

Examinons notre exemple de code pour cela :

<iframe height="600" width="800" style="width: 100%;" scrolling="no" title="Z-index: #4 different stacking contexts" src="//codepen.io/thecodercoder/embed/qwYdZw/?height=265&theme-id=0&default-tab=html,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/thecodercoder/pen/qwYdZw/'>Z-index: #4 different stacking contexts</a> by Jessica
  (<a href='https://codepen.io/thecodercoder'>@thecodercoder</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

Voici ce que nous avons : une simple page web avec du contenu régulier, et un onglet latéral rose qui dit « Envoyer un retour » qui est positionné au-dessus du contenu.

Ensuite, lorsque vous cliquez sur la photo du chat, une fenêtre modale avec un calque de superposition de fond gris transparent s'ouvre.

Cependant, même lorsque la fenêtre modale est ouverte, l'onglet latéral est toujours au-dessus du calque de superposition gris. Nous voulons que le calque de superposition soit affiché par-dessus tout, y compris l'onglet latéral.

Examinons le CSS des éléments en question :

```css
.content { 
   position: relative; 
   z-index: 1; 
} 

.modal { 
   position: fixed; 
   z-index: 100; 
} 

.side-tab { 
   position: fixed; 
   z-index: 5; 
}
```

Tous les éléments ont leur position définie, et l'onglet latéral a un `z-index` de 5, ce qui le positionne au-dessus de l'élément de contenu, qui est à `z-index: 1`.

Ensuite, la modale a `z-index: 100` qui devrait la placer au-dessus de l'onglet latéral à `z-index: 5`. Mais au lieu de cela, le calque de superposition de la modale est sous l'onglet latéral.

Pourquoi cela se produit-il ?

Précédemment, nous avons abordé certains facteurs qui entrent dans le contexte de superposition, tels que si l'élément a sa position définie, ainsi que son ordre dans le balisage.

**Mais un autre aspect du contexte de superposition est qu'un élément enfant est limité au contexte de superposition de son parent.**

Examinons de plus près les trois éléments en question.

Voici le balisage que nous avons :

```css
<section class="content">            
    <div class="modal"></div>
</section>

<div class="side-tab"></div>
```

En regardant le balisage, nous pouvons voir que les éléments de contenu et d'onglet latéral sont des frères. C'est-à-dire qu'ils existent au même niveau dans le balisage (ce qui est différent du niveau de z-index). Et la modale est un élément enfant de l'élément de contenu.

Parce que la modale est à l'intérieur de l'élément de contenu, son `z-index` de 100 n'a d'effet qu'à l'intérieur de son parent, l'élément de contenu. Par exemple, s'il y avait d'autres éléments enfants qui étaient frères de la modale, leurs valeurs de `z-index` les placeraient les uns au-dessus ou en dessous des autres.

Mais la valeur de `z-index` de ces éléments enfants ne signifie rien en dehors du parent, car l'élément parent de contenu a son `z-index` défini à 1.

Ainsi, ses enfants, y compris la modale, ne peuvent pas sortir de ce niveau de `z-index`.

(Vous pouvez vous en souvenir avec cette métaphore légèrement déprimante : un enfant peut être limité par ses parents et ne peut pas se libérer d'eux.)

Il y a quelques solutions à ce problème :

### Solution : Déplacer la modale en dehors du parent de contenu et dans le contexte de superposition principal de la page.

Le balisage corrigé ressemblerait alors à ceci :

```css
<section class="content"></section>

<div class="modal"></div>

<div class="side-tab"></div>
```

Maintenant, l'élément modale est un élément frère des deux autres. Cela place les trois éléments dans le même contexte de superposition qu'eux, de sorte que chacun de leurs niveaux de z-index affectera désormais les uns les autres.

Dans ce nouveau contexte de superposition, les éléments s'afficheront dans l'ordre suivant, de haut en bas :

* modale (`z-index: 100`)
* onglet latéral (`z-index: 5`)
* contenu (`z-index: 1`)

### Solution alternative : Supprimer le positionnement du contenu, afin qu'il ne limite pas le z-index de la modale.

Si vous ne voulez pas ou ne pouvez pas changer le balisage, vous pouvez corriger ce problème en supprimant le paramètre `position` de l'élément de contenu :

```css
.content { 
   // Aucune position définie 
} 

.modal { 
   position: absolute; 
   z-index: 100; 
} 

.side-tab { 
   position: absolute; 
   z-index: 5; 
}
```

Puisque l'élément de contenu n'est plus positionné, il ne limitera plus la valeur de `z-index` de la modale. Ainsi, la modale ouverte sera positionnée au-dessus de l'élément d'onglet latéral, en raison de son `z-index` plus élevé de 100.

Bien que cela fonctionne, personnellement, je choisirais la première solution.

Car si pour une raison quelconque dans le futur vous devez positionner l'élément de contenu, il limitera à nouveau l'ordre de la modale dans le contexte de superposition.

### En résumé

J'espère que vous avez trouvé ce tutoriel utile ! Pour résumer, la plupart des problèmes avec z-index peuvent être résolus en suivant ces deux directives :

1. Vérifiez que les éléments ont leur position définie et que les nombres de z-index sont dans le bon ordre.
2. Assurez-vous que vous n'avez pas d'éléments parents limitant le niveau de `z-index` de leurs enfants.

#### Vous voulez plus ?

Je crée un cours sur le design réactif ! [Inscrivez-vous ici](https://coder-coder.com/responsive-design-beginners/) pour recevoir un email lorsque ce sera publié.

J'écris des tutoriels de développement web sur mon blog [coder-coder.com](https://coder-coder.com), je poste des mini-conseils sur [Instagram](https://www.instagram.com/thecodercoder/) et des tutoriels de codage sur [YouTube](https://www.youtube.com/c/codercodertv).