---
title: Apprenez Kubernetes et commencez à conteneuriser vos applications
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-01-19T17:58:49.000Z'
originalURL: https://freecodecamp.org/news/learn-kubernetes-and-start-containerizing-your-applications
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/KUBERNETES.png
tags:
- name: Kubernetes
  slug: kubernetes
- name: youtube
  slug: youtube
seo_title: Apprenez Kubernetes et commencez à conteneuriser vos applications
seo_desc: 'Kubernetes is an open-source container orchestration platform that automates
  the deployment, management, scaling, and networking of containers. It makes it simpler
  to deploy apps to production.

  We just published a Kubernetes course on the freeCodeCam...'
---

Kubernetes est une plateforme d'orchestration de conteneurs open-source qui automatise le déploiement, la gestion, la mise à l'échelle et la mise en réseau des conteneurs. Elle simplifie le déploiement des applications en production.

Nous venons de publier un cours Kubernetes sur la chaîne YouTube freeCodeCamp.org.

Bogdan Stashchuk a développé ce cours. Il est un instructeur DevOps populaire qui a enseigné à des centaines de milliers de personnes sur Udemy et YouTube.

Voici toutes les sections couvertes dans ce cours intensif sur Kubernetes :

* Introduction à Kubernetes pour les débutants
* Qu'est-ce que Kubernetes
* Qu'est-ce qu'un Pod
* Cluster Kubernetes et Nœuds
* Services Kubernetes
* Qu'est-ce que kubectl
* Logiciel requis pour ce cours
* Installation de kubectl
* Installation de Minikube
* Création d'un cluster Kubernetes en utilisant Minikube
* Exploration du nœud Kubernetes
* Création d'un seul Pod
* Exploration du Pod Kubernetes
* Création d'un alias pour la commande kubectl
* Création et exploration du Déploiement
* Connexion à l'un des Pods en utilisant son adresse IP
* Qu'est-ce qu'un Service
* Création et exploration du Service ClusterIP
* Connexion au Déploiement en utilisant le Service ClusterIP
* Suppression du Déploiement et du Service
* Création d'une application web Node
* Conteneurisation de l'application Node
* Poussée de l'image personnalisée vers Docker Hub
* Création d'un déploiement basé sur l'image Docker personnalisée
* Mise à l'échelle du déploiement de l'image personnalisée
* Création du Service NodePort

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=d6WC5n9G_sM) (3 heures de visionnage).

%[https://www.youtube.com/watch?v=d6WC5n9G_sM]

### Transcription

(générée automatiquement)

Kubernetes permet de conteneuriser des applications et simplifie le déploiement en production.

Bogdan Stashchuk vous enseignera tout ce que vous devez savoir pour commencer avec Kubernetes.

Bienvenue dans Kubernetes pour les débutants.

Kubernetes est le standard de facto pour le déploiement des applications conteneurisées en production.

Kubernetes est open source et donc gratuit à utiliser.

Permettez-moi d'abord de me présenter avant que nous commencions ce cours.

Je m'appelle Bogdan Stashchuk et j'utilise Docker et Kubernetes depuis plusieurs années en pratique.

Et j'ai déployé des applications réelles en production en utilisant Kubernetes.

De plus, j'enseigne en ligne et sur mes sites web personnels shoe.com, vous pourriez trouver tous les cours que j'enseigne.

Maintenant, commençons avec Kubernetes pour les débutants, et j'aimerais commencer par le plan du cours.

Alors, qu'est-ce qui est inclus dans ce cours, nous commencerons par parler de la terminologie et des principales caractéristiques de Kubernetes.

Et vous apprendrez ce qu'est un cluster Kubernetes, ce qu'est un nœud et ce qu'est un pod et ce que Kubernetes fait essentiellement.

Ensuite, nous plongerons immédiatement dans la pratique et nous construirons un petit cluster Kubernetes localement sur nos ordinateurs.

Et ensuite, en utilisant un tel cluster, nous créerons et mettrons à l'échelle différents déploiements.

De plus, nous construirons une image Docker personnalisée, la pousserons vers Docker Hub, et ensuite créerons un déploiement Kubernetes basé sur cette image Docker construite de manière personnalisée.

Autre que cela, nous créerons également des services et des déploiements dans Kubernetes en utilisant des fichiers de configuration YAML.

De plus, nous connecterons différents déploiements ensemble car c'est une situation très courante lorsque vous devez connecter différentes applications ensemble via le réseau.

Et Kubernetes permet bien sûr de le faire.

Et aussi finalement, nous changerons le runtime de conteneur de Docker à CRI-o car Kubernetes n'est pas lié à Docker.

Il supporte également d'autres runtimes de conteneurs comme CRI-O et container D.

Et vous pourriez utiliser Kubernetes absolument sans Docker.

Un seul prérequis pour ce cours est votre familiarité avec Docker, je suppose que vous savez ce qu'est un conteneur Docker et comment créer différents conteneurs.

Très bien, alors commençons avec ce cours.

Et j'aimerais commencer par la définition : Kubernetes est un système d'orchestration de conteneurs.

En utilisant Docker, vous pouvez bien sûr créer un conteneur sur n'importe quel ordinateur.

Mais bien sûr, si vous voulez créer plusieurs conteneurs sur différents ordinateurs, sur différents serveurs, vous pourriez rencontrer des problèmes.

Kubernetes vous permet de créer les conteneurs sur différents serveurs, qu'ils soient physiques ou virtuels.

Et tout cela est fait automatiquement sans votre intervention.

Vous dites simplement à Kubernetes combien de conteneurs vous souhaitez créer basés sur une image spécifique.

Kubernetes est un mot relativement long, et il se compose de 10 lettres différentes.

MAIS les professionnels de l'informatique et les développeurs de logiciels sont des personnes relativement paresseuses et ils n'aiment pas taper beaucoup.

C'est pourquoi le mot Kubernetes est généralement raccourci à seulement trois caractères.

Mais comment est-ce fait ? Regardons ce mot.

Entre k et s, il y a en fait huit lettres différentes.

Donc le nombre huit, c'est pourquoi le mot Kubernetes serait raccourci à seulement trois caractères, K eight s.

Donc huit représente simplement la quantité de lettres entre le début et la fin du mot. Simple comme ça.

Connaissant cette astuce très simple, nous pouvons continuer.

Et maintenant, laissez-moi vous expliquer ce dont Kubra s s'occupe.

Donc Kubernetes s'occupe du déploiement automatique des applications conteneurisées sur différents serveurs.

Et ces serveurs peuvent être des serveurs bare metal ou physiques ou des serveurs virtuels.

L'option des serveurs virtuels est bien sûr plus courante de nos jours, et presque personne n'utilise maintenant des serveurs bare metal.

Donc Kubernetes vous permet d'effectuer des déploiements automatisés sur différents serveurs qui peuvent être situés même dans différentes parties du monde.

Autre que cela, Kubernetes s'occupe également de la distribution de la charge sur ces multiples serveurs.

Et cela vous permet d'utiliser vos ressources efficacement et d'éviter la sous-utilisation ou la surutilisation des ressources.

De plus, Kubernetes s'occupe de la mise à l'échelle automatique des applications déployées au cas où vous devriez augmenter, par exemple, la quantité de conteneurs qui doivent être créés sur différents serveurs.

Et tout cela est fait automatiquement.

Vous dites simplement quand vous voulez mettre à l'échelle vers le haut ou vers le bas.

De plus, Kubernetes s'occupe de la surveillance et de la vérification de l'état des conteneurs.

Et au cas où certains conteneurs échouent pour une raison quelconque, Kubernetes peut automatiquement remplacer les conteneurs défaillants et tout cela est fait sans votre intervention.

Comme je viens de vous le dire, Kubernetes déploie des applications conteneurisées et doit donc utiliser un runtime de conteneur spécifique.

Et Docker est juste l'une des options possibles. Kubernetes supporte désormais des runtimes de conteneurs tels que Docker, CRI-O et container D, et le runtime de conteneur, par exemple Docker ou CRI-o, doit être en cours d'exécution sur chacun des serveurs qui sont inclus dans le cluster Kubernetes.

Et le principal résultat ici est que Kubernetes peut être utilisé même sans Docker du tout.

Il supporte d'autres runtimes de conteneurs comme CRI-O et container D.

Et à la fin de ce cours, je vous montrerai comment changer le runtime de conteneur et passer de Docker, par exemple, à CRI-O.

Maintenant, commençons avec la terminologie et l'architecture de Kubernetes.

Et commençons par le pod, qui est la plus petite unité dans le monde de Kubernetes. Dans Docker, le conteneur est la plus petite unité dans Kubernetes, le pod est la plus petite unité possible et les conteneurs sont créés à l'intérieur du pod.

Donc, le pod est l'atome suivant à l'intérieur du pod, il peut y avoir des conteneurs, soit un ou même plusieurs conteneurs.

De plus, il y a des volumes partagés et des ressources réseau partagées, par exemple, une adresse IP partagée.

Cela signifie que tous les conteneurs à l'intérieur du même pod partagent des volumes et partagent l'adresse IP.

Et vous devez garder cela à l'esprit si vous voulez créer plusieurs conteneurs à l'intérieur du même port.

Le scénario le plus courant est bien sûr d'avoir un seul conteneur par port.

Mais parfois, lorsque les conteneurs doivent être étroitement liés et qu'ils dépendent fortement les uns des autres et qu'ils peuvent exister dans le même espace de noms, il est possible de créer plusieurs conteneurs dans le même port.

Mais encore une fois, un seul conteneur par port est le cas d'utilisation le plus courant.

De plus, veuillez garder à l'esprit que chaque port doit être situé sur le même nœud, il n'est pas possible de répartir les conteneurs d'un seul port sur différents serveurs dans le cluster Kubernetes, un port, un serveur.

Alors, jetons maintenant un coup d'œil à ce cluster Kubernetes, qu'est-ce que ce cluster Kubernetes contient des nœuds, un nœud est en fait un serveur, soit un serveur bare metal ou un serveur virtuel.

Et vous pouvez inclure plusieurs serveurs dans le cluster Kubernetes et ils pourraient être situés dans différents centres de données dans différentes parties du monde.

Mais généralement, les nœuds qui appartiennent au même cluster Kubernetes sont situés à proximité les uns des autres afin d'effectuer tous les travaux plus efficacement.

À l'intérieur du nœud, il y a des ports, qui sont à nouveau la plus petite unité possible dans Kubernetes, et à l'intérieur de chaque port, il y a des conteneurs, généralement un seul conteneur par port, et de tels ports sont créés sur différents nœuds et tout cela est fait automatiquement pour vous par Kubernetes.

Mais bien sûr, votre travail est de créer de tels nœuds et de créer des clusters basés sur ces nœuds.

Les nœuds ne formeront pas automatiquement un cluster sans votre intervention.

Mais après une telle configuration initiale, tout sera automatisé et Kubernetes déployera automatiquement des pods sur différents nœuds.

Mais comment ces nœuds communiquent-ils réellement avec le cluster et comment sont-ils gérés.

Dans un cluster Kubernetes, il y avait un nœud maître et les autres nœuds du cluster sont appelés nœuds travailleurs.

Et le nœud maître gère réellement les nœuds travailleurs.

Et si le travail du nœud maître est de distribuer, par exemple, la charge sur les autres nœuds travailleurs et tous les pods, qui sont liés à vos applications sont déployés sur les nœuds travailleurs, le nœud maître exécute uniquement les pods système, qui sont responsables du travail réel du cluster Kubernetes en général, nous pourrions aussi dire que le nœud maître dans le cluster Kubernetes est en fait le plan de contrôle, et il n'exécute pas vos applications client.

Alors, quels services s'exécutent réellement sur différents nœuds ? Jetons un coup d'œil à ce diagramme.

Il y a des services tels que kubelet, kube proxy et container runtime et ces services sont présents sur chaque nœud dans un cluster Kubernetes.

Vous savez déjà ce qu'est le container runtime, le container runtime exécute les conteneurs réels à l'intérieur de chaque nœud, et il existe des runtimes de conteneurs tels que Docker CRI-o ou container D.

Il y a aussi un service appelé kubelet.

Et un tel service sur chaque nœud travailleur communique avec le service API Server sur le nœud maître.

Le service API Server est le point principal de communication entre les différents nœuds dans le monde Kubernetes.

Kube proxy, qui est également présent sur chaque nœud, est responsable de la communication réseau à l'intérieur de chaque nœud et entre les nœuds.

De plus, il y a d'autres services qui sont présents sur le nœud maître.

Et ce sont le planificateur et un tel service est responsable de la planification et de la distribution de la charge entre les différents nœuds dans la salle de classe.

De plus, il y avait le gestionnaire de contrôleur de cube, et ce point unique qui contrôle tout dans le cluster Kubernetes.

Et il contrôle en fait ce qui se passe sur chacun des nœuds dans le cluster.

De plus, il y avait le gestionnaire de contrôleur cloud.

Et son travail est l'interaction avec le fournisseur de services cloud où vous exécutez en fait votre cluster Kubernetes, car généralement vous ne créez pas de tels clusters vous-même en utilisant simplement vos propres serveurs.

Au lieu de cela, vous pouvez très facilement exécuter le cluster Kubernetes à partir de l'un des fournisseurs de cloud, qui effectue presque automatiquement la création de tous les nœuds et les connexions entre ces nœuds.

Et pour cela, vous devez exécuter le service cloud controller manager sur ce nœud maître.

De plus, par exemple, si vous souhaitez créer le déploiement de votre application à l'intérieur du cluster Kubernetes, qui sera ouvert au monde extérieur et permettra les connexions depuis l'extérieur, vous pouvez également créer des adresses IP de load balancer.

Et ces load balancers.

Les adresses IP sont généralement fournies par des fournisseurs de cloud spécifiques.

De plus, sur un nœud maître, il y a un service appelé etcd.

Et c'est un service qui stocke en fait tous les logs liés au fonctionnement de l'ensemble du cluster Kubernetes.

Et ces logs sont stockés sous forme de paires clé-valeur.

De plus, il y a d'autres services qui s'exécutent sur le nœud maître, par exemple, un service DNS qui est responsable de la résolution des noms de l'ensemble du cluster Kubernetes.

Et par exemple, en utilisant un service DNS, vous pouvez vous connecter à un déploiement spécifique par le nom du service de déploiement correspondant.

Et de cette manière, vous pouvez connecter différents déploiements avec un travail ou différents services qui s'exécutent sur différents nœuds dans le cluster Kubernetes.

Et le service principal sur le nœud maître est API Server.

Et d'ailleurs, en utilisant ce service API Server, vous pouvez en fait gérer l'ensemble du cluster Kubernetes.

Comment est-ce fait ? Cela est fait en utilisant kubectl ou kube control.

Et kube control est un outil de ligne de commande séparé, qui vous permet de vous connecter à un cluster Kubernetes spécifique et de le gérer à distance.

Et kubectl peut s'exécuter même sur votre ordinateur local.

Et en utilisant un tel outil kubectl, vous pouvez gérer un cluster Kubernetes distant.

Et en utilisant un tel outil, vous vous connectez en fait en utilisant l'API REST au service API Server sur le nœud maître.

Et une telle communication se fait via HTTPS.

D'ailleurs, les autres nœuds du cluster, je veux dire les nœuds travailleurs, communiquent avec le nœud maître de la même manière.

Cela signifie qu'en utilisant un tel outil kubectl, vous pouvez gérer n'importe quel cluster Kubernetes distant.

Cela suffit pour l'aperçu de l'architecture de Kubernetes, et maintenant vous savez que le cluster Kubernetes se compose des nœuds, et l'un des nœuds est le nœud maître, et il gère nos autres nœuds, qui sont appelés nœuds travailleurs.

Sur chaque nœud, il y a des pods et les pods sont créés automatiquement par Kubernetes.

Et à l'intérieur du pod, il y a des conteneurs, généralement un seul conteneur par pod.

De plus, veuillez garder à l'esprit que tous les conteneurs à l'intérieur du pod partagent l'espace de noms de ce pod, comme les volumes ou l'adresse IP du réseau.

De plus, les pods sont les plus petites unités dans Kubernetes, et les pods peuvent être créés, peuvent être supprimés, peuvent être déplacés d'un nœud à un autre.

Cela se produit automatiquement sans votre intervention.

Mais vous devez concevoir votre application avec cela à l'esprit, les pods peuvent être supprimés à tout moment.

De plus, il y a différents services qui s'exécutent sur différents nœuds.

Par exemple, le service API Server est le point central de communication entre le nœud maître et les autres nœuds travailleurs.

Et aussi en utilisant un tel service API Server, vous pouvez en fait gérer le cluster Kubernetes réel en utilisant l'outil kubectl, qui doit être installé, par exemple, sur votre ordinateur si vous effectuez la gestion depuis votre ordinateur.

Très bien, je ne veux pas approfondir les détails de Kubernetes car c'est un outil très compliqué.

Et je veux me concentrer davantage sur les tâches pratiques à la place.

C'est pourquoi maintenant, après cet aperçu, nous allons plonger ensemble avec vous dans la pratique et effectuer différentes tâches pratiques ensemble.

Par exemple, nous créerons des déploiements, des services, mettrons à l'échelle des déploiements, créerons une image Docker personnalisée et créerons le déploiement basé sur cette image, et ainsi de suite.

Afin d'effectuer toutes les tâches pratiques ensemble avec moi, vous devez installer certains programmes sur votre ordinateur.

Et maintenant, lorsque nous parlons du logiciel requis, et d'abord nous devons créer un cluster Kubernetes réel, où nous créerons différents déploiements.

Bien sûr, vous pouvez créer un cluster en utilisant les services de l'un des fournisseurs de cloud comme Amazon Web Services, ou Google Cloud, mais vous devez payer pour un tel service.

Si vous voulez une solution gratuite, vous pouvez créer un cluster localement sur votre ordinateur.

Et pour cela, il y avait un outil comme minikube.

Et un tel outil créera essentiellement un cluster à nœud unique.

Et ce nœud sera à la fois un nœud travailleur et un nœud maître.

Mais pour les déploiements de test, et comme terrain de jeu, cela fonctionne très bien et tout cela est gratuit et s'exécutera sur votre ordinateur local.

Afin d'exécuter minikube avec succès, vous devez utiliser une machine virtuelle ou un gestionnaire de conteneurs.

Et il y a les gestionnaires de machines virtuelles ou de conteneurs suivants qui sont pris en charge : VirtualBox, VMware, Docker, Hyper-V, ou Parallels.

Il y a aussi d'autres options disponibles.

Mais vous devez utiliser l'une de ces options.

Afin de créer réellement le nœud virtuel, qui exécutera tous les pods dans votre cluster Kubernetes.

Je vous suggère d'utiliser Hyper-V, si vous êtes un utilisateur Windows.

Et si vous êtes un utilisateur Mac OS, vous pouvez utiliser VirtualBox, il est gratuit et open source ou vous pouvez utiliser VMware ou Parallels.

D'ailleurs, il y avait aussi une option pour exécuter minikube comme conteneur à l'intérieur de Docker.

Bien sûr, si vous avez déjà installé Docker sur votre ordinateur, vous pouvez l'utiliser afin de créer un cluster Kubernetes en utilisant minikube et essentiellement il créera un conteneur Docker séparé et à l'intérieur de ce conteneur tous les pods seront créés.

Mais personnellement, je ne vous recommande pas d'utiliser l'option Docker car il y avait certaines limitations.

Par exemple, je n'ai pas pu changer le runtime de conteneur à l'intérieur du conteneur Docker en CRI ou container D.

Et donc je vous recommande d'utiliser les autres options qui sont mentionnées ici.

D'ailleurs, Hyper-V est disponible sur les ordinateurs Windows dès la sortie de la boîte et vous pouvez l'utiliser comme gestionnaire de machine virtuelle pour exécuter le nœud minikube.

Pour résumer, en utilisant minikube, vous créerez un cluster Kubernetes à nœud unique.

Mais comme je l'ai mentionné auparavant, vous devez utiliser un outil spécifique afin de gérer ce cluster.

Et cet outil s'appelle kubectl.

D'ailleurs, kubectl est inclus dans minikube.

Mais si vous voulez utiliser une telle version incluse, vous devez entrer les commandes minikube kubectl, ce n'est pas pratique.

Par conséquent, je vous recommande d'installer kubectl séparément.

Et en utilisant une installation séparée, vous pourrez bien sûr gérer d'autres clusters Kubernetes, qui sont situés par exemple, chez Amazon Web Services.

Donc, kubectl est aussi l'un des programmes que vous devez installer sur votre ordinateur.

Bien sûr, je vous expliquerai comment installer minikube et kubectl.

Autre que cela, nous ferons aussi un peu de codage dans ce cours pratique.

Et pour cela, vous devez utiliser l'un des éditeurs de code et je vous recommande d'installer Visual Studio code, il est open source et gratuit à utiliser.

Et si vous ne l'avez pas encore installé, veuillez le faire.

De plus, il a de nombreuses extensions différentes, et l'une d'entre elles est l'extension Kubernetes.

Et en utilisant une telle extension, vous pourriez très rapidement créer, par exemple, des fichiers de configuration YAML pour vos déploiements et services dans Kubernetes.

C'est tout ce dont vous avez besoin pour ce cours : minikube, kubectl et Visual Studio code.

Maintenant, commençons avec la partie pratique.

Et j'espère que vous apprécierez ce cours.

Et nous commencerons par l'installation de minikube et kubectl.

Très bien, maintenant, commençons avec la partie pratique du cours.

Et nous commencerons par installer minikube ainsi que kubectl.

Mais d'abord, je vous demanderais de naviguer vers kubernetes.io.

C'est le site principal dédié à Kubernetes en général et il contient toute la documentation liée à la configuration des clusters minikube, à la création de déploiements, etc.

Veuillez cliquer ici sur documentation.

Et ici, dans la section de gauche, allez dans getting started.

Et ici, vous pouvez lire comment vous pouvez créer un environnement d'apprentissage.

Avec cela, vous pouvez également trouver des informations sur la création d'un environnement de production.

Mais nous sommes intéressés maintenant par la création d'un cluster Kubernetes local.

Et pour cela, nous utiliserons minikube.

Et nous installerons également kubectl.

C'est pourquoi, veuillez cliquer ici sur ce lien hypertexte install tools.

Et trouver des instructions sur la façon d'installer kubectl sur différents systèmes d'exploitation, veuillez choisir le vôtre.

Je choisirai Mac OS ici.

Et si vous êtes un utilisateur Mac OS, vous pouvez très facilement installer kubectl en utilisant homebrew, laissez-moi vous montrer comment faire cela.

Laissez-moi cliquer sur cette option.

Exécutez la commande d'installation brew install kubectl, laissez-moi copier cette commande et ouvrir le terminal, j'utilise iterm sur Mac et coller cette commande ici.

Allons-y et installons kubectl.

Le package warden et kubectl a été installé.

Laissez-moi vérifier la version de kubectl.

Pour cela, je peux utiliser cette commande kubectl version, il y a le client de bureau.

Laissez-moi l'entrer ici.

Et je vois que kubectl a été installé avec succès.

Et ici, il y avait la version du client, majeure un et mineure 22.

Et ici, il y avait la version exacte qui a été installée.

Très bien, si vous êtes un utilisateur Windows, je vous recommande d'installer kubectl en utilisant le gestionnaire de paquets, vous pouvez aller à install and setup kubectl on Windows et ici choisir l'option install on Windows using chocolaty ou scoop.

Cliquez sur cette option et ici vous trouverez des instructions sur la façon d'installer différents paquets en utilisant le gestionnaire de paquets chocolaty ou l'installateur de ligne de commande scoop, je vous recommande d'installer le gestionnaire de paquets chocolaty.

Afin de le faire, veuillez ouvrir ce lien ici et trouver des instructions sur la façon d'installer ce gestionnaire de paquets pour Windows.

En utilisant le même gestionnaire de paquets, vous pouvez très facilement installer minikube également.

Alors, veuillez aller de l'avant et installer ce gestionnaire de paquets et ensuite, suivre ces instructions sur la façon d'installer kubectl sur Windows.

Utilisez simplement une seule commande, celle-ci, et ensuite, vérifiez que kubectl est disponible en utilisant cette commande.

Très bien.

Après cela, je suppose que kubectl est déjà disponible sur vos ordinateurs.

Et maintenant, allons-y et installons minikube.

Retournez à la page Getting Started et ici, faites défiler vers le bas jusqu'à learning environment et cliquez sur le lien hypertexte installed tools.

Celui-ci, vous trouverez le jeu auquel vous devez installer kubectl.

C'est ce que nous venons de faire ensemble.

Et si vous faites défiler vers le bas, vous trouverez des options que vous pouvez utiliser afin de créer un cluster Kubernetes local à des fins d'apprentissage et de test.

De nos jours, il existe des outils tels que kind, et il vous permet de créer un cluster Kubernetes localement sur votre ordinateur, mais il nécessite Docker.

Il y a aussi minikube et kube ADM.

Nous utiliserons minikube tout au long de ce cours.

C'est pourquoi, commençons avec l'installation de minikube.

Il ne nécessite pas Docker.

Mais il nécessite l'un des gestionnaires de machines virtuelles comme Hyper V, Parallels.

Ou si vous le souhaitez, vous pouvez également utiliser Docker, veuillez naviguer vers ce lien minikube, vous pouvez simplement entrer minikube dans la barre de recherche Google et cliquer sur le premier résultat dans la sortie.

Et ici, vous trouverez la documentation sur la façon de commencer avec minikube, veuillez cliquer sur ce lien get started.

Et ici, vous pouvez lire à propos de minikube et il créera essentiellement un cluster Kubernetes localement sur votre ordinateur.

Et il contiendra un seul nœud qui agira à la fois comme nœud maître et nœud travailleur.

Et tout ce dont vous avez besoin afin de créer un tel cluster est simplement une commande minikube start simple comme cela.

Mais afin de créer avec succès un cluster minikube, vous devez installer l'un des gestionnaires de conteneurs ou de machines virtuelles tels que Docker, HyperCard, Hyper V, Parallels et ainsi de suite.

Je vous ai dit avant que si vous êtes un utilisateur Windows, je vous recommande d'utiliser Hyper V car il est disponible sur Windows dès la sortie de la boîte.

Si vous êtes un utilisateur Mac, je vous recommande d'utiliser l'option VirtualBox ou Parallels ou VMware Fusion, VirtualBox est gratuit pour nous.

Par conséquent, si vous ne voulez rien acheter pour le gestionnaire de machine virtuelle, je vous recommande d'utiliser cette option.

Il est également possible de créer un cluster minikube à l'intérieur du conteneur Docker et pour cela, vous pouvez simplement installer Docker.

Mais personnellement, je ne vous recommande pas d'utiliser cette option car il y a certaines limitations à exécuter un tel cluster à l'intérieur du conteneur Docker.

Très bien, ici, vous pouvez trouver comment installer minikube sur différents systèmes d'exploitation Linux, Mac OS et Windows.

Si vous êtes un utilisateur Windows, vous pouvez, de manière similaire à kubectl, utiliser choco latte, veuillez sélectionner cette option et entrer simplement une commande choco install minikube simple comme cela et vous obtiendrez minikube installé sur un ordinateur Windows, mais j'utilise Mac OS, c'est pourquoi je sélectionnerai cette option et sélectionnerai homebrew et afin d'installer minikube en utilisant brew, je pourrais simplement entrer juste une commande brew install minikube.

Laissez-moi aller de l'avant et l'installer en utilisant brew.

Revenons au terminal et ici, la commande de base brew install minikube.

Attendons un peu jusqu'à ce que cela soit installé.

Très bien, minikube a été installé et maintenant je pourrais vérifier sa version minikube version.

Ici, il y avait une version dans mon cas et vous pourriez également entrer la commande minikube HELP afin de trouver la liste de toutes les commandes disponibles dans minikube.

Et si vous faites défiler vers le haut, vous découvrirez comment démarrer un cluster Kubernetes local, obtenir le statut du cluster Kubernetes local, arrêter le cluster ou le supprimer et ouvrir le tableau de bord.

Vous pourriez également mettre en pause et reprendre le cluster Kubernetes, maintenant, créons le cluster réel, je suppose que vous avez également installé minikube et kubectl.

Ces outils sont deux outils séparés.

C'est pourquoi ils sont disponibles en tant que deux commandes séparées, minikube et kubectl.

Et maintenant, allons-y et créons un cluster Kubernetes.

Pour cela, veuillez utiliser la commande minikube start, mais d'abord, entrons minikube status afin de vérifier le statut actuel du cluster minikube status.

Ici, je vois que le profil minikube n'est pas trouvé autour du profil minikube, ces deux profils et aussi ice afin de démarrer le cluster, je dois exécuter la commande minikube start.

C'est ce que nous allons faire maintenant, créons le cluster minikube start.

Et ici, je voudrais vous demander de démarrer le cluster minikube avec l'option.

Et cette option sera le pilote, et vous devriez écrire avec deux tirets, c'est le pilote.

Et ici, il y aura un signe égal.

Et après cela, vous devez spécifier la machine virtuelle ou le gestionnaire de conteneurs que vous utiliserez afin de créer le cluster minikube.

Je vous ai dit avant que si vous êtes un utilisateur Windows, je vous recommande d'utiliser Hyper V.

Par conséquent, si vous êtes sur Windows, entrez simplement ici Hyper V comme cela, tout en minuscules sans tiret, il y a ce pilote, signe égal Hyper V.

Si vous êtes un utilisateur Mac OS, vous pouvez utiliser l'une de ces options, VirtualBox, Parallels ou VMware Fusion, j'utiliserai VirtualBox.

Si vous n'avez pas votre boîte à outils, veuillez l'installer et ici, votre boîte à outils et cliquez sur le premier lien ici.

Votre boîte à outils est gratuite.

Et voici le lien où vous pouvez télécharger votre boîte à outils.

Donc, si vous n'avez pas votre boîte à outils, et si vous êtes un utilisateur Mac OS, veuillez l'installer.

Très bien, j'ai déjà installé votre boîte à outils.

C'est pourquoi je vais simplement le spécifier comme bio pour cette option de pilote ici.

Donc je vais taper Vertol box.

Allons-y et créons un cluster minikube à l'intérieur de la machine virtuelle VirtualBox, dans mon cas, en créant votre boîte à outils, machine virtuelle, quantité de CPU, mémoire et disque.

Cela prendra un certain temps, laissez-moi attendre un peu, la machine virtuelle a été créée.

Et maintenant je vois le message de préparation de Kubernetes sur Docker.

Et cela signifie que par défaut, nous utiliserons le runtime de conteneur Docker pour exécuter les conteneurs réels à l'intérieur du cluster Kubernetes.

Ici, je vois l'étape de génération des certificats et des clés, le démarrage du plan de contrôle.

Et enfin, à la fin, je vois terminé, kubectl n'est pas configuré pour utiliser le cluster minikube.

Et cela signifie que vous n'avez rien à faire pour vous connecter de kubectl au cluster minikube réel.

Cette connexion a été créée automatiquement pour vous lors de la création du cluster minikube.

De plus, dans mon cas, je vois un tel avertissement, vous avez sélectionné le pilote your toolbox, mais il existe de meilleures options pour de meilleures performances et support, envisagez d'utiliser un pilote différent HyperCard, Parallels ou VMware.

Maintenant, vérifions réellement le statut de ce cluster Kubernetes.

Et pour cela, vous pouvez entrer la commande minikube status.

Et vous devriez constater que l'hôte est ironique, cubelet est en cours d'exécution, le serveur API est en cours d'exécution et la configuration cube est configurée.

C'est le statut normal du cluster minikube.

Et maintenant, nous sommes réellement en mesure de créer des déploiements, des services, etc., à l'intérieur de ce cluster minikube.

De plus, je voudrais mentionner que je n'ai pas Docker en cours d'exécution en ce moment.

Je l'ai en fait installé sur cet ordinateur.

Mais ici, dans la barre des icônes, je ne vois pas l'icône Docker, cela signifie que maintenant Kubernetes sur mon ordinateur local n'utilise pas l'installation réelle de Docker sur mon ordinateur.

Mais il y a Docker qui s'exécute à l'intérieur du nœud minikube.

Et c'est ce que nous allons vérifier maintenant.

Donc, comme vous le savez déjà, chaque nœud dans le cluster Kubernetes est simplement un serveur, soit virtuel ou physique.

Dans notre cas, nous avons créé un serveur virtuel et vous pouvez vous connecter à n'importe quel serveur en utilisant le protocole SSH.

Et afin de vous connecter via SSH, nous devons d'abord trouver quelle adresse IP a été attribuée au nœud Kubernetes.

Minikube fournit une commande pour cela.

Tapez simplement minikube IP et vous verrez quelle adresse IP a été attribuée à une machine virtuelle qui exécute notre nœud Kubernetes qui a été créé par minikube, il y avait une adresse dans mon cas, saisissez simplement cette adresse IP et ensuite, tapez SSH Docker, c'est le nom d'utilisateur qui est le nom d'utilisateur par défaut pour un tel nœud, un tel serveur, et après le signe ajouté, basez un équilibre du nœud minikube et ensuite, veuillez appuyer sur Entrée, vous serez présenté avec une empreinte digitale, veuillez continuer et taper ici comme des retraits, une telle empreinte digitale.

Et ensuite, vous serez invité à entrer un mot de passe, le mot de passe par défaut pour minikube.

Votre machine virtuelle est DC user, veuillez continuer et le taper ici.

Donc, le nom d'utilisateur est Docker et le mot de passe est DC user, le mot de passe a été entré.

Et maintenant, je vois l'invite de bienvenue du serveur minikube.

Maintenant, je suis à l'intérieur du nœud Kubernetes.

Et la première commande que je voudrais vous demander d'entrer ici est docker ps.

Une telle commande vous listera tous les conteneurs Docker en cours d'exécution.

Et voici un ensemble de différents conteneurs qui ont été créés à l'intérieur du nœud Kubernetes.

Et encore une fois, veuillez noter que Docker est le runtime de conteneur par défaut pour Kubernetes.

Il existe d'autres runtimes de conteneurs, tels que CRI-O et container D.

Mais ici, nous voyons qu'il y a un ensemble de différents conteneurs, qui ont été créés par Docker à l'intérieur du nœud minikube.

Et par exemple, ici, je vois un conteneur tel que le serveur API cube, le planificateur cube, etc.

Rappelons que nous avons discuté avec vous des différents services qui s'exécutent sur les nœuds maîtres et les nœuds travailleurs.

Et ces services s'exécutent en fait à l'intérieur des conteneurs, comme vous le voyez maintenant ici.

De plus, il y a des conteneurs tels que le proxy cube, le provisionneur de stockage, ou, par exemple, le DNS core.

Et encore une fois, chaque conteneur a son propre but.

C'est ainsi que vous pouvez vérifier quels conteneurs ont été créés à l'intérieur du nœud Kubernetes.

Mais si j'entre ici une commande kubectl, je verrai une erreur de commande kubectl introuvable car la commande kubectl n'est pas disponible à l'intérieur du nœud Kubernetes, kubectl est un outil externe qui est utilisé afin de gérer le cluster Kubernetes, de cette manière, sortons maintenant de cette connexion SSH, la connexion a été fermée.

Et maintenant, utilisons la commande kubectl ici, kubectl est disponible localement sur nos ordinateurs car nous avons installé kubectl avant, vérifions d'abord les informations du cluster, kubectl cluster info et j'obtiens la sortie suivante, le plan de contrôle Kubernetes est en cours d'exécution.

Et ici, je vois l'adresse IP que nous venons de voir après avoir entré la commande minikube IP.

Dans votre cas, bien sûr, une telle adresse IP sera différente.

Et aussi, je vois que le service core DNS est également en cours d'exécution.

Cela signifie que maintenant nous sommes en mesure de créer des déploiements, des services, etc., sur notre cluster Kubernetes.

Mais d'abord, listons les nœuds qui sont disponibles dans notre cluster Kubernetes.

Pour cela, veuillez entrer la commande kubectl get nodes.

Et ici, je vois un seul nœud car minikube crée un cluster à nœud unique, il y avait le nom d'un tel nœud, le statut est prêt.

Et ici sont les rôles, plan de contrôle et maître.

Nous avons compris que maintenant, à l'intérieur de notre cluster minikube.

Ce nœud unique agit à la fois comme nœud maître et nœud travailleur et sur le nœud travailleur, Kubernetes crée différents pods liés à vos déploiements que vous déployez dans un cluster Kubernetes.

Maintenant, laissez-moi vérifier quels pods sont disponibles ou en cours d'exécution dans ce cluster.

Pour cela, entrons la commande kubectl get pods et maintenant je vois la sortie, aucune ressource trouvée dans l'espace de noms par défaut.

Listons tous les espaces de noms qui sont disponibles maintenant dans ce cluster Kubernetes.

Pour cela, veuillez entrer la commande kubectl get namespaces comme cela.

Et je vois plusieurs espaces de noms comme default, kube-node-lease, kube-public et kube-system, les espaces de noms sont utilisés dans Kubernetes afin de regrouper différentes ressources et objets de configuration.

Et si vous entrez simplement kubectl get pods, vous verrez uniquement les pods disponibles à l'intérieur de l'espace de noms par défaut ici.

Et d'ailleurs, tous les pods que nous créerons tout au long des scores seront créés dans l'espace de noms par défaut, mais nous n'avons pas encore créé de pods jusqu'à présent.

C'est pourquoi essayons de découvrir quels pods sont en cours d'exécution à l'intérieur de nos autres espaces de noms, par exemple kube-system.

Afin de lister les pods dans un espace de noms spécifique, vous devez utiliser l'option namespace.

Donc kubectl.

Get pods.

Il y a le namespace, signe égal et ici entrez kube-system.

Allons-y et exécutons cette commande.

Et maintenant ici dans cet espace de noms kube-system, je vois des pods tels que gordianus etcd, qui stocke tous les logs de l'ensemble du cluster Kubernetes, kube, API server, Kube controller, kube, proxy, kube schedule, et storage provisioner.

Tous ces pods sont des pods système, qui s'exécutent sur ce nœud maître.

Très bien, c'est ainsi que nous pouvons découvrir quels pods sont en cours d'exécution maintenant dans notre cluster Kubernetes.

Maintenant, allons-y et créons un pod manuellement.

Et pour cela, nous pouvons utiliser une commande qui est similaire à la commande docker run.

Mais avec la commande docker run, vous pouvez créer un seul conteneur Docker ici ou vous pouvez utiliser la commande kubectl Run afin de créer un seul pod.

Faisons cela, kubectl run ici sera nommé.

Utilisons par exemple l'image Docker nginx qui est disponible sur Docker Hub.

Pour cela, entrons ici le nom du pod Nginx.

Et ensuite, ajoutons l'option image et sa valeur sera Ingenix Ingenix.

Voici le nom de l'image Docker qui sera téléchargée automatiquement et un nouveau conteneur sera créé sur la base de cette image et ce conteneur s'exécutera à l'intérieur du pod Kubernetes.

Allons-y et voyons ce qui se passera.

Kubectl Iran Ingenix fait cette image égale signe Ingenix et ici je vois la sortie pod Ingenix.

Super.

Entrons la commande kubectl get pods.

Et ici je vois maintenant un seul pod nginx, il n'est pas encore prêt.

Et au lieu de son conteneur créé.

Entrons la même commande à nouveau kubectl get pods et maintenant je vois que ce pod est maintenant en cours d'exécution, il est prêt et son statut est en cours d'exécution.

Bien sûr, cela a pris un certain temps pour créer un tel pod car à l'intérieur, il y avait un conteneur nginx et Docker à l'intérieur du nœud Kubernetes a en fait été demandé de télécharger l'image nginx depuis Docker Hub et de créer le conteneur correspondant basé sur l'image de recherche Ingenix.

Faisons-nous connaître les détails de ce pod spécifique nommé Nginx.

Ce nom, nous l'avons spécifié manuellement ici.

Pour cela, veuillez entrer la commande kubectl describe pod et ici sera le nom du pod auquel vous souhaitez obtenir des détails, voici Ingenix.

C'est le nom du pod en cours d'exécution.

Et voici de nombreux détails différents liés à ce pod spécifique.

Laissez-moi faire défiler un peu vers le haut.

Et ici, je trouverai des informations telles que l'espace de noms auquel ce pod appartient et il a été automatiquement attribué à l'espace de noms par défaut.

C'est pourquoi nous avons pu le voir dans la liste lorsque nous avons entré la commande kubectl get pods car une telle commande liste tous les pods à l'intérieur de l'espace de noms par défaut.

Voici des informations sur le nœud où un tel pod spécifique a été créé ou gardé que Kubernetes distribue automatiquement une charge sur tous les nœuds travailleurs à l'intérieur du cluster et il sélectionne un nœud spécifique pour un pod spécifique, le contenu des informations sur le nœud où ce pod particulier a été créé.

Dans notre cluster à nœud unique, bien sûr, vous verrez le même nœud chaque fois que vous créerez un pod et ici était l'adresse IP d'un tel nœud, ici avec l'heure de démarrage, ici sont les étiquettes, le statut est en cours d'exécution.

Et ici se trouve une adresse B qui a été attribuée à ce pod particulier 172 17 03.

Mais veuillez noter que maintenant nous ne pourrons pas nous connecter à ce pod particulier en utilisant une telle adresse IP interne ou le port.

Afin de pouvoir se connecter aux ports, vous devez créer des services dans Kubernetes.

Et c'est ce que nous verrons un peu plus tard.

Ici ou ci-dessous, vous pouvez également découvrir quels conteneurs ont été créés à l'intérieur de ce pod.

Et il y avait un seul conteneur, voici l'ID d'un tel conteneur, voici un long ID, voici l'image qui a été utilisée pour ce conteneur particulier.

Et c'est cette image qui a été spécifiée en utilisant l'option dash dash Image lorsque nous avons créé un nouveau pod.

Voici l'ID de l'image et c'est l'ID de l'image du Docker hub car par défaut Kubernetes télécharge toutes les images depuis le Docker Hub.

Bien sûr, il est possible de configurer Kubernetes pour télécharger des images depuis d'autres dépôts.

Enregistrement des services, mais par défaut c'est Docker Hub.

Très bien, ce sont les détails sur ce pod particulier.

Et nous découvrons qu'il y avait une adresse B attribuée à ce pod, il y avait un conteneur qui a été créé à l'intérieur de ce pod.

Et voici les logs liés à la création de ce pod particulier.

Vous voyez que ce pod particulier a été attribué avec succès à la note minikube, ici était le message sur le téléchargement de l'image engine X depuis le Docker Hub, l'image a été téléchargée avec succès, le conteneur engine X a été créé et le conteneur Ingenix a été démarré.

Et cela signifie que maintenant il y avait un conteneur nginx en cours d'exécution à l'intérieur du pod de la grille.

Encore une fois, vous pouvez trouver la liste de tous les bateaux en entrant la commande kubectl get pods, et ici était un seul bateau disponible maintenant dans l'espace de noms par défaut.

Maintenant, revenons rapidement à nouveau à l'intérieur du nœud Kubernetes minikube, et listons à nouveau les conteneurs Docker et nous découvrirons qu'il y a maintenant un conteneur de plus qui a été créé dans l'exportation engine.

Donc en utilisant la flèche vers le haut, je pourrais revenir à la commande SSH que j'ai entrée auparavant.

La voici et me connecter à ce nœud à nouveau.

Entrer le mot de passe de l'utilisateur TC.

Et entrons ici docker ps.

Mais maintenant, filtrons la sortie par nom ngi NX.

Et maintenant, je découvrirai qu'il y a deux conteneurs différents ici, il y avait le premier et voici le second qui sont liés à engine X.

Voici le nom du conteneur de confiance, K eight s nginx nginx default et ainsi de suite.

Et il y avait également un autre conteneur GAE eight s pod nginx default et ainsi de suite.

Et ce second conteneur est appelé conteneur de pod.

Ici, vous voyez que l'exécutable de pod a été lancé, un conteneur a été créé et si Docker est un runtime de conteneur dans Kubernetes, il y a toujours de tels conteneurs de pod, qui sont créés pour chaque pod spécifique.

Et de tels conteneurs de pod sont créés afin de, disons, verrouiller l'espace de noms d'un pod spécifique.

Et nous avons discuté auparavant que tous les conteneurs à l'intérieur du même pod partagent en fait des espaces de noms.

Et ce conteneur, qui exécute en fait notre serveur web nginx, pourrait être arrêté, pourrait être recréé par Kubernetes.

Mais le pod reste intact.

Et ce second conteneur, qui est appelé conteneur de pod, est requis pour garder l'espace de noms du pod.

Très bien, c'est à quoi ressemblent les conteneurs maintenant.

Et essayons en fait de nous connecter à ce conteneur où nous exécutons le service nginx.

Afin de se connecter au conteneur, vous pouvez utiliser soit l'ID, celui-ci, soit ce nom.

Connectons-nous au conteneur par cet ID, veuillez sélectionner ce conteneur, notez le conteneur de pause.

Et entrons la commande Docker Exec.

C'est l'ID ici, c'était l'ID du conteneur.

Et connectons ce conteneur en utilisant l'exécutable SHA.

Maintenant, je suis à l'intérieur du conteneur.

Vérifions son nom d'hôte.

Ingenix.

C'est en fait le nom du pod.

Et le même nom a été attribué à ce conteneur.

Et vérifions également l'adresse IP de ce conteneur, voici une telle adresse 172 17 03.

Et c'est cette adresse IP que nous avons vue dans les détails du pod.

Maintenant, essayons de nous connecter au serveur web qui s'exécute à l'intérieur de ce conteneur où nous sommes actuellement en utilisant cette adresse IP.

Et pour cela, nous pouvons utiliser la commande curl et voici l'adresse IP de ce conteneur particulier.

Quoi qu'il en soit, nous sommes à l'intérieur du conteneur nginx.

Essayons d'établir une connexion.

Et ici, je vois la page de bienvenue à nginx qui a été retournée par ce serveur web.

Cela signifie que le serveur web nginx est opérationnel.

Sortons de ce conteneur et maintenant nous sommes toujours à l'intérieur du nœud Kubernetes.

D'accord, mais nous avons établi une connexion SSH avec lui.

Et maintenant, sortons de cette connexion également comme cela.

Et maintenant, entrons la commande suivante kubectl get pods this all white et avec une telle option, vous trouverez également l'adresse IP du pod particulier dans cette sortie, voici la même adresse IP, que nous venons de voir à l'intérieur du conteneur.

Essayons maintenant de nous connecter à une telle adresse P depuis notre ordinateur, notre ordinateur est externe par rapport à notre cluster Kubernetes, car le nœud Kubernetes s'exécute à l'intérieur de la machine virtuelle.

Et cette adresse IP a été attribuée par Docker à un conteneur particulier à l'intérieur du nœud.

Essayons de nous connecter à une telle adresse IP, je pourrais utiliser la même commande CRL.

La voici, disponible sur Mac.

Ou vous pouvez simplement ouvrir un navigateur web et vous connecter à cette adresse IP.

Et vous découvrirez que vous ne pourrez pas vous connecter au conteneur nginx comme cela.

Parce que, comme je vous l'ai dit auparavant, une telle adresse IP est une adresse IP interne du pod et vous n'êtes pas en mesure de vous connecter à un tel pod depuis l'extérieur, en dehors de la salle de classe.

Super.

C'est ainsi que nous avons créé le tout premier pod dans notre cluster Kubernetes.

Et nous avons également exploré la queue de ce pod.

Et j'espère que maintenant, il est clair pour vous ce qui se passe lorsque vous créez un pod à l'intérieur du pod, Kubernetes crée un conteneur.

Et afin de créer un conteneur, il doit extraire l'image de Docker Hub.

Et dans notre exemple, l'image nginx a été extraite et un nouveau conteneur a été créé sur la base de cette image.

De plus, nous sommes allés à l'intérieur du conteneur et avons vérifié que le serveur web nginx est maintenant en cours d'exécution.

Mais nous ne sommes pas en mesure de nous connecter à un tel pod depuis l'extérieur, car maintenant il n'a qu'une adresse IP interne qui a été attribuée par Docker.

Mais bien sûr, la création du pod en utilisant la commande kubectl Run n'est pas vraiment pratique, car vous n'êtes pas en mesure de mettre à l'échelle.

Et par exemple, augmenter la quantité de pods, il n'y avait qu'un seul pod, que nous avons créé en utilisant la commande kubectl Run.

C'est pourquoi maintenant, supprimons simplement le pod créé pour cela, il y a la commande kubectl Delete.

Prochain sera le nom de la ressource que nous aimerions supprimer et le Dysport et ici sera le nom du pod dans notre exemple Ingenix car nous avons spécifié le nom du site pour le pod manuellement lorsque nous avons entré la commande kubectl Run.

Alors, allons-y et supprimons le pod Sasha acheté Ingenix supprimé, kubectl get pods et il n'y a pas de ressources trouvées dans l'espace de noms par défaut et un tel pod a simplement disparu.

Et tous les volumes, tous les espaces de noms liés à ce pod particulier ont été supprimés.

Super.

Vous avez peut-être remarqué que nous avons entré la commande kubectl plusieurs fois et à mon avis, une telle commande est relativement longue.

Et nous sommes en mesure de créer un alias pour une telle commande afin de gagner du temps à l'avenir.

Et nous pourrions aliaser la commande kubectl à une seule lettre K.

Et ensuite, nous entrerons de telles commandes comme K get ports.

Mais maintenant, si j'entre une commande de recherche, j'obtiendrai l'erreur de commande introuvable car je n'ai pas encore créé d'alias.

Sur les systèmes d'exploitation de type Linux, vous pouvez très facilement créer des alias en entrant la commande alias.

Prochain sera un alias pour la commande puis signe égal et après le signe égal en doubles guillemets vous pourriez écrire la commande que vous aimeriez aliaser dans notre exemple kubectl si vous êtes un utilisateur Windows et si vous utilisez PowerShell cette commande ne fonctionnera pas là.

Si vous voulez obtenir une expérience similaire à la mienne en ligne de commande, je vous recommande d'installer Git Bash.

Afin de l'installer, veuillez naviguer vers get SCM comm et simplement télécharger Git.

Si git est déjà installé sur votre ordinateur Windows, vous avez déjà accès à Git Bash, c'est un autre terminal.

Si vous n'avez pas Git installé, veuillez aller dans la section Windows ici et télécharger git pour windows, voici différents liens pour manger.

Et après l'installation, veuillez ouvrir le terminal Git Bash au lieu de la power shell.

Donc, j'ai déjà la commande alias disponible dans ce terminal sur Mac OS.

Par conséquent, je serai en mesure de créer un tel alias, créons LS LS a été créé et maintenant je suis en mesure d'utiliser juste une version courte de la commande K get pods et maintenant je vois la sortie, aucune ressource trouvée dans l'espace de noms par défaut.

À partir de ce point, j'utiliserai une telle version courte de la commande kubectl, mais veuillez noter que cet alias ne durera que pendant cette session dans le terminal.

Après avoir chargé l'ordinateur ou lorsque vous ouvrez une autre session de terminal.

Cet alias aura disparu.

Si vous le souhaitez, vous pourriez créer un alias permanent, bien sûr, il est possible de le faire, afin d'effectuer une telle tâche, vous devez modifier votre profil de configuration de shell.

Mais je ne le ferai pas maintenant, il est suffisant d'avoir juste un alias temporel.

Super.

Maintenant, continuons.

Comme je l'ai mentionné auparavant, il n'est pas pratique de créer des pods séparés à l'intérieur du cluster Kubernetes, car vous n'êtes pas en mesure de mettre à l'échelle et d'augmenter la quantité de pods.

Par conséquent, la manière la plus courante de créer plusieurs pods, lorsque vous êtes en mesure d'augmenter la quantité de pods, de diminuer la quantité, de modifier la configuration, etc., est d'utiliser un déploiement.

Et le déploiement sera responsable de la création des pods réels.

Mais veuillez noter que tous les pods à l'intérieur du déploiement seront les mêmes, exactement les mêmes.

Mais vous pouvez créer plusieurs copies du même pod et distribuer la charge sur différents nœuds dans le cluster Kubernetes, c'est le but du déploiement.

Maintenant, allons-y et créons un déploiement.

Et nous utiliserons la même image que nous avons utilisée auparavant, c'est l'image nginx.

Et ensuite, nous augmenterons la quantité de pods dans ce déploiement.

Et nous créerons également un service pour ce déploiement afin de pouvoir nous connecter à notre déploiement depuis l'extérieur.

Allons-y et créons ce déploiement.

Et pour cela, nous utiliserons la commande kubectl create deployment, nous avons déjà aliasé la commande kubectl.

C'est pourquoi j'entrerai key create deployment.

Et ensuite, ce sera le nom du déploiement.

Appelons-le Ingenix.

Et ensuite, spécifions également l'image de manière similaire à ce que nous avons fait dans la commande kubectl Run.

Et ici, après le signe égal, ce sera le nom de l'image que nous aimerions utiliser pour ce déploiement.

Et entrons ici Nginx.

Afin d'éviter toute confusion, modifions le nom de ce déploiement.

Et appelons-le par exemple Ingenix.

Ce déploiement comme cela, allons-y et créons ce déploiement.

Le déploiement a été créé avec la commande ant ou K get deployments.

Il y avait un seul déploiement, il est prêt et à jour.

Et entrons K get pods.

Et maintenant je vois qu'il n'y a pas de pod unique qui est géré par ce déploiement particulier.

Et un tel pod a été créé automatiquement après que nous ayons créé un tel déploiement.

Et maintenant ce pod est géré par ce déploiement.

Il n'y avait qu'un seul pod à ce moment-là.

Et bien sûr, il est possible de mettre à l'échelle la quantité de pods et de diminuer le nombre de pods souhaités, par exemple 2, 3, 5, etc.

Mais d'abord, avant de faire cela, lisons les détails sur ce déploiement.

Et pour cela, entrons la commande gay describe deployment.

Et ici sera le nom du déploiement nginx deployment.

Voici les détails du déploiement créé.

Faisons défiler un peu vers le haut.

Et ici, au début de la sortie, je vois le nom du déploiement engine X deployment.

C'est ce nom, qui a été donné à ce déploiement par nous, ici était l'espace de noms où notre déploiement sash a été créé, l'espace de noms par défaut ci-dessous, vous verrez que Kubernetes a automatiquement attribué toutes les étiquettes à ce déploiement particulier.

Et il n'y avait qu'une seule étiquette up égal signe engine X deployment.

Il y a aussi des annotations, à nouveau créées automatiquement, ici était l'annotation.

Et il y avait aussi un sélecteur, les sélecteurs sont utilisés afin de connecter les pods avec les blueprints.

Parce que dans Kubernetes, les pods et les déploiements sont en fait des objets séparés.

Et nous devons savoir comment assigner des pods spécifiques à des déploiements particuliers.

Et ici, nous voyons le sélecteur up égal signe nginx deployment et pour un pod particulier, qui a été automatiquement créé et assigné à ce déploiement, nous trouverons une étiquette avec la même valeur up égal signe nginx deployment, nous jetterons un coup d'œil à cela dans une minute.

Il y avait aussi un champ réplica et ici vous pouvez trouver des informations sur la quantité de pods, qui sont souhaités par ce déploiement et la quantité réelle de pods qui sont en cours d'exécution, ici il n'y avait qu'un seul pod, une seule réplique qui est souhaitée, une mise à jour, un total et une disponible.

Cela signifie que maintenant il y avait un pod qui est assigné à ce déploiement, il y avait aussi un type de stratégie de mise à jour progressive, qui indique comment effectuer les mises à jour des déploiements.

Nous y reviendrons un peu plus tard dans ce cours.

Et aussi ci-dessous, vous trouverez d'autres détails sur ce déploiement particulier.

Ici, vous trouverez tous les détails sur le modèle de pod.

Et comme je viens de vous le dire, vous découvrirez à l'intérieur du pod l'étiquette correspondante up égal signe nginx deployment.

Et la même étiquette est mentionnée ici dans le champ sélecteur dans le déploiement.

Et c'est ainsi que le déploiement est connecté à des pods particuliers.

De plus, si vous faites défiler un peu vers le bas, vous trouverez les événements réels liés à ce déploiement particulier.

Et ici, nous voyons un seul événement de mise à l'échelle du jeu de réplicas.

Mais qu'est-ce qu'un jeu de réplicas, un peu plus haut, vous voyez un nouveau jeu de réplicas nginx deployment et l'ID du jeu de réplicas.

Et le jeu de réplicas gère en fait tous les pods liés au déploiement.

Et le jeu de réplicas est un ensemble de réplicas de votre application, car vous pouvez créer 5, 10, 100 différents pods dans le même déploiement.

Et tous sont inclus dans le jeu de réplicas.

Et c'est pourquoi ici, vous voyez que le jeu de réplicas a été mis à l'échelle à un et un pod a été créé dans ce jeu de réplicas.

Super, ce sont les détails sur ce déploiement particulier.

Et maintenant, jetons à nouveau un coup d'œil à la liste des pods get pods, il y avait un seul pod et notez son nom.

Il commence par le nom du jeu de réplicas, que nous venons de discuter.

Et donc dans la sortie des détails du déploiement, nginx deployment et ce hachage, et ensuite, il y avait un hachage spécifique pour ce pod particulier.

Et s'il y a plusieurs pods dans le même déploiement, qui appartiennent au même jeu de réplicas, vous verrez les mêmes graphiques ici, mais différents hachages ici pour différents pods.

Maintenant, il y aura un seul pod, qui est prêt, et nous venons de le créer.

De plus, nous pourrions obtenir les détails sur ce pod particulier, prenons son nom, et entrons ici gay describe pod.

Et ici, collons le hachage corporatif.

Et voici les détails sur ce pod particulier.

Faisons défiler vers le haut.

Il y avait le nom du pod, il correspond à ce nom.

Il a été attribué à l'espace de noms par défaut, comme le déploiement.

Voici le nœud où ce pod particulier est en cours d'exécution, voici les étiquettes de ce pod particulier.

Et je vois une étiquette telle que up nginx deployment et pod template hash.

Remarquez que ce hachage est égal à ce hachage.

Et il correspond à l'ID du jeu de réplicas.

De plus, isis qui était en cours d'exécution ici était l'adresse IP du pod.

Et ici, je vois que cela est contrôlé par un jeu de réplicas spécifique, jeu de réplicas nginx deployment.

Et voici un hachage du jeu de réplicas, qui contrôle ce pod particulier.

De plus, voici les détails sur les conteneurs qui sont en cours d'exécution à l'intérieur du pod.

Et voici l'ID du conteneur et l'image qui a été utilisée pour la création du conteneur dans ce pod particulier.

De plus, à la fin, vous pouvez trouver les logs liés au pod, comme nous l'avons discuté auparavant, attribué avec succès à un nœud spécifique, extraction de l'image nginx, etc.

Maintenant, il y avait un déploiement.

Et au lieu du déploiement, il y avait un jeu de réplicas.

Et les pods sont gérés par ce déploiement.

Maintenant, il n'y avait qu'un seul pod.

Super.

Maintenant, essayons de mettre à l'échelle ce déploiement et d'augmenter la quantité de pods à l'intérieur du déploiement.

Maintenant, il y avait un seul pod pour cela, nous pourrions utiliser la commande suivante kubectl.

En bref, Kay dans notre cas, scale, nous aimerions mettre à l'échelle le déploiement.

Écrivons ici deployment.

Nom du déploiement dans notre cas est Nginx.

Ce déploiement.

Et ensuite, spécifions l'un des réplicas que nous aimerions avoir dans ce déploiement maintenant.

Maintenant, il y aura un seul réplica.

Afin de spécifier la quantité souhaitée de réplicas, nous pourrions ajouter ici l'option réplicas, puis après le signe égal, spécifier la quantité de réplicas.

Disons que nous voulons mettre à l'échelle à cinq réplicas.

Entrons le fichier ici.

Et mettons à l'échelle notre déploiement.

Le déploiement a été mis à l'échelle et maintenant entrons la commande gate get votes.

Et je vois qu'il y a quatre nouveaux conteneurs qui sont actuellement en cours de création.

Voici un pod, le deuxième, le troisième et le quatrième pod.

Et ce pod est toujours en cours d'exécution.

En un instant, vous devriez voir que les cinq pods seront en cours d'exécution.

Les voici.

Nous venons de mettre à l'échelle notre déploiement à cinq réplicas différents.

Et maintenant, il y a cinq pods différents en cours d'exécution dans notre cluster Kubernetes.

Et remarquez à quel point c'est facile, nous n'avons pas créé ces pods manuellement, Kubernetes a mis à l'échelle ce déploiement automatiquement pour nous.

Remarquez que tous ces pods ont le même préfixe, c'est le nom du jeu de réplicas auquel ils appartiennent tous.

Et ces parties sont différentes pour les différents pods.

Et encore une fois, tous les pods sont en cours d'exécution.

Lisons également les détails sur ces pods, qui incluront les adresses IP, ajoutons ici l'option this all white.

Et je verrai que chaque pod a une adresse IP différente ici ou ici, ici, ici ou ici.

Et tous ces pods ont été créés sur un seul nœud minikube, car encore une fois, nous avons ici un cluster à nœud unique.

Si vous exécutiez plusieurs nœuds, bien sûr, une charge serait distribuée sur différents nœuds.

Et vous verriez que les pods ont été attribués à différents nœuds.

Très bien, maintenant essayons de réduire la quantité de réplicas dans ce déploiement.

de cinq à, disons, trois.

Revenons à cette commande, K, scale deployment nginx deployment.

Et ici, spécifions que je veux faire les réplicas comme trois comme cela.

Le déploiement a été mis à l'échelle, obtenons les pods.

Et je vois que maintenant il n'y a que trois pods en cours d'exécution et prêts, deux pods ont été supprimés.

Super.

Maintenant, essayons de nous connecter à l'un des pods.

Par exemple, celui-ci, saisissons son adresse IP.

Et avant, nous avons déjà essayé de nous connecter à l'un des pods depuis notre ordinateur local, et encore une fois, notre ordinateur local est externe par rapport au cluster Kubernetes, c'est très, très important.

Essayons de nous connecter à cette adresse IP CRL et collons l'adresse IP et la connexion n'est pas réussie.

Maintenant, allons à l'intérieur du nœud, le nœud minikube et essayons de nous connecter à ce pod, l'un de ces pods depuis l'intérieur du nœud.

Et cela signifiera que nous essayons de nous connecter au pod à l'intérieur du cluster.

SSH à nouveau à notre nœud minikube en tant que sage, Docker, apt et cette adresse IP.

Dans votre cas, cette IP est bien sûr différente, le mot de passe est DC user.

Et maintenant ici, voyons URL et entrons l'adresse IP de l'un des pods.

N'importe quel pod fonctionne ici.

Donc voyons URL et j'ai pu me connecter à un pod spécifique par son adresse IP.

Essayons de nous connecter à un autre pod avec une autre IP.

Par exemple, listez y 0.3.

Je ne suis pas sûr d'avoir un tel pod en cours d'exécution.

Oui, j'en ai un.

Et j'ai également obtenu une réponse d'un tel pod avec de tels liens sans fin, rappelons que maintenant je suis situé à l'intérieur du nœud.

Et je suis en mesure de me connecter aux pods qui s'exécutent sur ce nœud spécifique en utilisant les adresses IP de ces pods.

Sortons de ce nœud.

Et encore une fois, listons les pods avec une adresse.

Donc j'ai pu me connecter à ce pod et à ce pod depuis le nœud.

Mais bien sûr, de telles adresses IP sont attribuées aux pods de manière dynamique lorsque les pods sont créés.

Et vous ne devriez pas vous fier aux adresses IP des pods si vous souhaitez vous connecter à un pod spécifique.

Par conséquent, il n'est pas pratique d'utiliser de telles adresses IP.

Et vous devriez utiliser un autre type d'adresses IP qui sont gérées par Kubernetes et qui vous permettent de vous connecter à l'un des pods à l'intérieur du déploiement.

Laissez-moi vous montrer comment faire cela.

Dans Kubernetes.

Vous devez créer ce que l'on appelle des services si vous souhaitez vous connecter à des déploiements spécifiques en utilisant des adresses IP spécifiques.

Et il existe différentes options disponibles, vous pouvez créer ce que l'on appelle cluster IP et une telle adresse IP sera créée et attribuée à un déploiement spécifique et vous serez en mesure de vous connecter à ce déploiement spécifique à l'intérieur du cluster en utilisant cette adresse IP virtuelle.

Et Kubernetes distribuera la charge sur différents pods qui sont attribués à un déploiement spécifique, mais veuillez noter qu'une telle adresse IP sera juste une seule adresse IP pour l'ensemble du déploiement.

Et bien sûr, il est beaucoup plus pratique d'utiliser une telle adresse IP que des adresses IP spécifiques des pods comme nous venons de l'essayer.

De plus, il y avait une option pour créer des adresses IP externes pour exposer le déploiement au monde extérieur.

Et il est possible d'exposer un déploiement spécifique à l'adresse IP du nœud ou d'utiliser un équilibreur de charge ou d'obtenir à l'intérieur du cluster Kubernetes, il est possible d'avoir plusieurs nœuds et les pods pourraient être distribués sur différents nœuds.

Par conséquent, la solution la plus courante est d'avoir une adresse IP d'équilibreur de charge, qui sera juste une seule pour l'ensemble du cluster Kubernetes pour un déploiement spécifique.

Et vous serez en mesure de vous connecter à votre déploiement peu importe où les pods sont créés en utilisant juste une seule adresse IP externe.

Mais de telles adresses IP d'équilibreur de charge sont généralement attribuées par un fournisseur de cloud spécifique comme Amazon Web Services, ou Google Cloud.

Et de telles attributions sont gérées par le gestionnaire de contrôleur cloud, un service qui s'exécute sur le nœud maître.

Essayons maintenant de créer un cluster IP pour notre déploiement.

Et nous créerons pour cela un service spécifique.

Nous avons déjà un déploiement créé, lisons les détails sur ce déploiement, Kay, get deployments.

D'ailleurs, vous pourriez raccourcir une telle route longue à simplement déployer comme cela get deployed.

Et voici le nom de notre déploiement.

Maintenant, il y a trois pods différents, qui sont déjà dans ce déploiement.

Créons maintenant un service pour ce déploiement particulier.

Et en utilisant un service, vous pourriez exposer un port spécifique du déploiement.

Maintenant, nous exécutons trois pods différents.

Et à l'intérieur de chaque pod, il y avait un conteneur nginx.

Et par défaut, le serveur web nginx s'exécute sur le port 80.

Cela signifie que nous devons exposer le port interne 80 des conteneurs à tout autre pod à l'extérieur du déploiement.

Et nous pouvons choisir par exemple le port 8080.

Pour cet exemple particulier, afin d'exposer le port interne du déploiement des pods, vous devez utiliser la commande expose, entrons la commande gay expose deployment.

Ici sera le nom du déploiement pour lequel nous aimerions créer un service.

Ici était le nom de notre déploiement.

Rappelons que nous ne mentionnons pas ici les ports, nous travaillons avec des déploiements.

Et les ports sont gérés par les déploiements.

Donc, exposons le déploiement engine X, ici sera l'option port, spécifions un port que nous aimerions utiliser comme port externe pour notre déploiement.

Et définissons-le sur le port 8080.

Et nous devons également ajouter ici le port cible, si le port à l'intérieur des conteneurs est différent de ce port que nous spécifions maintenant ici.

Et dans notre exemple, maintenant, le port à l'intérieur du conteneur est âgé.

C'est pourquoi nous devons ajouter ici l'option target port égal signe 80, donc nous exposons le port interne des conteneurs au port externe 88.

Et nous faisons cela pour le déploiement des héros, le nom du déploiement.

Très bien, exposons le déploiement nginx, le service engine est exposé et maintenant listons les services pour cela, il y avait la commande gay get services.

Et maintenant, il y a deux services, le service Kubernetes est le service système par défaut.

Il est appelé Kubernetes, le type est cluster ID et voici l'adresse IP du cluster.

Et aussi ici, nous voyons un autre service sérieux nginx deployment.

Il y avait le nom, il y avait le type cluster IP et ici était cluster IP.

Et cette adresse IP est complètement différente de l'adresse IP attribuée aux pods, cette adresse IP provient même d'un autre réseau, les adresses IP des pods commencent par 172.

Et ici, cette adresse IP commence par 10 et c'est une adresse IP virtuelle qui a été créée par Kubernetes et c'est juste une seule adresse IP qui pourrait être utilisée afin de se connecter à l'un des pods et un tel type cluster IP vous permet de vous connecter à un déploiement spécifique dans notre exemple nginx deployment uniquement depuis l'intérieur du cluster Kubernetes.

Par exemple, si dans votre cluster Kubernetes, il y avait un déploiement de base de données, par exemple, il y avait une base de données MongoDB ou une base de données my SQL.

Et la base de données de recherche ne doit pas être disponible et accessible depuis l'extérieur, vous pourriez créer un service cluster IP pour un tel déploiement de base de données et d'autres déploiements à l'intérieur de votre cluster Kubernetes, pourront se connecter au déploiement de base de données en utilisant cluster IP.

Mais encore une fois, le déploiement de session sera caché du monde extérieur.

Mais d'un autre côté, si vous créez un déploiement de service web, et qu'il doit être disponible depuis l'extérieur, bien sûr, vous devez l'exposer au monde extérieur en utilisant node port ou load balancer.

C'est ce que nous essaierons un peu plus tard.

Cluster IP sera disponible uniquement à l'intérieur du cluster.

Donc ici, nous voyons l'adresse IP du cluster.

La voici, et voici le port qui a été exposé par notre déploiement.

De plus, vous pouvez obtenir la liste des services en utilisant la version courte de cette commande, entrez simplement gay get SVC, c'est la version courte des services SVC.

Et le résultat sera le même.

Il y a maintenant deux services différents avec ces trois dernières adresses IP, celle-ci pour le service Kubernetes, et celle-ci pour le service nginx deployment.

Et maintenant, essayons de nous connecter à notre déploiement en utilisant ce service.

Prenons cette adresse IP du cluster.

Et essayons d'abord de nous connecter à cette adresse IP du cluster depuis notre ordinateur local.

Voir URL et coller cette adresse IP.

Et après le froid, ajoutons également le port que nous avons exposé.

C'est le port externe pour notre déploiement.

En interne, il sera proxy vers le port 80 sur chaque conteneur.

Essayons si cela fonctionne sur notre ordinateur local ou non CRL.

Et je ne vois aucune réponse.

C'est ce que je viens de vous dire.

L'adresse IP du cluster n'est pas disponible en dehors du cluster Kubernetes.

Ce comportement de l'IP du cluster est juste une adresse IP disponible en interne, mais vous êtes en mesure d'accéder à l'IP du cluster depuis n'importe quel nœud.

Et essayons cela.

Faisons un SSH vers notre nœud.

Laissez-moi revenir à cette commande, SSH Docker et l'adresse IP du nœud DC user.

Et maintenant, essayons de nous connecter à l'IP du cluster depuis le nœud.

Et ici encore, spécifions le port 8080.

Et je vois le résultat Bienvenue à Ingenix.

Et cette réponse a été fournie par l'un des pods du déploiement.

Bien sûr, maintenant, à partir de cette sortie, je ne suis pas en mesure de reconnaître quel pod m'a exactement répondu.

Mais cette réponse a été fournie par l'un des pods du déploiement.

Je pourrais essayer à nouveau.

Encore une fois, et j'obtiens une réponse des pods du déploiement.

C'est ainsi que cela fonctionne.

Cluster IP est juste une seule IP qui a été créée comme un service pour un déploiement particulier.

Et vous pouvez utiliser une seule IP afin de vous connecter à l'un des pods et derrière les scènes, Kubernetes effectue tout le proxying de la demande vers un pod sélectionné particulier et il équilibre la charge sur différents pods du déploiement.

Très bien, fermons cette connexion et lisons aussi les détails sur un service particulier, nous obtiendrons là avec la commande K get SVC, version courte pour get services et il y avait le nom du service que nous avons créé avant.

Prenons ce nom et maintenant K describe service et le nom du service auquel nous aimerions obtenir des détails, voici Gloucester IP que nous venons d'utiliser afin de nous connecter à cette série.

Aussi, il y avait un port externe et ici était le port cible.

Et ici, il y a trois points de terminaison différents.

Ces points de terminaison indiquent des pods particuliers, qui sont utilisés pour les connexions à ce cluster IP particulier.

Ainsi, la charge sera équilibrée sur ces trois pods différents.

Et remarquez partout ici le port 80.

C'est le port cible pour notre service, Dysport, ad est le port par défaut où le serveur Ingenix est exécuté.

Donc AD AD et AD aussi ici, vous voyez le type de service cluster IP, et le sélecteur est également présent up égal signe Ingenix deployment.

Et c'est ainsi que ce service est en fait connecté à des pods particuliers.

Tous ces pods ont également une étiquette particulière up nginx deployment.

Et cette étiquette a été créée par Kubernetes.

Automatiquement, nous ne l'avons pas spécifiée, car nous avons simplement créé le déploiement en utilisant la commande grid deployment.

Et nous avons créé un service en utilisant la commande expose.

L'espace de noms ici est par défaut, comme pour les pods et le déploiement, qui s'appelle Nginx.

Deployment.

Très bien, c'est tout pour ce service.

Et nous avons exposé notre déploiement en utilisant cluster IP.

Et cluster IP est uniquement disponible à l'intérieur des clusters Kubernetes.

Maintenant, vous savez comment créer un pod, comment créer un déploiement, comment mettre à l'échelle un déploiement, et comment créer un service pour un déploiement particulier.

Et nous avons utilisé l'image Ingenix qui est disponible sur Docker Hub.

Et maintenant, il est temps de passer à l'étape suivante dans notre plan.

Et je vous ai promis que nous créerions une image Docker personnalisée, la pousserions vers Docker Hub, et ensuite créerions un déploiement basé sur cette image.

Et c'est ce que nous ferons ensuite.

Mais avant de faire cela, supprimons le service et le déploiement existants afin d'avoir une configuration propre, disons.

Alors, supprimons le déploiement key delete deployment.

Et ici sera le nom du déploiement nginx deployment.

Et aussi, supprimons le service gate delete series Ingenix deployment comme cela, le service a été supprimé également.

Listons maintenant les déploiements gate get deploy, la version courte des déploiements, aucune ressource trouvée, et listons les services gay get SVC, juste un seul service par défaut avec le nom Kubernetes.

Nous sommes prêts à partir.

Et maintenant, créons une application Node js très basique.

Ils sont, nous utiliserons le package serveur web Express et créerons notre serveur web personnalisé.

Le plan pour cette prochaine étape est le suivant : nous créerons une application web Express no GS et nous configurerons un serveur web de telle sorte qu'il répondra avec le nom d'hôte du serveur.

Lorsque nous nous connectons à lui en utilisant une URL racine et de cette manière, nous pourrons distinguer quel pod répond en fait à une requête spécifique.

Nous conteneuriserons également une telle application en utilisant un fichier Docker et la commande Docker build.

Et ensuite, nous la pousserons vers Docker Hub.

Et enfin, nous créerons un déploiement en utilisant une telle image construite de manière personnalisée.

Vous pouvez trouver tous les fichiers de projet finaux dans le dépôt GitHub, vous trouverez un lien vers celui-ci ici.

Mais je vous recommande vivement de créer une telle application vous-même même si vous ne connaissez pas beaucoup no GS et express.

Et bien sûr, je vous recommande de construire votre image personnalisée et de la pousser vers votre compte Docker Hub.

Bien sûr, vous pouvez utiliser les images disponibles sous Mon Compte.

Ils sont publics, c'est à vous de voir.

Alors, ouvrons Visual Studio code.

Si vous ne l'avez pas, veuillez l'installer.

Je vais l'ouvrir.

Et ici, dans Visual Studio Code, veuillez ouvrir le terminal intégré en appuyant sur la combinaison de touches Ctrl backtick comme cela, le terminal a été ouvert.

Et maintenant, créons un dossier pour nos fichiers de projet.

Je vais me déplacer vers le bureau.

Et ici, en utilisant la commande make directory, je vais créer un dossier gate eight S pour Kubernetes.

Comme vous le savez déjà, voyons le dossier 2k eight s et vous pouvez ouvrir n'importe quel dossier en utilisant la commande code dot si vous avez correctement installé Visual Studio code.

Si une telle commande n'est pas disponible sur votre ordinateur, vous pouvez appuyer sur la combinaison de touches Command Shift B ou Ctrl Shift B sur Windows et ici, entrer gold et sélectionner Show command install gold command in path et ensuite, la commande gold sera disponible depuis n'importe quel terminal.

Donc, j'ai déjà cette commande disponible dans le passé.

C'est pourquoi j'ouvrirai le dossier K eight s dans l'éditeur Visual Studio Code.

Donc, code.it sera ouvert dans la nouvelle fenêtre comme cela.

Maintenant, ce dossier est complètement vide et n'a pas de fichiers.

Laissez-moi ouvrir à nouveau le terminal intégré ici.

Il sera ouvert dans le dossier K eight s.

Et maintenant, ici, créons un dossier pour notre premier projet.

Et le nom de ce dossier sera, disons, gay.

Eight s, ce web, ce Hello, car nous allons construire une application web très basique, qui répondra simplement hello depuis Sarah et le nom du serveur.

Donc, gay a s web Hello.

Et ici, dans ce dossier, nous créerons une application Node js.

Allons-y, dans le terminal, CD vers le dossier K eight s web Hello comme cela.

Et ici, nous allons initialiser l'application Node js.

Et pour ce faire, vous devez installer NPM sur votre ordinateur.

Si vous n'avez pas no GS et NPM disponibles, veuillez vous rendre sur no GS download.

Voici le lien, téléchargez no Gs, et installez no GS depuis votre ordinateur, il sera installé avec NPM.

Bien sûr, nous n'exécuterons pas l'application en utilisant Node js sur nos ordinateurs, nous exécuterons l'application à l'intérieur du conteneur dans le cluster Kubernetes à la place.

Mais afin d'initialiser le projet localement et d'installer les dépendances, vous devez utiliser NPM.

Donc, veuillez installer no GS avec NPM.

Je vais masquer cette douleur.

Et maintenant, ici, laissez-moi NPM in it.

Et je vais initialiser ce projet.

Et vous pouvez ajouter ici l'option dash y, qui gardera toutes les réponses pour vous pendant l'initialisation du nouveau projet node js.

Donc, NPM in it, c'est pourquoi le nouveau projet a été initialisé.

Et ici, vous devriez trouver maintenant le fichier package.json avec un tel contenu, le nom du projet, la version, etc.

Et maintenant, installons un package appelé Express et BM install Express.

Il sera téléchargé depuis le registre NPM, le package a été installé et le fichier package.json a été mis à jour, voici la dépendance no appelée Express.

Donc maintenant, créons le fichier index.js dans notre dossier K eight s web Hello.

D'ailleurs, notez que maintenant il y avait un dossier node modules, qui contient toutes les dépendances de notre projet.

Mais maintenant, il est sûr de simplement supprimer ce dossier, nous n'en avons plus besoin, car nous n'exécuterons pas ce projet localement avec l'aide de node.

Donc, sélectionnez simplement ce dossier et supprimez-le.

Très bien, maintenant nous avons seulement les fichiers package.json et package log.json.

Super.

Maintenant, créons un fichier et nous le créerons à l'intérieur du dossier gay eight s web Hello.

D'ailleurs, notez que maintenant il y avait un dossier node modules, qui contient toutes les dépendances de notre projet.

Mais maintenant, il est sûr de simplement supprimer ce dossier, nous n'en avons plus besoin, car nous n'exécuterons pas ce projet localement avec l'aide de node.

Donc, sélectionnez simplement ce dossier et supprimez-le.

Très bien, maintenant nous avons seulement les fichiers package.json et package log.json.

Super.

Maintenant, créons un fichier et nous le créerons à l'intérieur du dossier gay eight s web Hello.

Donc, nouveau fichier, et appelons-le index.dot m j s y m car nous utiliserons la syntaxe des modules EF six, qui est disponible dans Node js à partir de la version 13.

Et si vous souhaitez utiliser des instructions d'importation, au lieu des instructions require, vous devez nommer les fichiers avec l'extension MJS.

Donc, créons le fichier index.dot MJS.

Et ici, je ne vais pas écrire le contenu de l'application entière, je vais simplement les copier afin de gagner du temps.

Donc, collez ici.

Si vous le souhaitez, vous pourriez bien sûr écrire cette application très petite vous-même.

Donc, nous importons Express depuis le package Express.

Nous importons également oils depuis oils, oils est un module intégré no GS.

Et ensuite, nous créons une application Express, voici le port 3000.

Vous pouvez spécifier un autre port si vous le souhaitez.

Et c'est le port où notre serveur web Express s'exécutera à l'intérieur du conteneur.

Ici, nous ajoutons un gestionnaire de route pour l'URL slash.

C'est une URL de route.

Et nous répondons simplement au client avec le texte Hello from their oils hostname en utilisant le package oils, nous récupérons le nom d'hôte du serveur.

Et dans la réponse du serveur, vous verrez simplement le message texte hello from there et le nom du serveur où cette application est exécutée.

Donc, la réponse envoyée, nous avons envoyé au client un tel message et nous l'avons également enregistré dans la console.

Et enfin, nous démarrons le serveur web Express Update listen, et nous avons démarré à ce port 3000 et le serveur web démarre, nous allons regarder le message de la console, le serveur web écoute au port et voici le port.

Je ne vais pas approfondir ces explications et la syntaxe de node GS car ce n'est pas un cours sur node GS.

Mais vous comprenez l'idée.

Nous créons un serveur web très basique qui répondra avec un tel message texte.

Donc, sauvegardons les modifications dans ce fichier.

Allez CTRL S sur Windows ou Command S sur Mac comme cela, les modifications ont été sauvegardées.

Et maintenant, conteneurisons cette application et pour cela, nous créerons un fichier Docker.

Maintenant, je vous recommande d'installer les extensions appelées Docker et Kubernetes.

Donc, allez dans Extensions ici et entrez throws Docker ici.

Sélectionnez Docker et cliquez sur Installer.

Dans mon cas, l'extension Docker était déjà installée.

Et ensuite, installez également l'extension Kubernetes, trouvez-la comme cela et installez-la également.

Dans mon cas, l'extension Kubernetes a été installée plus tôt.

Donc maintenant, nous sommes prêts à partir.

Et aussi, afin de construire l'image Docker réelle, vous devez exécuter Docker sur votre ordinateur.

Avant, nous n'avons pas autorisé Docker afin de démarrer un cluster Kubernetes minikube.

Mais maintenant, nous avons besoin de Docker afin de construire l'image Docker.

C'est pourquoi, veuillez installer Docker.

Si ce n'est pas installé sur votre ordinateur et ou Docker download.

Allez à ce lien et installez Docker desktop qui est disponible pour Windows Mac OS.

Et vous pouvez également installer Docker directement sur les systèmes de type Linux.

Donc, veuillez installer Docker.

Ensuite.

Veuillez l'exécuter, je vais l'exécuter comme cela.

Je l'ai déjà installé avant.

Maintenant, ici, je vois l'icône Docker qui démarre, voici les informations à ce sujet.

Je vais attendre un peu.

Pendant ce temps, créons un fichier Docker à l'intérieur du dossier K eight s web Hello.

Parce que nous créons une obligation séparée dans le dossier racine K eight s.

Donc, créons un fichier Docker ici, nouveau fichier et nommons-le Docker file comme cela.

Remarquez que Visual Studio Code reconnaît le type de ce fichier et il a ajouté l'icône Docker.

Et ici, dans le fichier Docker, ajoutons des instructions sur la façon dont nous aimerions construire l'image Docker personnalisée.

Je vais à nouveau prendre le contenu de ce fichier Docker et le coller ici afin de gagner du temps.

Et il y a les instructions suivantes.

Nous utiliserons Node Alpine comme image de base pour notre image personnalisée.

Ici, nous définissons le répertoire de travail comme slash up.

Ensuite, nous exposons le port 3000.

Ensuite, nous allons copier les fichiers package.json et package slug.json qui sont présents ici.

Et ensuite, nous exécutons npm install lorsque nous construirons cette image personnalisée.

Et après que NPM ait installé, nous copions tous les fichiers restants de ce dossier où se trouve notre fichier Docker.

Dans notre exemple, il ne s'agira que d'un seul fichier index.dot NGS.

Et ce fichier sera copié dans le dossier app à l'intérieur de l'image.

Si vous n'êtes pas familier avec ces étapes et ne savez pas ce que signifient from Rockdoor, exports, etc., je vous recommande vivement de trouver le cours intensif sur Docker et de le suivre afin de comprendre comment fonctionne Docker et comment vous êtes en mesure de construire des images personnalisées.

Ce cours n'est pas un cours sur Docker.

Donc, nous copions tous les fichiers d'application restants vers le dossier cible up.

Et enfin, nous ajoutons l'instruction CMD, qui indique en fait quelle commande sera exécutée lorsque le conteneur correspondant basé sur cette image reconstruite personnalisée sera démarré.

Et nous voulons exécuter la commande npm start.

Mais que se passe-t-il maintenant si nous entrons npm start dans notre dossier de projet.

Essayons cela.

Enregistrons ces modifications dans le fichier Docker, enregistrons.

Et ouvrons à nouveau le terminal intégré.

Je suis toujours dans le dossier K eight s web Hello.

Et ici, dans ce dossier, il y avait un fichier index both in GS.

Et ici, entrons la commande npm start.

Et ce que je vois, je vois le script start manquant.

Maintenant, notre obligation ne permettra rien si vous entrez la commande npm start.

Afin de pouvoir exécuter notre obligation de démarrage du serveur web, nous devons modifier le fichier package dot JSON.

Faisons cela.

Ouvrons le fichier package.json et ici, vous trouverez la section scripts et il y avait juste un script test par défaut.

Remplaçons en fait test par start comme cela.

Et ici, dans les doubles guillemets, tapez node index dot MJS.

Donc maintenant, il y aura un script start et il exécutera essentiellement en utilisant un nœud fichier index both NGS.

Et cela démarrera en fait notre serveur web Express sur le port 3000.

C'est ce que nous avons discuté ici.

Nous avons enregistré les modifications dans le fichier package.json.

Maintenant, NPM installé est disponible.

Et nous sommes en mesure maintenant de construire notre image.

Si vous voulez créer une image personnalisée, vous devez utiliser la commande Docker build.

Et généralement, cette commande est entrée dans le dossier où notre fichier Docker est situé.

C'est ce dossier dans notre exemple ici, et si je liste les fichiers et dossiers ici, je trouverai un fichier Docker.

Et le contenu du fichier Docker est ici from work, dir expose et ainsi de suite, do CMD maintenant, construisons une image Docker.

Et nous ajouterons également une étiquette à cette image construite de manière personnalisée.

Et cela inclura tous les noms d'utilisateur de votre compte sur Docker Hub.

Si vous n'avez pas de compte Docker Hub, veuillez vous rendre sur hub docker.com et créer un compte.

J'ai déjà un compte et voici mon nom d'utilisateur.

Veuillez créer votre compte et choisir votre nom d'utilisateur.

Et ensuite, vous serez en mesure de pousser des dépôts vers Docker Hub sous votre compte.

Et lorsque vous pousserez des dépôts, vous les trouverez ici dans la section dépôts.

Maintenant, sous Mon Compte, il n'y a pas de dépôts dans cet espace de noms.

Donc, revenons à Visual Studio code.

Et ici, construisons une image personnalisée pour notre application.

Utilisons la commande Docker build.

Ensuite, ce sera le chemin vers le fichier Docker.

J'utiliserai simplement le point car maintenant je suis à l'intérieur du dossier où le fichier Docker a été créé.

Donc, Docker build dot.

Ensuite, ajoutons une étiquette à notre image en utilisant l'option SD, puis le nom d'utilisateur de votre compte GitHub.

Dans mon cas, je taperai le mien.

Et après une barre oblique, je donnerai un nom au dépôt.

Appelons-le comme nous avons nommé ce dossier, gay eight s that's web does Hello.

Comme cela.

Construisons cette image en utilisant la commande Docker build.

Construire une image, notez que dans mon cas, l'image de base était déjà présente dans le cache et les autres couches étaient également mises en cache.

Et enfin, l'image a été construite.

Maintenant, si j'entre la commande Docker images et ajoute grep et ici sera K eight s web, je trouverai l'image qui est maintenant disponible dans notre dépôt d'images locales.

Voici le nom de l'image que nous venons de construire.

C'est la dernière car dans cette commande que je viens d'entrer, je n'ai pas spécifié d'étiquette que vous êtes en mesure de spécifier après la colonne ici.

Mais j'ai construit l'image avec la dernière pile.

C'est pourquoi la technologie ici est la dernière.

Et voici l'ID de l'image construite et la taille de l'image.

Maintenant, supposons que cette image ne coûte que la construction de l'image vers Docker Hub.

Pour ce faire, vous devez d'abord vous connecter à Docker Hub.

Pour cela, veuillez entrer la commande Docker login.

Je me suis déjà connecté avant.

C'est pourquoi Docker a utilisé les informations d'identification en cache et la connexion a réussi.

Dans votre cas, si vous entrez Docker login pour la première fois, vous serez invité à entrer le login et le mot de passe de Docker Hub.

Maintenant, je suis en mesure de pousser cette image construite vers Docker Hub.

Pour cela, j'utiliserai la commande docker push et ici sera le nom de l'image que je souhaite pousser vers un service d'hébergement de dépôt distant.

Mr Xu K s web Hello.

Allons-y et poussons-le en utilisant le dernier paquet par défaut, en poussant les différentes couches de l'image, cela prend un certain temps car l'image est trop grande.

Donc vous voyez en attente de toutes ces couches.

Et enfin, cette image a été poussée vers Docker Hub.

Laissez-moi vérifier qu'elle est apparue ici.

Actualisez la page et maintenant il y avait une image gate eight s web Hello.

Magnifique.

Cette image, d'ailleurs, est publique et vous êtes en mesure de l'utiliser également pour vos déploiements Kubernetes.

L'image est prête et prête à être utilisée sur Docker Hub.

Et maintenant, nous sommes en mesure de créer le déploiement Kubernetes basé sur cette image.

Faisons cela.

Allons au terminal ici.

Et créons un nouveau déploiement.

D'ailleurs, maintenant il n'y a pas de déploiements, Kay, get deploy.

Aucun déploiement, gave, get SVC services, aucun service, juste un seul Kubernetes.

C'est celui par défaut.

Et maintenant, créons un nouveau déploiement basé sur l'image construite de manière personnalisée.

Pour cela, utilisons d'abord la même commande que nous avons utilisée auparavant, okay, great deployment.

Okay, great deployment.

Appelons-le A S.

Web.

Hello.

Et ensuite, ce sera l'option image.

Et l'image sera be stashed up dans mon cas, slash gay eight s Web.

Hello, même nom, comme il apparaît ici lorsque j'ai poussé cette image vers Docker Hub, et même nom, comme je le vois ici.

Donc, voici mon nom d'utilisateur.

Et voici le nom du dépôt Docker.

Allons-y et créons un déploiement basé sur cette image.

Bien sûr, si vous avez effectué toutes les étapes vous-même et poussé l'image construite de manière personnalisée vers Docker Hub sous votre compte, vous pourriez utiliser ici votre nom d'utilisateur.

Donc, allons-y et créons un nouveau déploiement.

Le déploiement a été créé avec K get pods.

Maintenant, je vois que le statut de création du conteneur est le statut de ce pod, qui a été créé pour ce déploiement.

Vérifions à nouveau, toujours en création de conteneur, car il faut un certain temps pour télécharger l'image depuis Docker Hub.

Et maintenant, je vois que le conteneur est en cours d'exécution.

Ici, le nom du conteneur.

Et voici le hachage du jeu de réplicas, qui a été créé par le déploiement.

Et voici un hachage spécifique pour ce pod particulier.

Maintenant, créons un service en utilisant cluster IPL.

Et essayons de nous connecter ensuite à notre serveur web, qui s'exécute en utilisant no GS Express.

Donc, créons un service.

Pour cela, nous allons exposer le port key expose deployment.

Ici sera le nom du déploiement pour lequel nous aimerions créer un service.

Ici était le nom de notre déploiement.

Rappelons que nous ne mentionnons pas ici les ports, nous travaillons avec des déploiements.

Et les ports sont gérés par les déploiements.

Donc, exposons le déploiement engine X, ici sera l'option port, spécifions un port que nous aimerions utiliser comme port externe pour notre déploiement.

Et définissons-le sur le port 3000.

Et nous devons également ajouter ici le port cible, si le port à l'intérieur des conteneurs est différent de ce port que nous spécifions maintenant ici.

Et dans notre exemple, maintenant, le port à l'intérieur du conteneur est âgé.

C'est pourquoi nous devons ajouter ici l'option target port égal signe 80, donc nous exposons le port interne des conteneurs au port externe 88.

Et nous faisons cela pour le déploiement des héros, le nom du déploiement.

Très bien, exposons le déploiement nginx, le service engine est exposé et maintenant listons les services, get SVC.

Et voici le service nouvellement créé.

Ici était le nom du service et ici était cluster IP, qui a été créé par Kubernetes.

Et encore une fois, en utilisant une telle adresse IP, nous serons en mesure de nous connecter à notre déploiement, cela signifie que vous pouvez vous connecter à l'un des pods, vous ne sélectionnez pas à quel pod vous serez connecté, Kubernetes fait ce travail pour vous.

Et ici, nous voyons que nous avons ouvert le port 3000, exposé le port 3000.

Essayons de nous connecter à cette adresse IP de cluster et au port 3000.

Laissez-moi monter ici, cette adresse IP de cluster et bien sûr, je ne serai pas en mesure de me connecter à cette adresse IP de cluster depuis mon ordinateur local.

C'est pourquoi, comme d'habitude, connectons-nous rapidement à notre nœud minikube en tant que sage Docker à cette adresse IP 50 911.

Dans votre cas, cette adresse IP est différente.

Ici.

Notre mot de passe est DC user.

Et maintenant ici, voyons URL vers l'adresse IP du cluster et le port 3000.

C'est le port qui a été exposé depuis le déploiement.

Donc, allons-y et je vois le message hello from the gate eight s web Hello, et le nom entier du serveur où l'application no GS Express est en fait exécutée.

Et c'est le message qui provient du serveur web Express ici.

C'est là que nous le renvoyons au client hello from the et le nom d'hôte de la session.

Où que cette obligation soit exécutée.

Et cela signifie que tout fonctionne parfaitement.

Nous avons créé un déploiement basé sur l'image construite de manière personnalisée, que nous avons poussée vers Docker Hub.

Et voici le résultat et nous voyons la réponse de l'application serveur web.

Magnifique.

D'ailleurs, si vous entrez une commande CRL comme cela, vous serez automatiquement déplacé vers la nouvelle invite, et vous resterez sur cette ligne.

Si vous voulez passer à la nouvelle ligne, vous pouvez entrer un C URL, puis ajouter un point-virgule et ajouter ici act comme cela.

Et maintenant, vous serez déplacé vers la nouvelle ligne ici dans la sortie.

Magnifique.

Maintenant, nous avons obtenu une réponse du même pod.

Ici, nous voyons le même nom d'hôte, comme nous l'avons vu ici.

Maintenant, gardons cette fenêtre ouverte ici.

Et augmentons la quantité de sondages dans notre déploiement.

Mettons à l'échelle notre déploiement.

J'ouvrirai un nouvel onglet dans l'application item, vous pouvez ouvrir une nouvelle fenêtre de terminal si vous êtes sur Windows, j'utiliserai la combinaison de touches Command T afin d'ouvrir un nouvel onglet ici.

Et ici, dans le nouvel onglet.

Si j'entre key, je dirai erreur de commande introuvable car l'alias fonctionne uniquement dans cet onglet.

C'est pourquoi, créons à nouveau l'alias, alias k égal signe cube CTL.

D'ailleurs, vous pouvez omettre les doubles guillemets ici, si une commande se compose d'un seul mot.

Donc, laissez-moi supprimer ces doubles objectifs comme cela.

Alias a été créé.

Et maintenant, gay get pods.

Et ici, je vois le même nom du pod, que j'ai vu ici dans la réponse du serveur web.

Connaissons maintenant l'échelle de ce déploiement.

Rappelons.

Le nom de notre déploiement est K eight s web Hello.

Voici le nom du déploiement.

Et maintenant, il a actuellement un seul pod.

Mettons-le à l'échelle K scale deployment.

K eight s Web.

Hello.

Et j'aimerais mettre à l'échelle le déploiement à, disons, quatre répliques.

Allons-y, le déploiement a été mis à l'échelle.

Maintenant, obtenons les pods K get pods.

Maintenant, il y a quatre pods, un est toujours en cours de création.

Vérifions à nouveau.

Et maintenant, les quatre pods sont en cours d'exécution.

Ils appartiennent tous au même déploiement K eight s web Hello.

Et chaque pod a bien sûr sa propre adresse IP unique.

Obtenons les détails sur les pods, Gigabit pods, dash or white.

Et ici, je vois différentes adresses IP de chaque pod.

Et bien sûr, ils diffèrent de l'adresse IP du cluster, qui a été créée pour un service spécifique.

Avec la liste des services get SVC.

Et ici, comme avant, je vois l'adresse IP du cluster, 4k eight s web Hello service.

Et chacun de ces pods est maintenant disponible via cette adresse IP du cluster et Kubernetes décidera à quel pod se connecter pour chaque requête particulière.

Revenons maintenant à cette étape où nous sommes à l'intérieur du nœud Kubernetes et essayons d'établir des connexions à cette adresse IP du cluster et à ce port à nouveau.

Effaçons le terminal ici et voyons URL.

Maintenant, je vois une réponse de ce pod avec un tel nom.

Si je répète la commande, c'est une réponse d'un autre pod.

Répétons la commande une fois de plus, encore une fois, et ainsi de suite.

Je vois que maintenant, la charge est équilibrée sur différents pods.

Parce qu'ici, je vois des réponses de différents pods.

Différents noms apparaissent ici dans les réponses.

Différents pods servent différentes requêtes.

Et voici différents noms des pods.

C'est ainsi que la distribution de la charge fonctionne en action.

Et maintenant, en utilisant cette image Docker construite de manière personnalisée, nous avons pu le prouver.

Très bien, continuons.

Et maintenant, modifions le type de service que nous créons pour notre déploiement car maintenant il y avait cluster IP, qui est disponible uniquement depuis l'intérieur du cluster.

Allons ici et supprimons le service actuel K eight s web Hello.

Prenez simplement son nom, effacez le terminal et antigay delete SVC signifie service et nom de base du service que nous aimerions supprimer, le service a été supprimé get SVC, il n'y avait plus un tel service.

Et si j'ai essayé de me connecter à nouveau au déploiement en utilisant cluster IP que nous avons utilisé avant, j'obtiendrais définitivement une erreur.

Donc je vois No response.

Très bien.

Créons maintenant un service à nouveau.

Mais maintenant, nous définirons son type sur node port.

Utilisons la commande send K, expose deployment, K eight s web Hello.

Et ici, nous ajouterons le type, qui sera défini sur node port.

En notation Pascal Case, node port.

Et ajoutons ici l'option port et le port sera défini sur 3000.

Même port que nous avons utilisé avant, c'est le port où notre application Express no GS est en cours d'exécution.

Allons-y et créons un tel service de type node port, le déploiement a été exposé, listons les services get SVC.

Et maintenant, il y avait à nouveau un service avec le nom gate s web Hello, son type est maintenant node port.

Ici était à nouveau cluster IP, et port.

Mais ici, je vois le port qui a été spécifié ici en utilisant l'option port.

Et aussi après la colonne, je vois le port 32,142 généré aléatoirement.

Et maintenant, je suis en mesure de me connecter au déploiement en utilisant l'adresse IP du nœud, je pourrais obtenir l'adresse IP du nœud en entrant minikube IPL, nous avons un seul nœud, rappelons.

Et ici, c'était un peu dans mon cas.

Et je pourrais prendre cette IP à ce port.

Et je me connecterai à l'un des pods de ce déploiement.

Faisons cela.

Laissez-moi prendre cette IP, allez dans le navigateur web par exemple.

Parce que maintenant, je serai en mesure de me connecter au déploiement depuis mon ordinateur, laissez-moi coller cette IP et après la colonne, j'ajouterai ce port comme cela.

Donc, dans mon cas, la chaîne de connexion est ici.

Donc, voici l'adresse IP, c'est l'adresse IP du nœud et ici était le port généré aléatoirement, qui a été créé par Kubernetes lui-même lorsque nous avons créé le service pour notre déploiement.

Allons-y et essayons de nous connecter.

Et je vois la réponse de l'un des pods.

Actualisons.

Et je vois la réponse d'un autre pod avec RS ou nom, actualisons à nouveau, et je vois la réponse d'un autre pod ici.

C'est ainsi que nous sommes en mesure de nous connecter à notre déploiement en utilisant le service node port.

De plus, c'est une manière plus simple d'obtenir l'URL pour la connexion à ce déploiement en utilisant la commande minikube service minikube service.

Et ici, tapez le nom du service dans notre cas, gay eight s web Hello.

Un nouvel onglet dans le navigateur web sera ouvert automatiquement.

Et notez l'URL ici, même que celle que je viens d'utiliser avant, l'adresse IP du nœud et le port qui a été automatiquement généré par Kubernetes.

C'est le type de service node port.

De plus, ici, vous pouvez voir cette URL réelle lorsque vous entrez un service minikube K eight s web Hello, voici l'URL réelle.

Et si vous voulez obtenir uniquement l'URL, vous pouvez ajouter ici l'option URL et vous verrez uniquement l'URL et vous pourrez la coller où vous voulez.

Donc, c'est un type de service node port.

Et il expose le déploiement au port du nœud.

Et ici était ce port spécifique dans mon exemple, dans votre cas, ce port sera complètement différent.

Et une autre option, que je voudrais vous montrer en termes de création du service, est un équilibreur de charge.

Créons un service d'équilibreur de charge et pour cela, supprimons le service existant gate delete SVC service gate s web Hello.

Le service a été supprimé, gate gift SVC, il n'y avait plus un tel service.

Et créons un service de type load balancer.

Gate expose le déploiement.

Gate s web Hello.

Ici, ajoutons le type load balancer, la notation Pascal Case Foundation encore, et ajoutons l'option par défaut et sa valeur sera 3000.

Même que précédemment.

Créons un tel service, le service a été créé, get SVC.

Maintenant, je vois qu'il y a un service de type load balancer.

Ici était cluster IP mais external IP ici est en attente.

Et vous verrez ici en attente si vous utilisez minikube, mais lorsque vous déployez vos applications quelque part dans le cloud en utilisant l'un des fournisseurs de cloud comme Amazon, Google Cloud, etc.

Ici, vous verrez l'adresse IP de l'équilibreur de charge attribuée automatiquement.

Mais dans notre cas, en utilisant minikube, ce comportement est similaire à node port.

Et ici, nous serons toujours en mesure de nous connecter à notre déploiement en utilisant l'adresse IP du nœud.

Et si j'entre maintenant minikube, service, gate s web Hello, je verrai une connexion qui est faite à l'adresse IP du nœud.

Et ici était un jeu de port aléatoire qui a été généré ici.

Ici était ce port aléatoire.

Très bien, continuons.

Et gardons ce service et ce déploiement en place.

Rappelons que nous avons un seul service ici que nous avons créé avant, c'est k eight s web hello et le type est maintenant load balancer.

Et il y a un seul déploiement gate get deployed.

Et ce nom est K eight s web Hello.

Et maintenant, ce déploiement a quatre pods différents disponibles pour nous.

Nous pourrions lire les détails sur ce déploiement Kay, describe deployment, gait s web Hello.

Et voici les détails de ce déploiement.

D'ailleurs, à la fin ici, je vois les logs liés à la mise à l'échelle du jeu de réplicas, initialement, la quantité de réplicas était de un et plus tard, nous l'avons mise à l'échelle à quatre.

Si vous le souhaitez, vous pourriez essayer de le mettre à l'échelle à un autre nombre si vous le souhaitez.

Au-dessus, je vois que ce déploiement a un nom gay as web Hello.

L'espace de noms est par défaut, les étiquettes, l'annotation, le sélecteur, les réplicas souhaités pour la mise à jour pour la disponibilité pour.

Et maintenant, essayons de mettre à jour la version de l'image dans notre déploiement.

Remarquez ici que le type de stratégie est une mise à jour progressive.

Que signifie-t-il ? Lorsque vous publiez une nouvelle version de votre application, bien sûr, vous voulez déployer cette nouvelle version en production en douceur sans aucune interruption de service.

Et Kubernetes permet cela dès la sortie de la boîte.

Et c'est très facile.

Et ce type de stratégie de mise à jour progressive signifie que de nouveaux pods seront créés avec la nouvelle image tandis que les pods précédents seront toujours en cours d'exécution.

Ainsi, les pods seront remplacés un par un.

Et enfin, après un certain temps, ou les pods seront en cours d'exécution dans votre image mise à jour.

Et maintenant, essayons cela en action.

Nous allons mettre à jour un peu notre application et construire une nouvelle image avec NASA tech, par exemple, version deux dot 0.0.

Et ensuite, nous modifierons l'image dans notre déploiement et verrons ce qui se passera, comment Kubernetes déployera cette mise à jour.

Alors, allons-y et faisons cela.

D'ailleurs, je n'ai plus besoin de cette étape, où j'ai créé une connexion SSH au nœud.

Par conséquent, laissez-moi sortir de cette connexion et fermer cette étape en fait, et je garderai seulement un onglet ouvert.

Alors, revenons à Visual Studio code.

Et ici, les contenus du fichier index dot MJS.

Et nous avons déjà une image disponible pour cette version de l'application où le serveur répond avec une telle chaîne.

Maintenant, modifions ce twink par exemple, ajoutons ici br ethics version deux comme cela.

Et maintenant, construisons une nouvelle image avec une nouvelle étiquette, poussons-la vers Docker Hub et ensuite modifions l'image dans notre déploiement.

Enregistrons les modifications dans ce fichier, ouvrons le terminal intégré.

Et maintenant, construisons l'image et attribuons une autre étiquette.

Maintenant, l'image n'a qu'une seule étiquette, c'est la dernière.

Donc, construisons une nouvelle image Docker build dot dusty tech, Mr.

Chu préfixez votre nom si vous voulez pousser cette version de l'image vers votre compte Docker Hub.

Donc, basez le sucre et ici sera le nom de l'image gay eight s web Hello.

Et après la virgule.

J'ajouterai l'étiquette par exemple deux points 0.0 comme cela.

Construisons cette image, rappelons que j'ai modifié le fichier index dot NGS et j'ai mis à jour cette chaîne, donc elle devrait construire une nouvelle image.

Construisons cette image, en exportant des couches, l'image a été construite et maintenant, poussons-la vers Docker Hub.

Je vais copier ce nom, y compris l'étiquette.

Et maintenant, ici, j'entre docker push.

Et une nouvelle version de mon application sera poussée en utilisant une étiquette séparée pour la même image k eight s web Hello.

Construisons cette image, en exportant des couches, l'image a été construite et maintenant, poussons-la vers Docker Hub.

Je vais copier ce nom, y compris l'étiquette.

Et maintenant, ici, j'entre docker push.

Et une nouvelle version de mon application sera poussée en utilisant une étiquette séparée pour la même image k eight s web Hello.

Allons-y et poussons, en poussant, je vois que certaines couches existent déjà et qu'une seule couche a été poussée vers l'image, qui a été poussée avec succès, laissez-moi vérifier cela, allez à mon compte Docker Hub, actualisez-le, je vois toujours une seule image ici.

Remarquez, laissez-moi cliquer dessus.

Et ici, je devrais trouver deux étiquettes, latest et do dot 0.0.

Maintenant, déployons cette nouvelle version de cette image.

Et pour cela, nous utiliserons la commande suivante.

Allons au terminal ici.

Et définissons une nouvelle image pour le déploiement key set image.

Nous définissons une nouvelle image pour un déploiement particulier, ensuite ce sera le nom du déploiement K eight s web Hello.

Et ensuite, nous devons sélectionner les ports où nous aimerions définir une nouvelle image.

Ici, nous arriverons à gate eight s web Hello.

Et après le signe égal, nous spécifierons une nouvelle image.

Dans mon cas, c'est bits the shoe slash gay ID s web Hello, colonne deux dot 0.0.

C'est la nouvelle étiquette qui nous a été attribuée avant de pousser la nouvelle version de l'image vers Docker Hub.

Après avoir entré cette commande, l'image sera modifiée et le déploiement de la mise à jour sera démarré.

Soyez prêt à entrer la commande suivante après cela, 1k rollout status deployment K eight s web Hello, vous pourriez préparer cette commande quelque part dans l'éditeur de texte et ensuite la coller rapidement.

Après cette commande, j'essaierai de l'entrer manuellement.

Allons-y et changeons l'image, l'image a été mise à jour, key rollout status deployment gay eight s web Hello, en attente que le déploiement soit autorisé à se terminer.

Et maintenant, je vois que le déploiement a été déployé avec succès.

Et avant, je voyais des messages tels que trois sur quatre nouveaux réplicas ont été mis à jour, un ancien réplica est en attente de terminaison, et ainsi de suite.

Enfin, tous les réplicas précédents ont été terminés et de nouveaux réplicas ont été déployés.

Connaissons maintenant les pods, gay get pods.

Et maintenant, je vois qu'il y a quatre pods.

Et notez l'âge de ces pods de 30 à 40 secondes, cela signifie que les pods précédents ont été entièrement terminés et que de nouveaux pods ont été créés.

Et maintenant, dans tous ces quatre pods, nous exécutons une nouvelle version de notre application.

Et nous pouvons vérifier cela très facilement en accédant à notre déploiement en utilisant le service et il y avait encore le service get SVC, le type est un équilibreur de charge.

Et il y avait cluster IP ici était le port.

Et en entrant la commande minikube service, K eight s Webb Hello, je pourrais ouvrir la connexion à l'un des pods en cours d'exécution.

Donc, allons-y et en fait, il a été ouvert et maintenant je vois la réponse, qui inclut la version deux.

C'est ainsi que fonctionnent les mises à jour, vous pouvez actualiser la page ici, puis vous devriez voir une réponse d'un autre serveur.

Par exemple, celui-ci.

Et encore une fois, ici je vois la version deux, cela signifie que notre nouvelle version d'application a été déployée avec succès sur tous les pods du déploiement.

Magnifique.

C'est là que se trouvent les mises à jour progressives et c'est ainsi que vous pouvez vérifier le statut de la mise à jour progressive en entrant la commande K rollout status.

Celle-ci, si vous le souhaitez, vous pourriez créer une autre étiquette pour votre image, la pousser vers Docker Hub et vérifier comment fonctionne le déploiement à nouveau.

Ou si vous le souhaitez, vous pourriez revenir à la version précédente.

D'ailleurs, nous pourrions essayer cela ensemble rapidement.

Allons à cette commande et ici, je vais supprimer le pont et cela signifiera que je souhaite utiliser uniquement cette étiquette et vérifions comment l'image sera modifiée à nouveau.

Et nous revenons en fait à une version précédente de notre application.

Modifions l'image, vérifions ou autorisons le statut à notre nouveau réplica à avoir été mis à jour, en attente que le déploiement soit autorisé à se terminer.

Et enfin, le déploiement a été déployé avec succès.

Et encore une fois, je verrai quatre pods complètement nouveaux, get pods, ici était l'âge de ces quatre pods.

Connectons-nous à nouveau à notre déploiement, minikube service gay it as web Hello.

Et je vois à nouveau hello from the server sans version deux.

C'est ainsi que fonctionnent les mises à jour progressives.

Magnifique.

Maintenant, essayons de plier.

Maintenant, nous avons quatre pods en cours d'exécution.

Mais que se passe-t-il si je supprime simplement l'un des pods manuellement ? Essayons cela.

Prenons par exemple ce nom de pod, notez H de ces quatre pods, et entrons key delete pod et collez le nom de n'importe quel pod que vous aimez.

Et après cette commande, obtenons à nouveau les pods.

Et je verrai qu'un nouveau pod sera créé automatiquement, le conteneur créé.

Parce que nous avons dit à Kubernetes que la quantité souhaitée de pods dans le déploiement est de quatre.

C'est pourquoi il essaie de faire de son mieux pour créer la quantité souhaitée de répliques, son déploiement spécifique.

Et maintenant, je verrai qu'il y a à nouveau quatre pods, en cours d'exécution.

Et l'âge de ce pod est de 33 secondes.

Très bien, nous l'avons essayé, les mises à jour progressives.

Et aussi, nous avons essayé de supprimer l'un des pods.

Et ne me faites pas démontrer comment lancer le tableau de bord Kubernetes.

Si vous utilisez un minikube, c'est très facile, juste une seule commande.

Mais si vous exécutez Kubernetes sur vos propres locaux, ou quelque part dans le cloud, cela pourrait être un peu plus difficile, car vous devez sécuriser l'accès web au tableau de bord.

Mais ici encore, il y a juste une seule commande minikube dashboard.

Comme cela, activons ce pod lounging proxy vérifiant proxy hells.

Et cette page web sera ouverte ici.

Et comme vous l'avez vu ici, aucune invite pour le nom d'utilisateur et le mot de passe.

Ce tableau de bord a été simplement lancé comme cela, car nous utilisons minikube.

Et ici, vous pouvez observer les détails de votre cluster Kubernetes.

Par exemple, vous pouvez aller aux déploiements, et vous trouverez un seul déploiement ici, notez que je diminue un peu la taille comme cela.

Donc voici les métadonnées pour ce déploiement.

Voici les étiquettes.

Stratégie de mise à jour progressive, c'est ce que nous avons observé.

Statut des pods pour disponibles pour mis à jour.

Voici les conditions, nouveau jeu de répliques, voici l'ID du jeu de répliques, qui a été créé par ce déploiement.

Vous pouvez cliquer sur ce lien hypertexte et lire les détails sur un jeu de répliques spécifique.

Remarquez que le jeu de répliques, le déploiement et les pods appartiennent tous au même espace de noms par défaut, mais bien sûr, vous pouvez attribuer des déploiements à différents espaces de noms personnalisés, les étiquettes pour ce jeu de répliques, le statut des pods pour en cours d'exécution pour souhaité et voici les liens vers tous les pods qui appartiennent à ce jeu de répliques particulier.

De plus, ci-dessous, il y avait un service qui a été créé pour ce jeu de répliques pour ce déploiement, le type est un équilibreur de charge ici.

Et si vous cliquez sur un pod spécifique, vous pouvez lire les détails sur un pod particulier, voici le nom du pod, l'espace de noms lorsque le pod a été créé.

Voici les informations sur le nœud où ce pod a été créé, le statut est en cours d'exécution, l'adresse IP du pod.

Ci-dessous, vous pouvez également trouver les détails sur le jeu de répliques qui contrôle en fait ce pod particulier.

Et notez que l'étiquette pour ce pod est ici up Golang K eight s web Hello.

Et la même étiquette est trouvée ici contrôlée par le jeu de répliques et ici était l'étiquette dans le jeu de répliques.

De plus, ci-dessous, vous pourriez trouver les détails sur les événements qui se sont produits dans ce pod particulier.

Par exemple, voici l'étape de téléchargement de l'image Mr.

Xu K eight s web Hello.

Et voici les détails sur les conteneurs qui ne sont pas en cours d'exécution à l'intérieur du pod.

Il n'y avait qu'un seul conteneur à l'intérieur de chaque pod.

D'ailleurs, si je vais aux jeux de répliques, je trouverai en fait deux jeux de répliques différents qui ont été créés pour différentes images pour cette image et pour cette image.

Et maintenant, dans ce jeu de répliques, il y a zéro point car nous sommes revenus de cette image à cette image avec l'étiquette latest, c'est pourquoi maintenant ici je vois quatre pods, et ici, zéro pod.

Très bien, cette interface utilisateur graphique, vous pouvez cliquer sur d'autres éléments de menu et observer, par exemple, quels nœuds appartiennent à la salle de classe.

Maintenant, il y avait un seul nœud minikube.

Et si vous cliquez dessus, vous pouvez lire les détails sur ce nœud particulier.

C'était le tableau de bord Kubernetes.

Et vous pouvez l'utiliser afin d'observer le statut des déploiements et services Kubernetes, et ainsi de suite.

Laissez-moi le fermer.

Et maintenant, continuons et laissons Ctrl C afin d'interrompre ce processus ici.

Et maintenant, minikube ne sera plus disponible.

Maintenant, une notice importante, nous venons d'utiliser l'approche impérative pour la création de déploiements et de services.

Et nous créons des déploiements et des services en utilisant différentes commandes kubectl.

Mais généralement, ce n'est pas la manière dont les déploiements et les services sont créés.

Et dans la plupart des cas, l'approche déclarative est utilisée.

Et dans l'approche déclarative, vous devez créer des fichiers de configuration YAML, qui décrivent tous les détails pour les déploiements et les services.

Et ensuite, appliquer ces fichiers de configuration en utilisant kubectl.

Commande Apply.

Et c'est en fait l'approche déclarative de création de différentes ressources et objets dans Kubernetes.

Et c'est ce que nous allons faire maintenant.

Maintenant, supprimons les déploiements et services que nous avons créés auparavant.

Et pour cela, vous pourriez faire la commande alias, kubectl, delete the deployment, et ensuite, delete service.

Mais il y avait aussi une version courte de la suppression de toutes les ressources dans l'espace de noms par défaut, et c'est gate delete all avec l'option, il y a l'option all comme cela, toutes les ressources seront supprimées, vous verrez que les pods ont été supprimés, le service a été supprimé, et le déploiement a été supprimé également.

Obtenons les pods.

Les pods sont encore en cours de terminaison.

Vérifions à nouveau.

Toujours en cours de terminaison, attendons un peu.

Et maintenant, il n'y a pas de ressources trouvées dans l'espace de noms par défaut.

Tous les pods ont été terminés, obtenons les services get SVC.

Et maintenant, il y avait seulement un seul service système par défaut Kubernetes.

Et bien sûr, il n'y a pas de déploiements get deployed, aucune ressource trouvée.

Maintenant, créons un fichier de configuration YAML pour le déploiement.

Et pour les héros de services, nous créerons deux fichiers de configuration séparés.

Allons à Visual Studio code.

Et ici, laissez-moi d'ailleurs, masquer et par le terminal pour le moment.

Et laissez-moi fermer ces anciennes fenêtres.

Et maintenant ici, dans la racine du dossier K eight s ici, créons les fichiers suivants deployment pod YAML.

Et créons également le fichier service dot YAML.

Comme cela.

Donc deux fichiers deployment YAML et service dot YAML.

Ouvrons le fichier deployment dot YAML.

Si vous avez installé l'extension Kubernetes ici dans VS code, que je vous ai demandé de faire avant, vous pourriez créer de tels fichiers de configuration très rapidement.

Laissez-moi vous montrer.

Donc, tapez ici simplement deployment et vous verrez la suggestion Kubernetes deployment, nous avons sélectionné et vous verrez que le fichier de configuration YAML sera créé automatiquement pour vous.

Et vous verrez que toutes les apparences de my app seront mises en surbrillance et vous pourriez simplement taper le nom du déploiement que vous aimeriez définir et laisser définir le nom à K eight s comme nous l'avons fait avant.

Mais maintenant, nous utilisons le fichier de configuration YAML.

Donc, K eight s web Hello.

Comme cela.

Le nom du déploiement a été défini ici, il y avait le nom réel pour ce déploiement.

Il y avait une version d'API ops slash v1.

Ici, il y avait un sélecteur avec un schéma d'étiquette de correspondance.

Et par ce schéma d'étiquette de correspondance, nous spécifions quels pods seront gérés par ce déploiement.

Et ci-dessous, il y avait un modèle imbriqué et ce modèle décrit en fait le pod mais ici, vous n'avez pas besoin de spécifier le type de modèle comme cela, car ce modèle imbriqué pour le modèle de déploiement est toujours pod.

Par conséquent, le courant ici n'est pas nécessaire.

Ensuite, pour les pods qui appartiennent à ce déploiement, ici, nous définissons les étiquettes.

Et l'étiquette ici est la même que l'étiquette ici dans le sélecteur match labels.

Donc cette étiquette et cette étiquette correspondent ici.

Et ensuite, dans spec give, nous spécifions quels conteneurs nous voulons créer dans ce pod.

Et il y avait un seul conteneur avec un tel nom, l'image doit être remplie, nous remplacerons ce placeholder d'image maintenant par une vraie image.

Et aussi ci-dessous, vous pouvez spécifier quels ports vous aimeriez ouvrir dans un conteneur spécifique.

Et ci-dessous, dans la section port, vous pouvez spécifier une liste des ports de conteneur, qui seront ouverts sur l'adresse IP des pods.

Donc, remplissons maintenant les détails dans cette section spec.

L'image sera basée Ashok slash K eight s web Hello.

Et le port ici sera container Port 3000.

Comme cela.

Remarquez également que l'extension VS code Kubernetes a ajouté une section ressources ici.

Et dans cette section, il y avait une limite skip, qui spécifie les limites de mémoire et de CPU pour chaque pod, qui sera créé par ce déploiement.

Et ici, la limite de quantité de mémoire et de quantité de ressources CPU.

500 m signifie la moitié du cœur CPU.

Si vous voulez modifier 500 à 250, par exemple, 1/4 du cœur CPU, gardons-le comme cela.

Et c'est tout pour cette spécification du déploiement.

Enregistrons les modifications dans ce fichier.

Et maintenant, laissez-moi en fait montrer comment trouver la documentation sur la façon de créer des fichiers de configuration YAML spécifiques.

Allons dans le navigateur web et ici, allons sur kubernetes.io.

Et allez ici dans la documentation.

Et ici ou allez dans la référence.

Et ici, sélectionnez Kubernetes API.

Et dans Kubernetes API, vous pouvez sélectionner par exemple, les ressources de charge de travail.

Et vous trouverez les détails sur la façon de décrire par exemple les pods, ou de créer un modèle de pod ou de créer un jeu de répliques, nous venons de créer un déploiement.

Par conséquent, cliquons sur la section déploiement ici.

Et vous trouverez les détails sur la façon de créer des fichiers de configuration YAML.

Si vous voulez créer un déploiement, une version d'API doit être définie sur apps slash v1.

Et ci-dessous, vous trouverez d'autres clés qui doivent être présentes dans le fichier de configuration du déploiement.

Par exemple, le client doit être défini sur deployment.

Ensuite, il y avait la section metadata spec status, d'ailleurs, le status est rempli par Kubernetes automatiquement, et il sera ajouté après que vous ayez créé le déploiement basé sur un fichier de configuration spécifique.

Et si je reviens au fichier de configuration ici, je trouverai des clés telles que API version kind metadata et spec, les mêmes clés qui sont décrites ici API version kind metadata et spec.

Et si vous voulez obtenir des détails sur la spécification du déploiement, vous pouvez cliquer ici et vous trouverez que à l'intérieur de la spécification, vous devez spécifier un sélecteur, un modèle, des répliques, une stratégie, un radio secondes et ainsi de suite.

Et si je regarde ce fichier ici, je découvrirai que à l'intérieur de la spécification dans cet exemple, il y a un sélecteur et un modèle, un sélecteur et un modèle ici, et les deux sont requis.

Si vous cliquez sur le modèle, vous lirez les détails sur le modèle de spécification de pod.

Cliquons dessus.

Et ici, vous trouverez que à l'intérieur de la spécification de modèle de pod, vous devez spécifier les métadonnées et la spécification que nous venons de créer.

Et c'est ce que nous avons ajouté ici dans la section modèle, les métadonnées et la spécification pour le pod.

Cliquons sur la spécification de pod et lisons les détails sur la spécification de pod.

Les conteneurs sont requis et vous pouvez ajouter plusieurs conteneurs dans la spécification de pod si vous voulez le faire.

Et ici, dans cette spécification, nous avons des conteneurs ici, c'est le cas, cliquons sur le conteneur ici.

Et dans cette spécification de conteneur, vous trouverez le nom qui est requis.

C'est pourquoi nous avons défini le nom comme ce tout, vous devez également définir l'image pour un conteneur spécifique.

Ici avec l'image, les ressources et les ports sont également décrits ici sur cette page de recommandation.

Donc, voici la section de support.

De plus, vous pouvez définir, par exemple, des variables d'environnement pour un conteneur particulier.

Je vous recommande vivement de vous familiariser avec la documentation et avec toutes les options disponibles, et je viens de vous montrer comment vous pouvez creuser dans la documentation et découvrir comment remplir les différentes sections du fichier de configuration.

Très bien, nous avons terminé la création du fichier de configuration pour le déploiement.

Donc, le courant ici est le déploiement.

Et maintenant, appliquons ce fichier de configuration en utilisant l'approche déclarative, en créant un tel fichier en place, vous n'aurez plus besoin d'entrer la commande kubectl create deployment, vous entrerez simplement la commande kubectl apply.

Faisons cela.

Ouvrons le terminal intégré ici.

Et maintenant, je suis toujours à l'intérieur du dossier gate eight s web Hello.

Laissez-moi sortir de ce dossier où se trouve ce fichier de déploiement YAML.

Listons les fichiers ici.

Donc, voici le fichier de configuration YAML de déploiement.

Et ici, entrons la commande kubectl.

Apply this F signifie Fichier, et ici sera le nom du fichier deployment.

Dot YAML.

Simple comme cela, le fichier a été appliqué et le déploiement a été créé, a été généré.

D'ailleurs, ici, je n'ai pas d'alias avec adéquatement alias, alias K, kubectl.

Donc, K get deployments.

Et maintenant, il y avait K eight s web Hello deployment.

Et il y avait un seul pod dans ce déploiement get pods.

Le voici, qui est en cours d'exécution.

Exact.

Mais comment pouvons-nous maintenant mettre à l'échelle ce déploiement et augmenter la quantité de répliques ? Nous avons facilement modifié la spécification de ce fichier.

Mais comment pouvons-nous augmenter la quantité de répliques.

Ici, pour le moment, nous ne voyons aucun nombre.

Essayons de découvrir cela en utilisant la documentation.

Je suppose que je ne sais pas comment changer cela.

Donc, allons dans les ressources de charge de travail, vérifions le déploiement et faisons défiler vers le bas ici.

Donc, spec status metadata kind, pas d'options ici.

Cliquons sur deployment spec.

Ici, nous avons le sélecteur ou le modèle, les répliques, le nombre de pods souhaités.

Et c'est l'option que vous devez utiliser si vous voulez modifier la quantité de répliques du nombre par défaut un, oh ici était le nombre par défaut un à un autre nombre.

Et vous devez ajouter le nombre de répliques dans la spécification du déploiement.

Donc, allons dans la spécification du déploiement.

Donc, ici, nous avons la spécification.

Et ici, ajoutons un nouveau deal, les répliques.

Et sa valeur sera, disons, le nombre cinq.

Si je reviens en arrière, je peux lire que sa valeur est un entier 32.

Donc, vous n'avez pas besoin d'écrire ici file comme cela.

Exact.

Comme un nombre, nous avons sauvegardé les modifications.

Et appliquons à nouveau ce fichier de configuration de déploiement YAML, en utilisant la même commande kubectl, apply this F deployment YAML.

Allons-y, configuré, get pods.

Et maintenant, je vois que quatre nouveaux conteneurs sont en cours de création.

Et maintenant, mon déploiement a cinq pods différents, quatre d'entre eux sont déjà prêts, cinq autour.

C'est ainsi que nous avons pu modifier très facilement notre déploiement simplement en modifiant le fichier de configuration YAML du déploiement.

Mais bien sûr, maintenant, il n'y a pas de services K get SVC, créons un nouveau service en utilisant une approche similaire.

Masquons le terminal.

Et maintenant, allons au fichier de configuration YAML du service.

Et ici, je vais accélérer le processus de création du fichier de configuration du service et taper service et l'extension Kubernetes nous proposera cette option.

Et cette spécification sera créée automatiquement.

Le type est service, la version de l'API est b one, ici elle diffère de la version de l'API pour le déploiement, le type, les métadonnées, le nom définit le nom de ce service.

Entrons le nom gate s web hello et aussi, modifions le sélecteur et sélectionnons all sera up Golden Gate eight s web Hello également.

D'ailleurs, si vous survolez la souris sur l'une des clés de ce fichier de configuration, vous pouvez trouver des hyperliens vers la documentation pour chaque clé particulière, par exemple, l'URL du nom est ici.

Ou si vous survolez la souris sur le type, vous pouvez également trouver des hyperliens ici pour une version pour le type de métadonnées, par exemple.

Très bien, ce qui reste ici dans cette série est la modification de la section port.

Ici, je vois que le port et le port cible ont été remplis automatiquement.

Avant, nous avons utilisé le port que nous avons exposé, en fait le même port 3000, où notre serveur web Express est en cours d'exécution.

Et maintenant, nous pouvons essayer un port différent, exposer le port 3000, qui est le port cible au port, disons 3030, comme cela.

Et cela signifie que le port cible 3000 sera exposé au port externe 3030.

Remarquez également que dans cette spécification, il n'y avait pas de type pour ce service.

Et disons que nous voulons créer un service load balancer.

Pour cela, allons dans la documentation.

Trouvons la documentation pour le service ici.

Kubernetes, API, ressources de service, service.

Et ici, ou allons dans la spécification du service.

Ici, nous sélectionnerons les ports.

Et aussi ci-dessous, vous pouvez trouver le type de service, soit cluster IP, qui est par défaut, ou external name, ou node port ou load balancer.

Définissons le type sur load balancer.

Revenons à notre fichier de configuration.

Et ici, dans spec, définissons le type sur load balancer comme cela.

C'est tout pour cette spécification de service.

Enregistrons les modifications dans ce fichier.

Et appliquons cela en utilisant la même commande que précédemment kubectl.

Apply dash F signifie Fichier, et ici, tapez service dot YAML.

Je suis toujours à l'intérieur du dossier gate eight s.

Donc, appliquons le fichier YAML de service, appliqué GAE get SVC.

Et maintenant, je vois qu'un nouveau service avec le type load balancer a été créé.

Et maintenant, de manière similaire à avant, je pourrais ouvrir la connexion à notre déploiement en utilisant la commande minikube service K eight s Web.

Hello, allons-y et la page sera ouverte.

Actualisez et obtenez une bonne réponse d'un autre pod.

Cela signifie que maintenant tout fonctionne comme avant, il n'y avait pas de service et de déploiement.

Et nous avons créé tout en utilisant l'approche déclarative en utilisant des fichiers de configuration.

Il y avait un fichier pour le service et voici le fichier pour le déploiement.

Nous pourrions également très facilement supprimer le déploiement et le service que nous venons de créer en utilisant une seule commande.

Faisons cela, allez dans le terminal et ici entrez key delete this f ici sera le nom du premier fichier deployment YAML.

Et ici, ajoutons l'option dash f une fois de plus et tapez service that YAML.

Allons-y et supprimons à la fois le déploiement et le service.

Nous vérifierons, d'accord, get SVC aucun service, get deployment et aucun déploiement.

Super.

Maintenant, faisons ce qui suit.

Essayons de créer deux déploiements.

Et connectons-les ensemble.

Car c'est une tâche très courante lorsque vous voulez connecter différentes obligations ensemble, par exemple, connecter le front-end au back-end ou connecter le back-end au service de base de données, etc.

Par conséquent, maintenant, nous allons faire ce qui suit, laissez-moi dessiner une image.

De manière similaire à avant, nous allons créer un déploiement web et déployer notre application web no GS Express.

Et ici, laissez-moi taper web comme cela.

Et nous allons également créer un autre déploiement et nous l'appellerons Ingenix.

Ce déploiement Ingenix exécutera l'image nginx de base sans ajustements et ce déploiement nginx aura un service cluster IP correspondant.

Donc, laissez-moi dessiner ici une ligne et ici sera le service cluster IP, commençons par C majuscule cluster IP comme cela.

Et ces deux déploiements sont bien sûr alloués dans le cluster Kubernetes.

Et ce déploiement sera également exposé mais chaque service aura le type Load Balancer, cela signifie que nous pourrons nous connecter à l'un ou l'autre depuis l'extérieur en utilisant l'adresse IP de l'équilibreur de charge ici avec un équilibreur de charge.

Maintenant, à l'intérieur de l'application web, nous créerons deux points de terminaison, le premier sera le point de route, comme avant, qui retournera simplement hello from the web server.

Et un autre point de terminaison ici sera, disons, Ingenix.

Et lorsque la connexion sera établie à nginx, nous nous connecterons au service nginx en utilisant cluster IP.

Ou vous verrez que l'utilisation du nom de service nginx est comme cela.

Donc, à partir d'un déploiement, nous nous connecterons à un autre déploiement et obtiendrons une réponse de l'un des pods qui seront exécutés dans l'application nginx.

Et ensuite, nous retournerons le résultat au client avec le contenu que nous avons reçu de l'exportateur nginx.

Donc, c'est le plan.

Et de cette manière, nous connecterons en fait différents déploiements, le déploiement web et le déploiement nginx.

Commençons avec cela.

Vous êtes à l'intérieur du dossier K eight s.

Laissez-moi fermer ces fichiers pour le moment.

Créons une copie de ce dossier K eight s web Hello, qui contient tous les fichiers liés à notre application web Express.

Copions ce dossier et collons-le ici.

Et renommons-le simplement en cliquant sur ce nom, en appuyant sur Entrée et en entrant un nouveau nom K eight s web to Ingenix comme cela.

Ensuite, gardons le fichier Docker inchangé, Kira Coulter's a ce fichier Docker dans ce dossier, donc pas de modifications ici, mais nous modifierons légèrement le fichier index dot MGS.

Et je vais prendre un fichier modifié d'ici.

Laissez-moi le copier et le coller ici.

Donc, voici le contenu du fichier index dot MGS pour cette deuxième application.

Il y a toujours l'URL de route ici, la barre oblique, nous créons le serveur web Express.

Mais nous ajoutons ici un autre point de terminaison Ingenix.

Et son gestionnaire de route est maintenant une fonction async car maintenant nous allons nous connecter à un autre serveur en simulant la connexion entre différents déploiements.

Et notez l'URL ici, c'est simplement http colon slash slash Nginx.

Et nous allons créer un service appelé Ingenix.

Pour le deuxième déploiement nginx.

Et à partir de ce déploiement, nous serons en mesure de nous connecter à un autre déploiement en utilisant simplement le nom du service correspondant.

Simple comme cela.

Bien sûr, il est possible de se connecter en utilisant soit cluster IP ou non, cluster IP est dynamique, le nom du service est statique.

Donc, nous allons nous connecter à l'un des serveurs nginx en utilisant le nom de service nginx.

Et ici, nous utilisons fetch, que nous importons du package node fetch, d'ailleurs, dans le moment, nous allons l'installer également dans cette application.

Donc, nous attendons la réponse du serveur nginx.

Et ensuite, nous prenons le corps de la réponse en appelant la méthode text et retournons simplement au client ce corps, essentiellement ce que ce point de terminaison fera, il proxyera simplement la requête au serveur nginx et retournera le résultat de la réponse de l'Ingenix au client.

Simple comme cela.

Et ici, nous importons fetch de node fetch, donc nous devons installer une telle dépendance externe.

Et pour cela, ouvrons un autre terminal et ici, assurez-vous que vous voyez deep dans ce dossier, gate s web to Nginx.

Web to Nginx.

Et ici, entrons npm install Node fetch, installation du package, vous verrez que ce fichier package.json sera modifié.

Donc maintenant, voici deux dépendances Express et node fetch, la dépendance a été installée.

Et notez à nouveau que le dossier node modules est apparu ici mais nous n'en avons pas besoin ici.

Supprimons-le simplement car à l'intérieur de l'image que nous allons construire maintenant, nous avons l'instruction d'exécuter npm install.

La voici.

C'est pourquoi toutes les dépendances nécessaires seront installées à l'intérieur de l'image Docker.

Très bien, maintenant nous sommes prêts à partir.

D'ailleurs, cette application est également incluse dans les fichiers de projet finaux que vous pouvez cloner depuis mon dépôt GitHub.

Donc, K eight s web to Nginx.

Et ici était le fichier index dot MJS.

Et maintenant, construisons à nouveau l'image Docker, mais ce sera une image Docker différente de cette application.

Et maintenant, construisons-la en utilisant la même commande que précédemment Docker build.

Donc, listons les fichiers et dossiers ici, il y avait un fichier Docker.

Le fichier Docker n'a pas été modifié, il est le même que pour l'application précédente.

Et maintenant, construisons l'image Docker Docker build dot.

Et ajoutons une étiquette, Mr.

Ashok, slash, et nommons-la gay eight s web two Ingenix.

Même nom que pour ce dossier.

Et gardons l'étiquette comme latest.

Vous n'avez pas besoin d'ajouter ici une étiquette comme cela.

Dans ce cas, elle sera ajoutée automatiquement.

Donc, construisons une telle image, l'image est en cours de construction, notez la commande npm install, l'image a été construite.

Et maintenant, poussons-la vers Docker Hub.

Laissez-moi prendre ce nom.

docker push.

Et ici sera le nom de l'image que je veux pousser vers Docker Hub, en poussant certaines des couches seront réutilisées de notre image.

Et enfin, l'image a été poussée et maintenant nous sommes en mesure de l'utiliser dans le déploiement Kubernetes.

Super, cachons le terminal et ne lisons pas ce qui suit.

Maintenant, je voudrais vous montrer comment vous pouvez combiner les fichiers de configuration YAML de déploiement et de service en un seul fichier.

Fermons ces fichiers.

Et créons un nouveau fichier et nommons-le K eight s web to nginx dot YAML.

Comme cela.

Maintenant, dans ce fichier de configuration, nous combinerons les instructions pour la création du déploiement et du service.

Allons d'abord au service dot YAML.

Prenons le contenu de ce fichier et collons-le ici dans le gate s web to nginx YAML.

Ensuite, veuillez ajouter trois tirets exactement trois et allez à la ligne suivante.

Maintenant, allons au fichier YAML pour le déploiement, prenons tout son contenu et collons-le ici sous ces trois tirets.

Et maintenant, dans un seul fichier, nous avons la spécification, à la fois pour le service et le déploiement.

Maintenant, modifions le déploiement car nous aimerions utiliser notre autre image et ici nous utiliserons notre autre nom.

D'ailleurs, nous pouvons sélectionner ce nom ici, puis cliquer avec le bouton droit et sélectionner Modifier toutes les occurrences.

Et nommons le service et le déploiement comme gay eight s web to Ingenix.

Comme cela.

Gardons le type pour ce service comme un équilibreur de charge, le port ici pourrait être modifié en un autre, par exemple, définissons-le sur all three comme cela.

Et ici, dans la spécification du déploiement, diminuons la quantité de répliques à, disons, trois.

Et modifions également la spécification pour les conteneurs.

Et l'image que nous aimerions utiliser maintenant sera K eight s web to engine X, elle a été remplacée lorsque j'ai modifié le nom K eight s web Hello.

Donc, il y avait une image correcte que nous venons de pousser vers Docker Hub et cette image que nous aimerions utiliser pour ce déploiement particulier.

Et le port du conteneur restera inchangé, ce 3000, très bien, c'est tout pour la spécification du déploiement et du service pour la nouvelle application.

Et maintenant, créons la spécification pour le déploiement NJ MCs et le service car nous allons déployer maintenant deux applications différentes.

L'une qui sera basée sur notre image personnalisée et la seconde qui est basée sur l'image Docker officielle appelée Nginx.

Copions simplement ce fichier et collons-le ici.

Et nommons ce fichier nginx dot YAML.

Et maintenant, dans ce fichier nginx dot YAML.

Modifions les noms.

Une fois de plus, sélectionnez ceci et changez toutes les occurrences.

Et nommons-le simplement Ingenix.

Veuillez taper exactement comme je viens de le faire.

Exactement Ingenix car ce nom pour le service que nous utiliserons à l'intérieur de notre déploiement, à l'intérieur de nos conteneurs qui exécutent le serveur web Express no GS.

Nous nous connecterons à ce déploiement en utilisant le nom de service Ingenix.

C'est pourquoi ce nom est très important ici.

Maintenant, nous avons décidé d'utiliser le type de service cluster IP pour ce deuxième déploiement.

C'est pourquoi, supprimons le type load balancer d'ici.

Par défaut, cluster IP sera attribué ici.

Et modifions la section ports ici, supprimons le port cible et gardons uniquement le port et définissons-le sur huit.

C'est le port par défaut où Ingenix exécutera le serveur web.

De plus, dans la section déploiement, nous devons modifier l'image.

Et maintenant, ce sera simplement Ingenix sans votre nom d'utilisateur, car nous aimerions utiliser l'image Docker officielle appelée Nginx.

Gardons les limites de ressources ici en place, et modifions ici le port du conteneur pour ajouter comme cela.

Donc, la quantité de répliques sera par exemple cinq au lieu de trois.

Enregistrons les modifications ici et résumons ce que nous avons fait ici, nous allons créer un nouveau service appelé Nginx.

Et le nom ici est important pour notre configuration.

Ici se trouve la section port avec une seule clé port.

Et cela signifie que le port externe A sera mappé au port interne 80.

C'est le port où le serveur web nginx est exécuté par défaut.

Et le type de service ici est cluster IP, cela signifie qu'un tel service ne sera pas disponible en dehors du cluster Kubernetes.

Et ici, dans ce déploiement, nous utilisons l'image Docker officielle appelée Nginx.

Ici, la spécification des conteneurs et le port du conteneur est défini sur huit.

C'est tout.

Donc, nous avons créé les deux fichiers de configuration YAML, nginx dot YAML et K eight s web to Ingenix, qui utilise l'image construite de manière personnalisée.

Voici le nom de cette image.

Et maintenant, appliquons les deux fichiers de configuration, celui-ci et celui-ci.

Allons dans le terminal et vérifions que maintenant nous n'avons aucun déploiement get deploy.

Aucun déploiement pour le moment, et aucun service.

Et maintenant, déployons tout en utilisant une seule commande.

Maintenant, je suis toujours à l'intérieur du dossier K eight s web to engine X.

Montons d'un niveau où se trouvent nos fichiers de configuration YAML.

Les voici, celui-ci et celui-ci.

Et appliquons-les.

Okay, appliquons cette commande f ici sera le premier fichier.

Voici son nom.

Et nous pouvons également appliquer un autre fichier, ce F Ingenix YAML.

Comme cela.

Allons-y et créons les deux déploiements et les deux services.

Service créé, déploiement créé, service créé et déploiement créé.

Vérifions les déploiements gay get deployed.

Il y a maintenant deux déploiements, celui-ci et celui-ci.

Partiellement, ils sont déjà get SVC.

Lisons les informations sur les services.

Il y a deux services qui ont été créés, celui-ci qui a le type load balancer, et nginx, qui a le type cluster IP, rappelons que nous allons nous connecter depuis cette application web depuis le déploiement web au déploiement nginx en utilisant ce nom pour le service.

Ou nous pourrions également utiliser cluster IP afin de nous connecter d'un déploiement à un autre.

Mais cluster IP est dynamique.

Ce nom de service est statique.

Donc, vérifions également les pods, game get pods.

Certains des pods sont en cours d'exécution et un est toujours en attente.

Et maintenant, nous sommes en mesure de tester notre configuration et d'essayer de nous connecter depuis l'application web depuis le déploiement web au déploiement nginx.

Ouvrons la connexion à notre déploiement de service web car nous avons utilisé ici un type load balancer pour ce service.

Et nous pourrions utiliser ce port ici et l'adresse IP du nœud Kubernetes.

Rappelons que pour obtenir rapidement une URL pour un déploiement spécifique en utilisant minikube, vous pourriez entrer la commande minikube service et ici sera le nom du service K eight s web two Ingenix.

La page du navigateur web a été ouverte et nous avons obtenu une réponse de l'un des pods qui appartient à K eight s web to nginx deployment.

Et voici le nom du jeu de répliques correspondant.

Très bien, nous venons de déclencher la connexion à l'URL racine.

Revenons rapidement à notre application.

Laissez-moi masquer ce terminal ici.

Et allons à cette nouvelle application et ouvrons le fichier index dot m.

JS.

Et rappelons que ici nous avons deux points de terminaison, le point de terminaison racine, et le point de terminaison slash nginx, qui enverra essentiellement une requête à l'URL nginx, celle-ci et retournera au client la réponse proxy d'un autre serveur.

Ce serveur est externe par rapport à ce serveur où nous exécutons cette application web.

Nous venons de recevoir ce flux du serveur, essayons de nous connecter au point de terminaison Ingenix.

Revenons à notre navigateur et ajoutons ici slash Nginx.

Appuyez sur Entrée.

Et ce que j'ai obtenu, j'ai obtenu Welcome to Nginx.

Cela signifie que la réponse du serveur nginx a été proxyée avec succès à l'intérieur du serveur qui appartient à notre déploiement web.

Et nous avons été en mesure de cette manière de nous connecter d'un déploiement à un autre déploiement par le nom de l'autre service.

Donc, nginx, ici est le nom de l'autre service comme nous l'avons spécifié ici.

Et un tel service n'a pas de cluster IP, get SVC.

Donc, voici le cluster IP pour le service nginx.

Et nous avons été en mesure de nous connecter à un autre déploiement par le nom du service.

C'est ainsi que vous pouvez très facilement connecter différents déploiements ensemble.

Et une telle résolution du nom de service en adresse IP est effectuée par le service interne de Kubernetes, qui est appelé DNS.

Et nous pouvons en fait vérifier cela rapidement.

Allons dans le terminal par exemple ici.

Et rappelons que la semaine obtiendra encore ici la liste des pods K get pods.

Et maintenant, nous pouvons prendre l'un des pods et exécuter n'importe quelle commande à l'intérieur du conteneur en cours d'exécution à l'intérieur du pod.

En utilisant kubectl.

Commande Exec, cette commande est très similaire à la commande Docker exec.

Prenons maintenant le nom de n'importe quel pod qui appartient au déploiement k s web to nginx.

Laissez-moi copier ce nom, dans votre cas, les noms seront complètement différents.

Et laissez-moi effacer notre terminal ici et entrer K exec ici sera le nom du pod.

Ensuite, ce sera deux tirets.

Et ensuite, tapons NS lookup in Janux.

Comme cela, appuyons sur Entrée.

Et j'ai obtenu des correspondances étrangères.

Que signifie-t-il ? En utilisant cette commande, nous avons essayé de résoudre le nom NJ leaks depuis l'intérieur du conteneur qui appartient au pod et une telle résolution a été réussie.

Et cette adresse IP que j'ai obtenue du serveur DNS lorsque j'ai fait la demande et as lookup Ingenix.

Mais d'où vient cette IP ? Avec le droit gay get SVC.

Et ici, j'obtiens une telle vue.

Et notez que cette IP est la même que celle-ci.

Et c'est ce que je vous ai dit.

Maintenant, Kubernetes est en mesure de résoudre le nom du service en cluster IP correspondant.

Et c'est ce que nous voyons ici.

Et nous avons effectué la résolution à l'intérieur du pod qui appartient à notre déploiement et à notre autre service.

Et bien sûr, je pourrais exécuter une commande similaire dans l'un des pods, par exemple, je pourrais taper ici, we get there skew all this et ici taper http Ingenix.

Et cela se connectera en fait au serveur Nginx.

Sarah, puis récupéré de celui-ci la page web racine.

Essayons cela.

Et j'ai réussi à recevoir une réponse de l'un des pods Ingenix.

Et voici la page web nginx.

Très bien, c'est ainsi que différents déploiements peuvent être très facilement connectés les uns aux autres.

Revenons à Visual Studio code et supprimons tout ce que nous avons jusqu'à présent.

Si vous voulez approfondir et explorer les détails de ces déploiements, vous pouvez bien sûr le faire maintenant, vous pouvez l'autoriser par exemple, minikube dashboard, vous pouvez approfondir, aller à différents pods et explorer ce qui se passe à l'intérieur d'eux, et ainsi de suite.

Vous avez toutes les connaissances nécessaires pour cela.

Très bien, maintenant supprimons les deux déploiements et les deux services.

Supprimons ce F Ingenix dot YAML et dash f gay it s web to nginx dot YAML.

Allons-y, les deux services et déploiements ont été supprimés, gay get deployed.

Aucune ressource trouvée gay get as we see juste un seul service.

Je pense que vous serez d'accord avec moi pour dire que le déploiement en utilisant les fichiers de configuration YAML est beaucoup plus agréable et plus rapide que le déploiement en utilisant des commandes kubectl séparées.

Nous avons terminé la partie principale pratique de ce cours.

Et une étape reste.

Et je voudrais vous montrer comment changer le runtime de conteneur qui est actuellement Docker dans notre cluster Kubernetes en un autre runtime de conteneur, par exemple, CRI-o ou container D et afin de modifier le runtime de conteneur, nous devons supprimer la configuration actuelle de minikube et en créer une nouvelle.

Mais allons dans le terminal ici.

Et entrons la commande minikube status.

Maintenant, il est en cours d'exécution, cubelet est en cours d'exécution, le service de barrière est en cours d'exécution.

Maintenant, arrêtons minikube, minikube stop, arrêt du nœud minikube, un nœud a été arrêté et maintenant supprimons la configuration actuelle, minikube delete the little minikube in virtual box dans mon cas, j'ai supprimé toutes les traces du cluster minikube.

Maintenant, recréons le cluster.

Minikube start, j'utiliserai à nouveau l'option driver et sa valeur sera virtual box dans mon cas.

Si vous êtes un utilisateur Windows, vous devez taper ici Hyper V comme pour le précédent minikube start.

Mais veuillez noter que l'option Docker n'a pas fonctionné pour moi au moins, je n'ai pas pu exécuter les conteneurs CRI-o à l'intérieur du conteneur Docker.

Donc, pour une raison quelconque, cela n'a pas fonctionné.

Par conséquent, j'utilise VirtualBox et je ne vous recommande pas d'utiliser maintenant.

Driver Docker.

Donc, le driver est VirtualBox dans mon cas.

Et ensuite, j'ajouterai l'option.

Il y a ce conteneur, ce runtime et cette valeur sera CRI, ce oh une autre option est container D.

Vous pouvez essayer les deux si vous le souhaitez.

Donc, j'entrerai ici CRI-o comme cela.

Et créons un cluster minikube à partir de zéro une fois de plus.

Mais maintenant, le runtime de conteneur est défini sur CRI-o, allons-y, démarrez le nœud de contrôle du plan minikube dans la salle de classe minikube, encore une fois, créons des poupées réelles.

Cela prendra un certain temps, maintenant je vois l'étape de préparation de Kubernetes sur CRI oh et enfin, c'est fait.

Vérifions maintenant le statut minikube status.

Type Ctrl Blaine host est en cours d'exécution, tout est en cours d'exécution comme avant.

Mais maintenant, le runtime de conteneur à l'intérieur du nœud est CRI-O.

Vérifions cela.

Faisons un SSH vers l'adresse IP de minikube et entrons ici throws minikube IBM SSH Docker at 192 168 59.

One auto Yes, DC user.

Maintenant, je suis à l'intérieur du nœud minikube.

Et maintenant, entrons docker ps.

Et ce que je vois, je vois ne peux pas me connecter à Docker.

Et c'est une indication que Docker n'est pas en cours d'exécution à l'intérieur de ce nœud, car nous utilisons le runtime de conteneur CRI-o à la place.

Mais comment vérifier s'il y a des conteneurs CRI-o.

Facilement en utilisant la commande suivante sudo CRI CTL PS et voici un ensemble de conteneurs différents qui sont en cours d'exécution comme do proxy core DNS storage provisioner et ainsi de suite.

Maintenant, essayons à nouveau de déployer les deux applications, l'application web et l'application nginx, et de créer les deux services et voyons comment cela se passe.

Revenons aux résultats.

Au code.

Et ici, effectuons la même tâche qu'avant.

Appliquons simplement la configuration gate, appliquée this F et appliquons les deux fichiers de configuration YAML.

Très bien, allons-y, créons des déploiements et créons des services gate get deploy.

Pas encore prêt, mais il y a deux déploiements.

Encore une fois, pas encore prêt, vérifions les informations sur les services.

Il y a deux services comme avant, gate, get pods.

Certains des pods sont en cours de création de conteneur, un en cours de vérification de l'amour.

Certains sont déjà en cours d'exécution.

Gay get deploy for AWS to deployment is radio Ingenix is not yet ready.

Vérifions à nouveau.

Maintenant, nginx est partiellement prêt.

Et maintenant, tous ces conteneurs ont été créés par le runtime de conteneur CRI-o.

Entrons dans le service minikube et le nom du service afin de tester si tout fonctionne comme avant.

Donc, voici la réponse de l'un des pods.

Et ajoutons ici slash Ingenix.

Et comme avant, cela fonctionne.

Maintenant, nous avons pu obtenir une réponse du déploiement nginx.

Magnifique.

Nous venons de modifier le runtime de conteneur.

Et maintenant, il est défini sur CRI oh, revenons à cette connexion SSH où nous nous sommes connectés au nœud.

Et ici, entrons à nouveau.

Sudo CRI CTL PS.

Et essayons, par exemple, de prendre par le nom, K eight s web two Ingenix.

Et je vois maintenant trois conteneurs différents qui appartiennent à ce déploiement.

Et maintenant, ils sont créés en utilisant CRI.

Oh.

Très bien, maintenant déconnectons-nous de ce serveur.

Très bien, les gars, c'est tout pour ce cours Kubernetes pour les débutants.

Vous pouvez bien sûr garder votre cluster minikube en cours d'exécution.

Vous pouvez créer d'autres déploiements, vous pouvez construire d'autres images Docker.

En d'autres termes, jouez avec Kubernetes comme vous le souhaitez et familiarisez-vous avec tous les outils Kubernetes que nous avons discutés dans ce cours.

J'espère que vous avez apprécié ce cours et j'espère que vous avez apprécié passer du temps avec moi.

Si c'est le cas, vous pouvez me trouver sur les réseaux sociaux, tous les liens vous les trouverez ici à l'écran et je serai plus qu'heureux de vous rencontrer dans d'autres vidéos et je vous souhaite tout le meilleur.

Au revoir.