---
title: Comment mettre à l'échelle un système avec le fractionnement de processus et
  Redis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-20T19:26:45.000Z'
originalURL: https://freecodecamp.org/news/scale-system-split-processes
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/photo-1508624217470-5ef0f947d8be.jpeg
tags:
- name: Redis
  slug: redis
- name: scalability
  slug: scalability
seo_title: Comment mettre à l'échelle un système avec le fractionnement de processus
  et Redis
seo_desc: 'By Pramono Winata

  Have you ever gotten into trouble trying to handle a single process that''s really
  huge or heavy? If so, I can help you figure out how to better manage it.

  In this article I will be sharing how I''m currently managing a single message...'
---

Par Pramono Winata

Avez-vous déjà eu des problèmes pour gérer un seul processus qui est vraiment énorme ou lourd ? Si c'est le cas, je peux vous aider à trouver comment mieux le gérer.

Dans cet article, je vais partager comment je gère actuellement un seul message qui est trop volumineux pour être traité par un seul processus. Je l'ai divisé en différents morceaux, ce qui entraîne des processus séparés.

Je n'entrerai pas dans les détails techniques, mais plutôt dans le processus architectural. 
Je discuterai de certains aspects de l'utilisation du cache et de pubsub, mais je n'entrerai pas dans les détails de l'implémentation. Au lieu de cela, je me concentrerai sur le modèle lui-même.

## Le Problème

![Début.](https://images.unsplash.com/photo-1489533119213-66a5cd877091?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDh8fHN0YXJ0fGVufDB8fHx8MTYyNjYzMDgzMQ&ixlib=rb-1.2.1&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@dsmacinnes?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Danielle MacInnes</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Peut-être que la première question qui vous vient à l'esprit est pourquoi devons-nous diviser un seul processus en plusieurs processus simultanés ?

Il peut y avoir plusieurs raisons de le faire. Dans mon cas, cependant, je l'ai fait parce que le message était tout simplement trop volumineux.

Pour vous donner une idée de ma situation, laissez-moi vous briefer un peu avec ce simple diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/sad.png)
_Je ne suis pas un grand créateur de diagrammes, mais cela devrait faire passer le message_

Pour le simplifier avec des mots, imaginez deux services séparés, le service A et le service B, avec un service pubsub au milieu.

Si vous n'êtes pas sûr de ce qu'est un service pubsub, imaginez-le simplement comme un courtier qui aide le message d'un service à atteindre l'autre service.

Le service A publiera alors un message et, via le pubsub, le service B le traitera. Une fois le processus terminé, il effectuera un autre processus pour marquer que le message a été traité.

Assez simple, non ?

C'est juste que dans certains cas, lorsque le message est trop volumineux, il ne parviendra pas à publier le message en raison des limitations du service pubsub. 

D'accord, cela devrait vous donner un aperçu des problèmes que j'ai rencontrés. Alors, comment ai-je résolu ce problème ? Dans la section suivante, je vous expliquerai ma solution.

## Ma Première Approche

![Réfléchir](https://images.unsplash.com/photo-1513348355499-5bdba1597a80?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDg2fHx0aGlua3xlbnwwfHx8fDE2MjY2MzA4OTY&ixlib=rb-1.2.1&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@dose?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Dose Media</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

La première chose qui m'est venue à l'esprit était d'augmenter la taille que le service pubsub peut gérer, ce qui est réalisable avec un simple changement de configuration.

Mais la vie ne serait pas trop intéressante si c'était si facile, non ? Que se passe-t-il si le message ne cesse de grossir ? Devons-nous continuer à augmenter la taille du pubsub ?

Il s'avère que faire cela peut entraîner de nombreux problèmes de scalabilité. Pas bon pour une solution à long terme.

Ensuite, j'ai eu une autre idée qui, je pensais, pourrait résoudre le problème : j'ai divisé ce message en plusieurs messages et j'ai essayé de traiter ces parties séparément.

Maintenant, le système ressemblait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/asda.jpg)
_Mon système/processus mis à jour_

Comme vous pouvez le voir sur le diagramme, le message est divisé en plusieurs messages plus petits. La manière dont il est divisé et quelle partie du message doit être divisée peut différer pour chaque cas et flux. 

Dans mon cas, cependant, mon message contient en fait une liste d'éléments, donc je peux le diviser par chaque élément.

Disons que j'ai 10 éléments. Auparavant, il publiait tous les 10 éléments en un seul message. Mais maintenant, après avoir divisé le message, il transformera ce message en 10 messages.

Cela entraîne un seul processus devenant plusieurs processus ensemble. Une seule publication deviendra 10 publications, ce qui transformera ce seul processus en 10 processus. 

Cela peut ne pas sembler idéal lorsque vous le regardez de cette manière, mais c'est la meilleure solution que j'ai trouvée et elle fonctionne certainement.

Alors, est-ce tout, seulement le diviser ?

Pas vraiment – rappelez-vous cette partie finale où il marque le processus comme terminé ?  
Si c'est le cas, vous vous demandez peut-être pourquoi cette partie est manquante dans mon nouveau diagramme. 

Ne vous inquiétez pas – ce n'est pas que je l'ai oubliée. Je l'ai intentionnellement laissée de côté pour la partie suivante.

Le problème est que lorsque vous divisez le message et le divisez en plusieurs processus, votre système peut ne pas savoir si l'ensemble du processus est réellement terminé. C'est un autre problème majeur que nous devons résoudre, et heureusement, j'ai réussi à trouver une solution pour cela aussi.

## Comment Gérer les Processus de Fin

![Une baleine dans le ciel (Rassemblement d'étourneaux à Otmoor, Royaume-Uni)](https://images.unsplash.com/photo-1516434233442-0c69c369b66d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDF8fHN3YXJtfGVufDB8fHx8MTYyNjYzMDk3Mg&ixlib=rb-1.2.1&q=80&w=2000)
_Photo par [Unsplash](https://unsplash.com/@tumbao1949?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">James Wainscoat</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Alors, comment savoir exactement si le processus est terminé, puisque ces processus se déroulent simultanément ?

La solution que j'ai trouvée consiste à stocker le nombre de processus qui doivent être effectués et à le décrémenter chaque fois qu'un processus se termine. De cette manière, nous pourrons savoir si le dernier processus est terminé.

Cela semble assez simple, tant que nous avons un endroit fiable pour stocker ces données. 
Et en fait, il existe de nombreuses options pour cela. L'une d'entre elles s'appelle [Redis](https://redis.io/), et je l'utilise pour résoudre mon problème ici. 

Si vous n'êtes pas familier avec Redis, c'est un service qui est généralement utilisé comme cache.

Nous gérerons notre mécanisme Redis comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/saddd.png)
_Ajout de Redis pour marquer notre processus_

Le processus est exactement le même qu'avant, mais avec l'ajout de Redis au milieu. Vous devez vous assurer d'avoir un compte initial valide pour ce cas.

Dans mon cas, puisque je publie une liste, je peux facilement mettre la longueur de ma liste comme mon compteur initial. Et pour le compteur, je peux simplement le diminuer d'une unité chaque fois qu'un processus est terminé. Ensuite, je pourrai savoir si j'ai terminé tous mes processus simplement en me référant à mon compteur Redis. S'il a atteint 0, cela signifie que je peux marquer en toute sécurité que tous mes processus sont terminés.

## Conclusion

Pour résumer, j'ai divisé le message en plusieurs messages qui seront traités ensemble dans plusieurs processus. Pour gérer les processus de messages, j'utilise le cache Redis.

La solution que j'ai décrite ci-dessus ne sera pas une solution miracle chaque fois que vous avez un problème de traitement d'un message très volumineux. Il existe d'autres méthodes comme le streaming de votre message, mais ce sera une histoire pour un autre jour.

Merci d'avoir lu mon article jusqu'à la fin ! J'espère sincèrement que vous avez apprécié et trouvé mon article intéressant et, surtout, qu'il a été utile.