---
title: Comment la proposition Temporal de JavaScript va changer les fonctions Date/Heure
subtitle: ''
author: Jesse Hall
co_authors: []
series: null
date: '2024-11-13T20:27:43.514Z'
originalURL: https://freecodecamp.org/news/how-javascripts-temporal-proposal-will-change-datetime-functions
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/mRGtYItJRnA/upload/62e08fa08517011b9a4f54e9002b76ca.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: datetime
  slug: datetime
- name: Node.js
  slug: nodejs
seo_title: Comment la proposition Temporal de JavaScript va changer les fonctions
  Date/Heure
seo_desc: 'JavaScript''s handling of dates and times has long frustrated developers.
  The built-in Date object, created in JavaScript’s early days, has numerous limitations
  and quirks that complicate working with dates and times.

  Fortunately for us, the Temporal ...'
---

La gestion des dates et des heures en JavaScript a longtemps frustré les développeurs. L'objet `Date` intégré, créé aux débuts de JavaScript, présente de nombreuses limitations et particularités qui compliquent le travail avec les dates et les heures.

Heureusement pour nous, la [proposition Temporal](https://github.com/tc39/proposal-temporal) vise à résoudre ces problèmes en fournissant une API moderne et plus intuitive pour la manipulation des dates et des heures.

Dans cet article, nous allons passer en revue certains des défis liés à l'utilisation de `date`, ce qu'est l'API Temporal et comment elle fonctionnera, et ce que vous pouvez utiliser en attendant que Temporal soit prêt pour une utilisation en production.

## Problèmes actuels avec `Date` en JavaScript

### 1. API mutable

L'objet `Date` est mutable, ce qui peut entraîner des bugs et des comportements inattendus :

```javascript
// Le comportement actuel de Date est mutable
const date = new Date('January 1, 2024');
date.setMonth(1); // Modifie l'objet date original
console.log(date); // February 1, 2024

// Cette mutabilité peut entraîner des bugs lors du passage de dates entre fonctions
function processDate(date) {
  date.setDate(date.getDate() + 1); // Modifie la date originale !
  return date;
}
```

### 2. Numérotation des mois confuse

Les mois dans `Date` sont indexés à partir de zéro (0-11), tandis que les jours sont indexés à partir de un (1-31) :

```javascript
// Numérotation des mois confuse
const date = new Date(2024, 0, 1); // 1 janvier 2024
console.log(date.getMonth()); // 0 (janvier)
```

### 3. Support limité des fuseaux horaires

L'objet `Date` a un support limité pour les fuseaux horaires et dépend fortement du fuseau horaire local du système :

```javascript
// La gestion des fuseaux horaires dépend du système
const date = new Date('2024-01-01T00:00:00Z');
console.log(date.toString()); // Affichera différents résultats selon le fuseau horaire du système
```

## Qu'est-ce que l'API Temporal ?

Temporal est une nouvelle API JavaScript proposée qui offre une solution moderne pour travailler avec les dates, les heures et les timestamps. Elle est actuellement une proposition de stade 3, ce qui signifie qu'elle est dans les dernières étapes de développement mais pas encore prête pour une utilisation en production.

Concepts clés de Temporal :

1. **Immuable par défaut** : Tous les objets Temporal sont immuables

2. **Séparation claire des préoccupations** : Différents objets pour différents cas d'utilisation

3. **Gestion explicite des fuseaux horaires** : Meilleur support pour travailler avec les fuseaux horaires

4. **Indexation cohérente** : Toutes les unités utilisent une numérotation basée sur 1

## Fonctionnalités clés de Temporal

### 1. Différents types pour différents besoins

```javascript
// PlainDate pour travailler avec des dates de calendrier
const date = Temporal.PlainDate.from('2024-01-01');

// PlainTime pour travailler avec l'heure de l'horloge
const time = Temporal.PlainTime.from('09:00:00');

// ZonedDateTime pour travailler avec des fuseaux horaires spécifiques
const zonedDateTime = Temporal.ZonedDateTime.from('2024-01-01T09:00:00[America/New_York]');
```

Dans cet exemple, Temporal fournit différents types d'objets pour différents cas d'utilisation :

* `PlainDate` est utilisé lorsque vous ne vous souciez que des dates de calendrier sans information d'heure ou de fuseau horaire. Parfait pour les anniversaires, les jours fériés, etc.

* `PlainTime` gère l'heure indépendamment de toute date ou fuseau horaire. Utile pour les événements récurrents comme "réunion quotidienne à 9h".

* `ZonedDateTime` combine les informations de date, d'heure et de fuseau horaire pour une gestion complète des timestamps. Idéal pour planifier des réunions à travers les fuseaux horaires.

Chaque type est conçu pour un usage spécifique et est immuable, empêchant les modifications accidentelles. Cette séparation claire aide les développeurs à choisir le bon outil pour leurs besoins spécifiques, contrairement à l'objet `Date` universel qui essaie de tout gérer et conduit souvent à des confusions.

### 2. Opérations immuables

```javascript
// Toutes les opérations retournent de nouveaux objets au lieu de modifier l'original
const date = Temporal.PlainDate.from('2024-01-01');
const nextMonth = date.add({ months: 1 }); 
console.log(date.toString()); // '2024-01-01' - original inchangé
console.log(nextMonth.toString()); // '2024-02-01' - nouvel objet
```

Cet exemple démontre comment la conception immuable de Temporal empêche les mutations accidentelles et rend les calculs de dates plus prévisibles.

Avec l'API `Date` actuelle, des méthodes comme `setMonth()` modifient l'objet original, ce qui peut entraîner des bugs lorsque cet objet est utilisé à plusieurs endroits. En revanche, les méthodes de Temporal retournent toujours de nouveaux objets, laissant l'original intact.

### 3. Meilleur support des fuseaux horaires

```javascript
// Gestion explicite des fuseaux horaires
const nyDateTime = Temporal.ZonedDateTime.from({
  timeZone: 'America/New_York',
  year: 2024,
  month: 1,
  day: 1,
  hour: 9
});

const tokyoDateTime = nyDateTime.withTimeZone('Asia/Tokyo');
console.log(tokyoDateTime.toString()); // '2024-01-01T23:00:00+09:00[Asia/Tokyo]'
```

Contrairement à l'API `Date` actuelle, qui conduit souvent à des confusions avec des conversions de fuseaux horaires implicites, Temporal rend les opérations de fuseaux horaires explicites et simples :

1. Nous créons un objet `ZonedDateTime` spécifiquement pour le fuseau horaire de New York, avec tous les composants (année, mois, jour, heure) clairement spécifiés. Cette création explicite empêche toute ambiguïté sur le fuseau horaire avec lequel nous travaillons.

2. En utilisant `withTimeZone()`, nous pouvons facilement convertir les heures entre les fuseaux horaires sans calculs complexes. La conversion de l'heure de New York à celle de Tokyo est gérée automatiquement.

3. La chaîne de caractères résultante inclut le décalage horaire complet (`+09:00`) et le nom du fuseau horaire (`[Asia/Tokyo]`), fournissant une clarté complète sur l'heure représentée.

Cette approche résout de nombreux problèmes courants liés aux fuseaux horaires auxquels les développeurs sont confrontés aujourd'hui, tels que les transitions d'heure d'été, les calculs de décalage horaire et l'ambiguïté des heures locales par rapport aux heures UTC. Elle est particulièrement précieuse pour les applications qui doivent gérer la planification mondiale, la coordination d'événements à travers les fuseaux horaires, ou tout scénario où une gestion précise des fuseaux horaires est cruciale.

## Comparaison de Date, Intl et Temporal

### Approche actuelle avec `Date` et `Intl` :

```javascript
// Approche actuelle utilisant Date et Intl
const date = new Date('2024-01-01T09:00:00Z');
const formatter = new Intl.DateTimeFormat('en-US', {
  timeZone: 'America/New_York',
  dateStyle: 'full',
  timeStyle: 'long'
});

console.log(formatter.format(date)); // 'Monday, January 1, 2024 at 4:00:00 AM EST'
```

Avec l'approche actuelle, nous créons un timestamp UTC en utilisant `Date`, avons besoin d'un objet `Intl.DateTimeFormat` séparé pour le formatage, gérons la conversion de fuseau horaire implicitement pendant le formatage, et avons moins de contrôle sur le format exact de la sortie. Le résultat montre 4:00 AM EST parce que nous avons créé la date à 09:00 UTC et lorsqu'elle est formatée dans le fuseau horaire de New York. Cette conversion implicite peut être confuse et source d'erreurs.

### Approche future avec Temporal :

```javascript
// Approche future utilisant Temporal
const datetime = Temporal.ZonedDateTime.from('2024-01-01T09:00:00[America/New_York]');
console.log(datetime.toLocaleString('en-US', {
  weekday: 'long',
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  hour: 'numeric',
  minute: '2-digit',
  second: '2-digit',
  timeZoneName: 'short'
})); // 'Monday, January 1, 2024 at 9:00:00 AM EST'
```

Avec Temporal, nous créons un `ZonedDateTime` avec un fuseau horaire explicite, et les options de formatage sont directement intégrées dans l'API. L'heure (9:00 AM) est exactement celle que nous avons spécifiée pour New York, sans conversions implicites. Cela rend le comportement du code plus prévisible et plus facile à comprendre.

L'arithmétique devient également plus intuitive avec cette approche.

```javascript
const nextWeek = datetime.add({ weeks: 1 });
const duration = datetime.until(nextWeek);
console.log(nextWeek.toPlainDate().toString()); // '2024-01-08'
console.log(duration.toString()); // 'PT168H'
```

Dans cet exemple, nous pouvons voir plusieurs avantages clés de l'approche de Temporal :

1. **Gestion explicite des fuseaux horaires** : En créant un `ZonedDateTime` avec `[America/New_York]`, nous indiquons explicitement avec quel fuseau horaire nous travaillons. Il n'y a pas d'ambiguïté sur le fait que l'heure soit UTC, locale ou dans un autre fuseau horaire.

2. **Formatage intégré** : La méthode `toLocaleString()` fournit un moyen propre et unifié de formater les dates sans avoir besoin d'un objet formateur séparé. Toutes les options de formatage sont similaires à celles que vous utiliseriez avec Intl.DateTimeFormat, maintenant la familiarité tout en simplifiant l'API.

3. **Arithmétique intuitive** : Les méthodes `add()` et `until()` démontrent comment Temporal rend les calculs de date/heure plus simples :

   * `add({ weeks: 1 })` montre clairement que nous ajoutons une semaine

   * `until()` retourne un objet de durée propre qui peut être facilement compris et manipulé

   * La durée résultante de 'PT168H' représente une période de temps (P) avec 168 heures (T168H), suivant le format de durée ISO 8601

4. **Sécurité des types** : En ayant des types distincts comme `ZonedDateTime` et `PlainDate`, Temporal aide à prévenir les erreurs courantes. La méthode `toPlainDate()` convertit explicitement en une représentation de date uniquement lorsque nous n'avons pas besoin d'informations sur l'heure.

Cette approche élimine de nombreux pièges et comportements implicites qui rendent l'API `Date` actuelle problématique, tout en fournissant un moyen plus puissant et flexible de travailler avec les dates et les heures.

## État actuel et alternatives

### État actuel

* Temporal est actuellement au stade 3 du processus TC39

* Il n'est pas encore prêt pour une utilisation en production

* La prise en charge native par les navigateurs n'est pas encore disponible

### Alternatives recommandées

Jusqu'à ce que Temporal soit largement disponible, envisagez d'utiliser des bibliothèques établies :

1. [**Day.js**](https://day.js.org/)

   * Léger

   * Bon support des navigateurs

   * Bon support TypeScript

   * Extensible avec des plugins

   * Dispose d'une grande communauté et d'un développement actif

```javascript
// Utilisation de Day.js comme alternative
import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import timezone from 'dayjs/plugin/timezone';

dayjs.extend(utc);
dayjs.extend(timezone);

const date = dayjs('2024-01-01').tz('America/New_York');
const nextWeek = date.add(1, 'week');
```

Pour une plongée plus profonde dans Day.js, consultez cet article : [**JavaScript Dates – How to Use the DayJS Library to work with Date and Time in JS**](https://www.freecodecamp.org/news/javascript-date-time-dayjs/)

2. [**date-fns**](https://date-fns.org/)

   * Approche de programmation fonctionnelle

   * Tree-shakeable

   * Bon support TypeScript

3. [**Luxon**](https://moment.github.io/luxon/)

   * Fonctionnalités similaires à Temporal

   * Immuable par défaut

   * Support natif des fuseaux horaires et Intl

### Pourquoi attendre Temporal ?

Bien que ces bibliothèques soient de bonnes alternatives, Temporal offrira plusieurs avantages :

1. Support natif des navigateurs (pas de taille de bundle supplémentaire)

2. API standardisée dans tous les environnements JavaScript

3. Meilleure performance en tant qu'implémentation native

4. Comportement cohérent sur toutes les plateformes

Jusqu'à ce que Temporal atteigne le stade 4 et dispose d'un support généralisé par les navigateurs, je recommande d'utiliser soit les objets intégrés `Date` et `Intl`, soit l'une des bibliothèques établies mentionnées ci-dessus pour les applications de production. Mais préparez-vous et soyez prêt pour Temporal lorsqu'il sera prêt !

## Merci d'avoir lu !

Consultez mes autres contenus et faites-moi savoir comment je peux vous aider dans votre parcours pour devenir développeur web.

* [Abonnez-vous à ma chaîne YouTube](https://youtube.com/codeSTACKr)

* Réseaux sociaux : [Twitter](https://twitter.com/codeSTACKr) | [LinkedIn](https://www.linkedin.com/in/codeSTACKr/) | [Instagram](https://instagram.com/codeSTACKr)

* [Inscrivez-vous à ma newsletter](https://codestackr.com/)