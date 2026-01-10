---
title: 'Comment JavaScript fonctionne : Sous le capot du moteur V8'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-26T20:08:18.000Z'
originalURL: https://freecodecamp.org/news/javascript-under-the-hood-v8
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9904740569d1a4ca1d5f.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: 'Comment JavaScript fonctionne : Sous le capot du moteur V8'
seo_desc: 'By Ilya Lyamkin

  Today we’ll look under the hood of JavaScript''s V8 engine and figure out how exactly
  JavaScript is executed.

  In a previous article we learned how the browser is structured and got a high-level
  overview of Chromium. Let''s recap a bit s...'
---

Par Ilya Lyamkin

Aujourd'hui, nous allons examiner le fonctionnement interne du moteur V8 de JavaScript et comprendre comment JavaScript est exactement exécuté.

[Dans un article précédent](https://lyamkin.com/blog/what-are-web-standards-and-how-does-web-browser-work/), nous avons appris comment le navigateur est structuré et obtenu un [aperçu général de Chromium](https://www.chromium.org/developers/how-tos/getting-around-the-chrome-source-code). Faisons un bref rappel pour être prêts à plonger ici.

## Contexte

Les [normes Web](https://www.w3.org/TR/) sont un ensemble de règles que le navigateur implémente. Elles définissent et décrivent les aspects du [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web).

Le [W3C](https://www.w3.org/) est une communauté internationale qui développe des normes ouvertes pour le Web. Ils s'assurent que tout le monde suit les mêmes directives et n'a pas à supporter des dizaines d'environnements complètement différents.

Un navigateur moderne est un logiciel assez complexe avec une base de code de [dizaines de millions de lignes de code](https://www.openhub.net/p/chrome/analyses/latest/languages_summary). Il est donc divisé en de nombreux modules responsables de différentes logiques.

Et deux des parties les plus importantes d'un navigateur sont le moteur JavaScript et un moteur de rendu.

[Blink](https://docs.google.com/presentation/d/1boPxbgNrTU0ddsc144rcXayGA_WF53k96imRH8Mp34Y/edit#slide=id.g60f92a5151_40_0) est un moteur de rendu responsable de l'ensemble du pipeline de rendu, y compris les arbres DOM, les styles, les événements et l'intégration de V8. Il analyse l'arbre DOM, résout les styles et détermine la géométrie visuelle de tous les éléments.

Tout en surveillant en continu les changements dynamiques via les frames d'animation, Blink peint le contenu sur votre écran. Le moteur JS est une grande partie du navigateur – mais nous n'avons pas encore abordé ces détails.

### JavaScript Engine 101

Le moteur JavaScript exécute et compile JavaScript en code machine natif. Chaque navigateur majeur a développé son propre moteur JS : Google Chrome utilise V8, Safari utilise JavaScriptCore, et Firefox utilise SpiderMonkey.

Nous travaillerons particulièrement avec V8 en raison de son utilisation dans Node.js et Electron, mais les autres moteurs sont construits de la même manière.

Chaque étape inclura un lien vers le code responsable de celle-ci, afin que vous puissiez vous familiariser avec la base de code et poursuivre la recherche au-delà de cet article.

Nous travaillerons avec [un miroir de V8 sur GitHub](https://github.com/v8/v8) car il fournit une interface utilisateur pratique et bien connue pour naviguer dans la base de code.

## Préparation du code source

La première chose que V8 doit faire est de télécharger le code source. Cela peut être fait via un réseau, un cache ou des service workers.

Une fois le code reçu, nous devons le modifier de manière à ce que le compilateur puisse le comprendre. Ce processus est appelé analyse et se compose de deux parties : le scanner et l'analyseur lui-même.

[Le scanner](https://github.com/v8/v8/blob/master/src/parsing/scanner.h) prend le fichier JS et le convertit en une liste de tokens connus. Il y a une liste de tous les tokens JS dans [le fichier keywords.txt](https://github.com/v8/v8/blob/master/src/parsing/keywords.txt).

L'[analyseur](https://github.com/v8/v8/blob/master/src/parsing/parser.h) le prend et crée un [Abstract Syntax Tree (AST)](https://github.com/v8/v8/tree/master/src/ast) : une représentation arborescente du code source. Chaque nœud de l'arbre désigne une construction présente dans le code.

Regardons un exemple simple :

```javascript
function foo() {
  let bar = 1;
  return bar;
}
```

Ce code produira la structure arborescente suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ast-tree.png)
_Exemple d'arbre AST_

Vous pouvez exécuter ce code en effectuant un parcours préfixe (racine, gauche, droite) :

1. Définir la fonction `foo`.
2. Déclarer la variable `bar`.
3. Assigner `1` à `bar`.
4. Retourner `bar` hors de la fonction.

Vous verrez également `VariableProxy` — un élément qui connecte la variable abstraite à un emplacement en mémoire. Le processus de résolution de `VariableProxy` est appelé **Analyse de Portée**.

Dans notre exemple, le résultat du processus serait que tous les `VariableProxy` pointent vers la même variable `bar`.

## Le paradigme Just-in-Time (JIT)

Généralement, pour que votre code s'exécute, le langage de programmation doit être transformé en code machine. Il existe plusieurs approches pour savoir comment et quand cette transformation peut se produire.

La manière la plus courante de transformer le code est d'effectuer une compilation à l'avance. Cela fonctionne exactement comme cela sonne : le code est transformé en code machine avant l'exécution de votre programme lors de l'étape de compilation.

Cette approche est utilisée par de nombreux langages de programmation tels que C++, Java, et autres.

De l'autre côté, nous avons l'interprétation : chaque ligne de code sera exécutée au moment de l'exécution. Cette approche est généralement adoptée par les langages à typage dynamique comme JavaScript et Python car il est impossible de connaître le type exact avant l'exécution.

Parce que la compilation à l'avance peut évaluer tout le code ensemble, elle peut fournir une meilleure optimisation et finalement produire un code plus performant. L'interprétation, de l'autre côté, est plus simple à implémenter, mais elle est généralement plus lente que l'option compilée.

Pour transformer le code plus rapidement et plus efficacement pour les langages dynamiques, une nouvelle approche a été créée appelée Just-in-Time (JIT). Elle combine le meilleur de l'interprétation et de la compilation.

Tout en utilisant l'interprétation comme méthode de base, V8 peut détecter les fonctions qui sont utilisées plus fréquemment que d'autres et les compiler en utilisant les informations de type des exécutions précédentes.

Cependant, il y a une chance que le type puisse changer. Nous devons désoptimiser le code compilé et revenir à l'interprétation à la place (après cela, nous pouvons recompiler la fonction après avoir obtenu de nouvelles informations de type).

Explorons chaque partie de la compilation JIT plus en détail.

### Interpréteur

V8 utilise un interpréteur appelé [Ignition](https://github.com/v8/v8/blob/master/src/interpreter/interpreter.h). Initialement, il prend un arbre de syntaxe abstraite et génère du bytecode.

Les instructions de bytecode ont également des métadonnées, telles que les positions des lignes sources pour le débogage futur. Généralement, les instructions de bytecode correspondent aux abstractions JS.

Maintenant, prenons notre exemple et générons du bytecode pour celui-ci manuellement :

```bytecode
LdaSmi #1 // écrire 1 dans l'accumulateur
Star r0   // lire dans r0 (bar) depuis l'accumulateur 
Ldar r0   // écrire depuis r0 (bar) vers l'accumulateur
Return    // retourne l'accumulateur
```

Ignition a quelque chose appelé un accumulateur — un endroit où vous pouvez stocker/lire des valeurs.

L'accumulateur évite le besoin de pousser et de retirer le sommet de la pile. C'est aussi un argument implicite pour de nombreux bytecodes et contient généralement le résultat de l'opération. Return retourne implicitement l'accumulateur.

Vous pouvez consulter tous les bytecodes disponibles [dans le code source correspondant](https://github.com/v8/v8/blob/master/src/interpreter/bytecodes.h). Si vous êtes intéressé par la façon dont d'autres concepts JS (comme les boucles et async/await) sont présentés en bytecode, je trouve utile de lire ces [attentes de test](https://github.com/v8/v8/tree/master/test/cctest/interpreter/bytecode_expectations).

### Exécution

Après la génération, Ignition interprétera les instructions en utilisant une table de gestionnaires indexée par le bytecode. Pour chaque bytecode, Ignition peut rechercher les fonctions de gestionnaire correspondantes et les exécuter avec les arguments fournis.

Comme nous l'avons mentionné précédemment, l'étape d'exécution fournit également le feedback de type sur le code. Comprenons comment il est collecté et géré.

Tout d'abord, nous devons discuter de la manière dont les objets JavaScript peuvent être représentés en mémoire. Dans une approche naïve, nous pouvons créer un dictionnaire pour chaque objet et le lier à la mémoire.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/naive-object.png)
_La première approche pour conserver l'objet_

Cependant, nous avons généralement beaucoup d'objets avec la même structure, donc il ne serait pas efficace de stocker de nombreux dictionnaires dupliqués.

Pour résoudre ce problème, V8 sépare la structure de l'objet des valeurs elles-mêmes avec des **Formes d'Objets** (ou Maps en interne) et un vecteur de valeurs en mémoire.

Par exemple, nous créons un littéral d'objet :

```javascript
let c = { x: 3 }
let d = { x: 5 }
c.y = 4
```

Dans la première ligne, cela produira une forme `Map[c]` qui a la propriété `x` avec un décalage de 0.

Dans la deuxième ligne, V8 réutilisera la même forme pour une nouvelle variable.

Après la troisième ligne, il créera une nouvelle forme `Map[c1]` pour la propriété `y` avec un décalage de 1 et créera un lien vers la forme précédente `Map[c]`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/object-shapes-1.png)
_Exemple de formes d'objets_

Dans l'exemple ci-dessus, vous pouvez voir que chaque objet peut avoir un lien vers la forme de l'objet où, pour chaque nom de propriété, V8 peut trouver un décalage pour la valeur en mémoire.

Les formes d'objets sont essentiellement des listes liées. Donc, si vous écrivez `c.x`, V8 ira à la tête de la liste, trouvera `y` là, passera à la forme connectée, et finalement il obtiendra `x` et lira le décalage de celui-ci. Ensuite, il ira au vecteur de mémoire et retournera le premier élément de celui-ci.

Comme vous pouvez l'imaginer, dans une grande application web, vous verrez un énorme nombre de formes connectées. En même temps, il faut un temps linéaire pour rechercher dans la liste liée, ce qui rend les recherches de propriétés une opération vraiment coûteuse.

Pour résoudre ce problème dans V8, vous pouvez utiliser le [**Inline Cache (IC)**](https://github.com/v8/v8/tree/master/src/ic). Il mémorise les informations sur l'endroit où trouver les propriétés des objets pour réduire le nombre de recherches.

Vous pouvez penser à cela comme un site d'écoute dans votre code : il suit tous les événements _CALL_, _STORE_, et _LOAD_ dans une fonction et enregistre toutes les formes qui passent.

La structure de données pour garder l'IC est appelée [**Feedback Vector**](https://github.com/v8/v8/blob/master/src/objects/feedback-vector.h). C'est simplement un tableau pour garder tous les IC pour la fonction.

```javascript
function load(a) {
  return a.key;
}
```

Pour la fonction ci-dessus, le vecteur de feedback ressemblera à ceci :

```javascript
[{ slot: 0, icType: LOAD, value: UNINIT }]
```

C'est une fonction simple avec un seul IC qui a un type LOAD et une valeur `UNINIT`. Cela signifie qu'il n'est pas initialisé, et nous ne savons pas ce qui va se passer ensuite.

Appelons cette fonction avec différents arguments et voyons comment l'Inline Cache va changer.

```javascript
let first = { key: 'first' } // forme A
let fast = { key: 'fast' }   // la même forme A
let slow = { foo: 'slow' }   // nouvelle forme B

load(first)
load(fast)
load(slow)
```

Après le premier appel de la fonction `load`, notre cache inline obtiendra une valeur mise à jour :

```javascript
[{ slot: 0, icType: LOAD, value: MONO(A) }]
```

Cette valeur devient maintenant monomorphique, ce qui signifie que ce cache ne peut résoudre que la forme A.

Après le deuxième appel, V8 vérifiera la valeur de l'IC et verra qu'elle est monomorphique et a la même forme que la variable `fast`. Il retournera donc rapidement le décalage et le résoudra.

La troisième fois, la forme est différente de celle stockée. V8 la résoudra donc manuellement et mettra à jour la valeur à un état polymorphe avec un tableau de deux formes possibles.

```javascript
[{ slot: 0, icType: LOAD, value: POLY[A,B] }]
```

Maintenant, chaque fois que nous appelons cette fonction, V8 doit vérifier non seulement une forme mais itérer sur plusieurs possibilités.

Pour un code plus rapide, vous _pouvez_ initialiser les objets avec le même type et ne pas trop changer leur structure.

**Note : Vous pouvez garder cela à l'esprit, mais ne le faites pas si cela conduit à une duplication de code ou à un code moins expressif.**

Les caches inline suivent également la fréquence à laquelle ils sont appelés pour décider s'il s'agit d'un bon candidat pour l'optimisation du compilateur — Turbofan.

### Compilateur

Ignition ne nous mène que jusqu'à un certain point. Si une fonction devient suffisamment « chaude », elle sera optimisée dans le compilateur, [Turbofan](https://github.com/v8/v8/tree/master/src/compiler), pour la rendre plus rapide.

Turbofan prend le bytecode d'Ignition et le feedback de type (le Feedback Vector) pour la fonction, applique un ensemble de réductions basées sur celui-ci, et produit du code machine.

Comme nous l'avons vu précédemment, le feedback de type ne garantit pas qu'il ne changera pas à l'avenir.

Par exemple, Turbofan optimise le code en supposant que certaines additions ajoutent toujours des entiers.

Mais que se passerait-il s'il recevait une chaîne ? Ce processus est appelé **désoptimisation**. Nous jetons le code optimisé, revenons au code interprété, reprenons l'exécution et mettons à jour le feedback de type.

## Résumé

Dans cet article, nous avons discuté de l'implémentation du moteur JS et des étapes exactes de l'exécution de JavaScript.

Pour résumer, examinons le pipeline de compilation de haut en bas.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/v8-overview-2.png)
_Aperçu de V8_

Nous allons le passer en revue étape par étape :

1. Tout commence par l'obtention du code JavaScript depuis le réseau.
2. V8 analyse le code source et le transforme en un Abstract Syntax Tree (AST).
3. Sur la base de cet AST, l'interpréteur Ignition peut commencer à faire son travail et produire du bytecode.
4. À ce stade, le moteur commence à exécuter le code et à collecter le feedback de type.
5. Pour le rendre plus rapide, le bytecode peut être envoyé au compilateur d'optimisation avec les données de feedback. Le compilateur d'optimisation fait certaines hypothèses basées sur celles-ci et produit ensuite un code machine hautement optimisé.
6. Si, à un moment donné, l'une des hypothèses s'avère incorrecte, le compilateur d'optimisation désoptimise et revient à l'interpréteur.

C'est tout ! Si vous avez des questions sur une étape spécifique ou souhaitez connaître plus de détails à ce sujet, vous pouvez plonger dans le code source ou me contacter sur [Twitter](https://twitter.com/ilyamkin).

### Lectures complémentaires

* Vidéo ["Life of a script"](https://www.youtube.com/watch?v=voDhHPNMEzg) de Google
* [Un cours accéléré sur les compilateurs JIT](https://hacks.mozilla.org/2017/02/a-crash-course-in-just-in-time-jit-compilers/) de Mozilla
* Explication des [Inline Caches dans V8](https://www.youtube.com/watch?v=u7zRSm8jzvA)
* Plongée dans les [Formes d'Objets](https://mathiasbynens.be/notes/shapes-ics)