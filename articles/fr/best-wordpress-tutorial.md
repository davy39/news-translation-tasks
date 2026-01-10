---
title: Les meilleurs tutoriels WordPress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-24T00:45:00.000Z'
originalURL: https://freecodecamp.org/news/best-wordpress-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f17740569d1a4ca40c3.jpg
tags:
- name: MySQL
  slug: mysql
- name: PHP
  slug: php
- name: WordPress
  slug: wordpress
seo_title: Les meilleurs tutoriels WordPress
seo_desc: WordPress is a free and open-source content management system based on PHP
  and MySQL. Features include a plugin architecture and a template system. It is most
  associated with blogging, but supports other types of web content including more
  traditiona...
---

WordPress est un système de gestion de contenu gratuit et open-source basé sur PHP et MySQL. Ses fonctionnalités incluent une architecture de plugins et un système de templates. Il est principalement associé aux blogs, mais supporte également d'autres types de contenu web, y compris des listes de diffusion et des forums plus traditionnels, des galeries multimédias et des boutiques en ligne.

WordPress alimente près de 27 % de tous les sites web et domine actuellement la part de marché des CMS. Soutenu par une immense communauté, cette plateforme Open Source alimente une économie de plusieurs milliards de dollars avec des thèmes/plugins et des logiciels personnalisés.

Nous vous recommandons de commencer l'apprentissage avec [le tutoriel WordPress de 4 heures de freeCodeCamp](https://www.youtube.com/watch?v=KibbYf9avko) sur YouTube. Cela vous aidera à construire un site web WordPress à partir de zéro.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/wordpress-course-cover.jpg)

Ensuite, nous vous encourageons à apprendre le PHP - le langage de programmation qui alimente WordPress. freeCodeCamp propose un [tutoriel de 4 heures sur PHP et WordPress](https://www.youtube.com/watch?v=OK_JCtrrv-c) sur YouTube.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/php-course-cover.jpg)

## **Qu'est-ce que le PHP ?**

PHP est un langage de script côté serveur créé en 1995 par Rasmus Lerdorf.

PHP est un langage de script généraliste open source largement utilisé, particulièrement adapté au développement web et pouvant être intégré dans du HTML.

## **Que signifie l'acronyme PHP ?**

À l'origine, PHP signifiait « Personal Home Page », car Rasmus Lerdorf l'a créé pour son propre site web. Ensuite, en 1997, d'autres développeurs ont étendu le langage et l'acronyme a également changé pour ce qu'il signifie aujourd'hui : « PHP: Hypertext Preprocessor ». Comme le premier « P » de PHP signifie également « PHP », il est connu comme un « acronyme récursif ».

## **À quoi sert le PHP ?**

En octobre 2017, PHP était utilisé sur [82 % des sites web dont le langage côté serveur est connu](https://w3techs.com/technologies/overview/programming_language/all). Il est généralement utilisé sur les sites web pour générer dynamiquement le contenu des pages web. Les cas d'utilisation incluent :

* Sites web et applications web (scripting côté serveur)
* Scripting en ligne de commande
* Applications de bureau (GUI)

Typiquement, il est utilisé dans la première forme pour générer dynamiquement le contenu des pages web. Par exemple, si vous avez un site web de blog, vous pourriez écrire des scripts PHP pour récupérer vos articles de blog à partir d'une base de données et les afficher. D'autres utilisations des scripts PHP incluent :

* Traitement et sauvegarde des entrées utilisateur à partir des données de formulaire
* Définition et travail avec les cookies du site web
* Restriction de l'accès à certaines pages de votre site web

## **Comment fonctionne le PHP ?**

Tout le code PHP est exécuté uniquement sur un serveur web, et non sur votre ordinateur local. Par exemple, si vous remplissez un formulaire sur un site web et le soumettez, ou cliquez sur un lien vers une page web écrite en PHP, aucun code PHP réel ne s'exécute sur votre ordinateur.

Au lieu de cela, les données du formulaire ou la demande de la page web sont envoyées à un serveur web pour être traitées par les scripts PHP. Le serveur web envoie ensuite le HTML traité vers vous (d'où vient le « Hypertext Preprocessor » dans le nom), et votre navigateur web affiche les résultats.

Pour cette raison, vous ne pouvez pas voir le code PHP d'un site web, seulement le HTML résultant que les scripts PHP ont produit.

Cela est illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/PHP-server-model.png)

PHP est un langage interprété. Cela signifie que lorsque vous apportez des modifications à votre code source, vous pouvez immédiatement tester ces modifications, sans avoir besoin de compiler d'abord votre code source en forme binaire. Le fait de sauter l'étape de compilation rend le processus de développement beaucoup plus rapide.

Le code PHP est encadré entre les balises `<?php` et `?>` et peut ensuite être intégré dans du HTML.

## **Installation**

PHP peut être installé avec ou sans un serveur web.

### **GNU/Linux**

Sur les distributions GNU/Linux basées sur Debian, vous pouvez installer PHP avec :

```bash
sudo apt install php
```

Après l'installation, vous pouvez exécuter n'importe quel fichier PHP en faisant simplement ceci dans votre terminal :

```text
php fichier.php
```

Vous pouvez également installer un serveur local pour exécuter des sites web PHP. Pour installer le serveur web Apache :

```text
sudo apt install apache2 libapache2-mod-php
```

## **Que peut faire PHP ?**

* PHP peut générer du contenu de page dynamique
* PHP peut créer, ouvrir, lire, écrire, supprimer et fermer des fichiers sur le serveur
* PHP peut collecter des données de formulaire
* PHP peut envoyer et recevoir des cookies
* PHP peut ajouter, supprimer, modifier des données dans votre base de données
* PHP peut être utilisé pour contrôler l'accès des utilisateurs
* PHP peut chiffrer des données

## **Pourquoi PHP ?**

* PHP fonctionne sur diverses plateformes (Windows, Linux, Unix, Mac OS X, etc.)
* PHP est compatible avec presque tous les serveurs utilisés aujourd'hui (Apache, IIS, etc.)
* PHP supporte une large gamme de bases de données
* PHP est gratuit. Téléchargez-le depuis la ressource officielle PHP : [secure.php.net](https://secure.php.net/)
* PHP est facile à apprendre et s'exécute efficacement côté serveur

## **Frameworks PHP**

Étant donné qu'écrire tout le code pour un site web n'est pas vraiment pratique ou réalisable pour la plupart des projets, la plupart des développeurs tendent à utiliser des frameworks pour le développement web. L'avantage d'utiliser un framework est que :

* Vous n'avez pas besoin de réinventer la roue à chaque fois que vous créez un projet ; beaucoup de nuances sont déjà prises en charge pour vous
* Ils sont généralement bien structurés pour aider à la séparation des préoccupations
* La plupart des frameworks tendent à suivre les meilleures pratiques du langage
* Beaucoup d'entre eux suivent le modèle MVC (Modèle-Vue-Contrôleur) pour séparer la couche de présentation de la logique

## **Frameworks populaires**

* [Laravel](https://laravel.com/)
* [Symfony](https://symfony.com/)
* [Zend](http://www.zend.com/)
* [CakePHP](https://cakephp.org/)

## **Documentation**

PHP est [bien documenté](http://php.net/docs.php). Les [docs officiels](http://php.net/manual/en/) incluent des exemples sur presque chaque guide de référence de fonction, ainsi que des commentaires d'utilisateurs.

## **Autres ressources**

* [Tutoriel PHP de Tizag.com](http://www.tizag.com/phpT/) : des tutoriels toujours pertinents pour commencer avec PHP
* [Awesome PHP](https://github.com/ziadoz/awesome-php) : une liste organisée de bibliothèques PHP, de ressources et de "choses brillantes"
* [Laracasts.com](https://laracasts.com/) : un site d'adhésion pour apprendre le développement d'applications web avec PHP