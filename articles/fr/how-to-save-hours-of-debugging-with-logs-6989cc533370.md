---
title: Comment économiser des heures de débogage avec les logs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T17:34:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-save-hours-of-debugging-with-logs-6989cc533370
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mdCjm9D20RnHCIIQlgFr1w.jpeg
tags:
- name: Devops
  slug: devops
- name: logging
  slug: logging
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment économiser des heures de débogage avec les logs
seo_desc: 'By Maya Gilad

  A good logging mechanism helps us in our time of need.

  When we’re handling a production failure or trying to understand an unexpected response,
  logs can be our best friend or our worst enemy.

  Their importance for our ability to handle f...'
---

Par Maya Gilad

Un bon mécanisme de journalisation nous aide dans nos moments de besoin.

Lorsque nous gérons une panne de production ou que nous essayons de comprendre une réponse inattendue, les logs peuvent être notre meilleur ami ou notre pire ennemi.

Leur importance pour notre capacité à gérer les pannes est énorme. Dans notre travail quotidien, lorsque nous concevons notre nouveau service/fonctionnalité de production, nous négligeons parfois leur importance. Nous omettons de leur accorder l'attention nécessaire.

Lorsque j'ai commencé à développer, j'ai fait quelques erreurs de journalisation qui m'ont coûté de nombreuses nuits sans sommeil. Maintenant, je sais mieux, et je peux partager avec vous quelques pratiques que j'ai apprises au fil des ans.

### Pas assez d'espace disque

Lorsque nous développons sur notre machine locale, nous n'avons généralement pas de problème à utiliser un gestionnaire de fichiers pour la journalisation. Notre disque local est assez grand et la quantité d'entrées de log écrites est très faible.

Ce n'est pas le cas sur nos machines de production. Leur disque local a généralement un espace disque libre limité. Avec le temps, l'espace disque ne pourra plus stocker les entrées de log d'un service de production. Par conséquent, l'utilisation d'un gestionnaire de fichiers entraînera finalement la perte de toutes les nouvelles entrées de log.

Si vous souhaitez que vos logs soient disponibles sur le disque local du service, **n'oubliez pas d'utiliser un gestionnaire de fichiers rotatifs.** Cela peut limiter l'espace maximal que vos logs consommeront. Le gestionnaire de fichiers rotatifs gérera le remplacement des anciennes entrées de log pour faire de la place aux nouvelles.

### **Eeny, meeny, miny, moe**

![Image](https://cdn-media-1.freecodecamp.org/images/Pt2k019xulsxiiGcOhkWJ6R4Nm3QpN-THYid)

Notre service de production est généralement réparti sur plusieurs machines. La recherche d'une entrée de log spécifique nécessitera d'investiguer sur toutes celles-ci. Lorsque nous sommes pressés de corriger notre service, il n'y a pas de temps à perdre pour essayer de déterminer où exactement l'erreur s'est produite.

Au lieu de sauvegarder les logs sur le disque local, **transmettez-les vers un système de journalisation centralisé.** Cela vous permet de les rechercher tous en même temps.

Si vous utilisez AWS ou GCP, vous pouvez utiliser leur agent de journalisation. L'agent se chargera de transmettre les logs vers leur moteur de recherche de logs.

### Logger ou ne pas logger ? telle est la question...

![Image](https://cdn-media-1.freecodecamp.org/images/ZU2WKnvPTiAv6QIh8TUUQcK92TU5mSXgHjL3)

Il y a une fine ligne entre trop peu et trop de logs. À mon avis, les entrées de log doivent être significatives et ne servir qu'à investiguer les problèmes dans notre environnement de production. Lorsque vous êtes sur le point d'ajouter une nouvelle entrée de log, vous devriez réfléchir à la manière dont vous l'utiliserez à l'avenir. Essayez de répondre à cette question : **Quelles informations le message de log fournit-il au développeur qui le lira ?**

Trop souvent, je vois des logs utilisés pour l'analyse des utilisateurs. Oui, il est beaucoup plus facile d'écrire « user watermelon2018 a cliqué sur le bouton » dans une entrée de log que de développer une nouvelle infrastructure d'événements. Ce n'est pas à cela que servent les logs (et analyser les entrées de log n'est pas amusant non plus, donc extraire des insights prendra du temps).

### Une aiguille dans une botte de foin

Dans la capture d'écran suivante, nous voyons trois requêtes qui ont été traitées par notre service.

Combien de temps a-t-il fallu pour traiter la deuxième requête ? Est-ce 1ms, 4ms ou 6ms ?

```
2018-10-21 22:39:07,051 - simple_example - INFO - entered request 2018-10-21 
22:39:07,053 - simple_example - INFO - entered request 2018-10-21 
22:39:07,054 - simple_example - INFO - ended request 2018-10-21 
22:39:07,056 - simple_example - INFO - entered request 2018-10-21 
22:39:07,057 - simple_example - INFO - ended request 2018-10-21 
22:39:07,059 - simple_example - INFO - ended request
```

Puisque nous n'avons aucune information supplémentaire sur chaque entrée de log, nous ne pouvons pas être sûrs de la bonne réponse. Avoir l'ID de la requête dans chaque entrée de log aurait pu réduire le nombre de réponses possibles à une seule. De plus, **avoir des métadonnées dans chaque entrée de log peut nous aider à filtrer les logs** et à nous concentrer sur les entrées pertinentes.

Ajoutons quelques métadonnées à notre entrée de log :

```
2018-10-21 23:17:09,139 - INFO - entered request 1 - simple_example
2018-10-21 23:17:09,141 - INFO - entered request 2 - simple_example
2018-10-21 23:17:09,142 - INFO - ended request id 2 - simple_example
2018-10-21 23:17:09,143 - INFO - req 1 invalid request structure - simple_example
2018-10-21 23:17:09,144 - INFO - entered request 3 - simple_example
2018-10-21 23:17:09,145 - INFO - ended request id 1 - simple_example
2018-10-21 23:17:09,147 - INFO - ended request id 3 - simple_example
```

Les métadonnées sont placées dans la section de texte libre de l'entrée. Par conséquent, chaque développeur peut imposer ses propres normes et styles. Cela entraînera une recherche compliquée.

Nos métadonnées doivent être définies comme faisant partie de la structure fixe de l'entrée.

```
2018-10-21 22:45:38,325 - simple_example - INFO - user/create - req 1 - entered request
2018-10-21 22:45:38,328 - simple_example - INFO - user/login - req 2 - entered request
2018-10-21 22:45:38,329 - simple_example - INFO - user/login - req 2 - ended request
2018-10-21 22:45:38,331 - simple_example - INFO - user/create - req 3 - entered request
2018-10-21 22:45:38,333 - simple_example - INFO - user/create - req 1 - ended request
2018-10-21 22:45:38,335 - simple_example - INFO - user/create - req 3 - ended request
```

Chaque message dans le log a été repoussé par nos métadonnées. Puisque nous lisons de gauche à droite, nous devrions placer le message aussi près que possible du début de la ligne. De plus, placer le message au début « casse » la structure de la ligne. Cela nous aide à identifier le message plus rapidement.

```
2018-10-21 23:10:02,097 - INFO - entered request [user/create] [req: 1] - simple_example
2018-10-21 23:10:02,099 - INFO - entered request [user/login] [req: 2] - simple_example
2018-10-21 23:10:02,101 - INFO - ended request [user/login] [req: 2] - simple_example
2018-10-21 23:10:02,102 - INFO - entered request [user/create] [req: 3] - simple_example
2018-10-21 23:10:02,104 - INFO - ended request [user/create [req: 1] - simple_example
2018-10-21 23:10:02,107 - INFO - ended request [user/create] [req: 3] - simple_example
```

Placer le timestamp et le niveau de log avant le message peut nous aider à comprendre le flux des événements. Le reste des métadonnées est principalement utilisé pour le filtrage. À ce stade, il n'est plus nécessaire et peut être placé à la fin de la ligne.

Une erreur qui est enregistrée sous INFO sera perdue parmi toutes les entrées de log normales. **Utiliser toute la gamme des niveaux de journalisation (ERROR, DEBUG, etc.) peut réduire considérablement le temps de recherche.** Si vous souhaitez en savoir plus sur les niveaux de log, vous pouvez continuer à lire [ici](https://blog.scalyr.com/2017/12/logging-levels/).

```
2018-10-21 23:12:39,497 - INFO - entered request [user/create] [req: 1] - simple_example
2018-10-21 23:12:39,500 - INFO - entered request [user/login] [req: 2] - simple_example
2018-10-21 23:12:39,502 - INFO - ended request [user/login] [req: 2] - simple_example
2018-10-21 23:12:39,504 - ERROR - invalid request structure [user/login] [req: 1] - simple_example
2018-10-21 23:12:39,506 - INFO - entered request [user/create] [req: 3] - simple_example
2018-10-21 23:12:39,507 - INFO - ended request [user/create [req: 1] - simple_example
2018-10-21 23:12:39,509 - INFO - ended request [user/create] [req: 3] - simple_example
```

### Analyse des logs

Rechercher des entrées de log dans des fichiers est un processus long et frustrant. Cela nécessite généralement de traiter des fichiers très volumineux et parfois même d'utiliser des expressions régulières.

De nos jours, nous pouvons **tirer parti des moteurs de recherche rapides** tels qu'Elastic Search et indexer nos entrées de log. L'utilisation de la pile ELK vous fournira également la capacité d'analyser vos logs et de répondre à des questions telles que :

1. L'erreur est-elle localisée sur une seule machine ? Ou se produit-elle dans tout l'environnement ?
2. Quand l'erreur a-t-elle commencé ? Quel est le taux d'occurrence de l'erreur ?

Pouvoir effectuer des agrégations sur les entrées de log peut fournir des indices sur les causes possibles de pannes qui ne seraient pas remarquées simplement en lisant quelques entrées de log.

En conclusion, ne prenez pas la journalisation pour acquise. Pour chaque nouvelle fonctionnalité que vous développez, pensez à votre futur vous-même et à quelle entrée de log vous aidera et laquelle vous distraira simplement.

Rappelez-vous : vos logs vous aideront à résoudre les problèmes de production seulement si vous les laissez faire.