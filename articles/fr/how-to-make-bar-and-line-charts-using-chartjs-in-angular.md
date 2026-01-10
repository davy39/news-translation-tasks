---
title: Tutoriel Chart.js – Comment créer des graphiques en barres et en lignes dans
  Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-23T15:35:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-bar-and-line-charts-using-chartjs-in-angular
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Line-Bar-4.jpeg
tags:
- name: Angular
  slug: angular
- name: charts
  slug: charts
seo_title: Tutoriel Chart.js – Comment créer des graphiques en barres et en lignes
  dans Angular
seo_desc: 'By Swatej Patil

  In this tutorial we will learn how to create simple bar and line charts using the
  Chart.js library in an Angular application.

  But first of all, what is Chart.js and what does it do?

  What is Chart.js?

  Chart.js is a JavaScript library f...'
---

Par Swatej Patil

Dans ce tutoriel, nous allons apprendre à créer des graphiques en barres et en lignes simples en utilisant la bibliothèque Chart.js dans une application Angular.

Mais d'abord, qu'est-ce que Chart.js et à quoi sert-il ?

## Qu'est-ce que Chart.js ?

Chart.js est une bibliothèque JavaScript pour créer des graphiques. Elle est conçue pour être intuitive et simple, mais suffisamment puissante pour construire des visualisations complexes. Elle propose une large gamme de types de graphiques, y compris des graphiques en barres, en lignes, des camemberts, des nuages de points, et bien plus encore. 

Chart.js est open-source et vous pouvez l'utiliser sans aucune restriction sur des projets privés ou commerciaux. Il est écrit en JavaScript pur et n'a pas de dépendances à d'autres bibliothèques telles que jQuery ou D3. 

Il offre également des options pour animer les mises à jour de données et ajouter de l'interactivité aux graphiques, comme des infobulles et des événements de clic.

Il a été créé par l'équipe de Plotly et il est gratuit à utiliser.

Maintenant, nous pouvons passer à la création de notre premier graphique en barres avec Chart.js.

## Prérequis
Avant de commencer à créer les graphiques, assurez-vous de répondre aux prérequis suivants :

- Vous avez une compréhension de base de HTML, CSS et TypeScript, en particulier des concepts orientés objet des classes et méthodes TypeScript.
- Vous avez Node.js version 10 ou supérieure et le gestionnaire de paquets NPM ou Yarn. Vous pouvez télécharger Node.js depuis [ici](https://nodejs.org/en/download/).

## Comment installer Angular CLI

Angular CLI est un outil officiel des développeurs d'Angular. C'est un outil en ligne de commande très utile pour initialiser et développer des applications Angular. 

Vous pouvez installer Angular CLI en exécutant la commande suivante dans un terminal ou une fenêtre PowerShell :

```shell
npm install -g @angular/cli
```

## Comment créer une application Angular

Maintenant, créons une application Angular qui contiendra nos graphiques. Dans un terminal, exécutez les commandes suivantes :

```bash
 ng new angular-chartjs
```

Maintenant que vous avez créé votre application Angular, naviguez vers le dossier du projet et démarrez le serveur de développement local en utilisant la commande suivante :

```bash
cd angular-chartjs
ng serve -o
```

Une fenêtre de navigateur s'ouvrira sur `http://localhost:4200/` et vous pourrez voir votre application Angular en cours d'exécution.

Ouvrez maintenant une nouvelle fenêtre de terminal dans le même répertoire et installez la bibliothèque Chart.js en utilisant la commande suivante :

```bash
npm install chart.js
```

Maintenant, nous devons créer deux composants Angular : un pour le graphique en barres et un autre pour le graphique en lignes. 

Vous pouvez les créer facilement avec Angular CLI en exécutant les commandes suivantes :

```bash
ng generate component bar-chart
ng generate component line-chart
```

## Comment créer un graphique en barres avec Chart.js

Un graphique en barres est une représentation graphique de données, dans laquelle les axes horizontal et vertical représentent les valeurs, et la longueur de chaque barre représente les valeurs spécifiées sur l'axe. 

Les graphiques en barres sont l'une des formes les plus courantes de graphiques lorsqu'il s'agit de représenter des données visuellement. Nous les utilisons pour identifier des tendances et des motifs dans divers ensembles de données.

Quand utiliser les graphiques en barres :

- Pour montrer plusieurs valeurs à la fois
- Pour fournir une représentation graphique des données
- Pour comparer des ensembles de données
- Pour examiner les relations entre différentes variables.

Un graphique en barres est souvent utilisé en entreprise et en économie pour montrer des comparaisons entre des produits, des services ou des entreprises. Dans notre exemple, nous avons pris les données des ventes et des profits réalisés chaque jour pendant une période de 8 jours.

Maintenant que nous avons créé les composants, nous allons passer à la création du graphique en barres.

À l'intérieur du composant bar-chart, ouvrez le fichier `bar-chart.component.html` et collez le code suivant :

```html
<div class="chart-container">
      <canvas  id="MyChart" >{{ chart }}</canvas>
</div>
```

Nous avons simplement créé un conteneur et à l'intérieur de ce conteneur une toile avec un id de `MyChart`. Nous avons utilisé l'interpolation de chaînes d'Angular pour rendre la variable `chart`, que nous allons créer dans la toile.

À l'intérieur du composant bar-chart, ouvrez le fichier `bar-chart.component.ts` et importez la bibliothèque Chart.js en utilisant les commandes suivantes :

```js
import Chart from 'chart.js/auto';
//ou
import Chart from 'chart.js';
```

Maintenant, créons la variable `chart` dont nous avons parlé précédemment. Cette variable contiendra les informations de nos graphiques.

```js
public chart: any;
```

Maintenant, nous allons créer une méthode pour le graphique en barres. Cela inclura les données et les étiquettes pour notre graphique en barres. Copiez le code suivant et collez-le dans le fichier `bar-chart.component.ts` en dessous de la fonction `ngOnInit()` :

```js
createChart(){
  
    this.chart = new Chart("MyChart", {
      type: 'bar', //ceci indique le type de graphique

      data: {// valeurs sur l'axe X
        labels: ['2022-05-10', '2022-05-11', '2022-05-12','2022-05-13',
								 '2022-05-14', '2022-05-15', '2022-05-16','2022-05-17', ], 
	       datasets: [
          {
            label: "Ventes",
            data: ['467','576', '572', '79', '92',
								 '574', '573', '576'],
            backgroundColor: 'blue'
          },
          {
            label: "Profit",
            data: ['542', '542', '536', '327', '17',
									 '0.00', '538', '541'],
            backgroundColor: 'limegreen'
          }  
        ]
      },
      options: {
        aspectRatio:2.5
      }
      
    });
  }
```

Le code ci-dessus peut sembler intimidant au premier abord, mais il est assez simple. Nous fournissons le type de graphique, les étiquettes et les données.

Nous voulons que notre fonction `createChart()` s'exécute dès que la page se charge. Pour cela, nous devons appeler la fonction dans `ngOnInit()` comme ceci :

```ts
ngOnInit(): void {
    this.createChart();
  }
```

Enfin, nous devons ajouter le sélecteur HTML du composant bar-chart au fichier `app.component.html`. Supprimez le code de modèle Angular initial et ajoutez ce qui suit :

```html
<app-bar-chart></app-bar-chart>
```

Félicitations ! Si vous avez suivi attentivement, vous ne devriez rencontrer aucune erreur et votre résultat peut ressembler à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/barchart.png)

## Comment créer un graphique en lignes avec Chart.js
Les graphiques en lignes, similaires aux graphiques en barres, sont souvent utilisés pour montrer les tendances des données au fil du temps, comme la croissance économique ou les changements des prix des actions. 

Les graphiques en lignes sont également utiles pour montrer les changements de quantités, comme la population au fil du temps ou la perte de poids sur une période de semaines. 

Avec un graphique en lignes, contrairement à un graphique en barres, vous tracez des points individuels sur les deux axes et connectez les points voisins avec des lignes droites.

Quand utiliser les graphiques en lignes :
- Lorsque les différences entre les points de données sont plus petites
- Pour montrer les tendances au fil du temps

Si vous avez créé le graphique en barres, alors créer un graphique en lignes est assez simple. Suivez simplement les mêmes étapes que vous avez faites jusqu'à présent (et assurez-vous de les faire sur le composant du graphique en lignes).

Collez le même code pour la méthode `createChart()` dans le fichier `line-chart.component.ts` en dessous de la fonction `ngOnInit()`. Vous devez simplement changer le mot-clé pour le type de graphique de `bar` à `line`. 

Votre code devrait ressembler à ce qui suit :

```ts
createChart(){
  
    this.chart = new Chart("MyChart", {
      type: 'line', //ceci indique le type de graphique

      data: {// valeurs sur l'axe X
        labels: ['2022-05-10', '2022-05-11', '2022-05-12','2022-05-13',
								 '2022-05-14', '2022-05-15', '2022-05-16','2022-05-17', ], 
	       datasets: [
          {
            label: "Ventes",
            data: ['467','576', '572', '79', '92',
								 '574', '573', '576'],
            backgroundColor: 'blue'
          },
          {
            label: "Profit",
            data: ['542', '542', '536', '327', '17',
									 '0.00', '538', '541'],
            backgroundColor: 'limegreen'
          }  
        ]
      },
      options: {
        aspectRatio:2.5
      }
      
    });
  }
```

Appelez la fonction `createChart()` dans `ngOnInit()` et votre graphique en lignes est prêt.

```ts
ngOnInit(): void {
    this.createChart();
  }
```

Enfin, nous devons ajouter le sélecteur HTML du composant line-chart au fichier `app.component.html`.

```html
<app-line-chart></app-line-chart>
```

Votre résultat peut ressembler à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/linechart.png)

Le code complet de cette application Angular est hébergé sur mon [Dépôt GitHub](https://github.com/SwatejPatil/Bar-and-Line-Charts-using-ChartJs-in-Angular). 

J'espère que vous avez trouvé ce tutoriel utile. Merci d'avoir lu !

Photo par [Luke Chesser](https://unsplash.com/@lukechesser) | Unsplash