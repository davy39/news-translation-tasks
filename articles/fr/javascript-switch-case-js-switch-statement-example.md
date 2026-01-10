---
title: JavaScript Switch Case – Exemple d'instruction JS Switch
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-06T15:18:55.000Z'
originalURL: https://freecodecamp.org/news/javascript-switch-case-js-switch-statement-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/karl-pawlowicz-QUHuwyNgSA0-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript Switch Case – Exemple d'instruction JS Switch
seo_desc: "There are times in JavaScript where you might consider using a switch statement\
  \ instead of an if else statement.  \nswitch statements can have a cleaner syntax\
  \ over complicated if else statements. \nTake a look at the example below – instead\
  \ of using t..."
---

Il arrive en JavaScript que vous envisagiez d'utiliser une instruction `switch` plutôt qu'une instruction `if else`.

Les instructions `switch` peuvent avoir une syntaxe plus propre que les instructions `if else` compliquées.

Regardez l'exemple ci-dessous – au lieu d'utiliser cette longue instruction `if else`, vous pourriez choisir une instruction `switch` plus facile à lire.

```js
const pet = "dog";

if (pet === "lizard") {
  console.log("I own a lizard");
} else if (pet === "dog") {
  console.log("I own a dog");
} else if (pet === "cat") {
  console.log("I own a cat");
} else if (pet === "snake") {
  console.log("I own a snake");
} else if (pet === "parrot") {
  console.log("I own a parrot");
} else {
  console.log("I don't own a pet");
}
```

```js
const pet = "dog";

switch (pet) {
  case "lizard":
    console.log("I own a lizard");
    break;
  case "dog":
    console.log("I own a dog");
    break;
  case "cat":
    console.log("I own a cat");
    break;
  case "snake":
    console.log("I own a snake");
    break;
  case "parrot":
    console.log("I own a parrot");
    break;
  default:
    console.log("I don't own a pet");
    break;
}
```

Dans cet article, je vais expliquer ce que sont les instructions switch et comment elles fonctionnent. Je vais également vous aider à déterminer si elles constituent une bonne option à utiliser dans votre code.

## Qu'est-ce qu'une instruction Switch ?

En programmation, une instruction `switch` est une instruction de contrôle de flux qui teste la valeur d'une `expression` par rapport à plusieurs cas.

Voici la syntaxe de base d'une instruction `switch` :

```js
switch (expression) {
  case 1:
   //ce code s'exécutera si le cas correspond à l'expression
    break;
  case 2:
   //ce code s'exécutera si le cas correspond à l'expression
    break;
  case 3:
   //ce code s'exécutera si le cas correspond à l'expression
    break;
  default:
    //ce code s'exécutera si aucun des cas ne correspond à l'expression
    break;
}
```

L'ordinateur parcourra l'instruction `switch` et vérifiera l'égalité stricte `===` entre le `case` et l'`expression`. Si l'un des cas correspond à l'`expression`, alors le code à l'intérieur de cette clause `case` sera exécuté.

```js
switch (expression) {
  case 1:
   //ce code s'exécutera si le cas correspond à l'expression
    break;
  case 2:
   //ce code s'exécutera si le cas correspond à l'expression
    break;
}
```

Si aucun des cas ne correspond à l'expression, alors la clause `default` sera exécutée.

```js
  default:
    //ce code s'exécutera si aucun des cas ne correspond à l'expression
    break;
```

Si plusieurs cas correspondent à l'instruction `switch`, alors le premier `case` qui correspond à l'`expression` sera utilisé.

Les instructions `break` sortiront du `switch` lorsque le `case` sera trouvé. Si les instructions `break` ne sont pas présentes, alors l'ordinateur continuera à travers l'instruction `switch` même si une correspondance est trouvée.

Si des instructions `return` sont présentes dans le `switch`, alors vous n'avez pas besoin d'une instruction `break`.

## Exemple d'instructions Switch en JavaScript

Dans cet exemple, nous comparons `"oboe"` aux cas. `"oboe"` correspondrait à la troisième clause `case` et afficherait dans la console "I play the oboe".

```js
switch ("oboe") {
  case "trumpet":
    console.log("I play the trumpet");
    break;
  case "flute":
    console.log("I play the flute");
    break;
  case "oboe":
    console.log("I play the oboe");
    break;
  default:
    console.log("I don't play an instrument. Sorry");
    break;
}
```

Si je devais changer l'expression en `"no instrument"`, alors la clause `default` serait exécutée et le message affiché dans la console serait "I don't play an instrument. Sorry".

```js
switch ("no instrument") {
  case "trumpet":
    console.log("I play the trumpet");
    break;
  case "flute":
    console.log("I play the flute");
    break;
  case "oboe":
    console.log("I play the oboe");
    break;
  default:
    console.log("I don't play an instrument. Sorry");
    break;
}
```

## Instructions Break manquantes

Dans cet exemple, la correspondance serait `case` 2. Mais sans instruction `break`, l'ordinateur continuera vers `case` 3 et la clause `default`.

Vous devriez voir trois instructions `console.log` car une instruction `break` n'a pas été incluse.

```js
switch (2) {
  case 1:
    console.log("Number 1 was chosen");
  case 2:
    console.log("Number 2 was chosen");
  case 3:
    console.log("Number 3 was chosen");
  default:
    console.log("No number was chosen");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-04-at-10.20.10-PM.png)

## Où placer la clause Default

La convention standard est de placer le `default` comme dernière clause. Mais vous pouvez également le placer avant d'autres cas.

```js
const food = "nuts";

switch (food) {
  case "cake":
    console.log("I like cake");
    break;
  case "pizza":
    console.log("I like pizza");
    break;
  default:
    console.log("I like all foods");
    break;
  case "ice cream":
    console.log("I like ice cream");
    break;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-04-at-11.22.42-PM.png)

L'ordinateur parcourra chaque cas et trouvera une correspondance. Puisque la variable `food` ne correspond à aucun des cas, la clause `default` sera exécutée.

## Plusieurs cas pour une seule opération

Il peut arriver que vous ayez une opération qui sera la même pour plusieurs cas.

Au lieu d'écrire le même `console.log` pour chaque cas, nous pouvons omettre les instructions `break` et placer une opération unique après le groupe de cas.

Le message "This country is in Europe." sera affiché dans la console si `country` correspond à l'un des cas de `"France"`, `"Spain"`, `"Ireland"` ou `"Poland"`.

```js
const country = "Ireland";
switch (country) {
  case "France":
  case "Spain":
  case "Ireland":
  case "Poland":
    console.log("This country is in Europe.");
    break;
  case "United States":
  default:
    console.log("This country is not in Europe.");
}
```

## Portée de bloc et instructions Switch

Cet exemple produira un message d'erreur, car la variable `message` a déjà été déclarée et vous ne pouvez pas avoir le même nom de variable dans la même portée de bloc.

```js
const errand = "Going Shopping";
switch (errand) {
  case "Going to the Dentist":
    let message = "I hate going to the dentist";
    console.log(message);
    break;
  case "Going Shopping":
    let message = "I love to shop";
    console.log(message);
    break;
  default:
    console.log("No errands");
    break;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-05-at-12.45.29-AM.png)

Pour éliminer ce message d'erreur, les cas doivent être enveloppés dans un ensemble d'accolades.

```js
const errand = "Going Shopping";
switch (errand) {
  case "Going to the Dentist": {
    let message = "I hate going to the dentist";
    console.log(message);
    break;
  }
  case "Going Shopping": {
    let message = "I love to shop";
    console.log(message);
    break;
  }
  default: {
    console.log("No errand");
    break;
  }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-05-at-12.51.50-AM.png)

## Conclusion

Utiliser une instruction `switch` peut être une alternative à une instruction `if else`. Une instruction `switch` compare la valeur d'une `expression` à plusieurs cas.

Les instructions `switch` vérifieront l'égalité stricte. Dans cet exemple, puisque `"2"!== 2`, la clause `default` sera exécutée.

```js
switch (2) {
  case "2":
    console.log("Number 2 in a string");
    break;
  case "3":
    console.log("Number 3 in a string");
    break;
  default:
    console.log("Number not present");
    break;
}
```

Les instructions `break` sortiront du `switch` lorsque le `case` sera trouvé. Si les instructions `break` ne sont pas présentes, alors l'ordinateur continuera à travers l'instruction `switch` même si une correspondance est trouvée.

J'espère que vous avez apprécié cet article sur les instructions `switch`.