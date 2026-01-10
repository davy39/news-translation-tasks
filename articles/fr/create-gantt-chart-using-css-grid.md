---
title: Comment créer un diagramme de Gantt simple en utilisant CSS Grid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-04T16:32:18.000Z'
originalURL: https://freecodecamp.org/news/create-gantt-chart-using-css-grid
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ccd740569d1a4ca344b.jpg
tags:
- name: charts
  slug: charts
- name: data visualization
  slug: data-visualization
seo_title: Comment créer un diagramme de Gantt simple en utilisant CSS Grid
seo_desc: "By Alfrick Opidi\nA Gantt chart is a handy type of bar chart that is used\
  \ in project management for showcasing a schedule of tasks. This chart visualizes\
  \ project activities as cascading horizontal bars, with width depicting the project’s\
  \ duration. \nAs..."
---

Par Alfrick Opidi

Un diagramme de Gantt est un type pratique de graphique à barres utilisé en gestion de projet pour présenter un calendrier de tâches. Ce graphique visualise les activités du projet sous forme de barres horizontales en cascade, dont la largeur représente la durée du projet. 

En tant que designer ou développeur web front-end, vous pouvez utiliser des diagrammes de Gantt pour gérer des projets et améliorer la productivité au sein de votre équipe.

Dans cet article, je vais vous montrer comment créer un diagramme de Gantt simple en utilisant le système de mise en page CSS Grid—aucune bibliothèque externe ou autre superflu, juste du CSS pur.

Vous pouvez vous référer à [ce tutoriel](https://www.freecodecamp.org/learn/responsive-web-design/css-grid/) pour comprendre comment utiliser le système de mise en page pour appliquer des règles CSS.

Le diagramme montrera un processus typique de cycle de vie de développement logiciel, de janvier à décembre. 

Voici une capture d'écran de l'apparence du diagramme de Gantt à la fin de ce tutoriel :

![Image](https://paper-attachments.dropbox.com/s_71DD472E9787F22210482D610A0DD84B11827762D701C2FF3CA4E87715003165_1567325886724_gantt-chart.png)

Commençons !

## Étape 1 : Créer un div conteneur

Commençons par créer un élément **div** conteneur pour le diagramme de Gantt :

```css
<div class="container">

</div>
```

Ajoutons un peu de style CSS :

```css
.container {  
	max-width: 1200px; 
	min-width: 650px;  
	margin: 0 auto; 
	padding: 50px;
}
```

## Étape 2 : Créer un div pour le diagramme

Créons un div à l'intérieur du conteneur principal et nommons-le chart. C'est ici que toutes les actions restantes vont se dérouler.

```css
<div class="chart">

</div>
```

Ajoutons un peu de style CSS :

```css
.chart { 
	display: grid;  
	border: 2px solid #000;  
	position: relative;  
	overflow: hidden; 
} 
```

Remarquez que j'ai défini la propriété **display** de la classe sur **grid**. Par conséquent, tous ses enfants directs deviendront automatiquement des _éléments de grille_.

## Étape 3 : Créer les lignes du diagramme

Commençons par créer la première ligne, qui sera l'en-tête du diagramme de Gantt.

```css
<div class="chart-row chart-period">
<div class="chart-row-item">
    </div><span>Janvier</span><span>Février</span><span>Mars</span>
    <span>Avril</span><span>Mai</span><span>Juin</span><span>Juillet</span>
    <span>Août</span><span>Septembre</span><span>Octobre</span>
    <span>Novembre</span><span>Décembre</span>
</div>
```

Remarquez que j'ai fourni 12 éléments **span** qui vont traverser toute la ligne, montrant les mois de la durée du projet—de janvier à décembre.

Voici son CSS :

```css
.chart-row {  
	display: grid; 
	grid-template-columns: 50px 1fr; 
	background-color: #DCDCDC;
}
```

```css
.chart-period { 
	color:  #fff;  
	background-color:  #708090 !important;  
	border-bottom: 2px solid #000;  
	grid-template-columns: 50px repeat(12, 1fr);

}

.chart-period > span {
	text-align: center;  
	font-size: 13px;  
	align-self: center;  
	font-weight: bold;  
	padding: 15px 0;   
}
```

Remarquez que j'ai utilisé la propriété **grid-template-columns** pour spécifier la largeur et le nombre de colonnes dans la mise en page de la grille.

Voyons à quoi cela ressemble dans un navigateur, jusqu'à présent :

![Image](https://paper-attachments.dropbox.com/s_71DD472E9787F22210482D610A0DD84B11827762D701C2FF3CA4E87715003165_1567023822884_gantt1.png)

Ensuite, ajoutons des lignes qui vont parcourir tout le diagramme dans un style de type boîte, ce qui aide à montrer la durée de chaque projet. 

J'ai également utilisé 12 éléments **span** pour créer les lignes.

```css
<div class="chart-row chart-lines"> 
    <span></span><span></span><span></span>
    <span></span><span></span><span></span>
    <span></span><span></span><span></span>
    <span></span><span></span>	<span></span>    
</div>
```

Voici son CSS :

```css
.chart-lines { 
	position: absolute;  
	height: 100%;  
	width: 100%;  
	background-color: transparent;  
	grid-template-columns: 50px repeat(12, 1fr);}

.chart-lines > span {  
	display: block;  border-right: 1px solid rgba(0, 0, 0, 0.3);
}
```

Voyons le résultat dans un navigateur :

![Image](https://paper-attachments.dropbox.com/s_71DD472E9787F22210482D610A0DD84B11827762D701C2FF3CA4E87715003165_1567024250393_gantt2.png)

## Étape 4 : Ajouter des éléments d'entrée

Enfin, ajoutons les éléments qui illustrent un processus d'un an pour créer un logiciel.

Par exemple, voici comment j'ai ajouté le premier élément d'entrée :

```css
<div class="chart-row">  
	<div class="chart-row-item">1</div> 
	<ul class="chart-row-bars">    
		<li class="chart-li-one">Planification</li>
	</ul>
</div>
```

Permettez-moi de décrire ce qui se passe dans le code ci-dessus :

* Tout d'abord, l'élément **div** englobant a une classe de **chart-row**, que j'ai illustrée précédemment.
* Le **div** avec une classe de **chart-row-item** est utilisé pour numérotter les éléments d'entrée sur le diagramme de Gantt. Voici son CSS :

```css
.chart-row-item { 
	background-color: #808080;  
	border: 1px solid #000;  
	border-top: 0;  border-left: 0;  
	padding: 20px 0;  font-size: 15px;  
	font-weight: bold;  
	text-align: center;
}
```

* Pour montrer les tâches sur le diagramme de Gantt, j'ai créé une liste non ordonnée et l'ai stylisée pour afficher une barre horizontale, dont la longueur montre la durée de la tâche. 

Voici le style CSS pour la classe **chart-row-bars** :

```css
.chart-row-bars { 
	list-style: none; 
	display: grid;  padding: 15px 0;  
	margin: 0;  
	grid-template-columns: repeat(12, 1fr); 
	grid-gap: 10px 0;  
	border-bottom: 1px solid #000;
}
```

* L'élément d'entrée est défini dans la balise **li**. Voici son style CSS :

```css
li {  
    font-weight: 450;  
    text-align: left;  
    font-size: 15px;  min-height: 15px;  
    background-color: #708090;  
    padding: 5px 15px;  color: #fff;  
    overflow: hidden;  
    position: relative;  
    cursor: pointer;  
    border-radius: 15px;
 } 
 
 ul .chart-li-one { 
 	grid-column: 1/2;  
        background-color: #588BAE;
 }
```

Remarquez que j'ai utilisé la propriété **grid-column** pour spécifier la durée du projet. 

Par exemple, une propriété de **grid-column: 3/9;** comme l'entrée "Développement", étend une tâche sur la grille de mars à août.

Voici à quoi ressemble le premier élément d'entrée dans un navigateur :

![Image](https://paper-attachments.dropbox.com/s_71DD472E9787F22210482D610A0DD84B11827762D701C2FF3CA4E87715003165_1567024868326_gantt3.png)

J'ai ajouté les autres entrées sur le diagramme en suivant le même processus que pour la première entrée. Finalement, cela a abouti à un diagramme de Gantt bien présenté, comme l'image que j'ai montrée précédemment. 

## Conclusion

C'est tout ! Vous pouvez consulter l'intégralité du code de ce tutoriel sur CodePen :  


%[https://codepen.io/jasoya/pen/GRKWXvr]

Comme vous l'avez vu, créer un diagramme de Gantt en utilisant CSS Grid n'est pas compliqué. Avec ce type de diagramme, vous pouvez gérer vos projets de développement web de manière efficace et vous assurer que tout le monde est sur la bonne voie pour atteindre les objectifs stipulés.

De plus, les diagrammes de Gantt peuvent également être utilisés dans d'autres industries pour gérer des projets. Par exemple, si vous vendez des [toilettes à compost](https://www.waterless-toilet.com/top-6-best-composting-toilets-to-choose/), vous pouvez utiliser des diagrammes de Gantt pour montrer le nombre de ventes réalisées sur une période de temps. 

Bien sûr, je n'ai fait qu'effleurer la surface des choses que vous pouvez réaliser avec les diagrammes de Gantt. 

Il existe plusieurs autres ajustements que vous pouvez apporter aux diagrammes de Gantt pour répondre à vos besoins spécifiques et aux objectifs de votre projet. Par exemple, vous pouvez les utiliser pour montrer la relation entre diverses tâches et comment l'achèvement de l'une dépend d'une autre, montrer comment les ressources peuvent être allouées pour la réussite des projets, et montrer des exigences de projet claires qui garantissent que tout le monde est sur la même longueur d'onde.

Avez-vous des questions ou des commentaires ?

N'hésitez pas à me contacter via Twitter ci-dessous et je ferai de mon mieux pour répondre.