---
title: Une introduction rapide à l'architecture propre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-13T16:14:09.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-clean-architecture-990c014448d2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*vIfjwJFIvgfyghgD
tags:
- name: Design
  slug: design
- name: design patterns
  slug: design-patterns
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
seo_title: Une introduction rapide à l'architecture propre
seo_desc: 'By Daniel Deutsch

  In an open source project I started to contribute to, the concept of “clean architecture”
  was brought to me.

  First, it was pretty overwhelming, but after some reading it made sense. I thought
  it might be helpful for others if I wrot...'
---

Par Daniel Deutsch

Dans un [projet open source](https://github.com/Keep-Current) auquel j'ai commencé à contribuer, le concept d'« architecture propre » m'a été présenté.

Au début, c'était assez intimidant, mais après quelques lectures, cela a commencé à avoir du sens. J'ai pensé qu'il pourrait être utile pour les autres si j'écrivais mes réflexions.

### Table des matières

* [Représentations visuelles](https://github.com/Createdd/Writing/blob/master/2018/articles/CleanA.md#representations-visuelles)
* [Le concept — présenté en points](https://github.com/Createdd/Writing/blob/master/2018/articles/CleanA.md#le-concept-present-en-points)
* [Exemple de code](https://github.com/Createdd/Writing/blob/master/2018/articles/CleanA.md#exemple-de-code)
* [Ressources](https://github.com/Createdd/Writing/blob/master/2018/articles/CleanA.md#ressources)

### Représentations visuelles

Je pense qu'il est toujours bon de commencer par quelques visualisations.

Voici les images les plus courantes de ce concept.

![Image](https://cdn-media-1.freecodecamp.org/images/oVVbTLR5gXHgP8Ehlz1qzRm5LLjX9kv2Zri6)

![Image](https://cdn-media-1.freecodecamp.org/images/YsN6twE3-4Q4OYpgxoModmx29I8zthQ3f0OR)
_Source et crédit : [https://www.codingblocks.net/podcast/clean-architecture-make-your-architecture-scream/](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html" rel="noopener" target="_blank" title="">https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html</a> .<a href="https://www.codingblocks.net/podcast/clean-architecture-make-your-architecture-scream/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/lbexLhWvRfpexSV0lSIWczkHd5KdszeDy9a3)

![Image](https://cdn-media-1.freecodecamp.org/images/YIABVRTHRz58ZiT6W-emBkfNIQUHBelp8t6U)
_Source et crédit : Mattia Battiston, sous CC BY 4.0, [https://github.com/mattia-battiston/clean-architecture-example](https://github.com/mattia-battiston/clean-architecture-example" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/TmSQbZOg5bxn0cRXxIrRUd2zhqeDAXTe8ni5)
_Source et crédit : [https://marconijr.com/posts/clean-architecture-practice/](https://marconijr.com/posts/clean-architecture-practice/" rel="noopener" target="_blank" title=")_

### Le concept — présenté en points

Étendu à partir de Source et crédit : [Mattia Battiston, sous CC BY 4.0](https://github.com/mattia-battiston/clean-architecture-example)

#### La valeur qu'elle peut apporter

* Une stratégie de test efficace qui suit la pyramide des tests
* Les frameworks sont isolés dans des modules individuels. Lorsque (et non si) nous changeons d'avis, nous n'avons qu'à faire un changement à un seul endroit. L'application a des cas d'utilisation plutôt que d'être liée à un système CRUD
* Architecture expressive, c'est-à-dire qu'elle exprime clairement son usage prévu. Lorsque vous regardez la structure des packages, vous comprenez ce que fait l'application plutôt que de voir des détails techniques
* Toute la logique métier est dans un cas d'utilisation, donc elle est facile à trouver et non dupliquée ailleurs
* Difficile de faire la mauvaise chose car les modules imposent des dépendances de compilation. Si vous essayez d'utiliser quelque chose que vous n'êtes pas censé utiliser, l'application ne compile pas
* Elle est toujours prête à être déployée en laissant le câblage des objets pour la fin. Ou en utilisant des drapeaux de fonctionnalité, afin que nous obtenions tous les avantages de l'intégration continue
* Plusieurs travaux sur des histoires afin que différentes paires puissent facilement travailler sur la même histoire en même temps pour la terminer plus rapidement
* Bon monolithe avec des cas d'utilisation clairs que vous pouvez diviser en microservices plus tard, une fois que vous en avez appris davantage à leur sujet

#### Entités

* Représentent votre objet de domaine
* Appliquent uniquement la logique qui est applicable en général à l'entité entière (par exemple, valider le format d'un nom d'hôte)
* Objets simples : pas de frameworks, pas d'annotations

#### Cas d'utilisation

* Représentent vos actions métier : c'est ce que vous pouvez faire avec l'application. Attendez-vous à un cas d'utilisation pour chaque action métier
* Logique métier pure, code simple (sauf peut-être quelques bibliothèques d'utilitaires)
* Le cas d'utilisation ne sait pas qui l'a déclenché et comment les résultats vont être présentés (par exemple, pourrait être sur une page web, ou — retourné en JSON, ou simplement journalisé, etc.)
* Lance des exceptions métier

#### Interfaces / Adaptateurs

* Récupèrent et stockent des données à partir de et vers un certain nombre de sources (base de données, appareils réseau, système de fichiers, tiers, etc.)
* Définissent des interfaces pour les données dont elles ont besoin afin d'appliquer une certaine logique. Un ou plusieurs fournisseurs de données implémenteront l'interface, mais le cas d'utilisation ne sait pas d'où viennent les données
* Implémentent les interfaces définies par le cas d'utilisation
* Il existe des moyens d'interagir avec l'application, et impliquent généralement un mécanisme de livraison (par exemple, API REST, travaux planifiés, GUI, autres systèmes)
* Déclenchent un cas d'utilisation et convertissent le résultat au format approprié pour le mécanisme de livraison
* le contrôleur pour un MVC

#### Interfaces externes

* Utilisent le framework le plus approprié (ils vont être isolés ici de toute façon)

### Exemple de code

Voir la structure sur [GitHub](https://github.com/Createdd/web-miner/tree/master/webminer).

Tout d'abord, il est important de comprendre que l'architecture propre est un ensemble de principes d'organisation. Par conséquent, tout est ouvert à des ajustements personnels tant que les idées principales sont conservées intactes. Le dépôt lié est un fork du projet original qui m'a apporté cette idée de conception d'architecture. N'hésitez pas à consulter également le projet original, car il reflète des améliorations supplémentaires.

Le dossier webminer est structuré en couches de base :

1. entities
2. use_cases
3. interfaces_adapters
4. external_interfaces

![Image](https://cdn-media-1.freecodecamp.org/images/FSvBm5GdWA0uMo6NJhyOoF2hgJt8s1Bv3n1v)
_Structure du dossier webminer_

Il doit refléter l'approche très basique pour le modèle de conception.

* En commençant par `entities`, vous pouvez voir que le modèle central de ce projet est `arxiv_document`
* Le dossier suivant, `use_cases` montre notre cas d'utilisation, à savoir demander la page arxiv
* Après cela, nous passons par le dossier `interface_adapters` qui fournit des adaptateurs pour les demandes de processus dans une application REST ou pour la sérialisation
* La couche finale et dernière est `external_interfaces`. C'est ici que nous utilisons le serveur flask pour implémenter la fonctionnalité REST

Toutes ces couches dépendent des couches centrales mais pas l'inverse.

**Une note importante : Ceci n'est pas implémenté à 100% correctement dans le dépôt.**

Pourquoi ? Parce que les cas d'utilisation sont en réalité différents. En réalité, le cas d'utilisation principal est de fournir les données structurées. Un autre cas d'utilisation est d'obtenir les données à partir de la page arxiv.

Avez-vous repéré cette erreur dans l'architecture ? Si oui, félicitations ! Non seulement vous avez apporté assez de curiosité à cet article, mais vous comprenez probablement bien les principes pour construire votre propre cas et appliquer les concepts dans la réalité !

Êtes-vous d'accord ? Si non, pourquoi ? Merci d'avoir lu mon article ! N'hésitez pas à laisser vos commentaires !

### Ressources

Voici quelques articles que j'ai trouvés utiles pour comprendre le concept d'« architecture propre » :

* [https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
* [https://www.codingblocks.net/podcast/clean-architecture-make-your-architecture-scream/](https://www.codingblocks.net/podcast/clean-architecture-make-your-architecture-scream/)
* [https://github.com/mattia-battiston/clean-architecture-example](https://github.com/mattia-battiston/clean-architecture-example)
* [https://medium.com/@tiagoflores_23976/how-choose-the-appropriate-ios-architecture-mvc-mvp-mvvm-viper-or-clean-architecture-2d1e9b87d48](https://medium.com/@tiagoflores_23976/how-choose-the-appropriate-ios-architecture-mvc-mvp-mvvm-viper-or-clean-architecture-2d1e9b87d48)
* [https://de.slideshare.net/HimanshuDudhat1/mvp-clean-architecture](https://de.slideshare.net/HimanshuDudhat1/mvp-clean-architecture)
* [https://softwareengineering.stackexchange.com/questions/336677/what-is-the-difference-between-mvp-and-clean-architecture](https://softwareengineering.stackexchange.com/questions/336677/what-is-the-difference-between-mvp-and-clean-architecture)
* [https://engineering.21buttons.com/clean-architecture-in-django-d326a4ab86a9](https://engineering.21buttons.com/clean-architecture-in-django-d326a4ab86a9)
* [https://gist.github.com/ygrenzinger/14812a56b9221c9feca0b3621518635b](https://gist.github.com/ygrenzinger/14812a56b9221c9feca0b3621518635b)
* [https://medium.freecodecamp.org/how-to-write-robust-apps-consistently-with-the-clean-architecture-9bdca93e17b](https://medium.freecodecamp.org/how-to-write-robust-apps-consistently-with-the-clean-architecture-9bdca93e17b)
* [https://marconijr.com/posts/clean-architecture-practice/](https://marconijr.com/posts/clean-architecture-practice/)

Daniel est un étudiant en LL.M. en droit des affaires, travaillant comme ingénieur logiciel et organisateur d'événements technologiques à Vienne. Ses efforts d'apprentissage personnel actuels se concentrent sur le machine learning.

Connectez-vous sur :

* [LinkedIn](https://www.linkedin.com/in/createdd)
* [Github](https://github.com/Createdd)
* [Medium](https://medium.com/@ddcreationstudi)
* [Twitter](https://twitter.com/_createdd)
* [Steemit](https://steemit.com/@createdd)
* [Hashnode](https://hashnode.com/@DDCreationStudio)