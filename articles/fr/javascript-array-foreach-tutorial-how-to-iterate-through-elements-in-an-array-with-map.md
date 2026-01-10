---
title: Tutoriel JavaScript Array.forEach() – Comment itérer à travers les éléments
  d'un tableau
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-24T17:16:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-foreach-tutorial-how-to-iterate-through-elements-in-an-array-with-map
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/forEachtwo.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Tutoriel JavaScript Array.forEach() – Comment itérer à travers les éléments
  d'un tableau
seo_desc: 'In JavaScript, you''ll often need to iterate through an array collection
  and execute a callback method for each iteration. And there''s a helpful method
  JS devs typically use to do this: the forEach() method.

  The forEach() method calls a specified call...'
---

En JavaScript, vous aurez souvent besoin d'itérer à travers une collection de tableau et d'exécuter une méthode de rappel pour chaque itération. Et il existe une méthode utile que les développeurs JS utilisent typiquement pour cela : la méthode `forEach()`.

La méthode `forEach()` appelle une fonction de rappel spécifiée une fois pour chaque élément sur lequel elle itère à l'intérieur d'un tableau. Tout comme d'autres itérateurs de tableau tels que `map` et `filter`, la fonction de rappel peut prendre trois paramètres :

* L'élément actuel : il s'agit de l'élément du tableau qui est actuellement en cours d'itération.
  
* Son index : il s'agit de la position d'index de cet élément au sein du tableau
  
* Le tableau cible : il s'agit du tableau qui est en cours d'itération
  

La méthode `forEach` ne retourne pas un nouveau tableau comme d'autres itérateurs tels que `filter`, `map` et `sort`. Au lieu de cela, la méthode retourne `undefined`. Elle n'est donc pas chaînable comme ces autres méthodes.

Une autre chose à propos de `forEach` est que vous ne pouvez pas terminer la boucle (avec l'instruction break) ou la faire sauter une itération (avec l'instruction continue). En d'autres termes, vous ne pouvez pas la contrôler.

La seule façon de terminer une boucle `forEach` est de lancer une exception à l'intérieur de la fonction de rappel. Ne vous inquiétez pas, nous verrons tout cela en pratique bientôt.

## Comment utiliser la méthode `forEach()` en JavaScript

Imaginez qu'un groupe d'étudiants se soit aligné pour un appel de routine. Le coordinateur de la classe se déplace le long de la ligne et appelle le nom de chaque étudiant tout en marquant s'ils sont présents ou absents.

Il est important de noter que le coordinateur ne change pas l'ordre des étudiants dans la ligne. Il les garde également dans la même ligne après avoir terminé l'appel. Tout ce qu'il fait, c'est effectuer une action (son inspection) sur chacun d'eux.

Dans les exemples suivants, en gardant ce scénario à l'esprit, nous verrons comment vous pouvez utiliser la méthode `forEach` en JavaScript pour résoudre des problèmes réels.

## Exemples de la méthode `forEach()` en JavaScript

### Comment supprimer le premier nombre impair dans un tableau avec `forEach()`

Dans cet exemple, nous avons un tableau qui contient un nombre impair à la première position et plusieurs nombres pairs qui le suivent. Mais nous voulons que les nombres de ce tableau soient tous pairs. Nous allons donc supprimer le nombre impair du tableau en utilisant la boucle `forEach()` :

```js
let numbers = [3, 6, 8, 10, 12]
let odd = 3;

numbers.forEach(function(number) {
    if (number === odd) {
        numbers.shift() // 3 sera supprimé du tableau
    }
})

console.log(numbers);

[6, 8, 10, 12] // Tous pairs !
```

### Comment accéder à la propriété Index avec `forEach()`

Dans cet exemple, nous allons exécuter une fonction `rollCall` pour chaque étudiant parcouru à l'intérieur du tableau. La fonction `rollCall` enregistre simplement une chaîne concernant chacun des étudiants dans la console.

```js
names = ["anna", "beth", "chris", "daniel", "ethan"]

function rollCall(name, index) {
    console.log(`L'étudiant numéro ${index + 1} - ${name} est présent ? Oui !`)
    ;}

names.forEach((name, index) => rollCall(name, index));


/*
"L'étudiant numéro 1 - anna est présent ? Oui !"
"L'étudiant numéro 2 - beth est présent ? Oui !"
"L'étudiant numéro 3 - chris est présent ? Oui !"
"L'étudiant numéro 4 - daniel est présent ? Oui !"
"L'étudiant numéro 5 - ethan est présent ? Oui !"
*/
```

Dans cet exemple, la seule information que nous avions sur chaque étudiant était leur nom. Cependant, nous voulons également savoir quels pronoms chaque étudiant utilise. En d'autres termes, nous voulons une propriété de pronom définie pour chaque étudiant.

Nous définissons donc chaque étudiant comme un objet avec deux propriétés, nom et pronom :

```js
names = [
    {name:"anna",pronoun: "elle"},
    {name: "beth",pronoun: "iel"},
    {name: "chris",pronoun: "il"},
    {name: "daniel",pronoun: "il"},
    {name: "ethan",pronoun: "il"}
]

function rollCall(student, index) {
    console.log(`L'étudiant numéro ${index + 1} est ${student.name}. Est-ce que ${student.pronoun} est présent ? Oui !`);
}

names.forEach((name, index) => rollCall(name, index));

/*
"L'étudiant numéro 1 est anna. Est-ce qu'elle est présente ? Oui !"
"L'étudiant numéro 2 est beth. Est-ce que iel est présent ? Oui !"
"L'étudiant numéro 3 est chris. Est-ce qu'il est présent ? Oui !"
"L'étudiant numéro 4 est daniel. Est-ce qu'il est présent ? Oui !"
"L'étudiant numéro 5 est ethan. Est-ce qu'il est présent ? Oui !"
*/
```

Nous enregistrons le message d'appel de chaque étudiant dans la console, puis nous effectuons une vérification pour voir quel pronom l'étudiant utilise, et enfin nous passons dynamiquement le pronom précis dans le cadre de la chaîne.

### Comment copier un tableau dans un nouveau tableau avec `forEach()` en JavaScript

Après trois années d'études, il est maintenant temps pour chacun des étudiants de terminer leurs études. Dans notre JavaScript, nous définissons deux tableaux : `stillStudent` et `nowGraduated`. Comme vous l'avez probablement deviné, `stillStudent` contient les étudiants juste avant leur remise de diplôme.

Ensuite, la boucle `forEach` prend chacun des étudiants et appelle la fonction `graduateStudent` sur celui-ci.

Dans cette fonction, nous construisons un objet avec deux propriétés : le nom de l'étudiant ainsi que la position à laquelle il a obtenu son diplôme. Ensuite, nous passons le nouvel objet au tableau `nowGraduated`. À ce moment-là, l'étudiant est devenu un diplômé.

Cet exemple montre également comment vous pouvez utiliser la méthode `forEach()` pour copier un tableau dans un nouveau tableau.

```js
let stillStudent = ["anna", "beth", "chris", "daniel", "ethan"]
let nowGraduated = []

function graduateStudent(student, index) {
    let object = { name: student, position: index + 1}
    nowGraduated[index] = object
}

stillStudent.forEach((name, index) => graduateStudent(name, index));

console.log(nowGraduated);

/*
[
    { name: "anna", position: 1}, 
    { name: "beth", position: 2}, 
    { name: "chris", position: 3}, 
    { name: "daniel", position: 4}, 
    { name: "ethan", position: 5}]
]
*/
```

### Comment vérifier l'élément suivant dans un tableau avec le paramètre `array`

À un moment donné, l'enseignant devra vérifier si la liste contient un élément particulier suivant sur la liste. Dans un tel cas, l'enseignant devra avoir une vue d'ensemble de toute la liste. De cette façon, il peut dire s'il y a un prochain étudiant à appeler.

Dans notre JavaScript, nous pouvons reproduire cela car la fonction de rappel peut également accéder au paramètre `array` (le troisième). Ce paramètre représente le tableau cible, qui est `name`.

Nous vérifions s'il y a un élément suivant (étudiant) dans le tableau. Si c'est le cas, nous passons la chaîne `positive` à la variable `nextItem`. S'il n'y en a pas, nous passons la chaîne `negative` à la variable. Ensuite, pour chaque itération, nous vérifions si **cet** étudiant est bien le dernier.

```js
names = ["anna", "beth", "chris", "daniel", "ethan"]

function rollCall(name, index, array) {
    let nextItem = index + 1 < array.length ? "positif" : "negatif"
    console.log(`L'étudiant numéro ${index + 1} - ${name} est présent ? Oui !. Y a-t-il un prochain étudiant ? ${nextItem} !`);
}

names.forEach((name, index, array) => rollCall(name, index, array))

/*
"L'étudiant numéro 1 - anna est présent ? Oui !. Y a-t-il un prochain étudiant ? positif !"
"L'étudiant numéro 2 - beth est présent ? Oui !. Y a-t-il un prochain étudiant ? positif !"
"L'étudiant numéro 3 - chris est présent ? Oui !. Y a-t-il un prochain étudiant ? positif !"
"L'étudiant numéro 4 - daniel est présent ? Oui !. Y a-t-il un prochain étudiant ? positif !"
"L'étudiant numéro 5 - ethan est présent ? Oui !. Y a-t-il un prochain étudiant ? negatif !"
*/
```

## Vous ne pouvez pas sortir d'une boucle `forEach`, alors utilisez `every()` à la place

Vous souvenez-vous lorsque j'ai mentionné que, par nature, vous ne pouvez pas sortir (c'est-à-dire quitter) une boucle `forEach` ? Une fois qu'elle est démarrée, elle s'exécutera jusqu'à ce qu'elle atteigne le dernier élément du tableau. Donc, si vous insérez une instruction `break`, elle retournera une `SyntaxError` :

```js
let numbers = [2, 4, 5, 8, 12]
let odd = 5;

numbers.forEach(function(number) {
    if (number === odd) {
        break; // oops, cela ne va pas fonctionner !
    }
})
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/illegal.png align="left")

Normalement, vous voudriez sortir d'une boucle si vous finissez par atteindre ce que vous avez l'intention de faire avant d'atteindre le dernier élément. Dans notre exemple ci-dessus, nous avons déjà trouvé le nombre impair (5), donc il n'y avait alors plus besoin de continuer à itérer sur les éléments restants (8 et 12).

Si vous voulez sortir de la boucle sous une certaine condition, alors vous devrez utiliser l'une des méthodes suivantes :

* boucle `for`
  
* [boucle `for…of` ou `for…in`](https://futurestud.io/tutorials/node-js-for-of-vs-for-in-loops)
  
* `Array.some()`
  
* `Array.every()`
  
* `Array.find()`
  

Voici comment vous pouvez sortir d'une boucle avec `Array.every()` :

```js
let numbers = [2, 4, 5, 8, 12]
let odd = 5;

numbers.every(number => {
  if (number == odd) {
    return false;
  }

  console.log(number);
  
  return true;
});

// 2 4
```

## Conclusion

Dans ce tutoriel, j'ai présenté la méthode `forEach`, illustré son fonctionnement avec une analogie simple, et je vous ai également donné quelques exemples pratiques de son utilisation dans le code JavaScript.

J'espère que vous avez trouvé quelque chose d'utile dans cet article.

**Si vous souhaitez en apprendre davantage sur le développement Web, n'hésitez pas à visiter mon** [Blog](https://ubahthebuilder.tech)**.**

Merci d'avoir lu et à bientôt.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).