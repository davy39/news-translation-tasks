---
title: 'Une introduction à Amazon Fargate : ce que c''est, pourquoi c''est génial
  (et pas toujours), et quand l''utiliser.'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T19:14:00.000Z'
originalURL: https://freecodecamp.org/news/amazon-fargate-goodbye-infrastructure-3b66c7e3e413
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-5KIBlv5vzflb1zgsu9WJg.jpeg
tags:
- name: AWS
  slug: aws
- name: Docker
  slug: docker
- name: fargate
  slug: fargate
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une introduction à Amazon Fargate : ce que c''est, pourquoi c''est génial
  (et pas toujours), et quand l''utiliser.'
seo_desc: 'By Emmanuel Marboeuf

  When Amazon announced Fargate in late 2017 at AWS re:Invent (along with EKS) it
  really fell under the radar. None of the blogs or influencers that I was following
  at that time really talked about it other than something along the...'
---

Par Emmanuel Marboeuf

Lorsque Amazon a [annoncé](https://www.youtube.com/watch?v=8i82i9QYUGs) Fargate fin 2017 lors de l'AWS re:Invent (en même temps qu'EKS), cela est vraiment passé inaperçu. Aucun des blogs ou influenceurs que je suivais à l'époque n'en a vraiment parlé, si ce n'est quelque chose comme :

> Oh oui, et il y a cette nouvelle chose qui permettra aux utilisateurs d'ECS d'exécuter des conteneurs directement dans le cloud.

En tant que développeur, cela m'a vraiment impressionné. **Voyons pourquoi.**

### L'explosion de la productivité

Je pense qu'il y a eu **cinq** grandes révolutions dans le monde du développement logiciel qui ont considérablement augmenté la productivité des développeurs et leur capacité à écrire et déployer des applications de niveau production avec une efficacité maximale.

Elles ont toutes résolu des problèmes majeurs. Voici ma répartition des révolutions et des problèmes qu'elles ont résolus :

* Émergence des services cloud (IaaS)
**Coût de l'infrastructure et scalabilité**
* Communauté open source, conférences, ateliers, blogs techniques, Stack Overflow, etc.
**Accès limité aux connaissances**
* Systèmes de versionnement, outils de collaboration, outils d'intégration continue
**Ingénierie concurrente, disparités des systèmes et enfer de l'intégration**
* Architecture conteneurisée
**Difficulté à construire des applications dans des environnements incohérents**
* Services de calcul serverless (PaaS)
**Administration des serveurs et des systèmes**

Chacune de ces révolutions a un trait commun : elles donnent **plus de contrôle aux ingénieurs logiciels**. Elles y parviennent en encourageant les bonnes pratiques et le partage de code avec un flux de travail collaboratif, et elles réduisent le besoin de serveurs dédiés coûteux, d'administrateurs système, de DevOps, de support IT, et ainsi de suite.

Très bien, mais attendez — où est **Fargate** dans tout cela ?

### Votre navire est le problème

![Image](https://cdn-media-1.freecodecamp.org/images/1*o5kiw7FwodkMegfRDNfktg.jpeg)
_Le gilet de sauvetage est conseillé_

Voyez-vous, lorsque Docker a apporté les conteneurs aux masses, cela est rapidement devenu une nouvelle norme en développement et a été largement adopté.

Peu après, et suivant le succès de **Kubernetes**, AWS a lancé son propre service de gestion de conteneurs (plus basique) : Amazon Elastic Container Service (ECS). Il a introduit le concept de Tâches.

Une tâche peut être toute instance de conteneurs travaillant ensemble. D'une application web qui exécute un serveur web, plusieurs microservices, une base de données et un proxy inverse, à une liste de lots de scripts shell qui s'exécuteront périodiquement.

Étant un adopteur précoce d'ECS, j'ai vraiment aimé cela et cela a bien fonctionné pendant un moment. Mais finalement, devoir gérer ces **couches supplémentaires** (Tâches et conteneurs) au lieu de simplement des instances EC2 est devenu de plus en plus compliqué.

Je n'étais également pas à l'aise avec sa **sécurité**. Plus vous avez de couches dans votre stack, plus vous devez être vigilant. Chacune de ces couches apporte plus de complexité ainsi qu'une probabilité accrue de mauvaises configurations de sécurité et de vulnérabilités.

En effet, avec ECS, vos conteneurs s'exécutent dans **des instances de conteneurs EC2 dans un cluster** que vous configurerez pour l'auto-scaling. Chaque instance peut héberger plusieurs tâches différentes. Chaque tâche peut exécuter plusieurs conteneurs.

Parce que vos tâches seront déployées aléatoirement (par défaut) sur le même type d'**instances EC2 avec des ressources disponibles**, vous êtes confronté aux problèmes suivants :

* Un cluster suit les mêmes règles pour l'auto-scaling et provisionne automatiquement le même type d'instances EC2.
* Certains conteneurs auront besoin de ressources totalement différentes mais devront toujours travailler ensemble.
* Certains conteneurs ne suivent pas nécessairement les mêmes règles pour l'auto-scaling.
* Parfois, plusieurs conteneurs dans la même tâche ont besoin de leur propre équilibreur de charge, et avoir plusieurs équilibreurs de charge pour la même tâche n'est pas possible.

La solution de contournement préférée lorsque l'on est confronté à ces problèmes était de :

* déployer manuellement certaines de vos instances avec différentes ressources en fonction des besoins
* attacher ces instances à votre cluster
* exécuter un conteneur par tâche
* lier manuellement vos instances EC2 ensemble
* écrire des contraintes de placement de stratégie complexes sur ECS pour s'assurer que la bonne tâche était sur la bonne machine qui avait la ressource appropriée en fonction de ce qu'elle faisait

C'est **beaucoup** de travail, c'est assez **fastidieux**, et c'est **difficile à maintenir**. Et cela va un peu à l'encontre du but de travailler avec des conteneurs en premier lieu.

Quelqu'un devait avoir une meilleure idée.

### Laissez-les flotter

Il s'avère que l'équipe AWS avait les mêmes problèmes. Ils y ont réfléchi pendant l'année passée et ont travaillé sur la résolution du problème suivant :

> Comment pourrions-nous exécuter des conteneurs sans avoir à nous soucier des serveurs et des clusters ?

**Et c'est ce qu'est AWS Fargate**. Il abstrait complètement l'infrastructure sous-jacente, et vous voyez chacun de vos conteneurs comme une seule machine.

Vous n'avez qu'à spécifier les ressources dont vous avez besoin pour chaque conteneur et il fera le travail difficile pour vous. Vous n'avez plus à gérer des règles d'accès multi-couches. Vous pouvez ajuster finement les permissions entre vos conteneurs comme vous le feriez entre des instances EC2 individuelles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aLMrzsEK-E9EGIjxXvQ48Q.jpeg)
_conteneurs sur Fargate (rendu artistique)_

C'est comme si vos conteneurs devenaient des navires avec leur propre voile, gouvernail et équipage, capables de flotter vers leur destination par eux-mêmes.

### Conteneurs en tant que Service (CaaS)

Je crois en fait que **les Conteneurs en tant que Service (CaaS) sont le vrai PaaS** que les développeurs attendent depuis des années. Cela permet aux développeurs de déployer leurs conteneurs directement dans le cloud sans avoir à se soucier de tout ce qui se trouve entre les deux.

Bien sûr, il existe déjà de nombreuses technologies qui permettent d'exécuter votre code de manière transparente sur le cloud sans avoir à vous soucier de la scalabilité ou de l'administration des serveurs (comme l'incroyable **Heroku**, **Lambda**, ou même à sa manière **Google App Engine**). Mais toutes ont des limitations.

* Vous devez choisir entre perdre un peu de flexibilité
* Vous devez vous en tenir aux langages supportés
* Vous ne pouvez pas utiliser les langages supportés parce que votre projet nécessite une bibliothèque native de bas niveau qui n'est disponible que sur des systèmes très spécifiques
* Votre projet utilise une technologie de pointe qui ne sera pas disponible pour le grand public dans les années à venir
* Certaines de ces plateformes sont très (très) chères, surtout lorsque vous scalez

**Fargate (ou CaaS)** vous apporte le meilleur des deux mondes.

L'**architecture conteneurisée** vous apporte la flexibilité et le contrôle dont vous avez besoin. Elle vous permet d'utiliser **n'importe quel type de technologie** s'exécutant dans **n'importe quel type de système** que vous souhaitez. L'aspect conteneur garantira que vous aurez le même comportement sur chaque hôte, qu'il s'agisse d'un environnement de développement, de test, de staging ou de production.

Je trouve ce point critique pour de nombreuses startups technologiques. En fait, parfois l'un de vos avantages concurrentiels est l'utilisation d'une technologie de pointe à laquelle vous avez participé au développement, ou la réutilisation intelligente d'une autre dans un contexte totalement nouveau et révolutionnaire.

Le **déploiement serverless** vous permet de vous concentrer sur l'écriture d'un excellent code. Pas de provisionnement, scaling facile.

### Limites

#### CaaS vs PaaS

Il est vrai que vous renoncez à certains aspects intéressants du vrai PaaS. Oui, vous devrez toujours **mettre à jour manuellement** les images de vos conteneurs, et parfois vous devrez écrire vos propres images Docker. Cela peut être un défi au début si vous ne connaissez pas les bases de **l'administration système**.

Mais cela signifie également que vous pouvez faire presque tout ce à quoi vous pensez et avoir une **flexibilité et une liberté complètes** dans les systèmes, les langages, les outils, les bibliothèques et les versions que vous souhaitez utiliser.

#### Coût

Admettons-le, les services cloud (IaaS) sont **plus chers** que d'avoir votre propre infrastructure (si vous pouviez la scaler à la demande). Pour la même raison, ne pas avoir à provisionner, gérer et scaler vos serveurs a un coût. Ce n'est peut-être pas encore la meilleure solution pour certains de vos cas d'utilisation les plus simples.

Espérons qu'ils vont travailler à **réduire les coûts**. Aussi bon que soit le produit, il est difficile de justifier près de 4 [fois le prix d'une instance EC2 à la demande](https://aws.amazon.com/fargate/pricing/) équivalente (pour t2.medium par exemple).

![Image](https://cdn-media-1.freecodecamp.org/images/1*_GhNwtmR-m63DOx6b9GXDg.png)
_Comparaison des prix Fargate et EC2 en USD_

### Dois-je basculer toutes mes tâches ECS vers Fargate ?

Pas encore. Comme indiqué ci-dessus, vous allez plus que tripler vos coûts dans certains cas. Jusqu'à ce qu'ils réduisent les coûts, vous pourriez être mieux loti en utilisant des instances EC2 standard.

Cependant, Fargate peut être plus bénéfique pour vous dans les cas d'utilisation suivants :

* Si vous avez des difficultés à auto-scaler vos tâches ECS efficacement et que vous vous retrouvez souvent avec beaucoup de **CPU ou de mémoire inutilisés**. Avec Fargate, vous **ne payez que pour les ressources que vous avez définies dans vos tâches**.
* Pour vos tâches qui s'exécuteront **à la demande ou selon un calendrier** et qui n'ont pas besoin d'une instance EC2 dédiée. Avec Fargate, vous **ne payez que lorsque votre tâche s'exécute**.
* Pour vos tâches qui ont des **pics d'utilisation de mémoire et/ou de CPU**. Juste parce que cela vous fera économiser du temps et des tracas de configuration et de gestion de tels cas.

### Bonus

Pour ceux qui préfèrent **Kubernetes** à **ECS**, Fargate sera bientôt capable d'exécuter [Elastic Container Service for Kubernetes](https://aws.amazon.com/eks/).