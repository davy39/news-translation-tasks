---
title: Comment commencer avec Reason
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T01:26:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-reason-cef7ab40660
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vigyGXRulD0Kou3OgnR6HQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Reason
  slug: reason
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment commencer avec Reason
seo_desc: 'By Alireza Alidousti

  In this article, we will build a scheduler in Reason. Along the way, we will see
  how some of the core features of Reason interact with each other and make it an
  excellent fit for this project. You can find everything we cover her...'
---

Par Alireza Alidousti

Dans cet article, nous allons construire un planificateur en Reason. En cours de route, nous verrons comment certaines des fonctionnalités principales de Reason interagissent entre elles et en font un excellent choix pour ce projet. Vous pouvez trouver tout ce que nous couvrons ici dans le [dépôt](https://github.com/Artris/reason-scheduler).

La plupart des articles sur Reason montrent comment il fonctionne dans ReasonReact. Cela a du sens, puisque Facebook a développé Reason. Dans cet article, cependant, je voulais montrer comment Reason brille en tant que langage en dehors de ReasonReact.

Cet article suppose que vous avez une compréhension de base à intermédiaire de JavaScript. Une certaine familiarité avec la programmation fonctionnelle ne ferait pas de mal non plus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vigyGXRulD0Kou3OgnR6HQ.png)
_[arrière-plan pixelisé avec Imagemagick](https://reasonml.github.io/img/reason.svg" rel="noopener" target="_blank" title="">reason.svg</a> converti en png avec Imagemagic, <a href="https://stackoverflow.com/a/506662" rel="noopener" target="_blank" title=")_

### Pourquoi choisir Reason ?

Reason est un langage fonctionnel, qui encourage l'immuabilité, fournit un système de types statiques inférés et se compile en JavaScript. Examinons cela de plus près :

1. Reason et OCaml partagent la même sémantique. Ainsi, les constructions de programmation fonctionnelle disponibles dans OCaml telles que la correspondance de motifs et le currying se traduisent directement en Reason.
2. Dans Reason, presque toujours vous n'avez pas à écrire les types — le compilateur infère les types pour vous. Par exemple, le compilateur voit ceci `() => {1 +` 1} comme une fonction qui prend `une unité (aucun argument) et retourne `un` int.
3. La plupart des constructions dans Reason sont immuables. `List` est immuable. `Array` est mutable mais a une taille fixe. L'ajout d'un nouvel élément à un tableau retourne une copie du tableau étendu avec le nouvel élément. Les `Record`s (similaires aux objets JavaScript) sont immuables.
4. [BuckleScript](https://bucklescript.github.io/) compile Reason en JavaScript. Vous pouvez travailler avec JavaScript dans votre code Reason et utiliser vos modules Reason en JavaScript.

Reason apporte les avantages d'un langage fortement typé à JavaScript à un faible coût. Vous devriez définitivement lire la section [What and Why](https://reasonml.github.io/docs/en/what-and-why.html) de la documentation, car elle fournit plus de contexte sur le langage et ses fonctionnalités.

### Quelques ressources pour vous aider à commencer

1. [La documentation officielle de Reason](https://reasonml.github.io/docs/en/quickstart-javascript.html) est simple et directe
2. [Exploring ReasonML](http://reasonmlhub.com/exploring-reasonml/toc.html), un livre du Dr. Axel Rauschmayer, explore Reason de manière plus pratique
3. [La documentation de BuckleScript](https://bucklescript.github.io/docs/en/interop-overview.html) parle en détail de l'interopérabilité avec JavaScript et OCaml

Dans cet article, nous allons explorer comment différents concepts de Reason tels que les Modules, les Instructions, les Liaisons de Variables et l'Immuabilité fonctionnent ensemble. Chaque fois que j'introduis un nouveau concept ou une nouvelle syntaxe, je lierai les documents et articles associés.

### Le tableau général

Ce tutoriel a été inspiré par [Node Schedule](https://github.com/node-schedule/node-schedule), un planificateur pour Node.js qui utilise un seul timer à tout moment. Vous pouvez en apprendre davantage sur le fonctionnement de Node Schedule [ici](https://medium.com/artris/lazy-jar-scheduling-recurring-events-3e7dd7d246cc).

Aujourd'hui, nous allons créer un planificateur en Reason qui utilise un seul timer à tout moment. Nous utiliserons notre planificateur pour exécuter des travaux récurrents. Ce projet est juste assez grand pour démontrer certains des concepts clés de Reason.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XUqFXUvLLLVLQl1AJ844ow.png)
_Le tableau général :P_

Pour y parvenir, nous allons définir deux modules — un Heap et un Scheduler.

Heap est une implémentation d'une file de priorité. Il maintient les travaux dans l'ordre où ils doivent être exécutés ensuite. La clé d'un élément de heap est le prochain temps d'invocation du travail.

Scheduler est composé d'un heap et est responsable de la mise à jour du timer et de l'exécution des travaux selon les règles de récurrence spécifiées.

1. Lorsqu'un travail s'exécute, le scheduler supprimera le travail de la file, calculera son prochain temps d'invocation et insérera le travail dans la file avec son temps d'invocation mis à jour.
2. Lorsqu'un nouveau travail est ajouté, le scheduler vérifie le prochain temps d'invocation de la racine (tête / le travail qui sera exécuté ensuite). Si le nouveau travail doit être exécuté avant la tête, le scheduler met à jour le timer.

### Module Heap

L'API d'une file de priorité définit :

1. L'insertion d'un nouvel élément dans la file avec une clé représentant sa priorité
2. L'extraction de l'élément avec la priorité la plus élevée
3. La taille de la file

Heap effectue les opérations `insert` et `extract` en ordre `O(log(n))` où `n` est la taille de la file.

_Note : Nous parlerons de la complexité des algorithmes dans la dernière section de l'article. Si vous n'êtes pas à l'aise avec la complexité des algorithmes, vous pouvez ignorer la dernière section._

Si vous n'êtes pas à l'aise avec la structure de données Heap ou avez besoin d'un rappel, je vous recommande de regarder la conférence suivante du [cours MIT OCW 6006](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/). Dans le reste de cette section, nous allons implémenter le pseudocode décrit dans les [notes de cours](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf) de 6006.

#### Définition des types utilisés par le module heap

![Image](https://cdn-media-1.freecodecamp.org/images/1*PyY92n6VujArlyYJRKb4Cw.png)
_heapElement_

`heapElement` définit un type [record](https://reasonml.github.io/docs/en/record.html). Similaire à un objet JavaScript, vous pouvez accéder aux champs du record par leur nom. `{ key: 1, value: "1" }` crée une valeur de type `heapElement(int, string)`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x6t4tuT9L5mwr2LAQbM13A.png)
_Heap.t_

`t('a, 'b)` est un autre type de record et représente le Heap. C'est le type de retour de notre fonction `create` et le dernier paramètre passé à toutes les autres fonctions dans l'API publique de notre module heap.

Pour maintenir la propriété de max heap, Heap n'a besoin que de comparer les clés des éléments dans le tableau. Par conséquent, nous pouvons cacher le type de clé du Heap en fournissant une fonction de comparaison `compare` qui retourne vrai lorsque son premier argument a une priorité plus élevée que le second.

C'est la première fois que nous voyons `ref`. `ref` est la manière de Reason de supporter les [mutations](https://reasonml.github.io/docs/en/mutation.html). Vous pouvez avoir un `ref` vers une valeur et mettre à jour ce `ref` pour pointer vers une nouvelle valeur en utilisant l'opérateur `:=`.

Les [tableaux](http://2ality.com/2018/01/lists-arrays-reasonml.html) dans Reason sont mutables — vous pouvez mettre à jour une valeur à un index spécifique. Cependant, ils ont une longueur fixe. Pour supporter l'ajout et l'extraction, notre heap doit maintenir un `ref` vers un tableau d'éléments de heap. Si nous n'utilisons pas de référence ici, nous allons finir par avoir à retourner un nouveau heap après chaque ajout et extraction. Et les modules qui dépendent du heap doivent garder une trace du nouveau heap.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-p7C-2gEoHXi3e5GJlpACw.png)
_EmptyQueue exception_

Les [exceptions](https://reasonml.github.io/docs/en/exception.html) peuvent être étendues avec de nouveaux constructeurs. Nous allons `lever` l'exception `EmptyQueue` plus tard dans les fonctions `extract` et `head` dans le module heap.

> Les exceptions sont toutes du même type, `exn`. Le type `exn` est un cas spécial dans le système de types OCaml. Il est similaire aux types variants que nous avons rencontrés dans le chapitre 6, Variants, sauf qu'il est ouvert, ce qui signifie qu'il n'est pas entièrement défini en un seul endroit. — [RealWorldOcaml](https://v1.realworldocaml.org/)

#### Signature

![Image](https://cdn-media-1.freecodecamp.org/images/1*o3X_FL51hhzAkipO7pmuLA.png)
_Heap signature_

Par défaut, toutes les liaisons (assignations de variables) dans un [module](http://2ality.com/2017/12/modules-reasonml.html) sont accessibles partout, même en dehors du module où elles sont définies. `signature` est le mécanisme par lequel vous pouvez cacher la logique spécifique à l'implémentation et définir une API pour un module. Vous pouvez définir une signature dans un fichier avec le même nom que le module se terminant par le suffixe .`rei`. Par exemple, vous pouvez définir la signature pour `Heap.re` dans le fichier `Heap.rei`.

Ici, nous exposons la définition de `heapElement` afin que les utilisateurs du module Heap puissent utiliser la valeur retournée par `head` et `extract`. Mais nous ne fournissons pas la définition pour `t` notre type de heap. Cela fait de `t` un [type abstrait](http://2ality.com/2017/12/modules-reasonml.html#abstract-types-hiding-internals) qui garantit que seules les fonctions au sein du module Heap peuvent consommer un heap et le transformer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CFt90fE1yZP_eerExQXMWA.png)
_Heap initializer_

Chaque fonction sauf `create` prend comme argument un heap. `create` prend une fonction de comparaison et crée un `Heap.t` vide qui peut être consommé par les autres fonctions du module Heap.

#### Fonctions d'aide

![Image](https://cdn-media-1.freecodecamp.org/images/1*xsWmdX09mFB9m9PY6a0F5g.png)
_Helper functions_

`parent` est une fonction qui prend un seul argument — index. Elle retourne `None` lorsque l'index est `0`. L'index `0` indique la racine de l'arbre, et la racine d'un arbre n'a pas de parent.

`left` et `right` retournent l'index de l'enfant gauche et de l'enfant droit d'un nœud.

`swap` prend deux index `a` et `b` et un tableau `queue`. Il échange ensuite les valeurs aux index `a` et `b` de la `queue`.

`key` retourne simplement le champ clé d'un `heapElement` à l'index spécifié dans la queue.

`size` retourne la longueur de la queue

#### Add

`add` est l'une des fonctions principales que nous avons exposées dans la signature `heap`. Elle prend une valeur et une clé représentant la priorité de la valeur à insérer dans la queue. Nous utiliserons cette fonction plus tard dans le module `Scheduler` pour ajouter de nouveaux travaux à notre file d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*u6pNMpi_mXftOAQjj72P1Q.png)
_fix up_

`let rec` nous permet de définir des fonctions [récursives](https://reasonml.github.io/docs/en/function.html#recursive-functions). Avec `rec`, vous pouvez faire référence au nom de la fonction à l'intérieur du corps de la fonction.

Nous avons défini `key` comme une fonction qui prend un `queue` et un `index` comme arguments. Avec la déclaration `let key = key(queue)`, nous faisons de l'[ombrage](https://reasonml.github.io/docs/en/let-binding.html#bindings-are-immutable) sur `key` en [appliquant partiellement](https://reasonml.github.io/docs/en/function.html#currying) la fonction d'aide `key` que nous avons définie précédemment.

Lorsque vous fournissez un sous-ensemble des arguments à une fonction, elle retourne une nouvelle fonction qui prend les arguments restants comme entrée — cela est connu sous le nom de [currying](https://reasonml.github.io/docs/en/function.html#currying).

Les arguments que vous avez fournis sont disponibles pour la fonction retournée. Puisque `queue` est fixe dans `fix_up`, nous l'appliquons partiellement à la fonction `key` pour rendre notre code plus [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

Vous pouvez utiliser `<cas[e]>(https://reasonml.github.io/docs/en/pattern-matching.html#when-clauses); when <c`ondition> pour spécifier des conditions supplémentaires dans la correspondance de motifs. Les liaisons de valeurs dans le cas sont disponibles pour l'expression suivant when (dans notre exemple, p_ind est disponible dans compare(key(index), key(p_ind)). Seulem`ent lorsque la condition est satisfaite, nous exécutons l'instruction associée après le =>.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iCjD0S2bmy2RETedIvpEzw.png)
_add_

`add` concatène un nouvel élément à la fin de la queue. Si le nouvel élément a une priorité plus élevée que son parent, il viole la propriété de max heap. `fix_up` est une fonction récursive qui restaure la propriété de max heap en déplaçant le nouvel élément vers le haut dans l'arbre (échange par paires avec son parent) jusqu'à ce qu'il atteigne la racine de l'arbre ou que sa priorité soit inférieure à celle de son parent.

`fix_last` est simplement un wrapper autour de `fix_up` et l'appelle avec l'index du dernier élément de la queue.

`heap.queue^` est la manière dont nous accédons à la valeur à laquelle le `ref` fait référence.

`[||]` est la syntaxe littérale de tableau pour un tableau vide.

#### Extract

`extract` supprime l'élément avec la priorité la plus élevée (dans notre cas, l'élément avec la clé la plus petite) de la queue et le retourne. `extract` supprime la tête de la queue en l'échangeant d'abord avec le dernier élément du tableau. Cela introduit une seule violation de la propriété de max heap à la racine/tête de la queue.

Comme décrit dans la conférence, `heapify` — également connu sous le nom de [sift-down](https://en.wikipedia.org/wiki/Heap_(data_structure)) — corrige une seule violation. En supposant que les sous-arbres gauche et droit du nœud `n` satisfont la propriété de max heap, l'appel de `heapify` sur `n` corrige la violation.

Chaque fois que `heapify` est appelé, il trouve l'index `max_priority_index` de l'élément avec la priorité la plus élevée entre les heapElements aux index `index`, `left(index)`, et `right(index)`. Si `max_priority_index` n'est pas égal à `index`, nous savons qu'il y a encore une violation de la propriété de max heap. Nous échangeons les éléments aux index `index` et `max_priority_index` pour corriger la violation à `index`. Nous appelons récursivement `heapify` avec `max_priority_index` pour corriger la violation possible que nous pourrions créer en échangeant les deux éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*h-3PqzJSyfruTGXgBdaKZg.png)
_heapify_

`index` est un `int` représentant la racine d'un sous-arbre qui viole la propriété de max heap, mais ses sous-arbres satisfont la propriété. `compare` est la fonction de comparaison définie avec le heap. `queue` est un tableau qui contient les éléments du heap.

Les instructions `[if](https://reasonml.github.io/docs/en/if-else.html)` [statements](https://reasonml.github.io/docs/en/if-else.html) dans Reason, comme les autres expressions, évaluent à une valeur. Ici, les instructions `if` évaluent à un `int` qui représente quel index était plus petit dans la comparaison.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fiHB42uHbI8KsPxBQaxZTQ.png)
_extract_

`extract` fait correspondre le motif contre `queue` (le tableau, pas la référence).

`[|head|]` ne correspond qu'à un tableau avec un seul élément.

Lorsque la queue est vide `[||]`, nous levons l'exception `EmptyQueue` que nous avons définie précédemment. Mais pourquoi ? Pourquoi ne pas retourner `None` à la place ? Eh bien, c'est une question de préférence. Je préfère `lever` une exception, car lorsque j'utilise cette fonction, j'obtiens un `heapElement` et non un `option(heapElement)`. Cela m'évite de faire correspondre le motif contre la valeur retournée de `extract`. L'inconvénient est que vous devez être prudent lorsque vous utilisez cette fonction, en vous assurant que `queue` n'est jamais vide.

Lorsque nous avons plus d'un élément, nous échangeons le premier et le dernier élément de la queue, supprimons le dernier élément et appelons `heapify` sur le premier élément (la racine de l'arbre).

### Testing

Nous utilisons `bs-jest` — les liaisons BuckleScript pour `Jest` — pour écrire des tests. `Jest` est un framework de test créé par Facebook qui vient avec une bibliothèque de mocking intégrée et des rapports de couverture de code.

1. [https://github.com/glennsl/bs-jest](https://github.com/glennsl/bs-jest)
2. [https://facebook.github.io/jest/docs/en/getting-started.html](https://facebook.github.io/jest/docs/en/getting-started.html)

Suivez les instructions dans [bs-jest](https://github.com/glennsl/bs-jest#installation) pour configurer `Jest`.

Assurez-vous d'ajouter `@glennsl/bs-jest` à `bs-dev-dependencies` dans votre `bsconfig.json`. Sinon, BuckleScript ne trouvera pas le module `Jest` et votre build échouera.

Si vous écrivez vos cas de test dans un répertoire autre que `src`, vous devez le spécifier dans les `sources` dans le `bsconfig.json` pour que le compilateur BuckleScript les prenne en compte.

### Testing synchronous functions

Avec le module `Heap` en place et `Jest` installé, nous sommes prêts à écrire notre premier cas de test.

Pour tester notre module `Heap`, nous allons faire un heap sort.

1. créer un heap
2. insérer des éléments dans le heap
3. utiliser l'opération `extract` pour supprimer les éléments dans l'ordre croissant

![Image](https://cdn-media-1.freecodecamp.org/images/1*VITeahvFmnplQfFoCcpgWQ.png)
_Heap sort test_

`open Jest` ouvre le module afin que nous puissions nous référer aux liaisons disponibles dans le module `Jest` sans les préfixer avec `Jest.`. Par exemple, au lieu d'écrire `Jest.expect`, nous pouvons simplement écrire `expect`.

Nous utilisons `let {value: e1} =` pour déstructurer la valeur retournée par `extract` et créer un alias `e1` pour `value` — `e1` est maintenant lié au champ `value` de la valeur retournée par `extract`.

Avec l'opérateur `|&`g[t; pipe opera](http://2ality.com/2017/12/functions-reasonml.html#the-reverse-application-operator)tor, nous pouvons créer une fonction composite et appliquer la fonction résultante immédiatement sur une entrée. Ici, nous passons simplement le résultat de l'appel de `exp`ect avec (e1, ..., e9) à la fonction `toEq`ual.

### Scheduler module

Scheduler utilise le module Heap pour maintenir une liste de travaux récurrents triés par leur prochain temps d'invocation.

#### Définissons les types utilisés dans le module Scheduler

![Image](https://cdn-media-1.freecodecamp.org/images/1*M8mc6n7IKLQO3WSHugkrxQ.png)
_recurrence_

`recurrence` est un type [Variant](https://reasonml.github.io/docs/en/variant.html). Toute valeur du type `recurrence` peut être soit une `Second`, `Minute`, ou une `Hour`. `Second`, `Minute` et `Hour` sont les constructeurs pour `recurrence`. Vous pouvez invoquer un constructeur comme une fonction normale et obtenir une valeur du type Variant. Dans notre cas, si vous appelez `Second` avec un int, vous obtenez une valeur de type `recurrence`. Vous pouvez faire correspondre ce motif de valeur avec `Second(number_of_seconds)` pour accéder à l'argument qui a été passé au constructeur `Second`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VFEqg9AK0jp47yiNb9w5iA.png)
_job_

`job` est un type [record](https://reasonml.github.io/docs/en/record.html). `period` est de type `recurrence` et indique le délai entre chaque exécution d'un travail. `invoke` est une fonction qui prend `unit` (aucun argument) et retourne `unit` (aucun résultat). `invoke` est la fonction qui est exécutée lorsque le travail s'exécute.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UPPSJx7GxuMOdNN83JUiUw.png)
_Scheduler.t_

`t` est un type de record représentant le scheduler. Un scheduler maintient une `queue` de travaux triés par leur prochain temps d'invocation. `timer_id` référence le `timerId` pour le premier travail dans la `queue` — le travail qui sera invoqué en premier.

#### Interop

Vous pouvez invoquer des fonctions JavaScript depuis Reason. Il existe différentes manières de faire cela :

1. vous pouvez utiliser les liaisons BuckleScript si disponibles, telles que `Js.log`, et `[Js.Global.setTimeout](https://bucklescript.github.io/bucklescript/api/Js.Global.html)`
2. déclarer un `external` tel que `[@bs.val] external setTimeout`
3. exécuter du code JavaScript brut avec `[%raw ...]`

Les liaisons pour la plupart des fonctions JavaScript sont fournies par BuckleScript. Par exemple, `[Js.Date.getTime](https://bucklescript.github.io/bucklescript/api/Js.Date.html#VALgetTime)` prend un `Js.Date.t` — une valeur `date` — et retourne le nombre de millisecondes depuis l'époque. `Js.Date.getTime` est la liaison pour la méthode `getTime` de l'objet Date JavaScript. `Js.Date.getTime` retourne une valeur `float`.

L'utilisation des liaisons BuckleScript est exactement la même que l'utilisation des modules définis par l'utilisateur. Vous pouvez en lire plus sur les liaisons disponibles [ici](https://bucklescript.github.io/docs/en/stdlib-overview). Pour le reste de cette section, nous allons nous concentrer sur `external` et `[%raw ...]`.

#### external

Avec `[external](https://bucklescript.github.io/docs/en/intro-to-external.html)`, vous pouvez lier une variable à une fonction JavaScript. Ici, par exemple, nous lions la variable `setTimeout` à la fonction globale setTimeout de JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YmF0EZ_kc_ShonlkILaxeg.png)
_setTimeout et clearTimeout définition dans [BuckleScript docs](https://bucklescript.github.io/docs/en/bind-to-global-values.html#abstract-type" rel="noopener" target="_blank" title=")_

`setTimeout` retourne un `float`, un identifiant que nous pouvons passer à `clearTimeout` pour annuler le timer. La seule fonction qui utilise la valeur retournée par `setTimeout` est `clearTimeout`. Nous pouvons donc définir la valeur retournée par `setTimeout` pour avoir un [type abstrait](https://bucklescript.github.io/docs/en/bind-to-global-values.html). Cela garantit que seule une valeur retournée par `setTimeout` peut être passée à `clearTimeout`.

#### [%raw …]

`new Date.getTime()` en JavaScript retourne un entier Number. [Les nombres en JavaScript sont longs de 64 bits](https://www.w3schools.com/js/js_numbers.asp). Les [int](https://reasonml.github.io/docs/en/integer-and-float.html#integers) [en Reason ne sont longs que de 32 bits](https://reasonml.github.io/docs/en/integer-and-float.html#integers). C'est un problème !

Dans Reason, nous pouvons travailler avec la valeur retournée de `new Date.getTime()` en nous attendant à ce qu'elle soit `Float`. C'est en fait le type de retour attendu de `[Js.Date.getTime](https://bucklescript.github.io/bucklescript/api/Js.Date.html#VALgetTime)` fourni par BuckleScript.

Au lieu de cela, utilisons `[%raw ...]` et créons un type abstrait `long` similaire à ce que nous avons fait pour `setTimeout`. En faisant cela, nous cachons l'implémentation de `long`. Notre code Reason peut passer des valeurs de type `long`, mais il ne peut pas vraiment opérer sur elles. Pour cela, nous définissons un ensemble de liaisons d'aide qui prennent des valeurs de type `long` et délèguent le calcul à des expressions JavaScript brutes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZRlUB2r52RGmC-OTO4VCfg.png)
_working with JavaScript values_

Nous pouvons définir une expression JavaScript avec `[[%raw ...]](https://bucklescript.github.io/docs/en/embed-raw-javascript.html)`. Ici, nous définissons un [type abstrait](https://bucklescript.github.io/docs/en/bind-to-global-values.html#abstract-type) `long` et un ensemble de fonctions qui consomment et retournent des valeurs de type `long`. Le type de toutes les expressions est spécifié dans les liaisons `let`.

`time_now` retourne le nombre de millisecondes depuis l'époque.

Nous utilisons `sum` pour calculer le prochain temps d'invocation d'un travail, en passant le résultat de `time_now` et un `int` représentant combien de millisecondes à partir de maintenant le travail doit être exécuté.

Nous pouvons calculer combien de temps à partir de maintenant un travail sera invoqué en `subtract`ant le temps d'invocation d'un travail de `time_now`. Le résultat de `subtract` est passé à `setTimeout`.

`has_higher_priority` compare deux temps d'invocation. C'est la fonction de comparaison que nous utilisons pour initialiser notre Heap.

#### Invocation

À tout moment, nous n'avons qu'un seul timer qui expire lorsque le premier travail de la queue doit s'exécuter. Lorsque le timer expire, nous devons faire un peu de nettoyage. Lorsque le timer expire, nous devons

1. extraire le premier travail de la queue
2. calculer son prochain temps d'invocation (une nouvelle clé pour le travail)
3. insérer le travail dans la queue avec sa clé mise à jour
4. regarder la tête de la queue pour trouver le travail qui doit être exécuté ensuite et
5. créer un nouveau timer pour ce travail

![Image](https://cdn-media-1.freecodecamp.org/images/1*DO8Jffa0o3kOz7iewxbxbg.png)
_helpers_

`wait` prend une période — une valeur de type `recurrence` — et retourne un int représentant combien de milli-secondes un travail doit attendre avant de s'exécuter à nouveau. Nous passons la valeur retournée par `wait` à `setTimeout`.

`next_invocation` calcule le prochain temps d'invocation d'un travail. `time_now` retourne une valeur `long`. `sum` prend un `long` et une valeur `int` et retourne une valeur `long`. `sum` additionne les deux nombres en appelant l'opérateur JavaScript `+` sur ses arguments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aDR8VZdEHsqnbVjyw3lbyQ.png)
_Invoking a job_

`execute` est une fonction récursive qui est responsable de l'exécution du travail et du nettoyage. Elle capture le scheduler dans une fermeture et retourne une fonction qui peut être invoquée lorsque le timer expire.

Dans les trois premières lignes, nous supprimons le travail avec la priorité la plus élevée (clé la plus basse ou temps d'invocation le plus proche) et le réinsérons dans la queue avec son prochain temps d'invocation.

Nous continuons ensuite à créer un nouveau timer pour le travail à la tête de la queue (le prochain travail qui doit être exécuté après cette invocation). Nous mettons à jour la référence `timer_id` pour pointer vers le nouveau `timerId`.

Enfin, nous appelons le champ `invoke` du travail pour effectuer la tâche spécifiée.

#### Add a new job

![Image](https://cdn-media-1.freecodecamp.org/images/1*CUaRpxz-tRRsmTibKHsCkQ.png)
_adding a new job_

Lorsque la `queue` est vide, l'ajout d'un nouveau travail est simple. Nous créons un timer qui expire au prochain temps d'invocation du travail.

Le cas plus intéressant est lorsque la queue n'est pas vide ! Nous pouvons avoir deux situations ici. Soit la tête de la `queue` a une clé supérieure au prochain temps d'invocation du travail, soit non.

Le premier cas est lorsque la tête de la `queue` a une clé inférieure ou égale au prochain temps d'invocation du travail. C'est le cas lorsque le nouveau travail doit être exécuté avant le timer actuel. Dans ce cas, nous devons annuler le timer en appelant `clearTimeout` avec le `timer_id` et créer un nouveau timer qui expirera au prochain temps d'invocation du nouveau travail.

Dans l'autre cas, parce que le nouveau travail doit être exécuté après l'expiration du timer actuel, nous pouvons simplement insérer le nouveau travail dans la `queue`.

### Testing asynchronous functions

Toutes les fonctions du module heap sont [synchrones](https://medium.com/@siddharthac6/javascript-execution-of-synchronous-and-asynchronous-codes-40f3a199e687). Par exemple, lorsque vous appelez `add`, vous êtes bloqué jusqu'à ce qu'un nouvel heapElement ait été ajouté à la queue. Lorsque `add` retourne, vous savez que le heap a été étendu avec le nouvel élément.

Les fonctions du scheduler, en revanche, ont des [effets secondaires asynchrones](https://medium.com/@siddharthac6/javascript-execution-of-synchronous-and-asynchronous-codes-40f3a199e687). Lorsque vous `add` un nouveau travail au scheduler, le scheduler ajoute le travail à sa queue et retourne. Plus tard, selon la règle de `recurrence`, le travail est invoqué. Votre code n'attend pas que le travail soit invoqué et continue de s'exécuter.

Maintenant, écrivons un cas de test pour nous assurer que lorsqu'un travail est ajouté au scheduler, il est invoqué selon sa règle de récurrence.

Pour ce faire, nous allons

1. `add` un travail au scheduler pour qu'il soit exécuté chaque seconde. Ce travail incrémente un compteur `ref(int)`.
2. créer une `Promise` qui se résout après 4s
3. retourner une `Jest.assertion` promise qui s'attend à ce que le compteur ait été incrémenté 4 fois.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5w1tMJibX4SAKV_1Aa98wA.png)
_Test Scheduler add_

Nous pouvons utiliser `testPromise` pour tester les promesses. `testPromise` attend un `Js.Promise.t(Jest.assertion)`. Regardez la dernière ligne du cas de test.

`Scheduler.Second(1)` indique que nous voulons que notre travail s'exécute chaque seconde.

`counter` est un `ref` et chaque fois que `invoke` est appelé, il est incrémenté.

`promise` est un `[Js.Promise.t](https://reasonml.github.io/docs/en/promise.html)` qui se résoudra après 4s. Remarquez que nous attendons 4,1s pour nous assurer que le dernier appel à `invoke` a fini de s'exécuter. Sinon, nous pourrions résoudre la promesse lorsque nous n'avons incrémenté le compteur que trois fois.

Vous pouvez utiliser `|&`gt; pour chaîner les promesses. Dans notre exemple, `prom`ise se résoudra avec la valeur du compteur après 4s. Cette valeur est fournie comme le `co`unt à la fonction passée à `Js.Promise.th`en_.

### Optimize

Nous avons implémenté nos modules Heap et Scheduler de manière similaire à ce que nous aurions fait en JavaScript. En faisant cela, nous avons réduit les performances des fonctions opérant sur le heap telles que `add` et `extract` à `O(n)`.

Nous savons que Array en Reason a une longueur fixe. Chaque fois que nous ajoutons un nouveau travail ou en supprimons un, la taille de notre Array changera et donc une nouvelle copie sera créée. Nous pouvons corriger cela en créant un module de tableau dynamique qui implémente le [doublement de table](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-9-table-doubling-karp-rabin/).

J'ai créé une version de Heap et Dynamic Array si vous êtes intéressé par l'[implémentation](https://github.com/Artris/algorithms), cependant, je pense que cela serait en dehors du cadre de cet article. Donc pour l'instant, nous nous concentrons sur l'optimisation du Scheduler en appelant des opérations qui coûtent `O(n)` moins fréquemment.

Il y a deux endroits dans le Scheduler où nous appelons `Heap.add` et `Heap.extract` — lors de l'ajout d'un nouveau travail et lors de l'exécution d'un travail.

Nous ne pouvons pas aider `Scheduler.add` mais nous pouvons corriger les performances de `Scheduler.execute`. La fonction `execute` n'a pas besoin d'appeler `extract` ou `add` puisque la taille de notre queue avant et après `execute` devrait être la même.

Introduisons une nouvelle fonction à notre signature Heap. `decrease_root_priority` réduit la priorité de la racine du Heap. Nous pouvons utiliser cette nouvelle fonction pour mettre à jour la clé racine à son prochain temps d'invocation sans d'abord extraire la tête de la queue et la réinsérer avec son temps d'invocation mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fZg1ncv_dVYefFbr39tJdA.png)
_execute optimized_

`decrease_root_priority` prend la nouvelle priorité pour la racine, vérifie que la nouvelle priorité est inférieure à la priorité actuelle de la racine, et délègue le travail réel à une fonction d'aide `update_priority`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pb-1W-PBteiPwhpSroPCbA.png)
_decrease root priority_

`update_priority` peut diminuer ou augmenter la priorité de n'importe quel élément dans un Heap en `O(log(n))`. Il vérifie si la nouvelle priorité viole la propriété de max heap par rapport aux enfants d'un nœud ou à son parent. Lorsque nous augmentons la priorité d'un nœud, nous pouvons violer la propriété de max heap du nœud par rapport à son parent et donc nous `fix_up`. Lorsque nous diminuons la priorité d'un nœud, nous pouvons violer la propriété de max heap par rapport à ses enfants et donc nous appelons `heapify` pour corriger la violation possible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kPgoqtoJBe-Lt8zoZRTP2A.png)
_decrease priority_

### Next steps

Cet article est de loin un aperçu complet des fonctionnalités de Reason. Nous avons vu beaucoup de constructions du langage, mais ne les avons pas explorées en détail. Il y a aussi des fonctionnalités qui ont été laissées de côté, comme les foncteurs et les objets. Je vous recommande fortement de lire la [documentation](https://reasonml.github.io/docs/en/overview) ou [Exploring ReasonML and functional programming](http://reasonmlhub.com/exploring-reasonml/index.html) pour savoir ce qui est disponible pour vous avant de vous lancer dans le codage.

Le code source complet de ce que nous avons couvert aujourd'hui est disponible dans la branche `master` de [https://github.com/Artris/reason-scheduler](https://github.com/Artris/reason-scheduler)

Si vous voulez pratiquer, je vous encourage à ajouter la fonctionnalité `remove` au scheduler. En particulier, étendez la signature du `Scheduler` avec

* `type jobId` et
* `let remove = (t, jobId) => u`nit

Je vous encourage également à ajouter des cas de test pour les fonctions exposées dans la signature des modules `Heap` et `Scheduler`.

Les cas de test pour toutes les fonctions des modules `Heap` et `Scheduler` ainsi qu'une implémentation pour la fonctionnalité `remove` sont disponibles dans la branche [solutions](https://github.com/Artris/reason-scheduler/tree/solutions).

### Attribution

Je tiens à remercier la communauté Reason/BuckleScript pour avoir fourni une documentation détaillée. Et le Dr. [Axel Rauschmayer](http://2ality.com/) pour le livre [Exploring ReasonML](http://reasonmlhub.com/exploring-reasonml/toc.html) et de nombreux articles intéressants sur Reason.

Les extraits de code ont été générés en utilisant [carbon.now.sh](https://carbon.now.sh/).

Je tiens également à remercier [Grace](https://twitter.com/graziettahof), [Sami](https://twitter.com/sami_elfeki), [Freeman](https://twitter.com/freestellar), et [Preetpal](https://github.com/preetpalS) qui ont aidé à réviser cet article.