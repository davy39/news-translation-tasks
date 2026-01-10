---
title: Comment construire un serveur GraphQL avec Laravel GraphQL et le tester avec
  Postman
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2021-07-13T07:54:34.000Z'
originalURL: https://freecodecamp.org/news/build-graphql-server-with-laravel
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/ben-4wxWBy8Jo1I-unsplash.jpg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Comment construire un serveur GraphQL avec Laravel GraphQL et le tester
  avec Postman
seo_desc: "GraphQL is a query language for your API. It simplifies the process of\
  \ requesting the server by providing convenient ways to query objects. \nFor instance,\
  \ if you're using a REST API and you need a list of books, you might hit the GET\
  \ /books/list endp..."
---

[GraphQL](https://graphql.org/) est un langage de requête pour votre API. Il simplifie le processus de demande au serveur en fournissant des moyens pratiques pour interroger des objets. 

Par exemple, si vous utilisez une API REST et que vous avez besoin d'une liste de livres, vous pourriez frapper le point de terminaison `GET /books/list` pour tous les livres. Ensuite, si vous avez besoin d'un livre spécifique par ID, vous frapperiez `GET /book?id={id}`, ce qui signifie que vous ferez plusieurs requêtes au serveur.

Mais GraphQL fait quelque chose appelé récupération de données déclarative, où vous pouvez demander ce que vous voulez et obtenir un résultat prévisible en une seule requête. 

Génial, non ? Voyons comment tout cela fonctionne.

### Ce que nous allons apprendre ?

Dans cet article, vous apprendrez les bases de GraphQL en utilisant le [package Laravel GraphQL](https://github.com/rebing/graphql-laravel) pour construire un serveur qui fait ce qui suit :

1. Inscrire des utilisateurs 
2. Récupérer tous les utilisateurs
3. Obtenir un utilisateur par ID
4. Récupérer tous les posts
5. Récupérer tous les posts avec les relations utilisateurs
6. Enfin, en bonus, vous apprendrez également à utiliser l'outil super génial Postman pour exécuter votre requête et obtenir une réponse en temps réel

## Prérequis

Voici quelques éléments dont vous aurez besoin pour ce tutoriel :

1. Un serveur local ([XAMPP](https://www.apachefriends.org/download.html) ou [WAMP](https://www.wampserver.com/en/download-wampserver-64bits/))
2. Un éditeur de code ([Sublime Text](https://www.sublimetext.com/3), [VS](https://atom.io/) [Code](https://code.visualstudio.com/download), ou [Atom](https://atom.io/))
3. Un système de contrôle de version ([Git](https://git-scm.com/downloads))
4. Un gestionnaire de dépendances ([Composer](https://getcomposer.org/download/))
5. Le [package Laravel GraphQL](https://github.com/rebing/graphql-laravel)

## Bases de GraphQL

Avant de commencer, passons en revue quelques fondamentaux de GraphQL.

### Qu'est-ce qu'un schéma GraphQL ?

Un schéma GraphQL décrit les requêtes, les mutations et les types qui y sont associés :

```php
type User {
    id: ID !
    name : String !
    email : String !
    age : Int
    hobbies: [String]
    created_at : DateTime 
    updated_at : DateTime
}
```

Dans l'extrait de code ci-dessus, le point d'exclamation sur les noms de colonnes tels que `id`, `name` et `email` signifie qu'ils sont des champs obligatoires.

Vous pouvez également définir divers types de données tels que `Int`, `String`, et ainsi de suite. Vous pouvez également inclure des types de liste et définir le type de données qu'il doit contenir comme avec `hobbies`. 

### Qu'est-ce que les requêtes GraphQL ?

GraphQL facilite l'interaction avec les données d'un objet. Vous utilisez des méthodes pour demander des champs spécifiques sur des objets et obtenez ensuite les résultats attendus :

```php
{
  user {
    name
  }
}
```

```php
{
  "data": {
    "user": {
      "name": "John doe"
    }
  }
}
```

### Qu'est-ce que les résolveurs GraphQL ? 

Chaque fois que vous demandez des données à un serveur GraphQL, elles sont `résolues`.

Les résolveurs contiennent des arguments tels qu'un `objet`, `args`, `contexte` et `info`. Vous verrez comment fonctionnent les résolveurs en construisant ce projet.

## Comment commencer avec GraphQL

### Installation

Configurez un environnement Laravel en exécutant cette commande dans le terminal :

```php
composer create-project laravel/laravel graphql-laravel
```

Si vous n'avez pas installé Composer, vous pouvez l'obtenir [ici](https://getcomposer.org/).

Installez le package open-source [graphql-laravel server](https://github.com/rebing/graphql-laravel) :

```php
composer require rebing/graphql-laravel
```

Une fois l'installation terminée, publiez `config/graphql.php` :

```php
php artisan vendor:publish --provider="Rebing\GraphQL\GraphQLServiceProvider"
```

Et démarrez le serveur de développement avec `php artisan serve` :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-08-at-16.14.36.png)
_La page d'accueil de Laravel_

### Comment créer la migration, les contrôleurs et la ressource

#### Post

Dans cette section, vous allez créer une relation entre les utilisateurs et les posts.

Pour ce faire, vous devrez créer des modèles où vous définissez la relation entre les entités, créer des migrations et définir des schémas de base de données.

```php
php artisan make:model Post -mcr
```

Dans `app/Models/User`, créez une relation `hasMany` entre les utilisateurs et les posts :

```php
public function posts()
{
	return $this->hasMany(Post::class);
}
```

Et dans `app/models/Post`, définissez une relation pour mapper les utilisateurs aux posts :

```php
public function user()
{
	return $this->belongsTo(User::class);
}
```

### Comment créer la migration 

Dans cette section, vous allez créer la migration.

Laravel est déjà livré avec une migration utilisateur par défaut. Tout ce que vous avez à faire maintenant est d'ajouter une migration pour les posts :

```php
php artisan make:migration create_post_table
```

Cela crée un fichier de migration avec la direction `database/migrations`. Dans le fichier de migration, définissez le schéma :

```php
Schema::create('posts', function (Blueprint $table) {
            $table->id();
             $table->integer('user_id')->unsigned();
            $table->string('title');
            $table->text('comment');
            $table->timestamps();
        });
```

Ensuite, modifiez le fichier `.env` existant pour nommer la base de données et établir une connexion :

```php
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=graphql-laravel
DB_USERNAME=root
DB_PASSWORD=

```

Exécutez la commande de migration pour créer les tables `User` et `Post` :

```php
 php artisan migrate
```

Vous pouvez générer des enregistrements aléatoires pour les tables `User` et `Post` en utilisant les factories de Laravel.

Puisque Laravel est livré avec une factory `User` par défaut, vous pouvez l'utiliser et vous concentrer sur la création d'une factory `Post`.

### Comment créer une factory Post

```php
php artisan make:factory PostFactory
```

Une fois que `PostFactory` est créé dans le répertoire `database > factories`, vous devrez définir les noms de colonnes et les fakers dont vous avez besoin dans la méthode `definition` :

```php
use Illuminate\Support\Str;


public function definition()
    {
        return [
            'user_id' => rand(1,5),
            'title' => $this->faker->name(),
            'comment' => $this->faker->realText(180)
        ];
    }
```

### Comment créer le seeder de la base de données

Dans la classe seeder, créez une instance d'exécution pour les factories `User` et `Post`.

Cela créera cinq utilisateurs et cinq posts avec les `user_id` correspondants :

```php
public function run()
    {
        \App\Models\User::factory(5)->create();

        \App\Models\Post::factory(5)->create();
    }
```

Ensuite, exécutez la commande seeder artisan :

```php
php artisan db:seed
```

Une fois que vous avez exécuté cette commande dans le terminal, vérifiez les tables de la base de données (`User` et `Post`) :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-26-at-02.40.17.png)
_Table Post_

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-18.32.11.png)
_Table User_

### Comment créer une requête utilisateur

Au moment de la rédaction de cet article, le package Laravel GraphQL ne prend pas en charge la création d'un échafaudage pour les requêtes via le terminal.

Ajoutez donc ce qui suit à `app > GraphQL > Type > UserType.php` :

```php
<?php

namespace App\GraphQL\Type;

use App\Models\User;
use GraphQL\Type\Definition\Type;
use Rebing\GraphQL\Support\Type as GraphQLType;

class UserType extends GraphQLType
{
    protected $attributes = [
        'name'          => 'User',
        'description'   => 'A user',
        'model'         => User::class,
    ];

    public function fields(): array
    {
        return [
            'id' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'The id of the user',
            ],
            'name' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'The name of user',
            ],
            'email' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'The email of user'
            ],
        ];
    }
}

```

Dans l'extrait de code ci-dessus, vous ajoutez l'espace de noms dont vous avez besoin au modèle `User`. Vous incluez également un tableau `protected $attributes` qui décrit le modèle.

Vous avez également ajouté une fonction publique `field` qui retourne un tableau.

Dans cette fonction, vous définissez le schéma pour inclure les colonnes que vous avez spécifiées dans la table utilisateur `(id, name, email)`.

`Type::nonNull(Type::string())` est le point d'exclamation indiquant les champs obligatoires et le type de données string.

### Comment ajouter un type à la configuration

Ajoutez le `UserType` au fichier de configuration que vous avez créé précédemment : `app > config > graphql.php` :

```php
'types' => [
        App\GraphQL\Type\UserType::class
    ],
```

### Comment définir la requête utilisateur

Ensuite, vous devrez définir une requête qui retourne le `UserType` ou une liste. Vous devez également spécifier les arguments que vous utiliserez dans la méthode resolve :

```php
<?php

namespace App\GraphQL\Type;

use GraphQL;
use App\Models\User;
use GraphQL\Type\Definition\Type;
use Rebing\GraphQL\Support\Type as GraphQLType;

class UserType extends GraphQLType
{
    protected $attributes = [
        'name'          => 'User',
        'description'   => 'A user',
        'model'         => User::class,
    ];
    
    public function type(): Type
    {
        return Type::nonNull(Type::listOf(Type::nonNull(GraphQL::type('User'))));
    }

    public function args(): array
    {
        return [
            'id' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'The id of the user',
            ],
            'name' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'The name of user',
            ],
            'email' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'The email of user',
            ]
        ];
    }
    
    public function resolve($root, $args)
    {        
        if (isset($args['id'])) {
            return User::whereId($args['id'])->get();
        }
        
        if (isset($args['name'])) {
            return User::whereName($args['name'])->get();
        }

        if (isset($args['email'])) {
            return User::whereEmail($args['email'])->get();
        }

        return User::all();
    }
}

```

Dans l'extrait ci-dessus, vous utilisez l'espace de noms requis fourni par le package ainsi que `App\Models\User`.

Vous étendez également le `GraphQLType` du package Laravel et définissez les `attributes` comme un tableau protégé.

La méthode `args` retourne un ID, un nom et un email du modèle `User`.

La méthode resolve est utilisée pour récupérer les données de la base de données. Si des `args` sont présents, alors le bloc `if` est exécuté et vous aide à filtrer en fonction des requêtes utilisateur.

Sinon, toutes les données du modèle `User` sont récupérées.

### Comment ajouter une requête à la configuration

Ajoutez la requête suivante au fichier de configuration `app > config > graphql.php` :

```php
'schemas' => [
        'default' => [
            'query' => [
                App\GraphQL\Query\UsersQuery::class,
            ],
            'mutation' => [
                // ExampleMutation::class,
            ],
            'types' => [
                // ExampleType::class,
            ],
            'middleware' => [],
            'method' => ['get', 'post'],
        ],
    ],
```

Vous devriez maintenant pouvoir interroger les données à partir de ce point de terminaison : [http://localhost:8000/graphql](http://localhost:8000/graphql).

Et au cas où vous seriez curieux, `/graphql` est le préfixe de la route.

### Comment interroger pour récupérer tous les utilisateurs

Pour cette requête :

```php
query {
    users {
        id, name , email
    }
} 
```

Voici la sortie attendue avec Postman :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-26-at-01.13.22.png)
_Récupérer tous les utilisateurs_

### Comment créer une relation Post avec l'utilisateur

Maintenant, vous devez définir un `PostType`.

Cette approche suit ce que vous avez défini précédemment pour `UserType`.

Accédez à `app > Type > PostType.php` et ajoutez ce qui suit :

```php
<?php

namespace App\GraphQL\Type;

use GraphQL;
use App\Models\Post;
use GraphQL\Type\Definition\Type;
use Rebing\GraphQL\Support\Type as GraphQLType;

class PostType extends GraphQLType
{
    protected $attributes = [
        'name'          => 'Post',
        'description'   => 'A post',
        'model'         => Post::class,
    ];

    public function args(): array
    {
        return [
            'id' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'The id of the post',
            ],
            'title' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'The title of post',
            ],
        ];
    }
}

```

`Post` suit la spécification définie pour `User`. Ici, vous avez également utilisé l'espace de noms de la requête et le modèle `Post`.

Avec le code ci-dessus, vous étendez la requête sur la classe `PostQuery` et définissez le tableau `$attributes` pour qu'il soit protégé. Et vous avez une fonction `fields` qui retourne un tableau avec l'ID, le titre et le commentaire.

Enfin, vous avez un `type` dans la fonction `args` qui montre leurs différents types de données `int` ou `string` avec une description qui vous indique ce qu'ils font d'un coup d'œil.

### Comment créer une PostsQuery

Ajoutez ce qui suit à `app > GraphQL > Query > PostsQuery.php` :

```php
<?php 

namespace App\GraphQL\Query;

use Closure;
use App\Models\Post;
use Rebing\GraphQL\Support\Facades\GraphQL;
use GraphQL\Type\Definition\ResolveInfo;
use GraphQL\Type\Definition\Type;
use Rebing\GraphQL\Support\Query;

class PostsQuery extends Query
{
    protected $attributes = [
        'name' => 'posts',
    ];

    public function type(): Type
    {
        return Type::nonNull(Type::listOf(Type::nonNull(GraphQL::type('Post'))));
    }

    public function args(): array
    {
        return [
            'id' => [
                'name' => 'id', 
                'type' => Type::int(),
            ],
            'title' => [
                'name' => 'title', 
                'type' => Type::string(),
            ]
        ];
    }

    public function resolve($root, $args)
    {        
        if (isset($args['id'])) {
            return Post::whereId($args['id'])->get();
        }
        
        if (isset($args['title'])) {
            return Post::whereTitle($args['title'])->get();
        }

        return Post::all();
    }
}

```

Dans le code ci-dessus, vous utilisez la méthode resolve pour récupérer les données de la base de données comme je l'ai mentionné précédemment.

Si des `args` sont présents, alors le bloc `if` est exécuté et vous aide à filtrer en fonction de la requête utilisateur. Sinon, toutes les données du modèle `Post` sont retournées.

### Comment ajouter PostsQuery et PostType à la configuration

```php
'schemas' => [
        'default' => [
            'query' => [
                App\GraphQL\Query\UsersQuery::class,
                App\GraphQL\Query\PostsQuery::class
            ],
            'mutation' => [
                // ExampleMutation::class,
            ],
            'types' => [
                // ExampleType::class,
            ],
            'middleware' => [],
            'method' => ['get', 'post'],
        ],
    ],
```

```php
'types' => [
        App\GraphQL\Type\UserType::class,
        App\GraphQL\Type\PostType::class
    ],
```

Vous pouvez maintenant utiliser la requête suivante pour obtenir tous les posts :

```php
query{
    posts{
        id
        user_id
        title
        comment
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-26-at-03.00.41.png)
_Image de récupération de tous les posts_

Vous pouvez également récupérer les utilisateurs avec les relations de posts avec cette requête :

```php
query{
    users{
        id 
        name
        posts {
            title
        }
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screenshot-2021-07-11-at-15.40.05.png)
_Image pour récupérer les utilisateurs avec la relation de post_

### Comment créer une mutation 

Maintenant, vous allez configurer une mutation pour créer un utilisateur. Cette mutation aidera aux opérations qui impliquent de modifier l'état sur le serveur.

Dans votre cas, vous allez muter l'état du serveur en créant un utilisateur.

Créez un dossier de mutation dans le répertoire app, `app > Mutation > CreateUserMutation.php`.

Ensuite, ajoutez le code suivant à `CreateUserMutation.php` :

```php
<?php

namespace App\GraphQL\Mutation;

use Closure;
use App\Models\User;
use GraphQL;
use GraphQL\Type\Definition\Type;
use GraphQL\Type\Definition\ResolveInfo;
use Rebing\GraphQL\Support\Mutation;

class CreateUserMutation extends Mutation
{
    protected $attributes = [
        'name' => 'users'
    ];

    public function type(): Type
    {
        return Type::nonNull(GraphQL::type('User'));
    }

    public function args(): array
    {
        return [
            'name' => ['
                name' => 'name', 
                'type' => Type::nonNull(Type::string()),
            ],
            'email' => ['
                name' => 'email', 
                'type' => Type::nonNull(Type::string()),
            ],
            'password' => [
                'name' => 'password', 
                'type' => Type::nonNull(Type::string()),
            ]
        ];
    }

    public function resolve($root, $args, $context, ResolveInfo $resolveInfo, Closure $getSelectFields)
    {
        return User::firstOrCreate(
            [   'email' => $args['email']],
            [   'name' => $args['name'],
                'password' => bcrypt($args['password'])
            ]);
    }
}

```

La méthode `resolve` aide les utilisateurs de l'application à s'inscrire et à créer leur enregistrement. `resolve` accepte `args` comme paramètre puis utilise la méthode `firstOrCreate` pour s'assurer que tous les utilisateurs qui s'inscrivent ont un identifiant unique, dans ce cas, leur adresse email.

Dans la configuration, vous devrez également inclure la mutation que vous venez de créer :

```php
'schemas' => [
        'default' => [
            'query' => [
                App\GraphQL\Query\UsersQuery::class,
                App\GraphQL\Query\PostsQuery::class
            ],
            'mutation' => [
                App\GraphQL\Mutation\CreateUserMutation::class,
            ],
            'types' => [],
            'middleware' => [],
            'method' => ['get', 'post'],
        ],
    ],
```

Et voici comment créer un utilisateur :

```php
mutation{
    users(name : "John Doe", email : "Johndoe@gmail.com", password : "John1234"){
        id
        name
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-26-at-03.50.14.png)
_Image de création d'utilisateur_

## Conclusion

Félicitations ! Vous avez réussi à construire un serveur GraphQL en utilisant Laravel, et vous avez exécuté des requêtes avec Postman pour obtenir des réponses. Maintenant que vous connaissez les bases de GraphQL, j'espère que vous l'utiliserez dans vos projets à venir.

Tout le code de ce tutoriel est disponible sur [GitHub](https://github.com/LarrySul/GraphQL-Laravel), qui inclut également la collection Postman.

### Ressources

* [Site web GraphQL](https://graphql.org/) 
* [Laravel GraphQL](https://github.com/rebing/graphql-laravel)
* [Comment utiliser GraphQL avec Postman](https://www.apollographql.com/blog/tooling/graphql-ide/how-to-use-graphql-with-postman/)