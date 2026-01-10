---
title: How to Add Filtering Functionality to Your Applications
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-02-22T17:21:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-filtering-functionality-to-your-application
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/filtering.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'Suppose you have an application where you want to filter the data based
  on some criteria like size, color, price, and so on.

  In this article, we will see how you can do that.

  So let''s get started.

  Initial Setup

  Let''s say we have the following list of...'
---

Suppose you have an application where you want to filter the data based on some criteria like `size`, `color`, `price`, and so on.

In this article, we will see how you can do that.

So let's get started.

## Initial Setup

Let's say we have the following list of products:

```js
const products = [
  { name: 'Macbook Air', price: '180000', ram: 16 },
  { name: 'Samsung Galaxy M21', price: '13999', ram: 4 },
  { name: 'Redmi Note 9', price: '11999', ram: 4 },
  { name: 'OnePlus 8T 5G', price: '45999', ram: 12 }
];
```

and for filtering, we have two dropdowns – one for sorting by various criteria like `price` and `ram`, and the other dropdown is for the order of sorting like `descending` or `ascending` as shown below:

```html
<div class="filters">
  <div>
    Sort By:
    <select class="sort-by">
      <option value="">Select one</option>
      <option value="price">Price</option>
      <option value="ram">Ram</option>
    </select>
  </div>
  <div>
    Sort Order:
    <select class="sort-order">
      <option value="">Select one</option>
      <option value="asc">Ascending</option>
      <option value="desc">Descending</option>
    </select>
  </div>
</div>

<div class="products"></div>
```

## How to Display Products on the UI

Let's add a `displayProducts` function which will display the products on the UI.

```js
const container = document.querySelector(".products");

const displayProducts = (products) => {
  let result = "";

  products.forEach(({ name, price, ram }) => {
    result += `
     <div class="product">
      <div><strong>Name:</strong><span>${name}</span></div>
      <div><strong>Price:</strong><span>${price}</div>
      <div><strong>Ram:</strong><span>${ram} GB</div>
     </div>
    `;
  });

  container.innerHTML = result;
};

displayProducts(products);
```

The `displayProducts` function in the above code loops through the `products` array using the array `forEach` method. It generates HTML that'll be displayed using ES6 template literal syntax and inserts it inside the `products` div.

As we're passing the array of objects to the `displayProducts` function, we're using ES6 destructuring syntax for the `forEach` loop callback function to get `name`, `price`, and `ram`.

Here's a [Code Pen Demo](https://codepen.io/myogeshchavan97/pen/LYZaaqQ).

Your initial screen will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/filter_initial.png)

## How to Add the Filtering Functionality

Now, let's add the filtering functionality.

To handle an onchange event of the `Sort By` dropdown, we will add an event handler for that.

```js
sortByDropdown.addEventListener('change', () => {
  // some code
};
```

We have already defined the reference of all the required elements at the top in the above Code Pen as shown below:

```js
const sortByDropdown = document.querySelector(".sort-by");
const sortOrderDropdown = document.querySelector(".sort-order");
const container = document.querySelector(".products");
```

Now, let's add the sorting logic:

```js
sortByDropdown.addEventListener("change", () => {
  const sortByValue = sortByDropdown.value; // price or ram value
  const sortOrderValue = sortOrderDropdown.value; // asc or desc value

  const sorted =
    sortOrderValue === "desc"
      ? descendingSort(sortByValue)
      : ascendingSort(sortByValue);

  displayProducts(sorted);
});
```

Here, we're checking the value of the second dropdown. If it's `desc`, we're calling the `descendingSort` function (which we're yet to define). Otherwise we're calling the `ascendingSort` function by passing the first dropdown value whether to sort by `price` or `ram`.

Then we're passing that result to the `displayProducts` function so it will update the UI with that sorted products.

## How to Add Sorting Functionality

Now, let's add the `descendingSort` and `ascendingSort` functions.

```js
const ascendingSort = (sortByValue) => {
  return products.sort((a, b) => {
    if (a[sortByValue] < b[sortByValue]) return -1;
    if (a[sortByValue] > b[sortByValue]) return 1;
    return 0;
  });
};

const descendingSort = (sortByValue) => {
  return products.sort((a, b) => {
    if (a[sortByValue] < b[sortByValue]) return 1;
    if (a[sortByValue] > b[sortByValue]) return -1;
    return 0;
  });
};
```

Here, we're using the comparator function for the array sort function.

As you know, if we have an object like this:

```js
const product = { name: 'Macbook Air', price: '180000', ram: 16 };
```

then we can access its properties in two ways:

1. using `product.name`
2. using `product['name']`

As we're having a dynamic value of `sortByValue` variable, we're using the 2nd way inside the `sort` function to get the product value (`a[sortByValue]` or `b[sortByValue]`).

### How sorting in ascending order works

* If the first value to be compared is alphabetically before the second value, a negative value is returned.
* If the first value to be compared is alphabetically after the second value, a positive value is returned.
* If the first and second values are equal, zero is returned, which will automatically sort the array in ascending order.

### How sorting in descending order works

* If the first value to be compared is alphabetically before the second value, a positive value is returned.
* If the first value to be compared is alphabetically after the second value, a negative value is returned.
* If the first and second values are equal, zero is returned, which will automatically sort the array in descending order.

> If you're not familiar with how sorting works for the comparator function, check out [this article](https://levelup.gitconnected.com/array-sort-method-and-its-gotchas-5859ece92e8d?source=friends_link&sk=ad7f5a1b2a301517367783dc543ed908) to better understand everything about sorting in JavaScript.

Now, we want to trigger the sorting functionality when we change the sort order dropdown. So let's add an event handler for that also.

```js
sortOrderDropdown.addEventListener("change", () => {
  const event = new Event("change");
  const sortByValue = sortByDropdown.value;

  if (sortByValue) {
    sortByDropdown.dispatchEvent(event);
  }
});
```

Here, we have added the `if` condition because we don't want to sort the products when the sort by dropdown is not selected.

Here's a [Code Pen Demo](https://codepen.io/myogeshchavan97/pen/vYKPPwV).

Check out the below working functionality demo:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/manual_filter.gif)

## How to Use Lodash to Simplify the Sorting Code

If you don't want to write your own sorting logic, you can use the `orderBy` method provided by [lodash](https://lodash.com/) which is a very popular utility library.

> If you're not familiar with lodash and the powerful functions provided by the library check out [this article](https://levelup.gitconnected.com/extremely-useful-lodash-methods-b38f121fea7e?source=friends_link&sk=558db260b096e7592e02bd328982c0a4) for an introduction to its various useful methods.

Let's add the `orderBy` method on change of the sort by dropdown like this:

```js
sortByDropdown.addEventListener("change", () => {
  const sortByValue = sortByDropdown.value; // price or ram value
  const sortOrderValue = sortOrderDropdown.value; // asc or desc value

  const sorted = _.orderBy(products, [sortByValue], sortOrderValue);

  displayProducts(sorted);
});
```

and remove both the `ascendingSort` and `descendingSort` functions.

For the `orderBy` method, we have provided

* the array to sort as the first parameter
* the property from the object based on which we need to sort (`price` or `ram`) as the second parameter
* the sort order (`asc` or `desc`) as the third parameter

Here's a [Code Pen Demo](https://codepen.io/myogeshchavan97/pen/MWexdJP?editors=0010).

With this `orderBy` method of lodash, the functionality works exactly the same as before. The only thing is that we don't have to write the sorting logic.

### **Thanks for reading!**

Want to learn all ES6+ features in detail including `let` and `const`, promises, various promise methods, array and object destructuring, arrow functions, async/await, import and export and a whole lot more?

Check out my [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/?coupon=LA1HR55) book. This book covers all the pre-requisites for learning React and helps you to become better at JavaScript and React.

Also, check out my **free** [Introduction to React Router](https://yogeshchavan1.podia.com/react-router-introduction) course to learn React Router from scratch.

**Want to stay up to date with regular content regarding JavaScript, React, Node.js? [Follow me on LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**

