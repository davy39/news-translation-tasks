---
title: 'S''éloigner de la magie — ou : pourquoi je ne veux plus utiliser Laravel'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T22:34:12.000Z'
originalURL: https://freecodecamp.org/news/moving-away-from-magic-or-why-i-dont-want-to-use-laravel-anymore-2ce098c979bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C547D5BdRsA6qdzFz-5GgA.jpeg
tags:
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
seo_title: 'S''éloigner de la magie — ou : pourquoi je ne veux plus utiliser Laravel'
seo_desc: 'By Niklas Schöllhorn

  It is time for a change in the tools that I use. And I’ll tell you why!

  First of all, I want to make sure that you know about my intentions. I am not trying
  to rant about Laravel or why other frameworks might be better.

  This arti...'
---

Par Niklas Schöllhorn

_Il est temps de changer les outils que j'utilise. Et je vais vous dire pourquoi !_

Tout d'abord, je veux m'assurer que vous connaissez mes intentions. Je ne cherche pas à critiquer Laravel ou à expliquer pourquoi d'autres frameworks pourraient être meilleurs.

Cet article est très subjectif. Je vais vous donner mes réflexions et essayer de vous faire reconsidérer vos choix de framework. Et si vous restez avec Laravel après cette réévaluation, c'est très bien. Je n'ai pas l'intention de convertir les gens de Laravel vers d'autres frameworks ou langages. Mais il est important de regarder de plus près et de s'assurer que vous savez **ce** que vous utilisez et **pourquoi** vous l'utilisez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C547D5BdRsA6qdzFz-5GgA.jpeg)
_Noyade à cause de trop de magie. Photo par [Unsplash](https://unsplash.com/photos/PC_lbSSxCZE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Kristopher Roller</a> sur <a href="https://unsplash.com/search/photos/magic?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Introduction

J'ai travaillé avec Laravel pendant environ 2 ans. J'ai toujours apprécié la facilité avec laquelle on pouvait lancer une application et commencer en quelques minutes. Il fournit tant d'outils utiles prêts à l'emploi. Les commandes console vous assistent à chaque étape du codage. Elles génèrent des classes, des échafaudages pour l'authentification et bien plus encore.

Mais plus vous avancez et plus les projets deviennent grands, plus le développement avec Laravel devient compliqué. Ou, laissez-moi reformuler : plus les autres outils feront mieux le travail. Je ne dis pas que c'est uniquement de la faute de Laravel. C'est aussi partiellement dû au fait que PHP n'est pas très bien conçu.

Maintenant, commençons !

### Eloquent ORM

Si vous avez déjà travaillé avec Laravel, vous connaissez sûrement Eloquent. C'est l'ORM qui est fourni avec une installation par défaut. Il vient avec beaucoup de fonctionnalités pratiques. Mais sa conception rend votre application inutilement complexe et empêche l'IDE d'analyser correctement votre code.

Cela est partiellement dû au modèle **Active Record ORM** qui est utilisé et partiellement au fait qu'Eloquent veut éviter au développeur d'avoir à écrire plus de code. Pour ce faire, il permet au développeur de mettre beaucoup de choses dans le modèle qui n'y appartiennent pas.

Cela semble être de bonnes intentions, mais j'ai commencé à aimer de moins en moins cela.

Examinons un exemple :

La première chose que vous voyez est qu'il n'y a **aucune propriété** sur le modèle. Cela semble sans importance, mais pour moi, cela fait une grande différence. Tout est injecté « magiquement » dans la classe en lisant les métadonnées de la table. Bien sûr, votre IDE ne comprend pas cela sans aide. Et vous n'avez aucune chance de nommer vos propriétés différemment de vos colonnes.

Maintenant, regardez la méthode de portée. Pour les utilisateurs de Laravel, il est assez clair ce qu'elle fait. Si vous appelez cette méthode, elle limite la requête SQL sous-jacente en ajoutant la clause WHERE donnée.

Vous pouvez voir qu'elle n'est pas statique. Cela signifierait que cette méthode opère sur un objet spécifique de la classe. Mais dans ce cas, **ce n'est pas le cas**. Une portée est appelée sur un générateur de requêtes. Elle n'a **rien** à voir avec l'objet modèle lui-même. Je vais expliquer cela après que vous ayez vu comment vous appelez généralement ces portées :

Vous appelez une méthode statique `popular()` que personne n'a jamais définie. Mais puisque Laravel définit une méthode `__call()` et `__callStatic()`, elle est gérée par elles. [Ces méthodes transmettent l'appel à un générateur de requêtes.](https://github.com/laravel/framework/blob/5.7/src/Illuminate/Database/Eloquent/Model.php#L1610)

Ce n'est pas seulement quelque chose que votre IDE ne comprend pas. Cela rend le refactoring plus difficile, peut confondre les nouveaux développeurs, et [l'analyse statique](https://en.wikipedia.org/wiki/Static_program_analysis) devient également plus difficile.

De plus, en mettant de telles méthodes sur votre modèle, vous violez le S de [SOLID](https://hackernoon.com/solid-principles-made-easy-67b1246bcdf). Au cas où vous ne seriez pas familier avec cela, SOLID est un acronyme qui signifie :

* **S**ingle Responsibility Principle (Principe de responsabilité unique)
* **O**pen/Closed Principle (Principe ouvert/fermé)
* **L**iskov Substitution Principle (Principe de substitution de Liskov)
* **I**nterface Segregation Principle (Principe de ségrégation des interfaces)
* **D**ependency Inversion Principle (Principe d'inversion des dépendances)

Lorsque vous utilisez Eloquent, vos modèles ont plusieurs responsabilités. Il contient les données de votre base de données, ce que font habituellement les modèles, mais il contient également une logique de filtrage, peut-être de tri et bien plus encore. Vous ne voulez pas cela.

### Aides globales

Laravel vient avec plusieurs fonctions d'aide globales. Elles semblent très pratiques et oui, elles _sont_ pratiques.

Vous devez simplement savoir que vous sacrifiez votre indépendance pour cette praticité et que votre espace de noms global est pollué. Cela conduit rarement à des conflits, mais éviter cela devrait être préféré.

Regardons quelques exemples. Voici une liste de trois méthodes d'aide que nous avons mais dont nous n'avons pas besoin puisque de meilleures alternatives existent :

* `app_path()` — pourquoi ? Si vous avez besoin du chemin de l'application, demandez à l'objet application. Vous l'obtenez par typage.
* `app()` — quoi ? Nous n'avons pas besoin de cette méthode. Nous pouvons injecter l'instance de l'application !
* `collect()` — Cela crée une nouvelle instance de la classe Collection. Nous pouvons simplement instancier un objet nous-mêmes.

Un autre exemple concret :

Nous utilisons l'aide globale `request()` de Laravel pour récupérer les données POST et les mettre dans notre modèle comme attributs.

Au lieu d'utiliser l'aide globale, nous pourrions typer un objet `Request` comme paramètre dans la méthode du contrôleur. Le dispatcher dans Laravel sait comment nous fournir l'objet nécessaire. Il appellera notre méthode avec celui-ci et nous n'aurons pas à appeler une aide.

Et nous pouvons aller plus loin pour découpler davantage. Laravel est conforme à [PSR-7](https://www.php-fig.org/psr/psr-7/). Donc, au lieu de typer l'objet Request, vous pourriez également typer `ServerRequestInterface`. Cela vous permet de remplacer tout le framework par n'importe quoi qui est conforme à PSR-7. Tout dans cette méthode continuera à fonctionner. Cela échouerait si vous utilisiez encore les méthodes d'aide. Le nouveau framework ne viendrait pas avec la méthode d'aide et donc, vous devriez réécrire cette partie de votre code.

Vous remplacez rarement tout le framework, mais [il y a des gens qui le font.](https://dannyvankooten.com/from-go-back-to-php-again/) Et même si _vous_ ne le ferez peut-être jamais, c'est toujours important pour l'interopérabilité. Pouvoir injecter des dépendances et avoir un flux de données concis au lieu de résoudre et de demander des dépendances et des données de l'intérieur vers l'extérieur est la voie à suivre. Cela rend les tests, le refactoring et presque tout plus facile lorsque vous en avez la maîtrise.

J'étais heureux lorsque j'ai lu qu'avec Laravel 5.8 [les aides de chaîne et de tableau sont retirées du noyau et mises dans un package séparé.](https://laravel-news.com/laravel-5-8-deprecates-string-and-array-helpers) C'est un bon premier pas. Mais la documentation devrait commencer à décourager l'utilisation de **toutes** les fonctions d'aide.

### Façades

Les arguments de la dernière partie entrent également en jeu ici. Les façades semblent être un outil pratique pour accéder rapidement à certaines méthodes qui ne sont pas vraiment statiques. Mais elles vous lient une fois de plus au framework. Vous les utilisez pour résoudre manuellement les dépendances au lieu d'instruire l'environnement de les fournir.

Il en va de même pour la complexité en passant tout par les méthodes magiques.

Puisque nous parlions du support de l'IDE, je sais que certains d'entre vous pourraient me diriger vers le [package d'aide à l'IDE](https://github.com/barryvdh/laravel-ide-helper) de barryvdh. Vous n'avez pas besoin de le faire. Je connais déjà ce package. Mais pourquoi est-il même nécessaire ? Parce que certaines décisions de conception dans Laravel ne sont tout simplement pas bonnes. Il existe des frameworks où vous n'avez pas besoin de cela. Prenez Symfony par exemple. Pas besoin de fichiers d'aide à l'IDE, car il est bien conçu et implémenté.

Au lieu des façades, nous pourrions utiliser l'injection de dépendances comme nous l'avons fait dans l'exemple précédent. Nous aurions un vrai objet et pourrions appeler de vraies méthodes dessus. Bien mieux.

Je vais vous donner un autre exemple :

Nous pourrions facilement nettoyer cela. Disons à Laravel d'injecter une `ResponseFactory` et de nous passer la requête actuelle :

Nous avons maintenant réussi à éliminer l'utilisation des façades de notre contrôleur. Le code reste propre et compact, sinon même meilleur qu'avant. Et puisque nos contrôleurs étendent toujours la classe générale `Controller`, nous pourrions aller plus loin en déplaçant la fabrique de réponse vers cette classe parente. Nous en avons besoin dans toutes les autres classes de contrôleur de toute façon.

J'ai entendu dire que certaines personnes fournissent « trop de paramètres de constructeur » comme argument contre l'injection de tout. Mais je ne suis pas d'accord avec cela. Cela ne fait que cacher les dépendances et donc la complexité en premier lieu. Si vous n'aimez pas avoir 10 à 20 arguments dans votre constructeur, vous avez raison.

La solution n'est pas magique cependant. Avoir besoin de tant de dépendances dans une seule classe signifie que cette classe a probablement trop de responsabilités. Au lieu de cacher cette complexité, refactorisez cette classe. Divisez-la en de nouvelles et améliorez l'architecture de votre application.

Fait amusant : il existe un vrai modèle de conception appelé « modèle de façade », introduit dans le livre du Gang of Four. Mais il a une signification complètement différente. Les façades de Laravel sont essentiellement des **localisateurs de service statiques**. La nomenclature ne transmet tout simplement pas cela. Le même nom pour des choses différentes rend également les discussions sur l'architecture dans les projets plus difficiles, car l'autre partie pourrait s'attendre à quelque chose de complètement différent derrière ce nom.

### Conclusion

Venons-en à la fin. Je pourrais bientôt écrire une suite sur les technologies que je préfère utiliser de nos jours. Mais pour l'instant, laissez-moi résumer ce que nous avons appris :

L'approche de Laravel pour rendre tout aussi facile que possible est bonne. Mais il est difficile de s'en sortir lorsque vos applications deviennent plus avancées. Je préfère un excellent support IDE, un typage plus fort, de vrais objets et une bonne ingénierie. Je pourrais même revenir à Laravel lorsque je veux écrire une application plus petite.

Beaucoup de mes points ne sont pas uniquement de la faute de Laravel. Je pourrais échanger les parties que je n'aime pas, par exemple l'ORM. Mais au lieu de cela, je vais simplement changer de boîte à outils, où les valeurs par défaut correspondent mieux à mes besoins. Je ne vois aucun intérêt à utiliser un framework où je dois passer plus de temps à éviter les pièges qu'il pose pour une mauvaise ingénierie qu'à développer mon application. D'autres frameworks et outils viennent avec des valeurs par défaut mieux conçues et moins de magie.

Alors pour l'instant, je vais dire au revoir à Laravel.

Merci pour votre temps. J'apprécierais une discussion intéressante dans les commentaires et je suis bien sûr ouvert à vos questions et suggestions.

P.S. : Un merci spécial à [Marco Pivetta](https://www.freecodecamp.org/news/moving-away-from-magic-or-why-i-dont-want-to-use-laravel-anymore-2ce098c979bd/undefined) pour la relecture et les contributions supplémentaires !

_Édition du 1er mars 2019 :_  
Depuis que mon article a été publié sur Reddit, j'ai créé un compte Reddit pour répondre à quelques commentaires. Mon compte n'est pas celui depuis lequel l'article a été publié, mais celui-ci : [https://reddit.com/u/nschoellhorn](https://reddit.com/u/nschoellhorn)

_Édition du 13 mars 2019 :_  
Si vous avez lu jusqu'ici, vous pouvez également consulter mon [profil Twitter](https://twitter.com/nschoellhorn). Merci pour votre intérêt continu pour ce sujet ! Je suis toujours ouvert aux discussions productives, alors n'hésitez pas à me contacter, soit ici, soit sur Twitter.