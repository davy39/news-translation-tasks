---
title: Comment résoudre l'énigme des recruteurs de Google sur le lancer d'œufs depuis
  un bâtiment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T08:28:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-google-recruiters-puzzle-about-throwing-eggs-from-a-building-de6e7ef1755d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Uq3d3wn7B8yOPGIK.jpg
tags:
- name: Google
  slug: google
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment résoudre l'énigme des recruteurs de Google sur le lancer d'œufs
  depuis un bâtiment
seo_desc: 'By Marcin Moskala

  There are a lot of great puzzles for programming job interviews. My favorite one
  is also known as one of the favorites among Google recruiters:


  You work in a 100 floor building and you get 2 identical eggs. You need to figure
  out t...'
---

Par Marcin Moskala

Il existe de nombreuses énigmes passionnantes pour les entretiens d'embauche en programmation. Mon préférée est également connue comme l'une des préférées des recruteurs de Google :

> Vous travaillez dans un bâtiment de 100 étages et vous avez 2 œufs identiques. Vous devez déterminer le plus haut étage depuis lequel un œuf peut être lancé sans se casser. Trouvez un algorithme qui minimise le nombre de lancers dans le pire des scénarios.

Nous pouvons faire quelques hypothèses :

* Si un œuf ne se casse pas lorsqu'il est lancé depuis un certain étage, alors il ne se cassera pas lorsqu'il sera lancé depuis n'importe quel étage inférieur.
* Un œuf qui survit à une chute peut être réutilisé.
* Un œuf cassé doit être jeté.
* L'effet d'une chute est le même pour tous les œufs.
* Si un œuf se casse lorsqu'il est lancé, alors il se casserait s'il était lancé depuis un étage plus élevé.

La plupart des gens écrivent des algorithmes pour résoudre cette énigme (et nous le ferons aussi), mais il existe en réalité une solution simple.

#### Réponse la plus simple

La manière la plus simple d'obtenir l'étage minimal est de lancer un œuf depuis le premier étage, puis depuis le deuxième, et ainsi de suite. De cette façon, lorsque l'œuf se cassera enfin, nous saurons que c'est l'étage en question. C'est un algorithme fiable, mais dans le pire des scénarios, il faudrait 100 lancers.

L'important à noter est que c'est le seul algorithme fiable lorsque vous n'avez qu'un seul œuf. Vous devez donc commencer à utiliser cet algorithme lorsque vous cassez le premier œuf.

#### Réponse intuitive

Ainsi, notre premier œuf doit être utilisé pour diviser la plage de 100 étages en plages plus petites de manière aussi efficace que possible. Ainsi, une réponse intuitive et populaire est de lancer le premier œuf depuis le 1/n-ième des étages à vérifier. Par exemple, 1/3. L'algorithme ressemblera alors à ce qui suit :

* Lancez l'œuf depuis le 33ème étage. S'il se casse, alors nous vérifions les 32 premiers étages en utilisant le deuxième œuf.
* Sinon, nous lançons l'œuf depuis le 33 + (67 * 1/3) = 55ème étage. S'il se casse, alors nous vérifions les étages 34 à 55 en utilisant le deuxième œuf.
* …

Le pire scénario pour 1/3 est max(33, 24, …) = 33. De cette manière, nous pourrions trouver un n parfait qui optimise le nombre de lancers en utilisant une certaine programmation dynamique. C'est une solution valable qui présente une réflexion de programmation, mais ce n'est pas une solution optimale.

#### Solution parfaite

Pour comprendre la solution parfaite, nous devons comprendre l'équilibre utilisé pour calculer le nombre de lancers dans le pire des scénarios :

![Image](https://cdn-media-1.freecodecamp.org/images/OolWyrKqqniWgpZFcEXGMM8mey-gDM94m5Ln)

Où F(n) est le prochain étage depuis lequel nous lançons le premier œuf.

Si nous introduisons la variable suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/aksQXa8OxxKjmyWm4sH1JAygveWHijT0fMBB)

alors l'équilibre est le suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/WFWn-DWbpK3pgWfCAKq1Jgf6CWTjZdLyPwyZ)

La solution optimale est lorsque tous les [arguments](https://blog.kotlin-academy.com/programmer-dictionary-parameter-vs-argument-type-parameter-vs-type-argument-b965d2cc6929) de cette fonction max sont égaux. Comment y parvenir ? En regardant depuis la fin, le dernier D(n) sera 1, car nous arriverons finalement au point où il n'y a qu'un seul étage pour le premier œuf. Par conséquent, D(n-1) devrait être égal à 2 car il a un lancer de moins du premier œuf.

Nous voyons alors que le premier œuf devrait être lancé enfin depuis le 99ème étage, précédemment depuis 99–2=97, précédemment depuis 97–3=94, 90, 85, 79, 72, 64, 55, 45, 34, 22 et le 9ème étage. **C'est une solution optimale !** De cette manière, nous avons besoin de 14 lancers dans le pire des scénarios (la plus petite différence est 13, mais nous avons dû faire un lancer supplémentaire au 9ème étage).

L'équation simple pour trouver la réponse est la suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/7McAQgwk2rOkUR9Qc7g3-4Yz5HYBWFNi3JMG)

Où `f` est le nombre d'étages. Cela peut être simplifié en :

![Image](https://cdn-media-1.freecodecamp.org/images/XzJrN3BfcOlZgyoUgnjLSyznLhWyQ1MG9mu-)

Ce qui est égal à :

![Image](https://cdn-media-1.freecodecamp.org/images/EY22gKaNq7dvfRNd7Qo4wAdkQ36gubIzatvq)

#### Vérification

D'accord, nous avons donc une solution et nous pouvons la calculer sans aucune aide. Il est temps de vérifier si elle est correcte. Nous allons écrire un simple programme Kotlin pour cela. Tout d'abord, exprimons comment compter le nombre de lancers pour une certaine décision. Lorsque nous avons 2 étages ou moins, alors nous avons besoin d'autant de lancers qu'il reste d'étages. Sinon, nous devrions utiliser l'équilibre déjà présenté :

```
fun maxThrows(floorsLeft: Int, nextFloor: Int): Int =  if (floorsLeft <= 2) floorsLeft  else maxOf(nextFloor, bestMaxThrows(floorsLeft - nextFloor) + 1)
```

Nous avons utilisé ici la fonction `bestMaxThrows`. C'est une fonction hypothétique qui retourne le nombre de lancers en supposant que les prochaines décisions sont parfaites. Voici comment nous pouvons la définir :

```
fun bestMaxThrows(floorsLeft: Int): Int =  maxThrows(floorsLeft, bestNextStep(floorsLeft))
```

Encore une fois, nous avons simplement délégué la responsabilité de l'optimisation du prochain étage à la fonction `_bestNextStep_`. Cette fonction nous donne le meilleur prochain pas. Nous pouvons la définir simplement — lorsque 2 étages ou moins restent, alors nous lancerons un œuf depuis le premier étage. Sinon, nous devons vérifier toutes les options et trouver celle optimale. Voici l'implémentation :

```
val bestNextStep(floorsLeft: Int): Int =   if (floorsLeft <= 2) 1  else (1..floorsLeft)        .toList()        .minBy { maxThrows(floorsLeft, it) }!!
```

Notez que cette fonction utilise la fonction `_maxThrows_`, donc nous traitons avec une récurrence. Ce n'est pas un problème, car lorsque `bestNextStep` appelle `maxThrows`, elle l'appelle toujours avec une valeur plus petite que `floorsLeft` (car `nextFloor` est toujours plus grand que 0). Avant de l'utiliser, nous ajouterons une mise en mémoire tampon pour accélérer les calculs :

```
val bestNextStep: (Int) -> Int = memorise { floorsLeft ->  if (floorsLeft <= 2) 1  else (1..floorsLeft)        .toList()        .minBy { maxThrows(floorsLeft, it) }!!}fun maxThrows(floorsLeft: Int, nextFloor: Int): Int =  if (floorsLeft <= 2) floorsLeft  else maxOf(nextFloor, bestMaxThrows(floorsLeft - nextFloor) + 1)val bestMaxThrows: (Int) -> Int = memorise { floorsLeft ->  maxThrows(floorsLeft, bestNextStep(floorsLeft))}fun <V, T> memorise(f: (V) -&gt; T): (V) -> T {    val map = mutableMapOf<V, T&gt;()    return { map.getOrPut(it) { f(it) } }}
```

Tout d'abord, nous pouvons vérifier si cela retourne le même résultat que celui que nous avons calculé :

```
fun main(args: Array<String>) {    print(bestMaxThrows(100)) // Affiche : 14}
```

La réponse est bonne :) Vérifions nos prochaines étapes :

```
fun main(args: Array<String>) {    var floor = 0    while (floor < 100) {        val floorsLeft = 100 - floor        val nextStep = bestNextStep(floorsLeft)        floor += nextStep        print("$floor, ")    }}
```

Résultat :

9, 22, 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99, 100,

Tout comme nous l'avons calculé ! Bien :D

### Vue d'ensemble

Maintenant, nous avons un bel algorithme que nous pouvons utiliser pour de nombreux problèmes similaires. Par exemple, nous pouvons le modifier légèrement pour calculer le nombre de lancers pour le scénario le plus probable. Nous pouvons également vérifier comment ce nombre minimal de lancers variera en fonction de la hauteur du bâtiment. Voici un graphique répondant à cette question :

![Image](https://cdn-media-1.freecodecamp.org/images/avPL-Nw2Cqndgf57fnyD80X3PA9rjYlmoG-8)

### Conclusion

Vous êtes maintenant mieux préparé pour votre entretien chez Google, mais il est plus important que vous soyez maintenant mieux préparé pour la pensée algorithmique en général. Cet algorithme a présenté une approche fonctionnelle intéressante. Une approche similaire peut être utilisée pour de nombreux problèmes différents dans nos emplois quotidiens.

J'espère que cela vous a plu. **Applaudissez** pour dire merci et pour aider les autres à trouver cet article. Plus de matériaux intéressants sur [mon Twitter](https://twitter.com/marcinmoskala). Référez-moi en utilisant [@marcinmoskala](https://twitter.com/marcinmoskala). Si vous êtes intéressé par Kotlin, consultez [Kotlin Academy](https://blog.kotlin-academy.com/) et [Kotlin Academy portal](http://portal.kotlin-academy.com/) pour des énigmes Kotlin et des matériaux avancés.