---
title: Comment installer un serveur LAMP sur une machine locale Ubuntu Linux ou une
  VM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T21:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-a-lamp-server-on-a-local-ubuntu-linux-machine-or-vm
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d56740569d1a4ca3733.jpg
tags:
- name: Linux
  slug: linux
- name: MySQL
  slug: mysql
- name: PHP
  slug: php
- name: servers
  slug: servers
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer un serveur LAMP sur une machine locale Ubuntu Linux ou
  une VM
seo_desc: "The purpose of this brief guide is to take you through the process of setting\
  \ up a LAMP (Linux, Apache, MySQL, PHP) server on a local Ubuntu Linux machine or\
  \ virtual machine. \nThis will allow you to develop using PHP and MySQL (with phpMyAdmin).\
  \ This..."
---

Le but de ce guide est de vous accompagner dans le processus d'installation d'un serveur LAMP (Linux, Apache, MySQL, PHP) sur une machine locale Ubuntu Linux ou une machine virtuelle. 

Cela vous permettra de développer en utilisant PHP et MySQL (avec phpMyAdmin). Il s'agit d'une pile courante nécessaire pour le développement WordPress.

## Installer les paquets nécessaires

Vous devrez installer les paquets suivants pour le serveur LAMP. Vous pouvez les installer tous en une fois en les séparant par un espace, ou un par un comme montré.

Je préfère les télécharger un par un car il est plus facile de voir s'il y a eu des erreurs.

Entrez dans le terminal et tapez les commandes suivantes :

* `sudo apt-get install apache2`
* `sudo apt-get install php`
* `sudo apt-get install php-mysql`
* `sudo apt-get install mysql-server`

Vous devriez alors être invité à définir un mot de passe pour l'utilisateur root de MySQL. Après avoir défini le mot de passe, continuez l'installation :

* `sudo apt-get install libapache2-mod-php`
* `sudo apt-get install php-mcrypt`
* `sudo apt-get install phpmyadmin`

Vous devriez alors être invité à choisir le serveur à utiliser. Sélectionnez Apache en appuyant sur Entrée. Sélectionnez non pour la configuration avancée du serveur.

## Changer les permissions du répertoire /var/www/html

Pour que les scripts et fichiers PHP soient exécutés par le serveur LAMP, ils doivent être enregistrés dans le répertoire /var/www/html. Vous pouvez considérer cet emplacement comme votre serveur local.

Pour apporter des modifications à ce répertoire, nous devons changer les permissions. Dans le terminal, entrez la commande :

`sudo chown {votre nom d'utilisateur ubuntu} /var/www/html`

## Créer un lien symbolique vers phpMyAdmin

Par défaut, phpMyAdmin est installé dans le répertoire /usr/share/. Nous devons le déplacer vers notre répertoire de serveur local.

Nous naviguons vers le répertoire du serveur où nous voulons le lien avec : `cd /var/www/html`

Ensuite, créez le lien en entrant la commande `ln -s /usr/share/phpmyadmin phpmyadmin`.

## Redémarrer Apache et tester

Exécutez la commande suivante pour redémarrer Apache et appliquer les modifications :

`sudo systemctl restart apache2`

Vous devriez alors pouvoir créer un fichier info.php dans le répertoire /var/www/html avec cette commande : `touch /var/www/html/info.php`

Dans le fichier, tapez le code PHP suivant :

`<?php phpinfo(); ?>`

Ensuite, ouvrez un navigateur et tapez localhost/info.php. Vous devriez voir une page générée par le fichier PHP que vous venez d'écrire, qui vous donne des informations sur PHP.

Enfin, pour accéder à phpMyAdmin, allez sur localhost/phpmyadmin dans votre navigateur. Le nom d'utilisateur root par défaut est « root » et le mot de passe est celui que vous avez choisi précédemment pour la base de données MySQL.