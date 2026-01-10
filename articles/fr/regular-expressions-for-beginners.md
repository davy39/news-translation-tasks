---
title: Comment utiliser les expressions régulières en JavaScript – Tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-16T17:51:48.000Z'
originalURL: https://freecodecamp.org/news/regular-expressions-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/regex-image-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
seo_title: Comment utiliser les expressions régulières en JavaScript – Tutoriel pour
  débutants
seo_desc: "By Chinwendu Enyinna\nRegular expressions (regex) are a useful programming\
  \ tool. They are key to efficient text processing. Knowing how to solve problems\
  \ using regex is helpful to you as a developer and improves your productivity. \n\
  In this article, yo..."
---

Par Chinwendu Enyinna

Les expressions régulières (regex) sont un outil de programmation utile. Elles sont essentielles pour le traitement efficace de texte. Savoir résoudre des problèmes en utilisant les regex est utile pour vous en tant que développeur et améliore votre productivité. 

Dans cet article, vous apprendrez les fondamentaux des expressions régulières, la notation des motifs d'expressions régulières, comment interpréter un motif regex simple et comment écrire votre propre motif regex. Commençons !

## Qu'est-ce que les expressions régulières ?

Les expressions régulières sont des motifs qui permettent de décrire, faire correspondre ou analyser du texte. Avec les expressions régulières, vous pouvez faire des choses comme trouver et remplacer du texte, vérifier que les données d'entrée suivent le format requis, et d'autres choses similaires.

Voici un scénario : vous souhaitez vérifier que le numéro de téléphone saisi par un utilisateur sur un formulaire correspond à un format, par exemple, ###-###-#### (où # représente un chiffre). Une façon de résoudre cela pourrait être :

```js
function isPattern(userInput) {
  if (typeof userInput !== 'string' || userInput.length !== 12) {
    return false;
  }
  for (let i = 0; i < userInput.length; i++) {
    let c = userInput[i];
    switch (i) {
      case 0:
      case 1:
      case 2:
      case 4:
      case 5:
      case 6:
      case 8:
      case 9:
      case 10:
      case 11:
        if (c < 0 || c > 9) return false;
        break;
      case 3:
      case 7:
        if (c !== '-') return false;
        break;
    }
  }
  return true;
}

```

Alternativement, nous pouvons utiliser une expression régulière ici comme ceci :

```js
function isPattern(userInput) {
  return /^\d{3}-\d{3}-\d{4}$/.test(userInput);
}

```

Remarquez comment nous avons refactorisé le code en utilisant regex. Incroyable, n'est-ce pas ? C'est le pouvoir des expressions régulières.

## Comment créer une expression régulière

En JavaScript, vous pouvez créer une expression régulière de l'une des deux manières suivantes :

* Méthode #1 : en utilisant un littéral d'expression régulière. Cela consiste en un motif enfermé dans des barres obliques. Vous pouvez écrire cela avec ou sans un drapeau (nous verrons ce que signifie un drapeau sous peu). La syntaxe est la suivante :

```js
const regExpLiteral = /pattern/;          // Sans drapeaux

const regExpLiteralWithFlags = /pattern/; // Avec drapeaux

```

Les barres obliques `/.../` indiquent que nous créons un motif d'expression régulière, de la même manière que vous utilisez des guillemets `" "` pour créer une chaîne.

* Méthode #2 : en utilisant la fonction constructeur RegExp. La syntaxe est la suivante :

```js
new RegExp(pattern [, flags])

```

Ici, le motif est enfermé dans des guillemets, de même que le paramètre de drapeau, qui est facultatif.

Alors, quand utiliser chacune de ces méthodes ?

Vous devriez utiliser un littéral regex lorsque vous connaissez le motif d'expression régulière au moment d'écrire le code. 

D'autre part, utilisez le constructeur Regex si le motif regex doit être créé dynamiquement. De plus, le constructeur regex vous permet d'écrire un motif en utilisant un littéral de modèle, mais cela n'est pas possible avec la syntaxe de littéral regex.

### Qu'est-ce que les drapeaux d'expression régulière ?

Les drapeaux ou modificateurs sont des caractères qui activent des fonctionnalités de recherche avancées, y compris la recherche insensible à la casse et la recherche globale. Vous pouvez les utiliser individuellement ou collectivement. Voici quelques-uns des plus couramment utilisés :

* `g` est utilisé pour la recherche globale, ce qui signifie que la recherche ne s'arrêtera pas après la première correspondance.
* `i` est utilisé pour la recherche insensible à la casse, ce qui signifie qu'une correspondance peut se produire indépendamment de la casse.
* `m` est utilisé pour la recherche multiline.
* `u` est utilisé pour la recherche Unicode.

Examinons quelques motifs d'expressions régulières en utilisant les deux syntaxes.

#### Comment utiliser un littéral d'expression régulière : 

```js
// Syntaxe : /pattern/flags

const regExpStr = 'Hello world! hello there';

const regExpLiteral = /Hello/gi;

console.log(regExpStr.match(regExpLiteral));

// Sortie : ['Hello', 'hello']

```

Notez que si nous n'avions pas marqué le motif avec `i`, seul `Hello` serait retourné. 

Le motif `/Hello/` est un exemple de motif simple. Un motif simple se compose de caractères qui doivent apparaître littéralement dans le texte cible. Pour qu'une correspondance se produise, le texte cible doit suivre la même séquence que le motif. 

Par exemple, si vous réécrivez le texte dans l'exemple précédent et essayez de le faire correspondre :

```js
const regExpLiteral = /Hello/gi;

const regExpStr = 'oHell world, ohell there!';

console.log(regExpStr.match(regExpLiteral));

// Sortie : null

```

Nous obtenons _null_ parce que les caractères de la chaîne n'apparaissent pas comme spécifié dans le motif. Donc un motif littéral comme `/hello/`, signifie _h_ suivi de _e_ suivi de _l_ suivi de _l_ suivi de _o_, exactement comme cela.

#### Comment utiliser un constructeur regex :

```js
// Syntaxe : RegExp(pattern [, flags])

const regExpConstructor = new RegExp('xyz', 'g'); // Avec le drapeau -g

const str = 'xyz xyz';

console.log(str.match(regExpConstructor));

// Sortie : ['xyz', 'xyz']

```

Ici, le motif `xyz` est passé en tant que chaîne, tout comme le drapeau. De plus, les deux occurrences de `xyz` ont été trouvées parce que nous avons passé le drapeau -g. Sans lui, seule la première correspondance serait retournée. 

Nous pouvons également passer des motifs créés dynamiquement en tant que littéraux de modèle en utilisant la fonction constructeur. Par exemple :

```js
const pattern = prompt('Entrez un motif');
// Supposons que l'utilisateur entre 'xyz'

const regExpConst = new RegExp(`${pattern}`, 'gi');

const str = 'xyz XYZ';

console.log(str.match(regExpConst)); // Sortie : ['xyz', 'XYZ']

```

## Comment utiliser les caractères spéciaux des expressions régulières

Un **caractère spécial** dans une expression régulière est un caractère avec une signification réservée. En utilisant des caractères spéciaux, vous pouvez faire plus que simplement trouver une correspondance directe. 

Par exemple, si vous souhaitez faire correspondre un caractère dans une chaîne qui peut apparaître une fois ou plusieurs fois, vous pouvez le faire avec des caractères spéciaux. Ces caractères se divisent en différents sous-groupes qui remplissent des fonctions similaires.

Examinons chaque sous-groupe et les caractères qui les accompagnent.

### Ancres et limites :

Les **ancres** sont des métacaractères qui correspondent au début et à la fin d'une ligne de texte qu'ils examinent. Vous les utilisez pour affirmer où une limite doit être. 

Les deux caractères utilisés sont `^` et `$`.

* `^` correspond au début d'une ligne et ancré un littéral au début de cette ligne. Par exemple :

```js
const regexPattern1 = /^cat/;

console.log(regexPattern1.test('cat and mouse')); // Sortie : true

console.log(regexPattern1.test('The cat and mouse')); // Sortie : false car la ligne ne commence pas par cat

// Sans le ^ dans le motif, la sortie retournera true
// car nous n'avons pas affirmé de limite.

const regexPattern2 = /cat/;

console.log(regexPattern2.test('The cat and mouse')); // Sortie : true

```

* `$` correspond à la fin d'une ligne et ancré un littéral à la fin de cette ligne. Par exemple :

```js
const regexPattern = /cat$/;

console.log(regexPattern.test('The mouse and the cat')); // Sortie : true

console.log(regexPattern.test('The cat and mouse')); // Sortie : false

```

Notez que les caractères d'ancrage `^` et `$` **correspondent simplement à la position des caractères dans le motif** et non aux caractères eux-mêmes.

Les **limites de mot** sont des métacaractères qui correspondent à la position de début et de fin d'un mot – une séquence de caractères alphanumériques. Vous pouvez les considérer comme une version basée sur les mots de `^` et `$`. Vous utilisez les métacaractères `b` et `B` pour affirmer une limite de mot. 

* `\b` correspond au début ou à la fin d'un mot. Le mot est trouvé selon la position du métacaractère. Voici un exemple :

```js
// Syntaxe 1 : /\b.../ où .... représente un mot.

// Rechercher un mot qui commence par le motif ward
const regexPattern1 = /\bward/gi;

const text1 = 'backward Wardrobe Ward';

console.log(text1.match(regexPattern1)); // Sortie : ['Ward', 'Ward']

// Syntaxe 2 : /...\b/

// Rechercher un mot qui se termine par le motif ward
const regexPattern2 = /ward\b/gi;

const text2 = 'backward Wardrobe Ward';

console.log(text2.match(regexPattern2)); // Sortie : ['ward', 'Ward']

// Syntaxe 3 : /\b....\b/

// Rechercher un mot autonome qui commence et se termine par le motif ward
const regexPattern3 = /\bward\b/gi;

const text3 = 'backward Wardrobe Ward';

console.log(text3.match(regexPattern3)); // Sortie : ['Ward']

```

* `\B` est l'opposé de `\b`. Il correspond à chaque position où `\b` ne correspond pas.

### Raccourcis pour d'autres métacaractères :

En plus des métacaractères que nous avons vus, voici quelques-uns des plus couramment utilisés :

* `\d` – correspond à n'importe quel chiffre décimal et est un raccourci pour [0-9].
* `\w` – correspond à n'importe quel caractère alphanumérique qui pourrait être une lettre, un chiffre ou un trait de soulignement. `\w` est un raccourci pour [A-Za-z0-9_].
* `\s` – correspond à n'importe quel caractère d'espace blanc.
* `\D` – correspond à n'importe quel non-chiffre et est le même que [^0-9.]
* `\W` – correspond à n'importe quel caractère non-mot (c'est-à-dire non-alphanumérique) et est un raccourci pour [^A-Za-z0-9_].
* `\S` – correspond à un caractère non-espace blanc.
* `.` – correspond à n'importe quel caractère.

### Qu'est-ce qu'une classe de caractères ?

Une classe de caractères est utilisée pour faire correspondre l'un des plusieurs caractères dans une position particulière. Pour désigner une classe de caractères, vous utilisez des crochets `[]` et listez ensuite les caractères que vous souhaitez faire correspondre à l'intérieur des crochets. 

Examinons un exemple :

```js
// Trouver et faire correspondre un mot avec deux orthographes alternatives

const regexPattern = /ambi[ea]nce/;

console.log(regexPattern.test('ambiance')); // Sortie : true

console.log(regexPattern.test('ambiance')); // Sortie : true

// Le motif regex s'interprète comme : trouver a suivi de m, puis b,
// puis i, puis soit e ou a, puis n, puis c, et enfin e.

```

### Qu'est-ce qu'une classe de caractères négative ?

Si vous ajoutez un symbole circonflexe à l'intérieur d'une classe de caractères comme ceci `[^...]`, il correspondra à n'importe quel caractère qui n'est pas listé à l'intérieur des crochets. Par exemple :

```js
const regexPattern = /[^bc]at/;

console.log(regexPattern.test('bat')); // Sortie : false

console.log(regexPattern.test('cat')); // Sortie : false

console.log(regexPattern.test('mat')); // Sortie : true

```

### Qu'est-ce qu'une plage ?

Un tiret `-` indique une plage lorsqu'il est utilisé à l'intérieur d'une classe de caractères. Supposons que vous souhaitez faire correspondre un ensemble de chiffres, par exemple [0123456789], ou un ensemble de caractères, par exemple [abcdefg]. Vous pouvez l'écrire comme une plage comme ceci, [0-9] et [a-g], respectivement.

### Qu'est-ce que l'alternance ?

L'alternance est une autre façon de spécifier un ensemble d'options. Ici, vous utilisez le caractère pipe `|` pour faire correspondre l'une des plusieurs sous-expressions. Chacune des sous-expressions est appelée une **alternative**. 

Le symbole pipe signifie « ou », donc il correspond à une série d'options. Il vous permet de combiner des sous-expressions comme alternatives. 

Par exemple, `(x|y|z)a` correspondra à `xa` ou `ya`, ou `za`. Afin de limiter la portée de l'alternance, vous pouvez utiliser des parenthèses pour regrouper les alternatives ensemble. 

Sans les parenthèses, `x|y|za` signifierait `x` ou `y` ou `za`. Par exemple :

```js
const regexPattern = /(Bob|George)\sClan/;

console.log(regexPattern.test('Bob Clan')); // Sortie : true

console.log(regexPattern.test('George Clan')); // Sortie : true

```

### Qu'est-ce que les quantificateurs et l'avidité ?

Les quantificateurs indiquent combien de fois un caractère, une classe de caractères ou un groupe doit apparaître dans le texte cible pour qu'une correspondance se produise. En voici quelques-uns particuliers :

* `+` correspondra à n'importe quel caractère auquel il est ajouté si le caractère apparaît au moins une fois. Par exemple :

```js
const regexPattern = /hel+o/;

console.log(regexPattern.test('helo'));          // Sortie : true

console.log(regexPattern.test('hellllllllllo')); // Sortie : true

console.log(regexPattern.test('heo'));           // Sortie : false

```

* `*` est similaire au caractère + mais avec une légère différence. Lorsque vous ajoutez * à un caractère, cela signifie que vous souhaitez faire correspondre n'importe quel nombre de ce caractère, y compris aucun. Voici un exemple :

```js
const regexPattern = /hel*o/;

console.log(regexPattern.test('helo'));    // Sortie : true

console.log(regexPattern.test('hellllo')); // Sortie : true

console.log(regexPattern.test('heo'));     // Sortie : true

// Ici, le * correspond à 0 ou n'importe quel nombre de 'l'

```

* `?` implique "facultatif". Lorsque vous l'ajoutez à un caractère, cela signifie que le caractère peut apparaître ou non. Par exemple :

```js
const regexPattern = /colou?r/;

console.log(regexPattern.test('color'));  // Sortie : true

console.log(regexPattern.test('colour')); // Sortie : true

// Le ? après le caractère u rend u facultatif

```

* `{N}`, lorsqu'il est ajouté à un caractère ou une classe de caractères, spécifie combien de fois nous voulons que le caractère apparaisse. Par exemple, `/\d{3}/` signifie faire correspondre trois chiffres consécutifs.
* `{N,M}` est appelé le quantificateur d'intervalle et est utilisé pour spécifier une plage pour le nombre minimum et maximum de correspondances possibles. Par exemple, `/\d{3, 6}/` signifie faire correspondre un minimum de 3 et un maximum de 6 chiffres consécutifs.
* `{N, }` désigne une plage ouverte. Par exemple, `/\d{3, }/` signifie faire correspondre n'importe quel nombre de 3 chiffres consécutifs ou plus.

### Qu'est-ce que l'avidité dans les regex ?

Tous les quantificateurs sont **avidés** par défaut. Cela signifie qu'ils essaieront de faire correspondre tous les caractères possibles. 

Pour supprimer cet état par défaut et les rendre non-avidés, vous ajoutez un `?` à l'opérateur comme ceci `+?`, `*?`, `{N}?`, `{N,M}?`.....et ainsi de suite.

### Qu'est-ce que le regroupement et la rétro-référence ?

Nous avons précédemment vu comment nous pouvons limiter la portée de l'alternance en utilisant les parenthèses. 

Et si vous souhaitez utiliser un quantificateur comme `+` ou `*` sur plus d'un caractère à la fois – disons une classe de caractères ou un groupe ? Vous pouvez les regrouper ensemble en tant qu'ensemble en utilisant les parenthèses avant d'ajouter le quantificateur, comme dans cet exemple :

```js
const regExp = /abc+(xyz+)+/i;

console.log(regExp.test('abcxyzzzzXYZ')); // Sortie : true

```

Voici ce que signifie le motif : Le premier + correspond au c de abc, le deuxième + correspond au z de xyz, et le troisième + correspond à la sous-expression xyz, qui correspondra si la séquence se répète.

La **rétro-référence** vous permet de faire correspondre un nouveau motif qui est le même qu'un motif précédemment trouvé dans une expression régulière. Vous utilisez également des parenthèses pour la rétro-référence car elles peuvent se souvenir d'une sous-expression précédemment trouvée qu'elles enferment (c'est-à-dire, le groupe capturé).

Cependant, il est possible d'avoir plus d'un groupe capturé dans une expression régulière. Donc, pour rétro-référencer l'un des groupes capturés, vous utilisez un nombre pour identifier les parenthèses. 

Supposons que vous avez 3 groupes capturés dans une regex et que vous souhaitez rétro-référencer l'un d'eux. Vous utilisez `\1`, `\2`, ou `\3`, pour vous référer aux première, deuxième ou troisième parenthèses. Pour numéroter les parenthèses, vous commencez à compter les parenthèses ouvertes à partir de la gauche.

Examinons quelques exemples :

**`(x)`** correspond à x et se souvient de la correspondance.

```js
const regExp = /(abc)bar\1/i;

// abc est rétro-référencé et est ancré à la même position que \1
console.log(regExp.test('abcbarAbc')); // Sortie : true

console.log(regExp.test('abcbar')); // Sortie : false

```

**`(?:x)`** correspond à x mais ne se souvient pas de la correspondance. De plus, \n (où n est un nombre) ne se souvient pas d'un groupe capturé précédemment et correspondra en tant que littéral. En utilisant un exemple :

```js
const regExp = /(?:abc)bar\1/i;

console.log(regExp.test('abcbarabc')); // Sortie : false

console.log(regExp.test('abcbar\1')); // Sortie : true

```

### La règle d'échappement

Un métacaractère doit être échappé avec une barre oblique inverse si vous souhaitez qu'il apparaisse en tant que littéral dans votre expression régulière. En échappant un métacaractère dans une regex, le métacaractère perd sa signification spéciale.

## Méthodes d'expressions régulières

### La méthode `test()` 

Nous avons utilisé cette méthode plusieurs fois dans cet article. La méthode `test()` compare le texte cible avec le motif regex et retourne une valeur booléenne en conséquence. S'il y a une correspondance, elle retourne true, sinon elle retourne false.

```js
const regExp = /abc/i;

console.log(regExp.test('abcdef')); // Sortie : true

console.log(regExp.test('bcadef')); // Sortie : false

```

### La méthode `exec()` 

La méthode `exec()` compare le texte cible avec le motif regex. S'il y a une correspondance, elle retourne un tableau avec la correspondance – sinon elle retourne null. Par exemple :

```js
const regExp = /abc/i;

console.log(regExp.exec('abcdef'));
// Sortie : ['abc', index: 0, input: 'abcdef', groups: undefined]

console.log(regExp.exec('bcadef'));
// Sortie : null

```

De plus, il existe des méthodes de chaîne qui acceptent des expressions régulières comme paramètre comme `[match()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)`, `[replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)`, `[replaceAll()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)`, `[matchAll()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)`, `[search()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/search)`, et `[split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)`. 

## Exemples de Regex

Voici quelques exemples pour renforcer certains des concepts que nous avons appris dans cet article.

Premier exemple : Comment utiliser un motif regex pour faire correspondre une adresse e-mail :

```js
const regexPattern = /^[(\w\d\W)+]+@[\w+]+\.[\w+]+$/i;

console.log(regexPattern.test('abcdef123@gmailcom'));
// Sortie : false, il manque un point

console.log(regexPattern.test('abcdef123gmail.'));
// Sortie : false, il manque le littéral de fin 'com'

console.log(regexPattern.test('abcdef123@gmail.com'));
// Sortie : true, l'entrée correspond correctement au motif

```

Interprétons le motif. Voici ce qui se passe :

* **`/`** représente le début du motif d'expression régulière.
* **`^`** vérifie le début d'une ligne avec les caractères de la classe de caractères.
* `**[(\w\d\W)+ ]+**` correspond à n'importe quel mot, chiffre et caractère non-mot dans la classe de caractères au moins une fois. Remarquez comment les parenthèses ont été utilisées pour regrouper les caractères avant d'ajouter le quantificateur. Cela est identique à ceci `[\w+\d+\W+]+`.
* `**@**` correspond au littéral @ dans le format de l'e-mail.
* `**[\w+]+**` correspond à n'importe quel caractère de mot dans cette classe de caractères au moins une fois.
* `**\.**` échappe le point pour qu'il apparaisse comme un caractère littéral.
* `**[\w+]+$**` correspond à n'importe quel caractère de mot dans cette classe. De plus, cette classe de caractères est ancrée à la fin de la ligne.
* `**/**` - termine le motif

D'accord, exemple suivant : comment faire correspondre une URL avec le format http://example.com ou https://www.example.com :

```js
const pattern = /^[https?]+:\/\/((w{3}\.)?[\w+]+)\.[\w+]+$/i;

console.log(pattern.test('https://www.example.com'));
// Sortie : true

console.log(pattern.test('http://example.com'));
// Sortie : true

console.log(pattern.test('https://example'));
// Sortie : false

```

Interprétons également ce motif. Voici ce qui se passe :

* `/...../` représente le début et la fin du motif regex
* `^` affirme le début de la ligne
* `[https?]+` correspond aux caractères listés au moins une fois, cependant `?` rend 's' facultatif.
* `:` correspond à un point-virgule littéral.
* `\/\/` échappe les deux barres obliques.
* `(w{3}\.)` correspond au caractère w 3 fois et au point qui suit immédiatement. Cependant, ce groupe est facultatif.
* `[\w+]+` correspond au caractère de cette classe au moins une fois.
* `\.` échappe le point
* `[\w+]+$` correspond à n'importe quel caractère de mot dans cette classe. De plus, cette classe de caractères est ancrée à la fin de la ligne.

## Conclusion

Dans cet article, nous avons examiné les fondamentaux des expressions régulières. Nous avons également expliqué certains motifs d'expressions régulières et pratiqué avec quelques exemples.

Il y a plus à apprendre sur les expressions régulières au-delà de cet article. Pour vous aider à en apprendre davantage sur les expressions régulières, voici quelques ressources que vous pouvez consulter :

* [Regular Expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
* [Learn Regex crash course](https://www.freecodecamp.org/news/regular-expressions-crash-course/)
* [Regular Expression Tutorial](https://www.regular-expressions.info/tutorial.html)
* [Regular Expression Cheatsheet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet)

Et c'est tout pour ce tutoriel. Bon codage :)