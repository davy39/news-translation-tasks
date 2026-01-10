---
title: Comment utiliser Redis dans vos applications PHP
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2023-05-03T19:51:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-redis-with-php
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-tom-fisk-3063470.jpg
tags:
- name: database
  slug: database
- name: PHP
  slug: php
- name: Redis
  slug: redis
seo_title: Comment utiliser Redis dans vos applications PHP
seo_desc: 'Redis is a data store that stores data primarily in memory. It''s faster
  than traditional databases, and has grown quite popular.

  In this tutorial, you''ll learn the basics of how Redis works, when to use it, how
  to install it on your device, and how t...'
---

Redis est un système de stockage de données qui stocke principalement les données en mémoire. Il est plus rapide que les bases de données traditionnelles et est devenu très populaire.

Dans ce tutoriel, vous apprendrez les bases du fonctionnement de Redis, quand l'utiliser, comment l'installer sur votre appareil et comment l'utiliser comme système de cache dans une application web PHP.

## Qu'est-ce que Redis ?

Redis est un système de stockage de données – comme une base de données, mais qui stocke les données principalement en mémoire. Cela le rend beaucoup plus rapide que les bases de données traditionnelles où les données sont stockées sur des disques. Grâce à cette rapidité, Redis est souvent utilisé comme outil de cache.

Redis peut stocker des données dans n'importe quel type de données, car il utilise un système de paires clé-valeur pour stocker les données. Cela diffère également des bases de données traditionnelles qui utilisent des documents ou des lignes.

Vous pouvez penser à une base de données Redis comme un grand objet JSON, où tout dans la base de données est une paire clé-valeur. Cela signifie qu'il ne s'agit peut-être pas du meilleur endroit pour stocker des données structurées.

Vous pouvez également utiliser Redis comme base de données, car il a la capacité d'écrire des données sur disque pour la persistance. Vous pouvez configurer Redis pour persister les données soit périodiquement, soit après chaque commande que vous émettez. Lorsque Redis n'est pas configuré pour persister les données, il est très volatile, et un crash du système entraînerait une perte de données.

Redis est populaire dans les applications de niveau production et est utilisé par de grandes entreprises comme Twitter, Github, SnapChat et StackOverFlow.

## Quand utiliser Redis

* Pour les mots de passe à usage unique (OTP) : ceux-ci sont généralement générés pour être utilisés une fois et ont une durée de vie courte. Avec la capacité de Redis à définir une date d'expiration pour les données, vous pouvez stocker en toute sécurité l'OTP sans vous soucier de les supprimer après une certaine période.
* Pour les ressources fréquemment consultées : pour les données qui ne changent pas trop fréquemment mais qui sont souvent consultées, vous pouvez utiliser Redis pour gagner du temps qui aurait été passé à interroger la base de données ou à faire un appel à un service externe.
* Pour les requêtes intensives : pour les requêtes de base de données qui prennent du temps et qui ne changeront pas trop souvent, utilisez Redis pour réduire ce temps en stockant les résultats aussi longtemps que vous le souhaitez.

## Comment installer Redis

Vous pouvez installer Redis sur n'importe quel système d'exploitation. Voici les instructions pour macOS, Windows Subsystem for Linux et Linux.

### macOS

Pour installer Redis sur macOS, exécutez :

```shell
brew install redis
```

Ensuite, exécutez cette commande pour démarrer Redis :

```shell
redis-server
```

### Windows Subsystem for Linux et Linux

Redis ne prend pas exactement en charge le système d'exploitation Windows pour l'instant, vous pouvez donc installer WSL (Windows Subsystem for Linux) sur Windows pour avoir un environnement Linux.

Pour installer Redis sur Linux, exécutez :

```shell
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

Ensuite, exécutez cette commande pour démarrer Redis :

```shell
sudo service redis-server start
```

Maintenant que Redis est installé, vous pouvez le tester en exécutant `redis-cli ping`. Cela affichera _"PONG"_. Comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-13.36.14.png)
_Test de l'installation de Redis_

## Les bases de Redis

Pour utiliser Redis comme un REPL ou comme une application autonome, exécutez `redis-cli`. Cela ouvrira l'environnement REPL.

### Comment définir des données

Utilisez le mot-clé `SET` pour définir une paire clé-valeur dans Redis. Pour définir une clé `username` avec la valeur `Zubs`, exécutez ceci :

```redis
SET username Zubs
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-13.41.36.png)
_Définition d'une paire clé-valeur_

### Comment obtenir des données

Pour obtenir la clé `username` récemment sauvegardée, utilisez le mot-clé `GET` comme ceci :

```redis
GET username
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-13.43.52.png)
_Obtention d'une valeur par clé_

### Comment supprimer des données

Vous pouvez également supprimer une clé précédemment stockée en utilisant le mot-clé `DEL` comme ceci :

```redis
DEL username
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-17.57.26.png)
_Suppression d'une valeur par clé_

### Comment vérifier si une valeur existe

Vous pouvez vérifier l'existence d'une clé en utilisant le mot-clé `EXISTS`. Il retourne `0` lorsque la clé n'existe pas et `1` si elle existe. Vous pouvez tester en vérifiant si la clé `username` récemment supprimée existe. Comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-18.04.17.png)

### Comment définir un temps de vie pour les clés

Redis vous permet de spécifier combien de temps une clé doit exister lors de sa création. C'est une fonctionnalité vraiment géniale de Redis. Pour cela, utilisez le mot-clé `SETEX` comme ceci :

```redis
SETEX key seconds value
```

Vous pouvez vérifier le temps de vie pour une clé spécifique en utilisant le mot-clé `TTL`. Cela retourne `-1` si la clé n'a pas de date d'expiration définie, ce qui signifie qu'elle sera stockée indéfiniment. Il retourne `-2` si la clé n'existe pas. Et il retourne le temps en secondes si la clé existe.

Vous pouvez définir un temps d'expiration en secondes pour une clé précédemment créée sans temps d'expiration en utilisant le mot-clé `EXPIRE`. Par exemple, créez une clé pour stocker une variable `age` avec une valeur de `26`.

```redis
SET age 26
```

Ensuite, définissez un temps d'expiration de 10 secondes pour celle-ci.

```redis
EXPIRE age 20
```

Vérifiez le temps restant à vivre plusieurs fois pour voir comment il diminue réellement et finit par ne plus exister.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-18.22.58.png)

## Comment construire une application simple avec Redis

Pour vous aider à comprendre comment Redis fonctionne, nous allons maintenant construire une application web de base qui utilise Redis pour mettre en cache des données afin de charger les réponses plus rapidement. Vous allez construire une application simple qui récupère des données d'images depuis [JSONPlaceholder](https://www.freecodecamp.org/news/p/043f81af-1384-435c-b08a-4f80327a6002/'https://jsonplaceholder.typicode.com/photos') et les retourne.

### Créer un nouveau projet PHP en utilisant Composer

Créez un nouveau dossier pour le projet, changez de répertoire dans le dossier nouvellement créé et exécutez la commande suivante pour créer un nouveau projet composer :

```shell
composer init -q
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-19.06.40.png)

Cela créera un nouveau fichier `composer.json` qui devrait ressembler à ceci :

```json
{
    "require": {}
}

```

Ensuite, créez un dossier public pour héberger vos fichiers de code publics. Ensuite, créez un nouveau fichier `index.php` dans le dossier.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-19.26.54.png)

Mettez un contenu de base dans le fichier PHP pour l'instant et démarrez un serveur.

```php
<?php

echo "Hello World!";

```

```shell
php -S localhost:8080
```

### Installer un routeur simple et gérer les requêtes

Pour compléter le projet, installez un routeur PHP simple, `Altorouter`, et un client web, `Guzzlehttp`.

```shell
composer require altorouter/altorouter guzzlehttp/guzzle
```

Mettez à jour le fichier `index.php` pour qu'il contienne ce code :

```php
<?php

// Importer le fichier d'autoload de Composer
require_once __DIR__ . '/../vendor/autoload.php';

// Importer le client GuzzleHttp
use GuzzleHttp\Client;

// Instancier le routeur et le client web
$router = new AltoRouter();
$client = new Client();

// Enregistrer la route d'exemple
$router->map('GET', '/', function () {
	// Définir le type de contenu de la réponse
    header('Content-Type: application/json; charset=utf-8');
    
    // Retourner une réponse de base
    echo json_encode(['data' => 'Hello World']);
});

/**
 * Route pour obtenir toutes les photos
 */
$router->map('GET', '/photos', function () use ($client) {
	// Faire une requête à JSONPlaceholder
    $response = $client->request('GET', 'https://jsonplaceholder.typicode.com/photos');

    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'data' => json_decode($response->getBody()->getContents())
    ]);
});

/**
 * Route pour obtenir une seule photo par id
 */
$router->map('GET', '/photos/[i:id]', function (int $id) use ($client) {
    $response = $client->request('GET', 'https://jsonplaceholder.typicode.com/photos/' . $id);

    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'data' => json_decode($response->getBody()->getContents())
    ]);
});

$match = $router->match();

if( is_array($match) && is_callable( $match['target'] ) ) {
    call_user_func_array( $match['target'], $match['params'] );
} else {
    // aucune route n'a été trouvée
    header( $_SERVER["SERVER_PROTOCOL"] . ' 404 Not Found');
}

```

Le code est assez explicite. Mais voici une explication pour plus de clarté. Des lignes 1 à 11, les classes requises GuzzleHttp et AltoRouter sont importées et instanciées.

Des lignes 14 à 20, la première route est enregistrée, avec une fermeture simple qui retourne "Hello World!". Les lignes 25 à 45 enregistrent deux autres routes, une pour récupérer toutes les photos, `/photos`, et une autre pour récupérer une seule photo, `/photos/id`.

Les dernières lignes sont requises selon la documentation du package du routeur pour exécuter les fermetures définies dans la déclaration des routes.

Vous pouvez tester ces routes en utilisant Postman.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-20.19.36.png)
_Route Hello World_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-20.21.01.png)
_Route Obtenir toutes les photos_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-20.26.19.png)
_Route Obtenir une seule photo_

La route `/photos` prend en moyenne 1400 ms par requête. La route `/photos/id` prend en moyenne 900 ms par requête.

### Installer et instancier Redis

Ces temps peuvent être réduits en mettant en cache les résultats de la requête originale à JSONPlaceholder, puis en retournant une réponse depuis le cache au lieu de faire une requête à chaque fois.

Pour utiliser Redis avec PHP, installez l'extension [PhpRedis](https://github.com/phpredis/phpredis). Cette extension fournit une API pour communiquer avec Redis. Vous pouvez facilement l'installer en utilisant la commande :

```shell
pecl install redis
```

Après l'installation, vous pouvez utiliser cette classe dans votre projet PHP. Importez la classe et instanciez-la en haut de votre fichier `index.php` :

```php
$redis = new Redis();
$redis->connect('127.0.0.1');
```

Ayant fait cela, vous pouvez maintenant utiliser Redis dans votre projet.

### Comment mettre en cache des données avec Redis

Stockez la réponse JSON brute retournée par JSONPlaceholder dans Redis avec un temps d'expiration d'1 heure (3600 secondes).

```php
$response = $client->request('GET', 'https://jsonplaceholder.typicode.com/photos');

$redis->setex(
	'photos',
	3600,
	$response->getBody()->getContents()
);
```

Ici, vous créez une nouvelle clé appelée `photos`, lui donnez un temps d'expiration d'1 heure, puis lui attribuez la réponse brute obtenue de JSONPlaceholder.

Mais à ce stade, l'API met toujours beaucoup de temps à répondre. Cela est dû au fait que vous ne stockez que cette réponse, vous n'utilisez pas Redis pour retourner la réponse.

Pour corriger cela, lorsqu'une nouvelle requête arrive, vérifiez si vous avez des données précédemment stockées en mémoire. Si oui, vous retournez les données en mémoire, sinon, vous faites un appel à JSONPlaceholder.

Mettez à jour le bloc `/photos` comme suit :

```php
/**
 * Route pour obtenir toutes les photos
 */
$router->map('GET', '/photos', function () use ($client, $redis) {
    // Vérifier si Redis a la clé
    if (!$redis->exists('photos')) {
        $response = $client->request('GET', 'https://jsonplaceholder.typicode.com/photos');

        // Stocker les données pour une utilisation ultérieure
        $redis->setex(
            'photos',
            REDIS_STANDARD_EXPIRY,
            $response->getBody()->getContents()
        );
    }

    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'data' => json_decode($redis->get('photos'))
    ]);
});
```

En testant dans Postman pour voir les améliorations, vous voyez que le temps de réponse moyen après le premier appel (l'appel original avant qu'il ne soit mis en cache) est passé à une moyenne de 20 ms pour la route `/photos`. C'est une amélioration de plus de 50x. Redis économise beaucoup de temps et de puissance de traitement.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-21.11.34.png)

Mettez à jour la route `/photos/id` pour utiliser Redis également :

```php
$router->map('GET', '/photos/[i:id]', function (int $id) use ($client, $redis) {
    if (!$redis->exists('photos:' . $id)) {
        $response = $client->request('GET', 'https://jsonplaceholder.typicode.com/photos/' . $id);

        $redis->setex(
            'photos:' . $id,
            REDIS_STANDARD_EXPIRY,
            $response->getBody()->getContents()
        );
    }

    header('Content-Type: application/json; charset=utf-8');
    echo json_encode([
        'data' => json_decode($redis->get('photos:' . $id))
    ]);
});
```

La route `/photos/id` est désormais également beaucoup plus rapide, car elle prend moins de 5 ms pour obtenir une réponse, ce qui représente une amélioration de plus de 45x.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-30-at-21.12.31.png)

## Résumé

J'espère que vous comprenez maintenant ce qu'est Redis, ses bases et comment vous pouvez l'utiliser pour améliorer la vitesse de vos applications web PHP. Vous pouvez trouver les fichiers de code utilisés dans cet article sur [GitHub](https://github.com/Zubs/php-redis).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me rejoindre sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris) et [Github](https://github.com/Zubs). C'est rapide, c'est facile et c'est gratuit !