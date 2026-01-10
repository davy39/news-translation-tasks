---
title: Comment mettre à niveau les versions majeures de Postgres avec un temps d'arrêt
  quasi nul – un guide pratique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-15T21:42:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-upgrade-postgres-major-versions-with-near-zero-downtime
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Listen-Score-loves-postgres.png
tags:
- name: database
  slug: database
- name: postgres
  slug: postgres
seo_title: Comment mettre à niveau les versions majeures de Postgres avec un temps
  d'arrêt quasi nul – un guide pratique
seo_desc: "By Wenbin Fang\nIt's impossible to create zero-downtime Postgres upgrades\
  \ across major versions – right? Please, correct me if I’m wrong :) \nBut at least\
  \ we’ve found a way to get close to zero downtime.\n\nPostgreSQL Upgrades are hard!\n\
  How Retool upgrad..."
---

Par Wenbin Fang

Il est impossible de créer des mises à niveau de Postgres sans temps d'arrêt entre les versions majeures – n'est-ce pas ? Veuillez me corriger si je me trompe :) 

Mais au moins, nous avons trouvé un moyen de nous rapprocher du zéro temps d'arrêt.

* [Les mises à niveau de PostgreSQL sont difficiles !](https://andreas.scherbaum.la/blog/archives/1116-PostgreSQL-Upgrades-are-hard!.html)
* [Comment Retool a mis à niveau notre base de données PostgreSQL principale de 4 TB](https://retool.com/blog/how-we-upgraded-postgresql-database/)

Chez [Listen Notes](https://www.listennotes.com/), nous avons effectué des mises à niveau de versions majeures de Postgres deux fois depuis 2017, l'année où Listen Notes a été fondée. Lors de ces mises à niveau, nous n'avons subi aucun temps d'arrêt pour les opérations de "lecture", et moins d'une minute de temps d'arrêt pour les opérations d'"écriture".

Parcourons le processus que nous avons suivi pour mettre à niveau Postgres chez Listen Notes.

### **TL;DR**

1. Approvisionner une nouvelle base de données réplique (DB_A) avec l'ancienne version de Postgres.
2. Changer les adresses IP des hôtes de la base de données dans "etc/hosts" des serveurs en ligne pour utiliser la base de données réplique en lecture seule (pas DB_A). À partir de ce moment, toutes les opérations d'écriture échoueront.
3. Exécuter [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html) (avec "--link") sur DB_A pour passer à la nouvelle version de Postgres, et promouvoir DB_A comme base de données principale.
4. Remplacer toutes les adresses IP des hôtes de la base de données dans "etc/hosts" des serveurs en ligne pour utiliser DB_A. À partir de ce moment, les opérations d'écriture reprendront.
5. Réapprovisionner de nouveaux nœuds réplique avec la nouvelle version de Postgres.

## Comment nous utilisons Postgres dans Listen Notes

Listen Notes est un moteur de recherche de podcasts populaire. Nous fournissons un site web ([ListenNotes.com](https://www.listennotes.com/)) avec des millions de pages vues par mois, ainsi qu'une solide [API Podcast](https://www.listennotes.com/api/) utilisée par des milliers d'applications et de sites web tiers.

Nous utilisons Postgres comme notre base de données principale, qui stocke tous les podcasts, les métadonnées des épisodes et les données utilisateur. 

Nous exécutons un cluster Postgres auto-hébergé sur AWS EC2, composé d'un nœud principal (db1) pour les opérations d'écriture et de lecture, et de deux réplicas (db2 & db3) pour les opérations en lecture seule. La taille de la base de données est légèrement inférieure à 1 To.

### Progression de Postgres

Lorsque Listen Notes a été lancé en 2017, nous utilisions Postgres 9.6.

[Ensuite, nous avons mis à niveau vers Postgres 11.0 en 2019](https://www.listennotes.fm/p/monthly-update-for-may-2019-19-05-31).

[En 2021, nous utilisions Postgres 13.0](https://www.listennotes.fm/p/monthly-update-for-september-2021).

En général, nous ne sommes pas à l'aise avec l'utilisation de la dernière version de tout logiciel d'infrastructure, qu'il s'agisse de Postgres, Django, Redis ou autres.

Nous faisons confiance à la qualité de Postgres, mais il peut y avoir moins de documentation et de discussions en ligne pour la dernière version, ce qui pourrait rendre le dépannage difficile lorsque des problèmes spécifiques à une version se produisent.

Les serveurs Listen Notes qui communiquent avec la base de données Postgres utilisent des noms d'hôtes comme db1.internal.ln, db2.internal.ln, db3.internal.ln, et ainsi de suite.

Ces noms d'hôtes sont dans "etc/hosts", il est donc facile de changer l'adresse IP réelle tout en gardant les noms d'hôtes inchangés.

Il existe des charges de travail en ligne et hors ligne pour notre cluster Postgres. La charge de travail en ligne consiste à servir notre site web (ListenNotes.com) et les points de terminaison de l'API (PodcastAPI.com), qui ne peuvent pas avoir de temps d'arrêt prolongé (par exemple, plus de 5 minutes).

La charge de travail hors ligne exécute des tâches Celery et d'autres scripts qui peuvent être arrêtés pendant une période relativement longue (par exemple, 2 heures). Vous pouvez lire nos anciens articles de blog pour en savoir plus sur l'architecture de Listen Notes :

* [La technologie ennuyeuse derrière une entreprise Internet à une personne](https://www.listennotes.com/blog/the-boring-technology-behind-a-one-person-23/)
* [Un génie logiciel suffisant pour démarrer une entreprise Internet](https://www.listennotes.com/blog/good-enough-engineering-to-start-an-internet-27/)
* [Comment j'ai accidentellement construit une entreprise d'API Podcast](https://www.listennotes.com/blog/how-i-accidentally-built-a-podcast-api-business-46/)

Pour la mise à niveau de Postgres entre les versions majeures, notre objectif est d'atteindre un temps d'arrêt nul pour les opérations de lecture et un temps d'arrêt minimal (moins de 5 minutes) pour les opérations d'écriture. Cela garantira que la plupart de nos utilisateurs ne seront pas affectés pendant la mise à niveau.

## **Comment se préparer aux mises à niveau de Postgres**

La mise à niveau réelle peut prendre seulement 30 minutes, mais nous passons généralement quelques jours de travail à nous préparer, ce qui augmente les chances de succès pendant la mise à niveau.

### Étape de préparation 1 :

Nous devons nous assurer que la nouvelle version majeure de Postgres fonctionne bien avec notre base de code. Nous testons donc la nouvelle version de Postgres sur les environnements de développement et de pré-production. 

En plus des tests unitaires automatiques, nous devons tester manuellement toutes les fonctionnalités principales du produit.

### Étape de préparation 2 :

Les services en ligne ([ListenNotes.com](https://www.listennotes.com/) et [PodcastAPI.com](https://podcastapi.com/)) doivent fonctionner pour la plupart des utilisateurs même lorsque les opérations d'écriture de Postgres sont désactivées.

Pour ListenNotes.com, la majorité des utilisateurs effectuent des tâches "en lecture seule", telles que la recherche de podcasts, la navigation dans les détails des podcasts et des actions similaires inoffensives. Cela signifie que les échecs d'"écriture" ne devraient affecter qu'une infime fraction des utilisateurs.

Pour PodcastAPI.com, tous les points de terminaison de l'API sont en lecture seule ou déversent les écritures dans des tâches asynchrones hors ligne, de sorte que les opérations d'écriture peuvent être temporairement désactivées.

Nous passerions du temps à tester sur la pré-production pour nous assurer que les services en ligne peuvent toujours fonctionner lorsque les écritures dans la base de données sont désactivées.

### Étape de préparation 3 :

Nous passons le plus de temps à _répéter_ le processus de mise à niveau de Postgres. En gros, nous approvisionnons l'ensemble de la flotte de Listen Notes et pratiquons toutes les étapes nécessaires pour mettre à niveau Postgres.

Nous essayons de codifier certaines étapes dans des scripts Ansible ou Bash pour automatiser un peu. Nous documentons et chronométrons chaque étape. Au moment où nous l'exécutons dans l'environnement de production, nous savons combien de minutes (ou même de secondes) chaque étape prendra.

### Étape de préparation 4 :

Nous pratiquons comment revenir rapidement à l'ancienne version de Postgres, au cas où la mise à niveau échoue et que nous soyons forcés de restaurer un environnement stable dès que possible.

## **Comment mettre à niveau Postgres**

Nous effectuons généralement la mise à niveau réelle un vendredi soir, lorsque le trafic du site web et de l'API est faible. De plus, nous devons bien nous reposer pendant la journée, pour préserver suffisamment d'énergie pour effectuer de telles opérations dangereuses et stressantes en production plus tard dans la soirée :)

Puisque nous avons créé une liste de tâches détaillée dans Notion au cours des jours précédents de préparation, nous suivons soigneusement la liste de tâches pour mettre à niveau Postgres :

### Étape de mise à niveau 1 :

Nous approvisionnons une nouvelle base de données réplique en lecture seule avec l'ancienne version de Postgres. Appelons-la DB_A. Elle synchronisera les données de la base de données principale en temps réel, et sera mise à niveau vers la nouvelle version de Postgres avant d'être promue comme base de données principale. 

Si la mise à niveau sur DB_A échoue plus tard, nous avons toujours la possibilité de revenir rapidement en arrière et d'utiliser l'ancienne base de données principale à la place.

### Étape de mise à niveau 2 :

Nous arrêtons toutes les tâches hors ligne, sauf pour un travailleur Celery pour gérer certaines tâches asynchrones sensibles au temps, comme l'envoi d'e-mails de connexion. Nous arrêterons ce travailleur Celery juste avant l'étape 4. 

Nous retirons également la plupart des serveurs web/API du répartiteur de charge, ne laissant qu'une flotte minimale de serveurs en ligne.

### Étape de mise à niveau 3 :

Nous changeons toutes les adresses IP des hôtes de la base de données dans "etc/hosts" sur la flotte minimale de serveurs en ligne (par exemple, web, API…) pour utiliser une ancienne base de données en lecture seule. Appelons-la DB_B.

À partir de ce moment, toutes les opérations d'écriture devraient échouer. Cette étape est pour s'assurer que la future nouvelle base de données principale n'aura pas de données obsolètes.

### Étape de mise à niveau 4 :

Nous exécutons pg_upgrade (avec "--link") sur DB_A pour passer à la nouvelle version de Postgres, et la promouvoir comme base de données principale. À partir de ce moment, DB_A est la base de données principale, exécutant la nouvelle version de Postgres.

### Étape de mise à niveau 5 :

Nous remplaçons toutes les occurrences de l'IP de DB_B par celle de DB_A dans "etc/hosts" de la flotte minimale de serveurs en ligne (par exemple, web, API…). À ce stade, DB_A est utilisée à la fois comme base de données principale et réplique. Et les opérations d'écriture devraient fonctionner maintenant.

### Étape de mise à niveau 6 :

Nous changeons "etc/hosts" pour utiliser DB_A pour tous les hôtes de la base de données (principale + réplique) sur tous les autres serveurs et relançons les tâches hors ligne. 

Du point de vue des utilisateurs, tous les services de Listen Notes devraient être normaux maintenant. En fait, tous les utilisateurs de l'API ne devraient subir aucune interruption pendant tout le processus de mise à niveau, tandis qu'une infime partie des utilisateurs du site web peut rencontrer des erreurs lors de l'exécution d'opérations d'"écriture", telles que la création d'une playlist ou d'un clip de podcast.

### **L'étape la plus importante dans la mise à niveau vers une nouvelle version de Postgres**

Parmi toutes ces étapes, l'étape 4 est la plus critique. Si elle échoue ou prend trop de temps (par exemple, plus de 10 minutes), alors nous devons revenir en arrière en changeant "etc/hosts" sur ces serveurs en ligne.

D'après notre expérience, il a fallu moins d'une minute pour exécuter l'étape 4. Votre expérience peut varier si vous avez une base de données plus grande (ou plus petite).

Après nous être assurés que tout est revenu à la normale après l'étape 6, nous pourrions réapprovisionner les instances de base de données réplique avec la nouvelle version de Postgres. Et finalement, nous mettons fin aux anciennes instances de base de données.

## Réflexions finales

Cela semble complexe ? Oui, un peu…

Les opérations de base de données en production sont intrinsèquement complexes et dangereuses. Il ne faut pas se précipiter :)

![Image](https://production.listennotes.com/web/image/747a0d713bc541d8bc063df623d35ee0.jpeg)

## **FAQ**

### Pourquoi n'utilisez-vous pas Postgres géré, par exemple Amazon RDS ?

Nous voulons avoir un contrôle total sur les logiciels d'infrastructure clés (par exemple, Postgres, Elasticsearch…), car…

1. Nous ne voulons pas de verrouillage de plateforme
2. Nous voulons comprendre ce qui se passe à l'intérieur du serveur, en évitant d'attendre impuissants que les équipes de support client tiers (par exemple, AWS) aident à résoudre les problèmes urgents de production dans des boîtes noires
3. Il est plus rentable pour nous d'exécuter des instances Postgres sur nos propres serveurs – si l'argent n'était pas un problème (par exemple, lever des fonds importants de capital-risque) ou si nous avions moins d'expérience opérationnelle avec Postgres, alors Amazon RDS aurait pu être une bonne option pour commencer. Comme pour beaucoup de choses dans la vie, nous devons faire les choses avec des contraintes (comme l'argent, le temps, l'expertise…).

Pour autant que je sache, l'utilisation d'un Postgres géré (comme Amazon RDS) ne supprimera pas la douleur de la mise à niveau entre les versions majeures : recherchez "[Amazon RDS upgrade Postgres versions with zero downtime](https://www.google.com/search?q=amazon+rds+upgrade+postgres+versions+zero+downtime)".

### Pourquoi n'utilisez-vous pas des outils tiers pour automatiser un peu le processus (comme un bouton pour automatiser tout) ?

Nous ne savons pas s'il existe des outils tiers fiables faciles à utiliser, faciles à comprendre, sûrs à utiliser… Mais nous sommes ouverts aux recommandations – [wenbin@listennotes.com](mailto:wenbin@listennotes.com).

Nous devons souvent évaluer si cela vaut la peine de prendre le temps et le risque d'apprendre et d'utiliser de nouveaux outils de boîte noire en production, surtout pour des tâches DevOps sérieuses.

### Pourquoi n'utilisez-vous pas MySQL, MongoDB ou d'autres bases de données non-Postgres ?

Lorsque j'ai commencé Listen Notes, je connaissais Postgres bien mieux que MySQL et les autres bases de données, car mon ancien employeur Nextdoor.com utilise Postgres. Et je sais qu'Instagram et d'autres services en ligne à grande échelle utilisent également Postgres comme leur principal stockage de données (au moins pour les premières années). 

Si Postgres fonctionne bien pour d'énormes services en ligne, alors il devrait également fonctionner pour Listen Notes :) Parfois, nous passons du temps à apprendre de nouvelles technologies pour démarrer un projet, mais plus souvent, nous utilisons simplement les technologies que nous connaissons déjà afin de démarrer un projet plus rapidement et plus efficacement.

Encore une fois, la mise à niveau des bases de données non-Postgres entre les versions majeures n'est pas non plus facile… mais voici l'espoir que toutes les étapes ci-dessus aient aidé à faire de toute mise à niveau de Postgres que vous avez effectuée un succès !

_Cet article de blog a été initialement publié sur [ListenNotes.com](https://www.listennotes.com/blog/a-practical-way-to-upgrade-postgres-major-49/).