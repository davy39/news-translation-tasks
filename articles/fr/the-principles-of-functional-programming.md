---
title: Les principes de la programmation fonctionnelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-02T09:27:59.000Z'
originalURL: https://freecodecamp.org/news/the-principles-of-functional-programming
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/fp-cover-1.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
seo_title: Les principes de la programmation fonctionnelle
seo_desc: 'By Yann Salmon

  In this post, I will lay down the major principles of Functional Programming, starting
  with the basics and then exploring more advanced concepts.

  I''ll first talk about why you should bother with Functional Programming, that is
  when it''...'
---

Par Yann Salmon

Dans cet article, je vais exposer les principaux principes de la programmation fonctionnelle, en commençant par les bases avant d'explorer des concepts plus avancés.

Je vais d'abord parler de pourquoi vous devriez vous intéresser à la programmation fonctionnelle, c'est-à-dire quand elle est utile et quand elle ne l'est pas.

Nous allons couvrir beaucoup de choses ici, alors allez à votre propre rythme. Prenez des pauses et faites des siestes entre vos sessions de lecture et faites les exercices que je propose.

Bien sûr, vous pouvez sauter des sections ou revenir en arrière selon vos besoins.

Cet article cible intentionnellement plusieurs types de lecteurs :

1. Ceux qui ne connaissent presque rien à la PF mais sont assez familiers avec JavaScript
2. Ceux qui ont une connaissance intermédiaire de la PF et une certaine familiarité avec le paradigme, mais qui veulent une vision plus claire de l'ensemble et souhaitent explorer des concepts avancés
3. Ceux qui en savent beaucoup sur la PF et veulent une aide-mémoire pour revisiter certains concepts si nécessaire

Je vous invite à réfléchir soigneusement à chaque phrase au lieu de vous précipiter à travers le contenu comme nous en avons tous l'habitude.

J'espère que cet article sera une étape importante dans votre parcours vers la programmation fonctionnelle, ainsi qu'une source d'informations à laquelle revenir lorsque nécessaire.

Juste une petite mise en garde, cependant – cet article ne constitue pas une source unique de vérité mais plutôt une invitation à aller plus loin après l'avoir lu.

En d'autres termes, il est destiné à être revisité et enrichi avec d'autres ressources et pratiques.

J'espère clarifier le paysage fonctionnel dans votre esprit, éveiller votre intérêt pour ce que vous ne connaissiez pas, et surtout, fournir des outils utiles pour vos projets quotidiens.

Sans plus attendre, commençons !

## Pourquoi la programmation fonctionnelle ?

À mon avis, il y a 3 avantages majeurs à la PF et 3 (petits) inconvénients :

Avantages :

1. Plus de lisibilité, donc plus de maintenabilité
2. Moins de bugs, surtout dans les contextes concurrents
3. Une nouvelle façon de penser la résolution de problèmes
4. (Bonus personnel) Tout simplement génial à apprendre !

Inconvénients :

1. Peut avoir des problèmes de performance
2. Moins intuitif à utiliser lorsqu'on traite avec l'état et les E/S
3. Peu familier pour la plupart des gens + terminologie mathématique qui ralentit le processus d'apprentissage

Maintenant, je vais expliquer pourquoi je pense cela.

### Lisibilité accrue

Tout d'abord, la programmation fonctionnelle est souvent plus lisible grâce à sa nature **déclarative**.

En d'autres termes, le code est axé sur la description du résultat des calculs, et non sur les calculs eux-mêmes.

[Kyle Simpson](https://github.com/getify/Functional-Light-JS/blob/master/manuscript/ch1.md/#chapter-1-why-functional-programming) le formule ainsi :

> Le code déclaratif est un code plus axé sur la description du résultat "quoi". Le code impératif (l'opposé) est axé sur l'instruction précise à l'ordinateur "comment" faire quelque chose.

Parce que nous passons la grande majorité de notre temps à lire du code (environ 80 % du temps, je suppose) et non à l'écrire, la lisibilité est la première chose que nous devrions améliorer afin d'augmenter notre efficacité lors de la programmation.

Il est également très probable que vous reveniez à un projet après plusieurs semaines sans y avoir touché, donc tout le contexte chargé dans votre mémoire à court terme aura disparu.

Ainsi, comprendre votre code **impératif** ne sera pas aussi facile qu'avant.

La même chose s'applique aux potentiels collègues qui travaillent avec vous sur le projet.

Donc, la lisibilité est un énorme avantage pour un but de plus en plus important : la maintenabilité.

Je pourrais m'arrêter là. L'augmentation de la lisibilité devrait vous donner une motivation majeure pour apprendre la programmation fonctionnelle.

Heureusement, c'est un avantage que vous expérimenterez de plus en plus à mesure que vous vous familiariserez avec le paradigme.

Pas besoin d'être un expert. Le moment où vous écriverez une ligne de code déclarative, vous l'expérimenterez.

Maintenant, le deuxième argument.

### Code moins bogué

Les programmes fonctionnels sont moins bogués, surtout dans les contextes concurrents.

Parce que le style fonctionnel s'efforce d'éviter les mutations, les ressources partagées n'auront pas de contenus inattendus.

Par exemple, imaginez que 2 threads accèdent à la même variable.

Si cette variable peut être mutée, alors, à mesure que les programmes grandissent, vous n'obtiendrez probablement pas ce que vous voulez lorsque vous y accéderez à nouveau.

De plus, l'essor des systèmes multiprocesseurs permet à plusieurs threads de s'exécuter en parallèle.

Il y a donc aussi un risque de chevauchement (un thread peut essayer d'écrire tandis que l'autre essaie de lire).

C'est un peu dommage de ne pas exploiter le matériel parce que nous ne sommes pas capables de faire fonctionner le logiciel.

Cependant, JavaScript est mono-thread et mon expérience personnelle ne s'étend pas beaucoup au-delà.

Ainsi, je suis moins confiant dans cet argument, mais les programmeurs plus expérimentés semblent être d'accord sur ce fait (pour ce que j'ai entendu/lu).

### Résolution de problèmes

Enfin, le dernier avantage – et plus important que vous ne le pensez – est que la programmation fonctionnelle vous donne une nouvelle façon de penser la résolution de problèmes.

Vous êtes peut-être tellement habitué à résoudre des problèmes en utilisant des classes et des objets (programmation orientée objet) que vous ne pensez même pas qu'il pourrait y avoir une meilleure façon de le faire.

Je ne dis pas que la programmation fonctionnelle est toujours meilleure.

Je dis qu'elle sera meilleure dans certains cas et que posséder cette connaissance (ré)ouvrira votre esprit et fera de vous un meilleur programmeur.

Parce que maintenant vous aurez plus d'outils et une capacité accrue à choisir le bon pour le problème en question.

Je pense même que certains principes fondamentaux de la PF peuvent être appliqués à la résolution de problèmes en dehors du domaine des ordinateurs.

Voyons maintenant les inconvénients.

### Problèmes de performance

Le premier inconvénient est que, en appliquant des techniques de PF, vous pouvez finir par utiliser beaucoup de temps et/ou de mémoire.

Parce que vous ne voulez pas muté les choses, le processus consiste essentiellement à copier les données, puis à muté cette copie et à l'utiliser comme l'état actuel.

Cela signifie que les données originales sont laissées intactes, mais vous allouez un tas de temps et de mémoire pour faire la nouvelle copie.

Ainsi, lorsque vous faites beaucoup de copies (de très grands objets imbriqués) ou utilisez des techniques comme la récursion (accumulant des couches dans la pile d'appels), des problèmes de performance peuvent apparaître.

Cependant, de nombreuses solutions existent (partage structurel, optimisation de l'appel terminal) qui rendent les mauvaises performances très rares.

### Moins intuitif

Le deuxième inconvénient est lorsque vous avez besoin d'état ou d'opérations d'E/S.

Eh bien, vous allez dire :

> Les ordinateurs sont des machines à états ! Et éventuellement, j'aurai besoin d'appeler ma base de données, ou d'afficher quelque chose à l'écran, ou d'écrire un fichier.

Je suis tout à fait d'accord.

Le problème est de se rappeler que la programmation fonctionnelle est un style pratique pour les humains, mais les machines effectuent des opérations impératives (alias mutations) tout le temps.

C'est simplement ainsi que cela fonctionne au niveau le plus bas.

L'ordinateur est dans un état à un moment donné et il change tout le temps.

Le but de la PF est de faciliter notre raisonnement sur le code, ce qui augmente les chances que les choses compliquées qui en sortent fonctionnent réellement.

Et la programmation réactive fonctionnelle nous aide à gérer l'état (si vous voulez en savoir plus, il y a des liens à la fin de l'article).

Même si le code impératif semble plus facile/plus intuitif au premier abord, vous finirez par perdre le fil. Je suis assez confiant que si vous faites les efforts initiaux d'apprendre la PF, cela portera ses fruits.

Pour les E/S – abréviation de Entrée/Sortie, c'est-à-dire le code qui transfère des données vers ou depuis un ordinateur et vers ou depuis un périphérique – nous ne pouvons plus avoir de fonctions pures isolées.

Pour gérer cela, nous pouvons adopter une approche [Functional Core Imperative Shell](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell).

En d'autres termes, nous voulons faire autant que possible de manière fonctionnelle et repousser les opérations d'E/S à la couche externe du programme :

![Functional Core Imperative Shell](https://www.freecodecamp.org/news/content/images/2020/08/fp-core-imperative-shell-1.png)

### Courbe d'apprentissage plus raide

Enfin, le dernier inconvénient est que la programmation fonctionnelle est un peu encombrée de terminologie mathématique. Cela crée souvent des frictions inutiles lorsque les développeurs essaient de l'apprendre.

C'est probablement parce que ce style de programmation est d'abord apparu dans le monde académique et y est resté longtemps avant d'émerger et de devenir plus populaire.

Cependant, ces termes techniques/peu familiers ne devraient pas vous faire négliger les principes mathématiques très puissants qui les sous-tendent.

En fin de compte, je pense que les forces de la PF l'emportent sur les faiblesses.

Et la programmation fonctionnelle a beaucoup de sens pour la majorité de la programmation JavaScript à usage général.

Gardez simplement à l'esprit qu'il existe quelques programmes avec des exigences particulières pour lesquels la PF n'est pas adaptée. Mais si ce n'est pas votre cas, il n'y a aucune raison de ne pas tirer parti de ce paradigme.

Maintenant, si vous êtes un débutant complet, vous pouvez vous sentir un peu perdu. C'est normal – restez avec moi. Les sections suivantes clarifieront les concepts auxquels je fais référence ici.

Maintenant, plongeons dans les détails de la programmation fonctionnelle.

## Données, calculs et actions

En PF, vous pouvez décomposer votre programme en 3 parties : les données, les calculs et les actions.

### Données

Les données sont, eh bien, les données. Dans nos langages, elles ont différentes formes, différents types.

En JavaScript, vous avez des nombres, des chaînes de caractères, des tableaux, des objets, et ainsi de suite. Mais à la fin de la journée, ils ne sont que des bits.

Les données sont les éléments de base du programme. Ne pas en avoir est comme ne pas avoir d'eau dans un parc aquatique.

Ensuite, nous pouvons faire des choses avec les données : des calculs ou des actions.

### Calculs

Les calculs sont des transformations de type mathématique des données.

Les fonctions sont un moyen de les créer. Vous lui fournissez un ensemble d'entrées et elle vous retourne un ensemble de sorties.

C'est tout.

Elle ne fait rien en dehors de la fonction, comme en mathématiques. Le monde autour de la fonction n'est pas impacté.

De plus, si vous alimentez la fonction avec la même entrée plusieurs fois, elle devrait toujours vous donner la même sortie.

Un terme courant pour ce type de fonction est **fonction pure**.

En raison de ses caractéristiques, son comportement entier est connu à l'avance. En fait, parce qu'elle retourne simplement une valeur, nous pouvons la traiter comme cette valeur, comme une donnée.

En d'autres termes, nous pourrions remplacer l'appel de fonction par la valeur qu'elle retourne et cela ne changerait pas l'état du programme.

Cela s'appelle la **transparence référentielle**. Ainsi, elles sont vraiment faciles à raisonner, et vous pouvez les utiliser comme entrée ou sortie de fonction et les assigner à des variables.

Ces types de fonctions sont appelées **fonctions de première classe**. En JavaScript, toutes les fonctions sont de première classe.

Il est sûr d'utiliser des fonctions pures parce que, encore une fois, elles sont comme des valeurs.

Pour les fonctions qui font plus que retourner une valeur, vous dépendez de la mémoire humaine. C'est une mauvaise stratégie, surtout pour les logiciels volumineux avec plusieurs personnes travaillant dessus.

Ainsi, vous pouvez utiliser des **fonctions pures** comme remplacement pour les **calculs**. Elles sont identiques.

Maintenant, parlons des actions.

### Actions

Bien sûr, nous avons également besoin de fonctions qui impactent le monde extérieur, qui font réellement quelque chose. Sinon, votre programme serait une calculatrice sans écran.

Quand une fonction impacte des choses en dehors d'elle-même, nous disons qu'elle a des **effets secondaires**. Contrairement aux fonctions pures, elle est dite **impure**.

Les effets secondaires courants sont les affectations/mutations de variables en dehors de la fonction, le journalisation dans la console, l'appel à une API, et ainsi de suite.

Donc, en gros, les **actions** et les **fonctions impures** sont les mêmes.

Voici un exemple simple pour illustrer ces concepts :

```js

//  variable
//       données
let a = 3;

// Calcul / Fonction pure
const double = (x) => x * 2;

double(a);
// 6

// Action / Fonction impure
const IncThenPrint = () => {
  // affectation d'une variable en dehors de la portée de la fonction
  a = a + 1;

  // faire quelque chose (ici impression) en dehors de la fonction
  console.log(a);
};

IncThenPrint();
// console: 4
```

### Données, calculs et actions en programmation fonctionnelle

En PF, l'objectif est de séparer les données, les calculs et les actions tout en s'efforçant de faire la majorité du travail avec des calculs.

Pourquoi ? Parce que les actions dépendent du monde extérieur. Nous n'avons pas un contrôle total sur celui-ci.

Ainsi, nous pouvons obtenir des résultats/comportements inattendus. Donc si la majorité de votre programme est composée d'actions, cela devient rapidement un désordre.

Prenons l'exemple précédent, que se passe-t-il si ailleurs dans le programme, quelqu'un décide d'assigner un objet à la variable `a` ?

Eh bien, nous obtiendrons un résultat inattendu lors de l'exécution de `IncThenPrint` car cela n'a pas de sens d'ajouter 1 à un objet :

```js
let a = 3;

// ...
a = { key: "value" };
// ...

// Action / Fonction impure
const IncThenPrint = () => {
  // affectation d'une variable en dehors de la portée de la fonction
  a = a + 1;

  // faire quelque chose (ici impression) en dehors de la fonction
  console.log(a);
  // imprime: 4
};

IncThenPrint();
// imprime: [object Object]1
// (Parce que JavaScript est un langage à typage dynamique, il convertit les deux opérandes de l'opérateur +
// en chaînes de caractères afin de pouvoir effectuer l'opération, expliquant ainsi le résultat.
// Mais évidemment, ce n'est pas ce qui était prévu.)
```

La capacité à différencier les données, les calculs et les actions dans votre programme est une compétence fondamentale à développer.

### Mapping

Le mapping est un concept assez trivial mais très important dans le monde de la programmation fonctionnelle.

"Mapping de A à B" signifie aller de A à B via une certaine association.

En d'autres termes, A pointe vers B par un certain lien entre eux.

Par exemple, une fonction pure mappe une entrée à une sortie. Nous pouvons l'écrire comme ceci : entrée --> sortie ; où la flèche indique une fonction.

Un autre exemple sont les objets en JavaScript. Ils mappent les clés aux valeurs.

Dans d'autres langages, cette structure de données est souvent appelée "map" ou "hash-map", ce qui est plus explicatif.

Comme le suggère ce dernier terme, ce qui se passe en coulisses est que chaque clé est liée à sa valeur via une fonction de _hachage_. La clé est passée à la fonction de _hachage_ qui retourne l'index de la valeur correspondante dans le tableau qui les stocke toutes.

Sans entrer dans plus de détails, je voulais introduire ce terme car je l'utiliserai tout au long de cet article.

### Plus sur les effets secondaires

Avant de continuer, je veux approfondir les effets secondaires en JavaScript et montrer un piège vicieux dont vous n'êtes peut-être pas conscient.

Pour nous rappeler, dire qu'une fonction a des effets secondaires revient à dire : "Lorsque cette fonction s'exécute, quelque chose en dehors de sa portée va changer."

Comme je l'ai dit, cela peut être la journalisation dans la console, l'appel à une API, la modification d'une variable externe, etc.

Regardons un exemple de ce dernier :

```js
let y;

const f = (x) => {
  y = x * x;
};

f(5);
y; // 25
```

C'est assez facile à comprendre.

Lorsque `f` s'exécute, elle assigne une nouvelle valeur à la variable externe `y`, ce qui est un effet secondaire.

Une version pure de cet exemple serait :

```js
const f = (x) => x * x;

const y = f(5);
// 25
```

Mais il y a une autre façon de changer une variable externe qui est plus subtile :

```js
let myArr = [1, 2, 3, { key: "value" }, "a string", 4];

const g = (arr) => {
  let total = 0;

  for (let i = 0; i < arr.length; i++) {
    if (Number.isNaN(Number(arr[i]))) {
      arr[i] = 0;
    }
    total += arr[i];
  }

  return total;
};

g(myArr);
// 10
myArr;
// [1, 2, 3, 0, 0, 4]
// Oups, tous les éléments qui n'étaient pas des nombres ont été changés en 0 !
```

Pourquoi cela ?

En JavaScript, lors de l'assignation d'une valeur à une variable ou de son passage à une fonction, elle est automatiquement copiée.

Mais il y a une distinction à faire ici.

Les **valeurs primitives** (`null`, `undefined`, chaînes de caractères, nombres, booléens et symboles) sont toujours assignées/passées par **copie de valeur**.

En revanche, les **valeurs composées** comme les objets, les tableaux et les fonctions (d'ailleurs, les tableaux et les fonctions sont des objets en JavaScript, mais je ne les désigne pas comme des objets pour plus de clarté) créent une copie par **référence** lors de l'assignation ou du passage.

Ainsi, dans l'exemple précédent, la valeur passée à `g` est une valeur composée, le tableau `myArr`.

Ce qui se passe, c'est que `g` stocke l'adresse mémoire de `myArr` dans `arr`, le nom du paramètre utilisé dans le corps de la fonction.

En d'autres termes, il n'y a pas de copie de valeur de chaque élément dans `myArr` comme vous pourriez vous y attendre. Ainsi, lorsque vous manipulez ou changez `arr`, il va en fait à l'emplacement mémoire de `myArr` et effectue les calculs que vous avez spécifiés.

Donc oui, soyez conscient de cette particularité.

### Exercices (Set 1)

1. Dans l'extrait ci-dessous, trouvez les fonctions pures et les impures :

```js
// a
const capitalizeFirst = (str) => str.charAt(0).toUpperCase() + str.slice(1);

// b
const greeting = (persons) => {
  persons.forEach((person) => {
    const fullname = `${capitalizeFirst(person.firstname)} ${capitalizeFirst(
      person.lastname
    )}`;

    console.log(`Hello ${fullname} !`);
  });
};

// c
const getLabels = async (endpoint) => {
  const res = await fetch("https://my-database-api/" + endpoint);
  const data = await res.json();
  return data.labels;
};

// d
const counter = (start, end) => {
  return start === end
    ? "End"
    : // e
      () => counter(start + 1, end);
};
```

2. Convertissez cet extrait en une version pure (vous pouvez faire plus d'une fonction si vous en ressentez le besoin) :

```js
const people = [
  { firstname: "Bill", lastname: "Harold", age: 54 },
  { firstname: "Ana", lastname: "Atkins", age: 42 },
  { firstname: "John", lastname: "Doe", age: 57 },
  { firstname: "Davy", lastname: "Johnson", age: 34 },
];

const parsePeople = (people) => {
  const parsedPeople = [];

  for (let i = 0; i < people.length; i++) {
    people[i].firstname = people[i].firstname.toUpperCase();
    people[i].lastname = people[i].lastname.toUpperCase();
  }

  const compareAges = (person1, person2) => person1.age - person2.age;

  return people.sort(compareAges);
};

parsePeople(people);
// [
//   {firstname: "DAVY", lastname: "JOHNSON", age: 34},
//   {firstname: "ANA", lastname: "ATKINS", age: 42},
//   {firstname: "BILL", lastname: "HAROLD", age: 54},
//   {firstname: "JOHN", lastname: "DOE", age: 57},
// ]
```

[Vérifier les réponses](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#set-1).

## Immuabilité

Comme nous l'avons vu précédemment, un effet secondaire courant est de muter une variable.

Vous ne voulez pas faire cela en programmation fonctionnelle. Donc une caractéristique importante d'un programme fonctionnel est l'**immuabilité** des données.

Dans les langages fonctionnels comme Clojure et Haskell, cette fonctionnalité est intégrée – vous n'avez aucun moyen de muter les données sauf si le langage le permet. Dans tous les cas, vous devez choisir consciemment de le faire.

Mais en JavaScript, ce n'est pas le cas.

Donc, il s'agit davantage d'avoir l'état d'esprit "immuabilité" qu'une réelle implémentation robuste de cette fonctionnalité.

Ce que cela signifie, c'est que vous allez essentiellement faire des copies des données avec lesquelles vous voulez travailler.

Dans la première section, nous avons vu que les fonctions JavaScript copient automatiquement les arguments passés. Alors que les valeurs primitives sont copiées par valeur, les valeurs composées ne sont copiées que par référence, donc il est toujours possible de les muter.

Ainsi, lorsque vous travaillez avec un objet/tableau dans une fonction, vous devriez faire une copie et ensuite opérer dessus.

Au fait, remarquez que certaines fonctions intégrées ne mutent pas la valeur sur laquelle elles sont appelées, tandis que d'autres le font.

Par exemple, [Array.prototype.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map), [Array.prototype.filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter), ou [Array.prototype.reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) ne mutent pas le tableau original.

D'autre part, [Array.prototype.reverse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse) et [Array.prototype.push](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push) mutent le tableau original.

Vous pouvez découvrir si une fonction intégrée mute la valeur sur laquelle elle est appelée ou non dans la documentation, alors consultez-la si vous n'êtes pas sûr.

C'est ennuyeux, et finalement pas parfaitement sûr.

### Copies superficielles vs. copies profondes

Depuis ES6, il est facile de faire des copies d'objets/tableaux via la notation de décomposition, [`Array.from()`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Array/from), [`Object.assign()`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Object/assign).

Par exemple :

```js
// tableaux
const fruits = ["apple", "strawberry", "banana"];
const fruitsCopy = [...fruits];
fruitsCopy[0] = "mutation";
// fruitsCopy: ['mutation', 'strawberry', 'banana']
// fruits (non muté): ['apple', 'strawberry', 'banana']

// objets
const obj = { a: 1, b: 2, c: 3 };
const objCopy = { ...obj };
objCopy.a = "mutation";
// objCopy: {a: "mutation", b: 2, c: 3}
// obj (non muté): {a: 1, b: 2, c: 3}
console.log(obj);
console.log(objCopy);
```

C'est cool mais il y a un piège.

Les tableaux/objets étendus n'ont que leur premier niveau copié par valeur, également connu sous le nom de copie **superficielle**.

Ainsi, tous les niveaux suivants sont toujours mutables :

```js
// Mais avec des objets/tableaux imbriqués, cela ne fonctionne pas
const nestedObj = { a: { b: "canBeMutated" } };
const nestedObjCopy = { ...nestedObj };
nestedObjCopy.a.b = "hasBeenMutated!";
console.log(nestedObj);
console.log(nestedObjCopy);
// nestedObjCopy: {a: {b: "hasBeenMutated!"}}}
// nestedObj (muté): {a: {b: "hasBeenMutated!"}}
```

Pour résoudre ce problème, nous avons besoin d'une fonction personnalisée pour faire des copies **profondes**. Cet [article](https://medium.com/javascript-in-plain-english/how-to-deep-copy-objects-and-arrays-in-javascript-7c911359b089) discute de plusieurs solutions.

Voici une version abrégée de la fonction personnalisée proposée dans cet article :

```js
// fonctionne pour les tableaux et les objets
const deepCopy = (obj) => {
  if (typeof obj !== "object" || obj === null) {
    return obj; // Retourne la valeur si obj n'est pas un objet
  }

  // Crée un tableau ou un objet pour contenir les valeurs
  let newObj = Array.isArray(obj) ? [] : {};

  for (let key in obj) {
    // Copie récursive (profonde) pour les objets imbriqués, y compris les tableaux
    newObj[key] = deepCopy(obj[key]);
  }

  return newObj;
};

const nestedObj = {
  lvl1: { lvl2: { lvl3: { lvl4: "tryToMutateMe" } } },
  b: ["tryToMutateMe"],
};
const nestedObjCopy = deepCopy(nestedObj);

nestedObjCopy.lvl1.lvl2.lvl3.lvl4 = "mutated";
nestedObjCopy.b[0] = "mutated";

console.log(nestedObj);
// { lvl1: { lvl2: { lvl3: { lvl4: "tryToMutateMe" } } }, b: ["tryToMutateMe"]}
console.log(nestedObjCopy);
// { lvl1: { lvl2: { lvl3: { lvl4: "mutated" } } }, b: ["mutated"]}
```

Si vous utilisez déjà une bibliothèque qui fournit des utilitaires fonctionnels, il est probable qu'elle en ait un pour faire des copies profondes. Personnellement, j'aime [Ramda](https://ramdajs.com). Voir sa fonction [clone](https://ramdajs.com/docs/#clone).

Si la différence entre les copies superficielles et profondes n'est toujours pas claire, consultez [ceci](https://medium.com/@manjuladube/understanding-deep-and-shallow-copy-in-javascript-13438bad941c).

Maintenant, parlons de performance.

Évidemment, faire des copies n'est pas sans coût.

Pour les parties sensibles à la performance du programme, ou dans les cas où les changements se produisent fréquemment, créer un nouveau tableau ou objet (surtout s'il contient beaucoup de données) est indésirable pour des raisons de traitement et de mémoire.

Dans ces cas, l'utilisation de structures de données immuables d'une bibliothèque comme [Immutable.js](https://immutable-js.github.io/immutable-js/) est probablement une meilleure idée.

Ils utilisent une technique appelée **partage structurel** dont j'ai parlé lorsque j'ai abordé les inconvénients de la PF plus tôt dans cet article.

Consultez cette excellente [conférence](https://www.youtube.com/watch?v=I7IdS-PbEgI&list=PLts8-qGf74Q5QfIkOPGqwO_7d1ljMWa8p&index=22&t=0s) pour en savoir plus.

Travailler avec des données immuables est donc, à mon avis, la deuxième compétence à avoir dans votre boîte à outils de programmeur fonctionnel.

## Composition et Currying

### Composition

Sans surprise, les éléments de base fondamentaux d'un programme fonctionnel sont les fonctions.

Parce que vos fonctions sont exemptes d'effets secondaires et considérées comme de première classe, nous pouvons les composer.

Comme je l'ai dit, _première classe_ signifie qu'elles sont traitées comme des structures de données régulières, pouvant éventuellement être assignées à des variables, passées en arguments, ou retournées par d'autres fonctions.

La composition est une idée puissante.

À partir de petites fonctions, vous pouvez additionner leurs fonctionnalités pour en former une plus complexe, mais sans la douleur de la mettre en place d'emblée.

De plus, vous obtenez une plus grande flexibilité car vous pouvez facilement réorganiser vos compositions.

Soutenues par des lois mathématiques, nous savons que tout fonctionnera si nous les suivons.

Introduisons un peu de code pour concrétiser les choses :

```js
const map = (fn, arr) => arr.map(fn);

const first = (xs) => xs[0];

const formatInitial = (x) => x.toUpperCase() + ".";

const intercalate = (sep, arr) => arr.join(sep);

const employees = ["Yann", "Brigitte", "John", "William"];

const initials = intercalate("\n", map(formatInitial, map(first, employees)));
// Y.
// B.
// J.
// W.
```

Aïe – il y a un peu d'imbrication ici.

Prenez le temps de comprendre ce qui se passe. Comme vous pouvez le voir, il y a des appels de fonctions passés en arguments à des fonctions externes.

Avec le pouvoir de `map`, nous avons essentiellement composé les fonctionnalités de `first`, `formatInitial`, et `join` pour finalement les appliquer sur le tableau `employees`.

Plutôt cool !

Mais comme vous pouvez le voir, l'imbrication est ennuyeuse. Cela rend les choses plus difficiles à lire.

### Currying

Pour aplatir tout cela et rendre la composition un jeu d'enfant, nous devons parler de **currying**.

Ce terme peut vous faire peur, mais ne vous inquiétez pas, ce n'est que du jargon pour une idée simple : alimenter une fonction avec un argument à la fois.

Habituellement, lorsque nous faisons un appel de fonction, nous fournissons tous les arguments à la fois et obtenons le résultat :

```js
const add = (x, y) => x + y;

add(3, 7);
// 10
```

Mais que se passerait-il si nous pouvions passer un seul argument et fournir le second plus tard ?

Eh bien, nous pouvons le faire en curryant `add` comme ceci :

```js
const add = (x) => (y) => x + y;

const addTo3 = add(3);
// (y) => 3 + y

// ...plus tard
addTo3(7);
// 10
```

Cela peut être utile si nous n'avons pas encore tous les arguments.

Vous ne comprenez peut-être pas pourquoi nous n'aurions pas tous les arguments à l'avance, mais vous verrez plus tard.

Grâce aux fermetures, nous préchargeons la fonction avec ses arguments étape par étape jusqu'à ce que nous l'exécutions finalement.

Si vous avez du mal à saisir le concept de fermeture, consultez [ceci](https://www.youtube.com/watch?v=CQqwU2Ixu-U), puis [ceci](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch7.md#chapter-7-using-closures) pour approfondir.

En bref, la fermeture permet à une fonction interne d'accéder aux variables de la portée d'une fonction externe. C'est pourquoi nous pouvons accéder à `x` dans la portée de `addTo3` qui provient de la portée externe, `add`.

Souvent, vous ne voulez pas vous embêter à écrire vos fonctions sous cette forme spéciale. De plus, vous ne pouvez pas toujours les écrire de cette manière, par exemple, lorsque vous utilisez des fonctions de bibliothèque externe et virtuellement tout ce que vous n'écrivez pas mais utilisez tout de même.

Pour cette raison, il existe un helper commun pour curryer une fonction ([du livre de Kyle Simpson YDKJS](https://github.com/getify/Functional-Light-JS/blob/master/manuscript/ch3.md/#currying-more-than-one-argument)) :

```js
const curry = (fn, arity = fn.length) => {
  return (function nextCurried(prevArgs) {
    return function curried(...nextArgs) {
      const args = [...prevArgs, ...nextArgs];

      return args.length < arity ? nextCurried(args) : fn(...args);
    };
  })([]);
};
```

`curry` prend une fonction et un nombre appelé **arity** (optionnel).

L'arité d'une fonction est le nombre d'arguments qu'elle prend.

Dans le cas de `add`, c'est 2.

Nous avons besoin de cette information pour savoir quand tous les arguments sont présents, et ainsi décider d'exécuter la fonction ou de retourner une autre fonction curryée qui prendra les arguments restants.

Alors, refactorisons notre exemple avec `add` :

```js
const add = curry((x, y) => x + y);

const addTo3 = add(3);

addTo3(7);
// 10
```

Ou nous pouvons encore appeler `add` avec tous ses arguments directement :

```js
const add = curry((x, y) => x + y);

add(3, 7);
// 10
```

### Application partielle

En fait, _curried_ signifie strictement "prend un argument à la fois", pas plus, pas moins.

Lorsque nous pouvons fournir le nombre d'arguments que nous voulons, nous parlons en fait d'**application partielle**.

Ainsi, le currying est une forme contrainte d'application partielle.

Regardons un exemple plus explicite d'application partielle par rapport au currying :

```js
const listOf4 = curry((a, b, c, d) => `1. ${a}\n2. ${b}\n3. ${c}\n4. ${d}`);

// currying strict

const a = listOf4("First")("Second")("Third")("Fourth");
// ou
const b = listOf4("First");
// plus tard
const c = b("Second")("Third");
// plus tard
const d = c("Fourth");

// application partielle

const e = listOf4("First", "Second", "Third", "Fourth");
// ou
const b = listOf4("First");
// plus tard
const c = b("Second", "Third");
// plus tard
const d = c("Fourth");
```

Voyez-vous la différence ?

Avec le currying, vous devez fournir un argument à la fois. Si vous voulez alimenter plus d'un argument, alors vous devez faire un nouvel appel de fonction, d'où la paire de parenthèses autour de chaque argument.

Franchement, ce n'est qu'une question de style.

Cela semble un peu maladroit lorsque vous n'y êtes pas habitué, mais d'un autre côté, certaines personnes trouvent le style d'application partielle désordonné.

L'aide `curry` que j'ai introduite vous permet de faire les deux.

Elle étire la définition réelle du currying, mais je préfère avoir les deux fonctionnalités et n'aime pas le nom `looseCurry` que Kyle Simpson a utilisé dans son livre. Donc, j'ai un peu triché.

Gardez simplement les différences à l'esprit et soyez conscient que les aides `curry` que vous trouvez dans les bibliothèques suivent probablement la définition stricte.

### Les données viennent en dernier

Un dernier point que je veux souligner est que nous plaçons généralement les données comme dernier argument.

Avec les fonctions précédentes que j'ai utilisées, ce n'est pas évident car tous les arguments sont des données. Mais regardez ceci :

```js
const replace = curry((regex, replacement, str) =>
  str.replace(regex, replacement)
);
```

Vous pouvez voir que les données (`str`) sont dans la dernière position car c'est probablement la dernière chose que nous voudrons passer.

Vous verrez que c'est le cas lors de la composition de fonctions.

### Rassembler le tout

Maintenant, pour tirer parti du currying et aplatir notre imbrication précédente, nous avons également besoin d'un helper pour la composition.

Vous l'avez deviné, il s'appelle `compose` ! :

```js
const compose = (...fns) =>
  fns.reverse().reduce((fn1, fn2) => (...args) => fn2(fn1(...args)));
```

`compose` prend des fonctions comme arguments et retourne une autre fonction qui prend les argument(s) à passer à travers tout le pipeline.

Les fonctions sont appliquées de droite à gauche à cause de `fns.reverse()`.

Parce que `compose` retourne une fonction qui prend les futur(s) argument(s), nous pouvons librement associer nos fonctions sans les appeler, ce qui nous permet de créer des fonctions intermédiaires.

Alors avec notre exemple initial :

```js
const map = (fn, arr) => arr.map(fn);

const first = (xs) => xs[0];

const formatInitial = (x) => x.toUpperCase() + ".";

const intercalate = (sep, arr) => arr.join(sep);

const getInitials = compose(formatInitial, first);

const employees = ["Yann", "Brigitte", "John", "William"];

const initials = intercalate("\n", map(getInitials, employees));
// Y.
// B.
// J.
// W.
```

`first` et `formatInitial` prennent déjà un argument.

Mais `map` et `intercalate` prennent 2 arguments, donc nous ne pouvons pas les inclure tels quels dans notre helper `compose` car un seul argument sera passé. Dans ce cas, il s'agit d'un tableau que les deux prennent comme argument final (rappelons que les données sont la dernière chose à être passée).

Il serait bien de donner à `map` et `intercalate` leur premier argument respectif à l'avance.

Attendez une minute – nous pouvons les curryer ! :

```js
// ...

const map = curry((fn, arr) => arr.map(fn));

const intercalate = curry((sep, arr) => arr.join(sep));

const formatInitials = compose(
  intercalate("\n"),
  map(formatInitial),
  map(first)
);

const employees = ["Yann", "Brigitte", "John", "William"];

const initials = formatInitials(employees);
// Y.
// B.
// J.
// W.
```

Si propre !

Comme je l'ai dit, `compose` crée un pipeline avec les fonctions que nous lui donnons, les appelant de droite à gauche.

Alors, visualisons ce qui se passe lorsque `formatInitials(employees)` est analysé :

![compose pipeline](https://www.freecodecamp.org/news/content/images/2020/08/compose-1.png)

Personnellement, je préfère lorsque cela va de gauche à droite, car lors de l'écriture de la fonction, j'aime penser à quelle transformation appliquer en premier, l'écrire, puis répéter jusqu'à la fin du pipeline.

Alors qu'avec `compose`, je dois reculer pour écrire la transformation suivante. Cela brise simplement le flux de ma pensée.

Heureusement, ce n'est pas compliqué de le modifier pour aller de gauche à droite.

Nous devons simplement nous débarrasser de la partie `.reverse()`.

Appelons notre nouvel helper `pipe` :

```js
const pipe = (...fns) => fns.reduce((fn1, fn2) => (...args) => f2(f1(...args)));

```

Alors, si nous refactorisons l'extrait précédent, nous obtenons :

```js
const formatInitials = pipe(map(first), map(formatInitial), intercalate("\n"));

```

Pour la visualisation, même chose que `compose` mais dans l'ordre inverse :

![pipe pipeline](https://www.freecodecamp.org/news/content/images/2020/08/pipe.png)

## Signatures de type Hindley-Milner

Comme vous le savez, un programme complet se termine avec pas mal de fonctions.

Lorsque vous replongez dans un projet après plusieurs semaines, vous n'avez pas le contexte pour comprendre facilement ce que fait chaque fonction.

Pour contrer cela, vous relisez seulement les parties dont vous avez besoin. Mais cela peut être assez fastidieux.

Il serait bien d'avoir un moyen rapide et puissant de documenter vos fonctions et d'expliquer ce qu'elles font en un coup d'œil.

C'est là que les signatures de type entrent en jeu. Elles sont un moyen de documenter comment une fonction opère et ses entrées et sorties.

Par exemple :

```js
//  nom de la fonction
//                   entrée
//                             sortie
// formatInitial :: String -> String
const formatInitial = (x) => x.toUpperCase() + ".";
```

Ici, nous voyons que `formatInitial` prend un `String` et retourne un `String`.

Nous ne nous soucions pas de l'implémentation.

Regardons un autre exemple :

```js
// first :: [a] -> a
const first = (xs) => xs[0];

```

Les types peuvent être exprimés avec des variables (généralement `a`, `b`, etc.) et les crochets signifient "un tableau de" ce qui est à l'intérieur.

Ainsi, nous pourrions littéralement lire cette signature comme ceci :

`first` prend un tableau de `a` et retourne un `a`, où `a` peut être de n'importe quel type.

Mais parce que le type pris en entrée est le même que celui retourné en sortie, nous utilisons la même variable.

Si la sortie avait un autre type, nous aurions utilisé `b` :

```js
// imaginaryFunction :: a -> b

```

Attention !

Cela ne garantit pas que `a` et `b` sont des types différents. Ils peuvent encore être les mêmes.

Enfin, regardons le cas de `intercalate` qui est un peu plus complexe :

```js
// intercalate :: String -> [a] -> String
const intercalate = curry((sep, arr) => arr.join(sep));

```

OK, ici il y a 2 flèches, qui peuvent être remplacées par "retourne...".

Elles indiquent des fonctions.

Ainsi, `intercalate` prend un `String` puis retourne une fonction qui prend un tableau de `a`, qui retourne un `String`.

Wow, c'est difficile à suivre.

Nous aurions pu écrire la signature comme ceci :

```js
// intercalate :: String -> ([a] -> String)

```

Maintenant, il est plus évident qu'elle retourne d'abord une fonction, qui est entre parenthèses ici. Et ensuite, cette fonction prendra `[a]` comme entrée et retournera `String`.

Mais nous n'utilisons généralement pas les parenthèses pour des raisons de clarté. En gros, si vous tombez sur une signature de la forme :

```js
// imaginaryFunction :: a -> b -> c -> d -> e

// ou

// imaginaryFunction :: a -> (b -> (c -> (d -> e)))

// ...vous voyez comment l'imbrication des parenthèses affecte la lisibilité

```

`e`, le type du côté droit, est la sortie.

Et tout ce qui précède sont des entrées données une par une, ce qui indique que la fonction est curryée.

De nos jours, nous avons généralement des systèmes de types comme TypeScript ou Flow, et l'IDE est capable de nous donner la signature de type d'une fonction lorsque nous survolons son nom. Ainsi, il peut être inutile de les écrire en commentaires dans votre code.

Mais cela reste un bel outil à avoir dans votre boîte à outils car beaucoup de bibliothèques fonctionnelles utilisent ces signatures de type dans leur documentation. Et les langages fonctionnels idiomatiques (comme Haskell) les utilisent abondamment.

Alors, si vous leur donnez une chance, vous ne serez, espérons-le, pas complètement perdu.

Félicitez-vous d'avoir lu jusqu'ici.

Vous devriez maintenant avoir la capacité de travailler avec des fonctions d'ordre supérieur. Les fonctions d'ordre supérieur sont simplement des fonctions qui prennent des fonctions en entrées et/ou les retournent.

En effet, c'est exactement ce que nous avons fait.

Par exemple, `curry` est une fonction d'ordre supérieur car elle prend une fonction en entrée et en retourne une en sortie.

`compose`, `pipe`, `map` et `reduce` sont toutes des fonctions d'ordre supérieur car elles prennent au moins une fonction en entrée.

Elles sont plutôt cool car elles permettent de créer des abstractions très puissantes.

Assez de bavardages. Mettons-nous à la pratique.

### Exercices (Set 2)

1. Étant donné une chaîne de la forme :

```js
const input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

```

...et ces helpers :

```js
// filter :: (a -> Boolean) -> [a] -> [a]
const filter = curry((fn, arr) => arr.filter(fn));

// removeDuplicates :: [a] -> [a]
const removeDuplicates = (arr) => Array.from(new Set(arr));

// getChars :: String -> [Character]
const getChars = (str) => str.split("");

// lowercase :: String -> String
const lowercase = (str) => str.toLowerCase();

// sort :: [a] -> [a]
const sort = (arr) => [...arr].sort();
```

Créez une fonction `getLetters` qui retourne toutes les lettres d'une chaîne sans doublons, dans l'ordre alphabétique, et en minuscules.

Le but est d'utiliser `compose` et/ou `pipe` :

```js
// getLetters :: String -> [Character]
const getLetters = ...

```

Note : Vous devrez peut-être créer des fonctions intermédiaires avant la fonction finale.

2. Imaginez que vous avez un objet avec des noms de groupes comme clés et des tableaux d'objets représentant des personnes comme valeurs :

```js
{
  "groupName": [
    {firstname: "John", lastname: "Doe", age: 35, sex: "M"},
    {firstname: "Maria", lastname: "Talinski", age: 28, sex: "F"},
    // ...
  ],
  // ...
}

```

Créez une fonction qui retourne un objet de la forme :

```js
{
  "groupName": {
    "medianAgeM": 34,
    "medianAgeF": 38,
  },
  // ...
}

```

Où `medianAgeM` est l'âge médian des hommes dans le groupe et `medianAgeF` celui des femmes.

Voici quelques helpers :

```js
// map :: (a -> b) -> [a] -> [b]
const map = curry((fn, arr) => arr.map(fn));

// getEntries :: Object -> [[Key, Val]]
const getEntries = (o) => Object.entries(o);

// fromEntries:: [[Key, Val]] -> Object
const fromEntries = (entries) => Object.fromEntries(entries);

// mean :: Number -> Number -> Number
const mean = curry((x, y) => Math.round((x + y) / 2));

// reduceOverVal :: (b -> a -> b) -> b -> [Key, [a]] -> [Key, b]
const reduceOverVal = curry((fn, initVal, entry) => [
  entry[0],
  entry[1].reduce(fn, initVal),
]);
```

Vous devrez peut-être créer des fonctions intermédiaires avant la fonction finale, et comme avant, essayez d'utiliser `compose` et `pipe` :

```js
// groupsMedianAges :: Object -> Object
const groupsMedianAges = ...

```

3. Trouvez la signature de type de `reduce` :

```js
const reduce = curry((fn, initVal, arr) => arr.reduce(fn, initVal));
```

4. Trouvez la signature de type de `curry` :

```js
const curry = (fn, arity = fn.length) => {
  return (function nextCurried(prevArgs) {
    return function curried(...nextArgs) {
      const args = [...prevArgs, ...nextArgs];

      return args.length < arity ? nextCurried(args) : fn(...args);
    };
  })([]);
};
```

[Vérifier les réponses](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#set-2).

## Travailler avec des boîtes : des Functors aux Monads

Vous êtes peut-être déjà stressé par le titre de cette section. Vous pensez peut-être : "Qu'est-ce que 'Functors' et 'Monads' ?"

Ou peut-être avez-vous entendu parler des monads parce qu'ils sont célèbrement "difficiles" à comprendre.

Malheureusement, je ne peux pas prédire que vous comprendrez définitivement ces concepts, ou que vous les appliquerez efficacement dans le travail que vous faites.

En fait, si je parle d'eux à la fin de ce tutoriel, c'est parce que je pense qu'ils sont des outils très puissants dont nous n'avons pas souvent besoin.

Voici la partie rassurante : Comme tout dans le monde, ils ne sont pas magiques.

Ils suivent les mêmes règles de la physique (et plus spécifiquement de l'informatique et des mathématiques) que tout le reste.

Donc, à la fin de la journée, ils sont compréhensibles. Cela nécessite simplement la bonne quantité de temps et d'énergie.

De plus, ils s'appuient essentiellement sur ce dont nous avons parlé précédemment : les types, le mapping et la composition.

Maintenant, trouvez ce tube de _persévérance_ dans votre boîte à outils et commençons.

### Pourquoi utiliser des boîtes ?

Nous voulons faire notre programme avec des fonctions pures. Ensuite, nous utilisons la composition pour spécifier dans quel ordre les exécuter sur les données.

Cependant, comment traitons-nous `null` ou `undefined` ? Comment traitons-nous les exceptions ?

De plus, comment gérons-nous les effets secondaires sans perdre le contrôle, car un jour nous devrons les effectuer ?

Les deux premiers cas impliquent des branchements. Soit la valeur est `null` et nous faisons ceci, soit nous faisons cela. Soit il y a une erreur et nous faisons ceci, soit un succès et nous faisons cela.

La manière habituelle de traiter les branchements est le flux de contrôle.

Cependant, le flux de contrôle est impératif. Il décrit "comment" le code fonctionne.

Ainsi, les programmeurs fonctionnels ont eu l'idée d'utiliser une boîte qui contient une des deux valeurs possibles.

Nous utilisons cette boîte comme entrée/sortie pour les fonctions, indépendamment de ce qu'elle contient.

Mais parce que ces boîtes ont également des comportements spécifiques qui abstraient l'application de la fonction, nous pouvons appliquer une fonction sur une boîte et elle décidera comment l'exécuter réellement en fonction de sa valeur interne.

Ainsi, nous n'avons pas à adapter nos fonctions aux données. Nous n'avons pas à les encombrer avec une logique qui ne leur appartient pas.

Des choses comme :

```js
const myFunc = (x) => {
  // ...
  if (x !== null) {
    // ...
  } else {
    // ...
  }
};
```

Avec cela, nous pouvons implémenter des branchements (et d'autres choses) tout en utilisant uniquement des fonctions et préserver la composition.

Les boîtes que nous verrons, nommées **Algebraic Data Types** (ADT), nous permettent de faire plus tout en gardant les données et les fonctions séparées.

Les Functors et les monads sont effectivement des Algebraic Data Types.

### Functors

Les Functors sont des conteneurs/structures de données/types qui contiennent des données ainsi qu'une méthode `map`.

Cette méthode `map` nous permet d'appliquer une fonction sur la ou les valeurs contenues dans le functor. Ce qui est retourné est le même functor mais contenant le résultat de l'appel de la fonction.

Introduisons `Identity`, le functor le plus simple :

Nous aurions pu l'implémenter avec une classe, mais j'utiliserai des fonctions régulières ici :

```js
const Identity = (x) => ({
  inspect: () => `Identity(${x})`,
  map: (fn) => Identity(fn(x)),
  value: x,
});

// add5 :: Number -> Number
const add5 = (x) => x + 5;

const myFirstFunctor = Identity(1);

myFirstFunctor.map(add5);
// Identity(6)
```

Vous voyez ? Pas si compliqué !

`Identity` est l'équivalent de la fonction `identity` mais dans le monde des functors.

`identity` est une fonction bien connue en PF qui peut sembler inutile au premier abord :

```js
// identity :: a -> a
const identity = (x) => x;

```

Elle ne fait rien sur les données, elle les retourne simplement telles quelles.

Mais elle peut être utile lorsque l'on fait des choses comme la composition car parfois, vous ne voulez rien faire avec les données, juste les faire passer.

Et parce que la composition fonctionne avec des fonctions et non des valeurs brutes, vous devez les envelopper dans la fonction `identity`.

`Identity` sert le même but mais lors de la composition de functors.

Plus sur cela plus tard.

En revenant à l'extrait précédent, nous aurions pu faire `map(add5, 1)` et cela nous aurait donné le même résultat à part le fait qu'il n'y aurait pas eu de conteneur autour.

Donc, il n'y a pas de fonctionnalité supplémentaire ici.

Maintenant, voyons un autre functor appelé `Maybe` :

```js
const Nothing = () => ({
  inspect: () => `Nothing()`,
  map: Nothing,
});

const Maybe = { Just, Nothing };

// Just est équivalent à Identity
```

`Maybe` est un mélange de 2 functors, `Just` et `Nothing`.

`Nothing` contient, eh bien, rien. Mais c'est toujours un functor donc nous pouvons l'utiliser partout où nous avons besoin de functors.

`Maybe`, comme son nom le suggère, _peut_ contenir une valeur (`Just`) ou non (`Nothing`).

Maintenant, comment l'utiliserions-nous ?

La plupart du temps, il est utilisé dans des fonctions qui peuvent retourner `null` ou `undefined` :

```js
// isNothing :: a -> Boolean
const isNothing = (x) => x === null || x === undefined;

// safeProp :: String -> Object -> Maybe a
const safeProp = curry((prop, obj) =>
  isNothing(obj[prop]) ? Maybe.Nothing() : Maybe.Just(obj[prop])
);

const o = { a: 1 };

const a = safeProp("a", o);
// Just(1)

const b = safeProp("b", o);
// Nothing

a.map(add5);
// Just(6)

b.map(add5);
// Nothing
```

Voyez-vous où réside la puissance de `Maybe` ?

Vous pouvez appliquer en toute sécurité une fonction sur la valeur interne dans n'importe quel functor que `safeProp` retourne, vous n'obtiendrez pas un résultat `NaN` inattendu parce que vous avez ajouté un nombre avec `null` ou `undefined`.

Grâce au functor `Nothing`, la fonction mappée ne sera pas appelée du tout.

Cependant, les implémentations de `Maybe` trichent souvent un peu en faisant la vérification `isNothing` à l'intérieur du monad, alors qu'un monad strictement pur ne devrait pas :

```js
const Maybe = (x) => ({
  map: (fn) => (x === null || x === undefined ? Maybe(x) : Maybe(fn(x))),
  inspect: () => `Maybe(${x})`,
  value: x,
});

// safeProp :: String -> Object -> Maybe a
const safeProp = curry((prop, obj) => Maybe(obj[prop]));

const o = { a: 1 };

const c = safeProp("a", o);
// Maybe(1)

const d = safeProp("b", o);
// Maybe(undefined)

c.map(add5);
// Maybe(6)

d.map(add5);
// Maybe(undefined)
```

L'avantage d'avoir ces functors est que, pour être appelés "functors", ils doivent implémenter une interface spécifique, dans ce cas `map`.

Ainsi, chaque type de functor a des caractéristiques uniques tout en ayant des capacités partagées par tous les functors, ce qui les rend prévisibles.

Lorsque vous utilisez `Maybe` dans des cas réels, vous finissez par devoir faire quelque chose avec les données pour libérer la valeur.

De plus, si les opérations ont pris la branche non désirée et échouent, nous obtiendrons `Nothing`.

Imaginons que nous voulons imprimer la valeur récupérée de `o` dans notre exemple précédent.

Nous pourrions vouloir imprimer quelque chose de plus utile pour l'utilisateur que `"Nothing"` si l'opération a échoué.

Ainsi, pour libérer la valeur et fournir une solution de repli si nous obtenons `Nothing`, nous avons un petit helper appelé `maybe` :

```js
// maybe :: c -> (a -> b) -> Maybe a -> b | c
const maybe = curry((fallbackVal, fn, maybeFunctor) =>
  maybeFunctor.val === undefined ? fallbackVal : fn(maybeFunctor.val)
);

// ...

const o = { a: 1 };

const printVal1 = pipe(
  safeProp("a"),
  maybe("Failure to retrieve the value.", add5),
  console.log
);

const printVal2 = pipe(
  safeProp("b"),
  maybe("Failure to retrieve the value.", add5),
  console.log
);

printVal1(o);
// console: 6
printVal2(o);
// console: "Failure to retrieve the value."
```

Génial !

Si c'est la première fois que vous êtes exposé à ce concept, cela peut sembler peu clair et peu familier.

Mais en réalité, c'est quelque chose que vous connaissez déjà.

Si vous êtes familier avec JavaScript, il est probable que vous ayez utilisé le `map` intégré :

```js
[1, 2, 3].map((x) => x * 2);
// [2, 4, 6]

```

Eh bien, rappelez-vous la définition d'un functor. C'est une structure de données qui a une méthode `map`.

Maintenant, regardez l'extrait précédent : quelle est la structure de données qui a une méthode `map` ici ?

Le `Array` ! Le type natif `Array` en JavaScript est un functor !

Sa spécialité est qu'il peut contenir plusieurs valeurs. Mais l'essence de `map` reste la même : il prend une valeur en entrée et la retourne/mappe à une sortie.

Ainsi, dans ce cas, la fonction de mapping s'exécute pour chaque valeur.

Cool !

Maintenant que nous savons ce qu'est un functor, passons à l'extension de son interface.

### Pointed

Un functor pointé est celui qui a une méthode `of` (aka `pure`, `unit`).

Ainsi, avec `Maybe`, cela nous donne :

```js
const Maybe = {Just, Nothing, of: Just};

```

`of` est destiné à placer une valeur donnée dans le **contexte minimal par défaut** du functor.

Vous pourriez demander :

> Pourquoi `Just` et pas `Nothing` ?

Lorsque nous utilisons `of`, nous nous attendons à pouvoir mapper immédiatement.

Si nous utilisons `Nothing`, il ignorerait tout ce que nous mappons.

`of` s'attend à ce que vous insériez une valeur "réussie".

Ainsi, vous pouvez toujours vous tirer une balle dans le pied en insérant `undefined`, par exemple, puis en mappant une fonction qui n'attend pas cette valeur :

```js
Maybe.of(undefined).map((x) => x + 1);
// Just(NaN)

```

Introduisons un autre functor pour mieux comprendre quand il est utile :

```js
const IO = (dangerousFn) => ({
  inspect: () => `IO(?)`,
  map: (fn) => IO(() => fn(dangerousFn())),
});

IO.of = (x) => IO(() => x);
```

Contrairement à `Just`, `IO` ne reçoit pas une valeur telle quelle mais a besoin qu'elle soit enveloppée dans une fonction.

Pourquoi cela ?

_I/O_ signifie _Input/Output_.

Le terme est utilisé pour décrire tout programme, opération ou dispositif qui transfère des données vers ou depuis un ordinateur et vers ou depuis un périphérique.

Ainsi, il est destiné à être utilisé pour les opérations d'entrée/sortie, qui sont des effets secondaires car elles dépendent/affectent le monde extérieur.

Interroger le DOM en est un exemple :

```js
// getEl :: String -> DOM
const getEl = (sel) => document.querySelector(sel);

```

Cette fonction est impure car, pour une même entrée, elle peut retourner différentes sorties :

```js
getEl("#root");
// <div id="root"></div>

// ou

getEl("#root");
// <div id="root">There's text now !</div>

// ou

getEl("#root");
// null
```

Alors qu'en insérant une fonction intermédiaire, `getEl` retourne toujours la même sortie :

```js
// getEl :: String -> _ -> DOM
const getEl = (sel) => () => document.querySelector(sel);

getEl("#root");
// function...

```

Quels que soient les arguments passés, `getEl` retournera toujours une fonction, lui permettant d'être pure.

Cependant, nous n'effaçons pas magiquement l'effet car maintenant, c'est la fonction retournée qui est impure.

Nous obtenons la pureté grâce à la paresse.

La fonction externe ne sert que de boîte protectrice que nous pouvons passer en toute sécurité. Lorsque nous sommes prêts à libérer l'effet, nous appelons la fonction de la fonction retournée.

Et parce que nous voulons être prudents en le faisant, nous nommons la fonction `unsafePerformIO` pour rappeler au programmeur que c'est dangereux.

Jusqu'à présent, nous pouvons faire notre mapping et notre composition en toute tranquillité.

Ainsi, c'est le mécanisme utilisé par `IO`.

Si vous passez une valeur directement à `IO`, elle doit être une fonction avec la même signature que celle que `getEl` retourne :

```js
const a = IO(() => document.querySelector("#root"));

// et non :

const invalid = IO(document.querySelector("#root"));
```

Mais comme vous pouvez l'imaginer, il devient rapidement fastidieux de toujours envelopper notre valeur dans une fonction avant de la passer dans `IO`.

C'est là que `of` brille – il le fera pour nous :

```js
const betterNow = IO.of(document.querySelector("#root"));

```

C'est ce que je voulais dire par **contexte minimal par défaut**.

Dans le cas de `IO`, il enveloppe la valeur brute dans une fonction. Mais cela peut être autre chose, cela dépend du functor en question.

### Exercices (Set 3)

1. Écrivez une fonction `uppercaseF` qui met en majuscules une chaîne de caractères à l'intérieur d'un functor :

```js
// uppercaseF :: Functor F => F String -> F String
const uppercaseF = ...

```

2. Utilisez la fonction `uppercaseF` que vous avez construite précédemment, `maybe`, et `safeProp` pour créer une fonction qui récupère le nom d'un utilisateur et imprime une version en majuscules de celui-ci.

L'objet utilisateur a cette forme :

```js
{
  name: "Yann Salmon",
  age: 18,
  interests: ["Programming", "Sport", "Reading", "Math"],
  // ...
}

```

```js
// safeProp :: String -> Object -> Maybe a

// maybe :: c -> (a -> b) -> Maybe a -> b | c

// printUsername :: User -> _
const printUsername = ...

```

[Vérifier les réponses](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#set-3).

### Applicatives

Si vous travaillez avec des functors, vous rencontrerez des situations où vous avez plusieurs functors contenant des valeurs sur lesquelles vous aimeriez appliquer une fonction :

```js
// concatStr :: String -> String -> String
const concatStr = curry((str1, str2) => str1 + str2);

const a = Identity("Hello");

const b = Identity(" world !");
```

Malheureusement, nous ne pouvons pas passer des functors comme arguments à `concatStr` car il attend des chaînes de caractères.

L'interface `Applicative` résout ce problème.

Un functor qui l'implémente est celui qui implémente une méthode `ap`. `ap` prend un functor comme argument et retourne un functor du même type.

Dans le functor retourné, il y aura le résultat du mapping de la valeur du functor sur lequel `ap` a été appelé, sur la valeur du functor précédemment pris comme argument.

Je sais que c'est beaucoup à digérer. Prenez votre temps et laissez cela s'imprégner.

Continuons notre extrait précédent pour le voir en action :

```js
// concatStr :: String -> String -> String
const concatStr = curry((str1, str2) => str1 + str2);

const a = Identity("Hello");

const b = Identity(" world !");

const c = a.map(concatStr);
// Identity(concatStr("Hello", _))

const result = c.ap(b);
// Identity("Hello world !")
```

Tout d'abord, nous mappons `concatStr` sur `a`. Ce qui se passe, c'est que `concatStr("Hello")` est appelé et devient la valeur interne de `c`, toujours un functor `Identity`.

Et rappelez-vous, que retourne `concatStr("Hello")` ? Une autre fonction qui attend les arguments restants !

En effet, `concatStr` est curryé.

Notez que le currying est nécessaire afin d'utiliser cette technique.

Ensuite, comme je l'ai dit, `ap` mappe la valeur du functor sur lequel il est appelé (dans ce cas `c`, donc il mappe `concatStr("Hello")`) sur la valeur du functor pris comme argument (ici c'est `b` contenant `" world !"`).

Ainsi, `result` finit par être un functor `Identity` (même type que `b`) contenant le résultat de `concatStr("Hello")(" world !")`, c'est-à-dire `"Hello world !"` !

Voici l'implémentation :

```js
const Identity = (x) => ({
  inspect: () => `Identity(${x})`,
  // Interface Functor
  map: (fn) => Identity(fn(x)),
  // Interface Applicative
  ap: (functor) => functor.map(x),
  value: x,
});

// Interface Pointed
Identity.of = (x) => Identity(x);
```

Comme vous pouvez le voir, le functor sur lequel `ap` est appelé doit contenir une fonction. Sinon, cela ne fonctionnerait pas. Dans notre exemple précédent, c'était l'étape `c`.

Si nous mettons tout en ligne, nous obtenons :

```js
// concatStr :: String -> String -> String
const concatStr = curry((str1, str2) => str1 + str2);

const result = Identity("Hello").map(concatStr).ap(Identity(" world !"));
// Identity("Hello world !")
```

Il y a une propriété mathématique intéressante à propos de `ap` :

```js
F(x).map(fn) === F(fn).ap(F(x));

```

Le côté gauche de l'égalité correspond à ce que nous avons fait précédemment.

Ainsi, en suivant le côté droit, `result` pourrait également s'écrire comme ceci :

```js
const result = Identity(concatStr)
  .ap(Identity("Hello"))
  .ap(Identity(" world !"));
```

Prenez le temps de relire si vous vous sentez submergé.

La dernière version ressemble davantage à un appel de fonction régulier que la précédente. Nous alimentons `concatStr` avec ses arguments de gauche à droite :

![Chain of Applicative functors](https://www.freecodecamp.org/news/content/images/2020/08/applicatives.png)

Et tout cela se passe à l'intérieur de notre conteneur protecteur.

Enfin, nous pouvons encore nettoyer ce processus avec la paramétrisation.

Une fonction appelée `liftA2` fait cela :

```js
// liftA2 :: Apply functor F => (a -> b -> c) -> F a -> F b -> F c
const liftA2 = curry((fn, F1, F2) => F1.map(fn).ap(F2));

// ...

const result = liftA2(concatStr, Identity("Hello"), Identity(" world !"));
```

Je suis sûr que nous pouvons convenir que ce nom est vraiment maladroit.

Je suppose que cela avait du sens pour les pionniers de la programmation fonctionnelle, qui étaient probablement des "mathématiciens".

Mais de toute façon, vous pouvez penser à cela comme "soulever" une fonction et ses arguments, puis les mettre dans un functor afin d'`ap`pliquer chacun sur l'autre.

Cependant, cette métaphore n'est que partiellement vraie car les arguments sont déjà donnés dans leur conteneur.

La partie intéressante est le corps de la fonction.

Vous pouvez remarquer qu'il utilise le côté gauche de la propriété mathématique que nous avons vue plus tôt.

Si nous l'implémentons en utilisant le côté droit, nous devons savoir quel type de functor `F1` et `F2` sont car nous devons envelopper la fonction avec le même :

```js
const liftA2 = curry((fn, F1, F2) => F(fn).ap(F1).ap(F2));
//                                    qu'est-ce que F ? Nous avons besoin du constructeur précis.

```

Ainsi, en utilisant la version de gauche, nous abstraisons le type de functor gratuitement.

Maintenant, vous pourriez penser : "OK, mais que se passe-t-il si la fonction nécessite 3, 4, ou plus d'arguments ?"

Si c'est le cas, vous pouvez construire des variantes simplement en étendant notre précédent `liftA2` :

```js
// liftA3 :: Apply functor F => (a -> b -> c -> d) -> F a -> F b -> F c -> F d
const liftA3 = curry((fn, F1, F2, F3) => F1.map(fn).ap(F2).ap(F3));

// liftA4 :: Apply functor F => (a -> b -> c -> d -> e) -> F a -> F b -> F c -> F d -> F e
const liftA4 = curry((fn, F1, F2, F3, F4) => F1.map(fn).ap(F2).ap(F3).ap(F4));

// take3Args :: String -> String -> Number -> String
const take3Args = curry(
  (firstname, lastname, age) =>
    `My name is ${firstname} ${lastname} and I'm ${age}.`
);

// take4Args :: a -> b -> c -> d -> [a, b, c, d]
const take4Args = curry((a, b, c, d) => [a, b, c, d]);

liftA3(take3Args, Identity("Yann"), Identity("Salmon"), Identity(18));
// Identity("My name is Yann Salmon and I'm 18.")

liftA4(take4Args, Identity(1), Identity(2), Identity(3), Identity(4));
// Identity([1, 2, 3, 4])
```

Comme vous pouvez le constater, _A*_ fait référence au nombre d'arguments.

Wow ! Nous avons couvert un tas de choses.

Encore une fois, je veux vous féliciter pour le temps et l'attention que vous avez accordés jusqu'à présent.

Nous avons presque une boîte à outils complète pour résoudre des problèmes réels de manière fonctionnelle.

Nous devons maintenant explorer l'interface `Monad`.

### Exercices (Set 4)

Considérez cet objet utilisateur pour les 2 exercices suivants :

```js
const user = {
  id: "012345",
  name: "John Doe",
  hobbies: ["Cycling", "Drawing"],
  friends: [
    {name: "Mickael Bolp", ...},
    // ...
  ],
  partner: {name: "Theresa Doe", ...},
  // ...
}

```

1. Créez une fonction qui retourne une phrase décrivant le couple si l'utilisateur a un partenaire en utilisant les helpers donnés et `ap` :

```js
// safeProp :: String -> Object -> Maybe a
const safeProp = curry((prop, obj) =>
  obj[prop] === undefined || obj[prop] === null
    ? Maybe.Nothing()
    : Maybe.Just(obj[prop])
);

// getCouplePresentation :: User -> User -> String
const getCouplePresentation = curry(
  (name1, name2) => `${name1} and ${name2} are partners.`
);

// getName :: User -> String
const getName = (user) => user.name;
// J'aurais pu écrire : const getName = safeProp("name")
// mais je ne l'ai pas fait et c'est intentionnel.
// Nous supposons qu'un utilisateur a toujours un nom.

const couple = ...

```

2. Refactorisez la réponse précédente en utilisant `liftA2` (vérifiez la réponse de la question précédente avant) :

```js
// liftA2 :: Apply functor F => (a -> b -> c) -> F a -> F b -> F c
const liftA2 = curry((fn, F1, F2) => F1.map(fn).ap(F2));

const couple = ...

```

[Vérifier les réponses](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#set-4).

### Monads

Dans les exercices précédents, j'ai donné l'helper `getName` alors que nous aurions pu le dériver de `safeProp`.

La raison pour laquelle je l'ai fait est que `safeProp` retourne un functor `Maybe`.

Ainsi, en essayant d'obtenir le nom du partenaire d'un utilisateur, nous nous retrouvons avec 2 functors `Maybe` imbriqués :

```js

const getPartnerName = pipe(safeProp("partner"), map(safeProp("name")));
// Maybe(Maybe("Theresa Doe"))
```

Regardons un autre exemple où ce problème s'aggrave :

```js
// getUser :: Object -> IO User
const getUser = ({ email, password }) => IO.of(db.getUser(email, password));

// getLastPurchases :: User -> IO [Purchase]
const getLastPurchases = (user) => IO.of(db.purchases(user));

// display :: [Purchase] -> IO _
const display = "some implementation";

// displayUserPurchases :: Object -> IO _
const displayUserPurchases = pipe(
  getUser,
  map(getLastPurchases),
  map(map(display))
);

displayUserPurchases({ email: "johndoe@whatever.com", password: "1234" });
// IO(IO(IO _))
```

Comment se débarrasser de ces couches de conteneur qui nous obligent à faire des `map` imbriqués qui nuisent à la lisibilité ?

Les Monads à notre secours ! Les Monads sont des functors qui peuvent s'aplatir.

Encore une fois, comme les functors réguliers, vous ne les utiliserez probablement pas très souvent.

Cependant, ce sont des abstractions puissantes qui regroupent un ensemble spécifique de comportements avec une valeur.

Ce sont des structures de données soutenues par des lois mathématiques qui les rendent extrêmement prévisibles et fiables.

De plus, des lois comme la composition ou l'associativité nous disent que nous pouvons faire la même chose tout en effectuant les opérations d'une manière différente.

Rappelez-vous ce que nous avons vu avec les Applicatives et `ap` :

```js
F(x).map(fn) === F(fn).ap(F(x));

```

Celles-ci peuvent être utiles car certaines variantes peuvent être plus efficaces sur le plan computationnel.

Le problème est que la manière dont nous préférons écrire des programmes peut différer de la manière dont ils devraient être écrits si nous voulions qu'ils soient aussi efficaces que possible.

Ainsi, parce que ces lois nous assurent que toutes les variantes font la même chose, nous pouvons écrire comme nous le souhaitons et demander au compilateur d'utiliser la variante la plus efficace plus tard.

C'est pourquoi je ne vous ai pas ennuyé avec ces lois très souvent. Mais soyez conscient de leur utilité (qui s'étend certainement au-delà de cela).

Revenons à nos monads, le comportement d'aplatissement est généralement implémenté avec une méthode `chain` (aka `flatMap`, `bind`, `>==`) :

```js
const Identity = (x) => ({
  inspect: () => `Identity(${x})`,
  // Interface Functor
  map: (fn) => Identity(fn(x)),
  // Interface Applicative
  ap: (functor) => functor.map(x),
  // Interface Monad
  chain: (fn) => fn(x),
  value: x,
});

// Interface Pointed
Identity.of = (x) => Identity(x);

// chain :: Monad M => (a -> M b) -> M a -> M b
const chain = curry((fn, monad) => monad.chain(fn));

const getPartnerName = pipe(safeProp("partner"), chain(safeProp("name")));
```

Dans le cas de `Identity`, `chain` est comme `map` mais sans un nouveau functor `Identity` l'entourant.

Vous pourriez penser : "Cela va à l'encontre du but, nous allons obtenir une valeur déballée !"

Mais, nous ne le ferons pas car `fn` est censé retourner un functor.

Regardez la signature de type de cet helper `chain` :

```js
// chain :: Monad M => (a -> M b) -> M a -> M b
const chain = curry((fn, monad) => monad.chain(fn));
```

En fait, nous aurions pu faire la même chose en appliquant d'abord la fonction qui retourne un functor, ce qui nous donne un functor imbriqué, puis en supprimant le functor interne ou externe.

Par exemple :

```js
const Identity = (x) => ({
  // ...
  chain: (fn) => Identity(x).map(fn).value,
  value: x,
});
```

Vous pouvez voir que nous enveloppons d'abord `x`, puis nous mappons, puis nous prenons la valeur interne.

Parce qu'envelopper `x` dans un nouveau `Identity` et éventuellement prendre sa valeur interne sont opposés, il est plus propre de ne faire aucun des deux comme dans la première version.

Maintenant, refactorisons le premier extrait de cette section (avec des functors imbriqués) en utilisant l'helper `chain` :

```js
// AVANT
// ...

// displayUserPurchases :: Object -> IO _
const displayUserPurchases = pipe(
  getUser,
  map(getLastPurchases),
  map(map(display))
);

displayUserPurchases({ email: "johndoe@whatever.com", password: "1234" });
// IO(IO(IO _))

// APRÈS
// ...

const displayUserPurchases = pipe(
  getUser,
  chain(getLastPurchases),
  chain(display)
);

displayUserPurchases({ email: "johndoe@whatever.com", password: "1234" });
// IO _
```

Tout d'abord, `getUser` retourne un `IO(User)`.

Ensuite, nous enchaînons `getLastPurchases` au lieu de le mapper.

En d'autres termes, nous gardons le résultat de `getLastPurchases(User)` (qui est `IO(?)`), en nous débarrassant de l'`IO` original qui entourait `User`.

C'est pourquoi les monads sont souvent comparés à des oignons – les aplatir/les enchaîner est comme enlever une couche d'oignon. Lorsque vous le faites, vous libérez des résultats potentiellement indésirables qui pourraient vous faire pleurer ?.

Dans le dernier exemple, si le premier calcul `getUser` avait retourné `Nothing`, appeler `chain` dessus aurait également retourné `Nothing`.

Ce functor ne fait aucune opération.

Cependant, nous devons étendre la version simple que nous avons vue plus tôt dans cet article afin de lui donner les interfaces `Applicative` et `Monad`.

Sinon, nous ne pourrions pas l'utiliser comme tel :

```js
const Nothing = () => ({
  inspect: () => `Nothing()`,
  map: Nothing,
  ap: Nothing,
  chain: Nothing,
});

Nothing.of = () => Nothing();
```

Tant que vous gardez au moins une couche (c'est-à-dire un functor) jusqu'à ce que vous soyez prêt à libérer l'effet, c'est bon.

Mais si vous aplatissez la monade pour obtenir la valeur brute contenue partout parce que vous n'êtes pas capable de comprendre comment la composer, cela va à l'encontre du but.

### Récapitulatif

**Functors** appliquent une fonction à une valeur enveloppée (`map`).

**Pointed** functors ont une méthode pour placer une valeur dans le contexte minimal par défaut du functor (`of`).

**Applicatives** appliquent une fonction enveloppée à une valeur enveloppée (`ap` + `of`).

**Monads** appliquent une fonction qui retourne une valeur enveloppée à une valeur enveloppée (`chain` + `of`).

### Exercices (Set 5)

1. Considérez cet objet :

```js
const restaurant = {
  name: "The Creamery",
  address: {
    city: "Los Angeles",
    street: {
      name: "Melrose Avenue",
    },
  },
  rating: 8,
};
```

Créez une fonction `getStreetName` qui, comme son nom l'indique, retourne le nom de la rue du restaurant.

Utilisez `safeProp` (et `chain`, ainsi que tout autre helper fonctionnel dont vous avez besoin) pour le faire de manière pure.

```js
// safeProp :: String -> Object -> Maybe a
const safeProp = curry((prop, obj) =>
  obj[prop] === undefined || obj[prop] === null
    ? Maybe.Nothing()
    : Maybe.Just(obj[prop])
);

// getStreetName :: Object -> Maybe String
const getStreetName = ...

```

[Vérifier les réponses](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#set-5).

## Réponses aux exercices

Les réponses que je propose ne sont pas les seules. Vous pouvez trouver vos propres solutions, même meilleures.

Tant que votre solution fonctionne, c'est génial.

### Set 1

[Retour à l'exercice](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#exercises-set-1-).

1. Fonctions pures : a, d, e / Fonctions impures : b, c

Pour _e_, la réponse peut ne pas être facile à comprendre.

C'était cette fonction :

```js
const counter = (start, end) => {
  // ...

  // e
  () => counter(start + 1, end);
};
```

Donc, c'est une fonction à l'intérieur d'une autre.

Nous avons dit qu'une fonction pure ne devrait pas dépendre de l'extérieur, mais ici elle accède à des variables en dehors de sa portée, celles sur lesquelles elle a une fermeture (`counter`, `start` et `end`).

Dans un langage fonctionnel pur, contrairement à JavaScript, `counter`, `start` et `end` seraient immuables, donc _e_ serait pur car, pour la même entrée (dans ce cas aucune), nous obtiendrions toujours la même sortie.

Cependant, les valeurs en JavaScript sont mutables par défaut.

Ainsi, si `start` était un objet pour une raison quelconque, il pourrait être muté en dehors de `counter` ou à l'intérieur de _e_ lui-même.

Dans ce cas, _e_ serait considéré comme impur.

Mais comme ce n'est pas le cas ici, je le classe comme une fonction pure.

Voir ce [fil de discussion](https://softwareengineering.stackexchange.com/questions/235175/are-closures-considered-impure-functional-style) pour plus de détails.

2.

```js
const people = [
  { firstname: "Bill", lastname: "Harold", age: 54 },
  { firstname: "Ana", lastname: "Atkins", age: 42 },
  { firstname: "John", lastname: "Doe", age: 57 },
  { firstname: "Davy", lastname: "Johnson", age: 34 },
];

const uppercaseNames = (person) => ({
  firstname: person.firstname.toUpperCase(),
  lastname: person.lastname.toUpperCase(),
  age: person.age,
});

// "sort" mute le tableau original sur lequel il est appliqué.
// Donc je fais une copie avant ([...people]) pour ne pas muter l'argument original.
const sortByAge = (people) =>
  [...people].sort((person1, person2) => person1.age - person2.age);

const parsePeople = (people) => sortByAge(people.map(uppercaseNames));

// PAS SÛR D'INCLURE
// Si vous avez déjà lu la section sur la Composition (après celle-ci), vous pourriez proposer
// une version plus lisible pour "parsePeople" :
const parsePeople = pipe(map(uppercaseNames), sortByAge);
// ou
const parsePeople = compose(sortByAge, map(uppercaseNames));

parsePeople(people);
// [
//   {firstname: "DAVY", lastname: "JOHNSON", age: 34},
//   {firstname: "ANA", lastname: "ATKINS", age: 42},
//   {firstname: "BILL", lastname: "HAROLD", age: 54},
//   {firstname: "JOHN", lastname: "DOE", age: 57},
// ]
```

C'est la version à laquelle j'ai pensé, mais toute variation fonctionne à partir du moment où elle n'a pas d'effets secondaires.

La fonction de l'exercice mute effectivement l'objet passé en argument.

Mais vous pouvez vérifier que le tableau `people` original est inchangé dans cette correction.

### Set 2

[Retour à l'exercice](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#exercises-set-2-).

1. 

```js
const input =
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";

// ...

// keepLetters :: [Character] -> [Character] | []
const keepLetters = filter((char) =>
  "abcdefghijklmnopqrstuvwxyz".includes(char)
);

// getLetters :: String -> [Character]
const getLetters = pipe(
  lowercase,
  getChars,
  keepLetters,
  removeDuplicates,
  sort
);
// ou
const getLetters = compose(
  sort,
  removeDuplicates,
  keepLetters,
  getChars,
  lowercase
);

getLetters(input);
// ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x"]
```

2.

```js
// getMedianAges :: [Key, [Person]] ->  [Key, Object]
const getMedianAges = reduceOverVal((acc, person) => {
  const key = `medianAge${person.sex}`;

  return !acc[key]
    ? { ...acc, [key]: person.age }
    : { ...acc, [key]: mean(acc[key], person.age) };
}, {});

// groupsMedianAges :: Object -> Object
const groupsMedianAges = pipe(getEntries, map(getMedianAges), fromEntries);
// ou
const groupsMedianAges = compose(fromEntries, map(getMedianAges), getEntries);
```

3.

```js
// reduce :: (b -> a -> b) -> b -> [a] -> b

```

4.

```js
// curry :: ((a, b, ...) -> c) -> a -> b ->  ... -> c

```

### Set 3

[Retour à l'exercice](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#exercises-set-3-).

1. 

```js
const uppercaseF = map((str) => str.toUpperCase())

// Exemple:
const myFunctor = Just("string")

uppercaseF(myFunctor)
// Just("STRING")

```

2.

```js
const uppercaseF = map((str) => str.toUpperCase());

// Exemple:
const myFunctor = Just("string");

uppercaseF(myFunctor);
// Just("STRING")
```

2.

```js
// printUsername :: User -> _
const printUsername = pipe(
  safeProp("name"),
  uppercaseF,
  maybe("Username not found !", console.log)
);

// Exemple:
printUsername({
  name: "Yann Salmon",
  age: 18,
  interests: ["Programming", "Sport", "Reading", "Math"],
  // ...
});
// console: YANN SALMON
```

### Set 4

[Retour à l'exercice](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#exercises-set-4-).

1. 

```js
// getPartnerName :: User -> Maybe String
const getPartnerName = pipe(safeProp("partner"), map(getName));

// userName :: Maybe String
const userName = Maybe.of(getName(user));
// partnerName :: Maybe String
const partnerName = getPartnerName(user);

// couple :: Maybe String
const couple = Maybe.of(getCouplePresentation).ap(userName).ap(partnerName);
// Just("John Doe and Theresa Doe are partners.")
```

2.

```js
// ...

const couple = liftA2(getCouplePresentation, userName, partnerName);
```

### Set 5

[Retour à l'exercice](https://www.freecodecamp.org/news/the-principles-of-functional-programming/#exercises-set-5-).

1. 

```js
// ...

// getStreetName :: Object -> Maybe String
const getStreetName = pipe(
  safeProp("address"),
  chain(safeProp("street")),
  chain(safeProp("name"))
);

getStreetName(restaurant);
// Just("Melrose Avenue")
```

## Aller plus loin

Cet article est principalement inspiré de ce que j'ai appris de ces 3 ressources incroyables (par ordre de difficulté) :

* [Liste de lecture Fun Fun Function](https://www.youtube.com/playlist?list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84) (vidéo)
* [Functional-Light JavaScript](https://github.com/getify/Functional-Light-JS) (livre)
* [Guide principalement adéquat pour la programmation fonctionnelle](https://mostly-adequate.gitbooks.io/mostly-adequate-guide/content/) (livre)

Comme moi, vous trouverez certainement certains concepts vraiment difficiles à saisir au début.

Mais continuez, s'il vous plaît. N'hésitez pas à rembobiner les vidéos et à relire les paragraphes après une bonne nuit de sommeil.

Je vous assure que cela portera ses fruits.

Il y a aussi un excellent [dépôt Github](https://github.com/stoeffel/awesome-fp-js) qui rassemble des ressources sur la programmation fonctionnelle en JavaScript.

Vous y trouverez, entre autres, de belles bibliothèques qui fournissent des helpers fonctionnels. Ma préférée à l'heure actuelle est [Ramda JS](https://ramdajs.com/). D'autres fournissent également des monads comme [Sanctuary](https://sanctuary.js.org/).

Je ne connais certainement pas tout sur la programmation fonctionnelle, donc il y a des sujets que je n'ai pas couverts.

Ceux dont je suis conscient sont :

* Une technique appelée **transducing**. En bref, c'est un moyen de composer ensemble des opérations `map`, `filter` et `reduce`. Consultez [ceci](https://github.com/getify/Functional-Light-JS/blob/master/manuscript/apA.md/#appendix-a-transducing) et [cela](https://www.youtube.com/watch?v=6mTbuzafcII) pour en savoir plus.
* Autres types courants de monads : Either, Map, List
* Autres structures algébriques comme les semi-groupes et les monoïdes
* [Programmation Réactive Fonctionnelle](https://www.learnrxjs.io/)

## Conclusion

C'est tout !

Avant de finir, je veux vous avertir des erreurs potentielles.

Je ne suis pas un expert en programmation fonctionnelle, alors s'il vous plaît, soyez critique envers cet article à mesure que vous en apprenez davantage. Je suis toujours ouvert aux discussions et aux améliorations.

Dans tous les cas, j'espère avoir posé ce que je considère être les bases nécessaires pour que vous soyez plus productif dans votre travail quotidien, ainsi que vous donner les outils et l'intérêt pour aller plus loin.

Et avec cela, continuez à coder ! ?