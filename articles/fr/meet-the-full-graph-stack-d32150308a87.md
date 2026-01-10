---
title: Comment Construire un Serveur de Pointe Maintenant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T08:21:56.000Z'
originalURL: https://freecodecamp.org/news/meet-the-full-graph-stack-d32150308a87
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IBwh1zdiKEN7OdkOoUJC8w.png
tags:
- name: GraphQL
  slug: graphql
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment Construire un Serveur de Pointe Maintenant
seo_desc: 'By Yisroel Yakovson

  Meet the Full Graph Stack

  Are you looking for some quick new marketable skills? Or, do you want to create
  a robust back-end in a day for a startup?

  I’m about to tell you how I did just that. More importantly, I’ll tell you how Gra...'
---

Par Yisroel Yakovson

### Découvrez la Full Graph Stack

Vous cherchez à acquérir rapidement de nouvelles compétences commercialisables ? Ou souhaitez-vous créer un back-end robuste en une journée pour une startup ?

Je vais vous expliquer comment j'ai fait exactement cela. Plus important encore, je vais vous dire comment [GraphQL](https://graphql.org/index.html) a déclenché une disruption brillante dans les stacks d'applications.

J'ai une maîtrise en informatique et quelques brevets récents dans les interfaces utilisateur de données. Donc, d'une certaine manière, je peux apprécier la puissance de ces percées.

![Image](https://cdn-media-1.freecodecamp.org/images/PcJ6BnYn9fbSrglVYCe1HLRZHP73rGdZQpBs)
_Full Graph Stack_

Les temps changent, rapidement. J'ai passé un mois fascinant à repenser les backends, les APIs, les bases de données et les stacks. J'étais sur le point d'embaucher un développeur back-end senior. Le drôle de chose, c'est qu'à la fin, j'ai décidé que je n'en avais pas besoin. Et vous aussi, vous pourriez ne pas en avoir besoin.

J'appelle ce nouveau type de stack d'applications une _Full Graph Stack_, ou _Graph Stack_ en abrégé.

### L'Approche de Base

Vous construisez un graphe montrant les données dont vous avez besoin pour votre front end. Ensuite, des outils récemment développés génèrent le back end à partir de zéro.

Si vous n'êtes pas clair sur ce qu'est un [graphe](https://en.wikipedia.org/wiki/Graph_theory#Graph), prenez quelques minutes pour clarifier cela. Une définition informelle suffit : un graphe est un ensemble de points (pensez à des cercles) avec des lignes les reliant. Un nom commun pour ces points est _nœuds_, et les lignes sont des _arêtes_.

![Image](https://cdn-media-1.freecodecamp.org/images/SxrjtbFitVTc0j7gqAGj-yv33GFyqSPkX7u2)
_Un Exemple de Graphe Très Simple_

Une application (y compris une application web) a des types d'informations. Un graphe peut représenter les besoins en données d'une application. Les types d'informations sont des nœuds, et les relations entre eux sont des arêtes. Par exemple, le graphe pour une application de gestion d'événements peut ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1i0WmsoCEGG0843ekCQcvrOoNTS73yEXOn3l)
_Un Graphe d'Application_

Le point clé est qu'un tel graphe organise _chaque niveau_ de votre code d'application, du front end au back end.

### Comment cela Fonctionne

Une full graph stack se concentre sur une [spécification de schéma GraphQL](https://graphql.org/learn/schema/). Les [directives](https://graphql.org/learn/queries/#directives) peuvent enrichir la spécification. Si vous n'êtes pas familier avec GraphQL, lisez à ce sujet. Pour nos besoins, les requêtes API sont des sous-ensembles du graphe de l'application.

Le schéma GraphQL contient un graphe des types principaux et de leurs relations. [Apollo](https://www.apollographql.com/) offre un ensemble de services qui simplifient la construction d'interfaces GraphQL. Le graphe de données est les _TypeDefs_.

Les TypeDefs sont centraux dans tout ce qui concerne la full graph stack. Votre travail est de créer les TypeDefs pour montrer votre graphe d'application. Les convertisseurs génèrent :

* un schéma GraphQL complet à partir de vos TypeDefs. Cela inclut les _mutations_, qui sont des mises à jour.
* des _resolvers_. Ce sont des fonctions qui implémentent des requêtes et des mutations sur votre back end. Comme discuté dans le [deuxième article](https://medium.com/@yisroelyakovson/building-a-single-graph-stack-f95590ade5af), le convertisseur que j'ai utilisé était [neo4j-graphql-js](https://github.com/neo4j-graphql/neo4j-graphql-js).

![Image](https://cdn-media-1.freecodecamp.org/images/J1H1lvpfaRXi4LVQlhkjvtO7-WMYKanY5H7z)
_Aperçu de la Full Graph Stack_

Le point clé est que le back end utilise une base de données qui est soit [sans schéma](https://blog.couchbase.com/the-value-of-schema-less-databases/). Sans schéma signifie que les données ne sont pas confinées à une structure prédéfinie, ou schéma. Les bases de données relationnelles traditionnelles limitent les données à leur schéma.

L'approche courante est de créer une base de données virtuellement sans schéma en utilisant [Prisma](https://www.prisma.io/).

Mais je vous exhorte à considérer une deuxième approche : utiliser une base de données _intrinsèquement sans schéma_ ! Les [bases de données de documents](https://database.guide/what-is-a-document-store-database/) et les [bases de données de graphes](https://orientdb.com/graph-database/) n'ont pas de schéma inhérent. Vous pouvez donc prendre une base de données sans schéma et conformer ses données au schéma de l'API GraphQL.

Vous pourriez objecter qu'il n'est pas si difficile de mapper un schéma GraphQL à une base de données relationnelle. Je suis d'accord, mais aujourd'hui nous avons besoin de la flexibilité pour itérer. Une full graph stack vous offre cela. Une startup peut pivoter sans fin. Une base de données sans schéma est facile à mettre à jour pour se conformer aux changements de l'API.

### Bases de Données de Graphes

Je soutiens que les bases de données de graphes sont l'approche la plus idéale pour une full graph stack. Les bases de données sont elles-mêmes des graphes et se mappent donc de manière transparente au schéma GraphQL. Vous devrez probablement traiter avec votre serveur de base de données à un moment donné. Cela est plus simple et intuitif lorsque sa structure de données est identique à votre API.

Les bases de données de graphes ne sont pas nouvelles. De nombreux modèles de bases de données sémantiques ont vu le jour dans les années 70 et 80. La plupart présentaient le schéma sous forme de graphe. Mais aucun d'entre eux n'a vraiment percé jusqu'à la dernière décennie.

Les développements récents ont alimenté une nouvelle appréciation pour les modèles de données de graphes :

* le big data
* la maturation de l'apprentissage automatique
* le besoin d'alternatives plus efficaces et flexibles aux bases de données relationnelles (les soi-disant _bases de données NoSQL_).

Il existe de nombreux fournisseurs de bases de données de graphes aujourd'hui. Le leader actuel du marché est [Neo4j](https://neo4j.com/), mais une concurrence significative se profile. Je ne prétends pas avoir recherché les options et déterminé que Neo4j est le meilleur. Mais Neo4j est très établi, et un soutien énorme est disponible pour son utilisation.

### Le Front End

Je me concentre sur le back end dans ces articles, mais la graph stack s'étend jusqu'au front end.

Le site [GRANDstack](https://grandstack.io/) observe que [React](https://reactjs.org/) est particulièrement adapté à une graph stack. React utilise une hiérarchie simple d'éléments qui peuvent être mappés à des requêtes GraphQL.

Le [composant Query](https://www.apollographql.com/docs/react/essentials/queries.html) d'Apollo permet même à un élément de requêter ses données directement. Ainsi, les composants utilisant la requête se mappent à GraphQL. Votre [source unique de vérité](http://www.hackingwithreact.com/read/1/12/state-and-the-single-source-of-truth) devient le back end. Cela est beaucoup plus simple que de recréer les données du back end dans un état Redux.

### Avantages

La full graph stack est un nouveau paradigme, et tout le monde n'a pas encore saisi sa puissance. De nombreux articles et blogs des dernières années discutent de solutions centrées autour de GraphQL. La plupart revendiquent des choses comme un "back end instantané". Mais l'objectif fondamental d'un seul graphe exécutant votre stack n'est pas encore compris globalement. Une fois que les gens apprécieront cette vision, les outils deviendront plus cohérents et complets.

En bref, les avantages d'une full graph stack sont :

1. Implémentation rapide.
2. Flexibilité. Vous pouvez itérer votre solution rapidement.
3. Transparence.
4. Cohérence. Le même graphe à chaque niveau.
5. Indépendance. L'accent mis au niveau de l'API avec un back end simplifié élimine le verrouillage pour les services back end. C'est un retournement surprenant. Le pouvoir s'éloigne des fournisseurs de services cloud concurrents.

Consultez [Lancez Votre Serveur MVP en une Heure](https://medium.com/p/f95590ade5af/edit) pour des instructions étape par étape sur la construction d'un tel serveur !

_Ceci est le premier des 3 articles sur les Full Graph Stacks. Voir aussi_ [Lancez Votre Serveur MVP en une Heure](https://medium.com/p/f95590ade5af/edit) _et_ [D'un MVP à un Serveur de Production en un Jour](https://medium.com/p/ec231a938551/edit)_.