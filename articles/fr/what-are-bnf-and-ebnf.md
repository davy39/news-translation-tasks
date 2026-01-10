---
title: Qu'est-ce que BNF et EBNF en programmation ?
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2023-07-17T17:26:21.000Z'
originalURL: https://freecodecamp.org/news/what-are-bnf-and-ebnf
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/ryan-wallace-azA1hLbjBBo-unsplash.jpg
tags:
- name: programming languages
  slug: programming-languages
- name: syntax
  slug: syntax
seo_title: Qu'est-ce que BNF et EBNF en programmation ?
seo_desc: 'As programmers, we communicate with computers through many languages: Python,
  JavaScript, SQL, C... you name it. But do you know how the creators of these languages
  precisely describe their syntax to us, leaving no room for doubt?

  They could''ve relie...'
---

En tant que programmeurs, nous communiquons avec les ordinateurs à travers de nombreux langages : Python, JavaScript, SQL, C... vous l'appelez comme vous voulez. Mais savez-vous comment les créateurs de ces langages décrivent précisément leur syntaxe pour nous, sans laisser de place au doute ?

Ils auraient pu s'appuyer sur l'anglais simple, mais cela n'aurait pas été une bonne solution en raison de la verbosité et de l'ambiguïté potentielles. Ils ont donc utilisé des langages spécialement conçus pour cela.

Dans cet article, vous apprendrez deux de ces langages largement utilisés : BNF et EBNF.

Un autre aspect fascinant de ces langages spéciaux ou notations est que vous pouvez écrire la grammaire de votre propre langage en les utilisant et la donner en entrée à certains programmes informatiques magiques appelés "générateurs d'analyseurs". Ceux-ci peuvent produire d'autres programmes capables d'analyser n'importe quel texte selon la grammaire que vous avez utilisée. N'est-ce pas incroyable ?

Cette fonctionnalité peut vous faire gagner beaucoup de temps, car écrire manuellement de tels programmes est difficile et chronophage.

Avant d'apprendre (E)BNF, il est utile de pouvoir distinguer la syntaxe de la sémantique. Commençons donc par là.

## Syntaxe vs Sémantique dans les Langages de Programmation

La syntaxe fait référence à la structure des éléments d'un langage en fonction de son type. D'autre part, la sémantique concerne le sens.

Quelque chose écrit syntaxiquement correctement dans un langage peut être complètement dénué de sens. Et aucun texte ne peut être significatif si sa syntaxe est incorrecte.

Deux des phrases les plus célèbres concernant la syntaxe et la sémantique sont [composées par Noam Chomsky](https://en.wikipedia.org/wiki/Colorless_green_ideas_sleep_furiously) :

1. Colorless green ideas sleep furiously.
2. Furiously sleep ideas green colorless.

La syntaxe de la première phrase est correcte mais elle est dénuée de sens. Et comme la seconde est syntaxiquement incorrecte, elle est loin d'être significative.

Cela est également vrai pour les langages de programmation. Regardons les deux extraits de code JavaScript suivants pour voir ce que je veux dire.

Le code suivant est syntaxiquement correct mais sémantiquement incorrect car il n'est pas possible de réassigner quelque chose à une variable constante :

```js
const name = "Palash";
name = "Akash";

```

Ce qui suit est syntaxiquement incorrect et n'a donc même aucune chance d'être sémantiquement correct.

```js
"Palash" = const name;
"Akash" = name;

```

Vous pouvez vérifier la syntaxe de votre code JavaScript en ligne avec un outil comme le [Validateur de Syntaxe Esprima](https://esprima.org/demo/validate.html).

Il y a deux autres concepts que vous devez comprendre avant d'apprendre à lire BNF/EBNF.

## Terminals et Non-Terminals

BNF/EBNF est généralement utilisé pour spécifier la grammaire d'un langage. La grammaire est un ensemble de _règles_ (également appelées _règles de production_). Ici, le langage ne fait référence à rien d'autre qu'à un ensemble de chaînes qui sont valides selon les règles de sa grammaire.

Une description de grammaire BNF/EBNF est une liste non ordonnée de règles. Les _règles_ sont utilisées pour définir des _symboles_ à l'aide d'autres symboles.

Vous pouvez considérer les _symboles_ comme les éléments de base de la grammaire. Il existe deux types de symboles :

* **Terminal (ou Symbole terminal)** : Les terminaux sont des chaînes écrites entre guillemets. Ils sont destinés à être utilisés tels quels. Rien n'est caché derrière eux. Par exemple `"freeCodeCamp"` ou `"firefly"`.
* **Non-terminal (ou Symbole non-terminal)** : Parfois, nous avons besoin d'un nom pour faire référence à autre chose. Ceux-ci sont appelés _non-terminaux_. En BNF, les noms des _non-terminaux_ sont écrits entre chevrons (par exemple `<statement>`), tandis qu'en EBNF, ils n'utilisent généralement pas de chevrons (par exemple `statement`).

L'ensemble du langage est dérivé d'un seul symbole _non-terminal_. Cela s'appelle le **symbole** **start** ou **root** de la grammaire. Par convention, il est écrit comme le premier non-terminal dans la description de la grammaire BNF/EBNF.

Enfin, vous êtes prêt à apprendre BNF. C'est plus facile que vous ne le pensez.

## Qu'est-ce que BNF ?

BNF signifie **B**ackus**N**aur **F**orm qui résulte principalement des contributions de [John Backus](https://en.wikipedia.org/wiki/John_Backus) et [Peter Naur](https://en.wikipedia.org/wiki/Peter_Naur).

La syntaxe de BNF/EBNF est si simple que beaucoup de gens ont adopté leurs styles. Donc, dans différents endroits, vous verrez probablement différents styles. Si la syntaxe est différente des conventions, cela est généralement documenté là-bas. Dans cet article, j'utiliserai un style particulier, juste pour garder les choses simples.

Voici un exemple d'une simple _règle de production_ en BNF :

```bnf
<something> ::= "content" 

```

Chaque règle en BNF (également en ENBF) a trois parties :

* **Côté gauche** : Ici, nous écrivons un non-terminal pour le définir. Dans l'exemple ci-dessus, il s'agit de `<something>`.
* **`::=`** : Ce groupe de caractères sépare le **côté gauche** du **côté droit**. Lisez ce symbole comme "est défini comme".
* **Côté droit** : La définition du non-terminal spécifié du côté droit. Dans l'exemple ci-dessus, il s'agit de `"content"`.

Le `<something>` ci-dessus est juste une chose fixe. Voyons maintenant toutes les façons dont vous pouvez composer un _non-terminal_.

### Comment composer un non-terminal

BNF nous offre deux méthodes :

* Séquençage
* Choix

Vous pouvez simplement écrire une combinaison d'un ou plusieurs terminaux ou non-terminaux dans une séquence et le résultat est leur concaténation, les non-terminaux étant remplacés par leur contenu. Par exemple, vous pouvez exprimer votre petit-déjeuner de la manière suivante :

```bnf
<breakfast> ::= <drink> " and biscuit"
<drink> ::= "tea"

```

Cela signifie que la seule option pour le petit-déjeuner pour vous est `"tea and biscuit"`. Notez que ici, l'ordre des symboles est important.

Disons qu'un jour vous voulez boire du café au lieu de thé. Dans ce cas, vous pouvez exprimer vos possibles éléments de petit-déjeuner comme ci-dessous :

```bnf
<breakfast> ::= <drink> " and biscuit"
<drink> ::= "tea" | "coffee"

```

L'opérateur `|` indique que les parties séparées par lui sont des choix. Ce qui signifie que le non-terminal à gauche peut être n'importe quelle partie. Ici, l'ordre est _sans importance_, c'est-à-dire qu'il n'y a pas de différence entre `"tea" | "coffee` et `"coffee" | "tea"`.

C'est vraiment tout ce que vous devez savoir sur BNF pour le lire et le comprendre et même exprimer la syntaxe de votre propre langage en l'utilisant. Croyez-le ou non, c'est aussi simple que cela. Et pourtant, il peut être utilisé pour décrire la syntaxe de nombreux langages de programmation et d'autres types de langages de codage.

Ce qui rend possible de décomposer facilement la syntaxe complexe des langages de programmation est la capacité à définir des symboles non-terminaux de manière récursive.

En tant qu'exemple simple, voyons comment vous exprimez un ou plusieurs chiffres en BNF :

```bnf
<digits> ::= <digit> | <digit> <digits>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

```

Si vous voulez voir un exemple simple de grammaire BNF dans le monde réel, consultez : [Notation Semver](https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions).

## Qu'est-ce que EBNF ?

BNF est bien, mais parfois il peut devenir verbeux et difficile à interpréter. EBNF (qui signifie **E**xtended **B**ackus**N**aur **F**orm) peut vous aider dans ces cas. Par exemple, l'exemple précédent peut être écrit en EBNF comme ci-dessous :

```ebnf
digits = digit { digit }
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

```

Les accolades ci-dessus signifient que leur partie interne peut être répétée 0 ou plusieurs fois. Cela libère votre esprit de se perdre dans la récursion.

Un fait intéressant est que tout ce que vous pouvez exprimer en EBNF peut également être exprimé en BNF.

EBNF utilise généralement une notation légèrement différente de BNF. Par exemple :

* `::=` devient simplement `=`.
* Il n'y a pas de chevrons autour des non-terminaux.

```ad-info
Pour la concaténation, au lieu de la juxtaposition, certains préfèrent `,` pour être plus explicites. Cependant, je ne l'utiliserai pas ici.

```

Ne supposez pas que ces styles soient universels. Il existe plusieurs variantes et elles sont généralement claires d'après le contexte. La chose la plus importante sur laquelle se concentrer est les nouvelles opérations qu'il offre, comme les accolades que nous avons vues ci-dessus.

EBNF étend BNF en ajoutant les 3 opérations suivantes :

* Option
* Répétition
* Groupement

### Option

L'option utilise des crochets pour rendre le contenu interne facultatif. Exemple :

```ebnf
thing = "water" [ "melon" ]

```

Donc, le `thing` ci-dessus est soit `water` soit `watermelon`.

### Répétition

Les accolades indiquent que le contenu interne peut être répété 0 ou plusieurs fois. Vous avez déjà vu un bon exemple ci-dessus. Voici un exemple très simple juste pour solidifier l'idée dans votre esprit :

```ebnf
long_google = "Goo" { "o" } "gle"

```

Donc `"Google"`, `"Gooogle"`, `"Gooooooogle"` sont tous des `long_google` non-terminaux valides.

### Groupement

Les parenthèses peuvent être utilisées pour indiquer le groupement. Cela signifie que tout ce qu'elles enveloppent peut être remplacé par l'une des chaînes valides que les contenus du groupe représentent selon les règles de EBNF. Par exemple :

```ebnf
fly = ("fire" | "fruit") "fly"

```

Ici, `fly` est soit `"firefly"` soit `"fruitfly"`.

Avec BNF, nous n'aurions pas pu faire cela en une ligne. Cela ressemblerait à ce qui suit en BNF :

```ebnf
<fly> ::= <type> "fly"
<type> ::= "fire" | "fruit"

```

## Le BNF Playground

Il existe un très beau terrain de jeu en ligne pour BNF et EBNF : [<BNF> Playground](https://bnfplayground.pauliankline.com/).

Je vous recommande de le consulter et de jouer avec. Il utilise une notation légèrement différente, alors lisez la section "Grammar Help" au préalable.

Il peut tester si une chaîne est valide selon la grammaire que vous avez entrée. Il peut également générer des chaînes aléatoires basées sur votre grammaire !

Pour le plaisir, voici la syntaxe d'un texte de type poème (crédit à chatGPT) :

```ebnf
<poem> ::= <line> | <line> "\n" <poem>
<line> ::= <noun_phrase> " " <verb_phrase> " " <adjective>
<noun_phrase> ::= "the " <adjective> " " <noun> | <noun>
<verb_phrase> ::= <verb> | <verb> " " <adverb>
<adjective> ::= "red" | "blue" | "green" | "yellow"
<noun> ::= "sky" | "sun" | "grass" | "flower"
<verb> ::= "shines" | "glows" | "grows" | "blooms"
<adverb> ::= "brightly" | "slowly" | "vividly" | "peacefully"

```

Allez-y et copiez-collez-le dans le terrain de jeu et appuyez sur le bouton "Generate Random" pour obtenir quelques lignes pour la plupart dénuées de sens d'un poème grammaticalement correct.

## Conclusion

BNF et EBNF sont des notations simples et puissantes pour écrire ce que les informaticiens appellent _grammaire hors contexte_.

En termes simples, cela signifie que l'expansion d'un non-terminal ne dépend pas du contexte (symboles environnants), c'est-à-dire qu'elle est hors contexte. C'est la forme de grammaire la plus largement utilisée pour formaliser la syntaxe des langages de codage.

Voici quelques ressources que vous pourriez trouver intéressantes :

- [EBNF : Comment décrire la grammaire d'un langage](https://tomassetti.me/ebnf/)
- [Le langage des langages](https://matt.might.net/articles/grammars-bnf-ebnf/)
- Générateurs d'analyseurs :
  - [ANTLR](https://www.antlr.org/), un générateur d'analyseurs très puissant capable d'écrire des analyseurs dans de nombreux langages.
  - Si vous êtes une personne JavaScript comme moi et que vous voulez commencer avec un générateur d'analyseurs, jetez un œil à [nearly.js](https://nearley.js.org/) pour un début en douceur.

Voici quelques grammaires réelles écrites en utilisant BNF/EBNF ou des notations similaires que vous pourriez trouver intéressantes :

* [Lisp](https://iamwilhelm.github.io/bnf-examples/lisp)
* [Lua](https://www.lua.org/manual/5.4/manual.html#9)
* [Semver](https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions)
* [JavaScript](https://tc39.es/ecma262/multipage/grammar-summary.html#sec-grammar-summary)
* [JSX](https://facebook.github.io/jsx/)
* [Python](https://docs.python.org/3/reference/grammar.html)
* [Syntaxe de définition de valeur en CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Value_definition_syntax)

Merci d'avoir lu. Faites-moi savoir sur [Twitter](https://twitter.com/ashutoshbw) si vous avez des questions ou si vous avez trouvé cet article utile. Bon apprentissage !

Photo par [Ryan Wallace](https://unsplash.com/@accrualbowtie?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/azA1hLbjBBo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)