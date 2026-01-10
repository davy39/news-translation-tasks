---
title: Introduction à Linux
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-02-23T13:49:13.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/linux.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: 'Si vous débutez sous Linux, ce cours est fait pour vous.

  Dans ce cours complet, vous apprendrez à utiliser de nombreux outils utilisés quotidiennement par
  les administrateurs système Linux (SysAdmins) et les millions de personnes utilisant des distributions Linux comme
  Ubuntu sur leurs PC. Ce cours vous enseignera...'
---

Si vous débutez sous Linux, ce cours est fait pour vous.

Dans ce cours complet, vous apprendrez à utiliser de nombreux outils utilisés quotidiennement par les administrateurs système Linux (SysAdmins) et les millions de personnes utilisant des distributions Linux comme Ubuntu sur leurs PC. Ce cours vous enseignera comment naviguer dans les interfaces graphiques de Linux et dans son puissant écosystème d'outils en ligne de commande.

Le contenu de ce cours a été développé par la Fondation Linux (ils l'appellent LFS101x). J'ai pris leur cours principalement textuel et l'ai transformé en un cours vidéo.

Vous pouvez soit lire la version textuelle du cours ici même, soit regarder la version vidéo sur la chaîne YouTube de freeCodeCamp.org (6 heures de visionnage).

%[

Ce tutoriel est sous licence [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Si vous préférez la version textuelle du cours, continuez votre lecture !

## **Chapitre 1**

À la fin de ce chapitre, vous devriez être capable de :

* Décrire l'environnement logiciel requis pour ce cours.
* Et décrire les trois grandes familles de distributions Linux.

### Pré-requis du cours

Pour profiter pleinement de ce cours, vous devrez avoir au moins une distribution Linux installée (si vous n'êtes pas encore familier avec le terme distribution, en ce qui concerne Linux, vous le serez bientôt !).

Vous êtes sur le point d'apprendre plus de détails sur les nombreuses distributions Linux disponibles. Comme il existe littéralement des centaines de distributions, je ne les couvrirai pas toutes dans ce cours. Au lieu de cela, je me concentrerai sur les trois grandes familles de distributions.

Les familles et les distributions représentatives sur lesquelles ce cours se concentrera sont :

* **Systèmes de la famille Red Hat** (incluant **CentOS** et **Fedora**)
* **Systèmes de la famille SUSE** (incluant **openSUSE**)
* **Systèmes de la famille Debian** (incluant **Ubuntu** et **Linux Mint**).

![Trois captures d'écran montrant les bureaux Ubuntu, CentOS et OpenSUSE](https://courses.edx.org/assets/courseware/v1/fe27a9c47f2e272c238dc227cb749528/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnomedts.png)
_Bureaux Ubuntu, CentOS et openSUSE_

# 

### Focus sur les trois grandes familles de distributions Linux


Je vais vous en dire plus sur Red Hat, SUSE et Debian. Bien que ce cours se concentre sur ces trois grandes familles de distributions Linux, tant qu'il y aura des contributeurs talentueux, les familles de distributions et les distributions au sein de ces familles continueront de changer et de grandir. Les gens voient un besoin et développent des configurations et des utilitaires spéciaux pour répondre à ce besoin. Parfois, cet effort crée une toute nouvelle distribution de Linux. Parfois, cet effort s'appuie sur une distribution existante pour élargir les membres d'une famille existante.

![Les familles de distributions du noyau Linux et les distributions individuelles](https://courses.edx.org/assets/courseware/v1/1d8c97abd237dcd44a5fe5464f6521ac/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_The_Linux_Kernel_Distribution_Families_and_Individual_Distributions.png)
_Les familles de distributions du noyau Linux et les distributions individuelles_

### La famille Red Hat

Red Hat Enterprise Linux (ou RHEL [prononcé "rel"]) dirige la famille qui comprend CentOS, CentOS Stream, Fedora et Oracle Linux.

Fedora entretient une relation étroite avec RHEL et contient beaucoup plus de logiciels que la version entreprise de Red Hat. Une raison à cela est qu'une communauté diversifiée est impliquée dans la construction de Fedora, avec de nombreux contributeurs qui ne travaillent pas pour Red Hat. De plus, elle est utilisée comme plateforme de test pour les futures versions de RHEL.

![La famille Red Hat](https://courses.edx.org/assets/courseware/v1/8463dfd1fc8eb8ba7ff06731abc38382/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_The_Red_Hat_Family.png)
_La famille Red Hat_

Dans ce cours, nous utiliserons principalement CentOS Stream de la famille Red Hat.

La version de base de CentOS est également pratiquement identique à RHEL, la distribution Linux la plus populaire dans les environnements d'entreprise. Cependant, CentOS 8 n'a plus de mises à jour programmées. Le remplaçant est CentOS 8 Stream.

### Faits clés sur la famille Red Hat

Certains des faits clés concernant la famille de distribution Red Hat sont :

* Fedora sert de plateforme de test en amont (upstream) pour RHEL.
* CentOS est un clone proche de RHEL, tandis qu'Oracle Linux est principalement une copie avec quelques changements.
* Elle prend en charge les plateformes matérielles telles que Intel x86, Arm, Itanium, PowerPC et IBM System z.
* Elle utilise les gestionnaires de paquets basés sur RPM `yum` et `dnf` (discutés plus tard) pour installer, mettre à jour et supprimer des paquets dans le système.
* RHEL est largement utilisé par les entreprises qui hébergent leurs propres systèmes.

### La famille SUSE

La relation entre SUSE (SUSE Linux Enterprise Server, ou SLES) et openSUSE est similaire à celle décrite entre RHEL, CentOS et Fedora.

![La famille SUSE](https://courses.edx.org/assets/courseware/v1/ffd8ff6c0d84899812026c2e65efb0e1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_screen19.jpg)
_La famille SUSE_

Nous utilisons openSUSE comme distribution de référence pour la famille SUSE, car elle est disponible gratuitement pour les utilisateurs finaux. Comme les deux produits sont extrêmement similaires, le matériel qui couvre openSUSE peut généralement être appliqué à SLES avec peu de problèmes.

### Faits clés sur la famille SUSE

Certains des faits clés concernant la famille SUSE sont énumérés ci-dessous :

* SUSE Linux Enterprise Server (SLES) est en amont (upstream) pour openSUSE.
* Elle utilise le gestionnaire de paquets basé sur RPM `zypper` (nous le couvrirons en détail plus tard) pour installer, mettre à jour et supprimer des paquets dans le système.
* Elle inclut l'application YaST (Yet Another Setup Tool) à des fins d'administration système.
* SLES est largement utilisé dans le commerce de détail et de nombreux autres secteurs.

### La famille Debian

La distribution Debian est en amont pour plusieurs autres distributions, y compris Ubuntu. À son tour, Ubuntu est en amont pour Linux Mint et un certain nombre d'autres distributions. Elle est couramment utilisée à la fois sur les serveurs et les ordinateurs de bureau. Debian est un pur projet communautaire open source (non détenu par une entreprise) et met fortement l'accent sur la stabilité.

Debian fournit de loin le dépôt de logiciels le plus vaste et le plus complet à ses utilisateurs parmi toutes les distributions Linux.

![La famille Debian](https://courses.edx.org/assets/courseware/v1/223d3c300d6cdd86ae66e8c2b9faa265/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chapter01_screen20.jpg)
_La famille Debian_

Ubuntu vise à fournir un bon compromis entre la stabilité à long terme et la facilité d'utilisation. Comme Ubuntu obtient la plupart de ses paquets de la branche stable de Debian, elle a également accès à un très grand dépôt de logiciels. Pour ces raisons, nous utiliserons Ubuntu LTS (Long Term Support) comme référence aux distributions de la famille Debian pour ce cours.

### Faits clés sur la famille Debian

Certains faits clés sur la famille Debian sont énumérés ci-dessous :

* La famille Debian est en amont pour Ubuntu, et Ubuntu est en amont pour Linux Mint et d'autres.
* Elle utilise le gestionnaire de paquets basé sur DPKG APT (utilisant `apt`, `apt-get`, `apt-cache`, etc., que nous couvrirons en détail plus tard) pour installer, mettre à jour et supprimer des paquets dans le système.
* Ubuntu a été largement utilisé pour les déploiements cloud.
* Bien qu'Ubuntu soit construit sur Debian et soit basé sur GNOME sous le capot, il diffère visuellement de l'interface sur Debian standard, ainsi que d'autres distributions.

### Résumé du chapitre

* Il existe trois grandes familles de distributions au sein de Linux : **Red Hat**, **SUSE** et **Debian**. Dans ce cours, nous travaillerons avec des membres représentatifs de toutes ces familles tout au long du parcours.

## **Chapitre 2 : Philosophie et concepts Linux**

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Définir les termes courants associés à Linux.
* Discuter des composants d'une distribution Linux.

### La puissance de Linux

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V010000_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Introduction

Afin que vous puissiez tirer le meilleur parti de ce cours, nous vous recommandons d'avoir Linux installé sur une machine que vous pouvez utiliser tout au long de ce cours. Vous pouvez utiliser ce bref guide d'installation "_[Preparing Your Computer for Linux Training](https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+1T2020+type@asset+block@Preparing_Your_Computer_for_Linux_Training.pdf)_" (en anglais). Il vous aidera à sélectionner une distribution Linux à installer, à décider si vous voulez faire une machine purement Linux autonome ou un double démarrage (dual-boot), si vous voulez faire une installation physique ou virtuelle, etc. Et ensuite, il vous guide à travers les étapes. Je couvrirai également l'installation bientôt.

Nous n'avons pas tout couvert en grand détail, mais gardez à l'esprit que la plupart de la documentation sous Linux est en fait déjà sur votre système sous la forme de pages de manuel (man pages), dont nous discuterons en grand détail plus tard. Chaque fois que vous ne comprenez pas quelque chose ou que vous voulez en savoir plus sur une commande, un programme, un sujet ou un utilitaire, vous pouvez simplement taper **man <sujet>** sur la ligne de commande. Nous supposerons que vous pensez de cette façon et ne répéterons pas constamment "Pour plus d'informations, consultez la page de manuel pour **<sujet>**".

Sur une note connexe, tout au long du cours, nous utilisons un raccourci courant dans la communauté open source. Lorsque nous faisons référence à des cas où l'utilisateur doit faire un choix sur ce qu'il doit entrer (par exemple, le nom d'un programme ou d'un fichier), nous utilisons le raccourci '**foo**' pour représenter **<insérer le nom du fichier ici>**. Alors attention, nous ne suggérons pas réellement que vous manipuliez des fichiers ou installiez des services appelés '**foo**' !

La meilleure façon d'apprendre Linux est de le pratiquer. Assurez-vous donc d'essayer les choses vous-même au fur et à mesure.

Vous devrez avoir un système Linux opérationnel qui peut être soit un système Linux natif sur votre matériel, soit un système fonctionnant via une clé USB ou un CD live, soit une machine virtuelle fonctionnant via un hyperviseur.

Nous vous montrerons toutes ces méthodes, alors allons-y.

### Vidéo : Terminologie Linux

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V006600_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Distributions Linux

Supposons que vous ayez été affecté à un projet de construction d'un produit pour une plateforme Linux. Les exigences du projet incluent de s'assurer que le projet fonctionne correctement sur les distributions Linux les plus utilisées. Pour ce faire, vous devez apprendre les différents composants, services et configurations associés à chaque distribution. Nous sommes sur le point de voir comment vous y prendre exactement.

Alors, qu'est-ce qu'une distribution Linux et comment se rapporte-t-elle au noyau (kernel) Linux ?

Le noyau Linux est le cœur du système d'exploitation. Une distribution Linux complète se compose du noyau plus un certain nombre d'autres outils logiciels pour les opérations liées aux fichiers, la gestion des utilisateurs et la gestion des paquets logiciels. Chacun de ces outils fournit une partie du système complet. Chaque outil est souvent son propre projet séparé, avec ses propres développeurs travaillant à perfectionner cette pièce du système.

Bien que le noyau Linux le plus récent (et les versions antérieures) puisse toujours être trouvé dans [The Linux Kernel Archives](https://www.kernel.org/), les distributions Linux peuvent être basées sur différentes versions du noyau. Par exemple, la très populaire distribution RHEL 8 est basée sur le noyau 4.18, qui n'est pas nouveau, mais qui est extrêmement stable. D'autres distributions peuvent évoluer plus rapidement en adoptant les dernières versions du noyau. Il est important de noter que le noyau n'est pas une proposition "tout ou rien", par exemple, RHEL/CentOS ont incorporé de nombreuses améliorations récentes du noyau dans leurs anciennes versions, tout comme Ubuntu, openSUSE, SLES, etc.

Des exemples d'autres outils et ingrédients essentiels fournis par les distributions incluent les compilateurs C/C++ et Clang, le débogueur gdb, les bibliothèques système de base avec lesquelles les applications doivent se lier pour s'exécuter, l'interface de bas niveau pour dessiner des graphiques à l'écran, ainsi que l'environnement de bureau de plus haut niveau, et le système pour installer et mettre à jour les divers composants, y compris le noyau lui-même. Et toutes les distributions sont livrées avec une suite d'applications assez complète déjà installée.

![Rôles des distributions](https://courses.edx.org/assets/courseware/v1/be89578552325fd81fb6a9a6b613afe9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/distroroles.png)
_Rôles des distributions_

### Services associés aux distributions

La grande variété de distributions Linux est conçue pour répondre à de nombreux publics et organisations différents, selon leurs besoins et goûts spécifiques. Cependant, les grandes organisations, telles que les entreprises et les institutions gouvernementales et autres entités, ont tendance à choisir les principales distributions commercialement supportées de Red Hat, SUSE et Canonical (Ubuntu).

CentOS et CentOS Stream sont des alternatives gratuites (au sens de sans coût) populaires à Red Hat Enterprise Linux (RHEL) et sont souvent utilisées par des organisations qui sont à l'aise pour fonctionner sans support technique payant. Ubuntu et Fedora sont largement utilisées par les développeurs et sont également populaires dans le domaine éducatif. Scientific Linux est privilégié par la communauté de recherche scientifique pour sa compatibilité avec les paquets logiciels scientifiques et mathématiques. Les deux variantes de CentOS sont compatibles binaire avec RHEL ; c'est-à-dire que dans la plupart des cas, les paquets logiciels binaires s'installeront correctement entre les distributions.

Notez que CentOS devait disparaître fin 2021 au profit de CentOS Stream. Cependant, il existe au moins deux nouveaux substituts dérivés de RHEL : Alma Linux et Rocky Linux qui s'implantent.

De nombreux distributeurs commerciaux, y compris Red Hat, Ubuntu, SUSE et Oracle, fournissent un support payant à long terme pour leurs distributions, ainsi qu'une certification matérielle et logicielle. Tous les principaux distributeurs fournissent des services de mise à jour pour garder votre système prêt avec les derniers correctifs de sécurité et de bogues, et des améliorations de performance, ainsi que des ressources de support en ligne.

![Image](https://courses.edx.org/assets/courseware/v1/85a0445af315a7fb90444a2d3cd0e608/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch02_screen_24.jpg)
_Services associés aux distributions_

### Résumé du chapitre 2

Vous avez terminé le chapitre 2. Résumons les concepts clés couverts :

* Linux emprunte beaucoup au système d'exploitation UNIX, avec lequel ses créateurs étaient bien versés.
* Linux accède à de nombreuses fonctionnalités et services via des fichiers et des objets de type fichier.
* Linux est un système d'exploitation entièrement multitâche et multi-utilisateur, avec des processus de mise en réseau et de service intégrés connus sous le nom de démons (daemons).
* Linux est développé par une confédération lâche de développeurs du monde entier, collaborant sur Internet, avec Linus Torvalds à la tête. La compétence technique et le désir de contribuer sont les seules qualifications pour participer.
* La communauté Linux est un écosystème étendu de développeurs, de fournisseurs et d'utilisateurs qui soutient et fait progresser le système d'exploitation Linux.
* Certains des termes courants utilisés dans Linux sont : **noyau** (kernel), **distribution**, **chargeur d'amorçage** (boot loader), **service**, **système de fichiers** (filesystem), **système X Window**, **environnement de bureau** et **ligne de commande**.
* Une distribution Linux complète se compose du noyau plus un certain nombre d'autres outils logiciels pour les opérations liées aux fichiers, la gestion des utilisateurs et la gestion des paquets logiciels.

## **Chapitre 3 : Bases de Linux et démarrage du système**

À la fin de ce chapitre, vous devriez être capable de :

* Identifier les systèmes de fichiers Linux.
* Identifier les différences entre les partitions et les systèmes de fichiers.
* Décrire le processus de démarrage.
* Installer Linux sur un ordinateur.

## Le processus de démarrage

Le processus de démarrage Linux est la procédure d'initialisation du système. Il comprend tout ce qui se passe depuis le moment où l'ordinateur est mis sous tension jusqu'à ce que l'interface utilisateur soit pleinement opérationnelle.

Avoir une bonne compréhension des étapes du processus de démarrage peut vous aider à résoudre les problèmes, ainsi qu'à adapter les performances de l'ordinateur à vos besoins.

D'un autre côté, le processus de démarrage peut être assez technique, et vous pouvez commencer à utiliser Linux sans en connaître tous les détails.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-373.png)
_Le processus de démarrage._

### BIOS - La première étape

Le démarrage d'un système Linux basé sur x86 implique un certain nombre d'étapes. Lorsque l'ordinateur est mis sous tension, le **BIOS** (**B**asic **I**nput/**O**utput **S**ystem) initialise le matériel, y compris l'écran et le clavier, et teste la mémoire principale. Ce processus est également appelé **POST** (**P**ower **O**n **S**elf **T**est).

![BIOS](https://courses.edx.org/assets/courseware/v1/f02a193180acffca543bf8f69870cc79/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen16.jpg)
_BIOS_

Le logiciel BIOS est stocké sur une puce ROM sur la carte mère. Après cela, le reste du processus de démarrage est contrôlé par le système d'exploitation (OS).

### Master Boot Record (MBR) et chargeur d'amorçage

Une fois le POST terminé, le contrôle du système passe du BIOS au **chargeur d'amorçage** (boot loader). Le chargeur d'amorçage est généralement stocké sur l'un des disques durs du système, soit dans le secteur d'amorçage (pour les systèmes BIOS/MBR traditionnels) soit dans la partition **EFI** (pour les systèmes **EFI/UEFI** plus récents - (Unified) **E**xtensible **F**irmware **I**nterface). Jusqu'à ce stade, la machine n'accède à aucun support de stockage de masse. Par la suite, les informations sur la date, l'heure et les périphériques les plus importants sont chargées à partir des valeurs CMOS (d'après une technologie utilisée pour la mémoire alimentée par batterie qui permet au système de garder une trace de la date et de l'heure même lorsqu'il est éteint).

Un certain nombre de chargeurs d'amorçage existent pour Linux ; les plus courants sont **GRUB** (pour **GR**and **U**nified **B**oot loader), **ISOLINUX** (pour démarrer à partir de supports amovibles) et **DAS U-Boot** (pour démarrer sur des appareils/appliances embarqués). La plupart des chargeurs d'amorçage Linux peuvent présenter une interface utilisateur pour choisir des options alternatives pour démarrer Linux, et même d'autres systèmes d'exploitation qui pourraient être installés. Lors du démarrage de Linux, le chargeur d'amorçage est responsable du chargement de l'image du noyau et du disque RAM initial ou système de fichiers (qui contient certains fichiers critiques et pilotes de périphériques nécessaires pour démarrer le système) en mémoire.

![Master Boot Record](https://courses.edx.org/assets/courseware/v1/b053b7b69e99a0c06ef0da7fd84236d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen20.jpg)
_Master Boot Record_

### Le chargeur d'amorçage en action

Le chargeur d'amorçage a deux étapes distinctes :

Pour les systèmes utilisant la méthode BIOS/MBR, le chargeur d'amorçage réside au premier secteur du disque dur, également connu sous le nom de **M**aster **B**oot **R**ecord (**MBR**). La taille du MBR est juste de 512 octets. À ce stade, le chargeur d'amorçage examine la **table de partition** et trouve une partition amorçable. Une fois qu'il trouve une partition amorçable, il recherche alors le chargeur d'amorçage de deuxième étape, par exemple GRUB, et le chargee en RAM (Random Access Memory). Pour les systèmes utilisant la méthode EFI/UEFI, le firmware UEFI lit ses données de gestionnaire de démarrage pour déterminer quelle application UEFI doit être lancée et d'où (c'est-à-dire à partir de quel disque et partition la partition EFI peut être trouvée). Le firmware lance ensuite l'application UEFI, par exemple GRUB, telle que définie dans l'entrée de démarrage dans le gestionnaire de démarrage du firmware. Cette procédure est plus compliquée, mais plus polyvalente que les anciennes méthodes MBR.

![Le chargeur d'amorçage en action](https://courses.edx.org/assets/courseware/v1/abd1fcc0cc9a6fe48d886efdd98711ef/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen18.jpg)

Le chargeur d'amorçage de deuxième étape réside sous **/boot**. Un écran de démarrage s'affiche, ce qui nous permet de choisir quel système d'exploitation (OS) démarrer. Après avoir choisi l'OS, le chargeur d'amorçage charge le noyau du système d'exploitation sélectionné en RAM et lui passe le contrôle. Les noyaux sont presque toujours compressés, donc son premier travail est de se décompresser. Après cela, il vérifiera et analysera le matériel du système et initialisera tous les pilotes de périphériques matériels intégrés au noyau.

### Disque RAM initial

L'image du système de fichiers **initramfs** contient des programmes et des fichiers binaires qui effectuent toutes les actions nécessaires pour monter le système de fichiers racine approprié, comme fournir une fonctionnalité du noyau pour le système de fichiers nécessaire et des pilotes de périphériques pour les contrôleurs de stockage de masse avec une installation appelée **udev** (pour **u**ser **dev**ice), qui est responsable de déterminer quels périphériques sont présents, de localiser les pilotes de périphériques dont ils ont besoin pour fonctionner correctement et de les charger. Une fois le système de fichiers racine trouvé, il est vérifié pour les erreurs et monté.

Le programme **mount** indique au système d'exploitation qu'un système de fichiers est prêt à être utilisé et l'associe à un point particulier dans la hiérarchie globale du système de fichiers (le **point de montage**). Si cela réussit, l'initramfs est effacé de la RAM et le programme init sur le système de fichiers racine (**/sbin/init**) est exécuté.

**init** gère le montage et le basculement vers le système de fichiers racine réel final. Si des pilotes matériels spéciaux sont nécessaires avant que le stockage de masse puisse être accédé, ils doivent être dans l'image initramfs.

![Le disque RAM initial](https://courses.edx.org/assets/courseware/v1/13f8548b13ebe15a19aa1a6c3964fceb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen22.jpg)
_Le disque RAM initial_

### Connexion en mode texte

Vers la fin du processus de démarrage, **init** lance un certain nombre d'invites de connexion en mode texte. Celles-ci vous permettent de taper votre nom d'utilisateur, suivi de votre mot de passe, et d'obtenir éventuellement un shell de commande. Cependant, si vous exécutez un système avec une interface de connexion graphique, vous ne les verrez pas au début.

Comme vous l'apprendrez dans le _Chapitre 7 : Opérations en ligne de commande_, les terminaux qui exécutent les shells de commande peuvent être accédés en utilisant la touche **ALT** plus une touche de **fonction**. La plupart des distributions démarrent six terminaux texte et un terminal graphique commençant par **F1** ou **F2**. Dans un environnement graphique, passer à une console texte nécessite d'appuyer sur **CTRL-ALT** + la touche de fonction appropriée (avec **F7** ou **F1** menant à l'interface graphique).

![Connexion en mode texte](https://courses.edx.org/assets/courseware/v1/e35bea5a8c6b9a41453a0e01c5ca3077/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen26.jpg)
_Connexions en mode texte_

Généralement, le shell de commande par défaut est **bash** (le **GNU** **B**ourne **A**gain **Sh**ell), mais il existe un certain nombre d'autres shells de commande avancés disponibles. Le shell imprime une invite de texte, indiquant qu'il est prêt à accepter des commandes ; après que l'utilisateur tape la commande et appuie sur **Entrée**, la commande est exécutée, et une autre invite est affichée une fois la commande terminée.

### Le noyau Linux

Le chargeur d'amorçage charge à la fois le **noyau** et un système de fichiers initial basé sur la RAM (initramfs) en mémoire, afin qu'il puisse être utilisé directement par le noyau.

![Le noyau Linux](https://courses.edx.org/assets/courseware/v1/b953394cd3145a1bd239673dc5c5a5b7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen21.jpg)
_Le noyau Linux_

Lorsque le noyau est chargé en RAM, il initialise et configure immédiatement la mémoire de l'ordinateur et configure également tout le matériel connecté au système. Cela inclut tous les processeurs, sous-systèmes d'E/S, périphériques de stockage, etc. Le noyau charge également certaines applications de l'espace utilisateur nécessaires.

### /sbin/init et Services

Une fois que le noyau a configuré tout son matériel et monté le système de fichiers racine, le noyau exécute **/sbin/init**. Cela devient alors le processus initial, qui démarre ensuite d'autres processus pour faire fonctionner le système. La plupart des autres processus sur le système tracent leur origine ultimement à **init** ; les exceptions incluent les soi-disant processus du noyau. Ceux-ci sont démarrés par le noyau directement, et leur travail consiste à gérer les détails internes du système d'exploitation.

En plus de démarrer le système, **init** est responsable de maintenir le système en marche et de l'arrêter proprement. L'une de ses responsabilités est d'agir si nécessaire en tant que gestionnaire pour tous les processus non-noyau ; il nettoie après eux à la fin, et redémarre les services de connexion utilisateur au besoin lorsque les utilisateurs se connectent et se déconnectent, et fait de même pour d'autres services système en arrière-plan.

![/sbin/init et Services](https://courses.edx.org/assets/courseware/v1/640a31713f9fded06718cb06c468f685/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen24.jpg)
_/sbin/init et Services_

Traditionnellement, ce démarrage de processus était effectué en utilisant des conventions qui remontent aux années 1980 et à la variété System V d'UNIX. Ce processus série faisait passer le système par une séquence de **niveaux d'exécution** (runlevels) contenant des collections de scripts qui démarrent et arrêtent des services. Chaque niveau d'exécution prenait en charge un mode différent de fonctionnement du système. Au sein de chaque niveau d'exécution, des services individuels pouvaient être configurés pour s'exécuter, ou pour être arrêtés s'ils étaient en cours d'exécution.

Cependant, toutes les grandes distributions se sont éloignées de cette méthode séquentielle de niveau d'exécution pour l'initialisation du système, bien qu'elles émulent généralement de nombreux utilitaires System V à des fins de compatibilité. Ensuite, nous discutons des nouvelles méthodes, dont **systemd** est devenue dominante.

### Alternatives de démarrage

**SysVinit** voyait les choses comme un processus série, divisé en une série d'étapes séquentielles. Chaque étape nécessitait d'être terminée avant que la suivante puisse continuer. Ainsi, le démarrage ne tirait pas facilement parti du _traitement parallèle_ qui pouvait être effectué sur plusieurs processeurs ou cœurs.

De plus, l'arrêt et le redémarrage étaient considérés comme un événement relativement rare ; le temps exact que cela prenait n'était pas considéré comme important. Ce n'est plus vrai, surtout avec les appareils mobiles et les systèmes Linux embarqués. Certaines méthodes modernes, telles que l'utilisation de **conteneurs**, peuvent nécessiter des temps de démarrage presque instantanés. Ainsi, les systèmes nécessitent désormais des méthodes avec des capacités plus rapides et améliorées. Enfin, les anciennes méthodes nécessitaient des scripts de démarrage shell assez compliqués, qui étaient difficiles à garder universels à travers les versions de distribution, les versions de noyau, les architectures et les types de systèmes. Les deux principales alternatives développées étaient :

**Upstart**

* Développé par Ubuntu et inclus pour la première fois en 2006
* Adopté dans Fedora 9 (en 2008) et dans RHEL 6 et ses clones

**systemd**

* Adopté par Fedora en premier (en 2011)
* Adopté par RHEL 7 et SUSE
* A remplacé Upstart dans Ubuntu 16.04

Bien que la migration vers **systemd** ait été plutôt controversée, elle a été adoptée par toutes les grandes distributions, et nous ne discuterons donc pas de l'ancienne méthode System V ou d'Upstart, qui est devenu une impasse. Indépendamment de ce que l'on pense des controverses ou des méthodes techniques de **systemd**, l'adoption quasi universelle a rendu l'apprentissage du travail sur les systèmes Linux plus simple, car il y a moins de différences entre les distributions. Nous énumérons les fonctionnalités de **systemd** ensuite.

### Fonctionnalités de systemd

Les systèmes avec **systemd** démarrent plus rapidement que ceux avec les méthodes **init** antérieures. C'est en grande partie parce qu'il remplace un ensemble d'étapes sérialisées par des techniques de parallélisation agressives, ce qui permet à plusieurs services d'être initiés simultanément.

Les scripts shell de démarrage compliqués sont remplacés par des fichiers de configuration plus simples, qui énumèrent ce qui doit être fait avant qu'un service ne soit démarré, comment exécuter le démarrage du service, et quelles conditions le service doit indiquer avoir accomplies lorsque le démarrage est terminé. Une chose à noter est que **/sbin/init** pointe maintenant simplement vers **/lib/systemd/systemd** ; c'est-à-dire que **systemd** prend en charge le processus **init**.

Une commande **systemd** (**systemctl**) est utilisée pour la plupart des tâches de base. Bien que nous n'ayons pas encore parlé du travail en ligne de commande, voici une brève liste de son utilisation :

* Démarrer, arrêter, redémarrer un service (en utilisant **httpd**, le serveur web Apache, comme exemple) sur un système en cours d'exécution :
**$ sudo systemctl start|stop|restart httpd.service**
* Activer ou désactiver le démarrage d'un service système au démarrage du système :
**$ sudo systemctl enable|disable httpd.service**

Dans la plupart des cas, le **.service** peut être omis. Il existe de nombreuses différences techniques avec les anciennes méthodes qui dépassent le cadre de notre discussion.

![Logo systemd](https://courses.edx.org/assets/courseware/v1/2a63469f639dfeaf697c55ca137ac1d9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/systemd.png)

## Bases des systèmes de fichiers Linux

Pensez à un réfrigérateur qui a plusieurs étagères pouvant être utilisées pour stocker divers articles. Ces étagères vous aident à organiser les articles d'épicerie par forme, taille, type, etc. Le même concept s'applique à un système de fichiers, qui est l'incarnation d'une méthode de stockage et d'organisation de collections arbitraires de données sous une forme utilisable par l'homme.

Différents types de systèmes de fichiers pris en charge par Linux :

* Systèmes de fichiers disque conventionnels : **ext3**, **ext4**, **XFS**, **Btrfs**, **JFS**, **NTFS**, **vfat**, **exfat**, etc.
* Systèmes de fichiers de stockage Flash : **ubifs**, **jffs2**, **yaffs**, etc.
* Systèmes de fichiers de base de données
* Systèmes de fichiers à usage spécial : **procfs**, **sysfs**, **tmpfs**, **squashfs**, **debugfs**, **fuse**, etc.

Cette section décrira la disposition standard du système de fichiers partagée par la plupart des distributions Linux.

### Partitions et systèmes de fichiers

Une **partition** est une section physiquement contiguë d'un disque, ou ce qui semble l'être dans certaines configurations avancées.

Un **système de fichiers** est une méthode de stockage/recherche de fichiers sur un disque dur (généralement dans une partition).

On peut penser à une partition comme un conteneur dans lequel réside un système de fichiers, bien que dans certaines circonstances, un système de fichiers puisse s'étendre sur plus d'une partition si l'on utilise des liens symboliques, dont nous discuterons beaucoup plus tard.

Une comparaison entre les systèmes de fichiers sous Windows et Linux est donnée dans le tableau ci-joint :

<table border="0" width="100%" height="200" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 750px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 14px;">&nbsp;</td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Windows</strong></span></td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Linux</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Partition</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Disk1</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">/dev/sda1</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Type de système de fichiers</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">NTFS/VFAT</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">EXT3/EXT4/XFS/BTRFS...</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Paramètres de montage</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Lettre de lecteur</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Point de montage</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Dossier de base (où l'OS est stocké)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">C:\</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">/</td></tr></tbody></table>

### La norme de hiérarchie des systèmes de fichiers

Les systèmes Linux stockent leurs fichiers importants selon une disposition standard appelée **F**ilesystem **H**ierarchy **S**tandard (**FHS**), qui a longtemps été maintenue par la Fondation Linux. Pour plus d'informations, jetez un œil au document suivant : "_[Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf)_" créé par le groupe de travail LSB. Avoir une norme est conçu pour garantir que les utilisateurs, les administrateurs et les développeurs peuvent passer d'une distribution à l'autre sans avoir à réapprendre comment le système est organisé.

Linux utilise le caractère ‘**/**’ pour séparer les chemins (contrairement à Windows, qui utilise ‘**\**’), et n'a pas de lettres de lecteur. Plusieurs disques et/ou partitions sont montés en tant que répertoires dans le système de fichiers unique. Les supports amovibles tels que les clés USB et les CD et DVD apparaîtront comme montés à **/run/media/votrenomutilisateur/labeldisque** pour les systèmes Linux récents, ou sous **/media** pour les distributions plus anciennes. Par exemple, si votre nom d'utilisateur est **student**, une clé USB étiquetée FEDORA pourrait finir par être trouvée à **/run/media/student/FEDORA**, et un fichier **README.txt** sur ce disque serait à **/run/media/student/FEDORA/README.txt**.

Cliquez sur l'image pour voir une version agrandie.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-374.png)
_La norme de hiérarchie des systèmes de fichiers_

Tous les noms de systèmes de fichiers Linux sont sensibles à la casse, donc **/boot**, **/Boot** et **/BOOT** représentent trois répertoires (ou dossiers) différents. De nombreuses distributions font la distinction entre les utilitaires de base nécessaires au bon fonctionnement du système et les autres programmes, et placent ces derniers dans des répertoires sous **/usr** (pensez utilisateur). Pour avoir une idée de la façon dont les autres programmes sont organisés, trouvez le répertoire **/usr** dans le diagramme de la page précédente et comparez les sous-répertoires avec ceux qui existent directement sous le répertoire racine du système (**/**).

![fs tree](https://courses.edx.org/assets/courseware/v1/65256a6c88506b6e45744b97b8875775/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/fstree1.png)

### Vidéo : Visualisation de la hiérarchie du système de fichiers depuis l'interface graphique dans Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V004800_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Visualisation de la hiérarchie du système de fichiers depuis l'interface graphique dans openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V002000_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

## Installation d'une distribution Linux

Supposons que vous ayez l'intention d'acheter une nouvelle voiture. Quels facteurs devez-vous prendre en compte pour faire un choix approprié ? Les exigences qui doivent être prises en compte incluent la taille nécessaire pour faire tenir votre famille dans le véhicule, le type de moteur et l'économie de carburant, votre budget prévu et les options de financement disponibles, le dossier de fiabilité et les services après-vente, etc.

De même, déterminer quelle distribution déployer nécessite également une planification. La figure montre certains choix, mais pas tous. Notez que de nombreux systèmes Linux embarqués utilisent des contenus personnalisés, plutôt qu'Android ou Yocto.

![Choisir une distribution Linux](https://courses.edx.org/assets/courseware/v1/6eafa3b1170a0c208335ea46ac16945d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/distros.png)

### Questions à poser lors du choix d'une distribution

Quelques questions qui valent la peine d'être réfléchies avant de décider d'une distribution incluent :

* Quelle est la fonction principale du système (serveur ou bureau) ?
* Quels types de paquets sont importants pour l'organisation ? Par exemple, serveur web, traitement de texte, etc.
* Combien d'espace disque dur est requis et combien est disponible ? Par exemple, lors de l'installation de Linux sur un appareil embarqué, l'espace est généralement contraint.
* À quelle fréquence les paquets sont-ils mis à jour ?
* Quelle est la durée du cycle de support pour chaque version ? Par exemple, les versions **LTS** ont un support à long terme.
* Avez-vous besoin d'une personnalisation du noyau par le fournisseur ou un tiers ?
* Sur quel matériel fonctionnez-vous ? Par exemple, cela pourrait être **X86**, **ARM**, **PPC**, etc.
* Avez-vous besoin d'une stabilité à long terme ? Pouvez-vous accepter (ou avez-vous besoin) d'un système de pointe plus volatile exécutant les derniers logiciels ?

### Installation de Linux : Planification

La disposition des partitions doit être décidée au moment de l'installation ; il peut être difficile de la changer plus tard. Bien que les systèmes Linux gèrent plusieurs partitions en les montant à des points spécifiques du système de fichiers, et que vous puissiez toujours modifier la conception plus tard, il est toujours plus facile d'essayer de bien faire les choses dès le début.

![Partitions dans le disque dur Linux](https://courses.edx.org/assets/courseware/v1/ae8955c30e5b10b2fd1cab2c79673555/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen_34.jpg)
_Partitions dans le disque dur Linux_

Presque tous les installateurs fournissent une disposition par défaut raisonnable, soit avec tout l'espace dédié aux fichiers normaux sur une grande partition et une plus petite partition swap, soit avec des partitions séparées pour certaines zones sensibles à l'espace comme **/home** et **/var**. Vous devrez peut-être outrepasser les valeurs par défaut et faire quelque chose de différent si vous avez des besoins spéciaux, ou si vous voulez utiliser plus d'un disque.

### Installation de Linux : Choix de logiciels

Toutes les installations incluent le strict minimum de logiciels pour exécuter une distribution Linux.

La plupart des installateurs offrent également des options pour ajouter des catégories de logiciels. Les applications courantes (telles que le navigateur web Firefox et la suite bureautique LibreOffice), les outils de développement (comme les éditeurs de texte **vi** et **emacs**, que nous explorerons plus tard dans ce cours), et d'autres services populaires, (tels que les outils de serveur web Apache ou la base de données MySQL) sont généralement inclus. De plus, pour tout système avec un bureau graphique, un bureau choisi (tel que **GNOME** ou **KDE**) est installé par défaut.

Tous les installateurs configurent certaines fonctionnalités de sécurité initiales sur le nouveau système. Une étape de base consiste à définir le mot de passe pour le superutilisateur (root) et à configurer un utilisateur initial. Dans certains cas (comme Ubuntu), seul un utilisateur initial est configuré ; la connexion root directe n'est pas configurée et l'accès root nécessite de se connecter d'abord en tant qu'utilisateur normal puis d'utiliser **sudo**, comme nous le décrirons plus tard. Certaines distributions installeront également des cadres de sécurité plus avancés, tels que SELinux ou AppArmor. Par exemple, tous les systèmes basés sur Red Hat, y compris Fedora et CentOS, utilisent toujours SELinux par défaut, et Ubuntu est livré avec AppArmor opérationnel.

![Choix de logiciels d'installation Linux](https://courses.edx.org/assets/courseware/v1/10f3cbf30f540761b32e02764de07e5c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen_35.jpg)
_Choix de logiciels d'installation Linux_

### Installation de Linux : Source d'installation

Comme d'autres systèmes d'exploitation, les distributions Linux sont fournies sur des supports amovibles tels que des clés USB et des CD ou DVD. La plupart des distributions Linux prennent également en charge le démarrage d'une petite image et le téléchargement du reste du système via le réseau. Ces petites images sont utilisables sur des supports, ou comme images de démarrage réseau, auquel cas il est possible d'effectuer une installation sans utiliser de support local.

De nombreux installateurs peuvent effectuer une installation complètement automatiquement, en utilisant un fichier de configuration pour spécifier les options d'installation. Ce fichier est appelé un fichier Kickstart pour les systèmes basés sur Red Hat, un profil AutoYAST pour les systèmes basés sur SUSE, et un fichier Preseed pour les systèmes basés sur Debian.

Chaque distribution fournit sa propre documentation et ses propres outils pour créer et gérer ces fichiers.

![Trois images : une montrant un téléphone portable, un ordinateur et un ordinateur portable connectés au cloud ; une autre montrant un lecteur de disque avec un CD inséré ; et la dernière montrant une clé USB](https://courses.edx.org/assets/courseware/v1/1129ddea1e2fb579c9f309c8e9846b2c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen_36.jpg)

### Installation de Linux : Le processus

Le processus d'installation réel est assez similaire pour toutes les distributions.

Après avoir démarré à partir du support d'installation, l'installateur démarre et pose des questions sur la façon dont le système doit être configuré. Ces questions sont ignorées si un fichier d'installation automatique est fourni. Ensuite, l'installation est effectuée.

Enfin, l'ordinateur redémarre dans le système nouvellement installé. Sur certaines distributions, des questions supplémentaires sont posées après le redémarrage du système.

La plupart des installateurs ont l'option de télécharger et d'installer des mises à jour dans le cadre du processus d'installation ; cela nécessite un accès Internet. Sinon, le système utilise son mécanisme de mise à jour normal pour récupérer ces mises à jour une fois l'installation terminée.

### Installation de Linux : L'avertissement

Les démonstrations montrent comment installer Linux directement sur votre machine, **en effaçant tout ce qui s'y trouvait**. Bien que les démonstrations ne modifient pas votre ordinateur, suivre ces procédures dans la vie réelle effacera toutes les données actuelles.

La Fondation Linux a un document : _"Preparing Your Computer for Linux Training"_ qui décrit des méthodes alternatives d'installation de Linux sans écraser les données existantes. Vous voudrez peut-être le consulter, si vous avez besoin de préserver les informations sur votre disque dur.

Ces méthodes alternatives sont :

1. Re-partitionner votre disque dur pour libérer suffisamment d'espace pour permettre une installation en double démarrage (côte à côte) de Linux, avec votre système d'exploitation actuel.
2. Utiliser un programme hyperviseur de machine hôte (tel que les produits de VMWare ou Oracle Virtual Box) pour installer une machine virtuelle Linux cliente.
3. Démarrer et utiliser un Live CD ou une clé USB et ne pas écrire sur le disque dur du tout.

La première méthode est parfois compliquée et doit être effectuée lorsque votre confiance est élevée et que vous comprenez les étapes impliquées. Les deuxième et troisième méthodes sont assez sûres et rendent difficile d'endommager votre système.

### Vidéo : Étapes pour installer Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000300_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Étapes pour installer CentOS

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000500_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Étapes pour installer openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000500_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

## Résumé du chapitre 3

Vous avez terminé le chapitre 3. Résumons les concepts clés couverts :

* Une **partition** est une partie logique du disque.
* Un **système de fichiers** est une méthode de stockage/recherche de fichiers sur un disque dur.
* En divisant le disque dur en partitions, les données peuvent être regroupées et séparées selon les besoins. Lorsqu'une panne ou une erreur se produit, seules les données de la partition affectée seront endommagées, tandis que les données sur les autres partitions survivront probablement.
* Le processus de démarrage comporte plusieurs étapes, commençant par le BIOS, qui déclenche le chargeur d'amorçage pour démarrer le noyau Linux. De là, le système de fichiers initramfs est invoqué, ce qui déclenche le programme init pour terminer le processus de démarrage.
* Déterminer la distribution appropriée à déployer nécessite que vous fassiez correspondre vos besoins système spécifiques aux capacités des différentes distributions.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## **Chapitre 4 : Interface graphique**

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Gérer les sessions d'interface graphique.
* Effectuer des opérations de base à l'aide de l'interface graphique.
* Changer le bureau graphique pour répondre à vos besoins.

## Bureau graphique

Vous pouvez utiliser soit une **I**nterface en **L**igne de **C**ommande (**CLI**) soit une **I**nterface **G**raphique **U**tilisateur (**GUI**) lors de l'utilisation de Linux. Pour travailler en CLI, vous devez vous rappeler quels programmes et commandes sont utilisés pour effectuer des tâches, et comment obtenir rapidement et avec précision plus d'informations sur leur utilisation et leurs options. D'un autre côté, l'utilisation de l'interface graphique est souvent rapide et facile. Elle vous permet d'interagir avec votre système via des icônes graphiques et des écrans. Pour les tâches répétitives, la CLI est souvent plus efficace, tandis que l'interface graphique est plus facile à naviguer si vous ne vous souvenez pas de tous les détails ou si vous faites quelque chose rarement.

Nous apprendrons comment gérer les sessions à l'aide de l'interface graphique pour les trois familles de distributions Linux que nous couvrons le plus dans ce cours : Red Hat (CentOS, Fedora), SUSE (openSUSE) et Debian (Ubuntu, Mint). Comme nous utilisons la variante basée sur GNOME d'openSUSE plutôt que celle basée sur KDE, toutes sont en fait assez similaires. Si vous utilisez KDE (ou d'autres bureaux Linux tels que XFCE), votre expérience variera quelque peu de ce qui est montré, mais pas de manière intrinsèquement difficile, car les interfaces utilisateur ont convergé vers certains comportements bien connus sur les systèmes d'exploitation modernes. Dans les sections suivantes de ce cours, nous nous concentrerons en grand détail sur l'interface en ligne de commande, qui est à peu près la même sur toutes les distributions.

![Trois captures d'écran montrant les bureaux Ubuntu, CentOS et OpenSUSE](https://courses.edx.org/assets/courseware/v1/fe27a9c47f2e272c238dc227cb749528/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnomedts.png)
_Bureaux Ubuntu, CentOS et openSUSE_

### Système X Window

Généralement, dans un système de bureau Linux, le système X Window est chargé comme l'une des dernières étapes du processus de démarrage. Il est souvent simplement appelé X.

Un service appelé le **Gestionnaire d'affichage** (Display Manager) garde une trace des affichages fournis et charge le serveur X (ainsi appelé, car il fournit des services graphiques aux applications, parfois appelées clients X). Le gestionnaire d'affichage gère également les connexions graphiques et démarre l'environnement de bureau approprié après la connexion d'un utilisateur.

X est un logiciel assez ancien ; il remonte au milieu des années 1980 et, en tant que tel, présente certaines lacunes sur les systèmes modernes (par exemple, avec la sécurité), car il a été étiré assez loin de ses objectifs initiaux. Un système plus récent, connu sous le nom de [Wayland](https://wayland.freedesktop.org/), le remplace progressivement et est le système d'affichage par défaut pour Fedora, RHEL 8 et d'autres distributions récentes. Pour la plupart, il ressemble à X pour l'utilisateur, bien que sous le capot, il soit assez différent.

![Gestionnaire d'affichage](https://courses.edx.org/assets/courseware/v1/44717c86868ff7e9edc71c5747bb84ab/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen28.jpg)
_Gestionnaire d'affichage_

Un environnement de bureau se compose d'un gestionnaire de session, qui démarre et maintient les composants de la session graphique, et du gestionnaire de fenêtres, qui contrôle le placement et le mouvement des fenêtres, des barres de titre de fenêtre et des contrôles.

Bien que ceux-ci puissent être mélangés, généralement un ensemble d'utilitaires, un gestionnaire de session et un gestionnaire de fenêtres sont utilisés ensemble comme une unité, et ensemble fournissent un environnement de bureau transparent.

Si le gestionnaire d'affichage n'est pas démarré par défaut dans le niveau d'exécution par défaut, vous pouvez démarrer le bureau graphique différemment, après vous être connecté à une console en mode texte, en exécutant **startx** à partir de la ligne de commande. Ou, vous pouvez démarrer le gestionnaire d'affichage (**gdm**, **lightdm**, **kdm**, **xdm**, etc.) manuellement à partir de la ligne de commande. Cela diffère de l'exécution de **startx** car les gestionnaires d'affichage projetteront un écran de connexion. Nous en discutons ensuite.

![Environnement de bureau](https://courses.edx.org/assets/courseware/v1/c4a2925d0a2d22c238c9f1d91f71635b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch03_screen29.jpg)

### Démarrage de l'interface graphique

Lorsque vous installez un environnement de bureau, le gestionnaire d'affichage X démarre à la fin du processus de démarrage. Il est responsable du démarrage du système graphique, de la connexion de l'utilisateur et du démarrage de l'environnement de bureau de l'utilisateur. Vous pouvez souvent choisir parmi un choix d'environnements de bureau lors de la connexion au système.

![Main cliquant sur le bouton Connexion](https://courses.edx.org/assets/courseware/v1/b2b0c2d435bf94d2b9f10dab925967e5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen05.jpg)

Le gestionnaire d'affichage par défaut pour GNOME est appelé **gdm**. D'autres gestionnaires d'affichage populaires incluent **lightdm** (utilisé sur Ubuntu avant la version 18.04 LTS) et **kdm** (associé à KDE).

### Environnement de bureau GNOME

GNOME est un environnement de bureau populaire avec une interface utilisateur graphique facile à utiliser. Il est fourni comme environnement de bureau par défaut pour la plupart des distributions Linux, y compris Red Hat Enterprise Linux (RHEL), Fedora, CentOS, SUSE Linux Enterprise, Ubuntu et Debian. GNOME a une navigation basée sur des menus et est parfois une transition facile à accomplir pour les utilisateurs de Windows. Cependant, comme vous le verrez, l'apparence et la convivialité peuvent être assez différentes selon les distributions, même si elles utilisent toutes GNOME.

![Logo GNOME](https://courses.edx.org/assets/courseware/v1/70a3215567cf5bf6d84f1affb3ab0dfc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Ch4_Sec1_Gnome_logo.jpg)

Un autre environnement de bureau courant très important dans l'histoire de Linux et également largement utilisé est KDE, qui a souvent été utilisé en conjonction avec SUSE et openSUSE. D'autres alternatives pour un environnement de bureau incluent Unity (présent sur les anciens Ubuntu, mais toujours basé sur GNOME), XFCE et LXDE. Comme mentionné précédemment, la plupart des environnements de bureau suivent une structure similaire à GNOME, et nous nous limiterons principalement à celui-ci pour garder les choses moins complexes.

### Vidéo : Démarrage du système et connexion et déconnexion

<video controls width="100%" preload="none">

<source src="https://edx-video.net/521d4479-5b72-4a6f-b5ce-423a416fcf6a-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Arrière-plan du bureau graphique

Chaque distribution Linux est livrée avec son propre ensemble d'arrière-plans de bureau. Vous pouvez modifier la valeur par défaut en choisissant un nouveau fond d'écran ou en sélectionnant une image personnalisée à définir comme arrière-plan du bureau. Si vous ne souhaitez pas utiliser une image comme arrière-plan, vous pouvez sélectionner une couleur à afficher sur le bureau à la place.

![Ordinateur de bureau, clavier et souris](https://courses.edx.org/assets/courseware/v1/88ef9ed386547375f0aa50738e1f5af3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen63.jpg)

De plus, vous pouvez également modifier le thème du bureau, ce qui change l'apparence et la convivialité du système Linux. Le thème définit également l'apparence des fenêtres d'application.

Nous apprendrons comment changer l'arrière-plan du bureau et le thème.

### Personnalisation de l'arrière-plan du bureau

Pour changer l'arrière-plan, vous pouvez faire un clic droit n'importe où sur le bureau et choisir **Modifier l'arrière-plan**.

![Capture d'écran montrant comment personnaliser l'arrière-plan du bureau](https://courses.edx.org/assets/courseware/v1/5e5585d25c7c44efc58a7c5d7c5e6f2f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntubg.png)

### Vidéo : Comment changer l'arrière-plan du bureau

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000600_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### gnome-tweaks

La plupart des paramètres courants, à la fois personnels et à l'échelle du système, se trouvent en cliquant dans le coin supérieur droit, sur une icône d'engrenage ou une autre icône évidente, selon votre distribution Linux.

Cependant, il existe de nombreux paramètres que de nombreux utilisateurs aimeraient modifier qui ne sont pas accessibles par ce biais ; l'utilitaire de paramètres par défaut est malheureusement assez limité dans les distributions modernes basées sur GNOME. Malheureusement, la quête de simplicité a en fait rendu difficile l'adaptation de votre système à vos goûts et besoins.

Heureusement, il existe un utilitaire standard, **gnome-tweaks**, qui expose beaucoup plus d'options de réglage. Il vous permet également d'installer facilement des extensions par des tiers. Toutes les distributions Linux n'installent pas cet outil par défaut, mais il est toujours disponible (les anciennes distributions utilisaient le nom **gnome-tweak-tool**). Vous devrez peut-être l'exécuter en appuyant sur **Alt-F2** puis en tapant le nom. Vous voudrez peut-être l'ajouter à votre liste de **Favoris** comme nous en discuterons.

Comme discuté dans le chapitre suivant, certaines distributions récentes ont retiré la plupart des fonctionnalités de cet outil et les ont placées dans un nouvel outil, appelé **gnome-extensions-app**.

Dans la capture d'écran ci-dessous, le mappage du clavier est ajusté afin que la touche inutile **Verr Maj** (CapsLock) puisse être utilisée comme une touche **Ctrl** supplémentaire ; cela évite aux utilisateurs qui utilisent beaucoup **Ctrl** (comme les aficionados d'**emacs**) d'être physiquement endommagés par la fatigue du petit doigt.

![gnome-tweaks](https://courses.edx.org/assets/courseware/v1/b9aeb9e063eda9567443ab77501286d3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnometweaktool.png)
_gnome-tweaks_

### Changer le thème

L'apparence visuelle des applications (les boutons, les barres de défilement, les widgets et autres composants graphiques) est contrôlée par un **thème**. GNOME est livré avec un ensemble de thèmes différents qui peuvent changer l'apparence de vos applications.

La méthode exacte pour changer votre thème peut dépendre de votre distribution. Pour les anciennes distributions basées sur GNOME, vous pouvez simplement exécuter **gnome-tweaks**, comme indiqué dans la capture d'écran d'Ubuntu. Cependant, comme mentionné précédemment, si vous ne le trouvez pas là, vous devrez regarder **gnome-extensions-app**, qui peut maintenant configurer les thèmes. Cela nécessite d'installer encore plus de logiciels et d'aller sur des sites Web externes, il est donc peu probable que cela soit considéré comme une amélioration par de nombreux utilisateurs.

Il existe d'autres options pour obtenir des thèmes supplémentaires au-delà de la sélection par défaut. Vous pouvez télécharger et installer des thèmes à partir du site Web [Wiki de GNOME](https://wiki.gnome.org/Personalization).

![Capture d'écran montrant comment changer le thème](https://courses.edx.org/assets/courseware/v1/3b96462047b8da666c50589c7d570824/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/themesuse.png)
_Changer le thème_

## Gestion de session

### Connexion et déconnexion

L'écran suivant montre une démonstration pour se connecter et se déconnecter sur les principales familles de distributions Linux sur lesquelles nous nous concentrons dans ce cours. Notez que l'évolution nous a amenés à un stade où peu importe la distribution que vous choisissez, car elles sont toutes assez similaires.

![Boutons de connexion et de déconnexion](https://courses.edx.org/assets/courseware/v1/11ec196634ac41509995f108392b568f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen06.jpg)

### Vidéo : Connexion et déconnexion à l'aide de l'interface graphique dans Ubuntu, openSUSE et CentOS

<video controls width="100%" preload="none">

<source src="https://edx-video.net/a80a237c-bd71-4521-ac74-d85271da8103-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Verrouillage de l'écran

Il est souvent judicieux de verrouiller votre écran pour empêcher d'autres personnes d'accéder à votre session pendant que vous êtes loin de votre ordinateur.

_**NOTE**_ : Cela ne suspend pas l'ordinateur ; toutes vos applications et processus continuent de s'exécuter pendant que l'écran est verrouillé.

Il existe deux façons de verrouiller votre écran :

* Utilisation de l'interface graphique
Cliquer dans le coin supérieur droit du bureau, puis cliquer sur l'icône de cadenas.
* Utilisation du raccourci clavier SUPER-L
(La touche **SUPER** est également connue sous le nom de touche **Windows**).

Le raccourci clavier pour verrouiller l'écran peut être modifié en modifiant les paramètres du clavier, la prescription exacte variant selon la distribution, mais pas difficile à déterminer.

Pour revenir à la session de bureau, vous devez simplement fournir à nouveau votre mot de passe.

La capture d'écran ci-dessous montre comment verrouiller l'écran pour Ubuntu. Les détails varient peu dans les distributions modernes.

![Capture d'écran montrant comment verrouiller l'écran pour Ubuntu](https://courses.edx.org/assets/courseware/v1/d6ee89ab27aa5ff6a458210c8cba91b8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lockubuntu.png)

### Vidéo : Verrouillage et déverrouillage de l'écran plus en détail

<video controls width="100%" preload="none">

<source src="https://edx-video.net/fe32cdd9-570c-4bfa-a631-ab2ced0ed7cf-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Changement d'utilisateur

Linux est un véritable système d'exploitation multi-utilisateur, qui permet à plus d'un utilisateur d'être connecté simultanément. Si plus d'une personne utilise le système, il est préférable que chaque personne ait son propre compte utilisateur et mot de passe. Cela permet des paramètres individualisés, des répertoires personnels et d'autres fichiers. Les utilisateurs peuvent utiliser la machine à tour de rôle, tout en gardant les sessions de chacun actives, ou même être connectés simultanément via le réseau.

![Deux bustes de dessins animés reliés par des flèches](https://courses.edx.org/assets/courseware/v1/b68bf37dafb8f7d7e82e7143197620ef/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen18.jpg)

###
Vidéo : Changement d'utilisateur dans Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V000800_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Arrêt et redémarrage

Outre le démarrage et l'arrêt quotidiens normaux de l'ordinateur, un redémarrage du système peut être nécessaire dans le cadre de certaines mises à jour majeures du système, généralement uniquement celles impliquant l'installation d'un nouveau noyau Linux.

![Bouton d'allumage](https://courses.edx.org/assets/courseware/v1/6eea345b1964582af01d9f9d8923a608/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen26.jpg)

Lancer le processus d'arrêt à partir du bureau graphique est assez trivial sur toutes les distributions Linux actuelles, avec très peu de variations. Nous discuterons plus tard de la façon de le faire à partir de la ligne de commande, en utilisant la commande **shutdown**.

Dans tous les cas, vous cliquez sur une icône de paramètres (engrenage) ou d'alimentation et suivez les invites.

### Arrêt et redémarrage sur GNOME

Pour éteindre l'ordinateur dans toute distribution Linux récente basée sur GNOME, effectuez les étapes suivantes :

1. Cliquez soit sur l'icône **Alimentation** soit sur l'icône **Engrenage** dans le coin supérieur droit de l'écran.
2. Cliquez sur **Éteindre**, **Redémarrer** ou **Annuler**. Si vous ne faites rien, le système s'arrêtera dans 60 secondes.

Les opérations d'arrêt, de redémarrage et de déconnexion demanderont une confirmation avant de continuer. C'est parce que de nombreuses applications ne sauvegarderont pas leurs données correctement lorsqu'elles sont terminées de cette façon.

Enregistrez toujours vos documents et données avant de redémarrer, d'arrêter ou de vous déconnecter.

![Capture d'écran montrant l'arrêt et le redémarrage dans Ubuntu](https://courses.edx.org/assets/courseware/v1/d7aec4ecc99a643b6970ce88e4c7e7c5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/centos8shutdown.png)
_Arrêt et redémarrage_

### Suspension

Tous les ordinateurs modernes prennent en charge le **Mode Suspension** (ou **Veille**) lorsque vous souhaitez arrêter d'utiliser votre ordinateur pendant un certain temps. Le _Mode Suspension_ enregistre l'état actuel du système et vous permet de reprendre votre session plus rapidement tout en restant allumé, mais utilise très peu d'énergie dans l'état de veille. Il fonctionne en gardant les applications de votre système, le bureau, etc., dans la RAM du système, mais en éteignant tout le reste du matériel. Cela raccourcit le temps d'un démarrage complet du système ainsi que conserve la puissance de la batterie. Il convient de noter que les distributions Linux modernes démarrent en fait si vite que le gain de temps est souvent mineur.

Pour suspendre le système, la procédure commence de la même manière que pour l'arrêt ou le verrouillage de l'écran.

La méthode est assez simple et universelle dans la plupart des distributions récentes basées sur GNOME. Si vous cliquez sur l'icône **Alimentation** et maintenez pendant un court instant et relâchez, vous obtiendrez l'icône à double ligne affichée ci-dessous, sur laquelle vous cliquez ensuite pour suspendre le système. Certaines distributions, y compris Ubuntu, peuvent encore afficher une icône Suspendre séparée au lieu d'utiliser la méthode ci-dessus.

![Suspension du système Ubuntu](https://courses.edx.org/assets/courseware/v1/8bc873843331e65aa45bd8e71847d96f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/suspend.png)
_Suspension du système_

## Opérations de base

Même les utilisateurs expérimentés peuvent oublier la commande précise qui lance une application, ou exactement quelles options et arguments elle nécessite. Heureusement, Linux vous permet d'ouvrir rapidement des applications à l'aide de l'interface graphique.

Les applications se trouvent à différents endroits sous Linux (et au sein de GNOME) :

* Dans le menu **Applications** dans le coin supérieur gauche.
* Dans le menu **Activités** dans le coin supérieur gauche.
* Dans certaines versions d'**Ubuntu**, à partir du bouton **Dash** dans le coin supérieur gauche.
* Pour **KDE**, et certains autres environnements, les applications peuvent être ouvertes à partir du bouton dans le coin inférieur gauche.

Dans les pages suivantes, vous apprendrez à effectuer des opérations de base sous Linux à l'aide de l'interface graphique.

### Localisation des applications

Contrairement à d'autres systèmes d'exploitation, l'installation initiale de Linux est généralement livrée avec une large gamme d'applications et d'archives logicielles contenant des milliers de programmes qui vous permettent d'accomplir une grande variété de tâches avec votre ordinateur. Pour la plupart des tâches clés, une application par défaut est généralement déjà installée. Cependant, vous pouvez toujours installer plus d'applications et essayer différentes options.

Par exemple, Firefox est populaire comme navigateur par défaut dans de nombreuses distributions Linux, tandis qu'Epiphany, Konqueror et Chromium (la base open source pour Google Chrome) sont généralement disponibles pour l'installation à partir de dépôts de logiciels. Des navigateurs Web propriétaires, tels qu'Opera et Chrome, sont également disponibles.

La localisation des applications à partir des menus GNOME et KDE est facile, car elles sont soigneusement organisées en sous-menus fonctionnels.

![Localisation des applications](https://courses.edx.org/assets/courseware/v1/b24b746b71f7af714d6b07bf9074af87/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntu1910aps.png)
_Localisation des applications_

### Applications par défaut

Plusieurs applications sont disponibles pour accomplir diverses tâches et pour ouvrir un fichier d'un type donné. Par exemple, vous pouvez cliquer sur une adresse Web tout en lisant un e-mail et lancer un navigateur tel que Firefox ou Chrome.

Pour définir les applications par défaut, entrez dans le menu **Paramètres** (sur toutes les distributions Linux récentes) puis cliquez sur **Applications par défaut** ou **Détails > Applications par défaut**. La liste exacte variera de ce qui est montré ici dans la capture d'écran Ubuntu selon ce qui est réellement installé et disponible sur votre système.

![Applications par défaut](https://courses.edx.org/assets/courseware/v1/2c777f97912b2abd2ae65425ee717e2f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/defappsubuntu.png)
_Applications par défaut_

### Vidéo : Définition des applications par défaut

<video controls width="100%" preload="none">

<source src="https://edx-video.net/614af67b-a489-498e-939d-a8ca6b7f4a69-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Gestionnaire de fichiers

Chaque distribution implémente l'utilitaire **Nautilus** (**Gestionnaire de fichiers**), qui est utilisé pour naviguer dans le système de fichiers. Il peut localiser des fichiers et, lorsqu'un fichier est cliqué, soit il s'exécutera s'il s'agit d'un programme, soit une application associée sera lancée en utilisant le fichier comme données. Ce comportement est tout à fait familier à quiconque a utilisé d'autres systèmes d'exploitation.

Pour démarrer le gestionnaire de fichiers, vous devrez cliquer sur son icône (un classeur) qui est facilement trouvée, généralement sous **Favoris** ou **Accessoires**. Il aura le nom **Fichiers**.

Cela ouvrira une fenêtre avec votre répertoire **Personnel** (Home) affiché. Le panneau gauche de la fenêtre du gestionnaire de fichiers contient une liste de répertoires couramment utilisés, tels que **Bureau**, **Documents**, **Téléchargements** et **Images**.

Vous pouvez cliquer sur l'icône _Loupe_ en haut à droite pour rechercher des fichiers ou des répertoires (dossiers).

![Gestionnaire de fichiers](https://courses.edx.org/assets/courseware/v1/b3549f989a4dba1ca5720eaa3254bd15/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homefilesubuntu.png)
_Gestionnaire de fichiers_

### Répertoires personnels

Le gestionnaire de fichiers vous permet d'accéder à différents emplacements sur votre ordinateur et le réseau, y compris le répertoire **Personnel**, **Bureau**, **Documents**, **Images** et d'autres **Autres emplacements**.

Chaque utilisateur avec un compte sur le système aura un répertoire personnel, généralement créé sous **/home**, et généralement nommé selon l'utilisateur, tel que **/home/student**.

Par défaut, les fichiers que l'utilisateur enregistre seront placés dans une arborescence de répertoires commençant là. La création de compte, que ce soit lors de l'installation du système ou ultérieurement, lorsqu'un nouvel utilisateur est ajouté, induit également la création de répertoires par défaut sous le répertoire personnel de l'utilisateur, tels que **Documents**, **Bureau** et **Téléchargements**.

Dans la capture d'écran montrée pour Ubuntu, nous avons choisi le format liste et affichons également les _fichiers cachés_ (ceux commençant par un point). Voyez si vous pouvez faire de même sur votre distribution.

![Répertoires personnels](https://courses.edx.org/assets/courseware/v1/2a56d63772e3aff037135e2624dd9a37/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homefilesu1910.png)
_Répertoires personnels_

![Autres emplacements](https://courses.edx.org/assets/courseware/v1/6c854e3e52c67c75ffa29d8bdfcf8f77/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/otherfilesu1910.png)
_Autres emplacements_

### Visualisation des fichiers

Le gestionnaire de fichiers vous permet de visualiser les fichiers et les répertoires de plus d'une manière.

Vous pouvez basculer entre les formats Icônes et Liste, soit en cliquant sur les icônes familières dans la barre supérieure, soit en appuyant sur **CTRL-1** ou **CTRL-2** respectivement.

De plus, vous pouvez également organiser les fichiers et les répertoires par nom, taille, type ou date de modification pour un tri supplémentaire. Pour ce faire, cliquez sur **Affichage** et sélectionnez **Organiser les éléments**.

Une autre option utile est d'afficher les _fichiers cachés_ (parfois appelés imprécisément fichiers système), qui sont généralement des fichiers de configuration qui sont cachés par défaut et dont le nom commence par un point. Pour afficher les fichiers cachés, sélectionnez **Afficher les fichiers cachés** dans le menu ou appuyez sur **CTRL-H**.

Le navigateur de fichiers offre plusieurs façons de personnaliser votre vue de fenêtre pour faciliter les opérations de glisser-déposer de fichiers. Vous pouvez également modifier la taille des icônes en sélectionnant **Zoom avant** et **Zoom arrière** dans le menu _Affichage_.

![Visualisation des fichiers dans openSUSE](https://courses.edx.org/assets/courseware/v1/59b49f03cf57ecaf483df8f2f06f32b9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homefilessuse.png)

### Recherche de fichiers

Le gestionnaire de fichiers comprend un excellent outil de recherche à l'intérieur de la fenêtre du navigateur de fichiers.

1. Cliquez sur **Rechercher** dans la barre d'outils (pour faire apparaître une zone de texte).
2. Entrez le mot-clé dans la zone de texte. Cela amène le système à effectuer une recherche récursive à partir du répertoire actuel pour tout fichier ou répertoire contenant une partie de ce mot-clé.

Pour ouvrir le _Gestionnaire de fichiers_ à partir de la ligne de commande, sur la plupart des systèmes, tapez simplement **nautilus**.

![Loupe](https://courses.edx.org/assets/courseware/v1/2ba30c1757235e33a807500b1af9da42/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen48.jpg)

Le raccourci clavier pour accéder à la zone de texte de recherche est **CTRL-F**. Vous pouvez quitter la vue de la zone de texte de recherche en cliquant à nouveau sur le bouton _Rechercher_ ou **CTRL-F**.

Un autre moyen rapide d'accéder à un répertoire spécifique est d'appuyer sur **CTRL-L**, ce qui vous donnera une zone de texte **Emplacement** pour taper un chemin vers un répertoire.

### Plus sur la recherche de fichiers

Vous pouvez affiner votre recherche au-delà du mot-clé initial en fournissant des menus déroulants pour filtrer davantage la recherche.

1. Basé sur **Emplacement** ou **Type de fichier**, sélectionnez des critères supplémentaires dans la liste déroulante.
2. Pour régénérer la recherche, cliquez sur le bouton **Recharger**.
3. Pour ajouter plusieurs critères de recherche, cliquez sur le bouton **+** et sélectionnez _Critères de recherche supplémentaires_.

Par exemple, si vous souhaitez trouver un fichier PDF contenant le mot **Linux** dans votre répertoire personnel, accédez à votre répertoire **personnel** et recherchez le mot "Linux". Vous devriez voir que le critère de recherche par défaut limite déjà la recherche à votre répertoire **personnel**. Pour terminer le travail, cliquez sur le bouton **+** pour ajouter un autre critère de recherche, sélectionnez **Type de fichier** pour le type de critère, et sélectionnez **PDF** sous la liste déroulante **Type de fichier**.

![Capture d'écran montrant comment rechercher des fichiers en fonction de différents critères](https://courses.edx.org/assets/courseware/v1/92b46e00f94ca300fff886db41b6d2d3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/searchubuntu.png)
_Recherche de fichiers_

### Édition d'un fichier

L'édition de n'importe quel fichier texte via l'interface graphique est facile dans l'environnement de bureau GNOME. Double-cliquez simplement sur le fichier sur le bureau ou dans la fenêtre du navigateur de fichiers Nautilus pour ouvrir le fichier avec l'éditeur de texte par défaut.

![icône gedit](https://courses.edx.org/assets/courseware/v1/e47912c6805c7126aef11b9e4c5b8713/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen50.jpg)

L'éditeur de texte par défaut dans GNOME est **gedit**. Il est simple mais puissant, idéal pour éditer des documents, prendre des notes rapides et programmer. Bien que **gedit** soit conçu comme un éditeur de texte généraliste, il offre des fonctionnalités supplémentaires pour la vérification orthographique, la mise en évidence, les listes de fichiers et les statistiques.

Vous en apprendrez beaucoup plus sur l'utilisation des éditeurs de texte dans un chapitre ultérieur.

### Suppression d'un fichier

La suppression d'un fichier dans Nautilus déplacera automatiquement les fichiers supprimés vers le répertoire **.local/share/Trash/files/** (une sorte de corbeille) sous le répertoire personnel de l'utilisateur. Il existe plusieurs façons de supprimer des fichiers et des répertoires à l'aide de Nautilus.

1. Sélectionnez tous les fichiers et répertoires que vous souhaitez supprimer.
2. Appuyez sur **CTRL-Suppr** sur votre clavier, ou faites un clic droit sur le fichier.
3. Sélectionnez **Mettre à la corbeille**.

Notez que vous pouvez avoir une option **Supprimer définitivement** qui contourne le dossier corbeille, et que cette option peut être visible tout le temps ou uniquement en mode liste (plutôt qu'icône).

![Corbeille](https://courses.edx.org/assets/courseware/v1/7384e7b0992fc01be5544b2d30992425/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch04_screen52.jpg)

Pour supprimer _définitivement_ un fichier :

1. Sur le panneau gauche à l'intérieur d'une fenêtre de navigateur de fichiers Nautilus, faites un clic droit sur le répertoire **Corbeille**.
2. Sélectionnez _Vider la corbeille_.

Alternativement, sélectionnez le fichier ou le répertoire que vous souhaitez supprimer définitivement et appuyez sur **Maj-Suppr**.

Par précaution, vous ne devriez jamais supprimer votre répertoire _Personnel_, car cela effacera très probablement tous vos fichiers de configuration GNOME et vous empêchera peut-être de vous connecter. De nombreuses configurations personnelles du système et des programmes sont stockées sous votre répertoire personnel.

### Vidéo : Localisation et définition des applications par défaut, et exploration des systèmes de fichiers dans openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001000_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

## Résumé du chapitre 4

Vous avez terminé le chapitre 4. Résumons les concepts clés couverts :

* **GNOME** est un environnement de bureau populaire et une interface utilisateur graphique qui fonctionne au-dessus du système d'exploitation Linux.
* Le gestionnaire d'affichage par défaut pour GNOME est appelé **gdm**.
* Le gestionnaire d'affichage gdm présente à l'utilisateur l'écran de connexion, qui demande le nom d'utilisateur et le mot de passe de connexion.
* La déconnexion via l'environnement de bureau tue tous les processus de votre session **X** actuelle et revient à l'écran de connexion du gestionnaire d'affichage.
* Linux permet aux utilisateurs de basculer entre les sessions connectées.
* La suspension met l'ordinateur en mode veille.
* Pour chaque tâche clé, il y a généralement une application par défaut installée.
* Chaque utilisateur créé dans le système aura un répertoire **personnel**.
* Le menu _Emplacements_ contient des entrées qui vous permettent d'accéder à différentes parties de l'ordinateur et du réseau.
* **Nautilus** donne trois formats pour visualiser les fichiers.
* La plupart des éditeurs de texte sont situés dans le sous-menu _Accessoires_.
* Chaque distribution Linux est livrée avec son propre ensemble d'arrière-plans de bureau.
* GNOME est livré avec un ensemble de thèmes différents qui peuvent changer l'apparence de vos applications.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

#

## **Chapitre 5 : Configuration du système depuis l'interface graphique**

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Appliquer les paramètres système, d'affichage, et de date et heure à l'aide du panneau _Paramètres système_.
* Suivre les paramètres réseau et gérer les connexions à l'aide de _Network Manager_ sous Linux.
* Installer et mettre à jour des logiciels sous Linux à partir d'une interface graphique.

_**NOTE**_ : Nous reviendrons sur toutes ces tâches plus tard, lorsque nous discuterons de la façon de les accomplir à partir de l'interface en ligne de commande.

## Paramètres système, d'affichage, de date et d'heure

Le panneau **Paramètres système** vous permet de contrôler la plupart des options de configuration de base et des paramètres du bureau, tels que la spécification de la résolution de l'écran, la gestion des connexions réseau ou la modification de la date et de l'heure du système.

Pour le gestionnaire de bureau GNOME, on clique sur le coin supérieur droit, puis on sélectionne l'image des outils (tournevis croisé avec une clé ou un engrenage). Selon votre distribution, vous pouvez également trouver d'autres moyens d'accéder à la configuration des paramètres. Vous trouverez également des variations dans la disposition des menus entre les distributions et les versions Linux, vous devrez donc peut-être chercher les paramètres que vous devez examiner ou modifier.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-410.png)
_Panneau Paramètres système_

### Menus des paramètres système

Pour aller plus loin dans la configuration, on peut cliquer sur _Périphériques_ dans le menu précédent afin de configurer des éléments comme l'affichage, le clavier, les imprimantes, etc.

![Configuration des applications sur Ubuntu](https://courses.edx.org/assets/courseware/v1/37875055d2d8368b6c8b2edd1af73ace/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntusetapps.png)
_Configuration des applications sur Ubuntu_

On peut également cliquer sur l'icône _Utilisateurs_ (qui peut être sous _Détails_) pour définir des valeurs pour les utilisateurs du système, telles que leur image de connexion, mot de passe, etc.

![Configuration des attributs utilisateur](https://courses.edx.org/assets/courseware/v1/9f2a5b8ed015a7d39f6b15df59b78c98/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntuuserconfig.png)
_Configuration des attributs utilisateur_

### gnome-tweaks

De nombreux paramètres de configuration personnalisés n'apparaissent pas dans les menus de paramètres. Au lieu de cela, vous devez lancer un outil appelé soit **gnome-tweaks** (ou **gnome-tweak-tool** sur les anciennes distributions Linux). Nous n'avons pas vraiment discuté du travail en ligne de commande encore, mais vous pouvez toujours lancer un programme comme celui-ci en faisant **Alt-F2** et en tapant la commande. Certaines distributions ont un lien vers les menus tweaks dans les paramètres, mais pour une raison mystérieuse, beaucoup obscurcissent l'existence de cet outil, et il devient difficile de découvrir comment modifier même des attributs et comportements de bureau assez basiques.

Les choses importantes que vous pouvez faire avec cet outil incluent la sélection d'un **thème**, la configuration des **extensions** que vous pouvez obtenir de votre distribution ou télécharger sur Internet, le contrôle des polices, la modification de la disposition du clavier et la définition des programmes qui démarrent lorsque vous vous connectez.

Les versions les plus récentes de GNOME ont supprimé une grande partie des fonctionnalités de **gnome-tweaks** ; les extensions doivent maintenant être configurées à l'aide d'une nouvelle application appelée **gnome-extensions-app**. Le raisonnement derrière cela est obscur.

La capture d'écran ici provient d'un système Red Hat avec pas mal d'extensions installées, mais pas toutes utilisées.

![Extensions installées sur RHEL](https://courses.edx.org/assets/courseware/v1/206249c2dbef56d193c9a2e4a7a97b2f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnometweaks.png)
_Extensions installées sur RHEL_

### Paramètres d'affichage

Cliquer sur **Paramètres > Écrans** (ou **Paramètres > Périphériques > Écrans**) exposera les paramètres les plus courants pour changer l'apparence du bureau. Ces paramètres fonctionnent indépendamment des pilotes d'affichage spécifiques que vous exécutez. L'apparence exacte dépendra énormément du nombre de moniteurs que vous avez et d'autres facteurs, tels que la distribution Linux et la version particulière.

Si votre système utilise un pilote de carte vidéo propriétaire (généralement de **nVidia** ou **AMD**), vous aurez probablement un programme de configuration séparé pour ce pilote. Ce programme peut donner plus d'options de configuration, mais peut aussi être plus compliqué, et pourrait nécessiter un accès administrateur système (root). Si possible, vous devriez configurer les paramètres dans le panneau **Écrans** plutôt qu'avec le programme propriétaire.

Le serveur X, qui fournit réellement l'interface graphique, utilise **/etc/X11/xorg.conf** comme fichier de configuration _s'il existe_ ; Dans les distributions Linux modernes, ce fichier n'est généralement présent que dans des circonstances inhabituelles, comme lorsque certains pilotes graphiques moins courants sont utilisés. Changer ce fichier de configuration directement est généralement pour les utilisateurs plus avancés.

![Paramètres d'affichage sur un système Ubuntu plus ancien et plus récent](https://courses.edx.org/assets/courseware/v1/c2af77e8b90d9b4213a8ec8218838999/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Display_Settings_on_an_Older_and_Newer_Ubuntu_Systems.png)
_Paramètres d'affichage sur un système Ubuntu plus ancien et plus récent_

### Réglage de la résolution et configuration de plusieurs écrans

Bien que votre système déterminera généralement la meilleure résolution pour votre écran automatiquement, il peut se tromper dans certains cas, ou vous pourriez vouloir changer la résolution pour répondre à vos besoins.

Vous pouvez accomplir cela en utilisant le panneau _Écrans_. Le passage à la nouvelle résolution sera effectif lorsque vous cliquerez sur _Appliquer_, puis confirmerez que la résolution fonctionne. Au cas où la résolution sélectionnée ne fonctionnerait pas ou que vous ne seriez tout simplement pas satisfait de l'apparence, le système reviendra à la résolution d'origine après un court délai. Encore une fois, l'apparence exacte de l'écran de configuration variera beaucoup entre les distributions et les versions, mais est généralement assez intuitive et facile, une fois que vous avez trouvé les menus de configuration.

Dans la plupart des cas, la configuration pour plusieurs écrans est configurée automatiquement comme un grand écran s'étendant sur tous les moniteurs, en utilisant une estimation raisonnable pour la disposition de l'écran. Si la disposition de l'écran n'est pas celle souhaitée, une case à cocher peut activer le mode miroir, où le même affichage est vu sur tous les moniteurs. Cliquer sur une image de moniteur particulière vous permet de configurer la résolution de chacun, et s'ils forment un grand écran, ou reflètent la même vidéo, etc.

![Réglage de la résolution et configuration de plusieurs écrans](https://courses.edx.org/assets/courseware/v1/c9815d9b551a9d4bc8f71530471ae097/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/multidisplayrhel8.png)
_Réglage de la résolution et configuration de plusieurs écrans_

### Vidéo : Configuration des paramètres d'affichage

<video controls width="100%" preload="none">

<source src="https://edx-video.net/9adfb9c8-07d7-4910-92ce-b3168692e082-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Paramètres de date et d'heure

Par défaut, Linux utilise toujours le temps universel coordonné (UTC) pour son propre chronométrage interne. Les valeurs de temps affichées ou stockées dépendent du paramètre de fuseau horaire du système pour obtenir l'heure correcte. UTC est similaire à, mais plus précis que, l'heure moyenne de Greenwich (GMT).

Si vous cliquez sur l'heure affichée sur le panneau supérieur, vous pouvez ajuster le format avec lequel la date et l'heure sont affichées ; sur certaines distributions, vous pouvez également modifier les valeurs.

Les paramètres de date et d'heure plus détaillés peuvent être sélectionnés à partir de la fenêtre **Date et heure** dans le menu Paramètres système.

![Capture d'écran montrant les paramètres de date et d'heure dans Ubuntu](https://courses.edx.org/assets/courseware/v1/fafa9bab5da6a86410f8a8ad98278e34/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntudate.png)
_Paramètres de date et d'heure_

Les paramètres "automatiques" font référence à l'utilisation du protocole de temps réseau (NTP), dont nous discutons ensuite.

### Protocole de temps réseau

Le **N**etwork **T**ime **P**rotocol (**NTP**) est le protocole le plus populaire et le plus fiable pour régler l'heure locale en consultant des serveurs Internet établis. Les distributions Linux sont toujours livrées avec une configuration NTP fonctionnelle, qui fait référence à des serveurs de temps spécifiques gérés ou utilisés par la distribution. Cela signifie qu'aucune configuration, au-delà de "on" ou "off", n'est généralement requise pour la synchronisation de l'heure réseau.

![Image montrant différents types de montres](https://courses.edx.org/assets/courseware/v1/6559d606ae7043ce2a92fc4b5b17cdf9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen11.jpg)

### Configuration réseau

Toutes les distributions Linux ont des fichiers de configuration réseau, mais les formats de fichiers et les emplacements peuvent différer d'une distribution à l'autre. L'édition manuelle de ces fichiers peut gérer des configurations assez compliquées, mais n'est pas très dynamique ou facile à apprendre et à utiliser. **Network Manager** a été développé pour rendre les choses plus faciles et plus uniformes entre les distributions. Il peut lister tous les réseaux disponibles (filaires et sans fil), permettre le choix d'un réseau filaire, sans fil ou haut débit mobile, gérer les mots de passe et configurer des réseaux privés virtuels (VPN). Sauf pour des situations inhabituelles, il est généralement préférable de laisser Network Manager établir vos connexions et garder une trace de vos paramètres.

![Configuration réseau](https://courses.edx.org/assets/courseware/v1/427ccf47dacf228ee1d15672b07d0ad2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen18.jpg)
_Configuration réseau_

Dans cette section, vous apprendrez à gérer les connexions réseau, y compris les connexions filaires et sans fil, et les connexions haut débit mobile et VPN.

### Connexions filaires et sans fil

Les connexions filaires ne nécessitent généralement pas de configuration compliquée ou manuelle. L'interface matérielle et la présence du signal sont automatiquement détectées, puis Network Manager définit les paramètres réseau réels via **D**ynamic **H**ost **C**onfiguration **P**rotocol (DHCP).

Pour les configurations **statiques** qui n'utilisent pas DHCP, la configuration manuelle peut également être effectuée facilement via Network Manager. Vous pouvez également modifier l'adresse Ethernet **M**edia **A**ccess **C**ontrol (MAC) si votre matériel le prend en charge. L'adresse MAC est un nombre hexadécimal unique de votre carte réseau.

![Connexions filaires et sans fil](https://courses.edx.org/assets/courseware/v1/34c61d5ecb1a4f58b5729603e08b9995/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen19.jpg)

Les réseaux sans fil ne sont généralement pas connectés par défaut. Vous pouvez afficher la liste des réseaux sans fil disponibles et voir lequel (le cas échéant) vous êtes actuellement connecté en utilisant Network Manager. Vous pouvez ensuite ajouter, modifier ou supprimer des réseaux sans fil connus, et également spécifier ceux que vous souhaitez connecter par défaut lorsqu'ils sont présents.

### Configuration des connexions sans fil

Pour configurer un réseau sans fil dans toute distribution récente basée sur GNOME :

Cliquez sur le coin supérieur droit du panneau supérieur, ce qui fait apparaître une fenêtre de paramètres et/ou de réseau. Bien que l'apparence exacte dépende de la distribution Linux et de la version, il sera toujours possible de cliquer sur un sous-menu **Wi-Fi**, tant que le matériel est présent. Voici un exemple d'un système RHEL 8 :

![Configuration des connexions sans fil](https://courses.edx.org/assets/courseware/v1/8f9f84c03fd872a5c510fb1370ea0933/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wifi1.png)
_Configuration des connexions sans fil_

Sélectionnez le réseau sans fil auquel vous souhaitez vous connecter. S'il s'agit d'un réseau sécurisé, la première fois, il vous demandera d'entrer le mot de passe approprié. Par défaut, le mot de passe sera enregistré pour les connexions ultérieures.

![Sélection d'un réseau](https://courses.edx.org/assets/courseware/v1/ab20057497c4be2af101ade999d0bd52/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wifi2.png)
_Sélection d'un réseau_

Si vous cliquez sur **Paramètres Wi-Fi**, vous ferez apparaître la troisième capture d'écran. Si vous cliquez sur l'icône **Engrenage** pour n'importe quelle connexion, vous pouvez la configurer plus en détail.

![Configuration du réseau de votre choix](https://courses.edx.org/assets/courseware/v1/bd0d58ae53ee5b9cc0705679b7e4cf9c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wifi3.png)
_Configuration du réseau de votre choix_

Les distributions Linux plus anciennes et autres peuvent sembler un peu différentes dans les détails, mais les étapes et les choix sont essentiellement identiques, car elles exécutent toutes Network Manager avec peut-être un habillage quelque peu différent.

### Vidéo : Gestion des paramètres réseau

<video controls width="100%" preload="none">

<source src="https://edx-video.net/704c77f7-c31b-4aab-996f-cafbd84e72a7-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Connexions haut débit mobile et VPN

Vous pouvez configurer une connexion haut débit mobile avec Network Manager, qui lancera un assistant pour configurer les détails de connexion pour chaque connexion.

Une fois la configuration terminée, le réseau est configuré automatiquement chaque fois que le réseau haut débit est attaché.

![Image montrant des ordinateurs portables, des tablettes et des téléphones portables connectés par des lignes](https://courses.edx.org/assets/courseware/v1/c747395ba6d725293f45c70acc201e93/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen26.jpg)

Network Manager peut également gérer vos connexions VPN.

Il prend en charge de nombreuses technologies VPN, telles que IPSec natif, Cisco OpenConnect (via le client Cisco ou un client open source natif), Microsoft PPTP et OpenVPN.

Vous pourriez obtenir un support pour VPN sous forme de paquet séparé de votre distributeur. Vous devez installer ce paquet si votre VPN préféré n'est pas pris en charge.

### Installation et mise à jour de logiciels

Chaque paquet dans une distribution Linux fournit une pièce du système, telle que le noyau Linux, le compilateur **C**, des utilitaires pour manipuler du texte ou configurer le réseau, ou pour vos navigateurs Web et clients de messagerie préférés.

Les paquets dépendent souvent les uns des autres. Par exemple, parce que votre client de messagerie peut communiquer en utilisant SSL/TLS, il dépendra d'un paquet qui fournit la capacité de chiffrer et déchiffrer la communication SSL et TLS, et ne s'installera pas à moins que ce paquet ne soit également installé en même temps.

![Pingouin de dessin animé portant des livres](https://courses.edx.org/assets/courseware/v1/277740a799bbd78d92f99ef9acc4e8db/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen33.jpg)

Tous les systèmes ont un utilitaire de bas niveau qui gère les détails du déballage d'un paquet et de la mise en place des pièces aux bons endroits. La plupart du temps, vous travaillerez avec un utilitaire de plus haut niveau qui sait comment télécharger des paquets depuis Internet et peut gérer les dépendances et les groupes pour vous.

Dans cette section, vous apprendrez à installer et mettre à jour des logiciels sous Linux en utilisant le système de paquets Debian (utilisé par des systèmes tels qu'Ubuntu également) et les systèmes de paquets RPM (qui est utilisé par les familles de systèmes Red Hat et SUSE). Ce sont les principaux utilisés bien qu'il y en ait d'autres qui fonctionnent bien pour d'autres distributions moins utilisées.

### Paquetage Debian

Regardons la gestion des paquets pour le système de la famille Debian.

**dpkg** est le gestionnaire de paquets sous-jacent pour ces systèmes. Il peut installer, supprimer et construire des paquets. Contrairement aux systèmes de gestion de paquets de plus haut niveau, il ne télécharge pas et n'installe pas automatiquement les paquets et ne satisfait pas leurs dépendances.

![Gestion des paquets dans le système de la famille Debian](https://courses.edx.org/assets/courseware/v1/c3ddb34d7f243624f888143c74665a94/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen34.jpg)
_Gestion des paquets dans le système de la famille Debian_

Pour les systèmes basés sur Debian, le système de gestion de paquets de plus haut niveau est le système d'utilitaires **A**dvanced **P**ackage **T**ool (APT). Généralement, bien que chaque distribution au sein de la famille Debian utilise APT, elle crée sa propre interface utilisateur par-dessus (par exemple, apt et apt-get, synaptic, gnome-software, Ubuntu Software Center, etc). Bien que les dépôts apt soient généralement compatibles entre eux, les logiciels qu'ils contiennent ne le sont généralement pas. Par conséquent, la plupart des dépôts ciblent une distribution particulière (comme Ubuntu), et souvent les distributeurs de logiciels livrent avec plusieurs dépôts pour prendre en charge plusieurs distributions. Des démonstrations sont présentées plus loin dans cette section.

### Red Hat Package Manager (RPM)

Red Hat Package Manager (RPM) est l'autre système de gestion de paquets populaire sur les distributions Linux. Il a été développé par Red Hat et adopté par un certain nombre d'autres distributions, y compris SUSE/openSUSE, Mageia, CentOS, Oracle Linux et d'autres.

![Red Hat Package Manager](https://courses.edx.org/assets/courseware/v1/d803cf81ee0659af701365b16aebcb3a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen35.jpg)
_Red Hat Package Manager_

Le gestionnaire de paquets de plus haut niveau diffère entre les distributions. Les distributions de la famille Red Hat utilisent historiquement RHEL/CentOS et Fedora utilise dnf, tout en conservant une bonne compatibilité ascendante avec l'ancien programme yum. Les distributions de la famille SUSE telles qu'openSUSE utilisent également RPM, mais utilisent l'interface zypper.

### Gestion de logiciels YaST d'openSUSE

Le gestionnaire de logiciels **Y**et **a**nother **S**etup **T**ool (YaST) est similaire aux autres gestionnaires de paquets graphiques. C'est une application basée sur RPM. Vous pouvez ajouter, supprimer ou mettre à jour des paquets à l'aide de cette application très facilement. Pour accéder au gestionnaire de logiciels YaST :

1. Cliquez sur **Activités**
2. Dans la zone de **Recherche**, tapez **YaST**
3. Cliquez sur l'icône **YaST**
4. Cliquez sur **Gestion de logiciels**

Vous pouvez également trouver YaST en cliquant sur **Applications > Autre-YaST**, ce qui est un endroit étrange pour le mettre.

![Gestion de logiciels d'openSUSE](https://courses.edx.org/assets/courseware/v1/3daba44866ca7ac7880f9eb6e74bc467/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch05_screen36.jpg)
_Gestion de logiciels d'openSUSE_

L'application de gestion de logiciels YaST d'openSUSE est similaire aux gestionnaires de paquets graphiques dans d'autres distributions. Une démonstration du gestionnaire de logiciels YaST est présentée plus loin dans cette section.

### Vidéo : Installation et mise à jour de logiciels dans openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001400_DTH.mp4"
        type="video/mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Installation et mise à jour de logiciels dans Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/0f1c4770-518a-416f-87ef-c1d515e4023f-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

## Résumé du chapitre 5

Vous avez terminé le chapitre 5. Résumons les concepts clés couverts :

* Vous pouvez contrôler les options de configuration de base et les paramètres du bureau via le panneau _Paramètres système_.
* Linux utilise toujours le temps universel coordonné (UTC) pour son propre chronométrage interne. Vous pouvez définir les paramètres de date et d'heure à partir de la fenêtre _Paramètres système_.
* Le protocole de temps réseau est le protocole le plus populaire et le plus fiable pour régler l'heure locale via des serveurs Internet.
* Le panneau _Écrans_ vous permet de modifier la résolution de votre écran et de configurer plusieurs écrans.
* Network Manager peut présenter les réseaux sans fil disponibles, permettre le choix d'un réseau sans fil ou haut débit mobile, gérer les mots de passe et configurer des VPN.
* **dpkg** et **RPM** sont les systèmes de gestion de paquets les plus populaires utilisés sur les distributions Linux.
* Les distributions Debian utilisent des utilitaires basés sur **dpkg** et **apt** pour la gestion des paquets.
* RPM a été développé par Red Hat et adopté par un certain nombre d'autres distributions, y compris openSUSE, Mandriva, CentOS, Oracle Linux et d'autres.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## **Chapitre 6 : Applications courantes**

À la fin de ce chapitre, vous devriez être familier avec les applications Linux courantes, notamment :

* Les applications Internet telles que les navigateurs et les programmes de messagerie.
* Les suites de productivité bureautique telles que LibreOffice.
* Les outils de développement, tels que les compilateurs, les débogueurs, etc.
* Les applications multimédias, telles que celles pour l'audio et la vidéo.
* Les éditeurs graphiques tels que GIMP et d'autres utilitaires graphiques.

## Applications Internet

Internet est un réseau mondial qui permet aux utilisateurs du monde entier d'effectuer de multiples tâches, telles que la recherche de données, la communication par e-mails et les achats en ligne. Évidemment, vous devez utiliser des applications compatibles réseau pour profiter d'Internet. Celles-ci incluent :

* Navigateurs Web
* Clients de messagerie
* Applications de streaming multimédia
* Chats Internet Relay (IRC)
* Logiciels de conférence

![Applications Internet](https://courses.edx.org/assets/courseware/v1/9ab13d93d41e76edae95a90f12c96dd3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch17_screen03.jpg)
_Applications Internet_

### Navigateurs Web

Comme discuté dans le chapitre _Interface graphique_, Linux offre une grande variété de navigateurs Web, à la fois graphiques et textuels, notamment :

* Firefox
* Google Chrome
* Chromium
* Epiphany (renommé web)
* Konqueror
* linx, lynx, w3m
* Opera

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-31.png)

###
Applications de messagerie

Les applications de messagerie permettent d'envoyer, de recevoir et de lire des messages sur Internet. Les systèmes Linux offrent un grand nombre de clients de messagerie, à la fois graphiques et textuels. De plus, de nombreux utilisateurs utilisent simplement leurs navigateurs pour accéder à leurs comptes de messagerie.

La plupart des clients de messagerie utilisent le protocole d'accès aux messages Internet (IMAP) ou l'ancien protocole de bureau de poste (POP) pour accéder aux e-mails stockés sur un serveur de messagerie distant. La plupart des applications de messagerie affichent également des e-mails formatés en HTML (HyperText Markup Language) qui affichent des objets, tels que des images et des hyperliens. Les fonctionnalités des applications de messagerie avancées incluent la possibilité d'importer des carnets d'adresses/listes de contacts, des informations de configuration et des e-mails à partir d'autres applications de messagerie.

Linux prend en charge les types d'applications de messagerie suivants :

* Clients de messagerie graphiques, tels que Thunderbird, Evolution et Claws Mail.
* Clients de messagerie en mode texte, tels que Mutt et mail.
* Tous les clients basés sur un navigateur Web, tels que Gmail, Yahoo Mail et Office 365.

![Applications de messagerie](https://courses.edx.org/assets/courseware/v1/7ea5bcb37db44af78b8e56e6f351fc00/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch17_screen05.jpg)
_Applications de messagerie_

### Autres applications Internet

Les systèmes Linux fournissent de nombreuses autres applications pour effectuer des tâches liées à Internet. Celles-ci incluent :

<table align="left" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Application</strong></span></td><td align="center" bgcolor="#003f60" width="85%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">FileZilla</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Client FTP graphique intuitif qui prend en charge FTP, Secure File Transfer Protocol (SFTP) et FTP Secured (FTPS).<span>&nbsp;</span>Utilisé pour transférer des fichiers vers/depuis des serveurs (FTP).</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Pidgin</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour accéder à GTalk, AIM, ICQ, MSN, IRC et d'autres réseaux de messagerie.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Ekiga</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour se connecter aux réseaux Voice over Internet Protocol (VoIP).</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Hexchat</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour accéder aux réseaux Internet Relay<span>&nbsp;</span>Chat (IRC).</td></tr></tbody></table>

![Logo FileZilla](https://courses.edx.org/assets/courseware/v1/f9dff170755a23939c284386a7ceed60/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/save-website-ftp-login-credentials-filezilla.png)

![Logo Pidgin](https://courses.edx.org/assets/courseware/v1/fc25e3da569679a9515327f5fe570f00/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Pidgin-Chat-App-logo.png)

![Logo xChat](https://courses.edx.org/assets/courseware/v1/bf94cb9811a89ffa464df7c9d963df57/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Xchat_mongol.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-32.png)

### Applications bureautiques

La plupart des systèmes informatiques quotidiens ont des applications de productivité (parfois appelées suites bureautiques) disponibles ou installées. Chaque suite est une collection de programmes étroitement couplés utilisés pour créer et éditer différents types de fichiers tels que :

* Texte (articles, livres, rapports, etc.)
* Feuilles de calcul
* Présentations
* Objets graphiques.

La plupart des distributions Linux proposent LibreOffice, une suite bureautique open source qui a débuté en 2010 et a évolué à partir d'OpenOffice. Bien que d'autres suites bureautiques soient disponibles comme nous l'avons indiqué, LibreOffice est la plus mature, la plus utilisée et la plus intensément développée.

De plus, les utilisateurs de Linux ont un accès complet aux suites bureautiques basées sur Internet telles que Google Docs et Microsoft Office 365.

![Logo LibreOffice](https://courses.edx.org/assets/courseware/v1/6f2b4af8b24fd4702c5b9a48e5310cd2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LibreOffice_external_logo_600px.png)

### Composants LibreOffice

Les applications composantes incluses dans LibreOffice sont :

* Writer : Traitement de texte
* Calc : Feuilles de calcul
* Impress : Présentations
* Draw : Créer et éditer des graphiques et des diagrammes.

Les applications LibreOffice peuvent lire et écrire des formats de documents non natifs, tels que ceux utilisés par Microsoft Office. Généralement, la fidélité est assez bien maintenue, mais les documents compliqués peuvent avoir des conversions imparfaites.

![Capture d'écran de la suite bureautique LibreOffice](https://courses.edx.org/assets/courseware/v1/208b36f99828ebe377c49dbbde60e4bc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/libreoffice.png)
_Applications LibreOffice_

### Applications de développement

Les distributions Linux sont livrées avec un ensemble complet d'applications et d'outils nécessaires à ceux qui développent ou maintiennent à la fois des applications utilisateur et le noyau lui-même.

Ces outils sont étroitement intégrés et comprennent :

* Éditeurs avancés personnalisés pour les besoins des programmeurs, tels que vi et emacs.
* Compilateurs (tels que gcc et clang pour les programmes en C et C++) pour chaque langage informatique ayant jamais existé, y compris les nouveaux très populaires tels que Golang et Rust.
* Débogueurs tels que gdb et diverses interfaces graphiques pour celui-ci et de nombreux autres outils de débogage (tels que Valgrind).
* Programmes de mesure et de surveillance des performances, certains avec des interfaces graphiques faciles à utiliser, d'autres plus arcanes et destinés à être utilisés uniquement par des ingénieurs de développement expérimentés sérieux.
* Environnements de développement intégrés complets (IDE) tels qu'Eclipse et Visual Studio Code qui rassemblent tous ces outils.

Sur d'autres systèmes d'exploitation, ces outils doivent être obtenus et installés séparément, souvent à un coût élevé, alors que sous Linux, ils sont tous disponibles gratuitement via des systèmes d'installation de paquets standard.

![Logo gcc](https://courses.edx.org/assets/courseware/v1/563456f06696ec4ab148bdd5ac68c9f0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gccegg-65.png)

![Logo gdb](https://courses.edx.org/assets/courseware/v1/2694164dcff3b59bee56c60eab76e8d4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gdb-logo.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-33.png)

### Lecteurs audio

Les applications multimédias sont utilisées pour écouter de la musique, regarder des vidéos, etc., ainsi que pour présenter et visualiser du texte et des graphiques. Les systèmes Linux offrent un certain nombre d'applications de lecture audio, notamment :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto 20px 0px; font-size: 16px; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Application</strong></span></td><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Amarok</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Lecteur MP3 mature avec une interface graphique, qui lit des fichiers audio et vidéo, et des flux (fichiers audio en ligne). Il vous permet de créer une liste de lecture contenant un groupe de chansons et utilise une base de données pour stocker des informations sur la collection musicale.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Audacity</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour enregistrer et éditer des sons. Il peut être rapidement installé via un gestionnaire de paquets. Audacity a une interface simple pour vous aider à démarrer.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Rhythmbox</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Prend en charge une grande variété de sources de musique numérique, y compris l'audio Internet en streaming et les podcasts. L'application permet également de rechercher un audio particulier dans une bibliothèque. Elle prend en charge les<span>&nbsp;</span><em style="line-height: 1.4em; font-style: italic;">listes de lecture intelligentes</em>&nbsp;avec une fonctionnalité de<span>&nbsp;</span><em style="line-height: 1.4em; font-style: italic;">mise à jour automatique</em>, qui peut réviser les listes de lecture en fonction de critères de sélection spécifiés.</td></tr></tbody></table>

Bien sûr, les systèmes Linux peuvent également se connecter à des services de streaming musical en ligne commerciaux, tels que Pandora et Spotify via des navigateurs Web.

![Logo Amarok](https://courses.edx.org/assets/courseware/v1/edb81f83b69bdd2a5c0ba95600449381/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Amarok_logo.jpeg)

![Logo Audacity](https://courses.edx.org/assets/courseware/v1/d03d86902ba54f1d44c23541d2b8c096/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Screen_Shot_2018-07-01_at_1.48.44_PM.png)

![Logo Rhythmbox](https://courses.edx.org/assets/courseware/v1/687be8b4d50a2fef213ec5ffd0a1dfd8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/2000px-Rhythmbox_logo_256px.svg.png)

###
Lecteurs vidéo

Les lecteurs vidéo (film) peuvent afficher des entrées provenant de nombreuses sources différentes, soit locales à la machine, soit sur Internet.

![Image montrant les logos de VLC, MPlayer, Xine et Totem](https://courses.edx.org/assets/courseware/v1/30a387dca706a3a2e03403c3918c0a3a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch17_screen13.jpg)

Les systèmes Linux offrent un certain nombre de lecteurs vidéo, notamment :

* VLC
* MPlayer
* Xine
* Totem

### Éditeurs vidéo

Les éditeurs vidéo sont utilisés pour éditer des vidéos ou des films. Les systèmes Linux offrent un certain nombre d'éditeurs vidéo, notamment :

<table border="0" align="left" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto; font-size: 16px; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Application</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Cinepaint</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Retouche image par image. Cinepaint est utilisé pour éditer des images dans une vidéo.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Blender</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Créer une animation et un design 3D. Blender est un outil professionnel qui utilise la modélisation comme point de départ. Il existe des outils complexes et puissants pour la capture de caméra, l'enregistrement, l'édition, l'amélioration et la création de vidéo, chacun ayant son propre objectif.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Cinelerra</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Capturer, composer et éditer audio/vidéo.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">FFmpeg</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Enregistrer, convertir et diffuser audio/vidéo. FFmpeg est un convertisseur de format, entre autres, et dispose d'autres outils tels que<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">ffplay</strong><span>&nbsp;</span>et<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">ffserver</strong>.</td></tr></tbody></table>

![Logo Cinepaint](https://courses.edx.org/assets/courseware/v1/95c74e658654dc7a2e470cf4c4a44fe0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lp_cinepaint.png)

![Logo Blender](https://courses.edx.org/assets/courseware/v1/c39a5cff9c78cfea1ad459acdbe4fb0f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/blenderlogosocket.png)

![Logo Cinelerra](https://courses.edx.org/assets/courseware/v1/3b627fb386a21a6e955331d2522f2d8c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cinelerra-logo.png)

![Logo FFmpeg](https://courses.edx.org/assets/courseware/v1/74a177f8982742c68c666dfe2d11c18a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/2000px-FFmpeg_Logo_new.svg.png)

###
GIMP (GNU Image Manipulation Program)

Les éditeurs graphiques vous permettent de créer, éditer, visualiser et organiser des images de divers formats, comme Joint Photographic Experts Group (JPEG ou JPG), Portable Network Graphics (PNG), Graphics Interchange Format (GIF) et Tagged Image File Format (TIFF).

Le programme de manipulation d'images GNU (GIMP) est un outil de retouche et d'édition d'images riche en fonctionnalités similaire à Adobe Photoshop et est disponible sur toutes les distributions Linux. Certaines fonctionnalités de GIMP sont :

* Il peut gérer n'importe quel format de fichier image.
* Il dispose de nombreux plugins et filtres à usage spécial.
* Il fournit des informations détaillées sur l'image, telles que les calques, les canaux et les histogrammes.

![Capture d'écran de l'éditeur GIMP](https://courses.edx.org/assets/courseware/v1/eb5482ce7f196048de0070d3a517dd8c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gimpsuse.png)
_Éditeur GIMP_

### Utilitaires graphiques

En plus de GIMP, il existe d'autres utilitaires graphiques qui aident à effectuer diverses tâches liées à l'image, notamment :

<table border="0" align="left" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 751.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilitaire graphique</strong></span></td><td align="center" bgcolor="#003f60" width="57%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">eog</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Eye of Gnome (eog) est une visionneuse d'images qui offre une capacité de diaporama et quelques outils d'édition d'images, tels que la rotation et le redimensionnement. Il peut également parcourir les images d'un répertoire en un seul clic.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Inkscape</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Inkscape est un éditeur d'images avec de nombreuses fonctionnalités d'édition. Il fonctionne avec des calques et des transformations de l'image. Il est parfois comparé à Adobe Illustrator.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">convert</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">convert est un outil en ligne de commande (faisant partie de l'ensemble d'applications ImageMagick) qui peut modifier les fichiers image de nombreuses façons. Les options incluent la conversion de format de fichier et de nombreuses options de modification d'image, telles que le flou, le redimensionnement, le dépoussiérage, etc.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Scribus</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Scribus est utilisé pour créer des documents utilisés pour l'édition et fournir un environnement<span>&nbsp;</span><em style="line-height: 1.4em; font-style: italic;">What You See Is What You Get (WYSIWYG)</em>. Il fournit également de nombreux outils d'édition.</td></tr></tbody></table>

![Logo eog](https://courses.edx.org/assets/courseware/v1/51f5d22403673922faa621eeaf5ec6f3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/eog.jpeg)

![Logo Inkscape](https://courses.edx.org/assets/courseware/v1/d3c6cef446815cb7744a5d3c02ceb78f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/inkscape-logo.png)

![Logo Image Magic](https://courses.edx.org/assets/courseware/v1/7dfca43de79c0839c4b3f676f6c60988/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/logo_liquid-60.gif)

## Résumé du chapitre

Vous avez terminé le chapitre 6. Résumons les concepts clés couverts :

* Linux offre une grande variété d'applications Internet, telles que des navigateurs Web, des clients de messagerie, des applications multimédias en ligne, et d'autres.
* Les navigateurs Web pris en charge par Linux peuvent être graphiques ou textuels, tels que Firefox, Google Chrome, Epiphany, w3m, lynx, et d'autres.
* Linux prend en charge les clients de messagerie graphiques, tels que Thunderbird, Evolution et Claws Mail, et les clients de messagerie en mode texte, tels que Mutt et mail.
* Les systèmes Linux fournissent de nombreuses autres applications pour effectuer des tâches liées à Internet, telles que Filezilla, XChat, Pidgin, et d'autres.
* La plupart des distributions Linux proposent LibreOffice pour créer et éditer différents types de documents.
* Les systèmes Linux offrent des suites entières d'applications et d'outils de développement, y compris des compilateurs et des débogueurs.
* Les systèmes Linux offrent un certain nombre de lecteurs audio, notamment Amarok, Audacity et Rhythmbox.
* Les systèmes Linux offrent un certain nombre de lecteurs vidéo, notamment VLC, MPlayer, Xine et Totem.
* Les systèmes Linux offrent un certain nombre d'éditeurs vidéo, notamment Kino, Cinepaint, Blender entre autres.
* L'utilitaire GIMP (GNU Image Manipulation Program) est un outil de retouche et d'édition d'images riche en fonctionnalités disponible sur toutes les distributions Linux.
* D'autres utilitaires graphiques qui aident à effectuer diverses tâches liées à l'image sont eog, Inkscape, convert et Scribus.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 7 : Opérations en ligne de commande

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Utiliser la ligne de commande pour effectuer des opérations sous Linux.
* Rechercher des fichiers.
* Créer et gérer des fichiers.
* Installer et mettre à jour des logiciels.

### Introduction à la ligne de commande

Les administrateurs système Linux passent une grande partie de leur temps devant une invite de commande. Ils automatisent et dépannent souvent des tâches dans cet environnement textuel. Il y a un dicton : _"les interfaces graphiques rendent les tâches faciles plus faciles, tandis que les interfaces en ligne de commande rendent les tâches difficiles possibles"_. Linux s'appuie fortement sur l'abondance d'outils en ligne de commande. L'interface en ligne de commande offre les avantages suivants :

* Aucune surcharge GUI n'est encourue.
* Pratiquement n'importe quelle tâche peut être accomplie en étant assis devant la ligne de commande.
* Vous pouvez implémenter des scripts pour des tâches souvent utilisées (ou faciles à oublier) et des séries de procédures.
* Vous pouvez vous connecter à des machines distantes n'importe où sur Internet.
* Vous pouvez lancer des applications graphiques directement depuis la ligne de commande au lieu de chercher dans les menus.
* Alors que les outils graphiques peuvent varier entre les distributions Linux, l'interface en ligne de commande ne le fait pas.

![Ligne de commande](https://courses.edx.org/assets/courseware/v1/aff4954e12f4f2a299a3c763a1679773/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cmdline.png)

### Utilisation d'un terminal texte sur le bureau graphique

Un programme **émulateur de terminal** émule (simule) un terminal autonome dans une fenêtre sur le bureau. Par cela, nous voulons dire qu'il se comporte essentiellement comme si vous vous connectiez à la machine sur un terminal purement textuel sans interface graphique en cours d'exécution. La plupart des programmes émulateurs de terminal prennent en charge plusieurs sessions de terminal en ouvrant des onglets ou des fenêtres supplémentaires.

Par défaut, sur les environnements de bureau GNOME, l'application **gnome-terminal** est utilisée pour émuler un terminal en mode texte dans une fenêtre. D'autres programmes de terminal disponibles incluent :

* **xterm**
* **konsole** (par défaut sur KDE)
* **terminator**

![Utilisation de la commande $ ls -a sur Ubuntu, openSUSE, Gentoo et CentOS](https://courses.edx.org/assets/courseware/v1/38f9208d04f151d5d360416b21a00db7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/terminalall.png)
_$ ls -a_

### Lancement de fenêtres de terminal

Pour ouvrir un terminal sur n'importe quel système utilisant un bureau GNOME récent, cliquez sur **Applications > Outils système > Terminal** ou **Applications > Utilitaires > Terminal**. Si vous n'avez pas le menu **Applications**, vous devrez installer le paquet **gnome-shell-extension** approprié et l'activer avec **gnome-tweaks**.

Sur toutes les distributions sauf certaines des plus récentes basées sur GNOME, vous pouvez toujours ouvrir un terminal en faisant un clic droit n'importe où sur l'arrière-plan du bureau et en sélectionnant **Ouvrir dans un terminal**. Si cela ne fonctionne pas, vous devrez encore une fois installer et activer le paquet **gnome-shell-extension** approprié.

Vous pouvez également appuyer sur **Alt-F2** et taper soit **gnome-terminal** soit **konsole**, selon ce qui est approprié.

Parce que les distributions ont eu l'habitude de cacher l'ouverture d'un terminal de ligne de commande, et que l'endroit dans les menus peut varier dans l'interface graphique du bureau, il est bon de comprendre comment "épingler" l'icône du terminal au panneau, ce qui pourrait signifier l'ajouter au groupe Favoris sur les systèmes GNOME.

![Capture d'écran montrant comment ouvrir un terminal sur n'importe quel système utilisant le bureau GNOME](https://courses.edx.org/assets/courseware/v1/8f3255532efb831d557e3fd804d6b6a9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/applications.png)
_Ouverture d'un terminal à l'aide du bureau GNOME_

### Quelques utilitaires de base

Il existe des utilitaires de ligne de commande de base qui sont utilisés constamment, et il serait impossible d'aller plus loin sans en utiliser certains sous une forme simple avant d'en discuter plus en détail. Une courte liste doit inclure :

* **cat** : utilisé pour afficher un fichier (ou combiner des fichiers).
* **head** : utilisé pour afficher les premières lignes d'un fichier.
* **tail** : utilisé pour afficher les dernières lignes d'un fichier.
* **man** : utilisé pour afficher la documentation.

La capture d'écran montre des utilisations élémentaires de ces programmes. Notez l'utilisation du symbole tube (**|**) utilisé pour qu'un programme prenne comme entrée la sortie d'un autre.

Pour la plupart, nous n'utiliserons ces utilitaires que dans des captures d'écran affichant diverses activités, avant d'en discuter en détail.

![Capture d'écran montrant les utilitaires de ligne de commande de base](https://courses.edx.org/assets/courseware/v1/4a2d0c574b1aca9a21e03764634688c7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cmdutils.png)
_Utilitaires de ligne de commande de base_

### La ligne de commande

La plupart des lignes d'entrée saisies à l'invite du shell comportent trois éléments de base :

* Commande
* Options
* Arguments

La commande est le nom du programme que vous exécutez. Elle peut être suivie d'une ou plusieurs options (ou commutateurs) qui modifient ce que la commande peut faire. Les options commencent généralement par un ou deux tirets, par exemple, **-p** ou **--print**, afin de les différencier des arguments, qui représentent ce sur quoi la commande opère.

Cependant, de nombreuses commandes n'ont pas d'options, pas d'arguments, ou ni l'un ni l'autre. De plus, d'autres éléments (tels que la définition de variables d'environnement) peuvent également apparaître sur la ligne de commande lors du lancement d'une tâche.

### sudo

Toutes les démonstrations créées ont un utilisateur configuré avec des capacités **sudo** pour fournir à l'utilisateur des privilèges administratifs (admin) lorsque cela est nécessaire. **sudo** permet aux utilisateurs d'exécuter des programmes en utilisant les privilèges de sécurité d'un autre utilisateur, généralement root (superutilisateur).

Sur vos propres systèmes, vous devrez peut-être configurer et activer **sudo** pour qu'il fonctionne correctement. Pour ce faire, vous devez suivre certaines étapes que nous n'expliquerons pas en détail maintenant, mais que vous apprendrez plus tard dans ce cours. Lors de l'exécution sur Ubuntu et certaines autres distributions récentes, **sudo** est déjà toujours configuré pour vous lors de l'installation. Sur d'autres distributions Linux, vous devrez probablement configurer **sudo** pour qu'il fonctionne correctement pour vous après l'installation initiale.

Ensuite, vous apprendrez les étapes pour configurer et exécuter **sudo** sur votre système.

![sudo ls -la /root](https://courses.edx.org/assets/courseware/v1/a33e740a25f053b970a27e7ebb0055b6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sudosuse.png)
_sudo ls -la /root_

### Étapes pour configurer et exécuter sudo

Si votre système n'a pas déjà **sudo** configuré et activé, vous devez effectuer les étapes suivantes :

1. Vous devrez effectuer des modifications en tant qu'administrateur, ou superutilisateur, root. Bien que **sudo** deviendra la méthode préférée pour ce faire, nous ne l'avons pas encore configuré, nous utiliserons donc **su** (dont nous discuterons plus tard en détail) à la place. À l'invite de commande, tapez **su** et appuyez sur **Entrée**. Vous serez alors invité à saisir le mot de passe root, alors entrez-le et appuyez sur **Entrée**. Vous remarquerez que rien n'est imprimé ; c'est pour que les autres ne puissent pas voir le mot de passe à l'écran. Vous devriez vous retrouver avec une invite différente, se terminant souvent par ‘**#**’. Par exemple :
**$ su** **Password:**
**#**
2. Maintenant, vous devez créer un fichier de configuration pour permettre à votre compte utilisateur d'utiliser sudo. Typiquement, ce fichier est créé dans le répertoire **/etc/sudoers.d/** avec le nom du fichier identique à votre nom d'utilisateur. Par exemple, pour cette démo, disons que votre nom d'utilisateur est **student**. Après avoir effectué l'étape 1, vous créeriez alors le fichier de configuration pour **student** en faisant ceci :
**# echo "student ALL=(ALL) ALL" > /etc/sudoers.d/student**
3. Enfin, certaines distributions Linux se plaindront si vous ne changez pas également les permissions sur le fichier en faisant :
**# chmod 440 /etc/sudoers.d/student**

Cela devrait être tout. Pour le reste de ce cours, si vous utilisez **sudo**, vous devriez être correctement configuré. Lors de l'utilisation de **sudo**, par défaut, vous serez invité à donner un mot de passe (votre propre mot de passe utilisateur) au moins la première fois que vous le faites dans un intervalle de temps spécifié. Il est possible (bien que très peu sûr) de configurer **sudo** pour ne pas exiger de mot de passe ou changer la fenêtre de temps dans laquelle le mot de passe n'a pas à être répété avec chaque commande **sudo**.

![Image](https://courses.edx.org/assets/courseware/v1/5e50e3c0ee4bb967610271e4e43862c3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sandwich.png)

**Sandwich**
(Récupéré de [XKCD](https://xkcd.com/149/), fourni sous une [Licence Creative Commons Attribution-NonCommercial 2.5](https://creativecommons.org/licenses/by-nc/2.5/))

### Basculer entre l'interface graphique et la ligne de commande

La nature personnalisable de Linux vous permet de supprimer l'interface graphique (temporairement ou définitivement) ou de la démarrer après que le système a fonctionné.

La plupart des distributions Linux donnent une option lors de l'installation (ou ont plus d'une version du support d'installation) pour choisir entre bureau (avec un bureau graphique) et serveur (généralement sans).

Les serveurs de production Linux sont généralement installés sans l'interface graphique, et même si elle est installée, ne la lancent généralement pas au démarrage du système. Supprimer l'interface graphique d'un serveur de production peut être très utile pour maintenir un système léger, qui peut être plus facile à supporter et à garder sécurisé.

![Basculer entre l'interface graphique et la ligne de commande](https://courses.edx.org/assets/courseware/v1/117f4f89c2400d3fb8cb296a7dc13c65/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/debianterminal.png)
_Basculer entre l'interface graphique et la ligne de commande_

### Terminaux virtuels

Les **Terminaux Virtuels** (**VT**) sont des sessions de console qui utilisent l'affichage entier et le clavier en dehors d'un environnement graphique. De tels terminaux sont considérés comme "virtuels" car, bien qu'il puisse y avoir plusieurs terminaux actifs, un seul terminal reste visible à la fois. Un VT n'est pas tout à fait la même chose qu'une fenêtre de terminal en ligne de commande ; vous pouvez en avoir beaucoup visibles à la fois sur un bureau graphique.

Un terminal virtuel (généralement le numéro un ou sept) est réservé à l'environnement graphique, et les connexions texte sont activées sur les VT inutilisés. Ubuntu utilise le VT 7, mais CentOS/RHEL et openSUSE utilisent le VT 1 pour l'affichage graphique.

Un exemple de situation où l'utilisation des VT est utile est lorsque vous rencontrez des problèmes avec le bureau graphique. Dans cette situation, vous pouvez passer à l'un des VT texte et dépanner.

Pour basculer entre les VT, appuyez sur la touche **CTRL-ALT-fonction** pour le VT. Par exemple, appuyez sur **CTRL-ALT-F6** pour le VT 6. En fait, vous n'avez qu'à appuyer sur la combinaison de touches **ALT-F6** si vous êtes dans un VT et que vous voulez passer à un autre VT.

![Basculer entre les terminaux virtuels](https://courses.edx.org/assets/courseware/v1/cce9159be8b08390567dc02f1043cf92/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen07.jpg)
_Basculer entre les terminaux virtuels_

### Désactiver le bureau graphique

Les distributions Linux peuvent démarrer et arrêter le bureau graphique de diverses manières. La méthode exacte diffère d'une distribution à l'autre et entre les versions de distribution. Pour les distributions plus récentes basées sur systemd, le gestionnaire d'affichage est exécuté en tant que service, vous pouvez arrêter le bureau GUI avec l'utilitaire systemctl et la plupart des distributions fonctionneront également avec la commande **telinit**, comme dans :

**$ sudo systemctl stop gdm** (ou **sudo telinit 3**)

et le redémarrer (après s'être connecté à la console) avec :

**$ sudo systemctl start gdm** (ou **sudo telinit 5**)

Sur les versions d'Ubuntu antérieures à 18.04 LTS, remplacez **gdm** par **lightdm**.

![Désactiver le bureau graphique](https://courses.edx.org/assets/courseware/v1/7d39cf055c684fe05168b1f42819daf1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/console.png)

## Opérations de base

Dans cette section, nous discuterons de la façon d'accomplir des opérations de base à partir de la ligne de commande. Celles-ci incluent comment se connecter et se déconnecter du système, redémarrer ou arrêter le système, localiser des applications, accéder aux répertoires, identifier les chemins absolus et relatifs, et explorer le système de fichiers.

![Opérations de base : cd, cat, echo, ls, rmdir, man, exit, login, mkdir](https://courses.edx.org/assets/courseware/v1/678d889dcb1112024ef10815f9210a07/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen11.jpg)
_Opérations de base_

### Connexion et déconnexion

Un terminal texte disponible demandera un nom d'utilisateur (avec la chaîne **login:**) et un mot de passe. Lorsque vous tapez votre mot de passe, rien ne s'affiche sur le terminal (pas même un * pour indiquer que vous avez tapé quelque chose), pour empêcher les autres de voir votre mot de passe. Après vous être connecté au système, vous pouvez effectuer des opérations de base.

Une fois votre session démarrée (soit en vous connectant à un terminal texte, soit via un programme de terminal graphique), vous pouvez également vous connecter et vous connecter à des systèmes distants en utilisant Secure SHell (SSH). Par exemple, en tapant **ssh student@remote-server.com**, SSH se connecterait de manière sécurisée à la machine distante (**remote-server.com**) et donnerait à **student** une fenêtre de terminal en ligne de commande, en utilisant soit un mot de passe (comme pour les connexions régulières) soit une clé cryptographique pour se connecter sans fournir de mot de passe pour vérifier l'identité.

![Connexion et déconnexion](https://courses.edx.org/assets/courseware/v1/e0941aff295156471c049248a7d21464/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntulogin.png)

### Redémarrage et arrêt

La méthode préférée pour arrêter ou redémarrer le système est d'utiliser la commande **shutdown**. Cela envoie un message d'avertissement, puis empêche d'autres utilisateurs de se connecter. Le processus init contrôlera alors l'arrêt ou le redémarrage du système. Il est important de toujours arrêter correctement ; ne pas le faire peut entraîner des dommages au système et/ou une perte de données.

Les commandes **halt** et **poweroff** émettent **shutdown -h** pour arrêter le système ; **reboot** émet **shutdown -r** et provoque le redémarrage de la machine au lieu de simplement s'arrêter. Le redémarrage et l'arrêt à partir de la ligne de commande nécessitent un accès superutilisateur (root).

Lors de l'administration d'un système multi-utilisateur, vous avez la possibilité de notifier tous les utilisateurs avant l'arrêt, comme dans :

**$ sudo shutdown -h 10:00 "Arrêt pour maintenance programmée."**

_**NOTE**_ : Sur les distributions Linux récentes basées sur Wayland, les messages de diffusion n'apparaissent pas sur les sessions d'émulation de terminal exécutées sur le bureau ; ils n'apparaissent que sur les affichages de la console VT.

![Redémarrage et arrêt : $ sudo shutdown -h](https://courses.edx.org/assets/courseware/v1/fcfc77b8338d21c5b242707a434d0f0a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntushutdown.png)
_Redémarrage et arrêt_

### Localisation des applications

Selon les spécificités de la politique de votre distribution particulière, les programmes et les paquets logiciels peuvent être installés dans divers répertoires. En général, les programmes exécutables et les scripts devraient résider dans les répertoires **/bin**, **/usr/bin**, **/sbin**, **/usr/sbin**, ou quelque part sous **/opt**. Ils peuvent également apparaître dans **/usr/local/bin** et **/usr/local/sbin**, ou dans un répertoire dans l'espace de compte d'un utilisateur, tel que **/home/student/bin**.

Une façon de localiser les programmes est d'utiliser l'utilitaire `which`. Par exemple, pour savoir exactement où réside le programme `diff` sur le système de fichiers :

**$ which diff**
**/usr/bin/diff**

Si **which** ne trouve pas le programme, **whereis** est une bonne alternative car il recherche des paquets dans une gamme plus large de répertoires système :

**$ whereis diff**
**diff: /usr/bin/diff /usr/share/man/man1/diff.1.gz /usr/share/man/man1p/diff.1p.gz**

ainsi que la localisation des fichiers source et **man** emballés avec le programme.

![Utilitaires which et whereis](https://courses.edx.org/assets/courseware/v1/716532f91059bd5a66899f8ef6e07c31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/whereis.png)
_Utilitaires `which` et `whereis`_

### Accès aux répertoires

Lorsque vous vous connectez pour la première fois à un système ou ouvrez un terminal, le répertoire par défaut devrait être votre répertoire personnel. Vous pouvez imprimer le chemin exact de celui-ci en tapant **echo $HOME**. De nombreuses distributions Linux ouvrent en fait de nouveaux terminaux graphiques dans **$HOME/Desktop**. Les commandes suivantes sont utiles pour la navigation dans les répertoires :

<table height="280" align="center" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 603.047px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="25%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="75%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Résultat</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Affiche le répertoire de travail actuel</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd ~</span></strong></span><span>&nbsp;</span>ou<span>&nbsp;</span><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd</span></strong></span></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Change vers votre répertoire personnel (le nom raccourci est<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">~</span></strong><span>&nbsp;</span>(tilde))</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd ..</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Change vers le répertoire parent (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">..</span></strong>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">cd -</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Change vers le répertoire précédent (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">- (moins)</span></strong>)</td></tr></tbody></table>

Vidéo : Accès aux répertoires

<video controls width="100%" preload="none">

<source src="https://edx-video.net/41e9ceca-8aa4-4b08-8afc-8162da7ce91d-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Comprendre les chemins absolus et relatifs

Il existe deux façons d'identifier les chemins :

* **Chemin absolu**
Un chemin absolu commence par le répertoire racine et suit l'arborescence, branche par branche, jusqu'à ce qu'il atteigne le répertoire ou le fichier souhaité. Les chemins absolus commencent toujours par **/**.
* **Chemin relatif**
Un chemin relatif commence à partir du répertoire de travail actuel. Les chemins relatifs ne commencent jamais par **/**.

Plusieurs barres obliques (**/**) entre les répertoires et les fichiers sont autorisées, mais toutes sauf une barre oblique entre les éléments du chemin sont ignorées par le système. **////usr//bin** est valide, mais vu comme **/usr/bin** par le système.

La plupart du temps, il est plus pratique d'utiliser des chemins relatifs, qui nécessitent moins de frappe. Généralement, vous profitez des raccourcis fournis par : **.** (répertoire actuel), **..** (répertoire parent) et **~** (votre répertoire personnel).

Par exemple, supposons que vous travaillez actuellement dans votre répertoire personnel et que vous souhaitez vous déplacer vers le répertoire **/usr/bin**. Les deux méthodes suivantes vous amèneront au même répertoire depuis votre répertoire personnel :

* Méthode du chemin absolu
**$ cd /usr/bin**
* Méthode du chemin relatif
**$ cd ../../usr/bin**

Dans ce cas, la méthode du chemin absolu nécessite moins de frappe.

![Comprendre les chemins absolus et relatifs](https://courses.edx.org/assets/courseware/v1/c9a79bc0bfc23d476b1c89380ca90aad/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen19.jpg)
_Comprendre les chemins absolus et relatifs_

### Exploration du système de fichiers

Traverser l'arborescence du système de fichiers de haut en bas peut devenir fastidieux. La commande **tree** est un bon moyen d'obtenir une vue d'ensemble de l'arborescence du système de fichiers. Utilisez **tree -d** pour afficher uniquement les répertoires et supprimer la liste des noms de fichiers.

![Exploration du système de fichiers : tree -d](https://courses.edx.org/assets/courseware/v1/1bfb9dae7fe271d3ab73c66d983aadff/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tree-d.png)
_Exploration du système de fichiers_

Les commandes suivantes peuvent aider à explorer le système de fichiers :

<table border="0" align="left" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 877px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="75%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd /</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Change votre répertoire actuel vers le répertoire racine (/) (ou le chemin que vous fournissez)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ls</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Liste le contenu du répertoire de travail actuel</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ls –a</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Liste tous les fichiers, y compris les fichiers et répertoires cachés (ceux dont le nom commence par . )</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tree</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Affiche une vue arborescente du système de fichiers</td></tr></tbody></table>

Vidéo : Exploration du système de fichiers

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V006100_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Liens durs

L'utilitaire **ln** est utilisé pour créer des liens durs et (avec l'option **-s**) des liens souples, également connus sous le nom de liens symboliques ou symlinks. Ces deux types de liens sont très utiles dans les systèmes d'exploitation basés sur UNIX.

Supposons que **file1** existe déjà. Un lien dur, appelé **file2**, est créé avec la commande :

**$ ln file1 file2**

Notez que deux fichiers semblent maintenant exister. Cependant, une inspection plus approfondie de la liste des fichiers montre que ce n'est pas tout à fait vrai.

**$ ls -li file1 file2**

L'option **-i** de **ls** imprime dans la première colonne le numéro d'inode, qui est une quantité unique pour chaque objet fichier. Ce champ est le même pour ces deux fichiers ; ce qui se passe réellement ici, c'est qu'il n'y a qu'un seul fichier, mais il a plus d'un nom associé, comme l'indique le **2** qui apparaît dans la sortie **ls**. Ainsi, il y avait déjà un autre objet lié à **file1** avant que la commande ne soit exécutée.

Les liens durs sont très utiles et économisent de l'espace, mais vous devez faire attention à leur utilisation, parfois de manière subtile. D'une part, si vous supprimez soit **file1** soit **file2** dans l'exemple, l'objet inode (et le nom de fichier restant) restera, ce qui pourrait être indésirable, car cela peut entraîner des erreurs subtiles plus tard si vous recréez un fichier de ce nom.

Si vous modifiez l'un des fichiers, ce qui se passe exactement dépend de votre éditeur ; la plupart des éditeurs, y compris **vi** et **gedit**, conserveront le lien _par défaut_, mais il est possible que la modification de l'un des noms brise le lien et entraîne la création de deux objets.

![Liens durs : $ touch file1, $ ln file1 file2, $ ls -li file?](https://courses.edx.org/assets/courseware/v1/aefe6c7fa6a198680e110ceae5c95c11/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lnubuntu.png)

### Liens souples (symboliques)

Les liens souples (ou symboliques) sont créés avec l'option **-s**, comme dans :

**$ ln -s file1 file3**
**$ ls -li file1 file3**

Remarquez que **file3** ne semble plus être un fichier régulier, et il pointe clairement vers **file1** et a un numéro d'inode différent.

Les liens symboliques ne prennent pas d'espace supplémentaire sur le système de fichiers (à moins que leurs noms ne soient très longs). Ils sont extrêmement pratiques, car ils peuvent facilement être modifiés pour pointer vers différents endroits. Un moyen facile de créer un raccourci de votre répertoire **personnel** vers des chemins longs est de créer un lien symbolique.

Contrairement aux liens durs, les liens souples peuvent pointer vers des objets même sur différents systèmes de fichiers, partitions et/ou disques et autres supports, qui peuvent ou non être actuellement disponibles ou même exister. Dans le cas où le lien ne pointe pas vers un objet actuellement disponible ou existant, vous obtenez un lien cassé (dangling link).

![Liens souples (symboliques) : $ ln -s file1 file3, $ ls -li file?](https://courses.edx.org/assets/courseware/v1/cea407ef8cfd36b34ede2a154959a98f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lnsubuntu.png)
_Liens souples (symboliques)_

### Navigation dans l'historique des répertoires

La commande **cd** se souvient de l'endroit où vous étiez en dernier, et vous permet d'y retourner avec **cd -**. Pour se souvenir de plus que le dernier répertoire visité, utilisez **pushd** pour changer de répertoire au lieu de **cd** ; cela pousse votre répertoire de départ sur une liste. L'utilisation de **popd** vous renverra ensuite vers ces répertoires, en marchant dans l'ordre inverse (le répertoire le plus récent sera le premier récupéré avec **popd**). La liste des répertoires est affichée avec la commande **dirs**.

![Navigation dans l'historique des répertoires : $mkdir /tmp/dirl /tmp/dir2](https://courses.edx.org/assets/courseware/v1/319814cbd06ee587a78854e88478c5b0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pushdfedora.png)
_Navigation dans l'historique des répertoires_

Vidéo : Navigation dans l'historique des répertoires

<video controls width="100%" preload="none">

<source src="https://edx-video.net/89eb42ec-3c89-4dec-8b73-c9b890c88d9f-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Travailler avec des fichiers

Linux fournit de nombreuses commandes qui vous aident à visualiser le contenu d'un fichier, à créer un nouveau fichier ou un fichier vide, à modifier l'horodatage d'un fichier, et à déplacer, supprimer et renommer un fichier ou un répertoire. Ces commandes vous aident à gérer vos données et fichiers et à vous assurer que les données correctes sont disponibles au bon endroit.

![Dossiers jaunes avec des papiers](https://courses.edx.org/assets/courseware/v1/08e475796103299f4fcfac22b2c67fd7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen47A.jpg)

Dans cette section, vous apprendrez à gérer les fichiers.

### Visualisation des fichiers

Vous pouvez utiliser les utilitaires de ligne de commande suivants pour visualiser les fichiers :

<table align="left" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 861.5px; margin: 20px auto 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Commande</span></strong></td><td align="center" bgcolor="#003f60" width="85%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisation</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">cat</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour visualiser des fichiers qui ne sont pas très longs ; il ne fournit aucun défilement arrière.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">tac</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour regarder un fichier à l'envers, en commençant par la dernière ligne.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">less</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour visualiser des fichiers plus volumineux car c'est un programme de pagination. Il s'arrête à chaque écran plein de texte, fournit des capacités de défilement arrière et vous permet de rechercher et de naviguer dans le fichier.<br style="line-height: 1.4em;"><br style="line-height: 1.4em;"><em style="line-height: 1.4em; font-style: italic;"><strong style="font-weight: bold; line-height: 1.4em;">NOTE</strong> : Utilisez&nbsp;<span style="color: inherit; font-style: italic; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">/</strong></span>&nbsp;pour rechercher un motif dans le sens avant et&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: italic; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">?</span></strong>&nbsp;pour un motif dans le sens arrière. Un programme plus ancien nommé&nbsp;more&nbsp;est toujours utilisé, mais a moins de capacités : "less&nbsp;is&nbsp;more".</em></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">tail</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour imprimer les 10 dernières lignes d'un fichier par défaut. Vous pouvez changer le nombre de lignes en faisant&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-n 15</span></strong><span>&nbsp;</span>ou juste<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">-15</strong></span><span>&nbsp;</span>si vous vouliez regarder les 15 dernières lignes au lieu de la valeur par défaut.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">head</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">L'opposé de&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tail</span></strong><span style="color: rgb(51, 51, 51); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif;">; par défaut, il imprime les 10 premières lignes d'un fichier.</span></td></tr></tbody></table>

Vidéo : Plus sur la visualisation des fichiers

<video controls width="100%" preload="none">

<source src="https://edx-video.net/6244a0ed-8260-4df0-bbee-553dae259d64-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### touch

**touch** est souvent utilisé pour définir ou mettre à jour les heures d'accès, de changement et de modification des fichiers. Par défaut, il réinitialise l'horodatage d'un fichier pour qu'il corresponde à l'heure actuelle.

Cependant, vous pouvez également créer un fichier vide en utilisant **touch** :

**$ touch <nomfichier>**

Cela est normalement fait pour créer un fichier vide comme espace réservé pour un usage ultérieur.

**touch** fournit plusieurs options utiles. Par exemple, l'option **-t** vous permet de définir la date et l'horodatage du fichier à une valeur spécifique, comme dans :

**$ touch -t 12091600 myfile**

Cela définit l'horodatage du fichier **myfile** à 16h00, le 9 décembre (12 09 1600).

![touch](https://courses.edx.org/assets/courseware/v1/d29a554d4187aae729d4ed40e42a0146/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/touch.png)
_touch_

### mkdir et rmdir

**mkdir** est utilisé pour créer un répertoire :

* **mkdir sampdir**
Il crée un répertoire exemple nommé **sampdir** sous le répertoire actuel.
* **mkdir /usr/sampdir**
Il crée un répertoire exemple appelé **sampdir** sous **/usr**.

La suppression d'un répertoire se fait avec **rmdir**. Le répertoire doit être vide ou la commande échouera. Pour supprimer un répertoire et tout son contenu, vous devez faire **rm -rf**.

![mkdir](https://courses.edx.org/assets/courseware/v1/72f578cd278d2bd6bd48d63efbfe589e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/mkdir.png)
_mkdir_

### Déplacement, renommage ou suppression d'un fichier

Notez que **mv** fait double emploi, en ce sens qu'il peut :

* Simplement renommer un fichier
* Déplacer un fichier vers un autre emplacement, tout en changeant éventuellement son nom en même temps.

Si vous n'êtes pas certain de supprimer des fichiers qui correspondent à un motif que vous fournissez, il est toujours bon d'exécuter **rm** de manière interactive (**rm –i**) pour demander confirmation avant chaque suppression.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 516.898px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Commande</span></strong></td><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisation</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mv</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Renommer un fichier&nbsp;</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer un fichier&nbsp;</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm –f</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer un fichier de force</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm –i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer un fichier de manière interactive</span></td></tr></tbody></table>

### Renommage ou suppression d'un répertoire

**rmdir** ne fonctionne que sur les répertoires vides ; sinon vous obtenez une erreur.

Bien que taper **rm –rf** soit un moyen rapide et facile de supprimer une arborescence de système de fichiers entière de manière récursive, c'est extrêmement dangereux et doit être utilisé avec le plus grand soin, surtout lorsqu'il est utilisé par root (rappelez-vous que récursif signifie descendre à travers tous les sous-répertoires, jusqu'en bas d'une arborescence).

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 516.898px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mv</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Renommer un répertoire</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rmdir</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer un répertoire vide</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rm -rf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprimer un répertoire de force et récursivement</td></tr></tbody></table>

### Modification de l'invite de ligne de commande

La variable **PS1** est la chaîne de caractères qui s'affiche comme invite sur la ligne de commande. La plupart des distributions définissent **PS1** sur une valeur par défaut connue, qui convient dans la plupart des cas. Cependant, les utilisateurs peuvent vouloir que des informations personnalisées s'affichent sur la ligne de commande. Par exemple, certains administrateurs système exigent que l'utilisateur et le nom du système hôte apparaissent sur la ligne de commande comme dans :

**student@c8 $**

Cela pourrait s'avérer utile si vous travaillez dans plusieurs rôles et que vous voulez toujours vous rappeler qui vous êtes et sur quelle machine vous vous trouvez. L'invite ci-dessus pourrait être implémentée en définissant la variable **PS1** sur : **\u@\h \$**.

Par exemple :

**$ echo $PS1**
**\$**
**$ PS1="\u@\h \$ "**
**student@c8 $ echo $PS1**
**\u@\h \$**
**student@c8 $**

Par convention, la plupart des systèmes sont configurés de sorte que l'utilisateur root ait un signe dièse (**#**) comme invite.

![Bulle de pensée affichant la question Avez-vous une idée pour une invite ?](https://courses.edx.org/assets/courseware/v1/999a9aca943e61f41473186765960c14/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/prompt.png)

Vidéo : Travailler avec des fichiers et des répertoires à l'invite de commande

<video controls width="100%" preload="none">

<source src="https://edx-video.net/0a2c05cb-7749-4c31-b351-8c1cc7791859-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Flux de fichiers standard

Lorsque des commandes sont exécutées, par défaut, il y a trois flux de fichiers standard (ou descripteurs) toujours ouverts pour utilisation : l'entrée standard (standard in ou **stdin**), la sortie standard (standard out ou **stdout**) et l'erreur standard (ou **stderr**).

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 689.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Nom</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Nom symbolique</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Valeur</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Exemple</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">entrée standard</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">stdin</strong></code></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">clavier</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">sortie standard</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">stdout</strong></code></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">terminal</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">erreur standard</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">stderr</strong></code></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">2</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">fichier journal</td></tr></tbody></table>

Généralement, **stdin** est votre clavier, et **stdout** et **stderr** sont imprimés sur votre terminal. **stderr** est souvent redirigé vers un fichier journal d'erreurs, tandis que **stdin** est fourni en dirigeant l'entrée pour qu'elle provienne d'un fichier ou de la sortie d'une commande précédente via un tube (pipe). **stdout** est également souvent redirigé vers un fichier. Comme **stderr** est l'endroit où les messages d'erreur sont écrits, généralement rien n'y ira.

Sous Linux, tous les fichiers ouverts sont représentés en interne par ce qu'on appelle des descripteurs de fichiers. Simplement dit, ceux-ci sont représentés par des nombres commençant à zéro. **stdin** est le descripteur de fichier 0, **stdout** est le descripteur de fichier 1, et **stderr** est le descripteur de fichier 2. Typiquement, si d'autres fichiers sont ouverts en plus de ces trois, qui sont ouverts par défaut, ils commenceront au descripteur de fichier 3 et augmenteront à partir de là.

Sur la page suivante et dans les chapitres à venir, vous verrez des exemples qui modifient l'endroit où une commande en cours d'exécution obtient son entrée, où elle écrit sa sortie, ou où elle imprime des messages de diagnostic (erreur).

### Redirection d'E/S

Grâce au shell de commande, nous pouvons rediriger les trois flux de fichiers standard afin que nous puissions obtenir une entrée à partir d'un fichier ou d'une autre commande, au lieu de notre clavier, et nous pouvons écrire la sortie et les erreurs dans des fichiers ou les utiliser pour fournir une entrée pour les commandes suivantes.

Par exemple, si nous avons un programme appelé **do_something** qui lit à partir de **stdin** et écrit vers **stdout** et **stderr**, nous pouvons changer sa source d'entrée en utilisant le signe inférieur à (**<**) suivi du nom du fichier à consommer pour les données d'entrée :

**$ do_something < input-file**

Si vous voulez envoyer la sortie vers un fichier, utilisez le signe supérieur à (**>**) comme dans :

**$ do_something > output-file**

Parce que **stderr** n'est pas la même chose que **stdout**, les messages d'erreur seront toujours vus sur les fenêtres du terminal dans l'exemple ci-dessus.

Si vous voulez rediriger **stderr** vers un fichier séparé, vous utilisez le numéro de descripteur de fichier de **stderr** (2), le signe supérieur à (**>**), suivi du nom du fichier que vous voulez contenir tout ce que la commande en cours d'exécution écrit vers **stderr** :

**$ do_something 2> error-file**

_**NOTE :** Par la même logique, **do_something 1> output-file** est la même chose que **do_something > output-file**._

Une notation abrégée spéciale peut envoyer tout ce qui est écrit vers le descripteur de fichier **2** (**stderr**) au même endroit que le descripteur de fichier **1** (**stdout**) : **2>&1**.

**$ do_something > all-output-file 2>&1**

bash permet une syntaxe plus facile pour ce qui précède :

**$ do_something >& all-output-file**

### Tubes (Pipes)

La philosophie UNIX/Linux est d'avoir de nombreux programmes (ou commandes) simples et courts qui coopèrent ensemble pour produire des résultats assez complexes, plutôt que d'avoir un programme complexe avec de nombreuses options et modes de fonctionnement possibles. Pour accomplir cela, une utilisation extensive des tubes est faite. Vous pouvez tuber la sortie d'une commande ou d'un programme dans un autre comme son entrée.

Pour ce faire, nous utilisons le symbole de barre verticale, tube (**|**), entre les commandes comme dans :

**$ command1 | command2 | command3**

Ce qui précède représente ce que nous appelons souvent un pipeline, et permet à Linux de combiner les actions de plusieurs commandes en une seule. C'est extraordinairement efficace car **command2** et **command3** n'ont pas à attendre que les commandes de pipeline précédentes se terminent avant de pouvoir commencer à pirater les données dans leurs flux d'entrée ; sur les systèmes à plusieurs CPU ou cœurs, la puissance de calcul disponible est bien mieux utilisée et les choses se font plus rapidement.

De plus, il n'est pas nécessaire d'enregistrer la sortie dans des fichiers (temporaires) entre les étapes du pipeline, ce qui économise de l'espace disque et réduit la lecture et l'écriture sur le disque, ce qui est souvent le goulot d'étranglement le plus lent pour faire quelque chose.

![Pipeline](https://courses.edx.org/assets/courseware/v1/50bdd18ba2e7d4343c184f5e0e3e058a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pipeline.png)
_Pipeline_

### Recherche de fichiers

Être capable de trouver rapidement les fichiers que vous recherchez vous fera gagner du temps et améliorera la productivité. Vous pouvez rechercher des fichiers à la fois dans votre espace de répertoire personnel, ou dans tout autre répertoire ou emplacement sur le système.

![Classeurs](https://courses.edx.org/assets/courseware/v1/4495f95739476edc371e3a69b29f8fc2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen32a.jpg)

Les principaux outils pour ce faire sont les utilitaires **locate** et **find**. Nous montrerons également comment utiliser les caractères génériques dans **bash**, afin de spécifier tout fichier qui correspond à une demande généralisée donnée.

### locate

Le programme utilitaire **locate** effectue une recherche en tirant parti d'une base de données précédemment construite de fichiers et de répertoires sur votre système, correspondant à toutes les entrées qui contiennent une chaîne de caractères spécifiée. Cela peut parfois entraîner une liste très longue.

Pour obtenir une liste plus courte (et peut-être plus pertinente), nous pouvons utiliser le programme **grep** comme filtre. **grep** n'imprimera que les lignes qui contiennent une ou plusieurs chaînes spécifiées, comme dans :

**$ locate zip | grep bin**

qui listera tous les fichiers et répertoires avec à la fois **zip** et **bin** dans leur nom. Nous couvrirons **grep** beaucoup plus en détail plus tard. Remarquez l'utilisation de **|** pour tuber les deux commandes ensemble.

**locate** utilise une base de données créée par un utilitaire connexe, **updatedb**. La plupart des systèmes Linux exécutent cela automatiquement une fois par jour. Cependant, vous pouvez le mettre à jour à tout moment en exécutant simplement **updatedb** à partir de la ligne de commande en tant qu'utilisateur root.

![locate](https://courses.edx.org/assets/courseware/v1/db04248c7965e78a927a0fa8a42fc703/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/locatesuse.png)
_locate_

Vidéo : Localisation de fichiers

<video controls width="100%" preload="none">

<source src="https://edx-video.net/d9de7136-78d9-4cf5-9549-1b61e2f31d4e-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Caractères génériques et correspondance de noms de fichiers

Vous pouvez rechercher un nom de fichier contenant des caractères spécifiques à l'aide de caractères génériques.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 710.797px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Caractère générique</strong></span></td><td align="center" bgcolor="#003f60" width="75%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Résultat</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">?</span></strong>&nbsp;</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Correspond à n'importe quel caractère unique</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">*</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Correspond à n'importe quelle chaîne de caractères</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[set]</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Correspond à n'importe quel caractère dans l'ensemble de caractères, par exemple<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[adf]</span></strong><span>&nbsp;</span>correspondra à toute occurrence de<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">a</strong></span>,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">d</span></strong>, ou<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">f</strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">[!set]</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Correspond à n'importe quel caractère qui n'est pas dans l'ensemble de caractères</span></td></tr></tbody></table>

Pour rechercher des fichiers en utilisant le caractère générique **?**, remplacez chaque caractère inconnu par **?**. Par exemple, si vous savez seulement que les deux premières lettres sont 'ba' d'un nom de fichier de trois lettres avec une extension **.out**, tapez **ls ba?.out**.

Pour rechercher des fichiers en utilisant le caractère générique *****, remplacez la chaîne inconnue par *****. Par exemple, si vous vous souvenez seulement que l'extension était **.out**, tapez **ls *.out**.

Vidéo : Utilisation des caractères génériques pour rechercher des fichiers

<video controls width="100%" preload="none">

<source src="https://edx-video.net/162ffd59-cf5b-4896-aade-b99a16aa95fa-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Le programme find

**find** est un programme utilitaire extrêmement utile et souvent utilisé dans la vie quotidienne d'un administrateur système Linux. Il parcourt récursivement l'arborescence du système de fichiers à partir d'un répertoire particulier (ou d'un ensemble de répertoires) et localise les fichiers qui correspondent aux conditions spécifiées. Le chemin par défaut est toujours le répertoire de travail actuel.

Par exemple, les administrateurs recherchent parfois des fichiers core potentiellement volumineux (qui contiennent des informations de diagnostic après l'échec d'un programme) datant de plusieurs semaines afin de les supprimer.

Il est également courant de supprimer des fichiers non essentiels ou obsolètes dans **/tmp** (et d'autres répertoires volatils, tels que ceux contenant des fichiers mis en cache) qui n'ont pas été accédés récemment. De nombreuses distributions Linux utilisent des scripts shell qui s'exécutent périodiquement (généralement via **cron**) pour effectuer ce nettoyage.

![find](https://courses.edx.org/assets/courseware/v1/102046563ac484a6047300c801886837/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findubuntu.png)
_find_

### Utilisation de find

Lorsqu'aucun argument n'est donné, **find** liste tous les fichiers dans le répertoire courant et tous ses sous-répertoires. Les options couramment utilisées pour raccourcir la liste incluent **-name** (ne lister que les fichiers avec un certain motif dans leur nom), **-iname** (ignorer également la casse des noms de fichiers), et **-type** (qui restreindra les résultats aux fichiers d'un certain type spécifié, tel que **d** pour répertoire, **l** pour lien symbolique, ou **f** pour un fichier régulier, etc.).

Recherche de fichiers et de répertoires nommés **gcc** :

**$ find /usr -name gcc**

Recherche uniquement des répertoires nommés **gcc** :

**$ find /usr -type d -name gcc**

Recherche uniquement des fichiers réguliers nommés **gcc** :

**$ find /usr -type f -name gcc**

![Utilisation de la commande find](https://courses.edx.org/assets/courseware/v1/ea8161eed2e8b061792778df2dec70d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findrhel7.png)
_Utilisation de find_

### Utilisation des options avancées de find

Une autre bonne utilisation de **find** est de pouvoir exécuter des commandes sur les fichiers qui correspondent à vos critères de recherche. L'option **-exec** est utilisée à cette fin.

Pour trouver et supprimer tous les fichiers qui se terminent par **.swp** :

**$ find -name "*.swp" -exec rm {} ’;’**

Le **{}** (accolades) est un espace réservé qui sera rempli avec tous les noms de fichiers résultant de l'expression find, et la commande précédente sera exécutée sur chacun d'eux individuellement.

Veuillez noter que vous devez terminer la commande par ‘**;**’ (y compris les guillemets simples) ou "**\;**". Les deux formes sont correctes.

On peut également utiliser l'option **-ok**, qui se comporte comme **-exec**, sauf que **find** vous demandera la permission avant d'exécuter la commande. Cela en fait un bon moyen de tester vos résultats avant d'exécuter aveuglément des commandes potentiellement dangereuses.

![Recherche et suppression de fichiers se terminant par .swp](https://courses.edx.org/assets/courseware/v1/cbdf6dc606a39eace7d669077837e628/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen41.jpg)
_Recherche et suppression de fichiers se terminant par .swp_

### Recherche de fichiers basée sur le temps et la taille

Il arrive parfois que vous souhaitiez trouver des fichiers en fonction d'attributs, tels que leur date de création, leur dernière utilisation, etc., ou en fonction de leur taille. Il est facile d'effectuer de telles recherches.

Pour trouver des fichiers basés sur le temps :

**$ find / -ctime 3**

Ici, **-ctime** est le moment où les métadonnées de l'inode (c'est-à-dire la propriété du fichier, les permissions, etc.) ont changé pour la dernière fois ; c'est souvent, mais pas nécessairement, le moment où le fichier a été créé pour la première fois. Vous pouvez également rechercher les temps d'accès/dernière lecture (**-atime**) ou de modification/dernière écriture (**-mtime**). Le nombre est le nombre de jours et peut être exprimé soit comme un nombre (**n**) qui signifie exactement cette valeur, **+n**, qui signifie supérieur à ce nombre, ou **-n**, qui signifie inférieur à ce nombre. Il existe des options similaires pour les temps en minutes (comme dans **-cmin**, **-amin** et **-mmin**).

Pour trouver des fichiers basés sur la taille :

**$ find / -size 0**

Notez que la taille ici est en blocs de 512 octets, par défaut ; vous pouvez également spécifier des octets (c), des kilo-octets (k), des méga-octets (M), des giga-octets (G), etc. Comme avec les nombres de temps ci-dessus, les tailles de fichiers peuvent également être des nombres exacts (**n**), **+n** ou **-n**. Pour plus de détails, consultez la page de manuel de find.

Par exemple, pour trouver des fichiers de plus de 10 Mo et exécuter une commande sur ces fichiers :

**$ find / -size +10M -exec command {} ’;’**

![Recherche de fichiers basée sur le temps et la taille](https://courses.edx.org/assets/courseware/v1/007f36e6f54ef7e1547682492e8a9b93/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findsizerhel7.png)
_Recherche de fichiers basée sur le temps et la taille_

Vidéo : Recherche de fichiers dans un répertoire

<video controls width="100%" preload="none">

<source src="https://edx-video.net/467b3768-bf4b-4ba1-9899-87ef71310722-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Systèmes de gestion de paquets sous Linux

Les parties centrales d'une distribution Linux et la plupart de ses logiciels complémentaires sont installés via le **Système de Gestion de Paquets**. Chaque paquet contient les fichiers et autres instructions nécessaires pour faire fonctionner correctement un composant logiciel et coopérer avec les autres composants qui constituent l'ensemble du système. Les paquets peuvent dépendre les uns des autres. Par exemple, un paquet pour une application web écrite en PHP peut dépendre du paquet PHP.

![Boîte remplie de divers objets](https://courses.edx.org/assets/courseware/v1/5bb5d9653cc975c21a23103c015b1483/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch06_screen59a.jpg)

Il existe deux grandes familles de gestionnaires de paquets : ceux basés sur Debian et ceux qui utilisent RPM comme gestionnaire de paquets de bas niveau. Les deux systèmes sont incompatibles, mais globalement, fournissent les mêmes fonctionnalités et satisfont les mêmes besoins. Il existe d'autres systèmes utilisés par des distributions Linux plus spécialisées.

Dans cette section, vous apprendrez comment installer, supprimer ou rechercher des paquets à partir de la ligne de commande en utilisant ces deux systèmes de gestion de paquets.

### Gestionnaires de paquets : Deux niveaux

Les deux systèmes de gestion de paquets fonctionnent à deux niveaux distincts : un outil de bas niveau (tel que **dpkg** ou **rpm**) s'occupe des détails du déballage des paquets individuels, de l'exécution des scripts, de l'installation correcte du logiciel, tandis qu'un outil de haut niveau (tel que **apt-get**, **dnf, yum** ou **zypper**) travaille avec des groupes de paquets, télécharge des paquets depuis le fournisseur et gère les dépendances.

La plupart du temps, les utilisateurs n'ont besoin de travailler qu'avec l'outil de haut niveau, qui se chargera d'appeler l'outil de bas niveau selon les besoins. La résolution des dépendances est une fonctionnalité particulièrement importante de l'outil de haut niveau, car elle gère les détails de la recherche et de l'installation de chaque dépendance pour vous. Soyez prudent, cependant, car l'installation d'un seul paquet pourrait entraîner l'installation de plusieurs dizaines, voire centaines de paquets dépendants.

![Gestionnaires de paquets : Deux niveaux](https://courses.edx.org/assets/courseware/v1/b2cfd35138881e077bfc97915aed86b8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Package_Managers.png)
_Gestionnaires de paquets : Deux niveaux_

### Travailler avec différents systèmes de gestion de paquets

L'Advanced Packaging Tool (**apt**) est le système de gestion de paquets sous-jacent qui gère les logiciels sur les systèmes basés sur Debian. Bien qu'il forme le backend pour les gestionnaires de paquets graphiques, tels que le Centre logiciel Ubuntu et synaptic, son interface utilisateur native est en ligne de commande, avec des programmes qui incluent **apt** (ou **apt-get**) et **apt-cache**.

**dnf** est l'utilitaire de gestion de paquets en ligne de commande open source pour les systèmes Linux compatibles RPM qui appartiennent à la famille Red Hat. **dnf** possède à la fois des interfaces en ligne de commande et graphiques. Fedora et RHEL 8 ont remplacé l'ancien utilitaire **yum** par **dnf**, éliminant ainsi beaucoup de bagages historiques, ainsi qu'introduisant de nombreuses nouvelles capacités intéressantes. **dnf** est à peu près rétrocompatible avec **yum** pour les commandes quotidiennes.

![Travailler avec différents systèmes de gestion de paquets](https://courses.edx.org/assets/courseware/v1/272cd4906572ff37d0352281abe81dbe/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Different_Package_Mmanagement_Tools.png)

**zypper** est le système de gestion de paquets pour la famille SUSE/openSUSE et est également basé sur RPM. **zypper** vous permet également de gérer les dépôts à partir de la ligne de commande. **zypper** est assez simple à utiliser et ressemble assez étroitement à **dnf**/**yum**.

Pour apprendre les commandes de base de gestion des paquets, jetez un œil à ces commandes de base :

<table height="395" align="center" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 800px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="padding-left" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p align="padding-left" style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Opération</strong></span></p></td><td width="30%" align="padding-left" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p align="padding-left" style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">rpm</strong></span></p></td><td width="30%" align="padding-left" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p align="padding-left" style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">deb</strong></span></p></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Installer un paquet</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">rpm -i foo.rpm</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --install foo.deb</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Installer un paquet, dépendances</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;install foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get install foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Supprimer un paquet</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -e foo.rpm</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --remove foo.deb</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Supprimer un paquet, dépendances</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;remove foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get autoremove foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Mettre à jour un paquet</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -U foo.rpm</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --install foo.deb</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Mettre à jour un paquet, dépendances</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;update foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get install foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Mettre à jour le système entier</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;update</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-get dist-upgrade</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Afficher tous les paquets installés</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -qa</strong></span><span>&nbsp;</span>ou&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf list installed</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --list</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Obtenir des informations sur un paquet</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -qil foo</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --listfiles foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Afficher les paquets nommés<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">foo</strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;list "foo"</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-cache search foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Afficher tous les paquets disponibles</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dnf&nbsp;list</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">apt-cache dumpavail foo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">De quel paquet fait partie le fichier<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">file</strong></span><span>&nbsp;</span>?</p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">rpm -qf file</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">dpkg --search file</strong></span></td></tr></tbody></table>

### Vidéo : Gestion de paquets Debian bas niveau avec dpkg

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001500_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Gestion de paquets RPM bas niveau avec rpm

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001600_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Gestion de paquets haut niveau avec dnf

<video controls width="100%" preload="none">

<source src="https://edx-video.net/825ce6b8-4cc5-4680-ae8d-a31efd12b83a-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Gestion de paquets haut niveau avec zypper sur openSUSE

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002400_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Gestion de paquets haut niveau avec apt sur Ubuntu

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001800_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Résumé du chapitre

Vous avez terminé le chapitre 7. Résumons les concepts clés que nous avons couverts :

* Les terminaux virtuels (VT) sous Linux sont des consoles, ou des terminaux en ligne de commande qui utilisent le moniteur et le clavier connectés.
* Différentes distributions Linux démarrent et arrêtent le bureau graphique de différentes manières.
* Un programme émulateur de terminal sur le bureau graphique fonctionne en émulant un terminal dans une fenêtre sur le bureau.
* Le système Linux vous permet de vous connecter soit via un terminal texte, soit à distance via la console.
* Lorsque vous tapez votre mot de passe, rien n'est imprimé sur le terminal, pas même un symbole générique pour indiquer que vous avez tapé.
* La méthode préférée pour arrêter ou redémarrer le système est d'utiliser la commande **shutdown**.
* Il existe deux types de chemins : absolus et relatifs.
* Un chemin absolu commence par le répertoire racine et suit l'arborescence, branche par branche, jusqu'à ce qu'il atteigne le répertoire ou le fichier souhaité.
* Un chemin relatif commence à partir du répertoire de travail actuel.
* L'utilisation de liens durs et souples (symboliques) est extrêmement utile sous Linux.
* **cd** se souvient de l'endroit où vous étiez en dernier, et vous permet d'y retourner avec **cd -**.
* **locate** effectue une recherche dans une base de données pour trouver tous les noms de fichiers qui correspondent à un motif donné.
* **find** localise les fichiers de manière récursive à partir d'un répertoire ou d'un ensemble de répertoires donné.
* **find** est capable d'exécuter des commandes sur les fichiers qu'il liste, lorsqu'il est utilisé avec l'option **-exec**.
* **touch** est utilisé pour définir les heures d'accès, de changement et d'édition des fichiers, ainsi que pour créer des fichiers vides.
* Le système de gestion de paquets Advanced Packaging Tool (**apt**) est utilisé pour gérer les logiciels installés sur les systèmes basés sur Debian.
* Vous pouvez utiliser l'utilitaire de gestion de paquets en ligne de commande **dnf** pour les distributions Linux de la famille Red Hat basées sur RPM.
* Le système de gestion de paquets **zypper** est basé sur RPM et utilisé pour openSUSE.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 8 : Trouver de la documentation Linux

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Utiliser différentes sources de documentation.
* Utiliser les pages de manuel (man pages).
* Accéder au système GNU Info.
* Utiliser la commande **help** et l'option **--help**.
* Utiliser d'autres sources de documentation.

### Sources de documentation Linux

Que vous soyez un utilisateur inexpérimenté ou un vétéran, vous ne saurez pas toujours (ou ne vous souviendrez pas) de l'utilisation correcte des divers programmes et utilitaires Linux : quelle est la commande à taper, quelles options prend-elle, etc. Vous devrez consulter régulièrement la documentation d'aide. Parce que les systèmes basés sur Linux s'appuient sur une grande variété de sources, il existe de nombreux réservoirs de documentation et de moyens d'obtenir de l'aide. Les distributeurs consolident ce matériel et le présentent de manière complète et facile à utiliser.

![Sources de documentation Linux](https://courses.edx.org/assets/courseware/v1/cf55b1fe48a37f0ae2fed5fee049c262/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch07_screen03.jpg)

**Sources de documentation Linux**

Les sources de documentation Linux importantes incluent :

* Les pages **man** (abréviation de pages de manuel)
* GNU Info
* La commande **help** et l'option **--help**
* D'autres sources de documentation, par exemple le [Manuel Gentoo](https://www.gentoo.org/support/documentation/) ou la [Documentation Ubuntu](https://help.ubuntu.com/community/CommunityHelpWiki).

### Les pages man

Les pages man sont la source de documentation Linux la plus souvent utilisée. Elles fournissent une documentation approfondie sur de nombreux programmes et utilitaires, ainsi que sur d'autres sujets, y compris les fichiers de configuration et les API de programmation pour les appels système, les routines de bibliothèque et le noyau. Elles sont présentes sur toutes les distributions Linux et sont toujours à portée de main.

L'infrastructure des pages man a été introduite pour la première fois dans les premières versions d'UNIX, au début des années 1970. Le nom man est juste une abréviation de manuel.

![Livre](https://courses.edx.org/assets/courseware/v1/be369a4b31dfa8c5655024c337b9c1b8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch07_screen05.jpg)

Taper man avec un nom de sujet comme argument récupère les informations stockées dans les pages man du sujet.

Les pages man sont souvent converties vers d'autres formats, tels que des documents PDF et des pages Web. Pour en savoir plus, jetez un œil aux [pages man Linux en ligne](http://man7.org/linux/man-pages/). De nombreuses pages Web ont une interface graphique pour les éléments d'aide, qui peut inclure des pages man.

D'autres sources de documentation incluent des livres publiés et de nombreux sites Internet.

### man

Le programme **man** recherche, formate et affiche les informations contenues dans le système de pages man. Parce que de nombreux sujets ont des quantités copieuses d'informations pertinentes, la sortie est tubée à travers un programme de pagination (tel que **less**) pour être visualisée une page à la fois. En même temps, les informations sont formatées pour un bon affichage visuel.

Un sujet donné peut avoir plusieurs pages associées et il existe un ordre par défaut déterminant laquelle est affichée lorsqu'aucune option ou numéro de section n'est spécifié. Pour lister toutes les pages sur le sujet, utilisez l'option **-f**. Pour lister toutes les pages qui traitent d'un sujet spécifique (même si le sujet spécifié n'est pas présent dans le nom), utilisez l'option **–k**.

* **man –f** génère le même résultat que de taper **whatis**.
* **man –k** génère le même résultat que de taper **apropos**.

L'ordre par défaut est spécifié dans **/etc/man_db.conf** et est approximativement (mais pas exactement) dans l'ordre numérique croissant par section.

![man -f sysctl](https://courses.edx.org/assets/courseware/v1/c164a9474ac7ecb00e78799f2cfd602c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/man1.png)
_man_

### Chapitres du manuel

Les pages man sont divisées en chapitres numérotés de 1 à 9. Dans certains cas, une lettre est ajoutée au numéro de chapitre pour identifier un sujet spécifique. Par exemple, de nombreuses pages décrivant une partie de l'API X Window sont dans le chapitre **3X**.

Le numéro de chapitre peut être utilisé pour forcer man à afficher la page d'un chapitre particulier. Il est courant d'avoir plusieurs pages à travers plusieurs chapitres avec le même nom, en particulier pour les noms de fonctions de bibliothèque ou d'appels système.

Avec le paramètre **-a**, man affichera toutes les pages avec le nom donné dans tous les chapitres, l'une après l'autre, comme dans :

**$ man -a socket**

![Chapitres du manuel : $ man -a socket](https://courses.edx.org/assets/courseware/v1/83583dd77505523938107d8480bea1d4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/manchap.png)
_Chapitres du manuel_

### Vidéo : Utilisation de man

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002300_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Le système GNU Info

La source suivante de documentation Linux est le système GNU Info.

C'est le format de documentation standard du projet GNU, qu'il préfère comme alternative à **man**. Le système Info est essentiellement de forme libre et prend en charge les sous-sections liées.

![Logo du projet GNU](https://courses.edx.org/assets/courseware/v1/6f9aed0e12194cfc5c52cf50664c3bdd/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/GNU_Project_logo.jpg)

Fonctionnellement, **info** ressemble à man à bien des égards. Cependant, les sujets sont connectés à l'aide de liens (même si sa conception précède le World Wide Web). Les informations peuvent être visualisées via une interface en ligne de commande, un utilitaire d'aide graphique, imprimées ou consultées en ligne.

### Utilisation d'info à partir de la ligne de commande

Taper **info** sans arguments dans une fenêtre de terminal affiche un index des sujets disponibles. Vous pouvez parcourir la liste des sujets en utilisant les touches de déplacement habituelles : flèches, **Page Up** et **Page Down**.

Vous pouvez afficher l'aide pour un sujet particulier en tapant **info <nom du sujet>**. Le système recherche alors le sujet dans tous les fichiers **info** disponibles.

Quelques touches utiles sont : **q** pour quitter, **h** pour l'aide et **Entrée** pour sélectionner un élément de menu.

![info](https://courses.edx.org/assets/courseware/v1/d7c774dd6b4b262495a16a57aed417a5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/infoubuntu.png)
_info_

### Structure de la page info

Le sujet que vous visualisez dans une page info est appelé un **nœud**. Le tableau liste les frappes de base pour se déplacer entre les nœuds.

Les nœuds sont essentiellement des sections et des sous-sections dans la documentation. Vous pouvez vous déplacer entre les nœuds ou visualiser chaque nœud séquentiellement. Chaque nœud peut contenir des menus et des sous-thèmes liés, ou des éléments.

Les éléments fonctionnent comme des liens de navigateur et sont identifiés par un astérisque (*****) au début du nom de l'élément. Les éléments nommés (en dehors d'un menu) sont identifiés par deux-points (**::**) à la fin du nom de l'élément. Les éléments peuvent faire référence à d'autres nœuds dans le fichier ou à d'autres fichiers.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 344.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche&nbsp;</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Fonction</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" :="" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px; font-family: &quot;Courier New&quot;;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">n</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Aller au nœud suivant</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">p</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Aller au nœud précédent</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">u</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Monter d'un nœud dans l'index</td></tr></tbody></table>

### Vidéo : Utilisation d'info

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002200_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### L'option --help

Une autre source importante de documentation Linux est l'utilisation de l'option **--help**.

La plupart des commandes ont une courte description disponible qui peut être visualisée en utilisant l'option **--help** ou **-h** avec la commande ou l'application. Par exemple, pour en savoir plus sur la commande **man**, vous pouvez taper :

**$ man --help**

L'option **--help** est utile comme référence rapide et affiche les informations plus rapidement que les pages **man** ou **info**.

![L'option --help](https://courses.edx.org/assets/courseware/v1/f9d86b387589f5e13d24cc7e88272e61/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/manhelp.png)
_L'option --help_

### La commande help

Lorsqu'elles sont exécutées dans un shell de commande **bash**, certaines commandes populaires (telles que **echo** et **cd**) exécutent en fait des versions spécialement intégrées à **bash** des commandes plutôt que les binaires habituels trouvés sur le système de fichiers, disons sous **/bin** ou **/usr/bin**. Il est plus efficace de le faire car l'exécution est plus rapide car moins de ressources sont utilisées (nous discuterons des shells de commande plus tard). Il convient de noter qu'il peut y avoir quelques (généralement petites) différences dans les deux versions de la commande.

Pour afficher un synopsis de ces commandes intégrées, vous pouvez simplement taper **help** comme indiqué dans la capture d'écran.

Pour ces commandes intégrées, **help** remplit la même fonction de base que les arguments **-h** et **--help** remplissent pour les programmes autonomes.

![La commande help](https://courses.edx.org/assets/courseware/v1/79040611925a7890d2337fb896445e08/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/helpbash.png)
_La commande help_

### Autres sources de documentation

En plus des pages man, du système GNU Info et de la commande **help**, il existe d'autres sources de documentation Linux, dont voici quelques exemples :

* Système d'aide du bureau
* Documentation des paquets
* Ressources en ligne.

![Autres sources de documentation](https://courses.edx.org/assets/courseware/v1/d4be6c97491354162222dd6068f4ba04/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch07_screen23.jpg)
_Autres sources de documentation_

### Systèmes d'aide graphiques

Tous les systèmes de bureau Linux ont une application d'aide graphique. Cette application est généralement affichée sous la forme d'une icône de point d'interrogation ou d'une image de bouée de sauvetage de navire, et peut également toujours être trouvée dans le système de menus. Ces programmes contiennent généralement une aide personnalisée pour le bureau lui-même et certaines de ses applications, et incluront parfois également des pages **info** et **man** rendues graphiquement.

Si vous ne voulez pas passer du temps à chercher la bonne icône ou l'élément de menu pour lancer l'application d'aide, vous pouvez également démarrer le système d'aide graphique à partir d'une fenêtre de terminal ou d'une invite de commande en utilisant l'un des programmes utilitaires suivants :

* GNOME : **gnome-help** ou **yelp**
* KDE : **khelpcenter**

![Aide GNOME](https://courses.edx.org/assets/courseware/v1/c782c9043e9c07ee0e290aaff8503432/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gnome-help.png)
_Aide GNOME_

![Centre d'aide KDE](https://courses.edx.org/assets/courseware/v1/d7496895a50216347fcd26f479adb0b9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/khelpcenter.png)
_Aide KDE_

### Documentation des paquets

La documentation Linux est également disponible dans le cadre du système de gestion de paquets. Généralement, cette documentation est directement tirée du code source en amont, mais elle peut également contenir des informations sur la façon dont la distribution a emballé et configuré le logiciel.

Ces informations sont placées sous le répertoire **/usr/share/doc**, regroupées dans des sous-répertoires nommés d'après chaque paquet, incluant peut-être le numéro de version dans le nom.

![Documentation des paquets](https://courses.edx.org/assets/courseware/v1/dcab137a19a95616557b1c49f0754419/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/usrsharedoc.png)
_Documentation des paquets_

### Ressources en ligne

Il existe de nombreux endroits pour accéder à la documentation Linux en ligne, et un peu de recherche vous y plongera.

Le livre suivant a été bien noté par d'autres utilisateurs de ce cours. C'est un recueil de ligne de commande gratuit et téléchargeable sous licence Creative Commons : _"[The Linux Command Line](http://linuxcommand.org/tlcl.php)"_ par William Shotts.

Vous pouvez également trouver une documentation très utile pour chaque distribution. Chaque distribution a ses propres forums générés par les utilisateurs et ses sections wiki. Voici quelques liens vers de telles sources :

* [Documentation Ubuntu](https://help.ubuntu.com/)
* [Documentation CentOS](https://wiki.centos.org/Documentation)
* [Documentation openSUSE](https://doc.opensuse.org/)
* [Documentation Gentoo](https://www.gentoo.org/support/documentation/)
* [Documentation Fedora](https://docs.fedoraproject.org/).

De plus, vous pouvez utiliser des sites de recherche en ligne pour localiser des ressources utiles partout sur Internet, y compris des articles de blog, des messages de forum et de liste de diffusion, des articles de presse, etc.

### Résumé du chapitre

Vous avez terminé le chapitre 8. Résumons les concepts clés couverts :

* Les principales sources de documentation Linux sont les pages man, GNU info, les options et la commande **help**, et une riche variété de sources de documentation en ligne.
* L'utilitaire **man** recherche, formate et affiche les pages man.
* Les pages man fournissent une documentation approfondie sur les programmes et d'autres sujets concernant le système, y compris les fichiers de configuration, les appels système, les routines de bibliothèque et le noyau.
* Le système GNU Info a été créé par le projet GNU comme sa documentation standard. Il est robuste et accessible via des outils en ligne de commande, Web et graphiques utilisant **info**.
* De courtes descriptions pour les commandes sont généralement affichées avec l'argument **-h** ou **--help**.
* Vous pouvez taper **help** à la ligne de commande pour afficher un synopsis des commandes intégrées.
* Il existe de nombreuses autres ressources d'aide à la fois sur votre système et sur Internet.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 9 : Processus

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Décrire ce qu'est un processus et distinguer les types de processus.
* Énumérer les attributs des processus.
* Gérer les processus à l'aide de **ps** et **top**.
* Comprendre l'utilisation des moyennes de charge et d'autres métriques de processus.
* Manipuler les processus en les mettant en arrière-plan et en les restaurant au premier plan.
* Utiliser **at**, **cron** et **sleep** pour planifier des processus dans le futur ou les mettre en pause.

### Qu'est-ce qu'un processus ?

Un **processus** est simplement une instance d'une ou plusieurs tâches (threads) connexes s'exécutant sur votre ordinateur. Ce n'est pas la même chose qu'un **programme** ou une **commande**. Une seule commande peut en fait démarrer plusieurs processus simultanément. Certains processus sont indépendants les uns des autres et d'autres sont liés. Une défaillance d'un processus peut ou non affecter les autres en cours d'exécution sur le système.

![Processus](https://courses.edx.org/assets/courseware/v1/219d348bf46fa4b3b8c83b3dbdf3fb31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen03.jpg)
_Processus_

Les processus utilisent de nombreuses ressources système, telles que la mémoire, les cycles CPU (unité centrale de traitement) et les périphériques, tels que les cartes réseau, les disques durs, les imprimantes et les écrans. Le système d'exploitation (en particulier le noyau) est responsable de l'allocation d'une part appropriée de ces ressources à chaque processus et de garantir une utilisation globale optimisée du système.

### Types de processus

Une fenêtre de terminal (un type de shell de commande) est un processus qui s'exécute aussi longtemps que nécessaire. Il permet aux utilisateurs d'exécuter des programmes et d'accéder aux ressources dans un environnement interactif. Vous pouvez également exécuter des programmes en arrière-plan, ce qui signifie qu'ils se détachent du shell.

Les processus peuvent être de différents types selon la tâche effectuée. Voici quelques types de processus différents, ainsi que leurs descriptions et exemples :

<table width="80%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 861.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Type de processus</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td><td width="25%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Exemple</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Processus interactifs</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Doivent être démarrés par un utilisateur, soit en ligne de commande, soit via une interface graphique telle qu'une icône ou une sélection de menu.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">bash, firefox, top</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Processus par lots (Batch)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Processus automatiques qui sont planifiés à partir du terminal puis déconnectés de celui-ci. Ces tâches sont mises en file d'attente et fonctionnent sur une base&nbsp;<strong style="font-weight: bold; line-height: 1.4em;">FIFO</strong><span>&nbsp;</span>(<strong style="font-weight: bold; line-height: 1.4em;">F</strong>irst-<strong style="font-weight: bold; line-height: 1.4em;">I</strong>n,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">F</strong>irst-<strong style="font-weight: bold; line-height: 1.4em;">O</strong>ut - Premier entré, premier sorti).</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">updatedb, ldconfig</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Démons (Daemons)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Processus serveur qui s'exécutent en continu. Beaucoup sont lancés au démarrage du système et attendent ensuite une demande d'utilisateur ou de système indiquant que leur service est requis.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">httpd, sshd, libvirtd</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Threads</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Processus légers. Ce sont des tâches&nbsp;qui s'exécutent sous l'égide d'un processus principal, partageant la mémoire et d'autres ressources, mais sont planifiées et exécutées par le système sur une base individuelle. Un thread individuel peut se terminer sans terminer l'ensemble du processus et un processus peut créer de nouveaux threads à tout moment. De nombreux programmes non triviaux sont&nbsp;multi-threadés.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">firefox, gnome-terminal-server</strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Threads du noyau</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Tâches du noyau que les utilisateurs ne démarrent ni ne terminent et sur lesquelles ils ont peu de contrôle. Celles-ci peuvent effectuer des actions comme déplacer un thread d'un processeur à un autre, ou s'assurer que les opérations d'entrée/sortie sur le disque sont terminées.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">kthreadd, migration, ksoftirqd</strong></td></tr></tbody></table>

### Planification et états des processus

Une fonction critique du noyau appelée le **planificateur** (scheduler) déplace constamment les processus sur et hors du processeur, partageant le temps selon la priorité relative, le temps nécessaire et le temps déjà accordé à une tâche.

Lorsqu'un processus est dans un état dit **en cours d'exécution** (running), cela signifie qu'il exécute actuellement des instructions sur un processeur, ou attend qu'on lui accorde une part de temps (une tranche de temps) pour pouvoir s'exécuter. Tous les processus dans cet état résident sur ce qu'on appelle une file d'attente d'exécution (run queue) et sur un ordinateur avec plusieurs processeurs, ou cœurs, il y a une file d'attente d'exécution sur chacun.

![Planification et états des processus](https://courses.edx.org/assets/courseware/v1/49178932e74cb80a82c62db4fff8ce2a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen05.jpg)
_Planification et états des processus_

Cependant, parfois les processus passent dans ce qu'on appelle un état de **sommeil** (sleep), généralement lorsqu'ils attendent que quelque chose se produise avant de pouvoir reprendre, peut-être que l'utilisateur tape quelque chose. Dans cette condition, un processus est dit être assis dans une file d'attente (wait queue).

Il existe d'autres états de processus moins fréquents, en particulier lorsqu'un processus se termine. Parfois, un processus enfant se termine, mais son processus parent n'a pas demandé son état. De manière amusante, un tel processus est dit être dans un état zombie ; il n'est pas vraiment vivant, mais apparaît toujours dans la liste des processus du système.

### ID de processus et de thread

À tout moment, il y a toujours plusieurs processus en cours d'exécution. Le système d'exploitation les suit en attribuant à chacun un numéro d'identification de processus unique (**PID**). Le PID est utilisé pour suivre l'état du processus, l'utilisation du processeur, l'utilisation de la mémoire, l'emplacement précis des ressources en mémoire et d'autres caractéristiques.

Les nouveaux PID sont généralement attribués par ordre croissant au fur et à mesure que les processus naissent. Ainsi, le PID 1 désigne le processus **init** (processus d'initialisation), et les processus suivants se voient attribuer progressivement des numéros plus élevés.

Le tableau explique les types de PID et leurs descriptions :

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 861.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Type d'ID</strong></span></td><td align="center" bgcolor="#003f60" width="70%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">ID de processus (PID)</td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Numéro d'ID de processus unique</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">ID de processus parent (PPID)</td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Processus (Parent) qui a démarré ce processus. Si le parent meurt, le PPID fera référence à un parent adoptif ; sur les noyaux récents, c'est kthreadd qui a PPID=2.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">ID de thread (TID)</td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Numéro d'ID de thread. C'est le même que le PID pour les processus à un seul thread. Pour un processus multi-threadé, chaque thread partage le même PID, mais a un TID unique.</td></tr></tbody></table>

### Terminer un processus

À un moment donné, l'une de vos applications peut cesser de fonctionner correctement. Comment l'éliminer ?

Pour terminer un processus, vous pouvez taper **kill -SIGKILL <pid>** ou **kill -9 <pid>**.

Notez cependant que vous ne pouvez tuer que vos propres processus ; ceux appartenant à un autre utilisateur sont hors limites, sauf si vous êtes root.

![Terminer un processus](https://courses.edx.org/assets/courseware/v1/6a71bd8d47df4eaf7e430d8089c632a5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/rhelkill.png)
_Terminer un processus_

### ID d'utilisateur et de groupe

De nombreux utilisateurs peuvent accéder à un système simultanément, et chaque utilisateur peut exécuter plusieurs processus. Le système d'exploitation identifie l'utilisateur qui démarre le processus par l'ID utilisateur réel (RUID) attribué à l'utilisateur.

L'utilisateur qui détermine les droits d'accès pour les utilisateurs est identifié par l'UID effectif (EUID). L'EUID peut ou non être le même que le RUID.

![ID d'utilisateur et de groupe](https://courses.edx.org/assets/courseware/v1/fbe122ffd13edf336ad978cddb953a7f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen07.jpg)
_ID d'utilisateur et de groupe_

Les utilisateurs peuvent être classés en divers groupes. Chaque groupe est identifié par l'ID de groupe réel (RGID). Les droits d'accès du groupe sont déterminés par l'ID de groupe effectif (EGID). Chaque utilisateur peut être membre d'un ou plusieurs groupes.

La plupart du temps, nous ignorons ces détails et parlons simplement de l'ID utilisateur (UID) et de l'ID de groupe (GID).

### Plus sur les priorités

À tout moment, de nombreux processus sont en cours d'exécution (c'est-à-dire dans la file d'attente d'exécution) sur le système. Cependant, un processeur ne peut en fait accueillir qu'une seule tâche à la fois, tout comme une voiture ne peut avoir qu'un seul conducteur à la fois. Certains processus sont plus importants que d'autres, donc Linux vous permet de définir et de manipuler la priorité des processus. Les processus de priorité plus élevée obtiennent un accès préférentiel au processeur.

La priorité d'un processus peut être définie en spécifiant une **valeur nice** (gentillesse), ou niceness, pour le processus. Plus la valeur nice est basse, plus la priorité est élevée. Les valeurs basses sont attribuées aux processus importants, tandis que les valeurs élevées sont attribuées aux processus qui peuvent attendre plus longtemps. Un processus avec une valeur nice élevée permet simplement aux autres processus d'être exécutés en premier. Sous Linux, une valeur nice de **-20** représente la priorité la plus élevée et **+19** représente la plus basse. Bien que cela puisse sembler à l'envers, cette convention (plus le processus est gentil, plus la priorité est basse) remonte aux premiers jours d'UNIX.

![Sortie de nice](https://courses.edx.org/assets/courseware/v1/d929bb0d3a611c780e2dcb6dd00cddd5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/niceout.png)
_Sortie de nice_

Vous pouvez également attribuer une soi-disant **priorité temps réel** aux tâches sensibles au temps, telles que le contrôle de machines via un ordinateur ou la collecte de données entrantes. C'est juste une priorité très élevée et ne doit pas être confondue avec ce qu'on appelle le temps réel dur qui est conceptuellement différent, et a plus à voir avec le fait de s'assurer qu'un travail est terminé dans une fenêtre de temps très bien définie.

![Valeurs Nice](https://courses.edx.org/assets/courseware/v1/fcc61556971b7cdefbafabf3d7abab22/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch16_screen08.jpg)
_Valeurs Nice_

### Vidéo : Utilisation de renice pour définir les priorités

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000100_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Moyennes de charge

La **moyenne de charge** (load average) est la moyenne du nombre de charge pour une période de temps donnée. Elle prend en compte les processus qui sont :

* En cours d'exécution active sur un processeur.
* Considérés comme exécutables, mais en attente qu'un processeur devienne disponible.
* En sommeil : c'est-à-dire en attente qu'une ressource (généralement, E/S) devienne disponible.

_**NOTE**_ : Linux diffère des autres systèmes d'exploitation de type UNIX en ce qu'il inclut les processus en sommeil. De plus, il n'inclut que les dormeurs dits **ininterruptibles**, ceux qui ne peuvent pas être réveillés facilement.

La moyenne de charge peut être visualisée en exécutant **w**, **top** ou **uptime**. Nous expliquerons les chiffres sur la page suivante.

![Moyennes de charge : w](https://courses.edx.org/assets/courseware/v1/ca05a14d78d8e3bb26b519fe65047a66/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wuptimesuse.png)
_Moyennes de charge_

### Interprétation des moyennes de charge

La moyenne de charge est affichée à l'aide de trois nombres (**0.45**, **0.17** et **0.12**) dans la capture d'écran ci-dessous. En supposant que notre système est un système à un seul processeur, les trois nombres de moyenne de charge sont interprétés comme suit :

* **0.45** : Pour la dernière minute, le système a été utilisé à 45% en moyenne.
* **0.17** : Pour les 5 dernières minutes, l'utilisation a été de 17%.
* **0.12** : Pour les 15 dernières minutes, l'utilisation a été de 12%.

Si nous voyions une valeur de **1.00** en deuxième position, cela impliquerait que le système à un seul processeur était utilisé à 100%, en moyenne, au cours des 5 dernières minutes ; c'est bien si nous voulons utiliser pleinement un système. Une valeur supérieure à **1.00** pour un système à un seul processeur implique que le système était surutilisé : il y avait plus de processus nécessitant du CPU que de CPU disponible.

Si nous avions plus d'un processeur, disons un système à quatre processeurs, nous diviserions les nombres de moyenne de charge par le nombre de processeurs. Dans ce cas, par exemple, voir une moyenne de charge de 1 minute de **4.00** implique que le système dans son ensemble était utilisé à 100% (4.00/4) au cours de la dernière minute.

Les augmentations à court terme ne sont généralement pas un problème. Un pic élevé que vous voyez est probablement une rafale d'activité, pas un nouveau niveau. Par exemple, au démarrage, de nombreux processus démarrent et l'activité se calme ensuite. Si un pic élevé est observé dans les moyennes de charge de 5 et 15 minutes, cela peut être une source de préoccupation.

![Interprétation des moyennes de charge](https://courses.edx.org/assets/courseware/v1/5ad78e82ed03efc7777fad630abed5dd/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/woutputrhel.png)
_Interprétation des moyennes de charge_

### Processus d'arrière-plan et de premier plan

Linux prend en charge le traitement des tâches en arrière-plan et au premier plan. Une tâche dans ce contexte est juste une commande lancée depuis une fenêtre de terminal. Les tâches de premier plan s'exécutent directement à partir du shell, et lorsqu'une tâche de premier plan est en cours d'exécution, les autres tâches doivent attendre l'accès au shell (au moins dans cette fenêtre de terminal si vous utilisez l'interface graphique) jusqu'à ce qu'elle soit terminée. C'est bien lorsque les tâches se terminent rapidement. Mais cela peut avoir un effet négatif si la tâche actuelle va prendre beaucoup de temps (même plusieurs heures) pour se terminer.

Dans de tels cas, vous pouvez exécuter la tâche en arrière-plan et libérer le shell pour d'autres tâches. La tâche d'arrière-plan sera exécutée avec une priorité plus basse, ce qui, à son tour, permettra une exécution fluide des tâches interactives, et vous pourrez taper d'autres commandes dans la fenêtre du terminal pendant que la tâche d'arrière-plan s'exécute. Par défaut, toutes les tâches sont exécutées au premier plan. Vous pouvez mettre une tâche en arrière-plan en ajoutant le suffixe **&** à la commande, par exemple : **updatedb &**.

Vous pouvez soit utiliser **CTRL-Z** pour suspendre une tâche de premier plan, soit **CTRL-C** pour terminer une tâche de premier plan et pouvez toujours utiliser les commandes **bg** et **fg** pour exécuter un processus en arrière-plan et au premier plan, respectivement.

![Processus d'arrière-plan et de premier plan](https://courses.edx.org/assets/courseware/v1/3ff2741d99789599c91efda5c5028150/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bgfgrhel.png)
_Processus d'arrière-plan et de premier plan_

### Gestion des tâches

L'utilitaire **jobs** affiche toutes les tâches en cours d'exécution en arrière-plan. L'affichage montre l'ID de la tâche, l'état et le nom de la commande, comme indiqué ici.

**jobs -l** fournit les mêmes informations que **jobs**, et ajoute le PID des tâches d'arrière-plan.

Les tâches d'arrière-plan sont connectées à la fenêtre du terminal, donc, si vous vous déconnectez, l'utilitaire **jobs** ne montrera pas celles démarrées à partir de cette fenêtre.

![Gestion des tâches](https://courses.edx.org/assets/courseware/v1/8dcff92dcec85e717944d972b96d6fcc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/jobsrhel.png)
_Gestion des tâches_

### La commande ps (Style System V)

**ps** fournit des informations sur les processus en cours d'exécution indexés par PID. Si vous souhaitez une mise à jour répétitive de cet état, vous pouvez utiliser **top** ou d'autres variantes couramment installées (telles que **htop** ou **atop**) à partir de la ligne de commande, ou invoquer l'application de moniteur système graphique de votre distribution.

**ps** a de nombreuses options pour spécifier exactement quelles tâches examiner, quelles informations afficher à leur sujet et précisément quel format de sortie doit être utilisé.

Sans options, **ps** affichera tous les processus s'exécutant sous le shell actuel. Vous pouvez utiliser l'option **-u** pour afficher les informations des processus pour un nom d'utilisateur spécifié. La commande **ps -ef** affiche tous les processus du système en détail complet. La commande **ps -eLf** va un peu plus loin et affiche une ligne d'information pour chaque thread (rappelez-vous, un processus peut contenir plusieurs threads).

![La commande ps (Style System V)](https://courses.edx.org/assets/courseware/v1/a910c16bb6f18c4d38e9ff123a6f5e02/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntupsef.png)
_La commande ps (Style System V)_

### La commande ps (Style BSD)

**ps** a un autre style de spécification d'option, qui découle de la variété BSD d'UNIX, où les options sont spécifiées sans tirets précédents. Par exemple, la commande **ps aux** affiche tous les processus de tous les utilisateurs. La commande **ps axo** vous permet de spécifier quels attributs vous souhaitez visualiser.

La capture d'écran montre un exemple de sortie de **ps** avec les qualificatifs **aux** et **axo**.

![La commande ps (Style BSD)](https://courses.edx.org/assets/courseware/v1/8cca52331523da587fab092df4bc7dba/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/psbsdrhel.png)
_La commande ps (Style BSD)_

### Vidéo : Utilisation de ps

<video controls width="100%" preload="none">

<source src="https://edx-video.net/322cee4c-fb31-4b26-98c0-0fcb3da2b7aa-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### L'arborescence des processus

**pstree** affiche les processus en cours d'exécution sur le système sous la forme d'un diagramme arborescent montrant la relation entre un processus et son processus parent et tout autre processus qu'il a créé. Les entrées répétées d'un processus ne sont pas affichées, et les threads sont affichés entre accolades.

![L'arborescence des processus](https://courses.edx.org/assets/courseware/v1/bce96558c9c9be5c152a567a0c63d392/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ubuntupstree.png)
_L'arborescence des processus_

### top

Bien qu'une vue statique de ce que fait le système soit utile, surveiller les performances du système en direct au fil du temps est également précieux. Une option serait d'exécuter **ps** à intervalles réguliers, disons, toutes les quelques secondes. Une meilleure alternative est d'utiliser **top** pour obtenir des mises à jour constantes en temps réel (toutes les deux secondes par défaut), jusqu'à ce que vous quittiez en tapant **q**. **top** met clairement en évidence quels processus consomment le plus de cycles CPU et de mémoire (en utilisant les commandes appropriées depuis **top**).

![top](https://courses.edx.org/assets/courseware/v1/9eaf15c635ff33e0dbd318a36f295925/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhel.png)
_top_

### Première ligne de la sortie top

La première ligne de la sortie **top** affiche un résumé rapide de ce qui se passe dans le système, notamment :

* Depuis combien de temps le système est en marche
* Combien d'utilisateurs sont connectés
* Quelle est la moyenne de charge

La moyenne de charge détermine à quel point le système est occupé. Une moyenne de charge de 1.00 par CPU indique un système entièrement souscrit, mais non surchargé. Si la moyenne de charge dépasse cette valeur, cela indique que les processus sont en concurrence pour le temps CPU. Si la moyenne de charge est très élevée, cela peut indiquer que le système a un problème, tel qu'un processus emballé (un processus dans un état ne répondant pas).

![Première ligne de la sortie top](https://courses.edx.org/assets/courseware/v1/f70432d89645e43f5d72008706908bbc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline1.png)
_Première ligne de la sortie top_

### Deuxième ligne de la sortie top

La deuxième ligne de la sortie **top** affiche le nombre total de processus, le nombre de processus en cours d'exécution, en sommeil, arrêtés et zombies. Comparer le nombre de processus en cours d'exécution avec la moyenne de charge aide à déterminer si le système a atteint sa capacité ou si peut-être un utilisateur particulier exécute trop de processus. Les processus arrêtés doivent être examinés pour voir si tout fonctionne correctement.

![Deuxième ligne de la sortie top](https://courses.edx.org/assets/courseware/v1/486c9e55bf24f2dca9f628f0a3362bcf/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline2.png)
_Deuxième ligne de la sortie top_

### Troisième ligne de la sortie top

La troisième ligne de la sortie **top** indique comment le temps CPU est divisé entre les utilisateurs (**us**) et le noyau (**sy**) en affichant le pourcentage de temps CPU utilisé pour chacun.

Le pourcentage de tâches utilisateur s'exécutant à une priorité inférieure (**niceness - ni**) est ensuite listé. Le mode inactif (**id**) devrait être bas si la moyenne de charge est élevée, et vice versa. Le pourcentage de tâches en attente (**wa**) d'E/S est listé. Les interruptions incluent le pourcentage d'interruptions matérielles (**hi**) vs logicielles (**si**). Le temps volé (**st**) est généralement utilisé avec les machines virtuelles, qui ont une partie de leur temps CPU inactif pris pour d'autres utilisations.

![Troisième ligne de la sortie top](https://courses.edx.org/assets/courseware/v1/49e0cb9bbb88ccb9cc6ff9c4f32bc243/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline3.png)
_Troisième ligne de la sortie top_

### Quatrième et cinquième lignes de la sortie top

Les quatrième et cinquième lignes de la sortie **top** indiquent l'utilisation de la mémoire, qui est divisée en deux catégories :

* Mémoire physique (RAM) – affichée sur la ligne 4.
* Espace d'échange (Swap) – affiché sur la ligne 5.

Les deux catégories affichent la mémoire totale, la mémoire utilisée et l'espace libre.

Vous devez surveiller l'utilisation de la mémoire très attentivement pour garantir de bonnes performances système. Une fois la mémoire physique épuisée, le système commence à utiliser l'espace d'échange (espace de stockage temporaire sur le disque dur) comme un pool de mémoire étendu, et comme l'accès au disque est beaucoup plus lent que l'accès à la mémoire, cela affectera négativement les performances du système.

Si le système commence à utiliser souvent le swap, vous pouvez ajouter plus d'espace d'échange. Cependant, l'ajout de plus de mémoire physique devrait également être envisagé.

![Quatrième et cinquième lignes de la sortie top](https://courses.edx.org/assets/courseware/v1/8ec74d523983230af0d3c4d4f1556dfb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhelline4-5.png)
_Quatrième et cinquième lignes de la sortie top_

### Liste des processus de la sortie top

Chaque ligne de la liste des processus de la sortie **top** affiche des informations sur un processus. Par défaut, les processus sont classés par utilisation CPU la plus élevée. Les informations suivantes sur chaque processus sont affichées :

* Numéro d'identification du processus (**PID**)
* Propriétaire du processus (**USER**)
* Priorité (**PR**) et valeurs nice (**NI**)
* Mémoire virtuelle (**VIRT**), physique (**RES**) et partagée (**SHR**)
* Statut (**S**)
* Pourcentage de CPU (**%CPU**) et de mémoire (**%MEM**) utilisé
* Temps d'exécution (**TIME+**)
* Commande (**COMMAND**).

![Liste des processus de la sortie top](https://courses.edx.org/assets/courseware/v1/9eaf15c635ff33e0dbd318a36f295925/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/toprhel.png)
_Liste des processus de la sortie top_

### Touches interactives avec top

En plus de rapporter des informations, **top** peut être utilisé de manière interactive pour surveiller et contrôler les processus. Pendant que **top** s'exécute dans une fenêtre de terminal, vous pouvez entrer des commandes d'une seule lettre pour modifier son comportement. Par exemple, vous pouvez afficher les processus les mieux classés en fonction de l'utilisation du processeur ou de la mémoire. Si nécessaire, vous pouvez modifier les priorités des processus en cours d'exécution ou vous pouvez arrêter/tuer un processus.

Le tableau liste ce qui se passe lorsque vous appuyez sur diverses touches lors de l'exécution de **top** :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 689.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Sortie</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">t</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Afficher ou masquer les informations récapitulatives (lignes 2 et 3)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">m</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Afficher ou masquer les informations de mémoire (lignes 4 et 5)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">A</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Trier la liste des processus par les principaux consommateurs de ressources</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">r</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Renice (changer la priorité de) processus spécifiques</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">k</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Tuer un processus spécifique</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">f</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Entrer dans l'écran de configuration de<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">top</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">o</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Sélectionner interactivement un nouvel ordre de tri dans la liste des processus</td></tr></tbody></table>

### Vidéo : Utilisation de top

<video controls width="100%" preload="none">

<source src="https://edx-video.net/da3272c6-9559-41ac-a8b2-1168df22670c-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Vidéo : Utilisation de la surveillance du système

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000200_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Planification de processus futurs à l'aide de at

Supposons que vous deviez effectuer une tâche un jour spécifique dans le futur. Cependant, vous savez que vous serez loin de la machine ce jour-là. Comment allez-vous effectuer la tâche ? Vous pouvez utiliser le programme utilitaire **at** pour exécuter n'importe quelle commande non interactive à un moment spécifié, comme illustré dans la capture d'écran ci-dessous :

![Sortie de la commande at](https://courses.edx.org/assets/courseware/v1/ec37c00269266c49e55f7a52aab93f9a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/atout.png)
_Planification de processus futurs à l'aide de at_

### cron

**cron** est un programme utilitaire de planification basé sur le temps. Il peut lancer des tâches d'arrière-plan de routine à des heures et/ou des jours spécifiques de manière continue. **cron** est piloté par un fichier de configuration appelé **/etc/crontab** (table cron), qui contient les diverses commandes shell qui doivent être exécutées aux heures correctement planifiées. Il existe à la fois des fichiers **crontab** à l'échelle du système et des fichiers individuels basés sur l'utilisateur. Chaque ligne d'un fichier **crontab** représente une tâche, et est composée d'une expression dite **CRON**, suivie d'une commande shell à exécuter.

Taper **crontab -e** ouvrira l'éditeur crontab pour modifier les tâches existantes ou pour créer de nouvelles tâches. Chaque ligne du fichier **crontab** contiendra 6 champs :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 689.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="26%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Champ</strong></span></td><td width="26%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td><td width="28%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Valeurs</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">MIN</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Minutes</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0 à 59</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">HOUR</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Champ Heure</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0 à 23</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">DOM</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Jour du Mois</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1-31</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">MON</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Champ Mois</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1-12</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">DOW</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Jour de la Semaine</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0-6 (0 = Dimanche)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CMD</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Commande</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Toute commande à exécuter</td></tr></tbody></table>

**Exemples :**

* L'entrée *** * * * * /usr/local/bin/execute/this/script.sh** planifiera une tâche pour exécuter **script.sh** chaque minute de chaque heure de chaque jour du mois, et chaque mois et chaque jour de la semaine.
* L'entrée **30 08 10 06 * /home/sysadmin/full-backup** planifiera une sauvegarde complète à 8h30, le 10 juin, quel que soit le jour de la semaine.

### sleep

Parfois, une commande ou une tâche doit être retardée ou suspendue. Supposons, par exemple, qu'une application ait lu et traité le contenu d'un fichier de données et doive ensuite enregistrer un rapport sur un système de sauvegarde. Si le système de sauvegarde est actuellement occupé ou non disponible, l'application peut être mise en sommeil (attente) jusqu'à ce qu'elle puisse terminer son travail. Un tel délai pourrait être pour monter le périphérique de sauvegarde et le préparer à l'écriture.

**sleep** suspend l'exécution pendant au moins la période de temps spécifiée, qui peut être donnée comme le nombre de secondes (par défaut), minutes, heures ou jours. Une fois ce temps écoulé (ou qu'un signal d'interruption a été reçu), l'exécution reprendra.

La syntaxe est :

**sleep NOMBRE[SUFFIXE]...**

où **SUFFIXE** peut être :

* **s** pour secondes (par défaut)
* **m** pour minutes
* **h** pour heures
* **d** pour jours.

**sleep** et **at** sont assez différents ; **sleep** retarde l'exécution pendant une période spécifique, tandis que **at** démarre l'exécution à un moment ultérieur.

![sleep](https://courses.edx.org/assets/courseware/v1/b9444a7d9db9ee97c557d2373530b24d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sleepsuse.png)
_sleep_

## Résumé du chapitre

Vous avez terminé le chapitre 9. Résumons les concepts clés couverts :

* Les processus sont utilisés pour effectuer diverses tâches sur le système.
* Les processus peuvent être à thread unique ou multi-threadés.
* Les processus peuvent être de différents types, tels qu'interactifs et non interactifs.
* Chaque processus a un identifiant unique (PID) pour permettre au système d'exploitation de le suivre.
* La valeur nice, ou niceness, peut être utilisée pour définir la priorité.
* **ps** fournit des informations sur les processus en cours d'exécution.
* Vous pouvez utiliser **top** pour obtenir des mises à jour constantes en temps réel sur les performances globales du système, ainsi que des informations sur les processus en cours d'exécution sur le système.
* La moyenne de charge indique la quantité d'utilisation du système à des moments particuliers.
* Linux prend en charge le traitement en arrière-plan et au premier plan pour une tâche.
* **at** exécute toute commande non interactive à un moment spécifié.
* **cron** est utilisé pour planifier des tâches qui doivent être effectuées à intervalles réguliers.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 10 : Opérations sur les fichiers

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Explorer le système de fichiers et sa hiérarchie.
* Expliquer l'architecture du système de fichiers.
* Comparer des fichiers et identifier différents types de fichiers.
* Sauvegarder et compresser des données.

### Introduction aux systèmes de fichiers

Sous Linux (et tous les systèmes d'exploitation de type UNIX), on dit souvent "Tout est un fichier", ou du moins c'est traité comme tel. Cela signifie que vous traitiez des fichiers de données normaux et des documents, ou des périphériques tels que des cartes son et des imprimantes, vous interagissez avec eux par le même type d'opérations d'Entrée/Sortie (E/S). Cela simplifie les choses : vous ouvrez un "fichier" et effectuez des opérations normales comme lire le fichier et écrire dessus (ce qui est une raison pour laquelle les éditeurs de texte, que vous découvrirez dans une section à venir, sont si importants).

Sur de nombreux systèmes (y compris Linux), le système de fichiers est structuré comme un arbre. L'arbre est généralement représenté comme inversé, et commence à ce qu'on appelle le plus souvent le **répertoire racine**, qui marque le début du système de fichiers hiérarchique et est aussi parfois appelé le tronc, ou simplement noté par **/**. Le répertoire racine n'est _pas_ la même chose que l'utilisateur root. Le système de fichiers hiérarchique contient également d'autres éléments dans le chemin (noms de répertoires), qui sont séparés par des barres obliques (**/**), comme dans **/usr/bin/emacs**, où le dernier élément est le nom de fichier réel.

Dans cette section, vous apprendrez quelques concepts de base, y compris la hiérarchie du système de fichiers, ainsi que les partitions de disque.

![Systèmes de fichiers](https://courses.edx.org/assets/courseware/v1/6c6a76e5e83450a2f75777a86ba8e790/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen_03.jpg)
_Systèmes de fichiers_

### Variétés de systèmes de fichiers

Linux prend en charge un certain nombre de types de systèmes de fichiers natifs, expressément créés par les développeurs Linux, tels que :

* ext3
* ext4
* squashfs
* btrfs

Il offre également des implémentations de systèmes de fichiers utilisés sur d'autres systèmes d'exploitation étrangers, tels que ceux de :

* Windows (ntfs, vfat)
* SGI (xfs)
* IBM (jfs)
* MacOS (hfs, hfs+)

De nombreux systèmes de fichiers plus anciens et hérités, tels que FAT, sont également pris en charge.

Il est souvent le cas que plus d'un type de système de fichiers est utilisé sur une machine, en fonction de considérations telles que la taille des fichiers, la fréquence à laquelle ils sont modifiés, quel type de matériel ils reposent et quel type de vitesse d'accès est nécessaire, etc. Les types de systèmes de fichiers les plus avancés couramment utilisés sont les variétés **journalisées** : ext4, xfs, btrfs et jfs. Ceux-ci ont de nombreuses fonctionnalités de pointe et des performances élevées, et sont très difficiles à corrompre accidentellement.

### Partitions Linux

Chaque système de fichiers sur un système Linux occupe une **partition** de disque. Les partitions aident à organiser le contenu des disques selon le type et l'utilisation des données contenues. Par exemple, les programmes importants nécessaires pour exécuter le système sont souvent conservés sur une partition séparée (connue sous le nom de **racine** ou **/**) de celle qui contient les fichiers appartenant aux utilisateurs réguliers de ce système (**/home**). De plus, les fichiers temporaires créés et détruits pendant le fonctionnement normal de Linux peuvent être situés sur des partitions dédiées. Un avantage de ce type d'isolement par type et variabilité est que lorsque tout l'espace disponible sur une partition particulière est épuisé, le système peut toujours fonctionner normalement.

L'image montre l'utilisation de l'utilitaire **gparted**, qui affiche la disposition des partitions sur un système qui a quatre systèmes d'exploitation dessus : RHEL 8, CentOS 7, Ubuntu et Windows.

![Partitions Linux : gparted](https://courses.edx.org/assets/courseware/v1/6b82906abb49600a3143f0f3fd8208de/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gparted.png)
_Partitions Linux : gparted_

### Points de montage

Avant de pouvoir commencer à utiliser un système de fichiers, vous devez le **monter** sur l'arborescence du système de fichiers à un point de montage. C'est simplement un répertoire (qui peut ou non être vide) où le système de fichiers doit être greffé. Parfois, vous devrez peut-être créer le répertoire s'il n'existe pas déjà.

![Points de montage](https://courses.edx.org/assets/courseware/v1/90eea9eba0b63783a8bcf2b85ae8a9e3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen06.jpg)
_Points de montage_

**_AVERTISSEMENT_**_ : Si vous montez un système de fichiers sur un répertoire non vide, le contenu précédent de ce répertoire est recouvert et non accessible jusqu'à ce que le système de fichiers soit démonté. Ainsi, les points de montage sont généralement des répertoires vides._

### Montage et démontage

La commande **mount** est utilisée pour attacher un système de fichiers (qui peut être local à l'ordinateur ou sur un réseau) quelque part dans l'arborescence du système de fichiers. Les arguments de base sont le **nœud de périphérique** et le point de montage. Par exemple,

**$ sudo mount /dev/sda5 /home**

attachera le système de fichiers contenu dans la partition de disque associée au nœud de périphérique **/dev/sda5** dans l'arborescence du système de fichiers au point de montage **/home**. Il existe d'autres moyens de spécifier la partition autre que le nœud de périphérique, comme l'utilisation de l'étiquette de disque ou de l'UUID.

Pour démonter la partition, la commande serait :

**$ sudo umount /home**

Notez que la commande est **umount**, pas unmount ! Seul un utilisateur root (connecté en tant que root, ou utilisant **sudo**) a le privilège d'exécuter ces commandes, à moins que le système n'ait été configuré autrement.

Si vous voulez qu'il soit automatiquement disponible à chaque démarrage du système, vous devez modifier **/etc/fstab** en conséquence (le nom est l'abréviation de filesystem table). Regarder ce fichier vous montrera la configuration de tous les systèmes de fichiers préconfigurés. **man fstab** affichera comment ce fichier est utilisé et comment le configurer.

Exécuter **mount** sans aucun argument affichera tous les systèmes de fichiers actuellement montés.

La commande **df -Th** (disk-free) affichera des informations sur les systèmes de fichiers montés, y compris le type de système de fichiers, et des statistiques d'utilisation sur l'espace actuellement utilisé et disponible.

![Montage et démontage](https://courses.edx.org/assets/courseware/v1/18cd65d8ee6e189efd405e7e3c890f2d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/dfmountdebian.png)
_Montage et démontage_

### NFS et systèmes de fichiers réseau

Il est souvent nécessaire de partager des données entre des systèmes physiques qui peuvent être soit au même endroit, soit n'importe où accessible par Internet. Un système de fichiers réseau (aussi parfois appelé distribué) peut avoir toutes ses données sur une machine ou les avoir réparties sur plus d'un nœud réseau. Une variété de systèmes de fichiers différents peuvent être utilisés localement sur les machines individuelles ; un système de fichiers réseau peut être considéré comme un regroupement de systèmes de fichiers de niveau inférieur de types variés.

![Architecture client-serveur NFS](https://courses.edx.org/assets/courseware/v1/312ecb4a904d47191a99c6b1443f8b32/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/NFS_LFS101.png)
_****L'architecture client-serveur de NFS****<span class="-mobiledoc-kit__atom">‌‌</span>(basé sur l'original de [www.ibm.com](https://www.ibm.com/developerworks/library/l-network-filesystems/))_

De nombreux administrateurs système montent les répertoires personnels des utilisateurs distants sur un serveur afin de leur donner accès aux mêmes fichiers et fichiers de configuration sur plusieurs systèmes clients. Cela permet aux utilisateurs de se connecter à différents ordinateurs, tout en ayant accès aux mêmes fichiers et ressources.

Le système de fichiers le plus courant est nommé simplement **NFS** (le **N**etwork **F**ile**s**ystem). Il a une très longue histoire et a été développé pour la première fois par Sun Microsystems. Une autre implémentation courante est **CIFS** (aussi appelé **SAMBA**), qui a des racines Microsoft. Nous limiterons notre attention dans ce qui suit à NFS.

### NFS sur le serveur

Nous allons maintenant examiner en détail comment utiliser NFS sur le serveur.

Sur la machine serveur, NFS utilise des **démons** (processus de mise en réseau et de service intégrés sous Linux) et d'autres serveurs système sont démarrés en ligne de commande en tapant :

**$ sudo systemctl start nfs**

_**NOTE**_ : Sur RHEL/CentOS 8, le service est appelé **nfs-server**, pas **nfs**.

Le fichier texte **/etc/exports** contient les répertoires et les permissions qu'un hôte est prêt à partager avec d'autres systèmes via NFS. Une entrée très simple dans ce fichier peut ressembler à ce qui suit :

**/projects *.example.com(rw)**

Cette entrée permet au répertoire **/projects** d'être monté en utilisant NFS avec des permissions de lecture et d'écriture (**rw**) et partagé avec d'autres hôtes dans le domaine **example.com**. Comme nous le détaillerons dans le chapitre suivant, chaque fichier sous Linux a trois permissions possibles : lecture (**r**), écriture (**w**) et exécution (**x**).

Après avoir modifié le fichier **/etc/exports**, vous pouvez taper **exportfs -av** pour notifier Linux des répertoires que vous autorisez à être montés à distance en utilisant NFS. Vous pouvez également redémarrer NFS avec **sudo systemctl restart nfs**, mais c'est plus lourd, car cela arrête NFS pendant un court instant avant de le redémarrer. Pour vous assurer que le service NFS démarre chaque fois que le système est démarré, émettez **sudo systemctl enable nfs**.

![NFS sur le serveur](https://courses.edx.org/assets/courseware/v1/c9d06cf0b5114c7ff0553aae608e96bd/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/exportsnfs.png)
_NFS sur le serveur_

### NFS sur le client

Sur la machine cliente, s'il est souhaité que le système de fichiers distant soit monté automatiquement au démarrage du système, **/etc/fstab** est modifié pour accomplir cela. Par exemple, une entrée dans le **/etc/fstab** du client pourrait ressembler à ce qui suit :

**servername:/projects /mnt/nfs/projects nfs defaults 0 0**

Vous pouvez également monter le système de fichiers distant sans redémarrage ou comme un montage unique en utilisant directement la commande **mount** :

**$ sudo mount servername:/projects /mnt/nfs/projects**

Rappelez-vous, si **/etc/fstab** n'est pas modifié, ce montage distant ne sera pas présent la prochaine fois que le système sera redémarré. De plus, vous voudrez peut-être utiliser l'option **nofail** dans **fstab** au cas où le serveur NFS ne serait pas actif au démarrage.

![NFS sur le client](https://courses.edx.org/assets/courseware/v1/80a14e19e05a9cfdc8b19f09d20e8e07/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/nfsclientubuntu.png)
_NFS sur le client_

### Aperçu des répertoires personnels des utilisateurs

Dans cette section, vous apprendrez à identifier et différencier les répertoires les plus importants trouvés sous Linux. Nous commençons par l'espace de répertoire personnel des utilisateurs ordinaires.

Chaque utilisateur a un répertoire personnel, généralement placé sous **/home**. Le répertoire **/root** ("slash-root") sur les systèmes Linux modernes n'est rien de plus que le répertoire personnel de l'utilisateur root (ou superutilisateur, ou compte administrateur système).

Sur les systèmes multi-utilisateurs, l'infrastructure du répertoire **/home** est souvent montée comme un système de fichiers séparé sur sa propre partition, ou même exportée (partagée) à distance sur un réseau via NFS.

Parfois, vous pouvez regrouper les utilisateurs en fonction de leur département ou fonction. Vous pouvez ensuite créer des sous-répertoires sous le répertoire **/home** pour chacun de ces groupes. Par exemple, une école peut organiser **/home** avec quelque chose comme ce qui suit :

**/home/faculty/**
**/home/staff/**
**/home/students/**

![répertoires personnels](https://courses.edx.org/assets/courseware/v1/9817790ba352d4047027eb1d61516db5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Home_directories.png)
_Répertoires personnels_

### Les répertoires /bin et /sbin

Le répertoire **/bin** contient des binaires exécutables, des commandes essentielles utilisées pour démarrer le système ou en mode mono-utilisateur, et des commandes essentielles requises par tous les utilisateurs du système, telles que **cat**, **cp**, **ls**, **mv**, **ps** et **rm**.

![répertoire /bin](https://courses.edx.org/assets/courseware/v1/0f4cc85473fc7a961b3bc98b87d33a24/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsbin.png)
_Répertoire /bin_

De même, le répertoire **/sbin** est destiné aux binaires essentiels liés à l'administration système, tels que **fsck** et **ip**. Pour afficher une liste de ces programmes, tapez :

**$ ls /bin /sbin**

![Répertoire /sbin](https://courses.edx.org/assets/courseware/v1/f60523278764a748d479ef923f75b0d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lssbin.png)
_Répertoire /sbin_

Les commandes qui ne sont pas essentielles (théoriquement) pour que le système démarre ou fonctionne en mode mono-utilisateur sont placées dans les répertoires **/usr/bin** et **/usr/sbin**. Historiquement, cela était fait pour que **/usr** puisse être monté comme un système de fichiers séparé qui pourrait être monté à un stade ultérieur du démarrage du système ou même sur un réseau. Cependant, de nos jours, la plupart trouvent cette distinction obsolète. En fait, de nombreuses distributions ont été découvertes incapables de démarrer avec cette séparation, car cette modalité n'avait pas été utilisée ou testée depuis longtemps.

Ainsi, sur certaines des distributions Linux les plus récentes, **/usr/bin** et **/bin** sont en fait simplement liés symboliquement ensemble, tout comme **/usr/sbin** et **/sbin**.

### Le système de fichiers /proc

Certains systèmes de fichiers, comme celui monté à **/proc**, sont appelés **pseudo-systèmes de fichiers** car ils n'ont aucune présence permanente nulle part sur le disque.

Le système de fichiers **/proc** contient des fichiers virtuels (fichiers qui n'existent qu'en mémoire) qui permettent de visualiser les données du noyau en constante évolution. **/proc** contient des fichiers et des répertoires qui imitent les structures du noyau et les informations de configuration. Il ne contient pas de vrais fichiers, mais des informations système d'exécution, par exemple la mémoire système, les périphériques montés, la configuration matérielle, etc. Certaines entrées importantes dans **/proc** sont :

**/proc/cpuinfo**
**/proc/interrupts**
**/proc/meminfo**
**/proc/mounts**
**/proc/partitions**
**/proc/version**

**/proc** a également des sous-répertoires, notamment :

**/proc/<Process-ID-#>**
**/proc/sys**

Le premier exemple montre qu'il y a un répertoire pour chaque processus en cours d'exécution sur le système, qui contient des informations vitales à son sujet. Le deuxième exemple montre un répertoire virtuel qui contient beaucoup d'informations sur l'ensemble du système, en particulier son matériel et sa configuration. Le système de fichiers **/proc** est très utile car les informations qu'il rapporte ne sont rassemblées qu'au besoin et n'ont jamais besoin de stockage sur le disque.

![Le système de fichiers proc](https://courses.edx.org/assets/courseware/v1/5851a953799d1db46c17d156b1cd23bc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsproc.png)
_Le système de fichiers /proc_

### Le répertoire /dev

Le répertoire **/dev** contient des **nœuds de périphérique**, un type de pseudo-fichier utilisé par la plupart des périphériques matériels et logiciels, à l'exception des périphériques réseau. Ce répertoire est :

* Vide sur la partition de disque lorsqu'elle n'est pas montée
* Contient des entrées qui sont créées par le système **udev**, qui crée et gère les nœuds de périphérique sous Linux, les créant dynamiquement lorsque des périphériques sont trouvés. Le répertoire **/dev** contient des éléments tels que :

1. **/dev/sda1** (première partition sur le premier disque dur)
2. **/dev/lp1** (deuxième imprimante)
3. **/dev/random** (une source de nombres aléatoires).

![Le répertoire /dev](https://courses.edx.org/assets/courseware/v1/ee00318b4e056829ec5580f3f8c6ca10/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsdev.png)
_Le répertoire /dev_

### Le répertoire /var

Le répertoire **/var** contient des fichiers dont on s'attend à ce qu'ils changent de taille et de contenu pendant que le système fonctionne (var signifie variable), tels que les entrées dans les répertoires suivants :

* Fichiers journaux système : **/var/log**
* Paquets et fichiers de base de données : **/var/lib**
* Files d'attente d'impression : **/var/spool**
* Fichiers temporaires : **/var/tmp**.

![Le répertoire /var](https://courses.edx.org/assets/courseware/v1/2d840d9232739d72bb6a2af07308a46d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsvar.png)
_Le répertoire /var_

Le répertoire **/var** peut être placé sur son propre système de fichiers afin que la croissance des fichiers puisse être accommodée et que toute explosion de la taille des fichiers n'affecte pas fatalement le système. Les répertoires de services réseau tels que **/var/ftp** (le service FTP) et **/var/www** (le service web HTTP) se trouvent également sous **/var**.

![Le répertoire /var](https://courses.edx.org/assets/courseware/v1/948dafcdc47f674bd2c0b5c1560ebb7c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/varfolders.png)
_Le répertoire /var_

### Le répertoire /etc

Le répertoire **/etc** est le foyer des fichiers de configuration du système. Il ne contient aucun programme binaire, bien qu'il y ait quelques scripts exécutables. Par exemple, **/etc/resolv.conf** indique au système où aller sur le réseau pour obtenir les mappages de nom d'hôte à adresse IP (DNS). Des fichiers comme **passwd**, **shadow** et **group** pour gérer les comptes utilisateurs se trouvent dans le répertoire **/etc**. Bien que certaines distributions aient historiquement eu leur propre infrastructure étendue sous **/etc** (par exemple, Red Hat et SUSE ont utilisé **/etc/sysconfig**), avec l'avènement de **systemd**, il y a beaucoup plus d'uniformité entre les distributions aujourd'hui.

Notez que **/etc** est pour les fichiers de configuration à l'échelle du système et seul le superutilisateur peut modifier les fichiers là-bas. Les fichiers de configuration spécifiques à l'utilisateur se trouvent toujours sous leur répertoire personnel.

![Le répertoire /etc](https://courses.edx.org/assets/courseware/v1/4e485f3695bdc1468b81a286f3538f57/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/debianetc.png)
_Le répertoire /etc_

### Le répertoire /boot

Le répertoire **/boot** contient les quelques fichiers essentiels nécessaires pour démarrer le système. Pour chaque noyau alternatif installé sur le système, il y a quatre fichiers :

1. **vmlinuz**
Le noyau Linux compressé, requis pour le démarrage.
2. **initramfs**
Le système de fichiers ram initial, requis pour le démarrage, parfois appelé initrd, pas initramfs.
3. **config**
Le fichier de configuration du noyau, utilisé uniquement pour le débogage et la comptabilité.
4. **System.map**
Table des symboles du noyau, utilisée uniquement pour le débogage.

Chacun de ces fichiers a une version du noyau ajoutée à son nom.

Les fichiers du Grand Unified Bootloader (GRUB) tels que **/boot/grub/grub.conf** ou **/boot/grub2/grub2.cfg** se trouvent également sous le répertoire **/boot**.

![Le répertoire /boot](https://courses.edx.org/assets/courseware/v1/cc0ea7111ab46e927a9a6f2b5bfeddab/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bootdir.png)
_Le répertoire /boot_

La capture d'écran montre un exemple de liste du répertoire **/boot**, prise d'un système RHEL qui a plusieurs noyaux installés, y compris ceux fournis par la distribution et ceux compilés sur mesure. Les noms varieront et les choses auront tendance à sembler quelque peu différentes sur une distribution différente.

### Les répertoires /lib et /lib64

**/lib** contient des bibliothèques (code commun partagé par les applications et nécessaire à leur exécution) pour les programmes essentiels dans **/bin** et **/sbin**. Ces noms de fichiers de bibliothèque commencent soit par **ld** soit par **lib**. Par exemple, **/lib/libncurses.so.5.9**.

La plupart d'entre elles sont ce qu'on appelle des bibliothèques chargées dynamiquement (également connues sous le nom de bibliothèques partagées ou Shared Objects (SO)). Sur certaines distributions Linux, il existe un répertoire **/lib64** contenant des bibliothèques 64 bits, tandis que **/lib** contient des versions 32 bits.

Sur les distributions Linux récentes, on trouve :

![Les répertoires /lib et /lib64](https://courses.edx.org/assets/courseware/v1/a8ab641d68e711bfc4892c0e33b5033b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lslib.png)
_Les répertoires /lib et /lib64_

c'est-à-dire, tout comme pour **/bin** et **/sbin**, les répertoires pointent simplement vers ceux sous **/usr**.

Les modules du noyau (code du noyau, souvent des pilotes de périphériques, qui peuvent être chargés et déchargés sans redémarrer le système) sont situés dans **/lib/modules/<numéro-version-noyau>**.

![contenu de /lib/modules](https://courses.edx.org/assets/courseware/v1/43a3b062df788fc58b09fca237179261/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/libmodules.png)
_Contenu de /lib/modules_

### Supports amovibles : les répertoires /media, /run et /mnt

On utilise souvent des supports amovibles, tels que des clés USB, des CD et des DVD. Pour rendre le matériel accessible via le système de fichiers régulier, il doit être monté à un emplacement pratique. La plupart des systèmes Linux sont configurés de sorte que tout support amovible soit automatiquement monté lorsque le système remarque que quelque chose a été branché.

Bien qu'historiquement cela se faisait sous le répertoire **/media**, les distributions Linux modernes placent ces points de montage sous le répertoire **/run**. Par exemple, une clé USB avec une étiquette **myusbdrive** pour un utilisateur nommé **student** serait montée à **/run/media/student/myusbdrive**.

![Image montrant des CD, des disquettes, des cassettes, des clés USB et des cartes mémoire](https://courses.edx.org/assets/courseware/v1/02712e7fe9b99bf10e71a429cf756904/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/Forty_years_of_Removable_Storage.jpg)

Le répertoire **/mnt** a été utilisé depuis les premiers jours d'UNIX pour monter temporairement des systèmes de fichiers. Ceux-ci peuvent être ceux sur des supports amovibles, mais plus souvent pourraient être des systèmes de fichiers réseau, qui ne sont pas normalement montés. Ou ceux-ci peuvent être des partitions temporaires, ou des systèmes de fichiers dits **loopback**, qui sont des fichiers qui prétendent être des partitions.

![Le répertoire /run](https://courses.edx.org/assets/courseware/v1/42f91969ba3ca6077991a47dc1348f00/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsrun.png)
_Le répertoire /run_

### Répertoires supplémentaires sous /

Il existe quelques répertoires supplémentaires à trouver sous le répertoire racine :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 826.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Nom du répertoire<br style="line-height: 1.4em;"></strong></span></td><td align="center" bgcolor="#003f60" width="80%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/opt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Paquets logiciels d'application optionnels</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/sys</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pseudo-système de fichiers virtuel donnant des informations sur le système et le matériel<br style="line-height: 1.4em;">Peut être utilisé pour modifier les paramètres du système et à des fins de débogage</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/srv</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Données spécifiques au site servies par le système<br style="line-height: 1.4em;">Rarement utilisé</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/tmp</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Fichiers temporaires ; sur certaines distributions effacés lors d'un redémarrage et/ou peuvent être en fait un ramdisk en mémoire</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Applications, utilitaires et données multi-utilisateurs</span></td></tr></tbody></table>

### L'arborescence du répertoire /usr

L'arborescence du répertoire **/usr** contient des programmes et des scripts théoriquement non essentiels (dans le sens où ils ne devraient pas être nécessaires pour démarrer initialement le système) et possède au moins les sous-répertoires suivants :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 826.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Nom du répertoire<br style="line-height: 1.4em;"></strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/include</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Fichiers d'en-tête utilisés pour compiler des applications</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/lib</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Bibliothèques pour les programmes dans<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/bin</span></strong></span><span>&nbsp;</span>et<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/sbin</span></strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/lib64</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Bibliothèques 64 bits pour les programmes 64 bits dans<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/bin</span></strong></span><span>&nbsp;</span>et<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/sbin</span></strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/sbin</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Binaires système non essentiels, tels que les démons système</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/share</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Données partagées utilisées par les applications, généralement indépendantes de l'architecture</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/src</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Code source, généralement pour le noyau Linux</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/local</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Données et programmes spécifiques à la machine locale ; les sous-répertoires incluent&nbsp;<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">bin</strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">sbin</span></strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">lib</span></strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">share</span></strong></span>,&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">include</span></strong></span>, etc.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/usr/bin</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">C'est le répertoire principal des commandes exécutables sur le système</span></td></tr></tbody></table>

### Comparaison de fichiers avec diff

Maintenant que vous connaissez le système de fichiers et sa structure, apprenons à gérer les fichiers et les répertoires.

**diff** est utilisé pour comparer des fichiers et des répertoires. Ce programme utilitaire souvent utilisé possède de nombreuses options utiles (voir : **man diff**) notamment :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 826.5px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Option diff</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-c</span></strong><br style="line-height: 1.4em;"></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Fournit une liste des différences qui inclut&nbsp;trois&nbsp;lignes de contexte avant et après les lignes différant en contenu</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-r</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisé pour comparer récursivement&nbsp;les sous-répertoires, ainsi que le répertoire actuel</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ignorer la casse des lettres</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ignorer les différences dans les espaces et les tabulations (espaces blancs)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-q</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Être silencieux : ne signaler que si les fichiers sont différents sans lister les différences</span></td></tr></tbody></table>

Pour comparer deux fichiers, à l'invite de commande, tapez **diff [options] <nomfichier1> <nomfichier2>**. **diff** est destiné à être utilisé pour les fichiers texte ; pour les fichiers binaires, on peut utiliser **cmp**.

Dans cette section, vous apprendrez des méthodes supplémentaires pour comparer des fichiers et comment appliquer des correctifs (patches) aux fichiers.

### Utilisation de diff3 et patch

Vous pouvez comparer trois fichiers à la fois en utilisant **diff3**, qui utilise un fichier comme base de référence pour les deux autres. Par exemple, supposons que vous et un collègue ayez tous deux apporté des modifications au même fichier en travaillant en même temps indépendamment. **diff3** peut montrer les différences basées sur le fichier commun avec lequel vous avez tous les deux commencé. La syntaxe pour **diff3** est la suivante :

**$ diff3 MON-FICHIER FICHIER-COMMUN VOTRE-FICHIER**

Le graphique montre l'utilisation de **diff3**.

![Utilisation de diff3](https://courses.edx.org/assets/courseware/v1/33d173c484df38d28dcb85d2a49a010e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/diff3centos.png)
_Utilisation de diff3_

De nombreuses modifications du code source et des fichiers de configuration sont distribuées en utilisant des correctifs, qui sont appliqués, sans surprise, avec le programme **patch**. Un fichier de correctif contient les deltas (changements) nécessaires pour mettre à jour une ancienne version d'un fichier vers la nouvelle. Les fichiers de correctif sont en fait produits en exécutant **diff** avec les options correctes, comme dans :

**$ diff -Nur originalfile newfile > patchfile**

Distribuer uniquement le correctif est plus concis et efficace que de distribuer le fichier entier. Par exemple, si une seule ligne doit changer dans un fichier qui contient 1000 lignes, le fichier de correctif ne fera que quelques lignes.

![Utilisation de patch](https://courses.edx.org/assets/courseware/v1/6bb8e04e57d74c83cd0de7335128892d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/patchrhel.png)
_Utilisation de patch_

Pour appliquer un correctif, vous pouvez simplement faire l'une des deux méthodes ci-dessous :

**$ patch -p1 < patchfile**
**$ patch originalfile patchfile**

La première utilisation est plus courante, car elle est souvent utilisée pour appliquer des modifications à une arborescence de répertoires entière, plutôt qu'à un seul fichier, comme dans le deuxième exemple. Pour comprendre l'utilisation de l'option **-p1** et bien d'autres, consultez la page man de **patch**.

### Utilisation de l'utilitaire file

Sous Linux, l'extension d'un fichier ne le catégorise souvent pas comme cela pourrait être le cas dans d'autres systèmes d'exploitation. On ne peut pas supposer qu'un fichier nommé **file.txt** est un fichier texte et non un programme exécutable. Sous Linux, un nom de fichier est généralement plus significatif pour l'utilisateur du système que pour le système lui-même. En fait, la plupart des applications examinent directement le contenu d'un fichier pour voir quel type d'objet il s'agit plutôt que de se fier à une extension. C'est très différent de la façon dont Windows gère les noms de fichiers, où un nom de fichier se terminant par **.exe**, par exemple, représente un fichier binaire exécutable.

La nature réelle d'un fichier peut être vérifiée en utilisant l'utilitaire **file**. Pour les noms de fichiers donnés en arguments, il examine le contenu et certaines caractéristiques pour déterminer si les fichiers sont du texte brut, des bibliothèques partagées, des programmes exécutables, des scripts ou autre chose.

![Utilisation de l'utilitaire file](https://courses.edx.org/assets/courseware/v1/6bc751d9dafe1a200e66f2eb4479db0e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/fileu1910.png)
_Utilisation de l'utilitaire file_

## Sauvegarde des données

Il existe de nombreuses façons de sauvegarder des données ou même votre système entier. Les moyens de base pour le faire incluent l'utilisation de la copie simple avec **cp** et l'utilisation du plus robuste **rsync**.

Les deux peuvent être utilisés pour synchroniser des arborescences de répertoires entières. Cependant, **rsync** est plus efficace, car il vérifie si le fichier copié existe déjà. Si le fichier existe et qu'il n'y a pas de changement de taille ou d'heure de modification, **rsync** évitera une copie inutile et gagnera du temps. De plus, parce que **rsync** ne copie que les parties des fichiers qui ont réellement changé, il peut être très rapide.

![Ordinateurs connectés à un nuage à l'aide de lignes avec des flèches aux deux extrémités. À l'intérieur du nuage, il est écrit Sauvegarde](https://courses.edx.org/assets/courseware/v1/415a756cb43f614a31ef953a88377396/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen34.jpg)

**cp** ne peut copier des fichiers que vers et depuis des destinations sur la machine locale (à moins que vous ne copiez vers ou depuis un système de fichiers monté à l'aide de NFS), mais **rsync** peut également être utilisé pour copier des fichiers d'une machine à une autre. Les emplacements sont désignés sous la forme **cible:chemin**, où **cible** peut être sous la forme de **quelquun@hote**. La partie **quelquun@** est facultative et utilisée si l'utilisateur distant est différent de l'utilisateur local.

**rsync** est très efficace lors de la copie récursive d'une arborescence de répertoires vers une autre, car seules les différences sont transmises sur le réseau. On synchronise souvent l'arborescence de répertoires de destination avec l'origine, en utilisant l'option -r pour parcourir récursivement l'arborescence de répertoires en copiant tous les fichiers et répertoires en dessous de celui listé comme source.

### Utilisation de rsync

**rsync** est un utilitaire très puissant. Par exemple, un moyen très utile de sauvegarder un répertoire de projet pourrait être d'utiliser la commande suivante :

**$ rsync -r project-X archive-machine:archives/project-X**

Notez que **rsync** peut être très destructeur ! Une mauvaise utilisation accidentelle peut faire beaucoup de mal aux données et aux programmes, en copiant par inadvertance des modifications là où elles ne sont pas souhaitées. Prenez soin de spécifier les options et les chemins corrects. Il est fortement recommandé de tester d'abord votre commande **rsync** en utilisant l'option **-dry-run** pour vous assurer qu'elle fournit les résultats que vous souhaitez.

![Touche de clavier disant Sauvegarde](https://courses.edx.org/assets/courseware/v1/b466cf17ce5d978de488e7f13989c686/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen35.jpg)

Pour utiliser **rsync** à l'invite de commande, tapez **rsync fichier_source fichier_destination**, où chaque fichier peut être sur la machine locale ou sur une machine en réseau ; Le contenu de **fichier_source** sera copié vers **fichier_destination**.

Une bonne combinaison d'options est montrée dans :

**$ rsync --progress -avrxH --delete sourcedir destdir**

Les données de fichier sont souvent compressées pour économiser de l'espace disque et réduire le temps nécessaire pour transmettre des fichiers sur les réseaux.

Linux utilise un certain nombre de méthodes pour effectuer cette compression, notamment :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">L'utilitaire de compression Linux le plus fréquemment utilisé</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bzip2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Produit des fichiers significativement plus petits que ceux produits par<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">gzip</strong></span></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">L'utilitaire de compression le plus efficace en termes d'espace utilisé sous Linux</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">zip</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Est souvent requis pour examiner et décompresser des archives provenant d'autres systèmes d'exploitation</td></tr></tbody></table>

Ces techniques varient dans l'efficacité de la compression (combien d'espace est économisé) et dans le temps qu'elles prennent pour compresser ; généralement, les techniques les plus efficaces prennent plus de temps. Le temps de décompression ne varie pas autant entre les différentes méthodes.

De plus, l'utilitaire **tar** est souvent utilisé pour regrouper des fichiers dans une archive, puis compresser l'archive entière en une seule fois.

### Compression de données à l'aide de gzip

**gzip** est l'utilitaire de compression Linux le plus souvent utilisé. Il compresse très bien et est très rapide. Le tableau suivant fournit quelques exemples d'utilisation :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip *</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Compresse tous les fichiers dans le répertoire actuel ; chaque fichier est compressé et renommé avec une extension<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">.gz</span></strong></span></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">gzip -r projectX</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresse tous les fichiers dans le répertoire&nbsp;<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">projectX</span></strong></span>, ainsi que tous les fichiers dans tous les répertoires sous<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">projectX</span></strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gunzip foo</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Décompresse<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">foo</span></strong></span><span>&nbsp;</span>trouvé dans le fichier<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">foo.gz</span></strong></span>. Sous le capot, la commande&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gunzip</span></strong><span>&nbsp;</span>est en fait la même que<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip –d</span></strong></span>.</td></tr></tbody></table>

### Compression de données à l'aide de xz

**xz** est l'utilitaire de compression le plus efficace en termes d'espace utilisé sous Linux et est utilisé pour [stocker les archives du noyau Linux](https://www.kernel.org/). Encore une fois, il échange une vitesse de compression plus lente contre un taux de compression encore plus élevé.

Quelques exemples d'utilisation :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="55%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz *</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresse tous les fichiers dans le répertoire actuel et remplace chaque fichier par un avec une extension<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">.xz</strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz foo</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresse&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">foo</span></strong><span>&nbsp;</span>en<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">foo.xz</strong></span><span>&nbsp;</span>en utilisant le niveau de compression par défaut (-6), et supprime<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">foo</span></strong></span><span>&nbsp;</span>si la compression réussit.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz -dk bar.xz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Décompresse<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bar.xz</span></strong></span><span>&nbsp;</span>en&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bar</span></strong>&nbsp;et ne supprime pas<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bar.xz</span></strong></span><span>&nbsp;</span>même si la décompression réussit.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz -dcf a.txt b.txt.xz &gt; abcd.txt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Décompresse un mélange de fichiers compressés et non compressés vers la sortie standard, en utilisant une seule commande.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">xz -d *.xz</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Décompresse les fichiers compressés en utilisant<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz</span></strong>.</td></tr></tbody></table>

Les fichiers compressés sont stockés avec une extension **.xz**.

### Gestion des fichiers à l'aide de zip

Le programme **zip** n'est pas souvent utilisé pour compresser des fichiers sous Linux, mais est souvent requis pour examiner et décompresser des archives provenant d'autres systèmes d'exploitation. Il n'est utilisé sous Linux que lorsque vous obtenez un fichier zippé d'un utilisateur Windows. C'est un programme hérité.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="25%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">zip backup *</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compresse tous les fichiers du répertoire courant et les place dans<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">backup.zip</span></strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">zip -r backup.zip ~</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Archive votre répertoire de connexion (<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">~</span></strong></span>) et tous les fichiers et répertoires qu'il contient dans<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">backup.zip</span></strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">unzip backup.zip</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Extrait tous les fichiers de&nbsp;<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">backup.zip</span></strong><span>&nbsp;</span></span>et les place dans le répertoire courant.</td></tr></tbody></table>

### Archivage et compression de données à l'aide de tar

Historiquement, **tar** signifiait "**t**ape **ar**chive" (archive sur bande) et était utilisé pour archiver des fichiers sur une bande magnétique. Il vous permet de créer ou d'extraire des fichiers d'un fichier d'archive, souvent appelé **tarball**. En même temps, vous pouvez optionnellement compresser lors de la création de l'archive, et décompresser lors de l'extraction de son contenu.

Voici quelques exemples d'utilisation de **tar** :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 884px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tar xvf mydir.tar</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Extrait tous les fichiers de<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir.tar</span></strong><span>&nbsp;</span>dans le répertoire<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir</span></strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">tar zcvf mydir.tar.gz mydir</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Crée l'archive et la compresse avec<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">tar jcvf mydir.tar.bz2 mydir</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Crée l'archive et la compresse avec<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bz2</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tar Jcvf mydir.tar.xz mydir</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Crée l'archive et la compresse avec<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">xz</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tar xvf mydir.tar.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Extrait tous les fichiers de<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir.tar.gz</span></strong></span><span>&nbsp;</span>dans le répertoire<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mydir</span></strong></span>.<br style="line-height: 1.4em;"><em style="line-height: 1.4em; font-style: italic;"><strong style="font-weight: bold; line-height: 1.4em;">NOTE</strong> : Vous n'avez<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">pas</strong><span>&nbsp;</span>besoin de dire à<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">tar</strong><span>&nbsp;</span>qu'il est au format<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: italic; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">gzip</span></strong>.</em></td></tr></tbody></table>

Vous pouvez séparer les étapes d'archivage et de compression, comme dans :

**$ tar cvf mydir.tar mydir ; gzip mydir.tar**
**$ gunzip mydir.tar.gz ; tar xvf mydir.tar**

mais c'est plus lent et gaspille de l'espace en créant un fichier **.tar** intermédiaire inutile.

### Temps et tailles de compression relatifs

Pour démontrer l'efficacité relative de **gzip**, **bzip2** et **xz**, la capture d'écran suivante montre les résultats de la compression d'une arborescence de répertoires de fichiers purement textuels (le répertoire **include** de la source du noyau) en utilisant les trois méthodes.

![Temps et tailles de compression relatifs](https://courses.edx.org/assets/courseware/v1/72c55fb093021786337d84cd0a081993/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tartimes.png)
_Temps et tailles de compression relatifs_

Cela montre que lorsque les facteurs de compression augmentent, le temps CPU augmente également (c'est-à-dire que produire des archives plus petites prend plus de temps).

### Copie de disque à disque (dd)

Le programme **dd** est très utile pour faire des copies d'espace disque brut. Par exemple, pour sauvegarder votre Master Boot Record (MBR) (le premier secteur de 512 octets sur le disque qui contient une table décrivant les partitions sur ce disque), vous pourriez taper :

**dd if=/dev/sda of=sda.mbr bs=512 count=1**

**ATTENTION !**

Taper :

**dd if=/dev/sda of=/dev/sdb**

pour faire une copie d'un disque sur un autre, supprimera tout ce qui existait auparavant sur le deuxième disque.

Une copie exacte du premier périphérique disque est créée sur le deuxième périphérique disque.

**N'expérimentez pas avec cette commande telle qu'écrite ci-dessus, car elle peut effacer un disque dur !**

La signification exacte du nom **dd** est un sujet souvent débattu. Les mots data definition sont la théorie la plus populaire et ont des racines dans l'histoire ancienne d'IBM. Souvent, les gens plaisantent en disant que cela signifie disk destroyer et d'autres variantes telles que delete data !

![Copie de disque à disque (dd)](https://courses.edx.org/assets/courseware/v1/6ed7efb57f544c1bbac9baf55f75e535/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch08_screen_41.jpg)
_Copie de disque à disque (dd)_

### Résumé du chapitre

Vous avez terminé le chapitre 10. Résumons les concepts clés couverts :

* L'arborescence du système de fichiers commence à ce qu'on appelle souvent le répertoire racine (ou tronc, ou **/**).
* La norme de hiérarchie des systèmes de fichiers (FHS) fournit aux développeurs Linux et aux administrateurs système une structure de répertoires standard pour le système de fichiers.
* Les partitions aident à séparer les fichiers selon l'utilisation, la propriété et le type.
* Les systèmes de fichiers peuvent être montés n'importe où sur l'arborescence principale du système de fichiers à un point de montage. Le montage automatique du système de fichiers peut être configuré en éditant **/etc/fstab**.
* NFS (Network File System) est une méthode utile pour partager des fichiers et des données via les systèmes réseau.
* Les systèmes de fichiers comme **/proc** sont appelés pseudo-systèmes de fichiers car ils n'existent qu'en mémoire.
* **/root** (slash-root) est le répertoire personnel de l'utilisateur root.
* **/var** peut être placé dans son propre système de fichiers afin que la croissance puisse être contenue et n'affecte pas fatalement le système.
* **/boot** contient les fichiers de base nécessaires pour démarrer le système.
* **patch** est un outil très utile sous Linux. De nombreuses modifications du code source et des fichiers de configuration sont distribuées avec des fichiers de correctif, car ils contiennent les deltas ou les changements pour passer d'une ancienne version d'un fichier à la nouvelle version d'un fichier.
* Les extensions de fichiers sous Linux ne signifient pas nécessairement qu'un fichier est d'un certain type.
* **cp** est utilisé pour copier des fichiers sur la machine locale, tandis que **rsync** peut également être utilisé pour copier des fichiers d'une machine à une autre, ainsi que pour synchroniser le contenu.
* **gzip**, **bzip2**, **xz** et **zip** sont utilisés pour compresser des fichiers.
* **tar** vous permet de créer ou d'extraire des fichiers d'un fichier d'archive, souvent appelé tarball. Vous pouvez optionnellement compresser lors de la création de l'archive, et décompresser lors de l'extraction de son contenu.
* **dd** peut être utilisé pour faire de grandes copies exactes, même de partitions de disque entières, efficacement.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 11 : Éditeurs de texte

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être familier avec :

* Comment créer et éditer des fichiers en utilisant les éditeurs de texte Linux disponibles.
* nano, un éditeur de texte simple.
* gedit, un éditeur graphique simple.
* vi et emacs, deux éditeurs avancés avec des interfaces à la fois textuelles et graphiques.

### Aperçu des éditeurs de texte sous Linux

À un moment donné, vous devrez éditer manuellement des fichiers texte. Vous pourriez composer un e-mail hors ligne, écrire un script à utiliser pour **bash** ou d'autres interpréteurs de commandes, modifier un fichier de configuration système ou d'application, ou développer du code source pour un langage de programmation tel que C, Python ou Java.

Les administrateurs Linux peuvent éviter d'utiliser un éditeur de texte, en employant à la place des utilitaires graphiques pour créer et modifier des fichiers de configuration système. Cependant, cela peut être plus laborieux que d'utiliser directement un éditeur de texte, et être plus limité en capacité. Notez que les applications de traitement de texte (y compris celles qui font partie des suites bureautiques courantes) ne sont pas vraiment des éditeurs de texte de base ; elles ajoutent beaucoup d'informations de formatage supplémentaires (généralement invisibles) qui rendront probablement les fichiers de configuration d'administration système inutilisables pour leur usage prévu. Donc, savoir utiliser avec confiance un ou plusieurs éditeurs de texte est vraiment une compétence essentielle à avoir pour Linux.

À présent, vous avez certainement réalisé que Linux regorge de choix ; en ce qui concerne les éditeurs de texte, il existe de nombreux choix, allant du très simple au très complexe, notamment :

* nano
* gedit
* vi
* emacs

Dans cette section, nous apprenons d'abord les éditeurs nano et gedit, qui sont relativement simples et faciles à apprendre, puis plus tard les choix plus compliqués, vi et emacs. Avant de commencer, jetons un coup d'œil à certains cas où un éditeur n'est pas nécessaire.

![Éditeurs de texte sous Linux](https://courses.edx.org/assets/courseware/v1/57bd3f905d0a25d34771843b351ff71a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch10_screen03.jpg)
_Éditeurs de texte sous Linux_

### Création de fichiers sans utiliser d'éditeur

Parfois, vous voudrez peut-être créer un fichier court et ne voulez pas vous embêter à invoquer un éditeur de texte complet. De plus, le faire peut être très utile lorsqu'il est utilisé à l'intérieur de scripts, même lors de la création de fichiers plus longs. Vous vous retrouverez sans aucun doute à utiliser cette méthode lorsque vous commencerez les chapitres ultérieurs qui couvrent les scripts shell !

Si vous voulez créer un fichier sans utiliser d'éditeur, il existe deux façons standard d'en créer un à partir de la ligne de commande et de le remplir avec du contenu.

La première consiste à utiliser **echo** de manière répétée :

**$ echo ligne une > monfichier**
**$ echo ligne deux >> monfichier**
**$ echo ligne trois >> monfichier**

Notez que tandis qu'un seul signe supérieur à (**>**) enverra la sortie d'une commande vers un fichier, deux d'entre eux (**>>**) ajouteront la nouvelle sortie à un fichier existant.

La deuxième façon est d'utiliser **cat** combiné avec la redirection :

**$ cat << EOF > monfichier**
**> ligne une**
**> ligne deux**
**> ligne trois**
**> EOF**
**$**

Les deux techniques produisent un fichier avec les lignes suivantes dedans :

**ligne une**
**ligne deux**
**ligne trois**

et sont extrêmement utiles lorsqu'elles sont employées par des scripts.

![Création de fichiers sans utiliser d'éditeur](https://courses.edx.org/assets/courseware/v1/b04d6912d3a68cd8702829b69b260051/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/echocatubuntu.png)
_Création de fichiers sans utiliser d'éditeur_

### nano et gedit

Il existe des éditeurs de texte qui sont assez évidents ; ils ne nécessitent aucune expérience particulière pour apprendre et sont en fait assez capables, voire robustes. Un éditeur particulièrement facile à utiliser est l'éditeur basé sur un terminal texte nano. Invoquez simplement nano en donnant un nom de fichier comme argument. Toute l'aide dont vous avez besoin est affichée en bas de l'écran, et vous devriez pouvoir continuer sans aucun problème.

![Ordinateur](https://courses.edx.org/assets/courseware/v1/b3c8f733d43ceaff56f586b7c8f8708b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch10_screen04.jpg)

En tant qu'éditeur graphique, gedit fait partie du système de bureau GNOME (kwrite est associé à KDE). Les éditeurs gedit et kwrite sont très faciles à utiliser et sont extrêmement capables. Ils sont également très configurables. Ils ressemblent beaucoup au Bloc-notes (Notepad) sous Windows. D'autres variantes telles que kate sont également prises en charge par KDE.

### nano

nano est facile à utiliser et nécessite très peu d'efforts pour apprendre. Pour ouvrir un fichier, tapez **nano <nomfichier>** et appuyez sur **Entrée**. Si le fichier n'existe pas, il sera créé.

nano fournit une barre de raccourcis de deux lignes en bas de l'écran qui liste les commandes disponibles. Certaines de ces commandes sont :

* **CTRL-G**
Afficher l'écran d'aide.
* **CTRL-O**
Écrire dans un fichier.
* **CTRL-X**
Quitter un fichier.
* **CTRL-R**
Insérer le contenu d'un autre fichier dans le tampon actuel.
* **CTRL-C**
Afficher la position du curseur.

![nano](https://courses.edx.org/assets/courseware/v1/c0d7acca187acbb8d82288dee538658d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/nano.png)
_nano_

### gedit

gedit (prononcé 'g-edit') est un éditeur graphique simple à utiliser qui ne peut être exécuté qu'au sein d'un environnement de bureau graphique. Il est visuellement assez similaire à l'éditeur de texte Bloc-notes sous Windows, mais est en fait beaucoup plus capable et très configurable et dispose d'une multitude de plugins disponibles pour étendre davantage ses capacités.

Pour ouvrir un nouveau fichier, trouvez le programme dans le système de menus de votre bureau, ou à partir de la ligne de commande tapez **gedit <nomfichier>**. Si le fichier n'existe pas, il sera créé.

L'utilisation de gedit est assez simple et ne nécessite pas beaucoup de formation. Son interface est composée d'éléments assez familiers.

![gedit](https://courses.edx.org/assets/courseware/v1/739df8236f04571d52f8e387f0dfd50b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/gedit.png)

### vi et emacs

Les développeurs et administrateurs expérimentés travaillant sur des systèmes de type UNIX utilisent presque toujours l'une des deux options d'édition vénérables : vi et emacs. Les deux sont présents ou facilement disponibles sur toutes les distributions et sont complètement compatibles avec les versions disponibles sur d'autres systèmes d'exploitation.

vi et emacs ont tous deux une forme de base purement textuelle qui peut fonctionner dans un environnement non graphique. Ils ont également une ou plusieurs formes d'interface graphique avec des capacités étendues ; celles-ci peuvent être plus conviviales pour un utilisateur moins expérimenté. Bien que vi et emacs puissent avoir des courbes d'apprentissage significativement raides pour les nouveaux utilisateurs, ils sont extrêmement efficaces une fois que l'on a appris à les utiliser.

Vous devez être conscient que les combats entre utilisateurs chevronnés pour savoir quel éditeur est le meilleur peuvent être assez intenses et sont souvent décrits comme une guerre sainte.

![Éditeurs de texte Linux : les éditeurs de base sont nano et gedit et les éditeurs avancés sont vi et emacs](https://courses.edx.org/assets/courseware/v1/c1242e5076d40142646d5f7d0cbb6e31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch10_screen08.jpg)
_Éditeurs de texte Linux_

### Introduction à vi

Généralement, le programme réel installé sur votre système est vim, qui signifie Vi IMproved, et est aliasé au nom vi. Le nom se prononce comme "vi-aïe".

Même si vous ne voulez pas utiliser vi, il est bon d'acquérir une certaine familiarité avec lui : c'est un outil standard installé sur pratiquement toutes les distributions Linux. En effet, il peut y avoir des moments où il n'y a pas d'autre éditeur disponible sur le système.

GNOME étend vi avec une interface très graphique connue sous le nom de gvim et KDE propose kvim. L'un ou l'autre peut être plus facile à utiliser au début.

Lors de l'utilisation de vi, toutes les commandes sont entrées via le clavier. Vous n'avez pas besoin de continuer à bouger vos mains pour utiliser un dispositif de pointage tel qu'une souris ou un pavé tactile, sauf si vous voulez le faire en utilisant l'une des versions graphiques de l'éditeur.

![Introduction à vi](https://courses.edx.org/assets/courseware/v1/4421947fff5812630286c32046082020/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/vimubuntu.png)

### vimtutor

Taper **vimtutor** lance un tutoriel court mais très complet pour ceux qui veulent apprendre leurs premières commandes vi. Même s'il ne fournit qu'une introduction et seulement sept leçons, il a assez de matériel pour faire de vous un utilisateur vi très compétent, car il couvre un grand nombre de commandes. Après avoir appris ces bases, vous pouvez rechercher de nouvelles astuces à intégrer dans votre liste de commandes vi car il y a toujours des moyens plus optimaux de faire les choses dans vi avec moins de frappe.

![vim tutor](https://courses.edx.org/assets/courseware/v1/b1e67aea3546804f69588aab52e97fcb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/vimtutorubuntu.png)

### Modes dans vi

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="10%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Mode</strong></span></td><td align="center" bgcolor="#003f60" width="80%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Fonctionnalité</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><ul style="padding: 0px 0px 0px 1em; margin: 1em 0px; line-height: 1.4em; color: rgb(69, 69, 69); list-style: outside none disc;"><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Par défaut,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">vi</strong>&nbsp;démarre en mode<strong style="font-weight: bold; line-height: 1.4em;">&nbsp;</strong>Commande.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Chaque touche est une commande d'éditeur.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Les frappes au clavier sont interprétées comme des commandes qui peuvent modifier le contenu du fichier.</li></ul></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Insertion</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><ul style="padding: 0px 0px 0px 1em; margin: 1em 0px; line-height: 1.4em; color: rgb(69, 69, 69); list-style: outside none disc;"><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Tapez<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">i</span></strong></span><span>&nbsp;</span>pour passer en mode&nbsp;Insertion depuis le mode&nbsp;Commande.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Le mode Insertion est utilisé pour entrer (insérer) du texte dans un fichier.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Le mode Insertion est indiqué par un indicateur “<code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><strong style="font-weight: bold; line-height: 1.4em;">? INSERT ?</strong></code>” en bas de l'écran.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Appuyez sur<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><code style="font-family: monospace, serif; font-size: 1em; line-height: 1.4em; color: rgb(69, 69, 69); background: none; padding: 0px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Esc</span></code></span></strong></span><span>&nbsp;</span>pour quitter le mode Insertion et revenir au mode Commande.</li></ul></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Ligne</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><ul style="padding: 0px 0px 0px 1em; margin: 1em 0px; line-height: 1.4em; color: rgb(69, 69, 69); list-style: outside none disc;"><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Tapez&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:</span></strong></span><span>&nbsp;</span>pour passer en mode Ligne depuis le mode Commande.&nbsp;Chaque touche est une commande externe, incluant des opérations telles que l'écriture du contenu du fichier sur le disque ou la sortie.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Utilise des commandes d'édition de ligne héritées des anciens éditeurs de ligne. La plupart de ces commandes ne sont en fait plus utilisées. Certaines commandes d'édition de ligne sont très puissantes.</li><li style="line-height: 1.4em; margin-bottom: 0.70788em;">Appuyez sur<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Esc</span></strong></span><span>&nbsp;</span>pour quitter le mode Ligne et revenir au mode Commande.</li></ul></td></tr></tbody></table>

vi fournit trois modes, comme décrit dans le tableau ci-dessous. Il est vital de ne pas perdre de vue dans quel mode vous vous trouvez. De nombreuses frappes et commandes se comportent très différemment selon les modes.

### Travailler avec des fichiers dans vi

Le tableau décrit les commandes les plus importantes utilisées pour démarrer, quitter, lire et écrire des fichiers dans vi. La touche **ENTRÉE** doit être enfoncée après toutes ces commandes.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">vi myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Démarrer l'éditeur et éditer<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">vi -r myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Démarrer et éditer<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong><span>&nbsp;</span>en mode récupération après un plantage système</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:r file2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Lire<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file2</span></strong><span>&nbsp;</span>et l'insérer à la position actuelle</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Écrire dans le fichier</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:w myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Écrire dans<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:w! file2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Écraser<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file2</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:x ou :wq</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Quitter et écrire le fichier modifié</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:q</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Quitter<strong style="font-weight: bold; line-height: 1.4em;"></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:q!</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Quitter même si les modifications n'ont pas été enregistrées</span></td></tr></tbody></table>

### Changer la position du curseur dans vi

Le tableau décrit les frappes les plus importantes utilisées pour changer la position du curseur dans vi. Les commandes en mode ligne (celles suivant deux-points **:** ) nécessitent d'appuyer sur la touche **ENTRÉE** après avoir tapé la commande.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="25%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td width="35%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">touches fléchées</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour se déplacer vers le haut, le bas, la gauche et la droite</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">j</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&lt;ret&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour descendre d'une ligne</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">k</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour monter d'une ligne</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">h</span></strong><span>&nbsp;</span>ou Retour arrière</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour se déplacer d'un caractère vers la gauche</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">l</span></strong><span>&nbsp;</span>ou Espace</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour se déplacer d'un caractère vers la droite</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">0</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour aller au début de la ligne</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour aller à la fin de la ligne</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour aller au début du mot suivant</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:0</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1G</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour aller au début du fichier</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:n</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">nG</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour aller à la ligne n</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">:$</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">G</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour aller à la dernière ligne du fichier</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-F</span></strong></span><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Down</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour avancer d'une page</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-B</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Up</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour reculer d'une page</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">^l</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Pour rafraîchir et centrer l'écran</span></td></tr></tbody></table>

### Vidéo : Utilisation des modes et des mouvements du curseur dans vi

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V001700_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Recherche de texte dans vi

Le tableau décrit les _commandes_ les plus importantes utilisées lors de la recherche de texte dans vi. La touche **ENTRÉE** doit être enfoncée après avoir tapé le motif de recherche.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/pattern</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Rechercher vers l'avant le motif</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">?pattern</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Rechercher vers l'arrière le motif</span></td></tr></tbody></table>

Le tableau décrit les _frappes_ les plus importantes utilisées lors de la recherche de texte dans vi.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">n</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Aller à la prochaine occurrence du motif de recherche</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">N</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Aller à l'occurrence précédente du motif de recherche</span></td></tr></tbody></table>

### Travailler avec du texte dans vi

Le tableau décrit les frappes les plus importantes utilisées lors de la modification, de l'ajout et de la suppression de texte dans vi.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td width="65%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">a</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ajouter du texte après le curseur ; arrêter avec la touche<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Échap</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">A</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ajouter du texte à la fin de la ligne courante ; arrêter avec la touche<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Échap</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Insérer du texte avant le curseur ; arrêter avec la touche<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Échap</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">I</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Insérer du texte au début de la ligne courante ; arrêter avec la touche<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Échap</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">o</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Commencer une nouvelle ligne sous la ligne courante, y insérer du texte ; arrêter avec la touche<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Échap</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">O</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Commencer une nouvelle ligne au-dessus de la ligne courante, y insérer du texte ; arrêter avec la touche<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Échap</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">r</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Remplacer le caractère à la position actuelle</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">R</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Remplacer le texte à partir de la position actuelle ; arrêter avec la touche<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Échap</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">x</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer le caractère à la position actuelle</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Nx</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer N caractères, à partir de la position actuelle</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dw</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer le mot à la position actuelle</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">D</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer le reste de la ligne courante</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer la ligne courante</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Ndd</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dNd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Supprimer N lignes</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">u</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Annuler l'opération précédente</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">yy</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Yank (copier) la ligne courante et la mettre dans le tampon</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Nyy</span></strong></span><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">yNy</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Yank (copier) N lignes et les mettre dans le tampon</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">p</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Coller à la position actuelle la ligne ou les lignes copiées depuis le tampon</span></td></tr></tbody></table>

**[Voici un PDF consolidé avec les commandes pour vi.](https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block@Commands_for_vi.pdf)**

### Utilisation de commandes externes dans vi

Taper la commande **sh** ouvre un shell de commande externe. Lorsque vous quittez le shell, vous reprendrez votre session d'édition.

Taper **!** exécute une commande depuis l'intérieur de vi. La commande suit le point d'exclamation. Cette technique est la mieux adaptée pour les commandes non interactives, telles que **: ! wc %**. Taper ceci exécutera la commande **wc** (compteur de mots) sur le fichier ; le caractère **%** représente le fichier en cours d'édition.

![commande vi](https://courses.edx.org/assets/courseware/v1/1b96ee76e521a7f91666d8df989960d6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/vicommand.png)

### Vidéo : Utilisation de commandes externes, enregistrement et fermeture dans l'éditeur vi

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V002700_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Introduction à emacs

L'éditeur emacs est un concurrent populaire de vi. Contrairement à vi, il ne fonctionne pas avec des modes. emacs est hautement personnalisable et comprend un grand nombre de fonctionnalités. Il a été initialement conçu pour être utilisé sur une console, mais a rapidement été adapté pour fonctionner également avec une interface graphique. emacs a de nombreuses autres capacités autres que la simple édition de texte. Par exemple, il peut être utilisé pour le courrier électronique, le débogage, etc.

Plutôt que d'avoir différents modes pour la commande et l'insertion, comme vi, emacs utilise les touches **CTRL** et Meta (**Alt** ou **Esc**) pour les commandes spéciales.

![emacs](https://courses.edx.org/assets/courseware/v1/ce4dcc838b6cc24da8199d352dd4181c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/emacsc8.png)

### Travailler avec emacs

Le tableau liste certaines des combinaisons de touches les plus importantes qui sont utilisées lors du démarrage, de la sortie, de la lecture et de l'écriture de fichiers dans emacs.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 802.398px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">emacs myfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Démarrer emacs et éditer<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myfile</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x i</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Insérer le fichier demandé à la position actuelle</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x s</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Enregistrer tous les fichiers</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x CTRL-w</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Écrire dans le fichier en donnant un nouveau nom lorsque demandé</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x&nbsp;CTRL-s</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Enregistre le fichier actuel</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-x&nbsp;CTRL-c</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Quitter après avoir été invité à enregistrer&nbsp;tous les fichiers modifiés</td></tr></tbody></table>

Le tutoriel emacs est un bon endroit pour commencer à apprendre les commandes de base. Il est disponible à tout moment dans emacs en tapant simplement **CTRL-h** (pour help) puis la lettre **t** pour tutoriel.

### Changer la position du curseur dans emacs

Le tableau liste certaines des touches et combinaisons de touches qui sont utilisées pour changer la position du curseur dans emacs.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="27%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td width="53%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">touches fléchées</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisez les touches fléchées pour haut, bas, gauche et droite</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-n</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Une ligne vers le bas</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-p</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Une ligne vers le haut</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-f</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Un caractère vers l'avant/droite</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-b</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Un caractère vers l'arrière/gauche</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-a</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Aller au début de la ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-e</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Aller à la fin de la ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-f</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Aller au début du mot suivant</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-b</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Reculer au début du mot précédent</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-&lt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Aller au début du fichier</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-g-g-n</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Aller à la ligne n (peut aussi utiliser '<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Esc-x Goto-line n</span></strong>')</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-&gt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Aller à la fin du fichier</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-v</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Down</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Avancer d'une page</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Meta-v</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Page Up</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Reculer d'une page</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-l</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Rafraîchir et centrer l'écran</td></tr></tbody></table>

### Recherche de texte dans emacs

Le tableau liste les combinaisons de touches qui sont utilisées pour rechercher du texte dans emacs.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-s</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Rechercher vers l'avant le motif demandé, ou le motif suivant</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-r</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Rechercher vers l'arrière le motif demandé, ou le motif suivant</td></tr></tbody></table>

### Travailler avec du texte dans emacs

Le tableau liste certaines des combinaisons de touches utilisées pour changer, ajouter et supprimer du texte dans emacs :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-o</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Insérer une ligne vide</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-d</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprimer le caractère à la position actuelle</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-k</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprimer le reste de la ligne courante</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-_</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Annuler l'opération précédente</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-</span></strong><span>&nbsp;</span>(espace ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-@</span></strong>)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Marquer le début de la région sélectionnée. La fin sera à la position du curseur</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-w</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprimer le texte marqué actuel et l'écrire dans le tampon</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-y</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Insérer à l'emplacement actuel du curseur ce qui a été supprimé le plus récemment</td></tr></tbody></table>

[**Voici un fichier PDF consolidé avec les commandes pour emacs.**](https://courses.edx.org/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block@Commands_for_emacs.pdf)

### Vidéo : Opérations emacs

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V001900_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Résumé du chapitre

Vous avez terminé le chapitre 11. Résumons les concepts clés couverts :

* Les éditeurs de texte (plutôt que les programmes de traitement de texte) sont utilisés assez souvent sous Linux, pour des tâches telles que la création ou la modification de fichiers de configuration système, l'écriture de scripts, le développement de code source, etc.
* nano est un éditeur de texte facile à utiliser qui utilise des invites à l'écran.
* gedit est un éditeur graphique, très similaire au Bloc-notes sous Windows.
* L'éditeur vi est disponible sur tous les systèmes Linux et est très largement utilisé. Des versions d'extension graphique de vi sont également largement disponibles.
* emacs est disponible sur tous les systèmes Linux comme une alternative populaire à vi. emacs peut prendre en charge à la fois une interface utilisateur graphique et une interface en mode texte.
* Pour accéder au tutoriel vi, tapez **vimtutor** dans une fenêtre de ligne de commande.
* Pour accéder au tutoriel emacs, tapez **Ctl-h** puis **t** depuis l'intérieur d'emacs.
* vi a trois modes : _Commande_, _Insertion_ et _Ligne_. emacs n'en a qu'un, mais nécessite l'utilisation de touches spéciales, telles que **Control** et **Escape**.
* Les deux éditeurs utilisent diverses combinaisons de frappes pour accomplir des tâches. La courbe d'apprentissage pour les maîtriser peut être longue, mais une fois maîtrisée, l'utilisation de l'un ou l'autre éditeur est extrêmement efficace.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 12 : Environnement utilisateur

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Utiliser et configurer des comptes utilisateurs et des groupes d'utilisateurs.
* Utiliser et définir des variables d'environnement.
* Utiliser l'historique des commandes shell précédentes.
* Utiliser des raccourcis clavier.
* Utiliser et définir des alias.
* Utiliser et définir les permissions et la propriété des fichiers.

### Identifier l'utilisateur actuel

Comme vous le savez, Linux est un système d'exploitation multi-utilisateur, ce qui signifie que plusieurs utilisateurs peuvent se connecter en même temps.

* Pour identifier l'utilisateur actuel, tapez **whoami**.
* Pour lister les utilisateurs actuellement connectés, tapez **who**.

Donner à **who** l'option **-a** donnera des informations plus détaillées.

![Utilisation de who et whoami](https://courses.edx.org/assets/courseware/v1/b90c91f7776e3f55a5e63eb343e10b99/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/whoubuntu.png)
_Identifier l'utilisateur actuel_

### Fichiers de démarrage utilisateur

Sous Linux, le programme shell de commande (généralement **bash**) utilise un ou plusieurs fichiers de démarrage pour configurer l'environnement utilisateur. Les fichiers dans le répertoire **/etc** définissent les paramètres globaux pour tous les utilisateurs, tandis que les fichiers d'initialisation dans le répertoire personnel de l'utilisateur peuvent inclure et/ou remplacer les paramètres globaux.

![Fichiers de démarrage utilisateur](https://courses.edx.org/assets/courseware/v1/a61fd2656f3894d6f93397e755157b4b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch09_screen07.jpg)
_Fichiers de démarrage utilisateur_

Les fichiers de démarrage peuvent faire tout ce que l'utilisateur souhaite faire dans chaque shell de commande, tel que :

* Personnaliser l'invite
* Définir des raccourcis et des alias de ligne de commande
* Définir l'éditeur de texte par défaut
* Définir le chemin pour trouver les programmes exécutables

### Ordre des fichiers de démarrage

La prescription standard est que lorsque vous vous connectez pour la première fois à Linux, **/etc/profile** est lu et évalué, après quoi les fichiers suivants sont recherchés (s'ils existent) dans l'ordre indiqué :

1. **~/.bash_profile**
2. **~/.bash_login**
3. **~/.profile**

où **~/.** désigne le répertoire personnel de l'utilisateur. Le shell de connexion Linux évalue le premier fichier de démarrage qu'il rencontre et ignore le reste. Cela signifie que s'il trouve **~/.bash_profile**, il ignore **~/.bash_login** et **~/.profile**. Différentes distributions peuvent utiliser différents fichiers de démarrage.

Cependant, chaque fois que vous créez un nouveau shell, ou une fenêtre de terminal, etc., vous n'effectuez pas une connexion système complète ; seul un fichier nommé **~/.bashrc** est lu et évalué. Bien que ce fichier ne soit pas lu et évalué avec le shell de connexion, la plupart des distributions et/ou utilisateurs incluent le fichier **~/.bashrc** à l'intérieur de l'un des trois fichiers de démarrage appartenant à l'utilisateur.

Le plus souvent, les utilisateurs ne touchent qu'à **~/.bashrc**, car il est invoqué chaque fois qu'un nouveau shell de ligne de commande s'initie, ou qu'un autre programme est lancé depuis une fenêtre de terminal, tandis que les autres fichiers sont lus et exécutés uniquement lorsque l'utilisateur se connecte pour la première fois au système.

Les distributions récentes n'ont parfois même pas **.bash_profile** et/ou **.bash_login**, et certaines ne font guère plus qu'inclure **.bashrc**.

![Ordre des fichiers de démarrage](https://courses.edx.org/assets/courseware/v1/618e42fc4814cce9ff91eceac55438b9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bashinit.png)
_Ordre des fichiers de démarrage_

### Création d'alias

Vous pouvez créer des commandes personnalisées ou modifier le comportement de celles déjà existantes en créant des **alias**. Le plus souvent, ces alias sont placés dans votre fichier **~/.bashrc** afin qu'ils soient disponibles pour tous les shells de commande que vous créez. **unalias** supprime un alias.

Taper **alias** sans arguments listera les alias actuellement définis.

Veuillez noter qu'il ne doit pas y avoir d'espaces de chaque côté du signe égal et que la définition de l'alias doit être placée entre guillemets simples ou doubles si elle contient des espaces.

![Création d'alias](https://courses.edx.org/assets/courseware/v1/97491d062822787b87a74f33ea868847/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/aliassuse.png)
_Création d'alias_

### Bases des utilisateurs et des groupes

Tous les utilisateurs Linux se voient attribuer un identifiant utilisateur unique (**uid**), qui est juste un entier ; les utilisateurs normaux commencent avec un uid de 1000 ou plus.

Linux utilise des **groupes** pour organiser les utilisateurs. Les groupes sont des collections de comptes avec certaines permissions partagées. Le contrôle de l'appartenance au groupe est administré via le fichier **/etc/group**, qui montre une liste des groupes et de leurs membres. Par défaut, chaque utilisateur appartient à un groupe par défaut ou primaire. Lorsqu'un utilisateur se connecte, l'appartenance au groupe est définie pour son groupe primaire et tous les membres bénéficient du même niveau d'accès et de privilège. Les permissions sur divers fichiers et répertoires peuvent être modifiées au niveau du groupe.

Les utilisateurs ont également un ou plusieurs identifiants de groupe (**gid**), y compris un par défaut qui est le même que l'identifiant utilisateur. Ces numéros sont associés à des noms via les fichiers **/etc/passwd** et **/etc/group**. Les groupes sont utilisés pour établir un ensemble d'utilisateurs qui ont des intérêts communs à des fins de droits d'accès, de privilèges et de considérations de sécurité. Les droits d'accès aux fichiers (et aux périphériques) sont accordés sur la base de l'utilisateur et du groupe auquel ils appartiennent.

Par exemple, **/etc/passwd** pourrait contenir **george:x:1002:1002:George Metesky:/home/george:/bin/bash** et **/etc/group** pourrait contenir **george:x:1002**.

![Bases des utilisateurs et des groupes](https://courses.edx.org/assets/courseware/v1/03549a0189644137de64f426a69442c3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/etc_group_passwd.png)
_Bases des utilisateurs et des groupes_

### Ajout et suppression d'utilisateurs

Les distributions ont des interfaces graphiques simples pour créer et supprimer des utilisateurs et des groupes et manipuler l'appartenance aux groupes. Cependant, il est souvent utile de le faire à partir de la ligne de commande ou à l'intérieur de scripts shell. Seul l'utilisateur root peut ajouter et supprimer des utilisateurs et des groupes.

L'ajout d'un nouvel utilisateur se fait avec **useradd** et la suppression d'un utilisateur existant se fait avec **userdel**. Dans la forme la plus simple, un compte pour le nouvel utilisateur **bjmoose** serait fait avec :

**$ sudo useradd bjmoose**

ce qui, par défaut, définit le répertoire personnel à **/home/bjmoose**, le peuple avec quelques fichiers de base (copiés depuis **/etc/skel**) et ajoute une ligne à **/etc/passwd** telle que :

**bjmoose:x:1002:1002::/home/bjmoose:/bin/bash**

et définit le shell par défaut à **/bin/bash**. Supprimer un compte utilisateur est aussi simple que de taper **userdel bjmoose**. Cependant, cela laissera le répertoire **/home/bjmoose** intact. Cela pourrait être utile s'il s'agit d'une désactivation temporaire. Pour supprimer le répertoire personnel tout en supprimant le compte, il faut utiliser l'option **-r** avec **userdel**.

Taper **id** sans argument donne des informations sur l'utilisateur actuel, comme dans :

**$ id**
**uid=1002(bjmoose) gid=1002(bjmoose) groups=106(fuse),1002(bjmoose)**

Si on donne le nom d'un autre utilisateur comme argument, **id** rapportera des informations sur cet autre utilisateur.

![Ajout et suppression d'utilisateurs](https://courses.edx.org/assets/courseware/v1/1387735f26c0ae0b377390c4c9dd9e7a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/useradd.png)

### Vidéo : Utilisation des comptes utilisateurs

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000300_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Ajout et suppression de groupes

L'ajout d'un nouveau groupe se fait avec **groupadd** :

**$ sudo /usr/sbin/groupadd unnouvellegroupe**

Le groupe peut être supprimé avec :

**$ sudo /usr/sbin/groupdel unnouvellegroupe**

L'ajout d'un utilisateur à un groupe déjà existant se fait avec **usermod**. Par exemple, vous regarderiez d'abord à quels groupes l'utilisateur appartient déjà :

**$ groups rjsquirrel**
**rjsquirrel : rjsquirrel**

puis ajoutez le nouveau groupe :

**$ sudo /usr/sbin/usermod -a -G unnouvellegroupe rjsquirrel**

**$ groups rjsquirrel**
**rjsquirrel: rjsquirrel unnouvellegroupe**

Ces utilitaires mettent à jour **/etc/group** si nécessaire. Assurez-vous d'utiliser l'option **-a**, pour append (ajouter), afin d'éviter de supprimer les groupes déjà existants. **groupmod** peut être utilisé pour modifier les propriétés du groupe, telles que l'ID de groupe (gid) avec l'option **-g** ou son nom avec l'option **-n**.

Supprimer un utilisateur du groupe est un peu plus délicat. L'option **-G** de usermod doit donner une liste complète des groupes. Ainsi, si vous faites :

**$ sudo /usr/sbin/usermod -G rjsquirrel rjsquirrel**

**$ groups rjsquirrel**
**rjsquirrel : rjsquirrel**

seul le groupe **rjsquirrel** restera.

![Ajout et suppression de groupes](https://courses.edx.org/assets/courseware/v1/388d78b23f2b6d93f8f39cbecf6194b1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/newgroupsuse.png)
_Ajout et suppression de groupes_

### Le compte root

Le compte root est très puissant et a un accès complet au système. D'autres systèmes d'exploitation appellent souvent cela le compte administrateur ; sous Linux, il est souvent appelé le compte superutilisateur. Vous devez être extrêmement prudent avant d'accorder un accès root complet à un utilisateur ; c'est rarement, voire jamais, justifié. Les attaques externes consistent souvent en des astuces utilisées pour s'élever au compte root.

![Tux le pingouin et carré noir avec signe dièse et deux-points](https://courses.edx.org/assets/courseware/v1/5ec1a18add0a1780ef903912e0b5f6ba/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch09_screen04a.jpg)

Cependant, vous pouvez utiliser **sudo** pour attribuer des privilèges plus limités aux comptes utilisateurs :

* Uniquement sur une base temporaire
* Uniquement pour un sous-ensemble spécifique de commandes.

### su et sudo

Lors de l'attribution de privilèges élevés, vous pouvez utiliser la commande **su** (switch ou substitute user) pour lancer un nouveau shell s'exécutant en tant qu'un autre utilisateur (vous devez taper le mot de passe de l'utilisateur que vous devenez). Le plus souvent, cet autre utilisateur est root, et le nouveau shell permet l'utilisation de privilèges élevés jusqu'à ce qu'il soit quitté. Il est presque toujours une mauvaise pratique (dangereuse pour la sécurité et la stabilité) d'utiliser **su** pour devenir root. Les erreurs résultantes peuvent inclure la suppression de fichiers vitaux du système et des failles de sécurité.

Accorder des privilèges en utilisant **sudo** est moins dangereux et est préféré. Par défaut, **sudo** doit être activé sur une base par utilisateur. Cependant, certaines distributions (telles qu'Ubuntu) l'activent par défaut pour au moins un utilisateur principal, ou donnent cela comme option d'installation.

Dans le chapitre _Principes de sécurité locale_, nous décrirons et comparerons **su** et **sudo** en détail.

### Élévation vers le compte root

Pour devenir temporairement le superutilisateur pour une série de commandes, vous pouvez taper **su** et être ensuite invité à saisir le mot de passe root.

Pour exécuter une seule commande avec le privilège root, tapez **sudo <commande>**. Lorsque la commande est terminée, vous redeviendrez un utilisateur normal non privilégié.

Les fichiers de configuration **sudo** sont stockés dans le fichier **/etc/sudoers** et dans le répertoire **/etc/sudoers.d/**. Par défaut, le répertoire **sudoers.d** est vide.

![Élévation vers le compte root](https://courses.edx.org/assets/courseware/v1/7dd106f332e911d309ccdedc9823d9c7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sudo.png)
_Élévation vers le compte root_

### Variables d'environnement

Les **variables d'environnement** sont des quantités qui ont des valeurs spécifiques qui peuvent être utilisées par le shell de commande, tel que **bash**, ou d'autres utilitaires et applications. Certaines variables d'environnement reçoivent des valeurs prédéfinies par le système (qui peuvent généralement être remplacées), tandis que d'autres sont définies directement par l'utilisateur, soit à la ligne de commande, soit dans des scripts de démarrage et autres.

Une variable d'environnement est en fait juste une chaîne de caractères qui contient des informations utilisées par une ou plusieurs applications. Il existe plusieurs façons de visualiser les valeurs des variables d'environnement actuellement définies ; on peut taper **set**, **env** ou **export**. Selon l'état de votre système, **set** peut imprimer beaucoup plus de lignes que les deux autres méthodes.

![Variables d'environnement](https://courses.edx.org/assets/courseware/v1/1604db32728f9bb80765461155886f79/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/envsetexport.png)
_Variables d'environnement_

### Définition des variables d'environnement

Par défaut, les variables créées dans un script ne sont disponibles que pour le shell actuel ; les processus enfants (sous-shells) n'auront pas accès aux valeurs qui ont été définies ou modifiées. Permettre aux processus enfants de voir les valeurs nécessite l'utilisation de la commande **export**.

<table height="258" width="90%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Tâche</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Afficher la valeur d'une variable spécifique</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo $SHELL</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Exporter une nouvelle valeur de variable</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">export VARIABLE=valeur</strong></span>&nbsp;(ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">VARIABLE=valeur; export VARIABLE</span></strong>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ajouter une variable de façon permanente</span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Éditez<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">~/.bashrc</strong></span>&nbsp;et ajoutez la ligne<span>&nbsp;</span><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">export VARIABLE=valeur</span></strong></span></p><p style="color: rgb(69, 69, 69); margin: 20px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Tapez&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">source ~/.bashrc</span></strong>&nbsp;ou juste&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">. ~/.bashrc</span></strong><span>&nbsp;</span>(<em style="line-height: 1.4em; font-style: italic;">point</em><span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">~/.bashrc</span></strong>);&nbsp;ou démarrez simplement un nouveau shell en tapant<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">bash</span></strong></p></td></tr></tbody></table>

Vous pouvez également définir des variables d'environnement pour qu'elles soient transmises en une seule fois à une commande comme dans :

**$ SDIRS=s_0* KROOT=/lib/modules/$(uname -r)/build make modules_install**

qui transmet les valeurs des variables d'environnement **SDIRS** et **KROOT** à la commande **make modules_install**.

### La variable HOME

**HOME** est une variable d'environnement qui représente le répertoire personnel (ou de connexion) de l'utilisateur. **cd** sans arguments changera le répertoire de travail actuel à la valeur de **HOME**. Notez que le caractère tilde (**~**) est souvent utilisé comme abréviation pour **$HOME**. Ainsi, **cd $HOME** et **cd ~** sont des déclarations complètement équivalentes.

<table width="80%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="45%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Explication</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ echo $HOME</span><br style="line-height: 1.4em;"><span style="color: rgb(106, 191, 75); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">/home/me</span><br style="line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ cd /bin</span></span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Afficher la valeur de la variable d'environnement<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">HOME</span></strong>, puis changer de répertoire (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cd</span></strong>) vers<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/bin</span></strong></span></span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ pwd</span><br style="line-height: 1.4em;"><span style="color: rgb(106, 191, 75); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">/bin</span></span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Où sommes-nous ? Utilisez print (ou present) working directory (<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pwd</span></strong>) pour le savoir. Comme prévu,<span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/bin</span></strong></span></span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ cd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Changer de répertoire sans argument...</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">$ pwd</span><br style="line-height: 1.4em;"><span style="color: rgb(106, 191, 75); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">/home/me</span></span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">...nous ramène à<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">HOME</span></strong>, comme vous pouvez le voir maintenant.</td></tr></tbody></table>

La capture d'écran démontre cela.

![La variable HOME](https://courses.edx.org/assets/courseware/v1/946d3c6728f797c4ce929d2730915273/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/homeubuntu.png)
_La variable HOME_

### La variable PATH

**PATH** est une liste ordonnée de répertoires (le chemin) qui est scannée lorsqu'une commande est donnée pour trouver le programme ou le script approprié à exécuter. Chaque répertoire dans le chemin est séparé par des deux-points (**:**). Un nom de répertoire nul (vide) (ou **./**) indique le répertoire actuel à tout moment.

* **:path1:path2**
* **path1::path2**

Dans l'exemple **:path1:path2**, il y a un répertoire nul avant le premier deux-points (**:**). De même, pour **path1::path2**, il y a un répertoire nul entre **path1** et **path2**.

Pour préfixer un répertoire **bin** privé à votre chemin :

**$ export PATH=$HOME/bin:$PATH**
**$ echo $PATH**
**/home/student/bin:/usr/local/bin:/usr/bin:/bin/usr**

![La variable PATH](https://courses.edx.org/assets/courseware/v1/b955fc762a2b63221bc0a46e1fb9b419/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/setpath.png)
_La variable PATH_

### La variable SHELL

La variable d'environnement **SHELL** pointe vers le shell de commande par défaut de l'utilisateur (le programme qui gère tout ce que vous tapez dans une fenêtre de commande, généralement bash) et contient le chemin complet vers le shell :

**$ echo $SHELL**
**/bin/bash**
**$**

![Coquillage](https://courses.edx.org/assets/courseware/v1/411c5576bf37caded5284030bbd8cb0e/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/seashell.png)

### La variable PS1 et l'invite de ligne de commande

Prompt Statement (**PS**) est utilisé pour personnaliser votre chaîne d'invite dans vos fenêtres de terminal pour afficher les informations que vous souhaitez.

**PS1** est la variable d'invite principale qui contrôle l'apparence de votre invite de ligne de commande. Les caractères spéciaux suivants peuvent être inclus dans **PS1** :

**\u** - Nom d'utilisateur
**\h** - Nom d'hôte
**\w** - Répertoire de travail actuel
**\!** - Numéro d'historique de cette commande
**\d** - Date

Ils doivent être entourés de guillemets simples lorsqu'ils sont utilisés, comme dans l'exemple suivant :

**$ echo $PS1**
**$**
**$ export PS1='\u@\h:\w$ '**
**student@example.com:~$ # nouvelle invite**

Pour annuler les modifications :

**student@example.com:~$ export PS1='$ '**
**$**

Une pratique encore meilleure serait de sauvegarder l'ancienne invite d'abord, puis de la restaurer, comme dans :

**$ OLD_PS1=$PS1**

changer l'invite, et éventuellement la remettre avec :

**$ PS1=$OLD_PS1**
**$**

![La variable PS1 et l'invite de ligne de commande](https://courses.edx.org/assets/courseware/v1/0e41f5477fe686acda77ec04fe717d3d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ps1.png)

### Rappel des commandes précédentes

bash garde une trace des commandes et déclarations précédemment entrées dans un tampon d'historique. Vous pouvez rappeler les commandes précédemment utilisées simplement en utilisant les touches de curseur **Haut** et **Bas**. Pour afficher la liste des commandes précédemment exécutées, vous pouvez simplement taper **history** à la ligne de commande.

La liste des commandes est affichée avec la commande la plus récente apparaissant en dernier dans la liste. Ces informations sont stockées dans **~/.bash_history**. Si vous avez plusieurs terminaux ouverts, les commandes tapées dans chaque session ne sont pas enregistrées jusqu'à ce que la session se termine.

![Rappel des commandes précédentes](https://courses.edx.org/assets/courseware/v1/0dc7d17f95a156ae24e9ee8a22d98b69/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/debianhistory.png)
_Rappel des commandes précédentes_

### Utilisation des variables d'environnement d'historique

Plusieurs variables d'environnement associées peuvent être utilisées pour obtenir des informations sur le fichier `**history**`.

* **HISTFILE**
L'emplacement du fichier d'historique.
* **HISTFILESIZE**
Le nombre maximum de lignes dans le fichier d'historique (par défaut 500).
* **HISTSIZE**
Le nombre maximum de commandes dans le fichier d'historique.
* **HISTCONTROL**
Comment les commandes sont stockées.
* **HISTIGNORE**
Quelles lignes de commande peuvent être non enregistrées.

Pour une description complète de l'utilisation de ces variables d'environnement, consultez **man bash**.

![Utilisation des variables d'environnement d'historique](https://courses.edx.org/assets/courseware/v1/529cf8bca6c3fff74ad538be6dbab7f2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/history.png)
_Utilisation des variables d'environnement d'historique_

### Trouver et utiliser les commandes précédentes

Touches spécifiques pour effectuer diverses tâches :

<table border="0" width="100%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Touche</strong></span></td><td align="center" bgcolor="#003f60" width="65%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;">Touches fléchées Haut</strong></span>/<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><strong style="font-weight: bold; line-height: 1.4em;">Bas</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Parcourir la liste des commandes précédemment exécutées</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!!</span></strong></span><span>&nbsp;</span>(Prononcé bang-bang)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Exécuter la commande précédente</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-R</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Rechercher les commandes précédemment utilisées</td></tr></tbody></table>

Si vous souhaitez rappeler une commande dans la liste de l'historique, mais que vous ne voulez pas appuyer sur la touche fléchée à plusieurs reprises, vous pouvez appuyer sur **CTRL-R** pour effectuer une recherche intelligente inversée.

Dès que vous commencez à taper, la recherche remonte dans l'ordre inverse jusqu'à la première commande qui correspond aux lettres que vous avez tapées. En tapant plus de lettres successives, vous rendez la correspondance de plus en plus spécifique.

Voici un exemple de la façon dont vous pouvez utiliser la commande **CTRL-R** pour effectuer une recherche dans l'historique des commandes :

**$ ^R**                                                                      (Tout cela se passe sur 1 ligne)
**(reverse-i-search)'s': sleep 1000**         (Recherché 's'; correspondance "sleep")
**$ sleep 1000**                                                     (Appuyé sur Entrée pour exécuter la commande recherchée)
**$**

### Exécution des commandes précédentes

Le tableau décrit la syntaxe utilisée pour exécuter les commandes précédemment utilisées :

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Syntaxe</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Tâche</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Démarrer une substitution d'historique</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!$</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Faire référence au dernier argument d'une ligne</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!n</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Faire référence à la n<sup style="font-size: 12px; line-height: 1.4em; position: relative; vertical-align: baseline; top: -0.5em;">ième</sup><span>&nbsp;</span>ligne de commande</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">!string</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Faire référence à la commande la plus récente commençant par string</td></tr></tbody></table>

Toutes les substitutions d'historique commencent par **!**. En tapant la commande : **ls -l /bin /etc /var**, **!$** fera référence à **/var**, le dernier argument de la commande.

Voici d'autres exemples :

**$ history**

1. **echo $SHELL**
2. **echo $HOME**
3. **echo $PS1**
4. **ls -a**
5. **ls -l /etc/ passwd**
6. **sleep 1000**
7. **history**

**$ !1**                              (Exécuter la commande n°1 ci-dessus)
**echo $SHELL**
**/bin/bash**

**$ !sl**                           (Exécuter la commande commençant par "sl")
**sleep 1000**
**$**

### Raccourcis clavier

Vous pouvez utiliser des raccourcis clavier pour effectuer différentes tâches rapidement. Le tableau liste certains de ces raccourcis clavier et leurs utilisations. Notez que la casse de la "touche de raccourci" n'a pas d'importance, par exemple faire **CTRL-a** est la même chose que faire **CTRL-A**.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="20%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Raccourci clavier</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Tâche</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL-L</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Efface l'écran</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-D</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Quitte le shell actuel</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-Z</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Met le processus actuel en arrière-plan suspendu</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-C</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Tue le processus actuel</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-H</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Fonctionne comme la touche retour arrière</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-A</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Va au début de la ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-W</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprime le mot avant le curseur</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-U</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprime du début de la ligne jusqu'à la position du curseur</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">CTRL</strong><strong style="font-weight: bold; line-height: 1.4em;">-E</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Va à la fin de la ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">Tab</strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Auto-complète les fichiers, répertoires et binaires</td></tr></tbody></table>

### Propriété des fichiers

Sous Linux et d'autres systèmes d'exploitation basés sur UNIX, chaque fichier est associé à un utilisateur qui en est le propriétaire. Chaque fichier est également associé à un groupe (un sous-ensemble de tous les utilisateurs) qui a un intérêt dans le fichier et certains droits, ou permissions : lecture, écriture et exécution.

Les programmes utilitaires suivants concernent la propriété de l'utilisateur et du groupe et la définition des permissions :

<table width="80%" border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="15%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="75%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">chown</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisé pour changer la propriété utilisateur d'un fichier ou d'un répertoire</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">chgrp</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisé pour changer la propriété du groupe</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">chmod</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisé pour changer les permissions sur le fichier, ce qui peut être fait séparément pour le<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">propriétaire</strong>, le<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">groupe</strong><span>&nbsp;</span>et le reste du<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">monde</strong><span>&nbsp;</span>(souvent nommé<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">autre</strong>)</span></td></tr></tbody></table>

### Modes de permission de fichier et chmod

Les fichiers ont trois types de permissions : lecture (**r**), écriture (**w**), exécution (**x**). Celles-ci sont généralement représentées comme dans **rwx**. Ces permissions affectent trois groupes de propriétaires : utilisateur/propriétaire (**u**), groupe (**g**) et autres (**o**).

En conséquence, vous avez les trois groupes de trois permissions suivants :

**rwx: rwx: rwx**
 **u:   g:   o**

Il existe plusieurs façons différentes d'utiliser **chmod**. Par exemple, pour donner au propriétaire et aux autres la permission d'exécution et supprimer la permission d'écriture du groupe :

**$ ls -l somefile**
**-rw-rw-r-- 1 student student 1601 Mar 9 15:04 somefile**
**$ chmod uo+x,g-w somefile**
**$ ls -l somefile**
**-rwxr--r-x 1 student student 1601 Mar 9 15:04 somefile**

où **u** signifie utilisateur (propriétaire), **o** signifie autre (monde), et **g** signifie groupe.

Ce type de syntaxe peut être difficile à taper et à mémoriser, donc on utilise souvent un raccourci qui vous permet de définir toutes les permissions en une seule étape. Cela se fait avec un algorithme simple, et un seul chiffre suffit pour spécifier les trois bits de permission pour chaque entité. Ce chiffre est la somme de :

* **4** si la permission de lecture est souhaitée
* **2** si la permission d'écriture est souhaitée
* **1** si la permission d'exécution est souhaitée

Ainsi, **7** signifie lecture/écriture/exécution, **6** signifie lecture/écriture, et **5** signifie lecture/exécution.

Lorsque vous appliquez cela à la commande **chmod**, vous devez donner trois chiffres pour chaque degré de liberté, comme dans :

**$ chmod 755 somefile**
**$ ls -l somefile**
**-rwxr-xr-x 1 student student 1601 Mar 9 15:04 somefile**

![Modes de permission de fichier et chmod](https://courses.edx.org/assets/courseware/v1/5d60930deeaaca887d468867240fc6e0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chmodmint.png)
_Modes de permission de fichier et chmod_

### Exemple de chown

Voyons un exemple de changement de propriété de fichier en utilisant **chown**, comme indiqué dans la capture d'écran à droite. Tout d'abord, nous créons deux fichiers vides en utilisant **touch**.

Remarquez qu'il faut sudo pour changer le propriétaire de **file2** en root. La deuxième commande **chown** change à la fois le propriétaire et le groupe en même temps !

Enfin, seul le superutilisateur peut supprimer les fichiers.

![chown](https://courses.edx.org/assets/courseware/v1/d99d45386528584f3f861f182577fb1a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chownrhel7.png)
_chown_

### Exemple de chgrp

Maintenant, voyons un exemple de changement de propriété de groupe en utilisant **chgrp** :

![chgrp](https://courses.edx.org/assets/courseware/v1/2416814b8977e0048d01804a8319aace/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chgrouprhel7.png)
_chgrp_

### Résumé du chapitre

Vous avez terminé le chapitre 12. Résumons les concepts clés couverts :

* Linux est un système multi-utilisateur.
* Pour trouver les utilisateurs actuellement connectés, vous pouvez utiliser la commande **who**.
* Pour trouver l'identifiant utilisateur actuel, vous pouvez utiliser la commande **whoami**.
* Le compte **root** a un accès complet au système. Il n'est jamais judicieux d'accorder un accès root complet à un utilisateur.
* Vous pouvez attribuer des privilèges root aux comptes utilisateurs réguliers sur une base temporaire en utilisant la commande **sudo**.
* Le programme shell (bash) utilise plusieurs fichiers de démarrage pour créer l'environnement utilisateur. Chaque fichier affecte l'environnement interactif d'une manière différente. **/etc/profile** fournit les paramètres globaux.
* Les avantages des fichiers de démarrage incluent qu'ils personnalisent l'invite de l'utilisateur, définissent le type de terminal de l'utilisateur, définissent les raccourcis et alias de ligne de commande, et définissent l'éditeur de texte par défaut, etc.
* Une variable d'environnement est une chaîne de caractères qui contient des données utilisées par une ou plusieurs applications. Les variables shell intégrées peuvent être personnalisées pour répondre à vos besoins.
* La commande **history** rappelle une liste de commandes précédentes, qui peuvent être éditées et recyclées.
* Sous Linux, divers raccourcis clavier peuvent être utilisés à l'invite de commande au lieu de longues commandes réelles.
* Vous pouvez personnaliser les commandes en créant des alias. Ajouter un alias à **~/.bashrc** le rendra disponible pour d'autres shells.
* Les permissions de fichier peuvent être modifiées en tapant **chmod permissions nomfichier**.
* La propriété du fichier est modifiée en tapant **chown propriétaire nomfichier**.
* La propriété du groupe de fichiers est modifiée en tapant **chgrp groupe nomfichier**.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

### Vidéo : Introduction au chapitre 13

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V002500_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Afficher et ajouter au contenu des fichiers en utilisant **cat** et **echo**.
* Éditer et imprimer le contenu des fichiers en utilisant **sed** et **awk**.
* Rechercher des motifs en utilisant **grep**.
* Utiliser plusieurs autres utilitaires pour la manipulation de fichiers et de texte.

### Outils en ligne de commande pour manipuler des fichiers texte

Quel que soit le rôle que vous jouez avec Linux (administrateur système, développeur ou utilisateur), vous avez souvent besoin de parcourir et d'analyser des fichiers texte, et/ou d'en extraire des données. Ce sont des opérations de manipulation de fichiers. Ainsi, il est essentiel pour l'utilisateur Linux de devenir adepte de l'exécution de certaines opérations sur les fichiers.

La plupart du temps, une telle manipulation de fichiers se fait en ligne de commande, ce qui permet aux utilisateurs d'effectuer des tâches plus efficacement qu'en utilisant une interface graphique. De plus, la ligne de commande est plus adaptée à l'automatisation des tâches souvent exécutées.

En effet, les administrateurs système expérimentés écrivent des scripts personnalisés pour accomplir de telles tâches répétitives, standardisées pour chaque environnement particulier. Nous discuterons de tels scripts plus tard en détail.

Dans cette section, nous nous concentrerons sur les utilitaires de manipulation de fichiers et de texte en ligne de commande.

![Outils en ligne de commande pour manipuler des fichiers texte](https://courses.edx.org/assets/courseware/v1/1003ad62cadceacd75a659e16ec77873/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cmdlinetext.png)
_Outils en ligne de commande pour manipuler des fichiers texte_

### cat

**cat** est l'abréviation de _**concatenate**_ (concaténer) et est l'un des utilitaires de ligne de commande Linux les plus fréquemment utilisés. Il est souvent utilisé pour lire et imprimer des fichiers, ainsi que pour simplement visualiser le contenu des fichiers. Pour visualiser un fichier, utilisez la commande suivante :

**$ cat <nomfichier>**

Par exemple, **cat readme.txt** affichera le contenu de **readme.txt** sur le terminal. Cependant, le but principal de **cat** est souvent de combiner (concaténer) plusieurs fichiers ensemble. Vous pouvez effectuer les actions listées dans le tableau en utilisant **cat**.

La commande **tac** (**cat** épelé à l'envers) imprime les lignes d'un fichier dans l'ordre inverse. Chaque ligne reste la même, mais l'ordre des lignes est inversé. La syntaxe de **tac** est exactement la même que pour **cat**, comme dans :

**$ tac fichier**
**$ tac fichier1 fichier2 > nouveaufichier**

<table border="0" align="right" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="60%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat file1 file2</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Concaténer plusieurs fichiers et afficher la sortie ; c'est-à-dire que le contenu entier du premier fichier est suivi de celui du deuxième fichier</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat file1 file2 &gt; newfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Combiner plusieurs fichiers et enregistrer la sortie dans un nouveau fichier</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">cat file &gt;&gt; existingfile</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Ajouter un fichier à la fin d'un fichier existant</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat &gt; file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Toutes les lignes suivantes tapées iront dans le fichier, jusqu'à ce que<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-D</span></strong><span>&nbsp;</span>soit tapé</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">cat &gt;&gt; file</span></span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Toutes les lignes suivantes sont ajoutées au fichier, jusqu'à ce que<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">CTRL-D</span></strong><span>&nbsp;</span>soit tapé</td></tr></tbody></table>

### Utilisation de cat de manière interactive

**cat** peut être utilisé pour lire à partir de l'entrée standard (comme la fenêtre du terminal) si aucun fichier n'est spécifié. Vous pouvez utiliser l'opérateur **>** pour créer et ajouter des lignes dans un nouveau fichier, et l'opérateur **>>** pour ajouter des lignes (ou des fichiers) à un fichier existant. Nous avons mentionné cela en parlant de la façon de créer des fichiers sans éditeur.

Pour créer un nouveau fichier, à l'invite de commande tapez **cat** > **<nomfichier>** et appuyez sur la touche **Entrée**.

Cette commande crée un nouveau fichier et attend que l'utilisateur édite/entre le texte. Après avoir fini de taper le texte requis, appuyez sur **CTRL-D** au début de la ligne suivante pour enregistrer et quitter l'édition.

Une autre façon de créer un fichier au terminal est **cat > <nomfichier> << EOF**. Un nouveau fichier est créé et vous pouvez taper l'entrée requise. Pour quitter, entrez **EOF** au début d'une ligne.

Notez que **EOF** est sensible à la casse. On peut aussi utiliser un autre mot, tel que **STOP**.

![Utilisation de cat : la commande cat << EOF > somefile et sa sortie, ainsi que la commande cat somefile et sa sortie](https://courses.edx.org/assets/courseware/v1/2186f2162bb7f8d6f7fac9004f7d4784/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cateoffedora.png)
_Utilisation de cat_

### Vidéo : Utilisation de cat

<video controls width="100%" preload="none">

<source src="https://edx-video.net/fba83d11-cb13-4df8-9239-cb8f73dc3bdc-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Travailler avec de gros fichiers

Les administrateurs système doivent travailler avec des fichiers de configuration, des fichiers texte, des fichiers de documentation et des fichiers journaux. Certains de ces fichiers peuvent être volumineux ou devenir assez volumineux à mesure qu'ils accumulent des données avec le temps. Ces fichiers nécessiteront à la fois une visualisation et une mise à jour administrative. Dans cette section, vous apprendrez à gérer de tels gros fichiers.

Par exemple, un système bancaire pourrait maintenir un simple gros fichier journal pour enregistrer les détails de toutes les transactions ATM d'une journée. En raison d'une attaque de sécurité ou d'un dysfonctionnement, l'administrateur pourrait être forcé de vérifier certaines données en naviguant dans le fichier. Dans de tels cas, ouvrir directement le fichier dans un éditeur causera des problèmes, en raison de l'utilisation élevée de la mémoire, car un éditeur essaiera généralement de lire tout le fichier en mémoire d'abord. Cependant, on peut utiliser **less** pour visualiser le contenu d'un tel gros fichier, en faisant défiler page par page, sans que le système ait à placer le fichier entier en mémoire avant de commencer. C'est beaucoup plus rapide que d'utiliser un éditeur de texte.

![Diable avec trois boîtes](https://courses.edx.org/assets/courseware/v1/22c34eedb0df480dcad0a9e2dd731131/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/free-file-transfer.jpg)

Visualiser **somefile** peut être fait en tapant l'une des deux commandes suivantes :

**$ less somefile**
**$ cat somefile | less**

Par défaut, les pages **man** sont envoyées via la commande **less**. Vous avez peut-être rencontré l'ancien utilitaire **more** qui a la même fonction de base mais moins de capacités : c'est-à-dire **less** is **more** (moins c'est plus) !

### head

**head** lit les premières lignes de chaque fichier nommé (10 par défaut) et les affiche sur la sortie standard. Vous pouvez donner un nombre différent de lignes dans une option.

Par exemple, si vous voulez imprimer les 5 premières lignes de **/etc/default/grub**, utilisez la commande suivante :

**$ head –n 5 /etc/default/grub**

Vous pouvez aussi simplement dire :

**head -5 /etc/default/grub**

![head](https://courses.edx.org/assets/courseware/v1/a19d53c185f88f384a24c5b0ae6fe03a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/headubuntu.png)
_head_

### tail

**tail** imprime les dernières lignes de chaque fichier nommé et les affiche sur la sortie standard. Par défaut, il affiche les 10 dernières lignes. Vous pouvez donner un nombre différent de lignes en option. **tail** est particulièrement utile lorsque vous dépannez un problème en utilisant des fichiers journaux, car vous voulez probablement voir les lignes de sortie les plus récentes.

Par exemple, pour afficher les 15 dernières lignes de **somefile.log**, utilisez la commande suivante :

**$ tail -n 15 somefile.log**

Vous pouvez aussi simplement dire :

**tail -15 somefile.log**

Pour surveiller continuellement une nouvelle sortie dans un fichier journal en croissance :

**$ tail -f somefile.log**

Cette commande affichera continuellement toutes les nouvelles lignes de sortie dans **somefile.log** dès qu'elles apparaissent. Ainsi, cela vous permet de surveiller toute activité actuelle qui est rapportée et enregistrée.

![tail](https://courses.edx.org/assets/courseware/v1/e218e0f357f957b78420b93f6dc63aaf/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tailubuntu.png)
_tail_

### Visualisation de fichiers compressés

Lorsque vous travaillez avec des fichiers compressés, de nombreuses commandes standard ne peuvent pas être utilisées directement. Pour de nombreux programmes de manipulation de fichiers et de texte couramment utilisés, il existe également une version spécialement conçue pour fonctionner directement avec des fichiers compressés. Ces utilitaires associés ont la lettre "z" préfixée à leur nom. Par exemple, nous avons des programmes utilitaires tels que **zcat**, **zless**, **zdiff** et **zgrep**.

Voici un tableau listant certaines commandes de la famille **z** :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="40%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 1px solid rgb(196, 200, 203); font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zcat compressed-file.txt.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour visualiser un fichier compressé</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zless somefile.gz</span></strong></span><br style="line-height: 1.4em;">ou<br style="line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zmore somefile.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour paginer à travers un fichier compressé</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zgrep -i less somefile.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour rechercher à l'intérieur d'un fichier compressé</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ zdiff file1.txt.gz file2.txt.gz</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour comparer deux fichiers compressés</td></tr></tbody></table>

Notez que si vous exécutez **zless** sur un fichier non compressé, il fonctionnera toujours et ignorera l'étape de décompression. Il existe également des programmes utilitaires équivalents pour d'autres méthodes de compression en plus de **gzip**, par exemple, nous avons **bzcat** et **bzless** associés à **bzip2**, et **xzcat** et **xzless** associés à **xz**.

### Introduction à sed et awk

Il est très courant de créer puis d'éditer et/ou d'extraire à plusieurs reprises du contenu d'un fichier. Apprenons à utiliser **sed** et **awk** pour effectuer facilement de telles opérations.

![Papier et stylo](https://courses.edx.org/assets/courseware/v1/452cbb45fed4bda10d6125b421f77ff7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen12a.jpg)

Notez que de nombreux utilisateurs et administrateurs Linux écriront des scripts en utilisant des langages de script complets tels que Python et perl, plutôt que d'utiliser **sed** et **awk** (et certains autres utilitaires dont nous discuterons plus tard). Utiliser de tels utilitaires est certainement bien dans la plupart des circonstances ; on devrait toujours se sentir libre d'utiliser les outils avec lesquels on est expérimenté. Cependant, les utilitaires qui sont décrits ici sont beaucoup plus légers ; c'est-à-dire qu'ils utilisent moins de ressources système et s'exécutent plus rapidement. Il y a des situations (comme lors du démarrage du système) où beaucoup de temps serait perdu à utiliser les outils plus compliqués, et le système pourrait même ne pas être capable de les exécuter. Donc, les outils plus simples seront toujours nécessaires.

### sed

**sed** est un outil de traitement de texte puissant et est l'un des utilitaires UNIX les plus anciens, les plus précoces et les plus populaires. Il est utilisé pour modifier le contenu d'un fichier ou d'un flux d'entrée, plaçant généralement le contenu dans un nouveau fichier ou flux de sortie. Son nom est une abréviation pour stream editor (éditeur de flux).

![sed](https://courses.edx.org/assets/courseware/v1/64bebc2555b3777d251a871e72e873d7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen_13.jpg)
_sed_

**sed** peut filtrer du texte, ainsi qu'effectuer des substitutions dans des flux de données.

Les données d'une source/fichier d'entrée (ou flux) sont prises et déplacées vers un espace de travail. La liste entière des opérations/modifications est appliquée sur les données dans l'espace de travail et le contenu final est déplacé vers l'espace de sortie standard (ou flux).

### Syntaxe de la commande sed

Vous pouvez invoquer **sed** en utilisant des commandes comme celles listées dans le tableau ci-joint.

<table border="0" align="center" height="228" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="32%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="38%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed -e command &lt;filename&gt;</span></strong></span></p></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Spécifier des commandes d'édition à la ligne de commande, opérer sur le fichier et mettre la sortie sur la sortie standard (par exemple le terminal)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed -f scriptfile &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Spécifier un fichier de script contenant des commandes<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">sed</strong>, opérer sur le fichier et mettre la sortie sur la sortie standard</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "I hate you" | sed s/hate/love/</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utiliser<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;">sed</strong>&nbsp;pour filtrer l'entrée standard, mettant la sortie sur la sortie standard</td></tr></tbody></table>

L'option **-e** vous permet de spécifier plusieurs commandes d'édition simultanément à la ligne de commande. Elle est inutile si vous n'avez qu'une seule opération invoquée.

![Syntaxe de la commande sed](https://courses.edx.org/assets/courseware/v1/43267d11e71aba5dee81d8e780b24579/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/fedorased.png)
_Syntaxe de la commande sed_

### Opérations de base de sed

Maintenant que vous savez que vous pouvez effectuer plusieurs opérations d'édition et de filtrage avec **sed**, expliquons certaines d'entre elles plus en détail. Le tableau explique certaines opérations de base, où **pattern** est la chaîne actuelle et **replace_string** est la nouvelle chaîne :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="45%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="55%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed s/pattern/replace_string/ file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Substituer la première occurrence de la chaîne dans chaque ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed s/pattern/replace_string/g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Substituer toutes les occurrences de la chaîne dans chaque ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed 1,3s/pattern/replace_string/g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Substituer toutes les occurrences de la chaîne dans une plage de lignes</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sed -i s/pattern/replace_string/g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Enregistrer les modifications pour la substitution de chaîne dans le même fichier</td></tr></tbody></table>

Vous devez utiliser l'option **-i** avec précaution, car l'action n'est pas réversible. Il est toujours plus sûr d'utiliser **sed** sans l'option **–i** et de remplacer ensuite le fichier vous-même, comme indiqué dans l'exemple suivant :

**$ sed s/pattern/replace_string/g file1 > file2**

La commande ci-dessus remplacera toutes les occurrences de **pattern** par **replace_string** dans **file1** et déplacera le contenu vers **file2**. Le contenu de **file2** peut être visualisé avec **cat file2**. Si vous approuvez, vous pouvez alors écraser le fichier original avec **mv file2 file1**.

Exemple : Pour convertir **01/02/…** en **JAN/FEB/…**

**sed -e 's/01/JAN/' -e 's/02/FEB/' -e 's/03/MAR/' -e 's/04/APR/' -e 's/05/MAY/' \**
    **-e 's/06/JUN/' -e 's/07/JUL/' -e 's/08/AUG/' -e 's/09/SEP/' -e 's/10/OCT/' \**
    **-e 's/11/NOV/' -e 's/12/DEC/'**

### Vidéo : Utilisation de sed

<video controls width="100%" preload="none">

<source src="https://edx-video.net/8a5ec909-76f5-4085-9b47-15a8181047c8-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### awk

**awk** est utilisé pour extraire puis imprimer des contenus spécifiques d'un fichier et est souvent utilisé pour construire des rapports. Il a été créé aux Bell Labs dans les années 1970 et tire son nom des noms de famille de ses auteurs : Alfred Aho, Peter Weinberger et Brian Kernighan.

**awk** a les fonctionnalités suivantes :

* C'est un utilitaire puissant et un langage de programmation interprété.
* Il est utilisé pour manipuler des fichiers de données, et pour récupérer et traiter du texte.
* Il fonctionne bien avec des champs (contenant une seule pièce de données, essentiellement une colonne) et des enregistrements (une collection de champs, essentiellement une ligne dans un fichier).

**awk** est invoqué comme indiqué ci-dessous :

![awk](https://courses.edx.org/assets/courseware/v1/0969d1beca3f2106cc15d5fb77f74fc0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/awkmint.png)
_awk_

Comme avec **sed**, de courtes commandes **awk** peuvent être spécifiées directement à la ligne de commande, mais un script plus complexe peut être enregistré dans un fichier que vous pouvez spécifier en utilisant l'option **-f**.

<table border="0" height="177" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="45%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk ‘command’&nbsp; file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Spécifier une commande directement à la ligne de commande</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk -f scriptfile file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Spécifier un fichier qui contient le script à exécuter</td></tr></tbody></table>

### Opérations de base de awk

Le tableau explique les tâches de base qui peuvent être effectuées en utilisant **awk**. Le fichier d'entrée est lu une ligne à la fois, et, pour chaque ligne, **awk** correspond au motif donné dans l'ordre donné et effectue l'action demandée. L'option **-F** vous permet de spécifier un caractère _séparateur de champ_ particulier. Par exemple, le fichier **/etc/passwd** utilise "**:**" pour séparer les champs, donc l'option **-F:** est utilisée avec le fichier **/etc/passwd**.

La commande/action dans **awk** doit être entourée d'apostrophes (ou guillemets simples (')). **awk** peut être utilisé comme suit :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="25%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk '{ print $0 }' /etc/passwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Imprimer le fichier entier</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk -F: '{ print $1 }' /etc/passwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Imprimer le premier champ (colonne) de chaque ligne, séparé par un deux-points</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">awk -F: '{ print $1 $7 }' /etc/passwd</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Imprimer le premier et le septième champ de chaque ligne</td></tr></tbody></table>

### Utilitaires de manipulation de fichiers

Dans la gestion de vos fichiers, vous devrez peut-être effectuer des tâches telles que le tri des données et la copie de données d'un emplacement à un autre. Linux fournit de nombreux utilitaires de manipulation de fichiers que vous pouvez utiliser tout en travaillant avec des fichiers texte. Dans cette section, vous apprendrez à connaître les programmes de manipulation de fichiers suivants :

* **sort**
* **uniq**
* **paste**
* **join**
* **split**

Vous apprendrez également les expressions régulières et les motifs de recherche.

![Pingouin de dessin animé bleu portant une clé à molette](https://courses.edx.org/assets/courseware/v1/21bf47717bec390dbeba724a8a1b6ed6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/penguin-156529_640.png)

### sort

**sort** est utilisé pour réorganiser les lignes d'un fichier texte, soit par ordre croissant soit par ordre décroissant selon une clé de tri. Vous pouvez également trier par rapport à des champs particuliers (colonnes) dans un fichier. La clé de tri par défaut est l'ordre des caractères ASCII (c'est-à-dire essentiellement alphabétiquement).

**sort** peut être utilisé comme suit :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Syntaxe</strong></span></td><td width="70%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sort &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Trier les lignes dans le fichier spécifié, selon les caractères au début de chaque ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cat file1 file2 | sort</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Combiner les deux fichiers, puis trier les lignes et afficher la sortie sur le terminal</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sort -r &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Trier les lignes dans l'ordre inverse</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sort -k 3 &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Trier les lignes par le 3ème champ sur chaque ligne au lieu du début</td></tr></tbody></table>

Lorsqu'il est utilisé avec l'option **-u**, **sort** vérifie les valeurs uniques après avoir trié les enregistrements (lignes). C'est équivalent à exécuter **uniq** (dont nous discuterons) sur la sortie de sort.

![sort](https://courses.edx.org/assets/courseware/v1/9d6bbb9d27f74d0472f790c684258fdf/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sort.png)
_sort_

### uniq

**uniq** supprime les lignes consécutives en double dans un fichier texte et est utile pour simplifier l'affichage du texte.

Parce que **uniq** exige que les entrées en double soient consécutives, on exécute souvent sort d'abord puis on tube la sortie dans **uniq** ; si sort est utilisé avec l'option **-u**, il peut faire tout cela en une seule étape.

Pour supprimer les entrées en double de plusieurs fichiers à la fois, utilisez la commande suivante :

**sort file1 file2 | uniq > file3**

ou

**sort -u file1 file2 > file3**

Pour compter le nombre d'entrées en double, utilisez la commande suivante :

**uniq -c filename**

![uniq](https://courses.edx.org/assets/courseware/v1/f1bc4a8919c273c3e321466d5344b2c5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/suseuniq.png)
_uniq_

### paste

Supposons que vous ayez un fichier qui contient le nom complet de tous les employés et un autre fichier qui liste leurs numéros de téléphone et identifiants d'employé. Vous voulez créer un nouveau fichier qui contient toutes les données listées en trois colonnes : nom, identifiant d'employé et numéro de téléphone. Comment pouvez-vous faire cela efficacement sans investir trop de temps ?

**paste** peut être utilisé pour créer un seul fichier contenant les trois colonnes. Les différentes colonnes sont identifiées en fonction de délimiteurs (espacement utilisé pour séparer deux champs). Par exemple, les délimiteurs peuvent être un espace vide, une tabulation ou une **Entrée**. Dans l'image fournie, un seul espace est utilisé comme délimiteur dans tous les fichiers.

**paste** accepte les options suivantes :

* **-d** délimiteurs, qui spécifient une liste de délimiteurs à utiliser au lieu de tabulations pour séparer les valeurs consécutives sur une seule ligne. Chaque délimiteur est utilisé à tour de rôle ; lorsque la liste est épuisée, **paste** recommence au premier délimiteur.
* **-s**, qui fait que paste ajoute les données en série plutôt qu'en parallèle ; c'est-à-dire de manière horizontale plutôt que verticale.

![paste](https://courses.edx.org/assets/courseware/v1/0c746d1cc41ea999719d5cdad330d97b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen27.jpg)

### Utilisation de paste

**paste** peut être utilisé pour combiner des champs (tels que le nom ou le numéro de téléphone) de différents fichiers, ainsi que combiner des lignes de plusieurs fichiers. Par exemple, la ligne un de **file1** peut être combinée avec la ligne un de **file2**, la ligne deux de **file1** peut être combinée avec la ligne deux de **file2**, et ainsi de suite.

Pour coller le contenu de deux fichiers, on peut faire :

**$ paste file1 file2**

La syntaxe pour utiliser un délimiteur différent est la suivante :

**$ paste -d, file1 file2**

Les délimiteurs courants sont 'espace', 'tabulation', '|', 'virgule', etc.

![Utilisation de paste](https://courses.edx.org/assets/courseware/v1/56a2128c6d67fafd5051a4b462b5fddb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/paste.png)
_Utilisation de paste_

### join

Supposons que vous ayez deux fichiers avec certaines colonnes similaires. Vous avez enregistré les numéros de téléphone des employés dans deux fichiers, l'un avec leur prénom et l'autre avec leur nom de famille. Vous voulez combiner les fichiers sans répéter les données des colonnes communes. Comment réalisez-vous cela ?

La tâche ci-dessus peut être réalisée en utilisant **join**, qui est essentiellement une version améliorée de **paste**. Il vérifie d'abord si les fichiers partagent des champs communs, tels que des noms ou des numéros de téléphone, puis joint les lignes dans deux fichiers en fonction d'un champ commun.

![Exemple de join](https://courses.edx.org/assets/courseware/v1/da3d180e87ba8b70a3312fca74ecf815/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch12_screen30.jpg)
_join_

### Utilisation de join

Pour combiner deux fichiers sur un champ commun, à l'invite de commande tapez **join file1 file2** et appuyez sur la touche **Entrée**.

Par exemple, le champ commun (c'est-à-dire qu'il contient les mêmes valeurs) parmi les fichiers **phonebook** et **cities** est le numéro de téléphone, et le résultat de la jointure de ces deux fichiers est montré dans la capture d'écran.

![Utilisation de join](https://courses.edx.org/assets/courseware/v1/4ca7406b9c16747faf118ba6336e0cc5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/join.png)
_Utilisation de join_

### split

**split** est utilisé pour diviser (ou scinder) un fichier en segments de taille égale pour une visualisation et une manipulation plus faciles, et n'est généralement utilisé que sur des fichiers relativement volumineux. Par défaut, **split** divise un fichier en segments de 1000 lignes. Le fichier original reste inchangé, et un ensemble de nouveaux fichiers avec le même nom plus un préfixe ajouté est créé. Par défaut, le préfixe **x** est ajouté. Pour diviser un fichier en segments, utilisez la commande **split infile**.

Pour diviser un fichier en segments en utilisant un préfixe différent, utilisez la commande **split infile <Prefix>**.

![split](https://courses.edx.org/assets/courseware/v1/b842783bcec2180547358c235590e3f6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch012_screen31.jpg)

### Utilisation de split

Nous appliquerons **split** à un fichier dictionnaire anglais-américain de plus de 99 000 lignes :

**$ wc -l american-english**
**99171 american-english**

où nous avons utilisé **wc** (word count, bientôt discuté) pour rapporter le nombre de lignes dans le fichier. Ensuite, en tapant :

**$ split american-english dictionary**

divisera le fichier American-English en 100 segments de taille égale nommés **dictionary_xx_**. Le dernier sera bien sûr un peu plus petit.

![Utilisation de split](https://courses.edx.org/assets/courseware/v1/cccb1abafbbcd04bad08b735f151cbb0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/splitubuntu.png)
_Utilisation de split_

### Expressions régulières et motifs de recherche

Les **expressions régulières** sont des chaînes de texte utilisées pour faire correspondre un motif spécifique, ou pour rechercher un emplacement spécifique, tel que le début ou la fin d'une ligne ou d'un mot. Les expressions régulières peuvent contenir à la fois des caractères normaux ou des méta-caractères dits, tels que ***** et **$**.

De nombreux éditeurs de texte et utilitaires tels que **vi**, **sed**, **awk**, **find** et **grep** travaillent intensivement avec des expressions régulières. Certains des langages informatiques populaires qui utilisent des expressions régulières incluent Perl, Python et Ruby. Cela peut devenir assez compliqué et il y a des livres entiers écrits sur les expressions régulières ; ainsi, nous ne ferons qu'effleurer la surface ici.

Ces expressions régulières sont différentes des caractères génériques (ou méta-caractères) utilisés dans la correspondance de noms de fichiers dans les shells de commande tels que bash (qui ont été couverts dans le chapitre _Opérations en ligne de commande_). Le tableau liste les motifs de recherche et leur utilisation.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Motifs de recherche</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">.(point)</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Correspond à n'importe quel caractère unique</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">a|z</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Correspond à a ou z</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Correspond à la fin d'une ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">^</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Correspond au début d'une ligne</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Correspond à l'élément précédent 0 fois ou plus</td></tr></tbody></table>

### Utilisation des expressions régulières et des motifs de recherche

Par exemple, considérez la phrase suivante : **the quick brown fox jumped over the lazy dog**.

Certains des motifs qui peuvent être appliqués à cette phrase sont les suivants :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">a..</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">correspond à azy</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">b.|j.</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">correspond à la fois à br et ju</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">..$</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">correspond à og</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">l.*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">correspond à lazy dog</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">l.*y</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">correspond à lazy</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">the.*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">correspond à la phrase entière</td></tr></tbody></table>

### grep

**grep** est largement utilisé comme outil de recherche de texte principal. Il scanne les fichiers pour des motifs spécifiés et peut être utilisé avec des expressions régulières, ainsi que des chaînes simples, comme indiqué dans le tableau :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="35%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="55%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep [pattern] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Rechercher un motif dans un fichier et imprimer toutes les lignes correspondantes</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep -v [pattern] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Imprimer toutes les lignes qui ne correspondent<strong style="font-weight: bold; line-height: 1.4em;"><span>&nbsp;</span>pas</strong><span>&nbsp;</span>au motif</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep [0-9] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Imprimer les lignes qui contiennent les nombres<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">0</strong></span><span>&nbsp;</span>à<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">9</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">grep -C 3 [pattern] &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Imprimer le contexte des lignes (nombre spécifié de lignes au-dessus et en dessous du motif) pour correspondre au motif. Ici, le nombre de lignes est spécifié comme 3</td></tr></tbody></table>

### strings

**strings** est utilisé pour extraire toutes les chaînes de caractères imprimables trouvées dans le fichier ou les fichiers donnés en arguments. Il est utile pour localiser du contenu lisible par l'homme intégré dans des fichiers binaires ; pour les fichiers texte, on peut simplement utiliser **grep**.

Par exemple, pour rechercher la chaîne **my_string** dans une feuille de calcul :

**$ strings book1.xls | grep my_string**

La capture d'écran montre une recherche d'un certain nombre de programmes pour voir lesquels ont des licences GPL de différentes versions.

![strings](https://courses.edx.org/assets/courseware/v1/394fc9ada7ed399b6aa5f3d93bf08f89/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/strings.png)
_strings_

### tr

Dans cette section, vous découvrirez quelques utilitaires de texte supplémentaires que vous pouvez utiliser pour effectuer diverses actions sur vos fichiers Linux, telles que changer la casse des lettres ou déterminer le nombre de mots, de lignes et de caractères dans un fichier.

![tr](https://courses.edx.org/assets/courseware/v1/8d86fe669e95004b6b55386e5f15957b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/trfedora.png)
_tr_

L'utilitaire **tr** est utilisé pour traduire des caractères spécifiés en d'autres caractères ou pour les supprimer. La syntaxe générale est la suivante :

**$ tr [options] set1 [set2]**

Les éléments entre crochets sont facultatifs. **tr** nécessite au moins un argument et en accepte un maximum de deux. Le premier, désigné **set1** dans l'exemple, liste les caractères dans le texte à remplacer ou à supprimer. Le second, **set2**, liste les caractères qui doivent être substitués aux caractères listés dans le premier argument. Parfois, ces ensembles doivent être entourés d'apostrophes (ou guillemets simples (')) afin que le shell ignore qu'ils signifient quelque chose de spécial pour le shell. Il est généralement sûr (et peut être requis) d'utiliser les guillemets simples autour de chacun des ensembles comme vous le verrez dans les exemples ci-dessous.

Par exemple, supposons que vous ayez un fichier nommé **city** contenant plusieurs lignes de texte en casse mixte. Pour traduire tous les caractères minuscules en majuscules, à l'invite de commande tapez **cat city | tr a-z A-Z** et appuyez sur la touche **Entrée**.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="65%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Commande</span></strong></td><td width="35%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisation</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertir les minuscules en majuscules</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr '{}' '()' &lt; inputfile &gt; outputfile</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Traduire les accolades en parenthèses</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "This is for testing" | tr [:space:] '\t'</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Traduire les espaces blancs en tabulations</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;Courier New&quot;;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "This&nbsp;&nbsp; is&nbsp;&nbsp; for &nbsp;&nbsp; testing" | tr -s [:space:]</span></strong></span><br style="line-height: 1.4em;"></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Comprimer la répétition de caractères en utilisant<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-s</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "the geek stuff" | tr -d 't'</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprimer les caractères spécifiés en utilisant l'option<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-d</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">echo "my username is 432234" | tr -cd [:digit:]</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compléter les ensembles en utilisant l'option<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-c</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr -cd [:print:] &lt; file.txt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprimer tous les caractères non imprimables d'un fichier</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tr -s '\n' ' ' &lt; file.txt</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Joindre toutes les lignes d'un fichier en une seule ligne</td></tr></tbody></table>

### tee

**tee** prend la sortie de n'importe quelle commande, et, tout en l'envoyant vers la sortie standard, l'enregistre également dans un fichier. En d'autres termes, il _**tee**_ (divise en T) le flux de sortie de la commande : un flux est affiché sur la sortie standard et l'autre est enregistré dans un fichier.

Par exemple, pour lister le contenu d'un répertoire à l'écran et enregistrer la sortie dans un fichier, à l'invite de commande tapez **ls -l | tee newfile** et appuyez sur la touche **Entrée**.

Taper **cat newfile** affichera alors la sortie de **ls –l**.

![Capture d'écran de tee](https://courses.edx.org/assets/courseware/v1/afb2ed8327b3ff3ea608c1dffb16a555/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tee.png)
_tee_

### wc

**wc** (**w**ord **c**ount) compte le nombre de lignes, de mots et de caractères dans un fichier ou une liste de fichiers. Les options sont données dans le tableau ci-dessous.

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Option</span></strong></td><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Description</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">–l</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Affiche le nombre de lignes</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-c</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Affiche le nombre d'octets</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-w</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Affiche le nombre de mots</td></tr></tbody></table>

Par défaut, ces trois options sont actives.

Par exemple, pour imprimer uniquement le nombre de lignes contenues dans un fichier, tapez **wc -l filename** et appuyez sur la touche **Entrée**.

![wc](https://courses.edx.org/assets/courseware/v1/68d3426354bc524157608efe82db0ca6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wcrhel7.png)
_wc_

### cut

**cut** est utilisé pour manipuler des fichiers basés sur des colonnes et est conçu pour extraire des colonnes spécifiques. Le séparateur de colonne par défaut est le caractère **tabulation**. Un délimiteur différent peut être donné comme option de commande.

Par exemple, pour afficher la troisième colonne délimitée par un espace vide, à l'invite de commande tapez **ls -l | cut -d" " -f3** et appuyez sur la touche **Entrée**.

![cut](https://courses.edx.org/assets/courseware/v1/48dd7d485d39f6cafc82a3a0a1c2d01c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cutrhel7.png)
_cut_

### Résumé du chapitre

Vous avez terminé le chapitre 13. Résumons les concepts clés couverts :

* La ligne de commande permet souvent aux utilisateurs d'effectuer des tâches plus efficacement que l'interface graphique.
* **cat**, abréviation de concatenate, est utilisé pour lire, imprimer et combiner des fichiers.
* **echo** affiche une ligne de texte soit sur la sortie standard, soit pour la placer dans un fichier.
* **sed** est un éditeur de flux populaire souvent utilisé pour filtrer et effectuer des substitutions sur des fichiers et des flux de données texte.
* **awk** est un langage de programmation interprété, généralement utilisé comme outil d'extraction de données et de reporting.
* **sort** est utilisé pour trier des fichiers texte et des flux de sortie par ordre croissant ou décroissant.
* **uniq** élimine les entrées en double dans un fichier texte.
* **paste** combine des champs de différents fichiers. Il peut également extraire et combiner des lignes de plusieurs sources.
* **join** combine des lignes de deux fichiers basées sur un champ commun. Il ne fonctionne que si les fichiers partagent un champ commun.
* **split** divise un gros fichier en segments de taille égale.
* Les expressions régulières sont des chaînes de texte utilisées pour la correspondance de motifs. Le motif peut être utilisé pour rechercher un emplacement spécifique, tel que le début ou la fin d'une ligne ou d'un mot.
* **grep** recherche des motifs dans des fichiers texte et des flux de données et peut être utilisé avec des expressions régulières.
* **tr** traduit des caractères, copie l'entrée standard vers la sortie standard et gère des caractères spéciaux.
* **tee** enregistre une copie de la sortie standard dans un fichier tout en l'affichant au terminal.
* **wc** (word count) affiche le nombre de lignes, de mots et de caractères dans un fichier ou un groupe de fichiers.
* **cut** extrait des colonnes d'un fichier.
* **less** visualise des fichiers une page à la fois et permet le défilement dans les deux sens.
* **head** affiche les premières lignes d'un fichier ou d'un flux de données sur la sortie standard. Par défaut, il affiche 10 lignes.
* **tail** affiche les dernières lignes d'un fichier ou d'un flux de données sur la sortie standard. Par défaut, il affiche 10 lignes.
* **strings** extrait les chaînes de caractères imprimables des fichiers binaires.
* La famille de commandes **z** est utilisée pour lire et travailler avec des fichiers compressés.

## Chapitre 14 : Opérations réseau

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Expliquer les concepts de base des réseaux, y compris les types de réseaux et les problèmes d'adressage.
* Configurer des interfaces réseau et utiliser des utilitaires de réseau de base, tels que **ifconfig**, **ip**, **ping**, **route** et **traceroute**.
* Utiliser des navigateurs graphiques et non graphiques, tels que Lynx, w3m, Firefox, Chrome et Epiphany.
* Transférer des fichiers vers et depuis des clients et des serveurs en utilisant des applications graphiques et en mode texte, telles que Filezilla, ftp, sftp, curl et wget.

### Introduction aux réseaux

Un réseau est un groupe d'ordinateurs et de périphériques informatiques connectés ensemble par des canaux de communication, tels que des câbles ou des supports sans fil. Les ordinateurs connectés sur un réseau peuvent être situés dans la même zone géographique ou répartis à travers le monde.

![Image](https://courses.edx.org/assets/courseware/v1/11505fb59c6ba03d861023ab12c3c0a8/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen03.jpg)

Un réseau est utilisé pour :

* Permettre aux périphériques connectés de communiquer entre eux.
* Permettre à plusieurs utilisateurs de partager des périphériques sur le réseau, tels que des serveurs de musique et de vidéo, des imprimantes et des scanners.
* Partager et gérer facilement des informations entre ordinateurs.

La plupart des organisations ont à la fois un réseau interne et une connexion Internet pour que les utilisateurs communiquent avec des machines et des personnes en dehors de l'organisation. Internet est le plus grand réseau au monde et peut être appelé _"le réseau des réseaux"_.

### Adresses IP

Les périphériques connectés à un réseau doivent avoir au moins un identifiant d'adresse réseau unique connu sous le nom d'adresse **IP** (Internet Protocol). L'adresse est essentielle pour acheminer les paquets d'informations à travers le réseau.

L'échange d'informations sur le réseau nécessite l'utilisation de flux de petits paquets, chacun contenant une partie de l'information allant d'une machine à une autre. Ces paquets contiennent des tampons de données, ainsi que des en-têtes qui contiennent des informations sur la destination et la provenance du paquet, et où il s'insère dans la séquence de paquets qui constituent le flux. Les protocoles et logiciels de mise en réseau sont assez compliqués en raison de la diversité des machines et des systèmes d'exploitation avec lesquels ils doivent traiter, ainsi que du fait que même de très anciennes normes doivent être prises en charge.

![Adresses IP](https://courses.edx.org/assets/courseware/v1/6aefe557b5aedfc43e2983372dd202d0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen04.jpg)
_Adresses IP_

### IPv4 et IPv6

Il existe deux types différents d'adresses IP disponibles : IPv4 (version 4) et IPv6 (version 6). IPv4 est plus ancien et de loin le plus largement utilisé, tandis que IPv6 est plus récent et est conçu pour dépasser les limitations inhérentes à l'ancienne norme et fournir beaucoup plus d'adresses possibles.

IPv4 utilise 32 bits pour les adresses ; il n'y a _que_ 4,3 milliards d'adresses uniques disponibles. De plus, de nombreuses adresses sont allouées et réservées, mais pas réellement utilisées. IPv4 est considéré comme inadéquat pour répondre aux besoins futurs car le nombre de périphériques disponibles sur le réseau mondial a énormément augmenté ces dernières années.

IPv6 utilise 128 bits pour les adresses ; cela permet 3,4 X 10<sup>38</sup> adresses uniques. Si vous avez un grand réseau d'ordinateurs et que vous souhaitez en ajouter plus, vous voudrez peut-être passer à IPv6, car il fournit plus d'adresses uniques. Cependant, il peut être complexe de migrer vers IPv6 ; les deux protocoles ne fonctionnent pas toujours bien ensemble. Ainsi, le déplacement des équipements et des adresses vers IPv6 nécessite un effort important et n'a pas été aussi rapide qu'il était prévu à l'origine. Nous discuterons plus d'IPv4 que d'IPv6 car vous êtes plus susceptible d'y avoir affaire.

Une raison pour laquelle IPv4 n'a pas disparu est qu'il existe des moyens de rendre efficacement beaucoup plus d'adresses disponibles par des méthodes telles que le NAT (Network Address Translation). Le NAT permet de partager une adresse IP entre de nombreux ordinateurs connectés localement, chacun ayant une adresse unique vue uniquement sur le réseau local. Bien que cela soit utilisé dans des contextes organisationnels, c'est également utilisé dans les réseaux domestiques simples. Par exemple, si vous avez un routeur connecté à votre fournisseur d'accès Internet (comme un système par câble), il vous donne une adresse visible de l'extérieur, mais émet à chaque appareil de votre maison une adresse locale individuelle.

![IPv4 et IPv6](https://courses.edx.org/assets/courseware/v1/fa98328f7ff2e180a79cead9ee3e433f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen05.jpg)

### Décodage des adresses IPv4

Une adresse IPv4 de 32 bits est divisée en quatre sections de 8 bits appelées [octets](https://fr.wikipedia.org/wiki/Octet).

Exemple :
Adresse IP →            172  .          16  .          31  .         46
Format binaire →     10101100.00010000.00011111.00101110

_**NOTE**_ : Octet est juste un autre mot pour byte.

Les adresses réseau sont divisées en cinq classes : A, B, C, D et E. Les classes A, B et C sont classées en deux parties : Adresses réseau (Net ID) et Adresse hôte (Host ID). Le Net ID est utilisé pour identifier le réseau, tandis que le Host ID est utilisé pour identifier un hôte dans le réseau. La classe D est utilisée pour des applications multicast spéciales (l'information est diffusée à plusieurs ordinateurs simultanément) et la classe E est réservée pour une utilisation future. Dans cette section, vous apprendrez à connaître les classes A, B et C.

![Décodage des adresses IPv4](https://courses.edx.org/assets/courseware/v1/610943ad6bb219df591ec8659288e630/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen06.jpg)
_Décodage des adresses IPv4_

### Adresses réseau de classe A

Les adresses de classe A utilisent le premier octet d'une adresse IP comme leur Net ID et utilisent les trois autres octets comme Host ID. Le premier bit du premier octet est toujours mis à zéro. Vous ne pouvez donc utiliser que 7 bits pour des numéros de réseau uniques. En conséquence, il y a un maximum de 126 réseaux de classe A disponibles (les adresses 0000000 et 1111111 sont réservées). Sans surprise, cela n'était faisable que lorsqu'il y avait très peu de réseaux uniques avec un grand nombre d'hôtes. À mesure que l'utilisation d'Internet s'est développée, les classes B et C ont été ajoutées afin de répondre à la demande croissante de réseaux indépendants.

Chaque réseau de classe A peut avoir jusqu'à 16,7 millions d'hôtes uniques sur son réseau. La plage d'adresses hôtes va de **1.0.0.0** à **127.255.255.255**.

_**NOTE**_ : La valeur d'un octet, ou 8 bits, peut aller de 0 à 255.

![Adresses réseau de classe A](https://courses.edx.org/assets/courseware/v1/1867a1e02d2827251e50b65a03bcaa1b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen07.jpg)
_Adresses réseau de classe A_

### Adresses réseau de classe B

Les adresses de classe B utilisent les deux premiers octets de l'adresse IP comme leur Net ID et les deux derniers octets comme Host ID. Les deux premiers bits du premier octet sont toujours mis à binaire 10, il y a donc un maximum de 16 384 (14 bits) réseaux de classe B. Le premier octet d'une adresse de classe B a des valeurs de 128 à 191. L'introduction des réseaux de classe B a élargi le nombre de réseaux, mais il est vite devenu clair qu'un niveau supplémentaire serait nécessaire.

Chaque réseau de classe B peut prendre en charge un maximum de 65 536 hôtes uniques sur son réseau. La plage d'adresses hôtes va de **128.0.0.0** à **191.255.255.255**.

![Adresses réseau de classe B](https://courses.edx.org/assets/courseware/v1/7e40d0c228a2ac28dd4e1e9af18ba3ce/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen08.jpg)
_Adresses réseau de classe B_

### Adresses réseau de classe C

Les adresses de classe C utilisent les trois premiers octets de l'adresse IP comme leur Net ID et le dernier octet comme leur Host ID. Les trois premiers bits du premier octet sont mis à binaire 110, donc près de 2,1 millions (21 bits) de réseaux de classe C sont disponibles. Le premier octet d'une adresse de classe C a des valeurs de 192 à 223. Ce sont les plus courants pour les petits réseaux qui n'ont pas beaucoup d'hôtes uniques.

Chaque réseau de classe C peut prendre en charge jusqu'à 256 (8 bits) hôtes uniques. La plage d'adresses hôtes va de **192.0.0.0** à **223.255.255.255**.

![Adresses réseau de classe C](https://courses.edx.org/assets/courseware/v1/376a6fe8144e0d5799f331a803e1d33d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen09.jpg)
_Adresses réseau de classe C_

### Allocation d'adresses IP

Généralement, une plage d'adresses IP est demandée à votre fournisseur d'accès Internet (FAI) par l'administrateur réseau de votre organisation. Souvent, votre choix de la classe d'adresse IP qui vous est donnée dépend de la taille de votre réseau et des besoins de croissance prévus. Si le NAT est en opération, comme dans un réseau domestique, vous n'obtenez qu'une seule adresse visible de l'extérieur !

![Allocation d'adresses IP](https://courses.edx.org/assets/courseware/v1/303c5dc5b32edde05f599cac40512b7d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen10a.jpg)
_Allocation d'adresses IP_

Vous pouvez attribuer des adresses IP aux ordinateurs sur un réseau soit manuellement, soit dynamiquement. L'attribution manuelle ajoute des adresses statiques (ne changeant jamais) au réseau. Les adresses attribuées dynamiquement peuvent changer à chaque redémarrage ou même plus souvent ; le protocole de configuration dynamique des hôtes (**D**ynamic **H**ost **C**onfiguration **P**rotocol - DHCP) est utilisé pour attribuer des adresses IP.

### Résolution de noms

La résolution de noms est utilisée pour convertir des valeurs d'adresses IP numériques en un format lisible par l'homme connu sous le nom de nom d'hôte. Par exemple, **104.95.85.15** est l'adresse IP numérique qui fait référence au nom d'hôte whitehouse.gov. Les noms d'hôtes sont beaucoup plus faciles à retenir !

Étant donné une adresse IP, vous pouvez obtenir son nom d'hôte correspondant. Accéder à la machine sur le réseau devient plus facile lorsque vous pouvez taper le nom d'hôte au lieu de l'adresse IP.

Vous pouvez afficher le nom d'hôte de votre système simplement en tapant **hostname** sans argument.

_**NOTE**_ : Si vous donnez un argument, le système essaiera de changer son nom d'hôte pour qu'il corresponde, cependant, seuls les utilisateurs root peuvent le faire.

Le nom d'hôte spécial localhost est associé à l'adresse IP **127.0.0.1** et décrit la machine sur laquelle vous vous trouvez actuellement (qui a normalement des adresses IP supplémentaires liées au réseau).

![Capture d'écran montrant l'adresse IP du serveur du site Web de la Fondation Linux](https://courses.edx.org/assets/courseware/v1/c4e92d4d86a678c688c053c06672df41/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen12.jpg)
_Capture d'écran montrant l'adresse IP du serveur du site Web de la Fondation Linux_

<video controls width="100%" preload="none">

<source src="https://edx-video.net/fccd6182-2956-47b2-a3d8-6dd2e15ef226-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Fichiers de configuration réseau

Les fichiers de configuration réseau sont essentiels pour garantir que les interfaces fonctionnent correctement. Ils sont situés dans l'arborescence du répertoire **/etc**. Cependant, les fichiers exacts utilisés ont historiquement dépendu de la distribution Linux particulière et de la version utilisée.

Pour les configurations de la famille Debian, les fichiers de configuration réseau de base pouvaient être trouvés sous **/etc/network/**, tandis que pour les systèmes des familles Red Hat et SUSE, il fallait inspecter **/etc/sysconfig/network**.

Les systèmes modernes mettent l'accent sur l'utilisation de Network Manager, dont nous avons brièvement discuté lorsque nous avons examiné l'administration système graphique, plutôt que d'essayer de suivre les caprices des fichiers dans **/etc**. Bien que les versions graphiques de Network Manager semblent quelque peu différentes dans différentes distributions, l'utilitaire **nmtui** (montré dans la capture d'écran) varie presque pas du tout, tout comme l'utilitaire **nmcli** (interface en ligne de commande) encore plus spartiate. Si vous maîtrisez l'utilisation des interfaces graphiques, utilisez-les par tous les moyens. Si vous travaillez sur une variété de systèmes, les utilitaires de niveau inférieur peuvent vous faciliter la vie.

![Network Manager](https://courses.edx.org/assets/courseware/v1/30ad387df9ee4d04b71b8a402855df8c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/nmtui.png)
_Network Manager_

Les distributions Ubuntu récentes incluent **netplan**, qui est activé par défaut, et supplante Network Manager. Comme aucune autre distribution n'a montré d'intérêt, et comme il peut facilement être désactivé s'il vous dérange, nous l'ignorerons.

### Interfaces réseau

Les interfaces réseau sont un canal de connexion entre un périphérique et un réseau. Physiquement, les interfaces réseau peuvent passer par une carte d'interface réseau (NIC), ou peuvent être implémentées de manière plus abstraite sous forme de logiciel. Vous pouvez avoir plusieurs interfaces réseau fonctionnant à la fois. Des interfaces spécifiques peuvent être activées (brought up) ou désactivées (brought down) à tout moment.

Les informations sur une interface réseau particulière ou toutes les interfaces réseau peuvent être rapportées par les utilitaires **ip** et **ifconfig**, que vous devrez peut-être exécuter en tant que superutilisateur, ou au moins, donner le chemin complet, c'est-à-dire **/sbin/ifconfig**, sur certaines distributions. **ip** est plus récent que **ifconfig** et a beaucoup plus de capacités, mais sa sortie est plus laide à l'œil humain. Certaines nouvelles distributions Linux n'installent pas l'ancien paquet **net-tools** auquel appartient **ifconfig**, et vous devrez donc l'installer si vous voulez l'utiliser.

![Interfaces réseau](https://courses.edx.org/assets/courseware/v1/13f3ece7b614bbaab0872571831112b2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ipiconfigrhel7.png)
_Interfaces réseau_

### L'utilitaire ip

Pour voir l'adresse IP :

**$ /sbin/ip addr show**

Pour voir les informations de routage :

**$ /sbin/ip route show**

**ip** est un programme très puissant qui peut faire beaucoup de choses. Des utilitaires plus anciens (et plus spécifiques) tels que **ifconfig** et **route** sont souvent utilisés pour accomplir des tâches similaires. Un coup d'œil aux pages man pertinentes peut vous en dire beaucoup plus sur ces utilitaires.

![utilitaire ip](https://courses.edx.org/assets/courseware/v1/a863fadf4376afe31b1e3fea08fcc1cc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/iprhel7.png)
_Utilitaire ip_

### ping

**ping** est utilisé pour vérifier si une machine connectée au réseau peut ou non recevoir et envoyer des données ; c'est-à-dire qu'il confirme que l'hôte distant est en ligne et répond.

Pour vérifier l'état de l'hôte distant, à l'invite de commande, tapez **ping <nom d'hôte>**.

**ping** est fréquemment utilisé pour les tests et la gestion du réseau ; cependant, son utilisation peut augmenter la charge du réseau de manière inacceptable. Par conséquent, vous pouvez interrompre l'exécution de **ping** en tapant **CTRL-C**, ou en utilisant l'option **-c**, qui limite le nombre de paquets que **ping** enverra avant de quitter. Lorsque l'exécution s'arrête, un résumé est affiché.

![ping](https://courses.edx.org/assets/courseware/v1/ff267f7328fc6da9070a550a1b43d40b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pingc8.png)
_ping_

### route

Un réseau nécessite la connexion de nombreux nœuds. Les données se déplacent de la source à la destination en passant par une série de routeurs et potentiellement à travers plusieurs réseaux. Les serveurs maintiennent des tables de routage contenant les adresses de chaque nœud du réseau. Les protocoles de routage IP permettent aux routeurs de construire une table de transfert qui corrèle les destinations finales avec les adresses de saut suivant.

![route](https://courses.edx.org/assets/courseware/v1/fe2820385b830a22cf8deccad8e0428c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/routeubuntu.png)
_route_

On peut utiliser l'utilitaire **route** ou la nouvelle commande **ip route** pour visualiser ou modifier la table de routage IP pour ajouter, supprimer ou modifier des routes spécifiques (statiques) vers des hôtes ou des réseaux spécifiques. Le tableau explique certaines commandes qui peuvent être utilisées pour gérer le routage IP :

<table border="0" height="218" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Tâche</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Afficher la table de routage actuelle</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ route –n</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ip route</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Ajouter une route statique</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ route add -net address</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ip route add</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supprimer une route statique</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$ route del -net address</span></strong><span>&nbsp;</span>ou<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ip route del</span></strong></td></tr></tbody></table>

### traceroute

**traceroute** est utilisé pour inspecter la route que le paquet de données emprunte pour atteindre l'hôte de destination, ce qui le rend très utile pour dépanner les retards et les erreurs réseau. En utilisant **traceroute**, vous pouvez isoler les problèmes de connectivité entre les sauts, ce qui aide à les résoudre plus rapidement.

Pour imprimer la route empruntée par le paquet pour atteindre l'hôte réseau, à l'invite de commande, tapez **traceroute <adresse>**.

![traceroute](https://courses.edx.org/assets/courseware/v1/58901958924b2bc7e0ffe898fb384926/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tracerouterhel7.png)
_traceroute_

### Plus d'outils réseau

Maintenant, apprenons quelques outils réseau supplémentaires. Les outils réseau sont très utiles pour surveiller et déboguer les problèmes de réseau, tels que la connectivité réseau et le trafic réseau.

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="25%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Outils réseau</strong></span></td><td align="center" bgcolor="#003f60" width="55%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ethtool</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Interroge les interfaces réseau et peut également définir divers paramètres tels que la vitesse</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">netstat</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Affiche toutes les connexions actives et les tables de routage ; utile pour surveiller les performances et le dépannage</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">nmap</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Scanne les ports ouverts sur un réseau ; important pour l'analyse de sécurité</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">tcpdump</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Vide le trafic réseau pour analyse</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">iptraf</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Surveille le trafic réseau en mode texte</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">mtr</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Combine les fonctionnalités de ping et traceroute et donne un affichage mis à jour en continu</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">dig</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Teste le fonctionnement du DNS ; un bon remplacement pour host et nslookup</td></tr></tbody></table>

### Vidéo : Utilisation de plus d'outils réseau

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINLFS10/LINLFS102014-V004400_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Navigateurs graphiques et non graphiques

Les navigateurs sont utilisés pour récupérer, transmettre et explorer des ressources d'information, généralement sur le World Wide Web. Les utilisateurs de Linux utilisent couramment des applications de navigateur graphiques et non graphiques.

Les navigateurs graphiques courants utilisés sous Linux sont :

* [Firefox](https://www.mozilla.org/en-US/firefox/)
* [Google Chrome](https://www.google.com/chrome/)
* [Chromium](https://www.chromium.org/Home)
* [Konqueror](https://kde.org/applications/internet/org.kde.konqueror)
* [Opera](https://www.opera.com/)

Parfois, vous n'avez pas d'environnement graphique pour travailler (ou avez des raisons de ne pas l'utiliser) mais avez quand même besoin d'accéder à des ressources Web. Dans un tel cas, vous pouvez utiliser des navigateurs non graphiques, tels que les suivants :

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Navigateurs non graphiques</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><a href="http://lynx.browser.org/" target="_blank" style="color: rgb(0, 104, 141); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; text-decoration: none; transition: all 0.1s linear 0s;">lynx</a></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Navigateur web textuel configurable ; le plus ancien navigateur de ce type et toujours utilisé</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><a href="http://www.elinks.cz/" target="_blank" style="color: rgb(0, 104, 141); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; text-decoration: none; transition: all 0.1s linear 0s;">elinks</a></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Basé sur Lynx ; il peut afficher des tableaux et des cadres</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><a href="http://w3m.sourceforge.net/" target="_blank" style="color: rgb(0, 104, 141); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit; text-decoration: none; transition: all 0.1s linear 0s;">w3m</a></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Un autre navigateur web textuel avec de nombreuses fonctionnalités</td></tr></tbody></table>

### wget

Parfois, vous devez télécharger des fichiers et des informations, mais un navigateur n'est pas le meilleur choix, soit parce que vous voulez télécharger plusieurs fichiers et/ou répertoires, soit parce que vous voulez effectuer l'action à partir d'une ligne de commande ou d'un script. **wget** est un utilitaire de ligne de commande qui peut gérer efficacement les types de téléchargements suivants :

* Téléchargements de gros fichiers
* Téléchargements récursifs, où une page Web fait référence à d'autres pages Web et toutes sont téléchargées en même temps
* Téléchargements nécessitant un mot de passe
* Téléchargements de fichiers multiples.

Pour télécharger une page Web, vous pouvez simplement taper **wget <url>**, puis vous pouvez lire la page téléchargée comme un fichier local en utilisant un navigateur graphique ou non graphique.

![wget](https://courses.edx.org/assets/courseware/v1/47e400802600472e68f58d081c51a252/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/wgetc8.png)
_wget_

### curl

En plus du téléchargement, vous voudrez peut-être obtenir des informations sur une URL, telles que le code source utilisé. **curl** peut être utilisé à partir de la ligne de commande ou d'un script pour lire de telles informations. **curl** vous permet également d'enregistrer le contenu d'une page Web dans un fichier, tout comme **wget**.

Vous pouvez lire une URL en utilisant **curl <URL>**. Par exemple, si vous voulez lire [http://www.linuxfoundation.org](https://www.linuxfoundation.org/), tapez **curl http://www.linuxfoundation.org**.

Pour obtenir le contenu d'une page Web et le stocker dans un fichier, tapez **curl -o saved.html http://www.mysite.com**. Le contenu du fichier d'index principal du site Web sera enregistré dans **saved.html**.

![curl](https://courses.edx.org/assets/courseware/v1/f82c5e92a716627d3623a7cb1286613d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/curlrhel7.png)
_curl_

### FTP (File Transfer Protocol)

Lorsque vous êtes connecté à un réseau, vous devrez peut-être transférer des fichiers d'une machine à une autre. Le protocole de transfert de fichiers (FTP) est une méthode bien connue et populaire pour transférer des fichiers entre ordinateurs en utilisant Internet. Cette méthode est construite sur un modèle client-serveur. FTP peut être utilisé dans un navigateur ou avec des programmes clients autonomes.

![File Transfer Protocol](https://courses.edx.org/assets/courseware/v1/6c4efd743bc9707314f89c414e219e88/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen33.jpg)
_File Transfer Protocol_

FTP est l'une des plus anciennes méthodes de transfert de données réseau, remontant au début des années 1970. En tant que tel, il est considéré comme inadéquat pour les besoins modernes, ainsi que comme intrinsèquement non sécurisé. Cependant, il est toujours utilisé et lorsque la sécurité n'est pas une préoccupation (comme avec le soi-disant FTP anonyme), cela peut avoir du sens. Cependant, de nombreux sites Web, tels que [kernel.org](https://www.kernel.org/), ont abandonné son utilisation.

### Clients FTP

Les clients FTP vous permettent de transférer des fichiers avec des ordinateurs distants en utilisant le protocole FTP. Ces clients peuvent être des outils graphiques ou en ligne de commande. Filezilla, par exemple, permet l'utilisation de l'approche glisser-déposer pour transférer des fichiers entre hôtes. Tous les navigateurs Web prennent en charge FTP, il vous suffit de donner une URL comme **ftp://ftp.kernel.org** où l'habituel **http://** devient **ftp://**.

Certains clients FTP en ligne de commande sont :

* **ftp**
* **sftp**
* **ncftp**
* **yafc** (Yet Another FTP Client).

FTP est tombé en disgrâce sur les systèmes modernes, car il est intrinsèquement non sécurisé, puisque les mots de passe sont des informations d'identification utilisateur qui peuvent être transmises sans cryptage et sont donc sujettes à l'interception. Ainsi, il a été supprimé au profit de l'utilisation de **rsync** et de l'accès https par navigateur Web par exemple. Comme alternative, **sftp** est un mode de connexion très sécurisé, qui utilise le protocole Secure Shell (**ssh**), dont nous discuterons sous peu. **sftp** crypte ses données et ainsi les informations sensibles sont transmises de manière plus sécurisée. Cependant, il ne fonctionne pas avec le soi-disant FTP anonyme (informations d'identification utilisateur invité).

![Clients FTP](https://courses.edx.org/assets/courseware/v1/0daf82fa22922b50848d2d73df3cfa1c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen34.jpg)
_Clients FTP_

### SSH : Exécution de commandes à distance

Secure Shell (SSH) est un protocole réseau cryptographique utilisé pour la communication de données sécurisée. Il est également utilisé pour les services distants et d'autres services sécurisés entre deux périphériques sur le réseau et est très utile pour administrer des systèmes sur lesquels il n'est pas facile de travailler physiquement, mais auxquels vous avez un accès distant.

![SSH : Exécution de commandes à distance](https://courses.edx.org/assets/courseware/v1/b19e7547d1f707f6ba4b134c31f43a31/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen37.jpg)
_SSH : Exécution de commandes à distance_

Pour vous connecter à un système distant en utilisant votre même nom d'utilisateur, vous pouvez simplement taper **ssh un_systeme** et appuyer sur **Entrée**. **ssh** vous demande alors le mot de passe distant. Vous pouvez également configurer ssh pour autoriser en toute sécurité votre accès distant sans taper de mot de passe à chaque fois.

Si vous voulez vous exécuter en tant qu'un autre utilisateur, vous pouvez faire soit **ssh -l quelquun un_systeme** soit **ssh quelquun@un_systeme**. Pour exécuter une commande sur un système distant via SSH, à l'invite de commande, vous pouvez taper **ssh un_systeme ma_commande**.

### Copie de fichiers en toute sécurité avec scp

Nous pouvons également déplacer des fichiers en toute sécurité en utilisant Secure Copy (scp) entre deux hôtes en réseau. scp utilise le protocole SSH pour transférer des données.

Pour copier un fichier local vers un système distant, à l'invite de commande, tapez **scp <fichierlocal> <utilisateur@systemedistant>:/home/utilisateur/** et appuyez sur **Entrée**.

Vous recevrez une invite pour le mot de passe distant. Vous pouvez également configurer **scp** pour qu'il ne demande pas de mot de passe pour chaque transfert.

![Copie de fichiers en toute sécurité avec scp](https://courses.edx.org/assets/courseware/v1/83970c9d6a9a9462fe7463ada6b79e45/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch11_screen38.jpg)
_Copie de fichiers en toute sécurité avec scp_

### Vidéo : Utilisation de SSH entre deux machines virtuelles

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002000_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

## Résumé du chapitre

Vous avez terminé le chapitre 14. Résumons les concepts clés couverts :

* L'adresse IP (Internet Protocol) est une adresse réseau logique unique qui est attribuée à un périphérique sur un réseau.
* IPv4 utilise 32 bits pour les adresses et IPv6 utilise 128 bits pour les adresses.
* Chaque adresse IP contient à la fois un champ réseau et un champ adresse hôte.
* Il existe cinq classes d'adresses réseau disponibles : A, B, C, D & E.
* DNS (Domain Name System) est utilisé pour convertir les noms de domaine Internet et les noms d'hôtes en adresses IP.
* Le programme **ifconfig** est utilisé pour afficher les interfaces réseau actives actuelles.
* Les commandes **ip addr show** et **ip route show** peuvent être utilisées pour afficher les informations d'adresse IP et de routage.
* Vous pouvez utiliser **ping** pour vérifier si l'hôte distant est vivant et répond.
* Vous pouvez utiliser le programme utilitaire **route** pour gérer le routage IP.
* Vous pouvez surveiller et déboguer les problèmes de réseau à l'aide d'outils réseau.
* Firefox, Google Chrome, Chromium et Epiphany sont les principaux navigateurs graphiques utilisés sous Linux.
* Les navigateurs non graphiques ou textuels utilisés sous Linux sont Lynx, Links et w3m.
* Vous pouvez utiliser **wget** pour télécharger des pages Web.
* Vous pouvez utiliser **curl** pour obtenir des informations sur les URL.
* FTP (File Transfer Protocol) est utilisé pour transférer des fichiers sur un réseau.
* ftp, sftp, ncftp et yafc sont des clients FTP en ligne de commande utilisés sous Linux.
* Vous pouvez utiliser **ssh** pour exécuter des commandes sur des systèmes distants.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)



## Chapitre 15 : Le shell Bash et les scripts de base

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Expliquer les fonctionnalités et les capacités des scripts shell bash.
* Connaître la syntaxe de base des instructions de script.
* Être familier avec diverses méthodes et constructions utilisées.
* Tester les propriétés et l'existence de fichiers et d'autres objets.
* Utiliser des instructions conditionnelles, telles que les blocs if-then-else.
* Effectuer des opérations arithmétiques en utilisant le langage de script.

### Scripts Shell

Supposons que vous vouliez rechercher un nom de fichier, vérifier si le fichier associé existe, puis répondre en conséquence, en affichant un message confirmant ou non l'existence du fichier. Si vous n'avez besoin de le faire qu'une seule fois, vous pouvez simplement taper une séquence de commandes dans un terminal. Cependant, si vous devez le faire plusieurs fois, l'automatisation est la voie à suivre. Afin d'automatiser des ensembles de commandes, vous devrez apprendre à écrire des scripts shell. Le plus souvent sous Linux, ces scripts sont développés pour être exécutés sous l'interpréteur de commandes **bash**. Le graphique illustre plusieurs des avantages du déploiement de scripts.

![Fonctionnalités des scripts Shell : Combiner des séquences longues et répétitives de commandes en une seule commande simple ; Partager des procédures entre plusieurs utilisateurs ; Prototypage rapide, pas besoin de compiler ; Créer de nouvelles commandes en utilisant une combinaison d'utilitaires ; Fournir une interface contrôlée aux utilisateurs ; Automatiser les tâches et réduire le risque d'erreurs](https://courses.edx.org/assets/courseware/v1/86597edd8ece86b852333387ed386d8b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch14_screen03.jpg)

**Fonctionnalités des scripts Shell**

**_NOTE :_** _De nombreux sujets abordés dans ce chapitre et le suivant ont déjà été introduits plus tôt, lors de la discussion sur les choses qui peuvent être faites en ligne de commande. Nous avons choisi de répéter une partie de cette discussion afin de rendre les sections sur les scripts autonomes, donc la répétition est intentionnelle._

### Choix de shell de commande

L'interpréteur de commandes est chargé d'exécuter les instructions qui le suivent dans le script. Les interpréteurs couramment utilisés incluent : **/usr/bin/perl**, **/bin/bash**, **/bin/csh**, **/usr/bin/python** et **/bin/sh**.

Taper une longue séquence de commandes dans une fenêtre de terminal peut être compliqué, long et sujet aux erreurs. En déployant des scripts shell, l'utilisation de la ligne de commande devient un moyen efficace et rapide de lancer des séquences complexes d'étapes. Le fait que les scripts shell soient enregistrés dans un fichier facilite également leur utilisation pour créer de nouvelles variations de script et partager des procédures standard avec plusieurs utilisateurs.

Linux offre un large choix de shells ; ce qui est exactement disponible sur le système est listé dans **/etc/shells**. Les choix typiques sont :

**/bin/sh**
**/bin/bash**
**/bin/tcsh**
**/bin/csh**
**/bin/ksh**
**/bin/zsh**

La plupart des utilisateurs Linux utilisent le shell bash par défaut, mais ceux ayant une longue expérience UNIX avec d'autres shells peuvent vouloir outrepasser la valeur par défaut.

![Choix de shell de commande](https://courses.edx.org/assets/courseware/v1/8ddc714dd87a83c3b2724d72c86a42a4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_chapter14_screen_5.jpeg)
_Choix de shell de commande_

### Scripts Shell

Rappelez-vous de notre discussion précédente, un shell est un interpréteur de ligne de commande qui fournit l'interface utilisateur pour les fenêtres de terminal. Il peut également être utilisé pour exécuter des scripts, même dans des sessions non interactives sans fenêtre de terminal, comme si les commandes étaient directement tapées. Par exemple, taper **find . -name "*.c" -ls** à la ligne de commande accomplit la même chose que l'exécution d'un fichier de script contenant les lignes :

**#!/bin/bash**
**find . -name "*.c" -ls**

La première ligne du script, qui commence par **#!**, contient le chemin complet de l'interpréteur de commandes (dans ce cas **/bin/bash**) qui doit être utilisé sur le fichier. Comme nous l'avons noté, vous avez pas mal de choix pour le langage de script que vous pouvez utiliser, tel que **/usr/bin/perl**, **/bin/csh**, **/usr/bin/python**, etc.

![Scripts Shell - Capture d'écran de find . -name](https://courses.edx.org/assets/courseware/v1/0eb4ca4bc524fd56385e35895ee29687/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/findcrhel.png)
_Scripts Shell_

### Un script bash simple

Écrivons un script bash simple qui affiche un message d'une ligne à l'écran. Soit tapez :

**$ cat > hello.sh**
**#!/bin/bash**
**echo "Hello Linux Foundation Student"**

et appuyez sur **ENTRÉE** et **CTRL-D** pour enregistrer le fichier, ou créez simplement **hello.sh** dans votre éditeur de texte préféré. Ensuite, tapez **chmod +x hello.sh** pour rendre le fichier exécutable par tous les utilisateurs.

Vous pouvez ensuite exécuter le script en tapant **./hello.sh** ou en faisant :

**$ bash hello.sh**
**Hello Linux Foundation Student**

_**NOTE**_ : Si vous utilisez la deuxième forme, vous n'avez pas à rendre le fichier exécutable.

![Un script bash simple ; ceci est une capture d'écran des commandes utilisées comme exemples dans cette section et leur sortie](https://courses.edx.org/assets/courseware/v1/4fca06e1c36113a2f4e0fc7975e8020b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/hellosuse.png)
_Un script bash simple_

### Exemple interactif utilisant des scripts bash

Maintenant, voyons comment créer un exemple plus interactif en utilisant un script bash. L'utilisateur sera invité à entrer une valeur, qui est ensuite affichée à l'écran. La valeur est stockée dans une variable temporaire, **name**. Nous pouvons référencer la valeur d'une variable shell en utilisant un **$** devant le nom de la variable, tel que **$name**. Pour créer ce script, vous devez créer un fichier nommé **getname.sh** dans votre éditeur préféré avec le contenu suivant :

**#!/bin/bash**
**# Lecture interactive d'une variable**
**echo "ENTER YOUR NAME"**
**read name**
**# Afficher l'entrée de la variable**
**echo The name given was :$name**

Encore une fois, rendez-le exécutable en faisant **chmod +x getname.sh**.

Dans l'exemple ci-dessus, lorsque l'utilisateur tape **./getname.sh** et que le script est exécuté, l'utilisateur est invité avec la chaîne **ENTER YOUR NAME**. L'utilisateur doit alors entrer une valeur et appuyer sur la touche **Entrée**. La valeur sera alors imprimée.

_**NOTE**_ : Le dièse/croisillon/signe numéro (**_#_**) est utilisé pour commencer les commentaires dans le script et peut être placé n'importe où dans la ligne (le reste de la ligne est considéré comme un commentaire). Cependant, notez que la combinaison magique spéciale de **_#!_**, utilisée sur la première ligne, est une exception unique à cette règle.

![Exemple interactif utilisant des scripts bash, ceci est une capture d'écran de l'exemple fourni dans le texte](https://courses.edx.org/assets/courseware/v1/7c1b84e695c8774f7ffb474cf9321a74/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/getnamesuse.png)
_Exemple interactif utilisant des scripts bash_

### Valeurs de retour

Tous les scripts shell génèrent une valeur de retour à la fin de l'exécution, qui peut être explicitement définie avec l'instruction **exit**. Les valeurs de retour permettent à un processus de surveiller l'état de sortie d'un autre processus, souvent dans une relation parent-enfant. Connaître comment le processus se termine permet de prendre toutes les mesures appropriées qui sont nécessaires ou conditionnelles au succès ou à l'échec.

![Valeurs de retour : Représentation du processus parent appelant le processus enfant, qui à son tour renvoie une valeur au processus parent](https://courses.edx.org/assets/courseware/v1/4d9ca0cc7e62c429a040b0592dfe56dc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch14_screen10.jpg)
_Valeurs de retour_

### Visualisation des valeurs de retour

Lorsqu'un script s'exécute, on peut vérifier une valeur ou une condition spécifique et renvoyer le succès ou l'échec comme résultat. Par convention, le succès est renvoyé comme **0**, et l'échec est renvoyé comme une valeur non nulle. Un moyen facile de démontrer l'achèvement avec succès et échec est d'exécuter ls sur un fichier qui existe ainsi que sur un qui n'existe pas, la valeur de retour est stockée dans la variable d'environnement représentée par **$?** :

**$ ls /etc/logrotate.conf**
**/etc/logrotate.conf**

**$ echo $?**
**0**

Dans cet exemple, le système est capable de localiser le fichier **/etc/logrotate.conf** et `**ls**` renvoie une valeur de **0** pour indiquer le succès. Lorsqu'il est exécuté sur un fichier inexistant, il renvoie **2**. Les applications traduisent souvent ces valeurs de retour en messages significatifs facilement compris par l'utilisateur.

![Visualisation des valeurs de retour sur un exemple similaire à celui fourni dans le texte](https://courses.edx.org/assets/courseware/v1/90838d9edb43aa18d3a7805b6b952da3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/returnvalmint.png)
_Visualisation des valeurs de retour_

### Syntaxe de base et caractères spéciaux

Les scripts vous obligent à suivre une syntaxe de langage standard. Des règles délimitent comment définir des variables et comment construire et formater les instructions autorisées, etc. Le tableau liste certaines utilisations de caractères spéciaux dans les scripts bash :

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Caractère</strong></span></td><td align="center" bgcolor="#003f60" width="70%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">#</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour ajouter un commentaire, sauf lorsqu'il est utilisé comme<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">\#</span></strong>, ou comme<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">#!</span></strong><span>&nbsp;</span>lors du démarrage d'un script</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">\</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé à la fin d'une ligne pour indiquer la continuation sur la ligne suivante</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour interpréter ce qui suit comme une nouvelle commande à exécuter ensuite</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Indique que ce qui suit est une variable d'environnement</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&gt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Rediriger la sortie</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&gt;&gt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Ajouter la sortie</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">&lt;</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Rediriger l'entrée</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">|</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Utilisé pour tuber le résultat dans la commande suivante</td></tr></tbody></table>

Il existe d'autres caractères spéciaux et combinaisons de caractères et constructions que les scripts comprennent, tels que **(..)**, **{..}**, **[..]**, **&&**, **||**, **'**, **"**, **$((...))**, dont certains seront discutés plus tard.

### Division de longues commandes sur plusieurs lignes

Parfois, les commandes sont trop longues pour être facilement tapées sur une seule ligne, ou pour être saisies et comprises (même s'il n'y a pas de limite pratique réelle à la longueur d'une ligne de commande).

Dans ce cas, l'opérateur de concaténation (**\**), le caractère barre oblique inverse, est utilisé pour continuer les longues commandes sur plusieurs lignes.

Voici un exemple d'une commande installant une longue liste de paquets sur un système utilisant la gestion de paquets Debian :

**$~/> cd $HOME**
**$~/> sudo apt-get install autoconf automake bison build-essential \**
    **chrpath curl diffstat emacs flex gcc-multilib g++-multilib \**
    **libsdl1.2-dev libtool lzop make mc patch \**
    **screen socat sudo tar texinfo tofrodos u-boot-tools unzip \**
    **vim wget xterm zip**

La commande est divisée en plusieurs lignes pour la rendre lisible et plus facile à comprendre. L'opérateur **\** à la fin de chaque ligne fait que le shell combine (concatène) plusieurs lignes et les exécute comme une seule commande.

![Capture d'écran d'un exemple de division de longues commandes sur plusieurs lignes - similaire à celui donné dans le texte](https://courses.edx.org/assets/courseware/v1/5b9f46e3e0919a56bacc51f56da06592/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/continue.png)
_Division de longues commandes sur plusieurs lignes_

### Mettre plusieurs commandes sur une seule ligne

Les utilisateurs ont parfois besoin de combiner plusieurs commandes et instructions et même de les exécuter conditionnellement en fonction du comportement des opérateurs utilisés entre elles. Cette méthode est appelée chaînage de commandes.

Il existe plusieurs façons différentes de le faire, selon ce que vous voulez faire. Le caractère `**;**` (point-virgule) est utilisé pour séparer ces commandes et les exécuter séquentiellement, comme si elles avaient été tapées sur des lignes séparées. Chaque commande suivante est exécutée, que la précédente ait réussi ou non.

Ainsi, les trois commandes dans l'exemple suivant s'exécuteront toutes, même si celles qui les précèdent échouent :

**$ make ; make install ; make clean**

Cependant, vous voudrez peut-être interrompre les commandes suivantes lorsqu'une commande antérieure échoue. Vous pouvez le faire en utilisant l'opérateur **&&** (et) comme dans :

**$ make && make install && make clean**

Si la première commande échoue, la seconde ne sera jamais exécutée. Un dernier raffinement consiste à utiliser l'opérateur **||** (ou), comme dans :

**$ cat file1 || cat file2 || cat file3**

Dans ce cas, vous continuez jusqu'à ce que quelque chose réussisse, puis vous arrêtez d'exécuter d'autres étapes.

Le chaînage de commandes n'est pas la même chose que leur tubage ; dans le dernier cas, les commandes suivantes commencent à opérer sur les flux de données produits par les précédentes avant qu'elles ne soient terminées, tandis que dans le chaînage, chaque étape se termine avant que la suivante ne commence.

![Capture d'écran avec un exemple de mise de plusieurs commandes sur une seule ligne : cd / ; echo doing ls on / ; ls ; cd $HOME ; echo doing ls on $Home ; ls doing ls on / ](https://courses.edx.org/assets/courseware/v1/60f1cf664b8f4f4e3543445ce02b4c2d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/multcommint.png)
_Mettre plusieurs commandes sur une seule ligne_

### Redirection de sortie

La plupart des systèmes d'exploitation acceptent l'entrée du clavier et affichent la sortie sur le terminal. Cependant, dans les scripts shell, vous pouvez envoyer la sortie vers un fichier. Le processus de détournement de la sortie vers un fichier est appelé redirection de sortie. Nous avons déjà utilisé cette fonctionnalité dans nos sections précédentes sur l'utilisation de la ligne de commande.

Le caractère **>** est utilisé pour écrire la sortie dans un fichier. Par exemple, la commande suivante envoie la sortie de `**free**` vers **/tmp/free.out** :

**$ free > /tmp/free.out**

Pour vérifier le contenu de **/tmp/free.out**, à l'invite de commande tapez **cat /tmp/free.out**.

Deux caractères **>** (**>>**) ajouteront la sortie à un fichier s'il existe, et agiront exactement comme **>** si le fichier n'existe pas déjà.

![Capture d'écran avec un exemple de redirection de sortie : ls /etc/grub.d . /tmp/grubd](https://courses.edx.org/assets/courseware/v1/891c3d95be4e45c6e5c18bc85a7592bc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/outredirectubuntu.png)
_Redirection de sortie_

### Redirection d'entrée

Tout comme la sortie peut être redirigée vers un fichier, l'entrée d'une commande peut être lue à partir d'un fichier. Le processus de lecture de l'entrée à partir d'un fichier est appelé redirection d'entrée et utilise le caractère **<**.

Les trois commandes suivantes (utilisant **wc** pour compter le nombre de lignes, de mots et de caractères dans un fichier) sont entièrement équivalentes et impliquent une redirection d'entrée, et une commande opérant sur le contenu d'un fichier :

**$ wc < /etc/passwd**
**49  105 2678 /etc/passwd**

**$ wc /etc/passwd**
**49  105 2678 /etcpasswd**

**$ cat /etc/passwd | wc**
**49  105 2678**

### Commandes shell intégrées

Les scripts shell exécutent des séquences de commandes et d'autres types d'instructions. Ces commandes peuvent être :

* Des applications compilées
* Des commandes bash intégrées
* Des scripts shell ou des scripts d'autres langages interprétés, tels que perl et Python.

Les applications compilées sont des fichiers exécutables binaires, résidant généralement sur le système de fichiers dans des répertoires bien connus tels que **/usr/bin**. Les scripts shell ont toujours accès à des applications telles que **rm**, **ls**, **df**, **vi** et **gzip**, qui sont des programmes compilés à partir de langages de programmation de bas niveau tels que le C.

De plus, bash possède de nombreuses commandes intégrées, qui ne peuvent être utilisées que pour afficher la sortie dans un shell de terminal ou un script shell. Parfois, ces commandes ont le même nom que des programmes exécutables sur le système, tels que **echo**, ce qui peut entraîner des problèmes subtils. Les commandes intégrées bash incluent **cd**, **pwd**, **echo**, **read**, **logout**, **printf**, **let** et **ulimit**. Ainsi, un comportement légèrement différent peut être attendu de la version intégrée d'une commande telle que **echo** par rapport à **/bin/echo**.

Une liste complète des commandes intégrées bash peut être trouvée dans la page de manuel bash, ou en tapant simplement **help**, comme nous le passons en revue sur la page suivante.

![Commandes shell intégrées : Il existe différents types de commandes - pour les applications compilées, comme rm, ls, df, vi, gzip. Nous avons également des commandes bash intégrées, comme cd, pwd, echo, read, logout, printf, let, ulimit, et des commandes pour d'autres scripts.](https://courses.edx.org/assets/courseware/v1/552b91648741f8ce6769d7859aec989f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_chapter14_screen_15.jpg)
_Commandes shell intégrées_

### Commandes intégrées à bash

Nous avons déjà énuméré quelles commandes ont des versions intégrées à bash, dans notre discussion précédente sur la façon d'obtenir de l'aide sur les systèmes Linux. Encore une fois, voici une capture d'écran listant exactement quelles commandes sont disponibles.

![Capture d'écran listant exactement quelles commandes sont disponibles ; ces commandes peuvent également être récupérées à partir des pages man](https://courses.edx.org/assets/courseware/v1/79040611925a7890d2337fb896445e08/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/helpbash.png)
_Commandes intégrées à bash_

### Paramètres de script

Les utilisateurs ont souvent besoin de passer des valeurs de paramètres à un script, telles qu'un nom de fichier, une date, etc. Les scripts prendront différents chemins ou arriveront à différentes valeurs selon les paramètres (arguments de commande) qui leur sont passés. Ces valeurs peuvent être du texte ou des nombres comme dans :

**$ ./script.sh /tmp**
**$ ./script.sh 100 200**

Dans un script, le paramètre ou un argument est représenté par un **$** et un nombre ou un caractère spécial. Le tableau liste certains de ces paramètres.

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 652px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Paramètre</strong></span></td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Signification</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$0</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Nom du script</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$1</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Premier paramètre</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$2</span></strong>,<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$3</span></strong>, etc.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Deuxième, troisième paramètre, etc.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$*</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Tous les paramètres</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">$#</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Nombre d'arguments</td></tr></tbody></table>

### Utilisation des paramètres de script

Si vous tapez le script montré dans la figure, rendez le script exécutable avec **chmod +x param.sh**. Ensuite, exécutez le script en lui donnant plusieurs arguments, comme indiqué. Le script est traité comme suit :

**$0** imprime le nom du script : **param.sh**

**$1** imprime le premier paramètre : **one**

**$2** imprime le deuxième paramètre : **two**

**$3** imprime le troisième paramètre : **three**

**$*** imprime tous les paramètres : **one two three four five**

L'instruction finale devient : **All done with param.sh**

![Utilisation des paramètres de script. Une capture d'écran de la commande cat param.sh et sa sortie](https://courses.edx.org/assets/courseware/v1/a7d08ff7b0604bb8bd5d324cc162d17f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/scriptparams.png)
_Utilisation des paramètres de script_

### Substitution de commande

Parfois, vous devrez peut-être substituer le résultat d'une commande comme une partie d'une autre commande. Cela peut être fait de deux manières :

* En entourant la commande interne de **$( )**
* En entourant la commande interne de backticks **(**`**)**

La deuxième forme, backticks, est dépréciée dans les nouveaux scripts et commandes. Quelle que soit la méthode utilisée, la commande spécifiée sera exécutée dans un nouvel environnement shell lancé, et la sortie standard du shell sera insérée là où la substitution de commande est effectuée.

Pratiquement n'importe quelle commande peut être exécutée de cette façon. Bien que ces deux méthodes permettent la substitution de commande, la méthode **$( )** permet l'imbrication de commandes. Les nouveaux scripts devraient toujours utiliser cette méthode plus moderne. Par exemple :

**$ ls /lib/modules/$(uname -r)/**

Dans l'exemple ci-dessus, la sortie de la commande **uname –r** (qui sera quelque chose comme **5.13.3**), est insérée dans l'argument de la commande **ls**.

![Substitution de commande : une capture d'écran des commandes fournies dans cette section et leur sortie](https://courses.edx.org/assets/courseware/v1/9d5313940c7ba6bfcf850ccd3cfe7159/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/uname-rhel.png)
_Substitution de commande_

### Variables d'environnement

La plupart des scripts utilisent des variables contenant une valeur, qui peuvent être utilisées n'importe où dans le script. Ces variables peuvent être définies par l'utilisateur ou par le système. De nombreuses applications utilisent de telles variables d'environnement (déjà couvertes en détail dans le chapitre _Environnement utilisateur_) pour fournir des entrées, une validation et contrôler le comportement.

Comme nous l'avons discuté plus tôt, quelques exemples de variables d'environnement standard sont **HOME**, **PATH** et **HOST**. Lorsqu'elles sont référencées, les variables d'environnement doivent être préfixées par le symbole **$**, comme dans **$HOME**. Vous pouvez afficher et définir la valeur des variables d'environnement. Par exemple, la commande suivante affiche la valeur stockée dans la variable **PATH** :

**$ echo $PATH**

Cependant, aucun préfixe n'est requis lors de la définition ou de la modification de la valeur de la variable. Par exemple, la commande suivante définit la valeur de la variable **MYCOLOR** à blue :

**$ MYCOLOR=blue**

Vous pouvez obtenir une liste des variables d'environnement avec les commandes **env**, **set** ou **printenv**.

![Variables d'environnement : une capture d'écran avec différentes variables d'environnement : echo $MY_FAVORITE_OS; MY_FAVORITE_OS=Linux; echo $MY_FAVORITE_OS Linux; env | grep LANG](https://courses.edx.org/assets/courseware/v1/59918633e922e55ffec6d63ac36f6f08/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/envubuntu.png)
_Variables d'environnement_

### Exportation de variables d'environnement

Bien que nous ayons discuté de l'exportation des variables d'environnement dans la section sur l'"_Environnement utilisateur_", il vaut la peine de revoir ce sujet dans le contexte de l'écriture de scripts bash.

Par défaut, les variables créées dans un script ne sont disponibles que pour les étapes suivantes de ce script. Les processus enfants (sous-shells) n'ont pas d'accès automatique aux valeurs de ces variables. Pour les rendre disponibles aux processus enfants, elles doivent être promues en variables d'environnement à l'aide de l'instruction export, comme dans :

**export VAR=value**

ou

**VAR=value ; export VAR**

Bien que les processus enfants soient autorisés à modifier la valeur des variables exportées, le parent ne verra aucun changement ; les variables exportées ne sont pas partagées, elles sont seulement copiées et héritées.

Taper export sans arguments donnera une liste de toutes les variables d'environnement actuellement exportées.

![Exportation de variables : une capture d'écran de export | head -20](https://courses.edx.org/assets/courseware/v1/34717c82ff6e4ce8e5e5dc58c2f2e926/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/exportubuntu.png)
_Exportation de variables_

### Fonctions

Une fonction est un bloc de code qui implémente un ensemble d'opérations. Les fonctions sont utiles pour exécuter des procédures plusieurs fois, peut-être avec des variables d'entrée variables. Les fonctions sont aussi souvent appelées sous-routines. L'utilisation de fonctions dans les scripts nécessite deux étapes :

1. Déclarer une fonction
2. Appeler une fonction

La déclaration de fonction nécessite un nom qui est utilisé pour l'invoquer. La syntaxe correcte est :

**nom_fonction () {**
   **commande...**
**}**

Par exemple, la fonction suivante est nommée **display** :

**display () {**
   **echo "Ceci est une fonction exemple"**
**}**

La fonction peut être aussi longue que souhaité et avoir de nombreuses instructions. Une fois définie, la fonction peut être appelée plus tard autant de fois que nécessaire. Dans l'exemple complet montré dans la figure, nous montrons également un raffinement souvent utilisé : comment passer un argument à la fonction. Le premier argument peut être référencé comme **$1**, le deuxième comme **$2**, etc.

![Fonctions : une capture d'écran de cat testbashfunc.sh et sa sortie ; et de ./testbashfunc.sh et sa sortie](https://courses.edx.org/assets/courseware/v1/f504c2c7131128204c2482cfc4eb4926/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/bashfunubuntu.png)
_Fonctions_

### L'instruction if

La prise de décision conditionnelle, en utilisant une instruction **if**, est une construction de base que tout langage de programmation ou de script utile doit avoir.

Lorsqu'une instruction **if** est utilisée, les actions qui s'ensuivent dépendent de l'évaluation de conditions spécifiées, telles que :

* Comparaisons numériques ou de chaînes
* Valeur de retour d'une commande (0 pour succès)
* Existence ou permissions de fichier

Sous forme compacte, la syntaxe d'une instruction **if** est :

**if TEST-COMMANDS; then CONSEQUENT-COMMANDS; fi**

Une définition plus générale est :

**if condition**
**then**
       **instructions**
**else**
       **instructions**
**fi**

![L'instruction if : une représentation de l'instruction if IF (A=True) Then B Else C End IF](https://courses.edx.org/assets/courseware/v1/8f788761d1ca61e862e140b8942647a5/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/500px-If-Then-Else-diagram.svg.png)
_L'instruction if_

### Utilisation de l'instruction if

Dans l'exemple suivant, une instruction **if** vérifie si un certain fichier existe, et si le fichier est trouvé, elle affiche un message indiquant le succès ou l'échec :

**if [ -f "$1" ]**
**then**
    **echo file "$1 exists"**
**else**
    **echo file "$1" does not exist**
**fi**

Nous devrions vraiment vérifier d'abord qu'il y a un argument passé au script (**$1**) et abandonner sinon.

Remarquez l'utilisation des crochets (**[]**) pour délimiter la condition de test. Il existe de nombreux autres types de tests que vous pouvez effectuer, tels que vérifier si deux nombres sont égaux, supérieurs ou inférieurs l'un à l'autre et prendre une décision en conséquence ; nous discuterons de ces autres tests.

![Panneau montrant deux flèches divergentes](https://courses.edx.org/assets/courseware/v1/fda3ff96ecc163874e0bc6e8ba1dc17b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/49fork1.png)

Dans les scripts modernes, vous pouvez voir des crochets doublés comme dans **[[ -f /etc/passwd ]]**. Ce n'est pas une erreur. Ce n'est jamais faux de le faire et cela évite certains problèmes subtils, tels que faire référence à une variable d'environnement vide sans l'entourer de guillemets doubles ; nous n'en parlerons pas ici.

### L'instruction elif

Vous pouvez utiliser l'instruction **elif** pour effectuer des tests plus compliqués, et prendre les mesures appropriées. La syntaxe de base est :

**if [ sometest ] ; then**
    **echo Passed test1**
**elif [ somothertest ] ; then**
    **echo Passed test2**
**fi**

Dans l'exemple montré, nous utilisons des tests de chaînes que nous expliquerons sous peu, et montrons comment extraire une variable d'environnement avec l'instruction **read**.

![L'instruction elif : une capture d'écran avec un exemple cat ./show_elif.sh](https://courses.edx.org/assets/courseware/v1/4d5cccfd1d279bcb4d7c792561ecc574/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/elif.png)
_L'instruction elif_

### Test de fichiers

bash fournit un ensemble de conditions de fichier, qui peuvent être utilisées avec l'instruction **if**, y compris celles du tableau.

Vous pouvez utiliser l'instruction **if** pour tester les attributs de fichier, tels que :

* Existence de fichier ou de répertoire
* Permission de lecture ou d'écriture
* Permission d'exécution.

Par exemple, dans l'exemple suivant :

**if [ -x /etc/passwd ] ; then**
    **ACTION**
**fi**

l'instruction **if** vérifie si le fichier **/etc/passwd** est exécutable, ce qui n'est pas le cas. Notez la pratique très courante de mettre :

**; then**

sur la même ligne que l'instruction **if**.

Vous pouvez afficher la liste complète des conditions de fichier en tapant :

**man 1 test**.

<table border="1" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Condition</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Signification</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-e file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier existe.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-d file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier est un répertoire.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-f file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier est un fichier régulier (c'est-à-dire pas un lien symbolique, un nœud de périphérique, un répertoire, etc.)</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-s file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier est de taille non nulle.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;;">-g file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier a<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">sgid</span></strong><span>&nbsp;</span>défini.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-u file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier a<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">suid</span></strong><span>&nbsp;</span>défini.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-r file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier est lisible.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-w file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier est inscriptible.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-x file</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Vérifie si le fichier est exécutable.</span></td></tr></tbody></table>

### Expressions booléennes

Les expressions booléennes s'évaluent à VRAI ou FAUX, et les résultats sont obtenus en utilisant les divers opérateurs booléens listés dans le tableau.

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Opérateur</strong></span></td><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Opération</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Signification</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">&amp;&amp;</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">ET</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">L'action ne sera effectuée que si les deux conditions s'évaluent à vrai.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">||</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">OU</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">L'action sera effectuée si l'une des conditions s'évalue à vrai.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">!</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">NON</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">L'action ne sera effectuée que si la condition s'évalue à faux.&nbsp;</td></tr></tbody></table>

Notez que si vous avez plusieurs conditions enchaînées avec l'opérateur **&&**, le traitement s'arrête dès qu'une condition s'évalue à faux. Par exemple, si vous avez **A && B && C** et que A est vrai mais B est faux, C ne sera jamais exécuté.

De même, si vous utilisez l'opérateur **||**, le traitement s'arrête dès que quelque chose est vrai. Par exemple, si vous avez **A || B || C** et que A est faux et B est vrai, vous n'exécuterez jamais C non plus.

### Tests dans les expressions booléennes

Les expressions booléennes renvoient soit VRAI soit FAUX. Nous pouvons utiliser de telles expressions lorsque nous travaillons avec plusieurs types de données, y compris des chaînes ou des nombres, ainsi qu'avec des fichiers. Par exemple, pour vérifier si un fichier existe, utilisez le test conditionnel suivant :

**[ -e <nomfichier> ]**

De même, pour vérifier si la valeur de **number1** est supérieure à la valeur de **number2**, utilisez le test conditionnel suivant :

**[ $number1 -gt $number2 ]**

L'opérateur **-gt** renvoie VRAI si **number1** est supérieur à **number2**.

![Deux cercles, un rouge qui dit Faux et un vert qui dit Vrai](https://courses.edx.org/assets/courseware/v1/682aa174a76a223c71f9f7ee6718192b/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/truefalse.jpg)

### Exemple de test de chaînes

Vous pouvez utiliser l'instruction **if** pour comparer des chaînes en utilisant l'opérateur **==** (deux signes égal). La syntaxe est la suivante :

**if [ string1 == string2 ] ; then**
   **ACTION**
**fi**

Notez que l'utilisation d'un seul signe **=** fonctionnera également, mais certains considèrent cela comme un usage déprécié. Considérons maintenant un exemple de test de chaînes.

Dans l'exemple illustré ici, l'instruction **if** est utilisée pour comparer l'entrée fournie par l'utilisateur et afficher le résultat en conséquence.

![Exemple de test de chaînes : capture d'écran de la commande cat ./testifstring.sh et sa sortie](https://courses.edx.org/assets/courseware/v1/cfe88d1d2fd45ad3e5330dfe36d1b388/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/ifstringubuntu.png)
_Exemple de test de chaînes_

### Tests numériques

Vous pouvez utiliser des opérateurs spécialement définis avec l'instruction **if** pour comparer des nombres. Les différents opérateurs disponibles sont listés dans le tableau :

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 472px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Opérateur</strong></span></td><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Signification</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-eq</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Égal à</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-ne</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Différent de</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-gt</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supérieur à</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-lt</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Inférieur à</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-ge</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Supérieur ou égal à</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">-le</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Inférieur ou égal à</td></tr></tbody></table>

La syntaxe pour comparer des nombres est la suivante :

**exp1 -op exp2**

### Exemple de test de nombres

Considérons maintenant un exemple de comparaison de nombres en utilisant les différents opérateurs :

![Exemple de test de nombres](https://courses.edx.org/assets/courseware/v1/ec0a1d119f27a66c769d359c79c2903c/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/mathtestubuntu.png)
_Exemple de test de nombres_

### Expressions arithmétiques

Les expressions arithmétiques peuvent être évaluées des trois manières suivantes (les espaces sont importants !) :

* Utilisation de l'utilitaire **expr**
**expr** est un programme standard mais quelque peu déprécié. La syntaxe est la suivante :**expr 8 + 8**
**echo $(expr 8 + 8)**
* Utilisation de la syntaxe **$((...))**
C'est le format shell intégré. La syntaxe est la suivante :**echo $((x+1))**
* Utilisation de la commande shell intégrée **let**. La syntaxe est la suivante :**let x=( 1 + 2 ); echo $x**

Dans les scripts shell modernes, l'utilisation de **expr** est mieux remplacée par **var=$((...))**.

![Expressions arithmétiques : capture d'écran avec des exemples déjà fournis dans le texte](https://courses.edx.org/assets/courseware/v1/9dd7a4a63091202085482a6efcbb8e06/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/mathevalrhel7.png)
_Expressions arithmétiques_

## Résumé du chapitre

Vous avez terminé le chapitre 15. Résumons les concepts clés couverts :

* Les scripts sont une séquence d'instructions et de commandes stockées dans un fichier qui peuvent être exécutées par un shell. Le shell le plus couramment utilisé sous Linux est bash.
* La substitution de commande vous permet de substituer le résultat d'une commande comme une partie d'une autre commande.
* Les fonctions ou routines sont un groupe de commandes qui sont utilisées pour l'exécution.
* Les variables d'environnement sont des quantités soit pré-assignées par le shell, soit définies et modifiées par l'utilisateur.
* Pour rendre les variables d'environnement visibles aux processus enfants, elles doivent être exportées**.**
* Les scripts peuvent se comporter différemment en fonction des paramètres (valeurs) qui leur sont passés.
* Le processus d'écriture de la sortie dans un fichier est appelé redirection de sortie.
* Le processus de lecture de l'entrée à partir d'un fichier est appelé redirection d'entrée.
* L'instruction **if** est utilisée pour sélectionner une action basée sur une condition.
* Les expressions arithmétiques se composent de nombres et d'opérateurs arithmétiques, tels que **+**, **-** et *****.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 16 : Plus sur les scripts Shell Bash

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Manipuler des chaînes pour effectuer des actions telles que la comparaison et le tri.
* Utiliser des expressions booléennes lors du travail avec plusieurs types de données, y compris des chaînes ou des nombres, ainsi que des fichiers.
* Utiliser des instructions **case** pour gérer les options de ligne de commande.
* Utiliser des constructions de boucle pour exécuter une ou plusieurs lignes de code de manière répétitive.
* Déboguer des scripts en utilisant set **-x** et set **+x**.
* Créer des fichiers et des répertoires temporaires.
* Créer et utiliser des nombres aléatoires.

### Manipulation de chaînes

Allons plus loin et découvrons comment travailler avec des chaînes dans les scripts.

Une variable chaîne contient une séquence de caractères textuels. Elle peut inclure des lettres, des nombres, des symboles et des signes de ponctuation. Quelques exemples incluent : **abcde**, **123**, **abcde 123**, **abcde-123**, **&acbde=%123**.

Les opérateurs de chaîne incluent ceux qui font la comparaison, le tri et la recherche de la longueur. Le tableau suivant démontre l'utilisation de certains opérateurs de chaîne de base :

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Opérateur</strong></span></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Signification</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[[ string1 &gt; string2 ]]</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compare l'ordre de tri de<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string1</span></strong><span>&nbsp;</span>et<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string2</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">[[ string1 == string2 ]]</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Compare les caractères dans<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string1</span></strong><span>&nbsp;</span>avec les caractères dans<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">string2</strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myLen1=${#string1}</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Enregistre la longueur de<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">string1</span></strong><span>&nbsp;</span>dans la variable<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">myLen1</span></strong>.</td></tr></tbody></table>

### Exemple de manipulation de chaînes

Dans le premier exemple, nous comparons la première chaîne avec la deuxième chaîne et affichons un message approprié en utilisant l'instruction **if**.

![Comparaison de chaînes et utilisation de l'instruction if](https://courses.edx.org/assets/courseware/v1/d42af5098b77f89c8bc2b5a5b5dbc0e9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/stringdemos_horizontal1.png)
_Comparaison de chaînes et utilisation de l'instruction if_

Dans le deuxième exemple, nous passons un nom de fichier et voyons si ce fichier existe dans le répertoire actuel ou non.

![Passage d'un nom de fichier et vérification de son existence dans le répertoire actuel](https://courses.edx.org/assets/courseware/v1/800018a909b1873c8fcd29da8159ecd6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/stringdemos_horizontal2.png)
_Passage d'un nom de fichier et vérification de son existence dans le répertoire actuel_

### Parties d'une chaîne

Parfois, vous n'avez pas besoin de comparer ou d'utiliser une chaîne entière. Pour extraire les **n** premiers caractères d'une chaîne, nous pouvons spécifier : **${string:0:n}**. Ici, **0** est le décalage dans la chaîne (c'est-à-dire à partir de quel caractère commencer) où l'extraction doit commencer et **n** est le nombre de caractères à extraire.

Pour extraire tous les caractères d'une chaîne après un point (**.**), utilisez l'expression suivante : **${string#*.}**.

![Parties d'une chaîne - exemple de capture d'écran](https://courses.edx.org/assets/courseware/v1/55bddf886d7e365fae4c1842a4f0e58d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/stringmanip.png)
_Parties d'une chaîne_

### L'instruction case

L'instruction **case** est utilisée dans des scénarios où la valeur réelle d'une variable peut conduire à différents chemins d'exécution. Les instructions **case** sont souvent utilisées pour gérer les options de ligne de commande.

Voici quelques-uns des avantages de l'utilisation de l'instruction **case** :

* Elle est plus facile à lire et à écrire.
* C'est une bonne alternative aux blocs de code **if-then-else-fi** imbriqués à plusieurs niveaux.
* Elle vous permet de comparer une variable à plusieurs valeurs à la fois.
* Elle réduit la complexité d'un programme.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-106.png)
_Fonctionnalités de l'instruction case_

### Structure de l'instruction case

Voici la structure de base de l'instruction **case** :

**case expression in**
   **pattern1) execute commands;;**
   **pattern2) execute commands;;**
   **pattern3) execute commands;;**
   **pattern4) execute commands;;**
   *** )       execute some default commands or nothing ;;**
**esac**

![Structure de l'instruction case - une représentation graphique de l'exemple fourni dans le texte](https://courses.edx.org/assets/courseware/v1/afb49c3ebe75ff82910621adb09a22c6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch15_screen18.jpg)
_Structure de l'instruction case_

### Exemple d'utilisation de la construction case

Voici un exemple de l'utilisation d'une construction **case**. Notez que vous pouvez avoir plusieurs possibilités pour chaque valeur de cas qui prennent la même action.

![Exemple d'utilisation de la construction case - capture d'écran](https://courses.edx.org/assets/courseware/v1/d8b4e5bc4dec2df7351c100a88cf194a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testcase.png)
_Exemple d'utilisation de la construction case_

### Constructions de boucle

En utilisant des constructions de boucle, vous pouvez exécuter une ou plusieurs lignes de code de manière répétitive, généralement sur une sélection de valeurs de données telles que des fichiers individuels. Généralement, vous faites cela jusqu'à ce qu'un test conditionnel renvoie soit vrai soit faux, selon les besoins.

![Constructions de boucle - une représentation graphique d'une construction de boucle](https://courses.edx.org/assets/courseware/v1/5501cea8fcca399926635852bc90f847/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch15_screen23.jpg)

**Constructions de boucle**

Trois types de boucles sont souvent utilisés dans la plupart des langages de programmation :

* **for**
* **while**
* **until**

Toutes ces boucles sont facilement utilisées pour répéter un ensemble d'instructions jusqu'à ce que la condition de sortie soit vraie.

### La boucle for

La boucle **for** opère sur chaque élément d'une liste d'éléments. La syntaxe de la boucle **for** est :

**for _variable-name_** in _list_
**do**
    **execute one iteration for each item in the **_list_** until the _list_** is finished
**done**

Dans ce cas, **variable-name** et **list** sont substitués par vous selon le cas (voir exemples). Comme avec les autres constructions de boucle, les instructions qui sont répétées doivent être entourées par **do** et **done**.

La capture d'écran ici montre un exemple de la boucle **for** pour imprimer la somme des nombres de 1 à 10.

![La boucle for - capture d'écran](https://courses.edx.org/assets/courseware/v1/038af602fa06b5f5cb01872bd46f2423/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testfor.png)
_La boucle for_

### La boucle while

La boucle **while** répète un ensemble d'instructions tant que la commande de contrôle renvoie vrai. La syntaxe est :

**while condition is true**
**do**
    **Commands for execution**
    **----**
**done**

L'ensemble de commandes qui doivent être répétées doit être entouré entre **do** et **done**. Vous pouvez utiliser n'importe quelle commande ou opérateur comme condition. Souvent, elle est entourée de crochets (**[]**).

La capture d'écran ici montre un exemple de la boucle **while** qui calcule la factorielle d'un nombre. Savez-vous pourquoi le calcul de 21! donne un mauvais résultat ?

![La boucle while](https://courses.edx.org/assets/courseware/v1/8c4861a61a1dc05f846c70efcc38023f/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testwhile.png)
_La boucle while_

### La boucle until

La boucle **until** répète un ensemble d'instructions tant que la commande de contrôle est fausse. Ainsi, c'est essentiellement l'opposé de la boucle **while**. La syntaxe est :

**until condition is false**
**do**
    **Commands for execution**
    **----**
**done**

Similaire à la boucle **while**, l'ensemble de commandes qui doivent être répétées doit être entouré entre **do** et **done**. Vous pouvez utiliser n'importe quelle commande ou opérateur comme condition.

La capture d'écran ici montre un exemple de la boucle **until** qui calcule encore une fois des factorielles ; c'est seulement légèrement différent du cas de test pour la boucle **while**.

![La boucle until](https://courses.edx.org/assets/courseware/v1/3d9d6fd37f62074ecfb72259fd7aff2d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testuntil.png)
_La boucle until_

### Débogage des scripts bash

En travaillant avec des scripts et des commandes, vous pouvez rencontrer des erreurs. Celles-ci peuvent être dues à une erreur dans le script, telle qu'une syntaxe incorrecte, ou d'autres ingrédients, tels qu'un fichier manquant ou une permission insuffisante pour effectuer une opération. Ces erreurs peuvent être signalées avec un code d'erreur spécifique, mais donnent souvent simplement une sortie incorrecte ou confuse. Alors, comment vous y prenez-vous pour identifier et corriger une erreur ?

![Panneau d'avertissement : un point d'exclamation à l'intérieur d'un triangle](https://courses.edx.org/assets/courseware/v1/b166486f15fcdf1d865381b1bac2ebee/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Chapter15_Screen29.jpg)

Le débogage vous aide à dépanner et à résoudre de telles erreurs, et est l'une des tâches les plus importantes qu'un administrateur système effectue.

### Mode débogage de script

Avant de corriger une erreur (ou un bogue), il est vital de connaître sa source.

Vous pouvez exécuter un script bash en mode débogage soit en faisant **bash –x ./script_file**, soit en encadrant des parties du script avec **set -x** et **set +x**. Le mode débogage aide à identifier l'erreur car :

* Il trace et préfixe chaque commande avec le caractère **+**.
* Il affiche chaque commande avant de l'exécuter.
* Il peut déboguer uniquement des parties sélectionnées d'un script (si désiré) avec :

**set -x    # active le débogage**
**...**
**set +x    # désactive le débogage**

La capture d'écran montrée ici démontre un script qui s'exécute en mode débogage s'il est exécuté avec n'importe quel argument sur la ligne de commande.

![Mode débogage de script](https://courses.edx.org/assets/courseware/v1/c79e74ef2465111f5d42ab90f5354816/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/shdebug.png)
_Mode débogage de script_

### Redirection des erreurs vers un fichier et l'écran

Sous UNIX/Linux, tous les programmes qui s'exécutent reçoivent trois flux de fichiers ouverts lorsqu'ils sont démarrés, comme indiqué dans le tableau :

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Flux de fichier<br style="line-height: 1.4em;"></strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Description</strong></span></td><td align="center" bgcolor="#003f60" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Descripteur de fichier</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">stdin</strong></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Entrée standard, par défaut le clavier/terminal pour les programmes exécutés depuis la ligne de commande</td><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">0</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">stdout</strong></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Sortie standard, par défaut l'écran pour les programmes exécutés depuis la ligne de commande</td><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">1</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">stderr</strong></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Erreur standard, où les messages d'erreur de sortie sont affichés ou enregistrés</td><td bgcolor="#e8e8e8" width="20%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">2</td></tr></tbody></table>

En utilisant la redirection, nous pouvons enregistrer les flux de sortie stdout et stderr dans un fichier ou deux fichiers séparés pour une analyse ultérieure après l'exécution d'un programme ou d'une commande.

La capture d'écran montre un script shell avec un bogue simple, qui est ensuite exécuté et la sortie d'erreur est détournée vers **error.log**. L'utilisation de **cat** pour afficher le contenu du journal d'erreurs aide au débogage. Voyez-vous comment corriger le script ?

![Redirection des erreurs vers un fichier et l'écran](https://courses.edx.org/assets/courseware/v1/62739a0082a4076aaac72eba972e9760/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/testbasherr.png)
_Redirection des erreurs vers un fichier et l'écran_

### Création de fichiers et de répertoires temporaires

Considérez une situation où vous souhaitez récupérer 100 enregistrements d'un fichier contenant 10 000 enregistrements. Vous aurez besoin d'un endroit pour stocker les informations extraites, peut-être dans un fichier temporaire, pendant que vous effectuez un traitement supplémentaire dessus.

Les fichiers temporaires (et répertoires) sont destinés à stocker des données pendant une courte période. Généralement, on s'arrange pour que ces fichiers disparaissent lorsque le programme qui les utilise se termine. Bien que vous puissiez également utiliser touch pour créer un fichier temporaire, dans certaines circonstances, cela peut permettre aux pirates d'accéder facilement à vos données. C'est particulièrement vrai si le nom et l'emplacement du fichier temporaire sont prévisibles.

La meilleure pratique est de créer des noms de fichiers aléatoires et imprévisibles pour le stockage temporaire. Une façon de le faire est avec l'utilitaire **mktemp**, comme dans les exemples suivants.

Le **XXXXXXXX** est remplacé par **mktemp** avec des caractères aléatoires pour garantir que le nom du fichier temporaire ne peut pas être facilement prédit et n'est connu qu'au sein de votre programme.

<table width="80%" border="0" height="30" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="50%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td width="30%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour créer un fichier temporaire</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">TEMPDIR=$(mktemp -d /tmp/tempdir.XXXXXXXX)</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour créer un répertoire temporaire</td></tr></tbody></table>

### Exemple de création d'un fichier et d'un répertoire temporaires

La négligence dans la création de fichiers temporaires peut entraîner de réels dommages, soit par accident, soit s'il y a un acteur malveillant. Par exemple, si quelqu'un créait un lien symbolique d'un fichier temporaire connu utilisé par root vers le fichier **/etc/passwd**, comme ceci :

**$ ln -s /etc/passwd /tmp/tempfile**

Il pourrait y avoir un gros problème si un script exécuté par root contient une ligne comme celle-ci :

**echo $VAR > /tmp/tempfile**

Le fichier de mot de passe sera écrasé par le contenu du fichier temporaire.

Pour éviter une telle situation, assurez-vous de randomiser vos noms de fichiers temporaires en remplaçant la ligne ci-dessus par les lignes suivantes :

**TEMP=$(mktemp /tmp/tempfile.XXXXXXXX)**
**echo $VAR > $TEMP**

Notez que la capture d'écran montre des fichiers temporaires nommés de manière similaire à partir de jours différents, mais avec des caractères générés aléatoirement.

![Exemple de création d'un fichier et d'un répertoire temporaires](https://courses.edx.org/assets/courseware/v1/433c4d5c1a0172fe4a8f3e2cabfcf2d9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/tmpfilecentos.png)
_Exemple de création d'un fichier et d'un répertoire temporaires_

### Rejet de la sortie avec /dev/null

Certaines commandes (comme **find**) produiront des quantités volumineuses de sortie, ce qui peut submerger la console. Pour éviter cela, nous pouvons rediriger la grande sortie vers un fichier spécial (un nœud de périphérique) appelé **/dev/null**. Ce pseudo-fichier est également appelé le "bit bucket" (poubelle à bits) ou trou noir.

Toutes les données écrites dessus sont rejetées et les opérations d'écriture ne renvoient jamais de condition d'échec. En utilisant les opérateurs de redirection appropriés, cela peut faire disparaître la sortie des commandes qui généreraient normalement une sortie vers stdout et/ou stderr :

**$ ls -lR /tmp > /dev/null**

Dans la commande ci-dessus, tout le flux de sortie standard est ignoré, mais les erreurs apparaîtront toujours sur la console. Cependant, si l'on fait :

**$ ls -lR /tmp >& /dev/null**

à la fois **stdout** et **stderr** seront déversés dans **/dev/null**.

![Rejet de la sortie avec /dev/null - capture d'écran](https://courses.edx.org/assets/courseware/v1/f36fdbaed019caeb06c7a083c02c723a/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/devnullrhel.png)
_Rejet de la sortie avec /dev/null_

### Nombres et données aléatoires

Il est souvent utile de générer des nombres aléatoires et d'autres données aléatoires lors de l'exécution de tâches telles que :

* Effectuer des tâches liées à la sécurité
* Réinitialiser des périphériques de stockage
* Effacer et/ou masquer des données existantes
* Générer des données sans signification à utiliser pour des tests

De tels nombres aléatoires peuvent être générés en utilisant la variable d'environnement **$RANDOM**, qui est dérivée du générateur de nombres aléatoires intégré au noyau Linux, ou par la fonction de bibliothèque OpenSSL, qui utilise l'algorithme FIPS140 (Federal Information Processing Standard) pour générer des nombres aléatoires pour le chiffrement.

Pour en savoir plus sur FIPS140, lisez l'article _["FIPS 140-2"](https://en.wikipedia.org/wiki/FIPS_140-2)_ de Wikipédia (en anglais).

L'exemple vous montre comment utiliser facilement la méthode de la variable d'environnement pour générer des nombres aléatoires.

![Nombres et données aléatoires : capture d'écran : for n in 1 2 3 4 5 do echo A New Random Number is $RANDOM done](https://courses.edx.org/assets/courseware/v1/bea7e92c667890b6a5ae69110ca423b0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/randomubuntu.png)
_Nombres et données aléatoires_

### Comment le noyau génère des nombres aléatoires

Certains serveurs ont des générateurs de nombres aléatoires matériels qui prennent en entrée différents types de signaux de bruit, tels que le bruit thermique et l'effet photoélectrique. Un transducteur convertit ce bruit en un signal électrique, qui est à nouveau converti en un nombre numérique par un convertisseur A-N. Ce nombre est considéré comme aléatoire. Cependant, la plupart des ordinateurs courants ne contiennent pas un tel matériel spécialisé et, à la place, s'appuient sur des événements créés lors du démarrage pour créer les données brutes nécessaires.

Indépendamment de laquelle de ces deux sources est utilisée, le système maintient un soi-disant pool d'entropie de ces nombres numériques/bits aléatoires. Les nombres aléatoires sont créés à partir de ce pool d'entropie.

Le noyau Linux offre les nœuds de périphérique **/dev/random** et **/dev/urandom**, qui s'appuient sur le pool d'entropie pour fournir des nombres aléatoires qui sont tirés du nombre estimé de bits de bruit dans le pool d'entropie.

**/dev/random** est utilisé là où un caractère aléatoire de très haute qualité est requis, comme la génération de clé ou de masque jetable, mais il est relativement lent pour fournir des valeurs. **/dev/urandom** est plus rapide et approprié (assez bon) pour la plupart des fins cryptographiques.

De plus, lorsque le pool d'entropie est vide, **/dev/random** est bloqué et ne génère aucun nombre jusqu'à ce que du bruit environnemental supplémentaire (trafic réseau, mouvement de la souris, etc.) soit rassemblé, tandis que **/dev/urandom** réutilise le pool interne pour produire plus de bits pseudo-aléatoires.

![Comment le noyau génère des nombres aléatoires : capture d'écran de ls -l /dev/*random](https://courses.edx.org/assets/courseware/v1/0679d15bcba06e9661b627311a08d674/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/devrandom.png)
_Comment le noyau génère des nombres aléatoires_

### Résumé du chapitre

Vous avez terminé le chapitre 16. Résumons les concepts clés couverts :

* Vous pouvez manipuler des chaînes pour effectuer des actions telles que la comparaison, le tri et la recherche de la longueur.
* Vous pouvez utiliser des expressions booléennes lors du travail avec plusieurs types de données, y compris des chaînes ou des nombres, ainsi que des fichiers.
* La sortie d'une expression booléenne est soit vraie soit fausse.
* Les opérateurs utilisés dans les expressions booléennes incluent les opérateurs **&&** (ET), **||** (OU) et **!** (NON).
* Nous avons examiné les avantages de l'utilisation de l'instruction **case** dans des scénarios où la valeur d'une variable peut conduire à différents chemins d'exécution.
* Les méthodes de débogage de script aident à dépanner et à résoudre les erreurs.
* Les sorties standard et d'erreur d'un script ou de commandes shell peuvent facilement être redirigées vers le même fichier ou des fichiers séparés pour aider au débogage et à l'enregistrement des résultats.
* Linux vous permet de créer des fichiers et des répertoires temporaires, qui stockent des données pour une courte durée, économisant à la fois de l'espace et augmentant la sécurité.
* Linux fournit plusieurs façons différentes de générer des nombres aléatoires, qui sont largement utilisés.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## Chapitre 17 : Impression

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez savoir comment :

* Configurer une imprimante sur une machine Linux.
* Imprimer des documents.
* Manipuler des fichiers postscript et PDF à l'aide d'utilitaires en ligne de commande.

### Impression sous Linux

Pour gérer les imprimantes et imprimer directement depuis un ordinateur ou dans un environnement en réseau, vous devez savoir comment configurer et installer une imprimante. L'impression elle-même nécessite un logiciel qui convertit les informations de l'application que vous utilisez en un langage que votre imprimante peut comprendre. La norme Linux pour les logiciels d'impression est le Common UNIX Printing System (CUPS).

![Imprimante](https://courses.edx.org/assets/courseware/v1/514ce391fd913757d030e1f09c150a28/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_03.jpg)

Les systèmes de bureau Linux modernes rendent l'installation et l'administration des imprimantes assez simples et intuitives, et pas très différentes de la façon dont cela se fait sur d'autres systèmes d'exploitation. Néanmoins, il est instructif de comprendre les fondements de la façon dont cela se fait sous Linux.

### Aperçu de CUPS

CUPS est le logiciel sous-jacent que presque tous les systèmes Linux utilisent pour imprimer à partir d'applications comme un navigateur Web ou LibreOffice. Il convertit les descriptions de page produites par votre application (mettre un paragraphe ici, dessiner une ligne là, et ainsi de suite) et envoie ensuite les informations à l'imprimante. Il agit comme un serveur d'impression pour les imprimantes locales et réseau.

Les imprimantes fabriquées par différentes entreprises peuvent utiliser leurs propres langages et formats d'impression particuliers. CUPS utilise un système d'impression modulaire qui s'adapte à une grande variété d'imprimantes et traite également divers formats de données. Cela rend le processus d'impression plus simple ; vous pouvez vous concentrer davantage sur l'impression et moins sur la façon d'imprimer.

![Logo CUPS](https://courses.edx.org/assets/courseware/v1/b8f78f6dba29b1dc4c034cf9d4675136/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/CUPs_Logo.png)

Généralement, la seule fois où vous devriez avoir besoin de configurer votre imprimante est lorsque vous l'utilisez pour la première fois. En fait, CUPS comprend souvent les choses par lui-même en détectant et en configurant toutes les imprimantes qu'il localise.

### Comment fonctionne CUPS ?

CUPS effectue le processus d'impression avec l'aide de ses divers composants :

* Fichiers de configuration
* Planificateur
* Fichiers de travail (Job files)
* Fichiers journaux
* Filtre
* Pilotes d'imprimante
* Backend.

Vous en apprendrez plus sur chacun de ces composants dans les pages suivantes.

![Comment fonctionne CUPS](https://courses.edx.org/assets/courseware/v1/28c1710704f1ec7b7ccd6077c7aa31f4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_05.jpg)
_Comment fonctionne CUPS_

### Planificateur

CUPS est conçu autour d'un planificateur d'impression qui gère les travaux d'impression, gère les commandes administratives, permet aux utilisateurs d'interroger l'état de l'imprimante et gère le flux de données à travers tous les composants CUPS.

![Planificateur](https://courses.edx.org/assets/courseware/v1/1203221f84765ec536df6fdfb185fb41/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_06.jpg)
_Planificateur_

Nous examinerons l'interface basée sur un navigateur qui peut être utilisée avec CUPS, qui vous permet de visualiser et de manipuler l'ordre et l'état des travaux d'impression en attente.

### Fichiers de configuration

Le planificateur d'impression lit les paramètres du serveur à partir de plusieurs fichiers de configuration, dont les deux plus importants sont **cupsd.conf** et **printers.conf**. Ces fichiers et tous les autres fichiers de configuration liés à CUPS sont stockés sous le répertoire **/etc/cups/**.

**cupsd.conf** est l'endroit où se trouvent la plupart des paramètres à l'échelle du système ; il ne contient aucun détail spécifique à l'imprimante. La plupart des paramètres disponibles dans ce fichier concernent la sécurité du réseau, c'est-à-dire quels systèmes peuvent accéder aux capacités réseau de CUPS, comment les imprimantes sont annoncées sur le réseau local, quelles fonctionnalités de gestion sont offertes, et ainsi de suite.

**printers.conf** est l'endroit où vous trouverez les paramètres spécifiques à l'imprimante. Pour chaque imprimante connectée au système, une section correspondante décrit l'état et les capacités de l'imprimante. Ce fichier est généré ou modifié uniquement après l'ajout d'une imprimante au système, et ne doit pas être modifié à la main.

Vous pouvez voir la liste complète des fichiers de configuration en tapant **ls -lF /etc/cups**.

![répertoire /etc/cups/](https://courses.edx.org/assets/courseware/v1/de0cfde1b60578e057bc993ba743d0b4/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/etccupsubuntu.png)
_Répertoire /etc/cups/_

### Fichiers de travail

CUPS stocke les demandes d'impression sous forme de fichiers dans le répertoire **/var/spool/cups** (ceux-ci peuvent en fait être accédés avant qu'un document ne soit envoyé à une imprimante). Les fichiers de données sont préfixés par la lettre **d** tandis que les fichiers de contrôle sont préfixés par la lettre **c**.

![répertoire /var/spool/cups](https://courses.edx.org/assets/courseware/v1/2b1b29c43960fe465f11db866b7038ab/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/varspoolcups.png)
_Répertoire /var/spool/cups_

Après qu'une imprimante a traité avec succès un travail, les fichiers de données sont automatiquement supprimés. Ces fichiers de données appartiennent à ce qui est communément appelé la **file d'attente d'impression**.

![File d'attente d'impression](https://courses.edx.org/assets/courseware/v1/b27d7c01c145f191b20af19557961c06/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_08.jpg)
_File d'attente d'impression_

### Fichiers journaux

Les fichiers journaux sont placés dans **/var/log/cups** et sont utilisés par le planificateur pour enregistrer les activités qui ont eu lieu. Ces fichiers incluent les enregistrements d'accès, d'erreur et de page.

Pour voir quels fichiers journaux existent, tapez :

**$ sudo ls -l /var/log/cups**

![Visualisation des fichiers journaux en utilisant ls -l /var/log/cups](https://courses.edx.org/assets/courseware/v1/42b65f75b623d2abba013731fde26998/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/varlogcups.png)
_Visualisation des fichiers journaux en utilisant ls -l /var/log/cups_

Notez que sur certaines distributions, les permissions sont définies de telle sorte que vous n'avez pas besoin d'utiliser **sudo**. Vous pouvez visualiser les fichiers journaux avec les outils habituels.

![Visualisation des fichiers journaux en utilisant $sudo ls -l /var/log/cups](https://courses.edx.org/assets/courseware/v1/8982f4095d6fedbc55e436c682674f3d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_09.jpg)
_Visualisation des fichiers journaux en utilisant $ sudo ls -l /var/log/cups_

### Filtres, pilotes d'imprimante et backends

CUPS utilise des **filtres** pour convertir les formats de fichiers de travail en formats imprimables. Les **pilotes d'imprimante** contiennent des descriptions pour les imprimantes actuellement connectées et configurées, et sont généralement stockés sous **/etc/cups/ppd/**. Les données d'impression sont ensuite envoyées à l'imprimante via un filtre, et via un **backend** qui aide à localiser les périphériques connectés au système.

![Filtres, pilotes d'imprimante et backends](https://courses.edx.org/assets/courseware/v1/9337f33810fd20eecf2a2eb5a05b51fc/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_screen_10.jpg)
_Filtres, pilotes d'imprimante et backends_

Donc, en bref, lorsque vous exécutez une commande d'impression, le planificateur valide la commande et traite le travail d'impression, créant des fichiers de travail selon les paramètres spécifiés dans les fichiers de configuration. Simultanément, le planificateur enregistre les activités dans les fichiers journaux. Les fichiers de travail sont traités avec l'aide du filtre, du pilote d'imprimante et du backend, puis envoyés à l'imprimante.

### Gestion de CUPS

En supposant que CUPS a été installé, vous devrez démarrer et gérer le démon CUPS pour que CUPS soit prêt pour la configuration d'une imprimante. La gestion du démon CUPS est simple ; toutes les fonctionnalités de gestion peuvent être effectuées avec l'utilitaire **systemctl** :

**$ systemctl status cups**

**$ sudo systemctl [enable|disable] cups**

**$ sudo systemctl [start|stop|restart] cups**

**_NOTE_** _:_ _La_ section suivante _démontre cela sur Ubuntu, mais c'est la même chose pour toutes les grandes distributions Linux actuelles._

### Vidéo : Gestion du démon CUPS

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002100_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Configuration d'une imprimante depuis l'interface graphique

Chaque distribution Linux a une application GUI qui vous permet d'ajouter, de supprimer et de configurer des imprimantes locales ou distantes. En utilisant cette application, vous pouvez facilement configurer le système pour utiliser à la fois des imprimantes locales et réseau. Les écrans suivants montrent comment trouver et utiliser l'application appropriée dans chacune des familles de distribution couvertes dans ce cours.

Lors de la configuration d'une imprimante, assurez-vous que le périphérique est actuellement allumé et connecté au système ; si c'est le cas, il devrait apparaître dans le menu de sélection de l'imprimante. Si l'imprimante n'est pas visible, vous voudrez peut-être dépanner en utilisant des outils qui détermineront si l'imprimante est connectée. Pour les imprimantes USB courantes, par exemple, l'utilitaire **lsusb** affichera une ligne pour l'imprimante. Certains fabricants d'imprimantes exigent également l'installation de logiciels supplémentaires pour rendre l'imprimante visible pour CUPS, cependant, en raison de la standardisation de nos jours, cela est rarement nécessaire.

![Configuration d'une imprimante depuis l'interface graphique](https://courses.edx.org/assets/courseware/v1/e9032460f5217fca7de5f2a6c2250028/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/rh8settings.png)
_Configuration d'une imprimante depuis l'interface graphique_

### Vidéo : Ajout d'une imprimante réseau

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LINILXXX2017-V002600_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Ajout d'imprimantes depuis l'interface Web de CUPS

Un fait que peu de gens connaissent est que CUPS est également livré avec son propre serveur Web, qui rend une interface de configuration disponible via un ensemble de scripts CGI.

Cette interface Web vous permet de :

* Ajouter et supprimer des imprimantes locales/distantes
* Configurer des imprimantes :

– Locales/distantes– Partager une imprimante en tant que serveur CUPS

* Contrôler les travaux d'impression :– Surveiller les travaux

– Afficher les travaux terminés ou en attente– Annuler ou déplacer des travaux.

L'interface Web de CUPS est disponible sur votre navigateur à l'adresse : [http://localhost:631](http://localhost:631/).

Certaines pages nécessitent un nom d'utilisateur et un mot de passe pour effectuer certaines actions, par exemple pour ajouter une imprimante. Pour la plupart des distributions Linux, vous devez utiliser le mot de passe root pour ajouter, modifier ou supprimer des imprimantes ou des classes.

![Capture d'écran du site Web de CUPS](https://courses.edx.org/assets/courseware/v1/1dd8bc3bbcec1fee255a3ff121034328/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/cups_web.png)
_Capture d'écran du site Web de CUPS_

### Impression depuis l'interface graphique

De nombreuses applications graphiques permettent aux utilisateurs d'accéder aux fonctionnalités d'impression en utilisant le raccourci **CTRL-P**. Pour imprimer un fichier, vous devez d'abord spécifier l'imprimante (ou un nom de fichier et un emplacement si vous imprimez dans un fichier à la place) que vous souhaitez utiliser ; puis sélectionnez la mise en page, la qualité et les options de couleur. Après avoir sélectionné les options requises, vous pouvez soumettre le document pour impression. Le document est ensuite soumis à CUPS. Vous pouvez utiliser votre navigateur pour accéder à l'interface Web de CUPS à [http://localhost:631/](http://localhost:631/) pour surveiller l'état du travail d'impression. Maintenant que vous avez configuré l'imprimante, vous pouvez imprimer en utilisant soit l'interface graphique soit l'interface en ligne de commande.

La capture d'écran montre l'interface GUI pour **CTRL-P** pour CentOS, les autres distributions Linux semblent pratiquement identiques.

![Interface GUI pour CTRL-P pour CentOS](https://courses.edx.org/assets/courseware/v1/91be7ab270ff6ac96da0a42409b190fe/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/printingrhel7.png)
_Interface GUI pour CTRL-P pour CentOS_

### Impression depuis l'interface en ligne de commande

CUPS fournit deux interfaces en ligne de commande, descendantes des saveurs System V et BSD d'UNIX. Cela signifie que vous pouvez utiliser soit **lp** (System V) soit **lpr** (BSD) pour imprimer. Vous pouvez utiliser ces commandes pour imprimer du texte, du PostScript, du PDF et des fichiers image.

Ces commandes sont utiles dans les cas où les opérations d'impression doivent être automatisées (à partir de scripts shell, par exemple, qui contiennent plusieurs commandes dans un seul fichier).

**lp** est juste un frontal en ligne de commande pour l'utilitaire **lpr** qui transmet l'entrée à **lpr**. Ainsi, nous ne discuterons que de **lp** en détail. Dans l'exemple montré ici, la tâche est d'imprimer **$HOME/.emacs**.

![Impression depuis l'interface en ligne de commande](https://courses.edx.org/assets/courseware/v1/66b0064f81cd4f18fa50ccd9fde41bf9/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lprhel7.png)
_Impression depuis l'interface en ligne de commande_

### Utilisation de lp

**lp** et **lpr** acceptent des options de ligne de commande qui vous aident à effectuer toutes les opérations que l'interface graphique peut accomplir. **lp** est généralement utilisé avec un nom de fichier comme argument.

Certaines commandes **lp** et autres utilitaires d'impression que vous pouvez utiliser sont listés dans le tableau :

<table border="0" width="60%" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="35%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lp &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour imprimer le fichier sur l'imprimante par défaut</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lp -d printer &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour imprimer sur une imprimante spécifique (utile si plusieurs imprimantes sont disponibles)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">program | lp<br style="line-height: 1.4em;">echo string | lp</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour imprimer la sortie d'un programme</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lp -n number &lt;filename&gt;</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour imprimer plusieurs copies</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpoptions -d printer</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour définir l'imprimante par défaut</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpq -a</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour afficher l'état de la file d'attente</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpadmin</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour configurer les files d'attente d'imprimante</td></tr></tbody></table>

**lpoptions** peut être utilisé pour définir les options et les valeurs par défaut de l'imprimante. Chaque imprimante a un ensemble de balises associées, telles que le nombre de copies par défaut et les exigences d'authentification. Vous pouvez taper **lpoptions help** pour obtenir une liste des options prises en charge. **lpoptions** peut également être utilisé pour définir des valeurs à l'échelle du système, telles que l'imprimante par défaut.

### Vidéo : Impression avec lp

<video controls width="100%" preload="none">

<source src="https://edx-video.net/4cf89569-6b26-4f3e-b8ba-915db0f1a759-mp4_720p.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Gestion des travaux d'impression

Vous envoyez un fichier à l'imprimante partagée. Mais lorsque vous allez là-bas pour récupérer l'impression, vous découvrez qu'un autre utilisateur vient de lancer un travail de 200 pages qui n'est pas sensible au temps. Votre fichier ne peut pas être imprimé tant que ce travail d'impression n'est pas terminé. Que faites-vous maintenant ?

Sous Linux, les commandes de gestion des travaux d'impression en ligne de commande vous permettent de surveiller l'état du travail ainsi que de gérer la liste de toutes les imprimantes et de vérifier leur état, et d'annuler ou de déplacer des travaux d'impression vers une autre imprimante.

Certaines de ces commandes sont listées dans le tableau.

<table border="1" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Commande</span></strong></td><td align="center" bgcolor="#003f60" width="60%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Utilisation</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpstat -p -d</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour obtenir une liste des imprimantes disponibles, ainsi que leur état</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpstat -a</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour vérifier l'état de toutes les imprimantes connectées, y compris les numéros de travail</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">cancel job-id</span></strong><br style="line-height: 1.4em;">OU<br style="line-height: 1.4em;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lprm job-id</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour annuler un travail d'impression</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">lpmove job-id newprinter</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Pour déplacer un travail d'impression vers une nouvelle imprimante</td></tr></tbody></table>

### Travailler avec PostScript et PDF

PostScript est un langage de description de page standard. Il gère efficacement la mise à l'échelle des polices et des graphiques vectoriels pour fournir des impressions de qualité. C'est un format purement textuel qui contient les données fournies à un interpréteur PostScript. Le format lui-même est un langage qui a été développé par Adobe au début des années 1980 pour permettre le transfert de données vers des imprimantes.

![Travailler avec PostScript et PDF](https://courses.edx.org/assets/courseware/v1/0361c9466d73a78da7b4a4846bd6b984/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Ch13_Screen_42.jpg)

**Travailler avec PostScript et PDF**

Les caractéristiques de PostScript sont :

* Il peut être utilisé sur n'importe quelle imprimante compatible PostScript ; c'est-à-dire n'importe quelle imprimante moderne
* Tout programme qui comprend la spécification PostScript peut imprimer vers celui-ci
* Les informations sur l'apparence de la page, etc., sont intégrées dans la page.

Postscript a été en grande partie remplacé par le format PDF (Portable Document Format) qui produit des fichiers beaucoup plus petits dans un format compressé pour lequel le support a été intégré dans de nombreuses applications. Cependant, on doit encore traiter des documents postscript, souvent comme format intermédiaire sur le chemin de la production de documents finaux.

### Travailler avec enscript

**enscript** est un outil utilisé pour convertir un fichier texte en PostScript et d'autres formats. Il prend également en charge le Rich Text Format (RTF) et le HyperText Markup Language (HTML). Par exemple, vous pouvez convertir un fichier texte en PostScript formaté sur deux colonnes (**-2**) en utilisant la commande :

**$ enscript -2 -r -p psfile.ps textfile.txt**

Cette commande fera également pivoter (**-r**) la sortie pour imprimer de sorte que la largeur du papier soit supérieure à la hauteur (alias mode paysage), réduisant ainsi le nombre de pages requises pour l'impression.

Les commandes qui peuvent être utilisées avec **enscript** sont listées dans le tableau ci-dessous (pour un fichier appelé **textfile.txt**).

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="70%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">enscript -p psfile.ps textfile.txt</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertir un fichier texte en PostScript (enregistré dans<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">psfile.ps</span></strong></span>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">enscript -n -p psfile.ps textfile.txt</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertir un fichier texte en n colonnes où n=1-9 (enregistré dans<span>&nbsp;</span><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">psfile.ps</span></strong></span>)</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">enscript textfile.txt</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Imprimer un fichier texte directement sur l'imprimante par défaut</td></tr></tbody></table>

### Conversion entre PostScript et PDF

La plupart des utilisateurs sont aujourd'hui beaucoup plus habitués à travailler avec des fichiers au format PDF, les visualisant facilement soit sur Internet via leur navigateur, soit localement sur leur machine. Le format PostScript est toujours important pour diverses raisons techniques auxquelles l'utilisateur général aura rarement affaire.

De temps en temps, vous devrez peut-être convertir des fichiers d'un format à l'autre, et il existe des utilitaires très simples pour accomplir cette tâche. **ps2pdf** et **pdf2ps** font partie du paquet **ghostscript** installé ou disponible sur toutes les distributions Linux. Comme alternative, il y a **pstopdf** et **pdftops** qui font généralement partie du paquet **poppler**, qui peut devoir être ajouté via votre gestionnaire de paquets. À moins que vous ne fassiez beaucoup de conversions ou que vous ayez besoin de certaines des options plus sophistiquées (que vous pouvez lire dans les pages man de ces utilitaires), peu importe vraiment lesquels vous utilisez.

Une autre possibilité est d'utiliser le très puissant programme **convert**, qui fait partie du paquet **ImageMagick**. Certaines distributions plus récentes l'ont remplacé par Graphics Magick, et la commande à utiliser est **gm convert**.

Quelques exemples d'utilisation :

<table border="0" width="80%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 755.195px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdf2ps file.pdf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertit&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.pdf</span></strong>&nbsp;en<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.ps</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">ps2pdf file.ps</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertit&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.ps</span></strong><span>&nbsp;</span>en<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">file.pdf</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pstopdf input.ps output.pdf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertit&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.ps</span></strong><span>&nbsp;</span>en&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.pdf</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftops input.pdf output.ps</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertit&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.pdf</span></strong><span>&nbsp;</span>en&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.ps</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">convert input.ps output.pdf</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertit&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.ps</span></strong><span>&nbsp;</span>en&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.pdf</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">convert input.pdf output.ps</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Convertit<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">input.pdf</span></strong><span>&nbsp;</span>en&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">output.ps</span></strong></td></tr></tbody></table>

### Visualisation du contenu PDF

Linux dispose de nombreux programmes standard qui peuvent lire les fichiers PDF, ainsi que de nombreuses applications qui peuvent facilement les créer, y compris toutes les suites bureautiques disponibles, telles que LibreOffice.

Les lecteurs PDF Linux les plus courants sont :

1. evince est disponible sur pratiquement toutes les distributions et est le programme le plus largement utilisé.
2. okular est basé sur l'ancien kpdf et est disponible sur toute distribution qui fournit l'environnement KDE.

Ces lecteurs PDF open source prennent en charge et peuvent lire les fichiers suivant la norme PostScript. Le lecteur propriétaire Adobe Acrobat Reader, qui était autrefois largement utilisé sur les systèmes Linux, n'est heureusement plus disponible, car il faisait un rendu défectueux et était instable et mal entretenu.

![Logo Adobe Acrobat Reader, Okular et Evince](https://courses.edx.org/assets/courseware/v1/c727cbca47c30e1108756b2d4152353d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_Screen_46.jpg)

### Manipulation des PDF

Parfois, vous voudrez peut-être fusionner, diviser ou faire pivoter des fichiers PDF ; toutes ces opérations ne peuvent pas être réalisées en utilisant un visualiseur PDF. Certaines de ces opérations incluent :

* Fusionner/diviser/faire pivoter des documents PDF
* Réparer des pages PDF corrompues
* Extraire des pages uniques d'un fichier
* Chiffrer et déchiffrer des fichiers PDF
* Ajouter, mettre à jour et exporter les métadonnées d'un PDF
* Exporter des signets vers un fichier texte
* Remplir des formulaires PDF.

Afin d'accomplir ces tâches, il existe plusieurs programmes disponibles :

* qpdf
* pdftk
* ghostscript.

**qpdf** est largement disponible sur les distributions Linux et est très complet. **pdftk** était autrefois très populaire mais dépend d'un paquet obsolète non maintenu (**libgcj**) et un certain nombre de distributions l'ont abandonné ; nous recommandons donc de l'éviter. **Ghostscript** (souvent invoqué en utilisant **gs**) est largement disponible et bien maintenu. Cependant, son utilisation est un peu complexe.

### Utilisation de qpdf

Vous pouvez accomplir une grande variété de tâches en utilisant **qpdf**, notamment :

<table border="1" width="100%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"></tr></tbody><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="40" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="40" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --empty --pages 1.pdf 2.pdf -- 12.pdf</span></strong></span></td><td bgcolor="#e8e8e8" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Fusionner les deux documents&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>&nbsp;et<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">2.pdf</span></strong>. La sortie sera enregistrée dans&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">12.pdf</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --empty --pages 1.pdf 1-2 -- new.pdf</span></strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Écrire uniquement les pages 1 et 2 de&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>. La sortie sera enregistrée dans&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">new.pdf</span></strong>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --rotate=+90:1 1.pdf 1r.pdf</span></strong></span></p><p style="color: rgb(69, 69, 69); margin: 20px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;"><span style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">qpdf --rotate=+90:1-z 1.pdf 1r-all.pdf</span></strong><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"></span></strong></span></p></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><p style="color: rgb(69, 69, 69); margin: 0px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Faire pivoter la page 1 de&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">1.pdf</strong></span><span>&nbsp;</span>de 90 degrés dans le sens des aiguilles d'une montre et enregistrer dans<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">1r.pdf</strong></span>.</p><p style="color: rgb(69, 69, 69); margin: 20px 0px 1.41575em; text-align: left; font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; line-height: 1.6em !important; font-size: 1em;">Faire pivoter toutes les pages de&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</strong></span><span>&nbsp;</span>de 90 degrés dans le sens des aiguilles d'une montre et enregistrer dans&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">1r-all.pdf</strong></span></p></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span face="courier new, courier" style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">qpdf --encrypt mypw mypw 128 -- public.pdf private.pdf</strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Chiffrer avec 128 bits&nbsp;<span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">public.pdf</strong></span>&nbsp;en utilisant comme mot de passe<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">mypw</strong></span><span>&nbsp;</span>avec la sortie comme<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">private.pdf</strong></span>.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span face="courier new, courier" style="color: rgb(0, 0, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">qpdf --decrypt --password=mypw private.pdf file-decrypted.pdf</strong></span></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;">Déchiffrer<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">private.pdf</strong></span><span>&nbsp;</span>avec la sortie comme<span>&nbsp;</span><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;">file-decrypted.pdf</strong></span>.</td></tr></tbody></table>

![Utilisation de qpdf pour chiffrer/déchiffrer des fichiers](https://courses.edx.org/assets/courseware/v1/8741f9a6b933b1a95e363a20c73d3c77/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/qpdfcrypt.png)
_Utilisation de qpdf pour chiffrer/déchiffrer des fichiers_

### Vidéo : Utilisation de qpdf

<video controls width="100%" preload="none">

<source src="https://edx-video.net/LinuxFoundationXLFS101x-V000400_DTH.mp4">

Désolé, votre navigateur ne supporte pas les vidéos intégrées.
</video>

### Utilisation de pdftk

**pdftk** a maintenant été porté sur Java ! Marc Vinyals a développé et maintenu un portage vers Java pour **pdftk** qui peut être trouvé [ici](https://gitlab.com/pdftk-java/pdftk), avec des instructions pour l'installation. Certaines distributions telles qu'Ubuntu, peuvent installer cette version uniquement.

Vous pouvez accomplir une grande variété de tâches en utilisant **pdftk**, notamment :

<table border="1" width="100%" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px 0px; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"></tr></tbody><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Commande</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Utilisation</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftk 1.pdf 2.pdf cat output 12.pdf</span></strong></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Fusionner les deux documents<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong><span>&nbsp;</span>et<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">2.pdf</span></strong>. La sortie sera enregistrée dans<span>&nbsp;</span><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">12.pdf</span></strong>.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftk A=1.pdf cat A1-2 output new.pdf</span></strong></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Écrire uniquement les pages 1 et 2 de&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>. La sortie sera enregistrée dans&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">new.pdf</span></strong>.</span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">pdftk A=1.pdf cat A1-endright output new.pdfabc</span></strong></td><td bgcolor="#e8e8e8" width="30%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">Faire pivoter toutes les pages de&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">1.pdf</span></strong>&nbsp;de 90 degrés dans le sens des aiguilles d'une montre et enregistrer le résultat dans&nbsp;<strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">new.pdf</span></strong>.</span></td></tr></tbody></table>

### Chiffrement de fichiers PDF avec pdftk

Si vous travaillez avec des fichiers PDF contenant des informations confidentielles et que vous souhaitez vous assurer que seules certaines personnes peuvent visualiser le fichier PDF, vous pouvez lui appliquer un mot de passe en utilisant l'option **user_pw**. On peut le faire en émettant une commande telle que :

**$ pdftk public.pdf output private.pdf user_pw PROMPT**

Lorsque vous exécutez cette commande, vous recevrez une invite pour définir le mot de passe requis, qui peut avoir un maximum de 32 caractères. Un nouveau fichier, **private.pdf**, sera créé avec le contenu identique à **public.pdf**, mais tout le monde devra taper le mot de passe pour pouvoir le visualiser.

![Capture d'écran montrant un fichier PDF chiffré](https://courses.edx.org/assets/courseware/v1/36d90570d210656beea8e67715021db3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/pdfencryptsuse.png)
_Fichier PDF chiffré_

### Utilisation de Ghostscript

Ghostscript est largement disponible en tant qu'interpréteur pour les langages Postscript et PDF. Le programme exécutable qui lui est associé est abrégé en gs.

![Logo Ghostscript](https://courses.edx.org/assets/courseware/v1/6d510a9766cd8587516cf87cf5edf2c1/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/500px-Ghostscript.svg.png)

Cet utilitaire peut faire la plupart des opérations que pdftk peut faire, ainsi que beaucoup d'autres ; voir man gs pour les détails. L'utilisation est quelque peu compliquée par la nature plutôt longue des options. Par exemple :

* Combiner trois fichiers PDF en un seul :

**$ gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite  -sOutputFile=all.pdf file1.pdf file2.pdf file3.pdf**

* Diviser les pages 10 à 20 d'un fichier PDF :

**$ gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dDOPDFMARKS=false -dFirstPage=10 -dLastPage=20\**
**-sOutputFile=split.pdf file.pdf**

### Utilisation d'outils supplémentaires

Vous pouvez utiliser d'autres outils pour travailler avec des fichiers PDF, tels que :

* **pdfinfo**
Il peut extraire des informations sur les fichiers PDF, en particulier lorsque les fichiers sont très volumineux ou lorsqu'une interface graphique n'est pas disponible.
* **flpsed**
Il peut ajouter des données à un document PostScript. Cet outil est spécifiquement utile pour remplir des formulaires ou ajouter de courts commentaires dans le document.
* **pdfmod**
C'est une application simple qui fournit une interface graphique pour modifier des documents PDF. En utilisant cet outil, vous pouvez réorganiser, faire pivoter et supprimer des pages ; exporter des images d'un document ; éditer le titre, le sujet et l'auteur ; ajouter des mots-clés ; et combiner des documents en utilisant l'action glisser-déposer.

Par exemple, pour collecter les détails d'un document, vous pouvez utiliser la commande suivante :

**$ pdfinfo /usr/share/doc/readme.pdf**

![Utilisation d'outils supplémentaires : pdfinfo, flpsed, pdfmod](https://courses.edx.org/assets/courseware/v1/5c4cda1c771ca4c7a29e6bb1d4a3d5ea/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch13_Screen_53.jpg)
_Utilisation d'outils supplémentaires : pdfinfo, flpsed, pdfmod_

## Résumé du chapitre

Vous avez terminé le chapitre 17. Résumons les concepts clés couverts :

* CUPS fournit deux interfaces en ligne de commande : System V et BSD.
* L'interface CUPS est disponible à l'adresse [http://localhost:631](http://localhost:631/).
* **lp** et **lpr** sont utilisés pour soumettre un document à CUPS directement depuis la ligne de commande.
* **lpoptions** peut être utilisé pour définir les options et les valeurs par défaut de l'imprimante.
* PostScript gère efficacement la mise à l'échelle des polices et des graphiques vectoriels pour fournir des impressions de qualité.
* **enscript** est utilisé pour convertir un fichier texte en PostScript et d'autres formats.
* Le format PDF (Portable Document Format) est le format standard utilisé pour échanger des documents tout en garantissant un certain niveau de cohérence dans la façon dont les documents sont visualisés.
* **pdftk** joint et divise les PDF ; extrait des pages uniques d'un fichier ; chiffre et déchiffre des fichiers PDF ; ajoute, met à jour et exporte les métadonnées d'un PDF ; exporte des signets vers un fichier texte ; ajoute ou supprime des pièces jointes à un PDF ; répare un PDF endommagé ; et remplit des formulaires PDF.
* **pdfinfo** peut extraire des informations sur les documents PDF.
* **flpsed** peut ajouter des données à un document PostScript.
* **pdfmod** est une application simple avec une interface graphique que vous pouvez utiliser pour modifier des documents PDF.

![Tux le pingouin portant la coiffe académique carrée](https://courses.edx.org/assets/courseware/v1/284ae82f181c716d860820c08e880813/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_Summary.jpg)

## DEUXIÈME PARTIE

Cet article comporte une deuxième partie. Nous n'avons pas pu tout faire tenir dans un seul article.

Lisez la deuxième partie ici : [https://www.freecodecamp.org/news/introduction-to-linux-part-2/](https://www.freecodecamp.org/french/news/introduction-a-linux-partie-2/)