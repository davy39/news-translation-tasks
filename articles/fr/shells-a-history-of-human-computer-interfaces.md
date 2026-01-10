---
title: Interfaces en Ligne de Commande (CLI) – Une Brève Histoire des Interfaces Homme-Machine
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2023-07-18T16:45:23.000Z'
originalURL: https://freecodecamp.org/news/shells-a-history-of-human-computer-interfaces
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Evernote-cli-geeknote.png
tags:
- name: cli
  slug: cli
- name: command line
  slug: command-line
- name: Computer Science
  slug: computer-science
- name: shell
  slug: shell
seo_title: Interfaces en Ligne de Commande (CLI) – Une Brève Histoire des Interfaces
  Homme-Machine
seo_desc: 'By Chidiadi Anyanwu

  A computer is basically a piece of electronic circuitry that performs tasks as instructed
  by its users.

  But for a human to interact with this hardware, they must really know and understand
  how it works. The person must also know t...'
---

Par Chidiadi Anyanwu

Un ordinateur est fondamentalement un circuit électronique qui exécute des tâches selon les instructions de ses utilisateurs.

Mais pour qu'un humain interagisse avec ce matériel, il doit vraiment connaître et comprendre son fonctionnement. La personne doit également connaître l'ordre dans lequel donner à l'ordinateur diverses tâches pour produire un résultat significatif.

Mais la plupart d'entre nous ne connaissent pas ces choses. Que s'est-il passé ?

Dans cet article, nous allons examiner :

* L'histoire des débuts de l'informatique

* Comment les systèmes d'exploitation ont été développés

* Les systèmes d'exploitation modernes

* Le développement des noyaux et des shells

* L'histoire des shells

* Pourquoi les outils CLI sont toujours importants

## Les Débuts de l'Informatique

Dans les années 1800, les ordinateurs étaient principalement utilisés pour traiter de grandes quantités de données numériques. Ils étaient essentiellement des calculatrices programmables de la taille de petites usines.

Les données qu'ils traitaient étaient également très physiques. Elles étaient alimentées manuellement sous forme de cartes perforées dans les lecteurs de cartes de la machine. Les ordinateurs étaient ensuite programmés en réorganisant physiquement les câbles, les panneaux de connexion et les interrupteurs pour déterminer quelles opérations seraient effectuées sur les données d'entrée. Certains ordinateurs traitaient même la logique par des moyens partiellement mécaniques.

Les panneaux de connexion permettaient d'écrire (ou de câbler) un programme et de le stocker afin que, lorsque vous aviez besoin de ce programme, vous retiriez le panneau de connexion actuel et en installiez un nouveau. Les résultats des programmes étaient imprimés par des imprimantes ligne par ligne, enregistrés sur des bandes ou perforés sur des cartes.

Ces technologies de programmation et de mémoire ont été utilisées dans de nombreuses formes de conceptions technologiques.

Par exemple, la machine Enigma, utilisée pour brouiller les lettres et chiffrer les communications militaires et diplomatiques top secrètes, avait un panneau de connexion que vous deviez recâbler pour changer les paramètres.

L'IBM International Daily Dial Attendance Recorder comptait et enregistrait également la présence du personnel sur des cartes perforées. Il s'agissait d'équipements plus spécialisés.

## Les Premiers Systèmes d'Exploitation

La première synthèse vocale a été réalisée en 1962 sur un IBM 704, un ordinateur sans système d'exploitation.

À l'époque des premiers ordinateurs, personne ne pensait aux systèmes d'exploitation. Les gens écrivaient leurs programmes en langage machine (ou les câblaient sur des panneaux de connexion) et les exécutaient. Il n'y avait aucun moyen d'exécuter deux programmes en même temps ou de détecter/corriger des erreurs. Votre programme s'exécutait jusqu'à ce qu'il plante ou se termine.

![Photo d'un homme et d'une femme utilisant l'IBM 704 en 1957.](https://www.freecodecamp.org/news/content/images/2023/07/IBM_Electronic_Data_Processing_Machine_-_GPN-2000-001881-IBM-704.jpg align="left")

*Ordinateur IBM 704 avec deux opérateurs en 1957*

Initialement, les ordinateurs n'étaient livrés avec aucun logiciel. Plus tard, IBM a inclus des compilateurs FORTRAN et COBOL dans ses mainframes. Puis sont venus les "moniteurs résidents", les précurseurs des systèmes d'exploitation. Ils portaient littéralement ce nom car ils étaient des logiciels qui résidaient dans la mémoire de l'entreprise et surveillaient les tâches. Ils exécutaient essentiellement des tâches comme le nettoyage après les programmes et aidaient à séquencer les travaux sur les ordinateurs.

Les premiers systèmes d'exploitation ont été créés par les propriétaires d'ordinateurs qui en avaient assez de sous-utiliser leurs machines. Ils ne voulaient pas avoir à attendre qu'un programme se termine avant de charger manuellement un autre ensemble de données et de programmes.

L'un de ces premiers systèmes d'exploitation était le système Input/Output de General Motors et North American Aviation (GM-NAA I/O). Son objectif principal était d'exécuter automatiquement le programme suivant après la fin du programme actuel (traitement par lots). Il a été créé en 1956 et est connu comme le premier système d'exploitation fonctionnel.

IBM a ensuite modifié le système d'exploitation de l'un de ses clients et l'a distribué sous le nom d'IBSYS. Ensuite, IBM a pensé qu'il n'était pas bon que différents ordinateurs aient différents ensembles d'instructions (en langage machine), alors ils ont arrêté toute la production et ont lancé une nouvelle ligne appelée System/360.

Avec cela, ils visaient à construire un seul système d'exploitation pour tous leurs ordinateurs. Cela ne s'est pas tout à fait passé comme prévu, alors ils ont fini avec une famille de systèmes d'exploitation, OS/360.

OS/360 incluait des fonctionnalités comme le partage de temps, la détection/correction d'erreurs et la gestion des périphériques, qui sont toutes des fonctionnalités implémentées dans les systèmes d'exploitation modernes. OS/360 a été introduit en 1964 et a été utilisé jusqu'en 1977.

Les premières technologies de partage de temps ont permis à plusieurs personnes d'accéder au même mainframe depuis leurs différents terminaux en même temps. Les premiers terminaux informatiques étaient des télétypes (ou teletypes). Les télétypes ont été développés autour des années 1830 mais n'ont pas été utilisés comme terminaux informatiques avant les années 1970.

## Les Systèmes d'Exploitation Modernes

Le système d'exploitation MULTiplexed Information and Computing Service (MULTICS) a été initialement développé pour le mainframe 645 de General Electric, puis pour les mainframes de Honeywell lorsqu'ils ont racheté la division informatique de GE.

Il a été développé conjointement en 1964 par GE, MIT et Bell Labs, principalement comme successeur du Compatible Time-Sharing System (CTSS).

Il a introduit de nombreuses nouvelles idées dans le monde de l'informatique comme le contrôle d'accès, le lien dynamique, le support de l'ASCII et la reconfiguration dynamique.

La reconfiguration dynamique permettait aux opérateurs de retirer et d'ajouter des mémoires et des CPU sans se déconnecter ou perturber les utilisateurs. Avec l'avènement du Compatible Time-Sharing System (CTSS), les ordinateurs étaient considérés comme une utilité.

L'idée était que les ordinateurs étaient trop grands et trop chers et ne pouvaient être utilisés que par une seule personne à la fois. Mais que se passerait-il si ce matériel coûteux pouvait être utilisé plus efficacement en permettant à plus d'une personne de les utiliser en même temps ? Ainsi, l'ordinateur pourrait devenir une utilité publique, accessible depuis chez soi avec des terminaux.

Avec une utilité publique, vous devez pouvoir effectuer des opérations de maintenance sur différents composants sans perturber le service. C'était l'utilité de la reconfiguration dynamique.

Cette idée que les ordinateurs deviennent une utilité publique semble avoir perduré avec l'utilisation de serveurs, et maintenant, le cloud computing.

À un moment donné, MULTICS n'a pas fonctionné et les entreprises sont parties chacune de leur côté. Ken Thompson, l'un des programmeurs, a ensuite décrit MULTICS comme "surdimensionné", "surchargé" et presque inutilisable. Dans une interview avec Peter Seibel, il a déclaré que les choses qu'il aimait assez pour les reprendre étaient le système de fichiers hiérarchique et le shell.

Il a ensuite créé le système d'exploitation UNIX avec Dennis Ritchie.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Timeline-Computers.png align="left")

## Le Développement des Noyaux et des Shells

L'une des principales caractéristiques du système d'exploitation UNIX était la séparation du système d'exploitation en shell et noyau. Le noyau du système d'exploitation était alors chargé de gérer tous les appels système, tandis que le shell était utilisé pour accéder aux services du système sans exposer le fonctionnement interne du système d'exploitation.

Ce concept a été introduit pour la première fois par le scientifique informatique français Louis Pouzin en 1965. Il a également inventé le terme shell. Voici comment il l'a décrit dans un document intitulé, [The SHELL: A Global Tool for Calling and Chaining Procedures in the System](https://people.csail.mit.edu/saltzer/Multics/Multics-Documents/MDN/MDN-4.pdf).

> Nous pouvons envisager une procédure commune appelée automatiquement par le superviseur chaque fois qu'un utilisateur tape un message sur sa console... nous appellerons cette procédure le "SHELL".

![Définition du Document Shell de Louis Pouzin](https://www.freecodecamp.org/news/content/images/2023/07/Louis-Pouzin-Shell-Document-Definition.png align="left")

*Document de Louis Pouzin sur les Shells*

Selon le document, lorsque l'utilisateur tape une commande, le superviseur initie une nouvelle pile pour sauvegarder la commande, puis appelle le shell avec la commande comme argument.

Il a également envisagé un avenir où les gens créaient leurs propres shells et les utilisaient sans avoir à manipuler la structure sous-jacente du shell.

> "Une fonctionnalité importante est que le SHELL, étant lui-même une procédure commune, peut être remplacé par une procédure privée fournie par l'utilisateur. De cette manière, non seulement une procédure particulière peut être remplacée au choix de l'utilisateur, mais toutes les conventions concernant la frappe des commandes peuvent être sur mesure selon les souhaits de l'utilisateur simplement en fournissant son propre SHELL."

Cette idée a été mise en œuvre pour la première fois dans MULTICS, et est l'une des seules choses que Ken Thompson a admis aimer assez pour reprendre du projet.

Maintenant, dans les systèmes d'exploitation modernes, le shell est le logiciel qui vous permet de communiquer avec le système d'exploitation et d'accéder aux services du système d'exploitation, qui sont des choses comme l'exécution de programmes, la gestion de fichiers et la gestion des entrées/sorties. Il peut s'agir d'un shell en ligne de commande (CLI) ou d'une interface graphique (GUI).

Le noyau est la partie qui gère tous les appels système, gère les ressources de l'ordinateur comme la mémoire, le CPU et le stockage, et gère le partage de temps entre les processus.

## Histoire des Shells CLI

Les shells tels que nous les connaissons aujourd'hui ont vraiment commencé avec UNIX, et l'un des premiers était le Thompson shell.

### Thompson Shell (1971)

Ken Thompson, bien sûr, a créé son propre shell. Il s'agissait d'un simple interpréteur de commandes, non conçu pour le scripting. Il a introduit les symboles < > pour rediriger l'entrée ou la sortie d'une commande, et le symbole | pour le piping.

### C Shell (1978)

Le C Shell (ou csh) a été créé par Bill Joy et a permis le scripting. L'objectif était de créer un langage de commande qui ressemble davantage au langage de programmation C.

### Bourne Shell (1979)

Stephen Bourne a commencé à travailler sur le Bourne Shell en 1976 en tant que remplacement du Thompson Shell. Il était destiné à être un langage de scripting. L'un des principaux objectifs était de permettre l'utilisation de scripts comme filtres.

### Korn Shell (1983)

Développé par David Korn, le Korn Shell était basé sur le code source du Bourne Shell et tentait d'intégrer les fonctionnalités du C Shell et du Bourne Shell. Il est conforme à [POSIX.2](https://en.wikipedia.org/wiki/POSIX).

### Bourne Again SHell aka BASH (1989)

BASH a été écrit par Brian Fox en 1989 et publié sous licence GNU en tant que version libre et open-source du Bourne Shell.

C'était l'un des premiers programmes que Linus Torvalds a portés sur Linux et c'est le shell par défaut pour la plupart des distributions Linux. Il a été conçu pour le scripting et est conforme à [POSIX](https://en.wikipedia.org/wiki/POSIX).

### Z Shell (1990)

Le Z Shell (ou Zsh) a été créé par Paul Falstad comme une extension et une amélioration du Bourne Shell. Le nom a été dérivé du nom d'un assistant d'enseignement à l'université de Paul nommé Zhong Shao.

Il permet également le scripting et est esthétiquement supérieur à Bash. Il supporte les plugins et les extensions, la complétion automatique et certaines autres capacités de globing qui ne sont pas disponibles dans Bash.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Timeline-Shells-1.png align="left")

Il existe de nombreux autres shells populaires utilisés aujourd'hui, mais je ne vais pas en parler.

Tous ces shells mentionnés ne s'appliquaient pas à Windows (jusqu'à récemment). Windows avait deux shells en ligne de commande : l'invite de commandes (cmd) et PowerShell. PowerShell a été créé comme une extension de l'invite de commandes. Il supporte les cmdlets, le scripting, le piping et bien d'autres fonctionnalités.

Ensuite, en 2019, cela a changé avec Windows Terminal, un nouvel émulateur de terminal pour Windows qui peut exécuter Bash sur ce qu'on appelle le sous-système Windows pour Linux (WSL). Il supporte également l'invite de commandes, PowerShell et Azure Cloud shell dès la sortie de la boîte.

## Pourquoi Ces Outils CLI Sont-Ils Importants Alors Que Nous Avons des Interfaces Graphiques (GUI) ?

Vous vous demandez peut-être pourquoi nous prendrions la peine de passer par toute cette évolution et aimerions encore utiliser des outils CLI et des shells. Qu'y a-t-il d'aussi intéressant à taper des commandes dans des terminaux ?

La première et la plus convaincante raison est que les outils CLI sont légers car ils sont basés sur du texte. Dans les cas où vous avez des serveurs et d'autres appareils où vous devez optimiser l'utilisation des ressources, il n'est pas très judicieux d'utiliser la plupart des ressources pour exécuter des interfaces GUI.

L'utilisation de la CLI peut également vous offrir une grande flexibilité et rapidité que vous n'obtiendrez pas avec une GUI. Par exemple, vous pouvez vouloir rechercher toutes les images dans un dossier contenant 1000 fichiers et les renommer dans un certain ordre. Faire cela avec votre GUI serait long et peut-être frustrant. Avec la CLI, vous pouvez simplement taper quelques commandes.

Les scripts sont une autre fonctionnalité importante. Parfois, il y a des tâches que vous voulez effectuer plusieurs fois et vous ne voulez pas avoir à naviguer dans les menus tout le temps ou même taper des commandes plusieurs fois. Vous pouvez écrire des scripts que vous exécutez pour effectuer automatiquement les tâches de manière répétitive.

Dans les cas où vous devez accéder à des appareils à distance, comme des serveurs web ou des appareils réseau, la CLI est également la méthode la plus privilégiée. De plus, pour certaines tâches, il est simplement plus facile de les faire avec quelques commandes que d'utiliser votre GUI—par exemple, mettre à jour vos applications sur Linux.

## Conclusion

Nous avons vraiment parcouru un long chemin depuis les ordinateurs purement mécaniques jusqu'aux ordinateurs purement électroniques. La manière dont nous interagissons avec les ordinateurs a changé au fil des décennies, mais les interfaces en ligne de commande ne sont pas près de disparaître.

Merci d'avoir lu. J'espère que vous avez apprécié cet article. Vous pouvez [me contacter sur LinkedIn.](https://www.linkedin.com/in/chidiadi-anyanwu)