---
title: Comment utiliser un script Bash pour gérer le téléchargement et la visualisation
  de fichiers depuis un bucket AWS S3
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-03-02T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/bash-script-download-view-from-s3-bucket
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/code-coding-computer-data-574077.jpg
tags:
- name: Bash
  slug: bash
- name: Linux
  slug: linux
- name: Script
  slug: script
seo_title: Comment utiliser un script Bash pour gérer le téléchargement et la visualisation
  de fichiers depuis un bucket AWS S3
seo_desc: "As you can read in this article, I recently had some trouble with my email\
  \ server and decided to outsource email administration to Amazon's Simple Email\
  \ Service (SES). \nThe problem with that solution was that I had SES save new messages\
  \ to an S3 buck..."
---

Comme vous pouvez le [lire dans cet article](https://www.freecodecamp.org/news/aws-simple-email-service-email-server/), j'ai récemment eu des problèmes avec mon serveur de messagerie et j'ai décidé d'externaliser l'administration des e-mails vers le service Amazon Simple Email Service (SES).

Le problème avec cette solution était que j'avais configuré SES pour sauvegarder les nouveaux messages dans un bucket S3, et l'utilisation de la console de gestion AWS pour lire les fichiers dans les buckets S3 devient rapidement fastidieuse.

J'ai donc décidé d'écrire un script Bash pour automatiser le processus de téléchargement, de stockage approprié et de visualisation des nouveaux messages.

Bien que j'aie écrit ce script pour l'utiliser sur mon bureau Ubuntu Linux, il ne nécessiterait pas trop de modifications pour fonctionner sur un système macOS ou Windows 10 via [Windows SubSystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

Voici le script complet en une seule partie. Après avoir pris quelques instants pour l'examiner, je vais vous le détailler étape par étape.

```bash
#!/bin/bash
# Récupérer les nouveaux messages depuis S3 et les sauvegarder dans le répertoire tmpemails/ :
aws s3 cp \
   --recursive \
   s3://bucket-name/ \
   /home/david/s3-emails/tmpemails/  \
   --profile myaccount

# Définir les variables de localisation :
tmp_file_location=/home/david/s3-emails/tmpemails/*
base_location=/home/david/s3-emails/emails/

# Créer un nouveau répertoire pour stocker les messages du jour :
today=$(date +"%m_%d_%Y")
[[ -d ${base_location}/"$today" ]] || mkdir ${base_location}/"$today"

# Donner aux fichiers de messages des noms lisibles :
for FILE in $tmp_file_location
do
   mv $FILE ${base_location}/${today}/email$(rand)
done

# Ouvrir les nouveaux fichiers dans Gedit :
for NEWFILE in ${base_location}/${today}/*
do
   gedit $NEWFILE
done
```

Nous commencerons par la commande unique pour télécharger les messages actuellement présents dans mon bucket S3 (au fait, j'ai changé les noms du bucket et autres détails de système de fichiers et d'authentification pour protéger ma vie privée).

```bash
aws s3 cp \
   --recursive \
   s3://bucket-name/ \
   /home/david/s3-emails/tmpemails/  \
   --profile myaccount
```

Bien sûr, cela ne fonctionnera que si vous avez déjà installé et configuré l'AWS CLI pour votre système local. C'est le moment [de le faire](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) si ce n'est pas déjà fait.

La commande _cp_ signifie "copier", _--recursive_ indique à la CLI d'appliquer l'opération même à plusieurs objets, _s3://bucket-name_ pointe vers mon bucket (le nom de votre bucket sera évidemment différent), la ligne /home/david... est l'adresse absolue du système de fichiers vers laquelle je souhaite que les messages soient copiés, et l'argument _--profile_ indique à la CLI lequel de mes multiples comptes AWS je référence.

La section suivante définit deux variables qui me faciliteront grandement la spécification des emplacements du système de fichiers tout au long du script.

```bash
tmp_file_location=/home/david/s3-emails/tmpemails/*
base_location=/home/david/s3-emails/emails/
```

Remarquez comment la valeur de la variable _tmp_file_location_ se termine par un astérisque. C'est parce que je veux faire référence aux _fichiers dans_ ce répertoire, plutôt qu'au répertoire lui-même.

Je vais créer un nouveau répertoire permanent dans la hiérarchie .../emails/ pour faciliter la recherche de messages plus tard. Le nom de ce nouveau répertoire sera la date actuelle.

```bash
today=$(date +"%m_%d_%Y")
[[ -d ${base_location}/"$today" ]] || mkdir ${base_location}/"$today"
```

Je commence par créer une nouvelle variable shell nommée _today_ qui sera remplie par la sortie de la commande _date +"%m_%d_%Y"_. _date_ elle-même produit la date/horodatage complet, mais ce qui suit (_"%m_%d_%Y"_) édite cette sortie pour un format plus simple et plus lisible.

Je teste ensuite l'existence d'un répertoire utilisant ce nom - ce qui indiquerait que j'ai déjà reçu des e-mails ce jour-là et, par conséquent, qu'il n'est pas nécessaire de recréer le répertoire. Si un tel répertoire n'existe _pas_ (||), alors _mkdir_ le créera pour moi. Si vous n'exécutez pas ce test, votre commande pourrait retourner des messages d'erreur ennuyeux.

Puisque Amazon SES donne des noms laids et illisibles à chacun des messages qu'il dépose dans mon bucket S3, je vais maintenant les renommer dynamiquement tout en les déplaçant vers leur nouvel emplacement (dans le répertoire daté que je viens de créer).

```bash
for FILE in $tmp_file_location
do
   mv $FILE ${base_location}/${today}/email$(rand)
done
```

La boucle _for...do...done_ lira chacun des fichiers dans le répertoire représenté par la variable _$tmp_file_location_ puis le déplacera vers le répertoire que je viens de créer (représenté par la variable _$base_location_ en plus de la valeur actuelle de $_today_).

Dans le cadre de la même opération, je lui donnerai son nouveau nom, la chaîne "_email_" suivie d'un nombre aléatoire généré par la commande _rand_. Vous devrez peut-être installer un générateur de nombres aléatoires : ce sera _apt install rand_ sur Ubuntu.

Une version antérieure du script créait des noms différenciés par des nombres séquentiels plus courts qui étaient incrémentés en utilisant une logique _count=1...count=$((count+1))_ dans la boucle _for_. Cela fonctionnait bien tant que je ne recevais pas plus d'un lot de messages le même jour. Si c'était le cas, les nouveaux messages écraseraient les anciens fichiers dans le répertoire de ce jour.

Je suppose qu'il est mathématiquement possible que ma commande _rand_ puisse attribuer des nombres qui se chevauchent à deux fichiers, mais étant donné que la plage par défaut utilisée par _rand_ est comprise entre 1 et 32 576, c'est un risque que je suis prêt à prendre.

À ce stade, il devrait y avoir des fichiers dans le nouveau répertoire avec des noms comme email3039, email25343, etc. pour chacun des nouveaux messages que j'ai reçus.

L'exécution de la commande _tree_ sur mon propre système me montre que cinq messages ont été sauvegardés dans mon répertoire 02_27_2020, et un de plus dans 02_28_2020 (ces fichiers ont été générés en utilisant l'ancienne version de mon script, donc ils sont numérotés séquentiellement).

Il n'y a actuellement aucun fichier dans _tmpemails -_ c'est parce que la commande mv déplace les fichiers vers leur nouvel emplacement, sans laisser de trace.

```bash
$ tree
.
├── emails
│   ├── 02_27_2020
│   │   ├── email1
│   │   ├── email2
│   │   ├── email3
│   │   ├── email4
│   │   ├── email5
│   └── 02_28_2020
│       └── email1
└── tmpemails
```

La section finale du script ouvre chaque nouveau message dans mon éditeur de texte de bureau préféré (Gedit). Il utilise une boucle _for...do...done_ similaire, lisant cette fois les noms de chaque fichier dans le nouveau répertoire (référencé en utilisant la commande "_today_") puis ouvrant le fichier dans Gedit. Remarquez l'astérisque que j'ai ajouté à la fin de l'emplacement du répertoire.

```bash
for NEWFILE in ${base_location}/${today}/*
do
   gedit $NEWFILE
done
```

Il reste encore une chose à faire. Si je ne nettoie pas mon bucket S3, il téléchargera tous les messages accumulés à chaque fois que j'exécuterai le script. Cela rendra la gestion de plus en plus difficile.

Donc, après avoir téléchargé avec succès mes nouveaux messages, j'exécute ce court script pour supprimer tous les fichiers dans le bucket :

```bash
#!/bin/bash
# Supprimer tous les e-mails existants 

aws s3 rm --recursive s3://bucket-name/ --profile myaccount
```