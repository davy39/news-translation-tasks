---
title: Comment utiliser les variables et les types de données en JavaScript – Expliqué
  avec des exemples de code
subtitle: ''
author: Austin Asoluka
co_authors: []
series: null
date: '2024-08-19T13:33:18.714Z'
originalURL: https://freecodecamp.org/news/how-to-use-variables-and-data-types-in-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723754441356/34416215-e12b-41ec-8c11-332d2c8214e1.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: variables
  slug: variables
- name: beginner
  slug: beginner
seo_title: Comment utiliser les variables et les types de données en JavaScript –
  Expliqué avec des exemples de code
seo_desc: 'A variable is like a box where you can store data or a reference to data.

  In this article, you will learn how to create and use variables. You''ll also learn
  about the different data types in JavaScript and how to use them.

  Let''s get started!

  Table of...'
---

Une variable est comme une boîte où vous pouvez stocker des données ou une référence à des données.

Dans cet article, vous apprendrez comment créer et utiliser des variables. Vous apprendrez également les différents types de données en JavaScript et comment les utiliser.

Commençons !

## Table des matières

* [Qu'est-ce qu'une variable ? Exemple #1](#heading-questce-quune-variable-exemple-1)
    
* [Qu'est-ce qu'une variable ? Exemple #2](#heading-questce-quune-variable-exemple-2)
    
* [Qu'est-ce qu'une variable ? Exemple #3](#heading-questce-quune-variable-exemple-3)
    
* [Comment déclarer une variable](#heading-comment-declarer-une-variable)
    
* [Assignation et initialisation de variable](#heading-assignation-et-initialisation-de-variable)
    
* [Comment appeler une variable](#heading-comment-appeler-une-variable)
    
* [Comment nommer les variables](#heading-comment-nommer-les-variables)
    
    * [Mots réservés en JavaScript](#heading-mots-reserves-en-javascript)
        
    * [Règles pour nommer les variables en JavaScript](#heading-regles-pour-nommer-les-variables-en-javascript)
        
    * [Conventions de nommage des variables populaires](#heading-conventions-de-nommage-des-variables-populaires)
        
* [Types de données des variables](#heading-types-de-donnees-des-variables)
    
    * [Types de données primitifs](#heading-types-de-donnees-primitifs)
        
    * [Types de référence en JavaScript](#heading-types-de-reference-en-javascript)
        
* [Résumé](#heading-resume)
    

### Qu'est-ce qu'une variable ? Exemple #1

Lorsqu'un enfant naît, on lui donne un nom et tout au long de sa vie, il sera désigné par ce nom (sauf si le nom est changé à un moment donné).

Avez-vous déjà vu quelqu'un sans nom ? Comment avez-vous pu l'appeler ?  
Dans un monde idéal, tout le monde devrait avoir un nom ou une manière unique de les désigner. En JavaScript, chaque variable a un nom.

> Tout le monde doit avoir un nom ou une manière de les désigner.

### **Qu'est-ce qu'une variable ? Exemple #2**

Dans une équation mathématique, lorsque nous disons `x = 1`, cela signifie : "partout où vous voyez `x`, vous devez le remplacer par `1`". Dans ce cas, `x` est une variable, tandis que `1` est sa valeur. C'est-à-dire : `x` pointe vers `1`.

Cela signifie que sans `x`, il n'y aura aucune référence à `1`. Il pourrait y avoir d'autres occurrences de `1` dans l'équation, mais celles-ci seront différentes du `1` auquel `x` faisait référence. Par exemple :

```javascript
/* Le code ci-dessous signifie que x est 1 
 * Donc pendant l'exécution, partout où x apparaît après la ligne ci-dessous, 
 * le compilateur remplace x par 1.
 */
let x = 1;
let y = 1; // la valeur à laquelle y fait référence est différente de celle de x
console.log(x); // Cette ligne affichera 1 dans la console.
```

Dans l'extrait de code ci-dessus, `x` fait référence à la valeur 1, et `y` fait également référence à une autre valeur 1, mais notez que les deux valeurs sont distinctes, tout comme vous pouvez avoir deux marques différentes d'eau en bouteille même si elles contiennent toutes deux de l'eau.

Ainsi, lorsque nous mentionnons le nom de la variable `x`, nous obtenons la valeur assignée à cette variable.

### **Qu'est-ce qu'une variable ? Exemple #3**

Une variable peut être conceptualisée comme un conteneur. Le nom de la variable sert d'identifiant, sa valeur représente le contenu du conteneur, et son type spécifie la nature de ces contenus.

![Bouteille d'eau](https://cdn.hashnode.com/res/hashnode/image/upload/v1690903992237/a783721f-1fbc-4c84-8df6-24a49e7dddb3.jpeg align="center")

Une marque d'eau populaire ici au Nigeria est connue sous le nom de "Eva".

Disons que vous avez acheté de l'eau Eva, que vous l'avez rapportée chez vous et que vous l'avez placée parmi d'autres marques d'eau. Vous pouvez facilement dire à quelqu'un : "S'il vous plaît, donnez-moi l'eau Eva là-bas" et grâce au nom, il devient facile pour la personne d'identifier et de prendre exactement ce dont vous avez besoin.

Tout comme vous pouvez facilement distinguer votre eau Eva des autres marques d'eau par son nom, une variable est identifiée de manière unique par son nom dans un programme. Bien qu'il puisse y avoir plusieurs variables stockant des données, le nom spécifique d'une variable vous permet de référencer son contenu de manière précise.

En JavaScript, les valeurs sont assignées à un nom et chaque fois que nous avons besoin de cette valeur, nous mentionnons simplement le nom auquel elle a été assignée. Lorsque le code s'exécute, le nom de cette variable est remplacé par la valeur à laquelle il fait référence.

Dans le cas de l'analogie ci-dessus, le contenu de la bouteille est de l'eau et le type est un liquide. Mais en supposant que nous avons une variable `x` qui fait référence à la valeur `1`, le type de la variable est `number`.

```javascript
// Ajoutez la ligne de code ci-dessous à l'extrait de code précédent pour
// découvrir le type de données de x ;
console.log(typeof x)
```

Dans l'extrait de code ci-dessus, `number` est affiché dans la console car la variable x contient la valeur `1` qui est un nombre.

**Les variables existent dans notre programme pour nous aider à contenir des valeurs et à pouvoir les référencer chaque fois que nous en avons besoin**. **Partout où une variable est mentionnée, la valeur de cette variable est ce qui est utilisé pour le calcul à ce moment-là**.

## Comment déclarer une variable

```javascript
let score;
```

Le programme ci-dessus déclare/crée une variable appelée `score`.

En JavaScript, créer des variables est aussi simple que cela. Le type de la variable est le type de la valeur stockée dans celle-ci. C'est-à-dire, si la variable `score` contient une valeur de `1`, le type de la variable `score` est `number`. Nous pouvons donc dire que `score` est une variable de type nombre.

Pour créer une variable, nous devons faire ce qui suit ;

1. Déclarer la variable en utilisant l'un de ces mots-clés : `let`, `const` ou `var`.
    
2. Déterminer un nom pour appeler la variable et l'écrire sur la même ligne que le mot-clé utilisé à l'étape 1.
    

```javascript
let score; // crée la variable 'score'
```

Remarquez que cette fois, nous ne lui avons pas donné de valeur. Nous avons simplement créé un conteneur qui stockera quelque chose. Pour l'instant, il est vide. Bien qu'il n'ait pas de contenu pour le moment, nous lui fournirons certainement du contenu.

## Assignation et initialisation de variable

Nous pouvons assigner une valeur à une variable en utilisant l'opérateur d'assignation (`=`) — le nom de la variable à gauche de celui-ci, et la valeur à droite.

```javascript
score = 1;
```

L'extrait de code ci-dessus assigne `1` comme valeur de `score` (c'est ce qu'on appelle **l'assignation de variable**).

Lorsque nous combinons la déclaration de variable et l'assignation en une seule opération, cela s'appelle **l'initialisation de variable**.

```javascript
let score = 1;
```

Comme on peut le voir ci-dessus, nous déclarons la variable `score`, et immédiatement sur la même ligne, nous assignons la valeur `1` à celle-ci.

Cela signifie que nous avons fourni une valeur initiale pour la variable lorsqu'elle a été créée.

## Comment appeler une variable

Si vous souhaitez utiliser une variable pour une opération à tout moment dans votre programme, vous pouvez simplement "l'appeler". **Appeler** une variable revient à la **mentionner** ou à **l'utiliser**.

```javascript
console.log(score + 1) // 2
```

Dans l'extrait de code ci-dessus, la variable `score` a été **utilisée** dans la ligne de code. Par conséquent, elle sera remplacée par sa valeur réelle `1` pendant l'exécution du code. Cela signifie que nous aurons `1 + 1` exécuté, ce qui donnera `2`.

Dans la section suivante, apprenons comment nommer correctement nos variables afin de garantir que nos codes soient propres et lisibles.

## Comment nommer les variables

Tout comme nommer un humain, un animal de compagnie ou étiqueter un objet, nous réfléchissons toujours beaucoup pour nous assurer que le nom raconte une histoire et donne une idée de ce que nous ressentons à propos du rôle de cet animal, humain ou objet.

JavaScript est quelque peu libéral en ce qui concerne la manière dont le nommage des variables peut être fait et aussi combien de temps cela pourrait prendre.

Par exemple, `pneumonoultramicroscopicsilicovolcanoconiosis` est un nom de variable valide en JavaScript même s'il est long.

Il est généralement une bonne pratique de donner des noms significatifs aux variables et ils doivent être d'une longueur raisonnable.

Laissez vos variables être simples et contextuelles. Par exemple : `author`, `publishedDate`, `readTime`, `shouldCompress`, et ainsi de suite.

Cela devrait être auto-explicatif. Évitez simplement les noms cryptiques lorsque cela est possible.

### Mots réservés en JavaScript

Même si nous pouvons créer des variables comme nous le souhaitons, certains noms sont déjà utilisés dans JavaScript pour signifier quelque chose de spécifique. Ces noms ne peuvent pas être utilisés par un développeur pour identifier une variable. Ils sont appelés mots réservés.

Par exemple, le mot-clé `catch` est utilisé pour gérer correctement une erreur et l'empêcher de faire planter une application. Par conséquent, vous ne pouvez pas appeler une variable `catch` dans votre programme.

Voici tous les mots réservés en JavaScript :

`arguments` `await` `break` `case` `catch` `class` `const` `continue` `debugger` `default` `delete` `do` `else` `enum` `eval` `export` `extends` `false` `finally` `for` `function` `if` `implements` `import` `in` `Infinity` `instanceof` `interface` `let` `NaN` `new` `null` `package` `private` `protected` `public` `return` `static` `super` `switch` `this` `throw` `true` `try` `typeof` `undefined` `var` `void` `while` `with` `yield`

**NOTE** : Vous n'avez pas besoin de mémoriser ces mots-clés. Si vous essayez de les utiliser, vous obtiendrez une erreur et vous apprendrez à les reconnaître et à les connaître avec l'expérience.

De plus, JavaScript a certaines règles que vous devez suivre lors du nommage des variables ainsi que des conventions généralement acceptées (meilleures pratiques) que vous devriez connaître. Parlons-en dans la section suivante.

### **Règles pour nommer les variables en JavaScript**

* Les mots réservés ne peuvent pas être utilisés comme noms de variables.
    
* La première lettre de votre nom de variable doit être une lettre de l'alphabet, un trait de soulignement (_), ou un signe dollar ($). Vous ne pouvez pas utiliser un nombre comme premier caractère de votre nom de variable. Bien que d'autres types de caractères spéciaux soient autorisés à commencer un nom de variable, par bonne pratique et pour éviter les complexités au début, vous devriez toujours commencer par une lettre. L'utilisation d'un trait de soulignement ou d'un signe dollar est symbolique par convention et nous apprendrons ce qu'ils signifient dans le futur.
    
* Le reste du nom de la variable peut contenir n'importe quoi sauf des symboles, des ponctuations et des caractères réservés (+, -, *, et ainsi de suite).
    
* Les noms de variables sont sensibles à la casse. Cela signifie que `Boy` et `boy` seront traités comme des variables différentes dans votre programme.
    
* Un nom de variable peut être aussi long que nécessaire pour qu'il ait du sens. Il n'y a pas de limite imposée par le langage.
    
* Les espaces ne sont pas autorisés dans les noms de variables.
    

### **Conventions de nommage des variables populaires**

* Les noms de variables avec plusieurs mots doivent utiliser la **casse camel**. C'est-à-dire, le premier mot doit être entièrement en minuscules tandis que la première lettre des mots suivants doit être en majuscule : `studentRegistrationNumber`
    
* Utilisez des lettres majuscules pour les variables constantes : `const PI = 3.1432`
    
* Si une variable constante est composée de plusieurs mots, utilisez la casse snake (séparation des mots par un trait de soulignement) : `const PROGRAM_NAME = "Vacation planner"`
    
* Si une variable est destinée à être privée, préfixez son nom avec un trait de soulignement : `let _memorySize = 2042`.  
    **Note** : Cela sert simplement à informer l'équipe (les autres travaillant sur le projet) que l'auteur a l'intention de l'utiliser comme privée. Cela n'empêche pas la valeur de la variable d'être accessible (il existe d'autres moyens de garantir cela).
    
* Il est courant de préfixer les variables booléennes avec `is` ou `has` : `let isMarked = true`.
    

Dans la section suivante, nous apprendrons les différents types de données et comment travailler avec eux.

## Types de données des variables

Le type de données signifie simplement "type de données" 😉.

Le mot "données" dans ce contexte signifie une pièce d'information. Nous utiliserons parfois le mot "valeur" pour signifier des données et vice versa.

En JavaScript, nous stockons des valeurs de différents types dans des variables. Ces valeurs ont différentes attributs/propriétés et le type de données qu'une variable contient déterminera les opérations que vous pouvez effectuer avec cette variable.

Par exemple, si vous avez de l'eau (valeur) stockée dans un conteneur (variable), vous pouvez utiliser l'eau (valeur) pour laver ou boire, mais si ce qui est stocké dans le conteneur sont des bonbons, vous pouvez les manger mais vous ne pourrez pas les utiliser pour laver.

Si vous avez une variable qui contient des nombres, vous pouvez les utiliser pour effectuer des opérations arithmétiques. Si la variable contient un booléen, vous ne pouvez pas l'utiliser pour des opérations arithmétiques mais elle peut être utilisée pour des opérations logiques.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Le type de valeur stockée dans la variable détermine ce que vous pouvez faire avec elle.</div>
</div>

Les types de données en JavaScript sont classés en deux groupes principaux, à savoir ;

* **Primitif** : Number, String, Boolean, Undefined, Null, BigInt, Symbol
    
* **Réference** : Object, Array, Function
    

Dans cet article, nous ne parlerons pas des Symboles et des BigInt pour éviter les complexités. Le but est de faire de notre mieux pour expliquer les concepts fondamentaux aux débutants de la manière la plus simple possible.

Considérons les types de données primitifs.

### **Types de données primitifs**

Les variables ayant ce type de données sont appelées primitives car elles contiennent des valeurs simples. Le mot [primitive](https://www.google.com/search?q=primitive&rlz=1C5CHFA_enNG1050NG1050&oq=primitive&aqs=chrome..69i57j0i271.760j0j7&sourceid=chrome&ie=UTF-8) peut être traduit pour signifier non complexe.

Les valeurs primitives sont généralement une seule unité comme 1, "cup", null, undefined, true, et ainsi de suite. Considérons brièvement comment ces types de données sont utilisés et quel type d'opérations vous pouvez effectuer avec eux.

* **NUMBER** : En JavaScript, tous les nombres sont des valeurs à virgule flottante. Qu'ils soient des nombres sans points décimaux comme un nombre entier qui peut être négatif, positif, zéro, ou des valeurs avec un point décimal comme 0.2, -0.5, 1, -2, 0. Ils sont tous du type `number`.
    

Ce type de valeur peut être utilisé dans des opérations arithmétiques comme la multiplication, la division, la soustraction, l'addition, le modulo, et ainsi de suite.

```javascript
let score1 = 2;
let score2 = 5;
let averageScore = (score1 + score2) // 2
console.log(averageScore) // 3.5
```

Pour vérifier le type de données de la valeur d'une variable, utilisez l'opérateur `typeof` comme ceci : `typeof variableName`. C'est-à-dire : `typeof score1`

Dans l'extrait de code ci-dessus, `score1` est une variable qui contient une valeur de `2`, `score2` contient une valeur de `5`, tandis que la variable `averageScore` stocke le résultat de la division de la somme de `score1` et `score2` par `2`, ce qui donne `3.5`.

L'utilisation de l'opérateur `typeof` sur la variable `score1` retournera `number`.

**Exercice** : Copiez le code dans l'extrait ci-dessus et exécutez-le dans votre éditeur de code pour voir comment il fonctionne pour vous. Vous pouvez jouer avec les valeurs et utiliser l'opérateur `typeof` pour vérifier le type de données des variables.

Lors de l'exécution d'opérations arithmétiques, vous pouvez rencontrer d'autres types de nombres comme `Infinity`, `-Infinity` et `NaN`.

**Infinity** signifie quelque chose sans aucune limite. Une façon d'atteindre l'infini est de diviser un nombre par 0.

```javascript
let result = 12 / 0;

console.log(result) // Infinity
```

Dans le code ci-dessus, nous avons divisé `12` par `0` et enregistré le résultat dans la console qui imprime `Infinity`.

**Negative Infinity** est utilisé pour désigner un nombre qui est inférieur à tout nombre naturel. Pour arriver à l'infini négatif, copiez le code dans l'extrait ci-dessous et exécutez-le dans votre environnement de codage.

```javascript
console.log(Number.NEGATIVE_INFINITY) // -Infinity
```

**NaN** signifie Not **a** Number. Cela se produira lorsque vous essayez de réaliser une opération mathématique impossible comme montré ci-dessous :

```javascript
const result = "Ella" / 2; // Essayer de diviser une chaîne avec un nombre
console.log(result) // NaN
```

La première ligne du code ci-dessus essaie de diviser une chaîne par un nombre et le résultat est `NaN`.

Vous n'atteindrez pas souvent l'infini ou -Infinity en tant que débutant faisant des choses basiques/intermédiaires, mais c'est quelque chose dont vous devriez être conscient afin de ne pas vous énerver lorsque vous le voyez se produire dans votre code (c'est quelque chose que vous ne voulez pas mémoriser dans votre tête). `NaN` se produira plus souvent que les autres. Lorsque vous le voyez, sachez simplement que quelque chose ne va pas avec l'opération que vous essayez de réaliser.

* **STRING** : En JavaScript, une chaîne est une collection de caractères enfermés dans des guillemets : `"Cathy"`.
    

L'extrait ci-dessous montre comment une chaîne peut être utilisée dans un programme JavaScript :

```javascript
let author = "Sleekcodes";
let publishedDate = "14 August 2023";

console.log("Written by: " + author); // Written by: Sleekcodes
console.log("Published on: " + publishedDate); // Published on: 14 August 2023"
```

Je suis sûr que vous avez remarqué l'opérateur + utilisé avec des chaînes. Lorsque cela se produit, le résultat est que la chaîne à droite et celle à gauche seront jointes pour n'en former qu'une. Cela s'appelle la concaténation de chaînes.

Le code ci-dessus dit simplement : "Créez une variable appelée `author` et stockez le texte `"sleekCodes"` comme sa valeur, créez une autre variable `publishedDate` et stockez le texte `"14 August 2023"` dans celle-ci."

Ensuite, à la ligne 4, nous disons au moteur JavaScript d'enregistrer (imprimer) la chaîne "Written by: Sleekcodes**"** dans la console. La ligne 5 dit également d'enregistrer **"**Published on: 14 August 2023**"** dans la console.

Remarquez que dans le code ci-dessus, pendant l'exécution, `author` est remplacé par la valeur "Sleekcodes" et `publishedDate` est remplacé par "14 August 2023" où ils sont utilisés.

Les chaînes sont utilisées pour dépeindre ou transmettre des données en format texte/alphabétique. Une chaîne peut être composée de zéro ou plusieurs caractères. Une chaîne qui n'a aucun caractère est appelée une chaîne vide. Par exemple : `""`.

* **BOOLEAN** : Lorsque nous devons représenter des données dans deux états possibles seulement comme vrai/faux, on/off, ou oui/non, nous utilisons des valeurs booléennes. La valeur d'une variable booléenne est soit `true` soit `false`.
    

```javascript
let isQualified = true

if (isQualified) {
    console.log("Tola is qualified"); // Tola is qualified
}
```

Le code ci-dessus affichera l'instruction "Tola is qualified", car la valeur de la variable `isQualified` est true. Cette opération est un type d'opération conditionnelle. C'est là que les valeurs booléennes excellent.

**Exercice** : Changez la valeur de `isQualified` pour qu'elle soit `false` et observez ce qui se passe.

* **UNDEFINED** : Cela est à la fois une valeur et un type de données. `undefined` est utilisé pour indiquer qu'une variable n'a pas de valeur définie. Par exemple, lorsqu'une variable est déclarée (`let age`), et que vous essayez d'accéder à sa valeur, le résultat serait `undefined`.
    

```javascript
let age; // notez qu'il n'y a pas de valeur assignée à la variable ici

console.log(age); // undefined
```

Dans l'extrait de code ci-dessus, parce que age n'est pas donné de valeur explicite, le compilateur assigne la valeur `undefined` à la variable par défaut.

**Exercice** : Utilisez l'opérateur `typeof` sur la variable `age` et voyez ce que vous obtenez. Assignez également la valeur `undefined` à `age` et utilisez l'opérateur `typeof` sur celle-ci à nouveau pour voir le résultat.

* **NULL** : Null est une valeur que nous pouvons assigner à une variable pour indiquer qu'elle n'a pas de valeur. Elle est utilisée pour représenter "vide" ou "inconnu".
    

```javascript
let age = null;

console.log(age); // null
```

Comme on peut le voir dans l'extrait de code ci-dessus, au lieu de laisser le compilateur assigner `undefined` pour nous, nous indiquons explicitement que la variable n'a pas de valeur en lui assignant la valeur `null`.

Cela signifie que `age` est vide ou inconnu.

Les gens se confondent souvent sur la différence entre `undefined` et `null`. L'un est la valeur par défaut assignée à une variable sans valeur explicite, tandis que l'autre (`null`) est une valeur assignée à une variable par le programmeur délibérément pour indiquer que la variable est vide. En règle générale, ne pas assigner `undefined` à une variable, utilisez plutôt `null` (le compilateur auto-assigne `undefined` là où c'est nécessaire).

Les types de données primitifs n'ont pas de complexité. Ils sont simples et directs (une seule valeur). Cette déclaration aura plus de sens lorsque vous lirez comment les types de référence fonctionnent dans la section suivante.

Considérez l'image ci-dessous.

![concept de types primitifs](https://cdn.hashnode.com/res/hashnode/image/upload/v1691169563292/8cd6a8de-e6c5-46fe-8271-c2a522b6c663.png align="center")

**La partie A** ci-dessus est le code que vous écrivez, tandis que **la partie B** est ce qui se passe lorsque le code s'exécute. Pour les types de données primitifs, la valeur est simplement assignée à la variable (c'est direct).

Les valeurs primitives sont passées par valeur (elles ne génèrent aucune référence). Ne vous inquiétez pas de ce que cela signifie pour l'instant car nous expliquerons dans la section suivante.

## Types de référence en JavaScript

Les types de données de référence sont des données passées par "référence". Une compréhension approfondie de cette déclaration est cruciale tout au long de votre carrière en tant que développeur JavaScript, alors faites bien attention au concept que nous allons apprendre.

Considérez attentivement l'image ci-dessous.

![concept de types de référence](https://cdn.hashnode.com/res/hashnode/image/upload/v1691062567476/e31e1bfe-6b85-418e-a88a-e19810f11839.png align="center")

Dans l'image ci-dessus, **la partie A** est le code que vous écrivez, tandis que **la partie B** est ce qui se passe "derrière les scènes".

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Utilisez l'image ci-dessus pour suivre l'explication suivante.</div>
</div>

Lorsque vous créez une variable dont le type de données est dans la catégorie de référence (objets, fonctions, tableaux), au lieu que la valeur soit directement assignée à la variable, une référence est générée pour la valeur et cette référence est ce qui est assigné à la variable.

La référence est assignée à la variable, mais elle pointe vers la valeur réelle.

Cela signifie que lorsque vous essayez d'utiliser la variable n'importe où, vous travaillez avec la référence de la valeur réelle et tout ce qui est fait à la référence affecte la valeur réelle.

Pensez-y comme un intermédiaire entre la valeur réelle et le nom de la variable.

Considérez l'exemple ci-dessous :

```javascript
let studentInfo = {
    name: "John Doe",
    age: 205
}

let staffInfo = studentInfo //6. Cela signifie ; assigner la référence de studentInfo à staffInfo

staffInfo.name = "Lorry Sante" //8. Changer la valeur de la clé name dans la référence que staffInfo détient.

console.log(studentInfo.name) //9. Lorry Sante
```

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text"><strong>Essayez ceci :</strong> Aux lignes 7 et 8, enregistrez la valeur de <a target="_blank" rel="noopener noreferrer nofollow" href="http://studentInfo.name" style="pointer-events: none"><code>studentInfo.name</code></a> et <a target="_blank" rel="noopener noreferrer nofollow" href="http://staffInfo.name" style="pointer-events: none"><code>staffInfo.name</code></a> dans la console pour voir ce qu'ils sont.</div>
</div>

Vous devriez remarquer que, changer `name` dans l'objet `staffInfo` (ligne 8), entraîne également le changement du nom dans l'objet `studentInfo` (comme on peut le voir dans la sortie de la ligne 9).

En fait, les deux variables pointent techniquement vers la même valeur (voir l'image ci-dessous) ;

![stockage des variables de types de référence](https://cdn.hashnode.com/res/hashnode/image/upload/v1691069171621/a53d4f52-6b86-4581-85fc-57452cbc90be.png align="center")

Lorsque nous disons qu'une variable est passée par référence, cela signifie que partout où cette variable est utilisée, vous interagissez avec une référence (qui pointe) vers sa valeur réelle.

Ainsi, dans l'extrait de code ci-dessus, lorsque `studentInfo` a été assigné à `staffInfo`, nous avons simplement fait en sorte que `staffInfo` stocke la référence de la variable `studentInfo`, ce qui signifie effectivement que les variables `staffInfo` et `studentInfo` pointent toutes deux vers la même valeur.

Par conséquent, si la référence générée pour `studentInfo` est `000xx2` et qu'il est vrai que pendant l'exécution, les variables sont remplacées par ce qu'elles contiennent, alors `staffInfo = studentInfo` deviendrait `staffInfo = 000xx2` pendant l'exécution, tandis que `staffInfo.name` deviendrait `000xx2.name`.

Si nous avions écrit `studentInfo.name`, alors pendant l'exécution, cela deviendrait `000xx2.name`, il devrait être clair maintenant que `studentInfo` et `staffInfo` contiennent tous deux des références à une seule valeur. Ils sont comme différentes routes vers une seule destination.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Si c'est la première fois que vous apprenez ce concept, vous devriez répéter la section ci-dessus avant de continuer. Cela deviendra plus clair et lorsque nous commencerons à opérer avec des types de référence, vous serez content d'avoir lu cet article.</div>
</div>

Il existe trois principaux types de données de référence que vous rencontrerez principalement dans votre parcours en tant que développeur JavaScript : Object, Array et Function. Examinons-les un par un.

* **OBJECT** : Un objet est une structure de données utilisée pour stocker des données complexes en paires clé/valeur. La variable créée dans la session précédente a un type d'objet comme ceci :
    

```javascript
let studentInfo = {
    name: "John Doe",
    age: 205
}
```

Vous pouvez voir que ce n'est pas primitif (simple). Contrairement aux types primitifs avec des valeurs simples, un objet peut être utilisé pour stocker différentes informations qui peuvent être composées même de types primitifs et de types de référence.

Les objets stockent les données en paires clé/valeur comme suit : `{key: value}`

Dans l'extrait de code ci-dessus, `name` est la clé, tandis que `"John Doe"` est sa valeur. De même, `age` est la clé, tandis que `205` est sa valeur.

Si vous remarquez, `name` et `age` ont tous deux des valeurs primitives (chaîne et nombre).

Pour accéder à la valeur d'un objet, nous utilisons le nom de l'objet, la notation point (.) et la clé dont nous voulons accéder à la valeur. Par exemple : `objectName.key`.

Les objets peuvent également contenir des objets imbriqués comme suit :

```javascript
let studentInfo = {
    name: "John Doe",
    age: 205,
    beneficiary: {
       name: "Tira Doe",
       age: 200,
       relationship: "Wife"
    }
}
```

Dans l'exemple ci-dessus, l'objet `studentInfo` a un objet imbriqué appelé `beneficiary`. `beneficiary` est une clé dont la valeur est un objet (type de référence). Les objets peuvent encore contenir des tableaux et des fonctions.

L'accès à la valeur associée à une clé dans un objet au sein d'un autre objet (objet imbriqué) est naturel. Nous utilisons simplement la notation point. Comme ceci : `parentObjectName.nestedObjectName.key`

Par exemple, pour accéder au nom du bénéficiaire dans l'objet `studentInfo` ci-dessus, nous écrivons simplement `studentInfo.beneficiary.name`.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Il n'y a pas de limite à l'imbrication des objets dans les objets. Cependant, assurez-vous que l'imbrication est nécessaire pour ce que vous voulez réaliser et évitez une imbrication excessive pour des raisons de simplicité.</div>
</div>

Ce n'est pas tout ce que vous devez savoir sur les objets, mais c'est une très bonne façon de commencer.

* **ARRAY** : Un tableau est une sorte d'objet mais stocke les données en utilisant des index automatiquement assignés au lieu de clés.
    

Un tableau est créé en écrivant une liste de valeurs séparées par des virgules et enfermées dans des crochets : `[0, 1, 2, 3, "Tosin", "Mike", {name: "Abel Joe", age: 250}]`

Si vous prêtez une attention particulière aux valeurs utilisées dans le tableau ci-dessus, vous remarquerez qu'elles sont de différents types de données. Oui, les tableaux vous permettent également de stocker des valeurs de différents types en un seul endroit, mais cela est fortement déconseillé (vous ne devriez pas le faire du tout). Les valeurs dans un tableau doivent toutes être du même type.

Exemple d'un tableau correct : `let scores = [1, 3, 5, 6, 9, 12]`

Pour accéder à une valeur dans un tableau, nous spécifions simplement le nom du tableau, suivi d'un crochet `[]` sans aucun espace entre le nom et le crochet. Ensuite, à l'intérieur du crochet, fournissez l'index de la valeur que vous souhaitez accéder. C'est-à-dire : `arrayName[index]`.

Qu'est-ce qu'un index et comment savons-nous quel index fait référence à la valeur que nous voulons accéder ?

Un index est simplement un nombre automatiquement assigné à une valeur de tableau. Vous pouvez le considérer comme une adresse pour les valeurs dans le tableau. Les tableaux sont indexés à partir de `0` (ce qui signifie qu'ils commencent à compter à partir de zéro).

Pour déterminer l'index de la valeur que vous souhaitez accéder, commencez à compter à partir du début du tableau et votre compte doit commencer à 0.

Considérez l'image ci-dessous ;

![tableau et index](https://cdn.hashnode.com/res/hashnode/image/upload/v1691072847798/ca5bc276-f024-40eb-b69e-b8e31f17314f.png align="left")

Pour accéder à la valeur `80` dans le tableau `scores` représenté dans l'image ci-dessus, nous écrivons simplement `scores[3]`

Il y a beaucoup de choses que vous pouvez faire avec les tableaux en tant que développeur JavaScript. Pour l'instant, voici une simple introduction au type de données tableau.

* **FUNCTION** : Une fonction est un type différent de variable et elle est déclarée différemment (en utilisant le mot-clé `function` au lieu de `let`, `const` ou `var`). C'est une construction utilisée pour effectuer une tâche spécifique.
    

Par exemple, si vous devez additionner deux nombres plusieurs fois dans votre code, il est préférable de créer une fonction dédiée à cette tâche. En réutilisant cette fonction, vous évitez le code redondant et améliorez la maintenabilité du code par rapport à l'écriture répétée de la logique d'addition. Attendez !!! Vous n'êtes pas perdu. L'exemple ci-dessous va confirmer cela 😊

Scénario 1 (sans fonction) :

```javascript
let num1 = 2;
let num2 = 3;
let result = num1 + num2;

console.log(result) // 5

let num3 = 3;
let num4 = 8;
let result2 = num3 + num4;

console.log(result2) // 11
```

Scénario 2 (avec fonction) :

```javascript
// déclaration de fonction.
function addNumbers (num1, num2) {
    return num1 + num2;
}

console.log(addNumbers(2, 3)); // 5
console.log(addNumbers(3, 8)); // 11
```

Vous conviendrez que le scénario 2 contient moins de code, semble plus propre et même plus naturel.

Les fonctions nous permettent d'écrire des aides que nous pouvons appeler pour effectuer un travail spécifique pour nous à tout moment. Nous devons simplement lui dire comment faire le travail une fois et l'appeler chaque fois que nous avons besoin qu'il fasse ce travail (en passant les informations requises pour la tâche en tant qu'arguments) et il livre.

Syntaxe des fonctions :

Pour écrire une fonction, nous utilisons le mot-clé `function`, suivi du nom de la fonction : `functionName`, une paire de parenthèses `()`, et une paire d'accolades `{}`.

```javascript
function functionName () {}
```

Il y a quelques choses/conventions que vous devriez avoir à l'esprit lors de l'écriture de fonctions :

* Les noms de fonctions doivent suivre les mêmes règles de nommage que les variables.
    
* Les noms de fonctions doivent être des verbes (pour dépeindre une action).
    
* La logique du code pour la tâche réelle doit être écrite entre les accolades ouvrantes `{` et fermantes `}`.
    
* Si des valeurs sont requises pour effectuer la tâche, elles doivent être passées à la fonction en tant qu'arguments. Dans ce cas, lors de la déclaration de la fonction, les paramètres doivent être indiqués entre les parenthèses ouvrantes `(` et fermantes `)` de manière séparée par des virgules. C'est-à-dire : `function addNumbers(num1, num2)...`.
    
* Si aucune donnée n'est requise pour effectuer la tâche, alors les parenthèses ouvrantes `(` et fermantes `)` doivent être laissées vides : `function sayHi()...`.
    

Un paramètre est une variable définie entre les parenthèses ouvrantes `(` et fermantes `)` d'une fonction lors de sa déclaration : `function doSomething (param1, param2) {...}`.

Un argument est la valeur passée à la fonction lors de son appel/invocation : `doSomething(1, 2)`

Comme on peut le voir ci-dessus, pour appeler/invoquer une fonction, écrivez le nom de la fonction, suivi d'une parenthèse ouvrante et d'une parenthèse fermante (sans aucun espace blanc). Les arguments requis doivent être fournis entre les parenthèses ouvrantes et fermantes (le cas échéant).

Pour illustrer ce concept, créons une fonction pour multiplier deux chiffres :

```javascript
//        functionName   param1 param2
function multiplyNumbers (num1, num2) {
    return num1 * num2; // tâche à effectuer.
}
```

C'est aussi simple que cela.

Ayant fait cela, appelons/invoquons la fonction.

```javascript
multiplyNumbers(2, 3) // 6
```

Remarquez que lors de la création de la fonction, nous avons déclaré deux paramètres : `num1` et `num2`. Lors de l'appel de la fonction, nous avons assigné des valeurs aux deux arguments : 1 et 2.

**Mot-clé return**

Les fonctions peuvent retourner des valeurs ou non.

Si une fonction contient une instruction `return`, comme la fonction `multiplyNumbers`, alors elle retournera une valeur si tout se passe bien. Si la fonction n'a pas d'instruction return, elle retournera `undefined`.

```javascript
function sayHi () {
    console.log("Hi");
}
```

Si nous invoquons `sayHi`, elle enregistrera le texte `Hi` dans la console et elle retournera également `undefined`.

Rappelez-vous que les fonctions sont comme des aides, lorsque vous envoyez une aide pour effectuer une tâche, vous pouvez exiger qu'elle vous donne un retour (le résultat de la tâche qu'elle a effectuée) ou vous pouvez ne pas avoir besoin de retour.

Si vous avez besoin de retour, ajoutez une instruction `return` sur le retour dont vous avez besoin. Sinon, n'ajoutez pas d'instruction `return` à la fonction.

Il y a encore beaucoup de choses à apprendre sur chaque type de données que nous avons mis en évidence dans cet article, alors prenez votre temps pour pratiquer ces bases et lorsque vous vous sentirez suffisamment à l'aise pour les utiliser, vous verrez le besoin de plonger plus profondément.

## Résumé

Les variables sont des "pointeurs" vers des valeurs. Lorsque vous mentionnez (utilisez) une variable n'importe où dans votre code, l'identifiant de la variable (nom) est remplacé par la valeur à laquelle il pointe. C'est comme appeler le nom de quelqu'un. Le nom ne répond pas, c'est la personne (valeur) derrière le nom que vous espérez obtenir comme réponse.

Pour la rétention, n'essayez pas de mémoriser toutes ces règles et conventions. N'hésitez pas à vous référer à cet article lors de la programmation et en peu de temps, vous serez habitué à toutes ces règles et vous n'aurez plus besoin de vous référer à un article pour nommer correctement vos variables.

Si vous devez avoir quelque chose en tête, rappelez-vous de commencer les variables par une lettre minuscule si la variable est composée de plusieurs mots, les mots suivants doivent commencer par des lettres majuscules. C'est-à-dire : `age`, `dateOfBirth`.

Pour créer une variable, utilisez le mot-clé `let`, `const`, ou `var`, suivi du nom de la variable. Si vous souhaitez initialiser la variable, alors sur la même ligne avant le point-virgule, entrez l'opérateur d'assignation et la valeur de la variable après celui-ci.

Par exemple : `let score;` ou `let score = 3;` (si vous souhaitez initialiser lors de la déclaration).

Si vous souhaitez utiliser une variable, mentionnez simplement son nom et la valeur sera utilisée lors de l'exécution de votre code.

```javascript
let a = 2;
let b = 3;
console.log(a + b) // 4
```

Cet article vous a également montré les différents types de données en JavaScript et comment les utiliser.

Cet article vous a-t-il aidé ? Continuons la conversation. N'hésitez pas à partager vos pensées ou questions sur Twitter (x) ou LinkedIn. Vous pouvez me trouver sur Twitter (x) [@asoluka\_tee](https://x.com/asoluka_tee) et [Tochukwu Austin Asoluka](https://www.linkedin.com/in/tochukwu-austin-asoluka-415326155/) sur LinkedIn.