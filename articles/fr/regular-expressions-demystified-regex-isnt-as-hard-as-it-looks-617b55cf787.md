---
title: 'Les Expressions Régulières Démystifiées : RegEx n''est pas aussi difficile
  qu''il en a l''air'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-23T21:35:28.000Z'
originalURL: https://freecodecamp.org/news/regular-expressions-demystified-regex-isnt-as-hard-as-it-looks-617b55cf787
coverImage: https://cdn-media-1.freecodecamp.org/images/0*kKGQn6RZmO--M8ix.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: 'Les Expressions Régulières Démystifiées : RegEx n''est pas aussi difficile
  qu''il en a l''air'
seo_desc: 'By Vijayabharathi Balasubramanian

  Are you one of those people who stays away from regular expressions because it looks
  like a foreign language? I was one. Not anymore.

  Think of all those sounds, traffic signs and smells that you can recognize. Regula...'
---

Par Vijayabharathi Balasubramanian

Êtes-vous l'une de ces personnes qui évitent les expressions régulières parce que cela ressemble à une langue étrangère ? J'en faisais partie. Plus maintenant.

Pensez à tous ces sons, panneaux de signalisation et odeurs que vous pouvez reconnaître. Les expressions régulières ne sont pas différentes. C'est comme une langue des signes pour analyser des chaînes de caractères.

Nous allons comprendre les expressions régulières aujourd'hui. Au moins, les expressions **régulières** utilisées.

Tout comme n'importe quel langage de programmation, une expression régulière est un langage succinct à part entière.

Nous saurons comment utiliser les expressions régulières à bon escient à la fin de cet article. Nous résoudrons des problèmes simples et apprendrons beaucoup en cours de route.

Êtes-vous prêt à investir 30 minutes et à ressortir éclairé en RegEx ? Installez-vous alors.

#### Pourquoi les expressions régulières ?

Nous avons chacun notre propre « pourquoi », n'est-ce pas ? L'un peut être de tester si la chaîne est un code couleur hexadécimal valide. Vous pouvez écrire une bibliothèque de processeur telle que [Sass](https://github.com/search?l=&q=regexp+repo%3Asass%2Fsass&ref=advsearch&type=Code&utf8=%E2%9C%93) qui exploite RegEx.

Je laisserai l'univers vous lancer le **pourquoi** et je vous aiderai à couvrir le **comment**.

### 0. Préparez Votre Terrain de Jeu

#### Références

La plupart du temps, je trouve cette page adéquate pour commencer : [Expressions Régulières de MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions). En fait, cette page est tout ce dont vous avez besoin. Vous pouvez arrêter de lire cet article. Maintenant. Fermez cet onglet. ?

Toujours avec moi ? Merci. Vous avez besoin d'un bac à sable pour jouer. Heureusement, il y en a un disponible sur votre navigateur. Utilisez simplement les DevTools dans la console de votre navigateur.

#### Familiarisez-vous avec la syntaxe

Pour commencer, nous allons utiliser la syntaxe `/expression/.test('string')`.

Une `expression` est n'importe quelle expression régulière que nous construisons. Une `string` est la chaîne sous test. La méthode `test` retourne `true` ou `false` selon la correspondance.

Les barres obliques marquent le début et la fin de l'expression. Traitez-les comme les guillemets doubles (») et simples (’) que vous utilisez pour marquer le début et la fin d'une chaîne de caractères simple.

L'expression entre `/` est un littéral. **Ils sont traités comme des caractères littéraux.** Les noms de variables ne seraient pas résolus en leurs contenus.

Pour la rendre dynamique, nous devons passer par le constructeur, en utilisant la syntaxe `new RegEx(variable_name)`. Cela viendra à notre secours vers la fin de l'article.

**Faites-le maintenant.** Tapez simplement ceci dans votre console de navigateur.

```js
/a/.test("a"); //true
/a/.test("b"); //false
```

Si cela fonctionne, vous êtes prêt. Ne vous inquiétez pas de ce que c'est. C'est ce que nous allons décomposer en morceaux dans les lignes suivantes.

Plongeons-nous...

### 1. Commencez Petit Avec Les Lettres

Commençons petit. Nous devons trouver si une chaîne contient un caractère particulier. Cherchez le caractère `a` dans une chaîne.

Voici l'expression dans toute sa gloire :

```js
/a/.test("abc"); //true 
/a/.test("bcd"); //false 
/a/.test("cba"); //true
```

L'expression fait ce que nous avons demandé, « Cherchez `a` dans la chaîne sous test ». Dans notre cas, `abc` et `bca` contiennent bien le caractère `a`. Mais `bcd` ne l'a pas.

#### Décomposition

Maintenant, il y a beaucoup de barres obliques et de barres obliques inverses. Décomposons-les.

Nous avons vu que `/expression/` est la façon dont nous construisons les expressions régulières. Donc pas de question sur la barre oblique là. En fait, nous pouvons même **l'assigner à une variable** et la faire paraître mieux.

**Le même code :**

```js
let e=/a/; 
e.test("abc"); //true 
e.test("bcd"); //false 
e.test("cba"); //true
```

L'expression entre les barres obliques est juste un seul caractère `a` dans notre cas. Nous cherchons seulement ce caractère.

#### Atteindre les Multi-Caractères

Échelonnons la solution.

Que faire si vous voulez trouver plus d'un caractère ?

Mettez-les en séquence. Traitez-les comme une sous-chaîne.

Voici un exemple :

```js
/ab/.test("abacus"); //true 
/bac/.test("abacus"); //true  
/abc/.test("abacus"); //false 
/abas/.test("abacus"); //false
```

La chaîne sous test doit contenir l'expression exacte entre les barres obliques. Nous obtenons une correspondance si cette condition est remplie.

`bac` est dans `abacus` mais `abas` n'est pas dans `abacus` tel quel. Même si nous avons ces caractères mélangés, nous n'obtenons pas de correspondance exacte.

#### Révision du terrain couvert

Symbole `/.../` . La barre oblique (/) marque le début et la fin de l'expression régulière. Ignorez les points, c'est là que nous plaçons le motif. Le caractère `/a/` entre les barres obliques est un motif correspondant à la chaîne sous test. Les caractères `/abc/` entre les barres obliques sont recherchés comme une sous-chaîne lors du test de correspondance de motif sur la chaîne sous test.

### 2. Motifs dans les Nombres

Ajoutons un peu d'épice. Disons que vous voulez savoir si une chaîne est pleine de caractères numériques.

Voici comment faire :

```js
let e=/0|1|2|3|4|5|6|7|8|9/;
e.test("42"); //true 
e.test("The answer is 42"); //true
```

Tout d'abord, le motif semble assez long. Mais la même longue série de caractères **peut être exprimée en seulement deux caractères**. Je l'ai réservé pour la fin de cette section pour une conclusion dramatique.

Le deuxième cas ne devrait pas être vrai. Nous nous en occuperons un peu plus tard.

Pour l'instant, le symbole pipe (`|`) signifie **ou**. En dehors des expressions régulières, nous l'avons utilisé comme un **ou** binaire et un **ou** conditionnel avec des doubles pipes (||). C'est le même gars.

Je pourrais appeler cela facile et en rester là. Mais vous crieriez pour quelque chose de mieux, n'est-ce pas ? Nous sommes développeurs. Nous passons la meilleure partie de notre journée à penser à de meilleurs alias Bash et Git pour économiser quelques frappes.

Dois-je taper neuf symboles pipe ? Non.

Recommençons :

```js
e=/[0123456789]/; 
e.test("42"); //true 
e.test("The answer is 42"); //still true
```

C'est mieux. 9 pipes ont été remplacés par 2 crochets. 7 caractères ont été économisés. C'est 77,7 % de frappes en moins.

Au fait, tout ce qui se trouve entre crochets est considéré comme « Soit ceci » ou « cela ». C'est un ensemble de caractères. Dans notre cas, la chaîne doit contenir soit `0`, soit `1`, soit `2`, soit... portez avec moi, je me suis promis d'écrire 1000 mots par jour, soit `3` soit `4` soit `5`. Bon, arrêtons. Vous avez compris.

Qu'est-ce que vous dites ? Cela semble encore assez long ? Pas satisfait ?

D'accord, recommençons une fois de plus :

```js
e=/[0-9]/; 
e.test(42); //true 
e.test("42"); //true 
e.test("The answer is 42"); //true!
```

Comment cela ? Cela semble beaucoup plus propre, n'est-ce pas ? Tout ce qui se trouve entre crochets `[]` signifie **ou**. `0-9` marque une plage, signifiant de zéro à neuf.

Ainsi, le test recherche des caractères de zéro à neuf dans la chaîne de test.

Comme vous pouvez le voir, le test accepte également les nombres.

#### Les motifs de préfixe et de suffixe

Abordons maintenant ce deuxième cas qui échoue. `The answer is 42` correspond à notre test parce que notre motif recherche des caractères numériques quelque part **dans** la chaîne. **Pas du début à la fin**.

Faisons appel à `^` et `$` pour nous aider.

* `^` signifie le **début** de la chaîne. C'est un agent double et il va nous faire trébucher. Son deuxième avatar n'est démasqué que dans la dernière section.
* `$` signifie la **fin** de la chaîne.

Commençons par le motif de préfixe :

```js
/^a/.test("abc"); //true 
/^a/.test("bca"); //false 
/^http/.test("https://pineboat.in"); //true /^http/.test("ftp://pineboat.in"); //false
```

Tout motif qui suit `^` doit être au début de la chaîne sous test.

La deuxième chaîne commence par `b` tandis que notre motif recherche `a`. La quatrième recherche `http` tandis que la chaîne commence par `ftp`. C'est la raison pour laquelle elles échouent.

#### Les motifs de suffixe

Le motif de suffixe suit. `$` à la fin du motif dirige le test pour rechercher la fin de la chaîne.

```js
/js$/.test("regex.js"); //true 
/js$/.test("regex.sj"); //false
```

Cela devrait résonner dans votre tête comme, « Recherchez `js` puis la fin de la chaîne ». Mieux encore, « Recherchez une chaîne qui se termine par `js` ».

#### Correspondance de motif de bout en bout

Cela ouvre la voie à la correspondance de motif de début à fin, vous pourriez aussi bien l'appeler de bout en bout.

```js
let e=/^[0-9]$/ 
e.test("42"); //false - NON ! 
e.test("The answer is 42"); //false 
e.test("7"); //true
```

Étonnamment, le premier a échoué lorsque nous avons ajouté `^` et `$`.

`/^[0-9]$/` se lit comme, « Allez au début de la chaîne. Recherchez un **chiffre unique** dans l'ensemble de caractères. Vérifiez si la chaîne se termine là. » C'est la raison pour laquelle la dernière entrée a retourné `true`. Ce n'est qu'un seul chiffre, du début à la fin.

Ce n'est pas ce que nous voulions. Nous voulions tester si la chaîne avait un ou plusieurs chiffres.

Nous sommes très proches. Une dernière chose que nous devons apprendre est comment instruire le motif pour rechercher plus d'un caractère dans l'ensemble.

#### Le Conte des Trois Mousquetaires

Un point d'interrogation (`?`), un plus (`+`) et un astérisque (`*`) se sont rencontrés sur un champ de bataille. Chacun a une vue différente.

Le modeste point d'interrogation (`?`) dit, « Je peux ne rien voir ou juste un. »

Plus (`+`) dit, « Je dois voir au moins un ou plus. »

Astérisque (`*`) dit, « Je vous comprends tous les deux. Je peux ne rien voir, un, ou plus. »

**L'un d'eux cache habilement ce dont il est capable.**

Le point d'interrogation monte sur scène en premier :

```js
/a?/.test("") //true 
/a?/.test("a") //true 
/a?/.test("b") //true! 
/a?/.test("aa") //true 
/^a?$/.test("aa") //false
```

* Correspond à la chaîne vide `""`   
car `?` signifie 0 ou 1
* Correspond à `a`   
une correspondance
* Correspond à `b`  
correspond à 0 occurrence
* Correspond à `aa`   
une correspondance et le second `a` ne fait pas partie du motif
* `/^a?$/` ne correspond pas à `aa`  
Il recherche zéro ou un `a`, du début à la fin, rien de plus, rien de moins

Le plus (`+`) regarde le point d'interrogation et remarque, « Je suis impressionné, mais votre focus est si binaire ! ». Et prend la scène pour se montrer :

```js
/a+/.test("a") //true 
/a+/.test("aa") //true 
/a+/.test("ba") //true! 
/^a+$/.test("aa") //true  
/a+/.test("") //false 
/a+/.test("b") //false 
/^a+$/.test("ab") //false
```

Souvenez-vous de ce que le plus (`+`) a dit ? Il peut correspondre à une ou plusieurs occurrences du motif précédent.

Tous ceux qui retournent `true` ont un ou plusieurs `a`. Nous avons même réussi à obtenir une chaîne entière composée uniquement de `a` dans le dernier qui a retourné vrai avec `/^a+$/`.

`false` devrait maintenant avoir du sens, mais un mot sur le dernier qui a retourné false. `/^a+$/` recherche `a` du début à la fin, aucun autre caractère n'est autorisé. C'est pourquoi `ab` a échoué au test.

Enfin, l'étoile (`*`) du spectacle monte sur scène. Il se vante de pouvoir, « Je peux duel seul ou duel vous deux à la fois » et dit, « Je peux correspondre à zéro, un ou plus ».

```js
/a*/.test("a") //true 
/a*/.test("aa") //true 
/a*/.test("ba") //true 
/a*/.test("") //true 
/a*/.test("b") //true 
/^a*$/.test("aa") //true 
/^a*$/.test("") //true  
/^a*$/.test("ab") //false
```

Sauf le dernier, * a pu gérer tout le reste. `/^a*$/` se lit comme, 0 ou plus `a` du début à la fin. C'est pourquoi la chaîne vide `""` a passé le test et `"ab"` a échoué.

#### Retour à la Réponse Universelle

Souvenez-vous où nous en étions avant de rencontrer les trois mousquetaires ? Oui, « The answer is 42 ».

Maintenant, si nous devons rechercher uniquement des chiffres, un ou plusieurs, du début à la fin, que faisons-nous ?

```js
//Ajoutons un plus 
let e=/^[0-9]+$/ 
e.test("4"); //true 
e.test("42"); //true 
e.test("The answer 42"); //false - Hourra
```

Le signe plus (`+`) dans `[0-9]+` vient à notre secours. Plus signifie plus d'une occurrence du caractère ou du motif qui le précède. Dans notre cas, plus d'un chiffre.

Il échoue également la correspondance pour notre dernier cas `The answer is 42` parce qu'il n'y a pas de chiffres au début de la chaîne.

#### Pratique des Motifs

* Pouvez-vous essayer d'écrire un motif pour les nombres hexadécimaux (composés de chiffres 0-9 et de lettres a-f, avec un # facultatif devant) ?
* Et pour un nombre binaire ? Pouvez-vous tester si une chaîne est pleine de 0 et de 1 ?

#### Cette Fin Dramatique

Oh, j'ai presque oublié. `[0-9]` représente n'importe quel caractère numérique et a également une version abrégée `\d`.

```js
let e=/^\d+$/; e.test("4"); //true e.test("42"); //true e.test("The answer 42"); //false - Hourra
```

Seulement deux caractères désignant des chiffres. Et non, cela ne devient pas plus court que cela.

Il existe toute une série de ces motifs spéciaux pour spécifier des groupes tels que les nombres (`\d`), les caractères alphanumériques (`\w`), les espaces blancs (`\s`).

#### Révision

* `[123]`  
L'expression entre crochets est un ensemble de caractères  
L'un des caractères correspondra pour passer le test. Juste UN caractère.
* `[0-9]`   
Recherche un chiffre numérique unique entre 0 et 9
* `[0-5]`   
Recherche un chiffre numérique unique entre 0 et 5
* `[a-z]`   
Recherche une lettre unique entre a et z
* `[A-F]`   
Recherche une lettre unique entre A et F
* `[123]+`   
Plus (`+`) recherche une ou plusieurs occurrences des caractères dans l'ensemble. Celui-ci correspond à une sous-chaîne « 23132 » qui se compose de 1, 2 et 3 dans une chaîne plus grande « abc23132 ».
* `|`   
Le symbole pipe signifie **ou**
* `\d`   
Un raccourci pour les chiffres  
Correspond à un chiffre numérique unique.
* `\D`   
Un raccourci pour les caractères non numériques  
Tout ce qui n'est pas un chiffre qui sera correspondre par `\d`

### 3. Correspondance de Récurrence pour Trouver des Doublons

C'est le problème réel que j'essayais de résoudre. J'ai plongé profondément dans les expressions régulières, ce qui a finalement conduit à cet article.

On vous a donné une chaîne. Découvrez si elle a été infusée avec des caractères en double avant le coucher du soleil.

Voici la solution pour les caractères en double apparaissant immédiatement après une occurrence :

```js
let e=/(\w)\1/; 
e.test("abc"); //false 
e.test("abb"); //true
```

L'expression ne correspond à aucune partie de la chaîne `abc` car il n'y a pas de caractères en double en séquence. Donc elle retourne false.

Mais elle correspond à la partie `bb` de la chaîne `abb` et retourne true.

Allez-y, tapez cela sur votre console DevTool. Regardez ça !

Décomposons-le en morceaux compréhensibles.

#### Backslash \ Déchaîné

J'ai été un peu silencieux sur la barre oblique inverse qui a été introduite dans la dernière section. Pour ceux qui ont **été là** et **l'ont fait**, cela n'a peut-être pas été une surprise. Ils ont peut-être **échappé** à la confusion. Mais si vous êtes nouveau dans le monde de la programmation, vous devez en savoir plus sur la barre oblique inverse.

Dans le langage des expressions régulières, la barre oblique inverse est spéciale. La barre oblique inverse modifie la signification des caractères qui les suivent. Cela vous dit quelque chose ?

Que appelez-vous `\n` lorsque vous le rencontrez dans une chaîne ? Oui, une nouvelle ligne. Nous avons quelque chose de similaire ici.

En fait, `\n` est ce que vous utilisez comme motif si vous voulez rechercher une nouvelle ligne. Cela s'appelle `échapper` à la signification habituelle de `n` et lui donner une toute nouvelle apparence appelée `nouvelle ligne`.

* `\d`  
Un raccourci pour les chiffres  
Correspond à un chiffre numérique unique
* `\D`   
Un raccourci pour les caractères non numériques  
Tout ce qui n'est pas un chiffre qui sera correspondre par `\d`
* `\s`   
Raccourci pour un caractère d'espace blanc unique tel qu'un espace, une nouvelle ligne ou une tabulation.
* `\S` Antonyme de `\s`  
tout ce qui n'est pas un espace blanc
* `\w`   
Raccourci pour un caractère alphanumérique  
Correspond à a-z, A-Z, 0-9 et au soulignement _.
* `\W`   
Antonyme de `\w`

#### Correspondances Rappelables

Nous avons commencé cette section avec la solution pour trouver des caractères en double. `/(\w)\1/` a correspondu à `"abb"`. Cela montre l'utilisation de la mémoire et du rappel dans les expressions régulières.

Considérez l'utilisation des parenthèses dans ce format `(expression)`. La chaîne résultante qui correspond à l'expression dans une parenthèse est mémorisée pour une utilisation ultérieure.

`\1` se souvient et utilise la correspondance de la première expression qui est dans les parenthèses. De même, `\2` de la deuxième série de parenthèses. Et ainsi de suite.

Traduisons notre expression `(\w)\1` en anglais simple :

Correspond à n'importe quel caractère alphanumérique sur une chaîne donnée. Souvenez-vous-en comme `\1`. Vérifiez si ce caractère apparaît juste à côté de la première occurrence.

#### Extension 1 — Paires Inverses

Disons que nous voulons trouver deux caractères apparaissant dans l'ordre inverse juste à côté l'un de l'autre. C'est comme `abba`. `ab` est inversé en `ba` et est juste à côté l'un de l'autre.

Voici l'expression :

```js
let e=/(\w)(\w)\2\1/; 
e.test("aabb"); //false 
e.test("abba"); //true 
e.test("abab"); //false
```

Le premier `(\w)` correspond à `a` et s'en souvient comme `\1`. Le deuxième `(\w)` correspond à `b` et s'en souvient comme `\2`. Ensuite, l'expression attend que `\2` se produise en premier suivi de `\1`. Par conséquent, `abba` est la seule chaîne qui correspond à l'expression.

#### Extension 2 — Pas de doublons

Cette fois, nous allons examiner une séquence de caractères sans doublons. Aucun caractère ne doit être suivi du même caractère. Simple et clair.

Voici, regardez la solution :

```js
let e=/^(\w)(?!\1)$/; 
e.test("a"); //true 
e.test("ab"); //false 
e.test("aa"); //false
```

Pas celui que nous voulions, mais proche. Celui du milieu ne devrait pas être faux. Mais nous avons ajouté quelques symboles supplémentaires qui nécessitent des explications. Cela signifie affronter le mousquetaire le plus puissant une fois de plus.

#### Retour du Point d'Interrogation

Souvenez-vous des trois mousquetaires que nous avons rencontrés plus tôt. Le modeste **point d'interrogation est en fait le manipulateur le plus puissant** qui peut faire faire sa volonté à d'autres symboles. C'est-à-dire, si vous prenez la barre oblique inverse pour acquise.

Une combinaison de parenthèses, de point d'interrogation et de point d'exclamation `(?!)`, est appelée une **anticipation**. Une anticipation négative pour être précis. `a(?!b)` correspond à `a` seulement si ce n'est **pas** suivi de `b`.

Dans l'écosystème JavaScript, le point d'exclamation signifie **non**. Mais son cousin CSS fait un demi-tour et `!important` signifie qu'il est en fait très important et ne doit pas être remplacé. J'ai presque fait défiler le tweet de [Chen](https://twitter.com/vijayabharathib/status/910772769964548096) en pensant qu'il était marqué comme non important. Je m'égare.

D'autre part, `(?=)` est une **anticipation** positive. `a(?=b)` correspond à `a` seulement si ce dernier est suivi de `b`.

Nous avions une solution. `(\w)(?!\1)` recherche un caractère sans récurrence. **Mais seulement pour un caractère.** Nous devons le regrouper et rechercher 1 ou plusieurs occurrences de caractères avec l'utilisation du plus (`+`). C'est tout.

```js
let e=/^((\w)(?!\1))+$/; 
e.test("madam"); //false 
e.test("maam"); //false
```

Mais cela ne semble pas fonctionner. Si nous regroupons le motif dans des parenthèses simples comme `((\w)(?!\1))`, le `\1` ne représente pas `(\w)`, il représente la paire de parenthèses de niveau supérieur qui regroupe le motif. Donc il échoue.

Ce dont nous avons besoin est une option de regroupement **oubliable**. C'est là que le point d'interrogation, `?`, contre-attaque. Il s'associe à un deux-points, `(?:)` et efface toute fonction de mémoire que les parenthèses peuvent apporter.

Une dernière fois :

```js
let e=/^(?:(\w)(?!\1))+$/; 
e.test("madam"); //true 
e.test("maam"); //false
```

Cette fois, le premier niveau de parenthèses n'est pas mémorisé, grâce à `?:`, donc, `\1` se souvient de la correspondance retournée par `\w`.

Cela nous aide à utiliser le plus `+` contre le regroupement global pour trouver des paires similaires de caractères du début à la fin, ce qui fonctionne comme par magie.

En anglais, « Recherchez un caractère. Regardez devant pour vous assurer qu'il n'est pas suivi du même caractère. Faites cela du début à la fin pour tous les caractères. »

#### Révision

* `\w` représente tous les caractères alphanumériques  
Si vous mettez 'w' en majuscule et utilisez `\W`, cela signifierait tous les caractères **autres que** alphanumériques
* `( )`   
L'expression entre parenthèses est mémorisée pour une utilisation ultérieure
* `\1` se souvient et utilise la correspondance de la première expression qui est entre parenthèses  
 `\2` de la deuxième série de parenthèses. Et ainsi de suite.
* `a(?!b)`   
Une combinaison de parenthèses, de point d'interrogation et de point d'exclamation (`?!`), est appelée une **anticipation**  
Cela correspond à `a` seulement si ce n'est **pas** suivi de `b`
* `a(?=b)`  
L'autre côté de la pièce  
Correspond à `a` seulement si ce dernier est suivi de `b`. `(?:a)`   
**Regroupement oubliable**  
Recherchez `a` mais ne vous en souvenez pas  
Vous ne pouvez pas utiliser le motif `\1` pour réutiliser cette correspondance

### 4. Séquence Alternée

Le cas d'utilisation est simple. Correspondre à une chaîne qui utilise seulement deux caractères. Ces deux caractères doivent alterner tout au long de la longueur de la chaîne. Deux tests d'échantillon pour « abab » et « xyxyx » suffiront.

Ce n'était pas facile. Je me suis trompé à plusieurs reprises. Cette [réponse](https://stackoverflow.com/questions/45504400/regex-match-pattern-of-alternating-characters) m'a dirigé dans la bonne voie.

Voici la solution :

```js
let e=/^(\S)(?!\1)(\S)(\1\2)*$/; 
e.test("abab"); //true 
e.test("$#$#"); //true 
e.test("#$%"); //false 
e.test("$ $ "); //false 
e.test("xyxyx"); //false
```

C'est là que vous dites, « J'en ai assez ! » et jetez l'éponge.

Mais attendez le moment Aha ! Vous êtes à 3 pieds de l'or, ce n'est pas le bon moment pour arrêter de creuser.

Commençons par comprendre les résultats avant d'arriver à « **comment ?** » `abab` correspond. `$#$#` correspond, ce n'est pas différent de `abab`.

`#$%` échoue car il y a un troisième caractère. `$ $` échoue bien qu'ils soient des paires, car l'espace est exclu dans notre motif.

Tout va bien sauf que `xyxyx` échoue, car notre motif ne sait pas comment gérer ce dernier x. Nous y arriverons.

Jetons un coup d'œil aux outils ajoutés à notre ceinture. Cela va commencer à avoir du sens bientôt.

#### Une pièce à la fois

Vous connaissez déjà la plupart des pièces. `\S` est l'opposé de `\s`. `\S` recherche des caractères non blancs.

Voici la version en anglais simple de `/^(\S)(?!\1)(\S)(\1\2)*$/`.

* Commencez par le début `/^`
* Recherchez un caractère non blanc `(\S)`
* Souvenez-vous-en comme `\1`
* Regardez devant et voyez si le premier caractère n'est pas suivi du même caractère `(?!\1)`.   
Souvenez-vous que c'est une **anticipation négative**.
* Si nous sommes bons jusqu'à présent, recherchez un autre caractère `(\S)`
* Souvenez-vous-en comme `\2`
* Recherchez ensuite **0 ou plusieurs paires des deux premières correspondances** `(\1\2)*`
* Recherchez un tel motif jusqu'à la fin de la chaîne `$/`

Appliquez cela à nos cas de test. `"abab"` et `"$#$#"` correspondent.

#### Fin de la Queue

Après avoir regardé la solution, vous pourriez penser que cela ne demande pas une section séparée. Mais la simplicité de cela est élégante. Réparons ce cas d'échec `xyxyx`. Comme nous l'avons vu, le dernier x traînard est le problème. Nous avons une solution pour `xyxy`. Tout ce dont nous avons besoin est un motif pour dire « Recherchez une occurrence facultative du premier caractère ».

Comme d'habitude, commençons par la solution.

```js
let e=/^(\S)(?!\1)(\S)(\1\2)*\1?$/; e.test("xyxyx"); //true e.test("$#$#$"); //true
```

Le point d'interrogation frappe encore. Il n'y a pas moyen de lui échapper. Il vaut mieux en faire notre allié que notre ennemi. Un point d'interrogation `?` après un caractère ou un motif signifie 0 ou 1 correspondance pour le motif précédent. Il n'est pas gourmand en caractères.

Dans notre cas, `\1?` signifie, 0 ou 1 correspondance du premier caractère mémorisé par la première série de parenthèses.

Facile. Détendez-vous.

#### Révision

* `\S`   
Représente tous les caractères à l'exclusion des espaces blancs tels qu'un espace et des nouvelles lignes  
Notez qu'il s'agit d'un S majuscule
* `a*`   
L'astérisque ou l'étoile, recherche 0 ou plusieurs occurrences du caractère précédent. Dans ce cas, il s'agit de 0 ou plusieurs `a`  
Souvenez-vous du plus (`+`) qui recherche 1 ou plusieurs ? Oui, ces gars sont cousins.
* `a(?!b)`   
Cette combinaison de parenthèses, de point d'interrogation et de point d'exclamation (`?!`) est appelée une **anticipation**.   
Cela correspond à `a` seulement si ce n'est pas suivi de `b`.   
Par exemple, il correspond à `a` dans `aa`, `ax`, `a$` mais ne correspond pas à `ab`  
Bien qu'il utilise des parenthèses, il ne mémorise pas le caractère correspondant après `a`.
* `\s`   
Le `s` minuscule correspond à un caractère d'espace blanc unique tel qu'un espace ou une nouvelle ligne.
* `a(?=b)`   
Cela correspond à `a` qui est suivi de `b`.
* `^ab*$`   
Vous pouvez penser que cela se traduit par 0 ou plusieurs occurrences de `ab`, mais il correspond à `a` suivi de 0 ou plusieurs `b`  
Par exemple : Cela correspond à `abbb`, `a` et `ab`, mais ne correspond pas à `abab`
* `^(ab)*$`   
Cela correspond à 0 ou plusieurs paires de `ab`  
Cela signifie qu'il correspondra à la chaîne vide `""`, `ab` et `abab`, mais pas à `abb`
* `a?`   
`?` correspond à 0 ou 1 occurrence du caractère ou du motif précédent  
 `\1?` correspond à 0 ou 1 récurrence de la première correspondance mémorisée

### 5. Correspondre à une adresse e-mail

#### Avertissement pour la Production

Les expressions régulières seules peuvent ne pas aider à valider les e-mails. Certains soutiendraient même que les expressions régulières ne devraient pas être utilisées car elles ne peuvent jamais correspondre à 100 % des e-mails.

Pensez à tous les noms de domaine fantaisistes qui apparaissent. Considérez également l'inclusion de symboles dans les adresses e-mail, tels que le point (.) et le plus (+).

Vous devez valider l'e-mail deux fois. Une fois du côté client pour aider les utilisateurs à éviter les adresses mal orthographiées. Commencez par une balise d'entrée sémantique de type `<input type='email'>. Certains navigateurs la valident automatiquement sans aucun script supplémentaire en front-end.

Validez-la une fois de plus sur le serveur en envoyant réellement un e-mail de confirmation.

N'en avez-vous pas vu un récemment ? Essayez simplement de vous abonner à ce [pineboat](https://www.pineboat.in/). Vous recevrez un e-mail réel vous demandant de confirmer qu'il est le vôtre. Cette confirmation est une preuve solide que votre e-mail est valide.

C'était une navigation de plaisir, n'est-ce pas ?

#### RegEx pour l'E-mail

Maintenant que nous avons ajouté l'avertissement, vous voulez réellement voir un motif, n'est-ce pas ? Non, cherchez une expression régulière pour une adresse e-mail. Un tel résultat du [module perl](http://www.ex-parrot.com/~pdw/Mail-RFC822-Address.html) s'étend sur plus d'une page.

Donc, je ne vais même pas essayer. De si longues expressions régulières sont générées par des ordinateurs via des constructeurs de motifs. Pas pour de simples mortels comme nous.

### 6. Correspondre à un Mot de Passe Fort

Si vous êtes un amateur de café, c'est le bon moment pour en prendre un fort. Parce que nous sommes à la dernière section de cet article, mais la plus longue jusqu'à présent.

Elle introduit très peu de nouveaux opérateurs et motifs. Mais elle réutilise de nombreux motifs. Comme d'habitude, nous réservons le plus court optimisé pour la fin.

La plage ASCII est la meilleure partie de cet article. Parce que je l'ai apprise en recherchant pour cet article.

Maintenant, le problème. Vous souvenez-vous de ce formulaire d'inscription qui a pris plusieurs tentatives avant de pouvoir répondre à leurs exigences de mot de passe fort ? Faible, bon, fort et très fort ? Oui, nous allons construire cette validation.

Le mot de passe doit :

* avoir un minimum de 4 caractères
* contenir des minuscules
* contenir des majuscules
* contenir un chiffre
* contenir un symbole

C'est un peu délicat. Une fois que vous commencez à consommer des lettres, vous ne pouvez pas revenir en arrière pour vérifier si elles répondent à une autre condition. C'est là que se trouve notre indice. **Nous ne pouvons pas regarder en arrière, mais nous pouvons regarder devant !**

#### Longueur de la chaîne

Testons d'abord si le mot de passe de la chaîne fait 4 caractères de long. Assez simple. Utilisez `.length` sur la chaîne de mot de passe. Fini, non ? Non, qui a besoin d'une solution simple ? Ajoutons un peu d'épice.

```js
//expression avec juste une anticipation
//ne consommerait aucun caractère
e1=/^(?=.{4,})$/; 
e1.test("abc") //false
e1.test("abcd") //false  

//après l'anticipation, 
//un motif pour consommer le caractère est nécessaire.
e2=/^(?=.{4,}).*$/; 
e2.test("abc") //false 
e2.test("abcd") //true
```

* Vous vous souvenez peut-être de `(?=)` de notre travail précédent sur [« pas de doublons »](https://www.pineboat.in/post/regular-expressions-your-ally/#extension-2-no-duplicates). C'est une utilisation de l'anticipation  
Elle ne consomme aucun caractère
* Le point (`.`) est un caractère intéressant  
Il signifie, **n'importe quel caractère**.
* `{4,}`   
Représente au moins 4 caractères précédents sans limite maximale
* `\d{4}`   
Rechercherait exactement 4 chiffres
* `\w{4,20}`   
Rechercherait de 4 à 20 caractères alphanumériques

Traduisons `/^(?=.{4,})$/`. « Commencez par le début de la chaîne. Regardez devant pour au moins 4 caractères. Ne vous souvenez pas de la correspondance. Revenez au début et vérifiez si la chaîne se termine là. »

Cela ne semble pas correct. N'est-ce pas ? Au moins le dernier morceau.

C'est pourquoi nous avons apporté la variation `/^(?=.{4,}).*$/`. Un point et une étoile supplémentaires. Cela se lit comme ceci, « Commencez par le début. Regardez devant pour 4 caractères. Ne vous souvenez pas de la correspondance. Revenez au début. Consommez tous les caractères en utilisant `.*` et voyez si vous atteignez la fin de la chaîne. »

Cela a du sens maintenant. N'est-ce pas ?

C'est pourquoi `abc` échoue et `abcd` passe le motif.

#### Au Moins Un Chiffre

Cela va être facile.

```js
e=/^(?=.*\d+).*$/ 
e.test(""); //false 
e.test("a"); //false 
e.test("8"); //true 
e.test("a8b"); //true 
e.test("ab890"); //true
```

Commencez par le début de la chaîne `/^`. Regardez devant pour 0 ou plusieurs caractères `?=.*`. Vérifiez si 1 ou plusieurs chiffres suivent `\d+`. Une fois qu'il correspond, revenez au début (parce que nous étions dans l'anticipation). Consommez tous les caractères de la chaîne jusqu'à la fin de la chaîne `.*$/`.

#### Au Moins Une Lettre Minuscule

Cela suit le même motif que ci-dessus.

```js
e=/^(?=.*[a-z]+).*$/; 
e.test(""); //false 
e.test("A"); //false 
e.test("a"); //true
```

Traduction ? Bien sûr. « Commencez par le... d'accord. » Au lieu de `\d+`, nous avons `[a-z]+` qui est un ensemble de caractères de lettres de `a` à `z`.

#### Au Moins Une Lettre Majuscule

Ne surchargeons pas. `[A-Z]` au lieu de `[a-z]` de la section précédente suffira.

#### Au Moins Un Symbole

Cela va être un défi. Une façon de faire correspondre les symboles est de placer une liste de symboles dans un ensemble de caractères. `/^(?=.*[-+=_)(\*&\^%\$#@!~:;|\}]{[/?.>,<]+).*$/.test`("$") C'est tous les symboles dans un ensemble de caractères. Correctement échappés lorsque nécessaire. Il me faudrait des mois pour l'écrire en anglais simple.

Donc, pour nous épargner à tous une douleur éternelle, voici une solution simple :

```js
//considère l'espace comme symbole 
let e1; 
e1=/^(?=.*[^a-zA-Z0-9])[ -~]+$/ 
e1.test("_"); //true 
e1.test(" "); //true  

//ne prend pas l'espace 
let e2; 
e2=/^(?=.*[^a-zA-Z0-9])[!-~]+$/ 
e2.test(" "); //false 
e2.test("_"); //true  

//l'exception du soulignement 
let e3; 
e3=/^(?=.*[\W])[!-~]+$/ 
e3.test("_"); //false
```

Attendez, qu'est-ce que ce `^` qui revient du milieu de nulle part ? Si vous êtes arrivé jusqu'ici, c'est là que vous réalisez que ce `^` innocent et sans prétention qui marque le début d'une chaîne est un agent double. Ce qui signifie que la fin n'est pas trop loin. Il a été exposé.

Dans un ensemble de caractères, `^` nie l'ensemble de caractères. C'est-à-dire, `[^a-z]` signifie, n'importe quel caractère autre que `a` à `z`.

`[^a-zA-Z0-9]` signifie alors n'importe quel caractère autre que les lettres minuscules, les lettres majuscules et les chiffres.

Nous aurions pu utiliser `\W` au lieu du long ensemble de caractères. Mais `\W` signifie tous les caractères alphanumériques **y compris le soulignement _.** Comme vous pouvez le voir dans le troisième ensemble d'exemples ci-dessus, cela n'acceptera pas le soulignement comme un symbole valide.

#### Plage de Caractères

Le cas curieux de `[!-~]`. Ils se trouvent côte à côte sur le clavier, mais leurs valeurs ASCII sont diagonalement opposées.

Vous vous souvenez de a-z ? A-Z ? 0-9 ? Ce ne sont pas des constantes. Elles sont en fait basées sur la plage ASCII de leurs valeurs.

La [table ASCII](http://www.asciitable.com/) contient 125 caractères. zéro (0) à 31 ne nous concernent pas. L'espace commence à 32 et va jusqu'à 126 qui est le tilde (~). Le point d'exclamation est 33.

Ainsi, `[!-~]` couvre tous les symboles, lettres et chiffres dont nous avons besoin. L'idée de cette solution vient d'une [autre solution](https://stackoverflow.com/questions/8359566/regex-to-match-symbols) au problème des symboles.

#### Assembler les Troupes

En mettant tout cela ensemble, nous obtenons ce bel morceau d'expression régulière `/^(?=.{5,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)(?=.*[^\w])[ -~]+$/`.

Cela commence à nous hanter et à nous intimider. Bien que nous les ayons étudiés individuellement.

C'est là que la syntaxe pour construire dynamiquement l'objet d'expression est utile. Nous allons construire chaque pièce séparément et les assembler plus tard.

```js
//commencez par le préfixe 
let p = "^"; 

//regardez devant  
// min 4 caractères 
p += "(?=.{4,})"; 
// minuscules 
p += "(?=.*[a-z]+)"; 
// majuscules 
p += "(?=.*[A-Z]+)"; 
// chiffres 
p += "(?=.*\\d+)"; 
// symboles 
p += "(?=.*[^ a-zA-Z0-9]+)"; 
//fin des anticipations  

//consommation finale 
p += "[ -~]+";  
//suffixe 
p += "$"; 

//Construire RegEx 
let e = new RegEx(p); 
// tests 
e.test("aB0#"); //true  
e.test(""); //false 
e.test("aB0"); //false 
e.test("ab0#"); //false 
e.test("AB0#"); //false 
e.test("aB00"); //false 
e.test("aB!!"); //false  

// l'espace est sous notre contrôle 
e.test("aB 0"); //false 
e.test("aB 0!"); //true
```

Si vos yeux ne sont pas encore fatigués, vous aurez remarqué deux syntaxes étranges dans le code ci-dessus.

* Premièrement, nous n'avons pas utilisé `/^`, mais seulement `^`. Nous n'avons pas utilisé `$/` pour terminer l'expression, mais seulement `$`.  
La raison est que le constructeur `RegEx` ajoute automatiquement les barres obliques de début et de fin pour nous.
* Deuxièmement, pour correspondre aux chiffres, nous avons utilisé `\\d` au lieu du `\d` habituel. Cela est dû au fait que la variable `p` est simplement une chaîne normale entre guillemets doubles. Pour insérer une barre oblique inverse, vous devez échapper la barre oblique inverse elle-même.   
`\\d` se résout en `\d` dans le constructeur `RegEx`

Apparemment, il devrait y avoir des validations côté serveur pour les mots de passe également. Pensez aux vulnérabilités d'injection SQL si votre framework ou langage ne les gère pas déjà.

### 7. Conclusion

Cela nous amène à la fin de l'histoire. Mais c'est le début d'un voyage.

Nous avons à peine effleuré la partie de correspondance de motifs de RegEx avec la méthode `test`. La méthode `exec` s'appuie sur cette fondation pour retourner des sous-chaînes correspondantes basées sur le motif.

L'objet String possède des méthodes telles que `match`, `search`, `replace` et `split` qui utilisent largement les expressions régulières.

J'espère que cela vous lancera dans l'exploration de ces capacités plus avant avec une compréhension solide de la composition de motifs pour RegEx.

### 8. Appel à l'Action

Non, après toutes les difficultés que nous avons traversées, je ne vais pas vous demander de vous abonner.

Faites simplement de bons logiciels.

Si l'un des blocs de code présentés ici ne fonctionne pas, laissez un commentaire sur ce [problème github](https://github.com/pineboat/pineboat.github.io/issues/3) que j'ai créé spécialement pour cet article.

J'espère que cela a été utile ! Partagez-le si d'autres pourraient en bénéficier.

Vous avez été merveilleux. J'apprécie votre temps. Ce contenu est bien long selon les normes récentes. Merci d'avoir lu.

Publié à l'origine sur [www.pineboat.in](https://www.pineboat.in/post/regular-expressions-your-ally/).