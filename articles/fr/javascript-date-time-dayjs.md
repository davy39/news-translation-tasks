---
title: Dates JavaScript – Comment utiliser la bibliothèque DayJS pour travailler avec
  les dates et heures en JS
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2023-08-28T22:09:07.000Z'
originalURL: https://freecodecamp.org/news/javascript-date-time-dayjs
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/fcc_template--5-.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Dates JavaScript – Comment utiliser la bibliothèque DayJS pour travailler
  avec les dates et heures en JS
seo_desc: 'When it comes to handling dates and times in JavaScript, developers often
  find themselves grappling with the complexities of the built-in Date object.

  While vanilla JavaScript provides fundamental functionality, it can be quite cumbersome
  to work wit...'
---

Lorsque l'on traite les dates et heures en JavaScript, les développeurs se retrouvent souvent à lutter avec les complexités de l'objet `Date` intégré.

Bien que JavaScript natif offre une fonctionnalité fondamentale, il peut être assez fastidieux à utiliser, surtout lorsqu'il s'agit de parser, formater et manipuler des dates.

C'est là que des bibliothèques externes comme DayJS entrent en jeu, offrant une multitude d'avantages qui rendent le travail avec les dates et heures un jeu d'enfant.

Dans cet article, je vais vous présenter DayJS et comment cette petite bibliothèque peut grandement améliorer votre base de code et votre productivité.

Voici ce que nous allons couvrir :

* Comment installer la bibliothèque DayJS
* Comment travailler avec les dates et heures en JavaScript
* Comment vous pouvez utiliser la bibliothèque DayJS pour rendre ces fonctions plus faciles, plus concises et plus lisibles
* Comparaisons entre l'exécution de fonctionnalités en JavaScript natif et DayJS
* Fonctions utiles disponibles dans la bibliothèque DayJS

## Table des matières :

1. [Introduction rapide à l'objet Date en JavaScript](#heading-introduction-rapide-a-lobjet-date-en-javascript)
2. [Comment installer la bibliothèque DayJS](#heading-comment-installer-la-bibliotheque-dayjs)
3. [API DayJS et syntaxe de base](#heading-api-dayjs-et-syntaxe-de-base)
4. [Modularité dans DayJS](#heading-modularite-dans-dayjs)
5. [Mutabilité dans DayJS](#heading-mutabilite-dans-dayjs)
6. [Immuabilité et objets immuables dans DayJS](#heading-immuabilite-et-objets-immuables-dans-dayjs)
7. [Flexibilité de parsing](#heading-flexibilite-de-parsing)
8. [Comment ajouter ou soustraire à une date et heure](#heading-comment-ajouter-ou-soustraire-a-une-date-et-heure)
9. [Comment comparer des dates dans DayJS](#heading-comment-comparer-des-dates-dans-dayjs)
10. [Comment obtenir la différence entre deux dates](#heading-comment-obtenir-la-difference-entre-deux-dates)
11. [Comment obtenir le début ou la fin d'une période de temps](#heading-comment-obtenir-le-debut-ou-la-fin-dune-periode-de-temps)
12. [Comment combiner des fonctions dans DayJS](#heading-comment-combiner-des-fonctions-dans-dayjs)
13. [Conclusion](#heading-conclusion)


## Introduction rapide à l'objet Date en JavaScript

Vous pouvez utiliser l'objet `Date` en JavaScript pour travailler avec des dates et des périodes de temps. Mais parfois, travailler avec l'objet `Date` peut être fastidieux, et la date/heure peut être difficile à manipuler.

Regardons comment obtenir la date d'aujourd'hui en JavaScript :

```javascript
var date = new Date();
```

Assez facile, n'est-ce pas ? Cela nous donne une date ISO (c'est un format de date universel) qui s'affiche comme ceci :
`2023-07-16T14:51:47.557Z`

Ainsi, vous pouvez voir que dans `année-mois-date`, le `T` marque le point où la partie Heure de la Date commence. Ensuite, les chiffres suivants sont `heures:minutes:secondes.secondes fractionnaires`. Le `Z` à la fin signifie qu'il n'y a pas de fuseau horaire spécifié et qu'il doit utiliser le fuseau horaire UTC (il se prononce "Zulu").

Vous pouvez en lire plus sur ce format [ici](https://www.ionos.co.uk/digitalguide/websites/web-development/iso-8601/).

# La bibliothèque DayJS

Maintenant, je ne dis pas que les autres méthodes de travail avec les dates et heures sont fausses, mais en raison de leur complexité, pour moi, elles ne semblent tout simplement pas valoir la peine.

Lorsque je traite des dates et heures dans le code, je veux une solution facile à utiliser, prête à l'emploi, qui ajoute de la lisibilité à mon code et offre de la flexibilité.

C'est là que DayJS entre en jeu. C'est une alternative pour gérer les dates et heures en JavaScript, sous la forme d'une bibliothèque.

Cette bibliothèque, contrairement à d'autres, est extrêmement petite en taille. Par exemple, il existe une autre bibliothèque courante utilisée par certains développeurs appelée `MomentJs`, mais sa taille de fichier est très grande. Moment.js lui-même fait **280,9 ko**, et cela augmente à **467,6 ko** après l'inclusion de la bibliothèque de fuseaux horaires (vous permettant de définir des fuseaux horaires par défaut et de manipuler des dates basées sur des fuseaux horaires spécifiques).

Les grandes importations et fichiers de bibliothèque sont quelque chose que nous voulons vraiment éviter lors du développement pour le web et le mobile afin d'aider à augmenter les vitesses de chargement et les tailles de bundle.

DayJs arrive à un impressionnant **2 ko** – c'est une taille de fichier extrêmement petite, surtout si l'on considère ses capacités et fonctionnalités.

## Comment installer la bibliothèque DayJS

Afin de tirer le meilleur parti de ce tutoriel, je recommande vivement d'installer DayJS afin que vous puissiez suivre les exemples et les points abordés.

DayJS s'installe facilement via les gestionnaires de paquets yarn ou npm en utilisant les commandes suivantes

```cmd
// yarn
yarn add dayjs

//node
npm install dayjs
```

Pour utiliser DayJS dans votre fichier `.js`, importez-le simplement en utilisant la syntaxe d'importation régulière :

```javascript
import dayjs from 'dayjs'
```


## API DayJS et syntaxe de base

Travailler avec des dates et heures en JavaScript natif implique souvent plusieurs appels de méthodes et calculs. Cela rend le code trop verbeux et difficile à lire.

La bibliothèque DayJS résout ce problème en fournissant une API beaucoup plus intuitive et rationalisée, qui simplifie grandement la manipulation des dates et heures.

Considérez la tâche de formater une date dans un format spécifique, tel que "YYYY-MM-DD HH:mm:ss", (année-mois-date 24Heures:minutes:secondes).

Voici comment vous pourriez le faire en utilisant l'objet Date de JavaScript natif :

```javascript
const currentDate = new Date();
const formattedDate = `${currentDate.getFullYear()}-${(currentDate.getMonth() + 1).toString().padStart(2, '0')}-${currentDate.getDate().toString().padStart(2, '0')} ${currentDate.getHours().toString().padStart(2, '0')}:${currentDate.getMinutes().toString().padStart(2, '0')}:${currentDate.getSeconds().toString().padStart(2, '0')}`;

console.log(formattedDate); // Sortie 2023-08-23 17:02:33
```

Le code ci-dessus utilise les fonctions intégrées de `Date` pour rassembler diverses parties de l'objet date.

- `getFullYear()` – obtient l'année complète
- `getMonth()` – obtient la partie mois
- `getDate()` – obtient la partie date
- `getHours()` – obtient l'heure actuelle au format 24h
- `getMinutes()` – obtient la partie minutes
- `getSeconds()` – obtient la partie secondes

Il construit ensuite une variable de chaîne interpolée complexe contenant toutes les parties requises telles que nous nous attendons à les voir, c'est-à-dire avec des 0 initiaux pour les mois/jours/minutes/secondes à un seul chiffre, (ce que fait la fonction `padStart()`).

Comme vous pouvez le voir, cela est très illisible – et nous pourrions refactoriser cela pour le rendre plus lisible. Mais le concept reste valable.

Prenons l'exemple ci-dessous. Ici, nous créons une fonction `formatDate` qui prendra un objet `Date` JS et retournera une date formatée en utilisant le format `jour/mois/année` :

```javascript
const formatDate = (date) => {
  // Obtenir les composants individuels de la date
  var day = date.getDate(); // obtenir la partie Date
  var month = date.getMonth() + 1; // Obtenir le Mois (les Mois sont basés sur zéro)
  var year = date.getFullYear(); // Obtenir l'année
  var hours = date.getHours(); // Obtenir l'heure
  var minutes = date.getMinutes(); // Obtenir les minutes
  var seconds = date.getSeconds(); // Obtenir les secondes
```

Vous vous demandez peut-être pourquoi nous avons dû ajouter 1 au mois. Comme j'ai essayé de l'expliquer dans les commentaires, `getMonth()` est basé sur zéro. Cela signifie que janvier est égal à **0**, donc pour obtenir le numéro de mois correct, nous devons ajouter 1 à tous les mois. Cela signifie que maintenant janvier deviendrait **1**.

Ainsi, dans le code ci-dessus, nous avons obtenu les parties pertinentes de l'objet Date dont nous avons besoin (jour, mois, année). Maintenant, nous devons formater ces parties pour qu'elles correspondent à notre résultat attendu de 2 chiffres pour le jour et le mois.

```javascript
  // Remplir les chiffres uniques avec des zéros initiaux pour obtenir 2 chiffres
  var formattedDay = day < 10 ? "0" + day : day;
  var formattedMonth = month < 10 ? "0" + month : month;

  // Concaténer (joindre) les composants de date formatés
  return formattedDay + "/" + formattedMonth + "/" + year;
};

// Exemple d'utilisation
var currentDate = new Date();
var formatted = formatDate(currentDate);
console.log(formatted); // Sortie : "16/07/2023"
```

Ainsi, si nous devions tout mettre ensemble, nous obtiendrions le code suivant :

```
const formatDate = (date) => {
  // Obtenir les composants individuels de la date
  var day = date.getDate(); // obtenir la partie Date
  var month = date.getMonth() + 1; // Obtenir le Mois (les Mois sont basés sur zéro)
  var year = date.getFullYear(); // Obtenir l'année
  var hours = date.getHours(); // Obtenir l'heure
  var minutes = date.getMinutes(); // Obtenir les minutes
  var seconds = date.getSeconds(); // Obtenir les secondes
  
  // Remplir les chiffres uniques avec des zéros initiaux pour obtenir 2 chiffres
  var formattedDay = day < 10 ? "0" + day : day;
  var formattedMonth = month < 10 ? "0" + month : month;

  // Concaténer (joindre) les composants de date formatés
  return formattedDay + "/" + formattedMonth + "/" + year;
}

// Utilisation
var currentDate = new Date();
var formatted = formatDate(currentDate);
console.log(formatted); // Sortie : "16/07/2023"
```

Maintenant, c'est une combinaison de 19 lignes de code, 6 fonctions basées sur des objets et 1 fonction utilitaire – et c'est aussi très inflexible.

### Comment DayJS peut-il rendre cela plus facile ?

Voyons comment nous pourrions accomplir cela dans DayJS :

```javascript

const currentDate = dayjs();
const formattedDate = currentDate.format('YYYY-MM-DD HH:mm:ss');
console.log(formattedDate);

```

C'est tout ! En 3 lignes de code, nous avons récupéré la date et l'heure actuelles en utilisant la fonction `dayjs()`, nous l'avons formatée dans le format dateHeure fourni en utilisant un paramètre de chaîne, et nous avons enregistré la sortie.

Dans le code ci-dessus, nous utilisons la fonction utilitaire `dayjs.format()`. Cette fonction nous permet de passer notre format de date préféré, basé sur une syntaxe de format JS courante.

`YYYY` = année numérique
`MM` = mois numérique de l'année en 2 chiffres
`DD` = date numérique en 2 chiffres
`HH` = horloge 24 heures pour les heures
`mm` = minutes en 2 chiffres
`ss` = secondes en 2 chiffres

Tous séparés par des tirets et des deux-points.

Pour une liste de tous les formats possibles, consultez les options de format de la documentation DayJS [ici](https://day.js.org/docs/en/display/format#list-of-all-available-formats).

Je pense que nous pouvons tous convenir que 3 lignes de code lisible sont bien supérieures à 19 lignes de code compliqué.

# Modularité dans DayJS
La bibliothèque DayJS offre une conception modulaire qui permet aux développeurs d'inclure uniquement les fonctionnalités spécifiques dont ils ont besoin.

Cette modularité non seulement améliore la flexibilité de la bibliothèque, mais aide également à optimiser la taille de votre bundle d'application. Voici un aperçu de la manière dont DayJS réalise la modularité et ses implications pour la taille de l'application.

DayJS est conçu comme un ensemble de plugins individuels qui fournissent diverses fonctionnalités. Ces plugins peuvent être inclus ou exclus en fonction des exigences de votre projet.

Certains des plugins disponibles couvrent des fonctionnalités telles que la prise en charge des fuseaux horaires, les calculs de durée, le parsing personnalisé et des options de formatage plus avancées.

Cette structure modulaire garantit que vous ne chargez que les parties de la bibliothèque que vous allez réellement utiliser, évitant ainsi un gonflement inutile de votre application.

Voici un exemple simplifié de la manière dont vous pouvez tirer parti de la modularité dans DayJS :

```javascript

// Importer uniquement les fonctionnalités spécifiques de dayjs dont vous avez besoin
import dayjs from 'dayjs';
import timezone from 'dayjs/plugin/timezone';

// Appliquer le plugin requis
dayjs.extend(timezone);

// Vous avez maintenant une instance dayjs personnalisée avec uniquement les fonctionnalités nécessaires
const customDayjs = dayjs().tz('America/New_York');
```

Comme vous pouvez le voir dans les commentaires ci-dessus, nous importons simplement DayJS, ainsi que le module `timezone`. Nous créons ensuite un nouvel objet `dayjs()` et définissons le fuseau horaire sur New York, Amérique. Cela signifie que la date et l'heure seront la date/heure actuelle à New York, plutôt que le UTC par défaut de DayJS.

La modularité de la bibliothèque DayJS offre aux développeurs la flexibilité d'adapter leur gestion des dates et heures aux besoins spécifiques du projet. Cela non seulement garde votre base de code propre et ciblée, mais optimise également la taille de votre bundle d'application.

En incluant uniquement les fonctionnalités requises, vous pouvez améliorer les performances de votre application, en particulier en termes de temps de chargement pour les utilisateurs.

Cela contraste complètement avec l'objet `Date` de JavaScript natif qui, parce qu'il est intégré au langage JavaScript, ne peut pas être écrasé, étendu ou avoir des éléments particuliers supprimés.

# Mutabilité dans DayJS

Attendez, que signifie mutabilité ?

La mutabilité fait référence à la capacité d'un objet à changer d'état après sa création.

En programmation, un objet **mutable** peut être modifié. C'est-à-dire que ses propriétés ou valeurs peuvent être altérées après sa création initiale. Cela peut entraîner des changements inattendus et des effets secondaires, affectant potentiellement le comportement du programme.

Cela est particulièrement vrai lorsqu'il s'agit de dates et d'heures. L'objet Date de JavaScript natif est **mutable**, ce qui signifie que la modification d'une instance peut affecter involontairement d'autres instances.

C'est pourquoi l'objet `Date` possède des méthodes `set` sur l'objet lui-même. Ainsi, lors de l'appel de ces méthodes, cela affecte l'objet lui-même.

Peut-être qu'un exemple aidera :

Avec l'objet Date JS natif (mutable) :

```javascript
var date = new Date("2023-07-16"); // objet date original
console.log(date); //2023-07-16T00:00:00.000Z

date.setDate(date.getDate() + 1); // changer la date - ajouter 1 jour
console.log(date); // 2023-07-17T00:00:00.000Z la date originale a été changée
```

Ici, nous avons utilisé la commande `new Date()` pour initialiser un nouvel objet date. Cet objet est mutable, et pour obtenir une valeur mise à jour, nous devons muter l'objet original car il est *mutable*. Nous faisons cela en utilisant la fonction `setDate()`.

Lorsque vous utilisez la fonctionnalité Date intégrée de JavaScript, vous devez faire attention à la manière dont vous utilisez et modifiez les objets date. Vous pouvez vous retrouver dans une toile de résultats inattendus si vous commencez à modifier trop l'objet date original.

## Immuabilité et objets immuables dans DayJS

En revanche, l'immuabilité signifie qu'un objet ne peut pas changer d'état une fois créé, car il ne fait pas d'actions de "changement" sur l'objet réel lui-même.

Lorsque vous travaillez avec des objets immuables, vous créez une nouvelle instance avec des valeurs modifiées au lieu de modifier l'original. Cela aide à garantir que vos données restent cohérentes et prévisibles tout au long de votre programme.

Les structures de données immuables sont souvent privilégiées en programmation fonctionnelle et peuvent conduire à un code plus robuste et plus facile à maintenir.

Lorsque vous effectuez des opérations sur un objet DayJS, telles que l'ajout ou la soustraction de temps, la bibliothèque retourne une nouvelle instance avec la valeur modifiée, laissant l'instance originale inchangée.

Cette approche empêche les changements inattendus de vos données et réduit le risque d'introduire des erreurs qui peuvent être difficiles à tracer.

Considérez l'exemple suivant utilisant DayJS :

```javascript
var originalDate = dayjs("2023-07-16");
var modifiedDate = originalDate.add(1, "day");

console.log(originalDate.format("YYYY-MM-DD")); // Sortie : "2023-07-16"
console.log(modifiedDate.format("YYYY-MM-DD")); // Sortie : "2023-07-17"
```

En utilisant DayJS, vous pouvez modifier l'objet date original autant que vous le souhaitez en utilisant les diverses fonctions disponibles, sans perdre la valeur originale. Cela signifie qu'il peut être utilisé/accédé à tout moment.

### Avantages de l'immuabilité

- Prévisibilité : L'immuabilité garantit qu'une fois qu'un objet de date ou d'heure est créé (définis), il ne changera pas de manière inattendue dans votre code. Cela facilite le raisonnement sur le comportement de votre programme.

- Débogage : Les objets mutables peuvent entraîner des bugs difficiles à tracer lorsque leurs valeurs changent de manière inattendue. Avec l'immuabilité, vous pouvez être confiant qu'une date ou une heure ne changera pas sans votre intention explicite.

- Traitement parallèle : Dans les environnements de programmation multithread ou parallèle, les structures de données immuables sont intrinsèquement thread-safe. Cela peut prévenir les conditions de course et les problèmes de synchronisation.

**Note :** Vous pouvez obtenir un "immuable" comme solution de contournement en clonant l'objet `Date` original comme suit :

```javascript
const cloneDate = (date) => {
  return new Date(date.getTime());
};

// Exemple d'utilisation
var originalDate = new Date("2023-07-16");
var mutableDate = cloneDate(originalDate);

mutableDate.setDate(mutableDate.getDate() + 1);

console.log(originalDate); // 2023-07-16T00:00:00.000Z
console.log(mutableDate); // 2023-07-17T00:00:00.000Z
```

Ce code crée une fonction de clonage, qui prend la date originale, puis crée une nouvelle date à partir de l'originale et la retourne. Cela vous permet de conserver la date originale, mais d'apporter des modifications à une réplique de cette date, sans modifier l'originale.

L'inconvénient de cela est une utilisation accrue de la mémoire et la complexité supplémentaire.

## Flexibilité de parsing

Le parsing des chaînes de date peut être un vrai défi en JavaScript natif, en particulier lorsqu'il s'agit de formats non standard.

DayJS offre un ensemble étendu d'options de parsing, le rendant beaucoup plus polyvalent lorsqu'il s'agit de traiter une large gamme de formats d'entrée. Cette fonctionnalité s'avère particulièrement précieuse lorsqu'on travaille avec des données provenant de sources diverses ou d'API qui peuvent avoir différentes représentations de dates.

* Saisie utilisateur : Lorsqu'on traite des saisies utilisateur, telles que des dates provenant de formulaires, les utilisateurs peuvent entrer des dates dans divers formats. Les capacités de parsing de DayJS vous permettent de traiter ces entrées de manière précise et cohérente.

* Interaction avec la base de données : Les bases de données peuvent stocker des dates dans différents formats ou fuseaux horaires. Le parsing de DayJS peut aider à interpréter correctement ces dates pour une utilisation dans votre application.

* Réponses API : Les API retournent souvent des données de date et d'heure dans des formats standardisés comme ISO 8601, mais ils peuvent également varier. DayJS vous permet de parser facilement les réponses API, garantissant une représentation correcte des données dans votre application.


### Comment cela se compare avec JavaScript natif :

L'objet Date de JavaScript natif manque de la même flexibilité de parsing. Bien qu'il puisse gérer certains formats standard (ISO8601 / RFC2822) et quelques autres variations, la gestion de formats non standard ou divers peut être difficile. Vous devez souvent diviser manuellement la chaîne de date et effectuer des calculs pour créer un objet Date valide.

Supposons que nous avions une date en-GB, (jour/mois/année). Par défaut, l'objet `Date` ne gère pas cela. Cela signifie que nous devons la parser nous-mêmes en divisant la chaîne en parties, et en passant celles-ci à l'appel `new Date()`.

```javascript
const dateString = "23/08/2023";
const parts = dateString.split("/");
const dateObject = new Date(parts[2], parts[0] - 1, parts[1]);

console.log(dateObject);
```

Si vous essayiez de passer `dateString` directement à l'appel `new Date()`, vous obtiendriez une erreur, cependant au format en-US (mois/jour/année), cela fonctionne bien.

```javascript
const ukDate = new Date("21/01/2023");
console.log(ukDate) // Sortie : Date invalide

const usDate = new Date("01/21/2023");
console.log(usDate); // Sortie : 2023-01-21T00:00:00.000Z
```

Ici, vous pouvez voir que la connaissance du fonctionnement de l'objet `Date` est nécessaire. Si cela se trouvait dans une application réelle, des tests seraient nécessaires pour garantir que nous n'obtenons aucune erreur lors du parsing à partir de plusieurs sources.

### Flexibilité de parsing de DayJS

DayJS s'appuie sur la fonctionnalité principale de `Date`, et pour moi, ajoute l'une des meilleures options de parsing pour les développeurs. Il vous permet de passer n'importe quelle chaîne de date à la fonction `dayjs()`, ainsi que le format de cette chaîne.

**Note :** Cela nécessite l'ajout du plugin `customParseFormat` de DayJS – celui-ci peut être importé très facilement.

```javascript:
import dayjs from "dayjs";
import CustomParseFormat from "dayjs/plugin/customParseFormat";

dayjs.extend(CustomParseFormat);
```

Cela signifie que lorsque vous traitez avec plusieurs sources, vous pouvez dire à DayJS de parser la chaîne de date selon la manière dont la source la présente.

Normalement, je dirais de stocker toutes les dates (lorsque vous avez le contrôle sur une telle chose) sous forme de chaînes de date UTC ISO8601, car alors vous avez une base solide, et vous pouvez les convertir dans le fuseau horaire pertinent lorsque nécessaire.

En décomposant la fonction `dayjs()`, nous pouvons voir qu'elle peut recevoir plusieurs paramètres. Ce sont :

- **string** (string) – c'est la représentation sous forme de chaîne de la date que vous souhaitez créer.

- **format** (string) – c'est le format de la chaîne que vous passez (de la même manière que nous l'avons fait avec la fonction `format()`).

- **timezone** / **locale** (string) – Clé de locale à utiliser lors du parsing.

- **strict parsing** (boolean) – Le parsing strict nécessite que le format et l'entrée correspondent exactement, y compris les délimiteurs.

Alors, que signifie tout cela ? Eh bien, cela signifie que nous avons beaucoup plus de contrôle sur notre parsing / création de dates.

Exemples :

```javascript
const date1 = dayjs('20/03/2013', 'DD/MM/YYYY').toISOString(); // Pas d'erreur & Sortie : '2023-03-20T00:00:00.000Z'

// indiquer le format dans lequel la dateString sera de l'API
const customFormat = 'YYYY/MM/DD HH:mm:ss'; 

const dateStr = '2023/08/23 14:37:41'; // dateString de l'API

// créer un objet dayjs à partir de dateString en le parsant en utilisant le format fourni
const parsedDate = dayjs(dateStr, customFormat);

// formater la date parsée, en supprimant le timestamp
console.log(parsedDate.format('YYYY-MM-DD'));  // Sortie : 2023-08-23
```

Espérons que vous pouvez voir que DayJS rend le parsing et le travail avec les dates beaucoup plus faciles. Il offre une multitude de façons différentes et flexibles de parser diverses dates, rendant le travail avec plusieurs sources beaucoup plus facile que simplement utiliser l'objet `Date` intégré.

# Que peut faire d'autre DayJS ?

## Comment ajouter ou soustraire à une date et heure

De nombreuses fois, on m'a demandé de calculer une date dans le futur en ajoutant un certain nombre de jours à la date actuelle, ou en soustrayant un certain nombre d'heures de l'heure.

### Comment faire cela en JavaScript natif :

En utilisant l'objet `Date` de JavaScript, nous pouvons faire cela en utilisant les fonctions `setDate()`. Nous faisons cela en :

1. Obtenant la date actuelle
2. Obtenant le nombre de jours à ajouter (5 jours)
3. En utilisant la fonction `setDate()` sur l'objet `Date` en obtenant la partie date de l'objet Date, et en ajoutant 5 jours,

Par exemple, `getDate()` pourrait retourner 16, donc nous réinitialisons la partie date à 16 + 5 = 21. Donc la date serait le 21 plutôt que le 16.

Exemple ci-dessous :

```javascript
var date = new Date(); //2023-08-16T16:43:33.072Z
var daysToAdd = 5;
date.setDate(date.getDate() + daysToAdd);

console.log(date); // 2023-08-21T16:43:33.072Z

```

ou condensé (si les lignes de code sont une préoccupation) en :

```javascript
var date = new Date()
console.log(date.setDate(date.getDate() + 5));
```

Bien que concis, cela perd un peu en lisibilité.

### Comment faire cela dans DayJS :

DayJS a une convention de nommage plus lisible pour ses fonctions. Cela signifie que lors de la lecture de votre code, vous pouvez voir ce qu'il fait plus clairement.

Par exemple, en prenant le même exemple que ci-dessus et en l'écrivant dans DayJS, cela ressemblerait à quelque chose comme ceci :

```javascript
var date = dayjs().add(5, "day").toISOString(); //2023-08-21T16:43:33.000Z
```

Ici, nous maximisons l'utilisation de l'enchaînement de fonctions et appelons `add()` sur l'objet dayjs retourné. Nous passons un nombre que nous voulons ajouter, ainsi qu'une période de temps à ajouter (dans ce cas `day`). La bibliothèque DayJS se chargera ensuite d'ajouter 5 jours à notre date actuelle. Ensuite, elle retourne cette date au format d'une chaîne ISO.

Cela peut également être fait avec la soustraction de jours comme suit :

En JavaScript natif :

```javascript
var date = new Date(); //2023-08-16T16:43:33.072Z
var daysToSubtract = 5;
date.setDate(date.getDate() - daysToAdd);

console.log(date); // 2023-08-11T16:43:33.072Z

```

Dans DayJS :

```javascript
var date = dayjs().subtract(5, "day").toISOString(); //2023-08-11T16:43:33
```

Une fois de plus, la clarté de la bibliothèque DayJS permet à l'utilisateur de la lire plus comme de l'anglais simple : "Soustraire 5 jours de cet objet DayJS et retourner sous forme de chaîne ISO."

## Comment comparer des dates dans DayJS

Lorsque vous travaillez avec des dates, il y aura souvent des moments où vous devez comparer des objets de date – par exemple, vérifier si une date est avant ou après une autre date spécifique.

Avec l'objet `Date` de JavaScript, vous feriez généralement cela en utilisant les opérateurs `greaterThan` (>) ou `lessThan` (<).

Mais il peut souvent être confus de savoir dans quel sens utiliser ces opérateurs. Cela est dû au fait que pour appliquer les opérateurs aux dates, les dates sont converties en timestamps sous le capot, puis comparées chronologiquement.

Par exemple :

```javascript
var date1 = new Date("2023-07-16");
var date2 = new Date("2023-07-18");

if (date1 < date2) {
  console.log("Date 1 est avant Date 2");
} else {
  console.log("Date 1 est après Date 2");
}

// après
if (date1 > date2) {
  console.log("Date 1 est après Date 2");
} else {
  console.log("Date 1 est avant Date 2");
}

// même
if (date1 === date2) {
  console.log("Date 1 est exactement la même que Date 2");
} else {
  console.log("Date 1 n'est pas exactement la même que Date 2");
}
```

Bien que cela semble très simple à lire et à utiliser, DayJS offre une excellente API pour traiter la comparaison de dates, qui peut être un peu plus facile à lire immédiatement.

Par exemple :

```javascript
var date1 = dayjs("2023-07-16");
var date2 = dayjs("2023-07-18");
```

Maintenant, disons que nous voulons vérifier si date1 est avant date2 – nous pouvons utiliser la fonction API `isBefore()`. Moi et de nombreux autres développeurs trouvons cela beaucoup plus clair quant à ce que le code fait réellement, plutôt que de devoir réfléchir à quel opérateur le code utilise.

```javascript
if (date1.isBefore(date2)) {
  console.log("Date 1 est avant date 2");
} else {
  console.log("Date 1 est après date 2");
}
```

Vous pouvez également utiliser la fonction `isAfter()` pour obtenir un résultat similaire, en vérifiant si date1 est **après** date2.

```javascript
if (date1.isAfter(date2)) {
  console.log("Date 1 est après date 2");
} else {
  console.log("Date 1 est avant date 2");
}
```

Une fonction API que je trouve beaucoup plus fiable est la fonction `isSame`. Comme de nombreux développeurs JavaScript le savent, lors de la vérification de l'égalité des objets, surtout pour les développeurs nouveaux dans le langage, il peut être confus de savoir quand utiliser `==` vs `===`.

DayJS élimine cette inconnue et donne une fonction claire/lisible pour le faire pour vous.

```
//vérifier si date1 est la même que date2
if (date1.isSame(date2)) {
  console.log("Date 1 est exactement la même que date 2");
} else {
  console.log("Date 1 n'est pas exactement la même que date 2");
}
```

Disons que nous voulons vérifier qu'une date se situe entre deux plages. Encore une fois, DayJS facilite cela avec la fonction `isBetween()`. L'utilisation de la fonction `isBetween()` nous offre plusieurs autres avantages :

* Vérification facile de la plage de dates : Au lieu de comparer manuellement les dates et d'effectuer des opérations arithmétiques, vous pouvez utiliser `isBetween()` pour vérifier facilement si une date se situe dans une plage spécifiée.

* Lisibilité et maintenabilité : L'utilisation de `isBetween()` rend votre code plus lisible et compréhensible. Il exprime clairement l'intention de vérifier si une date se situe dans une certaine plage.

* Prise en charge des plages inclusives et exclusives : La fonction `isBetween()` dans DayJS vous permet de spécifier si les dates de début et de fin sont incluses ou exclues de la plage. Cela vous donne de la flexibilité dans la définition de vos intervalles de dates.

Exemple :

```javascript
const targetDate = dayjs('2023-08-15');
const startDate = dayjs('2023-08-01');
const endDate = dayjs('2023-08-31');

const isWithinRange = targetDate.isBetween(startDate, endDate, null, '[]'); 
console.log(isWithinRange) // Sortie : true
```

Comme vous pouvez le voir, les fonctions `isBefore`, `isAfter`, `isSame` et `isBetween` rendent plus clair ce que le code vérifie.

Avoir des noms aussi verbeux montre une intention claire de ce que fait la fonction (par opposition aux méthodes intégrées de JavaScript utilisant des opérateurs ou des conversions mathématiques). La nature claire et concise des fonctions API peut être utile pour les développeurs juniors ou lors du simple parcours du code.

Cela est certainement plus apparent avec les fonctions DayJS comme :

- `isYesterday()`
- `isTomorrow()`
- `isToday()`

## Comment obtenir la différence entre deux dates

La fonction `diff` rend l'obtention de la différence entre deux dates si simple. Bien plus facile qu'avec l'objet `Date` standard !

Quand voudrions-nous faire cela, cependant ? Supposons que vous construisiez un portail utilisateur et que vous souhaitiez afficher le nombre de jours ou d'heures depuis votre dernière visite. Ou une application de compte à rebours, qui peut nous montrer combien de jours, semaines, heures jusqu'à une date et une heure particulières. Vous pourriez faire tout cela en utilisant la fonction `diff()`.

Examinons la fonction `diff` :

```javascript
const date1 = dayjs("2019-01-25");
const date2 = dayjs("2018-06-05");

const differenceInMilliseconds = date1.diff(date2); 
console.log(differenceInMilliseconds); // Sortie : // 20214000000 
```

Mais les millisecondes ne sont pas toujours utiles pour les éléments d'interface utilisateur, où nous pouvons vouloir afficher des jours, des semaines ou des mois.

Heureusement pour nous, DayJS nous permet de spécifier la dénomination de temps que nous souhaitons retourner comme différence.

En revenant à notre exemple d'interface utilisateur, nous pourrions avoir un bouton bascule qui pourrait passer entre plusieurs dénominations de temps. Cela montrerait à l'utilisateur plusieurs périodes depuis sa dernière connexion, ou combien de jours ou d'heures il a passés à compléter un jeu, etc.

Dénominations disponibles :
- jours
- semaines
- trimestres
- mois
- années
- heures
- secondes
- millisecondes

```javascript
const date1 = dayjs("2023-01-25");
const date2 = dayjs("2022-06-05")
date1.diff(date2, "month"); // 7 (mois)

const date1 = dayjs("2023-08-25");
date1.diff("2023-08-27", "day"); // 2
```

Par défaut, `diff()` tronque le résultat à zéro décimale, retournant un entier. Si vous voulez un nombre à virgule flottante, passez true comme troisième argument, ce qui vous donnera une différence plus précise.

```javascript
const date1 = dayjs("2023-01-25");
date1.diff("2022-06-05", "month", true); // 7.645161290322581
```

D'accord, mais pourquoi est-ce tellement mieux que d'utiliser l'objet `Date` en JavaScript ? Eh bien, regardons comment nous ferions cela avec `Date`.

```javascript
function calculateDateDifferenceInDays(date1, date2) {
  // Convertir les deux dates en millisecondes
  const date1Millis = date1.getTime();
  const date2Millis = date2.getTime();

  // Calculer la différence en millisecondes
  const differenceMillis = Math.abs(date2Millis - date1Millis);

  // Convertir les millisecondes en jours (1 jour = 24 heures = 24 * 60 * 60 * 1000 ms)
  const differenceDays = differenceMillis / (24 * 60 * 60 * 1000);

  return differenceDays;
}

// Exemple d'utilisation
const startDate = new Date('2023-08-15');
const endDate = new Date('2023-08-25');

const daysDifference = calculateDateDifferenceInDays(startDate, endDate);
console.log(`La différence entre les dates est de ${daysDifference} jours.`);

```

D'emblée, nous avons dû coder en dur la fonction pour qu'elle ne retourne que les `jours`. Pour permettre les mêmes variations que nous obtenons dans la bibliothèque `dayjs`, nous devrions écrire notre propre fonction d'extension, qui gérerait chaque combinaison de conversion nécessaire.

Par exemple, obtenir la différence en mois pourrait être calculé légèrement différemment :

```javascript
function calculateMonthDifference(startDate, endDate) {
  const startYear = startDate.getFullYear();
  const startMonth = startDate.getMonth();

  const endYear = endDate.getFullYear();
  const endMonth = endDate.getMonth();

  const yearDifference = endYear - startYear;
  const monthDifference = endMonth - startMonth;

  return yearDifference * 12 + monthDifference;
}
```

Mais encore une fois, ce n'est que plus de code complexe pour faire quelque chose qu'une petite bibliothèque pourrait faire en un maximum de 3 lignes de code. Ce n'est tout simplement pas aussi flexible et facile à utiliser que DayJS.

## Comment obtenir le début ou la fin d'une période de temps

`startOf` et `endOf` sont deux autres fonctions intéressantes de la bibliothèque DayJS. Elles vous permettent de retourner facilement le début et la fin d'une période de date.

Par exemple, vous pourriez obtenir le début/la fin du jour, de la semaine, du mois ou de l'année. Cela pourrait être utile lorsque vous avez besoin de calculer combien de jours il reste dans un mois. Certains mois ont plus de jours que d'autres, mais nous ne voulons pas avoir à calculer/suivre cela quelque part dans notre code.

Voyons comment vous pouvez l'utiliser :

```javascript
const startOfDay = dayjs().startOf("day"); // 00:00:00 d'aujourd'hui

// ou date donnée
const startOfGivenDate = dayjs("2023-08-12T15:00:00").startOf("day");

const startOfWeek = dayjs().startOf("week"); // 00:00:00 premier jour de la semaine (sensible à la locale)
const startOfYear = dayjs().startOf("year"); // 1er janvier 2023 00:00:00

const endOfDay = dayjs().endOf("day"); // 23:59:59 d'aujourd'hui
const endOfWeek = dayjs().endOf("week"); // 23:59:59 du dernier jour de la semaine (sensible à la locale)
const endOfYear = dayjs().endOf("year"); // 31 décembre 2023 23:59:59
```

Si nous voulions accomplir la même chose avec JavaScript natif, nous devrions faire quelque chose comme ceci :

```javascript
const beginningOfDay = (inputTime?: string) => {

  // Convertir inputTime en un objet Date si fourni
  let date inputTime ? new Date(inputTime) : new Date();

  // Définir l'heure à 00:00:00
  date.setHours(0, 0, 0, 0);

  return date;
};

const givenTime = "2023-08-12T15:00:00"; // 15h le 12 août 2023
const startOfGiven = beginningOfGivenDay(givenTime);
```

Comme vous pouvez le voir, DayJS facilite la gestion du début et de la fin des périodes de temps par rapport à l'utilisation de JavaScript pur. JavaScript tend à nécessiter plus de code, car vous devriez écrire votre propre implémentation de chacune de ces méthodes.


## Comment combiner des fonctions dans DayJS

Comme déjà discuté, DayJS permet l'enchaînement de fonctions, ce qui en fait un outil très puissant.

Prenons un scénario où nous avons un portail utilisateur et nous voulons savoir si le temps entre aujourd'hui et la fin du mois est supérieur à 7 jours pour déterminer quel élément d'interface afficher (par exemple "expirant bientôt" ou "continuer").

Vous pouvez faire cela en moins de 5 lignes de code avec DayJS comme suit :

```javascript
const current = dayjs();
const differenceInDays = current.endOf('month').diff(current,'day');

if(differenceInDays <= 7){
 console.log("Expire bientôt"); 
}
```

**Que fait-il ?**

1. Obtenir la date et l'heure actuelles
2. Utiliser l'enchaînement de fonctions et l'immuabilité pour :
    a. obtenir la fin du mois en cours
    b. obtenir la différence entre la fin actuelle du mois et la date et l'heure actuelles.
3. Vérifier si la `differenceInDays` est inférieure ou égale à 7
4. Si oui, afficher un message `expire bientôt`.

"Oh, allez, nous pourrions encore le faire en JavaScript" je vous entends dire. Eh bien, oui – comme tous les autres exemples, vous pourriez le faire en JS. Mais encore une fois, cela prendrait plus d'efforts et de code qui doit être maintenu. Voici à quoi cela ressemblerait :

```javascript
function daysUntilEndOfMonth() {
  const currentDate = new Date();
  const currentYear = currentDate.getFullYear();
  const currentMonth = currentDate.getMonth();
  
  // Obtenir le premier jour du mois suivant
  const firstDayOfNextMonth = new Date(currentYear, currentMonth + 1, 1);
  
  // Soustraire un jour pour obtenir le dernier jour du mois en cours
  const lastDayOfCurrentMonth = new Date(firstDayOfNextMonth.getTime() - 1);
  
  // Calculer la différence en jours (en utilisant le timestamp)
  const timeDifference = lastDayOfCurrentMonth - currentDate;
  console.log(timeDifference) // Sortie : 689366264 (millisecondes)
  
  // Convertir le timestamp en jours réels
  const daysDifference = Math.ceil(timeDifference / (24 * 60 * 60 * 1000));
  
  return daysDifference;
}

// Exemple d'utilisation
const daysUntilEnd = daysUntilEndOfMonth();
console.log(`Nombre de jours jusqu'à la fin du mois : ${daysUntilEnd} jours`); //Sortie : Nombre de jours jusqu'à la fin du mois : 8 jours

```

Un peu plus simple avec DayJS, n'est-ce pas ?


## Conclusion

En essence, l'objectif final de cet article était de mettre en lumière une bibliothèque utile qui facilite grandement le travail avec les dates et les heures. Le code est beaucoup plus concis et plus facile à lire que l'objet Date standard intégré dans JavaScript.

Je ne dis pas que l'une des utilisations de l'objet `Date` dans ce tutoriel est fausse ou mauvaise. Je souligne simplement que vous n'avez pas toujours besoin d'écrire un code fastidieux et surcompliqué lorsqu'une bibliothèque libre est disponible. Surtout lorsqu'elle est extrêmement petite (négligeable) en taille. Elle aura également un impact minime sur le bundling ou l'exécution de votre code, et elle vous offre tant en termes d'avantages.

Allez, jetez un coup d'œil et ajoutez-la à votre prochain projet ou à un projet existant. Essayez-la et faites-moi savoir ce que vous en pensez via [twitter](http://twitter.com/gweaths).

Vous pouvez en savoir plus sur DayJS et tirer parti de toutes ses capacités [ici](https://dayjs.org) sur leur site web.