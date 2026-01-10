---
title: Comprendre l'interpolation linéaire dans l'animation UI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-14T07:06:02.000Z'
originalURL: https://freecodecamp.org/news/understanding-linear-interpolation-in-ui-animations-74701eb9957c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DFXftmJxkHo5P_E94ElwMQ.png
tags:
- name: animation
  slug: animation
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: Comprendre l'interpolation linéaire dans l'animation UI
seo_desc: 'By Nash Vail

  In traditional (hand-drawn) animation, a senior or key artist draws keyframes that
  define the motion.

  An assistant, generally an intern or a junior artist, then draws the necessary inbetweens
  for the scene. The job of the assistant, also...'
---

Par Nash Vail

Dans l'animation traditionnelle (dessins à la main), un artiste senior ou clé dessine des images clés qui définissent le mouvement.

Un assistant, généralement un stagiaire ou un artiste junior, dessine ensuite les images intermédiaires nécessaires pour la scène. Le travail de l'assistant, également appelé interpolateur, est de rendre les transitions entre les poses clés fluides et naturelles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GI0WbHlZ7uBpOY0Xvkl5Cw.png)

Les images intermédiaires sont nécessaires car les animations sans elles semblent saccadées. Malheureusement, dessiner des images intermédiaires est plus ou moins un travail ingrat. Mais nous sommes au vingt-et-unième siècle, et nous avons des ordinateurs qui peuvent gérer ce type de tâche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xnLjqe-1m6stF9pLUeTXkA.gif)
_Animation saccadée_

Vous souvenez-vous de ce que les enseignants vous disaient à l'école primaire sur le fait que les ordinateurs sont stupides ? Les ordinateurs doivent être informés de la séquence exacte d'étapes à suivre pour effectuer une action. Aujourd'hui, nous allons examiner une telle séquence d'étapes, ou algorithme, qui aide l'ordinateur à dessiner les images intermédiaires nécessaires pour créer une animation fluide.

J'utiliserai HTML5 canvas et JavaScript pour illustrer l'algorithme. Cependant, vous pourrez lire et comprendre l'article même si vous n'êtes pas familier avec eux.

### Intention

Notre objectif est simple, animer une balle du point A `(startX, startY)` au point B `(endX, endY)`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W-Fo7GodNwVwsV_9z33OzQ.png)

Si cette scène était passée à un studio qui fait de l'animation traditionnelle, l'artiste senior dessinerait les poses clés suivantes...

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Kq3EdW2sv_qUPy6skk6qQ.png)

...et passerait ensuite le tableau de dessin à un artiste junior pour dessiner les images intermédiaires comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*99zCw2qgEd2O32tSl_ZU4g.png)

Pour notre situation, il n'y a pas de studio d'animation ni d'artistes juniors. Tout ce que nous avons, c'est un objectif, un ordinateur et la capacité d'écrire du code.

### Approche

Le code HTML est simple, nous n'avons besoin que d'une seule ligne.

```
<canvas id="canvas"></canvas>
```

Cette partie du code JavaScript (montrée ci-dessous) récupère simplement `<canvas/>` depuis le Document Object Model (DOM), [obtient le contexte](https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D), et définit les propriétés de largeur et de hauteur du canevas pour correspondre à la fenêtre d'affichage.

```
const canvas = document.getElementById('canvas'),  context = canvas.getContext('2d'),  width = canvas.width = window.innerWidth,  height = canvas.height = window.innerHeight;
```

La fonction ci-dessous dessine un cercle solide vert de rayon `radius` aux coordonnées `x` et `y`.

```
function drawBall(x, y, radius) {  context.beginPath();   context.fillStyle = '#66DA79';  context.arc(x, y, radius, 0, 2 * Math.PI, false);  context.fill();}
```

Tout le code ci-dessus est du code standard pour configurer notre animation, voici la partie intéressante.

```
// Point Alet startX = 50, startY = 50;
```

```
// Point Blet endX = 420, endY = 380;
```

```
let x = startX, y = startY;
```

```
update();function update() {  context.clearRect(0, 0, width, height);  drawBall(x, y, 30);  requestAnimationFrame(update);}
```

Tout d'abord, remarquez que la fonction `update` est appelée juste au-dessus de sa déclaration. Ensuite, remarquez `requestAnimationFrame(update)` qui appelle `update` de manière répétée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zw30luTk6Y2yS2rheUF3yw.gif)
_Une animation de flipbook_

L'animation de flipbook est une bonne analogie pour le type de programme que nous écrivons. Tout comme le fait de feuilleter rapidement un flipbook crée l'illusion du mouvement, le fait d'appeler de manière répétée la fonction `update` crée l'illusion du mouvement pour notre balle verte.

Une chose à noter à propos du code ci-dessus est que « update » est juste un nom. La fonction aurait pu être nommée autrement. Certains programmeurs préfèrent les noms `nextFrame`, `loop`, `draw`, ou `flip` parce que la fonction est appelée de manière répétée. L'important est ce que fait la fonction.

À chaque appel ultérieur de `update`, nous nous attendons à ce que la fonction dessine une image légèrement différente sur le canevas par rapport à la précédente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gr1EShaIgQcYKCxfp0TzSQ.png)

Notre implémentation actuelle de `update` dessine la balle à la même position exacte à chaque appel `drawBall(x, y, 30)`. Il n'y a pas d'animation, mais changeons cela. Ci-dessous se trouve un [pen](http://codepen.io/nashvail/pen/XRNprQ) qui contient le code que nous avons écrit jusqu'à présent, vous pouvez l'ouvrir et suivre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KgTqUC2mKagPNnxxsuWGpQ.png)

À chaque itération de `update`, allons-y et incrémentons la valeur de `x` et `y` et voyons le type d'animation que cela crée.

```
function update() {  context.clearRect(0, 0, width, height);  drawBall(x, y, 30);  x++; y++;  requestAnimationFrame(update);}
```

Chaque itération déplace la balle vers l'avant dans les directions x et y, et les appels répétés de `update` résultent en l'animation comme montré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Iyd6S-yGVdvF5G1TH5hWDA.gif)

Voici le problème cependant, notre intention était de déplacer la balle d'une position de départ à une position de fin. Mais nous ne faisons absolument rien pour arrêter la balle à une position de fin. Corrigons cela.

Une solution évidente est de n'incrémenter les coordonnées que lorsqu'elles sont plus petites que les valeurs `endX` et `endY`. De cette façon, une fois que la balle dépasse `endX, endY`, ses coordonnées cesseront de se mettre à jour et la balle s'arrêtera.

```
function update() {  context.clearRect(0, 0, width, height);  drawBall(x, y, 30);   if(x <= endX && y <= endY) {    x++;    y++;  }   requestAnimationFrame(update);}
```

Il y a une erreur dans cette approche cependant. La voyez-vous ?

Le problème ici est que vous ne pouvez pas faire atteindre à la balle n'importe quelle coordonnée de fin que vous voulez simplement en incrémentant les valeurs `x` et `y` de `1`. Par exemple, considérons les coordonnées de fin `(500, 500)`, bien sûr si vous commencez à `(0, 0)` et ajoutez `1` à `x` et `y`, ils finiront par atteindre `(500, 500)`. Mais que se passe-t-il si je choisis `(432, 373)` comme coordonnées de fin ?

En utilisant l'approche ci-dessus, vous ne pouvez atteindre que les points situés sur une ligne droite à 45 degrés de l'axe horizontal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HSmtd5gcIYYnAVmU5t3L0w.png)

Maintenant, vous pouvez utiliser la trigonométrie et des mathématiques avancées pour calculer les quantités précises dont `x` et `y` doivent être incrémentés pour atteindre n'importe quelle coordonnée que vous voulez. Mais vous n'avez pas besoin de faire cela lorsque vous avez l'interpolation linéaire.

### Approche avec interpolation linéaire

Voici à quoi ressemble la fonction d'interpolation linéaire, également connue sous le nom de `lerp`.

```
function lerp(min, max, fraction) {  return (max — min) * fraction + min;}
```

Pour comprendre ce que fait l'interpolation linéaire, considérons un curseur avec une valeur `min` à l'extrémité gauche et une valeur `max` à l'extrémité droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G5vGdPXQhec7hnOmBSJZkA.png)
_min = 0, max = 100_

La prochaine chose dont nous avons besoin est de choisir `fraction`. `lerp` prend `fraction` et le convertit en une valeur entre `min` et `max`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DFXftmJxkHo5P_E94ElwMQ.png)
_min = 0, max = 100, fraction = 0.5_

Lorsque je mets `0.5` dans la formule `lerp`, sans surprise, cela se traduit par 50. C'est exactement le point médian entre `0` (min) et `100` (max).

De même, si nous choisissons une autre valeur pour `fraction`, disons `0.85`...

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytUp7zQTmzwiRmPAIEMyIQ.png)
_min = 0, max = 100, fraction = 85_

Et si nous laissons `fraction = 0`, `lerp` produira `0` (min) et avec `fraction = 1`, `lerp` produira `100` (max).

J'ai choisi 0 et 100 comme `min` et `max` pour garder cet exemple simple, mais `lerp` fonctionnera pour n'importe quel choix arbitraire de `min` et `max`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ik-7ASOSmqFmKNwytsA8qg.png)
_min = 18, max = 37, fraction = 0.73_

Pour les valeurs de `fraction` entre `0` et `1`, `lerp` vous permet d'_interpoler_ entre `min` et `max`. Ou en d'autres termes, de parcourir entre les valeurs `min` et `max`, où choisir `0` pour `fraction` vous place à `min`, choisir `1` vous place à `max` et pour toute autre valeur entre `0` et `1`, vous place n'importe où entre `min` et `max`. Vous pouvez également voir `min` et `max` comme des poses clés, comme dans l'animation traditionnelle, et `lerp` produit des images intermédiaires ;-).

D'accord, mais que se passe-t-il si quelqu'un donne une valeur en dehors des limites de `0` et `1` comme `fraction` à `lerp` ? Vous voyez, la formule pour `lerp` est extrêmement simple avec les opérations mathématiques les plus basiques. Il n'y a pas de truc ou de mauvaises valeurs ici, imaginez simplement étendre le curseur dans les deux directions. Quelle que soit la valeur de `fraction` fournie, `lerp` _produira_ un résultat logique. Nous ne devrions pas trop réfléchir aux mauvaises valeurs ici, ce à quoi nous devrions réfléchir, c'est comment tout cela se rapporte à l'animation de la balle.

Si vous suivez, allez-y et changez la fonction `update` pour correspondre au code suivant. N'oubliez pas non plus d'ajouter la fonction `lerp` que nous avons définie au début de cette section.

```
function update() {  context.clearRect(0, 0, width, height);  drawBall(x, y, 30);  x = lerp(x, endX, 0.1);  y = lerp(y, endY, 0.1);  requestAnimationFrame(update);}
```

Voici un [pen](http://codepen.io/nashvail/pen/wdjpVZ) de ce à quoi ressemble notre programme maintenant. Essayez de cliquer autour :)

Fluide, n'est-ce pas ? Voici comment `lerp` aide à améliorer l'animation.

Dans le code, remarquez les variables `x` et `y` — qui sont initialement définies sur `startX` et `startY` — marquent la position actuelle de la balle dans n'importe quelle image. De plus, mon choix de `0.1` comme `fraction` est arbitraire, vous pouvez choisir n'importe quelle valeur fractionnaire que vous voulez. Gardez à l'esprit que votre choix de `fraction` affecte la vitesse de l'animation.

Dans chaque image, `x` et `endX` sont pris comme `min` et `max` et interpolés avec `0.1` comme `fraction` pour obtenir une nouvelle valeur pour `x`. De même, `y` et `endY` sont utilisés comme `min` et `max` pour obtenir une nouvelle valeur pour `y` en utilisant `0.1` comme fraction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vUfujdUFficArMFoNqEN7A.png)

La balle est ensuite dessinée à la coordonnée `(x, y)` nouvellement calculée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W1x88vpgSUD7BidIeHG5Eg.png)

Ces étapes sont répétées jusqu'à ce que `x` devienne `endX` et `y` devienne `endY`, auquel cas `min = max`. Lorsque `min` et `max` deviennent égaux, `lerp` renvoie la même valeur exacte (min/max) pour toute image ultérieure, arrêtant ainsi l'animation.

Et c'est ainsi que vous utilisez l'interpolation linéaire pour animer en douceur une balle.

Cet article court couvre beaucoup de choses. Nous avons commencé par définir des termes comme les poses clés et les images intermédiaires. Ensuite, nous avons essayé une approche triviale pour dessiner des images intermédiaires et remarqué ses limitations. Enfin, avec l'interpolation linéaire, nous avons pu atteindre notre objectif.

J'espère que toutes les mathématiques vous ont paru claires. N'hésitez pas à jouer encore plus avec l'interpolation linéaire. Cet article a été inspiré par le [post de Rachel Smith](https://www.freecodecamp.org/news/understanding-linear-interpolation-in-ui-animations-74701eb9957c/undefined) sur [CodePen](https://codepen.io/rachsmith/post/animation-tip-lerp). Le post de Rachel contient de nombreux autres exemples, assurez-vous de le consulter.

Vous cherchez plus ? Je publie régulièrement sur mon [blog à nashvail.me](https://nashvail.me). À bientôt, bonne journée !

![Image](https://cdn-media-1.freecodecamp.org/images/1*JZ2patu496gPkJOYXhb9MA.png)