---
title: Qu'est-ce qu'un fichier SVG ? Explication des images et balises SVG
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T22:19:00.000Z'
originalURL: https://freecodecamp.org/news/svg-basics-what-are-scalable-vector-graphics-and-how-do-you-use-them
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d39740569d1a4ca3693.jpg
tags:
- name: SVG
  slug: svg
- name: toothbrush
  slug: toothbrush
seo_title: Qu'est-ce qu'un fichier SVG ? Explication des images et balises SVG
seo_desc: 'SVG

  SVG or Scalable Vector Graphics is a web standard for defining vector-based graphics
  in web pages. Based on XML the SVG standard provides markup to describe paths, shapes,
  and text within a viewport. The markup can be embedded directly into HTML ...'
---

## **SVG**

SVG ou Scalable Vector Graphics est un standard web pour définir des graphiques vectoriels dans les pages web. Basé sur XML, le standard SVG fournit un balisage pour décrire des chemins, des formes et du texte dans une fenêtre d'affichage. Le balisage peut être intégré directement dans le HTML pour l'affichage ou enregistré dans un fichier `.svg` et inséré comme toute autre image. 

Vous pouvez écrire du SVG à la main, mais des graphiques plus complexes peuvent être conçus dans des éditeurs de graphiques vectoriels tels qu'Illustrator ou InkScape et exportés vers des fichiers ou du code SVG.

## **Bases du SVG**

Les développeurs commencent un graphique SVG avec la balise `<svg>` et l'espace de noms XML comme suit :

```svg
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">

</svg>
```

L'exemple inclut également un attribut `version`. L'attribut `version` est facultatif mais il est recommandé pour la conformité avec les spécifications XML.

Cet exemple n'affichera rien, il établit simplement une fenêtre d'affichage. Vous pouvez ajouter des attributs `height` et `width` pour définir une taille d'affichage pour la fenêtre d'affichage, ce qui établit essentiellement une toile sur laquelle travailler.

Avec une fenêtre d'affichage en place, vous pouvez ajouter des graphiques de base, du texte et des éléments de chemin.

```svg
<svg
     version="1.1"
     width="100%"
     viewbox="0 0 600 300"
     xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="100" height="100" fill="#f7b2c1" />
  <circle cx="240" cy="60" r="50" fill="#c1b2f7" stroke="#b2c1f7" stroke-width="15"/>
  <text x="450" y="70" font-size="20" text-anchor="middle">Le texte SVG est lisible par le navigateur !</text>
  <g stroke="#b2c1f7"> <!-- g signifie groupe -->
    <path stroke-width="2" d="M10 170 l590 0" />
    <path stroke-width="4" d="M10 190 l590 0" />
    <path stroke-width="6" d="M10 210 l590 0" />
  </g>  
</svg>  
```

Vous pouvez voir le résultat et jouer avec le code dans [ce codepen](https://codepen.io/SgiobairOg/pen/OxbNpW).

Dans la balise d'ouverture `svg`, nous ajoutons un attribut width pour définir la largeur de la fenêtre d'affichage à 100 % de la largeur du conteneur, vous pouvez utiliser des pourcentages ou des largeurs en pixels. La balise d'ouverture svg a également un attribut `viewbox` qui définit une fenêtre à travers laquelle les éléments de votre svg sont visibles, dans ce cas, la viewbox s'étend de (0,0) à (600,300). Dans l'espace SVG, l'axe X commence avec zéro à gauche et augmente vers la droite ; l'axe Y commence avec zéro en haut et augmente vers le bas.

La première nouvelle balise est la balise `<rect />` qui définit un rectangle dans la fenêtre d'affichage SVG. Dans ce cas, nous définissons un carré qui est à 10 unités du haut et de la gauche et de 100 unités de haut et de large. L'attribut `fill` définit la couleur de remplissage pour la forme.

Ensuite, nous définissons un cercle ou un ovale avec la balise `<circle />`. L'exemple définit un cercle centré à (240,60) avec un rayon de 50 unités. Les attributs `stroke` et `stroke-width` définissent une couleur de trait et une taille pour le trait.

Vous pouvez ajouter du texte au graphique avec la balise `text`. Le texte de l'exemple est ancré depuis le milieu du texte à un point à (450, 70) et a une taille de police de 20 unités. L'avantage du texte dans SVG est qu'il s'adaptera avec le reste de votre graphique, mais il reste lisible par le navigateur et les robots web.

Lorsque vous souhaitez appliquer les mêmes attributs ou styles CSS à plusieurs éléments SVG, vous pouvez les regrouper avec la balise `<g>`. Les attributs assignés à la balise `<g>`, comme l'attribut `stroke` dans l'exemple, seront appliqués à tous les éléments du groupe. Dans ce cas, trois éléments `<path />`.

L'élément `<path />` définit un chemin vectoriel dans la fenêtre d'affichage. Le chemin est défini par l'attribut `d`. Dans le premier exemple, la définition se lit comme suit : 'déplacer vers la coordonnée absolue (10, 170) _et_ dessiner une ligne vers les coordonnées relatives 590 dans la direction X et 0 dans la direction Y.

Les commandes suivantes peuvent être utilisées pour créer votre chemin :

M = déplacer vers L = ligne vers H = ligne horizontale vers V = ligne verticale vers Z = fermer le chemin C = (courbe de bézier cubique) courbe vers S = courbe lisse vers Q = courbe de bézier quadratique vers T = courbe de bézier quadratique lisse vers A = arc

### **L'élément canvas**

Les graphiques Canvas peuvent être dessinés sur un

Un contexte est créé via la méthode getContext sur le

```text
<p> Avant canvas</p >
<canvas width ="120" height ="60"> </canvas>
<p >Après canvas</p>
<script>
    var canvas = document.querySelector("canvas");
    var context = canvas.getContext("2d");
    context.fillStyle = "red";
    context.fillRect (10, 10, 100, 50);
</script>
```

![Image](http://www.crwflags.com/fotw/images/s/sly@stt.gif)

Après avoir créé l'objet contexte, l'exemple dessine un rectangle rouge de 100 pixels de large et 50 pixels de haut, avec son coin supérieur gauche aux coordonnées (10,10).

### **Dessiner un graphique en secteurs**

La variable results contient un tableau d'objets qui représentent les réponses à l'enquête.

```text
var results = [
{ name : "Satisfait", count: 1043, color: "lightblue"} ,
{ name : "Neutre", count: 563 , color: "lightgreen"} ,
{ name : "Insatisfait", count: 510 , color: "pink"} ,
{ name : "Sans commentaire", count: 175 , color: "silver"}
];
```

Pour dessiner un graphique en secteurs, nous dessinons un certain nombre de secteurs, chacun composé d'un arc et d'une paire de lignes vers le centre de cet arc. Nous pouvons calculer l'angle occupé par chaque arc en divisant un cercle complet (2 π) par le nombre total de réponses, puis en multipliant ce nombre (l'angle par réponse) par le nombre de personnes ayant choisi une option donnée.

```text
<canvas width ="200" height ="200"></canvas>
<script>
    var cx = document.querySelector("canvas").getContext("2d");
    var total = results.reduce(function (sum, choice) {
    return sum + choice.count;
    }, 0);

    // Commencer en haut

    var currentAngle = -0.5 * Math.PI;
    results.forEach (function (result) {
    var sliceAngle = (result.count / total) * 2 * Math.PI;
    cx.beginPath() ;
    // centre = 100, 100, rayon = 100
    // à partir de l'angle actuel, dans le sens des aiguilles d'une montre selon l'angle du secteur
    cx.arc(100, 100, 100, currentAngle, currentAngle + sliceAngle);
    currentAngle += sliceAngle;
    cx.lineTo(100, 100);
    cx.fillStyle = result.color ;
    cx.fill() ;
    });
</script>
```

Cela dessine le graphique suivant :

![Image](https://pbs.twimg.com/media/CTDvkA8UwAAdJg5.png)

### **Support des navigateurs**

Le [support des navigateurs pour SVG](https://caniuse.com/#feat=svg) est disponible dans tous les navigateurs modernes. Il existe quelques problèmes de mise à l'échelle dans IE 9 à IE 11, mais ils peuvent être surmontés avec l'utilisation des attributs `width`, `height`, `viewbox`, et CSS.

## **Éditeurs**

* [Vectr](https://vectr.com/) - outil web et de bureau pour créer et éditer des graphiques SVG, gratuitement

## **Outils pour créer des SVG**

Il existe quelques outils disponibles pour créer des SVG sous forme de programme de dessin.

* [Inkscape](https://www.inkscape.org/) - Il s'agit d'un outil open source pour le dessin vectoriel de pointe avec une interface graphique facile à utiliser.
* [Adobe Illustrator](https://www.adobe.com/products/illustrator/) - Adobe Illustrator est un outil commercial pour l'imagerie vectorielle.

Pour plus d'outils, consultez la [liste W3C des outils qui supportent SVG](https://https//www.w3.org/Graphics/SVG/WG/wiki/Implementations)

## **Pourquoi vous devriez utiliser les SVG**

En tant que format d'image vectorielle, il vous permet de redimensionner une image sans perte de qualité et avec un poids particulièrement léger. En tant que format XML, il vous permet de bénéficier de toute la puissance de JavaScript et surtout de CSS.

## Plus d'informations sur les SVG :

* [Pourquoi vous devriez utiliser des images SVG](https://www.freecodecamp.org/news/a-fresh-perspective-at-why-when-and-how-to-use-svg/)
* [Ce que vous devez savoir pour travailler avec SVG dans VS Code](https://www.freecodecamp.org/news/things-you-need-to-know-about-working-with-svg-in-vs-code-63be593444dd/)
* [Comment rendre votre bouton SVG fantaisie accessible](https://www.freecodecamp.org/news/how-to-make-your-fancy-svg-button-accessible-83c9172c3c15/)