---
title: Comment créer des applications Web avec Nuxt et Laravel
subtitle: ''
author: Abdulrahman Yusuf
co_authors: []
series: null
date: '2024-02-07T10:59:00.000Z'
originalURL: https://freecodecamp.org/news/build-web-apps-with-nuxt-and-laravel
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-pixabay-270557.jpg
tags:
- name: Laravel
  slug: laravel
- name: Nuxt.js
  slug: nuxtjs
- name: Web Applications
  slug: web-applications
seo_title: Comment créer des applications Web avec Nuxt et Laravel
seo_desc: "The Laravel framework is one of the most widely used technologies in the\
  \ web development ecosystem. It's relatively straightforward, and it's easy to use\
  \ for building websites. \nLaravel is built upon PHP, a popular web programming\
  \ language that’s use..."
---

Le framework Laravel est l'une des technologies les plus utilisées dans l'écosystème du développement web. Il est relativement simple et facile à utiliser pour créer des sites web. 

Laravel est construit sur PHP, un langage de programmation web populaire utilisé dans plus de 75 % des sites web sur le web. Savoir utiliser un framework comme Laravel peut donc vous aider à devenir un développeur recherché – et cela rend également la création de sites web et d'applications plus fluide. 

Nuxt est un framework Vue.js utilisé pour créer des applications web riches et interactives. Il vous permet de choisir entre différents modes de rendu en fonction des exigences de l'application que vous souhaitez créer. Vous pouvez choisir entre la création d'une application entièrement rendue côté serveur ou côté client. Nuxt offre également un mélange des deux modes de rendu, rendant les applications beaucoup plus puissantes, efficaces et interactives.

Dans cet article, vous apprendrez à créer des applications full-stack en utilisant Nuxt et Laravel en construisant une application de bibliothèque de livres. L'application comprendra une API de bibliothèque que nous créerons en utilisant Laravel et un frontend utilisant Nuxt. 

Nous parlerons de :

* Installation et configuration de Laravel
* Création de modèles de base de données
* Migrations
* Contrôleurs
* Tests d'API
* Validations de formulaires
* Récupération de données dans Nuxt

Et plus encore. Préparez-vous, et plongeons.

## **Table des matières :**

- [Prérequis](#heading-prerequis)
- [Comment installer Laravel sur votre machine](#heading-comment-installer-laravel-sur-votre-machine)
- [Comment construire l'API de la bibliothèque de livres](#heading-comment-construire-lapi-de-la-bibliotheque-de-livres)
  - [Configuration de notre base de données](#configuration-de-notre-base-de-donnees)
  - [Création de notre modèle de livre](#creation-de-notre-modele-de-livre)
  - [Création de notre contrôleur de livre](#creation-de-notre-controleur-de-livre)
  - [Définition de nos routes API](#definition-de-nos-routes-api)
  - [Test de notre API](#test-de-notre-api)
    - [Création d'un nouveau livre](#heading-creation-dun-nouveau-livre-1)
    - [Obtention de notre liste de livres](#obtention-de-notre-liste-de-livres)
    - [Édition de notre livre](#edition-de-notre-livre)
  
- [Comment construire le frontend Nuxt](#heading-comment-construire-le-frontend-nuxt)
- [Comment intégrer l'API Laravel dans le frontend](#heading-comment-integrer-lapi-laravel-dans-le-frontend)
  - [Obtention de tous les livres de notre bibliothèque](#obtention-de-tous-les-livres-de-notre-bibliotheque)
  - [Création d'un nouveau livre](#heading-creation-dun-nouveau-livre-1)
  - [Édition d'un livre](#heading-edition-dun-livre)
  - [Suppression d'un livre](#heading-suppression-dun-livre)
- [Conclusion](#heading-conclusion)
- [Ressources](#heading-ressources)

## **Prérequis**

1. [PHP](https://www.php.net) et [Composer](https://getcomposer.org) sont installés sur votre machine locale.
2. [Node.js](https://nodejs.org/) est installé sur votre machine locale.
3. [yarn](https://yarnpkg.com/) ou [npm](https://www.npmjs.com) installé sur votre machine locale (npm est préinstallé avec Node).
4. Un éditeur de texte installé, comme [VSCode](https://code.visualstudio.com).
5. Connaissances de base en HTML, CSS, JavaScript et terminal.
6. Connaissances de base en PHP, Vue.js et TypeScript.

## **Comment installer Laravel sur votre machine**

Pour commencer l'installation de Laravel, ouvrez votre terminal et initialisez un nouveau projet Laravel avec la commande suivante : 

```bash
composer create-project laravel/laravel library-api && cd library-api && code .

```

Cette commande crée un nouveau projet Laravel dans votre répertoire, se déplace dedans avec `cd`, et ouvre VSCode avec la commande `code .`. (Si vous utilisez un autre éditeur, vous pouvez supprimer cette commande et ouvrir le répertoire manuellement).

Pour tester votre serveur Laravel et vous assurer que tout fonctionne, testons le serveur en utilisant la commande `php artisan serve` dans le terminal. Cela devrait rendre votre API disponible sur le port 8000 et accessible dans votre navigateur.

![Image](https://lh7-us.googleusercontent.com/Wd1K8FLTnBwThyGwMl8lYeTmpO2886t4IN2lJ6Nv2tShwvw0HGxNWhl3cneeAEVVdVL_Gvf9sB0feecPHqpRpXYbPz-dBRPPAnBxJAabWyMySW-FqSwJkUi1_bTOX7fLqo1luWJIRi1iEPlbSkVxh3U)
_Application de démarrage Laravel_

## **Comment construire l'API de la bibliothèque de livres**

Nous allons créer un endpoint CRUD simple pour notre bibliothèque de livres, c'est-à-dire que l'API doit être capable de réaliser les actions suivantes :

* Créer de nouvelles entrées de livres
* Obtenir une liste de toutes les entrées de livres dans la base de données
* Modifier les entrées de livres ajoutées précédemment
* Supprimer les entrées de livres de la base de données

### Configuration de la base de données

Laravel propose une variété de bases de données que vous pouvez utiliser pendant le développement. Par défaut, il crée automatiquement une configuration pour MySQL. Mais pour simplifier, nous utiliserons une base de données [SQLite](https://www.sqlite.org/index.html) dans ce tutoriel. 

Ouvrez le fichier `.env` dans votre répertoire racine, changez la valeur `DB_CONNECTION` de `mysql` à `sqlite`, et commentez les autres configurations de la base de données comme vous pouvez le voir ci-dessous :

![Image](https://lh7-us.googleusercontent.com/NoxsSV5jfFxxzAsKDX04xAfWzUAESGajpJnam3zTA3LpBIil9-esqfxk4I1CJXjlK_jyjEk3twDTGu_Bi_Efw1DUXaU0yUcdCFcdKECCZ-V-hT4Y_03YKfeQCz8JQ5MVSznXcC3dYei8vBb9wTCo1_c)
_Variables d'environnement (disponibles dans le fichier .env)_

Laravel crée automatiquement la base de données SQLite lorsque la commande de migration est exécutée. Nous le ferons dans un instant après avoir créé nos modèles de base de données.

### **Création du modèle de livre**

Lorsque vous construisez des API backend, un modèle sert de modèle utilisé pour configurer vos tables de base de données. Il contient des instructions de haut niveau sur la manière dont les tables et les colonnes doivent être créées. 

Dans Laravel, vous pouvez utiliser la commande suivante pour créer un modèle `Book` :

```bash
php artisan make:model Book -m
```

Cela crée votre modèle Book dans le répertoire `app/models` et crée également un nouveau fichier de migration pour vous dans le répertoire `database/migrations`.

Accédez au répertoire des migrations et ouvrez le fichier de migration nouvellement créé. Il devrait être au format `current_date_create_books_table.php` comme vous pouvez le voir ci-dessous :

![Image](https://lh7-us.googleusercontent.com/zW84PQRgiGuLMX9yvmCJ_NvDS4xZfraKtxh7g0Du6rhOoqSpuXGlWnxkCSlTT9yhqT3c6N_jfPAsiuKakLG_MULYgYD6_Qe-Eycxo4hxaozonEVzbjVe64ddSu2FOpdOGMexms1jPuSZc43HB-N0-hY)
_Migrations par défaut_

Modifiez la fonction `up` et ajoutez le contenu suivant :

```php
$table->string('title');
$table->string('author');
$table->string('isbn');
$table->date('published_date');
$table->text('cover_image')->nullable();
$table->foreignIdFor(User::class);
```

Votre fichier de migration devrait maintenant ressembler à ceci :

![Image](https://lh7-us.googleusercontent.com/sgSaSbourHadcXleC2Jxn8DHAkulytaRIQfcAZC7ZUPvNTJJITJDr9rDEeYSNf-mNjJxxW285Kz1C5MQlFWBNlSMG7Gk0VEIShz8-AtaA6hRHChRuYYkrYQkIl9IwZ_I0-tO7cXMFd8f3OLen-bAm9o)
_Migrations mises à jour_

En résumé, vous avez ajouté de nouveaux champs à créer pour les tables de livres. `Title`, `author` et `isbn` ont tous un type de données string, tandis que `published_date` et `cover_image` ont des types de données date et text, respectivement. 

Vous avez également rendu `cover_image` nullable, c'est-à-dire que le champ peut être omis lors de la création d'une nouvelle entrée de livre. 

Enfin, vous avez importé la classe `User` et en avez fait une [clé étrangère](https://www.educative.io/blog/what-is-foreign-key-database) de votre table Book, créant une relation plusieurs-à-un avec la table User.

Maintenant, créons vos tables en exécutant le fichier de migration avec la commande suivante :

```php
php artisan migrate
```

Vous devriez obtenir une invite dans le terminal vous demandant si vous souhaitez créer votre base de données SQLite avant les migrations. Sélectionnez oui et appuyez sur Entrée pour procéder aux migrations.

Une fois la migration exécutée avec succès, accédez au modèle Book et collez le code suivant :

```php
 /**
* Les attributs qui sont assignables en masse.
*
* @var array<int, string>
*/

protected $fillable = [
    'user_id',
    'title',
    'author',
    'isbn',
    'published_date',
    'cover_image'
];
```

Cela permettra l'assignation en masse lors du passage de données dans le modèle (passage des données en bloc au lieu de manière individuelle). Votre modèle Book devrait maintenant ressembler à ceci :

![Image](https://lh7-us.googleusercontent.com/zjYcbtyiQXKFRJubxnDuL5M6PRyEI5u5PaHGHUAfYgju5A8lQqOJAxRSLdsaIkg0bjFCXOOUTBGHlQXuJhpuEfOW5K6XbPDl2aEQoUyNvjs-p-m5TfRQhF2dlnwnZKHDb0EXsR6JneIGIXCw0ol1plI)
_Modèle Book mis à jour_

### **Création du contrôleur de livre**

Le contrôleur est responsable du logement de la logique métier pour toute API créée. La logique d'implémentation pour la manière dont nous voulons effectuer des opérations CRUD avec l'API de la bibliothèque résidera ici. 

Laravel fournit également une commande pour faciliter cela pour les développeurs. Collez la commande suivante dans votre terminal pour créer notre contrôleur de livre :

```php
php artisan make:controller BookController
```

Cela devrait être accessible à `app\Http\Controllers\BookController.php`. Remplacez le contenu de votre classe BookController par l'extrait de code suivant :

```php
<?php

namespace App\Http\Controllers;

use App\Models\Book;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Storage;


class BookController extends Controller
{
    public function store(Request $request)
    {
        $data = $request->validate([
            'title' => 'required|string',
            'author' => 'required|string',
            'isbn' => 'required|string|unique:books',
            'published_date' => 'required|string',
            'cover_image' => 'nullable|image|max:2048',
        ]);

        try {
            $published_date = Carbon::parse($data['published_date'])->toDateString();
            $data['published_date'] = $published_date;
            $data['user_id'] = 1; // En supposant que l'id de l'utilisateur est 1 
        } catch (\Exception $e) {
            return response()->json(['Error' => 'Bad Request'], 400);
        }

        $book = new Book($data);

        if ($request->hasFile('cover_image')) {
            $coverImage = $request->file('cover_image');
            $coverImageName = time() . '.' . $coverImage->getClientOriginalExtension();
            $coverImage->move(public_path('images'), $coverImageName);
            $book->cover_image = $coverImageName;
        }

        $book->save();

        return response()->json(['message' => 'Book added successfully'], 201);
    }

    public function index()
    {
        $books = Book::all();

        return response()->json(['books' => $books], 200);
    }

    public function update(Request $request, $id)
    {
        $book = Book::findOrFail($id);
        $data = $request->all();

        try {
            $published_date = Carbon::parse($data['published_date'])->toDateString();
            $data['published_date'] = $published_date;
            $data['user_id'] = $book->user_id;
        } catch (\Throwable $th) {
            Log::error('Error ', $th);
            return response()->json(['Error' => 'Bad Request'], 400);
        }

        $book->update($data);

        if ($request->hasFile('cover_image')) {
            // Supprimer l'ancienne image de couverture si elle existe
            if ($book->cover_image) {
                Storage::delete('public/images/' . $book->cover_image);
            }

            $coverImage = $request->file('cover_image');
            $coverImageName = time() . '.' . $coverImage->getClientOriginalExtension();
            $coverImage->storeAs('public/images', $coverImageName);
            $book->cover_image = $coverImageName;
            $book->save();
        }

        return response()->json(['message' => 'Book updated successfully'], 200);
    }

    public function destroy($id)
    {
        $book = Book::findOrFail($id);

        // Supprimer l'image de couverture si elle existe
        if ($book->cover_image) {
            Storage::delete('public/images/' . $book->cover_image);
        }

        $book->delete();

        return response()->json(['message' => 'Book deleted successfully'], 200);
    }
}

```

### **Définition des routes API**

Le routage est l'une des parties les plus importantes de la création d'une API. Les routes servent de points d'accès par lesquels les développeurs, les clients ou tout autre service peuvent accéder à une API. 

Le routeur Laravel vous permet d'enregistrer des routes qui correspondent à n'importe quel verbe HTTP demandé.

```php
Route::get($uri, $callback);
Route::post($uri, $callback);
Route::put($uri, $callback);
Route::patch($uri, $callback);
Route::delete($uri, $callback);
Route::options($uri, $callback);
```

Accédez au fichier `routes/api.php` et créez les routes suivantes pour votre API :

```php
Route::post('/books', [BookController::class, 'store']);
Route::get('/books', [BookController::class, 'index']);
Route::put('/books/{id}', [BookController::class, 'update']);
Route::delete('/books/{id}', [BookController::class, 'destroy']);
```

### **Test de l'API**

Maintenant, il est temps de tester votre API et de vous assurer que tous vos endpoints sont accessibles et fonctionnent comme prévu. 

Exécutez le serveur Laravel avec la commande suivante :

```php
php artisan serve
```

Vous pouvez tester l'API en utilisant n'importe quel client API de votre choix. Nous avons plusieurs options populaires parmi lesquelles choisir – [Postman](https://www.postman.com), [Insomnia](https://insomnia.rest), [Thunder Client](https://www.thunderclient.com), etc. J'utiliserai Thunder Client ici.

Nous testerons toutes les opérations CRUD dans votre client API en confirmant si tous vos objectifs pour votre API sont atteints.

### Création d'un nouveau livre

![Image](https://lh7-us.googleusercontent.com/pUy0u6hCbOEihAsLhLTtSS6p0l3a42PIKHceWRnq5m4-0MJHwwG2r4mL5Y8MCr_EG3g7AuvvmW6nEx9SZ4-GtHTQNFO5Som8f4PYBPjntJSTNJXzrV0sbjL9RYRGhILUWHo6eWFb9tX82XWmrwH70yI)
_Endpoint de création de livre_

### Obtention d'une liste de livres

![Image](https://lh7-us.googleusercontent.com/9QNUQRrxFzime9Dsl9bKuh82o0XzD6AY8fUaAmQB_mHP0-pyqviLOVPfesLUsINl9n54tYqbjPNOWYEkJwfoXkaVuREbjGhqhghYI5ifi8e7TTQrNSIIm4jU3rM_8akLtc4so-4AzeegJicMpL8IGZw)
_Endpoint d'obtention de livres_

### Édition d'un livre

![Image](https://lh7-us.googleusercontent.com/ZTC04dUEXPF2BdxNH-l9RbfzjhkMqO338pQSHjcoEl_hfa3EZbRUtWS2Stgk7slAlwjXpl1_ypvALbuQX3AvLaDPO0gj2rzh5BpqO-uwK6yjSehztm1wJnrjWLzKM0-asFqOU2wMOTp1xffqVroewec)
_Endpoint d'édition de livre_

## Comment construire le frontend Nuxt

La configuration d'une nouvelle application Nuxt est aussi simple que d'exécuter la commande suivante :

```bash
npx nuxi@latest init nuxt-library-frontend
```

Ouvrez le projet nouvellement créé une fois que vous avez terminé l'installation de toutes les dépendances et démarrez le serveur de développement avec cette commande :

```bash
npm run dev
```

Votre application Nuxt devrait maintenant être accessible sur le port 3000 :

![Image](https://lh7-us.googleusercontent.com/ZOV-VAcrLLTW7i6SAmFNh5q8hRcxhY05wC4vZUXbxTwgR5tTsKop-An1SYlFdXEiquu1zCz1tx5TTwrY9WlDEPuiuNpHh4vDsVWwlUVGvZFWljmsTGgRYST3478Pk79jNcNeXJoGa7lQcAdbTx3YitI)
_Page de démarrage Nuxt_

Voici à quoi votre frontend devrait ressembler à la fin du tutoriel :

![Image](https://lh7-us.googleusercontent.com/FbnijAJw1D-VJTnT8VNPQBfl694-fW2PhYTqoEokTMxceEnsN5Oa-mBTmSAcoeU8xcqRFyDceWTQjElj43oidAg2xtW2KWSVamDbL0kmVDuCZktQc1mER5pbCbGkshNsYm0WJKqbgQy8GVymZ8-Bo5I)
_Exemple de notre application terminée_

J'ai créé un [code de base](https://github.com/Young-Einstein10/laravel-nuxt-app) pour aider à la configuration du frontend Nuxt. Cela nous permettra de nous concentrer sur la logique d'implémentation pour consommer l'API Laravel plutôt que de passer du temps à configurer les choses et à les styliser. 

Pour information, j'ai créé les composants d'interface utilisateur pour l'application en utilisant [shadcn-vue](https://www.shadcn-vue.com). Il s'agit d'une collection incroyable de composants d'interface utilisateur accessibles et réutilisables que vous pouvez personnaliser selon vos goûts. Consultez les étapes d'[installation](https://www.shadcn-vue.com/docs/installation/nuxt.html) pour plus de détails sur la facilité de configuration pour l'application Nuxt. 

Il inclut également une installation de la bibliothèque d'utilitaires [Tailwind CSS](https://tailwindcss.com/) que nous utiliserons pour le style dans ce tutoriel.

Clonez la configuration de base depuis le dépôt GitHub [ici](https://github.com/Young-Einstein10/laravel-nuxt-app) pour que nous puissions commencer.

Accédez à `pages/index.vue` et remplacez le contenu de la page d'accueil par ceci :

```vue
<template>
 <main class="bg-white p-10 min-h-screen">
   <div class="max-w-4xl mx-auto">
     <header class="flex justify-between items-center mb-20">
       <h1 class="font-semibold text-4xl">My Library</h1>
       <Button>Add New Book</Button>
     </header>


     <div v-if="isLoading">
       <p class="italic text-2xl font-medium text-center">Loading...</p>
     </div>
     <div class="mt-8">
       <div class="flex flex-col gap-8">
         <div class="flex gap-4" v-for="book in books">
           <div
             v-if="book.cover_image"
             class="rounded-lg w-32 h-44 flex items-center justify-center"
           >
             <NuxtImg
               :src="`${API_BASE_URL}/images/${book.cover_image}`"
               :alt="book.title"
               class="w-full h-auto"
             />
           </div>
           <div v-else class="bg-slate-300 rounded-lg w-32 h-44"></div>
           <div class="flex items-center justify-between flex-1">
             <div>
               <h3 class="font-medium text-xl mb-4">{{ book.title }}</h3>
               <p class="mb-2">
                 <span>by:</span>
                 <span class="italic"> {{ book.author }} </span>
               </p>
               <p>
                 <span>Published:</span>
                 {{ book.published_date }}
               </p>
             </div>
             <div class="actions flex gap-4">
               <Button>Edit</Button>
               <Button variant="destructive"> Delete </Button>
             </div>
           </div>
         </div>
       </div>
     </div>
   </div>
 </main>
</template>


<script lang="ts" setup>
import { API_BASE_URL } from "@/utils/constants";
import type { BookProps } from "@/utils/types";


const isLoading = ref(false);
const books = ref<BookProps[]>([]);
</script>
```

Nous devons créer un nouveau dossier appelé `utils` dans votre projet racine qui contiendra deux fichiers : `constants.ts` et `types.ts`. Collez l'extrait de code suivant dans votre fichier `constants.ts` :

```typescript
export const API_BASE_URL = "http://localhost:8000";
```

Et le suivant dans votre `types.ts` :

```typescript
export interface BookProps {
     id?: number;
     title: string;
     author: string;
     isbn: string;
     published_date: string;
     cover_image?: string;
     user_id?: number;
     created_at?: string;
     updated_at?: string;
}
```

Enregistrez le fichier `pages/index.vue`. Vous devriez pouvoir voir ce résultat dans votre navigateur :

![Image](https://lh7-us.googleusercontent.com/1M7J0_i-u7rUaHr6vX5na1sReyIh1e1s5VGFh1mZteE0j7sXM5lFUWBmPXZNDbLuobYM9nkJtodCvUTZig22KnJS471YHdOowjXmlmMBwkBuYpQ0J10rgi_xmJt8Vyfm_tHqsTEh6wdtqLx1q1X7KDc)
_Échafaudage du frontend de la bibliothèque avec Nuxt_

Maintenant, nous devons créer un tiroir latéral et une boîte de dialogue pour ajouter de nouveaux livres et supprimer les livres ajoutés de la base de données, respectivement. 

Créez un nouveau fichier appelé `BookDrawer.vue` dans la racine des composants et ajoutez le code suivant :

```vue
<script setup lang="ts">
import type { BookProps } from "@/utils/types";


type PickedProps = "title" | "author" | "isbn" | "published_date";
interface CustomBookProps extends Pick<BookProps, PickedProps> {
 cover_image?: string;
}


const props = defineProps<{ open: boolean; book?: BookProps }>();
const emit = defineEmits(["update:open", "refresh-data"]);


const isSubmitting = ref(false);
let form = reactive<CustomBookProps>({
 title: "",
 author: "",
 isbn: "",
 published_date: "",
 cover_image: undefined,
});


const onFileChange = async (e: any) => {
 form.cover_image = e.target.files[0];
};


const onSubmit = async () => {};


const closeDrawer = (openState: boolean) => emit("update:open", openState);
</script>


<template>
 <Sheet :open="open" @update:open="closeDrawer">
   <SheetContent class="w-full bg-white">
     <SheetHeader>
       <SheetTitle>
         <template v-if="book"> Edit Book </template>
         <template v-else>Add New Book</template>
       </SheetTitle>
       <SheetDescription>
         Make changes to your profile here. Click save when you're done.
       </SheetDescription>
     </SheetHeader>
     <div class="grid gap-4 py-4">
       <div class="grid grid-cols-4 items-center gap-4">
         <Label for="bookTitle" class="text-right"> Book Title </Label>
         <Input
           v-model:model-value="form.title"
           type="text"
           id="bookTitle"
           class="col-span-3"
           required
         />
       </div>
       <div class="grid grid-cols-4 items-center gap-4">
         <Label for="author" class="text-right"> Author </Label>
         <Input
           v-model:model-value="form.author"
           type="text"
           id="author"
           class="col-span-3"
           required
         />
       </div>
       <div class="grid grid-cols-4 items-center gap-4">
         <Label for="isbn" class="text-right"> ISBN </Label>
         <Input
           v-model:model-value="form.isbn"
           type="text"
           id="isbn"
           class="col-span-3"
           required
         />
       </div>
       <div class="grid grid-cols-4 items-center gap-4">
         <Label for="published_date" class="text-right">
           Published Date
         </Label>
         <Input
           v-model:model-value="form.published_date"
           type="date"
           id="published_date"
           class="col-span-3"
           required
         />
       </div>
       <div class="grid grid-cols-4 items-center gap-4">
         <Label for="cover_image" class="text-right"> Book Cover </Label>


         <Input
           type="file"
           @change="onFileChange"
           id="cover_image"
           class="col-span-3"
           required
         />
       </div>
     </div>
     <SheetFooter>
       <Button type="submit" @click="onSubmit">
         <template v-if="isSubmitting">Saving...</template>
         <template v-else> Save changes </template>
       </Button>
     </SheetFooter>
   </SheetContent>
 </Sheet>
</template>
```

Créez un autre fichier appelé `DeleteBookDrawer.vue` et ajoutez le contenu de code suivant : 

```vue
<script lang="ts" setup>
const emit = defineEmits(["refresh-data", "update:open"]);
const props = defineProps<{ open: boolean; book?: BookProps }>();
</script>


<template>
 <AlertDialog
   :open="open"
   @update:open="(openState) => $emit('update:open', openState)"
 >
   <AlertDialogContent>
     <AlertDialogHeader>
       <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
       <AlertDialogDescription>
         This action cannot be undone. This will permanently delete your book
         and remove your data from the server.
       </AlertDialogDescription>
     </AlertDialogHeader>
     <AlertDialogFooter>
       <AlertDialogCancel @click="$emit('update:open', false)"
         >Cancel</AlertDialogCancel
       >
       <AlertDialogAction>Continue</AlertDialogAction>
     </AlertDialogFooter>
   </AlertDialogContent>
 </AlertDialog>
</template>

```

Importez les fichiers nouvellement créés dans votre page d'accueil comme vous pouvez le voir ci-dessous :

```vue
<template>
 <main class="bg-white p-10 min-h-screen">
	...
    
   <BookDrawerDialog
     v-if="isBookDrawerOpen"
     :open="isBookDrawerOpen"
     @update:open="(open: boolean) => isBookDrawerOpen = open"
     :book="currentBook"
     @refresh-data="fetchBooks"
   />
   <DeleteBookDialog
     v-if="isDeleteBookDialogOpen"
     :open="isDeleteBookDialogOpen"
     @update:open="(open: boolean) => isDeleteBookDialogOpen = open"
     :book="currentBook"
     @refresh-data="fetchBooks"
   />
 </main>
</template>

```

Maintenant, nous devons créer un système pour ouvrir et fermer le tiroir et la boîte de dialogue, respectivement. Nous allons créer un [ref](https://vuejs.org/guide/essentials/reactivity-fundamentals.html#ref) pour suivre l'état ouvert/fermé pour les composants de tiroir et de boîte de dialogue dans votre page d'accueil. Collez le contenu de code suivant dans la section script pour activer cela :

```vue
<script lang="ts" setup>

...

const currentBook = ref<BookProps>();


const isBookDrawerOpen = ref(false);
const isDeleteBookDialogOpen = ref(false);


const toggleAddBookDrawer = () => {
 isBookDrawerOpen.value = !isBookDrawerOpen.value;
};


const toggleEditBookDrawer = (book: BookProps) => {
 currentBook.value = book;
 isBookDrawerOpen.value = !isBookDrawerOpen.value;
};


const toggleDeleteDialog = (book: BookProps) => {
 currentBook.value = book;
 isDeleteBookDialogOpen.value = !isDeleteBookDialogOpen.value;
};
</script>

```

Mettez à jour les boutons `Edit` et `Delete` dans votre page d'accueil pour inclure le gestionnaire de bascule :

```vue
	...
    
             <div class="actions flex gap-4">
               <Button @click="toggleEditBookDrawer(book)">Edit</Button>
               <Button @click="toggleDeleteDialog(book)" variant="destructive">
                 Delete
               </Button>
             </div>
             
           ...
```

Incluez le `toggleAddDrawer` dans votre bouton Add Book également :

```vue
<Button @click="toggleAddBookDrawer">Add New Book</Button>
```

Enregistrez les modifications du fichier et visualisez dans votre navigateur. Vous devriez avoir le tiroir actif maintenant :  


![Image](https://lh7-us.googleusercontent.com/82AHDkwCX-oTW6pOpcwi735-8i5HluzloFnwDGnidH5gNKP8dkj3pXxr-Oa6gpMcQGZA-FnzsCP5nzpP0uGPDMhyTMkNqvxLXnVaK0TWFTBG-IrQPGU74-vhPpqCz1y7CcRULG7AUWcJsmejfdR5O2k)
_Tiroir Ajouter un nouveau livre_

Ensuite, nous devons nous assurer que le EditDrawer et le Delete Dialog fonctionnent. Nous allons créer un tableau temporaire de données de livres fictifs pour tester cela afin que vous puissiez voir le résultat sur votre page. Mettez à jour la valeur de la référence `books` avec les données que vous avez ci-dessous (et n'oubliez pas de mettre à jour la valeur de la référence books à un tableau vide – c'est-à-dire `books = ref<BookProps>([])`) :

```vue
const books = ref<BookProps[]>([
     {
       title: "Atomic Habits",
       author: "James Clear",
       isbn: "XYEOUIUEHEJ2902",
       published_date: "2020-09-01",
       cover_image: "",
     },
     {
       title: "The Power of Habits",
       author: "Charles Duhigg",
       isbn: "WIUIQUEWHSDBSD28",
       published_date: "2012-02-28",
       cover_image: "",
     },
]);

```

Enregistrez les modifications et vérifiez le EditDrawer et le DeleteDialog en action :

![Image](https://lh7-us.googleusercontent.com/_kiROvQBeLBq1UV9Zj4n0tVYOdW9nLUUjb5qlxGtgFGvAJtHsGJ0CvoEyYHxB4BIQ31SznXfwkiXhg_5VowECEMuSCYnIhfEHWeiHAt-hhA9dETiyTOgqNjsxxAenIhx0gl2koYaLVGYnohdpTV13KU)
_Boîte de dialogue de suppression_

![Image](https://lh7-us.googleusercontent.com/YSTKDAEOpLp45EXn61OlRYTTW3hYmOF-ur3SES7emDWMyigINQNvpAozgscEF84-RgiZrgCkTIxtZehFYDMIntzWmy589khRcP7FV4OpdacfXvsi8xRlJG9qWBuXc8Csbal0C_Tr-_lrDt6AatSnVIg)
_EditDrawer_

## Comment intégrer l'API Laravel dans le frontend

### Obtention de tous les livres de la bibliothèque

Jusqu'à présent, nous n'avons que l'interface utilisateur de notre frontend qui fonctionne, et les données affichées ne proviennent pas de l'API. Pour rendre l'application entièrement dynamique, vous devez faire une requête HTTP au serveur pour obtenir toutes les données dont vous avez besoin pour votre page. 

Mettez à jour le corps de la fonction `fetchBooks` dans la page d'accueil avec le code suivant :

```vue
const fetchBooks = async () => {
 try {
   isLoading.value = true;
   const response = await $fetch<{ books: BookProps[] }>(
     `${API_BASE_URL}/api/books`
   );


   books.value = response.books.sort(
     (a, b) =>
       Number(new Date(b.created_at as string)) -
       Number(new Date(a.created_at as string))
   );


 } catch (error) {
   console.log(error);
 } finally {
   isLoading.value = false;
 }
};


onMounted(() => {
 fetchBooks();
});

```

En gros, vous appelez votre fonction `fetchBooks` lorsque la page est montée en utilisant l'un des [hooks de cycle de vie](https://vuejs.org/api/composition-api-lifecycle.html#onmounted) disponibles dans Vue.js. Lorsque la fonction est appelée, elle exécute l'instruction que vous avez créée dans le corps :

* Définir l'état de chargement de l'application sur vrai.
* Faire une requête HTTP GET à l'endpoint des livres de votre API et définir la réponse à la référence des livres que vous avez créée précédemment.
* Lorsque la requête-réponse a été complétée, définir l'état de chargement de l'application sur faux pour indiquer à l'utilisateur que le processus a été complété.

Enregistrez les modifications, et vous devriez voir les résultats dans le navigateur :

![Image](https://lh7-us.googleusercontent.com/SGyND7gBGa7NmUXM4k-7Jn8pyuRizWhMJOOGnwZMMe7NIz6Jzt_qC0D3JUf-7X9IlGJMdm8XLbzGHG8cuKcJ6z83XpxOrrSGdAgOFaaUd6tDmo6-bDY-3PZG1lLRW4mywF77A86ABoIggR6NGwDDK5A)
_Récupération de la liste des livres_

### Création d'un nouveau livre

Pour que la création de votre livre soit réussie, vous devez inclure la logique de création d'un livre dans votre `BookDrawer`. Ajoutez le code suivant dans le fichier `BookDrawer.vue` :

```vue
...

const isSubmitting = ref(false);


const addNewBook = async (data: any) => {
 const response = await $fetch(`${API_BASE_URL}/api/books`, {
   method: "POST",
   body: data,
   headers: {
     Accept: "application/json",
   },
 });
 return response;
};


const onSubmit = async () => {
 try {
   const formData = new FormData();
   Object.keys(form).forEach((key) => {
     // @ts-ignore
     if (form[key]) {
       formData.append(key, form[key as never]);
     }
   });
   isSubmitting.value = true;
   const data = await addNewBook(formData);
   closeDrawer(false);
   emit("refresh-data");
 } catch (error) {
   console.log(error);
 } finally {
   isSubmitting.value = false;
 }
};

...
```

Similaire à l'implémentation pour récupérer vos livres, la seule différence ici est que vous faites une requête HTTP POST à la place. Vous utilisez cette méthode chaque fois que vous devez muter des données sur le serveur.

![Image](https://lh7-us.googleusercontent.com/7zQhG_V35mPWJW9sxMyTP8QjnezzoVg1eX08pdJ3Mw7EiXPwcHiTLdYHUD8HWqXg54SjvXymxrBCVWUjXbiuVNCAdj5vccdPyFl6KFJuuKAFTC9sYUQkkGYnESKr3aVHgUONnyOqAf1-fkafeqgyifE)
_Création d'un nouveau livre_

### Édition d'un livre

Mettez à jour votre `BookDrawer` avec le code suivant pour permettre l'édition des livres qui ont été ajoutés :

```vue
<script setup lang="ts">

...

onMounted(() => {
 if (props.book) {
   form = props.book;
 }
});


const editBook = async () => {
 try {
   isSubmitting.value = true;
   const resp = await $fetch(`${API_BASE_URL}/api/books/${props?.book?.id}`, {
     method: "PUT",
     body: formData,
   });
   closeDrawer(false);
   emit("refresh-data");
 } catch (error) {
   console.log(error);
 } finally {
   isSubmitting.value = false;
 }
};

...
</script>
```

Mettez à jour le bouton de sauvegarde avec le gestionnaire de bascule également :

```vue
<Button
  type="submit"
  @click="() => (book?.id ? editBook() : onSubmit())"
>
  <template v-if="isSubmitting">Saving...</template>
  <template v-else> Save changes </template>
</Button>
```

Et voici le résultat :

![Image](https://lh7-us.googleusercontent.com/aUGh8K6y9u8qXRwckj_PRphjvbnTR2DXf8jnHVehD2aaKtaCdCK1SVPjW-AbWwp_CXZROabKsTk0JBCaUjLAAzEbDHlFCbG6sjkpcVdW9VaKPqoYkVp2aoEtec5vPpjxFtNVAdFFWp3E3T_ZWNdxtYc)
_Mise à jour d'un livre_

### Suppression d'un livre

Collez ce qui suit dans le fichier `DeleteBookDialog.vue` :

```vue
const refreshData = () => emit("refresh-data");
const closeDialog = () => emit("update:open", false);


const deleteBook = async () => {
 await $fetch(`${API_BASE_URL}/api/books/${props?.book?.id}`, {
   method: "DELETE",
 });
 closeDialog();
 refreshData();
};

```

Cela fonctionne également bien :

![Image](https://lh7-us.googleusercontent.com/KyP9Y8L7qzkvvQCfyuFSBCQvrV30hE-rpQ72Q2Z1-DL-6rzkXnFAuwWEAL0Y1t110slYV813RPXyTKlxxKG5gHFQitUdVuT_7a-gkPxpJXtYOtRsxHWI0JSt9nFDeM6ywNf3ReoCxeIsKzguzZosw_E)
_Suppression d'un livre_

## Conclusion

Construire des applications web full-stack avec Laravel et Nuxt est une expérience très enrichissante, car vous pouvez profiter des avantages et des récompenses des deux mondes. 

Puisque Laravel est un framework backend riche en fonctionnalités, il est livré avec de nombreux modules et packages que vous pouvez installer chaque fois qu'une fonctionnalité ou une implémentation doit être travaillée. 

Et Nuxt, en tant que framework Vue, vous donne le superpouvoir de construire des applications monopages qui sont rapides, accessibles et réactives, offrant aux utilisateurs finaux une expérience agréable.

Dans ce tutoriel, nous avons vu comment construire des applications full-stack en utilisant Nuxt et le framework Laravel. J'espère que vous avez pu apprendre quelque chose de nouveau et que vous êtes enthousiaste à l'idée d'explorer cela plus avant. N'hésitez pas à me contacter si vous avez des questions ou des idées. 

Le code complet du tutoriel peut être trouvé dans le dépôt GitHub [ici](https://github.com/Young-Einstein10/laravel-nuxt-app/tree/final).

### Ressources

* [Documentation Laravel](https://laravel.com/docs/10.x)
* [Documentation Nuxt](https://nuxt.com/docs/getting-started/installation)
* [Shadcn-vue](https://www.shadcn-vue.com), composants d'interface utilisateur prêts à l'emploi qui peuvent être copiés-collés à tout moment
* [Documentation Vue](https://vuejs.org)