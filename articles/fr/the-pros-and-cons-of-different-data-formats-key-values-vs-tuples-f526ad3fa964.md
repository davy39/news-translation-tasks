---
title: 'Les avantages et inconvénients des différents formats de données : paires
  clé-valeur vs tuples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-28T16:44:57.000Z'
originalURL: https://freecodecamp.org/news/the-pros-and-cons-of-different-data-formats-key-values-vs-tuples-f526ad3fa964
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1LI9TzwDU1l6IyJFBRcULw.jpeg
tags:
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
seo_title: 'Les avantages et inconvénients des différents formats de données : paires
  clé-valeur vs tuples'
seo_desc: 'By Hieu Nguyen (Jack)

  How data is formatted under the hood


  _Photo by [Unsplash](https://unsplash.com/photos/1K6IQsQbizI?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Franki Chamaki on <a ...'
---

Par Hieu Nguyen (Jack)

#### Comment les données sont formatées en interne

![Image](https://cdn-media-1.freecodecamp.org/images/7XaDSrL1K83J1dBxAzMjovGc4jrC9Hfqd968)
_Photo par [Unsplash](https://unsplash.com/photos/1K6IQsQbizI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Franki Chamaki</a> sur <a href="https://unsplash.com/search/photos/data?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Travailler sur [Vasern](http://github.com/vasern/vasern) (une base de données cliente pour React Native) m'a donné l'opportunité d'essayer et de tester différents formats de données, notamment les paires clé-valeur, les formats orientés colonnes, les documents et les tuples. Chaque format a été conçu pour répondre à différents scénarios.

Les critères de ces tests se concentrent sur la performance, la capacité à rechercher des valeurs et l'efficacité de l'espace. De plus, il n'est pas nécessaire d'avoir des clés et des indices triés sur disque. Ils seront chargés en mémoire pour une recherche rapide.

Dans cet article, je vais résumer les avantages et les inconvénients des deux formats courants : les **paires clé-valeur** et le **format de tuples**. Je vais également présenter les **paires clé-valeur étiquetées**, une extension des paires clé-valeur avec recherche d'index, qui bénéficie du format de tuples.

### Stockage Clé-Valeur

![Image](https://cdn-media-1.freecodecamp.org/images/D07YYA0726oX0lONmcxCzk9GUxcLbNa2c2Qn)
_Une collection de stockage clé-valeur_

Le stockage clé-valeur stocke une collection de paires clé-et-valeur, où parfois la valeur représente plus d'une valeur, séparée par des délimiteurs (par exemple, une virgule). Ces paires sont organisées en blocs de longueur fixe (pour un parcours rapide entre les enregistrements).

![Image](https://cdn-media-1.freecodecamp.org/images/mctmmR2ACQsQhkEYXwqTiYnLdOCvqHKKrDQO)
_Exemple de disposition de stockage clé-valeur à bloc unique ("\0" représente une valeur nulle/vide)_

**Avantages du stockage clé-valeur :**

* Format de données simple qui rend les opérations d'écriture et de lecture rapides
* La valeur peut être n'importe quoi, y compris du JSON, des schémas flexibles

**Inconvénients :**

* Optimisé uniquement pour les données avec une seule clé et une seule valeur. Un analyseur est nécessaire pour stocker plusieurs valeurs.
* Non optimisé pour la recherche. La recherche nécessite de scanner toute la collection ou de créer des valeurs d'index séparées

### Stockage de Données en Tuples (SGBDR)

Le format de données en tuples existe depuis de nombreuses décennies. Il est utilisé dans les bases de données relationnelles telles que MySQL, Postgres, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/a-xcLNN9JVKQjs6Jd8vPqZstcJDmixKSqfYq)
_Un exemple du format de données en tuples dans une base de données relationnelle_

Contrairement au format clé-valeur, il repose sur un schéma prédéfini pour organiser les enregistrements en lignes et ses valeurs en colonnes de longueur fixe. Chaque valeur représente généralement une seule information.

**Avantages du stockage de données en tuples :**

* Format de données structuré qui aide à parcourir rapidement les valeurs des enregistrements
* Optimisé pour la recherche (utilisation courante de SQL pour interroger les enregistrements)

**Inconvénients :**

* Contraint par la structure du schéma
* La modification du schéma nécessite généralement de réécrire toute la base de données

### Stockage Clé-Valeur Étiquetées

![Image](https://cdn-media-1.freecodecamp.org/images/J-Kuww82Dhi4q8ZQCrcMQ2CJGtZ88cWEIQiR)
_Uhmm, TKVF (format clé-valeur étiquetées)_

Les Clés-Valeurs Étiquetées sont une version étendue du stockage Clé-Valeur — elles ont plus d'une clé pour une seule valeur. En d'autres termes, elles ont une clé, des index (ou étiquettes) et une valeur de corps pour chaque enregistrement. Où :

* **Clé** et **Index** seront chargés en mémoire au démarrage
* **Valeur du corps** peut être n'importe quoi, d'une simple chaîne, BSON/JSON, ou une valeur séparée par des virgules.

**Avantages du stockage Clé-Valeur Étiquetées :**

* Semi-structuré, ce qui aide à parcourir rapidement les enregistrements et les index
* Optimisé pour la recherche (via les clés et les index)
* Le **corps** d'un enregistrement peut être n'importe quoi, idéal pour des schémas flexibles
* Efficacité de l'espace (clé, index sont organisés en colonnes serrées)

**Inconvénients :**

* La modification du schéma qui inclut les **index** peut nécessiter une migration des données

![Image](https://cdn-media-1.freecodecamp.org/images/-PoMvWSH9PIYAiyGs1141mhgVsyJQBliHyvP)
_Un exemple de format de clé-valeur étiquetées_

#### Vasern avec le Stockage Clé-Valeur Étiquetées

Vasern est une base de données cliente pour React Native. La dernière version a été publiée en bêta pour les tests et utilisait le stockage clé-valeur.

Dans la prochaine [**version 0.3.0-RC**](https://github.com/vasern/vasern/tree/0.3.0-rc)**,** Vasern passe à une disposition de stockage clé-valeur étiquetées. L'accent est mis sur sa puissante fonctionnalité de recherche et son efficacité spatiale.

Ci-dessous se trouve une démonstration de requête. C'est beau, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/Mo1NpiljkgEHIkRV1JxndzR1CgmqoHRiNY9v)
_Une démonstration de requête Vasern_

### Conclusion

Il existe de nombreuses bases de données avec différents formats de données à choisir pour une application. Deux formats courants sont :

* **Paires Clé-Valeur** — lecture et écriture rapides mais non optimisées pour la recherche. Elles sont souvent utilisées comme stockage de données simple, NoSQL.
* **Tuples** — supportent des valeurs multi-typées, des index, optimisées pour la recherche, mais manquent de flexibilité de schéma. Communément utilisées pour les bases de données relationnelles.

En combinant les forces mentionnées ci-dessus, le format **Clé-Valeur Étiquetées** est flexible avec le schéma de données et est capable de rechercher des enregistrements via des clés et des index. Cela est souvent mieux adapté pour une base de données cliente.

**Si vous avez trouvé cet article utile, veuillez cliquer sur le bouton** ? **plusieurs fois pour aider les autres à trouver l'article et montrer votre soutien ! ?**

**Merci d'avoir lu !**