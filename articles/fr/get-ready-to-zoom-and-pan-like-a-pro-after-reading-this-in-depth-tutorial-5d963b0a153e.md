---
title: "D3 zoom\n\x14\n le manuel manquant"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T16:06:13.000Z'
originalURL: https://freecodecamp.org/news/get-ready-to-zoom-and-pan-like-a-pro-after-reading-this-in-depth-tutorial-5d963b0a153e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xQbd3tLH8julKZ9G7MCuQQ.png
tags:
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: "D3 zoom\n\x14\n le manuel manquant"
seo_desc: 'By lars verspohl

  How to zoom and pan in your data visualizations using SVG and Canvas


  _‘[Aged Pixel](https://fineartamerica.com/featured/telescope-zoom-lens-patent-from-1999-blueprint-aged-pixel.html"
  rel="noopener" target="_blank" title="">Telescop...'
---

Par Lars Verspohl

#### Comment zoomer et faire défiler dans vos visualisations de données en utilisant SVG et Canvas

![Image](https://cdn-media-1.freecodecamp.org/images/FbgmVzCpVFIDImXj81x7KBtODb3rsYBvQG2R)
_[Aged Pixel](https://fineartamerica.com/featured/telescope-zoom-lens-patent-from-1999-blueprint-aged-pixel.html" rel="noopener" target="_blank" title="">Brevet de lentille de zoom télescopique de 1999  Blueprint</a> par <a href="https://www.agedpixel.com/" rel="noopener" target="_blank" title=")_

Le meilleur paragraphe d'introduction pour un article sur le zoom D3 a déjà été écrit, et il est ainsi libellé :

![Image](https://cdn-media-1.freecodecamp.org/images/-To1xq3bsoojKnRm9-CWqhCkDlUv8quitXhI)
_Peter Kerpedijec sur Empty Pipes (voir [sources](#28f2" rel="noopener" target="_blank" title=") ci-dessous)_

C'est bien. En quatre phrases, il vous dit précisément ce qu'est le zoom et ce qu'il fait, et  probablement plus important encore  il dissipe vos craintes concernant le zoom.

Alors, tout a-t-il déjà été dit ? Eh bien, non. Il est toujours bon d'avoir de nombreuses perspectives différentes, surtout avec des événements qui déplacent votre précieuse visualisation partout et la redimensionnent selon le bon vouloir de l'utilisateur.

Il y a quelque temps, j'ai travaillé sur une visualisation assez complexe avec de nombreux éléments mobiles et une longue liste d'interactions, y compris le zoom et le défilement, au cœur initialement sombre. La visualisation statique elle-même était déjà relativement complexe, mais ajouter le zoom et le défilement était un peu comme attacher le château Lego de 4 par 6 pieds de mon fils à un buffle d'eau en fuite.

Le problème conceptuel ici est que le zoom et le défilement interfèrent si fondamentalement avec notre travail. Ils semblent contrôler une grande partie de notre visualisation artisanale, qui n'est rarement une seule chose entière, mais une concoction soignée de positions, d'échelles et d'axes. Cela peut être déroutant au mieux et intimidant au pire.

Ainsi, après que mes mouvements de zoom et de défilement ont gagné en confiance et ont été testés dans quelques autres projets, le moment semblait mûr pour les écrire. Peut-être est-il trop tard et vous avez tous résolu cela il y a des années, mais même alors, il pourrait être utile d'avoir une autre perspective.

Notre voyage comportera trois parties :

1. Une recette synchrone pour le zoom et le défilement
2. Construire une visualisation
3. Implémenter le zoom et le défilement en SVG et en Canvas

En bonus, nous ajouterons un zoom programmatique et rendrons notre visualisation joli.

Maintenant, vous pourriez regarder cette barre de défilement là-bas, en pensant que vous allez manquer le souper en lisant tout cela. C'est détaillé pour une raison, mais je vais vous faciliter la navigation et la sélection en pointant les sections que vous pouvez sauter sans manquer de choses cruciales. Ainsi, vous pouvez rendre ce voyage aussi court ou complet que vous le souhaitez et en tirer quelque chose dans les deux cas.

### Une recette simple de zoom et de défilement

Cette première partie est l'épine dorsale de ce post. C'est un manuel court  rien de plus qu'une série de cinq points simples que vous pouvez suivre tout en construisant vos événements de zoom et de défilement. Ce manuel vous donnera une séquence de type ligne de vie sur la façon d'intégrer le zoom et le défilement dans votre application. Le monde asynchrone et noué de la programmation est souvent aidé par une série d'étapes synchrones et simples à suivre.

#### S'accorder sur une terminologie

Avant de nous tirer le long de la ligne, définissons d'abord une terminologie utile :

* Une **transformation de zoom** est un objet produit et maintenu par D3. C'est votre possession la plus précieuse dans le contexte du zoom et du défilement, et il contient trois valeurs : la translation _x_ et _y_ ainsi que le facteur d'échelle représenté par _k_. Nous verrons bientôt quand et où il est produit et modifié. Voici à quoi il ressemble dans son état initial :

![Image](https://cdn-media-1.freecodecamp.org/images/BRG67a68-J4Xqu1zza2hApHFJ0OquvWtQZJ8)

* Il dit : _L'utilisateur n'a pas encore zoomé, ou fait défiler la visualisation. Par conséquent, le facteur d'échelle de zoom est 1 et la translation x et y est 0._
* Le **comportement de zoom** est le système d'événements qui suit et transmet les valeurs de transformation. Un écouteur consomme (prend note) des actions de l'utilisateur. Une fois activé, il enverra un objet d'événement avec des informations sur cet événement à une fonction de gestion. Vous écrirez ce gestionnaire et utiliserez les informations de l'objet d'événement. La pièce d'information la plus importante que votre gestionnaire de zoom recevra est la transformation ci-dessus à chaque activité de zoom. Quelles que soient les actions que nous voulons effectuer avec les valeurs de transformation, nous les effectuerons dans le gestionnaire de zoom. Cela peut sembler beaucoup, mais sous sa forme la plus simple, vous configurez le comportement de zoom comme suit :

```
var zoom = d3.zoom().on(zoom, zoomed);
```

* La **base de zoom** est l'élément parent auquel le zoom est attaché ou _enregistré_, comme ils disent. Il fait deux choses : 1) C'est la surface qui reçoit tous les mouvements et gestes de l'utilisateur, et 2) il contient l'objet de transformation (le _x_, le _y,_ et le facteur d'échelle _k_).
* Les **cibles de zoom** sont tous les éléments que nous voulons déplacer. Si vous voulez zoomer et dézoomer sur un cercle, alors ce cercle serait votre cible de zoom.

De plus, nous pourrions vouloir distinguer entre deux types de zoom. Ils deviendront beaucoup plus clairs lorsque nous passerons à nos exemples, mais il sera utile de les définir d'abord au niveau supérieur :

* **Zoom géométrique** (ou _zoom graphique_) signifie que les éléments sont simplement mis à l'échelle sans aucune différenciation. Toutes leurs propriétés seront mises à l'échelle. Pensez à cela comme à déplacer ou à mettre à l'échelle le système de coordonnées des éléments respectifs. Tout ce qui s'y trouve sera mis à l'échelle et déplacé de manière indiscriminée. Le zoom géométrique est le plus proche de notre expérience de la vie réelle. Lorsque nous marchons vers une maison, chaque aspect de la maison semble plus grand à chaque pas. De même, si nous mettons à l'échelle un axe, toutes les parties de celui-ci deviendraient plus grandes ou plus petites  les lignes, le chemin de domaine, les étiquettes. Par exemple, une étiquette d'axe de 14px mise à l'échelle par un facteur d'échelle de 2 apparaîtrait _14  2 = 28px_ grande.
* **Zoom sémantique** (ou _zoom non géométrique_) signifie que nous contrôlons chaque propriété d'un seul élément pendant le zoom. Si nous avons un axe, par exemple, avec des étiquettes de taille 14px et que nous zoomons sémantiquement sur l'axe, nous pourrions commander aux étiquettes de conserver leur taille originale pour chaque facteur d'échelle. Les lignes pourraient devenir plus grandes et plus fines et l'axe serait repositionné selon le zoom, mais notre étiquette resterait à 14px de large.

Nous n'aborderons pas cela dans ce qui suit, mais un zoom sémantique bona fide peut aller plus loin. Il nous permet non seulement de contrôler les propriétés de l'élément, mais aussi la représentation de notre élément en fonction du niveau de zoom. Google Maps, par exemple, montre des pays lorsqu'on est zoomé, des états ou des districts administratifs à un zoom moyen et des villes plus petites lorsqu'on est zoomé.

#### Zoom et défilement en 5 étapes

![Image](https://cdn-media-1.freecodecamp.org/images/gze0YROBUH-XYSY6mz4ng2-QrRl9q4TNkb7X)
_[Aged Pixel](https://fineartamerica.com/featured/1895-firemans-ladder-patent-blueprint-aged-pixel.html" rel="noopener" target="_blank" title="">Brevet d'échelle de pompier de 1895  Blueprint</a> par <a href="https://www.agedpixel.com/" rel="noopener" target="_blank" title=")_

Nous sommes bien équipés pour cela maintenant. Voici notre zoom et défilement en cinq étapes simples :

#### 1. Construisez d'abord votre visualisation statique

Pour zoomer dans une visualisation, vous aurez besoin d'une visualisation.

#### 2. Identifiez votre base de zoom et vos cibles de zoom

Prenez une feuille de papier, nommez un élément qui écoute (la _base de zoom_), et notez une liste d'éléments qui doivent bouger (les _cibles de zoom_).

* Choisissez d'abord votre élément **base de zoom**. Déterminez quel élément DOM vous voulez utiliser pour votre base de zoom. Vous pouvez attacher le zoom à un `svg`, `g`, `rect` ou tout autre élément auquel votre souris a accès. Notez ici que les éléments `g` ne peuvent enregistrer des événements que là où ils ont des enfants avec un remplissage. Donc, si vous avez un grand élément `g` avec un cercle de rayon 1, vos gestes de zoom ne fonctionneront que sur ce petit cercle. Il est souvent préférable de configurer un rectangle SVG dédié (`rect`) avec un remplissage mais une opacité de 0 et `pointer-events` défini sur `all` pour enregistrer l'écouteur de zoom. Vous devrez peut-être désactiver les événements de pointeur des éléments ascendants.
* Identifiez vos éléments **cibles de zoom** et notez-les. N'oubliez pas, les cibles de zoom sont les éléments que vous voulez déplacer. Faites une liste de tous les éléments cibles de zoom.
* Pour chaque cible, identifiez si vous voulez utiliser un **zoom géométrique** ou **sémantique**.
* Notez-le. Voici un exemple de tableau que vous pourriez obtenir :

![Image](https://cdn-media-1.freecodecamp.org/images/hpR5CKaU3QXrBRrNVvNygZ3C2z6EA7kMyU5T)

#### 3. Configurez le comportement de zoom

Maintenant, vous voulez configurer le comportement qui fera écouter l'écouteur.

* Créez le comportement de zoom avec au moins :

```
var zoom = d3.zoom().on(zoom, zoomed);
```

* Consultez la [référence de l'API D3 pour d3.zoom()](https://github.com/d3/d3-zoom) pour les méthodes d'aide comme `scaleExtent` et `translateExtent`.
* Appelez le comportement de zoom sur votre élément de base comme suit :

```
zoomBaseElement.call(zoom)
```

_Notez que vous n'avez pas à appeler votre base de zoom_ `zoomBaseElement` _bien sûr._

#### 4. Écrivez le gestionnaire

C'est là que le zoom et le défilement se produiront. La possession la plus précieuse du gestionnaire sera l'objet `transform` mettant à jour _x_, _y,_ et _k_ en continu lorsque l'utilisateur fait défiler ou glisse. Vous appliquerez ces valeurs à vos cibles de zoom.

* La première chose que vous voulez faire est de capturer l'objet `transform` passé dans le gestionnaire par l'écouteur à chaque interaction utilisateur (roue ou souris) :

```
var transform = d3.event.transform;
```

* Maintenant que vous avez vos paramètres de zoom et de défilement (_tx_, _ty_, _k_), vous pouvez faire ce que vous voulez avec...
* Si vous voulez seulement administrer un **zoom géométrique**, vous appelez simplement :

```
zoomTargetElement  .attr(transform,         translate( + transform.x + ,  + transform.y + )          scale( + transform.k + ));
```

ou plus simplement :

```
zoomTargetElement.attr(transform, transform.toString());
```

qui est exactement la même chose. Cela suppose que vous voulez appliquer toutes les valeurs de transformation. Vous pouvez également vous concentrer uniquement sur _tx_, _ty_ ou l'échelle _k_ bien sûr.

* Si vous voulez un **zoom sémantique**, vous devez redimensionner.
* En supposant que toutes vos valeurs de données sont passées par une échelle pour être traduites de l'espace de données à l'espace écran, cette traduction change lors du zoom. Si votre point de données x = 10 a été traduit en espace pixel 50 avant le zoom, le zoom le déplacera à un point différent.
* Si vous traduisez x par 5 et mettez à l'échelle par 2, la nouvelle position sera :

> x2 = x1  k + tx   
> x2 = 50  2 + 5 = 105

* Heureusement, vous n'avez pas à (ni ne devriez) produire ces calculs vous-même, mais vous pouvez redimensionner votre échelle à chaque zoom et l'appliquer aux propriétés cibles que vous voulez changer. Cela inclut les axes ou les cercles ou les `rects` ou toute autre forme et composant cible que vous avez.
* Avec une échelle appelée `xScale`, vous pouvez utiliser la fonction sugar `.rescaleX()` et l'appliquer comme suit :

```
var updatedScale = transform.rescaleX(xScale);
```

* Maintenant, vous pouvez utiliser `updatedScale` dans votre fonction zoomée pour tous les éléments que vous voulez mettre à jour. Par exemple, un axe :

```
xAxis.scale(updatedScale); gAxis.call(xAxis);
```

* ou un ensemble de positions x de cercle :

```
circles.attr(cx. function(d) { return updatedScale(d.value); })
```

#### 5. Devez-vous déplacer votre cible par programme dans une position ?

* Calculez/déterminez la position et l'échelle
* Déterminez les nouvelles positions _tx_ et _ty_ et la nouvelle échelle _k_ dans la fonction de production de `transform` propre à D3 en disant :

```
var t = d3.zoomIdentity.translateBy(tx, ty).scale(k);
```

* Stockez l'objet dans la base de zoom ET propagez les changements en appelant votre premier gestionnaire de zoom, qui déplacera les cibles avec :

```
zoomBaseElement.call(zoom.transform, t);
```

* Activez maintenant le zoom déclenché par l'utilisateur avec :

```
zoomBaseElement.call(zoom)
```

Nous y voilà. Je pense qu'ils appellent cela un résumé exécutif. Cependant, nous n'avons fait qu'effleurer les concepts clés et n'avons même pas mentionné les différents moteurs de rendu. Ajoutons un peu de chair aux os avec un exemple concret.

### Ce que nous faisons

Voici le cobaye que nous allons construire en passant :

![Image](https://cdn-media-1.freecodecamp.org/images/eszAkHyvPQMl5RoS91QkOucP9dHyOEehHSaQ)
_[cela semble encore mieux sur le site final.](https://bl.ocks.org/larsvers/raw/c894849af45ce94dc85d76467980f922/" rel="noopener" target="_blank" title=")_

C'est une visualisation des planètes de notre système solaire montrant leur distance par rapport au Soleil. Le zoom sera utile pour permettre une vue d'ensemble, et le défilement donne une certaine sensation de distance. De plus, toutes les orbes sont roses !

Oh, et vous n'avez pas vraiment à le faire, mais si vous le souhaitez, vous pouvez suivre. [Allez ici pour tout le code commenté](https://github.com/larsvers/Understanding-Zoom). Alternativement, vous pouvez simplement jouer avec l'application [étape par étape](https://bl.ocks.org/larsvers/93b2f692217845d51fc75cd43c029303). Je vais laisser un lien chaque fois que nous progressons.

### Construire notre visualisation statique

Comme pour presque toutes les visualisations, les données sont notre point de départ. Donc, voici les données dans leur intégralité :

![Image](https://cdn-media-1.freecodecamp.org/images/ene8Uo371j1OexCau6haScB-2oHOdJC4EElr)

Nous avons 8 planètes, 1 étoile appelée Soleil, et Pluton, qui n'est plus vraiment une planète mais reste ici pour des raisons romantiques. Nous avons aussi la distance de chaque planète par rapport au soleil et leurs rayons. C'est tout ce dont nous avons besoin. Mais pour transformer cela en ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/3Yh8UZV5CfwPltrg85gHHKu4SCSfwlUw0y3G)

nous devons écrire un peu de code.

Veuillez noter : cet article parle du zoom plutôt que de la construction d'une visualisation statique de notre système solaire. Néanmoins, je vais passer en revue le code pour vous donner un tour complet de cette application. Cependant, si vous n'êtes ici que pour le zoom, n'hésitez pas à parcourir cette section et à passer rapidement à la première étape de construction du zoom appelée [Identifier notre base de zoom et nos cibles de zoom](#c311) (notez qu'il pourrait être utile de lire la section [Calculer les dimensions](#b9f7) dans un instant).

Commençons par le HTML minimaliste :

```
<h1 id="headline">Mesurer les <span id="pink">     <a href="http://bit.do/solar-system">distances</a>   </span> de nos planètes</h1> 
```

```
<div id="vis"></div>
```

C'est tout. Nous avons un titre avec un lien et un `span` pour lui donner une bordure inférieure rose appropriée et un conteneur `div` pour notre vis. Maintenant, nous passerons rapidement au JavaScript et contournerons le CSS, qui n'est pas invité jusqu'à la fin de cet article

La première chose que nous faisons est de charger les données :

```
d3.csv('planets.csv', row, function(error, data) {   if (error) throw error;    make(data); 
```

```
}); 
```

```
function row(d) {   return {     planet: d.planet,     distance: +d.distance,     radius: +d.radius   }; }
```

Nous chargeons notre fichier _planets.csv_ en le passant par la fonction `row()` qui s'assure que nos nombres sont bien des nombres. Ensuite, nous appelons la fonction `make()`, qui sera le foyer de tout le code suivant.

La fonction `make()` fait ce qui suit :

1. Elle définit les dimensions de notre visualisation
2. Elle construit un `svg` ainsi qu'une surface de zoom
3. Elle calcule nos échelles
4. Elle construit notre axe
5. Elle construit les planètes

Commençons par définir les dimensions de notre visualisation.

#### Calculer les dimensions [^](#3f43)

Le calcul de la marge et de la hauteur est simple :

```
var margin = {   top: window.innerHeight * 0.3,   left: 50,   bottom: window.innerHeight * 0.4,   right: 50 }; 
```

```
var height = window.innerHeight - margin.top - margin.bottom;
```

Nous voulons que l'élément `svg` couvre tout notre écran. Donc, notre hauteur sera `window.innerHeight` moins certaines marges. Nous définissons les marges supérieure et inférieure par rapport à `window.innerHeight` pour les garder relatives l'une à l'autre.

Passons à la largeur, qui nécessite un peu plus de réflexion :

```
var maxDist = d3.max(data, function(d) { return d.distance; }); 
```

```
var mapScale = 1/10e4; 
```

```
// La largeur totale de toutes les planètes var chartWidth = maxDist * mapScale; 
```

```
// la largeur du svg ne sera que aussi grande que l'écran var screenWidth = window.innerWidth - margin.left - margin.right;
```

L'essentiel de notre calcul de largeur est que nous voulons **deux** largeurs. Une pour le graphique et une pour le `svg`. Quelle est la différence ? Eh bien, le graphique sera très large, car il doit contenir toutes nos planètes. Le `svg`, cependant, n'a pas besoin d'être très large. La tâche du `svg` est de nous montrer les planètes qui tiennent dans notre fenêtre de navigateur. Un `svg` des dimensions de la fenêtre est donc suffisant. Cela ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/fM25kd-1OYa6wUnNnE7TnD8ta1DNPy0lA5Ih)
_Notre graphique est plus large que notre svg_

Notez que cela n'est possible qu'en utilisant le comportement de zoom. Si nous voulions permettre à l'utilisateur de voir toutes les planètes sans la magie du zoom et du défilement, nous devrions avoir un `svg` aussi large que le graphique. En conséquence, le navigateur nous donnerait des barres de défilement que nos utilisateurs pourraient utiliser pour se déplacer vers la droite ou la gauche  comme dans la merveilleuse [visualisation If the Moon were only 1 Pixel](http://joshworth.com/dev/pixelspace/pixelspace_solarsystem.html).

Cependant, en utilisant D3 zoom, l'objet de transformation de zoom que nous allons initialiser gardera une trace de nos gestes : à quel point nous avons défiler vers la droite, la gauche, et le long de l'axe z, perçant virtuellement à travers l'écran en suivant notre ligne de mire.

Sur la base de la transformation, nous pouvons repositionner nos éléments. Et s'ils se trouvent être dans les coordonnées de l'écran, ils s'affichent sur notre `svg` de base. Pas de mal si ce n'est pas le cas, ils ne seront simplement pas affichés.

Ainsi, la largeur de notre `svg` recevra `screenWidth` qui est simplement `window.innerWidth` moins les marges. À quel point notre `chartWidth`, la base de toutes les planètes, sera-t-elle large ? Nous allons réduire l'échelle de la distance entre les deux orbes les plus éloignés (le Soleil et Pluton, c'est-à-dire) avec notre `mapScale` de 10e4, ou 1:10,000. Lorsque Pluton est à 5,913,000,000 km du Soleil dans l'espace réel, il sera à 59,130 pixels du centre du Soleil dans notre visualisation.

Ce n'était pas trop mauvais. En avant !

#### Construire la base

Tout d'abord, nous construisons notre base `svg` : un élément `g` transformé par la marge suspendu à un élément `svg` :

```
var svg = d3.select('#vis')   .append('svg')     .attr('width', screenWidth + margin.left + margin.right)         .attr('height', height + margin.top + margin.bottom)      .append('g')     .attr('class', 'chart')     .attr('transform', 'translate(' + margin.left + ', '            + margin.top + ')');
```

Ensuite, nous le superposons avec un élément `rect` que nous utiliserons comme notre **base de zoom**. Ce `rect` écoutera tous les événements et gestes de la souris, et comme tel, nous l'appellerons audacieusement `listenerRect` :

```
var listenerRect = svg   .append('rect')     .attr('class', 'listener-rect')     .attr('x', 0)     .attr('y', -margin.top)    .attr('width', screenWidth)     .attr('height', height)    .style('opacity', 0);
```

Il est important de noter ici que notre base de zoom est au même endroit que les cibles de zoom  les éléments que nous voulons zoomer. Nous attacherons notre base de zoom `listenerRect` au `svg` (qui est en fait l'élément `g.chart` traduit par la marge comme vous pouvez le voir juste un bloc de code au-dessus), qui sera également le foyer de nos cercles de planètes que nous dessinerons plus tard.

Passons aux échelles.

#### Configurer nos échelles

Nous mappons deux mesures aux coordonnées de l'écran : la distance et le rayon. Comme tel, nous avons besoin de deux échelles. Voici la première, mappant les rayons de nos planètes en km aux rayons de l'écran :

```
var rExtent = d3.extent(data, function(d) { return d.radius; }); 
```

```
var rScale = d3.scaleLinear()   .domain([0, rExtent[1]])   .range([3, height/2 * 0.9]);
```

Tout d'abord, nous obtenons l'échelle du rayon. Nous calculons le domaine et mappons ces valeurs à une plage de 3px à un peu moins de la moitié de la hauteur de notre fenêtre, en gardant les mesures relatives à la fenêtre.

Notre deuxième échelle est l'échelle de distance :

```
var xScale = d3.scaleLinear()   .domain([0, maxDist])   .range([0, chartWidth]);
```

Nous mappons l'étendue des données à la `chartWidth` complète. Si vous la mappiez à la `screenWidth`, toutes les planètes seraient debout sur leurs pieds :

![Image](https://cdn-media-1.freecodecamp.org/images/FWA6ldRH7g1teJGRQJTQ1fTlKB0yrabcK61D)
_Trop dense_

Nous pourrions corriger cela en utilisant une échelle de rayon plus serrée, mais nous aimerions qu'elles s'étirent initialement et permettent ensuite à l'utilisateur de zoomer ou de dézoomer.

#### Dessiner l'axe

![Image](https://cdn-media-1.freecodecamp.org/images/2MMoXn49wHPp1zk6BteqVNXW4hzD9xwesRgH)
_[Aged Pixel](https://fineartamerica.com/featured/fountain-pen-patent-from-1884-blueprint-aged-pixel.html" rel="noopener" target="_blank" title="">Brevet de stylo à plume de 1884  Blueprint</a>  par <a href="https://www.agedpixel.com/" rel="noopener" target="_blank" title=")_

Nous utiliserons un composant d'axe D3 normal pour construire l'axe. Cependant, comme vous pouvez le voir sur l'image ci-dessus, nous allons décaler les étiquettes pour qu'elles ne se chevauchent pas.

Tout d'abord, nous construisons le composant d'axe :

```
var xAxis = d3.axisBottom(xScale)   .tickSizeOuter(0)   .tickPadding(10)   .tickValues(data.map(function(el) { return el.distance; }))   .tickFormat(function(d, i) {     return data[i].planet + ' ' + d3.format(',')(d) + ' km';   });
```

Nous déterminons le nombre exact d'étiquettes de graduation en passant un tableau des valeurs de distance des planètes à `.tickValues()` :

```
[0, 58000000, 108000000, 150000000, 228000000, 778000000,   1429000000, 2871000000, 4504000000, 5913000000]
```

L'axe ne dessinera maintenant que des étiquettes de graduation pour ces valeurs. Nous utilisons `.tickFormat()` pour spécifier ce que l'étiquette dira. Dans notre cas, ce sera _<nom de la planète> <distance du soleil> <km>._

Maintenant, nous produisons la base `g` de l'axe et libérons le composant sur celle-ci :

```
var xAxisDraw = svg.insert('g', ':first-child')  .attr('class', 'x axis')   .call(xAxis);
```

Comme notre `listenerRect`, l'axe devient un enfant de notre élément `g.chart` que nous avons étiqueté `svg`. Pourquoi l'insérer ? Nous voulons que notre base de zoom soit au-dessus de tous les autres éléments suspendus au `svg` afin qu'elle puisse consommer tous les événements. En regardant le DOM, il devrait être le dernier enfant de `svg`. Pour y parvenir, nous insérerons l'axe  et bientôt les planètes  _avant_ `listenerRect`.

Passons à nos étiquettes d'axe. Par défaut, toutes les étiquettes seront dessinées au même niveau _y_. Mais nous voulons qu'elles soient décalées, nous devons donc écrire un peu de code pour obtenir les étapes. Voici le décalage que nous appliquons :

```
// Déplacer les étiquettes et les lignes de l'axe vers le bas 
```

```
var labelHeight = xAxisDraw.select('text').node().getBBox().height; 
```

```
xAxisDraw.attr('transform', 'translate(0, ' +                 (height + labelHeight * data.length) + ')'); 
```

```
// Positionner le texte de l'axe 
```

```
xAxisDraw.selectAll('text')   .attr('y', function(d, i) {     return -(i * labelHeight + labelHeight);   })   .attr('dx', '-0.15em')   .attr('dy', '1.15em')   .style('text-anchor', 'start');
```

Ne vous sentez pas obligé de me suivre dans ce terrier de lapin  en bref, nous les déplaçons tous vers le bas par _# de labels  leur hauteur de label_. Ensuite, nous déplaçons chaque étiquette vers le haut par _leur hauteur  leur index_. En conséquence, le Soleil, par exemple, ne bougera pas vers le haut car il sera soulevé par _0  labelHeight = 0_, mais Mercure (la planète suivante du Soleil) bougera vers le haut par _1  labelHeight_ et ainsi de suite.

La ligne de graduation nécessite un peu plus d'attention, car nous devons tenir compte de ses valeurs _y1_ et _y2_ :

```
// Dessiner les lignes de l'axe 
```

```
xAxisDraw.selectAll('line')   .attr('y1', function(d, i) {     return -(i * labelHeight + labelHeight);   })   .attr('y2', function(d, i) {       return -(i * labelHeight + labelHeight + from axis-y 0            // ^ cette position de départ de l'étiquette              (data.length-1-i) * labelHeight +             // ^ la distance de la position de départ             //   au bas de la zone du graphique               height);             // ^ la hauteur    });
```

Bonne nouvelle. Nous pouvons maintenant dessiner nos planètes en (presque) une seule chaîne D3 :

```
var gPlanets = svg  .insert('g', '.listener-rect')  .attr('class', 'planet-group');
```

```
var planets = gPlanets.selectAll('.planet')     .data(data)  .enter().append('circle')     .attr('class', 'planet')     .attr('id', function(d) { return d.planet; })     .attr('cx', function(d) { return xScale(d.distance); })     .attr('cy', 0)     .attr('r', function(d) {       d.scaledRadius = rScale(d.radius);       return d.scaledRadius;     });
```

Tout d'abord, nous créons un groupe pour toutes nos planètes et nous assurons que le `listenerRect` couvre également ces planètes en insérant notre `g.planet-group` avant le `rect.listener-rect`. Ensuite, nous joignons et `enter()` les données à nos `.planet` virtuels, qui se manifesteront sous forme de cercles avec les distances respectivement mises à l'échelle comme positions x et les rayons `rScale`. Donc, voici :

![Image](https://cdn-media-1.freecodecamp.org/images/8xq7RBo6J3qXZByVPabvhU2O-bVrJBZWdOuK)
_Une disposition planétaire sensée_

Super ! Nous avons notre visualisation. Maintenant, passons au zoom

### Identifier notre base de zoom et nos cibles de zoom [^](#3f43)

![Image](https://cdn-media-1.freecodecamp.org/images/ro4TGnVUmyhVVvswxFoDVNFK3dw494Awt2E3)

Il est souvent judicieux de commencer par réfléchir à ce que vous voulez faire avant de plonger tête la première dans le code. Avant de configurer notre zoom, identifions **quoi** et **comment** nous voulons zoomer et faire défiler. Nous posons 3 questions :

1. Quelle sera notre base de zoom  l'élément capteur que nous utiliserons pour le zoom ?
2. Quelles seront nos cibles de zoom  les éléments que nous allons déplacer ?
3. Quel type de zoom voulons-nous pour chaque élément  zoom géométrique ou sémantique ?

#### Identifier notre base de zoom

Choisissons d'abord notre élément de base de zoom. Vous pouvez attacher le zoom à un `svg`, `g`, `rect` ou tout autre élément auquel votre souris a accès. Notez ici que les éléments `g` ne peuvent enregistrer des événements que là où ils ont des enfants avec une propriété `fill` définie. Donc, si vous avez un grand élément `g` avec un cercle de rayon 1, vos gestes de zoom ne fonctionneront que sur ce petit cercle.

Ainsi, il est souvent judicieux de configurer un `rect` dédié avec un remplissage, mais une opacité de 0. Vous devez vous assurer que la base de zoom peut consommer tous les événements. Donc, elle doit soit être au-dessus de tous les autres éléments, soit ses `pointer-events` doivent être définis sur `all` tandis que les `pointer-events` de tous les autres éléments sont définis sur `none`.

En fait, nous avons déjà totalement décidé de configurer un élément `rect` supplémentaire pour écouter les événements. Nous l'avons judicieusement mis en cache dans la variable `listenerRect`, à laquelle nous pouvons nous référer lors de la configuration. Fait.

#### Identifier nos cibles de zoom

Maintenant, identifions nos éléments cibles et notons-les. Quels éléments voulons-nous déplacer lorsque nous zoomons et faisons défiler ? Faisons une liste :

* Les planètes
* L'axe et tous leurs éléments (lignes de graduation et texte de graduation uniquement ; nous ne montrons pas le chemin de l'axe).

Maintenant que nous connaissons notre base de zoom et nos cibles, nous voulons nous assurer qu'elles partagent le même système de coordonnées à l'état de zoom initial  lorsque aucun zoom ou défilement n'a encore eu lieu. C'est pourquoi nous avons attaché la base de zoom et les cibles (planètes, axe) au même `g` ci-dessus.

Cela se passe vraiment bien !

#### Identifier le type de zoom

Enfin, décidons **comment** nous voulons les zoomer  géométriquement ou sémantiquement ? Tout d'abord, cette distinction n'a de sens que pour le zoom, pas pour le défilement. Nous l'avons défini ci-dessus, mais pour le bien de la complétude redondante, répétons que le zoom géométrique est simple : tous les éléments sont simplement mis à l'échelle uniformément. Le zoom sémantique est un peu plus élaboré, car vous pouvez décider ce que vous voulez mettre à l'échelle.

Dans notre cas, nous pourrions vouloir mettre à l'échelle la taille des planètes, mais garder la largeur de la ligne à 4px. Pour cela, nous aurions besoin d'un zoom sémantique. À des fins éducatives, implémentons les deux types ! Pourquoi pas ?

#### Configurer le zoom

Pour tout zoom que nous décidons d'implémenter, nous devrons d'abord le configurer. Vous serez probablement d'accord pour dire que cela ne pourrait pas être moins complexe :

```
var zoom = d3.zoom() .on('zoom', zoomed);
```

L'appel à `d3.zoom()` renverra un objet et une fonction. Comme pour de nombreuses parties de l'API D3, l'objet nous permet de configurer les variables que nous utilisons dans la fonction. Donc, ce que nous faisons là-haut, c'est configurer l'utilisation de la fonction `d3.zoom()` avec une seule méthode : `.on()` attache une fonction de gestionnaire appelée `zoomed`. `zoomed` sera appelée chaque fois que nous `zoom`. C'est là que nous ferons bouger les éléments.

Nous avons deux autres événements de cycle de zoom pour déclencher une fonction, `start` et `end`. Il devrait être relativement facile de deviner quand ils déclencheraient le rappel.

Nous stockons la fonction retournée dans la variable créativement nommée `zoom`. Ensuite, nous pouvons utiliser cette fonction comme `zoom(<listener-elemen`t>) ou, comme c'est plus couramment fait dans D3 `<listener-element>`;.call(zoom) comme suit :

```
listenerRect.call(zoom);
```

C'est bien, mais que signifie cela ? Cela signifie que le `listenerRect` est maintenant le foyer officiel de notre zoom. Notre **base de zoom** ! À ce moment précis, il a deux choses qui pendent : l'événement `.on()` et la transformation de zoom. Si nous `console.dir(d3.select(#listener-rect).node())` et vérifions nos attributs, nous trouverons ces deux propriétés D3 tout en bas de la liste :

![Image](https://cdn-media-1.freecodecamp.org/images/Dzkx825jmBmynOuux1ywx7F14t6-lnZBLSe0)

L'objet `__on` contient les informations de notre écouteur, et l'objet `__zoom` est un objet de transformation contenant les 3 valeurs dont nous avons parlé au début de ce pot : la translation _x_ et _y_ lorsque nous zoomons et faisons défiler, et le facteur d'échelle _k_ qui change lors du zoom.

Vous pouvez toujours venir à votre base de zoom  le `listenerRect` pour nous  pour interroger les valeurs de transformation actuelles. Cependant, vous n'avez pas besoin de le faire très souvent, car la transformation sera facilement accessible dans l'objet d'événement depuis notre fonction de gestionnaire `zoomed`. Bien. Pour l'amour de nos vies  zoomons enfin.

### Zoom géométrique avec SVG

![Image](https://cdn-media-1.freecodecamp.org/images/-36w5lnDI3YN5Fnvam5OULSpIQdF3cHj7f9C)
_[Aged Pixel](https://fineartamerica.com/featured/microscope-patent-from-1886-blueprint-aged-pixel.html" rel="noopener" target="_blank" title="">Brevet de microscope de 1865  Blueprint</a> par <a href="https://www.agedpixel.com/" rel="noopener" target="_blank" title=")_

Nous avons notre visualisation statique. Nous avons configuré le zoom. Nous l'avons attaché à la base de zoom. Décidons enfin quel type de zoom nous allons utiliser. Voici la chose : les axes doivent être zoomés sémantiquement, vous décidez pour les autres éléments. En revenant à nos cibles de zoom, décretsons cela ici dans un tableau sur un morceau de parchemin :

![Image](https://cdn-media-1.freecodecamp.org/images/jhn4SXxDV1nZhLiXGPD2YwVQ4Wodu46J-1de)

Maintenant, écrivons le gestionnaire de zoom :

```
function zoomed() { 
```

```
  var transform = d3.event.transform; 
```

```
  gPlanets.attr('transform', transform.toString()); 
```

```
}
```

Nous n'avons pas tout à fait terminé, mais c'est le zoom le plus simple possible et il déplacera déjà nos planètes. Nous mettons en cache l'objet de transformation qui pend à l'objet `d3.event` qui est passé à chaque mouvement de zoom et de défilement dans la variable `transform`. Ensuite, nous déplaçons nos planètes en mettant simplement à jour l'attribut `transform` de nos cercles.

`transform.toString()` est juste une méthode de commodité que l'objet de transformation nous donne. Elle nous évite d'avoir à taper la valeur de l'attribut de transformation. Pour la transformation d'identité `{ k: 1, x: 0, y: 0 }`, elle retourne la chaîne `"translate(0, 0) scale(1)"`

À quoi cela ressemblera-t-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/Mou1U4RBJaWyJldIlaFxL7xpEnVm7PDYe9BP)
_Super ! Les planètes bougent (partout dans le magasin)_

Très bien ! Les planètes bougent  le reste ne bouge pas. Nous devons faire 3 choses pour améliorer cela :

1. Empêchons les planètes de se déplacer vers la droite (il n'y a pas de planète à gauche du soleil, donc ce serait futile).
2. Empêchons également les planètes de se déplacer vers le haut et vers le bas.
3. Déplaçons les échelles.

1 et 2 sont simples ; nous manipulons simplement l'objet de transformation avant de l'utiliser comme suit :

```
function zoomed() { 
```

```
  var transform = d3.event.transform;     transform.x = Math.min(0, transform.x);   transform.y = 0; 
```

```
  gPlanets.attr('transform', transform.toString()); 
```

```
}
```

En conséquence, _x_ n'est jamais supérieur à 0, et donc nous ne pouvons pas déplacer la chose vers la droite. De plus, _y_ sera toujours 0. Le résultat fait ce que nous attendons :

![Image](https://cdn-media-1.freecodecamp.org/images/KAhIb4qUCSfvKQU6ctgBlOtUG9229UYL0Nch)
_Les planètes bougent (..seulement sur les parties sensées du magasin)_

Ensuite, faisons bouger l'axe de manière sémantique. Notre axe se compose d'étiquettes et de lignes. Nous choisissons le zoom sémantique plutôt que le zoom géométrique, car nous voulons seulement changer leur **position** lors du zoom  pas la taille de l'étiquette ou la largeur de la ligne.

Le principal moteur de positionnement derrière les éléments de l'axe  la chose qui fait bouger les étiquettes et les lignes  est l'échelle. Et que fait l'échelle ? L'échelle mappe nos valeurs de données à la largeur de notre élément `svg`. Si nous voulons changer une échelle avec D3, nous mettons généralement à jour le domaine et/ou la plage de l'échelle. Mais comme le redimensionnement des axes est une activité si courante pour D3 zoom, nous avons les méthodes `rescaleX()` et `rescaleY()` qui pendent de l'objet `transform`. Il met à jour le mappage pour nous selon le zoom. Parfait sucre syntaxique que nous pouvons utiliser pour créer une échelle mise à jour :

```
var xScaleNew = transform.rescaleX(xScale);
```

La section suivante s'appelle _Zoom sémantique avec SVG_ et ouvrira négligemment le capot de cette méthode `rescaleX()` en beaucoup plus de détails. Mais pour l'instant, utilisons simplement `xScaleNew` de manière confiante comme suit :

```
xAxis.scale(xScaleNew); xAxisDraw.call(xAxis);
```

Nous mettons à jour l'échelle de notre `xAxis` et redessinons l'axe avec notre nouveau composant d'axe. La dernière chose que nous devons faire à l'axe est de décaler à nouveau nos étiquettes et lignes, comme nous l'avons fait ci-dessus.

```
// Décaler les étiquettes de l'axe xAxisDraw.selectAll('text')   .attr('y', function(d, i) {     return -(i * labelHeight + labelHeight);   }) 
```

```
// Décaler les lignes de l'axe xAxisDraw.selectAll('line')   .attr('y1', function(d, i) {     return -(i * labelHeight + labelHeight);   })   .attr('y2', function(d, i) {     return -(i * labelHeight + labelHeight            + (data.length-1-i) * labelHeight + height);   });
```

N'oubliez pas que tout cela se passe dans notre gestionnaire `zoomed`.

Cela fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/NiYK94-4Hzwmye85Qxj1TQgDnT1hf25COoUX)
_Zoom géométrique avec SVG [sans code](https://bl.ocks.org/larsvers/95115f57fb67ac8c0a568fdd28ae8c00" rel="noopener" target="_blank" title="">avec</a> et <a href="https://bl.ocks.org/larsvers/raw/95115f57fb67ac8c0a568fdd28ae8c00" rel="noopener" target="_blank" title=")_

### Zoom sémantique avec SVG

Ce titre arrive un peu tard. Nous avons déjà zoomé sémantiquement notre axe. Mais maintenant, appliquons-le également à nos planètes et plongeons dans le processus de redimensionnement. Voici notre tableau de préparation mis à jour :

![Image](https://cdn-media-1.freecodecamp.org/images/cNic-yb-7CiIwK-rAqtCGsC6xV8hGIcts9U7)

#### Zoom sémantique des cercles

Tout d'abord, pourquoi voudrions-nous utiliser le zoom sémantique sur les planètes ? Je pense que le gif ci-dessus démontre assez bien le besoin sémantique. À mesure que les planètes deviennent plus petites, leur contour est presque impossible à voir. Avec le zoom sémantique, nous aurons le contrôle sur les propriétés des éléments qui changent ou restent. Dans notre cas, le zoom doit changer la position ainsi que la taille de nos planètes, mais la largeur du trait de contour doit rester constante à 4px.

Ce que nous faisons est simple :

```
function zoomed() { 
```

```
  var transform = d3.event.transform; 
```

```
  transform.x = Math.min(0, transform.x); 
```

```
  var xScaleNew = transform.rescaleX(xScale); 
```

```
  planets     .attr('cx', function(d) {       return xScaleNew(d.distance);     })    .attr('r', function(d) {       return d.scaledRadius * transform.k;     }); 
```

```
  // Zoom et défilement de l'axe ici () 
```

```
}
```

Tout d'abord, nous supprimons notre zoom géométrique des planètes. Ensuite, nous prenons nos planètes et, au lieu de les transformer, nous accédons spécifiquement uniquement à leurs attributs `cx` et `r`. La position _x_ sera recalculée avec l'échelle `xScaleNew` mise à jour et le rayon doit simplement être multiplié par le facteur d'échelle. Aucune traduction nécessaire ici.

Et c'est tout :

![Image](https://cdn-media-1.freecodecamp.org/images/pDDoB4YnFS7ljpd4TbCzbmDemrf8FrLaGO2w)
_Zoom sémantique avec SVG [sans code](https://bl.ocks.org/larsvers/1333b243c89809d39290e42bb3d79924" rel="noopener" target="_blank" title="">avec</a> et <a href="https://bl.ocks.org/larsvers/raw/1333b243c89809d39290e42bb3d79924" rel="noopener" target="_blank" title=")_

Cependant, aussi loin que nous zoomions ou dézoomions, notre trait reste à 4px, nous permettant de voir nos planètes même si elles sont complètement dézoomées.

#### Comprendre le redimensionnement du zoom

![Image](https://cdn-media-1.freecodecamp.org/images/XiS97HLNt8M630tW1MfHN5jJXvMIfekFQGsP)
_quelques échelles non liées_

Le zoom sémantique nous oblige à zoomer et à faire défiler les propriétés de manière sélective. Notre zoom sémantique des planètes ci-dessus n'a changé que l'attribut `cx` et `r`, tout en gardant la largeur du trait à 4px. Pour changer spécifiquement `cx`, nous avons dû mettre à jour notre échelle  le principal moteur de positionnement de notre visualisation  afin qu'elle positionne nos éléments selon la nouvelle transformation.

Comme mentionné, D3 offre les méthodes de commodité `rescaleX()` et `rescaleY()` pour mettre à jour les échelles selon la transformation. Bien sûr, il est parfaitement acceptable d'utiliser ces méthodes sans connaître les rouages internes, alors n'hésitez pas à sauter directement à [la section suivante](#6867). Mais si vous êtes curieux de savoir comment se fait exactement le redimensionnement, restez avec moi. Il y aura des images en couleur aussi.

Nous utiliserons un exemple très simple. Supposons que nous ne regardons que la dimension x, et que nous voulons mapper un espace de données couvrant un domaine de 0 à 100 à un écran de 1000 pixels de large. Ainsi, nous avons un domaine de données [0, 100] que nous voulons mapper à une plage de largeur [0, 1000]. Notre échelle ressemblerait à ceci :

```
var xScale = d3.scaleLinear()   .domain([0, 100])   .range([0, 1000]);
```

Supposons également que nous avons un seul cercle avec la valeur de données 20, qui serait mappée à la valeur de pixel 200 :

![Image](https://cdn-media-1.freecodecamp.org/images/UZGEof1XMqOO815gui41FLr3ujg234G1qqgz)

Facile. Maintenant, nous zoomons pour que notre facteur d'échelle _k_ soit 2. Pas de translation, juste un zoom. En conséquence, notre cercle se déplacerait selon notre formule de transformation de zoom que nous avons commencé ce post avec : _tx + x  k_, ce qui donnerait _0 + 200  2 = 400_ :

![Image](https://cdn-media-1.freecodecamp.org/images/uZNrX6CdYH6FRK29azSAdZFAfURSDyLH-4hZ)

Notez que nous avons également mis à l'échelle son rayon par 2. Tout va bien jusqu'à présent ? Super.

Dans ce cas, nous pourrions simplement faire notre calcul de transformation pour le cercle. Mais il est beaucoup plus simple, plus pratique et plus cohérent de continuer à utiliser notre échelle. Cependant, nous devons la mettre à jour, car notre valeur de données 10 ne doit plus être mise à l'échelle à 100px mais à 200px !

Comment faisons-nous cela ? Comme nous l'avons fait ci-dessus, nous passons simplement notre `xScale` à la fonction `transform.rescaleX()`. Cela retourne l'échelle `newXScale` respectivement mise à jour, que nous utilisons sur la valeur de données du cercle pour déterminer la position `cx` :

```
var newXScale = transform.rescaleX(xScale); 
```

```
circle.attr(cx, function(d) { return d.dataValue; }); // note : d.dataValue provient d'un ensemble de données fictif
```

Mais que fait exactement ce redimensionnement ? Regardons d'abord le [code](https://github.com/d3/d3-zoom/blob/master/src/transform.js#L33) [source](https://github.com/d3/d3-zoom/blob/master/README.md#transform_rescaleX) avant de considérer sa logique. Un redimensionnement sous le capot ressemble à ceci :

```
function rescaleX(x) { 
```

```
  var range = x.range().map(transform.invertX, transform), 
```

```
  domain = range.map(x.invert, x); 
```

```
  return x.copy().domain(domain); 
```

```
}
```

Comme vous pouvez le voir à la dernière ligne, il retournera l'échelle originale **MAIS** avec un domaine mis à jour. La plage restera telle quelle. Si vous me l'aviez demandé avant que je ne regarde ce code, j'aurais deviné que D3 mettrait à jour la plage et garderait le domaine tel quel. Beaucoup plus direct. Mais c'est l'inverse. Cela a du sens, car la plage de pixels est un concept plus statique. Dans notre cas, 1000 est la largeur de l'écran  cela ne changera pas lors du zoom.

Le (petit) inconvénient est que le calcul du nouveau domaine est légèrement plus complexe que le calcul d'une nouvelle plage. Il y a 4 étapes impliquées dans le calcul du nouveau domaine à chaque mouvement de zoom et de défilement :

1. Nous prenons d'abord la plage de notre échelle originale. Dans notre exemple, ce serait [0, 1000].
2. Nous appliquons ensuite la transformation inverse, qui retournera [0, 500].
3. Ensuite, nous utiliserons la méthode `.invert()` de l'échelle pour trouver la valeur de données associée aux valeurs de plage 0 et 500, qui sera [0 et 50] dans notre cas.
4. Enfin, nous remplaçons le domaine actuel de l'échelle x par ce nouveau domaine et le retournons.

Mais pourquoi ? Considérons cela conceptuellement

Tout d'abord, nous calculons une nouvelle plage en prenant l'inverse de notre fonction de transformation pour la valeur _x_. Maintenant, nous savons que la fonction de transformation de zoom pour _x est tx + x  k_. Son inverse est _(x  tx) / k_.

Si vous n'avez jamais rencontré de fonctions inverses, elles sont simplement l'opposé  le inverse de leur fonction principale. Si vous aviez **f(x) = 3  x**, alors l'inverse est **g(y) = y/3**. En insérant 2 dans la fonction principale **f(x)**, cela retourne 6  en insérant ce 6 dans la fonction inverse **g(y)**, cela retourne 2 à nouveau. Cela inverse le processus de la fonction principale.

Pourquoi prenons-nous l'inverse de notre plage ? Nous voulons ajuster le domaine, mais garder la plage à [0, 1000]. Le moyen le plus simple d'obtenir le domaine mis à jour est de calculer d'abord les valeurs d'étendue de plage mises à jour (min et max) afin d'en déduire les nouvelles valeurs d'étendue de domaine.

Jouons cela avec une seule valeur. Prenons notre valeur de plage maximale de 1000. Notre échelle actuelle mappe la valeur de données maximale de 100 à la valeur de plage maximale de 1000 pixels.

Quelle est la valeur de plage maximale lorsque nous mettons à l'échelle par 2 ? Mettre à l'échelle par 2 signifie que nous zoomons. Donc, notre valeur de plage maximale actuelle de 1000 se déplacera à 2000 _(0 + 1000  2)_. Cependant, nous aimerions connaître le nouveau point de pixel qui se déplace vers le bord de notre écran lorsque nous zoomons. Le point précédent qui était à 1000 et est maintenant à 2000 ne nous est d'aucune aide car il est maintenant au-delà de la zone de l'écran. Donc, quel point est au bord de notre fenêtre après avoir zoomé ? Quel point est notre nouvelle valeur de plage maximale ?

Afin d'obtenir ce point, nous ne demandons pas : où notre valeur de plage maximale actuelle de 1000 zoome-t-elle ? Nous demandons, d'où vient la nouvelle valeur de plage maximale ! Logiquement, c'est l'opposé ou la **QUESTION INVERSE**. En conséquence, nous appliquons la transformation de zoom inverse : _(x  tx) / k_. Nous insérons notre valeur de plage maximale précédente de 1000px, notre _tx_ de 0 et l'échelle _k_ de 2 pour obtenir : _(10000) / 2 = 500_.

![Image](https://cdn-media-1.freecodecamp.org/images/pnfU0FULVdfx8DDWt24rf2nI8b7dlAazujKz)

Nous pouvons maintenant dire que notre nouvelle valeur de plage maximale proviendrait de la position de pixel 500.

Pourquoi avons-nous fait cela à nouveau ? N'est-ce pas un peu stupide puisque nous voulons garder la plage à [0, 1000] de toute façon ? Oui. Et non. Ce n'est pas stupide, car nous n'utilisons pas cette nouvelle valeur de plage maximale dans une nouvelle entrée de plage pour notre échelle. Nous l'utilisons simplement pour trouver notre nouvelle valeur de domaine de données maximale.

Nous prenons notre échelle originale qui mappait une valeur de données de 0 à 0 pixel, une valeur de données de 100 à 1000 pixel et toutes les valeurs intermédiaires en conséquence. Maintenant, nous demandons quelle valeur de données mappe à la valeur de pixel de 500 ? Pour ce cas simple, nous pouvons utiliser notre cerveau, ou  beaucoup mieux  nous utilisons la méthode `.invert()` de notre échelle x originale. `xScale.invert(500)` retournera 50 comme probablement attendu.

Rappelons-nous ici que nous avons toujours notre plage originale de [0, 1000]. Tous les calculs de plage que nous avons faits n'ont été faits que pour obtenir le nouveau domaine. Notre nouvelle échelle x mappe toujours la valeur de données 0 au pixel 0, mais mappe maintenant la nouvelle valeur de domaine de données maximale de 50 à la valeur de plage maximale fidèlement debout de 1000.

![Image](https://cdn-media-1.freecodecamp.org/images/rXBMWsok6EnXSerqaIiss9wLZtJxfbxACIJe)

De même, la valeur x du centre de notre cercle a toujours la valeur de données de 10, qui maintenant ne mappe pas à 100 mais à 200. Nous avons réussi à zoomer, nous l'avons fait.

Bien joué ! Maintenant, passons à Canvas. Même jeu  tableau différent

### Zoom géométrique avec Canvas [^](#102a)

![Image](https://cdn-media-1.freecodecamp.org/images/ODtogah6O8ay1E4DOoTtnb2D7sfXrisggqAd)

Nous n'avons que 10 cercles sur notre site. Cependant, il y a bien sûr beaucoup plus d'orbes à visualiser. Visualiser plus de 1000 d'entre eux pourrait vous causer des problèmes de performance de rendu, que vous pouvez tenter de résoudre avec Canvas.

Contrairement à SVG, Canvas produit une seule image bitmap de votre dessin. 1000 planètes sur votre écran seront dessinées sur un seul élément DOM, le `canvas`. En SVG, 1000 planètes produiront 1000 éléments de cercle que le navigateur doit maintenir, ce qui affecte les performances. Il y a une liste de ressources Canvas dans la [section sources](#28f2) ci-dessous si vous voulez en savoir plus, mais ne vous inquiétez pas, vous n'avez pas besoin d'un diplôme Canvas pour suivre.

Nous allons changer très peu de choses dans notre application. Pour un rappel rapide, voici les principales étapes que nous avons suivies pour en arriver là :

1. Charger les données
2. Calculer les dimensions de notre visualisation
3. **Construire la base SVG et le rectangle écouteur**
4. Calculer les échelles
5. Définir et dessiner l'axe
6. **Construire la visualisation SVG**
7. **Zoom**

Nous allons changer les points 3, 6 et 7 ci-dessus et laisser le reste inchangé. En fait, nous ne produirons pas un dessin Canvas pur, mais plutôt dessinerons les planètes en Canvas et garderons les axes en SVG. Cela s'appelle le **rendu en mode mixte**, et est vraiment intelligent si vous avez des axes à dessiner. Dessiner des axes est merveilleusement résolu par D3 en SVG mais peut être un casse-tête en Canvas. ([Elijah Meeks](https://www.freecodecamp.org/news/get-ready-to-zoom-and-pan-like-a-pro-after-reading-this-in-depth-tutorial-5d963b0a153e/undefined) consacre une bonne section au rendu en mode mixte dans le chapitre 11 de son livre [D3js in Action](https://www.manning.com/books/d3-js-in-action))

#### Ajouter une base canvas

Comme pour SVG, nous avons besoin d'une base sur laquelle dessiner. Pour Canvas, nous avons besoin de deux choses, l'élément `canvas` et son contexte de dessin  les outils que nous pouvons utiliser pour dessiner sur le canvas. Sous notre base `svg`, nous ajoutons le snippet de base Canvas suivant :

```
var canvas = d3.select('#vis').append('canvas')   .attr('width', screenWidth + margin.left + margin.right)     .attr('height', height + margin.top + margin.bottom); 
```

```
var context = canvas.node().getContext('2d');
```

Il est souvent judicieux de sauter la convention de marge pour Canvas (nous n'avons pas de `g` que nous pouvons déplacer). Mais, surtout lorsque nous dessinons des axes SVG, nous voulons nous accrocher à nos marges.

Nous voulons également superposer parfaitement notre élément `canvas` sur notre élément `svg` et ses enfants, le `g` de la planète et le `listenerRect`. Pour y parvenir, nous devons lui donner la même taille que l'élément `svg` et positionner le canvas de manière absolue au-dessus du `svg`. Voici notre CSS :

```
canvas {   position: absolute;   top: 0;   left: 0;   pointer-events: none; }
```

Remarquez que nous supprimons également tous les pointer-events de notre `canvas` afin que le `listenerRect` reçoive tous les gestes. En conséquence, nous avons plusieurs couches :

![Image](https://cdn-media-1.freecodecamp.org/images/a3BybwKg5TDLH-2sQ8alKamCObAuAFC4qGGT)
_Notre gâteau à couches avec l'axe SVG et les planètes Canvas_

Le `g` ne contient maintenant que notre axe, que nous pouvons voir à travers notre `svg`. Le `canvas` affichera nos planètes, mais seulement la section en vert ci-dessus (les autres planètes sont dessinées ici pour l'exhaustivité mais seront initialement invisibles). Le niveau supérieur est le `listenerRect` qui consomme tous les événements de pointeur et informe notre zoom et notre défilement.

#### Dessiner les cercles des planètes en Canvas

Nous supprimons la logique qui a construit les planètes SVG, et dessinons plutôt nos cercles Canvas. Nous allons le dessiner dans une seule fonction. Laissez-moi d'abord vous montrer le code de cette fonction de dessin Canvas avant de vous la faire parcourir. C'est parti :

```
function drawGeometricCircles(data, transform) {
```

Nous passons nos données et la transformation. Si nous voulions seulement construire une visualisation statique, nous n'aurions pas à nous soucier de la transformation, mais le zoom est très beaucoup notre mission !

```
  context.clearRect(0, 0, screenWidth + margin.left + margin.right,                       height + margin.top + margin.bottom);
```

Ensuite, nous accédons à notre contexte Canvas (que nous avons mis en cache dans la variable `context`) et exécutons une méthode appelée `.clearRect`. Vous pouvez sûrement deviner ce qu'elle fait  elle efface le `canvas`. Nous lui passons les dimensions du `canvas`, ce qui effacera le `canvas` chaque fois que nous appelons cette fonction.

C'est ce que nous faisons avec Canvas. Contrairement à SVG où nous avons des nœuds manifestes dans le DOM pour nos cercles, nous n'avons qu'une image pixel sur notre `canvas`. Au lieu de déplacer un nœud DOM, nous supprimons simplement l'image que nous avons dessinée précédemment et dessinons une nouvelle image avec des éléments dans des positions légèrement différentes. C'est Canvas pour vous.

```
  context.save();
```

Ensuite, nous `.save()` le contexte par défaut et inchangé, et nous le `.restore()` dans un instant après que tout le dessin soit terminé. De cette façon, nous sécurisons non seulement une ardoise de canvas vierge, mais aussi une ardoise de contexte vierge chaque fois que nous dessinons une nouvelle planète.

```
  context.lineWidth = 4;   context.strokeStyle = 'deeppink';   context.fillStyle = 'white';
```

Ensuite, nous définissons nos pinceaux de peinture. Nous voulons une largeur de ligne de 4px, nous voulons une couleur de trait deeppink et un remplissage blanc. Ces propriétés esthétiques s'appliqueront à tout ce que nous dessinons après les avoir définies. Jusqu'à ce que nous les changions.

```
  context.translate(transform.x + margin.left, margin.top);       context.scale(transform.k, transform.k);
```

Ces deux lignes suivantes sont le zoom géométrique. Nous translatons et mettons à l'échelle toute l'image que nous dessinons par les valeurs de transformation respectives.

```
  for (var i = 0; i < data.length; i++) {
```

```
    context.beginPath();    context.arc(xScale(data[i].distance), 0,                 rScale(data[i].radius), 0, 2 * Math.PI, false);     context.stroke();     context.fill(); 
```

```
    context.fill(); 
```

```
  } 
```

```
  context.restore(); 
```

```
}
```

Enfin, nous dessinons les cercles. Si vous n'avez pas vu beaucoup de Canvas jusqu'à présent, cela peut sembler un peu brut. Et en effet, D3 internalise cette boucle à travers les éléments pour nous en joignant les données aux sélections que nous pouvons ensuite accéder, positionner et styliser.

Avec Canvas, nous faisons cela nous-mêmes. Nous parcourons les données, commençons un chemin, dessinons le chemin comme un cercle avec la méthode `context.arc()`, et enfin traçons et remplissons le chemin.

Le reste est un morceau de code. Nous devons simplement l'appeler ici, puis avec nos données et l'identité, transformer, qui est simplement `{ k: 1, x: 0, y: 0 }` :

```
drawGeometricCircles(data, d3.zoomIdentity);
```

Chaque fois que nous zoomons, nous remplaçons le code qui a déplacé nos planètes SVG par ceci :

```
drawGeometricCircles(data, transform);
```

Je vous épargnerai le gif car cela ressemble exactement à ce que nous avons vu ci-dessus avec le zoom géométrique SVG. Mais l'implémentation fonctionnelle avec le code est juste [à un clic](https://bl.ocks.org/larsvers/6f4305086c832298167a2334e3c68990) !

### Zoom sémantique avec Canvas

Célébrons notre exploit de zoom géométrique en nous en débarrassant. En fait, pour obtenir un zoom sémantique au lieu d'un zoom géométrique, nous allons simplement renommer et changer notre fonction de dessin. Nous l'appellerons de manière appropriée `drawSemanticCircles()`.

Le passage du zoom géométrique au zoom sémantique dans Canvas nécessite les mêmes actions de haut niveau. Au lieu de translater et de mettre à l'échelle le système de coordonnées des planètes, nous allons changer les positions et le rayon des planètes selon les transformations.

`drawSemanticCircles()` effacera notre canvas puis dessinera tous les cercles avec `drawCircle()` :

```
function drawSemanticCircles(data, transform) { 
```

```
  context.clearRect(0, 0, screenWidth + margin.left + margin.right,                     height + margin.top + margin.bottom); 
```

```
  for (var i = 0; i < data.length; i++) {     drawCircle(data[i], transform);   } 
```

```
}
```

`drawCircle()` sera exécuté pour chaque élément de données, prenant l'élément de données et la transformation actuelle :

```
function drawCircle(elem, transform) { 
```

```
  var x = (transform.x + transform.k * xScale(elem.distance))           + margin.left;  var y = margin.top;   var r = transform.k * rScale(elem.radius); 
```

```
  context.lineWidth = 4; context.strokeStyle = 'deeppink';     context.fillStyle = 'white'; 
```

```
  context.beginPath();   context.arc(x, y, r, 0, 2 * Math.PI);   context.stroke();   context.fill(); 
```

```
}
```

Nous déterminons d'abord les positions _x_ et _y_ ainsi que le rayon _r_. Ensuite, nous définissons les styles pour nos cercles. Enfin, nous dessinons nos sphères galactiques comme des arcs. Et c'est tout

![Image](https://cdn-media-1.freecodecamp.org/images/PDyFmGe4PRyeidQofD5IRdqSaeztdbQrlqoX)
_Zoom sémantique dans Canvas [sans code](https://bl.ocks.org/larsvers/32f2ef58c910e1d4ada8a462f7474b75" rel="noopener" target="_blank" title="">avec</a> et <a href="https://bl.ocks.org/larsvers/raw/32f2ef58c910e1d4ada8a462f7474b75" rel="noopener" target="_blank" title=")_

Super ! Nous avons couvert les deux types de zoom dans deux moteurs de rendu. Passons aux pistes bonus : zoom programmatique et rendre notre galaxie joli

### Zoom programmatique

Il est souvent utile de déplacer nos visuels dans une certaine position. Vous pouvez laisser un utilisateur centrer une carte, déplacer un long graphique à barres au début, ou zoomer et dézoomer du système solaire.

Nous n'avons ni une carte ni un graphique à barres, alors zoomons et dézoomons de manière programmatique sur nos planètes au chargement. Nous revenons à SVG pour cela, car nous n'avons pas vraiment besoin de Canvas ici. En raison de son niveau inférieur, je recommanderais d'utiliser Canvas uniquement si vous en avez besoin ou si vous le parlez comme votre langue maternelle. Comme nous n'avons que 10 cercles à déplacer ici, nous n'en avons pas besoin.

Voici ce que nous voulons réaliser :

![Image](https://cdn-media-1.freecodecamp.org/images/RgvDdfWPtDv6SecdjIRmXjuaU3oeuDooqKnI)
_Zoom programmatique en SVG [sans code](https://bl.ocks.org/larsvers/4b39be68e8cb77e7c402bd96df292db0" rel="noopener" target="_blank" title="">avec</a> et <a href="https://bl.ocks.org/larsvers/raw/4b39be68e8cb77e7c402bd96df292db0" rel="noopener" target="_blank" title=")_

Nous commençons avec une visualisation fortement zoomée à une échelle de zoom de 20. Ensuite, nous dézoomons à notre zoom minimum, de sorte que toutes les planètes tiennent confortablement sur la page. Enfin, nous zoomons à nouveau à notre échelle de zoom par défaut de 1.

Pour y parvenir, nous ajoutons la logique programmatique en bas de notre fonction `make()` où vit tout le code de notre application. Nous commençons par zoomer à un facteur d'échelle de 20 sans défilement :

```
var initialTransform = d3.zoomIdentity.scale(20); listenerRect.call(zoom.transform, initialTransform);
```

`d3.zoomIdentity` retourne la transformation d'identité que nous avons déjà rencontrée plusieurs fois. Nous changeons l'échelle de transformation à 20 et la mettons en cache dans `initialTransform`. Ensuite, nous utilisons la fonction `zoom.transform()`. Cette fonction est évidemment différente de notre objet de transformation, mais elle le manipule directement. Nous l'utilisons ici avec la méthode `.call()` propre à D3 que nous avons rencontrée ci-dessus. La sélection sur laquelle nous appelons `zoom.trans`form() sera son premier argument. Ce sera notre base de zoom `listen`erRect, foyer de notre objet de transformation actuel. Le deuxième argument doit être un nouvel objet de transformation. Il remplacera la transformation actuelle sur ce nœud.

La cerise sur le gâteau est que, au lieu de passer notre base de zoom comme une simple sélection, nous pouvons la passer comme une transition. Rappelez-vous (ou notez) que les transitions sont simplement des sélections dérivées, donc passer `listenerRect.transition()` transitionnera en fait notre visuel d'une transformation à l'autre.

Mais jusqu'à présent, nous avons simplement fait basculer notre visuel à une échelle de 20. Lancions la transition. D'abord à une échelle de `minZoom` que nous avons définie précédemment, puis à une échelle de 1. Voici ce que nous faisons :

```
// Déclencher le zoom programmatique progZoom()
```

Écrivons-le. Il ne prendra aucun argument :

```
function progZoom() {
```

Nous définissons d'abord la transformation pour le `minZoom` que nous voulons zoomer en premier :

```
var zoomOutTransform = d3.zoomIdentity.scale(minZoom);
```

Dans les lignes suivantes, nous transformons notre `listenerRect` en une transition et appelons à nouveau `zoomTransform()`. En utilisant `.call()`, nous passons la transition que nous venons de construire comme premier argument et `zoomOutTransform`  la transformation `minZoom` que nous venons de sauvegarder :

```
listenerRect   .transition()   .duration(5000)   .call(zoom.transform, zoomOutTransform)     .on('end', zoomToNormal)
```

À la fin du zoom, nous appelons une fonction appelée `zoomToNormal`. Elle fait exactement ce que nous venons de faire, à part le zoom de transition vers une transformation d'identité :

```
function zoomToNormal() {   listenerRect     .transition()     .duration(3000)     .ease(d3.easeQuadInOut)     .call(zoom.transform, d3.zoomIdentity) }
```

Outre le zoom vers une transformation différente, nous définissons également une durée différente ainsi qu'une fonction d'assouplissement différente.

```
}
```

Et c'était notre première piste bonus. Passons à la piste deux

### Rendre notre visuel joli

Il est judicieux de rendre vos visuels corrects en noir et blanc d'abord (rose et blanc dans notre cas). Mais à la fin, une touche de peinture ne peut pas faire de mal. Pour en arriver là

![Image](https://cdn-media-1.freecodecamp.org/images/asjd4eAOr5k3eJSQ7sCp5pWQqDRg9qgsmqUm)
_Notre application finale [sans code](https://bl.ocks.org/larsvers/c894849af45ce94dc85d76467980f922/" rel="noopener" target="_blank" title="">avec</a> et <a href="https://bl.ocks.org/larsvers/raw/c894849af45ce94dc85d76467980f922/" rel="noopener" target="_blank" title=")_

nous devons seulement changer quelques choses, dont la lueur des planètes est probablement la plus élaborée. Regardons d'abord le reste :

Nous ajouterons un fond bleu foncé avec un dégradé radial se déplaçant dans le bleu foncé à partir d'un bleu légèrement plus clair. C'est une ligne dans notre CSS `body` :

```
body {   font-family: Avenir, sans-serif;  sans-serif;   font-size: 0.75rem;   margin: 0;   background: radial-gradient(#091C33, #091426); }
```

Nous changeons la couleur du texte et des lignes en un gris blanc cassé (`#ddd`), et au lieu des lignes pleines, nous rendons des lignes en pointillés avec de larges écarts :

```
.tick line, .lines {   stroke: #ddd;   stroke-width: 0.5;   shape-rendering: crispEdges;   stroke-dasharray: 1,5; }
```

Enfin, nous remplissons les planètes avec notre `deeppink` préféré et ajoutons la lueur. La lueur est un filtre SVG que nous appliquons à chaque planète. Je ne vais pas entrer dans les détails ici, mais vous pouvez trouver le code commenté [ici](https://github.com/larsvers/Understanding-Zoom/blob/master/zoom_step_07.html#L165-L207). En bref, nous épaississons un peu les planètes avant de les estomper avec un peu de flou gaussien. Nous remplissons le flou `deeppink` et admirons la lueur résultante. Le filtre obtient un id de `#soft-glow`, que nos planètes peuvent référencer avec l'attribut `filter` :

```
var planets = gPlanets.selectAll('.planet')     .data(data)  .enter().append('circle')     .attr('class', 'planet')     // ()     .attr('filter', 'url(#soft-glow)');
```

Et c'est tout !

Nous avons parcouru un long chemin, et espérons que vous comprenez maintenant un peu mieux le zoom D3. Nous avons examiné une recette courte que vous pouvez suivre avant et pendant le câblage de votre visuel avec tout zoom et défilement. Nous avons ensuite appliqué ce plan à un projet réel avec des orbes roses, en jouant avec le rendu de zoom géométrique et sémantique en SVG ainsi qu'en Canvas. En bonus, nous avons examiné le zoom programmatique et enfin rendu son visage subtilement rose encore plus rose. Quel plaisir !

Deux autres choses qui pourraient aider : une note rapide sur la mise à jour de votre zoom de D3 v3 à v4, et une liste de sources.

### Mise à jour du zoom de v3 à v4

En 2016 (comme dans de nombreuses générations auparavant), D3 v4 a remplacé v3 avec quelques changements importants mais cassants. Certains changements conceptuels, y compris le comportement de zoom, ont tenu les développeurs éveillés la nuit (y compris moi-même). Les changements sont cohérents et sensés, mais valent quelques notes supplémentaires qui pourraient vous aider à trouver le sommeil :

* Comme avec v3, le zoom dans v4 concerne simplement la translation x et y et l'échelle  les paramètres de transformation. Cela simplifie bien sûr la complexité de manière brutale, mais c'est un mantra que vous devriez essayer lorsque vous êtes bloqué.
* Les paramètres de transformation sont stockés avec la base de zoom dans v4, alors qu'ils étaient stockés avec le comportement dans v3. Le comportement passe maintenant simplement la transformation aux cibles. C'est bon à savoir lorsque nous voulons récupérer la transformation en dehors du gestionnaire de zoom.
* Le comportement v3 redimensionnait automatiquement votre échelle. Dans v4, vous devez redimensionner votre échelle manuellement dans la fonction de zoom, et mettre à jour toutes les formes et composants basés sur l'échelle. C'est un peu plus de travail, mais significativement moins de magie et une séparation plus claire des préoccupations.

### Sources [^](#07df) [^](#7362)

Il n'y a pas d'abondance de posts et tutoriels liés au zoom (v4) D3. Le manque de ceux-ci était une raison d'écrire ce tutoriel. Cependant, il y a quelques pépites de zoom ainsi que quelques matériaux supplémentaires liés à Canvas que vous pouvez consulter :

Ajouts d'articles :

* [Dépôt GitHub pour tout le code que nous avons parcouru dans cet article](https://github.com/larsvers/Understanding-Zoom)
* [Toutes les étapes que nous avons suivies ci-dessus en tant qu'applications fonctionnelles avec code](https://bl.ocks.org/larsvers/93b2f692217845d51fc75cd43c029303)

Tutoriels Zoom :

* [Zoom expliqué par Empty Pipes](http://emptypipes.org/2016/07/03/d3-panning-and-zooming/)
* [Zoom expliqué par Puzzlr](http://www.puzzlr.org/zoom-in-d3-v4/)
* [Zoom avec React et D3](https://swizec.com/blog/two-ways-build-zoomable-dataviz-component-d3-zoom-react/swizec/7753)

Technologie Zoom :

* [Exemples de zoom de Mike Bostock](https://bl.ocks.org/mbostock/3680958)
* [Zoom Géométrique vs Sémantique](http://infovis-wiki.net/index.php/Semantic_Zoom)
* [Référence de l'API Zoom D3 v4](https://github.com/d3/d3-zoom)

Canvas :

* [D3 et Canvas (référence éhontée à soi-même)](https://medium.freecodecamp.org/d3-and-canvas-in-3-steps-8505c8b27444)
* [Plus de D3 et Canvas](https://www.visualcinnamon.com/2015/11/learnings-from-a-d3-js-addict-on-starting-with-canvas.html)
* [Et encore plus de D3 et Canvas](https://bocoup.com/blog/2d-picking-in-canvas)

![Image](https://cdn-media-1.freecodecamp.org/images/aMyKkFc-nUbdJzE-WYTHwbfBFKB71EcFMXuj)

J'espère vraiment que vous avez apprécié la lecture de ceci. Applaudissez si vous voulez faire passer le mot, suivez-moi sur [Twitter](https://twitter.com/lars_vers) et [dites bonjour](mailto:lars@datamake.io?Subject=Hello) pour soit simplement dire bonjour ou me parler d'autres façons de zoomer.

La connaissance est partielle et nous sommes tous ici pour apprendre

_Publié à l'origine sur [www.datamake.io](http://www.datamake.io/blog/d3-zoom)._