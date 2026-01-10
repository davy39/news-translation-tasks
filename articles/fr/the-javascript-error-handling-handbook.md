---
title: Le guide de gestion des erreurs en JavaScript
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2025-07-11T18:52:06.597Z'
originalURL: https://freecodecamp.org/news/the-javascript-error-handling-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752254732491/dd413499-64f4-4a20-8fd6-7f73cfcd55c0.png
tags:
- name: JavaScript
  slug: javascript
- name: error handling
  slug: error-handling
- name: Web Development
  slug: web-development
- name: handbook
  slug: handbook
seo_title: Le guide de gestion des erreurs en JavaScript
seo_desc: Errors and exceptions are inevitable in application development. As programmers,
  it is our responsibility to handle these errors gracefully so that the user experience
  of the application is not compromised. Handling errors correctly also helps progra...
---

Les erreurs et les exceptions sont inévitables dans le développement d'applications. En tant que programmeurs, il est de notre responsabilité de gérer ces erreurs avec élégance afin que l'expérience utilisateur de l'application ne soit pas compromise. Gérer correctement les erreurs aide également les programmeurs à déboguer et à comprendre ce qui les a causées afin qu'ils puissent les traiter.

JavaScript est un langage de programmation populaire depuis plus de trois décennies. Nous construisons des applications web, mobiles, PWA et côté serveur en utilisant JavaScript et diverses bibliothèques (comme ReactJS) et frameworks (comme Next.js, Remix, etc.) basés sur JavaScript.

Étant un langage faiblement typé, JavaScript impose le défi de gérer correctement la sécurité des types. TypeScript est utile pour gérer les types, mais nous devons toujours gérer efficacement les erreurs d'exécution dans notre code.

Des erreurs comme `TypeError`, `RangeError`, `ReferenceError` vous sont probablement familières si vous construisez avec JavaScript depuis un certain temps. Toutes ces erreurs peuvent causer des données invalides, de mauvaises transitions de page, des résultats indésirables, ou même faire planter l'ensemble de l'application - aucune de ces situations ne rendra les utilisateurs finaux heureux !

Dans ce guide, vous apprendrez tout ce que vous devez savoir sur la gestion des erreurs en JavaScript. Nous commencerons par comprendre les erreurs, leurs types et leurs occurrences. Ensuite, vous apprendrez comment traiter ces erreurs afin qu'elles ne causent pas une mauvaise expérience utilisateur. À la fin, vous apprendrez également à créer vos propres types d'erreurs personnalisées et des méthodologies de nettoyage pour mieux gérer le flux de votre code pour les optimisations et les performances.

J'espère que vous apprécierez la lecture et la pratique des tâches que j'ai fournies à la fin de l'article.

Ce guide est également disponible sous forme de session vidéo dans le cadre de l'initiative [40 Days of JavaScript](https://www.youtube.com/watch?v=t8QXF85YovE&list=PLIJrr73KDmRw2Fwwjt6cPC_tk5vcSICCu). Veuillez la consulter.

%[https://www.youtube.com/watch?v=XpMW-gxNYD8]

## Table des matières

1. [Les erreurs en JavaScript](#heading-les-erreurs-en-javascript)

2. [Gestion des erreurs avec try et catch](#heading-gestion-des-erreurs-avec-try-et-catch)

   * [Le bloc try](#heading-le-bloc-try)

   * [Le bloc catch](#heading-le-bloc-catch)

3. [Gestion des erreurs : cas d'utilisation réels](#heading-gestion-des-erreurs-cas-dutilisation-réels)

   * [Gestion de la division par zéro](#heading-gestion-de-la-division-par-zéro)

   * [Gestion du JSON](#heading-gestion-du-json)

4. [Anatomie de l'objet Error](#heading-anatomie-de-lobjet-error)

   * [Qu'est-ce que l'objet Error ?](#heading-quest-ce-que-lobjet-error)

5. [Lancement d'erreurs et relancement d'erreurs](#heading-lancement-derreurs-et-relancement-derreurs)

   * [Relancement](#heading-relancement)

6. [Le finally avec try-catch](#heading-le-finally-avec-try-catch)

   * [Précautions avec finally](#heading-précautions-avec-finally)

7. [Erreurs personnalisées](#heading-erreurs-personnalisées)

   * [Un cas d'utilisation réel des erreurs personnalisées](#heading-un-cas-dutilisation-réel-des-erreurs-personnalisées)

8. [Devoirs pour vous](#heading-devoirs-pour-vous)

   * [Trouver la sortie](#heading-trouver-la-sortie)

   * [Validation du processus de paiement](#heading-validation-du-processus-de-paiement)

9. [Initiative du défi 40 Days of JavaScript](#heading-initiative-du-défis-40-days-of-javascript)

10. [Avant de terminer...](#heading-avant-de-terminer)

## Les erreurs en JavaScript

Les erreurs et les exceptions sont des événements qui perturbent l'exécution du programme. JavaScript analyse et exécute le code ligne par ligne. Le code source est évalué avec la grammaire du langage de programmation pour s'assurer qu'il est valide et exécutable. En cas d'incompatibilité, JavaScript rencontre une `erreur de parsing`. Vous devez vous assurer de suivre la syntaxe et la grammaire correctes du langage pour éviter les erreurs de parsing.

Jetez un coup d'œil à l'extrait de code ci-dessous. Ici, nous avons fait l'erreur de ne pas fermer les parenthèses pour console.log.

```javascript
console.log("hi"
```

Cela entraînera une erreur de syntaxe comme ceci :

![Uncaught SyntaxError](https://cdn.hashnode.com/res/hashnode/image/upload/v1743047661114/11a445de-132f-49d0-9f3c-8516a0d21950.png align="center")

D'autres types d'erreurs peuvent survenir en raison de données d'entrée incorrectes, de la tentative de lecture d'une valeur ou d'une propriété qui n'existe pas, ou de l'action sur des données inexactes. Voici quelques exemples :

```javascript
console.log(x); // Uncaught ReferenceError: x is not defined

let obj = null;
console.log(obj.name); // Uncaught TypeError: Cannot read properties of null

let arr = new Array(-1) // Uncaught RangeError: Invalid array length

decodeURIComponent("%"); // Uncaught URIError: URI malformed

eval("var x = ;"); // Uncaught EvalError
```

Voici la liste des erreurs d'exécution possibles que vous pouvez rencontrer, avec leurs descriptions :

* `ReferenceError` - Se produit lorsque l'on tente d'accéder à une variable qui n'est pas définie.

* `TypeError` - Se produit lorsqu'une opération est effectuée sur une valeur du mauvais type.

* `RangeError` - Se produit lorsqu'une valeur est en dehors de la plage autorisée.

* `SyntaxError` - Se produit lorsqu'il y a une erreur dans la syntaxe du code JavaScript.

* `URIError` - Se produit lorsqu'une fonction URI incorrecte est utilisée dans l'encodage et le décodage des URI.

* `EvalError` - Se produit lorsqu'il y a un problème avec la fonction eval().

* `InternalError` - Se produit lorsque le moteur JavaScript atteint une limite interne (dépassement de pile).

* `AggregateError` - Introduit dans ES2021, utilisé pour gérer plusieurs erreurs à la fois.

* `Custom Errors` - Ce sont des erreurs définies par l'utilisateur, et nous apprendrons bientôt comment les créer et les utiliser.

Avez-vous remarqué que tous les exemples de code que nous avons utilisés ci-dessus résultent en un message expliquant de quelle erreur il s'agit ? Si vous regardez ces messages de près, vous trouverez un mot appelé `Uncaught`. Cela signifie que l'erreur s'est produite, mais qu'elle n'a pas été capturée et gérée. C'est exactement ce que nous allons faire maintenant - afin que vous sachiez comment gérer ces erreurs.

## Gestion des erreurs avec `try` et `catch`

Les applications JavaScript peuvent planter pour diverses raisons, comme une syntaxe invalide, des données invalides, des réponses d'API manquantes, des erreurs utilisateur, etc. La plupart de ces raisons peuvent entraîner un plantage de l'application, et vos utilisateurs verront une page blanche.

Plutôt que de laisser l'application planter, vous pouvez gérer ces situations avec élégance en utilisant `try...catch`.

```javascript
try {
    // logique ou code
} catch (err) {
    // gérer l'erreur
}
```

### Le bloc `try`

Le bloc `try` contient le code - la logique métier - qui pourrait lancer une erreur. Les développeurs veulent toujours que leur code soit exempt d'erreurs. Mais en même temps, vous devez être conscient que le code pourrait lancer une erreur pour plusieurs raisons possibles, comme :

* Analyse de JSON

* Exécution de la logique de l'API

* Accès aux propriétés d'objets imbriqués

* Manipulations du DOM

* ... et bien plus encore

Lorsque le code à l'intérieur du bloc try lance une erreur, l'exécution du code restant dans le bloc try sera suspendue, et le contrôle passe au bloc catch le plus proche. Si aucune erreur ne se produit, le bloc catch est complètement ignoré.

```javascript
try {
  // Code qui pourrait lancer une erreur
} catch (error) {
  // Gérer l'erreur ici
}
```

### Le bloc `catch`

Le bloc catch ne s'exécute que si une erreur a été lancée dans le bloc try. Il reçoit l'`objet Error` en tant que paramètre pour nous donner plus d'informations sur l'erreur. Dans l'exemple montré ci-dessous, nous utilisons quelque chose appelé `abc` sans le déclarer. JavaScript lancera une erreur comme ceci :

```javascript
try {
    console.log("l'exécution commence ici");
    abc;
    console.log("l'exécution se termine ici");
} catch (err) {
    console.error("Une erreur s'est produite", err);
}
```

JavaScript exécute le code ligne par ligne. La séquence d'exécution du code ci-dessus sera :

* Tout d'abord, la chaîne "l'exécution commence ici" sera enregistrée dans la console.

* Ensuite, le contrôle passera à la ligne suivante et trouvera `abc` là. Qu'est-ce que c'est ? JavaScript ne trouve aucune définition de cela nulle part. Il est temps de déclencher l'alarme et de lancer une erreur. Le contrôle ne passe pas à la ligne suivante (le prochain journal de la console), mais passe plutôt au bloc catch.

* Dans le bloc catch, nous gérons l'erreur en la journalisant dans la console. Nous pourrions faire beaucoup d'autres choses comme afficher un message toast, envoyer un email à l'utilisateur, ou éteindre un grille-pain (pourquoi pas si votre client en a besoin).

Sans try...catch, l'erreur ferait planter l'application.

## Gestion des erreurs : cas d'utilisation réels

Voyons maintenant quelques cas d'utilisation réels de la gestion des erreurs avec try...catch.

### Gestion de la division par zéro

Voici une fonction qui divise un nombre par un autre nombre. Nous avons donc des paramètres passés à la fonction pour les deux nombres. Nous voulons nous assurer que la division ne rencontre jamais d'erreur pour diviser un nombre par zéro (0).

En tant que mesure proactive, nous avons écrit une condition selon laquelle si le diviseur est zéro, nous lancerons une erreur disant que la division par zéro n'est pas autorisée. Dans tous les autres cas, nous procéderons à l'opération de division. En cas d'erreur, le bloc catch gérera l'erreur et fera ce qui est nécessaire (dans ce cas, journaliser l'erreur dans la console).

```javascript
function divideNumbers(a, b) {
    try {
        if (b === 0) {
            const err = new Error("La division par zéro n'est pas autorisée.");
            throw err;
        }
        const result = a/b;
        console.log(`Le résultat est ${result}`);
    } catch(error) {
        console.error("Erreur mathématique :", error.message)
    }
}
```

Maintenant, si nous invoquons la fonction avec les arguments suivants, nous obtiendrons un résultat de 5, et le deuxième argument est une valeur non nulle.

```javascript
divideNumbers(15, 3); // Le résultat est 5
```

Mais si nous passons la valeur 0 pour le deuxième argument, le programme lancera une erreur, et elle sera journalisée dans la console.

```javascript
divideNumbers(15, 0);
```

Sortie :

![Erreur mathématique](https://cdn.hashnode.com/res/hashnode/image/upload/v1752115297863/02d9e89d-e5c1-4759-a11e-ab57d04bcfff.png align="center")

### Gestion du JSON

Souvent, vous recevrez du JSON en réponse à un appel d'API. Vous devez analyser ce JSON dans votre code JavaScript pour extraire les valeurs. Que se passe-t-il si l'API vous envoie par erreur un JSON mal formé ? Vous ne pouvez pas vous permettre de laisser votre interface utilisateur planter à cause de cela. Vous devez le gérer avec élégance - et voici que le bloc try...catch vient à la rescousse :

```javascript
function parseJSONSafely(str) {
  try {
    return JSON.parse(str);
  } catch (err) {
    console.error("JSON invalide :", err.message);
    return null;
  }
}

const userData = parseJSONSafely('{"name": "tapaScript"}'); // Analysé
const badData = parseJSONSafely('name: tapaScript');         // Géré avec élégance
```

Sans try...catch, le deuxième appel ferait planter l'application.

## Anatomie de l'objet Error

Obtenir des erreurs en programmation peut être une sensation effrayante. Mais les `Error`s en JavaScript ne sont pas seulement des messages effrayants et ennuyeux - ce sont des objets structurés qui contiennent beaucoup d'informations utiles sur ce qui s'est mal passé, où et pourquoi.

En tant que développeurs, nous devons comprendre l'anatomie de l'objet `Error` pour nous aider à déboguer plus rapidement et à récupérer plus intelligemment les problèmes d'applications de niveau production.

Plongeons profondément dans l'objet Error, ses propriétés et comment l'utiliser efficacement avec des exemples.

### Qu'est-ce que l'objet Error ?

Le moteur JavaScript lance un objet `Error` lorsque quelque chose ne va pas pendant l'exécution. Cet objet contient des informations utiles comme :

* Un message d'erreur : il s'agit d'un message d'erreur lisible par l'homme.

* Le type d'erreur : TypeError, ReferenceError, SyntaxError, etc., que nous avons discutés ci-dessus.

* La trace de la pile : cela vous aide à naviguer jusqu'à la racine de l'erreur. Il s'agit d'une chaîne contenant la trace de la pile au moment où l'erreur a été lancée.

Jetez un coup d'œil à l'extrait de code ci-dessous. Le moteur JavaScript lancera une erreur dans ce code, car la variable `y` n'est pas définie. L'objet d'erreur contient le nom de l'erreur (type), le message et les informations de trace de la pile.

```javascript
function doSomething() {
  const x = y + 1; // y n'est pas défini
}
try {
  doSomething();
} catch (err) {
  console.log(err.name);    // ReferenceError
  console.log(err.message); // y n'est pas défini
  console.log(err.stack); // ReferenceError: y n'est pas défini
                          // à doSomething (<anonymous>:2:13)
                          // à <anonymous>:5:3
}
```

Astuce : Si vous avez besoin de propriétés spécifiques de l'objet d'erreur, vous pouvez utiliser la déstructuration pour cela. Voici un exemple où nous ne sommes intéressés que par le nom et le message de l'erreur, et non par la pile.

```javascript
try {
  JSON.parse("{ invalid json }");
} catch ({name, message}) {
  console.log("Nom :", name);       // Nom : SyntaxError
  console.log("Message :", message); // Message : Nom de propriété attendu ou '}' dans JSON à la position 2 (ligne 1 colonne 3)
}
```

## Lancement d'erreurs et relancement d'erreurs

JavaScript fournit une instruction `throw` pour déclencher une erreur manuellement. Elle est très utile lorsque vous souhaitez gérer une condition invalide dans votre code (vous souvenez-vous du problème de division par zéro ?).

Pour lancer une erreur, vous devez créer une instance de l'objet `Error` avec des détails, puis la lancer.

```javascript
throw new Error("Quelque chose ne va pas !");
```

Lorsque l'exécution du code rencontre une instruction `throw`,

* Elle arrête l'exécution du bloc de code actuel immédiatement.

* Le contrôle passe au bloc catch le plus proche (s'il y en a un).

* Si le bloc catch n'est pas trouvé, l'erreur ne sera pas capturée. L'erreur remonte et peut finir par faire planter le programme. Vous pouvez en apprendre davantage sur les événements et la remontée d'événements [ici](https://www.youtube.com/watch?v=ybgI5vVE668).

### Relancement

Parfois, capturer l'erreur elle-même dans le bloc catch n'est pas suffisant. Parfois, vous ne savez peut-être pas comment gérer complètement l'erreur, et vous souhaitez peut-être faire des choses supplémentaires, comme :

* Ajouter plus de contexte à l'erreur.

* Journaliser l'erreur dans un journal basé sur des fichiers.

* Passer l'erreur à quelqu'un de plus spécialisé pour la gérer.

C'est là que le `relancement` intervient. Avec le relancement, vous capturez une erreur, faites autre chose avec elle, puis la relancez.

```javascript
function processData() {
  try {
    parseUserData();
  } catch (err) {
    console.error("Erreur dans processData :", err.message);
    throw err; // Relancer pour que la fonction externe puisse également la gérer
  }
}

function main() {
  try {
    processData();
  } catch (err) {
    handleErrorBetter(err);
  }
}
```

Dans le code ci-dessus, la fonction `processData()` capture une erreur, la journalise, puis la `relance`. La fonction externe `main()` peut maintenant la capturer et faire quelque chose de plus pour la gérer mieux.

Dans le développement d'applications réelles, vous souhaiterez séparer les préoccupations pour les erreurs, comme :

* **Couche API** - Dans cette couche, vous pouvez détecter les échecs HTTP

```javascript
async function fetchUser(id) {
  const res = await fetch(`/users/${id}`);
  if (!res.ok) throw new Error("Utilisateur non trouvé"); // lancer ici
  return res.json();
}
```

* **Couche Service** - Dans cette couche, vous gérez la logique métier. Ainsi, l'erreur sera gérée pour les conditions invalides.

```javascript
async function getUser(id) {
  try {
    const user = await fetchUser(id);
    return user;
  } catch (err) {
    console.error("Échec de la récupération de l'utilisateur :", err.message);
    throw new Error("Impossible de charger le profil de l'utilisateur"); // relancement
  }
}
```

* **Couche UI** - Afficher un message d'erreur convivial.

```javascript
async function showUserProfile() {
  try {
    const user = await getUser(123);
    renderUser(user);
  } catch (err) {
    displayError(err.message); // Un message approprié est affiché à l'utilisateur
  }
}
```

## Le `finally` avec try-catch

Le bloc try...catch nous donne un moyen de gérer les erreurs avec élégance. Mais vous pouvez toujours vouloir exécuter un code indépendamment du fait qu'une erreur se soit produite ou non. Par exemple, fermer la connexion à la base de données, arrêter un chargeur, réinitialiser certains états, etc. C'est là que `finally` intervient.

```javascript
try {
  // Code pouvant lancer une erreur
} catch (error) {
  // Gérer l'erreur
} finally {
  // Toujours exécuté, qu'une erreur se soit produite ou non
}
```

Prenons un exemple :

```javascript
function performTask() {
  try {
    console.log("Faire quelque chose de cool...");
    throw new Error("Oups !");
  } catch (err) {
    console.error("Erreur capturée :", err.message);
  } finally {
    console.log("Nettoyage : Tâche terminée (succès ou échec).");
  }
}

performTask();
```

Dans la fonction `performTask()`, l'erreur est lancée après le premier journal de la console. Ainsi, le contrôle passera au bloc catch et journalisera l'erreur. Après cela, le bloc `finally` exécutera son journal de la console.

Sortie :

```bash
Faire quelque chose de cool...
Erreur capturée : Oups !
Nettoyage : Tâche terminée (succès ou échec).
```

Prenons un cas d'utilisation plus réel consistant à faire un appel d'API et à gérer le spinner de chargement :

```javascript
async function loadUserData() {
  showSpinner(); // Afficher le spinner ici

  try {
    const res = await fetch('/api/user');
    const data = await res.json();
    displayUser(data);
  } catch (err) {
    showError("Échec du chargement de l'utilisateur.");
  } finally {
    hideSpinner(); // Masquer le spinner pour les cas de succès et d'échec.
  }
}
```

Habituellement, nous affichons un spinner de chargement lors d'un appel d'API (asynchrone) depuis le navigateur. Indépendamment de la réponse réussie ou d'une erreur de l'appel d'API, nous devons arrêter d'afficher le spinner de chargement. Au lieu d'exécuter la logique du code deux fois pour arrêter le spinner (une fois à l'intérieur du bloc `try` et une autre fois à l'intérieur du bloc `catch`), vous pouvez le faire à l'intérieur du bloc `finally`.

### Précautions avec `finally`

Le bloc `finally` peut remplacer les valeurs de retour ou une erreur lancée. Ce comportement peut être déroutant et peut également entraîner des bugs.

```javascript
function test() {
  try {
    return 'from try';
  } finally {
    return 'from finally';
  }
}

console.log(test());
```

Que pensez-vous que le code ci-dessus retourne ?

Il retournera `'from finally'`. Le return `'from try'` est complètement ignoré. Le return de finally le remplace silencieusement.

Voyons un autre exemple du même problème :

```javascript
function willThrow() {
  try {
    throw new Error("Erreur originale");
  } finally {
    throw new Error("Erreur de remplacement"); // L'erreur originale est perdue
  }
}

try {
  willThrow();
} catch (err) {
  console.log(err.message); // "Erreur de remplacement"
}
```

Ici, l'erreur originale (`"Erreur originale"`) est avalée. Le bloc finally remplace la cause racine réelle.

Lorsque vous utilisez `finally` :

* Évitez les returns et les throws depuis `finally` autant que possible.

* Évitez d'effectuer une logique dans le bloc `finally` qui pourrait affecter le résultat réel. Le bloc `try` est le meilleur endroit pour cela.

* Toute prise de décision critique doit être évitée à l'intérieur du bloc `finally`.

* Utilisez `finally` pour les activités de nettoyage, telles que la fermeture de fichiers, de connexions, l'arrêt des spinners de chargement, etc.

* Assurez-vous que le bloc `finally` contient du code sans effets secondaires.

## Erreurs personnalisées

L'utilisation de l'erreur générique et de ses types existants, comme ReferenceError, SyntaxError, etc., peut être un peu vague dans les applications complexes. JavaScript vous permet de créer des erreurs personnalisées qui sont plus liées à vos cas d'utilisation métier. Les erreurs personnalisées peuvent fournir :

* Des informations contextuelles supplémentaires sur l'erreur.

* De la clarté sur l'erreur.

* Des journaux plus lisibles.

* La capacité de gérer plusieurs cas d'erreur conditionnellement.

Une erreur personnalisée en JavaScript est un type d'erreur défini par l'utilisateur qui étend la classe Error intégrée. L'erreur personnalisée doit être une [classe ES6](https://www.youtube.com/watch?v=kG5t34ciG9w) qui étend la classe Error de JavaScript. Nous pouvons utiliser `super()` dans la fonction constructeur pour hériter de la propriété message de la classe Error. Vous pouvez optionnellement assigner un nom et nettoyer la trace de la pile pour l'erreur personnalisée.

```javascript
class MyCustomError extends Error {
  constructor(message) {
    super(message);         // Hériter de la propriété message
    this.name = this.constructor.name; // Optionnel mais recommandé
    Error.captureStackTrace(this, this.constructor); // Nettoyer la trace de la pile
  }
}
```

Voyons maintenant un cas d'utilisation réel pour une erreur personnalisée.

### Un cas d'utilisation réel des erreurs personnalisées

L'utilisation d'un formulaire sur une page web est un cas d'utilisation extrêmement courant. Un formulaire peut contenir un ou plusieurs champs de saisie. Il est recommandé de valider les saisies de l'utilisateur avant de traiter les données du formulaire pour toute action serveur.

Créons une erreur de validation personnalisée que nous pouvons utiliser pour valider plusieurs données de saisie de formulaire, comme l'email de l'utilisateur, l'âge, le numéro de téléphone, etc.

Tout d'abord, nous créerons une classe appelée `ValidationError` qui étend la classe `Error`. La fonction constructeur configure la classe `ValidationError` avec un message d'erreur. Nous pouvons également instancier des propriétés supplémentaires, comme name, field, etc.

```javascript
class ValidationError extends Error {
  constructor(field, message) {
    super(`${field}: ${message}`);
    this.name = "ValidationError";
    this.field = field;
  }
}
```

Maintenant, voyons comment utiliser `ValidationError`. Nous pouvons valider un modèle d'utilisateur pour vérifier ses propriétés et lancer une `ValidationError` chaque fois que les attentes ne correspondent pas.

```javascript
function validateUser(user) {
  if (!user.email.includes("@")) {
    throw new ValidationError("email", "Format d'email invalide");
  }
  if (!user.age || user.age < 18) {
    throw new ValidationError("age", "L'utilisateur doit avoir 18 ans ou plus");
  }
}
```

Dans l'extrait de code ci-dessus,

* Nous lançons une erreur de validation de format d'email invalide si l'email de l'utilisateur ne contient pas le symbole `@`.

* Nous lançons une autre erreur de validation si les informations d'âge de l'utilisateur sont manquantes ou inférieures à 18.

Une erreur personnalisée nous donne le pouvoir de créer des types d'erreurs spécifiques au domaine/d'utilisation pour garder le code plus gérable et moins sujet aux erreurs.

## Devoirs pour vous

Si vous avez lu ce guide jusqu'ici, j'espère que vous avez maintenant une solide compréhension de la gestion des erreurs en JavaScript. Essayons quelques devoirs basés sur ce que nous avons appris jusqu'à présent. Ce sera amusant.

### Trouver la sortie

Quel sera le résultat de l'extrait de code suivant et pourquoi ?

```javascript
try {
    let r = p + 50;
    console.log(r);
} catch (error) {
    console.log("Une erreur s'est produite :", error.name);
}
```

Les options sont :

* ReferenceError

* SyntaxError

* TypeError

* Pas d'erreur, cela imprime 10

### Validation du processus de paiement

Écrivez une fonction `processPayment(amount)` qui vérifie si le montant est positif et ne dépasse pas le solde. Si une condition échoue, lancez des erreurs appropriées.

Indice : Vous pouvez penser à créer une erreur personnalisée ici.

## Initiative du défi 40 Days of JavaScript

Il existe 101 façons d'apprendre quelque chose. Mais rien ne peut battre les méthodologies d'apprentissage structurées et progressives. Après avoir passé plus de deux décennies dans l'ingénierie logicielle, j'ai pu rassembler le meilleur de JavaScript pour créer l'initiative de défi [40 Days of JavaScript](https://www.youtube.com/playlist?list=PLIJrr73KDmRw2Fwwjt6cPC_tk5vcSICCu).

Consultez-la si vous souhaitez apprendre JavaScript avec des concepts fondamentaux, des projets et des devoirs gratuitement (pour toujours). Se concentrer sur les fondamentaux de JavaScript vous préparera bien pour un avenir dans le développement web.

## **Avant de terminer...**

C'est tout ! J'espère que vous avez trouvé cet article instructif.

Restez en contact :

* Abonnez-vous à ma [Chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1).

* Suivez-moi sur [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils pour monter en compétences.

* Consultez et suivez mes travaux open-source sur [GitHub](https://github.com/atapas).

À bientôt avec mon prochain article. En attendant, prenez soin de vous et continuez à apprendre.