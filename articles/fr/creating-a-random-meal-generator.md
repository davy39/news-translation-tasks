---
title: Comment créer un générateur de repas aléatoires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-22T22:00:00.000Z'
originalURL: https://freecodecamp.org/news/creating-a-random-meal-generator
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/random-meal-generator-1.png
tags:
- name: 100Days100Projects
  slug: 100days100projects
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment créer un générateur de repas aléatoires
seo_desc: 'By Florin Pop

  Last week I decided to take on a new challenge. I called it: The #100Days100Projects
  Challenge.

  The purpose of the challenge is to create one project every single day. Think of
  it as a next step for the #100DaysOfCode challenge.

  A proje...'
---

Par Florin Pop

La semaine dernière, j'ai décidé de relever un nouveau défi. Je l'ai appelé : le défi [#100Days100Projects](https://www.florin-pop.com/blog/2019/09/100-days-100-projects).

Le but du défi est de créer un projet chaque jour. Considérez cela comme une étape suivante pour le défi #100DaysOfCode.

Un projet peut être soit :
- une application
- un composant
- un site web
- un jeu
- une bibliothèque
et ainsi de suite...

Le langage de programmation utilisé n'est pas non plus important, mais je dois terminer le projet avant 23h59 (mon heure), sinon je me "punis" en donnant 5 $ à 5 personnes (25 $ au total) - les cinq premières personnes qui le signalent sur Twitter que j'ai manqué la date limite. ?

Si vous voulez vous joindre, vous pouvez en lire plus sur ce défi et ses autres variantes [ici](https://www.florin-pop.com/blog/2019/09/100-days-100-projects).

**Note** : vous n'êtes pas obligé de donner 5 $ si vous échouez, fixez simplement une autre "punition" pour vous-même. De plus, il existe d'autres variantes avec moins de jours (**7Days7Projects** et **30Days30Projects**) si vous ne vous sentez pas de relever le défi des 100 jours.

---

Pour le premier projet du défi [#100Days100Projects](https://florin-pop.com/blog/2019/09/100-days-100-projects), j'ai pensé travailler avec une API publique afin d'obtenir des données qui seraient affichées sur une page web - une chose habituelle à faire avec une API.

Pour cela, j'ai choisi d'utiliser l'API publique de [TheMealDB](https://www.themealdb.com) afin d'obtenir des repas aléatoires en appuyant sur un bouton. Quelque chose de simple ! ?

Consultez la version live de ce que nous allons construire dans cet article sur [CodePen](https://codepen.io/FlorinPop17/full/WNeggor) :

%[https://codepen.io/FlorinPop17/pen/WNeggor]

Comme toujours, commençons par le début :

## Le HTML

```html
<div class="container">
	<div class="row text-center">
		<h3>
			Vous avez faim ?
		</h3>
		<h5>Obtenez un repas aléatoire en cliquant ci-dessous</h5>
		<button class="button-primary" id="get_meal">Obtenir un repas ?</button>
	</div>
	<div id="meal" class="row meal"></div>
</div>
```

Nous avons un peu de texte, mais les deux parties les plus importantes sont :

- le bouton `#get_meal` et
- la div `#meal`

Nous allons utiliser le `button` pour faire une requête à l'API. Cela renverra des données que nous allons mettre dans la div `#meal` qui sert de conteneur - dans ce cas.

Habituellement, après le HTML, je passe directement au CSS. Mais nous n'avons pas encore tout le balisage car il sera rempli dans la section **JavaScript**, c'est donc ce que nous allons faire ensuite.

## Le JavaScript

Comme mentionné ci-dessus, nous avons besoin du `button` et de ce conteneur `div` :

```js
const get_meal_btn = document.getElementById('get_meal');
const meal_container = document.getElementById('meal');
```

Ensuite, avant de plonger plus dans le code, voyons ce que l'API va retourner. Pour cela, veuillez ouvrir l'URL suivante : [https://www.themealdb.com/api/json/v1/1/random.php](https://www.themealdb.com/api/json/v1/1/random.php).

Comme vous pouvez le voir dans l'URL, nous obtenons un repas **aléatoire** de cette API (rafraîchissez pour voir l'_aléatoire_). Lorsque nous faisons une requête **GET** à ce point de terminaison (comme y accéder depuis le navigateur), il renvoie une réponse JSON, que nous pouvons analyser afin de récupérer les données que nous voulons.

Les données ressemblent à quelque chose comme ceci :

```js
{
	meals: [
		{
			idMeal: '52873',
			strMeal: 'Beef Dumpling Stew',
			strDrinkAlternate: null,
			strCategory: 'Beef',
			strArea: 'British',
			strInstructions: 'Long description',
			strMealThumb:
				'https://www.themealdb.com/images/media/meals/uyqrrv1511553350.jpg',
			strTags: 'Stew,Baking',
			strYoutube: 'https://www.youtube.com/watch?v=6NgheY-r5t0',
			strIngredient1: 'Olive Oil',
			strIngredient2: 'Butter',
			strIngredient3: 'Beef',
			strIngredient4: 'Plain Flour',
			strIngredient5: 'Garlic',
			strIngredient6: 'Onions',
			strIngredient7: 'Celery',
			strIngredient8: 'Carrots',
			strIngredient9: 'Leek',
			strIngredient10: 'Swede',
			strIngredient11: 'Red Wine',
			strIngredient12: 'Beef Stock',
			strIngredient13: 'Bay Leaf',
			strIngredient14: 'Thyme',
			strIngredient15: 'Parsley',
			strIngredient16: 'Plain Flour',
			strIngredient17: 'Baking Powder',
			strIngredient18: 'Suet',
			strIngredient19: 'Water',
			strIngredient20: '',
			strMeasure1: '2 tbs',
			strMeasure2: '25g',
			strMeasure3: '750g',
			strMeasure4: '2 tblsp ',
			strMeasure5: '2 cloves minced',
			strMeasure6: '175g',
			strMeasure7: '150g',
			strMeasure8: '150g',
			strMeasure9: '2 chopped',
			strMeasure10: '200g',
			strMeasure11: '150ml',
			strMeasure12: '500g',
			strMeasure13: '2',
			strMeasure14: '3 tbs',
			strMeasure15: '3 tblsp chopped',
			strMeasure16: '125g',
			strMeasure17: '1 tsp ',
			strMeasure18: '60g',
			strMeasure19: 'Splash',
			strMeasure20: '',
			strSource:
				'https://www.bbc.co.uk/food/recipes/beefstewwithdumpling_87333',
			dateModified: null
		}
	];
}
```

En gros, nous obtenons un tableau de `meals`, mais avec un seul élément - celui généré aléatoirement. Et cet élément contient toutes les données que nous voulons mettre en avant dans notre petite application. Des choses comme :

- le nom du repas (sous `strMeal`)
- la catégorie du repas (sous `strCategory`)
- l'image du repas (sous `strMealThumb`)
- une vidéo YouTube avec la recette (sous `strYoutube`)
- les ingrédients et les mesures (sous `strIngredientsX` et `strMeasureX` - X représentant le nième ingrédient et sa mesure).Cela est un peu étrange car je m'attendrais à avoir ici un tableau avec ces informations, mais ils ont choisi de les ajouter en tant que propriétés d'objet. Bon... ? L'important est de noter qu'il y a un maximum de 20 ingrédients/mesures, bien qu'ils ne soient pas tous remplis - certains peuvent être vides, nous devons donc en tenir compte.

Maintenant que nous avons le bouton, nous allons ajouter un écouteur d'événement pour l'événement `click`. À l'intérieur, nous allons faire une requête à l'API :

```js
get_meal_btn.addEventListener('click', () => {
	fetch('https://www.themealdb.com/api/json/v1/1/random.php')
		.then(res => res.json())
		.then(res => {
			createMeal(res.meals[0]);
		})
		.catch(e => {
			console.warn(e);
		});
});
```

Nous utilisons l'API [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) pour faire la requête. Nous devons simplement passer l'URL de l'API à laquelle nous voulons faire une requête **GET**, et nous allons obtenir une promesse en retour.

Une fois celle-ci résolue, nous avons une réponse (`res`). Cette `res` n'est pas encore dans l'état où nous la voulons, nous allons donc appeler la méthode `.json()` dessus. Ensuite, nous avons enfin le bel objet. Youpi ! ?

Comme mentionné ci-dessus, l'API retourne le tableau `meals` mais avec un seul élément. Nous allons donc passer cet élément (à l'index `0`) à notre fonction `createMeal`, que nous allons définir ensuite.

Je vais coller l'ensemble du bloc de code ci-dessous et nous allons entrer dans les détails par la suite, alors accrochez-vous une seconde. ?

```js
const createMeal = meal => {
	const ingredients = [];

	// Obtenir tous les ingrédients de l'objet. Jusqu'à 20
	for (let i = 1; i <= 20; i++) {
		if (meal[`strIngredient${i}`]) {
			ingredients.push(
				`${meal[`strIngredient${i}`]} - ${meal[`strMeasure${i}`]}`
			);
		} else {
			// Arrêter s'il n'y a plus d'ingrédients
			break;
		}
	}

	const newInnerHTML = `
		<div class="row">
			<div class="columns five">
				<img src="${meal.strMealThumb}" alt="Image du repas">
				${
					meal.strCategory
						? `<p><strong>Catégorie :</strong> ${meal.strCategory}</p>`
						: ''
				}
				${meal.strArea ? `<p><strong>Zone :</strong> ${meal.strArea}</p>` : ''}
				${
					meal.strTags
						? `<p><strong>Tags :</strong> ${meal.strTags
								.split(',')
								.join(', ')}</p>`
						: ''
				}
				<h5>Ingrédients :</h5>
				<ul>
					${ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
				</ul>
			</div>
			<div class="columns seven">
				<h4>${meal.strMeal}</h4>
				<p>${meal.strInstructions}</p>
			</div>
		</div>
		${
			meal.strYoutube
				? `
		<div class="row">
			<h5>Recette vidéo</h5>
			<div class="videoWrapper">
				<iframe width="420" height="315"
				src="https://www.youtube.com/embed/${meal.strYoutube.slice(-11)}">
				</iframe>
			</div>
		</div>`
				: ''
		}
	`;

	meal_container.innerHTML = newInnerHTML;
};
```

En gros, le but de toute la fonction est de récupérer la réponse JSON, de l'analyser et de la transformer en un composant HTML. Pour cela, nous devons faire quelques choses, car les données ne sont pas encore formatées exactement comme nous le voulons.

Tout d'abord, nous récupérons tous les **ingrédients** et leurs **mesures**. Comme mentionné ci-dessus, il y a un maximum de 20 ingrédients, mais ils sont séparés dans leurs propres propriétés dans l'objet comme : `strIngredient1`, `strIngredient2`, etc... (Je ne sais toujours pas pourquoi ils ont fait cela, mais... ?).

Nous créons donc une boucle `for` qui va de `1` à `20` et vérifie si le `meal` a cette paire `ingredient`-`measure` correspondante. Si c'est le cas, nous la mettons dans le tableau `ingredients`. S'il n'y a plus d'ingrédients, nous arrêtons la boucle `for` avec une condition `break`.

Ensuite, nous créons la chaîne `newInnerHTML` qui va contenir tout le balisage HTML. Dans celle-ci, nous analysons les propriétés restantes que nous voulons afficher.

**Notez** que certaines des propriétés peuvent ne pas être disponibles. Nous utilisons donc l'opérateur [ternaire](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) pour vérifier si nous avons les données pour afficher le tag correspondant. Si nous ne l'avons pas, nous retournons une chaîne vide et rien ne sera affiché sur la page. La `category` et la `area` sont des exemples de ce type de propriétés.

Les tags arrivent dans une chaîne divisée par une virgule comme : `'tag1,tag2,tag3'`. Nous devons donc les `split` par cette virgule, et les `join` avec une virgule et un espace car cela semble plus joli (`'tag1, tag2, tag3'` F496). Ou du moins pour moi. ?

Pour afficher les `ingredients`, nous parcourons le tableau et créons un `<li>` pour chaque paire ingrédient/mesure. À la fin, nous rejoignons le tableau pour former une chaîne. (C'est quelque chose que vous feriez en ReactJS mais sans la partie `join` ?).

Il y a aussi une chaîne de vidéo YouTube (peut-être) qui retourne l'URL de la vidéo. Mais pour que nous puissions intégrer la vidéo dans la page, nous devons extraire uniquement l'ID de la vidéo. Pour cela, nous utilisons `.slice(-11)` pour obtenir les 11 derniers caractères de la chaîne car c'est là que se cache l'ID ?.

Et enfin, nous définissons ce `newInnerHTML` entier comme étant le `innerHTML` du `meal_container` -> cela remplira cette div avec toutes ces informations !

Ce processus entier se répétera chaque fois que nous appuierons sur le bouton `Obtenir un repas`.

## Le CSS

La dernière partie consiste à le styliser un peu, n'est-ce pas ? ?

Pour le **CSS**, je voulais utiliser quelque chose de nouveau, alors j'ai essayé la bibliothèque [SkeletonCSS](http://getskeleton.com/). Elle est utile si vous avez un petit projet et que vous ne voulez pas être submergé par toutes ces classes, car elle n'en a que quelques-unes qui s'occupent de quelques styles de base (le bouton par exemple) et de la partie responsive.

```css
@import url('https://fonts.googleapis.com/css?family=Muli&display=swap');

* {
	box-sizing: border-box;
}

body {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	padding: 30px 0;
	min-height: calc(100vh - 60px);
}

img {
	max-width: 100%;
}

p {
	margin-bottom: 5px;
}

h3 {
	margin: 0;
}

h5 {
	margin: 10px 0;
}

li {
	margin-bottom: 0;
}

.meal {
	margin: 20px 0;
}

.text-center {
	text-align: center;
}

.videoWrapper {
	position: relative;
	padding-bottom: 56.25%;
	padding-top: 25px;
	height: 0;
}

.videoWrapper iframe {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}
```

Vous pouvez voir que le CSS est assez simple. La seule partie qui mérite d'être mentionnée est la déclaration CSS `.videoWrapper`. Cela garantit que l'intégration YouTube est responsive. (J'ai obtenu cela de [CSS-Tricks](https://css-tricks.com/NetMag/FluidWidthVideo/Article-FluidWidthVideo.php) - merci les gars ! ?)

## Conclusion

Et voilà ! Nous avons terminé ! ?

Vous devriez maintenant savoir comment utiliser une API publique pour obtenir des données que vous pouvez ensuite insérer facilement sur la page ! Bien joué ! ?

_Ce est le premier projet que j'ai fait pour le défi [#100Days100Projects](https://florin-pop.com/blog/2019/09/100-days-100-projects). Vous pouvez consulter les autres projets que j'ai construits et quelles sont les règles du défi (si vous souhaitez vous joindre) en cliquant [ici](https://florin-pop.com/blog/2019/09/100-days-100-projects)._

Vous pouvez lire plus de mes articles sur [www.florin-pop.com](https://florin-pop.com).


Bon codage ! ?