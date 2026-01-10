---
title: Comment j'ai construit un crawler web sans serveur pour extraire des données
  immobilières de Vancouver à grande échelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-23T04:42:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-scalable-crawler-on-the-cloud-that-can-mine-thousands-of-data-points-costing-less-a9825331eef5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6PzbAGogRZ7eluH7lI17fA.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Comment j'ai construit un crawler web sans serveur pour extraire des données
  immobilières de Vancouver à grande échelle
seo_desc: 'By Marcello Lins

  I recently moved from Rio de Janeiro, Brazil to Vancouver, Canada. The first thing
  that hits you right in the face, aside from the beautiful scenery, are the rental
  prices. Vancouver is currently ranked among the top 5 most expensive...'
---

Par Marcello Lins

J'ai récemment déménagé de Rio de Janeiro, Brésil, à Vancouver, Canada. La première chose qui vous frappe en plein visage, en plus des magnifiques paysages, ce sont les prix des locations. Vancouver est actuellement classée parmi les 5 villes les plus chères au monde où vivre. Le prix de location d'un bien est indicatif de son coût d'achat et d'hypothèque.

J'ai décidé de lancer un projet parallèle pour extraire un nombre décent d'annonces immobilières et analyser les données. Je voulais tirer mes propres conclusions sur le marché immobilier actuel à Vancouver. Il y a une multitude de données bien formatées sur ces sites d'annonces en ligne, alors pourquoi ne pas les récupérer ? C'est ainsi que ce projet est né.

Cet article vous guidera à travers l'architecture, les coûts, les avantages et inconvénients, et plus encore, concernant le premier crawler que j'ai construit sans utiliser de serveurs. Il est entièrement hébergé dans le cloud, en utilisant uniquement AWS (Amazon Web Services).

### Attendez, avez-vous dit « Sans Serveur » ?

Bien sûr, tout ce que vous exécutez dans le cloud repose finalement sur des serveurs. Ce que je veux dire par « sans serveur » (Server-less), c'est que vous n'aurez pas à maintenir vous-même un serveur ou une machine virtuelle.

L'astuce consiste à construire votre architecture autour de services natifs du cloud tels que [AWS Lambda](https://aws.amazon.com/lambda/), [DynamoDB](https://aws.amazon.com/dynamodb/), [RDS MySQL](https://aws.amazon.com/rds/mysql/) et [Cloudwatch](https://aws.amazon.com/cloudwatch/). Ensuite, faites-les fonctionner ensemble de manière intelligente.

Commençons-nous ?

### Architecture du Projet

![Image](https://cdn-media-1.freecodecamp.org/images/oG0rJUB7H8x1Ke79IaTSCfcdj-dkTpDVSboU)

Si vous n'êtes pas familier avec ces services, voici un résumé :

* [AWS Lambda](https://aws.amazon.com/lambda/) :
Fonctions éphémères qui s'exécutent dans le cloud
Chaque fois qu'elles sont invoquées ou déclenchées, elles démarrent, exécutent le code que vous avez écrit, puis s'arrêtent dès que l'exécution est terminée. Vous ne payez que pour les secondes pendant lesquelles chaque fonction est effectivement en cours d'exécution.
* [DynamoDB](https://aws.amazon.com/dynamodb/) :
Base de données NoSQL entièrement gérée dans le cloud
Vous pouvez l'alimenter avec des enregistrements JSON qui seront stockés sur un serveur que vous n'aurez pas à maintenir. Vous pouvez ajuster la capacité de lecture et d'écriture en quelques secondes. Depuis début 2017, ils prennent en charge un mécanisme [TTL](https://aws.amazon.com/about-aws/whats-new/2017/02/amazon-dynamodb-now-supports-automatic-item-expiration-with-time-to-live-ttl/) (Time To Live). Cela permet à vos objets d'être supprimés automatiquement après avoir atteint leur TTL.
* [RDS MySQL](https://aws.amazon.com/rds/) :
Base de données MySQL entièrement gérée dans le cloud
Vous pouvez ajuster la taille, prendre des sauvegardes à votre guise. Nous avons récemment annoncé une nouvelle fonctionnalité [Start and Stop](https://aws.amazon.com/about-aws/whats-new/2017/06/amazon-rds-supports-stopping-and-starting-of-database-instances/). Elle vous permet de garder votre instance arrêtée pendant jusqu'à 7 jours consécutifs. Vous ne payez que pour le volume de l'instance, au lieu de payer également pour les heures d'instance.
* [CloudWatch](https://aws.amazon.com/cloudwatch/) :
Surveille et journalise vos ressources dans le cloud
Vous obtenez cela gratuitement puisque chaque message de « log » exécuté depuis Python sur Lambda est directement journalisé dans un flux CloudWatch.

### Objectifs du Projet

En démarrant ce projet, j'avais quelques objectifs en tête. Ensuite, j'ai commencé à improviser au fur et à mesure. Le projet idéal pour moi devait :

* Être entièrement géré par AWS dans le Cloud et ne nécessiter aucun serveur
* Être élastique pour s'adapter à la charge
* Capable de traiter des dizaines de milliers d'annonces pour commencer
* Être peu coûteux

### Détail des Coûts

Vous pouvez compter sur Lambda et CloudWatch pour ce projet. Ils sont gratuits sauf si vous exécutez cela en continu et sans interruption. Ensuite, la facture arrivera.

Pour les couches de stockage de DynamoDB et RDS MySQL, vous paierez moins de 3 dollars par mois. Vous pouvez arrêter votre base de données RDS pendant jusqu'à 7 jours consécutifs. Et vous pouvez réduire vos tables DynamoDB à 1 unité de lecture + 1 unité d'écriture lorsque vous ne les utilisez pas.

Cela porte vos coûts totaux à une estimation de 2,40 $ par mois. Consultez [ma documentation](https://github.com/MarcelloLins/ServerlessCrawler-VancouverRealState/wiki) pour une ventilation plus détaillée.

### Le Voyage

De début à fin, le projet entier m'a pris environ 19 heures de travail. Votre expérience peut varier en fonction de vos connaissances préalables d'AWS et de Python. Je suis familier avec les deux, mais pas avec les services Dynamo et Lambda.

La configuration des fonctions Lambda prend du temps pour s'y habituer. C'est définitivement en dessous de la moyenne par rapport à d'autres services AWS en termes de convivialité et de métriques.

Une fois que vous vous êtes habitué à la danse du développement Lambda : `éditer les fichiers Python localement` -> créer un package .zip` -> uploa`d pour remplacer votre Fonction Lambda -> Sauvegarder` et Tester, cela devient mieux.

L'intégration avec CloudWatch est définitivement un plus. C'est gratuit, et cela s'avère utile lorsque vous essayez de comprendre pourquoi votre lambda a échoué après cette requête HTTP, ou pendant cette autre boucle que vous avez oublié d'indenter.

L'utilisation de [Variables d'Environnement](http://docs.aws.amazon.com/lambda/latest/dg/env_variables.html), l'ajustement des ressources et des délais d'attente des fonctions, et l'activation et la désactivation des déclencheurs pour les tests fonctionnent en douceur et s'intègrent très bien. Cela ne nécessite pas de redéployer vos fonctions. De plus, j'ai remarqué que le démarrage des fonctions Lambda est rapide, avec un délai presque imperceptible. J'imagine qu'ils utilisent une sorte de cache intelligent [ECS](https://aws.amazon.com/ecs/) sous le capot, mais je ne saurais le dire.

La configuration des tables DynamoDB ne pourrait pas être plus simple. Nous parlons d'une configuration en une étape, où vous n'avez qu'à remplir 2 champs : le nom de votre table et la clé de partition pour votre table. La configuration du TTL pour chaque table fonctionne bien. Mais vous ne pouvez pas l'activer et la désactiver souvent. Cela vous empêchera de basculer, car il supprime vos enregistrements sans vous facturer pour ces opérations. L'insertion manuelle d'enregistrements DynamoDB dans chaque table à des fins de test fonctionne parfaitement. Chaque insertion ou lot déclenche les fonctions lambda avec peu ou pas de délai. Ajustez la capacité de chaque table avec des unités de lecture et d'écriture est un jeu d'enfant. Cela vous permet de les ajuster avec seulement quelques secondes de délai pour appliquer la nouvelle configuration.

Configurer RDS MySQL est définitivement plus facile que Lambda, mais comporte plus d'étapes que DynamoDB. Vous avez également plus d'options. Vous pouvez choisir le type d'instance, les tailles et types de volume, la redondance, les fenêtres de maintenance et les périodes de conservation des sauvegardes. Une fois configuré, vous aurez votre instance MySQL prête à l'emploi en environ 10 minutes.

Après la phase de configuration et de test, j'ai eu un moment de contemplation alors que les annonces étaient en train de se diriger vers MySQL. Je pouvais m'asseoir, me détendre et boire une bière pendant que la capture se faisait. Ou trois bières. Faire une sieste ? *Cette chose est lente !*

### Points Difficiles

La performance n'a jamais été mon objectif. Jouer avec les technologies disponibles et construire quelque chose de cool l'était. Mais je ne m'attendais pas à ce que ce soit si lent. Au final, il a pu capturer environ 11 000 annonces toutes les 6 heures, ce qui équivaut à environ une annonce toutes les ~2 secondes. J'ai écrit des crawlers distribués avec des taux facilement trente fois plus rapides que celui-ci. Ils n'étaient peut-être pas aussi excitants, cependant.

Chaque requête HTTP pour une page prend entre 0,7 et 1,1 seconde en moyenne. Ajoutez à cela le temps nécessaire pour démarrer chaque conteneur lambda, plus la connexion à MySQL et l'insertion de chaque enregistrement, vous obtenez 2 secondes. Chaque lambda reçoit un lot ou un flux de 5 enregistrements DynamoDB. La durée de vie moyenne de chaque fonction lambda était d'environ 7 secondes pour les lambdas d'analyse.

Quelques optimisations qui pourraient être faites seraient d'effectuer les requêtes HTTP pour chaque lot en parallèle et d'effectuer des insertions par lots dans MySQL.

En parlant de parallélisme, le seau d'eau froide le plus glacial pour moi a été le fait que Lambda ne s'adapte pas très bien horizontalement. Dans ma tête, chaque flux inséré dans Dynamo déclencherait immédiatement une fonction lambda pour le traiter. Cela signifiait que Lambda rattraperait toujours le rythme des insertions sur Dynamo. J'aurais donc des dizaines de fonctions Lambda en cours d'exécution à tout moment, toutes en parallèle, et c'était magnifique. **J'avais tort**

Ce qui se passe réellement, c'est que Lambda a une limite de [exécutions simultanées](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html) qui est liée au nombre de shards que la table DynamoDB possède. Comme ma table n'avait qu'un seul shard, il n'y avait qu'une seule fonction Lambda en cours d'exécution à tout moment. Ce qui s'est passé, c'est que même si les insertions dans l'une des tables DynamoDB ont pris quelques minutes, la deuxième couche de Lambda était déclenchée lentement, l'une après l'autre. Il y avait une file d'attente interne stockant mes flux Dynamo et les alimentant à Lambda en sérialisant mon exécution au lieu de la paralléliser.

Chaque changement dans le contenu d'une table DynamoDB déclenchera vos fonctions Lambda configurées pour se déclencher. Le piège est que ces changements peuvent ne pas être uniquement des insertions, mais aussi des mises à jour, et certaines suppressions déclenchées lorsque le collecteur TTL se met en marche et commence à effacer vos enregistrements configurés pour expirer. Heureusement, chaque flux DynamoDB contient pour chaque enregistrement dans le flux un attribut que vous pouvez utiliser pour déterminer si cet objet a été inséré, mis à jour ou supprimé. Je recevais tout car il n'y a aucun moyen de configurer Lambda autrement, mais je ne traitais que les insertions.

### Avantages et Inconvénients

**Avantages** :

* Peu coûteux
* Entièrement géré / Sans serveur
* Technologie de pointe
* Infrastructure flexible
* Si vous trouvez un bug, vous pouvez modifier vos lambdas immédiatement pour corriger chaque lot suivant

**Inconvénients** :

* Lent
* Une fois lancé, vous ne pouvez pas le mettre en pause et le redémarrer là où il s'est arrêté
* Seules certaines modifications sont possibles (modifications du code)
* Tester des parties spécifiques nécessite de désactiver et d'activer constamment les déclencheurs Lambda

### Verdict Final

Malgré l'attrait initial, je ne recommanderais pas cette architecture pour quelque chose qui nécessite des performances et une flexibilité pour changer facilement d'architecture et ajuster plus que le code en cours d'exécution. Mais cette configuration est peu coûteuse et pour quelque chose de petit, elle fonctionne bien. Ce n'est peut-être pas la plus facile à configurer, mais une fois que vous avez passé cette étape, la maintenance est pratiquement nulle.

J'ai pris du plaisir à écrire cela et à assembler toutes ces pièces pour construire ce petit Frankenstein. Je le referais. J'ai toujours coché les cases de tous mes objectifs initiaux pour ce projet, mais oui, la performance pourrait être meilleure.

En fin de compte, j'ai réussi à télécharger les données de plus de 40 000 annonces en exécutant ce processus plusieurs fois. Avec cela en main, je prévois d'écrire le code pour analyser ces données, mais pour l'instant, cela reste un travail en cours.

Je ne peux que vous remercier si vous êtes arrivé jusqu'ici. J'ai rassemblé un guide sur la façon de [configurer votre propre compte AWS](https://github.com/MarcelloLins/ServerlessCrawler-VancouverRealState/wiki/How-do-I-set-this-up-On-My-Own-AWS-Account%3F). Puisque le code est [open-source](https://github.com/MarcelloLins/ServerlessCrawler-VancouverRealState) de toute façon, allez le modifier !

Le code est ouvert sur [GitHub](https://github.com/MarcelloLins/ServerlessCrawler-VancouverRealState) si vous souhaitez le consulter. L'article original a été publié [sur mon blog](https://techflow.me/). Passez voir si vous voulez voir sur quoi je travaille d'autre.

N'hésitez pas à me contacter via n'importe quel contact sur ma [page personnelle](http://about.me/marcellolins), au cas où vous auriez des questions ou simplement envie de discuter.

À la prochaine :)