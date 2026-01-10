---
title: Options de stockage cloud – Stockage par blocs vs stockage de fichiers vs stockage
  d'objets expliqués
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-07-26T17:10:33.000Z'
originalURL: https://freecodecamp.org/news/cloud-storage-options
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pictures.001.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: storage
  slug: storage
seo_title: Options de stockage cloud – Stockage par blocs vs stockage de fichiers
  vs stockage d'objets expliqués
seo_desc: 'There are three types of storage options offered by most cloud providers:
  block storage, file storage, and object storage (often referred to as BLOB or Binary
  Large Object).

  This tutorial will explain these types of storage, their real-world use case...'
---

Il existe trois types d'options de stockage offertes par la plupart des fournisseurs de cloud : le stockage par blocs, le stockage de fichiers et le stockage d'objets (souvent appelé BLOB ou Binary Large Object).

Ce tutoriel expliquera ces types de stockage, leurs cas d'utilisation réels et certains compromis.

## Qu'est-ce que le stockage par blocs ?

Imaginez que vous avez une grande bibliothèque avec de nombreuses étagères, et chaque étagère peut contenir un nombre spécifique de pages d'un livre.

Maintenant, supposons que vous avez une collection de livres, mais ils sont tous de tailles différentes. Pour stocker ces livres efficacement, vous décidez de les diviser en plus petits morceaux uniformes, appelés blocs, qui s'adaptent parfaitement sur les étagères.

Chaque étagère ne peut stocker que 100 pages d'un livre. Gatsby le Magnifique compte environ 200 pages, donc chaque étagère ne peut stocker que la moitié du livre. Par conséquent, ce seul livre sera stocké dans deux étagères séparées comme montré ci-dessous, avec la moitié du livre à un endroit et l'autre moitié à un autre endroit.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89b745ba-7f4a-4bbd-9a66-08a2670319f4_1798x962.png align="left")

Nous avons défini un bloc comme le nombre maximum de pages qui peuvent être stockées dans une étagère. Dans cet exemple, la taille du bloc est de 100 pages.

Avec le stockage par blocs, les données sont divisées en blocs de taille fixe, tout comme les pages d'un livre dans notre analogie. Ces blocs font généralement plusieurs milliers d'octets.

Chaque bloc se voit attribuer une adresse unique, similaire à l'emplacement d'un livre spécifique (ou des pages d'un livre) sur une étagère. Ces adresses vous permettent de trouver et d'accéder rapidement à des blocs de données individuels sans avoir à parcourir l'ensemble du stockage.

Lorsque vous souhaitez stocker ou récupérer des données en utilisant le stockage par blocs, vous interagissez directement avec les blocs. Vous pouvez écrire de nouvelles données dans un bloc vide ou écraser des données existantes dans un bloc. Si vous devez récupérer des informations spécifiques, vous pouvez demander le bloc par son adresse unique, et il vous sera retourné.

Les disques durs (HDD) et les disques à semi-conducteurs (SSD) qui sont attachés physiquement à un ordinateur ou via un réseau sont des exemples de dispositifs de stockage par blocs.

Les principaux fournisseurs de cloud ont tous des options de stockage par blocs :

1. AWS – Elastic Block Storage (EBS)
   
2. GCP – Persistent Disks
   
3. Azure – Managed Disks

Les dispositifs de stockage par blocs sont généralement attachés à une seule instance. C'est l'une des façons dont le stockage par blocs diffère du stockage de fichiers, que je vais expliquer dans la section suivante.

Le stockage par blocs physiquement attaché n'est pas persistant, ce qui signifie qu'il ne dure que tant que l'instance n'est pas terminée. Le stockage par blocs attaché en réseau persiste au-delà de la durée de vie de l'instance.

En revenant à l'analogie du stockage d'un nombre fixe de pages d'un livre dans une bibliothèque, le stockage par blocs vous permettra de modifier ou de récupérer des pages spécifiques sans avoir à manipuler le livre entier.

Cependant, pourquoi auriez-vous jamais besoin de faire cela ? N'est-il pas préférable que les étagères stockent simplement un livre dans son intégralité ?

Pour les humains, c'est certainement préféré. Pour les ordinateurs, le stockage d'informations en blocs présente certains avantages.

Puisque le stockage par blocs présente des blocs bruts à l'instance de calcul, l'instance a la flexibilité de gérer les blocs. Cela est idéal pour les applications qui nécessitent des performances élevées et un stockage à faible latence comme les bases de données, les applications de calcul haute performance et l'ETL (Extract Transform Load), parmi d'autres applications.

Les dispositifs de stockage par blocs sont également utilisés pour stocker le système d'exploitation. Ils sont également bootables. « Bootable » fait simplement référence à la capacité d'un dispositif à démarrer ou à initier le processus de chargement d'un système d'exploitation ou d'un programme logiciel lorsque l'ordinateur est mis sous tension ou redémarré.

Un dispositif bootable contient les fichiers et données nécessaires qui permettent à un ordinateur de commencer sa séquence de démarrage et de charger le système d'exploitation dans la mémoire de l'ordinateur.

## Qu'est-ce que le stockage de fichiers ?

Le stockage par blocs est l'abstraction de stockage de plus bas niveau. Il fournit une interface de bas niveau où vous pouvez lire ou écrire dans des blocs de données individuels. Mais il ne comprend pas intrinsèquement le concept de fichiers, de répertoires ou de la structure hiérarchique généralement associée aux systèmes de fichiers.

Le stockage de fichiers est une abstraction construite sur le stockage par blocs. Il introduit le concept de fichiers, de répertoires et d'une structure hiérarchique pour organiser et gérer les données.

Avec le stockage de fichiers, vous pouvez regrouper des blocs de données apparentés pour former des fichiers et organiser les fichiers dans des répertoires. Cela permet une manière plus intuitive d'accéder et de gérer les données, car vous pouvez travailler avec des fichiers et des répertoires plutôt que de traiter avec des blocs individuels.

En utilisant notre analogie de bibliothèque, avec le stockage de fichiers, tout ce avec quoi vous interagissez sont des fichiers et leurs hiérarchies, tout comme une librairie peut organiser ses livres de manière structurée pour faciliter la recherche et la consultation des sélections par les clients. Les livres peuvent être rangés par ordre alphabétique selon le nom de l'auteur, par genre, ou une combinaison des deux comme montré ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1bea5d8-3368-4809-bb46-d520357c6934_1406x1014.png align="left")

Les livres peuvent également être organisés par sous-genres (science-fiction, fantastique, mystère, etc.), best-sellers, nouvelles parutions, livres en promotion, recommandations du personnel et livres pour enfants.

De même, avec le stockage de fichiers, vous avez la flexibilité de la structure hiérarchique, ce qui facilite l'accès aux données pour les utilisateurs (humains ou autres applications).

Cette structure de fichiers hiérarchique n'est qu'une [abstraction](https://lightcloud.substack.com/p/cloud-computing-abstractions-explained). En coulisses, le système d'exploitation abstrait le stockage par blocs sous-jacent et donne plutôt l'apparence d'un classeur avec une structure de type dossier. Cela simplifie l'accès aux applications qui tentent de lire ou d'écrire des fichiers sur le disque.

Les applications n'ont pas besoin de connaître l'adresse de bloc sous-jacente pour récupérer les fichiers, ce qui facilite l'interaction de l'application avec les fichiers. Cette facilité d'interaction a un coût de performance, qui est acceptable pour certains cas d'utilisation.

Les principaux fournisseurs de cloud ont tous des options de stockage de fichiers :

1. AWS – Elastic File Storage (EFS)
   
2. GCP – Cloud Filestore
   
3. Azure – Azure Files

Contrairement au stockage par blocs, **plusieurs instances de calcul peuvent être montées sur le même dispositif de stockage de fichiers.**

## Qu'est-ce que le stockage d'objets ?

Il s'agit de la forme de stockage la plus récente dans le cloud. Le stockage d'objets stocke toutes les données sous forme d'objets dans une structure plate. Il n'y a pas de hiérarchie, contrairement au stockage de fichiers. Mais une hiérarchie artificielle de type dossier est impartie au stockage par blocs pour lui donner l'apparence d'avoir une structure.

Le stockage d'objets est hautement scalable. Il peut stocker plusieurs milliards d'objets. En 2009, il stockait [82 milliards d'objets](https://www.allthingsdistributed.com/2009/11/82_billion_objects_in_amazon_s.html). Il ne serait pas surprenant que ce nombre ait dépassé les billions d'objets à ce jour en 2023.

Les objets peuvent être n'importe quel fichier. Il peut s'agir de vidéo, d'audio, d'image, de fichier texte, de fichier Excel, de document Word, de HTML, de CSS, de XML, de JSON, et ainsi de suite.

Le stockage d'objets est hautement durable – c'est-à-dire qu'il y a une très faible probabilité que tout objet stocké soit perdu.

Le stockage d'objets offert par les fournisseurs de cloud fournit généralement une durabilité de 99,999999999 % sur un an. Cela est communément appelé 11 neuf de durabilité.

La durabilité est définie comme la probabilité de **ne pas** perdre un objet. Un système de stockage qui a une durabilité de 99,999999999 % a une probabilité de 0,000000001 % de perdre un seul objet en un an. Cela signifie que même si vous avez un million d'objets stockés dans le stockage d'objets, vous n'êtes susceptible de perdre qu'un seul objet en 100 000 ans.

C'est un niveau remarquable de durabilité qui n'est pas égalé par les autres systèmes de stockage.

Naturellement, toutes ces probabilités sont sans signification si la Terre est détruite, puisque tous les serveurs stockant ces objets résident actuellement sur une seule planète.

Les principaux fournisseurs de cloud ont tous des options de stockage d'objets :

1. AWS – S3
   
2. GCP – Cloud Storage
   
3. Azure – Azure Blob storage

## Modèles et anti-modèles – Quand utiliser chaque type de stockage

Le tableau ci-dessous résume les compromis entre les différents types de stockage ainsi que certains cas d'utilisation.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd05d0204-4368-4ad7-94b7-6598713e23fc_2048x1246.png align="left")

Note : "Mountable" fait référence à la capacité de connecter ou d'attacher un dispositif de stockage ou un système de fichiers à un emplacement spécifique dans la hiérarchie du système de fichiers d'un ordinateur.

Lorsque un dispositif de stockage ou un système de fichiers est "mountable", cela signifie qu'il peut être intégré et rendu accessible au système d'exploitation et aux applications exécutées sur l'ordinateur.

Comme vous pouvez le voir dans l'image ci-dessus, certains cas d'utilisation courants pour chaque type de stockage sont les suivants :

* Stockage par blocs : bases de données, ETL, calcul haute performance, stockage du système d'exploitation et volume de démarrage
   
* Stockage de fichiers : partage de fichiers entre plusieurs instances de calcul
   
* Stockage d'objets : stockage grand, scalable et durable de différents objets (comme des images, de l'audio et de la vidéo), reprise après sinistre et archivage de données.

## Mettre tout ensemble

Imaginons un scénario simple où vous devriez utiliser le stockage par blocs, le stockage de fichiers et le stockage d'objets ensemble.

Imaginez que vous avez été chargé de concevoir l'architecture cloud pour un cabinet d'avocats. Vous devez stocker un grand nombre de fichiers de preuves dans différents formats (audio, vidéo, image, texte, Excel, JSON, etc.).

Vous devez traiter ces fichiers, extraire les informations utiles et les rendre disponibles pour un traitement ultérieur par différentes personnes. Vous devez également les rendre disponibles pour une utilisation directe par une équipe d'avocats dans différentes parties du monde.

À un niveau élevé, comment pourriez-vous concevoir une telle solution ?

Vous pouvez voir comment faire cela dans l'image ci-dessous :

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b53e26c-68ee-4f4b-82f4-e8de7d5d66ff_2022x1324.png align="left")

Tout d'abord, les fichiers bruts pourraient être stockés en utilisant soit le stockage d'objets, soit le stockage de fichiers. Le stockage d'objets est préférable car il est moins coûteux. Il est également idéal pour le stockage d'archives à faible coût si vous devez conserver des fichiers pendant plusieurs années.

Pour traiter les fichiers, vous pouvez exécuter plusieurs applications sur une instance EC2 qui utilise le stockage par blocs. L'autre alternative est d'utiliser le stockage de fichiers.

Le stockage par blocs est préférable car ces tâches de traitement peuvent inclure des choses comme la transcription de fichiers audio, l'extraction de texte à partir d'images, l'amélioration et la stabilisation de fichiers vidéo, une base de données qui extrait des données au format JSON et les stocke dans une base de données relationnelle, et ainsi de suite. Ce sont toutes des tâches qui nécessitent des performances plus élevées, ce qui est un cas d'utilisation idéal pour le stockage par blocs.

Les fichiers traités sont ensuite stockés dans S3 avant d'être chargés dans un système de fichiers avec plusieurs instances montées dessus.

Les fichiers traités à jour doivent être disponibles pour un traitement ultérieur ou pour une utilisation directe par une équipe d'avocats. Le stockage par blocs n'est pas idéal ici car le stockage par blocs ne peut pas être partagé entre plusieurs instances. Le stockage d'objets n'est pas non plus idéal car il n'est pas mountable (ne peut pas être attaché à une instance de calcul).

Dans ce cas, le stockage de fichiers est idéal car il n'a aucune de ces contraintes – il peut être partagé entre plusieurs instances et il est mountable.

## Résumé

En résumé, le stockage par blocs est idéal pour les applications haute performance. Le stockage de fichiers est idéal pour partager des fichiers entre plusieurs instances.

Comme le stockage par blocs, le stockage de fichiers est mountable – c'est-à-dire qu'il peut être intégré et rendu accessible au système d'exploitation et aux applications exécutées sur l'instance.

Le stockage d'objets est idéal pour un stockage durable et scalable à faible coût où les performances élevées ne sont pas importantes.

Merci d'avoir lu !