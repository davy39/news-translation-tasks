---
title: Qu'est-ce qu'un objet JavaScript ? Paires clé-valeur et notation par points
  expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T22:04:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-javascript-object
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Blue--Violet-and-Orange-Shapes-Fitness-Influencer-YouTube-Thumbnail-Set--2--1.png
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: Qu'est-ce qu'un objet JavaScript ? Paires clé-valeur et notation par points
  expliquées
seo_desc: "By Danny Thompson\nObjects are one of the most valuable things you can\
  \ learn in JavaScript. You can use them to take your programs to the next level.\
  \ \nAn object is a collection of data – or key value pairs – which consist of variables\
  \ and functions th..."
---

Par Danny Thompson

Les objets sont l'une des choses les plus précieuses que vous pouvez apprendre en JavaScript. Vous pouvez les utiliser pour faire passer vos programmes au niveau supérieur. 

Un **objet** est une collection de données – ou paires clé-valeur – qui se composent de variables et de fonctions auxquelles vous pouvez accéder en utilisant la notation par points.

Maintenant, ce sont des mots qui peuvent ne rien signifier pour vous pour le moment, alors décomposons cela. 

## Qu'est-ce qu'une paire clé-valeur en JavaScript ? 

La manière la plus simple d'expliquer une paire clé-valeur est que vous avez 2 éléments qui sont liés ensemble. L'un étant la "clé" et l'autre étant la "valeur". Un objet peut avoir plusieurs paires clé-valeur à l'intérieur.

![Une image d'un objet montrant la relation entre la clé et la valeur.](https://www.freecodecamp.org/news/content/images/2021/07/Blue--Violet-and-Orange-Shapes-Fitness-Influencer-YouTube-Thumbnail-Set--3-.png)

Maintenant que nous comprenons ce que sont les paires clé-valeur, nous pouvons plonger plus profondément dans les objets.

## Qu'est-ce qu'un objet en JavaScript ? 

Voici un objet en JavaScript : 

```js
const phone = {
	brand: ['Samsung', 'Apple', 'Google'],
	quantity: [1,2,3],
	howManyGooglePhones: function(){
		alert("There are " + this.quantity[1] + ' ' + this.brand[2] + " phones available.");
	}
}

phone.howManyGooglePhones();
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-35.png)

Nous créons et nommons notre objet – dans ce cas, nous l'avons nommé `phone`. Nous avons également tout enveloppé dans nos accolades { }. Chaque clé est séparée de la valeur en utilisant un deux-points `:`.

Dans le code ci-dessus, nous avons 2 tableaux et une fonction. Remarquez comment chaque paire clé-valeur se termine par une virgule `,` – cela est très important et requis.

## Qu'est-ce que la notation par points en JavaScript ?

La notation par points est l'endroit où nous pouvons appeler cette paire clé-valeur (qui est connue sous le nom de propriété) et récupérer cette information. 

Si je voulais la marque Samsung, je pourrais faire **`phone.brand[0]`** et cela me donnerait Samsung. Nous utilisons le nom de l'objet (dans cet exemple, c'est `phone`), utilisons un point, puis procédons en écrivant le nom de la propriété.

Notre fonction est configurée pour afficher combien de téléphones nous avons de chaque marque. Dans la fonction ci-dessus, nous l'utilisons pour montrer combien de téléphones Google nous avons en stock.

**`this.quantity[1]`** accède à la propriété "quantity" et recherche la valeur à la position [1]. **`this.brand[2]`** accède à la propriété Brand que nous voulons afficher, qui dans ce cas est Google. 

Pouvez-vous rapidement déterminer comment nous accéderions à Apple avec une quantité de 3 ? À quoi cela ressemblerait-il dans cette situation ?

`this` est utilisé car nous voulons accéder à ces valeurs depuis cet objet. L'alerte crée une fenêtre contextuelle pour afficher ces informations lorsque le programme se charge pour cet exemple.

Maintenant que notre objet est complet, nous voulons appeler la fonction qui se trouve dans l'objet et l'afficher. Puisque nous ne sommes plus dans l'objet, **nous n'utiliserons pas `this`** comme nous l'avons fait à l'intérieur de l'objet. 

**À la place**, nous appellerons l'objet par son nom et utiliserons la notation par points. Le nom de notre objet est **`phone`**, alors utilisons-le puis le nom de la fonction :

**`phone.howManyGooglePhones();`**

L'appel de la fonction créera maintenant cette fenêtre contextuelle :

![Pop up alert shows that there are 2 Google Phones available.](https://www.freecodecamp.org/news/content/images/2021/07/image-34.png)

Vous avez réussi à créer un objet, à appeler une fonction, qui était dans l'objet et qui a accédé à 2 valeurs différentes des propriétés. Beau travail !

Si vous aimez mes articles de blog, vous allez adorer mes publications sur les réseaux sociaux.   
Suivez-moi sur Twitter @DThompsonDev