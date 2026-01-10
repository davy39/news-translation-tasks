---
title: Tutoriel sur les fonctions JavaScript – IIFE, paramètres de fonction et blocs
  de code expliqués
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-10-05T16:06:29.000Z'
originalURL: https://freecodecamp.org/news/javascript-function-iife-parameters-code-blocks-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/programming-image-by-mohamed-hassan-from-pixabay-javascript-function-iffe-parameters-blocks-explained-codesweetly.png
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur les fonctions JavaScript – IIFE, paramètres de fonction et
  blocs de code expliqués
seo_desc: 'Functions are one of the most widely-used features in programming. So,
  it helps to have a solid understanding of how they work.

  This tutorial discusses everything you need to know to use JavaScript functions
  like a pro.

  Table of Contents


  What Is a F...'
---

Les fonctions sont l'une des fonctionnalités les plus utilisées en programmation. Il est donc utile d'avoir une compréhension solide de leur fonctionnement.

Ce tutoriel traite de tout ce que vous devez savoir pour utiliser les fonctions JavaScript comme un pro.

## Table des matières

1. [Qu'est-ce qu'une fonction ?](#heading-quest-ce-quune-fonction)
2. [Pourquoi utiliser des fonctions ?](#heading-pourquoi-utiliser-des-fonctions)
3. [Syntaxe d'une fonction JavaScript](#heading-syntaxe-dune-fonction-javascript-1)
4. [Qu'est-ce que le mot-clé `function` ?](#heading-quest-ce-que-le-mot-cle-function)
5. [Qu'est-ce qu'un nom de fonction ?](#heading-quest-ce-quun-nom-de-fonction)
6. [Qu'est-ce qu'un paramètre ?](#heading-quest-ce-quun-parametre)
7. [Qu'est-ce qu'un bloc de code ?](#heading-quest-ce-quun-bloc-de-code)
8. [Qu'est-ce qu'un corps de fonction ?](#heading-quest-ce-quun-corps-de-fonction)
9. [Les types de fonctions JavaScript](#heading-les-types-de-fonctions-javascript)
10. [Qu'est-ce qu'une déclaration de fonction JavaScript ?](#heading-quest-ce-quune-declaration-de-fonction-javascript)
11. [Qu'est-ce qu'une expression de fonction JavaScript ?](#heading-quest-ce-quune-expression-de-fonction-javascript)
12. [Qu'est-ce qu'une expression de fonction fléchée JavaScript ?](#heading-quest-ce-quune-expression-de-fonction-flechee-javascript)
13. [Qu'est-ce qu'une expression de fonction invoquée immédiatement (IIFE) en JavaScript ?](#heading-quest-ce-quune-expression-de-fonction-invoquee-immediatement-javascript)
14. [Aperçu](#heading-apercu)

Alors, commençons par les bases.

## Qu'est-ce qu'une fonction ?

Une **fonction JavaScript** est un morceau de code exécutable que les développeurs utilisent pour regrouper un bloc de zéro ou plusieurs instructions.

En d'autres termes, une fonction est un sous-programme exécutable (mini-programme).

Une fonction JavaScript est un sous-programme parce que son corps se compose d'une série d'instructions pour les ordinateurs — tout comme un programme ordinaire.

Les instructions dans le corps d'une fonction peuvent être une déclaration de [variable](https://codesweetly.com/javascript-variable#example-3-javascript-variable), un appel [return](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return), une invocation [console.log()](https://developer.mozilla.org/en-US/docs/Web/API/console/log), une définition de [fonction](#heading-syntaxe-dune-fonction-javascript-1) ou toute autre [instruction](https://codesweetly.com/javascript-statement) JavaScript.

**Note :**

* Un programme est une liste d'instructions écrites pour être exécutées par des ordinateurs.
* Contrairement aux autres [types d'objets](https://codesweetly.com/javascript-non-primitive-data-type#types-of-javascript-objects), vous pouvez invoquer une fonction sans la stocker dans une variable.
* Une fonction JavaScript est similaire aux procédures ou sous-programmes d'autres langages de programmation.

## Pourquoi utiliser des fonctions ?

Les fonctions permettent de regrouper des morceaux de code et de les réutiliser n'importe quand, n'importe où, pour une durée illimitée. Cela vous aide à éliminer la corvée d'écrire le même code de manière répétée.

Par exemple, [alert()](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert) est une [fonction intégrée de l'objet window](https://developer.mozilla.org/en-US/docs/Web/API/Window) que quelqu'un a écrite une fois pour que tous les développeurs puissent l'utiliser n'importe quand, n'importe où.

## Syntaxe d'une fonction JavaScript

```js
function nomDeLaFonction(parametre1, parametre2, ..., parametreX) {
  // corps de la fonction
}
```

Une fonction est composée de cinq éléments :

1. Un mot-clé `function`
2. Le nom de la fonction
3. Une liste de zéro ou plusieurs paramètres
4. Un bloc de code (`{...}`)
5. Le corps de la fonction

Examinons chaque élément.

## Qu'est-ce que le mot-clé `function` ?

Nous utilisons le mot-clé `function` pour déclarer aux navigateurs qu'un morceau de code spécifique est une fonction JavaScript — et non une fonction mathématique ou une autre fonction générique.

## Qu'est-ce qu'un nom de fonction ?

Le **nom d'une fonction** vous permet de créer un identifiant pour votre fonction, que vous pouvez utiliser pour y faire référence.

## Qu'est-ce qu'un paramètre ?

Un **paramètre** spécifie le nom que vous souhaitez donner à l'[argument](https://codesweetly.com/javascript-arguments) de votre fonction.

Un paramètre est un composant optionnel d'une fonction. En d'autres termes, vous n'avez pas besoin de spécifier de paramètre si votre fonction n'accepte aucun argument.

Par exemple, la méthode [pop()](https://codesweetly.com/javascript-pop-method) de JavaScript est une fonction sans aucun paramètre car elle n'accepte pas d'arguments.

D'un autre côté, [forEach()](https://codesweetly.com/javascript-foreach-method) possède deux paramètres qui acceptent deux arguments.

### Exemple d'un paramètre JavaScript

```js
// Définir une fonction avec deux paramètres :
function monNom(prenom, nom) {
  console.log(`Mon nom complet est ${prenom} ${nom}.`);
}

// Invoquer la fonction monNom tout en passant deux arguments à ses paramètres :
monNom("Oluwatobi", "Sofela");

// L'appel ci-dessus retournera :
"Mon nom complet est Oluwatobi Sofela."
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-edvj3g?devToolsHeight=33&file=index.js)

La fonction `monNom()` dans l'extrait ci-dessus possède deux paramètres : `prenom` et `nom`.

Supposons que vous souhaitiez prédéfinir des valeurs pour vos paramètres que les navigateurs pourront utiliser si les utilisateurs n'invoquent pas la fonction avec les arguments requis. Dans ce cas, vous pouvez créer des paramètres par défaut.

### Qu'est-ce qu'un paramètre par défaut ?

Les **paramètres par défaut** vous permettent d'initialiser les paramètres de votre fonction avec des valeurs par défaut.

Par exemple, supposons que des utilisateurs invoquent votre fonction sans fournir un argument requis. Dans un tel cas, les navigateurs définiront la valeur du paramètre sur `undefined`.

Cependant, les paramètres par défaut vous permettent de définir les valeurs que les navigateurs doivent utiliser à la place de `undefined`.

### Exemples de paramètres par défaut

Voici des exemples du fonctionnement des paramètres par défaut en JavaScript.

#### Comment définir une fonction sans paramètres par défaut

```js
// Définir une fonction avec deux paramètres :
function monNom(prenom, nom) {
  console.log(`Mon nom complet est ${prenom} ${nom}.`);
}

// Invoquer la fonction monNom tout en passant un seul argument à ses paramètres :
monNom("Oluwatobi");

// L'appel ci-dessus retournera :
"Mon nom complet est Oluwatobi undefined."
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-9ce3xt?devToolsHeight=33&file=index.js)

L'ordinateur a automatiquement défini le paramètre `nom` sur `undefined` car nous n'avons pas fourni de valeur par défaut.

#### Comment définir une fonction avec un argument `undefined` et aucun paramètre par défaut

```js
// Définir une fonction avec deux paramètres :
function monNom(prenom, nom) {
  console.log(`Mon nom complet est ${prenom} ${nom}.`);
}

// Invoquer la fonction monNom tout en passant deux arguments à ses paramètres :
monNom("Oluwatobi", undefined);

// L'appel ci-dessus retournera :
"Mon nom complet est Oluwatobi undefined."
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-csbxta?devToolsHeight=33&file=index.js)

L'ordinateur a défini le paramètre `nom` sur `undefined` parce que nous avons fourni `undefined` comme second argument de `monNom()`.

#### Comment définir une fonction avec un paramètre par défaut

```js
// Définir une fonction avec deux paramètres :
function monNom(prenom, nom = "Sofela") {
  console.log(`Mon nom complet est ${prenom} ${nom}.`);
}

// Invoquer la fonction monNom tout en passant un seul argument à ses paramètres :
monNom("Oluwatobi");

// L'appel ci-dessus retournera :
"Mon nom complet est Oluwatobi Sofela."
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ghiyzm?devToolsHeight=33&file=index.js)

Au lieu de `undefined`, JavaScript a utilisé `"Sofela"` comme argument par défaut du paramètre `nom`.

#### Comment définir une fonction avec un argument `undefined` et un paramètre par défaut

```js
// Définir une fonction avec deux paramètres :
function monNom(prenom, nom = "Sofela") {
  console.log(`Mon nom complet est ${prenom} ${nom}.`);
}

// Invoquer la fonction monNom tout en passant deux arguments à ses paramètres :
monNom("Oluwatobi", undefined);

// L'appel ci-dessus retournera :
"Mon nom complet est Oluwatobi Sofela."
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-umqgqp?devToolsHeight=33&file=index.js)

Au lieu de `undefined`, JavaScript a utilisé `"Sofela"` comme argument par défaut du paramètre `nom`.

Discutons maintenant du quatrième élément d'une fonction JavaScript : un **bloc de code.**

## Qu'est-ce qu'un bloc de code ?

Un **bloc** est une paire d'accolades (`{...}`) utilisée pour regrouper plusieurs instructions.

**Voici un exemple :**

```js
{
  const heureActuelle = new Date().getHours();
}
```

Le bloc dans l'extrait ci-dessus contient une [instruction](https://codesweetly.com/javascript-statement) JavaScript.

**Voici un autre exemple :**

```js
if (new Date().getHours() < 18) {
  const heureActuelle = new Date().getHours();
  const minutesActuelles = new Date().getMinutes();
  console.log(`Il est ${heureActuelle}:${minutesActuelles}.`);
}
```

Le bloc de code de la condition `if` a regroupé trois instructions JavaScript.

**Maintenant, considérez cet extrait :**

```js
function obtenirHeure() {
  const heureActuelle = new Date().getHours();
  const minutesActuelles = new Date().getMinutes();
  console.log(`Il est ${heureActuelle}:${minutesActuelles}.`);
}
```

Le bloc de code de la fonction `obtenirHeure()` a regroupé trois instructions JavaScript. Notez que le "corps de la fonction" est l'espace à l'intérieur du bloc de code de la fonction. Parlons-en plus en détail maintenant.

## Qu'est-ce qu'un corps de fonction ?

Un **corps de fonction** est l'endroit où vous placez une séquence d'instructions que vous souhaitez exécuter.

### Syntaxe du corps d'une fonction JavaScript

```js
function nomDeLaFonction() {
  // corps de la fonction
}

```

### Exemples de corps de fonction

Voici des exemples d'utilisation du corps de la fonction.

#### Comment définir une fonction avec trois instructions dans son corps

```js
function obtenirNom() {
  const prenom = "Oluwatobi";
  const nom = "Sofela";
  console.log(prenom + " " + nom);
}

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-flz5tf?devToolsHeight=33&file=index.js)

Dans l'extrait ci-dessus, le corps de la fonction contient trois instructions que l'ordinateur exécutera chaque fois que la fonction sera invoquée.

**Note :** `console.log()` est une [méthode](https://codesweetly.com/web-tech-terms-m#method) que nous utilisons pour journaliser (écrire) des messages dans une console Web.

#### Comment définir une fonction avec deux instructions dans son corps

```js
const meilleuresCouleurs = ["Coral", "Blue", "DeepPink"];

function mettreAJourMesCouleurs(couleursPrecedentes, nouvelleCouleur) {
   const mesMeilleuresCouleurs = [...couleursPrecedentes, nouvelleCouleur];
   return mesMeilleuresCouleurs;
}

mettreAJourMesCouleurs(meilleuresCouleurs, "GreenYellow");
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-nb9sr6?devToolsHeight=33&file=index.js)

Dans l'extrait ci-dessus, le corps de la fonction contient deux instructions que l'ordinateur exécutera chaque fois que la fonction sera invoquée.

**Note :**

* Les trois points que nous avons ajoutés devant `couleursPrecedentes` sont appelés un [opérateur de décomposition (spread operator)](https://codesweetly.com/spread-operator). Nous l'avons utilisé pour étendre l'argument [tableau](https://codesweetly.com/javascript-array-object) en éléments individuels.
* Vous pouvez également faire précéder le paramètre `nouvelleCouleur` d'un [opérateur de reste (rest operator)](https://codesweetly.com/javascript-rest-operator) si vous souhaitez ajouter deux nouvelles couleurs ou plus.
* Le mot-clé `return` met fin à l'exécution de sa fonction et renvoie l'[expression](https://codesweetly.com/javascript-statement#what-is-a-javascript-expression-statement) spécifiée (ou `undefined` si vous ne fournissez aucune expression).

Maintenant que nous connaissons les composants d'une fonction JavaScript, nous pouvons discuter de ses types.

## Les types de fonctions JavaScript

Les quatre types de fonctions JavaScript sont :

* Déclaration de fonction
* Expression de fonction
* Expression de fonction fléchée
* Expression de fonction invoquée immédiatement (IIFE)

Examinons chaque type.

## Qu'est-ce qu'une déclaration de fonction JavaScript ?

Une **déclaration de fonction** est une fonction créée sans l'assigner à une [variable](https://codesweetly.com/javascript-variable).

**Note :** Nous appelons parfois la déclaration de fonction une "définition de fonction" ou une "instruction de fonction".

**Voici un exemple :**

```js
function additionnerNombres() {
  return 100 + 20;
}

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-pwh2jr?devToolsHeight=33&file=index.js)

La fonction ci-dessus est une déclaration de fonction car nous l'avons définie sans la stocker dans une variable.

## Qu'est-ce qu'une expression de fonction JavaScript ?

Une **expression de fonction** est une fonction que vous créez et assignez à une variable.

**Voici un exemple :**

```js
const monExprDeFunc = function additionnerNombres() {
  return 100 + 20;
};

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-hjg1iq?devToolsHeight=33&file=index.js)

La fonction ci-dessus est une expression de fonction **nommée** que nous avons assignée à la variable `monExprDeFunc`.

Vous pouvez également écrire l'extrait ci-dessus sous forme d'expression de fonction **anonyme** comme ceci :

```js
const monExprDeFunc = function() {
  return 100 + 20;
};

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-pmeqy4?devToolsHeight=33&file=index.js)

La fonction ci-dessus est une expression de fonction anonyme que nous avons assignée à la variable `monExprDeFunc`.

**Note :**

* Une **fonction anonyme** est une fonction sans nom.
* Une **fonction nommée** est une fonction avec un nom.

Le principal avantage d'une fonction nommée est que le nom facilite la recherche de l'origine d'une erreur.

En d'autres termes, supposons que votre fonction génère une erreur. Dans ce cas, si la fonction est nommée, la [trace de la pile (stack trace)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack) d'un débogueur contiendra le nom de la fonction. Par conséquent, il vous sera plus facile d'identifier l'origine de l'erreur.

## Qu'est-ce qu'une expression de fonction fléchée JavaScript ?

Une **expression de fonction fléchée** est une manière abrégée d'écrire une expression de fonction.

### Syntaxe d'une fonction fléchée

Nous définissons une fonction fléchée avec les symboles d'égalité et de supériorité (`=>`). Voici la syntaxe :

```js
const nomDeVariable = () => {
  // corps de la fonction
}

```

### Exemple d'une fonction fléchée

```js
const monExprDeFunc = () => {
  return 100 + 20;
};

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-1euhch?devToolsHeight=33&file=index.js)

Vous pouvez voir que nous avons défini la fonction sans mot-clé `function` ni nom de fonction.

Vous devez omettre le mot-clé `function` et le nom de la fonction lors de l'écriture d'une expression de fonction fléchée. Sinon, JavaScript lèvera une erreur de syntaxe (`SyntaxError`).

### Choses importantes à savoir sur l'expression de fonction fléchée JavaScript

Voici trois faits essentiels à retenir lors de l'utilisation d'une expression de fonction fléchée.

#### 1. Les parenthèses des paramètres sont facultatives

Supposons que votre fonction fléchée ne contienne qu'un seul paramètre. Dans ce cas, vous pouvez omettre ses parenthèses.

```js
const monExprDeFunc = a => {
  return a + 20;
};

```

[**Essayer sur CodePen**](https://codepen.io/oluwatobiss/pen/OJQJejr)

#### 2. Les accolades et le mot-clé `return` sont facultatifs

Supposons que votre fonction fléchée ne contienne qu'une seule instruction. Dans ce cas, vous pouvez omettre ses accolades et le mot-clé `return`.

```js
const monExprDeFunc = (x, y) => x + y;
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-8t2udu?devToolsHeight=33&file=index.js)

Dans l'extrait ci-dessus, nous avons implicitement renvoyé la somme des paramètres `x` et `y` en supprimant les accolades et le mot-clé `return`.

**Note :** Chaque fois que vous choisissez d'omettre les accolades, assurez-vous également de supprimer le mot-clé `return`. Sinon, l'ordinateur lèvera une erreur de syntaxe (`SyntaxError`).

#### 3. Utilisez des parenthèses pour envelopper tout retour d'objet implicite

Supposons que vous souhaitiez renvoyer un objet implicitement. Dans ce cas, enveloppez l'objet dans un [opérateur de groupement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Grouping) `(...)`.

Par exemple, considérez le code ci-dessous :

```js
const monExprDeFunc = () => {
  carColor: "White",
  shoeColor: "Yellow",
};

```

[**Essayer sur CodeSandbox**](https://codesandbox.io/s/wrong-way-to-use-an-arrow-function-expression-to-return-an-object-implicitly-s8w132?file=/src/index.js)

L'extrait ci-dessus lèvera une erreur de syntaxe (`SyntaxError`) car JavaScript a supposé que les accolades (`{}`) étaient le bloc de code du corps de la fonction — et non un [littéral d'objet](https://codesweetly.com/javascript-properties-object).

Par conséquent, chaque fois que vous souhaitez renvoyer un littéral d'objet implicitement — sans utiliser explicitement le mot-clé `return` — assurez-vous d'envelopper le littéral d'objet dans un opérateur de groupement.

**Voici un exemple :**

```js
const monExprDeFunc = () => ({
  carColor: "White",
  shoeColor: "Yellow",
});

```

[**Essayer sur CodeSandbox**](https://codesandbox.io/s/correct-way-to-use-an-arrow-function-expression-to-return-an-object-implicitly-p61l5c?file=/src/index.js)

Notez que vous pouvez utiliser l'opérateur de groupement pour renvoyer n'importe quelle valeur unique. Par exemple, l'extrait ci-dessous a regroupé la somme de `x` et `56`.

```js
const monExprDeFunc = x => (x + 56);
```

[**Essayer sur CodePen**](https://codepen.io/oluwatobiss/pen/rNJNXeG)

Discutons maintenant du quatrième type de fonction JavaScript.

## Qu'est-ce qu'une expression de fonction invoquée immédiatement (IIFE) en JavaScript ?

Une **expression de fonction invoquée immédiatement (IIFE)** est une expression de fonction qui s'invoque automatiquement.

**Note :** Nous appelons parfois une IIFE une "expression de fonction auto-invoquée" ou une "expression de fonction anonyme auto-exécutable".

### Syntaxe d'une IIFE

```js
(function() {
  /* ... */
})();

```

Une IIFE est composée de trois composants principaux :

1. **Un opérateur de groupement :** La première paire de parenthèses `()`
2. **Une fonction :** Enfermée dans l'opérateur de groupement
3. **Un invocateur :** La dernière paire de parenthèses `()`

### Exemples

Voici des exemples d'une IIFE.

#### Comment définir une IIFE nommée

```js
(function additionnerNombres() {
  console.log(100 + 20);
})();

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-nkjjnz?devToolsHeight=33&file=index.js)

La fonction dans l'extrait ci-dessus est une expression de fonction auto-invoquée nommée.

#### Comment définir une IIFE anonyme

```js
(function() {
  console.log(100 + 20);
})();

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ywrmkt?devToolsHeight=33&file=index.js)

La fonction dans l'extrait ci-dessus est une expression de fonction auto-invoquée anonyme.

#### Comment définir une IIFE de fonction fléchée

```js
(() => console.log(100 + 20))();
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-xqlfgi?devToolsHeight=33&file=index.js)

La fonction dans l'extrait ci-dessus est une expression de fonction auto-invoquée fléchée.

#### Comment définir une IIFE asynchrone

```js
(async () => console.log(await 100 + 20))();
```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-ryxftq?devToolsHeight=33&file=index.js)

La fonction dans l'extrait ci-dessus est une expression de fonction auto-invoquée [asynchrone](https://codesweetly.com/asynchronous-javascript).

Maintenant que nous savons ce qu'est une expression de fonction invoquée immédiatement, nous pouvons discuter de son fonctionnement.

### Comment fonctionne une IIFE ?

Par défaut, l'ordinateur ne connaît pas le [type de données](https://codesweetly.com/javascript-data-types) d'un [code](https://codesweetly.com/document-vs-data-vs-code#what-exactly-is-code) avant de l'avoir évalué.

Par exemple, supposons que vous demandiez à l'ordinateur de traiter `4`. Dans ce cas, le système ne saura pas si `4` est un type de nombre tant qu'il ne l'aura pas évalué.

Par conséquent, JavaScript lèvera une erreur de syntaxe (`SyntaxError`) si vous utilisez une méthode de nombre directement sur `4`.

**Voici un exemple :**

```js
// Convertir 4 en une valeur de chaîne de caractères :
4.toString();

// L'appel ci-dessus retournera :
"Uncaught SyntaxError: Invalid or unexpected token"

```

[**Essayer sur CodeSandbox**](https://codesandbox.io/s/how-iife-works-example-1-kc8g5b)

L'ordinateur a levé une erreur de syntaxe (`SyntaxError`) car il ne reconnaît pas `4` comme un type de données numérique.

Cependant, supposons que vous assigniez `4` à une variable. Dans ce cas, l'ordinateur le convertira d'abord en un type de données numérique avant de le stocker dans la variable.

Ensuite, JavaScript vous permettra d'utiliser n'importe quelle méthode de nombre sur la variable numérique.

**Voici un exemple :**

```js
// Assigner 4 à une variable :
const monNum = 4;

// Convertir le contenu de monNum en une valeur de chaîne de caractères :
monNum.toString();

// L'appel ci-dessus retournera :
"4"

```

[**Essayer sur CodeSandbox**](https://codesandbox.io/s/how-iife-works-example-2-jz4kwi)

L'extrait ci-dessus n'a renvoyé aucune erreur car JavaScript a évalué `monNum` comme un type de données numérique.

Mais vous n'avez pas besoin d'assigner `4` à une variable avant que l'ordinateur puisse évaluer son type de données de manière appropriée.

Vous pouvez alternativement mettre votre valeur entre [parenthèses](https://www.computerhope.com/jargon/p/parenthe.htm) pour forcer l'ordinateur à évaluer son type de données avant de l'utiliser pour d'autres choses.

Par exemple, considérez cet extrait :

```js
// Évaluer le type de données de 4 et le transformer en une valeur de chaîne de caractères :
(4).toString();

// L'appel ci-dessus retournera :
"4"

```

[**Essayer sur CodeSandbox**](https://codesandbox.io/s/how-iife-works-example-3-rz4j9b)

L'extrait ci-dessus a enfermé `4` entre parenthèses pour que l'ordinateur évalue son type de données avant d'utiliser la méthode [`toString()`](https://codesweetly.com/javascript-number-tostring-method) pour le convertir en une valeur de chaîne de caractères.

L'utilisation de parenthèses pour que JavaScript évalue d'abord le type de données de votre code est ce qui se passe dans une expression de fonction invoquée immédiatement (IIFE).

Par exemple, considérez cet exemple :

```js
// Évaluer le type de données de la fonction et l'invoquer immédiatement :
(function additionnerNombres() {
  console.log(100 + 20);
})();

// L'appel ci-dessus retournera :
120

```

[**Essayer sur StackBlitz**](https://stackblitz.com/edit/js-nkjjnz?devToolsHeight=33&file=index.js)

L'extrait ci-dessus a enfermé la fonction `additionnerNombres` entre parenthèses pour que l'ordinateur évalue son type de données avant de l'invoquer immédiatement après l'évaluation.

## Aperçu

Dans cet article, nous avons discuté de ce qu'est un objet fonction JavaScript. Nous avons également utilisé des exemples pour voir comment il fonctionne.

Merci de votre lecture.

### **Et voici une ressource ReactJS utile :**

J'ai écrit un livre sur React !

* Il est adapté aux débutants ✔
* Il contient des extraits de code en direct ✔
* Il contient des projets évolutifs ✔
* Il contient de nombreux exemples faciles à comprendre ✔

Le livre [React Explained Clearly](https://www.amazon.com/dp/B09KYGDQYW) est tout ce dont vous avez besoin pour comprendre ReactJS.

[![Le livre React Explained Clearly est maintenant disponible sur Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://www.amazon.com/dp/B09KYGDQYW)