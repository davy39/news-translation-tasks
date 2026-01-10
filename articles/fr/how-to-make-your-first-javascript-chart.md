---
title: Comment créer votre premier graphique JavaScript avec JSCharting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T14:45:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-first-javascript-chart
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/first-javascript-chart-using-csv-jscharting-fit.jpg
tags:
- name: charts
  slug: charts
- name: JavaScript
  slug: javascript
seo_title: Comment créer votre premier graphique JavaScript avec JSCharting
seo_desc: 'By Arthur Puszynski

  When you''re starting out as a beginner JavaScript developer, I think it is important
  to pursue interesting projects. That way you can make sure you have fun as you learn,
  and you''ll likely find an area of specialization that you e...'
---

Par Arthur Puszynski

Lorsque vous débutez en tant que développeur JavaScript débutant, je pense qu'il est important de poursuivre des projets intéressants. Ainsi, vous pouvez vous assurer de vous amuser tout en apprenant, et vous trouverez probablement un domaine de spécialisation qui vous passionne. 

Comme on dit, _"Si vous aimez ce que vous faites, vous ne travaillerez jamais de votre vie"_. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/not-suited-for-work.gif)
_Source : giphy.com_

Dans cet article, je vais vous initier à la visualisation de données front-end, qui est ma passion personnelle. Peut-être deviendra-t-elle également votre passion !

Les moments les plus gratifiants pour moi en tant que développeur sont ceux où je peux voir ou expérimenter les résultats de ce que j'ai créé. Il est très satisfaisant de créer un graphique qui révèle des informations intéressantes sur ses données, ou une expérience interactive qui aide à explorer les détails d'un ensemble de données unique. Plus le résultat est significatif, plus la récompense est grande. 

Cependant, j'ai réalisé que la quantité de travail que vous mettez dans un projet ne correspond pas nécessairement au sentiment d'accomplissement – parfois, cela semble génial même si c'était relativement facile. 

Avec le temps, vous trouverez des outils qui vous aideront à être plus efficace, et parfois vous déplacerez des montagnes avec peu d'effort. Il existe de nombreuses bibliothèques et outils de graphiques disponibles dans le domaine de la visualisation de données. Avec les bons outils, vous créerez de nouveaux graphiques avec peu d'effort, quel que soit le type de graphique dont vous avez besoin. Personnellement, je pense que la visualisation de données offre une grande récompense pour votre investissement en temps et en effort.

Dans ce tutoriel, vous utiliserez un certain nombre d'outils pour obtenir des données sur Internet, les traiter et dessiner un beau graphique qui peut être visualisé dans n'importe quel navigateur moderne. Vous pouvez cliquer sur les liens ci-dessous pour télécharger le code exemple pour chaque étape individuellement, les voir tous sur **[GitHub](https://github.com/arthurPuszynski/first-chart-article)**, ou télécharger toutes les étapes à la fois ici : **[all-steps.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/all-steps.zip).**

## Le Résultat

À la fin de ce tutoriel, vous aurez créé ce graphique interactif basé sur des données. Vous apprendrez à obtenir des données sur Internet, à les traiter et à créer un graphique avec ces données. Vous serez également capable de créer vos propres graphiques à partir de zéro.

![Graphique en ligne JavaScript interactif](https://www.freecodecamp.org/news/content/images/2019/12/javascript-line-chart.png)
_Graphique en ligne JavaScript interactif_

Après avoir traité les données et les avoir représentées sous forme de graphique, vous apprendrez également à apporter des ajustements au graphique, y compris la modification de la légende par défaut, l'activation des lignes de référence de l'axe x avec des infobulles, et l'application d'annotations textuelles pour ajouter du contexte et d'autres informations au graphique.

## Les Outils

Pour commencer, utilisez un navigateur Internet comme celui que vous utilisez probablement pour lire cet article. Je recommande Chrome car il offre une grande expérience et des outils intégrés pour les développeurs.

Ensuite, vous aurez besoin d'un éditeur de texte. Quelque chose d'aussi simple que le bloc-notes fera l'affaire. Mais je suggère d'utiliser un éditeur de code plus avancé comme VS Code, car c'est un environnement dans lequel vous passerez beaucoup de temps. Il vous offrira une expérience de codage plus pratique et agréable, et facilitera l'écriture de HTML5, CSS et JavaScript. Le plus important, si vous oubliez une guillemet ou une virgule quelque part, un éditeur de code peut vous aider à trouver l'erreur.

Cet article peut vous aider à [choisir le meilleur éditeur de code JavaScript pour le développement web](https://www.freecodecamp.org/news/how-to-choose-a-javascript-code-editor/).

Vous utiliserez la bibliothèque de graphiques JSCharting pour dessiner automatiquement et ajouter une fonctionnalité interactive à ce graphique. Aucune autre bibliothèque JavaScript telle que jQuery, ou plateforme front-end incluant React et Angular (communément utilisées pour les projets de sites web) ne sera requise.

### Pourquoi JSCharting ?

[JSCharting](https://jscharting.com/) est une bibliothèque de graphiques JavaScript qui peut dessiner de nombreux types de graphiques différents en utilisant SVG. Elle est facile à utiliser et à démarrer, ce qui en fait un bon choix pour ce tutoriel. L'API (Application Programming Interface, c'est-à-dire les options et paramètres nécessaires pour créer des graphiques) simplifie les choses difficiles et c'est une bonne option lorsque vous expérimentez avec des visualisations de données. 

Vous pouvez utiliser JSCharting gratuitement pour un usage personnel et commercial avec le branding inclus.

Vous pouvez créer des graphiques réactifs avec JSCharting en suivant quelques étapes simples :

- Définir une balise `<div>` dans le fichier HTML avec un id unique.
- Fournir cet id, les données, et toute autre option lors de l'appel de `JSC.Chart()` dans le fichier JavaScript.

C'est tout. JSC dessinera un graphique professionnel en remplissant cette balise div avec des éléments visuels SVG. Le graphique sera réactif et interactif sans aucun effort supplémentaire.

## Les Données

Vous utiliserez un fichier de données fourni par le NCHS (National Center for Health Statistics) listant l'espérance de vie historique des hommes et des femmes aux États-Unis.

Vous pouvez le trouver ici : [https://data.cdc.gov/resource/w9j2-ggv5.csv](https://data.cdc.gov/resource/w9j2-ggv5.csv). 

Ce fichier CSV contient des données qui classent les espérances de vie par année, race et sexe. Vous utiliserez certaines de ces données pour dessiner une simple ligne de tendance homme/femme sur les 100 dernières années.

Le format CSV (Comma Separated Values) est idéal pour transmettre des données sur Internet. Il est compact, lisible par l'homme et vous pouvez l'ouvrir directement dans Excel, ce qui est également pratique.

Alors sans plus attendre, commençons.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/readycat.gif)
_Source : giphy.com_

## Étape 1 - Ajouter un graphique vide

Le premier fichier zip contient un point de départ vide que vous pouvez remplir au fur et à mesure. Si vous êtes perdu ou confus, ou si vous souhaitez passer à l'étape suivante, le fichier zip à la fin ou tout au long de chaque section vous mettra à jour.  

Si vous souhaitez télécharger tous les fichiers à la fois, voir **[all-steps.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/all-steps.zip)** à la place._

### [step1-a.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step1-a.zip)

Ce fichier zip contient les fichiers suivants.
- `index.html`
- `js/index.js`

Le fichier `.html` est vide à l'exception de quelques codes standard qui en font un fichier valide et le fichier `.js` est complètement vide.

La première étape consiste à ajouter quelques scripts au fichier de page web HTML. Normalement, les gens suggèrent d'ajouter des balises `<script>` à l'intérieur des balises `<head>`. Cependant, pour les scripts qui affectent le contenu HTML, il est souvent préférable de les ajouter après la balise de fermeture `</body>`. 

Cette technique charge tout le HTML dans le DOM avant d'exécuter un quelconque JavaScript. Le graphique a besoin que le HTML soit chargé avant de pouvoir y dessiner. Le DOM (Document Object Model) est une représentation de votre code HTML dans la mémoire du navigateur. Une fois que le HTML est chargé dans le DOM, le navigateur peut l'afficher et JavaScript peut interagir avec lui.

Commencez par ajouter la bibliothèque JSCharting au fichier HTML. Ouvrez le fichier `index.html` dans l'éditeur de votre choix. Ensuite, ajoutez une balise de script pour inclure JSCharting après la balise de fermeture `</body>`. Le code résultant en bas du fichier devrait ressembler à ceci :

```html
</body>
<script src="https://code.jscharting.com/2.9.0/jscharting.js"></script>
</html>
```

Cette URL de bibliothèque pointe vers un CDN (Content Delivery Network). Il héberge le code du graphique et le rend pratique pour ajouter rapidement la bibliothèque à n'importe quelle page HTML pour prototyper des graphiques et expérimenter. Vous pouvez également [télécharger](https://jscharting.com/download/) et utiliser la bibliothèque localement ou utiliser le package npm dans votre projet, mais le CDN ne nécessite aucune étape supplémentaire.

Ensuite, en utilisant la même technique, ajoutez une autre balise de script référençant votre fichier JavaScript vide. Ajoutez ce script après le script `jscharting.js` pour qu'il ressemble à ceci :

```html
</body>
<script src="https://code.jscharting.com/2.9.0/jscharting.js"></script>
<script src="js/index.js"></script>
</html>
```

Super. Nous sommes presque prêts à dessiner un graphique vide. La dernière chose que vous devez faire est d'ajouter un espace réservé `<div>` à l'intérieur du fichier HTML pour définir où nous voulons que ce graphique soit dessiné.

Ajoutez ce code HTML à l'intérieur des balises `<body>`.

```html
<body>
    <div id="chartDiv" style="width:50%; height:300px; margin:0 auto;"></div>
</body>
```

La div doit avoir un id pour que vous puissiez indiquer au graphique dans quelle div dessiner. Dans ce cas, l'id est `chartDiv`. 

Vous avez peut-être remarqué l'attribut de style de la balise `<div>`. Il fait en sorte que la div occupe 50 % de la largeur de la fenêtre et 300 pixels de haut. Le style de marge `margin:0 auto;` centre la div sur la page. Le graphique remplira la taille de la div, donc changer la taille de la div est un bon moyen de contrôler la taille du graphique.

Vous avez terminé avec le fichier HTML. Ouvrez le fichier `index.js` et ajoutez un graphique vide à cette page en écrivant le code suivant qui inclut l'id de la div `chartDiv` :

```javascript
JSC.Chart('chartDiv', {});
```

Ouvrez le fichier `index.html` dans un navigateur (glissez-déposez le fichier dans un navigateur web comme Chrome).

Il n'y a pas grand-chose à voir pour l'instant, mais vous avez peut-être remarqué un petit logo JSC sur cette page. Cela indique qu'un graphique est connecté et en cours de dessin.

![Le logo JSCharting montre que le graphique fonctionne](https://www.freecodecamp.org/news/content/images/2019/12/jscharting-brand.png)
_Le logo JSCharting montre que le graphique fonctionne_

**[step1-b.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step1-b.zip)**

## Étape 2 - Jouer un peu avec le graphique

D'accord, en guise de test, ajoutons quelques valeurs pour que le graphique les visualise afin de voir comment cela fonctionne.

En revenant au fichier `index.js`, remplacez le contenu par le code suivant qui ajoute plus d'options au graphique.

```javascript
JSC.Chart('chartDiv', {
   type: 'horizontal column',
   series: [
      {
         points: [
            {x: 'Apples', y: 50},
            {x: 'Oranges', y: 42}
         ]
      }
   ]
});
```

Maintenant, actualisez (F5) la fenêtre du navigateur où la page `index.html` est chargée.

![Graphique à colonnes horizontales avec une série et deux points](https://www.freecodecamp.org/news/content/images/2019/12/horizontal-column-chart.png)
_Graphique à colonnes horizontales avec une série et deux points_

Bien joué ! Vous venez de créer votre premier graphique en utilisant JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/yeah-1.gif)
_Source : giphy.com_

Vous avez créé un graphique à barres en définissant le type de graphique sur `'horizontal column'`. Si vous préférez une colonne verticale, définissez la valeur sur `'column'`. Vous avez également ajouté une série avec deux points au graphique pour les pommes et les oranges.

Toutes les données de graphique sont composées de séries et de points. Une série est simplement un groupe de points de données. Les graphiques peuvent contenir une ou plusieurs séries de données. Les points de données consistent en des valeurs qui se mapent aux axes x et y. Les points peuvent également inclure de nombreuses autres variables et valeurs descriptives.

L'exemple ci-dessus ne contient qu'une seule série. Maintenant, regardons les options pour un graphique avec deux séries. Remplacez le contenu du fichier JavaScript par ce code.

```javascript
JSC.Chart('chartDiv', {
   type: 'horizontal column',
   series: [
      {
         name:'Andy',
         points: [
            {x: 'Apples', y: 50},
            {x: 'Oranges', y: 32}
         ]
      },{
         name:'Anna',
         points: [
            {x: 'Apples', y: 30},
            {x: 'Oranges', y: 22}
         ]
      }
   ]
});
```

L'actualisation de la fenêtre du navigateur affichera ce graphique.

![Graphique à colonnes horizontales avec deux séries](https://www.freecodecamp.org/news/content/images/2019/12/horizontal-column-cluster.png)
_Graphique à colonnes horizontales avec deux séries_

Les options du graphique semblent similaires. Toujours un graphique à barres, mais cette fois il y a un objet supplémentaire dans le tableau des séries. Nous avons également ajouté des propriétés de nom pour chaque série afin que le graphique puisse les identifier dans la légende.

Si vous êtes intéressé par la création de différents graphiques comme des graphiques radar, des graphiques en aire, des graphiques en camembert, des graphiques de Gantt, ou même des graphiques de calendrier en carte thermique, consultez la [galerie d'exemples de JSCharting](https://jscharting.com/examples/chart-types/) et le code source (options de graphique) utilisé pour créer ces graphiques. Vous pouvez rapidement apprendre à utiliser d'autres fonctionnalités de graphique en copiant les exemples disponibles.

**[step2.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step2.zip)**

## Étape 3 - Préparer les données

![Image](https://www.freecodecamp.org/news/content/images/2019/12/data.gif)
_Source : giphy.com_

Le format de données CSV est exactement cela – des valeurs séparées par des virgules. Le fichier contient des lignes (lignes) et chaque ligne représente un enregistrement ou une entrée. Normalement, la première ligne de valeurs contient les noms de chaque valeur séparée par des virgules (colonne). Les lignes suivantes contiennent les valeurs elles-mêmes. 

```
name,age
chris,26
mike,34
```

Le CSV est lisible par l'homme, mais il existe des variations de ce format. Parfois, si les valeurs contiennent des virgules (par exemple, les adresses postales), le format ne fonctionne pas tel quel, donc chaque valeur est également entourée de guillemets. Ainsi, les virgules à l'intérieur des guillemets sont ignorées et le format peut toujours fonctionner en utilisant uniquement les virgules à l'extérieur des guillemets pour séparer les valeurs. 

```
"name","age","parents"
"Chris","26","Gregory, Mary"
"Mike","34","David, Sarah"
```

Les valeurs peuvent également être séparées en utilisant un caractère différent comme des tabulations à la place des virgules.

Mais ne nous attardons pas sur les détails. JSCharting fournit un certain nombre d'outils qui aident dans ce processus et nous utiliserons l'un d'eux pour éviter de nous soucier du format de fichier CSV et le convertir en JSON (JavaScript Object Notation). Le résultat sera un tableau d'objets. Chaque objet représente une ligne avec des propriétés nommées. La première ligne du fichier CSV est utilisée pour définir les noms de ces propriétés.

Voici l'URL des données qui nous intéressent : [https://data.cdc.gov/resource/w9j2-ggv5.csv](https://data.cdc.gov/resource/w9j2-ggv5.csv).

Vous pouvez cliquer pour le télécharger et l'ouvrir dans Excel.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-28.png)
_Fichier CSV ouvert dans Excel_

Cependant, vous allez télécharger et accéder à ces données CSV en temps réel en utilisant du code JavaScript. Le code ci-dessous peut sembler légèrement déroutant au début, mais il est court et vous pouvez le réutiliser pour obtenir n'importe quel fichier CSV, texte ou JSON sur Internet de manière programmatique. Il est similaire à l'ancienne technologie AJAX mais beaucoup plus simple à utiliser.

Une fois de plus, remplacez le contenu du fichier `index.js` par le suivant :

```javascript
fetch('https://data.cdc.gov/resource/w9j2-ggv5.csv')
   .then(function (response) {
      return response.text();
   })
   .then(function (text) {
	csvToSeries(text);
   })
   .catch(function (error) {
      //Quelque chose s'est mal passé
      console.log(error);
   });

function csvToSeries(text) {
   console.log(text);
}
```

Pourquoi est-ce si compliqué ? C'est parce que lorsque vous demandez un fichier, il ne devient pas immédiatement disponible. Il y a un délai et vous devez attendre que le fichier arrive. Donc d'abord vous demandez le fichier à partir d'un autre site web en utilisant `fetch()`.

```javascript
fetch('https://data.cdc.gov/resource/w9j2-ggv5.csv')
```

Ensuite, le code à l'intérieur de la fonction d'argument `then(...)` est appelé avec la réponse lorsqu'elle arrive. Cette fonction convertit la réponse en texte et la retourne, ce qui transmet le résultat à la fonction d'argument `then()` suivante.

```javascript
.then(function (response) {
	return response.text();
})
```

La fonction d'argument `then(...)` suivante appelle la fonction `csvToSeries()`, et transmet le texte comme argument.

```javascript
.then(function (text) {
	csvToSeries(text);
})
```

Dans la fonction `catch()`, vous pouvez spécifier quoi faire si quelque chose ne va pas. Par exemple, peut-être que l'internet est en panne, ou l'URL n'est pas correcte.

```javascript
.catch(function (error) {
	//Quelque chose s'est mal passé
	console.log(error);
});
```

Dans ce cas, l'erreur est envoyée à la console.

Dans la fonction `csvToSeries()`, nous transmettons ce texte à la console pour inspection.

```javascript
function csvToSeries(text) {
   console.log(text);
}
```

? **Note :** La fonction native `fetch()` n'est pas prise en charge dans Internet Explorer 11. Si vous souhaitez également prendre en charge ce navigateur, vous pouvez utiliser la fonction `JSC.fetch()` qui est incluse avec JSCharting. Elle offre la même fonctionnalité, mais ajoute un support supplémentaire pour IE11.

Faites glisser le fichier `index.html` dans une fenêtre de navigateur (ou actualisez la page si elle est déjà ouverte) et appuyez sur F12. Cela ouvrira la fenêtre DevTools du navigateur Chrome. Par défaut, la moitié inférieure de la fenêtre DevTools affichera la sortie de la console. C'est ici que le texte est envoyé lorsque vous exécutez du code comme :

```javascript
console.log(text);
```

![Image](https://lh4.googleusercontent.com/C9pr4DISX6SwVwUdrSUz8s54gIuNgseApHISaR-C0HXkU-8OKaup09xhIeWjn7MvzWraT4uIEYPJU63ZVopGAHSshqxE64a6m8mHQlPiTVZUV0mAh4_p_3vBvSxWnqM0B9Vt3kLP)
_Sortie de la fenêtre de la console_

Vous pouvez également coller ou écrire du code dans cette fenêtre de console pour l'exécuter. Essayez de coller l'intégralité de l'extrait de code ci-dessus dans la fenêtre de la console (à côté du caractère >) et appuyez sur Entrée. Vous remarquerez que vous obtenez le même résultat dans la sortie de la fenêtre de la console. Cela peut être utile pour tester une ligne de code et expérimenter.

**[step3-a.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step3-a.zip)**

À ce stade, vous avez récupéré le texte du fichier CSV sur Internet et l'avez envoyé à la console pour prouver que cela fonctionne. Maintenant, nous pouvons commencer à travailler avec.

Jetons un coup d'œil à ce fichier de données pour avoir une idée de ce qu'il contient : [https://data.cdc.gov/resource/w9j2-ggv5.csv](https://data.cdc.gov/resource/w9j2-ggv5.csv)

J'ai utilisé Excel pour trier les lignes par la colonne année afin d'analyser les lignes de données pour une seule année. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-27.png)
_Les données CSV triées par année._

Chaque année contient 9 lignes avec des données basées sur la race et le sexe. Nous ne sommes intéressés que par les valeurs mâles et femelles mises en évidence de toutes les races pour chaque année. Vous allez créer deux séries basées sur les lignes mises en évidence. Une série pour les femmes et une pour les valeurs masculines. 

Maintenant que vous avez une idée de ce qui doit se passer, commençons.

Tout d'abord, utilisons la fonction `JSC.csv2Json()` pour convertir le texte au format JSON et le transmettre à la console pour voir ce qu'il fait. 

Mettez à jour la fonction `csvToSeries()` avec le code suivant :


```javascript
function csvToSeries(text) {
   let dataAsJson = JSC.csv2Json(text);
   console.log(dataAsJson)
}
```

Actualisez le navigateur pour voir la sortie de la console mise à jour.   


![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-29.png)
_Données CSV converties en JSON en utilisant la fonction utilitaire JSC.csv2Json()_

La console montre un tableau de 1062 enregistrements. Et voici l'un de ces enregistrements :

```json
{year: 1900, race: "All Races", sex: "Both Sexes", average_life_expectancy: 47.3, mortality: 2518}
```

? **Note :** La console peut afficher des tableaux et des objets pour inspection et vous pouvez développer et réduire des sections dans la console pour explorer les détails.

Le nom de la propriété `average_life_expectancy` est un peu long, mais vous devrez l'utiliser. Pour éviter de le taper plus d'une fois, définissez une variable constante pour stocker ce nom. Lorsque vous devez utiliser cette propriété, vous pouvez simplement écrire le nom de la variable `lifeExp`. Cela ressemblera à ceci `row[lifeExp]` au lieu de `row.average_life_expectancy`.

Ajoutez cette ligne en haut de la fonction `csvToSeries()`.

```javascript
function csvToSeries(text) {
	const lifeExp = 'average_life_expectancy';
	...
```

Vous pouvez traiter ces données en utilisant du JavaScript vanilla simple. Le résultat final que nous voulons est deux séries avec des points de données qui incluent une année et une espérance de vie pour chaque point.

Mettez à jour `csvToSeries()` avec le code suivant :


```javascript
function csvToSeries(text) {
	const lifeExp = 'average_life_expectancy';
	let dataAsJson = JSC.csv2Json(text);
	let male = [], female = [];
	dataAsJson.forEach(function (row) {
		 //ajoutez soit à male, female, ou jetez.
		console.log(row);
	});
}
```

Il définit des tableaux pour les points de données masculins et féminins. Ensuite, il appelle la fonction `dataAsJson.forEach()` en passant une fonction de rappel `function(row){...}` comme argument. La fonction `forEach()` exécutera la fonction de rappel pour chaque élément du tableau `dataAsJson`. Pour l'instant, nous allons simplement appeler `console.log(row)` sur chaque ligne que la fonction de rappel rencontre.

Actualisez le navigateur et inspectez la sortie de la console. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-30.png)
_Chaque objet de ligne que la fonction de rappel a rencontré_

Ajoutons une logique pour filtrer les données que nous voulons et enregistrer le résultat dans la fenêtre de la console. Remplacez la fonction `csvToSeries()` par ce code.


```javascript
function csvToSeries(text) {
	const lifeExp = 'average_life_expectancy';
	let dataAsJson = JSC.csv2Json(text);
	let male = [], female = [];
	dataAsJson.forEach(function (row) {
		 //ajoutez soit à male, female, ou jetez.
		if (row.race === 'All Races') {
			if (row.sex === 'Male') {
				male.push({x: row.year, y: row[lifeExp]});
			} else if (row.sex === 'Female') {
				female.push({x: row.year, y: row[lifeExp]});
			}
		}
	});
    console.log([male, female]);
}
```

À l'intérieur de la fonction de rappel, vous décidez si la ligne est d'intérêt et l'utilisez ou si ce n'est pas le cas, vous la jetez. 

```javascript
if (row.race === 'All Races') {
	if (row.sex === 'Male') {
		//ajoutez les données au tableau male
		male.push({x: row.year, y: row[lifeExp]});
	} else if (row.sex === 'Female') {
		//ajoutez les données au tableau female
		female.push({x: row.year, y: row[lifeExp]});
	}
}
```

La logique vérifie si la valeur `row.race` est égale à 'All Races'. Si c'est le cas, elle vérifie ensuite si la propriété `row.sex` est égale à 'Male' ou 'Female'. Si la ligne est égale à l'une ou l'autre, elle ajoute les données soit au tableau `male` soit au tableau `female` en tant qu'objet de point `{x, y}`. Remarquez l'utilisation de la variable `lifeExp` définie ci-dessus qui aide à raccourcir ce code.


À la fin, vous avez utilisé `console.log([male, female])` pour transmettre les variables male et female à la console pour inspection et pour vous assurer que votre code fonctionne comme prévu.

Après avoir actualisé le navigateur, la console montre le résultat qui est deux tableaux, chacun avec 118 points de données couvrant les années 1900 à 2017.

![Image](https://lh6.googleusercontent.com/V3yi_ZyqpoOMvn8jr1Tb31obS1WPHbgJ8p1LkPirFMLu8rjmzUs5-CgVCvtsLLnXscGO7HxR8_IM02_Q1twFPRNa1ll5JCCOoQbuK_S0hxqA7IZNoAqskksO62nXXRoSedjwUmzg)
_Les tableaux de points masculins et féminins_

Enfin, au lieu de transmettre le résultat à la console, enveloppez ces points de données dans un tableau de deux séries que le graphique peut utiliser directement et retournez-les.

Ajoutez ce code à la fin de la fonction `csvToSeries()` :


```javascript
return [
   {name: 'Male', points: male},
   {name: 'Female', points: female}
];
```

Si la valeur retournée était envoyée à la console, elle produirait ce résultat.  


![Image](https://lh6.googleusercontent.com/_xlnsylk8kbv1u9-Fw4K0dnmJ7J_UBzhbhrWT8j48S4xtr04gYezHIITd_cNWQ5ZvJvi4MPdqi_IIat-JSfmRiOZT7jDzco5JYSstOzec67OxAQ-LCB7zuyqm20gxV8FYEm1XL0d)
_Deux objets de séries que le graphique peut consommer directement_

Comme vous pouvez le voir, la logique de filtrage des lignes est assez simple et vous pouvez l'ajuster pour obtenir d'autres détails à partir de cet ensemble de données. 

Pour en savoir plus sur la gestion des fichiers CSV en utilisant les utilitaires JSCharting, consultez ce [tutoriel](https://jscharting.com/tutorials/js-chart-data/client-side/fetch-csv-and-json/). Lorsque vous êtes prêt pour une gestion de données plus avancée, l'[utilitaire JSC.nest()](https://jscharting.com/tutorials/js-chart-data/client-side/data-nesting/) peut être utilisé pour créer des séries et des points à partir de données JSON avec très peu de code. 

[**step3-b.zip**](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step3-b.zip)

## Étape 4 - Mettre le tout ensemble

La section de gestion des données était l'étape la plus difficile, mais cela seul vous permettra de manipuler et d'extraire des données d'intérêt de n'importe quel fichier CSV. C'est là que tout se met en place et où vous ressentirez un sentiment d'accomplissement. 

Commencez par ajouter une fonction `renderChart()` à la fin du fichier `index.js`. Vous passerez les données de la série à cette fonction en tant qu'argument. 


```javascript
function renderChart(series){
   JSC.Chart('chartDiv', {
      series: series
   });
}
```

Dans la fonction d'argument `then()` qui appelle `csvToSeries()`, passez le résultat de la série à la fonction `renderChart()` pour voir ce qu'elle dessine dans le navigateur.

```javascript
.then(function (text) {
	let series = csvToSeries(text);
	renderChart(series);
})
```

**[step4-a.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step4-a.zip)**

Maintenant, actualisez le navigateur. Vous devriez voir ce graphique qui utilise les données CSV que vous avez traitées dans la section précédente. Sweet! 😊

![Graphique en ligne montrant les données CSV filtrées](https://www.freecodecamp.org/news/content/images/2019/12/csv-line-chart.png)
_Graphique en ligne montrant les données CSV filtrées_

Qu'est-ce qui s'est passé en 1918 ? L'espérance de vie a considérablement chuté cette année-là. Selon Wikipedia, il y a eu une [pandémie de grippe](https://en.wikipedia.org/wiki/Spanish_flu) impliquant le virus H1N1 qui a décimé une partie de la population mondiale. Cet événement malheureux montre comment la visualisation des données fournit des informations que vous n'obtiendriez pas normalement en regardant simplement les chiffres.

Vous avez créé un graphique en utilisant le type de série de lignes par défaut et il a l'air bien, mais vous pouvez apporter quelques ajustements et améliorations pour le rendre encore meilleur.

Tout d'abord, ajoutez un titre en haut pour expliquer ce que le spectateur regarde et une annotation en bas du graphique pour créditer la source des données. Mettez à jour la fonction constructeur `JSC.Chart()` pour passer les options suivantes :


```javascript
function renderChart(series){
	JSC.Chart('chartDiv', {
		title_label_text: "Espérance de vie aux États-Unis",
		annotations: [{
			label_text: "Source : National Center for Health Statistics",
			position: 'bottom left'
		}],
		series: series
	});
}

```

Lorsque vous actualisez le navigateur, vous pouvez voir le graphique mis à jour.

![Graphique en ligne avec titre et annotation pour l'attribution](https://www.freecodecamp.org/news/content/images/2019/12/line-chart-annotations.png)
_Graphique en ligne avec titre et annotation pour l'attribution_

Vous avez ajouté une annotation avec un texte de label et un paramètre de position. Nous pouvons également utiliser une autre annotation pour le titre, mais il était plus facile d'utiliser le label de titre dans cet exemple. 

Il est facile de contrôler la position de l'annotation en utilisant des valeurs telles que `'top right'` ou `'inside bottom right'`. La valeur `'inside'` signifie que l'annotation est placée à l'intérieur de la zone du graphique où les données sont dessinées. Cet [exemple de positions de boîte de graphique](https://jscharting.com/examples/chart-features/annotation/box-positions/) démontre toutes les options de paramétrage de position.

La légende montre la somme des valeurs des points pour chaque série, mais la somme n'est pas importante pour cet ensemble de données. Vous pouvez réduire les colonnes de la légende pour n'afficher que l'icône et le nom de la série en utilisant ce paramètre :

```javascript
legend_template: '%icon,%name'
```

Mais vous n'avez pas vraiment besoin d'utiliser une légende du tout. Il sera plus propre d'étiqueter simplement les lignes elles-mêmes. Vous pouvez désactiver la légende et dire au graphique d'écrire le nom de la série sur le dernier point de chaque série de lignes avec ces options de graphique :

```javascript
legend_visible: false,
defaultSeries_lastPoint_label_text: '<b>%seriesName</b>',

```

![Graphique en ligne utilisant des étiquettes de points au lieu d'une légende](https://www.freecodecamp.org/news/content/images/2019/12/csv-line-chart-labels.png)
_Graphique en ligne utilisant des étiquettes de points au lieu d'une légende_

Le jeton `'%seriesname'` est l'un des nombreux [jetons liés aux points](https://jscharting.com/tutorials/js-chart-labels/token-reference/#point-tokens) qui peuvent être utilisés dans n'importe quel texte d'étiquette de point pour afficher les détails et les calculs des points. 

Enfin, activons l'infobulle combinée de la ligne de référence de l'axe x pour afficher l'espérance de vie masculine et féminine pour une année donnée. Sur les appareils mobiles, vous pouvez appuyer sur le graphique pour voir l'infobulle de la ligne de référence. Lorsque vous utilisez un PC, les infobulles s'affichent lorsque vous survolez le graphique avec le pointeur de la souris.

```javascript
xAxis_crosshair_enabled: true,
```

Vous vous demandez peut-être, pourquoi tous ces traits de soulignement dans les noms de propriétés ? Ce n'est pas le nom réel de la propriété. C'est une manière abrégée d'écrire :

```javascript
xAxis: {crosshair: {enabled: true}},
```

Vous pouvez trouver plus pratique de spécifier un paramètre avec des traits de soulignement et JSCharting comprendra ce que vous voulez dire. 


Le texte de l'infobulle par défaut est clair, mais personnalisons-le légèrement pour le rendre unique. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-60.png)
_Infobulle combinée par défaut_

Puisque l'infobulle de la ligne de référence montre des informations sur chaque point qu'elle croise, le texte de l'infobulle est défini dans les options de point. La propriété `defaultPoint` définit les options de point que tous les points hériteront automatiquement.

```javascript
defaultPoint_tooltip: '%seriesName <b>%yValue</b> years',
```

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-61.png)
_Infobulle combinée personnalisée_

Pour plus d'informations sur cette fonctionnalité, consultez le [tutoriel sur la ligne de référence et l'infobulle combinée](https://jscharting.com/tutorials/js-chart-interactivity/crosshair-combined-tooltip/).

Lorsque vous appliquez toutes ces options, votre code ressemblera à l'extrait suivant. Remplacez l'intégralité de la fonction `renderChart()` par ce code.


```javascript
function renderChart(series){
	JSC.Chart('chartDiv', {
		title_label_text: "Espérance de vie aux États-Unis",
		annotations: [{
			label_text: "Source : National Center for Health Statistics",
			position: 'bottom left'
		}],
        legend_visible: false,
		defaultSeries_lastPoint_label_text: '<b>%seriesName</b>',
		defaultPoint_tooltip: '%seriesName <b>%yValue</b> years',
		xAxis_crosshair_enabled: true,
		series: series
	});
}

```

Actualisez une fois de plus la fenêtre du navigateur.

![Graphique en ligne avec des lignes de référence et des infobulles combinées personnalisées](https://www.freecodecamp.org/news/content/images/2019/12/csv-line-chart-tooltips.png)
_Graphique en ligne avec des lignes de référence et des infobulles combinées personnalisées_

Vous l'avez fait ! 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/congratulations.gif)
_Source : giphy.com_

Tout d'abord, vous avez récupéré des données CSV en utilisant du JavaScript natif. Vous les avez ensuite converties au format JSON et filtrées en deux séries. Avec ces séries, vous avez créé un beau graphique en ligne interactif en utilisant JSCharting et l'avez configuré pour qu'il ait l'air professionnel. 

Vous pouvez personnaliser et ajuster davantage les graphiques pour répondre à vos besoins spécifiques. Visitez la section [tutoriels](https://jscharting.com/tutorials/) de JSCharting pour en savoir plus sur un sujet spécifique, ou trouvez des graphiques similaires à ce que vous souhaitez créer dans la [galerie d'exemples](https://jscharting.com/examples/chart-types/) et copiez-les pour continuer votre voyage dans la visualisation de données.

Si vous rencontrez des problèmes avec JSCharting, n'hésitez pas à [contacter](https://jscharting.com/support.htm) l'équipe de support. Ils seront heureux de vous guider ou de vous aider à résoudre tout problème que vous pourriez rencontrer.

**[step4-b.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step4-b.zip)**

## Défi Bonus

Nous n'avons pas utilisé toutes les données disponibles dans ce fichier CSV. Expérimentons avec pour le plaisir et la pratique.

Créez ce graphique en utilisant ce que vous avez appris.

![Défi : Répliquez ce graphique par vous-même](https://www.freecodecamp.org/news/content/images/2019/12/bonus-trend-line-chart.png)
_Défi : Répliquez ce graphique par vous-même_

Ce fichier zip contient la réponse :

**[step5-bonus.zip](https://github.com/arthurPuszynski/first-chart-article/raw/master/zips/step5-bonus.zip)**

Pouvez-vous penser à d'autres graphiques que vous pouvez créer avec ces données ? Continuez à expérimenter et profitez de chaque minute !