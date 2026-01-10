---
title: Voici un cours gratuit pour aider les développeurs front-end à apprendre les
  maths
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-25T15:05:47.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-practical-math-for-front-end-developers-heres-our-free-11-part-course-by-radical-coder
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-23-at-16.49.35.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: Scrimba
  slug: scrimba
seo_title: Voici un cours gratuit pour aider les développeurs front-end à apprendre
  les maths
seo_desc: 'By Per Harald Borgen

  Are you looking to become a more effective developer by improving your fundamental
  math skills without reaching for NASA-level calculations? Look no further!

  At Scrimba, we''re are really excited to announce our new course ''Practi...'
---

Par Per Harald Borgen

Cherchez-vous à devenir un développeur plus efficace en améliorant vos compétences fondamentales en maths sans atteindre des calculs de niveau NASA ? Ne cherchez plus !

Chez Scrimba, nous sommes vraiment ravis d'annoncer notre nouveau cours ['Mathématiques Pratiques pour les Développeurs Front-End'](https://scrimba.com/course/gpracticalmath), qui offre exactement cela. Dans le cours, nous construisons 3 projets :

1. Un Panier d'Achat, où nous générons une liste de produits, calculons le prix total des produits et appliquons un taux de taxe.
2. Un Calendrier Hebdomadaire, où nous introduisons l'objet `Date`, effectuons une manipulation de mise en page et apprenons la fonction `reduce`.
3. Une Feuille de Dépenses Mensuelles, qui rassemble tout ce que nous avons appris et nous donne quelques conseils et astuces pratiques.

Ce cours vous est présenté par Ryan Gonyon, qui a ses propres chaînes [Twitch](https://www.google.com/url?q=https://www.twitch.tv/radicalcoder&sa=D&ust=1585686482555000&usg=AFQjCNHoQP_okALIk85y1YojlBM-DwEiHw) et [YouTube](https://www.google.com/url?q=https://www.youtube.com/channel/UC2J1l95xB98Fd-v9xGkxHIg&sa=D&ust=1585686482556000&usg=AFQjCNGzqdwTLYFINOKqnrb4a0XgwxY_DA).

Avec 5 ans d'expérience en développement Web, un B.S. en informatique et de l'expérience dans l'enseignement des maths de la maternelle à l'université, Ryan est le tuteur parfait pour ce cours. Rendez-vous sur [Scrimba](https://scrimba.com/playlist/pzKyeuP?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) pour voir ce qu'il a en réserve !

# Mise en page de l'application et introduction à CSS calc()

[![En-tête du site, principal et pied de page](https://dev-to-uploads.s3.amazonaws.com/i/6ox8mhsqz51nnxda6q0t.png)](https://scrimba.com/p/pzKyeuP/c73zJGtp?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans ce screencast, Ryan nous montre comment construire la coque externe de nos applications en dimensionnant correctement les balises `<header>`, `<footer>` et `<main>` avec des variables CSS et la fonction `calc()`.

Nous utilisons `overflow-y: auto`; pour nous assurer que le contenu de la balise `<main>` ne s'étend pas sur le pied de page.

```css
* {
	--headerFontSize: 2rem;
	--headerPadding: 0.5rem;
	--footerFontSize: 1rem;
	--footerPadding: 1rem;
}

header {
	font-size: var(--headerFontSize);
	padding: var(--headerPadding);
}

main {
	font-size: 1.5rem;
	height: calc(
		100vh - var(--headerFontSize) - (2 * var(--headerPadding)) - var(
				--footerFontSize
			) - (2 * var(--footerPadding))
	);
	overflow-y: auto;
}

footer {
	font-size: var(--footerFontSize);
	padding: var(--footerPadding);
}
```

# La fonction roll()

À un moment donné de votre parcours en développement front-end, il sera utile de générer des données aléatoires pour tester vos mises en page. La fonction `roll()` fait exactement cela. Ce cast nous montre également comment utiliser le module `Math` de JavaScript et la fonction `random()`.

```js
function roll(min, max, floatFlag) {
	let r = Math.random() * (max - min) + min;
	return floatFlag ? r : Math.floor(r);
}
```

# Panier d'Achat - Générer des Données / Construire la Mise en Page

[![Mise en page du Panier d'Achat terminée](https://dev-to-uploads.s3.amazonaws.com/i/bd17qggr11kjt0mwjsib.png)](https://scrimba.com/p/pzKyeuP/cn4kQnUK?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Cliquez sur l'image pour accéder au cours._

Nous commençons maintenant à construire notre premier projet, le Panier d'Achat, en utilisant notre fonction `roll()` nouvellement écrite pour générer des prix. Cela nous montre combien de temps nous économisons en utilisant nos nouvelles connaissances !

```js
let products = [...Array(5)].map((_, i) => {
	return {
		index: i,
		title: possibleProducts[roll(0, possibleProducts.length)],
		price: roll(1, 10, 1).toFixed(2),
		count: roll(1, 6),
	};
});
```

# Panier d'Achat - Calculer le Total / Appliquer le Taux de Taxe

Dans ce screencast, nous apprenons à utiliser `.reduce` pour calculer le prix total du panier.

```js
let cartTotal = products
	.reduce(function (accumulator, product) {
		console.log(accumulator, product);
		return accumulator + parseFloat(product.price) * product.count;
	}, 0)
	.toFixed(2);
```

Nous voyons également comment utiliser `roll()` pour générer un taux de taxe aléatoire et l'appliquer.

```js
let taxRate = roll(5, 9, 1).toFixed(1);
```

En cours de route, nous pratiquons l'analyse des valeurs flottantes et leur arrondi à un nombre spécifié après un point décimal.

# Panier d'Achat (Défi Bonus) - Poids

En tant que défi bonus dans ce cast, nous générons aléatoirement le poids de chaque article dans notre panier d'achat et calculons le poids total à la caisse. Dans le monde réel, cela pourrait être utilisé pour estimer le coût d'expédition pour l'acheteur.

Pas de spoilers ici, donc si vous voulez voir la solution, vous devrez cliquer sur [le cours](https://scrimba.com/p/pzKyeuP/ce99mQsa?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) ?

# Une Brève Exploration des Formes CSS

[![Formes rendues construites avec CSS](https://dev-to-uploads.s3.amazonaws.com/i/afroa8rcp6hv0g24aej2.png)](https://scrimba.com/p/pzKyeuP/cGmWKMfR?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans ce cast, nous apprenons à créer un carré, un cercle, un losange et un triangle avec des formes CSS.

```css
.triangle {
	height: 0;
	width: 0;
	border-left: 5.5rem solid transparent;
	border-right: 5.5rem solid transparent;
	border-bottom: 5.5rem solid black;
	margin: 1rem;
	position: relative;
}

.triangle:after {
	content: "";
	position: absolute;
	height: 0;
	width: 0;
	border-left: 4.5rem solid transparent;
	border-right: 4.5rem solid transparent;
	border-bottom: 4.5rem solid red;
	left: -4.5rem;
	top: 0.6rem;
}
```

# Calendrier Hebdomadaire - Utilisation de Date() pour Construire la Semaine / Génération de Tâches

Dans ce cast, nous commençons à travailler sur notre application Calendrier Hebdomadaire. Tout d'abord, nous apprenons à connaître l'objet `Date` de JavaScript.

```js
function getNextDay(day) {
	let nextDay = new Date(day);
	nextDay.setDate(day.getDate() + 1);
	return nextDay;
}
```

Ensuite, nous examinons l'utilisation de la fonction `roll()` pour tester la mise en page et produire une liste de tâches. Jetez un coup d'œil [au cours](https://scrimba.com/p/pzKyeuP/c2KKPGh6?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) pour voir comment cela fonctionne.

# Calendrier Hebdomadaire - Construire la Mise en Page / Afficher les Données

[![Application Calendrier Hebdomadaire](https://dev-to-uploads.s3.amazonaws.com/i/uezalgp2o5marghv69gs.png)](https://scrimba.com/p/pzKyeuP/caZZyNA9?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans ce cast, Ryan nous montre comment utiliser la fonction `calc()` pour afficher les données générées dans le cast précédent.

```css
--mainHeight: calc(
	100vh - var(--headerFontSize) - (2 * var(--headerPadding)) - var(
			--footerFontSize
		) - (2 * var(--footerPadding))
);
```

Nous apprenons également à barrer les tâches terminées ([cliquez ici](https://scrimba.com/p/pzKyeuP/caZZyNA9?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article) pour découvrir comment). Le résultat est une application propre et fonctionnelle que nous pouvons utiliser dans la vie quotidienne.

# Feuille de Dépenses Mensuelles - Générer et Afficher le Mois

[![Affichage en grille](https://dev-to-uploads.s3.amazonaws.com/i/a6you8qo65mq9smjyhrv.png)](https://scrimba.com/p/pzKyeuP/cD44VpTW?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Cliquez sur l'image pour accéder au cours._

Ensuite, utilisez les concepts des casts précédents pour construire quelque chose de plus complexe - notre suivi des dépenses. Dans ce projet, nous générons des données, affichons des mois et dessinons une grille.

```js
function displayMonth(month) {
	// <div class="day">3</div>
	let monthHtml = month.reduce(function (accumulator, day) {
		return accumulator + `<div class="day">${day.date.getDate()}</div>`;
	}, "");
	document.getElementById("MonthlyExpenses").innerHTML = monthHtml;
}
```

# Feuille de Dépenses Mensuelles - Générer, Afficher et Suivre les Dépenses

[![Application Feuille de Dépenses Mensuelles](https://dev-to-uploads.s3.amazonaws.com/i/kb2kp4o9k4p6mwlvi0hl.png)](https://scrimba.com/p/pzKyeuP/cD4weyhd?utm_source=fcc&utm_medium=referral&utm_campaign=gpracticalmath_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans le dernier cast, nous effectuons des calculs budgétaires en écrivant des fonctions pour suivre nos dépenses, loyer et factures de services publics. Nous affichons ensuite les dépenses aux côtés du budget restant disponible.

```js
function displayMonth(month, budget, netValue) {
	let monthHtml =
		`<div class="monthly-summary">
        Budget: \$${budget.toFixed(2)} | Valeur Nette: \$${netValue.toFixed(2)}
    </div>` +
		month.reduce(function (accumulator, day) {
			return accumulator + `<div class="day">${day.date.getDate()}</div>`;
		}, "");
	document.getElementById("MonthlyExpenses").innerHTML = monthHtml;
}
```

# Conclusion

Félicitations pour avoir terminé ce cours, j'espère vraiment que vous avez appris quelques conseils et astuces utiles que vous pourrez appliquer dans vos futures aventures de codage !

Bonne apprentissage ;)