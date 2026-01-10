---
title: How to Create a Random Meal Generator
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
seo_title: null
seo_desc: 'By Florin Pop

  Last week I decided to take on a new challenge. I called it: The #100Days100Projects
  Challenge.

  The purpose of the challenge is to create one project every single day. Think of
  it as a next step for the #100DaysOfCode challenge.

  A proje...'
---

By Florin Pop

Last week I decided to take on a new challenge. I called it: The [#100Days100Projects](https://www.florin-pop.com/blog/2019/09/100-days-100-projects) Challenge.

The purpose of the challenge is to create one project every single day. Think of it as a next step for the #100DaysOfCode challenge.

A project can be either:
- an app
- a component
- a website
- a game
- a library
and so on...

The programming language used is also not important, but I need to complete the project by 11:59 PM (my time), otherwise I'm "punishing" myself by giving away $5 for 5 people ($25 total) - first 5 people who point it out on Twitter that I missed the deadline. ?

If you want to join, you can read more about this challenge and the other variants it has [here](https://www.florin-pop.com/blog/2019/09/100-days-100-projects). 

**Note**: you don't have to give away $5 if you fail, just set some other "punishment" for yourself. Also, there are other variants with less days (**7Days7Projects** and **30Days30Projects**) if you don't feel like taking on the 100Days challenge.

---

For the first project in the [#100Days100Projects](https://florin-pop.com/blog/2019/09/100-days-100-projects) I thought about working with a public API in order to get some data that would be displayed in a webpage - an usual thing to do with an API.

For that I chose to use [TheMealDB](https://www.themealdb.com)'s public API in order to get some random meals by pressing a button. Something straightforward! ?

Check out the live version of what we're going to build in this article over on [CodePen](https://codepen.io/FlorinPop17/full/WNeggor):

%[https://codepen.io/FlorinPop17/pen/WNeggor]

As always let's start at the beginning:

## The HTML

```html
<div class="container">
	<div class="row text-center">
		<h3>
			Feeling hungry?
		</h3>
		<h5>Get a random meal by clicking below</h5>
		<button class="button-primary" id="get_meal">Get Meal ?</button>
	</div>
	<div id="meal" class="row meal"></div>
</div>
```

We have a little text, but the two most important parts are:

- the `#get_meal` button and
- the `#meal` div

We're going to use the `button` to make a request to the API. This will send back some data that we're going to put into the `#meal` div which acts as a container - in this case.

Usually after the HTML I'll go right into the CSS. But we don't yet have the entire markup as it will be populated in the **JavaScript** section, so that's what we're going to do next.

## The JavaScript

As mentioned above, we need the `button` and that container `div`:

```js
const get_meal_btn = document.getElementById('get_meal');
const meal_container = document.getElementById('meal');
```

Next, before we dive more into the code, let's see what the API is going to return. For that please open the following URL: [https://www.themealdb.com/api/json/v1/1/random.php](https://www.themealdb.com/api/json/v1/1/random.php).

As you can see from the URL, we are getting a **random** meal from this API (refresh to see the _randomness_). When we're making a **GET** request to that endpoint (like accessing it from the browser), it sends back a JSON response, which we can parse in order to retrieve the data we want.

The data looks something like this:

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

Basically we get back an array of `meals`, but with only one item in it - the randomly generated one. And this item has all the data we want to showcase in our little application. Things like:

- meal name (under `strMeal`)
- meal caterogy (under `strCategory`)
- meal image (under `strMealThumb`)
- a youtube video with the recipe (under `strYoutube`)
- the ingredients and the measures (under `strIngredientsX` and `strMeasureX` - X representing the nth ingredient and it's measure).This is a little bit awkward as I would expect here to have an array with this information, but they choose to add it as object props. On well... ? The important thing to note is that there are a maximum of 20 ingredients / measures, although they aren't all filled in - some of them might be empty so we need to account for that.

Now that we have the button we're going to add an event listener for the `click` event. Inside we're going to make a request to the API:

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

We're using the [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) API to do the request. We just have to pass in the url of the API we want to make a **GET** request to, and we're going to get back a promise. 

Once this is resolved we have a response (`res`). This `res` isn't yet in the state we want it to be, so we're going to call the `.json()` method on it. Then finally we have the beautiful object. Yay! ?

As mentioned above, the API returns the `meals` array but only with an item in it. So we're going to pass that item (at index `0`) into our `createMeal` function, which we'll define next.

I'm going to paste the entire block of code below and we're going to go into detail afterwards, so hold on for a second. ?

```js
const createMeal = meal => {
	const ingredients = [];

	// Get all ingredients from the object. Up to 20
	for (let i = 1; i <= 20; i++) {
		if (meal[`strIngredient${i}`]) {
			ingredients.push(
				`${meal[`strIngredient${i}`]} - ${meal[`strMeasure${i}`]}`
			);
		} else {
			// Stop if there are no more ingredients
			break;
		}
	}

	const newInnerHTML = `
		<div class="row">
			<div class="columns five">
				<img src="${meal.strMealThumb}" alt="Meal Image">
				${
					meal.strCategory
						? `<p><strong>Category:</strong> ${meal.strCategory}</p>`
						: ''
				}
				${meal.strArea ? `<p><strong>Area:</strong> ${meal.strArea}</p>` : ''}
				${
					meal.strTags
						? `<p><strong>Tags:</strong> ${meal.strTags
								.split(',')
								.join(', ')}</p>`
						: ''
				}
				<h5>Ingredients:</h5>
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
			<h5>Video Recipe</h5>
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

Basically the entire function's purpose is to get the JSON response, parse it, and transform it into an HTML component. For that we need to do a couple of things, as the data is not yet formated exactly the way we want it to be.

First, we're getting all the **ingredients** and their **measures**. As mentioned above there are a maximum of 20 ingredients, but they are separated into their own properties in the object like: `strIngredient1`, `strIngredient2`, etc... (I still don't know why they did that, but... ?).

So, we're creating a `for` loop which goes from `1` to `20` and checks if the `meal` has that corresponding `ingredient`-`measure` pair. If it does, we're putting it into the `ingredients` array. If there aren't any more ingredients we're stopping the for loop with a `break` condition.

Next, we're creating the `newInnerHTML` string which is going to hold the entire HTML markup. In it we are parsing the remaining properties that we want to be displayed.

**Note** that some of the properties might not be available. So for that we're using the [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) to check if we have the data to display the corresponding tag. If we don't have it then we're returning an empty string and nothing will be displayed on the page. The `category` and the `area` are examples of these type of properties.

The tags are coming in a string divided by a comma like: `'tag1,tag2,tag3'`. So we need to `split` it by that comma, and `join` it back by a comma and a space as it looks nicer (`'tag1, tag2, tag3'` ❤️). Or at least for me does. ?

To show the `ingredients`, we're mapping over the array and we're creating an `<li>` for each ingredient/measure pair. At the end we're joining the array back to form a string. (This is something you would do in ReactJS but without the `join`ing part ?).

There is also a Youtube video _string_ (maybe) which is returning the URL of the video. But in order for us to embed the video in the page we need to extract the video ID only. For that we're using `.slice(-11)` to get the last 11 characters of the string as this is where the ID is hiding ?.

And finally, we're setting this entire `newInnerHTML` to be the `meal_container`'s `innerHTML` -> this will populate that div with all this information!

This entire process will repeat every time we're pressing the `Get Meal` button.

## The CSS

The last part is to style it a little bit, right? ?

For the **CSS** I wanted to use something new so I tried out the [SkeletonCSS](http://getskeleton.com/) library. It's useful if you have a small project and don't want to get overwhelmed with all those classes, as it only has a couple of them that take care of some basic styling (the button for example) and the responsive part.

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

You can see that the CSS is pretty simple. The only part that's worth mentioning is the `.videoWrapper` CSS declaration. This makes sure that the YouTube embed is responsive. (Got this from [CSS-Tricks](https://css-tricks.com/NetMag/FluidWidthVideo/Article-FluidWidthVideo.php) - thanks guys! ?)

## Conclusion

And voilà! We're done! ?

You should now know how to use a public API to get some data which you can then insert on the page easily! Well done! ?

_This is the first project I did for the [#100Days100Projects](https://florin-pop.com/blog/2019/09/100-days-100-projects) challenge. You can check out what other projects I've built and what are the rules of the challenge (if you might want to join) by clicking [here](https://florin-pop.com/blog/2019/09/100-days-100-projects)._

You can read more of my articles on [www.florin-pop.com](https://florin-pop.com).


Happy Coding! ?



