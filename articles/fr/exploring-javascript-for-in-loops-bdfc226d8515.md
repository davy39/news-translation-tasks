---
title: Exploration de l'itération en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-23T02:50:20.000Z'
originalURL: https://freecodecamp.org/news/exploring-javascript-for-in-loops-bdfc226d8515
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XJvkwoG4BLFnx6tpfzPZQQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Exploration de l'itération en JavaScript
seo_desc: 'By Festus K. Yangani

  Loops allow programs to perform repetitive tasks, such as iterating through an array,
  while adhering to the DRY principle (Don’t Repeat Yourself). They come in handy
  when you want to execute a function a number of times, using di...'
---

Par Festus K. Yangani

Les boucles permettent aux programmes d'effectuer des tâches répétitives, telles que l'itération à travers un tableau, tout en respectant le [principe DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Ne vous répétez pas). Elles sont utiles lorsque vous souhaitez exécuter une fonction plusieurs fois, en utilisant différents ensembles d'entrées à chaque fois.

Tout comme d'autres langages de programmation, JavaScript supporte différents types de boucles. Cet article explorera les boucles **for**, **for/in**, **while** et **do/while**.

#### La boucle For

La boucle **for** est le style de boucle JavaScript le plus courant. Voici sa syntaxe de base :

```
for (<initialisation>; <condition>; <expression d'incrémentation>) {   bloc de code // Ceci est exécuté si la condition est évaluée à vrai}
```

* **initialisation** - utilisée pour déclarer de nouvelles variables avec le mot-clé **var**, généralement utilisée pour initialiser une variable de compteur (var i = 0).
* **condition** - Une expression booléenne à évaluer avant chaque itération de la boucle. Si cette expression est évaluée à vrai, les commandes internes seront exécutées.
* **expression d'incrémentation** - une expression évaluée à la fin de chaque itération de la boucle. Cela est généralement utilisé pour incrémenter, décrémenter ou mettre à jour la variable de compteur.

Exemples :

```
//Compter de 1 à 5for (var i = 1; i <= 5; i++) {  console.log(i);}//=&gt; 1//=> 2//=&gt; 3//=&gt; 4//=&gt; 5
```

```
//Itérer à travers un tableauvar arr = [17, 22, 35, 54, 96];
```

```
for (var i = arr.length; i >=0; i--) {  console.log(arr[i]);}//=&gt; 96//=&gt; 54//=> 35//=> 22//=> 17
```

#### La boucle For/in

La boucle **for/in** est utilisée pour itérer à travers les propriétés d'un objet. Une instruction **for/in** se présente comme suit :

```
for (variable in object) {  instructions}
```

* **variable** - un nom de propriété différent est assigné à celle-ci à chaque itération.
* **object** - l'objet dont les propriétés énumérables sont itérées.

Exemple :

```
var myObj = {city: "Austin", state: "Texas", country: "USA"}
```

```
for (var key in myObj) {  console.log(myObj[key]);}//=&gt; Austin//=> Texas//=> USA
```

#### La boucle While

Les boucles **while** sont des boucles conditionnelles où une condition est vérifiée au début de l'itération, et — si la condition est vraie — les instructions sont exécutées. Voici la syntaxe de base d'une boucle **while** :

```
while (condition) {  instruction //bloc de code à exécuter tant que la condition est vraie.}
```

* **condition** - l'expression évaluée avant chaque itération de la boucle. Si cette condition est évaluée à vrai, les commandes internes sont exécutées. Si la condition est évaluée à faux, alors l'instruction interne ne sera pas exécutée et le programme continuera.
* **instruction** - le bloc de code à exécuter tant que la condition est évaluée à vrai.

Exemple :

```
var i = 0;while (i < 3) {  console.log(i);  i++;}
```

```
//=>0//=>1//=>2
```

#### La boucle do/while

La boucle **do/while** est une variante de la boucle while. Contrairement à la boucle while, la boucle **do/while** exécutera le bloc de code une fois, avant même de vérifier si la condition est vraie. Ensuite, elle répétera la boucle tant que la condition est vraie.

Syntaxe :

```
do {      instruction //bloc de code à exécuter}while (condition);
```

* **instruction** - exécutée au moins une fois, et est réexécutée chaque fois que la condition est évaluée à vrai.
* **condition** - l'expression évaluée après chaque itération de la boucle. Si la condition est évaluée à vrai, l'instruction est réexécutée. Si la condition est évaluée à faux, alors l'exécution de l'instruction est arrêtée.

Exemple :

```
var cars = ["Tesla", "Prius", "GMC", "Ford"];
```

```
var i = 0;do {      console.log(cars[i]);              i++;}while (i < cars.length)
```

```
//=&gt; Tesla//=> Prius//=> GMC//=> Ford
```

J'espère que ce bref tour des boucles vous a aidé à mieux comprendre comment fonctionne l'itération en JavaScript. Si vous avez des questions sur les boucles, ou si vous souhaitez simplement discuter, vous pouvez également me contacter sur [twitter](https://twitter.com/yangani).