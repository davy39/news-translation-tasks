---
title: Comment j'ai analysé les tendances des développeurs avec un tableau croisé
  dynamique JavaScript et une bibliothèque de graphiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T16:20:53.000Z'
originalURL: https://freecodecamp.org/news/analysis-of-developers-trends-with-javascript-pivot-table-and-charting-library-b7b6e16ab71b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MUpijMKC5wC_Ged6o_ZJPA.png
tags:
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment j'ai analysé les tendances des développeurs avec un tableau croisé
  dynamique JavaScript et une bibliothèque de graphiques
seo_desc: 'By Veronika Rovnik

  Hi, dev community!

  Today I’d like to share my experience of analyzing developers’ preferences based
  on StackOverflow’s Developer Survey Results. Of course, there are plenty of ready
  analytical reports but it’s always much more exci...'
---

Par Veronika Rovnik

Bonjour, communauté des développeurs !

Aujourd'hui, je voudrais partager mon expérience d'analyse des préférences des développeurs basée sur les [Résultats de l'Enquête des Développeurs de StackOverflow](https://insights.stackoverflow.com/survey/?r=fr3). Bien sûr, il existe de nombreux **rapports analytiques** prêts à l'emploi, mais il est toujours beaucoup plus excitant de créer un projet personnel à partir de zéro et d'améliorer nos compétences en analyse de données. Et c'est exactement ce que je vais faire. :)

### **Défis**

Dès le début, j'ai été confrontée au défi de trouver un outil capable de traiter 100 000 enregistrements textuels. Comme il s'agit d'un ensemble de données énorme, l'outil doit être puissant et utiliser le moins possible de mémoire du navigateur. Il doit également être simple à utiliser. Heureusement, j'ai trouvé un composant de **tableau croisé dynamique web**. Il semblait prometteur à première vue et m'a aidée à accomplir toutes mes intentions liées à la création de rapports.

Au-delà de ses capacités de reporting, j'ai remarqué qu'il supportait l'intégration avec des bibliothèques de graphiques. J'ai choisi **FusionCharts**. Il s'intègre également avec différents frameworks JavaScript et fournit des graphiques sophistiqués. En utilisant une combinaison de tableau croisé dynamique et de graphique, j'ai réussi à créer un petit projet personnel sur l'analyse et la visualisation de données.

### **Objectifs**

Mes objectifs analytiques comprenaient la _création d'un rapport_ et la _visualisation des résultats de l'enquête_. J'ai décidé de me concentrer sur les profils des développeurs, leurs statuts d'emploi, les technologies, langages, frameworks et bibliothèques les plus aimés, et de réunir ces informations pour obtenir de nouvelles perspectives.

Par exemple, il était intéressant pour moi de découvrir les antécédents des développeurs qui aiment des technologies spécifiques. Comme prochaine étape, j'aimerais analyser les relations entre le choix de différentes technologies.

Cet article sera sous la forme d'un **tutoriel étape par étape** où je vais essayer de couvrir les aspects les plus importants du travail avec ces deux outils.

Je suis ravie de partager avec vous le processus de création d'un tableau de bord interactif doté de fonctionnalités de drill-through, de glisser-déposer et de graphiques.

Commençons !

#### **Installer les bibliothèques dans votre projet**

En premier lieu, vous devez ajouter les scripts de la bibliothèque, le connecteur Flexmonster pour FusionCharts, et les conteneurs où les composants seront rendus.

```html
<script src="https://cdn.flexmonster.com/flexmonster.js"></script>
<script src="https://cdn.flexmonster.com/lib/flexmonster.fusioncharts.js"></script>
<script src="https://static.fusioncharts.com/code/latest/fusioncharts.js"></script>

<div id="pivotContainer"></div>
<div id="fusionchartContainer"></div>
```

Si vous souhaitez créer plusieurs graphiques, ajoutez plus de conteneurs pour eux.

#### **Intégrer un tableau croisé dynamique**

Ajoutez un outil de reporting à votre projet et configurez ses paramètres de base :

```js
var pivot = new Flexmonster({
    container: "pivotContainer",
    toolbar: true
});
```

Pour découvrir comment étendre les possibilités du tableau croisé dynamique avec diverses propriétés, vous pouvez consulter l'article sur [l'appel d'API init](https://www.flexmonster.com/api/new-flexmonster/?r=fr3).

#### **Préparer et importer les données**

En tant que jeu de données, j'ai choisi les Résultats de l'Enquête des Développeurs. Il contient 195 Mo de données textuelles brutes.

Une façon de charger les données dans un tableau croisé dynamique est de définir la fonction qui retourne les données JSON. Mais comme je ne peux pas montrer toutes les données dans une démonstration CodePen en raison de ses limitations sur la taille du code. Pour ne pas encombrer mon code, j'ai chargé un fichier sur CDN et défini un chemin vers ma source de données :

```js
dataSource: {
    filename: "surveyresults.csv"
}
```

#### **Définir une tranche**

Organisez les hiérarchies sur la grille — placez-les dans les lignes, colonnes et mesures. Vous pouvez également ajouter des filtres de rapport pour garder votre grille propre et trier les données pour voir les enregistrements les plus pertinents en premier.

```js
"slice": {
    "reportFilters": [{
            "uniqueName": "Country"
        },
        {
            "uniqueName": "Gender"
        }
    ],
    "rows": [{
        "uniqueName": "DevType"
    }],
    "columns": [{
        "uniqueName": "[Measures]"
    }],
    "measures": [{
        "uniqueName": "Salary",
        "aggregation": "average"
    }],
    "sorting": {
        "column": {
            "type": "desc",
            "tuple": [],
            "measure": {
                "uniqueName": "Salary",
                "aggregation": "average"
            }
        }
    }
}
```

Plus tard, vous pouvez changer la tranche en temps réel avec la fonctionnalité de **glisser-déposer** — dès que vous avez besoin de regarder d'un point de vue différent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5-QioWPFn5sIdjmZpZol2Q.gif)

#### **Lier les graphiques et le tableau croisé dynamique ensemble**

Faisons en sorte que les graphiques affichent les données du tableau croisé dynamique. Pour cela, attachez un gestionnaire d'événements à l'événement `reportcomplete` de Flexmonster. Il est déclenché dès que le tableau croisé dynamique est prêt à agir en tant que fournisseur de données.

Le code ressemble à ceci :

```js
reportcomplete: function() {
    pivot.off("reportcomplete");
    createFusionChart();
}
```

Maintenant, passons à la partie du code qui rendra le tableau de bord interactif.

Définissez une fonction qui est responsable de la récupération des données du rapport, de la création et du dessin du graphique.

Dans **createFusionChart()**, invoquez la méthode **getData()** sur l'instance du tableau croisé dynamique pour obtenir les données du rapport actuel ou de la tranche dont vous avez besoin. Cette méthode les pré-traite pour le type de graphique donné et transmet les données à _callbackHandler_ et _updateHandler_. Ces gestionnaires spécifient ce qui se passe une fois que le rapport est affiché pour la première fois ou lorsque les données sont mises à jour (filtrées, triées, etc.). Dans _callbackHandler_, vous devez instancier un graphique et lui envoyer les données. Dans _updateHandler_, il suffit de définir les données mises à jour pour le graphique et de le rendre à nouveau.

Hourra ! Le graphique et le tableau croisé dynamique sont rendus sur la même page. Maintenant, le graphique montre les données de la grille et réagit à tout changement appliqué au rapport.

De la même manière, vous pouvez ajouter autant de graphiques que vous le souhaitez.

Pour cette visualisation de données, j'ai choisi une carte, des graphiques en barres et en colonnes.

#### **Ce que j'ai obtenu**

Après avoir suivi toutes ces étapes, j'ai obtenu un **tableau de bord totalement interactif** basé sur l'outil de reporting et les graphiques. Permettez-moi de partager avec vous quelques-unes des perspectives que j'ai tirées des données des résultats de l'enquête.

#### **Démographie**

![Image](https://cdn-media-1.freecodecamp.org/images/0*IcGLQst9QbPAIRtd)

Il est facile de voir sur le graphique que la plupart des développeurs qui ont répondu à l'enquête vivent aux États-Unis, en Inde et au Canada.

#### **Occupation**

Plus de 18 000 répondants sont des étudiants à temps plein :

![Image](https://cdn-media-1.freecodecamp.org/images/0*0OEIgVLDia7pAOo4)

De plus, environ 80 000 développeurs disent qu'ils codent en dehors du travail pendant leur temps libre :

![Image](https://cdn-media-1.freecodecamp.org/images/0*rlZmbr8C_h7Jiag7)

Il était intéressant de découvrir les types de développeurs les plus courants. Ce sont les développeurs back-end, full-stack et mobile :

![Image](https://cdn-media-1.freecodecamp.org/images/0*94lFxI9r8OAPmxK-)

#### **Éducation**

La plupart des répondants ont au moins une licence :

![Image](https://cdn-media-1.freecodecamp.org/images/0*QPOREOP7Y8MTS_6F)

Plus de 50,34K développeurs ont étudié l'informatique, l'ingénierie informatique et logicielle :

![Image](https://cdn-media-1.freecodecamp.org/images/0*0MLo5qKwXojD44l-)

Plus de 23K développeurs ont appris à coder au cours des cinq dernières années :

![Image](https://cdn-media-1.freecodecamp.org/images/0*KgysPedq40UT5wn4)

#### **Frameworks, bibliothèques et outils**

Passons aux frameworks, bibliothèques et outils les plus désirés avec lesquels les développeurs veulent travailler l'année prochaine :

![Image](https://cdn-media-1.freecodecamp.org/images/0*yCzb2wEg5G2h1kN0)

Comme vous pouvez le voir, .NET Core, Node.js, React et TensorFlow ont obtenu le plus de votes.

### **Mettre tout cela ensemble**

En utilisant les API et les guides conviviaux pour les développeurs du tableau croisé dynamique et d'une bibliothèque de graphiques, j'ai réussi à obtenir une vue d'ensemble des tendances dans la communauté des développeurs. Je vous encourage à plonger plus profondément dans les données et à partager des perspectives uniques avec vos amis et coéquipiers.

J'espère que ce tutoriel vous inspirera à créer votre propre projet de visualisation.

Merci d'avoir lu !

**Liens utiles**

* [Démonstration live CodePen](https://codepen.io/ronika/pen/mooKab/?r=fr3)
* [Comment intégrer Flexmonster avec FusionCharts](https://www.flexmonster.com/doc/integration-with-fusioncharts/?r=fr3)
* [FusionCharts : galerie de graphiques](https://www.fusioncharts.com/charts?product=fusioncharts/?r=fr3)