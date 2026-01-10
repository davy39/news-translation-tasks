---
title: Tutoriel OpenStack – Gérez Votre Propre Cloud Privé (Cours Complet)
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2022-07-11T14:40:04.000Z'
originalURL: https://freecodecamp.org/news/openstack-tutorial-operate-your-own-private-cloud
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/openstack.png
tags:
- name: Infrastructure as code
  slug: infrastructure-as-code
- name: youtube
  slug: youtube
seo_title: Tutoriel OpenStack – Gérez Votre Propre Cloud Privé (Cours Complet)
seo_desc: 'OpenStack is an open source software that provides cloud infrastructure
  for virtual machines, bare metal, and containers.

  In this article, you will learn how to use OpenStack to operate your own private
  cloud.

  By the end of the tutorial, you will hav...'
---

OpenStack est un logiciel open source qui fournit une infrastructure cloud pour les machines virtuelles, les serveurs bare metal et les conteneurs.

Dans cet article, vous apprendrez à utiliser OpenStack pour gérer votre propre cloud privé.

À la fin de ce tutoriel, vous aurez une compréhension de base de ce qu'est OpenStack et vous connaîtrez les bases de la configuration et de l'administration d'OpenStack en utilisant la plateforme OpenMetal. Vous comprendrez également certains services OpenStack couramment utilisés.

En plus de créer cette version article du tutoriel, j'ai également créé une version vidéo. Vous pouvez regarder la vidéo sur la chaîne YouTube de freeCodeCamp.org.

%[https://youtu.be/_gWfFEuert8]

Pour suivre ce tutoriel, il peut être utile d'avoir une compréhension de base de la ligne de commande Linux, des réseaux et de la virtualisation. Mais rien de tout cela n'est requis.

Merci à OpenMetal pour avoir sponsorisé ce tutoriel.

## Qu'est-ce qu'OpenStack ?

OpenStack est une plateforme de cloud computing open source utilisée par les organisations pour gérer et contrôler des déploiements à grande échelle de machines virtuelles, comme dans un environnement de cloud computing ou de serveur privé virtuel. OpenStack est un choix populaire pour les organisations car il est scalable, fiable et offre un haut degré de contrôle sur l'infrastructure sous-jacente.

En plus d'être utilisé pour gérer des déploiements de machines virtuelles, OpenStack peut également être utilisé pour gérer les ressources de stockage et de réseau dans un environnement cloud.

À certains égards, OpenStack peut être comparé à AWS, mais voici quelques différences clés entre les deux :

* OpenStack est une plateforme open source, tandis qu'AWS est une plateforme propriétaire.
* OpenStack offre plus de flexibilité et d'options de personnalisation qu'AWS.
* OpenStack nécessite généralement plus d'expertise technique pour être configuré et géré qu'AWS, car vous devez essentiellement tout configurer vous-même.

Examinons plus en détail ce qu'OpenStack offre.

Au-delà des fonctionnalités standard d'infrastructure en tant que service, des composants supplémentaires fournissent l'orchestration, la gestion des pannes et des services, et d'autres services pour assurer une haute disponibilité des applications utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/openstack.svg)
_Diagramme OpenStack._

OpenStack est divisé en services pour vous permettre de brancher et de jouer avec les composants en fonction de vos besoins. La carte OpenStack ci-dessous montre les services courants et comment ils s'emboîtent.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/openstack-map.svg)
_Carte OpenStack._

Je ne couvrirai pas tous les services, mais voici ce que font certains des services OpenStack les plus courants.

**Stockage d'objets** : OpenStack Object Storage (Swift) est un système de stockage d'objets distribué et hautement scalable.

**Calcul** : OpenStack Compute (Nova) est un contrôleur de tissu de cloud computing, qui gère l'allocation des ressources de calcul.

**Réseautage** : OpenStack Networking (Neutron) est un système pour gérer les réseaux et les adresses IP.

**Tableau de bord** : Le tableau de bord OpenStack (Horizon) est une interface web pour gérer les ressources OpenStack.

**Identité** : OpenStack Identity (Keystone) est un système pour gérer les comptes utilisateur et le contrôle d'accès.

**Image** : OpenStack Image (Glance) est un service pour stocker et récupérer des images de machines virtuelles.

**Stockage par blocs** : OpenStack Block Storage (Cinder) est un service pour gérer les dispositifs de stockage par blocs.

**Télémétrie** : OpenStack Telemetry (Ceilometer) est un service pour collecter et stocker des données de mesure.

**Orchestration** : OpenStack Orchestration (Heat) est un service pour l'orchestration et la formation de cloud.

**Bare Metal** : OpenStack Bare Metal (Ironic) est un service pour le provisionnement et la gestion des serveurs bare metal.

**Traitement de données** : OpenStack Data Processing (Sahara) est un service pour le provisionnement et la gestion des clusters Hadoop et Spark.

Nous allons démontrer quelques-uns des services OpenStack les plus courants plus tard dans ce cours.

Il existe plusieurs façons différentes de déployer et de configurer OpenStack en fonction des besoins de votre application ou organisation.

Dans ce cours, nous apprendrons comment commencer avec OpenStack et utiliser de nombreuses fonctionnalités les plus courantes.

L'une des façons les plus simples de commencer avec OpenStack est d'utiliser le cloud privé à la demande OpenMetal. Cela nous permet de déployer rapidement OpenStack dans le cloud et simplifie le processus de configuration. OpenMetal a fourni une subvention qui a rendu ce tutoriel possible.

Bien que nous utiliserons OpenMetal pour apprendre OpenStack, le matériel couvert dans ce tutoriel s'applique à tout déploiement OpenStack, pas seulement à ceux qui utilisent OpenMetal. Donc, peu importe comment vous souhaitez utiliser OpenStack, ce tutoriel est pour vous.

## Configuration d'OpenStack sur OpenMetal

Pour configurer OpenStack, vous devez provisionner et configurer votre cloud sur OpenMetal. Suivez simplement les invites sur [cette page OpenMetal Central](https://central.openmetal.io/) pour tout configurer.

Lors de la configuration, vous devrez

Les clouds privés OpenMetal sont déployés avec OpenStack sur trois serveurs bare metal. Ces trois serveurs constituent le cœur du cloud privé. Pour OpenStack, ces trois serveurs sont considérés comme le plan de contrôle. Les clouds privés sont déployés avec Ceph, fournissant à votre cloud un stockage partagé. Ceph est une solution de stockage définie par logiciel open source.

Examinons les actifs matériels qui ont été créés sur OpenMetal. Si vous venez de créer un cloud, vous êtes peut-être déjà sur la page de gestion du cloud. Sinon, cliquez sur "gérer". Cliquez maintenant sur "Assets" dans le menu de gauche.

Cette page contient une liste des actifs inclus avec votre déploiement de cloud privé. Ceux-ci incluent vos nœuds de plan de contrôle matériels et les blocs IP pour les adresses IP d'inventaire et de fournisseur.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-51.png)
_Page des actifs du tableau de bord de gestion du cloud pour OpenMetal_

La capture d'écran ci-dessus est une liste des actifs dans un cloud privé de démonstration. Votre cloud privé peut avoir un matériel différent en fonction des options que vous avez sélectionnées dans votre déploiement :

Dans cet exemple, vous remarquerez trois sections principales :

* 3 nœuds de plan de contrôle **mb_small_v1** du cœur du cloud
* Blocs d'adresses IP d'inventaire
* Blocs d'adresses IP de fournisseur

Avec ces clouds privés, OpenStack est déployé avec trois nœuds de plan de contrôle hyper-convergés.

Vous pouvez accéder directement à ces nœuds de plan de contrôle via SSH en tant qu'utilisateur root. Cet accès est effectué via les clés SSH que vous avez fournies lors de votre déploiement de cloud privé. Utilisez cette commande pour vous connecter (vous devrez changer le nom de la clé et l'IP pour correspondre à vos informations) :

`ssh -i ~/.ssh/votre_nom_de_clé root@173.231.217.21`

## Prise en main d'OpenStack Horizon

Horizon est le nom du tableau de bord OpenStack par défaut, qui fournit une interface utilisateur basée sur le web pour les services OpenStack. Il permet à un utilisateur de gérer le cloud.

Pour accéder au tableau de bord OpenStack (appelé Horizon) de votre nouveau cloud, vous devrez obtenir le mot de passe administrateur de Horizon. Le nom d'utilisateur est "admin".

Pour commencer, connectez-vous en SSH à l'un des serveurs du cloud (vous pouvez utiliser n'importe quelle adresse IP de la page "Assets"). Par exemple :

`ssh -i ~/.ssh/votre_nom_de_clé root@173.231.217.21`

Une fois connecté au serveur, exécutez cette commande :

`grep keystone_admin_password /etc/kolla/passwords.yml`

Le mot de passe sera affiché dans la sortie comme dans cet exemple :

`keystone_admin_password: aB0cD1eF2gH3iJ4kL5mN6oP7qR8sT9uV`

Ensuite, lancez Horizon. Sur OpenMetal, vous pouvez cliquer sur l'onglet "Horizon" dans le menu de gauche.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-52.png)

Connectez-vous en utilisant "admin" et le mot de passe que vous venez d'obtenir.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-53.png)
_Tableau de bord Horizon._

## Créer un projet dans OpenStack Horizon

Dans OpenStack, le cloud est divisé par l'utilisation de projets. Les projets ont des utilisateurs associés, qui ont différents niveaux d'accès, définis par des rôles. Un administrateur définit les limites de ressources par projet en modifiant les quotas.

Maintenant, nous allons apprendre à créer un projet et à associer un utilisateur à celui-ci. Et nous apprendrons comment les quotas de projet peuvent être ajustés. L'interface Horizon sera similaire, peu importe où vous déployez OpenStack. Cela n'est pas spécifique à OpenMetal.

Il y a trois onglets de niveau racine dans le menu de gauche dans Horizon : Projet, Admin et Identité. Seuls les utilisateurs avec des privilèges administratifs peuvent voir l'onglet admin.

Pour créer votre premier projet, naviguez vers Identité -> Projets.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-56.png)
_Projets._

Plusieurs projets existent déjà, y compris le projet admin. Ces projets sont déployés par défaut et ne doivent généralement pas être modifiés.

Cliquez sur le bouton **Créer un projet** en haut à droite pour créer un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-57.png)

Sous le champ **Nom**, spécifiez un nom pour le projet. Ce projet d'exemple s'appelle **Développement**. Vous pouvez également ajouter des membres de projet et des groupes de projet, mais nous n'allons pas les couvrir pour l'instant. Cliquez sur **Créer un projet** pour terminer la création du premier projet.

Une fois créé, le projet apparaît dans la page de liste des projets.

Tout en étant dans la page de liste des projets, vous pouvez afficher et ajuster les quotas pour ce projet en tant qu'utilisateur **admin**. Les quotas sont des limites sur les ressources, comme le nombre d'instances.

Pour afficher les quotas de ce projet tout en étant dans l'onglet **Identité -> Projets**, trouvez le menu déroulant à droite avec la première option étant **Gérer les membres**. À partir de ce menu, cliquez sur **Modifier les quotas** pour afficher les valeurs de quota par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-58.png)

Vous verrez un formulaire avec plusieurs onglets et vous serez présenté avec les quotas pour le service de calcul. Les quotas existent également pour les services de volume et de réseau.

Vous pouvez ajuster les paramètres de ce formulaire en fonction de votre charge de travail. Définir une valeur sur `-1` signifie que le quota est illimité.

## Comment créer un utilisateur et l'associer à un projet

Maintenant que vous avez un projet, vous pouvez associer un utilisateur à celui-ci. Il y a déjà l'utilisateur **admin** par défaut, mais voyons maintenant comment créer un nouvel utilisateur et se connecter avec le nouvel utilisateur.

Tout d'abord, naviguez en tant qu'**admin** vers **Identité -> Utilisateurs**. Par défaut, plusieurs utilisateurs sont déjà listés, et c'est attendu. Ceux-ci sont créés lors du déploiement du cloud et ne doivent généralement pas être modifiés.

Cliquez sur le bouton **Créer un utilisateur**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-74.png)
_Onglet Utilisateurs._


Dans le formulaire de création d'utilisateur, définissez les valeurs pour **Nom d'utilisateur**, **Mot de passe**, **Projet principal** et **Rôle**. Le champ **Email** est facultatif mais utile pour les réinitialisations de mot de passe. Pour le **Projet**, choisissez le projet que nous avons créé précédemment.

Pour le **Rôle**, il y a plusieurs options selon le niveau d'accès requis. Les rôles OpenStack par défaut sont **lecteur**, **membre** et **admin**. Des rôles supplémentaires existent également dans le menu déroulant. **Lecteur** est le rôle le moins autoritaire dans la hiérarchie. Pour cet exemple, choisissez **membre** pour le rôle.

Appuyez sur **Créer un utilisateur** pour créer l'utilisateur.

Ensuite, déconnectez-vous de Horizon en tant qu'**admin**, et reconnectez-vous avec votre nouvel utilisateur. Après vous être reconnecté, vous êtes par défaut dans le projet nouvellement créé. Vous pouvez voir le projet dans lequel vous vous trouvez en haut à gauche et votre utilisateur peut être vu en haut à droite de Horizon.

## Gestion et création d'images

Maintenant, apprenons à télécharger une image (non pas une image graphique mais une copie d'une installation Linux) dans OpenStack ainsi qu'à créer des images à partir d'une instance existante.

Les images contiennent un système d'exploitation amorçable qui est utilisé pour créer des instances. Dans votre cloud OpenMetal, il existe plusieurs images différentes qui sont immédiatement disponibles, notamment CentOS, Debian, Fedora et Ubuntu. En plus de cela, vous avez la possibilité de télécharger des images à partir d'autres sources ou de créer vos propres images.

Nous allons apprendre à télécharger des images vers Glance via Horizon et à créer une image à partir d'un instantané d'instance. Glance est un outil de gestion d'images qui permet aux utilisateurs de découvrir, récupérer et enregistrer des images de machines virtuelles (VM) et des images de conteneurs. Glance utilise Ceph pour stocker les images au lieu du système de fichiers local.

Pour accéder aux images depuis votre tableau de bord Horizon, naviguez vers l'onglet **Projets**. Dans l'onglet projets, sélectionnez **Calcul** puis **Images**. Cet onglet contient une liste de toutes vos images dans OpenStack.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-75.png)
_Images_

Les images peuvent être téléchargées via votre tableau de bord Horizon en cliquant sur le bouton **Créer une image**. Lors de la création d'une image, vous devez choisir le format de l'image. Avec notre configuration, le format recommandé pour les images est **QCOW2 – Émulateur QEMU**. QCOW2 est le format le plus courant pour Linux KVM, s'étend dynamiquement et prend en charge la copie à l'écriture.

Pour télécharger une image sur Horizon, vous devez d'abord avoir l'image localement sur votre machine. Dans cet exemple, nous allons télécharger une image CirrOS. Vous pouvez télécharger une [image CirrOS ici](https://download.cirros-cloud.net/0.5.2/cirros-0.5.2-x86_64-disk.img).

Cliquez maintenant sur le bouton **Créer une image** en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-85.png)

Pour cet exemple, nous utiliserons les valeurs suivantes pour les champs :

* **Nom de l'image** : Nom de l'image
* **Description de l'image** : Description facultative de l'image
* **Fichier** : Le fichier source sur votre machine
* **Format** : QCOW2 – Émulateur QEMU

Remplissez les détails selon vos besoins et soumettez le formulaire. Cela peut prendre un certain temps pour terminer le téléchargement de l'image.

## Créer une instance dans OpenStack Horizon

Avec OpenStack, les instances, ou machines virtuelles, jouent un rôle important dans la charge de travail d'un cloud. OpenStack fournit un moyen de créer et de gérer des instances avec son service de calcul, appelé [Nova](https://docs.openstack.org/nova/latest/).

Nova est le projet OpenStack qui fournit un moyen de provisionner des instances de calcul (alias serveurs virtuels). Nova prend en charge la création de machines virtuelles, de serveurs bare metal et a un support limité pour les conteneurs système. Nova s'exécute comme un ensemble de démons sur des serveurs Linux existants pour fournir ce service.

Maintenant, apprenons à créer une instance, y compris la configuration d'un réseau privé et d'un routeur, la création d'un groupe de sécurité et comment ajouter une paire de clés SSH.

### Créer un réseau privé

Tout d'abord, apprenons à créer un réseau privé et un routeur. Plus tard, nous créerons une instance sur ce réseau privé. Le routeur est créé pour que le réseau privé puisse être connecté au réseau public de votre cloud, vous permettant d'assigner une adresse IP flottante, rendant l'instance accessible via Internet.

Pour créer un réseau privé, commencez par naviguer vers **Projet -> Réseau -> Réseaux**. Ensuite, cliquez sur **Créer un réseau**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-86.png)
_Onglet Réseaux._

Pour cet exemple, nous allons créer un réseau avec les détails suivants :

* **Nom du réseau** : Définissez un nom pour le réseau. Cet exemple s'appelle **Privé**.
* **Activer l'état admin** : Laissez cette case cochée pour activer le réseau.
* **Créer un sous-réseau** : Laissez cette case cochée pour créer un sous-réseau.
* **Indices de zone de disponibilité** : Laissez cette option par défaut.

Ensuite, passez à l'onglet **Sous-réseau** de ce formulaire et utilisez ces détails :

* **Nom du sous-réseau** : Définissez un nom pour le sous-réseau. Ce sous-réseau d'exemple s'appelle **private-subnet**.
* **Adresse réseau** : Sélectionnez une plage de réseau privé. Par exemple : `192.168.0.1/24`
* **Version IP** : Laissez cela en IPv4.
* **IP de la passerelle** : Ceci est facultatif. Si non défini, une IP de passerelle est sélectionnée automatiquement.
* **Désactiver la passerelle** : Laissez cette case décochée.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-87.png)
_Créer un réseau._

Pour l'instant, nous conserverons les détails par défaut dans l'onglet **Détails du sous-réseau**.

Cliquez sur **Créer** pour créer le réseau. Une fois créé, il apparaît dans la liste des réseaux.

### Créer un routeur

Vous devez ensuite créer un routeur pour établir la connexion entre le réseau privé et le réseau public. Le réseau public s'appelle **Externe**.

Pour créer un routeur, commencez par naviguer vers **Projet -> Réseau -> Routeurs**. Cliquez sur **Créer un routeur**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-88.png)
_Routeurs._

Saisissez ces données pour cet exemple :

* **Nom du routeur** : Définissez un nom pour le routeur ici. Ce routeur d'exemple s'appelle **Routeur**.
* **Activer l'état admin** : Laissez cette case cochée pour activer le routeur.
* **Réseau externe** : Choisissez le réseau **Externe**.
* **Indices de zone de disponibilité** : Laissez cela par défaut.

Une fois terminé, créez le routeur en appuyant sur **Créer un routeur**.

### Connecter le routeur au réseau privé

Ensuite, connectez le routeur au réseau privé en attachant une interface. Effectuer cette étape permet la communication réseau entre les réseaux Privé et Externe.

Pour attacher une interface au routeur, commencez par naviguer vers la liste des routeurs et localisez celui créé précédemment.

Cliquez sur le nom du routeur pour accéder à sa page de détails. C'est ici que l'interface est attachée. Il y a trois onglets : **Aperçu**, **Interfaces** et **Routes statiques**. Pour attacher une interface, naviguez vers l'onglet **Interfaces**, puis chargez le formulaire pour attacher une interface en cliquant sur **Ajouter une interface** en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-89.png)

Sur la nouvelle interface, choisissez le private-subnet pour **Sous-réseau**. Si vous ne définissez pas d'adresse IP, une est sélectionnée automatiquement. Appuyez sur **Soumettre** pour attacher le réseau **Privé** à ce routeur. L'interface est alors attachée et maintenant listée.

Vous pouvez voir visuellement la topologie du réseau pour votre cloud en naviguant vers **Projet -> Réseau -> Topologie du réseau**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-90.png)

L'exemple ci-dessus indique que le réseau **Externe** est connecté au réseau **Privé** via le routeur appelé **Routeur**.

### Groupes de sécurité

Les groupes de sécurité permettent de contrôler le trafic réseau vers et depuis les instances. Par exemple, le port 22 peut être ouvert pour SSH pour une seule IP ou une plage d'IP.

Voyons comment créer un groupe de sécurité pour l'accès SSH. Plus tard, nous appliquerons le groupe de sécurité que nous créons à une instance.

Pour afficher et gérer les groupes de sécurité, naviguez vers **Projet -> Réseau -> Groupes de sécurité**.

Vous devriez remarquer un seul groupe de sécurité appelé **default**. Ce groupe de sécurité restreint tout le trafic réseau entrant (ingress) et permet tout le trafic réseau sortant (egress). Lorsque qu'une instance est créée, ce groupe de sécurité est appliqué par défaut. Pour permettre le trafic réseau que votre instance nécessite, ouvrez uniquement les ports nécessaires pour les plages d'IP requises.

Pour créer un groupe de sécurité pour SSH, cliquez sur **Créer un groupe de sécurité** en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-92.png)

Nommez le groupe **SSH**, puis cliquez sur **Créer un groupe de sécurité**

Après avoir créé le groupe de sécurité SSH, nous devons ajouter une règle permettant le trafic SSH. Nous allons autoriser le trafic SSH depuis le premier nœud matériel de ce cloud vers cette instance.

Pour ajouter une règle, chargez le formulaire en naviguant vers **Ajouter une règle** en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-93.png)

Nous devons obtenir l'adresse IP du premier nœud matériel de votre cloud. Vous pouvez la trouver en utilisant [OpenMetal Central](https://central.openmetal.io/) sous la page [Assets Page](https://central.openmetal.io/documentation/operators-manual/introduction-to-openmetal-central-and-your-private-cloud-core#how-to-view-your-hardware-assets) de votre cloud.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-94.png)
_L'adresse IP du premier nœud matériel._

Dans le menu **Ajouter une règle**, ajoutez les informations suivantes :

* **Règle** : Sélectionnez **SSH**. Lors de l'ajout de règles, vous pouvez choisir parmi des options prédéfinies. Dans ce cas, nous choisissons la règle **SSH** dans le premier menu déroulant.
* **Description** : Facultatif. Fournissez une description de la règle.
* **Distance** : Sélectionnez **CIDR**.
* **CIDR** : Spécifiez l'adresse IP de votre premier nœud matériel.

Appuyez sur **Ajouter** pour ajouter cette règle au groupe de sécurité.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-95.png)
_Ajout d'une règle._

## Créer une instance

Nous avons maintenant presque tout en place pour créer une instance.

Nous aurons besoin d'une clé publique SSH. Une clé publique SSH est requise pour accéder à une instance via SSH. Cette clé est injectée dans l'instance lors de sa création. Une clé SSH ne peut pas être ajoutée à une instance déjà en cours d'exécution.

Nous allons créer une instance accessible via SSH depuis l'un des nœuds matériels du cloud. Nous devrons donc créer une paire de clés SSH dans l'un des nœuds matériels. La partie publique de cette paire de clés est associée à l'instance que nous créerons bientôt.

**** Pour apprendre à créer cette paire de clés, consultez le guide complémentaire : [Créer une paire de clés SSH pour un nœud de plan de contrôle OpenStack](https://central.openmetal.io/documentation/operators-manual/create-ssh-key-pair-for-an-openstack-control-plane-node/).**

Pour créer une instance, commencez par naviguer vers **Projet -> Calcul -> Instances**. Ensuite, cliquez sur le bouton **Lancer une instance**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-96.png)

Dans l'onglet détails, remplissez les détails suivants :

* **Nom de l'instance** : Définissez un nom pour l'instance. Cette instance d'exemple s'appelle **Jumpstation**.
* **Description** : Facultatif. Définissez une description si cela s'applique.
* **Zone de disponibilité** : Laissez par défaut, qui est **nova**.
* **Compte** : Contrôle le nombre d'instances générées. Créez-en simplement 1.

Ensuite, passez à l'onglet **Source** vous permettant de spécifier une image de système d'exploitation.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-97.png)
_Onglet Source._

Remplissez les détails suivants :

* **Sélectionner la source de démarrage** : Dans cet exemple, nous utilisons **Image** comme source de démarrage.
* **Créer un nouveau volume** : Laissez cette case cochée sur **Oui**. Cela crée un nouveau volume Cinder où l'image du système d'exploitation spécifiée est copiée. Le volume existe finalement avec le cluster Ceph, dans le pool `vms`.
* **Taille du volume** : Laissez le système déterminer cela pour vous.
* **Supprimer le volume lors de la suppression de l'instance** : Laissez cette option définie sur **Non**. Si cochée, lorsque l'instance est supprimée, le volume l'est également.
* Sous la section **Disponible**, sélectionnez le système d'exploitation approprié. Cet exemple utilise `CentOS 8 Stream (el8-x86_64)`. Cliquer sur la flèche vers le haut la déplacera dans la section **Allouée**.

Cela conclut la configuration de la source de l'instance. Ensuite, passez à l'onglet **Flavor**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-100.png)
_Onglet Flavor._

Les flavors sont un moyen de définir les VCPUs, la RAM et l'espace disque utilisés par une instance. Des flavors pré-construits sont disponibles pour vous. Pour cette étape, sélectionnez un flavor approprié parmi les options sous l'en-tête Disponible. Cet exemple utilise le flavor m1.small. Cliquez sur la flèche vers le haut pour le déplacer dans la section **Allouée**.

Ensuite, passez à l'onglet Réseaux.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-101.png)
_Onglet Réseau._

Dans cette section, vous spécifiez le réseau auquel l'instance est associée. Pour cet exemple, sélectionnez le réseau **Privé** créé précédemment. Vous pouvez également choisir le réseau **Externe**, mais cela est généralement déconseillé en faveur de l'utilisation d'une IP flottante si votre instance nécessite une connectivité Internet.

Vous ne devez exposer que les parties de votre réseau nécessaires. Cela réduit la surface d'attaque et améliore la sécurité des applications. Si un réseau privé n'est pas créé et qu'une instance est créée dans un cloud par défaut, elle est associée au réseau **Externe**. Cela signifie que l'instance consomme une IP publique et pourrait être atteinte via Internet.

Ensuite, passez l'onglet **Ports réseau** et allez à **Groupes de sécurité**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-102.png)
_Onglet Groupes de sécurité._

C'est ici que vous sélectionnez les groupes de sécurité pour l'instance. Cet exemple utilise le groupe de sécurité **SSH** dans la section **Disponible**. Cliquez sur la flèche vers le haut pour déplacer le groupe de sécurité SSH dans la section **Allouée**.

En tant qu'étape finale, passez à l'onglet **Paire de clés**.

Dans cette section, vous spécifiez une clé publique SSH à injecter dans l'instance. Vous pouvez télécharger votre clé à ce stade en utilisant ce formulaire en utilisant le bouton **Importer une paire de clés**. Vous pouvez également créer une paire de clés dans cet onglet.

Nous allons créer une paire de clés à partir du premier nœud matériel de notre cloud afin que cette instance soit accessible via SSH depuis ce nœud.

Pour créer la paire de clés SSH à partir du premier nœud matériel, la première étape consiste à se connecter au premier nœud matériel. Vous pouvez obtenir l'IP du nœud matériel à partir de l'onglet Assets sur OpenMetal. Nous nous sommes déjà connectés à ce nœud vers le début du tutoriel et la commande est la même. Cela ressemblera à quelque chose comme ceci :

`ssh -i ~/.ssh/votre_nom_de_clé root@173.231.217.21`

Après vous être connecté au nœud, utilisez `ssh-keygen` pour générer une paire de clés SSH.

Par exemple :

```
[root@modest-galliform ~]# ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:BNIzHPcqCyjjZqWm88s0zqHrj8J8+gUnkF1cNOEDKZs root@modest-galliform.local
The key's randomart image is:
+---[RSA 3072]----+
|    o=**o        |
|  o..+Bo..       |
| o .+  =. .      |
|  .E   ...       |
|o .+... S        |
|.oo +. o         |
|o*+  ..          |
|BO.+.            |
|*B@+             |
+----[SHA256]-----+
```

La clé privée est enregistrée dans l'emplacement par défaut `/root/.ssh/id_rsa` et une phrase secrète est définie pour une sécurité supplémentaire.

Pour afficher le contenu de la clé publique, utilisez `cat /root/.ssh/id_rsa.pub`.

Par exemple :

```
[root@modest-galliform ~]# cat /root/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCv6YOgYbRmXCEFxZP+t+pzh/RRKzsgWpvcnmKwF+uwiKDuihHadScCkgd8dE6ymCjP/+UVdVLGEzXfHXG5EfbcPQYOGjqqOGqOVCHIrhFMG3GjSPao99KaDIAvXsWyTDI9FmrXTiC+0WkmOLNb0UeDic+lQ6KJumw12O1niZjC19jMpWR5amRWEJo6oKFylC8JLHsdfhqr7EBcBzvUJkqh/1zY3qcsABHBrBCWOKC5oNiDAzctQ5MeHq6tv6w6YxdZLLdupczteERN6roroySMtR2JZnOIcnq1aUgD/YDJDeg9zpvUN7stsndONYVOH42+bBu7xEWsm8zobgdfLlmhv+8ab7dKVlYvJUkITqCoKpp8m0f3dbLtQSevCJ9qaeQvmxkjU9OHVPkkTolw4aUHvUsutpVynNfmErf3RGMjQRiQ3ZE7xGKVV7iSFDK9l0mMWBHpYu2OnVKQlP823IC0YKD2dP3qDd/nnvGXVlxfRI+C08n9ehoHwZAIz4SM3dU= root@modest-galliform.local
```

Copiez la clé entière. Elle commence par "ssh-rsa" et continue jusqu'à la fin.

Retournez maintenant à l'onglet **Paire de clés**. Cliquez sur **Importer une paire de clés**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-103.png)

Saisissez les valeurs suivantes :

* **Nom de la paire de clés** : Définissez un nom pour la clé publique SSH. Cette clé publique d'exemple s'appelle `jumpstation-key`, mais elle peut vraiment être n'importe quoi.
* **Type de clé** : Cet exemple utilise un type de clé **Clé SSH**.
* **Clé publique** : Collez la clé publique que vous venez de copier.

Cliquez sur **Importer une paire de clés**.

Une fois la clé publique importée, créez l'instance en appuyant sur **Lancer une instance**. (Les autres onglets sont en dehors du cadre de cette démonstration.)

L'instance passe par un processus de construction. Laissez quelques minutes pour que cela se produise. Une fois terminé, l'instance apparaît dans la page **Liste des instances**.

### Assigner et attacher une IP flottante

L'instance créée précédemment est associée à un réseau privé. Actuellement, la seule façon d'accéder à cette instance est de s'y connecter depuis les nœuds matériels du cloud. Une autre option pour se connecter est d'utiliser une IP flottante. Dans cette section, nous démontrons comment allouer une IP flottante et l'attacher à cette instance.

Pour allouer une IP flottante, naviguez d'abord vers **Projet -> Réseau -> IP flottantes**. Ensuite, cliquez sur **Allouer une IP au projet**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-104.png)
_Onglet IP flottantes._

Dans la fenêtre contextuelle, assurez-vous que **Pool** est défini sur **Externe** (et ajoutez éventuellement une description), puis cliquez sur **Allouer une IP** pour ajouter cette adresse IP flottante à utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-105.png)

Dans la même section, allouez l'IP à l'instance Jumpstation en cliquant sur le bouton **Associer** à l'extrême droite.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-106.png)

Remplissez les détails :

* **Adresse IP** : Ce champ est présélectionné avec l'IP flottante, donc il n'est pas nécessaire de changer quoi que ce soit ici.
* **Port à associer** : Sélectionnez l'instance créée précédemment. Dans ce cas, nous utilisons l'instance Jumpstation.

Cliquez sur **Associer**. Cette instance est maintenant accessible via SSH depuis le premier nœud matériel de votre cloud.

Pour vous connecter à cette instance, après vous être connecté à votre nœud matériel, exécutez la commande suivante [vous devrez changer l'adresse IP par celle que vous venez d'associer] :

`ssh -i /root/.ssh/id_rsa centos@173.231.255.40`

Cela devrait ressembler à quelque chose comme ceci dans votre terminal :

```
[root@modest-galliform ~]# ssh -i /root/.ssh/id_rsa centos@173.231.255.40
The authenticity of host '173.231.255.40 (173.231.255.40)' can't be established.
ECDSA key fingerprint is SHA256:z45zzE8fPuKagtyrSGP9AWR4vIVpBppoaqkqj1Kx4SA.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '173.231.255.40' (ECDSA) to the list of known hosts.
Enter passphrase for key '/root/.ssh/id_rsa': 
Activate the web console with: systemctl enable --now cockpit.socket

[centos@jumpstation ~]$ 
```

Dans la section suivante, vous devrez faire quelque chose en étant connecté à cette machine.

### Comment installer et utiliser l'interface de ligne de commande d'OpenStack

Jusqu'à présent, nous avons appris à gérer OpenStack via un navigateur web. Mais il est également possible de gérer via la ligne de commande en utilisant l'interface de ligne de commande d'OpenStack appelée OpenStackClient.

L'utilisation de la ligne de commande pour gérer votre cloud introduit plus de flexibilité dans les tâches d'automatisation et peut généralement simplifier la vie d'un administrateur. Apprenons comment.

Nous allons maintenant installer OpenStackClient sur l'instance que nous venons de créer et que nous avons nommée Jumpstation.

Avant d'installer OpenStackClient, vous devez obtenir deux fichiers de Horizon, qui sont nécessaires pour préparer votre environnement shell. Ces deux fichiers sont `clouds.yaml` et le fichier RC OpenStack.

* `clouds.yaml` : Utilisé comme source de configuration pour la connexion à un cloud
* Fichier RC OpenStack : Utilisé comme source d'authentification pour votre utilisateur et projet

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-141.png)

Pour collecter ces fichiers, connectez-vous à Horizon en tant que votre utilisateur. Naviguez vers **Projet -> Accès API**. Ensuite, cliquez sur **Télécharger le fichier RC OpenStack** et téléchargez les fichiers `clouds.yaml` et `OpenStack RC` sur votre machine. Les fichiers sont associés à l'utilisateur actuel et au projet dans lequel se trouve cet utilisateur.

#### Préparer et installer OpenStackClient

Ensuite, utilisez SSH pour vous connecter à l'instance créée précédemment. Si vous avez suivi jusqu'à présent, alors cette instance ne peut être accessible que depuis l'un de vos nœuds de plan de contrôle. Utilisez les instructions récemment données pour vous connecter à l'instance.

Voici les étapes pour préparer et installer OpenStackClient, après vous être connecté.

**Étape 1** : Préparer les fichiers `clouds.yaml` et OpenStack RC

Le fichier `clouds.yaml` obtenu précédemment doit être préparé dans cette instance. Pour cette démonstration, nous allons l'enregistrer dans `~/.config/openstack/clouds.yaml`. Nous devrons copier le contenu de `clouds.yaml` que nous avons téléchargé sur notre machine depuis Horizon et le stocker en tant que `~/.config/openstack/clouds.yaml`.

Voici comment créer le répertoire puis éditer le fichier. Exécutez les commandes après le `$` sur votre ligne de commande.

```
# Créer le répertoire suivant
$ mkdir -p ~/.config/openstack

# Créer et ouvrir clouds.yaml pour l'éditer
$ vi ~/.config/openstack/clouds.yaml

```

Pour obtenir le contenu du fichier `clouds.yaml` sur votre ordinateur local dans l'instance, vous devrez d'abord ouvrir la version locale dans un éditeur de texte. Ensuite, vous devrez copier tout le texte puis le coller dans la version que vous venez de créer sur l'instance.

Après avoir collé le texte du fichier dans l'éditeur vi dans votre terminal, utilisez la commande `:wq` pour sauvegarder et quitter l'éditeur.

Le fichier `clouds.yaml` peut en fait être placé à plusieurs endroits. Pour plus d'informations, consultez l'en-tête [Fichiers de configuration](https://docs.openstack.org/python-openstackclient/victoria/configuration/index.html#configuration-files) de la documentation d'OpenStack Victoria.

Ensuite, copiez le contenu du fichier RC OpenStack de votre machine locale dans l'instance. Le fichier peut être placé n'importe où, donc pour cet exemple, nous allons le stocker dans le répertoire personnel de l'utilisateur. Le chemin complet sera `~/Development-openrc.sh`.

Créez et commencez à éditer le fichier avec la commande suivante (ne pas utiliser le `$` lorsque vous copiez et collez la commande).

```
$ vi ~/Development-openrc.sh

```

Tout comme avant, vous devrez ouvrir la version locale du fichier, copier tout le texte, puis le coller dans la version de l'instance du fichier qui est ouverte dans votre terminal. Ensuite, utilisez la commande `:wq` pour sauvegarder et quitter l'éditeur.

Maintenant, vous devez exécuter le fichier. Changez d'abord les permissions :

`$ chmod +x Development-openrc.sh`

Ensuite, exécutez le fichier :

`$ ./Development-openrc.sh`

Vous devrez entrer votre mot de passe OpenStack.

Ensuite, exécutez la commande :

`$ source Development-openrc.sh`

**Étape 2** : Créer un environnement virtuel Python

Nous allons créer un environnement virtuel pour ne pas interférer avec la version Python du système.

Dans une installation par défaut de CentOS 8 Stream, l'exécutable Python du système est `/usr/libexec/platform-python` et est ce qui sera utilisé pour créer l'environnement virtuel.

Utilisez `/usr/libexec/platform-python -m venv ~/venv` pour créer un environnement virtuel dans le chemin `~/venv`.

Par exemple :

```
$ /usr/libexec/platform-python -m venv ~/venv

```

**Étape 3** : Activer l'environnement virtuel Python

Utilisez `source ~/venv/bin/activate` pour activer l'environnement virtuel.

Par exemple :

```
$ source ~/venv/bin/activate

```

Après avoir activé l'environnement virtuel, le nom de celui-ci apparaîtra au début de la ligne de commande. Donc, cela ressemblera à quelque chose comme ceci :

```
[centos@jumpstation ~]$ /usr/libexec/platform-python -m venv ~/venv
[centos@jumpstation ~]$ source ~/venv/bin/activate
(venv) [centos@jumpstation ~]$ 

```

**Étape 4** : Mettre à niveau `pip`

Avant d'installer OpenStackClient et pour faciliter une installation fluide, mettez à niveau `pip`. Mettez à niveau `pip` en utilisant `pip install --upgrade pip`.

Par exemple :

```
$ pip install --upgrade pip

```

**Étape 5** : Installer OpenStackClient

Avec tout préparé, OpenStackClient peut être installé.

**Note !** – Il existe deux packages OpenStackClient : `python-openstackclient` et `openstackclient`. Je recommande d'utiliser `python-openstackclient` car il est maintenu beaucoup plus fréquemment que le package précédent.

Installez OpenStackClient en utilisant :

```
$ pip install python-openstackclient

```

**Étape 6** : Lister les serveurs associés à votre projet

Pour une commande initiale, listez les serveurs associés à votre projet en exécutant `openstack server list`.

Par exemple :

```
(venv) [centos@jumpstation ~]$ openstack server list
+--------------------------------------+-------------+--------+---------------------------------------+--------------------------+----------+
| ID                                   | Name        | Status | Networks                              | Image                    | Flavor   |
+--------------------------------------+-------------+--------+---------------------------------------+--------------------------+----------+
| 412fc87f-a4d9-40f1-ba07-fe3eee216c38 | Jumpstation | ACTIVE | Private=173.231.255.40, 192.168.0.140 | N/A (booted from volume) | m1.small |
+--------------------------------------+-------------+--------+---------------------------------------+--------------------------+----------+
```

Ici, nous pouvons voir le serveur créé précédemment.

## Structure de commande

Lors de l'utilisation d'OpenStackClient, il existe généralement un modèle de commande courant pour ce que vous souhaitez accomplir. Toutes les commandes `openstack` commencent par `openstack`. Vous pouvez exécuter `openstack` seul pour entrer dans un shell, où les commandes n'ont plus besoin d'être précédées par `openstack` :

```
(venv) [centos@jumpstation ~]# openstack
(openstack)

```

### Lister toutes les sous-commandes disponibles

Utilisez `openstack --help` pour lister toutes les sous-commandes disponibles. Vous voyez initialement tous les drapeaux que vous pouvez passer, mais après avoir fait défiler un peu, la liste des sous-commandes commence :

```
Commands:
  access rule delete  Delete access rule(s)
  access rule list  List access rules
  access rule show  Display access rule details
  access token create  Create an access token
  acl delete  Delete ACLs for a secret or container as identified by its href. (py
thon-barbicanclient)
[...output truncated...]

```

### En savoir plus sur une sous-commande

Après avoir vu les commandes disponibles, en savoir plus sur une commande en utilisant `openstack help <command>`.

Par exemple, pour en savoir plus sur la commande `openstack server`, utilisez `openstack help server` :

```
$ openstack help server
Command "server" matches:
  server add fixed ip
  server add floating ip
  server add network
  server add port
  server add security group
[...output truncated...]

```

### Lister les éléments et afficher les détails

Il est très courant lors de l'utilisation d'OpenStackClient de lister les éléments et la forme de commande est généralement `openstack <subcommand> list`. Par exemple, `openstack server list`, liste tous les serveurs pour le projet actuellement configuré.

De plus, plus d'informations sur un élément peuvent être trouvées en exécutant généralement `openstack <subcommand> show <item>`. Par exemple, `openstack server show Jumpstation` montre les détails sur l'instance nommée **Jumpstation**.

## Comment les clouds privés sont déployés

Maintenant, nous allons en apprendre davantage sur la manière dont votre cloud privé a été déployé et en savoir plus sur l'environnement. OpenStack peut être déployé de plusieurs manières différentes et cette section met en évidence les caractéristiques de votre cloud privé. Nous expliquons également certains des avantages de ce type de déploiement et les domaines qui sont uniques à OpenMetal.

Dans OpenMetal, OpenStack est conteneurisé via Docker en utilisant Kolla Ansible. Cela est fait via un conteneur de déploiement initial appelé FM-Deploy. FM-Deploy fournit les modifications de configuration initiale pendant le processus de provisionnement de votre cloud privé. Le conteneur FM-Deploy est une partie nécessaire de l'architecture actuelle de votre cloud privé. Le conteneur FM-Deploy doit rester en cours d'exécution dans votre cloud privé car il est utilisé par nos systèmes dans le cas où vous souhaitez ajouter ou supprimer des nœuds de votre cloud.

### Conteneurisation d'OpenStack

OpenMetal utilise Kolla Ansible pour configurer des conteneurs Docker pour tous les services en cours d'exécution. Si vous devez apporter des modifications de configuration à vos nœuds, Kolla Ansible doit être utilisé pour pousser ces modifications. Si Kolla Ansible n'est pas utilisé, il existe un risque que ces modifications soient annulées lors des mises à jour du système.

Certains avantages de la conteneurisation via Docker sont :

* Les conteneurs créent un environnement isolé réduisant les dépendances logicielles
* Les conteneurs peuvent être mis à l'échelle et permettent aux services de s'équilibrer sur votre cluster
* Les conteneurs offrent une flexibilité accrue pour les versions de test, les correctifs et l'automatisation
* Les conteneurs ont un déploiement cohérent et reproductible et un temps d'initialisation plus court

### Stockage sur disque et Ceph

Dans OpenMetal, le stockage sur disque est fourni via Ceph. Ceph est une interface de stockage d'objets qui peut fournir des interfaces pour plusieurs types de stockage différents sur un seul cluster. Dans OpenMetal, Ceph est composé de deux éléments : le stockage d'objets et le stockage par blocs.

Le **stockage d'objets Ceph** utilise le démon de passerelle de stockage d'objets Ceph (RADOSGW). Avec les clouds OpenMetal, le RGW de Ceph remplace Swift, donc il n'y a pas de conteneur Docker pour Swift. Au lieu de cela, les points de terminaison Swift sont connectés directement au RGW. L'authentification pour RGW est gérée via Keystone dans `/etc/ceph/ceph.conf`.

Le **stockage par blocs Ceph** se connecte au service Cinder en utilisant le périphérique de bloc RADOS de Ceph. Dans votre cloud, ces objets sont stockés dans des pools Ceph. Ceph fournit une couche d'abstraction qui permet aux objets d'être reconnus comme des blocs.

Certains avantages de l'utilisation de Ceph sont :

* Les données sont auto-cicatrisantes et redistribueront les données sur votre cluster en cas de problèmes d'alimentation, de matériel ou de connectivité
* Les données sont répliquées et hautement disponibles
* Ceph a la capacité de fonctionner sur du matériel standard et de mélanger du matériel de différents fournisseurs

## Introduction à Ceph

Ceph est un système de stockage distribué open-source qui fournit des interfaces de stockage d'objets, de blocs et de fichiers à partir d'un seul cluster.

Ceph a été sélectionné comme solution de stockage pour les clouds OpenStack Private Cloud Core en raison de sa capacité à stocker des données de manière répliquée. Les données stockées dans le cluster Ceph sont accessibles depuis l'un des nœuds de plan de contrôle de votre cloud. Le stockage est considéré comme partagé sur tous les nœuds, ce qui peut rendre la récupération d'une instance et de ses données triviale.

Apprenons comment vérifier l'état de votre cluster Ceph et voir l'utilisation du disque disponible en utilisant la ligne de commande.

### Vérifier l'état de Ceph

Tout d'abord, assurez-vous d'être connecté à l'un des nœuds de plan de contrôle de votre cloud (pas une instance). Pour vérifier l'état de votre cluster Ceph, utilisez `ceph status`.

Par exemple :

```
[root@modest-galliform ~]# ceph status
  cluster:
    id:     ac5c03ba-fcb8-4963-b235-e9020b5bfcc2
    health: HEALTH_OK
 
  services:
    mon: 3 daemons, quorum modest-galliform,gifted-badger,hopeful-guineafowl (age 7d)
    mgr: hopeful-guineafowl(active, since 7d), standbys: modest-galliform, gifted-badger
    osd: 3 osds: 3 up (since 7d), 3 in (since 7d)
    rgw: 3 daemons active (gifted-badger.rgw0, hopeful-guineafowl.rgw0, modest-galliform.rgw0)
 
  task status:
 
  data:
    pools:   12 pools, 329 pgs
    objects: 2.06k objects, 9.4 GiB
    usage:   31 GiB used, 2.6 TiB / 2.6 TiB avail
    pgs:     329 active+clean
 
  io:
    client:   2.2 KiB/s rd, 2 op/s rd, 0 op/s wr
```

### Vérifier l'utilisation du disque Ceph

Pour vérifier l'espace disque disponible dans votre cluster Ceph, utilisez `ceph df`.

Par exemple :

```
[root@modest-galliform ~]# ceph df
--- RAW STORAGE ---
CLASS  SIZE     AVAIL    USED    RAW USED  %RAW USED
ssd    2.6 TiB  2.6 TiB  28 GiB    31 GiB       1.15
TOTAL  2.6 TiB  2.6 TiB  28 GiB    31 GiB       1.15
 
--- POOLS ---
POOL                   ID  PGS  STORED   OBJECTS  USED     %USED  MAX AVAIL
device_health_metrics   1    1  418 KiB        3  1.2 MiB      0    839 GiB
images                  2   32  6.8 GiB      921   20 GiB   0.81    839 GiB
volumes                 3   32  2.4 GiB      662  7.3 GiB   0.29    839 GiB
vms                     4   32  4.2 KiB        6   48 KiB      0    839 GiB
backups                 5   32      0 B        0      0 B      0    839 GiB
metrics                 6   32  2.1 MiB      242  8.4 MiB      0    839 GiB
manila_data             7   32      0 B        0      0 B      0    839 GiB
manila_metadata         8   32      0 B        0      0 B      0    839 GiB
.rgw.root               9   32  2.4 KiB        6   72 KiB      0    839 GiB
default.rgw.log        10   32  3.4 KiB      207  384 KiB      0    839 GiB
default.rgw.control    11   32      0 B        8      0 B      0    839 GiB
default.rgw.meta       12    8      0 B        0      0 B      0    839 GiB

```

## Maintenir les mises à jour logicielles d'OpenStack

Le logiciel dans l'écosystème OpenStack évolue au fil du temps, soit par l'ajout de nouvelles fonctionnalités, des corrections de bugs, ou lorsque des vulnérabilités sont corrigées. Faire fonctionner un cloud OpenStack implique de maintenir son logiciel à jour. Dans cette section, nous soulignons les sections d'un cloud OpenMetal où les mises à jour logicielles se produisent et expliquons les meilleures pratiques lors de la réalisation des mises à jour.

Le logiciel d'un cloud OpenMetal qui peut être mis à jour comprend le gestionnaire de paquets de chaque nœud matériel et les images Docker de Kolla Ansible. Les mises à jour de Ceph sont gérées via le gestionnaire de paquets du nœud.

Maintenant, nous allons spécifiquement couvrir les étapes pour effectuer les mises à jour du gestionnaire de paquets.

1. **Migrer la charge de travail**

Les mises à jour du gestionnaire de paquets nécessitant un redémarrage du serveur sur un nœud de plan de contrôle OpenMetal peuvent perturber toute charge de travail en cours d'exécution. Avant de réaliser des actions perturbatrices, il peut être possible de migrer les instances vers un autre nœud exécutant le service Compute. Pour des informations sur la migration des instances, consultez la [documentation](https://docs.openstack.org/nova/latest/admin/live-migration-usage.html) d'OpenStack Nova.

**2. Mettre à jour un nœud à la fois**

Lors de la réalisation des mises à jour du gestionnaire de paquets, assurez-vous que les mises à jour se produisent avec succès pour un nœud matériel avant de mettre à jour un autre nœud.

**3. Désactiver Docker**

Avant de mettre à jour le gestionnaire de paquets, assurez-vous que la socket Docker et le service dans SystemD sont arrêtés et désactivés. Par exemple :

```
systemctl disable docker.socket
systemctl stop docker.socket
systemctl disable docker.service
systemctl stop docker.service

```

**4. Mettre à niveau les paquets du système d'exploitation hôte**

Après avoir vérifié que la socket Docker et le service sont arrêtés, effectuez les mises à jour du gestionnaire de paquets :

```
dnf upgrade

```

**5. Déterminer le besoin de redémarrage**

Une fois le gestionnaire de paquets terminé, vérifiez si un redémarrage est nécessaire avec dnf-utils `needs-restarting` et le drapeau d'indice de redémarrage (-r) :

```
$ needs-restarting -r
Core libraries or services have been updated since boot-up:
  * kernel
  * systemd
Reboot is required to fully utilize these updates.
More information: https://access.redhat.com/solutions/27943
$


```

**6. Maintenance de Ceph**

_Cette étape est facultative et n'est requise que si le nœud doit être redémarré._

Avant le redémarrage, si le nœud fait partie du cluster Ceph, la suppression automatique de l'OSD et la rééquilibrage des données doivent être temporairement suspendues. Pour ce faire, effectuez :

```
ceph osd set noout
ceph osd set norebalance

```

Cela réduira le temps de reconstruction et aidera à garantir que le nœud rejoigne le cluster automatiquement.

Une fois le nœud redémarré et qu'un cluster Ceph sain est confirmé, ces paramètres doivent être désactivés. Pour désactiver cette configuration, effectuez :

```
ceph osd unset noout
ceph osd unset norebalance

```

### Redémarrer si nécessaire

Redémarrez le nœud si nécessaire :

```
shutdown -r now

```

Vous devrez peut-être attendre une minute ou deux avant de pouvoir vous reconnecter au nœud de plan de contrôle.

### Vérifier le redémarrage réussi

Lorsque le nœud revient en ligne, connectez-vous en SSH pour vérifier que les conteneurs Docker OpenStack ont démarré. De plus, si ce nœud faisait partie du cluster Ceph, vérifiez l'état du cluster Ceph.

Pour vérifier que les conteneurs Docker ont démarré, utilisez `docker ps`. Vous devriez voir un certain nombre de conteneurs Docker en cours d'exécution. Sous la colonne **STATUS**, chaque conteneur doit refléter le statut `Up`.

Par exemple :

```
[root@modest-galliform ~]# docker ps
CONTAINER ID   IMAGE                                                                        COMMAND                  CREATED        STATUS                          PORTS     NAMES
6f7590bc2191   harbor.imhadmin.net/kolla/centos-binary-telegraf:victoria                    "dumb-init --single-   "   20 hours ago   Restarting (1) 14 seconds ago             telegraf
67a4d47e8c78   harbor.imhadmin.net/kolla/centos-binary-watcher-api:victoria                 "dumb-init --single-   "   3 days ago     Up 6 minutes                              watcher_api
af815b1dcb5d   harbor.imhadmin.net/kolla/centos-binary-watcher-engine:victoria              "dumb-init --single-   "   3 days ago     Up 6 minutes                              watcher_engine
a52ab61933ac   harbor.imhadmin.net/kolla/centos-binary-watcher-applier:victoria             "dumb-init --single-   "   3 days ago     Up 6 minutes                              watcher_applier
[...output truncated...]

```

Ensuite, si ce nœud fait partie d'un cluster Ceph, vérifiez le statut de Ceph en utilisant `ceph status`.

Par exemple :

```
[root@modest-galliform ~]# ceph status
  cluster:
    id:     06bf4555-7c0c-4b96-a3b7-502bf8f6f213
    health: HEALTH_OK
[...output truncated...]

```

La sortie ci-dessus montre le statut comme `HEALTH_OK`, indiquant que le cluster Ceph est sain. Ceph est naturellement résilient et devrait se rétablir après le redémarrage d'un nœud.

# Voir l'utilisation des ressources de votre cloud privé

Maintenant, voyons comment trouver l'utilisation des ressources de votre cloud privé. Nous allons explorer comment utiliser le tableau de bord Horizon pour déterminer l'utilisation totale de la mémoire et du calcul pour un projet ainsi que comment voir les instances stockées sur chaque nœud. Ensuite, nous examinerons l'utilisation du disque en expliquant comment interagir brièvement avec le cluster Ceph de votre cloud en utilisant la ligne de commande. Enfin, nous passerons en revue l'ajout et la suppression de nœuds de votre cluster Ceph.

Il existe actuellement trois variations de déploiements de clouds privés : Petit, Standard et Grand. Tous les déploiements de clouds privés ont un cluster de trois serveurs hyper-convergés, mais auront des allocations différentes de mémoire, de stockage et de puissance de traitement CPU en fonction de la configuration et du matériel. De plus, vous avez la possibilité d'ajouter des nœuds matériels supplémentaires à votre cluster.

### Voir l'utilisation de la mémoire et du calcul dans Horizon

Pour voir les ressources utilisées par votre cloud, vous devez être l'utilisateur admin et assigné au projet admin. Une fois que vous êtes dans le projet admin, naviguez vers **Admin -> Calcul -> Hyperviseurs**. Cette section liste les éléments suivants :

* Utilisation des VCPU
* Utilisation de la mémoire
* Utilisation du disque local

### Voir l'état des instances dans le cluster

Il existe également une option pour voir l'emplacement de vos instances au sein de votre cluster. Pour voir ces informations, naviguez vers **Admin -> Calcul -> Instances**. Vous avez la possibilité de voir le projet, l'hôte, ainsi que l'adresse IP et l'état.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-156.png)
_Résumé des instances._

### Comment accéder aux informations sur les ressources de Ceph

Pour accéder aux informations concernant les pools de ressources de votre cluster Ceph, vous devrez utiliser l'interface de ligne de commande de Ceph. Voici un résumé de quelques commandes utiles de surveillance des ressources et de santé.

* `ceph -s` pour vérifier l'état de Ceph
* `ceph df` pour lister l'aperçu de l'utilisation du disque
* `ceph health detail` fournit des détails sur les problèmes de santé existants
* `ceph osd pool ls` pour lister les pools, ajoutez `detail` pour des détails supplémentaires concernant la réplication et les métriques de santé

### 

## Créer et restaurer des sauvegardes de volumes

Avec les clouds privés, vous avez la possibilité de créer des sauvegardes et des instantanés de vos données de volume. Si les données d'un volume sont corrompues ou supprimées par erreur, avoir une copie de ces données pourrait être inestimable. Maintenant, nous allons voir comment créer et restaurer des sauvegardes de volumes en utilisant Horizon.

Tout d'abord, rappelons ce qu'est un volume. Les volumes sont des dispositifs de stockage par blocs que vous attachez aux instances pour activer le stockage persistant. Vous pouvez attacher un volume à une instance en cours d'exécution ou détacher un volume et l'attacher à une autre instance à tout moment. Vous pouvez également créer un instantané à partir d'un volume ou le supprimer.

### Créer une sauvegarde de volume

Naviguez dans Horizon vers Projet -> Volume -> Volumes.

![Image](https://docs.flexmetal.net/wp-content/uploads/2022/01/jumpstation-volume-list.png)
_Liste des volumes_

Créez une sauvegarde de votre volume en sélectionnant dans le menu déroulant **Créer une sauvegarde**.

![Image](https://docs.flexmetal.net/wp-content/uploads/2021/09/create_volume_backup.png)
_Accéder au formulaire de création de sauvegarde de volume_

Vous devrez remplir les champs suivants.

* **Nom de la sauvegarde** : Spécifiez un nom pour la sauvegarde du volume
* **Description** : Fournissez une description si nécessaire
* **Nom du conteneur** : Laissez ce champ vide, sinon la sauvegarde du volume ne peut pas être créée. Horizon vous indique que si ce champ est vide, la sauvegarde est stockée dans un conteneur appelé `volumebackups`, mais ce n'est pas le cas avec notre configuration. Avec les clouds privés, toutes les sauvegardes de volumes créées de cette manière sont stockées dans le pool Ceph appelé `backups`.
* **Instantané de sauvegarde** : Si applicable, spécifiez un instantané pour créer une sauvegarde

Après avoir soumis le formulaire, vous êtes redirigé vers **Projet -> Volume -> Sauvegardes de volumes** où vous pouvez voir le volume dont vous venez de créer une sauvegarde.

![Image](https://docs.flexmetal.net/wp-content/uploads/2021/09/volume_backup_list.png)
_Liste des sauvegardes de volumes_

### Tester les sauvegardes de volumes

Créer des copies de sauvegarde de vos données importantes n'est qu'une partie d'un plan de sauvegarde et de récupération solide. De plus, envisagez de tester les données sauvegardées pour vous assurer que si quelque chose d'inattendu se produit, la restauration de vos sauvegardes sera réellement utile. Pour tester les sauvegardes de volumes, vous pouvez restaurer une sauvegarde de volume dans OpenStack aux côtés du volume original et comparer les contenus.

### Restaurer une sauvegarde de volume

Pour restaurer une sauvegarde de volume, commencez par naviguer dans Horizon vers **Projet -> Volume -> Sauvegardes de volumes**.

Ensuite, trouvez la sauvegarde de volume que vous souhaitez restaurer et, dans son menu déroulant à droite, sélectionnez **Restaurer la sauvegarde**.

![Image](https://docs.flexmetal.net/wp-content/uploads/2021/09/restore_volume_backup.png)
_Restaurer la sauvegarde de volume_

Choisissez le volume à restaurer, ou laissez le système restaurer la sauvegarde vers un nouveau volume.

### Ceph, Volumes et Durabilité des Données

Lorsque des sauvegardes de volumes sont créées, elles sont stockées dans le cluster Ceph de votre cloud dans un pool appelé backups. Par défaut, le cluster Ceph est configuré avec une réplication au niveau de l'hôte sur chacun des trois nœuds de plan de contrôle de votre cloud. Avec cette configuration, votre cloud pourrait subir la perte de tous les nœuds Ceph sauf un et conserver toutes les données du cluster.

## Conclusion

Vous devriez maintenant avoir une compréhension de base d'OpenStack et de certaines des choses que vous pouvez faire avec. Bonne chance pour la configuration de votre propre système OpenStack.

##