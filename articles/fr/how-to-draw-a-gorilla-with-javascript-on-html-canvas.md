---
title: Comment dessiner avec JavaScript sur un élément Canvas HTML – Exemple Gorille
subtitle: ''
author: Hunor Márton Borbély
co_authors: []
series: null
date: '2024-02-15T16:30:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-draw-a-gorilla-with-javascript-on-html-canvas
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Thumbnail.png
tags:
- name: canvas
  slug: canvas
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment dessiner avec JavaScript sur un élément Canvas HTML – Exemple Gorille
seo_desc: 'Drawing from code can be fun for many reasons. You can generate art that
  follows a certain logic. You can create animations by moving only parts of an image.
  And you can even build up a whole game as I covered in this tutorial.

  In my last article, we...'
---

Dessiner à partir de code peut être amusant pour de nombreuses raisons. Vous pouvez générer de l'art qui suit une certaine logique. Vous pouvez créer des animations en ne déplaçant que des parties d'une image. Et vous pouvez même construire un jeu entier comme je l'ai couvert dans [ce tutoriel](https://www.freecodecamp.org/news/gorillas-game-in-javascript/).

Dans mon dernier article, nous nous sommes concentrés sur les [bases du dessin](https://www.freecodecamp.org/news/drawing-on-a-canvas-element-with-javascript/). Maintenant, voyons un exemple concret et explorons comment utiliser JavaScript pour dessiner un Gorille.

Vous n'avez pas besoin de prérequis pour ce tutoriel. Même si vous avez manqué les bases, vous pouvez commencer tout de suite. Nous allons simplement avoir un peu de HTML simple et un fichier JavaScript que vous pouvez exécuter directement dans le navigateur.

À la fin, vous saurez comment dessiner un gorille avec JS.

## Table des matières :

1. [Comment définir un Canvas](#heading-comment-definir-un-canvas)
2. [Comment inverser le système de coordonnées](#heading-comment-inverser-le-systeme-de-coordonnees)
3. [Comment dessiner le corps du Gorille](#heading-comment-dessiner-le-corps-du-gorille)
4. [Comment dessiner les jambes du gorille](#heading-comment-dessiner-les-jambes-du-gorille)
5. [Comment dessiner les bras du Gorille](#heading-comment-dessiner-les-bras-du-gorille)
6. [Comment dessiner le visage du Gorille](#heading-comment-dessiner-le-visage-du-gorille)
7. [Prochaines étapes](#heading-prochaines-etapes)

## Comment définir un Canvas

Pour dessiner notre gorille, définissons d'abord un fichier HTML simple avec un élément Canvas. Ensuite, nous verrons comment y accéder depuis JavaScript.

Dans le fichier HTML, dans l'en-tête, nous ajouterons notre fichier JavaScript. Notez que j'utilise le mot-clé `defer` pour m'assurer que le script ne s'exécute qu'une fois le reste du document analysé.

Dans le corps, nous ajouterons un élément `canvas`. Nous définissons sa taille à 500 x 500 et définissons un ID.

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <title>Gorille</title>
    <script src="index.js" defer></script>
  </head>
  <body>
    <canvas id="gorilla" width="500" height="500"></canvas>
  </body>
</html>
```

Ensuite, créons un fichier JavaScript. Dans ce fichier, nous récupérerons d'abord l'élément canvas par son ID. Ensuite, nous obtiendrons le contexte de rendu de l'élément canvas. Il s'agit d'une API intégrée avec de nombreuses méthodes et propriétés que nous pouvons utiliser pour dessiner sur le canvas.

```js
// L'élément canvas et son contexte de dessin 
const canvas = document.getElementById("gorilla"); 
const ctx = canvas.getContext("2d");

. . .
```

Avant de commencer à dessiner, facilitons-nous la vie en inversant le système de coordonnées.

## Comment inverser le système de coordonnées

Lorsque nous utilisons canvas, nous avons un système de coordonnées avec l'origine dans le coin supérieur gauche du canvas qui s'étend vers la droite et vers le bas. Cela est aligné avec le fonctionnement général des sites web. Les éléments vont de gauche à droite et de haut en bas.

C'est le comportement par défaut, mais nous pouvons le changer.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-with-and-without-transforming-and-scaling.jpg)
_Le gorille avec et sans transformation et mise à l'échelle du système de coordonnées_

Dans notre cas, il est plus pratique d'aller de bas en haut. Ainsi, le gorille peut se tenir en bas, et nous n'avons pas à déterminer où se trouve le bas du canvas.

Nous pouvons utiliser la méthode `translate` pour déplacer l'ensemble du système de coordonnées vers le bas au milieu du canvas. Nous déplacerons le système de coordonnées vers le bas le long de l'axe Y de la taille du canvas, et vers la droite le long de l'axe X de la moitié de la taille du canvas.

Une fois cela fait, la coordonnée Y augmente toujours vers le bas. Nous pouvons l'inverser en utilisant la méthode `scale`. Définir un nombre négatif pour la direction verticale inversera l'ensemble du système de coordonnées.

```js
// L'élément canvas et son contexte de dessin 
const canvas = document.getElementById("gorilla"); 
const ctx = canvas.getContext("2d");

ctx.translate(250, 500);
ctx.scale(1, -1);

. . .
```

Nous devons faire cela avant de peindre quoi que ce soit sur le canvas car les méthodes `translate` et `scale` ne déplacent pas réellement ce qui est déjà sur le canvas. Mais tout ce que nous peindrons après ces appels de méthodes sera peint selon ce nouveau système de coordonnées.

## Comment dessiner le Gorille

Maintenant, voyons comment dessiner le gorille. Nous allons décomposer cela en plusieurs étapes. D'abord, nous dessinerons le corps, puis les jambes, les bras et enfin le visage du gorille.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/drawing-gorilla-steps.jpg)
_Nous dessinerons le gorille en plusieurs étapes_

### Comment dessiner le corps du gorille

Nous dessinerons le corps du gorille sous forme de chemin. Les chemins commencent par la méthode `beginPath` et se terminent par l'appel de la méthode `fill` ou `stroke` – ou les deux.

Entre les deux, nous construirons le chemin en appelant des méthodes de construction de chemin. Dans ce cas, pour construire le corps du gorille, nous utiliserons la méthode `moveTo` et une série de méthodes `lineTo`.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-12-at-23.53.57.png)
_Le corps du gorille. L'image montre le chemin que nous remplissons._

Nous définirons le style de remplissage en noir, puis nous commencerons un chemin. Nous nous déplacerons vers une position de départ, puis nous dessinerons des lignes droites pour dessiner la silhouette du gorille. Une fois terminé, nous remplirons la forme avec la méthode `fill`.

```js
. . .

ctx.fillStyle = "black";

// Dessiner le corps du Gorille
ctx.beginPath();
ctx.moveTo(-68, 72);
ctx.lineTo(-80, 176);

ctx.lineTo(-44, 308);
ctx.lineTo(0, 336);
ctx.lineTo(+44, 308);

ctx.lineTo(+80, 176);
ctx.lineTo(+68, 72);
ctx.fill();

. . .
```

Si vous vous demandez comment j'ai obtenu ces coordonnées, j'ai en fait commencé par un croquis initial avec un stylo et du papier. J'ai essayé d'estimer les coordonnées, je les ai essayées avec du code, puis je les ai ajustées jusqu'à ce qu'elles commencent à prendre la bonne forme. Bien sûr, vous pouvez avoir d'autres méthodes également.

### Comment dessiner les jambes du gorille

Nous dessinerons les jambes de la même manière. Nous pourrions même continuer le même chemin que nous avons utilisé auparavant, mais il pourrait être plus facile de voir ce qui se passe si nous décomposons cela en chemins séparés.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-12-at-23.09.59.png)
_Dessiner les jambes comme deux chemins séparés_

```js
. . .

// Dessiner la jambe gauche
ctx.beginPath();
ctx.moveTo(0, 72);
ctx.lineTo(-28, 0);
ctx.lineTo(-80, 0);
ctx.lineTo(-68, 72);
ctx.fill();

// Dessiner la jambe droite
ctx.beginPath();
ctx.moveTo(0, 72);
ctx.lineTo(+28, 0);
ctx.lineTo(+80, 0);
ctx.lineTo(+68, 72);
ctx.fill();

. . .
```

La couleur de remplissage dans ce cas sera également noire. Pourquoi ? Parce que c'est ce que nous avons défini pour la propriété `fillStyle`, la dernière fois que nous avons défini sa valeur. Chaque chemin qui suit cette instruction utilisera cette couleur jusqu'à ce que nous changions sa valeur.

### Comment dessiner les bras du gorille

Alors que le corps et les jambes sont des parties relativement simples du gorille, les bras sont un peu plus compliqués. Nous les dessinerons sous forme de courbe.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-12-at-23.12.03.png)
_Dessiner les bras comme une courbe_

Commençons par le bras gauche. La partie principale de cela n'est en fait que deux lignes de code. Nous utiliserons la méthode `moveTo` pour nous déplacer vers l'épaule du gorille, puis à partir de là, nous dessinerons le bras comme une courbe quadratique avec la méthode `quadraticCurveTo`.

Une courbe quadratique est une courbe simple avec un point de contrôle. Alors que la courbe va du point de départ (que nous définirons avec `moveTo`), la courbe se courbe vers ce point de contrôle (définie comme les deux premiers arguments de la méthode `quadraticCurveTo`) alors qu'elle atteint sa position finale (définie comme les deux derniers arguments).

```js
. . .

ctx.strokeStyle = "black";
ctx.lineWidth = 70;

// Dessiner le bras gauche
ctx.beginPath();
ctx.moveTo(-56, 200);
ctx.quadraticCurveTo(-176, 180, -112, 48);
ctx.stroke();

// Dessiner le bras droit
ctx.beginPath();
ctx.moveTo(+56, 200);
ctx.quadraticCurveTo(+176, 180, +112, 48);
ctx.stroke();

. . .
```

Nous dessinerons les mains comme des traits. Au lieu de terminer le chemin avec la méthode `fill`, nous utiliserons la méthode `stroke`.

Nous définirons également le style différemment. Au lieu d'utiliser la propriété `fillStyle`, ici nous définirons la couleur avec `strokeStyle` et donnerons de l'épaisseur aux bras avec la propriété `lineWidth`.

Dessiner le bras droit est la même chose, sauf que les coordonnées horizontales sont inversées. Les nombres négatifs ont maintenant un signe positif.

En conséquence, nos gorilles devraient commencer à prendre forme. Ils n'ont toujours pas de visage, mais nous avons maintenant toute la silhouette.

### Comment dessiner le visage du gorille

Le visage du gorille se compose de plusieurs parties différentes. D'abord, nous dessinerons le masque facial avec trois cercles.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-facial-mask.jpg)
_Nous dessinons le masque facial comme trois cercles_

Malheureusement, nous n'avons pas de méthode simple de remplissage de cercle, comme nous en avons dans le cas des rectangles. Nous devons dessiner un `arc` à la place.

Une méthode `arc` peut être appelée dans le cadre d'un chemin. Nous commencerons chaque cercle avec la méthode `beginPath` et terminerons avec la méthode `fill`.

```js
. . .

ctx.fillStyle = "lightgray";

// Dessiner le masque facial
ctx.beginPath();
ctx.arc(0, 252, 36, 0, 2 * Math.PI);
ctx.fill();

ctx.beginPath();
ctx.arc(-14, 280, 16, 0, 2 * Math.PI);
ctx.fill();

ctx.beginPath();
ctx.arc(+14, 280, 16, 0, 2 * Math.PI);
ctx.fill();

. . .
```

La méthode `arc` a beaucoup de propriétés. Cela peut sembler un peu effrayant, mais nous n'avons besoin de nous concentrer que sur les trois premières lors du dessin de cercles :

* Les deux premiers arguments sont `x` et `y`, les coordonnées du centre de l'arc.
* Le troisième argument est le `rayon`.
* Ensuite, les deux derniers arguments sont l'`angleDeDébut` et l'`angleDeFin` de l'arc en radians. Parce qu'ici nous voulons avoir un cercle complet et non un arc, nous commencerons à 0 et terminerons à un cercle complet. Un cercle complet en radians est deux fois Pi.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-12-at-23.17.08.png)

Si ces deux dernières propriétés sont déroutantes, ne vous en souciez pas. Ce qui est important, c'est que lorsque nous dessinons des cercles, ils sont toujours `0` et `2 * Math.Pi`.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/gorilla-final-steps.jpg)
_Nous dessinons les yeux, les narines et la bouche_

Ensuite, nous dessinons les yeux du gorille comme deux autres cercles. Ici, les coordonnées du centre des cercles sont les mêmes que les grands cercles gris autour d'eux. Seuls leur rayon et leur couleur de remplissage sont différents.

```js
. . .

ctx.fillStyle = "black";

// Dessiner l'œil gauche
ctx.beginPath();
ctx.arc(-14, 280, 6, 0, 2 * Math.PI);
ctx.fill();

// Dessiner l'œil droit
ctx.beginPath();
ctx.arc(+14, 280, 6, 0, 2 * Math.PI);
ctx.fill();

. . .
```

Ensuite, pour le nez, nous dessinerons deux courtes lignes comme narines. Elles font partie du même chemin, et nous appellerons la méthode `moveTo` entre les deux pour passer d'un côté à l'autre. Avant d'appeler `stroke` à la fin de ce chemin, nous mettrons à jour la propriété `lineWidth`.

```js
. . .

ctx.lineWidth = 6;

// Dessiner les narines
ctx.beginPath();
ctx.moveTo(-14, 266);
ctx.lineTo(-6, 260);

ctx.moveTo(14, 266);
ctx.lineTo(+6, 260);
ctx.stroke();

. . .
```

Et enfin, nous ajouterons également un chemin pour la bouche. Cela pourrait faire partie du même chemin que le nez, car il a la même largeur de ligne et la même couleur, mais il pourrait être plus clair de les avoir séparés.

```js
. . .

// Dessiner la bouche
ctx.beginPath();
ctx.moveTo(-20, 230);
ctx.quadraticCurveTo(0, 245, 20, 230);
ctx.stroke();
```

Dessiner une autre courbe quadratique. Cela est similaire à celle que nous avons utilisée pour les bras. Le point de départ et le point final de cette courbe sont au même niveau, mais le point de contrôle est un peu plus haut de sorte que le milieu de la bouche est plus haut que les deux côtés.

## Prochaines étapes

Maintenant que nous avons un gorille de base, que pouvons-nous faire avec ? Nous pouvons construire un jeu entier autour de lui. Dans ce [tutoriel de jeu JavaScript](https://www.freecodecamp.org/news/gorillas-game-in-javascript/), nous reconstruisons le jeu classique de 1991, Gorillas.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-01-19-at-23.49.34.png)
_Capture d'écran du tutoriel de jeu JavaScript_

Pour une plongée en profondeur, lisez le [tutoriel complet](https://www.freecodecamp.org/news/gorillas-game-in-javascript/) où nous construisons un jeu complet avec du JavaScript simple. Dans ce tutoriel, nous couvrons non seulement comment dessiner les gorilles et la ligne d'horizon de la ville, mais aussi comment implémenter toute la logique du jeu. De la gestion des événements, en passant par la boucle d'animation, jusqu'à la détection des impacts.

Pour encore plus, vous pouvez également regarder le [tutoriel étendu sur YouTube](https://www.youtube.com/watch?v=2q5EufbUEQk). Dans la version YouTube, nous couvrons également comment rendre les bâtiments destructibles, comment animer la main du gorille pour suivre le mouvement de glisser lors de la visée, avoir des graphismes plus beaux, et nous ajoutons une logique d'IA, afin que vous puissiez jouer contre l'ordinateur.

Consultez-le pour en savoir plus :

[Contenu intégré](https://www.youtube.com/embed/2q5EufbUEQk?feature=oembed)

Vous pouvez vous abonner à ma chaîne pour plus de tutoriels sur le développement de jeux JavaScript :

%[https://www.youtube.com/channel/UCxhgW0Q5XLvIoXHAfQXg9oQ]