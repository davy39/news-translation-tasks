---
title: Comment utiliser une API GraphQL pour l'administration de base de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T13:02:43.000Z'
originalURL: https://freecodecamp.org/news/using-a-graphql-api-for-database-administration-1a5039b43c8f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*htOb7MGk4cXDpp4md_iHSQ.png
tags:
- name: api
  slug: api
- name: database
  slug: database
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment utiliser une API GraphQL pour l'administration de base de données
seo_desc: 'By Michael Hunger

  A recent discussion at graphql-europe made me realize that GraphQL would make for
  an amazing API for database administration.

  You know that plethora of functions and options to control details from security,
  indexing, metadata, clus...'
---

Par Michael Hunger

Une récente discussion à graphql-europe m'a fait réaliser que GraphQL ferait une API incroyable pour l'administration de bases de données.

Vous connaissez cette pléthore de fonctions et d'options pour contrôler les détails de la sécurité, de l'indexation, des métadonnées, du clustering et d'autres opérations ?

J'ai utilisé le trajet du retour en train pour construire un endpoint d'administration GraphQL pour Neo4j, exposant toutes les procédures disponibles soit comme des requêtes soit comme des mutations. En utilisant Kotlin, cela n'a été qu'une question de quelques lignes (200) de code. Et cela a fonctionné surprenamment bien.

Si vous connaissez une autre base de données qui expose son API d'administration via GraphQL, faites-le moi savoir dans les commentaires — j'adorerais y jeter un coup d'œil.

Et si vous êtes inspiré pour baser une partie de votre travail sur cette idée, je serais honoré, encore plus avec une attribution :)

### TL;DR

Vous pouvez obtenir votre API d'administration Neo4j servie à `/graphql/admin` en installant la dernière version de l'extension `[neo4j-graphql](http://github.com/neo4j-graphql/neo4j-graphql)`. Dans [Neo4j Desktop](https://neo4j.com/developer/guide-neo4j-desktop/), cliquez simplement sur "Install GraphQL" dans la section Plugins de votre base de données (`version 3.4.0.1`). Vous devrez peut-être configurer un _en-tête d'authentification de base_ pour les identifiants de votre utilisateur de base de données. Ensuite, vous êtes prêt à interroger votre nouvelle et brillante API d'administration via GraphiQL ou GraphQL Playground.

![Image](https://cdn-media-1.freecodecamp.org/images/6GfcIFSf6Dz2wcWKTzNHJYi3EmP6Py6w1MnY)
_Une requête administrative contre l'API de la base de données_

L'endpoint n'est **pas limité aux procédures intégrées.** Les bibliothèques externes comme APOC, graph-algorithms ou neo4j-spatial sont automatiquement exposées.

### Avantages

À mon avis, le plus grand avantage est la **nature auto-documentée** des API GraphQL basées sur le schéma strict fourni.

Le typage fort, la documentation et les valeurs par défaut pour les types d'entrée et de sortie augmentent la **clarté** et réduisent le nombre de tentatives par essai et erreur. La sélection personnalisée des champs de sortie et la traversée optionnelle plus profonde des structures de résultats permettent des personnalisations rapides de ce que vous souhaitez récupérer.

Avec la **séparation claire** entre les requêtes de lecture et les mutations d'écriture, il est facile de raisonner sur l'impact d'un appel.

Et bien sûr, l'**incroyable auto-complétion avec aide en ligne** et la documentation automatiquement disponible dans GraphiQL et GraphQL-Playground rendent l'interaction avec une telle API un plaisir. ✨

**Paramétrer** toutes les entrées et limiter les tailles des résultats est juste la cerise sur le gâteau. 🍒

Un autre avantage est que vous pouvez **combiner plusieurs requêtes** en un seul appel. Toutes les informations pertinentes pour un écran complet sont récupérées en une seule requête.

Bien sûr, vous pouvez **utiliser tous les outils GraphQL disponibles** comme les middlewares ou les bibliothèques pour construire rapidement des applications front-end (apollo-tools, React, semantic-ui, victory, etc.). Cela vous permet d'intégrer rapidement ces API dans vos scripts ou tableaux de bord de monitoring/administration.

### Détails de l'implémentation

Comme l'endpoint GraphQL régulier dans `[neo4j-graphql](https://github.com/neo4j-graphql/neo4j-graphql)`, il s'agit d'une extension de serveur servant les endpoints GET, POST et OPTIONS. Ils prennent en entrée des _requêtes_, des _variables_ et des _noms d'opération_ à exécuter dans une seule transaction. Après exécution, les _résultats_ ou _erreurs_ sont retournés au client sous forme de JSON.

Le schéma graphql nécessaire est construit à partir des procédures définies par l'utilisateur disponibles déployées dans Neo4j.

Vous devez explicitement autoriser les procédures à être exposées via le paramètre de configuration `graphql.admin.procedures.(read/write)` avec soit la syntaxe des procédures Neo4j soit les noms de champs de l'endpoint d'administration. Par exemple, vous pourriez le définir comme suit :

```
graphql.admin.procedures.read=db.*,dbms.components,dbms.queryJ*graphql.admin.procedures.write=db.create*,dbIndexExplicitFor*
```

#### **Procédures définies par l'utilisateur**

En 2016, Neo4j 3.0 a obtenu un nouveau point d'extension. Vous pouviez fournir des méthodes Java annotées en tant que procédures définies par l'utilisateur, qui pouvaient ensuite être appelées soit de manière autonome soit dans le cadre de vos requêtes de base de données. Alors que notre navigateur Neo4j (basé sur React) est passé de HTTP à un transport binaire, les API REST de gestion originales ont été augmentées avec des procédures fournissant la même fonctionnalité.

Chaque procédure peut prendre des _paramètres_ et retourne un _flux de données_ avec des colonnes nommées individuellement, similaires aux résultats de requêtes régulières. Les entrées et les sorties peuvent utiliser des types de données du [système de types Cypher](https://neo4j.com/docs/developer-manual/current/drivers/cypher-values/#driver-neo4j-type-system).

```
call dbms.listConfig('dbms.connector.http')   yield name, value, description;
```

```
└────────────────────────────┬─────────────┬─────────────────────────┐
│"name"                     │"value"     │"description"          │
├────────────────────────────┼─────────────┼─────────────────────────┤
│"dbms.connector.http.enabled"│"true"      │"Enable this connector."│
├────────────────────────────┼─────────────┼─────────────────────────┤
│"dbms.connector.https.enabled"│"true"     │"Enable this connector."│
└────────────────────────────┴─────────────┴─────────────────────────┘
```

Depuis lors, une grande quantité de fonctionnalités a été déplacée vers des procédures et des fonctions, nous offrant une large sélection de choses à exposer via GraphQL.

Pour construire le schéma, j'ai itéré sur les procédures disponibles, créant un _champ_ pour chaque procédure.

J'ai pris les paramètres de procédure nommés comme _arguments d'entrée_ et utilisé des _types de sortie personnalisés_ (par procédure) contenant les colonnes retournées. Les paramètres d'entrée avec des valeurs par défaut pouvaient être _nuls_, les autres sont définis comme non nuls. Les descriptions de procédure sont devenues des _descriptions de champ_, et les informations de _dépréciation_ ont également été transférées.

J'ai mappé les types scalaires de base et les listes directement aux types GraphQL.

Seulement pour le type `Map` (dict/object), j'ai dû mapper vers un `List<Attribute>` où chaque attribut est

```
type Attribute {   name: String!   value: String   type: String!  = "String"}
```

ce qui a fonctionné surprenamment bien à la fois pour les entrées et les sorties.

![Image](https://cdn-media-1.freecodecamp.org/images/TPHbVofDoxIaYzVCak4nnwQQXBKAvM1QNCYT)
_Utilisation de la liste d'attributs pour les maps/dictionnaires, à la fois comme entrée et sortie_

De même, j'ai créé des types personnalisés pour `Node`, `Relationship` et `Path`.

Pour ces quatre types personnalisés, j'ai ajouté le code de (dé)sérialisation approprié. Tous les autres types inconnus ont été rendus en chaînes de caractères.

Le _résolveur_ pour chaque champ exécute simplement la _procédure encapsulée_ avec les arguments d'entrée de l'environnement. Les résultats sont ensuite mappés aux champs de type de sortie (optionnellement transformés) et retournés à l'endpoint.

Sur la base de leurs métadonnées, j'ai combiné les champs en types d'objets pour les requêtes et les mutations, respectivement.

![Image](https://cdn-media-1.freecodecamp.org/images/NttyWbz1Rr8ra6ioksZrF0viNzxHW79yNFzF)
_Exécution d'une opération d'administration de mutation avec des variables_

Et c'était essentiellement tout.

J'ai été surpris moi-même lorsque j'ai lancé GraphiQL après avoir déployé l'extension, j'ai pu appeler intuitivement n'importe laquelle des requêtes et mutations sans accroc.

### Défis

Mon plus grand défi est le **manque de namespaces** dans GraphQL. Bien que vous puissiez sous-structurer les requêtes avec des types imbriqués, la même chose n'est pas disponible pour les mutations.

Pour garder la nomenclature de l'API cohérente entre les deux, j'ai décidé de **ne pas sous-structurer** les requêtes et les mutations, et j'ai plutôt joint les parties capitalisées du namespace et du nom de la procédure ensemble.

Ainsi, `db.labels` devient `dbLabels`.

Un autre léger défi était l'absence d'informations sur les opérations de lecture par rapport à l'écriture dans les portées `DBMS` et `SCHEMA` des procédures Neo4j. J'ai donc dû utiliser une _liste blanche_ pour déterminer celles en "lecture seule", ce qui, bien sûr, n'est pas suffisant.

### Points notables

Une chose que les autres technologies d'API n'ont pas intégrée, et qui est vraiment cool, est la capacité de choisir et de sélectionner n'importe quel nombre de requêtes ou de mutations que vous souhaitez exécuter dans une **seule requête**.

Si nécessaire, vous pouvez même aliaser plusieurs invocations de la même requête avec différents paramètres (pensez aux statistiques par base de données).

![Image](https://cdn-media-1.freecodecamp.org/images/rIlWmkfgvMhEKShmGFmZV2YWLfKQB8ergdzS)
_Exécuter plusieurs opérations d'API dans une seule requête._

Et vous pouvez même exécuter des algorithmes de graphes ou des instructions Cypher dans le cadre de cette API, ce qui est plutôt cool.

![Image](https://cdn-media-1.freecodecamp.org/images/tgV-N2b8UdF9HlO6uZ1fQs8YJPuwjj5PRP0D)
_Exécuter une requête "Cypher"._

![Image](https://cdn-media-1.freecodecamp.org/images/WDPAzuzfGnmmu5urddjgVHwa56UINx1-pPfQ)
_Exécuter une procédure "graph-algorithm"_

### Prochaines étapes

Actuellement, je n'expose directement que les paramètres et résultats des procédures aux utilisateurs. À l'avenir, il serait intéressant de dériver des types de niveau supérieur qui offrent leurs propres champs de requête (dynamiques), comme

* un type Label qui peut également retourner des comptes
* un type Server qui peut fournir son rôle de cluster ou d'autres informations locales
* ajouter plus de champs dynamiques avec des paramètres sur un type Node ou Relationship pour des traversées personnalisées

J'adorerais 💡 une série d'applications mobiles, web et de clients en ligne de commande de **monitoring et de gestion** construites sur cette API de gestion.

Je suis excité de voir où nous pourrions améliorer l'utilisabilité et quels retours et demandes nous recevrons. Bien sûr, la première cible serait une [graph-app](http://neo4j-apps.github.io) pour [Neo4j Desktop](https://neo4j.com/developer/guide-neo4j-desktop/). Donc, si vous êtes intéressé par l'une de ces choses, **n'hésitez pas à nous contacter et discutons**.

Bon hacking ! — Michael

Si vous rencontrez des problèmes, veuillez ajouter un commentaire ou ouvrir un [GitHub issue](https://github.com/neo4j-graphql/neo4j-graphql/issues).