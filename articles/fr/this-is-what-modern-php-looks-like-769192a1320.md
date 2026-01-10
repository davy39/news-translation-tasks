---
title: Voici à quoi ressemble le PHP moderne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-12T23:29:01.000Z'
originalURL: https://freecodecamp.org/news/this-is-what-modern-php-looks-like-769192a1320
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NAnxO5afaagm6GqHFfDEVw.jpeg
tags:
- name: coding
  slug: coding
- name: language
  slug: language
- name: PHP
  slug: php
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: Voici à quoi ressemble le PHP moderne
seo_desc: 'By Felipe Lopes

  The title is really pretentious, isn’t? Yeah, it is. Although I’ve been working
  with PHP for years, how could I state what are the best practices and tools for
  the job? I couldn’t, but I’m going to do so.

  I’m seeing a real change in t...'
---

Par Felipe Lopes

Le titre est vraiment prétentieux, n'est-ce pas ? Oui, c'est vrai. Bien que je travaille avec PHP depuis des années, comment pourrais-je affirmer quelles sont les meilleures pratiques et outils pour le travail ? Je ne le pourrais pas, mais je vais le faire.

Je vois un vrai changement dans la façon dont les développeurs travaillent avec PHP, non seulement le langage change radicalement pour devenir plus mature et robuste avec de nouvelles versions et améliorations, mais tout l'écosystème autour de lui change également.

De nouveaux outils, bibliothèques, frameworks et articles sont créés, des modèles sont définis pour rendre le code plus élégant et facile à comprendre. Plusieurs personnes réfléchissent à des moyens de rendre le travail (et votre vie en tant que développeur) plus productif, propre et amusant.

Je ne suis pas un adopteur précoce des nouvelles tendances, en fait, j'adopte un nouvel outil uniquement lorsque je suis sûr qu'il y a une communauté derrière lui et que je pense vraiment qu'il améliorera mon travail. Ce que je fais toujours, c'est essayer d'écrire mon code en suivant les meilleures pratiques.

À cause de cela, il m'a fallu du temps pour commencer à utiliser des choses comme Composer et PHPUnit. Il y a environ un an, plus ou moins, j'ai ouvert mon cœur à toutes ces nouvelles choses brillantes.

PSR est arrivé en premier, puis Composer, PHPUnit, Travis-ci et plusieurs autres bibliothèques et outils incroyables. J'utilise même un IDE maintenant (Vim FTW, mais PHPStorm avec l'intégration XDebug est un must pour un workflow sain) !

### Qu'est-ce que le moderne ?

![Image](https://cdn-media-1.freecodecamp.org/images/YZBaPT1Lru14OBbpx3EVkSF18fLAhwhsPRUs)
_Par [http://creativecommons.org/licenses/by/2.0](https://www.flickr.com/photos/karen_roe/" rel="noopener" target="_blank" title="Go to Karen Roe's photostream">Karen Roe</a> (Flickr) [CC BY 2.0 (<a href="http://creativecommons.org/licenses/by/2.0" rel="noopener" target="_blank" title="))]_

Il y a des tonnes d'articles sur le web sur la façon dont PHP est horrible, comment votre vie serait terrible si vous deviez travailler avec du code PHP, comment le langage est laid et tout ce que vous pourriez imaginer !

Si vous allez travailler avec du code hérité, peut-être que votre vie ne sera pas si bonne, mais si vous avez l'opportunité de travailler sur un nouveau projet et que vous pouvez utiliser tous les nouveaux outils, vous allez voir ce nouveau PHP dont je vais parler.

J'ai plusieurs problèmes à travailler avec PHP au quotidien, mais on ne peut pas fermer les yeux sur les changements qui ont lieu dans le langage, la communauté et l'écosystème. Il y a un long chemin à parcourir, mais les choses deviennent matures dans le monde de PHP.

J'ai commencé à créer un SDK pour une API interne dans l'entreprise pour laquelle je travaille, juste comme un projet personnel, et j'ai décidé de suivre les meilleures pratiques. La plupart d'entre elles, je les faisais déjà, mais j'ai apporté quelques changements dans la façon dont je fais certaines choses. Ces changements et ce que j'ai appris au cours de la dernière année sont le sujet de cet article et ce que j'appelle le PHP moderne.

### Commençons par le workflow

![Image](https://cdn-media-1.freecodecamp.org/images/OxFTdnqCE2r6crD78HLRRgtwsvv01ctxu7aT)
_TRIO FABRIKKER — [https://nos.twnsnd.co](https://nos.twnsnd.co" rel="noopener" target="_blank" title=")_

Comme je l'ai dit, je suis un nouveau venu dans le monde des IDE, mais ce fut le coup de foudre. PHPStorm est un excellent logiciel. C'est mon premier et seul IDE. C'était mon premier essai et je n'ai même pas eu besoin d'essayer un autre.

L'intégration avec XDebug est parfaite, la résolution des espaces de noms PHP, l'intégration de Composer, l'intégration de Git, l'auto-complétion, la génération de code, le refactoring de code. Je pourrais continuer ainsi.

Je ne pense pas que vous deviez utiliser un IDE, en fait, ce point est complètement personnel. Vous devriez utiliser ce qui convient à vos besoins - Vim, Atom, Emacs, Bracket, NetBeans, PHPStorm, Eclipse, peu importe. Deux points importants ici sont la productivité et l'ergonomie. Votre IDE/éditeur de texte doit être là pour vous aider.

Cependant, pour moi, un grand point est l'intégration du débogueur. Pour écrire du code pour de grands projets (en fait pour les petits aussi), vous devez utiliser un débogueur décente. Oublions ces var_dumps et print_rs. Vous devez examiner ces variables à l'exécution, analyser les traces de la pile, définir des points d'arrêt. Ces choses sont essentielles et rendent le développement et le refactoring plus faciles.

Je ne sais même pas s'il y a d'autres options ici, XDebug a tout ce dont vous avez besoin. Avez-vous quelques minutes ? Si vous ne l'avez pas encore fait, prenez un moment pour configurer XDebug et l'intégrer dans votre IDE ou éditeur de texte. Commencez à déboguer votre code en utilisant les bons outils.

L'autre outil auquel je veux attirer votre attention est GitHub. Un autre article entier pourrait être écrit sur la qualité de Git et GitHub et pourquoi vous devez commencer à garder votre code sous un système de versioning. Mais je veux vous montrer une autre raison.

Le focus ici est l'intégration.

Il y a plusieurs outils qui s'intègrent avec GitHub et vous devriez commencer à les utiliser. Ces outils peuvent générer des métriques, exécuter des tests, exécuter des jobs pour vous pendant un processus d'intégration continue et faire toutes sortes de choses dans votre workflow. L'intégration est une bonne raison pour vous de commencer à utiliser GitHub, toutes les autres sont sujet à un autre moment.

### Gestion des dépendances

![Image](https://cdn-media-1.freecodecamp.org/images/TQqLDoQvKV730jefjQIuEyaUOSYyAY596Tzg)
_INSTITUTO PASTEUR. LISBOA, PORTUGAL — [https://nos.twnsnd.co](https://nos.twnsnd.co" rel="noopener" target="_blank" title=")_

Un autre point dans cet écosystème PHP moderne est la gestion des dépendances, et Composer est l'outil pour le travail.

Composer a 5 ans, mais il me semble que l'adoption massive a eu lieu il y a quelques années. Peut-être parce que je ne suis pas un adopteur précoce ou peut-être parce que les développeurs PHP sont réticents au changement.

Cet outil fournit une interface frontale pour Packagist, qui est un dépôt de paquets PHP composé de bibliothèques PHP, de projets et d'outils, dont le code source est stocké dans Github (ou d'autres endroits comme BitBucket).

Toutes les bibliothèques dont je parle dans cet article, et peut-être l'un de ces projets personnels, peuvent être ajoutées à votre projet avec un simple

```
$ composer require package_vendor/package_name
```

Si vous ne connaissez pas le fournisseur d'un paquet, vous pouvez `rechercher` un paquet pour trouver et installer le bon.

```
$ composer search package_name
```

Composer serait un excellent outil s'il faisait simplement ce travail, gérer les dépendances, mais il fait beaucoup plus. Prenez le temps d'installer Composer et de lire la [documentation](https://getcomposer.org/doc/).

### Interface de ligne de commande bien faite

J'aime vraiment essayer des idées rapidement en utilisant des interfaces CLI. Pour moi, l'un des meilleurs outils REPL est [IPython](https://ipython.org/). Il vous aide à auto-compléter votre code, vous permet de définir facilement des fonctions, facilite l'accès à la documentation et plusieurs autres fonctionnalités incroyables. L'inconvénient pour nous, l'outil est pour Python, pas PHP.

Dans le monde PHP, nous avons quelque chose appelé "mode interactif" qui peut être accessible par le terminal, en tapant simplement

```
$ php -aInteractive mode enabled
```

```
php >
```

À ce stade, vous êtes en mode interactif et pouvez commencer à tester quelque chose. Cela fonctionne, mais l'outil est tout simplement trop peu intuitif. Je l'ai essayé plusieurs fois mais, puisque je savais ce que IPython était capable de faire, je ne pouvais pas continuer à l'utiliser.

Pour notre chance, il y a un nouvel outil CLI (interface de ligne de commande) sur le bloc et son nom est Psysh. Psysh est un outil incroyable, plein de fonctionnalités intéressantes et peut être installé globalement ou par projet en utilisant Composer.

La fonctionnalité la plus agréable de Psysh pour moi est la documentation en ligne. Accéder à la documentation pour une fonction PHP sans se rendre sur Php.net est génial. L'inconvénient est que vous devez faire quelques choses avant qu'elle ne soit pleinement fonctionnelle.

Après l'avoir installé, tapez les commandes suivantes (j'utilise Debian ici, cela peut ne pas fonctionner pour tout le monde) afin de le faire fonctionner correctement

```
$ apt-get install php7.1-sqlite3$ mkdir /usr/local/share/psysh$ wget http://psysh.org/manual/en/php_manual.sqlite -o /usr/local/share/psysh/php_manual.sqlite
```

La première commande n'est pas obligatoire et si vous avez déjà installé Sqlite, vous pouvez sauter cette étape. La deuxième commande crée le répertoire pour stocker la documentation et la troisième ligne télécharge et sauvegarde la documentation dans le répertoire précédemment créé. N'oubliez pas, toutes ces commandes doivent être exécutées en tant que root.

Maintenant, vous avez ceci

![Image](https://cdn-media-1.freecodecamp.org/images/PLyALiyVTXJ5076Iq7s9f085JJxWdJWGqo-X)
_Capture d'écran de la documentation psysh en action, montrant des informations sur json_decode_

Rendez-vous sur [Psysh](http://psysh.org) et découvrez-en plus sur cet outil incroyable.

### Vous devriez commencer à tester

C'est un mantra que je me répète chaque jour. Comme beaucoup de gens, je ne teste pas mon code autant que le TDD le suggère. Je commence à tester maintenant et je le fais depuis les six derniers mois, et il y a un long chemin à parcourir.

J'ai décidé d'apprendre à tester en travaillant sur un projet hérité complexe. Le code était si fragile et rigide que chaque fois que nous ajoutions du code, cela cassait quelque chose. Nouvelle fonctionnalité ? Implémentez et cassez quelque chose ! Correction d'un bug ? Créez-en un autre.

C'était un gros problème, dont j'ai discuté dans [un autre article](https://medium.freecodecamp.org/few-thoughts-on-legacy-hell-e229f76529e0), et cela m'a fait commencer à donner une chance aux tests.

Le premier outil qui m'a été présenté était [PHPUnit](https://phpunit.de/). Comme indiqué sur le site officiel

> PHPUnit est un framework de test orienté programmeur pour PHP.  
> C'est une instance de l'architecture xUnit pour les frameworks de test unitaire.

Donc, PHPUnit est un framework pour vous aider à créer des tests pour vos projets, des tests unitaires. Il vous donne plusieurs fonctions pour tester le résultat de votre code et générer une sortie agréable avec le résultat de ces tests.

Depuis que j'ai commencé à réfléchir aux tests, à lire et à parler aux gens à ce sujet, j'ai découvert un autre outil incroyable, qui complète le travail que vous avez mis dans ces tests unitaires, il s'appelle Behat, qui est un framework BDD pour PHP.

BDD (Behavior-Driven Development) est un processus de développement qui vient du TDD (Test-Driven Development). Ces acronymes ne sont pas importants maintenant, ce qui est important, c'est que vous pouvez spécifier vos tests en utilisant un langage plus naturel, un langage que les non-techniciens peuvent comprendre.

Ce langage s'appelle Gherkin et est utilisé pour décrire le comportement attendu testé. Une description de test, utilisant Gherkin, ressemble à ceci

![Image](https://cdn-media-1.freecodecamp.org/images/m0wRKIZ8qPUqDcmhRejF4pes2rLYVJoR4mRJ)

Derrière ces lignes, il y a du code PHP qui est appelé chaque fois qu'il y a une correspondance entre une ligne et un motif regex spécifié dans le PhpDoc de la méthode. Ce code implémente ces étapes et ce qu'un utilisateur réel ferait, en utilisant votre SDK, application ou système web.

Le workflow avec Behat est si fluide. Après tout bien configuré, vous commencez à écrire tous les scénarios possibles pour tester une fonctionnalité. La première fois que vous exécutez Behat, il vous donne tous les modèles de méthodes que vous devriez ajouter à votre classe de contexte PHP afin d'implémenter chaque étape d'un scénario.

Après cela, vous commencez à écrire le code réel pour chaque étape et continuez à répéter ce cycle.

* Implémenter le code PHP pour une étape
* Exécuter les tests
* Si tout est correct, écrire le code PHP pour une autre étape
* Si quelque chose est cassé, le corriger

Après une demi-heure de configuration et de lecture de la documentation, vous êtes prêt à utiliser Behat, vous verrez qu'à la fin, c'est tout du code PHP et vous savez déjà comment programmer avec.

### Intégration Continue

L'intégration continue (CI) est un processus - une façon de faire quelque chose, et cette chose, pour nous ingénieurs logiciels, est la création de logiciels.

En anglais simple, c'est l'acte d'incorporer constamment de petits morceaux de code (peut-être plusieurs fois par jour) dans votre base de code. Du code qui a été testé et qui n'a rien cassé. CI vous aide à automatiser la construction, les tests et le déploiement de vos applications.

Avec quelques clics, vous pouvez intégrer votre projet GitHub avec Travis CI et chaque push vers votre dépôt exécutera ces tests que vous avez créés avec PHPUnit et Behat, vous indiquant si la dernière fonctionnalité que vous avez implémentée est prête, ou non, à être fusionnée. En outre, vous pouvez utiliser Travis CI pour déployer votre code en production et en staging.

Avoir un bon pipeline de travail avec un processus bien défini est génial et Travis CI peut vous aider dans ce travail. Suivez ce [Getting started](https://docs.travis-ci.com/user/getting-started/) et découvrez à quel point il est intéressant de réfléchir au processus de développement logiciel, pas seulement au code lui-même.

### Adhérer à PSR-1 et PSR-2

Si vous ne savez pas ce qu'est PSR, vous devriez. En fait, PSR signifie PHP Standard Recommendations et est proposé par [PHP-FIG](http://www.php-fig.org/) (PHP Framework Interop Group), un consortium formé par des membres des plus grands projets PHP, frameworks et CMS, qui réfléchissent à l'avenir du langage, de l'écosystème et discutent des normes à suivre.

Pendant longtemps, PHP n'avait pas de style de codage. Je ne suis pas si vieux, mais chaque fois que je regardais le projet ou la bibliothèque de quelqu'un, il suivait un style différent. Parfois l'accolade était laissée dans une position, parfois elle était mise à la ligne suivante, différentes approches étaient utilisées pour traiter les longues lignes et toutes les autres combinaisons de style et de préférence que vous pourriez imaginer. C'était un désordre.

PHP-FIG fait beaucoup d'autres travaux, mais en proposant une seule unité de code, ils disent "Arrêtons de nous soucier du style de code, suivons tous une norme et commençons à penser à créer de grands logiciels". Maintenant, chaque fois que vous regardez le code de quelqu'un, vous vous souciez seulement de comprendre comment il fonctionne, pas de blâmer le format, la structure.

Il y a, à la fin de cet article, 9 PSR acceptés proposant des solutions communes pour des problèmes communs. Mais si vous ne savez rien de ces normes, commencez par [PSR-1](http://www.php-fig.org/psr/psr-1/) et [PSR-2](http://www.php-fig.org/psr/psr-2/).

Ces normes proposent le style de codage PHP moderne. Assurez-vous de les lire avant de commencer à les utiliser. Ne pensez pas que vous vous souviendrez de toutes lorsque vous coderez, c'est un processus, mais pour vous en assurer, il y a des outils pour vous aider.

[PHP CodeSniffer](https://packagist.org/packages/squizlabs/php_codesniffer) est un outil que vous pouvez trouver sur Packagist et que vous pouvez installer avec Composer. Je ne pense pas que le nom du dépôt était le meilleur choix, car il contient deux outils différents, phpcs et phpcbf.

Phpcs est le renifleur de code, il analysera tout votre code, à la recherche de parties qui ne suivent pas la norme de codage configurée.

Vous pouvez utiliser plusieurs normes de codage avec phpcs et vous pouvez même créer la vôtre. À la fin de l'analyse du code, phpcs vous montre une liste des morceaux de code ne suivant pas la norme. C'est génial.

Maintenant, comment changer tout ce qui est faux ? Vous pourriez ouvrir chaque fichier, changer le code, exécuter phpcs à nouveau, voir l'erreur ne pas être affichée, et répéter le processus. Ce sera extra ennuyeux.

Pour résoudre ce problème, PHP CodeSniffer est venu avec un autre outil, appelé phpcbf, ou PHP Code Beautifier. Vous exécutez phpcbf, en suivant le même ensemble de règles et, voilà, il corrige tout pour vous, ou il essaie de faire de son mieux sans casser votre code.

Essayez de créer l'habitude d'exécuter phpcs et phpcbf avant de pousser des changements dans votre code vers le dépôt, cela garantira que tout votre code adhère aux normes et si quelqu'un aime votre outil/projet et veut contribuer, il n'aura aucun problème à le lire.

### Frameworks

Je ne vais pas consacrer trop de temps à discuter des frameworks. Il y en a plusieurs bons, chacun avec ses avantages et ses inconvénients. Personnellement, je préfère ne pas utiliser ces grands frameworks, avec tout à l'intérieur. J'aime l'idée que vous devez utiliser seulement ce dont vous avez besoin.

Si vous avez besoin d'un client HTTP, utilisez Guzzle. Si vous avez besoin d'un moteur de template, utilisez Twig. Si vous avez besoin d'un routeur, trouvez un bon composant qui convient à vos besoins et utilisez-le. Collez ces composants ensemble et créez votre application.

[Symfony](https://symfony.com/) fait un excellent travail vers ce concept. Vous pouvez utiliser l'ensemble du framework pour un projet, ou vous pouvez simplement prendre ce que vous voulez et l'utiliser. Simple comme ça.

Cependant, chaque fois que j'ai besoin d'un framework pour écrire une application, je choisis l'un des soi-disant microframeworks. Ils sont vraiment petits, offrent seulement les bases et sont faciles à personnaliser et plus faciles à faire suivre la structure de votre projet.

Mon microframework de choix est [Slimframework](https://www.slimframework.com/) et je pense que vous devriez le lire. Il est simple pour faire de petits projets, mais il devient un peu plus complexe pour les plus grands.

Au fait, et c'est pour ceux qui commencent avec la programmation, je pense vraiment que avant d'adopter un framework et de mourir pour lui, vous devriez essayer de créer le vôtre. Cela vous donnera la compréhension du mécanisme entier et facilitera l'adoption d'un grand framework.

### L'ensemble d'outils PHP moderne

Terminons cet article avec une liste de liens. Pour moi, ces composants, outils et bibliothèques représentent une grande partie de ce qu'est le PHP moderne :

* [Slimframework](https://www.slimframework.com/) : un microframework sympa et cool
* [Symfony](http://symfony.com/) : un framework plus grand qui est rempli de composants réutilisables
* [Guzzle](http://docs.guzzlephp.org/en/stable/) : un client HTTP simple et facile à utiliser
* [PHPUnit](https://phpunit.de/) : un framework pour les tests unitaires
* [Behat](http://behat.org/en/latest/) : un framework pour le développement piloté par le comportement
* [PHPCS/CBF](https://github.com/squizlabs/PHP_CodeSniffer) : renifleur de code et embellisseur de code
* [Faker](https://github.com/fzaninotto/Faker) : générateur de données fictives
* [Psysh](http://psysh.org/) : une console de développement en temps réel (CLI) pleine de fonctionnalités incroyables
* [Composer](https://getcomposer.org/) : gestion des dépendances et autres fonctionnalités utiles
* [Packagist](https://packagist.org/) : dépôt de paquets
* [Twig](https://twig.symfony.com/) : moteur de template

Le titre était vraiment prétentieux, je sais. Ce que je voulais vraiment montrer ici, c'est que PHP évolue et que l'écosystème évolue au même rythme (peut-être plus vite).