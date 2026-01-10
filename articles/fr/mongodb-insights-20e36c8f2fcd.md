---
title: Comment décider si MongoDB est fait pour vous
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-29T07:38:53.000Z'
originalURL: https://freecodecamp.org/news/mongodb-insights-20e36c8f2fcd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JkS75JaEP1Zk1aVJIMkdBQ.png
tags:
- name: database
  slug: database
- name: MongoDB
  slug: mongodb
- name: NoSQL
  slug: nosql
- name: Productivity
  slug: productivity
- name: technology
  slug: technology
seo_title: Comment décider si MongoDB est fait pour vous
seo_desc: 'By Luc Claustres

  For the past couple of years, I built web applications around MongoDB. In this short
  article I would like to answer some of the recurrent questions or misunderstanding
  most developers have when evaluating it:


  What is the licensing?

  ...'
---

Par Luc Claustres

Au cours des dernières années, j'ai construit des applications web autour de [MongoDB](https://www.mongodb.com/). Dans cet article court, je souhaite répondre à certaines des questions récurrentes ou des incompréhensions que la plupart des développeurs ont lors de son évaluation :

* Quelle est la licence ?
* Que signifie le fait que MongoDB soit une base de données NoSQL ?
* Qu'en est-il des performances de MongoDB ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*JkS75JaEP1Zk1aVJIMkdBQ.png)

### Licence

Oui, MongoDB est sous licence de la Free Software Foundation [GNU AGPL v3.0](https://www.mongodb.com/community/licensing). En pratique, cela signifie que les améliorations que vous apportez à MongoDB doivent être publiées pour la communauté. Le code source de tout travail dérivé doit également être distribué.

Vous pourriez vous demander si votre application est un travail dérivé. Je dois avouer que je n'ai jamais trouvé de définition simple d'un tel terme. Cependant, dans le cas spécifique de MongoDB, ils [reconnaissent simplement que les applications utilisant leur base de données sont un travail séparé](https://www.mongodb.com/blog/post/the-agpl). De plus, leurs pilotes pris en charge sont publiés sous [Licence Apache v2.0](http://www.apache.org/licenses/LICENSE-2.0). Il s'agit d'une [licence permissive](https://en.wikipedia.org/wiki/Permissive_software_licence). Elle ne vous oblige pas à publier votre code source, et votre application communique généralement avec MongoDB uniquement via un pilote.

Par conséquent, vous n'avez pas besoin de vous préoccuper de la licence de MongoDB pour construire votre application autour de celle-ci. Ils envoient même des lettres signées affirmant la promesse aux départements juridiques en cas de questions. Ils proposent également des licences commerciales si la lettre signée n'est pas suffisante.

> Remarque : bien qu'une grande expérience me fasse confiance dans cette analyse, je ne suis pas avocat. La vue présentée ici est ma compréhension personnelle et non une vue officielle.

### NoSQL

Oui, MongoDB est une base de données NoSQL. Ce terme peut être assez confus. Je vais essayer d'analyser les idées les plus courantes en me concentrant sur la manière dont cela s'applique à MongoDB.

#### Orienté document

Dans les bases de données SQL traditionnelles, les données sont organisées sous forme de tables et de lignes. Chaque ligne a un nombre fixe de colonnes qui ne peuvent stocker que des données d'un type spécifique (par exemple, Integer, Text, Datetime). Cela définit le _schéma_ de vos données.

Dans MongoDB, les données sont stockées sous forme d'[objets BSON](http://bsonspec.org/) organisés en _collections_. Les données sont généralement manipulées sous forme d'[objets JSON](http://www.json.org/). Cela rend le mappage des objets dans la base de données une tâche simple, _éliminant normalement tout ce qui ressemble à un_ [_mappage objet-relationnel_](https://en.wikipedia.org/wiki/Object-relational_mapping).

#### Transactionnel

Avant la version 4, MongoDB ne fournissait que des transactions au niveau du document. Les écritures n'étaient jamais partiellement appliquées à un document inséré ou mis à jour. L'opération était atomique dans le sens où elle échouait ou réussissait. Pour le document dans son intégralité, il était dit être [ACID](https://en.wikipedia.org/wiki/ACID_(computer_science)) au niveau du document. Par conséquent, il n'y avait pas de possibilité de changements atomiques couvrant plusieurs documents. Vous deviez émuler les transactions de base de données requises (par exemple, en utilisant le [commit en 2 phases](https://en.wikipedia.org/wiki/Two-phase_commit_protocol)).

Depuis la version 4, MongoDB prend en charge les transactions ACID multi-documents, ce qui en fait la seule base de données open source à combiner le modèle de document avec des garanties ACID.

#### Sans schéma (vraiment ?)

Cela signifie que vous n'avez pas à dire à la base de données la structure de vos données et les types primitifs à utiliser avant de pouvoir les gérer. Cela signifie également que vous pouvez mélanger des documents ayant différentes structures dans la même collection de données.

L'un des grands avantages est que _les migrations de schéma deviennent plus faciles_ (la plupart des ajustements de la base de données sont transparents et automatiques). Le retour en arrière est peu susceptible de causer des problèmes. Un autre avantage est que _l'extension dynamique des modèles de données existants avec des attributs personnalisés à l'exécution est simple_.

Mais tout cela ne signifie pas que vous n'avez aucun schéma du tout. S'il n'est pas **explicitement** déclaré, il brille **implicitement** à travers la logique de votre application. Il peut être déclaré de différentes manières pour gérer la validation des formulaires/données. De toute façon, vous devez toujours dire explicitement à la base de données comment créer des index pour garantir de bonnes performances.

En effet, la conception du schéma est la pierre angulaire de la création de bases de données exceptionnelles, qu'elles soient SQL ou non. Si vous ne comprenez pas vos données et les limitations du matériel et des logiciels, vous ne pouvez pas concevoir efficacement un schéma.

#### Non relationnel (vraiment ?)

Cela signifie que vous n'avez pas toujours besoin de créer une relation entre deux documents pour gérer des structures de données agrégées.

En effet, dans les bases de données relationnelles, la clause SQL JOIN vous permet de combiner des lignes de deux tables ou plus en utilisant un champ commun entre elles. Les bases de données orientées document comme MongoDB sont conçues pour stocker des données **dénormalisées**. Idéalement, il ne devrait y avoir aucune relation entre les collections : si les mêmes données sont requises dans deux documents ou plus, elles doivent être répétées. L'un des grands avantages est qu'une _seule opération de lecture_ est nécessaire pour obtenir toutes les données.

Mais vous pouvez toujours créer des relations et faire référence à un autre document si vous le souhaitez ou en avez besoin :

* par ID, puis vous pouvez le "peupler" manuellement avec une deuxième requête ou en utilisant [DBRefs](https://docs.mongodb.com/manual/reference/database-references/#dbrefs)
* par tout autre champ, puis vous pouvez utiliser l'opérateur [`$lookup`](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)

Cela rend MongoDB vraiment flexible et vous permet de choisir comment gérer les relations entre vos objets _au cas par cas_.

### Performance

#### Lecture/Écriture

Oui, MongoDB comme toute autre "vraie" base de données est conçu pour gérer un volume énorme de données. _En résumé, des centaines ou des milliers d'objets ne sont rien pour une base de données_, vous n'avez donc pas à vous inquiéter si vous avez de tels nombres. Vous pouvez trouver de nombreux benchmarks. En voici un simple pour vous donner un ordre de grandeur approximatif. Les documents stockés sont très simples et représentent typiquement une mesure horodatée :

```
{    value: random(0,100),    timestamp: date}
```

En raison de la manière dont MongoDB délègue la gestion de la mémoire au système d'exploitation, avoir des documents plus complexes (contenant typiquement des dizaines d'attributs) n'affecte pas significativement les résultats.

Les deux attributs ont été indexés. MongoDB ajoute et indexe automatiquement l'ID unique du document. J'ai testé trois requêtes :

* trouver la valeur maximale de la collection en utilisant le [framework d'agrégation](https://docs.mongodb.com/manual/aggregation/)
* trouver les 100 plus grandes valeurs supérieures à 99,9
* obtenir un seul document par ID

La requête "maximum" ne bénéficie pas des index en raison de l'agrégation, tandis que les requêtes "supérieur à" et "par ID" peuvent les utiliser. Vous verrez à quel point cela est important pour les performances.

La configuration de test était MongoDB 3.4.1 64 bits — OS Windows 7 Pro SP1 — CPU Core i7–4712HQ 2.3GHz — 16Go RAM — SSD HD, et les résultats des tests étaient les suivants :

Ainsi, si vous construisez les bons index en interrogeant un milliard de documents, cela reste performant pour la plupart des applications sur un seul serveur. Si nécessaire, vous pouvez augmenter les performances en utilisant le [sharding](https://docs.mongodb.com/manual/sharding/).

Voici les scripts utilisés pour créer/interroger la base de données pour ce test :

Et les commandes d'exécution :

```
// Lancer le serveur./mongod --dbpath "C:\Program Files\MongoDB\Server\3.4\data" --port 27018// Exemple d'insertion pour 10e7./mongo --port 27018 --eval "var arg1=10000000" create_collection.js// Requêtes./mongo --port 27018 --eval "" query_collection.js
```

#### Mémoire

Oui, MongoDB semble souvent utiliser toute la RAM disponible. Il repose en fait sur différents moteurs de stockage. [WiredTiger](https://docs.mongodb.com/manual/core/wiredtiger/) est le moteur par défaut à partir de MongoDB 3.2, et [MMAPv1](https://docs.mongodb.com/manual/core/mmapv1/) est le moteur par défaut pour les versions de MongoDB avant 3.2. Cependant, ils fonctionnent de manière assez similaire. Via le cache du système de fichiers, ils _utilisent automatiquement toute la mémoire libre qui n'est pas utilisée par le cache du moteur ou par d'autres processus_. Et cela est cohérent si vous souhaitez avoir des performances maximales.

Ainsi, les moniteurs de ressources système montrent souvent que MongoDB utilise beaucoup de mémoire, _mais son utilisation est dynamique_. Si un autre processus a soudainement besoin de la moitié de la RAM du serveur, MongoDB cédera la mémoire cache à l'autre processus.

Par conséquent, le seul paramètre que vous pouvez ajuster pour optimiser l'utilisation de la mémoire est la taille du cache du moteur. Par exemple, par défaut, le moteur WiredTiger utilise 50 % de la RAM moins 1 Go, ce qui peut être assez grand sur les serveurs avec beaucoup de mémoire. Cela peut même causer quelques problèmes si vous utilisez des conteneurs avec une mémoire limitée, [trouvez simplement le bon équilibre pour votre cas d'utilisation](https://docs.mongodb.com/manual/faq/storage/#to-what-size-should-i-set-the-wiredtiger-internal-cache).

#### Conclusion

J'espère que vous avez maintenant une idée plus précise des avantages offerts par MongoDB si cela correspond à vos besoins. Récemmment, MongoDB a lancé une offre de base de données en tant que service appelée [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) qui pourrait être utile pour vous pour tester.

_Si vous avez aimé cet article, n'hésitez pas à jeter un œil à [nos solutions Open Source](https://kalisio.com/#projects), l'équipe [Kalisio](https://kalisio.com/) !_