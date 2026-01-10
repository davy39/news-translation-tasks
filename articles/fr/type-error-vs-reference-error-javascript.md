---
title: Erreur de Type vs Erreur de Référence en JavaScript – Quelle est la Différence
  ?
subtitle: ''
author: Tejan Singh
co_authors: []
series: null
date: '2023-02-15T17:12:30.000Z'
originalURL: https://freecodecamp.org/news/type-error-vs-reference-error-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-kim-stiver-909256.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
seo_title: Erreur de Type vs Erreur de Référence en JavaScript – Quelle est la Différence
  ?
seo_desc: 'As a JavaScript developer, you''ve likely encountered different types of
  errors while coding. Most of the time these will be type errors or reference errors.
  But have you ever wondered what they mean?

  Have you ever tried reading about the error type s...'
---

En tant que développeur JavaScript, vous avez probablement rencontré différents types d'erreurs lors du codage. La plupart du temps, il s'agira d'erreurs de type ou d'erreurs de référence. Mais vous êtes-vous déjà demandé ce qu'elles signifient ?

Avez-vous déjà essayé de lire le type d'erreur spécifié par l'interpréteur avant de résoudre ces erreurs ? Si ce n'est pas le cas, vous devriez, car connaître ces erreurs peut vous aider à résoudre vos problèmes.

Par exemple, lorsque vous rencontrez une erreur, vous la recherchez probablement sur Google. Vous copiez et collez l'erreur entière et essayez de trouver la solution en visitant divers sites web et forums. C'est une méthode d'essai et d'erreur pour trouver et résoudre les bugs.

Mais que se passerait-il si vous saviez déjà pourquoi l'erreur se produit généralement ? Cela vous ferait gagner du temps que vous passeriez autrement à chercher des solutions en ligne. Au lieu de cela, vous pourriez commencer à chercher des solutions par vous-même simplement en regardant le type d'erreur.

Dans ce guide, vous apprendrez les deux types d'erreurs les plus couramment rencontrés, qui sont les erreurs de type et les erreurs de référence. Vous apprendrez pourquoi elles se produisent, la différence entre elles et comment éviter de les obtenir.

Note : Il existe d'autres types d'erreurs en JavaScript comme les erreurs de syntaxe, les erreurs internes, les erreurs de plage et les erreurs d'évaluation. Mais le champ de cet article est limité aux deux erreurs les plus couramment rencontrées.

## Qu'est-ce qu'une Erreur de Type ?

Les erreurs de type se produisent lorsque vous utilisez quelque chose qui n'est pas destiné à être utilisé de cette manière particulière. Par exemple, utiliser un tournevis pour enfoncer un clou, au lieu d'utiliser un marteau.

Comprenons cela à l'aide d'un exemple :

```javascript
let a = 1
console.log(a()) 

//output
Uncaught TypeError: a is not a function
```

Ici, `a` est une variable initialisée avec une valeur. Vous avez rencontré une erreur parce que vous avez essayé d'appeler une fonction avec le nom de la variable. Une variable ne peut pas être appelée comme une fonction. Les fonctions et les variables fonctionnent différemment. Donc dans ce cas, vous avez obtenu une erreur de type. Vous avez utilisé la variable `let` différemment de son _type_. 

Cela nous donne une erreur de type.

Solution : Pour résoudre cette erreur, vous devez référencer la variable dans la console, comme elle est destinée à être utilisée. Dans ce cas, vous passez `a` comme une variable au lieu d'une fonction.

```javascript
let a = 1
console.log(a)

//output
1
```

Prenons un autre exemple :

```javascript
const a = 1
a = 2 // vous réassignez une variable de type const

//output
TypeError: Assignment to constant variable.

```

Ici, nous avons réassigné la variable de type `const` `a` à une nouvelle valeur. Mais vous ne pouvez pas changer les variables const comme cela, donc dans ce cas, vous obtenez une erreur de type.

Solution : ne réassignez jamais une variable de type `const` une fois que vous l'avez définie.

```javascript
const a = 1
const b = 2
console.log(a, b)

//output
1 2
```

Voici un autre exemple utilisant un tableau :

```javascript
const myArray = [1,2,3,4]
myArray = myArray.push(5) // réassigner le tableau

//output
TypeError: Assignment to constant variable.
```

Dans ce cas, nous avons réassigné le `const` type `myArray`. Cela nous donne une erreur de type car encore une fois, ce type de réassignation est contraire aux propriétés de `const`. 

Solution :

```javascript
const myArray = [1,2,3,4]
myArray.push(5) // vous pouvez ajouter de nouvelles valeurs

//output
[1,2,3,4,5]
```

Vous pouvez facilement ajouter de nouvelles valeurs au tableau sans le réassigner. Cela ne vous donnera aucune erreur. Ajouter des valeurs dans un tableau est autorisé. De cette façon, vous pouvez éviter d'obtenir l'erreur.

### Comment éviter d'obtenir une erreur de type

Le moyen le plus simple de prévenir les erreurs de type est d'éviter d'utiliser les mêmes noms pour différentes variables et fonctions. 

Si vous utilisez des noms différents, vous ne serez pas confus ou ne remplacerez pas l'un par l'autre, et vous pourrez facilement éviter d'obtenir cette erreur.

Une autre façon est de vous assurer que vous utilisez les variables comme elles sont destinées à être utilisées. Au lieu d'utiliser `const` lorsque vous devez réassigner une valeur, utilisez `let` (qui permet ce type de changement).

## Qu'est-ce qu'une Erreur de Référence ?

Les erreurs de référence se produisent lorsque vous essayez de référencer ou d'utiliser quelque chose qui n'existe pas. Par exemple, chercher un tournevis dans votre boîte à outils, mais il n'y est pas.

Comprenons cela à l'aide d'un exemple :

```javascript
let a = 1
console.log(b) // variable non définie utilisée

//output
Uncaught ReferenceError: b is not defined
```

Ici, `a` est une variable initialisée avec une valeur. Nous avons rencontré une erreur parce que nous avons essayé de logger la variable `b` qui n'existe pas. Nous n'avions pas encore déclaré une telle variable, donc nous avons obtenu une erreur de référence ici.

Solution : n'utilisez que les variables que vous avez déclarées pour éviter d'obtenir une erreur.

```javascript
let a = 1
console.log(a) // variable définie utilisée

//output
1
```

Voici un autre exemple :

```javascript
if(true){
    let a = 1
}

console.log(a)

//output
ReferenceError: a is not defined
```

Dans cet exemple, nous essayons d'accéder à la variable `a` de type `let` en dehors de son bloc. L'interpréteur ne peut pas la trouver en dehors du bloc. Cela nous donne une erreur.

Solution :

```javascript
if(true){
    let a = 1
    console.log(a)
}


//output
1
```

L'utilisation de la variable à l'intérieur de son bloc ou de sa portée ne vous donnera aucune erreur.

Prenons un autre exemple, mais celui-ci peut être difficile à comprendre.

```javascript
if(true){
	console.log(a)
    let a = 1
}


//output
ReferenceError: Cannot access 'a' before initialization
```

`a` est toujours dans sa portée. Mais nous obtenons une erreur. Pourquoi ? Parce que nous essayons d'utiliser la variable avant de l'avoir définie. Cela n'est pas autorisé et va à l'encontre des propriétés de la variable `let`. 

Solution : utilisez la variable `let` uniquement après l'avoir définie. 

```javascript
if(true){
	let a = 1
	console.log(a)
    
}

//output
1
```

### Comment éviter d'obtenir une erreur de référence

Le moyen le plus simple d'éviter d'obtenir des erreurs de référence est de référencer ou d'accéder uniquement aux variables définies. N'utilisez que les variables qui existent. 

Vous pouvez également utiliser des instructions conditionnelles et la gestion des erreurs pour éviter d'exécuter du code si une variable ou une fonction n'existe pas.

## Conclusion

Vous pouvez facilement déboguer votre code lorsque vous savez déjà comment résoudre vos erreurs. Il est bon de connaître les erreurs couramment rencontrées et comment les éviter. Cela vous fera gagner du temps à chercher des solutions en ligne et à perdre des heures à essayer de trouver une solution lorsque quelques connaissances et une prise de conscience de ces choses peuvent aider.