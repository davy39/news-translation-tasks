---
title: Portée lexicale en JavaScript – Guide pour débutants
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-05-26T15:27:00.000Z'
originalURL: https://freecodecamp.org/news/lexical-scope-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/spacex--p-KCm6xB9I-unsplash-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Lexical Scoping
  slug: lexical-scoping
seo_title: Portée lexicale en JavaScript – Guide pour débutants
seo_desc: "In this article, we are going to understand what lexical scope is by going\
  \ through some helpful examples. \nWe will also have a brief discussion about how\
  \ JavaScript compiles and executes programs. \nLastly, we will have a look at how\
  \ you can use lexic..."
---

Dans cet article, nous allons comprendre ce qu'est la portée lexicale en examinant quelques exemples utiles. 

Nous aurons également une brève discussion sur la façon dont JavaScript compile et exécute les programmes. 

Enfin, nous verrons comment vous pouvez utiliser la portée lexicale pour expliquer les erreurs de variables non déclarées ou les erreurs de référence.

Sans plus attendre, commençons.

## Table des matières

* [Comment JavaScript exécute-t-il les programmes ?](#heading-comment-javascript-execute-les-programmes)
* [Comment JavaScript analyse/compile et exécute le code](#heading-comment-javascript-analysecompile-et-execute-le-code)
* [Comprendre l'erreur de syntaxe](#heading-erreur-de-syntaxe)
* [Comprendre le hissing des variables/fonctions](#heading-hissing-des-variablesfonctions)
* [Qu'est-ce que la portée lexicale](#heading-qu-est-ce-que-la-portee-lexicale) ?
* [Comprendre la portée lexicale](#heading-comprendre-la-portee-lexicale)
* [Résumé](#heading-resume)

## Comment JavaScript exécute-t-il les programmes ?

Avant de comprendre comment JavaScript exécute un code/programme, nous allons d'abord explorer les différentes étapes impliquées dans tout processus de compilation du point de vue de la théorie des compilateurs.

Pour tout langage, le compilateur effectue les opérations suivantes :

### Tokenisation/Lexing

Dans ce processus, l'ensemble du programme est divisé en mots-clés appelés tokens. Par exemple, considérons l'instruction suivante : `let temp = 10` – une fois la tokenisation appliquée, elle divise cette instruction en mots-clés comme suit : `let`, `temp`, `=`, `10`. 

Les termes lexing et tokenisation sont utilisés de manière interchangeable, mais il existe une différence subtile entre eux. Le lexing est un processus de tokenisation, mais il vérifie également s'il doit être considéré comme un token distinct. Nous pouvons considérer le **Lexing** comme une version intelligente de la tokenisation.

### Parsing

Il s'agit d'un processus de collecte de tous les tokens générés à l'étape précédente et de leur transformation en une structure arborescente imbriquée qui représente grammaticalement le code.

Cette structure arborescente est appelée un arbre de syntaxe abstraite (AST).

### Génération de code

Ce processus convertit l'AST en code lisible par la machine.

Voici donc une brève explication de la façon dont le compilateur fonctionne et génère un code lisible par la machine. 

Bien sûr, il existe d'autres étapes en plus de celles mentionnées ci-dessus. Mais expliquer les autres étapes/phases du compilateur est hors de portée pour cet article.

L'observation la plus importante que nous pouvons faire sur l'exécution de JS est que pour exécuter du code, il passe par deux phases :

1. Parsing
2. Exécution

Avant de comprendre la portée lexicale, il est important de comprendre d'abord comment JavaScript exécute un programme. Dans les sections suivantes, nous approfondirons le fonctionnement de ces deux phases.

## Comment JavaScript analyse/compile et exécute le code

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Untitled.png)
_Phase de parsing_

Commençons par parler de la phase de parsing. Dans cette phase, le moteur JavaScript parcourt l'ensemble du programme, attribue des variables à leurs portées respectives et vérifie également les erreurs. S'il trouve une erreur, l'exécution du programme est arrêtée.

Dans la phase suivante, l'exécution réelle du code a lieu.

Pour comprendre cela plus en détail, nous allons examiner les deux scénarios suivants :

* Erreur de syntaxe
* Hissage de variable

### Erreur de syntaxe

Pour vous montrer comment JS analyse d'abord le programme puis l'exécute, la meilleure et la plus simple façon est de démontrer le comportement d'une erreur de syntaxe.

Considérons le code suivant contenant des bugs :

```javascript
const token = "ABC";
console.log(token);

//Erreur de syntaxe :
const newToken = %((token);
```

Le programme ci-dessus générera une erreur de syntaxe à la dernière ligne. Voici à quoi ressemblera l'erreur :

```javascript
Uncaught SyntaxError: Unexpected token '%'

```

Si vous regardez l'erreur, les moteurs JavaScript n'ont pas exécuté l'instruction `console.log`. Au lieu de cela, il a parcouru l'ensemble du programme de la manière suivante :

* Ligne 1, a trouvé qu'il y avait une déclaration et une définition de variable. Il a donc stocké la référence de la variable `token` dans la portée actuelle, c'est-à-dire la portée globale.
* Ligne 2, le moteur JavaScript a découvert que la variable `token` était référencée. Il a d'abord fait référence à la portée actuelle pour vérifier si la variable `token` était présente ou non. Si elle est présente, alors elle est référencée à la déclaration de la variable `token`.
* Ligne 3, le moteur a découvert que la variable `newToken` était déclarée et définie. Il a vérifié si une variable avec le nom `newToken` était présente dans la portée actuelle ou non. Si oui, alors il lance une erreur de référence. Si non, alors il stocke la référence de cette variable dans la portée actuelle.
* À la même ligne, le moteur a également découvert qu'il essayait de faire référence à une variable `%((token)`. Mais il a trouvé qu'elle commençait par `%` et que les noms de variables ne peuvent pas commencer par des mots-clés réservés, donc il a lancé une erreur de syntaxe.

### Hissage de variable/fonction

Le hissing est un mécanisme via lequel toutes les variables présentes dans leurs portées respectives sont hissées, c'est-à-dire mises à disposition en haut. 

Maintenant, examinons l'exemple ci-dessous qui vous montrera que le hissing se produit pendant la phase de parsing et ensuite l'exécution se produit :

```javascript
doSomething();

function doSomething(){
	console.log("Comment ça va ?");
}
```

Dans le programme ci-dessus, le moteur parcourt le programme de la manière suivante :

* Ligne 1, le moteur JavaScript a rencontré une fonction appelée `doSomething`. Il a recherché pour voir si `doSomething` était disponible dans la portée actuelle. Si oui, alors il fait référence à la fonction, sinon il lance une erreur de référence.
* Il s'est avéré que pendant la phase de parsing, le moteur a trouvé la ligne `function doSomething` présente dans la portée actuelle. Par conséquent, il a ajouté la référence de cette variable dans la portée actuelle et l'a rendue disponible dans tout le programme.
* Enfin, la fonction `doSomething` a imprimé la chaîne `Comment ça va ?`.

Comme nous pouvons le voir à partir de l'explication ci-dessus, le code a d'abord été analysé afin de générer un code intermédiaire qui garantit que la variable/fonction (c'est-à-dire `doSomething`) référencée dans la portée actuelle est mise à disposition. 

Dans la phase suivante, JavaScript connaît la fonction et commence donc à l'exécuter.

D'après les exemples ci-dessus, nous pouvons conclure en toute sécurité que le moteur JavaScript fait les choses suivantes avant d'exécuter le code :

1. Analyse le code.
2. Génère le code intermédiaire qui donne une description des variables/fonctions disponibles.
3. En utilisant le code intermédiaire ci-dessus, il commence ensuite l'exécution du programme.

## Qu'est-ce que la portée lexicale ?

Le processus de détermination des portées des variables/fonctions pendant l'exécution est appelé portée lexicale. Le mot _lexical_ vient de la phase _lexicale/tokenisation_ des étapes du compilateur JS.

Pendant l'exécution, JavaScript fait ces deux choses : `parsing` et `exécution`. Comme vous l'avez appris dans la dernière section, pendant la phase de parsing, les portées des variables/fonctions sont définies. C'est pourquoi il était important de comprendre d'abord la phase de parsing de l'exécution du code, car elle pose les bases de la compréhension de la portée lexicale.

En termes profanes, la phase de parsing du moteur JavaScript est celle où la portée lexicale prend place.

Maintenant que nous en connaissons les bases, examinons quelques-unes des principales caractéristiques de la portée lexicale :

Tout d'abord, pendant la phase de parsing, une portée est attribuée/référencée à une variable où elle est déclarée. 

Par exemple, considérons un scénario où une variable est référencée dans la fonction interne et sa déclaration est présente dans la portée globale. Dans ce cas, la variable interne est attribuée avec la portée externe, c'est-à-dire la portée globale.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ezgif.com-gif-maker--1---1-.gif)
_Illustration de la portée attribuée_

Ensuite, lors de l'attribution de la portée à une variable, le moteur JavaScript vérifie ses portées parent pour la disponibilité de la variable. 

Si la variable est présente, alors cette portée parent est appliquée à la variable. Si une variable n'est pas trouvée dans aucune des portées parent, une erreur de référence est lancée.  
  
Jetez un coup d'œil à l'illustration ci-dessous qui démontre comment la portée d'une variable est recherchée.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ezgif.com-gif-maker--3---1-.gif)
_Le moteur JS trouve avec succès une variable en parcourant chaque portée_

Voici une illustration qui représente le moteur JS essayant de trouver une variable qui n'existe dans aucune portée :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/ezgif.com-gif-maker--6---1-.gif)
_Le moteur JS lance une erreur de référence_

## Comprendre la portée lexicale

Dans la section précédente, nous avons défini ce qu'est la portée lexicale. Nous avons également compris quelles caractéristiques elle possède. 

Dans cette section, nous allons comprendre la portée lexicale à l'aide d'un exemple. Comme on dit, il est toujours plus facile de comprendre des sujets difficiles en regardant des exemples de la vie réelle, du code quotidien. Commençons.

L'exemple que nous allons utiliser implique la coloration des zones de notre code qui ont des portées similaires. Cela peut sembler confus, mais laissez-moi vous démontrer cela avec une simple illustration.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Global-and-Functional-Scope--1---1-.gif)
_Comprendre la portée lexicale avec un exemple de coloration_

Faisons un pas en arrière et comprenons ce qui se passe dans cette illustration.

Nous avons les éléments suivants dans notre programme :

* `empData` : Tableau d'objets.
* `allPositions` : Tableau de chaînes qui contient toutes les positions des employés.
* Enfin, nous avons une instruction console qui imprime les variables `allPositions`.

Maintenant, examinons ce qui se passe dans la phase de parsing de ce programme :

* Le moteur commence avec la première ligne et rencontre une déclaration de variable `empData`.
* Le moteur vérifie ensuite si `empData` est disponible dans la portée actuelle ou non. Comme aucune variable similaire n'est trouvée, il vérifie l'existence de cette variable dans sa portée parent.
* Le moteur arrêtera sa recherche ici, car aucune portée n'est disponible et la portée actuelle est la portée globale.
* Ensuite, le moteur attribue une valeur `undefined` à `empData` pendant la phase de parsing afin que, une fois qu'une portée imbriquée essaie de référencer cette variable, elle puisse être utilisée.
* Le côté droit de cet opérateur d'affectation est évalué pendant la phase d'exécution du programme.
* De manière similaire, le moteur fait de même pour la variable `allPositions` et lui attribue une valeur `undefined`.
* Mais du côté droit, nous référençons également la variable `empData`. À ce stade, le moteur vérifie si cette variable est disponible dans la portée actuelle. Comme elle est disponible, elle fait référence à la même (c'est-à-dire présente dans la portée globale).
* Le moteur est toujours du côté droit, car il a découvert qu'il y a une fonction fléchée à l'intérieur de la fonction map. Comme le moteur a rencontré la définition de la fonction, il crée une nouvelle portée. Dans le gif, ceci est le numéro 2.
* Comme il s'agit d'une nouvelle portée, nous allons la colorier en noir.
* Cette fonction fléchée a un argument `data` et retourne `data.position`. Dans la phase de parsing, le moteur hisse toutes les variables nécessaires en référençant les variables présentes dans la portée actuelle ainsi que dans sa portée parent. 
* À l'intérieur de cette fonction, la variable `data` est référencée, donc le moteur vérifie si la portée actuelle possède cette variable. Comme la variable est présente dans la portée actuelle, elle fait référence à la même.
* Une fois que le moteur rencontre l'accolade `}`, il sort de la portée fonctionnelle.
* Enfin, à la fin du programme, nous avons une instruction console qui affiche les variables `allPositions`. Comme elle référence la variable `allPositions`, elle recherche dans la portée actuelle (c'est-à-dire la portée globale). Comme elle est trouvée, elle fait référence à la même dans l'instruction `console`.

## Résumé

Dans cet article, nous avons appris ce que signifie la portée lexicale et comment elle fonctionne en examinant un simple exemple de coloration.

Merci d'avoir lu !

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).