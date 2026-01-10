---
title: Récupérations ponctuelles de MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-18T15:10:12.000Z'
originalURL: https://freecodecamp.org/news/mongodb-point-in-time-recoveries-or-how-we-saved-600-dollars-a-month-and-got-a-better-backup-55466b7d714
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OD8s07RZ8po8hMY7q0Y2LQ.png
tags:
- name: database
  slug: database
- name: Devops
  slug: devops
- name: MongoDB
  slug: mongodb
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Récupérations ponctuelles de MongoDB
seo_desc: 'By Gitter

  (…or how we saved 600 dollars a month and got a better backup solution)

  At Gitter, a small startup, we work hard every day to provide the best chat for
  communities (have you checked Ping Pong Wars?), while keeping costs low. So when
  I found...'
---

Par Gitter

### (…ou comment nous avons économisé 600 dollars par mois et obtenu une meilleure solution de sauvegarde)

Chez [Gitter](http://gitter.im), une petite startup, nous travaillons dur chaque jour pour fournir le meilleur chat pour les communautés (avez-vous vérifié [Ping Pong Wars](https://gitter.im/dexterneo/ping_pong_wars) ?), tout en gardant les coûts bas. Alors quand j'ai découvert que nous payions 600 $ chaque mois pour un service de sauvegarde basique pour nos bases de données au lieu de cubes Rubik et de bière artisanale, j'ai pensé qu'il y avait une possibilité de gagner facilement.

Les récupérations ponctuelles sont à la pointe de la technologie lorsqu'il s'agit de sauvegarder vos bases de données. C'est-à-dire, être capable de cibler une transaction particulière, souvent catastrophique, et de récupérer complètement l'état de votre ensemble de données jusqu'à ce point. Notre solution ne fournissait que des sauvegardes horaires, ce qui n'est pas tout à fait suffisant pour nos besoins. Et pourtant, nous payions beaucoup d'argent pour cela. Bah.

Chez Gitter, nous utilisons MongoDB sur des instances EC2 avec des volumes EBS pour stocker nos ensembles de données. Cette solution est très pratique lorsqu'il s'agit d'architecturer un système de sauvegarde interne qui supporte les récupérations ponctuelles et c'est surprenamment plus facile que cela peut sembler. Je vais vous montrer comment nous le faisons.

### Le snapshot

Tout d'abord, la partie snapshot. Nous prenons des snapshots régulièrement en utilisant [un script que j'ai écrit](https://github.com/omame/mongodb-tools/blob/master/mongodb-ebs-snapshot). Il est basé sur [le tutoriel officiel](https://docs.mongodb.org/ecosystem/tutorial/backup-and-restore-mongodb-on-amazon-ec2/) de MongoDB, donc rien de trop surprenant ici. Les snapshots sont également très pratiques lorsque vous souhaitez lancer un nouveau nœud réplica : il suffit de créer une nouvelle instance en utilisant un volume de données basé sur le dernier snapshot, de l'ajouter à l'ensemble réplica et MongoDB ne rejouera que moins d'une heure d'oplog, ce qui est beaucoup plus rapide qu'une resynchronisation complète.

Vous voulez stocker à la fois les fichiers de données et le journal sur le même volume EBS : la plupart du temps, cela n'impacte pas les performances d'E/S et atteindre la cohérence peut être délicat autrement.

Ensuite, vous devez prendre un snapshot du volume EBS. Vous pouvez utiliser votre interface AWS favorite pour ce faire. Rappelez-vous que prendre un snapshot est une opération instantanée : une fois qu'AWS reçoit l'appel API, le volume sera "photographié" dans son état actuel, donc vous pouvez reprendre vos opérations d'écriture en toute sécurité. Néanmoins, il est recommandé d'effectuer cette opération sur un nœud secondaire.

L'avantage de prendre des snapshots EBS est qu'AWS compresse les blocs et ne stocke que les différentiels dans S3, ce qui représente une économie supplémentaire en termes de coût.

L'ensemble "freeze mongo ; take snapshot ; unfreeze mongo" prend environ 1,4 seconde pour nous, donc c'est un compromis abordable étant donné la grande commodité qu'il nous offre. De plus, l'avantage de la solution de snapshot EBS est qu'AWS compresse les blocs et ne stocke que les différentiels dans S3, ce qui représente une économie supplémentaire en termes de coût.

Mission accomplie, vous êtes un héros de l'économie de coûts ! Fermez tous ces comptes coûteux et contribuez à une augmentation de salaire. Mais est-ce suffisant ?

### La récupération

Avoir des snapshots EBS de votre ensemble de données MongoDB n'est granulaire qu'à la fréquence à laquelle vous les prenez, disons toutes les 30 minutes ou même une heure. Cela peut ne pas être suffisant et prendre un snapshot toutes les minutes peut être excessif (et vous aurez toujours une granularité d'une minute). Peu importe comment vous le présentez, certaines données seront perdues même si ce n'est que peu. Pour éviter cela, vous pouvez utiliser l'oplog de MongoDB pour rejouer les transactions à partir du moment du snapshot jusqu'à la transaction défectueuse et combler l'écart de temps. Notez que cela ne fonctionne que si votre fenêtre oplog est suffisamment large, alors soyez très prudent en dimensionnant votre oplog. Vous pouvez garder un œil dessus en utilisant [cet émetteur statsd](https://github.com/omame/mongodb-tools/blob/master/mongodb-oplog-window-size).

De plus, l'oplog doit être disponible sur un nœud réplica, même si l'ensemble de données est perdu. Dans le pire des scénarios, la transaction qui a détruit votre ensemble de données était si désastreuse que vous finirez par récupérer jusqu'au moment du snapshot, ce qui, compte tenu de l'ampleur du désastre, n'est pas une si mauvaise perspective.

Alors, où pouvez-vous obtenir l'oplog ? Un nœud secondaire est généralement un bon choix. Vous pouvez dumper l'oplog avec mongodump, mais il y a un piège : vous voulez uniquement dumper les transactions qui se sont produites après la dernière dans le snapshot que vous récupérez. La raison est que, par exemple, rejouer des insertions lorsqu'une contrainte d'index unique est présente fera échouer votre restauration. Vous voulez donc rogner votre oplog des deux côtés : après le snapshot et avant l'événement catastrophique.

![Image](https://cdn-media-1.freecodecamp.org/images/WIp4zpFAO2VPZNstAe9YFP9WYnJqjPTHK7Hk)

Pour ce faire, vous devez trouver le timestamp de la dernière transaction dans le snapshot. Créez un volume EBS en utilisant le snapshot pris avant l'événement catastrophique et montez-le sur une instance. Démarrez mongod en le liant à localhost et à un port temporaire, disons 27272. Ensuite, exécutez cette requête :

```
$ mongo --port 27272 local> db.oplog.rs.find({}, {ts: 1,}).sort({ts: -1}).limit(1){"ts" : Timestamp(1459850401, 11)}
```

Dumpez l'oplog à partir d'un nœud réplica secondaire en utilisant le timestamp nouvellement calculé pour la requête. Cela crée un répertoire appelé oplog avec le fichier bson de la collection oplog et les métadonnées de la collection, que nous ignorerons. Ne craignez pas de dumper l'oplog : ce n'est pas une opération très lourde et cela ne prendra que quelques secondes si vous avez une bande passante raisonnable.

```
$ mongodump -h secondary-node \--db local \--collection oplog.rs \--out oplog \--query '{"ts": { "$gt": { "$timestamp": {"t": 1459850401, "i": 11}}}}'
```

Convertissez les données bson en json pour qu'elles deviennent lisibles par les humains :

```
$ bsondump oplog/local/oplog.rs.bson > oplog.json
```

Trouvez le timestamp de la transaction erronée, qui représente le point jusqu'auquel vous voulez rejouer l'oplog :

```
$ grep "Hello. My name is Inigo Montoya. You killed my father. Prepare to die." oplog.json{"ts":{"$timestamp":{"t":1459852199,"i":1}},"h":{"$numberLong":"-6882763316726998947"},"v":2,"op":"i","ns":"quotes.movies","o":{"_id":{"$oid":"570393abf5d634897f2360a3"},"quote":"Hello. My name is Inigo Montoya. You killed my father. Prepare to die.","character":"Inigo Montoya","title":"The Princess Bride"}
```

Dans ce cas, votre timestamp est 1459852199:1.

Ensuite, déplacez l'oplog là où mongorestore le cherchera :

```
mv oplog/local/oplog.rs.bson oplog/oplog.bson
```

Vous êtes maintenant prêt à rejouer l'oplog en utilisant --oplogLimit pour définir le délimiteur :

```
$ mongorestore -h localhost:27272 --oplogReplay --oplogLimit 1459852199:1 oplog
```

Il est temps de vérifier votre base de données, mais il ne devrait pas y avoir de problèmes si vous avez suivi attentivement les instructions.

Vous êtes maintenant prêt à redémarrer l'instance en production. Bien joué !

_Cet article a été écrit par [Daniele Valeriani](https://twitter.com/escociao)._