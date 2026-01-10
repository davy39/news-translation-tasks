---
title: Les opérateurs JavaScript et la priorité des opérateurs – Guide pour débutants
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2023-03-20T21:15:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-operators-and-operator-precedence
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/JavaScript_Operator_precedence.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Les opérateurs JavaScript et la priorité des opérateurs – Guide pour débutants
seo_desc: "A few months ago, I attempted to solve a math problem in my head before\
  \ writing it in JavaScript. It was then that I received the most stunning revelation\
  \ of my career, which was both shocking and eye-opening. \nSo what did I attempt\
  \ to do? I made the..."
---

Il y a quelques mois, j'ai tenté de résoudre un problème de mathématiques de tête avant de l'écrire en JavaScript. C'est alors que j'ai reçu la révélation la plus stupéfiante de ma carrière, à la fois choquante et révélatrice.

Alors, qu'ai-je essayé de faire ? J'ai effectué les calculs mentaux suivants :

```js
2 + 3 * 4
```

Naturellement, ma réponse était `20`, j'ai donc procédé au codage. Mais lorsque la sortie sur la console a révélé que la réponse était `14`, cela a complètement modifié ma façon de percevoir JavaScript.

Mais comment effectuais-je des opérations arithmétiques avant JavaScript ? Eh bien, je saisissais simplement les nombres concernés dans une calculatrice et j'attendais mes résultats. Facile !

L'inexactitude de mon modèle mental sur la manière dont les opérations mathématiques sont effectuées en JavaScript a été mise en évidence par la réalisation mentale de ces calculs.

En tant que développeur JavaScript, vous avez peut-être déjà rencontré ce type d'« erreur » en faisant des mathématiques de tête par rapport à la façon dont JavaScript ou votre calculatrice le fait. Ce n'est pas de la magie, mais plutôt un concept simple connu sous le nom de **Précédence des opérateurs (Operator Precedence).**

Dans cet article, nous allons passer en revue ce que sont les opérateurs et comment les opérateurs en JavaScript sont analysés. Cela vous aidera non seulement avec JavaScript mais aussi avec d'autres langages de programmation si vous choisissez de les apprendre.

## Que sont les opérateurs ?

Les opérateurs sont des symboles spéciaux utilisés pour effectuer des opérations sur des opérandes, qui peuvent être des variables ou des valeurs. Par exemple, dans 13 / 3, le symbole de division « / » sert d'opérateur, tandis que « 13 » et « 3 » servent d'opérandes.

Une valeur ou une variable sur laquelle les opérateurs effectuent des opérations est connue sous le nom d'opérande. Voici un petit exercice pour vous tester. Examinez l'extrait de code ci-dessous et distinguez les opérateurs des opérandes :

```js
1. 2 + 5 * 3
2. (12 + 4) / 4
3. 20 ** 4 - 4

/* RÉPONSES
  Les opérateurs des opérations ci-dessus sont "+", "*" , "()", "**", "/" et "-"
  
 Les nombres sont les opérandes de l'opération
 
 */
```

## Types d'opérateurs en JavaScript

Tous les opérateurs en JavaScript n'effectuent pas d'opérations arithmétiques. Au contraire, les opérateurs varient dans leurs fonctions. Dans cette section, nous examinerons certains des différents types d'opérateurs et leur fonctionnement en JavaScript.

### Opérateurs arithmétiques

Un opérateur arithmétique est utilisé pour effectuer des opérations mathématiques de base. Il prend des valeurs numériques comme opérandes, qui peuvent être des variables ou des littéraux, et renvoie une valeur.

 Les opérateurs arithmétiques en JavaScript incluent :

* Addition (+)
* Soustraction (-)
* Multiplication (*)
* Exponentiation (**)
* Modulo (%)
* Décrémentation (--)
* Incrémentation (++)
* Division (/)

L'extrait de code suivant contient des exemples d'opérations utilisant les opérateurs arithmétiques :

```js
2 + 3   // RÉPONSE : 5. Ceci additionne les opérandes.

10 * 5 // RÉPONSE : 50. Ceci multiplie les opérandes.

10 % 3 // RÉPONSE : 1. Ceci renvoie le reste de la division des deux opérandes.

10++   // RÉPONSE : 11. Ceci augmente l'opérande de 1.

100-- // RÉPONSE : 99. Ceci diminue l'opérande de 1

10 ** 3 // RÉPONSE : 1000. Ceci multiplie les opérandes par la puissance de 3 ( 10 * 10 * 10)

10 - 3 // RÉPONSE : 7. Ceci soustrait les opérandes

10 / 5 // RÉPONSE : 2. Ceci divise 10 par 5
```

### Opérateurs de comparaison

Un opérateur de comparaison compare deux opérandes et renvoie une valeur booléenne (true ou false) comme résultat de la comparaison.

Les opérateurs de comparaison JavaScript sont les suivants :

* Égal (==)
* Non égal (!=)
* Égalité stricte (===)
* Inégalité stricte (!==)
* Supérieur à (>)
* Supérieur ou égal à (>=)
* Inférieur à (<)
* Inférieur ou égal à (<=)

L'extrait de code ci-dessous fournit quelques exemples du fonctionnement des opérateurs de comparaison :

```js
10 == 10  // RÉPONSE : True. Retourne vrai car 10 est égal à 10.

10 != 7 // RÉPONSE : True. Retourne une valeur Truthy car 10 n'est pas égal à 7.

10 == "10" // RÉPONSE : True. Retourne vrai car 10 est égal à 10.

10 === "10" // RÉPONSE : False. Retourne faux car 10, qui est de type number, n'est pas égal à "10" qui est de type string. Il les compare strictement par leurs valeurs et par leur type.

10 !== "10" // RÉPONSE : True. Retourne une valeur Truthy car 10, qui est de type number, n'est pas strictement égal à "10", qui est de type string.

10 > 30  // RÉPONSE : False. Retourne faux car 10 n'est pas supérieur à 30.

10 < 50 // RÉPONSE : True. Retourne une valeur truthy car 10 est inférieur à 50.

10 >= 70  // RÉPONSE : False. Retourne une valeur falsy car 10 n'est ni supérieur à 70, ni égal à 70.

10 <= 34 // RÉPONSE : True. C'est vrai car 10 est inférieur à 34 (même s'il n'est pas égal à 34 - c'est "inférieur ou égal à").

```

### Opérateurs d'affectation

Sur la base de la valeur de son opérande de droite, un opérateur d'affectation assigne une valeur à son opérande de gauche. L'application la plus fondamentale est l'utilisation de l'opérateur d'affectation (=) pour assigner une valeur à une variable. Il assigne essentiellement la valeur d'un opérande à un autre.

L'extrait de code ci-dessous fournit quelques exemples du fonctionnement de l'opérateur d'affectation :

```js
const author = "Franklin"

const platform = "Freecodecamp"

const age = 78

```

Voyons d'autres exemples d'opérateurs d'affectation :

* Affectation (=)
* Affectation après addition (+=)
* Affectation après soustraction (-=)
* Affectation après division (/=)
* Affectation après multiplication (*=)
* Affectation après exponentiation (**=)
* Affectation après modulo (%=)

Il est important de se rappeler que lors de l'utilisation d'opérateurs d'affectation autres que l'opérateur « = » — que j'aime appeler « affectations arithmétiques » — ils effectuent également une opération arithmétique avant d'assigner la valeur à l'opérande.

Pour en voir un exemple en action, regardez le code ci-dessous :

```js
let people = 20;

people += 20

console.log(people) // SORTIE : 40

let cars = 30

cars -= 20

console.log(cars) // SORTIE : 10
```

Nous pouvons voir dans l'extrait de code ci-dessus que les opérations arithmétiques ont d'abord été effectuées sur les opérandes avant d'être assignées, en utilisant les opérateurs arithmétiques appropriés.

Les « affectations arithmétiques » fonctionnent essentiellement comme suit : JavaScript exécute d'abord l'opération arithmétique, puis il assigne la valeur de l'opération à l'opérande (variable).

Après avoir vu comment cela fonctionne, apprenons-en davantage sur les différents opérateurs et comment les utiliser :

```js
let result = 400;  // L'opérateur d'affectation a été utilisé pour assigner la valeur 400 à la variable result.

result += 20; 
console.log(result)  // SORTIE : 420. La valeur de l'opérande de gauche a été ajoutée à 20 et la valeur assignée à l'opérande de gauche (400 + 20).

result -= 20; 
console.log(result)  // SORTIE : 400. La valeur de l'opérande de droite a été soustraite de l'opérande de gauche et la valeur assignée à l'opérande de gauche (420 - 20).

result *= 10 
console.log(result)  // SORTIE : 4000. Les valeurs des deux opérandes sont multipliées et la valeur de l'opération est assignée à l'opérande de gauche.

result /= 10; 
console.log(result)  // SORTIE : 400. L'opérande de gauche est divisé par 10 et la valeur de l'opération est assignée à l'opérande de gauche.

result %= 21;
console.log(result)  // SORTIE : 1. L'opérande de gauche est divisé par 21 et le reste de l'opération est assigné à l'opérande de gauche.

result **= 2; 
console.log(result)  // SORTIE : 1. L'opérande de gauche est élevé à la puissance 2 et la valeur est assignée à l'opérande de gauche.
```

Passons maintenant au type d'opérateur suivant maintenant que nous avons vu comment les opérateurs d'affectation fonctionnent.

### Opérateurs logiques

Lorsqu'il est utilisé avec des valeurs booléennes, un opérateur logique produit une valeur booléenne (true ou false), sinon il renvoie la valeur de l'un des opérandes. Les opérateurs logiques sont utilisés pour vérifier et déterminer la logique entre deux opérandes ou plus.

Bien qu'ils puissent être difficiles à comprendre, passons en revue les opérateurs et voyons comment ils fonctionnent :

* OU (| |)
* ET (&&)
* NON (!)

Des exemples d'utilisation des opérateurs sont fournis ci-dessous :

```js
// UTILISATION DE L'OPÉRATEUR ET (&&)

let canDrive = true;
let hasLicense = false;

const readyToDrive = canDrive && hasLicense;

console.log(readyToDrive) // SORTIE : false
```

À l'aide de l'extrait de code ci-dessus, nous avons pu construire une logique qui détermine si une personne est qualifiée pour conduire si elle possède un permis de conduire et a de l'expérience en conduite. Les deux conditions doivent être remplies avant que la personne puisse réussir le test d'éligibilité.

L'opérateur ET (&&) détermine cela car si l'une des exigences est fausse, le résultat de l'opération sera également faux. L'opération ne peut pas produire une valeur truthy à moins que les deux valeurs ne soient vraies :

```js
// UTILISATION DE L'OPÉRATEUR ET (&&)

let canDrive = true;
let hasLicense = true;

const readyToDrive = canDrive && hasLicense;

console.log(readyToDrive) // SORTIE : true
```

Ensuite, avec le même scénario que précédemment, examinons comment nous pouvons utiliser l'opérateur OU (||) :

```js
// UTILISATION DE L'OPÉRATEUR OU (||)

let canDrive = true;
let hasLicense = false;

const readyToDrive = canDrive || hasLicense;

console.log(readyToDrive) // SORTIE : true
```

À titre d'illustration, les règlements d'éligibilité ont été modifiés pour permettre à ceux qui n'ont pas de permis de conduire de conduire tant qu'ils en sont capables.

Nous avons créé une logique qui teste cela à l'aide de l'opérateur OU (||). Si l'un des opérandes est une valeur vraie, l'opération renvoie vrai, indiquant que dans ce cas, la personne a réussi le test d'éligibilité et est autorisée à conduire.

Vous pourriez trouver difficile de déterminer si une opération renvoie vrai ou faux lors de l'utilisation d'opérateurs logiques, j'ai donc fait un petit pense-bête que vous pouvez mémoriser et consulter dès que vous êtes bloqué :

```js
// Pense-bête de l'opérateur ET (&&).

true && false = false;
false && false = false;
true && true = true
```

```js
// Pense-bête de l'opérateur OU (||).

true || false = true;
false || false = false;
true || true = true
```

Si ce qui précède est trop long à mémoriser pour vous, voici un autre pense-bête aussi simple :

```js
false && n'importe quoi = false;
true || n'importe quoi = true;
```

Espérons que ces petits conseils vous serviront de référence lorsque vous utiliserez les opérateurs logiques en JavaScript.

Consultez l'échantillon de code ci-dessous pour un exemple d'utilisation de l'opérateur NON (!), qui est le dernier opérateur logique de la liste :

```js
const author = "Franklin"

if (author != "Franklin") {
    console.log("Ceci n'est pas l'auteur")
}
```

Nous avons créé un programme de base à partir de l'extrait de code ci-dessus qui vérifie l'auteur d'un article ou d'un livre et affiche un message si l'auteur ne correspond pas à l'auteur original du livre. L'opérateur NON (!) est généralement combiné avec d'autres opérateurs pour créer des opérations utiles.

Vous pouvez également l'utiliser pour déterminer si une valeur est vraie ou fausse en inversant une valeur booléenne. Voyons comment cela fonctionne ci-dessous, en utilisant le scénario du test d'éligibilité à la conduite :

```js
// UTILISATION DE L'OPÉRATEUR NON (!)

let canDrive = true;
let hasLicense = false;

if (!canDrive && !hasLicense) {
     console.log("Désolé, vous n'êtes pas éligible pour conduire")
}

// SORTIE : "Désolé, vous n'êtes pas éligible pour conduire"
```

Décortiquons la logique. Tout d'abord, nous avons une personne qui sait conduire mais qui n'a pas de permis de conduire, ce qui est requis par la loi pour qu'une personne soit éligible à la conduite.

Nous avons créé une logique pour garantir que si une personne manque de l'une des deux qualités, elle n'est pas autorisée à conduire. La logique précédente peut être traduite comme suit :

« Si une personne NE PEUT PAS conduire et N'A PAS de permis de conduire, elle n'est pas autorisée à conduire ».

Parce que la variable déclarée `canDrive` est `true`, alors `!canDrive` s'inverse en `false` et `hasLicense` étant `false`, il s'inverse en `true`.

Alors comment cela finit-il par être faux ? Vous vous souvenez de notre pense-bête de tout à l'heure ? Nous pouvons l'utiliser pour vérifier le résultat de l'opération.

`false` && `true` sera `false`.

Si vous avez lu l'article jusqu'ici, félicitations pour vos nouvelles connaissances sur les opérateurs JavaScript. Si vous souhaitez explorer davantage et voir plus de types d'opérateurs, voici un lien vers une [ressource MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators). Les opérateurs sont cruciaux dans nos activités quotidiennes avec JavaScript, il est donc important de les connaître.

Nous pouvons maintenant passer à la section suivante de cet article où vous apprendrez comment utiliser plusieurs opérateurs dans une opération et comment JavaScript calcule cette opération.

## Précédence des opérateurs en JavaScript

Le concept de précédence des opérateurs décrit comment les opérateurs sont comparés les uns aux autres tout au long d'une opération. Les opérateurs qui ont une précédence plus élevée reçoivent une priorité plus élevée que les opérateurs ayant une précédence plus faible.

En dehors de l'écriture de logique de base en JavaScript tous les jours, nous passons environ la moitié de notre temps à écrire des opérations mathématiques complexes, des opérations logiques, et occasionnellement nous traduisons même certaines formules de physique et de mathématiques en code JavaScript. Cela entraîne des complications importantes car aucune des formules susmentionnées n'est simple – elles contiennent toutes deux de multiples opérateurs et opérandes.

Mais comment JavaScript analyse-t-il cette condition lorsqu'il la rencontre ? Voyons un exemple ci-dessous :

```js
/* ÉTANT DONNÉ UN ENSEMBLE DE SCORES OBTENUS PAR UNE ÉQUIPE,
CALCULER LE SCORE MOYEN DE L'ÉQUIPE

LA FORMULE DE LA MOYENNE EST : SOMME DES VALEURS DIVISÉE PAR LE NOMBRE TOTAL DE VALEURS

firstScore = 40;
secondScore = 38;
thirdScore = 24;
fourthScore = 32; 
*/

const averageScore = 40 + 38 + 24 + 32 / 4;

console.log(averageScore)    // SORTIE : 110
```

Si vous utilisez n'importe quel [outil de calcul de moyenne en ligne](https://www.omnicalculator.com/math/average), le résultat sera `33.5`, ce qui est la bonne réponse. Le résultat de l'opération susmentionnée dans notre code est `110`, ce qui est tout à fait « faux » car la moyenne de ces valeurs ne peut pas être `110`. Pourtant, pourquoi ? Ici, la précédence des opérateurs est en jeu.

Tout comme les hiérarchies fonctionnent dans le monde réel, certains opérateurs au pays de JavaScript sont plus importants que d'autres. JavaScript reconnaît et utilise d'abord les opérateurs les « plus » importants avant les « moins » essentiels dans une opération.

### Règles de la précédence des opérateurs

JavaScript ne choisit pas au hasard l'opérateur auquel il accorde la priorité dans une opération en fonction de l'ordre dans lequel ils apparaissent ou pour toute autre raison. Faire cela aboutirait à un univers JavaScript en proie à des incohérences mathématiques.

JavaScript a une règle qu'il respecte scrupuleusement afin de déterminer la précédence. Plutôt que de parcourir un long tableau ou graphique de toutes ces règles, il existe une méthode plus rapide et plus facile à retenir : **BODMAS**

BODMAS se traduit par :

* Bracket (Parenthèse) "()"
* Of (Puissance/Exposant) (**)
* Division (/)
* Multiplication (*)
* Addition (+)
* Subtraction (Soustraction) (-)

Chaque opérande est listé ci-dessus dans l'ordre précis où sa précédence est déterminée. Facile ? J'adore cette technique et je l'emploie régulièrement pour éviter les erreurs que la précédence des opérateurs peut introduire.

Examinons comment JavaScript a géré l'opération du score moyen. Comme nous pouvons le voir d'après la petite formule ci-dessus (**BODMAS**), l'opérateur Division (/) a une précédence plus élevée que l'opérateur Addition (+), donc JavaScript effectue d'abord les opérations de division en divisant `32` par `4`, ce qui donne `8`. Ensuite, il passe à l'opérateur suivant conformément à la précédence, qui est l'opérateur Addition (+), qui additionne toutes les valeurs et renvoie un résultat de 110.

Maintenant, regardons à nouveau l'exemple du début de ce tutoriel :

```js
let attendees = 2 + 3 * 4;

console.log(attendees) // SORTIE : 14.
```

Vous avez peut-être effectué mentalement le calcul précédent et obtenu `20` (c'est ce que j'ai obtenu), mais JavaScript pense autrement, ce qui est en fait correct.

Selon la règle de précédence **BODMAS**, la multiplication vient avant l'addition. JavaScript a donc multiplié 3 par 4 (ce qui donne 12) avant d'ajouter le résultat à l'autre opérande pour obtenir le nombre 14.

Parce que nous devions diviser le nombre total de scores par la somme des scores, nous pouvons maintenant ajuster notre opération de score moyen avec cette connaissance :

```js
/* ÉTANT DONNÉ UN ENSEMBLE DE SCORES OBTENUS PAR UNE ÉQUIPE,
CALCULER LE SCORE MOYEN DE L'ÉQUIPE

LA FORMULE DE LA MOYENNE EST : SOMME DES VALEURS DIVISÉE PAR LE NOMBRE TOTAL DE VALEURS

 firstScore = 40;
secondScore = 38;
thirdScore = 24;
fourthScore = 32; 
*/

const averageScore = (40 + 38 + 24 + 32) / 4;

console.log(averageScore) // SORTIE : 33.5
```

Hourra ! Enfin, nous avons la bonne réponse ! Pouvez-vous dire comment JavaScript a interprété cela ?

La hiérarchie de précédence place les parenthèses en premier, donc JavaScript exécute les opérations contenues dans les parenthèses avant de passer à l'opération suivante. En conséquence, il a ajouté 40, 38, 24 et 32 pour produire 144, qui a ensuite été divisé par le nombre de scores (4), nous donnant le résultat final de 33,5.

Voici quelques exercices que vous pouvez essayer pour mettre vos nouvelles connaissances sur la précédence des opérateurs à l'épreuve :

```js
1. 2 + 4 - 6 / 2
2. 4 + 4 * 8 / 3
3. 8 ** 2 + 4


/* 
RÉPONSES : 
1. 3
2. 14.666... (Note : L'original indiquait 20, mais 4 + (32/3) ≈ 14.66)
3. 68
*/
```

Il manque certains opérateurs dans la formule **BODMAS** ci-dessus. La formule n'est pas « absolue » car elle ne couvre qu'une infime partie des opérateurs, à savoir les opérateurs arithmétiques que nous utilisons dans nos opérations de codage quotidiennes. Cette [ressource MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence#table) montre un tableau de hiérarchie de précédence plus complet.

## Conclusion

Nous sommes à la fin de ce tutoriel, dans lequel nous avons appris les opérateurs JavaScript et comment JavaScript les analyse lors de l'exécution d'une opération à l'aide d'une technique appelée **Précédence des opérateurs**. En utilisant cette [ressource MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence), vous pouvez en apprendre davantage sur la précédence des opérateurs.

Comme il peut être assez fastidieux de se souvenir de toute la **Précédence des opérateurs**, vous pouvez utiliser l'acronyme **BODMAS.**

J'espère vraiment que vous avez beaucoup appris de cet article.

Suivez-moi sur [Twitter](https://twitter.com/developeraspire) pour plus de conseils sur JavaScript et CSS.

Je vous remercie de m'avoir lu. À la prochaine !