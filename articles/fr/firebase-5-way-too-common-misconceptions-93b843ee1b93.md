---
title: 'Firebase : 5 idées reçues beaucoup trop courantes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T16:12:26.000Z'
originalURL: https://freecodecamp.org/news/firebase-5-way-too-common-misconceptions-93b843ee1b93
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zdrREji23Eu5dqVVJE1E7w.png
tags:
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Firebase : 5 idées reçues beaucoup trop courantes'
seo_desc: 'By Cathryn Griffiths

  I’ve been reading a lot of online commentary recently about Firebase. Mostly — it
  must be pointed out — written by developers who hate Firebase.

  “Complex queries are impossible!” says one.

  “Dumb data modeling!” says another.

  “Eve...'
---

Par Cathryn Griffiths

J'ai lu beaucoup de commentaires en ligne récemment sur Firebase. Principalement — il faut le souligner — écrits par des développeurs qui détestent Firebase.

[« Les requêtes complexes sont impossibles ! »](https://crisp.chat/blog/why-you-should-never-use-firebase-realtime-database/) dit l'un.

[« Modélisation de données stupide ! »](https://medium.freecodecamp.com/firebase-the-great-the-meh-and-the-ugly-a07252fbcf15) dit un autre.

« [Tout doit être côté client !](https://lugassy.net/why-im-dumping-firebase-for-web-cd64a78cb43e) » se plaint un autre.

On peut presque entendre les petites veines saillantes sur leurs fronts.

Je comprends. Les problèmes qu'ils ont rencontrés sont frustrants. Mais une grande partie du problème est un manque de compréhension de Firebase, ce qu'il peut (et ne peut pas !) faire.

Je travaille avec Firebase depuis quelques mois. Chez [FFunction](https://ffctn.com/?utm_source=medium&utm_medium=5-firebase-myths&utm_campaign=general-pr), nous utilisons Firebase pour construire un [outil de planification de projet appelé Min](https://www.min.team/?utm_source=medium&utm_medium=5-firebase-myths&utm_campaign=early-access). Il y a de sérieuses idées reçues/mythes/incompréhensions sur cette solution de backend-as-a-service (BaaS). Alors, j'ai voulu en démystifier quelques-unes ici.

Au fait : Nous ne sommes en aucun cas affiliés à Firebase. Je veux ajouter un peu de nuance à ce qui devient une discussion assez unilatérale.

### Idée reçue #1 : Firebase est uniquement côté client

Jusqu'à récemment, Firebase était une technologie exclusivement côté client. Bien qu'il fournissait des capacités de stockage et de requêtage. Mais la majorité de la logique de votre application devait exister et s'exécuter sur le client. Pour de nombreux développeurs, c'était un véritable frein. Après tout, combien d'applications web ces jours-ci n'ont pas besoin de backend ?

L'équipe Firebase a en fait écouté les demandes de la communauté des développeurs. En mars 2017, ils ont introduit [Cloud Functions for Firebase](https://firebase.googleblog.com/2017/03/introducing-cloud-functions-for-firebase.html). Avec les cloud functions, vous pouvez sauvegarder des extraits de code sur Google Cloud. Ce code s'exécutera en réponse à des événements Firebase spécifiques et à des requêtes HTTP. Par exemple, si vous souhaitez effectuer un traitement de données lors de la sauvegarde de données dans la base de données, [vous pouvez le faire](https://firebase.google.com/docs/functions/use-cases#perform_database_sanitization_and_maintenance). De plus, si vous ne voulez pas que les clés API de votre application soient exposées dans votre code côté client, [vous pouvez le faire aussi](https://firebase.google.com/docs/functions/use-cases#integrate_with_third-party_services_and_apis).

Si vous êtes intéressé à en savoir plus, je vous recommande de consulter la [documentation sur les Cloud Functions pour Firebase](https://firebase.google.com/docs/functions/) (qui contient quelques excellents exemples) et [ces tutoriels récemment publiés](https://www.youtube.com/playlist?list=PLl-K7zZEsYLkPZHe41m4jfAxUi0JjLgSM).

### Idée reçue #2 : Firebase entraîne du code spaghetti

Cela me fait penser à ce vieux adage : « Un mauvais ouvrier blâme ses outils ! » Mais creusons un peu ce sujet.

D'après mon expérience jusqu'à présent, Firebase n'entraîne pas de code spaghetti. Puisque Firebase est principalement côté client, la plupart de votre logique backend se retrouvera sur le client. Si vous n'êtes pas prudent, vous pourriez vous retrouver avec un tas de code désordonné et difficile à maintenir.

Dans les premières étapes du développement de [Min](https://www.min.team/?utm_source=medium&utm_medium=5-firebase-myths&utm_campaign=early-access), nous avons passé beaucoup de temps à planifier l'application. Nous avons planifié comment modéliser nos données, la structure de notre base de données et la meilleure façon d'interagir avec nos données. Nous avons créé un connecteur pour communiquer avec Firebase. Il contenait tout le code pour effectuer des opérations CRUD et pour interagir avec Firebase. Nous avons construit une collection de classes pour traiter les données des objets selon la structure de la base de données Firebase.

Cette abstraction nous a aidés à garder la logique liée à Firebase et la logique de l'application séparées. Notre code était maintenable et facile à déboguer.

### Idée reçue #3 : Modélisation de données stupide / trop de duplication

Comme l'équipe Firebase le décrit, la base de données Firebase est [juste un gigantesque arbre JSON](https://firebase.google.com/docs/database/web/structure-data#how_data_is_structured_its_a_json_tree). Les données sont stockées sous forme de collections de paires clé-valeur et peuvent avoir toute la largeur et la profondeur que vous souhaitez. Il y a beaucoup de flexibilité dans la façon dont vous pouvez stocker vos données, ce qui peut vous causer beaucoup de problèmes si vous n'êtes pas prudent. Permettez-moi de montrer cela avec un exemple.

Disons que vous construisez une application de gestion de projet de base. Vous avez des utilisateurs et des tâches. Les utilisateurs peuvent être assignés à des tâches. Vous pourriez vouloir stocker toutes les informations sur les tâches dans un seul emplacement de la base de données sous le nœud des tâches :

```
tasks : {    "001" : {        name         : "Development Round 1"        description  : "Lorem ipsum dolor sit amet elit..."        startDate    : "20170101"        endDate      : "20170201"        loggedHours  : {            "20170101" : "1.66"            "20170102" : "7"            "20170103" : "5.5"        }        assignedStaff : "Cathryn"    }    "002" : {        name : "Development Round 2"        description : "Mauris quis turpis ut ante..."        startDate   : "20170206"        endDate     : "20170228"        loggedHours  : {            "20170206" : "3"            "20170207" : "1"            "20170208" : "4.75"        }        assignedStaff : "Sam"    }    "003" : {        name : "Browser Testing"        description : "Vivamus nec ligula et nulla blandit..."        startDate   : "20170301"        endDate     : "20170303"        loggedHours  : {            "20170301" : "1"            "20170301" : "3"        }        assignedStaff : "Cathryn"    }}
```

Maintenant, disons que vous voulez afficher le nom des tâches assignées à Cathryn. Pour ce faire, vous pourriez interroger la base de données pour retourner toutes les tâches dont la valeur « assignedStaff » est « Cathryn ».

```
firebase.database().ref("tasks/").orderByValue("assignedStaff").equalTo("Cathryn").once("value");
```

Le problème avec cette requête est qu'elle retournera _toutes_ les informations sur les tâches assignées à Cathryn, et pas seulement le nom de la tâche. Cela représente beaucoup de données inutiles à télécharger.

Pour corriger cela, Firebase recommande de [dénormaliser vos données](https://firebase.googleblog.com/2013/04/denormalizing-your-data-is-normal.html) ([il y a un excellent guide sur ce sujet ici](https://www.youtube.com/watch?v=vKqXSZLLnHA&index=6&list=PLl-K7zZEsYLlP-k-RKFa7RyNPa9_wCH2s&t=1s)). La dénormalisation est un processus de stockage de copies redondantes de données dans toute la base de données, pour améliorer les performances de lecture. Dans notre exemple, nous pourrions dénormaliser nos données en ajoutant ce qui suit à notre base de données :

```
tasksByUser : {    "Cathryn" : {        "001" : "Development Round 1"        "003" : "Browser Testing"    }    "Sam" : {        "002" : "Development Round 2"    }}
```

Maintenant, si nous voulons récupérer les noms des tâches assignées à Cathryn, nous devons simplement lire à partir d'un seul emplacement de la base de données :

```
firebase.database().ref("tasksByUser/Cathryn").once("value");
```

Comparé à notre requête précédente, cela retournera le nom des tâches assignées à Cathryn. Cela entraîne des opérations de lecture plus rapides avec de meilleures performances à long terme.

La dénormalisation peut sembler un hack pour certains. Mais c'est une stratégie impérative lors de la conception d'une base de données Firebase pour une application web complexe et évolutive. Cela nécessite que vous ayez une compréhension approfondie des données que vous souhaitez stocker et de la manière dont vous allez les utiliser.

Avant de vous lancer dans la construction de votre base de données Firebase, prenez le temps d'apprendre sur [la dénormalisation](https://www.youtube.com/watch?v=vKqXSZLLnHA), [comment structurer vos données](https://firebase.google.com/docs/database/web/structure-data), et [comment maintenir la cohérence des données dénormalisées](https://firebase.googleblog.com/2015/09/introducing-multi-location-updates-and_86.html). Comme l'équipe Firebase l'a dit, « Considérez que l'espace disque est bon marché, mais le temps d'un utilisateur ne l'est pas. »

Si vos temps de lecture sont lents, alors il y a des chances que vos utilisateurs ne resteront pas.

De plus, des requêtes inefficaces qui retournent des données inutiles peuvent être coûteuses financièrement. Selon votre plan de tarification Firebase, vous pourriez devoir payer jusqu'à [1 $ par Go téléchargé](https://firebase.google.com/pricing/).

### Idée reçue #4 : Firebase peut entraîner des incohérences de données

Si vous concevez votre base de données Firebase de la bonne manière, il y a des chances que vos données soient dénormalisées à travers plusieurs emplacements de la base de données. Et si vos données sont stockées à plusieurs emplacements, alors vous vous demandez probablement... « comment vais-je garder toutes ces données cohérentes ? »

Dans un cas normal, lors de l'envoi de données à Firebase, vous spécifiez un chemin de base de données et les données que vous souhaitez y stocker. Revenons à l'exemple, pour mettre à jour un nom de tâche (avant d'utiliser la dénormalisation), je ferais ceci :

```
firebase.database().ref("tasks/001/name").set("Here's the new name");
```

Maintenant, avec la dénormalisation, je pourrais mettre à jour le nom d'une tâche en effectuant deux opérations d'écriture :

```
firebase.database().ref("tasks/001/name").set("Here's the new name");
```

```
firebase.database().ref("tasksByUser/Cathryn/001").set("Here's the new name");
```

Mais effectuer ces deux opérations d'écriture peut entraîner des incohérences de données. Que se passe-t-il si l'une des opérations d'écriture échoue et que l'autre ne le fait pas ? Ce dont j'ai besoin, c'est d'une opération d'écriture atomique, me permettant d'écrire dans les chemins de la base de données en même temps. Pour cela, Firebase fournit des [mises à jour multipath](https://firebase.googleblog.com/2015/09/introducing-multi-location-updates-and_86.html) pour résoudre exactement ce problème. Vous pouvez regarder un excellent guide sur ce sujet [ici](https://www.youtube.com/watch?v=i1n9Kw3AORw&index=7&list=PLl-K7zZEsYLlP-k-RKFa7RyNPa9_wCH2s&t=4s). Maintenant, pour mettre à jour un nom de tâche, nous devons simplement faire ce qui suit :

```
firebase.database().ref().update({    "tasks/001/name" : "Here's the new name",    "tasksByUser/Cathryn/001" : "Here's the new name"});
```

Si la mise à jour échoue à l'un des chemins de la base de données, toute la mise à jour échouera. Tant que vous utilisez des mises à jour multipath, vos données devraient toujours être cohérentes.

### Idée reçue #5 : Capacités de requêtage très limitées

Firebase a des capacités de requêtage limitées. Vous pouvez trier les données par clés ou par valeur et filtrer les données par égalité ou en utilisant des plages.

Par exemple, en utilisant les exemples de tâches et d'utilisateurs. Je pourrais faire une requête pour récupérer les tâches qui commencent le, avant ou après 20170601. Je pourrais également faire une requête pour récupérer toutes les tâches assignées à Cathryn, ou qui ont des heures enregistrées pour 20170203. Mais ce que je _ne peux pas_ faire, c'est filtrer par plusieurs valeurs ou clés. Par exemple, je ne peux pas faire une requête pour récupérer les tâches assignées à Cathryn _et_ qui commencent après 20170601. Une requête pour récupérer les tâches qui ont des heures enregistrées le 20170203 et le 20170304 ne fonctionnera pas non plus.

Les requêtes ou le filtrage sur plusieurs clés ou valeurs ne fonctionnent pas, et les développeurs adorent s'en plaindre. Mais s'ils faisaient leurs recherches, ils réaliseraient qu'il y a en fait une très bonne raison à cela. Puisque Firebase est une base de données en temps réel et conçue pour la vitesse, [Firebase ne supporte que les opérations qu'il peut garantir être rapides](https://firebase.googleblog.com/2013/04/denormalizing-your-data-is-normal.html). Si vous voulez effectuer des requêtes complexes, vous devrez concevoir votre base de données en conséquence. Les requêtes complexes ne sont pas impossibles, vous devez simplement les planifier à l'avance.

Par exemple, si je voulais faire une requête pour récupérer toutes les tâches assignées à Cathryn qui commencent le 20170201. Je pourrais ajouter une propriété « staff_startDate » à mes tâches, comme suit :

```
tasks : {    "001" : {        ...        startDate       : "20170101"        assignedStaff   : "Cathryn"        staff_startDate : "Cathryn_20170101"        ...    }    ...}
```

Ensuite, je devrais simplement faire cette requête :

```
firebase.database().ref("tasks/").orderByChild("staff_startDate").equalTo("Cathryn_20170101");
```

Je vous recommande vivement de regarder [Common SQL Queries converted for the Firebase Database](https://www.youtube.com/watch?v=sKFLI5FOOHs&t=7s) et [Firebase Database Querying 101](https://www.youtube.com/watch?v=3WTQZV5-roY). Savoir comment structurer et requêter vos données vous permettra d'effectuer des requêtes plus avancées. Cela vous évitera beaucoup de maux de tête à l'avenir.

J'ai décidé de suivre cet article avec une liste de contrôle des meilleures pratiques Firebase. Si vous mettez votre email dans la boîte ci-dessous, je vous l'enverrai.

En attendant, j'aimerais avoir des nouvelles d'autres développeurs utilisant Firebase.

Est-ce que quelqu'un d'autre aime Firebase ?

Pas tant que ça ?

Vous vous cognez la tête contre l'écran ?

Parlez-moi, développeurs. Les commentaires sont ouverts.