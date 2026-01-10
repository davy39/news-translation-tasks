---
title: Tutoriel sur les graphiques en lignes – Comment créer un graphique en lignes
  en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-08T19:58:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-line-charts-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/line-chart.png
tags:
- name: charts
  slug: charts
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
seo_title: Tutoriel sur les graphiques en lignes – Comment créer un graphique en lignes
  en JavaScript
seo_desc: "By Shachee Swadia\nData visualization is a vast field with so many different\
  \ types of charts to learn and create. \nBut there are several basic, evergreen\
  \ graphs that every data designer and web developer dealing with analytics should\
  \ know how to build..."
---

Par Shachee Swadia

La visualisation de données est un domaine vaste avec tant de différents [types de graphiques](https://datavizcatalogue.com/) à apprendre et à créer. 

Mais il existe plusieurs graphiques de base, intemporels, que tout concepteur de données et développeur web traitant de l'analytique devrait savoir construire. 

L'un d'eux est le **graphique en lignes** (ou **graphique linéaire**). Il est principalement conçu pour représenter des données au fil du temps.

Vous pouvez suivre ce tutoriel pour apprendre à créer rapidement de beaux graphiques en lignes interactifs (et en lignes étagées) en utilisant JavaScript. Nous examinerons quelques exemples intéressants et les construirons étape par étape, ce qui rendra le processus à la fois clair et divertissant. 

Pour votre commodité, vous pouvez trouver tous les exemples sur [CodePen](https://codepen.io/collection/pgPwyr) afin de pouvoir jouer avec le code de création de graphiques en lignes sans limites.

### Notre ensemble de données

Les deux dernières décennies ont été rien de moins que spectaculaires dans le monde du tennis. Le [Big Three](https://en.wikipedia.org/wiki/Big_Three_(tennis)) — Roger Federer, Rafael Nadal et Novak Djokovic — ont remporté un nombre impressionnant de 63 (sur les 78 derniers) tournois du Grand Chelem. Ce sont les championnats les plus prestigieux. 

J'ai décidé de tracer leur rivalité exceptionnelle. Ainsi, les graphiques en lignes JS de ce tutoriel visualiseront **la course aux titres du Grand Chelem du Big Three**. Et le premier service arrive déjà !

# **Comment construire des graphiques en lignes en 4 étapes**

En général, le processus entier de création de n'importe quel graphique en JavaScript est divisé en quatre étapes, et un graphique en lignes ne fait pas exception :

1. Créer une page HTML avec un conteneur.
2. Inclure les fichiers JavaScript.
3. Ajouter vos données.
4. Coder une visualisation.

Passons en revue chacune de ces étapes maintenant.

### 1. Créer une page HTML avec un conteneur

Pour commencer, vous avez besoin d'un endroit où vous voulez que votre graphique apparaisse.

Si vous n'en avez pas encore, créez une page web de base. Ensuite, créez un conteneur pour le graphique en lignes — ajoutez un élément HTML de niveau bloc et donnez-lui un identifiant unique pour référence ultérieure.

Voici à quoi une telle page pourrait ressembler :

```html
<html>
  <head>
    <title>Graphique en lignes JS</title>
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

Les paramètres `width` et `height` de l'élément sont définis à 100%. Par conséquent, le graphique en lignes s'affichera sur toute la page web. Bien sûr, vous pouvez définir les paramètres de style selon vos propres préférences et besoins.

### 2. Inclure les fichiers JavaScript

Ensuite, incluez tous les fichiers JavaScript, que nous utiliserons pour créer le graphique en lignes, dans la section `<head>`.

Il existe de nombreuses bibliothèques de graphiques JavaScript différentes qui vous permettent de visualiser des données de manière rapide et simple. Beaucoup d'entre elles supportent les graphiques en lignes, et vous pouvez choisir l'une ou l'autre en fonction des exigences de votre projet. 

À des fins d'illustration, dans ce tutoriel, j'utilise [AnyChart JS Charts](https://www.anychart.com/). Il est flexible, dispose d'une documentation complète sur les [graphiques](https://docs.anychart.com) et les [références API](https://api.anychart.com), et vous pouvez l'utiliser gratuitement (sauf si vous construisez quelque chose pour une entreprise.)

Pour le graphique en lignes, j'ajoute le module « Base » depuis le [CDN](https://www.anychart.com/download/cdn/). (Bien sûr, vous pouvez le télécharger, le placer dans un dossier sur votre site web, et utiliser votre propre lien dans ce cas.)

```html
<html>
  <head>
    <title>Graphique en lignes JS</title>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-base.min.js"></script>
    <style type="text/css">      
      html, body, #container { 
        width: 100%; height: 100%; margin: 0; padding: 0; 
      } 
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      // Code JavaScript pour le graphique en lignes.
    </script>
  </body>
</html>
```

Le code JavaScript pour le graphique en lignes sera inséré entre les balises `<script>` et `</script>` situées dans la section `<body>` (vous pouvez les placer dans la section `<head>` si vous le souhaitez).

### 3. Ajouter vos données

Ensuite, ajoutez les données que vous souhaitez visualiser dans votre graphique en lignes.

J'ai compté tous les [titres en simple du Grand Chelem remportés par Federer, Nadal et Djokovic](https://en.wikipedia.org/wiki/Big_Three_(tennis)#Grand_Slam_tournaments), par année. Je vais les ajouter tels quels sous forme de tableau de tableaux. 

Si vous préférez d'autres formats dans votre cas particulier, tels que JSON, XML, CSV ou autre chose, consultez les [façons de travailler avec les données](https://docs.anychart.com/Working_with_Data/Overview).

```javascript
var data = [
  ["2003", 1, 0, 0],
  ["2004", 4, 0, 0],
  ["2005", 6, 0, 0],
  ["2006", 9, 1, 0],
  ["2007", 12, 2, 0],
  ["2008", 13, 5, 1],
  ["2009", 15, 6, 1],
  ["2010", 16, 9, 1],
  ["2011", 16, 10, 4],
  ["2012", 17, 11, 5],
  ["2013", 17, 13, 6],
  ["2014", 17, 14, 7],
  ["2015", 17, 14, 10],
  ["2016", 17, 14, 12],
  ["2017", 19, 16, 12],
  ["2018", 20, 17, 14],
  ["2019", 20, 19, 16],
  ["2020", 20, 20, 17],
  ["2021", 20, 20, 20],
  ["2022", 20, 22, 20]
];
```

Dans chaque tableau, l'année est le premier paramètre (colonne #0). Ensuite vient le nombre de titres remportés par les trois joueurs successivement (cumulatif pour chacun).

### 4. Coder une visualisation

Maintenant, la séance d'échauffement est terminée, et le court est prêt. Alors commençons le match et faisons un peu de codage JavaScript rapide !

Tout d'abord, ajoutez `anychart.onDocumentReady()` comme montré ci-dessous :

```html
<script>
  anychart.onDocumentReady(function() {
    // Le code principal JS pour le graphique en lignes sera ici.
  });
</script>
```

Tout le reste va à l'intérieur de cette fonction.

Donc, deuxièmement, incluez les données (de l'étape précédente).

Troisièmement, créez un ensemble de données et mappez-le pour chaque série (une pour chaque joueur) :

```javascript
// créer un ensemble de données
var dataSet = anychart.data.set(data);

// mapper les données pour toutes les séries
var firstSeriesData = dataSet.mapAs({x: 0, value: 1});
var secondSeriesData = dataSet.mapAs({x: 0, value: 2});
var thirdSeriesData = dataSet.mapAs({x: 0, value: 3});
```

Quatrièmement, créez une instance de graphique en lignes et trois séries avec les données mappées :

```javascript
// créer un graphique en lignes
var chart = anychart.line();

// créer les séries et les nommer
var firstSeries = chart.line(firstSeriesData);
firstSeries.name("Roger Federer");
var secondSeries = chart.line(secondSeriesData);
secondSeries.name("Rafael Nadal");
var thirdSeries = chart.line(thirdSeriesData);
thirdSeries.name("Novak Djokovic");
```

Cinquèmement, pour rendre clair d'un coup d'œil ce qui est montré dans le graphique en lignes, une bonne idée est d'ajouter une légende et un titre :

```javascript
// ajouter une légende
chart.legend().enabled(true);
  
// ajouter un titre
chart.title("Course aux titres du Grand Chelem du Big Three");
```

Enfin, référencez l'ID de l'élément conteneur et dessinez le graphique en lignes résultant :

```javascript
// spécifier où afficher le graphique
chart.container("container");
  
// dessiner le graphique résultant
chart.draw();
```

C'est tout ! Un graphique en lignes entièrement fonctionnel construit avec JS est prêt. Cela ressemble à une victoire en [sets directs](https://sports.answers.com/Q/What_does_straight_sets_mean_in_a_game_of_tennis), n'est-ce pas ?

![Un graphique en lignes de base, JS.](https://www.freecodecamp.org/news/content/images/2022/09/line-chart-1.png)
_Graphique en lignes montrant la course aux titres du Big 3 - créé avec AnyChart_

Consultez cette version de base du graphique en lignes avec le code HTML/CSS/JS complet sur [CodePen](https://codepen.io/shacheeswadia/pen/gOvjVaK). Juste au cas où, voici aussi le code :

```html
<html>
  <head>
    <title>Graphique en lignes JS</title>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-base.min.js"></script>
    <style type="text/css">      
      html, body, #container { 
        width: 100%; height: 100%; margin: 0; padding: 0; 
      } 
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      anychart.onDocumentReady(function () {
  
        // ajouter les données
        var data = [
          ["2003", 1, 0, 0],
          ["2004", 4, 0, 0],
          ["2005", 6, 0, 0],
          ["2006", 9, 1, 0],
          ["2007", 12, 2, 0],
          ["2008", 13, 5, 1],
          ["2009", 15, 6, 1],
          ["2010", 16, 9, 1],
          ["2011", 16, 10, 4],
          ["2012", 17, 11, 5],
          ["2013", 17, 13, 6],
          ["2014", 17, 14, 7],
          ["2015", 17, 14, 10],
          ["2016", 17, 14, 12],
          ["2017", 19, 16, 12],
          ["2018", 20, 17, 14],
          ["2019", 20, 19, 16],
          ["2020", 20, 20, 17],
          ["2021", 20, 20, 20],
          ["2022", 20, 22, 20]
        ];
  
        // créer un ensemble de données
        var dataSet = anychart.data.set(data);

        // mapper les données pour toutes les séries
        var firstSeriesData = dataSet.mapAs({x: 0, value: 1});
        var secondSeriesData = dataSet.mapAs({x: 0, value: 2});
        var thirdSeriesData = dataSet.mapAs({x: 0, value: 3});

        // créer un graphique en lignes
        var chart = anychart.line();

        // créer les séries et les nommer
        var firstSeries = chart.line(firstSeriesData);
        firstSeries.name("Roger Federer");
        var secondSeries = chart.line(secondSeriesData);
        secondSeries.name("Rafael Nadal");
        var thirdSeries = chart.line(thirdSeriesData);
        thirdSeries.name("Novak Djokovic");

        // ajouter une légende
        chart.legend().enabled(true);
  
        // ajouter un titre
        chart.title("Course aux titres du Grand Chelem du Big Three");
  
        // spécifier où afficher le graphique
        chart.container("container");
  
        // dessiner le graphique résultant
        chart.draw();
  
      });
    </script>
  </body>
</html>
```

# **Comment personnaliser vos graphiques en lignes**

Le graphique en lignes de base que nous avons créé en suivant les quatre étapes ci-dessus a déjà fière allure. Mais que faire si vous souhaitez le personnaliser ?

Laissez-moi vous montrer comment apporter quelques modifications de la même manière rapide et facile.

### 1. Nommer les axes

Il est toujours bon d'expliquer ce que représente chaque axe du graphique en lignes, même si cela semble assez évident. Pour ajouter des titres aux axes X et Y, utilisez ce qui suit :

```javascript
chart.yAxis().title("Titres remportés");
chart.xAxis().title("Année");
```

### 2. Personnaliser les marqueurs

Par défaut, lorsque vous déplacez le pointeur de la souris sur le tracé, des marqueurs apparaissent sur chaque série de lignes, et leurs formes sont différentes. Pourquoi ne pas donner aux marqueurs la même forme ? De plus, il serait bien de les rendre plus petits.

Voici comment vous pouvez personnaliser l'apparence des marqueurs des séries de lignes :

```javascript
firstSeries.hovered().markers().type("circle").size(4);
secondSeries.hovered().markers().type("circle").size(4);
thirdSeries.hovered().markers().type("circle").size(4);
```

### 3. Activer les lignes de référence

Les lignes de référence sont une paire de lignes perpendiculaires suivant le pointeur de la souris pour vous aider à mieux comprendre les valeurs X et Y à n'importe quel point actuellement survolé. 

Dans ce cas, il pourrait être suffisant d'obtenir une seule ligne de ce type, verticale, pour mettre en évidence l'année. Voici comment cela se fait :

```javascript
chart.crosshair().enabled(true).yStroke(null).yLabel(false);
```

### 4. Changer la position de l'infobulle

Actuellement, l'infobulle suit le pointeur de la souris. Mais dans cette situation, il pourrait être préférable de la faire coller aux points de données. 

Pour obtenir ce type de comportement, il suffit de définir le mode de position de l'infobulle du graphique en lignes comme « point » et d'ajuster les autres paramètres de position selon vos préférences. Par exemple :

```javascript
chart.tooltip().positionMode("point");
chart.tooltip().position("right").anchor("left-center").offsetX(5).offsetY(5);
```

Vérifiez à quoi ressemble le graphique en lignes JavaScript maintenant après toutes ces personnalisations. (Voir le code complet en direct sur [CodePen](https://codepen.io/shacheeswadia/pen/vYdaoyR).)

![Un graphique en lignes personnalisé, JS.](https://www.freecodecamp.org/news/content/images/2022/09/line-chart-2.png)

### 5. Changer les couleurs

L'une des manières les plus simples, mais aussi les plus efficaces, de personnaliser une visualisation de données est de jouer avec les couleurs. 

Le code ci-dessous change la couleur de la ligne de chaque joueur en la couleur principale du tournoi du Grand Chelem qu'il a remporté le plus de fois : le violet de Wimbledon pour Federer, le marron du French Open pour Nadal et le bleu de l'Australian Open pour Djokovic. De plus, l'épaisseur des lignes est ajustée.

```javascript
firstSeries.normal().stroke("#7b60a2", 2.5);
secondSeries.normal().stroke("#db7346", 2.5);
thirdSeries.normal().stroke("#43a7dc", 2.5);
```

### 6. Améliorer le texte du titre et de la légende

Les derniers changements que je souhaite démontrer dans ce tutoriel — et rendre le graphique en lignes interactif complet — sont les personnalisations du titre et de la légende.

Vous pouvez ajouter un sous-titre pour fournir plus de contexte, et vous pouvez rendre le style du texte plus attrayant en quelques ajustements rapides avec l'aide de HTML :

```javascript
chart
  .title()
  .enabled(true)
  .useHtml(true)
  .text(
    '<span style="color: #006331; font-size:20px;">Course aux titres du Grand Chelem du Big Three</span>' +
      '<br/><span style="font-size: 16px;">(Triomphes à l\'Australian Open, French Open, Wimbledon, U.S. Open)</span>'
  );
```

Pour la légende du graphique, il est facile de modifier la taille de la police et le remplissage :

```javascript
chart.legend().enabled(true).fontSize(14).padding([10, 0, 10, 0]);
```

Voyez ce que nous avons obtenu ! (Consultez ce graphique en lignes JS sur [CodePen](https://codepen.io/shacheeswadia/pen/wvyxVqZ).)

![Graphique en lignes avancé construit avec JavaScript.](https://www.freecodecamp.org/news/content/images/2022/09/line-chart-3.png)

%[https://codepen.io/shacheeswadia/pen/wvyxVqZ]

## Comment créer un graphique en lignes étagées

Tout comme c'est toujours plus excitant lorsqu'un match de tennis se joue en cinq sets, voici quelque chose en plus pour rendre ce tutoriel et cette visualisation de graphique en lignes encore plus géniales.

Du point de vue de la visualisation de données, un graphique en lignes étagées fonctionnera en fait mieux dans ce cas. Et nous pouvons en créer un avec une seule petite modification. 

Il suffit de changer la fonction `line()` en `stepLine()` et votre graphique en lignes deviendra votre graphique en lignes étagées :

```javascript
// créer un graphique en lignes étagées
var chart = anychart.stepLine();

// créer les séries et les nommer
var firstSeries = chart.stepLine(firstSeriesData);
firstSeries.name("Roger Federer");
var secondSeries = chart.stepLine(secondSeriesData);
secondSeries.name("Rafael Nadal");
var thirdSeries = chart.stepLine(thirdSeriesData);
thirdSeries.name("Novak Djokovic");
```

Profitez de l'élégant graphique en lignes étagées alimenté par JavaScript visualisant la course aux titres du Grand Chelem entre le Big Three du tennis. (N'hésitez pas à explorer et à continuer à jouer avec son code source complet sur [CodePen](https://codepen.io/shacheeswadia/pen/zYRmXpv).)

![Un graphique en lignes étagées visualisant la course aux titres du Grand Chelem de Federer, Nadal et Djokovic. JavaScript HTML5.](https://www.freecodecamp.org/news/content/images/2022/09/line-chart-4.png)

Et voici le code complet :

```html
<html>
  <head>
    <title>Graphique en lignes JS</title>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-base.min.js"></script>
    <style type="text/css">      
      html, body, #container { 
        width: 100%; height: 100%; margin: 0; padding: 0; 
      } 
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      anychart.onDocumentReady(function () {
  
        // ajouter les données
        var data = [
          ["2003", 1, 0, 0],
          ["2004", 4, 0, 0],
          ["2005", 6, 0, 0],
          ["2006", 9, 1, 0],
          ["2007", 12, 2, 0],
          ["2008", 13, 5, 1],
          ["2009", 15, 6, 1],
          ["2010", 16, 9, 1],
          ["2011", 16, 10, 4],
          ["2012", 17, 11, 5],
          ["2013", 17, 13, 6],
          ["2014", 17, 14, 7],
          ["2015", 17, 14, 10],
          ["2016", 17, 14, 12],
          ["2017", 19, 16, 12],
          ["2018", 20, 17, 14],
          ["2019", 20, 19, 16],
          ["2020", 20, 20, 17],
          ["2021", 20, 20, 20],
          ["2022", 20, 22, 20]
        ];
  
        // créer un ensemble de données
        var dataSet = anychart.data.set(data);

        // mapper les données pour toutes les séries
        var firstSeriesData = dataSet.mapAs({x: 0, value: 1});
        var secondSeriesData = dataSet.mapAs({x: 0, value: 2});
        var thirdSeriesData = dataSet.mapAs({x: 0, value: 3});

        // créer un graphique en lignes étagées
        var chart = anychart.stepLine();

        // créer les séries et les nommer
        var firstSeries = chart.stepLine(firstSeriesData);
        firstSeries.name("Roger Federer");
        var secondSeries = chart.stepLine(secondSeriesData);
        secondSeries.name("Rafael Nadal");
        var thirdSeries = chart.stepLine(thirdSeriesData);
        thirdSeries.name("Novak Djokovic");

        // ajouter une légende et la personnaliser
        chart.legend().enabled(true).fontSize(14).padding([10, 0, 10, 0]);
  
        // ajouter un titre et le personnaliser
        chart
          .title()
          .enabled(true)
          .useHtml(true)
          .text(
            '<span style="color: #006331; font-size:20px;">Course aux titres du Grand Chelem du Big Three</span>' +
              '<br/><span style="font-size: 16px;">(Triomphes à l\'Australian Open, French Open, Wimbledon, U.S. Open)</span>'
          );
  
        // nommer les axes
        chart.yAxis().title("Titres remportés");
        chart.xAxis().title("Année");
  
        // personnaliser les marqueurs des séries
        firstSeries.hovered().markers().type("circle").size(4);
        secondSeries.hovered().markers().type("circle").size(4);
        thirdSeries.hovered().markers().type("circle").size(4);
  
        // activer les lignes de référence et supprimer la ligne y
        chart.crosshair().enabled(true).yStroke(null).yLabel(false);
  
        // changer la position de l'infobulle
        chart.tooltip().positionMode("point");
        chart.tooltip().position("right").anchor("left-center").offsetX(5).offsetY(5);
  
        // personnaliser le trait des séries dans l'état normal
        firstSeries.normal().stroke("#7b60a2", 2.5);
        secondSeries.normal().stroke("#db7346", 2.5);
        thirdSeries.normal().stroke("#43a7dc", 2.5);
  
        // spécifier où afficher le graphique
        chart.container("container");
  
        // dessiner le graphique résultant
        chart.draw();
  
      });
    </script>
  </body>
</html>
```

%[https://codepen.io/shacheeswadia/pen/zYRmXpv]

# **Conclusion**

Comme vous pouvez le voir dans ce tutoriel, la création de graphiques en lignes interactifs (et en lignes étagées) avec JavaScript peut être assez simple. Faites-moi savoir si vous avez des questions ou des suggestions.

C'est motivant de voir comment ces grands ont accompli tant de choses dans leur vie professionnelle. 

Utilisons cette inspiration pour avancer dans le domaine du développement de la visualisation de données en construisant encore plus de graphiques et de graphes (et toujours plus géniaux) !