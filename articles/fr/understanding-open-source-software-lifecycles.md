---
title: Comment fonctionnent les cycles de vie des logiciels open source ?
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2024-03-26T17:01:50.000Z'
originalURL: https://freecodecamp.org/news/understanding-open-source-software-lifecycles
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/danial-igdery-FCHlYvR5gJI-unsplash.jpg
tags:
- name: lifecycle methods
  slug: lifecycle-methods
- name: open source
  slug: open-source
seo_title: Comment fonctionnent les cycles de vie des logiciels open source ?
seo_desc: 'Software projects follow identifiable milestones as they move towards a
  successful completion. If you want to give your project the best chances of success,
  it''s important to understand what those milestones mean and how they''re defined.

  This article...'
---

Les projets logiciels suivent des étapes identifiables alors qu'ils avancent vers une réalisation réussie. Si vous souhaitez donner à votre projet les meilleures chances de succès, il est important de comprendre ce que signifient ces étapes et comment elles sont définies.

Cet article provient de mon guide d'étude complet pour l'examen LPI Open Source Essentials [cours Udemy](https://www.udemy.com/course/complete-lpi-open-source-essentials-exam-study-guide/?referralCode=05B999CE18EF4D6E243C) et [livre](https://www.amazon.com/dp/B0CK3Q8DCF). Vous pouvez également [voir la version vidéo](https://youtu.be/eZ_4DLVxs7Q).

## Qu'est-ce que les versions logicielles ?

Il existe plusieurs types de versions logicielles et certaines méthodes de versionnage associées utilisées pour suivre les changements logiciels et les communiquer aux utilisateurs. Commençons par les versions.

* Il y a la **version alpha** – une version initiale du logiciel qui n'est généralement pas complète en termes de fonctionnalités et qui n'est pas destinée à être utilisée par le grand public. Elle est utilisée uniquement pour des tests et un usage interne.
* Une **version bêta** est une version pré-lancement du logiciel qui est complète en termes de fonctionnalités mais qui peut encore contenir des bugs ou d'autres problèmes. Elle est publiée auprès d'un public limité pour des tests et des retours avant la version finale.
* Ensuite, il y a un **candidat à la version**, qui est une version du logiciel considérée comme stable et prête pour le lancement, en attente des derniers tests et corrections de bugs.
* Et enfin, vous produirez une **version de disponibilité générale** comme version finale du logiciel qui est publiée auprès du grand public.

## Qu'est-ce que le versionnage logiciel ?

Le versionnage logiciel (parfois appelé versionnage sémantique) est la pratique consistant à attribuer des numéros de version uniques aux différentes versions d'un logiciel.

Voici un exemple utile :

```
vmlinuz-5.19.0-40-generic
```

Dans certaines approches, le premier nombre dans le numéro de version ("5" dans ce cas) est la version majeure. Un changement de version majeure indique des modifications significatives ou de nouvelles fonctionnalités qui ne sont pas rétrocompatibles avec les versions précédentes.

Le deuxième nombre ("19") est la version mineure. Un changement de version mineure indique de nouvelles fonctionnalités ou fonctionnalités qui sont rétrocompatibles avec les versions précédentes.

Le troisième nombre dans le numéro de version ("0") est la version de correctif. Un changement de version de correctif indique des corrections de bugs ou des modifications mineures qui sont rétrocompatibles avec les versions précédentes.

Pourquoi distinguer les versions majeures et mineures ? Les versions majeures sont généralement utilisées pour des modifications significatives ou de nouvelles fonctionnalités qui ne sont pas rétrocompatibles avec les versions précédentes. Les versions majeures sont généralement annoncées aux utilisateurs et aux clients avec beaucoup de publicité, car elles représentent une étape significative dans le développement du logiciel.

Les versions mineures, en revanche, sont utilisées pour des modifications plus petites ou de nouvelles fonctionnalités qui sont rétrocompatibles avec les versions précédentes. Les versions mineures sont généralement publiées plus fréquemment et visent à fournir aux utilisateurs des améliorations incrémentielles du logiciel.

## Que signifie la rétrocompatibilité ?

La rétrocompatibilité est la capacité d'une version plus récente d'un logiciel ou d'un système à fonctionner avec des fichiers, des données et d'autres composants créés dans une version plus ancienne de ce logiciel ou système. Cela signifie que les utilisateurs peuvent passer à la version plus récente sans perdre l'accès à leurs données ou fichiers existants.

Par exemple, supposons qu'un utilisateur a créé un document dans une version plus ancienne d'un programme de traitement de texte. Si la version plus récente du programme est rétrocompatible, l'utilisateur peut ouvrir et modifier le même document sans aucun problème. Cela est dû au fait que la version plus récente du programme est conçue pour lire et interpréter le format de fichier utilisé dans la version plus ancienne.

Cependant, si la version plus récente du programme n'est pas rétrocompatible, l'utilisateur ne pourra peut-être pas ouvrir ou modifier le fichier créé dans la version plus ancienne sans d'abord le convertir ou le recréer dans la version plus récente. Cela peut représenter un inconvénient significatif pour les utilisateurs et peut entraîner des problèmes de compatibilité et une perte de données.

Voici quelques autres définitions rapides – mais importantes.

## Gel des fonctionnalités

Le gel des fonctionnalités est une étape du processus de développement logiciel où aucune nouvelle fonctionnalité n'est ajoutée au produit ou au projet. Il est généralement mis en œuvre comme une date limite à laquelle toutes les nouvelles fonctionnalités doivent être terminées et approuvées avant la publication du produit logiciel.

L'objectif principal d'un gel des fonctionnalités est de stabiliser le produit logiciel en préparation de sa publication. En fixant une date limite pour le gel des fonctionnalités, les développeurs peuvent se concentrer sur la finalisation et les tests des fonctionnalités existantes plutôt que d'introduire de nouvelles. Cela permet de consacrer du temps à des tests rigoureux et à la correction de bugs, améliorant ainsi la qualité et la fiabilité globales du produit logiciel.

## Feuille de route

Une feuille de route est un document stratégique de haut niveau qui décrit les objectifs, les buts et le calendrier du développement d'un produit logiciel. Elle fournit une représentation visuelle du plan de développement du produit, décrivant les étapes clés et le calendrier prévu pour leur réalisation.

Les feuilles de route sont utiles pour communiquer la direction générale d'un produit logiciel aux parties prenantes, y compris les développeurs, les chefs de produit, les investisseurs et les clients.

## Étapes clés

Les étapes clés sont des réalisations spécifiques et mesurables qui marquent les progrès vers la réalisation d'un produit logiciel. Elles sont généralement fixées à intervalles réguliers tout au long du processus de développement et sont utilisées pour suivre les progrès et s'assurer que le projet reste dans les temps.

Des exemples d'étapes clés peuvent inclure la réalisation d'une fonctionnalité spécifique, la réussite d'une phase de test ou la publication d'une version bêta du produit logiciel.

## Journal des modifications

Un journal des modifications est un document qui liste les modifications apportées à un produit logiciel au fil du temps, y compris les corrections de bugs, les nouvelles fonctionnalités et autres mises à jour. Les journaux des modifications permettent aux développeurs et autres parties prenantes de comprendre ce qui a été mis à jour et quand.

Les journaux des modifications sont particulièrement utiles pour les produits logiciels qui sont fréquemment mis à jour ou qui ont un grand nombre de contributeurs.

## Support à long terme (LTS)

Le support à long terme fait référence à une version de logiciel désignée pour un support et une maintenance à plus long terme, généralement pour une période de plusieurs années. Pendant cette période, l'éditeur du logiciel fournit un support continu, y compris des corrections de bugs, des mises à jour de sécurité et d'autres activités de maintenance.

Les versions LTS sont souvent utilisées dans les environnements d'entreprise où la stabilité et la fiabilité sont cruciales. En avril de chaque année paire, par exemple, Canonical publiera une version LTS d'Ubuntu. Ces versions sont normalement supportées pendant quatre ou cinq ans.

## Fin de vie (EOL)

D'autre part, la fin de vie fait référence à un moment où une version de logiciel n'est plus supportée par l'éditeur. Cela signifie que l'éditeur ne fournira plus de mises à jour ou de corrections pour le logiciel, et que toute vulnérabilité de sécurité ou bug découvert ne sera pas traité. Cela peut laisser les utilisateurs avec un logiciel non supporté qui peut être sujet à des risques de sécurité et à d'autres problèmes.

Lorsque un produit logiciel atteint sa fin de vie, il est généralement retiré, et les utilisateurs sont encouragés à passer à une version plus récente ou à changer de produit. Le processus de fin de vie est souvent progressif, avec l'éditeur fournissant un préavis et des conseils aux utilisateurs pour les aider à migrer vers une nouvelle version ou un nouveau produit.

## Conclusion

Vous avez vu à quel point il est important de comprendre les étapes par lesquelles les projets logiciels réussis passeront. Et ce n'est pas seulement théorique, car cette connaissance vous donne les outils pour suivre vos progrès et identifier rapidement lorsque les choses déraillent.

_Cet article provient de mon cours_ [_Complete LPI_](https://www.udemy.com/course/complete-lpi-open-source-essentials-exam-study-guide/?referralCode=05B999CE18EF4D6E243C) Open Source _Essentials Study Guide_. _Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_