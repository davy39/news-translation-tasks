---
title: Comment ajouter le plugin Zoom de Chart.js à une application Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-12T18:38:17.000Z'
originalURL: https://freecodecamp.org/news/chart-js-zooom-plugin
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/chartjsZoom.jpg
tags:
- name: Angular
  slug: angular
- name: chartjs
  slug: chartjs
- name: charts
  slug: charts
seo_title: Comment ajouter le plugin Zoom de Chart.js à une application Angular
seo_desc: 'By Swatej Patil

  In this tutorial you will learn how to the Add Chart.js Zoom plugin to an Angular
  application.

  When you have a lot of data in a chart, you may want to zoom in and see the details.
  Line charts are a good way to visualise large amounts ...'
---

Par Swatej Patil

Dans ce tutoriel, vous apprendrez comment ajouter le plugin Zoom de Chart.js à une application Angular.

Lorsque vous avez beaucoup de données dans un graphique, vous pouvez vouloir zoomer et voir les détails. Les graphiques en ligne sont un bon moyen de visualiser de grandes quantités de données. Vous pouvez utiliser la fonctionnalité de zoom dans Chart.js pour explorer vos données plus en détail.

Chart.js est une bibliothèque open-source que vous pouvez utiliser pour créer de beaux graphiques dans n'importe quelle partie de votre application Angular. La fonctionnalité de zoom a été créée pour vous permettre d'agrandir certains points de données pour une inspection plus approfondie. Vous pouvez zoomer rapidement et facilement en faisant défiler avec la molette de la souris.

Voyons comment cela fonctionne.

## Installation
Je vais supposer que vous savez déjà comment utiliser Chart.js dans une application Angular pour créer des graphiques en ligne et en barres simples.

Ne vous inquiétez pas si ce n'est pas le cas – je vous ai couvert. Vous pouvez suivre mon [Tutoriel Chart.js – Comment créer des graphiques en barres et en ligne dans Angular](https://www.freecodecamp.org/news/how-to-make-bar-and-line-charts-using-chartjs-in-angular/) pour commencer.

Nous allons créer un nouveau composant Angular juste pour le graphique en ligne, puis y incorporer le plugin de zoom. Nous utiliserons une grande quantité de données pour voir à quel point le plugin Zoom est utile.

Mais d'abord, dans votre application Angular, vous devrez installer le plugin Chart.js Zoom si vous ne l'avez pas déjà. 

Ouvrez un nouveau terminal dans le dossier du projet Angular et collez la commande suivante :

```bash
npm install chartjs-plugin-zoom
```

Cela installera le plugin dans votre application Angular.

Maintenant, créons un nouveau composant Angular et réalisons le graphique en ligne. Utilisez la commande suivante pour créer un nouveau composant Angular :

```bash
ng g c line-chart
```

Cela créera un nouveau composant Angular dans le répertoire `/src`. 

Ouvrez ensuite le fichier `line-chart.component.html` et collez le code suivant :

```html
<div class="chart-container">
      <canvas  id="MyChart" >{{ chart }}</canvas>
</div>
```

Ouvrez maintenant le fichier `line-chart.component.ts` et supprimez tout le code à l'intérieur. Ensuite, collez le code suivant :

```js
import { Component, OnInit } from '@angular/core';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.css']
})
export class LineChartComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    this.createChart();
  }
  public chart: any;

  createChart() {

    this.chart = new Chart("MyChart", {
      type: 'line', //ceci indique le type de graphique

      data: {// valeurs sur l'axe X
        labels: ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche",
          "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
        datasets: [
          {
            label: "Ventes",
            data: ['467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573',
            '467', '576', '572', '79', '92', '574', '573', ],
            backgroundColor: 'blue',
            borderColor: "#084de0"
          }
        ]
      },
      options: {
        aspectRatio: 3
      }

    });
  }

}
```

Encore une fois, si vous ne savez pas comment ce code fonctionne, vous pouvez toujours vous référer à ce [Tutoriel Chart.js](https://www.freecodecamp.org/news/how-to-make-bar-and-line-charts-using-chartjs-in-angular/).

Nous devons ajouter le sélecteur HTML du composant line-chart au fichier `app.component.html`. Supprimez le code de modèle initial d'Angular et ajoutez ce qui suit :

```
<app-line-chart></app-line-chart>

```

Démarrez le serveur de développement local en utilisant la commande suivante :
```bash
ng serve -o
```

Une fenêtre de navigateur s'ouvrira sur http://localhost:4200/ et vous pourrez voir votre application Angular en cours d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/NotZoomLine.png)

Comme vous pouvez le voir, afin de présenter l'ensemble du graphique, ce graphique commence à sauter certaines étiquettes. Cela semblera pire si le graphique contient plus de données.

Ajoutons maintenant une fonction de zoom à notre graphique afin de pouvoir agrandir les points de données pour une vue plus détaillée.

## Comment ajouter le plugin Zoom de Chart.js

Ouvrez le fichier `line-chart.component.ts` et importez le plugin Zoom de Chart.js. Assurez-vous de l'enregistrer après l'avoir importé. Le code suivant vous montrera comment faire :

```js
import zoomPlugin from 'chartjs-plugin-zoom';
Chart.register(zoomPlugin);
```

Maintenant que vous avez importé le plugin, dans les options de Chart.js, nous allons ajouter le plugin et activer le zoom avec la molette.

```js
options: {
        aspectRatio: 3,
        plugins: {
          zoom: {
            zoom: {
              wheel: {
                enabled: true,
              },
              pinch: {
                enabled: true
              },
              mode: 'xy',
            }
          }
        }
      }
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/ChartjsZoom.gif)

Comme vous pouvez le voir, maintenant nous pouvons zoomer sur le point que nous voulons voir de près.

## Conclusion

Le code complet de cette application Angular est hébergé sur mon [GitHub](https://github.com/SwatejPatil/ChartJs-Zoom-Plugin-Tutorial).

J'espère que vous avez trouvé ce tutoriel utile. Si vous avez des questions ou des commentaires, n'hésitez pas à me contacter sur [LinkedIn](http://www.linkedin.com/in/swatejpatil/). Je serai plus que ravi de vous aider avec vos questions.

Merci d'avoir lu !

Photo par <a href="https://unsplash.com/@isaacmsmith?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Isaac Smith</a> sur <a href="https://unsplash.com/s/photos/line-chart?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>