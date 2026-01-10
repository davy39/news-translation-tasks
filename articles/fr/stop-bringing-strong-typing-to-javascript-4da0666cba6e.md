---
title: Introduire la sécurité de type dans votre projet JavaScript ? Réfléchissez
  à nouveau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-02T12:39:31.000Z'
originalURL: https://freecodecamp.org/news/stop-bringing-strong-typing-to-javascript-4da0666cba6e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0o35DC9HRHPhjwYMHwbz_g.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Introduire la sécurité de type dans votre projet JavaScript ? Réfléchissez
  à nouveau
seo_desc: 'By James Wright

  Update — 1st February 2017

  I’ve heard various counter-arguments regarding type safety in JavaScript since I
  first published this article, and while I still believe a lot of projects do not
  require the use of a typed JavaScript superse...'
---

Par James Wright

### Mise à jour — 1er février 2017

J'ai entendu divers contre-arguments concernant la sécurité de type en JavaScript depuis que j'ai publié cet article pour la première fois, et bien que je pense toujours que beaucoup de projets n'ont pas besoin d'utiliser un sur-ensemble typé de JavaScript, j'admets que j'ai été trop précipité en publiant cet article. Certains cas d'utilisation appropriés ont ensuite attiré mon attention :

* [Glimmer](https://github.com/tildeio/glimmer), le moteur de rendu de bas niveau derrière Ember, est écrit en TypeScript pour promouvoir les [sites d'appel monomorphes](http://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html), aidant à la performance lors de l'exécution par V8 et potentiellement d'autres moteurs JavaScript
* [Visual Studio Code](https://github.com/Microsoft/vscode) bénéficie de TypeScript en raison de la taille énorme du projet ; étant donné qu'il est distribué comme une application de bureau, avoir une seule base de code plutôt que de réconcilier des packages individuels au moment de la construction est, à mon avis, une option sensée
* [Sect](https://github.com/jamesseanwright/sect) (admettons qu'il s'agit d'un projet à moi, donc il y a un potentiel biais ici !) est écrit en TypeScript afin que les consommateurs puissent écrire de grands jeux modulaires pour le web tout en réduisant de manière fiable les erreurs d'exécution résultant de fautes de frappe et d'autres problèmes qui surviennent en raison de la nature dynamique de JavaScript

J'ai également réalisé que l'écriture de petites bibliothèques en TypeScript et leur publication avec les définitions de type générées au moment de la construction permettent simultanément leur intégration transparente avec des projets JavaScript typés et traditionnels, offrant ainsi aux développeurs un choix technologique plus large.

Néanmoins, pour la postérité, voici l'article original dans son intégralité.

Aujourd'hui, j'ai rencontré un article concernant le lancement de [JS++](http://sdtimes.com/onux-seeks-fix-javascripts-lack-type-safety/), qui prétend "corriger le manque de sécurité de type de JavaScript". Ironiquement, nous avons déjà [TypeScript](https://www.typescriptlang.org/), [ST-JS](http://st-js.github.io/), et [Scala.js](https://www.scala-js.org/), qui aident les développeurs à atteindre finalement le même objectif.

Avant de me lancer dans cette tirade, permettez-moi de souligner trois points importants :

* J'ai précédemment écrit [un tutoriel](http://www.codeproject.com/Articles/871622/Writing-a-chat-server-using-Node-js-TypeScript-and) sur l'établissement d'un projet TypeScript simple. Je vois l'hypocrisie, mais mes opinions ont changé depuis que je l'ai publié il y a plus d'un an
* Le typage fort et le typage statique sont des paradigmes vitaux. Le premier fournit de la transparence sur les entités représentées dans le code de quelqu'un, leurs relations, et la fonctionnalité qu'elles peuvent être censées fournir, tandis que le second est un filet de sécurité important, au moment de la compilation, dans les systèmes complexes. Je viens d'un arrière-plan C#, donc j'ai une expérience directe de cela
* J'aime aussi JavaScript, malgré ses défauts inhérents, dont beaucoup ont été abordés avec ECMAScript 6 et 7

Alors, pourquoi suis-je généralement contre le typage statique en JavaScript ?

Principalement, ce qui rend JavaScript si puissant est sa nature faiblement typée ; il est trivial d'implémenter des branches de logique via la coercition de type, et il est si facile de créer des instances d'objets d'un type arbitraire. De plus, l'absence de compilation (sauf si l'on utilise un transpileur ou un outil de construction tel que Babel, par exemple) rend le développement incroyablement rapide, tant que le code ne résulte pas en des comportements bizarres. À mon avis, c'est ce qui le rend si puissant pour le développement frontend et backend **simple** (par exemple, IoT).

Je pense personnellement que si l'on développe un système si complexe qu'il nécessite une sécurité de type, alors on devrait utiliser un langage qui le supporte au cœur ; écrire un système de guidage, qui implique des opérations mathématiques complexes, en JavaScript est insensé.

Ma principale préoccupation avec ces outils et sur-ensembles JavaScript est qu'ils compilent vers, eh bien, JavaScript ; ces programmes s'exécutent par conséquent dans un contexte dynamique, ainsi les mêmes effets secondaires pourraient encore se produire. TypeScript, par exemple, peut être typé statiquement (c'est-à-dire que les informations de type sont collectées et analysées au moment de la compilation), mais il faut avoir une confiance totale que le code résultant s'exécutera toujours comme prévu. Oui, bien sûr, même les langages typés statiquement sont généralement compilés vers un langage de plus bas niveau, qui est ensuite typiquement interprété, mais ces langages cibles ont sûrement été conçus avec le typage comme un citoyen de première classe ; par exemple, le compilateur JIT de Microsoft pour .NET implémente toujours [la vérification de type à l'exécution de son langage intermédiaire](https://msdn.microsoft.com/en-us/library/k5532s8a(v=vs.110).aspx) avant de compiler vers du code natif.

De plus, lors de la réalisation de développement frontend, je suis toujours d'avis que JavaScript devrait être utilisé pour _compléter_ les solutions HTML et CSS, par exemple, ajouter des classes aux éléments, faire des appels HTTP aux services backend, etc. Bien que le web ait mûri en termes de frameworks pour la création d'applications plus grandes basées sur l'UI (FYI, j'ai écrit de plus grandes applications avec React.js et vanilla JS aussi ; j'aime les deux), je préfère garder mon JS aussi léger que possible. Je comprends que ce n'est pas toujours une possibilité en réalité, mais si les systèmes backend servent de source de vérité pour la logique métier fondamentale, alors le code frontend devient plus léger et moins redondant ; à cet égard, quels avantages un système de typage apportera-t-il ?

Suivant mon point sur la taille des logiciels frontend, mon travail actuel consiste à écrire des applications web concentrées pour chaque préoccupation du système global ; au lieu d'une grande application monopage pour notre magasin, qui contient une vue de liste de produits, une vue de détails de produits, et une vue de parcours d'achat, nous avons des applications respectives soutenues par Node.js pour chacune. Évidemment, cela est une meilleure pratique en termes de couplage lâche et de résilience, mais d'un point de vue code, cela permet de se concentrer plus facilement sur l'implémentation d'une zone de notre frontend.

Mon dernier argument est le suivant ; JavaScript est-il vraiment si difficile à apprendre ? Comme je l'ai dit avant, ECMAScript 5 lui-même est un langage défectueux ; [les différents motifs d'invocation de fonction](https://www.safaribooksonline.com/library/view/javascript-the-good/9780596517748/ch04s03.html) et la manière dont ils affectent le mot-clé `this` et le manque de portée de bloc, par exemple, peuvent le rendre difficile pour les débutants. Cependant, avec ECMAScript 6, plus la pléthore de ressources incroyables disponibles, il est facile de surmonter et d'être conscient de ces problèmes. Pourquoi ne pas simplement sauter l'intermédiaire et apprendre le langage directement ?

Je conclurai en disant que je suis un fan de toutes les approches de typage, mais certaines conviennent mieux à certains scénarios qu'à d'autres. Si JavaScript fonctionne mieux pour la majorité des logiciels frontend, étant donné son ubiquité au sein des équipes de développement et de leurs projets, alors sûrement il n'a pas besoin d'un sur-ensemble. De plus, il existe une multitude de langages qui sont intrinsèquement sûrs en termes de type, alors arrêtez de réinventer la roue !