---
title: Comment calculer la hauteur d'un arbre binaire avec la méthode récursive
subtitle: ''
author: Ry Vee
co_authors: []
series: null
date: '2019-01-07T23:49:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-binary-tree-height-with-the-recursive-method-aafc461f2201
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ci3-dY6FOCFu2UeqtzJ73A.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: General Programming
  slug: programming
- name: Recursion
  slug: recursion
- name: Ruby
  slug: ruby
- name: software development
  slug: software-development
seo_title: Comment calculer la hauteur d'un arbre binaire avec la méthode récursive
seo_desc: 'Previously I wrote about an algorithm for finding out the height of a binary
  tree using iteration. Though that method gets the job done (in 7 steps no less),
  the same can be accomplished in a much simpler way.

  In my opinion, one of the most powerful ...'
---

Précédemment, j'ai écrit sur un algorithme pour déterminer la hauteur d'un arbre binaire [en utilisant l'itération](https://medium.freecodecamp.org/how-to-calculate-a-binary-trees-height-using-array-iteration-in-ruby-63551c6c65fe). Bien que cette méthode accomplisse la tâche (en 7 étapes ni plus ni moins), le même résultat peut être obtenu de manière beaucoup plus simple.

À mon avis, l'une des techniques de programmation les plus puissantes est la récursivité. Pour les lecteurs nouveaux en programmation — c'est simplement une fonction ou une méthode qui s'appelle elle-même. Pour simplifier l'introduction, nous avons une méthode ci-dessous qui appelle une autre méthode :

```ruby
def outer_method(name)       (R1)
  inner_method + name
end
def inner_method             (R2)
  "Hello "
end
print outer_method("Steve") -> #"Hello Steve"
```

Dans la méthode ci-dessus `outer_method`, qui prend une chaîne de caractères comme argument, appelle `inner_method`, qui retourne simplement la chaîne « Hello » à l'intérieur. La récursivité est similaire en ce sens que, disons dans ce cas, `outer_method` s'appelle simplement elle-même :

```ruby
def outer_method(name)              (R3)
  outer_method("hello ") + name
end (R3)
```

Un avertissement, cependant, avec le code `R3` ci-dessus — il s'exécutera jusqu'à ce que l'ordinateur se plaigne que les ressources ne sont pas suffisantes pour continuer à traiter la méthode. C'est comme exécuter une boucle infinie sauf que les boucles infinies ne lèvent pas nécessairement d'exceptions. La raison en est que le code `R3` n'a pas d'« état terminal » ou un point où il ne « récurse » plus.

Nous pouvons résoudre cela en incluant un état terminal :

```ruby
def outer_method(name)                 (R4)
  return name if name == "hello "
  outer_method("hello ") + name
end
```

La première ligne à l'intérieur de la définition de la méthode indique simplement que si l'argument `name` est égal à « hello » alors retourne simplement `name`. Cela ignorera alors toute ligne après celle-ci. Par conséquent, dans la deuxième ligne, le code `outer_method("hello ")` donnera simplement la chaîne "hello " à ajouter à n'importe quel nom dans l'argument principal. Ainsi, le même `print outer_method("Steve")` résultera en la sortie "hello Steve" également.

D'accord, cela n'est peut-être pas le meilleur exemple pour décrire la récursivité (car la version récursive dans ce cas n'a pas tant d'avantages sur la version non récursive). Mais en travaillant sur le problème de la hauteur de l'arbre binaire, nous verrons que la récursivité est beaucoup plus simple à comprendre et plus rapide à exécuter.

Pour cette discussion, je vais remettre le même exemple que celui que j'ai montré dans l'article précédent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tsVyCA_zXrAh3LqTF4LHxw.png)
_Figure 1 : Arbre binaire simple_

que nous pouvons représenter comme le tableau suivant :

```ruby
tree = [1, 7, 5, 2, 6, 0, 9, 3, 7, 5, 11, 0, 0, 4, 0] (T0)
```

Les indices des enfants gauche et droit de n'importe quel sous-arbre peuvent être déterminés comme suit :

```ruby
left child of tree[i] is at index 2*i + 1 (T1)
right child of tree[i] is at index 2*i + 2 (T2)
```

Si vous êtes perplexe quant à la manière dont la figure ci-dessus est devenue le tableau qui suit, je vous dirige vers la lecture de l'[article précédent](https://medium.freecodecamp.org/how-to-calculate-a-binary-trees-height-using-array-iteration-in-ruby-63551c6c65fe) sur la méthode itérative pour clarification.

Et à nouveau, la formule pour calculer la hauteur d'un arbre binaire, ainsi que les hauteurs de n'importe lequel de ses sous-arbres, est :

```ruby
height = 1 + max of(left_child_height, right_child_height) (T3)

```

Maintenant, avec ces éléments, nous pouvons esquisser les étapes pour développer un programme récursif.

**Étape 0 :** Définir les valeurs par défaut — Pour simplifier l'appel initial de la méthode, j'aime toujours définir des valeurs par défaut pour les arguments qui changeront lors de chaque appel récursif. Puisque nous allons calculer les hauteurs de manière répétitive, nos indices changeront toujours.

Par exemple, pour trouver la hauteur de l'enfant gauche de la racine (`tree[0]`), nous devrons appeler la méthode sur cet enfant gauche (dont l'index est à `2*(0) + 1`). Par conséquent, notre définition de méthode sera :

```rb
def tree_height_recursive(tree_array,i=0) (S0.1)
```

pour indiquer que pour l'appel initial, nous l'appelons sur l'élément racine. Cela nous permettra simplement d'appeler `tree_height_recursive` en entrant uniquement le tree_array. Cependant, cela signifie également, comme nous le verrons dans la simulation par la suite, que nous pouvons trouver la hauteur de n'importe quel sous-arbre en incluant simplement son index comme deuxième argument dans l'appel de méthode.

**Étape 1 :** Trouver l'état terminal — À quel moment retournons-nous simplement une valeur et n'effectuons plus d'appels récursifs ? Dans notre problème d'arbre binaire, l'état terminal est à :

```rb
return 0 if tree[i].nil or tree[i] == 0 (S1.1)
```

Il indique simplement que si l'élément à l'index `i` n'existe pas ou si sa valeur est 0, alors retourne simplement 0. Logiquement, un sous-arbre inexistant n'aura aucune hauteur.

**Étape 2 :** Trouver la hauteur de l'enfant gauche — c'est là que la magie de la récursivité commence à nous bénéficier. Nous n'avons besoin d'aucun code sophistiqué. Plus besoin de déclarer un autre tableau pour contenir la hauteur de chaque élément. Plus besoin de définitions de variables multiples pour les indices de hauteur et les hauteurs elles-mêmes, juste :

```rb
right_child_height = tree_height_recursive(tree_array, 2*i + 2)

```

Nous passons simplement l'index de l'enfant gauche comme deuxième argument. Pouvez-vous voir pourquoi ?

Nous faisons de même pour trouver la hauteur de l'enfant droit ensuite.

**Étape 3 :** Trouver la hauteur de l'enfant droit — De même, nous faisons simplement un appel récursif à notre méthode mais en passant l'index de l'enfant droit comme deuxième argument :

```rb
right_child_height = tree_height_recursive(tree_array, 2*i + 2)

```

Maintenant que nous avons les hauteurs des enfants gauche et droit, nous pouvons maintenant calculer la hauteur totale.

**Étape 4 :** Calculer et retourner la hauteur totale — Comme le stipule le code `T3`, nous ajoutons simplement 1 et la hauteur de celui qui est le plus grand entre les enfants gauche et droit.

```rb
total_height = 1 + [left_child_height, right_child_height].max (S4.1)
```

Puisque `S.4` sera la dernière instruction dans notre méthode, alors la `total_height` évaluée sera retournée. Souvenez-vous que si les conditions dans `S1.1` sont vraies (notre état terminal), alors aucune des étapes 2-4 ne s'exécutera et la méthode retournera simplement 0.

La méthode complète ci-dessous :

En comparant cela à la [méthode itérative](https://medium.freecodecamp.org/how-to-calculate-a-binary-trees-height-using-array-iteration-in-ruby-63551c6c65fe), la version récursive a pris 3 étapes de moins et 4 définitions de variables de moins. Le code est également (en excluant les espaces vides et les commentaires) 7 lignes de moins. En plus de cela, le code récursif s'exécutera 2 fois plus vite (en utilisant le module intégré `benchmark` de Ruby). C'est un grand avantage si nous exécutons la méthode sur des arbres binaires de centaines de niveaux de haut.

Maintenant, faisons la même simulation que précédemment. Pour l'arbre à `T0`, nous exécutons la méthode récursive :

```
tree = [1, 7, 5, 2, 6, 0, 9, 3, 7, 5, 11, 0, 0, 4, 0]
```

```rb
puts tree_height_recursive(tree_array)-> #should give us 4
```

Notez que puisque nous avons un `i=0` par défaut dans notre définition de méthode, nous n'avons pas besoin de spécifier l'index ici car nous trouvons la hauteur de l'arbre entier. Pour rendre cette simulation plus intuitive, nous allons créer un tableau imaginaire appelé `call_stack` où nous poussons chaque appel à `tree_height_recursive`.

Ainsi, lorsque nous appelons la méthode pour la première fois (l'appel principal), nous la stockons dans une variable temporaire `ht_0` et la poussons dans `call_stack` :

```
ht_0 = height of tree[0] = tree_height_recursive(tree_array,i=0)
```

```rb
call_stack = [ht_0]
```

Nous exécutons ensuite l'étape 1 :

```rb
tree[0].nil? -> #falsetree[0] == 0 -> #false, it is 2
```

Puisque cela donne `false`, nous passons à l'étape 2 :

```
since i= 0, then 2*i + 1 = 2*0 + 1 = 1:
```

```rb
left_child_height = tree_height_recursive(tree_array,1)
```

Puisque nous ne pouvons pas déterminer immédiatement cette hauteur, nous la poussons à nouveau dans `call_stack` :

```
ht_1 = left_child_height = tree_height_recursive(tree_array,1)
```

```
call_stack = [ht_0,ht_1]
```

Puis, en effectuant l'étape 3 :

```rb
ht_2 = right_child_height = left_child_height = tree_height_recursive(tree_array,)
```

```rb
call_stack = [ht0,ht1,ht2]
```

Nous ne pouvons pas passer à l'étape 4 tant que tous les éléments dans `call_stack` n'ont pas été évalués par notre programme et retirés de `call_stack` (ce qui devrait se produire chaque fois que chaque hauteur a été évaluée).

Nous ferons donc de même pour chacune des hauteurs suivantes. Par exemple, pour calculer `ht1`, nous savons que nous devons également calculer les hauteurs de ses propres enfants gauche et droit. Cela signifie que la méthode sera également appelée pour eux. Pour ne pas prolonger cet article, le lecteur est invité à essayer cela sur papier.

En fin de compte, la méthode sera appelée récursivement avec `i = 14` comme deuxième argument. Ainsi, à ce stade, `call_stack` sera :

```rb
call_stack = [ht0,ht1,ht2,ht3,ht4,ht5,ht6,ht7,ht8,ht9,ht10,ht11,ht12,ht13,ht14]
```

Maintenant, nous allons évaluer chacun. Notez que de `tree[7]` à `tree[14]`, les éléments n'ont pas d'enfants. Nous pouvons donc simplement évaluer leurs hauteurs à 1 ou 0 (selon que `tree[i]` est 0 ou non (où `i ≥ 7`) :

```
ht14 = 0
```

```
ht13 = 1
```

```
ht12 = 0
```

```
ht11 = 0
```

```
ht10 = 1
```

```
ht9 = 1
```

```
ht8 = 1
```

```
ht7 = 1
```

Encore une fois, lorsque ces hauteurs sont évaluées, nous les retirons successivement de `call_stack`. Après quoi, `call_stack` apparaîtra comme suit :

```rb
call_stack = [ht0, ht1, ht2, ht3, ht4, ht5, ht6]
```

Maintenant, pour évaluer `ht6`, nous devons nous souvenir qu'il s'agit de l'appel à `tree_height_recursive(tree_array, 6)`. À l'intérieur de cet appel, nous appelons également la méthode pour calculer les hauteurs des enfants gauche et droit de `tree[6]`. Celles-ci, nous les avons déjà évaluées comme `ht13` et `ht14`. Donc alors :

```rb
ht6 = 1 + [ht13, ht14].max = 1 + [1,0] = 1 + 1 = 2
```

Nous évaluons maintenant `ht5`, qui est la hauteur de `tree[5]`. Nous connaissons les hauteurs de ses enfants sont `ht11` et `ht12`

```rb
ht5 = 1 + [ht11,ht12].max = 1 + [0,0].max = 1 + 0 = 1
```

Faisons de même pour `ht4` à `h1` (à nouveau, le lecteur est invité à faire la confirmation sur papier) :

```
ht4 = 1 + [ht9,ht10].max = 1 + [1,1].max = 1 + 1 = 2
```

```
ht3 = 1 + [ht7, ht8].max = 1 + [1, 1].max = 1 + 1 = 2
```

```
ht2 = 1 + [ht5, ht6].max = 1 + [1,2].max = 1 + 2 = 3
```

```rb
ht1 = 1 + [ht3, ht4].max = 1 + [2,2].max = 1 + 3 = 3
```

Encore une fois, nous retirons chaque hauteur de `call_stack` au fur et à mesure que nous l'évaluons, donc après avoir évalué `ht1`, le `call_stack` apparaît comme suit :

```rb
call_stack = [ht0]
```

Maintenant, l'évaluation de `ht0` revient à l'appel principal de `tree_height_recursive`, donc voici l'étape 4 restante :

```rb
ht0 = 1 + [ht1, ht2].max = 1 + [3, 3].max = 1 + 3 = 4ortotal_height = 1 + [left_child_height, right_child_height].max
```

Ce qui retournera `4` comme résultat de l'appel de méthode principal.

Comme je le mentionne souvent, faire cela sur papier, que ce soit lors de la formulation de l'algorithme ou lors de la simulation, aidera beaucoup à le comprendre. Cette même méthode peut également être utilisée pour déterminer la hauteur de n'importe quel sous-arbre à l'intérieur du `tree_array`, par exemple pour déterminer uniquement la hauteur de l'enfant gauche de l'arbre :

```rb
puts tree_height_recursive(tree_array, 1) -> #will print out 3
```

Ou n'importe quel sous-arbre inférieur :

```rb
puts tree_height_recursive(tree_array, 3) -> #will print out 2
```

#### Conclusion

Le point clé dans la création d'un algorithme récursif, selon ma perspective, est de définir l'état terminal. Encore une fois, il s'agit du scénario dans lequel la méthode principale n'aura pas à effectuer d'appel récursif à elle-même. Sans cela, la méthode continuera à s'appeler elle-même jusqu'à ce que l'ordinateur explose (au sens figuré...). Lorsque nous avons l'état terminal, nous pouvons facilement définir les arguments pour les appels récursifs et savoir que notre méthode retournera en toute sécurité la valeur que nous attendons.

Enfin, travailler sur des algorithmes met notre esprit au défi de réfléchir. En tant qu'ingénieurs logiciels, ou même ingénieurs en général, notre tâche principale est de résoudre des problèmes. Nous devons donc développer nos compétences en pensée critique.

Si pour un problème, notre première option est toujours « google it » et copier/coller le code d'autres personnes sans comprendre pleinement le problème et la solution copiée, alors nous nous nuisons à nous-mêmes.

Ma suggestion est donc d'avoir toujours un stylo et du papier à portée de main et de ne pas taper de code immédiatement lorsqu'on est confronté à un défi algorithmique. Simulez le problème pour des entrées simples, puis élaborez le code après avoir déterminé les étapes (comme je les ai décrites ci-dessus).

**Suivez-moi** sur [**Twitter**](https://twitter.com/coachryanv) | [**Github**](https://github.com/rvvergara)