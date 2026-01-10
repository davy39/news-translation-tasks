---
title: Tutoriel Chart.js – Comment créer des graphiques Marimekko avec Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-21T17:51:26.000Z'
originalURL: https://freecodecamp.org/news/chart-js-tutorial-how-to-make-marimekko-charts-in-angular
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/austin-distel-DfjJMVhwH_8-unsplash.jpg
tags:
- name: Angular
  slug: angular
- name: chartjs
  slug: chartjs
- name: charts
  slug: charts
- name: data visualization
  slug: data-visualization
seo_title: Tutoriel Chart.js – Comment créer des graphiques Marimekko avec Angular
seo_desc: "By Swatej Patil\nData visualization is an essential part of data analysis.\
  \ And charts are one of the most effective ways to present data in a clear and concise\
  \ manner. \nMarimekko charts are an excellent choice for displaying complex data\
  \ sets in a com..."
---

Par Swatej Patil

La visualisation de données est une partie essentielle de l'analyse de données. Et les graphiques sont l'un des moyens les plus efficaces de présenter des données de manière claire et concise.

Les graphiques Marimekko sont un excellent choix pour afficher des ensembles de données complexes dans un format compact et visuellement attrayant.

Un graphique Marimekko, également connu sous le nom de graphique mosaïque ou graphique mekko, est une combinaison d'un graphique à barres empilées et d'un graphique à barres empilées à 100 %. La largeur de chaque barre représente la valeur totale de la catégorie correspondante, et la hauteur de chaque barre représente la contribution relative de chaque sous-catégorie à ce total.

Dans ce tutoriel, nous explorerons comment créer un graphique Marimekko en utilisant Chart.js, une puissante bibliothèque de graphiques. Nous approfondirons les détails de la structuration des données pour les graphiques Marimekko, ainsi que la personnalisation de l'apparence et du comportement du graphique à l'aide des options et des API de Chart.js.

# **Pour commencer**

Je suppose que vous savez déjà comment créer des graphiques linéaires et à barres simples avec Chart.js dans une application Angular. Dans ce guide, certains concepts seront plus faciles à appréhender si vous avez des connaissances préalables.

Ne vous inquiétez pas si ce n'est pas le cas – je m'occupe de tout. Vous pouvez suivre mon [Tutoriel Chart.js – Comment créer des graphiques à barres et linéaires avec Angular](https://www.freecodecamp.org/news/how-to-make-bar-and-line-charts-using-chartjs-in-angular/) pour commencer.

## Comment structurer les données pour les graphiques Marimekko

Discutons de la structure de données requise pour les graphiques Marimekko avant de créer le graphique.

Les graphiques Marimekko nécessitent un tableau d'objets, chaque objet représentant une catégorie. Chaque objet doit avoir un libellé (label) et un sous-tableau d'objets, où chaque sous-objet représente une sous-catégorie.

Chaque sous-objet doit avoir un libellé et une valeur. La valeur représente la proportion de la sous-catégorie par rapport au total de sa catégorie.

Voici un exemple de la structure des données pour un graphique Marimekko :

```jsx
data: [
  {
    label: 'Catégorie 1',
    subcategories: [
      { label: 'Sous-catégorie 1', value: 10 },
      { label: 'Sous-catégorie 2', value: 20 },
      { label: 'Sous-catégorie 3', value: 30 }
    ]
  },
  {
    label: 'Catégorie 2',
    subcategories: [
      { label: 'Sous-catégorie 1', value: 40 },
      { label: 'Sous-catégorie 2', value: 50 },
      { label: 'Sous-catégorie 3', value: 60 }
    ]
  }
]

```

Dans cet exemple, nous avons deux catégories : Catégorie 1 et Catégorie 2, avec trois sous-catégories chacune. Les valeurs des sous-catégories représentent la proportion de la sous-catégorie par rapport au total de sa catégorie. Par exemple, dans la Catégorie 1, la Sous-catégorie 1 représente 10 sur 60, soit 16,7 % du total.

## Comment créer un graphique Marimekko avec Chart.js

Maintenant que nos données sont correctement structurées, passons à la création de notre graphique Marimekko avec Chart.js.

Tout d'abord, nous devons créer un élément canvas dans notre code HTML pour accueillir le graphique :

```jsx
<canvas id="marimekkoChart"></canvas>

```

Ensuite, nous devrons installer Chart.js et l'importer dans notre composant Angular :

```jsx
npm install chart.js

```

```jsx
import Chart from 'chart.js/auto';

```

Dans notre classe de composant, nous pouvons ensuite créer un nouvel objet Chart et y passer nos données et options :

```jsx
ngAfterViewInit() {
  const canvas = document.getElementById('marimekkoChart') as HTMLCanvasElement;
  const ctx = canvas.getContext('2d') as CanvasRenderingContext2D;

  const data = {
    labels: ['Catégorie 1', 'Catégorie 2'],
    datasets: [
      {
        label: 'Sous-catégorie 1',
        data: [10, 40],
        backgroundColor: 'rgba(255, 99, 132, 0.7)',
        borderWidth: 1
      },
      {
        label: 'Sous-catégorie 2',
        data: [20, 50],
        backgroundColor: 'rgba(54, 162, 235, 0.7)',
        borderWidth: 1
      },
      {
        label: 'Sous-catégorie 3',
        data: [30, 60],
        backgroundColor: 'rgba(255, 206, 86, 0.7)',
        borderWidth: 1
      }
    ]
  };

  const options = {
    indexAxis: 'y',
    plugins: {
      legend: {
        position: 'bottom'
      }
    }
  };

  const marimekkoChart = new Chart(ctx, {
    type: 'bar',
    data: data,
  });
}

```

Dans cet exemple, nous créons un graphique Marimekko avec trois sous-catégories pour deux catégories. Nous avons défini le type de graphique sur 'bar', et nous passons nos données et options. L'option 'indexAxis' est définie sur 'y' pour rendre le graphique horizontal, et l'option 'legend' est configurée pour positionner la légende au bas du graphique.

Félicitations ! Si vous avez suivi attentivement, vous ne devriez rencontrer aucune erreur et votre résultat devrait ressembler à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Mekkochart.png)

Et voilà ! Avec ce code, nous pouvons créer un graphique Marimekko avec Chart.js dans Angular.

Vous pouvez personnaliser davantage votre graphique à l'aide de diverses options et API de Chart.js, comme l'ajustement des couleurs, des étiquettes et du comportement des info-bulles (tooltips), pour le rendre encore plus informatif et attrayant.

# **Conclusion**

Chart.js est une bibliothèque très utile et puissante. Dans ce court tutoriel, nous avons vu comment créer un graphique Marimekko avec Chart.js dans Angular. Si vous souhaitez inclure n'importe quel type de graphique dans votre application Angular, il est très facile de les réaliser avec Chart.js.

Le code complet de cette application Angular est hébergé sur mon [dépôt GitHub](https://github.com/SwatejPatil/Chart.js-Tutorial-How-to-Make-a-Marimekko-Chart-in-Angular).

J'espère que vous avez trouvé ce tutoriel utile et instructif. Si vous avez des questions ou des commentaires, n'hésitez pas à me contacter sur [LinkedIn](http://www.linkedin.com/in/swatejpatil/) !

### **Articles connexes que j'ai écrits sur Chart.js :**

* [Comment créer des graphiques à barres et linéaires avec Chart.js dans Angular](https://www.freecodecamp.org/news/chart-js-zooom-plugin/)
* [Tutoriel Chart.js – Comment créer des graphiques circulaires et en anneau avec Angular](https://www.freecodecamp.org/news/how-to-make-pie-and-doughnut-charts-using-chartjs-in-angular/)
* [Comment ajouter le plugin de zoom Chart.js à une application Angular](https://www.freecodecamp.org/news/chart-js-zooom-plugin/)

Photo par [Austin Distel](https://unsplash.com/@austindistel?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/DfjJMVhwH_8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).