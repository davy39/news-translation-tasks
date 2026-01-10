---
title: Comment fonctionnent le positionnement CSS et Flexbox – Expliqué avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-09T01:25:42.000Z'
originalURL: https://freecodecamp.org/news/css-positioning-and-flexbox-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--38-.png
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
seo_title: Comment fonctionnent le positionnement CSS et Flexbox – Expliqué avec des
  exemples
seo_desc: 'By Nishant Kumar

  If you have ever used CSS, then you know how hard it is to position elements. But
  by the end of this tutorial you''ll know much more about CSS positioning and Flexbox,
  and you''ll be able to position elements in your dream project like...'
---

Par Nishant Kumar

Si vous avez déjà utilisé CSS, alors vous savez à quel point il est difficile de positionner des éléments. Mais à la fin de ce tutoriel, vous en saurez beaucoup plus sur le positionnement CSS et Flexbox, et vous pourrez positionner des éléments dans votre projet de rêve comme un chef.

Tout d'abord, comprenons quelques bases sur le positionnement CSS.

## Propriété de position CSS

Vous pouvez utiliser la propriété de position CSS pour positionner des éléments, des divs et des conteneurs en CSS selon vos besoins. La grande chose à propos de la propriété de position est que vous pouvez l'utiliser pour arranger les éléments de votre application où vous voulez, et c'est facile à apprendre et à implémenter.

Il existe cinq types de positionnement en CSS :

1. Positionnement statique
2. Positionnement relatif
3. Positionnement absolu
4. Positionnement fixe
5. Positionnement collant

Apprenons-les un par un.

## Positionnement statique en CSS

Le positionnement statique est la propriété de positionnement par défaut utilisée en CSS. Il suit toujours le flux normal de la page. Quel que soit l'élément qui vient en premier dans votre document, il sera affiché en premier.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--30-.png)
_Sortie_

Voici à quoi ressemblerait le code :

```css
/* Positionnement statique */
.parent {
    padding: 5px;
    position: static;
    background-color: #00AAFF;
    width: 40%;
  }

  .child-one {
  	position: static;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
  	position: static;
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
  	position: static;
    background-color: rgb(255, 116, 232);
  }
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Position et Flexbox</title>
    <link rel="stylesheet" href="./index.css">
</head>
<body>
    <div class="parent">Parent
        <div class="child-one">One</div>
        <div class="child-two">Two</div>
        <div class="child-three">Three</div>
    </div>
</body>
</html>
```

Dans l'exemple ci-dessus, nous avons notre parent, puis child one, puis child two, et enfin child three. Ils sont tous arrangés selon le positionnement statique, c'est-à-dire selon le flux normal de la page.

## Positionnement relatif en CSS

Le positionnement relatif fonctionne exactement comme le positionnement statique, mais il y a un piège.

Il y a quatre choses que nous pouvons faire en positionnement relatif que nous ne pouvons pas faire avec le statique : nous pouvons déplacer nos éléments à gauche, à droite, en bas et en haut.

Comprenons ce que je veux dire avec un exemple.

```css
/* Positionnement relatif */
.parent {
    padding: 5px;
    background-color: #00AAFF;
    width: 40%;
  }

  .child-one {
    position: relative;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--31-.png)

Si nous exécutons notre application, nous verrons qu'il n'y a aucune différence dans la sortie. En d'autres termes, le positionnement statique et relatif sont les mêmes, sauf si nous utilisons top, bottom, left et right avec le relatif.

Essayons d'utiliser top, bottom, left et right.

```css
/* Positionnement relatif avec Top, Bottom, Left et Right */
.parent {
    padding: 5px;
    background-color: #00AAFF;
    width: 40%;
  }

  .child-one {
    position: relative;
    top: 10px;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
  }
```

Nous utilisons **Top** avec **Relative** dans **child-one.**

Cela sort **child-one** du flux du document, et il se décalera du haut vers le bas de 10px.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--32-.png)
_Positionnement relatif avec Top_

Vous pouvez voir qu'il couvre l'élément **child-two**. Et il en sera de même si vous utilisez left, right ou bottom, selon la propriété.

La principale raison pour laquelle **child-one** couvre **child-two** est que **child-one** ne fait plus partie du flux normal du document, mais **child-two** et **child-three** en font toujours partie.

## Positionnement absolu en CSS

La prochaine façon de positionner des éléments est avec le positionnement absolu. Ce positionnement retire complètement l'élément du flux du document. Tous les autres éléments ignoreront l'élément qui a la **propriété absolue.**

Et si nous utilisons Top, Bottom, Left ou Right avec Absolute, il arrangera l'élément selon le conteneur parent, _à condition que le conteneur parent soit également positionné de manière absolue._

```css
/* Positionnement absolu */
.parent {
    padding: 5px;
    background-color: #00AAFF;
    width: 40%;
    position: static;
  }

  .child-one {
    position: absolute;
    top: 0px;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--33-.png)

Ici, child one est en dehors du flux normal du document, si nous définissons **Top à 0px.**

C'est parce que child-one est absolu, et le parent est statique.

Mais que se passe-t-il si nous définissons le parent à **absolu avec top à 0px** ?

```css
/* Positionnement absolu */
.parent {
    padding: 5px;
    background-color: #00AAFF;
    width: 40%;
    position: absolute;
    top: 0px;
  }

  .child-one {
    position: absolute;
    top: 0px;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--34-.png)

Ici, vous pouvez voir que le premier enfant chevauche l'élément parent, et les deux sont **en haut avec 0px.**

Il y a un troisième cas d'utilisation, où nous pouvons définir le **Parent comme relatif** et le **premier enfant comme absolu.**

```css
/* Positionnement absolu */
.parent {
    padding: 5px;
    background-color: #00AAFF;
    width: 40%;
    position: relative;
    top: 0px;
  }

  .child-one {
    position: absolute;
    top: 0px;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--35-.png)

C'est le cas d'utilisation le plus utile lorsque nous utilisons relatif avec absolu. Maintenant, vous pouvez voir que notre **child-one** est relatif à l'**élément parent**, et non au document entier.

En termes plus simples, si vous fixez le parent comme relatif et l'enfant comme absolu, l'enfant suivra le parent comme son conteneur.

## Positionnement fixe en CSS

Vous vous souvenez de l'absolu avec le positionnement relatif ? Il y a une position qui ignore complètement l'élément parent, et c'est le positionnement fixe.

Le positionnement fixe est fixe selon l'ensemble du document HTML. Il ne suivra aucun autre parent, même s'il est défini comme relatif.

Une autre chose est que si nous définissons quelque chose comme fixe, il restera dans la même position même si nous faisons défiler.

Le positionnement fixe est principalement utilisé pour les éléments et boutons flottants.

```css
/* Positionnement fixe */
.parent {
    padding: 5px;
    background-color: #00AAFF;
    width: 40%;
    position: relative;
    top: 0px;
    height: 1000px;
  }

  .child-one {
    position: fixed;
    top: 0px;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--36-.png)

Vous pouvez voir que le premier élément est complètement en dehors de son composant parent, même si le parent est défini comme relatif.

Et si nous faisons défiler, le reste des enfants suivra le flux du document, mais le fixe restera le même.

## Positionnement collant en CSS

La position collante est la combinaison du relatif et du fixe.

```css
/* Positionnement collant */
.parent {
    padding: 5px;
    background-color: #00AAFF;
    width: 40%;
    position: relative;
    top: 0px;
    height: 1000px;
  }

  .child-one {
    position: sticky;
    top: 0px;
    background-color: rgb(116, 255, 116);
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--37-.png)

Si nous définissons un enfant en positionnement collant, il aura l'air normal, comme relatif. Mais dès que nous commençons à faire défiler, l'élément enfant collant collera en haut. Il deviendra une position fixe.

La position collante est principalement utilisée pour créer des barres de navigation.

Maintenant que nous avons terminé avec les positions CSS, concentrons-nous sur Flexbox.

## Comment utiliser Flexbox

Vous pouvez utiliser la propriété CSS Flexbox pour arranger des éléments sans utiliser float. Cela rend l'arrangement des éléments dans le document beaucoup plus facile. Vous pouvez l'utiliser pour remplacer les Grids en CSS.

Sans Flexbox, notre sortie suivra le flux du document, c'est-à-dire child-one, puis child-two, et enfin child-three.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-14-00-12.png)

Mais que se passe-t-il si nous voulions les voir côte à côte horizontalement, comme dans l'image ci-dessous ?

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-14-01-02.png)

La solution est Flexbox. Nous devons les positionner de manière uniforme par rapport aux lignes ou aux colonnes, avec des espaces entre eux ou autour d'eux.

Pour commencer, créons une div parent avec trois enfants à l'intérieur.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Position et Flexbox</title>
    <link rel="stylesheet" href="./index.css">
</head>
<body>
    <div class="parent">
        <div class="child-one"></div>
        <div class="child-two"></div>
        <div class="child-three"></div>
    </div>
</body>
</html>
```

Quelque chose comme ceci :

```css
/* Conteneur Flexbox */
.parent {
    background-color: #00AAFF;
    width: 300px;
    height: 300px;
    display: flex;
  }

  .child-one {
    background-color: rgb(116, 255, 116);
    width: 300px;
    height: 300px;
  }
  
  .child-two {
    background-color: rgb(248, 117, 117);
    width: 300px;
    height: 300px;
  }
  
  .child-three {
    background-color: rgb(255, 116, 232);
    width: 300px;
    height: 300px;
  }
```

Nous pouvons voir que le parent a été déclaré comme **flex.**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-14-01-02-1.png)

Ici, nous avons trois div boxes, chacune avec des couleurs différentes. C'est l'arrangement Flexbox par défaut.

Voyons les différents types d'arrangements dans Flexbox.

## Comment arranger des éléments avec Flexbox

### Direction Flex

Cette propriété définit comment vos éléments apparaîtront à l'écran, c'est-à-dire verticalement ou horizontalement.

**Row** est utilisé pour arranger les éléments horizontalement.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-38-32.png)

Comme vous pouvez le voir, nous avons l'arrangement dans une ligne horizontale.

**Column** arrange les éléments verticalement, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-39-10.png)

Les carrés sont maintenant arrangés dans une colonne verticale.

**Row Reverse** fonctionne exactement comme row, mais la position des éléments sera inversée. Le premier élément sera le dernier, et le dernier élément se déplacera au premier. L'arrangement des éléments sera l'opposé de **flex-direction: row.**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-39-51.png)

**Column Reverse** fonctionne exactement comme column, mais les éléments seront inversés. Le premier élément sera le dernier, et le dernier élément se déplacera au premier.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-42-38.png)

### Justify Content

Cette propriété détermine l'alignement des éléments de manière horizontale.

**Center** place les éléments au centre horizontal de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-43-23.png)

**Flex Start** positionne l'élément au début de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-44-15.png)

**Flex End** place l'élément à la fin de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-44-40.png)

**Space Around** arrange les éléments de manière uniforme mais avec des espaces entre eux. Les espaces seront égaux parmi tous les éléments à l'intérieur d'un conteneur flex-box, mais pas à l'extérieur.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-45-24.png)

Ici, les espaces entre child-one, child-two et child-three sont égaux, mais pas à l'extérieur.

**Space Between** maximise les espaces entre les éléments enfants (c'est une propriété Justify Content).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-45-54.png)

**Space Evenly** distribue des espaces égaux entre les éléments enfants et l'espace à l'extérieur du conteneur FlexBox.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-46-41.png)

### Align Items

Align items est utilisé pour aligner les éléments verticalement à l'intérieur d'un conteneur flex. Mais cela ne fonctionne que s'il y a une hauteur fixe.

**Center** place les éléments au centre de la page, verticalement.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-47-26.png)

**Flex Start** est le même que Justify Content to Center, mais il arrange les éléments verticalement. Dans notre cas, les éléments seront dans le coin supérieur gauche de l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-48-12.png)

**Flex End** est le même que Flex Start, mais cela alignera les éléments dans le coin inférieur gauche de l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-05-05-48-42.png)

Maintenant, vous connaissez quelques bases de Flexbox.

## Comment aligner les éléments au centre de l'écran.

Ces propriétés Flexbox peuvent également être utilisées ensemble. Par exemple, si nous voulons arranger les éléments au centre, nous pouvons utiliser à la fois **align-items: center** et **justify-content: center.**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-07-16-31-13.png)

Vous pouvez [trouver le code sur Github](https://github.com/nishant-666/CSS-Positioning-and-Flexbox) si vous voulez expérimenter davantage.

C'est tout pour aujourd'hui – merci d'avoir lu.

> Continuez à expérimenter. Continuez à apprendre !