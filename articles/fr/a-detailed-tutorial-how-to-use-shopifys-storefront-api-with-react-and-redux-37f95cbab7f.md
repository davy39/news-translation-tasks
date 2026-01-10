---
title: 'Un tutoriel détaillé : comment utiliser l''API Storefront de Shopify avec
  React et Redux'
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
seo_title: 'Un tutoriel détaillé : comment utiliser l''API Storefront de Shopify avec
  React et Redux'
seo_desc: 'By Chris Frewin

  E-commerce for all! (…websites, that is ?)

  Written by Chris August 2018, updated November, 2018


  _Courtesy of Negative Space on [pexels.com](https://www.pexels.com/photo/grayscale-photo-of-computer-laptop-near-white-notebook-and-ceram...'
---

Par Chris Frewin

#### L'e-commerce pour tous ! (…enfin, pour les sites web ?)

_Écrit par [Chris](https://medium.com/@frewin.christopher) en août 2018, mis à jour en novembre 2018_

![Image](https://cdn-media-1.freecodecamp.org/images/QjOaB1iMaaTA4wYVDOKhmtNyjYnzcm-DDxjd)
_Avec l'aimable autorisation de Negative Space sur [pexels.com](https://www.pexels.com/photo/grayscale-photo-of-computer-laptop-near-white-notebook-and-ceramic-mug-on-table-169573/" rel="noopener" target="_blank" title=")_

#### Contexte et motivation

La motivation ici était assez simple. Je voulais que les visiteurs de mon site puissent parcourir, rechercher et sélectionner des produits directement sur mon domaine personnalisé sans avoir à se rendre sur notre site Shopify.

La motivation secondaire est que je préfère de loin avoir ma propre base de code pour un site web plutôt que d'utiliser l'un des modèles d'usine de Shopify. Sans offense pour l'équipe Shopify ! Les modèles sont modernes et propres, mais ils sont plutôt basiques. Je suis sûr que ces modèles sont hautement personnalisables, mais ce n'est pas une pile technologique que je connais pour le moment.

C'est donc le meilleur des deux mondes — mon site React personnalisé (déjà construit et en ligne ?), avec l'API et le processus de paiement de Shopify en plus !

À la fin de ce tutoriel, vous serez en mesure d'ajouter vos produits Shopify sur _n'importe quelle_ page de votre site. La seule partie du processus d'achat qui se déroulera sur Shopify est le moment où l'utilisateur clique sur « Checkout » (Paiement).

J'ai également créé [un dépôt de boilerplate vide](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example) pour ce tutoriel.

La motivation spécifique pour écrire ici sur Medium était simplement que je ne parvenais pas à trouver de tutoriel sur ce processus moi-même — j'ai donc décidé d'en créer un !

Je suis développeur professionnel depuis 4 ans maintenant, et je programme depuis 7 ans. J'ai travaillé sur des piles technologiques allant du Fortran et du Perl à l'ancienne, jusqu'à React, Javascript, Python et Node.

Siren Apparel est l'un de mes projets parallèles / startup / entreprises de créateur que je dirige depuis 5 ans maintenant, et nous avons fait des dons à 5 services de police et de pompiers différents jusqu'à présent !

Commençons enfin ce tutoriel.

#### L'API Storefront de Shopify

Les formidables équipes de Shopify ont mis au point l'[API Storefront](https://help.shopify.com/en/api/custom-storefronts/storefront-api). Avec l'API Storefront, vous pouvez créer des composants React pour ajouter des photos de produits, des variantes de produits, des tailles de produits, un panier, ainsi que des boutons « ajouter au panier » et « paiement » dans votre propre site non-Shopify.

*Notez que ce tutoriel ne concerne PAS [Shopify Polaris](https://github.com/Shopify/polaris), qui est utilisé pour créer des composants en React pour la gestion de la boutique Shopify elle-même.

#### Premiers pas : le dépôt `react-js-buy` 

Jetez un œil à [cet exemple React construit par l'équipe Shopify](https://github.com/Shopify/storefront-api-examples/tree/master/react-js-buy). La majeure partie du code de ce tutoriel provient de ce dépôt.

…Vous avez jeté un œil ? Bien ! ?

Maintenant, nous allons plonger directement dans le code ! Rendez-vous dans le dossier racine de votre site React et installez le module `shopify-buy` via le terminal :

```
cd my-awesome-react-project/npm install --save shopify-buy
```

(ou `yarn add shopify-buy` si vous préférez `yarn`)

Ensuite, dans votre `index.js` frontend (PAS `App.js` !), vous devrez importer `Client` depuis le SDK JS Buy :

```
import Client from 'shopify-buy';
```

Ajoutez ensuite l'objet de configuration suivant au-dessus de l'appel `ReactDOM.render()` :

```
const client = Client.buildClient({    storefrontAccessToken: 'your-access-token',    domain: 'your-shopify-url.myshopify.com'});
```

C'est tout pour `index.js` pour le moment — nous y reviendrons bientôt.

Nous allons maintenant ajouter tous les composants nécessaires pour une expérience d'achat et de paiement fluide. Copiez tous les composants du dépôt `react-js-buy` :

`Cart.js`

`LineItem.js`

`Product.js`

`Products.js`

`VariantSelector.js`

Nous collerons ces composants dans un dossier `components/shopify/` dans votre dossier `src/`. Vous pourriez placer ces fichiers de composants n'importe où ailleurs dans le dossier `src/`, si vous le souhaitiez. Le reste du tutoriel suppose que vous les avez placés dans `components/shopify/` .

#### Modification de App.js

`App.js` nécessitera des modifications importantes. Tout d'abord, importez ce composant Cart que vous venez de copier dans votre propre projet :

```
import Cart from './components/shopify/Cart';
```

Si votre composant `App.js` était sans état (stateless), comme le mien, vous devriez pouvoir copier toute cette fonction `constructor()` sans risque :

```
constructor() {    super();    this.updateQuantityInCart = this.updateQuantityInCart.bind(this);    this.removeLineItemInCart = this.removeLineItemInCart.bind(this);    this.handleCartClose = this.handleCartClose.bind(this);}
```

Si vous avez déjà un état, ne copiez que ces lignes `bind`. Ces trois lignes sont des fonctions de gestion d'événements dont le panier Shopify a besoin pour fonctionner correctement.

> « Mais qu'en est-il de l'état du panier !? »

Pourriez-vous demander ; ou :

> « Qu'en est-il de la définition de ces gestionnaires d'événements pour le panier !? »

En effet, cela arrive, mais pas encore ! ?

Vous pouvez ensuite ajouter le composant `<Cart/>` au bas de votre fonction `render()`, avant la balise div de fermeture.

À mon avis, le panier devrait être accessible n'importe où dans votre application. Je pense qu'il est donc logique de placer le composant `<Cart/>` dans le composant racine de votre application — en d'autres termes, `App.js` :

```
return (<div>...<Cart    checkout={this.state.checkout}    isCartOpen={this.state.isCartOpen}    handleCartClose={this.handleCartClose}    updateQuantityInCart={this.updateQuantityInCart}    removeLineItemInCart={this.removeLineItemInCart} /></div>);
```

Encore une fois, je n'ai pas encore inclus de code sur les gestionnaires d'événements pour le panier. De plus, je n'ai pas abordé l'absence de composants d'état pour le panier dans App.js.

Il y a une bonne raison à cela.

À mi-chemin de ce projet, j'ai réalisé que mon composant de produits n'était bien sûr pas dans mon fichier `App.js`.

Au lieu de cela, il était enfoui environ trois composants enfants plus bas.

Alors, au lieu de transmettre les produits sur trois niveaux aux enfants, puis les gestionnaires de fonctions tout au long de la remontée…

J'ai décidé d'utiliser…

**? Redux !!! ?**

**Argh ! Je sais, je sais, Redux, bien que n'étant pas très difficile, est une corvée à câbler initialement avec tout le boilerplate requis. Mais, si vous êtes un développeur travaillant sur une boutique e-commerce ou un propriétaire de boutique e-commerce, voyez les choses ainsi : Redux vous permettra d'accéder à l'état du panier depuis n'importe quel composant ou page de notre site web ou application web.**

**Cette capacité sera essentielle à mesure que Siren Apparel se développe et que nous concevons plus de produits. Au fur et à mesure que nous créerons plus de produits, je ferai une page de boutique dédiée séparée avec tous les produits, tout en laissant juste une poignée de produits vedettes sur la page d'accueil.**

**La possibilité d'accéder au panier est essentielle si un utilisateur fait un peu de shopping, lit quelques histoires ou informations sur Siren Apparel, et décide _ensuite_ de passer au paiement. Peu importe sa navigation, rien de son panier ne sera perdu !**

**En résumé, j'ai décidé qu'il était probablement préférable d'implémenter Redux maintenant, tant que la base de code de [notre site](https://sirenapparel.us) n'est pas trop volumineuse.**

#### **Implémentation de Redux pour le SDK Shopify Buy avec le strict minimum de boilerplate**

**Installez les packages NPM `redux` et `react-redux` :**

**`npm install --save redux react-redux`**

**Dans `index.js`, importez `Provider` de `react-redux` et votre `store` depuis `./store` :**

**`import { Provider } from 'react-redux';`**  
**`import store from './store';`**

**Enveloppez le composant `<Provider>` avec le store transmis autour de votre `<App>` dans index.js pour connecter votre application à votre store Redux :**

**`ReactDOM.render(`**  
**`<Provider store={store}>`**  
    **`<IntlProvider locale={locale} messages={flattenMessages(messages[locale.substring(0, 2)])}>`**  
      **`<App locale={locale}/>`**  
    **`</IntlProvider>`**  
 **`</Provider>,`**  
**`document.getElementById('root')`**  
**`);`**

**(Notez que j'ai également un `<IntlProvider>`, mais cela [fait l'objet d'un autre article sur la façon dont j'ai appliqué l'internationalisation et la localisation pour rendre dynamiquement le contenu sur le site de Siren Apparel](https://medium.com/@sirenapparel/internationalization-and-localization-of-sirenapparel-eu-sirenapparel-us-and-sirenapparel-asia-ddee266066a2). Une autre histoire pour un autre jour.)**

**Maintenant, bien sûr, nous n'avons pas encore créé de fichier `./store.js`. Créez votre store dans `store.js` à la racine de `src/` et mettez-y ceci :**

**`import {createStore} from 'redux';`**  
**`import reducer from './reducers/cart';export default createStore(reducer);`**

**Créez votre fichier de réducteurs dans `src/reducers/cart.js` et collez ce code :**

**`// état initial`**  
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
**`const CLOSE_CART = 'CLOSE_CART'// réducteurs`**  
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

**Ne vous inquiétez pas, je ne vais pas me contenter de poster ce gros réducteur sans discuter de ce qui s'y passe ; nous aborderons chaque événement ! Il y a quelques points à noter ici.**

**Nous prenons l'état initial tel qu'il est écrit dans l'exemple GitHub de Shopify et nous le mettons dans notre `initState`, à savoir les quatre parties suivantes de l'état :**

**`isCartOpen: false,`**  
**`checkout: { lineItems: [] },`**  
**`products: [],`**  
**`shop: {}`**

**Cependant, dans mon implémentation, je crée également une partie `client` de l'état. J'appelle la fonction `createClient()` une fois, puis je la définis immédiatement dans l'état Redux dans `index.js`. Dirigeons-nous donc vers `index.js` :**

#### **Retour à index.js**

**`const client = Client.buildClient({`**  
  **`storefrontAccessToken: 'your-shopify-token',`**  
  **`domain: 'your-shopify-url.myshopify.com'`**  
**`});`**  
**`store.dispatch({type: 'CLIENT_CREATED', payload: client});`**

**Dans l'exemple du SDK Shopify buy, il y a quelques appels asynchrones pour obtenir des informations sur les produits et stocker les informations dans la fonction `componentWillMount()` de React. Ce code d'exemple ressemble à ceci :**

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

**J'ai choisi de faire cela le plus en amont possible du chargement du site, directement dans `index.js`. Ensuite, j'ai émis un événement correspondant lorsque chaque partie de la réponse a été reçue :**

**`// buildClient() est synchrone, nous pouvons donc appeler tout cela après !`**  
**`client.product.fetchAll().then((res) => {`**  
  **`store.dispatch({type: 'PRODUCTS_FOUND', payload: res});`**  
**`});`**  
**`client.checkout.create().then((res) => {`**  
  **`store.dispatch({type: 'CHECKOUT_FOUND', payload: res});`**  
**`});`**  
**`client.shop.fetchInfo().then((res) => {`**  
  **`store.dispatch({type: 'SHOP_FOUND', payload: res});`**  
**`});`**

**À présent, le réducteur est créé et l'initialisation du `client` de l'API Shopify est terminée pour `index.js`.**

#### **Retour à `App.js`**

**Maintenant, dans `App.js`, connectez le store de Redux à l'état de l'application :**

**`import { connect } from 'react-redux';`**

**et n'oubliez pas d'importer également le store :**

**`import store from './store';`**

**En bas, là où `export default App` devrait se trouver, modifiez-le comme suit :**

**`export default connect((state) => state)(App);`**

**Cela connecte l'état Redux au composant `App`.**

**Maintenant, dans la fonction `render()`, nous pouvons accéder à l'état de Redux avec `getState()` de Redux (par opposition à l'utilisation du `this.state` de React classique) :**

**`render() {`**  
    **`...`**      
    **`const state = store.getState();`**  
**`}`**

#### **Enfin : les gestionnaires d'événements (nous sommes toujours dans App.js)**

**Comme vu plus haut, vous savez qu'il n'y a que trois gestionnaires d'événements dont nous avons besoin dans `App.js`, car le panier n'en utilise que trois : `updateQuantityInCart`, `removeLineItemInCart` et `handleCartClose`. Les gestionnaires d'événements originaux du panier provenant du dépôt GitHub d'exemple, qui utilisaient l'état local du composant, ressemblaient à ceci :**

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

**Nous pouvons les refactoriser pour distribuer (dispatch) des événements au store Redux comme suit :**

**`updateQuantityInCart(lineItemId, quantity) {`**  
    **`const state = store.getState(); // état du store redux`**  
    **`const checkoutId = state.checkout.id`**  
    **`const lineItemsToUpdate = [{id: lineItemId, quantity: parseInt(quantity, 10)}]`**  
    **`state.client.checkout.updateLineItems(checkoutId, lineItemsToUpdate).then(res => {`**  
      **`store.dispatch({type: 'UPDATE_QUANTITY_IN_CART', payload: {checkout: res}});`**  
    **`});`**  
**`}`**  
**`removeLineItemInCart(lineItemId) {`**  
    **`const state = store.getState(); // état du store redux`**  
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

**Si vous suiviez, j'ai déjà mentionné que j'avais ajouté ma propre fonction `handleCartOpen`, car je transmets cette fonction en tant que prop à mon composant `<Nav/>`, afin qu'un utilisateur puisse ouvrir et fermer le panier à partir d'un lien dans la navigation. À l'avenir, je pourrais déplacer cette fonction vers le Nav lui-même au lieu de la transmettre en tant que prop, puisque bien sûr le store Redux y sera également disponible !**

#### **Ajoutez enfin ce composant <Products/> !**

**Alors, vous avez une boutique de base peut-être avec quelques simples `href` qui pointent vers le produit correspondant sur votre boutique Shopify ? Ha ! Débarrassez-vous-en et remplacez-les par votre tout nouveau composant `<Products/>` !**

**Tout d'abord, importez le composant là où le balisage de votre boutique doit se trouver (rappelez-vous, dans ma base de code, j'ai mis les composants d'exemple Shopify dans un dossier appelé `shopify/`)**

**Ce sera là où se trouvent actuellement vos produits. (Dans [le dépôt de boilerplate](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example) que j'ai créé, j'ai mis cela dans le composant `GenericProductsPage`, pour signaler que ce code pourrait être appliqué à n'importe quelle page ayant une section de produits) :**

**`import Products from './shopify/Products';`**

**Maintenant, enfin, ces 15 à 20 dernières minutes de modifications de code boilerplate Redux portent leurs fruits : nous pouvons récupérer la partie `products` de notre état — non pas par le biais de l'état React classique transmis encore et encore via des props — mais en la récupérant via l'état Redux, en une seule ligne propre `const state = store.getState();` :**

**`render () {`**  
    **`const state = store.getState(); // état du store redux`**  
    **`let oProducts = <Products`**  
      **`products={state.products}`**  
      **`client={state.client}`**  
      **`addVariantToCart={this.addVariantToCart}`**  
    **`/>;`**

**N'oubliez pas d'insérer le composant lui-même là où il doit aller dans votre fonction `render()`. Pour moi, cet emplacement était enfoui dans des classes de style Bootstrap et du HTML :**

**`...`**  
**`<div className="service-content-one">`**  
    **`<div className="row">`**  
        **`<Products/>`**  
    **`</div>{/*/.row*/}`**  
**`</div>{/*/.service-content-one*/}`**  
**`...`**

**Enfin, nous aurons besoin d'une seule fonction d'événement `addVariantToCart` pour que le panier fonctionne avec ce composant de produits. Encore une fois, pour référence, voici la version originale avec l'état local (`state`) React classique de `addVariantToCart` (toujours d'après le dépôt d'exemple Shopify) :**

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

**et la nouvelle version compatible Redux avec `store.dispatch()` :**

**`addVariantToCart(variantId, quantity) {`**  
    **`const state = store.getState(); // état du store redux`**  
    **`const lineItemsToAdd = [{variantId, quantity: parseInt(quantity, 10)}]`**  
    **`const checkoutId = state.checkout.id`**  
    **`state.client.checkout.addLineItems(checkoutId, lineItemsToAdd).then(res => {`**  
      **`store.dispatch({type: 'ADD_VARIANT_TO_CART', payload: {isCartOpen: true, checkout: res}});`**  
    **`});`**  
**`}`**

**qui est bien sûr celle que nous utiliserons. ?**

**N'oubliez pas de le lier (bind) dans le constructeur :**

**`this.addVariantToCart = this.addVariantToCart.bind(this);`**

**De plus, vous devrez connecter ce composant au store comme vous l'avez fait pour `App.js`, et importer le store :**

**`import { connect } from 'react-redux'`**  
**`import store from '../store';`**

**en haut, et (en supposant que le composant où vous avez mis le composant Shopify `Product` s'appelle `GenericProductPage`) :**

**`export default connect((state) => state)(GenericProductsPage);`**

**en bas.**

**Génial ! Désormais, peu importe à quel point il est enfoui dans les composants, ou l'endroit où votre composant de produits est déclaré, il peut communiquer avec l'état du panier !**

#### **Exemple BONUS final : Le panier dans votre en-tête ou navigation**

**Si vous voulez avoir un bouton « Panier » dans votre en-tête / navigation, ajoutez ce bouton dans la fonction de rendu de votre composant Nav (encore une fois, un exemple de mon site actuel, qui a des styles Bootstrap — une version très simple se trouve dans l'[exemple de boilerplate](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example) :**

**`<div className="App__view-cart-wrapper">`**  
**`<button className="App__view-cart" onClick={this.props.handleCartOpen}>`**  
    **`Cart`**  
    **`</button>`**  
**`</div>`**

**où `handleCartOpen` est une nouvelle méthode de gestion que vous devrez ajouter à `App.js` :**

**`constructor() {`**  
  **`super();`**  
  **`...`**  
  **`this.handleCartOpen = this.handleCartOpen.bind(this);`**  
  **`...`**  
**`}`**

**dans le constructeur. Ensuite, lorsque vous référencez votre composant Nav dans App.js (ou partout où vous placez votre Nav), vous transmettez le gestionnaire de fonction :**

**`<Nav handleCartOpen={this.handleCartOpen}/>`**

**Cela pourrait également être refactorisé en un événement dans Redux, mais comme il n'y avait qu'un seul niveau d'enfant, je l'ai fait à la manière de React classique.**

#### **Stylisation du ou des composants**

**Je me suis appuyé sur le fichier CSS de Shopify, `app.css`, situé dans le dossier `shared/` du dépôt `storefront-api-example` (vous ne pouvez pas le manquer, c'est le seul fichier dans `shared/`) !**

**Assurez-vous de le copier dans votre dossier `styles/` ou là où il doit être et de l'inclure dans votre fichier `index.js`. Dans mon `index.js`, cela ressemble à ceci :**

**`import './styles/shopify.css';`**

**Puisque j'ai renommé le fichier `app.css` qui se trouvait dans le dépôt d'exemple Shopify en `shopify.css`, et que je l'ai mis dans le dossier `styles`. Cette convention est également utilisée dans le code du dépôt de boilerplate.**

**À partir de là, il est assez facile d'identifier où exactement dans `shopify.css` la couleur bleu vif par défaut des boutons est définie, et ainsi de suite. Je vous laisse le soin de gérer la personnalisation détaillée du CSS. ?**

**Mais qui sait, je posterai peut-être là-dessus un jour — mais je trouve les styles de Shopify plutôt bons et assez faciles à modifier.**

#### **Points à retenir**

**À mon avis, c'est une utilisation parfaite de Redux (qui n'est pas une liste de tâches ?). Redux organise proprement les fonctions d'événement et l'état du panier Shopify et facilite l'accès à l'état du panier depuis n'importe quel autre composant. C'est beaucoup plus facile à maintenir que de transmettre des morceaux d'état aux enfants et d'utiliser plusieurs gestionnaires d'événements pour faire remonter les événements aux fonctions parentes partout dans une application React.**

**Comme le montre l'exemple du tutoriel, l'état du panier est facilement accessible dans le composant Nav et la section boutique de la page d'accueil. Je pourrai également l'ajouter facilement à une sorte de section de produits « vedettes », une fois que Siren Apparel sera prêt pour cela.**

#### **Trouver le code**

**Un dépôt de boilerplate de cette implémentation [peut être trouvé ici](https://github.com/frewinchristopher/react-redux-shopify-storefront-api-example). Il s'agit d'une application `create-react-app` presque vide, mais avec toutes les modifications de ce tutoriel implémentées dans `index.js` et `App.js`, ainsi que des composants `GenericStorePage` et `Nav` super basiques.**

**J'ai construit le code sur le dépôt tout en relisant et en mettant à jour mon propre tutoriel ici, pour m'assurer que ce tutoriel est logique !**

**Parce que je suis fou ?, le site web de Siren Apparel est entièrement open-source. Donc, si vous voulez vous amuser avec mon implémentation, [consultez le dépôt !](https://github.com/frewinchristopher/sirenapparel.us)**

**J'espère que vous avez apprécié ce tutoriel ! Si quelque chose n'est pas clair ou ne fonctionne tout simplement pas, faites-le moi savoir ! J'essaierai de vous aider !**

**Merci à [Lisa Catalano](http://css-snippets.com/author/lisa/) de CSS-Snippets pour [l'exemple simple de Nav](http://css-snippets.com/simple-horizontal-navigation/#code) que j'ai utilisé dans le dépôt de boilerplate !**

**Santé ! ?**

**Chris**