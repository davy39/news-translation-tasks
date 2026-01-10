---
title: Instruction vs Expression – Quelle est la Différence en Programmation ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-08T23:44:58.000Z'
originalURL: https://freecodecamp.org/news/statement-vs-expression-whats-the-difference-in-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/kaleidico-7lryofJ0H9s-unsplash.jpg
tags:
- name: beginner
  slug: beginner
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: syntax
  slug: syntax
- name: Tutorial
  slug: tutorial
seo_title: Instruction vs Expression – Quelle est la Différence en Programmation ?
seo_desc: 'By Ogundiran Ayobami

  Learning the syntax of a programming language is key if you want to use that language
  effectively. This is true for both new and experienced developers.

  And one of the most important things to pay attention to while learning a pr...'
---

Par Ogundiran Ayobami

Apprendre la syntaxe d'un langage de programmation est essentiel si vous souhaitez utiliser ce langage efficacement. Cela est vrai pour les développeurs débutants et expérimentés.

Et l'une des choses les plus importantes à surveiller lors de l'apprentissage d'un langage de programmation est de savoir si le code que vous manipulez est une instruction ou une expression.

Il peut parfois être confus de différencier les instructions et les expressions en programmation. Cet article vise donc à simplifier les différences afin que vous puissiez améliorer vos compétences en programmation et devenir un meilleur développeur.

## Qu'est-ce qu'une Expression en Programmation ?

![Homme caucasien senior tenant une bannière vide couvrant sa bouche avec sa main, choqué et effrayé par une erreur. expression surprise](https://images.unsplash.com/photo-1603792907191-89e55f70099a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDF8fHN1cnByaXNlZHxlbnwwfHx8fDE2NzA1MTMyNzI&ixlib=rb-4.0.3&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@krakenimages?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">krakenimages</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Une expression est tout mot ou groupe de mots ou de symboles qui représente une valeur. En programmation, une expression est une valeur, ou tout ce qui s'exécute et finit par être une valeur.

Il est nécessaire de comprendre qu'une valeur est unique. Par exemple, `const`, `let`, `2`, `4`, `s`, `a`, `true`, `false` et `world` sont des valeurs car chacune d'elles a une signification ou un caractère unique.

Examinons un exemple de code :

```js
const price = 500;
```

D'après le code ci-dessus, `const`, `price`, `=` et `500` sont des expressions car chacune d'elles a une signification ou une valeur définie et unique. Mais si nous les prenons toutes ensemble `const price = 500`, alors nous avons une instruction.

Examinons un autre exemple :

```js
let multiply = function (firstNumber, secondNumber) {
    return firstNumber * secondNumber;
}
```

En regardant le code ci-dessus, vous pouvez voir qu'une fonction anonyme est assignée à une variable. Oh, attendez ! Vous savez peut-être qu'une fonction est une instruction. Peut-elle aussi être une expression ?

Oui ! Une "fonction" et une "classe" sont à la fois des instructions et des expressions car elles peuvent effectuer des actions (faire ou ne pas faire des tâches) et s'exécuter pour donner une valeur.

Cela nous amène aux instructions – alors, qu'est-ce que c'est ?

## Qu'est-ce qu'une Instruction en Programmation ?

Une instruction est un groupe d'expressions et/ou d'instructions que vous concevez pour accomplir une tâche ou une action.

Les instructions sont à double tranchant – c'est-à-dire qu'elles font soit des tâches, soit ne les font pas. Toute instruction qui peut retourner une valeur est automatiquement qualifiée pour être utilisée comme une expression. C'est pourquoi une fonction ou une classe est une instruction et aussi une expression en JavaScript.

Si vous regardez l'exemple de la fonction sous la section sur les expressions, vous pouvez voir qu'elle est assignée et s'exécute pour donner une valeur passée à une variable. C'est pourquoi c'est une expression dans ce cas.

## Exemples d'Instructions en Programmation

### Instructions en ligne

```js
let amount = $2000;
```

L'ensemble du code ci-dessus est une instruction car il accomplit la tâche d'assigner `$2000` à `amount`. Il est sûr de dire qu'une ligne de code est une instruction car la plupart des compilateurs ou interpréteurs n'exécutent aucune expression autonome.

![Portraits d'homme heureux](https://images.unsplash.com/photo-1625314517201-dd442445cf42?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDF8fGV4Y2l0ZWR8ZW58MHx8fHwxNjcwNTEzMzMx&ixlib=rb-4.0.3&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@1nimidiffa_?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Nimi Diffa</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

### Instructions de bloc

Regardez l'instruction `if` ci-dessous :

```js
if( iLoveYou ) {
    let status = "you should know I mean it"; 

    console.log(status)
}
```

L'instruction `if` est une instruction car elle nous aide à vérifier si `I love you` ou non. Comme je l'ai dit avant, elle est à double tranchant : ce code détermine si "I love you" ou non, et c'est pourquoi c'est une instruction. De plus, elle ne retourne aucune valeur mais peut créer des effets secondaires.

Voici une instruction de `boucle` :

```js
for( ) {
   //code block
}

while ( counter < 5 ) {
   console.log(' less than 5' );
}
```

En bref, toute boucle est une instruction car elle peut soit faire les tâches pour lesquelles elle est conçue, soit ne pas les faire – elle boucle ou ne boucle pas. Mais une boucle ne peut pas s'exécuter pour donner une valeur à la fin. Elles ne peuvent avoir que des effets secondaires en JavaScript. Une fois qu'elles peuvent s'exécuter pour donner une valeur dans un langage de programmation, alors elles peuvent aussi être utilisées comme une expression.

Par exemple, vous pouvez utiliser forloop et if statement comme expressions en Python.

```python
# Définir une liste de nombres
numbers = [1, 2, 3, 4, 5]

# calculer la somme des nombres
total = sum([num for num in numbers])
```

Il existe également une expression "IF" en Python. Cela signifie que quelque chose qui est une instruction dans un langage peut être une expression (ou à la fois une instruction et une expression) dans un autre.

```python
a = 1
result = 'even' if a % 2 == 0 else 'odd'
print(result)
```

Regardez l'instruction de fonction ci-dessous :

```js
// nous définissons la fonction comme une instruction
function add(firstNumber, secondNumber) {
    return firstNumber * secondNumber;
}

// nous l'appelons comme une instruction
add(2, 3);
```

Nous déclarons la fonction `add(firstNumber, secondNumber)` et elle retourne une valeur. La fonction est appelée avec deux arguments comme dans `add(2, 3)` par déclaration et donc c'est une instruction. Si vous prêtez une attention particulière, vous réaliserez que l'appel de la fonction comme une instruction est inutile puisqu'elle n'a aucun effet secondaire.

Hé, stop ! Comment pouvons-nous la transformer en expression ? Oh oui, nous pouvons le faire comme ceci :

```js
   const five = add(2, 3)
```

Bien que la fonction soit maintenant une expression de la manière dont elle est appelée ci-dessus, l'ensemble du code est toujours une instruction.

Découvrez cette instruction de classe :

```js
let User = class Person {
  sayHi() {
    alert("Hi");
  }
};
```

Vous pouvez voir que nous déclarons la classe "Person" et **l'instancions et l'assignons** à "User" immédiatement. Donc, elle est utilisée comme une expression.

Maintenant, utilisons-la comme une instruction :

```js
// Nous écrivons la classe comme une instruction
class Person {
  sayHi() {
    alert("Hi");
  }
}

// nous l'instancions comme une instruction.
new Person().sayHi();

// nous l'instancions comme une expression
let User = Person();
```

[Une classe](https://www.techtarget.com/whatis/definition/class#:~:text=In%20object-oriented%20programming%20%2C%20a,ideas%20of%20object-oriented%20programming.) est similaire à une fonction dans le sens où elle peut être déclarée, assignée ou utilisée comme un opérande tout comme une classe. Donc, une classe est une instruction et/ou une expression.

## Les Principales Différences Entre une Expression et une Instruction en Programmation

Les expressions peuvent être assignées ou utilisées comme opérandes, tandis que les instructions ne peuvent être que déclarées.

Les instructions créent des effets secondaires pour être utiles, tandis que les expressions sont des valeurs ou s'exécutent pour donner des valeurs.

Les expressions sont uniques en signification, tandis que les instructions sont à double tranchant dans leur exécution. Par exemple, 1 a une certaine valeur tandis que `go()` peut être exécuté ou non.

Les instructions sont la structure entière, tandis que les expressions sont les blocs de construction. Par exemple, une ligne ou un bloc de code est une instruction.

## Pourquoi Vous Devriez Connaître la Différence

Tout d'abord, comprendre la différence entre les instructions et les expressions devrait rendre l'apprentissage de nouveaux langages de programmation moins surprenant. Si vous êtes habitué à JavaScript, vous pourriez être surpris par la capacité de Python à assigner une instruction if comme une variable, ce qui n'est pas possible en JavaScript.

Deuxièmement, cela facilite l'utilisation de paradigmes de programmation à travers différents langages de programmation.

Par exemple, une instruction "if" en JavaScript ne peut pas être utilisée comme une expression car elle ne peut pas s'exécuter pour donner une valeur – elle ne peut créer que des effets secondaires. Pourtant, vous pouvez utiliser l'opérateur ternaire si vous voulez éviter les effets secondaires de l'utilisation d'une instruction if en JavaScript.

Pour cette raison, vous pouvez comprendre pourquoi certains programmeurs évitent les instructions if en utilisant l'opérateur ternaire en JavaScript. C'est parce qu'ils veulent éviter les [effets secondaires](https://en.wikipedia.org/wiki/Side_effect_(computer_science)).

Cela vous fait également réaliser pourquoi vous devez toujours être prudent quant à la portée de vos variables chaque fois que vous utilisez une instruction. Cela est vrai car les instructions ont principalement des effets secondaires pour être utiles, et il est raisonnable de comprendre la portée de vos variables et opérations. Par exemple,

```js
let counter = 0;

function addFive() {
    counter += 5
    console.log(counter)
}

function addTwo() {
    counter += 2
    console.log(counter)
}

addFive(counter);// que va montrer ceci dans la console ?
addTwo(counter);// que va montrer ceci dans la console ?
```

Hé attendez ! Que serait enregistré dans la console si vous exécutiez le code ci-dessus ?

Dites-vous d'abord la réponse puis collez le code dans la console pour confirmer. Si vous avez tort, vous devez en apprendre davantage sur la portée et les effets secondaires. Mais si vous avez raison, essayez de rendre ces fonctions un peu meilleures pour éviter la confusion qu'elles peuvent générer.

Connaître la différence aide également à identifier facilement les syntaxes non composables et composables (fonctions, classes, modules, etc.) d'un langage de programmation. Cela rend le transfert de votre expérience d'un langage de programmation à un autre plus intéressant et direct.

## **Conclusion**

Maintenant que vous comprenez la différence entre les expressions et les instructions en programmation, et que vous savez pourquoi comprendre les différences est important, vous pouvez identifier des morceaux de code comme des expressions ou des instructions pendant que vous codez.

La prochaine fois, nous irons encore plus loin et aiderons à rendre l'apprentissage d'un second langage de programmation plus facile.

Allez et faites des choses maintenant ! À bientôt.

Je prévois de partager beaucoup de conseils et de tutoriels de programmation en 2023. Si vous avez du mal à construire des projets ou si vous voulez rester connecté avec mes écrits et vidéos, veuillez rejoindre ma liste à [YouTooCanCode](https://youtoocancode.aweb.page) ou vous abonner à ma chaîne YouTube à [You Too Can Code sur YouTube](https://www.youtube.com/c/youtoocancode).