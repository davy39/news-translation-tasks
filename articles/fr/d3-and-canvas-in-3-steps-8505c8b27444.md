---
title: D3 et Canvas en 3 étapes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-18T05:32:17.000Z'
originalURL: https://freecodecamp.org/news/d3-and-canvas-in-3-steps-8505c8b27444
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KCOutWkXvU7YhGY2f76kfQ.jpeg
tags:
- name: D3
  slug: d3
- name: data visualization
  slug: data-visualization
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: D3 et Canvas en 3 étapes
seo_desc: 'By lars verspohl

  The bind, the draw and the interactivity


  Let’s say you’re building a data visualization using D3 and SVG. You may hit a ceiling
  when you try to display several thousand elements at the same time. Your browser
  may start to puff under...'
---

Par lars verspohl

#### La liaison, le dessin et l'interactivité

![Image](https://cdn-media-1.freecodecamp.org/images/LJWqERx6v-qDQFc5jb7w2gFCP3YKaNuU36AA)

Disons que vous construisez une visualisation de données en utilisant [D3](https://d3js.org/) et [SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics). Vous pourriez rencontrer un plafond lorsque vous essayez d'afficher plusieurs milliers d'éléments en même temps. Votre navigateur pourrait commencer à s'essouffler sous le poids de tous ces [éléments DOM](https://css-tricks.com/dom/).

Eh bien, voici [HTML5 Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial) à la rescousse ! Il est beaucoup plus rapide, donc il peut résoudre les problèmes d'essoufflement de votre navigateur.

Mais vous pourriez rapidement vous sentir découragé. Parce que D3 et Canvas fonctionnent un peu différemment de D3 et SVG — surtout lorsqu'il s'agit de dessiner et d'ajouter de l'interactivité.

Mais ne craignez rien — ce n'est pas si compliqué. Toute expérience que vous avez eue avec la construction de visuels avec D3 et SVG — ou l'approche de D3 avec un autre moteur de rendu — vous aidera énormément.

Ce tutoriel s'appuie sur les épaules de géants qui ont déjà bien couvert Canvas. J'ai appris ces trois tutoriels par cœur et je vous recommande de faire de même :

* [Working with D3.js and Canvas: When and How](https://bocoup.com/weblog/d3js-and-canvas) d'Irene Ros
* [Needles, Haystacks, and the Canvas API](https://bocoup.com/weblog/2d-picking-in-canvas) de Yannick Assogba
* [Learnings from a D3.js addict on starting with Canvas](http://www.visualcinnamon.com/2015/11/learnings-from-a-d3-js-addict-on-starting-with-canvas.html) de Nadieh Bremer

Alors pourquoi continuer à lire ceci, alors ? Eh bien, lorsque je veux apprendre quelque chose de nouveau, cela m'aide beaucoup de regarder le même sujet sous des angles légèrement différents. Et ce tutoriel _est_ un angle légèrement différent.

De plus, ce tutoriel couvre les trois étapes clés : **liaison des données**, **dessin des éléments**, et **ajout d'interactivité** — et il fait tout cela en une seule fois, avec un **manuel étape par étape** pour vous mettre en route.

### Que construisons-nous ?

![Image](https://cdn-media-1.freecodecamp.org/images/lYZIDOUAORE42uN6Xx872jkaX1iG3Lx2TTJ3)
_Une grille de jolies couleurs_

Une grille de (nombreux) carrés. Leurs couleurs n'ont pas de signification profonde mais ne sont-elles pas jolies ? Le point important est que vous pouvez la mettre à jour (pour couvrir la liaison et la mise à jour des données), qu'elle a de nombreux éléments (jusqu'à 10 000 afin que canvas soit rentable), et que vous pouvez survoler chaque carré pour afficher des informations spécifiques au carré (interactivité). Vous pouvez jouer avec [ici en plein écran](http://bl.ocks.org/larsvers/raw/d187337850d58a444082841c739985ca/) ou [ici avec tout le code](http://blockbuilder.org/larsvers/d187337850d58a444082841c739985ca)

### Le modèle mental

Avant de plonger réellement, faisons rapidement un pas en arrière et comprenons conceptuellement ce que nous faisons lorsque nous créons des éléments avec D3 pour les dessiner à l'écran. Passez cette partie si vous voulez simplement faire des choses.

La première étape lors de l'utilisation de D3 n'implique généralement pas de dessin — elle implique la préparation de tous vos éléments que vous voulez dessiner. C'est un peu comme construire des LEGO. Vous pouvez ouvrir la boîte et commencer à construire quelque chose ou vous pouvez regarder le manuel d'abord et le construire selon le plan. Le manuel est votre modèle mental, un plan ou une recette de ce que vous voulez construire.

![Image](https://cdn-media-1.freecodecamp.org/images/7BFtJOkOIVODiluRi9004udf0p2F-6zS9C5o)
_Un modèle mental devenu matériel (Mike, 2009 [https://creativecommons.org/licenses/by/2.0/](https://creativecommons.org/licenses/by/2.0/" rel="noopener" target="_blank" title="))_

Quel est le modèle de D3 ? En plus du grand nombre de fonctions et méthodes utiles qui calculent les positions, remodèlent les ensembles de données (les mises en page) et génèrent des fonctions qui dessinent, par exemple, des chemins pour nous, D3 a un modèle pour la façon dont la vie des éléments devrait évoluer à l'écran. Il a une certaine façon de penser au cycle de vie de chaque élément.

De manière moins éthérée, vous injectez des données dans un DOM encore inexistant, et D3 crée de nouveaux éléments de votre choix selon les données que vous injectez. Habituellement un élément par point de données. Si vous voulez injecter de nouvelles données dans le DOM, vous pouvez le faire et D3 identifie quels éléments doivent être nouvellement créés, quels éléments sont autorisés à rester et quels éléments doivent faire leurs valises et quitter l'écran.

D3 est généralement utilisé en conjonction avec SVG ou parfois avec des éléments HTML. Dans ce cas orthodoxe, vous pouvez voir les données dans le DOM lorsque vous choisissez de les regarder à travers la console, par exemple. Vous pouvez les attraper, vous pouvez les déplacer vers le haut ou vers le bas du DOM et vous pouvez — ce qui est important — ajouter de l'interactivité à chaque élément que vous souhaitez montrer, par exemple, une info-bulle.

Mais — du côté négatif — vous ne pouvez pas montrer beaucoup d'éléments. Pourquoi ? Parce que plus vous poussez d'éléments dans le DOM, plus le navigateur doit travailler dur pour les afficher tous. Laissez-les aussi se déplacer et le navigateur doit les recalculer constamment. Plus le navigateur s'épuise, plus votre taux de rafraîchissement ou FPS (Frames Per Second) est bas, ce qui mesure combien de frames le navigateur peut peindre chaque seconde. Un taux de rafraîchissement de 60 est bon et permet une expérience fluide tant qu'aucune frame n'est manquée — un taux de rafraîchissement de moins de 30 peut égaler une expérience saccadée. Donc lorsque vous voulez montrer plus d'éléments, vous pouvez revenir à canvas.

Pourquoi canvas ? Canvas est un élément HTML5 qui vient avec sa propre API pour peindre dessus. Tous les éléments dessinés sur l'élément canvas ne se manifesteront pas dans le DOM et économiseront beaucoup de travail pour le navigateur. Ils sont dessinés en [mode immédiat](https://en.wikipedia.org/wiki/Immediate_mode_%28computer_graphics%29). Cela signifie que les éléments rendus ne seront pas sauvegardés dans le DOM mais vos instructions les dessineront directement sur une frame particulière. Le DOM ne connaît que l'élément canvas ; tout ce qui est dessus n'est qu'en mémoire. Si vous voulez changer vos éléments canvas, vous devez redessiner la scène pour la frame suivante.

Le problème avec cela est bien sûr que vous ne pouvez pas communiquer directement avec ces éléments non matériels vivant en mémoire. Vous devez trouver un moyen de leur parler indirectement. C'est là que le modèle D3 intervient ainsi que des éléments DOM personnalisés ou 'virtuels'. Ce que vous ferez en principe est :

1. Lier vos données à des éléments DOM personnalisés. Ils ne vivent pas dans le DOM mais seulement en mémoire (dans un DOM 'virtuel') et décrivent le cycle de vie de ces éléments de manière connue de D3.
2. Utiliser canvas pour dessiner ces éléments.
3. Ajouter de l'interactivité avec une technique appelée 'picking'.

Faisons-le.

### Les données

Avant de commencer à coder, produisons quelques données. Disons que vous voulez 5 000 points de données. Donc créons un tableau avec 5 000 éléments, chacun étant un objet avec une seule propriété value portant l'index de l'élément. Voici comment le créer avec `d3.range()`. `[d3.range()](https://github.com/d3/d3-array/blob/master/README.md#range)` est une fonction utilitaire D3, qui crée un tableau basé sur son argument :

```
var data = [];
```

```
d3.range(5000).forEach(function(el) {
```

```
  data.push({ value: el }); 
```

```
});
```

Voici à quoi ressemblent les données dans la console

![Image](https://cdn-media-1.freecodecamp.org/images/9KKliKgPxgMlDmp4MzZQQ5-RXRAvUVbUzkWm)

Des frissons !

### Le conteneur canvas et ses outils

L'élément canvas est un élément HTML. Conceptuellement, il est très similaire à tout élément parent SVG, que j'ajoute au moins habituellement à une simple div conteneur comme dans :

```
<div id="container"></div>
```

Donc, ajoutons-le à votre conteneur avec D3 comme dans...

```
var width = 750, height = 400;
```

```
var canvas = d3.select('#container')  .append('canvas')  .attr('width', width)  .attr('height', height);
```

```
var context = canvas.node().getContext('2d');
```

Vous devez également ajouter le contexte, qui est la boîte à outils du canvas. La variable de contexte est à partir de maintenant l'objet portant toutes les propriétés et méthodes, les pinceaux et couleurs dont vous avez besoin pour dessiner sur le canvas. Sans le contexte, l'élément canvas resterait vide et blanc. C'est tout ce dont vous avez besoin pour la configuration — un canvas et ses outils...

![Image](https://cdn-media-1.freecodecamp.org/images/Qf47F2fKGkcjFa6czkWrFEllQvSVtzkgIOKh)
_Base par Stilfehler — Travail personnel, CC BY-SA 3.0, [https://creativecommons.org/licenses/by/2.0/](https://commons.wikimedia.org/w/index.php?curid=5899171" rel="noopener" target="_blank" title="">https://commons.wikimedia.org/w/index.php?curid=5899171</a>; Lego bleu par David Lofink, 2008 <a href="https://creativecommons.org/licenses/by/2.0/" rel="noopener" target="_blank" title=")_

### Le HTML

...est simple. La structure HTML principale de votre site sera :

```
<!-- Un titre --><h3>Grilles colorées</h3>
```

```
<!-- Un champ de saisie avec une valeur par défaut. --> <input type="text" id="text-input" value="5000">
```

```
<!-- Une explication... --> <div id="text-explain">...prend des nombres entre 1 et 10k</div>
```

```
<!-- ...et un conteneur pour l'élément canvas. --> <div id="container"></div>
```

### La structure JavaScript

Au niveau supérieur, vous n'avez besoin que de 2 fonctions :

```
databind(data) {
```

```
  // Lier les données aux éléments personnalisés.
```

```
}
```

```
draw() {
```

```
  // Dessiner les éléments sur le canvas.
```

```
}
```

Assez simple jusqu'à présent.

### Lier les éléments

Pour lier les données aux éléments, vous créez d'abord un élément de base pour tous vos éléments personnalisés que vous allez produire et dessiner. Si vous connaissez bien D3, pensez-y comme un remplacement de l'élément SVG :

```
var customBase = document.createElement('custom');
```

```
var custom = d3.select(customBase); // C'est votre remplacement SVG et le parent de tous les autres éléments
```

Ensuite, vous ajoutez quelques paramètres pour votre grille. En bref, ces paramètres vous permettent de dessiner une grille de carrés. 100 carrés forment un 'parcelle' et il y a un saut de ligne après 10 parcelles (ou après 1 000 carrés). Vous pouvez ajuster cela pour différentes 'parcellisations' des carrés ou différentes ruptures de ligne. Ou simplement ne pas vous en soucier. Je suggère cette dernière option...

```
// Paramètres pour une grille avec 10 cellules dans une ligne, // 100 cellules dans un bloc et 1000 cellules dans une ligne.
```

```
var groupSpacing = 4; var cellSpacing = 2; var offsetTop = height / 5; var cellSize = Math.floor((width - 11 * groupSpacing) / 100) - cellSpacing;
```

Maintenant, commençons la mission de liaison des données. Commençons par les nécessités et créons une échelle de couleurs que vous appliquerez à vos carrés un peu plus tard.

```
function databind(data) {
```

```
// Obtenez une échelle pour les couleurs - pas essentielle mais sympa.
```

```
colourScale = d3.scaleSequential(d3.interpolateSpectral)                      .domain(d3.extent(data, function(d) { return d; }));
```

Maintenant, joignons vos données au 'SVG de remplacement' que vous avez appelé `custom` ci-dessus et ajoutons des éléments personnalisés encore inexistants avec la classe `.rect`

```
var join = custom.selectAll('custom.rect')  .data(data);
```

Vous entrez dans les éléments personnalisés (rappelez-vous que rien n'entre dans le DOM, tout cela est en mémoire).

```
var enterSel = join.enter()  .append('custom')  .attr('class', 'rect')  .attr("x", function(d, i) {    var x0 = Math.floor(i / 100) % 10, x1 = Math.floor(i % 10);         return groupSpacing * x0 + (cellSpacing + cellSize) * (x1 + x0 * 10); })  .attr("y", function(d, i) {  var y0 = Math.floor(i / 1000), y1 = Math.floor(i % 100 / 10);   return groupSpacing * y0 + (cellSpacing + cellSize) * (y1 + y0 * 10); })  .attr('width', 0)  .attr('height', 0);
```

Lorsque qu'un élément entre dans votre modèle, vous lui donnez simplement une position x et y ainsi qu'une largeur et une hauteur de 0, que vous changerez dans la prochaine sélection de mise à jour...

Vous fusionnez la sélection d'entrée dans la sélection de mise à jour et définissez tous les attributs pour la sélection de mise à jour et d'entrée. Cela inclut une valeur de largeur et de hauteur ainsi qu'une couleur de l'échelle de couleurs que vous avez construite précédemment :

```
join   .merge(enterSel)  .transition()  .attr('width', cellSize)  .attr('height', cellSize)  .attr('fillStyle', function(d) { return colourScale(d); });
```

Deux choses à noter sur cette dernière ligne. Lorsque vous travaillez avec SVG, cette ligne serait

```
.style('color', function(d) { return colourScale(d); })
```

Mais avec canvas, vous utilisez `.attr()`. Pourquoi ? Votre principal intérêt ici est de trouver un moyen sans douleur de transférer certaines informations spécifiques à l'élément. Ici, vous voulez transférer une chaîne de couleur de `databind()` à la fonction `draw()`. Vous utilisez l'élément simplement comme un vaisseau pour transporter vos données là où elles sont rendues sur le canvas.

C'est une distinction très importante : lorsque vous travaillez avec SVG ou HTML, vous pouvez lier des données aux éléments et dessiner ou appliquer des styles aux éléments en une seule étape. Dans canvas, vous avez besoin de deux étapes. D'abord, vous liez les données, puis vous dessinez les données. Vous ne pouvez pas styliser les éléments pendant la liaison. Ils n'existent qu'en mémoire et canvas ne peut pas être stylisé via les propriétés de style CSS, ce qui est exactement ce que vous accédez lorsque vous utilisez `.style()`.

Au début, cela peut sembler limitant car vous pouvez faire moins en une seule étape, mais c'est conceptuellement presque plus propre et cela vous donne aussi une certaine liberté. `.attr()` nous permet d'envoyer n'importe quelle paire clé-valeur en voyage. Vous pourriez utiliser d'autres méthodes comme la propriété `.dataset` HTML par exemple, mais `.attr()` fera très bien l'affaire.

Remarquez que nous ne disons pas `color` mais `fillStyle`. Pour être honnête, vous pourriez utiliser `color` ou vous pourriez utiliser `chooChooTrain` ici. Vous devriez simplement vous en souvenir lorsque vous récupérez l'information plus tard pendant le dessin. Cependant, comme canvas utilise une propriété appelée `fillStyle` pour styliser les éléments, cela semble plus approprié dans ce cas.

Enfin, vous définissez également la sélection de sortie, en décidant ce qui doit arriver aux éléments sortants.

```
var exitSel = join.exit()  .transition()  .attr('width', 0)  .attr('height', 0)  .remove();
```

C'est tout ! Vous pouvez fermer votre fonction `databind()` et passer à...

```
} // databind()
```

Ce n'est pas vraiment effrayant en venant de D3 car c'est presque exactement la même chose. Vous avez maintenant créé avec succès votre modèle de données, la façon dont l'application pensera aux données. Chaque élément obtiendra les propriétés dont il a besoin pour être dessiné via les fonctions `.attr()` et chaque élément se verra attribuer un état de cycle de vie en fonction des données injectées. Notre modèle D3 standard.

### Dessiner les éléments

![Image](https://cdn-media-1.freecodecamp.org/images/ZaCpM7PV8TG1tI1LzZ4n5d6bsxNiBQNxDDYk)
_Par Kristina Alexanderson, 2011 [https://creativecommons.org/licenses/by-nc-nd/2.0/](https://creativecommons.org/licenses/by-nc-nd/2.0/" rel="noopener" target="_blank" title=")_

Maintenant, vous devez écrire la fonction de dessin pour obtenir les éléments à l'écran. Notons simplement ici que rien ne s'est encore passé. Vous n'avez pas encore appelé `databind()` car vous devez trouver un moyen de le dessiner sur le canvas d'abord. Alors, voici... La fonction `draw()` n'a pas besoin de prendre d'arguments dans ce cas :

```
function draw() {
```

Comme mentionné brièvement ci-dessus, vous devez prendre soin de nettoyer le canvas chaque fois que vous dessinez à nouveau. Le DOM est matériel, en ce sens que lorsque vous dessinez un élément rect dessus et que vous changez sa valeur x, il se déplacera dans la direction x et le DOM prendra soin de ce déplacement (ou de la re-peinture) automatiquement.

Si vous déplacez un rect de x = 0 à x = 1 à un certain moment (après un appui sur un bouton par exemple), le navigateur déplacera le rect de 0 à 1 en un seul tick ou une peinture de frame (qui dure environ 16 ms). Si vous le déplacez de 0 à 10, il le fera en un temps dépendant de la durée que vous avez demandée pour cette transition, peut-être 1 pixel par tick ou peut-être 8 pixels par tick (pour plus d'informations, lisez [cet article de blog](https://www.html5rocks.com/en/tutorials/speed/unnecessary-paints/)).

Mais il dira au pixel à 0 que le rect a disparu et au pixel à 1 qu'il y a un rect maintenant. Canvas ne fait pas cela. Vous devez dire à canvas quoi peindre, et si vous peignez quelque chose de nouveau, vous devez lui dire de supprimer la peinture précédente.

Alors, commençons par nettoyer tout ce qui pourrait être sur le canvas avant de dessiner. Voici comment :

```
context.clearRect(0, 0, width, height); // Nettoyer le canvas.
```

Simple.

Maintenant, vous...

1. ...obtenez tous les éléments afin de
2. parcourir tous les éléments et
3. prendre les informations que vous avez stockées dans la fonction `databind()` pour dessiner l'élément :

```
// Dessiner chaque élément personnalisé individuel avec leurs propriétés.
```

```
var elements = custom.selectAll('custom.rect');// Prendre tous les éléments auxquels vous avez lié des données dans la fonction databind().
```

```
elements.each(function(d,i) { // Pour chaque élément virtuel/personnalisé...
```

```
  var node = d3.select(this);   // C'est chaque élément individuel dans la boucle.     context.fillStyle = node.attr('fillStyle');   // Ici, vous récupérez la couleur de l'individu en mémoire et définissez le fillStyle pour la peinture du canvas
```

```
  context.fillRect(node.attr('x'), node.attr('y'), node.attr('width'), node.attr('height'));  // Ici, vous récupérez la position du nœud et l'appliquez à la fonction de contexte fillRect qui remplira et peindra le carré.
```

```
}); // Parcourir chaque élément.
```

Et c'est tout ! Vous pouvez fermer la fonction `draw()`

```
} // draw()
```

Lorsque j'ai commencé avec canvas après un certain temps de vouloir plonger dedans, cette simplicité a vraiment boosté mon moral.

Cependant, rien ne s'est encore passé dans le navigateur. Nous avons les outils dans `databind()` et la fonction `draw()`, mais rien n'a encore été dessiné. Comment faites-vous cela ? Si vous vouliez simplement dessiner un visuel ou une image statique, vous appelez simplement :

```
databind(data);
```

```
draw();
```

Cela lierait les données aux éléments personnalisés, qui vivraient en mémoire et les dessinerait — une fois !

Mais vous avez des transitions. Rappelez-vous ci-dessus : lorsque vous avez écrit la fonction `databind()`, vous avez fait la transition de la largeur et de la hauteur de la cellule de 0 à leur taille ainsi que la couleur du noir (par défaut) à la couleur respective de l'élément. Une transition D3 par défaut dure 250 millisecondes, donc vous devez redessiner les carrés de nombreuses fois dans ces 250 ms afin d'obtenir une transition fluide. Comment faites-vous cela ?

C'est à nouveau simple. Vous appelez simplement `databind(data)` pour créer nos éléments personnalisés avant d'appeler `draw()` de manière répétée pendant toute la durée de la transition. Donc dans notre cas, au moins 250 ms. Vous pourriez utiliser `setInterval()` pour cela, mais nous devrions vraiment utiliser `requestAnimationFrame()` afin d'être aussi performant que possible (pour plus d'informations, lisez [cet article](https://css-tricks.com/using-requestanimationframe/)). Il y a quelques façons de l'utiliser, mais en restant dans l'esprit de D3, je suggère d'utiliser `d3.timer()` qui implémente `requestAnimationFrame()` ainsi qu'être simple à utiliser. Alors, voici :

```
// === Premier appel === //
```

```
databind(d3.range(value)); // Construire les éléments personnalisés en mémoire.
```

```
var t = d3.timer(function(elapsed) {
```

```
  draw();
```

```
  if (elapsed > 300) t.stop();
```

```
}); // Timer exécutant la fonction draw de manière répétée pendant 300 ms.
```

`d3.timer()` appelle le callback de manière répétée jusqu'à ce que `elapsed` (qui est le temps écoulé en millisecondes depuis l'instantiation) dépasse 300 et ensuite le timer est arrêté. Dans ces 300 millisecondes, il exécute `draw()` à chaque tick (environ chaque 16 ms). `draw()` regarde ensuite les attributs de chaque élément et les dessine en conséquence.

C'est ainsi qu'une transition fonctionne dans canvas. Vous appelez la fonction de dessin juste après la fonction de liaison de nombreuses fois. Tout ce que votre modèle D3 est configuré pour transitionner (positions, couleurs, tailles) sera redessiné de nombreuses fois avec de petits changements incrémentiels pour chaque dessin.

Notez que `draw()` doit venir juste après la fonction `databind()`. Vous ne pourriez pas demander à la machine d'exécuter `databind()`, puis de faire autre chose pendant une seconde et ensuite d'appeler `draw()`. Parce qu'après 1 seconde, les états transitionnés calculés par votre fonction `databind()` ont déjà tous transitionné. Fini, terminé et oublié.

C'est tout ! Vous avez lié des données à des éléments personnalisés et vous les avez dessinés sur le canvas.

#### Laissez l'utilisateur mettre à jour le nombre de carrés

Pour donner à l'utilisateur la chance de répéter cet exploit avec un nombre personnalisé d'éléments (ok, semi-personnalisé avec un maximum de 10 000), vous ajoutez l'écouteur et le gestionnaire suivant à votre boîte de saisie de texte :

```
// === Écouteurs/gestionnaires === //
```

```
d3.select('#text-input').on('keydown', function() {
```

```
if (d3.event.keyCode === 13) { // Ne faire quelque chose que si l'utilisateur appuie sur entrée (code clé 13).
```

```
  if (+this.value < 1 || +this.value > 10000) {   // Si l'utilisateur va en dessous de 1 ou au-dessus de 10k...         d3.select('#text-explain').classed('alert', true);     // ... mettre en surbrillance la note sur la plage et retourner.
```

```
    return;
```

```
  } else {   // Si l'utilisateur tape un nombre raisonnable...
```

```
    d3.select('#text-explain').classed('alert', false);     // ... supprimer les couleurs d'alerte potentielles de la note...
```

```
    value = +this.value; // ... définir la valeur...
```

```
    databind(d3.range(value)); // ... et lier les données.
```

```
    var t = d3.timer(function(elapsed) {
```

```
      draw();        if (elapsed > 300) t.stop();
```

```
    }); // Timer exécutant la fonction draw de manière répétée pendant 300 ms.     } // Si l'utilisateur appuie sur entrée.
```

```
}); // Écouteur/gestionnaire de saisie de texte
```

La voici à nouveau, notre grille colorée de carrés canvas, prête à être mise à jour et redessinée :

![Image](https://cdn-media-1.freecodecamp.org/images/-FueZaUWkrLNINguKlHuQ1P6YMLlzz4B4QkQ)

### Interactivité

Le plus grand 'problème' avec canvas en comparaison à SVG ou HTML est qu'il n'y a pas d'éléments matériels vivant dans le DOM. S'il y en avait, vous pourriez simplement enregistrer des écouteurs sur les éléments et ajouter des gestionnaires aux écouteurs. Par exemple, vous pouvez déclencher un survol de souris sur un élément `rect` SVG et chaque fois que l'écouteur se déclenche, vous pourriez faire quelque chose au rect. Comme montrer les valeurs de données stockées avec le `rect` dans une info-bulle.

Avec canvas, vous devez trouver un autre moyen de faire entendre un événement sur nos éléments canvas. Heureusement, il y a un certain nombre de personnes intelligentes qui ont pensé à une méthode indirecte mais logique.

Alors, quelle interactivité voulons-nous ? Comme dit ci-dessus, allons-y pour une info-bulle et supposons que vous voulez montrer l'index du carré dans une info-bulle dès que vous survolez l'élément. Pas très excitant, mais l'important est que vous pouvez accéder aux données liées à l'élément en le survolant.

#### Picking

Il y a quelques étapes impliquées (toutes logiques cependant). Mais en bref, vous allez construire deux canvases pour y parvenir. Un **canvas principal** qui produit notre visuel et un **canvas caché** (comme dans nous ne pouvons pas le voir) qui produit le même visuel. La clé ici est que tous les éléments sur le deuxième canvas seront à la position exacte par rapport à l'origine du canvas par rapport au premier canvas. Donc le carré 1 commence à 0,0 sur le canvas principal ainsi que sur le canvas caché. Le carré 2 commence à 8,0 sur le canvas principal ainsi que sur le canvas caché et ainsi de suite.

Il n'y a qu'une seule différence importante. Chaque élément sur le canvas caché recevra une couleur unique. Nous allons créer un objet (ou plutôt un [tableau associatif](https://en.wikipedia.org/wiki/Associative_array) ou _map_ pour faire court) qui lie chaque couleur unique aux données de chaque élément.

Pourquoi ? Parce que ensuite nous attachons un écouteur de mouvement de souris au canvas principal pour récupérer un flux de positions de souris. À chaque position de souris, nous pouvons utiliser une méthode propre au canvas pour 'picking' la couleur à cette position exacte. Ensuite, nous cherchons simplement la couleur dans notre tableau associatif et nous avons les données ! Et nous volons...

![Image](https://cdn-media-1.freecodecamp.org/images/19HOxzrPQbTQEcdVlJxpnid99YSrjfbozdxy)
_Par Kenny Louie, 2010 [https://creativecommons.org/licenses/by/2.0/](https://creativecommons.org/licenses/by/2.0/" rel="noopener" target="_blank" title=")_

Vous pourriez dire 'eh bien, mes carrés ont déjà une couleur unique, je peux les utiliser ?' Et en effet, vous pourriez les utiliser. Cependant, votre interactivité serait compromise dès que vous décideriez de priver vos carrés de leurs couleurs. Donc vous devriez vous assurer d'avoir toujours un canvas — le canvas caché — qui a un ensemble garanti de couleurs uniques pour les carrés.

Appliquons cette technique étape par étape. Le code que vous avez construit jusqu'à présent peut rester tel quel — vous ajoutez simplement au fur et à mesure.

#### 1. Préparer le canvas caché

Tout d'abord, créons le canvas caché qui abritera notre visuel avec une couleur unique par carré.

1.1 Créer l'élément canvas caché et définir son CSS sur `{ display: none; }`.

```
// Renommer le canvas principal et ajouter une classe 'mainCanvas'.
```

```
var mainCanvas = d3.select('#container')  .append('canvas')  .classed('mainCanvas', true)  .attr('width', width) .attr('height', height); // nouveau ----------------------------------- 
```

```
// Ajouter le canvas caché et lui donner la classe 'hiddenCanvas'.
```

```
var hiddenCanvas = d3.select('#container')  .append('canvas')  .classed('hiddenCanvas', true)   .attr('width', width)   .attr('height', height);
```

En fait, je ne vais pas cacher le canvas dans cet exemple pour montrer ce qui se passe. Mais pour le faire, ajoutez simplement `.hiddenCanvas { display: none; }` à votre CSS et le tour est joué.

1.2 Construire la variable de contexte dans la fonction `draw()` et passer deux arguments à la fonction : le canvas ainsi qu'un booléen appelé 'hidden' déterminant quel canvas nous construisons (hidden = true || false) comme dans :

```
function draw(canvas, hidden) {
```

1.3 Vous devez maintenant adapter toutes les fonctions de dessin pour inclure les deux nouveaux arguments `draw()`. Donc à partir de maintenant, vous n'appelez plus simplement `draw()`, vous appelez soit `draw(mainCanvas, false)` soit `draw(hiddenCanvas, true)`

#### 2. Appliquer des couleurs uniques aux éléments cachés et les mapper

Ici, cher lecteur, vient la partie clé de notre opération, le moteur de notre camion, l'épice dans notre soupe.

![Image](https://cdn-media-1.freecodecamp.org/images/DOlN5RCi8jbLQTNI821trNukfFg4PVtBjiHC)
_Par Andrew Becraft, 2007 [https://creativecommons.org/licenses/by-nc-sa/2.0/](https://creativecommons.org/licenses/by-nc-sa/2.0/" rel="noopener" target="_blank" title=")_

2.1 Inclure une fonction pour générer une nouvelle couleur unique chaque fois qu'elle est appelée (via [Stack Overflow](http://stackoverflow.com/a/15804183))

```
// Fonction pour créer de nouvelles couleurs pour le picking.
```

```
var nextCol = 1;
```

```
function genColor(){     var ret = [];
```

```
  if(nextCol < 16777215){         ret.push(nextCol & 0xff); // R     ret.push((nextCol & 0xff00) >> 8); // G     ret.push((nextCol & 0xff0000) >;> 16); // B
```

```
    nextCol += 1;     }
```

```
var col = "rgb(" + ret.join(',') + ")";
```

```
return col;
```

```
}
```

`genColour()` produit une chaîne de définition de couleur sous la forme rgb(0,0,0). Chaque fois qu'elle est appelée, elle incrémente la valeur R de un. Une fois qu'elle atteint 255, elle incrémente la valeur G de 1 et réinitialise la valeur R à 0. Une fois qu'elle atteint r(255,255,0), elle incrémente la valeur B de 1, réinitialisant les valeurs R et G à 0, et ainsi de suite.

Donc au total, vous pouvez avoir 256*256*256 = 16.777.216 éléments pour conserver une couleur unique. Cependant, je peux vous assurer que votre navigateur mourra avant. Même avec canvas (tutoriel webGL à suivre).

2.2 Créer l'objet map qui gardera une trace de quel élément personnalisé a quelle couleur unique :

```
var colourToNode = {}; // Map pour suivre la couleur des nœuds.
```

Vous pouvez ajouter la fonction `genColour()` où vous voulez dans votre script, tant qu'elle est en dehors de la portée des fonctions `databind()` et `draw()`. Mais notez que votre variable map doit être créée avant et au-delà de la portée de la fonction `databind()`.

2.3 Ajouter une couleur unique à chaque élément personnalisé comme par exemple `.attr('fillStyleHidden')` et   
2.4 construire l'objet map pendant la création des éléments

Ici, vous utiliserez votre 'canon à couleurs' `genColour()` dans notre fonction `databind()` lors de l'attribution du `fillStyle` à nos éléments. Comme vous avez également accès à chaque point de données pendant qu'il est lié à chaque élément, vous pouvez rassembler couleur et données dans votre map `colourToNode`.

```
join   .merge(enterSel)   .transition()   .attr('width', cellSize)   .attr('height', cellSize)   .attr('fillStyle', function(d) {     return colorScale(d.value);   });
```

```
  // nouveau -----------------------------------------------------         .attr('fillStyleHidden', function(d) { 
```

```
    if (!d.hiddenCol) {
```

```
      d.hiddenCol = genColor();       colourToNode[d.hiddenCol] = d;
```

```
    }
```

```
    // Ici, vous (1) ajoutez une couleur unique en tant que propriété à chaque élément     // et (2) mappez la couleur au nœud dans la map colourToNode.
```

```
    return d.hiddenCol;
```

```
});
```

2.5 Vous pouvez maintenant colorier les éléments en fonction du canvas que la fonction `draw()` rend. Vous ajoutez une condition sur le `fillStyle` dans la fonction `draw()` appliquant les couleurs pour notre visuel au canvas principal et les couleurs uniques au canvas caché. C'est une simple ligne :

```
context.fillStyle = hidden ? node.attr('fillStyleHidden') : node.attr('fillStyle');
```

```
// La couleur du nœud dépend du canvas que vous dessinez.
```

Le canvas principal a toujours le même aspect bien sûr :

![Image](https://cdn-media-1.freecodecamp.org/images/iiJNAhyR0ReK2tU1aoHuRjnODkWsgr83906J)

Ajoutons enfin un peu d'interactivité et commençons par dessiner le canvas caché chaque fois que nous déplaçons la souris sur notre canvas principal.

#### 3. Ramasser les couleurs avec la souris

3.1 Tout d'abord, enregistrez simplement un écouteur sur le canvas principal, à l'écoute des événements de mouvement de la souris.

```
d3.select('.mainCanvas').on('mousemove', function() {
```

```
});
```

Pourquoi mousemove ? Comme vous ne pouvez pas enregistrer d'écouteurs avec des carrés individuels mais devez utiliser tout le canvas, vous ne pourrez pas travailler avec des événements mouseover ou -out car ils ne se déclencheront que lorsque vous entrez dans le canvas, pas dans les éléments. Afin d'obtenir la position de la souris sur votre canvas, vous pouvez faire mousemove ou click/mousedown.

```
d3.select('.mainCanvas').on('mousemove', function() {
```

```
  draw(hiddenCanvas, true); // Dessiner le canvas caché.
```

```
});
```

De cette façon, la première chose que notre utilisateur déclenche en passant la souris sur le canvas principal est de créer sans le savoir le canvas caché. Comme dit, en production ce canvas serait caché, mais à des fins éducatives, nous voulons le voir et en effet, déclencher le dessin du canvas caché lorsque la souris se déplace sur le canvas principal comme suit :

Les couleurs sur le canvas principal vont du noir au rouge, de rgb(0,0,0) à rgb(255,0,0) et ensuite il semble que la même plage du noir au rouge soit répétée. Cependant, maintenant la couleur va d'un noir légèrement plus vert, précisément de rgb(0,1,0) à rgb(255,1,0) :

![Image](https://cdn-media-1.freecodecamp.org/images/jypEjz7sRIAVtg1uf7YLNbza2ban7FkvAYKF)

En zoomant sur les premiers centaines de carrés, voici les couleurs du premier, du 256ème et du 257ème carré :

![Image](https://cdn-media-1.freecodecamp.org/images/R3tNkcWdwboHcnNxeyNNlw3gV42GoMErCHSu)

3.3 Comme notre canvas caché est structurellement une copie carbone de notre canvas principal, tous les éléments du canvas caché seront à la même position que les éléments sur notre canvas principal. Donc, vous pouvez maintenant utiliser les positions x et y de la souris que vous collectez à partir de l'écouteur sur le canvas principal pour établir le même emplacement sur le canvas caché. De retour dans l'écouteur, vous ajoutez :

```
d3.select('.mainCanvas').on('mousemove', function() {       // Dessiner le canvas caché.  draw(hiddenCanvas, true);
```

```
  // Obtenir les positions de la souris à partir du canvas principal.  var mouseX = d3.event.layerX || d3.event.offsetX;   var mouseY = d3.event.layerY || d3.event.offsetY; });
```

Notez ici que nous prenons les propriétés `event.layerX` et `event.layerY` qui retournent la position de la souris incluant le défilement. [Cela peut casser](https://developer.mozilla.org/en/docs/Youb/API/UIEvent/layerX) donc utilisez offsetX comme solution de repli (ou utilisez simplement offsetX).

3.4 Le picking : Canvas permet grandement l'accès aux données de pixel sur lesquelles la souris survole avec la fonction `getImageData()` et sa propriété `.data`. En pleine floraison, cela ressemblera à :

`getImageData(posX, posY, 1, 1).data` .

Il retournera un tableau avec quatre nombres : le R, le G, le B et la valeur alpha. Comme vous avez diligemment construit la map `colourToNode` en attribuant les données de l'élément à chacune de ses couleurs cachées, vous pouvez maintenant accéder aux données de cet élément simplement en cherchant la couleur dans la map !

```
d3.select('.mainCanvas').on('mousemove', function() {
```

```
  // Dessiner le canvas caché.  draw(hiddenCanvas, true);
```

```
  // Obtenir les positions de la souris à partir du canvas principal.  var mouseX = d3.event.layerX || d3.event.offsetX;   var mouseY = d3.event.layerY || d3.event.offsetY;
```

```
// nouveau -----------------------------------------------
```

```
  // Obtenir la boîte à outils pour le canvas caché.  var hiddenCtx = hiddenCanvas.node().getContext('2d');
```

```
  // Choisir la couleur à partir de la position de la souris.   var col = hiddenCtx.getImageData(mouseX, mouseY, 1, 1).data; 
```

```
  // Puis transformer les valeurs en une chaîne que notre objet map peut lire.  var colKey = 'rgb(' + col[0] + ',' + col[1] + ',' + col[2] + ')';
```

```
  // Obtenir les données de notre map !   var nodeData = colourToNode[colKey];
```

```
  console.log(nodeData);
```

```
});
```

Et en effet, la journalisation de `nodeData` dans la console retourne un objet chaque fois que vous survolez un carré :

Les données par nœud montrent maintenant la `value` qui constitue les données originales ainsi que la clé `hiddenCol` montrant la couleur de ce nœud pour le canvas caché :

![Image](https://cdn-media-1.freecodecamp.org/images/ldW0tKW2CWZY5oMgBqQIDknGQ60lLb9eK3Iq)

3.5 Enfin — et c'est une formalité — vous ajoutez l'info-bulle

```
d3.select('.mainCanvas').on('mousemove', function() {
```

```
  // Dessiner le canvas caché.  draw(hiddenCanvas, true);
```

```
  // Obtenir les positions de la souris à partir du canvas principal.  var mouseX = d3.event.layerX || d3.event.offsetX;   var mouseY = d3.event.layerY || d3.event.offsetY;
```

```
  // Obtenir la boîte à outils pour le canvas caché.  var hiddenCtx = hiddenCanvas.node().getContext('2d');
```

```
  // Choisir la couleur à partir de la position de la souris.   var col = hiddenCtx.getImageData(mouseX, mouseY, 1, 1).data;
```

```
  // Puis transformer les valeurs en une chaîne que notre objet map peut lire.  var colKey = 'rgb(' + col[0] + ',' + col[1] + ',' + col[2] + ')';
```

```
  // Obtenir les données de notre map !   var nodeData = colourToNode[colKey];     console.log(nodeData);
```

```
  // nouveau -----------------------------------------------
```

```
  if (nodeData) {   // Montrer l'info-bulle uniquement lorsqu'il y a des nodeData trouvées par la souris
```

```
    d3.select('#tooltip')       .style('opacity', 0.8)       .style('top', d3.event.pageY + 5 + 'px')       .style('left', d3.event.pageX + 5 + 'px')         .html(nodeData.value); 
```

```
  } else {   // Cacher l'info-bulle lorsque la souris ne trouve pas de nodeData.      d3.select('#tooltip').style('opacity', 0);     }
```

```
}); // Écouteur/gestionnaire de canvas
```

C'est tout ! Vous avez visualisé un grand nombre d'éléments sur canvas — plus que vous n'auriez pu en afficher sans problème avec SVG. Vous avez toujours utilisé le modèle de cycle de vie de D3 et vous avez ajouté une certaine interactivité pour accéder aux données attachées à chaque élément. Ces trois étapes devraient vous permettre de faire à peu près n'importe quoi ou au moins plus que ce à quoi vous êtes habitué lorsque vous travaillez avec D3 et SVG.

Il y a un [manuel étape par étape](http://www.datamake.io/blog/d3-canvas-full#manual) de zéro à D3/canvas interactif sur mon blog qui permet des liens de page internes. De cette façon, vous pouvez voir tout le processus en une seule vue et cliquer à travers avec facilité :

![Image](https://cdn-media-1.freecodecamp.org/images/WFMyJnhsCus25iIwedpkhmFOyR5GhIDK-1Pk)
_Cliquez pour accéder au manuel_

...et [voici le code complet à nouveau](http://blockbuilder.org/larsvers/6049de0bcfa50f95d3dcbf1e3e44ad48).

J'espère que vous avez apprécié la lecture de ceci et n'hésitez pas à dire [bonjour](http://www.datamake.io/contact) et/ou...

![Image](https://cdn-media-1.freecodecamp.org/images/U2X4aQqHtu8wQ4tmHtx31iS1aTNRabBRO2h5)

_lars verspohl [www.datamake.io](http://www.datamake.io) @lars_vers [https://www.linkedin.com/in/larsverspohl](https://www.linkedin.com/in/larsverspohl)_

_...est toujours reconnaissant pour un like ? ou un follow qu'il peut retourner._