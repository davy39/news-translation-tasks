---
title: Comment comparer deux dates en JavaScript – Techniques, Méthodes et Bonnes
  Pratiques
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2024-02-12T17:57:17.000Z'
originalURL: https://freecodecamp.org/news/compare-two-dates-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Python-Data-Types--2-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment comparer deux dates en JavaScript – Techniques, Méthodes et Bonnes
  Pratiques
seo_desc: "In JavaScript, you can use the date object to work effectively with dates,\
  \ times, and time zones within an application. \nDate objects help you efficiently\
  \ manipulate data, handle various date-related tasks, and perform some calculations\
  \ when creating..."
---

En JavaScript, vous pouvez utiliser l'objet date pour travailler efficacement avec les dates, les heures et les fuseaux horaires au sein d'une application. 

Les objets date vous aident à manipuler efficacement les données, à gérer diverses tâches liées aux dates et à effectuer certains calculs lors de la création d'applications réelles.

Dans cet article, nous allons apprendre les sujets suivants :

* [Aperçu de la comparaison de dates](#heading-apercu-de-la-comparaison-de-dates)
* [Importance de la comparaison de dates en JavaScript](#heading-importance-de-la-comparaison-de-dates-en-javascript)
* [Objets Date en JavaScript](#heading-objets-date-en-javascript)
* [Comment créer des objets Date](#how-to-create-date-objects)
* [Bases de la comparaison de dates](#heading-bases-de-la-comparaison-de-dates)
* [Comment comparer des dates avec les opérateurs de comparaison](#heading-comment-comparer-des-dates-avec-les-operateurs-de-comparaison)
* [Comment comparer des dates avec la](#heading-comment-comparer-des-dates-avec-la-methode-gettime) [méthode `getTime()`](#comparing-dates-with-gettime-method)
* [Comment utiliser la méthode `valueOf()`](#heading-comment-utiliser-la-methode-valueof)
* [Comment utiliser la méthode `toISOString()`](#heading-comment-utiliser-la-methode-toisostring)
* [Défis de la comparaison de dates en JavaScript](#heading-defis-de-la-comparaison-de-dates-en-javascript)
* [Conclusion](#heading-conclusion)

## Aperçu de la comparaison de dates

En JavaScript, la comparaison de dates implique l'évaluation de deux dates pour déterminer si une date est antérieure, postérieure ou identique à l'autre. 

Il existe diverses façons de comparer des dates, qui incluent (mais ne sont pas limitées à) les opérateurs de comparaison (`<`, `>`, `<=`, `>=`) et des méthodes telles que `getTime()` et `valueOf()`. 

## Importance de la comparaison de dates en JavaScript

La comparaison de dates en JavaScript est importante pour le traitement et l'organisation des données liées au temps, et les fonctionnalités sensibles au temps dans les applications web. Elle est cruciale dans les applications pour traiter le filtrage des données, la planification et la gestion des événements basés sur le temps. 

En JavaScript, la compréhension des techniques de comparaison de dates vous permet de construire des applications robustes et fluides qui peuvent résister à divers scénarios liés au temps.

Pour commencer, voici quelques raisons pour lesquelles la comparaison de dates est un concept clé à connaître en JavaScript :

* **Filtrage des données** : La comparaison de dates est cruciale dans les applications où les données sensibles au temps comme les enregistrements de transactions et les journaux, le filtrage et la récupération d'informations sont des parties intégrantes de l'application.
* **Planification d'événements** : Il est facile de déterminer le statut d'un événement avec la comparaison de dates. Cela aide à organiser les événements, les rappels et les tâches.
* **Arithmétique** : En JavaScript, la comparaison de dates facilite l'arithmétique simple, telle que l'ajout et la soustraction d'intervalles de temps, la réalisation de manipulations de dates et le calcul de la durée entre deux dates.
* **Logique conditionnelle** : Avec la comparaison de dates, vous pouvez utiliser la logique conditionnelle basée sur des conditions liées au temps pour déclencher une action si un certain événement approche.
* **Expérience utilisateur** : La comparaison de dates améliore la fiabilité d'une application en garantissant que les fonctionnalités liées au temps fonctionnent parfaitement.

## Objets Date en JavaScript

En JavaScript, les objets date sont un concept très important à connaître. Vous les utilisez pour travailler avec les heures et les dates et fournir des moyens de manipuler, formater et représenter les dates et les heures dans de nombreux formats.

### Comment créer un objet Date

Il existe plusieurs méthodes pour créer un objet date en JavaScript. Voici quelques-unes des façons :

#### Utilisation du mot-clé `new`

```javascript
let currentDate = new Date();
console.log(currentDate)


//SORTIE.. Tue Feb 06 2024 00:28:59 GMT-0800 (Heure normale du Pacifique)
```

Dans le code ci-dessus, le constructeur Date a été appelé sans passer de paramètre. Cela signifie qu'il retourne un objet date avec la date et l'heure actuelles comme valeurs.

#### Utilisation de `Date` (`dateString`)

```javascript
let current = new Date("6 février 2025 10:25:00");

console.log(current);


// SORTIE .. Thu Feb 06 2025 10:25:00 GMT-0800 (Heure normale du Pacifique)
```

Dans le code ci-dessus, le constructeur `Date` a été appelé en passant une date et une heure spécifiques comme paramètre pour créer un objet date personnalisé. Le point clé à noter ici est que les paramètres sont au format chaîne.

#### Utilisation de l'année, du mois, du jour, des heures, des minutes, des secondes et des millisecondes

```javascript
let current = new Date(2024, 1, 6, 12, 0, 0, 0);

console.log(current);

// SORTIE... Tue Feb 06 2024 12:00:00 GMT-0800 (Heure normale du Pacifique)
```

Dans le code ci-dessus, un constructeur `Date` avec **année, mois, jour, heures, minutes, secondes et millisecondes** a été appelé pour créer un objet personnalisé avec une heure et une date spécifiques.

#### Dates avec timestamps

```javascript
const timestamp = new Date(14852959902)
console.log(timestamp)

// SORTIE ... Sun Jun 21 1970 14:49:19 GMT-0700 (Heure avancée du Pacifique)
```

Bien que la création d'une date avec un timestamp soit la moins populaire, c'est toujours l'une des méthodes de création d'une date.

Un timestamp est le nombre total de millisecondes écoulées depuis le 1er janvier 1970. 

## Bases de la comparaison de dates

En JavaScript, vous pouvez comparer des dates en utilisant différentes méthodes, comme les opérateurs de comparaison et les méthodes intégrées `Date`.

### Comment comparer des dates avec les opérateurs de comparaison

En JavaScript, vous pouvez utiliser des opérateurs de comparaison comme `<`, `>`, `<=`, `>=`, et `!=` pour comparer des dates. JavaScript convertit internement les dates (millisecondes depuis le 1er janvier 1970) en leurs timestamps correspondants.

Le code ci-dessous montre une comparaison de dates en utilisant les opérateurs de comparaison :

```javascript
// Créer deux objets date

const firstDate = new Date('2024-01-07')
const secondDate = new Date('2023-11-09')

// Rechercher une comparaison parmi les deux en utilisant les opérateurs de comparaison

console.log(firstDate < secondDate) // false (firstDate est postérieure à secondDate)
console.log(firstDate > secondDate) // true (firstDate est antérieure à secondDate)
console.log(firstDate >= secondDate) // false (firstDate est antérieure ou égale à secondDate)
console.log(firstDate <= secondDate) // true (firstDate est postérieure ou égale à secondDate)
console.log(firstDate == secondDate) // false (firstDate n'est pas égale à secondDate)
console.log(firstDate != secondDate) // true (firstDate n'est pas égale à secondDate)
```

La sortie du code montre que `firstDate` est postérieure à `secondDate` dans la première comparaison. Dans le contexte des dates, entre deux dates, `postérieure` est la date qui se produit après une autre dans le temps. 

La deuxième comparaison montre que `firstDate` est antérieure à `secondDate`. Dans le contexte des dates, entre deux dates, `antérieure` fait référence à la date qui vient en premier dans le temps.

La sortie pour la troisième comparaison montre que `firstDate` est antérieure ou égale à `secondDate`.

La sortie du code pour la troisième comparaison montre que `firstDate` est postérieure ou égale à `secondDate`.

La cinquième comparaison montre que `firstDate` n'est pas égale à `secondDate`.

Et la dernière comparaison a affiché que `firstDate` n'est pas égale à `secondDate`.

Il est important de noter que les opérateurs de comparaison en JavaScript sont basés sur le Temps Universel Coordonné (UTC).

Si vous souhaitez comparer des dates en fonction de leurs valeurs de date et d'heure réelles (y compris l'année, le mois, le jour, les heures, les minutes, les secondes et les millisecondes), vous devrez peut-être extraire ces composants et les comparer individuellement.

Le code ci-dessous montre comment comparer deux dates en fonction de leurs composants respectifs.

```javascript
const firstDate = new Date('2024-02-05');
const secondDate = new Date('2024-02-05');

// Extraire les composants année, mois et jour des deux dates

const firstYear = firstDate.getFullYear();
const firstMonth = firstDate.getMonth();
const firstDay = firstDate.getDate();
const secondYear = secondDate.getFullYear();
const secondMonth = secondDate.getMonth();
const secondDay = secondDate.getDate();

// Comparer les deux composants de date

let result;
switch (true) {
  case firstYear === secondYear && firstMonth === secondMonth && firstDay === secondDay:
    result = "Les dates sont égales.";
    break;
  case firstYear < secondYear || (firstYear === secondYear && firstMonth < secondMonth) || (firstYear === secondYear && firstMonth === secondMonth && firstDay < secondDay):
    result = "firstDate est antérieure à secondDate.";
    break;
  default:
    result = "firstdate est postérieure à secondDate.";
}
console.log(result);

```

La décomposition du code ci-dessus est la suivante :

* Création d'objets Date : Deux objets `firstDate` et `secondDate` initialisés avec la même date ont été créés.
* Avec les méthodes `getFullYear()`, `getMonth()`, et `getDate()`, le code extrait les composants année, mois et jour de chaque date.
* Comparaison entre les composants des dates en utilisant l'instruction switch case. Le code a été évalué en fonction de la valeur `true` `boolean`, chaque cas vérifiant diverses conditions pour déterminer la relation entre les deux dates.
* Le résultat est enregistré dans la console.

En résumé, pour déterminer si deux objets date sont égaux en fonction de leurs valeurs comme l'année, le mois et le jour, le code les compare en utilisant une instruction switch case pour gérer les multiples scénarios de comparaison. 

### Comment comparer des dates avec la méthode `getTime()`

La méthode `getTime()` est utile pour comparer des dates à la milliseconde. Il est important de se rappeler que `getTime()` effectue une comparaison numérique entre les dates et retourne la valeur temporelle depuis le 1er janvier 1970.

```javascript
// Créer deux objets Date
const firstDate = new Date('2025-01-01');
const secondDate = new Date('2024-01-02');

// Obtenir le temps en millisecondes pour chaque date
const firstTime = firstDate.getTime();
const secondTime = secondDate.getTime();

// Comparer les valeurs temporelles
if (firstTime < secondTime) {
  console.log('firstDate est antérieure à secondDate');
} else if (firstTime > secondTime) {
  console.log('firstDate est postérieure à secondDate');
} else {
  console.log('firstDate et secondDate sont égales');
}

//SORTIE....firstDate est postérieure à secondDate

```

Dans le code ci-dessus :

* Les deux objets date sont `firstDate` et `secondDate`, représentant tous deux des dates différentes.
* La méthode `getTime()` a été utilisée pour obtenir le temps des deux éléments en millisecondes.
* Les opérateurs de comparaison standard (`<`, `>`, `===`) ont été utilisés pour déterminer leur relation.
* La sortie du code ci-dessus était `firstDate` est postérieure à `secondDate`, car `secondDate` précède `firstDate`.

### Comment utiliser la méthode `valueOf()`

En JavaScript, la méthode `valueOf()` est automatiquement appelée en arrière-plan pour retourner la valeur primitive de l'objet spécifié.

```javascript
const word = new String("Bonjour !");
console.log(word); // Sortie: [String: 'Bonjour!']
console.log(str.valueOf()); // Sortie: 'Bonjour!'

var number = new Number(10);
console.log(number); // Sortie: [Number: 10]
console.log(num.valueOf()); // Sortie: 10

```

Dans l'exemple ci-dessus, la méthode `valueOf()` des objets string et number retourne les valeurs string et number qu'ils représentent.

La méthode `valueOf()`, cependant, retourne un timestamp (millisecondes depuis l'époque Unix), ce qui facilite la comparaison des dates.

```javascript
const date = new Date();
const date1 = new Date();

if (date.valueOf() < date1.valueOf()) {
  console.log('date est antérieure à date1')
} else if (date.valueOf() > date1.valueOf()) {
  console.log('date est postérieure à date1')
} else {
  console.log('date et date1 sont identiques')
}

// SORTIE ... date et date1 sont identiques
```

La sortie montre que les deux objets date sont identiques.

### Comment utiliser la méthode `toISOString()`

En JavaScript, la méthode `toISOString()` est utilisée pour convertir un objet `Date` en une représentation de chaîne au format ISO 8601 étendu simplifié, qui est toujours de 24 à 27 caractères de long. Les caractères sont `YYYY-MM-DDTHH:mm:ss.sssZ` ou `1YYYYYY-MM-DDTHH:mm:ss.sssZ`, respectivement.

La méthode fournit un moyen standardisé de représenter les dates sous forme de chaînes lorsque vous l'utilisez pour manipuler ou comparer des dates. La conversion de deux dates en chaînes ISO via `toISOString()` est bénéfique, car elle rend la comparaison fluide en garantissant que les deux dates sont au même format.

Vous pouvez utiliser les opérateurs de comparaison de chaînes standard comme `===`, `<`, `>` pour comparer les chaînes ISO.

```javascript
// Créer deux objets Date
const firstDate = new Date('2024-02-06T12:00:00');
const secondDate = new Date('2024-02-07T12:00:00');

// Convertir les dates en chaînes ISO
const firstISODate = firstDate.toISOString();
const secondISODate = secondDate.toISOString();


// Comparer les deux chaînes ISO
if (firstISODate === secondISODate) {
  console.log("Les dates sont égales.");
} else if (firstISODate < secondISODate) {
  console.log("firstDate est avant secondDate.");
} else {
  console.log("firstDate est après secondDate.");
}
// SORTIE ....firstDate est avant secondDate.
```

Le code ci-dessus montre que les dates ont été converties en chaînes ISO et compare directement les deux chaînes pour déterminer leur statut relatif. Cela garantit la facilité de comparaison et la cohérence.

## Défis de la comparaison de dates en JavaScript

Être conscient des problèmes possibles et de leurs solutions peut vous aider à garantir la précision et la cohérence lors de la comparaison de dates en JavaScript.

Certains des problèmes connus sont listés ci-dessous :

### Opérateurs de comparaison

Les valeurs numériques `getTime()` doivent être les seules métriques de comparaison lors de l'utilisation des opérateurs de comparaison. La méthode ne gère pas intrinsèquement les conversions de fuseau horaire, ce qui signifie que vous devez vous assurer que les heures sont normalisées à un fuseau horaire commun avant d'utiliser `getTime()`.

En JavaScript, l'objet `date` vous permet de créer des dates invalides (comme le 30 février). Vous devez utiliser `getTime()` pour éviter un comportement inattendu après avoir validé les dates.

**Comment résoudre le problème :**

* **Valider les dates** : La validation des dates doit être la première étape pour garantir que les dates sont valides avant d'effectuer toute comparaison.
* **Normaliser les fuseaux horaires** : Avant d'utiliser la méthode `getTime()`, vous devez vous assurer que les dates sont normalisées à un fuseau horaire commun.
* **Besoins de précision** : Confirmez si la précision de `getUTCFullYear()`, `getUTCMonth()`, et `getUTCDate()` sera nécessaire pour votre exigence de comparaison. Sinon, utilisez la méthode `getTime()`.

```javascript
const firstDate = new Date('2024-02-01');
const secondDate = new Date('2024-02-03');

if (firstDate.getTime() < secondDate.getTime()) {
  // firstDate est antérieure à secondDATE
}

```

### Différence de fuseau horaire

Assurez-vous de comparer les dates dans le même fuseau horaire ou avec UTC et non le fuseau horaire local de l'utilisateur. L'utilisation des fuseaux horaires locaux peut entraîner des divergences lors de la comparaison de dates dans différents fuseaux horaires ou lors de la manipulation de dates provenant de différentes sources.

Dans certains fuseaux horaires, le mode d'heure d'été peut être le format horaire adopté. Dans ce cas, l'heure locale peut être ajustée en avant ou en arrière. Cet ajustement peut affecter la durée entre deux dates et provoquer des résultats inattendus.

**Comment résoudre le problème :**

* Normaliser le fuseau horaire : convertir toutes les dates à un fuseau horaire standard, c'est-à-dire UTC (Temps Universel Coordonné), avant la comparaison. Cela garantit la cohérence.
* Communication : Assurez-vous que les informations de fuseau horaire sont communiquées et standardisées lors de la manipulation de dates obtenues à partir de plusieurs sources. Cela aide à garantir une interprétation cohérente des dates.

```javascript
const firstDate = new Date('2024-02-02T12:00:00Z'); // Date UTC
const secondDate = new Date(); // Date locale actuelle

// Comparer les dates en UTC pour éviter les problèmes de fuseau horaire
if (firstDate.toISOString() === secondDate.toISOString()) {
  // Les dates sont égales
}

```

### Précision

En JavaScript, le temps est représenté en millisecondes depuis l'époque Unix (1er janvier 1970). Cela est crucial lors de la comparaison d'une date qui a une heure associée, car vous pouvez rencontrer des problèmes de précision.

**Comment résoudre le problème :**

* **Contrôle de qualité** : Des inspections régulières, des tests et une validation des systèmes et procédures de mesure peuvent aider à corriger les erreurs dans le processus de mesure.
* **Calibration** : La calibration régulière des instruments et équipements aide à maintenir la précision et l'exactitude des mesures. La calibration implique la comparaison des mesures prises par un appareil avec des normes connues pour garantir la précision et la fiabilité.

```javascript
const firstDate = new Date('2023-02-06');
const secondDate = new Date('2022-02-06');

// Cela peut ne pas toujours être vrai en raison des informations de temps
if (firstDate === secondDate) {
  // Les dates ne sont pas nécessairement égales
}

```

## Conclusion

Dans ce tutoriel, vous avez appris la comparaison de dates et pourquoi il est important de comprendre comment le faire en JavaScript. Nous avons parlé des objets date et de la façon d'en créer un, ainsi que des bases de la comparaison de dates et des méthodes de comparaison de dates.

Nous avons également examiné certains des problèmes susceptibles d'être rencontrés lors de la comparaison de dates en JavaScript.

Bonne lecture !