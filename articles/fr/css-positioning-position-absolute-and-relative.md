---
title: Positionnement CSS – Exemple de Position Absolute et Relative
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-01T18:30:19.000Z'
originalURL: https://freecodecamp.org/news/css-positioning-position-absolute-and-relative
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/greg-rakozy-vw3Ahg4x1tY-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Positionnement CSS – Exemple de Position Absolute et Relative
seo_desc: "When you want to design complex layouts, you'll need to change the typical\
  \  document flow and override the default browser styles. \nYou have to control\
  \ how elements behave and are positioned on the page.\nFor example, you may want\
  \ to stack elements ne..."
---

Lorsque vous souhaitez concevoir des mises en page complexes, vous devrez modifier le flux de document typique et remplacer les styles par défaut du navigateur. 

Vous devez contrôler le comportement et le positionnement des éléments sur la page.

Par exemple, vous pouvez vouloir empiler des éléments les uns à côté des autres ou les uns sur les autres d'une manière spécifique, ou faire en sorte qu'un en-tête "colle" en haut de la page et ne bouge pas lorsque vous faites défiler la page vers le haut et vers le bas.

Pour faire ce qui précède, et bien plus encore, vous utiliserez la propriété `position` de CSS. 

Cette propriété prend cinq valeurs : `static`, `relative`, `absolute`, `fixed` et `sticky`.

Dans cet article, nous nous concentrerons sur les valeurs `relative` et `absolute`. 

Nous verrons un aperçu de leur fonctionnement, leurs différences et comment elles sont mieux utilisées conjointement pour un effet maximal.

Commençons !

## Comment voir la position des éléments à l'aide des outils de développement Chrome

Un outil utile dans votre flux de travail de développement web front-end est les outils de développement de Chrome.

Parmi beaucoup d'autres choses, vous avez la possibilité de regarder le code HTML/CSS/JavaScript de n'importe quel site web pour comprendre comment différents styles fonctionnent.

Pour voir quelle position un élément a sur une page web sur un Mac, appuyez sur `Control` et cliquez en même temps sur l'élément souhaité. Sur un PC Windows, faites un clic droit sur l'élément que vous souhaitez sélectionner.

Un menu apparaîtra, puis sélectionnez `Inspecter`.

Les outils de développement Chrome s'ouvriront. 

Sélectionnez l'onglet `Computed` et à partir de là, faites défiler vers le bas jusqu'à l'élément `position` ou dans la boîte de recherche `filter`, tapez `position`.

![Screenshot-2021-08-29-at-3.13.33-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-29-at-3.13.33-PM.png)


## Quelle est la position par défaut des éléments HTML en CSS ?

Par défaut, la propriété `position` pour tous les éléments HTML en CSS est définie sur `static`. Cela signifie que si vous ne spécifiez aucune autre valeur `position` ou si la propriété `position` n'est pas déclarée explicitement, elle sera `static`.

Visuellement, tous les éléments suivent l'ordre du code HTML, et de cette manière, le flux de document typique est créé.

Les éléments apparaissent les uns après les autres – directement en dessous les uns des autres, selon l'ordre du code HMTL.

Les éléments de bloc comme `<div>` sont empilés les uns après les autres comme ceci :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Positionnement CSS</title>
  </head>
  <body>
    <div class="parent">
      <div class="child one">Un</div>
      <div class="child two">Deux</div>
      <div class="child three">Trois</div>
      <div class="child four">Quatre</div>
    </div>
  </body>
</html>

```


```css
body {
  margin: 100px auto;
}

.parent {
  width: 500px;
  border: 1px solid red;
  margin: auto;
  text-align: center;
}

.child {
  border-radius: 10%;
  width: 100px;
  height: 100px;
  margin: 20px;
}

.one {
  background-color: powderblue;
}

.two {
  background-color: royalblue;
}

.three {
  background-color: sienna;
}

.four {
  background-color: slateblue;
}

```

![Screenshot-2021-08-30-at-2.00.39-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-2.00.39-PM.png)


La propriété `position` n'est pas déclarée dans le code ci-dessus et elle revient donc à la valeur par défaut `position: static`. Elle suit l'ordre du code HTML.

Ce qui vient en premier dans le HTML est montré en premier, et chaque élément suit le suivant, créant le flux de document comme je l'ai décrit ci-dessus.
 
Dans notre code ici, la div avec le texte "Un" est écrite en premier, donc elle est montrée en premier sur la page. Directement en dessous, la boîte avec le texte "Deux" est montrée, puisque elle vient ensuite dans le HTML, et ainsi de suite.

Ce positionnement par défaut ne laisse aucune place à la flexibilité ou au déplacement des éléments.

Et si vous vouliez déplacer le premier carré un peu vers la gauche de la page – comment feriez-vous cela ?

Il existe des propriétés de décalage pour le faire, comme `top`, `bottom`, `right` et `left`. 

Mais si vous essayez de les appliquer alors que le carré a cette position statique par défaut appliquée, ces propriétés ne feront rien et le carré ne bougera pas. 

Ces propriétés n'ont aucun effet sur `position: static`.

## Qu'est-ce que la position relative en CSS ?

`position: relative` fonctionne de la même manière que `position: static;`, mais elle vous permet de changer la position d'un élément.

Mais écrire cette règle CSS seule ne changera rien.

Pour modifier la position, vous devrez appliquer les propriétés `top`, `bottom`, `right` et `left` mentionnées précédemment et spécifier ainsi où et combien vous voulez déplacer l'élément.

Les décalages `top`, `bottom`, `right` et `left` poussent la balise *loin* de l'endroit où elle est spécifiée, fonctionnant à l'envers. 

`top` déplace en fait l'élément vers le bas du conteneur parent de l'élément. `bottom` pousse l'élément vers le haut du conteneur parent de l'élément, et ainsi de suite.

Maintenant, vous pouvez déplacer le premier carré vers la gauche en mettant à jour le CSS comme ceci :

```css
.one {
  background-color: powderblue;
  position: relative;
  right: 50px;
}

```


![Screenshot-2021-08-30-at-2.14.15-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-2.14.15-PM.png)

Ici, le carré s'est déplacé de `50px` vers la gauche par rapport à l'endroit où il aurait dû être par défaut.

`position: relative;` change la position de l'élément *par rapport* à l'élément parent et par rapport à lui-même et à l'endroit où il serait habituellement dans le flux de document régulier de la page. Cela signifie qu'il est relatif à sa position d'origine dans l'élément parent. 

Il déplace la balise en fonction de l'endroit où elle se trouve actuellement, par rapport à sa place habituelle et par rapport aux balises environnantes sans affecter leur mise en page.

En utilisant ces décalages et `position: relative`, vous pouvez également changer l'ordre dans lequel les éléments apparaissent sur la page. 

Le deuxième carré peut apparaître au-dessus du premier :

```css
.one {
  background-color: powderblue;
  position: relative;
  top: 150px;
}

.two {
  background-color: royalblue;
  position: relative;
  bottom: 120px;
}

```

![Screenshot-2021-08-30-at-2.18.16-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-2.18.16-PM.png)

Visuellement, l'ordre est maintenant inversé, tandis que le code HTML reste exactement le même.

Pour résumer, les éléments positionnés de manière relative peuvent se déplacer tout en restant dans le flux de document régulier. 

Ils n'affectent également pas la mise en page des éléments environnants.

## Qu'est-ce que la position absolute en CSS ?

Si vous mettez à jour la règle CSS pour le premier carré comme suit :

```css
.one {
  background-color: powderblue;
  position: absolute;
}

```

Vous obtiendrez ce résultat :

![Screenshot-2021-08-30-at-2.31.53-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-2.31.53-PM.png)

Ceci est un comportement inattendu. Le deuxième carré a complètement disparu.

Si vous ajoutez également des propriétés de décalage comme ceci :


```css
.one {
  background-color: powderblue;
  position: absolute;
  top: 50px;
  left: 0;
}

```

![Screenshot-2021-08-30-at-2.44.28-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-2.44.28-PM.png)

Eh bien, maintenant le carré a complètement abandonné son parent.

Les éléments positionnés de manière absolue sont complètement sortis du flux régulier de la page web. 

Ils ne sont pas positionnés en fonction de leur place habituelle dans le flux du document, mais en fonction de la position de leur ancêtre.

Dans l'exemple ci-dessus, le carré positionné de manière absolue est à l'intérieur d'un parent positionné de manière statique.

Cela signifie qu'il sera positionné par rapport à la page entière elle-même, ce qui signifie par rapport à l'élément `<html>` – la racine de la page.

Les coordonnées, `top: 50px;` et `left: 0;`, sont donc basées sur la page entière.

Si vous voulez que les coordonnées soient appliquées à son élément parent, vous devez positionner l'élément parent de manière relative en mettant à jour `.parent` tout en gardant `.one` identique :


```css
.parent {
  width: 500px;
  border: 1px solid red;
  margin: auto;
  text-align: center;
  position: relative;
}

.one {
  background-color: powderblue;
  position: absolute;
  top: 50px;
  left: 0;
}

```

Ce code crée le résultat suivant :

![Screenshot-2021-08-30-at-2.45.47-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-30-at-2.45.47-PM.png)
 
Le positionnement absolu sort les éléments du flux de document régulier tout en affectant la mise en page des autres éléments sur la page.

## Conclusion

Espérons que vous avez maintenant une meilleure compréhension de comment le positionnement relatif et absolu fonctionne.

Si vous êtes intéressé à en apprendre davantage sur HTML et CSS, vous pouvez sauvegarder et travailler à travers [cette playlist](https://www.youtube.com/playlist?list=PLWKjhJtqVAbnSe1qUNMG7AbPmjIG54u88) sur la chaîne YouTube de freeCodeCamp.

Elle inclut des vidéos pour vous aider à commencer à partir de zéro, et elle vous aidera à acquérir une bonne compréhension des fondamentaux.

freeCodeCamp propose également une certification gratuite et interactive basée sur des projets [Responsive Web Design Certification](https://www.freecodecamp.org/learn/responsive-web-design/), qui est un excellent point de départ pour votre parcours de développement web front-end.

Merci d'avoir lu et bon apprentissage !