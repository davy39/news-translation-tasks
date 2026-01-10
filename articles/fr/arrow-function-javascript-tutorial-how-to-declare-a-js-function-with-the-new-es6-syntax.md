---
title: Tutoriel sur les fonctions fléchées JavaScript – Comment déclarer une fonction
  JS avec la nouvelle syntaxe ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T15:38:35.000Z'
originalURL: https://freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/nick-fewings-zF_pTLx_Dkg-unsplash-1.jpg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: learn to code
  slug: learn-to-code
- name: programing
  slug: programing
seo_title: Tutoriel sur les fonctions fléchées JavaScript – Comment déclarer une fonction
  JS avec la nouvelle syntaxe ES6
seo_desc: 'By Amy Haddad

  You’ve probably seen arrow functions written a few different ways.

  //example 1

  const addTwo = (num) => {return num + 2;};


  //example 2

  const addTwo = (num) => num + 2;


  //example 3

  const addTwo = num => num + 2;


  //example 4

  const addTw...'
---

Par Amy Haddad

Vous avez probablement vu des fonctions fléchées écrites de plusieurs manières différentes.

```JS
//exemple 1
const addTwo = (num) => {return num + 2;};

//exemple 2
const addTwo = (num) => num + 2;

//exemple 3
const addTwo = num => num + 2;
 
//exemple 4
const addTwo = a => {
 const newValue = a + 2;
 return newValue;
};
```

Certaines ont des parenthèses autour des paramètres, tandis que d'autres non. Certaines utilisent des accolades et le mot-clé `return`, d'autres non. Une d'entre elles s'étend même sur plusieurs lignes, tandis que les autres consistent en une seule ligne.

Intéressamment, lorsque nous invoquons les fonctions fléchées ci-dessus avec le même argument, nous obtenons le même résultat.

```JS
console.log(addTwo(2));
//Résultat : 4
```

Comment savoir quelle syntaxe de fonction fléchée utiliser ? C'est ce que cet article va révéler : comment déclarer une fonction fléchée.

## Une différence majeure

Les fonctions fléchées sont une autre façon—plus concise—d'écrire des expressions de fonction. Cependant, elles n'ont pas leur propre liaison au mot-clé **`this`**. 

```JS
//Expression de fonction
const addNumbers = function(number1, number2) {
   return number1 + number2;
};

//Expression de fonction fléchée
const addNumbers = (number1, number2) => number1 + number2;
```

Lorsque nous invoquons ces fonctions avec les mêmes arguments, nous obtenons le même résultat.

```JS
console.log(addNumbers(1, 2));
//Résultat : 3
```

Il y a une différence syntaxique importante à noter : les fonctions fléchées utilisent la flèche **`=>`** au lieu du mot-clé **`function`**. Il y a d'autres différences à connaître lorsque vous écrivez des fonctions fléchées, et c'est ce que nous allons explorer ensuite.

## Parentheses

Certaines fonctions fléchées ont des parenthèses autour des paramètres et d'autres non.

```JS
//Exemple avec parenthèses
const addNums = (num1, num2) => num1 + num2;

//Exemple sans parenthèses
const addTwo = num => num + 2;
```

Il s'avère que le nombre de paramètres d'une fonction fléchée détermine si nous devons inclure des parenthèses ou non.

Une fonction fléchée avec **zéro paramètre** nécessite des parenthèses.

```JS
const hello = () => "hello";
console.log(hello());
//Résultat : "hello"
```

Une fonction fléchée avec **un paramètre** ne nécessite _pas_ de parenthèses. En d'autres termes, les parenthèses sont facultatives. 

```JS
const addTwo = num => num + 2;
```

Nous pouvons donc ajouter des parenthèses à l'exemple ci-dessus et la fonction fléchée fonctionne toujours.

```JS
const addTwo = (num) => num + 2;
console.log(addTwo(2));
//Résultat : 4
```

Une fonction fléchée avec **plusieurs paramètres** nécessite des parenthèses.

```JS
const addNums = (num1, num2) => num1 + num2;
console.log(addNums(1, 2));
//Résultat : 3
```

Les fonctions fléchées supportent également les **paramètres rest** et la **destructuration**. Ces deux fonctionnalités nécessitent des parenthèses.

Voici un exemple de fonction fléchée avec un **paramètre rest**.

```JS
const nums = (first, ...rest) => rest;
console.log(nums(1, 2, 3, 4));
//Résultat : [ 2, 3, 4 ]
```

Et voici une fonction qui utilise la **destructuration**.

```JS
const location = {
   country: "Greece",
   city: "Athens"
};

const travel = ({city}) => city;

console.log(travel(location));
//Résultat : "Athens"
```

Pour résumer : s'il n'y a qu'un seul paramètre—et que vous n'utilisez pas de paramètres rest ou de destructuration—alors les parenthèses sont facultatives. Sinon, assurez-vous de les inclure.

## Le corps de la fonction

Maintenant que nous avons couvert les règles des parenthèses, tournons-nous vers le corps de la fonction d'une fonction fléchée.

Le corps d'une fonction fléchée peut avoir soit un ["corps concis" ou "corps de bloc"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#:~:text=An%20arrow%20function%20expression%20is,cannot%20be%20used%20as%20constructors.). Le type de corps influence la syntaxe.

D'abord, la syntaxe "corps concis".

```JS
const addTwo = a => a + 2;
```

La syntaxe "corps concis" est justement cela : elle est concise ! Nous n'utilisons pas le mot-clé `return` ni les accolades. 

Si vous avez une fonction fléchée d'une seule ligne (comme l'exemple ci-dessus), alors la valeur est retournée implicitement. Vous pouvez donc omettre le mot-clé `return` et les accolades. 

Maintenant, regardons la syntaxe "corps de bloc".

```JS
const addTwo = a => {
    const total = a + 2;
    return total;
}
```

Remarquez que nous utilisons _à la fois_ les accolades et le mot-clé `return` dans l'exemple ci-dessus. 

Vous voyez généralement cette syntaxe lorsque le corps de la fonction fait plus d'une ligne. Et c'est un point clé : enveloppez le corps d'une fonction fléchée multi-ligne dans des accolades et utilisez le mot-clé `return`.

### Objets et fonctions fléchées

Il y a une autre nuance syntaxique à connaître : enveloppez le corps de la fonction dans des parenthèses lorsque vous voulez retourner une [expression littérale d'objet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

```JS
const f = () => ({
 city:"Boston"
})
console.log(f().city)
```

Sans les parenthèses, nous obtenons une erreur.

```JS
const f = () => {
   city:"Boston"
}
//Résultat : erreur
```

Si vous trouvez la syntaxe des fonctions fléchées un peu confuse, vous n'êtes pas seul. Il faut un certain temps pour s'y familiariser. Mais être conscient de vos options et de vos exigences sont des étapes dans cette direction.

_Je parle de l'apprentissage de la programmation et des meilleures façons de s'y prendre (_[amymhaddad.com](https://amymhaddad.com/)).