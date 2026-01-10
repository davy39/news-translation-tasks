---
title: 'Analyse Asymptotique Expliquée avec Pokémon : Une Plongée Profonde dans l''Analyse
  de Complexité'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T17:38:04.000Z'
originalURL: https://freecodecamp.org/news/asymptotic-analysis-explained-with-pokemon-a-deep-dive-into-complexity-analysis-8bf4396804e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iWO7juZ8Nb--nnMGUKvKcA.jpeg
tags: []
seo_title: 'Analyse Asymptotique Expliquée avec Pokémon : Une Plongée Profonde dans
  l''Analyse de Complexité'
seo_desc: 'By Divya Godayal

  by Sachin Malhotra and Divya Godayal



  Let’s admit that we are either still stuck on the nuances of how to write a good
  algorithm or we dread the term itself.


  An algorithm is nothing fancy. It is just the method of doing something. ...'
---

Par Divya Godayal

par [Sachin Malhotra](https://medium.com/@sachinmalhotra) et [Divya Godayal](https://medium.com/@divyagodayal)

![Image](https://cdn-media-1.freecodecamp.org/images/1*iWO7juZ8Nb--nnMGUKvKcA.jpeg)

> Admettons que nous sommes soit toujours bloqués sur les nuances de l'écriture d'un bon algorithme, soit que nous redoutons le terme lui-même.

Un algorithme n'est rien de fancy. Ce n'est que la méthode pour faire quelque chose. Par exemple, disons que Pikachu doit rendre visite à son ami ce soir. Il peut le faire de nombreuses manières différentes. Ce qui compte, c'est la méthode qu'il choisit.

La méthode qu'il choisit déterminera le temps qu'il mettra pour atteindre son ami. Nous traitons de tels scénarios au quotidien. Nous ne pensons peut-être pas à chaque décision comme à une décision algorithmique, mais elle pourrait en être une.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RcDh9k3wXyrTeeCEXJNlhg.png)
_Ceci est un algorithme. Mais peut-être que même cela n'est pas suffisant pour un itinéraire efficace!!_

Les programmeurs doivent faire un choix éclairé à chaque fois. Cela compte encore plus lorsque vous construisez une application hautement scalable et réactive.

![Image](https://cdn-media-1.freecodecamp.org/images/1*luh16KeQqc7tSiTaYGsw_A.png)
_**Est-ce vrai ? Mmmm peut-être.**_

Vous êtes responsable de chaque morceau de code que vous écrivez, même si cela ne fonctionne pas. ?

## Table des Matières ✧

* [Pourquoi analyser un algorithme ? 🧠](https://medium.com/p/8bf4396804e0#845b)
* [Complexité et Comportement Asymptotique 🏃‍♀️](https://medium.com/p/8bf4396804e0#e744)
* [Degrés de Complexité ⏹⏸⏺⏏⋆](https://medium.com/p/8bf4396804e0#267c)
* [Outils pour l'Analyse de Complexité 🔧](https://medium.com/p/8bf4396804e0#ee13)
* [Complexité Spatiale 🌍](https://medium.com/p/8bf4396804e0#ec3c)
* [Le Compromis Temps et Espace 🌳](https://medium.com/p/8bf4396804e0#b336)
* [Tri à Bulles 🍸](https://medium.com/p/8bf4396804e0#889a)
* [Tri par Insertion 📖📕🦧](https://medium.com/p/8bf4396804e0#f4cd)
* [Tri Fusion 👫](https://medium.com/p/8bf4396804e0#4ead)
* [Analyse de l'Arbre de Récursivité 🌳](https://medium.com/p/8bf4396804e0#3bdd)
* [Analyse par la Méthode Maître 🤠👶](https://medium.com/p/8bf4396804e0#f99f)
* [Recherche Binaire 🧠 👋 👈](https://medium.com/p/8bf4396804e0#d256)

## Pourquoi analyser un algorithme ? 🧠

![Image](https://cdn-media-1.freecodecamp.org/images/1*jeBCn1BrA07hRR_oIrodlQ.png)
_**Application des Algorithmes** — Basiquement tout, vous pouvez penser à tout !!!_

Les algorithmes sont partout. Littéralement, partout. En fait, pour écrire cet article, nous avons compilé une liste de 1200 étapes.

Ne prenez pas cela au sérieux maintenant. Je plaisante, bien sûr ! 🤭

Ce que je veux dire, c'est qu'il n'y a pas d'échappatoire aux algorithmes dans aucun domaine de la vie. Mieux vaut apprendre l'art de choisir le bon !

Disons que nos Pokémon bien-aimés ont organisé un championnat. Chaque fois qu'un Pokémon gagne un combat, son rang est mis à jour. Pour départager les égalités, le prochain combat est avec le Pokémon qui partage le même score.

On vous demande de construire un site web, qui est rapide pour indiquer le prochain match. Le ninja du codage en vous s'est excité et s'est lancé. Vous avez construit un site web chic, avec des graphiques cool. On vous avait initialement dit qu'il y avait 50 Pokémon qui feraient partie du combat.

Pour trouver le prochain jeu du Pokémon gagnant, vous avez décidé de comparer son score avec le score de chaque Pokémon dans le championnat, ce qui est essentiellement une recherche linéaire. Et cela a fonctionné comme un charme !

Mais le jour du premier match, **1000 nouveaux** Pokémon (assumons simplement 😜) se sont inscrits !! Aaaah, dommage. Vous ne vous y attendiez pas, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*6AYCwrz4Xkdjhu7EHYFJuw.gif)
_**Scalabilité : Vous ne pouvez pas l'ignorer.**_

L'analyse asymptotique est **l'évaluation de la performance d'un algorithme en termes de taille d'entrée (N), où N est très grand**. Elle vous donne une idée du comportement limite d'une application, et est donc très importante pour mesurer la performance de votre code.

Par exemple, si le nombre de Pokémon participant au combat est **N**, alors la complexité asymptotique de votre algorithme de [recherche linéaire](https://guide.freecodecamp.org/algorithms/search-algorithms/linear-search/) est **O(N)**. Si vous ne savez pas ce que cette notation signifie, ne vous inquiétez pas. Nous allons l'aborder bientôt.

En termes simples, c'est comme demander à tous les **N** Pokémon quel est leur rang et puis prendre une décision. Imaginez demander à tous les 1000 Pokémon. Fatigant ! n'est-ce pas ?

Pour une machine, **O(N)** n'est peut-être pas mauvais, mais sur un site web où l'accent est mis sur la réactivité et la vitesse, ce n'est peut-être pas le meilleur choix.

La raison pour laquelle 1000 nouveaux Pokémon deviennent un énorme problème est que vous n'avez pas pensé à l'aspect de la scalabilité de l'application dès le départ et avez utilisé une approche naïve pour résoudre le problème. Rencontrer de tels problèmes de scalabilité n'était qu'une question de temps.

L'analyse des algorithmes est comme cela, elle est toujours présente. Mais vous ne vous en souciez vraiment que lorsqu'elle est vraiment nécessaire. Et puis vous tournez simplement autour de la queue... uh oh, je veux dire autour du buisson 😸

![Image](https://cdn-media-1.freecodecamp.org/images/1*csi_6eFs6SnTeaXyezrUkw.gif)
_Oh Ma Queue ! Que diable fais-tu ici ??_

> Analyser un algorithme aide à mesurer l'efficacité de votre programme et nécessite votre attention dès le moment où vous commencez à penser à une solution.

Vous auriez simplement pu utiliser un [dictionnaire](https://guide.freecodecamp.org/computer-science/data-structures/dictionaries/) ou une [table de hachage](https://guide.freecodecamp.org/computer-science/data-structures/hash-tables/) pour trouver tous les Pokémon avec le même rang et réduire la complexité temporelle algorithmique à **O(1)**. C'est comme aller voir un seul Pokémon manager qui a la réponse à votre requête.

Une réduction folle de la complexité temporelle, de **O(N) à O(1)**. Analyser un algorithme rend possible la comparaison de différentes approches et la décision de la meilleure.

### Qu'est-ce que N, au fait ? 🤔

N définit l'entrée. Ici, N est le nombre de Pokémon. Pour les besoins de l'analyse algorithmique, nous considérons que N est très grand.

### Complexité et Comportement Asymptotique 🏃‍♀️

Disons que [Pikachu](https://www.pokemon.com/us/pokedex/pikachu) est à la recherche d'un co-Pokémon qui a un certain type de pouvoir spécial. Pikachu commence par demander à tous les Pokémon leurs pouvoirs un par un. Une telle approche est connue sous le nom de **recherche linéaire** puisque elle est faite linéairement, un par un. Mais pour notre référence, appelons-la **Recherche de Pikachu**.

```
1. Pikachu_Search(pokemon):              # Liste de pokemon
2.     for p in pokemon_list:           # Nombre d'itérations -  N 
3.         if p a un pouvoir spécial:  # Opération en temps constant
4.           return p               # Opération en temps constant
    
5.   return "Aucun Pokémon Trouvé"            # Opération en temps constant
```

Dans l'extrait de code ci-dessus, `pokemon_list` est la liste de tous les Pokémon participant au championnat. Par conséquent, la taille de cette liste est N.

**Analyse du Temps d'Exécution pour la Recherche de Pikachu :**

1. `Étape 2` est une boucle for, ainsi les opérations à l'intérieur seront répétées N fois. `Étape 4` n'est exécutée que si la condition à l'`étape 3` est vraie. Une fois que l'`étape 4` est exécutée, la boucle se rompt et le résultat est retourné.
2. Si l'`Étape 3` prend un temps constant, disons `C1`, alors le temps total pris dans la boucle for serait `**C1.N.**`
3. Toutes les autres opérations sont des opérations en temps constant non affectées par la boucle, donc nous pouvons prendre une constante cumulative pour toutes, `**C2**`.

> _Temps d'Exécution Total f(N) =_ `**_C1.N + C2_**` **_,_** _une fonction de N._

**Rendons-le grand.** Que se passe-t-il si la valeur de N est très, très grande. Pensez-vous que les constantes auraient une quelconque signification alors ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*1mx8dpF1xhICxc-z-ae9aQ.jpeg)

**Dans l'analyse algorithmique, une idée importante est de supprimer la partie moins importante.**

Par exemple, si le temps d'exécution d'un algorithme est exprimé comme `10N² + 2N + 5`, alors asymptotiquement, seul le terme d'ordre supérieur **N²** est significatif. Cela rend la comparaison entre les algorithmes beaucoup plus facile.

### Degrés de Complexité ⏹⏸⏺⏏⋆

Un algorithme montre différents comportements lorsqu'il est exposé à différents types d'entrées. Cela nous amène à la discussion de la manière dont nous pouvons définir ce comportement ou la complexité de l'algorithme. Puisque la recherche de Pikachu est toujours en cours, voyons ce qu'il se passe avec lui.

1. **Meilleur Cas ~** _Optimisme Pur_. Il a eu beaucoup de chance puisque le tout premier Pokémon qu'il a approché avait le pouvoir spécial que Pikachu recherchait.
2. **Pire Cas ~** _Pessimisme Pur_. Il a dû aller voir tous les Pokémon et, à son grand dam, le tout dernier Pokémon avait le super pouvoir qu'il voulait.
3. **Cas Moyen ~** _Être Pratique._ Pikachu est un Pokémon adulte maintenant. L'expérience lui a beaucoup appris et il sait que c'est une question de temps et de chance. Il a estimé de grandes chances de trouver le super Pokémon dans les 500 premiers Pokémon qu'il visite et il avait raison.

L'analyse d'un algorithme pourrait être faite de trois manières mentionnées ci-dessus.

La `complexité du meilleur cas` ne donne pas grand-chose. Elle agit comme la borne inférieure pour la complexité d'un algorithme. Si vous l'utilisez, vous vous préparez simplement pour le meilleur. Vous devez être très chanceux pour que votre algorithme atteigne les bornes du meilleur cas de toute façon. Dans un sens pratique, cela n'aide pas beaucoup.

Toujours bon à savoir, la `complexité du cas moyen` est généralement difficile à calculer car elle nécessite d'analyser la performance de votre algorithme sur différentes variations de l'entrée et n'est donc pas largement utilisée.

La `complexité du pire cas` vous aide à vous préparer au pire. Dans les algorithmes, ce type de pessimisme est considéré comme bon car il donne une borne supérieure sur la complexité. Ainsi, vous connaissez toujours les limites de votre algorithme !

### Outils pour l'Analyse de Complexité 🔧

Nous avons vu précédemment que le temps d'exécution total pour la Recherche de Pikachu est `f(N)= **_C1.N + C2_**` **,** une fonction de N. Connaissons mieux les outils que nous avons, pour représenter le temps d'exécution, afin de rendre possible la comparaison entre les algorithmes.

**Big O** 😮: Oh oui ! C'est prononcé comme ça. `Big — Oh` ! C'est la borne supérieure de la complexité d'un algorithme. Par conséquent, il est utilisé pour désigner le pire comportement d'un algorithme.

**Essentiellement, cela désigne le temps d'exécution maximum pour un algorithme quel que soit l'entrée.**

C'est la notation la plus largement utilisée en raison de sa facilité d'analyse d'un algorithme en apprenant son pire comportement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*riGmrXn3x7j87Lw8chswPA.png)
_C est une constante. **f(N)** est la fonction de temps d'exécution pour laquelle la borne supérieure est **g(N)**._

Pour la recherche de Pikachu, nous pouvons dire que f(N) ou le temps d'exécution est borné _par le haut_ par `**C.g(N)**` pour un N très grand, où c est une constante et `g(N) = N`. Ainsi, `O(N)` représente la borne supérieure asymptotique pour la recherche de Pikachu.

**Big Omega(Ω):** Similaire à la notation Big O, la notation Ω est utilisée pour définir une borne inférieure asymptotique sur la performance d'un algorithme. Par conséquent, cela est utilisé pour représenter les scénarios du meilleur cas.

La borne omega signifie essentiellement **la quantité minimale de temps que notre algorithme prendra pour s'exécuter**, indépendamment de l'entrée.

Cette notation n'est pas souvent utilisée dans les scénarios pratiques, puisque l'étude du meilleur comportement ne peut pas être une mesure correcte pour la comparaison.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CG_56UCl0vZ678ocCI7urA.png)
_C est une constante. **f(N)** est la fonction de temps d'exécution pour laquelle la borne inférieure est **g(N)**._

Pour la recherche de Pikachu, nous pouvons dire que f(N) ou le temps d'exécution est borné _par le bas_ par `**C.g(N)**` pour un N très grand, où c est une constante et `g(N) = 1`. Ainsi, `**Ω**(1)` représente la borne inférieure asymptotique pour la Recherche de Pikachu.

**Big Theta**(**Θ**): Une borne serrée sur le comportement d'un algorithme, cette notation définit les bornes supérieure et inférieure pour une fonction. Cela est appelé une `borne serrée` car nous fixons le temps d'exécution à un facteur constant près au-dessus et en dessous. Quelque chose comme ceci:

![Image](https://cdn-media-1.freecodecamp.org/images/1*XrZtO7deNDuZvWP4SwDO8A.png)
_C1 et C2 sont des constantes. **f(N)** est le temps d'exécution pour lequel la fonction de borne serrée serait **g(N)**_

Un algorithme peut présenter différents comportements dans les meilleurs et pires cas. Lorsque les deux sont identiques, nous avons tendance à utiliser la notation theta. Sinon, les meilleurs et pires cas sont appelés **séparément** comme:

(a) Pour le `**pire cas**`, f(N) est borné par la fonction `g(N) = N`, pour de grandes valeurs de N. Ainsi, la complexité de la borne serrée serait notée comme `Θ(N)`. Cela signifie que le temps d'exécution du pire cas pour la recherche de Pikachu est **au moins** `C_1⋅N_` et **au plus** `C_2⋅N._`

(b) De même, sa complexité de borne serrée pour le `**meilleur cas**` est `Θ(1)`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6wtt9IcNS3eBzGQlDDGrtw.png)

Prenons un autre exemple où `f(N) = 10N² + 2N + 5`, pour cette fonction, les complexités des meilleurs et pires cas seraient Ω(N²) et O(N²) respectivement. Ainsi, la complexité moyenne ou de la borne serrée serait Θ(N²).

Puisque la complexité du pire cas agit comme une meilleure métrique de comparaison, à partir de maintenant, nous utiliserons Big-O pour l'analyse de complexité.

### Complexité Spatiale 🌍

Nous avons discuté de la complexité temporelle jusqu'à présent. Un concept important dans l'analyse de complexité est la _Complexité Spatiale_. Comme le suggère le nom, cela signifie combien d'_espace ou de mémoire_ l'algorithme prendra en termes de N, où N est très grand.

Chaque fois que nous comparons différents algorithmes pour résoudre un problème particulier, nous ne nous concentrons pas uniquement sur les complexités temporelles. La complexité spatiale est également un aspect important pour comparer différents algorithmes. Oui, il est vrai que nous avons beaucoup de mémoire disponible de nos jours et donc, l'espace est quelque chose qui peut être compromis. Cependant, ce n'est pas quelque chose que nous devrions ignorer tout le temps.

Il y a un dilemme intéressant auquel les développeurs sont confrontés tout le temps lorsqu'ils trouvent des solutions pour des problèmes de programmation. Discutons un peu de ce que c'est.

### Le Compromis Temps et Espace 🌳

Plus souvent qu'autrement, vous voulez rendre votre algorithme extrêmement rapide. Parfois, en faisant cela, vous finissez par compromettre la complexité spatiale.

> Cependant, parfois nous échangeons un peu de **temps** pour optimiser l'**espace**.

Dans les applications pratiques, une chose ou une autre est compromise et cela est famously appelé le compromis temps-espace dans le monde de l'analyse algorithmique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TxlQ9MDoOIqB1H-rTA5CnQ.gif)
_Balançoire. Nous parlons d'un type de jeu similaire entre **Temps et Espace**_

Pikachu a réalisé qu'il cherchait un Pokémon tous les deux jours. Cela signifie essentiellement exécuter la Recherche de Pikachu encore et encore. Huh ! 😰 Naturellement, il s'est tellement fatigué de la quantité épuisante de travail qu'il devait fournir chaque jour.

Pour l'aider et accélérer son processus de recherche, nous avons décidé d'utiliser une table de hachage. Nous pouvons utiliser le _type de pouvoir_ d'un Pokémon comme _clé_ dans la table de hachage.

Si nous devons trouver le Pokémon avec un pouvoir spécial, la complexité du pire cas serait `O(1)`, puisque la recherche dans une table de hachage est une opération en temps constant.

Sans utiliser cette table de hachage, le pauvre petit Pikachu aurait dû aller voir chaque Pokémon individuellement et demander leurs pouvoirs. Et répéter cela est insensé.

Tout ce qu'il a fallu, c'est créer une table de hachage une fois et, à partir de là, l'utiliser pour les recherches afin de réduire le temps d'exécution global !

![Image](https://cdn-media-1.freecodecamp.org/images/1*0A9yDB0qZ88wnzw13V_Cng.gif)
_Whaaaaaaaaatttttttttt?_

Mais ce n'est pas tout, comme vous l'avez vu, cela s'accompagne d'un coût d'espace. La table de hachage aurait besoin d'une entrée pour chaque Pokémon. Par conséquent, la complexité spatiale serait `O(N)`.

`_O(N) Temps, O(1) Espace_` — **Choisissez entre** — `_O(1) Temps, O(N) Espace_`

![Image](https://cdn-media-1.freecodecamp.org/images/1*V84IpE3a3TPslY53nSEVyA.gif)
_Ne vous inquiétez pas, ce n'est pas si grave. ?_

Ce choix dépend des besoins de l'application. Si nous avons une application orientée client, elle ne doit pas être lente. La priorité dans une telle situation serait de rendre l'application aussi réactive que possible, peu importe la quantité d'espace utilisée. Cependant, si nous sommes vraiment limités par l'espace disponible, nous devons sacrifier le temps pour compenser cela.

> Choisir votre algorithme judicieusement aide à optimiser à la fois le temps et l'espace.

La complexité temporelle et spatiale vont toujours de pair. Nous devons faire les calculs et opter pour la meilleure approche. Il existe une règle d'or pour vous aider à décider laquelle compromettre. Tout dépend de l'application.

C'est beaucoup de concepts théoriques à assimiler. Nous savons, même le pauvre Pikachu s'est un peu ennuyé. Mais ne vous inquiétez pas, nous allons maintenant mettre tous ces concepts en pratique et les utiliser pour analyser la complexité de certains algorithmes. Cela aidera à clarifier les différences minimes entre les différents types de complexités, l'importance de la complexité Big-Oh, le compromis temps-espace et plus encore.

Pour commencer, Pikachu veut analyser toutes les techniques de tri. Trier tous les Pokémon par leurs rangs l'aide à garder le tableau des rangs organisé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CEyd9iHvnZkyuWVcabHQHA.gif)

Examinons les algorithmes de tri de base mais cruciaux. Le tableau d'entrée `pk_rank` à trier est de taille N.

Au cas où vous ne seriez pas familier avec l'un des algorithmes de tri mentionnés ci-dessous, nous vous conseillons de les lire avant de passer aux sections suivantes. L'intention des exemples suivants est **de ne pas** expliquer les différents algorithmes mais d'expliquer comment vous pouvez dériver leur complexité temporelle et spatiale.

### Tri à Bulles 🍸

Le [**tri à bulles**](https://guide.freecodecamp.org/algorithms/sorting-algorithms/bubble-sort)**,** l'un des algorithmes de tri les plus simples, compare répétitivement les éléments adjacents d'un tableau et les échange s'ils sont dans le mauvais ordre. L'analogie est tirée des bulles qui finissent par remonter à la surface. À mesure que les éléments d'un tableau sont triés, ils **remontent** progressivement à leur position correcte dans le tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hinlmu41uBcmnbO0kmypyw.gif)
_Exactement comme les bulles dans le verre de Pikachu. ?_

![Image](https://cdn-media-1.freecodecamp.org/images/1*uKKrhrU6C1ZV67WacLcwCQ.png)
_Algorithme de Tri à Bulles_

**Complexité Temporelle :** Maintenant que nous avons l'algorithme en place, analysons sa complexité temporelle et spatiale. Nous pouvons clairement voir à partir des `étapes 2 et 3` qu'il y a une structure de _boucle imbriquée_ dans l'algorithme. De plus, la plage de la deuxième boucle for est `N — 1 — i`, ce qui indique clairement qu'elle dépend de la boucle précédente.

```
si i = 0, la deuxième boucle for s'exécuterait N-1 fois
si i = 1, la deuxième boucle for s'exécuterait N-2 fois
si i = 2, la deuxième boucle for s'exécuterait N-3 fois
.
.
si i = N-1, la deuxième boucle for s'exécuterait 0 fois
```

Maintenant, nous savons la quantité de temps (itérations) que notre algorithme de tri à bulles prend à chaque étape. Nous avons mentionné précédemment qu'il y a une boucle imbriquée dans l'algorithme. Pour chaque valeur de la variable dans la première boucle, nous connaissons la quantité de temps prise dans la deuxième boucle. Il ne reste plus qu'à les additionner. Faisons cela.

```
S = N-1 + N-2 + N-3 + ... + 3 + 2 + 1
~ N * (N+1) / 2 
~ N² + N, en ignorant tous les coefficients
```

Si vous regardez les `étapes 4` et `5`, ce sont des opérations en temps constant. Elles n'ajoutent vraiment rien à la complexité temporelle (ou spatiale d'ailleurs). Cela implique que nous avons **N² + N** itérations et dans chaque itération, nous avons des opérations en temps constant qui sont effectuées.

Par conséquent, la complexité temporelle de l'algorithme de tri à bulles serait **C.(N² + N)** où `C` est une constante. Asymptotiquement, nous pouvons dire que la complexité temporelle du pire cas pour le Tri à Bulles est `**O(N²)**`.

Est-ce un bon algorithme de tri ? Nous n'avons pas regardé d'autres algorithmes pour comparer. Cependant, voyons combien de temps il faudra à cet algorithme pour trier un milliard de Pokémon (reproduction, surpopulation, vous voyez 😛).

Nous vous laissons faire le calcul, mais le tri à bulles prendra environ **31 709 ans** pour trier un milliard de Pokémon (en supposant que chaque instruction prend 1 ms pour s'exécuter). Pikachu est-il immortel ou quelque chose 🤔

![Image](https://cdn-media-1.freecodecamp.org/images/1*xKTLPvG81Zik6oeBScok3g.gif)
_tic-tac 1, tic-tac 2._

**Complexité Spatiale :** L'analyse de la complexité spatiale est comparativement plus simple que celle de la complexité temporelle pour cet algorithme. L'algorithme de tri à bulles n'effectue qu'une seule opération de manière répétée. L'échange de nombres. En faisant cela, il n'utilise aucune mémoire externe. Il réarrange simplement les nombres dans le tableau original et donc, la complexité spatiale est constante, ou `O(1)` ou même `Θ(1)`.

### Tri par Insertion 📖📕🦧

Aimez-vous jouer aux cartes ?

Eh bien, même si vous ne le faites pas, vous devez savoir qu'une bonne stratégie initiale dans de nombreux jeux est de ranger les cartes dans un ordre spécifique, c'est-à-dire **trier le jeu de cartes**. L'idée du tri par insertion est très similaire à celle de ranger le jeu de cartes.

Disons que vous avez quelques cartes triées dans l'ordre croissant. Si on vous donne une autre carte à `insérer` à la bonne position afin que les cartes dans votre main soient toujours triées. _Que ferez-vous ?_

> _Vous commenceriez par l'une ou l'autre des extrémités gauche ou droite des cartes en main et compareriez la nouvelle carte avec chaque carte du jeu pour trouver la bonne place._

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHkmGYcdX6nsWrmZCSp_ig.gif)
_Une fois que vous avez trouvé la bonne position, vous `insérerez` la carte là._

De même, si d'autres nouvelles cartes sont fournies, vous répétez le même processus pour chaque nouvelle carte et gardez les cartes dans votre main triées.

Le [**tri par insertion**](https://guide.freecodecamp.org/algorithms/sorting-algorithms/insertion-sort/) fonctionne de la même manière. Il commence à l'index `1` (l'indexation du tableau commence à `0`) et traite chaque élément comme une nouvelle carte. Chacun des nouveaux éléments peut alors être placé à la position correcte dans le _sous-tableau de gauche déjà trié_.

La chose importante à noter ici est que, étant donné une nouvelle carte (ou un élément dans notre cas à un index `j`), toutes les cartes en main (ou tous les éléments avant cet index) sont _déjà triées_.

Regardons un algorithme formel pour le tri par insertion suivi d'une animation qui exécute l'algorithme sur une entrée de test.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NeNYxh_69LXhnTJ3Ni160A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UpB6EEJZB8HihhERZWxC-A.gif)

**Complexité Temporelle :** À partir des `étapes 1 et 4`, il y a une structure `while` _imbriquée_ dans une boucle `for`. La boucle while s'exécute `j+1` fois et `j` dépend clairement de `i`. Voyons comment la valeur de `j` change avec les valeurs changeantes de `i`.

```
si i = 1, alors j = 0 donc la boucle while s'exécuterait 1 fois
si i = 2, alors j = 1 donc la boucle while s'exécuterait 2 fois
si i = 3, alors j = 2 donc la boucle while s'exécuterait 3 fois
.
.
si i = N-1, alors j = N-2 donc la boucle while s'exécuterait N-1 fois
```

Maintenant, nous savons la quantité de temps (itérations) que notre algorithme de tri par insertion prend à chaque étape. Le temps total est :

```
S = 1 + 2 + 3 + .... + N-2 + N-1
~ N * (N+1) / 2 
~ N² + N, en ignorant tous les coefficients
```

Les `étapes 2 à 7` sont des opérations en temps constant. Elles n'ajoutent vraiment rien à la complexité temporelle (ou spatiale d'ailleurs). Cela implique que nous avons **N² + N** itérations et dans chaque itération, nous avons des opérations en temps constant qui sont effectuées.

Par conséquent, la complexité temporelle de l'algorithme de tri par insertion serait **C.(N² + N)** où `C` est une constante. Asymptotiquement, nous pouvons dire que la complexité temporelle du pire cas pour le Tri par Insertion est la même que celle du tri à bulles, c'est-à-dire `**O(N²)**`.

**Complexité Spatiale :** L'analyse de la complexité spatiale est comparativement plus simple que celle de la complexité temporelle pour cet algorithme. L'algorithme de tri par insertion ne réarrange que les nombres dans le tableau original. En faisant cela, il n'utilise aucune mémoire externe. Par conséquent, la complexité spatiale est constante, ou `O(1)` ou même `Θ(1)`.

**Note :** Comparer les algorithmes sur la base de la complexité asymptotique est facile et rapide. De plus, à un niveau supérieur, c'est une bonne mesure. Mais d'un point de vue pratique, si deux algorithmes ont la même complexité, cela ne signifie pas nécessairement qu'ils ont la même performance dans des scénarios pratiques.

Lors du calcul de la complexité asymptotique d'un algorithme, nous ignorons tous les _facteurs constants_ et les termes d'ordre inférieur.

> _Mais ces valeurs ignorées finissent par s'ajouter au temps d'exécution d'un algorithme._

Le tri par insertion est beaucoup plus rapide que le tri à bulles lorsque le tableau est _presque_ trié. Pour chaque passage dans le tableau, le tri à bulles doit aller jusqu'à la fin du tableau et comparer les paires adjacentes, tandis que le tri par insertion, en revanche, s'arrêterait tôt s'il trouve que le tableau est trié. Essayez d'exécuter les deux algorithmes sur un tableau trié et regardez le nombre d'itérations qu'il faut à chacun pour terminer l'exécution.

Ainsi, chaque fois que vous cherchez le meilleur algorithme pour votre application, il doit être analysé sous de nombreux aspects différents. L'analyse asymptotique aide définitivement à éliminer les algorithmes plus lents, mais l'observation et des insights plus profonds aident à trouver l'algorithme le mieux adapté à votre application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XrDxuuZzmbrTDXWWGv9s7w.gif)
_Faites attention à cela !_

### Tri Fusion 👫

Jusqu'à présent, nous avons analysé deux des algorithmes de tri les plus basiques. Ce sont des algorithmes de tri introductifs mais ne sont pas ceux généralement utilisés en pratique en raison de leur complexité asymptotique élevée.

Passons à un algorithme de tri plus rapide et plus pratique. L'algorithme de tri fusion s'écarte de la structure de tri à _boucle imbriquée_ que nous avons vue dans les deux algorithmes précédents et adopte un nouveau paradigme que nous allons discuter ci-dessous.

L'algorithme de [**Tri Fusion**](https://guide.freecodecamp.org/algorithms/sorting-algorithms/merge-sort) est basé sur quelque chose connu sous le nom de paradigme de programmation _Diviser pour Régner_. Ce paradigme de programmation est basé sur une idée très simple et trouve son utilité dans de nombreux algorithmes différents, y compris le tri fusion. Diviser pour Régner est divisé en trois étapes de base :

> _**Diviser**_ : Diviser un grand problème en sous-problèmes plus petits.  
> _**Conquérir**_ : Résoudre de manière optimale les sous-problèmes plus petits  
> _**Combiner**_ : Enfin, combiner les résultats des sous-problèmes pour trouver la solution du grand problème original.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l-BZTiXtFs3jCYehwzsy6A.png)
_Lequel semble **plus facile**?_

Regardons un aperçu de la manière dont l'algorithme de tri fusion utilise le paradigme diviser pour régner.

1. _Diviser_ ~ La première étape du processus est de _diviser_ le tableau donné en deux sous-tableaux de taille égale. Cela aide puisque nous avons maintenant 2 sous-tableaux plus petits à trier, chacun avec la moitié du nombre d'éléments d'origine.
2. _Conquérir ~_ L'étape suivante consiste à trier les sous-tableaux plus petits. Cette partie est appelée l'étape de _conquête_ puisque nous résolvons les sous-problèmes de manière optimale.
3. _Combiner ~_ Enfin, nous avons deux moitiés triées du tableau original et nous devons les combiner de manière optimale pour obtenir un seul tableau trié. C'est l'étape de _combinaison_ du paradigme expliqué ci-dessus.

Mais attendez. Est-ce tout ?

Étant donné un tableau de 1000 éléments, si nous le divisons en 2 moitiés égales de 500 chacune, nous avons encore beaucoup d'éléments à trier dans un tableau (ou sous-tableau).

Ne devrions-nous pas diviser les deux moitiés en 4 pour obtenir des sous-tableaux encore plus courts ?

Oui ! En effet, nous devrions !

**Nous** [**divisons récursivement**](https://medium.freecodecamp.org/recursion-demystified-99a2105cb871) **le tableau en moitiés plus petites et trions et fusionnons les moitiés plus petites pour obtenir le tableau original.**

Cela signifie essentiellement que nous divisons, par exemple, un tableau de taille 1000 en 2 moitiés de 500 chacune. Ensuite, nous divisons ces deux moitiés en 4 portions de 250 chacune et ainsi de suite. Ne vous inquiétez pas si vous n'arrivez pas à contempler tout cela intuitivement en termes d'analyse de complexité. Nous y viendrons très bientôt.

Regardons l'algorithme pour le tri fusion. L'algorithme est divisé en deux fonctions, l'une qui trie récursivement les deux moitiés égales d'un tableau donné et une autre qui fusionne les deux moitiés triées ensemble.

Nous allons d'abord analyser la complexité de la fonction _fusion_ puis passer à l'analyse de la fonction _tri_fusion_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZVMhC2h0ndre_brfB2cEHg.png)
_**Fusionner** deux tableaux **triés**_

La fonction ci-dessus prend simplement deux moitiés triées du tableau et les fusionne en une seule moitié triée. Les deux moitiés sont définies à l'aide d'indices. La moitié gauche est de `[gauche, milieu]` et la moitié droite est de `[milieu + 1, droite]`.

Les `étapes 2-3` copient les éléments du tableau original vers un tampon temporaire et nous utilisons ce tampon à des fins de fusion. Les éléments triés sont copiés dans le tableau original. Puisque nous itérons sur une certaine portion du tableau, la complexité temporelle pour cette opération est `O(N)` en considérant qu'il y a `N` éléments dans le tableau.

L'`étape 5` est une boucle while qui itère sur la plus courte des deux sous-tableaux. Cette boucle while et celles qui suivent, aux `étapes 13 et 14`, couvrent tous les éléments des deux sous-tableaux. Ainsi, leur complexité temporelle combinée est `O(N)`.

Cela signifie que l'étape de fusion est un algorithme en temps linéaire.

> _La complexité globale du tri fusion est décidée par le nombre de fois où la fonction de fusion est appelée._

Passons à la fonction _tri_fusion_ originale. Elle est extrêmement simple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O84DDNcLEbGcQKZs5oFNLg.png)
_Algorithme de Tri Fusion_

L'`étape 4` appelle la fonction `tri_fusion` sur la moitié gauche du tableau.

L'`étape 5` appelle la fonction `tri_fusion` sur la moitié droite du tableau.

et ensuite l'`étape 6` appelle enfin la fonction `fusion` pour combiner les deux moitiés.

Oh. Une fonction qui s'appelle elle-même ? 🤨🤨

Comment calcule-t-on sa complexité ?

Jusqu'à présent, nous avons discuté de l'analyse des boucles. Cependant, de nombreux algorithmes, comme le Tri Fusion, sont récursifs par nature. Lorsque nous les analysons, nous obtenons une relation de récurrence pour la complexité temporelle. Nous obtenons le temps d'exécution sur une entrée de taille `N` en fonction de `N` et du temps d'exécution sur des entrées de tailles plus petites.

Principalement, il existe deux façons importantes d'analyser la complexité d'une relation de récurrence :

1. En utilisant un Arbre de Récursivité et
2. En utilisant la Méthode Maître.

### Analyse de l'Arbre de Récursivité 🌳

C'est la manière la plus intuitive pour analyser la complexité des relations de récurrence. Essentiellement, nous pouvons visualiser une relation de récurrence sous la forme d'un arbre de récursivité.

La visualisation aide à connaître la quantité de travail effectuée par l'algorithme à chaque étape (lire niveau) le long du chemin et la somme du travail effectué à chaque niveau nous indique la complexité globale de l'algorithme.

Avant de regarder l'arbre de récursivité pour l'algorithme de Tri Fusion, regardons d'abord la relation de récurrence pour celui-ci.

```
T(N) = 2T(N / 2) + O(N)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*gAesvFZFJT3uSq0tR1e3Kg.png)

Soit `T(N)` la quantité de travail effectuée (ou le temps pris pour) trier un tableau composé de `N` éléments. La relation ci-dessus stipule que le temps total pris est égal au temps pris pour trier les deux moitiés du tableau `+` le temps pris pour fusionner les deux moitiés. Nous avons déjà vu le temps pris pour fusionner les deux moitiés auparavant et cela est `O(N)`.

Nous pouvons écrire la relation de récurrence comme suit :

```
T(N) = 2T(N / 2) + O(N)
T(N / 2) = 2T(N / 4) + O(N / 2)
T(N / 4) = 2T(N / 8) + O(N / 4)
...
```

Il est beaucoup plus facile de visualiser cela sous la forme d'un arbre. Chaque nœud de l'arbre consisterait en deux branches puisque nous avons deux sous-problèmes différents étant donné un seul problème. Regardons l'arbre de récursivité pour le tri fusion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JQhExzK_FA8UlKgnHPHM6g.png)
_Arbre de Récursivité pour le Tri Fusion_

Chaque nœud de l'arbre représente un sous-problème et la valeur à chaque nœud représente la quantité de travail dépensée à chaque sous-problème. Le nœud racine représente le problème original.

Dans notre arbre de récursivité, chaque nœud non-feuille a 2 enfants, représentant le nombre de sous-problèmes en lesquels il se divise. Nous avons vu à partir de l'algorithme pour le Tri Fusion que, à chaque étape de la récursivité, le tableau donné est divisé en deux moitiés égales.

Ainsi, il y a deux choses importantes que nous devons déterminer afin d'analyser la complexité de l'algorithme de tri fusion.

1. Nous devons connaître la quantité de _travail_ effectué à chaque _niveau_ de l'arbre et
2. Nous devons connaître le nombre total de _niveaux_ dans l'arbre, ou, comme on l'appelle plus communément, la _hauteur de l'arbre._

Tout d'abord, nous allons calculer la hauteur de notre arbre de récursivité. Nous pouvons voir à partir de l'arbre de récursivité ci-dessus que chaque nœud non-feuille se divise en deux nœuds. Par conséquent, ce que nous avons ci-dessus est un _arbre binaire complet_.

Intuitivement, nous continuerons à diviser le tableau jusqu'à ce qu'il ne reste qu'un seul élément dans un sous-tableau, moment auquel nous n'avons besoin d'aucun tri (c'est le cas de base) et nous retournons simplement.

Au premier niveau de notre arbre de récursivité binaire, il y a un seul sous-problème composé de `N` éléments. Le niveau suivant de l'arbre se compose de `2` sous-problèmes (sous-tableaux à trier) avec `N / 2` éléments chacun.

Pour l'instant, nous ne nous préoccupons pas vraiment du _nombre de sous-problèmes_. Nous voulons simplement connaître la taille de chaque sous-problème puisque nous pouvons voir que **tous les sous-problèmes à un niveau particulier de l'arbre sont de la même taille.**

```
Au Niveau 0, nous avons des sous-problème(s) chacun composé de N    éléments
Au Niveau 1, nous avons des sous-problème(s) chacun composé de N/2  éléments
Au Niveau 2, nous avons des sous-problème(s) chacun composé de N/4  éléments
Au Niveau 3, nous avons des sous-problème(s) chacun composé de N/8  éléments
Au Niveau 4, nous avons des sous-problème(s) chacun composé de N/16 éléments
.
.
.
Au Niveau X, nous avons des sous-problème(s) chacun composé de 1 élément.
```

Le nombre d'éléments semble diminuer en _puissances de 2_. D'après le motif ci-dessus, il semble que :

```
N = 2^X 
X = log_2(N)
```

Cela signifie que la hauteur de notre arbre est `log_2(N)` (logarithme en base 2 de N). Maintenant, regardons la _quantité de travail effectuée par l'algorithme à chaque étape._

`T(N)` est défini comme la quantité de travail nécessaire pour trier un tableau de `N` éléments. Nous avons examiné la relation de récurrence pour cela plus tôt et elle était :

```
T(N) = 2T(N / 2) + O(N)
```

Cela implique que la quantité de travail effectuée au premier niveau de l'arbre est `O(N)` et le reste du travail est effectué au niveau suivant. Cela est dû à l'appel de récursion sous la forme `2T(N / 2)`. Au niveau suivant, comme nous pouvons le voir sur la figure ci-dessus, la quantité de travail effectuée est `2 * O(N / 2) = O(N)`. De même, la quantité de travail effectuée au troisième niveau est `4 * O(N / 4) = O(N)`.

Étonnamment, l'algorithme doit effectuer la même quantité de travail à chaque niveau et cette quantité de travail s'élève à `O(N)` qui est le temps consommé par la procédure de _fusion_. Ainsi, le nombre de niveaux définira la complexité temporelle globale.

Comme nous l'avons calculé précédemment, le nombre de niveaux dans notre arbre de récursivité est `log(N)` et donc, la complexité temporelle pour le Tri Fusion est `O(Nlog(N))`.

Hourra ! Nous avons appris une nouvelle méthodologie pour l'analyse asymptotique sous la forme d'arbres de récursivité. C'est une manière amusante de construire une intuition sur la complexité de toute relation de récurrence. Il n'est peut-être pas toujours faisable de dessiner l'arbre de récursivité complet, mais cela aide définitivement à construire une compréhension.

### Analyse par la Méthode Maître 🤠👶

Nous avons examiné la méthode basée sur l'arbre de récursivité pour l'analyse asymptotique des récurrences. Cependant, comme mentionné précédemment, il n'est peut-être pas faisable de dessiner l'arbre de récursivité à chaque fois pour calculer la complexité.

La récursivité du tri fusion divise un problème donné (tableau) en deux sous-problèmes plus petits (sous-tableaux). Et si nous obtenons un algorithme où un problème est divisé en, disons, 100 sous-problèmes ? Nous ne pourrons pas dessiner l'arbre de récursivité pour l'analyse.

Ainsi, nous avons besoin d'une méthode plus directe pour analyser la complexité d'une relation de récurrence. Nous avons besoin d'une méthode qui ne nécessite pas de _dessiner réellement_ l'arbre de récursivité mais qui s'appuie sur les mêmes concepts que l'arbre de récursivité.

C'est là que la **Méthode Maître** entre en jeu. Cette méthode est basée sur la méthode de l'arbre de récursivité. Il existe trois scénarios différents qui sont couverts par la méthode maître et qui couvrent essentiellement la plupart des relations de récurrence. Avant de regarder ces cas, cependant, regardons l'arbre de récursivité pour la relation de récurrence générale suivante :

```
T(n) = a T(n / b) + f(n)
```

* `n` est la taille du problème.
* `a` est le nombre de sous-problèmes dans la récursion.
* `n / b` est la taille de chaque sous-problème. (Ici, il est supposé que tous les sous-problèmes sont essentiellement de la même taille.)
* `f(n)` est le coût du travail effectué en dehors des appels récursifs, qui inclut le coût de la division du problème en sous-problèmes plus petits et le coût de la fusion des solutions aux sous-problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pyIKd1wW3vVXw3MF_Ssv_g.png)

Les deux choses les plus importantes à connaître pour comprendre la méthode maître sont la quantité de travail effectuée par l'algorithme à la racine et la quantité de travail effectuée aux feuilles.

Le travail effectué à la racine est simplement `f(n)`. La quantité de travail effectuée aux feuilles dépend de la hauteur de l'arbre.

La hauteur de cet arbre serait `log_b(n)` c'est-à-dire le logarithme en base `b` de `n`. Cela suit de l'arbre de récursivité que nous avons vu pour le tri fusion. `b` dans le cas du tri fusion est `2`. Le nombre de nœuds à n'importe quel niveau, `l` sont `a^l` et donc, le nombre de nœuds feuilles au dernier niveau serait :

```
a^{log_b(n)} = n ^ log_b(a) nœuds.
```

Puisque la quantité de travail effectuée sur chaque sous-problème au niveau final est `Θ(1)`, la quantité totale de travail effectuée aux nœuds feuilles est `n ^ log_b(a)`.

Si vous vous concentrez sur la relation de récurrence générique ci-dessus, vous remarquerez qu'il y a deux forces principales en jeu :

1. _L'étape de Division_ ~ le terme 𝒇(𝒏/𝒃) essaie désespérément de se reproduire, multipliant des copies de plus en plus petites de lui-même.
2. _L'étape de Conquête_ ~ le terme 𝒇(𝒏) représente la fusion puisqu'il essaie désespérément de fusionner ces mini-portions ensemble.

Les deux forces essaient de s'opposer l'une à l'autre et, en faisant cela, elles veulent contrôler la quantité totale de travail effectuée par l'algorithme et donc la complexité temporelle globale.

Qui va gagner ?

#### Cas 1 (L'étape de Division gagne)

Si `f(n) = Θ(n^c)` tel que `c < log_b(a)`, alors `T(n) = Θ(n^log_b(a)`. `f(n)` est la quantité de travail effectuée à la racine de l'arbre et `n ^ log_b(a)` est la quantité de travail effectuée aux feuilles.

Si le travail effectué aux feuilles est polynomialement plus important, alors les feuilles sont la partie dominante, et notre résultat devient le travail effectué aux feuilles.

```
ex. T(n) = 8 T(n / 2) + 1000 n^2
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*3oZQZ-MzHZX0GC91IIT_Dg.png)

Si nous adaptons cette relation de récurrence à la Méthode Maître, nous obtenons :

```
a = 8, b = 2, et f(n) = O(n^2)
D'où, c = 2 et log_b(a) = log_2(8) = 3
Clairement, 2 < 3 et cela correspond au Cas 1 de la Méthode Maître. Cela implique que la quantité de travail effectuée aux feuilles de l'arbre est asymptotiquement plus élevée que le travail effectué à la racine. Par conséquent, la complexité de cette relation de récurrence est Θ(n^log_2(8)) = Θ(n^3).
```

### Cas 2 (L'étape de Conquête gagne)

Si `f(n) = Θ(n^c)` tel que `c > log_b(a)`, alors `T(n) = Θ(f(n))`. Si le travail effectué à la racine est asymptotiquement plus important, alors notre complexité finale devient le travail effectué à la racine.

Nous ne nous préoccupons pas de la quantité de travail effectuée aux niveaux inférieurs ici, puisque le terme polynomial le plus grand dépendant de `n` est celui qui contrôle la complexité de l'algorithme. Par conséquent, le travail effectué à tous les niveaux inférieurs peut être ignoré en toute sécurité.

```
ex. T(n) = 2 T(n / 2) + n^2
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*gQdAJIqbC87o0Ct1dD9ySQ.png)

Si nous adaptons cette relation de récurrence à la Méthode Maître, nous obtenons :

```
a = 2, b = 2, et f(n) = O(n^2)
D'où, c = 2 et log_b(a) = log_2(2) = 1
Clairement, 2 > 1 et donc cela correspond au Cas 2 de la Méthode Maître où la majorité du travail est effectuée à la racine de l'arbre de récursivité et c'est pourquoi Θ(f(n)) contrôle la complexité de l'algorithme. Ainsi, la complexité temporelle de cette relation de récurrence est Θ(n^2).
```

#### Cas 3 [C'est une égalité !]

Si `f(n) = Θ(n^c)` tel que `c = log_b(a)`, alors `T(n) = Θ(n^c log(n))`. Le dernier cas est lorsque le travail effectué aux feuilles et le travail effectué à la racine de l'arbre sont égaux.

Dans ce cas, les étapes de conquête et de division sont également dominantes et donc, la quantité totale de travail effectuée est égale au travail effectué à _n'importe quel niveau * la hauteur de l'arbre._

```
ex. T(n) = 2T(n / 2) + O(n)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*JQhExzK_FA8UlKgnHPHM6g.png)
_Attendez, n'est-ce pas le Tri Fusion ?_

Oui ! C'est la complexité de l'algorithme de Tri Fusion. Si nous adaptons la relation de récurrence pour le tri fusion dans la Méthode Maître, nous obtenons :

```
a = 2, b = 2, et f(n) = O(n^1)
D'où, c = 1 = log_2(2)
Cela correspond au critère du Cas 3 décrit ci-dessus. La quantité de travail effectuée est la même à tous les niveaux comme on peut le vérifier sur la figure ci-dessus. Ainsi, la complexité temporelle est le travail effectué à n'importe quel niveau * le nombre total de niveaux (ou la hauteur de l'arbre).
```

Nous avons analysé la complexité temporelle de l'algorithme de Tri Fusion en utilisant deux méthodes différentes, à savoir l'Arbre de Récursivité et la Méthode Maître. Nous avons dû utiliser ces différentes techniques car l'algorithme de tri fusion est un algorithme **récursif** et les approches classiques d'analyse asymptotique que nous avons vues précédemment pour les **boucles** n'étaient d'aucune utilité ici.

**Complexité Spatiale :** En ce qui concerne la complexité spatiale, nous n'avons pas à utiliser de techniques compliquées et donc, l'analyse est beaucoup plus simple. Une structure de données principale occupant de l'espace dans l'algorithme de Tri Fusion est le tableau `tampon temporaire` qui est utilisé pendant la procédure de `fusion`.

Ce tableau est initialisé une fois et la taille de ce tableau est `N`. Une autre structure de données qui occupe de l'espace est la [_pile de récursion_](https://www.hackerearth.com/practice/notes/demystifying-recursion-by-stack-tracing/). Essentiellement, le nombre total d'appels récursifs détermine la taille de la pile de récursion. Comme nous l'avons vu dans la représentation de l'arbre de récursivité, **le nombre d'appels effectués par le tri fusion est essentiellement la hauteur de l'arbre de récursivité.**

La hauteur de l'arbre de récursivité était `log_2(N)` et donc, la taille de la pile de récursion sera également `log_2(N)` au maximum.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OQ4SghHM5aB1_e41KARnbA.png)

Par conséquent, la complexité spatiale totale pour le tri fusion serait `N + log_2(N) = O(N)`.

### Recherche Binaire 🧠 👋 👈

Souvenez-vous de notre ami Pikachu et de sa recherche d'un Pokémon avec un pouvoir spécifique. Le pauvre petit Pikachu avait 1000 Pokémon à sa disposition et il devait trouver celui avec un pouvoir spécifique. Oui, Pikachu est très sélectif quant à ses adversaires.

Ses exigences changent jour après jour et il ne peut certainement pas aller vérifier auprès de chaque Pokémon, chaque fois que ses exigences changent, c'est-à-dire qu'il ne peut pas effectuer une **Recherche Linéaire** dans la liste des Pokémon pour trouver celui qu'il cherche.

Nous avons mentionné précédemment l'utilisation d'une **Table de Hachage** pour stocker les Pokémon en utilisant leur valeur de pouvoir unique comme clé et le Pokémon lui-même comme valeur. Cela réduirait la complexité de la recherche à `O(1)`, c'est-à-dire un temps constant.

Cependant, cela utilise un espace supplémentaire qui augmente la complexité spatiale de l'opération de recherche à `O(N)` en considérant qu'il y a `N` Pokémon disponibles. `N` dans ce cas serait `1000`. Et si Pikachu n'avait pas tout cet espace supplémentaire disponible et qu'il voulait toujours accélérer le processus de recherche ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*zPvLZixp2h7khcIzBBXI6w.jpeg)
_Puis-je faire cela ?_

Oui ! Bien sûr, Pikachu peut utiliser ses connaissances profondes sur les **algorithmes de tri** pour trouver une stratégie de recherche qui serait plus rapide que la lente recherche linéaire.

Pikachu a décidé de demander de l'aide à son bon ami Deoxys. Deoxys, étant le Pokémon le plus rapide, aide Pikachu à **trier** la liste des Pokémon selon leur pouvoir.

Au lieu de s'appuyer sur les algorithmes de tri traditionnels, Deoxys utilise l'algorithme de [**Tri Rapide**](https://guide.freecodecamp.org/algorithms/sorting-algorithms/quick-sort/) (bien sûr qu'il le fait !) pour trier les Pokémon.

En faisant cela, il n'utilise aucun espace supplémentaire et le temps pris pour trier les `N` Pokémon est le même que celui de l'algorithme de **Tri Fusion**. Donc, Pikachu est heureux que son ami l'aide au moment opportun.

Pikachu, étant extrêmement intelligent, invente une stratégie de recherche qui utilise la nature triée de la liste des Pokémon. Ce nouvel algorithme est connu sous le nom d'algorithme de [**Recherche Binaire**](https://guide.freecodecamp.org/miscellaneous/freecodecamp-algorithm-binary-search-guide/) (**Note** : Le tri est une condition préalable pour exécuter une recherche binaire, une fois la liste triée, Pikachu peut exécuter une recherche binaire autant de fois qu'il le souhaite sur cette liste triée).

Regardons le code de cet algorithme puis analysons sa complexité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d3K7llJtj5gl2RjITp0WAw.png)

Clairement, l'algorithme est récursif par nature. Voyons si nous pouvons utiliser nos nouveaux trucs pour analyser la complexité temporelle de l'algorithme de recherche binaire. Les deux variables `l` et `r` définissent essentiellement la portion du tableau dans laquelle nous devons rechercher l'élément donné, `x`.

Si nous regardons l'algorithme, tout ce qu'il fait vraiment est de diviser la portion de recherche du tableau d'entrée en deux. En plus de faire un appel récursif basé sur une certaine condition, il ne fait pas grand-chose. Donc, regardons rapidement la relation de récurrence pour l'algorithme de recherche binaire.

```
T(n) = T(n / 2) + O(1)
```

Cela semble être une relation de récurrence assez simple à analyser. D'abord, essayons d'analyser l'arbre de récursivité et d'en déduire la complexité, puis nous regarderons le théorème Maître et verrons lequel des trois cas correspond à cette récursion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U9jFamdwwGALXvS6eW2XNg.png)

Waouh ! Cet algorithme de recherche binaire est super rapide. Il est beaucoup plus rapide que la recherche linéaire. Ce que cela implique pour notre petit ami mignon Pikachu, c'est que pour 1000 Pokémon, il devrait simplement aller et « demander » **10** d'entre eux au maximum pour trouver le Pokémon spécial qu'il cherche (comment ? 🤓).

Maintenant, voyons comment la méthode plus « formulaire » d'approche de l'analyse de complexité récursive, c'est-à-dire la méthode Maître, peut nous aider dans ce cas. La relation récursive générique de la méthode Maître est

```
T(n) = a T(n / b) + f(n)
```

et pour notre algorithme de recherche binaire, nous avons

```
T(n) = T(n / 2) + O(1)
f(n) = O(n^0), donc c = 0
a = 1
b = 2
c = 0
```

Il y a 3 cas différents pour le théorème Maître et `c ? log_b(a)` décide lequel des trois cas est utilisé pour une analyse particulière. Dans notre cas, `0 < log_2(1)` c'est-à-dire `0 = 0`. Cela implique que notre algorithme de recherche binaire correspond au **cas-3** du théorème Maître, donc `T(n) = Θ(n^0 log(n)) = Θ(log(n)`

### Comment choisir le meilleur algorithme ? 🤨

Dans cet article, nous avons introduit l'idée de l'analyse de complexité qui est une partie importante de la conception et du développement d'algorithmes. Nous avons vu pourquoi l'analyse de la complexité d'un algorithme est importante et comment elle affecte directement nos décisions de scalabilité. Nous avons même vu quelques techniques géniales pour analyser cette complexité de manière efficace et correcte afin de prendre des décisions éclairées en temps opportun. La question se pose cependant,

**Étant donné tout ce que je sais sur les complexités temporelle et spatiale de deux algorithmes, comment choisir celui à utiliser finalement ? Y a-t-il une règle d'or ?**

La réponse à cette question, malheureusement, est **Non !**

Il n'y a pas de règle d'or pour vous aider à décider quel algorithme utiliser. Cela dépend totalement de nombreux facteurs externes. Essayons de regarder quelques-uns de ces scénarios dans lesquels vous pourriez vous trouver et voyons aussi le type de décisions que vous voudriez prendre.

#### Aucune contrainte sur l'espace !

Eh bien, si vous avez deux algorithmes A et B et que vous voulez décider lequel utiliser, en plus de la complexité temporelle, la complexité spatiale devient également un facteur important.

Cependant, étant donné que l'espace n'est pas un problème qui vous préoccupe, il est préférable d'opter pour l'algorithme qui a la capacité de réduire davantage la complexité temporelle, même avec plus d'espace.

Par exemple, le [Tri par Comptage](https://guide.freecodecamp.org/algorithms/sorting-algorithms/counting-sort) est un algorithme de tri en temps linéaire, mais il dépend fortement de la quantité d'espace disponible. Précisément, la _plage_ de nombres qu'il peut traiter dépend de la quantité d'espace disponible. Avec un espace illimité, vous êtes mieux loti en utilisant l'algorithme de tri par comptage pour trier une grande plage de nombres.

#### Exigence de latence sous-seconde et espace limité disponible

Si vous vous trouvez dans un tel scénario, il devient vraiment important de comprendre profondément la performance de l'algorithme sur de nombreuses entrées variées, surtout le type d'entrées que vous attendez de l'algorithme pour travailler dans votre application.

Par exemple, nous avons deux algorithmes de tri : le tri à bulles et le tri par insertion, et vous voulez décider lequel utiliser pour trier une liste d'utilisateurs en fonction de leur âge. Vous avez analysé le type d'entrée attendu et vous avez trouvé que le tableau d'entrée est **presque trié**. Dans un tel scénario, il est préférable d'utiliser le tri par insertion plutôt que le tri à bulles en raison de sa capacité inhérente à gérer de manière amazone les entrées presque triées.

#### Attendez, pourquoi quelqu'un utiliserait-il le tri à bulles ou le tri par insertion dans des scénarios réels ?

Si vous pensez que ces algorithmes sont juste à des fins éducatives et ne sont pas utilisés dans des scénarios réels, vous n'êtes pas seul ! Cependant, cela ne pourrait pas être plus éloigné de la vérité. Je suis sûr que vous avez tous utilisé la fonctionnalité `sort()` en Python à un moment donné dans votre carrière.

Eh bien, si vous l'avez utilisée et que vous avez été émerveillé par ses performances, vous avez utilisé un algorithme hybride basé sur le tri par insertion et le tri fusion appelé l'algorithme Tim Sort. Pour en savoir plus, rendez-vous ici :

[**Timsort — le plus rapide algorithme de tri que vous n'avez jamais entendu**](https://skerritt.blog/timsort-the-fastest-sorting-algorithm-youve-never-heard-of/)  
[_Timsort : Un algorithme de tri très rapide, O(n log n), stable, construit pour le monde réel — pas construit dans le milieu universitaire…_skerritt.blog](https://skerritt.blog/timsort-the-fastest-sorting-algorithm-youve-never-heard-of/)

Il est vrai que le tri par insertion peut ne pas être utile pour des entrées très grandes comme nous l'avons tous vu avec sa complexité temporelle polynomiale. Cependant, sa capacité inhérente à trier rapidement une plage de nombres _presque_ triée est ce qui le rend si spécial et c'est précisément la raison pour laquelle il est utilisé dans l'algorithme Timsort.

En bref, vous n'aurez jamais une division claire en noir et blanc entre les algorithmes parmi lesquels vous avez du mal à choisir. Vous devez analyser toutes les propriétés des algorithmes, y compris leur complexité temporelle et spatiale. Vous devez considérer la taille des entrées que vous attendez que votre algorithme traite et toute autre contrainte qui pourrait exister. En tenant compte de tous ces facteurs, vous devez prendre une décision éclairée !

> _Si vous avez passé un bon moment à comprendre les subtilités de l'analyse de complexité et à jouer avec notre ami Pikachu, n'oubliez pas de détruire ce bouton like et de répandre un peu d'amour. _❤️__  
>   
> _Si vous voulez plus de problèmes de programmation avec une analyse de complexité détaillée, rendez-vous dans notre [cuisine](https://github.com/DivyaGodayal/CoderChef-Kitchen)! _🍳__  
>   
> _Analyser un algorithme est une partie importante de l'ensemble des compétences de tout développeur et si vous pensez qu'il y a d'autres personnes qui pourraient bénéficier de cet article, alors partagez-le autant que possible!_