---
title: 'Virtualisation de serveur Linux : les bases'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-12T11:15:00.000Z'
originalURL: https://freecodecamp.org/news/linux-server-virtualization-the-basics
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca17e740569d1a4ca4ee1.jpg
tags:
- name: Linux
  slug: linux
- name: technology
  slug: technology
seo_title: 'Virtualisation de serveur Linux : les bases'
seo_desc: 'Excerpted from my book: Teach Yourself Linux Virtualization and High Availability:
  prepare for the LPIC-3 304 certification exam — also available from my Bootstrap-IT
  site.

  Despite having access to ever more efficient and powerful hardware, operation...'
---

Extrait de mon livre : [_Teach Yourself Linux Virtualization and High Availability: prepare for the LPIC-3 304 certification exam_](https://www.amazon.com/gp/product/B06XTZ4YWQ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B06XTZ4YWQ&linkCode=as2&tag=projemun-20&linkId=fa7577d96ed91ffe111b08665bcb53f9) — également disponible sur mon site [_Bootstrap-IT_](https://bootstrap-it.com/).

Malgré l'accès à du matériel de plus en plus efficace et puissant, les opérations exécutées directement sur des serveurs physiques traditionnels (ou "bare-metal") rencontrent inévitablement des limites pratiques significatives. Le coût et la complexité de la construction et du lancement d'un seul serveur physique signifient qu'il est difficile, voire impossible dans certains cas, d'ajouter ou de supprimer des ressources rapidement pour répondre à une demande changeante. Tester en toute sécurité de nouvelles configurations ou des applications complètes avant leur publication peut également être compliqué, coûteux et chronophage.

Comme l'ont envisagé les chercheurs pionniers Gerald J. Popek et Robert P. Goldberg dans un article de 1974 ("Formal Requirements for Virtualizable Third Generation Architectures" — Communications of the ACM 17 (7) : 412–421), une virtualisation réussie doit fournir un environnement qui :

* Est équivalent à celui d'une machine physique de sorte que l'accès logiciel aux ressources matérielles et aux pilotes doit être indistinguishable d'une expérience non virtualisée.
* Permet un contrôle complet du client sur le matériel du système virtualisé.
* Exécute efficacement les opérations directement sur les ressources matérielles sous-jacentes, y compris les CPU, chaque fois que possible.

La virtualisation permet de diviser les ressources physiques de calcul, de mémoire, de réseau et de stockage (les "quatre piliers") entre plusieurs entités virtuelles. Chaque périphérique virtuel est représenté dans son environnement logiciel et utilisateur comme une entité réelle et autonome. Configurées correctement, les ressources virtuellement isolées peuvent fournir des applications plus sécurisées sans connectivité visible entre les environnements. La virtualisation permet également de provisionner et d'exécuter de nouvelles machines virtuelles presque instantanément, puis de les détruire dès qu'elles ne sont plus nécessaires.

Pour les grandes applications soutenant des besoins commerciaux en constante évolution, la capacité à monter et descendre rapidement en échelle peut faire la différence entre la survie et l'échec. Le type d'adaptabilité que la virtualisation offre permet aux scripts d'ajouter ou de supprimer des machines virtuelles en quelques secondes... plutôt que les semaines qu'il pourrait falloir pour acheter, provisionner et déployer un serveur physique.

### Comment fonctionne la virtualisation

Dans des conditions non virtualisées, les architectures x86 contrôlent strictement quels processus peuvent fonctionner dans chacune des quatre couches de privilèges soigneusement définies (décrites comme Ring 0 à Ring 3).

Normalement, seul le noyau du système d'exploitation hôte a une chance d'accéder aux instructions conservées dans le Ring 0. Cependant, puisque vous ne pouvez pas donner à plusieurs machines virtuelles exécutées sur un seul ordinateur physique un accès égal au Ring 0 sans demander de gros problèmes, il doit y avoir un gestionnaire de machine virtuelle (ou "hyperviseur") dont le travail est de rediriger efficacement les demandes de ressources comme la mémoire et le stockage vers leurs équivalents virtualisés.

Lorsqu'on travaille dans un environnement matériel sans virtualisation SVM ou VT-x, cela se fait par un processus appelé _trap and emulate and binary translation_. Sur du matériel virtualisé, de telles demandes peuvent généralement être interceptées par l'hyperviseur, adaptées à l'environnement virtuel et renvoyées à la machine virtuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VKQEIJ0eOYiEYyE9tdfosA.png)

Simplement ajouter une nouvelle couche logicielle pour fournir ce niveau de coordination ajoutera une latence significative à presque tous les aspects des performances du système. Une solution très réussie a été d'introduire de nouveaux jeux d'instructions dans les CPU qui créent un soi-disant "Ring -1" qui agira comme le Ring 0 et permettra à un système d'exploitation invité de fonctionner sans avoir d'impact sur d'autres opérations non liées.

En fait, lorsqu'elle est bien implémentée, la virtualisation permet à la plupart des codes logiciels de s'exécuter exactement comme ils le feraient normalement sans avoir besoin de piégeage.

Bien qu'elle joue souvent un rôle de support dans les déploiements de virtualisation, l'émulation fonctionne assez différemment. Alors que la virtualisation cherche à diviser les ressources matérielles existantes entre plusieurs utilisateurs, le but de l'émulation est de faire en sorte qu'un environnement matériel/logiciel particulier _imite_ un environnement qui n'existe pas réellement, afin que les utilisateurs puissent lancer des processus qui ne seraient pas possibles nativement. Cela nécessite un code logiciel qui simule l'environnement matériel sous-jacent souhaité pour tromper votre logiciel en lui faisant croire qu'il s'exécute réellement ailleurs.

L'émulation peut être relativement simple à implémenter, mais elle entraînera presque toujours une pénalité de performance sérieuse.

Il existe traditionnellement deux classes d'hyperviseurs : Type-1 et Type-2.

* Les **hyperviseurs bare-metal (Type-1)** sont démarrés en tant que système d'exploitation d'une machine et — parfois via une machine virtuelle privilégiée principale (VM) — maintiennent un contrôle total sur le matériel hôte, exécutant chaque système d'exploitation invité en tant que processus système. XenServer et VMWare ESXi sont des exemples modernes notables de Type-1. Ces dernières années, l'usage populaire du terme "hyperviseur" s'est étendu pour inclure toutes les technologies de virtualisation hôte, mais autrefois, il aurait été utilisé pour décrire uniquement les systèmes de Type-1. Le terme plus général couvrant tous les types aurait à l'origine été "Virtual Machine Monitors". Dans la mesure où les gens utilisent le terme Virtual Machine Monitors de nos jours, je suspecte qu'ils veulent dire "hyperviseur" dans toutes ses itérations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xHciV6s-OME8Re8y-rncQA.png)

* Les **hyperviseurs hébergés (Type-2)** sont eux-mêmes simplement des processus s'exécutant sur une pile de système d'exploitation normale. Les hyperviseurs de Type-2 (qui incluent VirtualBox et, dans une certaine mesure, KVM) abstraient les ressources du système hôte pour les systèmes d'exploitation invités, fournissant l'illusion d'un environnement matériel privé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7Wer6qT1tWFU8SDNjw6Jag.png)

### Virtualisation : PV vs HVM

Les machines virtuelles (VM) sont entièrement virtualisées. En d'autres termes, elles pensent qu'elles sont des déploiements de systèmes d'exploitation réguliers vivant heureux sur leur propre matériel privé. Parce qu'elles n'ont pas besoin d'interfacer avec leur environnement différemment d'un système d'exploitation autonome, elles peuvent s'exécuter avec des piles logicielles non modifiées prêtes à l'emploi. Par le passé, cependant, cette compatibilité avait un coût, car la traduction des signaux matériels à travers une couche d'émulation prenait du temps et des cycles supplémentaires.

Les invités paravirtualisés (PV) sont, en revanche, au moins partiellement conscients de leur environnement virtuel, y compris du fait qu'ils partagent des ressources matérielles avec d'autres machines virtuelles. Cette conscience signifie qu'il n'est pas nécessaire pour les hôtes PV d'émuler le stockage et le matériel réseau et rend disponibles des pilotes d'E/S efficaces. Historiquement, cela a permis aux hyperviseurs PV d'atteindre de meilleures performances pour les opérations nécessitant une connectivité aux composants matériels.

Cependant, pour fournir un accès invité à un Ring 0 virtuel (c'est-à-dire Ring -1), les plateformes matérielles modernes — et en particulier l'architecture Ivy Bridge d'Intel — ont introduit une nouvelle bibliothèque de jeux d'instructions CPU qui a permis à la virtualisation de machines virtuelles matérielles (**HVM**) de dépasser le goulot d'étranglement du piégeage et de l'émulation et de tirer pleinement parti des extensions matérielles et des opérations de noyau logiciel non modifiées.

La technologie récente d'Intel, Extended Page Tables (EPT), peut également augmenter significativement les performances de la virtualisation.

Par conséquent, pour la plupart des cas d'utilisation, vous constaterez maintenant que HVM offre de meilleures performances, portabilité et compatibilité.

### Compatibilité matérielle

Au moins certaines fonctionnalités de virtualisation nécessitent un support matériel — surtout de la part du CPU de l'hôte. Par conséquent, vous devriez vous assurer que votre serveur dispose de tout ce dont vous aurez besoin pour la tâche que vous allez lui confier. La plupart de ce que vous devrez savoir est conservé dans le fichier **/proc/cpuinfo** et, en particulier, dans la section "flags" de chaque processeur. Comme il y aura tant de flags, vous devrez savoir quoi chercher.

Exécutez

> _$ grep flags /proc/cpuinfo_

… pour voir ce que vous avez sous le capot.

### Virtualisation de conteneurs

Comme nous l'avons vu, une VM d'hyperviseur est un système d'exploitation complet dont la relation avec les ressources matérielles Core Four est entièrement virtualisée : elle pense qu'elle s'exécute sur son propre ordinateur.

Un hyperviseur installe une VM à partir de la même image ISO que vous téléchargeriez et utiliseriez pour installer un système d'exploitation directement sur un disque dur physique vide.

Un conteneur, en revanche, est effectivement une application, lancée à partir d'un modèle de type script, qui pense qu'elle est un système d'exploitation. Dans les technologies de conteneurs (comme LXC et Docker), les conteneurs ne sont rien de plus que des abstractions de logiciels et de ressources (fichiers, processus, utilisateurs) qui dépendent du noyau hôte et d'une représentation des ressources matérielles "core four" (c'est-à-dire, CPU, RAM, réseau et stockage) pour tout ce qu'ils font.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kfhJ8J0sgU4vg-Zv1HdMyg.png)

Bien sûr, puisque les conteneurs sont, effectivement, des extensions isolées du noyau hôte, virtualiser Windows (ou même des versions plus anciennes ou plus récentes de Linux exécutant des versions incompatibles de libc) sur, par exemple, un hôte Ubuntu 16.04, est impossible. Mais la technologie permet des opportunités de calcul incroyablement légères et polyvalentes.

### Migration

Le modèle de virtualisation permet également une très large gamme d'opérations de migration, de sauvegarde et de clonage — même à partir de systèmes en cours d'exécution (V2V). Puisque les ressources logicielles qui définissent et pilotent une machine virtuelle sont si facilement identifiées, il ne faut généralement pas trop d'efforts pour dupliquer des environnements de serveur complets dans plusieurs emplacements et pour plusieurs objectifs.

Parfois, ce n'est pas plus compliqué que de créer une archive d'un système de fichiers virtuel sur un hôte, de la décompresser dans le même chemin sur un hôte différent, de vérifier les paramètres réseau de base et de la démarrer. La plupart des plateformes offrent une seule opération en ligne de commande pour déplacer les invités entre les hôtes.

Migrer des déploiements de serveurs physiques vers des environnements virtualisés (P2V) peut parfois être un peu plus délicat. Même créer une image clonée d'un serveur physique simple et l'importer dans une VM vide peut impliquer une certaine complexité. Et une fois que c'est fait, vous devrez peut-être encore apporter des ajustements considérables à la conception pour tirer pleinement parti de toutes les fonctionnalités que la virtualisation a à offrir. Selon le système d'exploitation que vous migrez, vous devrez peut-être également incorporer des pilotes paravirtualisés dans le processus pour permettre au système d'exploitation de s'exécuter correctement dans son nouvel environnement.

Comme pour tout le reste dans la gestion des serveurs : planifiez soigneusement à l'avance.

_Extrait de mon livre :_ [_Teach Yourself Linux Virtualization and High Availability: prepare for the LPIC-3 304 certification exam_](https://www.amazon.com/gp/product/B06XTZ4YWQ/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B06XTZ4YWQ&linkCode=as2&tag=projemun-20&linkId=fa7577d96ed91ffe111b08665bcb53f9).

_Intéressé à apprendre à déployer des projets pratiques d'administration Linux ? Consultez mon livre Manning,_ [_Linux in Action_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9).

_Ou, vous pouvez essayer un cours hybride appelé_ [_Linux in Motion_](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) _qui est composé de plus de deux heures de vidéo et d'environ 40 % du texte de Linux in Action._