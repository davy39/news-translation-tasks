---
title: How to Make a Filter Component in React
subtitle: ''
author: Ateev Duggal
co_authors: []
series: null
date: '2022-01-19T16:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-filter-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Filter-Component-1.png
tags:
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Filter components are useful on websites because they help users find the
  results they need quickly and easily.

  This is especially true if your data comes from an API, since users cannot look
  through everything your app has to offer.

  In this article,...'
---

Filter components are useful on websites because they help users find the results they need quickly and easily.

This is especially true if your data comes from an API, since users cannot look through everything your app has to offer.

In this article, we will be using dummy data that we have hardcoded and saved like an array in a separate component named **Data.js.**

**What we'll cover here:**

1. Getting Started
    
2. Creating our React App
    
3. Getting data from Data.js using Hooks
    
4. Working on the UI of our App
    
5. Making the Filter Component
    
6. Wrapping Up
    

## Getting Started

For this particular project, we will be using dummy food data which contains several key-value pairs as shown in this code:

```json
const Data = [
  {
    id: "1",
    title: "Poha",
    category: "Breakfast",
    price: "$1",
    img: "https://c.ndtvimg.com/2021-08/loudr2go_aloo-poha_625x300_05_August_21.jpg?im=FeatureCrop,algorithm=dnn,width=620,height=350",
    desc: " Poha. Light, filling and easy to make, poha is one famous breakfast that is eaten almost everywhere in the country. And the best part is- it can be made in a number of ways. Kanda poha, soya poha, Indori poha, Nagpur Tari Poha are a few examples",
  },
  {
    id: "2",
    title: "Upma",
    category: "Breakfast",
    price: "$1",
    img: "https://c.ndtvimg.com/2021-04/37hi8sl_rava-upma_625x300_17_April_21.jpg?im=FeatureCrop,algorithm=dnn,width=620,height=350",
    desc: " A quintessential South Indian Breakfast! Made with protein-packed urad dal and semolina followed by crunchy veggies and curd, this recipe makes for a hearty morning meal. With some grated coconut on top, it gives a beautiful south-Indian flavour.",
  },
  {
    id: "3",
    title: "Cheela",
    category: "Breakfast",
    price: "$1",
    img: "https://c.ndtvimg.com/2019-05/1afu8vt8_weight-loss-friendly-breakfast-paneer-besan-chilla_625x300_25_May_19.jpg?im=FaceCrop,algorithm=dnn,width=620,height=350",
    desc: "A staple across Indian households, moong dal is widely used in a number of Indian delicacies. One such delicacy is moong dal cheela. You can also add paneer to this recipe to amp up the nutritional value and make it, even more, protein-dense",
  },
  {
    id: "4",
    title: "Channa Kulcha",
    category: "Lunch",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-04/chana-kulcha_625x350_41429707001.jpg",
    desc: "A classic dish that never goes out of style. The quintessential chana kulcha  needs only a few ingredients - cumin powder, ginger, coriander powder, carom powder, and some mango powder, which is what gives the chana its sour and tangy taste.",
  },
  {
    id: "5",
    title: "Egg Curry",
    category: "Lunch",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2017-11/goan-egg-curry_620x350_41511515276.jpg",
    desc: "Eggs are a versatile food that can be cooked for any meal of the day. From breakfast to dinner, it can be a go-to food. Here is a mildly-spiced egg curry made with garlic, onions, a whole lot of kasuri methi, fresh cream, yogurt, and fresh coriander.",
  },
  {
    id: "6",
    title: "Paneer Aachari",
    category: "Lunch",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-04/paneer_625x350_61429707960.jpg",
    desc: "Don't get intimidated by the list of ingredients because not only are already in your kitchen cabinet, but also because all they'll need is 20 minutes of your time. Chunks of cottage cheese cooked in some exciting spices, yogurt and a pinch of sugar.",
  },
  {
    id: "7",
    title: "Fish Fry",
    category: "Dinner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-06/indian-dinner_625x350_41434360207.jpg",
    desc: "Get your daily dose of perfect protein. Pieces of surmai fish marinated in garlic, cumin, fennel, curry leaves, and tomatoes are pan-fried in refined oil and served hot. This fish fry recipe has a host of delectable spices used for marination giving it a unique touch.",
  },
  {
    id: "8",
    title: "Dum Alloo",
    category: "Dinner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2015-06/indian-dinner_625x350_51434362664.jpg",
    desc: "Your family will thank you for this fantastic bowl of dum aloo cooked Lakhnawi style. Take some potatoes, crumbled paneer, kasuri methi, butter, onions, and some ghee.",
  },
  {
    id: "9",
    title: "Malai Kofta",
    category: "Dinner",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2017-10/makhmali-kofte_620x350_51508918483.jpg",
    desc: "A rich gravy made of khus khus, coconut and milk that tastes best with koftas made from khoya. This velvety and creamy recipe will leave you licking your fingers. Makhmali kofte can be your go-to dish for dinner parties as this is quite different from other kofta recipes and extremely delicious.",
  },
  {
    id: "10",
    title: "Malai Kofta",
    category: "Snaks",
    price: "$1",
    img: "https://i.ndtvimg.com/i/2017-10/makhmali-kofte_620x350_51508918483.jpg",
    desc: "A rich gravy made of khus khus, coconut and milk that tastes best with koftas made from khoya. This velvety and creamy recipe will leave you licking your fingers. Makhmali kofte can be your go-to dish for dinner parties as this is quite different from other kofta recipes and extremely delicious.",
  },
];
 
export default Data;
```

Among these key-value pairs, we also have a category which will be used for filtering the results.

We will be using bootstrap as the CDN for this project for styling our app.

After this tutorial, you should know more about how to make and import components in React, how to use data dynamically, and most of all how to pass and use props between parent and child components.

## How to Create our React Component

It's very easy to create a React App – just go to your working directory in any of your preferred IDE’s and enter the following command in the terminal:

```php
npx create-react-app react-filter-app
```

If you are unsure how to properly set up a create-react-app project you can refer to the official guide here at [create-react-app-dev](https://create-react-app.dev/docs/getting-started/).‌‌

After the setup, run `npm start` in the same terminal to start the localhost:3000 where our React app will be hosted. We can also see all our changes there.

## How to Get the data from Data.js using Hooks

Now that we have successfully set up our React project, it’s time to fetch our data from Data.js and use it in our UI.

For this, we will first need to import our data in our **App.js** component and then use the useState hook for managing the state of our data.

```javascript
import React, { useState } from "react";
import Data from "./Data";
import Card from "./Card";
 
const App = () => {
  const [item, setItem] = useState(Data);
  return (
    <>
      <div className="container-fluid">
        <div className="row">
          <h1 className="col-12 text-center my-3 fw-bold">Our Menu</h1>
          <Card item={item} /> // UI Component
        </div>
      </div>
    </>
  );
};
 
export default App;
```

## How to Build the UI Part of our App

Now we have our data stored in a variable which we can use freely in our App, we can work on the UI.

The UI will contain [bootstrap cards](https://getbootstrap.com/docs/5.0/components/card/) which we'll make dynamically using the map function.

We will make a different component for our cards. As you can see in the above code, we have named it **Card.js** and have also imported it. We've also passed **item** as props so that we can use the data stored in the item in the card component.

This component will contain all our cards and the data which we will show dynamically in our App using the **map function.**

```javascript
import React from "react";
 
const Card = ({ item }) => {            
           // destructuring props
  return (
    <>
      <div className="container-fluid">
        <div className="row justify-content-center">
          {item.map((Val) => {
            return (
              <div
                className="col-md-4 col-sm-6 card my-3 py-3 border-0"
                key={Val.id}
              >
                <div className="card-img-top text-center">
                  <img src={Val.img} alt={Val.title} className="photo w-75" />
                </div>
                <div className="card-body">
                  <div className="card-title fw-bold fs-4">
                    {Val.title} &nbsp;&nbsp;&nbsp;&nbsp;--&nbsp;&nbsp;
                    {Val.price}
                  </div>
                  <div className="card-text">{Val.desc}</div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
};
 
export default Card;
```

Our App with 10 cards will look this:

![Image](https://lh5.googleusercontent.com/dcZ-3eTALXbuRdMYsDgy672KsDcuN7D--QbHOl5_2xNjocun5-zAONVPFqD8txXpVvbyKNNBV6rjEi5JAIceQzMy-K-D1OOOjWkKs59EzlRzf-VBkjwz3LxY2I8E4FBL6Bn4vrf5 align="left")

## How to Make the Filter Component

There are many ways we can use the filter components to filter out the data which the user gets from the search results. But here, we will be making buttons for this purpose which will filter out the data based on the category of that food – like breakfast, lunch, dinner, and snacks.

We have to make a new array that will contain only the values of the key category and display them using the map method.

```javascript
// spread operator will display all the values from our category section of our data while Set will only allow the single value of each kind to be displayed

  const menuItems = [...new Set(Data.map((Val) => Val.category))];
```

We're using the **spread operator** here so that every value we get by displaying the above array has the same UI, and also to display all 10 categories as buttons.

We use the `Set()` value so that only 3 or 4 values that are unique will be displayed and also to ensure that there are no repeated values.

We'll create a new component for these buttons that will be dynamically displayed using the map method. But this time we will use our newly formed array as it has all the categories stored in an array and will display them only once due to **Set()**.

```javascript
import React from "react";
import Data from "./Data";
 
const Buttons = ({ setItem, menuItems }) => {
  return (
    <>
      <div className="d-flex justify-content-center">
        {menuItems.map((Val, id) => {
          return (
            <button
              className="btn-dark text-white p-1 px-2 mx-5 btn fw-bold"
              key={id}
            >
              {Val}
            </button>
          );
        })}
        <button
          className="btn-dark text-white p-1 px-3 mx-5 fw-bold btn"
          onClick={() => setItem(Data)}
        >
          All
        </button>
       </div>
    </>
  );
};
 
export default Buttons;
```

Put this button component where you want to display the buttons. In our case, we have displayed buttons above our card component in app.js.

![Image](https://lh5.googleusercontent.com/gX2PTVbyYQIJ-6o_WvhHZVucTJwEZhQz0moqf7GZoC68fcgC2iORyLyqRILAmhQn-e_SQy172o1_BgeLMidY69Jm3UCAXtRBiP-fNwFf50VaJPj8_54SjjlngVvCun_EaOVG-DRh align="left")

It’s time to add a filter in these buttons so that they can filter out dishes depending upon the category.

```javascript
const filterItem = (curcat) => {
    const newItem = Data.filter((newVal) => {
      return newVal.category === curcat; 
        	// comparing category for displaying data
    });
    setItem(newItem);
  };
```

The filter method filters out the data depending upon the category of that object.

Using the `onClick()` event handler, we can attach this filter to our buttons:

```javascript
import React from "react";
import Data from "./Data";
 
const Buttons = ({ filterItem, setItem, menuItems }) => {
  return (
    <>
      <div className="d-flex justify-content-center">
        {menuItems.map((Val, id) => {
          return (
            <button
              className="btn-dark text-white p-1 px-2 mx-5 btn fw-bold"
              onClick={() => filterItem(Val)}
              key={id}
            >
              {Val}
            </button>
          );
        })}
        <button
          className="btn-dark text-white p-1 px-3 mx-5 fw-bold btn"
          onClick={() => setItem(Data)}
        >
          All
        </button> 
       </div>
    </>
  );
};
 
export default Buttons;
```

## Wrapping Up

There are many ways we can use a filter component to reduce the time our user wastes searching for ideal results in our apps.

There are only 10 objects in the array we have used in this app, but many times we get our data from API, where there can be tons of data. In these cases, only a single search isn't often ideal to give exact results, so we use filters to help.

You can see the whole code in the [GitHub Repo](https://github.com/Ateevduggal/Filter-Menu-in-React), and you can check out how these filter buttons work by going through a [live link](https://filter-menu-in-react.vercel.app/) of the app.

You can go through my other projects as well:

1. [How to make a Pagination component in React using Hooks](https://tekolio.com/how-to-make-custom-pagination-in-react-js-with-hooks/)
    
2. [How to make a Dictionary App in React using Hooks](https://tekolio.com/how-to-create-a-dictionary-app-in-react/)
    
3. [How to host a React App on GitHub Pages with a Custom Domain](https://tekolio.com/how-to-host-a-react-app-on-github-pages-with-a-custom-domain/)
