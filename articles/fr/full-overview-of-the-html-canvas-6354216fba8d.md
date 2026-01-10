---
title: Un aperçu complet du HTML Canvas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-25T17:16:06.000Z'
originalURL: https://freecodecamp.org/news/full-overview-of-the-html-canvas-6354216fba8d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YrdvMQb-_K_uyRck
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un aperçu complet du HTML Canvas
seo_desc: 'By Shukant Pal

  A must read before doing anything with the canvas tag, even if you know it already.


  _Photo by [Unsplash](https://unsplash.com/@armand_khoury?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Armand Khoury ...'
---

Par Shukant Pal

#### Une lecture incontournable avant de faire quoi que ce soit avec la balise canvas, même si vous la connaissez déjà.

![Image](https://cdn-media-1.freecodecamp.org/images/S2wC31H-hVpDUXleTG7ACWegdqSKOPDNgXKA)
_Photo par [Unsplash](https://unsplash.com/@armand_khoury?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Armand Khoury</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

# Aperçu

L'élément HTML canvas est utilisé pour dessiner des graphiques "raster" sur une application web. L'API Canvas fournit deux contextes de dessin : 2D et 3D, et dans ce guide, nous allons parler de celui en 2D (que je désignerai par l'API Canvas pour simplifier).

Avant de commencer, je veux que vous sachiez un point très important. Canvas est une API de graphiques raster — vous manipulez des éléments au niveau des pixels. Cela signifie que le logiciel sous-jacent ne connaît pas le modèle que vous utilisez pour afficher votre contexte — il ne sait pas si vous dessinez un rectangle ou un cercle.

J'ai divisé l'API Canvas en plusieurs parties, pour que vous puissiez les assimiler une par une :

* **API de Path**
* **Styles de dessin**
* **Dégradés et motifs**
* **Manipulation directe des pixels & Images**
* **Transformations**
* **Régions de détection**
* **État et la méthode clip()**

# Installation

Pour démarrer votre tutoriel Canvas, créez un fichier HTML et un fichier JS lié à celui-ci.

```html
<!DOCTYPE html>
<html>
    <head><title>Démo Canvas</title></head>
    <body>
        <canvas id="canvas-demo" width="400" height="400">
             Cela sera affiché si votre navigateur ne
             supporte pas l'élément canvas. La balise de fermeture est
             nécessaire.
        </canvas>
        <script src="canvas-demo.js"></script>
    </body>
</html>
```

Dans votre fichier `canvas-demo.js`,

```js
// canvas-demo.js

const demoCanvas = document.getElementById('canvas-demo').getContext('2d');

window.onload = function() {// assurez-vous d'utiliser onload
    
/* Ajoutez du code ici au fur et à mesure !!! @nodocs
 */
    
}
```

# Paths

Les paths sont une collection de points dans la grille de pixels 2D du canvas. Ils sont dessinés à l'aide de cette API. Chaque forme dans un path que vous dessinez est appelée un "subpath" par la documentation W3C.

* `beginPath()` et `closePath()` : Toutes les formes que vous dessinez sont ajoutées au path actuel. Si vous appelez `stroke` ou `fill` plus tard, cela s'appliquera à toutes les formes que vous avez dessinées dans le path actuel. Pour éviter cela, vous divisez votre dessin en appelant `beginPath` et `closePath`.

```js
// Appeler cela n'est pas nécessaire, mais c'est une bonne pratique.
demoCanvas.beginPath();

/*
 * Code de dessin, copiez et collez chaque exemple (séparément) ici
 */

demoCanvas.closePath();// cela est requis si vous voulez dessiner
// dans un path séparé plus tard
```

* `moveTo(x,y)` : Cela signifie la construction d'une nouvelle forme qui commence au point (x, y).
* `lineTo(x,y)` : Dessine une ligne du dernier point de la forme actuelle au point passé. Si aucune forme n'a été créée (via `moveTo`), alors une nouvelle est créée en commençant à (x, y) (comme `moveTo`).
* `quadraticCurveTo(cpx1,cpy1,x,y)` et `bezierCurveTo(cpx1,cpy1,cpx2,cpy2,x,y)` : Dessine une courbe de Bézier quadratique/cubique en partant du dernier point de la forme, passant par les points de contrôle (`cpx1,cpy1` et `cpx2,cpy2`), et se terminant à `x,y`. Une courbe de Bézier est simplement une courbe "lisse" qui passe par des points de contrôle intermédiaires avec des points de fin donnés. Notez que la courbe n'a pas à passer exactement par les points de contrôle — elle peut être lissée.
* `arcTo(x1,y1,x2,y2,radius)` : C'est une méthode légèrement compliquée à utiliser. Supposons que le point actuel dans le path soit `x0,y0` — alors `arcTo` dessine un arc qui a deux tangentes reliant ces deux paires de points `(x1,y1) & (x0,y0)` et `(x1,y1) & (x2,y2)`. Le rayon de l'arc sera celui donné. Plus le rayon est grand, plus l'arc sera éloigné de `x1,y1` (voir l'exemple 1.2 pour plus de clarté visuelle). Si vous n'avez pas utilisé `moveTo` encore, alors `x0,y0` sera par défaut `0,0`.
* `arc(x,y,radius,startAngle,endAngle,counterclockwise)` : Cela relie le point actuel dans le path (par défaut `0,0`) au début de l'arc. Il dessine l'arc à partir du centre `x,y` de rayon `radius`, de `startAngle` à `endAngle`. (Note : Contrairement aux mathématiques sur papier, les angles sont décrits dans le sens horaire dans l'API Canvas) ; mais dans quatre conditions spéciales — `(x0,y0)` est égal à `(x1,y1)`, `(x1,y1)` est égal à `(x2,y2)`, `(x0,y0),(x1,y1),(x2,y2)` sont colinéaires, ou si `radius` est zéro, alors l'appel à `arc` sera équivalent à `lineTo(x1,y1)` et une ligne sera dessinée à la place.
* `rect(x,y,w,h)` : Dessine un rectangle avec le coin supérieur gauche `x,y` et de largeur `w` et de hauteur `h`.

**Exemple 1.1 :**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_1QaTuF2ersiZYKjtAm5AlQ.png)
_Démo Canvas 1_

Maintenant, nous devons essayer une démo — nous allons dessiner quelques lignes horizontales aléatoires puis un croquis d'un œil. Le résultat ressemblera à quelque chose sur la gauche. N'oubliez pas de parcourir le code et de le modifier.

```js
/* Dessiner des sous-paths horizontaux (formes) dans un path. */

// Dessiner un motif de lignes horizontales empilées verticalement
demoCanvas.moveTo(10, 10);// commencer à (10,10)
demoCanvas.lineTo(110, 10);
demoCanvas.moveTo(10, 20);// 10 pts en dessous
demoCanvas.lineTo(180, 20);
demoCanvas.moveTo(10, 30);
demoCanvas.lineTo(150, 30);
demoCanvas.moveTo(10, 40);
demoCanvas.lineTo(160, 40);
demoCanvas.moveTo(10, 50);
demoCanvas.lineTo(130, 50);

// essayez de supprimer ce moveTo, la courbe quadratique commencera alors
// à partir de (130, 50), à cause du lineTo.
demoCanvas.moveTo(10, 100);// la courbe quadratique commence ici
demoCanvas.quadraticCurveTo(110, 55, 210, 100);// courbe vers le haut
demoCanvas.moveTo(10, 100);// revenir ici, dessinons une en dessous
demoCanvas.quadraticCurveTo(110, 145, 210, 100);// courbe en dessous
// cela forme le contour de l'œil

demoCanvas.moveTo(132.5, 100);// supprimez ceci, une ligne horizontale sera
// dessinée de (210, 100) à (132.5, 100) car arc() relie le dernier
// point au début de l'arc.

demoCanvas.arc(110, 100, 22.5, 0, 2*Math.PI, false);// pupille (cercle)

/* Nous parlerons de cela bientôt */
demoCanvas.stroke();// dessine (en traçant nos formes dans le path)
```

**Exemple 1.2 :**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_KSUgriGZETCdodVNnOqC-g.png)
_Démo Canvas 2_

Dans l'exemple ci-dessous, je crée une courbe cubique (avec des lignes directrices visuelles), des appels `arcTo` au milieu à droite, et un pack-man avec `arc()` en bas à gauche. Les points de contrôle (dans la courbe cubique) sont les coins formés par les trois lignes directrices.

`(x1,y1)` pour `arcTo` est le coin formé par les deux tangentes.

```js
// commentez ce bloc si vous pouvez voir la courbe cubique
demoCanvas.moveTo(100, 100);
demoCanvas.lineTo(150, 10);
demoCanvas.moveTo(250, 100);
demoCanvas.lineTo(200, 190);
demoCanvas.moveTo(150, 10);
demoCanvas.lineTo(200, 190)

demoCanvas.moveTo(100, 100);
demoCanvas.bezierCurveTo(150, 10, 200, 190, 250, 100);

// arcTo() est trop compliqué à utiliser
// demoCanvas.stroke(); demoCanvas.closePath(); demoCanvas.beginPath();
demoCanvas.moveTo(200, 200);// commentez la ligne ci-dessus (et commentez cette ligne),
// alors la tangente de l'arc viendra de (0,0)!! Essayez-le.

demoCanvas.arcTo(100, 300, 300, 300, 100);
demoCanvas.moveTo(200, 200);
demoCanvas.arcTo(100, 300, 300, 300, 50);

demoCanvas.moveTo(100, 300);
demoCanvas.lineTo(300, 300);
demoCanvas.moveTo(100, 300);
demoCanvas.lineTo(200, 200);

demoCanvas.moveTo(50, 300);
// packman
demoCanvas.arc(50, 300, 35, Math.PI/6, 11*Math.PI/6, false);
demoCanvas.lineTo(50, 300);

demoCanvas.stroke();
```

# Styles de dessin

Jusqu'à présent, nous avons dessiné des paths simples avec des lignes fines. Les styles de dessin nous aideront à améliorer nos dessins.

Notez que vous ne pouvez pas appliquer deux styles différents sur le même path. Par exemple, si vous voulez dessiner une ligne rouge et une ligne bleue — vous devrez créer un nouveau path pour dessiner la bleue. Si vous ne créez pas de nouveau path, alors en appelant `stroke` la 2ème fois après avoir défini votre couleur de style d'affichage sur bleu, les deux lignes seront colorées en bleu. Par conséquent, les styles sont appliqués à tous les sous-paths, qu'ils aient été tracés ou non.

Quelques propriétés de l'objet de contexte 2D `demoCanvas` sont définies à cet effet :

* `lineWidth` : L'épaisseur des lignes dessinées. Par défaut, cela vaut 1 ; par conséquent, les deux exemples ci-dessus ont utilisé un contour d'une épaisseur de 1 pixel.
* `lineCap` : C'est le cap appliqué aux extrémités des sous-paths (formes). C'est une chaîne et peut avoir trois valeurs valides : "butt", "round", "square" (voir l'exemple 1.3 pour plus de clarté visuelle). "butt" terminera les lignes sans cap — résultant en des extrémités rigides et orthogonales comme des rectangles fins. "round" ajoute un demi-cercle aux extrémités pour donner des extrémités lisses. "square" ajoute un carré à l'extrémité, mais cela ressemble à "butt". "round" et "square" ajoutent un peu de longueur supplémentaire à chaque sous-path.
* `lineJoin` : Cela décide comment deux lignes qui se chevauchent sont jointes. Par exemple, si vous voulez créer une flèche vers la droite (>), alors vous pouvez changer la façon dont le coin est formé avec cette propriété. Cela a trois valeurs valides : "round", "bevel" et "miter". Vérifiez l'exemple 1.4 pour voir comment ils changent les coins. (La valeur par défaut est "miter"). "round" formera des coins circulaires, tandis que "bevel" créera des coins rigides à trois côtés, et "miter" formera une arête nette.
* `miterLimit` : Lorsque `lineJoin="miter"`, cela décide la distance maximale entre le coin intérieur et extérieur de la ligne. Voir l'exemple 1.4(b) pour plus de clarté visuelle. Si la limite de mitre est trop élevée, alors les flèches nettes peuvent avoir une grande zone commune entre les deux lignes. Si la limite de mitre est dépassée, alors l'affichage revient à une jointure en biseau.

**Exemple 1.3 & 1.4 :**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_ApS2swKjILWD6TNAeBFxHA.png)
_Démo Canvas 3—1.butt, 2.round, 3.square_

Dans l'exemple 1.3 à gauche, vous pouvez voir comment les lignes avec des extrémités rondes et carrées sont plus longues que le capuchon par défaut. (NOTE : Plus la ligne est épaisse, plus l'augmentation de longueur est grande)

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_w5YqtkQmqAEqPst8_HgWvg.png)
_Démo Canvas 4(a) — 1. lineJoin="round", 2. lineJoin="bevel"_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_q4eVrvXbbgvOWiMaql3dOg.png)
_Démo Canvas 4(b)—1.miterLength=10, 2.miterLength=5. Les deux utilisent la jointure de ligne par défaut — "miter". Les lignes utilisées sont identiques dans les deux — haut et bas. La limite de mitre est la distance maximale entre le coin intérieur et le coin extérieur. En la diminuant, la limite de mitre est dépassée, ce qui fait que la jointure en biseau s'applique._

Dans l'exemple 1.4(a), vous pouvez voir comment les jointures rondes et en biseau fonctionnent. Les lignes créées sont identiques dans les parties supérieure et inférieure. Seules les propriétés `lineJoin` sont différentes.

Dans l'exemple 4.1(b), vous pouvez voir comment une jointure en mitre fonctionne, et ce qui se passe si la longueur de la mitre est dépassée.

Des propriétés de style d'affichage supplémentaires sont définies :

* `font` : Cette chaîne définit comment vous voulez styliser le texte. Par exemple, `demoCanvas.font="10px Times New Roman"` est une valeur de police valide.
* `textAlign` : Les valeurs valides sont — "start", "end", "left", "right", et "center". La valeur par défaut est "start".
* `textBaseline` : Les valeurs valides sont — "top", "hanging", "middle", "alphabetic", "ideographic", "bottom". La valeur par défaut est "alphabetic".

# Méthodes de dessin réelles

Dans les exemples jusqu'à présent, vous avez peut-être remarqué que j'ai utilisé `demoCanvas.stroke()` avant de fermer chaque path. La méthode stroke fait le dessin réel en partie dans ces exemples.

* `stroke` : Cette méthode dessine le contour autour de chaque sous-path (formes) selon le `lineWidth` et les propriétés connexes.
* `fill` : Cette méthode remplit l'intérieur de la forme tracée par le path. Si le path n'est pas fermé, il le fermera automatiquement en reliant le dernier point au premier point.

```js
demoCanvas.moveTo(10,10);
demoCanvas.lineTo(50, 50);
demoCanvas.lineTo(10, 50);
demoCanvas.fill();
```

Le code ci-dessus ne ferme pas le triangle (10,10),(50,50),(10,50) mais l'appel à `fill()` le remplit comme prévu.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_lA_qJE0Gaf9SBzENOFJRpQ.png)
_Triangle rempli_

* `clearRect(x,y,w,h)` : Efface les pixels dans le rectangle formé avec les paramètres donnés.
* `strokeRect(x,y,w,h)` : Équivalent à appeler `rect` puis `stroke`. Il n'ajoute pas le rectangle au path actuel — donc, vous pouvez changer le style plus tard et appeler `stroke` sans affecter le rectangle formé.
* `fillRect(x,y,w,h)` : Équivalent à appeler `rect` puis `fill`. Cela n'ajoute pas non plus le rectangle au path actuel.
* `strokeText(text,x,y,maxWidth)` et `fillText(text,x,y,maxWidth)` : Écrit le texte à (x,y) selon la propriété `strokeStyle` / `fillStyle`. `maxWidth` est optionnel et définit la longueur maximale en pixels que vous voulez que le texte occupe. Si le texte est plus long, il est mis à l'échelle avec une police plus petite. `measureText("text").width` peut être utilisé pour trouver la largeur d'affichage d'un morceau de texte, basé sur la `font` actuelle.

NOTE : `fillStyle` et `strokeStyle` sont les propriétés qui peuvent être définies sur n'importe quelle chaîne de couleur CSS pour définir les couleurs de remplissage et de contour.

# Dégradés et motifs

Par défaut, le contexte 2D fournit des dégradés linéaires et radiaux. Les méthodes `createLinearGradient` et `createRadialGradient` retournent des objets `CanvasGradient`, qui peuvent ensuite être modifiés comme nous le voulons.

* `createLinearGradient(x0,y0,x1,y1)` : Construit un dégradé linéaire qui s'étend sur la ligne `x0,y0` à `x1,y1`.
* `createRadialGradient(x0,y0,r0,x1,y1,r1)` : Construit un dégradé radial qui s'étend dans le cône (de cercles) avec le haut (cercle intérieur) de rayon `r0` et le bas (cercle extérieur) de rayon `r1`. La première couleur aurait un rayon de `r0`.

Le `CanvasGradient` a une méthode : `addColorStop(offset,color)`. Le dégradé commence à 0 et se termine à 1. La couleur à la position de `offset` sera définie en utilisant cette méthode. Par exemple, `addColorStop(.5, "green")` rendra la couleur du milieu verte. Les couleurs entre deux arrêts adjacents seront interpolées (mélangées).

**Exemple 1.6 :**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_qZPegs7HKnMgKWy14NVIgw.png)
_Démo Canvas 6—1. Ligne de dégradé linéaire, 2. Arc rempli de dégradé radial_

Dans l'exemple à gauche, vous pouvez voir comment les dégradés linéaires et radiaux fonctionnent.

```js
var linearGrad = demoCanvas.createLinearGradient(5,5,100,5);
linearGrad.addColorStop(0, "blue");
linearGrad.addColorStop(.5, "green");
linearGrad.addColorStop(1, "red");
demoCanvas.strokeStyle=linearGrad;
demoCanvas.lineWidth=50;
demoCanvas.moveTo(5,5);
demoCanvas.lineTo(100,5);
demoCanvas.stroke();// changez strokeStyle(l10) en fillStyle(l10)
// et stroke() en fill(). Ensuite, changez lineTo(100,5) en rect(5,5,95,50).
// Les résultats devraient être presque identiques.

demoCanvas.closePath();
demoCanvas.beginPath();
var radialGrad = demoCanvas.createRadialGradient(50,50,10,50,50,40);
radialGrad.addColorStop(0, "blue");
radialGrad.addColorStop(.5, "green");
radialGrad.addColorStop(1, "red");
demoCanvas.fillStyle=radialGrad;
demoCanvas.arc(50,50,30,0,2*Math.PI,false);
demoCanvas.fill();
```

Vous pourriez vous demander ce qui se passe si `x0,y0` et `x1,y1` donnés au dégradé linéaire/radial ne sont pas égaux à la ligne/arc que nous créons ? Voir l'exemple 1.7

**Exemple 1.7**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_KI8G7zaPbWa4rF80YyLhuQ.png)
_Démo Canvas — 1. Déplacé la ligne de 100px horizontalement, 2. Déplacé l'arc de (10,10) vers le bas à droite._

```js
var linearGrad = demoCanvas.createLinearGradient(5,5,100,5);
linearGrad.addColorStop(0, "blue");
linearGrad.addColorStop(.5, "green");
linearGrad.addColorStop(1, "red");
demoCanvas.strokeStyle=linearGrad;
demoCanvas.lineWidth=50;
demoCanvas.moveTo(50,5);
demoCanvas.lineTo(155,5);
demoCanvas.stroke();// changez strokeStyle(l10) en fillStyle(l10)
// et stroke() en fill(). Ensuite, changez lineTo(100,5) en rect(5,5,95,50).
// Les résultats devraient être presque identiques.

demoCanvas.closePath();
demoCanvas.beginPath();
var radialGrad = demoCanvas.createRadialGradient(50,50,10,50,50,40);
radialGrad.addColorStop(0, "blue");
radialGrad.addColorStop(.5, "green");
radialGrad.addColorStop(1, "red");
demoCanvas.fillStyle=radialGrad;
demoCanvas.arc(60,60,30,0,2*Math.PI,false);
demoCanvas.fill();
```

---

# Manipulation directe des pixels & Images

L'objet `ImageData` peut être utilisé pour manipuler des pixels individuels. Il a trois propriétés :

* `width` : La largeur des données d'image en pixels d'affichage de l'appareil.
* `height` : La hauteur des données d'image en pixels d'affichage de l'appareil.
* `data` : Il s'agit d'un `Uint8ClampedArray` (doc MDN [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray?source=post_page---------------------------)) qui contient les données de pixels individuelles dans une série d'octets (R,G,B,A) pour le pixel le plus haut à gauche jusqu'au pixel en bas à droite. Ainsi, la valeur rouge du _n_ième pixel serait à `data[y*width+x]`, le vert serait à `data[y*width+x+1]`, le bleu serait à `data[y*width+x+2]`, et l'alpha serait à `data[y*width+x+3]`.

NOTE : Une valeur RGBA peut être utilisée pour représenter une couleur — où R,G,B sont les quantités de rouge, vert et bleu et A est l'opacité (valeur alpha). Dans le Canvas, ces éléments peuvent avoir n'importe quelle valeur entière dans [0, 255].

Vous pouvez obtenir un objet `ImageData` avec les méthodes suivantes dans l'API Canvas :

* `createImageData(sw,sh)` : Cela crée un objet `ImageData` de largeur et de hauteur `sw` et `sh`, définis en pixels CSS. Tous les pixels seront initialisés à noir transparent (hex R,G,B=0, et aussi A=0).

> _Les pixels CSS peuvent correspondre à un nombre différent de pixels réels de l'appareil exposés par l'objet lui-même_

* `createImageData(data)` : Copie les données d'image données et retourne la copie.
* `getImageData(sx,sy,sw,sh)` : Retourne une copie des pixels du canvas dans le rectangle formé par `sx,sy,sw,sh` dans un objet `ImageData`. Les pixels en dehors du canvas sont définis à noir transparent.
* `putImageData(imagedata,dx,dy,dirtyX,dirtyY,dirtyWidth,dirtyHeight)` : (Les quatre derniers arguments 'dirty' sont optionnels). Copie les valeurs de pixels dans `imagedata` dans le rectangle du canvas à `dx,dy`. Si vous fournissez les quatre derniers arguments, il ne copiera que les pixels sales dans les données d'image (le rectangle formé à `dirtyX,dirtyY` de dimensions `dirtyWidth*dirtyHeight`). Ne pas passer les quatre derniers arguments est la même chose que d'appeler `putImageData(imagedata,dx,dy,0,0,imagedata.width,imagedata.height)`.

> _Pour toutes les valeurs entières de x et y où dirtyX ≤ x < dirtyX+dirtyWidth et dirtyY ≤ y < dirtyY+dirtyHeight, copiez les quatre canaux du pixel avec la coordonnée (x, y) dans la structure de données `imagedata` vers le pixel avec la coordonnée (dx+x, dy+y) dans les données de pixels sous-jacentes du canvas._

**Exemple 1.8 :**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_gNpUUBTbqqDEJzt7xTHTjw.png)
_Démo Canvas 1.8(a) — Pixels aléatoires dans un canvas 400x400_

J'ai rempli tout le canvas 400x400 avec des couleurs aléatoires (totalement opaques) en utilisant les méthodes `getImageData/putImageData`.

Notez que l'utilisation de `beginPath/closePath` n'est pas nécessaire pour utiliser l'API ImageData — car vous n'utilisez pas l'API Canvas pour former des formes/courbes.

```js
/* remplacez cette ligne par demoCanvas.createImageData(390,390) à la place. */
var rectData = demoCanvas.getImageData(10, 10, 390, 390);

for (var y=0; y<390; y++) {
  for (var x=0; x<390; x++) {
    const offset = 4*(y*390+x);// 4* car chaque pixel est 4 octets
    rectData.data[offset] = Math.floor(Math.random() * 256);// rouge
    rectData.data[offset+1] = Math.floor(Math.random() * 256);// vert
    rectData.data[offset+2] = Math.floor(Math.random() * 256);// bleu
    rectData.data[offset+3] = 255;// alpha, complètement opaque
  }
}

demoCanvas.putImageData(rectData, 10, 10);

/* beginPath/closePath ne sont pas requis pour ce code */
```

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_u3xTtkvlksp0f4aHnhMykw.png)
_Démo Canvas 1.8(b) — x commence avec une valeur aléatoire entre 1 et y._

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_vwl-Mtzaai1sAOr-UWnN9Q.png)
_Démo Canvas 1.8(c) — x se termine à une valeur aléatoire supérieure à sa valeur initiale._

**Images** peuvent être dessinées directement sur le canvas. La méthode `drawImage` peut être utilisée de trois manières différentes pour ce faire. Elle nécessite une `CanvasImageSource` comme source de pixels.

> _Une `CanvasImageSource` peut être l'une des suivantes — HTMLImageElement, HTMLCanvasElement, HTMLVideoElement. Pour copier dans le canvas, vous pouvez utiliser un `<img style="display:none;" src="..." />`. Vous pourriez également copier un canvas existant ou la capture d'écran d'une vidéo !!!_

* `drawImage(image,dx,dy)` : Copie la source d'image dans le canvas à (_dx,dy_). L'image entière est copiée.
* `drawImage(image,dx,dy,dw,dh)` : Copie la source d'image dans le rectangle du canvas à (_dx,dy_) de taille (_dw,dh_). Elle sera redimensionnée vers le bas ou vers le haut si nécessaire.
* `drawImage(image,sx,sy,sw,sh,dx,dy,dw,dh)` : Copie le rectangle dans la source d'image `sx,sy,sw,sh` dans le rectangle du canvas `dx,dy,dw,dh` et redimensionne vers le haut ou vers le bas si nécessaire. Cependant, si le rectangle `sx,sy,sw,sh` a des parties en dehors de la source réelle — alors le rectangle source est rogné pour inclure les parties internes et le rectangle de destination est rogné dans la même proportion ; cependant, vous ne devriez pas passer de rectangle hors limites — gardez cela simple, stupide.

**Exemple 1.9 :**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_2C02zm5g3JkamcSWbaiQlg.png)
_Exemple de copie d'image_

```js
var image = document.getElementById('game-img');
demoCanvas.drawImage(image, 50, 50, 200, 200, 100, 100, 200, 200);

/* beginPath/closePath ne sont pas requis pour ce code */
```

NOTE : Ajoutez ceci à votre HTML —

```html
<img id="game-img" src="/path/to/your/image.ext" style="display:none" />
```

# Transformations

Maintenant, nous arrivons aux parties passionnantes de l'API Canvas !!!

Le Canvas utilise une _matrice de transformation_ pour transformer les coordonnées d'entrée (_x, y_) en coordonnées affichées (_x, y_). Notez que les pixels dessinés avant la transformation ne sont pas transformés — ils sont intacts. Seuls les éléments dessinés après l'application de la transformation seront modifiés.

Il existe trois méthodes de transformation intégrées :

* `scale(xf,yf)` : Cette méthode met à l'échelle l'entrée par `xf` dans la direction horizontale et `yf` dans la direction verticale. Si vous voulez agrandir une image d'un facteur de `m`, alors passez `xf=yf=m`. Pour étirer/compresser une image horizontalement par `m`, `xf=m,yf=1`. Pour étirer/compresser une image verticalement par `m`, `xf=1,yf=m`.
* `rotate(angle)` : Fait tourner l'entrée d'un angle de `angle` dans le sens horaire, en radians.
* `translate(dx,dy)` : Décale l'entrée de `dx,dy`.

**Exemple 2.0 :**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_1uej9lcnNCVEX4cnASBG0g.png)
_Dessin d'une image transformée par-dessus l'image originale. Échelle=2,2 ; Rotation=30deg ; Translation=10,10_

```js
var image = document.getElementById('game-img');
demoCanvas.drawImage(image, 0, 0, 400, 400);
demoCanvas.rotate(Math.PI / 6);
demoCanvas.scale(2, 2);
demoCanvas.translate(10, 10);
demoCanvas.drawImage(image, 0, 0, 400, 400);
```

> _Dans l'exemple 2.0, remarquez comment l'image originale est intacte. Seule la deuxième image (superposition) est transformée par trois méthodes — rotation, mise à l'échelle, transformation._

Pour annuler toutes les transformations :

```js
demoCanvas.setTransform(1, 0, 0, 0, 0, 1);
// définit la transformation à la matrice identité
```

NOTE :

* Changer l'ordre de transformation peut affecter le résultat final.
* Pour les utilisateurs avancés, vous pouvez regarder les méthodes `transform` et `setTransform`. Cela vous permettra de définir la matrice de transformation 3D directement.
* `getImageData` et `putImageData` ne sont pas affectés par la transformation. Cela signifie que si vous dessinez un rectangle noir en utilisant `putImageData`, il ne sera pas transformé (roté/mis à l'échelle/translaté).
* Comme changer la transformation ne fonctionne que pour les dessins réalisés après son application, vous ne pouvez pas mettre à l'échelle/rotater/translater le canvas existant directement (ni `getImageData` puis `putImageData` ne fonctionne). Vous devrez peut-être créer un autre canvas caché de la même taille — puis copier les données d'image dans le 2ème canvas, puis utiliser `drawImage` sur le 2ème canvas.
* Vérifiez cet exemple : [https://canvasdemo2d.github.io/](https://canvasdemo2d.github.io/?source=post_page---------------------------) (source : [https://github.com/canvasdemo2d/canvasdemo2d.github.io](https://github.com/canvasdemo2d/canvasdemo2d.github.io?source=post_page---------------------------)). Déplacez votre curseur sur le canvas et voyez ce qu'il fait. Cela ne fonctionnera pas sur les téléphones mobiles, malheureusement. L'effet en cascade est dû au fait que je translate le canvas par rapport à la souris en utilisant `drawImage`. `drawImage` écrit ensuite sur le même canvas à partir duquel il lit, ce qui provoque le motif répétitif !

---

# Régions de détection

Au moment de la rédaction (mars 2019), _le support des régions de détection est expérimental_ dans Chrome et sur Firefox. Les navigateurs mobiles ne le supportent pas du tout. Par conséquent, je vais vous expliquer "ce que" les régions de détection pourraient être utilisées.

Les régions de détection sont utilisées pour capturer les événements de pointeur sur le canvas et savoir "où" l'utilisateur a cliqué. Par exemple, vous pourriez avoir deux rectangles A & B — lorsque l'utilisateur clique sur A, vous voulez effectuer l'action $A et lorsque l'utilisateur clique sur B, vous voulez effectuer l'action $B. Parcourons tout le processus !

Une région de détection est liée à ces trois choses :

* **Path** : Le path actuel lorsque la région de détection a été créée (par exemple, un rectangle). Tous les événements de pointeur à l'intérieur du path sont acheminés vers cette région de détection.
* **Id** : Un identifiant unique pour identifier la région de détection par le gestionnaire d'événements.
* **Control** : Un élément DOM alternatif (par exemple, `HTMLButtonElement`) qui reçoit les événements de pointeur à la place.

NOTE : Le path est automatiquement fourni par le canvas lors de l'ajout d'une nouvelle région de détection. Un seul — id ou control — est nécessaire pour former une région de détection.

Les méthodes pour manipuler la liste des régions de détection d'un canvas sont :

* `addHitRegion(options)` : Prend un objet `HitRegionOptions` et forme une région de détection enfermée par le path actuel. L'argument `options` doit être une propriété de chaîne `id` ou une propriété `HTMLElement` `control`.
* `removeHitRegion(id)` : Supprime la région de détection avec l'id `id` afin qu'elle ne reçoive plus d'événements de pointeur.
* `clearHitRegions()` : Supprime toutes les régions de détection.

```js
demoCanvas.fillStyle = 'red';
demoCanvas.rect(10,10,60,60);
demoCanvas.fill();// premier rectangle
demoCanvas.addHitRegion({ id: 'btn1' });

demoCanvas.fillStyle = 'blue';
demoCanvas.rect(10,110,60,60);
demoCanvas.fill();
demoCanvas.addHitRegion({ id: 'btn2' });

document.getElementById('demo-canvas').onpointerdown = function(evt) {
// demoCanvas est le contexte 2d, pas l'HTMLCanvasElement
    
  console.log('Bonjour id : ' + evt.region);// region est l'id de la région de détection
}

// Ce code pourrait ne pas fonctionner en raison du fait que cela est une
// fonctionnalité non supportée (nouvelle) de HTML5.
```

NOTE : Les régions de détection ne sont pas supportées — mais cela ne signifie pas que vous devez les utiliser pour capturer les événements de pointeur. Vous pourriez créer votre "propre liste de régions de détection" et des représentations des limites des régions (car vous ne pouvez pas obtenir le path actuel à partir du canvas, dommage). Dans la méthode `document.getElementById('demo-canvas').onpointerdown`, obtenez les propriétés `clientX,clientY` actuelles et parcourez la liste des régions de détection. En fonction de la région de détection qui contient le point, vous pouvez effectuer l'action prévue.

---

# États et la méthode clip()

La sauvegarde d'état est une commodité fournie par la spécification W3C. Vous pouvez sauvegarder l'état actuel d'un canvas et le restaurer plus tard.

Vous pourriez également construire un tel système (partiellement) en écrivant votre propre modèle JavaScript. Mais vous devriez sauvegarder beaucoup de choses : matrice de transformation, liste des régions de détection, propriétés de style, et ainsi de suite. De plus, vous ne pouvez pas inverser directement la zone de rognage (nous aborderons la méthode `clip` dans un certain temps).

NOTE : Les méthodes `save` / `restore` ne sauvegardent et ne restaurent pas le dessin/pixels réel. Elles ne sauvegardent que d'autres propriétés.

Par conséquent, je recommande fortement d'utiliser les méthodes `save` et `restore` pour aller et venir au lieu d'effacer des choses vous-même ou de créer votre propre mécanisme de sauvegarde d'état.

L'objet `CanvasRendering2DContext` a une pile d'états associée. La méthode `save` poussera l'état actuel du canvas sur cette pile, tandis que la méthode `restore` extraira le dernier état de la pile.

**La région de rognage**

La région de rognage est une région spécifique dans laquelle tous les dessins doivent être faits. Évidemment, par défaut, la région de rognage est le rectangle qui est tout le canvas. Mais vous pouvez vouloir dessiner dans une région spécifique au lieu de tout. Par exemple, vous pouvez vouloir dessiner la moitié inférieure d'une étoile formée par plusieurs méthodes `lineTo`.

Donc, par exemple, disons que vous savez comment dessiner une étoile dans le canvas. Elle touche tous les côtés du canvas. Mais maintenant, vous voulez afficher uniquement la moitié inférieure de l'étoile. Dans ce scénario, vous feriez :

1. Sauvegardez l'état du canvas
2. Rognez la région de la moitié inférieure
3. Dessinez votre étoile (comme si c'était sur tout le canvas)
4. Restaurez l'état du canvas

Pour rogner une région, vous devez appeler la méthode `clip()` qui fait ce qui suit :

> _La méthode `clip()` doit créer une nouvelle région de rognage en calculant l'intersection de la région de rognage actuelle et de la zone décrite par le path, en utilisant la règle du nombre d'enroulement non nul. Les sous-paths ouverts doivent être implicitement fermés lors du calcul de la région de rognage, sans affecter les sous-paths réels. La nouvelle région de rognage remplace la région de rognage actuelle._  
>   
> _Lorsque le contexte est initialisé, la région de rognage doit être définie sur le rectangle avec le coin supérieur gauche à (0,0) et la largeur et la hauteur de l'espace de coordonnées._  
>   
> _— Documentation W3C pour le contexte 2D Canvas_

```js
demoCanvas.save();
demoCanvas.rect(0, 200, 400, 200);// sous-path rectangle de la moitié inférieure
demoCanvas.clip();
/* méthode de dessin d'étoile */
demoCanvas.restore();
```

C'est tout pour l'instant. J'écrirai un article sur les animations avec le canvas et comment écrire une interface personnalisée complètement sur le canvas.

Pour aller plus loin :

* [Comment utiliser Firebase pour construire des jeux multijoueurs Android](https://www.freecodecamp.org/news/match-making-with-firebase-hashnode-de9161e2b6a7)
* [Comment synchroniser votre application de jeu sur plusieurs appareils Android](https://www.freecodecamp.org/news/how-to-synchronize-your-game-app-across-multiple-devices-88794d4c95a9)
* [Dépendances circulaires en JavaScript](https://medium.com/@sukantk3.4/circular-dependencies-in-javascript-34183fc2720?source=post_page---------------------------)

_Shukant Pal est le créateur du noyau Silcos. Il est un apprenant passionné et pratique maintenant le développement avancé d'applications web. Il a une expérience pratique avec React et son écosystème._

---

_Toutes les citations sont tirées des documents W3C pour le contexte 2D Canvas._

Salut, je suis Shukant Pal. Je développe beaucoup d'applications web pendant mon temps libre. Suivez-moi sur [les réseaux sociaux](https://twitter.com/ShukantP).