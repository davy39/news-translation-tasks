---
title: Comment créer un graphique de type Gantt en utilisant D3 pour visualiser un
  ensemble de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-28T12:39:13.000Z'
originalURL: https://freecodecamp.org/news/d3-visualizations-with-datasets-how-to-build-a-gantt-like-chart-9c9afa9b8d9d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t1WrOVTnZKGrY2oVjjoUfA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer un graphique de type Gantt en utilisant D3 pour visualiser
  un ensemble de données
seo_desc: 'By Déborah Mesquita

  When you finish learning about the basics of D3.js, usually the next step is to
  build visualizations with your dataset. Because of how D3 works, the way we organize
  the dataset can make our lives really easy or really hard.

  In thi...'
---

Par Débora Mesquita

Lorsque vous avez terminé d'apprendre les bases de D3.js, généralement l'étape suivante consiste à créer des visualisations avec votre ensemble de données. En raison du fonctionnement de D3, la manière dont nous organisons l'ensemble de données peut rendre notre vie vraiment facile ou vraiment difficile.

Dans cet article, nous allons discuter des différents aspects de ce processus de construction. Pour illustrer ces aspects, nous allons créer une visualisation similaire à un graphique de Gantt.

La leçon la plus importante que j'ai apprise est que **vous devez créer un ensemble de données où chaque point de données correspond à une unité de données de votre graphique**. Plongeons dans notre étude de cas pour voir comment cela fonctionne.

Le but est de créer un graphique de type Gantt similaire à celui ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DmEXz6uHizu2o02SibCRKg.png)
_La visualisation que nous voulons créer_

Comme vous pouvez le voir, ce n'est pas un graphique de Gantt car les tâches commencent et se terminent le même jour.

### Création de l'ensemble de données

J'ai extrait les données des procès-verbaux. Pour chaque fichier texte, j'ai reçu des informations sur les projets et leurs statuts des réunions. Au début, j'ai structuré mes données comme ceci :

```
{    "meetings": [{            "label": "1ère Réunion",            "date": "09/03/2017",            "projects_presented": [],            "projects_approved": ["002/2017"],            "projects_voting_round_1": ["005/2017"],            "projects_voting_round_2": ["003/2017", "004/2017"]        },        {            "label": "2ème Réunion",            "date_start": "10/03/2017",            "projects_presented": ["006/2017"],            "projects_approved": ["003/2017", "004/2017"],            "projects_voting_round_1": [],            "projects_voting_round_2": ["005/2017"]        }    ]}
```

Examinons de plus près les données.

Chaque projet a 4 statuts : `presented`, `voting round 1`, `voting round 2` et `approved`. Lors de chaque réunion, le statut des projets peut ou non changer. J'ai structuré les données en les regroupant par réunions. Ce regroupement nous a posé beaucoup de problèmes lors de la création de la visualisation. Cela était dû au fait que nous devions passer des données aux nœuds avec D3. Après avoir vu le graphique de Gantt que Jess Peter a construit [ici](https://codepen.io/jey/full/jmClJ/), j'ai réalisé que je devais changer mes données.

Quelle était l'information minimale que je voulais afficher ? Quel était le nœud minimal ? En regardant l'image, c'est l'information du projet. J'ai donc changé la structure des données comme suit :

```
{  "projects": [                  {                    "meeting": "1ère Réunion",                    "type": "project",                    "date": "09/03/2017",                    "label": "Projet 002/2017",                    "status": "approved"                  },                  {                    "meeting": "1ère Réunion",                    "type": "project",                    "date": "09/03/2017",                    "label": "Projet 005/2017",                    "status": "voting_round_1"                  },                  {                    "meeting": "1ère Réunion",                    "type": "project",                    "date": "09/03/2017",                    "label": "Projet 003/2017",                    "status": "voting_round_2"                  },                  {                    "meeting": "1ère Réunion",                    "type": "project",                    "date": "09/03/2017",                    "label": "Projet 004/2017",                    "status": "voting_round_2"                  }               ]}
```

Et tout a mieux fonctionné après cela. C'est drôle de voir comment la frustration a disparu après ce simple changement.

### Création de la visualisation

Maintenant que nous avons l'ensemble de données, commençons à créer la visualisation.

#### Création de l'axe des x

Chaque date doit être affichée sur l'axe des x. Pour cela, définissez `d3.timeScale()` :

```
var timeScale = d3.scaleTime()                .domain(d3.extent(dataset, d => dateFormat(d.date)))                .range([0, 500]);
```

Les valeurs minimale et maximale sont données dans le tableau `d3.extent()`.

Maintenant que vous avez `timeScale`, vous pouvez appeler l'axe.

```
var xAxis = d3.axisBottom()                .scale(timeScale)                .ticks(d3.timeMonth)                .tickSize(250, 0, 0)                .tickSizeOuter(0);
```

Les ticks doivent faire 250px de long. Vous ne voulez pas le tick extérieur. Le code pour afficher l'axe est :

```
d3.json("projects.json", function(error, data) {            chart(data.projects);});
```

```
function chart(data) {    var dateFormat = d3.timeParse("%d/%m/%Y");
```

```
    var timeScale = d3.scaleTime()                   .domain(d3.extent(data, d => dateFormat(d.date)))                   .range([0, 500]);
```

```
    var xAxis = d3.axisBottom()                  .scale(timeScale)                  .tickSize(250, 0, 0)                  .tickSizeOuter(0);
```

```
    var grid = d3.select("svg").append('g').call(xAxis);}
```

Si vous tracez cela, vous pouvez voir qu'il y a beaucoup de ticks. En fait, il y a des ticks pour chaque jour du mois. Nous voulons afficher uniquement les jours où il y a eu des réunions. Pour cela, nous allons définir explicitement les valeurs des ticks :

```
let dataByDates = d3.nest().key(d => d.date).entries(data);let tickValues = dataByDates.map(d => dateFormat(d.key));
```

```
var xAxis = d3.axisBottom()                .scale(timeScale)                .tickValues(tickValues)                .tickSize(250, 0, 0)                .tickSizeOuter(0);
```

En utilisant `d3.nest()`, vous pouvez regrouper tous les projets par date (voir à quel point il est pratique de structurer les données par projets ?), puis obtenir toutes les dates et les passer à l'axe.

#### Placement des projets

Nous devons placer les projets le long de l'axe des y, alors définissons une nouvelle échelle :

```
yScale = d3.scaleLinear().domain([0, data.length]).range([0, 250]);
```

Le domaine est le nombre de projets. La plage est la taille de chaque tick. Maintenant, nous pouvons placer les rectangles :

```
var projects = d3.select("svg")                   .append('g')                   .selectAll("this_is_empty")                   .data(data)                   .enter();
```

```
var innerRects = projects.append("rect")              .attr("rx", 3)              .attr("ry", 3)              .attr("x", (d,i) => timeScale(dateFormat(d.date)))              .attr("y", (d,i) => yScale(i))              .attr("width", 200)              .attr("height", 30)              .attr("stroke", "none")              .attr("fill", "lightblue");
```

`selectAll()`, `data()`, `enter()` et `append()` sont toujours un peu délicats. Pour utiliser la méthode `enter()` (afin de créer un nouveau nœud à partir d'un point de données), nous avons besoin d'une sélection. C'est pourquoi nous avons besoin de `selectAll("this_is_empty")`, même si nous n'avons pas encore de `rect`. J'ai utilisé ce nom pour clarifier que nous avons seulement besoin de la sélection vide. En d'autres termes, nous utilisons `selectAll("this_is_empty")` pour obtenir une sélection vide sur laquelle nous pouvons travailler.

La variable `projects` contient des sélections vides liées aux données, donc nous pouvons l'utiliser pour dessiner les projets dans `innerRects`.

Maintenant, vous pouvez également ajouter une étiquette pour chaque projet :

```
var rectText = projects.append("text")                .text(d => d.label)                .attr("x", d => timeScale(dateFormat(d.date)) + 100)                .attr("y", (d,i) => yScale(i) + 20)                .attr("font-size", 11)                .attr("text-anchor", "middle")                .attr("text-height", 30)                .attr("fill", "#fff");
```

#### Colorier chaque projet

Nous voulons que la couleur de chaque rectangle reflète le statut de chaque projet. Pour cela, créons une autre échelle :

```
let dataByCategories = d3.nest().key(d => d.status).entries(data);let categories = dataByCategories.map(d => d.key).sort();
```

```
let colorScale = d3.scaleLinear()             .domain([0, categories.length])             .range(["#00B9FA", "#F95002"])             .interpolate(d3.interpolateHcl);
```

Et ensuite, nous pouvons remplir les rectangles avec des couleurs de cette échelle. En mettant ensemble tout ce que nous avons vu jusqu'à présent, voici le code :

```
d3.json("projects.json", function(error, data) {            chart(data.projetos);        });
```

```
function chart(data) {    var dateFormat = d3.timeParse("%d/%m/%Y");    var timeScale = d3.scaleTime()                   .domain(d3.extent(data, d => dateFormat(d.date)))                   .range([0, 500]);      let dataByDates = d3.nest().key(d => d.date).entries(data);    let tickValues = dataByDates.map(d => dateFormat(d.key));      let dataByCategories = d3.nest().key(d => d.status).entries(data);    let categories = dataByCategories.map(d => d.key).sort();    let colorScale = d3.scaleLinear()                 .domain([0, categories.length])                 .range(["#00B9FA", "#F95002"])                 .interpolate(d3.interpolateHcl);      var xAxis = d3.axisBottom()                .scale(timeScale)                .tickValues(tickValues)                .tickSize(250, 0, 0)                .tickSizeOuter(0);    var grid = d3.select("svg").append('g').call(xAxis);      yScale = d3.scaleLinear().domain([0, data.length]).range([0, 250]);      var projects = d3.select("svg")                   .append('g')                   .selectAll("this_is_empty")                   .data(data)                   .enter();      var barWidth = 200;      var innerRects = projects.append("rect")                  .attr("rx", 3)                  .attr("ry", 3)                  .attr("x", (d,i) => timeScale(dateFormat(d.date)) - barWidth/2)                  .attr("y", (d,i) => yScale(i))                  .attr("width", barWidth)                  .attr("height", 30)                  .attr("stroke", "none")                  .attr("fill", d => d3.rgb(colorScale(categories.indexOf(d.status))));      var rectText = projects.append("text")                  .text(d => d.label)                  .attr("x", d => timeScale(dateFormat(d.date)))                  .attr("y", (d,i) => yScale(i) + 20)                  .attr("font-size", 11)                  .attr("text-anchor", "middle")                  .attr("text-height", 30)                  .attr("fill", "#fff"); }
```

Et avec cela, nous avons la structure brute de notre visualisation.

Bien joué.

### Création d'un graphique réutilisable

Le résultat montre qu'il n'y a pas de marges. De plus, si nous voulons afficher ce graphique sur une autre page, nous devons copier tout le code. Pour résoudre ces problèmes, créons un graphique réutilisable et importons-le simplement. Pour en savoir plus sur les graphiques, cliquez [ici](https://bost.ocks.org/mike/chart/). Pour voir un tutoriel précédent que j'ai écrit sur les graphiques réutilisables, cliquez [ici](https://medium.freecodecamp.org/a-gentle-introduction-to-d3-how-to-build-a-reusable-bubble-chart-9106dc4f6c46).

La structure pour créer un graphique réutilisable est toujours la même. J'ai créé un outil pour en générer un. Dans ce graphique, je veux définir :

* Les données (bien sûr)
* Les valeurs pour la largeur, la hauteur et les marges
* Une échelle de temps pour la valeur x des rectangles
* Une échelle pour la valeur y des rectangles
* Une échelle pour la couleur
* Les valeurs pour `xScale`, `yScale` et `colorScale`
* Les valeurs pour le début et la fin de chaque tâche et la hauteur de chaque barre

Je passe ensuite cela à la fonction que j'ai créée :

```
chart: ganttAlikeChartwidth: 800height: 600margin: {top: 20, right: 100, bottom: 20, left:100}xScale: d3.scaleTime()yScale: d3.scaleLinear()colorScale: d3.scaleLinear()xValue: d => d.datecolorValue: d => d.statusbarHeight: 30barWidth: 100dateFormat: d3.timeParse("%d/%m/%Y")
```

Ce qui me donne ceci :

```
function  ganttAlikeChart(){width = 800;height = 600;margin = {top: 20, right: 100, bottom: 20, left:100};xScale = d3.scaleTime();yScale = d3.scaleLinear();colorScale = d3.scaleLinear();xValue = d => d.date;colorValue = d => d.status;barHeight = 30;barWidth = 100;dateFormat = d3.timeParse("%d/%m/%Y");function chart(selection) { selection.each(function(data) {   var svg = d3.select(this).selectAll("svg").data([data]).enter().append("svg");   svg.attr("width", width + margin.left + margin.right).attr("height", height + margin.top + margin.bottom);  var gEnter = svg.append("g");  var mainGroup = svg.select("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");})}
```

```
[...]
```

```
return chart;}
```

Maintenant, nous devons simplement remplir ce modèle avec le code que nous avons créé précédemment. J'ai également apporté quelques modifications au CSS et ajouté une infobulle.

Et c'est tout.

Vous pouvez consulter l'intégralité du code [ici](https://github.com/dmesquita/d3_gantt_alike_chart).

Merci d'avoir lu ! 😊

Avez-vous trouvé cet article utile ? Je fais de mon mieux pour écrire un article approfondi chaque mois, vous pouvez [recevoir un email lorsque j'en publie un nouveau](https://goo.gl/forms/SLrJDrGtxgAoILkt1).