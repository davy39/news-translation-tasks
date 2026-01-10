---
title: Tutoriel d'authentification Laravel – Comment configurer l'authentification
  de base dans Laravel 8
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2021-08-12T15:48:12.000Z'
originalURL: https://freecodecamp.org/news/basic-authentication-in-laravel8-using-laravel-breeze
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/download-1.png
tags:
- name: authentication
  slug: authentication
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Tutoriel d'authentification Laravel – Comment configurer l'authentification
  de base dans Laravel 8
seo_desc: "Authentication is an important feature and basic requirement in web applications\
  \ these days. And developers spend lots of time building authentication modules\
  \ for every application they create. \nBut this manual approach can get tiring and\
  \ is a bit un..."
---

L'authentification est une fonctionnalité importante et une exigence de base dans les applications web de nos jours. Et les développeurs passent beaucoup de temps à construire des modules d'authentification pour chaque application qu'ils créent. 

Mais cette approche manuelle peut devenir fatigante et est un peu improductive. C'est là que Laravel brille vraiment. Il vous permet, avec Laravel Breeze, de vous concentrer sur les fonctionnalités principales de votre application, tandis qu'il s'occupe de l'authentification pour vous.

Avant de commencer, je suppose que vous connaissez un peu de PHP si vous lisez cet article. Cela pourrait très bien être votre premier article sur Laravel, mais la connaissance de PHP sera très utile.

## Qu'est-ce que Laravel Breeze ?

Vous vous demandez peut-être - qu'est-ce que Laravel Breeze et à quoi sert-il ? [D'après la documentation](https://laravel.com/docs/8.x/starter-kits) :

> Laravel Breeze est une implémentation minimale et simple de toutes les fonctionnalités d'authentification de Laravel, y compris la connexion, l'inscription, la réinitialisation du mot de passe, la vérification par e-mail et la confirmation du mot de passe.

Laravel Breeze génère automatiquement les routes, les contrôleurs et les vues nécessaires pour inscrire et authentifier les utilisateurs de votre application.

Dans les versions précédentes de Laravel, il existait d'autres moyens de générer facilement les échafaudages d'authentification.

* Dans Laravel 7, il y avait le package `[laravel/ui](https://laravel.com/docs/7.x/authentication)`. Contrairement à Laravel Breeze, il utilisait Bootstrap au lieu de Tailwind CSS.
* Dans les versions antérieures à la 6, vous pouviez générer les échafaudages en utilisant `php artisan make:auth`.

Ainsi, Laravel Breeze est essentiellement la dernière évolution des versions précédentes.

Vous pouvez gagner beaucoup de temps de développement en utilisant Laravel Breeze, et votre application sera moins sujette aux erreurs. Cela est dû au fait que les échafaudages générés par Laravel Breeze ont été confirmés comme étant les meilleurs par les professionnels de Laravel.

Avant de commencer, vous devez avoir Composer et Laravel installés pour continuer. Vous pouvez installer Composer [ici](https://getcomposer.org/download/) et Laravel [ici](https://laravel.com/docs/8.x/installation). Plongeons dans le vif du sujet.

## Comment installer Laravel Breeze

```
composer require laravel/breeze --dev
```

Après l'installation, vous devez exécuter la commande `breeze:install` pour publier les vues d'authentification, les routes, les contrôleurs et autres ressources dans votre application. 

Laravel Breeze vous donne un contrôle total sur vos fonctionnalités et leur implémentation en publiant son code dans votre application.

```
php artisan breeze:install
```

Après avoir exécuté cette commande, vous devriez voir quelques changements dans vos fichiers. En voici quelques-uns auxquels vous devez prêter attention :

* Il a créé des contrôleurs d'authentification (un certain nombre) pour gérer l'inscription, la connexion (authentification) et la déconnexion, la confirmation du mot de passe, la vérification par e-mail, et la réinitialisation et la mise à jour du mot de passe (il envoie même un e-mail).
* Il a également créé des vues pour correspondre à toutes les actions des contrôleurs en utilisant Tailwind CSS.
* Il y a une vue de tableau de bord où les utilisateurs sont redirigés après une authentification réussie.
* Il a modifié la page d'accueil pour inclure des liens vers les pages d'authentification.
* Il a également créé des fichiers CSS et JavaScript, qui doivent être compilés plus tard.
* Il y a maintenant des routes liées à l'authentification qui sont stockées dans le fichier de routes `auth.php`.
* Des tests sont également inclus dans le répertoire `tests`.

## Comment compiler les actifs statiques

Nous allons vouloir minifier les fichiers CSS et JavaScript qui ont été générés dans les dossiers `css` et `js` du dossier des ressources, respectivement. 

Cela nous donnera un temps de chargement plus rapide et réduira également le nombre de requêtes HTTP (puisque tous les fichiers JavaScript et CSS ont été compilés en un seul fichier chacun).

De plus, comme Laravel vous donne la liberté d'utiliser votre propre préprocesseur CSS, vous allez vouloir compiler votre code pour que le navigateur puisse l'interpréter.

Maintenant, nous devons compiler nos actifs statiques pour terminer l'installation. Pour ce faire, exécutez ces commandes :

```
npm install
npm run dev
```

Gardez simplement à l'esprit que cela peut prendre un certain temps en fonction de votre vitesse de connexion Internet.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-from-2021-08-08-11-32-05.png)
_Compilation réussie_

Remarquez également que dans votre dossier `public`, vous avez maintenant des répertoires `css` et `js` qui contiennent des fichiers compilés que vous pouvez utiliser dans votre code.

## Comment configurer la base de données et effectuer les migrations

En tant qu'étape finale, vous devez configurer votre base de données et exécuter les migrations, car les données que vous avez obtenues de vos utilisateurs ne peuvent actuellement pas être stockées.

```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=breeze
DB_USERNAME=root
DB_PASSWORD=
```

```
php artisan migrate
```

Vous êtes maintenant prêt, et vous pouvez exécuter votre application :

```
php artisan serve
```

Rendez-vous sur [http://localhost:8000](http://localhost:8000) pour voir votre application en cours d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-from-2021-08-08-13-33-17.png)
_Page d'accueil_

Vous pouvez voir toutes les différentes pages comme la page de connexion, la page de mot de passe oublié, la page d'inscription et le tableau de bord :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-from-2021-08-08-13-34-00.png)
_Page de connexion_

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-from-2021-08-08-13-34-47.png)
_Page de mot de passe oublié_

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-from-2021-08-08-13-35-21.png)
_Page d'inscription_

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-from-2021-08-08-15-12-07.png)
_Tableau de bord_

Et voilà. Vous avez installé et configuré avec succès Laravel et Laravel Breeze. 🎊

## Comment ajouter un framework Front End

Les avantages de Laravel Breeze ne se limitent pas aux templates Blade. Laravel vous permet également de construire des applications monopages (SPA) avec ces avantages.

Laravel Breeze vous permet d'utiliser inertia.js (alimenté par Vue ou React), que vous pouvez facilement installer pour générer ces échafaudages si vous le souhaitez.

Si vous avez déjà installé Laravel Breeze sans framework front-end, les fichiers d'authentification précédemment générés (principalement des fichiers Blade) devront être réécrits par Laravel Breeze pour utiliser le framework.

```
php artisan breeze:install vue

// Ou
php artisan breeze:install react
```

N'oubliez pas de compiler à nouveau vos actifs.

```
npm install && npm run dev
```

## Résumé

Laravel vous aide à gagner du temps tout en vous aidant à maintenir une bonne qualité de code. Il vous permet de générer des vues, des contrôleurs et des routes d'authentification en utilisant Laravel Breeze.

Vous pouvez trouver tout le code de cet article [ici](https://github.com/Zubs/breeze).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me retrouver sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris) et [Github](https://github.com/Zubs). C'est rapide, c'est facile et c'est gratuit !