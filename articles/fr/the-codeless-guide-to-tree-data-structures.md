---
title: Comment apprendre les structures de données arborescentes sans coder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T23:16:20.000Z'
originalURL: https://freecodecamp.org/news/the-codeless-guide-to-tree-data-structures
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c36740569d1a4ca30b5.jpg
tags:
- name: data structures
  slug: data-structures
- name: Trees
  slug: trees
seo_title: Comment apprendre les structures de données arborescentes sans coder
seo_desc: 'By Armstrong Subero

  The tree data structure can form some of the most useful and complex data structures
  in all of programming. In fact the tree is so powerful that I can make the bold
  claim:

  Once you understand trees you''ll be able to understand man...'
---

Par Armstrong Subero

La structure de données arborescente peut former certaines des structures de données les plus utiles et complexes de toute la programmation. En fait, l'arbre est si puissant que je peux faire l'affirmation audacieuse :

**Une fois que vous comprenez les arbres, vous serez en mesure de comprendre de nombreuses autres structures de données et algorithmes avec facilité.**

Il y a un bémol. Il existe tant de types d'arbres qu'il peut être impossible de savoir par où commencer ! Il y a les B-arbres, les arbres rouge-noir, les arbres binaires, les arbres AVL et bien d'autres. Il y a des choix abondants et chacun semble précieux à apprendre.

Cela pose un problème. En tant que personne apprenant les arbres, vous pourriez vous demander, quelle structure de données arborescente dois-je apprendre en premier ? Quel arbre est le plus important pour moi ? Il y en a tant, par où commencer ?

Apprendre les arbres, c'est comme apprendre les nombreuses merveilles de notre monde actuel. Nous avons beaucoup de choix, en fait, nous avons peut-être même trop de choix.

Les psychologues appellent cela le **surcharge de choix** ou « surcharge de choix », c'est-à-dire que face à de nombreuses options, les gens ont du mal à décider quoi faire. Je l'appelle le pire cauchemar d'un débutant en codage.

Cependant, il n'y a pas lieu de paniquer. D'après ma connaissance de l'utilisation de la structure de données arborescente, comme pour la plupart des choses dans la vie, le principe de Pareto (ce que nous appelons la règle des 80/20) s'applique.

Ce que cela signifie, c'est qu'en tant que programmeur, 80 % des cas où vous devrez utiliser des arbres seront couverts par environ 20 % des types d'arbres que vous tenterez d'apprendre.

Pour cette raison, nous nous concentrerons uniquement sur ces 20 % que je pense être les arbres les plus importants que vous devez comprendre. Ne vous méprenez pas, je ne dis pas de ne pas apprendre d'autres types d'arbres. Je dis d'apprendre ceux-ci en premier, puis de vous concentrer sur les autres pour vraiment obtenir cet avantage.

Même lorsque vous aurez déterminé quelle structure de données arborescente vous souhaitez apprendre, vous serez confronté à un autre problème.

Il existe de nombreuses ressources qui vous enseignent les arbres, cependant, elles vous présentent toutes du code dans un langage particulier, qu'il s'agisse de JavaScript, Java, Python ou autres, dans le cadre de l'explication.

**Dans cet article, je brise ce statu quo et vous enseigne les structures de données arborescentes essentielles, et tout cela sans que vous ayez à écrire une seule ligne de code.**

Rejoignez-moi dans un voyage au cœur du monde des arbres, quel que soit le langage de programmation que vous utilisez, vous pourrez apprendre toutes les bases que vous devez connaître sur la structure de données arborescente.

## Aller à la racine des arbres

Allons à la racine de notre discussion (jeu de mots intended). La façon dont j'aime expliquer les arbres est en les reliant à quelque chose que nous connaissons tous, celui de l'arbre biologique. Au cas où vous ne seriez pas familier, regardons-en un maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/photography-of-tree-1067333.jpg)
_Un arbre biologique_

Regardez notre arbre, n'est-il pas magnifique ! Nous voyons qu'un arbre est une plante géante avec un tronc, une branche et des feuilles. Il y a aussi des racines cachées sous le sol qui font également partie de l'organisme.

Un arbre en informatique n'est pas si différent. Regardons-en un ici :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-23.png)
_Un arbre en informatique_

Un arbre en informatique est très similaire à un arbre régulier – il ressemble un peu à un arbre biologique à l'envers, n'est-ce pas ? Il ne ressemble pas seulement, mais il a aussi des parties qui sont nommées de manière similaire à notre bon vieux arbre tangible.

Avant d'apprendre les types d'arbres, il y a quelques faits sur les arbres que vous devez connaître.

### Voici 5 faits que vous devez savoir sur les arbres :

1. Chacun des cercles de l'arbre est appelé un nœud et chaque ligne est appelée une arête.

2. Le nœud racine est la partie de l'arbre sur laquelle toutes les autres parties sont construites.

3. Il y a des nœuds parents connectés à d'autres nœuds dans la direction de la racine, et des nœuds enfants connectés dans la direction opposée à la racine.

4. Les derniers nœuds des arbres sont appelés feuilles.

5. Le processus de navigation dans un arbre est appelé parcours.

Si vous aimez voir les choses visuellement, voici un diagramme de l'arbre que nous avons regardé plus tôt identifiant les parties :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-25.png)
_Notre arbre étiqueté_

Vous devriez également savoir que lorsqu'un arbre est l'enfant d'un nœud, il est appelé un sous-arbre. Regardez le diagramme ci-dessus, le nœud étiqueté « Parent » ainsi que ses deux nœuds enfants peuvent être classés comme un sous-arbre.

Super, maintenant vous avez une idée des arbres de base. Alors plongeons dans certains des types d'arbres les plus utiles que vous rencontrerez.

## L'arbre général

Le premier type d'arbre que nous devons connaître est l'arbre général. L'arbre général est ce que nous appelons un sur-ensemble. C'est parce que tous les autres types d'arbres sont dérivés de l'arbre général.

Les arbres sont hiérarchiques dans la façon dont ils stockent les données. Alors que des structures de données plus simples peuvent stocker des données de manière linéaire (pensez à un tableau), les arbres sont non linéaires.

L'arbre général est l'incarnation d'une structure d'arbre hiérarchique car il n'a pas de restrictions sur le nombre d'enfants que chaque nœud peut avoir, et n'a pas de contrainte imposée sur la hiérarchie de l'arbre.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-29.png)
_Exemple d'un arbre général_

## L'arbre binaire

Il est impossible de parler des arbres sans parler de l'arbre binaire (d'accord, pas totalement impossible, mais vous voyez ce que je veux dire).

Simplement dit, un arbre binaire est un type d'arbre qui a une restriction. Dans l'arbre binaire, chaque parent ne peut être lié qu'à deux nœuds enfants dans l'arbre.

Il y a un type d'arbre binaire qui illustre cela le mieux : l'arbre de recherche binaire. Les arbres que vous voyez ne sont pas simplement des cercles vides connectés par des lignes. Chacun des nœuds de l'arbre a une valeur qui lui est associée et l'ensemble de l'arbre est une structure clé-valeur.

Les arbres de recherche binaire gardent leurs clés triées. Ils les trient comme ceci : tous les nœuds sont plus grands que les nœuds dans leur sous-arbre gauche, mais sont plus petits que les nœuds dans leur sous-arbre droit. Confus ? Peut-être qu'une image aidera :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-26.png)
_Un arbre de recherche binaire_

Regardez attentivement cet arbre et vous apprendrez un petit secret. Dans l'arbre binaire, le plus petit nœud est situé dans le sous-arbre le plus à gauche partant du nœud racine. Vous voulez deviner où nous pouvons trouver le plus grand nœud ?

## Arbre rouge-noir

Regardons une variante de l'arbre de recherche binaire que les gens ont tendance à surcompliquer. Je parle de l'arbre rouge-noir.

Il y a de nombreux cas d'arbres où des données peuvent être insérées et supprimées. Ainsi, des variations de l'arbre de recherche binaire ont été créées pour rendre cette insertion et suppression constantes plus efficaces.

L'arbre rouge-noir est une telle configuration de l'arbre de recherche binaire qui rend le processus d'insertion et de suppression plus efficace.

L'arbre fait cela en ayant un bit qui ajoute un attribut au nœud. Cet attribut qui est ajouté au nœud est la couleur, et cette couleur peut être interprétée comme rouge ou noire. D'où le nom d'arbre rouge-noir.

Regardons comment un arbre rouge-noir peut être arrangé :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-28.png)
_Un arbre rouge-noir_

Dans l'arbre rouge-noir, le nœud racine est généralement noir et chaque nœud rouge a des enfants qui sont noirs.

Si vous êtes arrivé jusqu'ici, alors félicitations ! Vous comprenez déjà suffisamment pour faire une incursion dans le monde des structures de données arborescentes.

## Où sont utilisés les arbres ?

À ce stade, vous vous demandez peut-être à quoi servent les arbres. C'est une bonne question ! Les arbres sont utilisés dans de nombreux aspects du développement, y compris dans :

1. Les bases de données
2. Les compilateurs
3. Le réseau
4. Les tas
5. Les algorithmes d'apprentissage automatique

Il y a d'innombrables utilisations pour les arbres et la seule limite à leur utilisation est l'imagination du concepteur.

## Conclusion

Dans cet article, nous avons commencé notre voyage dans le monde de l'arbre. Bien que nous ayons couvert du terrain, nous avons à peine effleuré la surface de cette vaste et complexe structure de données.

Nous avons aiguisé notre appétit pour les structures de données arborescentes en couvrant ce que sont les arbres et en regardant leur structure. Nous avons ensuite discuté de trois types courants d'arbres, y compris les arbres généraux, les arbres binaires et les arbres rouge-noir. Enfin, nous avons regardé quelques endroits où les arbres peuvent être utilisés.

À la fin de cet article, vous devriez avoir une base solide pour vous aventurer dans le monde des arbres !

## Où aller ensuite ?

Vous voulez apprendre les arbres et autres structures de données sans écrire une seule ligne de code ? Alors procurez-vous le livre « Codeless Data Structures and Algorithms », où vous apprendrez tout ce que vous devez savoir sur les structures de données et les algorithmes sans écrire une seule ligne de code !

Nous ne nous contenterons pas d'approfondir ce que nous avons appris, mais nous aborderons des sujets passionnants non couverts ici comme l'équilibrage des arbres, les arbres AVL, les B-arbres, les tas et une tonne de sujets dans le domaine des structures de données et des algorithmes !

Vous pouvez lire le livre ici :

%[https://www.apress.com/gp/book/9781484257241]