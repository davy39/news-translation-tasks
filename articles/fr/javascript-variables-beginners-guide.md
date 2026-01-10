---
title: Variables JavaScript – Un guide pour débutants sur var, const et let
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-30T18:24:36.000Z'
originalURL: https://freecodecamp.org/news/javascript-variables-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Screen-Shot-2020-11-22-at-8.51.01-PM.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: variables
  slug: variables
seo_title: Variables JavaScript – Un guide pour débutants sur var, const et let
seo_desc: 'By Madison Kanna

  Variables are a fundamental concept in any programming language. In JavaScript,
  you can declare variables by using the keywords var, const, or let.

  In this article, you’ll learn why we use variables, how to use them, and the differen...'
---

Par Madison Kanna

Les variables sont un concept fondamental dans tout langage de programmation. En JavaScript, vous pouvez déclarer des variables en utilisant les mots-clés var, const ou let.

Dans cet article, vous apprendrez pourquoi nous utilisons des variables, comment les utiliser et les différences entre const, let et var.

## **À quoi servent les variables en JavaScript ?**

Dans le contexte de la programmation, les données sont des informations que nous utilisons dans nos programmes informatiques. Par exemple, votre nom d'utilisateur Twitter est une donnée.

Une grande partie de la programmation consiste à manipuler ou afficher des données. Pour ce faire, les programmeurs ont besoin d'un moyen de stocker et de suivre les données. Illustrons cela avec un exemple.

Commençons par ouvrir notre console JavaScript. Pour lancer votre console JavaScript sur Chrome, vous pouvez utiliser le raccourci Ctrl + Shift + J sur Windows et Linux. Pour Mac, utilisez Cmd + Option + J.

Une fois la console lancée, pensez à l'âge actuel de votre chien ou chat (ou à un nombre similaire si vous n'avez pas d'animaux de compagnie) et entrez-le dans la console.

```js
4
```

Maintenant, si nous voulons nous référer à ce nombre à nouveau ? Nous devrons le taper une deuxième fois.

Nous avons besoin d'un moyen de nous référer à cette donnée afin de pouvoir la réutiliser dans tout notre programme.

## **Introduction aux variables en JavaScript**

Une analogie utile est de penser aux variables comme des étiquettes pour nos valeurs. Imaginez un contenant de myrtilles avec une étiquette marquée myrtilles. Dans cet exemple, la variable, _myrtilles_, pointe vers une valeur, qui est les myrtilles elles-mêmes.

Déclarons une variable, age, et utilisons l'opérateur d'assignation (le signe égal) pour assigner notre valeur, 4, à cette variable. Nous utiliserons le mot-clé var.

```js
var age = 4
```

Les variables sont la manière dont les programmeurs donnent un nom à une valeur afin que nous puissions la réutiliser, la mettre à jour ou simplement la suivre. Les variables peuvent être utilisées pour stocker n'importe quel type JavaScript.

Maintenant que nous avons assigné cette valeur à la variable age, nous pouvons nous y référer plus tard. Si vous tapez maintenant la variable age dans votre console, vous obtiendrez la valeur 4.

## Comment utiliser le mot-clé var en JavaScript

Les mots-clés en JavaScript sont des mots réservés. Lorsque vous utilisez le mot-clé var, vous indiquez à JavaScript que vous allez déclarer une variable.

Lorsque vous utilisez le mot-clé var, les variables peuvent être réassignées. Nous allons démontrer cela en déclarant d'abord une nouvelle variable, name, et en lui assignant la valeur Madison.

```
var name = 'Madison'
```

Ensuite, nous allons réassigner cette variable pour qu'elle pointe vers la valeur d'un autre nom, Ben.

```
name = 'Ben'
```

Maintenant, si vous exécutez `console.log(name)`, vous obtiendrez la sortie Ben.

Lorsque vous utilisez le mot-clé var, les variables peuvent également être déclarées sans valeur initiale.

```
var year
```

Ici, nous avons déclaré une variable `year` mais elle ne pointe vers aucune valeur. Plus tard, si nous voulons qu'elle pointe vers une valeur, nous pouvons utiliser l'opérateur d'assignation pour le faire.

```
year = 2020
```

Maintenant, notre variable year pointera vers la valeur 2020.

Lorsque JavaScript a été créé pour la première fois, la seule façon de déclarer une variable était avec le mot-clé var.

Dans les mises à jour récentes de JavaScript (ECMAScript2015), `const` et `let` ont été créés comme d'autres mots-clés pour déclarer des variables.

Pour expliquer pourquoi ils étaient nécessaires, nous allons examiner les problèmes avec le mot-clé var. Pour examiner ces problèmes, nous allons apprendre ce qu'est la portée.

## Qu'est-ce que la portée ?

La portée fait référence à l'endroit dans notre code où les variables sont disponibles pour être utilisées. Lorsqu'une variable est _globale_, cela signifie qu'elle est disponible n'importe où dans votre programme. Examinons un exemple.

Prenez le code suivant et entrez-le dans votre console.

```js
var name = 'Bob'
function printName() {
    console.log(name)
}
printName()
```

Ici, nous avons créé et appelé une fonction, printName, qui imprimera la valeur de la variable var, `Madison`. Vous verrez cela imprimé dans votre console.

Parce que notre var a été créée en dehors de la fonction, elle est globale. Cela signifie qu'elle est disponible n'importe où dans votre code, y compris à l'intérieur de toute fonction. C'est pourquoi notre fonction, printName, a accès à la variable name.

Créons maintenant une variable qui est locale à une fonction. Cela signifie que la variable n'est accessible qu'à l'intérieur de la fonction dans laquelle elle a été créée. Cet exemple suivant sera très similaire au code ci-dessus, mais avec un placement différent de la variable.

```js
function printYear() {
 var year = 2020
}
console.log(year)
```

Maintenant, dans notre console, nous obtiendrons une erreur : `year is not defined.` Cela est dû au fait que la variable var year est locale à la fonction. C'est-à-dire qu'elle n'existe qu'à l'intérieur de la fonction dans laquelle elle a été créée. Nous n'avons pas accès à elle en dehors de la fonction, ce qui est l'endroit où nous essayons d'y accéder lorsque nous exécutons notre console.log.

Les variables locales à une fonction sont utiles pour les programmeurs car nous voulons souvent créer des variables qui ne sont utiles ou nécessaires qu'à l'intérieur d'une certaine fonction. La création de variables globales peut également entraîner des erreurs ou des mistakes.

Maintenant que nous avons une compréhension de base de la portée, nous pouvons revenir à notre discussion sur les problèmes avec le mot-clé var.

## Problèmes avec le mot-clé var en JavaScript

Examinons un autre exemple.

Nous allons créer une variable, `age`. Ensuite, nous allons écrire une instruction if qui vérifie si age a une valeur, et si c'est le cas, retourne une console.log du nombre qui est le double de cet âge.

Ceci est un exemple simplifié, mais nous allons d'abord vérifier si age a une valeur car nous voulons nous assurer que nous ajoutons à une valeur valide.

```js
var age = 27
If (age) {
 var doubleAge = age + age
 console.log(`Double your current age is ${yearPlusTwenty}`)
}
```

Maintenant, dans notre console, vous verrez `Double your current age is 47`.

Notre variable, `doubleAge`, est maintenant une variable globale. Si vous entrez `doubleAge` dans votre console, vous verrez que vous avez accès à celle-ci.

```js
doubleAge
47
```

Comme discuté précédemment, les variables créées avec le mot-clé var sont locales à une fonction. Les variables locales à une fonction n'existent qu'à l'intérieur de la fonction dans laquelle elles ont été créées.

Mais puisque la variable `doubleAge` n'est pas à l'intérieur d'une fonction, cela signifie qu'elle a été portée globalement. C'est-à-dire que la variable `doubleAge` est maintenant disponible n'importe où dans notre code.

Le problème est que `doubleAge` est juste une variable que nous avons utilisée une fois à l'intérieur de notre `if statement`, et nous n'avons pas nécessairement besoin qu'elle soit disponible partout dans notre code. Elle a "fui" en dehors de l'instruction if dans laquelle elle a été créée, même si nous n'avions pas besoin qu'elle le fasse.

```js
var age = 27
if (age) {
 //Nous avons besoin de notre var doubleAge uniquement dans ce bloc de code entre nos accolades.
    var doubleAge = age + age
    console.log(`Double your current age is ${yearPlusTwenty}`)

}

doubleAge
47
//notre var doubleAge est disponible en dehors de ces accolades, sur la portée globale.
```

Il serait bien si nous avions un moyen de créer une variable qui *n'existe* qu'à l'intérieur de l'instruction if dans laquelle elle a été créée. En d'autres termes, le bloc de code qui existe entre les accolades.

```js
var age = 27
If (age) {
 //Nous voulons que notre variable n'existe que ici, où nous allons l'utiliser
 var doubleAge = age + age
 console.log(`Double your current age is ${yearPlusTwenty}`)
}
```

Pour aider à résoudre ce problème, les mots-clés const et let ont été introduits en JavaScript.

## Comment utiliser le mot-clé const en JavaScript

`const` fonctionne de manière similaire à var, mais avec quelques grandes différences.

Tout d'abord, `const` est _locale au bloc_, alors que var est _locale à la fonction_.

Qu'est-ce qu'un **bloc** ?

Un _bloc_ fait référence à tout espace entre une accolade ouvrante et fermante. Cela peut sembler confus au début. Réécrivons notre exemple précédent, mais cette fois en utilisant const au lieu de let lors de la déclaration de notre variable `doubleAge`.

```js
var age = 27
If (age) {
 const doubleAge = age + age
 console.log(`Double your current age is ${yearPlusTwenty}`)
}
```

Maintenant, tapez `doubleAge` dans votre console et appuyez sur entrer. Vous devriez obtenir une erreur, `doubleAge is not defined.` Cela est dû au fait que const est locale au bloc : _elle n'existe que dans le bloc où elle a été définie._

La variable `doubleAge` est "piégée" à l'intérieur des deux accolades où elle a été définie. Le code qui se trouve également à l'intérieur de ces accolades peut accéder à doubleAge, mais aucun code en dehors de celles-ci ne le peut.

En utilisant `const` au lieu de `var`, notre problème précédent est résolu. Notre variable `doubleAge` ne "fuit" plus dans notre portée globale inutilement. Au lieu de cela, elle n'existe qu'à l'intérieur du bloc où elle a été créée.

Comment fonctionnent les variables locales au bloc dans le contexte des fonctions ? Pour apprendre cela, créons puis appelons une fonction, `returnX`.

```js
function returnX() {
 const x = 1
 return x
}
returnX()
```

En appelant cette fonction `returnX`, nous pouvons voir que notre fonction retourne la valeur de x, qui est 1.

Si nous tapons ensuite `x`, nous obtiendrons `referenceError: x is not defined`. Cela est dû au fait que les fonctions sont également considérées comme des blocs, donc notre const `x` existera uniquement au sein de la fonction.

La prochaine chose à savoir sur const est qu'elle ne peut être déclarée qu'une seule fois. Tapez ce code dans votre console :

```js
const y = 1
const y = 2
```

Vous devriez voir une erreur, `Identifier 'x' has already been declared.`

Ceci est une différence entre var et const. Alors que const vous donnera une erreur, vous indiquant que vous avez déjà déclaré cette variable, le mot-clé var ne le fera pas.

```js
var x = 1
var x = 2
```

La variable `x` pointera vers la valeur `2` sans erreur. Cela peut causer des bugs pour vous en tant que programmeur, car peut-être que vous ne vouliez pas réassigner votre valeur à une nouvelle variable. Ainsi, utiliser const peut vous aider car vous recevrez une erreur si vous essayez accidentellement de réassigner une variable.

Ceci est une force du mot-clé `const` qui a été introduit comme une manière mise à jour et meilleure de créer des variables en JavaScript. Cependant, que faire des fois où vous voulez _vraiment_ mettre à jour votre variable ?

Examinons un exemple qui montre pourquoi nous voudrions faire cela.

Déclarons une variable, `adult`, et définissons-la sur `false`. Nous allons également créer une variable `age` et la définir sur `20`.

`const adult = false`

`const age = 20.`

Supposons que nous voulons vérifier l'âge d'un utilisateur et définir notre variable adult sur false si l'âge est supérieur à 18. Nous pouvons écrire une instruction if pour cela.

```js
if (age > 18) {
 adult = true
}
```

Que se passe-t-il lorsque nous exécutons ce code ?

Ici, nous verrons `Error: Assignment to constant variable.`

Cela est dû au fait que, conformément aux règles de `const`, nous ne pouvons pas redéclarer cette variable. C'est-à-dire que notre variable `age` pointe déjà vers la valeur true, et nous ne pouvons pas maintenant la faire pointer vers autre chose.

Si nous imprimons à nouveau `adult`, nous pouvons voir qu'elle est restée la même et conserve toujours la valeur `false`.

Nous ne pouvons pas réassigner notre variable `age`, et `const` fonctionne comme prévu. Cependant, que se passe-t-il si nous voulons vraiment réassigner cette variable ?

Souvent, les programmeurs voudront pouvoir redéclarer leurs variables.

C'est là que notre troisième mot-clé, let, entre en jeu.

## Comment utiliser le mot-clé let en JavaScript

Tout d'abord, passons en revue comment `let` est similaire à `const`.

`Let`, comme `const`, est locale au bloc. Si vous remplaciez const par let dans notre exemple `doubleAge` ci-dessus, cela fonctionnerait de la même manière.

Cependant, `let` diffère de `const` d'une manière fondamentale. Les variables déclarées avec le mot-clé `let` peuvent être redéclarées, alors que les variables créées avec le mot-clé `const` ne le peuvent pas. Passons en revue un exemple.

En utilisant le même exemple ci-dessus, remplacez const par let. Nous garderons notre variable age comme une `const` avec la valeur `20`.

```js
let adult = false
const age = 20
if (age > 18) {
    adult = true
}
```

Maintenant, si nous tapons `adult`, au lieu d'obtenir une erreur comme nous l'avons fait précédemment, nous verrons la sortie `true`.

En utilisant le mot-clé `let`, nous avons mis à jour notre variable pour qu'elle pointe vers la valeur `true` comme nous le voulions. Parfois en programmation, nous voudrons mettre à jour notre variable en fonction de certaines données que nous recevons. Nous pouvons utiliser `let` pour cela.

## Conclusion

En résumé, nous avons appris que les variables sont utilisées pour suivre et réutiliser les données dans nos programmes informatiques. La portée fait référence à l'endroit dans notre code où les variables sont disponibles pour être utilisées.

Les variables peuvent être déclarées en utilisant var, const ou let. Var est locale à la fonction, tandis que const et let sont locales au bloc. Les variables const ne peuvent pas être réassignées, alors que les variables let le peuvent.

Var, const et let peuvent être déroutants au début. Il peut être utile de lire différents tutoriels à leur sujet, ainsi que de tester votre propre code de différentes manières pour solidifier votre compréhension.

Avoir une solide fondation de var, const et let vous aidera non seulement au début de votre carrière en JavaScript, mais tout au long de celle-ci.

### Merci d'avoir lu !

Si vous avez aimé cet article, inscrivez-vous à [ma liste de diffusion](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f) où j'envoie mes derniers articles et annonce les réunions pour mon club de lecture de programmation.

Si vous avez des commentaires ou des questions sur cet article, n'hésitez pas à me tweeter @[madisonkanna.](https://twitter.com/Madisonkanna)