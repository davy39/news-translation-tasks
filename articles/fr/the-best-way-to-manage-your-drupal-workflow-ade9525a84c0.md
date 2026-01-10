---
title: La meilleure façon de gérer votre flux de travail Drupal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-27T23:54:06.000Z'
originalURL: https://freecodecamp.org/news/the-best-way-to-manage-your-drupal-workflow-ade9525a84c0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yhQ2g4zBCCDEo-mGalYocg.jpeg
tags:
- name: Drupal
  slug: drupal
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La meilleure façon de gérer votre flux de travail Drupal
seo_desc: 'By Ankit Jain

  One of the struggles that developers face when moving to Drupal 8 is the lack of
  best practices in deploying Drupal sites. The Challenges in deployment revolve around
  Dependency Management, Drupal Contrib Modules/Themes, Configuration M...'
---

Par Ankit Jain

L'un des défis auxquels les développeurs sont confrontés lors du passage à Drupal 8 est le manque de bonnes pratiques pour le déploiement des sites Drupal. Les défis de déploiement tournent autour de la gestion des dépendances, des modules/thèmes contrib Drupal, de la gestion de la configuration et, bien sûr, de la base de code.

Drupal 7 n'a pas de tels problèmes. Mais ahhh, Drupal 8 arrive avec beaucoup de choses à gérer. L'un des plus grands changements dans Drupal 8 est l'adoption de Composer. Les bonnes choses ont un prix.

Nous utiliserons une base de code pour un site Drupal et utiliserons Git pour le contrôle de version et le déploiement.

### Composer

[Composer](https://getcomposer.org/) est un gestionnaire de dépendances pour PHP (comme npm pour Node ou pip pour Python). Le cœur de Drupal utilise Composer pour gérer les dépendances principales comme les composants Symfony et Guzzle. Composer nous permet de gérer systématiquement une liste de dépendances et leurs dépendances subsidiaires. Composer installe ces dépendances via un fichier manifeste appelé composer.json.

![Image](https://cdn-media-1.freecodecamp.org/images/pUUUDONIPBc5YhXinYyVuLMZ6Gw8pfcjLaga)

Ce fichier composer.json contient les dépendances dont le projet a besoin. Vous pouvez l'installer en exécutant

```
composer install
```

pour la première fois. Il localise, télécharge, valide et charge les packages. Il garantit également que les versions exactes de chaque package sont utilisées et maintient le fichier de journal appelé composer.lock.

**Note : toujours commiter votre fichier composer.lock,** car il contient la version exacte des dépendances que vous avez définies dans le projet.

Si vous souhaitez mettre à jour un package spécifique, il est bon de pratiquer d'exécuter cette commande :

```
composer update package/package-name
```

Vous ne devriez jamais exécuter **composer update,** car composer essaiera de mettre à jour chaque dépendance. Cela peut causer des problèmes à votre site.

### Drupal Composer

[drupal-composer/drupal-project](https://github.com/drupal-composer/drupal-project) est le projet salvateur pour gérer les dépendances de votre site avec Composer.

Pour installer ce modèle de projet, exécutez cette commande :

```
composer create-project drupal-composer/drupal-project:8.x-dev drupal8 --stability dev --no-interaction
```

Il installera automatiquement un site Drupal avec toutes les dépendances. Il installera également [Drupal console](https://drupalconsole.com/) et [Drush](https://github.com/drush-ops/drush) localement.

Composer est l'un des moyens les plus rapides d'installer des dépendances, car il met en cache les dépendances et charge les données à partir du cache la prochaine fois.

#### **Structure du répertoire**

![Image](https://cdn-media-1.freecodecamp.org/images/s7H0wBMBgz4kfLm1hjGlxdNLJV5KwlBsb9EN)

Elle est différente de la structure du répertoire Drupal. Vous pouvez réassembler le répertoire web avec le répertoire public qui contient les fichiers Drupal. Toutes les dépendances tierces sont à l'extérieur du dossier web.

Vous pouvez installer n'importe quel module, thème et profil Drupal via composer, qui sera téléchargé dans le dossier contrib à l'intérieur des modules, thèmes et profils, respectivement. De cette manière, le fichier composer.lock aura un enregistrement de tous les modules contrib Drupal ainsi que les dépendances tierces.

Pour télécharger des modules et des thèmes en utilisant composer, exécutez ce qui suit :

```
composer require drupal/mediumish_blog
```

```
# Pour installer le thème, nous utiliserons drupal console
```

```
drupal theme:install mediumish_blog
```

#### **Gitignore**

Comme toutes les dépendances et les modules/thèmes contrib Drupal sont gérés par composer, nous ne pousserons pas ce contenu vers Git.

```
# Ignorer les répertoires générés par Composer /drush/contrib /vendor/ /web/core/ /web/modules/contrib/ /web/themes/contrib/ /web/profiles/contrib/ /web/libraries/
```

```
# Ignorer les informations sensibles /web/sites/*/settings.php /web/sites/*/settings.local.ph
```

### Gestion de la configuration

Le déploiement et la gestion de la configuration sont des actions courantes du cycle de vie d'un projet. Nous avons installé divers modules et configuré notre site local, mais notre site de production n'a pas une telle configuration.

Dans Drupal 7, nous avions le module features, qui est utilisé pour synchroniser la configuration. Mais Drupal 8 a une solution intégrée pour gérer les configurations. Cela vous permet d'exporter des configurations complètes de site web et de les stocker dans des fichiers YAML. Les fichiers exportés peuvent être importés vers un autre site web avec le même résultat.

Le système de configuration de Drupal aide à résoudre le problème de synchronisation des fichiers de configuration de deux manières : une manière unifiée de stocker la configuration et un processus pour importer/exporter les changements entre les instances du même site.

#### **Comment synchroniser les fichiers de configuration**

Ouvrez /web/sites/default/settings.php et définissez $config_directories['sync']

```
$config_directories['sync'] = '../config/sync';
```

C'est une bonne pratique de stocker les fichiers de configuration à l'extérieur du répertoire web pour éviter de les rendre accessibles depuis Internet.

Utilisez maintenant la console Drupal pour exporter la configuration :

```
drupal config:export
```

```
# importer sur le serveur de production
```

```
drupal config:import
```

**Note :** les sites Drupal de production et locaux doivent avoir les mêmes UUID. Voir [ici](https://www.drupal.org/docs/8/configuration-management/managing-your-sites-configuration) pour plus d'informations.

**Note :** La gestion de la configuration Drupal a un bug — les données des blocs personnalisés ne doivent ni être importées ni exportées. Voir le lien de l'issue [ici](https://www.drupal.org/project/drupal/issues/2756331).

### Git

Nous utiliserons Git pour ajouter, commiter et pousser les données du site local avec toute la configuration. Cela sera tiré du serveur/site de production. Voyons le flux :

```
# Local
```

```
git add .
```

```
git commit -m"Add commit message"
```

```
git push origin HEAD
```

```
# Serveur
```

```
git pull origin HEAD
```

```
composer install # pour installer de nouvelles dépendances, modules contrib drupal, thèmes
```

```
drupal config:import # pour importer la configuration
```

```
drupal cache:rebuild all # reconstruire le cache
```

#### **Mettre à jour les modules, thèmes et profils**

```
composer update drupal/mediumish_blog
```

```
drupal update:execute mediumish_blog
```

```
drupal update:execute all
```

#### **Mettre à jour le cœur de Drupal**

Généralement, nous rencontrons des problèmes lors de la mise à jour du cœur de Drupal. Mais composer a une manière simple de gérer cela également :

```
composer update drupal/core --with-dependencies
```

Il mettra à jour le cœur de Drupal et toutes ses dépendances associées.

### Gestion de la configuration de l'environnement

Mon aspect préféré de Drupal, en tant que développeur, est la capacité de gérer différentes configurations d'environnement. Cela peut être fait en utilisant le module [vlucas/phpdotenv](https://github.com/vlucas/phpdotenv), qui est également inclus avec le modèle de composer Drupal.

Tout ce qui est susceptible de changer entre les environnements de déploiement — comme les identifiants de base de données ou les identifiants pour les services tiers — doit être extrait du code dans des variables d'environnement. Basiquement, un fichier `.env` est un moyen facile de charger des variables de configuration personnalisées dont votre application a besoin sans avoir à modifier d'autres fichiers.

Renommez .env.example en .env et ajoutez tous les identifiants sous forme de paire clé-valeur dans le fichier .env.

Le fichier load.environment.php à la racine chargera ce fichier .env et le rendra disponible pour vous.

#### **Comment utiliser le fichier .env**

Ouvrez /web/sites/default/setting.php et ajoutez ce ensemble de code :

```
$databases['default']['default'] = [ 'database' => getenv('MYSQL_DATABASE'), 'driver' => 'mysql', 'host' => getenv('MYSQL_HOSTNAME'), 'namespace' => 'Drupal\\Core\\Database\\Driver\\mysql', 'password' => getenv('MYSQL_PASSWORD'), 'port' => getenv('MYSQL_PORT'), 'prefix' => '', 'username' => getenv('MYSQL_USER'), ];
```

Ouvrez le fichier .env et définissez les identifiants suivants :

```
MYSQL_DATABASE='db_name' MYSQL_HOSTNAME='localhost' MYSQL_PASSWORD='secret' MYSQL_PORT='3306' MYSQL_USER='root'
```

Maintenant, comme tous nos identifiants sont stockés dans le fichier .env, nous pouvons pousser notre settings.php vers le serveur et gérer sa configuration via le fichier .env.

Nous activons généralement le débogage twig pendant le développement et le désactivons en production. Cela peut également être fait facilement et en douceur via un fichier .env.

Ajoutez une nouvelle paire clé-valeur dans le fichier .env :

```
APP_ENV='local'
```

Maintenant, copiez web/sites/example.settings.local.php vers web/sites/default/settings.local.php et ajoutez ce code dans web/sites/development.services.yml sous paramètres :

```
twig.config: debug: true auto_reload: true cache: false
```

Maintenant, ouvrez web/sites/default/settings.php et ajoutez ce code :

```
$env = getenv('APP_ENV');
```

```
$base_path = $app_root . '/' . $site_path; $settingsFile = $base_path . '/settings.' . $env . '.php';
```

```
if (file_exists($settingsFile)) { include $settingsFile; }
```

Ainsi, de cette manière, si vous définissez votre APP_ENV='local', le débogage Twig sera activé. En production, vous pouvez le désactiver en définissant APP_ENV='prod'. Vous pouvez également configurer différentes configurations pour différents environnements.

### Conclusion

Drupal 8 offre une solution intégrée pour exporter et importer des configurations de site, ce qui est bien mieux que ce que vous pouviez faire dans D7. Les dépendances et les modules/thèmes contrib sont gérés par le composer lui-même.

Ce n'est pas encore parfait, car il n'y a pas d'approche standard, mais le flux de travail décrit ci-dessus est une solution simple et efficace. Vous pouvez définir votre propre flux de travail en fonction de vos besoins.

Pour référence, j'ai poussé le code vers [ce dépôt](https://github.com/ankitjain28may/drupal-best-practices).

J'espère que vous avez trouvé cet article utile. J'adorerais avoir votre retour :)

Cet article provient de mon propre blog. Pour lire plus d'articles comme celui-ci, suivez-le [ici](http://ankitjain28.me/).