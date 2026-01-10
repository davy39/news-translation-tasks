---
title: Comment créer un composant de pagination
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-12T12:38:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-pagination-component
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/how-to-create-a-pagination.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Pagination
  slug: pagination
- name: WeeklyCodingChallenge
  slug: weeklycodingchallenge
seo_title: Comment créer un composant de pagination
seo_desc: 'By Florin Pop

  The theme for week #17 of the Weekly Coding Challenge is:

  Pagination

  A Pagination Component is used on websites where you have more content available
  than you want to display at one time to the user so you''d split it on multiple
  pages. ...'
---

Par Florin Pop

Le **thème** pour la semaine #17 du [Défi de codage hebdomadaire](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) est :

## Pagination

Un composant de pagination est utilisé sur les sites web où vous avez plus de contenu disponible que ce que vous souhaitez afficher à l'utilisateur en une seule fois, vous le divisez donc en plusieurs pages. En séparant le contenu sur différentes pages, vous économisez également beaucoup de bande passante pour l'utilisateur car il ne sera pas nécessaire de télécharger toutes les informations en une seule fois.

Quelques **exemples** où vous auriez une pagination : un blog avec plusieurs pages, une boutique en ligne avec plusieurs produits, etc.

Dans cet article, nous allons construire ce [Composant de Pagination](https://codepen.io/FlorinPop17/full/BgrvgX/) :

%[https://codepen.io/FlorinPop17/pen/BgrvgX/]

**Note** : la pagination n'est pas fonctionnelle, elle est juste à des fins de démonstration (visuelle). En tant que défi supplémentaire, vous pouvez lier cela à un site web réel.

## Le HTML

Pour la structure HTML, nous allons utiliser une balise `ul` comme conteneur avec plusieurs `li`. Chaque `li` contiendra une balise `a` car elle est cliquable (et sémantique) et elle enverra l'utilisateur à la page requise (si nécessaire).

Nous utilisons également [FontAwesome](https://fontawesome.com/) pour les icônes (gauche, droite et les icônes de points).

```html
<ul class="pagination">
	<li>
		<a href="#"><i class="fas fa-chevron-left"></i></a>
	</li>
	<li>
		<a href="#"><i class="fas fa-ellipsis-h"></i></a>
	</li>
	<li><a href="#">2</a></li>
	<li class="active"><a href="#">3</a></li>
	<li><a href="#">4</a></li>
	<li><a href="#">5</a></li>
	<li>
		<a href="#"><i class="fas fa-ellipsis-h"></i></a>
	</li>
	<li>
		<a href="#"><i class="fas fa-chevron-right"></i></a>
	</li>
</ul>
```

Comme vous pouvez le voir, j'ai également ajouté une classe `.active` à l'un des `li` - cela sert simplement à mettre en évidence la page sur laquelle nous nous trouvons.

## Le CSS

Je vais coller le CSS et nous discuterons des parties importantes par la suite.

```css
.pagination {
	border: 2px solid #aaa;
	border-radius: 4px;
	display: flex;
	list-style-type: none;
	overflow: hidden;
	padding: 0;
}

.pagination li {
	background-color: #fff;
}

.pagination li:hover,
.pagination li.active {
	background-color: #aaa;
}

.pagination li a {
	color: #555;
	display: block;
	font-weight: bold;
	padding: 10px 15px;
	text-decoration: none;
}

.pagination li:hover a,
.pagination li.active a {
	color: #fff;
}
```

Points à noter :

1. La balise `ul` / `.pagination` est un conteneur **flex** - cela est dû au fait qu'il est beaucoup plus facile de positionner les `li` à l'intérieur en utilisant flexbox (et qui n'aime pas flexbox ? ?)
2. Parce que nous avons un petit `border-radius` sur la balise `ul`, nous devons ajouter `overflow: hidden` car sinon le coin des `li` sera visible par-dessus la bordure de la balise `ul` (supprimez le overflow et vous verrez ce que je veux dire)
3. Nous avons le même style sur `li:hover` que sur `li.active`, mais vous pouvez différencier ces deux états si vous le souhaitez

Autrement que cela, je crois que c'est assez simple, mais si vous avez des questions, n'hésitez pas à me les poser. ?

## Conclusion

Il existe d'autres variantes de paginations sur le web. Trouvez celle que vous aimez et convertissez-la en code.

Assurez-vous de partager avec moi ce que vous avez construit !

Bon codage ! ?