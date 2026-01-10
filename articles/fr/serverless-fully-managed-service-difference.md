---
title: 'Serverless vs Services entièrement gérés : Quelle est la différence ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-03T16:51:37.000Z'
originalURL: https://freecodecamp.org/news/serverless-fully-managed-service-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cloud-pic.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: 'Serverless vs Services entièrement gérés : Quelle est la différence ?'
seo_desc: 'By Periklis Gkolias

  If you''re new to cloud technologies, you might be confused about the difference
  between serverless technologies and managed services.

  So in this article you''ll learn what these terms mean and what the main differences
  are.


  What A...'
---

Par Periklis Gkolias

Si vous êtes nouveau dans les technologies cloud, vous pourriez être confus quant à la différence entre les technologies serverless et les services gérés.

Alors dans cet article, vous apprendrez ce que signifient ces termes et quelles sont les principales différences.

![Clouds. Crédits à Zbynek Burival](https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80)


## Qu'est-ce que les Services Gérés ?

Un service géré permet à l'utilisateur final de se concentrer sur l'*utilisation* d'un service plutôt que sur sa *configuration*.

Cela ne signifie pas que le fournisseur cloud peut lire vos pensées. Plutôt, toute entrée requise par le service se fait via un formulaire convivial.

Les services gérés entrent dans la catégorie des produits PaaS (Platform as a Service).

L'un des services gérés les plus célèbres est [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) d'Amazon. Dans Elastic Beanstalk, vous pouvez :

a) configurer certains paramètres
b) fournir une image Docker

et le service configurera le reste pour vous. Il gérera des choses comme :

- Machines virtuelles
- Un serveur web (si nécessaire)
- Exposition de votre application au public
- Infrastructure de surveillance et de journalisation
- Configuration semi-automatisée
- Équilibrage de charge
- Mise à l'échelle

Et plus encore.

Vous pourrez voir les résultats de l'opération Elastic Beanstalk, par exemple les machines virtuelles qui ont été démarrées. 

Généralement, vous ne pourrez pas y accéder et les manipuler. Sinon, ce n'est pas un service géré – vous êtes le gestionnaire.

![AWS ElasticBeanStalk](https://cdn-images-1.medium.com/fit/t/1600/480/1*Fd6rk1k1FHPZcg4aK_OXtQ.png)

Ainsi, un service géré est essentiellement une abstraction d'un... service non géré. L'abstraction est généralement interfacée via des formulaires web. Et dans un service géré, en tant qu'utilisateur, vous ne vous souciez pas des mises à jour, des correctifs, etc.

C'est parce que vous n'avez pas accès aux machines. Quelqu'un doit faire le travail. Généralement, vous n'avez que des choix limités, si choix il y a, sur le système sous-jacent. Cela peut être le système d'exploitation ou la version du logiciel utilisé.

Assez simple, n'est-ce pas ? Passons au serverless, qui est un peu plus complexe.

## Que signifie Serverless ?

Avec le terme serverless, nous faisons référence à un modèle de calcul différent, distinct du modèle "traditionnel" orienté serveur.

Dans le calcul orienté serveur (ou serverfull si vous préférez des mots plus sophistiqués), nous utilisons des machines virtuelles ou physiques pour configurer et exécuter notre application.

Des qualités comme la disponibilité et la performance de vos applications sont fortement liées à la santé de vos machines.

Nous avons perfectionné les solutions de clusterisation au fil du temps (et d'autres outils) pour rendre le déclin de la santé des machines de moins en moins important.

Qu'en est-il du coût, cependant ? Pourquoi payons-nous encore pour des serveurs inactifs ou sous-utilisés (soit en argent, soit en cycles CPU perdus) ? Si nous devons mettre à l'échelle un cluster de machines, pourquoi cela prend-il du temps ?

Voici le serverless. Le serverless entre dans la catégorie des produits FaaS (Function as a Service).

Le nom est un peu trompeur, cependant – le serveur sur lequel le code s'exécute existe bel et bien.

Vous n'avez simplement pas besoin de vous en soucier, tout comme dans les services gérés. Le serverless va un peu plus loin, cependant – votre application s'exécute lorsque vous en avez besoin, et seulement aussi longtemps qu'elle le devrait. Il n'y a pas de temps d'inactivité.

Vous ne verrez jamais le serveur dans votre tableau de bord de machine virtuelle et, bien sûr, vous ne connaîtrez aucun détail sur le serveur.

Les implémentations serverless sont généralement basées sur des événements. Les instances sont inactives sauf si un événement se produit.

> Une chose à noter : il peut y avoir un cas où vous avez instructé vos serveurs à ne pas être inactifs, ce qui est connu sous le nom de "scale-to-one". Ils deviennent occupés et, lorsqu'ils ont terminé, ils redeviennent inactifs. S'ils deviennent trop occupés, ils reçoivent de l'aide d'autres clones (également connus sous le nom de mise à l'échelle horizontale).


## Avantages du Serverless

Il y a quelques avantages aux implémentations serverless. Un grand avantage est qu'elles se mettent à l'échelle facilement et efficacement. Cela est dû au fait qu'elles sont généralement basées sur des médias d'installation légers, comme des images/conteneurs Docker, et vous n'avez pas besoin de provisionner des machines supplémentaires.

En théorie, avec le calcul serverless, vous avez toute l'infrastructure cloud du fournisseur à vos pieds. Avec les coûts respectifs, bien sûr. :)

En parlant de coûts, le code serverless est facturé à la seconde et à un taux plus élevé qu'une location de machine. Il est donc recommandé de l'exécuter pour des charges de travail relativement courtes.

Certains fournisseurs imposent une limite stricte sur la durée d'exécution du code serverless. Cela permet également d'éviter les mauvaises surprises sur votre facture.

Un exemple notable de serverless full-stack et des avantages de coût qui l'accompagnent est acloud.guru.

Je me souviens avoir étudié pour la certification AWS Architect en utilisant l'un de leurs cours (excellente formation d'ailleurs, fortement recommandée), et l'instructeur mentionnant que "Nous payons 400 $ par mois avec Serverless et cela serait autour de 100 000 $ en utilisant des serveurs".

### Qu'en est-il des inconvénients du serverless ?

L'un des inconvénients de l'architecture serverless concerne les applications critiques en temps. 

Généralement, les fonctions serverless nouvellement déployées subissent une certaine latence, également connue sous le nom de "cold start". Il existe des atténuations qui peuvent vous aider à gérer les cold starts, appelées - surprise, surprise - "warm starts". Mais vous pourriez vouloir vérifier d'autres architectures pour de telles exigences.

Au fait, les solutions serverless fournies par les fournisseurs cloud (comme AWS Lambda, Azure Functions) sont en fait également gérées. Cela signifie que vous pouvez configurer votre architecture serverless en utilisant des abstractions de haut niveau et entrer vos préférences/configuration avec les formulaires qu'ils fournissent.

## Services Gérés + Serverless

Comme vous l'avez probablement compris maintenant, le serverless et les services gérés ont des similitudes intéressantes. Nous pouvons les résumer ainsi : Ne vous souciez pas de l'infrastructure, concentrez-vous sur la valeur de votre entreprise.

Il existe un service public très intéressant qui combine les deux saveurs, géré et serverless. Il s'agit d'AWS Aurora. Aurora est une base de données gérée, compatible avec MySQL et Postgresql.

![Emprunté à David Zhang](https://miro.medium.com/max/960/1*1_5fnrCrSYmyCUhugLxU5A.jpeg)

Il existe deux versions d'Aurora. Il y a l'option gérée, où vous configurez une base de données en utilisant un formulaire, et elle démarre quelques machines virtuelles et prend soin de leur santé. Dans ce cas, vous pouvez simplement vous concentrer sur le déploiement d'un bon schéma de base de données.

Dans cette méthode gérée, la base de données fonctionne 24/7/365. Ou du moins c'est l'objectif, car elle offre une très haute disponibilité et fonctionne sinon de la même manière que tout serveur de base de données que vous avez utilisé dans le passé.

Il y a aussi la version serverless, où Aurora est configurée de manière serverless. Dans ce cas, vous avez le stockage "déployé" 24/7/365 comme ci-dessus. Vous ne pouvez pas avoir de stockage serverless, ce qui est contradictoire (selon mes connaissances actuelles au moins). :)

Mais les processus qui effectuent des manipulations de données sur vos données, comme la récupération et la mise à jour, peuvent être facilement convertis en fonctions serverless.

Aurora serverless coûte souvent beaucoup moins cher, car les manipulations de données s'exécutent sur une base ponctuelle. Mais si la base de données est assez occupée, les coûts pourraient être plus élevés que dans une architecture serverfull.

Cela dit, il est préférable d'utiliser Aurora serverless lorsque votre charge de travail est intermittente et imprévisible.

## Qu'est-ce qu'Openfaas ?

Dans cet article, j'ai expliqué ces technologies dans le contexte des fournisseurs de cloud public.

Si vous souhaitez exécuter du calcul serverless / FaaS sans dépendre d'un fournisseur public, vous pouvez utiliser OpenFaas (un futur article à venir).

![Logo OpenFaaS](https://avatars.githubusercontent.com/u/27013154?s=280&v=4)

Cette technologie ne vous donnera pas seulement plus de contrôle sur votre architecture. Elle vous aidera également à réaliser que le modèle serverless repose sur des technologies de clustering comme Kubernetes. De plus, vous apprendrez comment configurer des règles de mise à l'échelle et des démarrages à froid/chaud.

## Conclusion

Merci d'avoir lu jusqu'à la fin. Nous avons parlé des technologies Serverless et les avons comparées aux services gérés.

Ils ont un chevauchement sérieux mais couvrent également des besoins différents. Si vous avez besoin d'ajouter quelque chose, j'adorerais entendre vos réflexions.