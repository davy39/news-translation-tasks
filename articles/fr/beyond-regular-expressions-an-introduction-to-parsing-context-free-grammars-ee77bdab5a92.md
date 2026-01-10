---
title: 'Au-delà des expressions régulières : Une introduction à l''analyse des grammaires
  hors contexte'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T19:12:10.000Z'
originalURL: https://freecodecamp.org/news/beyond-regular-expressions-an-introduction-to-parsing-context-free-grammars-ee77bdab5a92
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yyZM9V_77Q-uAj0F
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
seo_title: 'Au-delà des expressions régulières : Une introduction à l''analyse des
  grammaires hors contexte'
seo_desc: 'By Christopher Diggins

  An important and useful tool that is already a part of most programmers’ arsenals
  is the trusty regular expression. But beyond that lie context-free grammars. This
  is a simple concept with a fancy name.

  A regular expression is ...'
---

Par Christopher Diggins

Un outil important et utile qui fait déjà partie de l'arsenal de la plupart des programmeurs est l'expression régulière fiable. Mais au-delà de cela se trouvent les grammaires hors contexte. C'est un concept simple avec un nom sophistiqué.

Une expression régulière est une méthode de validation et de recherche de motifs dans le texte. Les types de motifs (aka grammaires) qui peuvent être décrits et détectés à l'aide d'une expression régulière sont appelés langues régulières. Les langues régulières sont les plus simples des langues formelles dans la hiérarchie de Chomsky.

Les expressions régulières sont excellentes pour trouver ou valider de nombreux types de motifs simples, par exemple les numéros de téléphone, les adresses e-mail et les URL. Cependant, elles sont insuffisantes lorsqu'elles sont appliquées à des motifs qui peuvent avoir une structure récursive, tels que :

* Les balises d'ouverture/fermeture HTML / XML
* Les accolades d'ouverture/fermeture {/} dans les langues de programmation
* Les parenthèses d'ouverture/fermeture dans les expressions arithmétiques

Pour analyser ces types de motifs, nous avons besoin de quelque chose de plus puissant. Nous pouvons passer au niveau suivant des grammaires formelles appelées grammaires hors contexte (CFG).

### Analyse des expressions mathématiques

L'analyse de l'ensemble de toutes les expressions mathématiques dépasse la capacité d'une véritable expression régulière. La raison en est que celles-ci peuvent contenir des paires de parenthèses imbriquées de manière arbitrairement profonde.

Par exemple, considérons l'expression : `(2 + (3 * (74)))`

Remarquez que la structure de l'expression arithmétique est effectivement un arbre :

```
  + / \ 2   *   / \  3   -     / \     7 4
```

La structure arborescente générée comme résultat de l'exécution d'un analyseur CFG est appelée un arbre d'analyse.

### Description des grammaires hors contexte

Il existe deux méthodes populaires pour exprimer les grammaires CFG :

1. Forme de Backus-Naur étendue (EBNF)  décrit une CFG en termes de règles de production. Ce sont des règles qui, lorsqu'elles sont appliquées, peuvent générer toutes les phrases légales possibles dans la langue.
2. Grammaire d'expression d'analyse (PEG)  décrit une CFG en termes de règles de reconnaissance. Ce sont des règles qui peuvent être utilisées pour faire correspondre des phrases valides dans la langue.

Le formalisme PEG présente l'avantage sur EBNF que la cartographie vers un analyseur est sans ambiguïté et peut être facilement automatisée.

Ce qui suit est un PEG simple [tiré de sa page Wikipedia](https://en.wikipedia.org/wiki/Parsing_expression_grammar) décrivant des formules mathématiques qui appliquent les quatre opérations de base à des entiers non négatifs.

```
Expr  SumSum  Product ((+ / -) Product)*Product  Value ((* / /) Value)*Value  [09]+ / ( Expr )
```

En anglais simple, nous pouvons lire ceci comme :

* `Expr` est un `Sum`
* `Sum` est un `Product` suivi de zéro ou plusieurs sous-motifs qui consistent en un + ou - suivi d'un `Product`
* `Product` est un `Value` suivi de zéro ou plusieurs sous-motifs qui consistent en un * ou / suivi d'un `Value`
* `Value` est soit un ou plusieurs membres de l'ensemble de caractères {0,..9}, soit il s'agit d'une parenthèse ouverte ( suivie d'un `Expr` et d'une parenthèse fermante ).

### Générateurs d'analyseurs versus bibliothèques d'analyse

En supposant que vous n'êtes pas le genre de personne qui aime réinventer la roue (ce qui n'est pas un problème en soi), il existe généralement deux options pour créer un analyseur :

1. **Utiliser un générateur d'analyseur**  un outil qui génère le code source pour un analyseur à partir d'une définition abstraite de l'analyseur. Certains exemples populaires en JavaScript incluent [Jison](http://jison.org/), [PEG.js](https://pegjs.org/), [nearley](http://nearley.js.org/), et [ANTLR](http://www.antlr.org/).

2. **Utiliser une bibliothèque d'analyse**  une bibliothèque qui permet l'expression des règles d'analyse sous forme d'API. Certains exemples en JavaScript incluent [Myna](https://github.com/cdiggins/myna-parser), [Parsimmon](https://github.com/jneen/parsimmon), et [Chevrotain](https://github.com/SAP/chevrotain).

Ma préférence est d'utiliser des bibliothèques d'analyse, car elles sont plus faciles à comprendre, à déboguer, à maintenir et à personnaliser.

### Écriture d'analyseurs en TypeScript / JavaScript en utilisant la bibliothèque d'analyse Myna

![Image](https://cdn-media-1.freecodecamp.org/images/1*YvovmmxWoIEpHKQ1Fu6cxw.png)
_Common Myna par Mahesh Iyer de Wikimedia Commons_

Récemment, un projet sur lequel je travaillais ([le langage Heron](https://github.com/cdiggins/heron-language/)) nécessitait une bibliothèque d'analyse qui pouvait s'exécuter dans le navigateur. J'ai trouvé la complexité et les frais généraux des bibliothèques existantes trop importants. Étant donné que j'avais une expérience précédente dans l'écriture de bibliothèques d'analyse en C++ et C#, j'ai décidé d'écrire une bibliothèque d'analyse appelée **Myna** en utilisant TypeScript.

Myna utilise la syntaxe fluide (chaînage de méthodes) pour faciliter la définition d'un analyseur comme un ensemble de règles (sous-analyseur) qui ressemblent à une grammaire PEG.

L'exemple suivant est tiré du dépôt GitHub de Myna :

### De l'arbre de syntaxe concrète (CST) à l'arbre de syntaxe abstraite (AST)

Lorsque l'analyseur traite l'entrée, chaque règle appariée avec succès (aka production de grammaire) peut être mappée à un nœud dans l'arbre d'analyse. Ce mappage littéral des règles de production aux nœuds dans un arbre est un arbre de syntaxe concrète (CST).

Dans certains cas, le CST est d'une utilité limitée car il contient beaucoup de désordre syntaxique, par exemple des commentaires dans le code source, ou si un littéral de chaîne a des guillemets doubles ou simples. Il peut contenir des résultats de règles qui sont créées pour faciliter l'utilisation de la grammaire, mais ne représentent pas la structure arborescente prévue pour l'analyse.

La chose la plus simple à faire est de ne créer des nœuds dans l'arbre de sortie que pour des règles spécifiques et de sauter les autres règles. Cette version simplifiée de l'arbre d'analyse est appelée un arbre de syntaxe abstraite (AST). Il peut y avoir plusieurs passes effectuées sur un AST pour le transformer en représentations AST alternatives, afin de simplifier les étapes de traitement ultérieures.

Dans Myna, un AST est généré en créant des nœuds à partir de règles étiquetées avec la propriété `ast`. Techniquement, cette propriété retourne une nouvelle règle qui a une propriété interne définie qui indique à l'analyseur de générer un nœud d'analyse dans l'arbre d'analyse.

### Utilisation de l'arbre de syntaxe abstraite généré par Myna

Voici un exemple d'utilisation d'un analyseur défini par Myna dans "Node.JS" pour évaluer une expression arithmétique :

### Mots de la fin

Si vous êtes intéressé à en apprendre davantage sur la création et l'utilisation d'analyseurs, que la bibliothèque Myna réponde ou non à vos besoins spécifiques, je vous encourage à prendre un peu de temps pour lire le code source de la bibliothèque d'analyse Myna.

Myna a été écrit en TypeScript (qui a une syntaxe familière pour la plupart des programmeurs), est contenu dans un seul fichier sans dépendances, et fait moins de 1200 lignes incluant une documentation détaillée.

Si vous êtes intéressé à voir Myna appliqué à un scénario plus complexe, jetez un coup d'œil au langage de programmation Chickadee. Celui-ci est entièrement implémenté en TypeScript et ne dépend que de la bibliothèque d'analyse Myna. Chickadee est un petit langage de programmation conçu spécifiquement pour aider les gens à apprendre les techniques de mise en œuvre des langues de programmation.

Si vous avez aimé cet article, faites-le moi savoir et envisagez de le partager avec vos amis et collègues.