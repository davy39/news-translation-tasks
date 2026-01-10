---
title: Comment choisir la meilleure source d'événements pour la messagerie pub/sub
  avec AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T21:38:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-best-event-source-for-pub-sub-messaging-with-aws-lambda-31ca4db9be69
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dEUcN2mmJXDmiwb8.png
tags:
- name: AWS
  slug: aws
- name: messaging
  slug: messaging
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment choisir la meilleure source d'événements pour la messagerie pub/sub
  avec AWS Lambda
seo_desc: 'By Yan Cui

  AWS offers a wealth of options for imple­ment­ing mes­sag­ing pat­terns such as
  Publish/Subscribe (often short­ened to pub/sub) with AWS Lamb­da. In this article,
  we’ll com­pare and con­trast some of these options.

  The pub/sub pattern

  Pub/...'
---

Par Yan Cui

AWS offre une multitude d'options pour implémenter des modèles de messagerie tels que `Publish/Subscribe` (souvent abrégé en pub/sub) avec AWS Lambda. Dans cet article, nous allons comparer et contraster certaines de ces options.

### Le modèle pub/sub

Pub/Sub est un modèle de messagerie où les éditeurs et les abonnés sont découplés par l'intermédiaire d'un courtier de messages (ZeroMQ, RabbitMQ, SNS, etc.).

![Image](https://cdn-media-1.freecodecamp.org/images/aMYeJtlvg8qD1aw7GWlpLcrptCADpvXiGRlt)
_Source : [Publish Subscribe Pattern (Wikipedia)](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/in-2N2y0wjCxQdEAMjGcplRv7yUWRfMvewOr)

Dans l'écosystème AWS, le candidat évident pour le rôle de courtier est Simple Notification Service (SNS).

SNS effectuera trois tentatives pour que votre fonction Lambda traite un message avant de l'envoyer à une file d'attente de lettres mortes (DLQ) si une DLQ est spécifiée pour la fonction. Cependant, selon une [analyse](https://engineering.opsgenie.com/aws-lambda-performance-series-part-2-an-analysis-on-async-lambda-fail-retry-behaviour-and-dead-b84620af406) des gens chez OpsGenie, le nombre de nouvelles tentatives peut atteindre six.

Une autre chose à considérer est le degré de parallélisme que cette configuration offre. Pour chaque message, SNS créera une nouvelle invocation de votre fonction. Ainsi, si vous publiez 100 messages sur SNS, vous pouvez avoir 100 exécutions simultanées de la fonction Lambda abonnée.

**C'est génial si vous optimisez pour le débit.**

![Image](https://cdn-media-1.freecodecamp.org/images/lKqW9l3keN4ybs4AHSxxJSu76E22YUADwgWE)

Cependant, nous sommes souvent **contraints** par le débit maximal que nos dépendances en aval peuvent gérer — bases de données, S3, services internes/externes, etc.

Si le pic de débit est court, il y a de bonnes chances que les nouvelles tentatives soient suffisantes (il y a un délai aléatoire et exponentiel entre les nouvelles tentatives) et vous ne manquerez aucun message.

![Image](https://cdn-media-1.freecodecamp.org/images/aUrhbLV0y5hatCjtR-kpZuvzi6eQZBmM9Gtz)
_Les messages erronés sont réessayés 2 fois avec un délai exponentiel. Si le pic est de courte durée, la nouvelle tentative est susceptible de réussir, ce qui ne entraîne aucune perte de message._

Si le pic de débit est soutenu sur une longue période, vous pouvez épuiserez le nombre maximal de nouvelles tentatives. À ce stade, vous devrez vous fier à la DLQ et éventuellement à une intervention humaine pour récupérer les messages qui n'ont pas pu être traités la première fois.

![Image](https://cdn-media-1.freecodecamp.org/images/2uzNYBIHpLiAdHSsZBRl9aLIXXbKM5mQ5LBG)
_Les messages erronés sont réessayés 2 fois avec un délai exponentiel. Mais le pic du taux de messages chevauche les nouvelles tentatives, aggravant davantage le problème et épuisant finalement le nombre maximal de nouvelles tentatives, les messages erronés devant être livrés à la DLQ à la place (si une est spécifiée)._

De même, si la dépendance en aval subit une panne, tous les messages reçus et réessayés pendant la panne sont voués à échouer.

![Image](https://cdn-media-1.freecodecamp.org/images/PFbSpQtb0Nxx2RREF9VATvUBjJxR5lxu0WD5)
_Tout message reçu ou réessayé pendant la panne en aval échouera et sera envoyé à la DLQ._

Vous pouvez également rencontrer la [limite Lambda](http://docs.aws.amazon.com/lambda/latest/dg/limits.html) sur le nombre d'exécutions simultanées dans une région. Comme il s'agit d'une limite au niveau du compte, elle affectera également vos autres systèmes au sein du compte qui dépendent d'AWS Lambda : API, traitement d'événements, tâches cron, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/MdSMzBdPAvsgSkw47bXD2Dj8qlB4K9y0v5fd)

SNS est également sujet à des problèmes temporaires, comme des pics de trafic, des pannes en aval, etc. Kinesis, en revanche, gère ces problèmes beaucoup mieux comme décrit ci-dessous :

* Le degré de parallélisme est contraint par le nombre de shards, qui peut être utilisé pour amortir les pics dans le taux de messages

![Image](https://cdn-media-1.freecodecamp.org/images/MvIaF-A3FjeFNn5GSzSRzJ3vD-fcdF5kZv9q)
_Les pics dans le taux de messages sont amortis, car le débit maximal est déterminé par le nombre de shards * taille maximale du lot * 5 lectures par seconde. Ce qui vous donne deux leviers pour ajuster le débit maximal._

* Les enregistrements sont réessayés jusqu'à ce que le succès soit atteint, sauf si la panne dure plus longtemps que la politique de rétention que vous avez sur le flux (la valeur par défaut est de 24 heures). Vous pourrez éventuellement traiter les enregistrements

![Image](https://cdn-media-1.freecodecamp.org/images/v8c03ATaEUayJurzgbxbPSWtqG-rebS7v40U)
_L'impact d'une panne en aval est absorbé par la politique d'invocation de réessayer jusqu'à succès._

Mais Kinesis Streams n'est pas sans ses propres problèmes. En fait, d'après mon expérience d'utilisation de Kinesis Streams avec Lambda, j'ai trouvé un certain nombre de mises en garde qui doivent être comprises afin de faire un usage efficace du service.

Vous pouvez lire à propos de ces mises en garde dans un autre article que j'ai écrit [ici](https://read.acloud.guru/aws-lambda-3-pro-tips-for-working-with-kinesis-streams-8f6182a03113).

Intéressamment, Kinesis Streams n'est pas la seule option de streaming disponible sur AWS. Il y a aussi DynamoDB Streams.

![Image](https://cdn-media-1.freecodecamp.org/images/ZVV6125FoRnsc-WWr5xDeiQdYMgdJgbxZFbn)
_DynamoDB Streams peut être utilisé comme un remplacement équivalent pour Kinesis Streams._

Dans l'ensemble, DynamoDB Streams + Lambda fonctionne de la même manière que Kinesis Streams + Lambda. De plus, il présente quelques particularités intéressantes :

* DynamoDB Streams ajuste automatiquement le nombre de shards
* Si vous traitez DynamoDB Streams avec AWS Lambda, vous ne payez pas pour les lectures depuis DynamoDB Streams (mais vous payez toujours pour les unités de capacité de lecture et d'écriture pour la table DynamoDB elle-même)

![Image](https://cdn-media-1.freecodecamp.org/images/elMIs2s1bvzsS3t1s6lck8kKjUQtoN16p2d6)
_Source : [Tarification DynamoDB](https://aws.amazon.com/dynamodb/pricing/" rel="noopener" target="_blank" title=")_

* Kinesis Streams offre l'option d'étendre la rétention des données à 7 jours, mais DynamoDB Streams n'offre pas une telle option

![Image](https://cdn-media-1.freecodecamp.org/images/ZfHR49h8Odv-6oORBUdbEoulWBpkeTobaFSV)
_Source : [Travailler avec DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html" rel="noopener" target="_blank" title=")_

Le fait que DynamoDB Streams ajuste automatiquement le nombre de shards peut être une arme à double tranchant. D'une part, il élimine le besoin pour vous de gérer et de mettre à l'échelle le flux (ou de concevoir des solutions maison de [mise à l'échelle automatique](https://read.acloud.guru/auto-scaling-kinesis-streams-with-aws-lambda-299f9a0512da)). Mais d'autre part, cela peut également diminuer la capacité à amortir les pics de charge que vous transmettez aux systèmes en aval.

Pour autant que je sache, il n'y a aucun moyen de limiter le nombre de shards auxquels un flux DynamoDB peut être mis à l'échelle, ce qui est certainement quelque chose à considérer lors de la mise en œuvre de votre propre solution de mise à l'échelle automatique.

Je pense que la question la plus pertinente est : « quelle est votre source de vérité ? »

Un enregistrement écrit dans DynamoDB le rend-il canonique pour l'état de votre système ? C'est certainement le cas dans la plupart des systèmes N-tiers qui sont construits autour d'une base de données, qu'il s'agisse d'une base de données RDBMS ou NoSQL.

Dans un système basé sur des événements où l'état est modélisé comme une séquence d'événements (par opposition à un instantané), la source de vérité pourrait bien être le flux Kinesis. Par exemple, dès qu'un événement est écrit dans le flux, il est considéré comme canonique pour l'état du système.

Ensuite, il y a d'autres considérations autour des coûts, de la mise à l'échelle automatique, etc.

D'un point de vue développement, les flux DynamoDB ont également certaines limitations et lacunes :

* Chaque flux est limité aux événements d'une seule table
* Les enregistrements décrivent les événements DynamoDB et non les événements de votre domaine, ce qui, à mon avis, crée un sentiment de dissonance lorsque l'on travaille avec ces événements

En excluant le coût des invocations Lambda pour le traitement des messages, voici quelques projections de coûts pour l'utilisation de SNS vs Kinesis Streams vs DynamoDB Streams en tant que courtier. Je fais l'hypothèse que le débit est constant et que chaque message fait 1 Ko.

**Coût mensuel à 1 msg/s**

![Image](https://cdn-media-1.freecodecamp.org/images/yyuEQdQUtDXmaG-3FeSvBuM3Y1quo52SkIQY)

**Coût mensuel à 1 000 msg/s**

![Image](https://cdn-media-1.freecodecamp.org/images/11RcJ9KEIfnJbOCXvUz8g2J2AR6K5lKuGsNX)

**Ces projections ne doivent pas être prises au pied de la lettre.** Pour commencer, l'hypothèse d'un débit parfaitement constant et d'une taille de message est irréaliste, et vous aurez besoin d'une certaine marge avec Kinesis et les flux DynamoDB même si vous ne rencontrez pas les limites de throttling.

Cela dit, ce que ces projections me disent, c'est que :

1. Vous obtenez beaucoup avec chaque shard dans les flux Kinesis
2. Bien qu'il y ait un coût de base pour l'utilisation des flux Kinesis, le coût diminue lorsque l'utilisation augmente par rapport à SNS et aux flux DynamoDB, grâce au coût significativement plus bas par million de requêtes

Bien que SNS, Kinesis et les flux DynamoDB soient vos choix de base pour le courtier, les fonctions Lambda peuvent également agir en tant que courtiers à part entière et propager des événements vers d'autres services.

C'est l'approche utilisée par le projet [aws-lambda-fanout](https://github.com/awslabs/aws-lambda-fanout) d'awslabs. Il vous permet de propager des événements depuis Kinesis et les flux DynamoDB vers d'autres services qui ne peuvent pas s'abonner directement aux trois choix de base de courtiers (soit en raison de limitations de compte/région, soit parce qu'ils ne sont tout simplement pas supportés).

![Image](https://cdn-media-1.freecodecamp.org/images/arPDE4lmFHJ-GPKb3u-366nUFaDeaZxiyZp8)
_Le projet aws-lambda-fanout d'awslabs propage des événements depuis Kinesis et les flux DynamoDB vers d'autres services à travers plusieurs comptes et régions._

Bien que ce soit une bonne idée et qu'elle réponde définitivement à certains besoins spécifiques, il est important de garder à l'esprit les complexités supplémentaires qu'elle introduit, telles que la gestion des échecs partiels, la gestion des pannes en aval, les mauvaises configurations, etc.

### Conclusion

Alors, quelle est la meilleure source d'événements pour faire du pub-sub avec AWS Lambda ? Comme la plupart des décisions techniques, cela dépend du **problème** que vous essayez de résoudre et des **contraintes** avec lesquelles vous travaillez.

Dans cet article, nous avons examiné SNS, Kinesis Streams et DynamoDB Streams comme candidats pour le rôle de courtier. Nous avons passé en revue un certain nombre de scénarios pour voir comment le choix de la source d'événements affecte l'évolutivité, le parallélisme et la résilience face aux problèmes temporaires et aux coûts.

Vous devriez maintenant avoir une bien meilleure compréhension des compromis entre les différentes sources d'événements lors de l'utilisation de Lambda.

À la prochaine !