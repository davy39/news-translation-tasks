---
title: Apprenez les bases de Swift en moins de dix minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-25T16:21:21.000Z'
originalURL: https://freecodecamp.org/news/learn-swift-basics-in-5-minutes-30a530e23231
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S4__g3knEbuuE6qHyWIbNQ.png
tags:
- name: coding
  slug: coding
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Apprenez les bases de Swift en moins de dix minutes
seo_desc: "By Saul Costa\nSwift is a relatively new programming language designed\
  \ by Apple Inc which was initially made available to Apple developers in 2014. \n\
  It was primarily intended as a replacement for the aging Objective-C language that\
  \ was the foundation ..."
---

Par Saul Costa

Swift est un langage de programmation relativement nouveau conçu par Apple Inc, qui a été initialement mis à disposition des développeurs Apple en 2014.

Il était principalement destiné à remplacer le langage Objective-C vieillissant, qui était la base du développement logiciel OS X et iOS à l'époque. Il a été rendu open source en décembre 2015.

Bien qu'il reste principalement utilisé par les développeurs ciblant les plateformes Apple macOS et iOS, Swift est également entièrement pris en charge sur Linux, et il existe des ports non officiels en développement pour Windows également.

Contrairement à de nombreux langages orientés objet, qui sont basés sur des langages procéduraux plus anciens — par exemple, C++ et Objective-C sont basés sur C — Swift a été conçu dès le départ comme un nouveau langage orienté objet moderne qui rend la programmation plus rapide et plus facile, et aide les développeurs à produire du code expressif moins sujet aux erreurs que de nombreux langages.

Bien que non basé sur un langage plus ancien, Swift, selon les mots de son architecte en chef, Chris Lattner, « s'est inspiré en puisant des idées de Ruby, Python, C#, CLU, et bien trop nombreux autres à lister ».

Dans ce cours accéléré, nous couvrirons les fondamentaux de l'utilisation du langage de programmation Swift. Vous apprendrez :

* La syntaxe de base de Swift
* La structure du programme Swift
* Les variables et les constantes
* L'inférence de type
* Les conventions de nommage des variables et des constantes
* L'impression et l'interpolation de chaînes

Commençons !

> Ce cours accéléré est adapté du cours complet Beginning Swift de Next Tech, qui inclut un environnement en bac à sable dans le navigateur avec Swift préinstallé. Il comprend également de nombreuses activités à compléter. Vous pouvez le consulter gratuitement [ici](https://c.next.tech/2FkiuWI) !

### Syntaxe de Swift

Dans cette première section, nous examinerons la syntaxe de base du langage Swift.

Comme de nombreux langages de programmation modernes, Swift tire sa syntaxe la plus basique du langage de programmation C. Si vous avez une expérience de programmation dans d'autres langages inspirés de C, de nombreux aspects de Swift vous sembleront familiers, par exemple :

* Les programmes sont composés d'instructions, exécutées séquentiellement.
* Plus d'une instruction est autorisée par ligne d'éditeur lorsqu'elles sont séparées par un point-virgule (`;`).
* Les unités de travail dans Swift sont modularisées à l'aide de fonctions et organisées en types.
* Les fonctions acceptent un ou plusieurs paramètres et retournent des valeurs.
* Les commentaires sur une seule ligne et sur plusieurs lignes suivent la même syntaxe que dans C++ et Java.
* Les noms et l'utilisation des types de données Swift sont similaires à ceux de Java, C# et C++.
* Swift a le concept de variables nommées, qui sont mutables, et de constantes nommées, qui sont immuables.
* Swift a à la fois des sémantiques de struct et de classe, comme C++ et C#.

Cependant, Swift présente certaines améliorations et différences par rapport aux langages inspirés de C auxquels vous devrez peut-être vous habituer, telles que :

* Les points-virgules ne sont pas requis à la fin des instructions — sauf lorsqu'ils sont utilisés pour séparer plusieurs instructions tapées sur la même ligne dans un fichier source.
* Swift n'a pas de méthode `main()` pour servir de point de départ du programme lorsque le système d'exploitation charge l'application. Les programmes Swift commencent à la première ligne de code du fichier source du programme — comme c'est le cas dans la plupart des langages **interprétés**.
* Les fonctions dans Swift placent le type de retour de la fonction du côté droit de la déclaration de la fonction, plutôt que du côté gauche.
* La syntaxe de déclaration des paramètres de fonction est inspirée de Objective-C, qui est assez différente et souvent au début déroutante pour les développeurs Java, C# et C++.
* La différence entre une struct et une classe dans Swift est similaire à ce que nous avons dans C# (type valeur versus type référence), mais pas la même que dans C++ (les deux sont les mêmes, sauf que les membres de la struct sont publics par défaut).

### Structure du programme Swift — `Bonjour, le monde !`

Pour illustrer la structure de base d'un programme Swift, créons un simple programme Swift pour afficher la chaîne `Bonjour, le monde.` sur la console :

```
[Out:]Bonjour, le monde
```

> Si vous utilisez le bac à sable de Next Tech, vous pouvez suivre les extraits de code de ce cours accéléré en tapant simplement dans l'éditeur. Sinon, vous pouvez suivre avec votre propre IDE — assurez-vous simplement que Swift est installé !

Félicitations ! En deux lignes de code, vous venez d'écrire votre premier programme Swift entièrement fonctionnel.

Maintenant, passons à l'apprentissage et à l'utilisation du langage Swift — et décomposons chaque partie de votre programme `Bonjour le monde` !

### Variables Swift

Pratiquement tous les langages de programmation incluent la capacité pour les programmeurs de stocker des valeurs en mémoire en utilisant un nom associé choisi par le programmeur. Les **variables** permettent aux programmes d'opérer sur des valeurs de données qui changent pendant l'exécution du programme.

Une déclaration de variable Swift utilise la syntaxe de base suivante :
`var <nom de la variable> : <type> = <valeur>`

Étant donné cette syntaxe, une déclaration légale pour une variable appelée `pi` serait :

Cette déclaration signifie : « créer une variable nommée `pi`, qui stocke un type de données `Double`, et lui assigner une valeur initiale de `3.14159` ».

### Constantes Swift

Vous pouvez vouloir stocker une valeur nommée dans votre programme qui ne changera pas pendant la durée de vie du programme. Comment pouvons-nous nous assurer que, une fois définie, cette valeur nommée ne pourra jamais être accidentellement modifiée par notre code ? En déclarant une **constante** !

Dans notre programme `Bonjour, le monde` précédent, nous avons déclaré `message` en utilisant `let` au lieu de `var` — donc, `message` est une constante.

Puisque `message` a été déclaré comme une constante, si nous ajoutions la ligne de code suivante à la fin de notre programme, nous recevrions une erreur de compilation, car changer une constante `let` est illégal :

```
[Out:]erreur : impossible d'assigner une valeur : 'message' est une constante 'let'
```

Généralement, chaque fois que vous créez une valeur nommée qui ne sera jamais modifiée pendant l'exécution de votre programme, vous devez utiliser le mot-clé `let` pour créer une constante. Le compilateur Swift impose cette recommandation en créant un avertissement de compilation chaque fois qu'un `var` est créé et n'est pas modifié par la suite.

À part la restriction sur la mutation de la valeur d'une constante une fois déclarée, les variables et les constantes Swift sont utilisées de manière pratiquement identique.

### Inférence de type

Dans notre exemple Bonjour le monde, nous avons créé la constante `message` sans spécifier son type de données. Nous avons tiré parti d'une fonctionnalité du compilateur Swift appelée **inférence de type**.

Lorsque vous attribuez la valeur d'une variable ou d'une constante au moment de sa création, le compilateur Swift analysera le côté droit de l'attribution, **déduira** le type de données et attribuera ce type de données à la variable ou à la constante que vous créez. Par exemple, dans la déclaration suivante, le compilateur créera la variable name comme un type de données String :

En tant que langage **typé de manière sûre**, une fois qu'un type de données est déduit par le compilateur, il reste fixe pour la durée de vie de la variable ou de la constante. Tenter d'attribuer une valeur non chaîne à la variable name déclarée ci-dessus entraînerait une erreur de compilation :

```
[Out:]erreur : « impossible d'attribuer une valeur de type 'Double' à une valeur de type 'String' »
```

Bien que Swift soit un langage typé de manière sûre, où les types de variables sont explicites et ne changent pas, il est possible de créer du code Swift qui se comporte comme un langage de type dynamique en utilisant le type de données `Any` de Swift. Par exemple, le code suivant est légal en Swift :

Bien que cela soit légal, ce n'est pas une bonne pratique de programmation Swift. Le type `Any` est principalement fourni pour permettre le pont entre le code Objective-C et Swift. Pour garder votre code aussi sûr et exempt d'erreurs que possible, vous devez utiliser des types explicites chaque fois que possible.

### Conventions de nommage des variables

Les variables et les constantes Swift ont les mêmes règles de nommage que la plupart des langages de programmation inspirés de C :

* Ne doivent pas commencer par un chiffre
* Après le premier caractère, les chiffres sont autorisés
* Peut commencer et inclure un caractère de soulignement
* Les noms de symboles sont sensibles à la casse
* Les mots-clés réservés du langage peuvent être utilisés comme noms de variables s'ils sont enfermés dans des backticks. Par exemple :

Lors de la création de noms de variables et de constantes en Swift, la convention de nommage généralement acceptée est d'utiliser une convention de nommage **camelCase**, commençant par une lettre minuscule. Suivre les conventions de nommage généralement acceptées rend le code plus facile à lire et à comprendre pour les autres.

Par exemple, ce qui suit serait une déclaration de variable conventionnelle :

Cependant, ce qui suit ne serait pas conventionnel et serait considéré comme incorrect par de nombreux autres développeurs Swift :

Contrairement à de nombreux autres langages de programmation, Swift n'est pas restreint à l'alphabet occidental pour ses caractères de noms de variables. Vous pouvez utiliser n'importe quel caractère Unicode comme partie de vos déclarations de variables. Les déclarations de variables suivantes sont légales en Swift :

Notez que simplement parce que vous pouvez utiliser n'importe quel caractère Unicode dans un nom de variable, et pouvez utiliser des mots réservés comme variables lorsqu'ils sont enfermés dans des backticks, cela ne signifie pas que vous devriez le faire. Pensez toujours aux autres développeurs qui pourraient avoir besoin de lire et de maintenir votre code à l'avenir. La priorité pour les noms de variables est qu'ils doivent rendre le code plus facile à lire, à comprendre et à maintenir.

### Impression et interpolation de chaînes

En Swift, vous pouvez imprimer une variable ou une constante sur votre console en utilisant la fonction `print()`. Créons une variable et une constante et imprimons-les.

Exécutez cet extrait dans votre éditeur de code pour créer une constante nommée `name`, et une variable nommée `address` :

```
[Out:]John Doe vit au 201 Main Street
```

`name` et `address` stockent tous deux du texte de chaîne. En enveloppant le nom de la variable ou de la constante dans une paire de parenthèses, précédé d'un backslash (`\`), nous sommes en mesure d'imprimer leurs valeurs stockées dans une instruction `print` — cela s'appelle **l'interpolation de chaînes**.

J'espère que vous avez apprécié ce cours accéléré sur les bases de Swift ! Nous avons appris la syntaxe de base et la structure du programme, comment déclarer et utiliser les variables et les constantes Swift, l'inférence de type, l'impression et l'interpolation de chaînes.

Si vous êtes intéressé à en apprendre davantage sur Swift, nous avons un cours complet [Beginning Swift](https://c.next.tech/2FkiuWI) chez Next Tech que vous pouvez commencer gratuitement ! Dans ce cours, nous couvrons :

* D'autres concepts de programmation de base tels que : les optionnels, les tuples, les énumérations, les conditionnelles et les boucles, les méthodes, les structs et les classes.
* La création de scripts et d'applications en ligne de commande en Swift
* L'utilisation de Swift en dehors des cycles de développement iOS et macOS

Bon apprentissage !