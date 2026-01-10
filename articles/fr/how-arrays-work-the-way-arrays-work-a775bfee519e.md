---
title: Aperçu du fonctionnement des tableaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T03:05:06.000Z'
originalURL: https://freecodecamp.org/news/how-arrays-work-the-way-arrays-work-a775bfee519e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IAFX-G9C6sOXI-s6Q0widw.png
tags:
- name: Computer Science
  slug: computer-science
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
seo_title: Aperçu du fonctionnement des tableaux
seo_desc: 'By Edison Yap

  In computer science, there is the concept of a linear data structure, which means
  that the data are structured in a linear way in which order matters. There are Arrays
  and Linked Lists, but today I’ll be talking mostly about arrays, and...'
---

Par Edison Yap

En informatique, il existe le concept de **structure de données linéaire**, ce qui signifie que les données sont structurées de manière linéaire où **l'ordre compte**. Il existe des **tableaux** et des **listes chaînées**, mais aujourd'hui je vais parler principalement des tableaux, et un peu des listes chaînées.

La plupart des langages orientés objet sont livrés avec des **tableaux**, tandis que la plupart des langages _f_onctionnels sont livrés avec des **listes chaînées** (voir pourquoi dans un autre de mes articles, mentionné à la fin de cet article).

Il y a une bonne raison à cette différenciation que nous allons explorer plus tard. Pour l'instant, jetons un rapide coup d'œil aux différences entre ces deux structures de données. Pour ce faire, nous devons faire un voyage dans le passé.

### Remonter le temps

Les objets, les fonctions et tout ce que nous savons sur les ordinateurs sont fondamentalement stockés en bits et en octets dans l'ordinateur.

Dans des langages comme Java et C, vous devez déclarer explicitement la taille d'un tableau au préalable.

> _Attendez, mais Ruby ne fait pas ça ?_

En Ruby, nous utilisons `Array` pour nos structures de données linéaires. Nous pouvons ajouter apparemment une infinité de choses dans un tableau Ruby et cela n'aura pas d'importance pour nous.

Ce n'est pas génial ? Cela signifie que les tableaux sont **infini**ment grands, n'est-ce pas ? Et que Ruby est le langage supérieur ? Quelle chance nous avons !

Mais pas si vite. _*éclate votre bulle*_

Il n'existe pas de **tableaux de taille infinie** ; ce que vous voyez en Ruby est ce que nous appelons un **tableau dynamique**, et cela a un coût.

Pour comprendre ce que sont les tableaux dynamiques, examinons d'abord comment les tableaux sont représentés en mémoire. Puisque MRI Ruby (Matz's Ruby Interpreter) compile en code C, nous allons voir comment les tableaux sont représentés en C.

### Voir c'est croire

Nous allons plonger dans un peu de code C pour nous aider à mieux comprendre...

Dans les langages de bas niveau comme C, vous devez gérer les pointeurs et l'allocation de mémoire vous-même. Même si vous n'avez jamais traité avec C auparavant (avertissement — moi non plus), vous avez peut-être déjà vu l'un des exemples les plus (in)fames ci-dessous :

Décomposons ce bout de code :

* `malloc` n'a pas de signification magique derrière lui, il signifie littéralement `allocation de mémoire`
* `malloc` retourne un pointeur
* `malloc` prend un argument, qui est la taille de la mémoire que vous voulez que le programme alloue pour vous.
* `100 * sizeof(int)` indique au programme que nous voulons stocker 100 entiers, donc allouez-nous 100 * la taille de ce que chaque entier occuperait.
* `ptr`/pointeur stocke la référence à l'adresse mémoire.

### Timmy stocke des bagages !

Si l'exemple ci-dessus n'a pas vraiment de sens, essayez cette analogie. Pensez à l'allocation de mémoire comme à un concierge de bagages. Cela fonctionne comme suit :

* Timmy se rend au comptoir, dit au concierge qu'il a 2 pièces de bagages, environ _cette_ taille, et qu'il aimerait les stocker dans la salle de stockage.
* Le concierge jette un coup d'œil à la salle de stockage et dit « Oui, nous avons de la place dans la zone désignée `B4` et allons allouer cet espace pour stocker vos bagages ».
* Ils remettent à Timmy une **carte de retrait** avec la zone désignée dessus, `B4` dans notre cas.
* Timmy est heureux, vaque à ses occupations, et quand il veut récupérer ses bagages, il retourne au comptoir et leur montre sa **carte de retrait**. « _Avez-vous vu mes bagages ?_ »

Dans notre exemple, les bagages de Timmy sont les **données**, la **carte de retrait est le pointeur** (elle indique où le sac de Timmy est stocké). L'endroit où le concierge stocke les bagages de Timmy est le **bloc mémoire**, et le comptoir est le **programme**.

En montrant la carte de Timmy (**pointeur/adresse mémoire**) au comptoir (**le programme**), Timmy peut récupérer ses bagages (**données**). Bonus ? Parce qu'ils savent **exactement** où le sac de Timmy est stocké — `B4`, cela signifie qu'ils peuvent récupérer tous les bagages de Timmy relativement rapidement !

Aussi, vous êtes-vous déjà demandé pourquoi vous accédez aux éléments d'un tableau avec un **index**, comme ceci ?

C'est parce que le tableau contient les références au bloc mémoire, et l'index indique le **décalage**.

Une analogie pour cela est si je vous demande de chercher Timmy dans une file de 20 personnes, vous devriez logiquement demander à chacun d'eux s'ils étaient Timmy. Mais, si je vous disais que Timmy est le 6ème (**index**) à partir de la première personne (**votre pointeur d'origine**), vous savez exactement où regarder.

La récupération des éléments dans les tableaux est rapide exactement pour cette raison — le programme n'a pas à parcourir tous les 100 éléments pour trouver ce que vous cherchez. Si vous avez l'index, il doit simplement ajouter le décalage à l'adresse mémoire d'origine, et le droïde que vous cherchiez sera juste là !

### Qu'est-ce que les tableaux dynamiques alors ?

Je vous ai un peu parlé de la façon dont les tableaux sont représentés en mémoire, mais il est maintenant temps de parler de quelques inconvénients.

Souvenez-vous comment vous devez déclarer explicitement la quantité de mémoire dont vous avez besoin ? Cela signifie que le tableau trouvera un emplacement qui correspondra exactement à votre taille. Il n'y a aucune garantie qu'il pourra contenir plus que ce que vous avez (parce que le bloc mémoire juste derrière pourrait être occupé).

Retour à notre analogie des bagages : imaginez que Timmy doive stocker 2 pièces de bagages, et que `B4` puisse stocker exactement 2 pièces de bagages, donc ils l'allouent à Timmy. Maintenant, pour une raison quelconque, Timmy veut stocker _une autre_ pièce de bagages, mais `B4` ne peut pas stocker 3 pièces, seulement 2, alors que font-ils ?

Ils prennent tous ses bagages existants, les déplacent dans un nouvel endroit qui peut contenir plus de 3 pièces, puis les stockent tous ensemble.

C'est une opération coûteuse mais c'est exactement ainsi que fonctionne la mémoire aussi !

En Ruby, vous n'avez pas à déclarer une taille spécifique _à l'avance_, mais c'est parce que Ruby le gère pour vous automatiquement grâce aux tableaux dynamiques.

Ce qu'un tableau dynamique fait, c'est que si le tableau approche de sa capacité maximale, il déclarera automatiquement un nouveau tableau plus grand et déplacera tous les éléments existants dedans, et l'ancien tableau sera alors collecté par le garbage collector. De combien plus grand ? Le facteur de croissance est _généralement_ 2 ; le double de la taille du tableau actuel.

**En fait, ne me croyez pas sur parole.**

Ruby dispose d'un module [ObjectSpace](https://ruby-doc.org/core-2.2.0/ObjectSpace.html) qui nous permet d'interagir avec les objets actuels vivant en mémoire. Nous pouvons utiliser ce module pour jeter un coup d'œil à l'utilisation de la mémoire de notre tableau dynamique — cela semble exactement ce que nous voulons !

J'ai écrit un petit script Ruby qui calcule le facteur de croissance du tableau dynamique. N'hésitez pas à y jeter un coup d'œil [ici](https://gist.github.com/edisonywh/c61b3ab50359e68454d87b2c13d5d1a8), et si vous le faites, vous pouvez voir que les tableaux Ruby ont un facteur de croissance de 1,5x (c'est-à-dire qu'ils créent un tableau 50 % plus grand à chaque copie).

### Je sais ce que sont les tableaux, mais qu'est-ce que les listes chaînées ?

Gardez à l'esprit que bien que les tableaux et les listes chaînées soient tous deux considérés comme des structures de données linéaires, ils ont une grande différence entre eux.

Les éléments d'un tableau sont stockés littéralement les uns à côté des autres en mémoire (donc nous pouvons avoir un index pour des recherches rapides). Mais les nœuds dans les listes chaînées n'ont pas une telle restriction (c'est pourquoi il n'y a pas de recherche par index pour les listes chaînées) — chaque élément peut être stocké n'importe où sur le bloc mémoire.

C'est presque comme si Timmy essayait de stocker 5 pièces de bagages, et que le concierge n'avait pas d'espace et décidait de les laisser partout. Cela semble désorganisé ?

De plus, s'ils sont stockés dans différents endroits, comment savez-vous quels sacs sont ceux de Timmy ? _Indice : Il suffit de suivre le nœud/sac suivant !_ Dans notre cas, le concierge les garde séparément mais avec une étiquette sur chacun d'eux qui pointe vers le sac suivant.

Un nœud dans une liste chaînée se compose de deux parties — la partie données et un pointeur vers le nœud suivant. C'est ainsi qu'ils sont capables de maintenir la partie `linéaire` — ils ont toujours le concept d'ordre, ils n'ont juste pas à être stockés dans l'ordre littéralement !

`node = [ data | pointer ]`

Par exemple, étant donné l'exemple suivant stocké en mémoire :

`[C | D] [A | B] [B | C] [D | nil]`

Ces bits semblent être dans le désordre — mais si je vous avais dit que le premier élément est `A`, vous seriez capable de me dire l'ordre exact de la liste :

`list = [A -> B -> C -> D -> nil]`

Il y a beaucoup de choses intéressantes que vous pouvez faire avec les listes chaînées que je ne vais pas explorer ici (aussi beaucoup sur Big O que je n'ai pas abordé). Mais il y a déjà beaucoup de bons articles sur les structures de données. Si vous êtes arrivé jusqu'ici, je vous suggère de lire l'article de blog d'Ali [ici](https://dev.to/aspittel/thank-u-next-an-introduction-to-linked-lists-4pph).

[**thank u, next: une introduction aux listes chaînées**](https://dev.to/aspittel/thank-u-next-an-introduction-to-linked-lists-4pph)
[_Dans cet article, nous allons parler de la structure de données de liste chaînée dans le langage de "thank u, next" par
_dev.to](https://dev.to/aspittel/thank-u-next-an-introduction-to-linked-lists-4pph)

Vous pouvez également lire plus sur List/Cons sur [Wiki ici](https://en.wikipedia.org/wiki/Cons).

### Note de clôture

J'ai initialement écrit cet article pour un sujet légèrement différent — [[ Elixir | Pourquoi les listes chaînées ?]](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d), mais j'ai trouvé que cela prenait trop de temps pour expliquer comment fonctionnent les tableaux avant de pouvoir explorer pourquoi Elixir utilise des listes chaînées. Je les ai donc séparés en deux articles.

Dans cet article, je parle de pourquoi les langages fonctionnels utilisent des listes chaînées comme leur structure de données linéaire. Allez y jeter un coup d'œil !

[**[ Elixir | Pourquoi les listes chaînées ? ]**](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d)
[_J'ai toujours pensé que les structures de données étaient cool, mais vous savez ce qui est encore plus cool ? Les voir en action ! En parcourant
_dev.to](https://dev.to/edisonywh/-elixir--why-linked-lists--1e9d)

### Sources

1. [https://medium.com/@rebo_dood/ruby-has-a-memory-problem-part-1-7887bbacc579](https://medium.com/@rebo_dood/ruby-has-a-memory-problem-part-1-7887bbacc579) — C'est là que j'ai découvert des méthodes supplémentaires `ObjectSpace` en l'exigeant

_Publié à l'origine sur [dev.to](https://dev.to/edisonywh/how-arrays-work-the-way-arrays-work-3bpg)_