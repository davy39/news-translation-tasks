---
title: Les instructions if en JavaScript, l'égalité et Truthy/Falsy – Expliqués avec
  des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-21T21:06:20.000Z'
originalURL: https://freecodecamp.org/news/javascript-if-statement-equality-and-truthy-falsy
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/thumbnail-2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Les instructions if en JavaScript, l'égalité et Truthy/Falsy – Expliqués
  avec des exemples
seo_desc: 'By Deborah Kurata

  Decisions, decisions, decisions. Go left? Or go right? In programming, we use an
  if statement when we want our code to make a decision.

  In this tutorial, we''ll deep dive into the JavaScript if statement. Along the way,
  we''ll examine...'
---

Par Deborah Kurata

Des décisions, encore des décisions. Aller à gauche ? Ou aller à droite ? En programmation, nous utilisons une instruction `if` lorsque nous voulons que notre code prenne une décision.

Dans ce tutoriel, nous allons explorer en profondeur l'instruction `if` en JavaScript. En chemin, nous examinerons la différence entre l'égal simple, le double égal et le triple égal. Nous clarifierons également la signification de truthy et falsy en JavaScript.

Vous pouvez regarder la vidéo associée ici qui présente une démonstration.

%[https://youtu.be/_rqsd4DPKkE]

Supposons que nous construisons un jeu de devinettes de nombres comme le montre la Figure 1 ci-dessous. Le jeu génère un nombre aléatoire. L'utilisateur essaie de deviner ce nombre en saisissant sa proposition et en cliquant sur le bouton Guess.

Le jeu vérifie ensuite le nombre saisi. Si la proposition est trop basse, le jeu affiche "too low" (trop bas). Si la proposition est trop haute, le jeu affiche "too high" (trop haut). Et si la proposition est correcte, le jeu affiche "is correct ... You win!" (est correct... Vous avez gagné !).

![Interface utilisateur pour un jeu de devinettes de nombres.](https://www.freecodecamp.org/news/content/images/2023/03/GamePlay-1.png)
_Figure 1. Un jeu de devinettes de nombres._

Il y a de nombreux "si" dans ce paragraphe ! Pour écrire le code de ce jeu, nous aurons besoin de quelques instructions `if`.

## **Anatomie d'une instruction if en JavaScript**

En JavaScript, `if` est une instruction de bloc. Une instruction de **bloc** regroupe un ensemble d'instructions. Un bloc est délimité par des accolades.

Commençons par une version simplifiée de la logique requise pour notre jeu. Ici, nous déterminons si la proposition de l'utilisateur est juste ou fausse.

```javascript
if (guess === randomNumber) {
  feedbackText = 'Correct ... Vous avez gagné !';
  displayPlayAgain(true);
}
```

L'instruction `if` commence par le mot-clé `if`. Notez que JavaScript est sensible à la casse, y compris pour les mots-clés. Ainsi, si un mot-clé comme `if` est en minuscules, il doit être tapé en minuscules.

Le mot-clé `if` est suivi de parenthèses. À l'intérieur des parenthèses, nous définissons les conditions pour que l'instruction `if` prenne sa décision, appelées **critères de décision**.

Dans l'exemple ci-dessus, les critères de décision déterminent si la valeur de la variable `guess` est égale à la valeur de la variable `randomNumber`. Remarquez le triple égal `===`. Nous en reparlerons dans un instant.

Le corps du bloc `if` est entouré d'accolades. Le bloc peut contenir n'importe quel nombre d'instructions, y compris d'autres instructions `if`. Si les critères de décision à l'intérieur des parenthèses sont évalués comme vrais (true), le code à l'intérieur du bloc est exécuté. Sinon, l'exécution du code continue après le bloc `if`.

## **Égal simple vs double égal vs triple égal en JavaScript**

En JavaScript, nous utilisons un, deux ou trois signes égal, selon nos besoins.

Le signe égal simple `=` est une affectation. Nous l'utilisons pour affecter une valeur ou une expression à une variable.

```javascript
let feedbackText = 'Correct ... Vous avez gagné !';
const randomNumber = Math.floor(Math.random() * 20) + 1;
```

Dans ce code, nous affectons une chaîne de caractères à la variable `feedbackText`. Et nous affectons un nombre aléatoire généré à la variable `randomNumber`.

Le double égal `==` et le triple égal `===` sont des opérateurs de comparaison. Ils évaluent l'égalité de deux valeurs. Mais la manière dont ils effectuent cette égalité est légèrement, mais significativement, différente.

Le double égal `==` compare les deux valeurs. Si les valeurs sont de types différents, il tente de les convertir au même type avant de comparer.

Regardons un exemple.

```javascript
let randomNumber = 8;
let guess = "8"

if (guess == randomNumber) {
  feedbackText = 'Vous avez gagné !';
  displayPlayAgain(true);
}
```

Dans le code ci-dessus, au lieu de générer un nombre aléatoire, nous affectons le nombre 8 à la variable `randomNumber`. Et nous affectons une valeur de chaîne de caractères "8" à la variable `guess`. Comme notre instruction `if` utilise un double égal dans cet exemple, les types de données sont convertis au même type. Le critère de décision est alors évalué comme vrai car les valeurs sont toutes deux 8. Et la variable `feedbackText` est définie sur "Vous avez gagné !"

Pour plus d'informations sur les variables et les types de données en JavaScript, consultez cette vidéo.

%[https://youtu.be/hRQ3BtPmNNc]

Le triple égal `===` correspond à l'égalité stricte. Il compare les types de données et leurs valeurs. Il n'effectue aucune coercition de type, ce qui signifie qu'il ne tentera pas de convertir les types. Pour que l'égalité stricte soit évaluée comme vraie, le type de données et la valeur doivent être identiques.

Regardons le même exemple, mais en utilisant le triple égal à la place.

```javascript
let randomNumber = 8;
let guess = "8"
if (guess === randomNumber) {
  feedbackText = 'Vous avez gagné !';
  displayPlayAgain(true);
}
```

En utilisant le triple égal `===`, la valeur de chaîne `guess` de "8" n'est pas convertie en nombre. Comme les valeurs ne sont pas du même type de données, `guess` ne correspond pas à `randomNumber`. Le critère de décision est évalué comme faux et le code à l'intérieur du bloc `if` n'est pas exécuté.

La Figure 2 fournit un résumé. Utilisez le triple égal chaque fois que vous voulez une correspondance exacte, incluant les valeurs et les types de données.

![Image](https://lh6.googleusercontent.com/jHUrGIhddGXeNWbtO6hGM2HMUoLckdPHiWu2rJ2Z63deCR6iDmpA98d_uHYKURwcp19sS8qrIWiht1kqE9JKFqgRZ5b3fTkPV-EKMAQKqfCtjFQDbRQEj4rCKJq7AGx6hjjtW3NKhqfZDAleEBvLkT4)
_Figure 2. En JavaScript, nous utilisons un, deux ou trois signes égal._

## **if vs else vs else if en JavaScript**

L'instruction `if` seule fonctionne très bien si vous voulez que le code fasse quelque chose si une condition est vraie. Mais parfois, vous voulez aussi que le code fasse autre chose si la condition n'est pas vraie. C'est le but du bloc `else`.

```javascript
if (guess > randomNumber) {
  feedback = 'Trop haut';
} else {
  feedback = 'Trop bas';
}
```

Dans l'exemple de code ci-dessus, si la proposition de l'utilisateur est supérieure au nombre aléatoire, la variable `feedback` reçoit la valeur 'Trop haut'. Sinon (`else`), elle est définie sur 'Trop bas'.

En général, si le critère de décision est faux, le bloc `else` est exécuté.

Nous pouvons également utiliser un `else if`. Le `else if` fournit un deuxième ensemble de critères de décision. Ainsi, le bloc `else if` n'est exécuté que si ces critères de décision sont vrais.

Voici un exemple qui utilise `if`, `else` et `else if` :

```javascript
if (guess === randomNumber) {
  feedback = 'Correct ... Vous avez gagné ! ';
} else if (guess > randomNumber) {
  feedback = 'Trop haut';
} else {
  feedback = 'Trop bas';
}
```

Parcourons ce code.

Lorsque ce code est exécuté, le premier critère de décision est évalué. Comme ce critère utilise le triple égal `===`, il s'agit d'une comparaison stricte, ce qui signifie qu'il compare le type de données et la valeur. Si le type de données et la valeur sont identiques, le critère de décision est évalué comme vrai et le code du bloc `if` est exécuté. Dans cet exemple, le bloc `if` n'a qu'une seule instruction, mais il pourrait y en avoir n'importe quel nombre.

Si le premier critère de décision est faux, soit parce que les variables ont un type de données différent, soit une valeur différente, le critère de décision du `else if` est évalué. Si la proposition est supérieure au nombre aléatoire, le bloc `else if` est exécuté. Dans ce cas, le bloc ne contient qu'une seule instruction, mais il pourrait y en avoir n'importe quel nombre.

Si le critère de décision du `else if` est faux, le code du bloc `else` est exécuté. Encore une fois, il pourrait y avoir n'importe quel nombre d'instructions dans ce bloc `else`.

Pour visualiser ce concept, la Figure 3 montre cette logique sous forme d'organigramme.

![Organigramme de la logique if](https://www.freecodecamp.org/news/content/images/2023/03/flow-chart.png)
_Figure 3. Organigramme de la logique du code_

Sur l'organigramme, les critères de décision sont représentés par des losanges avec des chemins pour vrai (true) et faux (false).

Si la proposition de l'utilisateur correspond exactement au `randomNumber` (type de données et valeur), les critères de décision sont vrais et nous définissons le feedback sur 'Correct ... Vous avez gagné !'.

Si les critères de décision de l'instruction `if` sont faux, les critères de décision du `else if` sont évalués. Si la proposition de l'utilisateur est plus grande que le nombre aléatoire, les critères de décision du `else if` sont vrais et nous définissons le feedback sur 'Trop haut'.

Si les critères de décision du `else if` sont faux, nous définissons le feedback sur 'Trop bas'.

Dans ces instructions `if`, il est généralement clair quand les critères de décision sont vrais ou faux. La proposition est exactement la même que le nombre aléatoire ou elle ne l'est pas. La proposition est supérieure au nombre aléatoire ou elle ne l'est pas.

Mais qu'en est-il de cette instruction `if` ?

```javascript
if (guessInput) {
  let guess = guessInput.valueAsNumber;
}
```

Sans opérateur de comparaison, il s'agit d'une syntaxe abrégée pour "si cette variable est truthy". Comment savoir si `guessInput` est vrai ou faux ?

## **Valeurs Truthy vs Falsy en JavaScript**

JavaScript a une notion unique de vrai et faux, appelée **truthy** et **falsy**. Truthy et falsy sont utilisés lors de l'évaluation de critères de décision qui ne sont pas clairement vrais ou faux. Regardons quelques exemples.

```javascript
let guess = false;
if (guess) { … } // falsy
```

Comme on s'y attend, une variable définie sur `false` est falsy. Le code à l'intérieur du bloc `if` n'est pas exécuté.

```javascript
let guess = 0;
if (guess) { … } // falsy
```

Une valeur de `0` (zéro) est également falsy.

```javascript
let guess = "";
if (guess) { … } // falsy
```

Et `""`, qui est une chaîne vide, est falsy.

```javascript
let guess;		// undefined
if (guess) { … } // falsy
```

Si une variable n'a pas reçu de valeur, elle est `undefined`. Une variable `undefined` est falsy. Un motif de codage courant consiste à s'assurer qu'une variable a une valeur avant de faire quelque chose avec cette variable en utilisant une instruction `if` comme indiqué ci-dessus.

```javascript
let guess = null;
if (guess) { … } // falsy
```

Une variable `null` est également falsy.

```javascript
let guess = Number("quatre"); // NaN
if (guess) { … } // falsy
```

Et si le code tente de convertir une valeur qui n'est pas un nombre en un nombre, le résultat est `NaN`, qui signifie "not a number" (pas un nombre). Les variables qui sont `NaN` sont évaluées comme falsy.

Toutes les autres valeurs sont truthy.

```javascript
let guess = 4;
if (guess) { … } // truthy

guess = 'quatre';
if (guess) { … } // truthy
```

Dans le premier exemple, la variable est définie sur un nombre non nul, elle est donc truthy. Dans le second exemple, la variable est définie sur une chaîne non vide, elle est donc truthy.

Fondamentalement, si la valeur de la variable est false, zéro, vide, null, undefined ou `NaN`, elle est falsy et le code à l'intérieur du bloc `if` n'est pas exécuté.

Si la valeur de la variable est n'importe quoi d'autre, comme un nombre qui n'est pas zéro, une chaîne non vide, un tableau ou un objet, elle est truthy et le code dans le bloc `if` est exécuté.

Que diriez-vous d'un exemple plus complet ?

## **Exemple de jeu de devinettes**

Notre jeu de devinettes comprend le code suivant :

```javascript
// Trouver les éléments
const guessButton = document.getElementById('guess-button');
guessButton.addEventListener('click', processGuess);

const guessInput = document.getElementById('guess-input');
const feedbackContainer = document.getElementById('feedback');

function processGuess() {
  let feedbackText;
  if (guessInput){
    const guess = guessInput.valueAsNumber;

    if (guess === randomNumber) {
      feedback = 'Correct ... Vous avez gagné ! ';
    } else if (guess > randomNumber) {
      feedback = 'Trop haut';
    } else {
      feedback = 'Trop bas';
    }
  }

  if (feedbackContainer) {
    feedbackContainer.innerHTML += '<br>' + feedbackText;
  }
}
```

Nous trouvons d'abord les éléments HTML avec lesquels nous voulons travailler. Nous trouvons le bouton de devinette et utilisons `addEventListener` pour écouter l'événement de clic sur le bouton. Lorsque l'utilisateur clique sur le bouton, le code appelle la fonction que nous avons passée à `addEventListener`, qui est `processGuess`.

Pour plus d'informations sur la recherche d'éléments HTML et la réaction à leurs événements, [consultez cet article](https://www.freecodecamp.org/news/reacting-to-actions-with-javascript/).

Nous trouvons ensuite l'élément de saisie (input) pour pouvoir lire la proposition de l'utilisateur. Et nous trouvons un élément de feedback que nous utiliserons pour écrire le texte de feedback sur la page.

La fonction `processGuess()` lit la proposition de l'utilisateur à partir de l'élément d'entrée et affiche le feedback approprié. Décomposons-la.

La première instruction `if` garantit que nous avons trouvé l'élément d'entrée. Si l'élément a été trouvé, nous avons une référence à cet élément dans la variable `guessInput`. La variable `guessInput` est évaluée comme truthy, et le code du bloc `if` est exécuté.

Le code à l'intérieur du bloc `if` lit la valeur de l'élément d'entrée. Il utilise `valueAsNumber`, qui lit une entrée numérique en tant que nombre plutôt qu'en tant que chaîne. De cette façon, nous pouvons plus facilement comparer la valeur devinée au nombre généré aléatoirement.

Le code compare ensuite strictement la proposition au nombre aléatoire généré. Si les valeurs ont le même type et la même valeur, les critères de décision sont vrais et ce code du bloc `if` est exécuté.

Si la proposition n'est pas correcte, un bloc `else if` détermine si la valeur est trop haute ou trop basse. Sur la base de cette comparaison, le texte de feedback est défini.

Enfin, nous vérifions si nous avons une référence au conteneur de feedback. Si c'est le cas, la variable `feedbackContainer` est définie, l'instruction `if` est évaluée comme truthy, et nous écrivons le texte de feedback approprié dans ce conteneur.

## **Conclusion**

Nous utilisons des instructions `if` pour prendre des décisions dans notre code. Les instructions à l'intérieur d'un bloc `if` sont exécutées si les critères de décision définis entre parenthèses sont évalués comme vrais (true) ou truthy. Les instructions à l'intérieur d'un bloc `else` sont exécutées si les critères de décision sont évalués comme faux (false) ou falsy.

Lors de la définition des critères de décision, il est important de définir la comparaison appropriée :

* Un signe égal simple `=` en JavaScript affecte une valeur à une variable. Il ne doit pas être utilisé dans les critères de décision.
* Le double égal `==` compare les valeurs pour voir si elles sont égales. Si les valeurs ne sont pas du même type de données, il essaie de les convertir au même type avant de vérifier l'égalité.
* Le triple égal `===` compare strictement les valeurs pour voir si elles sont égales. S'ils ne sont pas du même type, ils ne sont pas égaux.

Et soyez attentif aux règles de JavaScript pour truthy et falsy, en particulier lors de la définition des critères de décision.

Vous pouvez trouver le code du jeu de devinettes ici : [https://github.com/DeborahK/Gentle-Introduction-to-JavaScript](https://github.com/DeborahK/Gentle-Introduction-to-JavaScript)

Pour plus d'informations sur la programmation avec JavaScript et pour construire ce jeu de devinettes étape par étape, consultez ce cours :

%[https://youtu.be/jJLn5XxyXWc]

Maintenant, ne soyez pas hésitant, utilisez ces instructions `if` avec sagesse !