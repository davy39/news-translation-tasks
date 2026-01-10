---
title: Comment utiliser la logique en JavaScript – Opérateurs, Conditions, Truthy/Falsy,
  et plus
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-11-29T21:50:16.000Z'
originalURL: https://freecodecamp.org/news/logic-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Beige-aesthetic-thesis-defense-presentation.png
tags:
- name: JavaScript
  slug: javascript
- name: logic
  slug: logic
seo_title: Comment utiliser la logique en JavaScript – Opérateurs, Conditions, Truthy/Falsy,
  et plus
seo_desc: "JavaScript is a versatile programming language that empowers developers\
  \ to create dynamic and interactive web pages. \nOne of the foundational elements\
  \ of JavaScript programming is the application of logical operations to make decisions\
  \ and control pr..."
---

JavaScript est un langage de programmation polyvalent qui permet aux développeurs de créer des pages web dynamiques et interactives.

L'un des éléments fondamentaux de la programmation JavaScript est l'application d'opérations logiques pour prendre des décisions et contrôler le flux du programme.

Dans ce guide, nous allons approfondir les bases des opérations logiques en JavaScript. Je vais fournir des explications simples et de nombreux extraits de code pour rendre ces concepts plus faciles à comprendre.

## Comprendre les opérateurs logiques

Les opérateurs logiques en JavaScript permettent aux développeurs d'effectuer des opérations sur des valeurs ou des expressions, jouant un rôle crucial dans la prise de décision efficace au sein du code.

Les principaux opérateurs logiques sont `&&` (ET), `||` (OU) et `!` (NON). Examinons chacun d'eux maintenant.

### 1. Opérateur ET (`&&`)

L'opérateur ET (`&&`) en JavaScript est un opérateur logique qui combine deux conditions ou plus. Il retourne `true` uniquement si toutes les conditions évaluées sont `true`. Si l'une des conditions est `false`, l'expression entière est évaluée à `false`.

### Exemple :

```javascript
let isSunny = true;
let isWarm = true;

if (isSunny && isWarm) {
  console.log("Temps parfait pour les activités de plein air !");
} else {
  console.log("Peut-être un autre jour.");
}

```

Dans cet exemple, la condition `isSunny && isWarm` doit être vraie pour que le message sur le temps parfait soit affiché. Si `isSunny` ou `isWarm` est `false`, le bloc `else` est exécuté.

Examinons quelques scénarios où l'opérateur ET est particulièrement utile.

**Lors de la combinaison de conditions :** Utilisez `&&` lorsque vous voulez qu'une action soit effectuée uniquement lorsque plusieurs conditions sont remplies simultanément.

```javascript
if (userIsLoggedIn && userHasPermission) {
  // Effectuer une action privilégiée.
} else {
  // Afficher un message d'erreur ou rediriger vers la connexion.
}

```

**Dans les clauses de garde :** Utilisez `&&` dans les clauses de garde pour vous assurer que certaines conditions sont remplies avant de poursuivre l'exécution du code.

```javascript
function performAction(user) {
  if (!user || !user.isLoggedIn) {
    return; // Quitter tôt si l'utilisateur n'est pas connecté.
  }

  // Continuer avec l'action pour les utilisateurs connectés.
}

```

**Pour la validation de formulaire :** Dans des scénarios comme la validation de formulaire, vous pouvez utiliser `&&` pour vérifier plusieurs conditions avant d'autoriser la soumission du formulaire.

```javascript
if (isUsernameValid && isPasswordValid && isEmailValid) {
  // Soumettre le formulaire.
} else {
  // Afficher un message d'erreur.
}

```

L'opérateur ET est utile lorsque vous voulez vous assurer que toutes les conditions spécifiées sont vraies avant de poursuivre avec une action ou une décision particulière dans votre code. C'est un outil fondamental pour créer une logique plus nuancée et spécifique au contexte dans vos programmes JavaScript.

### 2. Opérateur OU (`||`)

L'opérateur OU (`||`) en JavaScript est un opérateur logique qui retourne `true` si au moins l'une des conditions qu'il connecte est `true`. Il est souvent utilisé lorsque vous voulez qu'une action se produise si l'une des multiples conditions est remplie.

Voici un exemple de base pour illustrer l'opérateur OU :

```javascript
let hasCoffee = true;
let hasTea = false;

if (hasCoffee || hasTea) {
  console.log("Vous pouvez profiter d'une boisson chaude !");
} else {
  console.log("Aucune boisson chaude disponible.");
}

```

Dans cet exemple, la condition `hasCoffee || hasTea` est `true` parce que `hasCoffee` est `true`. Par conséquent, le message "Vous pouvez profiter d'une boisson chaude !" sera enregistré.

Voici quelques scénarios où vous pourriez vouloir utiliser l'opérateur OU :

**Valeurs de repli :**

```javascript
let userInput = ""; // L'utilisateur n'a pas fourni de valeur
let username = userInput || "Invité";
console.log("Bienvenue, " + username);

```

Dans ce cas, si l'utilisateur n'a pas fourni de nom d'utilisateur (`userInput` est une chaîne vide), l'opérateur OU attribue une valeur par défaut de "Invité" à `username`. C'est un modèle courant pour fournir des valeurs de repli ou par défaut.

**Vérification de plusieurs conditions :**

```javascript
let isWeekend = false;
let isHoliday = true;

if (isWeekend || isHoliday) {
  console.log("C'est l'heure de faire une pause !");
} else {
  console.log("Retour au travail.");
}

```

Cet exemple utilise l'opérateur OU pour vérifier si c'est le week-end ou un jour férié, indiquant qu'il est temps de faire une pause.

**Validation de formulaire :**

```javascript
let username = "john_doe";
let password = "";

if (username && password) {
  console.log("Formulaire soumis avec succès !");
} else {
  console.log("Veuillez remplir à la fois le nom d'utilisateur et le mot de passe.");
}

```

Ici, l'opérateur OU peut être utilisé pour vérifier si le nom d'utilisateur ou le mot de passe est manquant. Si l'une des conditions est `true`, il invite l'utilisateur à remplir les deux champs.

L'opérateur OU est utile lorsque vous voulez qu'une action se produise si au moins l'une des conditions spécifiées est vraie. Il est couramment utilisé dans des scénarios impliquant des valeurs de repli, la vérification de plusieurs conditions ou la validation de formulaires où l'un des plusieurs champs doit être rempli.

### 3. Opérateur NON (`!`)

L'opérateur NON (`!`) en JavaScript est un opérateur unaire qui nie la vérité d'une valeur. Il est utilisé pour inverser une valeur booléenne ou une expression truthy/falsy. En termes plus simples, il transforme `true` en `false` et `false` en `true`. Voici comment il fonctionne :

```javascript
let isSunny = true;

// Utilisation de l'opérateur NON pour inverser la valeur
let isNotSunny = !isSunny;

console.log(isNotSunny); // Sortie : false

```

Maintenant, discutons de quand vous pourriez vouloir utiliser l'opérateur NON :

**Vérification de la négation :** L'utilisation la plus directe de l'opérateur NON est lorsque vous voulez vérifier la négation d'une condition. Par exemple :

```javascript
let isRaining = false;

if (!isRaining) {
  console.log("Il ne pleut pas. Profitez de la journée !");
} else {
  console.log("N'oubliez pas votre parapluie !");
}

```

Dans ce cas, la condition `!isRaining` est vraie lorsqu'il ne pleut pas. Cela fournit un moyen concis d'exprimer l'idée qu'il fait beau lorsqu'il ne pleut pas.

**Vérification des valeurs Falsy :** L'opérateur NON est souvent utilisé pour vérifier si une valeur est falsy. Rappelez-vous qu'en JavaScript, certaines valeurs sont considérées comme falsy, telles que `false`, `0`, `null`, `undefined`, `NaN`, et une chaîne vide `""`. L'opérateur NON peut être utile pour vérifier si une variable contient une valeur falsy :

```javascript
let userRole = null;

if (!userRole) {
  console.log("Le rôle de l'utilisateur n'est pas défini. Attribution d'un rôle par défaut.");
  userRole = "Invité";
}

```

Dans cet exemple, si `userRole` est `null` (une valeur falsy), la condition `!userRole` est évaluée à `true`, et un rôle par défaut est attribué.

**Création de conditions plus claires :** L'opérateur NON peut également être utilisé pour rendre les conditions plus explicites ou lisibles. Par exemple :

```javascript
let isLoggedIn = false;

if (!isLoggedIn) {
  console.log("L'utilisateur n'est pas connecté. Redirection vers la page de connexion.");
}

```

Cette condition vérifie si l'utilisateur n'est pas connecté et prend une action en conséquence.

L'opérateur NON est utile lorsque vous devez nier une valeur booléenne ou vérifier des valeurs falsy, fournissant un moyen concis et lisible d'exprimer des conditions dans votre code JavaScript.

## Comment combiner les opérateurs logiques

Vous pouvez combiner des opérateurs logiques pour créer des conditions plus complexes, en introduisant des parenthèses pour contrôler l'ordre d'évaluation.

Considérons un exemple où nous voulons déterminer si une personne est éligible pour entrer dans un club en fonction de son âge et de savoir si elle a une pièce d'identité valide. Les conditions d'entrée sont les suivantes :

* La personne doit avoir au moins 18 ans.
* Si la personne a entre 16 et 18 ans, elle peut entrer uniquement si elle a une pièce d'identité valide.
* Si la personne a moins de 16 ans, l'entrée n'est pas autorisée.

Voici le code JavaScript pour ce scénario :

```javascript
let age = 17;
let hasValidID = false;

if ((age >= 18) || (age >= 16 && hasValidID)) {
    console.log("Bienvenue au club !");
} else {
    console.log("Entrée non autorisée.");
}

```

Dans ce code :

* `age` est défini à `17`, indiquant que la personne a 17 ans.
* `hasValidID` est défini à `false`, indiquant que la personne n'a pas de pièce d'identité valide.

Maintenant, évaluons la condition dans l'instruction `if` :

1. `(age >= 18)` est évalué à `false` parce que la personne n'a pas 18 ans ou plus.
2. `(age >= 16 && hasValidID)` est évalué à `true && false`, ce qui est `false`. Cela est dû au fait que la personne a 17 ans, ce qui satisfait la première partie de la condition, mais elle n'a pas de pièce d'identité valide.

Puisque les deux parties de la condition sont `false`, le bloc de code dans l'instruction `else` est exécuté, ce qui donne le résultat :

```
Entrée non autorisée.

```

Cet exemple démontre comment les opérateurs logiques peuvent être combinés pour créer des conditions complexes, vous permettant de contrôler le flux de votre programme en fonction de divers facteurs.

## Instructions conditionnelles

Les opérateurs logiques sont fréquemment utilisés dans les instructions conditionnelles (`if`, `else if` et `else`) pour dicter le flux du programme en fonction de conditions spécifiques.

### 1. **Instruction if :**

L'instruction `if` en JavaScript est utilisée pour exécuter un bloc de code si une condition spécifiée est vraie. Les opérateurs logiques jouent souvent un rôle crucial dans la définition de ces conditions.

```javascript
let isHungry = true;
let hasFood = true;

if (isHungry && hasFood) {
  console.log("Mangeons !");
} else {
  console.log("Pas besoin de manger tout de suite.");
}

```

Dans cet exemple, l'opérateur `&&` (ET) combine deux conditions (`isHungry` et `hasFood`). Le bloc de code à l'intérieur de l'instruction `if` ne sera exécuté que si les deux conditions sont vraies. Si `isHungry` ou `hasFood` est faux, le code à l'intérieur du bloc `else` sera exécuté.

### 2. **Instruction else :**

L'instruction `else` est associée à l'instruction `if` pour exécuter un bloc de code lorsque la condition spécifiée est fausse.

```javascript
let isNight = true;

if (isNight) {
  console.log("C'est la nuit. Bonne nuit !");
} else {
  console.log("C'est le jour. Bonne journée !");
}

```

Ici, l'instruction `if` vérifie si `isNight` est vrai. Si c'est le cas, le message correspondant est imprimé. Si `isNight` est faux, le bloc `else` est exécuté, fournissant un message alternatif pour la journée.

### 3. **Instruction else if :**

L'instruction `else if` permet de gérer plusieurs conditions, permettant une prise de décision plus complexe.

```javascript
let timeOfDay = "morning";

if (timeOfDay === "morning") {
  console.log("Bonjour !");
} else if (timeOfDay === "afternoon") {
  console.log("Bon après-midi !");
} else {
  console.log("Bonsoir !");
}

```

Dans ce cas, le code salue les utilisateurs différemment en fonction de la valeur de `timeOfDay`. L'opérateur `===` est utilisé pour une comparaison d'égalité stricte, et des opérateurs logiques comme `&&` ou `||` peuvent être incorporés pour former des conditions plus complexes.

Ces exemples illustrent comment les opérateurs logiques sont utilisés dans les instructions `if`, `else` et `else if` pour contrôler le flux d'un programme JavaScript en fonction de conditions spécifiques.

## Opérateur ternaire

L'opérateur ternaire, souvent représenté par `? :`, fournit une manière concise d'exprimer des instructions conditionnelles. C'est une version abrégée d'une instruction `if-else`. La syntaxe de base est :

```javascript
condition ? expression_si_vrai : expression_si_faux;

```

Voici une décomposition des composants :

* `condition` : une expression booléenne qui est évaluée. Si elle est vraie, l'expression avant le `:` est exécutée – sinon, l'expression après le `:` est exécutée.
* `expression_si_vrai` : la valeur ou l'expression retournée si la condition est vraie.
* `expression_si_faux` : la valeur ou l'expression retournée si la condition est fausse.

Maintenant, examinons de plus près l'exemple fourni :

```javascript
const weather = isSunny ? "Profitez du soleil !" : "Prenez un parapluie !";

```

Dans cet exemple :

* `isSunny` est la condition vérifiée. Si `isSunny` est vrai, la valeur de l'expression entière devient "Profitez du soleil !". Si `isSunny` est faux, la valeur devient "Prenez un parapluie !".
* Le `?` est comme poser une question : "Est-ce qu'il fait soleil ?" Si la réponse est oui, alors "Profitez du soleil !" est la réponse (avant le `:`). Si la réponse est non, alors "Prenez un parapluie !" est la réponse (après le `:`).

Cela peut être vu comme une manière abrégée d'écrire une instruction `if-else`. L'instruction `if-else` équivalente pour l'exemple serait :

```javascript
let weather;
if (isSunny) {
  weather = "Profitez du soleil !";
} else {
  weather = "Prenez un parapluie !";
}

```

L'opérateur ternaire et l'instruction `if-else` atteignent le même résultat, mais l'opérateur ternaire est plus concis et est souvent utilisé pour des affectations conditionnelles simples.

Il est important de noter que l'utilisation excessive de l'opérateur ternaire ou dans des scénarios complexes peut réduire la lisibilité du code, il est donc préférable de l'utiliser pour des conditions simples.

## Instruction switch

L'instruction `switch` gère plusieurs conditions efficacement, en particulier lorsqu'il y a plusieurs valeurs possibles pour une variable. Étendons notre exemple de jour de la semaine :

```javascript
let dayOfWeek = "Wednesday";

switch (dayOfWeek) {
  case "Monday":
    console.log("C'est le début de la semaine.");
    break;
  case "Wednesday":
    console.log("C'est le milieu de la semaine.");
    break;
  case "Friday":
    console.log("C'est la fin de la semaine.");
    break;
  default:
    console.log("C'est un jour ordinaire.");
}

```

Ici, l'instruction `switch` déclenche le message approprié en fonction du jour de la semaine.

## Évaluation en court-circuit

JavaScript utilise l'évaluation en court-circuit avec les opérateurs logiques, optimisant les performances en arrêtant l'évaluation une fois le résultat déterminé.

### Exemple 1 : Court-circuit avec l'opérateur `&&`

```javascript
let isTrue = false;
let result = isTrue && someFunction();

console.log(result); // `someFunction()` n'est pas appelée si `isTrue` est false

```

Dans cet exemple, `someFunction()` n'est appelée que si `isTrue` est vrai, montrant l'efficacité de l'évaluation en court-circuit.

### Exemple 2 : Court-circuit avec l'opérateur `||`

```javascript
let isLoggedIn = false;
let username = isLoggedIn || "Invité";

console.log("Bienvenue, " + username); // Si non connecté, le nom d'utilisateur par défaut est "Invité"

```

Ici, `username` se voit attribuer la valeur par défaut "Invité" uniquement si l'utilisateur n'est pas connecté, grâce à l'évaluation en court-circuit.

## Valeurs Truthy et Falsy

En JavaScript, les opérateurs logiques peuvent être utilisés avec des valeurs non booléennes. Comprendre les valeurs truthy et falsy est crucial dans de tels scénarios.

### Aperçu des valeurs Truthy et Falsy

Chaque valeur en JavaScript a une vérité ou une fausseté inhérente. Les valeurs falsy incluent `false`, `0`, `null`, `undefined`, `NaN` et une chaîne vide (`""`). Les valeurs truthy englobent toutes les valeurs qui ne sont pas explicitement falsy.

### Exemple : Valeurs Truthy et Falsy

```javascript
let userRole = ""; // Une chaîne vide est falsy

let roleMessage = userRole || "Utilisateur";

console.log("Vous êtes un " + roleMessage); // Si `userRole` est falsy, par défaut "Utilisateur"

```

Ici, la valeur par défaut "Utilisateur" est attribuée à `roleMessage` uniquement si `userRole` est falsy.

## Tableau récapitulatif

Fournissons un guide de référence rapide pour les différents opérateurs logiques :

<table>
<thead>
<tr>
<th>Opérateur</th>
<th>Symbole</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>ET</td>
<td><code>&amp;&amp;</code></td>
<td>Retourne vrai si toutes les conditions sont vraies.</td>
</tr>
<tr>
<td>OU</td>
<td><code>||</code></td>
<td>Retourne vrai si au moins une condition est vraie.</td>
</tr>
<tr>
<td>NON</td>
<td><code>!</code></td>
<td>Inverse le résultat d'une expression logique.</td>
</tr>
</tbody>
</table>

## Applications pratiques

Les opérateurs logiques jouent un rôle crucial dans les applications JavaScript du monde réel. Voici quelques exemples pratiques :

### Validation de formulaire

```javascript
let username = "JohnDoe";
let password = "secretp@ss";

if (username && password) {
  console.log("Formulaire soumis avec succès.");
} else {
  console.log("Veuillez entrer à la fois le nom d'utilisateur et le mot de passe.");
}

```

Dans ce scénario, la soumission du formulaire est validée en s'assurant que le nom d'utilisateur et le mot de passe sont fournis.

### Interface utilisateur réactive

```javascript
let screenWidth = 800;

if (screenWidth > 600 && screenWidth <= 1024) {
  console.log("Affichage d'une mise en page adaptée aux tablettes.");
} else if (screenWidth > 1024) {
  console.log("Affichage d'une mise en page de bureau.");
} else {
  console.log("Affichage d'une mise en page adaptée aux mobiles.");
}

```

Les opérateurs logiques sont souvent utilisés pour déterminer la mise en page en fonction de la largeur de l'écran, créant une interface utilisateur réactive.

### Contrôle d'accès

```javascript
let userRole = "admin";
let isLoggedIn = true;

if (userRole === "admin" && isLoggedIn) {
  console.log("Accès accordé au tableau de bord administrateur.");
} else {
  console.log("Accès refusé.");
}

```

Les opérateurs logiques aident à contrôler l'accès en vérifiant à la fois le rôle de l'utilisateur et l'état de connexion.

## Conclusion

Maîtriser les opérateurs logiques est essentiel pour écrire un code JavaScript efficace et significatif. Que vous créiez des conditions, preniez des décisions ou contrôliez le flux du programme, les opérateurs logiques sont des outils essentiels.

En explorant ces concepts à travers de nombreux exemples, vous êtes bien équipé pour les appliquer dans vos projets. De plus, comprendre les valeurs truthy et falsy améliore votre capacité à travailler avec des contextes non booléens.

Utilisez ce guide comme base pour écrire un JavaScript clair et concis, et vous serez sur la bonne voie pour construire des applications web robustes et réactives. Bon codage !