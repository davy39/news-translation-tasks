---
title: Comment fonctionnent les conteneurs Docker – Explications pour débutants
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-10-23T16:45:13.000Z'
originalURL: https://freecodecamp.org/news/how-docker-containers-work
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/cover-final.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
- name: virtual machine
  slug: virtual-machine
- name: virtualization
  slug: virtualization
seo_title: Comment fonctionnent les conteneurs Docker – Explications pour débutants
seo_desc: 'A container is a lightweight, standalone, and executable software package
  that includes everything needed to run a piece of software.

  And one of the most popular tools for working with containers is Docker.

  Docker is both the name of the company (Doc...'
---

Un conteneur est un package logiciel léger, autonome et exécutable qui inclut tout ce qui est nécessaire pour exécuter un logiciel.

Et l'un des outils les plus populaires pour travailler avec des conteneurs est Docker.

Docker est à la fois le nom de l'entreprise (Docker Inc) et le nom du logiciel qu'ils ont créé pour packager des logiciels dans des conteneurs.

Pour comprendre comment fonctionnent les conteneurs et pourquoi ils sont incroyablement utiles pour le développement logiciel, vous devez comprendre deux sujets apparemment sans rapport : les conteneurs de transport et les machines virtuelles.

## Une brève histoire des conteneurs de transport

"The Box: How the Shipping Container Made the World Smaller and the World Economy Bigger" est un livre de [Marc Levinson](https://www.amazon.co.uk/Box-Shipping-Container-Smaller-Economy/dp/0691170819/ref=sr_1_1?crid=14VL4VEQHDVNL&keywords=the+box+book&qid=1694037660&sprefix=the+box+book%2Caps%2C97&sr=8-1). Il explore l'impact profond des conteneurs de transport sur le commerce mondial et l'économie mondiale.

Bien que l'histoire des conteneurs de transport puisse sembler sans rapport dans une discussion sur les conteneurs Docker, ils ont plus en commun que vous ne le pensez.

Avant les conteneurs de transport, la manutention des marchandises était intensive en main-d'œuvre et chronophage, entraînant des inefficacités et des retards dans le commerce mondial. Les marchandises arrivaient sous diverses formes et tailles, et l'absence d'emballage standardisé rendait difficile l'empilage et la sécurisation des articles de manière efficace.

Sans conteneurs standardisés, les marchandises étaient souvent stockées de manière désordonnée dans les cales des navires ou dans les docks. Cette utilisation inefficace de l'espace signifiait que les navires ne transportaient pas autant de marchandises qu'ils auraient pu potentiellement contenir, entraînant des coûts de transport plus élevés.

L'adoption de dimensions et de procédures de manutention uniformes a permis un transfert transparent des marchandises entre différents modes de transport : navires, camions, trains et les grues utilisées pour déplacer les conteneurs.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ac7826e-ebd0-4062-8f49-d48a6f9ef9ce_1886x946.png align="left")

*Image montrant comment les tailles standardisées des conteneurs permettent de les déplacer facilement entre les navires, les trains et les camions.*

Cette standardisation a été la clé du succès des conteneurs de transport. Après tout, si les conteneurs d'une entreprise ne s'adaptaient pas aux navires, camions ou trains de marchandises d'une autre entreprise, ils ne pouvaient pas être transportés correctement. Chaque entreprise aurait besoin de sa propre flotte de conteneurs pour pouvoir envoyer des choses à chacun de ses clients – ce qui serait un cauchemar opérationnel.

La standardisation des conteneurs de transport les rend portables, c'est-à-dire faciles à déplacer d'un endroit à un autre. Cette portabilité est également une caractéristique clé des conteneurs Docker, comme nous le discuterons bientôt.

## Qu'est-ce que les machines virtuelles ?

Les machines virtuelles (VM) sont créées grâce à un processus appelé virtualisation.

La virtualisation est une technologie qui permet de créer plusieurs environnements simulés ou versions virtuelles de quelque chose, comme un système d'exploitation, un serveur, un stockage ou un réseau, sur une seule machine physique.

Ces environnements virtuels se comportent comme s'ils étaient des entités indépendantes et séparées, même s'ils partagent les ressources du système physique sous-jacent.

La virtualisation est comme avoir un chapeau de magicien qui peut faire apparaître plusieurs chapeaux à l'intérieur. Tout comme le chapeau du magicien crée l'illusion de nombreux chapeaux apparaissant à partir d'un seul chapeau physique, la virtualisation permet à un seul ordinateur ou serveur physique d'apparaître comme plusieurs machines virtuelles (VM), chacune avec son propre système d'exploitation et ses ressources.

Les VM virtualisent le matériel. Cela signifie simplement qu'une VM prend un seul morceau de matériel – un serveur – et crée des versions virtuelles d'autres serveurs exécutant leurs propres systèmes d'exploitation. Physiquement, ce n'est qu'un seul morceau de matériel.

Logiquement, plusieurs machines virtuelles peuvent fonctionner sur un seul morceau de matériel. Cela revient essentiellement à un ou plusieurs ordinateurs fonctionnant à l'intérieur d'un ordinateur, comme illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9733d44-d0c7-49e6-8978-da253cf9c3a9_1650x966.png align="left")

*Image montrant comment la virtualisation crée plusieurs machines virtuelles (VM) à partir d'un seul serveur physique*

### Comment fonctionne la virtualisation ?

Vous vous demandez peut-être comment fonctionne exactement la virtualisation ? Jetez un coup d'œil à l'image ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3cd74b32-e3d1-430f-bbd6-e0daf2150b82_1084x576.png align="left")

*Image montrant comment la virtualisation fonctionne en virtualisant un seul morceau de matériel pour créer plusieurs machines virtuelles*

À la base, vous avez le matériel et le système d'exploitation hôte. Il s'agit de la machine physique utilisée pour créer les machines virtuelles. Par-dessus, vous avez l'hyperviseur. Cela permet à plusieurs machines virtuelles, chacune avec son propre système d'exploitation (OS), de fonctionner sur un seul serveur physique.

Les VM ont cependant quelques inconvénients, que les conteneurs adressent. Deux inconvénients se distinguent particulièrement :

1. Les VM consomment plus de ressources : Les VM ont une surcharge de ressources plus élevée en raison de la nécessité d'exécuter une instance complète de système d'exploitation pour chaque VM. Cela peut entraîner une consommation accrue de mémoire et de stockage. Cela peut à son tour avoir un effet négatif sur les performances et les temps de démarrage de la machine virtuelle.

2. Portabilité : Les VM sont généralement moins portables en raison des différences dans les environnements de système d'exploitation sous-jacents. Le déplacement de VM entre différents hyperviseurs ou fournisseurs de cloud peut être plus complexe.

Les principaux fournisseurs de cloud ont tous des VM. Pour AWS, c'est EC2, GCP a Compute Engine, et Azure a Azure Virtual Machines.

## Qu'est-ce que les conteneurs ?

Un conteneur est un package logiciel léger, autonome et exécutable qui inclut tout ce qui est nécessaire pour exécuter un logiciel, y compris le code, le runtime, les outils système et les bibliothèques.

Les conteneurs sont conçus pour isoler les applications et leurs dépendances, garantissant qu'ils peuvent fonctionner de manière cohérente dans différents environnements. Que l'application s'exécute depuis votre ordinateur ou dans le cloud, le comportement de l'application reste le même.

Contrairement aux VM qui virtualisent le matériel, [les conteneurs virtualisent le système d'exploitation](https://aws.amazon.com/compare/the-difference-between-containers-and-virtual-machines/#:~:text=Containers%20virtualize%20the%20operating%20system,use%20your%20hardware%20resources%20efficiently.). Cela signifie simplement qu'un conteneur utilise un seul système d'exploitation pour créer une application virtuelle et ses bibliothèques. Les conteneurs s'exécutent sur un système d'exploitation partagé fourni par le système hôte.

Cela est illustré ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55e6ff35-1917-4374-8006-80aa8668a772_1160x470.png align="left")

*Image montrant comment les conteneurs fonctionnent en virtualisant le système d'exploitation*

Le moteur de conteneur vous permet de lancer des conteneurs. Il fournit les outils et services nécessaires pour construire, exécuter et déployer des applications conteneurisées.

Les conteneurs présentent plusieurs avantages :

1. **Portabilité** : Les conteneurs sont conçus pour être indépendants de la plateforme. Ils peuvent s'exécuter sur n'importe quel système prenant en charge le runtime de conteneur, tel que Docker, indépendamment du système d'exploitation sous-jacent. Cela facilite le déplacement des applications entre différents environnements, y compris les machines de développement locales, les serveurs de test et les différentes plateformes cloud.

2. **Efficacité** : Les conteneurs partagent le système d'exploitation du système hôte, ce qui réduit la surcharge de l'exécution d'une machine virtuelle avec plusieurs systèmes d'exploitation. Cela conduit à une utilisation plus efficace des ressources et permet une densité plus élevée d'applications pouvant s'exécuter sur un seul hôte.

3. **Cohérence** : Les conteneurs regroupent tous les composants nécessaires, y compris le code de l'application, le runtime, les bibliothèques et les dépendances, en une seule unité. Cela élimine le problème "ça marche sur ma machine" et garantit que l'application s'exécute de manière cohérente dans différents environnements, du développement à la production.

4. **Isolation** : Les conteneurs fournissent un environnement léger et isolé pour l'exécution des applications. Chaque conteneur encapsule l'application et ses dépendances, garantissant qu'ils n'interfèrent pas les uns avec les autres. Cette isolation aide à prévenir les conflits et garantit un comportement cohérent dans différents environnements.

5. **Déploiement rapide** : Les conteneurs peuvent être créés et démarrés rapidement, souvent en quelques secondes. Cette vitesse de déploiement rapide est particulièrement bénéfique pour les applications qui doivent rapidement monter ou descendre en charge en fonction de la demande.

## Qu'est-ce que Docker ?

Maintenant que nous avons couvert les VM et les conteneurs, qu'est-ce que Docker exactement ? Docker est simplement un outil pour créer et gérer des conteneurs.

Au cœur de Docker, il y a deux concepts utiles à comprendre : le Dockerfile et les images Docker.

Un Dockerfile contient l'ensemble des instructions pour construire une image Docker.

Une image Docker sert de modèle pour créer des conteneurs Docker. Elle contient tout le code nécessaire, le runtime, les outils système, les bibliothèques et les paramètres requis pour exécuter une application logicielle.

Ainsi, un Dockerfile est utilisé pour construire une image Docker qui est ensuite utilisée comme modèle pour créer un ou plusieurs conteneurs Docker. Cela est illustré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f5a703a-0a08-48a0-be54-46ca4a29a9dc_1974x534.png align="left")

*Image montrant les étapes pour créer un conteneur Docker. D'abord, vous créez le Dockerfile qui est utilisé pour construire l'image Docker qui est finalement utilisée pour exécuter un conteneur Docker*

Si cette explication vous fait encore gratter la tête, considérons l'analogie suivante en utilisant des conteneurs de transport.

Imaginez que vous devez construire plusieurs conteneurs de transport pour transporter des articles dans le monde entier. Vous commencez par un document listant les exigences pour votre conteneur de transport. Cela contiendra des informations comme les dimensions du conteneur, le type de joints, les mécanismes de verrouillage des portes, les exigences de ventilation et de réfrigération (si vous transportez des aliments nécessitant un environnement à température contrôlée, par exemple), et ainsi de suite.

Ce document d'exigences sera ensuite utilisé pour créer un modèle détaillé pour le conteneur qui inclura des dessins techniques montrant les dimensions et autres spécifications.

À partir de ce modèle, les conteneurs physiques seront ensuite construits. Ce seul modèle peut être utilisé pour construire un ou plusieurs conteneurs physiques qui seront tous identiques et correspondront aux spécifications du modèle de conteneur.

Cela est illustré ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa1ac249-4fd1-49f2-8b7b-e52914017f89_1944x830.png align="left")

*Image montrant une analogie de conteneur de transport pour les conteneurs Docker*

Le Dockerfile est analogue au document d'exigences, qui contient simplement un ensemble d'instructions pour construire le modèle de conteneur.

L'image Docker est analogue au modèle de conteneur, qui détaille toutes les instructions nécessaires pour construire le conteneur physique.

Une fois créées, les images Docker sont immuables, ce qui signifie qu'elles ne peuvent pas être modifiées. Si vous devez apporter des modifications à une application, vous devez modifier le Dockerfile et créer une nouvelle image. Cette immuabilité garantit la cohérence et la reproductibilité dans le déploiement des applications.

Et enfin, le conteneur Docker est analogue au conteneur de transport physique.

## Mettre tout cela ensemble

En résumé, les conteneurs offrent un moyen **portable** et **efficace** de packager des applications et leurs dépendances, garantissant la cohérence dans divers environnements. Les avantages qu'ils apportent au développement logiciel sont similaires aux avantages apportés à l'économie mondiale par le modeste conteneur de transport.

### Portabilité

Les conteneurs de transport, grâce à la standardisation, garantissent que n'importe quel conteneur, n'importe où dans le monde, peut être utilisé de manière transparente pour déplacer des articles à travers divers modes de transport : navires, camions, trains et les grues utilisées pour les charger et les décharger de différentes formes de transport.

De même, les conteneurs Docker permettent la portabilité. Ils garantissent que les applications peuvent s'exécuter de manière cohérente dans différents environnements, des ordinateurs portables de développement aux serveurs de production, et à travers différents fournisseurs de cloud.

### Efficacité accrue

Avec des tailles de conteneurs standard, la densité de chargement des marchandises que vous pouvez déplacer augmente. Maintenant, vous pouvez entasser plus de choses dans un seul conteneur de transport, comparé aux jours avant l'existence des conteneurs de transport où vous aviez des marchandises de formes et de tailles non standard stockées de manière désordonnée dans les cales des navires ou sur les docks. Ainsi, chaque navire, train de marchandises ou camion peut transporter plus de marchandises à chaque voyage, rendant le transport de marchandises autour du monde moins cher.

Avec les conteneurs Docker, une meilleure efficacité provient du fait que les conteneurs partagent le système d'exploitation hôte, les rendant légers par rapport aux VM. Cela conduit à des temps de démarrage rapides des conteneurs et à une utilisation moindre du CPU, de la mémoire et du stockage.

Une utilisation moindre des ressources signifie également que les conteneurs peuvent augmenter la densité des applications par rapport aux VM. Avec les conteneurs, vous pouvez exécuter plus d'applications sur le même matériel sans une baisse significative des performances.

Pour conclure, le conteneur de transport en lui-même n'est pas magique. Après tout, ce n'est qu'une boîte en métal. C'est la standardisation des conteneurs de transport qui les a rendus portables et un moyen bon marché et efficace de déplacer des marchandises autour du monde.

Dans le développement d'applications, les conteneurs bénéficient de la standardisation de la même manière. Les conteneurs offrent un moyen portable et efficace de packager des applications et leurs dépendances, garantissant la cohérence dans divers environnements.