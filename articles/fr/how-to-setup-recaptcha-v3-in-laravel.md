---
title: Comment configurer reCAPTCHA v3 dans un projet Laravel
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2021-09-20T22:26:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-recaptcha-v3-in-laravel
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-davis-sanchez-1727004.jpg
tags:
- name: Laravel
  slug: laravel
- name: Web Security
  slug: web-security
seo_title: Comment configurer reCAPTCHA v3 dans un projet Laravel
seo_desc: "In this article, you'll learn how to set up reCAPTCHA v3 in your Laravel\
  \ project. This can be a bit tricky, so I'll help you simplify the process here.\
  \ \nWhat is reCaptcha?\nreCaptcha is a Google service provided for free that helps\
  \ you protect your we..."
---

Dans cet article, vous apprendrez comment configurer reCAPTCHA v3 dans votre projet Laravel. Cela peut être un peu délicat, alors je vais vous aider à simplifier le processus ici. 

## Qu'est-ce que reCaptcha ?

[reCaptcha](https://developers.google.com/recaptcha/) est un service Google fourni gratuitement qui vous aide à protéger vos sites web contre le spam et les attaques malveillantes. 

La nouvelle version, V3, présente de nombreuses améliorations par rapport aux versions précédentes grâce aux nouveaux défis captcha. Elle retourne un score et des analyses que vous pouvez utiliser pour prendre des mesures appropriées pour votre site web.

Voici à quoi ressemble la version précédente de reCaptcha – mais avec la dernière version (v3), reCaptcha a beaucoup changé et offre une meilleure expérience utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/newCaptchaAnchor.gif)
_Version précédente de reCaptcha_

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-26-at-04.11.28.png)
_Version précédente de reCaptcha_

## Ce que vous allez apprendre

À la fin de cet article, vous aurez appris les points suivants :

1. Comment intégrer reCaptcha v3 dans votre projet Laravel
2. Comment configurer un tableau de bord d'administration Google reCaptcha
3. Comment consulter les scores et les analyses de reCaptcha de votre site pour vous aider à prendre de meilleures décisions de sécurité

## Comment configurer reCaptcha dans un projet Laravel

Vous pouvez suivre ces étapes simples pour configurer reCaptcha sur votre projet.

1. Installez ce [projet Laravel](https://laravel.com/docs/8.x/installation) si vous ne l'avez pas encore fait
2. Dans le terminal, ajoutez le package open-source à votre projet avec Composer.

```
composer require biscolab/laravel-recaptcha
```

3. Publiez le fichier `recaptcha.php` avec cette commande :

```php
php artisan vendor:publish --provider="Biscolab\ReCaptcha\ReCaptchaServiceProvider"
```

Cela créera un fichier dans le répertoire de configuration, appelé `config\recaptcha.php`, où nous ajouterons plus de configurations reCaptcha.

4. [Visitez ce lien](https://www.google.com/recaptcha/admin/create) pour créer un compte administrateur reCaptcha pour vous-même.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/reCAPTCHA-2021-07-23-10-59-07.png)
_Enregistrer reCaptcha v3_

Pour créer l'administrateur reCaptcha, vous pouvez faire ce qui suit :

* Ajoutez le nom de votre site dans l'étiquette – `localhost` ou `examplesite.com`
* Sélectionnez v3 comme type de reCaptcha
* Incluez les domaines dans la section des domaines (`localhost` ou `examplesite.com`)
* Ajoutez l'adresse e-mail du propriétaire dans la section du propriétaire
* Cochez la case "accepter les termes et conditions"

Juste une note – le localhost est uniquement destiné au développement local. Par conséquent, il doit être mis à jour avant de passer à un environnement de production.

5. Ajoutez reCaptcha à votre site

Cliquez sur le bouton de soumission et enregistrez vos clés secrètes. 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/reCAPTCHA-2021-07-23-11-16-17.png)
_Ajout de reCaptcha à votre site dans le fichier .env_

6. Ajoutez les clés du site au fichier `.env` de votre projet :

```php
RECAPTCHA_SITE_KEY=ADD_YOUR_SITE_KEY
RECAPTCHA_SECRET_KEY=ADD_YOUR_SECRET_KEY
RECAPTCHA_SITE=https://www.google.com/recaptcha/admin/
```

Puisque vous avez apporté des modifications au fichier `.env`, il est préférable de vider toutes les configurations mises en cache afin que les nouvelles modifications prennent effet. Utilisez `php artisan optimize:clear` dans votre terminal.

7. Dans le fichier `config > recaptcha.php`, mettez à jour la propriété de la version à V3. Il est également important de noter que les clés `api_site_key` et `api_secret_key` générées via le tableau de bord d'administration seront référencées à partir de ce que nous avons défini dans le fichier .env du projet.

```php
return [
	'version'                      => 'v3'
]
```

Vous pouvez maintenant vous rendre sur la page d'analyse de l'administrateur reCaptcha pour voir comment votre site se comporte, consulter vos scores et prendre des décisions lorsque vous êtes dans un environnement de production.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/reCAPTCHA-2021-07-24-10-27-04-1.png)
_page d'analyse de reCaptcha_

L'image ci-dessous montre que reCaptcha a été implémenté.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-19-at-15.37.00.png)



## Conclusion

À la fin de cet article, j'espère que vous trouverez plus facile de configurer reCaptcha et que vous aurez une meilleure compréhension de ce que c'est. Maintenant, vous devriez être en mesure de configurer la version la plus récente dans votre projet Laravel.

### Ressources

* Qu'est-ce que [reCaptcha](https://developers.google.com/recaptcha/) ?
* Dépôt Laravel reCaptcha [repo](https://github.com/biscolab/laravel-recaptcha)
* Documentation Laravel reCaptcha [docs](https://laravel-recaptcha-docs.biscolab.com/docs/configuration)