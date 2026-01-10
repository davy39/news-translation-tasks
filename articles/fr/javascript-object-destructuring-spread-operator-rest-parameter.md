---
title: Destructuration d'objets JavaScript, syntaxe de propagation et paramètre Rest
  – Un guide pratique
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-02-08T20:30:30.000Z'
originalURL: https://freecodecamp.org/news/javascript-object-destructuring-spread-operator-rest-parameter
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/freeCodeCamp-Cover-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Destructuration d'objets JavaScript, syntaxe de propagation et paramètre
  Rest – Un guide pratique
seo_desc: "In JavaScript, we use objects to store multiple values as a complex data\
  \ structure. There are hardly any JavaScript applications that do not deal with\
  \ objects. \nWeb developers commonly extract values from an object property to use\
  \ further in programm..."
---

En JavaScript, nous utilisons des objets pour stocker plusieurs valeurs sous forme de structure de données complexe. Il existe rarement des applications JavaScript qui ne manipulent pas d'objets.

Les développeurs web extraient couramment des valeurs d'une propriété d'objet pour les utiliser dans la logique de programmation. Avec ES6, JavaScript a introduit la `destructuration d'objets` pour faciliter la création de variables à partir des propriétés d'un objet.

Dans cet article, nous allons apprendre la `destructuration d'objets` à travers de nombreux exemples pratiques. Nous apprendrons également à utiliser la `syntaxe de propagation` et le `paramètre rest`. J'espère que vous apprécierez.

# Destructuration d'objets en JavaScript

Nous créons des objets avec des accolades `{…}` et une liste de propriétés. Une propriété est une paire clé-valeur où la clé doit être une chaîne ou un symbole, et la valeur peut être de n'importe quel type, y compris un autre objet.

```js
const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}
```

Ici, nous avons créé un objet utilisateur avec trois propriétés : name, address et age. Le besoin réel en programmation est d'extraire ces valeurs de propriétés et de les assigner à une variable.

Par exemple, si nous voulons obtenir la valeur des propriétés `name` et `age` de l'objet `user`, nous pouvons faire ceci :

```js
let name = user.name;
let age = user.age;
console.log(name, age);
```

Cela nécessite indéniablement un peu plus de frappe. Nous devons explicitement mentionner les propriétés `name` et `age` avec l'objet `user` en notation pointée, puis déclarer les variables en conséquence et les assigner.

Nous pouvons simplifier ce processus en utilisant la nouvelle syntaxe de `destructuration d'objets` introduite dans ES6.

> La destructuration d'objets JavaScript est la syntaxe pour extraire des valeurs d'une propriété d'objet et les assigner à une variable. La destructuration est également possible pour les tableaux JavaScript.

Par défaut, le nom de la clé de l'objet devient la variable qui contient la valeur respective. Ainsi, aucun code supplémentaire n'est requis pour créer une autre variable pour l'assignation de valeur. Voyons comment cela fonctionne avec des exemples.

## Exemple de base de destructuration d'objets

Prenons le même objet `user` auquel nous avons fait référence ci-dessus.

```js
const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

```

L'expression pour extraire la valeur de la propriété `name` en utilisant la destructuration d'objets est la suivante :

```js
const { name } = user;

console.log(name); // Sortie, Alex
```

Comme vous le voyez, du côté gauche de l'expression, nous prenons la clé de la propriété de l'objet (`name` dans ce cas) et la plaçons à l'intérieur des `{}` . Elle devient également le nom de la variable pour contenir la valeur de la propriété.

Le côté droit de l'expression est l'objet réel qui extrait la valeur. Nous mentionnons également les mots-clés, `const`, `let` et ainsi de suite pour spécifier la portée de la variable.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/destructure.png)

Alors, comment extraire les valeurs de plus d'une propriété d'objet ? Simple – nous continuons à ajouter les clés de l'objet à l'intérieur des `{}` avec des virgules les séparant. Dans l'exemple ci-dessous, nous destructurons les propriétés `name` et `age` de l'objet `user`.

```js
const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

const { name, age } = user;

console.log(name, age); // Sortie, Alex 43

```

## Règle de déclaration de variable

Les mots-clés let et const sont significatifs dans la syntaxe de destructuration d'objets. Considérez l'exemple ci-dessous où nous avons omis le mot-clé let ou const. Cela se terminera par l'erreur, `Uncaught SyntaxError: Unexpected token '='`.

```js
const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

{ name  } = user // Uncaught SyntaxError: Unexpected token '='
```

Que se passe-t-il si nous déclarons la variable à l'avance et essayons ensuite de destructurer la clé du même nom de l'objet ? Non, pas beaucoup de chance ici non plus. Cela reste syntaxiquement incorrect.

```js
let name;

{ name  } = user; // Uncaught SyntaxError: Unexpected token '='
```

Dans ce cas, la syntaxe correcte consiste à placer l'expression de destructuration entre parenthèses (`(...)`).

> Veuillez noter que les parenthèses sont requises lorsque vous souhaitez omettre le mot-clé let ou const dans l'expression de destructuration elle-même.

```js
let name;

({ name  } = user);

console.log(name); // Sortie, Alex
```

## Ajouter une nouvelle variable et une valeur par défaut

Nous pouvons ajouter une nouvelle variable lors de la destructuration et lui ajouter une valeur par défaut. Dans l'exemple ci-dessous, la variable `salary` n'existe pas dans l'objet `user`. Mais nous pouvons l'ajouter dans l'expression de destructuration et lui ajouter une valeur par défaut.

```js
const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}
const { name, age, salary=123455 } = user;

console.log(name, age, salary); // Sortie, Alex 43 123455
```

L'autre façon de faire ce qui précède est celle-ci :

```js
let salary = user.salary ? user.salary : 123455;
```

Il y a un avantage considérable à la flexibilité d'ajouter une variable avec une valeur par défaut. La valeur par défaut de cette nouvelle variable n'est pas nécessairement une valeur constante. Nous pouvons calculer sa valeur à partir d'autres valeurs de propriétés destructurées.

Prenons un objet `user` avec deux propriétés, `first_name` et `last_name`. Nous pouvons maintenant calculer la valeur d'un `full_name` inexistant en utilisant ces deux propriétés.

```js
const user = { 
    'first_name': 'Alex',
    'last_name': 'Brandos',
}
const { first_name, last_name, full_name=`${first_name} ${last_name}` } = user;

console.log(full_name); // Sortie, Alex Brandos
```

N'est-ce pas élégant et utile !

## Ajouter des alias

Vous pouvez donner un nom d'alias à vos variables destructurées. Cela s'avère très pratique si vous souhaitez réduire les risques de conflits de noms de variables.

Dans l'exemple ci-dessous, nous avons spécifié un nom d'alias pour la propriété `address` comme `permanentAddress`.

```js
const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

const { address: permanentAddress } = user;

console.log(permanentAddress); // 15th Park Avenue
```

Veuillez noter qu'une tentative d'accès à la variable `address` ici entraînera cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-12.png)

## Destructuration d'objets imbriqués

Un objet peut être imbriqué. Cela signifie que la valeur d'une propriété d'objet peut être un autre objet, et ainsi de suite.

Prenons l'objet `user` ci-dessous. Il a une propriété appelée `department` dont la valeur est un autre objet. Mais n'arrêtons pas ici ! Le `department` a une propriété avec la clé `address` dont la valeur est un autre objet. Un scénario assez réaliste, n'est-ce pas ?

```js
const user = { 
        'name': 'Alex',
        'address': '15th Park Avenue',
        'age': 43,
        'department':{
            'name': 'Sales',
            'Shift': 'Morning',
            'address': {
                'city': 'Bangalore',
                'street': '7th Residency Rd',
                'zip': 560001
            }
        }
}
```

Comment extraire la valeur de la propriété `department` ? Ok, cela devrait être simple maintenant.

```js
const { department } = user;
```

Et voici la sortie lorsque vous loggez `department` :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-30.png)

Mais, descendons d'un niveau imbriqué. Comment extraire la valeur de la propriété `address` du `department` ? Cela peut sembler un peu délicat. Cependant, si vous appliquez les mêmes principes de `destructuration d'objets`, vous verrez que c'est similaire.

```js
const { department: { address } } = user;
```

Voici la sortie lorsque vous loggez `address` :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-31.png)

Dans ce cas, `department` est la clé sur laquelle nous nous concentrons et nous destructurons la valeur `address` de celle-ci. Remarquez les `{}` autour des clés que vous souhaitez destructurer.

Il est maintenant temps de passer au niveau suivant. Comment extraire la valeur de `city` de l'adresse du département ? Même principe encore !

```js
const { department: { address: { city } } } = user; 
```

La sortie lorsque vous loggez `city` est "Bangalore".

Cela peut aller à n'importe quel niveau imbriqué.

> La règle de base est de commencer par le niveau supérieur et de descendre dans la hiérarchie jusqu'à atteindre la valeur que vous souhaitez extraire.

## Propriété de nom dynamique

De nombreuses fois, vous ne connaissez peut-être pas le nom de la propriété (clé) d'un objet lors de sa destructuration. Considérez cet exemple. Nous avons un objet `user` :

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

```

Maintenant, la méthode `getValue(key)` prend un nom de clé de propriété et doit retourner sa valeur.

```js
getValue('name') // Doit retourner Alex
getValue('age') // Doit retourner 43
```

Alors, comment écrire la définition de la méthode `getValue(key)` en utilisant la syntaxe de destructuration ?

Eh bien, la syntaxe est très similaire à la création d'alias. Comme nous ne connaissons pas le nom de la `clé` à coder en dur dans la syntaxe de destructuration, nous devons l'enfermer dans des crochets (`[...]`).

```js
const getValue = key => {
    const { [key]: returnValue } = user;   
    return returnValue;
}
```

## Destructurer vers le paramètre de fonction

C'est l'un de mes préférés, et il réduit considérablement le code inutile. Vous souhaitez peut-être passer seulement quelques valeurs de propriétés spécifiques en tant que paramètre à la définition de la fonction, et non l'objet entier. Utilisez la destructuration d'objets vers le paramètre de fonction dans ce cas.

Prenons à nouveau l'exemple de l'objet `user`.

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}
```

Supposons que nous avons besoin d'une fonction pour retourner une chaîne en utilisant le nom et l'âge de l'utilisateur. Disons quelque chose comme `Alex a 43 ans !` est la valeur de retour lorsque nous appelons ceci :

```js
logDetails(user); 
```

Nous pouvons simplement utiliser la destructuration ici pour passer les valeurs `name` et `age`, respectivement, à la définition de la fonction. Il n'est pas nécessaire de passer l'objet `user` entier et ensuite extraire les valeurs une par une. Veuillez consulter :

```js
function logDetails({name, age}) {
    console.log(`${name} a ${age} ans !`)
}

```

## Destructurer la valeur de retour de la fonction

Lorsque une fonction retourne un objet et que vous êtes intéressé par des valeurs de propriétés spécifiques, utilisez la destructuration immédiatement. Voici un exemple :

```js

const getUser = () => {
    return{ 
        'name': 'Alex',
        'address': '15th Park Avenue',
        'age': 43
    }
}

const { name, age } = getUser();

console.log(name, age); // Alex 43

```

Cela est similaire à la destructuration d'objets de base que nous avons vue au début.

## Destructurer dans les boucles

Vous pouvez utiliser la destructuration d'objets avec la boucle `for-of`. Prenons un tableau d'objets utilisateurs comme ceci :

```js

const users = [
    { 
        'name': 'Alex',
        'address': '15th Park Avenue',
        'age': 43
    },
    { 
        'name': 'Bob',
        'address': 'Canada',
        'age': 53
    },
    { 
        'name': 'Carl',
        'address': 'Bangalore',
        'age': 26
    }
];
```

Nous pouvons extraire les valeurs des propriétés avec la destructuration d'objets en utilisant la boucle `for-of`.

```js
for(let { name, age } of users) {
    console.log(`${name} a ${age} ans !`);
}
```

Voici la sortie :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-27.png)

## L'objet `Console`

En JavaScript, `console` est un objet intégré pris en charge par tous les navigateurs. Si vous avez remarqué, l'objet `console` a de nombreuses propriétés et méthodes, et certaines sont très populaires, comme `console.log()`.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-13.png)

En utilisant la syntaxe de destructuration d'objets, nous pouvons simplifier l'utilisation de ces méthodes et propriétés dans notre code. Que pensez-vous de ceci ?

```js
const { log, warn, error } = console;

log('Je me connecte à la console du navigateur');
warn('Je suis un avertissement');
error('Je suis une erreur');
```

# Syntaxe de propagation en JavaScript

La syntaxe de propagation (également connue sous le nom d'opérateur de propagation) est une autre excellente fonctionnalité de ES6. Comme son nom l'indique, elle prend un itérable (comme un tableau) et l'étend (étale) en éléments individuels.

Nous pouvons également étendre des objets en utilisant la syntaxe de propagation et copier ses propriétés `énumérables` vers un nouvel objet.

La syntaxe de propagation nous aide à cloner un objet avec la syntaxe la plus simple en utilisant les accolades et trois points `{...}`.

```js
const clone_some_object = {...some_object}
```

Avec la syntaxe de propagation, nous pouvons cloner, mettre à jour et fusionner des objets de manière `immutable`. L'immuabilité aide à réduire tout changement accidentel ou involontaire à l'objet original (Source).

> La destructuration d'objets et les syntaxes de propagation ne sont pas la même chose en JavaScript.

## Créer un clone d'un objet

Nous pouvons créer une instance clonée d'un objet en utilisant la syntaxe de propagation comme ceci :

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

const clone = {...user} // Sortie, {name: "Alex", address: "15th Park Avenue", age: 43}

clone === user; // Sortie, false

```

Vous pouvez également utiliser `object.assign()` pour créer un clone d'un objet. Cependant, la syntaxe de propagation est beaucoup plus précise et beaucoup plus courte.

> La syntaxe de propagation effectue une copie superficielle de l'objet. Cela signifie qu'aucune des instances d'objets imbriqués n'est clonée.

## Ajouter des propriétés aux objets

Nous pouvons ajouter une nouvelle propriété (paire clé-valeur) à l'objet en utilisant la `syntaxe de propagation`. Notez que l'objet réel ne change jamais. La nouvelle propriété est ajoutée à l'objet cloné.

Dans l'exemple ci-dessous, nous ajoutons une nouvelle propriété (`salary`) en utilisant la syntaxe de propagation.

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

// Ajouter une nouvelle propriété salary
const updatedUser = {...user, salary:12345}; // {name: "Alex", address: "15th Park Avenue", age: 43, salary: 12345}

// L'objet original est inchangé
console.log(user); // {name: "Alex", address: "15th Park Avenue", age: 43}

```

## Mettre à jour les propriétés

Nous pouvons également mettre à jour une valeur de propriété existante en utilisant la syntaxe de propagation. Comme l'opération d'ajout, la mise à jour a lieu sur l'instance clonée de l'objet, et non sur l'objet réel.

Dans l'exemple ci-dessous, nous mettons à jour la valeur de la propriété `age` :

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

const updatedUser = {...user, age:56}; // {name: "Alex", address: "15th Park Avenue", age: 56}

console.log(user); // {name: "Alex", address: "15th Park Avenue", age: 43}

```

## Mettre à jour les objets imbriqués

Comme nous l'avons vu, la mise à jour d'un objet avec la syntaxe de propagation est facile et ne modifie pas l'objet original. Cependant, cela peut être un peu délicat lorsque vous essayez de mettre à jour un objet imbriqué en utilisant la syntaxe de propagation. Comprenons cela avec un exemple.

Nous avons un objet `user` avec une propriété `department`. La valeur de la propriété `department` est un objet qui a un autre objet imbriqué avec sa propriété `address`.

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43,
    'department':{
        'name': 'Sales',
        'Shift': 'Morning',
        'address': {
            'city': 'Bangalore',
            'street': '7th Residency Rd',
            'zip': 560001
        }
    }
}

```

Maintenant, comment pouvons-nous ajouter une nouvelle propriété appelée `number` avec une valeur de, disons, `7` pour l'objet `department` ? Eh bien, nous pourrions essayer le code suivant pour y parvenir (mais ce serait une erreur) :

```js
const updated = {
    ...user, 
    department: {'number': 7}
}

console.log(updated);
```

Lorsque vous l'exécutez, vous réaliserez que le code remplacera tout l'objet department par la nouvelle valeur, `{'number': 7}`. Ce n'est pas ce que nous voulions !

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-28.png)

Comment corriger cela ? Nous devons étendre les propriétés de l'objet imbriqué ainsi que l'ajouter/mettre à jour. Voici la syntaxe correcte qui ajoutera une nouvelle propriété `number` avec la valeur `7` à l'objet `department` sans remplacer sa valeur :

```js
const updated = {
    ...user, 
    department: {
        ...user.department, 
        'number': 7
    }
};

console.log(updated);
```

La sortie est la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-29.png)

## Combiner (ou fusionner) deux objets

La dernière utilisation pratique de la syntaxe de propagation dans les objets JavaScript est de combiner ou fusionner deux objets. obj_1 et obj_2 peuvent être fusionnés ensemble en utilisant la syntaxe suivante :

```js
const merged = {...obj_1, ...obj_2};
```

Notez que cette façon de fusionner effectue une `fusion superficielle`. Cela signifie que si une propriété commune existe entre les deux objets, la valeur de la propriété de obj_2 remplacera la valeur de la propriété de obj_1 dans l'objet fusionné.

Prenons les objets `user` et `department` pour les combiner (ou fusionner) ensemble.

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

const department = {
    'id': '001',
    'Shift': 'Morning'
}

```

Fusionnez les objets en utilisant la syntaxe de propagation, comme ceci :

```js
const completeDetails = {...user, ...department};

console.log(completeDetails);
```

La sortie sera la suivante :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-33.png)

Si nous modifions l'objet `department` comme ceci :

```js
const department = {
    'name': 'Sales',
    'Shift': 'Morning'
}
```

Essayez maintenant de les combiner et observez la sortie de l'objet combiné :

```js
const completeDetails = {...user, ...department};

console.log(completeDetails);
```

La sortie sera :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-34.png)

La valeur de la propriété `name` de l'objet `user` est remplacée par la valeur de la propriété `name` de l'objet `department` dans la sortie de l'objet fusionné. Soyez donc prudent lorsque vous l'utilisez de cette manière.

Pour l'instant, vous devez implémenter la `fusion profonde` des objets par vous-même ou utiliser une bibliothèque comme `lodash` pour y parvenir.

# Le paramètre Rest en JavaScript

Le paramètre `Rest` est en quelque sorte l'opposé de la syntaxe `spread`. Alors que la syntaxe spread aide à étendre ou à propager les éléments et les propriétés, le paramètre rest aide à les collecter ensemble.

Dans le cas des objets, le paramètre rest est principalement utilisé avec la syntaxe de destructuration pour consolider les propriétés restantes dans un nouvel objet avec lequel vous travaillez.

Regardons un exemple de l'objet `user` suivant :

```js

const user = { 
    'name': 'Alex',
    'address': '15th Park Avenue',
    'age': 43
}

```

Nous savons comment destructurer la propriété `age` pour créer une variable et assigner sa valeur. Que diriez-vous de créer un autre objet en même temps avec les propriétés restantes de l'objet `user` ? Voici comment faire :

```js

const {age, ...rest} = user;
console.log(age, rest);
```

La sortie sera :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-26.png)

Dans la sortie, nous voyons que la valeur `age` est `43`. Le `paramètre rest` a consolidé le reste des propriétés de l'objet `user`, `name` et `address`, dans un objet séparé.

# En résumé

Pour résumer,

* La destructuration d'objets est une nouvelle syntaxe introduite dans ES6. Elle aide à créer des variables en extrayant les propriétés de l'objet de manière beaucoup plus simple.
* Si vous travaillez avec (ou prévoyez d'utiliser) un framework/bibliothèque comme `angular`, `react` ou `vue`, vous utiliserez beaucoup la syntaxe de destructuration d'objets.
* La destructuration d'objets et la syntaxe de propagation ne sont pas la même chose.
* La syntaxe `spread` (également connue sous le nom d'opérateur de propagation) est utilisée pour copier les propriétés énumérables d'un objet afin de créer un clone de celui-ci. Nous pouvons également mettre à jour un objet ou le fusionner avec un autre objet en utilisant la syntaxe de propagation.
* Le paramètre `Rest` est en quelque sorte l'opposé de la syntaxe `spread`. Il aide à consolider (ou collecter) les propriétés restantes de l'objet dans un nouvel objet lors de la destructuration.

## Avant de partir

J'espère que vous avez trouvé cet article perspicace et qu'il vous aide à commencer à utiliser ces concepts plus efficacement. Restons en contact. Vous me trouverez actif sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). N'hésitez pas à me suivre.

Vous pouvez trouver tous les exemples de code source utilisés dans cet article dans mon dépôt GitHub - [js-tips-tricks](https://github.com/atapas/js-tips-tricks/blob/master/object-destructuring.js). Êtes-vous intéressé à faire un peu de codage pratique basé sur ce que nous avons appris jusqu'à présent ? Veuillez [jeter un coup d'œil au quiz ici](https://github.com/atapas/js-tips-tricks/blob/master/quiz-od.js), et vous pourriez le trouver intéressant.

Vous pourriez également aimer ces articles :

* [Comment apprendre quelque chose de nouveau chaque jour en tant que développeur logiciel](https://www.freecodecamp.org/news/learn-something-new-every-day-as-a-software-developer/)
* [Comment trouver des idées de contenu de blog sans effort ?](https://blog.greenroots.info/how-to-find-blog-content-ideas-effortlessly-ckghrjv5200o7rhs1ewn40102)
* [Pourquoi avez-vous besoin de faire des projets parallèles en tant que développeur ?](https://blog.greenroots.info/why-do-you-need-to-do-side-projects-as-a-developer-ckhn5m5km05teajs1fvjd7u5f)
* [16 dépôts GitHub de projets parallèles que vous pourriez trouver utiles](https://blog.greenroots.info/16-side-project-github-repositories-you-may-find-useful-ckk50hic406quhls1dui2d6sd)