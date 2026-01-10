---
title: Pourquoi vous devriez échantillonner les journaux de débogage en production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T12:41:47.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-sample-debug-logs-in-production-39d78ef3968d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hF7dKQVn7EpWn3loQqECYQ.jpeg
tags:
- name: logging
  slug: logging
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi vous devriez échantillonner les journaux de débogage en production
seo_desc: 'By Yan Cui

  It’s com­mon prac­tice to set your log lev­el to warning for pro­duc­tion due to
  traf­fic vol­ume. This is because you have to con­sid­er var­i­ous cost fac­tors:


  Cost of log­ging : Cloud­Watch Logs charges $0.50 per GB ingest­ed. In my e...'
---

Par Yan Cui

Il est courant de régler votre niveau de journalisation à **warning** pour la production en raison du volume de trafic. Cela est dû à divers facteurs de coût :

* **Coût de la journalisation** : _CloudWatch Logs_ facture 0,50 $ par Go ingéré. Selon mon expérience, cela est souvent beaucoup plus élevé que les coûts de facturation Lambda
* **Coût de stockage** : _CloudWatch Logs_ facture 0,03 $ par Go par mois, et sa politique de rétention par défaut est **Jamais Expirer** ! Une pratique courante consiste à envoyer vos journaux à un autre service d'agrégation de journaux et à régler la politique de rétention à X jours. Voir [cet article](https://theburningmonk.com/2017/08/centralised-logging-for-aws-lambda/) pour plus de détails.
* **Coût de traitement** : si vous traitez les journaux avec _Lambda_, vous devez également prendre en compte le coût des facturations _Lambda_.

Mais, faire cela nous laisse sans **aucun** journal de débogage en production. Lorsqu'un problème survient en production, vous n'aurez pas les journaux de débogage pour vous aider à identifier la cause racine.

Au lieu de cela, vous devez perdre un temps précieux à déployer une nouvelle version de votre code pour activer la journalisation de débogage. Sans oublier que vous ne devez pas oublier de désactiver la journalisation de débogage lorsque vous déployez la correction.

Avec les microservices, vous devez souvent faire cela pour plus d'un service afin d'obtenir tous les messages de débogage dont vous avez besoin.

Tout cela **augmente le [temps moyen de récupération](https://en.wikipedia.org/wiki/Mean_time_to_recovery) (MTTR)** pendant un incident. Ce n'est pas ce que nous voulons.

![Image](https://cdn-media-1.freecodecamp.org/images/TV4JL3ABTOYu877SdNZOEje39xCsENsie6uy)

Cela n'a pas à être comme ça.

Il existe un juste milieu entre n'avoir aucun journal de débogage et avoir tous les journaux de débogage. Au lieu de cela, nous devrions échantillonner les journaux de débogage à partir d'un petit pourcentage d'invocations.

![Image](https://cdn-media-1.freecodecamp.org/images/-Sc5WbK9QBaTZ-S65EbI8zrIZGACvvZkAcqB)

J'ai démontré comment faire cela dans le chapitre _Journalisation_ de mon cours vidéo [Production-Ready Serverless](https://bit.ly/production-ready-serverless). Vous avez besoin de deux choses de base :

* un logger qui vous permet de changer le niveau de journalisation dynamiquement, par exemple via des variables d'environnement
* un moteur de middleware tel que [middy](https://github.com/middyjs/middy)

![Image](https://cdn-media-1.freecodecamp.org/images/kqho30Wb7OCBPap3XY2FvBtCSt9nUf-bGN--)

Avec _Lambda_, je n'ai pas besoin de la plupart des fonctionnalités d'un logger complet comme [pino](https://github.com/pinojs/pino). Au lieu de cela, je préfère utiliser un module de journalisation simple comme [celui-ci](https://github.com/theburningmonk/manning-aws-lambda-in-motion/blob/master/lib/log.js). Il est écrit en quelques lignes et me donne les bases :

* [journalisation structurée avec JSON](https://theburningmonk.com/2018/01/you-need-to-use-structured-logging-with-aws-lambda/)
* capacité à journaliser à différents niveaux
* capacité à contrôler le niveau de journalisation dynamiquement via des variables d'environnement

En utilisant _middy_, je peux créer un [middleware](https://github.com/theburningmonk/manning-aws-lambda-in-motion/blob/master/middleware/sample-logging.js) pour mettre à jour dynamiquement le niveau de journalisation à **debug**. Cela le fait pour un pourcentage configurable d'invocations. À la fin de l'invocation, le middleware restaurerait le niveau de journalisation précédent.

![Image](https://cdn-media-1.freecodecamp.org/images/qO1K1e3vzJXADCmbdATAm92TS9epcO-AFkLw)

Vous pourriez remarquer que nous avons également un traitement spécial pour lorsque l'invocation échoue.

![Image](https://cdn-media-1.freecodecamp.org/images/Gn15P9fo3QKW-HVk1Y1baSPgumRjfIhsAOl4)

Cela est pour s'assurer que nous capturons l'erreur avec autant de contexte que possible, y compris :

* l'ID de requête AWS unique
* l'événement d'invocation, afin que nous puissions [rejouer l'événement d'invocation localement](https://theburningmonk.com/2017/08/running-and-debugging-aws-lambda-functions-locally-with-the-serverless-framework-and-vs-code/) et déboguer le problème
* le message d'erreur et la trace de la pile

Avoir des journaux de débogage pour un petit pourcentage d'invocations est génial. Mais lorsque vous traitez avec des microservices, vous devez vous assurer que vos journaux de débogage couvrent une chaîne d'appels complète.

C'est la seule façon de rassembler une image complète de tout ce qui s'est passé sur cette chaîne d'appels. Sinon, vous vous retrouverez avec des fragments de journaux de débogage de nombreuses chaînes d'appels mais jamais l'image complète d'une seule.

Vous pouvez faire cela en transmettant la décision d'activer la journalisation de débogage en tant qu'ID de corrélation. La fonction suivante dans la chaîne respectera cette décision et la transmettra. Voir [cet article](https://theburningmonk.com/2017/09/capture-and-forward-correlation-ids-through-different-lambda-event-sources/) pour plus de détails.

![Image](https://cdn-media-1.freecodecamp.org/images/FeWU7Hr6-zviBenJKyVZvNUp8GWlgyV1lVH5)

C'est tout, un autre conseil professionnel sur la façon de construire l'observabilité dans votre application serverless. Si vous souhaitez en savoir plus sur la façon de vous lancer complètement dans le serverless, consultez mon guide en 10 étapes [ici](https://blog.binaris.com/how-to-go-all-in-with-serverless-adoption/).

À la prochaine !