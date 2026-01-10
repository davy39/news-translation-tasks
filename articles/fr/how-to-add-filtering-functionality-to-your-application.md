---
title: Comment ajouter une fonctionnalité de filtrage à vos applications
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
seo_title: Comment ajouter une fonctionnalité de filtrage à vos applications
seo_desc: 'Suppose you have an application where you want to filter the data based
  on some criteria like size, color, price, and so on.

  In this article, we will see how you can do that.

  So let''s get started.

  Initial Setup

  Let''s say we have the following list of...'
---

Supposons que vous avez une application où vous souhaitez filtrer les données en fonction de certains critères comme `size`, `color`, `price`, et ainsi de suite.

Dans cet article, nous verrons comment vous pouvez faire cela.

Alors, commençons.

## Installation initiale

Disons que nous avons la liste suivante de produits :

```js
const products = [
  { name: 'Macbook Air', price: '180000', ram: 16 },
  { name: 'Samsung Galaxy M21', price: '13999', ram: 4 },
  { name: 'Redmi Note 9', price: '11999', ram: 4 },
  { name: 'OnePlus 8T 5G', price: '45999', ram: 12 }
];
```

et pour le filtrage, nous avons deux menus déroulants – un pour le tri par divers critères comme `price` et `ram`, et l'autre menu déroulant pour l'ordre de tri comme `descending` ou `ascending` comme montré ci-dessous :

```html
<div class="filters">
  <div>
    Trier par :
    <select class="sort-by">
      <option value="">Sélectionnez une option</option>
      <option value="price">Prix</option>
      <option value="ram">Ram</option>
    </select>
  </div>
  <div>
    Ordre de tri :
    <select class="sort-order">
      <option value="">Sélectionnez une option</option>
      <option value="asc">Ascendant</option>
      <option value="desc">Descendant</option>
    </select>
  </div>
</div>

<div class="products"></div>
```

## Comment afficher les produits sur l'interface utilisateur

Ajoutons une fonction `displayProducts` qui affichera les produits sur l'interface utilisateur.

```js
const container = document.querySelector(".products");

const displayProducts = (products) => {
  let result = "";

  products.forEach(({ name, price, ram }) => {
    result += `
     <div class="product">
      <div><strong>Nom :</strong><span>${name}</span></div>
      <div><strong>Prix :</strong><span>${price}</div>
      <div><strong>Ram :</strong><span>${ram} GB</div>
     </div>
    `;
  });

  container.innerHTML = result;
};

displayProducts(products);
```

La fonction `displayProducts` dans le code ci-dessus parcourt le tableau `products` en utilisant la méthode `forEach` du tableau. Elle génère du HTML qui sera affiché en utilisant la syntaxe de littéral de gabarit ES6 et l'insère dans la div `products`.

Comme nous passons le tableau d'objets à la fonction `displayProducts`, nous utilisons la syntaxe de déstructuration ES6 pour la fonction de rappel de la boucle `forEach` afin d'obtenir `name`, `price` et `ram`.

Voici une [démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/LYZaaqQ).

Votre écran initial ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/filter_initial.png)

## Comment ajouter la fonctionnalité de filtrage

Maintenant, ajoutons la fonctionnalité de filtrage.

Pour gérer un événement onchange du menu déroulant `Trier par`, nous ajouterons un gestionnaire d'événements pour cela.

```js
sortByDropdown.addEventListener('change', () => {
  // du code
};
```

Nous avons déjà défini la référence de tous les éléments requis en haut dans le Code Pen ci-dessus comme montré ci-dessous :

```js
const sortByDropdown = document.querySelector(".sort-by");
const sortOrderDropdown = document.querySelector(".sort-order");
const container = document.querySelector(".products");
```

Maintenant, ajoutons la logique de tri :

```js
sortByDropdown.addEventListener("change", () => {
  const sortByValue = sortByDropdown.value; // valeur de price ou ram
  const sortOrderValue = sortOrderDropdown.value; // valeur asc ou desc

  const sorted =
    sortOrderValue === "desc"
      ? descendingSort(sortByValue)
      : ascendingSort(sortByValue);

  displayProducts(sorted);
});
```

Ici, nous vérifions la valeur du deuxième menu déroulant. Si c'est `desc`, nous appelons la fonction `descendingSort` (que nous devons encore définir). Sinon, nous appelons la fonction `ascendingSort` en passant la valeur du premier menu déroulant pour trier par `price` ou `ram`.

Ensuite, nous passons ce résultat à la fonction `displayProducts` pour qu'elle mette à jour l'interface utilisateur avec ces produits triés.

## Comment ajouter la fonctionnalité de tri

Maintenant, ajoutons les fonctions `descendingSort` et `ascendingSort`.

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

Ici, nous utilisons la fonction de comparaison pour la fonction de tri de tableau.

Comme vous le savez, si nous avons un objet comme ceci :

```js
const product = { name: 'Macbook Air', price: '180000', ram: 16 };
```

alors nous pouvons accéder à ses propriétés de deux manières :

1. en utilisant `product.name`
2. en utilisant `product['name']`

Comme nous avons une valeur dynamique de la variable `sortByValue`, nous utilisons la deuxième manière à l'intérieur de la fonction `sort` pour obtenir la valeur du produit (`a[sortByValue]` ou `b[sortByValue]`).

### Comment fonctionne le tri par ordre ascendant

* Si la première valeur à comparer est alphabétiquement avant la deuxième valeur, une valeur négative est retournée.
* Si la première valeur à comparer est alphabétiquement après la deuxième valeur, une valeur positive est retournée.
* Si les première et deuxième valeurs sont égales, zéro est retourné, ce qui triera automatiquement le tableau par ordre ascendant.

### Comment fonctionne le tri par ordre descendant

* Si la première valeur à comparer est alphabétiquement avant la deuxième valeur, une valeur positive est retournée.
* Si la première valeur à comparer est alphabétiquement après la deuxième valeur, une valeur négative est retournée.
* Si les première et deuxième valeurs sont égales, zéro est retourné, ce qui triera automatiquement le tableau par ordre descendant.

> Si vous n'êtes pas familier avec le fonctionnement du tri pour la fonction de comparaison, consultez [cet article](https://levelup.gitconnected.com/array-sort-method-and-its-gotchas-5859ece92e8d?source=friends_link&sk=ad7f5a1b2a301517367783dc543ed908) pour mieux comprendre tout sur le tri en JavaScript.

Maintenant, nous voulons déclencher la fonctionnalité de tri lorsque nous changeons le menu déroulant de l'ordre de tri. Alors, ajoutons un gestionnaire d'événements pour cela également.

```js
sortOrderDropdown.addEventListener("change", () => {
  const event = new Event("change");
  const sortByValue = sortByDropdown.value;

  if (sortByValue) {
    sortByDropdown.dispatchEvent(event);
  }
});
```

Ici, nous avons ajouté la condition `if` car nous ne voulons pas trier les produits lorsque le menu déroulant de tri n'est pas sélectionné.

Voici une [démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/vYKPPwV).

Consultez la démonstration de la fonctionnalité ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/manual_filter.gif)

## Comment utiliser Lodash pour simplifier le code de tri

Si vous ne voulez pas écrire votre propre logique de tri, vous pouvez utiliser la méthode `orderBy` fournie par [lodash](https://lodash.com/) qui est une bibliothèque d'utilitaires très populaire.

> Si vous n'êtes pas familier avec lodash et les fonctions puissantes fournies par la bibliothèque, consultez [cet article](https://levelup.gitconnected.com/extremely-useful-lodash-methods-b38f121fea7e?source=friends_link&sk=558db260b096e7592e02bd328982c0a4) pour une introduction à ses diverses méthodes utiles.

Ajoutons la méthode `orderBy` lors du changement du menu déroulant de tri comme ceci :

```js
sortByDropdown.addEventListener("change", () => {
  const sortByValue = sortByDropdown.value; // valeur de price ou ram
  const sortOrderValue = sortOrderDropdown.value; // valeur asc ou desc

  const sorted = _.orderBy(products, [sortByValue], sortOrderValue);

  displayProducts(sorted);
});
```

et supprimons les fonctions `ascendingSort` et `descendingSort`.

Pour la méthode `orderBy`, nous avons fourni

* le tableau à trier comme premier paramètre
* la propriété de l'objet sur laquelle nous devons trier (`price` ou `ram`) comme deuxième paramètre
* l'ordre de tri (`asc` ou `desc`) comme troisième paramètre

Voici une [démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/MWexdJP?editors=0010).

Avec cette méthode `orderBy` de lodash, la fonctionnalité fonctionne exactement comme avant. La seule différence est que nous n'avons pas à écrire la logique de tri.

### **Merci d'avoir lu !**

Vous voulez apprendre toutes les fonctionnalités ES6+ en détail, y compris `let` et `const`, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export et bien plus encore ?

Consultez mon livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/?coupon=LA1HR55). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.

De plus, consultez mon cours **gratuit** [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

**Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**