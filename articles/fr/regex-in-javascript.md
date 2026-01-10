---
title: Expressions régulières (RegEx) en JavaScript – Un guide pour débutants
subtitle: ''
author: Samyak Jain
co_authors: []
series: null
date: '2024-02-27T20:17:37.000Z'
originalURL: https://freecodecamp.org/news/regex-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Regular-Expressions-in-JavaScript-Cover-2.png
tags:
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
- name: Regex
  slug: regex
seo_title: Expressions régulières (RegEx) en JavaScript – Un guide pour débutants
seo_desc: Regular expressions, also known as regex, are powerful tools for pattern
  matching and text manipulation. Whether you're validating user input, extracting
  data from strings, or performing advanced text processing tasks, understanding regex
  is essentia...
---

Les expressions régulières, également connues sous le nom de regex, sont des outils puissants pour la correspondance de motifs et la manipulation de texte. Que vous validiez les entrées utilisateur, extrayiez des données de chaînes de caractères ou effectuiez des tâches avancées de traitement de texte, la compréhension des regex est essentielle pour les développeurs.

Ce guide complet vous guidera à travers les fondamentaux des expressions régulières en JavaScript, y compris comment les créer et les utiliser, leurs caractères spéciaux, les drapeaux et des exemples pratiques. 

### Prérequis : 

Bien que ce tutoriel soit conçu pour être accessible aux débutants, avoir une compréhension de base des fondamentaux de JavaScript sera bénéfique. La familiarité avec les variables, les types de données, les fonctions et la manipulation de chaînes de caractères en JavaScript vous aidera à saisir les concepts couverts.

## Table des matières :

1. [Qu'est-ce que les Regex](#heading-quest-ce-que-les-regex) ?  
– [Comment écrire des motifs d'expressions régulières](#heading-comment-ecrire-des-motifs-d-expressions-regulieres)
2. [Comment utiliser les expressions régulières en JavaScript](#heading-comment-utiliser-les-expressions-regulieres-en-javascript)  
– Méthodes RegEx en JavaScript  
– [Recherche avancée avec des drapeaux](#heading-recherche-avancee-avec-des-drapeaux)
3. [Ancres dans Regex](#heading-ancres-dans-regex)  
– [Mode Multiline (m) des ancres](#heading-mode-multiline-m-des-ancres)   
– [Limites de mots (`\b`)](#heading-limites-de-mots-b)
4. [Quantificateurs dans Regex](#heading-quantificateurs-dans-regex)  
– [Quantificateurs gourmands](#heading-quantificateurs-gourmands)  
– [Quantificateurs non gourmands (Mode paresseux)](#heading-quantificateurs-non-gourmands-mode-paresseux)
5. [Ensembles et plages dans Regex](#heading-ensembles-et-plages-dans-regex)  
– [Ensembles](#heading-ensembles)  
– [Plages](#heading-plages)  
– [Négation / Exclusion de plages](#heading-negation-exclusion-de-plages)  
– [Classes de caractères prédéfinies](#heading-classes-de-caracteres-predefinies)
6. [Caractères spéciaux et échappement dans Regex](#heading-caracteres-speciaux-et-echappement-dans-regex)  
– [Metacaractères](#heading-metacaracteres)  
– [Échappement des caractères spéciaux](#heading-echappement-des-caracteres-speciaux)
7. [Groupements dans RegEx](#heading-groupements-dans-regex)  
– [Groupes de capture](#heading-groupes-de-capture)  
– [Groupes non capturants](#heading-groupes-non-capturants)  
– [Références arrière](#heading-references-arriere)  
– [Alternance Regex](#heading-alternance-regex)
8. [Assertions de lookahead et lookbehind dans Regex](#heading-assertions-de-lookahead-et-lookbehind-dans-regex)  
– [Lookahead (?=)](#heading-lookahead)  
– [Negative Lookahead (?!)](#heading-negative-lookaheads)  
– [Lookbehind (?<=)](#heading-lookbehind)  
– [Negative Lookbehind (?<!)](#heading-negative-lookbehind)
9. [Exemples pratiques et cas d'utilisation de Regex](#heading-exemples-pratiques-et-cas-d-utilisation-de-regex)  
– [Vérification de la force du mot de passe](#heading-verification-de-la-force-du-mot-de-passe)  
– [Validation d'email](#heading-validation-d-email)   
– [Formatage de numéro de téléphone](#heading-formatage-de-numero-de-telephone)
10. [Conseils et meilleures pratiques pour utiliser les expressions régulières](#heading-conseils-et-meilleures-pratiques-pour-utiliser-les-expressions-regulieres)
11. [Conclusion](#heading-conclusion)

## Qu'est-ce que les Regex ?

Une expression régulière, souvent abrégée en "regex", est une séquence de caractères qui définit un motif de recherche. Ce motif est utilisé pour trouver des correspondances dans des chaînes de caractères, vous aidant à identifier un texte spécifique ou des motifs de caractères, fournissant un moyen puissant de rechercher, remplacer et manipuler du texte.

En JavaScript, vous pouvez créer des expressions régulières en utilisant soit une notation littérale, soit le constructeur `RegExp` :

* **Utilisation d'un littéral d'expression régulière** : Cela implique d'enfermer le motif entre des barres obliques ("/").

```javascript
const re = /pattern/;

// exemple
const re = /ab+c/;

```

* **Utilisation de la fonction constructeur : `RegExp`** constructeur. Cela permet la compilation à l'exécution de l'expression régulière et est utile lorsque le motif peut changer.

```javascript
const re = new RegExp("pattern");

// exemple
const re = new RegExp("ab+c");

```

Les deux méthodes produisent le même résultat – c'est une question de préférence de choisir l'une ou l'autre.

### Comment écrire des motifs d'expressions régulières

Un motif d'expression régulière peut consister en des caractères simples ou une combinaison de caractères simples et spéciaux. 

1. **Motif simple** : Ils correspondent à des séquences de caractères exactes. Par exemple, le motif `/abc/` correspond à la séquence "abc" dans une chaîne.
2. **Caractères spéciaux** : Ils améliorent la correspondance de motifs avec des capacités comme la répétition ou la correspondance de types spécifiques de caractères, permettant une correspondance de motifs plus flexible et puissante. Par exemple, `*` correspond à zéro ou plusieurs occurrences de l'élément précédent. `/ab*c/` correspond à "ac", "abc", "abbc", et ainsi de suite.

## Comment utiliser les expressions régulières en JavaScript

Vous pouvez utiliser des expressions régulières avec diverses méthodes disponibles pour les objets `RegExp` et `String` en JavaScript. Certaines méthodes comme `test()`, `exec()`, et autres ont cette syntaxe :

```javascript
regex.methodname(string)

// exemple
regex.test(string)
```

Alors que certaines méthodes comme `match()`, `replace()`, et ainsi de suite ont cette syntaxe :

```javascript
string.methodname(regex)

// exemple
string.replace(regex, replacement)
```

Ici, `string` est la chaîne et `regex` est un motif d'expression régulière.

Explorons comment ces méthodes sont utilisées en pratique.

**La méthode `test()`** : vérifie si une chaîne particulière correspond à un motif ou une expression régulière spécifiée. Elle retourne `true` si le motif est trouvé dans la chaîne, sinon, elle retourne `false`.

```javascript
let pattern = /hello/;
let str = "hello world";

let result = pattern.test(str);
console.log(result); // Sortie : true

```

**La méthode `exec()`** : recherche une correspondance d'un motif dans une chaîne. Elle retourne un tableau contenant des détails comme le texte correspondant, l'index de la correspondance dans la chaîne, et la chaîne d'entrée elle-même. Exemple :

```javascript
let pattern = /world/;
let str = "hello world";

let result = pattern.exec(str);
console.log(result); // Sortie : ["world", index: 6, input: "hello world"]

```

**La méthode `match()`** : Recherche des occurrences d'un motif dans une chaîne. Elle retourne le premier élément correspondant. Si elle a le drapeau global (`g`), elle retourne un tableau contenant toutes les correspondances trouvées, ou `null` si aucune correspondance n'est trouvée.

```javascript
let str = "The quick brown fox jumps over the lazy dog.";
let matches = str.match(/the/gi);

console.log(matches); // Sortie : ["The", "the"]

```

**La méthode `matchAll()`** : Retourne un itérateur de tous les résultats correspondant à une expression régulière contre une chaîne. Chaque élément de l'itérateur est un tableau contenant des détails sur la correspondance, y compris les groupes capturés.

```javascript
let str = "Hello world! This is a test string.";
let regex = /[a-zA-Z]+/g;

let matches = str.matchAll(regex);

for (let match of matches) {
    console.log(match);
}

```

Cette méthode est utile lorsque vous avez besoin d'informations détaillées sur toutes les correspondances trouvées dans une chaîne.

**La méthode `search()`** : Recherche un motif spécifié dans une chaîne. Elle retourne l'index de la première occurrence du motif dans la chaîne, ou `-1` si le motif n'est pas trouvé.

```javascript
let str = "The quick brown fox jumps over the lazy dog";
let pattern = /brown/;

let result = str.search(pattern);
console.log(result); // Sortie : 10

```

**La méthode `replace()`** : Remplace la première occurrence d'un motif spécifié dans une chaîne par une autre sous-chaîne ou valeur. Pour remplacer toutes les occurrences, vous pouvez utiliser le drapeau global (`g`) dans l'expression régulière.

```javascript
let str = "Hello, World!";
let newStr = str.replace(/o/g, "0");

console.log(newStr); // Sortie : "Hell0, W0rld!"
```

**La méthode `replaceAll()`** : Remplace toutes les occurrences d'une sous-chaîne ou d'un motif spécifié par une chaîne de remplacement. Elle diffère de `replace()` en ce qu'elle remplace toutes les occurrences par défaut, sans avoir besoin d'un drapeau global (`g`).

```javascript
let str = "apple,banana,apple,grape";
let newStr = str.replaceAll("apple", "orange");
console.log(newStr); // Sortie : "orange,banana,orange,grape"

```

Cette méthode simplifie le processus de remplacement de toutes les occurrences d'une sous-chaîne dans une chaîne.

**La méthode `split()`** : Bien que ce ne soit pas exclusivement une méthode RegEx, `split()` peut accepter un motif RegEx comme argument pour diviser une chaîne en un tableau de sous-chaînes basées sur les motifs ou délimiteurs spécifiés. Par exemple :

```javascript
let str = "apple,banana,grape";
let arr = str.split(/,/);
console.log(arr); // Sortie : ["apple", "banana", "grape"]

```

Ces méthodes offrent différentes fonctionnalités en fonction de vos besoins. Par exemple, si vous avez seulement besoin de savoir si un motif est trouvé dans une chaîne, les méthodes `test()` ou `search()` sont efficaces. Si vous avez besoin de plus d'informations sur les correspondances, les méthodes `exec()` ou `match()` sont appropriées.

## Recherche avancée avec des drapeaux

En JavaScript, les expressions régulières supportent les drapeaux de motif, qui sont des paramètres optionnels modifiant le comportement de la correspondance de motifs. 

Examinons deux drapeaux courants : le drapeau ignore (`i`) et le drapeau global (`g`).

### Le drapeau Ignore (`i`) :

Le drapeau ignore (`i`) indique à l'expression régulière d'ignorer la sensibilité à la casse lors de la recherche de correspondances. Par exemple :

```javascript
let re = /hello/i;
let testString = "Hello, World!";
let result = re.test(testString);

console.log(result); // Sortie : true

```

Dans ce cas, l'expression régulière `/hello/i` correspond à la chaîne `"Hello"` malgré les différences de casse car nous avons utilisé le drapeau ignore.

### Le drapeau Global (`g`) :

Le drapeau global (`g`) permet à l'expression régulière de trouver toutes les correspondances dans une chaîne, plutôt que de s'arrêter après la première correspondance. Par exemple :

```javascript
let re = /hi/g;
let testString = "hi there, hi again!";
let result = testString.match(re);

console.log(result); // Sortie : ["hi", "hi"]

```

Dans cet exemple, l'expression régulière `/hi/g` trouve les deux occurrences de `"hi"` dans la chaîne `"hi there, hi again!"`.

### Combinaison de drapeaux

Vous pouvez combiner des drapeaux pour obtenir un comportement de correspondance spécifique. Par exemple, utiliser à la fois le drapeau ignore (`i`) et le drapeau global (`g`) ensemble permet une correspondance insensible à la casse tout en trouvant toutes les occurrences du motif.

```javascript
let re = /hi/gi;
let testString = "Hi there, HI again!";
let result = testString.match(re);

console.log(result); // Sortie : ["Hi", "HI"]

```

Ici, l'expression régulière `/hi/gi` correspond à la fois à `"Hi"` et `"HI"` dans la chaîne `"Hi there, HI again!"`.

### Le drapeau `u` :

Bien que peu utilisé, le drapeau `u` gère correctement les caractères Unicode, en particulier les paires de substitution. Les paires de substitution sont utilisées pour représenter des caractères en dehors du plan multilingue de base (BMP) dans l'encodage UTF-16.

**Exemple :** Considérons une chaîne contenant des caractères emoji et essayons de les faire correspondre en utilisant une expression régulière sans et avec le drapeau `u`.

```javascript
// Sans le drapeau u
let result1 = 'Smile Please \ud83d\ude0a'.match(/[\ud83d\ude12\ud83d\ude0a\ud83d\ude44]/);
console.log(result1); // Sortie : ["\ufffd"]

// Avec le drapeau u
let result2 = 'Smile Please \ud83d\ude0a'.match(/[\ud83d\ude12\ud83d\ude0a\ud83d\ude44]/u);
console.log(result2); // Sortie : ["\ud83d\ude0a"]

```

Sans le drapeau `u`, le regex échoue à faire correspondre correctement l'emoji car ils sont représentés comme des paires de substitution dans l'encodage UTF-16. Cependant, avec le drapeau `u`, il fait correctement correspondre l'emoji `'\ud83d\ude0a'`.

## Ancres dans Regex

Les ancres sont des caractères spéciaux dans les regex qui ne représentent pas des caractères réels mais indiquent plutôt des positions dans une chaîne. Il existe deux ancres principales : `^` et `$`.

**L'ancre `^`** : L'ancre `^` correspond au début du texte. Essentiellement, elle vérifie si une chaîne commence par un caractère ou un motif spécifique.

```javascript
let str = 'Mountain';
console.log(/^S/.test(str)); // Sortie : false
```

**L'ancre `$`** : L'ancre `$` correspond à la fin du texte. Elle vérifie si une chaîne se termine par un caractère ou un motif spécifique.

```javascript
let str = 'Ocean';
console.log(/n$/.test(str)); // Sortie : true
```

Vous pouvez souvent utiliser `^` et `$` ensemble pour vérifier si une chaîne correspond entièrement à un motif.

```javascript
let isValid = /^\d\d:\d\d$/.test('10:01');
console.log(isValid); // Sortie : true

```

* Dans le code ci-dessus, `^\d\d:\d\d$` garantit que la chaîne contient exactement deux chiffres, suivis d'un deux-points, puis exactement deux chiffres supplémentaires.

### Mode Multiline des ancres (`^` et `$`) :

Par défaut, les ancres `^` et `$` dans les expressions régulières fonctionnent en mode monoligne, ce qui signifie qu'elles correspondent au début et à la fin de toute la chaîne. Mais dans certains cas, vous pouvez vouloir faire correspondre le début et la fin de lignes individuelles dans une chaîne multiligne. C'est là que le mode multiligne, indiqué par le drapeau `m`, entre en jeu.

Puisque le mode monoligne est le mode par défaut, il ne correspond qu'au premier chiffre "1" au début de la chaîne.

```javascript
let str = `1st line\n2nd line\n3rd line`;

let re = /^\d/g; // "^\d" correspond au chiffre au début de la chaîne
let matches = str.match(re);

console.log(matches); // Sortie : ["1"]

```

* **mode multiligne (m)** : `/^\d/gm` est le motif regex avec le drapeau `m` activé. En utilisant le drapeau `m`, vous pouvez vous assurer que `^` et `$` correspondent au début et à la fin de lignes individuelles dans une chaîne multiligne, plutôt qu'à la chaîne entière elle-même.

En conséquence, il correspond à "1" de la première ligne, "2" de la deuxième ligne et "3" de la troisième ligne :

```javascript
let str = `1st line\n2nd line\n3rd line`;

let re = /^\d/gm;
let matches = str.match(re);

console.log(matches); // Sortie : ["1", "2", "3"]

```

Cela est particulièrement utile lorsque vous travaillez avec du texte contenant plusieurs lignes ou des sauts de ligne.

### Limites de mots (`\b`) :

Le `\b` est un caractère spécial dans les expressions régulières appelé ancre, tout comme `^` et `$`. Il est utilisé pour faire correspondre une position dans la chaîne où un caractère de mot (comme une lettre, un chiffre ou un soulignement) n'est pas suivi ou précédé par un autre caractère de mot. Par exemple :

* `\bword\b` correspond au mot "word" dans la chaîne, mais pas aux sous-chaînes comme "wording" ou "swordfish".

```javascript
let pattern = /\bword\b/;
let pattern2 = /word/;
console.log(pattern.test("This is a word.")); // Sortie : true
console.log(pattern.test("This is wording.")); // Sortie : false (ne correspond pas à "wording")
console.log(pattern2.test("This is wording")); // Sortie : True

```

`/word/` correspond à la sous-chaîne "word" n'importe où dans la chaîne. Il correspond à "word" dans "This is wording." car il n'inclut aucune assertion de limite de mot.

D'autres exemples peuvent être :

* `\b\d+\b` correspond aux nombres entiers dans la chaîne, mais n'inclut pas les caractères non numériques adjacents aux nombres.
* `^\bword\b$` correspond à une chaîne qui consiste uniquement en le mot "word".

## Quantificateurs dans Regex

Dans les regex, les quantificateurs vous permettent de spécifier la quantité de caractères ou de classes de caractères que vous souhaitez faire correspondre dans une chaîne. Ils sont des symboles ou des caractères qui définissent combien d'instances d'un caractère ou d'un groupe vous recherchez.

### Compte exact `{n}` :

Le quantificateur le plus simple est `{n}`, qui spécifie un compte exact de caractères ou de classes de caractères que vous souhaitez faire correspondre. Supposons que nous avons une chaîne "Year: 2022" et que nous voulons extraire l'année de celle-ci :

```javascript
let str = 'Year: 2022';
let re = /\d{4}/; // Correspond à un nombre à quatre chiffres ; essentiellement une manière concise et meilleure d'écrire \d\d\d\d

let result = str.match(re);

console.log(result); // Sortie : ["2022"]

```

### La plage `{n,m}` :

Le quantificateur de plage `{n,m}` correspond à un caractère ou une classe de caractères de n à m fois, inclusivement. Exemple :

```javascript
let str = "The meeting is scheduled for 10:30 AM and ends at 2 PM";
let re = /\d{2,4}/g; // Correspond aux nombres avec 2 à 4 chiffres

let result = str.match(re);
console.log(result); // Sortie : [ '10', '30' ]

```

### `{n,}` et raccourcis :

Le quantificateur `{n,}` correspond à un caractère ou une classe de caractères au moins n fois. De plus, il existe des notations raccourcies pour les quantificateurs courants. Exemple :

```javascript
let str = 'The price of the item is $2500';
let re = /\d{2,}/g; // Correspond aux nombres avec 2 chiffres ou plus

let result = str.match(re);
console.log(result); // Sortie : ["2500"]

```

### Raccourcis : `+`, `?`, `*` :

Les quantificateurs `+`, `?`, et `*` sont des notations raccourcies pour des cas d'utilisation courants. Utilisons le raccourci `+` pour faire correspondre un ou plusieurs chiffres dans un numéro de téléphone :

```javascript
let phone = "+1-(103)-777-0101";
let result = phone.match(/\d+/g); // Correspond à un ou plusieurs chiffres

console.log(result); // Sortie : ["1", "103", "777", "0101"]

```

### Quantificateurs : Zéro ou un (`?`) :

Le quantificateur `?` dans les expressions régulières signifie zéro ou une occurrence du caractère ou du groupe précédent. Il est équivalent à {0,1}. Exemple :

```javascript
let str = 'The sky is blue in color, but the ocean is blue in colour';
let result = str.match(/colou?r/g); // Correspond à "color" et "colour"

console.log(result); // Sortie : ["color", "colour"]

```

Dans cet exemple, l'expression régulière `/colou?r/g` correspond à la fois à "color" et "colour" dans la chaîne donnée, permettant zéro ou une occurrence de la lettre "u".

### Quantificateurs : Zéro ou plusieurs (`*`) :

Le quantificateur `*` dans les expressions régulières signifie zéro ou plusieurs occurrences du caractère ou du groupe précédent. Il est équivalent à {0,}. Exemple :

```javascript
let str = 'Computer science is fascinating, but computational engineering is equally interesting';
let re = /comput\w*/g; // Correspond à "computer" et "computational"

let results = str.match(re);

console.log(results); // Sortie : ["computer", "computational"]

```

### Quantificateurs gourmands :

Dans les expressions régulières, les quantificateurs déterminent combien de fois un élément particulier peut se produire dans une correspondance. 

Par défaut, les quantificateurs fonctionnent dans ce qu'on appelle un mode "gourmand". Cela signifie qu'ils essaient de faire correspondre autant que possible l'élément précédent. Par exemple :

```javascript
let regexp = /".+"/g;
let str = 'The "Boy" and his "Friends" were here';
console.log( str.match(regexp) ); // "Boy" and his "Friends"
```

Au lieu de trouver deux correspondances séparées ("Boy" et "Friends"), il trouve une correspondance englobant les deux ("Boy" and his "Friends").

#### Comprendre la recherche gourmande

Pour comprendre pourquoi la tentative initiale a échoué, examinons comment le moteur d'expressions régulières effectue sa recherche. 

1. Le moteur commence depuis le début de la chaîne et trouve la guillemet ouvrant.
2. Il procède à la correspondance des caractères suivant le guillemet ouvrant. Puisque le motif est `".+"`, où `.` correspond à n'importe quel caractère et `+` le quantifie pour correspondre une ou plusieurs fois, le moteur continue à correspondre aux caractères jusqu'à ce qu'il atteigne la fin de la chaîne.
3. Le moteur revient ensuite en arrière pour trouver le guillemet fermant `"` qui compléterait la correspondance. Il commence par supposer le nombre maximum de caractères correspondants par `".+"` et réduit progressivement le nombre de caractères jusqu'à ce qu'il trouve une correspondance valide.
4. Finalement, le moteur trouve une correspondance englobant toute la sous-chaîne "Boy" and his "Friends".

Ce comportement de correspondance gourmande de autant de caractères que possible est le mode par défaut des quantificateurs dans les expressions régulières et ne produit pas toujours les résultats souhaités. Vous pouvez le voir dans l'exemple où il en résulte une seule correspondance au lieu de plusieurs correspondances séparées pour les chaînes entre guillemets.

### Quantificateurs non gourmands (Mode paresseux) : 

Pour remédier aux limitations du mode gourmand, les expressions régulières supportent également un mode paresseux pour les quantificateurs. En mode paresseux, les caractères quantifiés sont répétés le nombre minimal de fois nécessaire pour satisfaire le motif.

Nous pouvons activer le mode paresseux en ajoutant un point d'interrogation `?` après le quantificateur. Par exemple, `*?` ou `+?` désigne une répétition paresseuse.

```javascript
let regexp = /".+?"/g;
let str = 'The "Boy" and his "Friends" were here';
console.log( str.match(regexp) ); // "Boy" "Friends"
```

Dans cet exemple, le quantificateur paresseux `".+?"` garantit que chaque chaîne entre guillemets est correspondue séparément en minimisant le nombre de caractères correspondus entre les guillemets ouvrants et fermants.

Traçons le processus de recherche étape par étape pour comprendre comment fonctionne le quantificateur paresseux :

* Le moteur commence depuis le début de la chaîne et trouve le guillemet ouvrant.
* Au lieu de correspondre gourmandement à tous les caractères jusqu'à la fin de la chaîne, le quantificateur paresseux `".+?"` ne correspond qu'aux caractères nécessaires pour satisfaire le motif. Il s'arrête dès qu'il rencontre le guillemet fermant `"`.
* Le moteur répète ce processus pour chaque chaîne entre guillemets dans le texte, ce qui donne des correspondances séparées pour "Boy" et "Friends".

## Ensembles et plages dans Regex

Dans les expressions régulières, vous utilisez des ensembles et des plages pour faire correspondre des caractères spécifiques ou une plage de caractères dans un motif donné.

### Ensembles :

Un ensemble est défini en utilisant des crochets `[...]`. Il vous permet de faire correspondre n'importe quel caractère dans l'ensemble. Par exemple, `[aeiou]` correspond à l'une des voyelles 'a', 'e', 'i', 'o', ou 'u'.

**Exemple :** Supposons que nous avons une chaîne `'The quick brown fox jumps over the lazy dog.'`. Pour faire correspondre toutes les voyelles dans cette chaîne, nous pouvons utiliser l'expression régulière `/[aeiou]/g`.

```javascript
let str = 'The quick brown fox jumps over the lazy dog.';
let re = /[aeiou]/g;
let results = str.match(re);

console.log(results); // Sortie : ['e', 'u', 'i', 'o', 'o', 'u', 'o', 'e', 'e', 'a', 'o']

```

```javascript
let str = 'The cat chased the rats in the backyard';;
let re = /[cr]at/g;
let results = str.match(re);

console.log(results); // Sortie : ['cats', 'rats']

```

Ici, le RegEx `[cr]at` correspond aux mots qui commencent par soit 'c', soit 'r' et sont suivis par 'at'.

### Plages :

Les plages vous permettent de spécifier une plage de caractères dans un ensemble. Par exemple, `[a-z]` correspond à n'importe quelle lettre minuscule de 'a' à 'z', et `[0-9]` correspond à n'importe quel chiffre de '0' à '9'. Exemple :

```javascript
let str = 'Hello World!';
let re = /[a-z]/g;
let results = str.match(re);

console.log(results); // Sortie : ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

```

### Négation / Exclusion de plages :

Pour exclure certains caractères d'un ensemble, vous pouvez utiliser le symbole `^` à l'intérieur des crochets. Exemple :

```javascript
let str = 'The price is $19.99';
let re = /[^0-9]/g;
let results = str.match(re);

console.log(results); // Sortie : ['T', 'h', 'e', ' ', 'p', 'r', 'i', 'c', 'e', ' ', 'i', 's', ' ', '$', '.'] 

```

De même, `[^a-z]` correspondra à n'importe quel caractère qui n'est pas une lettre minuscule :

```javascript
let str = 'The price is $19.99';
let results2 = str.match(/[^a-z]/g);

console.log(results2); // Sortie : ['T', ' ', ' ', ' ', '$', '1', '9', '.', '9', '9']

```

### Classes de caractères prédéfinies :

Certaines classes de caractères ont des notations raccourcies prédéfinies pour des plages courantes de caractères. 

**Classe `\d`** : Elle correspond à n'importe quel caractère de chiffre, équivalent à la plage `[0-9]`. Exemple : 

```javascript
let phone = '+1-(103)-777-0101';
let re = /\d/g;
let numbers = phone.match(re);
let phoneNo = numbers.join('');
console.log(phoneNo); // Sortie : 11037770101

```

Nous avons utilisé les méthodes `match()` et `join()` pour formater le numéro de téléphone. Cette approche simplifie le processus de formatage et de nettoyage des données, le rendant adapté à diverses applications de traitement de texte.

De même, `**\s**` correspond à un seul caractère d'espace blanc, y compris les espaces, les tabulations et les caractères de nouvelle ligne, et `**\w**` correspond à n'importe quel caractère de mot (caractère alphanumérique ou soulignement), équivalent à la plage `[a-zA-Z0-9_]`.

La combinaison de ces classes permet une correspondance de motifs plus flexible et précise, permettant une large gamme de tâches de traitement de texte. Exemple :

```javascript
let str = 'O2 is oxygen';
let re = /\w\d/g;
console.log(str.match(re)); // Sortie : ["O2"]

```

Ces classes de caractères prédéfinies fournissent des raccourcis pratiques pour les plages de caractères couramment utilisées.

**Les classes inverses**, désignées par des lettres majuscules (par exemple, `\D`), correspondent à n'importe quel caractère non inclus dans la classe minuscule correspondante. Cela fournit un moyen pratique de faire correspondre des caractères en dehors de ensembles spécifiques, tels que des caractères non numériques, des caractères non blancs ou des caractères non mots. Exemple :

```javascript
let phone = '+1-(103)-777-0101';
let re = /\D/g;
console.log(phone.replace(re,'')); // Sortie : 11037770101

```

## Caractères spéciaux et échappement dans Regex

### Metacaractères : 

Les métacaractères sont des caractères qui ont des significations spéciales dans les expressions régulières et sont utilisés pour construire des motifs de correspondance de texte. 

Les ancres (`^` et `$`), l'alternance (`|`), les quantificateurs (`+`, `?`, `{}`), et les classes de caractères prédéfinies (`\d`, `\w`, `\s`) sont tous considérés comme des métacaractères, chacun servant des objectifs distincts dans la définition de motifs. Nous en avons quelques autres, que nous allons couvrir maintenant.

**Le point (`.`) est un métacaractère avec une signification spéciale. Il est utilisé pour correspondre à n'importe quel caractère unique sauf les caractères de nouvelle ligne (`\n`). Il sert de joker, permettant une correspondance de motifs flexible lorsque le caractère exact est inconnu ou sans importance. 

Si vous avez besoin que le point corresponde également aux caractères de nouvelle ligne, vous pouvez utiliser le drapeau `/s` en JavaScript, qui active le mode "ligne unique", faisant correspondre le point à n'importe quel caractère, y compris les caractères de nouvelle ligne. Exemple :

```javascript
const regex = /a.b/; 

console.log(regex.test('acb')); // true
console.log(regex.test('aXb')); // true
console.log(regex.test('a\nb')); // false (le caractère de nouvelle ligne n'est pas correspond)
console.log(regex.test('a\nb', 's')); // true (avec le drapeau 's', le caractère de nouvelle ligne est correspond)
console.log(regex.test('ab')); // false (caractère manquant entre 'a' et 'b')

```

Le point (`.`) peut être combiné avec d'autres éléments regex pour former des motifs plus complexes. Par exemple, `/.at/` correspond à n'importe quelle séquence de trois caractères se terminant par 'at', comme 'cat', 'bat', ou 'hat'.

### Échappement des caractères spéciaux :

L'échappement des caractères spéciaux est essentiel lorsque vous souhaitez rechercher ou faire correspondre ces caractères dans des chaînes d'entrée sans invoquer leurs significations spéciales regex. 

Pour faire correspondre un caractère spécial littéralement dans un motif regex, vous devez l'échapper en le précédant d'un antislash (). Cela indique au moteur regex de traiter le caractère spécial comme un caractère régulier. Exemple :

```javascript
let str = 'This ^ symbol is called Caret ';
let re = /[\^]/g;
let results = str.match(re);

console.log(results); // Sortie : ['^']

```

Fait amusant : le `/` que nous utilisons pour échapper les métacaractères est lui-même un métacaractère et peut être échappé avec un autre antislash comme `//`.

## Groupements dans RegEx 

### Groupes de capture :

Dans les expressions régulières JavaScript, les groupes de capture sont utilisés pour extraire des parties spécifiques d'une chaîne correspondante. Imaginez que vous avez un chemin comme "resource/id", par exemple, "posts/123". Pour faire correspondre ce chemin, vous pouvez utiliser une expression régulière comme `/\w+\/\d+/`.

* `\w+` correspond à un ou plusieurs caractères de mot.
* `\/` correspond à la barre oblique `/`.
* `\d+` correspond à un ou plusieurs chiffres.

Supposons que vous avez un chemin comme "posts/123" et que vous voulez capturer la partie `id` (123). Nous pouvons utiliser des groupes de capture pour cela.

Pour créer un groupe de capture, vous enfermez la partie du motif regex que vous voulez capturer entre parenthèses. Par exemple, `(\d+)` capture un ou plusieurs chiffres.

Voici comment cela fonctionne :

```javascript
const path = 'posts/123';
const pattern = /\w+\/(\d+)/;

const match = path.match(pattern);
console.log(match);

```

Sortie :

```bash
[ 'posts/123', '123', index: 0, input: 'posts/123', groups: undefined ]

```

Ici, `'123'` est capturé par le groupe de capture `(\d+)`.

**Utilisation de plusieurs groupes de capture** : Vous pouvez avoir plusieurs groupes de capture dans un motif regex. Par exemple, pour capturer à la fois la ressource (comme "posts") et l'id (comme "123") à partir du chemin "posts/123", vous pouvez utiliser `/(\w+)\/(\d+)/`.

```javascript
const path = 'posts/123';
const pattern = /(\w+)\/(\d+)/;

const match = path.match(pattern);
console.log(match);

```

Sortie :

```bash
['posts/123', 'posts', '123', index: 0, input: 'posts/123', groups: undefined]

```

Ici, `'posts'` et `'`123`'` sont capturés par les deux groupes de capture `(\w+)` et `(\d+)` respectivement.

**Les groupes de capture nommés** vous permettent d'assigner des noms aux groupes de capture, ce qui facilite leur référence ultérieure dans votre code.

La syntaxe pour les groupes de capture nommés est `(?<name>rule)`, où :

* `()` indique un groupe de capture.
* `?<name>` spécifie le nom du groupe de capture.
* `rule` est une règle dans le motif.

Par exemple, supposons que nous voulons capturer la ressource (comme "posts") et l'id (comme "123") à partir du chemin "posts/123" en utilisant des groupes de capture nommés.

```javascript
const path = 'posts/123';
const pattern = /(?<resource>\w+)\/(?<id>\d+)/;

const match = path.match(pattern);
console.log(match);

```

Sortie :

```javascript
[
  'posts/123',
  'posts',
  '123',
  index: 0,
  input: 'posts/123',
  groups: [Object: null prototype] { resource: 'posts', id: '10' }
]

```

Ici, `resource` et `id` sont les noms assignés aux groupes de capture. Nous pouvons y accéder en utilisant `match.groups`.

**Un autre exemple** : Supposons que nous avons un chemin comme "posts/2022/02/18" et que nous voulons capturer la ressource (comme "posts"), l'année (comme "2022"), le mois (comme "02"), et le jour (comme "18") en utilisant des groupes de capture nommés.

Le motif regex pour cela serait :

```javascript
const path = 'posts/2024/02/22';
const pattern =
  /(?<resource>\w+)\/(?<year>\d{4})\/(?<month>\d{2})\/(?<day>\d{2})/;

const match = path.match(pattern);
console.log(match.groups);

```

Sortie :

```bash
{resource: 'posts', year: '2024', month: '02', day: '22'}

```

Ici, chaque partie du chemin est capturée en utilisant des groupes de capture nommés, ce qui facilite l'accès à ceux-ci par leurs noms respectifs.

### Groupes non capturants :

Dans les expressions régulières, les groupes non capturants sont utilisés pour regrouper des parties d'un motif ensemble pour appliquer des quantificateurs ou des alternances, sans capturer la sous-chaîne correspondante. 

Pour créer un groupe non capturant, vous ajoutez `?:` au début des parenthèses. Ainsi, `/(?:\d)+/` est la version non capturante de l'exemple précédent. Le `?:` indique au moteur regex de ne pas capturer la sous-chaîne correspondante.

Voyons la différence entre les groupes capturants et non capturants avec un exemple :

```javascript
// groupe capturant
const regexWithCapture = /(\d{2})\/(\d{2})\/(\d{4})/;
const matchWithCapture = regexWithCapture.exec('02/26/2024');

console.log(matchWithCapture); // ["02/26/2024", "02", "26", "2024"]

```

```javascript
// groupe non capturant
const regexWithoutCapture = /(?:\d{2})\/(?:\d{2})\/(?:\d{4})/;
const matchWithoutCapture = regexWithoutCapture.exec('02/26/2024');

console.log(matchWithoutCapture); // ["02/26/2024"]

```

En résumé, les groupes non capturants `(?:pattern)` se comportent comme des groupes capturants réguliers `()` en termes de correspondance de motifs, mais ils ne stockent pas le texte correspondant en mémoire pour une récupération ultérieure. Cela les rend utiles lorsque vous n'avez pas besoin d'extraire des parties spécifiques du texte correspondant.

### Références arrière :

Les références arrière vous permettent de faire référence à des groupes capturés précédemment dans une expression régulière. Considérez-les comme des variables qui stockent des motifs correspondants. 

En JavaScript, la syntaxe pour une référence arrière est `\N`, où `N` est un entier représentant le numéro du groupe de capture.

Par exemple, considérons une chaîne avec un mot dupliqué "Lion" et nous voulons supprimer le mot dupliqué pour obtenir `'Lion is the King'` :

```javascript
const s = 'Lion Lion is the King';

```

* Tout d'abord, nous faisons correspondre un mot en utilisant `\w+\s+`.
* Ensuite, nous créons un groupe de capture pour capturer le mot en utilisant `(\w+)\s+`.
* Ensuite, nous utilisons une référence arrière (`\1`) pour faire référence au premier groupe de capture.
* Enfin, nous remplaçons toute la correspondance par le premier groupe de capture en utilisant `String.replace()`.

```javascript
const pattern = /(\w+)\s+\1/;
const result = s.replace(pattern, '$1');
console.log(result); // Sortie : 'Lion is the King'

```

### Alternance Regex :

L'alternance Regex est une fonctionnalité qui vous permet de faire correspondre différents motifs dans une seule expression régulière. Elle fonctionne de manière similaire à l'opérateur logique OR. Dans les regex, vous utilisez le symbole pipe `|` pour désigner l'alternance, où vous pouvez faire correspondre soit A soit B.

```
A | B // Cela signifie que vous pouvez faire correspondre soit le motif A soit le motif B.
```

Maintenant, explorons quelques applications pratiques de l'alternance regex :

**Correspondance de chaîne de temps au format hh:mm** : Supposons que nous voulons faire correspondre des chaînes de temps au format hh:mm, où hh représente les heures et mm représente les minutes. Une expression régulière de base pour faire correspondre ce format serait `/\d{2}:\d{2}/`. 

Cependant, ce motif de base fait correspondre des heures invalides comme "99:99". Pour nous assurer que nous faisons correspondre des heures valides (heures allant de 00 à 23 et minutes allant de 00 à 59), nous devons affiner notre regex en utilisant l'alternance.

Pour faire correspondre des heures valides (00 à 23), nous pouvons utiliser le motif suivant :

* `[01]\d` correspond aux nombres de 00 à 19.
* `2[0-3]` correspond aux nombres de 20 à 23.

Ainsi, le motif pour les heures devient `[01]\d|2[0-3]`.

Pour faire correspondre des minutes valides (00 à 59), nous pouvons utiliser le motif `[0-5]\d`.

Maintenant, nous pouvons combiner les motifs d'heure et de minute en utilisant l'alternance pour obtenir le motif regex final :

`/([01]\d|2[0-3]):[0-5]\d/g`

Dans ce motif :

* `([01]\d|2[0-3])` correspond aux heures valides.
* `:` correspond au deux-points.
* `[0-5]\d` correspond aux minutes valides.

Ce motif regex garantit que nous ne faisons correspondre que des chaînes de temps valides au format `hh:mm`. Exemple :

```javascript
const timeString = '07:23 33:71 21:17 25:81';
const pattern = /([01]\d|2[0-3]):[0-5]\d/g;
const matches = timeString.match(pattern);

console.log(matches);

```

**Sortie attendue** :

```
['07:23', '21:17']

```

## Lookahead et Lookbehind dans Regex

### Lookahead :

Le lookahead dans les expressions régulières permet de faire correspondre un motif (X) uniquement s'il est suivi d'un autre motif spécifique (Y). La syntaxe est `X(?=Y)`, où :

* **X** est le motif que vous voulez faire correspondre.
* **(?=Y)** est l'assertion de lookahead indiquant que `X` doit être suivi par `Y`.

**Exemple** : Supposons que nous avons une chaîne décrivant diverses distances, et nous voulons identifier les nombres suivis des unités "miles" mais pas "kilometers". Nous pouvons utiliser le lookahead dans un motif regex :

```javascript
const dist = "He ran 5 miles, but not 10 kilometers.";

const regex = /\d+(?=\s*miles)/g;

console.log(dist.match(regex)); // Sortie : ["5"]

```

**Plusieurs Lookaheads** : Il est possible d'avoir plusieurs lookaheads dans une expression régulière en utilisant la syntaxe `X(?=Y)(?=Z)`. Cela nous permet d'imposer plusieurs conditions pour la correspondance.

**Exemple** : Supposons que nous voulons faire correspondre des chaînes qui contiennent à la fois "foo" et "bar", mais dans n'importe quel ordre :

```javascript
const regex = /(?=.*foo)(?=.*bar)/;

console.log(regex.test("foobar")); // true
console.log(regex.test("barfoo")); // true
console.log(regex.test("foo"));    // false
console.log(regex.test("bar"));    // false
```

### Negative Lookaheads :

Pour nier un lookahead, utilisez un negative lookahead avec la syntaxe `(?!Y)`, où le moteur regex fait correspondre X uniquement s'il n'est pas suivi par Y.

**Exemple** : Supposons que nous voulons faire correspondre des nombres mais pas s'ils sont suivis par "miles" :

```javascript
const text = "He ran 5 miles, but not 10 kilometers.";

const regex = /\d+(?!\s*miles)/g;

console.log(text.match(regex)); // Sortie : ["10"]

```

### Lookbehind :

Les lookbehinds fournissent un moyen de faire correspondre des motifs en fonction de ce qui les précède, essentiellement en faisant correspondre un élément s'il y a un autre élément spécifique avant lui.

**Exemple** : Supposons que nous avons une chaîne contenant des prix, et nous voulons faire correspondre des nombres précédés du symbole de devise "$" mais pas précédés de " ". Nous pouvons utiliser un lookbehind dans un motif regex

```javascript
const priceString = "The price is $100, but \u20ac200.";

const regex = /(?<=\$)\d+/g;

console.log(priceString.match(regex)); // Sortie : ["100"]

```

**Explication** : `(?<=\$)` correspond à un élément s'il y a une chaîne littérale "$" avant lui. La barre oblique inverse `\` est utilisée pour échapper le caractère spécial "$", le traitant comme un caractère littéral.

### Negative Lookbehind :

Les negative lookbehinds vous permettent de faire correspondre un motif uniquement s'il n'est pas précédé d'un motif spécifique. Cela est utile pour exclure certains motifs des correspondances en fonction de ce qui les précède. 

Exemple : Supposons que nous avons une chaîne contenant divers prix dans différentes devises, et nous voulons faire correspondre les nombres non précédés du symbole de devise "$". Nous pouvons utiliser un negative lookbehind dans un motif regex :

```javascript
const priceString = "The price is $50, but not \u20ac100.";

const regex = /(?<!\$)\b\d+\b/g;

console.log(priceString.match(regex)); // Sortie : ["100"]

```

**Explication :** `(?<!\$)` est la syntaxe du negative lookbehind, qui correspond au motif suivant uniquement s'il n'est pas précédé de la chaîne littérale "$".

## Exemples pratiques et cas d'utilisation de Regex

Maintenant, explorons quelques exemples pratiques d'utilisation des expressions régulières dans les applications JavaScript pour résoudre des problèmes courants et effectuer des tâches de manipulation de texte.

### Vérification de la force du mot de passe :

Vous pouvez utiliser des expressions régulières pour imposer des exigences de force de mot de passe, telles que la longueur minimale et la présence de caractères spéciaux.

```javascript
function checkPasswordStrength(password) {
    let pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/;
    return pattern.test(password);
}

console.log(checkPasswordStrength("Passw0rd!"));    // Sortie : true
console.log(checkPasswordStrength("weakpassword")); // Sortie : false

```

Voici ce que fait ce motif :

* `(?=.*\d)` : Exige au moins un chiffre.
* `(?=.*[a-z])` : Exige au moins une lettre minuscule.
* `(?=.*[A-Z])` : Exige au moins une lettre majuscule.
* `(?=.*[!@#$%^&*])` : Exige au moins un caractère spécial.
* `.{8,}` : Exige une longueur minimale de 8 caractères.

### Fonction de validation d'email :

La validation d'email est cruciale pour garantir l'intégrité et la sécurité des données dans les applications web. Avec les méthodes regex, nous pouvons facilement implémenter des mécanismes de validation d'email robustes.

```javascript
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

console.log(validateEmail("example@email.com")); // true
console.log(validateEmail("invalid-email"));      // false

```

Voici ce que fait ce motif :

* `^` : Assertion du début de la chaîne.
* `[^\s@]+` : Correspond à un ou plusieurs caractères qui ne sont pas des espaces blancs ou '@'.
* `@` : Correspond au symbole '@'.
* `[^\s@]+` : Correspond à un ou plusieurs caractères qui ne sont pas des espaces blancs ou '@'.
* `\.` : Correspond au symbole '.' (échappé car '.' a une signification spéciale dans RegEx).
* `[^\s@]+` : Correspond à un ou plusieurs caractères qui ne sont pas des espaces blancs ou '@'.
* `$` : Assertion de la fin de la chaîne.

### Fonction de formatage de numéro de téléphone :

Le formatage des numéros de téléphone améliore l'expérience utilisateur et la lisibilité dans les applications qui impliquent la saisie et l'affichage de numéros de téléphone.  

En définissant un motif regex qui correspond aux composants du numéro de téléphone, nous pouvons facilement formater les numéros de téléphone dans un motif souhaité en utilisant la méthode `replace()`.

```javascript
function formatPhoneNumber(phoneNumber) {
    const phoneRegex = /(\d{3})(\d{3})(\d{4})/;
    return phoneNumber.replace(phoneRegex, "($1) $2-$3");
}

const formattedNumber = formatPhoneNumber("9876543210");
console.log(formattedNumber); // (987) 654-3210

```

Dans la méthode `replace()`, `$1`, `$2`, et `$3` représentent les groupes capturés dans le motif RegEx, correspondant aux trois ensembles de chiffres dans le numéro de téléphone.

## Conseils et meilleures pratiques pour utiliser les expressions régulières

#### 1. Comprendre la syntaxe des expressions régulières :

Comprendre la syntaxe et les métacaractères des expressions régulières pour une utilisation efficace.

#### 2. Tester les expressions régulières :

Les expressions régulières peuvent parfois se comporter de manière inattendue en raison de motifs complexes ou de caractères spéciaux. Testes toujours vos expressions régulières avec différentes chaînes d'entrée pour vous assurer qu'elles se comportent comme prévu dans divers scénarios.

#### 3. Optimiser les performances :

Envisagez d'optimiser vos expressions régulières pour les performances en simplifiant les motifs ou en utilisant des alternatives plus efficaces lorsque cela est possible.

#### 4. Utiliser les méthodes intégrées :

JavaScript fournit des méthodes intégrées comme `String.prototype.match()`, `String.prototype.replace()`, et `String.prototype.split()` pour les tâches courantes de manipulation de chaînes. Évaluez si ces méthodes peuvent accomplir votre tâche sans avoir besoin d'expressions régulières.

#### 5. Commenter vos expressions régulières :

Ajoutez des commentaires dans votre regex en utilisant la syntaxe `(?#comment)` pour expliquer les parties de motifs complexes. Exemple :

```javascript
const regex = /(\d{3})-(\d{3})-(\d{4})\s(?# Faire correspondre un numéro de téléphone au format XXX-XXX-XXXX)/;

```

#### 6. Décomposer les motifs complexes :

Si votre expression régulière devient trop complexe à comprendre ou à maintenir, envisagez de la décomposer en parties plus petites et plus gérables. Utilisez des variables pour stocker les composants individuels du motif et combinez-les selon les besoins.

#### 7. Utiliser les ressources en ligne et continuer à pratiquer :

Il existe plusieurs ressources et outils en ligne pour tester et apprendre les expressions régulières. Des sites comme [Regex101](https://regex101.com/) et [RegExr](https://regexr.com/) fournissent des plateformes interactives pour tester et déboguer les expressions régulières. Utilisez également des tutoriels et de la documentation en ligne pour apprendre les concepts regex.

La documentation MDN Web Docs contient un guide utile sur les [Expressions régulières ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions). Et voici un guide de démarrage rapide sur les expressions régulières en JavaScript : [Tutoriel RegExp](https://www.freecodecamp.org/news/a-quick-and-simple-guide-to-javascript-regular-expressions-48b46a68df29/).

## Conclusion

Les expressions régulières sont des outils polyvalents pour la correspondance de motifs et la manipulation en JavaScript. 

En comprenant leurs méthodes, leurs fonctionnalités avancées et leur utilisation avec des drapeaux, en exploitant les ressources en ligne et les outils de débogage, vous pouvez les apprendre et les appliquer efficacement dans divers scénarios, allant de la simple correspondance de motifs aux tâches complexes de traitement de texte.