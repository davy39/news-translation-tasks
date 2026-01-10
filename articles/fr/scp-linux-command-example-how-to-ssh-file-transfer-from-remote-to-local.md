---
title: Commande SCP Linux – Comment transférer des fichiers SSH d'un serveur distant
  vers un serveur local
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2021-09-21T21:41:38.000Z'
originalURL: https://freecodecamp.org/news/scp-linux-command-example-how-to-ssh-file-transfer-from-remote-to-local
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/uide-to-writting-a-good-readme-file--3-.png
tags:
- name: File sharing
  slug: file-sharing
- name: information security
  slug: information-security
- name: Linux
  slug: linux
seo_title: Commande SCP Linux – Comment transférer des fichiers SSH d'un serveur distant
  vers un serveur local
seo_desc: 'Whenever you''re working with computers or any electronic device that has
  storage capacity, you might need to distribute or share information and files in
  various ways.

  Some of the most commonly shared files include audio files, images, videos, pdfs
  o...'
---

Lorsque vous travaillez avec des ordinateurs ou tout appareil électronique disposant d'une capacité de stockage, vous pourriez avoir besoin de distribuer ou de partager des informations et des fichiers de diverses manières.

Certains des fichiers les plus couramment partagés incluent des fichiers audio, des images, des vidéos, des PDF ou toute forme de documents texte.

La plupart du temps, les informations partagées seront privées ou confidentielles – ce qui signifie qu'elles sont destinées à une personne spécifique ou à un groupe de personnes, il est donc essentiel de les protéger.

En ce qui concerne les appareils comme les téléphones mobiles, nous avons des applications qui facilitent le transfert de fichiers comme Xender, AppShare ou même parfois l'utilisation du Bluetooth. Maintenant, en ce qui concerne les ordinateurs, le cas n'est pas différent, nous avons des logiciels et même des sites qui facilitent la même chose.

En ce qui concerne le partage de données dans des systèmes d'exploitation comme Linux, il existe plusieurs commandes parmi lesquelles vous pouvez choisir pour partager des informations. Mais aujourd'hui, nous allons nous concentrer sur la commande **SCP**. Elle vous permet de partager des fichiers et des données de manière sécurisée et facile.

Dans le marché actuel, avoir des compétences en Linux est très essentiel et utile, surtout si vous êtes administrateur système. En tant qu'administrateur système, le partage de données fera partie de vos activités quotidiennes et vous aurez besoin que les données partagées soient sûres, et en utilisant la commande SCP, vous pourrez y parvenir.

Avant de commencer, commençons par comprendre ce qu'est SCP, puis nous apprendrons quelques commandes que vous pouvez utiliser pour le transfert de fichiers.

## Qu'est-ce que les commandes SCP ?

SCP est l'acronyme de Secure Copy Protocol. C'est un utilitaire en ligne de commande qui permet à l'utilisateur de copier des fichiers et des répertoires de manière sécurisée entre deux emplacements, généralement entre des systèmes Unix ou Linux.

Le protocole garantit que la transmission des fichiers est cryptée pour empêcher toute personne ayant des intentions suspectes d'obtenir des informations sensibles.

En termes plus simples, nous pouvons dire que SCP est une option plus sûre pour la commande `cp` (_copy_).

Il est également important de noter que SCP utilise le cryptage via une connexion SSH (Secure Shell), ce qui garantit que les données transférées sont protégées contre les attaques suspectes.

## Syntaxe de SCP

Tout comme les autres commandes utilisées dans le terminal, SCP a également un format utilisé pour une exécution réussie. En comprenant la syntaxe, il est plus facile pour vous d'écrire les commandes :

```bash
scp [OPTIONS] [[user@]src_host:]file1 [[user@]dest_host:]file2
```

* `scp` - Initialise la commande et assure qu'un shell sécurisé est en place.
* `OPTIONS` - Elles accordent différentes permissions selon leur utilisation. Certaines des options les plus courantes incluent :
* **P** (majuscule) - spécifie le port pour établir la connexion avec l'hôte distant.
* **p** (minuscule) - préserve les horodatages pour faciliter la modification et l'accès.
* **r** - copie l'ensemble du répertoire de manière récursive.
* **q** - copie les fichiers en mode silencieux, n'affiche pas les messages de progression. Également connu sous le nom de mode silencieux.
* **C** - pour la compression des données pendant la transmission.
Pour en savoir plus sur les OPTIONS, lisez [scp options](https://linux.die.net/man/1/scp)
* `src_host` - où le fichier est hébergé. La source peut être un client ou un serveur selon l'origine du fichier.
* `dest_host` - où le fichier sera copié.

Puisque nous traitons de la transmission de fichiers, cela signifie définitivement qu'il doit y avoir l'implication de plus d'une machine pour rendre le processus possible. Nous pouvons utiliser SCP dans les cas suivants :

* Copier des fichiers au sein de la même machine.
* Copier des fichiers d'un hôte local vers un hôte distant et vice versa.
* Copier des fichiers entre deux serveurs distants différents.

À ce stade, il sera juste de préciser que, avant d'utiliser des commandes SCP, vous devrez avoir quelques éléments en place :

* SSH installé sur les machines client et serveur.
* Accès root aux machines client et serveur.

Avec ces deux éléments prêts, vous pouvez commencer. Commençons par voir les commandes en action.

## Commandes SCP courantes

### Copier un fichier d'un hôte local vers un serveur distant

Lors de la copie de fichiers, pouvoir transférer des fichiers/données du stockage local vers un serveur distant est très essentiel. Lorsque vous utilisez les commandes SCP, vous devrez spécifier quelques éléments pour que cela se produise.

Vous devrez spécifier le chemin vers le fichier en tant que source et également spécifier le chemin de l'hôte distant, où les fichiers sont copiés.

Prenons un scénario où nous avons un fichier `test.txt` et nous devons le copier sur un serveur distant, notre commande ressemblera à ceci :

```
scp test.txt userbravo@destination:/location2
```

Nous ne sommes pas limités au nombre de fichiers que nous pouvons copier. Supposons que nous sommes sur notre bureau dans le dossier appelé web où nous avons des extensions de fichiers `.php` et que nous devons les copier dans le répertoire personnel du serveur distant. Notre commande ressemblera à ceci :

```
scp *.php userbravo@destination_host:/~/
```

***.php** - copie tous les fichiers avec l'extension .php dans le dossier actuellement spécifié.
**/~/** - signifie les copier dans le répertoire personnel.

Supposons que vous souhaitiez copier un fichier nommé test.txt et l'enregistrer avec un nom différent dans le serveur distant, cette fois-ci en utilisant une option de port. La commande sera :

```
scp -P 8080 test.txt userbravo@destination_host:/user/home/test2.txt
```

Dans cet exemple, nous avons copié un fichier test.txt de la machine locale vers un serveur distant où il sera enregistré sous le nom test2.txt en utilisant le port 8080.

### Copier des fichiers d'un serveur distant vers un serveur local

Une meilleure façon de comprendre cela est d'utiliser un exemple. Prenons un scénario où vous souhaitez copier des fichiers depuis un système distant. Pour copier les fichiers, vous devrez d'abord invoquer SCP, suivi du nom d'utilisateur distant@adresse IP, du chemin vers le fichier.

Si vous ne spécifiez pas le chemin, il est supposé par défaut dans ce cas, qui sera le répertoire personnel de l'utilisateur, cela sera suivi du chemin où le fichier sera stocké localement.

**La Syntaxe**

```
scp <remote_username>@<IPorHost>:<PathToFile>   <LocalFileLocation>
```

Supposons que je souhaite copier un fichier nommé _linuxcheatsheet_ depuis l'appareil distant avec cette adresse _192.168.1.100_.

Le fichier _linuxcheatsheet_ est stocké dans le répertoire personnel de l'utilisateur kali, l'utilisateur que j'authentifierai. Par conséquent, après le deux-points, je n'ai pas besoin de spécifier le chemin car c'est celui par défaut, qui est le répertoire personnel, et je tape simplement le nom du fichier (« linuxcheatsheet »). Ensuite, je spécifie le répertoire actuel comme emplacement local pour stocker le fichier en tapant un point.

```
scp lary@192.168.1.100:linuxcheatsheet .
```

### Copier des fichiers d'un hôte distant vers un autre

La beauté de l'utilisation de SCP dans le transfert de fichiers est qu'il ne permet pas seulement la connexion entre des machines locales, mais il permet également de se connecter à des serveurs distants.

Supposons que nous voulions copier un fichier nommé test.txt vers un autre serveur distant, la commande ressemblerait à ceci :

```
scp user1@host1.com:/files/test.txt user2@host2.com:/files
```

Ce que cette commande fera est de copier test.txt du dossier files dans user1 et de créer une réplique dans user2 qui s'exécute sur _host2.com_, toujours dans le dossier files.

### Copier plusieurs fichiers

Lors de la copie de plusieurs fichiers, tout ce que vous avez à faire est de spécifier le nom du fichier en tant que chemin source. Par exemple.

**La Syntaxe**

```
scp file1 file2 ... user@<ip_address_of_user>: Destination
```

Supposons que nous voulions copier les fichiers 1, 2, 3 et 4. La commande ressemblerait à ceci :

```
scp file1.txt file2.txt file3.txt file4.txt user1@host1.com:/home/user1/Desktop
```

## Points à retenir :

* Pour pouvoir copier des fichiers, vous devez avoir des permissions de lecture sur le fichier source et des permissions d'écriture sur le système cible.
* La commande SCP repose sur SSH pour un transfert de données sécurisé, ce qui signifie qu'elle nécessite un mot de passe pour s'authentifier sur les systèmes distants.
* Faites attention lors de la copie de fichiers avec le même nom et le même emplacement, car SCP les écrasera sans vous avertir.
* Pour pouvoir distinguer les emplacements locaux et distants, utilisez le deux-points complet **: **.

## Conclusion

Que vous soyez ingénieur support, administrateur système, ou même un développeur en croissance comme moi qui utilise Linux ou souhaite l'apprendre – il est probable que vous devrez transférer des fichiers à un moment donné. Et connaître ces commandes SCP simples sera utile.

Dans cet article, nous avons couvert certains des scénarios les plus courants où vous pourriez vouloir utiliser SCP et, espérons-le, vous avez appris quelque chose de nouveau.

Bonne programmation ❤