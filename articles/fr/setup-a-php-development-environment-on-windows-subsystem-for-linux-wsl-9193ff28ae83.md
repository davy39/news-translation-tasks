---
title: Comment configurer un environnement de développement PHP sur Windows Subsystem
  for Linux (WSL)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T15:43:04.000Z'
originalURL: https://freecodecamp.org/news/setup-a-php-development-environment-on-windows-subsystem-for-linux-wsl-9193ff28ae83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hgWsj4pEYwb8sdp3UQDlTw.jpeg
tags:
- name: Linux
  slug: linux
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Ubuntu
  slug: ubuntu
seo_title: Comment configurer un environnement de développement PHP sur Windows Subsystem
  for Linux (WSL)
seo_desc: 'By András Magyar

  PHP development on Windows has some disadvantages. But, Microsoft now offers a great
  option for PHP developers who work on Windows: The Windows Subsystem for Linux (WSL).
  WSL is a compatibility layer for running Linux binary executab...'
---

Par András Magyar

Le développement PHP sur Windows présente certains inconvénients. Mais Microsoft offre désormais une excellente option pour les développeurs PHP qui travaillent sur Windows : le Windows Subsystem for Linux (WSL). WSL est une couche de compatibilité pour exécuter des exécutables binaires Linux (au format ELF) nativement sur Windows 10. Microsoft déclare :

> « C'est principalement un outil pour les développeurs — surtout les développeurs web et ceux qui travaillent sur ou avec des projets open source. »

Nous pouvons exécuter un environnement Linux directement sur Windows sans le surcoût d'une machine virtuelle.

**Note :** Cet article n'est pas uniquement destiné aux Windows Insiders. Ces méthodes fonctionneront également sur les dernières versions stables de Windows 10.

Dans ce tutoriel, nous allons configurer une pile LAMP (Ubuntu 16.04, Apache, PHP 7.1, MariaDB) sur WSL pour le développement. Vous pouvez configurer d'autres piles (par exemple, une pile LEMP) avec des méthodes similaires.

### Prérequis

Avant de commencer ce guide, vous aurez besoin des éléments suivants :

* Une version 64 bits de Windows 10 avec la [Creators Update](https://support.microsoft.com/en-us/help/4028685/windows-get-the-windows-10-creators-update) ou une version ultérieure.
* Une familiarité avec Linux/bash (si vous souhaitez vous familiariser avec la ligne de commande, vous pouvez lire [ce tutoriel DigitalOcean](https://www.digitalocean.com/community/tutorials/an-introduction-to-the-linux-terminal)).

### Étape 1 : installation de bash sur Windows

Tout d'abord, vous aurez besoin de WSL installé sur votre ordinateur.

Vous pouvez installer d'autres distributions Linux depuis le Microsoft Store (Ubuntu, openSUSE, SUSE Linux Enterprise Server 12). Mais dans ce tutoriel, nous allons configurer la pile LAMP sur Ubuntu, **vous devez donc sélectionner Ubuntu**.

Microsoft propose un excellent tutoriel sur la façon d'installer WSL, [veuillez suivre les instructions de l'article](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

Si vous avez installé avec succès Bash sur Ubuntu sur Windows, installons et configurons une simple pile LAMP pour le développement.

### Étape 2 : installation d'un serveur HTTP Apache

Nous voulons installer la dernière version stable d'Apache, mais les dépôts officiels d'Ubuntu ne contiennent pas la dernière version.

Nous devons ajouter un PPA pour les paquets Apache. Un Personal Package Archive (PPA) est un dépôt qui permet aux développeurs tiers de construire et de distribuer des paquets pour Ubuntu. Le PPA d'Ondřej Surý offre les derniers paquets Apache/PHP pour Ubuntu.

Pour ajouter le PPA, exécutez la commande suivante dans le bash WSL :

```
sudo add-apt-repository ppa:ondrej/apache2
```

Une fois le PPA configuré, mettez à jour l'index des paquets locaux :

```
sudo apt-get update
```

Installez Apache :

```
sudo apt-get install apache2
```

Créez un dossier de projet pour vos applications web. Ce dossier doit être en dehors du système de fichiers WSL. Je vous recommande d'utiliser votre dossier Documents.

La commande suivante créera un dossier serveur dans votre répertoire Documents. Veuillez remplacer **VOTRE NOM D'UTILISATEUR WINDOWS** par votre nom d'utilisateur Windows.

```
sudo mkdir /mnt/c/Users/VOTRE NOM D'UTILISATEUR WINDOWS/Documents/server
```

Créez un lien symbolique vers le dossier sélectionné.

```
sudo ln -s /mnt/c/Users/VOTRE NOM D'UTILISATEUR WINDOWS/Documents/server /var/www/devroot
```

Ouvrez le fichier de configuration du virtual host par défaut d'Apache :

```
sudo nano /etc/apache2/sites-enabled/000-default.conf
```

Modifiez la racine du document en « /var/www/devroot », qui pointe vers votre dossier de projet en dehors du système de fichiers de WSL. Définissez `ServerName` sur `localhost` (si le port 80 est réservé par une application Windows, remplacez 80 par un port non utilisé) :

```
<VirtualHost *:80>        ServerName localhost        ServerAdmin webmaster@localhost        DocumentRoot  /var/www/devroot      <Directory /var/www/>        Options Indexes FollowSymLinks        AllowOverride All        Require all granted      </Directory>        ErrorLog ${APACHE_LOG_DIR}/error.log        CustomLog ${APACHE_LOG_DIR}/access.log combined</VirtualHost>
```

Lorsque vous avez terminé, enregistrez le fichier en appuyant sur Ctrl-O, puis appuyez sur Entrée pour confirmer. Quittez avec Ctrl-X.

Ouvrez votre éditeur/IDE Windows préféré et créez un fichier « index.html » dans votre dossier de projet (C:\Users\ **VOTRE NOM D'UTILISATEUR WINDOWS**\Documents\server) avec le contenu suivant :

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="utf-8">  <title>Ça marche !</title></head>&lt;body>  <h1>Ça marche !</h1></body></html>
```

Démarrez le serveur HTTP Apache :

```
sudo service apache2 start
```

Ouvrez [http://localhost/](http://localhost/) dans votre navigateur et vous devriez voir le titre « Ça marche ».

N'oubliez pas d'activer les modules Apache nécessaires pour vous. Par exemple, vous pouvez activer mod_rewrite :

```
sudo a2enmod rewritesudo service apache2 restart
```

### Étape 3 : installation du serveur MariaDB

Ajoutez un dépôt qui contient les derniers paquets MariaDB :

```
sudo apt-get install software-properties-common
```

```
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
```

```
sudo add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://ams2.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu xenial main'
```

Installez MariaDB :

```
sudo apt-get updatesudo apt-get install mariadb-server
```

Vous serez invité à créer un mot de passe root pendant l'installation. Choisissez un mot de passe sécurisé et retenez-le, car vous en aurez besoin plus tard.

Démarrez MariaDB :

```
sudo service mysql start
```

Exécutez le script suivant (cela modifie certaines des options par défaut moins sécurisées) :

```
mysql_secure_installation
```

### Étape 4 : installation de PHP

Ajoutez le PPA pour la dernière version de PHP :

```
sudo add-apt-repository ppa:ondrej/phpsudo apt-get update
```

Installez les paquets PHP 7.1 :

```
sudo apt-get install php7.1 libapache2-mod-php7.1 php7.1-mcrypt php7.1-mysql php7.1-mbstring php7.1-gettext php7.1-xml php7.1-json php7.1-curl php7.1-zip
```

Nous devons redémarrer Apache :

```
sudo service apache2 restart
```

Créez un fichier info.php dans votre dossier de projet avec le contenu suivant :

```
<?phpphpinfo();
```

Ouvrez [http://localhost/info.php](http://localhost/info.php) dans votre navigateur. Si PHP fonctionne correctement, vous devriez voir ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1q-zAJXFIrM9FsQmnkgSLwfMJgVTolUpKY0Y)

### Étape 5 : installation de phpMyAdmin

phpMyAdmin est un outil d'administration gratuit et open source pour MySQL et MariaDB.

Avec phpMyAdmin, vous pouvez facilement créer/gérer vos bases de données en utilisant une interface web.

```
sudo apt-get install phpmyadmin
```

* Lorsque la première invite apparaît, appuyez sur Espace, Tabulation, puis Entrée pour sélectionner Apache.
* Sélectionnez oui lorsque vous êtes invité à utiliser dbconfig-common pour configurer la base de données.
* Fournissez votre mot de passe root MariaDB
* Choisissez un mot de passe pour l'application phpMyAdmin elle-même

Activez les extensions PHP nécessaires :

```
sudo phpenmod mcryptsudo phpenmod mbstring
```

Redémarrez Apache :

```
sudo service apache2 restart
```

Vous pouvez maintenant accéder à phpMyAdmin sur l'URL suivante : [http://localhost/phpmyadmin/](http://localhost/phpmyadmin/)
Vous pouvez vous connecter en utilisant le nom d'utilisateur root et le mot de passe root que vous avez configuré pendant l'installation de MariaDB.

### Étape 6 : installation de Composer

Composer est un gestionnaire de paquets pour PHP. Il vous permet d'installer/mettre à jour les bibliothèques dont votre projet dépend. Si vous êtes un développeur PHP, vous utilisez probablement Composer.

Visitez la [page de téléchargement de Composer](https://getcomposer.org/download/) et suivez les instructions dans la section Installation en ligne de commande. Après que Composer soit installé avec succès, vous pouvez l'installer globalement :

```
sudo mv composer.phar /usr/local/bin/composer
```

Maintenant, il peut être exécuté depuis n'importe quel emplacement en tapant :

```
composer
```

![Image](https://cdn-media-1.freecodecamp.org/images/eRZmxz7jyQxXn1Z7RlegrHDn1M4E6kgB6Gml)

### Étape 7 : installation de Git :

Git est un système de contrôle de version qui est principalement utilisé pour la gestion du code source. [En savoir plus sur Git ici](https://git-scm.com/doc).

Vous pouvez l'installer en exécutant la commande suivante :

```
sudo apt-get install git
```

Avant d'utiliser Git (et si vous n'êtes pas familier avec lui), veuillez lire la section « Comment configurer Git » du [tutoriel Comment installer Git sur Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-16-04).

### Étape 8 : démarrer automatiquement LAMP sur WSL (optionnel)

Les tâches en arrière-plan ne sont actuellement pas prises en charge sur WSL. Lorsque vous fermez Bash, vos services (Apache et MariaDB) s'arrêteront.

**Note pour les Windows Insiders :** Les tâches en arrière-plan sont désormais prises en charge sur WSL à partir de la version Windows Insider Build 17046 (pour plus de détails, vous pouvez lire l'article de blog suivant : [Prise en charge des tâches en arrière-plan dans WSL](https://blogs.msdn.microsoft.com/commandline/2017/12/04/background-task-support-in-wsl/)), mais le démarrage automatique des services n'est toujours pas disponible.

Malheureusement, le démarrage automatique de vos services est un peu difficile.

Configurons le démarrage automatique !

Nous devons démarrer les services sans taper votre mot de passe.

**Avant de commencer**, veuillez consulter le tutoriel suivant [Comment éditer le fichier Sudoers sur Ubuntu et CentOS](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos).

Exécutez la commande suivante :

```
sudo visudo -f /etc/sudoers.d/services
```

Copiez et collez ce qui suit dans l'éditeur, puis enregistrez :

```
%sudo ALL=(root) NOPASSWD: /usr/sbin/service *%wheel ALL=(root) NOPASSWD: /usr/sbin/service *
```

Cela nous permet de démarrer les services (comme Apache et MariaDB) sans utiliser notre mot de passe.

Démarrez l'invite de commandes (pas le bash) en tant qu'administrateur et exécutez :

```
SchTasks /Create /SC ONLOGON /TN "Démarrer WSL LAMP" /TR "c:\Windows\System32\bash.exe -c 'sudo service apache2 start; sudo service mysql start; cd ~; bash'"
```

La commande ci-dessus crée une tâche qui s'exécute automatiquement lorsque vous vous connectez à Windows. Elle fait ce qui suit :

* Démarre Apache
* Démarre MariaDB
* Change le répertoire vers votre répertoire personnel

**N'oubliez pas : lorsque vous fermez la fenêtre du terminal, les services s'arrêteront et vous devrez les redémarrer manuellement !**

### Étape 9 : ajouter des domaines de test (optionnel)

Lorsque vous travaillez sur plusieurs applications web, plusieurs domaines de test seront utiles. Par exemple, si vous travaillez sur myapp.com, vous pouvez accéder à la version de développement locale sur [http://myapp.test/](http://myapp.test/) au lieu de [http://localhost/myapp](http://localhost/myapp).

Dans ce qui suit, vous pouvez remplacer « myapp » par le nom de votre application web.
Créez un dossier dans votre répertoire de projets pour votre application web :

```
sudo mkdir /mnt/c/Users/VOTRE NOM D'UTILISATEUR WINDOWS/Documents/server/myapp
```

Ajoutez le fichier de virtual host à Apache :

```
sudo nano /etc/apache2/sites-available/myapp.test.conf
```

Enregistrez la configuration suivante dans le nouveau fichier (n'oubliez pas de remplacer myapp par le nom de votre application).

```
<VirtualHost *:80>
```

```
ServerName myapp.test
```

```
ServerAdmin webmaster@localhost DocumentRoot /var/www/devroot/myapp
```

```
<Directory /var/www/> Options Indexes FollowSymLinks AllowOverride All Require all granted </Directory>
```

```
ErrorLog ${APACHE_LOG_DIR}/error.log CustomLog ${APACHE_LOG_DIR}/access.log combined
```

```
</VirtualHost>
```

Activez le nouveau site :

```
sudo a2ensite myapp.test
```

Redémarrez Apache :

```
sudo service apache2 restart
```

Enfin, démarrez le Bloc-notes ou votre éditeur/IDE préféré sur Windows avec des privilèges d'administrateur (**Exécuter en tant qu'administrateur**) et ouvrez le fichier **hosts**. Il se trouve dans le dossier **c:\windows\system32\drivers\etc**.

Ajoutez la ligne suivante à la fin du fichier et enregistrez-le :

```
127.0.0.1 myapp.test
```

Vous pouvez maintenant accéder à votre application web sur le domaine [http://myapp.test/](http://myapp.test/).
Vous pouvez également ajouter plus de domaines de test avec la même méthode.

#### Conclusion

WSL ne remplace pas Vagrant ou Docker, et il est expérimental. Le démarrage automatique des services n'est actuellement pas pris en charge sur WSL, et c'est l'un des plus grands problèmes avec lui à l'heure actuelle. Cependant, le Windows Subsystem for Linux est une excellente option pour les développeurs d'utiliser un shell Linux natif sur Windows. Je pense que vous devriez l'essayer !