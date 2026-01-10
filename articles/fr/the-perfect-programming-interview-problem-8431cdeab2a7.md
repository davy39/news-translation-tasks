---
title: Le problème d'entretien de programmation parfait
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T23:03:02.000Z'
originalURL: https://freecodecamp.org/news/the-perfect-programming-interview-problem-8431cdeab2a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ovq-JmKB2jLyBO8wAa6V3Q.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Le problème d'entretien de programmation parfait
seo_desc: 'By Sachin Malhotra

  Programming Interviews are hard!

  Telephone screening interviews are a bit easier than the traditional onsite whiteboard
  interviews. The whiteboard interviews involve a whole lot of pressure and anxiety
  due to the lack of a code edi...'
---

Par Sachin Malhotra

Les entretiens de programmation sont difficiles !

Les entretiens de dépistage téléphonique sont un peu plus faciles que les entretiens traditionnels sur tableau blanc. Les entretiens sur tableau blanc impliquent beaucoup de pression et d'anxiété en raison de l'absence d'un éditeur de code pour coder. Ce que ces entretiens ont en commun, ce sont les types de compétences qu'ils testent.

Habituellement, un entretien de programmation impliquera un défi de programmation. Le candidat doit travailler dessus pendant toute la durée de l'entretien. Le temps alloué est généralement de 30 à 35 minutes. Les 10 premières minutes sont prises par les introductions et autres choses.

Étant donné un problème de programmation, l'intervieweur veut généralement que le candidat :

1. **Donne une solution fonctionnelle**
   Trouve une solution fonctionnelle pour le problème. Cela peut être une solution de force brute pour commencer. Le critère est que le candidat doit être capable de coder un programme syntaxiquement correct pour l'algorithme dans ce court laps de temps.
2. **Pose des questions de clarification**
   Pose des questions pour clarifier les choses qui ont été intentionnellement omises.
   → Quelle est la taille de l'entrée ?
   → Combien de nombres peuvent être dans le tableau ?
   → Quelle est la taille de l'alphabet pour la chaîne donnée ?
   → Peut-on utiliser de la mémoire supplémentaire ?
   → Peut-on modifier l'entrée donnée ou est-elle en lecture seule ?
3. **Code syntaxiquement correct** Une fois que l'intervieweur est convaincu de la solution que le candidat décrit, il est attendu qu'il écrive une solution fonctionnelle pour le problème. Dans un entretien sur tableau blanc, cette solution doit être écrite sur le tableau blanc. Le tableau blanc n'a évidemment aucune correction de syntaxe ! C'est ce qui le rend vraiment difficile.
4. **Trouve de meilleures solutions**
   Si vous ne présentez qu'une solution de force brute à l'intervieweur pour briser le silence gênant, il vous demandera plus souvent qu'autrement de trouver une meilleure solution. À moins que ce ne soit votre jour de chance et que l'intervieweur soit convaincu par la solution que vous avez proposée ?. Le genre de questions de suivi qu'ils posent généralement sont :
   → Pouvez-vous trouver une meilleure solution ? O(logn) → O(n)
   → Pouvez-vous rendre votre solution plus efficace en termes d'espace ? O(1) espace.
5. **Cas limites**
   Même si vous avez pu trouver une solution optimale et fonctionnelle pour le problème, il est possible que vous ayez manqué quelques cas limites. Vous avez peut-être manqué quelques scénarios qui ne changent pas l'algorithme. Ils peuvent affecter l'implémentation. Un candidat est censé effectuer des exécutions à sec approfondies avec le code après l'avoir écrit. Vous êtes censé essayer quelques cas de test pour trouver tout problème qu'ils pourraient avoir laissé dans leur code.
6. **Analyse de complexité**
   Si vous avez encore du temps restant dans votre entretien et que l'intervieweur semble satisfait du code que vous avez produit, il pourrait vous demander la complexité temporelle et spatiale de votre solution. Par conséquent, l'analyse de complexité est également un ensemble de compétences critiques requis pour réussir ces entretiens de programmation.

Oui, c'est effectivement écrasant.

Cet article ne traite pas vraiment des astuces et conseils pour préparer et passer un entretien de programmation. Il existe de nombreux bons articles à ce sujet. Si vous êtes venu ici à la recherche de quelques conseils généraux, je voudrais vous rediriger vers certains de mes articles préférés.

[**5 choses que vous devez savoir dans un entretien de programmation**](https://medium.freecodecamp.org/the-most-important-things-you-need-to-know-for-a-programming-interview-3429ac2454b)
[_Cet article est destiné à ceux qui essaient de commencer leur carrière en programmation, ou se préparent à passer un entretien pour..._medium.freecodecamp.org](https://medium.freecodecamp.org/the-most-important-things-you-need-to-know-for-a-programming-interview-3429ac2454b)[**Le guide de 30 minutes pour réussir votre prochain entretien de codage**](https://medium.freecodecamp.org/coding-interviews-for-dummies-5e048933b82b)
[_Comment je me suis amélioré dans les entretiens de codage et j'ai reçu des offres des grandes entreprises technologiques._medium.freecodecamp.org](https://medium.freecodecamp.org/coding-interviews-for-dummies-5e048933b82b)

Je suis récemment tombé sur un problème de programmation que je devais résoudre dans un délai d'1 heure. Il faisait partie d'un concours de programmation organisé sur [Leetcode.](https://leetcode.com) J'ai trouvé ce problème être un excellent candidat pour être posé lors d'un entretien de programmation. Je vais passer en revue le problème en détail ici et discuter de mes raisons pour lesquelles c'est un bon problème d'entretien. Je vais faire de mon mieux pour essayer de le relier aux points mentionnés précédemment.

#### Table des matières

* [? Jouons aux Serpents et Échelles](https://medium.com/p/8431cdeab2a7#a667)
* [Ressemble à un problème typique de Programmation Dynamique](https://medium.com/p/8431cdeab2a7#0028)
* [Modèle de Graphe](https://medium.com/p/8431cdeab2a7#838c)
* [Le Défaut dans la formulation DP](https://medium.com/p/8431cdeab2a7#b56d)
* [Formulation DP mise à jour](https://medium.com/p/8431cdeab2a7#9ed1)
* [La Recherche en Largeur à la Rescue! ⚡](https://medium.com/p/8431cdeab2a7#8720)
* [Mappage de la Valeur de Cellule à la Ligne et Colonne ?](https://medium.com/p/8431cdeab2a7#9ab1)
* [Valeurs de Cellule Problématiques ?](https://medium.com/p/8431cdeab2a7#5724)
* [Faire un mouvement par Serpent ?](https://medium.com/p/8431cdeab2a7#1546)
* [Pouvons-nous nous débarrasser de la chose "direction" ? ?](https://medium.com/p/8431cdeab2a7#a68e)
* [Mappage dans l'autre sens](https://medium.com/p/8431cdeab2a7#6afa)
* [Pourquoi est-ce encore le meilleur problème d'entretien de programmation ?](https://medium.com/p/8431cdeab2a7#ce03)

### ? Jouons aux Serpents et Échelles

Cette question faisait partie d'un récent concours de programmation hebdomadaire organisé sur [LeetCode](https://medium.com/@BlogLeetCode). C'est un concours de 1,5 heure avec 4 défis de programmation de difficulté variable. Celui-ci était marqué comme un problème de difficulté moyenne. Pouvoir le résoudre dans le délai imparti est une grande chose comme vous le réaliserez après avoir lu l'article.

Pour votre information, je n'ai pas pu ?

[**Serpents et Échelles - LeetCode**](https://leetcode.com/problems/snakes-and-ladders/description/)
[_Améliorez vos compétences en codage et trouvez rapidement un emploi. C'est le meilleur endroit pour développer vos connaissances et vous préparer..._leetcode.com](https://leetcode.com/problems/snakes-and-ladders/description/)

C'est une grande question et je vous encourage définitivement à la lire avant de continuer.

La partie du problème sur laquelle je veux que vous vous concentriez est la suivante :

> Retournez le nombre minimum de mouvements nécessaires pour atteindre la case N*N. Si ce n'est pas possible, retournez `-1`.

### Ressemble à un problème typique de Programmation Dynamique

Ou pas ?

Si vous avez pratiqué les problèmes de programmation dynamique pendant un certain temps, il devrait être évident que les énoncés de problèmes similaires à celui ci-dessus emploient généralement le paradigme de la programmation dynamique.

La raison pour laquelle nous disons cela est qu'un problème doit avoir certaines caractéristiques pour être résoluble en utilisant la programmation dynamique.

1. Le problème doit être **divisable en sous-problèmes plus petits**. Les sous-problèmes peuvent être utilisés pour résoudre le problème principal. Les solutions optimales aux sous-problèmes devraient nous aider à trouver la solution optimale au problème principal. Cela signifie qu'un problème doit être résoluble **récursivement**.
2. La deuxième propriété la plus importante est celle des **sous-problèmes qui se chevauchent**. Essentiellement, ce que la programmation dynamique fait pour nous, c'est qu'elle nous aide à réutiliser les solutions optimales pour les sous-problèmes. Dans le cas où nous avons plusieurs chemins de récursion avec des sous-problèmes qui se chevauchent, nous ne devrions calculer les réponses pour eux qu'une seule fois. Ensuite, nous les réutilisons. C'est la partie de mise en cache de la programmation dynamique.

La raison pour laquelle ce problème correspond à la programmation dynamique est due aux composants suivants du problème :

* Nous avons une grille où chaque cellule a un numéro spécifique. Ce numéro peut nous aider à définir l'état d'une solution de programmation dynamique.
* À chaque cellule de la grille, nous avons 6 options disponibles. Celles-ci représentent les 6 valeurs de dés que nous pouvons éventuellement obtenir en jouant aux serpents et échelles. Naturellement, ces 6 étapes nous aident à passer d'un état à un autre. Cela représente la partie "divisable en sous-problèmes" des exigences de la programmation dynamique.
* Puisque nous pouvons diviser le problème en sous-problèmes plus petits, nous avons déjà une exigence satisfaite. Si vous réfléchissez attentivement, il est possible d'atteindre la même cellule de la grille plusieurs fois via différents itinéraires. Regardons deux façons possibles d'atteindre la valeur de cellule `22` en partant de `1`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EybVSVwUGmlxBhJTfVhUCw.gif)
_Itinéraire suivi : 1 → 4 → 10 (Serpent vers le haut !) → 22_

Le chemin suivi par le joueur dans le GIF ci-dessus est le suivant :

```
--> Commencez à la case marquée 1--> Valeur du dé 3, donc déplacez-vous à la case marquée 4--> Valeur du dé 6, donc déplacez-vous à la case marquée 10--> Puisqu'il y avait un serpent à la case 10, déplacez-vous à sa tête et donc à la case valorisée 22.
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AI9GiDgIR6GJiiX1SlIkVw.gif)
_Itinéraire suivi : 1 → 4 → 9 → 14 → 17 → 22_

Le chemin suivi par le joueur dans le GIF ci-dessus est le suivant :

```
--> Commencez à la case marquée 1--> Valeur du dé 3, donc déplacez-vous à la case marquée 4--> Valeur du dé 5, donc déplacez-vous à la case marquée 9--> Valeur du dé 5, donc déplacez-vous à la case marquée 14--> Valeur du dé 3, donc déplacez-vous à la case marquée 7--> Valeur du dé 5, donc déplacez-vous à la case marquée 22
```

Comme nous pouvons le voir à partir des deux chemins ci-dessus dans une grille d'échantillon de serpents et échelles, il y a deux façons d'atteindre la case valorisée `22`. Il y a beaucoup d'autres façons également. Pour illustrer le point des sous-problèmes qui se chevauchent, les deux montrés ici suffisent.

Maintenant que nous savons qu'une seule cellule définit l'état de notre solution de programmation dynamique et qu'il existe plusieurs façons d'atteindre la même cellule, cela implique que notre deuxième exigence pour un problème de programmation dynamique est également satisfaite, c'est-à-dire des sous-problèmes qui se chevauchent. Une fois le calcul de la réponse pour un sous-problème donné effectué, il ne devrait pas être recalculé. Il devrait simplement être réutilisé.

Regardons maintenant une formulation formelle de programmation dynamique pour ce problème.

```
dp[i] = Nombre minimum d'étapes à partir de la cellule(i) pour atteindre la cellule de destination.
```

```
dp[i] = min(dp[i + 1], dp[i + 2], ... dp[1 + 6])Nous devons choisir le mouvement qui donne le nombre minimum d'étapes.
```

La formulation ci-dessus semble assez propre et nous pouvons procéder avec elle.

Cependant, il y a un défaut majeur dans la formulation ci-dessus. ?

La façon dont nous avons modélisé notre problème ici est quelque chose qui continuera jusqu'à la fin de l'article. Donc, définissons d'abord le modèle de notre problème. Ensuite, continuons avec la description du défaut dans l'approche de programmation dynamique.

### Modèle de Graphe

Nous pouvons considérer chacune des cellules de notre grille de serpents et échelles comme un nœud dans un graphe. Les six mouvements possibles qu'un joueur peut faire à partir d'une cellule donnée représentent les arêtes. Ces arêtes sont des **arêtes dirigées**. Un mouvement qui nous amène de la cellule `i` à la cellule `j` ne nous ramène pas nécessairement de la cellule `j` à la cellule `i`. Donc, pour la formulation de notre problème, nous avons :

* Un Graphe **G(V, E)**
* Chaque cellule de notre grille de serpents et échelles représente un nœud dans le graphe. Naturellement, il y a **N²** nœuds dans le graphe.
* Chaque mouvement de la cellule `i` à la cellule `j` représente une arête dirigée dans le graphe du nœud `i` au nœud `j`.
* Puisque, pour chaque cellule de la grille, nous avons au plus 6 mouvements, cela signifie que le nombre total d'arêtes dans notre graphe serait **6N²**.

Considérons une petite grille et son graphe correspondant pour plus de clarté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tewxBhmWE1Ofl4-i_oLSlg.png)

Et le graphe correspondant pour cette grille serait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5kgrWbmh3HhjXvmM9YtRyg.png)
_Arêtes pour les nœuds 1 et 2 dans le graphe. Comme vous pouvez l'imaginer, le graphe devient compliqué très rapidement à cause du nombre d'arêtes. Il devrait y avoir 4 * 4 * 6 = 96 arêtes au total dans le graphe puisque nous avons 16 nœuds et chacun d'eux aura 6 arêtes au total. Mais, les nœuds finaux 11-16 auront moins d'arêtes. par exemple, 11 aura juste 5 arêtes. De même, 16 aura 0 arêtes. Par conséquent, le nombre total d'arêtes sera de 96 — (1 + 2 + 3 + 4 + 5 + 6) = 75._

### Le Défaut dans notre formulation DP

Maintenant que nous avons défini notre modèle graphique pour le problème, nous pouvons examiner le défaut dans notre formulation de programmation dynamique. La formulation que nous avons examinée était la suivante :

```
dp[i] = Nombre minimum d'étapes à partir de la cellule(i) pour atteindre la cellule de destination.
```

```
dp[i] = min(dp[i + 1], dp[i + 2], ... dp[1 + 6])Nous devons choisir le mouvement qui donne le nombre minimum d'étapes.
```

Si aucun serpent n'était impliqué dans le problème, alors la formulation ci-dessus aurait été complète en elle-même. Le problème induit par les serpents est celui des **boucles dans notre graphe**. Un serpent peut nous ramener à un état déjà visité dans notre graphe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kLIADq0TSTvPGO8CAQwVSw.png)
_Boucle introduite par les serpents dans la représentation graphique._

Le problème que cela crée dans notre formulation est que nous ne pouvons pas vraiment considérer une seule cellule dans la grille pour définir l'état de notre formulation de programmation dynamique.

Voyons pourquoi c'est le cas via un exemple, puis nous verrons comment corriger ce problème par une formulation différente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ivdDp1CaUdfIBTETgLxn9g.png)
_Le joueur se déplace de la cellule 1 à 22 et suit le chemin 1 → 5 → 16 (Serpent vers le haut !) → 22._

C'est l'un des itinéraires possibles pour atteindre la cellule 36 en partant de la cellule initiale 1.

Supposons que nous voulons trouver le nombre minimum d'étapes pour aller de la cellule `22` à la cellule de destination `36`. Dans le cas ci-dessus, le joueur est allé de `1 --> 5 --> 16 (Serpent vers le haut !)` --> 22. Comme nous pouvons le voir dans la figure ci-dessus, le joueur descendra à la cellule `th` 11 à cause du serpent. Puis il fera un pas en avant, c'est-à-dire `t` à la cellule 12. Enfin, il prendra le serpent vers la cellule de destination `io` 36. Ce n'est qu'une seule étape.

En suivant le serpent de `22 -->` 11 et fr`om 12 --&`gt; 36 n'est pas vraiment un mouvement. Le mouvement réel est `from 11` --> 12. Par conséquent, le nombre minimum d'étapes nécessaires pour m`ov`e fr`om` 22 à 36 est 1.

Considérons maintenant l'état suivant de la grille lorsque l'utilisateur avait atteint `22`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hm-qbmJwtc9KT0yl8fSJvA.png)
_Le joueur se déplace de la cellule 1 à 22 et suit le chemin 1 → 6→ 11 → 16 → 22._

Le scénario ci-dessus est également possible pendant la récursion. Dans ce cas, lorsque le joueur atteint la cellule `22`, il n'a pas 6 options devant lui. La raison en est que la cellule `22` est le point de départ d'un serpent. Si une cellule est un point de départ pour un serpent, alors il faut suivre jusqu'à sa tête. Le joueur se retrouvera à la cellule `11` qui a déjà été visitée. C'est une boucle dans notre récursion. Puisque nous ne pouvons pas faire d'autre mouvement à partir de la cellule `22`, il n'y a aucun moyen de trouver le nombre minimum d'étapes de `22 à 36`.

Le problème est :

Une cellule seule ne peut pas représenter l'état de notre formulation de programmation dynamique. Nous devons également garder une trace des cellules visitées avant celle en main. Une combinaison de ces deux éléments définirait un état unique dans notre formulation DP.

### Formulation DP mise à jour

La formulation DP mise à jour, comme mentionné précédemment, devra prendre en compte les cellules visitées et la cellule actuelle où se trouve le joueur.

Puisque l'état d'un problème de programmation dynamique est généralement utilisé comme clé pour un cache qui stocke les résultats pour divers états (**mémoisation**), le simple fait de garder un dictionnaire ou un ensemble de nœuds de cellules visitées n'est pas réalisable. Ces structures de données ne sont pas hachables.

Une approche alternative qui peut être adoptée est le **masquage de bits**. Nous pouvons utiliser un masque de bits pour marquer les cellules de la grille qu'un utilisateur a déjà visitées avant de visiter une cellule particulière.

Considérons si cette approche est même réalisable. Donc, pour une taille de grille de `20 par 20`, il y aurait `400` cellules et nous aurions besoin d'un masque de bits de `400` bits. Chacune de ces valeurs de bits représenterait si cette cellule particulière est déjà visitée ou non pendant la récursion. Puisque chacun des bits peut avoir deux valeurs différentes : `0 et 1`, il y a **2⁴⁰⁰** états de grille possibles. En le multipliant par 400 puisque nous avons également besoin de la cellule actuelle, nous obtenons un **nombre impressionnant (2⁴⁰⁰ * 400)**.

Un nombre aussi élevé d'états possibles ne fonctionnera pas et n'est pas du tout traitable. C'est la raison pour laquelle nous devons passer d'une solution de programmation dynamique à autre chose en raison du nombre énorme d'états dans la formulation du problème.

### La Recherche en Largeur à la Rescue! ⚡

Essayons de formuler le problème d'une manière légèrement différente. Nous avons déjà dit que les cellules de notre grille représentent les nœuds dans un graphe. Les 6 mouvements possibles représentent les arêtes dirigées vers d'autres nœuds dans le graphe.

Nous voulons trouver le nombre minimum de mouvements pour atteindre la destination en partant du point initial sur la grille. Cela revient à **trouver le chemin le plus court dans un graphe non pondéré**.

Vous pouvez dire que ce graphe est non pondéré, ou vous pouvez dire que toutes les arêtes ont des poids égaux. Par conséquent, les poids peuvent être ignorés. Trouver le chemin le plus court dans un graphe non pondéré est un problème assez standard. L'algorithme le plus standard pour le résoudre est l'**algorithme de recherche en largeur**.

Nous n'avons pas besoin d'un état spécial dans notre graphe pour la recherche en largeur comme nous en avions besoin dans le cas de la programmation dynamique. Nous pouvons définitivement avoir plusieurs façons d'atteindre un nœud particulier à partir de la position de départ. **Cependant, le premier itinéraire qui est découvert dans l'algorithme de recherche en largeur est le plus court**. C'est la base de l'algorithme.

Cela signifie que la première fois que nous rencontrons un nœud/cellule pendant notre recherche, le nombre de mouvements effectués jusqu'alors serait le nombre minimum de mouvements nécessaires pour atteindre cet état/cellule/nœud à partir de la position de départ.

Après cela, si nous rencontrons le même nœud à nouveau, nous pouvons simplement l'ignorer. Nous aurions déjà le chemin le plus court vers ce nœud à ce moment-là. **Cela garantit que nous ne traitons aucun nœud du graphe plus d'une fois dans la recherche en largeur**.

L'algorithme de recherche en largeur utilise la structure de données **file d'attente**. La file d'attente contient les nœuds du graphe à un niveau particulier à tout moment. Puisque nous ne traiterons chaque nœud qu'exactement une fois, la taille maximale possible de la file d'attente peut être O(N). C'est la limite supérieure de la taille de la file d'attente. Cette approche du problème est très traitable et est en fait la manière optimale de le faire.

Regardons le pseudo-code de l'algorithme que nous venons de proposer pour ce problème. Ensuite, nous examinerons l'implémentation de celui-ci.

```
1. Initialiser une file d'attente pour l'algorithme BFS. Appelons-la "Q".2. Ajouter la première cellule à la Q. Notez que nous devons également garder une trace du niveau des nœuds dans notre graphe. Le niveau nous indiquera le nombre minimum de mouvements effectués pour atteindre un nœud spécifique. Le niveau pour le nœud initial serait 0.3. Traiter jusqu'à ce que la Q devienne vide.    a. Retirer l'élément de tête de la Q. Appelons-le "node".    b. Pour chacun des 6 mouvements possibles à partir de "node", ajouter ceux qui n'ont pas été traités auparavant, à la Q.4. Si nous rencontrons le nœud de destination pendant le traitement, retourner simplement la valeur de niveau à ce point.
```

Il y a beaucoup de points intéressants que nous devons aborder avant de regarder l'implémentation. Ceux-ci proviennent de ma propre tentative du problème. Certains de ceux-ci peuvent sembler trop simples pour avoir été mentionnés. Je voulais exposer tous ces cas. Ils sont importants pour la manière dont vous écrivez le code pour cet algorithme que nous avons discuté.

### Mappage de la Valeur de Cellule à la Ligne et Colonne ?

Le premier de ces points qui est important à considérer est le mappage des valeurs de cellule aux numéros de ligne et de colonne réels.

Rappelez-vous, nous avons une grille de certaines valeurs et chaque cellule de la grille a une numérotation. Le système de numérotation est écrit [_boustrophédoniquement_](https://en.wikipedia.org/wiki/Boustrophedon) à partir du bas en commençant par le coin inférieur gauche du plateau, et en alternant la direction à chaque ligne.

La façon dont l'implémentation a été faite ici initialement est en considérant les numéros de ligne et de colonne réels et en les utilisant ensuite pour progresser dans la grille.

Selon le problème, si une cellule contient un serpent, alors la valeur dans cette cellule est la cellule de destination où le joueur atterrirait. Nous devons mapper la valeur de la cellule de destination au numéro de ligne et de colonne correspondant.

Le mouvement pour la ligne est toujours facile. Nous nous déplaçons soit dans différentes colonnes de la même ligne, soit nous pouvons passer à une ligne supérieure. C'est tout pour la ligne.

En ce qui concerne la colonne, il y a deux directions de mouvement possibles. La question est particulièrement délicate. La numérotation des cellules **alterne** d'une ligne à l'autre. Le mouvement dans une ligne (pour les différents mouvements) aura également des directions alternées dans des lignes alternées, par exemple, pour une grille `6 par 6`, le mouvement sera vers la droite pour la ligne du bas et il sera vers la gauche dans la deuxième ligne du bas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y3ibwfZCN9cvUO52zB3ovw.png)

Pour une matrice `6 par 6`, le numéro de ligne `5` (en considérant un indexage basé sur 0 des lignes et colonnes de la matrice) serait celui contenant les cellules de `1 .. 6` et le numéro de ligne `4` contiendrait les cellules de `7 .. 12`.

Cela signifie que pour les lignes numérotées paires, la direction est vers la gauche. Pour les lignes numérotées impaires, la direction est vers la droite. Cependant, ce mappage est inversé lorsque `N` est impair. Considérons le scénario dans une matrice `5 par 5`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UiJmWB5ATrALdzP0EUE07A.png)

La dernière ligne de cette matrice est `4` et cette ligne a une direction vers la droite. Cela signifie que dans ces cas, la ligne numérotée paire a une direction vers la droite. La ligne numérotée impaire a une direction vers la gauche.

En termes d'implémentation, nous pouvons utiliser quelque chose comme ce qui suit.

```
even_direction = 1 si N % 2 != 0 sinon -1direction = even_direction * (1 si row % 2 == 0 sinon -1)
```

Dans notre implémentation, nous considérons une valeur de `1` pour une direction vers la droite et une valeur de `-1` pour représenter une direction vers la gauche. La raison de cela est la simplicité qu'elle induit dans la simulation du mouvement. Nous pouvons simplement faire quelque chose comme :

```
for move in range(6):     new_cell = cell[r][c + direction]
```

Le `c + direction` irait soit vers la droite soit vers la gauche. Cela est dû au fait que la valeur de `direction` sera soit `1` soit `-1` en fonction de la valeur de `N`.

Maintenant, nous pouvons examiner le mappage d'une valeur de cellule aux indices de ligne et de colonne correspondants.

Notez que le code suivant n'est à exécuter que lorsque nous trouvons un serpent dans l'une des cellules. `board[row][col]` contiendra un `-1` pour représenter une cellule normale. Le code suivant est exécuté lorsqu'un serpent est trouvé, c'est-à-dire `board[row][col] != -1`

```
(1) value = board[row][col](2) snake_dest_row = N - (value / N) - 1(3) new_direction = even_direction * (1 if snake_dest_row % 2 == 0 else -1)(4) snake_dest_column = (value % N)                        (5) if new_direction < 0:(6)    snake_dest_column = N - 1 - snake_dest_column                        (7) next_cell = (snake_dest_row, snake_dest_column)
```

#### Ligne 1

Nous donne la valeur stockée à la cellule actuelle. La cellule actuelle est représentée par `row` et `col`.

#### Ligne 2

En utilisant la valeur stockée dans la cellule, nous trouvons la ligne où cette cellule serait située. Rappelez-vous, la valeur représente la cellule vers laquelle nous devons déplacer le joueur puisqu'il a rencontré un serpent.

#### **Ligne 3**

Puisque nous avons déterminé la ligne où la nouvelle cellule (cellule de destination) serait située, nous pouvons également déterminer la direction des cellules dans cette ligne particulière. Nous avons discuté des directions vers la droite et vers la gauche en fonction de la valeur de N, ci-dessus.

#### **Ligne 4, 5 et 6**

Représente le décalage pour trouver la valeur de la colonne. Pour une ligne dont la direction va vers la droite, le décalage lui-même représentera l'index de la colonne. Si la direction est vers la gauche, alors le décalage sera à partir de la droite. Nous trouvons l'index de la colonne en utilisant `N — snake_dest_column — 1`.

### Valeurs de Cellule Problématiques ?

Comme mentionné précédemment, les cellules contiennent soit `-1`, soit elles contiennent un serpent. La façon dont un serpent est représenté est par une valeur de cellule qui représente la cellule de destination qu'un joueur atteindra en suivant ce serpent.

Ainsi, lors de la gestion du cas du serpent, nous devons être capables d'obtenir le numéro de ligne et de colonne où la cellule correspondante sera située.

Nous avons vu dans la section précédente la manière dont nous pouvons faire cela. Il y a cependant une petite erreur dans le code.

Considérons le scénario où nous avons une grille `4 par 4`. Une cellule particulière contient un serpent qui emmène le joueur à (ou dont la cellule de destination est) `8`. Regardons les valeurs de ligne et de colonne correspondantes que nous obtenons en utilisant le code ci-dessus.

```
value = 8even_direction = -1snake_dest_row = 4 - (8 / 4) - 1 = 1new_direction = -1 * (-1) = 1snake_dest_column = 8 % 4 = 0
```

```
next_cell = (1, 0)
```

Clairement, ce n'est pas la bonne cellule. La bonne cellule représentant la valeur `8` est `(2, 0) et non (1, 0)`. La façon dont nous corrigeons cela est de ne pas considérer la valeur telle quelle, mais en soustrayant 1 de celle-ci. Ensuite, ce problème ne se pose pas.

```
value = board[row][col] - 1
```

### Faire un mouvement par Serpent ?

L'un des derniers composants importants de l'implémentation est de respecter la règle mentionnée dans l'énoncé du problème qui stipule que "vous ne prenez un serpent ou une échelle qu'au plus une fois par mouvement". Si la destination d'un serpent ou d'une échelle est le début d'un autre serpent ou d'une autre échelle, **vous ne continuez pas à vous déplacer**.

La façon dont BFS fonctionne est que nous traitons le nœud actuellement sorti de la file d'attente en regardant sa liste d'adjacence. Ensuite, nous considérons tous les nœuds qui n'ont pas encore été traités et nous les ajoutons à la file d'attente.

Ainsi, pour une cellule donnée, il y aurait 6 nœuds adjacents. Sauf dans certains cas où il n'est pas possible d'avoir 6 mouvements dans tous les cas. Nous devons considérer tous ceux-ci et ajouter ceux qui n'ont pas encore été traités à la file d'attente.

Aucun traitement spécial n'est requis pour les mouvements qui atterrissent dans des cellules qui ne contiennent pas de serpent. Donc, tout ce que nous faisons dans ce cas est :

```
if board[row][col + direction] == -1:    process it normally
```

Dans le cas où le mouvement que nous faisons nous amène à un serpent, au lieu de considérer/traiter le nœud où nous sommes après le mouvement, nous considérons la cellule de destination du serpent et nous l'ajoutons à la file d'attente à la place si elle n'a pas été traitée auparavant. Considérons un exemple pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cDpzOjDHBHBbWY-YfiLikw.png)
_Les 6 mouvements lorsque le joueur est à la cellule 1_

Comme vous pouvez le voir dans la figure ci-dessus, nous ne considérons pas le nœud 4 lors du traitement des 6 mouvements correspondant à la cellule `1`. Au lieu de cela, nous considérons la destination finale pour `4`, c'est-à-dire `11`.

Si, par exemple, il y avait un serpent de `11` à un autre nœud, alors nous ne le traiterions pas. Nous avons déjà traité un mouvement de serpent de `4 à 11`. Il ne peut y avoir de continuation de mouvements de serpent ici. C'est une chose importante à noter.

Regardons l'implémentation qui rassemble toutes ces idées.

### Pouvons-nous nous débarrasser de la chose "direction" ? ?

Il s'avère qu'il existe une manière plus simple de faire ce qui est accompli en utilisant la variable `even_direction` ci-dessus.

Essentiellement, nous voulons savoir, étant donné un numéro de ligne, quelle est la direction des cellules dans celle-ci. Est-ce vers la droite ou vers la gauche ?

La raison pour laquelle nous avons besoin de cette information est que cela nous aide à décider du numéro de colonne final lorsque nous rencontrons un serpent.

Au lieu de nous fier à la variable `even_direction`, nous pouvons utiliser une vérification simple comme celle-ci :

```
if N % 2 != row % 2:   direction = rightelse   direction = left
```

Cela couvre tous les cas pour nous. Rappelez-vous, la direction d'une ligne dépend de la valeur de `N`.

* `N` est pair et `row` est pair, alors `N % 2 == row % 2` et donc la direction sera vers la **gauche**.
* `N` est pair et `row` est impair, alors `N % 2 != row % 2` et donc la direction sera vers la **droite**.
* `N` est impair et `row` est impair, alors `N % 2 == row % 2` et donc la direction sera vers la **gauche**.
* `N` est impair et `row` est pair, alors `N % 2 != row % 2` et donc la direction sera vers la **droite**.

Merci à [Divya Godayal](https://www.freecodecamp.org/news/the-perfect-programming-interview-problem-8431cdeab2a7/undefined) pour avoir suggéré cette vérification simpliste. Cela réduit définitivement la longueur du code et couvre tous les cas ci-dessus. Santé !

### Mappage dans l'autre sens

Dans l'implémentation ci-dessus, nous avons travaillé avec des numéros de ligne et de colonne. Ensuite, nous avons mappé une valeur de cellule à un numéro de ligne et de colonne chaque fois que cela était nécessaire (en cas de serpent). Nous pouvons également résoudre ce problème en travaillant dans l'autre sens.

Il est beaucoup plus simple de travailler avec des numéros de cellule. En commençant par `1` et pour chaque cellule, nous devons considérer les `6` cellules suivantes.

Tout ce que nous aurions à faire est de mapper ces valeurs de cellule aux numéros de `ligne` et `colonne` correspondants (à nouveau, pour vérifier la présence ou l'absence de serpents). Nous avons déjà vu comment faire cela dans l'implémentation ci-dessus également.

Cela raccourcit le code. La solution que j'ai expliquée ci-dessus est celle à laquelle j'ai pensé en réfléchissant au problème. Je voulais l'expliquer telle quelle pour clarifier les choses. Cela peut ne pas être la meilleure façon de procéder pour écrire le code de l'algorithme décrit. Cela aide à décrire tous les pièges.

### Pourquoi est-ce encore le meilleur problème d'entretien de programmation ?

1. Vous pourriez être tenté par une solution basée sur la programmation dynamique (comme je l'ai été ?). Dans ce cas, vous devez raisonner et sortir de ce piège. La DP ne fonctionne pas ici.
2. Proposer une approche basée sur la BFS ici est super critique. Une bonne maîtrise de vos algorithmes basés sur les graphes est nécessaire. L'important est de mapper le problème à la _recherche des plus courts chemins dans un graphe non pondéré_.
3. Écrire le code pour mapper les valeurs de cellule aux numéros de ligne et de colonne correspondants peut être super confus, surtout sous contrainte de temps. Ce n'est pas un gros morceau de code, mais vous devez être capable de le réfléchir correctement.
4. Gérer le cas limite où nous obtenons un mappage incorrect si nous considérons les valeurs de cellule telles quelles. Nous avons dû soustraire 1 de la valeur de cellule avant de la mapper à la ligne et à la colonne correspondantes. L'échec à faire cela donnera des résultats incorrects.
5. Écrire un code correct et fonctionnel sous contrainte de temps est également une tâche assez difficile. Vous devez vraiment garder votre calme.

Dans l'ensemble, ce problème teste de nombreux aspects différents de la programmation et de la capacité de réflexion d'un programmeur. Je pense que c'est l'un des aspects les plus importants à tester lors de tels entretiens.

Ce n'est pas que ces entretiens soient la meilleure façon d'embaucher les candidats. Puisqu'ils existent, ce problème révèle de nombreuses qualités différentes que les intervieweurs recherchent chez les candidats.

Si vous avez trouvé l'article utile, partagez-le autant que possible ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*EsnZKUKCORDc5z_rckxOKQ.gif)