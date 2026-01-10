---
title: Apprendre D3.js en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T10:10:31.000Z'
originalURL: https://freecodecamp.org/news/learn-d3-js-in-5-minutes-c5ec29fb0725
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l5jZdAa3_ZeDSoxHzmIagw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Apprendre D3.js en 5 minutes
seo_desc: 'By Sohaib Nehal

  An introduction to creating visual representations of your data


  D3.js is a JavaScript library used to manipulate documents based on data. It uses
  HTML, CSS, and SVG to create visual representations of data which can be viewed
  on any ...'
---

Par Sohaib Nehal

#### Une introduction à la création de représentations visuelles de vos données

![Image](https://cdn-media-1.freecodecamp.org/images/1*l5jZdAa3_ZeDSoxHzmIagw.png)

D3.js est une bibliothèque JavaScript utilisée pour manipuler des documents basés sur des données. Elle utilise HTML, CSS et SVG pour créer des représentations visuelles de données qui peuvent être visualisées sur n'importe quel navigateur moderne.

Elle offre également des fonctionnalités impressionnantes pour les interactions et les animations.

Dans ce tutoriel, nous explorerons les concepts et fonctionnalités de base de D3.js. Nous apprendrons à l'utiliser à l'aide de quelques exemples comme le rendu d'un graphique à barres, le rendu d'éléments HTML et SVG, et l'application de transformations et d'événements.

**Nous avons également créé un cours gratuit en 10 parties sur D3.js sur Scrimba. [Découvrez-le ici.](https://scrimba.com/g/gd3js)**

### Démarrage avec D3

Puisque D3.js est une bibliothèque JavaScript, vous pouvez simplement l'inclure dans votre fichier HTML à l'intérieur d'une balise script.

```html
<script src='https://d3js.org/d3.v4.min.js'></script>
```

Le [code source complet et les tests](https://github.com/d3/d3) sont également disponibles [pour téléchargement](https://github.com/d3/d3/zipball/master) sur GitHub.

### Sélection du DOM

En utilisant D3.js, nous pouvons manipuler le Document Object Model (DOM), ce qui signifie que nous pouvons sélectionner des éléments et appliquer diverses transformations.

Commençons par un exemple simple, où nous utiliserons D3 pour sélectionner et changer la couleur et la taille de la police d'une balise de titre.

```html
<html>
<head>
    <title>Apprendre D3 en 5 minutes</title>
</head>
<body>

<h3>Aujourd'hui est une belle journée!!</h3>

<script src='https://d3js.org/d3.v4.min.js'></script>

<script>
    d3.select('h3').style('color', 'darkblue');
    d3.select('h3').style('font-size', '24px');
</script>
</body>
</html>
```

Nous enchaînons simplement la méthode `select()` sur l'objet `d3`, puis nous utilisons `style()`. Le premier paramètre indique ce que nous voulons changer et le second donne la valeur. Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DHfDsYddhyFresbaU4-P_Q.png)
_Exemple 1 : Sélection du DOM_

### Liaison de données

Le prochain concept que vous devez apprendre est la liaison de données, car c'est l'une des fonctionnalités les plus intéressantes de D3. Grâce à elle, nous pouvons remplir ou manipuler des éléments DOM en temps réel.

Dans notre HTML, nous avons une simple liste non ordonnée `<ul>` :

```
<ul> </ul>
```

Nous voulons créer les éléments de la liste à l'aide d'un objet de données. Voici le code pour faire exactement cela :

```html
<script>
    var fruits = ['pomme', 'mangue', 'banane', 'orange'];
    d3.select('ul')
        .selectAll('li')
        .data(fruits)
        .enter()
        .append('li')
        .text(function(d) { return d; });
</script>
```

Dans notre code JavaScript ci-dessus, D3 sélectionne d'abord le `<ul>` et tous les éléments `<li>` à l'intérieur avec les méthodes `select()` et `selectAll()`. Il peut sembler un peu étrange que nous sélectionnions tous les éléments `li` avant de les avoir créés, mais c'est ainsi que fonctionne D3.

Nous passons ensuite les données avec la méthode `data()`, et nous ajoutons `enter()`, qui fonctionne un peu comme une boucle. Tout ce qui suit ce point sera exécuté une fois par élément dans le tableau `fruits`.

En d'autres termes, il ajoute ensuite un `<li>` pour chaque élément dans les données. Pour chaque balise `<li>`, il ajoute également du texte à l'intérieur en utilisant la méthode `text()`. Le paramètre `d` à l'intérieur de la fonction de rappel `text()` fait référence à l'élément dans le tableau à l'itération donnée (_pomme, mangue, etc._).

Voici donc notre résultat final :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CnImNDBOg4Ei-kAyacb3Xg.png)
_Exemple 2 : Liaison de données_

### Création d'éléments SVG

Les graphiques vectoriels scalables (SVG) sont un moyen de rendre des éléments graphiques et des images dans le DOM. Comme SVG est basé sur des vecteurs, il est à la fois léger et scalable. D3 utilise SVG pour créer toutes ses visualisations, et c'est donc un bloc de construction central de la bibliothèque.

Dans l'exemple ci-dessous, un rectangle est dessiné à l'aide de D3 dans un conteneur SVG.

```js
// Sélectionner l'élément SVG
var svg = d3.select('svg');

// Créer un élément rectangle à l'intérieur du SVG
svg.append('rect')
   .attr('x', 50)
   .attr('y', 50)
   .attr('width', 200)
   .attr('height', 100)
   .attr('fill', 'green');
```

Dans ce code, D3 rend un élément rectangle à l'intérieur du DOM. Il sélectionne d'abord l'élément SVG, puis rend un élément rectangle à l'intérieur. Il définit également les coordonnées x et y du rectangle ainsi que sa largeur, sa hauteur et ses propriétés de remplissage à l'aide de la méthode `attr()`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sk3Jxh93HMTUAPeC-_fTRg.png)
_Exemple 3 : Création d'un élément SVG_

### Création d'un graphique à barres

D3 nous permet également de créer de nombreux types de graphiques et de diagrammes pour représenter les données de manière efficace. Dans l'exemple ci-dessous, nous créons un simple graphique à barres en utilisant D3.

Commençons par créer une balise SVG directement dans notre HTML.

```html
<svg width='200' height='500'></svg>
```

Ensuite, nous écrivons le JavaScript nécessaire pour rendre le graphique à barres dans notre balise `<svg>` :

```js
var data = [80, 120, 60, 150, 200];

var barHeight = 20;

var bar = d3.select('svg')
          .selectAll('rect')
          .data(data)
          .enter()
          .append('rect')
          .attr('width', function(d) {  return d; })
          .attr('height', barHeight - 1)
          .attr('transform', function(d, i) {
            return "translate(0," + i * barHeight + ")";
          });
```

Dans ce code, nous avons un tableau de nombres que nous utiliserons pour rendre notre graphique à barres. Chaque élément du tableau représente une seule barre. Nous utilisons le fait que les barres sont simplement des rectangles avec une largeur ou une hauteur variable.

Après avoir sélectionné les éléments SVG et rectangle, nous passons notre ensemble de données en utilisant la méthode `data()` et nous appelons `enter()` pour commencer à boucler sur les données.

Pour chaque élément de données, nous rendons un rectangle et définissons sa largeur équivalente à sa valeur. Nous définissons ensuite la hauteur de chaque barre, et pour éviter les chevauchements, nous lui donnons un peu de marge en soustrayant 1 de `barHeight`.

Nous transformons ensuite nos barres en utilisant la propriété translate qui positionnera chaque rectangle l'un après l'autre plutôt que de commencer au même point. `transform()` prend une fonction de rappel qui reçoit les données et l'index dans ses paramètres. Nous translatons le rectangle sur l'axe y, en multipliant l'index par la hauteur de la barre.

Voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PcGb1csr4o5hZZ7d0ZzqMQ.png)
_Exemple 4 : Création d'un graphique à barres_

### Gestion des événements

Enfin, examinons également la gestion des événements. D3 prend également en charge les événements intégrés et personnalisés que nous pouvons lier à n'importe quel élément DOM avec son écouteur. Dans l'exemple ci-dessous, nous lions l'événement de clic au bouton et nous ajoutons une balise de titre au corps dans son gestionnaire d'événements.

```js
d3.select('#btn')
        .on('click', function () {
            d3.select('body')
               .append('h3')
               .text('Aujourd\'hui est une belle journée!!');
        });
```

Ainsi, lorsque nous cliquons sur le bouton, le texte suivant apparaît :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DiReX2IfapXHHuSTLThGNg.png)
_Exemple 5 : Gestion des événements_

### Conclusion

D3.js est une bibliothèque JavaScript très puissante, mais simple, qui vous permet de manipuler et de donner vie à des documents basés sur des données en utilisant HTML, CSS et SVG.

Il existe de nombreuses bonnes ressources en ligne pour apprendre D3.js. **Il existe un cours gratuit sur D3.js que nous avons créé sur Scrimba et qui est disponible gratuitement** [**ici.**](https://scrimba.com/g/gd3js)

Merci :)

_Je suis Sohaib Nehal. Je suis un développeur d'applications Web Full-Stack. Vous pouvez me joindre à sohaib.nehal@ymail.com ou sur Twitter @Sohaib_Nehal. Merci :-)_