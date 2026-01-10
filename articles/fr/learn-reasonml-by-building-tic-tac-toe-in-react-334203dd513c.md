---
title: Apprendre ReasonML en construisant un Tic Tac Toe dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-17T17:23:12.000Z'
originalURL: https://freecodecamp.org/news/learn-reasonml-by-building-tic-tac-toe-in-react-334203dd513c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-ANKA_z3Mz_RFYKRjPnSNQ.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: reasonml
  slug: reasonml
- name: Web Development
  slug: web-development
seo_title: Apprendre ReasonML en construisant un Tic Tac Toe dans React
seo_desc: 'By David Kopal


  3. 7. 2018: UPDATED to ReasonReact v0.4.2


  You may have heard of Reason before. It’s a syntax on top of OCaml that compiles
  to both readable JavaScript code and to native and bytecode as well.

  This means you could potentially write a ...'
---

Par David Kopal

> **_3. 7. 2018: MIS À JOUR vers ReasonReact v0.4.2_**

Vous avez peut-être déjà entendu parler de [Reason](https://reasonml.github.io/). C'est une syntaxe basée sur [OCaml](https://ocaml.org/) qui compile à la fois en code JavaScript lisible et en natif et bytecode.

Cela signifie que vous pourriez potentiellement écrire [une seule application](https://github.com/jaredly/gravitron) en utilisant la syntaxe Reason, et être en mesure de l'exécuter dans le navigateur, ainsi que sur les téléphones Android et iOS.

C'est l'une des raisons pour lesquelles Reason (ouch, jeu de mots) devient de plus en plus populaire. Cela est particulièrement vrai dans la communauté JavaScript en raison des similitudes de syntaxe.

Si vous étiez un développeur JavaScript avant la sortie de Reason et que vous vouliez apprendre un langage de programmation fonctionnelle (FP), vous auriez dû également apprendre une toute nouvelle syntaxe et un ensemble de règles. Cela aurait pu décourager beaucoup de gens.

Avec Reason, vous devez principalement comprendre les principes de la FP sur lesquels il est basé — comme l'immuabilité, le currying, la composition et les fonctions d'ordre supérieur.

Avant de découvrir Reason, j'essayais d'utiliser les principes de la FP en JavaScript autant que possible. Cependant, JavaScript est limité dans ce sens, puisqu'il n'est pas conçu pour être un langage FP. Pour tirer parti de ces principes efficacement, vous devez utiliser un ensemble de bibliothèques qui créent des abstractions compliquées qui vous sont cachées.

Reason, en revanche, ouvre tout le domaine de la FP à tous les développeurs JavaScript intéressés. Il nous offre l'opportunité d'utiliser toutes ces fonctionnalités cool d'OCaml en utilisant une syntaxe que nous connaissons bien.

Enfin, mais non des moindres, nous pouvons écrire nos applications [React](https://reasonml.github.io/reason-react/) ou [React Native](https://github.com/reasonml-community/bs-react-native) en utilisant Reason.

### Pourquoi devriez-vous essayer Reason ?

J'espère que vous découvrirez la réponse par vous-même une fois que vous aurez terminé de lire cet article.

Alors que nous parcourons le code source du jeu classique Tic Tac Toe — écrit en Reason, en utilisant React — je vais expliquer les fonctionnalités principales du langage. Vous verrez les avantages du système de typage fort, de l'immuabilité, de la correspondance de motifs, de la composition fonctionnelle utilisant le pipe, et ainsi de suite. Contrairement à JavaScript, ces fonctionnalités sont intrinsèques à Reason lui-même.

### Échauffement

Avant de vous retrousser les manches, vous devez installer Reason sur votre machine en suivant [ce guide](https://reasonml.github.io/docs/en/installation).

Après cela, vous devez configurer votre application. Pour ce faire, vous pouvez soit cloner [mon dépôt](https://github.com/codinglawyer/reason-tic-tac-toe) contenant le code de notre application, soit configurer votre propre projet en utilisant [ReasonScripts](https://github.com/reasonml-community/reason-scripts) et coder en même temps.

Pour visualiser votre application dans le navigateur, vous devez d'abord compiler vos fichiers Reason en fichiers JavaScript. Le compilateur [BuckleScript](https://bucklescript.github.io/) s'en chargera.

En d'autres termes, lorsque vous exécutez `npm start` (dans le projet ReasonScripts), votre code Reason est compilé en JavaScript. Le résultat de la compilation est ensuite rendu dans le navigateur. Vous pouvez voir par vous-même à quel point le code compilé est lisible en vérifiant le dossier `lib` à l'intérieur de votre application.

### Notre premier composant

![Image](https://cdn-media-1.freecodecamp.org/images/GBLERj-jp68NeaR1Ray8hXWUIfsItL0Gf8Y1)

Comme nous l'avons déjà mentionné, notre application Tic Tac Toe est écrite en utilisant la bibliothèque [ReasonReact](https://github.com/reasonml/reason-react). Cela rend Reason accessible pour les développeurs JavaScript, et beaucoup de nouveaux venus viennent de cette communauté.

Notre application a une structure de composant classique, comme toute autre application React. Nous allons parcourir les composants de haut en bas lorsque nous parlerons de l'interface utilisateur, et de bas en haut lorsque nous décrirons leur logique.

Commençons par jeter un coup d'œil au composant de niveau supérieur `App`.

```jsx
let component = ReasonReact.statelessComponent("App");
let make = _children => {
  ...component,
  render: _self =>
    <div>
       <div className="title">
         (ReasonReact.string("Tic Tac Toe"))
       </div>
       <Game />
    </div>,
};
```

Le composant est créé lorsque vous appelez `ReasonReact.statelessComponent` et que vous lui passez le nom du composant. Vous n'avez pas besoin de mots-clés de classe comme dans React, puisque Reason n'en a aucun.

Le composant n'est ni une classe ni une fonction — c'est ce qu'on appelle un [record](https://reasonml.github.io/docs/en/record.html). `record` est l'une des structures de données de Reason, qui est similaire à l'objet JavaScript. Contrairement à ce dernier, cependant, `record` est immuable.

Notre nouveau composant `record` contient diverses propriétés par défaut telles que l'état initial, les méthodes de cycle de vie et le rendu. Pour ajuster le composant à nos besoins, nous devons remplacer certaines de ces propriétés. Nous pouvons le faire à l'intérieur de la fonction `make` qui retourne notre composant.

Puisque le `record` est immuable, nous ne pouvons pas remplacer ses propriétés par mutation. Au lieu de cela, nous devons retourner un nouveau `record`. Pour ce faire, nous devons étendre notre composant et redéfinir les propriétés que nous voulons changer. Cela est très similaire à l'opérateur de propagation d'objet JavaScript.

Puisque `App` est un composant assez simple, nous voulons remplacer uniquement la méthode `render` par défaut afin de pouvoir rendre nos éléments à l'écran. La méthode `render` prend un seul argument `self` qui nous donne accès à l'état et aux réducteurs, comme nous le verrons plus tard.

Puisque ReasonReact supporte [JSX](https://reactjs.org/docs/introducing-jsx.html), notre fonction `render` peut retourner des éléments JSX. L'élément non capitalisé sera reconnu comme un élément DOM — `div`. L'élément capitalisé sera reconnu comme un composant — `Game`.

En raison du système de typage fort de Reason, vous ne pouvez pas simplement passer une chaîne à un élément afin de l'afficher, comme vous pouvez le faire dans React classique.

Au lieu de cela, vous devez passer une telle chaîne dans une fonction d'assistance `ReasonReact.string` qui la convertira en `reactElement` qui peut être rendu.

Puisque cela est un peu verbeux, et que nous utiliserons souvent cette fonction d'assistance, stockons-la dans une variable `toString`. Dans Reason, vous pouvez utiliser uniquement le mot-clé `let` pour le faire.

```
let toString = ReasonReact.string;
```

Avant d'aller plus loin, parlons un peu des arguments de la fonction `make`. Puisque nous ne passons aucune propriété au composant `App`, il ne prend que l'argument `children` par défaut.

Cependant, nous ne l'utilisons pas. Nous pouvons rendre cela explicite en écrivant un souligné avant. Si nous n'avions pas fait cela, le compilateur nous aurait donné un avertissement que l'argument n'est pas utilisé. Nous faisons de même avec l'argument `self` dans la méthode `render`.

Les messages d'erreur et d'avertissement compréhensibles sont une autre fonctionnalité cool qui améliorera votre expérience de développeur, par rapport à JavaScript.

### Configuration des types de variantes

![Image](https://cdn-media-1.freecodecamp.org/images/BH-VorOdK3kCiMmNYWKwfWWeSwUFBLKgYI1m)

Avant de plonger dans l'application elle-même, nous allons d'abord définir nos types.

Reason est un langage typé statiquement. Cela signifie qu'il évalue les types de nos valeurs pendant le temps de compilation. En d'autres termes, vous n'avez pas besoin d'exécuter votre application pour vérifier si vos types sont corrects. Cela signifie également que votre éditeur peut vous fournir un [support d'édition utile](https://github.com/reasonml-editor/vscode-reasonml).

Cependant, avoir un système de types ne signifie pas que vous devez définir explicitement les types pour toutes les valeurs. Si vous décidez de ne pas le faire, Reason déterminera (inférera) les types pour vous.

Nous allons tirer parti du système de types pour définir les types que nous utiliserons dans notre application. Cela nous obligera à réfléchir à la structure de notre application avant de la coder et nous obtiendrons une documentation de code en bonus.

Si vous avez déjà eu une expérience avec [TypeScript](https://www.typescriptlang.org/) ou [Flow](https://flow.org/), les types Reason vous sembleront familiers. Cependant, contrairement à ces deux bibliothèques, vous n'avez besoin d'aucune configuration préalable (je vous regarde, TypeScript). Les types sont disponibles dès le départ.

Dans Reason, nous pouvons distinguer entre [types](https://reasonml.github.io/docs/en/type.html) et [types de variantes](https://reasonml.github.io/docs/en/variant.html) (en bref, variantes). Les types sont par exemple `bool`, `string` et `int`. D'autre part, les variantes sont plus complexes. Pensez à elles comme à des ensembles énumérables de valeurs — ou plus précisément, de constructeurs. Les variantes peuvent être traitées via la correspondance de motifs, comme nous le verrons plus tard.

```
type player =
  | Cross
  | Circle;
  
type field =
  | Empty
  | Marked(player);
```

Ici, nous définissons les **variantes** `player` et `field`. Lors de la définition d'une variante, vous devez utiliser un mot-clé `type`.

Puisque nous construisons un jeu de Tic Tac Toe, nous aurons besoin de deux joueurs. Donc, le type `player` aura deux constructeurs possibles — `Cross` et `Circle`.

Si nous pensons au plateau de jeu, nous savons que chaque type `field` peut avoir deux constructeurs possibles — soit `Empty` soit `Marked` par l'un des joueurs.

Si vous regardez le constructeur `Marked`, vous pouvez voir que nous l'utilisons comme une structure de données. Nous utilisons une variante pour contenir une autre pièce de données. Dans notre cas, nous lui passons la variante `player`. Ce comportement est assez puissant car il nous permet de combiner différentes variantes et types ensemble pour créer des types plus complexes.

Donc, nous avons la variante `field`. Cependant, nous devons définir le plateau de jeu entier qui se compose de lignes de champs.

```
type row = list(field);
type board = list(row);
```

Chaque `row` est une liste de `field`s et le plateau de jeu `board` est composé d'une liste de `row`s.

La `list` est l'une des structures de données de Reason — similaire au tableau JavaScript. La différence est qu'elle est immuable. Reason a également un `array` comme liste de longueur fixe mutable. Nous reviendrons sur ces structures plus tard.

```
type gameState = 
  | Playing(player)
  | Winner(player)
  | Draw;
```

Une autre variante que nous devons définir est un `gameState`. Le jeu peut avoir trois états possibles. L'un des `player`s peut être `Playing`, être un `Winner`, ou nous pouvons avoir un `Draw`.

Maintenant, nous avons tous les types dont nous avons besoin pour composer l'état de notre jeu.

```jsx
type state = {
  board,
  gameState,
};
```

L'état de notre composant est un `record` composé du `board` et du `gameState`.

Avant d'aller plus loin, j'aimerais parler des modules. Dans Reason, les fichiers sont des modules. Par exemple, nous avons stocké toutes nos variantes dans le fichier `SharedTypes.re`. Ce code est automatiquement enveloppé dans le module comme ceci :

```jsx
module SharedTypes {
  /* code des types de variantes */
}
```

Si nous voulions accéder à ce module dans un fichier différent, nous n'avons pas besoin de mot-clé `import`. Nous pouvons facilement accéder à nos modules n'importe où dans notre application en utilisant la notation par points — par exemple `SharedTypes.gameState`.

Puisque nous utilisons nos variantes assez souvent, nous pouvons le rendre plus concis en écrivant `open SharedTypes` en haut du fichier dans lequel nous voulons accéder à notre module. Cela nous permet de supprimer la notation par points puisque nous pouvons utiliser notre module dans le scope de notre fichier.

### Établir l'état

![Image](https://cdn-media-1.freecodecamp.org/images/7mmAc2Jq5I1NBrtabAzNIPOTCH66gTLcvpv3)

Puisque nous savons à quoi ressemblera l'état de notre application, nous pouvons commencer à construire le jeu lui-même.

Nous avons vu que notre composant `App` rend le composant `Game`. C'est là que tout le plaisir commence. Je vais vous guider à travers le code étape par étape.

L'`App` était un composant sans état, similaire au composant fonctionnel dans React. D'autre part, le `Game` est un composant avec état, ce qui signifie qu'il peut contenir un état et des réducteurs. Les réducteurs dans Reason sont basés sur les mêmes principes que ceux que vous connaissez de [Redux](https://github.com/reactjs/redux). Vous appelez une action, et le réducteur la capturera et mettra à jour l'état en conséquence.

Pour voir ce qui se passe dans le composant `Game`, inspectons la fonction `make` (le code est raccourci).

```jsx
let component = ReasonReact.reducerComponent("Game");

let make = _children => {
  ...component,
  initialState: () => initialState,
  reducer: (action: action, state: state) => ...,
  render: ({state, send}) => ...,
};
```

Dans le composant `App`, nous avons remplacé uniquement la méthode `render`. Ici, nous remplaçons également les propriétés `reducer` et `initialState`. Nous parlerons des réducteurs plus tard.

`initialState` est une fonction qui (sans surprise) retourne l'état initial que nous avons stocké dans une variable.

```jsx
let initialState = {
  board: [
    [Empty, Empty, Empty],
    [Empty, Empty, Empty],
    [Empty, Empty, Empty],
  ],
  gameState: Playing(Cross),
};
```

Si vous faites défiler un peu vers le haut et vérifiez notre type `state`, vous verrez que l'`initialState` a la même structure. Il est composé du `board` qui consiste en des `row`s de `field`s. Au début du jeu, tous les champs sont `Empty`.

Cependant, leur statut peut changer au fur et à mesure que le jeu avance. Une autre partie de l'état est le `gameState` qui est initialement défini sur le joueur `Cross` qui joue en premier.

### Rendu du plateau

Jetons un coup d'œil à la méthode `render` de notre composant `Game`.

```jsx
render: ({state, send}) =>
    <div className="game">
      <Board
        state
        onRestart=(_evt => send(Restart))
        onMark=(id => send(ClickSquare(id)))
      />
    </div>,
```

Nous savions déjà qu'il reçoit l'argument `self`. Ici, nous utilisons la déstructuration pour accéder à l'`state` et à la fonction `send`. Cela fonctionne exactement comme en JavaScript.

La méthode de rendu retourne le composant `Board` et lui passe l'`state` et deux gestionnaires d'état en tant que props. Le premier s'occupe du redémarrage de l'application et le second se déclenche lorsque le champ est marqué par un joueur.

Vous avez peut-être remarqué que nous n'écrivons pas `state=state` lorsque nous passons la prop `state`. Dans Reason, si nous ne changeons pas le nom de la prop, nous pouvons passer la prop en utilisant cette syntaxe simplifiée.

Maintenant, nous pouvons jeter un coup d'œil au composant `Board`. J'ai omis la plupart de la méthode `render` pour l'instant.

```jsx
let component = ReasonReact.statelessComponent("Board");

let make = (~state: state, ~onMark, ~onRestart, _children) => {
  ...component,
  render: _ =>
    <div className="game-board">
      /* ... */
    </div>,
};
```

Le `Board` est un composant sans état. Comme vous l'avez peut-être remarqué, la fonction `make` prend maintenant plusieurs arguments. Ce sont les props que nous avons passées depuis le composant parent `Game`.

Le symbole `~` signifie que l'argument est étiqueté. Lorsque vous appelez une fonction avec un tel argument, vous devez explicitement écrire le nom de l'argument lors de l'appel de cette fonction (composant). Et c'est ce que nous avons fait lorsque nous avons passé les props dans le composant `Game`.

Vous avez peut-être également remarqué que nous faisons une autre chose avec l'un des arguments — `~state:state`. Dans la section précédente, nous avons défini notre type `state`. Ici, nous disons au compilateur que la structure de cet argument doit être la même que celle du type `state`. Vous connaissez peut-être ce motif de Flow.

![Image](https://cdn-media-1.freecodecamp.org/images/G9CmB7A70emHKIGRogQ0uKXPKrrKQw3AwjcH)

Revenons à la méthode `render` du composant `Board`.

Puisque nous traitons des listes ici, nous allons en parler un peu plus maintenant, avant d'inspecter le reste de la méthode `render`.

### Excursion I : liste et tableau

Dans Reason, nous avons deux structures de données ressemblant aux tableaux JavaScript — `list` et `array`. La `list` est immuable et redimensionnable, tandis que l'`array` est mutable et a une longueur fixe. Nous utilisons une `list` en raison de sa flexibilité et de son efficacité qui se révèle vraiment lorsque nous l'utilisons de manière récursive.

Pour mapper une `list`, vous pouvez utiliser la méthode `List.map` qui reçoit deux arguments — une fonction et une `list`. La fonction prend un élément de la `list` et le mappe. Cela fonctionne presque comme le `Array.map` de JavaScript. Voici un exemple simple :

```jsx
let numbers = [1, 5, 8, 9, 15];
let increasedNumbers = List.map((num) => num + 2, numbers);
Js.log(increasedNumbers);  /* [3,[7,[10,[11,[17,0]]]]] */
```

Quoi ? Vous dites que le résultat imprimé semble bizarre ? C'est parce que les listes dans Reason sont [liées](https://en.wikipedia.org/wiki/Linked_list).

L'impression des listes dans votre code peut être déroutante. Heureusement, vous pouvez la convertir en un `array` en utilisant la méthode `Array.of_list`.

```jsx
Js.log(Array.of_list(increasedNumbers));  /* [3,7,10,11,17] */
```

Revenons à notre application et rappelons-nous à quoi ressemble notre `state`.

```jsx
let initialState = {
  board: [
    [Empty, Empty, Empty],
    [Empty, Empty, Empty],
    [Empty, Empty, Empty],
  ],
  gameState: Playing(Cross),
};
```

À l'intérieur de la méthode `render` du Board, nous commençons par mapper sur `board` qui est composé d'une liste de lignes. Donc, en le mappant, nous obtiendrons accès aux `row`s. Ensuite, nous rendons le composant `BoardRow`.

```jsx
let component = ReasonReact.statelessComponent("Board");

let make = (~state: state, ~onMark, ~onRestart, _children) => {
   ...component,
   render: _ =>
      <div className="game-board">
         ( 
            ReasonReact.array(
               Array.of_list(
                  List.mapi(
                    (index: int, row: row) =>
                     <BoardRow
                        key=(string_of_int(index))
                        gameState=state.gameState
                        row
                        onMark
                        index
                     />,
                   state.board,
                 ),
             ),
           )
        )
     /* ... */
```

Nous utilisons la méthode `List.mapi`, qui nous fournit un argument `index` dont nous avons besoin pour définir de manière unique nos ids.

Lorsque nous mappons la `list` aux éléments JSX, nous devons faire deux choses supplémentaires.

Premièrement, nous devons la convertir en un `array` en utilisant `Array.of_list`. Deuxièmement, nous devons convertir le résultat en `reactElement` en utilisant `ReasonReact.array`, puisque nous (comme déjà mentionné) ne pouvons pas simplement passer la chaîne à l'élément JSX comme dans React.

Pour obtenir les valeurs des champs, nous devons mapper chaque `row` également. Nous faisons cela à l'intérieur du composant `BoardRow`. Ici, chaque élément de la `row` est ensuite mappé au composant `Square`.

```jsx
let component = ReasonReact.statelessComponent("BoardRow");

let make = (~gameState: gameState, ~row: row, ~onMark, ~index: int, _children) => {
   ...component,
   render: (_) =>
      <div className="board-row">
         (ReasonReact.array(
            Array.of_list(
               List.mapi(
                  (ind: int, value: field) => {
                    let id = string_of_int(index) ++ string_of_int(ind);
                    <Square
                       key=id
                       value
                       onMark=(() => onMark(id))
                       gameState
                    />;
                 },
               row,
             ),
          ),
        ))
    </div>,
};
```

En utilisant ces deux mappages, notre plateau est rendu. Vous serez d'accord avec moi pour dire que la lisibilité de ce code n'est pas très bonne à cause de toutes les enveloppes de fonctions.

Pour l'améliorer, nous pouvons utiliser l'opérateur `pipe` qui prend nos données `list` et les passe à travers nos fonctions. Voici le deuxième exemple de mappage — cette fois en utilisant `pipe`.

```jsx
let component = ReasonReact.statelessComponent("BoardRow");

let make = (~gameState: gameState, ~row: row, ~onMark, ~index: int, _children) => {
   ...component,
   render: (_) =>
      <div className="board-row">
         (
            row
            |> List.mapi((ind: int, value: field) => {
               let id = string_of_int(index) ++ string_of_int(ind
               <Square 
                 key=id
                 value
                 onMark=(() => onMark(id))
                 gameState
               />;
             })
            |> Array.of_list
            |> ReasonReact.array
         )
      </div>,
};
```

Cela rend notre code beaucoup plus lisible, ne pensez-vous pas ? D'abord, nous prenons la `row` et la passons à la méthode de mappage. Ensuite, nous convertissons notre résultat en un `array`. Enfin, nous le convertissons en `reactElement`.

En mappant notre plateau, nous rendons un ensemble de composants `Square` à l'écran et en faisant cela, nous créons le plateau de jeu entier.

Nous passons quelques props au `Square`. Puisque nous voulons que notre `id` soit unique, nous le créons en combinant les indices des deux mappages. Nous passons également la `value` qui contient le type `field` qui peut être soit `Empty` soit `Marked`.

Enfin, nous passons un `gameState` et le gestionnaire `onMark` qui sera invoqué lorsqu'un `Square` particulier est cliqué.

### Entrée des champs

![Image](https://cdn-media-1.freecodecamp.org/images/GEIYAkhGbe884pLggpWM4JAVEww3pR0JQYmg)

```jsx
let component = ReasonReact.statelessComponent("Square");

let make = (~value: field, ~gameState: gameState, ~onMark, _children) => {
  ...component,
  render: _self =>
    <button
      className=(getClass(gameState, value))
      disabled=(gameState |> isFinished |> Js.Boolean.to_js_boolean)
      onClick=(_evt => onMark())>
      (value |> toValue |> toString)
    </button>,
};
```

Le composant `Square` rend un bouton et lui passe quelques props. Nous utilisons quelques fonctions d'assistance ici, mais je ne parlerai pas de toutes en détail. Vous pouvez les trouver toutes dans le [dépôt](https://github.com/codinglawyer/reason-tic-tac-toe).

La classe du bouton est calculée en utilisant la fonction d'assistance `getClass` qui rend le carré vert lorsque l'un des joueurs gagne. Lorsque cela se produit, tous les `Square`s seront également désactivés.

Pour rendre la `value` du bouton, nous utilisons deux helpers.

```jsx
let toValue = (field: field) =>
  switch (field) {
  | Marked(Cross) => "X"
  | Marked(Circle) => "O"
  | Empty => ""
};
```

`toValue` convertira le type `field` en chaîne en utilisant la correspondance de motifs. Nous parlerons de la correspondance de motifs plus tard. Pour l'instant, vous devez savoir que nous faisons correspondre les données `field` à nos trois motifs. Donc, le résultat serait `X`, `O`, ou une chaîne vide. Ensuite, nous utilisons `toString` pour le convertir en `reactElement`.

Ouf. Nous venons de rendre le plateau de jeu. Faisons un rapide récapitulatif de la façon dont nous l'avons fait.

Notre composant de niveau supérieur `App` rend le composant `Game` qui contient l'état du jeu et le transmet avec les gestionnaires au composant `Board`.

Le `Board` prend ensuite la prop d'état du plateau et mappe les lignes au composant `BoardRow` qui mappe les lignes aux composants `Square`. Chaque `Square` a un gestionnaire onClick qui le remplira avec un carré ou un cercle.

### Faites-le faire quelque chose déjà !

Jetons un coup d'œil à la façon dont notre logique contrôlant le jeu fonctionne.

Puisque nous avons un plateau, nous pouvons permettre à un joueur de cliquer sur n'importe quel carré. Lorsque cela se produit, le gestionnaire `onClick` est déclenché et le gestionnaire `onMark` est appelé.

```jsx
/* Composant Square */
<button
  className=(getClass(gameState, value))
  disabled=(gameState |> isFinished |> Js.Boolean.to_js_boolean)
  onClick=(_evt => onMark())>
  (value |> toValue |> toString)
</button>
```

Le gestionnaire `onMark` a été passé depuis le composant `BoardRow`, mais il a été initialement défini dans le composant `Game` qui s'occupe de l'état.

```jsx
/* Composant Game */
render: ({state, send}) =>
    <div className="game">
      <Board
        state
        onRestart=(_evt => send(Restart))
        onMark=(id => send(ClickSquare(id)))
      />
    </div>,
```

Nous pouvons voir que la prop `onMark` est un réducteur `ClickSquare`, ce qui signifie que nous l'utilisons pour mettre à jour l'état (comme dans Redux). Le gestionnaire `onRestart` fonctionne de manière similaire.

Remarquez que nous passons l'`id` unique du carré au gestionnaire `onMark` à l'intérieur du composant `BoardRow`.

```jsx
/* Composant BoardRow */
(
  row
  |> List.mapi((ind: int, value: field) => {
    let id = string_of_int(index) ++ string_of_int(ind
    <Square 
      key=id
      value
      onMark=(() => onMark(id))
      gameState
    />;
   })
  |> Array.of_list
  |> ReasonReact.array
)
```

Avant de regarder nos réducteurs en détail, nous devons définir des actions auxquelles nos réducteurs répondront.

```jsx
type action =
  | ClickSquare(string)
  | Restart;
```

Comme pour les types de variantes globaux, cela nous oblige à réfléchir à notre logique avant de commencer à l'implémenter. Nous définissons deux variantes d'action. `ClickSquare` prend un argument qui aura un type de `string`.

Maintenant, jetons un coup d'œil à nos réducteurs.

```jsx
let updateBoard = (board: board, gameState: gameState, id) =>
  board
  |> List.mapi((ind: int, row: row) =>
    row
      |> List.mapi((index: int, value: field) =>
        string_of_int(ind) ++ string_of_int(index) === id ?
          switch (gameState, value) {
          | (_, Marked(_)) => value
          | (Playing(player), Empty) => Marked(player)
          | (_, Empty) => Empty
          } :
          value
      )
  );
  
reducer: (action: action, state: state) =>
    switch (action) {
    | Restart => ReasonReact.Update(initialState)
    | ClickSquare((id: string)) =>
       let updatedBoard = updateBoard(state.board, state.gameState, id);
       ReasonReact.Update({
         board: updatedBoard,
         gameState:
            checkGameState3x3(updatedBoard, state.board, state.gameState),
       });
    },
```

Le réducteur `ClickSquare` prend un `id` du `Square` particulier. Comme nous l'avons vu, nous le passons dans le composant `BoardRow`. Ensuite, notre réducteur calcule un nouvel état.

Pour la mise à jour de l'état du `board`, nous appellerons la fonction `updateBoard`. Elle utilise la même logique de mappage que nous avons utilisée dans les composants `Board` et `BoardRow`. À l'intérieur, nous mappons sur le `state.board` pour obtenir les lignes, puis nous mappons sur les lignes pour obtenir les valeurs des champs.

Puisque l'`id` de chaque carré est une composition d'ids des deux mappages, nous l'utiliserons pour trouver le champ sur lequel le joueur a cliqué. Lorsque nous le trouvons, nous utiliserons la correspondance de motifs pour déterminer quoi en faire. Sinon, nous laisserons la `value` du carré inchangée.

### Excursion II : correspondance de motifs

![Image](https://cdn-media-1.freecodecamp.org/images/fiLwW5agrPnevGF1Y-ZgXjbpfmEZbmE85YV1)

Nous utilisons la correspondance de motifs pour traiter nos données. Nous définissons des **motifs** que nous ferons correspondre à nos **données**. Lorsque nous utilisons la correspondance de motifs dans Reason, nous utilisons une instruction `switch`.

```jsx
switch (state.gameState, value) {
  | (_, Marked(_)) => value
  | (Playing(player), Empty) => Marked(player)
  | (_, Empty) => Empty
}
```

Dans notre cas, nous utilisons un [tuple](https://reasonml.github.io/docs/en/tuple.html) pour représenter nos **données**. Les tuples sont des structures de données qui séparent les données avec des virgules. Notre `tuple` contient le `gameState` et la `value` (contenant le type `field`).

Ensuite, nous définissons plusieurs **motifs** que nous ferons correspondre à nos données. La première correspondance détermine le résultat de toute la correspondance de motifs.

En écrivant un souligné à l'intérieur du motif, nous disons au compilateur que nous ne nous soucions pas de la valeur particulière. En d'autres termes, nous voulons une correspondance à chaque fois.

Par exemple, le premier motif est apparié lorsque la `value` est `Marked` par n'importe quel joueur. Donc, nous ne nous soucions pas du `gameState` et nous ne nous soucions pas non plus du type de joueur.

Lorsque ce motif est apparié, le résultat est la `value` originale. Ce motif empêche les joueurs de remplacer les `Squares` déjà marqués.

Le deuxième motif traite la situation lorsque n'importe quel joueur joue et que le champ est `Empty`. Ici, nous utilisons le type `player` dans le motif et ensuite à nouveau dans le résultat. Nous disons essentiellement que nous ne nous soucions pas de quel joueur joue (`Circle` ou `Cross`), mais que nous voulons toujours marquer le carré selon le joueur qui joue réellement.

Le dernier motif agit comme celui par défaut. Si le premier ou le deuxième motif n'est pas apparié, le troisième sera toujours apparié. Ici, nous ne nous soucions pas du `gameState`.

Cependant, puisque nous vérifions l'état de jeu `Playing` dans le motif précédent, nous vérifions maintenant l'état de jeu `Draw` ou `Winner`. Si c'est le cas, nous laisserons le champ `Empty`. Ce scénario par défaut empêche les joueurs de continuer à jouer lorsque le jeu est terminé.

Une chose cool à propos de la correspondance de motifs dans Reason est que le compilateur vous avertira si vous n'avez pas couvert toutes les correspondances de motifs possibles. Cela vous épargnera beaucoup de problèmes, car vous saurez toujours si vous avez couvert tous les scénarios possibles. Donc, si le compilateur ne vous donne aucun avertissement, votre correspondance de motifs ne échouera jamais.

Lorsque la correspondance de motifs est terminée, le champ particulier est mis à jour. Lorsque tous les mappages sont terminés, nous obtenons un nouvel état de plateau et le stockons comme `updatedBoard`. Nous pouvons ensuite mettre à jour l'état du composant en appelant `ReasonReact.Update`.

```jsx
ReasonReact.Update({
  board: updatedBoard,
  gameState:
    checkGameState3x3(updatedBoard, state.board, state.gameState),
```

Nous mettons à jour l'état du `board` en utilisant le résultat de la correspondance de motifs. Lorsque nous mettons à jour le `gameState`, nous appelons l'assistant `checkGameState3x3` qui calcule l'état du jeu pour nous.

### Avons-nous un gagnant ?

![Image](https://cdn-media-1.freecodecamp.org/images/te2QEBpX1w-XX4HghCfe543FZVCCHR5n6ma9)

Jetons un coup d'œil à ce que fait `checkGameState3x3`.

Tout d'abord, nous devons définir toutes les combinaisons possibles de champs gagnants (pour le plateau 3x3) et les stocker sous forme de `winningCombs`. Nous devons également définir le type `winningRows`.

```jsx
type winningRows = list(list(int));

let winningCombs = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],  
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];
```

Nous avons passé cette liste à la fonction `checkGameState` en tant que premier argument.

```jsx
let checkGameState3x3 = checkGameState(winningCombs);
```

En faisant cela, nous tirons parti du principe de [currying](https://en.wikipedia.org/wiki/Currying). Lorsque nous passons les `winningCombs` à la fonction `checkGameState`, nous obtenons une nouvelle fonction attendant que le reste des arguments soit passé. Nous stockons cette nouvelle fonction sous le nom de `checkGameState3x3`.

Ce comportement est vraiment utile, car nous sommes en mesure de configurer la fonction `checkGameState` en fonction de la largeur et de la hauteur du plateau.

Voyons ce qui se passe à l'intérieur de la fonction `checkGameState`.

```jsx
let checkGameState =
  (
    winningRows: winningRows,
    updatedBoard: board,
    oldBoard: board,
    gameState: gameState,
  ) =>
 oldBoard == updatedBoard ?
   gameState :
   {
     let flattenBoard = List.flatten(updatedBoard);
     let rec check = (rest: winningRows) => {
       let head = List.hd(rest);
       let tail = List.tl(rest);
       switch (
         getWinner(flattenBoard, head),
         gameEnded(flattenBoard),
         tail,
       ) {
       | (Cross, _, _) => Winner(Cross)
       | (Circle, _, _) => Winner(Circle)
       | (_, true, []) => Draw
       | (_, false, []) => whosPlaying(gameState)
       | _ => check(tail)
       };
    };
    check(winningRows);
};
```

Tout d'abord, nous vérifions si l'état du plateau est différent du précédent. Si ce n'est pas le cas, nous retournerons le `gameState` inchangé. Sinon, nous calculerons le nouvel état du jeu.

#### Calcul des nouveaux états

![Image](https://cdn-media-1.freecodecamp.org/images/oanyRY03r9aMAUtxtzFR-GvsnnMoT8azntmX)

Nous commençons à déterminer notre nouvel état de jeu en convertissant la partie `board` de l'état, qui se compose d'une liste de lignes, en une simple `list` en utilisant `List.flatten`. Le résultat aplati aura ce type de structure :

```jsx
[Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Empty]
```

De retour dans la fonction, nous définissons une fonction `check` qui reçoit un seul argument `rest` qui a le type `winningRows`. Le mot-clé `rec` avant sa définition signifie qu'elle peut être invoquée de manière récursive. Cependant, pour les appels de fonctions récursives, nous avons également besoin de données récursives. Heureusement, la `list` est une structure de données récursive.

Nous avons déjà appris que les listes dans Reason sont liées. Cette fonctionnalité nous permet d'itérer facilement à travers les [listes en utilisant la récursion](http://reasonmlhub.com/exploring-reasonml/ch_recursion.html).

Au bas de `checkGameState`, nous appelons la fonction `check` pour la première fois et lui passons la liste `winningCombs`. À l'intérieur de la fonction, nous extrayons le premier élément de la `list` et le stockons en tant que `head`. Le reste de la `list` est stocké en tant que `tail`.

Après cela, nous utilisons à nouveau la correspondance de motifs. Nous savons déjà comment cela fonctionne, donc je ne vais pas entrer dans les détails. Mais il vaut la peine de vérifier comment nous définissons nos données et nos motifs.

```jsx
type winner =
  | Cross
  | Circle
  | NoOne;
  
switch (
  getWinner(flattenBoard, head),
  gameEnded(flattenBoard),
  tail,
) { ...
```

À l'intérieur de l'instruction `switch`, nous utilisons à nouveau un `tuple` pour représenter nos données. Notre `tuple` contient trois éléments — le type de gagnant en tant que résultat de la fonction `getWinner`, un booléen en tant que résultat de la fonction `gameEnded`, et les éléments restants de la `list` (`tail`).

Avant d'aller plus loin, parlons un peu de ces deux fonctions d'assistance.

Nous allons d'abord jeter un coup d'œil à l'intérieur de la fonction `getWinner`.

```jsx
let getWinner = (flattenBoard, coords) =>
  switch (
    List.nth(flattenBoard, List.nth(coords, 0)),
    List.nth(flattenBoard, List.nth(coords, 1)),
    List.nth(flattenBoard, List.nth(coords, 2)),
  ) {
  | (Marked(Cross), Marked(Cross), Marked(Cross)) => Cross
  | (Marked(Circle), Marked(Circle), Marked(Circle)) => Circle
  | (_, _, _) => NoOne
  };
```

Lorsque nous appelons la fonction récursive `check` pour la première fois, le `head` sera le premier élément de `winningRows`, c'est-à-dire `[0, 1, 2]` qui est une `list`. Nous passons `head` à la fonction `getWinner` en tant qu'argument `coords` ainsi que le `flattenBoard`.

Encore une fois, nous utilisons la correspondance de motifs avec le `tuple`. À l'intérieur du `tuple`, nous utilisons la méthode `List.nth` pour accéder aux positions équivalentes des coordonnées `coords` dans la `list` du plateau aplati. La fonction `List.nth` prend une `list` et un nombre et retourne l'élément de la liste à cette position.

Ainsi, notre `tuple` se compose des trois coordonnées gagnantes de notre plateau auxquelles nous avons accédé en utilisant `List.nth`.

Maintenant, nous pouvons faire correspondre nos données de `tuple` aux motifs. Les deux premiers motifs vérifient si les trois champs sont marqués par le même joueur. Si c'est le cas, nous retournerons le gagnant — `Cross` ou `Circle`. Sinon, nous retournerons `NoOne`.

Voyons ce qui se passe à l'intérieur de la fonction `gameEnded`. Elle vérifie si tous les champs sont `Marked` et retourne un booléen.

```jsx
let gameEnded = board =>
  List.for_all(
    field => field == Marked(Circle) || field == Marked(Cross),
    board,
  );
```

Puisque nous savons quelles valeurs peuvent être retournées par nos fonctions d'assistance, revenons à notre fonction `check`.

```jsx
switch (
  getWinner(flattenBoard, head),
  gameEnded(flattenBoard),
  tail,
  ) {
  | (Cross, _, _) => Winner(Cross)
  | (Circle, _, _) => Winner(Circle)
  | (_, true, []) => Draw
  | (_, false, []) => whosPlaying(gameState)
  | _ => check(tail)
  };
```

Notre correspondance de motifs peut maintenant déterminer si le jeu s'est terminé par une victoire ou un match nul. Si ces cas ne sont pas appariés, nous passerons au cas suivant. Si celui-ci est apparié, le jeu continuera et la fonction `whosPlaying` sera appelée, et l'autre joueur prendra son tour.

```jsx
let whosPlaying = (gameState: gameState) =>
  switch (gameState) {
  | Playing(Cross) => Playing(Circle)
  | _ => Playing(Cross)
  };
```

Sinon, nous appellerons la fonction `check` de manière récursive avec une nouvelle combinaison de champs gagnants.

C'est tout. Maintenant, vous savez comment notre code contrôlant la logique du jeu fonctionne.

### C'est tout, les amis !

J'espère que cet article vous a aidé à comprendre les fonctionnalités principales de ce langage prometteur et encore en développement. Cependant, pour apprécier pleinement la puissance de cette nouvelle syntaxe basée sur OCaml, vous devez commencer à construire vos propres projets. Maintenant, vous êtes prêt à le faire.

Bonne chance !

![Image](https://cdn-media-1.freecodecamp.org/images/1zDhVxvp1uDIV-5RdNDxFMYqiyQTYNdQyC4G)

Si vous avez aimé cet article, donnez-lui quelques applaudissements. Je l'apprécierais beaucoup et plus de gens pourront voir cet article également.

Cet article a été [publié à l'origine sur mon blog](https://www.codinglawyer.io/).

Si vous avez des questions, des critiques, des observations ou des conseils pour l'amélioration, n'hésitez pas à écrire un commentaire ci-dessous ou à me contacter via [Twitter](https://twitter.com/coding_lawyer).