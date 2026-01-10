---
title: Trouver l'équilibre entre la complexité temporelle et mémorielle — un exemple
  illustré
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-22T05:25:11.000Z'
originalURL: https://freecodecamp.org/news/finding-the-balance-between-time-and-memory-complexity-an-illustrated-example-4845ab7afadd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LWC0y01B6B8UOhVwVZcyyQ.png
tags:
- name: Android
  slug: android
- name: Data Science
  slug: data-science
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Trouver l'équilibre entre la complexité temporelle et mémorielle — un exemple
  illustré
seo_desc: 'By Anmol Uppal

  As programmers, we often have to trade-off between time and memory complexity. Managing
  one often means compromising on the other. It is hard to find the right sweet spot
  between them.

  The problem becomes even more pressing for Android...'
---

Par Anmol Uppal

En tant que programmeurs, nous devons souvent faire des compromis entre la complexité temporelle et mémorielle. Gérer l'une signifie souvent compromettre l'autre. Il est difficile de trouver le bon équilibre entre les deux.

Le problème devient encore plus pressant pour les appareils Android et iOS, qui ont des ressources relativement limitées.

Voyons comment nous pouvons trouver ce "sweet spot" à l'aide d'un exemple. Notre exemple sera de développer une requête qui vérifie si un mot donné est présent dans le dictionnaire anglais ou non.

Le cas d'utilisation est très spécifique aux applications de saisie de texte (comme un clavier de téléphone mobile), mais les concepts utilisés dans cet article peuvent être utilisés dans d'autres domaines également.

Les structures de données souvent appliquées à ce problème incluent :

* Set
* Trie
* HashMap

Parmi ces structures de données, Trie est spécialement conçu pour la vérification orthographique. Les autres structures de données sont génériques et peuvent être appliquées à de nombreux types de données. Visualisons comment Trie fonctionne.

#### Comprendre Trie

Supposons que nous n'avons que quatre mots dans le dictionnaire, par exemple : "hello", "world", "he" et "win".

Nous pouvons visualiser un Trie pour ce dictionnaire comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/PPLPKmyFAnoPnxQoc9ob4IuLtZ0iAXUXl8Gn)
_Visualisation d'un Trie d'exemple_

Les cercles rouges marquent la terminaison d'un mot valide. La structure Trie maintient une hiérarchie de relations parent-enfant valides. Chaque nœud contient au moins ces trois champs :

```
TrieNode {    char            character;  // a, b, c, d, ... y, z    boolean         isTerminal; // Si ce nœud se termine par un mot valide    List<TrieNode>  children;   // Liste des nœuds enfants.}
```

Une discussion détaillée sur la construction de Trie n'est pas dans le cadre de cet article, mais nous aborderons brièvement comment une recherche est effectuée dans Trie :

![Image](https://cdn-media-1.freecodecamp.org/images/YiPnUv0Hp9U7qLalllTFdVewHDGApfZ6OMdh)
_Visualisation de la recherche d'un mot dans Trie_

Supposons que dans le Trie ci-dessus (avec seulement quatre mots valides), nous devons rechercher si "hell" est un mot valide.

Nous commencerons par le nœud racine et prendrons "h", le premier caractère de "hell", puis nous parcourons les enfants du nœud racine. Si "h" est trouvé, alors nous parcourons les enfants de "h" et ignorons les autres enfants du nœud racine.

Ce processus se poursuit jusqu'à ce que nous atteignions le dernier caractère du mot recherché. Pour le dernier caractère, "l", nous vérifions également le champ `isTerminal` de ce nœud. Dans ce cas, il est `false`, car les mots valides dans ce dictionnaire étaient "he", "hello", "win" et "world" uniquement.

#### Introduction à MagicDict

MagicDict tire parti des propriétés spécifiques à la langue que Trie a négligées :

* Tous les caractères (a-z) peuvent être imaginés comme une plage d'entiers continus (0-26).

Puisque tous les caractères enfants possibles (a-z) pour un nœud donné peuvent être réalisés comme une plage d'entiers contigus, nous pouvons utiliser un tableau de valeurs `Boolean` pour représenter les enfants.

Nous utiliserons un tableau `Boolean` de taille 26, avec tous les éléments `False` comme valeur initiale. Nous avons également besoin d'un autre tableau de 26 valeurs `Boolean` pour représenter `isTerminal`.

![Image](https://cdn-media-1.freecodecamp.org/images/7C63nuYNYz-IBMbJxAqhvTyrP-ENpkqBrPGp)
_Visualisation de Magic Dict de la relation parent-enfant_

Ce seul tableau 2D représente uniquement 1 niveau de relations parent-enfant. Pour la langue anglaise avec 26 caractères, la taille du tableau 2D serait de : 26 x 52.

Nous pouvons les empiler les uns sur les autres. Cela signifie que les enfants de la 1ère couche deviennent les parents dans la 2ème couche, les enfants de la 2ème couche deviennent les parents dans la 3ème... et ainsi de suite. Cela forme une sorte de structure enchaînée, et les éléments de base de MagicDict.

#### Insertion dans MagicDict

Nous construisons une pile de couches 2D, où le nombre de couches nécessaires pour construire la pile est `longest_word_length - 1`.

Pour l'ensemble précédent de mots : "he", "hello", "win" et "world", `longest_word_length` est égal à 5. Nous devons donc réserver une taille de pile de 4.

Supposons que nous voulons insérer "hello" dans cette structure de données. Nous commençons avec la première paire {"h" et "e"}, et activons le drapeau booléen `isChildren` correspondant dans la couche 1.

Ensuite, nous prenons la paire suivante {"e", "l"}, en activant de manière similaire le drapeau booléen `isChildren` correspondant dans la couche 2. Ce processus est répété jusqu'à ce que nous atteignions la paire de terminaison {"l" et "o"}, où nous activons également le drapeau booléen `isTerminal` correspondant.

L'ensemble du processus peut être visualisé comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/yRWRIGSB3v379RL0esoaPcHvDJhVn-ed53BH)

#### Recherche dans MagicDict

La recherche suit le même flux que l'insertion. La seule différence est que dans l'insertion, nous changeons les valeurs de bits. Mais dans le cas de la recherche, nous lisons uniquement les valeurs pour vérifier si la séquence de caractères dans le mot de la requête est valide.

#### La touche finale de magie

Maintenant, nous avons une structure de données qui stocke _n_ tableaux 2D de taille 26 x 52. Chaque tableau 2D stocke 1352 valeurs booléennes (vrai/faux).

Nous savons également que les valeurs booléennes prennent au plus 1 octet de mémoire (puisque la plus petite unité adressable de mémoire est un octet). Consommer 1 octet pour stocker un drapeau `Boolean` n'est pas le scénario idéal.

Et si nous pouvions trouver un type de données suffisamment grand pour contenir les drapeaux booléens du tableau 2D sous forme de motif binaire contigu ?

Il s'avère qu'il n'y en a aucun ! Les types de données primitifs ont des représentations 8 bits, 16 bits, 32 bits, 64 bits, 128 bits... mais aucun type de données primitif n'est suffisamment grand pour stocker 1352 bits contigus.

Le motif binaire contigu disponible le plus proche semble être 64 bits, qui est également connu sous le nom de `long` dans certains langages. Nous remplaçons les lignes dans notre tableau 2D par une valeur `long` contenant 64 bits.

![Image](https://cdn-media-1.freecodecamp.org/images/QlewRRyDy1IM0Ed27NRKgs0zctAE2jRPsuiI)
_Visualisation du tableau booléen en tant que motif binaire contigu_

Pour un dictionnaire avec une longueur maximale de mot de 21, et chaque couche consommant 26 x 8 octets, la taille totale de la structure de données serait de 4 160 octets.

#### Benchmarking

Nous avons analysé 370 000 mots de la langue anglaise à partir de ce [dépôt Github](https://github.com/dwyl/english-words/blob/master/words_alpha.txt), et enregistré le temps pris pour :

* Insertion de 370 000 mots
* Suppression de 100 000 mots
* Requête de 100 000 mots (50 000 mots existants, 50 000 mots non existants)

Et nous avons également examiné la consommation de mémoire estimée de diverses structures de données.

![Image](https://cdn-media-1.freecodecamp.org/images/LDFj948LxO02P9vN-GfgN0tQmPH59yePR8qd)
_Benchmarks pratiques pour les structures de données grand public_

#### **Réflexions finales**

Ce modèle initial ne possède pas de fonctionnalités extensives. Mais il pourrait être étendu à d'autres langues que l'anglais en utilisant des types de données plus grands.

Le principal enseignement de cette structure de données est l'utilisation efficace de l'espace, tout en améliorant les performances d'exécution. Cela se rapproche du scénario "le meilleur des deux mondes".

Pour des informations détaillées sur la mise en œuvre de cette structure de données, vous pouvez consulter le [code source de MagicDict](https://github.com/anmoluppal/MagicDict).