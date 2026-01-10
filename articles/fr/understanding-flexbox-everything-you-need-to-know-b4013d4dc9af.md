---
title: 'Comprendre Flexbox : Tout ce que vous devez savoir'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-08T21:15:08.000Z'
originalURL: https://freecodecamp.org/news/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l65gLk36q9uBzujX3LNz1A.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: responsive design
  slug: responsive-design
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Comprendre Flexbox : Tout ce que vous devez savoir'
seo_desc: 'By Emmanuel Ohans

  This article will cover all the fundamental concepts you need to get good with the
  CSS Flexbox model. It’s a long one, so I hope you’re ready for it.

  If you prefer to read the entire tutorial in a single .pdf document, here’s the
  do...'
---

Par Emmanuel Ohans

Cet article couvrira tous les concepts fondamentaux dont vous avez besoin pour maîtriser le modèle CSS Flexbox. C'est un long article, alors j'espère que vous êtes prêt.

Si vous préférez lire l'intégralité du tutoriel dans un seul document .pdf, voici le [lien de téléchargement](http://bit.ly/und_f) — sans conditions, et si vous voulez une expérience plus immersive, utilisez [_le cours interactif_](https://www.educative.io/collection/5191711974227968/5741031244955648) — il est gratuit. Sans conditions.

### Une note sur la courbe d'apprentissage de Flexbox

Voici un tweet de Philip Roberts, un développeur que je respecte beaucoup :

![Image](https://cdn-media-1.freecodecamp.org/images/JWbKP9cIze7fGlOP-ycdxlU5rDBANGEUdDtx)

Apprendre Flexbox peut ne pas être amusant au début. Cela remettra en question ce que vous savez sur les mises en page en CSS. Mais ce n'est pas grave. Tout ce qui vaut la peine d'être appris commence ainsi.

Flexbox est certainement quelque chose que vous devriez prendre au sérieux. Il ouvre la voie au style moderne de mise en page du contenu, et il n'est pas prêt de disparaître. Il est devenu une nouvelle norme. Alors, avec les bras grands ouverts, adoptez-le !

### Ce que vous allez apprendre

Je vais d'abord vous guider à travers les bases de Flexbox. Je crois que toute tentative de compréhension de Flexbox doit commencer ici.

![Image](https://cdn-media-1.freecodecamp.org/images/GwQfjHhv1ZtEpMG1PBsmEmOk94a0OX1MNsTu)
_Fondamentaux de Flexbox_

Apprendre les fondamentaux est bien. Ce qui est encore mieux, c'est d'appliquer ces fondamentaux pour construire des applications réelles.

Je vais vous guider à travers la construction de nombreuses "petites choses". Ensuite, je conclurai avec cette application musicale entièrement mise en page avec Flexbox.

![Image](https://cdn-media-1.freecodecamp.org/images/TGJcRHirsIuymaHtKDhMeuzA-BBPzEd2fyMp)
_Mise en page de l'application musicale_

Cela ne semble-t-il pas joli ?

Je vais entrer dans les rouages internes de Flexbox pendant que vous apprenez à construire la mise en page de l'application musicale. Vous aurez également une idée du rôle que joue Flexbox dans le design web responsive.

Je suis ravi de vous montrer tout cela.

![Image](https://cdn-media-1.freecodecamp.org/images/wn1v1YeQuqWxGz7V9uzSz9Zs0WGO5amabcid)
_GIF par [Jona Dinges](https://dribbble.com/jonadinges" rel="noopener" target="_blank" title=")_

Mais avant de commencer à construire des interfaces utilisateur, je vais vous guider à travers quelques exercices. Cela peut sembler ennuyeux, mais c'est tout partie du processus pour vous rendre compétent avec Flexbox.

Commençons.

### Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/FRNVuUSvTD3VSSgPgN28g7TKlFNinvkqOdyK)

CSS a beaucoup évolué au cours des dernières années. Les designers ont adoré l'introduction des filtres, des transitions et des transformations. Mais quelque chose manquait. Quelque chose que nous désirions tous.

Créer des mises en page intelligentes avec CSS semblait avoir persisté trop longtemps, et cela nous a poussés à écrire du CSS bidouillé.

Nous devions toujours gérer les flottements, les hacks d'affichage de tableau et les conséquences qu'ils entraînaient. Si vous avez écrit du CSS pendant un certain temps, vous pouvez probablement vous identifier à cela. Et si ce n'est pas le cas, bienvenue dans un monde meilleur !

Il semble que nos prières en tant que designers et développeurs front-end ont enfin été entendues. Cette fois, en grand style.

Maintenant, nous pouvons tous abandonner ces astuces CSS bidouillées. Plus d'utilisation incessante de flottements, d'affichages en cellule de tableau.

Il est temps d'adopter une syntaxe moderne plus propre pour créer des mises en page intelligentes. Bienvenue au modèle CSS Flexbox.

### Qu'est-ce que Flexbox ?

Selon la spécification, le modèle Flexbox fournit un moyen efficace de mettre en page, d'aligner et de distribuer l'espace entre les éléments de votre document — même lorsque la fenêtre d'affichage et la taille de vos éléments sont dynamiques ou inconnues.

Si cela semble trop formel, je comprends le sentiment. Dans un instant, je vais expliquer ce que cela signifie en anglais simple.

Que vous écriviez du CSS dans vos rêves ou que vous commeniez tout juste, vous vous sentirez chez vous.

### Comment commencer à utiliser le modèle Flexbox ?

C'est la première question que tout le monde pose, et la réponse est beaucoup plus simple que vous ne l'auriez attendu.

Pour commencer à utiliser le modèle Flexbox, tout ce que vous avez à faire est de définir d'abord un _flex-container_.

En HTML standard, la mise en page d'une simple liste d'éléments prend cette forme :

```
<ul> <!-- élément parent -->  <li></li> <!-- premier élément enfant -->  <li></li> <!-- deuxième élément enfant -->  <li></li> <!-- troisième élément enfant --></ul>
```

Si vous avez jeté un coup d'œil à cela, vous avez dû voir que la liste non ordonnée (`ul`) contient les éléments de liste (`li`).

Vous appelleriez la `ul` l'élément _parent_, et la `li` l'élément _enfant_.

Pour utiliser le modèle Flexbox, vous devez faire d'un élément parent un conteneur flexible (AKA _conteneur flexible_).

Vous faites cela en définissant `display: flex` ou `display: inline-flex` pour la variation en ligne. C'est aussi simple que cela, et à partir de là, vous êtes prêt à utiliser le modèle Flexbox.

Ce qui se passe réellement, c'est qu'un contexte de formatage Flexbox est immédiatement initié.

Je vous l'avais dit, ce n'était pas aussi difficile que vous l'aviez imaginé.

![Image](https://cdn-media-1.freecodecamp.org/images/5WdWqo8y412lw8lMtH2cacPB9ptbi4I8uDdX)

En utilisant une liste non ordonnée et un ensemble d'éléments de liste, voici à quoi ressemble l'initiation d'un contexte de formatage Flexbox.

```
/* Faire de l'élément parent un conteneur flexible */ul {  display: flex; /* ou inline-flex */}
```

Stylez les éléments de liste juste un peu, pour que vous puissiez voir ce qui se passe ici.

```
li {  width: 100px;  height: 100px;  background-color: #8cacea;  margin: 8px;}
```

Voici ce que vous devriez avoir :

![Image](https://cdn-media-1.freecodecamp.org/images/zH32QRcs75OBcaVfUhBgVq5cwbLux0vBvjSs)
_Flexbox activé_

Vous n'avez peut-être pas remarqué, mais quelque chose s'est déjà passé. Le contexte de formatage Flexbox est maintenant initié.

Rappelez-vous que les éléments 'li' sont par nature des éléments de bloc, ce qui signifie qu'ils s'empilent verticalement, et cela s'applique pour d'autres éléments de bloc CSS, tels que 'div'.

![Image](https://cdn-media-1.freecodecamp.org/images/pQbujwnAyIjC74-JaFLETA7nVEbIhR6Xgz6z)
_Affichage par défaut pour les 'divs'_

L'image ci-dessus est le résultat que vous auriez pu espérer.

Cependant, avec l'inclusion de cette simple ligne, `display:flex`, vous pouvez immédiatement voir un changement de mise en page.

Les éléments de liste sont maintenant empilés horizontalement, de gauche à droite. Tout comme ils le seraient si vous aviez utilisé _float_.

![Image](https://cdn-media-1.freecodecamp.org/images/3CDiVRnCQ07ZjGkwz9ZESfVE3zEekOegnQWP)
_Flexbox activé_

Le modèle Flexbox se met en place dès que vous introduisez le "display flex" sur un élément parent.

Vous ne comprenez peut-être pas pourquoi ce changement dans l'orientation des éléments de liste s'est produit. Je promets que je vais expliquer le fonctionnement interne de cela très bientôt. Pour l'instant, une confiance aveugle suffirait.

Comprendre que l'inclusion du "display flex" lance le modèle Flexbox.

Il y a une autre chose à laquelle je dois attirer votre attention.

Dès que vous définissez la propriété display sur flex, la liste non ordonnée devient automatiquement le _conteneur flexible_ et les éléments enfants (dans ce cas, les éléments de liste `li`) deviennent des _éléments flexibles_.

Ces termes reviendront encore et encore alors que je vous guide à travers d'autres choses intéressantes que le modèle Flexbox a à offrir.

J'ai utilisé deux mots clés, et j'aimerais insister davantage sur eux. Ils sont vitaux pour comprendre ce qui suit.

1. **Conteneur flexible** : L'élément parent sur lequel vous avez défini `display: flex`.
2. **Éléments flexibles** : Les éléments enfants à l'intérieur d'un conteneur flexible.

![Image](https://cdn-media-1.freecodecamp.org/images/UWNpb0mXe3WwnQ3ylR5bAr0vdI1qHvWAnTH0)

C'est la base pour utiliser le modèle Flexbox.

### Les propriétés du conteneur flexible

`Flex-direction || Flex-wrap || Flex-flow || Justify-content || Align-items || Align-content`

![Image](https://cdn-media-1.freecodecamp.org/images/52oXVRJbgsCt97OsTJzQQaWYWlMDne39DgmI)

Dans la section précédente, j'ai établi quelques principes fondamentaux. Ce que sont les conteneurs flexibles et les éléments flexibles, et comment initier le modèle Flexbox.

Maintenant est un bon moment pour mettre tout cela à bonne utilisation.

Ayant défini un élément parent comme un conteneur flexible, plusieurs propriétés d'alignement sont mises à disposition pour être utilisées sur le conteneur flexible.

Tout comme vous définiriez la propriété de largeur sur un élément de bloc comme `width: 200px`, il y a 6 propriétés différentes que le conteneur flexible peut prendre.

La bonne nouvelle est que la définition de ces propriétés ne nécessite pas une approche différente de celle à laquelle vous êtes déjà habitué.

### 1. Flex-direction

La propriété `Flex-direction` contrôle la direction dans laquelle les éléments flexibles sont disposés le long de l'_axe principal_.

Elle peut prendre l'une des quatre valeurs suivantes.

```
/* où ul représente un conteneur flexible */ul {  flex-direction: row || column || row-reverse || column-reverse;  }
```

En termes simples, la propriété `flex-direction` vous permet de décider comment les éléments flexibles sont disposés. Soit _horizontalement_, _verticalement_ ou _inversés_ dans les deux directions.

Techniquement, « _horizontal_ » et « _vertical_ » ne sont pas les noms des directions dans le « _monde flex_ ».

Celles-ci sont décrites comme **axe principal** et **axe transversal**. Les valeurs par défaut sont illustrées ci-dessous.

En termes simples à nouveau, la direction par défaut de l'axe principal ressemble à « _horizontal_ ». De gauche à droite.

L'axe transversal ressemble à « _vertical_ ». De haut en bas.

![Image](https://cdn-media-1.freecodecamp.org/images/VuD8vU94ieA9xI5tHpOarLZp1IhgYylYdiQD)

Par défaut, la propriété `flex-direction` est définie sur `row` et elle aligne le ou les éléments flexibles le long de l'axe principal. Cela explique ce qui s'est passé avec la liste non ordonnée au début de cet article.

Même si la propriété `flex-direction` n'a pas été explicitement définie, elle a pris la valeur par défaut de `row`.

Les éléments flexibles ont ensuite été disposés le long de l'axe principal, s'empilant horizontalement de gauche à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/Ft3b0WOCw6PQ9ggoqHOPqjEC53uSDNh-2jWU)
_éléments flexibles empilés le long de l'axe principal_

Si la propriété `flex-direction` est modifiée en `column`, les éléments flexibles seront alignés le long de l'axe transversal.

Ils s'empileraient de haut en bas, et non plus de gauche à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/ffiHoJ-7gzt8Ja-mOmWJZlWxPt19lCkrlOUa)
_éléments flexibles empilés le long de l'axe transversal_

### 2. Flex-wrap

La propriété flex-wrap peut prendre l'une des trois valeurs suivantes :

```
//où ul représente un conteneur flexibleul {  flex-wrap: wrap || nowrap || wrap-reverse;  }
```

Je vais expliquer comment la propriété `flex-wrap` fonctionne en vous guidant à travers un exemple.

Essayez d'ajouter beaucoup plus d'éléments de liste dans la liste non ordonnée.

Que pensez-vous ? Le conteneur flexible va-t-il redimensionner pour en accommoder plus, ou va-t-il diviser les éléments de liste sur une autre ligne ?

```
/* ajout de 3 éléments li supplémentaires */<ul> <!-- élément parent -->  <li></li> <!-- premier élément enfant -->  <li></li> <!-- deuxième élément enfant -->  <li></li> <!-- troisième élément enfant -->  <li></li>  <li></li>  <li></li></ul>
```

Heureusement, le conteneur flexible s'adapte pour accommoder les nouveaux éléments flexibles.

![Image](https://cdn-media-1.freecodecamp.org/images/dQbW7G75C3KobGg3jrF2Rr2lrIb-K5o7DZtA)
_3 éléments flexibles supplémentaires ajoutés à la liste non ordonnée_

Allez un peu plus loin.

Ajoutez une quantité ridicule d'éléments flexibles à l'élément parent. Faites-en un total de 10 éléments.

Que se passe-t-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/Mx8nhNNbEdgI5WwrrHnrLOjwjnuzCxSoVFjj)
_Après avoir ajouté encore plus d'éléments de liste_

Encore une fois, le conteneur flexible s'adapte pour contenir tous les enfants, même si le navigateur doit être défilé horizontalement.

C'est le comportement par défaut de chaque conteneur flexible. Un conteneur flexible continuera à accommoder plus d'éléments flexibles sur une seule ligne.

C'est parce que la propriété `flex-wrap` est par défaut définie sur `nowrap`. Cela fait que le conteneur flexible ne s'enroule PAS.

```
ul {    flex-wrap: nowrap;     /* Continuer à prendre plus d'éléments flexibles sans rupture (retour à la ligne) */}
```

Le `no-wrap` n'est pas une valeur immuable. Elle peut être changée.

Avec ce nombre d'éléments flexibles, vous voulez certainement que les éléments flexibles « s'enroulent » dans le conteneur flexible.

« Enrouler » est un terme fantaisiste pour dire : « lorsque l'espace disponible dans le conteneur flexible ne peut plus contenir les éléments flexibles dans leurs largeurs par défaut, passez à plusieurs lignes. »

C'est possible avec la valeur `wrap`.

```
ul {    flex-wrap: wrap;}
```

Avec cela, les éléments flexibles se divisent maintenant en plusieurs lignes lorsque nécessaire.

Dans ce cas, lorsqu'une seule ligne ne peut plus contenir tous les éléments de la liste dans leur largeur par défaut, ils se divisent en plusieurs lignes. Même lors du redimensionnement du navigateur.

Voici à quoi cela ressemble.

Notez que les éléments flexibles sont maintenant affichés dans leurs largeurs par défaut. Il n'est pas nécessaire de forcer plusieurs éléments flexibles sur une seule ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/B6xangJ7u-OqUYwUj6u34E9J6dVlM79FAR6-)
_flex-wrap initié_

Il y a une autre valeur, `wrap-reverse`.

Oui, vous avez deviné juste. Il permet aux éléments flexibles de se diviser en plusieurs lignes, mais dans la direction inverse.

![Image](https://cdn-media-1.freecodecamp.org/images/xieEwXHJUuUbI9cAFGgdFI65jkec9e9lnvdL)
_éléments flexibles s'enroulant à l'envers_

### 3. Flex-flow

Le `flex-flow` est une propriété raccourcie qui prend les valeurs de `flex-direction` et `flex-wrap`.

Vous avez déjà utilisé la propriété raccourcie `border` ? `border: 1px solid red`.

C'est le même concept ici. Plusieurs valeurs déclarées en une seule ligne.

Voir l'exemple ci-dessous.

```
ul {    flex-flow: row wrap; /* direction "row" et oui, s'il vous plaît, enveloppez les éléments. */}
```

![Image](https://cdn-media-1.freecodecamp.org/images/x97nEIS3qYGMzn0sr92DCHGXWrteIzvLc-je)
_flex-flow décomposé en morceaux_

Essayez les autres combinaisons que cela pourrait prendre. `flex-flow: row nowrap`, `flex-flow: column wrap`, `flex-flow: column nowrap`

Les résultats produits ne sont pas différents de ce que vous avez vu avec les valeurs `flex-direction` et `flex-wrap`.

Je suis sûr que vous comprenez ce que celles-ci produiraient.

Essayez-les.

### 4. Justify-content

La vie est vraiment belle avec le modèle Flexbox. Si vous en doutez encore, la propriété `justify-content` pourrait vous convaincre.

La propriété `justify-content` peut prendre l'une des 5 valeurs ci-dessous.

```
ul {    justify-content: flex-start || flex-end || center || space-between || space-around}
```

Et que apporte exactement la propriété `justify-content` ?

Eh bien, elle pourrait vous rappeler la propriété text-align.

La propriété justify-content définit comment les éléments flexibles sont disposés sur l'_axe principal_.

Un exemple rapide.

Considérez la simple liste non ordonnée ci-dessous.

```
<ul>  <li>1</li>  <li>2</li>  <li>3</li></ul>
```

Ajoutez un peu de style de base.

```
ul {    border: 1px solid red;    padding: 0;    list-style: none;    background-color: #e8e8e9;  }
```

```
li {      background-color: #8cacea;      width: 100px;      height: 100px;      margin: 8px;      padding: 4px;  }
```

Vous devriez avoir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0DYDdAVazQvPTwJxhvHQP9EihmQKDkJntDeH)
_vue par défaut après avoir « initié » flexbox_

Avec la propriété `justify-content`, les trois éléments flexibles peuvent être alignés le long de l'axe principal de la manière que vous désirez.

Voici la répartition de ce qui est possible.

#### (i) Flex-start

La valeur par défaut est `flex-start`.

`flex-start` regroupe tous les éléments flexibles au **début** de l'axe principal.

```
ul {    justify-content: flex-start;  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1fFse2yFp1BuSKTjiD35E9YyYwNEKGaSLzUV)
_justify-content: flex-start (comportement par défaut)_

#### (ii) Flex-end

`flex-end` regroupe les éléments flexibles à la **fin** de l'axe principal.

```
ul {    justify-content: flex-end;  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/UqXTrhCqefcEEXLv2TjHEqqYLjhszzqIltqL)
_justify-content: flex-end_

#### (iii) Center

`Center` fait exactement ce que vous attendez : il centre les éléments flexibles le long de l'axe principal.

```
ul {    justify-content: center;  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/9pOoYTfYUwRPqew9dDMvA82pqkWkyURtPlmf)
_justify-content: center_

#### (iv) Space-between

`Space-between` maintient le même espace entre chaque élément flexible.

```
ul {    justify-content: space-between;  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/B0s8IBmdHyxBWvCJNldZqDBsDpEDW3UP89Lr)
_justify-content: space-between_

Um, avez-vous remarqué quelque chose de différent ici ?

Jetez un coup d'œil à l'image descriptive ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/JXtVnsdtk3UVaaZ-5Pymi3UHJKjeFKBKbkAr)

#### (v) Space-around

Enfin, `space-around` maintient le même espacement autour des éléments flexibles.

```
ul {    justify-content: space-around;  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/0z0ssIhQXPnmklYqvk21vApwSndRl3Ev3Fav)
_justify-content: space-around_

Un deuxième regard ne fait pas de mal.

Voir l'image descriptive ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/XHuT7la356SYp4X4Dz6slTIs3vMp7rnQRNSV)

Ne vous inquiétez pas si cela semble trop à saisir. Avec un peu de pratique, vous vous sentirez très à l'aise avec la syntaxe.

Assurez-vous de comprendre comment ils affectent l'affichage des éléments flexibles le long de l'axe principal.

### 5. Align-items

La propriété `align-items` est quelque peu similaire à la propriété `justify-content`.

Ayant compris la propriété `justify-content`, cela devrait être plus facile à assimiler.

`Align-items` peut être défini sur l'une de ces valeurs : `flex-start || flex-end || center || stretch || baseline`

```
/* ul représente n'importe quel conteneur flexible */ul {    align-items: flex-start || flex-end || center || stretch || baseline}
```

Il définit comment les éléments flexibles sont disposés sur l'**axe transversal**. C'est la différence entre la propriété `align-items` et `justify-content`.

Voici comment les différentes valeurs affectent les éléments flexibles.

N'oubliez pas la direction affectée par ces propriétés. L'axe transversal.

#### (i) Stretch

La valeur par défaut est `stretch`. Cela va "étirer" les éléments flexibles pour qu'ils remplissent toute la hauteur du conteneur flexible.

![Image](https://cdn-media-1.freecodecamp.org/images/kcANpoA0Vh8CxlvgLVaZlc6jqNv7T9ighmEN)
_align-items: stretch_

#### **(ii) Flex-start**

Le `flex-start` fait ce que vous attendez. Il regroupe les éléments flexibles au début de l'axe transversal.

![Image](https://cdn-media-1.freecodecamp.org/images/GFl0irQSx8a3lPiC4plrFUxsY8wTgcx2cQQh)
_align-items: flex-start_

#### **(iii) Flex-end**

Comme prévu, `flex-end` regroupe les éléments flexibles à la fin de l'axe transversal.

![Image](https://cdn-media-1.freecodecamp.org/images/gBIh243Swy00LXek0YWOsp45lNW1W7IFX-ZX)
_align-items: flex-end_

#### **(iv) Center**

La valeur `center` est également prévisible. Elle aligne les éléments flexibles au centre du conteneur flexible.

![Image](https://cdn-media-1.freecodecamp.org/images/0TyEUsELZd3OsP9EaIcTmrRHONZsUK28d5OR)
_align-items: center_

#### **(v) Baseline**

Et la valeur de la ligne de base ?

Elle aligne les éléments flexibles le long de leurs _lignes de base_.

![Image](https://cdn-media-1.freecodecamp.org/images/UkrdQi8y4LvFJv1F03oerLiQDFFWO51Nqmms)
_align-items: baseline_

"_Baseline_" sonne vraiment chic.

Le résultat semble similaire à `flex-start` mais il est subtilement différent.

Qu'est-ce que le "baseline" ?

L'image ci-dessous devrait aider.

![Image](https://cdn-media-1.freecodecamp.org/images/8-BPKQHsT3SLuvm--djHqBOl9TWeJap1Hv5l)

Remarquez comment tous les éléments flexibles sont alignés pour que leur contenu repose sur la "ligne de base" ?

### 6. Align-content

En discutant de la propriété `wrap`, vous souvenez-vous de ce qui s'est passé lorsque vous avez ajouté plus d'éléments flexibles au conteneur flexible ?

Vous avez obtenu un conteneur flexible _multi-ligne_.

La propriété `align-content` est utilisée sur les conteneurs flexibles _multi-ligne_.

Elle prend les mêmes valeurs que `align-items` à l'exception de `baseline`.

Par définition, elle contrôle comment les éléments flexibles sont alignés dans un conteneur flexible multi-ligne.

Tout comme `align-items`, la valeur par défaut est également `stretch`.

Ce sont des valeurs que vous devriez maintenant connaître. Donc, voici comment elles affectent un conteneur flexible _multi-ligne_ avec 10 éléments flexibles.

#### **(i) Stretch**

Avec `stretch`, les éléments flexibles sont "étirés" pour remplir l'espace disponible le long de l'axe transversal.

L'espacement que vous voyez entre les éléments flexibles ci-dessous est dû à la `margin` définie sur les éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/QkX7HYMqs1jf8uKsShHUa6fF8nSnPj6HPwOv)

#### **(ii) Flex-start**

Vous avez déjà vu la valeur `flex-start`.

Cette fois, elle aligne les éléments dans le conteneur _multi-ligne_ au **début** de l'axe transversal.

N'oubliez pas que l'axe transversal par défaut va de haut en bas.

Ainsi, les éléments flexibles sont alignés en haut du conteneur flexible.

![Image](https://cdn-media-1.freecodecamp.org/images/sG2Ek2TfxfkO54shUBkJeDJ9vmPdjy2SUOTW)

#### **(iii) Flex-end**

La valeur `flex-end` aligne les éléments flexibles à la fin de l'axe transversal.

![Image](https://cdn-media-1.freecodecamp.org/images/1faAtYPvCreycViq7LKlKEDSSAdOuNgtQOJC)

#### **(iv) Center**

Comme vous l'avez peut-être deviné, `center` aligne les éléments flexibles au **centre** de l'axe transversal.

![Image](https://cdn-media-1.freecodecamp.org/images/f51SSpu1Bw3zv38xlBmGTWBFEd2I-Q7iRWwz)

C'est la dernière des propriétés du conteneur flexible.

Vous comprenez maintenant comment utiliser les différentes propriétés du conteneur flexible.

Vous allez utiliser celles-ci pour travailler sur les sections pratiques à venir.

### Les propriétés des éléments flexibles

`Order || Flex-grow || Flex-shrink || Flex-basis`

![Image](https://cdn-media-1.freecodecamp.org/images/fmBrYh1QHuEivCOJn1HDzti0s-Mi8gjGawkT)

Dans la section précédente, j'ai expliqué les conteneurs flexibles et leurs propriétés d'alignement.

C'est effectivement beau.

Je suis sûr que vous commencez à avoir une idée de ce qui vous attend.

Je vais maintenant me concentrer moins sur les conteneurs flexibles et vous guider à travers les éléments flexibles et leurs propriétés d'alignement.

Comme les conteneurs flexibles, plusieurs propriétés d'alignement sont également disponibles sur tous les éléments flexibles.

Laissez-moi vous guider à travers elles.

### 1. Order

La propriété order permet de réorganiser les éléments flexibles au sein d'un conteneur.

En gros, avec la propriété order, vous pouvez déplacer un élément flexible d'une position à une autre. Tout comme vous le feriez avec des listes "triables".

Cela se fait sans affecter le code source. Ce qui signifie que la position des éléments flexibles dans le code source HTML n'est pas modifiée.

La valeur par défaut de la propriété order est 0. Elle peut prendre des valeurs négatives ou positives.

Il est important de noter que les éléments flexibles sont réorganisés en fonction des valeurs numériques de la propriété order. Du plus bas au plus haut.

Un exemple fait toujours l'affaire. Considérez la liste non ordonnée ci-dessous :

```
<ul>    <li>1</li>    <li>2</li>    <li>3</li>    <li>4</li>                          </ul>
```

Par défaut, tous les éléments flexibles ont une valeur `order` de `0`.

Comme vous vous y attendiez, vous obtenez ceci (voir ci-dessous) après un peu de style de base.

![Image](https://cdn-media-1.freecodecamp.org/images/nETXHfxwRyY4Uakz96c1htBU94WMWet61hMM)
_Vue par défaut_

Les éléments flexibles sont affichés exactement comme spécifié dans l'ordre source HTML. Élément flexible 1, puis 2, 3, et 4.

Et si, pour une raison quelconque, vous vouliez que l'élément flexible 1 apparaisse en dernier ? Sans changer l'ordre source dans le document HTML ?

"_Sans changer l'ordre source_" signifie que vous ne pouvez pas faire ceci :

```
<ul>    <li>2</li>    <li>3</li>    <li>4</li>    <li>1</li>                      </ul>
```

C'est là que la propriété `order` entre en jeu.

Tout ce que vous avez à faire est de donner à l'élément flexible 1 une valeur `order` plus élevée que celle des autres éléments de la liste.

Si vous avez déjà utilisé la propriété `z-index` sur des éléments de bloc, vous serez familier avec ce genre de chose.

```
/* sélectionner le premier élément li dans le ul */    li:nth-child(1) {        order: 1; /* lui donner une valeur supérieure à 0 */    }
```

Les éléments flexibles sont ensuite réorganisés du plus bas au plus haut.

N'oubliez pas que par défaut, les éléments de liste 2, 3 et 4 ont tous une valeur d'ordre de 0.

Maintenant, l'élément flexible 1 a une valeur d'ordre de 1.

![Image](https://cdn-media-1.freecodecamp.org/images/fAUwR4XlhuQIhbO4Yl7NljxW5vRY17NnhVnk)
_Nouveau look après avoir changé la valeur d'ordre pour 1_

Les éléments flexibles 2, 3 et 4 ont tous une valeur d'ordre de 0. Donc, l'ordre source HTML est conservé — aucune modification apportée à l'affichage par défaut.

Et si vous donniez à l'élément flexible 2 une valeur d'ordre de 2 ?

Oui, vous avez deviné juste. Il monte aussi dans la pile. Il représente maintenant l'élément flexible avec la valeur `order` la plus élevée.

![Image](https://cdn-media-1.freecodecamp.org/images/36Ibx25mSnO1X0MoLY84BK8GKYjNCQjP6v66)
_L'élément flexible 2 a maintenant une valeur d'ordre plus élevée_

Et que se passe-t-il lorsque deux éléments flexibles ont la même valeur d'ordre ?

Dans l'exemple ci-dessous, les éléments flexibles 1 et 3 se voient attribuer les mêmes valeurs `order`

```
li:nth-child(1) {        order: 1;    }
```

```
li:nth-child(3) {        order: 1;    }
```

![Image](https://cdn-media-1.freecodecamp.org/images/R1XbIaatL5kGiFcKV9V7Zba64BNFPzUjKYH0)
_Les éléments flexibles 1 et 3 avec la même valeur d'ordre_

Les éléments sont toujours disposés de la valeur d'ordre la plus basse à la plus élevée.

Cette fois, l'élément flexible 3 apparaît en dernier car il vient après l'élément flexible 1 dans le fichier source (document HTML).

Le réordonnancement est basé sur les positions dans le fichier source, lorsque deux éléments flexibles ou plus ont la même valeur d'ordre.

C'était beaucoup d'explications.

Je vais passer à une autre propriété.

### 2. Flex-grow et flex-shrink

La beauté des éléments flexibles est d'être « flexibles ».

Les propriétés `flex-grow` et `flex-shrink` nous permettent de jouer encore plus avec cette « flexibilité ».

Les propriétés `flex-grow` et `flex-shrink` contrôlent combien un élément flexible doit « grandir » (s'étendre) s'il y a des espaces supplémentaires, ou « rétrécir » s'il n'y a pas d'espaces supplémentaires.

Elles peuvent prendre n'importe quelles valeurs allant de 0 à n'importe quel nombre positif. `0 || nombre positif`

Permettez-moi de démystifier cela.

Considérez la simple liste non ordonnée ci-dessous. Elle ne comprend qu'un seul élément de liste.

```
<ul>    <li>Je suis une liste simple</li></ul>
```

```
ul {    display: flex;}
```

Avec un peu plus de style, cela ressemble à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1OcFexvPTtPtzb7hF07srRGjlmKSgT1EBfKg)
_Élément flexible simple_

Par défaut, la propriété `flex-grow` est définie sur `0`. Par implication, l'élément flexible ne grandit PAS pour remplir tout l'espace disponible.

La valeur `0` est comme un interrupteur « éteint ». L'interrupteur `flex-grow` est éteint.

Cependant, si vous changez la valeur `flex-grow` en `1`, voici ce qui se passe.

![Image](https://cdn-media-1.freecodecamp.org/images/cFuJct8qfJ593WTjnShz3yJtFE0yDP0gORiQ)
_L'élément flexible grandit pour remplir l'espace disponible_

L'élément flexible « grandit » maintenant pour occuper tout l'espace disponible. L'interrupteur est allumé !

Si vous essayez de redimensionner votre navigateur, l'élément flexible « rétrécirait » également pour s'adapter à la nouvelle largeur de l'écran.

Pourquoi ? Par défaut, la propriété `shrink` est définie sur 1. Ce qui signifie que l'interrupteur `flex-shrink` est également allumé !

Je vais examiner de plus près les propriétés `flex-grow` et `flex-shrink` dans un instant au cas où vous ne vous sentirez pas encore en confiance avec votre compréhension de cela.

### 3. Flex-basis

Vous vous souvenez quand j'ai dit que la beauté des éléments flexibles est d'être « flexibles » ? Eh bien, il semble que vous ayez également un contrôle sur cela.

La propriété `flex-basis` spécifie la taille initiale d'un élément flexible. Avant que les propriétés `flex-grow` ou `flex-shrink` n'ajustent sa taille pour s'adapter au conteneur ou non.

La déclaration précédente est vraiment importante - alors je prends un moment pour la renforcer.

La valeur par défaut est `flex-basis: auto`. `Flex-basis` peut prendre n'importe quelles valeurs que vous utiliseriez sur la propriété de largeur normale. C'est-à-dire, `pourcentages || ems || rems || pixels` etc.

Notez que lorsque vous essayez de définir la propriété basis à une valeur basée sur zéro, utilisez également l'unité. Utilisez `flex-basis: 0px` et non pas juste `flex-basis: 0`.

Je vais revenir à l'exemple de la « liste unique » ici.

```
<ul>    <li>Je suis une liste simple</li></ul>
```

```
ul {    display: flex}
```

```
li {    padding: 4px; /* un peu d'espace pour respirer */}
```

Par défaut, la largeur initiale de l'élément flexible est influencée par la valeur par défaut, `flex-basis: auto`.

La largeur de l'élément flexible est calculée « automatiquement » en fonction de la taille du contenu (et évidemment, plus le padding que vous avez défini).

![Image](https://cdn-media-1.freecodecamp.org/images/pbGtL0p2EKntexu3pgRSaYRuz3NukPd107Yx)
_vue par défaut_

Cela signifie que si vous augmentez le contenu dans l'élément flexible, il se redimensionne automatiquement pour s'adapter.

```
<ul>    <li>Je suis une liste simple ET Je suis une liste simple</li></ul>
```

![Image](https://cdn-media-1.freecodecamp.org/images/45swqBCBDeSl0a6-nbwp4YFeoc4N-iSf5OKK)
_la largeur est calculée automatiquement_

Si, cependant, vous souhaitez définir l'élément flexible à une largeur fixe, vous pouvez également faire ceci :

```
li {    flex-basis: 150px;}
```

Maintenant, l'élément flexible a été contraint à une largeur de 150px.

![Image](https://cdn-media-1.freecodecamp.org/images/7HpICOFmTkiBoMVTVWzepOHEZnTkXFMPCqkd)
_élément flexible avec une largeur contrainte_

Cela devient encore plus intéressant.

### 4. Le raccourci flex

Le raccourci `flex` vous permet de définir les propriétés `flex-grow`, `flex-shrink` et `flex-basis` en une seule fois.

Lorsque c'est approprié, je vous conseille de définir les trois propriétés en une seule fois en utilisant le raccourci flex plutôt que de le faire individuellement.

```
li {  flex: 0 1 auto;}
```

Le code ci-dessus est équivalent à définir les trois propriétés : `flex-grow: 0; flex-shrink: 1; flex-basis: auto`.

Veuillez noter l'ordre.

`Flex-grow` d'abord, puis `flex-shrink`, et enfin `flex-basis`. L'acronyme **GSB** peut aider.

Que se passe-t-il si vous ne définissez pas l'une des valeurs dans le raccourci flex ?

Si vous définissez uniquement les valeurs `flex-grow` et `flex-shrink`, `flex-basis` prendra par défaut zéro.

Cela s'appelle un _flex absolu_. Et lorsque vous définissez uniquement `flex-basis`, vous obtenez un _flex relatif_.

```
/* ceci est un élément flex absolu */li {  flex: 1 1; /* flex-basis prend par défaut 0 */}
```

```
/* ceci est un élément flex relatif */li {  flex-basis: 200px; /* seul flex-basis est défini */}
```

Je sais ce que vous pensez. Quel est le but du _flex relatif_ et _absolu_ ?

Je réponds à cette question plus tard dans cet article. Encore une fois, la confiance aveugle suffira pour l'instant.

Regardons quelques valeurs de raccourci flex très utiles.

#### `1. flex: 0 1 auto`

```
/* encore une fois, le "li" représente n'importe quel élément flex */li {  flex: 0 1 auto;}
```

C'est la même chose que d'écrire `flex: default` et c'est le comportement par défaut de tous les éléments flex.

Permettez-moi de décomposer cela, juste un peu.

![Image](https://cdn-media-1.freecodecamp.org/images/J1qjG9Ri-3pO4ZDuhAkYaFhyhajSXTdCsGLI)

Il est plus facile de comprendre cela en regardant d'abord la propriété `flex-basis`.

La `flex-basis` est définie sur `auto`, ce qui signifie que la largeur initiale de l'élément flex sera déterminée _automatiquement_ en fonction de la taille du contenu.

Vous avez compris ?

Passons à la propriété suivante, la valeur `flex-grow` est zéro. Cela signifie que la propriété `flex-grow` ne modifiera pas la largeur initiale de l'élément flex.

L'interrupteur de croissance est éteint.

Puisque flex-grow contrôle la « croissance » des éléments flexibles et qu'il est défini sur zéro, les éléments flexibles ne « grandiront » pas pour s'adapter à l'écran.

Enfin, la valeur flex shrink est 1. Cela signifie : « rétrécir l'élément flex lorsque c'est nécessaire ».

Voici à quoi cela ressemble lorsqu'il est appliqué à certains éléments flexibles.

![Image](https://cdn-media-1.freecodecamp.org/images/9UYQa-EPoyus-A0Oyz61rMbIrnIQEalHerMJ)
_`flex: 0 1 auto`_

Remarquez comment les éléments flexibles ne grandissent pas. La largeur est calculée automatiquement, et ils se rétrécissent lors du redimensionnement du navigateur — si nécessaire.

#### 2. `Flex: 0 0 auto`

```
/* encore une fois, le "li" représente n'importe quel élément de liste */
```

```
li {  flex: 0 0 auto;}
```

C'est la même chose que `flex: none`.

En utilisant le même cadre que j'ai établi précédemment, la largeur est calculée automatiquement MAIS l'élément flex ne grandit ni ne rétrécit (ils sont tous les deux définis à zéro).

Les interrupteurs de croissance et de rétrécissement sont tous les deux éteints.

C'est essentiellement un élément de largeur fixe dont la largeur initiale est basée sur la taille du contenu dans l'élément flex.

Voyez comment ce raccourci flex affecte deux éléments flexibles. L'un contenant plus de contenu que l'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/vP2z580Ytr9gv3yKyAQyjYVFb8-qr1dRDOZN)
_`Flex: 0 0 auto`_

La première chose que vous devriez remarquer est que les éléments flexibles ont tous deux des largeurs différentes.

C'est attendu puisque les largeurs sont calculées automatiquement, en fonction de la taille du contenu.

Essayez de redimensionner votre navigateur, et vous remarquerez que les éléments flexibles ne se rétrécissent pas avec sa largeur. Ils sortent de l'élément parent, et vous devez faire défiler votre navigateur horizontalement pour voir tout le contenu.

Pas de soucis, je vais vous montrer comment gérer ce comportement étrange plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/d38EvqihgFMLiIihSFgKqVcQQfHl1dt-Op2V)
_Lors du redimensionnement du navigateur, les éléments flexibles ne se rétrécissent PAS. Au lieu de cela, ils sortent du conteneur flexible._

#### 3. `Flex: 1 1 auto`

C'est la même chose que `flex: auto`.

Utilisez le cadre que j'ai établi précédemment.

Cela signifie : "calculer la largeur initiale automatiquement, mais grandir pour remplir tout l'espace disponible et rétrécir si nécessaire".

Les interrupteurs de croissance et de rétrécissement sont activés, et les largeurs sont calculées automatiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/oIhOowjCWc0VuZqGiPy6miUwVpUknQUjnsJ4)
_`Flex: 1 1 auto`_

Cette fois-ci, les éléments remplissent l'espace disponible et ils se rétrécissent également lors du redimensionnement du navigateur.

#### 4. `Flex: "nombre positif"`

Où "_nombre positif_" représente n'importe quel nombre positif (sans les guillemets)

C'est la même chose que `flex: "nombre positif" 1 0`.

`flex: 2 1 0` est la même chose que d'écrire `flex:2` où 2 représente n'importe quel nombre positif.

```
/* encore une fois, le "li" représente n'importe quel élément de liste */li {  flex: 2 1 0; /* même chose que flex: 2 */}
```

En suivant le même cadre que j'ai établi précédemment, cela signifie : "définir la largeur initiale de l'élément flexible à zéro (euh, pas de largeur ?), faire grandir l'élément pour remplir l'espace disponible, et enfin rétrécir l'élément chaque fois que possible".

Avec les éléments flexibles ayant "aucune largeur", comment la largeur est-elle calculée ?

La valeur `flex-grow` prend le relais et détermine dans quelle mesure l'élément flexible "s'élargit".

Cela résout le problème de "pas de largeur".

Il est plus pratique d'utiliser ce raccourci flex lorsque vous avez plus d'un élément flexible dont les largeurs initiales, `flex-basis`, sont définies sur des valeurs basées sur zéro, par exemple 0px.

Ce qui se passe réellement, c'est que les largeurs des éléments flexibles sont calculées en fonction des ratios de la valeur `flex-grow`.

Je vais décomposer cela un peu.

Considérez les deux éléments de liste marqués et stylisés ci-dessous.

```
<ul>    <li>Je suis Un</li>    <li>Je suis Deux</li></ul>
```

```
ul {    display: flex;}
```

```
/* premier élément flexible */li:nth-child(1) {    flex: 2 1 0; /* même chose que d'écrire simplement flex: 2 */}
```

```
/* deuxième élément flexible */li:nth-child(2){    flex: 1 1 0;    background-color: #8cacea;}
```

Rappelez-vous que définir `flex-grow : 1` permet à l'élément flexible de remplir l'espace disponible. L'interrupteur de croissance est activé.

Ici, vous avez deux éléments flexibles. L'un a une propriété `flex-grow` de `1` et l'autre de `2`, que se passe-t-il alors ?

Vous avez les interrupteurs de croissance activés pour les deux éléments. Cependant, l'ampleur de la croissance diffère. 1 et 2.

Ils s'étendent tous les deux pour remplir l'espace disponible, mais dans une certaine proportion.

Voici comment cela fonctionne.

Ce dernier prend 2/3 de l'espace disponible tandis que le premier prend 1/3.

Vous savez comment j'ai obtenu cela ?

Ratio mathématique de base. `ratio individuel / ratio total` J'espère que vous n'avez pas sauté ces cours de maths.

![Image](https://cdn-media-1.freecodecamp.org/images/ZWamUjTEZRH9HQdv63Y7960E2XmTKQuvMDjf)
_éléments flexibles partageant l'espace_

Vous voyez ce qui se passe ?

Même si les deux éléments flexibles ont des contenus de la même taille (approximativement), ils occupent cependant des espaces différents.

Les largeurs ne sont pas basées sur la taille du contenu, mais sur les valeurs de croissance.

L'un est environ deux fois l'autre.

### 5. Align-self

La propriété `align-self` va plus loin en nous donnant tant de contrôle sur les éléments flexibles.

Vous avez déjà vu comment la propriété `align-items` aide à aligner collectivement tous les éléments flexibles au sein d'un conteneur flexible.

Et si vous vouliez changer la position d'un **seul** élément flexible le long de l'axe transversal, sans affecter les éléments flexibles voisins ?

C'est là que la propriété `align-self` vient à la rescousse.

Elle peut prendre l'une de ces valeurs : `auto || flex-start || flex-end || center || baseline || stretch`

```
/* cibler le premier élément de la liste */li:first-of-type {    align-self: auto || flex-start || flex-end || center || baseline || stretch}
```

Ce sont des valeurs que vous connaissez déjà, mais pour vous rafraîchir la mémoire, voici comment elles affectent un élément particulier ciblé.

Dans ce cas, le premier élément du conteneur.

L'élément flexible ciblé est en rouge.

#### 1. Flex-end

`flex-end` aligne l'élément ciblé à la fin de l'axe transversal.

![Image](https://cdn-media-1.freecodecamp.org/images/-RSwnVGXOEG46d8U7ZE65ls47EZsWlyaBfL9)
_élément flexible ciblé à la fin de l'axe transversal_

#### `2. Center`

`center` aligne l'élément ciblé au centre de l'axe transversal.

![Image](https://cdn-media-1.freecodecamp.org/images/KFxobQZvIkD0zzkuooteIOoawJmVFIGOALtG)
_élément flexible ciblé au centre de l'axe transversal_

#### `3. Stretch`

`stretch` "étire" l'élément flexible ciblé pour remplir l'espace disponible le long de l'axe transversal.

![Image](https://cdn-media-1.freecodecamp.org/images/izoR6UgjBdUqYIWrRZpkg7XT98aZt4Lkj8DY)
_élément flexible ciblé étiré le long de l'axe transversal_

#### `4. Baseline`

`baseline` aligne l'élément flexible ciblé le long de la ligne de base.

Cela semble donner le même résultat que `flex-start`, mais je suis sûr que vous comprenez ce qu'est la ligne de base.

Je l'ai expliqué beaucoup plus tôt.

![Image](https://cdn-media-1.freecodecamp.org/images/2sy08h6wWB5DGfzPz7IKWK-h3lCUE8QqfTAT)
_élément flexible ciblé aligné le long de la ligne de base_

#### `5. auto`

`auto` définit la valeur de l'élément flexible ciblé sur la valeur `align-items` du parent ou `stretch` si l'élément n'a pas de parent.

Dans le cas ci-dessous, le conteneur flexible a une valeur `align-items` de `flex-start`.

Cela aligne tous les éléments flexibles au début de l'axe transversal.

L'élément flexible ciblé hérite maintenant de la valeur `flex-start` — la valeur `align-items` du parent.

![Image](https://cdn-media-1.freecodecamp.org/images/hTD9BgcMOrJ9Eo9XGXndPzOkXEvFXudQTA7p)
_élément flexible ciblé aligné le long du début de l'axe transversal_

C'est le style de base appliqué aux éléments flexibles utilisés ci-dessus. Juste pour que vous compreniez encore mieux ce qui se passe.

```
ul {    display: flex;    border: 1px solid red;    padding: 0;    list-style: none;    justify-content: space-between;    align-items: flex-start; /* affecte tous les éléments flexibles */    min-height: 50%;    background-color: #e8e8e9;}
```

```
li {  width: 100px;  background-color: #8cacea;  margin: 8px;  font-size: 2rem;}
```

Vous êtes presque prêt pour la partie amusante maintenant :-)

### Éléments flexibles absolus et relatifs.

![Image](https://cdn-media-1.freecodecamp.org/images/hPowuz7PW6MQqt1ZaUQUTRHSdvujLNLj43hj)

Ayant couvert du terrain dans les sections précédentes, il est important de clarifier quelques concepts importants ici aussi.

Quelle est vraiment la différence entre un élément flexible absolu et relatif ?

La différence majeure entre ces deux types concerne l'espacement et la manière dont ils sont calculés.

L'espacement dans un élément flexible relatif est calculé en fonction de la taille de son contenu. Dans un élément flexible absolu, il est basé uniquement sur le « flex », et non sur le contenu.

Considérez le balisage ci-dessous.

```
<ul>    <li>        Ce n'est qu'un texte aléatoire pour illustrer le point expliqué.    Un peu plus de texte aléatoire pour illustrer le point expliqué.    </li>
```

```
    <li>Ce n'est qu'un texte aléatoire plus court.</li></ul>
```

Deux éléments de liste. L'un a beaucoup plus de texte que l'autre.

Ajoutez un peu de style.

```
ul {    display: flex; /* flexbox activé */}
```

```
li {    flex: auto; /* rappelez-vous que c'est la même chose que flex: 1 1 auto; */    border: 2px solid red;    margin: 2em;}
```

Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/2xHCJgvr7XVmOvr-2LhjBG9r8y1-DgsSJHwh)

Si vous avez déjà oublié, `flex: 1 1 auto` est la même chose que de définir : `flex-grow: 1` `flex-shrink: 1` et `flex-basis: auto`.

En utilisant le cadre que j'ai établi précédemment, les largeurs initiales des éléments flexibles sont calculées automatiquement `flex-basis: auto`, puis ils "grandissent" pour remplir l'espace disponible `flex-grow: 1`.

Lorsque les éléments flexibles ont leurs largeurs calculées automatiquement, `flex-basis: auto`, cela est basé sur la taille du contenu contenu dans les éléments flexibles.

Les éléments flexibles dans l'exemple ci-dessus n'ont pas de contenus de la même taille. Par conséquent, les tailles des éléments flexibles seraient inégales.

Puisque les largeurs individuelles n'étaient pas égales au départ (elles étaient basées sur le contenu), lorsque les éléments grandissent, les largeurs restent également inégales.

![Image](https://cdn-media-1.freecodecamp.org/images/jtFUbFKluKua-rnhUg7TBDkzZ9Q7afq-csO1)

Les éléments flexibles dans l'exemple ci-dessus sont des éléments flexibles _relatifs_.

Rendons les éléments flexibles absolus — ce qui signifie que cette fois, leurs largeurs doivent être basées sur le « flex » et non sur la taille du contenu.

Une « ligne de code » fait le tour.

```
li {    flex: 1 ; /* même chose que flex: 1 1 0 */}
```

Voyez le résultat ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1vaSuvYJiwBRZA2tgd9U4iA4abRWhmCLWSnR)

Voyez-vous que les deux éléments flexibles ont la même largeur cette fois-ci ?

Les largeurs initiales des éléments flexibles sont de zéro `flex-basis: 0`, puis ils « grandissent » pour remplir l'espace disponible.

Lorsque deux éléments flexibles ou plus ont des valeurs `flex-basis` basées sur zéro, ils partagent l'espace disponible en fonction des valeurs `flex-grow`.

J'ai parlé de cela plus tôt.

Maintenant, les largeurs ne sont pas calculées en fonction de la taille du contenu. Les largeurs sont basées sur la valeur flex spécifiée.

Donc, vous avez compris. N'est-ce pas ?

Les éléments flexibles absolus ont leurs largeurs basées uniquement sur le flex, tandis que les éléments flexibles relatifs ont leurs largeurs basées sur la taille du contenu.

### Alignement automatique des marges

![Image](https://cdn-media-1.freecodecamp.org/images/apPe8D7E8l85EggChiG5HLPJXrjO5RseH7dP)

#### Attention à l'alignement `margin: auto` sur les éléments flexibles.

Lorsque vous utilisez `margin: auto` sur des éléments flexibles, les choses peuvent sembler assez étranges.

Vous devez comprendre ce qui se passe. Cela peut entraîner des résultats inattendus, mais je vais tout expliquer.

Lorsque vous utilisez `margin: auto` sur un élément flexible, la direction (gauche, droite ou les deux) qui a la valeur `auto` occupera tout espace vide disponible.

C'est un concept difficile à saisir.

Voici ce que je veux dire.

Considérez la barre de navigation marquée et stylisée ci-dessous :

```
<ul>    <li>Branding</li>    <li>Home</li>    <li>Services</li>    <li>About</li>    <li>Contact</li></ul>
```

```
ul {    display: flex;}li {    flex: 0 0 auto;}
```

Voici le résultat de cela ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/xh92YBbv5JVc9wybiiD2ByVCo6BU0Y3fkUyI)
_Barre de navigation simple_

Il y a quelques points à noter ici :

1. La valeur `flex-grow` est définie sur zéro. Cela explique pourquoi les éléments de liste ne grandissent pas.
2. Les éléments flexibles sont alignés au début de l'axe principal (comportement par défaut).
3. En raison du fait que les éléments sont alignés au début de l'axe principal, un espace supplémentaire est laissé à droite. Vous voyez cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/DahLZz6Cn5plr-2Mug6Itth90B5Gp-RrYO-1)

Maintenant, utilisez `margin: auto` sur le premier élément de la liste (branding) et voyez ce qui se passe.

```
li:nth-child(1) {    margin-right: auto; /* appliqué uniquement à droite */}
```

![Image](https://cdn-media-1.freecodecamp.org/images/Z9l-DWS8cWh5ihYUVcGMjIYKmuHKR5nToIJy)
_margin:auto appliqué à 'branding'_

Que s'est-il passé ?

L'espace supplémentaire qui existait a maintenant été distribué à droite du premier élément flexible.

![Image](https://cdn-media-1.freecodecamp.org/images/hgk7KKNXN8JjEVM2XUugGZ2bznXq-kAcAOnE)

Vous vous souvenez de ce que j'ai dit plus tôt ?

Lorsque vous utilisez `margin:auto` sur un élément flexible, la direction (gauche, droite ou les deux) qui a la valeur `auto` occupera tout espace vide disponible.

Et si vous vouliez un alignement automatique des marges des deux côtés d'un élément flexible ?

```
/* vous pouvez utiliser le raccourci margin pour définir les deux côtés si vous le souhaitez */li:nth-child(1) {    margin-left: auto;    margin-right: auto}
```

![Image](https://cdn-media-1.freecodecamp.org/images/swRJd9celASXulipDVS77ltOFIZ-dF4Rq4-2)
_margin:auto appliqué des deux côtés du « branding »_

Maintenant, l'espace est distribué des deux côtés de l'élément flexible.

Alors, y a-t-il un compromis avec le cool alignement automatique des marges ?

Il semble qu'il y en ait un. Cela peut être une source de frustration si vous ne faites pas attention non plus.

Lorsque vous utilisez l'alignement automatique des marges sur un élément flexible, la propriété `justify-content` ne fonctionne plus.

Par exemple, définir une option d'alignement différente sur le conteneur flexible ci-dessus via la propriété `justify-content` n'a aucun impact sur la mise en page.

```
ul {    justify-content: flex-end;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/WJjUeqcKMIJh5ycwoSmRvuckActwd3y5LlA5)
_justify-content n'a aucun impact_

### Cas d'utilisation pratiques

Les systèmes de navigation sont une partie très importante de chaque site web ou application. Chaque site web sur la planète a une sorte de système de navigation en place.

Jetez un coup d'œil à ces sites populaires et à la manière dont ils abordent leurs systèmes de navigation.

Voyez-vous comment Flexbox peut vous aider à construire ces mises en page plus efficacement ?

Regardez de plus près pour voir où la fonctionnalité de marge automatique peut être très utile également.

#### (i) Navigation Bootstrap

![Image](https://cdn-media-1.freecodecamp.org/images/ib8MiNv4ZHuBbAo6Sshmcxr3zeULC4cfNDEx)

#### (ii) Navigation de bureau AirBnB

![Image](https://cdn-media-1.freecodecamp.org/images/u7N9Z8AnwYq47fe0gwSxAV7XtrgWTpF8T8GL)

#### (iii) Navigation de bureau Twitter

![Image](https://cdn-media-1.freecodecamp.org/images/Af0KxVqCbSOhqKSoBQ1kF37LR73rxUIqp9iP)

Je vous recommande d'écrire réellement du code comme forme de pratique. J'ai écrit un guide pratique ici : [Les barres de navigation les plus populaires créées avec Flexbox](https://medium.com/flexbox-and-grids/the-most-popular-navigation-bars-created-with-flexbox-6c0f59f55686)

Allez y jeter un coup d'œil.

Je vais attendre.

### Que se passe-t-il lorsque vous changez flex-direction ?

Avertissement équitable : il y a des choses étranges en route.

![Image](https://cdn-media-1.freecodecamp.org/images/5w8tqmw8WpA03xHv0ucxjaQ5x1l6H1EIHAFo)

Lorsque j'ai commencé à apprendre le modèle Flexbox, cette partie était la plus confuse.

Je parie que beaucoup de nouveaux venus dans le « monde flex » le trouvent ainsi aussi.

Vous vous souvenez quand j'ai parlé des axes principal et transversal par défaut étant dans les directions « de gauche à droite » et « de haut en bas » ?

Eh bien, vous pouvez changer cela aussi.

C'est exactement ce qui se passe lorsque vous utilisez `flex-direction: column` comme décrit dans une section précédente.

Lorsque vous utilisez `flex-direction: column`, les axes principal et transversal sont changés comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/XmBZv4HJUK8eLozcYcGZHMWVMaWb3vrB8Wu4)
_axe principal et transversal par défaut_

![Image](https://cdn-media-1.freecodecamp.org/images/qaRmzHMsHKDBYIxBSIfRt4yg9uIBUHVuWaMD)
_Nouvel axe principal et transversal_

Si vous avez déjà écrit un texte en anglais, alors vous savez déjà que la langue est écrite de gauche à droite et de haut en bas.

C'est également la direction prise pour l'axe principal et transversal par défaut de Flexbox.

Cependant, en changeant la direction flex en `column`, elle ne suit plus le modèle de la "langue anglaise" mais celui du japonais !

Oh oui, le japonais.

Si vous avez écrit un texte en japonais, alors cela vous sera familier. (Pour la record, je n'ai jamais écrit un texte en japonais.)

Le texte japonais est traditionnellement écrit de **haut en bas** ! Pas si étrange, hein ?

Cela explique pourquoi cela peut être un peu déroutant pour les écrivains anglais.

![Image](https://cdn-media-1.freecodecamp.org/images/ssP-BXLvPhEkCB16ErLP65pWRpb2vUX45i4U)
_Nouvel axe principal et transversal_

Jetez un coup d'œil à cet exemple. La liste non ordonnée standard avec 3 éléments de liste, sauf que cette fois, je vais changer la direction flex.

```
<ul>        <li></li>        <li></li>        <li></li>    </ul>
```

```
ul {    display: flex;    flex-direction: column;}
```

Voici l'apparence avant le changement de direction :

![Image](https://cdn-media-1.freecodecamp.org/images/M0OB14qsVkERTcQbTA4lTpBqSVf9xvQYFyIG)

Et après :

![Image](https://cdn-media-1.freecodecamp.org/images/NvfOHBWNW56LoKhEe4vuESbgqgTfPxJRDMXF)

Alors, que s'est-il passé ?

Le « texte » est maintenant écrit à la manière japonaise — de haut en bas (axe principal).

Il y a quelque chose que vous pourriez trouver drôle, j'aimerais le souligner.

Vous voyez que la largeur des éléments remplit l'espace, n'est-ce pas ?

Si vous deviez changer cela auparavant, vous auriez simplement traité avec les propriétés `flex-basis` et (ou) `flex-grow`.

Voyons comment celles-ci affectent notre nouvelle mise en page.

```
li {    flex-basis: 100px;}
```

...et voici ce que vous obtiendriez.

![Image](https://cdn-media-1.freecodecamp.org/images/G4XDfdaw4JIK1ozO3x2mh-9e08zPUhsv50Xn)

Wow — quoi ? La hauteur est affectée, mais pas la largeur ?

Comme je l'ai dit plus tôt, la propriété flex-basis définit la largeur initiale de chaque élément flexible.

J'avais tort — ou mieux dit, je pensais en « anglais ». Passons au japonais pour un instant.

Ce n'est pas toujours « largeur ».

Lors du changement de flex-direction, veuillez noter que chaque propriété qui affectait l'axe principal affecte maintenant le _nouvel_ axe principal.

Une propriété comme `flex-basis` qui affectait la largeur des éléments flexibles le long de l'axe principal affecte maintenant la hauteur et non la largeur.

La direction a été changée !

Ainsi, même si vous utilisiez la propriété `flex-grow`, elle affecterait également la hauteur.

Essentiellement, chaque propriété flex qui opérait sur l'axe horizontal (l'axe principal alors) opère maintenant verticalement, le nouvel axe principal.

C'est juste un changement de directions.

Voici un autre exemple. Je vous promets que vous aurez une meilleure compréhension après celui-ci.

Réduisez la largeur des éléments flexibles que nous avons regardés juste avant maintenant, et ils ne remplissent plus tout l'espace :

```
li {    width: 200px;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/kFnM7WwjsJxtbSXX9suozyoDWJo2tT7jpRZK)

Et si vous vouliez déplacer les éléments de la liste au centre de l'écran ?

En anglais, ce qui est la façon dont vous avez traité les conteneurs flexibles jusqu'à présent. Cela signifierait « déplacer les éléments flexibles au centre de l'axe principal ».

Donc, vous auriez utilisé `justify-content: center`.

Mais faire cela maintenant ne fonctionne pas.

Puisque la direction a changé, le centre est le long de l'axe transversal — pas l'axe principal.

Jetez un autre coup d'œil :

![Image](https://cdn-media-1.freecodecamp.org/images/cFQqFbN4Z2VLCIFwIUQVWFOkHZwQvC8hFoa3)
_Nouvel axe principal et transversal_

Alors, pensez en termes de _texte japonais_.

L'axe principal est de haut en bas, vous n'en avez pas besoin.

L'axe transversal est de gauche à droite. Cela ressemble à ce dont vous avez besoin.

Vous devez « déplacer les éléments flexibles au centre de l'axe transversal ».

Une propriété de conteneur flexible vous vient à l'esprit ?

Oui, la propriété `align-items`.

La propriété `align-items` traite de l'alignement sur l'axe transversal.

Donc, pour déplacer ceux-ci au centre, vous feriez ceci :

```
ul {    align-items: center;}
```

Et voilà ! Vous avez les éléments flexibles centrés.

![Image](https://cdn-media-1.freecodecamp.org/images/qWSI8xpwrGvSfiWePLYXWOvncFXMNkEBRnr3)
_éléments flexibles centrés dans la nouvelle direction_

Cela peut être un peu déroutant, je le sais. Passez-le en revue une fois de plus si nécessaire.

En étudiant le modèle Flexbox, j'ai remarqué que de nombreux livres sur CSS ont sauté cette partie.

Un peu de réflexion en _texte japonais_ pourrait grandement aider.

Il est important de comprendre que toutes les propriétés Flexbox fonctionnent en fonction de la `flex-direction` qui est en place.

Je suis sûr que vous avez appris quelque chose de nouveau. J'ai du plaisir à expliquer cela. J'espère que vous aussi :-)

### Oh mon Dieu, Flexbox a résolu ça ?

![Image](https://cdn-media-1.freecodecamp.org/images/b72b2A-wEM0pjWI4MGJPOAJB82ecaUKqPQXY)

Certains problèmes classiques auxquels de nombreux designers sont confrontés avec CSS ont été résolus de manière triviale par Flexbox.

[Philip Walton](https://philipwalton.com/), dans son projet [solved-by-flexbox](https://github.com/philipwalton/solved-by-flexbox), liste 6 problèmes classiques (à la date de rédaction de cet article).

Il discute en détail des limitations précédentes avec CSS et des solutions actuelles que Flexbox apporte.

Je vous recommande de jeter un coup d'œil après avoir terminé cet article.

Dans la section pratique à venir, j'expliquerai certains des concepts qu'il aborde tout en vous guidant à travers la construction d'une mise en page d'application musicale avec Flexbox.

### Flexbugs et pièges pour les navigateurs non conformes

Si vous n'êtes pas du type de personne qui écrit du CSS dans ses rêves, vous pourriez vouloir surveiller ce dépôt github [repository](https://github.com/philipwalton/flexbugs).

Des personnes plus intelligentes que moi y compilent une liste de bugs Flexbox et leurs solutions de contournement.

C'est le premier endroit où je regarde lorsque quelque chose ne fonctionne pas comme je l'attends.

Je vais également vous guider à travers certains bugs importants dans la section pratique à venir.

Donc, vous êtes couvert !

### Construction d'une mise en page d'application musicale avec Flexbox

![Image](https://cdn-media-1.freecodecamp.org/images/n1YF0wHXGhV0ZClOY3FYNR6ojbqbJPSRZYH6)

Après avoir parcouru les choses rigoureuses et ennuyeuses, vous méritez un projet amusant.

Il est temps de passer à un exemple pratique et d'appliquer vos compétences nouvellement acquises en _Flexbox_.

Cela m'a pris des jours pour trouver un bon projet.

Faute d'une option créative, j'ai imaginé une mise en page d'application musicale pour chats.

Je l'appelle _catty music_.

Peut-être qu'en 2036, nous aurons des chats chantant dans des groupes de rock quelque part sur Mars :-)

Voici à quoi ressemble la mise en page terminée, et elle est entièrement conçue avec Flexbox.

![Image](https://cdn-media-1.freecodecamp.org/images/JdTtM2ARIeCEkyeQHcDIPeEz13BFRXVyzuHo)

Vous pouvez la consulter en ligne [ici](http://output.jsbin.com/wubudog/).

Si vous la consultez sur un appareil mobile, vous aurez une apparence légèrement différente. C'est quelque chose sur lequel vous travaillerez dans la section de design responsive de cet article.

J'ai une confession à faire cependant.

J'ai fait quelque chose considéré comme incorrect par beaucoup.

J'ai entièrement construit la mise en page globale avec Flexbox.

Pour de nombreuses raisons, cela peut ne pas être idéal. Mais c'est intentionnel dans ce scénario. Je me suis fixé de vous montrer tout ce que vous pouvez faire avec Flexbox, le tout regroupé dans un seul projet.

Si vous êtes curieux de savoir quand il est considéré comme correct ou incorrect d'utiliser le modèle Flexbox, vous pouvez consulter mon article à ce sujet.

[**Flexbox est génial mais il n'est PAS le bienvenu ici !**](https://medium.com/@ohansemmanuel/flexbox-is-awesome-but-its-not-welcome-here-a90601c292b6)  
[_Flexbox est sans doute la meilleure chose qui soit arrivée à la plupart d'entre nous (si vous écrivez du css) mais cela en fait-il le choix parfait pour tout..._medium.com](https://medium.com/@ohansemmanuel/flexbox-is-awesome-but-its-not-welcome-here-a90601c292b6)

Voilà, j'ai dit ce que j'avais sur le cœur. Maintenant, je suis sûr que personne ne va me crier dessus après avoir lu ceci.

Tout dans Catty Music est mis en page en utilisant le modèle Flexbox — ceci est intentionnel pour montrer ce qui est possible.

Alors, construisons cette chose !

Comme pour tout projet raisonnable, un peu de planification va loin pour éliminer les inefficacités.

Permettez-moi de vous guider à travers une approche planifiée pour construire la mise en page de catty music.

### **Par où commencer ?**

Lorsque vous construisez une mise en page avec Flexbox, vous devriez commencer par chercher quelles sections de votre mise en page peuvent se démarquer comme des conteneurs flexibles.

Vous utilisez ensuite les puissantes propriétés d'alignement que Flexbox met à disposition.

### La décomposition

Vous pouvez avoir le corps global contenant comme un conteneur flexible (contenu dans la bordure rouge dans l'image ci-dessous) et avoir les autres sections de la mise en page divisées en éléments flexibles (éléments 1 et 2).

![Image](https://cdn-media-1.freecodecamp.org/images/TZejdd6yd7Bvr6KNcR9qW6a6QP8pWi1uInJx)

Cela a tout son sens, car l'élément 1 contient toutes les parties de la mise en page autres que le "pied de page" — la section qui contient les boutons de contrôle de la musique.

Saviez-vous qu'un élément flexible pouvait également être transformé en un conteneur flexible ?

Oui, c'est possible !

Vous pouvez imbriquer aussi profondément que vous le souhaitez (bien que la chose sensée à faire soit de garder cela à un niveau raisonnable).

Donc, avec cette nouvelle révélation vient ceci...

L'élément 1 (le premier élément flexible) peut également être transformé en un conteneur flexible.

La barre latérale (élément 1b) et la section principale (élément 1a) seraient alors des éléments flexibles.

![Image](https://cdn-media-1.freecodecamp.org/images/b7Re-CAnjyJabWvSsin4T5VAfWgJJFQe3FHX)

Vous êtes toujours avec moi, n'est-ce pas ?

Décomposer votre mise en page de cette manière vous donne un très bon modèle mental à travailler.

Lorsque vous commencez à construire des mises en page encore plus complexes avec le modèle Flexbox, vous verrez à quel point cela est vital.

Vous n'avez pas besoin d'une image fantaisiste comme celles ci-dessus. Un simple croquis sur papier devrait suffire pour vous lancer.

Vous vous souvenez que j'ai dit que vous pouviez imbriquer aussi profondément que vous le souhaitiez ? Il semble que vous puissiez faire une imbrication supplémentaire ici.

Jetez un coup d'œil à la section principale ci-dessus (Élément 1a).

Elle pourrait également être transformée en un conteneur flexible pour contenir les sections mises en évidence ci-dessous. "Élément 1a — A" et "Élément 1a — B"

![Image](https://cdn-media-1.freecodecamp.org/images/EMKDL6rpg1E2crXIMAxaMsi2rnt5YV-6f4sB)

Vous pouvez décider de ne pas faire de la section principale (élément 1a) un conteneur flexible et simplement y mettre deux "divs" pour contenir les sections mises en évidence.

Oui, c'est possible, puisque "Élément 1a — A" et "Élément 1a — B" sont empilés verticalement.

Par défaut, les "divs" s'empilent verticalement. C'est ainsi que fonctionne le modèle de boîte.

Si vous choisissez de faire de la section principale un conteneur flexible, vous disposez des puissantes propriétés d'alignement à votre disposition. Au cas où vous en auriez besoin à un moment donné.

Le "flex" dans Flexbox signifie flexible.

Les conteneurs flexibles sont par défaut flexibles, un peu comme réactifs.

Cela peut être une autre raison d'utiliser un conteneur flexible plutôt que des "divs" réguliers. Cela dépend cependant du scénario.

Je vais aborder d'autres choses pendant que vous construisez catty music. Vous devriez commencer à écrire du code maintenant.

#### Configuration HTML de base

Commencez par la configuration HTML de base ci-dessous.

```
<!DOCTYPE html>  <html>  <head>  <title>Catty Music</title>  </head>  <body>
```

```
<main></main> <!-- pour contenir la section principale de l'application -->
```

```
<footer></footer> <!-- pour contenir les boutons de contrôle de la musique et les détails de la chanson -->
```

```
</body></html>
```

Alors, stylez ceci...

```
html,  body {    height: 100%; /* définir cela explicitement est important */  }
```

```
body {    display: flex; /* superpouvoirs flex activés ! */    flex-direction: column; /* Empiler les éléments flexibles (éléments main et footer) verticalement et non horizontalement */  }
```

La première étape pour utiliser le modèle Flexbox est d'établir un conteneur flexible.

C'est exactement ce que fait le code ci-dessus. Il définit la propriété d'affichage de l'élément body sur `flex`.

Maintenant, vous avez un conteneur flexible, l'élément body.

Les éléments flexibles sont également définis (élément 1 et élément 2) — comme dans la décomposition faite précédemment.

Notez que vous devriez jeter un autre coup d'œil aux images que j'ai montrées dans ma décomposition initiale précédente si ce concept semble encore flou pour vous.

En gardant à l'esprit l'image de la fin, vous devriez faire fonctionner les éléments flexibles.

#### Faire en sorte que le pied de page reste en bas.

Le pied de page, qui contient les commandes de musique, reste en bas de la page tandis que la section principale remplit l'espace restant.

Comment faites-vous cela ?

```
main {    flex: 1 0 auto; /* remplir l'espace disponible */  }
```

```
footer {    flex: 0 0 90px; /* ne pas grandir ou rétrécir - rester à une hauteur de 90px. */  }
```

Veuillez consulter les commentaires dans la liste de code ci-dessus.

Grâce à la propriété `flex-grow`, il est relativement facile de faire en sorte que la section principale remplisse tout l'espace.

Il suffit de définir la valeur `flex-grow` à 1. Vous devez également définir la propriété `flex-shrink` à zéro. Pourquoi ?

La raison peut ne pas être évidente ici parce que la direction flex est changée.

Dans certains navigateurs, il y a un bug qui permet aux éléments flexibles de rétrécir en dessous de la taille de leur contenu. C'est un comportement assez étrange.

La solution à ce bug est de garder la valeur `flex-shrink` à `0`, et non à la valeur par défaut de `1`, et de définir également la propriété `flex-basis` à `auto`.

C'est comme dire : « S'il vous plaît, calculez automatiquement la taille de l'élément flexible, mais ne le rétrécissez jamais. »

Avec cette valeur raccourcie, vous obtenez toujours le comportement par défaut des éléments flexibles.

L'élément flexible se rétrécirait lors du redimensionnement du navigateur. Le redimensionnement n'est pas basé sur la propriété `shrink`. Il est basé sur le recalcul automatique de la largeur de l'élément flexible. `flex-basis: auto`

Cela fera en sorte que l'élément flexible soit au moins aussi grand que sa largeur ou sa hauteur (si déclarées) ou sa taille de contenu par défaut.

Veuillez ne pas oublier le cadre dans lequel j'ai décomposé les propriétés `flex-shorthand`. Il y aura beaucoup de choses raccourcies à venir.

Maintenant que les choses commencent à se mettre en place, ajoutons un peu de style pour définir les espaces et les couleurs :

```
body {    display: flex;    flex-direction: column;    background-color: #fff;    margin: 0;    font-family: Lato, sans-serif;    color: #222;    font-size: 0.9em;  }  footer {    flex: 0 0 90px;    padding: 10px;    color: #fff;    background-color: rgba(61, 100, 158, .9);  }
```

Rien de magique pour l'instant.

Voici ce que vous devriez avoir maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/NXQ9LR3Hzk--gRakEmZDq3gvYWLLmMFI7n6u)

En voyant comment les choses commencent à prendre forme, vous allez les améliorer encore.

#### Fixer la barre latérale.

Si vous codez en même temps, mettez à jour votre document HTML.

```
<main>  <aside> <!-- Cela représente la barre latérale et contient des ensembles d'icônes de font-awesome -->    <i class="fa fa-bars"></i>    <i class="fa fa-home"></i>    <i class="fa fa-search"></i>    <i class="fa fa-volume-up"></i>    <i class="fa fa-user"></i>    <i class="fa fa-spotify"></i>    <i class="fa fa-cog"></i>    <i class="fa fa-soundcloud"></i>  </aside>
```

```
<section class="content"> <!-- Cette section contiendra tout sauf la barre latérale -->  </section>
```

```
</main>
```

La liste ci-dessus est assez explicative.

Pour les ensembles d'icônes, j'utilise la bibliothèque populaire [Font Awesome](http://fontawesome.io/).

Avoir l'icône souhaitée est aussi simple que d'ajouter une classe CSS. C'est ce que j'ai fait dans la balise `aside`.

Comme expliqué précédemment, la section « main » ci-dessus sera également transformée en un conteneur flexible. La barre latérale (représentée par la balise aside), et la section seront des éléments flexibles.

```
main {  flex: 1 0 auto; /* Est un élément flexible */  display: flex; /* Je viens de l'inclure ! - maintenant un conteneur flexible avec des éléments flexibles : sidebar & section de contenu principal */  }
```

D'accord, cela devient intéressant, n'est-ce pas ?

Maintenant, vous avez la section principale comme un conteneur flexible. Traitez l'un de ses éléments flexibles, la barre latérale.

Tout comme vous avez fait en sorte que le pied de page reste en bas de la page, vous voulez également que la barre latérale reste — cette fois à gauche de la page.

```
aside {       flex: 0 0 40px; /* ne pas grandir ou rétrécir. Rester fixe à 40px */ }
```

La barre latérale doit avoir des icônes empilées verticalement.

Vous pouvez faire de la barre latérale un conteneur flexible et lui donner une direction flexible qui permet à toutes les icônes de s'empiler verticalement.

Ensuite, appliquez une propriété d'alignement pour avoir les icônes en position.

Voyez comment vous pouvez faire cela dans la liste ci-dessous.

```
aside {       /* ...  */
```

```
    display: flex; /* Maintenant un conteneur flexible aussi */          flex-direction: column; /* empiler les icônes verticalement */          /* puisque la direction est changée, cela fonctionne sur la direction verticale */
```

```
    justify-content: space-around;   
```

```
        align-items: center; /* la direction est changée ! Cela affecte la direction horizontale. Place les icônes au centre */          background-color: #f2f2f2; /* me rendre joli */  }
```

```
     aside i.fa {        font-size: 0.9em;  /* taille de police pour les icônes */  }
```

J'ai commenté de manière obsessionnelle le code ci-dessus et maintenant voyez à quel point tout est joliment disposé.

Super propre avec quelques lignes de code.

Code raisonnable, pas de hacks désordonnés.

![Image](https://cdn-media-1.freecodecamp.org/images/owl8OSMhTJ25G849L5adFH4O2dI5y7sLx6QD)
_Barre latérale traitée proprement_

La section de contenu principal est actuellement vide. N'oubliez pas qu'elle est le deuxième élément de la liste. La barre latérale est la première.

Mettez-y quelques éléments.

#### Ajout de contenu à la section principale.

Vous pouvez jeter un autre coup d'œil au projet terminé, pour ne pas perdre de vue où cela mène.

Plus important encore, cela vous aidera à comprendre la prochaine liste de code.

Mettez à jour votre document HTML et placez ces éléments dans la section `.content`.

```
<section class="content"> <!-- Cette section était vide. La remplir avec du contenu -->
```

```
<div class="music-head"> <!-- Premier élément de la liste : contient les détails de la musique -->
```

```
     <img src="images/cattyboard.jpg" /> <!-- Art de l'album -->
```

```
     <section class="catty-music"> <!-- autres détails de l'album -->          <div>            <p>CattyBoard Top 100 Single Charts (11.06.36)</p>            <p>Artiste Inconnu</p>            <p>2016 . Classements . 100 chansons</p>          </div>
```

```
         <div> <!-- Contrôles de la musique -->            <i class="fa fa-play"> 
0Play all</i>            <i class="fa fa-plus"> 
0Add to</i>            <i class="fa fa-ellipsis-h">
0
0More</i>          </div>     </section>
```

```
 </div> <!-- fin .music-head -->
```

```
<!-- Deuxième élément de la liste : Contient une liste de toutes les chansons affichées -->
```

```
<ul class="music-list">        <li>          <p>1. One Dance</p>          <p>Crake feat CatKid & Cyla</p>          <p>2:54</p>          <p><span class="catty-cloud">CATTY CLOUD SYNC</span></p>      </li>
```

```
      <li>          <p>2. Panda</p>          <p>Cattee</p>          <p>4:06</p>          <p><span class="catty-cloud">CATTY CLOUD SYNC</span></p>      </li>
```

```
      <li>          <p>3. Can't Stop the Feeling!</p>          <p>Catin Cimberlake</p>          <p>3:56</p>          <p><span class="catty-cloud">CATTY CLOUD SYNC</span></p>      </li>
```

```
      <li>          <p>4. Work From Home</p>          <p>Cat Harmony feat Colla</p>          <p>3:34</p>          <p><span class="catty-cloud">CATTY CLOUD SYNC</span></p>      </li>    </ul></section>
```

Um, j'ai ajouté un peu plus que la dernière fois, mais c'est assez simple.

J'ai rempli la section de contenu vide avec une `div` qui contient l'art de l'album et quelques détails de l'album catty.

La `ul` contient une liste de chansons de l'album.

Le _titre de la chanson_, _l'artiste_, _la durée_ et "_catty cloud sync_" sont contenus dans des paragraphes individuels au sein de la liste.

Alors, que allez-vous faire avec le style ?

Vous voyez ce que j'ai fait ?

Tout d'abord, vous devriez faire de la section `.content` un conteneur flexible.

```
.content {    display: flex;
```

```
    flex: 1 1 auto; /* cela garantit que la section grandit pour remplir tout l'espace disponible et se rétrécit également */
```

```
    flex-direction: column;}
```

Vous devriez également traiter ses éléments flexibles :

```
.music-head {   flex: 0 0 280px; /* Même mémo, ne pas grandir ou rétrécir - rester à 280px */
```

```
  display: flex;    padding: 40px;  background-color: #4e4e4e;}
```

```
.music-list {    flex: 1 0 auto;    list-style-type: none;    padding: 5px 10px 0px;}
```

`.music-head` contient l'art de l'album et d'autres détails liés à l'album.

Même mémo, ne pas grandir ou rétrécir mais garder une hauteur de 280px.

Hauteur ? Pas largeur ? Oui !

L'élément parent avait déjà la `flex-direction` changée.

Oh, vous allez avoir besoin que cela soit un conteneur flexible plus tard aussi. Donc mettez `display: flex`.

`.music-list` contient la liste des chansons et remplit l'espace disponible restant partagé avec `.music-head` ci-dessus.

Cela ne semble pas très joli encore, mais vous faites du bon travail si vous suivez toujours.

Pouce levé.

![Image](https://cdn-media-1.freecodecamp.org/images/oFKtcL6vacB5d99qNJW5WKjGC6jD9B59Nh4u)
_catty music - inachevé_

Il y a quelques problèmes ici.

1. **La liste des chansons a l'air terrible.**

![Image](https://cdn-media-1.freecodecamp.org/images/YXrbtyVshgwW3YwRSgta7wOUFDHypjn8klL4)
_liste des chansons_

2. La section contenant l'art musical a un **texte vraiment laid**.

![Image](https://cdn-media-1.freecodecamp.org/images/4ZUF63ee6eNF8Kz7WHt2rvUoL8Hho3pccH-Z)
_Textes laids de l'art musical_

Encore une fois, je vais vous guider à travers la résolution de ces problèmes.

Voici les solutions que je propose.

#### Traiter la liste des chansons

Chaque liste de chansons contient 4 paragraphes. Titre de la chanson, artiste, durée et "catty cloud sync".

Il doit y avoir un moyen de mettre tout cela sur une seule ligne, chaque paragraphe occupant un espace égal sur cette ligne.

Flexbox à la rescousse !

Le concept ici est le même que celui utilisé dans de nombreux systèmes de grille.

Traduisez cela en code.

```
li {  display: flex; /* Les paragraphes sont maintenant affichés sur une seule ligne */  padding: 0 20px; /* Un peu d'espace pour respirer */  min-height: 50px;}
```

```
li p {  flex: 0 0 25%; /* C'est la sauce sucrée */}
```

Vous voyez ce qui se passe là avec les paragraphes ?

```
flex: 0 0 25%;
```

« Ne pas grandir ou rétrécir, mais chaque paragraphe doit occuper 25 % de l'espace disponible ».

L'espace est partagé également entre les paragraphes.

#### Utilisation de cette technique

Cette technique est inestimable. Vous pouvez l'utiliser pour créer des zones de contenu inégales. Par exemple, une vue à deux colonnes.

Une section peut occuper 60 % de l'espace disponible, et l'autre 40 %.

```
.first-section: 0 0 60%;
```

```
.second-section: 0 0 40%;
```

Vous pouvez utiliser cette technique pour créer des systèmes de grille.

Voici comment les listes devraient apparaître maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/m81B75ZeZpW9-o76GLW-eogrSUX6YDcC9pwE)
_Liste des chansons corrigée_

Donnez aux listes des couleurs alternées, traitez également l'étiquette "catty cloud sync".

```
li span.catty-cloud {  border: 1px solid black;  font-size: 0.6em;  padding: 3px;}
```

```
li:nth-child(2n) {  background-color: #f2f2f2;}
```

Alors, vous êtes en train de tout casser, et vous commencez vraiment à comprendre le "jargon flexbox" mieux.

C'est ce que vous devriez avoir maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/ZK8WvEkvPCIr4w9Exkz96mTrvQwi1jhCg-mO)
_Catty music — presque terminé_

Le deuxième problème sera traité maintenant.

#### Rendre le texte des détails de l'album plus joli.

Des choses vraiment simples se passent en dessous.

```
.catty-music{  flex: 1 1 auto;  display: flex;  flex-direction: column;  font-weight: 300;  color: #fff;  padding-left: 50px;}
```

```
.catty-music div:nth-child(1){  margin-bottom: auto;}
```

```
.catty-music div:nth-child(2){  margin-top: 0;}
```

```
.catty-music div:nth-child(2) i.fa{  font-size: 0.9em;  padding: 0 0.7em;  font-weight: 300;}.catty-music div:nth-child(1) p:first-child{  font-size: 1.8em;  margin: 0 0 10px;}
```

```
.catty-music div:nth-child(1) p:not(:first-child){  font-size: 0.9em;  margin: 2px 0;}
```

et vous l'avez fait.

Vous avez presque terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/rlbT0BeurDWJjeD2Tin-1pnhCol57QUqTzGr)
_Textes de l'art musical beaucoup plus beaux_

### Un exercice rapide

J'ai gardé le pied de page pour que vous puissiez travailler dessus comme exercice.

Essayez de corriger le pied de page vous-même. Utilisez simplement les mêmes techniques. Vous pouvez le faire, vous savez ?

Si vous êtes bloqué, vous pouvez toujours consulter le code source complet de catty music.

Vous pouvez également diviser tout le pied de page en éléments flexibles, et commencer à partir de là.

![Image](https://cdn-media-1.freecodecamp.org/images/wyb3ofh5UeUL-U7XgIGgQ4Bes4hIBXZnlNF3)
_Pied de page expliqué_

Wow. Je n'arrive pas à croire que vous soyez arrivé à ce point. C'est génial ! Vous devenez un ninja de Flexbox maintenant.

Ensuite, vous verrez comment Flexbox aide avec les designs responsives.

### Design responsive avec Flexbox

![Image](https://cdn-media-1.freecodecamp.org/images/7mKG3OFgA3rhs9ELMxrzdTv9hN3BdocmqUWr)

Des livres ont été écrits sur le design responsive, de bons livres d'ailleurs.

Puisque cet article se concentre sur le modèle Flexbox, je ne vais pas plonger profondément dans l'état général des designs responsives.

Comme je l'ai mentionné quelque part plus tôt, nous obtenons une certaine réactivité avec le modèle Flexbox.

Flexbox comme dans "boîte flexible".

Cependant, il est possible de cibler diverses tailles d'écran via des requêtes média et de changer ensuite le comportement flex.

Voici un exemple.

La liste non ordonnée pratique vient à la rescousse à nouveau.

```
<ul>    <li>Accueil</li>    <li>À propos</li>    <li>Contact</li>    <li>S'inscrire</li>    <li>Se connecter</li>  </ul>
```

et avec un peu de style...

```
ul {        list-style-type: none;        display: flex;        border: 1px solid #4e4e4e;    }
```

```
li {        flex: 0 0 auto;        padding: 10px;        margin: 10px;        background-color: #8cacea;        color: #fff;        font-size: 1em;    }
```

Vous êtes un pro de ce truc flex maintenant, donc vous comprenez ce qui se passe là-haut.

Voici à quoi ressemble la barre de navigation.

![Image](https://cdn-media-1.freecodecamp.org/images/IlAkBuNqc12truVN5Kdl-JLLhidWk4R6pbL-)
_Navigation Flexbox_

Bien que cela puisse être cool pour les ordinateurs de bureau et les tablettes, à certaines tailles d'écran, cela ne semble pas bien.

Sur mobile, vous voudriez empiler les éléments de navigation verticalement.

Ensuite, les requêtes média entrent en jeu.

```
@media screen and (max-width: 769px) {
```

```
/* le code ici ne s'applique qu'aux appareils écran dont la largeur est inférieure à 769px */         ul {        flex-direction: column; /* Sur les appareils plus petits, changer la direction */    }
```

```
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/n7K6yuEN8nqC4UBxG1c8niDgRUrpibBQOiEW)
_Barre de navigation pour les appareils mobiles_

Si vous connaissiez déjà quelques notions de design responsive, c'est génial.

Il suffit de transposer le modèle Flexbox sur vos connaissances existantes et vous êtes prêt à partir.

Au fait, j'ai fait l'hypothèse que vous comprenez ce que sont les requêtes média.

Si ce n'est pas le cas, voyez le briefing rapide ci-dessous.

#### Requêtes média

Les requêtes média sont au cœur du design responsive. Elles vous permettent de cibler des tailles d'écran spécifiques et de spécifier des codes à exécuter sur ces appareils uniquement.

La forme la plus populaire sous laquelle les requêtes média sont utilisées est ce que l'on appelle la règle _@media_.

Cela ressemble à ceci :

```
@media screen and (max-width: 300px) {  /* écrire votre css dans ce bloc de code */}
```

En le regardant, vous pouvez presque deviner ce qu'il fait.

"Pour un appareil écran avec une largeur maximale de 300px ... faites ceci et cela" 

Tout style dans le bloc de code ne s'appliquera qu'aux appareils qui correspondent à l'expression, "screen and (max-width: 300px)".

Je suppose que cela a aidé à clarifier certaines confusions.

#### Exercice rapide

Catty music est affiché différemment sur les appareils mobiles. C'est une bonne nouvelle. Ce qui est encore mieux, c'est que vous devriez essayer de recréer cela.

![Image](https://cdn-media-1.freecodecamp.org/images/wQLo3x-ciAw8Xg0k9F3QVehgXxZyr499iqCA)
_catty music mobile_

Au cas où vous seriez bloqué, le lien vers le dépôt pour ce tutoriel se trouve dans la section suivante. La solution à cela se trouve également dans le dépôt.

Vous êtes presque à la fin !

Dans la section de conclusion, je vais discuter de la compatibilité des navigateurs, des liens utiles et des ressources pour vous aider à avancer.

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/FBQ056-MrxnyOByMNsoRR56qzYcXP8XCpVj4)

Vous avez appris à utiliser les propriétés d'alignement des conteneurs flexibles et des éléments flexibles.

Je vous ai guidé à travers la compréhension des flex absolus et relatifs, des alignements de marges automatiques et du changement de direction flex.

Vous avez également eu l'occasion d'appliquer vos compétences en "flex" à la construction de _Catty Music_, puis j'ai abordé le design responsive.

Cela a été un long voyage en effet.

Maintenant, je vais vous expliquer quelques concepts finaux. Vous aider avec des ressources et des liens que je pense que vous trouverez très utiles.

### Comment est la compatibilité des navigateurs pour Flexbox ?

C'est une question courante posée lorsque l'on cherche à utiliser le modèle Flexbox en production.

Je ne peux pas répondre à la question parfaitement, mais le site [caniuse](http://caniuse.com/) rend justice à cela.

Voici une capture d'écran de _caniuse_, et la compatibilité des navigateurs est assez impressionnante. Vous pouvez voir par vous-même [ici](http://caniuse.com/#feat=flexbox).

![Image](https://cdn-media-1.freecodecamp.org/images/nFTAbG7ASL74Eeho0WAJD5iPL7pP3mwJUji6)

Au début de ma carrière, j'ai consulté _caniuse_ à plusieurs reprises et je n'ai toujours pas compris ce que les données représentaient. Alors voici une brève explication.

En bas à droite du site _caniuse_ se trouve une légende.

![Image](https://cdn-media-1.freecodecamp.org/images/9mmJyaD2yVAbYSEfSjh3k203aLDxUTlvCbf3)
_[caniuse](http://caniuse.com" rel="noopener" target="_blank" title=") légende_

Jetez un coup d'œil à l'image ci-dessus, ou visitez simplement le site, trouvez la légende et vous serez prêt à partir.

C'est en fait tout ce qu'il y a à savoir.

### Ressources supplémentaires

J'espère que vous trouverez celles-ci utiles :

1. Obtenez l'intégralité de l'article Comprendre Flexbox sous forme de [document PDF](http://bit.ly/und_f) — lien direct
2. Le cours [Interactif Flexbox](https://www.educative.io/collection/5191711974227968/5741031244955648)
3. [Jouer avec le code de Catty Music en ligne](http://output.jsbin.com/wubudog/)
4. [Le dépôt pour l'intégralité du tutoriel « Comprendre Flexbox »](https://github.com/ohansemmanuel/Understanding-Flexbox)
5. [Flexbox Froggy : Un jeu Flexbox cool](http://flexboxfroggy.com/)

Enfin, je dois dire merci de m'avoir suivi.

### Voulez-vous devenir Pro ?

Téléchargez ma feuille de triche CSS Grid gratuite, et obtenez également deux cours interactifs Flexbox de qualité gratuitement !

![Image](https://cdn-media-1.freecodecamp.org/images/FlmwIIP7ogHeiKUChUWTMGuCzDK099yiQAuf)
_[Obtenez la feuille de triche CSS Grid gratuite + Deux cours Flexbox de qualité gratuitement !](http://eepurl.com/dcNiP1" rel="noopener" target="_blank" title=")_

[Obtenez-les maintenant](http://eepurl.com/dcNiP1)