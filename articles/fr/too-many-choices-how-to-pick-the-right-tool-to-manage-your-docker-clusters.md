---
title: 'Trop de choix : comment choisir le bon outil pour gérer vos clusters Docker'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-15T14:04:00.000Z'
originalURL: https://freecodecamp.org/news/too-many-choices-how-to-pick-the-right-tool-to-manage-your-docker-clusters
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca174740569d1a4ca4eaf.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: 'Trop de choix : comment choisir le bon outil pour gérer vos clusters Docker'
seo_desc: There are all kinds of ways to play the Docker game and, obviously, no one
  of them is going to be right for every use case. So what I’m going to do here is
  give you a brief functional overview of each of the most obvious management options
  in a way t...
---

Il existe toutes sortes de façons de jouer au jeu Docker et, évidemment, aucune d'entre elles ne conviendra à tous les cas d'utilisation. Ce que je vais faire ici, c'est vous donner un bref aperçu fonctionnel de chacune des options de gestion les plus évidentes, de manière à vous aider à choisir par vous-même et à vous faire gagner beaucoup de temps et de frustration dans le processus. Ainsi, vous aurez l'air intelligent et personne n'aura besoin de savoir que c'était moi tout du long.

Tout d'abord, voici la phrase avec laquelle tout article sur un sujet même vaguement lié à Docker doit commencer : Au cours des n dernières années (où n < 6), les technologies de conteneurs, et Docker en particulier, sont devenus des outils dominants dans le monde de la fourniture d'applications.

Bien. Cela étant dit, nous pouvons passer aux choses sérieuses. Vous envisagez donc de livrer votre application ou votre service réseau via des conteneurs Docker... ou au moins de leur donner un bon coup d'œil. Je ne vais certainement pas argumenter avec vous : c'est probablement un bon choix.

Maintenant, présumément, vous savez déjà que Docker Engine est l'environnement logiciel open source qui vous permet de virtualiser des parties d'un système matériel hôte jusqu'à ce qu'ils ressemblent et agissent comme de vrais serveurs. Docker est maintenant disponible en versions gratuites (Community Edition) ou avec support commercial (Enterprise Edition).

Sans aucun doute, vous savez également que l'invocation de Docker Engine à partir de votre ligne de commande en utilisant des choses comme :

```
$ docker ps$ docker images
```

et :

```
$ docker network inspect
```

...fera avancer les choses. Pas très à l'aise avec tout cela ? Il y a du matériel de niveau intro que vous pourriez aimer et qui est inclus dans mes [cours orientés Docker sur Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton).

Tout cela fonctionnera très bien pendant que vous apprenez simplement à vous repérer. Mais une fois que vous êtes prêt à commencer à planifier un déploiement robuste et hautement évolutif — complet avec des configurations complexes qui peuvent inclure des microservices et des ponts réseau — alors le paysage change rapidement. La question n'est pas tant "comment", mais "où et lequel" : Avez-vous les ressources de calcul et de réseau pour exécuter votre application localement, ou devrez-vous trouver un hôte ? Devez-vous le faire vous-même ou choisir un service géré sur un cloud public comme Elastic Beanstalk d'AWS ?

Et puis, qu'en est-il de l'administration ? Êtes-vous du type pratique ou préférez-vous rester un ou deux niveaux en arrière et laisser des outils de gestion comme Kubernetes ou le mode essaim Docker faire une partie du travail difficile pour vous ? Ou peut-être deux ou trois niveaux en arrière et opter pour Ansible ou Puppet ?

Divisons les choses en trois catégories : les outils de dépôt pour stocker et gérer les images Docker, les frameworks d'administration pour définir, lancer et gérer les conteneurs Docker tout au long de leur cycle de vie, et enfin quelques outils de ligne de commande et d'automatisation de la configuration.

## 1. Registres d'images

### Docker Hub

Pour la plupart des gens, l'endroit le plus évident pour chercher des images Docker — les packages contenant les systèmes d'exploitation et les logiciels utilisés pour exécuter des conteneurs — est Docker Hub. Fournis par Docker lui-même, Docker Hub contient une vaste collection d'images préchargées pour soutenir tous types de projets d'applications. Vous pouvez trouver et rechercher des images sur le site web [hub.docker.com](https://hub.docker.com/), puis les extraire directement dans votre propre environnement Docker Engine.

```
$ docker pull ubuntu
```

Une fois que vous commencez à créer vos propres images, vous pouvez les stocker en toute sécurité, autant que vous le souhaitez, dans des dépôts publics sur Docker Hub. De plus, ils vous permettent un dépôt privé gratuitement, et plus à un taux d'environ un dollar par dépôt. Peut-être que la chose la plus agréable à propos de Docker Hub est la façon dont il fonctionne de manière transparente avec presque tout ce qui est connecté à Docker, y compris les fournisseurs de cloud public comme AWS et les services de gestion d'infrastructure comme Docker Cloud.

Le service séparé Docker Store vous permet de publier des images et des plugins pré-certifiés pour satisfaire la demande d'accès à des ressources de confiance.

### EC2 Container Registry (ECR)

Amazon AWS connaît tout le pouvoir et le potentiel de Docker et veut participer au jeu. Dans le cadre de leurs efforts pour ouvrir leur écosystème cloud à autant d'affaires Docker que possible, ils ont construit leur propre registre pour accompagner leur plateforme EC2 Container Service : ECR. Les images peuvent être poussées, tirées et gérées via l'interface graphique ou l'outil CLI d'AWS. Les politiques de permissions peuvent contrôler étroitement l'accès aux images uniquement pour les personnes que vous sélectionnez.

La limitation ? ECR est évidemment conçu pour fonctionner au mieux avec une infrastructure exécutée sur des services basés sur AWS comme ECS et Elastic Beanstalk.

### Docker Registry

Si vous devez maintenir vos images un peu plus près de chez vous — soit pour des raisons de sécurité ou pratiques — alors vous voudrez savoir que Docker propose un Docker Registry librement disponible. Vous désignez un serveur de registre avec accès à et depuis vos autres actifs réseau, installez puis activez le package docker-registry, étiquetez les images pour qu'elles soient pointées vers votre registre local, et vous avez un vrai dépôt privé en direct.

```
$ dpkg -i docker-registry_2.4.1~ds1-2_amd64.deb$ systemctl enable docker-registry$ docker tag hello-world localhost:5000/hello-world:latest
```

Les images elles-mêmes sont stockées profondément dans le système de fichiers de votre serveur, mais elles sont disponibles via les mêmes outils CLI que celles sur Docker Hub. Vous vous inquiétez de la sécurité de vos images ? Docker Registry vous permet d'appliquer des certificats SSL/TLS et de contrôler l'accès en imposant une authentification de connexion à votre site.

Le Docker Trusted Registry est la version commerciale de Docker Registry. En échange de frais mensuels ou annuels, vous obtenez des fonctionnalités supplémentaires, y compris le support, une interface graphique basée sur le navigateur et l'intégration LDAP/AD.

## 2. Frameworks d'administration

Même une fois que vous avez dépassé le stade de la simple découverte du fonctionnement des choses, vous pourriez encore vouloir maintenir un déploiement Docker actif sur site : peut-être que tous vos clients sont locaux ou que votre charge de travail projetée n'est pas si lourde. Ou peut-être que vous êtes simplement paranoïaque en matière de sécurité. Et par "paranoïaque en matière de sécurité", je veux bien sûr dire "bien informé sur l'état actuel des vulnérabilités du réseau".

Une façon de "rester local" est de simplement continuer ce que vous avez fait jusqu'à présent. Tant que vous prenez en compte la sécurité des ressources et les considérations de capacité, il n'y a aucune raison d'abandonner le bon vieux Docker Engine Community Edition que vous avez déjà installé.

Cependant, si le niveau de complexité auquel vous pensez être confronté vous laisse un peu perdu, alors vous pourriez vouloir envisager de passer à un environnement commercial qui, en plus du support continu, peut offrir des consoles d'administration basées sur le navigateur. Dans les deux cas, vous devrez fournir votre propre environnement d'hébergement où vos conteneurs s'exécuteront. Cela pourrait être vos serveurs locaux, ou des machines virtuelles s'exécutant dans un cloud public comme AWS ou Azure.

### Docker Datacenter

Vous configurez Datacenter (maintenant commercialisé dans le cadre de Docker Enterprise Edition) en téléchargeant et en installant le Docker Engine régulier sur votre serveur local, ainsi qu'un deuxième package appelé Docker Universal Control Plane (UCP). L'UCP fournit une interface de navigateur qui permet une gestion centralisée de toutes les images, applications et réseaux qui composent votre infrastructure. La sécurité est également gérée via l'interface.

### Docker Cloud

Très similaire à Docker Datacenter (qui est également un produit officiel Docker), Docker Cloud offre une console GUI basée sur le navigateur pour gérer tous les aspects de vos déploiements Docker. Cela inclut l'administration de vos nœuds hôtes s'exécutant dans des clouds publics. La grande différence est que, contrairement à Datacenter, le service d'administration Docker Cloud est hébergé sur le site [cloud.docker.com](https://cloud.docker.com/app/dbclinton) : il n'y a pas de logiciel serveur à installer sur votre propre équipement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ab1QINvkjm9id1jY.png)
_Docker Cloud — paramètres du fournisseur de cloud_

Il fonctionne en entrant les informations d'authentification pour vos comptes de fournisseurs de cloud (comme AWS) ou en installant l'agent Docker Cloud sur toute machine Linux ou Windows s'exécutant n'importe où où il y a une connectivité réseau. En cliquant sur le bouton "Bring your own node" dans la fenêtre Node Clusters, une commande Linux pour télécharger et installer l'agent qui pourrait ressembler à ceci s'affichera :

```
$ curl -Ls https://get.cloud.docker.com/ | sudo -H sh -s 90b501cb04e344bfbf76890a09362c39
```

Docker Cloud organise les ressources en clusters de nœuds, qui sont des groupes de nœuds individuels gérés dans le cadre d'un seul service, tous dédiés à un objectif de déploiement unifié.

Je pense que la raison pour laquelle Docker continue de promouvoir deux services aussi similaires (Datacenter et Cloud) remonte à il y a quelques années, lorsque Docker a racheté une entreprise appelée Tutum et a renommé leur produit basé sur le web Docker Cloud. Tutum avait déjà une base de clients heureuse et un modèle commercial assez réussi, donc il n'y avait aucune raison de le fermer. Dans tous les cas, les deux fonctionnent, alors choisissez simplement celui qui vous plaît.

### AWS EC2 Container Service (ECS)

Outre le registre d'images ECR, AWS a créé sa propre infrastructure complète pour l'hébergement et la gestion des clusters de conteneurs Docker. ECS fonctionne en provisionnant une instance EC2 spécialement conçue avec Docker Engine et un agent ECS installés. En utilisant soit la console ECS soit l'interface CLI AWS, vous pouvez définir, lancer et gérer des conteneurs sur cette instance EC2.

```
$ aws ecs describe-clusters
```

Pour être honnête, comprendre comment toutes les pièces de l'ECS s'emboîtent peut être une tâche difficile. [Mon cours "Using Docker on Amazon Web Services" sur Pluralsight](https://pluralsight.pxf.io/nZgKx) consacre du temps à expliquer comment les pièces fonctionnent. Voici la version courte :

* **Tâches** : métadonnées définissant une application et son environnement réseau, de stockage et de sécurité
* **Services** : logiciel qui lance, surveille et contrôle vos conteneurs
* **Conteneurs** : définitions pour les machines qui exécuteront une tâche
* **Clusters** : structures d'organisation pour les tâches et les services

![Image](https://cdn-media-1.freecodecamp.org/images/0*IaNAvWY8t6EU_oMA.jpg)
_Un diagramme de l'architecture du service EC2 Container_

### AWS Elastic Beanstalk

Elastic Beanstalk se place effectivement au-dessus de l'ECS, vous permettant de déployer votre application sur toutes les ressources AWS normalement utilisées par l'ECS, mais avec pratiquement toute la logistique soigneusement abstraite. En effet, tout ce dont vous avez besoin pour lancer un environnement de microservices complexe et entièrement évolutif est un script déclaratif au format JSON dans un fichier appelé Dockerrun.aws.json. Vous pouvez soit télécharger votre script vers l'interface graphique, soit, à partir d'un répertoire local initialisé en utilisant l'interface de ligne de commande AWS Beanstalk, l'exécuter en utilisant :

```
$ eb run
```

Et c'est tout. Non, vraiment.

Je devrais mentionner que les fichiers Dockerrun.aws.json existent en deux versions : V1 pour les déploiements de conteneurs uniques, et V2 pour les conteneurs multiples. Il est également intéressant de noter qu'un grand avantage de l'utilisation de l'interface CLI par rapport à la version navigateur est la facilité avec laquelle elle peut permettre les connexions SSH à distance à l'hôte EC2 et les tâches d'administration.

Voici une autre chose à laquelle penser : les dix-sept premiers chapitres de mon livre "[Learn Amazon Web Services in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27)" ont retracé, étape par étape, la construction d'un site WordPress hautement disponible, évolutif et sécurisé. Pour le chapitre 19 — juste pour illustrer rapidement comment cela fonctionne — j'ai créé un fichier Dockerrun.aws.json de 20 lignes qui a fait presque exactement la même chose... mais en seulement cinq minutes.

_Cela ne signifie pas que les 17 premiers chapitres du livre étaient une perte de temps ! En fait, sans comprendre comment chaque service AWS séparé fonctionne, vous ne comprendriez pas pleinement ce que Beanstalk a réellement accompli. Et vous manquerez certainement toutes sortes de fonctionnalités qui peuvent vous emmener bien au-delà des choses que Beanstalk peut offrir. Mais cela en dit long sur la puissance des déploiements scriptés, n'est-ce pas ?_

## 3. Outils de gestion

#### Mode Docker Swarm

Bien qu'il fasse maintenant partie intégrante de Docker Engine dès sa sortie, peut-être parce qu'il subit encore des changements constants, le mode essaim Docker a d'une certaine manière la saveur d'un produit autonome. L'idée est que vous pouvez désigner l'un de vos serveurs (appelé nœud) comme gestionnaire :

```
$ docker swarm init
```

...et d'autres serveurs comme clients :

```
$ docker swarm join
```

À partir de là, en utilisant les commandes "docker service" depuis le gestionnaire, vous créerez et administrerez des clusters de conteneurs Docker en tant que services, et répartirez automatiquement et efficacement les conteneurs parmi tous vos serveurs disponibles, où qu'ils se trouvent. Vous devriez essayer cela par vous-même juste pour le frisson d'exécuter une simple commande "service scale" et de voir le nombre approprié de conteneurs apparaître magiquement et instantanément sur votre réseau.

```
$ docker service create -p 80:80 --name webserver nginx$ docker service scale webserver=5
```

J'ai consacré une partie de mon cours [Pluralsight "Using Docker with AWS Elastic Beanstalk"](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton) à démontrer Docker Swarm en action. Jetez un coup d'œil si vous êtes intéressé.

### Kubernetes

Comme Swarm, Kubernetes de Google est également très efficace pour gérer de grands clusters de conteneurs. Et dire que Kubernetes est populaire, c'est comme dire que la pluie est humide. Évidemment.

Kubernetes organise les ressources en pods, qui eux-mêmes sont composés de conteneurs interconnectés exécutant des microservices individuels. Vous devriez considérer un pod comme étant entièrement jetable, sa fonction instantanément remplaçable par d'autres attendant leur chance d'entrer dans ce monde.

En fait, les pods sont créés et détruits selon les besoins définis sur le nœud maître par des éléments comme les planificateurs et les contrôleurs de réplication, qui peuvent à leur tour être gérés par le programme kubectl. Les pods — et leurs conteneurs — s'exécutent sur des serveurs appelés nœuds de travail exécutant leurs propres instances de Docker Engine.

_Je ne sais pas pour vous, mais je trouve à la fois confus et ennuyeux que chaque plateforme informatique choisisse de désigner les éléments constitutifs par des noms différents — mais souvent seulement légèrement différents. Il devrait y avoir une loi._

### Outils d'automatisation de déploiement

Je ne peux pas quitter un article de revue comme celui-ci sans au moins mentionner comment vous pouvez utiliser presque tous les outils populaires d'orchestration de déploiement comme Ansible, Jenkins et Puppet pour automatiser vos environnements Docker. Plonger dans les détails fins me mènerait bien au-delà de mon plan initial pour cet article, alors choisissez simplement votre outil préféré et documentez-le.

_Cela a-t-il été utile ? Consultez mon site [Bootstrap IT](https://bootstrap-it.com/) pour une multitude de contenus similaires sur Docker, Linux et AWS._