---
title: Comment créer un graphique à barres divergentes avec une bibliothèque de graphiques
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-24T17:09:07.000Z'
originalURL: https://freecodecamp.org/news/diverging-bar-chart-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/diverging-bar-chart-javascript-1500.png
tags:
- name: charts
  slug: charts
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
seo_title: Comment créer un graphique à barres divergentes avec une bibliothèque de
  graphiques JavaScript
seo_desc: 'By Shachee Swadia

  This article is a step-by-step guide that''ll show you how to build an interactive
  JavaScript range chart that visualizes 20 years of the LA Lakers’ performance with
  Kobe Bryant.

  The year 2020 was pretty poignant for obvious reasons....'
---

Par Shachee Swadia

Cet article est un guide étape par étape qui vous montrera comment construire un graphique de plage JavaScript interactif qui visualise 20 ans de performance des LA Lakers avec Kobe Bryant.

L'année 2020 a été assez poignante pour des raisons évidentes. Mais même avant la pandémie, l'année a commencé sur une note triste avec la mort de la légende du basket-ball [Kobe Bryant](https://en.wikipedia.org/wiki/Kobe_Bryant). Il était une star de la NBA qui avait joué pendant 20 ans avec une seule et unique équipe — les Los Angeles Lakers. 

En me souvenant de Kobe un an après cet horrible accident, je me suis demandé comment les Lakers avaient performé durant son ère de deux décennies. J'ai donc visualisé cela dans un graphique à barres divergentes interactif avec l'aide de JavaScript pur. 

Pensant que ce projet pourrait être utile pour ceux qui sont nouveaux dans la création de graphiques web, j'ai également consigné tout le processus et fait un tutoriel. Jetez un coup d'œil !

## Qu'est-ce qu'un graphique à barres divergentes ?

Tout d'abord, je vais vous donner une brève explication sur ce que sont les graphiques à barres divergentes, puis nous plongerons dans le tutoriel. 

Un graphique à barres divergentes montre deux mesures ou plus qui sont tracées à partir d'une ligne de base centrale, s'étendant soit à droite et à gauche (barres de plage horizontales) soit en haut et en bas (colonnes de plage verticales). 

Le point clé de la visualisation des données dans de tels graphiques divergents est de faciliter la comparaison de plusieurs catégories en les affichant contre un point médian bifurqué.

Dans ce tutoriel, j'utilise la technique du graphique à barres divergentes pour montrer les victoires et les défaites des LA Lakers au cours des 20 ans de la carrière de Kobe Bryant.

Voici un aperçu du graphique final pour vous préparer au début du jeu ! Suivez-moi pour apprendre comment je crée ce beau graphique à barres de plage avec JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/js-diverging-bar-chart.gif)

## Comment créer un graphique à barres divergentes JavaScript en 4 étapes de base

Il existe de [multiples](https://en.wikipedia.org/wiki/Comparison_of_JavaScript_charting_libraries) bibliothèques JavaScript qui fournissent du code JS pré-écrit pour des fonctions couramment nécessaires, ce qui peut rendre le processus de visualisation de données interactives assez rapide et simple. 

J'ai choisi une bibliothèque appelée [AnyChart](https://www.anychart.com) pour créer ce graphique à barres divergentes. Cette bibliothèque de graphiques JS semblait supporter (particulièrement utile dans ce cas) les graphiques de plage directement et était également suffisamment flexible pour faire ce que je voulais. 

De plus, il est assez facile de commencer avec AnyChart même pour les débutants car il y a de nombreux exemples prêts à l'emploi et une [documentation](https://docs.anychart.com) intensive.

Bien sûr, avoir de bonnes compétences en HTML et JavaScript vous donne un avantage lors de la visualisation de données sur le web. Mais de toute façon, le meilleur aspect de l'utilisation de bonnes bibliothèques de graphiques est qu'elles rendent la création de graphiques interactifs assez simple, même sans beaucoup d'expérience.

L'ensemble du processus de création de n'importe quel graphique JS, y compris un graphique à barres divergentes comme celui-ci, peut être décomposé en quatre étapes fondamentales :

1. Créer une page HTML.
2. Référencer les fichiers JS nécessaires.
3. Définir les données.
4. Écrire le code JS pour le graphique.

Passons en revue chaque étape en détail maintenant.

### 1. Créer une page HTML de base

La première chose que nous devons faire est de créer une page HTML de base. Donnons-lui un titre et créons un élément de bloc HTML pour contenir le graphique. Pour identifier ce `<div>` plus tard dans le code, nous devons également lui donner un attribut id (appelons-le "container").

```html
<html>
  <head>
    <title>Graphique à barres divergentes JavaScript</title>
    <style type="text/css">      
        html, body, #container { 
            width: 100%; height: 100%; margin: 0; padding: 0; 
        } 
    </style>
  </head>
  <body>
    <div id="container"></div>
  </body>
</html>
```

Notez qu'il est possible de spécifier les paramètres de largeur et de hauteur à l'intérieur du bloc `<style>` pour modifier l'espace que votre graphique occupera. J'ai mis 100% dans les deux paramètres pour que le graphique remplisse toute la page.

### 2. Inclure les fichiers JavaScript nécessaires

Ensuite, nous devons ajouter les scripts de la bibliothèque de graphiques qui aideront à créer la visualisation des données. Puisque nous travaillons avec la bibliothèque AnyChart ici, incluons les fichiers correspondants depuis son [CDN](https://www.anychart.com/download/cdn/). (Gardez à l'esprit que vous pouvez toujours télécharger les scripts si vous le souhaitez.)

Pour le graphique à barres divergentes, nous avons besoin du [script du module de base](https://docs.anychart.com/Quick_Start/Modules#base) qui doit être ajouté à la section `<head>` de la page HTML.

```js
<html>
  <head>
    <title>Graphique à barres divergentes JavaScript</title>
    <script src="https://cdn.anychart.com/releases/8.9.0/js/anychart-base.min.js" type="text/javascript"></script>
    <style type="text/css">
      html,
      body,
      #container {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      // Tout le code pour le graphique à barres divergentes JS viendra ici
    </script>
  </body>
</html>

```

### 3. Ajouter les données

Je voulais visualiser le nombre de victoires et de défaites de l'équipe des LA Lakers sur toutes les saisons de 1996 à 2016. J'ai donc obtenu les données depuis le [site web de la NBA](https://www.nba.com/lakers/history/seasonbyseason/) et créé un tableau avec l'année, les victoires et les défaites.

Puisque la quantité de données n'est pas énorme, nous pouvons les ajouter comme suit :

```
var winlossData = [
  [65, 17, "2015-16"],
  [61, 21, "2014-15"],
  [55, 27, "2013-14"],
  [37, 45, "2012-13"],
  [25, 41, "2011-12"],
  [25, 57, "2010-11"],
  [25, 57, "2009-10"],
  [17, 65, "2008-09"],
  [25, 57, "2007-08"],
  [40, 42, "2006-07"],
  [37, 45, "2005-06"],
  [48, 34, "2004-05"],
  [26, 56, "2003-04"],
  [32, 50, "2002-03"],
  [24, 58, "2001-02"],
  [26, 56, "2000-01"],
  [15, 67, "1999-00"],
  [19, 31, "1998-99"],
  [21, 61, "1997-98"],
  [26, 56, "1996-97"]
];
```

Maintenant que la scène est prête, commençons à jouer en ajoutant le code JavaScript qui créera le graphique à barres divergentes interactif !

### 4. Écrire le code JavaScript pour votre graphique

Avant toute chose, nous devons ajouter une fonction englobant tout le code JS, qui garantit que l'ensemble du code à l'intérieur ne s'exécutera qu'une fois la page chargée.

```js
<script>
  anychart.onDocumentReady(function() {
    // L'endroit pour le code du graphique à barres divergentes JS
  });
</script>
```

En général, un graphique à barres divergentes JS est assez simple à créer et je vais vous guider à travers chaque action. Alors préparez-vous à bouger, bloquer et tirer !

Tout d'abord, nous créons un graphique à barres et entrons les données, tout cela à l'intérieur de la fonction englobante `anychart.onDocumentReady()`.

```js
// créer un graphique à barres
var chart = anychart.bar();

// données
var winlossData = [
  [65, 17, "2015-16"],
  [61, 21, "2014-15"],
  [55, 27, "2013-14"],
  [37, 45, "2012-13"],
  [25, 41, "2011-12"],
  [25, 57, "2010-11"],
  [25, 57, "2009-10"],
  [17, 65, "2008-09"],
  [25, 57, "2007-08"],
  [40, 42, "2006-07"],
  [37, 45, "2005-06"],
  [48, 34, "2004-05"],
  [26, 56, "2003-04"],
  [32, 50, "2002-03"],
  [24, 58, "2001-02"],
  [26, 56, "2000-01"],
  [15, 67, "1999-00"],
  [19, 31, "1998-99"],
  [21, 61, "1997-98"],
  [26, 56, "1996-97"]
];
```

Ensuite, nous créons une fonction qui accepte deux paramètres — un numéro de colonne et un nom. Le numéro de colonne indique la colonne dans le jeu de données et le nom indique la série. Dans notre cas, nous avons deux séries — une pour le nombre de victoires et une pour le nombre de défaites. 

Puisque nous voulons un graphique à barres divergentes, prenons le centre et traçons les barres pour les victoires à droite et les barres pour les défaites à gauche. Ensuite, nous devons préparer le jeu de données en ajoutant toutes les valeurs requises via une boucle 'for'.

Ne vous inquiétez pas si cela semble un peu compliqué. Il s'agit simplement de préparer nos données à être tracées, et lorsque vous regarderez le code ci-dessous, vous verrez probablement que tout est complètement logique.

Il y a deux autres choses que nous devons inclure dans la fonction. Nous définissons une série avec la fonction rangeBar et ajoutons une ligne pour indiquer les noms des séries et une ligne de séparation entre les barres de gauche et de droite.

```js
var createSeries = function (columnNumber, name) {
  var data = [];
  for (var i = 0; i < winlossData.length; i++) {
    var value = winlossData[i][columnNumber];
    var center = 0;
    if (name === "Wins") {
      data.push({
        x: winlossData[i][2],
        low: center,
        high: center + value,
        value: value
      });
    } else {
      data.push({
        x: winlossData[i][2],
        low: -center,
        high: -center - value,
        value: value
      });
    }
  }
    
  var series = chart.rangeBar(data);
  series.name(name);
};

```

Maintenant, nous créons les deux séries avec les arguments souhaités en utilisant la fonction que nous venons de définir.

```js
createSeries(0, "Losses");
createSeries(1, "Wins");
```

C'est la mi-temps et les parties les plus compliquées sont terminées ! Maintenant, nous avons simplement la configuration du graphique.

Ajoutez le titre au graphique à barres divergentes :

```js
chart
  .title()
  .enabled(true)
  .text("20 ans de bilan victoires-défaites des LA Lakers avec Kobe Bryant (1996-2016)");
```

Et activez la légende du graphique :

```js
chart
  .legend()
  .enabled(true);
```

Pour faire en sorte que les victoires et les défaites de chaque année apparaissent adjacentes les unes aux autres, nous devons convertir le graphique à barres multi-séries en un graphique à barres empilées. Ensuite, pour souligner la divergence, ajoutons un marqueur de ligne à 0. Enfin, nous attribuons le div conteneur et dessinons le graphique :

```js
// créer un graphique à barres empilées à partir du graphique à barres multi-séries
chart.yScale().stackMode("value");

// définir un identifiant de conteneur pour le graphique
chart.container("container");
  
// initier le dessin du graphique
chart.draw();

```

C'est le coup de sifflet et voilà — un graphique à barres divergentes interactif très basique, mais entièrement fonctionnel, construit avec JavaScript !

![Image](https://www.freecodecamp.org/news/content/images/2021/02/initial-chart-default-colors-1.PNG)

Bien que Kobe ait pu être spectaculaire dans les derniers matchs de sa carrière en NBA, nous pouvons voir que les Lakers ont lutté pendant ses dernières années avec plus de défaites que de victoires. Mais le bilan global est définitivement beaucoup plus de triomphes que de défaites.

**Jetez un coup d'œil à cette version initiale du graphique à barres divergentes avec le code complet JS/CSS/HTML [sur CodePen](https://codepen.io/shacheeswadia/pen/jOVrqLQ).**

```js
<html>
  <head>
    <title>Graphique à barres divergentes JavaScript</title>
    <script src="https://cdn.anychart.com/releases/8.9.0/js/anychart-base.min.js" type="text/javascript"></script>
    <style type="text/css">
      html,
      body,
      #container {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>

    anychart.onDocumentReady(function () {
  
      // créer un graphique à barres
      var chart = anychart.bar();

      // données
      var winlossData = [
        [65, 17, "2015-16"],
        [61, 21, "2014-15"],
        [55, 27, "2013-14"],
        [37, 45, "2012-13"],
        [25, 41, "2011-12"],
        [25, 57, "2010-11"],
        [25, 57, "2009-10"],
        [17, 65, "2008-09"],
        [25, 57, "2007-08"],
        [40, 42, "2006-07"],
        [37, 45, "2005-06"],
        [48, 34, "2004-05"],
        [26, 56, "2003-04"],
        [32, 50, "2002-03"],
        [24, 58, "2001-02"],
        [26, 56, "2000-01"],
        [15, 67, "1999-00"],
        [19, 31, "1998-99"],
        [21, 61, "1997-98"],
        [26, 56, "1996-97"]
      ];

      // configurer une fonction pour créer des séries
      var createSeries = function (columnNumber, name) {
        var data = [];
        for (var i = 0; i < winlossData.length; i++) {
          var value = winlossData[i][columnNumber];
          var center = 0;
          if (name === "Wins") {
            data.push({
              x: winlossData[i][2],
              low: center,
              high: center + value,
              value: value
            });
          } else {
            data.push({
              x: winlossData[i][2],
              low: -center,
              high: -center - value,
              value: value
            });
          }
        }
    
        var series = chart.rangeBar(data);
        series.name(name);
      };

      // créer des séries
      createSeries(0, "Losses");
      createSeries(1, "Wins");

      // définir le titre du graphique
     chart
        .title()
        .enabled(true)
        .text("20 ans de bilan victoires-défaites des LA Lakers avec Kobe Bryant (1996-2016)");

      // activer la légende du graphique
      chart
        .legend()
        .enabled(true);
  
      // créer un graphique à barres empilées à partir du graphique à barres multi-séries
      chart.yScale().stackMode("value");

      // définir un identifiant de conteneur pour le graphique
      chart.container("container");
  
      // initier le dessin du graphique
      chart.draw();

    });

    </script>
  </body>
</html>

```

## Comment personnaliser notre graphique à barres divergentes JavaScript

Un truc de dunk dans la visualisation interactive de données avec JavaScript est la liberté que nous avons de la personnaliser pour que nos données racontent de meilleures histoires. Je vais vous montrer comment apporter quelques modifications rapides au graphique à barres divergentes JS de base pour le rendre plus engageant et informatif.

Maintenant, je vais lancer un tir à trois points et personnaliser le graphique pour améliorer certaines de ses fonctionnalités et esthétiques.

### 1. Style de base et paramètres des axes

Pour commencer, changeons certains styles de base et paramètres pour les axes X et Y pour rendre les choses plus lisibles. 

Rappelez-vous simplement que dans AnyChart, un [graphique à barres de plage](https://docs.anychart.com/Basic_Charts/Range_Bar_Chart) est la version verticale d'un [graphique à colonnes de plage](https://docs.anychart.com/Basic_Charts/Range_Column_Chart). Par conséquent, dans notre graphique à barres divergentes, l'axe horizontal est l'axe Y, et l'axe vertical est appelé l'axe X.

Alors, débarrassons-nous des ticks, configurons le titre de l'axe et personnalisons les étiquettes sur l'axe vertical. Nous allons également définir 80 comme maximum et supprimer le signe moins des étiquettes sur l'axe horizontal :

```js
chart
  .xAxis()
  .ticks(false);
chart
  .xAxis()
  .title()
  .enabled(true)
  .text("Années")
  .padding([0, 0, 10, 0]);
chart
  .xAxis()
  .labels()
  .fontSize(11)
  .fontColor("#474747")
  .padding([0, 10, 0, 0]);
chart.yScale().maximum(80);
chart
  .yAxis(0)
  .labels()
  .format(function () {
    return Math.abs(this.value);
  });

```

Ensuite, pour souligner la divergence, il serait bien d'ajouter un trait blanc entre les deux séries et un marqueur de ligne à 0.

```js
// ajouter le trait en le définissant dans cette ligne
series.name(name).stroke("3 #fff 1");

...

// créer un marqueur de ligne à 0
chart
  .lineMarker()
  .value(0)
  .stroke("#CECECE");

```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/intermediate-chart-1-1.PNG)

Ah, le graphique ne semble-t-il pas plus poli et plus facile à lire maintenant ?

**Consultez le code de cette version du graphique à barres divergentes [sur CodePen](https://codepen.io/shacheeswadia/pen/zYoEMEd).**

Avant d'apporter d'autres personnalisations, il y a une petite digression que je veux faire. J'ai également pensé à faire en sorte que l'axe horizontal affiche les victoires et les défaites pour chaque saison en pourcentages plutôt qu'en valeurs absolues. C'est assez facile, mais le résultat n'offrait aucun aperçu supplémentaire. 

De plus, les valeurs absolues représentent effectivement lorsque les Lakers ont joué plus ou moins de matchs au cours de l'année. C'est finalement pourquoi j'ai décidé de garder les valeurs absolues. Mais vous êtes les bienvenus pour consulter la version avec les pourcentages [sur CodePen](https://codepen.io/shacheeswadia/pen/jOVrqKd). 

Bien, passons de ce tir manqué et revenons en mode concentration.

### 2. Personnalisation de l'infobulle

Ensuite, j'ai personnalisé l'infobulle pour la rendre plus informative et intéressante.

Ici, j'ai également eu l'idée de présenter les valeurs de pourcentage précédemment calculées (voir l'exemple de la digression juste au-dessus) comme un élément d'information supplémentaire dans l'infobulle de notre graphique à barres divergentes.

Donc, la première étape consiste à implémenter le calcul des valeurs de pourcentage :

```js
// calculer les pourcentages pour l'infobulle
var val = winlossData[i][columnNumber] * 100;
if (columnNumber == 0) {
  var percentValue =
    val / (winlossData[i][columnNumber] + winlossData[i][columnNumber + 1]);
} else {
  var percentValue =
    val / (winlossData[i][columnNumber] + winlossData[i][columnNumber - 1]);
}
percentValue = percentValue.toFixed(2);

```

Le calcul du pourcentage fait partie de la fonction de configuration de la série — regardez comment il est inclus là :

```js
// configurer une fonction pour créer des séries
var createSeries = function (columnNumber, name) {
  var data = [];
  for (var i = 0; i < winlossData.length; i++) {

    // calculer les pourcentages pour l'infobulle
    var val = winlossData[i][columnNumber] * 100;
    if (columnNumber == 0) {
      var percentValue =
        val / (winlossData[i][columnNumber] + winlossData[i][columnNumber + 1]);
    } else {
      var percentValue =
        val / (winlossData[i][columnNumber] + winlossData[i][columnNumber - 1]);
    }
    percentValue = percentValue.toFixed(2);     
      
    var value = winlossData[i][columnNumber];
    var center = 0;
    if (name === "Wins") {
      data.push({
        x: winlossData[i][2],
        low: center,
        high: center + value,
        value: value,
        // ajouter la valeur de pourcentage calculée
        percentValue: percentValue
      });
    } else {
      data.push({
        x: winlossData[i][2],
        low: -center,
        high: -center - value,
        value: value,
        // ajouter la valeur de pourcentage calculée
        percentValue: percentValue
      });
    }
  }

```

Ensuite, nous avons un formatage supplémentaire de l'infobulle pour que tout ait l'air net et beau :

```js
// personnaliser l'infobulle
chart
  .tooltip()
  .useHtml(true)
  .fontSize(12)
  .titleFormat(function () {
    return this.getData("x") + " " + this.seriesName;
  })
  .format(function () {
    return (
      "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Total games: " +
      "<b>" +
      this.getData("value") +
      "</b></h6>" +
      "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Percentage games: " +
      "<b>" +
      this.getData("percentValue") +
      " %</b></h6>"
    );
  });

```

### 3. Changement de la palette de couleurs

Eh bien, cette dernière personnalisation est définitivement un coup de poignard — le tir qui va rendre le graphique complètement génial et gagner le match ! Il s'agit simplement de changer la palette de couleurs pour qu'elle corresponde aux couleurs des maillots des LA Lakers. Si simple :

```js
chart.palette(
  anychart.palettes.distinctColors().items(["#FDB827", "#542583"])
);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/final-chart-without-tooltip-2.PNG)

Vous voyez, à la toute dernière seconde, j'ai également désactivé le mode de sélection en ajoutant la commande correspondante à cette ligne :

```js
series.name(name).stroke("3 #fff 1").selectionMode("none");
```

**D'accord ! Ce graphique à barres de plage divergentes interactif JavaScript final est disponible [sur CodePen](https://codepen.io/shacheeswadia/pen/NWbrpYj).**

Au cas où, le code complet pour la page HTML est juste ici :

```js
<html>
  <head>
    <title>Graphique à barres divergentes JavaScript</title>
    <script src="https://cdn.anychart.com/releases/8.9.0/js/anychart-base.min.js" type="text/javascript"></script>
    <style type="text/css">
      html,
      body,
      #container {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>

    anychart.onDocumentReady(function () {
  
      // créer un graphique à barres
      var chart = anychart.bar();

      // données
      var winlossData = [
        [65, 17, "2015-16"],
        [61, 21, "2014-15"],
        [55, 27, "2013-14"],
        [37, 45, "2012-13"],
        [25, 41, "2011-12"],
        [25, 57, "2010-11"],
        [25, 57, "2009-10"],
        [17, 65, "2008-09"],
        [25, 57, "2007-08"],
        [40, 42, "2006-07"],
        [37, 45, "2005-06"],
        [48, 34, "2004-05"],
        [26, 56, "2003-04"],
        [32, 50, "2002-03"],
        [24, 58, "2001-02"],
        [26, 56, "2000-01"],
        [15, 67, "1999-00"],
        [19, 31, "1998-99"],
        [21, 61, "1997-98"],
        [26, 56, "1996-97"]
      ];

      // configurer une fonction pour créer des séries
      var createSeries = function (columnNumber, name) {
        var data = [];
        for (var i = 0; i < winlossData.length; i++) {

          // calculer les pourcentages pour l'infobulle
          var val = winlossData[i][columnNumber] * 100;
          if (columnNumber == 0) {
            var percentValue =
              val / (winlossData[i][columnNumber] + winlossData[i][columnNumber + 1]);
         } else {
            var percentValue =
              val / (winlossData[i][columnNumber] + winlossData[i][columnNumber - 1]);
          }
          percentValue = percentValue.toFixed(2);     
      
          var value = winlossData[i][columnNumber];
          var center = 0;
          if (name === "Wins") {
            data.push({
              x: winlossData[i][2],
              low: center,
              high: center + value,
              value: value,
              // ajouter la valeur de pourcentage calculée
              percentValue: percentValue
            });
          } else {
            data.push({
              x: winlossData[i][2],
              low: -center,
              high: -center - value,
              value: value,
              // ajouter la valeur de pourcentage calculée
              percentValue: percentValue
            });
          }
        }
    
        var series = chart.rangeBar(data);
        series.name(name).stroke("3 #fff 1").selectionMode("none");
      };

      // créer des séries
      createSeries(0, "Losses");
      createSeries(1, "Wins");

      // définir le titre du graphique
      chart
        .title()
        .enabled(true)
        .text("20 ans de bilan victoires-défaites des LA Lakers avec Kobe Bryant (1996-2016)");

      // activer la légende du graphique
      chart
        .legend()
        .enabled(true);
  
      // créer un graphique à barres empilées à partir du graphique à barres multi-séries
      chart.yScale().stackMode("value");
  
      // personnaliser les paramètres des axes
      chart
        .xAxis()
        .ticks(false);
      chart
        .xAxis()
        .title()
        .enabled(true)
        .text("Années")
        .padding([0, 0, 10, 0]);
      chart
        .xAxis()
        .labels()
        .fontSize(11)
        .fontColor("#474747")
        .padding([0, 10, 0, 0]);
      chart.yScale().maximum(80);
      chart
        .yAxis(0)
        .labels()
        .format(function () {
          return Math.abs(this.value);
        });

      // créer un marqueur de ligne à 0
      chart
        .lineMarker()
        .value(0)
        .stroke("#CECECE");
  
      // personnaliser l'infobulle
      chart
        .tooltip()
        .useHtml(true)
        .fontSize(12)
        .titleFormat(function () {
          return this.getData("x") + " " + this.seriesName;
        })
        .format(function () {
          return (
            "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Total games: " +
            "<b>" +
            this.getData("value") +
            "</b></h6>" +
            "<h6 style='font-size:12px; font-weight:400; margin: 0.25rem 0;'>Percentage games: " +
            "<b>" +
            this.getData("percentValue") +
            " %</b></h6>"
          );
        });
  
      // définir une palette de couleurs personnalisée
      chart.palette(
        anychart.palettes.distinctColors().items(["#FDB827", "#542583"])
      );

      // définir un identifiant de conteneur pour le graphique
      chart.container("container");
  
      // initier le dessin du graphique
      chart.draw();

    });

    </script>
  </body>
</html>

```

## Conclusion

Dans ce tutoriel, je vous ai montré à quel point il est rapide et facile de mettre en place un graphique à barres divergentes en utilisant JavaScript. Nous avons également vu comment un peu d'effort rend le graphique vraiment cool et vous permet de tirer plus de profit des données sous-jacentes. N'hésitez pas à me faire savoir si vous avez des questions.

Si vous êtes motivé pour travailler davantage avec la visualisation de données interactive basée sur JS, allez-y et jouez avec les graphiques à barres divergentes sur CodePen (j'ai ajouté des liens tout au long du tutoriel), consultez [d'autres options de graphiques](https://www.anychart.com/chartopedia/), ou essayez [d'autres bibliothèques JavaScript](https://en.wikipedia.org/wiki/Comparison_of_JavaScript_charting_libraries).

De plus, alors que nous regardons avec affection les statistiques de l'équipe de la légende du basket-ball ici, n'oubliez pas de faire plus de sport et de créer plus de visualisations !