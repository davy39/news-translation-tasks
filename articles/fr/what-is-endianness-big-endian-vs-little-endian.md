---
title: Qu'est-ce que l'endianness ? Big-Endian vs Little-Endian expliqué avec des
  exemples
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-02-01T23:23:58.000Z'
originalURL: https://freecodecamp.org/news/what-is-endianness-big-endian-vs-little-endian
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Endianness.png
tags:
- name: binary
  slug: binary
- name: Computer Science
  slug: computer-science
seo_title: Qu'est-ce que l'endianness ? Big-Endian vs Little-Endian expliqué avec
  des exemples
seo_desc: 'Computers only understand binary. This means that 0''s and 1''s make up
  the language computers work with.

  One bit is one 0 or 1. 8 bits make up a byte. From these simple pieces we can build
  incredibly complex connected computer systems to render videos...'
---

Les ordinateurs ne comprennent que le binaire. Cela signifie que les `0` et les `1` constituent le langage avec lequel les ordinateurs fonctionnent.

Un bit est un `0` ou un `1`. 8 bits constituent un **octet**. À partir de ces simples éléments, nous pouvons construire des systèmes informatiques incroyablement complexes pour rendre des vidéos, afficher du texte du monde entier et calculer des algorithmes extrêmement complexes.

Certaines données (certains caractères anglais comme a, e, i, o et u) peuvent être représentées par un octet, mais certaines pièces de données nécessitent plusieurs octets pour être représentées.

Mais l'**endianness** est une partie fondamentale de la manière dont les ordinateurs lisent et comprennent les octets.

## Qu'est-ce que l'endianness ?

Différentes langues lisent leur texte dans différents ordres. L'anglais se lit de gauche à droite, par exemple, tandis que l'arabe se lit de droite à gauche.

C'est exactement ce qu'est l'**endianness** pour les ordinateurs.

Si mon ordinateur lit les **octets** de gauche à droite, et que votre ordinateur lit de droite à gauche, nous allons avoir des problèmes lorsque nous devons communiquer.

L'**endianness** signifie que les octets en mémoire informatique sont lus dans un certain ordre.

Nous n'aurons aucun problème si nous n'avons jamais besoin de partager des informations. Chaque ordinateur est interne cohérent pour ses propres données. C'est juste que l'internet nous a permis de partager plus de données que jamais auparavant, et nos données ne sont pas toujours **lues** dans le même ordre.

L'**endianness** est représenté de deux manières : **Big-endian** (**BE**) et **Little-endian** (**LE**).

* **BE** stocke le **big-end** en premier. Lors de la lecture de plusieurs octets, le premier octet (ou l'adresse mémoire la plus basse) est le plus grand - donc il a le plus de sens pour les personnes qui lisent de gauche à droite.
* **LE** stocke le **little-end** en premier. Lors de la lecture de plusieurs octets, le premier octet (ou l'adresse mémoire la plus basse) est le plus petit - donc il a le plus de sens pour les personnes qui lisent de droite à gauche.

Si ce qui précède ne vous semble pas clair, ce n'est pas grave - regardons un exemple.

## Exemple de fonctionnement de l'endianness

Prenons un nombre que nous devons utiliser plusieurs octets pour représenter, et montrons les façons big-endian et little-endian dont il peut être représenté.

Nous prendrons un nombre qui nécessite trois octets pour être représenté en binaire.

Cela peut légèrement le simplifier, mais j'espère que cela servira d'explication visuelle utile.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Decimal-number_--1-.png)
_Un exemple binaire où les nombres big-endian et little-endian sont disposés dans l'ordre dans lequel ils seraient lus._

Le 0b au début est juste une notation pour indiquer aux lecteurs qu'il s'agit de binaire. Ainsi, nous savons la différence entre le binaire `1100` et 1,100 en tant que nombre décimal (mille cent). J'ai également utilisé des couleurs pour, je l'espère, rendre cela plus clair.

Je veux juste être clair que l'_ordre des bits_ est correct. Il n'y a pas de différence entre l'ordre des **bits**. Mais il y a une différence dans l'ordre correct des **octets**. J'espère que ce qui précède démontre que l'ordre des `0` et des `1` dans un octet ne change pas. Mais l'ordre des **octets** change.

Si nous n'avions jamais eu à envoyer qu'un seul **octet**, il n'y aurait pas de problème (il n'y a pas plusieurs façons d'ordonner une seule chose). Ce n'est un problème qu'avec une séquence de plus d'un **octet**.

## Octet le plus significatif (MSbyte)

La terminologie **Most Significant Byte** est une manière courante de décrire l'**endianness**, donc je veux m'assurer de la couvrir complètement.

Avant de commencer à expliquer avec des **bits** et des **octets**, faisons-le simplement avec un nombre décimal.

Si je prends le nombre décimal 2,984, quel nombre pourriez-vous changer pour changer le nombre par la plus petite quantité ? Le 4. Si je change le 4 en 5, le nombre entier n'augmente que de 1.

Mais disons que vous changez le 2 dans 2,984. Il changera le nombre de manière significative et augmentera de mille.

C'est exactement la même chose avec les **octets** et les **bits**.

Nous faisons référence à l'**octet** contenant la position la plus petite comme étant le **Least Significant Byte** (**LSbyte**) et au **bit** contenant la position la plus petite comme étant le **Least Significant Bit** (**LSbit**).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/MSbyte.png)
_Un diagramme pour illustrer que l'octet contenant les nombres de position les plus bas est l'octet le moins significatif._

L'octet qui contient la position la plus significative est appelé **Most Significant Byte** (**MSbyte**) et le bit contenant la position de bit la plus significative est le **Most Significant Bit** (**MSbit**).

Maintenant, connaissant cette nouvelle définition, nous pouvons définir **BE** et **LE** comme suit :

* Le big endian stocke les données **MSbyte** en premier
* Le little endian stocke les données **MSbyte** en dernier

## Quand cela peut-il poser problème ?

L'endianness doit être pris en compte dans l'informatique dans quelques cas différents.

Par exemple, les caractères Unicode (l'ensemble de caractères utilisé pour afficher des caractères sur votre téléphone, PC, TV, partout !) doivent passer une séquence spéciale d'octets de caractères (U+FEFF BYTE ORDER MARK) appelée **Byte Order Mark** ou **BOM**. Le **BOM** sert quelques objectifs.

Le **BOM** rend le système conscient :

* Que le flux entrant est Unicode.
* De l'encodage de caractères Unicode utilisé.
* De l'ordre **endian** du flux entrant.

Certains langages de programmation s'attendent même à ce que vous détailliez quelle séquence d'ordre d'octets est utilisée. Ainsi, un programme peut utiliser, envoyer et recevoir des nombres en **BE** ou **LE** selon ce que vous souhaitez. Swift est un exemple de cela (le langage utilisé pour le développement iOS).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/image-206.png)
_La documentation Apple détaillant comment obtenir la représentation little-endian d'un Integer._

Vous pouvez lire du code Swift [ici](https://gist.github.com/vukcevich/fa793c8bcb55b14b6e0a0700f5f7316b) pour un exemple d'échange d'octets pour obtenir des représentations little et big-endian de `Integer`s.

## Pourquoi est-ce même un problème en premier lieu ?

Il se trouve simplement que différents protocoles ont émergé et ont ensuite dû interagir les uns avec les autres. **BE** est l'ordre dominant dans les protocoles réseau, et est appelé **network order**, par exemple. D'autre part, la plupart des PC sont **little-endian**.

Vous pouvez exécuter un extrait de code C++ en ligne [ici](http://cpp.sh/524wi) pour voir quel est l'endian de votre machine (le mien est **little-endian**).

L'**endianness** a largement cessé d'importer avec les langages de haut niveau et l'abstraction des détails d'implémentation particuliers dont nous n'avons pas à nous soucier.

Une autre partie de cela est que les processeurs décident s'ils sont little-endian ou big-endian (ou peuvent gérer les deux - appelé **Bi-endian**) donc le choix des consommateurs a conduit une partie de ce que nous considérons comme "normal" dans nos systèmes informatiques.

## Conclusion

J'espère que cet article a expliqué ce qu'est l'endianness, ce que sont le big-endian et le little-endian, et que vous comprenez maintenant ces concepts plus clairement.

Je partage mes écrits sur [Twitter](https://twitter.com/kealanparr) si vous avez aimé cet article et voulez en voir plus.