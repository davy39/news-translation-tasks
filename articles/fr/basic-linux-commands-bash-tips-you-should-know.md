---
title: Commandes Linux - Conseils de base pour la ligne de commande Bash que vous
  devriez connaître
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2020-01-05T22:19:00.000Z'
originalURL: https://freecodecamp.org/news/basic-linux-commands-bash-tips-you-should-know
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e28740569d1a4ca3ba8.jpg
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Commandes Linux - Conseils de base pour la ligne de commande Bash que vous
  devriez connaître
seo_desc: "Linux has a ton of commands, but most people only use a fraction of them.\
  \ Here are some of the most used Linux commands to use in the terminal. \nFirst,\
  \ we'll cover some tips that will make the command line easier to use:\n\nUse tab\
  \ for autocompletion. ..."
---

Linux dispose d'une multitude de commandes, mais la plupart des gens n'en utilisent qu'une fraction. Voici quelques-unes des commandes Linux les plus utilisées à utiliser dans le terminal. 

Tout d'abord, nous allons couvrir quelques conseils qui rendront la ligne de commande plus facile à utiliser :

* Utilisez la touche tabulation pour l'autocomplétion. Après avoir commencé à taper quelque chose dans le terminal Linux, appuyez sur tabulation et il suggérera les options possibles qui commencent par la chaîne que vous avez tapée jusqu'à présent.
* Utilisez `ctrl+r terme_de_recherche` pour rechercher des commandes que vous avez précédemment utilisées.
* Déplacez-vous rapidement au début ou à la fin d'une ligne avec `ctrl+a` et `ctrl+e`.
* Réutilisez la commande précédente dans la commande actuelle avec `!!`.
* Vous pouvez exécuter plusieurs commandes en une seule ligne en séparant les commandes avec un `;`.

Il est temps d'apprendre les commandes Linux courantes. Vous pouvez obtenir plus d'informations sur n'importe laquelle de ces commandes en utilisant la commande `man`. Cela affichera la page de manuel pour une commande. Par exemple, si vous tapez `man cat` dans un terminal Linux, vous obtiendrez plus d'informations sur la commande `cat`.

### ls

Lister le contenu d'un répertoire.  
_Exemple :_ `ls /applications` affichera tous les fichiers et dossiers stockés dans le dossier applications.

### cd

Changer de répertoire.  
_Exemple :_ Changez du répertoire actuel vers _/usr/local_ avec `cd /usr/local`.

**mv**   
Renommer ou déplacer des fichiers ou des répertoires.  
_Exemple :_ la commande `mv todo.txt /home/qlarson/Documents` déplacerait "todo.txt" vers le répertoire "Documents".

### mkdir

Créer un nouveau répertoire.  
_Exemple :_ `mkdir freecodecamp` créera un répertoire nommé "freecodecamp".

### rmdir

Supprimer des répertoires vides.

### touch

Créer un fichier vide avec le nom spécifié.

### rm

Supprimer des fichiers et/ou des répertoires.  
_Exemple :_ `rm todo.txt` supprimera le fichier.

### locate 

Localiser un fichier spécifique.  
_Exemple :_  la commande `locate -i vacuum*mop` recherchera tout fichier contenant les mots "vacuum" et "mop". L'option `-i` rend la recherche insensible à la casse.

### clear

Effacer l'écran/la fenêtre de la ligne de commande pour un nouveau départ.

### cp

Copier des fichiers et des répertoires.  
_Exemple :_ la commande `cp todo.txt /home/qlarson/Documents` créerait une copie de "todo.txt" dans le répertoire "Documents".

### alias 

Créer un alias pour les commandes Linux.   
_Exemple :_ `alias search=grep` vous permettra d'utiliser `search` au lieu de `grep`_._

### cat

Afficher le contenu d'un fichier à l'écran.   
_Exemple :_ `cat todo.txt` affichera le texte de "todo.txt" à l'écran.

### chown

Changer le propriétaire d'un fichier.  
_Exemple :_ `chown qlarson todo.txt` fera de "qlarson" le propriétaire de "todo.txt".

### chmod

Changer les permissions d'un fichier.  
_Exemple :_ `chmod 777 todo.txt` rendra "todo.txt" lisible, modifiable et exécutable par tout le monde. Les chiffres dans "777" spécifient les permissions pour l'utilisateur, le groupe et les autres, dans cet ordre.

### sudo

Exécuter des tâches qui nécessitent des permissions administratives ou root.  
Exemple : Utilisez `sudo passwd quincy` pour changer le mot de passe de l'utilisateur "quincy".  
["Sudo make me a sandwich."](https://xkcd.com/149/)

### find 

Rechercher des fichiers correspondant à un motif fourni. Cette commande est utilisée pour rechercher des fichiers et des dossiers en utilisant des filtres tels que le nom, la taille, l'heure d'accès et l'heure de modification.  
_Exemple :_ `find /home/ -name todo.txt` recherchera un fichier nommé "todo.txt" dans le répertoire home et ses sous-répertoires.

### grep 

Rechercher des fichiers ou une sortie pour une chaîne ou une expression particulière. Cette commande recherche des lignes contenant un motif spécifié et, par défaut, les écrit dans la sortie standard.  
_Exemple :_ `grep run todo.txt` recherchera le mot "run" dans le fichier "todo.txt". Les lignes qui contiennent "run" seront affichées.

### date

Afficher ou définir la date et l'heure du système.

### df

Afficher un rapport sur l'utilisation de l'espace disque du système.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-114.png)

### du

Montrer combien d'espace chaque fichier occupe. Cela affichera la taille en nombres de blocs de disque. Si vous voulez la voir en octets, kilooctets et mégaoctets, ajoutez l'argument `-h` comme ceci : `du -h`.

### file

Déterminer le type d'un fichier.   
_Exemple :_ `file todo.txt` afficherait probablement le type "texte ASCII".

### history 

Affiche l'historique des commandes.

### kill 

Arrêter un processus.  
_Exemple :_ Arrêter un processus avec un PID de 485 en utilisant la commande `kill 485`. Utilisez la commande `ps` (ci-dessous) pour déterminer le PID d'un processus.

### less

Voir le contenu d'un fichier une page à la fois.  
_Exemple :_ `less todo.txt` affichera le contenu de "todo.txt".

**ps**   
Afficher une liste des processus en cours d'exécution. Cela peut être utilisé pour déterminer les PIDs nécessaires pour `kill` des processus.

### pwd 

Afficher le chemin du répertoire actuel. "**p**rint **w**orking **d**irectory"

### ssh 

Se connecter à distance à une autre machine Linux, via le réseau.   
_Exemple :_ `ssh quincy@104.25.105.32` se connectera à 104.25.105.32 en utilisant le nom d'utilisateur "quincy".

**tail** - Afficher les 10 dernières lignes d'un fichier. Voir moins ou plus de lignes en utilisant l'option -n (nombre).  
_Exemple :_ `tail -n 5 todo.txt` affichera les 5 dernières lignes de "todo.txt".

### tar

Stocker et extraire des fichiers d'un fichier tar (.tar) ou d'une archive tarball (.tar.gz ou .tgz).

### top 

Affiche les ressources utilisées sur votre système, similaire au gestionnaire de tâches dans Windows.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-115.png)