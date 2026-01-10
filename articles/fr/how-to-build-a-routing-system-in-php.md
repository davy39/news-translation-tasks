---
title: Comment créer un système de routage pour une application PHP à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-02T08:36:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-routing-system-in-php
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Pink-8-March-Happy-Woman-s-Day-Facebook-Post-1-.png
tags:
- name: PHP
  slug: php
- name: routing
  slug: routing
seo_title: Comment créer un système de routage pour une application PHP à partir de
  zéro
seo_desc: 'By Abel Lifaefi Mbula

  If you’re just at the beginning of your journey in PHP development, chances are
  that you use complete file names in the URL to navigate your application, like server/contact.php.
  No worries, we all started that way, and it’s how...'
---

Par Abel Lifaefi Mbula

Si vous êtes au début de votre parcours en développement PHP, il est probable que vous utilisez des noms de fichiers complets dans l'URL pour naviguer dans votre application, comme `server/contact.php`. Pas de souci, nous avons tous commencé ainsi, et c'est ainsi que nous apprenons.

Aujourd'hui, je veux vous aider à améliorer la façon dont vous naviguez dans les fichiers de votre application. Nous allons parler de routage, car c'est crucial dans toute application moderne. Cela vous aidera à faire un pas en avant dans votre développement PHP professionnel.

Un système de routage mappe simplement une requête [HTTP](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) à un gestionnaire de requête (fonction ou méthode). En d'autres termes, il définit comment nous naviguons ou accédons à différentes parties d'une application sans avoir besoin de taper le nom du fichier. Vous pouvez faire cela en créant ou en définissant des routes (ou chemins). Par exemple, la route `server/contact` nous permet d'accéder au fichier `contact.php`.

## Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous aurez besoin des éléments suivants :

* Une compréhension de base de PHP.
* Une compréhension de base de HTTP et des réseaux.
* Un serveur Apache ou NGINX, et une compréhension de base de la configuration de ceux-ci.

Et avec cela, plongeons-nous dans le sujet.

## Comment fonctionne le routage

Tout d'abord, laissez-moi vous rappeler ce qu'est le routage. Le routage nous permet de structurer notre application de manière plus efficace et de nous débarrasser des URLs désordonnées. Voici deux fonctionnalités principales offertes par tout bon système de routage :

* Détermine quelle action exécuter pour chaque requête entrante.
* Génère des URLs conviviales pour le référencement (par exemple, `/views/users` au lieu de `views/user.php?all`).

Pour créer un système de routage, nous avons besoin d'un routeur, qui n'est rien de plus que le fichier d'entrée de notre application. Par défaut, ce fichier d'entrée est nommé `index.php`. À l'intérieur du fichier, nous définissons le système de routage grâce aux instructions `[switch](https://www.php.net/manual/en/control-structures.switch.php)` ou `[match](https://www.php.net/manual/en/control-structures.match.php)`.

Enfin, mais non des moindres, nous devons rediriger toutes les requêtes vers le routeur. Cela se fait dans le fichier de configuration du serveur PHP.

## Configuration du projet

Avant de continuer, voyons à quoi ressemblera le projet :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/file-tree-1.png)
_Structure des fichiers_

Utilisez les commandes shell ci-dessous pour initier le projet :

```bash
mkdir php-routing & cd php-routing
touch index.php .htaccess 
```

* `.htaccess` : Un fichier de configuration Apache au niveau du répertoire. Vous n'en avez pas besoin si vous utilisez un serveur NGINX.
* `index.php` : C'est le routeur et le fichier d'entrée du projet. Toutes les requêtes entrantes seront redirigées ici.
* `views` : Ce dossier contient toutes les interfaces utilisateur pour le projet.

## **Comment rediriger toutes les requêtes HTTP vers le routeur**

Nous avons dit précédemment que la redirection se fait dans le fichier de configuration du serveur PHP. Vous devrez donc faire quelques ajustements selon que vous utilisez un serveur Apache ou NGINX.

### Redirection avec Apache

Ici, nous pouvons facilement utiliser le fichier `.htaccess` que nous avons déjà créé à la racine du projet. Ajoutez les directives ci-dessous :

```bash
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.*)\$ index.php
```

* _ligne 1_ : Nous activons le moteur de réécriture en temps réel du serveur Apache.
* _ligne 2_ : Nous limitons l'accès aux fichiers physiques.
* _ligne 3_ : Nous redirigeons toutes les requêtes entrantes vers `index.php`.

Note : Si le site ou l'application n'est pas à la racine du serveur (ou si nous n'avons pas d'hôte virtuel), voici à quoi devrait ressembler le `.htaccess` :

```bash
RewriteEngine On
RewriteBase /folder/
RewriteRule ^index\\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /folder/index.php [L]
```

Dans le code ci-dessus, remplacez `/folder/` par le nom du dossier contenant votre site.

### Redirection avec NGINX

Le fichier de configuration par défaut est nommé `nginx.conf`. Ce fichier peut être trouvé dans `etc/nginx`, `usr/local/nginx/conf`, ou `/usr/local/etc/nginx`.

Pour rediriger vers `index.php`, utilisez la commande ci-dessous :

```nginx
location / {
        try_files $uri $uri/ /index.php
}
```

Le bloc `location /` spécifie que cela correspond à tous les emplacements sauf si un `location /<name>` est explicitement spécifié.

La directive `try_files` indique au serveur que pour toute requête vers l'URI qui correspond au bloc dans l'emplacement, essayez d'abord `$uri` (ou `$uri/`), et si le fichier est présent, servez le fichier. Sinon, l'option de repli (`index.php`) est utilisée. Et ce dernier comportement est ce que nous voulons.

Rechargez le serveur après la modification.

## **Comment créer le système de routage**

Nous savons maintenant comment fonctionne le routage, et nous envoyons même toutes les requêtes au routeur. Il est maintenant temps d'écrire le code pour le routeur dans `index.php`.

Tout d'abord, créez une variable pour contenir la chaîne de requête HTTP :

```php
$request = $_SERVER['REQUEST_URI'];
```

Cette variable nous aidera à comparer avec de nombreuses routes (chemins) et à appeler l'interface de vue appropriée.

```php
switch ($request) {
	 case '/views/users':
    	require __DIR__ . '/views/users.php';
        
     case '/views/department':
    	require __DIR__ . '/views/dep.php';
}
```

Que se passe-t-il ici ? L'instruction `switch` est similaire à une série d'instructions `if` sur la même expression (variable). Elle exécute un code uniquement lorsqu'une instruction `case` est trouvée dont l'expression évalue à une valeur qui correspond à la valeur de l'expression `switch`. Laissez-moi illustrer cela pour que vous puissiez bien le comprendre.

Supposons que notre variable contient la valeur `/views/users/`. Lorsque le morceau de code ci-dessus sera exécuté, PHP vérifiera si la valeur `/views/users` est égale à la valeur de l'instruction `case`, qui dans notre cas est `/views/users`. Cette condition évaluera donc à `true`, et PHP appellera le fichier `/views/users.php`. Si la condition évalue à `false`, PHP vérifiera l'instruction `case` suivante jusqu'à la fin du bloc `switch`.

**Note** : Chaque fois que l'instruction `case` évalue à `true`, PHP continuera à exécuter le code dans les instructions `case` suivantes sans nécessairement évaluer ces instructions `case`. Dans notre cas, PHP requiert également `views/dep.php`. Pour éviter ce "mauvais comportement", vous devez ajouter une instruction `break` après chaque instruction `case`.

Mettons maintenant tout cela ensemble dans notre fichier `index.php` :

```php
<?php

$request = $_SERVER['REQUEST_URI'];
$viewDir = '/views/';

switch ($request) {
    case '':
    case '/':
        require __DIR__ . $viewDir . 'home.php';
        break;

    case '/views/users':
        require __DIR__ . $viewDir . 'users.php';
        break;

    case '/contact':
        require __DIR__ . $viewDir . 'contact.php';
        break;

    default:
        http_response_code(404);
        require __DIR__ . $viewDir . '404.php';
}
```

Comme vous le savez déjà, nous commençons par stocker une requête utilisateur dans la variable `$request`, puis nous l'utilisons dans l'instruction `switch`. Pour un code propre, j'ai créé une variable pour contenir le nom du répertoire des vues.

Vous remarquerez également deux autres choses :

* `''` et `'/'` sont utilisés pour correspondre à `site.com` ainsi qu'à `site.com/` lorsque les utilisateurs sont à la racine de l'application ou du site web.
* Il y a une instruction `case` spéciale, `default`, pour correspondre à tout ce qui n'a pas été correspondre par les autres cas, c'est-à-dire lorsque la route est inconnue.

Ajoutons maintenant quelques données factices dans nos vues.

## **Ajouter des données factices dans les fichiers de vues**

Nous avons déjà créé tous les fichiers dans le répertoire `views`. Passons simplement à ce répertoire et ajoutons du contenu dans chaque fichier.

Mettez simplement du contenu dans chaque fichier :

```php
<h1>Accueil</h1>
<p>Bienvenue dans mon application.</p>
```

```php
<h1>Utilisateurs</h1>
<p>Liste de nos utilisateurs.</p>
```

```php
<h1>Contactez-nous</h1>
<p>Nous contacter est facile. Envoyez-nous simplement un email</p>
```

```php
<h1>404</h1>
<p>Vous avez atteint la fin de l'Internet.</p>
```

Comme vous pouvez le voir, chaque fichier contient simplement un titre et un paragraphe. N'hésitez pas à ajouter le contenu que vous souhaitez et à tester le routeur.

## **Réflexions finales**

Dans ce tutoriel, vous avez appris à créer un système de routage de base à partir de zéro, y compris :

* Comment créer un fichier nommé `index.php` à la racine du projet. C'est le routeur pour votre application.
* Comment rediriger toutes les requêtes entrantes vers le routeur. Vous faites cela dans le fichier de configuration de votre serveur.
* Comment créer le système de routage avec une instruction `switch` dans le routeur.

Bon codage !