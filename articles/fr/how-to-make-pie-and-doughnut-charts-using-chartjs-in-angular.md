---
title: Tutoriel Chart.js – Comment créer des graphiques en camembert et en anneau
  dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-31T17:03:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-pie-and-doughnut-charts-using-chartjs-in-angular
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/piechart-1.png
tags:
- name: Angular
  slug: angular
- name: chartjs
  slug: chartjs
- name: data analysis
  slug: data-analysis
seo_title: Tutoriel Chart.js – Comment créer des graphiques en camembert et en anneau
  dans Angular
seo_desc: 'By Swatej Patil

  In this tutorial we will learn how to create a simple pie and doughnut chart using
  the Chart.js library in an Angular application.

  What is Chart.js?

  Chart.js is a JavaScript library for building charts. It''s designed to be intuitive
  a...'
---

Par Swatej Patil

Dans ce tutoriel, nous allons apprendre à créer un simple graphique en camembert et en anneau en utilisant la bibliothèque Chart.js dans une application Angular.

## Qu'est-ce que Chart.js ?

Chart.js est une bibliothèque JavaScript pour créer des graphiques. Elle est conçue pour être intuitive et simple, mais elle est suffisamment puissante pour construire des visualisations complexes.

Elle offre une large gamme de types de graphiques, y compris les graphiques en barres, les graphiques en lignes, les graphiques en camembert, les graphiques en nuage de points, et bien d'autres. Chart.js est open-source et peut être utilisé sans aucune restriction sur des projets privés ou commerciaux.

### **Prérequis**

Avant de commencer à créer les graphiques, assurez-vous de répondre aux prérequis suivants :

* Compréhension de base du HTML/CSS et de TypeScript, en particulier la compréhension des concepts orientés objet des classes et méthodes TypeScript.
* Node.js version 10 ou supérieure et le gestionnaire de paquets NPM ou Yarn. Vous pouvez télécharger Node.js depuis [ici](https://nodejs.org/en/download/).

## Comment installer Angular CLI

Nous allons utiliser Angular CLI pour générer une application de démarrage pour notre projet. Vous pouvez installer Angular CLI en exécutant la commande suivante dans un terminal ou une fenêtre PowerShell :

```
npm install -g @angular/cli
```

Si vous avez déjà Angular CLI installé, vous pouvez ignorer cette étape.

## Comment créer une application Angular

Maintenant, créons une application Angular qui contiendra nos graphiques. Dans un terminal, exécutez les commandes suivantes :

```bash
 ng new angular-chartjs

```

Maintenant que notre application Angular a été créée, naviguez vers le dossier du projet et démarrez le serveur de développement local en utilisant la commande suivante :

```bash
cd angular-chartjs
ng serve -o

```

Une fenêtre de navigateur s'ouvrira sur `http://localhost:4200/` et vous pourrez voir votre application Angular en cours d'exécution.

## Comment installer le package Chart.js

Ouvrez maintenant une nouvelle fenêtre de terminal dans le même répertoire et installez la bibliothèque Chart.js en utilisant la commande suivante :

```bash
npm install chart.js

```

Maintenant, nous devons créer deux composants Angular, l'un pour le graphique en camembert et l'autre pour le graphique en anneau. Vous pouvez les créer facilement avec Angular CLI en exécutant les commandes suivantes :

```bash
ng generate component pie-chart
ng generate component doughnut-chart

```

## Comment créer un graphique en camembert avec Chart.js

Un graphique en camembert est un graphique circulaire qui affiche les données en tranches, où chaque tranche représente une catégorie de données. La taille de chaque tranche représente la proportion de la catégorie par rapport à l'ensemble des données.

Les graphiques en camembert sont un moyen efficace de montrer la répartition des données en catégories, en particulier lorsque les données représentent des parties d'un tout. Ils sont utiles lorsque vous souhaitez montrer combien chaque catégorie contribue au total.

Quand utiliser les graphiques en camembert :

* Pour montrer les proportions de différentes catégories dans un tout
* Pour comparer les tailles relatives de différentes catégories
* Pour démontrer comment chaque catégorie contribue au tout

Les graphiques en camembert sont couramment utilisés en entreprise et en économie pour montrer la distribution des dépenses, des parts de marché, ou d'autres aspects de la performance de l'entreprise.

Maintenant que nous avons créé les composants, nous allons passer à la création du graphique en camembert.

Naviguez vers le composant `/src/app/pie-chart` et ouvrez le fichier `pie-chart.component.html` puis collez le code suivant :

```html
<div class="chart-container">
      <canvas  id="MyChart" >{{ chart }}</canvas>
</div>

```

Nous avons simplement créé un conteneur, et à l'intérieur de ce conteneur, une toile avec un identifiant `MyChart`. Nous avons utilisé l'interpolation de chaînes d'Angular pour rendre la variable `chart`, que nous allons créer bientôt.

À l'intérieur du composant pie-chart, ouvrez le fichier `pie-chart.component.ts` et importez la bibliothèque Chart.js en utilisant la commande suivante :

```bash
import Chart from 'chart.js/auto';

```

Maintenant, créons la variable `chart` dont nous avons parlé précédemment. Cette variable contiendra les informations de nos graphiques.

```tsx
public chart: any;

```

Maintenant, nous allons créer une méthode pour le graphique en camembert. Cela inclura les données et les étiquettes pour notre graphique.

Copiez le code suivant et collez-le dans le fichier `pie-chart.component.ts` en dessous de la fonction `ngOnInit()` :

```tsx
createChart(){

    this.chart = new Chart("MyChart", {
      type: 'pie', //ceci indique le type de graphique

      data: {// valeurs sur l'axe X
        labels: ['Rouge', 'Rose','Vert','Jaune','Orange','Bleu', ],
	       datasets: [{
    label: 'Mon Premier Jeu de Données',
    data: [300, 240, 100, 432, 253, 34],
    backgroundColor: [
      'red',
      'pink',
      'green',
			'yellow',
      'orange',
      'blue',			
    ],
    hoverOffset: 4
  }],
      },
      options: {
        aspectRatio:2.5
      }

    });
  }


```

Ici, nous avons défini le `type` de graphique comme `pie`. Nous avons donné des étiquettes comme les noms de couleurs courantes. Et nous avons ajouté des valeurs de données, qui seront automatiquement allouées à une portion du camembert dans le graphique en camembert.

Nous voulons que notre fonction `createChart()` s'exécute dès que la page se charge. Pour ce faire, nous devons appeler la fonction dans le `ngOnInit()` :

```tsx
ngOnInit(): void {
    this.createChart();
  }


```

Enfin, nous devons ajouter le sélecteur HTML du composant pie-chart au fichier `app.component.html`. Supprimez le code de modèle initial d'Angular et ajoutez le suivant :

```html
<app-pie-chart></app-pie-chart>

```

Enregistrez tous les fichiers et la fenêtre du navigateur se rafraîchira automatiquement. Votre premier graphique en camembert est prêt !

![Image](https://www.freecodecamp.org/news/content/images/2023/01/piechart.png)
_Notre graphique en camembert_

## Comment créer un graphique en anneau avec Chart.js

Un graphique en anneau est une variation du graphique en camembert et sert le même but de représenter des données dans un format circulaire. Il est composé de plusieurs secteurs, où chaque secteur représente une valeur de données, la taille de chaque secteur étant proportionnelle à sa valeur.

Vous pouvez utiliser un graphique en anneau :

* Pour montrer une relation parties-tout dans les données
* Pour comparer différentes catégories de données
* Pour montrer la progression vers un objectif ou une cible

Maintenant, nous allons passer à la création du graphique en anneau. Puisque les graphiques en anneau et les graphiques en camembert peuvent être utilisés de manière interchangeable, nous n'avons pas besoin de modifier quoi que ce soit sauf le type de graphique. Suivez simplement les mêmes étapes que vous avez faites jusqu'à présent et assurez-vous de les faire sur le composant du graphique en anneau.

Collez le même code pour la méthode `createChart()` dans le fichier `doughnut-chart.component.ts` en dessous de la fonction `ngOnInit()`. Vous devez simplement changer le mot-clé pour le type de graphique de `pie` à `doughnut`. Votre code devrait ressembler à ce qui suit :

```tsx
createChart(){

    this.chart = new Chart("MyChart", {
      type: 'doughnut', //ceci indique le type de graphique

      data: {// valeurs sur l'axe X
        labels: ['Rouge', 'Rose','Vert','Jaune','Orange','Bleu', ],
	       datasets: [{
    label: 'Mon Premier Jeu de Données',
    data: [300, 240, 100, 432, 253, 34],
    backgroundColor: [
      'red',
      'pink',
      'green',
			'yellow',
      'orange',
      'blue',			
    ],
    hoverOffset: 4
  }],
      },
      options: {
        aspectRatio:2.5
      }

    });
  }

```

Appelez la fonction `createChart()` dans `ngOnInit()` et votre graphique en anneau sera prêt.

```tsx
ngOnInit(): void {
    this.createChart();
  }


```

Enfin, nous devons ajouter le sélecteur HTML pour le composant du graphique en anneau au fichier `app.component.html`.

```html
<app-doughnut-chart></app-doughnut-chart>

```

Votre résultat peut ressembler à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/doughtnutchart.png)
_Notre graphique en anneau_

## Conclusion

Chart.js est une bibliothèque très utile et puissante. Si vous souhaitez inclure un type de graphique dans votre application Angular, il est alors très facile de les créer avec Chart.js.

Le code complet de cette application Angular est hébergé sur mon [Dépôt GitHub](https://github.com/SwatejPatil/Pie-and-Doughnut-Charts-using-ChartJs-in-Angular/upload/main).

J'espère que vous avez trouvé ce tutoriel utile. Merci pour votre lecture !

### Articles connexes

* [Comment créer des graphiques en barres et en lignes en utilisant Chart.js dans Angular](https://www.freecodecamp.org/news/chart-js-zooom-plugin/)