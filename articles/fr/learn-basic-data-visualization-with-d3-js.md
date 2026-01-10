---
title: Apprendre les bases de la visualisation de données avec D3.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T01:37:00.000Z'
originalURL: https://freecodecamp.org/news/learn-basic-data-visualization-with-d3-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb8740569d1a4ca33cc.jpg
tags:
- name: D3
  slug: d3
- name: data visualization
  slug: data-visualization
- name: toothbrush
  slug: toothbrush
seo_title: Apprendre les bases de la visualisation de données avec D3.js
seo_desc: 'Our goal is to learn the basics of data

  You''ll learn the basics of data visualization using D3 through this project.


  What is D3.js?

  For those who are not familiar with D3, D3.js is a JavaScript library for manipulating
  documents based on data. D3 he...'
---

## **Notre objectif est d'apprendre les bases des données**

Vous apprendrez les bases de la visualisation de données en utilisant D3 à travers ce projet.

![screen shot 2016-05-17 at 5 02 41 pm](https://discourse-user-assets.s3.amazonaws.com/original/2X/2/2d46c5c1c76bd03b9e85d450da02695d3f07c75c.png)

## **Qu'est-ce que D3.js ?**

Pour ceux qui ne sont pas familiers avec D3, D3.js est une bibliothèque JavaScript pour manipuler des documents basés sur des données. D3 vous aide à donner vie aux données en utilisant HTML, SVG et CSS.

D3.js vous aide à attacher vos données aux éléments du DOM (Document Object Model). Ensuite, vous pouvez utiliser CSS3, HTML et/ou SVG pour présenter ces données. Enfin, vous pouvez rendre les données interactives grâce aux transformations et transitions pilotées par les données de D3.js.

## **Explication du projet :**

### **Scénario :**

Il y a une classe d'étudiants en ligne interagissant avec différents sujets et passant des quiz sur ces sujets.

Il y a 15 sujets et pour chaque sujet, nous avons un nombre d'étudiants qui ont passé le quiz et ont obtenu des scores dans trois catégories : Faible, Moyen et Élevé.

### **Par exemple (Données fournies) :**

Sujet : "1", faible : 4, moyen :13, élevé : 18

Sujet : "2", faible : 11, moyen :12, élevé : 6

Sujet : "3", faible : 12, moyen :24, élevé : 6 et ainsi de suite.

Notez que le Sujet 1 a `4 + 13 + 8 = 35` étudiants ayant passé le quiz et le Sujet 2 a `11+12+6 = 29` étudiants et le sujet 3 a 42 étudiants et ainsi de suite.

Nous voulons créer des graphiques à barres et des camemberts interactifs. Par exemple, un survol de souris sur l'une des barres modifiera le camembert en conséquence et vice-versa.

Avec une combinaison interactive de graphique à barres et de camembert, où le graphique à barres montre le nombre d'étudiants ayant interagi avec un sujet particulier (passé le quiz) et le camembert montrant la classification de la performance de ces étudiants en catégories de "faible, moyen, élevé", nous pouvons visualiser nos données et obtenir plus d'analyses à partir de celles-ci.

## **Conseils et Ressources :**

### **Instructions étape par étape :**

[**Introduction à D3 :**](https://d3js.org/) où vous pouvez apprendre les Sélections, les propriétés dynamiques et les transitions dans D3.js.

Dans la fonction JavaScript principale, écrivez une fonction pour gérer l'histogramme (graphique à barres) - L'histogramme montrera le nombre total d'étudiants ayant passé le quiz (interagi avec ce sujet) pour 15 sujets.

* (Voici le [**Tutoriel**](https://bost.ocks.org/mike/bar/) où vous pouvez apprendre à créer un graphique à barres en utilisant la bibliothèque JavaScript D3. Le premier tutoriel enseigne comment créer une version basique en HTML, puis un graphique plus complet en graphiques vectoriels scalables (SVG), et enfin des transitions animées entre les vues.)
* [Créer un SVG pour l'histogramme](http://codepen.io/SundeepB/pen/CxveH)
* Créer une fonction pour le mappage de l'axe x et ajouter l'axe x au SVG de l'histogramme
* Créer une fonction pour le mappage de l'axe y et créer des barres pour l'histogramme contenant des rectangles et des étiquettes de sujet.
* Créer les rectangles et les étiquettes de sujet
* Créer une fonction pour mettre à jour les barres. Cela sera utilisé par le camembert

Écrivez une fonction pour gérer le camembert. Le camembert aura trois parts : Faible, Moyen et Élevé pour représenter les scores.

* [**Tutoriel**](http://zeroviscosity.com/d3-js-step-by-step/step-1-a-basic-pie-chart) où vous pouvez apprendre à créer un camembert, puis des transitions entre les vues et comment créer une légende.
* Créer un SVG pour le camembert.
* Créer une fonction pour dessiner les arcs des parts du camembert - les parts du camembert seront Faible, Moyen et Élevé
* Créer une fonction pour calculer les angles des parts du camembert.
* Dessiner les parts du camembert.
* Créer une fonction pour mettre à jour le camembert. Cela sera utilisé par l'histogramme.
* Calculer la fréquence totale par segment pour tous les sujets.
* Calculer la fréquence totale par état pour tous les segments.

## **Résultat de l'analyse des données et ce que nous pouvons déduire de la visualisation :**

* Le camembert initial montre la classification agrégée de tous les scores des étudiants sur tous les sujets combinés en trois catégories "faible, moyen, élevé"
* Le graphique à barres initial montre le nombre d'étudiants ayant interagi sur ce sujet particulier
* Toute catégorie sélectionnée dans le camembert mettra à jour le graphique à barres, montrant le nombre d'étudiants ayant interagi sur divers sujets ayant des scores appartenant à cette catégorie particulière.
* Les captures d'écran ci-dessous montrent le survol de la souris sur la part "Moyen" et la part "Élevé" du camembert respectivement et pour cette part particulière, les graphiques à barres par sujet et le nombre d'étudiants.

![screen shot 2016-05-17 at 5 13 53 pm](https://discourse-user-assets.s3.amazonaws.com/original/2X/1/106f06d412df6db5b4a421dc4769d22695cbec72.png)

![screen shot 2016-05-17 at 5 14 05 pm](https://discourse-user-assets.s3.amazonaws.com/original/2X/7/7b23ebe89f74f11090984dbc4dc68212e3beceb3.png)

* Toute barre sélectionnée dans le graphique à barres mettra à jour le camembert montrant la classification de tous les scores des étudiants sur ce sujet particulier en trois catégories Faible, Moyen et Élevé. La capture d'écran ci-dessous montre le survol de la souris sur le Sujet 2 et pour ce sujet particulier, combien d'étudiants sont dans les catégories Faible, Moyen et Élevé

![screen shot 2016-05-17 at 5 13 26 pm](https://discourse-user-assets.s3.amazonaws.com/original/2X/7/7bd7c613bdb882f2b7c1f76f9778a1bda3e886dd.png)