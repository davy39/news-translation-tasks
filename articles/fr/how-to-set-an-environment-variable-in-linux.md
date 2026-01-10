---
title: Comment définir une variable d'environnement sous Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-10-26T18:38:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-an-environment-variable-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Copy-of-Copy-of-read-write-files-python--3-.png
tags:
- name: Linux
  slug: linux
seo_title: Comment définir une variable d'environnement sous Linux
seo_desc: "In programming, you use variables to store information like strings and\
  \ numbers temporarily. \nVariables can be used repeatedly throughout the code or\
  \ by your operating system to provide values. You can edit them, overwrite them,\
  \ and delete them.\nIn t..."
---

En programmation, vous utilisez des variables pour stocker temporairement des informations comme des chaînes de caractères et des nombres. 

Les variables peuvent être utilisées à plusieurs reprises dans le code ou par votre système d'exploitation pour fournir des valeurs. Vous pouvez les modifier, les écraser et les supprimer.

Dans ce tutoriel, je vais vous apprendre ce que sont les variables d'environnement et comment les définir sous Linux. 

## Qu'est-ce qu'une variable d'environnement ?

Les variables d'environnement sont des variables spécifiques à un certain environnement. Par exemple, chaque utilisateur dans un système d'exploitation a son propre environnement. Un utilisateur administrateur a un environnement différent de celui des autres utilisateurs, par exemple. 

Vous pourriez déclarer une variable d'environnement nécessaire uniquement pour votre utilisateur (par exemple, un jeton secret) qui n'a pas besoin d'être exposé aux autres utilisateurs. 

Voici quelques exemples de variables d'environnement sous Linux :

* `USER` – Cela pointe vers l'utilisateur actuellement connecté.
* `HOME` – Cela montre le répertoire personnel de l'utilisateur actuel.
* `SHELL` – Cela stocke le chemin de l'interpréteur de commandes de l'utilisateur actuel, comme bash ou zsh.
* `LANG` – Cette variable pointe vers les paramètres de langue/locales actuels.
* `MAIL` – Cela montre l'emplacement où le courrier de l'utilisateur actuel est stocké.

Ces variables d'environnement varient en fonction de la session utilisateur actuelle.

## Comment lister les variables d'environnement sous Linux

La commande utilisée pour afficher toutes les variables d'environnement définies pour une session actuelle est `env`. 

Voici la sortie pour ma session :

```bash
root@Zaira:~# env
SHELL=/bin/bash
PWD=/root
LOGNAME=root
HOME=/root
LANG=C.UTF-8
LESSOPEN=| /usr/bin/lesspipe %s
USER=root
SHLVL=1
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
MAIL=/var/mail/root
_=/usr/bin/env
```

## Comment afficher les variables d'environnement sous Linux

Il existe deux façons d'afficher les variables d'environnement déjà définies :

* `printenv NOM_VARIABLE`
* `echo $nomvariable`

Affichons la valeur de la variable `SHELL` en utilisant les deux méthodes. Voici un exemple d'affichage en utilisant `printenv` :

```bash
root@Zaira:~# printenv SHELL
/bin/bash
```

Et voici un exemple d'utilisation de `echo` :

```bash
root@Zaira:~# echo $SHELL
/bin/bash
```

## Comment définir des variables d'environnement sous Linux

La syntaxe de base pour définir une variable d'environnement est la suivante :

```bash
export NOM_VARIABLE=valeur
```

Définissons une variable d'environnement, listons-la et affichons sa valeur.

* Définir la variable `JAVA_HOME` :

```bash
root@Zaira:~# export JAVA_HOME=/usr/bin/java
```

* Vérifier en la listant :

```bash
root@Zaira:~# env
SHELL=/bin/bash
JAVA_HOME=/usr/bin/java
PWD=/root
LOGNAME=root
HOME=/root
LANG=C.UTF-8
LESSCLOSE=/usr/bin/lesspipe %s %s
TERM=xterm-256color
global22=yolo
LESSOPEN=| /usr/bin/lesspipe %s
USER=root
SHLVL=1
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
MAIL=/var/mail/root
_=/usr/bin/env
```

* Afficher sa valeur :

```bash
root@Zaira:~# echo $JAVA_HOME
/usr/bin/java
```

Cependant, les variables définies en utilisant cette méthode sont stockées pour la session actuelle uniquement. Elles ne seront pas disponibles pour la prochaine session. 

Vérifions en ouvrant une nouvelle session et en affichant la valeur de la variable.

```bash
zaira@Zaira:/etc$ echo $JAVA_HOME


```

Mais, nous pouvons rendre les définitions persistantes comme montré dans la section suivante.

## Comment rendre les variables d'environnement persistantes sous Linux

Pour rendre la variable `JAVA_HOME` persistante, éditez le fichier `.bashrc` et définissez sa valeur dans celui-ci. 

Le fichier `.bashrc` est un fichier de script qui est exécuté chaque fois qu'un utilisateur se connecte. Il est caché et situé dans le répertoire personnel de l'utilisateur par défaut. 

J'ai édité mon fichier `.bashrc` comme suit :

```bash
vi ~/.bashrc
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-194.png)
_Ajoutez la définition de la variable d'environnement à la fin du fichier `.bashrc`_

Pour que les modifications prennent effet, mettez à jour le fichier `.bashrc` en utilisant la commande `source` :

```bash
source .bashrc
```

Vérifions en ouvrant une nouvelle session.

```bash
root@Zaira:~# echo $JAVA_HOME
/usr/bin/java
```

## Comment créer une variable globale persistante sous Linux

Parfois, vous pourriez avoir besoin de définir une variable d'environnement globale accessible par tous les utilisateurs. 

Pour cela, nous devons d'abord déclarer une variable et apporter des modifications dans les fichiers pertinents où les variables d'environnement sont lues.

Procédez étape par étape.

1. Je suis connecté en tant qu'utilisateur `Zaira`. Je crée une variable globale `GLOBAL_VARIABLE` comme ceci :

```bash
zaira@Zaira:~$ export GLOBAL_VARIABLE="Ceci est une variable globale"
```

2. Éditez les fichiers suivants :

* `/etc/environment` – Ce fichier est utilisé pour configurer des variables d'environnement système.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-196.png)
_Mettez à jour le fichier `/etc/environment`_

Pour que les modifications prennent effet, utilisez la commande `source /etc/environment`.

* `/etc/profile` – Les variables définies dans ce fichier sont lues chaque fois qu'un shell bash est connecté. Éditez ce fichier et utilisez la commande `export` :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-198.png)
_Mettez à jour le `/etc/profile`_

Il est temps de tester !

Maintenant, je vais changer d'utilisateur pour l'utilisateur root et vérifier si je peux accéder à la variable `GLOBAL_VARIABLE`.

```bash
root@Zaira:~# echo $GLOBAL_VARIABLE
Ceci est une variable globale
```

Cela a fonctionné ! J'ai pu accéder à la variable globale définie par l'utilisateur `Zaira` via l'utilisateur `root` également. Le même principe s'appliquerait aux autres utilisateurs. Vous savez maintenant également comment définir des variables d'environnement globales.

## Conclusion

Dans ce tutoriel, vous avez appris comment créer et définir des variables d'environnement sous Linux. Vous avez également appris comment les rendre persistantes afin de pouvoir les utiliser dans plusieurs sessions. 

Quelle est la chose préférée que vous avez apprise ici ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

[Image par catalyststuff](https://www.freepik.com/free-vector/hacker-operating-laptop-cartoon-icon-illustration-technology-icon-concept-isolated-flat-cartoon-style_11602236.htm#query=programmer&position=2&from_view=search&track=sph) sur Freepik.