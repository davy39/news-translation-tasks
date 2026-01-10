---
title: Comment fonctionne la journalisation dans les applications Laravel
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2023-01-06T19:38:55.000Z'
originalURL: https://freecodecamp.org/news/laravel-logging
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/how-logging-works-laravel.png
tags:
- name: lavarel
  slug: lavarel
- name: logging
  slug: logging
seo_title: Comment fonctionne la journalisation dans les applications Laravel
seo_desc: "Logs are records of the events happening with your application. Laravel,\
  \ by default, writes log information into the laravel.log file that ships with a\
  \ fresh Laravel installation. The file is housed within the storage > logs directory.\
  \ \nIn this tutor..."
---

Les logs sont des enregistrements des événements se produisant dans votre application. Laravel, par défaut, écrit les informations de log dans le fichier laravel.log qui est fourni avec une nouvelle installation de Laravel. Le fichier est situé dans le répertoire `storage > logs`. 

Dans ce tutoriel, vous apprendrez les points suivants :

* Introduction à la journalisation
* Comprendre les configurations de log
* Pilotes de canaux pour les fichiers de log
* Formater les messages de log

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-05-at-23.26.03.png)
_Image du fichier de log_

## Introduction à la journalisation

Laravel fournit un log de ce qui se passe dans votre application. Le service de log est construit sur la bibliothèque open-source Monolog. 

Le service de journalisation est robuste car il vous permet d'écrire des messages de log dans des fichiers et d'envoyer les messages critiques à des équipes sur Slack (si configuré), Socket, des bases de données et d'autres services web. 

Le canal sur lequel vous souhaitez écrire vos informations de log est défini par l'équipe, car il existe plusieurs canaux supportés par Laravel. En fonction de la gravité des informations de log, l'écriture des informations peut également être effectuée sur plusieurs canaux. Vous verrez comment faire cela dans la section configuration.

## Comment configurer vos logs Laravel 

La configuration des logs Laravel se trouve dans le fichier **config > logging.php**. Envisagez d'utiliser plusieurs canaux de log en fonction de vos préférences, tels que stack, single, daily, syslogs, slack, papertail, etc. 

Les canaux sont les endroits où vous envoyez les informations de log. Le canal par défaut pour chaque projet est généralement **stack**. Vous pouvez le changer en définissant `LOG_CHANNEL` dans l'environnement ou en spécifiant le nom du canal comme deuxième paramètre dans le même fichier **logging.php**.

```
'default' => env('LOG_CHANNEL', 'stack')
```

Le canal stack a un nom de pilote défini sur `stack`. Les canaux définis sur `single` signifient que vous obtenez tous les logs dans un seul fichier de log. Vous pouvez également utiliser `daily`, ce qui signifie qu'un nouveau log est généré automatiquement chaque jour. C'est un tableau. 

Vous pouvez également utiliser plusieurs canaux, `'channels' => ['daily', 'slack']`, et `ignore_exception` est un booléen (true, false). 

Je recommande vivement d'utiliser le canal daily, car cela vous aide à suivre les logs quotidiens en générant automatiquement un nouveau fichier de log chaque jour (laravel-2023-01-15.log, laravel-2023-01-16.log et ainsi de suite) sans avoir à effacer les logs du jour précédent. 

Les options daily vous tiennent informé chaque jour des informations de log dans vos fichiers de log aussi longtemps que vous le souhaitez. Cela vous permet également de surveiller les erreurs fréquentes dans l'application si elles se produisent à différents jours.

```php
 'channels' => [
	'stack' => [
		'driver' => 'stack',
		'channels' => ['daily'],
		'ignore_exceptions' => false,
	    ],
....],
```

## Pilotes de canaux pour les fichiers de log

Voici la liste des pilotes de canaux offerts par Laravel :

1. `Single` : Le pilote Single garantit que les informations de log sont envoyées à un seul fichier. Le pilote envoie les logs vers **storage > logs > laravel.log** par défaut.
2. `daily` : Le pilote garantit que les logs sont écrits quotidiennement. L'avantage est qu'un nouveau fichier de log est généré automatiquement chaque jour. Comparé au pilote Single, il n'est pas nécessaire d'effacer fréquemment les informations de log du jour précédent. Mais l'inconvénient de ce canal est que vous pourriez avoir plusieurs fichiers de log. Chaque semaine/mois, vous devriez effacer tous les fichiers inutilisés.

Dans le répertoire des logs, vous obtenez souvent des logs comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-26-at-13.29.50.png)
_Fichier de log quotidien_

3. `slack` : Le pilote Slack garantit que tous les logs sont envoyés à Slack. Slack doit être configuré pour obtenir les identifiants de l'utilisateur (nom d'utilisateur, webhook) afin d'aider à la journalisation des erreurs. Cela est très utile car cela permet à votre équipe de rester informée de ce qui se passe directement dans un canal Slack. 

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-26-at-13.19.26.png)

4. `syslog` : Les logs utilisant ce pilote enverront des rapports de log au log système. L'emplacement de ce pilote de log dépend du système d'exploitation du serveur.

5. `errorlog` : Les logs configurés pour utiliser ce pilote enverront des rapports de log au fichier de logs d'erreurs configuré sur le système d'exploitation du serveur web.

6. `monolog` : Ce pilote fournit un support pour tous les gestionnaires Monolog.

7. `custom` : Ce pilote aide à créer un canal personnalisé basé sur les préférences de l'utilisateur. Il pourrait s'agir d'un service tiers nécessitant des rapports de log.

8. `stack` : Le pilote stack est responsable de la création de plusieurs canaux.

9. `null` : Tous les messages de log sont ignorés par le pilote.

## Comment formater les messages de log

Si vous avez besoin d'un rappel sur le fonctionnement des facades ou sur la façon d'en créer une, vous devriez vous référer à cet article sur [comment fonctionnent les facades dans Laravel](https://www.freecodecamp.org/news/how-to-use-facades-in-laravel/). 

Laravel dispose d'une facade `Log` qui aide à écrire des logs. Importez la facade en haut du fichier pour utiliser n'importe quel niveau de log.

```php
<?php

use Illuminate\Support\Facades\Log; 


Log::info($message);
```

Vous pouvez également choisir d'échapper la facade `Log`, afin de ne pas avoir à importer quoi que ce soit. Cela est adapté si vous journalisez une seule instance d'information de log.

```php
<?php

\Log::info($message);
```

Dans une récente version de Laravel, la journalisation a été grandement améliorée. Vous pouvez vous passer de la facade Log lors de la journalisation d'informations et référencer `info` depuis votre application Laravel.

```php
<?php

info($message);
```

D'autres niveaux de journalisation utilisés pour écrire des informations incluent **alert, emergency, critical, warning, error, notice, et debug**.

Dans un fichier, vous pouvez journaliser n'importe quel type de données ou messages et même formater la sortie du texte que vous souhaitez écrire dans le fichier de log. 

### Comment formater des chaînes de caractères, des booléens et des entiers :

```php
<?php

use Illuminate\Support\Facades\Log;


Log::warning('Il y a un avertissement'); 

Log::error(false);

Log::notice(500); 

```

### Comment formater en tableau :

Vous pouvez également formater en tableau. Avec la fonction array, un nouveau tableau est créé. Nous pouvons donc écrire un tableau dans le fichier de log en passant les informations de log à la fonction array. Le `json_decode` convertit l'objet JSON en un objet PHP, et le `true` garantit qu'il retourne des tableaux associatifs (paires clé-valeur).

```php
<?php

$person = '{"Peter":35, "John":37, "Yinka":43}'; 

$data = json_decode($person, true);

info($data);
```

### Comment formater en objet :

Vous pouvez également écrire des objets JSON dans le fichier de log lorsque vous travaillez avec des logs. Utilisez `json_encode` pour encoder les valeurs au format JSON.

```php
<?php 

$data = ["Peter"=> 35, "John"=> 37, "Yinka" => 43];

info(json_encode($data));
```

### Comment concaténer une chaîne avec un tableau ou des objets :

Cela est utile lorsque vous incluez une chaîne pour suivre les informations de log. Vous pouvez le faire en utilisant l'opérateur de concaténation (.)

```php
<?php

$persons = ["Peter"=> 35, "John"=> 37, "Yinka" => 43];

info('Les informations de la personne ' . json_encode($persons));
```

### Comment écrire dans des canaux dédiés :

Cette méthode est utile lorsque vous sentez qu'il est nécessaire d'écrire dans des canaux spécifiques en plus du canal de log par défaut. Vous devez spécifier le nom du canal lors de l'appel de la facade Log.

```php
<?php


\Log::channel('slack')->info('enregistrement réussi');
```

L'extrait ci-dessus garantit que l'opération d'écriture est effectuée sur le canal Slack. De plus, la méthode stack permet la journalisation sur plusieurs canaux.

```php
<?php


\Log::stack(['single', 'slack'])->info('enregistrement réussi !');

```

Vous pouvez en apprendre davantage sur les canaux personnalisés via les factories et la personnalisation des canaux monolog à partir de la [documentation officielle](https://laravel.com/docs/master/logging).

## Conclusion

Dans cet article, vous avez appris la journalisation, la configuration des logs dans votre application Laravel, les pilotes de canaux disponibles et comment écrire des fichiers de log dans différents formats. 

Vous devriez maintenant avoir une meilleure compréhension de la journalisation dans Laravel. Continuez à apprendre, et bon codage !

Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/suleolanrewaju/) et [Twitter](https://twitter.com/bigdevlarry).