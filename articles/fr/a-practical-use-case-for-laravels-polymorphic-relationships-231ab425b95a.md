---
title: 'Les relations polymorphiques de Laravel : un cas d''utilisation pratique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T14:31:26.000Z'
originalURL: https://freecodecamp.org/news/a-practical-use-case-for-laravels-polymorphic-relationships-231ab425b95a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*js7-5fdBmy0r36PW32dqYA.png
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: 'Les relations polymorphiques de Laravel : un cas d''utilisation pratique'
seo_desc: 'By Joe Dixon

  Recently, when working on my side hustle Zero to Grow, I ran into quite a complex
  database design issue.

  The solution involves a use case for Laravel’s Polymorphic relations that goes way
  beyond the comments example in the documentation....'
---

Par Joe Dixon

Récemment, en travaillant sur mon projet parallèle [Zero to Grow](https://zerotogrow.io/), je me suis heurté à un problème de conception de base de données assez complexe.

La solution implique un cas d'utilisation des relations polymorphiques de Laravel qui va bien au-delà de l'exemple des [commentaires](https://laravel.com/docs/5.5/eloquent-relationships#polymorphic-relations) dans la documentation.

### Quel est le problème

Pour comprendre ce problème, vous devez en savoir un peu plus sur l'application que je développe.

[Zero to Grow](https://zerotogrow.io/) est une application destinée aux développeurs qui souhaitent faire croître leurs projets parallèles. Que leur objectif soit d'augmenter le trafic, la rétention, les conversions ou autre chose ; cette application est là pour aider.

Lors de l'inscription, l'utilisateur est invité à définir les objectifs globaux qu'il souhaite atteindre et les métriques qu'il doit suivre tout au long du processus.

Une fois leurs objectifs définis, l'utilisateur crée et exécute des tests sur son projet parallèle dans le but d'atteindre ces objectifs. Un exemple de test serait « Envoyer au moins un tweet par jour pour augmenter l'engagement ».

Comme pour les objectifs, l'utilisateur doit définir les métriques à suivre afin de déterminer si le test a été réussi ou non.

Il doit être possible de mettre à jour les métriques aussi souvent que l'utilisateur le nécessite tout au long du test ou de l'objectif.

Pour compliquer les choses, nous avons également le concept d'idées. Elles peuvent être soit privées à un utilisateur individuel, soit mises à disposition du public pour que d'autres puissent les utiliser.

Les idées sont toujours le point de départ des tests. L'utilisateur trouvera une idée, soit en la créant lui-même, soit en recherchant dans le répertoire public, et commencerà à la tester pour voir son impact sur l'objectif global.

### Conception du schéma

Afin de comprendre comment les relations polymorphiques peuvent aider, je vais vous expliquer le schéma que j'ai conçu pour résoudre ce problème, pièce par pièce.

#### Objectifs et métriques

Un utilisateur peut souhaiter que son objectif principal soit d'augmenter le taux de conversion global d'une page de destination. Pour mesurer cela efficacement, il peut vouloir suivre le nombre total de visiteurs de la page de destination ainsi que le nombre total d'inscriptions.

Lors du démarrage de l'objectif, l'utilisateur doit entrer les valeurs de base et cibles des métriques. Pendant la durée de vie de l'objectif, il doit régulièrement mettre à jour les métriques avec les dernières valeurs.

La structure de données ressemblerait à quelque chose comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/0*fzAQFZrAMwAXD0SK.png)

Ce diagramme nous indique que chaque objectif peut avoir une ou plusieurs métriques et que chaque métrique peut avoir une ou plusieurs entrées.

Avec cette structure de données, les utilisateurs pourront créer un objectif et lui assigner toutes les métriques qu'ils souhaitent suivre. Ils pourront ensuite mettre à jour l'objectif avec de nouvelles entrées selon les besoins pendant la durée de vie de l'objectif.

#### Idées et métriques

Un utilisateur doit pouvoir définir une idée et associer les métriques à suivre. À cet égard, la structure de données sera similaire à celle des objectifs et des métriques ci-dessus. Cependant, nous n'avons pas besoin de nous soucier du suivi des métriques jusqu'à ce que l'utilisateur commence à la tester.

![Image](https://cdn-media-1.freecodecamp.org/images/0*mvuBFDL9ZwBMMdD6.png)

Comme dans l'exemple précédent, chaque idée peut avoir plusieurs métriques, ce qui satisfera nos exigences.

#### Tests

Les tests sont là où les choses commencent à devenir intéressantes.

Comme mentionné précédemment, les idées peuvent être mises à disposition du public et donc testées par de nombreux utilisateurs différents. Le fait que chaque test doive être assigné à un objectif rend cela encore plus complexe.

Lors du lancement d'un nouveau test, l'utilisateur doit entrer ses valeurs de base et cibles des métriques. Ensuite, pendant la durée de vie du test, il doit régulièrement ajouter les dernières valeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/0*yZwfhqpnClreNfpN.png)

Essentiellement, il s'agit d'une table pivot à trois voies. La convention de nommage par défaut pour cette table dans Laravel serait `idea_goal_user`. Ce n'est pas exactement facile à prononcer.

Habituellement, je trouve que les tables pivots tendent à encapsuler une sorte de fonctionnalité ou de comportement, et je préfère les nommer de manière à refléter cela. Dans ce cas, la combinaison d'un objectif, d'une idée et d'un utilisateur est tout ce dont on a besoin pour exécuter un test. Ainsi, cette table devient `tests`. Elle permet à une idée d'être utilisée par plusieurs utilisateurs ainsi que d'être assignée à un objectif.

Ce que vous avez peut-être remarqué dans le diagramme ci-dessus, c'est que la table `entries` facilite une relation plusieurs-à-plusieurs entre les tables `tests` et `metrics`.

Une décision de conception clé a dû être prise ici. Le fait que les idées soient disponibles publiquement et puissent être testées par plusieurs utilisateurs signifie que, si cette relation plusieurs-à-plusieurs n'existait pas, il serait impossible de savoir quel utilisateur a entré une valeur contre la métrique.

### Comment les relations polymorphiques peuvent aider

En examinant ce schéma, il y a quelques endroits où les relations polymorphiques peuvent être utilisées.

Tout d'abord, l'endroit le plus évident pour extraire une relation polymorphique est entre les tables des objectifs et des idées vers la table des métriques. Bien que les relations soient différentes, les données de stockage sont identiques entre les deux et constituent donc le cas d'utilisation parfait.

Plutôt que de définir des tables séparées pour définir les métriques telles que `goal_metrics` et `idea_metrics`, définissez simplement une seule table et utilisez une relation polymorphique un-à-plusieurs pour les deux. La migration pourrait ressembler à quelque chose comme ceci.

Avec les relations de modèle définies comme suit :

C'est tout ce qui est nécessaire pour cette relation. L'utiliser n'est pas différent de la définition d'une relation standard un-à-plusieurs.

Le deuxième cas d'utilisation est un peu plus difficile à repérer et vous pourriez ne pas être d'accord avec mon approche. Cependant, à mon avis, c'est une solution vraiment élégante.

Les métriques pour les objectifs et les métriques pour les tests ont une relation avec une table d'entrées. C'est là que sont stockées les valeurs associées aux métriques définies.

Pour les objectifs, la relation devrait vraiment être un-à-plusieurs. Une métrique peut avoir plusieurs entrées, mais une entrée appartient à une métrique.

Avec les tests, la relation est légèrement différente car les métriques sont définies contre une idée qui peut être testée par plusieurs utilisateurs. Ainsi, chaque test peut avoir plusieurs métriques et chaque métrique peut appartenir à plusieurs tests. Il s'agit d'une relation plusieurs-à-plusieurs.

Pour résoudre ce problème, une table intermédiaire (ou pivot) peut être définie entre les tests et les métriques. Il est logique d'appeler cette table `entries` et de stocker les valeurs entrées directement dans cette table pivot.

Bien que la relation entre les entrées et les tests et les objectifs soit différente, je pense que dans ce cas, il est logique de rompre la normalisation standard des bases de données et d'utiliser une seule table pour stocker toutes les données d'entrée des métriques.

L'implémentation pourrait ressembler à quelque chose comme ceci :

Avec les relations de modèle définies comme suit :

Interagir avec ces relations reste extrêmement simple.

Vous y voilà, une relation polymorphique plusieurs-à-plusieurs.

Comme je l'ai mentionné précédemment, ce n'est pas la seule façon de résoudre ce problème. Vous pourriez souhaiter aborder la dernière relation plusieurs-à-plusieurs en utilisant des tables séparées. Même si cela rompt avec la convention, garder toutes les données d'entrée des métriques dans la même table est une solution particulièrement élégante et un excellent exemple de la puissance des relations polymorphiques natives de Laravel.

Pour moi, concevoir la solution de cette manière la rend beaucoup plus facile à « grok » ce que l'application fait, tant pour les nouveaux venus dans le projet que pour moi-même, six mois plus tard. En fin de compte, cependant, à chacun sa propre approche ! Auriez-vous pris une route différente ? Si oui, discutons-en dans les commentaires ci-dessous — j'adorerais lire vos réflexions.

Publié à l'origine sur [joedixon.co.uk](https://joedixon.co.uk/a-practical-use-case-for-laravels-polymorphic-relationships).