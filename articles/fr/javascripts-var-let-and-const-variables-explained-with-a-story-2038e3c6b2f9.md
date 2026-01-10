---
title: Les variables var, let et const de JavaScript expliquées avec une histoire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T23:17:21.000Z'
originalURL: https://freecodecamp.org/news/javascripts-var-let-and-const-variables-explained-with-a-story-2038e3c6b2f9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ikou8bbQjbVnRyjh
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les variables var, let et const de JavaScript expliquées avec une histoire
seo_desc: 'By Prarthana S. Sannamani

  In this article, we will explore the history of var in JavaScript, the need for
  let and const, and the differences between them.

  This post consists of two sections: Fictional piece and Technical explanation.

  The fictional pi...'
---

Par Prarthana S. Sannamani

Dans cet article, nous allons explorer l'histoire de `var` en JavaScript, le besoin de `let` et `const`, et les différences entre eux.

Cet article se compose de deux sections : une pièce fictive et une explication technique.

La pièce fictive est destinée à faciliter l'apprentissage des concepts pour les débutants, mais plusieurs parties sont simplifiées et ne présentent pas toujours une analogie exacte 1:1.

Commençons !

### Un conte de trois variables

La ville de JavaScript était une ville animée au bord de la mer avec un quartier commercial rempli de gratte-ciels.

Depuis la nuit des temps, les résidents de la ville de JavaScript utilisaient des boîtes `Vary` pour stocker leurs objets de valeur, surtout leurs précieuses billes d'or. Pour ce faire, les résidents avaient deux options :

1. Ils pouvaient placer les billes d'or directement dans la boîte (passage par valeur)
2. S'ils avaient un grand nombre de billes d'or qui ne rentraient pas dans la boîte, ils pouvaient placer un morceau de papier spécial dans la boîte, indiquant où ils les avaient stockées. Par exemple, le morceau de papier pouvait dire « deuxième tiroir de l'armoire de stockage » (passage par référence)

Puisque la ville se targuait de loi et d'ordre, ils ont établi plusieurs règles et procédures.

#### **_Règles pour les magasins_**

1. Pour maintenir la sérénité de la ville, les magasins ne pouvaient être construits que sur des collines (les fonctions créent leur propre portée locale)
2. La seule exception à la règle 1 était le magasin spécial au niveau de la mer (portée globale).
3. Un magasin pouvait avoir des magasins intérieurs pour aider à payer le loyer (fonctions imbriquées). Cependant, chaque magasin intérieur devait être sur une colline plus haute que celle du magasin propriétaire (portée de fonction locale).
4. Un magasin pouvait avoir des comptoirs « offre spéciale », comme « `Si` vous avez plus de 20 ans, achetez une boîte spéciale ici. » Et « `Pour` (chaque) enfant `de` votre famille, achetez une boîte pour enfant ici » (autres blocs tels que `if` et les boucles).
5. Chaque magasin devait avoir un comptoir « déclaration-initialisation » avec un garde à l'entrée, qui tenait un registre d'inscription (hissage en haut de la portée correspondante).
6. Chaque magasin pouvait avoir un nombre illimité de comptoirs « affectation » avec un assistant de magasin, qui placerait les billes d'or d'un résident dans la boîte.

#### Règles pour la régulation du marché des boîtes

1. Les boîtes ne pouvaient être achetées qu'au magasin spécial au niveau de la mer ou dans un magasin sur les collines (une variable peut avoir une portée globale ou locale).
2. Au niveau de la mer ou sur n'importe quelle colline, les résidents ne pouvaient posséder qu'une seule boîte colorée `Vary` (les identifiants en double ne sont pas autorisés).
3. La boîte `Vary` ne pouvait jamais être vide dès sa création. Elle devait contenir du coton (`undefined`) ou des billes d'or à tout moment (effet du hisage).
4. Une fois qu'un résident quittait un magasin (et descendait donc de la colline), toutes les boîtes qu'il y avait achetées disparaissaient (fin de la portée de la variable).

#### Procédure pour les résidents pour acheter les boîtes `Vary`

Nous allons suivre le parcours d'un résident, John, dans cet article.

1. John entre dans le magasin et déclare quelle couleur de boîte `Vary` il souhaite acheter au comptoir « déclaration-initialisation ». Le garde note cela dans son registre.
2. Le garde fait apparaître la boîte colorée `Vary`, la remplit de coton et la remet à John.
3. John reçoit un ticket pour son tour et, lorsqu'il arrive, il se rend au comptoir « affectation ». Jusqu'à ce moment, il peut tenir sa boîte mais ne peut pas y placer ses billes d'or.
4. Au comptoir, John remet sa boîte et ses billes d'or à l'assistant du magasin, qui retire le coton, place les billes d'or à l'intérieur et la lui rend.

Naturellement, ces règles ont apporté des problèmes particuliers.

1. Avec des temps d'attente longs pour le comptoir « affectation », John oubliait qu'il n'avait pas encore placé ses billes d'or dans sa boîte. Il l'ouvrait pour se vanter auprès de ses amis et ne trouvait que du coton. Dommage !
2. Souvent, John oubliait qu'il avait déjà acheté une certaine boîte colorée dans un magasin et s'inscrivait à nouveau pour la même boîte colorée. Cela entraînait instantanément la disparition de sa boîte existante (et de ses billes d'or !!), suivie de l'apparition par le garde d'une nouvelle boîte remplie de coton. Aucun avertissement ! Cela était particulièrement répandu aux comptoirs « offres spéciales ».

Vous pouvez imaginer à quel point cette situation était frustrante. Avec les résidents de la ville de JavaScript perdant leurs billes, le Conseil de la ville a décidé de prendre des mesures.

Lors d'une grande réunion de la ville en 2015, ils ont fièrement introduit deux nouvelles boîtes : `Lety` et `Consty`.

Ils ont également introduit l'autre changement majeur : la suppression des comptoirs « offres spéciales » des magasins `Lety` et `Consty`. À la place, ces comptoirs ont été mis à niveau en magasins intérieurs, construits sur une colline à l'intérieur du magasin.

#### Règles pour l'achat des boîtes `Lety` et `Consty`

1. John entre dans le magasin et déclare quel type et quelle couleur de boîte il souhaite acheter au comptoir « déclaration ». Le garde note cela dans son registre. Cette information apparaît de manière floue sur la grande horloge murale, qui peut être vue mais pas utilisée, et est appelée la « zone morte temporelle ».
2. John reçoit un ticket pour son tour. **Puisque la boîte n'est pas créée à la déclaration, elle n'est pas disponible pour une utilisation.**

C'est là que les règles d'achat de `Lety` et `Consty` divergent.

#### Règles pour `Lety` :

1. Une fois que le tour de John arrive, il se rend au comptoir « initialisation ».
2. Au comptoir, John a le choix d'acheter une boîte `Lety` vide, ou d'acheter une boîte `Lety` et d'y placer ses billes d'or immédiatement.
3. Selon son choix, l'assistant du magasin fait apparaître la boîte `Lety`, la remplit de coton ou la remet au comptoir « affectation », où les billes d'or de John sont placées à l'intérieur.

#### Règles pour `Consty`

Les boîtes `Consty` sont **extrêmement** spéciales. Doublées d'une couche d'or à l'intérieur et scellées avec un cadenas, ces boîtes sont si chères aux assistants du magasin qu'ils refusent de les vendre sans savoir exactement ce qui y sera placé.

1. Une fois que le tour de John arrive, il se rend au comptoir « initialisation-affectation ».
2. John est **obligé** de remettre ses billes d'or à l'assistant du magasin, qui fait apparaître la boîte colorée `Consty`, y place les billes d'or et **verrouille la boîte pour toujours**.

Si vous vous souvenez, John pouvait placer directement ses billes d'or dans la boîte ou placer un morceau de papier spécial indiquant l'emplacement de ses billes d'or.

1. S'il place ses billes d'or à l'intérieur de la boîte `Consty`, il ne peut plus en ajouter ou en retirer. Elles sont verrouillées pour toujours.
2. Cependant, s'il place le morceau de papier spécial, c'est un peu différent. Bien qu'il ne puisse pas **remplacer** le papier, il peut ajouter ou retirer ses billes d'or à l'emplacement qu'il a spécifié sur le papier.

Revenons aux problèmes particuliers qui ont motivé l'invention des boîtes `Lety` et `Consty`, et voyons s'ils sont résolus.

> Avec des temps d'attente longs pour le comptoir « affectation », John oubliait qu'il n'avait pas encore placé ses billes d'or dans sa boîte. Il l'ouvrait pour se vanter auprès de ses amis et ne trouvait que du coton. Dommage !

Puisque les boîtes `Lety` et `Consty` ne sont pas créées avant que John ne se rende respectivement aux comptoirs « initialisation » ou « initialisation-affectation », il sait qu'il ne possède pas la boîte et n'essaie donc pas de l'utiliser. Même s'il le fait, des alarmes installées dans les magasins se déclenchent pour l'alerter.

> Souvent, John oubliait qu'il avait déjà acheté une certaine boîte colorée dans un magasin et s'inscrivait à nouveau pour la même boîte colorée. Cela entraînait instantanément la disparition de sa boîte existante (et de ses billes d'or !!), suivie de l'apparition par le garde d'une nouvelle boîte remplie de coton. Aucun avertissement ! Cela était particulièrement répandu aux comptoirs « offres spéciales ».

Cela est géré par la suppression des comptoirs « offres spéciales » et l'introduction de la règle suivante :

**_Une fois qu'un résident s'est inscrit pour une certaine boîte colorée au comptoir « déclaration » dans les magasins `Lety` ou `Consty`, il ne peut plus s'inscrire à nouveau pour la même boîte colorée dans ce magasin ! S'il le fait, des alarmes retentissantes se déclencheront._**

Ces merveilleuses nouvelles boîtes et règles ont apporté la paix et la sérénité à la ville de JavaScript une fois de plus, et tout le monde a vécu heureux pour toujours.

### Plongeons dans les détails techniques

Passons en revue les aspects techniques de `var`, `let` et `const` pour comprendre l'histoire.

Si vous n'êtes pas familier avec le hisage et la portée (niveau fonction et niveau bloc), je vous recommande de lire mon article précédent [**ici**](https://codeburst.io/hoist-your-knowledge-of-javascript-hoisting-59b73124b430)**.**

Voici un extrait pour comprendre l'analogie des collines que j'ai utilisée ci-dessus :

> Pour augmenter notre compréhension de la portée au niveau bloc et au niveau fonction, considérons l'analogie des collines. Supposons que la portée globale est la terre au niveau de la mer et que les portées locales sont des collines. Si vous vous tenez au sommet d'une colline, vous pouvez voir (accéder) les variables en dessous de votre altitude. Cependant, si vous êtes au niveau de la mer, vous ne pouvez pas voir (accéder) les variables à une altitude plus élevée.

> En C++, chaque bloc `{}` entraîne la formation d'une nouvelle colline (portée locale), à une altitude d'un niveau supérieur à celle dans laquelle il est enfermé. Les blocs imbriqués entraînent des collines à plusieurs niveaux.

> En JavaScript, seule une fonction entraîne la formation d'une nouvelle colline (portée locale). Les autres blocs tels que les blocs `if` sont présents à la même altitude.

> Par conséquent, si une variable est déclarée sur une certaine colline (bloc), elle peut être accessible depuis cette colline (bloc) et toutes les collines (blocs) au-dessus.

### Cycle de vie d'une variable

**Phase de déclaration** : Enregistrement d'une variable dans sa portée, qui peut être globale, fonctionnelle ou de bloc. Dans cette phase, aucune mémoire n'est encore allouée.

**Phase d'initialisation** : Allocation de mémoire pour la variable, où une liaison est créée, et la variable est initialisée avec `undefined`.

**Phase d'affectation** : Affectation d'une valeur à la variable.

Il est important de noter que la déclaration de variable et la phase de déclaration ne sont pas les mêmes !

Une déclaration de variable est une instruction telle que `var a`.

La phase de déclaration est une étape réalisée par le compilateur JavaScript. Dans cette étape, lorsque le compilateur rencontre une déclaration de variable, il la déclare/enregistre dans sa portée correspondante (si la déclaration n'existe pas déjà). Plus tard, le code généré par le compilateur est exécuté par le moteur JavaScript.

### var

1. portée globale ou fonctionnelle
2. la valeur peut être mise à jour
3. peut être re-déclarée
4. hissée : enregistrée dans la portée, et initialisée avec `undefined`

Voici un exemple simple où nous initialisons une variable, mettons à jour sa valeur et la re-déclarons.

```
// Hisséeconsole.log(a); // undefined
```

```
var a = 10;console.log(a); // 10
```

```
a = 20; // valeur mise à jour : OKconsole.log(a); // 20
```

```
var a = 30; // re-déclarée : OKconsole.log(a); // 30
```

En haut de la portée, toutes les variables sont déclarées dans leur portée correspondante et initialisées avec une valeur de `undefined`. L'enregistrement et l'initialisation sont couplés. Ainsi, la variable `a` est disponible pour une utilisation dès le haut de la portée. Donc, lorsque nous essayons d'accéder à la valeur de `a` avant qu'elle ne soit déclarée, cela ne génère pas d'erreur. Au contraire, `undefined` est imprimé. Cela est connu sous le nom de hisage de variable.

Voici un exemple qui montre la portée fonctionnelle de `var`.

```
function outerFunc() {  var a = 10;  if (a > 5) {    var a = 20;    console.log(a); // 20  }  console.log(a); // 20}
```

La variable `a` est initialement déclarée dans la portée de `outerFunc`. Puisque le bloc `if` ne crée pas une nouvelle portée, lorsque nous re-déclarons la variable `a`, l'ancienne variable `a` est effacée et une nouvelle variable `a` est créée avec une valeur de `20`.

La re-déclaration accidentelle des variables `var` est une erreur courante que les développeurs commettent en raison de la re-déclaration silencieuse et de la confusion dans la compréhension de la portée fonctionnelle.

### let

1. portée de bloc
2. la valeur peut être mise à jour
3. ne peut pas être re-déclarée
4. hissée mais non initialisée

Voici un exemple simple où nous initialisons une variable, mettons à jour sa valeur et essayons de la re-déclarer.

```
console.log(a); //   ReferenceError: a is not defined
```

```
let a = 10;console.log(a); // 10
```

```
a = 20;console.log(a); // 20
```

```
let a = 30; // SyntaxError: Identifier 'a' has already been declared
```

La mise à jour d'une variable `let` est autorisée. Cependant, si vous essayez de la re-déclarer, vous rencontrez une `SyntaxError`. Cela protège les développeurs de la re-déclaration silencieuse et accidentelle des variables.

Les variables `let` sont-elles hissées ?

C'est une question délicate. Internet est divisé sur ce point : il y a des arguments pour les deux côtés. Certains développeurs pensent que les variables `let` (et `const`) ne sont pas hissées, car elles ne peuvent pas être accessibles avant que leur instruction de déclaration ne soit atteinte, contrairement à `var`. Cependant, cette réponse dépend vraiment de votre définition du hisage. Si le hisage est le couplage des phases de déclaration et d'initialisation d'une variable en haut de sa portée correspondante, alors les variables `let` et `const` ne sont pas hissées.

Cependant, après avoir lu plusieurs avis et sans être plus proche de la vérité, j'ai décidé de suivre la définition de hisage de MDN.

> Les liaisons `let` sont créées en haut de la portée (bloc) contenant la déclaration, communément appelée « hisage ». (MDN)

Selon cette définition, la réponse à notre question est oui. Les variables `let` sont hissées, mais elles ne sont pas initialisées avec `undefined`. Ainsi, elles existent dans une période de temps appelée la « Zone Morte Temporelle » depuis le début du bloc jusqu'à ce que leur définition soit évaluée. Essayer d'y accéder dans la ZMT génère une `ReferenceError`, comme vu dans l'exemple.

Voici un exemple qui montre la portée de bloc de `let`.

```
function outerFunc() {  let a = 10;  if (a > 5) {    let a = 20;    console.log(a); // 20  }  console.log(a); // 10}
```

La première déclaration de la variable `a` est dans la portée de `outerFunc`. Le bloc `if` crée une nouvelle portée, et lorsque nous faisons la deuxième déclaration de la variable `a`, elle est enregistrée dans la nouvelle portée. Cela est indépendant de la portée de `outerFunc`. Par conséquent, une variable `a` séparée est créée, et nous pouvons observer que les modifications de la variable interne `a` n'affectent pas la variable externe `a`.

Cela permet aux développeurs de créer facilement des variables temporaires à l'intérieur des blocs de condition et de boucle, sans avoir à chercher si la variable existe déjà dans la fonction.

### const

1. portée de bloc
2. la liaison est immuable (mais la valeur peut ou non être changée)
3. ne peut pas être re-déclarée
4. hissée mais non initialisée

Voici un exemple simple où nous initialisons une variable, essayons de mettre à jour sa valeur et essayons de la re-déclarer.

```
console.log(a); //  ReferenceError: a is not defined
```

```
const a = 10;console.log(a); // 10
```

```
a = 20; // TypeError: Assignment to constant variable.
```

```
const a = 30; // SyntaxError: Identifier 'a' has already been declared
```

```
const b; // SyntaxError: Missing initializer in const declaration
```

Similaire aux variables `let`, les variables `const` sont hissées, mais non initialisées avec `undefined`. Essayer d'y accéder dans la Zone Morte Temporelle génère une `ReferenceError`.

Si nous essayons d'initialiser une variable `const` sans affectation, comme dans l'exemple ci-dessus pour `const b;` , nous rencontrons une `SyntaxError: Missing initializer in const declaration`. De même, nous ne pouvons pas re-déclarer les variables `const`. Cela conduit à une `SyntaxError`.

Reportons temporairement notre discussion sur la mise à jour des variables `const`.

Voici un exemple de portée de niveau bloc des variables `const` :

```
function outerFunc() {  const a = 10;  if (a > 5) {    const a = 20;    console.log(a); // 20  }  console.log(a); // 10}
```

Le comportement ci-dessus est similaire à celui des variables `let`, où une nouvelle portée est créée pour le bloc `if`, et donc, les modifications de la variable interne `a` n'affectent pas la variable externe `a`.

Revenons à la discussion sur la mise à jour des variables `const`.

Il y a une incompréhension courante selon laquelle les variables `const` contiennent des valeurs constantes et ne peuvent jamais être mises à jour. Cependant, `const` fonctionne différemment.

Après l'affectation initiale, la **liaison** des variables `const` est **immuable**, et donc, la **référence** à ce qui est stocké dans la variable `const` ne peut pas être modifiée. En termes simples, cela signifie que vous ne pouvez pas avoir une instruction avec **seulement** la variable `const` du côté gauche, suivie d'un signe égal `=` , et une nouvelle valeur du côté droit.

Cependant, si la valeur peut être mise à jour dépend de ce qui y est stocké. Considérons les deux cas :

1. Type de données primitif : Booléen, Null, Undefined, Nombre, Chaîne, Symbole
2. Objets

Si une variable est assignée à un type de données primitif, le type de données est passé par **valeur**. Par conséquent, si nous avons une instruction `let x = 10` , nous pouvons visualiser `x` contenant le Nombre `10`.

Si une variable est assignée à un objet, l'objet est passé par **référence**. Par conséquent, si nous avons une instruction `let x = [1,2,3]`, `x` ne contient pas le tableau `[1,2,3]` . Au lieu de cela, il contient une référence (adresse) de l'endroit où le tableau `[1,2,3]` est stocké en mémoire après sa création. Par conséquent, nous pouvons visualiser `x` contenant une adresse telle que `5274621`.

Voyons des exemples de types de données primitifs et objets :

```
// Booléenconst a = true;a = false; // TypeError: Assignment to constant variable.
```

```
// Nullconst b = null;b = 10; // TypeError: Assignment to constant variable.
```

```
// Undefinedconst c = undefined;c = 10; // TypeError: Assignment to constant variable.
```

```
// Nombreconst d = 50;d = 100; // TypeError: Assignment to constant variable.
```

```
// Chaîneconst e = 'hello';e = 'world'; // TypeError: Assignment to constant variable.
```

```
// Symboleconst f = Symbol('foo');f = 100; // TypeError: Assignment to constant variable.
```

Comme nous pouvons le voir ci-dessus, essayer de mettre à jour la valeur de tout type de données primitif entraîne une `TypeError`.

```
/* Les tableaux sont stockés par référence.Par conséquent, bien que la liaison soit immuable, les valeurs ne le sont pas. */
```

```
const c = [1,2,3];
```

```
c.push(10); // Pas d'erreurconsole.log(c); // [1,2,3,10]
```

```
c.pop(); // Pas d'erreurconsole.log(c); // [1,2,3]
```

```
c = [4,5,6]; // TypeError: Assignment to constant variable.
```

Comme nous pouvons le voir ci-dessus, nous pouvons ajouter et retirer des éléments du tableau puisque cela ne modifie que le contenu de ce que la variable `const` pointe, mais n'essaie pas de réécrire le contenu de la variable `const` elle-même. Cependant, si nous essayons de mettre à jour la liaison de la variable `const` en lui réassignant un tout nouveau tableau `c = [4,5,6]`, cela génère une `TypeError`.

```
/* Les objets sont stockés par référence.Par conséquent, bien que la liaison soit immuable, les valeurs ne le sont pas. */
```

```
const d = { name: 'John Doe', age: 35};
```

```
d.age = 40; // Modification d'une propriété : Pas d'erreurconsole.log(d); // { name: 'John Doe', age: 40};
```

```
d.zipCode = '52534'; // Ajout d'une propriété : Pas d'erreurconsole.log(d); // { age: 40, name: "John Doe", zipCode: '52534; }
```

```
d = { name: 'Mary Jane', age: 25}; // TypeError: Assignment to constant variable.
```

Comme nous pouvons le voir ci-dessus, nous pouvons modifier et ajouter des propriétés à l'objet puisque cela ne modifie que le contenu de ce que la variable `const` pointe, mais n'essaie pas de réécrire le contenu de la variable `const` elle-même. Cependant, si nous essayons de mettre à jour la liaison de la variable `const` en lui réassignant un tout nouvel objet `d = { name: 'Mary Jane', age: 25 };`, cela génère une `TypeError`.

### Quand dois-je utiliser quoi ?

JavaScript dispose désormais de trois types de variables, et une question naturelle est de savoir quand utiliser quoi.

Après l'introduction de `let` à portée de bloc, l'utilisation de `var` est généralement déconseillée pour éviter la confusion avec la portée au niveau de la fonction, les re-déclarations accidentelles et les bugs de hisage avec la valeur `undefined`. À moins que vous n'ayez une raison impérieuse d'utiliser la portée de fonction de `var`, utilisez `let`.

Utilisez `const` pour contenir des valeurs qui sont des faits, comme `const PI = 3.14`, ou des valeurs qui doivent strictement rester inchangées pour toute l'exécution du programme.

Une approche de programmation courante consiste à ce que les développeurs commencent par déclarer toutes les variables avec `const` , et les convertissent progressivement en variables `let` si le besoin s'en fait sentir. Personnellement, je commence avec des variables `let`, et les convertis en variables `const` si je vois le besoin. Il n'y a pas d'approche fixe, et vous devriez utiliser ce qui fonctionne le mieux pour votre code.

Si vous avez le temps, je vous recommande vivement de relire la pièce fictive car cela renforcera les connexions dans votre esprit avec les connaissances techniques supplémentaires.

Merci d'avoir lu ! J'espère que vous avez appris quelque chose de nouveau, et j'adorerais recevoir des commentaires.

Suivez-moi sur Twitter [ici](https://twitter.com/prar_s), et LinkedIn [ici](https://www.linkedin.com/in/prarthana-sannamani/).

Références :

1. [_https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
2. [_https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
3. [_https://dmitripavlutin.com/variables-lifecycle-and-why-let-is-not-hoisted/_](https://dmitripavlutin.com/variables-lifecycle-and-why-let-is-not-hoisted/)
4. [_https://github.com/getify/You-Dont-Know-JS_](https://github.com/getify/You-Dont-Know-JS)