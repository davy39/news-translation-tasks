---
title: La Méthode de Régression des Moindres Carrés – Comment Trouver la Droite de
  Meilleur Ajustement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T18:59:02.000Z'
originalURL: https://freecodecamp.org/news/the-least-squares-regression-method-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d1740569d1a4ca1c34.jpg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: '#Regression'
  slug: regression
seo_title: La Méthode de Régression des Moindres Carrés – Comment Trouver la Droite
  de Meilleur Ajustement
seo_desc: 'By Diogo Spínola

  Would you like to know how to predict the future with a simple formula and some
  data?

  There are multiple ways to tackle the problem of attempting to predict the future.
  But we''re going to look into the theory of how we could do it wi...'
---

Par Diogo Spínola

Souhaitez-vous savoir comment prédire l'avenir avec une formule simple et quelques données ?

Il existe plusieurs façons d'aborder le problème de la prédiction de l'avenir. Mais nous allons examiner la théorie de la manière dont nous pourrions le faire avec la formule **Y = a + b * X**.

Après avoir couvert la théorie, nous allons créer un projet JavaScript. Cela nous aidera à visualiser plus facilement la formule en action en utilisant [Chart.js](https://www.chartjs.org/) pour représenter les données.

## Qu'est-ce que la méthode de régression des moindres carrés et pourquoi l'utiliser ?

Les moindres carrés sont une méthode pour appliquer la régression linéaire. Elle nous aide à prédire les résultats sur la base d'un ensemble de données existant ainsi qu'à éliminer les anomalies dans nos données. Les anomalies sont des valeurs qui sont trop bonnes, ou mauvaises, pour être vraies ou qui représentent des cas rares.

Par exemple, supposons que nous ayons une liste du nombre de sujets que les futurs ingénieurs ici chez freeCodeCamp peuvent résoudre s'ils investissent 1, 2 ou 3 heures en continu. Ensuite, nous pouvons prédire combien de sujets seront couverts après 4 heures d'étude continue même sans que ces données soient disponibles pour nous.

Cette méthode est utilisée par une multitude de professionnels, par exemple des statisticiens, des comptables, des managers et des ingénieurs (comme dans les problèmes d'apprentissage automatique).

## Mise en place d'un exemple

Avant de plonger dans la formule et le code, définissons les données que nous allons utiliser.

Pour cela, développons l'exemple mentionné précédemment.

Supposons que notre objectif est de déterminer combien de sujets sont couverts par un étudiant par heure d'apprentissage.

Chaque paire (X, Y) représentera un étudiant. Puisque nous avons tous des rythmes d'apprentissage différents, le nombre de sujets résolus peut être plus élevé ou plus faible pour le même temps investi.

| Heures (X) 	| Sujets Résolus (Y) 	|
|:---------:	|:-----------------:	|
| 1       	    | 1.5               	|
| 1.2         	| 2                 	|
| 1.5       	| 3                 	|
| 2         	| 1.8               	|
| 2.3       	| 2.7               	|
| 2.5       	| 4.7               	|
| 2.7       	| 7.1               	|
| 3         	| 10                	|
| 3.1       	| 6                 	|
| 3.2       	| 5                 	|
| 3.6       	| 8.9               	|

Vous pouvez le lire comme ceci : "Quelqu'un a passé 1 heure et a résolu 2 sujets" ou "Un étudiant après 3 heures a résolu 10 sujets".

Sur un graphique, ces points ressemblent à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-8.png)
_Chaque point est un étudiant (X, Y) et le temps qu'il a fallu à cet étudiant spécifique pour compléter un certain nombre de sujets_

**Avertissement :** Ces données sont fictives et ont été générées en appuyant sur des touches aléatoires. Je n'ai aucune idée des valeurs réelles.

## La formule

> **Y = a + bX**

La formule, pour ceux qui ne la connaissent pas, semble probablement peu impressionnante – d'autant plus que nous avons déjà les valeurs pour **Y** et **X** dans notre exemple.

Cela dit, et maintenant que nous ne sommes plus effrayés par la formule, nous devons simplement déterminer les valeurs **a** et **b**.

Pour donner un peu de contexte quant à leur signification :

* **a** est l'ordonnée à l'origine, en d'autres termes la valeur que nous attendons, en moyenne, d'un étudiant qui pratique pendant une heure. Une heure est la durée minimale que nous allons accepter dans notre ensemble de données d'exemple.
* **b** est la pente ou le coefficient, en d'autres termes le nombre de sujets résolus en une heure spécifique (**X)**. À mesure que nous augmentons le nombre d'heures (**X**) passées à étudier, **b** augmente de plus en plus.

## Calcul de "b"

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-50.png)
_Cela semble plus effrayant que cela ne l'est en réalité_

**X** et **Y** sont nos positions dans notre tableau précédent. Lorsqu'ils ont un **-** (macron) au-dessus d'eux, cela signifie que nous devons utiliser la moyenne que nous obtenons en les additionnant tous et en divisant par le nombre total :

**x** -> 1+1.2+1.5+2+2.3+2.5+2.7+3+3.1+3.2+3.6 = **2.37**

**y** -> 1,5+2+3+1,8+2,7+4,7+7,1+10+6+5+8,9 / 11 = **4.79**

Maintenant que nous avons la moyenne, nous pouvons étendre notre tableau pour inclure les nouveaux résultats :

| Heures (X) 	| Sujets Résolus (Y) 	| (X - x) 	| (y - y) 	| (X - x)*(y - y) 	| (x - x) 	|
|:---------:	|:-----------------:	|:-------:	|:-------:	|:---------------:	|:--------:	|
|     1     	|        1.5        	|   -1.37 	|  -3.29  	|            4.51 	|     1.88 	|
|    1.2    	|         2         	|   -1.17 	|  -2.79  	|            3.26 	|     1.37 	|
|    1.5    	|         3         	|   -0.87 	|  -1.79  	|            1.56 	|     0.76 	|
|     2     	|        1.8        	|   -0.37 	|  -2.99  	|            1.11 	|     0.14 	|
|    2.3    	|        2.7        	|   -0.07 	|  -2.09  	|            0.15 	|     0.00 	|
|    2.5    	|        4.7        	|    0.13 	|  -0.09  	|           -0.01 	|     0.02 	|
|    2.7    	|        7.1        	|    0.33 	|   2.31  	|            0.76 	|     0.11 	|
|     3     	|         10        	|    0.63 	|   5.21  	|            3.28 	|     0.40 	|
|    3.1    	|         6         	|    0.73 	|   1.21  	|            0.88 	|     0.53 	|
|    3.2    	|         5         	|    0.83 	|   0.21  	|            0.17 	|     0.69 	|
|    3.6    	|        8.9        	|    1.23 	|   4.11  	|            5.06 	|     1.51 	|

Le symbole étrange sigma (****) nous indique de tout additionner :

**(x - x)*(y - y)** -> 4.51+3.26+1.56+1.11+0.15+-0.01+0.76+3.28+0.88+0.17+5.06 = **20.73**

**(x - x)** -> 1.88+1.37+0.76+0.14+0.00+0.02+0.11+0.40+0.53+0.69+1.51 = **7.41**

Et enfin nous faisons **20.73 / 7.41** et nous obtenons **b = 2.8**

**Note :** Lorsque vous utilisez une calculatrice d'expression, comme celle disponible dans Ubuntu, -2 retourne -4 au lieu de 4. Pour éviter cela, entrez (-2).

## Calcul de "a"

Il ne reste plus que **a**, pour lequel la formule est **y = a +** **b x.** Nous avons déjà obtenu toutes ces autres valeurs, donc nous pouvons les substituer et nous obtenons :

* 4.79 = **a** + 2.8*2.37
* 4.79 = **a** + 6.64
* **a** = -6.64+4.79
* **a = -1.85**

## Le résultat

Notre formule finale devient :

> **Y = -1.85 + 2.8*X**

Maintenant, nous remplaçons le **X** dans notre formule par chaque valeur que nous avons :

| Heures (X) 	| -1.85 + 2.8 * X 	|
|:---------:	|:---------------:	|
|     1     	|       0.95      	|
|    1.2    	|       1.51      	|
|    1.5    	|       2.35      	|
|     2     	|       3.75      	|
|    2.3    	|       4.59      	|
|    2.5    	|       5.15      	|
|    2.7    	|       5.71      	|
|     3     	|       6.55      	|
|    3.1    	|       6.83      	|
|    3.2    	|       7.11      	|
|    3.6    	|       8.23      	|

Ce qui donne un graphique qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-9.png)
_Nous avons maintenant une ligne qui représente le nombre de sujets que nous nous attendons à résoudre pour chaque heure d'étude_

Si nous voulons prédire combien de sujets nous nous attendons à ce qu'un étudiant résolve avec 8 heures d'étude, nous le remplaçons dans notre formule :

* **Y = -1.85 + 2.8*8**
* **Y = 20.55**

Et sur un graphique, nous pouvons voir :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-10.png)
_Plus c'est loin dans le futur, moins nous devons nous attendre à une grande précision_

## Limites

Gardez toujours à l'esprit les limites d'une méthode. Cela vous aidera, espérons-le, à éviter des résultats incorrects.

Et cette méthode, comme toute autre, a ses limites. En voici quelques-unes :

* Elle ne prend pas en compte la complexité des sujets résolus. Un sujet couvert au début de la "[Certification en Conception Web Réactive](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/)" prendra probablement moins de temps à apprendre et à résoudre que de faire l'un des projets finaux. Donc, si les données que nous avons proviennent de différents points de départ d'un cours, les prédictions ne seront pas précises.
* Il est impossible pour quelqu'un d'étudier 240 heures en continu ou de résoudre plus de sujets que ceux disponibles. Néanmoins, la méthode nous permet de prédire ces valeurs. À ce stade, la méthode ne donne plus de résultats précis puisque c'est une impossibilité.

## Exemple de projet JavaScript

Faire cela à la main n'est pas nécessaire. Nous pouvons créer notre projet où nous entrons les valeurs X et Y, il dessine un graphique avec ces points et applique la formule de régression linéaire.

Le dossier du projet aura le contenu suivant :

```
src/
  |-public // dossier avec le contenu que nous allons alimenter dans le navigateur
    |-index.html
    |-style.css
    |-least-squares.js
  package.json
  server.js // notre serveur Node.js
```

Et **package.json** :

```json
{
  "name": "least-squares-regression",
  "version": "1.0.0",
  "description": "Visualiser les moindres carrés linéaires",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "server-debug": "nodemon --inspect server.js"
  },
  "author": "daspinola",
  "license": "MIT",
  "devDependencies": {
    "nodemon": "2.0.4"
  },
  "dependencies": {
    "express": "4.17.1"
  }
}

```

Une fois que nous avons le package.json et que nous exécutons _npm install_, nous aurons Express et nodemon disponibles. Vous pouvez les remplacer par d'autres si vous préférez, mais j'utilise ceux-ci par commodité.

Dans **server.js** :

```js
const express = require('express')
const path = require('path')

const app = express()

app.use(express.static(path.join(__dirname, 'public')))

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname, 'public/index.html'))
})

app.listen(5000, function () {
  console.log(`Listening on port ${5000}!`)
})
```

Ce petit serveur est conçu pour que nous puissions accéder à notre page lorsque nous écrivons dans le navigateur _localhost:5000._ Avant de l'exécuter, créons les fichiers restants :

**public/index.html**

```html
<html>
  <head>
    <title>Least Squares Regression</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div class="container">
      <div class="left-half">
        <div>
          <input type="number" class="input-x" placeholder="X">
          <input type="number" class="input-y" placeholder="Y">

          <button class="btn-update-graph">Add</button> 
        </div>
        <div>
          <span class="span-formula"></span>
        </div>
        <div>
          <table class="table-pairs">
            <thead>
              <th>
                X
              </th>
              <th>
                Y
              </th>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
      <div class="right-half">
        <canvas id="myChart"></canvas>
      </div>
    </div>
    <script src="/js/least-squares.js"></script>
  </body>
</html>
```

Nous créons nos éléments :

* Deux entrées pour nos paires, une pour X et une pour Y
* Un bouton pour ajouter ces valeurs à un tableau
* Une balise span pour afficher la formule actuelle à mesure que les valeurs sont ajoutées
* Un tableau pour afficher les paires que nous avons ajoutées
* Et une toile pour notre graphique

Nous importons également la bibliothèque [Chart.js](https://www.chartjs.org/) avec un CDN et ajoutons nos fichiers CSS et JavaScript.

**public/style.css**

```css
.container {
  display: grid; 
}

.left-half {
  grid-column: 1;
}

.right-half {
  grid-column: 2;
}
```

Nous ajoutons quelques règles pour avoir nos entrées et notre tableau à gauche et notre graphique à droite. Cela tire parti de la grille CSS.

**public/least-squares.js**

```js
document.addEventListener('DOMContentLoaded', init, false);

function init() {
  const currentData = {
    pairs: [],
    slope: 0,
    coeficient: 0,
    line: [],
  };

  const chart = initChart();
}
 
function initChart() {
  const ctx = document.getElementById('myChart').getContext('2d');

  return new Chart(ctx, {
    type: 'scatter',
    data: {
      datasets: [{
        label: 'Scatter Dataset',
        backgroundColor: 'rgb(125,67,120)',
        data: [],
      }, {
        label: 'Line Dataset',
        fill: false,
        data: [],
        type: 'line',
      }],
    },
    options: {
      scales: {
        xAxes: [{
          type: 'linear',
          position: 'bottom',
          display: true,
          scaleLabel: {
            display: true,
            labelString: '(X)',
          },
        }],
        yAxes: [{
          type: 'linear',
          position: 'bottom',
          display: true,
          scaleLabel: {
            display: true,
            labelString: '(Y)',
          },
        }],
      },
    },
  });
}
```

Et enfin, nous initialisons notre graphique. Au début, il devrait être vide puisque nous n'avons pas encore ajouté de données.

Maintenant, si nous exécutons _npm run server-debug_ et ouvrons notre navigateur sur localhost:5000, nous devrions voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-12.png)
_Nos entrées à gauche avec un bouton d'ajout, ou un tableau avec juste les en-têtes X et Y, à droite un graphique vide_

## Ajout de fonctionnalités

L'étape suivante consiste à faire en sorte que le bouton "Ajouter" fasse quelque chose. Dans notre cas, nous voulons réaliser :

* Ajouter les valeurs X et Y au tableau
* Mettre à jour la formule lorsque nous ajoutons plus d'une paire (nous avons besoin d'au moins 2 paires pour créer une ligne)
* Mettre à jour le graphique avec les points et la ligne
* Nettoyer les entrées, juste pour qu'il soit plus facile de continuer à introduire des données

### Ajouter les valeurs au tableau

**public/least-squares.js**

```js
document.addEventListener('DOMContentLoaded', init, false);

function init() {
  const currentData = {
    pairs: [],
    slope: 0,
    coeficient: 0,
    line: [],
  };
  const btnUpdateGraph = document.querySelector('.btn-update-graph');
  const tablePairs = document.querySelector('.table-pairs');
  const spanFormula = document.querySelector('.span-formula');

  const inputX = document.querySelector('.input-x');
  const inputY = document.querySelector('.input-y');

  const chart = initChart();

  btnUpdateGraph.addEventListener('click', () => {
    const x = parseFloat(inputX.value);
    const y = parseFloat(inputY.value);

    updateTable(x, y);
  });
  
  function updateTable(x, y) {
    const tr = document.createElement('tr');
    const tdX = document.createElement('td');
    const tdY = document.createElement('td');

    tdX.innerHTML = x;
    tdY.innerHTML = y;

    tr.appendChild(tdX);
    tr.appendChild(tdY);

    tablePairs.querySelector('tbody').appendChild(tr);
  }
}

// ... reste du code tel quel
```

Nous obtenons tous les éléments que nous allons utiliser bientôt et ajoutons un événement sur le bouton "Ajouter". Cet événement récupérera les valeurs actuelles et mettra à jour notre tableau visuellement.

Nous devons analyser le montant puisque nous obtenons une chaîne. Cela sera important pour l'étape suivante lorsque nous devons appliquer la formule.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-13.png)
_Lorsque nous appuyons sur ajouter, nous devrions voir les paires dans le tableau_

### Faire les calculs

Tous les calculs dont nous parlions plus tôt (obtenir la moyenne de **X** et **Y**, calculer **b**, et calculer **a**) doivent maintenant être transformés en code. Nous allons également afficher les valeurs **a** et **b** pour les voir changer à mesure que nous ajoutons des valeurs.

**public/least-squares.js**

```js
// ... reste du code tel quel

btnUpdateGraph.addEventListener('click', () => {
  const x = parseFloat(inputX.value);
  const y = parseFloat(inputY.value);

  updateTable(x, y);
  updateFormula(x, y);
});

function updateFormula(x, y) {
  currentData.pairs.push({ x, y });
  const pairsAmount = currentData.pairs.length;

  const sum = currentData.pairs.reduce((acc, pair) => ({
    x: acc.x + pair.x,
    y: acc.y + pair.y,
  }), { x: 0, y: 0 });

  const average = {
    x: sum.x / pairsAmount,
    y: sum.y / pairsAmount,
  };

  const slopeDividend = currentData.pairs
    .reduce((acc, pair) => parseFloat(acc + ((pair.x - average.x) * (pair.y - average.y))), 0);
  const slopeDivisor = currentData.pairs
    .reduce((acc, pair) => parseFloat(acc + (pair.x - average.x) ** 2), 0);

  const slope = slopeDivisor !== 0
    ? parseFloat((slopeDividend / slopeDivisor).toFixed(2))
    : 0;

  const coeficient = parseFloat(
    (-(slope * average.x) + average.y).toFixed(2),
  );

  currentData.line = currentData.pairs
    .map((pair) => ({
      x: pair.x,
      y: parseFloat((coeficient + (slope * pair.x)).toFixed(2)),
    }));

  spanFormula.innerHTML = `Formula: Y = ${coeficient} + ${slope} * X`;
}

// ... reste du code tel quel
```

Il n'y a pas grand-chose à dire sur le code ici puisque c'est toute la théorie que nous avons vue plus tôt. Nous parcourons les valeurs pour obtenir les sommes, les moyennes et toutes les autres valeurs dont nous avons besoin pour obtenir le coefficient (**a**) et la pente (**b**).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-15.png)
_La balise span pour que nous puissions afficher la formule et la voir changer à mesure que nous ajoutons des valeurs_

Nous avons les _paires_ et _ligne_ dans la variable _current_ pour les utiliser dans l'étape suivante pour mettre à jour notre graphique.

### Mettre à jour le graphique et nettoyer les entrées

**public/least-squares.js**

```js
// ... reste du code tel quel

btnUpdateGraph.addEventListener('click', () => {
  const x = parseFloat(inputX.value);
  const y = parseFloat(inputY.value);

  updateTable(x, y);
  updateFormula(x, y);
  
  updateChart();
  
  clearInputs();
});

function updateChart() {
  chart.data.datasets[0].data = currentData.pairs;
  chart.data.datasets[1].data = currentData.line;

  chart.update();
}
  
function clearInputs() {
  inputX.value = '';
  inputY.value = '';
}

// ... reste du code tel quel
```

La mise à jour du graphique et le nettoyage des entrées de **X** et **Y** sont très simples. Nous avons deux ensembles de données, le premier (position zéro) est pour nos paires, donc nous affichons le point sur le graphique. Le second (position un) est pour notre ligne de régression.

Nous devons récupérer notre instance du graphique et appeler _update_ pour voir les nouvelles valeurs prises en compte.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-16.png)
_Il faut au moins trois valeurs pour que nous puissions tirer quelque sorte d'information de notre graphique_

## Ajout de style

Nous pouvons changer un peu notre mise en page pour qu'elle soit plus gérable. Rien de majeur, cela sert juste de rappel que nous pouvons mettre à jour l'interface utilisateur à tout moment.

**public/style.css**

```css
.container {
  display: grid; 
}

.left-half {
  grid-column: 1;
}

.right-half {
  grid-column: 2;
}

.pairs-style input[type="number"],
.pairs-style button {
  margin: 5px 0px;
}

.table-pairs {
  border-collapse: collapse;
  width: 100%;
}

.table-pairs td {
  text-align: center;
}

.table-pairs,
.table-pairs th,
.table-pairs td {
  margin: 10px 0px;
  border: 1px solid black;
}
```

**public/index.html**

```html
<html>
  <head>
    <title>Least Squares Regression</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div class="container">
      <div class="left-half">
        <div class="pairs-style">
          <div>
            <input type="number" class="input-x" placeholder="X">
          </div>
          <div>
            <input type="number" class="input-y" placeholder="Y">
          </div>
          <button class="btn-update-graph">Add</button> 
        </div>
        <div>
          <span class="span-formula">Formula: Y = a + b * X</span>
        </div>
        <div>
          <table class="table-pairs">
            <thead>
              <th>
                X
              </th>
              <th>
                Y
              </th>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </div>
      <div class="right-half">
        <canvas id="myChart"></canvas>
      </div>
    </div>
    <script src="/js/least-squares.js"></script>
  </body>
</html>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-17.png)
_Pas un grand changement, mais au moins les éléments sont un peu mieux alignés_

## Preuve de concept

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-18.png)
_Nous ajoutons les mêmes valeurs que précédemment dans la théorie et obtenons le même graphique et la même formule ! :D_

## Remarques finales

Pour des raisons de brièveté, j'ai omis beaucoup de choses qui peuvent être prises comme un exercice pour améliorer considérablement le projet. Par exemple :

* Ajouter des vérifications pour les valeurs vides et similaires
* Faire en sorte que nous puissions supprimer les données que nous avons insérées par erreur
* Ajouter une entrée pour X ou Y et appliquer la formule de données actuelle pour "prédire l'avenir", similaire au dernier exemple de la théorie

Quoi qu'il en soit, prédire l'avenir est un concept amusant même si, en réalité, le plus que nous pouvons espérer prédire est une approximation basée sur des points de données passés.

C'est une formule puissante et si vous construisez un projet en l'utilisant, j'adorerais le voir.

J'espère que cet article a été utile pour servir d'introduction à ce concept. Le code utilisé dans l'article peut être trouvé sur mon GitHub **[ici](https://github.com/daspinola/least-squares-regression)**_._

À la prochaine, en attendant, allez coder quelque chose !