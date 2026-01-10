---
title: 'Une méthodologie de conception pour des systèmes logiciels fiables : Résumé
  d''un article académique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T10:00:39.000Z'
originalURL: https://freecodecamp.org/news/a-design-methodology-for-reliable-software-systems-a-summary-394dfd0dcbc2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YBoSTQ9iJHRhc3jm.jpeg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Une méthodologie de conception pour des systèmes logiciels fiables : Résumé
  d''un article académique'
seo_desc: 'By Shubheksha Jalan

  Let’s dig into A Design Methodology For Reliable Software Systems published by Barbara
  Liskov in 1972.

  The focus of this paper is on how to make reliable software systems and the techniques
  that can help us achieve that.

  Reliabili...'
---

Par Shubheksha Jalan

Plongeons dans [A Design Methodology For Reliable Software Systems](https://valbonne-consulting.com/papers/classic/Liskov_72-Design_Methodology_for_Reliable_Software_Systems.pdf) publié par Barbara Liskov en 1972.

L'accent de cet article est mis sur la manière de créer des systèmes logiciels fiables et les techniques qui peuvent nous aider à atteindre cet objectif.

La fiabilité implique ici qu'un système fonctionne comme prévu dans un ensemble donné de conditions.

> Le fait malheureux est que l'approche standard de construction de systèmes, impliquant un débogage extensif, n'a pas prouvé son succès dans la production de logiciels fiables, et il n'y a aucune raison de suggérer qu'elle le fera un jour.

> Bien que des améliorations dans les techniques de débogage puissent conduire à la détection de plus d'erreurs, cela ne signifie pas que toutes les erreurs seront trouvées.

> Il n'y a certainement aucune garantie implicite dans le débogage : comme Dijkstra l'a dit, « Les tests de programme peuvent être utilisés pour montrer la présence de bogues, mais jamais pour montrer leur absence. »

Pour être confiant que notre système fonctionne correctement, nous avons besoin de tests qui répondent aux conditions suivantes :

1. Nous pouvons générer un ensemble minimal de cas de test pertinents.
2. Tous les cas de test de l'ensemble peuvent être générés.

> Les solutions à ces problèmes ne résident pas dans le domaine du débogage, qui n'a aucun contrôle sur les sources des problèmes.

> Au lieu de cela, puisque c'est la conception du système qui détermine combien il y a de cas de test et à quel point ils peuvent être facilement identifiés, les problèmes peuvent être résolus le plus efficacement pendant le processus de conception. Le besoin de tests exhaustifs doit influencer la conception.

L'article soutient en outre que la fiabilité est un problème majeur avec les systèmes complexes. Il définit les systèmes complexes comme suit :

1. Le système a de nombreux états et il est difficile d'organiser la logique du programme pour les gérer correctement.
2. Il nécessite plusieurs personnes travaillant ensemble de manière coordonnée.

### Critères pour une bonne conception :

Pour maîtriser la conception d'un système complexe, nous devons utiliser la modularisation.

Divisez le programme en plusieurs modules (sous-programmes, appelés partitions dans l'article pour éviter de surcharger le terme « modules ») qui peuvent être compilés séparément, mais sont connectés à d'autres modules.

Les connexions sont définies par Parnas comme suit :

> Les connexions entre les modules sont les hypothèses que les modules font les uns sur les autres.

Bien que l'idée de modularité semble être un excellent outil pour construire de grands systèmes logiciels complexes, elle peut introduire une complexité supplémentaire si elle n'est pas bien faite.

> Le succès de la modularité dépend directement de la qualité du choix des modules.

Certains problèmes courants sont :

1. Un module fait trop de choses.
2. Une fonction commune est répartie parmi de nombreux modules différents.
3. Un module se comporte de manière inattendue avec des données communes.

La question suivante qui se pose est : Qu'est-ce qu'une bonne modularité ?

Nous utilisons deux techniques pour répondre à cela : les niveaux d'abstraction pour aborder la complexité inhérente du système, et la programmation structurée pour représenter la conception dans le logiciel.

#### Niveaux d'abstraction :

> Les niveaux d'abstraction...fournissent un cadre conceptuel pour atteindre une conception claire et logique pour un système. L'ensemble du système est conçu comme une hiérarchie de niveaux, les niveaux les plus bas étant ceux les plus proches de la machine.

Un groupe de fonctions apparentées constitue un niveau d'abstraction. Chaque niveau peut avoir les deux types de fonctions suivants :

1. Externes : Ces fonctions peuvent être appelées par des fonctions d'autres niveaux.
2. Internes : Ces fonctions effectuent une tâche commune au sein du niveau et ne peuvent pas être appelées par d'autres fonctions d'un niveau différent.

Les niveaux d'abstraction sont régis par les deux règles suivantes :

1. Chaque niveau a un contrôle exclusif sur un certain type de ressource.
2. Les niveaux inférieurs ne sont pas conscients des niveaux supérieurs et ne peuvent pas les référencer de quelque manière que ce soit. Mais les niveaux supérieurs peuvent demander aux niveaux inférieurs d'effectuer une action.

#### Programmation structurée :

Un programme structuré définit la manière dont le contrôle passe entre les différentes partitions d'un système.

Il est défini par les règles suivantes :

1. Le programme est développé dans un format descendant et divisé en niveaux. La notion de niveaux ici est différente de celle des niveaux d'abstraction car la première règle n'est pas satisfaite.
2. Seules les structures de contrôle suivantes peuvent être utilisées : concaténation, sélection de l'instruction suivante en fonction de la vérification d'une condition, et itération. Les sauts utilisant `goto` ne sont pas autorisés.

Revenons à la question posée précédemment : **comment définir une bonne modularité** ?

Dans un système modulaire qui est également fiable, les connexions entre les partitions sont limitées comme suit :

1. Elles doivent suivre les règles imposées par les niveaux d'abstraction et la programmation structurée.
2. Le passage de données entre les partitions doit être effectué en utilisant des arguments explicites. Les arguments sont passés aux fonctions externes d'une autre partition.
3. Les partitions doivent être logiquement indépendantes. Les fonctions au sein d'une partition doivent supporter sa propre abstraction uniquement.

La question suivante qui se pose après avoir compris comment définir une bonne modularité est — **comment l'atteindre dans notre conception** ?

> La technique traditionnelle de modularisation consiste à analyser le flux d'exécution du système et à organiser la structure du système autour de chaque tâche séquentielle majeure.

> Cette technique conduit à une structure qui a des connexions très simples en termes de contrôle, mais les connexions en termes de données tendent à être complexes.

Les partitions supportent les abstractions qu'un concepteur de système trouve utiles lorsqu'il pense au système.

> Les abstractions sont introduites afin de rendre ce que le système fait plus clair et plus compréhensible ; une abstraction est une simplification conceptuelle car elle exprime ce qui est fait sans spécifier comment cela est fait.

L'article présente ensuite quelques directives pour identifier différents types d'abstractions lors de la conception d'un système :

1. Abstraction des ressources : pour chaque ressource matérielle du système. Nous pouvons mapper les caractéristiques de la ressource abstraite à la ressource sous-jacente.
2. Caractéristiques abstraites des données : comment elles sont stockées.
3. Simplification via la limitation des informations que la partition doit connaître ou auxquelles elle a accès.
4. Simplification via la généralisation en identifiant les fonctions qui effectuent une tâche commune. De telles fonctions peuvent être regroupées dans une seule partition. « L'existence d'un tel groupe simplifie d'autres partitions, qui n'ont besoin que de faire appel aux fonctions de la partition inférieure plutôt que d'effectuer les tâches elles-mêmes. »
5. Maintenance et modification du système : les fonctions effectuant une tâche dont la définition est sujette à des changements futurs doivent faire partie de partitions indépendantes. Par exemple, les fonctions qui traitent de la connexion à un type particulier de backend de stockage afin que, si un backend différent est utilisé à l'avenir, seules les fonctions de cette partition seront affectées.

Maintenant que nous avons une idée de la manière dont nous pouvons atteindre une bonne modularité lors de la conception de notre système, **comment procédons-nous** ?

La première phase consiste à identifier un ensemble d'abstractions qui représentent le comportement éventuel du système de manière générale. La phase suivante « établit les connexions de données entre les partitions et décrit le flux de contrôle entre les partitions ».

> La deuxième phase se produit simultanément avec la première ; à mesure que les abstractions sont proposées, leur utilité et leur praticité sont immédiatement investiguées.

> Une partition a été suffisamment investiguée lorsque ses connexions avec le reste du système sont connues et lorsque les concepteurs sont confiants qu'ils comprennent exactement quel sera son effet sur le système.

La question suivante que l'on pourrait poser est : **comment identifier lorsque la conception est terminée** ?

1. Toutes les abstractions majeures ont été identifiées et liées à une partition. Les ressources du système ont été divisées entre les différentes partitions et leurs positions dans la hiérarchie ont été définies.
2. Les interfaces et le flux de contrôle entre les partitions sont clairement définis. Les cas de test pour chaque partition ont été identifiés.
3. Un guide utilisateur de base pour le système peut être écrit.