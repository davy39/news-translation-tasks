---
title: Comment configurer un projet Laravel avec un nom de domaine personnalisé sur
  Windows avec XAMPP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-14T02:58:05.000Z'
originalURL: https://freecodecamp.org/news/configure-a-laravel-project-with-custom-domain-name
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover--2-.png
tags:
- name: apache
  slug: apache
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Comment configurer un projet Laravel avec un nom de domaine personnalisé
  sur Windows avec XAMPP
seo_desc: "By Abdulwahab Ashimi\nLaravel's simplicity and MVC architecture make it\
  \ an ideal PHP framework for building web applications. \nIn this article, I will\
  \ show you how to set up Laravel on your Windows machine and configure it to run\
  \ on a custom domain na..."
---

Par Abdulwahab Ashimi

La simplicité de Laravel et son architecture MVC en font un framework PHP idéal pour construire des applications web. 

Dans cet article, je vais vous montrer comment installer Laravel sur votre machine Windows et le configurer pour qu'il fonctionne avec un nom de domaine personnalisé.

Ce guide est particulièrement adapté aux débutants qui souhaitent faire fonctionner Laravel rapidement et facilement. Mais même en tant que programmeur avancé, vous trouverez probablement de nouvelles perspectives sur la manière de simplifier le processus de configuration d'un projet Laravel. Alors, plongeons-nous dans le sujet !

## Comment installer et démarrer Xampp

Xampp est un outil open-source qui vous permet d'exécuter un serveur Apache, une base de données MySQL et d'autres outils à partir d'une seule interface pour le développement. 

Vous pouvez télécharger et installer Xampp ici : [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html).

Tout d'abord, lancez l'interface Xampp et démarrez votre serveur Apache et MySQL.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/XAMPP-Control-Panel-v3.3.0-----Compiled_-Apr-6th-2021---2_8_2023-12_12_47-PM.png)
_L'interface Xampp_

Ensuite, cliquez sur `Explorer` pour lancer votre dossier `htdocs` de Xampp. Supprimez les fichiers et dossiers à l'intérieur du dossier. Vous pouvez maintenant configurer votre application Laravel.

## Comment installer Laravel

À l'intérieur du dossier `htdocs`, vous pouvez cloner votre application Laravel existante ou configurer une nouvelle installation en utilisant `composer create-project laravel/laravel exemple-app`. Dans ce cas, "exemple-app" est le nom de votre projet, mais vous pouvez le remplacer par le nom de votre choix pour le projet.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/htdocs-2_8_2023-12_25_22-PM.png)
_La structure du répertoire Laravel dans htdocs_

Ouvrez le dossier htdocs dans votre éditeur de code préféré. J'utiliserai VScode pour mon exemple.

Remplacez la valeur `APP_URL` dans le fichier `.env` de votre projet Laravel par le nom de domaine personnalisé :

```env
APP_URL=https://projet.test
```

Vous pouvez remplacer "projet.test" par le nom de domaine de test de votre choix.

## Comment configurer votre fichier Hosts

Dans l'explorateur de fichiers Windows, accédez au fichier "hosts" situé à `C:\Windows\System32\drivers\etc\hosts` et ouvrez-le avec VScode (ou l'éditeur que vous utilisez). Je vous conseille d'utiliser VScode avec des privilèges administrateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/1.-Host-File.png)
_Répertoire etc contenant le fichier hosts et d'autres fichiers_

Ajoutez la ligne suivante au fichier :

```
127.0.0.1 projet.test
```

Cela mappera le nom d'hôte "projet.test" à l'adresse IP locale "127.0.0.1".

Maintenant, si vous lancez votre serveur Apache et visitez projet.test sur votre navigateur, il charge l'"index of" projet.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1675857587334/7a426d88-8963-4c75-a347-49054a33b8da.png)
_Index of' Le répertoire Laravel sur le navigateur_

C'est parce que pour que votre application Laravel fonctionne, elle doit charger le dossier public. Si vous pouvez charger public.test/public sur votre navigateur, vous serez redirigé vers le projet Laravel. Pour corriger cela, vous pouvez configurer le répertoire racine d'Apache.

## Comment configurer votre répertoire racine Apache

Dans l'explorateur de fichiers Windows, accédez au fichier "httpd.conf" qui contient la configuration d'Apache. Il est situé à `C:\xampp\apache\conf\httpd.conf`. Vous devez également utiliser VScode avec des privilèges administrateur dans ce cas.

Juste en dessous de `# Virtual hosts`, ajoutez ce qui suit :

```conf
<VirtualHost *:80>
    ServerName projet.test
    DocumentRoot "C:/xampp/htdocs/projet/public"
    <Directory "C:/xampp/htdocs/projet/public">
        Options Indexes FollowSymLinks Includes ExecCGI
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

Note : Remplacez `projet.test` par votre nom de domaine personnalisé et `C:/xampp/htdocs/projet/public` par le chemin vers votre dossier public.

Arrêtez et redémarrez le serveur Apache depuis votre interface Xampp et essayez de visiter "[**http://projet.test**](http://decmark.test)" sur votre navigateur pour voir la page d'accueil du projet Laravel.

## Conclusion

Vous pouvez avoir plusieurs projets avec leurs propres noms de domaine personnalisés en les configurant dans différents répertoires à l'intérieur du répertoire htdocs et en spécifiant leurs configurations Apache individuelles.

Si cet article vous a été utile, partagez-le avec vos amis ou mentionnez-moi sur Twitter [@adebowale1st](https://twitter.com/Adebowale1st).