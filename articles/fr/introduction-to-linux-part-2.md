---
title: Introduction à Linux, Partie 2
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-02-23T13:49:38.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-linux-part-2
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/linux2.png
tags:
- name: Linux
  slug: linux
seo_title: Introduction à Linux, Partie 2
seo_desc: In this comprehensive course, you'll learn many of the tools used every
  day by both Linux SysAdmins and the millions of people running Linux distributions
  like Ubuntu on their PCs. This course will teach you how to navigate Linux's Graphical
  User Int...
---

Dans ce cours complet, vous apprendrez de nombreux outils utilisés quotidiennement par les administrateurs système Linux et les millions de personnes exécutant des distributions Linux comme Ubuntu sur leurs PC. Ce cours vous apprendra à naviguer dans les interfaces utilisateur graphiques de Linux et son puissant écosystème d'outils en ligne de commande.

Ceci est la deuxième partie. Lisez d'abord la première partie : [https://www.freecodecamp.org/news/introduction-to-linux/](https://www.freecodecamp.org/news/introduction-to-linux/)

## Chapitre 18 : Principes de sécurité locale

### Objectifs d'apprentissage

À la fin de ce chapitre, vous devriez être capable de :

* Avoir une bonne compréhension des meilleures pratiques et des outils pour rendre les systèmes Linux aussi sécurisés que possible.
* Comprendre les pouvoirs et les dangers de l'utilisation du compte root (superutilisateur).
* Utiliser la commande **sudo** pour effectuer des opérations privilégiées tout en restreignant les pouvoirs étendus autant que possible.
* Expliquer l'importance de l'isolation des processus et de l'accès au matériel.
* Travailler avec les mots de passe, y compris comment les définir et les changer.
* Décrire comment sécuriser le processus de démarrage et les ressources matérielles.

### Comptes utilisateurs

Le noyau Linux permet aux utilisateurs correctement authentifiés d'accéder aux fichiers et aux applications. Bien que chaque utilisateur soit identifié par un entier unique (l'identifiant utilisateur ou UID), une base de données distincte associe un nom d'utilisateur à chaque UID. Lors de la création d'un compte, les nouvelles informations utilisateur sont ajoutées à la base de données des utilisateurs et le répertoire personnel de l'utilisateur doit être créé et peuplé avec certains fichiers essentiels. Des programmes en ligne de commande tels que **useradd** et **userdel** ainsi que des outils graphiques sont utilisés pour créer et supprimer des comptes.

![Comptes utilisateurs : /etc/passwd](https://courses.edx.org/assets/courseware/v1/5e3a5828edd1ac8364f2f744f8fa1942/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/etcpasswd.png)

Pour chaque utilisateur, les sept champs suivants sont maintenus dans le fichier **/etc/passwd** :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="15%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Nom du champ</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Détails</strong></span></td><td align="center" bgcolor="#003f60" width="40%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Remarques</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Nom d'utilisateur</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Nom de connexion de l'utilisateur</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Doit comporter entre 1 et 32 caractères</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Mot de passe</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Mot de passe de l'utilisateur (ou le caractère <strong style="font-weight: bold; line-height: 1.4em;">x</strong> si le mot de passe est stocké dans le fichier <strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;"><span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/etc/shadow</span></span></strong>) au format chiffré</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">N'est jamais affiché sous Linux lorsqu'il est tapé ; cela empêche les regards indiscrets</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Identifiant utilisateur (UID)</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Chaque utilisateur doit avoir un identifiant utilisateur (UID)</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><ul style="padding: 0px; margin: 0px; line-height: 1.4em; color: rgb(69, 69, 69); list-style: outside none disc; font-size: 16px;"><li style="line-height: 1.4em; margin-bottom: 0.70788em; font-size: 16px; margin-left: 30px; padding: 0px;">L'UID 0 est réservé pour l'utilisateur root</li><li style="line-height: 1.4em; margin-bottom: 0.70788em; font-size: 16px; margin-left: 30px; padding: 0px;">Les UID allant de 1 à 99 sont réservés pour d'autres comptes prédéfinis</li><li style="line-height: 1.4em; margin-bottom: 0.70788em; font-size: 16px; margin-left: 30px; padding: 0px;">Les UID allant de 100 à 999 sont réservés pour les comptes et groupes système</li><li style="line-height: 1.4em; margin-bottom: 0.70788em; font-size: 16px; margin-left: 30px; padding: 0px;">Les utilisateurs normaux ont des UID de 1000 ou plus</li></ul></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Identifiant de groupe (GID)</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">L'identifiant de groupe principal (GID) ; numéro d'identification de groupe stocké dans le fichier <span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: inherit;">/etc/group</span></strong></span></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Est couvert en détail dans le chapitre sur les <em style="line-height: 1.4em; font-style: italic;">Processus</em></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Informations utilisateur</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Ce champ est facultatif et permet l'insertion d'informations supplémentaires sur l'utilisateur, telles que son nom</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Par exemple : <strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">Rufus T. Firefly</span></strong></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;">Répertoire personnel</span></strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">L'emplacement du chemin absolu du répertoire personnel de l'utilisateur</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Par exemple : <span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/home/rtfirefly</span></strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;"><strong style="font-weight: bold; line-height: 1.4em;">Shell</strong></td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">L'emplacement absolu du shell par défaut d'un utilisateur</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Par exemple : <span style="color: rgb(153, 51, 0); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">/bin/bash</span></strong></span></td></tr></tbody></table>

### Types de comptes

Par défaut, Linux distingue plusieurs types de comptes afin d'isoler les processus et les charges de travail. Linux dispose de quatre types de comptes :

* root
* Système
* Normal
* Réseau

Pour un environnement de travail sécurisé, il est conseillé d'accorder le minimum de privilèges possibles et nécessaires aux comptes, et de supprimer les comptes inactifs. L'utilitaire **last**, qui montre la dernière fois que chaque utilisateur s'est connecté au système, peut être utilisé pour aider à identifier les comptes potentiellement inactifs qui sont candidats à la suppression du système.

Gardez à l'esprit que les pratiques que vous utilisez sur les systèmes multi-utilisateurs d'entreprise sont plus strictes que celles que vous pouvez utiliser sur les systèmes de bureau personnels qui n'affectent que l'utilisateur occasionnel. Cela est particulièrement vrai pour la sécurité. Nous espérons vous montrer des pratiques applicables aux serveurs d'entreprise que vous pouvez utiliser sur tous les systèmes, mais comprenez que vous pouvez choisir de relâcher ces règles sur votre propre système personnel.

![Utilitaire last](https://courses.edx.org/assets/courseware/v1/c74352d16a50f0bb625173f8f9c2abdb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lastoutput.png)
_Utilitaire last_

### Comprendre le compte root

**root** est le compte le plus privilégié sur un système Linux/UNIX. Ce compte a la capacité d'effectuer toutes les facettes de l'administration système, y compris l'ajout de comptes, le changement de mots de passe des utilisateurs, l'examen des fichiers jour, l'installation de logiciels, etc. La plus grande prudence doit être prise lors de l'utilisation de ce compte. Il n'a aucune restriction de sécurité imposée.

![Tux le pingouin avec une couronne et un sceptre](https://courses.edx.org/assets/courseware/v1/36cc69851c8f812250c33fd23b642507/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch18_screen05.jpg)

Lorsque vous êtes connecté en tant que, ou agissez en tant que root, l'invite de shell affiche '**#**' (si vous utilisez **bash** et que vous n'avez pas personnalisé l'invite, comme nous l'avons discuté précédemment). Cette convention est destinée à servir d'avertissement quant au pouvoir absolu de ce compte.

### Opérations nécessitant des privilèges root

Les privilèges root sont nécessaires pour effectuer des opérations telles que :

* Création, suppression et gestion de comptes utilisateurs
* Gestion des paquets logiciels
* Suppression ou modification de fichiers système
* Redémarrage des services système.

Les utilisateurs réguliers des distributions Linux peuvent être autorisés à installer des paquets logiciels, mettre à jour certains paramètres, utiliser certains périphériques, et appliquer divers types de modifications au système. Cependant, les privilèges root sont nécessaires pour effectuer des tâches d'administration telles que le redémarrage de la plupart des services, l'installation manuelle de paquets et la gestion de parties du système de fichiers qui sont en dehors des répertoires de l'utilisateur normal.

![Image](https://courses.edx.org/assets/courseware/v1/aee73bd08cabfc1b26a7f7927df8317d/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch018_screen8.jpg)
_Opérations nécessitant des privilèges root_

### Opérations ne nécessitant pas de privilèges root

Un utilisateur de compte régulier peut effectuer certaines opérations nécessitant des permissions spéciales ; cependant, la configuration du système doit permettre l'exercice de telles capacités.

**SUID** (**S**et owner **U**ser **ID** upon execution - similaire à la fonctionnalité "exécuter en tant que" de Windows) est un type spécial de permission de fichier accordé à un fichier. L'utilisation de SUID fournit des permissions temporaires à un utilisateur pour exécuter un programme avec les permissions du propriétaire du fichier (qui peut être root) au lieu des permissions détenues par l'utilisateur.

Le tableau fournit des exemples d'opérations qui ne nécessitent pas de privilèges root :

<table border="0" align="center" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 849.594px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td width="45%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Opérations ne nécessitant pas de privilèges root</strong></span></td><td width="45%" align="center" bgcolor="#003f60" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">Exemples de cette opération</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Exécution d'un client réseau</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Partage d'un fichier sur le réseau</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Utilisation de périphériques tels que les imprimantes</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Impression sur le réseau</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Opérations sur les fichiers auxquels l'utilisateur a les permissions d'accès appropriées</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Accès aux fichiers auxquels vous avez accès ou partage de données sur le réseau</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Exécution d'applications SUID-root</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Exécution de programmes tels que <span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;"><span style="color: inherit; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; font-size: 16px; line-height: 1.4em; font-family: &quot;courier new&quot;, courier;">passwd</span></strong></span></td></tr></tbody></table>

### Comparaison de sudo et su

Dans Linux, vous pouvez utiliser **su** ou **sudo** pour accorder temporairement l'accès root à un utilisateur normal. Cependant, ces méthodes sont en réalité assez différentes. Voici les différences entre les deux commandes :

<table border="0" style="border-collapse: collapse; border-spacing: 0px; table-layout: auto; word-break: normal; line-height: 1.4em; width: 944px; margin: 20px auto; font-size: 16px; color: rgb(34, 34, 34); font-family: Inter, &quot;Helvetica Neue&quot;, Arial, sans-serif; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; border: 2px solid white;"><tbody style="line-height: 1.4em;"><tr style="line-height: 1.4em;"><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">su</strong></span></td><td align="center" bgcolor="#003f60" width="50%" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px; border: 2px solid white; font-size: 16px;"><span style="color: rgb(255, 255, 255); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; font-size: inherit; line-height: 1.4em; font-family: inherit;"><strong style="font-weight: bold; line-height: 1.4em;">sudo</strong></span></td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Lorsque vous élevez les privilèges, vous devez entrer le mot de passe root. Donner le mot de passe root à un utilisateur normal ne devrait jamais, jamais être fait.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Lorsque vous élevez les privilèges, vous devez entrer le mot de passe de l'utilisateur et non le mot de passe root.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Une fois qu'un utilisateur élève ses privilèges au compte root en utilisant <strong style="font-weight: bold; line-height: 1.4em;">su</strong>, l'utilisateur peut faire tout ce que l'utilisateur root peut faire aussi longtemps qu'il le souhaite, sans être demandé à nouveau pour un mot de passe.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">Offre plus de fonctionnalités et est considéré comme plus sécurisé et plus configurable. Exactement ce que l'utilisateur est autorisé à faire peut être précisément contrôlé et limité. Par défaut, l'utilisateur devra soit toujours continuer à donner son mot de passe pour effectuer d'autres opérations avec <strong style="font-weight: bold; line-height: 1.4em;">sudo</strong>, soit pourra éviter de le faire pendant un intervalle de temps configurable.</td></tr><tr style="line-height: 1.4em;"><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">La commande a des fonctionnalités de journalisation limitées.</td><td bgcolor="#e8e8e8" style="vertical-align: top; line-height: 1.4em; margin: 20px 0px; padding: 10px 10px 10px 15px; border: 2px solid white; font-size: 16px;">La commande a des fonctionnalités de journalisation détaillées.</td></tr></tbody></table>

### Fonctionnalités de sudo

**sudo** a la capacité de suivre les tentatives infructueuses d'obtention de l'accès root. L'autorisation des utilisateurs pour utiliser **sudo** est basée sur les informations de configuration stockées dans le fichier **/etc/sudoers** et dans le répertoire **/etc/sudoers.d**.

Un message tel que le suivant apparaîtrait dans un fichier journal du système (généralement **/var/log/secure**) lors de la tentative d'exécution de **sudo** pour **badperson** sans authentification réussie de l'utilisateur :

**badperson : utilisateur non dans sudoers ; TTY=pts/4 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/tail secure**

![Fonctionnalités de sudo](https://courses.edx.org/assets/courseware/v1/221b78f7941bfa4846b7253289053ded/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch18_screen14b.jpg)
_Fonctionnalités de sudo_

### Le fichier sudoers

Chaque fois que **sudo** est invoqué, un déclencheur regardera **/etc/sudoers** et les fichiers dans **/etc/sudoers.d** pour déterminer si l'utilisateur a le droit d'utiliser **sudo** et quelle est l'étendue de ses privilèges. Les demandes d'utilisateurs inconnus et les demandes d'effectuer des opérations non autorisées pour l'utilisateur, même avec **sudo**, sont signalées. La structure de base des entrées dans ces fichiers est :

**qui où = (en tant que qui) quoi**

**/etc/sudoers** contient beaucoup de documentation sur la manière de le personnaliser. La plupart des distributions Linux préfèrent maintenant que vous ajoutiez un fichier dans le répertoire **/etc/sudoers.d** avec un nom identique à celui de l'utilisateur. Ce fichier contient la configuration **sudo** de l'utilisateur individuel, et il faut laisser le fichier de configuration principal intact sauf pour les modifications qui affectent tous les utilisateurs.

Vous devez éditer l'un de ces fichiers de configuration en utilisant **visudo**, qui garantit qu'une seule personne édite le fichier à la fois, a les permissions appropriées, et refuse d'écrire le fichier et de quitter s'il y a des erreurs de syntaxe dans les modifications apportées. L'édition peut être accomplie en exécutant une commande telle que les suivantes :

**# visudo /etc/sudoers**  
**# visudo -f /etc/sudoers.d/student**

L'éditeur spécifique réellement invoqué dépendra du paramétrage de votre variable d'environnement **EDITOR**.

![Le fichier sudoers](https://courses.edx.org/assets/courseware/v1/be9e3859dfc9da162c2aee89c1bb83f3/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sudoerssuse.png)
_Le fichier sudoers_

### Journalisation des commandes

Par défaut, les commandes **sudo** et les échecs sont journalisés dans **/var/log/auth.log** sous la famille de distributions Debian, et dans **/var/log/messages** et/ou **/var/log/secure** sur d'autres systèmes. Il s'agit d'une sauvegarde importante pour permettre le suivi et la responsabilité de l'utilisation de **sudo**. Une entrée typique du message contient :

* Nom d'utilisateur appelant
* Informations sur le terminal
* Répertoire de travail
* Compte utilisateur invoqué
* Commande avec arguments

L'exécution d'une commande telle que **sudo whoami** entraîne une entrée dans le fichier journal telle que :

**Dec 8 14:20:47 server1 sudo: op : TTY=pts/6 PWD=/var/log USER=root COMMAND=/usr/bin/whoami**

![Image](https://courses.edx.org/assets/courseware/v1/e391446157bf3f88641e613c9e2a55f0/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/varlogsecure.png)
_Journalisation des commandes_

### Isolation des processus

Linux est considéré comme plus sécurisé que de nombreux autres systèmes d'exploitation car les processus sont naturellement isolés les uns des autres. Un processus ne peut normalement pas accéder aux ressources d'un autre processus, même lorsque ce processus s'exécute avec les mêmes privilèges utilisateur. Linux rend ainsi difficile (bien que certainement pas impossible) pour les virus et les exploits de sécurité d'accéder et d'attaquer des ressources aléatoires sur un système.

Des mécanismes de sécurité supplémentaires plus récents qui limitent encore davantage les risques incluent :

* Groupes de contrôle (cgroups)  
Permet aux administrateurs système de regrouper des processus et d'associer des ressources finies à chaque cgroup.
* Conteneurs  
Permet d'exécuter plusieurs systèmes Linux isolés (conteneurs) sur un seul système en s'appuyant sur les cgroups.
* Virtualisation  
Le matériel est émulé de manière à ce que non seulement les processus puissent être isolés, mais que des systèmes entiers soient exécutés simultanément en tant qu'invités isolés et protégés (machines virtuelles) sur un seul hôte physique.

![Isolation des processus](https://courses.edx.org/assets/courseware/v1/ab1acbfb43d22b02e75c9a7f46e50c27/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch18_screen18.jpg)
_Isolation des processus_

### Accès aux périphériques matériels

Linux limite l'accès des utilisateurs aux périphériques matériels non réseau de manière extrêmement similaire à l'accès aux fichiers réguliers. Les applications interagissent en engageant la couche du système de fichiers (qui est indépendante du périphérique ou du matériel réel sur lequel le fichier réside). Cette couche ouvrira ensuite un fichier spécial de périphérique (souvent appelé nœud de périphérique) sous le répertoire **/dev** qui correspond au périphérique auquel on accède. Chaque fichier spécial de périphérique possède des champs standard de propriétaire, de groupe et de permissions mondiales. La sécurité est naturellement appliquée de la même manière que lors de l'accès à des fichiers standard.

Les disques durs, par exemple, sont représentés comme **/dev/sd***. Alors qu'un utilisateur root peut lire et écrire sur le disque de manière brute, par exemple, en faisant quelque chose comme :

**# echo hello world > /dev/sda1**

Les permissions standard, comme montré dans la figure, rendent impossible pour les utilisateurs réguliers de le faire. Écrire sur un périphérique de cette manière peut facilement oblitérer le système de fichiers stocké sur celui-ci d'une manière qui ne peut pas être réparée sans grand effort, si tant est que ce soit possible. La lecture et l'écriture normales de fichiers sur le disque dur par les applications sont effectuées à un niveau supérieur via le système de fichiers, et jamais via un accès direct au nœud de périphérique.

![Accès aux périphériques matériels](https://courses.edx.org/assets/courseware/v1/f329a3cc179860717d2d0252d7a2a8c2/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/lsdevsdcentos.png)
_Accès aux périphériques matériels_

### Rester à jour

Lorsque des problèmes de sécurité dans le noyau Linux ou les applications et bibliothèques sont découverts, les distributions Linux ont un bon historique de réaction rapide et de diffusion de correctifs à tous les systèmes en mettant à jour leurs dépôts de logiciels et en envoyant des notifications pour mettre à jour immédiatement. La même chose est vraie pour les correctifs de bugs et les améliorations de performance qui ne sont pas liées à la sécurité.

![Mise à jour rapide du système](https://courses.edx.org/assets/courseware/v1/5e74db8d93ac146d9d1fdcbf8b1c9a05/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch018_screen20.jpg)

Cependant, il est bien connu que de nombreux systèmes ne sont pas mis à jour suffisamment fréquemment et que des problèmes déjà résolus sont autorisés à rester sur les ordinateurs pendant une longue période ; cela est particulièrement vrai avec les systèmes d'exploitation propriétaires où les utilisateurs sont soit mal informés, soit méfiants à l'égard de la politique de correctifs du vendeur, car parfois les mises à jour peuvent causer de nouveaux problèmes et interrompre les opérations existantes. Beaucoup des vecteurs d'attaque les plus réussis proviennent de l'exploitation de failles de sécurité pour lesquelles des correctifs sont déjà connus mais pas universellement déployés.

La meilleure pratique est donc de tirer parti du mécanisme de votre distribution Linux pour les mises à jour automatiques et de ne jamais les reporter. Il est extrêmement rare qu'une telle mise à jour cause de nouveaux problèmes.

### Comment les mots de passe sont stockés

Le système vérifie l'authenticité et l'identité en utilisant les identifiants de l'utilisateur.

À l'origine, les mots de passe chiffrés étaient stockés dans le fichier **/etc/passwd**, qui était lisible par tout le monde. Cela rendait assez facile le piratage des mots de passe.

![Comment les mots de passe sont stockés](https://courses.edx.org/assets/courseware/v1/d8b630982847322e8a30865f4af85767/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch18_screen21.jpg)

**Comment les mots de passe sont stockés**

Sur les systèmes modernes, les mots de passe sont en réalité stockés dans un format chiffré dans un fichier secondaire nommé **/etc/shadow**. Seuls ceux ayant un accès root peuvent lire ou modifier ce fichier.

### Algorithme de mot de passe

Protéger les mots de passe est devenu un élément crucial de la sécurité. La plupart des distributions Linux s'appuient sur un algorithme moderne de chiffrement des mots de passe appelé SHA-512 (Secure Hashing Algorithm 512 bits), développé par la National Security Agency (NSA) des États-Unis pour chiffrer les mots de passe.

L'algorithme SHA-512 est largement utilisé pour les applications et protocoles de sécurité. Ces applications et protocoles de sécurité incluent TLS, SSL, PHP, SSH, S/MIME et IPSec. SHA-512 est l'un des algorithmes de hachage les plus testés.

Par exemple, si vous souhaitez expérimenter avec le codage SHA-512, le mot "test" peut être codé en utilisant le programme **sha512sum** pour produire la forme SHA-512 (voir le graphique) :

![Chiffrement des mots de passe : sha512sum](https://courses.edx.org/assets/courseware/v1/2b48e41c1608e121d66b9dbaf424a6c6/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/sha512rhel7.png)
_Chiffrement des mots de passe : sha512sum_

### Bonnes pratiques pour les mots de passe

Les professionnels de l'informatique suivent plusieurs bonnes pratiques pour sécuriser les données et le mot de passe de chaque utilisateur.

* Le vieillissement des mots de passe est une méthode pour s'assurer que les utilisateurs reçoivent des rappels pour créer un nouveau mot de passe après une période spécifique. Cela peut garantir que les mots de passe, s'ils sont piratés, ne seront utilisables que pendant une durée limitée. Cette fonctionnalité est implémentée en utilisant **chage**, qui configure les informations d'expiration du mot de passe pour un utilisateur.
* Une autre méthode consiste à forcer les utilisateurs à définir des mots de passe robustes en utilisant les **M**odules **d'****A**uthentification **P**luggables (**PAM**). PAM peut être configuré pour vérifier automatiquement qu'un mot de passe créé ou modifié en utilisant l'utilitaire **passwd** est suffisamment robuste. La configuration de PAM est implémentée en utilisant une bibliothèque appelée **pam_cracklib.so**, qui peut également être remplacée par **pam_passwdqc.so** pour tirer parti de plus d'options.
* On peut également installer des programmes de piratage de mots de passe, tels que [John The Ripper](http://www.openwall.com/john/), pour sécuriser le fichier de mots de passe et détecter les entrées de mots de passe faibles. Il est recommandé d'obtenir une autorisation écrite avant d'installer de tels outils sur tout système que vous ne possédez pas.

![Utilisation de chage](https://courses.edx.org/assets/courseware/v1/0ccd66e7a1088ab8450cac69aa9918fb/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/chagesuse.png)
_Utilisation de chage_

### Exigence de mots de passe pour le chargeur de démarrage

Vous pouvez sécuriser le processus de démarrage avec un mot de passe sécurisé pour empêcher quelqu'un de contourner l'étape d'authentification de l'utilisateur. Cela peut fonctionner en conjonction avec la protection par mot de passe pour le BIOS. Notez que bien que l'utilisation d'un mot de passe de chargeur de démarrage seul empêchera un utilisateur de modifier la configuration du chargeur de démarrage pendant le processus de démarrage, cela **n'**empêchera **pas** un utilisateur de démarrer à partir d'un média de démarrage alternatif tel que des disques optiques ou des clés USB. Ainsi, il doit être utilisé avec un mot de passe BIOS pour une protection complète.

![Panneau indiquant : Mot de passe requis](https://courses.edx.org/assets/courseware/v1/e74988af521d832ff71a899660352371/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/password.png)

Pour l'ancienne méthode de démarrage GRUB 1, il était relativement facile de définir un mot de passe pour **grub**. Cependant, pour la version GRUB 2, les choses sont devenues plus compliquées. Cependant, vous avez plus de flexibilité et pouvez tirer parti de fonctionnalités plus avancées, telles que des mots de passe spécifiques à l'utilisateur (qui peuvent être leurs mots de passe de connexion normaux).

De plus, vous ne modifiez jamais directement **grub.cfg** ; au lieu de cela, vous pouvez modifier les fichiers de configuration dans **/etc/grub.d** et **/etc/defaults/grub**, puis exécuter **update-grub**, ou `**grub2-mkconfig**` et enregistrer le nouveau fichier de configuration.

Pour en savoir plus, lisez l'article suivant : _["GRUB 2 Password Protection"](https://help.ubuntu.com/community/Grub2/Passwords)_.

### Vulnérabilité matérielle

Lorsque le matériel est physiquement accessible, la sécurité peut être compromise par :

* Enregistrement des frappes  
Enregistrement de l'activité en temps réel d'un utilisateur d'ordinateur, y compris les touches qu'il presse. Les données capturées peuvent être stockées localement ou transmises à des machines distantes.
* Reniflage du réseau  
Capture et visualisation des données au niveau des paquets réseau sur votre réseau.
* Démarrage avec un disque live ou de secours
* Remontage et modification du contenu du disque.

Votre politique de sécurité informatique doit commencer par des exigences sur la manière de sécuriser correctement l'accès physique aux serveurs et aux postes de travail. L'accès physique à un système permet aux attaquants de tirer facilement parti de plusieurs vecteurs d'attaque, de manière à rendre toutes les recommandations au niveau du système d'exploitation irrelevantes.

Les directives de sécurité sont :

* Verrouillez les postes de travail et les serveurs.
* Protégez vos liens réseau de sorte qu'ils ne puissent pas être accessibles par des personnes en qui vous n'avez pas confiance.
* Protégez vos claviers où les mots de passe sont saisis pour vous assurer que les claviers ne peuvent pas être manipulés.
* Assurez-vous qu'un mot de passe protège le BIOS de manière à ce que le système ne puisse pas être démarré avec un DVD ou une clé USB live ou de secours.

Pour les ordinateurs à utilisateur unique et ceux dans un environnement domestique, certaines des fonctionnalités ci-dessus (comme empêcher le démarrage à partir de supports amovibles) peuvent être excessives, et vous pouvez éviter de les implémenter. Cependant, si des informations sensibles se trouvent sur votre système et nécessitent une protection minutieuse, soit elles ne devraient pas s'y trouver, soit elles devraient être mieux protégées en suivant les directives ci-dessus.

![Vulnérabilité matérielle](https://courses.edx.org/assets/courseware/v1/a45dcc426b70817110e0d810f4df83a7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/LFS01_ch18_screen27.jpg)
_Vulnérabilité matérielle_

### Vulnérabilité logicielle

Comme tous les logiciels, les pirates trouvent parfois des faiblesses dans l'écosystème Linux. La force de Linux (et de la communauté open source en général) réside dans la rapidité avec laquelle ces vulnérabilités sont exposées et corrigées. La couverture spécifique des vulnérabilités dépasse le cadre de ce cours, mais le tableau de discussion peut être utilisé pour poursuivre la discussion.

![Pingouin de dessin animé ouvrant la porte](https://courses.edx.org/assets/courseware/v1/3ece571940430dd1c4cef1bcacfbc8c7/asset-v1:LinuxFoundationX+LFS101x+2T2021+type@asset+block/soft_vuln.png)

## Résumé du chapitre

Vous avez terminé le chapitre 18. Résumons les concepts clés abordés :

* Le compte root a autorité sur l'ensemble du système.
* Les privilèges root peuvent être nécessaires pour des tâches telles que le redémarrage des services, l'installation manuelle de paquets et la gestion de parties du système de fichiers qui sont en dehors de votre répertoire personnel.
* Pour effectuer des opérations privilégiées telles que des modifications système, vous devez utiliser soit **su**, soit **sudo**.
* Les appels à **sudo** déclenchent une recherche dans le fichier **/etc/sudoers** ou dans le répertoire **/etc/sudoers.d**, qui valide d'abord que l'utilisateur appelant est autorisé à utiliser **sudo** et qu'il est utilisé dans le cadre autorisé.
* L'une des fonctionnalités les plus puissantes de **sudo** est sa capacité à journaliser les tentatives infructueuses d'obtention de l'accès root. Par défaut, les commandes **sudo** et les échecs sont journalisés dans **/var/log/auth.log** sous la famille Debian et **/var/log/messages** dans les autres familles de distributions.
* Un processus ne peut pas accéder aux ressources d'un autre processus, même lorsque ce processus s'exécute avec les mêmes privilèges utilisateur.
* En utilisant les identifiants de l'utilisateur, le système vérifie l'authenticité et l'identité.
* L'algorithme SHA-512 est généralement utilisé pour encoder les mots de passe. Ils peuvent être chiffrés, mais pas déchiffrés.
* Les modules d'authentification pluggables (PAM) peuvent être configurés pour vérifier automatiquement que les mots de passe créés ou modifiés à l'aide de l'utilitaire **passwd** sont suffisamment robustes (ce qui est considéré comme suffisamment robuste peut également être configuré).
* Votre politique de sécurité informatique doit commencer par des exigences sur la manière de sécuriser correctement l'accès physique aux serveurs et aux postes de travail.
* Maintenir vos systèmes à jour est une étape importante pour éviter les attaques de sécurité.