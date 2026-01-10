---
title: Une approche fonctionnelle de l'algorithme de tri fusion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-11T00:04:59.000Z'
originalURL: https://freecodecamp.org/news/a-functional-approach-to-merge-sort-and-algorithms-in-general-bbc12457eeb0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1AHesZT5E0EAaT7feMhbaQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Erlang
  slug: erlang
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Une approche fonctionnelle de l'algorithme de tri fusion
seo_desc: 'By Joe Chasinga

  Algorithms are often difficult for people to understand. I believe that this is
  because they are most often programmed or explained in a language that encourages
  thinking in procedures or instructions which are not intuitive.

  Very oft...'
---

Par Joe Chasinga

Les algorithmes sont souvent difficiles à comprendre pour les gens. Je crois que cela est dû au fait qu'ils sont le plus souvent programmés ou expliqués dans un langage qui encourage à penser en procédures ou en instructions qui ne sont pas intuitives.

Très souvent, l'essentiel d'un algorithme (comment résoudre un problème particulier de manière logique sans codage informatique) semble très simple et compréhensible lorsqu'il est décrit graphiquement. Cependant, il est surprenant de constater qu'il ne se traduit souvent pas bien en code écrit dans des langages comme Python, Java ou C++. Il devient donc beaucoup plus difficile à comprendre.

**En d'autres termes, le concept algorithmique ne correspond pas directement à la manière dont le code doit être écrit et lu.**

### Pourquoi les algorithmes sont-ils si difficiles à coder ?

Eh bien, nous pourrions blâmer le fonctionnement interne des premiers ordinateurs électromécaniques. Les premiers inventeurs de certains des langages de programmation les plus utilisés aujourd'hui n'ont jamais pu se débarrasser de ces caractéristiques. Ou peut-être ne pouvaient-ils s'empêcher de laisser leurs empreintes sur leurs inventions. Une fois que vous comprenez si bien les ordinateurs, il n'y a pas de retour en arrière possible.

Pour aggraver les choses, en plus des langages déjà micro-gérés, quelqu'un a dû inventer une API pour une meilleure micro-gestion. Ils l'ont appelée programmation orientée objet (POO) et ont ajouté le concept de classes à la programmation — mais je pense que les modules et les fonctions pourraient gérer les mêmes choses très bien, merci beaucoup.

C++ n'a pas rendu C meilleur, mais il a ouvert la voie en inspirant plus de descendants de la POO. Et ensemble, toutes ces choses rendent la pensée algorithmique abstraite difficile pour les raisons mentionnées précédemment.

### L'étude de cas : le tri fusion

Pour notre discussion, nous utiliserons un algorithme de tri fusion comme spécimen. Jetez un coup d'œil au diagramme ci-dessous. Si vous pouvez compter et assembler des puzzles, alors vous pouvez probablement comprendre comment il fonctionne en quelques minutes.

![Image](https://cdn-media-1.freecodecamp.org/images/ZcTwK7oDpCLBjTjYrP-3ZlnUCSWe7EkYj7Zb)
_Par Swfung8 — Travail personnel, CC BY-SA 3.0, [https://commons.wikimedia.org/w/index.php?curid=14961648](https://commons.wikimedia.org/w/index.php?curid=14961648" rel="noopener" target="_blank" title=")_

Les étapes clés de la production d'un tri fusion sont peu nombreuses et simples. En fait, je peux l'expliquer en utilisant les blocs de nombres de ma fille (il est utile de suivre ces étapes en revenant au diagramme animé pour référence) :

* Tout d'abord, nous devons continuer à subdiviser une liste de nombres (ou de lettres, ou de tout type de valeurs triables) par moitié jusqu'à ce que nous obtenions de nombreuses listes à un seul élément. Une liste avec un seul élément est techniquement triée. Cela s'appelle trivialement trié.
* Ensuite, nous créons une nouvelle liste vide dans laquelle nous pouvons commencer à réorganiser les éléments et les placer un par un selon celui qui est inférieur/plus petit que l'autre.
* Ensuite, nous devons « fusionner » chaque paire de listes ensemble, inversant effectivement les étapes de subdivision. Mais cette fois, à chaque étape, nous devons nous assurer que l'élément le plus petit de la paire en question est placé en premier dans la liste vide.

Pour l'argument, nous allons essayer de cartographier les processus ci-dessus en faisant de chacun une sous-routine (fonction en langage normal). La partie la plus substantielle de cet algorithme est la fusion, alors commençons par là.

```ps
def merge(a, b):
    out = []

    while (len(a) > 0 and len(b) > 0): 
        if (a[0] <= b[0]):
            out.append(a[0])
            del a[0]
        else:
            out.append(b[0])
            del b[0]

    while (len(a) > 0):
        out.append(a[0])
        del a[0]
    while (len(b) > 0):
        out.append(b[0])
        del b[0]

    return out
```

Allez-y et passez du temps à l'examiner. Vous pourriez remarquer qu'avec le code Python impératif, il est conçu pour être prononcé puis compris. Il est très compréhensible en anglais, mais pas en logique.

#### Notre première tentative

Voici une tentative (que vous pourriez éventuellement utiliser lors d'une session de whiteboarding) :

Pour fusionner les listes `a` et `b`, nous devons d'abord créer une liste vide nommée `out` pour plus de clarté (car en Python, nous ne pouvons pas être sûrs qu'elle sera vraiment « out » à la fin). Ensuite, tant que (ou pendant que) les deux listes ne sont pas vides, nous continuerons à mettre la tête des deux listes en compétition. Celle qui est inférieure ou égale à l'adversaire gagne et entre dans `out` en premier. Le perdant devra rester et attendre là pour le nouveau concurrent. Les revanches continuent jusqu'à ce que la première boucle `while` se termine.

Maintenant, à un moment donné, soit `a` soit `b` sera vide, laissant l'autre avec un ou plusieurs éléments en suspens. Sans aucun concurrent restant dans l'autre liste, les deux boucles `while` s'assurent de faire passer ces pauvres éléments dans `out` afin que les deux listes soient épuisées. Ensuite, lorsque tout est terminé, nous retournons `out`.

Et voici les cas de test pour merge :

```py
assert(merge([1], [2]) == [1, 2])
assert(merge([2], [1]) == [1, 2])
assert(merge([4, 1], [3, 0, 2]) == [0, 1, 2, 3, 4])
```

J'espère qu'à ce stade, il est clair pour vous pourquoi nous obtenons le résultat dans le dernier cas. Si ce n'est pas le cas, essayez de dessiner sur un tableau blanc ou une feuille de papier et simulez l'explication.

#### Diviser pour mieux régner

Maintenant, nous allons continuer avec la partie subdivision. Ce processus est également connu sous le nom de partitionnement ou, en langage quelque peu plus grand, [Diviser pour mieux régner](https://fr.wikipedia.org/wiki/Diviser_pour_mieux_regner) (au fait, [la définition en politique est tout aussi intéressante](https://fr.wikipedia.org/wiki/Diviser_pour_mieux_regner)).

![Image](https://cdn-media-1.freecodecamp.org/images/7r1BOCtjx7Z261gFldhvdk6sxqLYy0xGpe57)
_Médaille d'or de Philippe II de Macédoine, à qui l'on attribue la maxime diviser pour mieux régner. Bibliothèque nationale de France, Paris_

En gros, si quelque chose est difficile à conquérir ou à comprendre, vous devriez le décomposer jusqu'à ce qu'il devienne plus petit et plus facile à comprendre. Faites cela jusqu'à ce que les parties soient indécomposables et répétez le processus avec le reste.

```py
def half(arr):
    mid = len(arr) / 2
    return arr[:mid], arr[mid:]
```

Ce que fait la routine `half` est de trouver l'index du milieu, de diviser la liste d'entrée en sous-listes approximativement égales et de retourner les deux comme une paire. Elle n'a besoin de le faire qu'une fois, puisque la fonction parente l'appellera éventuellement de manière récursive.

Puisque nous avons les morceaux, nous devons maintenant les assembler dans un schéma cohérent. C'est là que les choses se compliquent, car des récursions sont impliquées.

Avant d'entrer dans plus de code, laissez-moi expliquer pourquoi les récursions et les langages de programmation impératifs comme Python ne s'emboîtent pas si bien. Je n'aborderai pas le sujet de l'optimisation, car cela ne concerne pas la discussion d'aujourd'hui et n'est pas aussi intéressant.

Une ironie distincte ici est que, même dans un langage avec des boucles itératives comme Python, il ne peut pas entièrement éviter la récursion (il pourrait s'en passer sans récursion, mais je suis sûr que cela le rendrait encore plus bizarre). La récursion est un territoire où les constructions itératives, telles que les boucles for et while, deviennent totalement inutiles.

De plus, la récursion n'est pas naturelle en Python. Elle ne semble pas naturelle et transparente, mais plutôt assez mal cuite comme sa lambda. Une tentative de voix sur les récursions en Python serait comme, « puis nous faisons cela de manière récursive et prions simplement pour que tout fonctionne et atteigne le cas de base à la fin afin qu'il ne plonge pas dans l'obscurité infinie du débordement de pile. » Wow, n'est-ce pas ?

Voici donc la fonction `mergesort` :

```py
def mergesort(arr):

    if (len(arr) <= 1):
        return arr

    left, right = half(arr)
    L = mergesort(left)
    R = mergesort(right)

    return merge(L, R)
```

Apparemment, cela est vraiment propre et facile à lire. Mais il n'est pas clair ce qui se passe après l'appel à `half`, au moins sémantiquement. À cause de cette « non-nativité » à la récursion, les appels récursifs sont très opaques et obstructifs pour les efforts éducatifs.

La seule façon de visualiser ce processus de tri fusion est probablement de suivre les changements dans les sous-listes à chaque étape :

```
input: [0, 3, 1, 3, 2, 6, 5]
A alias pour mergesort / half
B alias pour merge

## subdivision par moitié ...

                 A([0, 3, 1, 3, 2, 6, 5])
              A([0, 3, 1])    A([3, 2, 6, 5])
          A([0])  A([3, 1])  A([3, 2])   A([6, 5])
    A([]) A([0]) A([3])  A([1]) A([3]) A([2]) A([6]) A([5]) 

## cas de base atteint, début de la fusion ...

       B([], [0]) B([3], [1]) B([3], [2]) B([6], [5])
          B([0], [1, 3])         B([2, 3], [5, 6])
                B([0, 1, 3], [2, 3, 5, 6])
                 B([0, 1, 2, 3, 3, 5, 6])

output: [0, 1, 2, 3, 3, 5, 6]
```

Sur une note asymptotique, diviser et conquérir entraîne presque toujours un temps d'exécution logarithmique. Lorsque vous continuez à diviser une collection en `N` sous-collections, qu'elle contienne 10 ou 100 000 000 éléments, le nombre d'étapes prises dans le dernier cas augmente au taux de log base `N`.

Par exemple, il faut environ 3 étapes pour continuer à diviser 10 par 2 jusqu'à ce qu'il soit aussi proche de 1 que possible (ou exactement 3 étapes pour atteindre 1 en division entière). Mais il ne faut qu'environ 26 étapes pour faire de même et diviser 100 000 000 par 2 jusqu'à atteindre 1. Ce fait peut être exprimé comme suit :

```
2^3.321928 = 10
2^6.643856 = 100

...

2^26.575425 = 100000000

ou 

log base 2 de 100000000 = 26.575425
```

Le point à retenir ici est que nous avons dû visualiser les processus récursifs afin de comprendre le fonctionnement interne de l'algorithme — même s'il semblait si trivial dans le diagramme animé.

**Pourquoi y a-t-il une division entre les processus conceptuels de l'algorithme lui-même et le code qui instructe l'ordinateur à calculer de tels processus ?**

C'est parce qu'en un sens, en utilisant des langages impératifs, nous sommes en fait encore mentalement asservis par les machines.

![Image](https://cdn-media-1.freecodecamp.org/images/NEuX4NWEDEEpa2TikKqjT2ABx5kj8tPZk8A5)
_Pas tout à fait comme ça, mais vous voyez le point._

### Plonger plus profondément dans le code

> « Il y a une différence entre connaître le chemin et marcher sur le chemin. »
> – [Morpheus, The Matrix](https://www.goodreads.com/author/show/7392901.Morpheus_The_Matrix)

La programmation est difficile, nous le savons tous. Et comprendre la programmation de manière vraiment approfondie est encore plus difficile pour votre âme (et votre carrière). Mais je dirais que, comme l'a dit Morpheus, parfois marcher sur le chemin est tout ce qui compte. Pouvoir voir clairement est l'une des choses les plus gratifiantes en programmation.

En programmation fonctionnelle, le programmeur (vous) obtient le siège avant pour voir comment les données changent de manière récursive. Cela signifie que vous avez la capacité de décider comment les données d'une certaine forme doivent être transformées en données d'une autre forme basée sur l'instantané de leur apparence. Cela n'est pas différent de la manière dont nous avons visualisé le processus de tri fusion. Laissez-moi vous donner un aperçu.

Disons que vous voulez créer un cas de base en Python. Dans celui-ci, vous voulez retourner la liste en question lorsqu'elle n'a qu'un seul élément, et une liste vide lorsqu'il y a deux éléments. Vous devriez donc écrire quelque chose comme ceci :

```py
if (len(arr) == 1):
    return arr
elif (len(arr) == 2):
    return []
```

Ou pour empirer les choses mais les rendre plus intéressantes, vous pourriez essayer d'accéder au premier élément par l'index 0 et au deuxième élément par l'index 1 et vous préparer à gérer l'exception `IndexError`.

Dans un langage fonctionnel comme Erlang — que j'utiliserai dans cet article pour son système de types dynamique comme Python — vous feriez plus ou moins quelque chose comme ceci :

```
case Arr of
  [_] -> Arr;
  [_,_] -> []
end.
```

Cela vous donne une vue plus claire de l'état des données. Une fois qu'il est suffisamment entraîné, il nécessite beaucoup moins de puissance cognitive pour lire et comprendre ce que fait le code que `len(arr)`. Gardez simplement à l'esprit : un programmeur qui ne parle pas anglais pourrait demander, « qu'est-ce que len ? » Ensuite, vous êtes distrait par le sens littéral de la fonction au lieu de la valeur de cette expression.

Cependant, cela a un prix : vous n'avez pas le luxe d'une construction de boucle. Un langage comme Erlang est natif en récursion. Presque tous les programmes Erlang significatifs utiliseront des appels de fonctions récursifs rigoureux. Et c'est pourquoi il est mappé plus étroitement aux concepts algorithmiques qui consistent généralement en récursion.

Essayons de retracer nos étapes dans la production de mergesort, mais cette fois en Erlang, en commençant par la fonction `merge`.

```
merge([], [], Acc) -> Acc;
merge([], [H | T], Acc) -> [H | merge([], T, Acc)];
merge([H | T], [], Acc) -> [H | merge(T, [], Acc)];
merge([Ha | Ta], [Hb | Tb], Acc) ->
  case Ha =< Hb of
    true  -> [Ha | merge(Ta, [Hb | Tb], Acc)];
    false -> [Hb | merge([Ha | Ta], Tb, Acc)]
  end.
```

Quelle abomination ! Définitivement pas une amélioration en termes de lisibilité, pensez-vous. Oui, Erlang n'aura probablement pas de prix pour la beauté du langage. En fait, de nombreux langages fonctionnels peuvent sembler du charabia aux yeux non entraînés.

Mais donnons-lui une chance. Nous allons passer par chaque étape comme nous l'avons fait auparavant, et peut-être qu'à la fin, certains d'entre nous verront la lumière. Mais avant de continuer, pour ceux qui ne sont pas familiers avec Erlang, voici quelques points à noter :

* Chaque bloc de `merge` est considéré comme une clause de fonction de la même fonction. Ils sont séparés par `;`. Lorsqu'une expression se termine en Erlang, elle se termine par un point (`.`). Il est courant de séparer une fonction en plusieurs clauses pour différents cas. Par exemple, la clause `merge([], [], Acc) -> Acc;` mappe le cas où les deux premiers arguments sont des listes vides à la valeur du dernier argument.
* L'arité joue un rôle important en Erlang. Deux fonctions avec le même nom et la même arité sont considérées comme la même fonction. Sinon, elles ne le sont pas. Par exemple, `merge/1` et `merge/3` (comment les fonctions et leur arité sont adressées en Erlang) sont deux fonctions différentes.
* Erlang utilise un [pattern matching](https://en.wikipedia.org/wiki/Pattern_matching) rigoureux (ceci est utilisé dans de nombreux autres langages fonctionnels, mais surtout en Erlang). Puisque les valeurs dans les langages fonctionnels purs sont immuables, il est sûr de lier des variables dans une forme de données similaire à celle existante avec une forme correspondante. Voici un exemple trivial :

```
{X, Y} = {0.5, 0.13}.
X.  %% 0.5
Y.  %% 0.13

[A, B, C | _] = [alice, jane, bob, kent, ollie].
[A, B, C].  %% [alice, jane, bob]
```

* Notez que nous parlerons rarement de retourner des valeurs lorsque nous travaillerons avec des fonctions Erlang, car elles ne « retournent » rien en soi. Elles mappent une valeur d'entrée à une nouvelle valeur. Ce n'est pas la même chose que de la sortir ou de la retourner de la fonction. L'application de la fonction elle-même **est** la valeur. Par exemple, si `Add(N1, N2) -> N1 + N2.`, alors `Add(1, 2)` est 3. Il n'y a aucun moyen pour qu'elle retourne autre chose que 3, donc nous pouvons dire qu'elle est 3. C'est pourquoi vous pourriez facilement faire `add_one = Add(1)` et ensuite `add_one(2)` est `3`, `add_one(5)` est 6, et ainsi de suite.

Pour ceux qui sont intéressés, voir [transparence référentielle](https://stackoverflow.com/questions/210835/what-is-referential-transparency). Pour rendre ce point plus clair et au risque de redondance, voici quelque chose à méditer :

> lorsque `f(x)` est une fonction avec une arité, et le mappage est `f(x) -> x`, alors il est concluant que `f(1) -> 1`, `f(2) -> 2`, `f(3.1416) -> 3.1416`, et `f("foo") -> "foo"`.
>
> Cela peut sembler une évidence, mais dans une fonction impure, il n'y a pas de mappage garanti :
>
> `a = 1`
> `def add_to_a(b):`
>  `return b + a`
>
> Maintenant, `a` pourrait bien être n'importe quoi avant que `add_to_a` ne soit appelé. Ainsi, en Python, vous pourriez écrire une version pure de ce qui précède comme :
>
> `def add(a, b):`
>  `return a + b`
> ou `lambda a, b: a + b`.

Maintenant, il est temps de plonger dans l'inconnu.

![Image](https://cdn-media-1.freecodecamp.org/images/Vg7C4II-2IY3Jx58NEN-nzHtSmVS9FwmWk6L)
_C'est ce que Frank O. Gehry a dit._

#### Avancer avec Erlang

```
merge([], [], Acc) -> Acc;
```

La première clause de la fonction `merge/3` signifie que lorsque les deux premiers arguments sont des listes vides, mappez l'expression entière à (ou « retournez ») le troisième argument `Acc`.

De manière intéressante, dans une fonction pure, il n'y a aucun moyen de conserver et de muter l'état en dehors d'elle-même. Nous ne pouvons travailler qu'avec ce que nous avons reçu en entrées dans la fonction, le transformer, puis alimenter le nouvel état dans l'argument d'une autre fonction (le plus souvent, il s'agit d'un autre appel récursif à elle-même).

Ici, `Acc` signifie accumulateur, que vous pouvez considérer comme un conteneur d'état. Dans le cas de `merge/3`, `Acc` est une liste qui commence vide. Mais à mesure que les appels récursifs avancent, il accumule des valeurs des deux premières listes en utilisant la logique que nous programmons (dont nous parlerons ensuite).

Ce processus d'épuisement d'une valeur pour en construire une autre est collectivement connu sous le nom de réduction. Par conséquent, dans ce cas, nous pouvons conclure que puisque les deux premières listes sont épuisées (vides), `Acc` doit être mûr pour être récupéré.

```
merge([], [H | T], Acc) -> [H | merge([], T, Acc)];
```

La deuxième clause correspond au cas où la première liste est déjà vide, mais il reste au moins un élément dans la deuxième liste. `[H | T]` signifie qu'une liste a un élément de tête `H` qui [se cons sur une autre liste](https://en.wikipedia.org/wiki/Cons#Lists) `T`. En Erlang, une liste est une liste chaînée, et la tête a un pointeur vers le reste de la liste. Ainsi, une liste de `[1, 2, 3, 4]` peut être considérée comme :

```
%% match A, B, C, et D à 1, 2, 3, et 4, respectivement

[A | [B | [C | [D | []]]]] = [1, 2, 3, 4].
```

Dans ce cas, comme vous pouvez le voir dans l'exemple de conning, `T` peut simplement être une liste de queue vide. Donc dans ce deuxième cas, nous le mappons à une valeur d'une nouvelle liste dans laquelle l'élément `H` de la deuxième liste est consé sur le résultat récursif de l'appel à `merge/3` lorsque `T` est le deuxième argument.

```
merge([H | T], [], Acc) -> [H | merge(T, [], Acc)];
```

Le troisième cas est simplement le revers du deuxième cas. Il correspond au cas où la première liste n'est pas vide, mais la deuxième l'est. Cette clause mappe à une valeur dans un motif similaire, sauf qu'elle appelle `merge/3` avec la queue de la première liste comme premier argument et garde la deuxième liste vide.

```
merge([Ha | Ta], [Hb | Tb], Acc) ->
  case Ha =< Hb of
    true  -> [Ha | merge(Ta, [Hb | Tb], Acc)];
    false -> [Hb | merge([Ha | Ta], Tb, Acc)]
  end.
```

Commençons par l'essentiel de `merge/3`. Cette clause correspond au cas où les premier et deuxième arguments sont des listes non vides. Dans ce cas, nous entrons dans une clause `case ... of` (équivalente à un switch case dans d'autres langages) pour tester si l'élément de tête de la première liste (`Ha`) est inférieur ou égal à l'élément de tête de la deuxième liste (`Hb`).

Si c'est vrai, nous consons `Ha` sur la liste résultante du prochain appel récursif à merge avec la liste de queue de la première liste précédente (`Ta`) comme nouveau premier argument. Nous gardons les deuxième et troisième arguments identiques.

Ces clauses constituent une seule fonction, `merge/3`. Vous pouvez imaginer qu'elle aurait pu être une seule clause de fonction. Nous aurions pu utiliser un cas complexe ... of et/ou une conditionnelle si plus un pattern-matching pour éliminer chaque cas et le mapper au bon résultat. Cela aurait rendu les choses plus chaotiques, alors que vous pouvez facilement lire chaque cas que la fonction correspond assez bien sur des lignes séparées.

Cependant, les choses se sont un peu compliquées pour l'opération de subdivision, qui nécessite deux fonctions : `half/1` et `half/3`.

```
half([]) -> {[], []};
half([X]) -> {[X], []};
half([X,Y]) -> {[X], [Y]};
half(L) ->
  Len = length(L),
  half(L, {0, Len}, {[], []}).

half([], _, {Acc1, Acc2}) ->
  {lists:reverse(Acc1), lists:reverse(Acc2)};
half([X], _, {Acc1, Acc2}) ->
  {lists:reverse(Acc1), lists:reverse([X | Acc2])};
half([H|T], {Cnt, Len}, {Acc1, Acc2}) ->
  case Cnt >= (Len div 2) of
      true -> half(T, {Cnt + 1, Len}, {Acc1, [H|Acc2]});
      false -> half(T, {Cnt + 1, Len}, {[H|Acc1], Acc2})
  end.
```

C'est là que vous allez manquer Python et sa nature destructive. Dans un langage fonctionnel pur, les listes sont des listes chaînées. Lorsque vous travaillez avec elles, il n'y a pas de retour en arrière. Il n'y a pas de logique qui dit « je veux diviser une liste en deux, donc je vais obtenir l'index du milieu, et la découper en deux portions _gauche_ et _droite_. »

Si votre esprit est fixé à travailler avec des listes chaînées, vous êtes plus dans l'idée de « je ne peux aller que vers l'avant dans la liste, en travaillant avec quelques éléments à la fois. J'ai besoin de créer deux listes vides et de compter combien d'éléments j'ai récupérés de la liste source et mis dans la première afin de savoir quand il est temps de passer à un autre seau. Tout ce qui précède doit être passé en arguments dans les appels récursifs. » Ouf !

En d'autres termes, couper une liste en deux peut être comparé à couper un bloc de fromage avec un couteau au milieu. D'un autre côté, une comparaison fonctionnelle pour le faire est comme verser du café dans deux tasses de manière égale — vous devez simplement savoir quand il est temps d'arrêter de verser dans la première et de passer à la deuxième.

La fonction `half/1`, bien qu'elle ne soit pas vraiment nécessaire, est là pour la commodité.

```
half([]) -> {[], []};
half([X]) -> {[X], []};
half([X,Y]) -> {[X], [Y]};
half(L) ->
  Len = length(L),
  half(L, {0, Len}, {[], []}).
```

À ce stade, vous devriez comprendre ce que fait chaque clause de fonction Erlang. Les nouvelles paires de crochets ici représentent des tuples en Erlang. Oui, nous retournons une paire de valeurs gauche et droite, comme dans la version Python. La fonction `half/1` est là pour gérer les cas de base simples et explicites qui ne justifient pas la transmission d'autres arguments.

Cependant, notez le dernier cas lorsque l'argument a une liste avec plus de deux éléments. (Note : ceux avec moins ou égal à deux éléments sont déjà gérés par les trois premières clauses.) Il calcule simplement ce qui suit :

* la longueur de la liste `L` et appelle `half/3` avec `L` comme premier argument
* une paire de variables de compteur et la longueur de la liste, qui sera utilisée pour signaler le passage de la liste une à la liste deux
* et bien sûr, une paire de listes vides pour remplir les éléments de `L`.

```
half([], _, {Acc1, Acc2}) ->
  {lists:reverse(Acc1), lists:reverse(Acc2)};
```

`half/3` semble désordonné, mais seulement pour les yeux non entraînés. La première clause correspond à un motif lorsque la liste source est épuisée. Dans ce cas, la deuxième paire de compteur et de longueur n'aura pas d'importance puisque c'est déjà la fin. Nous savons simplement que `Acc1` et `Acc2` sont mûrs pour être récupérés. Mais attendez, pourquoi inverser les deux ?

Ajouter un élément à une liste chaînée est une opération très lente. Elle s'exécute en O(N) fois pour chaque ajout, car elle doit créer une nouvelle liste, copier l'existante sur celle-ci, et créer un pointeur vers le nouvel élément et l'assigner au dernier élément. C'est comme refaire toute la liste. Couplez cela avec des récursions et vous êtes voué au désastre.

La seule bonne façon d'ajouter quelque chose à une liste chaînée est de le préfixer à la tête. Ensuite, tout ce qu'elle doit faire est de créer une mémoire pour cette nouvelle valeur et de lui donner une référence à la tête de la liste chaînée. Une simple opération O(1). Donc même si nous pourrions concaténer des listes en utilisant `++` comme `[1, 2, 3] ++ [4]`, nous voulons rarement le faire de cette manière, surtout avec des récursions.

La technique ici consiste à inverser d'abord la liste source, puis à ajouter un élément comme `[4 | [3, 2, 1]]`, et à les inverser à nouveau pour obtenir le bon résultat. Cela peut sembler terrible, mais inverser une liste et la réinverser est une opération O(2N), qui est O(N). Mais entre les deux, ajouter des éléments à la liste ne prend que O(1), donc cela ne coûte pratiquement aucun temps d'exécution supplémentaire.

```
half([H|T], {Cnt, Len}, {Acc1, Acc2}) ->
  case Cnt >= (Len div 2) of
      true -> half(T, {Cnt + 1, Len}, {Acc1, [H|Acc2]});
      false -> half(T, {Cnt + 1, Len}, {[H|Acc1], Acc2})
  end.
```

Revenons à `half/3`. La deuxième clause, l'essentiel de la fonction, fait exactement la même chose que la métaphore du versement de café que nous avons visitée plus tôt. Puisque la liste source émet toujours des données, nous voulons garder une trace du temps que nous avons passé à verser des valeurs de celle-ci dans la première tasse de café `Acc1`.

Rappelez-vous que dans la dernière clause de `half/1`, nous avons calculé la longueur de la liste originale ? C'est la variable Len ici, et elle reste la même tout au long des appels. Elle est là pour que nous puissions comparer le compteur `Cnt` à celui divisé par 2 pour voir si nous sommes arrivés au milieu de la liste source et si nous devons passer au remplissage de `Acc2`. C'est là que la clause `case ... of` intervient.

Maintenant, mettons-les tous ensemble dans `mergesort/1`. Cela devrait être aussi simple que la version Python, et peut être facilement comparé.

```
mergesort([A]) -> [A];
mergesort([A, B]) ->
  case A =< B of
      true -> [A,B];
      false -> [B,A]
  end;
mergesort(L) ->
  {Left, Right} = half(L),
  merge(mergesort(Left), mergesort(Right), []).
```

#### C'est tout !

À ce stade, soit vous pensez que c'est une manière nouvelle et utile de penser à un problème, soit vous la trouvez simplement déroutante. Mais j'espère que vous avez tiré quelque chose de cette approche de programmation qui aide à éclairer sous un nouveau jour la manière dont nous pouvons penser aux algorithmes.

#### **Mise à jour**

L'implémentation Python de la fonction `merge` n'est pas efficace car dans chaque boucle `while`, le premier élément de la liste est supprimé. Bien que ce soit un motif courant dans les langages fonctionnels comme Erlang, en Python, il est très coûteux de supprimer ou d'insérer un élément n'importe où sauf à la dernière position, car contrairement à une liste en Erlang qui est une liste chaînée très efficace pour supprimer ou ajouter un élément à la tête de la liste, la liste Python se comporte comme un tableau qui doit repositionner tous les autres éléments lorsqu'un est supprimé ou ajouté, entraînant un temps d'exécution O(n).

La meilleure façon est de sacrifier un peu d'espace pour définir une variable de compteur pour chaque liste qui peut être incrémentée et utilisée pour accéder à l'élément actuel de la liste source sans avoir besoin de supprimer l'élément le plus haut du tout.

```
def merge(a, b):
    out = []

    ai = 0
    bi = 0

    while (ai <= len(a) - 1 and bi <= len(b) - 1): 
        if (a[ai] <= b[bi]):
            out.append(a[ai])
            ai += 1
        else:
            out.append(b[bi])            
            bi += 1

    while (ai <= len(a) - 1):
        out.append(a[ai])
        ai += 1

    while (bi <= len(b) - 1):
        out.append(b[bi])
        bi += 1

    return out
```