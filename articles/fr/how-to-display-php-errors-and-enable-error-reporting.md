---
title: Comment afficher les erreurs PHP et activer le rapport d'erreurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-22T19:35:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-display-php-errors-and-enable-error-reporting
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95ea740569d1a4ca0ee2.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: PHP
  slug: php
seo_title: Comment afficher les erreurs PHP et activer le rapport d'erreurs
seo_desc: 'By Jonathan Bossenger

  I still vividly remember the first time I learned about PHP error handling.

  It was in my fourth year of programming, my second with PHP, and I''d applied for
  a developer position at a local agency. The application required me to ...'
---

Par Jonathan Bossenger

Je me souviens encore très bien de la première fois où j'ai appris la gestion des erreurs en PHP.

C'était ma quatrième année de programmation, ma deuxième avec PHP, et j'avais postulé pour un poste de développeur dans une agence locale. La candidature exigeait que j'envoie un échantillon de code (GitHub tel que nous le connaissons n'existait pas à l'époque), alors j'ai compressé et envoyé un simple CMS personnalisé que j'avais créé l'année précédente.

L'email que j'ai reçu de la personne qui a révisé le code me glace encore les os aujourd'hui.

"J'étais un peu inquiet à propos de votre projet, mais une fois que j'ai désactivé le rapport d'erreurs, je vois qu'il fonctionne en fait assez bien".

C'était la première fois que je recherchais "rapport d'erreurs PHP", que je découvrais comment l'activer, et que je mourais intérieurement quand j'ai vu le flux d'erreurs qui m'étaient cachées auparavant.

Les erreurs PHP et le rapport d'erreurs sont des choses que de nombreux développeurs nouveaux dans le langage pourraient manquer initialement. Cela est dû au fait que, sur de nombreuses installations de serveurs web basées sur PHP, les erreurs PHP peuvent être supprimées par défaut. Cela signifie que personne ne voit ou n'est même conscient de ces erreurs.

Pour cette raison, il est bon de savoir où et comment les activer, surtout pour votre environnement de développement local. Cela vous aide à détecter les erreurs dans votre code dès le début.

## Comment afficher les erreurs PHP

Si vous recherchez "erreurs PHP" sur Google, l'un des premiers résultats que vous verrez est un lien vers la documentation de la fonction [error_reporting](https://www.php.net/manual/en/function.error-reporting.php).

Cette fonction vous permet à la fois de définir le niveau de rapport d'erreurs PHP, lorsque votre script PHP (ou collection de scripts) s'exécute, ou de récupérer le niveau actuel de rapport d'erreurs PHP, tel que défini par votre configuration PHP.

La fonction `error_reporting` accepte un seul paramètre, un entier, qui indique quel niveau de rapport autoriser. Ne passer aucun paramètre retourne simplement le niveau actuel défini.

Il existe une longue liste de valeurs possibles que vous pouvez passer en tant que paramètre, mais nous les explorerons plus tard.

Pour l'instant, il est important de savoir que chaque valeur possible existe également sous forme de constante prédéfinie PHP. Par exemple, la constante `E_ERROR` a la valeur 1. Cela signifie que vous pourriez passer `1`, ou `E_ERROR` à la fonction error_reporting, et obtenir le même résultat.

En tant qu'exemple rapide, si nous créons un fichier de script PHP `php_error_test.php`, nous pouvons voir le niveau actuel de rapport d'erreurs défini, ainsi que le définir à un nouveau niveau.

```
<?php
// affiche le niveau actuel de rapport d'erreurs
echo error_reporting();
```

```
<?php
// rapporte toutes les erreurs fatales d'exécution.
echo error_reporting(1);
```

## Configuration du rapport d'erreurs

Utiliser la fonction `error_reporting` de cette manière est idéal lorsque vous souhaitez simplement voir les erreurs liées à la partie du code sur laquelle vous travaillez actuellement.

Mais il serait préférable de contrôler quelles erreurs sont rapportées dans votre environnement de développement local, et de les enregistrer quelque part de logique, afin de pouvoir les examiner au fur et à mesure que vous codez. Cela peut être fait à l'intérieur du fichier d'initialisation PHP (ou `php.ini`).

Le fichier `php.ini` est responsable de la configuration de tous les aspects du comportement de PHP. Dans celui-ci, vous pouvez définir des choses comme la quantité de mémoire à allouer aux scripts PHP, la taille des téléchargements de fichiers à autoriser, et le(s) niveau(x) de `error_reporting` que vous souhaitez pour votre environnement.

Si vous n'êtes pas sûr de l'emplacement de votre fichier `php.ini`, une façon de le découvrir est de créer un script PHP qui utilise la fonction [phpinfo](https://www.php.net/manual/en/function.phpinfo.php). Cette fonction affichera toutes les informations relatives à votre installation PHP.

```
<?php
phpinfo();

Comme vous pouvez le voir à partir de mon phpinfo, mon fichier `php.ini` actuel est situé à `/etc/php/7.3/apache2/php.ini`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/phpinfo.png)

Une fois que vous avez trouvé votre fichier `php.ini`, ouvrez-le dans l'éditeur de votre choix, et recherchez la section intitulée 'Gestion des erreurs et journalisation'. C'est là que le plaisir commence !

## Directives de rapport d'erreurs

La première chose que vous verrez dans cette section est une section de commentaires qui inclut une description détaillée de toutes les Constantes de Niveau d'Erreur. C'est génial, car vous les utiliserez plus tard pour définir vos niveaux de rapport d'erreurs.

Heureusement, ces constantes sont également [documentées dans le Manuel PHP en ligne](https://www.php.net/manual/en/errorfunc.constants.php), pour faciliter la référence.

En dessous de cette liste se trouve une deuxième liste de Valeurs Courantes. Cela vous montre comment définir certaines combinaisons de valeurs de rapport d'erreurs couramment utilisées, y compris les valeurs par défaut, la valeur suggérée pour un environnement de développement, et les valeurs suggérées pour un environnement de production.

```
; Valeurs Courantes :
;   E_ALL (Afficher toutes les erreurs, avertissements et notices y compris les normes de codage.)
;   E_ALL & ~E_NOTICE  (Afficher toutes les erreurs, sauf les notices)
;   E_ALL & ~E_NOTICE & ~E_STRICT  (Afficher toutes les erreurs, sauf les notices et les avertissements de normes de codage.)
;   E_COMPILE_ERROR|E_RECOVERABLE_ERROR|E_ERROR|E_CORE_ERROR  (Afficher uniquement les erreurs)
; Valeur par défaut : E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED
; Valeur de Développement : E_ALL
; Valeur de Production : E_ALL & ~E_DEPRECATED & ~E_STRICT
```

Enfin, en bas de tous les commentaires se trouve la valeur actuelle de votre niveau de `error_reporting`. Pour le développement local, je suggérerais de le définir sur `E_ALL`, afin de voir toutes les erreurs.

```
error_reporting = E_ALL
```

C'est généralement l'une des premières choses que je définis lorsque je configure un nouvel environnement de développement. De cette façon, je verrai toutes les erreurs qui sont rapportées.

Après la directive error_reporting, il y a quelques directives supplémentaires que vous pouvez définir. Comme avant, le fichier php.ini inclut des descriptions de chaque directive, mais je donnerai une brève description des plus importantes ci-dessous.

La directive `display_errors` vous permet de basculer si PHP affiche les erreurs ou non. Je l'ai généralement définie sur On, afin de voir les erreurs au fur et à mesure qu'elles se produisent.

```
display_errors=On
```

La directive `display_startup_errors` permet le même basculement On/Off des erreurs qui peuvent survenir pendant la séquence de démarrage de PHP. Il s'agit généralement d'erreurs dans votre configuration PHP ou de votre serveur web, et non spécifiquement de votre code. Il est recommandé de laisser cela sur Off, sauf si vous déboguez un problème et que vous n'êtes pas sûr de ce qui le cause.

La directive `log_errors` indique à PHP s'il doit ou non enregistrer les erreurs dans un fichier de journal des erreurs. Cela est toujours activé par défaut, et est recommandé.

Le reste des directives peut être laissé par défaut, sauf peut-être pour la directive `error_log`, qui vous permet de spécifier où enregistrer les erreurs, si `log_errors` est activé. Par défaut, il enregistrera les erreurs là où votre serveur web a défini qu'elles doivent être enregistrées.

## Journalisation des erreurs personnalisée

J'utilise le serveur web Apache sur Ubuntu, et mes configurations de virtual host spécifiques au projet utilisent ce qui suit pour déterminer l'emplacement du journal des erreurs.

```
ErrorLog ${APACHE_LOG_DIR}/project-error.log
```

Cela signifie qu'il enregistrera dans le répertoire de journal par défaut d'Apache, qui est `/var/log/apache2`, sous un fichier appelé `project-error.log`. Habituellement, je remplace `project` par le nom du projet web auquel il se rapporte.

Ainsi, selon votre environnement de développement local, vous devrez peut-être ajuster cela pour répondre à vos besoins. Alternativement, si vous ne pouvez pas changer cela au niveau du serveur web, vous pouvez le définir au niveau `php.ini` à un emplacement spécifique.

```
error_log = /path/to/php.log
```

Il est utile de noter que cela enregistrera toutes les erreurs PHP dans ce fichier, et si vous travaillez sur plusieurs projets, cela pourrait ne pas être idéal. Cependant, savoir toujours vérifier ce fichier pour les erreurs pourrait mieux fonctionner pour vous, donc cela peut varier.

## Trouver et corriger ces erreurs

Si vous avez récemment commencé à coder en PHP, et que vous décidez d'activer le rapport d'erreurs, soyez prêt à gérer les conséquences de votre code existant. Vous pourriez voir certaines choses que vous n'attendiez pas, et que vous devez corriger.

L'avantage, cependant, est que maintenant que vous savez comment tout activer au niveau du serveur, vous pouvez vous assurer de voir ces erreurs lorsqu'elles se produisent, et les traiter avant que quelqu'un d'autre ne les voie !

Oh, et si vous vous demandiez, les erreurs auxquelles je faisais référence au début de cet article étaient liées au fait que je définissais des constantes incorrectement, en n'ajoutant pas de guillemets autour du nom de la constante.

```
define(CONSTANT, 'Hello world.');
```

PHP permettait (et permet peut-être encore) cela, mais cela déclenchait une notice.

```
Notice: Use of undefined constant CONSTANT - assumed 'CONSTANT' 
```

Cette notice était déclenchée chaque fois que je définissais une constante, ce qui pour ce projet était environ 8 ou 9 fois. Pas génial pour quelqu'un de voir 8 ou 9 notices en haut de chaque page...