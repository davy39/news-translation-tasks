---
title: Sous-domaines Laravel – Comment créer et gérer des sous-domaines dans vos applications
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2021-09-16T17:19:06.000Z'
originalURL: https://freecodecamp.org/news/laravel-subdomians
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/subdomain-structure.png
tags:
- name: Laravel
  slug: laravel
- name: Web Applications
  slug: web-applications
seo_title: Sous-domaines Laravel – Comment créer et gérer des sous-domaines dans vos
  applications
seo_desc: "Modern web applications usually perform more than one function. They often\
  \ have more than one section, offer more than one service, and have a couple of\
  \ clients.\nBut the more functionality the app has, the clumsier your route paths\
  \ will get. \nWhat if..."
---

Les applications web modernes remplissent généralement plus d'une fonction. Elles ont souvent plus d'une section, offrent plus d'un service et ont plusieurs clients.

Mais plus l'application a de fonctionnalités, plus vos chemins de routage deviennent encombrants.

Et s'il existait un moyen de séparer toutes ces parties en composants plus petits avec des routes meilleures et plus propres ? Quelque chose que les utilisateurs pourraient facilement accéder et utiliser indépendamment, sous le même site web ?

Heureusement, il existe un tel moyen : les **Sous-domaines**.

## Qu'est-ce qu'un sous-domaine ?

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-75.png)
_Crédit : [Electroica Blog](https://www.google.com/url?sa=i&url=https%3A%2F%2Fblog.electroica.com%2Fgoogles-top-searches-india-2019%2F&psig=AOvVaw2bx9ZwYjA8ldb4CuGhccN-&ust=1631749915996000&source=images&cd=vfe&ved=0CAwQjhxqFwoTCMiBuKbU__ICFQAAAAAdAAAAABAh)_

Voici une [définition de base d'un sous-domaine](https://www.domain.com/blog/subdomain/) :

> Un sous-domaine est, comme son nom l'indique, une section supplémentaire de votre nom de **domaine principal**. Vous créez des sous-domaines pour aider à organiser et naviguer vers différentes sections de votre site web principal. Dans votre domaine principal, vous pouvez avoir autant de sous-domaines que nécessaire pour accéder à toutes les différentes pages de votre site web.

Donc, disons que vous avez un site web appelé mysite.com. Vous avez une section blog, une section boutique et une section générale pour les pages à propos et contact. Le site web pourrait avoir des sous-domaines comme blog.mysite.com et store.mysite.com, où le site web principal utiliserait le domaine principal.

## Pourquoi devriez-vous utiliser des sous-domaines ?

Les sous-domaines sont assez utiles, et voici quelques-uns de leurs principaux avantages :

* Les utilisateurs peuvent facilement se souvenir des domaines de votre site web, ce qui signifie qu'ils utiliseront probablement plus votre site.
* Vous pourriez diviser votre grande application en groupes plus petits, ce qui facilitera la gestion, le débogage et la mise à jour ou la mise à niveau.
* Les sous-domaines permettent également la personnalisation – par exemple, une application de blog pourrait donner à chaque utilisateur son propre sous-domaine (comme _username.domain.com_).
* Les sous-domaines permettent également aux développeurs de tester des versions de leur application avant de les déployer en production. Vous pourriez avoir un _beta.site.com_ pour prévisualiser les changements avant de les déployer sur le site principal.

Voyons comment tout cela fonctionne en construisant un projet réel et en le testant.

## Comment créer un nouveau projet Laravel

J'ai [Docker](https://www.docker.com/) configuré sur mon ordinateur portable, donc j'utiliserai la configuration [Sail](https://laravel.com/docs/8.x/sail) que [Laravel](https://laravel.com/docs/8.x/) fournit.

```bash
curl -s "https://laravel.build/example-app" | bash
```

> _Vous pouvez utiliser toute autre méthode avec laquelle vous êtes à l'aise. Consultez la [documentation](https://laravel.com/docs/8.x/installation) pour obtenir de l'aide._

### Démarrer le serveur Laravel

```bash
./vendor/bin/sail up -d

```

## Comment configurer les fichiers de routage

Dans votre fichier `web.php`, vous pouvez définir des routes individuelles avec leur domaine (ou sous-domaine) comme ceci :

```php
Route::get('/', function () {
    return 'First sub domain';
})->domain('blog.' . env('APP_URL'));
```

Maintenant, vous pouvez accéder à la page à l'adresse _blog.domain.com_.

Mais plus souvent qu'autrement, vous aurez plus d'un chemin dans une application, comme un domaine et des sous-domaines. Il est donc judicieux d'utiliser un groupe de routes pour couvrir toutes les routes dans le même domaine ou sous-domaine.

```php
Route::domain('blog.' . env('APP_URL'))->group(function () {
    Route::get('posts', function () {
        return 'Second subdomain landing page';
    });
    Route::get('post/{id}', function ($id) {
        return 'Post ' . $id . ' in second subdomain';
    });
});
```

Maintenant, toutes les routes pour le domaine peuvent être gérées en un seul endroit.

## Comment rendre les sous-domaines dynamiques

Comme je l'ai mentionné précédemment, vous pouvez utiliser des sous-domaines pour permettre la personnalisation dans les applications web, ils doivent donc être dynamiques. Par exemple, [Medium](https://medium.com) donne aux auteurs des domaines comme _username.domain.com_.

Vous pouvez faire cela facilement dans Laravel car les sous-domaines peuvent être assignés à des paramètres de route tout comme les URIs de route. Cela vous permet de capturer une portion du sous-domaine pour l'utiliser dans votre fermeture de route ou votre contrôleur.

```php
Route::domain('{username}.' . env('APP_URL'))->group(function () {
    Route::get('post/{id}', function ($username, $id) {
        return 'User ' . $username . ' is trying to read post ' . $id;
    });
});
```

Dans cet exemple, vous pourriez avoir un domaine comme _zubair.domain.com_ avec des paramètres de route également.

## Fournisseurs de services de routage

Pour les applications très grandes, le fichier `web.php` pourrait devenir un peu désordonné si les routes continuent d'augmenter. Il est préférable de diviser les routes en différents fichiers, de préférence par sous-domaine.

Dans votre fichier `RouteServiceProvider.php`, vous verrez ce code dans la méthode `boot` :

```php
public function boot()
    {
        $this->configureRateLimiting();

        $this->routes(function () {
            Route::prefix('api')
                ->middleware('api')
                ->namespace($this->namespace)
                ->group(base_path('routes/api.php'));

            Route::middleware('web')
                ->namespace($this->namespace)
                ->group(base_path('routes/web.php'));
        });
    }
```

Ceci est la configuration de route par défaut de Laravel pour séparer les routes API des routes web. Nous utiliserons ce même fichier pour séparer les sous-domaines.

Ajoutez ce qui suit à la méthode :

```php
Route::domain('blog.' . env('APP_URL'))
                ->middleware('web')
                ->namespace($this->namespace)
                ->group(base_path('routes/blog.php'));
```

Cela indique à Laravel que chaque fois que quelqu'un accède au point de terminaison _blog.domain.com_, il doit rechercher la route dans le fichier blog.php (que nous devons encore créer).

Nous pouvons ensuite créer le fichier `blog.php` dans le dossier `routes` et ajouter le contenu suivant :

```php
<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return 'Route using separate file';
});

```

À ce stade, vous avez terminé tout le code ! Il ne reste plus qu'une configuration serveur.

## Configuration du serveur

Si vous utilisez un service tel que [Laravel Valet](https://laravel.com/docs/8.x/valet), il est beaucoup plus facile à configurer.

Dans le répertoire racine de votre projet, exécutez :

```bash
valet link domain
valet link blog.domain
```

Et si vous n'utilisez pas Laravel Valet, vous pouvez ajouter ceci à votre fichier `/etc/hosts/` :

```
127.0.0.1       domain.test
127.0.0.1       blog.domain.test
```

Cela consiste essentiellement à mapper le domaine vers l'IP.

## **Résumé**

Maintenant, vous savez comment configurer et gérer des sous-domaines dans vos applications Laravel. Vous pouvez trouver tout le code pour cet article [ici](https://github.com/Zubs/subdomain-test).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

Pour lire plus de mes articles ou suivre mon travail, vous pouvez me connecter sur [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris) et [Github](https://github.com/Zubs). C'est rapide, c'est facile et c'est gratuit !