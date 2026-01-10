---
title: Destructuration JavaScript et l'opérateur de propagation – Expliqué avec des
  exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T21:46:07.000Z'
originalURL: https://freecodecamp.org/news/javascript-destructuring-and-spread-operator-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Cheers--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Destructuration JavaScript et l'opérateur de propagation – Expliqué avec
  des exemples de code
seo_desc: 'By Nishant Kumar

  JavaScript has two awesome data structures that help you write clean and efficient
  code. But handling them can get messy sometimes.

  In this blog, I am going to show you how to handle destructuring in arrays and objects
  in JavaScript....'
---

Par Nishant Kumar

JavaScript possède deux structures de données géniales qui vous aident à écrire un code propre et efficace. Mais les manipuler peut parfois devenir compliqué.

Dans cet article, je vais vous montrer comment gérer la destructuration des tableaux et des objets en JavaScript. Nous apprendrons également à utiliser l'opérateur de propagation.

Commençons.

## Qu'est-ce que la destructuration de tableau en JavaScript ?

Supposons que nous avons un tableau contenant cinq nombres, comme ceci :

```
let array1 = [1, 2, 3, 4, 5]
```

Pour obtenir les éléments du tableau, nous pouvons faire quelque chose comme obtenir le nombre selon ses index :

```
array1[0];
array1[1];
array1[2];
array1[3];
array1[4];

```

Mais cette méthode est ancienne et encombrante, et il existe une meilleure façon de faire – en utilisant la destructuration de tableau. Cela ressemble à ceci :

```
let [ indexOne, indexTwo, indexThree, indexFour, indexFive ] = array1;
```

Les deux méthodes ci-dessus donneront le même résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-105209.png)

Maintenant, nous avons cinq éléments dans le tableau, et nous les imprimons. Mais que faire si nous voulons sauter un élément entre les deux ?

```
let [ indexOne, indexTwo, , indexFour, indexFive ] = array1;
```

Ici, nous avons sauté `indexThird`, et il y a un espace vide entre indexTwo et indexFour.

```
let [ indexOne, indexTwo, , indexFour, indexFive ] = array1;

console.log(indexOne);
console.log(indexTwo)
console.log(indexFour)
console.log(indexFive)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-105709.png)

Vous pouvez voir que nous n'obtenons pas le troisième élément car nous l'avons défini comme vide.

## Qu'est-ce que la destructuration d'objet en JavaScript ?

Cette destructuration fonctionne également bien avec les objets. Permettez-moi de vous donner un exemple.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 200,
    height: '20 meters',
    weight: '70 KG'
}
```

Supposons que nous voulons que le nom, le salaire et le poids de cet objet soient imprimés dans la console.

```
console.log(object.name)
console.log(object.salary)
console.log(object.weight)
```

Nous pouvons les obtenir en utilisant les clés, qui sont name, salary et weight.

Mais ce code devient parfois difficile à comprendre. C'est là que la destructuration est utile :

```
let { name, salary, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

Et maintenant, nous pouvons simplement logger name, salary et weight au lieu d'utiliser cette ancienne méthode.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-111356.png)

Nous pouvons également utiliser la destructuration pour définir des valeurs par défaut si la valeur n'est pas présente dans l'objet.

```
let object = {
    name: "Nishant",
    age: 24, 
    height: '20 meters',
    weight: '70 KG'
}

let { name, salary, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

Ici, nous avons name et weight présents dans l'objet, mais pas le salary :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-111659.png)

Nous obtiendrons une valeur indéfinie pour le salaire. 

Pour corriger ce problème, nous pouvons définir des valeurs par défaut lorsque nous destructurons l'objet.

```
let object = {
    name: "Nishant",
    age: 24, 
    height: '20 meters',
    weight: '70 KG'
}

let { name, salary = 200, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-111907.png)

Vous pouvez voir que nous obtenons 200 comme salaire. Cela ne fonctionne que lorsque nous n'avons pas cette clé dans l'objet, et que nous voulons définir une valeur par défaut.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

let { name, salary = 200, weight } = object;

console.log(name)
console.log(salary)
console.log(weight)
```

Ajoutez salary dans l'objet, et vous obtiendrez 300 comme salaire.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-112128.png)

## Comment utiliser la destructuration d'objet avec des fonctions

Supposons que nous avons une fonction qui imprime toutes les données du tableau dans la console.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

function printData(){
    
}

printData(object)

```

Nous passons l'objet comme paramètre dans la fonction lorsqu'il est appelé :

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

function printData(object){
    console.log(object)
}

printData(object)
```

Normalement, nous ferions quelque chose comme ceci – passer l'objet et le logger dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-115047.png)

Mais encore une fois, nous pouvons faire la même chose en utilisant la destructuration.

```
let object = {
    name: "Nishant",
    age: 24, 
    salary: 300,
    height: '20 meters',
    weight: '70 KG'
}

function printData({name, age, salary, height, weight}){
    console.log(name, age, salary, height, weight)
}

printData(object)
```

Ici, nous destructurons l'objet en name, age, salary, height et weight dans les paramètres de la fonction et nous imprimons tout sur la même ligne. 

Vous pouvez voir comment la destructuration rend cela beaucoup plus facile à comprendre.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-115329.png)
_Impression des données de l'objet en utilisant la destructuration_

Regardons un dernier exemple. 

```
function sample(a, b) {
    return [a + b, a * b]
}

let example = sample(2, 5);
console.log(example)
```

Nous avons une fonction ici qui accepte deux nombres. Elle retourne un tableau en les additionnant et en les multipliant et les log dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-120108.png)

Utilisons plutôt la destructuration ici.

Nous pouvons la destructurer en variables d'addition et de multiplication comme ceci :

```
let [addition, multiplication] = sample(2, 5);
console.log(addition)
console.log(multiplication)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-120325.png)

Et dans la sortie, vous pouvez voir que nous obtenons l'_addition_ et la _multiplication_ des deux nombres.

## Qu'est-ce que l'opérateur de propagation en JavaScript ?

Spread signifie étendre ou développer. Et l'opérateur de propagation en JavaScript est représenté par trois points. 

Cet opérateur de propagation a de nombreuses utilisations différentes. Voyons-les une par une.

### Exemples d'opérateur de propagation

Supposons que nous avons deux tableaux et que nous voulons les fusionner. 

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [6, 7, 8, 9, 10]

let array3 = array1.concat(array2);
console.log(array3)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-112601.png)

Nous obtenons la combinaison des deux tableaux, qui sont array1 et array2.

Mais il existe une manière plus simple de faire cela :

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [6, 7, 8, 9, 10]

let array3 = [...array1, ...array2]
console.log(array3)
```

Dans ce cas, nous utilisons l'opérateur de propagation pour fusionner les deux tableaux.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-113020.png)

Et vous pouvez voir, nous obtiendrons la même sortie.

Imaginons un autre cas d'utilisation où nous devons insérer _array1_ entre les éléments de _array2_.

Par exemple, nous voulons insérer _array2_ entre le deuxième et le troisième élément de _array1_.

Alors, comment faisons-nous cela ? Nous pouvons faire quelque chose comme ceci :

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [6, 7, ...array1, 8, 9, 10]

console.log(array2);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-113502.png)

Et vous pouvez voir, nous obtenons les éléments de array1 entre 7 et 8.

Maintenant, fusionnons deux objets ensemble en utilisant l'opérateur de propagation.

```
let object1 = {
    firstName: "Nishant",
    age: 24, 
    salary: 300,
}

let object2 = {
    lastName: "Kumar",
    height: '20 meters',
    weight: '70 KG'
}
```

Nous avons deux objets ici. L'un contient firstName, age et salary. Le second contient lastName, height et weight. 

Fusionnons-les ensemble.

```
let object1 = {
    firstName: "Nishant",
    age: 24, 
    salary: 300,
}

let object2 = {
    lastName: "Kumar",
    height: '20 meters',
    weight: '70 KG'
}

let object3 = {...object1, ...object2}
console.log(object3);
```

Nous avons maintenant fusionné les deux objets en utilisant l'opérateur de propagation, et nous avons logué la valeur dans la console.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-114101.png)
_Combinaison des objets précédents_

Vous pouvez voir que nous obtenons la combinaison des deux objets.

Enfin, nous pouvons également copier un tableau dans un autre en utilisant l'opérateur de propagation. Permettez-moi de vous montrer comment cela fonctionne :

```
let array1 = [1, 2, 3, 4, 5]
let array2 = [...array1]
console.log(array2);
```

Ici, nous copions _array1_ dans _array2_ en utilisant l'opérateur de propagation.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-07-120757.png)

Nous loggons _array2_ dans la console, et nous obtenons les éléments de _array1_.

## Conclusion

C'est tout, les amis ! Dans cet article, nous avons appris la destructuration des tableaux et des objets ainsi que l'opérateur de propagation.

Vous pouvez également regarder ma vidéo YouTube sur [Array and Object Destructuring and the Spread Operator](https://youtu.be/QvQ4o0K9_g0) si vous souhaitez compléter votre apprentissage.

> Bon apprentissage.