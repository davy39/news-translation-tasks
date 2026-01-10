---
title: Un guide sur 'this' en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-26T21:02:04.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-this-in-javascript-e3b9daef4df1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dJjQKiKhX-PbafQS
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un guide sur 'this' en JavaScript
seo_desc: 'By Ashay Mandwarya ?️??

  The this keyword hands-down is one of the most widely used and yet misunderstood
  in JavaScript. I’ll try to change that today.

  Let’s go back to the good old school days, when we learned about pronouns.


  Phelps is swimming fast...'
---

Par Ashay Mandwarya 👨💻🚀

Le mot-clé `this` est sans conteste l'un des plus largement utilisés et pourtant incompris en JavaScript. Je vais essayer de changer cela aujourd'hui.

Retournons aux bons vieux jours d'école, lorsque nous avons appris les pronoms.

> Phelps nage vite parce qu'_il_ veut gagner la course.

Remarquez l'utilisation du pronom « il ». Nous ne nous adressons pas directement à Phelps ici, mais nous utilisons le pronom « il » pour _faire référence_ à Phelps. De manière similaire, JavaScript utilise le mot-clé `this` comme référent pour faire référence à l'objet dans le contexte, c'est-à-dire le sujet.

Exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/wTwrO4Y9ico1Ieh1NZV1HJK-PFVgeBlIq4rE)

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function () {console.log(this.make+" " +this.model);console.log(car.make+ " " +car.model);}}car.fullName();
```

Dans le code ci-dessus, nous avons un objet `car` qui possède les propriétés `make`, `model` et `fullName`. La valeur de `fullName` est une fonction qui imprime le nom complet de la voiture en utilisant deux syntaxes différentes.

* En utilisant `this` =&g`t; this.make+" " +this.mod`el `the t`his fait référence à l'objet dans le contexte qui `est c`ar `donc this.ma`ke est effectivement `car.m`ake et il en va de même pour `this.mo`del.
* En utilisant la notation par points, nous pouvons accéder aux propriétés des objets, `car.make` & `car.model`.

### `this` c'est ça !

Maintenant que nous avons compris ce qu'est `this` et son utilisation la plus basique, établissons quelques règles pour toujours nous en souvenir.

#### Le mot-clé `this` en JS fait référence à l'objet auquel il appartient.

```
var car={make:'....'func:()=>{console.log(this.make)}}
```

Le `this` dans l'extrait ci-dessus appartient à l'objet car.

#### Il prend différentes valeurs selon l'usage

1. À l'intérieur d'une méthode.
2. À l'intérieur d'une fonction.
3. Seul.
4. Dans un événement.
5. `call()`, et `apply()`.

**À l'intérieur d'une méthode**

Lorsque `this` est utilisé à l'intérieur d'une méthode, il fait référence à l'objet propriétaire.

Les fonctions définies à l'intérieur d'un objet sont appelées méthodes. Reprenons notre exemple de voiture.

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function () {console.log(this.make+" " +this.model);console.log(car.make+ " " +car.model);}}car.fullName();
```

`fullName()` ici est une méthode. Le `this` à l'intérieur de cette méthode appartient à `car`.

**À l'intérieur d'une fonction**

`this` à l'intérieur d'une fonction est un peu compliqué. La première chose à comprendre est que, comme tous les objets ont des propriétés, de même les fonctions ont aussi des propriétés. Chaque fois que cette fonction est exécutée, elle obtient la propriété `this`, qui est une variable avec la valeur de l'objet qui l'invoque.

> _this_ est vraiment juste une référence raccourcie pour l'objet « antécédent » — l'objet invoquant. — javascriptissexy.com

Si la fonction n'est pas invoquée par un objet, alors le `this` à l'intérieur de la fonction appartient à l'objet global, qui est appelé window. Dans ce cas, this fera référence aux valeurs définies dans la portée globale. Voyons un exemple pour mieux comprendre :

```
var make= "Mclaren";var model= "720s"function fullName(){ console.log(this.make+ " " + this.model);}
```

```
var car = {    make:"Lamborghini",    model:"Huracán",    fullName:function () {    console.log (this.make + " " + this.model);    }}    car.fullName(); // Lmborghini Huracán    window.fullName(); // Mclaren 720S    fullName(); // Mclaren 720S
```

![Image](https://cdn-media-1.freecodecamp.org/images/gZYHKpKwNHIdbUskoYkA9lrq4hORsGZb0MrX)

Ici, `make, model` et `fullName` sont définis globalement, tandis que l'objet `car` a également une implémentation de `fullName`. Lorsque invoqué par l'objet `car`, this fait référence aux propriétés définies à l'intérieur de l'objet. D'autre part, les deux autres appels de fonction sont les mêmes et retournent les propriétés définies globalement.

**Seul**

Lorsque utilisé seul, non à l'intérieur d'une fonction ou d'un objet, `this` fait référence à l'objet global.

![Image](https://cdn-media-1.freecodecamp.org/images/kDPYXnkWNp3oS7XWmnz9A9UpO5BobzsU8Rac)

Le `this` ici fait référence à la propriété de nom global.

**Dans un événement**

Les événements peuvent être de n'importe quel type, mais pour des raisons de simplicité et de clarté, prenons un événement de clic.

![Image](https://cdn-media-1.freecodecamp.org/images/vjRoyCEJjhZ6wuLoFwmJ8ZcUBs9q4CbCteLE)

Chaque fois qu'un bouton est cliqué et qu'un événement est déclenché, il peut appeler une autre fonction pour effectuer une certaine tâche basée sur le clic. Si `this` est utilisé à l'intérieur de cette fonction, il fera référence à l'élément qui a déclenché l'événement. Dans le DOM, tous les éléments sont stockés sous forme d'objets. C'est pourquoi, lorsqu'un événement est déclenché, il fait référence à cet élément, car cet _élément de la page web est en fait un objet à l'intérieur du DOM_.

Exemple :

```
<button onclick="this.style.display='none'">  Supprimez-moi !</button>
```

**call(), apply() & bind()**

* bind : nous permet de définir la valeur de `this` sur les méthodes.
* call & apply : nous permettent d'emprunter des fonctions et de définir la valeur de `this` lors de l'invocation de la fonction.

Call, Bind et Apply sont en eux-mêmes le sujet d'un autre article. Ils sont très importants, et les expliquer ici n'est pas possible car nous devons tout savoir sur `this` pour connaître l'utilisation de ces fonctions.

### La partie la plus délicate

Si bien compris, `this` facilite notre travail d'une certaine manière. Mais il y a certains cas où il est mal compris.

#### Exemple 1.

![Image](https://cdn-media-1.freecodecamp.org/images/QECIynBJi8AJ0BtMQ9WrKxhdDHTn5PCYzYM1)

```
var car = {make:"Lamborghini",model:"Huracán",name:null,fullName:function () {this.name=this.make + " " + this.model;console.log (this.name);}}
```

```
var anotherCar={make:"Ferrari",model:"Italia",name:null}
```

```
    anotherCar.name= car.fullName();
```

Nous obtenons ici un résultat inattendu. Nous avons emprunté une méthode qui utilise `this` à partir d'un autre objet, mais le problème ici est que la méthode est seulement assignée à la fonction `anotherCar` mais est en fait invoquée sur l'objet `car`. C'est pourquoi nous obtenons le résultat Lamborghini et non Ferrari.

Pour résoudre cela, nous utilisons la méthode `call()`.

![Image](https://cdn-media-1.freecodecamp.org/images/j-mA-iIgaiRYxmuvvi0ToNl3GN5jUJGMxLjS)

Ici, la méthode `call()` appelle `fullName()` sur l'objet `anotherCar` qui n'a pas initialement la fonction `fullName()`.

Nous pouvons également voir que, lorsque nous enregistrons `car.name` et `anotherCar.name`, nous obtenons le résultat pour ce dernier et non pour le premier, ce qui signifie que la fonction a effectivement été invoquée sur `anotherCar` et non sur `car`.

#### Exemple 2.

![Image](https://cdn-media-1.freecodecamp.org/images/OxopdQevmTVOOZrzt4Q3FtJf9yjOUl6GYUd3)

```
var cars=[{ make: "Mclaren", model: "720s"},{make: "Ferrari",model: "Italia"}]
```

```
var car = {cars:[{make:"Lamborghini", model:"Huracán"}],fullName:function () {console.log(this.cars[0].make + " " + this.cars[0].model);}}var vehicle=car.fullName;vehicle()
```

Dans l'extrait ci-dessus, nous avons un objet global appelé cars et nous avons le même objet nommé à l'intérieur de l'objet car. La méthode `fullName()` est ensuite assignée à la variable vehicle qui est ensuite appelée. La variable appartient à l'objet global donc `this` appelle l'objet global `cars` au lieu de l'objet `cars` en raison du contexte.

Pour résoudre cela, nous utilisons la fonction `.bind()` pour résoudre le problème.

![Image](https://cdn-media-1.freecodecamp.org/images/MkmeqFWxySNTcnDJtc-HgSAzXzTejtvEg4d0)

Le binding nous aide à définir spécifiquement la valeur de `this` et donc la variable vehicle pointe explicitement vers l'objet car et non vers l'objet global, donc this se trouve dans le contexte de l'objet `car`.

#### Exemple 3.

![Image](https://cdn-media-1.freecodecamp.org/images/ctGttd8h1qWNlNrursCjmjOcMzsGbNh5Z0lj)

```
var car = {cars:[{make:"Lamborghini",model:"Huracán"},{ make: "Mclaren", model: "720s"},{make: "Ferrari",model: "Italia"}],fullName:function(){this.cars.forEach(()=>{console.log (this.make + " " + this.model);})}}car.fullName();
```

Dans l'extrait ci-dessus, `fullName()` appelle une fonction qui itère à travers le tableau cars en utilisant `forEach`. À l'intérieur de `forEach`, il y a une fonction anonyme où this perd le contexte. Une fonction à l'intérieur d'une fonction en JavaScript est appelée une `closure`. Les `closures` sont très importantes et largement utilisées en JavaScript.

Un autre concept important jouant un rôle ici est `scope`. Une variable à l'intérieur d'une fonction ne peut pas accéder aux variables et propriétés en dehors de sa `scope`. `this` à l'intérieur de la fonction anonyme ne peut pas accéder à `this` en dehors de celle-ci. Donc `this` n'a nulle part où aller sauf pointer vers l'objet global. Mais là, aucune propriété n'est définie pour que `this` y accède, donc `undefined` est imprimé.

Une solution de contournement pour ce qui précède est que nous pouvons assigner une variable à la valeur de `this`, en dehors de la fonction anonyme et ensuite l'utiliser à l'intérieur.

![Image](https://cdn-media-1.freecodecamp.org/images/QnnxvDSMK09VH6ESN6P-Wg7f641JAiNZAYL5)

Ici, la variable self contient la valeur de `this` qui est utilisée avec la fonction interne, nous donnant ainsi la sortie.

#### Exemple 4.

![Image](https://cdn-media-1.freecodecamp.org/images/KNmGVCmOuov8GWgyQax139PGvdfUBVmuPMz3)

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function (cars) {cars.forEach(function(vehicle){console.log(vehicle +" "+ this.model);})}}car.fullName(['lambo','ferrari','porsche']);
```

C'est un exemple revisité, dans lequel `this` n'était pas accessible, donc nous avons préservé sa valeur en utilisant une variable appelée self. Utilisons la fonction fléchée pour résoudre le même problème :

![Image](https://cdn-media-1.freecodecamp.org/images/ADnAYyjYS7xXBZqC6U7FM8PdB4AV3TNk40N1)

Comme vous pouvez le voir, l'utilisation d'une fonction fléchée dans `forEach()` résout automatiquement le problème et nous n'avons pas à faire de bind, ou à donner la valeur de `this` à une autre variable. Cela est dû au fait que les fonctions fléchées lient leur contexte, donc `this` fait effectivement référence au contexte d'origine, ou à l'objet d'origine.

#### Exemple 5.

![Image](https://cdn-media-1.freecodecamp.org/images/oKsJC9oHyb0etj1IqlWF3gZW1x6gSQYOPnAC)

```
var car= {make: "Lamborghini",model: "Huracán",fullName: function () {console.log(this.make +" "+ this.model);}}var truck= {make: "Tesla",model: "Truck",fullName: function (callback) {console.log(this.make +" "+ this.model);callback();}}truck.fullName(car.fullName);
```

Le code ci-dessus se compose de deux objets identiques, l'un contenant une fonction de **rappel**. Une fonction de **rappel** est une fonction passée dans une autre fonction en tant qu'argument, qui est ensuite invoquée à l'intérieur de la fonction externe pour compléter une sorte de routine.

Ici, la méthode `fullName` de l'objet truck se compose d'un **rappel** qui est également invoqué à l'intérieur. Notre objet car est tel qu'avant. Lorsque nous invoquons la méthode `fullName` de truck avec le rappel (argument) en tant que méthode `fullName` de l'objet car, nous obtenons la sortie `Tesla Truck` et `undefined undefined`.

Après avoir lu sur `this`, certains d'entre vous ont peut-être eu l'intuition que `car.fullName` imprimerait le modèle et la marque de l'objet truck, mais à votre déception, `this` a encore joué un tour sur nous. Ici, `car.fullName` est passé en tant qu'argument et n'est pas réellement invoqué par l'objet truck. Le rappel invoque la méthode de l'objet car, mais notez que le site d'appel réel pour la fonction est le rappel qui lie this à l'objet global. C'est un peu confus, alors relisez-le !

![Image](https://cdn-media-1.freecodecamp.org/images/ygRcPGWkKHvfGTrXGnqA5nHxZxZG1C1zKXhd)

Ici, pour obtenir de la clarté, nous imprimons `this` lui-même. Nous pouvons voir que le `this` du rappel est donné une portée globale. Donc pour obtenir un résultat, nous créons des propriétés globales `make` et `model`.

![Image](https://cdn-media-1.freecodecamp.org/images/lpWM9its6z5qKDw0jwWiD5GJtfqicPu-w3Dl)

Encore une fois, en exécutant le même code avec les propriétés globales `make` et `model`, nous obtenons enfin la réponse au `this` global. Cela prouve que `this` fait référence à l'objet global.

Pour obtenir les résultats que nous désirons, le résultat `car.fullName`, nous utiliserons à nouveau `bind()` pour lier de manière permanente l'objet car au rappel, ce qui remettra tout en ordre.

![Image](https://cdn-media-1.freecodecamp.org/images/rQ3vsBx5Wafjo7E01sHQiQdsrs1cXI4WKKcy)

### Résolu !

Sans aucun doute, `this` est très utile, mais il a aussi ses propres pièges. J'espère avoir rendu cela assez facile pour vous à comprendre. Si vous voulez plus de contenu simplifié comme celui-ci, suivez-moi sur Medium. Veuillez laisser vos réponses et partager cela si vous l'avez aimé.

![Image](https://cdn-media-1.freecodecamp.org/images/Wdps8LMY6qHwRYPkdMh200uv4BmBLUPAM-PW)
_Google_