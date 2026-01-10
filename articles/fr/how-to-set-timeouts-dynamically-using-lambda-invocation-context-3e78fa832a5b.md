---
title: Comment définir des timeouts de manière dynamique en utilisant le contexte
  d'invocation Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-08T08:30:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-timeouts-dynamically-using-lambda-invocation-context-3e78fa832a5b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XKE_zsrkxUG3yf5qkbGPzA.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment définir des timeouts de manière dynamique en utilisant le contexte
  d'invocation Lambda
seo_desc: 'By Yan Cui

  With API Gate­way and Lamb­da, you’re forced to use short time­outs on the serv­er-side:


  API Gate­way has a 29s max time­out on all inte­gra­tion points

  The Server­less frame­work uses a default of 6s for AWS Lamb­da func­tions


  How­ev­er...'
---

Par Yan Cui

Avec API Gateway et Lambda, vous êtes obligé d'utiliser des timeouts courts côté serveur :

* **API Gateway a un timeout maximum de 29s** sur tous les points d'intégration
* Le framework [Serverless](https://serverless.com/framework/) utilise un timeout par défaut de **6s** pour les fonctions AWS Lambda

Cependant, vous avez une influence limitée sur le temps de démarrage à froid d'une fonction Lambda. Et vous n'avez aucun contrôle sur la quantité de surcharge ajoutée par API Gateway. Ainsi, la latence réelle que vous pourriez attendre d'une fonction appelante est bien moins prévisible que vous pourriez le penser.

![Image](https://cdn-media-1.freecodecamp.org/images/WhmOKbUJElluVZAAQUgnFi6N2vUIiQcXZgwo)

![Image](https://cdn-media-1.freecodecamp.org/images/WR1ntsEd4TwiicN1wDWWAuUAEokbPNZFeuIu)
_[https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/api-gateway-metrics-dimensions.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/api-gateway-metrics-dimensions.html" rel="noopener" target="_blank" title=")_

Nous ne voulons pas qu'une réponse HTTP lente provoque un timeout de la fonction appelante. Cela a un impact négatif sur l'expérience utilisateur. Au lieu de cela, nous devrions arrêter d'attendre une réponse avant que la fonction appelante ne dépasse le timeout.

> « L'objectif de la stratégie de timeout est de donner aux requêtes HTTP la **meilleure chance de réussir**, à condition que cela ne provoque pas d'erreur de la fonction appelante elle-même. »

> - Moi

La plupart du temps, je vois les gens utiliser des valeurs de timeout fixes, mais il est souvent difficile de décider :

* Trop court, et vous ne donnerez pas à la requête la meilleure chance de réussir. Par exemple, il reste 5s dans l'invocation, mais le timeout est défini à 3s.
* Trop long, et vous risquez de laisser la requête provoquer un timeout de la fonction appelante. Par exemple, il reste 5s dans l'invocation, mais le timeout est défini à 6s.

Les choses sont encore compliquées par le fait que nous effectuons souvent plus d'une requête HTTP pendant une invocation de fonction. Par exemple,

1. _lecture depuis DynamoDB_
2. exécution de la logique métier sur les données
3. _sauvegarde de la mise à jour dans DynamoDB_
4. _publication d'un événement vers Kinesis_

Examinons deux approches courantes pour choisir les valeurs de timeout et leurs limites.

![Image](https://cdn-media-1.freecodecamp.org/images/h2OAW3TBhEJGGYIwdZUhXZMIinuP8kLhvtzA)
_les requêtes n'ont pas la meilleure chance de réussir_

![Image](https://cdn-media-1.freecodecamp.org/images/gOowm9GXISJ1H-jb-wutX6ocGILgytVHD0xl)
_les requêtes sont autorisées à s'exécuter trop longtemps et provoquent le timeout de la fonction._

Au lieu de suivre ces approches, je propose que nous devrions **définir le timeout de la requête en fonction du temps d'invocation restant**. Nous devrions également réserver un peu de temps pour effectuer des **étapes de récupération** en cas d'échecs.

Vous pouvez savoir combien de temps il reste dans l'invocation actuelle via l'objet `context`.

![Image](https://cdn-media-1.freecodecamp.org/images/D7EMF5dKAZdN8yTbch2tm0nBKSFjB9SCSrfg)
_[https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html" rel="noopener" target="_blank" title=")_

Par exemple, si le `timeout` d'une fonction est de 6s et que nous sommes à 1s dans l'invocation. Si nous réservons 500ms pour la récupération, il nous reste alors 4,5s pour attendre une réponse HTTP.

Avec cette approche, nous obtenons le meilleur des deux mondes :

* Permettre aux requêtes la meilleure chance de réussir en fonction du temps d'invocation réel restant

![Image](https://cdn-media-1.freecodecamp.org/images/e7OC4y4Hoe7MhYCARqwejIPGpU4Y5upJXOll)
_les requêtes ont la meilleure chance de réussir, sans être limitées par un timeout déterminé de manière arbitraire._

* Empêcher les réponses lentes de provoquer un timeout de la fonction, ce qui nous donne une fenêtre d'opportunité pour effectuer des actions de récupération.

![Image](https://cdn-media-1.freecodecamp.org/images/FmnGFJFXltV07ajBvuXihhZ42zaOGW44G-Mo)
_les réponses lentes sont interrompues avant qu'elles ne provoquent le timeout de la fonction appelante_

Mais que allez-vous faire après avoir interrompu ces requêtes ? N'allez-vous pas devoir répondre avec une erreur HTTP, puisque vous n'avez pas pu terminer les opérations nécessaires ?

Au minimum, les actions de récupération doivent inclure :

* Journaliser l'incident de timeout avec autant de contexte que possible. Par exemple, cible de la requête, valeur de timeout, [ID de corrélation](https://theburningmonk.com/2017/09/capture-and-forward-correlation-ids-through-different-lambda-event-sources/), et l'objet de la requête.
* Suivre des métriques personnalisées pour `serviceX.timedout` afin qu'elles puissent être surveillées et que l'équipe puisse être alertée si la situation s'aggrave
* Retourner un code d'erreur d'application et l'ID de la requête originale dans le corps de la réponse. L'application cliente peut alors afficher un message convivial comme « Oups, il semble que cette fonctionnalité est actuellement indisponible, veuillez réessayer plus tard. Si c'est urgent, veuillez nous contacter à xxx@domain.com et mentionner l'ID de la requête f19a7dca. Merci pour votre coopération :-)

```
{   "errorCode": 10021,   "requestId": "f19a7dca",   "message": "service X timed out" }
```

Dans certains cas, vous pouvez également récupérer de manière encore plus élégante en utilisant des solutions de repli.

La bibliothèque [Hystrix](https://github.com/Netflix/Hystrix) de Netflix prend en charge plusieurs types de solutions de repli via le modèle de commande qu'elle utilise largement. Je recommande de lire sa [page wiki](https://github.com/Netflix/Hystrix/wiki/How-To-Use), car il y a beaucoup d'informations et d'idées utiles.

![Image](https://cdn-media-1.freecodecamp.org/images/d7dnsp1JyZBHfqvZaPzRgaRSM-Xz2lKIPUMN)

Chaque commande Hystrix vous permet de spécifier une action de repli.

![Image](https://cdn-media-1.freecodecamp.org/images/zYiuzrRGym4ZIHPv9Nu6idnxTlHRY8FIF2cR)

Vous pouvez également enchaîner les solutions de repli ensemble en enchaînant les commandes via leurs méthodes `getFallback` respectives.

![Image](https://cdn-media-1.freecodecamp.org/images/lSERDe6Z69uzepFiE3jkQvCS8z2K-JgTrZzs)

Par exemple,

1. exécuter une lecture DynamoDB dans `CommandA`
2. Dans la méthode `getFallback`, exécuter `CommandB` qui retournerait une réponse mise en cache précédemment si disponible
3. Si aucune réponse mise en cache n'est disponible, alors `CommandB` échoue et déclenche sa propre méthode `getFallback`
4. Exécuter `CommandC`, qui retourne une réponse simulée

Vous devriez consulter Hystrix si vous ne l'avez pas déjà fait. La plupart des modèles intégrés à Hystrix peuvent être facilement adoptés dans nos applications serverless pour les rendre plus résistantes aux pannes.