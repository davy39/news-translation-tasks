---
title: Une référence visuelle pour D3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-27T12:54:08.000Z'
originalURL: https://freecodecamp.org/news/a-visual-reference-for-d3
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/D3-article-image.jpg
tags:
- name: D3
  slug: d3
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
seo_title: Une référence visuelle pour D3
seo_desc: 'By Zaid Humayun

  I’ve been using D3 quite a bit recently to build an analytics dashboard. The main
  reason I went with D3 was because I got tired of dealing with the limitations of
  the various charting libraries and trying to understand their documenta...'
---

Par Zaid Humayun

J'ai utilisé D3 assez récemment pour construire un tableau de bord d'analyse. La raison principale pour laquelle j'ai choisi D3 est que j'en avais marre de devoir gérer les limitations des diverses bibliothèques de graphiques et d'essayer de comprendre leur documentation.

Je me suis retrouvé dans une situation où je passais plus de temps à essayer de comprendre si la bibliothèque que j'utilisais pouvait faire ce que je voulais plutôt qu'à essayer de comprendre comment faire ce que je voulais.

Avec D3, il n'y a presque jamais de cas où l'on se demande si l'on peut faire quelque chose. Il s'agit toujours de savoir comment on peut le faire.

Certes, se familiariser avec l'API de D3 est un défi de taille, mais cela en vaut la peine.

Dans cet article, je vais essayer de vous donner une représentation visuelle de ma compréhension de D3 après avoir travaillé avec lui pendant un certain temps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7Q2OWU3mpakpTMcr.jpg)
_Idées principales derrière D3_

### Les hauts et les bas de D3

Ce que j'aime avec D3, c'est qu'il est construit sur les plus petites primitives, et vous avez accès à toutes ces primitives.

Si vous deviez utiliser une bibliothèque de graphiques typique pour React, vous feriez probablement quelque chose comme ceci

```javascript
import { BarChart } from 'generic-charting-library'

export default class Chart() {
  render() {
    return (
      <BarChart data={data} />
    )
  }
}
```

Ce qui précède est parfaitement adapté à la plupart des cas d'utilisation. Cependant, dès que vous voulez faire quelque chose de légèrement plus compliqué, comme interagir avec le graphique à barres de manière unique (pensez au-delà de l'affichage d'une info-bulle), mon expérience personnelle a été que cela se transforme en une guerre avec la documentation de la bibliothèque.

Tout d'abord, vous devez déterminer si c'est même possible de faire cela avec la bibliothèque, puis vous devez déterminer comment le faire.

La première partie, selon mon expérience, est la partie difficile. Il est assez frustrant de chercher quelque chose dont on n'est pas sûr de l'existence. Cependant, avec D3, ce n'est pas le cas. Presque tout ce que vous voulez faire peut être fait avec D3. Il s'agit simplement de déterminer comment le faire.

L'inconvénient, bien sûr, est que l'API et la documentation de D3 sont si vastes et étendues que vous finissez par avoir des morceaux de connaissances disparates sur le fonctionnement des choses. Cela est également une conséquence de la manière dont j'ai choisi d'apprendre D3, c'est-à-dire en construisant quelque chose avec.

Disons, par exemple, que vous voulez construire un graphique à barres. Eh bien, vous allez probablement chercher quelque chose comme comment définir et placer des axes sur une page web. Ensuite, vous allez probablement chercher comment définir les barres réelles du graphique lui-même. Ce sont des problèmes bien définis et ils ont des solutions simples.

J'ai pris à peu près la même route et j'ai fini dans un endroit frustrant où je pouvais faire fonctionner les choses mais je ne pouvais pas tout à fait comprendre comment tout cela s'assemblait.

Je vais expliquer mon processus de réflexion sur la manière dont j'ai assemblé toutes les différentes pièces.

### Le tableau d'ensemble

L'image suivante représente un graphique à barres simpliste (quelque chose que nous allons essayer de recréer pour ce post)

![Image](https://cdn-media-1.freecodecamp.org/images/0*M2wwyv0H_FKdmvvv.jpg)
_Graphique à barres typique_

Maintenant, voici le même graphique à barres avec les différents composants marqués. Par composants, je veux dire les différentes choses dont nous devons nous soucier lors de la création du graphique à barres en utilisant D3.

![Image](https://cdn-media-1.freecodecamp.org/images/0*j2P5HLdATpIsLCOM.jpg)
_Graphique à barres étiqueté_

1. L'axe X
2. L'axe Y
3. Le titre
4. Les barres (je les compte toutes comme une seule)
5. L'espacement entre les graduations sur l'axe X
6. La zone du graphique elle-même
7. L'espacement entre les graduations sur l'axe Y

Nous allons explorer tout sauf l'espacement entre les graduations en détail. L'espacement entre les graduations se réglera de lui-même lorsque nous comprendrons comment construire les axes.

### Les petites choses qui composent le tableau d'ensemble

Avant même de commencer à composer les petites pièces qui constituent le tableau d'ensemble, nous devons comprendre l'élément qui fait partie de chaque composant du graphique ci-dessus : l'élément SVG.

### L'élément SVG

Un graphique D3 est principalement composé d'éléments SVG. Dans le graphique à barres ci-dessus, l'axe x, l'axe y, chaque barre individuelle sont toutes des instances d'éléments SVG.

Je recommande de lire [cette page](https://developer.mozilla.org/en-US/docs/Web/SVG) pour mieux comprendre ce qu'est un SVG. Les SVG sont essentiellement la manière dont vous décrivez des graphiques 2D sur une page web.

L'exemple le plus basique d'un élément SVG est l'élément cercle.

Voir le stylo [qGMxzO](https://codepen.io/redixhumayun/pen/qGMxzO/) par Zaid Humayun ([@redixhumayun](https://codepen.io/redixhumayun)) sur [CodePen](https://codepen.io).

Jetez un coup d'œil au codepen ci-dessus et vous devriez voir la définition pour le cercle SVG à l'intérieur du fichier HTML.

Je vous conseille de parcourir la documentation SVG sur MDN (lien ci-dessus), et de vous familiariser avec elle. D3 utilise largement les SVG.

#### Le G dans SVG

Il existe un type spécifique d'élément SVG appelé élément G. De manière similaire à la façon dont nous avons défini l'élément cercle ci-dessus, nous définissons cela avec

```
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- Utilisation de g pour hériter des attributs de présentation -->
  <g fill="white" stroke="green" stroke-width="5">
    <circle cx="40" cy="40" r="25" />
    <circle cx="60" cy="60" r="25" /> </g>
</svg>
```

Considérez un élément `g` comme similaire à un élément `div` qui est utilisé comme conteneur en HTML. Ils sont tous deux utilisés pour regrouper certains éléments.

Lisez la documentation MDN pour `g` [ici](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g)

Si vous voulez comprendre pourquoi les gens utilisent l'élément `g`, lisez [ceci](http://tutorials.jenkov.com/svg/g-element.html)

### Les données dont nous avons besoin

Avant de continuer, créons rapidement les données que nous allons utiliser. Voici un exemple de fichier JSON que nous pouvons utiliser pour créer un graphique à barres.

```
[
  {
    "key": "A",
    "value": 20
  },
  {
    "key": "B",
    "value": 40
  },
  {
    "key": "C",
    "value": 80
  },
  {
    "key": "D",
    "value": 55
  },
  {
    "key": "E",
    "value": 70
  }
]
```

### La zone du graphique

Commençons par créer une simple zone de graphique. La façon de créer une zone de graphique est de configurer un élément SVG de base puis d'assigner un attribut viewBox.

Ignorez simplement ce qu'est l'attribut viewBox pour l'instant. Ce n'est pas pertinent pour la discussion de ce post.

```
<svg class="chart" viewBox="0 0 800 600">
```

Vous ne verrez rien à l'écran pour l'instant car le graphique est transparent à ce stade. Si vous utilisez l'inspecteur de navigateur, cependant, vous verrez l'élément SVG.

Nous allons également définir quelques dimensions pour notre zone de graphique comme la hauteur, la largeur et les marges.

```
const height = 600
const width = 800
const margin = { top: 15, right: 30, bottom: 15, left: 30 }
```

Maintenant que nous avons défini les dimensions, nous devons réellement créer la zone pour notre graphique dans le DOM. Pour cela, nous devons utiliser quelque chose appelé `d3.select`

Considérez cela comme exactement la même chose que l'ensemble des commandes `document.getElementBy[X]` que le DOM offre nativement.

Lorsque vous utilisez quelque chose comme `d3.select('.chart')`, vous demandez à D3 de sélectionner un élément avec une classe nommée chart.

Notez que nous sauvegardons la sélection à l'intérieur d'une variable. Cela sera important plus tard.

Lorsque vous sélectionnez quelque chose avec `d3.select`, D3 vous permet d'utiliser l'enchaînement de méthodes pour modifier des attributs comme la largeur et la hauteur, comme je l'ai fait ici.

```
const chart = d3.select(".chart")  
				.attr("width", width)  
                .attr("height", height)
```

Ce avec quoi nous allons finir est quelque chose comme l'image suivante

![Image](https://cdn-media-1.freecodecamp.org/images/0*qNzjoEPBwmAozK2t.jpg)
_Affichage du graphique avec les marges_

Ne vous inquiétez pas des marges pour l'instant. Nous nous en occuperons plus tard.

### Définition des axes

Maintenant, nous commençons avec la partie substantielle de D3 : la création et le placement de nos axes.

Avant de pouvoir commencer, nous devons comprendre quelque chose de fondamental sur le fonctionnement des axes D3 : ils sont essentiellement une cartographie d'un ensemble de valeurs à un autre ensemble de valeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LbKrhlEvRrf8iXKG.jpg)

Les deux ensembles de valeurs sont appelés domaine et plage. La cartographie de D3 fonctionne du domaine vers la plage.

J'ai défini deux lignes de nombres vraiment simples pour illustrer le domaine et la plage. La plage est exactement la même que le domaine avec le double du nombre de marques.

Dans cet exemple, il est très facile de voir comment le domaine peut être cartographié vers la plage. Vous devez simplement multiplier la valeur par 2 puisque la plage a le double du nombre de marques et a la même valeur de marque de départ de 0.

J'ai dessiné deux lignes en pointillés pour montrer les cartographies suivantes

```
2 -> 4
5.5 -> 11
```

Maintenant, D3 n'est pas limité à n'avoir que des nombres réels (ou même simplement des nombres) pour définir des échelles. Vous pouvez même utiliser des caractères pour définir vos échelles.

#### L'échelle Y

Nous allons commencer par l'échelle Y.

D3 a différents types d'échelles mais celle que nous allons utiliser s'appelle l'échelle linéaire.

Pour définir l'échelle, nous avons besoin de deux choses : le domaine et la plage.

Nous allons utiliser une règle simple et stupide pour définir notre domaine. Nous allons supposer que la valeur minimale que nous pouvons avoir pour l'une de nos catégories est 0 et la valeur maximale est 100. Pas de nombres négatifs. Le domaine devient alors `[0, 100]`

```
const y = d3.scaleLinear()            
			.domain([0, 100])            
            .range([height - margin.bottom, margin.top])
```

Une chose que nous devons examiner ici est la plage. Il m'a fallu un certain temps pour comprendre pourquoi la plage semble être "inversée". Ma première pensée était que la plage devrait être `[margin.top, height - margin.bottom]`. Mais nous voulons que notre axe Y pour le graphique commence en bas et se déplace verticalement vers le haut.

Nous allons considérer les deux scénarios suivants dans un diagramme ultérieur pour examiner cela.

```
1. .range([height - margin.bottom, margin.top])
2. .range([margin.top, height - margin.bottom])
```

La différence importante entre les deux scénarios est que dans le premier scénario, nous traitons la valeur de hauteur comme notre valeur "zéro". Dans le deuxième scénario, nous traitons la valeur `margin.top` comme notre valeur 'zéro'.

> _Une chose à retenir avant de continuer : le point d'origine de chaque système de coordonnées SVG est dans le coin supérieur gauche._

Interprété autrement, le bas de l'axe Y est notre valeur "zéro" dans le premier scénario et le haut de l'axe Y est notre valeur "zéro" dans le deuxième scénario.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4o4B62gZcCxV2tTu.jpg)
_Les deux scénarios représentés visuellement_

Dans l'image ci-dessus, le scénario 1 est à gauche et le scénario 2 est à droite. Vous pouvez voir la direction du mouvement pour le domaine dans chaque image.

Dans le scénario 1, le domaine grandit vers le haut à partir du bas, ce que nous voulons. Dans le scénario 2, le domaine grandit vers le bas à partir du haut, ce que nous ne voulons pas.

J'apprécie que j'ai peut-être rendu les choses plus confuses pour ceux d'entre vous qui ont réussi à saisir le concept ci-dessus de manière intuitive, mais c'est quelque chose qui m'a pris un certain temps à comprendre. Si vous comprenez de manière intuitive, ne vous inquiétez pas de ce qui précède. Si vous ne comprenez toujours pas, vous le comprendrez à la fin de ce post.

#### L'échelle X

L'échelle X est un peu plus facile à comprendre. Nous avons besoin que l'échelle X grandisse de gauche à droite en tenant compte de la largeur de notre zone de graphique et aussi des marges à gauche et à droite.

Le domaine de cette échelle est un peu plus confus cependant parce que nous ne traitons plus avec des nombres. Nous traitons avec les lettres de nos catégories à la place.

Pour comprendre comment construire cette échelle, nous devons d'abord comprendre quelque chose appelé l'échelle ordinale. Le moyen le plus rapide de comprendre l'échelle ordinale est de considérer les différences entre les échelles linéaires et ordinales.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VbuoXdb6_GMV98lk.jpg)
_L'échelle linéaire et ordinale_

Dans l'image ci-dessus, vous pouvez voir un dessin approximatif des deux échelles. La différence importante à noter est que l'échelle linéaire est une échelle **continue** et l'échelle ordinale est une échelle **discrète**.

Dans l'exemple de l'échelle linéaire, si vous deviez fournir une valeur de 5,5, elle serait cartographiée au point médian entre 5 et 6. Cependant, si vous deviez fournir une valeur d'une lettre quelque part entre C et D (qui n'existe pas), D3 n'aurait aucune idée de comment la cartographier. En ce qui concerne D3, il n'y a aucun moyen de cartographier cette valeur parce que vous avez déclaré que toutes ces valeurs sont discrètes. C'est-à-dire qu'il n'y a pas de valeurs de connexion entre elles.

Maintenant, construisons l'axe X.

```
function getKeys(array) {
  return array.map(arrObj => {
    return arrObj.category;
  });
}
const keys = getKeys(data)

const x = d3.scaleOrdinal()
            .domain([...keys])
            .range([margin.left, width - margin.right])
```

Si vous vous demandez ce que fait la fonction et la variable keys, c'est pour extraire toutes les catégories présentes dans nos données et les fournir à la fonction de domaine sous forme de tableau.

J'aurais tout aussi facilement pu écrire `.domain(['A', 'B', 'C', 'D', 'E'])` mais alors j'aurais dû mettre à jour cela manuellement chaque fois que mes données changeaient.

La plage, comme je l'ai déjà mentionné, doit croître de gauche à droite. Donc, nous laissons de côté la marge à gauche, nous parcourons la longueur de la largeur et nous laissons de côté la marge à droite.

#### Création des axes réels

Maintenant, nous avons la zone du graphique et les échelles définies, nous devons configurer les axes eux-mêmes. Voici comment nous faisons cela.

```
const xAxis = d3.axisBottom(x)
```

Ici, nous créons une **fonction** appelée xAxis qui utilise la fonction `d3.axisBottom` avec notre échelle x fournie comme paramètre.

Pour afficher réellement l'axe X sur notre graphique, nous devons faire ce qui suit

```
chart.append('g')
      .attr('transform', `translate(0, ${height})`)
      .call(xAxis)
```

Deux choses à examiner ici.

Nous ajoutons un élément `g` à notre graphique. Nous avons discuté de l'élément `g` dans une section précédente. Nous appliquons ensuite une transformation à notre élément `g`. Cette transformation est quelque chose qui revient souvent dans D3.

Les SVG ont ce que l'on appelle des fonctions de transformation. Il existe plusieurs types de fonctions de transformation, mais celle qui nous intéresse ici est `translate`. `Translate` accepte deux paramètres, une coordonnée `x` et `y`. Cela signifie combien d'unités de pixels déplacer l'élément `g` soit dans la direction X soit dans la direction Y.

Vous pouvez lire plus sur les transformations [ici](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform).

Les deux paramètres que nous fournissons à la fonction `translate` sont 0 et `height`. Rappelez-vous que le point d'origine de notre graphique SVG est dans le coin supérieur gauche. Puisque nous savons déjà qu'il s'agit d'un axe horizontal qui commence au point d'origine, nous devons le déplacer verticalement vers le bas de `height` unités.

Si vous ne fournissiez pas l'attribut de transformation, l'axe X serait situé en haut de votre graphique.

La dernière partie de la chaîne de méthodes est une fonction `call` où xAxis est fourni comme paramètre. C'est probablement l'aspect le plus déroutant jusqu'à présent en raison du mauvais choix de terminologie.

Nous allons examiner ces deux lignes en premier.

```
.append('g')
.attr('transform', `translate(0, ${height})`)
```

Ce que vous devez comprendre, c'est que lorsque vous faites quelque chose comme `chart.append('g')`, cela ajoute un élément `g` à l'élément chart, sélectionne l'élément `g` puis le retourne. Vous pouvez tester cela en faisant ce qui suit

```
const test = chart.append('g')      
			.attr('transform', `translate(0, ${height})`)      	
            .call(xAxis)console.log(test)
```

Lorsque le résultat du log apparaît, vous verrez un élément `g` sous un objet `Selection`. C'est en fait ce qui nous permet de faire de l'enchaînement de méthodes sur la méthode `append`. Puisqu'elle retourne l'élément `g`, nous pouvons le transformer dans le cadre de la même chaîne de méthodes.

Passons maintenant à la dernière ligne

```
.call(xAxis)
```

Voici ce que dit la documentation de D3 sur `call`

> _Invoque la fonction spécifiée exactement une fois, en passant cette sélection ainsi que tous les arguments optionnels. Retourne cette sélection._

Donc, nous savons que nous utilisons call comme une fonction et nous devons lui passer une fonction comme paramètre. Nous savons cela parce que la documentation dit qu'elle invoque la fonction spécifique exactement une fois. Maintenant, l'autre chose à réaliser est que xAxis est aussi une fonction. Vous pouvez vérifier cela à nouveau en enregistrant xAxis.

Mais, si xAxis est aussi une fonction, alors elle a besoin d'un paramètre qui lui est passé également. Relisez la documentation pour `call` et vous remarquerez qu'elle dit "passe cette sélection...". Cela signifie que la fonction xAxis est appelée **implicitement** avec la sélection `g` retournée par l'appel de `chart.append('g')`

Devoir expliquer comment `call` fonctionne est précisément la raison pour laquelle je ne l'aime pas. Il se passe trop de choses implicitement qui semblent simplement de la magie noire.

Si vous êtes toujours confus sur le fonctionnement de `call`, espérons que le graphique suivant vous éclairera.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NQRME3mBTerW3CVWukVUZQ.jpeg)
_Comment fonctionne Call_

La création de l'axe Y maintenant que nous savons comment fonctionne l'axe X est beaucoup plus simple. Nous utilisons les mêmes principes mais nous remplaçons `axisBottom` par `axisLeft` et nous changeons légèrement la fonction de translation.

```
const yAxis = d3.axisLeft(y);

chart
  .append("g")
  .attr("transform", `translate(${margin.left}, ${margin.bottom})`)
  .call(yAxis);
```

Vous remarquerez que l'attribut `transform` a une fonction `translate` où l'attribut `y` est défini sur `margin.bottom`. Si vous revenez à la plage que nous avons définie pour l'échelle y, vous remarquerez que nous l'avons définie sur `height - margin.bottom`.

Lorsque nous appelons la fonction `axisBottom` de D3, D3 placera cela à `height - margin.bottom`, mais le bas du graphique est en fait à `height`, donc nous ajoutons le décalage `margin.bottom`.

### Placement des barres

C'est la partie la plus visuellement importante du graphique car c'est là que l'utilisateur voit réellement les données.

Tout d'abord, laissez-moi vous montrer le code qui créera les barres pour nous, puis nous le passerons en revue.

```
chart.selectAll('rect')
    .data(data)
    .join('rect')
    .attr('x', d => x(d.category))
    .attr('y', d => y(d.value))
    .attr('width', x.bandwidth())
    .attr('height', height - y(d.value))
    .style('fill', 'steelblue')
```

Les deux premières lignes sont simples. `selectAll` fonctionne de la même manière que `select` sauf qu'il retourne toutes les sélections possibles d'un élément spécifique.

L'appel de `.data` vous permet de définir les données que vous souhaitez associer aux éléments DOM.

Maintenant, le `.join` est là où se trouve le cœur de D3. C'est ce qui rend D3 incroyablement puissant pour créer des visualisations.

Si vous voulez lire ce que Mike Bostock (le créateur de D3) a à dire sur les jointures de données, vous pouvez trouver cela [ici](https://bost.ocks.org/mike/join/).

Ce qui suit est ma tentative d'expliquer ce que fait la fonction `.join` dans le contexte d'un graphique à barres.

Donc, si vous revenez en arrière et regardez les données que nous avons définies plus tôt dans ce post, vous remarquerez que c'est un tableau. La raison est que c'est la structure de données que D3 attend.

La fonction `.join` prend ensuite chaque élément du tableau et **construit un élément DOM correspondant avec ce point de données attaché**.

_Note : La fonction `_.join` utilisée auparavant était des fonctions séparées appelées `_.enter` et `_.append`. Cependant, cette syntaxe est beaucoup plus propre._ [_Voici_](https://github.com/d3/d3-selection/issues/194) _l'issue GitHub où Mike Bostock l'a d'abord suggéré._

![Image](https://cdn-media-1.freecodecamp.org/images/0*9Agl9_MBX5kNT8Dm.jpg)
_Comment .join() fonctionne visuellement_

_Note : Dans le graphique ci-dessus, il devrait être lu `_.join('rect')` et non `_.join('bar')`_

Le graphique ci-dessus illustre ce qui se passe lorsque vous effectuez une jointure de données. Si vous prenez un tableau de 5 éléments et effectuez un `.join('rect')` dessus, ce que D3 fera est de créer un élément SVG rect pour chacun de ces éléments.

Une autre chose que D3 fera est d'associer chaque point de données de votre tableau à son élément `rect` respectif.

```
const data = [1, 2, 3, 4, 5]

const selection = d3.selectAll('rect')
                    .data(data)
                    .join('rect')

selection.each(function(d, i) {
  console.log(d)
})

//1, 2, 3, 4, 5
```

Le code ci-dessus vous montre comment faire le journal de chaque point de données individuel pour satisfaire votre propre curiosité.

Vous pourriez, bien sûr, remplacer le `rect` ci-dessus par n'importe quel autre élément SVG et vous auriez le même résultat.

Bien, maintenant nous savons comment créer nos barres mais nous devons encore déterminer comment les placer. Avant de continuer, je vous recommande de lire [cet article MDN](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect) sur les rects.

Une chose qui m'a beaucoup troublé au début avec D3 était d'essayer de comprendre comment fonctionne le système de coordonnées SVG.

![Image](https://cdn-media-1.freecodecamp.org/images/0*643mFxRq-pIzDknQ.jpg)

_Si vous voulez une compréhension plus approfondie de comment fonctionnent les systèmes de coordonnées SVG, consultez_ [_cet_](https://www.sarasoueidan.com/blog/svg-coordinate-systems/) _article_

Le graphique ci-dessus vous montre comment différentes mesures affecteraient le placement d'un rect dans l'espace de coordonnées SVG.

Un élément SVG rect a quatre attributs principaux qui nous concernent : x, y, width et height.

Vous pouvez voir comment chacun d'eux se rapporte à l'espace de coordonnées SVG dans l'image.

Traduisons ce qui précède en code.

```
chart
  .selectAll("rect")
  .data(data)
  .join("rect")
  .attr("x", d => return x(d.category))
  .attr("y", d => return y(d.value))
  .attr("width", x.bandwidth())
  .attr("height", d => height - y(d.value))
  .style("fill", "steelblue");
```

Passons en revue les parties du code après l'appel `.join`.

Lorsque nous définissons les attributs `x` et `y`, nous faisons un appel aux échelles respectives que nous avons définies précédemment. Rappelez-vous lorsque nous avons défini les échelles, nous avons dit que chacune d'elles serait des fonctions qui pourraient être appelées avec une valeur pour la mapper du domaine à la plage. C'est précisément ce que nous faisons ici.

Maintenant, pour comprendre l'attribut width, nous devons d'abord revenir à l'`ordinalScale` que nous avons défini. D3 a une fonction associée à chaque échelle appelée la fonction `bandwidth`. Cela retourne la largeur de chaque bande définie. D3 fait cela en interne en divisant la plage également entre chaque élément du domaine.

Donc, nous avons fourni un tableau de 5 caractères comme domaine de l'axe x et nous avons défini la plage sur `[margin.left, width - margin.right]`, où `width = 800` et `margin = { left: 60, right: 60 }`

Donc, nous avons

```
(800 - 60 - 60) / 5 = 136
Toutes les unités sont en pixels.
```

Maintenant, l'attribut height est une autre chose qui m'a troublé pendant longtemps parce que je ne pouvais pas tout à fait comprendre pourquoi nous faisions `height - y(d.value)` pour représenter la hauteur du rect. Sûrement, cela aurait dû être simplement `y(d.value)` ?

Cela est à nouveau expliqué en se rappelant que le système de coordonnées SVG a son point d'origine dans le coin supérieur gauche et que l'axe Y +ve va vers le bas.

![Image](https://cdn-media-1.freecodecamp.org/images/0*bgKCtRR14RyZTBOI.jpg)
_Mesures pour une barre dans le système de coordonnées SVG_

Dans le graphique ci-dessus, j'ai présenté ma compréhension de la manière dont la hauteur de la barre est calculée. Encore une fois, si le calcul de la hauteur de la barre a du sens pour vous de manière intuitive, n'hésitez pas à sauter cela.

La chose principale à remarquer dans le visuel est qu'il y a une différence entre les axes du système de coordonnées SVG et les axes de notre graphique. L'axe Y pour le système de coordonnées SVG est positif vers le bas mais l'axe Y pour notre graphique est positif vers le haut.

C'est la raison pour laquelle j'ai dessiné deux ensembles séparés d'axes pour X et Y. Techniquement, les deux axes Y devraient être superposés l'un sur l'autre mais cela rendrait difficile de le voir visuellement. Mais vous pouvez supposer qu'ils sont superposés l'un sur l'autre.

Lorsque nous appelons la fonction d'échelle y avec `y(d.value)`, nous obtenons une valeur qui _décroît_ le long de l'axe Y +ve du système de coordonnées SVG en partant du haut. La hauteur est indiquée sur le côté, qui est la longueur totale de l'axe Y, puis ce qui reste est `height - y(d.value)`, qui est la hauteur que nous attribuons à la barre.

### Ajout de titres et d'étiquettes

Maintenant, nous arrivons à la partie facile. C'est seulement facile grâce à tout ce que nous avons couvert jusqu'à présent !

De manière similaire à la façon dont nous avons ajouté des `rects` à notre SVG jusqu'à présent, nous pouvons également ajouter du `text` comme un élément SVG comme ci-dessous :

```
chart.append('text')
      .attr('x', width / 2)
      .attr('y', margin.top)
      .style('font-size', 32px)
      .style('text-anchor', 'middle')
      .text('Distribution Among Categories')
```

L'élément text SVG a également un attribut `x` et `y` qui fonctionnent de manière très similaire à la façon dont les attributs `x` et `y` du `rect` fonctionnent.

Vous pouvez définir différents attributs de style pour l'élément text et vous définissez le texte lui-même en utilisant l'attribut `.text`.

Maintenant, plaçons l'étiquette de l'axe Y

```
chart
  .append("text")
  .attr("transform", "rotate(-90)")
  .attr("x", -height / 2)
  .attr("y", margin.left / 4)
  .text("Values")
```

D'accord, celui-ci est un peu déroutant, alors passons-le en revue.

Tout d'abord, nous appliquons une `transform` à l'élément et définissons cette valeur à `rotate(-90)`. Ce que cela fait est de faire tourner _le système de coordonnées SVG lui-même_ de -90 degrés.

_Note : Tout ce qui suit est ma tentative de reverse engineering de la façon dont la fonction rotate fonctionne. Si je me trompe, veuillez m'excuser._

![Image](https://cdn-media-1.freecodecamp.org/images/0*Om8G45AlhzM7Nxw6.jpg)
_Rotation de l'axe_

Le graphique ci-dessus montre ce qui arrive au système de coordonnées lors de l'application de `rotate(-90)`. Maintenant, vous êtes probablement encore plus confus parce qu'une rotation négative signifie généralement une rotation dans le sens des aiguilles d'une montre. Pourtant, il semble que j'ai tourné dans le sens inverse des aiguilles d'une montre ici.

Eh bien, rappelez-vous qu'un système de coordonnées typique a l'axe Y pointant positivement vers le haut. Nous l'avons pointant positivement vers le bas. Par conséquent, nos rotations sont inversées.

Maintenant, notre nouvel axe X pointe dans la direction opposée de l'ancien axe Y et notre nouvel axe Y pointe dans la direction de l'ancien axe X.

Maintenant, dans le contexte de cette nouvelle information, regarder les valeurs des attributs `x` et `y` a plus de sens. Puisque notre nouvel X pointe à l'opposé de la direction de l'ancien Y, nous définissons une valeur négative pour l'attribut `x`.

### Conclusion

D'accord, c'était un article assez long. Je ne m'attendais pas à ce qu'il devienne aussi massif, mais nous avons couvert beaucoup de choses en détail. J'espère que vous avez apprécié parcourir cet article et plus que tout, j'espère que vous avez une meilleure compréhension de comment fonctionne D3. C'est une bibliothèque vraiment merveilleuse qui vous fournit un ensemble d'outils très puissants.

J'ai créé un [Code Sandbox ici](https://codesandbox.io/s/blazing-pine-9vjw1) avec une version fonctionnelle du code de cet article. N'hésitez pas à le forker et à jouer avec !

---

_Si vous voulez me suivre, vous pouvez le faire sur_ [_GitHub_](https://github.com/) _ou_ [_Twitter_](https://twitter.com/zz_humayun)_. Si vous avez des questions, n'hésitez pas à demander._