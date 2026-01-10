---
title: Qu'est-ce que PHP ? La signification du langage de programmation PHP expliquée
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-30T15:13:30.000Z'
originalURL: https://freecodecamp.org/news/what-is-php-the-php-programming-language-meaning-explained
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/php.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: PHP
  slug: php
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que PHP ? La signification du langage de programmation PHP expliquée
seo_desc: "PHP is an open-source server-side scripting language that many devs use\
  \ for web development. It is also a general-purpose language that you can use to\
  \ make lots of projects, including Graphical User Interfaces (GUIs). \nIn this article,\
  \ I will help yo..."
---

PHP est un langage de script côté serveur open-source que de nombreux développeurs utilisent pour le développement web. C'est également un langage polyvalent que vous pouvez utiliser pour réaliser de nombreux projets, y compris des interfaces graphiques (GUI).

Dans cet article, je vais vous aider à explorer le monde de PHP afin que vous puissiez apprendre comment il fonctionne et ses fonctionnalités de base. À la fin, vous serez en mesure d'écrire votre premier programme Hello World en PHP.

## Que signifie PHP ?

L'abréviation PHP signifiait initialement Personal Homepage. Mais maintenant, c'est un acronyme récursif pour Hypertext Preprocessor. (Il est récursif dans le sens où le premier mot lui-même est une abréviation, donc la signification complète ne suit pas l'abréviation.)

La première version de PHP a été lancée il y a 26 ans. Maintenant, il est à la version 8, sortie en novembre 2020, mais la version 7 reste la plus largement utilisée.

PHP fonctionne sur le moteur Zend, qui est l'implémentation la plus populaire. Il existe également d'autres implémentations, comme Parrot, HPVM (Hip Hop Virtual Machine) et Hip Hop, créées par Facebook.

PHP est principalement utilisé pour créer des serveurs web. Il fonctionne sur le navigateur et est également capable de fonctionner en ligne de commande. Donc, si vous ne souhaitez pas afficher la sortie de votre code dans le navigateur, vous pouvez l'afficher dans le terminal.

## Avantages de PHP

PHP présente certains avantages qui l'ont rendu si populaire, et c'est le langage de prédilection pour les serveurs web depuis plus de 15 ans. Voici quelques-uns des avantages de PHP :

- Multiplateforme : PHP est indépendant de la plateforme. Vous n'avez pas besoin d'avoir un système d'exploitation particulier pour l'utiliser car il fonctionne sur toutes les plateformes, qu'il s'agisse de Mac, Windows ou Linux.

- Open Source : PHP est open source. Le code original est mis à la disposition de tous ceux qui souhaitent le développer. C'est l'une des raisons pour lesquelles l'un de ses frameworks, Laravel, est si populaire.

- Facile à apprendre : PHP n'est pas difficile à apprendre pour les débutants absolus. Vous pouvez l'apprendre assez facilement si vous avez déjà des connaissances en programmation.

- PHP se synchronise avec toutes les bases de données : Vous pouvez facilement connecter PHP à toutes les bases de données, relationnelles et non relationnelles. Il peut donc se connecter en un rien de temps à MySQL, Postgress, MongoDB ou toute autre base de données.

- Communauté de soutien : PHP dispose d'une communauté en ligne très active. La documentation officielle fournit des guides sur l'utilisation des fonctionnalités et vous pouvez facilement résoudre votre problème en cas de blocage.

## Qui utilise PHP

Un certain nombre d'entreprises établies et de géants de la technologie utilisent PHP pour faire fonctionner leurs serveurs et réaliser de nombreuses choses incroyables.

- Facebook : Facebook utilise PHP pour alimenter son site. En retour, l'entreprise a contribué à la communauté en créant une implémentation connue sous le nom de Hip Hop pour PHP.

- Wikipedia : l'une des plus grandes sources d'informations sur n'importe quel sujet au monde, Wikipedia est construite en PHP.

- Systèmes de gestion de contenu (CMS) : le système de gestion de contenu le plus populaire au monde, WordPress, est construit en PHP. D'autres systèmes de gestion de contenu tels que Drupal, Joomla et Magento sont également construits en PHP. Shopify fonctionne également sur PHP.

- Plateformes d'hébergement web : de nombreuses plateformes d'hébergement web telles que BlueHost, SiteGround et Whogohost font fonctionner leurs serveurs d'hébergement en utilisant PHP.

## PHP est-il en train de mourir ?

De nos jours, il y a un débat intense sur le fait que PHP soit en déclin ou non. Cela est dû à l'avènement et à la popularité croissante d'autres langages adaptés au côté serveur tels que JavaScript (Node JS), Python, Golang, et autres.

Cela a en fait conduit à de nombreux memes amusants ciblant PHP
![php-meme](https://www.freecodecamp.org/news/content/images/2021/08/php-meme.jpg)

Mais PHP est-il vraiment en train de mourir ? La réponse est non. Malgré certaines personnes qui le critiquent et les affirmations de déclin, PHP est toujours utilisé pour faire fonctionner les serveurs de près de 80 % de tous les sites web aujourd'hui. Donc, si vous visitez 10 sites web par jour, il y a des chances que 8 d'entre eux utilisent PHP.

En termes de disponibilité d'emplois, PHP se classe mieux que de nombreux autres langages de programmation sur la plateforme d'emploi Indeed. De nombreux développeurs PHP gagnent bien leur vie en créant des thèmes et des plugins WordPress chaque année – le développeur PHP moyen aux États-Unis gagne 86 000 $ par an.

![php-jobs](https://www.freecodecamp.org/news/content/images/2021/08/php-jobs.jpg)

## Comment écrire votre premier programme Hello World en PHP

Maintenant que vous avez appris ce qu'est PHP et ses avantages, il est temps d'écrire votre premier programme Hello World en PHP !

Tout d'abord, vous devez avoir PHP installé sur votre machine locale. Vous pouvez le faire en installant un serveur XAMP (Cross-Platform, Apache, MySQL et PHP) ou WAMP (Windows, Apache, MySQL et PHP).

XAMP fonctionne sur tous les systèmes d'exploitation et WAMP fonctionne uniquement sous Windows. Je vais utiliser WAMP.

Ouvrez le serveur WAMP ou XAMP et assurez-vous que tous les services sont en cours d'exécution. Si vous utilisez WAMP, le logo WAMP doit s'afficher dans votre barre des tâches avec la couleur verte.

![wamp-running](https://www.freecodecamp.org/news/content/images/2021/08/wamp-running.jpg)

Ouvrez votre lecteur `C` et recherchez le répertoire d'installation de votre serveur WAMP. Dans mon cas, il s'agit de `wamp64`.

![wampfolder](https://www.freecodecamp.org/news/content/images/2021/08/wampfolder.jpg)

Ouvrez le répertoire d'installation, puis le dossier `www`.

![wwwfolder](https://www.freecodecamp.org/news/content/images/2021/08/wwwfolder.jpg)

Créez un dossier là et nommez-le comme vous le souhaitez, puis ouvrez le dossier avec votre éditeur de code.

Créez un fichier `index.php` et collez le code suivant :

```php
<?php

echo "Hello World";

?>
```

Vous pouvez également mettre votre texte "Hello World" dans une variable, puis utiliser le système echo pour l'afficher dans le navigateur.

En PHP, vous pouvez déclarer une variable avec le signe dollar ($). Vos instructions, à l'exception de la dernière, doivent également être terminées par un point-virgule.

```php
<?php

$greeting = "Hello World";
echo $greeting

?>
```

Pour exécuter votre code dans le navigateur, ouvrez le navigateur et écrivez ceci dans la barre d'adresse `localhost/le-dossier-de-votre-fichier-php/fichier-php.php`, puis appuyez sur Entrée.

Assurez-vous que votre serveur WAMP ou XAMP est en cours d'exécution, sinon cela ne fonctionnera pas.

![hello-world](https://www.freecodecamp.org/news/content/images/2021/08/hello-world.jpg)

Vous pouvez voir que le code a été exécuté avec succès dans le navigateur, car j'ai obtenu le bon chemin de fichier.

Une autre belle chose à propos de PHP est que vous pouvez l'intégrer dans HTML. Vous pouvez le faire comme ceci :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code PHP</title>
</head>
<body>
    <h1> Ceci est le résultat d'un code PHP intégré dans HTML</h1>

        <?php 
            $greeting = "Hello World";
            $campers = "Hello Campers";

            echo $greeting;
            echo "<br>";
            echo $campers
        ?>
</body>
</html>
```

![php-in-html](https://www.freecodecamp.org/news/content/images/2021/08/php-in-html.jpg)

## Conclusion

PHP reste un langage pertinent et largement utilisé dans le développement web. Malgré les moqueries et les débats sur le fait qu'il soit encore précieux, les développeurs PHP continuent de gagner bien leur vie en travaillant avec ce langage. Donc, PHP ne semble pas prêt de disparaître.

Maintenant, allez coder en PHP !

Merci d'avoir lu, et continuez à coder.