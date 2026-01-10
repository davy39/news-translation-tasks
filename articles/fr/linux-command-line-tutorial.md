---
title: Tutoriel de la ligne de commande Linux – Comment utiliser les commandes courantes
  du terminal
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2022-10-18T23:33:44.000Z'
originalURL: https://freecodecamp.org/news/linux-command-line-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-sora-shimazaki-5935794--3-.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: Tutoriel de la ligne de commande Linux – Comment utiliser les commandes
  courantes du terminal
seo_desc: "An operating system is a set of software layers between you and your computer's\
  \ hardware. \nThe operating system (or OS) is a piece of software that controls\
  \ all other application programs and helps you manage the hardware and software\
  \ of your compute..."
---

Un système d'exploitation est un ensemble de couches logicielles entre vous et le matériel de votre ordinateur. 

Le système d'exploitation (ou OS) est un logiciel qui contrôle toutes les autres applications et vous aide à gérer le matériel et les logiciels de votre ordinateur.

Des exemples de systèmes d'exploitation populaires sont Windows, Linux, MacOS et Android. Dans ce tutoriel, nous nous concentrerons sur le système d'exploitation Linux.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/USER--1-.png)
_diagramme du système d'exploitation_

Vous apprendrez les commandes et opérateurs Linux les plus fréquemment utilisés. Vous obtiendrez également une compréhension de haut niveau du système d'exploitation Linux et de ses diverses distributions, qui sont appelées "distros" dans cet article.

## Table des matières

* [Pourquoi apprendre la ligne de commande Linux ?](#heading-pourquoi-apprendre-la-ligne-de-commande-linux)
* [Histoire des systèmes d'exploitation](#heading-histoire-des-systemes-d-exploitation)
* [L'essor du projet GNU](#heading-l-essor-du-projet-gnu)
* [Comment fonctionne Linux et ses composants de base](#heading-comment-fonctionne-linux-et-ses-composants-de-base)
* [Quelles sont les distributions Linux ?](#heading-quelles-sont-les-distributions-linux)
* [Comment choisir une distribution Linux](#heading-comment-choisir-une-distribution-linux)
* [Commandes de base Linux à exécuter dans le terminal](#heading-commandes-de-base-linux-a-executer-dans-le-terminal)
* [Comment travailler avec les répertoires sous Linux](#heading-comment-travailler-avec-les-repertoires-sous-linux)
* [Commandes pour travailler avec les fichiers sous Linux](#heading-commandes-pour-travailler-avec-les-fichiers-sous-linux)
* [Commandes pour travailler avec le contenu des fichiers](#heading-commandes-pour-travailler-avec-le-contenu-des-fichiers)
* [Opérations de commandes Linux](#heading-operations-de-commandes-linux)

## Pourquoi apprendre la ligne de commande Linux ?

Il y a beaucoup de raisons pour lesquelles vous devriez apprendre la ligne de commande Linux. Certaines d'entre elles sont :

* **Plus de contrôle sur votre machine** : Vous avez un grand pouvoir et contrôle avec la ligne de commande. Vous pouvez exécuter des commandes pour changer les permissions, voir les fichiers cachés, interagir avec les bases de données, démarrer des serveurs, et plus encore.
* **C'est plus rapide** : Vous pouvez accomplir des tâches beaucoup plus rapidement avec les commandes de base dans votre boîte à outils que vous ne le pourriez avec une interface graphique (GUI). Gardez simplement à l'esprit que cela peut être plus lent pendant l'apprentissage de la CLI.
* **Automatiser de nombreuses tâches** : Vous pouvez accélérer votre travail en utilisant une seule commande pour créer 10 000 fichiers, chacun avec un nom unique. Avec une GUI, ce processus est laborieux.
* **Disponible partout** : Les instructions que vous émettez s'exécuteront automatiquement de manière similaire sur les ordinateurs Linux et Mac. Et avec un peu de modification, elles fonctionneront également sur Windows.
* **Exigence de base** : Vous DEVEZ utiliser la ligne de commande si vous voulez approfondir vos connaissances dans n'importe quel domaine technologique lié à la programmation, y compris le développement, l'analyse de données, l'ingénierie devops, l'administration système, la sécurité, l'ingénierie du machine learning, et autres.

## Histoire des systèmes d'exploitation

La plupart des systèmes d'exploitation sont généralement divisés en deux familles : les descendants Unix et les descendants Microsoft NT.

**Unix** était un système d'exploitation développé au milieu des années 1960. C'est le "grand-parent" de nombreux systèmes d'exploitation modernes que nous utilisons fréquemment maintenant, comme Linux. 

Le système d'exploitation Unix était un projet à code source fermé (ce qui signifie que son code et ses fichiers n'étaient pas rendus publics). Et cela a conduit à l'essor du mouvement du "logiciel libre" dirigé par Richard Stallman. Il soutenait que les utilisateurs devraient avoir la liberté d'exécuter, copier, distribuer et collaborer sur le code source d'un projet.

**Les descendants Microsoft NT** étaient des systèmes d'exploitation graphiques propriétaires créés par Microsoft. Les descendants Windows NT n'ont pas naturellement des commandes similaires à Linux, contrairement à Unix et aux systèmes d'exploitation basés sur Unix, qui en ont. Au lieu de cela, Microsoft NT a son propre ensemble de commandes et de shells par défaut. 

Les descendants de Microsoft NT incluent Windows, Xbox OS, Windows Phone/Mobile, et autres.

## L'essor du projet GNU

Richard Stallman voulait créer une alternative de logiciel libre à Unix. Il a travaillé avec d'autres développeurs en 1984 pour créer un système d'exploitation complet qui serait libre. Ils ont donc commencé à travailler sur le projet GNU. 

À la même époque, un autre développeur nommé Linus Torvalds créait son propre noyau connu sous le nom de Linux. À cette époque, de nombreuses pièces de GNU étaient terminées mais elles manquaient d'un noyau. Torvalds a combiné son noyau avec les composants GNU existants pour créer un système d'exploitation complet. 

Certains développeurs pensent fortement que le nom devrait être GNU/Linux au lieu de simplement Linux, car cela reflète la jonction du noyau Linux avec le projet GNU.

## Comment fonctionne Linux et [i](https://en.wikipedia.org/wiki/Graphical_user_interface)ts composants de base

Dans cette section, vous apprendrez comment fonctionne Linux en comprenant ses composants fondamentaux. Nous allons maintenant discuter de ces éléments.

### Qu'est-ce qu'un noyau ?

Un **noyau** est une partie d'un système d'exploitation qui facilite les interactions entre le matériel et le logiciel. C'est un élément essentiel d'un système d'exploitation pour un ordinateur.

Le cœur du système d'exploitation seul est responsable de la fourniture de tous les autres composants avec les services nécessaires. Il aide au contrôle des périphériques, à la mise en réseau, à la gestion du système de fichiers, à la gestion des processus et de la mémoire, et il agit comme l'interface principale entre le système d'exploitation et le matériel.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-11-1.png)
_[noyau](https://d1m75rqqgidzqn.cloudfront.net/wp-data/2022/08/04135248/image-11.png)_

### Qu'est-ce qu'un shell ?

Un shell est une interface informatique pour un système d'exploitation. Le shell expose les services du système d'exploitation aux utilisateurs ou à d'autres programmes. Le shell prend vos commandes et les donne au système d'exploitation pour qu'il puisse les exécuter. 

Il est nommé shell car c'est la couche externe autour du système d'exploitation – comme la coquille autour d'une huître !

### Qu'est-ce que le terminal ?

Un terminal est un programme qui exécute un shell. C'est là que nous exécutons la plupart de nos commandes qui disent au système d'exploitation quoi faire. 

Vous installez le terminal de la manière suivante sur différents systèmes d'exploitation :

* **Utilisateurs de distributions Linux** – le shell Bash est installé par défaut
* **Utilisateurs de Mac** – Terminal est installé par défaut et peut exécuter des commandes similaires à Linux
* **Utilisateurs de Windows** – Téléchargez [Windows Subsystem for Linux (WSL)](https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) ou utilisez `git bash` et exécutez toutes les commandes Linux à partir de là.

## Quelles sont les distributions Linux ?

Les distributions Linux (populairement appelées **distros**) sont des variantes du système d'exploitation Linux. Ces distros sont construites sur la base du logiciel open source de Linux. 

Voici quelques exemples :

### Famille Debian

Depuis sa fondation en 1993, Debian a publié de nouvelles versions beaucoup plus lentement qu'Ubuntu et Mint. Il est donc l'un des distributeurs Linux les plus fiables.

Debian est la base d'Ubuntu, qui a été créé pour améliorer rapidement les composants fondamentaux de Debian et le rendre plus convivial.

Ubuntu a été créé par Canonical en 2004 et a immédiatement gagné en popularité. Canonical veut qu'Ubuntu soit utilisé comme un bureau Linux graphique simple, sans ligne de commande. C'est la distribution Linux la plus connue. 

Ubuntu est simple à utiliser pour les débutants. Il dispose d'un grand nombre d'applications préinstallées et de bibliothèques de dépôts pratiques.

### Famille Red Hat

Red Hat est un distributeur Linux professionnel. Red Hat Enterprise Linux (RHEL) et Fedora sont leurs produits, tous deux open source. 

Fedora offre des mises à jour plus rapides et aucun support, mais RHEL est soigneusement testé avant sa sortie et est supporté pendant sept ans après la sortie.

Red Hat utilise la loi sur les marques pour empêcher la redistribution de son logiciel. Le code source de Red Hat Enterprise Linux est utilisé dans CentOS, un effort communautaire qui élimine toutes les marques de Red Hat et le rend disponible au public. En d'autres termes, c'est une version gratuite de RHEL et offre une plateforme fiable et durable.

### Famille SUSE

SUSE a créé son propre système d'exploitation pour ordinateurs. Il est fourni avec des logiciels système et d'application d'autres projets open source et est développé sur la base du noyau Linux libre et open source. 

SUSE Linux a été principalement développé en Europe et est d'origine allemande. Le nom SUSE est un acronyme pour "Software und System-Entwicklung." SUSE est l'une des plus anciennes distributions commerciales encore en usage car la version initiale est sortie au début de 1994.

### Famille Fedora

Il s'agit d'un projet qui offre les versions les plus récentes des logiciels et se concentre principalement sur les logiciels libres. Il utilise des applications 'upstream' au lieu de développer son propre environnement de bureau. Il est livré avec l'environnement de bureau GNOME3 par défaut. Bien que moins fiable, il offre les informations les plus récentes.

## Comment choisir une distribution Linux

<table class="alt" style="width: 700.344px; border: 1px solid rgb(199, 204, 190); text-align: left; display: table; border-collapse: collapse; border-spacing: 0px; color: rgb(51, 51, 51); font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="display: table-row-group;"><tr style="display: table-row; vertical-align: inherit; border-color: inherit; background-color: rgb(239, 241, 235);"><th style="color: rgb(0, 0, 0); background-color: rgb(199, 204, 190); font-size: 17px; font-family: &quot;times new roman&quot;; padding: 12px; vertical-align: top; text-align: left;">Distribution</th><th style="color: rgb(0, 0, 0); background-color: rgb(199, 204, 190); font-size: 17px; font-family: &quot;times new roman&quot;; padding: 12px; vertical-align: top; text-align: left;">Raison d'utilisation</th></tr><tr style="display: table-row; vertical-align: inherit; border-color: inherit; background-color: rgb(255, 255, 255);"><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Ubuntu</td><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Il fonctionne comme Mac OS et est facile à utiliser.</td></tr></tr><tr style="display: table-row; vertical-align: inherit; border-color: inherit; background-color: rgb(239, 241, 235);"><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">CentOS</td><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Si vous voulez utiliser Red Hat mais sans sa marque déposée.</td></tr><tr style="display: table-row; vertical-align: inherit; border-color: inherit; background-color: rgb(239, 241, 235);"><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Fedora</td><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Si vous voulez utiliser Red Hat et les derniers logiciels.</td></tr><tr style="display: table-row; vertical-align: inherit; border-color: inherit; background-color: rgb(255, 255, 255);"><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Red Hat Enterprise</td><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Utilisé commercialement.</td></tr><tr style="display: table-row; vertical-align: inherit; border-color: inherit; background-color: rgb(255, 255, 255);"><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">OpenSUSE</td><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Il fonctionne de la même manière que Fedora mais est légèrement plus ancien et plus stable.</td></tr><tr style="display: table-row; vertical-align: inherit; border-color: inherit; background-color: rgb(239, 241, 235);"><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Arch Linux</td><td style="border: 1px solid rgb(199, 204, 190); text-align: justify; padding: 8px; vertical-align: top; font-size: 16px; font-family: inter-regular, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; color: rgb(51, 51, 51); line-height: 1.7; margin-left: 0px; display: table-cell;">Il n'est pas convivial pour les débutants.</td></tr></tbody></table>

Maintenant, parlons de quelques commandes que vous pouvez exécuter pour interagir avec le shell.

# Commandes de base Linux à exécuter dans le terminal

### La commande `whoami`

Cette commande imprime le nom de l'utilisateur actuellement connecté dans la session du terminal.

```bash
caesarsage@caesarsage:$ whoami
```

### La commande `man`

Cette commande imprime le **manuel** ou des informations sur une commande, des fichiers de configuration, etc. Cette commande est très utile lorsque vous avez besoin de plus d'informations sur une commande.

```bash
caesarsage@caesarsage:$ man whoami
```

### La commande `clear`

Efface toutes les commandes précédentes qui ont été exécutées dans le terminal actuel. Cela efface l'écran des commandes précédentes dans le terminal.

```bash
caesarsage@caesarsage:$ clear
```

### Comment ouvrir des fichiers

#### Utilisateurs Mac : 

`open <nom de fichier ou de répertoire>`

La commande open vous permet d'ouvrir un fichier ou un répertoire dans l'interface graphique (GUI) en dehors du terminal.

#### Utilisateurs Linux

`xdg-open <nom de fichier ou de répertoire>`

#### Utilisateurs Windows WSL

Vous pouvez ouvrir des fichiers de manière similaire à Linux, mais vous devez installer le paquet xdg-open.

Exemple pour les utilisateurs Linux et Windows :

```bash
caesarsage@caesarsage:$ xdg-open clean-code-architecture.pdf
```

Maintenant que nous avons couvert les commandes de base, apprenons quelques autres commandes que vous utiliserez souvent.

## Comment travailler avec les répertoires sous Linux

Voyons maintenant quelques-unes des commandes les plus courantes que vous utiliserez pour travailler avec les répertoires. 

Les répertoires sont comme des dossiers, et vous pouvez créer, supprimer et effectuer toutes les fonctions sur eux via l'interface de votre système avec une souris ou un curseur.

Ici, nous ferons quelque chose de similaire mais depuis le confort de notre terminal. Les commandes suivantes vous permettent d'effectuer différentes opérations sur les répertoires :

* **`pwd`** (répertoire de travail actuel)
* **`cd`** (répertoire actuel)
* **`ls`** (lister)
* **`mkdir`** (créer un répertoire)
* **`rmdir`** (supprimer un répertoire)

Voyons ce que fait chacune d'entre elles :

### La commande `pwd`

Chaque fois que vous vous sentez perdu dans le système de fichiers, appelez la commande `pwd` pour savoir où vous vous trouvez. Elle ne prend aucun argument.

```bash
casesarsage@caesarsage:~/Documents/github.com$ pwd
```

Elle devrait imprimer le chemin du dossier/répertoire actuel où vous vous trouvez.

### La commande `cd <chemin>`

Vous pouvez changer votre répertoire actuel avec la commande cd (Changer de Répertoire). Tout comme aller et venir entre les dossiers lorsque vous utilisez l'interface graphique.

```bash
caesarsage@caesarsage$: cd Documents/articles
```

Cette commande me mène à un dossier appelé articles à l'intérieur de mon dossier Documents.

Voyons ce que vous pouvez faire d'autre avec `cd`.

#### `cd ~`

Le cd est également un raccourci pour revenir dans votre répertoire personnel. Il suffit de taper cd sans répertoire cible pour vous placer dans votre répertoire personnel. Taper `cd ~` a le même effet.

```bash
caesarsage@caesarsage:~/Documents/github.com$ cd ~
```

Cela vous mène à votre répertoire personnel depuis le dossier github.com

#### `cd ..`

Pour aller au répertoire parent (celui juste au-dessus de votre répertoire actuel dans l'arborescence des répertoires), tapez **`cd ..`** :

```bash
caesarsage@caesarsage:~/Documents/github.com$ cd ..
```

### La commande `ls`

À l'intérieur d'un dossier, vous pouvez lister tous les fichiers que le dossier contient en utilisant la commande `ls`. Elle ne prend aucun argument.

```bash
caesarsage@caesarsage:~/Documents/mycatfolder$ ls
```

Tout comme avec `cd`, il y a quelques autres options que vous pouvez utiliser avec `ls` :

#### `ls -a`

Une option fréquemment utilisée avec ls est -a pour montrer tous les fichiers. Montrer tous les fichiers signifie inclure les fichiers cachés. 

Lorsque le nom d'un fichier sur un système de fichiers Linux commence par un point, il est considéré comme un fichier caché et n'apparaît pas dans les listes de fichiers régulières. Cette commande montrera ces fichiers.

#### `ls -l`

De nombreuses fois, vous utiliserez des options avec ls pour afficher le contenu du répertoire dans différents formats ou pour afficher différentes parties du répertoire. 

Taper simplement ls vous donne une liste de fichiers dans le répertoire. Taper **`ls -l`** donne une liste longue et les permissions (rwx - lire, écrire, exécuter).

### La commande `mkdir <nomDuRépertoire>`

Se promener dans l'arborescence des fichiers Unix est amusant, mais c'est encore plus amusant de créer vos propres répertoires/dossiers avec **mkdir**. 

Vous devez donner au moins un paramètre à `mkdir` – le nom du nouveau répertoire à créer. Réfléchissez avant de taper un / initial.

```bash
caesarsage@caesarsage:~/Documents$ mkdir cats
```

### La commande `rmdir <nomDuRépertoire>`

Lorsque qu'un répertoire est vide, vous pouvez utiliser **rmdir** pour supprimer ou effacer le répertoire.

```bash
caesarsage@caesarsage~/Documents$ rmdir cats
```

#### `rmdir -p <nomDuRépertoire>`

Lorsque vous voulez supprimer des répertoires imbriqués, vous pouvez utiliser le drapeau **-p**. Vous utilisez `rmdir -p` pour supprimer récursivement des répertoires. Cela est similaire à la création de répertoires imbriqués avec **mkdir -p**.

```bash
caesarsage@caesarsage:~/Documents$ rmdir -p articles/drafts
```

## Commandes pour travailler avec les fichiers sous Linux

Dans cette section, vous apprendrez à reconnaître, créer, supprimer, copier et déplacer des fichiers en utilisant les commandes suivantes :

* **`touch`**
* **`rm`**
* **`cp`**
* **`mv`**
* **`rename`**

### La commande `touch <nomDeFichier>`

Un moyen facile de créer un fichier vide est avec `touch` comme ceci :

```bash
caesarsage@caesarsage:~$ touch file1.txt file2.md file3
```

Ce qui précède crée trois fichiers (fichiers texte et markdown).

### La commande `rm <nomDeFichier>`

Lorsque vous n'avez plus besoin d'un fichier, utilisez rm pour le supprimer. 

**Notez** que contrairement à certaines interfaces graphiques, la ligne de commande en général n'a pas de corbeille ou de poubelle d'où vous pouvez récupérer des fichiers. Lorsque vous utilisez `rm` pour supprimer un fichier, le fichier est parti. Soyez donc prudent lorsque vous supprimez des fichiers !

```bash
caesarsage@caesarsage:~$ rm file1.txt
```

Voici quelques autres façons spécifiques d'utiliser `rm` :

#### `rm -v <nomDeFichier>`

Ce drapeau vous donne un retour sur ce qu'il a fait (suppression d'un fichier).

#### `rm -i <nomDeFichier>`

Pour éviter de supprimer accidentellement un fichier, vous pouvez taper `rm -i`. Cela affichera une invite pour confirmer si vous voulez vraiment supprimer le fichier ou non.

#### `rm -rf <nomDeFichier>ou<répertoire>`

Par défaut, `rm -r` ne supprimera pas les répertoires non vides. Cependant, rm accepte plusieurs options qui vous permettront de supprimer n'importe quel répertoire. 

L'instruction `rm -rf` est célèbre car elle effacera n'importe quoi (à condition que vous ayez les permissions de le faire). Lorsque vous êtes connecté en tant que root, soyez très prudent avec `rm -rf` (le f signifie forcer et le r signifie récursif), car être root implique que les permissions ne s'appliquent pas à vous. Vous pouvez littéralement effacer tout votre système de fichiers par accident.

### La commande `cp <ancienFichier> <nouveauFichier>`

Pour copier un fichier, utilisez `cp` avec un nom de fichier et un nouvel argument de nom de fichier.

```bash
caesarsage@caesarsage:$ cp text2.md text2Copy.md
```

#### `cp <source> <destination>`

Utilisez cette option pour copier un fichier dans un autre répertoire (destination).

Si la cible est un répertoire, alors les fichiers sources sont copiés dans ce répertoire cible.

```bash
caesarsage@caesarsage:~$ mkdir dir3
caesarsage@caesarsage:~$ cp file2.md dir3
```

#### `cp -r répertoireSource répertoireCible`

Pour copier des répertoires complets, utilisez `cp -r` (l'option -r force la copie récursive de tous les fichiers dans tous les sous-répertoires).

```bash
caesarsage@caesarsage:~$ cp -r dir1/dir2  dir3
```

### La commande `mv source destination`

Vous pouvez utiliser la commande `mv` pour déplacer et renommer des répertoires.

```bash
caesarsage@caesarsage:~/Documents/$ mv cat catFolder
```

```bash
caesarsage@caesarsage:~/Documents/$ mv newarticle.txt articles
```

## Commandes pour travailler avec le contenu des fichiers

Vous pouvez utiliser les commandes suivantes pour regarder le contenu des fichiers texte :

* **`head`**
* **`tail`**
* **`cat`**
* **`less`**
* **`echo`**
* **`wc`**
* **`grep`**

### La commande `head <fichier>`

Cette commande imprime la première partie des fichiers. Par défaut, elle donne les 10 premières lignes d'un fichier, mais vous pouvez outrepasser cela en ajoutant le drapeau `-n`.

```bash
caesarsage@caesarsage:$ head /etc/passwd
```

### La commande `tail <fichier>`

Cette commande imprime les 10 dernières lignes d'un fichier. Vous pouvez également outrepasser le défaut de manière similaire en passant le drapeau `-n`.

La commande tail a également un drapeau `-f` qui vous aide à continuer à imprimer les ajouts supplémentaires à un fichier. Cela est utile pour les fichiers de logs et d'erreurs qui changent constamment dans votre système afin que vous puissiez les surveiller.

```bash
caesarsage@caesarsage:$ tail /etc/passwd
```

### La commande `cat <nomDeFichier>`

`cat` peut ajouter du contenu à un fichier, ce qui le rend super puissant. Dans son utilisation la plus simple, cat imprime le contenu d'un fichier sur les sorties standard.

```bash
caesarsage@caesarsage:$ cat file
```

Vous pouvez imprimer le contenu de plusieurs fichiers également.

Et en utilisant l'**opérateur >** (nous verrons ce que cela fait plus tard – pour l'instant, sachez qu'il prend la sortie du terminal dans un fichier), vous pouvez concaténer le contenu de plusieurs fichiers dans un nouveau fichier :

```bash
caesarsage@caesarsage:$ cat file2.txt file3.txt > combine.txt
```

Vous pouvez également l'utiliser pour créer des fichiers :

```bash
caesarsage@caesarsage:$ cat > newfile.txt
```

### La commande `less <nomDeFichier>`

La commande `less` montre le contenu stocké à l'intérieur d'un fichier dans une interface utilisateur agréable et interactive.

```bash
caesarsage@caesarsage:$ less /etc/passwd
```

Utilisez **b** pour faire défiler une page, **G** pour aller à la fin, **g** pour aller au début et **q** pour quitter la commande.

### La commande `echo`

Cette commande imprime sur la sortie l'argument qui lui est passé.

```bash
caesarsage@caesarsage:$ echo 'Hello world'
```

### La commande `wc <entrée>`

`wc` signifie word count (compte de mots), et cette commande donne des informations sur l'entrée (par exemple un fichier) comme le nombre de lignes, le nombre de mots, le nombre d'octets pour le contenu, etc.

#### `wc -l`

Cette option imprime uniquement le compte des nouvelles lignes.

#### `wc -m`

Cette option imprime uniquement le compte des caractères.

#### `wc -c`

Cette option imprime uniquement le compte des octets.

#### `wc -w`

Cette option imprime uniquement le compte des mots.

### La commande `grep`

La commande grep est probablement la commande de manipulation de texte la plus largement utilisée. Elle vous permet de filtrer le contenu d'un fichier pour l'affichage. 

Si, par exemple, vous voulez voir toutes les lignes qui incluent le mot output dans votre fichier, vous pourriez utiliser cat et lui demander d'afficher uniquement ces lignes.

```bash
caesarsage@caesarsage:$ cat /etc/snort/snort.conf | grep output
```

Vous en apprendrez plus sur l'opérateur pipe (|) dans la section suivante.

## Opérations de commandes Linux

Quelques commandes courantes que vous pouvez utiliser pour manipuler les commandes Linux sont :

* **`>`** : redirige les sorties standard

La plupart des commandes que nous avons vues jusqu'à présent impriment quelque chose pour nous sur le terminal. Par exemple, PWD imprime notre répertoire actuel, et ainsi de suite. 

Ces sorties peuvent être stockées et redirigées vers un fichier avec l'utilisation de ">". Il remplace le contenu actuel du fichier lorsque vous l'exécutez plusieurs fois.

```bash
caesarsage@caesarsage: whoami > file.txt
caesarsage@caesarsage: pwd > file.txt
caesarsage@caesarsage: cat > file.txt
```

* **`>>`** : redirige les sorties standard et ajoute de nouveaux contenus.

Contrairement à l'opération '>', >> ne remplace pas la sortie précédemment stockée dans un fichier.

```bash
caesarsage@caesarsage: whoami >> file.txt
caesarsage@caesarsage: pwd >> file.txt
caesarsage@caesarsage: cat file.txt
```

* **`|`** : cet opérateur est appelé pipe.

Cela prend la sortie d'une commande et la passe comme entrée pour une autre commande. Voici comment l'utiliser :

```bash
caesarsage@caesarsage:$ cat /etc/snort/snort.conf | grep output
```

# Résumé

Dans cet article, vous avez appris le système d'exploitation Linux à un niveau élevé. Vous avez également appris à utiliser la ligne de commande Linux pour interagir avec le système d'exploitation.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).

À bientôt et à la prochaine ! 👋🏽