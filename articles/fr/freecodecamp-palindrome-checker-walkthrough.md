---
title: Un guide du projet Vérificateur de Palindromes de FreeCodeCamp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-11T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/freecodecamp-palindrome-checker-walkthrough
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/Palindrome-Checker-thumbnail.png
tags:
- name: algorithms
  slug: algorithms
- name: coding interview
  slug: coding-interview
- name: data structures
  slug: data-structures
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Interviewing
  slug: interviewing
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
seo_title: Un guide du projet Vérificateur de Palindromes de FreeCodeCamp
seo_desc: 'By Yazeed Bzadough

  Project 1 from JavaScript Algos and DS Certification.

  This is the blog version of my walkthrough. If you prefer video here is the YouTube
  video link.

  The Challenge


  Write a function called palindrome that takes a string, str. If st...'
---

Par Yazeed Bzadough

Projet 1 de la Certification JavaScript Algos et DS.

Il s'agit de la version blog de mon guide. Si vous préférez une vidéo [voici le lien YouTube](https://youtu.be/XV5OCibNpLI).

## Le Défi
![project-1-intro-screenshot](https://www.freecodecamp.org/news/content/images/2019/09/project-1-intro-screenshot.png)

Écrivez une fonction appelée `palindrome` qui prend une chaîne de caractères, `str`. Si `str` est un palindrome, retournez `true`, sinon retournez `false`.

## Qu'est-ce qu'un Palindrome ?
Un palindrome est un mot qui se lit de la même manière à l'endroit et à l'envers. Voici quelques exemples :

* Eye
* Racecar
* A Man, A Plan, A Canal – Panama!

Que vous les lisiez de gauche à droite ou de droite à gauche, vous obtenez la même séquence de caractères. **Nous ignorerons la ponctuation comme les virgules, les points, les points d'interrogation, les points d'exclamation et la casse.**

## Étape 0 - Éloignez-vous du Code
J'aime garder cela à l'esprit lors de tout entretien ou problème que je dois résoudre au travail. Se précipiter dans le code en premier est généralement une stratégie perdante, car maintenant vous devez considérer la syntaxe tout en essayant de résoudre le problème dans votre tête.

> Le code devrait venir en dernier

Ne laissez pas vos nerfs prendre le dessus. Au lieu de vous acharner frénétiquement sur une solution et d'élever votre pression artérielle, prenez une profonde inspiration et essayez de l'écrire sur un tableau blanc ou dans un cahier.

Une fois que vous avez réfléchi à une solution, le code vient facilement. Tout le travail difficile se passe dans votre esprit et vos notes, pas sur le clavier.

## Étape 1 - Uniformiser la Casse
Un palindrome est valide que sa casse se lise de la même manière à l'endroit ou à l'envers. Donc "Racecar" est valide même si techniquement il s'écrit "racecaR" à l'envers.

Pour nous prémunir contre tout problème de casse, j'ajouterai un commentaire disant que nous mettrons tout en minuscules.

Voici mon code jusqu'à présent (remarquez que je n'ai encore écrit aucun vrai code).

```js
function palindrome(str) {
  // 1) Mettre l'entrée en minuscules
}



palindrome("eye");

```

## Étape 2 - Supprimer les Caractères Non Alphanumériques
Tout comme le scénario de la casse, un palindrome est valide même si la ponctuation et les espaces ne sont pas cohérents dans les deux sens.

Par exemple, "A Man, A Plan, A Canal – Panama!" est valide car nous l'examinons sans aucune marque ou espace. Si vous faites cela et mettez tout en minuscules, cela devient ceci.

```js
"A Man, A Plan, A Canal – Panama!"

// tout mettre en minuscules
// supprimer les caractères non alphanumériques

"amanaplanacanalpanama"
```

Ce qui se lit de la même manière à l'endroit et à l'envers.

### Que signifie alphanumérique ?
Cela signifie "lettres et chiffres", donc tout ce qui va de a-z et 0-9 est un caractère alphanumérique. Afin d'examiner correctement notre entrée, les caractères non alphanumériques (espaces, ponctuation, etc.) doivent être supprimés.

Voici notre pseudocode mis à jour.

```js
function palindrome(str) {
  // 1) Mettre l'entrée en minuscules
  // 2) Supprimer les caractères non alphanumériques
}



palindrome("eye");

```

## Étape 3 - Comparer la Chaîne à son Inverse
Une fois notre chaîne correctement nettoyée, nous pouvons la retourner et voir si elle se lit de la même manière.

Je pense à une comparaison de ce type

```js
return string === reversedString
```

J'utilise le triple égal (`===`) pour la comparaison en JavaScript. Si les deux chaînes sont identiques, c'est un palindrome et nous retournons `true` ! Sinon, nous retournons `false`.

Voici notre pseudocode mis à jour.

```js
function palindrome(str) {
  // 1) Mettre l'entrée en minuscules
  // 2) Supprimer les caractères non alphanumériques
  // 3) return string === reversedString
}



palindrome("eye");

```

## Exécution de l'Étape 1 - Minuscules
Il s'agit de l'étape la plus facile. Si vous n'êtes pas sûr de la manière de mettre quelque chose en minuscules en JavaScript, une rapide recherche Google devrait vous mener à la méthode `toLowerCase`.

Il s'agit d'une méthode disponible sur toutes les chaînes, nous pouvons donc l'utiliser pour mettre notre entrée en minuscules avant de faire autre chose.

Je vais stocker la version en minuscules dans une variable appelée `alphanumericOnly` car nous allons éventuellement supprimer les caractères alphanumériques également.

```js
function palindrome(str) {
  // 1) Mettre l'entrée en minuscules
  const alphanumericOnly = str.toLowerCase();
  
  // 2) Supprimer les caractères non alphanumériques
  // 3) return string === reversedString
}



palindrome("eye");

```

## Exécution de l'Étape 2 - Uniquement Alphanumérique
Nous devons approfondir un peu ici, car il s'agit de l'étape la plus difficile. Comment allons-nous exactement purifier une chaîne de ses caractères non alphanumériques ?

### La méthode .match
Tout comme `toLowerCase`, toutes les chaînes supportent une méthode appelée `match`. Elle prend un paramètre indiquant quel(s) caractère(s) vous souhaitez rechercher dans une chaîne donnée.

Prenons mon nom comme exemple.

```js
myName = 'yazeed';

myName.match('e');
// ["e", index: 3, input: "yazeed", groups: undefined]
```

Comme vous pouvez le voir, `.match` retourne un tableau avec certaines informations. La partie qui nous intéresse est le premier élément, `'e'`. C'est la correspondance que nous avons trouvée dans la chaîne `'yazeed'`.

Mais mon nom a deux e ! Comment pouvons-nous faire correspondre l'autre ?

### Expressions Régulières (Regex)
Le premier paramètre de la méthode `.match` peut être une _expression régulière_.

> Expression Régulière - Une séquence de caractères qui définit un motif de recherche. Également connue sous le nom de "Regex".

Au lieu de guillemets pour une chaîne, placez votre paramètre entre des barres obliques.

```js
myName = 'yazeed';

myName.match(/e/);
// ["e", index: 3, input: "yazeed", groups: undefined]
```

Nous obtenons le même résultat, alors qui s'en soucie ? Eh bien, regardez ceci, regex nous permet d'ajouter des _flags_.

> Flag Regex - Un indicateur qui indique à Regex de faire quelque chose de spécial.

```js
myName = 'yazeed';

myName.match(/e/g);
// ^^ Remarquez le petit g maintenant ^^
// ["e", "e"]
```

Nous avons obtenu tous les e ! Si vous essayez un a ou un z, vous obtenez un tableau d'une seule correspondance. Cela a du sens.

```js
myName.match(/a/g);
// ["a"]

myName.match(/z/g);
// ["z"]
```

### Trouver tous les caractères alphanumériques
Donc, regex ne fait pas seulement correspondre des motifs, mais il peut correspondre à _plusieurs_ du même type de motif ! Cela semble parfait pour la prochaine étape de notre algorithme.

Si vous cherchez un peu sur Google, voici le regex que vous pourriez trouver pour correspondre à tous les caractères alphanumériques.

```js
/[a-z0-9]/g
```

Vous regardez la définition de _alphanumérique_. Ce regex peut être divisé en 3 parties.

1. Un ensemble de caractères `[]` - correspond à n'importe quel caractère entre ces crochets. ![character-sets](https://www.freecodecamp.org/news/content/images/2019/09/character-sets.png)
2. `a-z` - correspond à toutes les lettres minuscules ![a-z](https://www.freecodecamp.org/news/content/images/2019/09/a-z.png)
3. `0-9` - correspond à tous les nombres ![0-9](https://www.freecodecamp.org/news/content/images/2019/09/0-9.png)

L'exécuter sur `myName` retourne un tableau de chaque lettre.
```js
myName = 'yazeed';

myName.match(/[a-z0-9]/g);
// ["y", "a", "z", "e", "e", "d"]
```

Essayons-le avec l'un des cas de test du projet. Que dire de celui-ci qui est censé être un palindrome ?

```js
crazyInput = '0_0 (: /-\ :) 0-0';

crazyInput.match(/[a-z0-9]/g);
// ["0", "0", "0", "0"]
```

Wow, sans les caractères fous, ce n'est que quatre zéros. Oui, c'est un palindrome ! Je vais mettre à jour notre code.

```js
function palindrome(str) {
  const alphanumericOnly = str
        // 1) Mettre l'entrée en minuscules
        .toLowerCase()
        // 2) Supprimer les caractères non alphanumériques
        .match(/[a-z0-9]/g);
  
  // 3) return string === reversedString
}



palindrome("eye");

```

## Exécution de l'Étape 3 - Comparer la Chaîne à son Inverse
Rappelez-vous que `.match` retourne un _tableau_ de correspondances. Comment pouvons-nous utiliser ce tableau pour comparer notre chaîne nettoyée à son inverse ?

### Array.reverse
La méthode `reverse`, fidèle à son nom, inverse les éléments d'un tableau.

```js
[1, 2, 3].reverse();
// [3, 2, 1]
```

Cela semble assez utile ! Après avoir fait correspondre tous les caractères alphanumériques, nous pouvons inverser ce tableau et voir si tout s'aligne encore.

Mais comparer des tableaux n'est pas aussi simple que comparer des chaînes, alors comment pouvons-nous transformer ce tableau de correspondances en une chaîne ?

### Array.join
La méthode `join` assemble les éléments de votre tableau en une chaîne, en prenant optionnellement un _séparateur_.

Le séparateur est le premier paramètre, vous n'avez pas besoin de le fournir. Il va essentiellement "stringifier" votre tableau.

```js
[1, 2, 3].join();
// "1,2,3"
```

Si vous le fournissez, le séparateur va entre chaque élément.

```js
[1, 2, 3].join('my separator');
// "1my separator2my separator3"

[1, 2, 3].join(',');
// "1,2,3"

[1, 2, 3].join(', ');
// "1, 2, 3"

[1, 2, 3].join('sandwich');
// "1sandwich2sandwich3"
```

Voyons comment cela s'intègre dans notre algorithme.

```js
'Ra_Ce_Ca_r   -_-'
    .toLowerCase()
    .match(/[a-z0-9]/g)
    .join('');

// "racecar"
```

Voyez-vous comment faire tout cela recrée simplement la chaîne originale sans ponctuation ou casse mixte ?

Et si nous l'inversions ?

```js
'Ra_Ce_Ca_r   -_-'
    .toLowerCase()
    .match(/[a-z0-9]/g)
    // la retourner
    .reverse()
    .join('');

// "racecar"
```

C'est un palindrome ! Mon nom ne serait pas un palindrome.

```js
'yazeed'
    .toLowerCase()
    .match(/[a-z0-9]/g)
    // la retourner
    .reverse()
    .join('');

// "deezay"
```

Il semble que nous ayons notre solution. Voyons le code final.

## Le Code Final
```js
function palindrome(str) {
    const alphanumericOnly = str
        // 1) Mettre l'entrée en minuscules
        .toLowerCase()
        // 2) Supprimer les caractères non alphanumériques
        .match(/[a-z0-9]/g);
        
    // 3) return string === reversedString
    return alphanumericOnly.join('') ===
        alphanumericOnly.reverse().join('');
}



palindrome("eye");

```

Entrez cela et exécutez les tests, et c'est bon !

![all-tests-passed](https://www.freecodecamp.org/news/content/images/2019/09/all-tests-passed.png)

## Résumé
1. Mettre l'entrée en minuscules via `str.toLowerCase()` ;
2. Faire correspondre tous les caractères alphanumériques en utilisant une expression régulière via `str.match(/[a-z0-9]/g)`.
3. Utiliser `Array.reverse` et `Array.join` sur les correspondances alphanumériques pour comparer l'original avec son inverse. S'ils sont identiques, nous obtenons `true`, sinon nous obtenons `false` !

## Merci d'avoir lu
Si vous souhaitez une vidéo avec encore plus de détails, [voici à nouveau la version YouTube](https://youtu.be/XV5OCibNpLI) !

Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com</a>. Et s'il vous plaît, faites-moi savoir ce que vous aimeriez voir d'autre ! [Mes DM sont ouverts sur Twitter.](https://twitter.com/yazeedBee)

À la prochaine fois !