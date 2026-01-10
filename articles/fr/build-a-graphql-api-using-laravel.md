---
title: Comment construire une API GraphQL avec Laravel
subtitle: ''
author: Tamerlan Gudabayev
co_authors: []
series: null
date: '2021-05-26T16:34:32.000Z'
originalURL: https://freecodecamp.org/news/build-a-graphql-api-using-laravel
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/graphql-article-image.jpg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Comment construire une API GraphQL avec Laravel
seo_desc: 'In this article, I''ll walk you through how to set up your own GraphQL
  API using PHP and Laravel.

  Two years ago, I started working professionally as a backend developer. And I was
  very intimidated by all the technology I didn''t yet know. Words like Do...'
---

Dans cet article, je vais vous expliquer comment mettre en place votre propre API GraphQL en utilisant PHP et Laravel.

Il y a deux ans, j'ai commencé à travailler professionnellement en tant que développeur backend. Et j'étais très intimidé par toutes les technologies que je ne connaissais pas encore. Des mots comme Docker, Kubernetes et GraphQL semblaient assez effrayants.

Mais j'ai pris mon courage à deux mains et j'ai commencé à les apprendre un par un.

C'était en fait plus facile que je ne le pensais, c'est pourquoi j'aimerais partager avec vous ce que j'ai appris sur GraphQL en créant ensemble un projet de démonstration simple.

Vous pouvez trouver le projet final sur GitHub [ici](https://github.com/TamerlanG/GraphQL-using-Laravel).

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre système :

* PHP 7+
* Composer 2.0
* Docker 20.10.6 (toute autre version devrait convenir)
* Docker-Compose 1.29.1 (toute autre version devrait convenir)

Je suppose également que vous avez :

* Des connaissances de base sur Laravel (Eloquent, Migrations, MVC, Routes, etc.)
* Des connaissances en PHP (Syntaxe, POO, etc.)
* Des connaissances de base sur GraphQL (en théorie)

## Ce que nous allons construire

J'aime les jeux RPG comme la série Elder Scrolls ou Final Fantasy, donc bien sûr, notre application portera sur les jeux. Le projet consistera en seulement deux modèles appelés **Quests** (Quêtes) et **Categories** (Catégories).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1-1.png)
_Schéma de la base de données_

À la fin de cet article, nous aurons créé une API GraphQL CRUD pour chaque modèle.

## Comment initialiser le projet

Créez un projet Laravel à l'aide de cette commande :

```bash
composer create-project laravel/laravel quest_journal

```

Cela créera un nouveau projet dans un nouveau répertoire appelé `quest_journal`.

Ensuite, configurons Sail comme ceci :

```bash
# Se déplacer dans le projet
cd quest_journal

# Installer et configurer Laravel Sail
php artisan sail:install

```

Il vous sera demandé quels services installer. Appuyez simplement sur `entrée` pour n'installer que MySQL.

Si tout se passe bien, vous devriez maintenant voir un fichier `docker-compose.yml` dans le répertoire de votre projet.

Lançons ensuite les conteneurs en utilisant Sail :

```bash
# Lancer les conteneurs
./vendor/bin/sail up -d

# Vérifier si les conteneurs sont en cours d'exécution
docker ps

```

À ce stade, je vous suggère de créer un alias `sail` pour `./vendor/bin/sail`. Vous pouvez le faire en ajoutant ce morceau de code à votre fichier `bashrc` ou `zshrc` :

```bash
# dans ~./zshrc ou ~./bashrc

alias sail = 'bash vendor/bin/sail'

```

En continuant, si vous allez sur [localhost](http://localhost/), vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/2.png)
_Page d'accueil par défaut de Laravel_

Mais avant de poursuivre, nous devons d'abord installer certains packages :

```bash
# IDE helper pour Laravel, toujours utile à avoir.
sail composer require --dev barryvdh/laravel-ide-helper

# Bibliothèque GraphQL que nous allons utiliser
sail composer require rebing/graphql-laravel

```

Ensuite, nous devons publier la bibliothèque GraphQL comme ceci :

```bash
sail artisan vendor:publish --provider="Rebing\\GraphQL\\GraphQLServiceProvider"

```

Cela devrait créer un fichier de configuration GraphQL que nous utiliserons dans `config/graphql.php`.

## Comment créer les migrations et les modèles

Ceci n'est pas un tutoriel Laravel, nous allons donc créer rapidement les modèles avec les migrations appropriées.

Commençons par le modèle Category :

```bash
# Créer le modèle avec les migrations
sail artisan make:model -m Category

```

Cela créera le modèle Category avec son fichier de migration.

Notre catégorie sera composée de quatre champs :

* ID
* Title
* Created_At
* Updated_At

Notre fichier de migration de catégorie devrait ressembler à ceci :

```php
<?php

// database/migrations/yyyy_mm_dd_hhMMss_create_categories_table.php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

class CreateCategoriesTable extends Migration
{
    /**
     * Exécuter les migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('categories', function (Blueprint $table) {
            $table->id();
            $table->text('title');
            $table->timestamps();
        });
    }

    /**
     * Annuler les migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('categories');
    }
}

```

Ensuite, configurons la classe du modèle Category.

Nous allons faire deux choses ici :

* Rendre le champ `title` modifiable, nous l'ajouterons donc à notre tableau `$fillable`.
* Définir la relation entre le modèle Category et le modèle Quest.

```php
<?php

// App\\Models\\Category

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class Category extends Model
{
    use HasFactory;
		
	protected $fillable = ['title'];

    public function quests(){
        return $this->hasMany(Quest::class);
    }
}

```

Vous aurez quelques erreurs concernant le modèle Quest, mais ne vous inquiétez pas – nous allons gérer cela ensuite.

Lancez la commande pour créer un modèle et un fichier de migration pour Quest :

```bash
sail artisan make:model -m Quest

```

Cela créera un modèle nommé Quest et un fichier de migration correspondant.

Notre quête aura les champs :

* ID
* Title
* Description
* Reward
* Category_ID
* Created_At
* Updated_At

```php
<?php
// database/migrations/yyyy_mm_dd_hhMMss_create_quests_table.php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

class CreateQuestsTable extends Migration
{
    /**
     * Exécuter les migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('quests', function (Blueprint $table) {
            $table->id();
            $table->text('title');
            $table->text('description');
            $table->integer('reward');
            $table->foreignId('category_id')->constrained();
            $table->timestamps();
        });
    }

    /**
     * Annuler les migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('quests');
    }
}

```

Comme vous pouvez le voir, nous avons déclaré `category_id` comme étant un `foreignId`. De cette façon, Laravel créera automatiquement une relation de clé étrangère entre les tables `categories` et `quests`.

Ensuite, configurons la classe du modèle Quest.

Ici, nous allons :

* Rendre les champs appropriés modifiables en les ajoutant au tableau `$fillable`.
* Définir la relation entre le modèle Category et le modèle Quest.

```php
<?php

// App\\Models\\Quest

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class Quest extends Model
{
    use HasFactory;
		
	protected $fillable = ['title', 'category_id', 'description', 							  'reward'];

    public function category(){
        return $this->belongsTo(Category::class);
    }
}

```

Avec les migrations et les modèles prêts, nous pouvons appliquer les changements à la base de données.

Lancez cette commande :

```bash
# Appliquer les migrations
sail artisan migrate

```

Notre base de données devrait être mise à jour ! Ensuite, nous devrions insérer des données dans nos tables.

## Comment peupler la base de données

Nous avons besoin de données pour travailler, mais en tant que développeurs, nous sommes trop paresseux pour le faire manuellement.

C'est là que les factories interviennent.

Tout d'abord, nous allons créer les classes factory pour les modèles Quest et Category.

Lancez les commandes suivantes :

```bash
# Créer une classe factory pour le modèle Quest
sail artisan make:factory QuestFactory --model=Quest

# Créer une classe factory pour le modèle Category
sail artisan make:factory CategoryFactory --model=Category

```

Cela créera pour nous deux nouvelles classes :

* `QuestFactory` – une classe qui nous aide à générer des quêtes.
* `CategoryFactory` – une classe qui nous aide à générer des catégories.

Commençons par `QuestFactory`. Dans notre fonction `definition`, nous allons dire à Laravel comment chaque champ doit être généré. Pour le champ `category_id`, nous choisirons une catégorie au hasard.

```php
<?php

// database/factories/QuestFactory.php

namespace Database\\Factories;

use App\\Models\\Category;
use App\\Models\\Quest;
use Illuminate\\Database\\Eloquent\\Factories\\Factory;

class QuestFactory extends Factory
{
    /**
     * Le nom du modèle correspondant à la factory.
     *
     * @var string
     */
    protected $model = Quest::class;

    /**
     * Définir l'état par défaut du modèle.
     *
     * @return array
     */
    public function definition()
    {
        $categoryIDs = Category::all()->pluck('id')->toArray();

        return [
            'title' => $this->faker->title(),
            'description' => $this->faker->text(),
            'reward' => $this->faker->numberBetween(1 , 100),
            'category_id' => $this->faker->randomElement($categoryIDs)
        ];
    }
}
```

`CategoryFactory` est beaucoup plus simple, car nous n'avons qu'à générer un titre.

```php
<?php

// database/factories/CategoryFactory.php

namespace Database\\Factories;

use App\\Models\\Category;
use Illuminate\\Database\\Eloquent\\Factories\\Factory;

class CategoryFactory extends Factory
{
    /**
     * Le nom du modèle correspondant à la factory.
     *
     * @var string
     */
    protected $model = Category::class;

    /**
     * Définir l'état par défaut du modèle.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'title' => $this->faker->title()
        ];
    }
}

```

Maintenant, au lieu de créer des seeders, nous allons simplement exécuter la méthode create de la factory à l'intérieur de `DatabaseSeeder.php` :

```php
<?php

// database/seeders/DatabaseSeeder.php

namespace Database\\Seeders;

use App\\Models\\Category;
use App\\Models\\Quest;
use Illuminate\\Database\\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Peupler la base de données de l'application.
     *
     * @return void
     */
    public function run()
    {
        Category::factory(10)->create();
        Quest::factory(10)->create();
    }
}

```

Enfin, lancez la commande pour peupler la base de données.

```php
sail artisan db:seed

```

## Structure des dossiers

À ce stade, nous sommes prêts à créer nos API GraphQL. Pour ce faire, créons d'abord un nouveau dossier dans le répertoire `app` appelé `GraphQL`.

À l'intérieur du dossier GraphQL, créez trois nouveaux dossiers :

* Mutations
* Queries
* Types

Cela ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/3.png)

C'est ici que se trouvera l'essentiel de notre code. Comme vous pouvez le constater, c'est très différent de l'architecture REST. Avant de commencer à écrire le code, laissez-moi vous expliquer rapidement le but de chaque dossier.

* **Mutations** : Ce dossier contiendra les classes qui gèrent les opérations d'insertion, de mise à jour et de suppression.
* **Queries** : Ce dossier contiendra les classes qui récupèrent les données de la base de données.
* **Types** : Vous pouvez considérer cela comme un modèle, ou une ressource de modèle. Fondamentalement, les types sont des objets qui peuvent être récupérés de la base de données. Par exemple, nous allons avoir un `QuestType` et un `CategoryType`.

## Comment définir les types Category et Quest

Commençons d'abord par les types. Nous allons créer deux nouvelles classes dans notre dossier types appelées :

1. `CategoryType`
2. `QuestType`

C'est ici que nous utiliserons le package `rebing/graphql-laravel` qui nous aide essentiellement à créer des types, des requêtes et des mutations.

Nos types hériteront de la classe `Type` de `Rebing\\GraphQL\\Support\\Type`. Il existe également une autre classe appelée `Type` dans le package, mais elle est utilisée pour déclarer le type de champ (comme string, int, etc.).

Commençons par la classe `CategoryType` :

```php
<?php

// app/graphql/types/CategoryType 

namespace App\\GraphQL\\Types;

use App\\Models\\Category;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Type as GraphQLType;

class CategoryType extends GraphQLType
{
    protected $attributes = [
        'name' => 'Category',
        'description' => 'Collection de catégories',
        'model' => Category::class
    ];

    public function fields(): array
    {
        return [
            'id' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'ID de la quête'
            ],
            'title' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'Titre de la quête'
            ],
            'quests' => [
                'type' => Type::listOf(GraphQL::type('Quest')),
                'description' => 'Liste des quêtes'
            ]
        ];
    }
}

```

Analysons cela :

* **Attributes** : C'est la configuration de votre type. Elle contient des informations de base sur votre type et le modèle auquel il est associé.
* **Fields** : Cette méthode renvoie les champs que votre client peut demander.

Vous avez peut-être remarqué que nous avons un champ appelé `quests` qui est une liste de `QuestType`. Mais nous n'associons pas la classe directement – nous utilisons plutôt son `name` provenant de son attribut.

Ensuite, la classe `QuestType` :

```php
<?php

// app/graphql/types/QuestType 

namespace App\\GraphQL\\Types;

use App\\Models\\Quest;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Type as GraphQLType;

class QuestType extends GraphQLType
{
    protected $attributes = [
        'name' => 'Quest',
        'description' => 'Collection de quêtes avec leur catégorie respective',
        'model' => Quest::class
    ];

    public function fields(): array
    {
        return [
            'id' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'ID de la quête'
            ],
            'title' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'Titre de la quête'
            ],
            'description' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'Description de la quête'
            ],
            'reward' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'Récompense de la quête'
            ],
            'category' => [
                'type' => GraphQL::type('Category'),
                'description' => 'La catégorie de la quête'
            ]
        ];
    }
}

```

## Comment définir les requêtes pour votre modèle

Maintenant que nous avons défini nos types, nous pouvons passer aux requêtes (queries).

Pour chaque modèle, nous aurons deux requêtes :

* Une classe pour interroger un seul modèle
* Une classe pour interroger une liste de modèles

Pour garder les choses organisées, créez deux nouveaux dossiers dans votre dossier `Queries` :

* Category
* Quest

Créons nos classes :

* `QuestQuery`
* `QuestsQuery`
* `CategoryQuery`
* `CategoriesQuery`

Votre structure de fichiers devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/4.png)

Commençons par la classe `QuestQuery` :

```php
<?php

// app/graphql/queries/quest/QuestQuery 

namespace App\\GraphQL\\Queries\\Quest;

use App\\Models\\Quest;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Query;

class QuestQuery extends Query
{
    protected $attributes = [
        'name' => 'quest',
    ];

    public function type(): Type
    {
        return GraphQL::type('Quest');
    }

    public function args(): array
    {
        return [
            'id' => [
                'name' => 'id',
                'type' => Type::int(),
                'rules' => ['required']
            ]
        ];
    }

    public function resolve($root, $args)
    {
        return Quest::findOrFail($args['id']);
    }
}

```

Analysons cela :

* Nos classes de requête hériteront de `Rebing\\GraphQL\\Support\\Query`
* La fonction `attributes` est utilisée comme configuration de la requête.
* La fonction `type` est utilisée pour déclarer quel type d'objet cette requête retournera.
* La fonction `args` est utilisée pour déclarer quels arguments cette requête acceptera. Dans notre cas, nous n'avons besoin que de l' `id` de la quête.
* La fonction `resolve` fait le gros du travail – elle renvoie l'objet réel en utilisant Eloquent.

Le reste des classes a un format similaire, donc c'est assez explicite.

```php
<?php

// app/graphql/queries/quest/QuestsQuery 

namespace App\\GraphQL\\Queries\\Quest;

use App\\Models\\Quest;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Query;

class QuestsQuery extends Query
{
    protected $attributes = [
        'name' => 'quests',
    ];

    public function type(): Type
    {
        return Type::listOf(GraphQL::type('Quest'));
    }

    public function resolve($root, $args)
    {
        return Quest::all();
    }
}

```

```php
<?php

// app/graphql/queries/category/CategoryQuery 

namespace App\\GraphQL\\Queries\\Category;

use App\\Models\\Category;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Query;

class CategoryQuery extends Query
{
    protected $attributes = [
        'name' => 'category',
    ];

    public function type(): Type
    {
        return GraphQL::type('Category');
    }

    public function args(): array
    {
        return [
            'id' => [
                'name' => 'id',
                'type' => Type::int(),
                'rules' => ['required']
            ]
        ];
    }

    public function resolve($root, $args)
    {
        return Category::findOrFail($args['id']);
    }
}

```

```php
<?php

// app/graphql/queries/category/CategoriesQuery 

namespace App\\GraphQL\\Queries\\Category;

use App\\Models\\Category;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Query;

class CategoriesQuery extends Query
{
    protected $attributes = [
        'name' => 'categories',
    ];

    public function type(): Type
    {
        return Type::listOf(GraphQL::type('Category'));
    }

    public function resolve($root, $args)
    {
        return Category::all();
    }
}

```

## Comment créer les classes de mutation

Les mutations hébergeront nos classes qui contrôlent l'insertion/suppression de nos modèles. Ainsi, pour chaque modèle, nous aurons trois classes :

* Une classe pour créer un modèle
* Une classe pour mettre à jour un modèle
* Une classe pour supprimer un modèle

Nous avons deux modèles dans notre application, nous aurons donc 6 classes de mutation.

Pour garder les choses organisées, créez deux nouveaux dossiers dans votre dossier `Mutations` :

* Category
* Quest

Créons nos classes de mutation :

* `CreateCategoryMutation`
* `DeleteCategoryMutation`
* `UpdateCategoryMutation`
* `CreateQuestMutation`
* `DeleteQuestMutation`
* `UpdateQuestMutation`

Votre structure de fichiers devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/5.png)

Commençons par `CreateCategoryMutation` :

```php
<?php

// app/graphql/mutations/category/CreateCategoryMutation 

namespace App\\GraphQL\\Mutations\\Category;

use App\\Models\\Category;
use Rebing\\GraphQL\\Support\\Mutation;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;

class CreateCategoryMutation extends Mutation
{
    protected $attributes = [
        'name' => 'createCategory',
        'description' => 'Crée une catégorie'
    ];

    public function type(): Type
    {
        return GraphQL::type('Category');
    }

    public function args(): array
    {
        return [
            'title' => [
                'name' => 'title',
                'type' =>  Type::nonNull(Type::string()),
            ],
        ];
    }

    public function resolve($root, $args)
    {
        $category = new Category();
        $category->fill($args);
        $category->save();

        return $category;
    }
}

```

Comme vous pouvez le voir, la structure est très similaire à nos requêtes.

Encore une fois, analysons cette classe :

* Nos classes de mutation hériteront de `Rebing\\GraphQL\\Support\\Mutation`
* La fonction `attributes` est utilisée comme configuration de la mutation.
* La fonction `type` est utilisée pour déclarer quel type d'objet cette requête retournera.
* La fonction `args` est utilisée pour déclarer quels arguments cette mutation acceptera. Dans notre cas, nous n'avons besoin que du champ `title`.
* La fonction `resolve` fait le gros du travail – elle effectue la mutation réelle en utilisant Eloquent.

Le reste des mutations a un format similaire, elles devraient donc être explicites.

```php
<?php

// app/graphql/mutations/category/DeleteCategoryMutation 

namespace App\\GraphQL\\Mutations\\Category;

use App\\Models\\Category;
use Rebing\\GraphQL\\Support\\Mutation;
use GraphQL\\Type\\Definition\\Type;

class DeleteCategoryMutation extends Mutation
{
    protected $attributes = [
        'name' => 'deleteCategory',
        'description' => 'supprime une catégorie'
    ];

    public function type(): Type
    {
        return Type::boolean();
    }

    public function args(): array
    {
        return [
            'id' => [
                'name' => 'id',
                'type' => Type::int(),
                'rules' => ['required']
            ]
        ];
    }

    public function resolve($root, $args)
    {
        $category = Category::findOrFail($args['id']);

        return  $category->delete() ? true : false;
    }
}

```

```php
<?php

// app/graphql/mutations/category/UpdateCategoryMutation 

namespace App\\GraphQL\\Mutations\\Category;

use App\\Models\\Category;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Mutation;

class UpdateCategoryMutation extends Mutation
{
    protected $attributes = [
        'name' => 'updateCategory',
        'description' => 'Met à jour une catégorie'
    ];

    public function type(): Type
    {
        return GraphQL::type('Category');
    }

    public function args(): array
    {
        return [
            'id' => [
                'name' => 'id',
                'type' =>  Type::nonNull(Type::int()),
            ],
            'title' => [
                'name' => 'title',
                'type' =>  Type::nonNull(Type::string()),
            ],
        ];
    }

    public function resolve($root, $args)
    {
        $category = Category::findOrFail($args['id']);
        $category->fill($args);
        $category->save();

        return $category;
    }
}

```

```php
<?php

// app/graphql/mutations/quest/CreateQuestMutation 

namespace App\\GraphQL\\Mutations\\Quest;

use App\\Models\\Quest;
use Rebing\\GraphQL\\Support\\Mutation;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;

class CreateQuestMutation extends Mutation
{
    protected $attributes = [
        'name' => 'createQuest',
        'description' => 'Crée une quête'
    ];

    public function type(): Type
    {
        return GraphQL::type('Quest');
    }

    public function args(): array
    {
        return [
            'title' => [
                'name' => 'title',
                'type' =>  Type::nonNull(Type::string()),
            ],
            'description' => [
                'name' => 'description',
                'type' =>  Type::nonNull(Type::string()),
            ],
            'reward' => [
                'name' => 'reward',
                'type' => Type::nonNull(Type::int()),
            ],
            'category_id' => [
                'name' => 'category_id',
                'type' => Type::nonNull(Type::int()),
                'rules' => ['exists:categories,id']
            ]
        ];
    }

    public function resolve($root, $args)
    {
        $quest = new Quest();
        $quest->fill($args);
        $quest->save();

        return $quest;
    }
}

```

```php
<?php

// app/graphql/mutations/quest/DeleteQuestMutation 

namespace App\\GraphQL\\Mutations\\Quest;

use App\\Models\\Quest;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Mutation;

class DeleteQuestMutation extends Mutation
{
    protected $attributes = [
        'name' => 'deleteQuest',
        'description' => 'Supprime une quête'
    ];

    public function type(): Type
    {
        return Type::boolean();
    }

    public function args(): array
    {
        return [
            'id' => [
                'name' => 'id',
                'type' => Type::nonNull(Type::int()),
                'rules' => ['exists:quests']
            ]
        ];
    }

    public function resolve($root, $args)
    {
        $category = Quest::findOrFail($args['id']);

        return  $category->delete() ? true : false;
    }
}

```

```php
<?php

// app/graphql/mutations/quest/UpdateQuestMutation 

namespace App\\GraphQL\\Mutations\\Quest;

use App\\Models\\Quest;
use GraphQL\\Type\\Definition\\Type;
use Rebing\\GraphQL\\Support\\Facades\\GraphQL;
use Rebing\\GraphQL\\Support\\Mutation;

class UpdateQuestMutation extends Mutation
{
    protected $attributes = [
        'name' => 'updateQuest',
        'description' => 'Met à jour une quête'
    ];

    public function type(): Type
    {
        return GraphQL::type('Quest');
    }

    public function args(): array
    {
        return [
            'id' => [
                'name' => 'id',
                'type' =>  Type::nonNull(Type::int()),
            ],
            'title' => [
                'name' => 'title',
                'type' =>  Type::nonNull(Type::string()),
            ],
            'description' => [
                'name' => 'description',
                'type' =>  Type::nonNull(Type::string()),
            ],
            'reward' => [
                'name' => 'reward',
                'type' => Type::nonNull(Type::int()),
            ],
            'category_id' => [
                'name' => 'category_id',
                'type' => Type::nonNull(Type::int()),
                'rules' => ['exists:categories,id']
            ]
        ];
    }

    public function resolve($root, $args)
    {
        $quest = Quest::findOrFail($args['id']);
        $quest->fill($args);
        $quest->save();

        return $quest;
    }
}

```

## Schémas

Tout le travail difficile est fait ! Maintenant, nous devons tout assembler.

Nous devons enregistrer nos requêtes, mutations et types dans notre fichier `config/graphql` :

```php
<?php

return [
    // ... du code

    'schemas' => [
        'default' => [
            'query' => [
                'quest' => \\App\\GraphQL\\Queries\\Quest\\QuestQuery::class,
                'quests' => \\App\\GraphQL\\Queries\\Quest\\QuestsQuery::class,
                'category' => \\App\\GraphQL\\Queries\\Category\\CategoryQuery::class,
                'categories' => \\App\\GraphQL\\Queries\\Category\\CategoriesQuery::class,
            ],
            'mutation' => [
                'createQuest' => \\App\\GraphQL\\Mutations\\Quest\\CreateQuestMutation::class,
                'updateQuest' => \\App\\GraphQL\\Mutations\\Quest\\UpdateQuestMutation::class,
                'deleteQuest' => \\App\\GraphQL\\Mutations\\Quest\\DeleteQuestMutation::class,
                'createCategory' => \\App\\GraphQL\\Mutations\\Category\\CreateCategoryMutation::class,
                'updateCategory' => \\App\\GraphQL\\Mutations\\Category\\UpdateCategoryMutation::class,
                'deleteCategory' => \\App\\GraphQL\\Mutations\\Category\\DeleteCategoryMutation::class,
            ],
            'middleware' => [],
            'method' => ['get', 'post'],
        ],
    ],

		'types' => [
       'Quest' => \\App\\GraphQL\\Types\\QuestType::class,
       'Category' => \\App\\GraphQL\\Types\\CategoryType::class
    ],

    // du code 
];

```

Maintenant que tout cela est fait, essayons nos API.

## Comment tester les requêtes

Notre bibliothèque GraphQL nous fournit un IDE.

Assurez-vous donc que vos conteneurs Docker sont en cours d'exécution et rendez-vous sur [http://localhost/graphiql](http://localhost/graphiql).

Vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/6.png)

Testons nos requêtes :

### Récupérer une seule quête

![Image](https://www.freecodecamp.org/news/content/images/2021/05/7.png)

### Récupérer une liste de quêtes

![Image](https://www.freecodecamp.org/news/content/images/2021/05/8.png)

### Insérer une quête dans la base de données

![Image](https://www.freecodecamp.org/news/content/images/2021/05/9.png)

### Mettre à jour une quête

![Image](https://www.freecodecamp.org/news/content/images/2021/05/10.png)

### Supprimer une quête de la base de données

![Image](https://www.freecodecamp.org/news/content/images/2021/05/11.png)

## Conclusion

Félicitations, vous avez créé votre première API GraphQL.

En résumé :

* Une API GraphQL se compose de trois parties : les requêtes (Queries), les types (Types) et les mutations (Mutations).
* Les mutations gèrent vos opérations CRUD.
* Les requêtes récupèrent les données de la base de données.
* Les types sont les ressources de modèle qui sont renvoyées au client.

Merci de m'avoir lu !