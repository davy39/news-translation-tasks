---
title: 'Une introduction aux arbres en programmation : l''oxygène du codage efficace'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T18:25:19.000Z'
originalURL: https://freecodecamp.org/news/trees-in-programming-the-oxygen-of-efficient-code-6c7c11a3dd64
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yupSzA97Mon4gDQ1UzlbsA.png
tags:
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Une introduction aux arbres en programmation : l''oxygène du codage efficace'
seo_desc: 'By Tiago Antunes

  Many times you wish to save information in your program and access it many times.
  And you’ll often store it in a very simple data structure: an array. And it often
  works really well! But sometimes it just takes a lot of time to finis...'
---

Par Tiago Antunes

De nombreuses fois, vous souhaitez sauvegarder des informations dans votre programme et y accéder plusieurs fois. Et vous les stockez souvent dans une structure de données très simple : un tableau. Et cela fonctionne souvent très bien ! Mais parfois, cela prend juste **beaucoup** de temps pour se terminer.

Ainsi, pour optimiser ce type de programme, de nombreuses personnes intelligentes ont développé des choses étranges que nous appelons **structures de données**. Aujourd'hui, je vais aborder quelques bases sur ce sujet, et je vais discuter d'une structure spécifique qui est souvent demandée lors des entretiens de codage et qui rend tout le monde fou : les Arbres.

Je ne vais pas plonger beaucoup dans le code, seulement dans la théorie de comment tout fonctionne. Il y a des millions d'exemples de code en ligne, alors regardez-en un après avoir compris comment fonctionnent les arbres !

![Image](https://cdn-media-1.freecodecamp.org/images/kN9uEnU437d1O1pcz8DzlWjz3wjqyJuxJah0)
_Oui... Lequel ?_

### Alors, qu'est-ce qu'une structure de données vraiment ?

Selon Wikipedia :

> « une **structure de données** est une organisation et un format de stockage de données qui permet un accès et une modification [efficaces](https://en.wikipedia.org/wiki/Algorithmic_efficiency) »

Cela signifie essentiellement qu'il ne s'agit de rien de plus que de code écrit pour créer une manière complexe de stocker des données. Il existe de nombreuses structures de données que vous pouvez implémenter, et chacune a une tâche spécifique. Elles peuvent aller de structures très simples — comme les listes chaînées — à des structures vraiment complexes — comme les graphes.

Les arbres sont suffisamment complexes pour être vraiment rapides dans ce qu'ils font, mais suffisamment simples pour être compréhensibles. Et une chose dans laquelle ils excellent est la recherche de valeurs avec une utilisation minimale de la mémoire.

### Mais comment mesurez-vous l'efficacité d'une structure de données ?

Avez-vous déjà vu en ligne une notation étrange que les gens utilisent comme O(n) ? Cela s'appelle la notation Big O, et c'est la manière standard d'évaluer les performances des structures et des algorithmes. Le grand O que nous utilisons est la représentation du scénario du pire cas : avoir quelque chose qui est O(n) (avec **n** étant le nombre d'éléments à l'intérieur) signifie que dans le pire des cas, cela prend un temps **n**, ce qui est vraiment bien.

À l'intérieur des parenthèses, nous avons écrit **n** ce qui est équivalent à écrire l'expression `y = x →`. Cela évolue proportionnellement. Mais parfois nous avons différentes expressions :

* O(1)
* O(log(n))
* O(n)
* O(n²)
* O(n³)
* O(n!)
* O(e^n)

Plus le résultat d'une fonction est faible, plus une structure est efficace. Il existe plusieurs types d'arbres. Nous allons parler des BST (Binary-Search Trees) et des AVL Trees (arbres auto-équilibrés) qui ont différentes propriétés :

![Image](https://cdn-media-1.freecodecamp.org/images/Yv-dffABeNKNVMXCEwjPU7tSrLoNILfBnHk7)
_Comme vous pouvez le voir, les arbres AVL sont beaucoup plus efficaces, mais beaucoup plus complexes !_

### D'accord, vous avez parlé de toute cette notation étrange... alors comment fonctionnent les arbres ?

Le nom arbre vient de sa représentation réelle : il a une racine, des feuilles et des branches, et est souvent représenté comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Kan51et5e844FH0GbUNDMl8R2Hyb2Ck1-1xB)
_Remarquez comment 6 n'est pas une feuille car il n'est pas à la fin d'une branche !_

Il y a quelques dénominations que nous utilisons, notamment parent et enfant, qui ont une relation unique. Si **x** est le parent de **y**, alors **y** est l'enfant de **x**. Dans cette image, 2 est le parent de 5, puis 5 est l'enfant de 2. Chaque nœud — chaque position avec une valeur — ne peut avoir qu'un seul parent et deux enfants.

Mais en plus de tout cela, il n'y a pas de motif qui est suivi, donc cet arbre n'est pas vraiment très utile... Nous devrions donc ajouter quelques règles supplémentaires pour faire une bonne structure de données.

#### Arbres de recherche binaire

C'est là que les arbres de recherche binaire entrent en jeu ! Au lieu de simplement placer des nœuds enfants de manière aléatoire, ils suivent un ordre spécifique :

* S'il n'y a pas de nœuds, alors la première valeur entrée devient la **racine** de l'arbre.
* S'il y a des nœuds, alors l'insertion suit les étapes suivantes : en commençant par la racine, si la valeur que vous entrez est plus petite que le nœud actuel, passez par la branche de gauche, sinon passez par celle de droite. Si vous êtes dans un endroit vide, c'est là que votre valeur appartient !

Cela peut sembler un peu confus au début, mais écrivons un peu de pseudo-code pour le simplifier :

```
//Ce code ne compilera dans aucun langage (que je sache) et ne sert qu'à démontrer à quoi ressemblerait le code
```

```
def insert(Node n, int v) {    if n is NULL:        return createNode(v)    else if n.value < v:        n.right = insert(n.right, v)    else:        n.left = insert(n.left, v)    return n}
```

Maintenant, que se passe-t-il ici ? D'abord, nous vérifions si l'endroit où nous nous trouvons maintenant est vide. Si c'est le cas, nous créons un nœud à cet endroit avec la fonction `createNode`. Si ce n'est pas vide, alors nous devons voir où nous devons placer notre nœud.

Cette démonstration montre comment cela fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/vGugwFtmjnxPoUkwaz4eMfXCyeeR3NfDqAid)
_Source : [http://www.mathwarehouse.com/programming/gifs/binary-search-tree.php](http://www.mathwarehouse.com/programming/gifs/binary-search-tree.php" rel="noopener" target="_blank" title=")_

De cette manière, nous pouvons rechercher n'importe quelle valeur dans l'arbre sans avoir à parcourir tous les nœuds. Super !

Mais cela ne se passe pas toujours aussi bien que dans le gif ci-dessus. Et si nous obtenions quelque chose comme ceci ?

![Image](https://cdn-media-1.freecodecamp.org/images/9Ws05JR1XZhWP2S7Sq1oTQsBSDBow4oMUNCl)
_Oups, scénario du pire cas !_

Dans ce cas, le comportement de l'arbre vous fait parcourir tous les nœuds. C'est pourquoi l'efficacité du pire cas d'un BST est de O(n), ce qui le rend lent. Supprimer d'un BST est également facile :

* Si un nœud n'a pas d'enfants → supprimez le nœud
* Si un nœud a un enfant → connectez le nœud parent à son nœud petit-enfant et supprimez le nœud
* Si un nœud a 2 enfants → substituez le nœud par son plus grand enfant (l'enfant le plus à droite à gauche) → voir l'image ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/5FzpxzchOVtImfMifRlVUi2fgao-0NnMAzvW)
_La suppression du nombre 12 se fait par substitution de 12 par 9_

Maintenant, vous savez tout ce que vous devez savoir sur les BST. Plutôt cool, non ?

### Mais que feriez-vous si vous vouliez **TOUJOURS** avoir un arbre efficace ?

Si vous avez cette nécessité, les arbres AVL peuvent le faire pour vous très bien. En échange, ils sont des millions de fois plus complexes que les BST, mais suivent la même organisation qu'avant.

Un arbre AVL est un arbre auto-équilibré qui a des opérations spécifiques (appelées rotations) qui permettent à l'arbre de rester **équilibré**. Cela signifie que chaque nœud dans l'arbre aura une différence de **hauteur** entre ses deux branches enfants d'au maximum 1.

Avec cela, l'arbre aura toujours une hauteur de log(n) (n étant le nombre d'éléments) et cela vous permet de rechercher des éléments de manière vraiment efficace.

![Image](https://cdn-media-1.freecodecamp.org/images/UM1ijtzuMAJwnE0T47fU9ip84GDmF81nYBwC)
_Il y a 11 éléments et la hauteur est de 4. Cela signifie que le programme ferait au plus 4 recherches vers le bas ! C'est vraiment efficace car chaque niveau vers le bas contient le double du nombre d'éléments de son niveau supérieur_

Maintenant, vous voyez à quel point les arbres équilibrés sont bons et parfaits. Mais comment les créer est la vraie question. J'ai mentionné le mot **profondeur** auparavant, alors comprenons d'abord cela.

![Image](https://cdn-media-1.freecodecamp.org/images/95E-aGZFvGqAVy8BXaXga6fI-3Neol-5SQGV)
_Une feuille a une hauteur de 0 et un nœud non-feuille a une hauteur égale au maximum de ses enfants plus 1_

La hauteur est ce qui nous permet de comprendre si notre arbre est équilibré ou non. Et avec elle, nous sommes capables de déterminer où se trouve le problème et d'appliquer les fonctions d'équilibrage : **rotations**. Ce sont des fonctions vraiment simples qui consistent à échanger des nœuds entre eux afin de supprimer la différence de hauteur, mais elles peuvent sembler vraiment étranges au premier abord.

Il y a 4 opérations :

* Rotation à gauche
* Rotation à droite
* Rotation gauche-droite
* Rotation droite-gauche

![Image](https://cdn-media-1.freecodecamp.org/images/gsNUXSbb3fP-OXM8Z9rLc1MW-Sfqiz7MljHP)
_Le nœud où la hauteur des enfants était supérieure à 1 subit une rotation (imaginez un espace vide avec une hauteur de -1, si vous le calculez : balance(6) = 1 - -1 = 2)_

### Wow, c'était étrange... comment fonctionnent les rotations ?

Les rotations sont étranges au premier abord, et je suggère de regarder quelques animations de leur fonctionnement.

Essayez avec vos propres arbres sur ce site : [https://www.cs.usfca.edu/~galles/visualization/AVLtree.html](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html)

Il vous permet de voir dynamiquement les rotations se produire et est un excellent outil ! Il n'y a que quatre cas, donc les comprendre sera facile.

![Image](https://cdn-media-1.freecodecamp.org/images/8A62BNYoUXowG9koNOoAROgeQubxvXWHPUqM)
_Rotation Droite-Gauche. Ce n'est rien de plus que 2 rotations de base !_

### C'est tout pour maintenant !

Les arbres sont assez faciles à comprendre, et avec de la pratique, vous pouvez travailler avec eux facilement. Les appliquer dans votre code est une clé majeure pour rendre vos programmes beaucoup plus efficaces.

Si vous avez des questions sur quelque chose que vous n'avez pas compris, que vous n'êtes pas d'accord avec, ou que vous aimeriez suggérer, n'hésitez pas à me contacter via [Twitter](https://twitter.com/tm_antunes) ou par email !

Email : tiago.melo.antunes [at] tecnico [dot] ulisboa [dot] pt