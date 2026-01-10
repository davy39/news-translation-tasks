---
title: Comment calculer la hauteur d'un arbre binaire en utilisant l'itération de
  tableau en Ruby
subtitle: ''
author: Ry Vee
co_authors: []
series: null
date: '2018-12-19T16:58:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-calculate-a-binary-trees-height-using-array-iteration-in-ruby-63551c6c65fe
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca73c740569d1a4ca75d1.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
seo_title: Comment calculer la hauteur d'un arbre binaire en utilisant l'itération
  de tableau en Ruby
seo_desc: 'Data structures and algorithms are the heart and soul of computer science
  and software. One cannot learn programming without understanding how data is organized
  in code and how to manipulate it.

  One such data structure is a binary tree:


  _Photo by [U...'
---

Les structures de données et les algorithmes sont le cœur et l'âme de l'informatique et des logiciels. On ne peut pas apprendre la programmation sans comprendre comment les données sont organisées dans le code et comment les manipuler.

Une telle structure de données est un arbre binaire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HItcyUcWWnuqDzKgNCoprw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/EwKXn5CapA4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jeremy Bishop</a> sur <a href="https://unsplash.com/search/photos/tree?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Oh non, pas ce genre d'arbre, je veux dire celui-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tsVyCA_zXrAh3LqTF4LHxw.png)
_.Figure 1 : Arbre binaire simple_

En termes simples, un arbre est un réseau de 'nœuds'. Un nœud est un objet dont les propriétés incluent les données elles-mêmes et des pointeurs vers ses 'enfants'. Pour un arbre binaire, le nombre maximum d'enfants que chaque nœud peut avoir est 2. Un arbre binaire aura un nœud racine et au plus deux enfants. Chaque enfant est simplement un pointeur vers un autre objet d'arbre ou il peut être nil. En utilisant un hachage, cela peut être visualisé comme :

```rb
arbre = {
 :data        => 1,
 :left_child  => [another_tree] || nil,
 :right_child => [another_tree_again] || nil
}
```

Avant de nous lancer dans les calculs de hauteur, trouvons d'abord quelques utilisations pour les arbres binaires.

Si vous observez les répertoires ou la structure de fichiers dans votre ordinateur, elle suit une structure d'arbre (bien que plus générale). Chaque dossier peut contenir des fichiers (les données) et un certain nombre d'autres répertoires (qui ne sont pas nécessairement des données en eux-mêmes mais plutôt des adresses de telles données contenues dans ces sous-répertoires). Il existe d'autres cas d'utilisation pour les arbres binaires qui sont mieux discutés par d'autres articles :

[**Sur Quora**](https://www.quora.com/What-are-some-practical-applications-of-binary-search-trees)

[**Stack Overflow**](https://stackoverflow.com/questions/2130416/what-are-the-applications-of-binary-trees)

Les arbres binaires sont un sujet vaste et il y a tant de choses que je pourrais écrire à leur sujet (comme les différentes façons de les parcourir — un futur article peut-être ?). Cependant, ici je vais être très spécifique — calculer la hauteur d'un arbre binaire.

La première chose à comprendre à ce sujet est que nous pouvons représenter un arbre binaire en utilisant un tableau. Mais même si c'est possible, il existe plusieurs façons de disposer chaque nœud et de les associer (en tant qu'élément dans un tableau) à leurs enfants gauche et droit respectifs.

Pour simplifier, nous utiliserons la méthode « breadth-first » pour aplatir l'arbre. En « breadth-first », nous plaçons les données contenues dans chaque nœud en commençant par la racine. Ensuite, nous passons au niveau inférieur suivant, en plaçant les données de chaque nœud de gauche à droite. Nous parcourons tous les niveaux jusqu'au plus bas.

Si un sous-arbre n'a pas d'enfant gauche ou droit, alors un tel enfant peut être représenté par 0, tant que le sous-arbre n'est pas au niveau le plus bas de l'arbre binaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G7zWkk-nosVTUQxqJLwYCw.jpeg)
_Figure 2 : Arbre binaire modifié de la Figure 1._

```rb
arbre = [1, 7, 5, 2, 6, 0, 9, 3, 7, 5, 11, 0, 0, 4, 0] (T0)* représentation de tableau de la Figure 2
```

Numériquement, nous pouvons calculer les positions des enfants gauche et droit de chaque nœud :

```rb
enfant gauche de arbre[i] est à l'index 2*i + 1 (T1)
enfant droit de arbre[i] est à l'index 2*i + 2 (T2)
```

Comme nous pouvons le voir sur la figure 2, nous pouvons dire à quel point un arbre est grand — c'est-à-dire que nous devons simplement compter combien de nœuds il y a de la racine jusqu'à l'élément le plus bas (y compris la racine et l'élément le plus bas) le long de la branche la plus longue. Mais lorsqu'il est déjà sous forme de tableau, comment savons-nous à quel point il est grand ?

Tout d'abord, nous devons avoir une formule générale pour la hauteur de n'importe quel arbre :

```rb
hauteur = 1 + max(hauteur_enfant_gauche, hauteur_enfant_droit) (T3)
```

Pour les arbres multiniveaux, nous pouvons alors conclure que pour calculer la hauteur de n'importe quel sous-arbre (et de l'arbre lui-même), nous devons d'abord calculer les hauteurs des enfants gauche et droit, puis trouver la plus grande des deux. En calculant les hauteurs de ces deux enfants, nous devons calculer les hauteurs de leurs enfants respectifs, et ainsi de suite.

Ayant cela, nous pouvons maintenant commencer à esquisser un algorithme pour calculer la hauteur des arbres binaires multiniveaux. Il existe deux méthodes que nous pouvons suivre, l'une consiste à utiliser des itérations ou des boucles, et l'autre, en raison de la nature répétitive des étapes (paragraphe précédent), consiste à utiliser la récursivité. Je vais suivre cet article avec une discussion sur la façon d'utiliser la récursivité pour faire cela. Cependant, ce serait trop facile. Alors apprenons d'abord la manière difficile : nous allons faire cela en utilisant l'itération.

#### Méthode itérative

Nous allons utiliser le tableau d'arbre `T0` ci-dessus pour illustrer ce processus

**Étape 0 :** Déclarer un tableau de hauteurs qui stockera les hauteurs de chaque sous-arbre.

```rb
hauteurs = [] (S0.1)
```

**Étape 1 :** Parcourir le tableau — puisque nous devons calculer les hauteurs des descendants en premier, nous parcourons à partir du dernier élément. Et au lieu d'utiliser la méthode `each` directement dans le tableau d'arbre, nous allons l'utiliser pour les indices de chaque élément.

```rb
(tree.length - 1).downto(0) do |i| (S1.1)
```

**Étape 2 :** Pour chaque élément, trouver la hauteur initiale — si l'élément est zéro (ce qui signifie qu'il s'agit en fait d'un nœud nil), alors la hauteur initiale est 0, sinon elle est 1.

```rb
hauteur_initiale = arbre[i] == 0 ? 0 : 1 (S2.1)
```

**Étape 3 :** Trouver la hauteur de l'enfant gauche — à l'intérieur du tableau `hauteurs`, si l'élément a un enfant gauche, alors la hauteur de cet enfant est égale à :

```rb
hauteur_enfant_gauche = hauteurs[left_child_index] (S3.1)
```

Dans ce qui précède, l'`left_child_index` peut être calculé comme suit :

```rb
left_child_index = hauteurs.length - i - 1 (S3.2)
```

J'ai élaboré `S3.2` par un peu d'essais et d'erreurs. Dans la simulation qui suivra cette série d'étapes, je mentionnerai cela.

Pour résumer, j'avais initialement l'intention de `unshift` chaque hauteur de descendant dans `hauteurs` afin que les hauteurs de chaque élément aient les mêmes indices que l'élément lui-même a sur `arbres`. Mais comme je le noterai plus tard, utiliser unshift pour cela sera coûteux en ressources pour les grandes entrées de tableau.

J'ai donc décidé d'utiliser `push`. Chaque hauteur sera alors ordonnée à l'envers par rapport à l'ordre de leurs éléments correspondants dans `arbre`. Ainsi, la hauteur, disons de `arbre[0]`, se trouvera finalement dans `hauteurs[-1]`.

Si l'élément en question n'a pas d'enfant gauche, alors `left_child_index` devrait être `nil`. Pour nous assurer que nous capturons ce scénario :

```rb
left_child_index = nil if arbre[2*i + 1].nil? (S3.3)
```

En combinant `S3.2` et `S3.3` en utilisant un ternaire :

```rb
left_child_index = arbre[2*i + 1].nil? ? nil : hauteurs.length - i -1 (S3.4)
```

Par conséquent, la hauteur de l'enfant gauche devra être 0 si l'enfant gauche est `nil`. La formule complète pour `hauteur_enfant_gauche` est alors :

```rb
hauteur_enfant_gauche = left_child_index.nil? ? 0 : hauteurs[left_child_index] (S3.5)
```

**Étape 4 :** Trouver la hauteur de l'enfant droit — trouver la hauteur de l'enfant droit d'un sous-arbre suit la même logique que l'Étape 3. Puisque nous remplissons le tableau `hauteurs` de gauche à droite (en utilisant `push`) et que nous parcourons `arbre` de droite à gauche, la hauteur de l'enfant droit de n'importe quel sous-arbre sera toujours poussée en premier dans `hauteurs`. Par conséquent, l'enfant gauche de n'importe quel élément sera à la position `left_child_index -1` à l'intérieur de `hauteurs` (si l'enfant droit n'est pas `nil` dans `arbre`). En tenant compte de ces éléments et en suivant la logique de l'Étape 3 :

```
right_child_index = arbre[2*i + 2].nil? nil : left_child_index - 1 (S4.1)
```

```rb
hauteur_enfant_droit = right_child_index.nil? ? 0 : hauteurs[right_child_index] (S4.2)
```

**Étape 5 :** Trouver la hauteur totale de l'élément — Après avoir trouvé les hauteurs des enfants gauche et droit de l'élément en question (à l'index `i` dans `arbre`), nous pouvons maintenant trouver la hauteur totale de cet élément :

```rb
hauteur_totale = hauteur_initiale + [hauteur_enfant_gauche, hauteur_enfant_droit].max (S5.1)
```

Numériquement parlant, si l'élément est 0 et qu'il arrive à avoir un ou des enfants à l'intérieur de l'arbre, alors ces enfants seront également 0. Par conséquent, sa `hauteur_totale` sera également 0. Tel est le cas avec l'élément à `i = 5` dans `T0` ci-dessus :

```rb
                                         gauche  droite
                                         enfant enfant
arbre = [1, 7, 5, 2, 6, 0,  9, 3, 7, 5, 11, 0,   0,   4, 0] 
                      i=5                i=11 i=12
                  élément en question
(T0 ici répété)
hauteur_totale = 0 + [0,0].max = 0 (S5.2)
```

Mais pour l'élément à `i = 4`, la hauteur est :

```rb
                                    gauche   droite
                                    enfant  enfant
arbre = [1, 7, 5, 2, 6, 0,  9, 3, 7,   5,    11,     0, 0, 4, 0] 
                   i=4               i=9  i=10
                  élément 
                 en question
hauteur_totale = 1 + [1,1].max = 2 (S5.3)
```

Dans `S5.3` et `S5.4` ci-dessus, nous avons simplement utilisé une inspection visuelle pour calculer les hauteurs des enfants droit et gauche de l'élément en question. Mais cela illustre comment notre algorithme fonctionne. Maintenant, après avoir calculé la `hauteur_totale`, nous faisons simplement :

**Étape 6 :** Pousser `hauteur_totale` dans `hauteurs` — Comme je l'ai noté précédemment, utiliser la méthode push est plus efficace, surtout pour les grands tableaux.

```rb
hauteurs.push(hauteur_totale) (S6.1)
```

Une fois que nous avons parcouru tous les éléments du tableau `arbre`, nous aurons un tableau `hauteurs` composé des hauteurs de chaque sous-arbre dans l'arbre binaire. Il devrait ressembler à ceci :

```rb
hauteurs(après itération complète) = [0, 1, 0, 0, 1, 1, 1, 1, 2, 0, 2, 2, 3, 3, 4] (S6.2)
```

**Étape 7 :** Retourner la hauteur de l'arbre binaire — Si notre objectif est simplement de trouver la hauteur de l'arbre mère (c'est-à-dire de la racine jusqu'au nœud le plus bas et le plus à droite), alors nous faisons simplement :

```rb
return hauteurs[-1] (S7.1)
*Note si c'est la dernière ligne de la méthode, alors le mot-clé 'return' est redondant (en Ruby au moins)
```

Cependant, souvent nous pouvons être intéressés à calculer les hauteurs de n'importe lequel des sous-arbres. Dans ce cas, nous retournons simplement le tableau `hauteurs` lui-même et ensuite toute personne utilisant le programme peut simplement inclure n'importe quel index pour trouver la hauteur d'une branche spécifique dans l'arbre.

La méthode complète ci-dessous :

```rb
def hauteur_arbre_binaire(tableau_arbre)
  #0 Déclarer un tableau de hauteurs qui stockera les hauteurs de chaque sous-arbre
  hauteurs = []
  #1 Parcourir le tableau_arbre en commençant par le dernier élément jusqu'au premier
  (tableau_arbre.length - 1).downto(0) do |i|
  
  #2 Pour chaque élément, trouver la hauteur initiale
  hauteur_initiale = tableau_arbre[i] == 0 ? 0 : 1
  
  # 3 Trouver la hauteur de l'enfant gauche
  left_child_index = tableau_arbre[2*i + 1].nil? ? nil : hauteurs.length - i - 1 #index de la hauteur de l'enfant gauche dans hauteurs
  hauteur_enfant_gauche = left_child_index.nil? ? 0 : hauteurs[left_child_index] 
  
  # 4 Trouver la hauteur de l'enfant droit
  right_child_index = tableau_arbre[2*i + 2].nil? ? nil : left_child_index - 1 #index de la hauteur de l'enfant droit dans hauteurs
  hauteur_enfant_droit = right_child_index.nil? ? 0 : hauteurs[right_child_index]
  
  # 5 Trouver la hauteur totale de l'élément
  hauteur_totale = hauteur_initiale + [hauteur_enfant_gauche,hauteur_enfant_droit].max
    
  # 6 Pousser la hauteur totale dans le tableau des hauteurs
  hauteurs.push(hauteur_totale)
    
 end
 puts hauteurs[-1]
end

```

Testons cet algorithme.

Supposons que nous exécutons `hauteur_arbre_binaire(arbre)`. Calculer les hauteurs de `arbre[14]` à `arbre[7]` est assez simple (elles seront soit 0 soit 1 puisqu'elles sont toutes au niveau le plus bas de `arbre`), donc nous ne les simulerons plus ici. Nous supposerons que nous sommes déjà à cette partie de l'itération lorsque `i` sera égal à 6. Par conséquent, à ce stade :

```rb
i = 6 (F1)
arbre[6] = 9 (F2)
hauteurs = [0, 1, 0, 0, 1, 1, 1, 1] (hauteurs.length à ce point est 8) (F3)
```

Maintenant, nous pouvons voir que `arbre[6]` est égal à 9 (et non 0). Par conséquent :

```
hauteur_initiale = 1 (F4)
```

Comme promis, voici comment j'ai élaboré la formule pour les indices des enfants gauche et droit.

J'ai commencé avec un tableau `hauteurs` déjà rempli avec les hauteurs des éléments les plus bas comme montré dans `F3`. Puisque je travaille maintenant avec `arbre[6]` (qui est 9), ses enfants gauche et droit sont `arbre[13]` et `arbre[14]` ; dont les hauteurs correspondantes sont dans `hauteurs[1]` et `hauteurs[0]`, respectivement. Si ce n'est pas assez clair, nous savons que nous commençons à pousser à partir de `arbre[14]` — cela deviendra `hauteurs[0]`. Nous calculons ensuite et poussons la hauteur de `arbre[13]` — cela sera `hauteurs[1]`. En reliant les indices :

```rb
index de l'enfant gauche dans arbres = 13
index de la hauteur de l'enfant gauche dans hauteurs = LEFT_INDEX =1
index de l'enfant droit dans arbres = 14
index de la hauteur de l'enfant droit dans hauteurs = RIGHT_INDEX = 0
index actuel de l'élément en question = MOTHER_INDEX = 6
longueur actuelle du tableau hauteurs = LENGTH = 8
LEFT_INDEX = 1 = 8 - 6 - 1 = LENGTH - MOTHER_INDEX - 1
RIGHT_INDEX = 0 = 8 - 6 - 2 = LENGTH - MOTHER_INDEX - 2 
(ou simplement LEFT_INDEX -1 ) (F5)
```

Nous pouvons maintenant appliquer cette logique à tous les éléments, donc dans le code nous calculons la hauteur de `arbre[6]` comme suit :

```rb
Calcul de la hauteur de l'enfant gauche de arbre[6] :
à partir du code à S3.4 :
left_child_index = arbre[2*i + 1].nil? ? nil : hauteurs.length - i - 1
Puisque arbre[2*6 + 1] = arbre[13] = 4 n'est pas nil alors :
left_child_index = 8 - 6 - 1 = 1
à partir du code à S3.5 :
hauteur_enfant_gauche = left_child_index.nil? ? 0 : hauteurs[left_child_index]
Donc alors :
hauteur_enfant_gauche = hauteurs[1] = 1
```

Suivant la même logique pour la hauteur de l'enfant droit de `arbre[6]` :

```rb
à partir du code à S4.1 :
right_child_index = arbre[2*i + 2].nil? nil : left_child_index - 1 
Puisque arbre[2*6 + 2] = arbre[14] = 4 et n'est pas nil :
right_child_index = left_child_index -1 = 1 -1 = 0 -> !nil?
et à partir du code à S4.2 :
hauteur_enfant_droit = right_child_index.nil? ? 0 : hauteurs[right_child_index]
Par conséquent : hauteur_enfant_droit = hauteurs[0] = 0
```

Maintenant, nous pouvons trouver la hauteur totale de `arbre[6]` :

```rb
hauteur_totale (arbre[6]) = 1 + [1,0].max = 1 + 1 = 2
```

Nous pouvons alors pousser cette `hauteur_totale` dans `hauteurs` :

```rb
hauteurs.push(2), de sorte que :
```

```rb
hauteurs = [0, 1, 0, 0, 1, 1, 1, 1, 2]
```

Et la même chose continue jusqu'à ce que nous travaillons sur `arbre[0]` et le tableau final `hauteurs` devrait être :

```rb
hauteurs = [0, 1, 0, 0, 1, 1, 1, 1, 2, 0, 2, 2, 3, 3, 4]
```

Et en retournant `hauteurs[-1]` (ou `hauteurs[hauteurs.length -1]`, selon ce que nous préférons), nous déterminons que la hauteur de `arbre` est **4**. Nous pouvons vérifier cela visuellement dans les figures 1 et 2 ci-dessus.

Il nous a fallu 7 étapes pour obtenir la réponse. Avec cette taille de tableau `arbre`, l'opération a pris environ 0,024 millisecondes pour se terminer. Il faut la moitié du temps (seulement 0,012 millisecondes) pour accomplir la même chose en utilisant la récursivité.

En avant-première sur la façon de faire cela de manière récursive, nous pouvons simplement faire quelque chose comme :

```rb
def hauteur_arbre_recursive(tableau_arbre, index = 0)
  return 0 if tableau_arbre[index].nil? or tableau_arbre[index] == 0
  hauteur_enfant_gauche = hauteur_arbre_recursive(tableau_arbre, 2*index + 1)
  hauteur_enfant_droit = hauteur_arbre_recursive(tableau_arbre, 2*index +2)
  hauteur_totale = 1 + [hauteur_enfant_gauche, hauteur_enfant_droit].max
end
```

Nous voyons que la récursivité ne nous prendra probablement que 4 étapes au maximum pour accomplir la même tâche. Et cela nous fait économiser la moitié du temps et moins de ressources utilisées.

Un secret pour apprendre les algorithmes est le travail acharné et la pratique. Cela aide également si vous travaillez en collaboration avec d'autres. Je n'ai pas fait ce qui précède seul mais avec mon partenaire de codage. J'ai [précédemment écrit](https://hackernoon.com/how-five-weeks-of-remote-pair-programming-helped-me-build-strong-habits-e0493c9ba780) sur la façon dont apprendre de cette manière est tellement plus productif et efficace.

Voici mon [dépôt](https://github.com/rvvergara/data-structures) sur les différentes structures de données et algorithmes sur lesquels j'ai travaillé.

**Suivez-moi** sur [**Twitter**](https://twitter.com/coachryanv) | [**Github**](https://github.com/rvvergara)