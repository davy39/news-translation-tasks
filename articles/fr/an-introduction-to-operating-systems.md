---
title: Windows vs MacOS vs Linux – Manuel des systèmes d'exploitation
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-04-12T20:14:34.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-operating-systems
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/artiom-vallat-mx9axbKqKW8-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Computer Science
  slug: computer-science
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: software development
  slug: software-development
- name: Windows
  slug: windows
seo_title: Windows vs MacOS vs Linux – Manuel des systèmes d'exploitation
seo_desc: 'Hi everyone! In this handbook I''m going to give a brief introduction to
  operating systems and compare the three main OSs that are out there nowadays.

  First we''re going to review what an OS is and little history about them. Then,
  we''ll review the main...'
---

Bonjour à tous ! Dans ce manuel, je vais donner une brève introduction aux systèmes d'exploitation et comparer les trois principaux systèmes d'exploitation disponibles aujourd'hui.

Tout d'abord, nous allons passer en revue ce qu'est un système d'exploitation et un peu d'histoire à leur sujet. Ensuite, nous passerons en revue les principales caractéristiques et différences des systèmes d'exploitation les plus populaires (Windows, Mac et GNU/Linux).

L'idée ici est d'explorer leur histoire, comment et par qui ils ont été développés, leurs modèles économiques, ainsi que leurs avantages et inconvénients. Cela vous donnera une meilleure idée de leur fonctionnement et de celui à choisir.

Je vais partager des faits ainsi que mes opinions personnelles sur ce sujet. Gardez à l'esprit que certaines des choses que je mentionne ici seront basées sur ma propre expérience et mon analyse du sujet.

Je vais également fournir de nombreux articles/vidéos supplémentaires que vous pouvez consulter si vous souhaitez approfondir un sujet particulier.

Sans plus attendre, c'est parti !

## Table des matières

* [Qu'est-ce qu'un système d'exploitation ?](#heading-questce-quun-systeme-dexploitation)
    
* [Un peu d'histoire des systèmes d'exploitation](#heading-un-peu-dhistoire-des-systemes-dexploitation)
    
* [Les trois principaux systèmes d'exploitation](#heading-les-trois-principaux-systemes-dexploitation)
    
    * [Système d'exploitation Windows](#heading-systeme-dexploitation-windows)
        
    * [MacOS](#heading-macos)
        
    * [GNU/Linux](#heading-gnulinux)
        
        * [Debian](#heading-debian)
            
        * [Ubuntu](#heading-ubuntu)
            
        * [Mint](#heading-mint)
            
        * [Fedora](#heading-fedora)
            
        * [Red Hat Enterprise Linux](#heading-red-hat-enterprise-linux)
            
        * [Arch Linux](#heading-arch-linux)
            
* [Windows vs Mac vs Linux – Comparaison des systèmes d'exploitation](#heading-windows-vs-mac-vs-linux-comparaison-des-systemes-dexploitation)
    
    * [Systèmes de fichiers](#heading-systemes-de-fichiers)
        
    * [Shells](#heading-shells)
        
    * [Gestionnaires de paquets](#heading-gestionnaires-de-paquets)
        
    * [Coût](#heading-cout)
        
    * [Compatibilité logicielle](#heading-compatibilite-logicielle)
        
    * [Qualité et compatibilité du matériel](#heading-qualite-et-compatibilite-du-materiel)
        
    * [Facilité d'utilisation](#heading-facilite-dutilisation)
        
    * [Sécurité et stabilité](#heading-securite-et-stabilite)
        
    * [Communauté et culture](#heading-communaute-et-culture)
        
* [Quel système d'exploitation choisir](#heading-quel-systeme-dexploitation-choisir)
    

## Qu'est-ce qu'un système d'exploitation ?

Selon [Wikipedia](https://en.wikipedia.org/wiki/Operating_system#Examples),

> "Un système d'exploitation (OS) est un système logiciel qui gère le matériel informatique, les ressources logicielles et fournit des services communs pour les programmes informatiques".

Vous pouvez penser à un système d'exploitation comme un programme "intermédiaire" qui se situe entre votre ordinateur et tous les autres programmes que vous exécutez dessus. Il gérera des tâches de base cruciales telles que la gestion des fichiers, la gestion de la mémoire, la gestion des processus, la gestion des entrées-sorties et le contrôle des périphériques.

Les systèmes d'exploitation ont été créés pour simplifier l'utilisation des ordinateurs. De nos jours, un programme donné peut se concentrer uniquement sur l'exécution de ses fonctionnalités principales et laisser toutes les fonctionnalités de base du système au système d'exploitation. Mais les choses n'ont pas toujours été ainsi...

## Un peu d'histoire des systèmes d'exploitation

![an9zgv0_700b](https://www.freecodecamp.org/news/content/images/2022/04/an9zgv0_700b.jpg align="left")

À l'époque (années 1940-50), les programmes étaient écrits pour fonctionner sur des machines spécifiques. Cela signifie qu'un programme pouvait fonctionner sur un seul modèle d'ordinateur.

Si vous vouliez exécuter le même programme sur un modèle d'ordinateur différent, les programmeurs devaient réécrire tout le programme car le matériel était configuré différemment. Il n'y avait pas de couche d'abstraction entre le programme en cours d'exécution et le matériel réel.

Commentaire : Avez-vous déjà pensé au travail d'un programmeur à cette époque ? Les programmes étaient écrits sur des cartes perforées ! =O Cela me souffle l'esprit chaque fois que j'y pense... C'est incroyable à quel point les choses étaient de bas niveau à cette époque et les progrès que la technologie a accomplis grâce à ces premiers programmeurs.

![837755a86e841b0452e12f0786128e02](https://www.freecodecamp.org/news/content/images/2022/04/837755a86e841b0452e12f0786128e02.png align="left")

Dans les années 1960, des géants de l'industrie comme IBM et AT&T ont commencé à travailler sur des systèmes d'exploitation qui pourraient servir de couche d'abstraction entre le matériel et le logiciel, ce qui simplifierait la mise en œuvre de nouveaux programmes.

Le plus notable de ces projets était [**Unix**](https://wikipedia.org/wiki/Unix), qui était un système d'exploitation développé dans les laboratoires Bell d'AT&T par les développeurs [Ken Thompson](https://wikipedia.org/wiki/Ken_Thompson) (qui travaille actuellement sur le développement du langage de programmation Go) et [Dennis Ritchie](https://wikipedia.org/wiki/Dennis_Ritchie) (qui a également créé le langage de programmation C. Des légendes du codage, oui.).

![ken-thompson-dennis-ritchie-111013](https://www.freecodecamp.org/news/content/images/2022/04/ken-thompson-dennis-ritchie-111013.jpg align="left")

Unix a connu un énorme succès et a inspiré la création de nombreux autres systèmes d'exploitation avec des caractéristiques très similaires. Ceux-ci ont ensuite eu une grande influence sur GNU/Linux et MacOS, que nous allons passer en revue dans un instant.

Dans les années 1980, les performances, l'accessibilité, la taille et le prix des ordinateurs s'étaient améliorés au point que le grand public pouvait les acheter et les utiliser pour des tâches personnelles. Cela a fait passer les systèmes d'exploitation de fonctions spécifiques aux entreprises à un usage général. Et cela nous amène à l'ère moderne...

> Si vous êtes intéressé par une explication plus détaillée de la manière dont les systèmes d'exploitation fonctionnent et de leur histoire, voici [une excellente vidéo](https://www.youtube.com/watch?v=26QPDBe-NB8) à ce sujet. Cette chaîne propose également une série de cours accélérés incroyables sur l'informatique, je la recommande définitivement ! ;)

# Les trois principaux systèmes d'exploitation

De nos jours, lorsqu'on parle d'ordinateurs de bureau/portables personnels, les trois systèmes d'exploitation les plus utilisés sont Microsoft Windows (avec environ 80 % de parts de marché), Apple MacOS (avec environ 15 % de parts de marché) et les systèmes d'exploitation basés sur GNU/Linux (avec environ 3 % de parts de marché).

En ce qui concerne les serveurs, environ 80 % fonctionnent sous GNU/Linux et 20 % sous Windows. Et en parlant des appareils mobiles, environ 75 % fonctionnent sous Android (qui utilise le noyau Linux) et 25 % sous IOs (qui est le système d'exploitation mobile d'Apple).

Nous allons passer brièvement en revue chacun d'eux individuellement et ensuite les comparer tous pour identifier leurs différences.

## Système d'exploitation Windows

![516094c7ed4e0--1-](https://www.freecodecamp.org/news/content/images/2022/04/516094c7ed4e0--1-.jpeg align="left")

L'ancêtre de Windows est [MS-DOS](https://wikipedia.org/wiki/MS-DOS), un système d'exploitation basé sur du texte que Microsoft a sorti en 1981.

MS-DOS a été développé pour être compatible avec les PC IBM et il a connu un grand succès. Mais pour le rendre plus accessible au grand public, il avait besoin d'une interface graphique, et c'est ce que Microsoft a sorti en 1985 avec [Windows](https://wikipedia.org/wiki/Microsoft_Windows) 1.0.

Depuis lors, Windows a sorti de nombreuses versions, comme 95, 98, XP, Vista et ainsi de suite... Et s'est imposé comme le système d'exploitation le plus utilisé au monde.

L'accessibilité de Windows et le fait qu'il soit préinstallé sur la plupart des ordinateurs personnels (grâce à des accords commerciaux) ont fait de ce système d'exploitation le plus populaire à ce jour.

[Voici une vidéo sympa](https://www.youtube.com/watch?v=hAJm6RYTIro) qui résume l'histoire de Windows en seulement 3 minutes.

Et si vous êtes intéressé à en savoir plus sur l'histoire de Microsoft, voici une autre [vidéo sympa à ce sujet](https://www.youtube.com/watch?v=JmtPWvT1vp8).

En ce qui concerne son modèle économique, je dirais que la stratégie de Windows est d'inonder le marché et de rendre son système aussi accessible et facile à utiliser que possible. Leur client cible principal est l'utilisateur général, donc peu d'importance particulière est donnée à la personnalisation, à la sécurité ou à la performance.

Windows est simplement le système d'exploitation par défaut pour la plupart des gens. C'est le premier qu'ils découvrent et il permet à l'utilisateur d'exécuter facilement des tâches quotidiennes (navigation sur Internet, jeux, travail de bureau) sans beaucoup de configuration.

Windows est un logiciel privé, ce qui signifie que son code source n'est pas disponible publiquement. Seule Microsoft y a accès.

Au début, les utilisateurs devaient payer s'ils voulaient acheter une copie du système d'exploitation Windows ou mettre à niveau leur version de Windows. Mais avec leurs dernières versions, Windows a adopté un modèle freemium. Sous ce modèle économique, l'utilisateur peut accéder à la plupart des fonctionnalités du logiciel gratuitement et ne doit payer que pour accéder à des fonctionnalités particulières.

La clé pour comprendre ce changement est de comprendre que Microsoft a un portefeuille d'entreprises extrêmement diversifié (Xbox - dans le gaming, Azure - dans les plateformes cloud, LinkedIn - dans les réseaux sociaux, Bing - dans les moteurs de recherche, GitHub... pour n'en nommer que quelques-uns). En rendant Windows gratuit, ils continuent d'inonder le marché et rendent encore plus facile pour les gens de l'adopter comme système d'exploitation par défaut.

Une autre chose à garder à l'esprit est que Windows affiche des publicités au sein du système d'exploitation. Il peut donc être considéré comme une plateforme publicitaire également.

Encore une autre vidéo sympa expliquant ce changement [ici](https://www.youtube.com/watch?v=AYaRzp--xyk).

Et un exemple bizarre/drôle/un peu effrayant du [style marketing old school de Microsoft](https://www.youtube.com/watch?v=EtuDS0ntaJY).

## MacOS

![How-do-I-plug-a-USB-stick-into-this--2000-Macbook-meme-7242](https://www.freecodecamp.org/news/content/images/2022/04/How-do-I-plug-a-USB-stick-into-this--2000-Macbook-meme-7242.png align="left")

MacOS (précédemment appelé OS X) est une ligne de systèmes d'exploitation créée par Apple. Il est préinstallé sur tous les ordinateurs Macintosh, ou Macs. La première version est sortie en 1984 et c'était le premier système d'exploitation pour ordinateurs personnels à être livré avec une interface graphique intégrée.

MacOS est construit sur un système d'exploitation de type UNIX, c'est pourquoi ce MacOS partage de nombreuses caractéristiques communes avec ceux dérivés de GNU/Linux.

À mon avis, le modèle économique d'Apple est principalement basé sur la différenciation et l'exclusivité. Contrairement à Microsoft, Apple fabrique à la fois le matériel et le logiciel de ses produits, et les logiciels d'Apple ne fonctionnent que sur leurs propres machines.

Apple s'est positionné comme un fabricant haut de gamme sur le marché de la technologie, visant à offrir à ses clients du matériel et des logiciels de haute qualité, pour un prix considérablement plus élevé que la plupart de la concurrence.

L'exclusivité est également promue comme un avantage pour les utilisateurs, vendant l'idée de faire partie d'un groupe sélect de personnes lorsqu'on possède un produit Apple.

Le fait que vous ne puissiez pas exécuter n'importe quel logiciel sur leur matériel, et que vous ne puissiez pas installer leur logiciel ailleurs que sur une machine Mac fait partie de la même idée. Vous devez acheter le package complet si vous voulez faire partie du groupe.

Apple fabrique la plupart de ses logiciels et matériels différemment et souvent incompatibles avec les autres. Contrairement à Microsoft, dont l'idée est de rendre le produit aussi largement disponible et facile à obtenir que possible, Apple vise à rendre ses produits de haute qualité mais chers et incompatibles avec d'autres matériels.

Un autre excellent coup marketing d'Apple a été leur capacité à profiter des personnalités extrêmement charismatiques et influentes de personnes comme [Steve Jobs](https://wikipedia.org/wiki/Steve_Jobs). Ils ont tiré parti de sa position et de sa trajectoire en tant que leader de l'industrie, innovateur et quelque peu "rebelle", pour traduire implicitement ces mêmes valeurs à leurs produits.

Jetez un coup d'œil à ces publicités pour savoir ce que je veux dire :

* [Publicité Think different](https://www.youtube.com/watch?v=5sMBhDv4sik)
    
* [Publicité 1984](https://www.youtube.com/watch?v=VtvjbmoDx-I)
    

Si vous êtes intéressé à en savoir plus sur l'histoire de MacOS, [voici une vidéo à ce sujet](https://www.youtube.com/watch?v=c77lU0Rhq8k).

## GNU/Linux

GNU/Linux est la base de nombreux systèmes d'exploitation open source. Contrairement aux exemples que nous venons de voir, GNU/Linux n'est pas un système d'exploitation complet, mais un ensemble de programmes/utilitaires et un noyau que de nombreux systèmes d'exploitation open source partagent.

Passons en revue chaque partie séparément.

[GNU](https://wikipedia.org/wiki/GNU) est une énorme collection de programmes et d'utilitaires qui a été lancée par [Richard Stallman](https://wikipedia.org/wiki/Richard_Stallman).

![EInHz4EWkAQYthk](https://www.freecodecamp.org/news/content/images/2022/04/EInHz4EWkAQYthk.jpg align="left")

Le projet GNU a été lancé en 1983 avec l'idée de développer un système d'exploitation de type UNIX libre (UNIX était la propriété d'AT&T, il n'était donc pas disponible gratuitement). Stallman a commencé à développer des programmes et des utilitaires nécessaires pour le système d'exploitation, mais une pièce maîtresse manquait – le noyau.

Le [noyau](https://en.wikipedia.org/wiki/Kernel_(operating_system)) est le cœur de tout système d'exploitation. C'est la partie du logiciel qui interagit le plus étroitement avec le matériel et le reste du système d'exploitation repose dessus. Le noyau est responsable des tâches de bas niveau telles que la gestion des disques, la gestion de la mémoire, la gestion des tâches, etc.

En 1991, un étudiant de l'université d'Helsinki nommé [Linus Torvalds](https://es.wikipedia.org/wiki/Linus_Torvalds) a commencé à développer un noyau pour un système d'exploitation de type UNIX.

![linus-torvalds](https://www.freecodecamp.org/news/content/images/2022/04/linus-torvalds.jpg align="left")

Au cours des années suivantes, les deux projets ont commencé à interagir et ont été réunis pour former une base solide que tout système d'exploitation pouvait utiliser.

L'idée clé ici est que les deux projets sont open source et entièrement libres. Cela signifie :

* Chacun est libre d'exécuter le programme, pour n'importe quel usage.
    
* Chacun est libre d'étudier comment le programme fonctionne et de le modifier pour qu'il fasse ce qu'il souhaite.
    
* Chacun est libre de redistribuer des copies du logiciel original.
    
* Chacun est libre de distribuer des copies de versions modifiées du logiciel.
    

Pour mieux comprendre le mouvement du logiciel libre, [écoutez cette conférence TED de Richard](https://www.youtube.com/watch?v=Ag1AKIl_2GM).

Et ensuite, regardez Richard parler espagnol et [chanter une chanson sur le logiciel libre](https://www.youtube.com/watch?v=9sJUDx7iEJw) (vous devez aimer ce gars...).

L'approche que Stallman et Torvalds ont prise dans le développement de GNU/Linux est radicalement différente des exemples que nous avons vus et de ce à quoi l'industrie était habituée jusqu'à ce point.

Rendre GNU/Linux libre n'était pas seulement la bonne chose à faire du point de vue de ses développeurs – c'était aussi un excellent choix du point de vue de la qualité du logiciel. Cela est dû au fait que des milliers de développeurs et d'entreprises à travers le monde choisissent de collaborer gratuitement afin d'améliorer le système.

Certaines des distributions GNU/Linux sont connues pour être les systèmes d'exploitation les plus sécurisés et stables disponibles. Ils sont utilisés dans des sphères clés telles que la banque, la finance, le gouvernement et le militaire.

Une grande partie de cela est grâce au modèle open source derrière GNU/Linux, et au fait que des milliers de personnes à travers le monde sont capables de passer en revue le code, de corriger les bugs et de proposer des améliorations constamment.

Ces deux vidéos de la Linux Foundation expliquent [comment Linux est né](https://www.youtube.com/watch?v=5ocq6_3-nEw) et [comment il fonctionne actuellement](https://www.youtube.com/watch?v=yVpbFMhOAwE).

Comme mentionné, GNU/Linux sert de base à de nombreux autres systèmes d'exploitation. Ces systèmes d'exploitation sont appelés "distributions" ou "distros" dans le monde Linux. Tous ont en commun qu'ils sont basés sur le même noyau et le même ensemble d'utilitaires. Ils peuvent être considérés comme des "saveurs" de Linux.

Il n'y a pas beaucoup de différence entre certaines distros, mais d'autres ont des distinctions qui valent la peine d'être mentionnées. Passons rapidement en revue les distros les plus utilisées afin de mieux comprendre cela :

### Debian

Debian est un système d'exploitation qui ne contient que des logiciels libres et open source. Debian a été lancé en 1993 et continue de prospérer et de sortir de nouvelles versions. Debian est principalement connu pour sa stabilité et sa sécurité, ce qui le rend plus conservateur et "lent" en ce qui concerne les nouvelles versions.

### Ubuntu

Ubuntu est la distribution GNU/Linux la plus largement utilisée. Elle a été créée pour prendre les parties principales de Debian et les améliorer plus rapidement. Elle a également un accent plus marqué sur la convivialité et l'accessibilité, ce qui en fait probablement la meilleure option pour quelqu'un venant d'un environnement Windows ou MacOS.

Ubuntu propose généralement des versions tous les six mois, avec une version LTS (support à long terme) plus stable tous les deux ans. Ubuntu est géré par une entreprise appelée [Canonical](https://canonical.com/).

### Mint

Mint est une distribution construite sur Ubuntu. À l'origine, elle était aimée par beaucoup car elle incluait des codecs multimédias et des logiciels propriétaires que Ubuntu n'incluait pas.

### Fedora

Fedora est une distribution qui se concentre fortement sur les logiciels libres. Fedora est sponsorisée par une entreprise appelée [Red Hat](https://es.wikipedia.org/wiki/Red_Hat), qui est elle-même détenue par [IBM](https://www.ibm.com/).

### Red Hat Enterprise Linux

Red Hat Enterprise Linux est une distribution Linux commerciale gérée par une entreprise appelée Red Hat, qui est cotée au Nasdaq. Le système d'exploitation est principalement utilisé pour les serveurs et les entreprises. Il est basé sur le projet open source Fedora, mais conçu pour être une plateforme stable avec un support à long terme.

Red Hat utilise la loi sur les marques pour empêcher la redistribution du logiciel Red Hat Enterprise Linux. Cependant, le logiciel de base est libre et open source.

### Arch Linux

Arch est probablement la distribution Linux la plus hardcore. Elle est très légère, flexible et minimale. Avec Arch, l'utilisateur est complètement responsable de la configuration du système. Le but d'Arch n'est pas d'être grand public. Elle est destinée aux utilisateurs qui ont une compréhension approfondie du fonctionnement d'un ordinateur et d'un système d'exploitation, ou qui sont au moins intéressés à apprendre.

Vous pouvez en savoir plus sur Arch et sur la manière dont vous pouvez le personnaliser [dans ce manuel approfondi](https://www.freecodecamp.org/news/how-to-install-arch-linux/).

Voici une [excellente vidéo](https://www.youtube.com/watch?v=ShcR4Zfc6Dw) qui résume rapidement l'histoire de GNU/Linux et passe en revue les caractéristiques des principales distributions. Fireship est une autre chaîne géniale que je recommande. ;)

En ce qui concerne le modèle économique de GNU/Linux, ils ne sont pas une entreprise pour commencer. Linux et la Free Software Foundation (l'organisation derrière GNU) sont des ONG qui fonctionnent grâce à des dons.

Linux, par exemple, gagne de l'argent grâce aux adhésions Platinum, Gold, Silver et Individual.

Des entreprises comme Microsoft, Google, Facebook, Cisco, Fujitsu, HPE, Huawei, IBM, Intel, Oracle, Qualcomm et Samsung sont toutes des contributeurs actifs à la Linux Foundation. Cela a du sens pour les entreprises car elles bénéficient toutes des connaissances et de la technologie générées par Linux, et leurs dons peuvent être déductibles des impôts.

En ce qui concerne les distributions, certaines sont entièrement gratuites et maintenues par des bénévoles, tandis que d'autres sont maintenues par des entreprises et sont gratuites pour certains utilisateurs mais commercialisées pour les utilisateurs corporatifs. Un autre modèle économique utilisé est l'utilisation gratuite mais facturée pour le support des utilisateurs corporatifs.

Aujourd'hui, Linux fonctionne sur la plupart des serveurs dans le monde. Il est utilisé sur la plupart des supercalculateurs et également sur la plupart des téléphones portables (comme mentionné ci-dessus, Android utilise le noyau Linux).

Côté ordinateurs de bureau/portables, l'utilisation de Linux n'est pas aussi répandue. Et c'est probablement parce qu'il n'est pas aussi largement disponible par défaut que Windows, et qu'il n'est pas du tout aussi commercialisé que Mac.

De plus, surtout à l'époque, la courbe d'apprentissage nécessaire pour implémenter et utiliser Linux était considérablement plus élevée que pour les deux autres options de systèmes d'exploitation.

Quoi qu'il en soit, cette situation a commencé à changer récemment, car les distributions Linux mettent davantage l'accent sur la convivialité et il est plus facile que jamais d'obtenir des ordinateurs avec des distributions Linux installées par défaut.

## Windows vs Mac vs Linux - Comparaison des systèmes d'exploitation

D'accord, outre l'histoire, le modèle économique, etc., quelles sont les différences réelles pour l'utilisateur en ce qui concerne ces trois systèmes d'exploitation ?

La réponse courte est : pas grand-chose, en fait. Mais passons en revue certaines différences dans la conception, les fonctionnalités et l'expérience utilisateur de ces systèmes d'exploitation, et ensuite je vous donnerai mon opinion à ce sujet.

### Systèmes de fichiers

La manière dont Windows organise les fichiers est différente de celle de Mac et GNU/Linux.

Windows utilise des "lecteurs". Il s'agit généralement d'un lecteur C et D qui stockent tous les fichiers de l'ordinateur, et des lecteurs séparés pour les périphériques externes tels que les CD, les clés USB, etc.

![992219e7-6b1f-4528-93d5-495994b77a5e](https://www.freecodecamp.org/news/content/images/2022/04/992219e7-6b1f-4528-93d5-495994b77a5e.png align="left")

Mac et GNU/Linux ont un système de fichiers similaire qui provient de UNIX. Dans ces systèmes d'exploitation, il n'y a pas de lecteurs – tout dans l'ordinateur est considéré comme un fichier (même les périphériques externes) et tous les fichiers sont organisés dans des répertoires qui descendent d'un répertoire racine unique. La structure des répertoires est formée comme un arbre qui a une racine unique.

Cela ne fait pas nécessairement une grande différence pour l'utilisateur final, mais c'est quelque chose à garder à l'esprit si vous êtes habitué à naviguer dans un type de système de fichiers ou l'autre.

### Shells

GNU/Linux et Mac ont Bash comme shell par défaut, tandis que Windows a son propre shell qui utilise une syntaxe différente.

En tant que développeurs et utilisateurs avides de terminal, apprendre Bash est probablement le meilleur choix, car ces connaissances peuvent être plus facilement traduites à tous les systèmes d'exploitation que le shell Windows. Surtout en tenant compte du fait que GNU/Linux fonctionne sur la plupart des serveurs dans le monde, ce qui est l'une des principales occasions où vous devrez utiliser le terminal pour interagir avec l'ordinateur.

Si vous souhaitez en savoir plus sur les shells et l'utilisation du terminal, j'ai récemment écrit [un article à ce sujet](https://www.freecodecamp.org/news/command-line-for-beginners/).

### Gestionnaires de paquets

Mac et GNU/Linux sont livrés avec des gestionnaires de paquets installés par défaut. Un gestionnaire de paquets est un logiciel qui vous permet d'installer, de mettre à jour et de désinstaller des programmes à partir du terminal, simplement en entrant quelques commandes.

Ils sont super utiles, surtout lorsque vous installez et désinstallez constamment des choses, car il est beaucoup plus efficace d'installer des programmes via des gestionnaires de paquets que manuellement.

Le gestionnaire de paquets de Mac s'appelle [homebrew](https://brew.sh/). Sur GNU/Linux, le gestionnaire de paquets par défaut dépend de la distribution. Par exemple, Ubuntu est livré avec [APT](https://ubuntu.com/server/docs/package-management), Arch est livré avec [Pacman](https://wiki.archlinux.org/title/pacman), et ainsi de suite.

Tous les gestionnaires de paquets fonctionnent de manière similaire, mais il existe certaines différences dans la syntaxe utilisée pour chacun. Il est également important de mentionner que vous pouvez installer et exécuter un gestionnaire de paquets différent de celui par défaut.

Windows n'est pas livré avec un gestionnaire de paquets par défaut. Si vous en voulez un, vous devez d'abord l'installer. L'un des gestionnaires de paquets disponibles pour Windows est [Chocolatey](https://docs.chocolatey.org/en-us/).

### Coût

Comme déjà mentionné, la plupart des distributions GNU/Linux sont entièrement gratuites pour tout le monde. Windows a actuellement un modèle freemium et MacOS ne fonctionne que sur les ordinateurs Mac, qui sont assez chers comme vous le savez.

### Compatibilité logicielle

Windows est le système d'exploitation le plus utilisé, et grâce à cela, la plupart des logiciels sont adaptés à celui-ci. Bien que moins populaire, MacOS est similaire à Windows à cet égard.

À l'époque, Linux n'était pas compatible avec de nombreux programmes disponibles, mais cela a commencé à changer récemment, surtout avec les distributions les plus populaires comme Ubuntu.

### Qualité et compatibilité du matériel

En ce qui concerne le matériel, seule Apple est directement responsable des ordinateurs sur lesquels le système d'exploitation fonctionne. Et le matériel d'Apple est parmi les meilleurs disponibles.

En tant qu'entreprise, Apple se concentre sur la fourniture de produits de haute qualité, donc leurs nouveaux ordinateurs tendent à être ceux avec les meilleures performances sur tout le marché.

Étant donné qu'Apple conçoit et développe à la fois le matériel et le logiciel, il est possible que la compatibilité entre la machine et le système d'exploitation soit plus fine qu'avec Windows ou GNU/Linux.

Du côté de Windows et GNU/Linux, la qualité du matériel dépend entièrement de ce que l'utilisateur décide ou peut se permettre d'acheter. Le bon côté ici est que vous pouvez installer le système d'exploitation où vous le souhaitez.

Cela est particulièrement cool lorsque l'on pense à installer des distributions Linux légères sur des ordinateurs plus anciens qui ne peuvent pas gérer les exigences de systèmes d'exploitation plus grands et plus gourmands comme Windows.

### Facilité d'utilisation

Windows et Mac sont des systèmes d'exploitation vraiment simples et conviviaux. En ce qui concerne GNU/Linux, cela dépend de la distribution que vous choisissez. Comme mentionné, des distributions comme Ubuntu sont pratiquement aussi faciles que Windows ou Mac, et d'autres comme Arch sont destinées aux utilisateurs avancés d'ordinateurs.

### Sécurité et stabilité

Certaines distributions GNU/Linux sont considérées comme les plus sécurisées et stables de nos jours. Le fait que le code soit disponible pour tout le monde n'est pas une menace pour la sécurité comme vous pourriez le penser au premier abord – mais plutôt un avantage. Les bugs peuvent être identifiés et corrigés plus rapidement, et lorsqu'une faille de sécurité est identifiée, de nombreuses personnes peuvent travailler dessus et proposer des correctifs.

Windows, en revanche, est considéré comme le moins sécurisé et stable des trois. Étant donné qu'il s'agit du système d'exploitation le plus populaire, la plupart des logiciels malveillants sont également développés pour attaquer le système d'exploitation Windows.

### Communauté et culture

Si vous êtes intéressé à en savoir plus sur un système d'exploitation particulier, à étudier son fonctionnement, à apprendre à le modifier et à créer des projets basés dessus, GNU/Linux est définitivement la voie à suivre. C'est le seul dont le code est disponible pour tous et sa communauté en ligne est énorme.

Bien que GNU/Linux ne soit pas aussi largement utilisé que les deux autres systèmes d'exploitation, je trouve que les utilisateurs de Linux sont généralement des personnes intéressées par les logiciels et la technologie, et des personnes qui aiment parler, apprendre et partager des connaissances à ce sujet.

Mac a également ses fans et est particulièrement populaire parmi les créatifs (designers graphiques, monteurs vidéo, animateurs, etc.).

Et enfin, Windows est couramment utilisé par l'utilisateur général et dans les environnements corporatifs.

En ce qui concerne la culture organisationnelle, je pense qu'il pourrait être intéressant de la visualiser dans l'environnement de travail des personnes qui ont créé ces systèmes d'exploitation :

* Jetez un coup d'œil au [siège d'Apple](https://www.youtube.com/watch?v=FzcfZyEhOoI)
    
* [Le "bureau à domicile" de Bill Gates](https://www.youtube.com/watch?v=ZjyVjU4gkHM)
    
* Et [le bureau à domicile de Linus Torvalds](https://www.youtube.com/watch?v=jYUZAF3ePFE)
    

> Si vous souhaitez voir une comparaison plus approfondie de ces trois systèmes d'exploitation, Zach Gollwitzer a [une très bonne vidéo sur ce sujet](https://www.youtube.com/watch?v=09puF-VKWeI) (une autre excellente chaîne à suivre ;)).

## Quel système d'exploitation choisir

J'ai eu l'occasion d'utiliser récemment les trois systèmes d'exploitation, et comme je l'ai mentionné, je ne pense pas que les différences entre chacun d'eux soient SI grandes.

À mon avis, Linux est un choix intelligent car il fonctionne très bien, il est largement utilisé dans l'industrie technologique (donc toutes les connaissances peuvent être traduites en environnements de travail), et si vous êtes intéressé à en savoir plus sur son fonctionnement, il y a une énorme communauté qui soutient cela. Et surtout... il est gratuit !

Je veux dire, si nous avons l'un des meilleurs et des plus largement utilisés logiciels de l'histoire de l'humanité à notre portée et entièrement gratuit, pourquoi paierions-nous pour obtenir autre chose ?

En ce qui concerne d'autres questions, je pense que la plupart des choses que vous pouvez faire sur GNU/Linux, vous pouvez aussi les faire sur Mac et Windows, au moins pour la plupart des utilisateurs. Cela ne fera probablement pas une énorme différence dans votre vie quotidienne, au moins de mon point de vue.

En ce qui concerne le matériel, acheter un ordinateur Apple moderne est presque une garantie d'avoir une machine performante (si vous pouvez vous le permettre). Mais si vous connaissez un peu le matériel ou prenez le temps de vous renseigner, vous pouvez facilement trouver de très bons choix aussi pour un prix plus petit.

À la fin, je pense qu'il est important de savoir ce que vous utilisez et de connaître les options disponibles. En tant qu'utilisateurs d'ordinateurs, il est bon d'être conscient des faits et des différences, et d'éviter d'être distrait par les campagnes marketing.

Je ne crois pas non plus qu'il faille accorder trop de jugement ou d'importance à un choix ou à un autre. Le fait que quelqu'un choisisse un système d'exploitation open source ne rend pas cette personne plus intelligente ou supérieure à quelqu'un qui ne le fait pas... Tout comme posséder le dernier ordinateur Mac ne fera pas de vous un meilleur programmeur.

En résumé, peu importe ce que vous choisissez, c'est bien tant que votre système vous permet de faire ce que vous voulez.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [linkedin](https://www.linkedin.com/in/germancocca/) ou [twitter](https://twitter.com/CoccaGerman).

À la vôtre et à la prochaine ! =D

![goodbye](https://www.freecodecamp.org/news/content/images/2022/04/goodbye.gif align="left")