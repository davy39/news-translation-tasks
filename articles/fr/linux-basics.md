---
title: Linux pour les hackers – Les bases pour les débutants en cybersécurité
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2022-09-26T23:20:22.000Z'
originalURL: https://freecodecamp.org/news/linux-basics
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/linux-basics-for-hackers.jpeg
tags:
- name: beginner
  slug: beginner
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: Linux
  slug: linux
seo_title: Linux pour les hackers – Les bases pour les débutants en cybersécurité
seo_desc: 'Time to learn how to use the operating system of the average hacker 🐧.

  In this article, we will take a little tour of:


  The Linux operating system

  Package management

  The Linux file structure

  The Command Line Interface


  And you get to learn how to up...'
---

Il est temps d'apprendre à utiliser le système d'exploitation du hacker moyen 🐧.

Dans cet article, nous allons faire un petit tour d'horizon de :

* Le système d'exploitation Linux
* La gestion des paquets
* La structure des fichiers Linux
* L'interface en ligne de commande (CLI)

Et vous apprendrez également comment mettre à jour votre distro Linux. On y va ? 🙃

## Qu'est-ce que Linux ?

![Hacker Penguins](https://miro.medium.com/max/1400/1*fIYQYmFd0dvGejmrXxzH0Q.jpeg)
_Hacker Penguins | Crédit : Wallpaperflare.com_

Le [kernel](https://www.redhat.com/en/topics/linux/what-is-the-linux-kernel) (noyau) Linux a été créé par Linus Torvalds en 1991. Ce qui en fait un [système d'exploitation](https://www.freecodecamp.org/news/what-is-an-os-operating-system-definition-for-beginners/), ce sont les ajouts au noyau tels qu'un gestionnaire de paquets, un environnement de bureau, un shell et un bootloader, entre autres composants.

Parce que Linux est [open-source](https://www.freecodecamp.org/news/what-is-open-source-software-explained-in-plain-english/), de nombreuses personnalisations ont été apportées au système d'exploitation. Chaque combinaison spécifique de personnalisations est appelée une distribution ou distro en abrégé.

Il existe des centaines, voire des milliers de distros dans le monde. Chacune d'entre elles a été optimisée pour un but spécifique, ou simplement pour le plaisir par des gens comme vous et moi.

Certaines distros célèbres sont :

1. [Ubuntu](https://en.wikipedia.org/wiki/Ubuntu) (La plus courante)
2. [Elementary OS](https://en.wikipedia.org/wiki/Elementary_OS) (L'une des plus belles)
3. [Debian](https://en.wikipedia.org/wiki/Debian) (Propre et classique)
4. [Arch Linux](https://en.wikipedia.org/wiki/Arch_Linux) (Pour les boss de Linux)
5. [Red Hat Enterprise Linux](https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux) (Commerciale et coûteuse 💰)

## Quel est le rapport entre Linux et le hacking ?

![A Guy Fawkes mask on a keyboard](https://miro.medium.com/max/1200/1*2vBHzk9Yxi_Tg_gHW_47IA.jpeg)
_Un masque de Guy Fawkes sur un clavier | Crédit : Wallpaperflare.com_

Linux est le système d'exploitation de choix de nombreux hackers. Pourquoi, me demanderez-vous ? Parce qu'il est open-source, moins sujet aux malwares, léger, portable et très compatible avec de multiples outils de hacking.

Windows est un système quelque peu fermé, il y a donc beaucoup de choses qu'il ne permet pas à un hacker de faire. Mac OS n'est pas non plus idéal en raison de ses nombreux logiciels propriétaires. Linux propose de nombreuses distros et la plupart peuvent être modifiées au gré de l'utilisateur sans aucune restriction.

Un certain nombre de distros couramment utilisées par les hackers sont Kali Linux, Parrot, BlackArch et Archstrike. Mais ne vous arrêtez pas là, les options sont illimitées.

Comme je l'ai mentionné plus tôt, Linux est également hautement personnalisable. Un excellent exemple de cette fonctionnalité est l'environnement de bureau, qui est un nom sophistiqué pour désigner l'apparence du bureau.

Sous Windows, il y a la barre des tâches de base, le menu démarrer et un arrière-plan avec des icônes. C'est bien de pouvoir faire de légères modifications, et le ressenti change avec chaque nouvelle version de Windows, surtout avec Windows 11. Mais les efforts de Microsoft font pâle figure face aux progrès massifs de la communauté Linux en ce qui concerne l'apparence et la convivialité d'un bureau.

Les environnements de bureau courants incluent :

1. [Gnome](https://en.wikipedia.org/wiki/GNOME) (Le meilleur 😎)
2. [KDE Plasma](https://en.wikipedia.org/wiki/KDE) (Un sosie de Windows)
3. [Xfce](https://en.wikipedia.org/wiki/Xfce) (Pour les geeks)
4. [Mate](https://en.wikipedia.org/wiki/MATE_(software)) (Économe en ressources matérielles)

Si vous aimez la programmation, vous pourriez vous baser sur un environnement de bureau actuel publié sous licence GNU ou développer votre propre environnement de bureau pour répondre à vos besoins.

Conseil : Si vous êtes complètement nouveau sur Linux, vous devriez peut-être attendre un peu avant de remplacer votre système d'exploitation par défaut. De nombreux utilisateurs ont l'habitude d'une GUI (Interface Graphique) pour effectuer leurs activités. Mais les utilisateurs de Linux ont tendance à utiliser davantage la CLI (Interface en Ligne de Commande). C'est simplement parce que Linux s'adresse aux développeurs et aux scientifiques, et non à l'utilisateur moyen.

Je suggère personnellement d'installer une distro Linux sur un [hyperviseur](https://www.redhat.com/en/topics/virtualization/what-is-a-hypervisor) tel que VirtualBox, et de vous entraîner à vous y habituer. (Je ne suggère pas VMware car il présente une vulnérabilité connue au moment de la rédaction). Si vous ne savez pas comment installer Linux, vous pouvez l'apprendre [ici](https://www.freecodecamp.org/news/how-to-install-kali-linux/).

## Gestion des paquets Linux

![Colourful Packages](https://miro.medium.com/max/1400/1*72i2_4etooYTxQO3LnFVMw.jpeg)
_Paquets colorés | Crédit : Wallpaperflare.com_

Linux est assez différent des autres systèmes d'exploitation, ce qui signifie que l'installation d'applications l'est aussi. Version courte ? Vous allez télécharger des applications depuis le magasin d'applications de la distro via la CLI (terminal). Passons maintenant à la version longue.

Les installateurs **.exe** et **.msi** (que vous utilisez pour installer des applications sous Windows) ne fonctionnent pas très bien sous Linux. Les gestionnaires d'une distro disposent donc de serveurs qui hébergent de multiples applications optimisées pour cette distro particulière.

Avec quelques commandes de votre part dans le terminal, et l'aide d'un gestionnaire de paquets, votre ordinateur se connecte au serveur, télécharge les applications et les installe. Vous pouvez également obtenir les mises à jour du système de cette manière.

Un gestionnaire de paquets est un logiciel utilisé pour gérer les logiciels téléchargés et installés. Vous avez peut-être entendu parler d'au moins un des gestionnaires de paquets suivants :

1. Apt (Linux)
2. Chocolatey (Windows)
3. MacPorts (MacOS)
4. Pip (Python)
5. Npm (Javascript)
6. Gradle (Java)
7. Composer (PHP)

Certains installateurs .exe et .msi peuvent fonctionner sur des ordinateurs Linux, mais avec un bémol. Un logiciel appelé Wine ajoute une couche de compatibilité Windows à la distro pour l'optimiser pour les applications Windows. Malheureusement, cela ne fonctionne pas pour toutes les applications.

Une autre alternative est d'installer Steam, ou mieux encore, SteamOS si vous êtes un joueur avec un penchant pour Linux 🎮.

## Structure des fichiers Linux

![Folders](https://miro.medium.com/max/1400/1*X3sQ8cTpRXdFw9SlJYVHCg.jpeg)
_Dossiers | Crédit : Wallpaperflare.com_

Le système d'exploitation Linux possède une arborescence de répertoires tout comme Windows. Tout en haut (ou en bas, selon votre perspective), nous avons le dossier « / ». Ce serait comme votre lecteur C: sous Windows. Il abrite tous vos répertoires, fichiers et applications. En dessous se trouvent d'autres dossiers qui sont résumés dans l'image ci-dessous :

![The Linux file structure](https://miro.medium.com/max/1400/1*gwrwO22ml-ZFqRUNT5USuA.png)
_La structure des fichiers Linux | Crédit : Hackers-arise.com_

Quelques répertoires importants à noter :

1. /bin : programmes binaires ou exécutables (un bon endroit pour conserver des scripts persistants)
2. /etc : fichiers de configuration du système (un endroit idéal pour obtenir des identifiants)
3. /home : répertoire personnel (le répertoire actuel par défaut lorsque vous ouvrez le terminal)
4. /opt : logiciels optionnels ou tiers
5. /tmp : espace temporaire, généralement vidé au redémarrage (un excellent endroit pour stocker des scripts d'énumération)
6. /usr : programmes liés à l'utilisateur
7. /var : fichiers de journaux (l'endroit parfait pour frustrer un analyste forensique)

Il y a beaucoup plus à dire sur la structure des fichiers Linux et cela mériterait probablement son propre article, mais cela suffira pour l'instant.

Maintenant, passons à une expérience beaucoup plus pratique dans le terminal et exécutons quelques commandes de base que tout hacker devrait connaître.

## Introduction au Shell Linux

![Image](https://miro.medium.com/max/1400/1*4lQrXCH59QvOWX1-nA--Zg.jpeg)
_Unix et ses divers dérivés | Crédit : Wallpaperflare.com_

Un shell est une interface textuelle permettant de contrôler un ordinateur Linux. Semblable au Powershell ou au cmd de Microsoft, c'est l'interface entre l'utilisateur et le noyau, en dehors de la GUI (Interface Graphique).

Il existe différents types de shells, chacun ayant été amélioré par rapport aux précédents ou optimisé pour un objectif particulier.

Les shells sont beaucoup utilisés par les hackers car ils constituent le moyen le plus rapide et le plus efficace de transmettre des instructions à un ordinateur. La GUI est correcte, mais peut être assez limitée car certaines fonctionnalités ne sont pas accessibles graphiquement, ou l'outil que vous voulez utiliser n'a tout simplement pas d'interface graphique.

Certains shells courants incluent :

1. Le Bourne shell (sh)
2. Le GNU-Bourne Again shell (bash)
3. Le Z shell (zsh)
4. Le C shell (csh)
5. Le Korn shell (ksh)

Petite leçon : Les mots « terminal » et « shell » sont utilisés de manière interchangeable dans le monde de la cybersécurité et tout au long de cet article. Pourtant, ils sont différents. Le terminal est le **programme** qui vous permet d'accéder au shell via une interface graphique.

## Commandes de base du Shell Linux

Dans cet article, nous allons passer en revue les commandes suivantes : `whoami, pwd, ls, cd, touch, cat, nano, operators, mv and cp, mkdir, rm and rmdir, stat, echo, grep,` le drapeau « help » et les pages `man`.

Vous aurez besoin de la distro Linux de votre choix, bien que je suggère Kali. Si vous ne savez pas comment en installer une, vous pouvez [lire cet article](https://www.freecodecamp.org/news/how-to-install-kali-linux/).

Ouvrez l'application appelée « Terminal » et commençons. On continue ? 🙃

### Comment utiliser la commande `whoami` 

Vous utilisez cette commande pour vérifier quel utilisateur vous êtes. Sur un ordinateur personnel, vous n'avez probablement que deux comptes : celui créé lors de l'installation de l'OS et root. Si vous êtes dans le terminal en tant qu'utilisateur normal (compte), vous pouvez l'essayer.

```
whoami
```

![Image](https://miro.medium.com/max/516/1*STvkLP5IE9ElhykvkcxSlw.png)
_whoami | Crédit : Mercury_

Si vous voulez être root, exécutez la commande _sudo su_ et entrez votre mot de passe. Essayez `whoami` et le terminal vous répondra root :

![Image](https://miro.medium.com/max/698/1*5beFT8yRjD6Gvlb91Wfs9A.png)
_whoami en tant que root | Crédit : Mercury_

Les ordinateurs d'entreprise ont tendance à avoir de nombreux utilisateurs sur une seule machine. Comme je l'ai indiqué dans un [article précédent](https://www.freecodecamp.org/news/what-is-hacking/), chacun possède diverses [permissions](https://www.howtogeek.com/school/windows-network-sharing/lesson1/), certaines plus étendues que d'autres. Lorsque vous obtenez un accès initial après l'exploitation, vous commencez généralement avec un compte standard. Si vous voulez vérifier le nom du compte compromis, utilisez cette commande.

### Comment utiliser la commande `pwd` 

La commande Present Working Directory (`pwd`) vous informe de l'endroit où vous vous trouvez actuellement dans l'arborescence des répertoires. Par défaut, il s'agit généralement du répertoire personnel.

```
pwd
```

![Image](https://miro.medium.com/max/554/1*1amzxhqu8TEM5-Qdkbv8ew.png)
_Répertoire de travail actuel | Crédit : Mercury_

Si vous êtes débutant, il est tout à fait normal de se perdre dans l'arborescence et de perdre soudainement le fil de l'endroit où vous êtes. Cette commande vous aide à garder une trace des choses.

Selon votre distro, vous pouvez voir un symbole `~` lorsque vous ouvrez le terminal. C'est le symbole du répertoire personnel par défaut de l'utilisateur. C'est comme le dossier `C:\Users\<default_user>` sous Windows, contenant tous les fichiers spécifiques à l'utilisateur. Sous Linux, il sera au format ci-dessus `/home/<default_user>`.

### Comment utiliser la commande `ls` 

Vous utilisez la commande `ls` pour lister le contenu d'un répertoire. Elle vous permet de savoir quels fichiers se trouvent à l'intérieur d'un répertoire sans GUI.

Lorsqu'elle est utilisée avec des drapeaux (flags), c'est un véritable couteau suisse, offrant diverses manières d'afficher le contenu du répertoire.

Les drapeaux courants que vous pourriez vouloir noter sont `-l` (liste détaillée), `-a` (tous, c'est-à-dire afficher les fichiers cachés) et `-c` (afficher les modifications récentes).

![Image](https://miro.medium.com/max/1316/1*NlpDMpdjfXoLqSFSEtozNg.png)
_Liste | Crédit : Mercury_

Les drapeaux sont des fonctionnalités des applications/outils qui vous permettent de leur dire quoi faire. Regardons le drapeau `-l` pour `ls` à titre d'exemple. La liste détaillée est une fonctionnalité qui peut être activée en utilisant la commande `ls -l`.

![Image](https://miro.medium.com/max/1008/1*GotS3bBvkTS1_wDy3z-uSQ.png)
_Liste détaillée | Crédit : Mercury_

Comme vous pouvez le voir, l'exécution de `ls` avec le drapeau diffère du simple `ls`. J'expliquerai les détails supplémentaires dans un autre article, ou vous pouvez faire vos propres recherches pour savoir ce qu'ils signifient.

### Comment utiliser la commande `cd` 

Vous utilisez la commande Change Directory (`cd`) pour naviguer dans l'arborescence des répertoires.

```
cd <directory>
```

![Image](https://miro.medium.com/max/1186/1*E0s7kJtwsxnFJsLf4eOkvA.png)
_Changement de répertoire | Crédit : Mercury_

Si vous exécutez la commande `ls -a`, vous remarquerez qu'il y a deux fichiers qui sont toujours là, quel que soit le dossier : `.` et `..` . Le fichier `.` représente le répertoire actuel et le fichier `..` représente le **répertoire parent** (le répertoire situé au-dessus du répertoire actuel).

### Comment utiliser les commandes `cat`, `more` et `less` 

Toutes les commandes ci-dessus sont des commandes de sortie. Vous les utilisez pour afficher le contenu des fichiers dans le terminal.

Mais il y a des différences notables. `cat` est couramment utilisé pour les fichiers contenant de petites quantités de texte. `less` et `more` sont plus susceptibles d'être utilisés pour des fichiers contenant de grandes quantités de texte, et la sortie peut être contrôlée avec les touches fléchées.

```
cat <file_name>
more <file_name>
less <file_name>
```

![Image](https://miro.medium.com/max/1400/1*fDzgjSBXWbi2oJxEDkF4vA.gif)
_cat vs more vs less | Crédit : Mercury_

Vous remarquerez que `cat` imprime la sortie directement dans votre terminal, tandis que `more` et `less` vous permettent d'utiliser les touches fléchées. Les commandes de sortie sont utilisées pour recueillir des informations et des identifiants à partir de systèmes compromis.

### Comment utiliser la commande `touch` 

Vous utilisez la commande touch pour créer des fichiers. Vous pouvez écrire dans ces fichiers de plusieurs manières, par exemple en utilisant un éditeur de texte ou en y redirigeant une entrée (nous y reviendrons plus tard).

Vous pouvez créer un fichier en utilisant la syntaxe suivante :

```
touch <file_name>
```

Vous pouvez ensuite utiliser la commande `ls` pour vérifier si votre fichier a bien été créé.

![Image](https://miro.medium.com/max/788/1*fQY39ligIX7500YEUq7mqg.png)
_Création d'un fichier | Crédit : Mercury_

### Comment utiliser la commande `nano` 

Nano est un éditeur de texte intégré populaire sous Linux. Il est très courant car il est facile à utiliser et supporté dans de nombreux environnements CLI. D'autres éditeurs de texte courants sont Vim (très agaçant 😫) et gedit (aussi simple que Notepad 🙃).

Vous pouvez éditer un fichier avec la commande suivante :

```
nano <file_name>
```

![Image](https://miro.medium.com/max/1400/1*ryyzZ2IdJb4yZ_DhCaDEPw.png)
_L'interface nano | Crédit : Mercury_

Certaines commandes sous l'interface Nano peuvent vous aider. « ^ » signifie simplement le bouton Ctrl et le bouton « M » est Alt. « ^S » (ou dans ce cas Ctrl + S) est utilisé pour enregistrer le fichier après y avoir écrit. La commande nano est utilisée par les hackers pour modifier des informations dans les fichiers, éditer des logs ou, si vous êtes un hacker red hat, supprimer des lignes essentielles de fichiers de configuration.

### Opérateurs de chaînage de commandes

Le « chaînage » de commandes est le concept consistant à écrire plusieurs commandes ensemble et à les exécuter de diverses manières. Vous le faites généralement à l'aide de caractères spéciaux. Les exemples incluent :

1. Esperluette (_&_) : Pour exécuter un programme en arrière-plan
2. ET logique (_&&_) : La commande suivante ne s'exécutera que si la précédente a réussi
3. Tube (_|_) : La sortie de la commande précédente sert d'entrée à la commande suivante
4. Écraser (>) : Écrase le contenu d'un fichier avec la sortie de la commande précédente
5. Ajouter (>>) : Ajoute la sortie de la commande précédente à la fin d'un fichier

Si vous ne comprenez pas comment tout cela fonctionne, ne vous inquiétez pas. Ils sont généralement exécutés avec d'autres commandes que je mentionnerai plus tard dans l'article.

### Comment utiliser les commandes `mv` et `cp` 

Ce sont deux commandes assez similaires mais qui présentent des différences notables. Vous utilisez `mv` pour déplacer un fichier vers un autre emplacement. Vous utilisez `cp` pour copier un fichier vers un autre emplacement.

```
mv <file_name>
cp <file_name>
```

![Image](https://miro.medium.com/max/1300/1*zU0ndkfgeNRxjaRqFsyJvQ.png)
_Exemples de cp et mv | Crédit : Mercury_

Il n'existe pas de commande spécifique pour renommer des fichiers sous Linux, la plupart des gens utilisent donc la commande `mv` avec cette syntaxe :

```
mv <original_file_name> <new_file_name>
```

Essayez par vous-même pour vous faire la main.

### Comment utiliser la commande `mkdir` 

La commande `mkdir` crée des répertoires. Vous pourriez l'utiliser pour créer un répertoire personnalisé auquel vous seul pouvez accéder sur un système compromis afin d'y conserver des scripts ou des outils pour la persistance.

```
mkdir <directory>
```

![Image](https://miro.medium.com/max/1052/1*3p9rSZRR5b15bXC-n4S27A.png)
_Création d'un nouveau répertoire | Crédit : Mercury_

### Comment utiliser les commandes `rm` et `rmdir` 

Vous pourriez être capable de deviner celle-ci par vous-même. `rm` est la commande pour supprimer des fichiers, et `rmdir` est la commande pour supprimer des répertoires.

```
rm <file_name>
rmdir <directory>
```

![Image](https://miro.medium.com/max/1400/1*4HPtNRZnozv2-NrbkCRrHA.png)
_rm, rmdir et rmdir avec le drapeau ignore-fail-on-non-empty | Crédit : Mercury_

Linux n'est pas très enclin à supprimer des dossiers s'ils ne sont pas vides. Pour remédier à cela, utilisez le drapeau `ignore-fail-if-non-empty` pour supprimer à la fois les fichiers et les répertoires.

Notez que vous devrez être extrêmement prudent avec ces commandes car elles n'envoient pas les fichiers ou répertoires supprimés à la Corbeille. Ils disparaissent, tout simplement.

### Comment utiliser la commande `stat` 

Vous utilisez la commande stat pour obtenir des informations sur un fichier.

```
stat <file_name>
```

![Image](https://miro.medium.com/max/1240/1*KTi872A6Qr9XES9Ag3IzAQ.png)
_stat | Crédit : Mercury_

Vous pouvez recueillir des informations sur le nom du fichier et son extension, les permissions, la date de création, de modification, de dernier accès et bien plus encore.

C'est le moment idéal pour en apprendre davantage sur les permissions. Si vous exécutez les commandes `ls -la` ou `stat`, vous verrez peut-être quelque chose comme ceci : drwxrwxrwx. Décortiquons cela.

![Image](https://miro.medium.com/max/1066/1*bJRHn0wWDnXZmNJ31Oc7Rg.png)
_Les permissions démystifiées | Crédit : unix.stackexchange.com_

La permission de lecture (r) vous permet de voir le contenu d'un fichier, la permission d'écriture (w) vous permet de modifier le fichier, et la permission d'exécution (x) vous permet de l'exécuter en tant que processus s'il s'agit d'un script ou d'un exécutable.

Il existe 3 classes d'utilisateurs pouvant accéder à un fichier : un utilisateur (user), un groupe (group) et les autres (others). Le compte root est une autre classe mais il est exempté ici.

Chaque ensemble « rwx » appartient à une classe de permission. Si l'espace affiche une lettre, l'ensemble possède cette permission. S'il y a un tiret, il n'a pas la permission.

Qu'en est-il du « d » au début ? Il indique s'il s'agit d'un répertoire (directory) ou d'un fichier. Le « d » signifie que c'est un répertoire, et s'il s'agit d'un tiret (-), c'est un fichier. Techniquement, un répertoire est un type spécial de fichier. Mais c'est une autre histoire.

### Comment utiliser la commande `echo` 

Vous utilisez la commande `echo` pour afficher une entrée. Prenons un exemple pour clarifier les choses.

```
echo "<text>"
```

![Image](https://miro.medium.com/max/1208/1*-l65O3_JkuG7Tzzgm-GnLg.png)

Comme vous pouvez le voir, vous pouvez utiliser `echo` avec l'opérateur > pour écrire du texte dans des fichiers.

### Comment utiliser la commande `grep` 

Montons d'un cran. Vous utilisez la commande `grep` pour extraire un texte spécifié d'un fichier en utilisant l'opérateur tube (pipe).

```
grep "<text>"
```

![Image](https://miro.medium.com/max/712/1*KX40zOFffHoiIZPC8IwV0Q.png)
_grep | Crédit : Mercury_

La commande ci-dessus n'est pas aussi compliquée qu'elle en a l'air. Nous disons à l'ordinateur d'afficher le contenu d'un fichier et, à l'aide de l'opérateur tube, nous disons à la commande `grep` de l'utiliser comme entrée. C'est ce qu'on appelle **rediriger (piping)** une commande vers une autre, et cela peut être fait plusieurs fois. Le texte trouvé est affiché en rouge.

`grep` est couramment utilisé pour rechercher certains textes dans des fichiers volumineux. Un exemple pratique serait de chercher les identifiants d'un utilisateur spécifique dans un fichier contenant beaucoup de texte. Vous pourriez utiliser `grep` pour chercher des mots comme « password », « login » et d'autres mots-clés que vous pensez trouver autour des identifiants que vous recherchez.

### Comment utiliser le drapeau « help » et les pages man

Les derniers sur notre liste sont « help » et `man`. Le drapeau « help » n'est pas nécessairement une commande mais c'est une aide précieuse si vous êtes confus au sujet d'une application ou d'un outil. Utilisez simplement ce qui suit :

```
<app or tool> --help
```

Cela vous donnera des informations rapides et concises à son sujet. `man`, quant à lui, vous donne toutes les informations documentées sur l'application.

```
man <app>
```

![Image](https://miro.medium.com/max/1400/1*iLguMiOH1fivVfS9cbeUew.gif)
_help vs man | Crédit : Mercury_

Vous remarquerez peut-être que dans le gif, j'ai utilisé `-h`. C'est parce que c'est la forme courte du drapeau. Certains drapeaux ont des formes courtes. S'il commence par un seul tiret, c'est la forme courte. S'il commence par deux tirets, c'est la forme longue.

## Comment mettre à jour votre Linux

Toute cette section peut en fait être réalisée avec une seule commande, mais décomposons-la pour bien comprendre l'ensemble. La tâche : mettre à jour votre système d'exploitation. Pour atteindre cet objectif, vous devez faire deux choses.

1. Mettre à jour les informations du dépôt local : Considérez cela comme une vérification des mises à jour avant de les télécharger et de les installer réellement.
2. Mettre à niveau le système : Comme son nom l'indique, nous téléchargeons les mises à jour, puis nous les installons.

La première commande à exécuter est :

```
sudo apt update
```

* sudo : Pour indiquer que nous exécutons la commande avec des privilèges élevés
* apt : Le gestionnaire de paquets
* update : Pour dire à l'ordinateur de mettre à jour ses informations locales sur le dépôt

Après avoir tapé cette commande, vous saisissez votre mot de passe, et voilà. Comme vous l'observerez, votre ordinateur téléchargera des informations depuis les dépôts sur les paquets (applications) à mettre à jour.

J'ai déjà mis à jour le mien, donc il ressemble à celui ci-dessous. Mais si c'est votre première fois, cela devrait prendre quelques minutes.

![sudo apt update](https://miro.medium.com/max/1150/1*-EmtTueRbZRXlPipT1OfUQ.png)
_sudo apt update | Crédit : Mercury_

Une fois que c'est terminé, vous pouvez exécuter la commande suivante pour télécharger et installer les mises à jour :

```
sudo apt full-upgrade
```

![sudo apt full-upgrade](https://miro.medium.com/max/1036/1*XzH5YOMUiMBn2OH02a3e3A.png)
_sudo apt full-upgrade | Crédit : Mercury_

Note : Vous pouvez interrompre le processus de téléchargement des paquets, mais **jamais le processus d'installation**. Cela pourrait casser votre système d'exploitation et le rendre inutilisable.

Pendant la mise à niveau, vous remarquerez peut-être quelques irrégularités, comme celle ci-dessous :

![Scrambled upgrade](https://miro.medium.com/max/1400/1*G9vDEmMMxCsLse32v-nVTQ.png)
_Mise à niveau brouillée | Crédit : Mercury_

Ne vous inquiétez pas, votre ordinateur ne va pas vous exploser au visage ou quoi que ce soit 😂. C'est juste un bug. Une fois les mises à niveau installées, vous devrez redémarrer votre ordinateur. Cela permettra à votre machine d'implémenter pleinement toutes les mises à jour.

![My personally customised desktop](https://miro.medium.com/max/1400/1*pIAewyHw1X7ovh1yrUMhsg.png)
_Mon bureau personnalisé | Crédit : Mercury_

Félicitations 🎉. Vous avez mis à jour votre système avec succès. Vous vous souvenez quand j'ai dit que tout cela pouvait être fait avec une seule commande ? La voici. 👀

```
sudo apt update && sudo apt upgrade -y && reboot
```

Détendez-vous, ce n'est pas aussi compliqué qu'il n'y paraît. Regardez le code morceau par morceau. Les seuls éléments inconnus sont les symboles `&&`.

Comme je l'ai mentionné plus tôt, ce sont des opérateurs ET logiques. Cela dit simplement à l'ordinateur d'exécuter la première commande, de la terminer, puis d'exécuter la suivante. Le drapeau `-y` dit à l'ordinateur d'effectuer la mise à niveau sans intervention de l'utilisateur.

Ainsi, la commande ci-dessus dit à l'ordinateur de d'abord mettre à jour, puis de mettre à niveau, et enfin, de redémarrer. Simple comme bonjour, non ? 😎

## Conclusion

![Image](https://www.freecodecamp.org/news/content/images/2022/09/1-WFhyEGF0fbJqwgo79KSdJQ-1.jpeg)
_Tux le Parrain ¦ Crédit : Wallpaperflare.com_

Faisons un récapitulatif rapide de ce que vous avez fait :

1. Nous avons fait un tour d'horizon de l'OS Linux
2. Nous avons appris la gestion des paquets sous Linux
3. Nous avons passé en revue la structure des fichiers Linux
4. Et nous avons exécuté quelques commandes sur l'interface en ligne de commande

Et sur cette note, nous sommes arrivés à la fin de cet article. J'espère qu'il vous a plu. Et comme je le dis toujours, bon hacking ! 🙃

### Ressources Linux

1. Vous pouvez [en savoir plus sur le chaînage des commandes ici](https://www.geeksforgeeks.org/chaining-commands-in-linux/)
2. Voici une [excellente vidéo sur la gestion des paquets](https://www.youtube.com/watch?v=0W8-3RwvJwc&t=152s).
3. Et voici une [introduction rapide à la structure des fichiers Linux](https://www.geeksforgeeks.org/linux-directory-structure/).

### Remerciements

Merci à Anuoluwapo Victor, [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), et ma famille pour l'inspiration, le soutien et les connaissances utilisés pour rédiger cet article. Vous êtes géniaux.