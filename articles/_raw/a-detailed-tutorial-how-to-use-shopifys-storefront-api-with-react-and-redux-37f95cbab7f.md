---
title: 'A detailed tutorial: how to use Shopify’s Storefront API with React and Redux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-06T17:56:22.000Z'
originalURL: https://freecodecamp.org/news/a-detailed-tutorial-how-to-use-shopifys-storefront-api-with-react-and-redux-37f95cbab7f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cUOknyEHrQ6wGqynmp__Eg.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: shopify
  slug: shopify
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Chris Frewin

  E-commerce for all! (…websites, that is ?)

  Written by Chris August 2018, updated November, 2018


  _Courtesy of Negative Space on [pexels.com](https://www.pexels.com/photo/grayscale-photo-of-computer-laptop-near-white-notebook-and-ceram...'
---

By Chris Frewin

#### E-commerce for all! (…websites, that is ?)

_Written by [Chris](https://medium.com/@frewin.christopher) August 2018, updated November, 2018_

![Image](https://cdn-media-1.freecodecamp.org/images/QjOaB1iMaaTA4wYVDOKhmtNyjYnzcm-DDxjd)
_Courtesy of Negative Space on [pexels.com](https://www.pexels.com/photo/grayscale-photo-of-computer-laptop-near-white-notebook-and-ceramic-mug-on-table-169573/" rel="noopener" target="_blank" title=")_

#### Background and Motivation

So the motivation here was pretty simple. I wanted my site visitors to be able to browse, search, and select products directly on my custom domain without having to go to our Shopify site.

The secondary motivation is that I’d much rather have my own codebase for a website than use one of Shopify’s factory templates. No offense Shopify team! The templates are modern and clean, but they are rather basic. I’m sure those templates are heavily customizable, but it’s not a stack I know at the moment.

So this is the best of both worlds — my custom React site (already built and online ?), with the added API and checkout process of Shopify!

By the end of this tutorial, you’ll be able to add your Shopify products on _any_ page of your site. The only part of the shopping process that will occur on Shopify is when the user clicks ‘Checkout’.

I’ve created [an empty boilerplate repository](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example) for this tutorial as well.

The motivation specifically for writing here on Medium was simply that I couldn’t find a tutorial on this process myself — so I decided to make one!

I’ve been a professional developer for 4 years now, and programming for 7. I’ve worked in tech stacks from old-school Fortran and Perl, to React, Javascript, Python, and Node.

Siren Apparel is one of my side project / startup / maker companies that I’ve run for 5 years now, and we’ve donated to 5 different police and fire departments so far!

Let’s finally get started with this tutorial.

#### Shopify’s Storefront API

The wonderful folks at Shopify have put together the [Storefront API](https://help.shopify.com/en/api/custom-storefronts/storefront-api). With the Storefront API, you can create React components to add product pictures, product variations, product sizes, a cart, and ‘add to cart’ and ‘checkout’ buttons into your own, non-Shopify site.

*Note that this tutorial is NOT about [Shopify Polaris](https://github.com/Shopify/polaris), which is used to create components in React for Shopify store management itself.

#### Getting Started: `react-js-buy` Repository

Take a look at [this React example built by the Shopify team](https://github.com/Shopify/storefront-api-examples/tree/master/react-js-buy). Most of the code in this tutorial comes from that repository.

…Did you take a look? Good! ?

Now we’re going to hop right into code! Head to your React site’s root folder and install the `shopify-buy` module via the terminal:

```
cd my-awesome-react-project/npm install --save shopify-buy
```

(or `yarn add shopify-buy` if you prefer `yarn`)

Then, in your frontend `index.js`, (NOT `App.js`!) you will need to import `Client` from the JS Buy SDK:

```
import Client from 'shopify-buy';
```

Then add the following configuration object above the `ReactDOM.render()`call:

```
const client = Client.buildClient({    storefrontAccessToken: 'your-access-token',    domain: 'your-shopify-url.myshopify.com'});
```

That’s it for `index.js` for now — we’ll come back to it soon.

Now we’re going to add in all the components needed for a smooth shopping and checkout experience. Copy all the components from the `react-js-buy` repository:

`Cart.js`

`LineItem.js`

`Product.js`

`Products.js`

`VariantSelector.js`

We will paste these components into a`components/shopify/` folder in your `src/` folder. You could put these component files anywhere else in the `src/` folder, if you wished. The rest of the tutorial assumes you have put them in `components/shopify/` .

#### Modifying App.js

`App.js` will need extensive changes. First, import that Cart component you just copied into your own project:

```
import Cart from './components/shopify/Cart';
```

If your `App.js` component was stateless, like mine, you should be safe copying this entire `constructor()` function:

```
constructor() {    super();    this.updateQuantityInCart = this.updateQuantityInCart.bind(this);    this.removeLineItemInCart = this.removeLineItemInCart.bind(this);    this.handleCartClose = this.handleCartClose.bind(this);}
```

If you already have state, copy only those `bind` lines. Those three lines are event handler functions that the Shopify cart needs to function properly.

> “But what about state for the cart!?”

You may ask; or:

> “What about defining those event handlers for the cart!?”

Indeed, that’s coming, but not yet! ?

You can then append the `<Car`t/> component to the bottom of `your re`nder() function, before the ending div.

In my opinion, the cart should be accessible anywhere in your app. I think it makes sense, then, to put the `<Car`t/> component in the root component of your app — in other w`ords,` App.js:

```
return (<div>...<Cart    checkout={this.state.checkout}    isCartOpen={this.state.isCartOpen}    handleCartClose={this.handleCartClose}    updateQuantityInCart={this.updateQuantityInCart}    removeLineItemInCart={this.removeLineItemInCart} /></div>);
```

Again, I haven’t included any code on the event handlers for the cart yet. Additionally, I didn’t address the lack of state components for the cart in App.js.

There is good reason for this.

About halfway through this project, I realized my products component was of course not in my `App.js` file.

Instead, it was buried about three children components down.

So instead of passing products three levels down to children, and then function handlers all the way back up…

I decided to use…

**? Redux!!! ?**

**Ugh! I know, I know, Redux, while not being very difficult, is a pain in the %*$! to wire up initially with all the boilerplate required. But, if you are a developer working on an E-commerce store or an E-commerce store owner, think of it this way: Redux will enable you to access the state of the cart from any component or page in our website or webapp.**

**This ability will be essential as Siren Apparel expands and we develop more products. As we create more products, I’ll make a separate dedicated store page with all products, while leaving just a handful of featured products on the homepage.**

**The ability to access the cart is essential if a user shops around a bit, reads some stories or info about Siren Apparel, and _then_ decides to checkout. It doesn’t matter how much they navigate around, nothing from their cart will be lost!**

**So, in short, I decided it’s probably better to implement Redux now while the codebase for [our site](https://sirenapparel.us) isn’t too large.**

#### **Implementing Redux for Shopify Buy SDK With Bare Minimum Boilerplate**

**Install NPM packages `redux` and `react-redux`:**

**`npm install --save redux react-redux`**

**In `index.js` , import `Provider` from `react-redux` and your `store` from `./store`:**

**`import { Provider } from 'react-redux';`**  
**`import store from './store';`**

**Wrap the `<Provid`er> component with the p`assed` store aroun`d you`r&l`t;App>`;in index.jsto hook up your App to your Redux store:**

**`ReactDOM.render(`**  
**`<Provider store={store}>`**  
    **`<IntlProvider locale={locale} messages={flattenMessages(messages[locale.substring(0, 2)])}>`**  
      **`<App locale={locale}/>`**  
    **`</IntlProvider>`**  
 **`</Provider>,`**  
**`document.getElementById('root')`**  
**`);`**

**(Note that I also have a `<IntlProvid`er>, but that[’s in a different post about how I applied internationalization and localization to dynamically render the content on Siren Apparel’s](https://medium.com/@sirenapparel/internationalization-and-localization-of-sirenapparel-eu-sirenapparel-us-and-sirenapparel-asia-ddee266066a2) site. A different story for a different day.)**

**Now of course we haven’t made a `./store.js` file yet. Create your store in `store.js`in the `src/` root and put this in it:**

**`import {createStore} from 'redux';`**  
**`import reducer from './reducers/cart';export default createStore(reducer);`**

**Create your reducers file in `src/reducers/cart.js` and paste this code:**

**`// initial state`**  
**`const initState = {`**  
  **`isCartOpen: false,`**  
  **`checkout: { lineItems: [] },`**  
  **`products: [],`**  
  **`shop: {}`**  
**`}// actions`**  
**`const CLIENT_CREATED = 'CLIENT_CREATED'`**  
**`const PRODUCTS_FOUND = 'PRODUCTS_FOUND'`**  
**`const CHECKOUT_FOUND = 'CHECKOUT_FOUND'`**  
**`const SHOP_FOUND = 'SHOP_FOUND'`**  
**`const ADD_VARIANT_TO_CART = 'ADD_VARIANT_TO_CART'`**  
**`const UPDATE_QUANTITY_IN_CART = 'UPDATE_QUANTITY_IN_CART'`**  
**`const REMOVE_LINE_ITEM_IN_CART = 'REMOVE_LINE_ITEM_IN_CART'`**  
**`const OPEN_CART = 'OPEN_CART'`**  
**`const CLOSE_CART = 'CLOSE_CART'// reducers`**  
**`export default (state = initState, action) => {`**  
  **`switch (action.type) {`**  
    **`case CLIENT_CREATED:`**  
      **`return {...state, client: action.payload}`**  
    **`case PRODUCTS_FOUND:`**  
      **`return {...state, products: action.payload}`**  
    **`case CHECKOUT_FOUND:`**  
      **`return {...state, checkout: action.payload}`**  
    **`case SHOP_FOUND:`**  
      **`return {...state, shop: action.payload}`**  
    **`case ADD_VARIANT_TO_CART:`**  
      **`return {...state, isCartOpen: action.payload.isCartOpen, checkout: action.payload.checkout}`**  
    **`case UPDATE_QUANTITY_IN_CART:`**  
      **`return {...state, checkout: action.payload.checkout}`**  
    **`case REMOVE_LINE_ITEM_IN_CART:`**  
      **`return {...state, checkout: action.payload.checkout}`**  
    **`case OPEN_CART:`**  
      **`return {...state, isCartOpen: true}`**  
    **`case CLOSE_CART:`**  
      **`return {...state, isCartOpen: false}`**  
    **`default:`**  
      **`return state`**  
  **`}`**  
**`}`**

**Don’t worry, I’m not going to just post this big reducer and not discuss what is going on; we’ll get to each event! There are a few things to note here.**

**We take the initial state from what the state is written as in the Shopify GitHub example and put it in our `initState`, namely the following four parts of state:**

**`isCartOpen: false,`**  
**`checkout: { lineItems: [] },`**  
**`products: [],`**  
**`shop: {}`**

**However, in my implementation, I also create a `client` part of the state. I call the `createClient()` function once and then immediately set it in the Redux state in `index.js` . So let’s head into `index.js`:**

#### **Back to index.js**

**`const client = Client.buildClient({`**  
  **`storefrontAccessToken: 'your-shopify-token',`**  
  **`domain: 'your-shopify-url.myshopify.com'`**  
**`});`**  
**`store.dispatch({type: 'CLIENT_CREATED', payload: client});`**

**In the Shopify buy SDK example, there are a few async calls to get information about the products and store information in React’s `componentWillMount()` function. That example code looks like this:**

**`componentWillMount() {`**  
    **`this.props.client.checkout.create().then((res) => {`**  
      **`this.setState({`**  
        **`checkout: res,`**  
      **`});`**  
    **`});this.props.client.product.fetchAll().then((res) => {`**  
      **`this.setState({`**  
        **`products: res,`**  
      **`});`**  
    **`});this.props.client.shop.fetchInfo().then((res) => {`**  
      **`this.setState({`**  
        **`shop: res,`**  
      **`});`**  
    **`});`**  
  **`}`**

**I opted to do that instead as far upstream of a site load as possible, directly in `index.js`. Then, I issued a corresponding event when each part of the response has been received:**

**`// buildClient() is synchronous, so we can call all these after!`**  
**`client.product.fetchAll().then((res) => {`**  
  **`store.dispatch({type: 'PRODUCTS_FOUND', payload: res});`**  
**`});`**  
**`client.checkout.create().then((res) => {`**  
  **`store.dispatch({type: 'CHECKOUT_FOUND', payload: res});`**  
**`});`**  
**`client.shop.fetchInfo().then((res) => {`**  
  **`store.dispatch({type: 'SHOP_FOUND', payload: res});`**  
**`});`**

**By now the reducer is created, and the initialization of the Shopify API `client` is complete all for `index.js`.**

#### **Back to `App.js`**

**Now in `App.js`, wire up Redux’s store to the App state:**

**`import { connect } from 'react-redux';`**

**and don’t forget to import the store as well:**

**`import store from './store';`**

**At the bottom where `export default App` should be, modify it to this:**

**`export default connect((state) => state)(App);`**

**This connects the Redux state to the `App` component.**

**Now in the `render()` function we are able to access the Redux’s state with Redux’s `getState()` (as apposed to using vanilla react’s `this.state`):**

**`render() {`**  
    **`...`**      
    **`const state = store.getState();`**  
**`}`**

#### **Finally: the Event Handlers (We’re Still in App.js)**

**From above, you know that there are only three event handlers that we need in `App.js`, because the cart uses only three: `updateQuantityInCart`, `removeLineItemInCart`, and `handleCartClose`. The original cart event handlers from the example GitHub repository, which used local component state looked like this:**

**`updateQuantityInCart(lineItemId, quantity) {`**  
  **`const checkoutId = this.state.checkout.id`**  
  **`const lineItemsToUpdate = [{id: lineItemId, quantity: parseInt(quantity, 10)}]return this.props.client.checkout.updateLineItems(checkoutId, lineItemsToUpdate).then(res => {`**  
    **`this.setState({`**  
      **`checkout: res,`**  
    **`});`**  
  **`});`**  
**`}removeLineItemInCart(lineItemId) {`**  
  **`const checkoutId = this.state.checkout.idreturn this.props.client.checkout.removeLineItems(checkoutId, [lineItemId]).then(res => {`**  
    **`this.setState({`**  
      **`checkout: res,`**  
    **`});`**  
  **`});`**  
**`}handleCartClose() {`**  
  **`this.setState({`**  
    **`isCartOpen: false,`**  
  **`});`**  
**`}`**

**We can refactor them to dispatch events to the Redux store as follows:**

**`updateQuantityInCart(lineItemId, quantity) {`**  
    **`const state = store.getState(); // state from redux store`**  
    **`const checkoutId = state.checkout.id`**  
    **`const lineItemsToUpdate = [{id: lineItemId, quantity: parseInt(quantity, 10)}]`**  
    **`state.client.checkout.updateLineItems(checkoutId, lineItemsToUpdate).then(res => {`**  
      **`store.dispatch({type: 'UPDATE_QUANTITY_IN_CART', payload: {checkout: res}});`**  
    **`});`**  
**`}`**  
**`removeLineItemInCart(lineItemId) {`**  
    **`const state = store.getState(); // state from redux store`**  
    **`const checkoutId = state.checkout.id`**  
    **`state.client.checkout.removeLineItems(checkoutId, [lineItemId]).then(res => {`**  
      **`store.dispatch({type: 'REMOVE_LINE_ITEM_IN_CART', payload: {checkout: res}});`**  
    **`});`**  
**`}`**  
**`handleCartClose() {`**  
    **`store.dispatch({type: 'CLOSE_CART'});`**  
**`}`**  
**`handleCartOpen() {`**  
    **`store.dispatch({type: 'OPEN_CART'});`**  
**`}`**

**If you were following along, I already mentioned that I added my own `handleCartOpen` function, because I pass that function down as a prop to my `<Na`v/> component, so a user is able to open and close the cart from a link in the nav. At a future time, I could move that function to the Nav itself instead of passing it as a prop, since of course the Redux store will also be available there!**

#### **Finally Add that <Products/> Component!**

**So, you’ve got a basic store maybe with some simple `href`’s that link to the corresponding product on your Shopify store? Ha! Get rid of those, and replace them with your brand spankin’ new `<Product`s/> component!**

**First, import the component into wherever your store markup should be (remember, in my code base I’ve put the shopify example components in a folder called `shopify/`)**

**This will be wherever your products currently are. (In [the boilerplate repository](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example) I made, I put this in the `GenericProductsPage` component, to signal that this code could be applied to any page that has a products section):**

**`import Products from './shopify/Products';`**

**Now finally, that past 15–20 minutes of redux boilerplate code edits pays off: we can grab the `products` part of our state — not by way of vanilla React state passed down over and over again through props — but through grabbing by way of Redux state, in a neat one liner `const state = store.getState();`:**

**`render () {`**  
    **`const state = store.getState(); // state from redux store`**  
    **`let oProducts = <Products`**  
      **`products={state.products}`**  
      **`client={state.client}`**  
      **`addVariantToCart={this.addVariantToCart}`**  
    **`/>;`**

**Don’t forget to drop the component itself into where it should go in your `render()` function. For me, that location was buried in Bootstrap style classes and HTML:**

**`...`**  
**`<div className="service-content-one">`**  
    **`<div className="row">`**  
        **`<Products/>`**  
    **`</div>{/*/.row*/}`**  
**`</div>{/*/.service-content-one*/}`**  
**`...`**

**Finally, we will need a single event function `addVariantToCart` for the cart to work with this products component. Again, for reference, here is the original, vanilla React local `state` version of `addVariantToCart`(again, from the shopify example repository):**

**`addVariantToCart(variantId, quantity){`**  
  **`this.setState({`**  
    **`isCartOpen: true,`**  
  **`});const lineItemsToAdd = [{variantId, quantity: parseInt(quantity, 10)}]`**  
  **`const checkoutId = this.state.checkout.idreturn this.props.client.checkout.addLineItems(checkoutId, lineItemsToAdd).then(res => {`**  
    **`this.setState({`**  
      **`checkout: res,`**  
    **`});`**  
  **`});`**  
**`}`**

**and the new, Redux-friendly `store.dispatch()` version:**

**`addVariantToCart(variantId, quantity) {`**  
    **`const state = store.getState(); // state from redux store`**  
    **`const lineItemsToAdd = [{variantId, quantity: parseInt(quantity, 10)}]`**  
    **`const checkoutId = state.checkout.id`**  
    **`state.client.checkout.addLineItems(checkoutId, lineItemsToAdd).then(res => {`**  
      **`store.dispatch({type: 'ADD_VARIANT_TO_CART', payload: {isCartOpen: true, checkout: res}});`**  
    **`});`**  
**`}`**

**which is of course the one we will use. ?**

**Don’t forget to bind it in the constructor:**

**`this.addVariantToCart = this.addVariantToCart.bind(this);`**

**Also, you’ll need to connect this component to the store like you did `App.js` , and import the store:**

**`import { connect } from 'react-redux'`**  
**`import store from '../store';`**

**at the top, and (assuming the component where you put the Shopify `Product` component name is `GenericProductPage`:**

**`export default connect((state) => state)(GenericProductsPage);`**

**at the bottom.**

**Great! Now, no matter how deeply buried in components, or wherever your products component is declared, it can communicate with the cart’s state!**

#### **Final BONUS Example: Cart in Your Header or Nav**

**If you want to have a ‘Cart’ button in your header / nav, add this button in your Nav component’s render function (again, an example from my current site, which has Bootstrap styles — a very simple version is in the [boilerplate example](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example):**

**`<div className="App__view-cart-wrapper">`**  
**`<button className="App__view-cart" onClick={this.props.handleCartOpen}>`**  
    **`Cart`**  
    **`</button>`**  
**`</div>`**

**where `handleCartOpen` is a new handler method you’ll have to add to `App.js`:**

**`constructor() {`**  
  **`super();`**  
  **`...`**  
  **`this.handleCartOpen = this.handleCartOpen.bind(this);`**  
  **`...`**  
**`}`**

**in the constructor. Then when you are referencing your Nav component in App.js (or wherever you place your Nav) you pass the function handler:**

**`<Nav handleCartOpen={this.handleCartOpen}/>`**

**This could also be refactored to an event in Redux, but since it was only one child down, I did it the vanilla React way.**

#### **Styling Component(s)**

**I relied on Shopify’s CSS file, `app.css`, located in the `shared/` folder in the `storefront-api-example` repository (you can’t miss it, it’s the only file in `shared/` )!**

**Make sure to copy that into your `styles/` folder or wherever it needs to be and include it in your `index.js` file. In my `index.js` it looks like this:**

**`import './styles/shopify.css';`**

**Since I renamed the `app.css` which was in the Shopify example repository to `shopify.css` , and put it folder `styles`. This convention is also used in the boilerplate repository code.**

**From here it’s pretty easy to identify where exactly in `shopify.css` the default bright blue color for the buttons is defined, and so on. I’m going to save detailed CSS customization for you to handle. ?**

**But who knows, maybe I’ll post on that eventually — but I find the styles from Shopify pretty good and easy enough to modify.**

#### **Takeaways**

**In my opinion, this is a perfect (non-todo list ?) use of Redux. Redux cleanly organizes the event functions and state of the Shopify cart and makes it easy to access the cart’s state from any other component. This is much easier to maintain than passing pieces of state to children and using multiple event handlers to pass events back up to parent functions all over a React app.**

**As shown as an example in the tutorial, the cart’s state is accessed easily in the Nav component and the shop section of the front page. I’ll also be able to easily add it to a sort of ‘featured’ product section as well, once Siren Apparel is ready for that.**

#### **Find the Code**

**A boilerplate repository of this implementation [can be found here](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example). It is a near blank `create-react-app` app, but with all the changes of this tutorial implemented in `index.js` and `App.js` , as well as a super basic `GenericStorePage` and `Nav` components.**

**I built the code on the repo while re-reading and updating my own tutorial here, to make sure this tutorial makes sense!**

**Because I am crazy ?, Siren Apparel’s website is all open-sourced. So if you want to fool around with my implementation, c[heck out the repository!](https://github.com/frewinchristopher/sirenapparel.us)**

**I hope you enjoyed this tutorial! If anything isn’t clear or just plain not working, let me know! I’ll try to assist you!**

**Thanks to [Lisa Catalano](http://css-snippets.com/author/lisa/) at CSS-Snippets for [the simple Nav example](http://css-snippets.com/simple-horizontal-navigation/#code) which I used in the boilerplate repository!**

**Cheers! ?**

**Chris**

