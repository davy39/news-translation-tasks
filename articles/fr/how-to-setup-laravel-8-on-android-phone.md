---
title: Comment installer Laravel 8 sur votre téléphone Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-11T16:34:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-laravel-8-on-android-phone
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-lisa-1092644--1-.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Laravel
  slug: laravel
- name: mobile app development
  slug: mobile-app-development
- name: PHP
  slug: php
seo_title: Comment installer Laravel 8 sur votre téléphone Android
seo_desc: "By Precious Oladele\nHey, how are you doing? In this article, I'm going\
  \ to show you how you can install Laravel 8 on your phone. \nTo get the most out\
  \ of this guide, you should have some knowledge of PHP and you should know what\
  \ Laravel is. But if you ..."
---

Par Precious Oladele

Salut, comment ça va ? Dans cet article, je vais vous montrer comment installer Laravel 8 sur votre téléphone. 

Pour tirer le meilleur parti de ce guide, vous devriez avoir quelques connaissances en PHP et savoir ce qu'est Laravel. Mais si ce n'est pas le cas, ne vous inquiétez pas – je vais expliquer les bases pour que vous puissiez commencer.

## Qu'est-ce que Laravel ?

Laravel est un framework d'application web avec une syntaxe expressive et élégante. Il est basé sur PHP, ce qui signifie que Laravel est PHP mais il facilite les choses.

Il est livré avec de nombreux packages pour diverses fonctionnalités, comme l'authentification, donc nous n'avons pas besoin d'écrire l'authentification nous-mêmes. Pour en savoir plus sur ce que Laravel peut faire, vous pouvez visiter le site à l'adresse [laravel.com](https://www.freecodecamp.org/news/p/8cc4755b-3b0b-4751-991c-a7b4997c0335/laravel.com).

## Pourquoi j'ai écrit ce tutoriel

J'ai créé ce tutoriel parce que je veux que les personnes intéressées par la programmation qui n'ont pas d'ordinateur portable ou de PC puissent construire des choses sur leurs téléphones. 

Mon [dernier article sur freeCodeCamp](https://www.freecodecamp.org/news/how-to-code-on-your-phone-python-pydroid-android-app-tutorial/) m'a fait réaliser que les gens sont intéressés à apprendre comment la technologie fonctionne, c'est pourquoi je fais plus de guides comme celui-ci.

Alors, plongeons-nous dedans. Dans ce tutoriel, je vais vous montrer comment installer composer.php et l'utiliser pour configurer Laravel 8 sur votre téléphone 🔥🔥. 

Je suis Precious Oladele, et j'aurai presque 19 ans ce mois-ci 🤴. Je viens du Nigeria et je vais vous guider à travers ce processus. Et si vous vous demandez comment je sais tant de choses à ce sujet, c'est parce que je n'ai pas non plus d'ordinateur portable, alors j'explore avec mon téléphone à la place 😊.

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin d'un téléphone Android avec V6.0+.

## Installation

Nous devons nous rendre sur le Play Store et télécharger **Termux** :

![Image](https://lh6.googleusercontent.com/cQlgYSj1hH3487jHevQn4eKEjC51xAn5vm0fo6tL8yfNV-nwTeLFW2kv480G5i-OjxtaKXCNQ2c5q36ywH5nqjitwKBjieL7NC4ZXmw7K3WbsuxrsKgAaQBslE9uFg_xnSOFdXc)

**Termux** est un système basé sur Linux que nous pouvons utiliser sur nos téléphones. C'est aussi simple que d'utiliser votre Linux habituel – vous pouvez installer n'importe quoi, même Kali, Ubuntu, ou ce que vous voulez. Mais pour ce tutoriel, nous allons l'utiliser pour installer Laravel 8 sur notre téléphone mobile.

## Télécharger Composer

Avant de télécharger Composer, nous devons ouvrir notre application **Termux** et taper cette commande :

```
termux-setup-storage
```

Il vous demandera des permissions de stockage, alors allez-y et cliquez sur accepter. Une fois que c'est fait, rendez-vous sur [https://getcomposer.org/download/](https://getcomposer.org/download/).

![Image](https://lh4.googleusercontent.com/6DrBqRU9swO3NdA0iEKhzhvK7bQtH3dLdKdx69YrCQboxPLIi-seYv84u_5I4dTAcAqAayNRv6wxlMxxLkivcLYi0N5-iLLYAwB9nzVKvxdMFRaY44ECp5duQLcX7j685RyK-K0)

Nous devons tout récupérer là-bas. Mais avant cela, nous devons installer **PHP** pour pouvoir l'utiliser dans notre application. Pour ce faire dans votre **Termux**, tapez la commande suivante :

```
apt install php 
```

et cliquez sur entrer. Vous devriez voir ceci :

![Image](https://lh6.googleusercontent.com/jamAoOq-pWlvWz9FfouVQVagFh1stoz-qvrCf4k_Aywd9pabMiDj8ygNR9lqCiXDmwF8M2nzHyrJoDlvrBoPAUSO4w7WY40vQlQqTWzdkDAvK8dlR9XMn19qVhLAu1iwv0E7R24)

Une fois cela fait, rendez-vous sur la page de Composer et récupérez le code. Nous devons faire cela parce que Termux est basé sur Linux. Si c'était Windows, il y aurait un simple bouton pour télécharger composer.exe. 

Copiez tout le code et rendez-vous sur Termux où vous pourrez le coller. Ensuite, cliquez sur entrer.

Lorsque Composer est installé, vous devriez voir quelque chose comme ceci :

![Image](https://lh3.googleusercontent.com/Ou_2eDdSX0ZuA0KW29MF2xNMi0YHh3f159-w7ujzGeQtIUEtEZ4mFaq4WYJLFxeGeox7lHmxMswxJcRm1fY6a2C4fZSd0329DnjPcHJvaiUs-vKerof13s2qYMCEi650q-X_qqU)

## Comment installer Laravel 8

Avant d'installer Laravel 8, vérifions si nous avons un fichier **composer.phar**. Dans votre **Termux**, tapez cette commande :

```php
ls
```

et appuyez sur entrer. Vous verrez les fichiers disponibles là.

![Image](https://lh4.googleusercontent.com/wNOLq4c37i9ccupbMQm64jvOibFEEN2ZuPi_Lez_HO6PZZalo0eI1Lp_XWwvpZK8fWgRedfNsUqo2tYsC4lN54w7TDjjFB4C3k0yR2NVcXiKRY4sFOk6tpCGjVk8X3GaIuMIJEw)

Vous pouvez voir le fichier **composer.phar** et un dossier **storage**. Le dossier storage donne accès à votre gestionnaire de fichiers. Souvenez-vous de la commande **termux-setup-storage** que vous avez écrite en premier.

Maintenant, installons Laravel 8. Pour ce faire, nous pouvons soit créer un projet, soit l'installer globalement. Mais c'est un processus un peu long lorsque vous l'installez globalement sur votre téléphone car vous devez définir un chemin, etc., et cela peut être assez confus. Donc dans ce guide, nous allons créer un projet à la place. 

Dans votre **Termux**, allez-y et tapez ceci :

```php
php composer.phar create-project laravel/laravel myapp
```

`myapp` est simplement le nom du projet – vous pouvez le changer en ce que vous voulez. Ensuite, appuyez sur entrer et attendez que la magie opère.

Lorsque vous voyez ce qui suit, cela signifie que Laravel a été installé :

![Image](https://lh5.googleusercontent.com/e1T64FywzWaz7amrgF0E5aXE6YqJdjMqCm2ZbAMeVyq2GBJ3wPXpAIxevqulsoPa2LOyqfWTtb6PjbqK48-IcWAssx6Hk3cPHyd5-N6Lw2fFWFdWEM0qhbA6ivKHjt5GH_ED5aI)

Facile comme bonjour. Maintenant, pour le tester, vous pouvez vous rendre dans `myapp` en tapant **`cd myapp`**. Ensuite, vous pouvez exécuter le serveur Laravel avec **`php artisan serve`**.

Voilà – le développement a commencé 🔥

![Image](https://lh5.googleusercontent.com/OmM_BEGUNTploSBEIItrnkn6S_yotTKJPo_q60PP7mx93Uo9V4Tb9p_ucHIiaHAOPbFGL36CWT-zWcGwc-a2FsiNbfyFpbnWu6IjT-MsS2X5TQhI1vAbhU3bGMgbM_tLC_nu3oU)

Maintenant, vous pouvez ouvrir [http://127.0](about:blank).0.1:8000 dans votre navigateur et voir que Laravel est en cours d'exécution :

![Image](https://lh5.googleusercontent.com/iG_uPbC4lzleqSPETYM6pRFsZ1BAj5PbAeTwSDNVWL2_r6V-AxpWk5iYpS-Gs2iBQUmvPZMnVoCjIk9ZtcOJj6QeCOi32dFJ-2zVJC420MIiFyN9pSKUb5sUGI2iSaJ0ITf9Wr4)

Assurez-vous également de faire cela pour que votre application **Termux** ne se ferme pas de force lorsque vous codez : 😊

![Image](https://lh5.googleusercontent.com/P6s9dGlmoHGeo2_vAmImYFSXrFgRZTUUlunlOwegzVw8QdLGKoigMhbm5lPlxsE-K5PraWkGlN6VYwzwk16FLi_A4GOGRJdCkPWB3rlc6bbZuJQN7d7s0WKkJTSu1QFTeGXABDM)

## C'est tout !

Merci d'avoir lu. J'espère que vous avez appris quelque chose de ce tutoriel. Vous devriez maintenant être en mesure d'installer Laravel sur votre téléphone Android et de commencer à l'utiliser pour construire des applications.

Si vous voulez plus de contenu de ma part, vous pouvez vous abonner à ma chaîne YouTube 👏😁 
[DevStack](https://youtube.com/channel/UCLcHGKxbEO1XGVETXqzYXLA)

%[https://www.youtube.com/watch?v=VAh6A1SpZfo&t=490s]