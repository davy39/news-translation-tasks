---
title: 'Démystifier les conteneurs 101 : Une plongée profonde dans la technologie
  des conteneurs pour débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T16:04:43.000Z'
originalURL: https://freecodecamp.org/news/demystifying-containers-101-a-deep-dive-into-container-technology-for-beginners-d7b60d8511c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zUYwSHCA2wFF8BW8E7D92w.png
tags:
- name: Computer Science
  slug: computer-science
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Démystifier les conteneurs 101 : Une plongée profonde dans la technologie
  des conteneurs pour débutants'
seo_desc: 'By Will Wang

  Introduction

  Regardless of whether you are a student in school, a developer at some company,
  or a software enthusiast, chances are you heard of containers. You may have also
  heard that containers are lightweight virtual machines, but wha...'
---

Par Will Wang

#### Introduction

Que vous soyez étudiant, développeur dans une entreprise ou passionné de logiciels, vous avez probablement entendu parler des _conteneurs_. Vous avez peut-être aussi entendu dire que les conteneurs sont des machines virtuelles légères, mais que signifie réellement cela, comment fonctionnent exactement les conteneurs et pourquoi sont-ils si importants ?

Cet article sert d'introduction aux conteneurs, à leurs grandes idées techniques clés et à leurs applications. Je ne supposerai aucune connaissance préalable dans ce domaine, autre qu'une compréhension de base de l'informatique.

### Le Noyau et le Système d'Exploitation

Votre ordinateur portable, comme tous les autres ordinateurs, est construit sur des composants matériels tels que le CPU, le stockage persistant (disque dur, SSD), la mémoire, la carte réseau, etc.

Pour interagir avec ce matériel, un logiciel du système d'exploitation appelé _noyau_ sert de pont entre le matériel et le reste du système. Le noyau est responsable de la planification des _processus_ (programmes) à exécuter, de la gestion des périphériques (lecture et écriture d'adresses sur le disque et la mémoire), et plus encore.

Le reste du système d'exploitation sert à démarrer et à gérer l'espace utilisateur, où les processus utilisateur sont exécutés, et interagira constamment avec le noyau.

![Image](https://cdn-media-1.freecodecamp.org/images/Dzj8uEQcg0VLXopQWmspJ3esROkT7vVRTB-r)
_Le noyau fait partie du système d'exploitation et interface avec le matériel. Le système d'exploitation dans son ensemble vit dans l'« espace noyau » tandis que les programmes utilisateur vivent dans l'« espace utilisateur ». L'espace noyau est responsable de la gestion de l'espace utilisateur._

### La Machine Virtuelle

Ainsi, vous avez un ordinateur qui exécute MacOS et une application conçue pour fonctionner sur Ubuntu. Hmmm... Une solution courante consiste à démarrer une machine virtuelle sur votre ordinateur MacOS qui exécute Ubuntu, puis à y exécuter votre programme.

Une _machine virtuelle_ est composée d'un certain niveau de virtualisation du matériel et du noyau sur lequel fonctionne un système d'exploitation invité. Un logiciel appelé _hyperviseur_ crée le matériel virtualisé qui peut inclure le disque virtuel, l'interface réseau virtuelle, le CPU virtuel, et plus encore. Les machines virtuelles incluent également un noyau invité qui peut communiquer avec ce matériel virtuel.

L'hyperviseur peut être hébergé, ce qui signifie qu'il s'agit d'un logiciel qui s'exécute sur le système d'exploitation hôte (MacOS) comme dans l'exemple. Il peut également être bare metal, s'exécutant directement sur le matériel de la machine (remplaçant votre système d'exploitation). Dans les deux cas, l'approche de l'hyperviseur est considérée comme lourde car elle nécessite la virtualisation de plusieurs parties, sinon de la totalité du matériel et du noyau.

Lorsque plusieurs groupes isolés doivent coexister sur la même machine, l'exécution d'une machine virtuelle pour chacun de ces groupes est trop lourde et gaspille des ressources pour être une bonne approche.

![Image](https://cdn-media-1.freecodecamp.org/images/y4w7Yvlj0aGyKUDYWnFJLf8jfyUkyKgVfGDN)
_Surcharge non à l'échelle._

Les machines virtuelles nécessitent une virtualisation matérielle pour l'isolement au niveau de la machine, tandis que les conteneurs fonctionnent sur l'isolement au sein du même système d'exploitation. La différence de surcharge devient vraiment apparente à mesure que le nombre d'espaces isolés augmente. Un ordinateur portable régulier peut exécuter des dizaines de conteneurs mais peut avoir du mal à exécuter même une seule machine virtuelle correctement.

### cgroups

En 2006, des ingénieurs de Google ont inventé les "groupes de contrôle" Linux, abrégés en _cgroups_. Il s'agit d'une fonctionnalité du noyau Linux qui isole et contrôle l'utilisation des ressources pour les processus utilisateur.

Ces processus peuvent être placés dans des _espaces de noms_, essentiellement des collections de processus qui partagent les mêmes limitations de ressources. Un ordinateur peut avoir plusieurs espaces de noms, chacun avec les propriétés de ressources appliquées par le noyau.

L'allocation des ressources par espace de noms peut être gérée afin de limiter la quantité globale de CPU, de RAM, etc., qu'un ensemble de processus peut utiliser. Par exemple, une application d'agrégation de logs en arrière-plan devra probablement avoir ses ressources limitées afin de ne pas submerger accidentellement le serveur réel qu'elle journalise.

Bien que ce ne soit pas une fonctionnalité originale, les cgroups dans Linux ont finalement été retravaillés pour inclure une fonctionnalité appelée _isolement des espaces de noms_. L'idée de l'isolement des espaces de noms n'est pas nouvelle, et Linux avait déjà de nombreux types d'isolement des espaces de noms. Un exemple courant est l'isolement des processus, qui sépare chaque processus individuel et empêche des choses comme la mémoire partagée.

L'isolement des cgroups est un niveau d'isolement plus élevé qui garantit que les processus au sein d'un espace de noms cgroup sont indépendants des processus dans d'autres espaces de noms. Quelques fonctionnalités importantes d'isolement des espaces de noms sont décrites ci-dessous et pavent la voie à l'isolement que nous attendons des conteneurs.

* Espaces de noms PID (Identifiant de Processus) : cela garantit que les processus au sein d'un espace de noms ne sont pas conscients des processus dans d'autres espaces de noms.
* Espaces de noms Réseau : Isolement du contrôleur d'interface réseau, des iptables, des tables de routage et d'autres outils de réseau de bas niveau.
* Espaces de noms de Montage : Les systèmes de fichiers sont montés, de sorte que la portée du système de fichiers d'un espace de noms est limitée aux seuls répertoires montés.
* Espaces de noms Utilisateur : Limite les utilisateurs au sein d'un espace de noms à cet espace de noms uniquement et évite les conflits d'ID utilisateur entre les espaces de noms.

En résumé, chaque espace de noms apparaîtrait comme sa propre machine pour les processus qui s'y trouvent.

### Conteneurs Linux

Les cgroups Linux ont ouvert la voie à une technologie appelée _conteneurs Linux_ (LXC). LXC était vraiment la première implémentation majeure de ce que nous connaissons aujourd'hui sous le nom de conteneur, tirant parti des cgroups et de l'isolement des espaces de noms pour créer un environnement virtuel avec un espace de processus et de réseau séparé.

En un sens, cela permet des espaces utilisateur indépendants et isolés. L'idée des _conteneurs_ découle directement de LXC. En fait, les premières versions de Docker étaient construites directement sur LXC.

#### Docker

Docker est la technologie de conteneurs la plus largement utilisée et vraiment ce que la plupart des gens entendent par conteneurs. Bien qu'il existe d'autres technologies de conteneurs open source (comme [rkt](https://github.com/rkt/rkt) de CoreOS) et de grandes entreprises qui construisent leur propre moteur de conteneurs (comme [lmctfy](https://github.com/google/lmctfy) chez Google), Docker est devenu la norme industrielle pour la conteneurisation. Il est toujours construit sur les cgroups et les espaces de noms fournis par le noyau Linux et récemment Windows également.

![Image](https://cdn-media-1.freecodecamp.org/images/7UNkwjdO9OZbH2zJyzwhVS5cncW1TsKHea2t)
_Source de l'image : Docker_

Un conteneur Docker est composé de couches d'_images_, des binaires regroupés en un seul package. L'image de base contient le système d'exploitation du conteneur, qui peut être différent du système d'exploitation de l'hôte.

Le système d'exploitation du conteneur est sous forme d'image. Ce n'est pas le système d'exploitation complet comme sur l'hôte, et la différence est que l'image est simplement le système de fichiers et les binaires pour le système d'exploitation, tandis que le système d'exploitation complet inclut le système de fichiers, les binaires et le noyau.

Au-dessus de l'image de base se trouvent plusieurs images qui construisent chacune une partie du conteneur. Par exemple, au-dessus de l'image de base peut se trouver l'image qui contient les dépendances `apt-get`. Au-dessus de celle-ci peut se trouver l'image qui contient le binaire de l'application, et ainsi de suite.

La partie intéressante est que si vous avez deux conteneurs avec les couches d'images `a, b, c` et `a, b, d`, alors vous n'avez besoin de stocker qu'une seule copie de chaque couche d'image `a, b, c, d` à la fois localement et dans le dépôt. Il s'agit du _système de fichiers union_ de Docker.

![Image](https://cdn-media-1.freecodecamp.org/images/r6qYZxeT3GRKYh1BeueAWaQ1YJiCGGQHGJ-5)

Chaque image, identifiée par un hachage, n'est qu'une des nombreuses couches d'images possibles qui composent un conteneur. Cependant, un conteneur est identifié uniquement par son image de niveau supérieur, qui contient des références aux images parent. Deux images de niveau supérieur (Image 1 et Image 2) présentées ici partagent les trois premières couches. L'Image 2 a deux couches de configuration supplémentaires, mais partage les mêmes images parent que l'Image 1.

Lorsqu'un conteneur est démarré, l'image et ses images parent sont téléchargées depuis le dépôt, les cgroups et les espaces de noms sont créés, et l'image est utilisée pour créer un environnement virtuel. Depuis l'intérieur du conteneur, les fichiers et les binaires spécifiés dans l'image semblent être les seuls fichiers de toute la machine. Ensuite, le processus principal du conteneur est démarré et le conteneur est considéré comme actif.

Docker possède quelques autres fonctionnalités vraiment intéressantes, telles que la copie à l'écriture, les volumes (systèmes de fichiers partagés entre les conteneurs), le démon Docker (gère les conteneurs sur une machine), les dépôts contrôlés par version (comme Github pour les conteneurs), et plus encore. Pour en savoir plus sur ces fonctionnalités et voir quelques exemples pratiques de l'utilisation de Docker, cet [article](https://medium.freecodecamp.org/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b) est extrêmement utile.

![Image](https://cdn-media-1.freecodecamp.org/images/pKupNiDXvO5DNVaBiaxQ3In3DuPX3heDIrA5)
_Un client en ligne de commande (1) indique à un processus sur la machine appelé le démon Docker (2) quoi faire. Le démon récupère les images depuis un registre/dépôt (3). Ces images sont mises en cache (4) sur la machine locale et peuvent être démarrées par le démon pour exécuter des conteneurs (5). Source de l'image : Docker_

### Pourquoi les Conteneurs

Outre l'isolement des processus, les conteneurs ont de nombreuses autres propriétés bénéfiques.

Le conteneur sert d'unité auto-isolée qui peut s'exécuter n'importe où où il est supporté. Et dans chacune de ces instances, le conteneur lui-même sera exactement identique. Peu importe que le système d'exploitation hôte soit CentOS, Ubuntu, MacOS, ou même quelque chose de non UNIX comme Windows — depuis l'intérieur du conteneur, le système d'exploitation sera celui spécifié par le conteneur. Ainsi, vous pouvez être sûr que le conteneur que vous avez construit sur votre ordinateur portable s'exécutera également sur les serveurs de l'entreprise.

Le conteneur agit également comme une unité standardisée de travail ou de calcul. Un paradigme courant est que chaque conteneur exécute un seul serveur web, un seul fragment d'une base de données, ou un seul travailleur Spark, etc. Ensuite, pour mettre à l'échelle une application, vous devez simplement mettre à l'échelle le nombre de conteneurs.

Dans ce paradigme, chaque conteneur se voit attribuer une configuration de ressources fixe (CPU, RAM, nombre de threads, etc.) et la mise à l'échelle de l'application nécessite la mise à l'échelle uniquement du nombre de conteneurs au lieu des primitives de ressources individuelles. Cela fournit une abstraction beaucoup plus facile pour les ingénieurs lorsque les applications doivent être mises à l'échelle.

Les conteneurs servent également d'excellent outil pour implémenter l'_architecture de microservices_, où chaque microservice est simplement un ensemble de conteneurs coopérants. Par exemple, le microservice Redis peut être implémenté avec un seul conteneur principal et plusieurs conteneurs réplicas.

Cette architecture orientée (micro)services possède certaines propriétés très importantes qui facilitent la création et le déploiement d'applications par les équipes d'ingénierie (voir mon [article précédent](https://hackernoon.com/how-microservices-saved-the-internet-30cd4b9c6230) pour plus de détails).

### Orchestration

Depuis l'époque des conteneurs Linux, les utilisateurs ont tenté de déployer des applications à grande échelle sur de nombreuses machines virtuelles où chaque processus s'exécute dans son propre conteneur. Pour ce faire, il était nécessaire de pouvoir déployer efficacement des dizaines à des milliers de conteneurs sur potentiellement des centaines de machines virtuelles et de gérer leur réseau, leurs systèmes de fichiers, leurs ressources, etc. Docker facilite aujourd'hui un peu cela en exposant des abstractions pour définir le réseau des conteneurs, les volumes pour les systèmes de fichiers, les configurations de ressources, etc.

Cependant, un outil est toujours nécessaire pour :

* prendre une spécification et attribuer des conteneurs à des machines (planification)
* démarrer effectivement les conteneurs spécifiés sur les machines via Docker
* gérer les mises à jour/retours en arrière/la nature constamment changeante du système
* répondre aux défaillances comme les plantages de conteneurs
* et créer des ressources de cluster comme la découverte de services, le réseau inter-machines virtuelles, l'entrée/sortie du cluster, etc.

Cet ensemble de problèmes concerne l'_orchestration_ d'un système distribué construit sur un ensemble de conteneurs (éventuellement transitoires ou constamment changeants), et les gens ont construit des systèmes vraiment miraculeux pour résoudre ce problème.

Dans mon prochain article, je parlerai en profondeur de l'implémentation de Kubernetes, le principal orchestrateur open source, ainsi que de deux autres tout aussi importants mais moins connus, Mesos et Borg.

Cet article fait partie d'une série. Je suis étudiant de premier cycle à l'UC Berkeley. Mes recherches portent sur les systèmes distribués et je suis conseillé par Scott Shenker.

> Précédent : [Comment les Microservices ont Sauvé Internet](https://hackernoon.com/how-microservices-saved-the-internet-30cd4b9c6230)

> Suivant : Orchestration (À venir)