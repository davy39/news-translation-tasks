---
title: Comment comprendre la mémoire de votre programme
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-20T18:15:08.000Z'
originalURL: https://freecodecamp.org/news/understand-your-programs-memory-92431fa8c6b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*VHc4F6eq1k7ZiOnT.jpg
tags:
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: software
  slug: software
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment comprendre la mémoire de votre programme
seo_desc: 'By Tiago Antunes

  When coding in a language like C or C++ you can interact with your memory in a more
  low-level way. Sometimes this creates a lot of problems you didn’t get before: segfaults.
  These errors are rather annoying, and can cause you a lot o...'
---

Par Tiago Antunes

Lorsque vous codez dans un langage comme C ou C++, vous pouvez interagir avec votre mémoire de manière plus bas niveau. Parfois, cela crée beaucoup de problèmes que vous n'aviez pas avant : **les segfaults**. Ces erreurs sont plutôt ennuyeuses et peuvent vous causer beaucoup de problèmes. Elles sont souvent des indicateurs que vous utilisez de la mémoire que vous ne devriez pas utiliser.

L'un des problèmes les plus courants est l'accès à une mémoire qui a déjà été libérée. Il s'agit de mémoire que vous avez soit libérée avec `free`, soit de mémoire que votre programme a automatiquement libérée, par exemple depuis la pile.

Comprendre tout cela est vraiment simple et cela vous permettra définitivement de mieux programmer et de manière plus intelligente.

### Comment la mémoire est-elle divisée ?

![Image](https://cdn-media-1.freecodecamp.org/images/6xEDNU7MCJLyXyOTKwWtml4uq6-mJLcTC221)
_High signifie **hautes adresses**_

La mémoire est divisée en plusieurs segments. Deux des plus importants pour cet article sont la **pile** et le **tas**. La pile est un endroit d'insertion ordonné tandis que le tas est aléatoire — vous allouez de la mémoire où vous pouvez.

La mémoire de la pile a un ensemble de méthodes et d'opérations pour son fonctionnement. C'est là que certaines informations des registres du processeur sont sauvegardées. Et c'est là que les informations pertinentes sur votre programme sont stockées — quelles fonctions sont appelées, quelles variables vous avez créées, et d'autres informations. Cette mémoire est également gérée par le programme et **non** par le développeur.

Le tas est souvent utilisé pour allouer de grandes quantités de mémoire qui doivent exister aussi longtemps que le développeur le souhaite. Cela dit, **c'est au développeur de contrôler l'utilisation de la mémoire sur le tas**. Lorsque vous construisez des programmes complexes, vous devez souvent allouer de grands blocs de mémoire, et c'est là que vous utilisez le tas. Nous appelons cela la **mémoire dynamique**.

Vous placez des éléments sur le tas chaque fois que vous utilisez `malloc` pour allouer de la mémoire pour quelque chose. Tout autre appel comme `int i;` est de la mémoire de pile. Savoir cela est vraiment important pour que vous puissiez facilement trouver des erreurs dans votre programme et améliorer votre recherche d'erreurs de segfault.

### Comprendre la pile

Bien que vous ne le sachiez peut-être pas, votre programme alloue constamment de la mémoire de pile pour fonctionner. Chaque variable locale et chaque fonction que vous appelez y est stockée. Avec cela, vous pouvez faire beaucoup de choses — la plupart d'entre elles sont des choses que vous ne vouliez pas voir arriver — comme des débordements de tampon et l'accès à une mémoire incorrecte.

Alors, comment cela fonctionne-t-il vraiment ?

La pile est une structure de données LIFO (Last-In-First-Out). Vous pouvez la voir comme une boîte de livres parfaitement ajustés — le dernier livre que vous placez est le premier que vous retirez. En utilisant cette structure, le programme peut facilement gérer toutes ses opérations et portées en utilisant deux opérations simples : **push** et **pop**.

Ces deux opérations font exactement l'inverse l'une de l'autre. Push insère la valeur au sommet de la pile. Pop prend la valeur supérieure.

![Image](https://cdn-media-1.freecodecamp.org/images/1Xc0oMmDVCRDzuluEcIFY5tJdBJ5POqDFLxx)
_Opérations Push et Pop._

Pour suivre l'emplacement actuel de la mémoire, il existe un registre spécial du processeur appelé **Stack Pointer**. Chaque fois que vous devez sauvegarder quelque chose — comme une variable ou l'adresse de retour d'une fonction — il pousse et déplace le pointeur de pile vers le haut. Chaque fois que vous quittez une fonction, il dépile tout depuis le pointeur de pile jusqu'à l'adresse de retour sauvegardée de la fonction. C'est simple !

Pour tester si vous avez compris, utilisons l'exemple suivant (essayez de trouver le bug seul 😊) :

![Image](https://cdn-media-1.freecodecamp.org/images/7qQgG58GTkftIbYS7OjWQNZeJDEO002WSn8J)
_Tout semble correct — jusqu'à ce que vous l'exécutiez._

Si vous l'exécutez, le programme provoquera simplement un segfault. Pourquoi cela arrive-t-il ? Tout semble en place ! Sauf pour... la pile.

Lorsque nous appelons la fonction `createArray`, la pile :

* sauvegarde l'adresse de retour,
* crée `arr` dans la mémoire de la pile et le retourne (un tableau est simplement un pointeur vers un emplacement mémoire avec ses informations)
* mais comme nous n'avons pas utilisé `malloc`, il est sauvegardé dans la mémoire de la pile.

Après avoir retourné le pointeur, comme nous n'avons aucun contrôle sur les opérations de la pile, le programme dépile les informations de la pile et les utilise comme il en a besoin. Lorsque nous essayons de remplir le tableau après être retourné de la fonction, nous corrompons la mémoire — provoquant un segfault du programme.

### Comprendre le tas

Contrairement à la pile, le tas est ce que vous utilisez lorsque vous voulez que quelque chose existe pendant un certain temps indépendamment des fonctions et des portées. Pour utiliser cette mémoire, la bibliothèque standard **stdlib** de C est vraiment bonne car elle apporte deux fonctions géniales : `malloc` et `free`.

**Malloc** (allocation de mémoire) demande au système la quantité de mémoire demandée et retourne un pointeur vers l'adresse de départ. **Free** indique au système que la mémoire que nous avons demandée n'est plus nécessaire et peut être utilisée pour d'autres tâches. Cela semble vraiment simple — tant que vous évitez les erreurs.

Le système ne peut pas outrepasser ce que les développeurs ont demandé. Cela dépend donc de nous, humains, de la gérer avec les deux fonctions ci-dessus. Cela ouvre la porte à une erreur humaine : les fuites de mémoire.

Une fuite de mémoire est une mémoire qui a été demandée par l'utilisateur mais qui n'a jamais été libérée — lorsque le programme s'est terminé ou que les pointeurs vers ses emplacements ont été perdus. Cela fait que le programme utilise beaucoup plus de mémoire que ce qu'il était censé utiliser. Pour éviter cela, chaque fois que nous n'avons plus besoin d'un élément alloué sur le tas, nous le libérons.

![Image](https://cdn-media-1.freecodecamp.org/images/bQ9wKhnYnJ10TyPVzva87ePnOCJCbL92il57)
_Pointeurs : mauvaise vs bonne méthode._

Dans l'image ci-dessus, la mauvaise méthode ne libère jamais la mémoire que nous avons utilisée. Cela finit par gaspiller 20 * 4 octets (taille de l'int en 64 bits) = 80 octets. Cela peut ne pas sembler beaucoup, mais imaginez ne pas faire cela dans un programme géant. Nous pouvons finir par gaspiller des gigaoctets !

Gérer votre mémoire de tas est essentiel pour rendre vos programmes efficaces en mémoire. Mais vous devez également être prudent sur la manière dont vous l'utilisez. Tout comme dans la mémoire de pile, **après que la mémoire a été libérée, y accéder ou l'utiliser peut provoquer un segfault.**

### Bonus : Structures et le tas

L'une des erreurs courantes lors de l'utilisation de structures est de simplement libérer la structure. Cela est correct, **tant que** nous n'avons pas alloué de mémoire aux pointeurs à l'intérieur de la structure. Si de la mémoire est allouée aux pointeurs à l'intérieur de la structure, nous devons d'abord les libérer. Ensuite, nous pouvons libérer toute la structure.

![Image](https://cdn-media-1.freecodecamp.org/images/UyQVaM0D6gOZitzmY7KCpqLgIlsOaLt5ORHh)
_Regardez comment j'ai utilisé free_

### Comment je résous mes problèmes de fuite de mémoire

La plupart du temps, lorsque je programme en C, j'utilise des structures. Par conséquent, j'ai toujours deux fonctions obligatoires à utiliser avec mes structures : le **constructeur** et le **destructeur**.

Ces deux fonctions sont les seules où j'utilise malloc et free sur la structure. Cela rend la résolution des fuites de mémoire vraiment simple et facile.

(Si vous souhaitez en savoir plus sur la manière de rendre le code plus facile à lire, [consultez mon article sur l'abstraction](https://medium.com/@tm.antunes/make-your-code-understandable-by-using-abstraction-4b522307130c)).

![Image](https://cdn-media-1.freecodecamp.org/images/LGoJhYkKmZZpPOOYOLSGZcuQHiTGpJS-GADL)
_Une façon de créer, et une façon de détruire !_

### Un excellent outil de gestion de la mémoire — Valgrind

Il est difficile de gérer votre mémoire et de vous assurer que vous avez tout géré correctement. Un excellent outil pour valider si votre programme se comporte correctement est [Valgrind](https://en.wikipedia.org/wiki/Valgrind). Cet outil valide votre programme, vous indiquant combien de mémoire vous avez allouée, combien a été libérée, si vous avez essayé d'écrire dans une zone de mémoire incorrecte... L'utiliser est un excellent moyen de valider si tout est correct, et chacun devrait l'utiliser pour éviter les compromis de sécurité.

![Image](https://cdn-media-1.freecodecamp.org/images/sN5lRHdCPsyLAicAokhZ4q4kDVgYrodPwh8l)
_Un exemple d'utilisation de valgrind, vous donnant des informations sur ce qui s'est mal passé_

### N'oubliez pas de me suivre !

En plus de poster ici sur Medium, je suis également sur [Twitter](https://twitter.com/tm_antunes).

Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter.