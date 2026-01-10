---
title: Un guide pratique des conteneurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T19:56:47.000Z'
originalURL: https://freecodecamp.org/news/a-practical-guide-to-containers-dfa66d37ac30
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BNdwczuGtUJQLjgi2EaxZg.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un guide pratique des conteneurs
seo_desc: 'By Julius Zerwick

  Containers have taken over the software world by storm — and for good reason.

  They’ve proven vital for DevOps and deployment, and have a multitude of uses for
  developers. And this goes not only for large companies, but for independe...'
---

Par Julius Zerwick

Les conteneurs ont conquis le monde du logiciel par la tempête — et pour de bonnes raisons.

Ils se sont avérés vitaux pour le DevOps et le déploiement, et ont une multitude d'utilisations pour les développeurs. Et cela ne concerne pas seulement les grandes entreprises, mais aussi les développeurs indépendants. En fait, les conteneurs ont joué un rôle vital dans le développement et le déploiement de notre projet [SpaceCraft](https://spacecraft-repl.com).

Dans cet article, nous allons donner une introduction aux conteneurs et expliquer leurs fonctionnalités principales. Nous allons ensuite montrer leurs utilisations dans le développement logiciel et couvrir quelques sujets importants concernant la sécurité et la gestion des ressources. En cours de route, nous donnerons un aperçu de [comment les conteneurs ont été utilisés dans SpaceCraft](https://spacecraft-repl.com/whitepaper#5-securite--gestion-des-ressources-avec-les-conteneurs). Commençons !

### Qu'est-ce qu'un conteneur ?

Alors, qu'est-ce qu'un conteneur exactement ?

À sa base, un conteneur peut être décrit comme une unité unique de logiciel encapsulé. C'est essentiellement une boîte dans laquelle vous pouvez placer toutes les dépendances de votre projet et exécuter un seul service ou un environnement de développement entier, tout en gardant tout ce qui se trouve à l'intérieur de la boîte isolé du système hôte.

![Image](https://cdn-media-1.freecodecamp.org/images/GTyN5psx6tnP8jU-X7MRTTZULVVcq12QmoMe)

Par exemple, imaginez que vous devez travailler sur un nouveau projet et que vous connaissez toutes les dépendances nécessaires. Mais certaines de ces dépendances peuvent entrer en conflit avec ce que vous avez déjà installé sur votre ordinateur, comme un numéro de version de langage.

Si vous deviez travailler sur le projet sur votre ordinateur, vous devriez passer par le processus fastidieux de gestion de vos dépendances et de désactivation des versions tout en activant les versions dont vous avez besoin.

Ce problème est aggravé lorsqu'il s'agit d'une équipe entière de développeurs travaillant sur le même projet, et aucun des deux développeurs n'a les mêmes configurations sur leur ordinateur.

Avec un conteneur, vous pouvez simplement mettre toutes vos dépendances nécessaires à l'intérieur et ensuite travailler sur votre projet depuis le conteneur. Cela permet d'éviter beaucoup de maux de tête en éliminant les problèmes de gestion des dépendances et en nous fournissant plutôt une zone isolée pour travailler.

### Comment sont fabriqués les conteneurs ?

Nous savons maintenant ce qu'est un conteneur. Mais comment les créons-nous exactement ?

Eh bien, pour commencer, nous devons créer une image. Il s'agit simplement d'un package qui inclut toutes les dépendances qui doivent exister dans notre conteneur. C'est un instantané de tout ce qui doit se trouver à l'intérieur de notre conteneur lorsque nous l'exécutons.

![Image](https://cdn-media-1.freecodecamp.org/images/4ONl-2xcwZXUBC3VFRjgGYPUO0SDakgpy1Na)

Une façon simple de visualiser cela est de penser à une image comme une classe et à un conteneur comme un objet qui est instancié à partir de cette classe. Ainsi, notre image servira de plan pour créer nos conteneurs, et nous pouvons créer un nombre quelconque de conteneurs identiques à partir de la même image.

### Comment sont construites les images ?

Les images sont construites en [exécutant un ensemble de commandes](https://www.aquasec.com/wiki/display/containers/Docker+Images+101). Dans Docker, l'ensemble des commandes est écrit dans un fichier texte appelé Dockerfile.

Lorsque le processus de construction de l'image commence, chaque commande [forme une couche](https://docs.docker.com/storage/storagedriver/#images-and-layers) qui compose l'image finale. La dernière couche spécifie quelle commande exécuter dans un conteneur lorsqu'un conteneur est démarré.

![Image](https://cdn-media-1.freecodecamp.org/images/rfC-aIsKtyAL5VruQcu34TTlATH4FZsqGekJ)
_Un exemple de Dockerfile qui construit une image. Chaque couche représente une instruction du Dockerfile._

Dans [SpaceCraft](https://spacecraft-repl.com), nous avons regroupé une [version modifiée d'Ubuntu](https://hub.docker.com/r/phusion/baseimage/), nos environnements d'exécution de langage et une copie de notre code d'application dans une image pour démarrer plusieurs conteneurs qui exécutent chacun une instance de notre application.

Les images n'ont pas nécessairement besoin d'être stockées ou construites uniquement sur votre machine locale. Les conteneurs sont conçus pour être déployables n'importe où et ainsi nous devrions pouvoir accéder à nos images depuis n'importe quelle machine physique. Cela est accompli grâce aux [registres](https://docs.docker.com/registry/introduction/#understanding-image-naming), qui sont essentiellement un endroit pour stocker et accéder aux images à distance.

### Pourquoi devrions-nous utiliser des conteneurs ?

Maintenant, nous pouvons plonger dans les nombreux cas d'utilisation des conteneurs.

Vous vous souvenez comment nous avons dit que les conteneurs peuvent nous fournir une boîte isolée pour contenir un environnement de développement avec un ensemble spécifique de dépendances ? Chaque développeur peut simplement télécharger l'image nécessaire depuis un registre sur son ordinateur local et ensuite créer un conteneur à partir de cette image.

De cette façon, ils peuvent commencer à contribuer à des projets existants en un rien de temps.

#### Facilité de déploiement

Comme vous pouvez le voir, l'un des plus grands avantages des conteneurs est qu'ils sont facilement déployables sur une variété de systèmes, grâce à leur isolation. Cela permet aux développeurs de découpler leur logiciel de leurs machines physiques et de lancer un conteneur depuis n'importe où.

#### Exécuter plusieurs services sur une seule machine

Un autre cas d'utilisation implique de placer un seul service dans un conteneur et ensuite de communiquer avec ce service.

Dans cette situation, vous pouvez construire un système qui héberge des services individuels dans des conteneurs séparés. Cela vous permet d'isoler chaque partie de votre architecture système et d'exécuter plusieurs services sur le même hôte tout en facilitant l'échange de services dans et hors de votre système selon les besoins.

Pour démontrer comment cela fonctionne, chaque service peut communiquer avec les autres via [Docker container networking](https://docs.docker.com/v17.09/engine/userguide/networking/) par leurs adresses IP. Avec cela, les conteneurs peuvent, par exemple, envoyer des requêtes HTTP avec l'adresse IP du conteneur de destination comme partie de l'URL.

![Image](https://cdn-media-1.freecodecamp.org/images/uLp2wy8wRF0OP2ovvggkNzh42OvFbkmdGIwu)
_Les conteneurs peuvent communiquer les uns avec les autres via leurs adresses IP._

En fait, nous utilisons cette technique dans [SpaceCraft](https://spacecraft-repl.com). Nous avons construit un [serveur proxy inverse](https://www.incapsula.com/cdn-guide/glossary/reverse-proxy.html) qui redirige les requêtes des clients vers les conteneurs appropriés. Pour permettre la communication entre notre serveur proxy inverse et les conteneurs, nous récupérons les adresses IP des conteneurs lors de l'initialisation et les utilisons comme destinations pour le proxy.

#### Isolation pour la sécurité

Un autre cas d'utilisation important est que les applications conteneurisées sont isolées du système hôte. Cela empêche l'accès non souhaité des utilisateurs au système de fichiers de l'hôte. Cela est important, surtout pour une application comme [SpaceCraft](http://repl.space) qui donne aux utilisateurs la possibilité d'exécuter du code.

Nous pouvons également ajouter des mesures de sécurité pour renforcer l'isolation et empêcher davantage les activités malveillantes d'atteindre notre système hôte. Nous explorerons ces stratégies dans la section suivante.

### Conteneurs versus machines virtuelles

À ce stade, nous voulons clarifier la distinction entre les conteneurs et les machines virtuelles, car cela peut fortement influencer votre décision sur lequel utiliser.

Les machines virtuelles sont apparues avant les conteneurs et étaient utilisées pour répondre aux mêmes points de douleur que les conteneurs. Essentiellement, elles fournissent un environnement isolé pour les services et le développement et sont déployables sur plusieurs systèmes.

Cependant, il existe des différences significatives entre eux et les conteneurs.

#### Les conteneurs sont plus légers et plus rapides à démarrer

Tout d'abord, les conteneurs sont plus légers en termes de besoins en mémoire que les machines virtuelles. Selon ce que vous placez dans un conteneur, ils fonctionnent généralement en dizaines à centaines de Mo pour la taille de la mémoire.

Les machines virtuelles sont beaucoup plus lourdes et fonctionnent en Go. Cela est principalement dû à une grande inclusion : le noyau du système d'exploitation.

![Image](https://cdn-media-1.freecodecamp.org/images/binzfjGViQTJIpQs3d9UUIxsgl62HClcJOac)
_Source : [Je suis un développeur : pourquoi devrais-je utiliser Docker ?](https://blog.octo.com/en/i-am-a-developer-why-should-i-use-docker" rel="noopener" target="_blank" title=")_

Les machines virtuelles contiennent non seulement toutes vos dépendances pour votre service ou environnement, mais aussi une copie complète d'un noyau de système d'exploitation pour exécuter toutes vos dépendances. Cette addition peut ajouter beaucoup de mémoire à une instance de machine virtuelle.

D'autre part, les conteneurs ne contiennent pas de noyau et font plutôt des appels système au noyau du système hôte. Cela réduit considérablement leur empreinte mémoire. Cela permet de créer et d'utiliser plus de conteneurs sur un système, par opposition au nombre de machines virtuelles que vous pouvez exécuter sur le même système.

En plus d'une empreinte mémoire plus petite, l'absence de noyau dans un conteneur rend leur temps de démarrage beaucoup plus rapide. Le démarrage d'un conteneur peut se faire en quelques secondes, alors que les machines virtuelles prendront beaucoup plus de temps.

#### Les machines virtuelles sont plus sécurisées par défaut

Cependant, il y a toujours des compromis. En ce qui concerne les machines virtuelles par rapport aux conteneurs, le grand compromis est la sécurité.

Parce que les conteneurs ont besoin d'accéder au noyau du système hôte pour faire des appels système, ils ne sont pas aussi étanches en matière de sécurité qu'une machine virtuelle.

En fait, des utilisateurs malveillants ingénieux peuvent trouver des moyens d'utiliser cet inconvénient de sécurité pour sortir d'un conteneur et accéder au système hôte.

Avec les machines virtuelles, ce risque est atténué car chaque instance de machine virtuelle contient un noyau pour ses appels système. Ainsi, il y a une isolation plus forte entre une machine virtuelle et le système hôte qu'avec un conteneur.

Cependant, les risques de sécurité des conteneurs peuvent être abordés en mettant en œuvre quelques mesures de sécurité que nous avons incorporées dans [SpaceCraft](https://spacecraft-repl.com), que nous allons examiner maintenant.

### Mesures de sécurité

Un énorme problème de sécurité que vous devez connaître est que les utilisateurs exécutent généralement en tant qu'utilisateurs root dans les conteneurs par défaut.

Cela signifie que toute personne qui travaille à l'intérieur d'un conteneur, qu'il s'agisse d'un développeur de votre équipe ou d'un utilisateur qui utilise une application hébergée dans un conteneur en arrière-plan, aura un accès privilégié au système de fichiers du conteneur.

Si vous êtes préoccupé par le fait de donner ce niveau de contrôle à l'utilisateur du conteneur, alors vous devriez envisager des moyens de limiter leurs privilèges.

Ce problème peut être résolu en créant un profil utilisateur non privilégié dans le système de fichiers du conteneur, et en faisant en sorte que les utilisateurs exécutent en tant que ce profil utilisateur tout en étant dans le conteneur.

Cela limitera leur capacité à accéder au système de fichiers du conteneur et à exécuter des commandes qui pourraient nuire à votre environnement de conteneur et à tout service s'exécutant à l'intérieur.

Un autre problème de sécurité qui peut se poser est la capacité des utilisateurs à sortir des conteneurs et à accéder au système de fichiers du système hôte.

Comme nous l'avons mentionné précédemment, les conteneurs font des appels système au noyau du système hôte afin d'exécuter des processus. Cela ouvre la porte aux utilisateurs malveillants pour sortir d'un conteneur et attacher le système hôte.

![Image](https://cdn-media-1.freecodecamp.org/images/WZ5jhJvKBZOluHlpS9dKrdvRy5THnryb24ts)
_La conteneurisation seule fournit une isolation faible, où tous les appels système effectués par notre application sont acceptés par le noyau hôte. Source : [gVisor Github](https://github.com/google/gvisor" rel="noopener" target="_blank" title=")_

L'une des méthodes que nous utilisons pour prévenir cette situation est d'utiliser un bac à sable d'exécution de conteneur pour intercepter les appels système effectués par un conteneur. Le bac à sable agit comme un noyau invité et crée un niveau d'isolation fort entre le conteneur et le noyau hôte. Cela empêche les utilisateurs malveillants d'attaquer notre système hôte.

Si vous êtes intéressé par l'utilisation d'un bac à sable d'exécution de conteneur, consultez [gVisor](https://github.com/google/gvisor) qui est une solution open-source fournie par Google que nous avons utilisée avec [SpaceCraft](https://spacecraft-repl.com).

### Contrôle des ressources des conteneurs

Un autre problème que nous voulons aborder concerne l'abus potentiel des ressources d'un conteneur.

Puisqu'un conteneur s'exécute sur un système hôte et utilise le noyau hôte, il consomme essentiellement des ressources CPU et mémoire du système hôte pour compléter ses processus et tâches.

Bien que cela ne soit généralement pas un problème au niveau individuel avec les développeurs utilisant des conteneurs, cela devient un problème plus important une fois que nous utilisons des conteneurs pour déployer des applications à utiliser par des utilisateurs externes.

Supposons que votre architecture système inclut l'utilisation de conteneurs pour exécuter des instances séparées de votre application que les utilisateurs peuvent accéder. Et quelque chose se produit avec l'une de ces instances conteneurisées qui nécessite plus de CPU et de mémoire du système hôte que prévu.

Ce à quoi cela peut aboutir est qu'une instance accapare les ressources système au détriment des autres instances, ce qui entraîne une baisse de leurs performances et crée une mauvaise expérience utilisateur.

Évidemment, c'est une situation que nous voulons éviter si possible. Heureusement, nous pouvons le faire avec les cgroups, qui est l'abréviation de « control groups ».

Avec les cgroups, vous pouvez limiter la quantité de ressources système utilisées par un conteneur et ainsi prévenir la situation que nous venons de décrire.

Par exemple, vous pouvez définir les cgroups sur un conteneur pour être un maximum de 100 Mo de mémoire et 20 % de CPU. Avec ces limites définies, ce conteneur ne pourra jamais utiliser plus de 100 Mo de mémoire ou utiliser plus de 20 % de CPU du système hôte pour sa durée de vie. Vous pouvez être tranquille en sachant que les performances de vos autres instances d'application conteneurisées ne diminueront pas.

Dans SpaceCraft, nous avons utilisé les cgroups pour limiter la quantité maximale de mémoire et de CPU qu'une seule session peut consommer. Si une session arrive à exécuter un calcul coûteux et à consommer toutes les ressources disponibles dans ce conteneur, seule cette session sera affectée.

![Image](https://cdn-media-1.freecodecamp.org/images/GVqFqcXMbtyeqoFz37VjUoH-Ge-keD5nstpE)
_Avec chaque session isolée et contrôlée via les cgroups, un seul pic de consommation de ressources n'affectera que cette session, tout en laissant les autres intactes._

### Par où commencer ?

Il existe de nombreux services de conteneurs parmi lesquels vous pouvez choisir. Nous avons utilisé Docker pour [SpaceCraft](https://spacecraft-repl.com) en raison de sa facilité d'utilisation et de sa documentation excellente. Nous le recommandons vivement pour votre prochain projet.

D'autres options incluent :

* Redhat OpenShift
* Amazon EC2 Container Service
* AWS Elastic Container Registry
* Google Cloud Container Registry
* Azure Kubernetes
* HashiCorp
* Quay

#### Intégration avec Node.js

Si vous utilisez principalement Node.js pour votre développement, [Dockerode](https://github.com/apocas/dockerode) peut vous aider à interagir avec Docker depuis un environnement Node.js. Nous avons utilisé Dockerode pour nous aider à effectuer certaines actions importantes sur les conteneurs, notamment :

* Démarrer et détruire un conteneur
* Lire l'adresse IP d'un conteneur
* Placer des limites sur l'utilisation de la mémoire et du CPU d'un conteneur

Ces opérations sont importantes pour nous aider à gérer plusieurs sessions et à mettre à l'échelle notre application.

### Conclusion

Les conteneurs sont un outil extrêmement utile dans votre arsenal en tant que développeur logiciel pour simplifier et accélérer le déploiement de votre projet.

Qu'il s'agisse de créer un environnement de développement isolé pour construire des projets, de mettre en place une architecture de microservices ou d'aider à intégrer un nouveau membre de l'équipe, l'utilité des conteneurs continue de croître avec le temps. Essayez-les dans votre prochain projet et voyez comment ils peuvent vous bénéficier !

Si vous avez aimé lire cet article, nous avons également écrit une étude de cas détaillée sur la façon dont nous avons construit SpaceCraft et les défis auxquels nous avons été confrontés. Vous pouvez [la lire ici](https://spacecraft-repl.com/whitepaper).

_Co-écrit par Julius, Gooi et Nick de l'équipe [SpaceCraft](https://spacecraft-repl.com/team)._

### Références

- [Qu'est-ce qu'un conteneur](https://www.docker.com/resources/what-container)  
- [Je suis un développeur : pourquoi devrais-je utiliser Docker ?](https://blog.octo.com/en/i-am-a-developer-why-should-i-use-docker/)  
- [Meilleures pratiques de sécurité Docker](https://dev.to/petermbenjamin/docker-security-best-practices-45ih)  
- [Open-sourcing gVisor, un runtime de conteneur en bac à sable](https://cloud.google.com/blog/products/gcp/open-sourcing-gvisor-a-sandboxed-container-runtime)  
- [Pourquoi est-il recommandé d'exécuter un seul processus dans un conteneur ?](https://devops.stackexchange.com/questions/447/why-it-is-recommended-to-run-only-one-process-in-a-container)  
- [Les processus dans les conteneurs ne doivent pas s'exécuter en tant que root](https://medium.com/@mccode/processes-in-containers-should-not-run-as-root-2feae3f0df3b)  
- [Sécurité et machines virtuelles](https://pubs.vmware.com/vsphere-4-esx-vcenter/index.jsp?topic=/com.vmware.vsphere.server_configclassic.doc_40/esx_server_config/security_for_esx_systems/c_security_and_virtual_machines.html)