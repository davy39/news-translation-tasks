---
title: Comment trier les données d'un tableau avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-19T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/sort-table-data-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/sort-table-data-with-react.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
seo_title: Comment trier les données d'un tableau avec React
seo_desc: 'By Florin Pop

  Often when you have a table with information you''d want to be able to sort the
  information in the table in ascending or descending order, especially when you are
  dealing with numbers.

  In this tutorial we''re going to see how to do exactl...'
---

Par Florin Pop

Souvent, lorsque vous avez un tableau avec des informations, vous souhaitez pouvoir trier les informations du tableau par ordre croissant ou décroissant, surtout lorsque vous traitez des nombres.

Dans ce tutoriel, nous allons voir comment faire exactement cela en utilisant ReactJS.

Voici ce que nous allons construire :

%[https://codepen.io/FlorinPop17/pen/gVYYxe]

Nous avons une liste des 10 milliards les plus riches du monde et nous voulons trier la liste en fonction de la valeur nette des milliards. J'ai obtenu les informations de la liste sur le site [theweek.co.uk](https://www.theweek.co.uk/people/57553/top-billionaires-who-richest-person-world).

## Prérequis

Avant de continuer, voyons les choses que nous allons utiliser dans ce tutoriel :

1. [FontAwesome](https://fontawesome.com) - pour les icônes
2. [Foundation](https://foundation.zurb.com/) - pour le style général. Nous utilisons cela surtout pour le style du tableau car nous ne voulons pas être distraits par le style dans ce tutoriel
3. [ReactJS](https://reactjs.org) - veuillez **noter** que je ne vais pas expliquer les bases de React dans ce tutoriel. En continuant, je suppose que vous avez déjà travaillé avec (bien que les choses que nous allons faire ne soient pas du tout difficiles ?)
4. Les données - comme mentionné ci-dessus, nous obtiendrons une liste des 10 milliards les plus riches du monde plus leur valeur nette

## Les Données

Nous allons créer un tableau avec des objets contenant le nom des milliards et leur valeur nette en milliards de dollars USD :

```js
const tableData = [
	{
		name: 'Amancio Ortega',
		net_worth: 62.7
	},
	{
		name: 'Bernard Arnault',
		net_worth: 76
	},
	{
		name: 'Bill Gates',
		net_worth: 96.5
	},
	{
		name: 'Carlos Sim Helu',
		net_worth: 64
	},
	{
		name: 'Jeff Bezos',
		net_worth: 131
	},
	{
		name: 'Larry Ellison',
		net_worth: 58
	},
	{
		name: 'Larry Page',
		net_worth: 50.8
	},
	{
		name: 'Mark Zuckerberg',
		net_worth: 62.3
	},
	{
		name: 'Michael Bloomberg',
		net_worth: 55.5
	},
	{
		name: 'Warren Buffet',
		net_worth: 82.5
	}
];
```

## Le composant App

Ce composant sera le principal qui sera généré sur la page. Il ne contient que du texte + le composant `<Table />` et transmet les `tableData` que nous avons déclarés ci-dessus.

```js
const App = () => (
	<div className='text-center'>
		<h4>Une liste des 10 milliards les plus riches.</h4>
		<p>
			Cliquez sur l'icône à côté de "Valeur nette" pour voir la fonctionnalité de tri
		</p>

		<Table data={tableData} />

		<small>
			* Données recueillies sur{' '}
			<a
				href='https://www.theweek.co.uk/people/57553/top-billionaires-who-richest-person-world'
				target='_blank'>
				theweek.co.uk
			</a>
		</small>
	</div>
);

ReactDOM.render(<App />, document.getElementById('app'));
```

Maintenant que tout cela est réglé, nous pouvons nous concentrer sur ce qui est important ?:

## Le composant Table

Ce sera un composant de classe car nous devons utiliser l'état, mais concentrons-nous d'abord sur la méthode `render`. Nous allons `mapper` les `data` qui proviennent du composant parent et nous allons créer une ligne de tableau (`tr`) pour chaque donnée du tableau. Avec cela, nous avons une structure de tableau de base (`table > thead + tbody`).

```js
class Table extends React.Component {
	render() {
		const { data } = this.props;

		return (
			data.length > 0 && (
				<table className='text-left'>
					<thead>
						<tr>
							<th>Nom</th>
							<th>Valeur nette</th>
						</tr>
					</thead>
					<tbody>
						{data.map(p => (
							<tr>
								<td>{p.name}</td>
								<td>${p.net_worth}b</td>
							</tr>
						))}
					</tbody>
				</table>
			)
		);
	}
}
```

Ensuite, le tri...

Nous allons avoir 3 types de tris : `'default'`, `'up'` (croissant), `'down'` (décroissant). Ces types seront changés à l'aide d'un bouton qui aura une icône FontAwesome selon le type de tri actuellement actif. Créons un objet qui nous donnera les informations nécessaires :

```js
const sortTypes = {
	up: {
		class: 'sort-up',
		fn: (a, b) => a.net_worth - b.net_worth
	},
	down: {
		class: 'sort-down',
		fn: (a, b) => b.net_worth - a.net_worth
	},
	default: {
		class: 'sort',
		fn: (a, b) => a
	}
};
```

Comme vous pouvez le voir, nous avons deux propriétés pour chaque type de tri :

1. `class` - cela sera utilisé par l'icône dans le bouton pour voir quel état est actuellement actif
2. `fn` - ce sera la `fonction` que nous utiliserons pour trier les éléments du tableau avant de les afficher dans le tableau. Basiquement, nous comparons la propriété `net_worth` des objets

Super jusqu'à présent ! ?

Nous devons également ajouter un état `currentSort` au composant `Table` qui suivra le type de tri actif et enfin, nous aurons une méthode `onSortChange` qui sera appelée chaque fois que le bouton de tri sera cliqué et qui changera la valeur de `currentSort`.

Beaucoup de mots ?, mais regardons le code et je parie que vous comprendrez ?:

```js
class Table extends React.Component {
	// déclaration de l'état par défaut
	state = {
		currentSort: 'default'
	};

	// méthode appelée chaque fois que le bouton de tri est cliqué
	// elle changera la valeur currentSort pour la suivante
	onSortChange = () => {
		const { currentSort } = this.state;
		let nextSort;

		if (currentSort === 'down') nextSort = 'up';
		else if (currentSort === 'up') nextSort = 'default';
		else if (currentSort === 'default') nextSort = 'down';

		this.setState({
			currentSort: nextSort
		});
	};

	render() {
		const { data } = this.props;
		const { currentSort } = this.state;

		return (
			data.length > 0 && (
				<table className='text-left'>
					<thead>
						<tr>
							<th>Nom</th>
							<th>
								Valeur nette
								<button onClick={this.onSortChange}>
									<i className={`fas fa-${sortTypes[currentSort].class}`} />
								</button>
							</th>
						</tr>
					</thead>
					<tbody>
						{[...data].sort(sortTypes[currentSort].fn).map(p => (
							<tr>
								<td>{p.name}</td>
								<td>${p.net_worth}b</td>
							</tr>
						))}
					</tbody>
				</table>
			)
		);
	}
}
```

Remarquez que nous ne changeons pas le tableau `data` original, mais nous créons un autre tableau avec l'opérateur `...` (spread), puis nous utilisons la fonction `fn` donnée par l'objet `sortTypes` pour trier le tableau en conséquence.

## Conclusion

C'est à peu près tout ! Maintenant, vous savez comment trier un tableau en fonction des valeurs d'une colonne. Félicitations ! 

Bon codage ! 


_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/07/sort-table-data-with-react/)_