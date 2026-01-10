---
title: Comment utiliser les Props dans React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-20T20:16:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-props-in-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/How-to-use-props-in-reactjs.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les Props dans React.js
seo_desc: "By Joy O. Oluwafemi\nProps are an important concept to understand in React.\
  \ You use props to pass data and values from one component to another to get dynamic\
  \ and unique outputs. \nWebsites built with React like Facebook, Twitter, and Netflix\
  \ use the s..."
---

Par Joy O. Oluwafemi

Les props sont un concept important à comprendre dans React. Vous utilisez les props pour passer des données et des valeurs d'un composant à un autre afin d'obtenir des résultats dynamiques et uniques. 

Les sites web construits avec React comme Facebook, Twitter et Netflix utilisent les mêmes motifs de conception dans de nombreuses sections qui ont simplement des données différentes. L'une des principales façons pour les développeurs d'atteindre cette fonctionnalité est d'utiliser les props.

Cet article expliquera ce que sont les props et nous examinerons la syntaxe pour passer et recevoir des props. Ensuite, pour renforcer davantage vos connaissances sur les props, nous construirons une section d'un site de commerce électronique qui affiche des informations sur différents produits aux utilisateurs.

Le concept de props est basé sur le concept de composants. Donc, pour tirer le meilleur parti de cet article, vous devez savoir [comment configurer une application React](https://www.freecodecamp.org/news/the-react-handbook-b71c27b0a795/#how-to-use-create-react-app) et [être familier avec le fonctionnement des composants React](https://www.freecodecamp.org/news/the-react-handbook-b71c27b0a795/#components).

## Qu'est-ce que les Props React ?

Les props dans React sont des entrées que vous passez aux composants. Les props permettent au composant d'accéder à des données personnalisées, des valeurs et des morceaux d'informations que les entrées contiennent. 

Le terme 'props' est une abréviation de 'properties' qui fait référence aux propriétés d'un objet.

Comme je l'ai dit dans l'introduction, le concept de props repose sur les composants. Nous ne pouvons donc pas travailler avec succès avec les props sans avoir un composant avec lequel travailler. 

Construisons et connectons les composants avec lesquels nous allons travailler dans ce tutoriel.

Voici la structure du composant parent :

```javascript
import Product from "./Product"

function App() {
  return (
      <div>
      	<h1>PRODUITS</h1>
      	<div className="App">
      		<Product />
      	</div>
      </div>
  )
}

export default App
```

Voici la structure du composant enfant :

```javascript
function Product() {
    return (
      <div>
        <img src="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933" alt="sneakers" />
        <h4>Cyxus</h4>
        <p>Chaussures de Running Loisirs Fitness Antidérapantes</p>
        <h4>29 $</h4>
      </div>
    );
}

export default Product
```

Notre objectif est de pouvoir afficher tous les différents produits qui varient en nom, prix, apparence et description aux utilisateurs. 

Bien sûr, nous pouvons réutiliser le composant produit autant de fois que nous le souhaitons en réaffichant simplement le composant. Par exemple :

```javascript
import Product from "./Product"

function App() {
  return (
    <div className="App">
      <Product />
      <Product />
      <Product />
    </div>
  )
}

export default App
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/props-repeated-design.PNG)
_Sortie en direct_

Nous pouvons voir la fonctionnalité React de répétition d'un design particulier sans écrire beaucoup de code en jeu ici. 

Mais nous n'avons pas encore atteint notre objectif, n'est-ce pas ? Bien que nous voulions réutiliser le composant, nous voulons également mettre à jour le nom du produit, le prix, la description et l'image sans avoir à coder en dur les données dans le composant Product.js. 

C'est là que nous pouvons utiliser les props dans React pour rendre notre sortie de données dynamique.

## Comment utiliser les Props React

Avant d'aller plus loin, il est important de noter que React utilise un flux de données à sens unique. Cela signifie que les données ne peuvent être transférées que du composant parent aux composants enfants. De plus, toutes les données passées du parent ne peuvent pas être modifiées par le composant enfant. 

Cela signifie que nos données seront passées de `App.js` qui est le composant parent à `Product.js` qui est le composant enfant (et jamais dans l'autre sens).

### Comment envoyer des Props dans un composant

La manière dont les props sont passées dans un composant est similaire à la manière dont les attributs fonctionnent dans les éléments HTML. 

Par exemple, lorsque vous souhaitez passer des attributs dans un élément d'entrée en HTML, vous écrivez l'attribut et attachez la valeur de l'attribut à celui-ci, comme ceci :

```html
<input type="text" placeholder="Cyxus" />
```

De même, lors de l'envoi de props (qui sont également des propriétés et peuvent être comparées à des attributs), vous attachez vos valeurs à celles-ci. 

Voici la syntaxe :

```javascript
<ComponentName property1="value" property2="value" property3="value" />
```

Dans la balise du composant, après avoir écrit le nom du composant, nous attribuerons une valeur à chaque propriété. 

Utilisons maintenant la syntaxe ci-dessus pour passer des données dans le composant `App.js` :

```javascript
<Product
  img="https://ng.jumia.is/unsafe/fitin/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933"
  name="Cyxus"
  desc="Chaussures de Running Loisirs Fitness Antidérapantes"
  price="29 $"
/>
```

Dans le code ci-dessus, le nom du composant dans la balise est `Product`, et la première propriété ou prop est `img` avec sa valeur `[https://m.media amazon.com/images/W/WEBP_402378T1/images/I/71TR1WrqqJL](https://m.media-amazon.com/images/W/WEBP_402378T1/images/I/71TR1WrqqJL)._AC_UL320_.jpg` attachée à celle-ci. Ensuite, nous avons `name` qui est la deuxième propriété et `desc` qui est la troisième propriété (auxquelles des valeurs sont également attribuées).

Lorsque nous structurons correctement le composant `App.js`, il ressemblera maintenant à ceci :

```javascript
import Product from "./Product";

function App() {
  return (
    <div>
      <h1>PRODUITS</h1>
      <div className="App">
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933"
          name="Cyxus"
          desc="Chaussures de Running Loisirs Fitness Antidérapantes"
          price="29 $"
        />
      </div>
    </div>
  );
}

export default App;
```

Il y a une légère différence entre l'écriture des attributs HTML et le passage de props : tandis que les attributs HTML sont des mots-clés spéciaux déjà fournis pour vous, vous personnalisez et définissez les props dans React. 

Par exemple, j'ai créé les propriétés ; 'img', 'name', 'desc' et 'price' ci-dessus. Ensuite, j'ai attaché les valeurs des props avec celles-ci.

### Comment accéder et utiliser les Props dans React

Le composant reçoit `props` en tant que paramètre de fonction. Il utilise la valeur des props en définissant le paramètre en tant qu'objets props. 

Voici la syntaxe :

```javascript
// la fonction reçoit 'props' en tant que paramètre de fonction
function Product(props) {
    return (
      <div>
// elle utilise la valeur des props en définissant le paramètre en tant qu'objets props
        <img src={props.objectName} alt="produits" />
        <h4>{props.objectName}</h4>
        <p>{props.objectName}</p>
        <h4>{props.objectName}</h4>
      </div>
    );
}

export default Product
```

Relions la syntaxe ci-dessus à notre `Product.js` en recevant `props` en tant que fonction de paramètre et en définissant les props en tant qu'objet :

```javascript
// la fonction reçoit 'props' en tant que paramètre de fonction
function Product(props) {
    return (
      <div>
// elle utilise la valeur des props en définissant le paramètre en tant qu'objets props
        <img src={props.img} alt="produits" />
        <h4>{props.name}</h4>
        <p>{props.description}</p>
        <h4>{props.price}</h4>
      </div>
    );
}

export default Product
```

Nous avons réussi à rendre dynamiques les données que nous avons passées dans le composant Product.js. 

Pour réutiliser le composant 'Product.js' afin d'afficher les données d'autres produits, tout ce que nous avons à faire est d'attacher les nouvelles données ou valeurs lors du réaffichage du composant. 

Voici la syntaxe pour cela :

```javascript

<ComponentName property1="valueA" property2="valueB" property3="valueC" />
<ComponentName property1="valueD" property2="valueE" property3="valueF" />
<ComponentName property1="valueG" property2="valueH" property3="valueI" />
```

Relions maintenant la syntaxe ci-dessus à notre `App.js` :

```javascript
import Product from "./Product";

function App() {
  return (
    <div>
      <h1>PRODUITS</h1>
      <div className="App">
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/82/6142201/1.jpg?2933"
          name="Cyxus"
          desc="Chaussures de Running Loisirs Fitness Antidérapantes"
          price="29 $"
        />
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/01/241417/1.jpg?6747"
          name="Vitike"
          desc="Dernières Baskets Homme - Noir"
          price="100 $"
        />
        <Product
          img="https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/06/4410121/1.jpg?4437"
          name="Aomei"
          desc="Chaussures de Sport Casual Tendances Homme"
          price="40 $"
        />
      </div>
    </div>
  );
}

export default App;
```

La sortie en direct du code ci-dessus affiche maintenant l'image, le nom et la description propres à chaque produit. 

Voici la sortie en direct :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/props-final-output.PNG)
_[Voir la sortie en direct ici](https://ekezwh.csb.app/)_

[Voici](https://codesandbox.io/s/ekezwh?file=/src/App.js) le code utilisé pour le projet dans cet article, n'hésitez pas à le comparer avec votre code.

## Déstructuration des Props dans React

Maintenant que nous avons atteint la fonctionnalité que nous visions, formatons notre `Product.js` en utilisant la déstructuration. Il s'agit d'une fonctionnalité de JavaScript qui consiste à attribuer des morceaux de données d'un objet ou d'un tableau à une variable séparée afin que la variable puisse contenir les données provenant du tableau ou de l'objet.

Les props sont des objets. Donc, pour déstructurer des objets dans React, la première étape consiste à regrouper vos propriétés dans un ensemble d'accolades. Ensuite, vous pouvez soit les stocker dans une variable appelée `props` dans le corps de la fonction, soit les passer directement en tant que paramètre de la fonction.

La deuxième étape consiste à recevoir les propriétés là où vous en avez besoin en indiquant les noms des propriétés sans attacher le préfixe 'props'.

Voici un exemple des deux façons dont vous pouvez déstructurer dans React :

```javascript

function Product = (props) => {
// Première étape : Déstructuration dans le corps de la fonction
    const { img, name, desc, price} = props ;
    return (
      <div>
  		<img src={img} alt="produits" />
// Deuxième étape : recevoir les propriétés là où vous en avez besoin en indiquant les noms des propriétés sans attacher le préfixe 'props'.
        <h4>{name}</h4>
        <p>{description}</p>
        <h4>{price}</h4>
      </div>
    );
}

export default Product
```

```javascript
// Première étape : Déstructuration dans le paramètre de la fonction
function Product = ({ img, name, desc, price}) => {
    return (
      <div>
  		<img src={img} alt="produits" />
// Deuxième étape : recevoir les propriétés là où vous en avez besoin en indiquant les noms des propriétés sans attacher le préfixe 'props'.
        <h4>{name}</h4>
        <p>{description}</p>
        <h4>{price}</h4>
      </div>
    );
}

export default Product
```

La déstructuration dans React rend notre code plus lisible et plus concis. Notez que les deux façons de déstructurer que j'ai démontrées ci-dessus auront toujours la même sortie.

## Conclusion

Cet article a expliqué comment fonctionnent les props dans React, ce qui vous aidera à écrire des pages web avec des sorties de données dynamiques. 

Utilisez ces connaissances pour construire des choses cool ! Connectez-vous avec moi sur Twitter [@JoyPaces](https://twitter.com/JoyPaces).