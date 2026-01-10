---
title: 'Les essentiels de JavaScript : pourquoi vous devriez savoir comment le moteur
  fonctionne'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-04T22:14:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-essentials-why-you-should-know-how-the-engine-works-c2cc0d321553
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SKOyguJ-AC0DmiQ8ZS0FwQ.jpeg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Les essentiels de JavaScript : pourquoi vous devriez savoir comment le
  moteur fonctionne'
seo_desc: 'By Rainer Hahnekamp

  This article is also available in Spanish.

  In this article, I want to explain what a software developer, who uses JavaScript
  to write applications, should know about engines so that the written code executes
  properly.

  You’ll see b...'
---

Par Rainer Hahnekamp

Cet article est également disponible en [espagnol](https://www.campusmvp.es/recursos/post/fundamentos-de-javascript-por-que-deberias-saber-como-funciona-el-motor.aspx).

Dans cet article, je souhaite expliquer ce qu'un développeur logiciel, qui utilise JavaScript pour écrire des applications, devrait savoir sur les moteurs afin que le code écrit s'exécute correctement.

Vous verrez ci-dessous une fonction en une ligne qui retourne la propriété lastName de l'argument passé. Simplement en ajoutant une seule propriété à chaque objet, nous obtenons une baisse de performance de plus de 700 % !

Comme je vais l'expliquer en détail, le manque de types statiques de JavaScript entraîne ce comportement. Considéré autrefois comme un avantage par rapport à d'autres langages comme C# ou Java, cela s'avère être plutôt un « pacte faustien ».

### Freinage à pleine vitesse

Habituellement, nous n'avons pas besoin de connaître les détails internes d'un moteur qui exécute notre code. Les éditeurs de navigateurs investissent massivement pour rendre les moteurs très rapides.

Super !

Laissez les autres faire le travail difficile. Pourquoi se soucier de savoir comment les moteurs fonctionnent ?

Dans notre exemple de code ci-dessous, nous avons cinq objets qui stockent les prénoms et noms de famille de personnages de Star Wars. La fonction `getName` retourne la valeur de lastname. Nous mesurons le temps total que cette fonction prend pour s'exécuter 1 milliard de fois :

```
(() => {   const han = {firstname: "Han", lastname: "Solo"};  const luke = {firstname: "Luke", lastname: "Skywalker"};  const leia = {firstname: "Leia", lastname: "Organa"};  const obi = {firstname: "Obi", lastname: "Wan"};  const yoda = {firstname: "", lastname: "Yoda"};  const people = [    han, luke, leia, obi,     yoda, luke, leia, obi   ];  const getName = (person) => person.lastname;
```

```
  console.time("engine");  for(var i = 0; i < 1000 * 1000 * 1000; i++) {     getName(people[i & 7]);   }  console.timeEnd("engine"); })();
```

Sur un Intel i7 4510U, le temps d'exécution est d'environ 1,2 seconde. Jusqu'à présent, tout va bien. Nous ajoutons maintenant une autre propriété à chaque objet et l'exécutons à nouveau.

```
(() => {  const han = {    firstname: "Han", lastname: "Solo",     spacecraft: "Falcon"};  const luke = {    firstname: "Luke", lastname: "Skywalker",     job: "Jedi"};  const leia = {    firstname: "Leia", lastname: "Organa",     gender: "female"};  const obi = {    firstname: "Obi", lastname: "Wan",     retired: true};  const yoda = {lastname: "Yoda"};
```

```
  const people = [    han, luke, leia, obi,     yoda, luke, leia, obi];
```

```
  const getName = (person) => person.lastname;
```

```
  console.time("engine");  for(var i = 0; i < 1000 * 1000 * 1000; i++) {    getName(people[i & 7]);  }  console.timeEnd("engine");})();
```

Notre temps d'exécution est maintenant de 8,5 secondes, ce qui est environ 7 fois plus lent que notre première version. Cela donne l'impression de freiner à pleine vitesse. Comment cela a-t-il pu se produire ?

Il est temps de regarder de plus près le moteur.

### Forces combinées : Interpréteur et Compilateur

Le moteur est la partie qui lit et exécute le code source. Chaque grand éditeur de navigateur a son propre moteur. Mozilla Firefox a Spidermonkey, Microsoft Edge a Chakra/ChakraCore et Apple Safari nomme son moteur JavaScriptCore. Google Chrome utilise V8, qui est également le moteur de Node.js.

La sortie de V8 en 2008 a marqué un moment décisif dans l'histoire des moteurs. V8 a remplacé l'interprétation relativement lente de JavaScript par le navigateur.

La raison derrière cette amélioration massive réside principalement dans la combinaison de l'interpréteur et du compilateur. Aujourd'hui, les quatre moteurs utilisent cette technique.

L'interpréteur exécute le code source presque immédiatement. Le compilateur génère du code machine que le système de l'utilisateur exécute directement.

Alors que le compilateur travaille sur la génération de code machine, il applique des optimisations. La compilation et l'optimisation résultent en une exécution de code plus rapide malgré le temps supplémentaire nécessaire dans la phase de compilation.

L'idée principale derrière les moteurs modernes est de combiner le meilleur des deux mondes :

* Démarrage rapide de l'application de l'interpréteur.
* Exécution rapide du compilateur.

![Image](https://cdn-media-1.freecodecamp.org/images/xcTig2PibioQS1T5oImy5exOvcn43uda9R42)
_Un moteur moderne utilise un interpréteur et un compilateur. Source : [imgflip](https://imgflip.com/i/23g834" rel="noopener" target="_blank" title=")_

Atteindre ces deux objectifs commence par l'interpréteur. En parallèle, le moteur marque les parties de code fréquemment exécutées comme un « Hot Path » et les transmet au compilateur avec des informations contextuelles recueillies pendant l'exécution. Ce processus permet au compilateur de s'adapter et d'optimiser le code pour le contexte actuel.

Nous appelons le comportement du compilateur « Just in Time » ou simplement JIT.

Lorsque le moteur fonctionne bien, vous pouvez imaginer certains scénarios où JavaScript surpasse même C++. Il n'est pas surprenant que la plupart du travail du moteur aille dans cette « optimisation contextuelle ».

![Image](https://cdn-media-1.freecodecamp.org/images/bu47j9z9Dee3O3hHm51ijuARr3aUTtj4j4EH)
_Interaction entre l'interpréteur et le compilateur_

### Types statiques pendant l'exécution : Inline Caching

L'Inline Caching, ou IC, est une technique d'optimisation majeure au sein des moteurs JavaScript. L'interpréteur doit effectuer une recherche avant de pouvoir accéder à une propriété d'un objet. Cette propriété peut faire partie du prototype d'un objet, avoir une méthode getter ou même être accessible via un proxy. La recherche de la propriété est assez coûteuse en termes de vitesse d'exécution.

Le moteur attribue à chaque objet un « type » qu'il génère pendant l'exécution. V8 appelle ces « types », qui ne font pas partie de la norme ECMAScript, des classes cachées ou des formes d'objet. Pour que deux objets partagent la même forme d'objet, les deux objets doivent avoir exactement les mêmes propriétés dans le même ordre. Ainsi, un objet `{firstname: "Han", lastname: "Solo"}` serait attribué à une classe différente de `{lastname: "Solo", firstname: "Han"}`.

Avec l'aide des formes d'objet, le moteur connaît l'emplacement mémoire de chaque propriété. Le moteur code en dur ces emplacements dans la fonction qui accède à la propriété.

Ce que fait l'Inline Caching, c'est éliminer les opérations de recherche. Il n'est pas surprenant que cela produise une énorme amélioration des performances.

Revenons à notre exemple précédent : Tous les objets de la première exécution n'avaient que deux propriétés, `firstname` et `lastname`, dans le même ordre. Disons que le nom interne de cette forme d'objet est `p1`. Lorsque le compilateur applique IC, il présume que la fonction ne reçoit que la forme d'objet `p1` et retourne la valeur de `lastname` immédiatement.

![Image](https://cdn-media-1.freecodecamp.org/images/o4aMw-H7fhu2dKraaGPkHqOiV0lMAJr7ks3j)
_Inline Caching en action (Monomorphique)_

Dans la deuxième exécution, cependant, nous avons traité avec 5 formes d'objet différentes. Chaque objet avait une propriété supplémentaire et `yoda` manquait complètement `firstname`. Que se passe-t-il une fois que nous traitons avec plusieurs formes d'objet ?

### Canards intervenants ou types multiples

La programmation fonctionnelle a le concept bien connu de « duck typing » où une bonne qualité de code exige des fonctions qui peuvent gérer plusieurs types. Dans notre cas, tant que l'objet passé a une propriété lastname, tout va bien.

L'Inline Caching élimine la recherche coûteuse de l'emplacement mémoire d'une propriété. Il fonctionne mieux lorsque, à chaque accès à une propriété, l'objet a la même forme d'objet. Cela s'appelle l'IC monomorphique.

Si nous avons jusqu'à quatre formes d'objet différentes, nous sommes dans un état IC polymorphe. Comme dans le monomorphique, le code machine optimisé « connaît » déjà les quatre emplacements. Mais il doit vérifier à laquelle des quatre formes d'objet possibles l'argument passé appartient. Cela entraîne une diminution des performances.

Une fois que nous dépassons le seuil de quatre, cela devient dramatiquement pire. Nous sommes maintenant dans un état IC mégamorphique. Dans cet état, il n'y a plus de mise en cache locale des emplacements mémoire. Au lieu de cela, il doit être recherché dans un cache global. Cela entraîne la chute extrême de performance que nous avons vue ci-dessus.

### Polymorphique et Mégamorphique en action

Ci-dessous, nous voyons un Inline Cache polymorphe avec 2 formes d'objet différentes.

![Image](https://cdn-media-1.freecodecamp.org/images/lNpKqU5ShHJkat0PpKIahkpFAwPOHpCJRIiA)
_Inline Cache Polymorphe_

Et l'IC mégamorphique de notre exemple de code avec 5 formes d'objet différentes :

![Image](https://cdn-media-1.freecodecamp.org/images/cDEEsdQECGIz20LpuSYqgtUtjRCD1wD0hRPx)
_Inline Cache Mégamorphique_

### La classe JavaScript à la rescousse

D'accord, nous avions 5 formes d'objet et nous sommes tombés dans un IC mégamorphique. Comment pouvons-nous corriger cela ?

Nous devons nous assurer que le moteur marque nos 5 objets comme ayant la même forme d'objet. Cela signifie que les objets que nous créons doivent contenir toutes les propriétés possibles. Nous pourrions utiliser des littéraux d'objet, mais je trouve que les classes JavaScript sont une meilleure solution.

Pour les propriétés qui ne sont pas définies, nous passons simplement `null` ou les omettons. Le constructeur s'assure que ces champs sont initialisés avec une valeur :

```
(() => {  class Person {    constructor({      firstname = '',      lastname = '',      spaceship = '',      job = '',      gender = '',      retired = false    } = {}) {      Object.assign(this, {        firstname,        lastname,        spaceship,        job,        gender,        retired      });    }  }
```

```
  const han = new Person({    firstname: 'Han',    lastname: 'Solo',    spaceship: 'Falcon'  });  const luke = new Person({    firstname: 'Luke',    lastname: 'Skywalker',    job: 'Jedi'  });  const leia = new Person({    firstname: 'Leia',    lastname: 'Organa',    gender: 'female'  });  const obi = new Person({    firstname: 'Obi',    lastname: 'Wan',    retired: true  });  const yoda = new Person({ lastname: 'Yoda' });  const people = [    han,    luke,    leia,    obi,    yoda,    luke,    leia,    obi  ];  const getName = person => person.lastname;  console.time('engine');  for (var i = 0; i < 1000 * 1000 * 1000; i++) {    getName(people[i & 7]);  }  console.timeEnd('engine');})();
```

Lorsque nous exécutons cette fonction à nouveau, nous voyons que notre temps d'exécution revient à 1,2 seconde. Mission accomplie !

### Résumé

Les moteurs JavaScript modernes combinent les avantages de l'interpréteur et du compilateur : démarrage rapide de l'application et exécution rapide du code.

L'Inline Caching est une technique d'optimisation puissante. Il fonctionne mieux lorsqu'une seule forme d'objet est passée à la fonction optimisée.

Mon exemple drastique a montré les effets des différents types d'Inline Caching et les pénalités de performance des caches mégamorphiques.

L'utilisation des classes JavaScript est une bonne pratique. Les transpilateurs à typage statique, comme TypeScript, rendent les IC monomorphiques plus probables.

#### Lectures complémentaires

* David Mark Clements : Performance Killers for TurboShift and Ignition : [https://github.com/davidmarkclements/v8-perf](https://github.com/davidmarkclements/v8-perf)
* Victor Felder : JavaScript Engines Hidden Classes
[https://draft.li/blog/2016/12/22/javascript-engines-hidden-classes](https://draft.li/blog/2016/12/22/javascript-engines-hidden-classes)
* Jörg W. Mittag : Overview of JIT Compiler and Interpreter
[https://softwareengineering.stackexchange.com/questions/246094/understanding-the-differences-traditional-interpreter-jit-compiler-jit-interp/269878#269878](https://softwareengineering.stackexchange.com/questions/246094/understanding-the-differences-traditional-interpreter-jit-compiler-jit-interp/269878#269878)
* Vyacheslav Egorov : What’s up with Monomorphism
[http://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html](http://mrale.ph/blog/2015/01/11/whats-up-with-monomorphism.html)
* WebComic expliquant Google Chrome
[https://www.google.com/googlebooks/chrome/big_00.html](https://www.google.com/googlebooks/chrome/big_00.html)
* Huiren Woo : Differences between V8 and ChakraCore
[https://developers.redhat.com/blog/2016/05/31/javascript-engine-performance-comparison-v8-charkra-chakra-core-2/](https://developers.redhat.com/blog/2016/05/31/javascript-engine-performance-comparison-v8-charkra-chakra-core-2/)
* Seth Thompson : V8, Advanced JavaScript, & the Next Performance Frontier
[https://www.youtube.com/watch?v=EdFDJANJJLs](https://www.youtube.com/watch?v=EdFDJANJJLs)
* Franziska Hinkelmann — Performance Profiling for V8
[https://www.youtube.com/watch?v=j6LfSlg8Fig](https://www.youtube.com/watch?v=j6LfSlg8Fig)
* Benedikt Meurer : An Introduction to Speculative Optimization in V8
[https://ponyfoo.com/articles/an-introduction-to-speculative-optimization-in-v8](https://ponyfoo.com/articles/an-introduction-to-speculative-optimization-in-v8)
* Mathias Bynens : JavaScript engine fundamentals: Shapes and Inline Caches
[https://mathiasbynens.be/notes/shapes-ics](https://mathiasbynens.be/notes/shapes-ics)