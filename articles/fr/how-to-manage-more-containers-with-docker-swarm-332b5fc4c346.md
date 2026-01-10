---
title: Comment gérer plus de conteneurs avec Docker Swarm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-17T16:34:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-more-containers-with-docker-swarm-332b5fc4c346
coverImage: https://cdn-media-1.freecodecamp.org/images/0*3rx5b0F29g00opjD.
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment gérer plus de conteneurs avec Docker Swarm
seo_desc: 'By nolan grace

  Scaling beyond a single server is a an important feature to understand about containers.
  When you start using containers to make it easy to scale your application, things
  really start to get interesting. Imagine you have used Docker co...'
---

Par nolan grace

Passer à l'échelle au-delà d'un seul serveur est une fonctionnalité importante à comprendre concernant les conteneurs. Lorsque vous commencez à utiliser des conteneurs pour faciliter la mise à l'échelle de votre application, les choses deviennent vraiment intéressantes. Imaginez que vous avez utilisé des conteneurs Docker pour le développement et les tests. Maintenant, vous êtes prêt à passer en production.

Comment pouvez-vous vous assurer que votre application dispose de suffisamment de ressources ? Si vous devenez viral, comment allez-vous mettre à l'échelle ?

C'est là que vous devriez commencer à utiliser un orchestrateur de conteneurs comme **Swarm**. Le même groupe qui vous a apporté Docker a construit Swarm. Swarm existe pour gérer les conteneurs Docker sur un cluster de machines. Docker Swarm facilite le déploiement, la gestion et la mise à l'échelle de vos conteneurs.

Dans cet article, nous allons passer en revue les bases de l'orchestration de conteneurs sur un cluster. Nous discuterons des fonctionnalités de Docker Swarm, y compris comment démarrer un Swarm, déployer une application et mettre à l'échelle cette application. Si vous n'êtes pas familier avec Docker, consultez mes autres articles.

[Qu'est-ce que Docker ?](https://medium.com/pintail-labs/docker-series-what-is-docker-9eddca88f434)
[Démarrer votre premier conteneur](https://medium.com/pintail-labs/docker-series-starting-your-first-container-92dfd1dc859)
[Créer votre premier Dockerfile](https://medium.com/pintail-labs/docker-series-creating-your-first-dockerfile-573bfea4991)
[Construire votre première image](https://medium.com/pintail-labs/docker-series-building-your-first-image-8a6f051ae637)
[Passer à plusieurs conteneurs](https://medium.com/pintail-labs/docker-series-moving-past-one-container-bf32b45831d3)

Revenez ici lorsque vous vous sentirez prêt.

![Image](https://cdn-media-1.freecodecamp.org/images/Lgg-h5hp0KgtrcuhueqFiFCciZwSoGRff0m7)

Vous avez peut-être entendu dire que Swarm est un orchestrateur de conteneurs. Que veux-je dire par là ? Swarm prend le contrôle de la gestion et de l'organisation des hôtes et des conteneurs Docker exécutés sur votre cluster.

Considérez Swarm comme une application qui comprend comment exécuter des commandes Docker. Vous lui indiquez où se trouvent tous vos hôtes Docker, quels conteneurs vous souhaitez exécuter, et Swarm s'occupe du reste. Swarm gère le réseau, l'accès, l'état de vos conteneurs, la mise à l'échelle des services, l'équilibrage de charge, et même le déplacement des conteneurs si un hôte devient non réactif.

Dans cet article, nous allons démarrer un Docker Swarm sur votre machine locale. Avec notre Swarm local, nous nous familiariserons avec les commandes les plus courantes et déployerons quelques services.

### Démarrer un swarm

Pour commencer, vous devrez avoir Docker-CE installé. Pour vous aider à installer Docker sur votre machine, veuillez consulter le site [Docker-CE](https://www.docker.com/community-edition).

Une fois que vous avez installé Docker avec succès, démarrer votre premier Docker Swarm est aussi simple que d'exécuter une commande. Ouvrez votre terminal ou votre invite de commande et exécutez la commande ci-dessous.

```
> docker swarm init
```

Vous l'avez fait ! Vous exécutez votre premier Swarm.

Si vous exécutez cet hôte sur une plateforme cloud comme AWS ou dans une ferme de serveurs, l'ajout de plus de nœuds à votre cluster swarm est simple. Suivez simplement les instructions dans la documentation Docker sur la façon de [créer un Swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/). Cette documentation vous montrera comment initialiser manuellement et ajouter des nœuds à un cluster Docker Swarm.

Une autre option est de lancer votre propre cluster [Rancher](http://rancher.com/). Après avoir configuré Rancher, vous pouvez le laisser faire le travail difficile pour vous. Rancher est un service que j'utilise lorsque j'explore les fonctionnalités de différents orchestrateurs de conteneurs. Rancher facilite le lancement d'un cluster de machines et le démarrage d'un orchestrateur de conteneurs de votre choix. Rancher dispose d'un tableau de bord web interactif et convivial qui facilite le lancement de différents orchestrateurs, y compris Swarm, Mesos ou Kubernetes.

Vous pouvez trouver des informations sur [Getting Started with Rancher](http://rancher.com/docs/rancher/v1.6/en/quick-start-guide/) et [Using Rancher to Start a Swarm](http://rancher.com/docs/rancher/v1.6/en/swarm/) dans la documentation Rancher.

Pour les besoins de cet article, nous allons nous en tenir au nœud unique s'exécutant sur votre machine locale. Cela rendra beaucoup plus facile la familiarisation avec Docker Swarm et l'interface de ligne de commande Swarm.

### Déployer sur Swarm

Maintenant que vous avez votre swarm en cours d'exécution, commençons quelques conteneurs ! Si vous êtes familier avec Docker, le déploiement sur Docker Swarm devrait être un jeu d'enfant. Les commandes utilisées pour déployer des services et des stacks pour Docker-CE sont les mêmes commandes utilisées pour Docker Swarm.

Pour déployer l'image docker [pintail-whoami](https://github.com/pintail-ai/pintail-whoami), exécutez la commande ci-dessous.

```
> docker service create --name pintail-whoami -p 80:80 pintailai/pintail-whoami:0.0.1
```

Ouvrez votre navigateur et allez à _http://localhost_ et vous devriez voir la page ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/9EnRZmrQVM5uRjhsnB81zMyOFurWzZD62YAM)

La commande utilisée pour démarrer ce service peut être exactement la même que Docker-CE, mais les choses fonctionnent un peu différemment lorsque vous êtes connecté à un Swarm.

Lorsque vous exécutez des services dans un Swarm, la plus grande différence est l'emplacement physique de vos conteneurs en cours d'exécution. Docker Swarm démarrera un conteneur sur n'importe quel hôte où des ressources sont disponibles. Donc, simplement parce que vous démarrez un conteneur à partir d'un hôte ne signifie pas que c'est là que le conteneur s'exécutera.

Alors, comment accédez-vous à un service qui pourrait être démarré n'importe où dans votre cluster ?

Docker Swarm dispose d'un outil très utile pour résoudre ce problème appelé le maillage de routage Swarm. Le maillage de routage gère l'entrée dans vos conteneurs en cours d'exécution. Par défaut, Swarm rend tous les services accessibles via leur port publié sur chaque hôte Docker.

![Image](https://cdn-media-1.freecodecamp.org/images/9hagYkC57mS2Ne9YCDAKnqUOHXPKPXfH0Z7z)

Supposons que vous avez un Swarm contenant trois hôtes Docker. Si vous déployez un service sur votre Swarm publié sur le port 80, peu importe depuis quel hôte vous accédez à ce port, vous serez redirigé vers votre service.

Dans le monde réel, si vous avez une application web et une API Rest, vous pourriez déployer votre application web sur le port 80 et votre API sur le port 8080. Avec cette configuration, vous pouvez mettre à l'échelle le nombre de conteneurs exécutant différentes parties de votre application. Mais vous pouvez toujours être sûr que le port 80 sur n'importe quel nœud du cluster Swarm vous mènera au site web, et le port 8080 à l'API Rest.

Le maillage de routage Swarm a ses avantages et ses inconvénients. Cette configuration par défaut a ses limitations, mais elle est conçue pour rendre le démarrage aussi facile que possible. À mesure que vos applications deviennent plus complexes, le maillage de routage peut être configuré pour se comporter différemment et différents services peuvent être déployés pour utiliser différentes configurations de routage. Pour plus d'informations, veuillez consulter la [documentation sur le maillage de routage du mode Swarm](https://docs.docker.com/engine/swarm/ingress/).

### Mettre à l'échelle votre service

Maintenant que nous avons un service en cours d'exécution, augmentons un peu la cadence !

Imaginez que vous exécutez votre site web sur un Docker Swarm en production et que votre site commence à devenir tendance sur Hacker News. Votre trafic triple et vous devez gérer la charge supplémentaire. Pour tripler le nombre de conteneurs que vous exécutez, exécutez simplement la commande ci-dessous :

```
> docker service scale pintail-whoami_pintail-whoami=3
```

Presto ! Docker Swarm met à l'échelle le nombre de réplicas que vous exécutez et achemine le trafic vers les conteneurs. Après que la commande ci-dessus soit terminée, retournez à l'exemple "Pintail.ai Docker Example" dans votre navigateur et cliquez sur actualiser plusieurs fois. Vous devriez voir le nombre changer à mesure que le maillage de routage vous dirige vers différents conteneurs.

Swarm facilite la mise à l'échelle des services afin que vous puissiez vous concentrer sur des problèmes plus importants.

### Nettoyer

Maintenant, nettoyons nos conteneurs et Swarm.

Pour supprimer la pile pintail-whoami, exécutez

```
> docker stack rm pintail-whoami
```

**Soyez prudent avec cette prochaine commande**. Si vous exécutez autre chose dans le swarm, cela sera supprimé.

Pour supprimer votre cluster Swarm, exécutez

```
> docker swarm leave --force
```

Dans cet article, nous avons démarré un hôte Swarm, nous avons discuté de l'ajout de nœuds à notre cluster, nous avons démarré et mis à l'échelle un service, et nous avons parlé du maillage de routage Swarm. Espérons que cette introduction vous aidera à mieux comprendre l'orchestration de conteneurs et Docker Swarm.

Cet article ne fait qu'effleurer la surface de ce qui est possible avec les conteneurs et Swarm, mais j'espère qu'il vous donne un contexte pour vous aider à continuer à apprendre.

Veuillez me faire savoir si vous avez des commentaires, des questions ou des préoccupations dans les commentaires. Je suis toujours ouvert aux retours et serais ravi d'entendre vos suggestions. Si vous avez aimé l'article, veuillez me laisser beaucoup d'applaudissements pour me le faire savoir.