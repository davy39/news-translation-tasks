---
title: Une introduction approfondie à Docker sur AWS
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2018-03-12T07:11:50.000Z'
originalURL: https://freecodecamp.org/news/an-in-depth-introduction-to-docker-on-aws-f373ff97da0e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6kZO8kBIc4hQPRYS-Q47nQ.jpeg
tags:
- name: AWS
  slug: aws
- name: Docker
  slug: docker
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: virtualization
  slug: virtualization
seo_title: Une introduction approfondie à Docker sur AWS
seo_desc: 'Container virtualization — most visibly represented by Docker — is a server
  paradigm that will likely drive enterprise computing for years to come.

  The Cloud is the most obvious and logical platform for containerdeployment.

  Amazon Web Services largel...'
---

La virtualisation par conteneurs — représentée de manière visible par Docker — est un paradigme de serveur qui va probablement alimenter l'informatique d'entreprise pendant des années à venir.

Le Cloud est la plateforme la plus évidente et logique pour le déploiement de conteneurs.

Amazon Web Services domine largement le monde de l'informatique en nuage. Ajoutez tout cela. Si vous êtes intéressé à obtenir une part de toute cette action, vous voudrez définitivement comprendre comment tout cela fonctionne.

Tout d'abord, définissons rapidement quelques termes clés.

### Virtualisation

La virtualisation est la division des ressources informatiques et réseau physiques en unités plus petites et plus flexibles, présentant ces unités plus petites aux utilisateurs comme si chacune était une ressource discrète.

L'idée est que, au lieu d'assigner des tâches informatiques spécifiques à des serveurs physiques individuels — qui peuvent parfois être sur- ou sous-utilisés — un seul serveur physique peut être divisé logiquement en aussi peu ou autant de serveurs virtuels que nécessaire.

Cela signifie, comme l'illustre la figure ci-dessous, qu'il peut y avoir des dizaines de systèmes d'exploitation (OS) installés individuellement fonctionnant côte à côte sur le même disque dur. Chaque OS est effectivement ignorant qu'il n'est pas seul dans son environnement local.

![Image](https://cdn-media-1.freecodecamp.org/images/UpeA5JtZvRnCwwCFTP-3hgd2X2-8HI0Or2zb)
_Multiples applications servies via des serveurs physiques ou, via des VM, à partir d'un seul serveur de virtualisation_

En pratique, chaque instance de système d'exploitation peut être accessible à distance par les administrateurs et les clients exactement de la même manière que n'importe quel autre serveur.

Dans ce type d'environnement, dès que votre serveur virtuel termine sa tâche ou devient inutile, vous pouvez le supprimer instantanément. Cela libérera les ressources qu'il utilisait pour la tâche suivante dans la file d'attente.

Il n'est pas nécessaire de sur-provisionner les serveurs virtuels pour anticiper les besoins futurs possibles, car les besoins futurs peuvent être facilement satisfaits lorsqu'ils se présentent.

En fait, le serveur virtuel d'aujourd'hui peut ne vivre que quelques minutes ou même secondes avant, ayant terminé sa tâche, être éteint pour de bon pour laisser place à ce qui suit. Tout cela permet une utilisation beaucoup plus efficace du matériel coûteux. Il offre la possibilité de provisionner et de lancer de nouveaux serveurs à volonté, soit pour tester de nouvelles configurations, soit pour ajouter de la puissance fraîche à vos services de production.

Les fournisseurs de cloud computing comme AWS utilisent des ordinateurs virtualisés d'une sorte ou d'une autre. Les centaines de milliers d'instances [Amazon EC2](https://aws.amazon.com/ec2/), par exemple, fonctionnent toutes sur les hyperviseurs open source [Xen](https://www.xenproject.org/) ou [KVM](https://www.linux-kvm.org/page/Main_Page) — qui sont eux-mêmes installés et exécutés sur des milliers de serveurs physiques maintenus dans les vastes fermes de serveurs d'Amazon.

Quelle que soit la technologie d'hyperviseur utilisée, l'objectif est de fournir un environnement d'hébergement largement automatisé pour plusieurs ordinateurs virtuels complets et autonomes.

Les conteneurs comme Docker, en revanche, ne sont pas des machines virtuelles autonomes mais des systèmes de fichiers modifiés partageant le noyau du système d'exploitation de leur hôte physique. C'est ce que nous allons discuter ensuite.

### Conteneurs

Qu'est-ce que les conteneurs ? Eh bien, pour une chose, ils ne sont pas des hyperviseurs. Au lieu de cela, ce sont des serveurs virtuels extrêmement légers qui, comme vous pouvez le voir sur la figure, au lieu de fonctionner comme des systèmes d'exploitation complets, partagent le noyau sous-jacent de leur système d'exploitation hôte.

![Image](https://cdn-media-1.freecodecamp.org/images/QEQeIyqAUN6Zk-KrvglUlbU6gjEW1s32MIZT)
_Conteneurs virtualisés fonctionnant avec accès au noyau et aux ressources matérielles de leur hôte_

Les conteneurs peuvent être construits à partir de scripts en texte brut, créés et lancés en quelques secondes, et facilement et de manière fiable partagés sur les réseaux. Les technologies de conteneurs incluent le projet [Linux Container](https://linuxcontainers.org/), qui a été l'inspiration originale de Docker.

La conception de conteneurs compatible avec les scripts facilite l'automatisation et la gestion à distance de clusters complexes de conteneurs, souvent déployés en tant que microservices.

Les microservices sont une architecture de services informatiques où plusieurs conteneurs sont déployés, chacun avec un rôle distinct mais complémentaire. Vous pourriez, par conséquent, lancer un conteneur comme backend de base de données, un autre comme serveur de fichiers, et un troisième comme serveur web.

#### Docker

Comme je l'explore dans [un ou deux de mes cours Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton), un conteneur Docker est une image dont le comportement est défini par un script. Le conteneur est lancé en tant que processus logiciel qui est habilement déguisé en serveur.

Mais qu'est-ce qu'une image ? C'est un fichier logiciel contenant une capture d'un système de fichiers complet de système d'exploitation. Tout ce qui est nécessaire pour lancer un serveur virtuel viable est inclus.

Une image peut consister en un simple système d'exploitation de base comme Ubuntu Linux, ou le petit et super-rapide Alpine Linux. Mais une image peut également inclure des couches supplémentaires avec des applications logicielles comme des serveurs web et des bases de données. Peu importe le nombre de couches qu'une image a et la complexité des relations entre elles, l'image elle-même ne change jamais.

Lorsque, comme le montre la figure suivante, une image est lancée en tant que conteneur, une coucheritable supplémentaire est automatiquement ajoutée dans laquelle l'enregistrement de toute activité système en cours est sauvegardé.

![Image](https://cdn-media-1.freecodecamp.org/images/HoFgA8qtjPi3GFm8SWES3O33X0RfM8S3Vgrh)
_Une simple image Docker MySQL/Ubuntu illustrée avec sa couche de données inscriptible_

Que font couramment les gens avec leurs conteneurs Docker ? Souvent, ils chargent un projet de développement d'application pour tester son fonctionnement, puis le partagent avec les membres de l'équipe pour obtenir des commentaires et des mises à jour. Lorsque l'application est complète, elle peut être lancée en tant que cluster de conteneurs (ou « essaim » comme Docker l'appelle) qui peut être mis à l'échelle de manière programmatique et instantanée selon la demande des utilisateurs.

Bien que Docker soit une technologie basée sur Linux et nécessite un noyau Linux pour fonctionner, l'exécution de conteneurs Docker distants ou même locaux sur des machines Mac ou Windows est possible via les applications Docker pour Mac ou Docker pour Windows, ou pour les machines plus anciennes, via l'outil Docker Machine.

### Cloud computing

Le cloud computing est la fourniture de ressources informatiques, de mémoire et de stockage à la demande et en libre-service, à distance via un réseau.

Puisque les services basés sur le cloud sont facturés en très petites incréments, vous pouvez rapidement configurer et lancer une large gamme de projets. Et puisque les ressources sont toutes virtuelles, les lancer dans le cadre d'une expérience ou pour résoudre un problème à court terme aura souvent beaucoup de sens. Lorsque le travail est terminé, la ressource est fermée.

Les plateformes cloud vous permettent de faire des choses qui seraient impossibles — ou impossiblement coûteuses — ailleurs.

Vous n'êtes pas sûr de la durée de votre projet ou de la demande qu'il attirera ? Peut-être que l'achat, la construction et l'hébergement de tout le matériel coûteux dont vous auriez besoin pour soutenir correctement votre projet en interne ne peuvent pas être justifiés.

Investir lourdement dans des équipements de serveur, de refroidissement et de routage pourrait simplement ne pas avoir de sens.

Mais si vous pouviez louer juste assez de matériel de quelqu'un d'autre pour correspondre aux niveaux de demande changeant rapidement et ne payer que pour ce que vous utilisez réellement, alors cela pourrait fonctionner.

### AWS

Il n'y a pas de pénurie de moyens pour gérer les conteneurs Docker sur AWS. En fait, entre les frameworks, les interfaces d'orchestration, les dépôts d'images, et les solutions hybrides, la variété peut devenir confuse.

Cet article ne plongera pas profondément dans chaque option, mais vous devriez au moins être conscient de tous vos choix :

Le service [EC2 Container Service](https://aws.amazon.com/ecs/) (ECS) d'Amazon utilise des instances EC2 spécialement configurées comme hôtes pour des conteneurs Docker intégrés. Vous n'avez pas besoin de vous salir les mains sur l'instance EC2 elle-même, car vous pouvez provisionner et administrer vos conteneurs via le framework ECS. ECS offre maintenant une plus grande abstraction (et simplicité) grâce à leur option de mode Fargate.

[AWS CloudFormation](https://aws.amazon.com/cloudformation/) vous permet de configurer toute combinaison de ressources AWS dans un modèle qui peut être déployé une ou plusieurs fois. Vous pouvez inclure des dépendances spécifiées et des paramètres personnalisés dans le modèle. Étant donné sa conception autonome et scriptable, CloudFormation est un environnement naturel pour les déploiements Docker. En fait, Docker lui-même offre son service Docker pour AWS (actuellement en bêta), qui générera automatiquement un modèle CloudFormation pour orchestrer un essaim de conteneurs Docker pour fonctionner sur l'infrastructure AWS dans votre compte.

[AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) se place effectivement au-dessus de ECS. Il vous permet de déployer votre application sur toutes les ressources AWS normalement utilisées par ECS, mais avec pratiquement toute la logistique soigneusement abstraite. Effectivement, tout ce dont vous avez besoin pour lancer un environnement de microservices entièrement scalable et complexe est un script déclaratif au format JSON dans un fichier appelé `Dockerrun.aws.json`. Vous pouvez soit télécharger votre script vers l'interface graphique, soit, à partir d'un répertoire local initialisé en utilisant le CLI AWS Beanstalk.

[Amazon Elastic Container Service for Kubernetes](https://aws.amazon.com/eks/) (EKS) est actuellement encore en préversion. C'est un outil qui vous permet de gérer des conteneurs en utilisant l'orchestrateur open source Kubernetes, mais sans avoir à installer vos propres clusters. Comme ECS, EKS déployera toute l'infrastructure AWS nécessaire pour vos clusters sans intervention manuelle.

[Docker pour AWS](https://www.docker.com/docker-aws) est, au moment de l'écriture, toujours en bêta. En utilisant son interface navigateur, vous pouvez utiliser le service pour installer et exécuter un « essaim de Docker Engines » qui sont entièrement intégrés avec les services d'infrastructure AWS comme l'auto-scaling, l'équilibrage de charge (ELB), et le stockage par blocs.

Docker Datacenter (maintenant commercialisé dans le cadre de [Docker Enterprise Edition](https://www.docker.com/enterprise-edition)) est un projet conjoint AWS/Docker qui fournit aux clients commerciaux une interface plus personnalisable pour intégrer Docker avec les infrastructures AWS, Azure et IBM.

[Docker Cloud](https://cloud.docker.com/), beaucoup comme Docker Datacenter, offre une console basée sur un navigateur GUI pour gérer tous les aspects de vos déploiements Docker. Cela inclut l'administration pour vos nœuds hôtes fonctionnant dans des clouds publics. La grande différence est que, contrairement à Datacenter, le service d'administration Docker Cloud est hébergé sur son propre site. Il n'y a pas de logiciel serveur à installer sur votre propre équipement.

[Docker Hub](https://hub.docker.com/) est probablement le premier endroit évident pour rechercher et partager des images Docker. Fournis par Docker lui-même, Docker Hub contient une vaste collection d'images qui sont préchargées pour supporter tous types de projets d'applications. Vous pouvez trouver et rechercher des images sur le site web hub.docker.com, puis les extraire directement dans votre propre environnement Docker Engine.

[EC2 Container Registry](https://aws.amazon.com/ecr/) (ECR) est le propre registre d'images d'Amazon pour accompagner leur plateforme EC2 Container Service. Les images peuvent être poussées, extraites et gérées via l'interface graphique AWS ou l'outil CLI. Les politiques de permissions peuvent contrôler étroitement l'accès aux images uniquement pour les personnes que vous sélectionnez.

Je pense que vous êtes prêt à commencer. Si vous ne l'avez pas encore fait, rendez-vous sur le site Amazon Web Services pour créer un compte AWS. Au cas où vous ne seriez pas encore familier avec le fonctionnement de tout cela, les nouveaux comptes bénéficient d'une année complète de généreuse expérimentation avec tout niveau de service éligible pour le Free Tier. En supposant que vous êtes encore dans votre première année, rien de ce que nous allons faire dans ce cours ne devrait vous coûter un centime.

Ensuite, nous allons ouvrir Docker et voir comment il fonctionne à son niveau le plus basique : votre ligne de commande de portable. Techniquement, cela a très peu de pertinence pour les charges de travail AWS, mais ce sera un excellent moyen de mieux comprendre le flux de travail.

### Introduction à Docker

Visualiser correctement comment toutes les nombreuses parties d'AWS fonctionnent sera probablement plus facile si vous comprenez d'abord ce qui se passe sous le capot avec Docker lui-même. Donc dans cet article, je vais vous guider à travers le lancement et la configuration d'un simple conteneur Docker sur ma station de travail locale.

Prêt à partir ?

#### La ligne de commande Docker

Voyons comment cela fonctionne réellement. Je vais faire fonctionner Docker sur ma station de travail locale et ensuite le tester avec une opération rapide hello-world. Je vais ensuite extraire une vraie image Ubuntu fonctionnelle et l'exécuter.

Je ne vais pas passer par le processus d'installation de Docker sur votre machine ici pour plusieurs raisons. Tout d'abord, les spécificités varieront grandement en fonction du système d'exploitation que vous exécutez. Mais elles sont également susceptibles de changer fréquemment, donc tout ce que j'écris ici sera probablement obsolète dans peu de temps. Et enfin, tout cela n'est pas très pertinent pour AWS. Consultez les instructions de Docker à l'adresse [docs.docker.com/install](https://docs.docker.com/install).

En cours de route, j'essaierai certaines des outils de ligne de commande de Docker, y compris la création d'une nouvelle interface réseau et l'association d'un conteneur à celle-ci. Il s'agit du type de configuration d'environnement qui peut être très utile pour les déploiements réels impliquant plusieurs niveaux de ressources qui doivent être logiquement séparés.

La plupart des distributions Linux utilisent désormais [systemd](https://www.freedesktop.org/wiki/Software/systemd/) via la commande [systemctl](https://www.freedesktop.org/software/systemd/man/systemctl.html) pour gérer les processus. Dans ce cas, `systemctl start docker` lancera le démon Docker s'il n'est pas déjà en cours d'exécution. `systemctl status docker` retournera quelques informations utiles, y compris des messages d'erreur approfondis si quelque chose a mal tourné. Dans ce cas, tout semble sain.

```
# systemctl start docker# systemctl status docker
```

C'est la seule partie spécifique à Linux. À partir de maintenant, nous utiliserons des commandes qui fonctionneront partout où Docker est correctement installé.

#### Lancer un conteneur

L'exécution de commandes à partir de la ligne de commande Docker commence toujours par le mot « docker ». Le premier test normal d'un système nouvellement installé est d'utiliser `docker run` pour lancer une petite image — l'image « hello-world » spécialement conçue dans ce cas.

Comme vous pouvez le constater à partir de la sortie ci-dessous, Docker a d'abord recherché l'image sur le système local. Docker est particulièrement efficace de cette manière. Il essaiera toujours de réutiliser les éléments disponibles localement avant de se tourner vers des sources distantes.

Dans ce cas, comme il n'y a pas d'images existantes dans ce nouvel environnement, Docker va chercher à extraire hello-world de la bibliothèque officielle Docker.

```docker
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:66ef312bbac49c39a89aa9bcc3cb4f3c9e7de3788c9
44158df3ee0176d32b751
Status: Downloaded newer image for hello-world:latest2.1. 
Hello from Docker!
This message shows that your installation appears to be
working correctly. To generate this message, Docker took the
following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image
from the Docker Hub. (amd64)
3. The Docker daemon created a new container from that
image which runs the executable that produces the output you
are currently reading.
4. The Docker daemon streamed that output to the Docker client,
which sent it to your terminal.
To try something more ambitious, you can run an Ubuntu container
with:
$ docker run -it ubuntu bash
Share images, automate workflows, and more with a free Docker ID:
https://cloud.docker.com/
For more examples and ideas, visit:
https://docs.docker.com/engine/userguide/
```

La sortie complète de cette commande inclut une description utile en quatre parties de ce qui vient de se passer. Le client Docker a contacté le démon Docker qui a procédé au téléchargement de l'image hello-world depuis le dépôt. L'image est convertie en un conteneur en cours d'exécution par la commande docker run dont la sortie est diffusée vers notre shell de ligne de commande — le client Docker.

Permettez-moi de décomposer ce jargon pour vous un peu :

* **Client Docker** — le shell de ligne de commande activé en exécutant des commandes docker
* **Démon Docker** — le processus Docker local que nous avons démarré juste avant avec la commande `systemctl`
* **Image** — un fichier contenant les données qui seront utilisées pour composer un système d'exploitation

Taper simplement `docker` imprimera une liste utile de commandes courantes avec de brèves descriptions, et `docker info` retournera des informations sur l'état actuel de notre client Docker.

Remarquez comment nous avons actuellement un conteneur et une image (le conteneur hello-world) et qu'il n'y a zéro conteneur en cours d'exécution en ce moment.

```docker
$ docker info
Containers: 1
Running: 0
Paused: 0
Stopped: 1
Images: 3
Server Version: 1.13.1
Storage Driver: aufs
Root Dir: /var/lib/docker/aufs
Backing Filesystem: extfs
Dirs: 28
Dirperm1 Supported: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
Volume: local
Network: bridge host macvlan null overlay
```

#### Sessions de conteneurs interactives

Essayons la commande « plus ambitieuse » `docker run -it ubuntu bash` que la documentation Docker a précédemment suggérée. Cela téléchargera la dernière image de base Ubuntu officielle et l'exécutera en tant que conteneur.

L'option `-i` rendra la session interactive, ce qui signifie que vous serez placé dans un shell en direct au sein du conteneur en cours d'exécution où vous pourrez contrôler les choses comme vous le feriez sur n'importe quel autre serveur. L'argument `-t` ouvrira un shell TTY.

```docker
$ docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
1be7f2b886e8: Pull complete
6fbc4a21b806: Pull complete
c71a6f8e1378: Pull complete
4be3072e5a37: Pull complete
06c6d2f59700: Pull complete
Digest: sha256:e27e9d7f7f28d67aa9e2d7540bdc2b33254
b452ee8e60f388875e5b7d9b2b696
Status: Downloaded newer image for ubuntu:latest
root@c81a051f6f03:/#
```

Notez la nouvelle invite de commande `root@c81a051f6f03:/#`. Nous sommes maintenant réellement à l'intérieur d'un conteneur Docker minimal mais fonctionnel.

Nous pouvons, par exemple, mettre à jour nos index de dépôt de logiciels.

```
# ls
bin dev home lib64 mnt proc run srv tmp var boot etc lib media opt root sbin sys usr
# apt update
Get:1 http://security.ubuntu.com/ubuntu xenial-security InRelease
Get:2 http://archive.ubuntu.com/ubuntu xenial InRelease
[]
Fetched 24.8 MB in 48s (515 kB/s)
Reading package lists Done
Building dependency tree
Reading state information Done
6 packages can be upgraded. Run 'apt list  upgradable' to
see them.
```

Si je quitte le conteneur, il s'éteindra et je me retrouverai sur mon serveur hôte. En tapant `docker info` une fois de plus, je vois maintenant deux conteneurs arrêtés plutôt qu'un seul.

```
$ docker infoContainers: 2Running: 0Paused: 0Stopped: 2Images: 4[]
```

#### Exécution de conteneurs en arrière-plan

Je pourrais lancer un conteneur en arrière-plan en ajoutant l'option `detach=true` qui retournera un ID de conteneur. La liste de tous les conteneurs Docker actifs avec `ps` me montrera alors mon nouveau conteneur **en cours d'exécution**.

```
$ docker info
Containers: 2
Running: 0
Paused: 0
Stopped: 2
Images: 4
[]
```

#### Gestion des conteneurs

Comme vous pouvez le voir à partir du nom `wizardly_pasteur`, les personnes qui ont conçu Docker ont compilé un ensemble plutôt excentrique de noms à attribuer à vos conteneurs. Si vous souhaitez renommer un conteneur — peut-être pour que sa gestion nécessite moins de frappe — exécutez `docker rename`, suivi du nom actuel du conteneur et du nouveau nom que vous souhaitez lui donner. Je vais exécuter `docker ps` une fois de plus pour montrer la mise à jour en action.

```js
$ docker rename wizardly_pasteur MyContainer
$ docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS NAMES
232a83013d39 ubuntu "bash" 3 minutes ago Up 5 minutes MyContainer
```

`docker inspect` suivi d'un nom de conteneur, retournera des pages et des pages d'informations utiles sur la configuration et l'environnement de ce conteneur. L'extrait de sortie que j'ai inclus ci-dessous affiche les détails de l'environnement réseau du conteneur. Notez que la passerelle réseau est `172.17.0.1` et que l'adresse IP réelle du conteneur est `172.17.0.2` — cela sera utile plus tard.

```
$ docker inspect MyContainer
[...]
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
[...]
```

#### Réseaux Docker

`docker network ls` listera toutes les interfaces réseau actuellement associées à notre client Docker. Notez en particulier l'interface `bridge` qui connecte un conteneur à l'hôte Docker, permettant la communication réseau vers et depuis le conteneur.

```
$ docker network ls
NETWORK ID          NAME            DRIVER        SCOPE
fa4da6f158de        bridge          bridge        local
18385f695b4e        host            host          local
6daa514c5756        none            null          local
```

Nous pouvons créer une nouvelle interface réseau en exécutant `docker network create` suivi du nom que nous souhaitons donner à notre nouvelle interface. Exécuter `inspect` sur la nouvelle interface nous montre — via la valeur `Driver` — que cette nouvelle interface a été automatiquement associée au réseau `bridge` que nous avons vu précédemment, mais existe sur son propre réseau `172.18.0.x`. Vous vous souviendrez que notre réseau par défaut utilisait `172.17.0.x`.

```
$ docker network create newNet
715f775551522c43104738dfc2043b66aca6f2946919b39ce
06961f3f86e33bb
$ docker network inspect newNet
[
    {
        "Name": "newNet",
 [...]
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
 [...]
]
```

Confus ? Mon livre Solving for Technology a un [chapitre sur les bases du réseau TCP/IP](https://learntech.bootstrap-it.com/chapter7.html).

#### Déplacement de conteneurs entre réseaux

Vous pourriez parfois vouloir déplacer un conteneur existant d'un réseau à un autre — peut-être avez-vous besoin de réorganiser et de mieux sécuriser vos ressources. Essayez-le en déplaçant ce conteneur Ubuntu vers un réseau différent, comme l'interface `newNet` que nous venons de créer. Utilisez `docker network connect` suivi du nom du réseau `newNet` et ensuite du nom du conteneur `MyContainer`.

```
$ docker network connect newNet MyContainer
```

Exécuter `inspect` sur le conteneur une fois de plus vous montrera que `MyContainer` est maintenant connecté **à la fois** à l'interface `bridge` avec son adresse `172.17.0.2`, **et** à l'interface `newNet` sur `172.18.0.2`. C'est maintenant comme un ordinateur avec deux cartes d'interface réseau physiquement connectées à des réseaux séparés.

Vous ne me croyez pas ? Vous pouvez réussir à `ping` les deux interfaces depuis la ligne de commande, donc nous pouvons voir qu'elles sont toutes deux actives. Tout cela a été possible, d'ailleurs, malgré le fait que le conteneur était en cours d'exécution tout le temps. N'essayez pas cela sur une machine physique !

```
$ ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.103 ms
64 bytes from 172.17.0.2: icmp_seq=2 ttl=64 time=0.070 ms
^C
   172.17.0.2 ping statistics  -
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.070/0.086/0.103/0.018 ms
$ ping 172.18.0.2
PING 172.18.0.2 (172.18.0.2) 56(84) bytes of data.
64 bytes from 172.18.0.2: icmp_seq=1 ttl=64 time=0.079 ms
64 bytes from 172.18.0.2: icmp_seq=2 ttl=64 time=0.062 ms
^C
   172.18.0.2 ping statistics  -
2 packets transmitted, 2 received, 0% packet loss, time 999ms
rtt min/avg/max/mdev = 0.062/0.070/0.079/0.011 ms
```

#### Travailler avec les Dockerfiles

Bien que les conteneurs puissent être définis et contrôlés à partir de la ligne de commande, le processus peut être largement automatisé via des scripts appelés [Dockerfiles](https://docs.docker.com/engine/reference/builder/). Exécuter `Dockerfile` dans le cadre d'une opération de construction Docker indiquera à Docker de créer un conteneur en utilisant les configurations spécifiées par le script.

Dans l'exemple de `simple dockerfile` affiché ci-dessous, la ligne `FROM` indique à l'hôte Docker d'utiliser Ubuntu version 16.04 comme système d'exploitation de base. Si une image Ubuntu 16.04 n'existe pas déjà sur le système local, Docker en téléchargera une.

```
# Simple Dockerfile
FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y apache2
RUN echo "Welcome to my web site" > /var/www/html/index.html
EXPOSE 80
```

Chacune des lignes `RUN` lance une commande au sein du système d'exploitation dont les résultats seront inclus dans le conteneur — même avant qu'il ne soit réellement lancé en tant que machine virtuelle active.

Dans ce cas, `apt-get update` met à jour les index de dépôt locaux pour permettre les téléchargements de logiciels, `apt-get install apache2` téléchargera et installera le paquet du serveur web Apache. Le `-y` répondra automatiquement « oui » à toute invite incluse dans le processus d'installation.

La commande `echo` remplacera le contenu du fichier `index.html` par mon texte personnalisé `Welcome`. `index.html` est, bien sûr, le premier fichier qu'un navigateur recherchera et chargera ensuite lorsqu'il visitera un nouveau site.

Enfin, `EXPOSE 80` ouvre le port 80 sur le conteneur pour permettre le trafic HTTP — nécessaire car ce sera un serveur web. Cela nous permettra d'accéder au serveur web depuis la machine hôte Docker. Ce sera votre responsabilité de fournir l'accès à votre hôte pour tout client distant que vous pourriez vouloir inviter.

Si vous êtes au courant des dernières nouvelles sur la gestion des paquets Ubuntu, vous saurez qu'il y a eu un changement de `apt-get` vers son nouveau remplacement `apt`. Alors pourquoi ai-je utilisé `apt-get` dans ce `Dockerfile` ? Parce qu'il est encore plus fiable pour une utilisation dans des environnements scriptés.

Pour créer réellement un conteneur basé sur ce Dockerfile, vous exécutez `docker build` avec `-t` pour créer un nom (ou une « étiquette ») pour le conteneur. Je vais opter pour `webserver`. Vous ajoutez un espace et ensuite un point pour indiquer à Docker de lire le fichier nommé `Dockerfile` trouvé dans ce répertoire actuel. Docker se mettra immédiatement au travail pour construire un conteneur sur la base de l'image Ubuntu que nous avons extraite précédemment, et exécuter les commandes `apt-get` et `echo`.

```
$ docker build -t "webserver" .
Sending build context to Docker daemon 2.048 kB
Step 1/5 : FROM ubuntu:16.04
16.04: Pulling from library/ubuntu
Digest: sha256:e27e9d7f7f28d67aa9e2d7540bdc2b33254b452ee8e
60f388875e5b7d9b2b696
Status: Downloaded newer image for ubuntu:16.04
  -> 0458a4468cbc
Step 2/5 : RUN apt-get update
  -> Running in c25f5462e0f2
[]
Processing triggers for systemd (2294ubuntu21) 
Processing triggers for sgml-base (1.26+nmu4ubuntu1) 
  -> 3d9f2f14150e
Removing intermediate container 42cd3a92d3ca
Step 4/5 : RUN echo "Welcome to my web site" > 
/var/www/html/index.html
  -> Running in ddf45c195467
  -> a1d21f1ba1f6
Removing intermediate container ddf45c195467
Step 5/5 : EXPOSE 80
  -> Running in af639e6b1c85
  -> 7a206b180a62
Removing intermediate container af639e6b1c85
Successfully built 7a206b180a62
```

Si j'exécute `docker images`, je verrai maintenant une version de mon image Ubuntu avec le nom `webserver`.

```
$ docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
webserver latest 7a206b180a62 3 minutes ago 250 MB
ubuntu 16.04 0458a4468cbc 12 days ago 112 MB
hello-world latest f2a91732366c 2 months ago 1.85 kB
```

Maintenant, nous sommes prêts à lancer le conteneur en utilisant `docker run`.

Structurer cette commande correctement est un processus un peu délicat et il y a beaucoup de choses qui peuvent mal tourner. L'argument `-d` indique à Docker d'exécuter ce conteneur en mode détaché, ce qui signifie que nous ne nous retrouverons pas sur la ligne de commande du conteneur, mais qu'il s'exécutera en arrière-plan. `-p` indique à Docker de transférer tout le trafic arrivant **sur** le port `80` (le port HTTP par défaut) **vers** le port `80` sur le conteneur. Cela permet un accès externe au serveur web. Je ne peux pas dire que je comprends pourquoi, mais l'ordre ici est crucial : ajoutez l'argument `-p` **après** `-d`.

Ensuite, nous indiquons à Docker le nom du conteneur que nous souhaitons lancer, `webserver` dans notre cas. Et après cela, nous indiquons à Docker d'exécuter une seule commande une fois le conteneur en cours d'exécution pour démarrer le serveur web Apache.

```
$ docker run -d -p 80:80 webserver \ /usr/sbin/apache2ctl -D FOREGROUND
```

Peut-être vous demandez-vous pourquoi je n'ai pas utilisé la commande plus moderne `Systemd` `systemctl start apache`. Eh bien, j'ai essayé et j'ai découvert que, à ce stade au moins, systemd est bien et cassé dans les conteneurs Docker Ubuntu. Restez à l'écart si vous savez ce qui est bon pour vous. `-D FOREGROUND` garantit qu'Apache — et le conteneur dans son ensemble — restera en cours d'exécution même une fois le lancement terminé. Exécutez-le vous-même.

On nous donne un ID pour le nouveau conteneur, mais rien d'autre. Vous pouvez exécuter `docker ps` et vous devriez voir notre `webserver` parmi la liste de tous les conteneurs en cours d'exécution. Vous devriez également pouvoir ouvrir la page `index.html` du serveur web en pointant votre navigateur vers l'adresse IP du conteneur.

Quoi ? Vous **ne connaissez pas** l'adresse IP de votre conteneur ? Eh bien, puisque le conteneur aura été associé au réseau `bridge` par défaut, vous pouvez utiliser `docker network inspect bridge` et, dans la section Containers de la sortie, vous devriez trouver ce que vous cherchez. Dans mon cas, c'était `172.17.0.3`.

#### Travailler avec les images Docker Hub

Nous avons déjà profité de certains des avantages que Docker Hub a à offrir. Les images que nous avons utilisées pour construire les conteneurs dans les clips précédents ont toutes été téléchargées de manière transparente depuis Docker Hub en arrière-plan.

En fait, en utilisant quelque chose comme `docker search apache2`, vous pouvez parcourir manuellement le dépôt pour des images disponibles publiquement qui viennent avec Apache préinstallé. Vous pouvez également parcourir ce qui est disponible sur le site web [Docker Hub](https://hub.docker.com/).

Cependant, vous devez vous rappeler que toutes ces images ne sont pas fiables ou même sûres. Vous voudrez rechercher des résultats qui ont obtenu beaucoup d'étoiles de révision et, en particulier, sont désignés comme « officiels ». L'exécution de `docker search ubuntu` retourne au moins quelques images officielles.

Trouvez quelque chose qui vous intéresse ? Vous pouvez l'ajouter à votre collection locale en utilisant `docker pull`. Une fois le téléchargement terminé, vous pouvez afficher vos images en utilisant `docker images`.

```
$ docker pull ubuntu-upstart
```

Pendant que vous êtes sur le site Docker Hub, prenez le temps de créer un compte gratuit. Cela vous permettra de stocker et de partager vos propres images de la même manière que vous pourriez utiliser un outil comme GitHub. Il s'agit probablement du cas d'utilisation le plus populaire pour Docker, car il permet aux membres de l'équipe travaillant à distance — ou aux développeurs paresseux travaillant dans le même bureau — d'obtenir un accès instantané et fiable aux environnements exacts utilisés à chaque étape de l'avancement d'un projet.

Ce sont les bases essentielles, et il est important de les comprendre clairement. Mais, en raison de la complexité impliquée dans la coordination de clusters de dizaines ou de milliers de conteneurs tous à la fois, la plupart des charges de travail sérieuses de conteneurs n'utiliseront pas ces outils particuliers de ligne de commande.

Au lieu de cela, vous allez probablement vouloir un framework plus robuste et riche en fonctionnalités. Vous pouvez lire à propos de certains de ces outils — y compris le mode Docker Swarm de Docker, Docker Enterprise Edition, ou Docker Cloud, et Kubernetes — dans mon article, « [Trop de choix : comment choisir le bon outil pour gérer vos clusters Docker](https://hackernoon.com/too-many-choices-how-to-pick-the-right-tool-to-manage-your-docker-clusters-b5b3061b84b7) ».

_Cet article est largement basé sur [des cours vidéo que j'ai créés pour Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton). J'ai également beaucoup de contenu Docker, AWS et Linux disponible via mon [site web](https://bootstrap-it.com/), y compris des liens vers mon livre, [Linux in Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9), et un cours hybride appelé [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui est composé de plus de deux heures de vidéo et d'environ 40 % du texte de Linux in Action._