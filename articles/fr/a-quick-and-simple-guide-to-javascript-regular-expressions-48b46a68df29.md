---
title: Un guide rapide et simple des expressions régulières JavaScript
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-05-09T21:27:52.000Z'
originalURL: https://freecodecamp.org/news/a-quick-and-simple-guide-to-javascript-regular-expressions-48b46a68df29
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mMTMvUSrCvoImD8N.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un guide rapide et simple des expressions régulières JavaScript
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Introduction to Regular Expressions

  A regular expression (also called regex for short) is a fast way to work with strings
  of text.

  By formulating a regular expression with a special s...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

### Introduction aux expressions régulières

Une expression régulière (aussi appelée **regex** en abrégé) est un moyen rapide de travailler avec des chaînes de texte.

En formulant une expression régulière avec une syntaxe spéciale, vous pouvez :

* **rechercher du texte** dans une chaîne
* **remplacer des sous-chaînes** dans une chaîne
* et **extraire des informations** d'une chaîne

Presque tous les langages de programmation disposent d'une implémentation des expressions régulières. Il existe de petites différences entre chaque implémentation, mais les concepts généraux s'appliquent presque partout.

Les expressions régulières remontent aux années 1950, lorsqu'elles ont été formalisées comme un motif de recherche conceptuel pour les algorithmes de traitement de chaînes.

Implémentées dans des outils UNIX comme grep, sed, et dans des éditeurs de texte populaires, les regex ont gagné en popularité. Elles ont été introduites dans le langage de programmation Perl, et plus tard dans de nombreux autres langages.

JavaScript, avec Perl, est l'un des langages de programmation qui a un support pour les expressions régulières directement intégré dans le langage.

### Difficile mais utile

Les expressions régulières peuvent sembler un absolu non-sens pour le débutant, et souvent aussi pour le développeur professionnel, si vous n'investissez pas le temps nécessaire pour les comprendre.

Les expressions régulières cryptiques sont **difficiles à écrire**, **difficiles à lire**, et **difficiles à maintenir/modifier**.

Mais parfois une expression régulière est **le seul moyen sensé** d'effectuer une manipulation de chaîne, donc c'est un outil très précieux dans votre poche.

Ce tutoriel vise à vous introduire aux expressions régulières JavaScript de manière simple, et à vous donner toutes les informations pour lire et créer des expressions régulières.

La règle générale est que **les expressions régulières simples sont simples à lire et à écrire**, tandis que **les expressions régulières complexes peuvent rapidement devenir un désordre** si vous ne maîtrisez pas profondément les bases.

### À quoi ressemble une expression régulière ?

En JavaScript, une expression régulière est un **objet**, qui peut être défini de deux manières.

La première est en instanciant un **nouvel objet RegExp** en utilisant le constructeur :

```js
const re1 = new RegExp('hey')
```

La seconde est en utilisant la forme **littérale d'expression régulière** :

```js
const re1 = /hey/
```

Vous savez que JavaScript a des **littéraux d'objet** et des **littéraux de tableau** ? Il a aussi des **littéraux regex**.

Dans l'exemple ci-dessus, `hey` est appelé le **motif**. Dans la forme littérale, il est délimité par des barres obliques, tandis qu'avec le constructeur d'objet, ce n'est pas le cas.

C'est la première différence importante entre les deux formes, mais nous en verrons d'autres plus tard.

### Comment cela fonctionne-t-il ?

L'expression régulière que nous avons définie comme `re1` ci-dessus est très simple. Elle recherche la chaîne `hey`, sans aucune limitation. La chaîne peut contenir beaucoup de texte, et `hey` au milieu, et la regex est satisfaite. Elle pourrait aussi contenir juste `hey`, et la regex serait satisfaite également.

C'est assez simple.

Vous pouvez tester la regex en utilisant `RegExp.test(String)`, qui retourne un booléen :

```js
re1.test('hey') // ✅
re1.test('blablabla hey blablabla') // ✅
re1.test('he') // ❌
re1.test('blablabla') // ❌

```

Dans l'exemple ci-dessus, nous avons simplement vérifié si `"hey"` satisfait le motif d'expression régulière stocké dans `re1`.

C'est le plus simple qu'il soit, mais vous connaissez déjà beaucoup de concepts sur les regex.

### Ancrage

```js
/hey/
```

correspond à `hey` où qu'il soit placé dans la chaîne.

Si vous voulez faire correspondre des chaînes qui **commencent** par `hey`, utilisez l'opérateur `^` :

```js
/^hey/.test('hey') // ✅
/^hey/.test('bla hey') // ❌

```

Si vous voulez faire correspondre des chaînes qui **se terminent** par `hey`, utilisez l'opérateur `$` :

```js
/hey$/.test('hey') // ✅
/hey$/.test('bla hey') // ✅
/hey$/.test('hey you') // ❌

```

Combinez ceux-ci, et faites correspondre des chaînes qui correspondent exactement à `hey`, et juste cette chaîne :

```js
/^hey$/.test('hey') // ✅

```

Pour faire correspondre une chaîne qui commence par une sous-chaîne et se termine par une autre, vous pouvez utiliser `**.***`, qui correspond à n'importe quel caractère répété 0 ou plusieurs fois :

```js
/^hey.*joe$/.test('hey joe') // ✅
/^hey.*joe$/.test('heyjoe') // ✅
/^hey.*joe$/.test('hey how are you joe') // ✅
/^hey.*joe$/.test('hey joe!') // ❌

```

### Correspondre à des éléments dans des plages

Au lieu de faire correspondre une chaîne particulière, vous pouvez choisir de faire correspondre n'importe quel caractère dans une plage, comme :

```js
/[a-z]/ // a, b, c, ... , x, y, z
/[A-Z]/ // A, B, C, ... , X, Y, Z
/[a-c]/ // a, b, c
/[0-9]/ // 0, 1, 2, 3, ... , 8, 9

```

Ces regex correspondent à des chaînes qui contiennent au moins l'un des caractères de ces plages :

```js
/[a-z]/.test('a') // ✅
/[a-z]/.test('1') // ❌
/[a-z]/.test('A') // ❌
/[a-c]/.test('d') // ❌
/[a-c]/.test('dc') // ✅

```

Les plages peuvent être combinées :

```js
/[A-Za-z0-9]/

/[A-Za-z0-9]/.test('a') // ✅
/[A-Za-z0-9]/.test('1') // ✅
/[A-Za-z0-9]/.test('A') // ✅
```

### Correspondre à un élément de plage plusieurs fois

Vous pouvez vérifier si une chaîne contient un et un seul caractère dans une plage en utilisant le caractère `-` :

```js
/^[A-Za-z0-9]$/

/^[A-Za-z0-9]$/.test('A') // ✅
/^[A-Za-z0-9]$/.test('Ab') // ❌
```

### Nier un motif

Le caractère `^` au début d'un motif l'ancre au début d'une chaîne.

Utilisé à l'intérieur d'une plage, il la **nie**, donc :

```js
/[^A-Za-z0-9]/.test('a') // ❌
/[^A-Za-z0-9]/.test('1') // ❌
/[^A-Za-z0-9]/.test('A') // ❌
/[^A-Za-z0-9]/.test('@') // ✅

```

* `**\d**` correspond à n'importe quel chiffre, équivalent à `[0-9]`
* `**\D**` correspond à n'importe quel caractère qui n'est pas un chiffre, équivalent à `[^0-9]`
* `**\w**` correspond à n'importe quel caractère alphanumérique, équivalent à `[A-Za-z0-9]`
* `**\W**` correspond à n'importe quel caractère non alphanumérique, équivalent à `[^A-Za-z0-9]`
* `**\s**` correspond à n'importe quel caractère d'espace : espaces, tabulations, nouvelles lignes et espaces Unicode
* `**\S**` correspond à n'importe quel caractère qui n'est pas un espace
* `**\0**` correspond à null
* `**\n**` correspond à un caractère de nouvelle ligne
* `**\t**` correspond à un caractère de tabulation
* `**\uXXXX**` correspond à un caractère unicode avec le code XXXX (nécessite le drapeau `u`)
* `**.**` correspond à n'importe quel caractère qui n'est pas un caractère de nouvelle ligne (par exemple, `\n`) (sauf si vous utilisez le drapeau `s`, expliqué plus tard)
* `**[^]**` correspond à n'importe quel caractère, y compris les caractères de nouvelle ligne. C'est utile sur les chaînes multilingues.

### Choix d'expressions régulières

Si vous voulez rechercher une chaîne **ou** une autre, utilisez l'opérateur `|`.

```js
/hey|ho/.test('hey') // ✅
/hey|ho/.test('ho') // ✅

```

### Quantificateurs

Disons que vous avez cette regex qui vérifie si une chaîne a un chiffre, et rien d'autre :

```js
/^\d$/

```

Vous pouvez utiliser **le quantificateur `?`** pour le rendre optionnel, nécessitant ainsi zéro ou un :

```js
/^\d?$/

```

mais que faire si vous voulez faire correspondre plusieurs chiffres ?

Vous pouvez le faire de 4 manières, en utilisant `+`, `*`, `{n}` et `{n,m}`. Examinons ceux-ci un par un.

### `+`

Correspond à un ou plusieurs (>=1) éléments :

```js
/^\d+$/

/^\d+$/.test('12') // ✅
/^\d+$/.test('14') // ✅
/^\d+$/.test('144343') // ✅
/^\d+$/.test('') // ❌
/^\d+$/.test('1a') // ❌

```

### `*`

Correspond à 0 ou plusieurs (>= 0) éléments :

```js
/^\d+$/

/^\d*$/.test('12') // ✅
/^\d*$/.test('14') // ✅
/^\d*$/.test('144343') // ✅
/^\d*$/.test('') // ✅
/^\d*$/.test('1a') // ❌

```

### `{n}`

Correspond exactement à `n` éléments :

```js
/^\d{3}$/

/^\d{3}$/.test('123') // ✅
/^\d{3}$/.test('12') // ❌
/^\d{3}$/.test('1234') // ❌
/^[A-Za-z0-9]{3}$/.test('Abc') // ✅

```

### `{n,m}`

Correspond entre `n` et `m` fois :

```js
/^\d{3,5}$/

/^\d{3,5}$/.test('123') // ✅
/^\d{3,5}$/.test('1234') // ✅
/^\d{3,5}$/.test('12345') // ✅
/^\d{3,5}$/.test('123456') // ❌

```

`m` peut être omis pour avoir une fin ouverte, donc vous avez au moins `n` éléments :

```js
/^\d{3,}$/

/^\d{3,}$/.test('12') // ❌
/^\d{3,}$/.test('123') // ✅
/^\d{3,}$/.test('12345') // ✅
/^\d{3,}$/.test('123456789') // ✅

```

### Éléments optionnels

Suivre un élément avec `?` le rend optionnel :

```js
/^\d{3}\w?$/

/^\d{3}\w?$/.test('123') // ✅
/^\d{3}\w?$/.test('123a') // ✅
/^\d{3}\w?$/.test('123ab') // ❌

```

### Groupes

En utilisant des parenthèses, vous pouvez créer des groupes de caractères : `(...)`

Cet exemple correspond exactement à 3 chiffres suivis d'un ou plusieurs caractères alphanumériques :

```js
/^(\d{3})(\w+)$/

/^(\d{3})(\w+)$/.test('123') // ❌
/^(\d{3})(\w+)$/.test('123s') // ✅
/^(\d{3})(\w+)$/.test('123something') // ✅
/^(\d{3})(\w+)$/.test('1234') // ✅

```

Les caractères de répétition placés après une parenthèse de fermeture de groupe font référence au groupe entier :

```js
/^(\d{2})+$/

/^(\d{2})+$/.test('12') // ✅
/^(\d{2})+$/.test('123') // ❌
/^(\d{2})+$/.test('1234') // ✅

```

### Groupes de capture

Jusqu'à présent, nous avons vu comment tester des chaînes et vérifier si elles contiennent un certain motif.

Une fonctionnalité très intéressante des expressions régulières est la capacité à **capturer des parties d'une chaîne**, et à les mettre dans un tableau.

Vous pouvez le faire en utilisant des Groupes, et en particulier des **Groupes de Capture**.

Par défaut, un Groupe est un Groupe de Capture. Maintenant, au lieu d'utiliser `RegExp.test(String)`, qui retourne simplement un booléen si le motif est satisfait, nous utilisons soit `String.match(RegExp)` soit `RegExp.exec(String)`.

Ils sont exactement les mêmes, et retournent un Array avec toute la chaîne correspondante dans le premier élément, puis chaque contenu de groupe correspondant.

Si il n'y a pas de correspondance, il retourne `null` :

```js
'123s'.match(/^(\d{3})(\w+)$/)
// Array [ "123s", "123", "s" ]

/^(\d{3})(\w+)$/.exec('123s')
// Array [ "123s", "123", "s" ]

'hey'.match(/(hey|ho)/)
// Array [ "hey", "hey" ]

/(hey|ho)/.exec('hey')
// Array [ "hey", "hey" ]

/(hey|ho)/.exec('ha!')
// null

```

Lorsque qu'un groupe est correspondant plusieurs fois, seule la dernière correspondance est mise dans le tableau de résultats :

```js
'123456789'.match(/(\d)+/)
// Array [ "123456789", "9" ]
```

### Groupes optionnels

Un groupe de capture peut être rendu optionnel en utilisant `(...)?`. Si il n'est pas trouvé, l'emplacement du tableau résultant contiendra `undefined` :

```js
/^(\d{3})(\s)?(\w+)$/.exec('123 s')
// Array [ "123 s", "123", " ", "s" ]

/^(\d{3})(\s)?(\w+)$/.exec('123s')
// Array [ "123s", "123", undefined, "s" ]

```

### Référence aux groupes correspondants

Chaque groupe qui est correspondant est assigné à un numéro. `$1` fait référence au premier, `$2` au second, et ainsi de suite. Cela sera utile lorsque nous parlerons plus tard du remplacement de parties d'une chaîne.

### Groupes de capture nommés

Ceci est une nouvelle fonctionnalité [ES2018](https://flaviocopes.com/ecmascript/).

Un groupe peut être assigné à un nom, plutôt que d'être simplement assigné à un emplacement dans le tableau résultant :

```js
const re = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/
const result = re.exec('2015-01-02')

// result.groups.year === '2015';
// result.groups.month === '01';
// result.groups.day === '02';

```

![Image](https://cdn-media-1.freecodecamp.org/images/O7t7h0vXGY1EDMe6jWKDV7K-K7QZskPzCcGs)

### Utilisation de match et exec sans groupes

Il y a une différence entre utiliser `match` et `exec` sans groupes : le premier élément dans le tableau n'est pas la chaîne correspondante entière, mais la correspondance directement :

```js
/hey|ho/.exec('hey')
// [ "hey" ]

/(hey).(ho)/.exec('hey ho')
// [ "hey ho", "hey", "ho" ]

```

### Groupes non capturants

Puisque par défaut les groupes sont des Groupes de Capture, vous avez besoin d'un moyen d'ignorer certains groupes dans le tableau résultant. Cela est possible en utilisant des **Groupes Non Capturants**, qui commencent par un `(?:...)` :

```js
'123s'.match(/^(\d{3})(?:\s)(\w+)$/)
// null

'123 s'.match(/^(\d{3})(?:\s)(\w+)$/)
// Array [ "123 s", "123", "s" ]

```

### Drapeaux

Vous pouvez utiliser les drapeaux suivants sur n'importe quelle expression régulière :

* `g` : correspond au motif plusieurs fois
* `i` : rend la regex insensible à la casse
* `m` : active le mode multilingue. Dans ce mode, `^` et `$` correspondent au début et à la fin de toute la chaîne. Sans cela, avec des chaînes multilingues, ils correspondent au début et à la fin de chaque ligne.
* `u` : active le support pour unicode (introduit dans ES6/ES2015)
* `s` : (nouveau dans [ES2018](https://flaviocopes.com/ecmascript/)) court pour **single line**, il fait en sorte que le `.` corresponde également aux caractères de nouvelle ligne.

Les drapeaux peuvent être combinés, et ils sont ajoutés à la fin de la chaîne dans les littéraux regex :

```js
/hey/ig.test('HEy') // ✅

```

ou en tant que second paramètre avec les constructeurs d'objets RegExp :

```js
new RegExp('hey', 'ig').test('HEy') // ✅

```

### Inspection d'une regex

Étant donné une regex, vous pouvez inspecter ses propriétés :

* `source` la chaîne de motif
* `multiline` vrai avec le drapeau `m`
* `global` vrai avec le drapeau `g`
* `ignoreCase` vrai avec le drapeau `i`
* `lastIndex`

```js
/^(\w{3})$/i.source // "^(\\d{3})(\\w+)$"
/^(\w{3})$/i.multiline // false
/^(\w{3})$/i.lastIndex // 0
/^(\w{3})$/i.ignoreCase // true
/^(\w{3})$/i.global // false

```

### Échappement

Ces caractères sont spéciaux :

* `\`
* `/`
* `[ ]`
* `( )`
* `{ }`
* `?`
* `+`
* `*`
* `|`
* `.`
* `^`
* `$`

Ils sont spéciaux car ce sont des caractères de contrôle qui ont une signification dans le motif d'expression régulière. Si vous voulez les utiliser à l'intérieur du motif comme caractères de correspondance, vous devez les échapper, en les précédant d'un antislash :

```js
/^\\$/
/^\^$/ // /^\^$/.test('^') ✅
/^\$$/ // /^\$$/.test('$') ✅
```

### Limites de chaîne

`\b` et `\B` vous permettent d'inspecter si une chaîne est au début ou à la fin d'un mot :

* `**\b**` correspond à un ensemble de caractères au début ou à la fin d'un mot
* `**\B**` correspond à un ensemble de caractères non au début ou à la fin d'un mot

Exemple :

```js
'I saw a bear'.match(/\bbear/) // Array ["bear"]
'I saw a beard'.match(/\bbear/) // Array ["bear"]
'I saw a beard'.match(/\bbear\b/) // null
'cool_bear'.match(/\bbear\b/) // null

```

### Remplacer, en utilisant des expressions régulières

Nous avons déjà vu comment vérifier si une chaîne contient un motif.

Nous avons également vu comment extraire des parties d'une chaîne dans un tableau, en correspondant à un motif.

Voyons comment **remplacer des parties d'une chaîne** en fonction d'un motif.

L'objet `String` en JavaScript a une méthode `replace()`, qui peut être utilisée sans expressions régulières pour effectuer un **remplacement unique** sur une chaîne :

```js
"Hello world!".replace('world', 'dog')
// Hello dog!

"My dog is a good dog!".replace('dog', 'cat')
// My cat is a good dog!

```

Cette méthode accepte également une expression régulière comme argument :

```js
"Hello world!".replace(/world/, 'dog') // Hello dog!

```

Utiliser le drapeau `g` est **la seule façon** de remplacer plusieurs occurrences dans une chaîne en JavaScript vanilla :

```js
"My dog is a good dog!".replace(/dog/g, 'cat') // My cat is a good cat!

```

Les Groupes nous permettent de faire des choses plus fantaisistes, comme déplacer des parties d'une chaîne :

```js
"Hello, world!".replace(/(\w+), (\w+)!/, '$2: $1!!!') // "world: Hello!!!"

```

Au lieu d'utiliser une chaîne, vous pouvez utiliser une fonction, pour faire des choses encore plus fantaisistes. Elle recevra un certain nombre d'arguments comme celui retourné par `String.match(RegExp)` ou `RegExp.exec(String)`, avec un nombre d'arguments qui dépend du nombre de groupes :

```js
"Hello, world!".replace(/(\w+), (\w+)!/, (matchedString, first, second) => { 
  console.log(first); 
  console.log(second); 
  return `${second.toUpperCase()}: ${first}!!!` 
}) 
// "WORLD: Hello!!!"

```

### Avidité

Les expressions régulières sont dites **avidité** par défaut.

Que signifie-t-il ?

Prenons cette regex :

```js
/\$(.+)\s?/

```

Elle est censée extraire un montant en dollars d'une chaîne :

```js
/\$(.+)\s?/.exec('This costs $100')[1] // 100

```

mais si nous avons plus de mots après le nombre, elle panique :

```js
/\$(.+)\s?/.exec('This costs $100 and it is less than $200')[1] // 100 and it is less than $200

```

Pourquoi ? Parce que la regex après le signe $ correspond à n'importe quel caractère avec `.+`, et elle ne s'arrêtera pas jusqu'à ce qu'elle atteigne la fin de la chaîne. Ensuite, elle termine parce que `\s?` rend l'espace de fin optionnel.

Pour corriger cela, nous devons dire à la regex d'être paresseuse, et d'effectuer le moins de correspondances possible. Nous pouvons le faire en utilisant le symbole `?` après le quantificateur :

```js
/\$(.+?)\s/.exec('This costs $100 and it is less than $200')[1] // 100

```

> _J'ai supprimé le `?` après `\s`. Sinon, elle ne correspondait qu'au premier nombre, puisque l'espace était optionnel_

Ainsi, `?` signifie différentes choses en fonction de sa position, car il peut être à la fois un quantificateur et un indicateur de mode paresseux.

### Lookaheads : faire correspondre une chaîne en fonction de ce qui la suit

Utilisez `?=` pour faire correspondre une chaîne qui est suivie d'une sous-chaîne spécifique :

```js
/Roger(?=Waters)/

/Roger(?= Waters)/.test('Roger is my dog') // false
/Roger(?= Waters)/.test('Roger is my dog and Roger Waters is a famous musician')
// true

```

`?!` effectue l'opération inverse, en correspondant si une chaîne n'est **pas** suivie d'une sous-chaîne spécifique :

```js
/Roger(?!Waters)/

/Roger(?! Waters)/.test('Roger is my dog') // true
/Roger(?! Waters)/.test('Roger Waters is a famous musician')
// false

```

### Lookbehinds : faire correspondre une chaîne en fonction de ce qui la précède

Ceci est une fonctionnalité [ES2018](https://flaviocopes.com/ecmascript/).

Les lookaheads utilisent le symbole `?=`. Les lookbehinds utilisent `?<=`.

```js
/(?<=Roger) Waters/
/(?<=Roger) Waters/.test('Pink Waters is my dog') 
// false

/(?<=Roger) Waters/.test('Roger is my dog and Roger Waters is a famous musician')
// true

```

Un lookbehind est nié en utilisant `?<!` :

```js
/(?<!Roger) Waters/

/(?<!Roger) Waters/.test('Pink Waters is my dog') 
// true

/(?<!Roger) Waters/.test('Roger is my dog and Roger Waters is a famous musician')
// false

```

### Expressions régulières et Unicode

Le drapeau `u` est obligatoire lors de la manipulation de chaînes Unicode. En particulier, cela s'applique lorsque vous pourriez avoir besoin de gérer des caractères dans les plans astraux (ceux qui ne sont pas inclus dans les 1600 premiers caractères Unicode).

Les emojis sont un bon exemple, mais ils ne sont pas les seuls.

Si vous n'ajoutez pas ce drapeau, cette regex simple qui devrait correspondre à un caractère ne fonctionnera pas, car pour JavaScript cet emoji est représenté en interne par 2 caractères (voir [Unicode en JavaScript](https://flaviocopes.com/javascript-unicode/)) :

```js
/^.$/.test('a') // ✅
/^.$/.test('\ud83d\udc36') // ❌
/^.$/u.test('\ud83d\udc36') // ✅

```

Donc, utilisez toujours le drapeau `u`.

Unicode, tout comme les caractères normaux, gère les plages :

```js
/[a-z]/.test('a') // ✅
/[1-9]/.test('1') // ✅
/[\ud83d\udc36-\ud83e\udd8a]/u.test('\ud83d\udc3a') // ✅
/[\ud83d\udc36-\ud83e\udd8a]/u.test('\ud83d\udc1b') // ❌

```

JavaScript vérifie la représentation interne du code, donc \ud83d\udc36 < \ud83d\udc3a < \ud83e\udd8a parce que `\u1F436` < `\u1F43A` < `\u1F98A`. Consultez la [liste complète des Emoji](https://unicode.org/emoji/charts/full-emoji-list.html) pour obtenir ces codes, et pour découvrir l'ordre (astuce : le sélecteur d'Emoji macOS a certains emojis dans un ordre mélangé, donc ne comptez pas dessus).

### Échappements de propriétés Unicode

Comme nous l'avons vu ci-dessus, dans un motif d'expression régulière, vous pouvez utiliser `\d` pour correspondre à n'importe quel chiffre, `\s` pour correspondre à n'importe quel caractère qui n'est pas un espace blanc, `\w` pour correspondre à n'importe quel caractère alphanumérique, et ainsi de suite.

Les échappements de propriétés Unicode sont une fonctionnalité [ES2018](https://flaviocopes.com/ecmascript/) qui introduit une fonctionnalité très intéressante, étendant ce concept à tous les caractères Unicode en introduisant `\p{}` et sa négation `\P{}`.

Tout caractère Unicode a un ensemble de propriétés. Par exemple, `Script` détermine la famille de langues, `ASCII` est un booléen qui est vrai pour les caractères ASCII, et ainsi de suite. Vous pouvez mettre cette propriété dans les parenthèses du graphe, et la regex vérifiera si elle est vraie :

```js
/^\p{ASCII}+$/u.test('abc') // ✅
/^\p{ASCII}+$/u.test('ABC@') // ✅
/^\p{ASCII}+$/u.test('ABC\ud83d\ude43') // ❌

```

`ASCII_Hex_Digit` est une autre propriété booléenne qui vérifie si la chaîne ne contient que des chiffres hexadécimaux valides :

```js
/^\p{ASCII_Hex_Digit}+$/u.test('0123456789ABCDEF') // ✅
/^\p{ASCII_Hex_Digit}+$/u.test('h') // ❌

```

Il existe de nombreuses autres propriétés booléennes, que vous vérifiez simplement en ajoutant leur nom dans les parenthèses du graphe, y compris `Uppercase`, `Lowercase`, `White_Space`, `Alphabetic`, `Emoji` et plus :

```js
/^\p{Lowercase}$/u.test('h') // ✅
/^\p{Uppercase}$/u.test('H') // ✅
/^\p{Emoji}+$/u.test('H') // ❌
/^\p{Emoji}+$/u.test('\ud83d\ude43\ud83d\ude43') // ✅

```

En plus de ces propriétés binaires, vous pouvez vérifier n'importe laquelle des propriétés des caractères unicode pour correspondre à une valeur spécifique. Dans cet exemple, je vérifie si la chaîne est écrite en alphabet grec ou latin :

```js
/^\p{Script=Greek}+$/u.test('\u03b5\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac') // ✅
/^\p{Script=Latin}+$/u.test('hey') // ✅

```

Lisez plus sur toutes les propriétés que vous pouvez utiliser [directement sur la proposition](https://github.com/tc39/proposal-regexp-unicode-property-escapes).

## Exemples

En supposant qu'une chaîne n'a qu'un seul nombre que vous devez extraire, `/\d+/` devrait le faire :

```
'Test 123123329'.match(/\d+/) 
// Array [ "123123329" ]
```

### Correspondre à une adresse e-mail

Une approche simpliste consiste à vérifier les caractères non-espace avant et après le signe `@`, en utilisant `\S` :

```js
/(\S+)@(\S+)\.(\S+)/
/(\S+)@(\S+)\.(\S+)/.exec('copesc@gmail.com')
               
// ["copesc@gmail.com", "copesc", "gmail", "com"]

```

Ceci est un exemple simpliste, cependant, car de nombreux e-mails invalides sont encore satisfaits par cette regex.

### Capturer le texte entre guillemets doubles

Supposons que vous avez une chaîne qui contient quelque chose entre guillemets doubles, et que vous voulez extraire ce contenu.

Le meilleur moyen de le faire est d'utiliser un **groupe de capture**, car nous savons que la correspondance commence et se termine par `"`, et nous pouvons facilement le cibler, mais nous voulons également supprimer ces guillemets de notre résultat.

Nous trouverons ce dont nous avons besoin dans `result[1]` :

```js
const hello = 'Hello "nice flower"'
const result = /"([^']*)"/.exec(hello)
// Array [ "\"nice flower\"", "nice flower" ]

```

### Obtenir le contenu à l'intérieur d'une balise HTML

Par exemple, obtenir le contenu à l'intérieur d'une balise span, en permettant n'importe quel nombre d'arguments à l'intérieur de la balise :

```js
/<span\b[^>]*>(.*?)<\/span>/

/<span\b[^>]*>(.*?)<\/span>/.exec('test')
// null

/<span\b[^>]*>(.*?)<\/span>/.exec('<span>test</span>')
// ["<span>test</span>", "test"]

/<span\b[^>]*>(.*?)<\/span>/.exec('<span class="x">test</span>')
// ["<span class="x">test</span>", "test"]

```

Intéressé par l'apprentissage de JavaScript ? Obtenez mon [JavaScript Handbook](https://flaviocopes.com/page/javascript-handbook).