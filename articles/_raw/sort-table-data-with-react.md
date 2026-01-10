---
title: How to sort table data with React
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
seo_title: null
seo_desc: 'By Florin Pop

  Often when you have a table with information you''d want to be able to sort the
  information in the table in ascending or descending order, especially when you are
  dealing with numbers.

  In this tutorial we''re going to see how to do exactl...'
---

By Florin Pop

Often when you have a table with information you'd want to be able to sort the information in the table in ascending or descending order, especially when you are dealing with numbers.

In this tutorial we're going to see how to do exactly that using ReactJS.

Here's what we're going to build:

%[https://codepen.io/FlorinPop17/pen/gVYYxe]

We have a list of the top 10 billionaires in the world and we want to sort the list based on the net worth of the billionaires. I got the list information from [theweek.co.uk](https://www.theweek.co.uk/people/57553/top-billionaires-who-richest-person-world) website.

## Prerequisites

Before we move on, let's see the things that we're going to use in this tutorial:

1. [FontAwesome](https://fontawesome.com) - for icons
2. [Foundation](https://foundation.zurb.com/) - for general styling. We're using this especially for the table styling as we don't want to get distracted by the styling in this tutorial
3. [ReactJS](https://reactjs.org) - please **note** that I'm not going to explain the basics of React in this tutorial. By continuing I'm assuming that you worked with it before (although the things that we're going to do aren't hard at all ?)
4. The data - as mentioned above, we'll get a list of the top 10 billionaires in the world plus their net worth

## The Data

We're going to create an array with objects containing the name of the billionaires and their net worth in billion USD:

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

## The App component

This component will the be main one which will be generated on the page. It only has some text + the `<Table />` component and it's passing down to it the `tableData` we declared above.

```js
const App = () => (
	<div className='text-center'>
		<h4>A list of top 10 richest billionaires.</h4>
		<p>
			Click on the icon next to "Net Worth" to see the sorting functionality
		</p>

		<Table data={tableData} />

		<small>
			* Data gathered from{' '}
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

Now that all of that is out of the way, we can focus on what's important ?:

## The Table component

It'll be a class component as we need to use the state in it, but first let's focus on the `render` method. We'll `map` over the `data` that's coming from the parent component and we'll create a table row (`tr`) for every data in the array. Alongside that we have a basic table structure (`table > thead + tbody`).

```js
class Table extends React.Component {
	render() {
		const { data } = this.props;

		return (
			data.length > 0 && (
				<table className='text-left'>
					<thead>
						<tr>
							<th>Name</th>
							<th>Net Worth</th>
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

Next, the sorting...

We're going to have 3 types of sorts: `'default'`, `'up'` (ascending), `'down'` (descending). These types will be changed with the aid of a button which will have a FontAwesome icon depending which sort type is currently active. Let's create an object which will give us the necessary information:

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

As you can see, we have two props for each type of sorts:

1. `class` - this will be used by the icon in the button as we'll see which state is currently active
2. `fn` - this will be the `function` that we'll use to sort the items in the array before we display it in the table. Basically we're comparing the `net_worth` property of the objects

Great so far! ?

We also need to add a `currentSort` state to the `Table` component which will keep track of the active sort type and finally, we'll have an `onSortChange` method which will be called every time the sort button will be clicked and it will change the `currentSort` value.

A lot of words ?, but let's see the code and I bet you'll understand ?:

```js
class Table extends React.Component {
	// declaring the default state
	state = {
		currentSort: 'default'
	};

	// method called every time the sort button is clicked
	// it will change the currentSort value to the next one
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
							<th>Name</th>
							<th>
								Net Worth
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

Notice that we're not changing the original `data` array, but we're creating another array with the `...` (spread) operator, and then we're using the `fn` given by the `sortTypes` object to sort the array accordingly.

## Conclusion

That's pretty much it! Now you know how to sort a table based on the values in a column. Congratulations! 

Happy Coding! 


_Originally posted on [www.florin-pop.com](https://www.florin-pop.com/blog/2019/07/sort-table-data-with-react/)_

