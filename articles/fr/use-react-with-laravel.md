---
title: Comment utiliser React.js avec Laravel pour créer une application de liste
  de tâches glissables
subtitle: ''
author: San B
co_authors: []
series: null
date: '2024-01-26T00:09:49.000Z'
originalURL: https://freecodecamp.org/news/use-react-with-laravel
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/freecodecamp-boolfalse-laravel-react-vite-draggable-tasklist.png
tags:
- name: Laravel
  slug: laravel
- name: React
  slug: react
- name: vite
  slug: vite
seo_title: Comment utiliser React.js avec Laravel pour créer une application de liste
  de tâches glissables
seo_desc: 'You may have seen tutorials that help you build a simple React.js app that
  use some third-party API or a Node.js server as a backend. You could also use Laravel
  for this purpose and integrate it with React.

  As a backend framework, Laravel actually of...'
---

Vous avez peut-être vu des tutoriels qui vous aident à créer une application React.js simple utilisant une API tierce ou un serveur Node.js comme backend. Vous pouvez également utiliser Laravel à cette fin et l'intégrer avec React.

En tant que framework backend, Laravel offre en réalité un outil pour vous aider à faire cela, appelé [Inertia](https://laravel.com/docs/10.x/frontend#inertia). Voici ce que disent les docs à ce sujet :

> Il comble le fossé entre votre application Laravel et votre frontend moderne Vue ou React, vous permettant de créer des frontends modernes et complets en utilisant Vue ou React tout en exploitant les routes et contrôleurs Laravel pour le routage, l'hydratation des données et l'authentification — le tout dans un seul dépôt de code.

Mais que faire si vous ne souhaitez pas utiliser un tel outil ? Et si vous souhaitez simplement utiliser React.js comme bibliothèque frontend et avoir un backend simple alimenté par Laravel ?

Eh bien, dans cet article, vous apprendrez comment utiliser React.js avec Laravel comme backend en créant une application de liste de tâches glissables.

Pour cette application full-stack monopage, vous utiliserez [Vite.js](https://vitejs.dev/) comme outil de build frontend et le package [react-beautiful-dnd](https://www.npmjs.com/package/react-beautiful-dnd) pour les éléments glissables.

À la fin de cet article, vous aurez une application monopage pour gérer les tâches, qui ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/tasklist.png)
_Capturé à partir d'un projet local fonctionnel_

Dans cet article, nous allons créer une page dynamique qui aura une liste de tâches, chacune appartenant à un projet spécifique. Ainsi, l'utilisateur pourra sélectionner un projet, et seules les tâches du projet sélectionné seront affichées sur la page. L'utilisateur peut également créer une nouvelle tâche pour le projet actuel, ainsi que modifier, supprimer et réorganiser les tâches en les glissant et en les déposant.

## Table des matières :

* [Prérequis](#heading-prerequis)
* [Le Backend : Comment installer Laravel](#heading-le-backend-comment-installer-laravel)
* [Comment créer des Modèles et des Migrations](#heading-comment-creer-des-modeles-et-des-migrations)
* [Comment créer des Seeders](#heading-comment-creer-des-seeders)
* [Comment se connecter à la base de données MySQL](#heading-comment-se-connecter-a-la-base-de-donnees-mysql)
* [Injection de Service](#heading-injection-de-service)
* [Routes Web et API dans Laravel](#heading-routes-web-et-api-dans-laravel)
* [Requêtes de Validation dans Laravel](#heading-requetes-de-validation-dans-laravel)
* [Comment écrire un Contrôleur qui utilise des Services](#heading-comment-ecrire-un-controleur-qui-utilise-des-services)
* [Comment Tester les Routes API](#heading-comment-tester-les-routes-api)
* [Le Frontend : Comment installer les Packages](#heading-le-frontend-comment-installer-les-packages)
* [Comment Configurer Vite.js](#heading-comment-configurer-vitejs)
* [React.js – Intégration Initiale](#heading-reactjs-integration-initiale)
* [Comment Ajouter du CSS](#heading-comment-ajouter-du-css)
* [Un Service pour les requêtes API](#heading-un-service-pour-les-requetes-api)
* [Composants React.js](#heading-composants-reactjs)
* [Résultats Finaux](#heading-resultats-finaux)
* [Conclusion](#heading-conclusion)

## Prérequis

Avant de suivre cet article, il serait utile d'avoir une compréhension de base de React.js, Laravel, et une familiarité avec les concepts fondamentaux du développement web.

Vous aurez besoin des outils suivants pour l'application que nous allons construire dans cet article :

* **PHP** 8.1 ou supérieur (exécutez `php -v` pour vérifier la version)
* **Composer** (exécutez `composer` pour vérifier qu'il existe)
* **Node.js** 18 ou supérieur (exécutez `node -v` pour vérifier la version)
* **MySQL** 5.7 ou supérieur (exécutez `mysql --version` pour vérifier s'il existe, ou suivez les [docs](https://dev.mysql.com/doc/mysql-windows-excerpt/5.7/en/windows-testing.html))

Outils supplémentaires (optionnels) que vous pouvez utiliser :

* **Postman** – un programme avec une interface utilisateur pour tester les routes API
* **curl** – une commande CLI pour tester les routes API

Nous commencerons par construire le backend, puis nous passerons au frontend.

## Le Backend : Comment installer Laravel

Tout d'abord, si vous ne l'avez pas déjà, vous devrez installer le framework Laravel sur votre machine locale.

Une façon d'installer Laravel est d'utiliser un gestionnaire de dépendances populaire pour PHP appelé Composer. Voici la commande à utiliser :

```shell
composer create-project laravel/laravel tasklist
```

Cela installera la dernière version stable de Laravel sur votre machine locale (actuellement, c'est la version 10).

Le _tasklist_ dans la commande est le nom du dossier racine de l'application, que vous pouvez définir comme vous le souhaitez.

À ce stade, vous pouvez vous déplacer dans le dossier du projet et exécuter l'application backend sans avoir besoin de configurer un serveur virtuel :

```shell
cd tasklist/ && php artisan serve
```

Le `artisan` dans la commande ci-dessus est un outil CLI inclus dans Laravel. Il existe à la racine de votre application Laravel sous la forme du fichier de script `artisan`, qui fournit un certain nombre de commandes utiles qui peuvent vous assister pendant que vous construisez votre application. Nous l'utiliserons souvent dans cet article.

Visitez [`http://127.0.0.1:8000`](http://127.0.0.1:8000) dans votre navigateur pour voir la page par défaut. Elle devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/laravel.png)
_Page d'accueil de Laravel_

## Comment créer des Modèles et des Migrations

Maintenant, créons les modèles _Project_ et _Task_, ainsi que les migrations pour eux.

Les modèles sont la façon dont vos entités d'application doivent être définies, et les migrations sont comme des définitions de schéma pour stocker les enregistrements de ces entités dans la base de données.

Vous pouvez créer des fichiers de modèle et de migration manuellement ainsi que les générer en utilisant la commande `artisan` :

```shell
php artisan make:model Project -m
php artisan make:model Task -m
```

L'argument `-m` générera automatiquement un fichier de migration en utilisant le nom du modèle fourni.

Gardez la séquence d'exécution des commandes telle quelle, afin que la migration du projet puisse s'exécuter avant la migration de la tâche.

Cela est important, car les tables `projects` et `tasks` doivent avoir une relation un-à-plusieurs (1-N) : chaque tâche fera référence à un seul projet, ou, en d'autres termes, chaque projet peut avoir plusieurs tâches.

Définissez les champs `$fillable` du modèle `Project` et la méthode de relation `task()` comme suit :

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Project extends Model
{
    use HasFactory;

    protected $table = 'projects';
    public $timestamps = false;
    protected $fillable = [
        'id', // clé primaire, auto-incrément, entier
        'name', // chaîne
    ];

    // un projet peut avoir plusieurs tâches
    public function tasks(): HasMany
    {
        return $this->hasMany(Task::class);
    }
}

```

Par défaut, la propriété publique `$timestamps` a une valeur `true`, qui provient de la classe parente `Model`. Cela signifie que les colonnes `created_at` et `updated_at` dans votre table de base de données seront maintenues automatiquement par _Eloquent_ (l'ORM inclus dans Laravel).

Mais vous pouvez la personnaliser en changeant sa valeur à `false`. Nous n'avons pas besoin d'avoir les champs `created_at` et `updated_at` dans la table `projects`, donc nous définirons `$timestamps` à `false`.

Définissez les champs `$fillable` du modèle `Task`, la méthode de relation `project()` et l'accessor `created`. Un [accessor](https://laravel.com/docs/10.x/eloquent-mutators#defining-an-accessor) dans Laravel est comme une fonction entre la base de données et votre code, qui peut accéder à l'enregistrement de la base de données déjà récupéré et le modifier.

```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\SoftDeletes;

class Task extends Model
{
    use HasFactory, SoftDeletes;

    protected $table = 'tasks';
    protected $fillable = [
        'id', // clé primaire, auto-incrément, entier
        'project_id', // clé étrangère, entier

        'priority', // entier
        'title', // chaîne
        'description', // texte
    ];
    protected $appends = [
        'created',
    ];

    // chaque tâche appartient à un seul projet
    public function project(): BelongsTo
    {
        return $this->belongsTo(Project::class);
    }

    public function getCreatedAttribute()
    {
        return $this->created_at->diffForHumans();
    }
}
```

Ci-dessus, dans le modèle `Task`, il y a un accessor appelé `created`. Pour avoir un accessor, nous avons le champ `created` dans le tableau `$appends`, et aussi une fonction publique `getCreatedAttribute()`.

Dans la fonction `get**<WordsInCamelCase>**Attribute()`, il y a une logique qui s'exécutera pour modifier l'enregistrement de la base de données déjà récupéré.

Dans notre cas, la fonction `getCreatedAttribute()` retournera une différence de temps lisible et conviviale entre l'heure actuelle et l'heure donnée. Par exemple, _"il y a 3 minutes"_ ou _"il y a 4 mois"_.

Maintenant que les modèles sont prêts, configurons les migrations.

Tout d'abord, configurez une migration pour la table `projects` :

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('projects', function (Blueprint $table) {
            $table->id();
            $table->string('name');
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('projects');
    }
};
```

Ensuite, configurez une migration pour la table `tasks` :

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('tasks', function (Blueprint $table) {
            $table->id();

            $table->foreignId('project_id')->nullable()->constrained();

            $table->integer('priority');
            $table->string('title');
            $table->text('description')->nullable();

            $table->timestamps();
            $table->softDeletes();
        });
    }

    public function down(): void
    {
        // supprimer les clés étrangères existantes
        Schema::table('tasks', function (Blueprint $table) {
            if (Schema::hasColumn('tasks', 'project_id')) {
                $table->dropForeign(['project_id']);
            }
        });

        // supprimer la table
        Schema::dropIfExists('tasks');
    }
};
```

La table `tasks` a une clé étrangère `project_id`, qui est une référence à la table `projects`. Il est donc bon de mettre à jour la méthode `down()` pour s'assurer que la clé étrangère `project_id` sera supprimée avant de supprimer la table `projects`.

Il y a également un champ `priority`, qui sera un nombre naturel non nul pour ordonner les tâches. Et optionnellement, vous pouvez ajouter une fonctionnalité de suppression douce au modèle `Task`.

## Comment créer des Seeders

Maintenant, nous devons ajouter des données factices aux tables `projects` et `tasks`. Pour ensemencer certaines données dans la base de données, vous pouvez utiliser les _seeders_ de Laravel. Cela vous permet de créer des données factices à utiliser dans votre base de données.

Si vous souhaitez en savoir plus sur le fonctionnement de cela, vous pouvez [consulter les docs ici](https://laravel.com/docs/10.x/seeding).

Laravel fournit un moyen de générer ces fichiers en utilisant la commande `make:seeder` artisan :

```shell
php artisan make:seeder ProjectsSeeder
php artisan make:seeder TasksSeeder
```

Ainsi, avec les commandes ci-dessus, vous aurez les fichiers `database/seeders/ProjectsSeeder.php` et `database/seeders/TasksSeeder.php` créés.

Tout d'abord, vous devrez configurer le `ProjectsSeeder` pour ajouter quelques projets à la table `projects`. Ensuite, vous pourrez configurer le `TasksSeeder` pour ajouter des tâches à la table `tasks`.

Comme je l'ai mentionné au début, chaque tâche appartiendra à un projet spécifique. D'un point de vue de base de données relationnelle, cela signifie que chaque entrée dans la table `tasks` sera liée à une entrée spécifique dans la table `projects`. Voici l'importance d'avoir une clé étrangère `project_id` dans la table `tasks` pour pouvoir relier chaque tâche à un projet spécifique ainsi que récupérer les tâches du projet spécifique.

Vous pouvez imaginer la structure de la base de données en regardant les visuels suivants :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/laravel_react_tasklist-1.png)
_généré par l'IDE PHPStorm_

En utilisant l'exemple ci-dessous, vous pouvez générer 3 projets :

```php
<?php

namespace Database\Seeders;

use App\Models\Project;
use Illuminate\Database\Seeder;

class ProjectsSeeder extends Seeder
{
    public function run(): void
    {
        for ($i = 1; $i <= 3; $i++) {
            Project::create([
                'name' => "Project $i",
            ]);
        }
    }
}
```

Ensuite, configurez `TasksSeeder`. Vous exécuterez tous les fichiers de seeder après les avoir configurés, et ils s'exécuteront un par un. Cela dit, à ce stade, votre `ProjectsSeeder` est prêt à créer quelques projets.

En l'imaginant, l'étape suivante sera de générer les tâches, chacune d'entre elles aura une référence à l'un des projets déjà existants par son champ `project_id`.

En utilisant l'exemple ci-dessous, vous pouvez générer 10 projets :

```php
<?php

namespace Database\Seeders;

use App\Models\Project;
use App\Models\Task;
use Illuminate\Database\Seeder;

class TasksSeeder extends Seeder
{
    public function run(): void
    {
        $project_ids = Project::all()->pluck('id')->toArray();

        $now = now();
        $tasks = [];
        $project_priorities = [];
        foreach ($project_ids as $project_id) {
            $project_priorities[$project_id] = 0;
        }

        for ($i = 1; $i <= 10; $i++) {
            $project_id = $project_ids[array_rand($project_ids)];
            $project_priorities[$project_id]++;

            $tasks[] = [
                'project_id' => $project_id,
                'priority' => $project_priorities[$project_id],
                'title' => "Task " . $project_priorities[$project_id],
                'description' => "Description for Task " . $project_priorities[$project_id],
                
                'created_at' => $now,
                'updated_at' => $now,
            ];
        }

        Task::insert($tasks);
    }
}

```

Le code ci-dessus récupère simplement tous les IDs de projet, puis choisit aléatoirement un projet pour chaque tâche. À la fin, il insère toutes les tâches dans la table `tasks`.

Comme vous l'avez peut-être remarqué, nous insérons `$tasks` dans la table `tasks` en utilisant la fonction statique `insert()`, qui nous permet d'insérer tous les éléments dans la table de la base de données avec une seule requête.

Mais cela a aussi un inconvénient : elle ne gère pas les champs `created_at` et `updated_at`. C'est pourquoi il est nécessaire de configurer ces champs manuellement en leur attribuant le même horodatage `$now`.

Maintenant, lorsque vous avez tous les seeders prêts, vous devez les enregistrer dans le `DatabaseSeeder`.

```php
<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        $this->call([
            ProjectsSeeder::class,
            TasksSeeder::class,
        ]);
    }
}
```

## Comment se connecter à la base de données MySQL

Avant d'exécuter les migrations et les seeders, créez une base de données MySQL et configurez les informations d'identification appropriées dans le fichier `.env`. Si le fichier `.env` n'existe pas, créez-le et collez le contenu du fichier `.env.example` dedans.

Après avoir configuré les informations d'identification de la base de données, vous aurez ces types de variables d'environnement :

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE="<DATABASE_NAME>"
DB_USERNAME="<USERNAME>"
DB_PASSWORD="<PASSWORD>"
```

Après avoir configuré les variables d'environnement, optimisez le cache :

```shell
php artisan optimize
```

Maintenant, vous pourrez créer les tables `projects` et `tasks` dans la base de données MySQL, configurer leur structure et ajouter des enregistrements initiaux avec une seule commande :

```shell
php artisan migrate:fresh --seed
```

Dans la commande ci-dessus, l'argument `migrate:fresh` supprimera toutes les tables de la base de données. Ensuite, il exécutera la commande `migrate`, qui exécutera vos migrations pour créer les tables `projects` et `tasks` de manière appropriée.

Avec l'argument `--seed`, il exécutera `ProjectsSeeder` et `TasksSeeder` après les migrations. Cela dit, il videra votre base de données pour vous, et créera toutes les tables et remplira toutes les données factices nécessaires.

Après avoir exécuté la commande, vous aurez ces types d'enregistrements de base de données :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-74.png)
_Une capture d'écran de l'IDE PHPStorm_

## Injection de Service

Maintenant, créons une classe de contrôleur et de service pour gérer toutes les fonctionnalités des tâches, telles que la liste, la création, la mise à jour, la suppression et le réordonnancement des tâches.

Tout d'abord, utilisez la commande ci-dessous pour générer un contrôleur.

```shell
php artisan make:controller TaskController
```

Afin de ne pas placer tout le code dans le contrôleur, vous pouvez garder uniquement la logique principale, et déplacer les autres implémentations logiques vers un autre fichier de classe.

Ces classes sont généralement appelées _services_, et l'utilisation d'implémentations de service dans une méthode de contrôleur est appelée **injection de service** (elle vient du terme _injection de dépendance_).

L'un des principaux avantages de l'utilisation des services est qu'il vous aide à créer une base de code maintenable.

Vous pouvez injecter votre classe de service dans la méthode de construction du contrôleur en tant qu'argument, donc après chaque exécution du contrôleur (quand la méthode `__construct()` du contrôleur s'exécute), vous pouvez initialiser un objet de service. Cela signifie que vous pouvez accéder aux fonctions de votre service directement dans votre contrôleur.

Maintenant, créons deux classes de service séparées, qui seront utilisées dans le `TaskController`.

Créez manuellement une classe de service `app/Services/ProjectService.php`, qui sera responsable de la logique liée aux projets.

```php
<?php

namespace App\Services;

use App\Models\Project;
use Illuminate\Database\Eloquent\Collection;

class ProjectService
{
    public function getAll(): Collection
    {
        return Project::all();
    }
}
```

La deuxième classe de service sera `app/Services/TaskService.php`, qui sera responsable des manipulations des tâches :

```php
<?php

namespace App\Services;

use App\Models\Task;
use Illuminate\Support\Facades\DB;

class TaskService
{
    public function list(int $projectId)
    {
        return Task::with('project')->where('project_id', $projectId)
            ->orderBy('priority')->get();
    }

    public function getById(int $id)
    {
        return Task::where('id', $id)->with('project')->first();
    }

    public function store($data): void
    {
        $count = Task::where('project_id', $data['project_id'])->count();
        $data['priority'] = $count + 1;

        Task::create($data);
    }

    public function update(int $id, array $data): void
    {
        $task = $this->getById($id);
        if (!$task) { return; }

        $task->update($data);
    }

    public function delete(int $id): void
    {
        $task = $this->getById($id);
        if (!$task) { return; }
        
        $task->delete();

        $tasks = Task::where('project_id', $task->project_id)
            ->where('priority', '>', $task->priority)->get();
        if ($tasks->isEmpty()) {
            return;
        }

        $when_then = "";
        $where_in = "";
        foreach ($tasks as $task) {
            $when_then .= "WHEN ".$task->id
                ." THEN ".($task->priority - 1)." ";
            $where_in .= $task->id.",";
        }

        $table_name = (new Task())->getTable();
        $bulk_update_query = "UPDATE `".$table_name
            ."` SET `priority` = (CASE `id` ".$when_then."END)"
            ." WHERE `id` IN(".substr($where_in, 0, -1).");";

        // il n'y a aucun moyen d'être injecté en SQL ici
        // car toutes les valeurs ne sont pas fournies par l'utilisateur
        DB::update($bulk_update_query);
    }

    public function reorder(int $project_id, int $start, int $end): void
    {
        $items = Task::where('project_id', $project_id)
            ->orderBy('priority')->pluck('priority', 'id')->toArray();

        if ($start > count($items) || $end > count($items)) {
            return;
        }

        $ids = [];
        $priorities = [];
        foreach ($items as $id => $priority) {
            $ids[] = $id;
            $priorities[] = $priority;
        }

        $out_priority = array_splice($priorities, $start - 1, 1);
        array_splice($priorities, $end - 1, 0, $out_priority);

        $when_then = "";
        $where_in = "";
        foreach ($priorities as $out_k => $out_v) {
            $id = $ids[$out_v - 1];
            $when_then .= "WHEN ".$id." THEN ".($out_k + 1)." ";
            $where_in .= $id.",";
        }

        $table_name = (new Task())->getTable();
        $bulk_update_query = "UPDATE `".$table_name
            ."` SET `priority` = (CASE `id` ".$when_then."END)"
            ." WHERE `id` IN(".substr($where_in, 0, -1).")"
            ." AND `deleted_at` IS NULL;"; // suppression douce

        DB::update($bulk_update_query);
    }
}
```

Dans la classe `TaskService` ci-dessus, vous utiliserez les fonctions suivantes dans le `TaskController`.

* **list** : récupère les tâches pour un ID de projet donné, y compris le projet associé, et les trie par _priority_.
* **getById** : récupère une tâche spécifique par son ID, y compris le projet associé.
* **store** : stocke une nouvelle tâche, en calculant la _priority_ en fonction des tâches existantes pour le même projet.
* **update** : met à jour une tâche existante par son ID.
* **delete** : supprime une tâche par son ID et ajuste les priorités des tâches restantes dans le même projet.
* **reorder** : change les priorités des tâches au sein d'un projet, (gère également la suppression douce avec `deleted_at IS NULL`).

## Routes Web et API dans Laravel

Maintenant, vous pouvez ajouter des routes pour tester les méthodes que vous avez déjà écrites. Dans ce projet, nous avons une application sans état sur le frontend qui demande des routes API pour obtenir des données JSON, donc elle suivra les principes RESTful (méthodes GET, POST, PUT, DELETE). Seule la page HTML initiale sera récupérée en tant que page web complète.

Alors maintenant, configurez une route dans `routes/web.php` pour la page initiale monopage :

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TaskController;

Route::group(['prefix' => '/', 'as' => 'tasks.'], function () {
    Route::get('/', [TaskController::class, 'index'])->name('index');
});
```

Configurez les routes API dans `routes/api.php` comme ceci :

```php
<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TaskController;

Route::group(['prefix' => '/tasks', 'as' => 'tasks.'], function () {
    Route::get('/', [TaskController::class, 'list']);
    Route::get('/{id}', [TaskController::class, 'get'])
		->where('id', '[1-9][0-9]*');
    Route::post('/', [TaskController::class, 'store']);
    Route::put('/{id}', [TaskController::class, 'update'])
    	->where('id', '[1-9][0-9]*');
    Route::delete('/{id}', [TaskController::class, 'delete'])
    	->where('id', '[1-9][0-9]*');
    Route::put('/', [TaskController::class, 'reorder']);
});
```

Nous avons toutes les routes API dans le fichier `routes/api.php` au lieu de `routes/web.php` car dans le fichier _web.php_, toutes les routes sont par défaut [protégées par CSRF](https://laravel.com/docs/10.x/routing#csrf-protection). Donc, dans une application sans état, vous n'aurez généralement pas besoin de cela – c'est pourquoi _api.php_ a été inventé dans Laravel.

Comme vous pouvez le voir, il y a un préfixe _"task"_ pour toutes les routes API. Il est facultatif d'avoir un préfixe, mais c'est simplement une bonne pratique. Et pour les routes API spécifiques, il y a des validations regex pour accepter uniquement des nombres naturels comme IDs de projet.

N'oubliez pas de rafraîchir les caches de routes après les modifications ci-dessus. Il est important de se souvenir que Laravel (version 10 dans ce cas) lit les routes à partir du fichier mis en cache `bootstrap/cache/routes-v7.php`, et elles ne seront pas mises à jour automatiquement juste après vos modifications. Il génère simplement un fichier si ce n'est pas encore mis en cache.

Utilisez la commande ci-dessous pour rafraîchir les caches Laravel ainsi que les caches de routes :

```shell
php artisan optimize
```

## Requêtes de Validation dans Laravel

Avant d'écrire les méthodes du contrôleur, vous devrez ajouter quelques fichiers de requêtes de validation. Vous pouvez le faire manuellement ou simplement en utilisant la commande `artisan` :

```shell
php artisan make:request Task/CreateTaskRequest
php artisan make:request Task/ListTasksRequest
php artisan make:request Task/ReorderTasksRequest
php artisan make:request Task/UpdateTaskRequest
```

Après les avoir créés, vous devrez configurer les règles de validation pour chaque requête.

Les règles de validation dans Laravel sont un moyen de décrire comment s'attendre à recevoir les données HTTP entrantes. Si les données correspondent aux règles, alors elles passent la validation – sinon, Laravel retournera un échec.

Laravel fournit un [ensemble de règles](https://laravel.com/docs/10.x/validation#available-validation-rules) que vous pouvez utiliser pour vérifier les données entrantes. Un champ de la requête entrante peut avoir plusieurs règles.

Une façon d'écrire des règles de validation pour un seul champ est de concaténer ces règles par un caractère "|".

Voici les règles de validation pour créer une nouvelle tâche :

```php
return [
    'project_id' => 'required|integer|exists:projects,id',
    'title' => 'required|string|max:255',
    'description' => 'nullable|string',
];
```

Voici la règle de validation pour lister les tâches du projet :

```php
return [
    'project_id' => 'required|integer|exists:projects,id',
];
```

Voici les règles de validation pour le réordonnancement des tâches :

```php
return [
    'project_id' => 'required|integer|exists:projects,id',
    'start' => 'required|integer',
    'end' => 'required|integer|different:start',
];
```

Voici les règles de validation pour mettre à jour une tâche :

```php
return [
    'title' => 'required|string|max:255',
    'description' => 'nullable|string',
];
```

N'oubliez pas de retourner `true` dans la méthode `authorize()` dans toutes les classes de validation :

```php
public function authorize(): bool
{
    return true;
}
```

Cette fonction est généralement conçue pour déterminer si l'utilisateur est autorisé à faire la requête. Comme nous n'utilisons pas l'authentification ainsi que l'autorisation dans l'application, elle doit retourner `true` pour tous les cas.

## Comment écrire un Contrôleur qui utilise des Services

En tant que dernière étape dans la partie backend, il est temps d'écrire les méthodes du contrôleur pour chaque route API, qui utiliseront les fonctions de service.

```php
<?php

namespace App\Http\Controllers;

use App\Http\Requests\Task\CreateTaskRequest;
use App\Http\Requests\Task\ListTasksRequest;
use App\Http\Requests\Task\ReorderTasksRequest;
use App\Http\Requests\Task\UpdateTaskRequest;
use App\Services\ProjectService;
use App\Services\TaskService;
use Illuminate\Http\JsonResponse;

class TaskController extends Controller
{
    protected ?TaskService $taskService = null;

    public function __construct(TaskService $taskService)
    {
        $this->taskService = $taskService;
    }

    public function index()
    {
        $projects = (new ProjectService())->getAll();

        return view('tasks.index', [
            'projects' => $projects,
        ]);
    }

    public function list(ListTasksRequest $request): JsonResponse
    {
        $tasks = $this->taskService->list($request->get('project_id'));

        return response()->json([
            'success' => true,
            'tasks' => $tasks,
            'message' => "Tasks retrieved successfully.",
        ]); // 200
    }

    public function store(CreateTaskRequest $request): JsonResponse
    {
        $this->taskService->store($request->all());

        return response()->json([
            'success' => true,
            'message' => "Task created successfully.",
        ], 201);
    }

    public function get(int $id): JsonResponse
    {
        $task = $this->taskService->getById($id);

        if ($task) {
            return response()->json([
                'success' => true,
                'task' => $task,
                'message' => "Task retrieved successfully.",
            ]); // 200
        } else {
            return response()->json([
                'success' => false,
                'message' => "Task not found!",
            ], 404);
        }
    }

    public function update(UpdateTaskRequest $request, int $id): JsonResponse
    {
        $this->taskService->update($id, $request->all());

        return response()->json([
            'success' => true,
            'message' => "Task updated successfully.",
        ], 201);
    }

    public function delete(int $id): JsonResponse
    {
        $this->taskService->delete($id);

        return response()->json([
            'success' => true,
            'message' => "Task deleted successfully.",
        ], 201);
    }

    public function reorder(ReorderTasksRequest $request): JsonResponse
    {
        $this->taskService->reorder(
            $request->get('project_id'),
            $request->get('start'),
            $request->get('end')
        );

        return response()->json([
            'success' => true,
            'message' => "Tasks reordered successfully.",
        ], 201);
    }
}
```

Comme vous pouvez le voir dans le `TaskController` :

* `TaskService` est injecté dans la méthode de construction en tant qu'argument. Dans le corps du constructeur, une instance de la classe `TaskService` est créée, et la propriété `$taskService` est initialisée. Ainsi, dans les méthodes personnalisées, vous pourrez accéder à ce `$taskService` et à ses fonctions.
* La méthode `index` est destinée à retourner le HTML.
* Toutes les autres méthodes personnalisées (`list`, `store`, `get`, `update`, `delete`, `reorder`) utilisent les fonctions `TaskService` via la propriété `$taskService` déjà initialisée. Ainsi, toute l'implémentation logique va au service, et de cette manière, vous appelez simplement une fonction de service et retournez la réponse.

## Comment Tester les Routes API

À ce stade, vous pouvez tester les routes API en les demandant via Postman ou tout outil similaire. Exécutez simplement (ou réexécutez) le backend :

```shell
php artisan serve
```

Voici la collection [Postman publiée](https://documenter.getpostman.com/view/1747137/2s9YsJArg7) avec toutes les requêtes.

Au lieu d'utiliser Postman, vous pouvez utiliser un outil en ligne de commande tel que _curl_ directement depuis votre terminal.

Voici toutes les commandes d'exemple que vous pouvez exécuter pour tester les routes API :

* Créer une nouvelle tâche pour un projet spécifique :

```shell
curl --location '127.0.0.1:8000/api/tasks?project_id=1' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Title",
    "description": "Description"
}'
```

* Lister les tâches du projet :

```shell
curl --location 'http://127.0.0.1:8000/api/tasks?project_id=1'
```

* Obtenir une tâche par ID :

```shell
curl --location 'http://127.0.0.1:8000/api/tasks/1'
```

* Mettre à jour une tâche par ID :

```shell
curl --location --request PUT 'http://127.0.0.1:8000/api/tasks/11' \
--header 'Content-Type: application/json' \
--data '{
    "title": "Title edited",
    "description": "Description edited"
}'
```

* Réorganiser les tâches du projet :

```shell
curl --location --request PUT 'http://127.0.0.1:8000/api/tasks' \
--header 'Content-Type: application/json' \
--data '{
    "project_id": "1",
    "start": "1",
    "end": "2"
}'
```

* Supprimer une tâche par ID :

```shell
curl --location --request DELETE 'http://127.0.0.1:8000/api/tasks/11'
```

Dans la capture d'écran ci-dessous, il y a un exemple de récupération des tâches du projet par son ID en utilisant la commande _curl_ (en bas à droite) :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-84.png)
_Un exemple d'utilisation de la commande **curl** pour récupérer les tâches existantes de la base de données_

## Le Frontend : Comment installer les Packages

Maintenant, il est temps de passer au frontend. Nous utiliserons TypeScript pour React.js. Après avoir terminé cette partie, vous pourrez intégrer React.js (avec Vite) dans votre application Laravel.

Tout d'abord, assurez-vous d'avoir Node.js version 18 ou supérieure en utilisant cette commande :

```shell
node -v
```

Installez ces packages npm nécessaires :

```shell
npm i react-dom dotenv react-beautiful-dnd react-responsive-modal react-toastify @vitejs/plugin-react
```

* **`react-dom`** est une bibliothèque de l'équipe React pour rendre les composants React dans le DOM (Document Object Model)
* **`dotenv`** est pour charger les variables d'environnement à partir du fichier `.env` dans l'environnement de processus
* **`react-beautiful-dnd`** est une bibliothèque d'Atlassian pour créer des interfaces de glisser-déposer avec des animations
* **`react-responsive-modal`** est pour créer des dialogues modaux simples et réactifs
* **`react-toastify`** est pour afficher des notifications ou des toasts
* **`@vitejs/plugin-react`** est un plugin pour l'outil de build Vite qui permet une intégration transparente de React avec des builds de développement rapides et des builds de production optimisés

Installez les dépendances de développement avec cette commande :

```shell
npm i -D @types/react-dom @types/react-beautiful-dnd
```

* **`@types/react-dom`** est les définitions de type TypeScript pour le package `react-dom`
* **`@types/react-beautiful-dnd`** est les définitions de type TypeScript pour le package `react-beautiful-dnd`

## Comment Configurer Vite.js

Comme Laravel v10 a déjà `vite.config.js`, vous voudrez configurer tout ce qui concerne React là-bas. Ou si vous n'avez toujours pas ce fichier, créez-en un comme ceci :

```javascript
import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import react from '@vitejs/plugin-react';
import 'dotenv/config';

export default defineConfig({
    build: {
        minify: process.env.APP_ENV === 'production' ? 'esbuild' : false,
        cssMinify: process.env.APP_ENV === 'production',
    },
    plugins: [
        laravel({
            input: ['resources/react/app.tsx'],
            refresh: true,
        }),
        react(),
    ],
});
```

Comme vous pouvez le voir dans le fichier de configuration Vite, il y a une référence à `resources/react/app.tsx`, qui sera le point d'entrée pour que Laravel utilise les ressources React.

Pour la page HTML initiale, créez un fichier blade `resources/views/tasks/index.blade.php`, afin que tous les actifs frontend soient injectés là dans le `div` avec l'ID `app` :

```php
<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ config("app.name") }}</title>
    <link rel="shortcut icon" href="{{ asset('favicon.ico') }}" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    @viteReactRefresh
    @vite('resources/react/app.tsx')
</head>
<body>
<div id="app" data-projects="{{ json_encode($projects) }}"></div>
</body>
</html>
```

Comme vous pouvez le voir dans le fichier blade, il y a une variable `$projects` passée depuis le backend. Ce sont les données complètes du projet qui seront utilisées pour filtrer les tâches dans le frontend.

## React.js – Intégration Initiale

Dans cet article, nous aurons simplement une application React.js de base fonctionnant avec Laravel.

Tout d'abord, il est bon de supprimer les ressources inutiles, comme les répertoires `resources/css` et `resources/js` par défaut.

Créez un fichier `resources/react/app.tsx` comme ceci :

```typescript
import ReactDOM from 'react-dom/client';
import Main from "./Main";
import './index.css'

ReactDOM.createRoot(document.getElementById('app')).render(
    <Main />
);

```

Ainsi, le dossier `resources/react` sera le répertoire racine pour toutes les prochaines choses React.

Créez un `index.css` avec un contenu temporaire :

```css
.test-class {
  color: red;
}
```

Créez également un `Main.tsx` avec un contenu temporaire :

```typescript
function Main() {
    return (
        <div>
            <h2 className="test-class">React App</h2>
        </div>
    );
}

export default Main;

```

Pour vérifier le résultat dans le navigateur, assurez-vous que le backend est en cours d'exécution et construisez les actifs via l'outil `vite` :

```shell
npm run build
```

Ou, si vous souhaitez surveiller les changements de fichiers React et construire automatiquement les actifs, vous pouvez garder cette commande en cours d'exécution :

```shell
npm run dev
```

Les deux commandes `npm run` ci-dessus font référence à `vite`, qui construit les actifs. Vous pouvez le voir en vérifiant le fichier `package.json`, le champ _"scripts"_ :

```json
"scripts": {
    "dev": "vite",
    "build": "vite build"
}
```

Maintenant, vous pouvez ouvrir _[http://localhost:8000](http://localhost:8000)_ pour voir la vue rendue initiale :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-85.png)
_Capture d'écran du navigateur_

## Comment Ajouter du CSS

Maintenant, une fois que vous avez configuré Vite et que vous avez intégré React dans votre application Laravel, vous pouvez travailler sur la partie React.

Nous ne passerons pas trop de temps sur les styles, donc vous pouvez coller ce CSS dans votre `index.css` :

```css
body { background-color: whitesmoke; color: rgba(255, 255, 255, 0.7); font-family: "Montserrat", sans-serif; cursor: default; margin: auto 0; }

/* MODAL start */
.modal-content { display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: #fff; padding: 20px; border-radius: 5px; width: 500px; color: #2d3748; }
.modal-header { font-size: 1.5rem; font-weight: 600; margin-bottom: 20px; }
.modal-input-header { font-weight: 600; margin-bottom: 10px; }
.modal-input { width: 100%; height: 30px; border: 1px solid #ccc; border-radius: 5px; padding: 5px; }
.modal-textarea { width: 100%; height: 100px; border: 1px solid #ccc; border-radius: 5px; padding: 5px; margin-bottom: 20px; resize: vertical; }
.modal-actions { display: flex; justify-content: space-between; align-items: center; width: 100%; }
.modal-btn { padding: 10px 20px; border-radius: 5px; cursor: pointer; }
.modal-btn-cancel { background-color: #e53e3e; color: #fff; border: none; }
.modal-btn-cancel:hover { background-color: #c53030; }
.modal-btn-submit { background-color: #2d3748; color: #fff; border: none; }
.modal-btn-submit:hover { background-color: #4a5568; }
.modal-question { font-size: 1.2rem; font-weight: 600; margin-bottom: 20px; }
/* MODAL end */

/* LEFT & RIGHT SIDE start */
.left-side { width: 50%; float: left; }
.right-side { width: 50%; float: left; }
/* LEFT & RIGHT SIDE end */

/* LEFT SIDE start */
.left-side .no-tasks { font-size: 1.2rem; font-weight: 600; margin-bottom: 20px; text-align: center; color: #2d3748; }
.left-side .task-item { padding: 10px; margin: 10px; min-height: 20px; min-width: 200px; color: #2d3748; list-style-type: none; }
.left-side .task-item-content { display: flex; justify-content: space-between; align-items: center; }
.left-side .task-project { display: flex; flex-direction: column; justify-content: center; align-items: center; margin-right: 10px; }
.left-side .task-project-name { font-size: 1.5rem; font-weight: 600; margin-bottom: 5px; }
.left-side .task-time { font-size: 0.8rem; }
.left-side .task-title { font-size: 1.2rem; }
.left-side .task-actions { display: flex; justify-content: space-between; align-items: center; }
.left-side .task-edit-btn { background-color: #2d3748; color: #fff; border: none; border-radius: 5px; padding: 5px 10px; cursor: pointer; margin: 0 5px; }
.left-side .task-edit-btn:hover { background-color: #4a5568; }
.left-side .task-delete-btn { background-color: #e53e3e; color: #fff; border: none; border-radius: 5px; padding: 5px 10px; cursor: pointer; margin: 0 5px; }
.left-side .task-delete-btn:hover { background-color: #c53030; }
/* LEFT SIDE end */

/* RIGHT SIDE start */
.right-side .projects { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.right-side .projects-select { width: 100%; height: 30px; border: 1px solid #ccc; border-radius: 5px; padding: 5px; }
.right-side .no-project-selected { font-size: 1.2rem; font-weight: 600; margin-bottom: 20px; }
.right-side .right-side-wrapper { display: flex; flex-direction: column; justify-content: center; align-items: center; background-color: #fff; padding: 20px; border-radius: 5px; color: #2d3748; }
.right-side .add-task-header { font-size: 1.5rem; font-weight: 600; margin-bottom: 20px; }
.right-side .add-task-input-header { font-weight: 600; margin-bottom: 10px; }
.right-side .add-task-input { width: 100%; height: 30px; border: 1px solid #ccc; border-radius: 5px; padding: 5px; }
.right-side .add-task-textarea { width: 100%; height: 100px; border: 1px solid #ccc; border-radius: 5px; padding: 5px; margin-bottom: 20px; resize: vertical; }
.right-side .add-task-actions { display: flex; justify-content: space-between; align-items: center; width: 100%; }
.right-side .add-task-btn { padding: 10px 20px; border-radius: 5px; cursor: pointer; }
.right-side .add-task-btn-cancel { background-color: #e53e3e; color: #fff; border: none; }
.right-side .add-task-btn-cancel:hover { background-color: #c53030; }
.right-side .add-task-btn-submit { background-color: #2d3748; color: #fff; border: none; }
.right-side .add-task-btn-submit:hover { background-color: #4a5568; }
/* RIGHT SIDE end */
```

Plus tard, vous attacherez le fichier `index.css` dans votre composant principal.

## Un Service pour les requêtes API

Comme vous l'avez fait dans le backend, ici dans le frontend, vous pouvez également déplacer toutes les implémentations logiques dans un fichier différent, afin que votre code soit plus lisible et maintenable. Nous pouvons nommer ce fichier `utils.ts`, car il contiendra les utilitaires dont nous avons besoin.

Avant cela, créez simplement `axiosConfig.ts` pour la configuration globale d'Axios, que vous utiliserez dans `utils.ts`.

```typescript
import axios from 'axios';

export default axios.create({ baseURL: '/api' });
```

En utilisant la configuration ci-dessus, vous pouvez être sûr que toutes les requêtes HTTP auront le préfixe `/api`.

Par exemple, si vous utilisez `axiosConfig.get('/example')`, il enverra une requête GET à `/api/example`. Il s'agit d'une configuration facultative, mais c'est une méthode recommandée pour éviter la répétition de code.

Comme vous aurez quelques cas d'utilisation pour envoyer des requêtes HTTP au serveur, vous pouvez avoir un fichier d'utilitaires séparé pour ces opérations :

* Créer une nouvelle tâche pour un projet
* Mettre à jour une tâche
* Lister les tâches d'un projet
* Supprimer une tâche
* Réorganiser les tâches d'un projet

Voici le fichier `utils.ts` :

```typescript
import axiosConfig from './axiosConfig';
import { toast } from 'react-toastify';

export const getErrorMessage = (error: unknown) => {
    if (error instanceof Error) return error.message;
    return String(error)
}

export const getTasks = async (projectId) => {
    if (!projectId) {
        toast.error("Project is required!");
        return;
    }

    try {
        const response = await axiosConfig.get(`/tasks?project_id=${projectId}`);
        const { success, tasks, message } = response.data;

        if (success) {
            return tasks;
        } else {
            toast.error(message);
            return [];
        }
    } catch (err) {
        toast.error(getErrorMessage(err));
        return [];
    }
}

export const reorderTasks = async (projectId, start, end) => {
    try {
        const response = await axiosConfig.put('/tasks', {
            project_id: projectId,
            start,
            end,
        });
        const { success, message } = response.data;
        
        toast[success ? 'success' : 'error'](message);
    } catch (err) {
        toast.error(getErrorMessage(err));
    }
}

export const editTask = async (task) => {
    if (!task.id) return;
    if (!task.title) {
        toast.error("Title is required!");
        return;
    }

    try {
        const response = await axiosConfig.put(`/tasks/${task.id}`, {
            title: task.title,
            description: task.description,
        });
        const { success, message } = response.data;

        toast[success ? 'success' : 'error'](message);
    } catch (err) {
        toast.error(getErrorMessage(err));
    }
}

export const deleteTask = async (id) => {
    if (!id) {
        toast.error("Invalid task!");
        return;
    }

    try {
        const response = await axiosConfig.delete(`/tasks/${id}`);
        const { success, message } = response.data;

        toast[success ? 'success' : 'error'](message);
    } catch (err) {
        toast.error(getErrorMessage(err));
    }
}

export const createTask = async (task, projectId) => {
    if (!projectId) {
        toast.error("Project is required!");
        return;
    }
    if (!task.title) {
        toast.error("Title is required!");
        return;
    }

    try {
        const response = await axiosConfig.post(`/tasks?project_id=${projectId}`, {
            title: task.title,
            description: task.description,
        });
        const { success, message } = response.data;

        toast[success ? 'success' : 'error'](message);
    } catch (err) {
        toast.error(getErrorMessage(err));
    }
}
```

Dans le fichier ci-dessus, vous trouverez les fonctions suivantes :

* **getErrorMessage** : Retourne le message d'erreur si l'entrée est une instance de Error – sinon, la convertit en chaîne.
* **getTasks** : Récupère les tâches pour un ID de projet donné en utilisant Axios. Affiche un toast d'erreur si l'ID de projet est manquant ou si la requête API est infructueuse.
* **reorderTasks** : Envoie une requête PUT pour réorganiser les tâches au sein d'un projet en fonction des positions de début et de fin. Affiche un toast de succès ou d'erreur en fonction de la réponse de l'API.
* **editTask** : Envoie une requête PUT pour mettre à jour les informations de la tâche. Valide que la tâche a un ID et un titre avant de faire la requête. Affiche un toast de succès ou d'erreur en fonction de la réponse de l'API.
* **deleteTask** : Envoie une requête DELETE pour supprimer une tâche par son ID. Affiche un toast de succès ou d'erreur en fonction de la réponse de l'API.
* **createTask** : Envoie une requête POST pour créer une nouvelle tâche pour un ID de projet donné. Valide que l'ID de projet est présent et que la tâche a un titre avant de faire la requête. Affiche un toast de succès ou d'erreur en fonction de la réponse de l'API.

## Composants React.js

Maintenant, puisque vous avez les utilitaires prêts, dans le dossier `resources/react/components`, vous pouvez créer les composants dont vous avez besoin pour utiliser dans votre `Main.tsx`.

Tout d'abord, créez `SelectProject.tsx`, qui sera responsable du choix du projet actuel :

```typescript
import {getTasks} from "../utils";

function SelectProject({projectId, projects, setProjectId, setTasks}) {
    const selectProject = (e) => {
        const value = e.target.value;
        setProjectId(value);
        if (value === '') {
            setTasks([]);
        } else {
            getTasks(value).then((tasksData) => setTasks(tasksData));
        }
    };

    return (
        <div className="projects">
            <select className="projects-select"
                    value={projectId}
                    onChange={selectProject}>
                <option value="" defaultValue>Choose a project</option>
                {projects.map((project) => (
                    <option key={project.id}
                            value={project.id}>{project.name}</option>
                ))}
            </select>
        </div>
    );
}

export default SelectProject;
```

Le composant `SelectProject` affiche un menu déroulant permettant à l'utilisateur de sélectionner un projet. Lorsqu'un projet est sélectionné, il met à jour l'état avec l'ID du projet sélectionné, récupère les tâches pour ce projet en utilisant la fonction utilitaire `getTasks`, et met à jour l'état avec les tâches récupérées, offrant une interaction dynamique avec la sélection de projet et le chargement des tâches.

Ensuite, créez `TaskList.tsx`, qui sera responsable de l'affichage des tâches du projet et de leurs manipulations par glisser-déposer :

```typescript
import {DragDropContext, Draggable, Droppable} from "react-beautiful-dnd";
import Task from "./Task";
import {reorderTasks} from "../utils";

const getItemStyle = (isDragging, draggableStyle) => ({
    background: isDragging ? 'lightgreen' : 'grey',
    ...draggableStyle,
});

function TaskList({ tasks, setIsModalEditOpen, setModalEditTask, setIsModalDeleteOpen, setModalDeleteTaskId, projectId, setTasks })
{
    const handleDragEnd = (result) => {
        if (!result.destination || result.destination.index === result.source.index) {
            return;
        }

        const items = Array.from(tasks);
        const [reorderedItem] = items.splice(result.source.index, 1);
        items.splice(result.destination.index, 0, reorderedItem);
        reorderTasks(projectId, result.source.index + 1, result.destination.index + 1);

        setTasks(items);
    };

    return (
        <DragDropContext onDragEnd={handleDragEnd}>
            <Droppable droppableId="droppable">
                {(provided) => (
                    <ul {...provided.droppableProps} ref={provided.innerRef}>
                        {tasks.map((task, index) => (
                            <Draggable key={task.id.toString()} draggableId={task.id.toString()} index={index}>
                                {(provided, snapshot) => (
                                    <li ref={provided.innerRef}
                                        {...provided.draggableProps}
                                        {...provided.dragHandleProps}
                                        className="task-item"
                                        style={getItemStyle(snapshot.isDragging, provided.draggableProps.style)}
                                    >
                                        <Task task={task}
                                              setIsModalEditOpen={setIsModalEditOpen}
                                              setModalEditTask={setModalEditTask}
                                              setIsModalDeleteOpen={setIsModalDeleteOpen}
                                              setModalDeleteTaskId={setModalDeleteTaskId}
                                        />
                                    </li>
                                )}
                            </Draggable>
                        ))}
                        {provided.placeholder}
                    </ul>
                )}
            </Droppable>
        </DragDropContext>
    );
}

export default TaskList;
```

Le composant `TaskList` utilise la bibliothèque `react-beautiful-dnd` pour implémenter une liste de tâches glissables. Il affiche une liste de tâches, permettant aux utilisateurs de glisser et déposer des tâches pour les réorganiser, avec une fonctionnalité de glisser-déposer déclenchant une fonction (`handleDragEnd`) qui met à jour l'ordre des tâches à la fois visuellement et dans le backend en utilisant la fonction utilitaire `reorderTasks`.

Maintenant, créez `Task.tsx`, qui sera responsable d'une seule tâche de la liste :

```typescript
function Task({ task, setIsModalEditOpen, setModalEditTask, setIsModalDeleteOpen, setModalDeleteTaskId })
{
    const handleEdit = () => {
        setModalEditTask(task);
        setIsModalEditOpen(true);
    };

    const handleDelete = () => {
        setModalDeleteTaskId(task.id);
        setIsModalDeleteOpen(true);
    };

    return (
        <div className="task-item-content">
            <span className="task-project">
                <span className="task-project-name">
                	{task.project.name}
                </span>
                <span className="task-time">
                	Created {task.created}
                </span>
           	</span>
            <span className="task-title">{task.title}</span>
            <div className="task-actions">
                <button className="task-edit-btn"
                	onClick={handleEdit}>Edit</button>
                <button className="task-delete-btn"
                	onClick={handleDelete}>Delete</button>
            </div>
        </div>
    );
}

export default Task;
```

Le composant `Task` représente un seul élément de tâche. Il affiche les détails de la tâche, y compris le nom du projet, l'heure de création et le titre, et fournit des boutons pour déclencher des actions telles que la modification et la suppression de la tâche, avec les gestionnaires correspondants (`handleEdit` et `handleDelete`).

Ensuite, créez `AddTaskForm.tsx`, qui sera responsable du formulaire de tâche pour ajouter des tâches au projet actuellement sélectionné :

```typescript
import {createTask} from "../utils";

function AddTaskForm({newTask, setNewTask, projectId, reloadTasks })
{
    const clearTaskCreate = () => {
        setNewTask({title: '', description: ''});
    };
    const submitTaskCreate = () => {
        createTask(newTask, projectId).then(() => {
            setNewTask({title: '', description: ''});
            reloadTasks();
        });
    };

    return (
        <>
            <h2 className="add-task-header">Add Task</h2>

            <h3 className="add-task-header">Title</h3>
            <input type="text"
                   className="add-task-input"
                   onChange={(e) => setNewTask({
                   	...newTask,
                    title: e.target.value
                   })}
                   value={newTask.title}
            />
            <h3 className="add-task-input-header">Description</h3>
            <textarea className="add-task-textarea"
                      onChange={(e) => setNewTask({
                      	...newTask,
                        description: e.target.value
                      })}
                      value={newTask.description || ''}
            />
            <div className="add-task-actions">
                <button className="add-task-btn add-task-btn-cancel"
                        onClick={clearTaskCreate}>Clear
                </button>
                <button className="add-task-btn add-task-btn-submit"
                        onClick={submitTaskCreate}>Add</button>
            </div>
        </>
    );
}

export default AddTaskForm;
```

Le composant `AddTaskForm` fournit un formulaire pour ajouter de nouvelles tâches. Il inclut des champs de saisie pour le titre et la description de la tâche, avec des boutons pour effacer le formulaire ou soumettre la création de la tâche, et il utilise la fonction utilitaire `createTask` pour gérer le processus de création de la tâche, déclenchant un rechargement des tâches en cas de succès.

Ensuite, créez `ModalEdit.tsx`, qui sera responsable de la fenêtre modale pour l'édition et la soumission des modifications à une tâche :

```typescript
import {Modal} from "react-responsive-modal";
import React from "react";
import {editTask} from "../utils";

function ModalEdit({
	isModalEditOpen, setIsModalEditOpen, setModalEditTask,
    modalEditTask, reloadTasks
}) {
    const submitTaskEdit = () => {
        setIsModalEditOpen(false);
        editTask(modalEditTask).then(() => {
            reloadTasks();
        });
    };

    return (
        <Modal open={isModalEditOpen} center
        	onClose={() => setIsModalEditOpen(false)}>
            <div className="modal-content">
                <h2 className="modal-header">Edit Task</h2>
                <h3 className="modal-input-header">Title</h3>
                <input type="text" value={modalEditTask.title}
                       className="modal-input"
                       onChange={(e) => setModalEditTask({
                       	...modalEditTask,
                        title: e.target.value
                       })}
                />
                <h3 className="modal-input-header">Description</h3>
                <textarea className="modal-textarea"
                          onChange={(e) => setModalEditTask({
                          	...modalEditTask,
                            description: e.target.value
                          })}
                          value={modalEditTask.description || ''}
                />
                <div className="modal-actions">
                    <button className="modal-btn modal-btn-cancel"
                            onClick={() => setIsModalEditOpen(false)}
                    >Close
                    </button>
                    <button className="modal-btn modal-btn-submit"
                            onClick={submitTaskEdit}
                    >Save</button>
                </div>
            </div>
        </Modal>
    )
}

export default ModalEdit;
```

Le composant `ModalEdit` affiche une modale pour modifier les détails de la tâche. Il inclut des champs de saisie pour modifier le titre et la description de la tâche, et des boutons pour fermer la modale ou enregistrer les modifications, en utilisant la fonction utilitaire `editTask` pour gérer le processus de modification de la tâche et déclencher un rechargement des tâches après une modification réussie.

Ensuite, créez `ModalDelete.tsx`, qui sera responsable de la soumission de la suppression d'une tâche :

```typescript
import {Modal} from "react-responsive-modal";
import {deleteTask} from "../utils";

function ModalDelete({
	isModalDeleteOpen, setIsModalDeleteOpen,
    modalDeleteTaskId, reloadTasks
}) {
    const submitTaskDelete = () => {
        setIsModalDeleteOpen(false);
        deleteTask(modalDeleteTaskId).then(() => {
            reloadTasks();
        });
    };

    return (
        <Modal open={isModalDeleteOpen} onClose={() => setIsModalDeleteOpen(false)} center>
            <div className="modal-content">
                <h2 className="modal-header">Delete Task</h2>
                <p className="modal-question">
                	Are you sure you want to delete this task?
                </p>
                <div className="modal-actions">
                    <button className="modal-btn modal-btn-cancel"
                            onClick={() => setIsModalDeleteOpen(false)}
                    >Cancel</button>
                    <button className="modal-btn modal-btn-submit"
                            onClick={submitTaskDelete}
                    >Yes</button>
                </div>
            </div>
        </Modal>
    );
}

export default ModalDelete;
```

Le composant `ModalDelete` affiche une modale pour confirmer la suppression d'une tâche. Il fournit des options pour annuler la suppression ou procéder à la suppression de la tâche, en utilisant la fonction utilitaire `deleteTask` et en déclenchant un rechargement des tâches après une suppression réussie.

Et enfin, configurez le `Main.tsx` en utilisant les composants définis ci-dessus.

```typescript
import { useState } from 'react';
import {getTasks} from "./utils";
import "react-responsive-modal/styles.css";
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import ModalEdit from "./components/ModalEdit";
import ModalDelete from "./components/ModalDelete";
import TaskList from "./components/TaskList";
import SelectProject from "./components/SelectProject";
import AddTaskForm from "./components/AddTaskForm";

function Main () {
    const [projectId, setProjectId] = useState('');
    const projectsData = document.getElementById('app').getAttribute('data-projects');
    const projects = JSON.parse(projectsData);
    const [tasks, setTasks] = useState([]);
    const [isModalEditOpen, setIsModalEditOpen] = useState(false);
    const [modalEditTask, setModalEditTask] = useState({id: '', title: '', description: ''});
    const [isModalDeleteOpen, setIsModalDeleteOpen] = useState(false);
    const [modalDeleteTaskId, setModalDeleteTaskId] = useState('');
    const [newTask, setNewTask] = useState({title: '', description: ''});

    const reloadTasks = () => {
        getTasks(projectId).then((tasksData) => setTasks(tasksData));
    };

    return (
        <div>
            <ToastContainer autoClose={2000} />
            <ModalEdit isModalEditOpen={isModalEditOpen}
                       setIsModalEditOpen={setIsModalEditOpen}
                       modalEditTask={modalEditTask}
                       setModalEditTask={setModalEditTask}
                       reloadTasks={reloadTasks}
            />
            <ModalDelete isModalDeleteOpen={isModalDeleteOpen}
                         setIsModalDeleteOpen={setIsModalDeleteOpen}
                         modalDeleteTaskId={modalDeleteTaskId}
                         reloadTasks={reloadTasks}
            />
            <div className="left-side">
                {tasks.length > 0 ? (
                    <TaskList tasks={tasks}
                              setIsModalEditOpen={setIsModalEditOpen}
                              setModalEditTask={setModalEditTask}
                              setIsModalDeleteOpen={setIsModalDeleteOpen}
                              setModalDeleteTaskId={setModalDeleteTaskId}
                              projectId={projectId}
                              setTasks={setTasks}
                    />
                ) : (
                    <div className="no-tasks">
                        {projectId === '' ? (
                            <p>Choose a project to see its tasks.</p>
                        ) : (
                            <p>This project has no tasks.</p>
                        )}
                    </div>
                )}
            </div>
            <div className="right-side">
                <div className="right-side-wrapper">
                    <SelectProject projectId={projectId}
                                   projects={projects}
                                   setProjectId={setProjectId}
                                   setTasks={setTasks}
                    />
                    {projectId === '' ? (
                        <div className="no-project-selected">
                            <p>Please select a project.</p>
                        </div>
                    ) : (
                        <AddTaskForm newTask={newTask}
                                     setNewTask={setNewTask}
                                     projectId={projectId}
                                     reloadTasks={reloadTasks}
                        />
                    )}
                </div>
            </div>
        </div>
    );
}

export default Main;
```

Le composant `Main` est un composant central qui gère les fonctionnalités liées aux projets et aux tâches. Il inclut des modales pour l'édition et la suppression des tâches, une liste de tâches avec des mises à jour dynamiques, un menu déroulant de sélection de projet et un formulaire pour ajouter de nouvelles tâches, en utilisant la gestion d'état et les fonctions utilitaires pour une interaction fluide avec l'utilisateur.

## Résultats Finaux

À ce stade, tous les composants sont prêts à interagir les uns avec les autres. Vous pouvez donc construire les actifs frontend et exécuter le serveur :

```shell
npm run build && php artisan serve
```

En visitant `http://127.0.0.1:8000`, vous obtiendrez ce type de résultat :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/tasklist.gif)
_GIF généré à partir d'un projet local fonctionnel_

**C'est tout !**

Maintenant, vous pouvez facilement intégrer React.js dans votre application Laravel sans utiliser d'outils Laravel supplémentaires (comme Inertia). Et en résultat, vous pouvez continuer à maintenir votre application Laravel pour construire des APIs plus évolutives avec son authentification et autres fonctionnalités.

Ainsi, cela peut être simplement une application exemple pour votre prochain projet full-stack Laravel et React.js.

## Conclusion

Avec cet article, vous avez construit une application Tasklist full-stack monopage en utilisant React.js (avec TypeScript) avec Vite.js comme technologies frontend, Laravel comme framework backend, et le package `react-beautiful-dnd` pour avoir des éléments glissables. Maintenant, vous savez comment intégrer manuellement React.js dans votre application Laravel et la maintenir.

Vous pouvez trouver le code complet du projet ici sur mon [**GitHub** 2b50](https://github.com/boolfalse/laravel-react-tasklist), où je publie activement une grande partie de mon travail sur diverses technologies modernes. Pour plus d'informations, vous pouvez visiter mon site web : [**boolfalse.com**](https://boolfalse.com/)

N'hésitez pas à partager cet article. 😇