---
title: Comment créer une heatmap interactive avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-16T23:26:39.000Z'
originalURL: https://freecodecamp.org/news/interactive-heatmap-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/heatmapchartjs.png
tags:
- name: data visualization
  slug: data-visualization
- name: Heat map
  slug: heat-map
- name: JavaScript
  slug: javascript
seo_title: Comment créer une heatmap interactive avec JavaScript
seo_desc: "By Shachee Swadia\nData visualization is a powerful tool that helps us\
  \ make sense of complex data. With it, we can spot patterns and trends that might\
  \ take much more time to become obvious just by looking at raw numbers. \nOne particularly\
  \ useful chart..."
---

Par Shachee Swadia

La visualisation de données est un outil puissant qui nous aide à comprendre des données complexes. Grâce à elle, nous pouvons repérer des motifs et des tendances qui pourraient prendre beaucoup plus de temps à devenir évidents simplement en regardant des chiffres bruts. 

Un type de graphique particulièrement utile est la **heatmap**, et je suis ravi de vous apprendre à en créer une avec JavaScript dans ce tutoriel.

## Qu'est-ce qu'une heatmap ?

Une heatmap est une représentation bidimensionnelle de l'ampleur d'un phénomène à travers des couleurs. Elle fournit un [résumé visuel rapide](https://datavizcatalogue.com/methods/heatmap.html) des valeurs élevées et basses dans les données. 

Par exemple, saviez-vous qu'en moyenne, 108 personnes sont mortes par jour dans des accidents de la route aux États-Unis en 2021 ? En utilisant une heatmap, nous pouvons analyser les jours et les heures des accidents mortels. Ce sera la visualisation que nous construirons pendant le tutoriel.

Alors, prenez votre tasse de café et plongeons dans ce guide étape par étape. À la fin, vous aurez les compétences pour créer facilement vos propres heatmaps interactives en JavaScript.

# La heatmap que nous allons construire

Voici à quoi ressemblera la heatmap finale basée sur JS :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/heatmapchart-006.png)

Prêt à plonger ? C'est parti !

# **Comment créer une heatmap JavaScript**

Super, commençons à créer une heatmap simple mais belle en utilisant JavaScript. Avec seulement quatre étapes faciles à suivre, vous aurez une heatmap interactive époustouflante en un rien de temps. 

Ne vous inquiétez pas pour un codage compliqué ou des détails techniques écrasants. Nous garderons les choses simples et faciles à comprendre.

## 1. Créer une page HTML

Tout d'abord, nous devons créer une page web qui contiendra notre super heatmap. Nous commençons par faire une page HTML de base, complète avec un élément `div` pour contenir notre graphique. Définissons également le style du `div` pour qu'il s'étende sur toute la page. Ne vous inquiétez pas, c'est très simple :

```html
<html>
  <head>
    <title>Heatmap en JavaScript</title>
    <style type="text/css">      
      html, body, #container { 
        width: 100%; margin: 0; padding: 0; 
      } 
    </style>
  </head>
  <body>
    <div id="container"></div>
  </body>
</html>
```

## 2. Inclure les fichiers JavaScript requis

D'accord, soyons réalistes : construire une heatmap JS à partir de zéro serait une vraie galère. Au lieu de cela, nous allons prendre la route la plus facile et utiliser une bibliothèque de graphiques JavaScript. 

Il existe [une tonne de bibliothèques de graphiques JS variées](https://en.wikipedia.org/wiki/Comparison_of_JavaScript_charting_libraries) là-bas. Pour ce projet, nous allons utiliser la [bibliothèque JS AnyChart](https://www.anychart.com/), qui supporte les heatmaps et est gratuite pour un usage personnel et d'autres usages non lucratifs. 

Pour faire fonctionner les choses, nous devons ajouter quelques scripts à la section `<head>` de notre page web. Plus précisément, nous devons inclure les modules de base et de heatmap. Ça semble facile, non ?

```html
<html>
  <head>
    <title>Heatmap en JavaScript</title>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-core.min.js"></script>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-heatmap.min.js"></script> 
    <style type="text/css">      
      html, body, #container { 
        width: 100%; margin: 0; padding: 0; 
      } 
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      // Tout le code pour la heatmap JS viendra ici
    </script>
  </body>
</html>
```

## 3. Ajouter les données

Chaque graphique est complet avec les données, n'est-ce pas ? Nous allons récupérer nos données depuis le [site web NSC](https://injuryfacts.nsc.org/motor-vehicle/overview/crashes-by-time-of-day-and-day-of-week/) et les ajouter à notre fichier HTML dans le format approprié.

Pour notre heatmap, chaque point de données doit inclure une valeur `x` (jour), une valeur `y` (heure), et une valeur `heat` (nombre d'accidents). Nous allons envelopper ces données dans une fonction que nous appellerons lorsque nous créerons le graphique JS.

```javascript
function getData() {
  return [
    {
      x: "Lundi",
      y: "Minuit3:59",
      heat: 705
    },
    {
      x: "Lundi",
      y: "4:007:59",
      heat: 713
    },
    {
      x: "Lundi",
      y: "8:0011:59",
      heat: 657
    },
    {
      x: "Lundi",
      y: "Midi3:59",
      heat: 957
    },
    {
      x: "Lundi",
      y: "4:007:59",
      heat: 1137
    },
    {
      x: "Lundi",
      y: "8:0011:59",
      heat: 956
    },
    {
      x: "Mardi",
      y: "Minuit3:59",
      heat: 482
    },
    {
      x: "Mardi",
      y: "4:007:59",
      heat: 641
    },
    {
      x: "Mardi",
      y: "8:0011:59",
      heat: 631
    },
    {
      x: "Mardi",
      y: "Midi3:59",
      heat: 905
    },
    {
      x: "Mardi",
      y: "4:007:59",
      heat: 1137
    },
    {
      x: "Mardi",
      y: "8:0011:59",
      heat: 986
    },
    {
      x: "Mercredi",
      y: "Minuit3:59",
      heat: 465
    },
    {
      x: "Mercredi",
      y: "4:007:59",
      heat: 616
    },
    {
      x: "Mercredi",
      y: "8:0011:59",
      heat: 627
    },
    {
      x: "Mercredi",
      y: "Midi3:59",
      heat: 914
    },
    {
      x: "Mercredi",
      y: "4:007:59",
      heat: 1159
    },
    {
      x: "Mercredi",
      y: "8:0011:59",
      heat: 1066
    },
    {
      x: "Jeudi",
      y: "Minuit3:59",
      heat: 584
    },
    {
      x: "Jeudi",
      y: "4:007:59",
      heat: 718
    },
    {
      x: "Jeudi",
      y: "8:0011:59",
      heat: 660
    },
    {
      x: "Jeudi",
      y: "Midi3:59",
      heat: 966
    },
    {
      x: "Jeudi",
      y: "4:007:59",
      heat: 1161
    },
    {
      x: "Jeudi",
      y: "8:0011:59",
      heat: 1186
    },
    {
      x: "Vendredi",
      y: "Minuit3:59",
      heat: 715
    },
    {
      x: "Vendredi",
      y: "4:007:59",
      heat: 747
    },
    {
      x: "Vendredi",
      y: "8:0011:59",
      heat: 738
    },
    {
      x: "Vendredi",
      y: "Midi3:59",
      heat: 1056
    },
    {
      x: "Vendredi",
      y: "4:007:59",
      heat: 1426
    },
    {
      x: "Vendredi",
      y: "8:0011:59",
      heat: 1631
    },
    {
      x: "Samedi",
      y: "Minuit3:59",
      heat: 1383
    },
    {
      x: "Samedi",
      y: "4:007:59",
      heat: 641
    },
    {
      x: "Samedi",
      y: "8:0011:59",
      heat: 635
    },
    {
      x: "Samedi",
      y: "Midi3:59",
      heat: 1034
    },
    {
      x: "Samedi",
      y: "4:007:59",
      heat: 1400
    },
    {
      x: "Samedi",
      y: "8:0011:59",
      heat: 1593
    },
    {
      x: "Dimanche",
      y: "Minuit3:59",
      heat: 1486
    },
    {
      x: "Dimanche",
      y: "4:007:59",
      heat: 695
    },
    {
      x: "Dimanche",
      y: "8:0011:59",
      heat: 564
    },
    {
      x: "Dimanche",
      y: "Midi3:59",
      heat: 932
    },
    {
      x: "Dimanche",
      y: "4:007:59",
      heat: 1292
    },
    {
      x: "Dimanche",
      y: "8:0011:59",
      heat: 1211
    }
  ];
}
```

## 4. Écrire le code JS nécessaire pour le graphique

Voici la partie amusante : il est temps d'écrire le code JavaScript qui rendra notre heatmap géniale.

Nous allons tout enfermer dans une fonction pour nous assurer que le code ne s'exécute que lorsque la page est prête. Nous allons créer le graphique en utilisant la fonction `heatmap()` et ajouter les données que nous avons créées à l'étape précédente.

```js
let chart = anychart.heatMap(getData());
```

Ensuite, nous allons donner au graphique un titre descriptif :

```js
chart.title("Accidents mortels de voiture aux États-Unis en 2021 par heure de la journée et jour de la semaine");
```

Enfin, nous allons définir la référence du conteneur et dessiner le graphique. Et voilà !

```js
chart.container('container');
chart.draw();
```

Et voilà. Avec juste un peu de HTML et de JavaScript, vous pouvez créer une heatmap interactive vraiment géniale. Vous pouvez voir le code entier de cette heatmap basée sur JS ci-dessous et la vérifier en direct [ici](https://playground.anychart.com/DEyz9Bjb). Après cela, nous apprendrons comment personnaliser notre heatmap de toutes sortes de manières amusantes.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/heatmapchart-001.png)

```html
<html>
  <head>
    <title>Heatmap en JavaScript</title>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-core.min.js"></script>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-heatmap.min.js"></script> 
    <style type="text/css">      
      html, body, #container { 
        width: 100%; margin: 0; padding: 0; 
      } 
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      anychart.onDocumentReady(function () {
        // créer une heatmap
        let chart = anychart.heatMap(getData());
        // nommer la heatmap
        chart.title("Accidents mortels de voiture aux États-Unis en 2021 par heure de la journée et jour de la semaine");
        // définir le conteneur pour la heatmap
        chart.container("container");
        // dessiner la heatmap
        chart.draw();
      });
      // ajouter les données
      function getData() {
        return [
          {
            x: "Lundi",
            y: "Minuit3:59",
            heat: 705
          },
          {
            x: "Lundi",
            y: "4:007:59",
            heat: 713
          },
          {
            x: "Lundi",
            y: "8:0011:59",
            heat: 657
          },
          {
            x: "Lundi",
            y: "Midi3:59",
            heat: 957
          },
          {
            x: "Lundi",
            y: "4:007:59",
            heat: 1137
          },
          {
            x: "Lundi",
            y: "8:0011:59",
            heat: 956
          },
          {
            x: "Mardi",
            y: "Minuit3:59",
            heat: 482
          },
          {
            x: "Mardi",
            y: "4:007:59",
            heat: 641
          },
          {
            x: "Mardi",
            y: "8:0011:59",
            heat: 631
          },
          {
            x: "Mardi",
            y: "Midi3:59",
            heat: 905
          },
          {
            x: "Mardi",
            y: "4:007:59",
            heat: 1137
          },
          {
            x: "Mardi",
            y: "8:0011:59",
            heat: 986
          },
          {
            x: "Mercredi",
            y: "Minuit3:59",
            heat: 465
          },
          {
            x: "Mercredi",
            y: "4:007:59",
            heat: 616
          },
          {
            x: "Mercredi",
            y: "8:0011:59",
            heat: 627
          },
          {
            x: "Mercredi",
            y: "Midi3:59",
            heat: 914
          },
          {
            x: "Mercredi",
            y: "4:007:59",
            heat: 1159
          },
          {
            x: "Mercredi",
            y: "8:0011:59",
            heat: 1066
          },
          {
            x: "Jeudi",
            y: "Minuit3:59",
            heat: 584
          },
          {
            x: "Jeudi",
            y: "4:007:59",
            heat: 718
          },
          {
            x: "Jeudi",
            y: "8:0011:59",
            heat: 660
          },
          {
            x: "Jeudi",
            y: "Midi3:59",
            heat: 966
          },
          {
            x: "Jeudi",
            y: "4:007:59",
            heat: 1161
          },
          {
            x: "Jeudi",
            y: "8:0011:59",
            heat: 1186
          },
          {
            x: "Vendredi",
            y: "Minuit3:59",
            heat: 715
          },
          {
            x: "Vendredi",
            y: "4:007:59",
            heat: 747
          },
          {
            x: "Vendredi",
            y: "8:0011:59",
            heat: 738
          },
          {
            x: "Vendredi",
            y: "Midi3:59",
            heat: 1056
          },
          {
            x: "Vendredi",
            y: "4:007:59",
            heat: 1426
          },
          {
            x: "Vendredi",
            y: "8:0011:59",
            heat: 1631
          },
          {
            x: "Samedi",
            y: "Minuit3:59",
            heat: 1383
          },
          {
            x: "Samedi",
            y: "4:007:59",
            heat: 641
          },
          {
            x: "Samedi",
            y: "8:0011:59",
            heat: 635
          },
          {
            x: "Samedi",
            y: "Midi3:59",
            heat: 1034
          },
          {
            x: "Samedi",
            y: "4:007:59",
            heat: 1400
          },
          {
            x: "Samedi",
            y: "8:0011:59",
            heat: 1593
          },
          {
            x: "Dimanche",
            y: "Minuit3:59",
            heat: 1486
          },
          {
            x: "Dimanche",
            y: "4:007:59",
            heat: 695
          },
          {
            x: "Dimanche",
            y: "8:0011:59",
            heat: 564
          },
          {
            x: "Dimanche",
            y: "Midi3:59",
            heat: 932
          },
          {
            x: "Dimanche",
            y: "4:007:59",
            heat: 1292
          },
          {
            x: "Dimanche",
            y: "8:0011:59",
            heat: 1211
          }
        ];
      }
    </script>
  </body>
</html>
```

Cette heatmap est à la fois visuellement attrayante et informative. En examinant le graphique, il devient clair qu'il y a certains moments où le nombre d'accidents est significativement plus élevé. Il n'est pas surprenant de voir que ces heures de pointe sont pendant les week-ends et les heures sombres de la journée.

Mais il y a beaucoup plus de choses que nous pouvons faire avec notre heatmap...

# **Comment personnaliser une heatmap JS**

Comme nous l'avons vu, avoir le graphique de base prêt était vraiment simple et rapide. Mais il y a tellement plus que nous pouvons faire pour améliorer la heatmap. Ce n'est pas si difficile, non plus. 

## Comment changer la palette de couleurs

Nous pouvons utiliser une palette de couleurs divergente pour rendre notre heatmap JavaScript plus efficace pour mettre en évidence les données. Ce type de schéma de couleurs aide à souligner la différence entre les valeurs élevées et basses, avec moins étant bon et plus étant alarmant. 

Nous pouvons définir quatre couleurs et des plages de valeurs en utilisant une échelle de couleurs ordinales, puis définir les couleurs du graphique pour utiliser cette échelle de couleurs. De cette façon, nous pouvons créer une heatmap qui attire rapidement l'attention du spectateur sur les points de données les plus significatifs.

Voici le code pour faire cela :

```
let colorScale = anychart.scales.ordinalColor();
colorScale.ranges([
  { less: 500, color: "#B0D8A4" },
  { from: 500, to: 900, color: "#FEE191" },
  { from: 900, to: 1300, color: "#FD8060" },
  { greater: 1300, color: "#CC333F" }
]);
chart.colorScale(colorScale);
```

Et voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/heatmapchart-002.png)

## Comment modifier le style de survol

Lorsque nous changeons la palette de couleurs de notre heatmap, nous devons également modifier les couleurs de survol pour qu'elles correspondent aux couleurs de base. Cela est simple à réaliser avec la fonction `color.darken`. 

Nous pouvons définir les paramètres du graphique et les paramètres de survol du graphique pour nous assurer que les couleurs de survol correspondent aux couleurs de base. Cela nous permet de créer une heatmap visuellement cohérente et facile à lire, la rendant plus efficace pour communiquer les données sous-jacentes.

```
chart
  .hovered()
  .fill(function () {
    return anychart.color.darken(this.sourceColor, 0.25);
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/heatmapchart-003.png)

## Comment changer les étiquettes

Par défaut, les étiquettes sur notre heatmap montrent les nombres réels. Mais nous pouvons personnaliser les étiquettes pour fournir une plus grande flexibilité et rendre le graphique plus facile à lire. 

Nous pouvons activer le HTML pour les étiquettes afin de permettre des options de formatage plus grandes. Ensuite, nous pouvons configurer les étiquettes pour qu'elles s'affichent de 'faible' à 'extrême' en fonction de la valeur de la tuile. Nous pouvons également faire en sorte que les valeurs 'élevées' et 'extrêmes' apparaissent en gras pour les faire ressortir.

```javascript
// activer le html pour les étiquettes
chart.labels().useHtml(true);

// configurer les étiquettes
chart.labels().format(function () {
  var heat = this.heat;
  if (heat < 500) return "Faible";
  if (heat < 1000) return "Moyen";
  if (heat < 1500) return "<span style='font-weight:bold'>Élevé</span>";
  if (heat >= 1500) return "<span style='font-weight:bold'>Extrême</span>";
});
```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/heatmapchart-004.png)

Dans la version finale, j'ai décidé de supprimer définitivement les étiquettes puisque les couleurs sont assez indicatives des valeurs.

## Comment formater le titre et l'infobulle

Il est maintenant temps de rendre notre visualisation de heatmap JS encore plus excitante avec quelques ajustements de formatage. 

Tout d'abord, nous allons activer le HTML pour l'infobulle, afin de pouvoir la personnaliser avec un formatage accrocheur. Nous allons afficher le nombre d'accidents dans l'en-tête et le jour ainsi que le timing dans le corps de l'infobulle. Cela ajoutera plus de contexte et aidera l'utilisateur à mieux comprendre les données.

```javascript
chart.tooltip().title().useHtml(true);
chart
  .tooltip()
  .useHtml(true)
  .titleFormat(function () {
    return "Accidents - " + this.heat;
  })
  .format(function () {
    return (
      '<span style="color: #CECECE">Jour : </span>' +
      this.x +
      "<br/>" +
      '<span style="color: #CECECE">Heure : </span>' +
      this.y
    );
  });
```

Ajoutons également un peu de remplissage sous le titre principal pour le rendre plus espacé et visuellement attrayant :

```javascript
chart
  .title()
  .enabled(true)
  .text("Accidents mortels de voiture aux États-Unis en 2021 par heure de la journée et jour de la semaine")
  .padding([0, 0, 20, 0]);	
```

Voici à quoi ressemblent ces modifications :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/heatmapchart-005.png)

## Comment modifier les axes

Pour une meilleure lisibilité, nous pouvons ajouter un remplissage entre les étiquettes des axes et les tuiles du graphique et supprimer les lignes des axes puisque les tuiles forment une frontière par elles-mêmes.

```javascript
chart.xAxis().stroke(null);
chart.yAxis().stroke(null);
chart.yAxis().labels().padding([0, 10, 0, 0]);
chart.xAxis().labels().padding([0, 0, 10, 0]);
```

Et voilà ! Avec juste quelques changements esthétiques, nous avons transformé une simple heatmap en une visualisation époustouflante qui fait vraiment passer un message puissant. Vous pouvez la vérifier ci-dessous avec le code source complet, et vous pouvez jeter un coup d'œil à la version interactive de la heatmap et jouer avec le code en direct [ici](https://playground.anychart.com/UDF2ym4E).

![Image](https://www.freecodecamp.org/news/content/images/2023/05/heatmapchart-006-1.png)

```html
<html>
  <head>
    <title>Heatmap en JavaScript</title>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-core.min.js"></script>
    <script src="https://cdn.anychart.com/releases/8.11.0/js/anychart-heatmap.min.js"></script> 
    <style type="text/css">      
      html, body, #container { 
        width: 100%; margin: 0; padding: 0; 
      } 
    </style>
  </head>
  <body>  
    <div id="container"></div>
    <script>
      anychart.onDocumentReady(function () {
        // créer une heatmap
        var chart = anychart.heatMap(getData());
        // définir une échelle de couleurs personnalisée
        var colorScale = anychart.scales.ordinalColor();
        colorScale.ranges([
          { less: 500, color: "#B0D8A4" },
          { from: 500, to: 900, color: "#FEE191" },
          { from: 900, to: 1300, color: "#FD8060" },
          { greater: 1300, color: "#CC333F" }
        ]);
        chart.colorScale(colorScale);
        // styliser la coloration dans l'état survolé
        chart
          .hovered()
          .fill(function () {
            return anychart.color.darken(this.sourceColor, 0.25);
          });
        // masquer les étiquettes
        chart.labels(false);
        // personnaliser les axes
        chart.xAxis().stroke(null);
        chart.yAxis().stroke(null);
        chart.yAxis().labels().padding([0, 10, 0, 0]);
        chart.xAxis().labels().padding([0, 0, 10, 0]);
        // définir l'infobulle
        chart.tooltip().title().useHtml(true);
        chart
          .tooltip()
          .useHtml(true)
          .titleFormat(function () {
            return "Accidents - " + this.heat;
          })
          .format(function () {
            return (
              '<span style="color: #CECECE">Jour : </span>' +
              this.x +
              "<br/>" +
              '<span style="color: #CECECE">Heure : </span>' +
              this.y
            );
          });
        // nommer la heatmap
        chart
          .title()
          .enabled(true)
          .text("Accidents mortels de voiture aux États-Unis en 2021 par heure de la journée et jour de la semaine")
          .padding([0, 0, 20, 0]);
        // définir le conteneur pour la heatmap
        chart.container("container");
        // dessiner la heatmap
        chart.draw();
      });
      // ajouter les données
      function getData() {
        return [
          {
            x: "Lundi",
            y: "Minuit3:59",
            heat: 705
          },
          {
            x: "Lundi",
            y: "4:007:59",
            heat: 713
          },
          {
            x: "Lundi",
            y: "8:0011:59",
            heat: 657
          },
          {
            x: "Lundi",
            y: "Midi3:59",
            heat: 957
          },
          {
            x: "Lundi",
            y: "4:007:59",
            heat: 1137
          },
          {
            x: "Lundi",
            y: "8:0011:59",
            heat: 956
          },
          {
            x: "Mardi",
            y: "Minuit3:59",
            heat: 482
          },
          {
            x: "Mardi",
            y: "4:007:59",
            heat: 641
          },
          {
            x: "Mardi",
            y: "8:0011:59",
            heat: 631
          },
          {
            x: "Mardi",
            y: "Midi3:59",
            heat: 905
          },
          {
            x: "Mardi",
            y: "4:007:59",
            heat: 1137
          },
          {
            x: "Mardi",
            y: "8:0011:59",
            heat: 986
          },
          {
            x: "Mercredi",
            y: "Minuit3:59",
            heat: 465
          },
          {
            x: "Mercredi",
            y: "4:007:59",
            heat: 616
          },
          {
            x: "Mercredi",
            y: "8:0011:59",
            heat: 627
          },
          {
            x: "Mercredi",
            y: "Midi3:59",
            heat: 914
          },
          {
            x: "Mercredi",
            y: "4:007:59",
            heat: 1159
          },
          {
            x: "Mercredi",
            y: "8:0011:59",
            heat: 1066
          },
          {
            x: "Jeudi",
            y: "Minuit3:59",
            heat: 584
          },
          {
            x: "Jeudi",
            y: "4:007:59",
            heat: 718
          },
          {
            x: "Jeudi",
            y: "8:0011:59",
            heat: 660
          },
          {
            x: "Jeudi",
            y: "Midi3:59",
            heat: 966
          },
          {
            x: "Jeudi",
            y: "4:007:59",
            heat: 1161
          },
          {
            x: "Jeudi",
            y: "8:0011:59",
            heat: 1186
          },
          {
            x: "Vendredi",
            y: "Minuit3:59",
            heat: 715
          },
          {
            x: "Vendredi",
            y: "4:007:59",
            heat: 747
          },
          {
            x: "Vendredi",
            y: "8:0011:59",
            heat: 738
          },
          {
            x: "Vendredi",
            y: "Midi3:59",
            heat: 1056
          },
          {
            x: "Vendredi",
            y: "4:007:59",
            heat: 1426
          },
          {
            x: "Vendredi",
            y: "8:0011:59",
            heat: 1631
          },
          {
            x: "Samedi",
            y: "Minuit3:59",
            heat: 1383
          },
          {
            x: "Samedi",
            y: "4:007:59",
            heat: 641
          },
          {
            x: "Samedi",
            y: "8:0011:59",
            heat: 635
          },
          {
            x: "Samedi",
            y: "Midi3:59",
            heat: 1034
          },
          {
            x: "Samedi",
            y: "4:007:59",
            heat: 1400
          },
          {
            x: "Samedi",
            y: "8:0011:59",
            heat: 1593
          },
          {
            x: "Dimanche",
            y: "Minuit3:59",
            heat: 1486
          },
          {
            x: "Dimanche",
            y: "4:007:59",
            heat: 695
          },
          {
            x: "Dimanche",
            y: "8:0011:59",
            heat: 564
          },
          {
            x: "Dimanche",
            y: "Midi3:59",
            heat: 932
          },
          {
            x: "Dimanche",
            y: "4:007:59",
            heat: 1292
          },
          {
            x: "Dimanche",
            y: "8:0011:59",
            heat: 1211
          }
        ];
      }
    </script>
  </body>
</html>
```

# Conclusion

En conclusion, la visualisation de données est un outil incroyablement puissant qui peut nous aider à découvrir des informations importantes à partir de nos données. Et avec JavaScript, créer des graphiques beaux et percutants, comme une heatmap, peut être un jeu d'enfant. 

Alors n'ayez pas peur d'expérimenter avec différents types de graphiques, styles et bibliothèques pour créer vos propres visualisations percutantes. Et surtout, n'oubliez pas de rester en sécurité sur les routes !