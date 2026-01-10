---
title: Tutoriel D3.js – Visualisation de données pour débutants
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-11-24T15:03:01.000Z'
originalURL: https://freecodecamp.org/news/d3js-tutorial-data-visualization-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Group-1.png
tags:
- name: D3
  slug: d3
- name: D3.js
  slug: d3js
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
seo_title: Tutoriel D3.js – Visualisation de données pour débutants
seo_desc: 'In this article, I''m going to walk you through how to use D3.js in a step
  by step and beginner-friendly way.

  We''ll talk about what D3.js is, how it works, and we''ll create some basic visualizations
  to add transitions, interactions, and zooming.

  Table...'
---

Dans cet article, je vais vous guider à travers l'utilisation de D3.js de manière étape par étape et adaptée aux débutants.

Nous parlerons de ce qu'est D3.js, de son fonctionnement, et nous créerons quelques visualisations de base pour ajouter des transitions, des interactions et du zoom.

## Table des matières

* [Prise en main](#heading-installation) Qu'est-ce que D3.js ? Comment configurer un environnement D3.js
    
* [Sélections](#heading-comment-selectionner-les-elements-dans-d3) Comment sélectionner des éléments dans D3 Comment modifier des éléments dans D3
    
* [D3 est piloté par les données](#heading-d3-est-pilote-par-les-donnees) Jointure de données dans D3 Chargement de données dans D3
    
* [Échelles dans D3](#heading-echelles-dans-d3)
    
* [Créer un graphique à barres avec d3.js](#heading-comment-creer-un-graphique-a-barre-avec-d3js) Composant d'axe dans D3 Convention de marge D3 Comment le styliser avec CSS dans D3
    
* [Créer une carte du monde avec d3.js](#heading-comment-creer-une-carte-du-monde-avec-d3js-lune-des-choses-que-jadore-personnellement-a-propos-de-d3-est-sa-capacite-a-gerer-les-donnees-geographiques-contrairement-a-nos-exemples-precedents-qui-utilisaient-le-format-de-donnees-json-pour-les-cartes-nous-allons-maintenant-utiliser-une-forme-speciale-de-donnees-json-appelée-geojson-vous-pouvez-trouver-les-donnees-geojson-que-nous-allons-utiliser-ici-comme-dans-nos-autres-exemples-commençons-d'abord-par-selectionner-notre-element-svg-dans-le-document-et-aussi-configurer-la-convention-de-marge-const-margin-top-5-right-5-bottom-5-left-5-width-documentqueryselectorbodyclientwidth-height-500-const-svg-d3selectd3demoattrviewbox-0-0-width-height-html-ensuite-pour-generer-notre-carte-nous-avons-besoin-dune-projection-pour-rendre-les-coordonnees-spheriques-dans-notre-fichier-de-donnees-et-dun-generateur-de-chemin-pour-convertir-les-coordonnees-projetees-en-un-chemin-svg-qui-est-ensuite-rendu-a-lecran-let-projection-d3geoequirectangularcenter0-0-d3-fournit-beaucoup-de-projections-je-nai-utilise-celle-ci-que-parce-que-je-laime-maintenant-que-nous-avons-choisi-notre-projection-convertissons-la-en-un-chemin-svg-d3-gerela-conversion-pour-nous-lorsque-nous-utilisons-la-methode-d3geopath-cette-methode-prend-en-entree-une-projection-celle-que-nous-avons-definie-ci-dessus-const-pathgenerator-d3geopathprojectionprojection-nous-ne-voulons-pas-dessiner-la-carte-directement-sur-le-svg-parce-que-nous-allons-ajouter-des-animations-et-du-zoom-plus-tard-aussi-nous-ajoutons-un-element-g-au-svg-selectionne-let-g-svgappendg-ensuite-nous-chargerons-nos-donnees-pour-la-carte-d3jsonhttpsrawgithubusercontentcomiamspruceintro-d3maindatacountries-110mgeojson-thendata-gt-consolelogdata-si-ceci-nest-pas-clair-je-vous-suggere-de-relire-la-section-sur-le-chargement-des-donnees-enfin-utilisons-notre-pathgenerator-pour-generer-nos-chemins-gselectallpath-datadatafeatures-joinpath-attrd-pathgenerator-au-dessus-nous-avons-utilise-d3-data-join-pour-ajouter-un-chemin-pour-chaque-pays-puis-nous-avons-defini-lattribut-d-a-notre-pathgeneratorattrd-pathgenerator-et-au-cas-ou-ce-ne-serait-pas-clair-cest-lequivalent-decrire-attrd-d-gt-pathgeneratord-vous-pouvez-trouver-le-code-final-et-laperçu-en-direct-sur-codepen) Comment utiliser plusieurs jeux de données dans D3.js Carte avec noms de villes Gestion des événements avec D3.js Carte avec panoramique et zoom Zoom programmatique Ajout de ToolTips
    
* [Conclusion](#heading-conclusion)
    

## À qui s'adresse cet article ?

Cet article s'adresse aux développeurs qui ont déjà une connaissance de base du HTML, du CSS, du SVG et du JavaScript et qui souhaitent apprendre à visualiser des données avec D3.js.

Cet article convient à la fois aux débutants complets et à ceux qui ont déjà une certaine expérience avec D3.js.

À la fin de cet article, vous devriez comprendre comment fonctionne D3.js et comment créer des visualisations avec vos données.

## Prise en main avec D3.js

D3.js est une bibliothèque JavaScript pour créer des visualisations comme des graphiques, des cartes, et plus encore sur le web.

> **D3.js** (également connu sous le nom de **D3**, abréviation de **Data-Driven Documents**) est une bibliothèque JavaScript pour produire des visualisations de données dynamiques et interactives dans les navigateurs web. Elle utilise les standards Scalable Vector Graphics (SVG), HTML5 et Cascading Style Sheets (CSS). – Wikipédia

Contrairement à de nombreuses autres bibliothèques de visualisation de données qui fournissent des graphiques prêts à l'emploi, D3 vous offre une grande liberté créative car vous avez un contrôle total sur les visualisations que vous créez. D3 utilise également des technologies web comme HTML, CSS, SVG et JavaScript.

En plus du fait que D3 utilise ces technologies familières, il présente plusieurs autres avantages :

* D3 est extrêmement rapide,
    
* Il encourage la réutilisation du code
    
* Il supporte de grands ensembles de données et fournit un moyen facile de charger et de transformer des données
    
* Il est bon pour créer des visualisations avec des interactions riches
    

### Comment configurer un environnement D3

D3 fonctionne dans tous les navigateurs modernes, et au moment de la rédaction de cet article, D3.js est en version 7 (v7).

Pour utiliser la dernière version de D3, vous devez la lier à votre page web comme ceci :

```html
<script src="https://d3js.org/d3.v7.min.js"></script>
```

Cependant, à des fins pédagogiques, tous les exemples de cet article sont sur [Codepen](https://codepen.io), afin que vous puissiez modifier les exemples en direct.

## Comment sélectionner des éléments dans D3

Lorsque vous codez en JavaScript et que vous devez modifier des éléments sur une page, vous devez sélectionner ces éléments. D3.js fonctionne de la même manière et nous fournit deux méthodes pour sélectionner des éléments DOM :

* `d3.select()`
    
* `d3.selectAll()`
    

Ces deux méthodes de sélection prendront n'importe quel sélecteur CSS et retourneront l'élément qui correspond au sélecteur spécifié. Si aucun élément ne correspond au sélecteur, il retournera une sélection vide.

La méthode `d3.select()` sélectionnera le premier élément qui correspond dans le DOM (de haut en bas).

```javascript
d3.select("#d3_p").style("color", "blue");

<div class="d3_example">
    <cite class="d3_example-text">Exemple de sortie</cite>
<p id="d3_p"> bonjour le monde 1</p>
</div>
```

S'il y a plusieurs éléments qui correspondent au sélecteur spécifié, [`d3.select`](http://d3.select)`()` correspondra au premier qu'il trouve.

```javascript
<div class="d3_example">
    <cite class="d3_example-text">Exemple de sortie</cite>
<p id="d3_p-all"> bonjour le monde 1</p>
<p id="d3_p-all"> bonjour le monde 2</p>
<p id="d3_p-all"> bonjour le monde 3</p>
<p id="d3_p-all"> bonjour le monde 4</p>
</div>
```

La méthode `d3.selectAll()` fonctionne de manière très similaire à [`d3.select`](http://d3.select)`()` – mais au lieu de cela, elle sélectionne TOUS les éléments qui correspondent au sélecteur :

```javascript
d3.selectAll
(".d3_p").style("color", "blue");

<div class="d3_example">
    <cite class="d3_example-text">Exemple de sortie</cite>
<p class="d3_p"> bonjour le monde 1</p>
<p class="d3_p"> bonjour le monde 2</p>
<p class="d3_p"> bonjour le monde 3</p>
<p class="d3_p"> bonjour le monde 4</p>
</div>
```

### Comment modifier des éléments dans D3

Après avoir sélectionné vos éléments DOM, D3 fournit les méthodes suivantes pour les modifier :

```javascript
| Méthode   |      Utilisation      |  Exemple |  
|---|---|---|
| `.attr()` |  Met à jour l'attribut de l'élément sélectionné | `d3.select("p").attr("name", "fred")` | 
| `..classed()` | Assigne ou désassigne les noms de classe CSS spécifiés sur les éléments sélectionnés   |   `d3.select("p").classed("radio", true);` |
| `.style()`  | Met à jour la propriété de style |    `d3.select("p").style("color", "blue");` |
| `.property()` | Utilisé pour définir une propriété d'élément |    `d3.select('input').property('value', 'hello world')` |
| `.text()`  | Met à jour le contenu textuel de l'élément sélectionné |    `d3.select('h1').text('Apprendre d3.js')` |
| `.html()` | Définit le HTML interne à la valeur spécifiée sur tous les éléments sélectionnés |    `d3.select('div').html('h1>apprendre d3.js</h1>')` |
| `.append()`  | Ajoute un nouvel élément comme dernier enfant de l'élément sélectionné |    `d3.select("div").append("p")` |
| `.insert()`  | Fonctionne de la même manière que la méthode `.append()`, sauf que vous pouvez spécifier un autre élément à insérer avant |    `d3.select("div").insert("p", "h1")` |
| `.remove()`  | Supprime l'élément sélectionné du DOM  | `d3.select("div").remove("p")` | 
```

Ne vous inquiétez pas si tout cela ne vous semble pas clair tout de suite – nous utiliserons bientôt toutes ces méthodes dans nos exemples.

Chacune des méthodes de manipulation du DOM ci-dessus prend en paramètre une valeur constante ou une fonction, ce qui donne lieu à la création de **propriétés dynamiques**.

La fonction prend deux propriétés : la première est la donnée qui est conventionnellement appelée `d` dans d3.js, et l'autre est l'`index`.

```javascript
d3.selectAll("circle").attr('cx', ((d, i) => i * 100))

<div class="d3_example">
    <cite class="d3_example-text">Exemple de sortie</cite>
<svg id="d3_svg_demo1">
  <g transform="translate(50, 40)">
    <circle r="30" />
	<circle r="30" />
	<circle r="30" />
    </g>
</svg>
</div>
```

Comme vous pouvez le voir ci-dessus, au sein de cette fonction, nous pouvons appliquer n'importe quelle logique pour manipuler les données et la sortie.

## D3 est piloté par les données

D3.js lui-même est piloté par les données, ce qui signifie qu'il tire ses super pouvoirs des données. D3 supporte différents types de données comme les tableaux, CSV, XML, TSV, JSON, et ainsi de suite.

Ces données peuvent provenir d'un fichier local dans votre répertoire de travail ou peuvent être récupérées depuis une API.

### Jointures de données dans D3

La jointure de données de D3 nous permet de joindre les données spécifiées aux éléments sélectionnés. Pour créer une jointure de données, vous pouvez utiliser la méthode `.data()` :

```javascript
let fruits = ['Apple', 'Orange', 'Mango']

d3.selectAll(".d3_fruit").data(fruits).text((d) => d)
```

```xml
<p class="d3_fruit"></p>

<div class="d3_example">
    <cite class="d3_example-text">Exemple de sortie</cite>
<p class="d3_fruit"></p>
</div>
```

Voyons ce qui se passe ici et pourquoi nous n'avons obtenu qu'une seule sortie au lieu de trois.

Jusqu'à présent, nous avons :

1. 3 points de données dans notre tableau Fruits
    
2. 1 élément `p` dans notre sélection
    

D3 assigne simplement le premier fruit (Apple) de notre tableau à la seule sélection `p` qu'il a obtenue et oublie le reste.

Une solution rapide pour cela est de créer manuellement les deux autres éléments p et de continuer. Mais la plupart du temps, vous ne savez pas réellement combien d'éléments se trouvent dans votre tableau de données qui est récupéré depuis une API externe.

Pour résoudre ce problème, les dernières versions de D3 nous fournissent une méthode `.join()`. Elle ajoute, supprime et réorganise les éléments si nécessaire pour correspondre aux données spécifiées. Essayons-la avec notre exemple précédent pour voir ce qui se passe :

```javascript
let fruits = ['Apple', 'Orange', 'Mango']

d3.select(".d3_fruit")
    .selectAll("p")
    .data(fruits)
    .join("p") // la méthode join
        .attr("class", "d3_fruit")
        .text((d) => d)
```

```xml
<div class="d3_fruit"></div>

<div class="d3_example">
    <cite class="d3_example-text">Exemple de sortie</cite>
<div class="d3_fruits"></div>
</div>
```

Décortiquons un peu cela :

1. Sélectionnez l'élément wrapper `div` `d3_fruit`
    
2. Sélectionnez tous les éléments `p` même lorsqu'il n'y a pas d'éléments `p` dans la div - cela retourne une sélection vide
    
3. `.data(fruits)` - Lie le tableau de fruits à la sélection vide
    
4. `.join("p")` - Cette méthode crée tous les éléments `p` pour chaque élément de notre tableau
    
5. `.attr("class", "d3_fruit")` - Nous définissons une classe pour chaque élément `p` qui a été créé
    
6. `.text((d) => d)` - Définit le texte de chaque `p` créé en fonction du tableau de fruits
    

### Chargement de données dans D3

Nous avons vu ce que sont les données pour D3 et comment joindre des données à nos sélections. Mais jusqu'à présent, nous n'avons utilisé que nos propres données auto-créées `let fruits = ['Apple', 'Orange', 'Mango']`.

Dans un scénario réel, ce n'est généralement pas le cas – vous devez parfois récupérer des données depuis une API ou un fichier local.

D3 dispose de certaines méthodes pour charger divers types de fichiers :

* d3.json
    
* d3.csv
    
* d3.xml
    
* d3.tsv
    
* d3.text
    

Lorsque vous utilisez l'une de ces méthodes, la syntaxe est généralement la même :

```javascript
// async await
const data = await d3.csv("/path/to/file.csv");
console.log(data);

// ou
d3.json("/path/to/file.json").then((data) => {  console.log(data); })
```

Voyons cela en action en chargeant des données depuis un fichier JSON externe réel.

Pour cet exemple, j'ai un fichier JSON qui contient toutes les informations sur le Nigeria et tous ses états :

```javascript
const el = d3.select("#d3_svg_demo2");

d3.json("https://raw.githubusercontent.com/iamspruce/intro-d3/main/nigeria-states.json").then(({data}) => {
    el
     .selectAll("p")
     .data(data)
	 .join("p")
	  .text((d) => d.Name)
});



<div class="d3_example" id="d3_svg_demo2">
    <cite class="d3_example-text">Exemple de sortie</cite>
    <p></p>
    <p></p>    
    <p></p>    
    <p></p>    
    <p></p>    
    ... + 31 autres
</div>
```

En utilisant la méthode ci-dessus, vous pouvez récupérer n'importe quelle donnée dans D3.

## Échelles dans D3

Jusqu'à présent, vous avez appris comment charger et utiliser des données dans D3.js. Maintenant, nous devons apprendre les **échelles**. Cela peut être la partie la plus confuse à apprendre pour la plupart des gens et c'est aussi le concept le plus important de D3.

Dans le dernier exemple que nous venons de voir ci-dessus, nous avons chargé des données JSON depuis une API et pour chaque État du Nigeria, nous avons ajouté le nom à un élément `p`. Ce fichier JSON contient également la population de chaque État et d'autres informations.

La population de chaque État varie de la plus faible à `2 millions` à la plus élevée à `16 millions`. Pour représenter correctement ces données sur un graphique à barres, par exemple, vous devez créer un graphique à barres avec une hauteur de `16000000px`.

En imaginant cela, vous seriez probablement d'accord pour dire que ce serait un graphique à barres très long. C'est là que `d3.scale` intervient.

La fonction `d3.scale` prend des données en entrée et retourne une valeur visuelle en pixels. `d3.scale` doit être configurée avec un **domaine** et une **plage**. Le domaine définit une LIMITE pour les données que nous essayons de représenter visuellement.

```javascript
const x_scale = d3.scaleLinear()
    .domain([10, 500])
    .range([2000000, 16000000]);
```

Décortiquons un peu cela :

* `d3.scaleLinear()` - nous disons à D3 que nous allons utiliser l'échelle linéaire
    
* `.domain([10, 500])` - nous définissons le domaine (Limite) de 10 à 500
    
* `.range([2000000, 16000000])` - nous définissons notre valeur minimale à 2 millions et maximale à 16 millions, ce qui signifie que nous mappons 2 millions à `10px` et 16 millions à `500px`
    

Maintenant, si nous avons une ville avec une population d'environ `8000000` (la moitié de 15 millions), elle serait mappée à une valeur de pixel de `250px` (la moitié de 500).

Il est important de souligner que D3 dispose de diverses formes d'[échelles](https://github.com/d3/d3-scale). Celle que vous décidez d'utiliser sera déterminée par le type de données que vous essayez de représenter.

* Lorsque vous travaillez avec des données représentant des dates, utilisez [d3.scaleTime](https://github.com/d3/d3-scale#scaleTime)
    
* Lorsque vous créez des graphiques à barres, utilisez [d3.scaleBand](https://github.com/d3/d3-scale#scaleBand)
    
* Pour d'autres échelles, consultez [d3.scale](https://github.com/d3/d3-scale)
    

## Comment créer un graphique à barres avec D3.js

Maintenant, appliquons tout ce que nous avons appris pour créer un graphique à barres réel avec D3.

Pour cet exemple, nous allons continuer à construire à partir du code de l'exemple dans la section de chargement de données de ce tutoriel :

```javascript
const el = d3.select("#d3_svg_demo2");

d3.json("https://raw.githubusercontent.com/iamspruce/intro-d3/main/nigeria-states.json").then(({data}) => {
    el
     .selectAll("p")
     .data(data)
	 .join("p")
	  .text((d) => d.Name)
});
```

Tout d'abord, créons les échelles pour notre graphique à barres :

```javascript
const width = 960, height = 500;
const x_scale = d3.scaleBand().range([0, width])
const y_scale = d3.scaleLinear().range([height, 0])
```

Ce qui se passe ici :

* Tout d'abord, nous avons défini notre échelle x (échelle horizontale) avec un minimum de 0 et un maximum de la largeur de notre SVG
    
* Deuxièmement, nous avons défini notre échelle y (échelle verticale) pour varier de 0 à la hauteur de notre SVG
    

Ensuite, nous devons sélectionner notre élément SVG dans le document :

```javascript
const svg = d3.select("#d3_demo")
    .attr("width", width)
    .attr("height", height)
```

Ici, nous avons sélectionné notre élément SVG et défini la hauteur et la largeur selon notre hauteur et largeur spécifiées. Ensuite, chargeons les données JSON depuis notre API :

```javascript
d3.json("https://raw.githubusercontent.com/iamspruce/intro-d3/main/nigeria-states.json").then(({ data }) => {
    data.forEach((d) => (d.Population = +d.info.Population))
})
```

Si cela ne vous semble pas familier, veuillez relire la section sur le chargement des données. En raison de la structure de nos données JSON, j'ai déstructuré `{ data }` depuis l'API.

Les données récupérées arrivent sous forme de chaîne, mais nous avons besoin que le champ Population soit un nombre. Ainsi, en utilisant l'opérateur JavaScript `+`, nous convertissons chaque champ Population en nombre :

```javascript
data.forEach((d) => (d.Population = +d.info.Population))
```

Ensuite, nous devons définir le domaine de nos échelles – et maintenant que nous avons récupéré nos données, nous pouvons le faire :

```javascript
x_scale.domain(data.map((d) => d.Name);
y_scale.domain([0, d3.max(data, (d) => d.Population)]);
```

Voyons ce qui se passe ici :

* `x_scale.domain(`[`data.map`](http://data.map)`((d) =>` [`d.Name`](http://d.Name)`)` - L'échelle x est une échelle de bande, donc nous définissons le domaine au nom des états (36 états)
    
* `y_scale.domain([0, d3.max(data, (d) => d.Population)])` - L'échelle y est une échelle linéaire, donc nous définissons la valeur minimale à 0. Et plutôt que de définir nous-mêmes la valeur maximale, nous laissons D3 le faire pour nous en utilisant la méthode `d3.max()`.
    

NOTE : avec la méthode `d3.max()`, nous parcourons les données fournies et retournons toujours la valeur maximale du champ spécifié (Population dans notre cas).

Enfin, nous devons ajouter les rectangles pour pouvoir voir notre graphique à barres :

```javascript
svg
 .selectAll("rect")
 .data(data)
 .join("rect")
  .attr("class", "bar")
  .attr("x", (d) => x_scale(d.Name))
  .attr("y", (d) => y_scale(d.Population))
  .attr("width", x_scale.bandwidth())
  .attr("height", (d) => height - y_scale(d.Population));
```

D'accord, ce n'est pas quelque chose de nouveau, n'est-ce pas ? Si cela est encore nouveau, veuillez relire la section sur la jointure de données de ce tutoriel. Mais il y a certaines choses que nous voyons pour la première fois :

* `.attr("x", (d) => x_scale(`[`d.Name`](http://d.Name)`))` - Nous définissons la position x (horizontale) de chaque `rect` créé selon l'échelle générée. Même chose pour la position y (verticale `.attr("y", (d) => y_scale(d.Population))`.
    
* `.attr("width", x_scale.bandwidth())` - ici nous définissons la largeur de chaque `rect`. Bien sûr, nous pouvons définir cela à n'importe quel nombre que nous aimons, mais en utilisant `x_scale.bandwidth()`, D3 redimensionne automatiquement le `rect` pour nous afin de correspondre à la largeur de notre SVG.
    
* `.attr("height", (d) => height - y_scale(d.Population))` - enfin, nous définissons la hauteur de chaque `rect` à la hauteur du SVG, puis nous soustrayons la hauteur générée par `y_scale(d.Population)`, en veillant à ce que chaque `rect` soit correctement représenté.
    

Voici le code complet rassemblé en un seul endroit :

```javascript
const width = 960, height = 500;

const x_scale = d3.scaleBand().range([0, width]).padding(0.1);
const y_scale = d3.scaleLinear().range([height, 0]);

const svg = d3.select("#d3_demo")
    .attr("width", width)
    .attr("height", height);

d3.json("https://raw.githubusercontent.com/iamspruce/intro-d3/main/nigeria-states.json")
    .then(({ data }) => {
    
	 data.forEach((d) => (d.Population = +d.info.Population));

	 // Mise à l'échelle du domaine
	 x_scale.domain(data.map((d) => d.Name));
	 y_scale.domain([0, d3.max(data, (d) => d.Population)]);

	 // Ajout des rectangles pour le graphique à barres
	 svg
	  .selectAll("rect")
	  .data(data)
	  .join("rect")
	  .attr("class", "bar")
	  .attr("x", (d) => x_scale(d.Name))
	  .attr("y", (d) => y_scale(d.Population))
	  .attr("width", x_scale.bandwidth())
	  .attr("height", (d) => height - y_scale(d.Population));
	});
```

Et voici le résultat :

```javascript
%[https://codepen.io/Spruce_khalifa/pen/porxVVd]
```

Et voilà, un graphique à barres D3.js très basique. Mais si vous montriez ce graphique à barres à un collègue ou un ami, il vous demanderait probablement "qu'est-ce qui se passe ici, que regardons-nous ?" Cela nous amènerait à un autre sujet – l'**axe**.

### Composant d'axe dans D3

> Le composant d'axe rend des repères de référence lisibles par l'homme pour les échelles. – Docs D3

Pour créer ces repères de référence lisibles par l'homme, `d3.axis` utilise la fonction `d3.scale` pour déterminer le nombre de graduations à générer.

Pour créer différentes orientations pour notre axe, D3 fournit quatre méthodes :

* d3.axisTop
    
* d3.axisBottom
    
* d3.axisLeft
    
* d3.axisRight
    

Voyons un exemple de celles-ci :

```javascript
let svg = d3.select("#d3_demo8").attr('width', 200).attr('height', 200)
let scale = d3.scaleLinear().domain([0, 100]).range([0, 200]);


let bottom_axis = d3.axisBottom(scale);

svg.append("g").call(bottom_axis);
```

```xml
<svg id="d3_demo">
</svg>

<div class="d3_example d3_no_pad" id="d3_svg_demo2">
    <cite class="d3_example-text">Exemple de sortie</cite>
<svg id="d3_demo8"></svg>
</div>
```

Pour faire fonctionner tout cela, vous devez simplement passer votre fonction `d3.scale` existante. Appliquons cela à notre exemple précédent.

La première chose que nous devons faire est de configurer la convention de marge D3.

### Convention de marge D3

La convention de marge est simplement un moyen d'ajouter des marges à nos graphiques afin d'avoir de l'espace pour ajouter notre axe.

Pour créer la marge, créez d'abord un objet avec une propriété pour chacun des quatre côtés :

```javascript
const margin = { top: 20, right: 30, bottom: 55, left: 70 }
```

Ensuite, vous devez définir la largeur et la hauteur pour notre SVG. Pour un graphique réactif, nous définissons la largeur à la largeur du corps du document :

```javascript
const width = document.querySelector("body").clientWidth;
const height = 500;
```

Ensuite, nous devons appliquer cette largeur comme une boîte de vue à notre élément SVG :

```javascript
const svg = d3.select("#d3_demo").attr("viewBox", [0, 0, width, height])
```

Ensuite, nous devons définir `x_scale` et `y_scale` pour qu'ils fonctionnent avec nos nouvelles marges :

```javascript
const x_scale = d3
	.scaleBand()
	.range([margin.left, width - margin.right])
	.padding(0.1);

const y_scale = d3.scaleLinear()
    .range([height - margin.bottom, margin.top]);
```

Ensuite, définissons notre axe gauche et notre axe inférieur – rappelez-vous que nous devons simplement passer notre échelle existante (celles ci-dessus) :

```javascript
let x_axis = d3.axisBottom(x_scale);

let y_axis = d3.axisLeft(y_scale);
```

Tout le reste est identique à notre exemple précédent, sauf la dernière partie où nous ajoutons l'axe :

```javascript
// ajouter l'axe x
svg
 .append("g")
  .attr("transform", `translate(0,${height - margin.bottom})`)
  .call(x_axis)
  .selectAll("text") // tout à partir de ce point est facultatif
  .style("text-anchor", "end")
  .attr("dx", "-.8em")
  .attr("dy", ".15em")
  .attr("transform", "rotate(-65)");

// ajouter l'axe y
svg
 .append("g")
  .attr("transform", `translate(${margin.left},0)`)
  .call(y_axis);
```

Vous pouvez consulter le [code complet et le résultat sur Codepen](https://codepen.io/Spruce_khalifa/pen/RwZvOPx).

### Comment le styliser avec CSS dans D3

Vous remarquerez que notre graphique à barres est de couleur verte – comment cela se fait-il ? Eh bien, nous avons ajouté une classe `bar` à chaque barre du graphique :

```javascript
.attr("class", "bar")
```

Nous pouvons utiliser cette classe pour styliser notre graphique à barres avec CSS :

```css
.bar {
  fill: green;
}
```

## Comment créer une carte du monde avec D3.js

L'une des choses que j'aime personnellement à propos de D3 est sa capacité à gérer les données géographiques. Contrairement à nos exemples précédents, qui utilisaient le format de données JSON pour les cartes, nous allons maintenant utiliser une forme spéciale de données JSON appelée [GeoJSON](http://geojson.org/).

Vous pouvez trouver les données GeoJSON que nous allons utiliser [ici](https://raw.githubusercontent.com/iamspruce/intro-d3/main/data/countries-110m.geojson).

Comme dans nos autres exemples, commençons d'abord par sélectionner notre élément SVG dans le document et configurer également **la convention de marge** :

```javascript
const margin = { top: 5, right: 5, bottom: 5, left: 5 },
	width = document.querySelector("body").clientWidth,
	height = 500;

const svg = d3.select("#d3_demo").attr("viewBox", [0, 0, width, height]);

```

```xml
<body>
<svg id="d3_demo"></svg>
</body>
```

Ensuite, pour générer notre carte, nous aurons besoin d'une projection pour rendre les coordonnées sphériques (dans notre fichier de données) et d'un générateur de chemin pour convertir les coordonnées projetées en un chemin SVG qui est ensuite rendu à l'écran :

```javascript
let projection = d3.geoEquirectangular().center([0, 0]);
```

D3 fournit de nombreuses [projections](https://github.com/d3/d3-geo-projection) (je n'ai utilisé celle-ci que parce que je l'aime). Maintenant que nous avons choisi notre projection, convertissons-la en un chemin SVG. D3 gère la conversion pour nous lorsque nous utilisons la méthode `d3.geoPath()`. Cette méthode prend en entrée une projection (celle que nous avons définie ci-dessus) :

```javascript
const pathGenerator = d3.geoPath().projection(projection);
```

Nous ne voulons pas dessiner la carte directement sur le SVG car nous allons ajouter des animations et du zoom plus tard. Nous ajoutons donc un élément `g` au SVG sélectionné :

```javascript
let g = svg.append("g");
```

Ensuite, nous chargerons nos données pour la carte :

```javascript
d3.json("https://raw.githubusercontent.com/iamspruce/intro-d3/main/data/countries-110m.geojson")
  .then((data) => {
      console.log(data)
  });
```

Si cela ne vous semble pas clair, je vous suggère de relire la section sur le chargement des données.

Enfin, utilisons notre `pathGenerator` pour générer nos chemins :

```javascript
 g.selectAll("path")
    .data(data.features)
    .join("path")
    .attr("d", pathGenerator);
```

Ci-dessus, nous avons utilisé la jointure de données D3 pour ajouter un chemin pour chaque pays, puis nous avons défini l'attribut `d` à notre `pathGenerator` :

```javascript
.attr("d", pathGenerator);
```

Et au cas où cela ne serait pas clair, c'est l'équivalent d'écrire ceci :

```javascript
.attr('d', (d) => pathGenerator(d))
```

Vous pouvez trouver le [code final et l'aperçu en direct sur Codepen](https://codepen.io/Spruce_khalifa/pen/dyzLyxp).

### Comment utiliser plusieurs jeux de données dans D3.js

Parfois, vous voudrez visualiser deux jeux de données provenant de différentes sources. Par exemple, j'ai un fichier de [données](https://github.com/iamspruce/intro-d3/blob/main/data/nigeria_state_boundaries.geojson) qui contient les données géographiques du Nigeria et un autre [fichier](https://github.com/iamspruce/intro-d3/blob/main/data/nigeria-states.json) qui contient des informations sur les états du Nigeria.

Dans la section de chargement des données de ce tutoriel, nous n'avons couvert que le chargement d'un seul jeu de données. Le chargement de plusieurs jeux de données dans D3 ressemble à ceci :

```javascript
Promise.all([
	d3.json("https://raw.githubusercontent.com/iamspruce/intro-d3/main/data/nigeria_state_boundaries.geojson"),
	d3.json("https://raw.githubusercontent.com/iamspruce/intro-d3/main/data/nigeria-states.json")
]).then(([geoJSONdata, countryData]) => {
    console.log(geoJSONdata)
    console.log(countryData)
});
```

En ajoutant toutes les méthodes de chargement de données D3 `d3.json()` à l'intérieur de `Promise.all`, la fonction de rappel `.then()` ne sera appelée que lorsque toutes les données auront fini de charger, bien que si l'un des fichiers de données échoue à charger, la fonction de rappel ne sera pas appelée et entraînera une erreur.

### Carte avec noms de villes

Maintenant, utilisons l'idée de **chargement de plusieurs jeux de données** pour créer une carte avec des noms de villes.

Pour simplifier, nous allons omettre la partie de création de la carte car nous l'avons déjà couverte ci-dessus. Maintenant, nous allons nous concentrer uniquement sur l'ajout des noms des villes :

Une fois les données chargées, nous devons les formater :

```javascript
countryData.data.forEach((d) => {
 d.info.Longitude = +d.info.Longitude;
 d.info.Latitude = +d.info.Latitude;
});
```

Ci-dessus, nous avons converti les longitudes et les latitudes. Ensuite, nous devons adapter notre carte à notre conteneur. Pour cela, vous utiliserez la méthode `d3.fitSize()` :

```javascript
projection.fitSize([width, height], geoJSONdata);
```

Enfin, nous devons ajouter les noms des villes :

```javascript
g.selectAll("text")
 .data(countryData.data)
 .join("text")
  .attr("x", (d) => projection([d.info.Longitude, d.info.Latitude])[0])
  .attr("y", (d) => projection([d.info.Longitude, d.info.Latitude])[1])
  .attr("dy", -7)
  .style("fill", "black")
  .attr("text-anchor", "middle")
  .text((d) => d.Name);
```

Et voilà ! Nous avons une carte avec les noms des villes (j'ai peut-être ajouté des cercles aussi, parce que je pense que c'est cool). Le [code complet est sur Codepen](https://codepen.io/Spruce_khalifa/pen/BadEywO).

## Gestion des événements avec D3.js

Au début de ce tutoriel, nous avons parlé des sélections, mais une chose que nous n'avons pas couverte était la gestion des événements.

Dans D3, nous pouvons ajouter ou supprimer des gestionnaires d'événements aux éléments du document sélectionnés en utilisant la méthode `.on()`.

La méthode `.on()` accepte deux arguments :

1. Type d'événement (généralement une chaîne)
    
2. Une fonction de rappel qui est appelée lorsque notre événement est déclenché
    

### Types d'événements dans D3

Le type d'événement `.on()` de D3 peut être n'importe quel [type d'événement DOM](https://developer.mozilla.org/en-US/docs/Web/Events#Standard_events), mais les événements les plus courants avec D3 sont :

```javascript
| Type d'événement  | Description  |
|---|---|
| zoom  | la sélection est en cours de panoramique et de zoom  |
| click  | la sélection a été cliquée  |
| mouseover  | le pointeur de la souris passe sur une sélection  |
| mouseout  | le pointeur de la souris quitte une sélection  |
```

### Carte avec panoramique et zoom

Pour voir comment fonctionne la gestion des événements D3, ajoutons un panoramique et un zoom à notre carte créée précédemment.

La première chose que nous devons faire est de définir la fonction de zoom :

```javascript
let zooming = d3
  .zoom()
  .scaleExtent([1, 8])
  .on("zoom", (event) => {
   console.log(event)
  })
```

Ensuite, la chose suivante que nous devons faire est d'utiliser la méthode `d3.zoom()`. Nous définissons également `scaleExtent([1,8])`. Nous faisons cela pour définir la limite du zoom, sinon vous continuerez à zoomer à l'infini. Maintenant, ajoutons la transformation à nos chemins de carte dans la fonction de rappel :

```javascript
.on("zoom", (event) => {
  // transformer les chemins lors du zoom
  g.selectAll("path").attr("transform", event.transform);
  
  // transformer les cercles lors du zoom
  g.selectAll("circle")
    .attr("transform", event.transform)
	.attr("r", 5 / event.transform.k);
  
  // transformer le texte lors du zoom
  g.selectAll("text")
	.attr("transform", event.transform)
	.style("font-size", `${18 / event.transform.k}`)
	.attr("dy", -7 / event.transform.k);
});
```

NOTE : `event.transform` est un raccourci pour définir `translate('x','y')` et `scale` (event.transform.k).

Enfin, appelons la fonction de zoom sur notre sélection SVG :

```javascript
svg.call(zooming)
```

Vous pouvez trouver le [code complet et l'aperçu sur Codepen](https://codepen.io/Spruce_khalifa/pen/MWvROBq).

### Zoom programmatique dans D3

Il s'avère que dans D3, nous pouvons contrôler le zoom de manière programmatique, ce qui nous permet de créer des boutons qui peuvent être utilisés pour contrôler le comportement du zoom :

Ajoutons ces boutons à notre carte précédente :

```xml
<body>
 <div class="btn-group-vertical" role="group" aria-label="..." id="float-button-group">
  <button class="btn-default" id="zoomIn">
   <svg class="svg-icon" viewBox="0 0 20 20">
    <title>Zoom In</title>
	...svg icon
	</svg>
  </button>
  <button class="btn-default" id="zoomOut">
   <svg class="svg-icon" viewBox="0 0 20 20">
  <title>Zoom Out</title>
  ...svg icon
	</svg>
  </button>
  <button class="btn-default" id="resetZoom">
   <svg class="svg-icon" viewBox="0 0 20 20">
	<title>Reset Zoom</title>
	...svg icon
	</svg>
  </button>
</div>
    
<svg id="d3_demo"></svg>
</body>
```

L'étape suivante consiste à sélectionner ces boutons et à contrôler le comportement du zoom :

```javascript
d3.select("#zoomIn").on("click", () => {
  svg.transition().call(zooming.scaleBy, 2);
});
d3.select("#zoomOut").on("click", () => {
  svg.transition().call(zooming.scaleBy, 0.5);
});
d3.select("#resetZoom").on("click", () => {
  svg.transition().call(zooming.scaleTo, 1);
});
```

Qu'est-ce que `scaleBy` et `scaleTo` ? `scaleBy` multiplie l'échelle actuelle par notre valeur donnée (2), tandis que `scaleTo` définit le facteur d'échelle à notre valeur donnée (1) qui réinitialise le zoom.

Vous pouvez trouver l'[aperçu et le code complet sur Codepen](https://codepen.io/Spruce_khalifa/pen/eYEoyYo).

### Comment ajouter des ToolTips dans D3

Ajoutons des ToolTips à notre carte. Un tooltip affiche plus d'informations sur un élément lorsque l'utilisateur survole cet élément.

Créons d'abord le tooltip :

```javascript
let tooltip = d3
  .select("body")
  .append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);
```

Ensuite, ajoutons le tooltip lorsque le cercle est survolé, et supprimons-le lorsque le pointeur de la souris quitte le cercle :

```javascript
g.selectAll("circle")
  ...
  .style("fill", "green")
  .on("mouseover", (event, d) => {
    tooltip.transition().duration(200).style("opacity", 0.9);
    tooltip.html(`<p>Population: ${d.info.Population}</a>` + `<p>Name: ${d.Name}</p>`)
    .style("left", event.pageX + "px")
    .style("top", event.pageY - 28 + "px");
  })
  .on("mouseout", (d) => {
    tooltip.transition().duration(500).style("opacity", 0);
  });
```

Voici le [code final et l'aperçu](https://codepen.io/Spruce_khalifa/pen/mdMYEBJ) (essayez de survoler les cercles) :

## Conclusion

Félicitations, ninja de D3 ! Vous êtes arrivé jusqu'ici. Espérons que vous avez appris les bases de la visualisation de données avec D3.

Voici quelques étapes suivantes :

* Consultez la [certification en visualisation de données de freeCodeCamp](https://www.freecodecamp.org/learn/data-visualization/)
    
* Consultez la documentation et plus encore sur le [site officiel de D3](https://d3js.org/)
    

Si vous avez créé quelque chose de merveilleux avec cela, n'hésitez pas à tweeter à ce sujet et à me taguer [@sprucekhalifa](https://twitter.com/sprucekhalifa). Et n'oubliez pas de cliquer sur le bouton suivre.

Oh, et bon codage !