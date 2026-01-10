---
title: Perfectionnez vos compétences en codage en construisant un programme de différentes
  manières
subtitle: ''
author: Niladri S. Jyoti
co_authors: []
series: null
date: '2024-03-04T15:39:55.000Z'
originalURL: https://freecodecamp.org/news/practice-coding-skills-by-building-a-program-different-ways
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Build-A-Leap-Year-Program-in-Many-Different-Ways-1.jpg
tags:
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
seo_title: Perfectionnez vos compétences en codage en construisant un programme de
  différentes manières
seo_desc: "While we have 365 days in other years, this year (2024) is special because\
  \ it has one ‘extra’ day. \nSo in the spirit of Leap Day, let's practice some coding\
  \ to understand various aspects of programming. We'll focus on the same program\
  \ but from differ..."
---

Alors que nous avons 365 jours dans les autres années, cette année (2024) est spéciale car elle a un jour "supplémentaire".

Alors, dans l'esprit du Jour Bisexte, pratiquons un peu de codage pour comprendre divers aspects de la programmation. Nous nous concentrerons sur le même programme mais sous différents angles.

Notre programme exemple explorera différentes façons de coder un programme qui détermine si une année donnée est une année bissextile. Les autres jours, nous codons. Mais aujourd'hui, décodons ce que nous faisons et tirons quelques connaissances supplémentaires de ce processus.

<h3>Table des Matières</h3>
<ul>
    <li><a href="#heading-installation">Exigences du Programme & Prérequis</a></li>
    <li><a href="#logical-approaches">Approches Logiques pour Résoudre le Problème</a></li>
    <ul style="margin-left: 1rem;">
        <li><a href="#naive-approach">Mon Approche Naïve</a></li>
        <li><a href="#single-return">Réaffectations et une Unique Instruction de Retour</a></li>
        <li><a href="#switch-case">Passage de If-Else à Switch-Case</a></li>
        <li><a href="#logical-deduction">Deduction Logique & Sous-ensembles pour une Meilleure Structure</a></li>
        <li><a href="#combine-conditions">Opérateurs Logiques Combinant Toutes les Conditions Vraies</a></li>
        <li><a href="#ternary-operator">Application de Nitro avec l'Opérateur Ternaire</a></li>
        <li><a href="#arrow-function">En Faire une Fonction Fléchée d'une Seule Ligne</a></li>
    </ul>
    <li><a href="#programming-paradigm">Changement de Paradigme : Programmation Déclarative</a></li>
    <ul style="margin-left: 1rem;">
        <li><a href="#side-effects">Fonctions avec Effets de Bord</a></li>
        <li><a href="#functional-programming">Plus sur la Programmation Fonctionnelle</a></li>
        <li><a href="#short-circuiting">Détour : Court-circuit !</a></li>
        <li><a href="#declarative-programming">Encapsulation et Programmation Déclarative</a></li>
    </ul>
    <li><a href="#code-quality">Aller Au-delà avec la Qualité du Code</a></li>
    <ul style="margin-left: 1rem;">
        <li><a href="#validations">Validations : Au-delà des Spécifications de Base</a></li>
        <li><a href="#unit-testing">Tester de l'Extérieur</a></li>
    </ul>
    <li><a href="#end-note">Note Finale</a></li>
</ul>

<h2 id="heading-installation">Exigences du Programme & Prérequis</h2>

Tout d'abord, discutons des exigences et établissons les spécifications. Le programme doit pouvoir recevoir une année (attend un nombre, un entier pour être précis) comme argument et retourne soit vrai soit faux (un booléen) selon qu'il s'agit d'une année bissextile ou non.

À travers les exemples, nous nous concentrerons sur la logique du programme (sémantique) plutôt que sur le langage (syntaxe).

Au fil des ans, j'ai utilisé JavaScript le plus fréquemment, donc nous utiliserons ce langage pour le projet. Si vous utilisez un autre langage, pas de souci car de nombreux concepts sont communs entre les langages de programmation. Par exemple, dans cet article, nous utiliserons la fonction fléchée qui est similaire à la fonction lambda utilisée dans certains autres langages de programmation, comme Python.

Ainsi, comme prérequis, vous devriez avoir une connaissance de base de la programmation et être à l'aise avec les concepts de fonctions (différentes façons de définir et d'appeler des fonctions, valeurs de retour, etc.) et de logique conditionnelle (if-else, switch-case, etc.). Cela serait suffisant pour suivre, pour la plupart, si vous voulez lire et essayer le code par vous-même.

Juste dans la dernière partie, nous faisons également des tests unitaires de notre code. Si vous n'êtes pas familier avec les tests unitaires, voici un bon rappel sur [comment écrire des tests unitaires en JavaScript avec Jest](https://dev.to/dstrekelj/how-to-write-unit-tests-in-javascript-with-jest-2e83).

<h2 id="logical-approaches">Approches Logiques pour Résoudre le Problème</h2>

<h3 id="naive-approach">Mon Approche Naïve</h3>

Cela est basé sur le style pédagogique de détermination d'une année bissextile que j'ai appris enfant qui savait diviser des nombres. Si une année (le nombre qui la représente) est divisible par 4, c'est généralement une année bissextile. Mais pas toujours. Lorsque cette année se termine par deux zéros (ce qui signifie que le nombre est divisible par 100), elle doit également être divisible par 400 pour être une année bissextile.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/FlowChart-LeapYear.jpg)
_Comment déterminer si une année est une année bissextile - comme décrit ci-dessus_

En tant que programmeur débutant, mes pensées coulaient comme vous pouvez le voir dans l'organigramme ci-dessus. En conséquence, j'ai converti cette logique dans mon programme comme suit :

```js
function isLeapYear(year) {
  if (year % 4 == 0) {
      if (year % 100 == 0) {
          if (year % 400 == 0) {
              return true;
          } else {
              return false;
          }
      } else {
          return true;
      }
  } else {
   return false
  }
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Cela rend le programme facilement compréhensible. Mais avec le temps, alors que j'ai progressé dans mon parcours de programmation, ce type de code semble laid à cause de tant de vérifications conditionnelles imbriquées. Ce n'est pas mauvais, mais à cause des niveaux imbriqués, mon cerveau doit travailler plus dur pour obtenir la logique à partir de l'instantané de code rapidement.

<h3 id="single-return">Réaffectations et une Unique Instruction de Retour</h3>

Pour éviter les boucles imbriquées, de nombreux programmeurs suivent la stratégie des conditions if consécutives, évitant les conditions else (comme le montre Kyle Cook de Web Dev Simplified dans cette [vidéo avec des exemples](https://www.youtube.com/watch?v=EumXak7TyQ0)). Cela améliore définitivement la lisibilité.

De plus, cela nous permet d'utiliser une seule instruction de retour à la fin tout en réaffectant la valeur retournable. Ne discutons pas trop plus lorsque vous pouvez mieux voir le code lui-même :

```js
function isLeapYear(year) {
  let isLeap = false;
  if (year % 4 == 0) {
      isLeap = true;
  }
  if (year % 100 == 0) {
      isLeap = false;
  }
  if (year % 400 == 0) {
      isLeap = true;
  }
  return isLeap;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Le code ci-dessus semble plus court et plus rapide à interpréter. Mais cela affecte l'efficacité du code, car maintenant vous devez passer par toutes les conditions if dans tous les cas.

En revanche, dans notre approche naïve précédente, grâce à la structure if-else, si une année n'est pas divisible par 4 (comme l'année 2023), elle serait simplement vérifiée par rapport à une condition if. Il est vrai, bien sûr, que pour de petits programmes comme celui-ci, vous n'avez pas à vous soucier excessivement de l'efficacité.

Le piège dans cette approche, cependant, est que vous devez être prudent pour appliquer toutes les conditions if les unes après les autres - utiliser 'else if' créerait des problèmes, car cela sauterait certaines vérifications de conditions if si le test de la condition if précédente a réussi.

Un autre fait important est que l'ordre compte. Puisque vous avez commencé avec les cas plus génériques des années n'étant pas une année bissextile (c'est-à-dire, let isLeap = false;), vous devez aller des cas relativement génériques aux cas relativement plus spécifiques.

Donc, si, parmi vos trois vérifications de conditions, la vérification de la divisibilité par 4 arrive à la fin, cela rendrait 'isLeap' vrai même pour les années qui sont divisibles par 100 mais pas divisibles par 400 (comme les années 1700, 1800, 1900, et ainsi de suite).

La même erreur logique se produirait si vous interchangez l'ordre des vérifications de divisibilité impliquant 100 et 400.

Un dernier point que je dois mentionner est que certains programmeurs débutants peuvent penser que vous ne pouvez pas utiliser plusieurs instructions de retour et que vous devez retourner une seule fois dans un programme (et que vous pouvez faire des réaffectations jusqu'à ce point). Mais les programmeurs expérimentés ne peuvent appeler cette notion qu'un mythe de débutant !

<h3 id="switch-case">Passage de If-Else à Switch-Case</h3>

Alors que la structure if-else est utilisée pour choisir entre deux options, vous pouvez également utiliser switch-case pour choisir une parmi plusieurs options. Vous pouvez la comparer à des blocs if-else imbriqués (comme dans la première approche) ou à une série de blocs if (comme dans la deuxième approche).

L'avantage de la structure switch-case est qu'elle est plus efficace car elle peut trouver le critère de succès correspondant en une seule fois.

Notez qu'il y a une chose étrange avec switch-case. Lorsque vous utilisez switch-case, une fois qu'un cas est trouvé, tous les cas suivants seront également exécutés à moins que vous n'utilisiez des instructions break. Donc, le programme suivant ne sera pas correct même s'il ressemble beaucoup à notre version précédente du code.

**Code incorrect : pour montrer les problèmes avec les instructions break manquantes **

```js example-bad
function isLeapYear(year) {
  let isLeap = false;
  switch (true) {
    case year % 4 == 0:
      isLeap = true;
    case year % 100 == 0:
      isLeap = false;
    case year % 400 == 0:
      isLeap = true;
  }
  return isLeap;
}
```

Si nous devons utiliser une structure switch-case, nous devons utiliser des instructions break. Nous devons également aller des cas spécifiques d'abord aux cas génériques ensuite. Bien que toutes les logiques if-else ne puissent pas être converties en une logique switch-case, nous pouvons convertir avec succès la fonction précédente comme suit :

```js
function isLeapYear(year) {
  let isLeap = false;
  switch (true) {
    case year % 400 == 0:
      isLeap = true;
      break;
    case year % 100 == 0:
      isLeap = false;
      break;
    case year % 4 == 0:
      isLeap = true;
      break;
  }
  return isLeap;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Remarquez que dans ce qui précède, nous n'avons pas de cas 'default'. Et cela est dû au fait que nous avons initialisé la variable isLeap avec false. Si nous avions simplement déclaré la variable sans initialisation avec une valeur, nous aurions pu écrire un cas par défaut qui aurait assigné la valeur false à isLeap.

De plus, la version ci-dessus du code switch-case est légèrement plus longue car nous voulions utiliser une instruction de retour à la fin et avons utilisé des assignations jusqu'à ce point. Mais si nous le refactorisons, un code plus court et plus organisé serait celui-ci :

```js
function isLeapYear(year) {
  switch (true) {
    case (year % 400 === 0):
      return true;
    case (year % 100 === 0):
      return false;
    case (year % 4 === 0):
      return true;
    default:
      return false;
  }
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Remarquez que puisque l'exécution d'une instruction de retour dans une fonction met automatiquement fin à l'appel de la fonction, le programme ne lit pas les lignes qui suivent cette instruction. Donc, dans cet exemple, nous n'avons pas à utiliser les instructions break nécessairement.

<h3 id="logical-deduction">Deduction Logique & Sous-ensembles pour une Meilleure Structure</h3>

Revenant de switch-case à la logique if-else, faisons une déduction logique. Dans notre logique if-else précédente, nous sommes passés des cas génériques aux cas spécifiques. Que se passe-t-il si nous faisons l'inverse ? Nous considérons qu'une année donnée sera une année bissextile à moins qu'elle ne soit niée.

Donc, nous commençons par les cas plus restreints des années centenaires - pour elles, la règle est simple : pour être niées, elles doivent être divisibles par 100 mais pas par 400 (comme les années 1700, 1800, 1900).

Dans ce processus, puisque nous avons déjà accepté des années comme 2000 (ou des années divisibles par 400) comme étant une année bissextile, nous ne les testerons pas pour la divisibilité par 4 (car un nombre divisible par 400 serait de toute façon divisible par 4 également).

À l'étape suivante, alors que nous considérons uniquement les années non centenaires, nous nierions simplement les cas où l'année n'est pas divisible par 4 (années comme 2023, 1996, et ainsi de suite).

```js
function isLeapYear(year) {
  let isLeap = true;
  if (year % 100 == 0 && year % 400 != 0) {
      isLeap = false;
  } else if (year % 4 != 0) {
      isLeap = false;
  }
  return isLeap;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Ici, vous voyez, nous considérons d'abord les années centenaires puis les années non centenaires - car elles sont mutuellement exclusives - et c'est pourquoi nous utilisons 'else-if' au lieu de if dans la deuxième vérification conditionnelle. Et dans ce processus, nous gagnons en efficacité par rapport aux blocs if consécutifs.

Comme cette approche consiste à diviser les routes possibles d'être une année bissextile (ou pour cela, de ne pas être une année bissextile) en sous-ensembles d'années, selon la manière dont nous divisons les années possibles en sous-ensembles, nous pouvons construire le programme alternativement comme montré ci-dessous :

```js
function isLeapYear(year) {
  let isLeap = false;
  if (year % 400 == 0) {
      isLeap = true;
  } else if (year % 100 != 0 && year % 4 == 0) {
      isLeap = true;
  }
  return isLeap;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Donc, en bref, notre déduction de la règle de l'année bissextile est que les années divisibles par 400 (comme 1600, 2000) sont des années bissextiles, et parmi toutes les autres années, elles doivent être divisibles par 4 mais pas divisibles par 100 pour être une année bissextile.

En adoptant cette approche, nous avons combiné des conditions et c'est pourquoi nous avons impliqué des opérateurs logiques (&&, l'opérateur ET logique). Cela nous a aidé à réduire la longueur de la fonction. Au lieu de trois blocs conditionnels, nous utilisons actuellement deux blocs - un bloc if et ensuite un else (où nous vérifions davantage la condition, et ainsi nous l'appelons else-if plutôt que simplement else).

Mais maintenant que nous utilisons presque une seule structure 'if-else' et que nous approfondissons également les opérateurs logiques, libérons plus de puissance des opérateurs logiques dans l'approche suivante.

<h3 id="combine-conditions">Opérateurs Logiques Combinant Toutes les Conditions Vraies</h3>

Cette fois, réorganisons simplement la logique de l'approche précédente (deux sous-ensembles) pour regrouper toutes les conditions positives ensemble et ensuite accepter une année comme une année bissextile. Si cela n'est pas satisfait, alors appelez-la une année non bissextile.

```js
function isLeapYear(year) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        return true;
    } else {
        return false;
    }
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Cela semble bien car cela augmente la lisibilité en organisant les conditions positives ensemble. Le seul coût que nous encourons ici est que la condition dans le bloc if est plus longue.

Mais avec les opérateurs logiques, cela semble visuellement plus court et pas complexe (au moins pour les programmeurs habitués à combiner les opérateurs logiques comme cela).

En disséquant davantage, puisque dans l'approche précédente nous avons dit que nous pouvions diviser les sous-ensembles de deux manières différentes, nous pouvons avoir deux versions correspondantes pour cette approche également. La deuxième est la suivante :

```js
function isLeapYear(year) {
  if ((year % 100 == 0 && year % 400 != 0) || year % 4 != 0) {
      return false;
  } else {
      return true;
  }
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

<h3 id="ternary-operator">Application de Nitro avec l'Opérateur Ternaire</h3>

Alors que vous progressez dans votre parcours d'apprentissage de la programmation, à un moment donné, vous devez avoir été ravi de découvrir la possibilité d'écrire des programmes ultra-courts.

Alors que les opérateurs logiques nous aident à faire cela, pour activer le mode 'Nitro', nous devons utiliser un Opérateur Ternaire - qui transforme essentiellement nos blocs if-else en une seule ligne.

```js
function isLeapYear(year) {
  return ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) ? true : false;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

À présent, en tant que programmeur pro, vous devez plaindre votre moi débutant. Vous pensez à ces moments où vous déclariez et initialisiez une variable avec une valeur par défaut d'abord, puis la réaffectiez avec la valeur que vous vouliez retourner, et enfin retourniez la valeur détenue par cette variable.

Cela fait longtemps que vous avez abandonné cette pratique, et vous retournez maintenant ce que vous devez retourner, et ne consommez pas d'espace mémoire inutile pour des variables inutiles.

<h3 id="arrow-function">En Faire une Fonction Fléchée d'une Seule Ligne</h3>

Maintenant que vous avez été boosté avec Nitro, votre technique de programmation avance comme une flèche, en mission pour arracher les vestiges de ES5 et voler hardiment dans le monde post-ES6. Vous accueillez donc les fonctions fléchées à bras ouverts.

```js
const isLeapYear = year => (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0));

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

Auparavant, vous avez sauté les variables, et vous avez sauté les blocs 'if-else'. Et maintenant, vous pouvez même sauter l'instruction de retour grâce à la fonction fléchée ayant une seule instruction dans son corps. Vous sautez également les parenthèses autour de votre argument car il s'agit d'un seul argument.

Alors que vous chantez la saga du code plus court, un point doit être fait que le code plus court n'est pas nécessairement le meilleur code. Tout dépend de vos utilisateurs du code (personnes qui pourraient le lire et éventuellement collaborer/l'améliorer).

Si vous travaillez avec des programmeurs expérimentés, ce niveau de concision est acceptable. Assurez-vous simplement de ne pas dépasser la largeur de ligne au-delà d'un certain nombre d'espaces (80 caractères recommandés) afin de ne pas ennuyer vos collègues avec le besoin de gérer des barres de défilement horizontales.

Mais si vous travaillez avec des membres d'équipe de niveaux d'expérience variés, ou si vous êtes un enseignant travaillant avec des apprenants, alors vous devez être conscient de la lisibilité de votre code pour tout le monde.

<h2 id="programming-paradigm">Changement de Paradigme : Programmation Déclarative</h2>

En tout cas, nous avons discuté de la logique de détermination de l'année bissextile dans les exemples ci-dessus. Mais examinons davantage pour trouver plus de nuances de la programmation. Et dans ce processus, passons de la programmation impérative (comme nous l'avons utilisée jusqu'à présent) à la programmation déclarative (qui est l'objectif final dans cette section).

<h3 id="side-effects">Fonctions avec Effets de Bord</h3>

Les fonctions sont dites avoir des effets de bord lorsqu'elles modifient des variables non locales. De plus, une fonction qui imprime (journalise) dans la console est également considérée comme une fonction avec certains effets de bord. Cela est dû au fait que si une fonction n'a pas d'effet de bord, un appel à celle-ci peut être remplacé par sa valeur de retour.

La programmation fonctionnelle est un paradigme qui dicte que notre programme doit être comme une fonction pure sans effets de bord. Une fonction pure signifie une fonction qui retourne toujours la même sortie donnée la même entrée. Donc, dans son corps, elle dépend uniquement du paramètre d'entrée donné de l'extérieur et d'aucune autre variable globale. De plus, elle doit simplement retourner la valeur de sortie sans effets de bord ou essayer de modifier quoi que ce soit en dehors de sa portée.

Mais considérons la variation suivante du programme qui ne retourne pas spécifiquement de valeur représentant le résultat. Au lieu de cela, elle journalise le résultat sous forme de déclaration (chaîne) dans la console. Il s'agit d'un exemple d'effet de bord.

```js
function isLeapYear(year) {
  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
      console.log("année bissextile.");
  } else {
      console.log("pas une année bissextile.");
  }
}

// Exemple d'utilisation :
let someValue = isLeapYear(2024); // Sortie : année bissextile.
console.log(someValue); // Sortie : undefined
```

Évidemment, cela ne suit pas la spécification, car elle doit retourner une valeur de type booléen. Une fonction peut, bien sûr, faire les deux - imprimer et retourner, comme une forme alternative de la fonction ci-dessus.

```js
function isLeapYear(year) {
  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
      console.log("année bissextile.");
      return true;
  } else {
      console.log("pas une année bissextile.");
      return false;
  }
}

// Exemple d'utilisation :
let someValue = isLeapYear(2024); // Sortie : année bissextile.
console.log(someValue); // Sortie : true
```

Mais le simple fait qu'elle fasse deux choses - retourner une valeur et imprimer dans la console - est le problème. Une fonction doit être faite pour faire une seule chose pour une réutilisabilité correcte. La fonction 'isLeapYear' doit simplement déterminer si une année est une année bissextile. Si nous devons imprimer quelque chose à ce sujet, laissons cette responsabilité des effets de bord à d'autres fonctions de journalisation.

```js
// fonction pure

function isLeapYear(year) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        return true;
    } else {
        return false;
    }
}

// fonctions avec effet de bord

function simpleLeapYearLogger(isLeap) {
    if (isLeap) {
        console.log("Oui, une année bissextile !");
    } else {
        console.log("Désolé, pas une année bissextile.");
    }
}

function advancedLeapYearLogger(year, isLeap) {
    if (isLeap) {
        console.log(`L'année ${year} est une année bissextile !`);
    } else {
        console.log(`L'année ${year} n'est pas une année bissextile !`);
    }
}

// Exemple d'utilisation :
let currYear = 2024;
let check2024 = isLeapYear(currYear); // Pas de sortie/effet de bord, juste une valeur retournée.
simpleLeapYearLogger(check2024); // Sortie : Oui, une année bissextile !
advancedLeapYearLogger(currYear, check2024); // Sortie : L'année 2024 est une année bissextile !
```

Comme vous pouvez le voir ci-dessus, la fonction 'isLeapYear' est plus réutilisable - avec deux cas d'utilisation différents dans deux fonctions de journalisation séparées. De plus, s'il y avait eu une erreur dans la logique de la fonction 'isLeapYear', il aurait été plus facile de la corriger sans toucher au code des fonctions de journalisation.

De même, si vous devez afficher la chaîne journalisée dans la console différemment, vous pourriez modifier la fonction de journalisation respective sans toucher à la fonction de logique de l'année bissextile. Ainsi, une fonction faisant simplement ce qu'elle est censée faire augmente la réutilisabilité et la maintenabilité de cette fonction.

<h3 id="functional-programming">Plus sur la Programmation Fonctionnelle</h3>

Dans la section ci-dessus, vous avez déjà pénétré dans l'espace de la programmation fonctionnelle. Et maintenant, il est temps de creuser plus profondément.

Si je recherche le terme 'Programmation Fonctionnelle' dans Wikipédia, la première ligne indique

> "la programmation fonctionnelle est un paradigme de programmation où les programmes sont construits en appliquant et [composant](https://en.wikipedia.org/wiki/Function_composition_%28computer_science%29) [fonctions](https://en.wikipedia.org/wiki/Function_%28computer_science%29)."

L'expression 'composer des fonctions' signifie construire des fonctions complexes à partir de fonctions simples. Dans notre exemple, la fonction de l'année bissextile est déjà assez simple. Mais pour montrer le mécanisme de la composition de fonctions, créons-la à partir de fonctions composantes.

```js
// fonction composante
function divisible(dividende, diviseur) {
    return dividende % diviseur == 0
}

// fonction composée
function isLeapYear(year) {
    let isLeap = false;
    divisible(year, 4) && (isLeap = true);
    divisible(year, 100) && (isLeap = false);
    divisible(year, 400) && (isLeap = true);
    return isLeap;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear(2023)); // Sortie : false
console.log(isLeapYear(1900)); // Sortie : false
console.log(isLeapYear(2000)); // Sortie : true
```

<h3 id="short-circuiting">Détour : Court-circuit !</h3>

Ci-dessus, vous utilisez une fonction pour en construire une autre - une approche basée sur les composants que vous suivez également dans la bibliothèque front-end React basée sur JavaScript.

Mais attendez, avant d'aller plus loin dans React, que fait ce '&&' dans ces trois lignes de la fonction 'isLeapYear' lorsque nous n'utilisons aucune instruction if-else ?

Bienvenue dans l'évaluation en court-circuit des opérateurs logiques. Dans ce processus, une expression cesse d'être évaluée dès que son résultat est déterminé. Donc, si deux côtés contiennent un ET logique (&&) entre eux, si le premier côté est faux, cela rend l'expression entière fausse - donc il ne lit pas (n'exécute pas) le deuxième côté.

Mais si le premier côté est évalué à vrai, il lit (exécute) davantage le deuxième côté pour évaluation. Et dans ce processus, il effectue cette affectation du côté droit de && dans notre exemple.

De même, le processus lorsque le OU logique (||) est impliqué est tel que si le côté gauche est évalué à vrai, l'expression entière est vraie (il lui faut une condition évaluée à vrai pour || pour que l'expression entière soit vraie). Ensuite, le deuxième côté est ignoré. Le deuxième côté est lu ou exécuté uniquement lorsque le premier côté est évalué à faux.

Vous pouvez utiliser ce type de logique d'évaluation comme un remplacement pour les vérifications de conditions 'if'. Pour plus d'exemples sur son fonctionnement dans différents scénarios, lisez la section 'Court-circuit des Opérateurs Logiques (&& et ||)' dans mon article de blog où j'ai discuté [de certaines nuances des Opérateurs JavaScript](https://codenil.medium.com/javascript-operators-some-nuances-57300eb2c354).

<h3 id="declarative-programming">Encapsulation et Programmation Déclarative</h3>

Revenant à REACT et aux composants, l'idée de construire des fonctions ou des composants de composition est enracinée dans le besoin d'encapsulation. Avec l'encapsulation, vous pouvez cacher les détails complexes, comme dans une capsule, et l'utiliser à plusieurs reprises sans vous soucier beaucoup de sa complexité sous-jacente.

Essentiellement, vous proclamez simplement (déclarez) ce dont vous avez besoin plutôt que de vous fatiguer avec la charge de travail et le mal de tête de la manière dont vous pouvez le faire étape par étape avec des instructions de type 'faire-ceci' et 'faire-cela' (impératifs).

Cela, brièvement, est la programmation déclarative pour vous.

<h2 id="code-quality">Aller Au-delà avec la Qualité du Code</h2>

Jusqu'à présent, nous avons couvert les structures logiques et les paradigmes de programmation, mais maintenant, examinons le troisième aspect : la qualité du code.

<h3 id="validations">Validations : Au-delà des Spécifications de Base</h3>

Les exigences que nous avons établies au début ne considéraient que les entrées valides. Que se passe-t-il si la fonction est appelée avec des arguments qui ne sont pas les idéaux - comme un non-nombre, ou même si un nombre mais un non-entier ?

Pour répondre à cela, nous pouvons construire une logique de validation. Pour construire une logique de validation, vous devez penser à toutes les différentes manières dont la valeur d'entrée (l'argument passé à votre fonction) peut ne pas être utilisable pour vous.

Si l'une de ces manières non utilisables se présente, vous devez retourner quelque chose qui a plus de sens - vous ne pouvez pas donner un verdict comme vrai ou faux dans ce cas. Vous pouvez retourner quelque chose de plus neutre (comme undefined ou null) pour indiquer que la fonction a rencontré une entrée invalide.

```js
function isLeapYear(year) {
  if (typeof year!="number" || year % 1 != 0 || year <= 0) return undefined;
  return ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) ? true : false;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear("TwentyTwentyFour")); // Sortie : undefined
console.log(isLeapYear(2023.99)); // Sortie : undefined
console.log(isLeapYear(0)); // Sortie : undefined
console.log(isLeapYear(-1)); // Sortie : undefined
console.log(isLeapYear("2024")); // Sortie : undefined
```

Mais si vous avez remarqué attentivement, dans notre vérification de la logique de l'année bissextile, nous avons évalué simplement l'égalité ordinaire (==) au lieu de l'égalité stricte (===). Nous ne pouvons pas tirer parti de cela pour une entrée au format chaîne pour une année comme "2024".

Si notre intention est d'accepter strictement un nombre, le type de validation que nous avons écrit est correct, et il serait alors encore plus approprié d'utiliser ===.

Mais si, d'autre part, nous voulons accepter des valeurs comme "2024", nous devons améliorer notre logique de validation comme suit :

```js
function isLeapYear(year) {
  if (isNaN(Number(year)) || year % 1 != 0 || year <= 0) return undefined;
  return ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) ? true : false;
}

// Exemple d'utilisation :
console.log(isLeapYear(2024)); // Sortie : true
console.log(isLeapYear("TwentyTwentyFour")); // Sortie : undefined
console.log(isLeapYear(2023.99)); // Sortie : undefined
console.log(isLeapYear(0)); // Sortie : undefined
console.log(isLeapYear(-1)); // Sortie : undefined
console.log(isLeapYear("2024")); // Sortie : true
```

<h3 id="unit-testing">Tester de l'Extérieur</h3>

Dans les deux blocs de code ci-dessus, nous écrivons notre code et le testons au même endroit. Mais le code qui passe en production n'aura pas l'opportunité d'inclure de tels journaux de console que nous avons utilisés abondamment pour démontrer l'utilisation d'exemple dans les blocs de code ci-dessus.

C'est là que les tests unitaires entrent en jeu. Dans les tests unitaires, nous exportons d'abord la fonction pour une utilisation dans d'autres endroits (fichiers), puis importons cette fonction dans un fichier de test. Dans ce fichier de test, nous exécutons le test, construisons nos cas, et enfin exécutons ce fichier de test pour exécuter ces tests.

J'ai utilisé le package Jest pour faire ces tests unitaires, et voici le code de mon fichier index et de mon fichier de script de test :

**index.js**

```js
function isLeapYear(year) {
  if (isNaN(Number(year)) || year % 1 != 0 || year <= 0) return undefined;
  return ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) ? true : false;
}

module.exports = isLeapYear;
```

**index.test.js**

```js
const isLeapYear = require('./index.js');

describe('Test isLeapYear', () => {
  it('should return true for leap year', () => {
    expect(isLeapYear(2020)).toBe(true);
  });
  it('should return false for non-leap year', () => {
    expect(isLeapYear(2023)).toBe(false);
  });
  it('should return undefined for invalid input', () => {
    expect(isLeapYear('TwentyTwentyFour')).toBe(undefined);
    expect(isLeapYear('2023.99')).toBe(undefined);
    expect(isLeapYear('0')).toBe(undefined);
    expect(isLeapYear('-1')).toBe(undefined);
  });
  it('should return true for a leap year in string format', () => {
    expect(isLeapYear("2024")).toBe(true);
  });
});
```

J'ai installé Jest en utilisant la commande `npm i jest`. Ensuite, j'ai ajouté `jest` comme valeur pour `test` dans l'objet `scripts` à l'intérieur de mon fichier package.json. Ensuite, lorsque j'ai exécuté `npm test`, il a réussi tous mes cas de test, comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-29-05.25.03.png)
_sortie de test_

Si vous souhaitez modifier et essayer ce code de test unitaire, vous pouvez utiliser et forker ce [projet replit](https://replit.com/@nil-sj/UnitTestingExample).

<h2 id="end-note">Note Finale</h2>

Nous avons passé en revue de nombreux concepts de programmation dans l'exercice ci-dessus. Et une conclusion clé est qu'un programme peut être écrit de multiples façons.

Il existe généralement de nombreuses solutions correctes à un problème de programmation. Les programmeurs débutants devraient donc penser à la partie logique (l'algorithme) plus qu'aux étapes d'exécution exactes lorsqu'ils commencent à résoudre un problème.

Et au fait, si vous vous demandez pourquoi nous avons des années bissextiles, alors ceci est pour vous : le temps que la Terre met pour effectuer une révolution autour du soleil n'est pas exactement de 365 jours (ou 365 x 24 heures) mais environ un quart de jour en plus.

Ce processus peut vous rappeler l'opérateur modulo, représenté par le symbole %, qui retourne le reste d'une opération de division. Ici, le temps approximatif (en heures) pris pour une révolution de la terre est divisé par 24 heures (c'est-à-dire un jour). Il donne un reste d'environ 6 heures.

```js
const approxTimeHrsRev = 8766;
const hrsPerDay = 24;
let completedDaysEachYear;

let remainderHrsPerYear = 8766 % hrsPerDay;
completedDaysEachYear = (approxTimeHrsRev - remainderHrsPerYear) / hrsPerDay;

console.log(`Après ${completedDaysEachYear} jours complets, il reste encore environ ${remainderHrsPerYear} heures chaque année.`);
// Sortie : Après 365 jours complets, il reste encore environ 6 heures chaque année.
```

Pour tenir compte de ces heures manquantes, nous devons ajuster nos calendriers une fois tous les quatre ans lorsque ces portions restantes s'additionnent pour faire - à nouveau approximativement - un jour.

Enfin, parce que ce n'est pas exactement 6 heures, mais un peu plus que cela, nous devons ajuster tous les 100 et 400 ans.