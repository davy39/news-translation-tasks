---
title: Comment implémenter une table de hachage simple en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-26T15:19:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-simple-hash-table-in-javascript-cb3b9c1f2997
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3jxEppESh9LLK14YMQ-ocA.png
tags:
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment implémenter une table de hachage simple en JavaScript
seo_desc: 'By Alex Nadalin

  How beautiful is {}?

  It lets you store values by key, and retrieve them in a very cost-efficient manner
  (O(1), more on this later).

  In this post I want to implement a very basic hash table, and have a look at its
  inner workings to exp...'
---

Par Alex Nadalin

Qu'est-ce que `{}` est beau ?

Il vous permet de stocker des valeurs par clé et de les récupérer de manière très économique (`O(1)`, plus d'informations à ce sujet plus tard).

Dans cet article, je souhaite implémenter une table de hachage très basique et examiner son fonctionnement interne pour expliquer l'une des idées les plus ingénieuses en informatique.

### Le problème

Imaginez que vous construisez un nouveau langage de programmation : vous commencez par avoir des types assez simples (chaînes de caractères, entiers, flottants, ...) puis vous passez à l'implémentation de structures de données très basiques. D'abord, vous inventez le tableau (`[]`), puis vient la table de hachage (également connue sous le nom de dictionnaire, tableau associatif, hashmap, map, et... la liste est longue).

Vous vous êtes déjà demandé comment ils fonctionnent ? Comment ils sont si rapides ?

Eh bien, disons que JavaScript n'avait pas `{}` ou `new Map()`, et implémentons notre propre `DumbMap` !

### Une note sur la complexité

Avant de commencer, nous devons comprendre comment fonctionne la complexité d'une fonction : Wikipedia a un bon rappel sur la [théorie de la complexité computationnelle](https://en.wikipedia.org/wiki/Computational_complexity_theory), mais j'ajouterai une brève explication pour les paresseux.

La complexité mesure le nombre d'étapes requises par notre fonction — moins il y a d'étapes, plus l'exécution est rapide (également connue sous le nom de "temps d'exécution").

Examinons le snippet suivant :

```
function fn(n, m) {  return n * m}
```

La complexité computationnelle (désormais simplement "complexité") de `fn` est `O(1)`, ce qui signifie qu'elle est constante (vous pouvez lire `O(1)` comme "le coût est un") : peu importe les arguments que vous passez, la plateforme qui exécute ce code n'a qu'à effectuer une opération (multiplier `n` par `m`). Encore une fois, puisque c'est une opération, le coût est appelé `O(1)`.

La complexité est mesurée en supposant que les arguments de votre fonction peuvent avoir des valeurs très grandes. Regardons cet exemple :

```
function fn(n, m) {  let s = 0

  for (i = 0; i < 3; i++) {    s += n * m  }

  return s}
```

Vous penseriez que sa complexité est `O(3)`, n'est-ce pas ?

Encore une fois, puisque la complexité est mesurée dans le contexte d'arguments très grands, nous avons tendance à "ignorer" les constantes et à considérer `O(3)` comme étant le même que `O(1)`. Donc, même dans ce cas, nous dirions que la complexité de `fn` est `O(1)`. Peu importe la valeur de `n` et `m`, vous finissez toujours par faire trois opérations — ce qui, encore une fois, est un coût constant (donc `O(1)`).

Maintenant, cet exemple est un peu différent :

```
function fn(n, m) {  let s = []

  for (i = 0; i < n; i++) {    s.push(m)  }

  return s}
```

Comme vous le voyez, nous bouclons autant de fois que la valeur de `n`, qui pourrait être en millions. Dans ce cas, nous définissons la complexité de cette fonction comme `O(n)`, car vous devrez faire autant d'opérations que la valeur de l'un de vos arguments.

D'autres exemples ?

```
function fn(n, m) {  let s = []

  for (i = 0; i < 2 * n; i++) {    s.push(m)  }

  return s}
```

Cet exemple boucle `2 * n` fois, ce qui signifie que la complexité devrait être `O(2n)`. Puisque nous avons mentionné que les constantes sont "ignorées" lors du calcul de la complexité d'une fonction, cet exemple est également classé comme `O(n)`.

Un de plus ?

```
function fn(n, m) {  let s = []

  for (i = 0; i < n; i++) {    for (i = 0; i < n; i++) {      s.push(m)    }  }

  return s}
```

Ici, nous bouclons sur `n` et nous bouclons à nouveau à l'intérieur de la boucle principale, ce qui signifie que la complexité est "carrée" (`n * n`) : si `n` est 2, nous exécuterons `s.push(m)` 4 fois, si `n` est 3 nous l'exécuterons 9 fois, et ainsi de suite.

Dans ce cas, la complexité de la fonction est appelée `O(n²)`.

Un dernier exemple ?

```
function fn(n, m) {  let s = []

  for (i = 0; i < n; i++) {    s.push(n)  }

  for (i = 0; i < m; i++) {    s.push(m)  }

  return s}
```

Dans ce cas, nous n'avons pas de boucles imbriquées, mais nous bouclons deux fois sur deux arguments différents : la complexité est définie comme `O(n+m)`. Très clair.

Maintenant que vous venez d'avoir une brève introduction (ou un rappel) sur la complexité, il est très facile de comprendre qu'une fonction avec une complexité `O(1)` va performer beaucoup mieux qu'une avec `O(n)`.

Les tables de hachage ont une complexité `O(1)` : en termes simples, elles sont **super rapides**. Continuons.

_(Je mens un peu sur le fait que les tables de hachage ont toujours une complexité `O(1)`, mais continuez à lire ;))_

### Construisons une table de hachage (simple)

Notre table de hachage a 2 méthodes simples — `set(x, y)` et `get(x)`. Commençons à écrire du code :

Et implémentons une manière très simple et inefficace de stocker ces paires clé-valeur et de les récupérer plus tard. Nous commençons d'abord par les stocker dans un tableau interne (rappelons-nous, nous ne pouvons pas utiliser `{}` puisque nous implémentons `{}` — l'esprit soufflé !) :

Ensuite, il s'agit simplement de récupérer le bon élément de la liste :

Notre exemple complet :

Notre `DumbMap` est incroyable ! Il fonctionne dès le départ, mais comment va-t-il performer lorsque nous ajouterons une grande quantité de paires clé-valeur ?

Essayons un simple benchmark. Nous allons d'abord essayer de trouver un élément non existant dans une table de hachage avec très peu d'éléments, puis essayer la même chose dans une table avec une grande quantité d'éléments :

Les résultats ? Pas très encourageants :

```
avec très peu d'enregistrements dans la map : 0.118msavec beaucoup d'enregistrements dans la map : 14.412ms
```

Dans notre implémentation, nous devons parcourir tous les éléments à l'intérieur de `this.list` afin de trouver celui avec la clé correspondante. Le coût est `O(n)`, et c'est assez terrible.

### Rendre cela plus rapide

Nous devons trouver un moyen d'éviter de parcourir notre liste : il est temps de remettre _hash_ dans la _table de hachage_.

Vous vous êtes déjà demandé pourquoi cette structure de données est appelée une **table de hachage** ? C'est parce qu'une fonction de hachage est utilisée sur les clés que vous définissez et récupérez. Nous utiliserons cette fonction pour transformer notre clé en un entier `i`, et stocker notre valeur à l'index `i` de notre liste interne. Puisque l'accès à un élément, par son index, à partir d'une liste a un coût constant (`O(1)`), alors la table de hachage aura également un coût de `O(1)`.

Essayons cela :

Ici, nous utilisons le module [string-hash](https://www.npmjs.com/package/string-hash), qui convertit simplement une chaîne en un hachage numérique. Nous l'utilisons pour stocker et récupérer des éléments à l'index `hash(key)` de notre liste. Les résultats ?

```
avec beaucoup d'enregistrements dans la map : 0.013ms
```

W — O — W. C'est de cela que je parle !

Nous n'avons pas à parcourir tous les éléments de la liste, et la récupération des éléments de `DumbMap` est super rapide !

Permettez-moi de mettre cela aussi simplement que possible : **le hachage est ce qui rend les tables de hachage extrêmement efficaces**. Pas de magie. Rien de plus. Nada. Juste une idée simple, intelligente et ingénieuse.

### Le coût de choisir la bonne fonction de hachage

Bien sûr, **choisir une fonction de hachage rapide est très important.** Si notre `hash(key)` s'exécute en quelques secondes, notre fonction sera assez lente indépendamment de sa complexité.

En même temps, **il est très important de s'assurer que notre fonction de hachage ne produit pas beaucoup de collisions**, car elles seraient préjudiciables à la complexité de notre table de hachage.

Confus ? Examinons de plus près les collisions.

### Collisions

Vous pourriez penser « Ah, une bonne fonction de hachage ne génère jamais de collisions ! » : eh bien, revenez dans le monde réel et réfléchissez à nouveau. [Google a réussi à produire des collisions pour l'algorithme de hachage SHA-1](https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html), et ce n'est qu'une question de temps, ou de puissance de calcul, avant qu'une fonction de hachage ne craque et ne retourne le même hachage pour 2 entrées différentes. Supposez toujours que votre fonction de hachage génère des collisions, et implémentez la bonne défense contre de tels cas.

En l'occurrence, essayons d'utiliser une fonction `hash()` qui génère beaucoup de collisions :

Cette fonction utilise un tableau de 10 éléments pour stocker les valeurs, ce qui signifie que les éléments sont susceptibles d'être remplacés — un bug désagréable dans notre `DumbMap` :

Afin de résoudre le problème, nous pouvons simplement stocker plusieurs paires clé-valeur au même index. Amendons donc notre table de hachage :

Comme vous pouvez le remarquer, ici nous revenons à notre implémentation originale : stocker une liste de paires clé-valeur et parcourir chacune d'elles. Cela va être assez lent lorsqu'il y a beaucoup de collisions pour un index particulier de la liste.

Faisons un benchmark de cela en utilisant notre propre fonction `hash()` qui génère des index de 1 à 10 :

```
avec beaucoup d'enregistrements dans la map : 11.919ms
```

et en utilisant la fonction de hachage de `string-hash`, qui génère des index aléatoires :

```
avec beaucoup d'enregistrements dans la map : 0.014ms
```

Waouh ! Voici le coût de choisir la bonne fonction de hachage — assez rapide pour ne pas ralentir notre exécution par elle-même, et assez bonne pour ne pas produire beaucoup de collisions.

### Généralement O(1)

Vous vous souvenez de mes mots ?

> Les tables de hachage ont une complexité `O(1)`

Eh bien, j'ai menti : la complexité d'une table de hachage dépend de la fonction de hachage que vous choisissez. Plus vous générez de collisions, plus la complexité tend vers `O(n)`.

Une fonction de hachage telle que :

```
function hash(key) {  return 0}
```

signifierait que notre table de hachage a une complexité de `O(n)`.

C'est pourquoi, en général, la complexité computationnelle a trois mesures : les meilleurs, moyens et pires scénarios. Les tables de hachage ont une complexité `O(1)` dans les meilleurs et moyens scénarios, mais tombent à `O(n)` dans leur pire scénario.

Rappelez-vous : **une bonne fonction de hachage est la clé d'une table de hachage efficace** — rien de plus, rien de moins.

### Plus sur les collisions...

La technique que nous avons utilisée pour corriger `DumbMap` en cas de collisions est appelée [chaînage séparé](https://xlinux.nist.gov/dads/HTML/separateChaining.html) : nous stockons toutes les paires clé-valeur qui génèrent des collisions dans une liste et nous parcourons cette liste.

Une autre technique populaire est l'[adressage ouvert](https://en.wikipedia.org/wiki/Open_addressing) :

* à chaque index de notre liste, nous stockons **une et une seule paire clé-valeur**
* lorsque nous essayons de stocker une paire à l'index `x`, s'il y a déjà une paire clé-valeur, nous essayons de stocker notre nouvelle paire à `x + 1`
* si `x + 1` est pris, nous essayons `x + 2` et ainsi de suite...
* lorsque nous récupérons un élément, nous hachons la clé et nous vérifions si l'élément à cette position (`x`) correspond à notre clé
* si ce n'est pas le cas, nous essayons d'accéder à l'élément à la position `x + 1`
* nous répétons jusqu'à ce que nous arrivions à la fin de la liste, ou lorsque nous trouvons un index vide — cela signifie que notre élément n'est pas dans la table de hachage

Intelligent, simple, élégant et [généralement très efficace](http://cseweb.ucsd.edu/~kube/cls/100/Lectures/lec16/lec16-28.html) !

### FAQs (ou TL;DR)

#### Une table de hachage hache-t-elle les valeurs que nous stockons ?

Non, les clés sont hachées afin qu'elles puissent être transformées en un entier `i`, et les clés et les valeurs sont stockées à la position `i` dans une liste.

#### Les fonctions de hachage utilisées par les tables de hachage génèrent-elles des collisions ?

Absolument — donc les tables de hachage sont implémentées avec des [stratégies de défense](https://en.wikipedia.org/wiki/Hash_table#Collision_resolution) pour éviter les bugs désagréables.

#### Les tables de hachage utilisent-elles une liste ou une liste chaînée en interne ?

Cela dépend, [les deux peuvent fonctionner](https://stackoverflow.com/questions/13595767/why-do-hash%20tables-use-a-linked-list-over-an-array-for-the-bucket). Dans nos exemples, nous utilisons le tableau JavaScript (`[]`) qui peut être [redimensionné dynamiquement](https://www.quora.com/Do-arrays-in-JavaScript-grow-dynamically) :

```
> a = []
```

```
> a[3] = 1
```

```
> a[ <3 empty items>, 1 ]
```

#### Pourquoi avez-vous choisi JavaScript pour les exemples ? Les tableaux JS SONT des tables de hachage !

Par exemple :

```
>  a = [][]
```

```
> a["some"] = "thing"'thing'
```

```
> a[ some: 'thing' ]
```

```
> typeof a'object'
```

Je sais, ce JavaScript.

JavaScript est "universel" et probablement le langage le plus facile à comprendre lorsque l'on regarde un exemple de code. JS n'est peut-être pas le meilleur langage, mais j'espère que ces exemples sont assez clairs.

#### Votre exemple est-il une très bonne implémentation d'une table de hachage ? Est-ce vraiment SIMPLE ?

Non, pas du tout.

Jetez un coup d'œil à "[implementing a hash table in JavaScript](http://www.mattzeunert.com/2017/02/01/implementing-a-hash-table-in-javascript.html)" par [Matt Zeunert](http://www.mattzeunert.com/), car cela vous donnera un peu plus de contexte. Il y a beaucoup plus à apprendre, donc je vous suggérerais également de consulter :

* [Cours de Paul Kube sur les tables de hachage](http://cseweb.ucsd.edu/~kube/cls/100/Lectures/lec16/lec16.html)
* [Implémentation de notre propre table de hachage avec chaînage séparé en Java](https://www.geeksforgeeks.org/implementing-our-own-hash-table-with-separate-chaining-in-java/)
* [Algorithmes, 4ème édition — Tables de hachage](https://algs4.cs.princeton.edu/34hash/)
* [Conception d'une table de hachage rapide](http://www.ilikebigbits.com/blog/2016/8/28/designing-a-fast-hash-table)

### En fin de compte...

Les tables de hachage sont une idée très ingénieuse que nous utilisons régulièrement : peu importe que vous créiez un [dictionnaire en Python](https://stackoverflow.com/questions/114830/is-a-python-dictionary-an-example-of-a-hash-table), un [tableau associatif en PHP](https://stackoverflow.com/a/3134315/934439) ou une [Map en JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map). Elles partagent toutes les mêmes concepts et fonctionnent magnifiquement pour nous permettre de stocker et de récupérer des éléments par un identifiant, à un coût (très probablement) constant.

J'espère que vous avez apprécié cet article, et n'hésitez pas à partager vos commentaires avec moi.

_Un remerciement spécial à [Joe](https://github.com/joejean) qui m'a aidé en relisant cet article._

Adios !