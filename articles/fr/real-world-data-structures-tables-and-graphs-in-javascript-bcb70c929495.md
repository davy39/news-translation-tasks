---
title: 'Structures de données du monde réel : tables et graphes en JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-22T16:20:55.000Z'
originalURL: https://freecodecamp.org/news/real-world-data-structures-tables-and-graphs-in-javascript-bcb70c929495
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l60KCqKpGbwvSTqO301VZg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Structures de données du monde réel : tables et graphes en JavaScript'
seo_desc: 'By Yung L. Leung

  An aerial view of boxes with addresses, each containing people & various items,
  shows neighborhoods connected by their roads. Viewed up close, you may say that
  we have a hash table. But, when viewed from afar, you might see a graph. ...'
---

Par Yung L. Leung

Une vue aérienne de boîtes avec des adresses, chacune contenant des personnes et divers objets, montre des quartiers connectés par leurs routes. Vue de près, on pourrait dire que nous avons une **table de hachage**. Mais, vue de loin, on pourrait voir un **graphe**. En progressant depuis les structures de données [**linéaires**](https://medium.com/@yunglleung1/linear-data-structures-linked-lists-stacks-queues-a13c7591ad87) **(**listes chaînées, piles et files d'attente**)** et [**binaires**](https://medium.com/@yunglleung1/binary-data-structures-trees-heaps-962ab536cb42) **(**arbres binaires de recherche, tas binaires**), les **tables de hachage** et les **graphes** sont des étapes vers une plus grande diversité d'applications du monde réel.

### Tables

Une **table de hachage** représente des données (paires clé-valeur) tabulées par des index.

![Image](https://cdn-media-1.freecodecamp.org/images/ZUvaqYuUfuop4ImFdmh8ETIYuIOzpdTKRA4l)
_[source](https://www.geeksforgeeks.org/implementing-our-own-hash-table-with-separate-chaining-in-java/" rel="noopener" target="_blank" title=")_

Chaque clé unique est utilisée pour générer un index (fonction de hachage). Une fonction de hachage peut générer le même index pour plusieurs clés uniques (**collision**). Une solution à ce problème est de stocker les ensembles de données sous le même index (**chaînage**).

Ainsi, vous pouvez imaginer une **table de hachage** comme un système pour ranger des articles similaires ensemble. Il suffit d'entrer le nom de l'article dans une **fonction de hachage** et tous les articles de type verdâtre se verront attribuer un espace sur l'étagère, par exemple 4.

![Image](https://cdn-media-1.freecodecamp.org/images/ZUHz2n8mBe59eDg2pYEh5lKSwqoH8tx25K3p)
_[source](http://verticalcarousel.com.au/wp-content/uploads/2015/05/003.gif" rel="noopener" target="_blank" title=")_

En général, l'**insertion** d'une paire clé-valeur nécessite de générer un **index** (numéro d'étagère), de vérifier si cette étagère existe et de placer l'article (**donnée**) sur l'étagère. Supposons que j'ai des bananes et des pommes sur l'étagère du bas (**index 0**) et du vin rouge sur mon étagère du haut (**index 2**).

![Image](https://cdn-media-1.freecodecamp.org/images/LGr1DoJ-ff7xBfWKUNsvjzAhBRyvyfbu2at-)
_**Articles en stock : 10 bananes, 20 pommes et 3 bouteilles de vin rouge**_

Si mon générateur d'index (**fonction de hachage**) retourne un **index 2** pour mes 2 "poulets rôtis", l'insertion de ces données nécessite de vérifier et de créer de l'espace sur l'étagère.

![Image](https://cdn-media-1.freecodecamp.org/images/kuBoqej6nIc86-NkYK3dn4dSacva67PQ-Cg9)
_**Articles en stock ajoutés : 2 poulets rôtis**_

Pour obtenir une **valeur** (article), il faut entrer son nom (**clé**) pour générer son index (numéro d'étagère) et récupérer tous les articles sur cette étagère. Ensuite, rechercher l'article exact (son nom ou sa clé) et le récupérer (retourner la valeur). Ainsi, pour trouver combien de pommes sont en stock (**20**), il faut parcourir mon étagère de fruits.

Pour obtenir une liste de toutes les **clés** ou **valeurs**, il faut parcourir chaque étagère existante, les enregistrer dans votre manifeste (les ajouter à un tableau) et soumettre les documents (retourner le tableau des clés ou des valeurs).

![Image](https://cdn-media-1.freecodecamp.org/images/2dzLy-laxGEJeh-82AriZNVRZrFNR3nc8DSX)
_**Clés (articles) et Valeurs (quantité) de la Table de Hachage (étagères d'articles en stock)**_

La complexité pour **insérer** une paire clé-valeur ou **accéder** à une valeur est, en général, un temps constant (**O(1)**). Une bonne fonction de hachage répartit uniformément tous les articles sur toutes les étagères disponibles. Ainsi, l'**insertion ou l'accès** ne nécessite pas de parcourir toutes les étagères existantes pour le stockage ou la récupération des données.

Parce que le catalogage (**clés ou valeurs**) nécessite de parcourir toutes les étagères, il a une complexité **O(n)**. Pour **n** ensembles de données différents (pour 4 articles différents), il faut **n étapes** pour effectuer un catalogage (nécessite de parcourir les 4 articles pour documenter leur nom ou leur quantité).

### Graphes

Un **graphe** est un ensemble de nœuds (**sommets**) de données reliés par leurs connexions (**arêtes**). Une carte routière de villes connectées par leurs routes est un graphe. Un graphe d'utilisateurs connectés d'une application de médias sociaux en est un autre exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/tigLuAgDy-UgPVLMxl1J8cY4Ad0ibhgHXkQG)
_[source](http://allthingsgraphed.com/2014/11/02/twitter-friends-network/" rel="noopener" target="_blank" title=")_

Pour **ajouter un sommet** et une **arête**, il faut les stocker sous forme de paires clé-valeur dans une **liste d'adjacence**. Ainsi, un sommet (New York) peut être connecté à d'autres sommets (New Jersey et Pennsylvanie) en faisant de "New York" une clé vers un tableau contenant "New Jersey", "Pennsylvanie".

![Image](https://cdn-media-1.freecodecamp.org/images/TIVezWjeMZplRJMlfSouOvwh0aLT2JjOlllu)
_**Liste de tous les États adjacents à New York**_

L'inverse doit également être implémenté, c'est-à-dire : "New Jersey" pointant vers un tableau de "New York", "Pennsylvanie", et ainsi de suite. Ainsi, le résultat est une liste d'adjacence de clés ("New York", "New Jersey", "Pennsylvanie"), chacune pointant vers des tableaux de leurs connexions correspondantes.

![Image](https://cdn-media-1.freecodecamp.org/images/WxoaIC-fYN31u0y7wUSLzoYyyPI2MMKrWEQk)
_**Liste d'adjacence complète de Google Maps**_

Pour **supprimer une arête**, il faut supprimer la connexion du sommet1 au sommet2 et vice versa. Ainsi, pour supprimer la connexion de New York au New Jersey, il faut également supprimer la connexion du New Jersey à New York.

![Image](https://cdn-media-1.freecodecamp.org/images/s5U41Kuzl32KdTufMakqs46-ae2bXCTEtJ-y)
_**Liste d'adjacence mise à jour de Google Maps**_

Pour **supprimer un sommet**, il faut parcourir ses connexions. Supprimer ses arêtes avant de finalement supprimer le sommet de la liste d'adjacence. Ainsi, pour supprimer New York, il faut le déconnecter de ses voisins avant de le supprimer de la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/LSlDfdqy6hctdAAbQo81-oFpT1P1ZFrhaZNU)
_**Liste d'adjacence sans New York de Google Maps**_

Relativement à un point de départ, un **parcours en profondeur** implique de visiter un voisin et ses voisins avant de procéder au prochain voisin immédiat. Un **parcours en largeur** implique de visiter tous les voisins immédiats avant les voisins éloignés.

Ainsi, pour un graphe avec New York, New Jersey, Pennsylvanie et Virginie comme sommets, un **parcours en profondeur** commençant par le New Jersey serait ["New Jersey", "Pennsylvanie", "Virginie", "New York"].

![Image](https://cdn-media-1.freecodecamp.org/images/bZWSlshOSxdFmeauaEAbiqYDVDVrfqn3FKdv)
_**Graphe de New York, New Jersey, Pennsylvanie et Virginie de Google Maps**_

Un **parcours en largeur** depuis le New Jersey serait ["New Jersey", "New York", "Pennsylvanie", "Virginie"].

Puisqu'un **graphe** est un ensemble de nœuds connectés, les structures de données [**linéaires**](https://medium.com/@yunglleung1/linear-data-structures-linked-lists-stacks-queues-a13c7591ad87) et [**binaires**](https://medium.com/@yunglleung1/binary-data-structures-trees-heaps-962ab536cb42) peuvent, en un sens, être vues comme des graphes simples. Parce que les graphes peuvent prendre de nombreuses formes et tailles différentes, la **complexité du parcours** à travers un graphe dépend des algorithmes utilisés pour le parcours, une discussion à réserver pour une autre fois.

### Références :

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)