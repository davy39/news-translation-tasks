---
title: Le Guide du Débutant en JavaScript
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2020-03-01T16:59:00.000Z'
originalURL: https://freecodecamp.org/news/the-complete-javascript-handbook-f26b2c71719c
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/cover-1.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Le Guide du Débutant en JavaScript
seo_desc: 'JavaScript is one of the most popular programming languages in the world.

  I believe it''s a great choice for your first programming language ever.

  We mainly use JavaScript to create


  websites


  web applications


  server-side applications using Node.js


  ...'
---

JavaScript est l'un des langages de programmation les plus populaires au monde.

Je crois que c'est un excellent choix pour votre premier langage de programmation.

Nous utilisons principalement JavaScript pour créer

* des sites web
  
* des applications web
  
* des applications côté serveur en utilisant Node.js
  

mais JavaScript ne se limite pas à ces choses, et il peut également être utilisé pour

* créer des applications mobiles en utilisant des outils comme React Native
  
* créer des programmes pour microcontrôleurs et l'internet des objets
  
* créer des applications pour montres intelligentes
  

Il peut essentiellement tout faire. Il est si populaire que tout ce qui est nouveau et qui apparaîtra aura une sorte d'intégration JavaScript à un moment donné.

JavaScript est un langage de programmation qui est :

* **de haut niveau** : il fournit des abstractions qui vous permettent d'ignorer les détails de la machine sur laquelle il s'exécute. Il gère la mémoire automatiquement avec un ramasse-miettes, afin que vous puissiez vous concentrer sur le code au lieu de gérer la mémoire comme d'autres langages comme C le nécessiteraient, et fournit de nombreuses constructions qui vous permettent de traiter des variables et des objets très puissants.
  
* **dynamique** : contrairement aux langages de programmation statiques, un langage dynamique exécute à l'exécution de nombreuses choses qu'un langage statique fait au moment de la compilation. Cela a des avantages et des inconvénients, et cela nous donne des fonctionnalités puissantes comme le typage dynamique, la liaison tardive, la réflexion, la programmation fonctionnelle, l'altération de l'objet à l'exécution, les fermetures et bien plus encore. Ne vous inquiétez pas si ces choses vous sont inconnues - vous les connaîtrez toutes à la fin du cours.
  
* **dynamiquement typé** : une variable n'impose pas de type. Vous pouvez réassigner n'importe quel type à une variable, par exemple, assigner un entier à une variable qui contient une chaîne de caractères.
  
* **faiblement typé** : contrairement au typage fort, les langages faiblement (ou faiblement) typés n'imposent pas le type d'un objet, permettant plus de flexibilité mais nous refusant la sécurité de type et la vérification de type (quelque chose que TypeScript - qui se construit sur JavaScript - fournit)
  
* **interprété** : il est communément connu comme un langage interprété, ce qui signifie qu'il n'a pas besoin d'une étape de compilation avant qu'un programme puisse s'exécuter, contrairement à C, Java ou Go par exemple. En pratique, les navigateurs compilent JavaScript avant de l'exécuter, pour des raisons de performance, mais cela est transparent pour vous - il n'y a pas d'étape supplémentaire impliquée.
  
* **multi-paradigme** : le langage n'impose aucun paradigme de programmation particulier, contrairement à Java par exemple, qui force l'utilisation de la programmation orientée objet, ou C qui force la programmation impérative. Vous pouvez écrire JavaScript en utilisant un paradigme orienté objet, en utilisant des prototypes et la nouvelle (à partir de ES6) syntaxe de classes. Vous pouvez écrire JavaScript dans un style de programmation fonctionnelle, avec ses fonctions de première classe, ou même dans un style impératif (comme C).
  

Au cas où vous vous poseriez la question, *JavaScript n'a rien à voir avec Java*, c'est un mauvais choix de nom mais nous devons vivre avec.

## Sommaire du guide

1. [Un peu d'histoire](#heading-un-peu-dhistoire)
  
2. [Juste JavaScript](#heading-juste-javascript)
  
3. [Une brève introduction à la syntaxe de JavaScript](#heading-une-breve-introduction-a-la-syntaxe-de-javascript)
  
4. [Points-virgules](#heading-points-virgules)
  
5. [Valeurs](#heading-valeurs)
  
6. [Variables](#heading-variables)
  
7. [Types](#heading-types)
  
8. [Expressions](#heading-expressions)
  
9. [Opérateurs](#heading-operateurs)
  
10. [Règles de priorité](#heading-regles-de-priorite)
  
11. [Opérateurs de comparaison](#heading-operateurs-de-comparaison)
  
12. [Conditionnelles](#heading-conditionnelles)
  
13. [Tableaux](#heading-tableaux)
  
14. [Chaînes de caractères](#heading-chaines-de-caracteres)
  
15. [Boucles](#heading-boucles)
  
16. [Fonctions](#heading-fonctions)
  
17. [Fonctions fléchées](#heading-fonctions-flechees)
  
18. [Objets](#heading-objets)
  
19. [Propriétés des objets](#heading-proprietes-des-objets)
  
20. [Méthodes des objets](#heading-methodes-des-objets)
  
21. [Classes](#heading-classes)
  
22. [Héritage](#heading-heritage)
  
23. [Programmation asynchrone et rappels](#heading-programmation-asynchrone-et-rappels)
  
24. [Promesses](#heading-promesses)
  
25. [Async et Await](#heading-async-et-await)
  
26. [Portée des variables](#heading-portee-des-variables)
  
27. [Conclusion](#heading-conclusion)
  

> Mise à jour : [Vous pouvez maintenant obtenir une version PDF et ePub de ce Guide du Débutant en JavaScript](https://flaviocopes.com/page/javascript-handbook/).

## Un peu d'histoire

Créé en 1995, JavaScript a parcouru un long chemin depuis ses modestes débuts.

Il a été le premier langage de script soutenu nativement par les navigateurs web, et grâce à cela, il a gagné un avantage compétitif sur tout autre langage et aujourd'hui, il est toujours le seul langage de script que nous pouvons utiliser pour construire des applications web.

D'autres langages existent, mais tous doivent compiler vers JavaScript - ou plus récemment vers WebAssembly, mais c'est une autre histoire.

Au début, JavaScript n'était pas aussi puissant qu'il l'est aujourd'hui, et il était principalement utilisé pour des animations fantaisistes et la merveille connue à l'époque sous le nom de *Dynamic HTML*.

Avec les besoins croissants que la plateforme web exigeait (et continue d'exiger), JavaScript *devait* évoluer également, pour répondre aux besoins de l'un des écosystèmes les plus largement utilisés au monde.

JavaScript est également désormais largement utilisé en dehors du navigateur. L'essor de Node.js ces dernières années a débloqué le développement backend, autrefois le domaine de Java, Ruby, Python, PHP, et d'autres langages côté serveur plus traditionnels.

JavaScript est désormais également le langage qui alimente les bases de données et bien d'autres applications, et il est même possible de développer des applications embarquées, des applications mobiles, des applications TV, et bien plus encore. Ce qui a commencé comme un petit langage à l'intérieur du navigateur est désormais le langage le plus populaire au monde.

## Juste JavaScript

Parfois, il est difficile de séparer JavaScript des fonctionnalités de l'environnement dans lequel il est utilisé.

Par exemple, la ligne `console.log()` que vous pouvez trouver dans de nombreux exemples de code n'est pas JavaScript. Au lieu de cela, elle fait partie de la vaste bibliothèque d'API fournies dans le navigateur.

De la même manière, sur le serveur, il peut être parfois difficile de séparer les fonctionnalités du langage JavaScript des API fournies par Node.js.

Une fonctionnalité particulière est-elle fournie par React ou Vue ? Ou est-ce du "JavaScript pur", ou "vanilla JavaScript" comme on l'appelle souvent ?

Dans ce livre, je parle de JavaScript, le langage.

Sans compliquer votre processus d'apprentissage avec des choses qui en sont extérieures, et fournies par des écosystèmes externes.

## Une brève introduction à la syntaxe de JavaScript

Dans cette petite introduction, je veux vous parler de 5 concepts :

* espace blanc
  
* sensibilité à la casse
  
* littéraux
  
* identifiants
  
* commentaires
  

### Espace blanc

JavaScript ne considère pas l'espace blanc comme significatif. Les espaces et les sauts de ligne peuvent être ajoutés de la manière que vous préférez, au moins *en théorie*.

En pratique, vous utiliserez très probablement un style bien défini et vous vous conformerez à ce que les gens utilisent couramment, et vous appliquerez cela en utilisant un linter ou un outil de style tel que *Prettier*.

Par exemple, j'utilise toujours 2 caractères d'espace pour chaque indentation.

#### Sensibilité à la casse

JavaScript est sensible à la casse. Une variable nommée `something` est différente de `Something`.

Il en va de même pour tout identifiant.

### Littéraux

Nous définissons un **littéral** comme une valeur écrite dans le code source, par exemple, un nombre, une chaîne de caractères, un booléen ou aussi des constructions plus avancées, comme les littéraux d'objets ou les littéraux de tableaux :

```js
5
'Test'
true
['a', 'b']
{color: 'red', shape: 'Rectangle'}
```

### Identifiants

Un **identifiant** est une séquence de caractères qui peut être utilisée pour identifier une variable, une fonction ou un objet. Il peut commencer par une lettre, le signe dollar `$` ou un trait de soulignement `_`, et il peut contenir des chiffres. En utilisant Unicode, une lettre peut être n'importe quel caractère autorisé, par exemple, un emoji ?.

```js
Test
test
TEST
_test
Test1
$test
```

Le signe dollar est couramment utilisé pour référencer les éléments du DOM.

Certains noms sont réservés pour l'usage interne de JavaScript, et nous ne pouvons pas les utiliser comme identifiants.

### Commentaires

Les commentaires sont l'une des parties les plus importantes de tout programme, dans n'importe quel langage de programmation. Ils sont importants car ils nous permettent d'annoter le code et d'ajouter des informations importantes qui ne seraient autrement pas disponibles pour les autres personnes (ou nous-mêmes) lisant le code.

En JavaScript, nous pouvons écrire un commentaire sur une seule ligne en utilisant `//`. Tout ce qui suit `//` n'est pas considéré comme du code par l'interpréteur JavaScript.

Comme ceci :

```js
// un commentaire
true //un autre commentaire
```

Un autre type de commentaire est un commentaire multi-lignes. Il commence par `/*` et se termine par `*/`.

Tout ce qui se trouve entre les deux n'est pas considéré comme du code :

```js
/* une sorte
de 
commentaire 

*/
```

## Points-virgules

Chaque ligne dans un programme JavaScript est optionnellement terminée en utilisant des points-virgules.

J'ai dit optionnellement, car l'interpréteur JavaScript est suffisamment intelligent pour introduire des points-virgules pour vous.

Dans la plupart des cas, vous pouvez omettre complètement les points-virgules de vos programmes sans même y penser.

Ce fait est très controversé. Certains développeurs utiliseront toujours des points-virgules, d'autres ne les utiliseront jamais, et vous trouverez toujours du code qui utilise des points-virgules et du code qui n'en utilise pas.

Ma préférence personnelle est d'éviter les points-virgules, donc mes exemples dans le livre n'en incluront pas.

## Valeurs

Une chaîne de caractères `hello` est une **valeur**. Un nombre comme `12` est une **valeur**.

`hello` et `12` sont des valeurs. `string` et `number` sont les **types** de ces valeurs.

Le **type** est le genre de valeur, sa catégorie. Nous avons de nombreux types différents en JavaScript, et nous en parlerons en détail plus tard. Chaque type a ses propres caractéristiques.

Lorsque nous devons avoir une référence à une valeur, nous l'assignons à une **variable**. La variable peut avoir un nom, et la valeur est ce qui est stocké dans une variable, afin que nous puissions accéder plus tard à cette valeur par le nom de la variable.

## Variables

Une variable est une valeur assignée à un identifiant, afin que vous puissiez la référencer et l'utiliser plus tard dans le programme.

C'est parce que JavaScript est **faiblement typé**, un concept que vous entendrez fréquemment.

Une variable doit être déclarée avant de pouvoir l'utiliser.

Nous avons 2 principales façons de déclarer des variables. La première est d'utiliser `const` :

```js
const a = 0
```

La deuxième façon est d'utiliser `let` :

```js
let a = 0
```

Quelle est la différence ?

`const` définit une référence constante à une valeur. Cela signifie que la référence ne peut pas être changée. Vous ne pouvez pas réassigner une nouvelle valeur à celle-ci.

En utilisant `let`, vous pouvez assigner une nouvelle valeur à celle-ci.

Par exemple, vous ne pouvez pas faire ceci :

```js
const a = 0
a = 1
```

Parce que vous obtiendrez une erreur : `TypeError: Assignment to constant variable.`.

D'autre part, vous pouvez le faire en utilisant `let` :

```js
let a = 0
a = 1
```

`const` ne signifie pas "constante" de la manière dont certains autres langages comme C le signifient. En particulier, cela ne signifie pas que la valeur ne peut pas changer - cela signifie qu'elle ne peut pas être réassignée. Si la variable pointe vers un objet ou un tableau (nous verrons plus sur les objets et les tableaux plus tard), le contenu de l'objet ou du tableau peut changer librement.

Les variables `const` doivent être initialisées au moment de la déclaration :

```js
const a = 0
```

mais les valeurs `let` peuvent être initialisées plus tard :

```js
let a
a = 0
```

Vous pouvez déclarer plusieurs variables à la fois dans la même instruction :

```js
const a = 1, b = 2
let c = 1, d = 2
```

Mais vous ne pouvez pas redéclarer la même variable plus d'une fois :

```js
let a = 1
let a = 2
```

ou vous obtiendrez une erreur de "déclaration en double".

Mon conseil est d'utiliser toujours `const` et d'utiliser `let` uniquement lorsque vous savez que vous devrez réassigner une valeur à cette variable. Pourquoi ? Parce que moins notre code a de pouvoir, mieux c'est. Si nous savons qu'une valeur ne peut pas être réassignée, c'est une source de bugs en moins.

Maintenant que nous avons vu comment travailler avec `const` et `let`, je veux mentionner `var`.

Jusqu'en 2015, `var` était la seule façon dont nous pouvions déclarer une variable en JavaScript. Aujourd'hui, une base de code moderne utilisera très probablement uniquement `const` et `let`. Il existe quelques différences fondamentales que je détaille [dans cet article](https://flaviocopes.com/javascript-difference-let-var/) mais si vous débutez, vous ne vous en souciez peut-être pas. Utilisez simplement `const` et `let`.

## Types

Les variables en JavaScript n'ont aucun type attaché.

Elles sont *non typées*.

Une fois que vous avez assigné une valeur avec un certain type à une variable, vous pouvez plus tard réassigner la variable pour héberger une valeur de n'importe quel autre type sans aucun problème.

En JavaScript, nous avons 2 principaux types de types : les **types primitifs** et les **types objets**.

### Types primitifs

Les types primitifs sont

* les nombres
  
* les chaînes de caractères
  
* les booléens
  
* les symboles
  

Et deux types spéciaux : `null` et `undefined`.

### Types objets

Toute valeur qui n'est pas d'un type primitif (une chaîne de caractères, un nombre, un booléen, null ou undefined) est un **objet**.

Les types objets ont des **propriétés** et ont également des **méthodes** qui peuvent agir sur ces propriétés.

Nous en parlerons plus tard.

## Expressions

Une expression est une unité unique de code JavaScript que le moteur JavaScript peut évaluer et retourner une valeur.

Les expressions peuvent varier en complexité.

Nous commençons par les plus simples, appelées expressions primaires :

```js
2
0.02
'something'
true
false
this //le scope actuel
undefined
i //où i est une variable ou une constante
```

Les expressions arithmétiques sont des expressions qui prennent une variable et un opérateur (plus sur les opérateurs bientôt), et résultent en un nombre :

```js
1 / 2
i++
i -= 2
i * 2
```

Les expressions de chaîne sont des expressions qui résultent en une chaîne :

```js
'A ' + 'string'
```

Les expressions logiques utilisent des opérateurs logiques et se résolvent en une valeur booléenne :

```js
a && b
a || b
!a
```

Des expressions plus avancées impliquent des objets, des fonctions et des tableaux, et je les introduirai plus tard.

## Opérateurs

Les opérateurs vous permettent de prendre deux expressions simples et de les combiner pour former une expression plus complexe.

Nous pouvons classer les opérateurs en fonction des opérandes avec lesquels ils fonctionnent. Certains opérateurs fonctionnent avec 1 opérande. La plupart fonctionnent avec 2 opérandes. Un seul opérateur fonctionne avec 3 opérandes.

Dans cette première introduction aux opérateurs, nous introduirons les opérateurs que vous connaissez probablement déjà : les opérateurs avec 2 opérandes.

J'ai déjà introduit l'un d'eux en parlant des variables : l'opérateur d'assignation `=`. Vous utilisez `=` pour assigner une valeur à une variable :

```js
let b = 2
```

Introduisons maintenant un autre ensemble d'opérateurs binaires que vous connaissez déjà des mathématiques de base.

### L'opérateur d'addition (+)

```js
const three = 1 + 2
const four = three + 1
```

L'opérateur `+` effectue également la concaténation de chaînes si vous utilisez des chaînes, alors faites attention :

```js
const three = 1 + 2
three + 1 // 4
'three' + 1 // three1
```

### L'opérateur de soustraction (-)

```js
const two = 4 - 2
```

### L'opérateur de division (/)

Retourne le quotient du premier opérateur et du second :

```js
const result = 20 / 5 //result === 4
const result = 20 / 7 //result === 2.857142857142857
```

Si vous divisez par zéro, JavaScript ne lève aucune erreur mais retourne la valeur `Infinity` (ou `-Infinity` si la valeur est négative).

```js
1 / 0 //Infinity
-1 / 0 //-Infinity
```

### L'opérateur de reste (%)

Le reste est un calcul très utile dans de nombreux cas d'utilisation :

```js
const result = 20 % 5 //result === 0
const result = 20 % 7 //result === 6
```

Un reste par zéro est toujours `NaN`, une valeur spéciale qui signifie "Not a Number" :

```js
1 % 0 //NaN
-1 % 0 //NaN
```

### L'opérateur de multiplication (\*)

Multiplie deux nombres

```js
1 * 2 //2
-1 * 2 //-2
```

### L'opérateur d'exponentiation (\*\*)

Élève le premier opérande à la puissance du second opérande

```js
1 ** 2 //1
2 ** 1 //2
2 ** 2 //4
2 ** 8 //256
8 ** 2 //64
```

## Règles de priorité

Chaque instruction complexe avec plusieurs opérateurs sur la même ligne introduira des problèmes de priorité.

Prenons cet exemple :

```js
let a = 1 * 2 + 5 / 2 % 2
```

Le résultat est 2.5, mais pourquoi ?

Quelles opérations sont exécutées en premier, et lesquelles doivent attendre ?

Certaines opérations ont plus de priorité que d'autres. Les règles de priorité sont listées dans ce tableau :

| Opérateur | Description |
| --- | --- |
| `*` `/` `%` | multiplication/division |
| `+` `-` | addition/soustraction |
| `=` | assignation |

Les opérations au même niveau (comme `+` et `-`) sont exécutées dans l'ordre où elles sont trouvées, de gauche à droite.

En suivant ces règles, l'opération ci-dessus peut être résolue de cette manière :

```js
let a = 1 * 2 + 5 / 2 % 2
let a = 2 + 5 / 2 % 2
let a = 2 + 2.5 % 2
let a = 2 + 0.5
let a = 2.5
```

## Opérateurs de comparaison

Après les opérateurs d'assignation et mathématiques, le troisième ensemble d'opérateurs que je veux introduire est les opérateurs conditionnels.

Vous pouvez utiliser les opérateurs suivants pour comparer deux nombres, ou deux chaînes de caractères.

Les opérateurs de comparaison retournent toujours un booléen, une valeur qui est `true` ou `false`).

Ce sont des **opérateurs de comparaison d'inégalité** :

* `<` signifie "inférieur à"
  
* `<=` signifie "inférieur ou égal à"
  
* `>` signifie "supérieur à"
  
* `>=` signifie "supérieur ou égal à"
  

Exemple :

```js
let a = 2
a >= 1 //true
```

En plus de ceux-ci, nous avons 4 **opérateurs d'égalité**. Ils acceptent deux valeurs, et retournent un booléen :

* `===` vérifie l'égalité
  
* `!==` vérifie l'inégalité
  

Notez que nous avons également `==` et `!=` en JavaScript, mais je vous suggère fortement d'utiliser uniquement `===` et `!==` car ils peuvent prévenir certains problèmes subtils.

## Conditionnelles

Avec les opérateurs de comparaison en place, nous pouvons parler des conditionnelles.

Une instruction `if` est utilisée pour faire prendre un chemin au programme, ou un autre, selon le résultat de l'évaluation d'une expression.

Voici l'exemple le plus simple, qui s'exécute toujours :

```js
if (true) {
  //faire quelque chose
}
```

au contraire, ceci ne s'exécute jamais :

```js
if (false) {
  //faire quelque chose (? jamais ?)
}
```

La conditionnelle vérifie l'expression que vous lui passez pour une valeur vraie ou fausse. Si vous passez un nombre, il s'évalue toujours à vrai sauf s'il est 0. Si vous passez une chaîne de caractères, elle s'évalue toujours à vrai sauf si elle est une chaîne vide. Ce sont des règles générales de conversion de types en booléen.

Avez-vous remarqué les accolades ? Cela s'appelle un **bloc**, et il est utilisé pour regrouper une liste d'instructions différentes.

Un bloc peut être placé partout où vous pouvez avoir une seule instruction. Et si vous avez une seule instruction à exécuter après les conditionnelles, vous pouvez omettre le bloc, et simplement écrire l'instruction :

```js
if (true) doSomething()
```

Mais j'aime toujours utiliser les accolades pour être plus clair.

Vous pouvez fournir une deuxième partie à l'instruction `if` : `else`.

Vous attachez une instruction qui sera exécutée si la condition `if` est fausse :

```js
if (true) {
  //faire quelque chose
} else {
  //faire autre chose
}
```

Puisque `else` accepte une instruction, vous pouvez imbriquer une autre instruction if/else à l'intérieur :

```js
if (a === true) {
  //faire quelque chose
} else if (b === true) {
  //faire autre chose
} else {
  //solution de repli
}
```

## Tableaux

Un tableau est une collection d'éléments.

Les tableaux en JavaScript ne sont pas un *type* à part entière.

Les tableaux sont des **objets**.

Nous pouvons initialiser un tableau vide de ces 2 manières différentes :

```js
const a = []
const a = Array()
```

La première utilise la **syntaxe littérale de tableau**. La seconde utilise la fonction intégrée Array.

Vous pouvez pré-remplir le tableau en utilisant cette syntaxe :

```js
const a = [1, 2, 3]
const a = Array.of(1, 2, 3)
```

Un tableau peut contenir n'importe quelle valeur, même des valeurs de types différents :

```js
const a = [1, 'Flavio', ['a', 'b']]
```

Puisque nous pouvons ajouter un tableau dans un tableau, nous pouvons créer des tableaux multi-dimensionnels, qui ont des applications très utiles (par exemple, une matrice) :

```js
const matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

matrix[0][0] //1
matrix[2][0] //7
```

Vous pouvez accéder à n'importe quel élément du tableau en référençant son index, qui commence à zéro :

```js
a[0] //1
a[1] //2
a[2] //3
```

Vous pouvez initialiser un nouveau tableau avec un ensemble de valeurs en utilisant cette syntaxe, qui initialise d'abord un tableau de 12 éléments, et remplit chaque élément avec le nombre `0` :

```js
Array(12).fill(0)
```

Vous pouvez obtenir le nombre d'éléments dans le tableau en vérifiant sa propriété `length` :

```js
const a = [1, 2, 3]
a.length //3
```

Notez que vous pouvez définir la longueur du tableau. Si vous attribuez un nombre plus grand que la capacité actuelle du tableau, rien ne se passe. Si vous attribuez un nombre plus petit, le tableau est coupé à cette position :

```js
const a = [1, 2, 3]
a //[ 1, 2, 3 ]
a.length = 2
a //[ 1, 2 ]
```

### Comment ajouter un élément à un tableau

Nous pouvons ajouter un élément à la fin d'un tableau en utilisant la méthode `push()` :

```js
a.push(4)
```

Nous pouvons ajouter un élément au début d'un tableau en utilisant la méthode `unshift()` :

```js
a.unshift(0)
a.unshift(-2, -1)
```

### Comment supprimer un élément d'un tableau

Nous pouvons supprimer un élément de la fin d'un tableau en utilisant la méthode `pop()` :

```js
a.pop()
```

Nous pouvons supprimer un élément du début d'un tableau en utilisant la méthode `shift()` :

```js
a.shift()
```

### Comment joindre deux ou plusieurs tableaux

Vous pouvez joindre plusieurs tableaux en utilisant `concat()` :

```js
const a = [1, 2]
const b = [3, 4]
const c = a.concat(b) //[1,2,3,4]
a //[1,2]
b //[3,4]
```

Vous pouvez également utiliser l'opérateur **spread** (`...`) de cette manière :

```js
const a = [1, 2]
const b = [3, 4]
const c = [...a, ...b]
c //[1,2,3,4]
```

### Comment trouver un élément spécifique dans le tableau

Vous pouvez utiliser la méthode `find()` d'un tableau :

```js
a.find((element, index, array) => {
  //retourne vrai ou faux
})
```

Retourne le premier élément qui retourne vrai, et retourne `undefined` si l'élément n'est pas trouvé.

Une syntaxe couramment utilisée est :

```js
a.find(x => x.id === my_id)
```

La ligne ci-dessus retournera le premier élément du tableau qui a `id === my_id`.

`findIndex()` fonctionne de manière similaire à `find()`, mais retourne l'index du premier élément qui retourne vrai, et si non trouvé, il retourne `undefined` :

```js
a.findIndex((element, index, array) => {
  //retourne vrai ou faux
})
```

Une autre méthode est `includes()` :

```js
a.includes(value)
```

Retourne vrai si `a` contient `value`.

```js
a.includes(value, i)
```

Retourne vrai si `a` contient `value` après la position `i`.

## Chaînes de caractères

Une chaîne de caractères est une séquence de caractères.

Elle peut également être définie comme un littéral de chaîne, qui est enfermé dans des guillemets simples ou doubles :

```js
'A string'
"Another string"
```

Je préfère personnellement les guillemets simples tout le temps, et j'utilise les guillemets doubles uniquement en HTML pour définir les attributs.

Vous attribuez une valeur de chaîne à une variable comme ceci :

```js
const name = 'Flavio'
```

Vous pouvez déterminer la longueur d'une chaîne en utilisant la propriété `length` :

```js
'Flavio'.length //6
const name = 'Flavio'
name.length //6
```

Ceci est une chaîne vide : `''`. Sa propriété length est 0 :

```js
''.length //0
```

Deux chaînes peuvent être jointes en utilisant l'opérateur `+` :

```js
"A " + "string"
```

Vous pouvez utiliser l'opérateur `+` pour *interpoler* des variables :

```js
const name = 'Flavio'
"My name is " + name //My name is Flavio
```

Une autre façon de définir des chaînes est d'utiliser des littéraux de gabarit, définis à l'intérieur de backticks. Ils sont particulièrement utiles pour rendre les chaînes multilignes beaucoup plus simples. Avec des guillemets simples ou doubles, vous ne pouvez pas définir facilement une chaîne multiligne - vous devriez utiliser des caractères d'échappement.

Une fois qu'un littéral de gabarit est ouvert avec le backtick, vous appuyez simplement sur entrée pour créer une nouvelle ligne, sans caractères spéciaux, et il est rendu tel quel :

```js
const string = `Hey
this

string
is awesome!`
```

Les littéraux de gabarit sont également géniaux car ils fournissent un moyen facile d'interpoler des variables et des expressions dans des chaînes.

Vous le faites en utilisant la syntaxe `${...}` :

```js
const var = 'test'
const string = `something ${var}` 
//something test
```

À l'intérieur des `${}` vous pouvez ajouter n'importe quoi, même des expressions :

```js
const string = `something ${1 + 2 + 3}`
const string2 = `something 
  ${foo() ? 'x' : 'y'}`
```

## Boucles

Les boucles sont l'une des principales structures de contrôle de JavaScript.

Avec une boucle, nous pouvons automatiser et répéter un bloc de code autant de fois que nous le souhaitons, même indéfiniment.

JavaScript fournit de nombreuses façons d'itérer à travers des boucles.

Je veux me concentrer sur 3 façons :

* les boucles while
  
* les boucles for
  
* les boucles for..of
  

### `while`

La boucle while est la structure de boucle la plus simple que JavaScript nous fournit.

Nous ajoutons une condition après le mot-clé `while`, et nous fournissons un bloc qui est exécuté jusqu'à ce que la condition s'évalue à `true`.

Exemple :

```js
const list = ['a', 'b', 'c']
let i = 0
while (i < list.length) {
  console.log(list[i]) //valeur
  console.log(i) //index
  i = i + 1
}
```

Vous pouvez interrompre une boucle `while` en utilisant le mot-clé `break`, comme ceci :

```js
while (true) {
  if (somethingIsTrue) break
}
```

et si vous décidez qu'au milieu d'une boucle vous voulez sauter l'itération actuelle, vous pouvez sauter à l'itération suivante en utilisant `continue` :

```js
while (true) {
  if (somethingIsTrue) continue

  //faire autre chose
}
```

Très similaire à `while`, nous avons les boucles `do..while`. C'est essentiellement la même chose que `while`, sauf que la condition est évaluée *après* que le bloc de code est exécuté.

Cela signifie que le bloc est toujours exécuté *au moins une fois*.

Exemple :

```js
const list = ['a', 'b', 'c']
let i = 0
do {
  console.log(list[i]) //valeur
  console.log(i) //index
  i = i + 1
} while (i < list.length)
```

### `for`

La deuxième structure de boucle très importante en JavaScript est la **boucle for**.

Nous utilisons le mot-clé `for` et nous passons un ensemble de 3 instructions : l'initialisation, la condition et la partie d'incrémentation.

Exemple :

```js
const list = ['a', 'b', 'c']

for (let i = 0; i < list.length; i++) {
  console.log(list[i]) //valeur
  console.log(i) //index
}
```

Tout comme avec les boucles `while`, vous pouvez interrompre une boucle `for` en utilisant `break` et vous pouvez avancer rapidement à l'itération suivante d'une boucle `for` en utilisant `continue`.

### `for...of`

Cette boucle est relativement récente (introduite en 2015) et c'est une version simplifiée de la boucle `for` :

```js
const list = ['a', 'b', 'c']

for (const value of list) {
  console.log(value) //valeur
}
```

## Fonctions

Dans tout programme JavaScript modérément complexe, tout se passe à l'intérieur des fonctions.

Les fonctions sont une partie essentielle de JavaScript.

Qu'est-ce qu'une fonction ?

Une fonction est un bloc de code, auto-contenu.

Voici une **déclaration de fonction** :

```js
function getData() {
  // faire quelque chose
}
```

Une fonction peut être exécutée à tout moment en l'invoquant, comme ceci :

```js
getData()
```

Une fonction peut avoir un ou plusieurs arguments :

```js
function getData() {
  //faire quelque chose
}

function getData(color) {
  //faire quelque chose
}

function getData(color, age) {
  //faire quelque chose
}
```

Lorsque nous pouvons passer un argument, nous invoquons la fonction en passant des paramètres :

```js
function getData(color, age) {
  //faire quelque chose
}

getData('green', 24)
getData('black')
```

Notez que dans la deuxième invocation, j'ai passé le paramètre de chaîne `black` comme argument `color`, mais pas d'`age`. Dans ce cas, `age` à l'intérieur de la fonction est `undefined`.

Nous pouvons vérifier si une valeur n'est pas indéfinie en utilisant cette conditionnelle :

```js
function getData(color, age) {
  //faire quelque chose
  if (typeof age !== 'undefined') {
    //...
  }
}
```

`typeof` est un opérateur unaire qui nous permet de vérifier le type d'une variable.

Vous pouvez également vérifier de cette manière :

```js
function getData(color, age) {
  //faire quelque chose
  if (age) {
    //...
  }
}
```

Bien que la conditionnelle sera également vraie si `age` est `null`, `0` ou une chaîne vide.

Vous pouvez avoir des valeurs par défaut pour les paramètres, au cas où ils ne sont pas passés :

```js
function getData(color = 'black', age = 25) {
  //faire quelque chose
}
```

Vous pouvez passer n'importe quelle valeur comme paramètre : des nombres, des chaînes, des booléens, des tableaux, des objets, et même des fonctions.

Une fonction a une valeur de retour. Par défaut, une fonction retourne `undefined`, sauf si vous ajoutez un mot-clé `return` avec une valeur :

```js
function getData() {
  // faire quelque chose
  return 'hi!'
}
```

Nous pouvons assigner cette valeur de retour à une variable lorsque nous invoquons la fonction :

```js
function getData() {
  // faire quelque chose
  return 'hi!'
}

let result = getData()
```

`result` contient maintenant une chaîne avec la valeur `hi!`.

Vous ne pouvez retourner qu'une seule valeur.

Pour retourner plusieurs valeurs, vous pouvez retourner un objet, ou un tableau, comme ceci :

```js
function getData() {
  return ['Flavio', 37]
}

let [name, age] = getData()
```

Les fonctions peuvent être définies à l'intérieur d'autres fonctions :

```js
const getData = () => {
  const dosomething = () => {}
  dosomething()
  return 'test'
}
```

La fonction imbriquée ne peut pas être appelée depuis l'extérieur de la fonction englobante.

Vous pouvez également retourner une fonction depuis une fonction.

## Fonctions fléchées

Les fonctions fléchées sont une introduction récente à JavaScript.

Elles sont très souvent utilisées à la place des fonctions "régulières", celles que j'ai décrites dans le chapitre précédent. Vous trouverez les deux formes utilisées partout.

Visuellement, elles vous permettent d'écrire des fonctions avec une syntaxe plus courte, de :

```js
function getData() {
  //...
}
```

à

```js
() => {
  //...
}
```

Mais... remarquez que nous n'avons pas de nom ici.

Les fonctions fléchées sont anonymes. Nous devons les assigner à une variable.

Nous pouvons assigner une fonction régulière à une variable, comme ceci :

```js
let getData = function getData() {
  //...
}
```

Lorsque nous le faisons, nous pouvons supprimer le nom de la fonction :

```js
let getData = function() {
  //...
}
```

et invoquer la fonction en utilisant le nom de la variable :

```js
let getData = function() {
  //...
}
getData()
```

C'est la même chose que nous faisons avec les fonctions fléchées :

```js
let getData = () => {
  //...
}
getData()
```

Si le corps de la fonction contient une seule instruction, vous pouvez omettre les parenthèses et écrire tout sur une seule ligne :

```js
const getData = () => console.log('hi!')
```

Les paramètres sont passés dans les parenthèses :

```js
const getData = (param1, param2) => 
  console.log(param1, param2)
```

Si vous avez un (et seulement un) paramètre, vous pourriez omettre les parenthèses complètement :

```js
const getData = param => console.log(param)
```

Les fonctions fléchées vous permettent d'avoir un retour implicite - les valeurs sont retournées sans avoir à utiliser le mot-clé `return`.

Cela fonctionne lorsqu'il y a une instruction sur une seule ligne dans le corps de la fonction :

```js
const getData = () => 'test'

getData() //'test'
```

Comme avec les fonctions régulières, nous pouvons avoir des valeurs par défaut pour les paramètres au cas où ils ne sont pas passés :

```js
const getData = (color = 'black', 
                 age = 2) => {
  //faire quelque chose
}
```

Et comme les fonctions régulières, nous ne pouvons retourner qu'une seule valeur.

Les fonctions fléchées peuvent également contenir d'autres fonctions fléchées, ou même des fonctions régulières.

Les deux types de fonctions sont très similaires, donc vous pourriez vous demander pourquoi les fonctions fléchées ont été introduites. La grande différence avec les fonctions régulières est lorsqu'elles sont utilisées comme méthodes d'objet. C'est quelque chose que nous allons bientôt examiner.

## Objets

Toute valeur qui n'est pas d'un type primitif (une chaîne de caractères, un nombre, un booléen, un symbole, null, ou undefined) est un **objet**.

Voici comment nous définissons un objet :

```js
const car = {

}
```

C'est la syntaxe **littérale d'objet**, qui est l'une des plus belles choses en JavaScript.

Vous pouvez également utiliser la syntaxe `new Object` :

```js
const car = new Object()
```

Une autre syntaxe est d'utiliser `Object.create()` :

```js
const car = Object.create()
```

Vous pouvez également initialiser un objet en utilisant le mot-clé `new` avant une fonction avec une lettre majuscule. Cette fonction sert de constructeur pour cet objet. Là, nous pouvons initialiser les arguments que nous recevons comme paramètres, pour configurer l'état initial de l'objet :

```js
function Car(brand, model) {
  this.brand = brand
  this.model = model
}
```

Nous initialisons un nouvel objet en utilisant :

```js
const myCar = new Car('Ford', 'Fiesta')
myCar.brand //'Ford'
myCar.model //'Fiesta'
```

Les objets sont **toujours passés par référence**.

Si vous attribuez une variable la même valeur qu'une autre, si c'est un type primitif comme un nombre ou une chaîne, ils sont passés par valeur :

Prenez cet exemple :

```js
let age = 36
let myAge = age
myAge = 37
age //36
```

```js
const car = {
  color: 'blue'
}
const anotherCar = car
anotherCar.color = 'yellow'
car.color //'yellow'
```

Même les tableaux ou les fonctions sont, sous le capot, des objets, donc il est très important de comprendre comment ils fonctionnent.

## Propriétés des objets

Les objets ont des **propriétés**, qui sont composées d'une étiquette associée à une valeur.

La valeur d'une propriété peut être de n'importe quel type, ce qui signifie qu'elle peut être un tableau, une fonction, et elle peut même être un objet, car les objets peuvent imbriquer d'autres objets.

C'est la syntaxe littérale d'objet que nous avons vue dans le chapitre précédent :

```js
const car = {

}
```

Nous pouvons définir une propriété `color` de cette manière :

```js
const car = {
  color: 'blue'
}
```

Ici nous avons un objet `car` avec une propriété nommée `color`, avec la valeur `blue`.

Les étiquettes peuvent être n'importe quelle chaîne de caractères, mais attention aux caractères spéciaux - si je voulais inclure un caractère non valide comme nom de variable dans le nom de la propriété, j'aurais dû utiliser des guillemets autour :

```js
const car = {
  color: 'blue',
  'the color': 'blue'
}
```

Les caractères non valides pour les noms de variables incluent les espaces, les tirets et autres caractères spéciaux.

Comme vous pouvez le voir, lorsque nous avons plusieurs propriétés, nous séparons chaque propriété avec une virgule.

Nous pouvons récupérer la valeur d'une propriété en utilisant 2 syntaxes différentes.

La première est la **notation par point** :

```js
car.color //'blue'
```

La seconde (qui est la seule que nous pouvons utiliser pour les propriétés avec des noms invalides), est d'utiliser des crochets :

```js
car['the color'] //'blue'
```

Si vous accédez à une propriété inexistante, vous obtiendrez la valeur `undefined` :

```js
car.brand //undefined
```

Comme mentionné précédemment, les objets peuvent avoir des objets imbriqués comme propriétés :

```js
const car = {
  brand: {
    name: 'Ford'
  },
  color: 'blue'
}
```

Dans cet exemple, vous pouvez accéder au nom de la marque en utilisant

```js
car.brand.name
```

ou

```js
car['brand']['name']
```

Vous pouvez définir la valeur d'une propriété lorsque vous définissez l'objet.

Mais vous pouvez toujours la mettre à jour plus tard :

```js
const car = {
  color: 'blue'
}

car.color = 'yellow'
car['color'] = 'red'
```

Et vous pouvez également ajouter de nouvelles propriétés à un objet :

```js
car.model = 'Fiesta'

car.model //'Fiesta'
```

Étant donné l'objet

```js
const car = {
  color: 'blue',
  brand: 'Ford'
}
```

vous pouvez supprimer une propriété de cet objet en utilisant

```js
delete car.brand
```

## Méthodes des objets

J'ai parlé des fonctions dans un chapitre précédent.

Les fonctions peuvent être assignées à une propriété de fonction, et dans ce cas, elles sont appelées **méthodes**.

Dans cet exemple, la propriété `start` a une fonction assignée, et nous pouvons l'invoquer en utilisant la syntaxe de point que nous avons utilisée pour les propriétés, avec les parenthèses à la fin :

```js
const car = {
  brand: 'Ford',
  model: 'Fiesta',
  start: function() {
    console.log('Started')
  }
}

car.start()
```

À l'intérieur d'une méthode définie en utilisant une syntaxe `function() {}` nous avons accès à l'instance de l'objet en référençant `this`.

Dans l'exemple suivant, nous avons accès aux valeurs des propriétés `brand` et `model` en utilisant `this.brand` et `this.model` :

```js
const car = {
  brand: 'Ford',
  model: 'Fiesta',
  start: function() {
    console.log(`Started 
      ${this.brand} ${this.model}`)
  }
}

car.start()
```

Il est important de noter cette distinction entre les fonctions régulières et les fonctions fléchées - nous n'avons pas accès à `this` si nous utilisons une fonction fléchée :

```js
const car = {
  brand: 'Ford',
  model: 'Fiesta',
  start: () => {
    console.log(`Started 
      ${this.brand} ${this.model}`) //ne va pas fonctionner
  }
}

car.start()
```

C'est parce que **les fonctions fléchées ne sont pas liées à l'objet**.

C'est la raison pour laquelle les fonctions régulières sont souvent utilisées comme méthodes d'objet.

Les méthodes peuvent accepter des paramètres, comme les fonctions régulières :

```js
const car = {
  brand: 'Ford',
  model: 'Fiesta',
  goTo: function(destination) {
    console.log(`Going to ${destination}`)
  }
}

car.goTo('Rome')
```

## Classes

Nous avons parlé des objets, qui sont l'une des parties les plus intéressantes de JavaScript.

Dans ce chapitre, nous allons monter d'un niveau en introduisant les classes.

Qu'est-ce que les classes ? Ce sont un moyen de définir un modèle commun pour plusieurs objets.

Prenons un objet personne :

```js
const person = {
  name: 'Flavio'
}
```

Nous pouvons créer une classe nommée `Person` (notez la majuscule `P`, une convention lors de l'utilisation des classes), qui a une propriété `name` :

```js
class Person {
  name
}
```

Maintenant, à partir de cette classe, nous initialisons un objet `flavio` comme ceci :

```js
const flavio = new Person()
```

`flavio` est appelé une *instance* de la classe Person.

Nous pouvons définir la valeur de la propriété `name` :

```js
flavio.name = 'Flavio'
```

et nous pouvons y accéder en utilisant

```js
flavio.name
```

comme nous le faisons pour les propriétés des objets.

Les classes peuvent contenir des propriétés, comme `name`, et des méthodes.

Les méthodes sont définies de cette manière :

```js
class Person {
  hello() {
    return 'Hello, I am Flavio'
  }
}
```

et nous pouvons invoquer des méthodes sur une instance de la classe :

```js
class Person {
  hello() {
    return 'Hello, I am Flavio'
  }
}
const flavio = new Person()
flavio.hello()
```

Il existe une méthode spéciale appelée `constructor()` que nous pouvons utiliser pour initialiser les propriétés de la classe lorsque nous créons une nouvelle instance d'objet.

Cela fonctionne comme ceci :

```js
class Person {
  constructor(name) {
    this.name = name
  }

  hello() {
    return 'Hello, I am ' + this.name + '.'
  }
}
```

Remarquez comment nous utilisons `this` pour accéder à l'instance de l'objet.

Maintenant, nous pouvons instancier un nouvel objet à partir de la classe, passer une chaîne, et lorsque nous appelons `hello`, nous obtiendrons un message personnalisé :

```js
const flavio = new Person('flavio')
flavio.hello() //'Hello, I am flavio.'
```

Lorsque l'objet est initialisé, la méthode `constructor` est appelée avec tous les paramètres passés.

Normalement, les méthodes sont définies sur l'instance de l'objet, et non sur la classe.

Vous pouvez définir une méthode comme `static` pour permettre son exécution sur la classe au lieu de l'instance :

```js
class Person {
  static genericHello() {
    return 'Hello'
  }
}

Person.genericHello() //Hello
```

C'est très utile, parfois.

## Héritage

Une classe peut **étendre** une autre classe, et les objets initialisés en utilisant cette classe héritent de toutes les méthodes des deux classes.

Supposons que nous avons une classe `Person` :

```js
class Person {
  hello() {
    return 'Hello, I am a Person'
  }
}
```

Nous pouvons définir une nouvelle classe, `Programmer`, qui étend `Person` :

```js
class Programmer extends Person {

}
```

Maintenant, si nous instancions un nouvel objet avec la classe `Programmer`, il a accès à la méthode `hello()` :

```js
const flavio = new Programmer()
flavio.hello() //'Hello, I am a Person'
```

À l'intérieur d'une classe enfant, vous pouvez référencer la classe parente en appelant `super()` :

```js
class Programmer extends Person {
  hello() {
    return super.hello() + 
      '. I am also a programmer.'
  }
}

const flavio = new Programmer()
flavio.hello()
```

Le programme ci-dessus imprime *Hello, I am a Person. I am also a programmer.*

## Programmation asynchrone et rappels

La plupart du temps, le code JavaScript est exécuté de manière synchrone.

Cela signifie qu'une ligne de code est exécutée, puis la suivante est exécutée, et ainsi de suite.

Tout est comme vous l'attendez, et comme cela fonctionne dans la plupart des langages de programmation.

Cependant, il arrive que vous ne puissiez pas simplement attendre qu'une ligne de code s'exécute.

Vous ne pouvez pas simplement attendre 2 secondes pour qu'un gros fichier se charge, et arrêter complètement le programme.

Vous ne pouvez pas simplement attendre qu'une ressource réseau soit téléchargée avant de faire autre chose.

JavaScript résout ce problème en utilisant des **rappels**.

L'un des exemples les plus simples de l'utilisation des rappels est avec les temporisateurs. Les temporisateurs ne font pas partie de JavaScript, mais ils sont fournis par le navigateur et Node.js. Laissez-moi parler de l'un des temporisateurs que nous avons : `setTimeout()`.

La fonction `setTimeout()` accepte 2 arguments : une fonction, et un nombre. Le nombre est le nombre de millisecondes qui doivent s'écouler avant que la fonction ne soit exécutée.

Exemple :

```js
setTimeout(() => {
  // s'exécute après 2 secondes
  console.log('inside the function')
}, 2000)
```

La fonction contenant la ligne `console.log('inside the function')` sera exécutée après 2 secondes.

Si vous ajoutez un `console.log('before')` avant la fonction, et `console.log('after')` après celle-ci :

```js
console.log('before')
setTimeout(() => {
  // s'exécute après 2 secondes
  console.log('inside the function')
}, 2000)
console.log('after')
```

Vous verrez ceci se produire dans votre console :

```js
before
after
inside the function
```

La fonction de rappel est exécutée de manière asynchrone.

C'est un modèle très courant lorsque l'on travaille avec le système de fichiers, le réseau, les événements, ou le DOM dans le navigateur.

Toutes les choses que j'ai mentionnées ne sont pas du "noyau" JavaScript, donc elles ne sont pas expliquées dans ce manuel, mais vous trouverez de nombreux exemples dans mes autres manuels disponibles sur [https://flaviocopes.com](https://flaviocopes.com).

Voici comment nous pouvons implémenter des rappels dans notre code.

Nous définissons une fonction qui accepte un paramètre `callback`, qui est une fonction.

Lorsque le code est prêt à invoquer le rappel, nous l'invoquons en passant le résultat :

```js
const doSomething = callback => {
  //faire des choses
  //faire des choses
  const result = /* .. */
  callback(result)
}
```

Le code utilisant cette fonction l'utiliserait comme ceci :

```js
doSomething(result => {
  console.log(result)
})
```

## Promesses

Les promesses sont une alternative pour gérer le code asynchrone.

Comme nous l'avons vu dans le chapitre précédent, avec les rappels, nous passerions une fonction à un autre appel de fonction qui serait appelé lorsque la fonction a terminé le traitement.

Comme ceci :

```js
doSomething(result => {
  console.log(result)
})
```

Lorsque le code `doSomething()` se termine, il appelle la fonction reçue en tant que paramètre :

```js
const doSomething = callback => {
  //faire des choses
  //faire des choses
  const result = /* .. */
  callback(result)
}
```

Le principal problème avec cette approche est que si nous devons utiliser le résultat de cette fonction dans le reste de notre code, tout notre code doit être imbriqué à l'intérieur du rappel, et si nous devons faire 2-3 rappels, nous entrons dans ce qui est généralement défini comme "l'enfer des rappels" avec de nombreux niveaux de fonctions imbriquées dans d'autres fonctions :

```js
doSomething(result => {
  doSomethingElse(anotherResult => {
    doSomethingElseAgain(yetAnotherResult => {
      console.log(result)
    })
  }) 
})
```

Les promesses sont un moyen de gérer cela.

Au lieu de faire :

```js
doSomething(result => {
  console.log(result)
})
```

Nous appelons une fonction basée sur les promesses de cette manière :

```js
doSomething()
  .then(result => {
    console.log(result)
  })
```

Nous appelons d'abord la fonction, puis nous avons une méthode `then()` qui est appelée lorsque la fonction se termine.

L'indentation n'a pas d'importance, mais vous utiliserez souvent ce style pour plus de clarté.

Il est courant de détecter les erreurs en utilisant une méthode `catch()` :

```js
doSomething()
  .then(result => {
    console.log(result)
  })
  .catch(error => {
    console.log(error)
  })
```

Maintenant, pour pouvoir utiliser cette syntaxe, l'implémentation de la fonction `doSomething()` doit être un peu spéciale. Elle doit utiliser l'API Promesses.

Au lieu de la déclarer comme une fonction normale :

```js
const doSomething = () => {
  
}
```

Nous la déclarons comme un objet promesse :

```js
const doSomething = new Promise()
```

et nous passons une fonction dans le constructeur de Promesse :

```js
const doSomething = new Promise(() => {

})
```

Cette fonction reçoit 2 paramètres. Le premier est une fonction que nous appelons pour résoudre la promesse, le second une fonction que nous appelons pour rejeter la promesse.

```js
const doSomething = new Promise(
  (resolve, reject) => {
    
})
```

Résoudre une promesse signifie la compléter avec succès (ce qui entraîne l'appel de la méthode `then()` dans ce qui l'utilise).

Rejeter une promesse signifie la terminer avec une erreur (ce qui entraîne l'appel de la méthode `catch()` dans ce qui l'utilise).

Voici comment :

```js
const doSomething = new Promise(
  (resolve, reject) => {
    //du code
    const success = /* ... */
    if (success) {
      resolve('ok')
    } else {
      reject('this error occurred')
    }
  }
)
```

Nous pouvons passer un paramètre aux fonctions resolve et reject, de n'importe quel type que nous voulons.

## Async et Await

Les fonctions asynchrones sont une abstraction de plus haut niveau des promesses.

Une fonction asynchrone retourne une promesse, comme dans cet exemple :

```js
const getData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => 
      resolve('some data'), 2000)
  })
}
```

Tout code qui souhaite utiliser cette fonction utilisera le mot-clé `await` juste avant la fonction :

```js
const data = await getData()
```

et en faisant cela, toute donnée retournée par la promesse sera assignée à la variable `data`.

Dans notre cas, la donnée est la chaîne de caractères "some data".

Avec une particularité : chaque fois que nous utilisons le mot-clé `await`, nous devons le faire à l'intérieur d'une fonction définie comme `async`.

Comme ceci :

```js
const doSomething = async () => {
  const data = await getData()
  console.log(data)
}
```

Le duo async/await nous permet d'avoir un code plus propre et un modèle mental simple pour travailler avec du code asynchrone.

Comme vous pouvez le voir dans l'exemple ci-dessus, notre code semble très simple. Comparez-le au code utilisant les promesses, ou les fonctions de rappel.

Et ceci est un exemple très simple, les principaux avantages apparaîtront lorsque le code sera beaucoup plus complexe.

Par exemple, voici comment vous obtiendriez une ressource JSON en utilisant l'API Fetch, et la parser, en utilisant des promesses :

```js
const getFirstUserData = () => {
  // obtenir la liste des utilisateurs
  return fetch('/users.json') 
    // parser le JSON
    .then(response => response.json()) 
    // choisir le premier utilisateur
    .then(users => users[0]) 
    // obtenir les données de l'utilisateur
    .then(user => 
      fetch(`/users/${user.name}`)) 
    // parser le JSON
    .then(userResponse => response.json()) 
}

getFirstUserData()
```

Et voici la même fonctionnalité fournie en utilisant await/async :

```js
const getFirstUserData = async () => {
  // obtenir la liste des utilisateurs
  const response = await fetch('/users.json') 
  // parser le JSON
  const users = await response.json() 
  // choisir le premier utilisateur
  const user = users[0] 
  // obtenir les données de l'utilisateur
  const userResponse = 
    await fetch(`/users/${user.name}`)
  // parser le JSON
  const userData = await user.json() 
  return userData
}

getFirstUserData()
```

## Portée des variables

Lorsque j'ai introduit les variables, j'ai parlé de l'utilisation de `const`, `let`, et `var`.

La portée est l'ensemble des variables qui est visible pour une partie du programme.

En JavaScript, nous avons une portée globale, une portée de bloc et une portée de fonction.

Si une variable est définie en dehors d'une fonction ou d'un bloc, elle est attachée à l'objet global et elle a une portée globale, ce qui signifie qu'elle est disponible dans toutes les parties d'un programme.

Il existe une différence très importante entre les déclarations `var`, `let` et `const`.

Une variable définie comme `var` à l'intérieur d'une fonction n'est visible qu'à l'intérieur de cette fonction, similaire aux arguments d'une fonction.

Une variable définie comme `const` ou `let`, en revanche, n'est visible qu'à l'intérieur du **bloc** où elle est définie.

Un bloc est un ensemble d'instructions regroupées dans une paire d'accolades, comme celles que nous pouvons trouver à l'intérieur d'une instruction `if`, d'une boucle `for`, ou d'une fonction.

Il est important de comprendre qu'un bloc ne définit pas une nouvelle portée pour `var`, mais il le fait pour `let` et `const`.

Cela a des implications très pratiques.

Supposons que vous définissez une variable `var` à l'intérieur d'une conditionnelle `if` dans une fonction

```js
function getData() {
  if (true) {
    var data = 'some data'
    console.log(data) 
  }
}
```

Si vous appelez cette fonction, vous obtiendrez `some data` imprimé dans la console.

Si vous essayez de déplacer console.log(data) après le `if`, cela fonctionne toujours :

```js
function getData() {
  if (true) {
    var data = 'some data'
  }
  console.log(data) 
}
```

Mais si vous passez de `var data` à `let data` :

```js
function getData() {
  if (true) {
    let data = 'some data'
  }
  console.log(data) 
}
```

Vous obtiendrez une erreur : `ReferenceError: data is not defined`.

C'est parce que `var` est limité à la portée de la fonction, et il se passe ici une chose spéciale appelée hoisting. En bref, la déclaration `var` est déplacée en haut de la fonction la plus proche par JavaScript avant qu'il n'exécute le code. C'est à cela que ressemble la fonction pour JS en interne, plus ou moins :

```js
function getData() {
  var data
  if (true) {
    data = 'some data'
  }
  console.log(data) 
}
```

C'est pourquoi vous pouvez également faire `console.log(data)` en haut d'une fonction, même avant qu'elle ne soit déclarée, et vous obtiendrez `undefined` comme valeur pour cette variable :

```js
function getData() {
  console.log(data) 
  if (true) {
    var data = 'some data'
  }
}
```

mais si vous passez à `let`, vous obtiendrez une erreur `ReferenceError: data is not defined`, parce que le hoisting ne se produit pas pour les déclarations `let`.

`const` suit les mêmes règles que `let` : il est limité à la portée du bloc.

Cela peut être trompeur au début, mais une fois que vous réalisez cette différence, alors vous verrez pourquoi `var` est considéré comme une mauvaise pratique de nos jours par rapport à `let` - ils ont moins de pièces mobiles, et leur portée est limitée au bloc, ce qui les rend également très bons comme variables de boucle car ils cessent d'exister après qu'une boucle a pris fin :

```js
function doLoop() {
  for (var i = 0; i < 10; i++) {
    console.log(i)
  }
  console.log(i)
}

doLoop()
```

Lorsque vous sortez de la boucle, `i` sera une variable valide avec la valeur 10.

Si vous passez à `let`, lorsque vous essayez de faire `console.log(i)`, cela entraînera une erreur `ReferenceError: i is not defined`.

## Conclusion

Merci beaucoup d'avoir lu ce livre.

J'espère qu'il vous inspirera à en apprendre davantage sur JavaScript.

Pour plus d'informations sur JavaScript, consultez mon blog [flaviocopes.com](https://flaviocopes.com).

> Note : [Vous pouvez obtenir une version PDF et ePub de ce Guide du Débutant en JavaScript](https://flaviocopes.com/page/javascript-handbook/)