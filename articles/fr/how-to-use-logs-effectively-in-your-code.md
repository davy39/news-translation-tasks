---
title: Logger ou ne pas logger — Une stratégie alternative pour faire des loggers
  vos alliés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T01:28:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-logs-effectively-in-your-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/shakespeare.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: logging
  slug: logging
seo_title: Logger ou ne pas logger — Une stratégie alternative pour faire des loggers
  vos alliés
seo_desc: "By Stanley Nguyen\nLogging is universally present in software projects\
  \ and has many different forms, requirements, and flavors. \nLogging is everywhere,\
  \ from small 1-person-startups to large enterprises. Even a simple algorithmic programming\
  \ question i..."
---

Par Stanley Nguyen

Le logging est universellement présent dans les projets logiciels et prend de nombreuses formes, exigences et variantes différentes.

Le logging est partout, des petites startups d'une seule personne aux grandes entreprises. Même une simple question de programmation algorithmique implique un certain logging en cours de route.

Nous dépendons tellement du logging pour développer, maintenir et garder nos programmes en fonctionnement. Cependant, peu d'attention a été accordée à la manière de concevoir le logging au sein de nos systèmes.

Souvent, le logging est traité comme une réflexion secondaire – il n'est ajouté au code source qu'au moment de l'implémentation, comme une sorte de poudre magique qui aide à éclairer l'abysse opérationnel quotidien de nos systèmes.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/salt-logger-1.jpg)
_Sommes-nous tous des fans de logs ?_

Tout comme tout code écrit finit par devenir une dette technique – un processus que nous ne pouvons que ralentir avec une grande discipline – les loggers se dégradent à une vitesse incroyable. Après un certain temps, nous nous retrouvons à corriger des problèmes causés par les loggers plus souvent que les loggers ne nous donnent des informations utiles.

Alors, comment pouvons-nous gérer ce désordre avec les loggers et en faire l'un de nos alliés plutôt que des fantômes hérités qui nous hantent à cause des erreurs de développement passées ?

## « État de l'art »

Avant de plonger plus profondément dans ma solution proposée, définissons un énoncé concret du problème basé sur mes observations.

Alors, qu'est-ce que le logging exactement ? Voici une définition intéressante et pertinente que j'ai trouvée dans [l'article de Colin Eberhardt](https://www.codeproject.com/Articles/42354/The-Art-of-Logging) :

> Le logging est le processus d'enregistrement des actions et de l'état de l'application vers une interface secondaire.

C'est exactement ainsi que le logging est intégré dans les systèmes. Nous semblons tous convenir inconsciemment que les loggers n'appartiennent à aucune couche particulière de nos systèmes. Au lieu de cela, nous les considérons comme étant à l'échelle de l'application et partagés entre différents composants.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/stackoverflow-answer.png)
_Une réponse très approuvée sur StackOverflow_

Un simple diagramme où le logging a été intégré dans un système conçu avec [une architecture propre](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/logging-arch.png)

Nous pouvons dire en toute sécurité que le logging lui-même est un sous-système au sein de notre application. Et nous pouvons dire en toute sécurité que, sans une considération minutieuse, il sort souvent du contrôle plus rapidement que nous ne le pensons.

Bien que concevoir le logging comme un sous-système au sein de nos applications ne soit pas faux, la perception traditionnelle du logging (avec 4 à 6 niveaux de `info`, `warn`, `error`, `debug`, etc.) fait souvent que les développeurs se concentrent sur la mauvaise chose. Cela nous fait nous concentrer sur le format plutôt que sur le but réel de pourquoi nous écrivons des logs.

C'est l'une des raisons pour lesquelles nous enregistrons les erreurs sans réfléchir à deux fois sur la manière de les gérer. C'est aussi pourquoi nous enregistrons à chaque étape de notre code tout en étant ironiquement incapables de déboguer efficacement s'il y a un problème en production.

C'est pourquoi je propose un cadre alternatif pour le logging et, en retour, comment nous pouvons concevoir le logging dans nos systèmes de manière fiable.

## Le Bon, le Mauvais et le Vilain

Ceci est un cadre pour la manière dont je pense que nous devrions stratégiser notre logging. Il comporte trois – et seulement trois – catégories ou préoccupations pour nos logs.

### Première règle du logging : ne pas logger

Le sur-logging est préjudiciable à la productivité de nos équipes et à leur capacité à gérer les opérations habituelles.

Il y a des tonnes de raisons pour lesquelles nous ne devrions pas « logger chaque fois que vous le pouvez » comme le conseillent certains partisans de l'observabilité. Le logging signifie plus de code à maintenir, il entraîne des coûts en termes de performance du système, et plus de logging nous soumet à plus d'audits réglementaires sur la confidentialité des données.

Si vous avez besoin de plus de raisons pour vous abstenir de logger, consultez [cet article de Nikita Sobolev](https://sobolevn.me/2020/03/do-not-log) ou [cet article de Jeff Atwood](https://blog.codinghorror.com/the-problem-with-logging/).

Néanmoins, je ne conseille pas d'éliminer complètement les logs. Je pense que le logging, utilisé correctement, peut nous aider de manière significative à garder nos systèmes en fonctionnement de manière fiable.

Je propose simplement que nous commencions sans logging et que nous identifiions les endroits où nous devons logger, plutôt que de « logger partout car nous pourrions avoir besoin de les consulter ».

Ma règle de base pour ajouter une ligne de logging est : « si nous ne pouvons pas identifier une raison exacte ou un scénario où nous consulterons le log, ne loggez pas ».

Cela dit, comment pouvons-nous introduire en toute sécurité le logging lorsqu'il est absolument nécessaire ? Comment devons-nous structurer nos logs et formater leur contenu ? Quelles informations sont nécessaires à inclure dans les logs ?

### Le Vilain

Ce sont les premiers types de logs que je veux décrire, et ils sont aussi ceux que je trouve le moins fréquemment. (Si nous les trouvons trop souvent, nous pourrions avoir de plus gros problèmes dans nos systèmes !)

« Le Vilain » est le type de log sous des scénarios catastrophiques ou inattendus qui nécessitent une action immédiate (comme des erreurs catastrophiques nécessitant un redémarrage de l'application). Nous pouvons soutenir que, dans ces circonstances, il est plus judicieux d'utiliser des outils d'alerte comme Sentry.

Néanmoins, un log d'erreur peut encore être utile pour nous fournir plus de contexte autour de ces erreurs qui ne sont pas disponibles dans leur trace de pile. Mais ils pourraient aider à reproduire ces erreurs, comme les entrées utilisateur.

Tout comme les erreurs qu'ils accompagnent, ces logs doivent être gardés à un minimum dans notre code et placés en un seul endroit. Ils doivent également être conçus/documentés dans la spécification comme un comportement système requis pour la gestion des erreurs. De plus, ils doivent être intégrés dans le code source autour de l'endroit où la gestion des erreurs se produit.

Bien que le format et le niveau pour les logs « Le Vilain » soient complètement préférentiels sur une base équipe par équipe, je recommanderais d'utiliser `log.error` ou `log.fatal` avant un arrêt et un redémarrage élégants de l'application. Vous devriez également attacher la trace complète de la pile d'erreurs et les données d'entrée de la fonction ou des requêtes pour la reproduction si nécessaire.

### Le Mauvais

« Le Mauvais » est le type de logs qui traite les erreurs attendues et gérées comme les problèmes de réseau et la validation des entrées utilisateur. Ce type de log ne nécessite l'attention des développeurs que s'il y a une anomalie avec eux.

Avec un moniteur configuré pour alerter les développeurs en cas d'erreur, ces logs sont pratiques pour atténuer les problèmes potentiellement graves d'infrastructure ou de sécurité.

Ce type de log doit également être spécifié dans les exigences techniques de gestion des erreurs et peut en fait être regroupé si nous gérons les erreurs attendues et inattendues au même endroit dans le code.

En fonction de la nature de ce qu'ils rendent « visible » pour les développeurs, `log.warn` ou `log.error` peuvent être utilisés pour les logs « Le Mauvais » selon la convention d'une équipe.

### Le Bon

Dernier mais certainement pas le moindre, « Le Bon » est le type de log qui devrait apparaître le plus souvent dans notre code source – mais c'est souvent le plus difficile à bien faire. « Le Bon » type de logs sont ceux associés aux étapes « heureuses » de nos applications, indiquant le succès des opérations.

De par sa nature même d'indiquer les opérations de démarrage/exécution réussies dans notre système, « Le Bon » est souvent mal utilisé par les développeurs qui sont séduits par le mantra « Juste un peu plus de données dans le log, nous pourrions en avoir besoin ».

Encore une fois, je reviendrais à notre toute première règle de logging : « Ne loggez pas à moins que ce soit absolument nécessaire ». Pour prévenir ce type de sur-logging, nous devrions documenter « Le Bon » comme faisant partie de nos exigences techniques complémentaires à la logique métier principale.

En plus de cela, pour chacun des logs « Le Bon » qui sont dans notre spécification technique, ils doivent passer le test de la pierre de touche : y a-t-il des circonstances dans lesquelles nous consulterions le log (que ce soit une demande de support client, une enquête d'un auditeur externe) ? Seulement de cette manière `log.info` ne sera pas un héritage redouté qui obscurcit la vision des développeurs dans nos applications.

### Le Reste (Que Vous Devez Savoir)

À ce stade, je suppose que vous avez remarqué que le thème général de ma stratégie de logging proposée tourne autour de la documentation claire et spécifique de l'objectif du log. Il est important que nous traitons le logging comme faisant partie de nos exigences, et que nous soyons spécifiques sur les mots-clés et les messages que nous voulons taguer dans chaque contexte de log pour qu'ils soient efficacement indexés.

Seulement en faisant cela pouvons-nous être conscients de chaque log que nous produisons, et à notre tour, avoir une vision claire de nos systèmes.

Alors que les logs sont promus au rang de citoyens de première classe avec des exigences techniques concrètes dans nos spécifications, les implications sont qu'ils devraient :

* être maintenus et mis à jour à mesure que les exigences commerciales et techniques évoluent
* être couverts par des tests unitaires et d'intégration

Cela peut sembler beaucoup de travail supplémentaire pour bien faire nos logs. Cependant, je soutiens que c'est le genre d'attention et d'effort que le logging mérite pour être utile.

**Servons nos logs, et nous serons magnifiquement récompensés !**

## Un Guide Pratique de Migration

Je pense qu'il n'y a pas d'utilité pour une nouvelle stratégie de logging (ou toute nouvelle stratégie/cadre d'ailleurs) pour les projets hérités s'il n'y a aucun moyen de les faire passer de leur état désordonné à l'idéal proposé.

J'ai donc un plan général en trois étapes pour quiconque est frustré par les logs de son système et est prêt à investir du temps pour logger plus efficacement.

### Identifier les Suspects Habituels

Puisque l'idée est de réduire les logs inutiles, notre première étape est d'identifier où se cachent les criminels. Avec les puissants éditeurs de texte et IDE que nous avons de nos jours (ou `grep` si vous lisez ceci dans le passé à travers une fenêtre-vers-le-futur), toutes les occurrences de logging peuvent être facilement identifiées.

Un document (ou une feuille de calcul si vous souhaitez être organisé) documentant toutes ces occurrences de logging peut être nécessaire s'il y en a trop.

### Condamnez ces Mauvais Acteurs !

Après avoir identifié tous les suspects, il est temps d'éliminer les mauvaises pommes. Les logs qui sont dupliqués ou inaccessibles sont des fruits à portée de main que nous pouvons immédiatement éliminer de notre code source.

Pour le reste de nos occurrences de logging, il est temps d'impliquer d'autres parties prenantes comme l'ingénieur « inception » qui a commencé le projet (si cela est possible), les chefs de produit, le support client, ou les responsables de la conformité pour répondre à la question : Avons-nous besoin de chacun de ces logs, et si oui, à quoi servent-ils ?

## Lumière au Bout du Tunnel

Maintenant que nous avons une liste restreinte de logs absolument nécessaires, les transformer en exigences techniques avec un objectif documenté pour chacun d'eux est essentiel pour finaliser un contrat (ou nous pouvons l'appeler spécification) pour notre sous-système de logging. Demandez-vous quoi faire lorsqu'un `log.error` se produit, et pour qui nous faisons `log.info` ?

Après cela, ce n'est qu'une question de discipline de la même manière que nous écrivons et maintenons le logiciel en général. Travaillons tous ensemble et rendons le logging génial !

Vous pouvez [me contacter sur Twitter](https://twitter.com/stanley_ngn) pour toute question ou commentaire.