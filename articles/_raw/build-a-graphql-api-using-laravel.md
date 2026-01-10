---
title: How to Build a GraphQL API Using Laravel
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
seo_title: null
seo_desc: 'In this article, I''ll walk you through how to set up your own GraphQL
  API using PHP and Laravel.

  Two years ago, I started working professionally as a backend developer. And I was
  very intimidated by all the technology I didn''t yet know. Words like Do...'
---

In this article, I'll walk you through how to set up your own GraphQL API using PHP and Laravel.

Two years ago, I started working professionally as a backend developer. And I was very intimidated by all the technology I didn't yet know. Words like Docker, Kubernetes, and GraphQL seemed quite scary.

But I mustered up the courage and started to learn them all one by one.

It was actually easier than I thought, so I would like to share with you what I've learned about GraphQL by creating a simple demo project together.

You can find the final project on GitHub [here](https://github.com/TamerlanG/GraphQL-using-Laravel).

## Prerequisites

Before we begin, make sure to have these installed on your system:

* PHP 7+
* Composer 2.0
* Docker 20.10.6 (Any other version should be fine)
* Docker-Compose 1.29.1 (Any other version should be fine)

I also assume that you have:

* Basic knowledge of Laravel (Eloquent, Migrations, MVC, Routes, and so on)
* Knowledge of PHP (Syntax, OOP, and so on)
* Basic knowledge of GraphQL (in theory)

## What We're Going to Build

I like RPG games like the Elder Scrolls Series or Final Fantasy, so of course our app will be about games. The project will consist of only two models called **Quests** and **Categories**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1-1.png)
_Database Schema_

By the end of this post we will create a CRUD GraphQL API for each model.

## How to Initialize the Project

Create a Laravel project using this command:

```bash
composer create-project laravel/laravel quest_journal

```

This will create a new project in a new directory called `quest_journal`.

Next let's setup sail like this:

```bash
# Move into the project
cd quest_journal

# Install and configure laravel sail
php artisan sail:install

```

It's gonna ask you which services to install. Just press `enter` to only install MySQL.

If all goes well, you should now see a `docker-compose.yml` file in your project directory.

Let's then run the containers using sail:

```bash
# Run the containers
./vendor/bin/sail up -d

# Check if the containers are running
docker ps

```

At this point I suggest you alias `sail` to `./vendor/bin/sail`. You can do that by adding this piece of code to your `bashrc` or `zshrc`:

```bash
# in ~./zshrc or ~./bashrc

alias sail = 'bash vendor/bin/sail'

```

Moving on, if you go to [localhost](http://localhost/) you should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/2.png)
_Default Laravel Home Page_

But before we move on, there are some packages that we need to install first:

```bash
# IDE helper for laravel, always useful to have.
sail composer require --dev barryvdh/laravel-ide-helper

# GraphQL library which we are going to use
sail composer require rebing/graphql-laravel

```

Next we have to publish the GraphQL library like this:

```bash
sail artisan vendor:publish --provider="Rebing\\GraphQL\\GraphQLServiceProvider"

```

This should create a GraphQL config file that we will use in `config/graphql.php`.

## How to Create the Migrations and Models

This isn't a Laravel tutorial, so we'll quickly create the models with the appropriate migrations.

Let's start with category model:

```bash
# Create model with migrations
sail artisan make:model -m Category

```

This will create the Category model with it's migration file.

Our category will consist of four fields:

* ID
* Title
* Created_At
* Updated_At

Our category migrations file should look like this:

```php
<?php

// database/migrations/yyyy_mm_dd_hhMMss_create_categories_table.php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

class CreateCategoriesTable extends Migration
{
    /**
     * Run the migrations.
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
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('categories');
    }
}

```

Next let's configure the category model class.

We will do two things here:

* Make the field `title` editable, so we will add it to our `$fillable` array.
* Define the relationship between category model and quest model.

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

You will have some errors concerning the Quest model, but no worries – we will handle that next.

Run the command to make a model and migration file for quest:

```bash
sail artisan make:model -m Quest

```

This will create a model named Quest and a migration file for it.

Our quest will have the fields:

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
     * Run the migrations.
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
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('quests');
    }
}

```

As you can see, we declared the `category_id` to be a `foreignId`. This way Laravel will automatically create a foreign key relationship between the tables `categories` and `quests`.

Next let's configure the quest model class. 

Here we will:

* Make the appropriate fields editable by adding them to the `$fillable` array.
* Define the relationship between category model and quest model.

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

With both the migrations and models ready, we can apply the changes to the database.

Run this command:

```bash
# Apply migrations
sail artisan migrate

```

Our database should be updated! Next we should put some data into our tables.

## How to Seed the Database

We need data to work with, but as developers we are too lazy to manually do it. 

This is where factories come.

First, we'll create the factory classes for both the quest and category model.

Run the following commands:

```bash
# Create a factory class for quest model
sail artisan make:factory QuestFactory --model=Quest

# Create a factory class for category model
sail artisan make:factory CategoryFactory --model=Category

```

This will create for us two new classes:

* `QuestFactory` – a class that helps us generate quests.
* `CategoryFactory` – a class that helps us generate categories.

Let's start with the `QuestFactory`. In our `definitions` function we will tell Laravel how each field should be generated. For the field `category_id`, we will pick a random category.

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
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Quest::class;

    /**
     * Define the model's default state.
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

`CategoryFactory` is much simpler, as we simply have to generate a title.

```php
<?php

// database/factories/CategoryFactory.php

namespace Database\\Factories;

use App\\Models\\Category;
use Illuminate\\Database\\Eloquent\\Factories\\Factory;

class CategoryFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Category::class;

    /**
     * Define the model's default state.
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

Now instead of creating seeders, we will simply run the factory create method inside `DatabaseSeeder.php`:

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
     * Seed the application's database.
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

Finally run the command to seed the database.

```php
sail artisan db:seed

```

## Folder Structure

At this point we are ready to create our GraphQL APIs. To do that let's first create a new folder in the `app` directory called `GraphQL`.

Inside the GraphQL folder, create three new folders:

* Mutations
* Queries
* Types

It will look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/3.png)

This is where the bulk of our code will be. As you might be able to tell, it's very different from REST architecture. Before we begin writing the code, let me quickly explain the purpose of each folder.

* **Mutations**: This folder will contain classes that manage the insert, update, and delete operations.
* **Queries**: This folder will contain the classes that fetch data from the database.
* **Types**: You can think of this as a model, or a model resource. Basically types are objects that can be fetched from the database. For example, we are going to have a `QuestType` and a `CategoryType`.

## How to Define the Category and Quest Types

Let's first start with types. We'll create two new classes in our types folder called:

1. `CategoryType`
2. `QuestType`

Here is where we will use the `rebing/graphql-laravel` package which basically helps us create types, queries, and mutations.

Our types will inherit the `Type` class from `Rebing\\GraphQL\\Support\\Type`. There's also another class called `Type` in the package but it's used to declare the type of field (like string, int, and so on).

Let's begin with the `CategoryType` class:

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
        'description' => 'Collection of categories',
        'model' => Category::class
    ];

    public function fields(): array
    {
        return [
            'id' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'ID of quest'
            ],
            'title' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'Title of the quest'
            ],
            'quests' => [
                'type' => Type::listOf(GraphQL::type('Quest')),
                'description' => 'List of quests'
            ]
        ];
    }
}

```

Let's break this down:

* **Attributes**: This is your type configuration. It has core information about your type, and to which model it associates.
* **Fields**: This method returns the fields that your client can ask for.

You may have noticed that we have a field called `quests` which is a list of `QuestType`. But we don't associate the class directly – we instead use its `name` from its attribute.

Next is the `QuestType` class:

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
        'description' => 'Collection of quests with their respective category',
        'model' => Quest::class
    ];

    public function fields(): array
    {
        return [
            'id' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'ID of quest'
            ],
            'title' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'Title of the quest'
            ],
            'description' => [
                'type' => Type::nonNull(Type::string()),
                'description' => 'Description of quest'
            ],
            'reward' => [
                'type' => Type::nonNull(Type::int()),
                'description' => 'Quest reward'
            ],
            'category' => [
                'type' => GraphQL::type('Category'),
                'description' => 'The category of the quest'
            ]
        ];
    }
}

```

## How to Define the Queries for Your Model

Now that we have defined our types, we can move on to queries.

For each model we will have two queries:

* A class to query a single model
* A class to query a list of models

To keep stuff organized, create two new folders in your `Queries` folder:

* Category
* Quest

Let's create our classes:

* `QuestQuery`
* `QuestsQuery`
* `CategoryQuery`
* `CategoriesQuery`

Your file structure should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/4.png)

Let's start with the `QuestQuery` class:

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

Let's break this down:

* Our query classes will inherit from `Rebing\\GraphQL\\Support\\Query`
* The `attributes` function is used as the query configuration.
* The `type` function is used to declare what type of object this query will return.
* The `args` function is used to declare what arguments this query will accept. In our case we only need the `id` of the quest.
* The `resolve` function does the bulk of the work – it returns the actual object using eloquent.

The rest of the classes have a similar format, so it's pretty much self explanatory.

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

## How to Create the Mutation Classes

Mutations will house our classes that control the insertion/deletion of our models. So for each model we will have three classes:

* A class to create a model
* A class to update a model
* A class to delete a model

We have two models in our app, so we will have 6 mutation classes.

To keep things organized, create two new folders in your `Mutations` folder:

* Category
* Quest

Let's create our mutation classes:

* `CreateCategoryMutation`
* `DeleteCategoryMutation`
* `UpdateCategoryMutation`
* `CreateQuestMutation`
* `DeleteQuestMutation`
* `UpdateQuestMutation`

Your file structure should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/5.png)

Let's start with `CreateCategoryMutation`:

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
        'description' => 'Creates a category'
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

As you can see, the structure is very similar to our queries.

Once again let's break down this class:

* Our mutation classes will inherit from `Rebing\\GraphQL\\Support\\Mutation`
* The `attributes` function is used as mutation configuration.
* The `type` function is used to declare what type of object this query will return.
* The `args` function is used to declare what arguments this mutation will accept. In our case we only need the `title` field.
* The `resolve` function does the bulk of the work – it does the actual mutation using eloquent.

The rest of the mutations have a similar format, so they should be self-explanatory.

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
        'description' => 'deletes a category'
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
        'description' => 'Updates a category'
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
        'description' => 'Creates a quest'
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
        'description' => 'Deletes a quest'
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
        'description' => 'Updates a quest'
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

## Schemas

All the hard work is done! Now we have to put everything together.

We have to register our queries, mutations, and types in our `config/graphql`:

```php
<?php

return [
    // ... some code

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

    // some code 
];

```

Now that all that's done, let's try out our APIs.

## How to Test the Queries

Our GraphQL library provides us with an IDE.

So make sure your Docker containers are running and head into [http://localhost/graphiql](http://localhost/graphiql).

You should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/05/6.png)

Let us test our queries:

### Fetch a Single Quest

![Image](https://www.freecodecamp.org/news/content/images/2021/05/7.png)

### Fetch a List of Quests

![Image](https://www.freecodecamp.org/news/content/images/2021/05/8.png)

### Insert a Quest into the Database

![Image](https://www.freecodecamp.org/news/content/images/2021/05/9.png)

### Update a Quest

![Image](https://www.freecodecamp.org/news/content/images/2021/05/10.png)

### Delete a Quest from the Database

![Image](https://www.freecodecamp.org/news/content/images/2021/05/11.png)

## Conclusion

Congratulations, you have created your first GraphQL API.

In summary:

* A GraphQL API consists of three parts: Queries, Types, and Mutations.
* Mutations manage your CRUD operations.
* Queries fetch from the database.
* Types are the model resource that gets returned to the client.

Thank you for reading!

