---
title: Le mot-clé this en JavaScript expliqué avec des exemples
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2024-06-05T14:58:48.000Z'
originalURL: https://freecodecamp.org/news/the-javascript-this-keyword-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Python-Data-Types--3-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Le mot-clé this en JavaScript expliqué avec des exemples
seo_desc: 'All leading web browsers support JavaScript, a popular and versatile programming
  language. The this keyword is a very important concept to know in JavaScript.

  The this keyword is a reference to an object, but the object varies based on where
  and how ...'
---

Tous les navigateurs web principaux supportent JavaScript, un langage de programmation populaire et polyvalent. Le mot-clé `this` est un concept très important à connaître en JavaScript.

Le mot-clé `this` est une référence à un objet, mais l'objet varie en fonction de l'endroit et de la manière dont il est appelé.

Dans cet article, vous apprendrez comment déterminer implicitement (basé sur le contexte) et explicitement (en utilisant les méthodes `call()`, `apply()`, et `bind()`) la valeur du mot-clé `this`.

Voici les sujets que nous allons aborder :

* [Quelles sont les règles qui guident le comportement du mot-clé `this`](#heading-quelles-sont-les-regles-qui-guident-le-comportement-du-mot-cle-this) ?
* [Qu'est-ce que la méthode `call()` en JavaScript](#heading-quest-ce-que-la-methode-call-en-javascript) ?
* [Qu'est-ce que la méthode `apply()` en JavaScript](#heading-quest-ce-que-la-methode-apply-en-javascript) ?
* [Qu'est-ce que la méthode `bind()` en JavaScript](#heading-quest-ce-que-la-methode-bind-en-javascript) ?
* [Pourquoi les méthodes `call()`, `apply()`, et `bind()` ont-elles été introduites en JavaScript](#heading-pourquoi-les-methodes-call-apply-et-bind-ont-elles-ete-introduites-en-javascript) ?
* [Quelles sont les différences entre les méthodes `call()`, `apply()`, et `bind()`](#heading-quelles-sont-les-differences-entre-les-methodes-call-apply-et-bind) ?
* [Pourquoi utiliser les méthodes `call()`, `apply()`, et `bind()` en JavaScript](#heading-pourquoi-utiliser-les-methodes-call-apply-et-bind-en-javascript) ?

## Quelles sont les règles qui guident le comportement du mot-clé `this` ?

Certaines règles guident le comportement du mot-clé `this` en JavaScript. Ce sont la portée globale, le contexte de fonction, la méthode d'objet, le constructeur et les gestionnaires d'événements.

### Portée globale

Chaque fois que le mot-clé `this` est utilisé en dehors de toute fonction, il fait référence à l'objet global.

Alors que l'objet global est `global` dans l'environnement Node.js, c'est une `fenêtre` dans le contexte d'un navigateur web :

```javascript
console.log(this);

```

![bind 1](https://hackmd.io/_uploads/Hy3UshesT.png)
_Résultat de la portée globale_

Le résultat du code ci-dessus montre que `this` retourne la `fenêtre`, qui est l'objet global pour le navigateur web.

### Contexte de fonction

La méthode d'invocation détermine la valeur du mot-clé `this` dans une fonction régulière standard :

```javascript
function saySomething() {
  console.log(this)
}

saySomething()  // {window: Window, self: Window, document: document, name: '', location: Location, …}

```

![bind 1](https://hackmd.io/_uploads/H1oponlia.png)
_Résultat du contexte de fonction_

Le résultat du code ci-dessus est l'objet global pour le navigateur web.

### Méthode d'objet

Les méthodes sont des propriétés de fonction d'un objet. En JavaScript, elles permettent à un objet de manipuler ses propriétés en utilisant le mot-clé `this` :

```javascript
const club = {
  name: "Arsenal",
  yearFounded: "1989",
  details() {
    return `Hey, ${this.name} ${this.yearFounded}`;
  },
};

console.log(club.details()); // Arsenal , 1989

```

Dans le contexte du code ci-dessus, `this` fait référence au `club`. Comme vous pouvez le voir à partir de la sortie, il dit `Arsenal 1989`.

Mais nous aurions un résultat différent si nous créions une nouvelle variable pour la méthode details, comme montré ci-dessous :

```javascript
const club = {
  name: "Arsenal",
  yearFounded: "1989",
  details() {
    return `Hey, ${this.name} ${this.yearFounded}`;
  },
};

const full = club.details;
console.log(full()); // Hey,  undefined

```

Bien que la méthode `details()` ait été définie à l'intérieur de l'objet `club`, elle n'est pas expressément liée à celui-ci. Nous appelons la méthode `details()` comme une méthode sur l'objet.

En JavaScript, une méthode obtient la valeur de `this` lorsqu'elle regarde la fonction qui précède le point.

### Fonction constructeur

Il n'est pas nouveau que le constructeur de fonction était l'initialisateur par défaut pour les objets définis par l'utilisateur avant l'introduction de la mise à jour ECMAScript 2015.

Le mot-clé `new` crée une instance d'une fonction constructeur :

```javascript
function Country(name) {
  this.name = name;
  this.age = 1960;

  this.info = function () {
    console.log(`${this.name} was founded ${this.age} years ago`);
  };
}

const country = new Country("Nigeria");
console.log(country.name);
console.log(country.info());

```

![nigeria](https://hackmd.io/_uploads/Skn8R3eip.png)
_Résultat de la fonction constructeur_

Le `this` fait référence au nouvel objet créé, dans ce cas, l'instance du pays.

### Gestionnaires d'événements

Dans un gestionnaire d'événements `addEventListener`, `this` fait référence à l'élément avant le point. Il s'agit de l'élément auquel l'écouteur d'événements a été ajouté pour déclencher l'événement :

```javascript
const button = document.querySelector("button");

button.addEventListener("click", function () {
  console.log(this);
});

// OUTPUT  <button>click</button>

```

Une fois que le code ci-dessus s'exécute, un bouton avec une valeur `innerText` de `click` sera enregistré dans la console.

Dans toutes les règles ci-dessus qui guident le comportement du mot-clé populaire `this`, une chose est claire : le contexte détermine la valeur du mot-clé `this`.

Outre la détermination implicite de la valeur de `this`, des méthodes de fonction comme `call()`, `apply()`, et `bind()` peuvent être utilisées pour déterminer explicitement à quoi `this` devrait faire référence.

## Qu'est-ce que la méthode `call()` en JavaScript ?

La méthode `call()` est l'une des façons les plus populaires de définir explicitement à quoi `this` fait référence. En JavaScript, la méthode `call()` est principalement utilisée pour emprunter une méthode à un objet isolé et l'utiliser sur un autre avec un contexte spécifique.

La méthode `call()` nécessite que ses arguments soient passés un par un :

```javascript
const game = {
  title: "PrisonBreak",
  year: 1979,
};

function detail() {
  console.log(`${this.title}, was released in ${this.year}`);
}
detail();

// RESULT undefined was released in undefined

```

Le résultat ci-dessus est imprimé car il n'y a pas de connexion entre le `game` et la méthode `detail`. Par conséquent, l'appel de la méthode `detail` par elle-même imprimera uniquement `undefined`.

```javascript
const game = {
  fullDetail: function () {
    return this.title + " " + this.year;
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.call(newGame);
console.log(fullDetail); // Output: Merlin 1994

```

Dans le code ci-dessus, il y a des objets `game` et `newGame`. Le `game` a une méthode `fullDetail`, tandis que le `newGame` a des propriétés de titre et d'année.

Comme nous le savons à partir de la définition ci-dessus, la méthode `call()` a utilisé le contexte de `newGame` pour invoquer la méthode `fullDetail` de l'objet `game`.

Cela signifie que nous avons accès aux propriétés de `newGame` car le `this` à l'intérieur de `fullDetail` fait référence à l'objet `newGame`.

Nous avons maintenant une connexion entre le `game` et le `newGame` avec l'aide de la méthode `call()`.

Outre le passage de `this` en tant qu'argument, il est possible de passer des arguments supplémentaires individuellement :

```javascript
const game = {
  fullDetail: function (category) {
    return `${this.title} was released ${this.year}, and the film is a ${category} film`;
    return this.title + " " + this.year + " " + "category";
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.call(newGame, "seasonal");

console.log(fullDetail); // Merlin was released 1994, and the film is a seasonal film


```

Le code ci-dessus montre la possibilité de passer un autre argument en plus du mot-clé `this`.

### Comment utiliser la méthode call() dans une application réelle

<iframe height="300" style="width: 100%;" scrolling="no" title="call and apply javascript" src="https://codepen.io/kamal90/embed/gOygyaO?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/gOygyaO">
  call and apply javascript</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Le code suivant a été extrait du code ci-dessus :

```javascript
const newMovie = {
    info: {
      title,
      [extraName]: extraValue,
    },
    id: Math.random(),
    formatted() {
      return this.info.title.toUpperCase();
    }
  };

```

Le code ci-dessus est un objet nommé `newMovie`. Dans l'objet `newMovie`, un objet `info` avec `title` et `extraName` a été créé.

Le `title` est le nom du film, tandis que la ligne `[extraName]` utilise la notation entre crochets pour accéder dynamiquement à l'entrée utilisateur, en utilisant la valeur de la variable comme nom de clé. Alors que `extraValue` est la valeur associée à la clé.

L'`id` est l'identifiant unique qui génère un nombre aléatoire en utilisant la fonction `Math.random()`.

La méthode `formatted()` retourne le format en majuscules du titre. En utilisant `this.info.title`, où l'objet `newMovie` est le même que `this`, et `info` est un objet à l'intérieur de `newMovie` qui contient des informations comme le titre, et le reste.

```javascript

filteredMovies.forEach((movie) => {
    const newMovieEl = document.createElement('li');
    const {info} = movie;
    const {formatted} = movie
    let text = formatted.call(movie) + '-';
    for (const key in info) {
      if (key !== 'title') {
        text = text + `${key}: ${info[key]}`
      }
    }
    newMovieEl.textContent = text;
    movieList.append(newMovieEl)

  })
}

```

Le code ci-dessus montre les utilisations de la méthode `call()` dans une application réelle.

Expliquons ce qui se passe dans le code.

La ligne `const newMovieEl = document.createElement('li');` crée un nouvel élément `<li>` en utilisant `document.createElement('li')`, avec le nouvel élément stocké dans la constante `newMovieEl`.

La ligne `const {info} = movie;` utilise l'affectation de déstructuration pour extraire la propriété `info` de l'objet movie.

La ligne `const {formatted} = movie` utilise l'affectation de déstructuration pour extraire la méthode `formatted` de l'objet movie.

La ligne `let text = formatted.call(movie) + '-';` montre comment utiliser la méthode `call()` dans une application.

L'invocation de la fonction `formatted` directement ne donnera pas le résultat requis, car la fonction de `this` dans ce contexte est l'objet window.

En utilisant la méthode `call` sur la fonction `formatted`, la méthode `call()` permet de changer le contexte de `this` de l'objet window à l'objet `movie`.

Comme dit ci-dessus, en JavaScript, la méthode `call()` est utilisée pour emprunter une méthode à un objet isolé et l'utiliser sur un autre avec un contexte spécifique.

La méthode `call()` nécessite que ses arguments soient passés un par un, et exécute la fonction instantanément.

La ligne `for (const key in info) {if (key !== 'title') {text = text +` ${key}: ${info[key]}`}` itère sur chaque clé dans l'objet info et vérifie si la clé actuelle n'est pas égale à `title`. Elle ajoute ensuite la paire clé-valeur à la chaîne de texte.

La ligne `newMovieEl.textContent = text movieList.append(newMovieEl)` définit le contenu texte du nouvel élément de liste créé sur le texte généré, et ajoute le nouvel élément de liste créé à l'élément parent avec l'id `movieList`.

## Qu'est-ce que la méthode `apply()` en JavaScript ?

La méthode `apply()` est similaire à la méthode `call()`, la seule différence étant que la méthode `apply()` prend les arguments sous forme de tableau (ou d'objet de type tableau), tandis que les arguments sont passés individuellement à la méthode `call()`.

Pour commencer avec la méthode `apply()`, vérifions sa syntaxe :

```javascript
nameOfFunction.apply(thisArg, [argsArray])

```

Le `nameOfFunction` est la fonction à appeler, `thisArg` est la valeur `this` fournie pour la fonction, et le tableau ou l'objet de type tableau est le `argsArray` à passer à la fonction.

```javascript
const game = {
  fullDetail: function () {
    return this.title + " " + this.year;
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.apply(newGame);
console.log(fullDetail); // Output: Merlin 1994

```

Tout comme dans la méthode `call()`, il y a des objets `game` et `newGame`. Le `game` a une méthode `fullDetail`, tandis que le `newGame` a des propriétés de titre et d'année.

Comme nous le savons à partir de la définition ci-dessus, la méthode `apply()` a utilisé le contexte de `newGame` pour invoquer la méthode `fullDetail` de l'objet `game`.

Cela signifie que nous avons accès aux propriétés de `newGame` car le `this` à l'intérieur de `fullDetail` fait référence à l'objet `newGame`.

Nous avons maintenant une connexion entre le `game` et le `newGame` avec l'aide de la méthode `apply()`.

La méthode `apply()` peut également être utilisée pour passer un tableau ou une collection de type tableau comme argument.

```javascript
const game = {
  fullDetail: function (greet) {
    return `${greet} ${this.title} ${this.year}`;
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.apply(newGame, ["Welcome"]);
console.log(fullDetail); // Output: Welcome Merlin 1994

```

Le code ci-dessus montre que la fonction `fullDetail` à l'intérieur de l'objet `game` attend un paramètre `greet`. La méthode `apply()` est utilisée pour invoquer `fullDetail` avec l'objet `newGame` et le tableau `['Welcome']` comme argument passé à la fonction.

### Comment utiliser la méthode apply() dans une application réelle

<iframe height="300" style="width: 100%;" scrolling="no" title="Apply" src="https://codepen.io/kamal90/embed/GRLWYoN?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/GRLWYoN">
  Apply</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Le code suivant a été extrait du code ci-dessus :

```javascript
const newMovie = {
    info: {
      title,
      [extraName]: extraValue,
    },
    id: Math.random(),
    formatted() {
      return this.info.title.toUpperCase();
    }
  };

```

Le code ci-dessus est un objet nommé `newMovie`. Dans l'objet `newMovie`, un objet `info` avec `title` et `extraName` a été créé.

Le `title` est le nom du film, tandis que la ligne `[extraName]` utilise la notation entre crochets pour accéder dynamiquement à l'entrée utilisateur, en utilisant la valeur de la variable comme nom de clé. Alors que `extraValue` est la valeur associée à la clé.

L'`id` est l'identifiant unique qui génère un nombre aléatoire en utilisant la fonction `Math.random()`.

La méthode `formatted()` retourne le format en majuscules du titre. En utilisant `this.info.title`, où l'objet `newMovie` est le même que `this`, et `info` est un objet à l'intérieur de `newMovie` qui contient des informations comme le titre, et le reste.

```javascript

filteredMovies.forEach((movie) => {
    const newMovieEl = document.createElement('li');
    const {info} = movie;
    const {formatted} = movie
    let text = formatted.apply(movie) + '-';
    for (const key in info) {
      if (key !== 'title') {
        text = text + `${key}: ${info[key]}`
      }
    }
    newMovieEl.textContent = text;
    movieList.append(newMovieEl)

  })
}

```

Le code ci-dessus montre les utilisations de la méthode `apply()` dans une application réelle.

Maintenant, expliquons le code.

La ligne `const newMovieEl = document.createElement('li');` crée un nouvel élément `<li>` en utilisant `document.createElement('li')`, avec le nouvel élément stocké dans la constante `newMovieEl`.

La ligne `const {info} = movie;` utilise l'affectation de déstructuration pour extraire la propriété `info` de l'objet movie.

La ligne `const {formatted} = movie` utilise l'affectation de déstructuration pour extraire la méthode `formatted` de l'objet movie.

La ligne `let text = formatted.apply(movie) + '-';` montre comment utiliser la méthode `apply()` dans une application.

L'invocation de la fonction `formatted` directement ne donnera pas le résultat requis, car la fonction de `this` dans ce contexte est l'objet window.

En utilisant la méthode `apply` sur la fonction `formatted`, la méthode `apply()` permet de changer le contexte de `this` de l'objet window à l'objet `movie`.

Comme dit ci-dessus, en JavaScript, la méthode `apply()` prend les arguments sous forme de tableau (ou d'objet de type tableau), et exécute la fonction instantanément.

La ligne `for (const key in info) {if (key !== 'title') {text = text +` ${key}: ${info[key]}`}` itère sur chaque clé dans l'objet info et vérifie si la clé actuelle n'est pas égale à `title`.

Elle ajoute ensuite la paire clé-valeur à la chaîne de texte.

La ligne `newMovieEl.textContent = text movieList.append(newMovieEl)` définit le contenu texte du nouvel élément de liste créé sur le texte généré, et ajoute le nouvel élément de liste créé à l'élément parent avec l'id `movieList`.

## Qu'est-ce que la méthode `bind()` en JavaScript ?

La méthode `bind()` crée une nouvelle fonction qui a son mot-clé `this` défini sur la valeur fournie et n'appelle pas immédiatement la fonction.

Elle est disponible sur toutes les fonctions JavaScript et est utilisée pour définir de manière permanente le contexte `this` pour une fonction.

La différence entre les méthodes `call()`, `apply()`, et `bind()` est que la méthode `bind()` crée une nouvelle fonction avec un `this` lié, tandis que `call()` et `apply()` sont des méthodes à usage unique qui ne créent pas de nouvelle fonction.

La méthode `bind()` n'appelle pas immédiatement la fonction, mais `call()` et `apply()` appellent la fonction instantanément.

Regardons la syntaxe de la méthode `bind()` :

```javascript
functionName.bind(thisArg[, arg1[, arg2[, ...]]])

```

Le `thisArg` représente la valeur à passer comme valeur `this` chaque fois que la fonction est exécutée, et les `arg1, arg2, ...` sont les arguments liés à la fonction lorsqu'elle est invoquée.

```javascript

const player = {
  name: "Rooney",
  jerseyNumber: 10,
  introduction: function () {
    console.log(this.name + "wears Jersey number " + this.jerseyNumber + ".");
  },
};
const player2 = {
  name: "Jimmy ",
  jerseyNumber: 18,
};

let result = player.introduction.bind(player2);

result(); // Jimmy wears Jersey number 18.

```

Dans le code ci-dessus, lorsque vous appelez `result()`, il imprime `Jimmy wears Jersey number 18`. Cela est possible car le mot-clé `this` à l'intérieur de la méthode introduction est lié à l'objet `player2`.

Il est également possible d'utiliser la méthode `bind()` avec plus d'un argument.

```javascript
const player = {
  name: "Rooney",
  jerseyNumber: 10,
  introduction: function (goals, country) {
    console.log(
      `${this.name} wears Jersey number ${this.jerseyNumber}, he plays for ${country}, and he has scored ${goals} goals`,
    );
  },
};
const player2 = {
  name: "Jimmy ",
  jerseyNumber: 18,
};

let result = player.introduction.bind(player2, 87, "Nigeria");

result(); // Jimmy  wears Jersey number 18, he plays for Nigeria, and he has scored 87 goals

```

Dans l'exemple ci-dessus, deux paramètres ont été passés : `thisArg` et `arg1`. Ensuite, l'objet `player2` est lié à la méthode `introduction` qui a deux paramètres : `goals` et `country`.

### Comment utiliser la méthode bind() dans une application réelle

Pour une compréhension appropriée de l'utilisation de la méthode `bind()` dans une application réelle, il est nécessaire de montrer l'application sans la méthode `bind()`.

La calculatrice non conventionnelle est le nom de l'application que nous allons construire pour cet exercice.

<iframe height="300" style="width: 100%;" scrolling="no" title="Untitled" src="https://codepen.io/kamal90/embed/qBwRWwX?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/qBwRWwX">
  Untitled</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Décomposons le code.

Le code ci-dessus crée une calculatrice non conventionnelle simple dans le but de réaliser des opérations arithmétiques de base (addition, soustraction, division et multiplication).

Il prend l'entrée de l'utilisateur, met à jour le résultat affiché et enregistre les calculs.

* La fonction `outputResult(answer, text)` met à jour le résultat et le texte de calcul.
* La fonction `getUserInput()` récupère l'entrée de l'utilisateur à partir du champ d'entrée.
* La tâche de `writeToLog(operationidentifier, older, olderTwo, newResult)` est de formater la chaîne de calcul pour une sortie.
* La fonction `createLog(operationidentifier, older, olderTwo, newResult)` crée un objet de journal pour le calcul et le stocke dans un tableau.
* La fonction `createOutput(conditional)` effectue la logique de calcul principale en fonction de l'opération fournie. Les opérations comme `add()`, `subtract()`, `divide()`, et `multiply()` déclenchent des calculs pour leurs opérations respectives.

Voici le code avec la fonction `bind()` :

<iframe height="300" style="width: 100%;" scrolling="no" title="Unconventional Calculator" src="https://codepen.io/kamal90/embed/MWRjXWg?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/MWRjXWg">
  Unconventional Calculator</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Le code ci-dessus crée une fonctionnalité de calculatrice simple en JavaScript.

Le code prend une entrée de l'utilisateur, effectue des calculs basés sur des clics de bouton, met à jour l'interface utilisateur avec les résultats et maintient un journal des calculs passés.

Décomposons le code JavaScript dans les sections suivantes.

#### Sélectionner tous les éléments HTML

Le code sélectionne tous les éléments HTML en utilisant leurs identifiants.

Les éléments `addButton`, `subtractButton`, `divideButton`, et `multiplyButton` sont des éléments pour afficher l'historique des calculs.

Le `result` est l'élément pour afficher le résultat actuel et le `inputNumber` est un champ d'entrée pour l'entrée utilisateur.

#### Créer des fonctions pour la sortie et l'entrée utilisateur

La fonction `outputResult (answer, text)` affiche la réponse fournie dans l'élément `result` et le texte dans l'élément `calculation`.

La fonction `getUserInput()` obtient la valeur entrée dans le champ `inputNumber` et la convertit en entier.

#### Créer des variables pour le calcul et la journalisation

`defaultResult` est une constante définie sur `0`, utilisée comme résultat initial.

`currentResult` est une variable pour stocker le résultat actuel des calculs.

`logEntries` est un tableau qui stocke les entrées de journal pour l'historique des calculs.

Pour les fonctions de journalisation, la fonction `writeToLog(prevResult, operand, original)` met à jour l'interface utilisateur avec la description du calcul et appelle la fonction `outputResult`.

La fonction `createLog (operationidentifier, older, olderTwo, newResult)` crée une entrée de journal et la pousse dans le tableau `logEntries`.

#### Créer une fonction de calcul

La fonction `calculate (operation)` prend une chaîne d'opération en entrée (`ADD`, `SUBTRACT`, `DIVIDE`, ou `MULTIPLY`). Elle effectue des calculs basés sur les opérations suivantes :

Elle additionne pour `ADD`, soustrait pour `SUBTRACT`, divise pour `DIVIDE`, multiplie pour `MULTIPLY`.

Les fonctions `writeToLog` et `createLog` sont appelées pour journaliser le calcul.

#### Créer des écouteurs d'événements pour les boutons

La ligne `addButton.addEventListener('click',calculate.bind(this, 'ADD')` attribue un écouteur d'événement au `addButton`.

Des écouteurs d'événements similaires sont attribués aux boutons `subtractButton`, `divideButton`, et `multiplyButton` pour leurs opérations respectives.

Le code indique que la fonction `calculate` sera exécutée chaque fois qu'un bouton est cliqué. La fonction est liée avec la méthode `bind()`, et des arguments tels que `ADD`, `SUBTRACT`, `MULTIPLY`, et `DIVIDE` sont passés à la fonction `calculate`.

## Pourquoi les méthodes `call()`, `apply()`, et `bind()` ont-elles été introduites en JavaScript ?

Avec ces méthodes, les applications JavaScript sont plus dynamiques et adaptables. Cela donne au programmeur plus de contrôle sur la manière dont la fonction est exécutée.

Il est généralement difficile d'avoir une compréhension complète du mot-clé `this` en JavaScript. Par conséquent, l'introduction des méthodes `call()`, `apply()`, et `bind()` donne aux programmeurs plus de contrôle sur ce sujet capricieux.

Disons que vous êtes un footballeur polyvalent qui peut jouer confortablement à différentes positions sur le terrain. Dans un match de football régulier, votre entraîneur vous attribue une aile spécifique (la fonction) et vous jouez selon les instructions de l'entraîneur (le code de la fonction), et les autres footballeurs avec lesquels vous êtes sur le terrain (les arguments).

Avec la méthode `call()`, votre entraîneur peut temporairement vous placer dans une position différente sur le terrain (définir la valeur `this`) pour un match spécifique. Cela vous permet d'utiliser vos compétences en football même sur l'aile où vous ne jouez pas normalement.

Avec la méthode `apply()`, c'est comme avoir une tactique de football entière (arguments) pleine de différentes fautes techniques, tactiques de retardement, et bien plus encore. L'entraîneur peut vous lancer toute la tactique, et vous pouvez tout utiliser (exécution de fonction avec un contexte spécifique) pour le match.

Avec la méthode `bind()`, imaginez que votre entraîneur crée un rôle de doublure spécial (fonction `bound()`) juste pour vous. Ce rôle de doublure a toujours une aile spécifique sur le terrain (valeur `this` prédéfinie) prête, afin que vous puissiez intervenir de manière transparente et exécuter les instructions (exécution de fonction) chaque fois que nécessaire.

## Quelles sont les différences entre les méthodes `call()`, `apply()`, et `bind()` ?

En ce qui concerne la gestion des arguments :

* La méthode `call()` accepte les arguments individuellement sous forme de liste séparée par des virgules.
* Avec la méthode `apply()`, les arguments sont acceptés sous forme de tableau ou d'objet de type tableau.
* La méthode `bind()` peut passer des arguments supplémentaires lorsque la nouvelle fonction est invoquée.

En ce qui concerne l'invocation et l'exécution :

* La méthode `call()` invoque la fonction immédiatement avec les arguments individuels spécifiques et la valeur `this` spécifiée, et elle accepte les arguments un par un.
* La méthode `apply()` invoque la fonction instantanément, tout comme la méthode `call()`, mais avec la différence qu'elle accepte les arguments sous forme de tableau ou d'objet de type tableau.
* La méthode `bind()` crée une nouvelle fonction avec des arguments optionnels et une valeur `this` spécifiée. Elle n'invoque pas immédiatement la fonction, car elle lie la fonction pour une exécution ultérieure.

## Pourquoi utiliser les méthodes `call()`, `apply()`, et `bind()` en JavaScript ?

Les méthodes `call()`, `apply()`, et `bind()` traitent largement de la manière de contrôler le contexte d'une fonction (mot-clé `this`) et les arguments lorsqu'elle est appelée.

Il existe plusieurs avantages à utiliser ces méthodes en JavaScript :

* **Changer la valeur du mot-clé `this`** : Le mot-clé `this` fait référence à l'objet qui appelle une certaine fonction. Avec l'aide de ces méthodes, vous pouvez définir explicitement la valeur du mot-clé `this` à autre chose.
* **Gestion des événements** : Les méthodes `call()` et `apply()` peuvent garantir que le gestionnaire est exécuté avec le contexte et les arguments corrects, même si son espace de définition est différent de l'espace d'invocation.
* **Arguments flexibles** : Ces méthodes prennent des arguments de différentes manières. La méthode `call()` prend un argument individuel, la méthode `apply()` prend un argument sous forme de tableau, et la méthode `bind()` permet de pré-définir certains arguments pour une utilisation ultérieure.
* **Fonction partielle** : La méthode `bind()` crée une nouvelle fonction composée d'un contexte prédéfini et d'arguments initiaux optionnels. Cela est très utile pour les applications partielles, où certains arguments sont fixés à l'avance, avec d'autres à fournir à un stade ultérieur.
* **Emprunt de fonctions** : Ces méthodes utilisent une fonction d'un nouvel objet à un autre ensemble d'objets entièrement.

En résumé, elles vous donnent suffisamment d'espace pour contrôler l'exécution des fonctions en JavaScript.

## Conclusion

Dans ce tutoriel, vous avez appris comment déterminer implicitement (basé sur le contexte) et explicitement (en utilisant les méthodes `call()`, `apply()`, et `bind()`) la valeur du mot-clé `this`.