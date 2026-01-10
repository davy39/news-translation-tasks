---
title: Je crains que vous ne pensiez pas correctement aux cold starts d'AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T09:30:29.000Z'
originalURL: https://freecodecamp.org/news/im-afraid-you-re-thinking-about-aws-lambda-cold-starts-all-wrong-45078231fe7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JMd9a_VwVAA8pRSLChu3gQ.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: Je crains que vous ne pensiez pas correctement aux cold starts d'AWS Lambda
seo_desc: 'By Yan Cui

  When I dis­cuss AWS Lamb­da cold starts with folks in the con­text of API Gate­way,
  I often get respons­es along the line of:


  Meh, it’s only the first request right? So what if one request is slow, the next
  mil­lion requests would be fast...'
---

Par Yan Cui

Lorsque je discute des cold starts d'AWS Lambda avec des personnes dans le contexte d'API Gateway, j'obtiens souvent des réponses du genre :

> Bof, ce n'est que la première requête, non ? Alors quoi si une requête est lente, les millions suivantes seront rapides.

Malheureusement, c'est une simplification excessive de ce qui se passe.

Un cold start se produit **une fois** pour chaque **exécution concurrente** de votre fonction.

API Gateway réutilise les exécutions concurrentes de votre fonction si possible. D'après mes observations, il **peut même** mettre en file d'attente les requêtes pendant un court moment dans l'espoir qu'une des exécutions concurrentes se termine et devienne réutilisable.

Si les requêtes des utilisateurs arrivent les unes après les autres, alors vous ne subirez qu'un seul cold start dans le processus. Vous pouvez simuler cela en utilisant [Charles proxy](https://www.charlesproxy.com/) en répétant une requête capturée avec un paramètre de concurrence réglé sur 1.

![Image](https://cdn-media-1.freecodecamp.org/images/uh1CpqN69lXmbg8-5a5iiPdt7ylXQz37mQks)

Comme vous pouvez le voir sur la chronologie ci-dessous, seule la première requête a subi un cold start. La réponse à cette requête était beaucoup plus lente que les autres.

1 sur 100 — c'est supportable. En fait, cela n'apparaîtra même pas dans ma métrique de latence du 99e percentile.

![Image](https://cdn-media-1.freecodecamp.org/images/LXCAeq5zIW9SIMwX5onEKXBY7AKkYbT4GoYB)

Et si les requêtes des utilisateurs arrivaient en masse ? Après tout, les comportements des utilisateurs sont imprévisibles et peu susceptibles de suivre le motif séquentiel que nous voyons ci-dessus. Alors simulons ce qui se passe lorsque nous recevons 100 requêtes avec une concurrence de 10.

![Image](https://cdn-media-1.freecodecamp.org/images/6HkV4EEduReCYILMg7mT8ISRBK-QmqZSjcdp)

![Image](https://cdn-media-1.freecodecamp.org/images/j7l6PzmEfzlKSfepxZttY8GvSImfaRfS17ix)

Maintenant, les choses ne semblent plus aussi roses — les 10 premières requêtes étaient toutes des cold starts ! Cela pose problème si votre trafic est irrégulier à des moments spécifiques de la journée ou lors d'événements spécifiques, par exemple :

* Les services de commande de nourriture (comme JustEat et Deliveroo) ont des pics de trafic aux heures des repas
* Les sites de commerce électronique ont des pics de trafic très concentrés lors des jours de shopping populaires de l'année — comme le Cyber Monday et le Black Friday
* Les services de paris ont des pics de trafic lors des événements sportifs
* Les réseaux sociaux ont des pics de trafic lors d'événements notables dans le monde

Pour ces services, les pics soudains de trafic signifient qu'API Gateway ajoutera plus d'exécutions concurrentes de votre fonction Lambda. Cela équivaut à des rafales de cold starts, et ce n'est pas une bonne nouvelle pour vous.

Ce sont également les périodes les plus cruciales pour votre entreprise, lorsque vous voulez que votre service soit à son meilleur comportement.

![Image](https://cdn-media-1.freecodecamp.org/images/WCGWkW58PVn3dwqF9JEhWolUGoi9St-u8YuY)

Si les pics sont prévisibles, vous pouvez atténuer l'effet des cold starts en préchauffant votre API.

Par exemple, dans le cas d'un service de commande de nourriture, vous savez qu'il y aura un pic de trafic à midi. Vous pouvez planifier une tâche cron en utilisant un événement planifié CloudWatch à 11h58 pour déclencher une fonction Lambda. Cette fonction générera une rafale de requêtes concurrentes pour forcer API Gateway à créer le nombre souhaité d'exécutions concurrentes à l'avance.

Vous pouvez utiliser les en-têtes HTTP pour taguer ces requêtes. La fonction de traitement peut alors les distinguer des requêtes normales des utilisateurs et les court-circuiter.

![Image](https://cdn-media-1.freecodecamp.org/images/11OPD33TBj4y9soH958GXVsYd4OhRNktSAjG)

**Cela ne trahit-il pas l'éthique du serverless computing selon laquelle vous ne devriez pas avoir à vous soucier de la mise à l'échelle ?**

Oui, c'est le cas, mais **rendre les utilisateurs heureux prime sur tout le reste**. Vos utilisateurs ne sont pas contents d'attendre que votre fonction démarre à froid pour pouvoir commander leur nourriture. Le coût de passage à un concurrent est si faible de nos jours, qu'est-ce qui les empêche de vous quitter ?

Vous pourriez également envisager de réduire l'impact des cold starts en réduisant leur durée :

* Écrivez vos fonctions Lambda dans un [langage qui n'entraîne pas un temps de cold start élevé](https://read.acloud.guru/does-coding-language-memory-or-package-size-affect-cold-starts-of-aws-lambda-a15e26d12c76) — c'est-à-dire Node.js, Python, ou [Go](https://aws.amazon.com/blogs/compute/announcing-go-support-for-aws-lambda/)
* Utilisez des paramètres de mémoire plus élevés pour les fonctions sur le chemin critique, y compris les APIs intermédiaires
* Optimisez les dépendances et la taille du package de votre fonction
* **Évitez les VPCs autant que possible !** Lambda crée des ENI (interfaces réseau élastiques) vers le VPC cible, ce qui peut ajouter jusqu'à 10s (oui, vous avez bien lu) à votre cold start

Il y a aussi deux autres facteurs à considérer :

* [Les exécutions inactives depuis un certain temps seront garbage collectées](https://read.acloud.guru/how-long-does-aws-lambda-keep-your-idle-functions-around-before-a-cold-start-bf715d3b810)
* Les exécutions qui ont été actives depuis un certain temps (entre 4 et 7 heures) seront également garbage collectées

Qu'en est-il des APIs rarement utilisées ? Dans ce cas, chaque invocation peut être un cold start si trop de temps s'écoule entre les invocations. Pour vos utilisateurs, ces APIs sont toujours lentes, donc elles sont moins utilisées, et cela devient un cercle vicieux.

Pour celles-ci, vous pouvez utiliser une tâche cron (c'est-à-dire un événement planifié CloudWatch avec une fonction Lambda comme cible) pour les maintenir actives. La tâche cron s'exécuterait toutes les 5 à 10 minutes et enverrait une requête spéciale à l'API. En maintenant ces APIs actives, vos utilisateurs n'auront pas à subir de cold starts.

![Image](https://cdn-media-1.freecodecamp.org/images/LGDH5Jx1YQ9H8Dqu4l4tEZXcz4kZoVMGNLn6)

Cette approche est moins efficace pour les fonctions occupées avec de nombreuses exécutions concurrentes. Le message ping n'atteindra qu'une des exécutions concurrentes, et il n'y a aucun moyen de le diriger vers des exécutions spécifiques. En fait, il n'y a aucun moyen fiable de connaître le nombre exact d'exécutions concurrentes pour une fonction.

De plus, si le nombre de requêtes concurrentes des utilisateurs diminue, il est dans votre intérêt de laisser les exécutions inactives être garbage collectées. Après tout, vous ne voudriez pas payer pour des ressources inutiles dont vous n'avez pas besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/tOP0ZmnqijAtz-rstaBmg7kgdWsWp16U1Ch3)

Cet article n'est pas destiné à être votre guide unique pour les cold starts d'AWS Lambda. Il est destiné à illustrer que parler des cold starts est une discussion plus nuancée que "la première requête".

Les cold starts sont une caractéristique de la plateforme avec laquelle nous devons vivre. Et nous aimons la plateforme AWS Lambda et voulons l'utiliser, car elle livre sur tant de fronts. Néanmoins, il est important de ne pas laisser nos propres préférences nous aveugler sur ce qui est important. **Garder nos utilisateurs heureux et construire un produit qu'ils aiment** est toujours l'objectif le plus important.

À cette fin, vous devez connaître la plateforme sur laquelle vous construisez. Avec le coût de l'expérimentation étant si faible, il n'y a aucune raison de ne pas expérimenter avec AWS Lambda vous-même. Essayez d'en apprendre davantage sur son comportement et sur la manière dont vous pouvez en tirer le meilleur parti.