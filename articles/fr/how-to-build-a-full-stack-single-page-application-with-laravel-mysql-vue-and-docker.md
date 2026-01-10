---
title: Comment construire une application monopage Full-Stack avec Laravel 9, MySQL,
  Vue.js, Inertia, Jetstream et Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-16T13:55:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-full-stack-single-page-application-with-laravel-mysql-vue-and-docker
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/EP__3__LiveCoding.jpg
tags:
- name: Docker
  slug: docker
- name: full stack
  slug: full-stack
- name: Laravel
  slug: laravel
- name: MySQL
  slug: mysql
- name: ' Single Page Applications '
  slug: single-page-applications
- name: Vue.js
  slug: vuejs
seo_title: Comment construire une application monopage Full-Stack avec Laravel 9,
  MySQL, Vue.js, Inertia, Jetstream et Docker
seo_desc: 'By Fabio Pacific

  In this tutorial, you will learn how to build a single page application. I''ll take
  you through the process step by step, using cutting edge technologies like Laravel
  9, Jetstream, Vuejs, Inertiajs, MySQL, Tailwind CSS, and Docker.

  Le...'
---

Par Fabio Pacific

Dans ce tutoriel, vous apprendrez à construire une application monopage. Je vous guiderai étape par étape, en utilisant des technologies de pointe comme Laravel 9, Jetstream, Vuejs, Inertiajs, MySQL, Tailwind CSS et Docker.

Commençons.

## Ce dont vous avez besoin pour suivre ce guide :

Pour suivre ce tutoriel, vous aurez besoin : 
- d'un ordinateur
- de savoir comment installer des logiciels 
- d'une compréhension de base de HTML, CSS, JavaScript et PHP 
- de la connaissance d'au moins un framework JavaScript et d'une compréhension du modèle de conception MVC.

Ce guide est organisé en 10 chapitres et est basé sur une série de codage en direct que j'enregistre. La série de codage en direct est complètement improvisée, donc il y aura des bugs et des pièges que vous ne trouverez pas dans ce guide.

Vous pouvez trouver la playlist complète à la fin de cet article.

Tout ici devrait fonctionner, mais si ce n'est pas le cas, n'hésitez pas à demander de l'aide en rejoignant ma communauté sur Slack. Là, vous pouvez partager des extraits de code et discuter directement avec moi. 

## Table des matières

- [Quelles technologies utilisons-nous ?](#heading-quelles-technologies-utilisons-nous)
- [Comment configurer votre machine](#heading-comment-configurer-votre-machine)
- [Comment construire l'application avec Laravel 9, Laravel Sail, Jetstram, Inertia et Vue3](#heading-comment-construire-lapplication-avec-laravel-9-laravel-sail-jetstram-inertia-et-vue3)
- [Comment refactoriser le tableau de bord admin et créer de nouvelles pages admin](#heading-comment-refactoriser-le-tableau-de-bord-admin-et-creer-de-nouvelles-pages-admin)
- [Comment soumettre des formulaires avec des fichiers](#heading-comment-soumettre-des-formulaires-avec-des-fichiers)
- [Comment ajouter le formulaire au composant](#heading-comment-ajouter-le-formulaire-au-composant)
- [Comment stocker des données](#heading-comment-stocker-des-donnees)
- [Comment mettre à jour les opérations](#heading-comment-mettre-a-jour-les-operations)
- [Comment supprimer une ressource](#heading-comment-supprimer-une-ressource)
- [Conclusion et prochaines étapes](#heading-conclusion-et-prochaines-etapes)
- [Conclusion](#heading-conclusion)


## Quelles technologies utilisons-nous ?

Commençons par passer en revue les différents outils que nous utiliserons dans ce projet.

### Docker
Docker est un ensemble de produits de plateforme en tant que service qui utilisent la virtualisation au niveau du système d'exploitation pour livrer des logiciels dans des packages appelés conteneurs. 

Pour simplifier ce concept, Docker vous permet de packager des applications et des dépendances dans un conteneur. 

Une application conteneurisée vous permet d'avoir un environnement de développement flexible afin que vous puissiez exécuter différentes applications sans vous soucier des dépendances, de leurs exigences et des conflits entre différentes versions. Vous pouvez facilement exécuter des applications qui, par exemple, nécessitent deux versions différentes de PHP et MySQL. 

Chaque membre de l'équipe peut rapidement reproduire le même environnement de votre application en exécutant simplement la même configuration de conteneur.

Si vous souhaitez en savoir plus sur Docker, sa [Documentation](https://www.docker.com/) est un excellent point de départ.

Voici un [Guide sur les essentiels de Docker](https://www.freecodecamp.org/news/the-docker-handbook/), également, pour que vous puissiez pratiquer vos compétences.

### Mysql
MySQL est un système de gestion de base de données relationnelle open-source. Vous pouvez l'utiliser pour organiser des données dans une ou plusieurs tables avec des données qui peuvent être liées les unes aux autres.

Nous devons stocker des données quelque part et c'est là que MySQL entre en jeu.

Voici les [Docs](https://www.mysql.com/) si vous souhaitez en lire plus. Voici un [cours gratuit complet sur MySQL](https://www.freecodecamp.org/news/learn-to-use-the-mysql-database/) si vous souhaitez approfondir.

### Laravel
Laravel est un framework web PHP gratuit et open-source qui vous aide à développer des applications web suivant le modèle architectural modèle-vue-contrôleur.

Laravel est un framework PHP amazing que vous pouvez utiliser pour créer des applications web sur mesure.

Voici la documentation Laravel [Documentation](https://laravel.com/) pour plus d'informations, et voici un [cours complet basé sur un projet](https://www.freecodecamp.org/news/laravel-full-course/) pour vous aider à apprendre Laravel.

### Laravel Sail
Laravel Sail est une interface de ligne de commande légère pour interagir avec l'environnement de développement Docker par défaut de Laravel. 

Sail fournit un excellent point de départ pour construire une application Laravel en utilisant PHP, MySQL et Redis sans nécessiter d'expérience préalable avec Docker.

Habituellement, créer un environnement de développement pour construire de telles applications signifie que vous devez installer des logiciels, des langages et des frameworks sur votre machine locale – et cela prend du temps. Grâce à Docker et Laravel Sail, nous serons opérationnels en un rien de temps !

**Laravel Sail est pris en charge sur macOS, Linux et Windows [via WSL2](https://docs.microsoft.com/en-us/windows/wsl/about).**

Voici la [Documentation](https://laravel.com/docs/9.x/sail) si vous souhaitez en lire plus.

### Laravel Jetstream
Lors de la construction d'applications web, vous souhaitez probablement permettre aux utilisateurs de s'inscrire et de se connecter pour utiliser votre application. C'est pourquoi nous utiliserons Jetstream.

Laravel Jetstream est un kit de démarrage d'application magnifiquement conçu pour Laravel et fournit le point de départ parfait pour votre prochaine application Laravel.

Il utilise Laravel Fortify pour implémenter toute la logique d'authentification back-end.
Voici les [Docs](https://jetstream.laravel.com/2.x/introduction.html).

### Vuejs
Vue.js est un framework JavaScript front-end open-source modèle-vue-VueModel pour construire des interfaces utilisateur et des applications monopages.

Vue est un framework fantastique que vous pouvez utiliser comme un framework autonome pour construire des applications monopages, mais vous pouvez également l'utiliser avec Laravel pour construire quelque chose d'extraordinaire.

Voici la documentation Vue [Documentation](https://vuejs.org/) si vous souhaitez en lire plus. Et voici un [grand cours Vue](https://www.freecodecamp.org/news/vue-3-full-course/) pour vous lancer.

### Inertia JS
Inertia est le lien entre Laravel et Vuejs que nous utiliserons pour construire des applications monopages modernes en utilisant le routage côté serveur classique.

Vous pouvez en apprendre plus à ce sujet dans la [Documentation ici](https://inertiajs.com/).

### Tailwind
Tailwind CSS est un framework CSS basé sur les utilitaires, rempli de classes comme flex, pt-4, text-center et rotate-90 que vous pouvez utiliser pour construire n'importe quel design, directement dans votre balisage.

Nous l'utiliserons dans ce projet pour construire notre design. Voici un [guide rapide pour vous lancer](https://www.freecodecamp.org/news/get-started-with-tailwindcss/) si vous n'êtes pas familier avec Tailwind.


## Comment configurer votre machine

Pour suivre mon codage en direct (et ce tutoriel), vous devrez installer Docker Desktop sur votre machine. Si vous utilisez Windows, vous devrez également activer WSL dans les paramètres de votre système.

Visitez la page [getting started de Docker](https://www.docker.com/get-started) pour installer Docker Desktop.

Si vous êtes sous Windows, activez WSL2 en suivant les étapes [ici](https://docs.microsoft.com/en-us/windows/wsl/about).

Si vous avez des problèmes, n'hésitez pas à demander de l'aide ou à rejoindre ma communauté sur Slack.

## Installation de Laravel avec Sail

Si vous avez installé Docker Desktop sur votre machine avec succès, nous pouvons ouvrir le terminal et installer Laravel 9. 

Ouvrez une fenêtre de terminal et accédez à un dossier où vous souhaitez conserver votre projet. Ensuite, exécutez la commande ci-dessous pour télécharger les derniers fichiers Laravel. La commande placera tous les fichiers dans un dossier appelé my-example-app, que vous pouvez modifier comme vous le souhaitez.

```bash
# Télécharger laravel
curl -s "https://laravel.build/my-example-app" | bash
# Entrer dans le dossier laravel
cd my-example-app
```

### Déployer Laravel sur Docker en utilisant la commande `sail up`

Avec Docker Desktop en cours d'exécution, l'étape suivante consiste à démarrer Laravel sail pour construire tous les conteneurs nécessaires à l'exécution de notre application localement.

Exécutez la commande suivante à partir du dossier où tous les fichiers Laravel ont été téléchargés :

```bash
vendor/bin/sail up
```

Cela prendra une minute. Ensuite, visitez <http://localhost> et vous devriez voir votre application Laravel.

Si vous exécutez `sail up` et obtenez l'erreur suivante, il est probable que vous deviez mettre à jour Docker Desktop :

```bash
ERREUR : Le service 'laravel.test' a échoué à construire :
```

## Comment construire l'application avec Laravel 9, Laravel Sail, Jetstram, Inertia et Vue3

Dans cette section, nous allons définir une feuille de route de base, installer Laravel 9 avec Laravel Sail, exécuter sail et construire les conteneurs. 

Je vais également vous faire visiter Laravel Sail et les commandes sail. 

Ensuite, nous installerons Jetstream et échafauderons les fichiers Vue et Inertia et jetterons un coup d'œil aux fichiers et fonctionnalités disponibles.

Ensuite, nous peuplerons notre base de données et ajouterons le front-end fourni par Jetstream pour enregistrer un compte et se connecter à une nouvelle application Laravel.

Enfin, nous jetterons un coup d'œil au tableau de bord Jetstream, aux composants Inertia/Vue et commencerons à jouer.

En cours de route, nous désactiverons l'inscription, activerons la fonctionnalité de photo de profil utilisateur de Jetstream, puis ajouterons notre première page Inertia où nous rendrons certaines données provenant de la base de données.

Voici la vidéo de codage en direct si vous souhaitez suivre de cette manière :


%[https://youtu.be/c0ibec9dhZA]

Et si vous préférez suivre ce tutoriel écrit, voici toutes les étapes.

Rappel – vous devriez avoir Laravel installé avec Sail et avoir Docker configuré sur votre machine. Vous pouvez suivre les étapes ci-dessus pour le faire si ce n'est pas déjà fait.


### Vue d'ensemble de Laravel Sail – Commandes Sail

Avec Laravel Sail installé, nos commandes Laravel habituelles ont légèrement changé.

Par exemple, au lieu d'exécuter la commande artisan Laravel en utilisant PHP comme `php artisan`, nous devons maintenant utiliser Sail, comme ceci : `sail artisan`.

La commande `sail artisan` retournera une liste de toutes les commandes Laravel disponibles.

Habituellement, lorsque nous travaillons avec Laravel, nous devons également exécuter les commandes `npm` et `composer`.

Encore une fois, nous devons préfixer nos commandes avec `sail` pour les faire fonctionner à l'intérieur du conteneur.

Ci-dessous, vous trouverez une liste de certaines commandes que vous devrez probablement exécuter :

```bash
# Interagir avec la base de données - exécuter les migrations
sail artisan migrate # C'était : php artisan migrate
# Utiliser les commandes composer
sail composer require <packageName> # c'était : composer require <packageName>
# Utiliser les commandes npm
sail npm run dev # c'était : npm run dev
```

Vous pouvez en lire plus dans la [documentation Sail](https://laravel.com/docs/9.x/sail#executing-sail-commands).


### Installer Jetstream et échafauder Vue et Inertia

Installons maintenant le package d'authentification Laravel Jetstream et utilisons l'échafaudage Inertia avec Vue3.

```bash
cd my-example-app
sail composer require laravel/jetstream 
```

N'oubliez pas de préfixer la commande composer avec `sail`.

La commande ci-dessus a ajouté une nouvelle commande à Laravel. Maintenant, nous devons l'exécuter pour installer tous les composants Jetstream :

```bash
sail artisan jetstream:install inertia
```

Ensuite, nous devons compiler tous les actifs statiques avec npm :

```bash
sail npm install
sail npm run dev
```

Avant de pouvoir voir notre application, nous devrons exécuter les migrations de la base de données afin que la table de session, requise par Jetstream, soit présente.

```bash
sail artisan migrate

```

Terminé ! Jetstream est maintenant installé dans notre application. Si vous visitez `http://localhost` dans votre navigateur, vous devriez voir l'application Laravel avec deux liens en haut pour vous inscrire et vous connecter.

![welcome-page](https://www.freecodecamp.org/news/content/images/2022/05/welcome-page.png)

### Remplir la base de données et créer un compte utilisateur

Avant de créer un nouvel utilisateur, jetons un coup d'œil rapide à la configuration de la base de données que Laravel Sail a créée pour nous dans le fichier `.env`.

```env
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=my-example-app
DB_USERNAME=sail
DB_PASSWORD=password
```

Comme vous pouvez le voir, Laravel Sail configure tout ce dont nous avons besoin pour accéder au conteneur de la base de données qui s'exécute sur Docker. Le `DB_DATABASE` est le nom de la base de données et il est le même que le dossier du projet. C'est pourquoi dans l'étape précédente nous avons pu exécuter la commande `migrate` sans problème.

Puisque nous avons déjà migré toutes les tables de la base de données, nous pouvons maintenant utiliser l'usine d'utilisateurs intégrée de Laravel pour créer un nouvel utilisateur, puis utiliser ses détails pour nous connecter à notre tableau de bord d'application.

Ouvrons artisan tinker pour interagir avec notre application.

```bash
sail artisan tinker
```

La commande ci-dessus ouvrira une interface de ligne de commande que nous pouvons utiliser pour interagir avec notre application. Créons un nouvel utilisateur.

```php
User::factory()->create()
```

La commande ci-dessus créera un nouvel utilisateur et enregistrera ses données dans notre base de données. Ensuite, elle affichera les données de l'utilisateur à l'écran. Assurez-vous de copier l'email de l'utilisateur afin que nous puissions l'utiliser plus tard pour nous connecter. Ensuite, quittez en tapant `exit;`.

Le mot de passe par défaut pour chaque utilisateur créé avec une usine est `password`.

Visitez la page de connexion et accédez à notre tableau de bord d'application.

![loginpage](https://www.freecodecamp.org/news/content/images/2022/05/loginpage.png)

### Tableau de bord Jetstream

Après la connexion, vous êtes redirigé vers le tableau de bord Jetstream, qui a l'air génial par défaut. Nous pouvons le personnaliser comme nous le souhaitons, mais ce n'est qu'un point de départ.

![dashboard](https://www.freecodecamp.org/news/content/images/2022/05/dashboard.png)

### Composants Jetstream/Vue et vue d'ensemble d'Inertia

La première chose que vous pouvez remarquer après avoir installé Jetstram est qu'il y a un certain nombre de composants Vue enregistrés dans notre application. Non seulement cela, mais Inertia apporte également des composants Vue. 

Pour utiliser Inertia, nous devons nous familiariser avec lui lors de la définition des routes.

Lorsque nous avons installé Jetstream, il a créé dans le répertoire `resources/js` un certain nombre de sous-dossiers où vivent tous nos composants Vue. Il ne s'agit pas seulement de simples composants, mais aussi de composants Pages rendus par inertia comme nos Vues.

L'échafaudage inertia de Jetstream a créé :

- `resources/js/Jetstream` Ici nous avons 27 composants utilisés par Jetstream, mais nous pouvons aussi les utiliser dans notre application si nous le voulons.
- `resources/js/Layouts` Dans ce dossier se trouve le composant de mise en page utilisé par inertia pour rendre la page du tableau de bord
- `resources/js/Pages` C'est ici que nous placerons tous nos composants Pages (vues). Vous trouverez la page Dashboard ainsi que les composants de la page de bienvenue Laravel ici.

La puissance d'Inertia vient principalement de la manière dont il connecte Vue et Laravel, nous permettant de passer des données (modèles de base de données et plus) en tant que props à nos composants Vue Pages.

Lorsque vous ouvrez le fichier `routes/web.php`, vous remarquerez que nous ne retournons plus une vue mais utilisons plutôt `Inertia` pour rendre un composant de page.

Examinons la route de la page d'accueil `/` qui rend le composant Welcome.

```php
Route::get('/', function () {
    return Inertia::render('Welcome', [
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
        'laravelVersion' => Application::VERSION,
        'phpVersion' => PHP_VERSION,
    ]);
});
```

Cela ressemble à notre définition de route habituelle, sauf que dans la fermeture nous retournons un `\Inertia\Response` en appelant la méthode `render` de la classe Inertia `Inertia::render()`. 

Cette méthode accepte deux paramètres. Le premier est un nom de composant. Ici nous avons passé le composant de page `Welcome`, tandis que le deuxième paramètre est un tableau associatif qui se transformera en une liste de `props` à passer au composant. C'est là que la magie opère.

En regardant à l'intérieur du composant Welcome, vous remarquerez que dans sa section script, nous définissons simplement quatre props correspondant aux clés de notre tableau associatif. Ensuite, inertia fera le reste.

```vue
<script>
    import { defineComponent } from 'vue'
    import { Head, Link } from '@inertiajs/inertia-vue3';

    export default defineComponent({
        components: {
            Head,
            Link,
        },
        // 👇 Définir les props 
        props: {
            canLogin: Boolean, 
            canRegister: Boolean,
            laravelVersion: String,
            phpVersion: String,
        }
    })
</script>
```

Nous pouvons ensuite simplement appeler les props à l'intérieur du template. Si vous regardez la section template, vous remarquerez que `laravelVersion` et `phpVersion` sont référencées dans le code comme vous le feriez normalement avec les props dans Vuejs.

```html
<div class="ml-4 text-center text-sm text-gray-500 sm:text-right sm:ml-0">
  Laravel v{{ laravelVersion }} (PHP v{{ phpVersion }})
</div>
```

Le composant dashboard est un peu différent. En fait, il utilise le Layout défini sous `Layouts/AppLayout.vue` et utilise le composant `Welcome` pour rendre le contenu de la page Dashboard, qui est le même que la page de bienvenue de laravel.

```html

<template>
    <app-layout title="Dashboard">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">
                Dashboard
            </h2>
        </template>

        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <div class="bg-white overflow-hidden shadow-xl sm:rounded-lg">
                    <welcome /> 
                </div>
            </div>
        </div>
    </app-layout>
</template>

```

À l'intérieur du composant de mise en page, vous remarquerez les deux composants inertia `Head` et `Link`.

Nous pouvons utiliser le composant `Head` pour ajouter des éléments head à notre page, comme des balises meta, le titre de la page, etc. Le composant `Link` est un wrapper autour d'une balise d'ancrage standard qui intercepte les événements de clic et empêche le rechargement complet de la page comme vous pouvez le lire dans la documentation Inertia.

[Composant Link](https://inertiajs.com/links)
[Composant Head](https://inertiajs.com/title-and-meta#head-component)

### Désactiver la fonctionnalité d'inscription

Si vous suivez ce tutoriel, l'étape suivante que je vais prendre est de désactiver l'une des fonctionnalités fournies par Jetstream – l'inscription d'un compte. 

Pour ce faire, nous pouvons naviguer vers `config/fortify.php` et commenter la ligne 135 `Features::registration()` dans le tableau des fonctionnalités.

```php
'features' => [
        //Features::registration(),
        Features::resetPasswords(),
        // Features::emailVerification(),
        Features::updateProfileInformation(),
        Features::updatePasswords(),
        Features::twoFactorAuthentication([
            'confirmPassword' => true,
        ]),
    ],
```

Si nous visitons la page d'accueil, nous remarquerons que le lien `register` a disparu. De plus, la route n'est plus listée lorsque nous exécutons `sail artisan route:list`.


### Activer la photo de profil utilisateur Jetstream

Maintenant, essayons d'activer la fonctionnalité Jetstream appelée ProfilePhotos. Comme vous pouvez le deviner, cela permettra à l'utilisateur d'ajouter une photo de profil.

Pour ce faire, nous devons visiter `config/jetstream.php` et décommenter la ligne 59 `Features::profilePhotos`.

```php
    'features' => [
        // Features::termsAndPrivacyPolicy(),
        Features::profilePhotos(), // 👇
        // Features::api(),
        // Features::teams(['invitations' => true]),
        Features::accountDeletion(),
    ],
```

Si vous vous connectez, vous verrez que dans le profil utilisateur, une nouvelle section est disponible pour télécharger une photo de profil.

Mais avant de faire quoi que ce soit d'autre, nous devons exécuter `sail artisan storage:link` afin que Laravel crée un lien symbolique vers le dossier `storage/app/public` où nous enregistrerons toutes les images de profil des utilisateurs.

Maintenant, essayez de visiter le profil utilisateur et de mettre à jour la photo de profil. Si vous obtenez une erreur 404 sur l'image, c'est parce que par défaut Laravel sail suppose que nous utilisons Laravel valet et définit l'URL de l'application comme suit `APP_URL=http://my-example-app.test` dans le fichier `.env`. Changeons cela et utilisons localhost à la place.

```env
APP_URL=http://localhost
```

Maintenant, nous devrions être prêts à voir et changer notre image de profil !🥳

### Comment ajouter notre première page Inertia et rendre les enregistrements de la base de données

Puisque nous rendons des composants Vue au lieu de vues blade, il est judicieux de démarrer `sail npm run watch` pour surveiller et recompiler nos composants Vue au fur et à mesure que nous les créons ou les modifions. Ensuite, ajoutons une nouvelle page Photos.

Je vais commencer par créer une nouvelle route dans web.php :

```php
Route::get('photos', function () {
    //dd(Photo::all());
    return Inertia::render('Guest/Photos');
});
```

Dans le code ci-dessus, j'ai défini une nouvelle route GET puis rendu un composant que je placerai dans `resources/js/Pages/Guest` et que j'appellerai `Photos`. Créons-le.

Créez un dossier Guest :

```bash
cd resources/js/Pages
mkdir Guest
cd Guest
touch Photos.vue
```

Ensuite, définissons un composant de base :

```vue
<template>
  <h1>Photos Page</h1>
</template>

```

Si nous visitons `http://localhost/photos/` nous verrons notre nouvelle page, cool ! Copions la structure de la page d'accueil pour obtenir également les liens de connexion et de tableau de bord.

Le composant changera pour cela :

```vue
<template>
    <Head title="Phots" />

    <div class="relative flex items-top justify-center min-h-screen bg-gray-100 dark:bg-gray-900 sm:items-center sm:pt-0">
        <div v-if="canLogin" class="hidden fixed top-0 right-0 px-6 py-4 sm:block">
            <Link v-if="$page.props.user" :href="route('admin.dashboard')" class="text-sm text-gray-700 underline">
                Dashboard
            </Link>

            <template v-else>
                <Link :href="route('login')" class="text-sm text-gray-700 underline">
                    Log in
                </Link>

                <Link v-if="canRegister" :href="route('register')" class="ml-4 text-sm text-gray-700 underline">
                    Register
                </Link>
            </template>
        </div>

        <div class="max-w-6xl mx-auto sm:px-6 lg:px-8">
            <h1>Photos</h1>
            
        </div>
    </div>
</template>

<script>
    import { defineComponent } from 'vue'
    import { Head, Link } from '@inertiajs/inertia-vue3';

    export default defineComponent({
        components: {
            Head,
            Link,
        },

        props: {
            canLogin: Boolean,
            canRegister: Boolean,
          
        }
    })
</script>

```

L'étape suivante consiste à rendre un ensemble de données sur cette nouvelle page. Pour cela, nous allons construire un modèle et ajouter quelques enregistrements à la base de données.

```bash
saild artisan make:model Photo -mfcr
```

Cette commande crée un modèle appelé `Photo`, plus une classe de table de migration de base de données, une usine et un contrôleur de ressource.

Maintenant, définissons la table de base de données à l'intérieur de la migration que nous venons de créer. Visitez le dossier `database/migrations` et vous devriez voir un fichier avec un nom similaire à celui-ci : `2022_02_13_215119_create_photos_table` (le vôtre sera légèrement différent).

À l'intérieur du fichier de migration, nous pouvons définir une table de base comme suit :

```php
 public function up()
    {
        Schema::create('photos', function (Blueprint $table) {
            $table->id();
            $table->string('path');
            $table->text('description');
            $table->timestamps();
        });
    }
```

Pour notre table, nous avons défini seulement deux nouvelles colonnes, `path` et `description`, plus l'`id`, `created_at` et `updated_at` qui seront créés par les méthodes `$table->id()` et `$table->timestamps()`.

Après la migration, nous définirons un seeder puis exécuterons les migrations et ensemencerons la base de données.

En haut du fichier `database/seeders/PhotoSeeder.php`, nous importerons notre modèle et Faker :

```php
use App\Models\Photo;
use Faker\Generator as Faker;
```

Ensuite, nous implémenterons la méthode run en utilisant une boucle for pour créer 10 enregistrements dans la base de données.

```php


    public function run(Faker $faker)
    {
        for ($i = 0; $i < 10; $i++) {
            $photo = new Photo();
            $photo->path = $faker->imageUrl();
            $photo->description = $faker->paragraphs(2, true);
            $photo->save();
        }
    }

```

Nous sommes prêts à exécuter les migrations et à ensemencer la base de données.

```php

sail artisan migrate
sail artisan db:seed --class PhotoSeeder

```

Nous sommes maintenant prêts à afficher les données sur le composant de page `Guest/Photos`.
Tout d'abord, mettez à jour la route et passez une collection de photos en tant que props au composant rendu :

```php
Route::get('photos', function () {
    //dd(Photo::all());
    return Inertia::render('Guest/Photos', [
        'photos' => Photo::all(), ## 👇 Passer une collection de photos, la clé deviendra notre prop dans le composant
        'canLogin' => Route::has('login'),
        'canRegister' => Route::has('register'),
    ]);
});

```

Deuxièmement, passez la prop aux props dans la section script du composant Guest/Photos :

```js

props: {
    canLogin: Boolean,
    canRegister: Boolean,
    photos: Array // 👇 Ici
}
```

Enfin, parcourez le tableau et rendez toutes les photos dans la section template, juste sous le h1 :

```html
<section class="photos">
    <div v-for="photo in photos" :key="photo.id" class="card" >
        <img :src="photo.path" alt="">
    </div>
</section>
```

Terminé ! Si vous visitez la page `/photos`, vous devriez voir dix photos. 🥳



## Comment refactoriser le tableau de bord admin et créer de nouvelles pages admin

Dans ce chapitre, nous allons rediriger le tableau de bord Jetstream et créer un groupe de routes pour toutes les pages admin. 

Ensuite, nous verrons comment ajouter un nouveau lien au tableau de bord et ajouter une nouvelle page admin. 

Enfin, nous prendrons une collection de données de la base de données et les rendrons dans un tableau de base. Le tableau par défaut n'est pas assez cool, donc pour ceux qui lisent cet article, j'ai décidé d'ajouter un composant de tableau Tailwind.

### Rediriger le tableau de bord Jetstream

Si nous regardons le fichier `config/fortify.php`, nous pouvons voir qu'autour de la ligne 64, il y a une clé appelée home. Elle appelle la constante `Home` du fournisseur de services de route.

Cela signifie que nous pouvons ajuster la constante et rediriger l'utilisateur authentifié vers une route différente.

Passons en revue étape par étape :

- mettre à jour la constante HOME
- créer un groupe de routes et rediriger les utilisateurs connectés vers `admin/` au lieu de '/dashboard'

Notre application n'aura qu'un seul utilisateur, donc une fois connecté, il s'agit clairement de l'administrateur du site – il est donc logique de rediriger vers un URI `admin`.

Modifiez la constante HOME dans `app/Providers/RouteServiceProvider.php` autour de la ligne 20 pour correspondre à ce qui suit :

```php
public const HOME = '/admin';
```

### Comment ajouter un groupe de routes pour les pages admin

Ensuite, mettons à jour notre route dans web.php. Nous allons changer la route enregistrée par Jetstream de ceci :

```php
Route::middleware(['auth:sanctum', 'verified'])->get('/', function () {
        return Inertia::render('Dashboard');
    })->name('dashboard');
```

À ceci :

```php
Route::middleware(['auth:sanctum', 'verified'])->prefix('admin')->name('admin.')->group(function () {

    Route::get('/', function () {
        return Inertia::render('Dashboard');
    })->name('dashboard');

    // autres routes admin ici
});

```

La route ci-dessus est un groupe de routes qui utilise le middleware `auth:sanctum` pour toutes les routes du groupe, un préfixe `admin`, et ajoute un suffixe `admin` à chaque nom de route.

Le résultat final est que nous pourrons nous référer à la route du tableau de bord par son nom, qui sera maintenant `admin.dashboard`. Lorsque nous nous connectons, nous serons redirigés vers la route `admin`. Notre route de tableau de bord répondra puisque son URI est simplement `/` mais le préfixe de groupe préfixera chaque route du groupe et fera commencer leur URI par `admin`.

Si vous exécutez maintenant `sail artisan route:list`, vous remarquerez que la route du tableau de bord a changé comme nous l'attendions.

Avant de passer à l'étape suivante, nous devons mettre à jour les composants `/layouts/AppLayout.vue` et `/Pages/Welcome.vue`.

Vous vous souvenez que le nom de la route du tableau de bord est maintenant `admin.dashboard` et non plus simplement `dashboard` ?

Inspectons les deux composants et mettons à jour chaque référence de `route('dahsboard')` par ceci :

```js
route('admin.dahsboard')
```

et aussi chaque référence de `route().current('dashboard')` par ceci :

```js
route().current('admin.dashboard')
```

Après toutes les modifications, assurez-vous de recompiler les composants Vue et de surveiller les changements en exécutant `sail npm run watch`. Ensuite, visitez la page d'accueil pour vérifier si tout fonctionne.

### Comment ajouter un nouveau lien au tableau de bord

Maintenant, pour ajouter une nouvelle page admin où nous pouvons lister toutes les photos stockées dans la base de données, nous devons ajouter une nouvelle route au groupe que nous avons créé précédemment. Modifions le fichier `web.php` et apportons nos modifications.

Dans le groupe de routes, nous ajouterons une nouvelle route :

```php
Route::middleware(['auth:sanctum', 'verified'])->prefix('admin')->name('admin.')->group(function () {

    Route::get('/', function () {
        return Inertia::render('Dashboard');
    })->name('dashboard');

    // 👇 autres routes admin ici 👇

    Route::get('/photos', function () {
        return inertia('Admin/Photos');
    })->name('photos'); // Cela répondra aux requêtes pour admin/photos et aura un nom de admin.photos

});
```

Dans la nouvelle route ci-dessus, nous avons utilisé la fonction d'assistance `inertia()` qui fait exactement la même chose – retourne une réponse Inertia et rend notre composant de page. Nous avons placé le composant sous un dossier `Admin` à l'intérieur de `Pages` et nous l'appellerons `Photos.vue`.

Avant de créer le composant, ajoutons un nouveau lien au tableau de bord qui pointe vers notre nouvelle route.

À l'intérieur de `AppLayout.vue`, trouvez le commentaire `Navigation Links` et copiez/collez le composant `jet-nav-link` qui affiche actuellement un lien vers le tableau de bord et faites-le pointer vers notre nouvelle route.

Vous obtiendrez quelque chose comme ceci :

```html
<!-- Navigation Links -->
<div class="hidden space-x-8 sm:-my-px sm:ml-10 sm:flex">
    <jet-nav-link :href="route('admin.dashboard')" :active="route().current('admin.dashboard')">
        Dashboard
    </jet-nav-link>
    <!-- 👇 voici notre nouveau lien -->
      <jet-nav-link :href="route('admin.photos')" :active="route().current('admin.photos')">
        Photos
    </jet-nav-link>
</div>

```

Notre lien ci-dessus utilise `route('admin.photos')` pour pointer vers la route correcte dans le groupe admin.

Si vous visitez `localhost/dashboard` et ouvrez l'inspecteur, vous devriez voir une erreur :

```js
Erreur : Impossible de trouver le module `./Photos.vue`
```

C'est normal – nous n'avons pas encore créé le composant de la page Photos. Alors faisons-le maintenant !

### Comment ajouter un nouveau composant de page admin

Créez un fichier nommé `Photos.vue` dans le dossier `Pages/Admin`. Voici les commandes bash pour créer le dossier et le fichier via le terminal, mais vous pouvez faire de même en utilisant l'interface graphique de votre IDE.

```bash
cd resources/js/Pages
mkdir Admin
touch Admin/Photos.vue
```

Pour que cette nouvelle page ressemble à la page Dashboard, nous allons copier son contenu. Vous devriez obtenir quelque chose comme ceci :

```vue

<template>
  <app-layout title="Dashboard"> <!-- 👇 si vous le souhaitez, vous pouvez mettre à jour le titre de la page -->
    <template #header>
      <h2 class="font-semibold text-xl text-gray-800 leading-tight">Photos</h2>
    </template>

    <div class="py-12">
      <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
        <div class="bg-white overflow-hidden shadow-xl sm:rounded-lg">
          <!-- 👇  Toutes les photos pour la page Admin ici -->
          <h1 class="text-2xl">Photos</h1>
           
        </div>
      </div>
    </div>
  </app-layout>
</template>

<script>
import { defineComponent } from "vue";
import AppLayout from "@/Layouts/AppLayout.vue";

export default defineComponent({
  components: {
    AppLayout,
  },
});
</script>

```

J'ai supprimé quelques éléments du modèle Dashboard, alors assurez-vous de vérifier le code ci-dessus. Le composant `welcome` a été supprimé du modèle car il n'est pas requis dans cette page, ainsi que sa référence dans la section script. Le reste est identique.

N'hésitez pas à mettre à jour le titre de la page référencé en tant que prop sur `<app-layout title="Dashboard">`.

Maintenant, lorsque vous visitez `localhost/admin`, vous pouvez cliquer sur l'élément de menu Photos et voir le contenu de notre composant de page Photos. Ce n'est pas grand-chose pour l'instant, juste un `h1`.

### Comment rendre les enregistrements dans la page admin sous forme de tableau

Il est maintenant temps de rendre les données dans un tableau. Pour que les choses fonctionnent, ajoutons d'abord notre balisage et faisons semblant que nous avons déjà accès à un tableau d'objets et parcourons-les à l'intérieur de notre tableau. Ensuite, nous découvrirons comment faire fonctionner les choses pour de vrai.

```html
 <table class="table-auto w-full text-left">
  <thead>
    <tr>
      <th>ID</th>
      <th>Photo</th>
      <th>Desciption</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="photo in photos">
      <td>{{ photo.id }}</td>
      <td><img width="60" :src="photo.path" alt="" /></td>
      <td>{{photo.description}}</td>
      <td>View - Edit - Delete</td>

    </tr>
  </tbody>
</table>

```

D'accord, puisque nous avons supposé que notre composant a accès à une liste de photos, passons une nouvelle prop au composant depuis la route.

Mettez à jour la route dans web.php et passez à la fonction `inertia()` un deuxième argument qui sera un tableau associatif. Ses clés seront passées en tant que props au composant Vue Page. 

Dans celui-ci, nous appellerons `Photo::all()` pour avoir une collection à assigner à une clé `photos`, mais vous pouvez utiliser d'autres méthodes éloquentes si vous souhaitez paginer les résultats, par exemple.

```php
Route::get('/photos', function () {
    return inertia('Admin/Photos', [
        'photos' => Photo::all()
    ]);
})->name('photos');

```

Pour connecter la prop à notre composant Page, nous devons définir la prop également à l'intérieur du composant.

```js
<script>
import { defineComponent } from "vue";
import AppLayout from "@/Layouts/AppLayout.vue";

export default defineComponent({
  components: {
    AppLayout,
  },
  /* 👇 Passer le tableau de photos en tant que props 👇 */
  props: {
    photos: Array,
  },
});
</script>
```

#### Extra : Comment utiliser un composant de tableau Tailwind

Tailwind est un framework CSS similaire à Bootstrap. Il existe un certain nombre de composants gratuits que nous pouvons prendre dans la documentation, modifier et utiliser.

Ce composant de tableau est gratuit et a l'air bien : <https://tailwindui.com/components/application-ui/lists/tables>.

Nous pouvons modifier le modèle de la page Photos et utiliser le composant de tableau Tailwind pour obtenir un tableau bien présenté comme suit :

```vue

<template>
    <app-layout title="Dashboard">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">Photos</h2>
        </template>

         <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
              <!-- Tous les posts vont ici -->
              <h1 class="text-2xl">Photos</h1>
              <a class="px-4 bg-sky-900 text-white rounded-md" href>Create</a>
              <div class="flex flex-col">
                  <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                          <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
                              <table class="min-w-full divide-y divide-gray-200">
                                  <thead class="bg-gray-50">
                                      <tr>
                                          <th
                                              scope="col"
                                              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                                          >ID</th>
                                          <th
                                              scope="col"
                                              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                                          >Photos</th>
                                          <th
                                              scope="col"
                                              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                                          >Description</th>
                                          <th scope="col" class="relative px-6 py-3">
                                              <span class="sr-only">Edit</span>
                                          </th>
                                      </tr>
                                  </thead>
                                  <tbody class="bg-white divide-y divide-gray-200">
                                      <tr v-for="photo in photos" :key="photo.id">
                                          <td class="px-6 py-4 whitespace-nowrap">
                                              <div
                                                  class="text-sm text-gray-900"
                                              >{{ photo.id }}</div>
                                          </td>

                                          <td class="px-6 py-4 whitespace-nowrap">
                                              <div class="flex items-center">
                                                  <div class="flex-shrink-0 h-10 w-10">
                                                      <img
                                                          class="h-10 w-10 rounded-full"
                                                          :src="photo.path"
                                                          alt
                                                      />
                                                  </div>
                                              </div>
                                          </td>

                                          <td class="px-6 py-4 whitespace-nowrap">
                                              <div class="text-sm text-gray-900">
                                                {{ photo.description.slice(0, 100) + '...' }}
                                              </div>
                                          </td>
                                        <!-- ACTIONS -->
                                          <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                              <a href="#" class="text-indigo-600 hover:text-indigo-900">
                                              View - Edit - Delete
                                              </a>
                                          </td>
                                      </tr>
                                  </tbody>
                              </table>
                          </div>
                      </div>
                  </div>
                </div>
            </div>
        </div>
    </app-layout>
</template>
```


## Comment soumettre des formulaires avec des fichiers

Pour la section suivante, nous allons voir comment soumettre un formulaire afin de pouvoir ajouter une nouvelle photo à la base de données.

- Ajouter un bouton de création
- Ajouter une route de création
- Définir le composant PhotosCreate
- Ajouter un formulaire
- Valider les données
- Afficher les erreurs de validation
- Enregistrer le fichier dans le système de fichiers
- Enregistrer le modèle

### Comment créer une nouvelle photo

Ajoutez un lien qui pointe vers une route de création :

```html
<a class="px-4 bg-sky-900 text-white rounded-md" :href="route('admin.photos.create')">Create</a>
```

Créez la route dans le groupe admin :

```php
Route::get('/photos/create', function () {
    return inertia('Admin/PhotosCreate');
})->name('photos.create');
```

Ajoutons également la route qui gérera la soumission du formulaire pour plus tard :

```php
Route::post('/photos', function () {
    dd('I will handle the form submission')   
})->name('photos.store');
```

Créez le composant `Admin/PhotosCreate.vue` :

```vue

    <template>
    <app-layout title="Dashboard">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">Photos</h2>
        </template>

         <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <h1 class="text-2xl">Add a new Photo</h1>
                <!-- 👇 Le formulaire de création de photo va ici -->

            </div>
        </div>
    </app-layout>
</template>


<script>
import { defineComponent } from "vue";
import AppLayout from "@/Layouts/AppLayout.vue";

export default defineComponent({
  components: {
    AppLayout,
  },

});
</script>

```

## Comment ajouter le formulaire au composant

L'étape suivante consiste à ajouter le formulaire à la page et à déterminer comment le soumettre.

Si vous consultez la documentation Inertia, vous découvrirez qu'il existe une classe useForm que nous pouvons utiliser pour simplifier le processus.

Tout d'abord, importez le module à l'intérieur de la balise script du composant Admin/PhotosCreate.vue :

```js
import { useForm } from '@inertiajs/inertia-vue3';
```

Ensuite, nous pouvons l'utiliser dans la fonction setup (API de composition Vue 3) :

```js
setup () {
    const form = useForm({
      path: null,
      description: null,
    })

    return { form }
  }
```

Dans le code ci-dessus, nous avons défini la fonction appelée `setup()` puis une constante appelée `form` pour avoir la classe `useForm()` assignée à celle-ci.

À l'intérieur de ses parenthèses, nous avons défini deux propriétés, `path` et `description`, qui sont les noms de colonne de notre modèle de photos.

Enfin, nous avons retourné la variable `form` pour la fonction setup. Cela permet de rendre la variable disponible à l'intérieur de notre template.

Ensuite, nous pouvons ajouter le balisage du formulaire :

```html
<form @submit.prevent="form.post(route('admin.photos.store'))">

<div>
    <label for="description" class="block text-sm font-medium text-gray-700"> Description </label>
    <div class="mt-1">
        <textarea id="description" name="description" rows="3" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md" placeholder="lorem ipsum" v-model="form.description"/>
    </div>
    <p class="mt-2 text-sm text-gray-500">Brief description for your photo</p>
        <div class="text-red-500" v-if="form.errors.description">{{form.errors.description}}</div>
</div>
<div>
    <label class="block text-sm font-medium text-gray-700"> Photo </label>
    <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
    <div class="space-y-1 text-center">
        <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
        <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <div class="flex text-sm text-gray-600">
        <label for="path" class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500">
            <span>Upload a file</span>
            <input id="path" name="path" type="file" class="sr-only" @input="form.path = $event.target.files[0]" />
        </label>
        <p class="pl-1">or drag and drop</p>
        </div>
        <p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
    </div>
    </div>
</div>
<div class="text-red-500" v-if="form.errors.path">{{form.errors.path}}</div>

<button type="submit" :disabled="form.processing" class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Save</button>
</form>
```

Le code ci-dessus utilise la syntaxe courte de la directive v-on de Vue `@submit.prevent="form.post(route('admin.photos.store'))"` sur la balise form, et l'événement dom `submit` avec le modificateur `prevent`. 

Ensuite, il utilise la variable `form` que nous avons créée précédemment et une méthode `post`. Cela est disponible parce que nous utilisons la classe `useForm`. 

Ensuite, nous pointons le formulaire vers la route nommée admin.photos.store que nous avons créée précédemment.

À l'intérieur du formulaire, nous avons deux groupes d'entrées. Tout d'abord, nous avons la zone de texte qui utilise le v-model pour la lier à la propriété `form.description` que nous avons déclarée auparavant.

Le deuxième groupe utilise le `form.path` dans un composant Tailwind (montrant le balisage pour une zone de dépôt de fichier).

Pour l'instant, nous permettons aux utilisateurs de télécharger une seule photo en utilisant la directive v-on sur l'événement DOM d'entrée `@input="form.path = $event.target.files[0]"`.

Les deux dernières choses à noter sont la gestion des erreurs effectuée via `<div class="text-red-500" v-if="form.errors.path">{{form.errors.path}}</div>` pour le chemin et également pour la description.

Enfin, nous utilisons `form.processing` pour désactiver le bouton de soumission pendant que le formulaire est en cours de traitement.

L'étape suivante consiste à définir la logique pour enregistrer les données dans la base de données.


## Comment stocker des données

Pour stocker les données, nous pouvons modifier la route que nous avons définie précédemment comme suit :

```php
Route::post('/photos', function (Request $request) {
    //dd('I will handle the form submission')  
    
    //dd(Request::all());
    $validated_data = $request->validate([
        'path' => ['required', 'image', 'max:2500'],
        'description' => ['required']
    ]);
    //dd($validated_data);
    $path = Storage::disk('public')->put('photos', $request->file('path'));
    $validated_data['path'] = $path;
    //dd($validated_data);
    Photo::create($validated_data);
    return to_route('admin.photos');
})->name('photos.store');
```

Le code ci-dessus utilise l'injection de dépendances pour nous permettre d'utiliser le paramètre `$request` à l'intérieur de la fonction de rappel. 

Nous validons d'abord la requête et enregistrons le tableau résultant dans la variable `$validated_data`. Ensuite, nous utilisons les facettes `Storage` pour enregistrer le fichier dans le système de fichiers et obtenir le chemin du fichier que nous stockons dans la variable `$path`.

Enfin, nous ajoutons une clé `path` au tableau associatif et lui passons la variable `$path`. Ensuite, nous créons la ressource dans la base de données en utilisant la méthode `Photo::create` et redirigeons l'utilisateur vers la page `admin.photos` en utilisant la nouvelle fonction d'assistance `to_route()`.

Assurez-vous d'importer la classe `Request` et les facettes `Storage` en haut du fichier web.php comme suit :

```php
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

```

Maintenant, nous pouvons ajouter une nouvelle photo dans la base de données et afficher une liste de photos pour les administrateurs et les visiteurs standard.

Ensuite, nous devons compléter les opérations CRUD et permettre à l'utilisateur de modifier/mettre à jour une photo et de la supprimer.


## Comment mettre à jour les opérations

Commençons par ajouter les routes responsables de l'affichage des formulaires utilisés pour modifier la ressource et mettre à jour ses valeurs dans la base de données.

Juste en dessous des autres routes dans le groupe Admin, ajoutons le code suivant :

```php

Route::get('/photos/{photo}/edit', function(Photo $photo){
     return inertia('Admin/PhotosEdit', [
            'photo' => $photo
        ]);
})->name('photos.edit');

```

La route ci-dessus utilise l'injection de dépendances pour injecter dans la fonction la photo actuelle, sélectionnée par l'URI `/photos/{photo}/edit`. 

Ensuite, elle retourne la réponse Inertia via la fonction `inertia()` qui accepte le nom du composant `'Admin/PhotosEdit'` comme premier paramètre et un tableau associatif comme second.

Faire `['photo' => $photo]` nous permettra de passer le modèle `$photo` en tant que prop au composant plus tard.

Ensuite, ajoutons le nouveau composant Page sous `resources/js/Pages/Admin/PhotosEdit.vue`

Voici son template :

```html
<template>
    <app-layout title="Edit Photo">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">Edit Photo</h2>
        </template>
        <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
                <form @submit.prevent="form.post(route('admin.photos.update', photo.id))">
                    <div>
                        <label
                            for="description"
                            class="block text-sm font-medium text-gray-700"
                        >Description</label>
                        <div class="mt-1">
                            <textarea
                                id="description"
                                name="description"
                                rows="3"
                                class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md"
                                placeholder="lorem ipsum"
                                v-model="form.description"
                            />
                        </div>
                        <p class="mt-2 text-sm text-gray-500">Brief description for your photo</p>
                        <div
                            class="text-red-500"
                            v-if="form.errors.description"
                        >{{ form.errors.description }}</div>
                    </div>

                    <div class="grid grid-cols-2">
                        <div class="preview p-4">
                            <img :src="'/storage/' + photo.path" alt />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Photo</label>
                            <div
                                class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md"
                            >
                                <div class="space-y-1 text-center">
                                    <svg
                                        class="mx-auto h-12 w-12 text-gray-400"
                                        stroke="currentColor"
                                        fill="none"
                                        viewBox="0 0 48 48"
                                        aria-hidden="true"
                                    >
                                        <path
                                            d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                                            stroke-width="2"
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                        />
                                    </svg>
                                    <div class="flex text-sm text-gray-600">
                                        <label
                                            for="path"
                                            class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500"
                                        >
                                            <span>Upload a file</span>
                                            <input
                                                id="path"
                                                name="path"
                                                type="file"
                                                class="sr-only"
                                                @input="form.path = $event.target.files[0]"
                                            />
                                        </label>
                                        <p class="pl-1">or drag and drop</p>
                                    </div>
                                    <p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
                                </div>
                            </div>
                            <div class="text-red-500" v-if="form.errors.path">{{ form.errors.path }}</div>
                        </div>
                    </div>

                    <button
                        type="submit"
                        :disabled="form.processing"
                        class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                    >Update</button>
                </form>
            </div>
        </div>
    </app-layout>
</template>
```

Le template est en fait identique au composant Create, à quelques exceptions près. Le formulaire pointe vers une route qui attend un paramètre que nous passons en tant que deuxième argument à la fonction `route`. Cela ressemble à ceci : `<form @submit.prevent="form.post(route('admin.photos.update', photo.id))">`.

Il y a une section où nous pouvons voir la photo originale à côté du groupe de formulaire de téléchargement :

```html
 <div class="preview p-4">
    <img :src="'/storage/' + photo.path" alt />
</div>
```

Le reste est identique, et voici la section script :

```js
import { defineComponent } from "vue";
import AppLayout from "@/Layouts/AppLayout.vue";
import { useForm } from '@inertiajs/inertia-vue3';

export default defineComponent({
    components: {
        AppLayout,
    },
    props: {
        photo: Object
    },
    setup(props) {
        const form = useForm({
            _method: "PUT",
            path: null,
            description: props.photo.description,
        })

        return { form }
    },

});
```

Remarquez que nous passons un objet props avec la clé photo, ce qui nous permet de référencer le modèle dans le template.

Ensuite, cette ligne de code `_method: "PUT",` est requise pour pouvoir soumettre une requête `PUT` au lieu de la requête `POST` appelée sur la balise de formulaire.

Maintenant, implémentons la logique pour gérer la soumission du formulaire à l'intérieur de la route ci-dessous.

Dans web.php, juste en dessous de la route précédente, ajoutons une route qui répond à la requête PUT soumise par notre formulaire.

```php
Route::put('/photos/{photo}', function (Request $request, Photo $photo)
    {
        //dd(Request::all());

        $validated_data = $request->validate([
            'description' => ['required']
        ]);

        if ($request->hasFile('path')) {
            $validated_data['path'] = $request->validate([
                'path' => ['required', 'image', 'max:1500'],

            ]);

            // Grab the old image and delete it
            // dd($validated_data, $photo->path);
            $oldImage = $photo->path;
            Storage::delete($oldImage);

            $path = Storage::disk('public')->put('photos', $request->file('path'));
            $validated_data['path'] = $path;
        }

        //dd($validated_data);

        $photo->update($validated_data);
        return to_route('admin.photos');
    })->name('photos.update');


```

La logique de la route est simple. D'abord, nous validons la description, ensuite nous vérifions si un fichier a été téléchargé et si c'est le cas, nous le validons. 

Ensuite, nous supprimons l'image précédemment téléchargée `Storage::delete($oldImage);` avant de stocker la nouvelle image dans la base de données et de mettre à jour la ressource en utilisant `$photo->update($validated_data);`.

Comme avant avec la route de stockage, nous redirigeons vers la route `admin.photos` en utilisant `return to_route('admin.photos');`.



## Comment supprimer une ressource

La dernière étape que nous devons franchir est d'écrire la logique pour supprimer la photo. Commençons par ajouter la route.

Juste en dessous de la route précédente, nous pouvons écrire :

```php
Route::delete('/photos/{photo}', function (Photo $photo)
{
    Storage::delete($photo->path);
    $photo->delete();
    return to_route('admin.photos');
})->name('photos.delete');
```

Cette route utilise également un joker dans son URI pour identifier la ressource. Ensuite, son deuxième paramètre est le rappel qui utilise l'injection de dépendances comme précédemment. À l'intérieur du rappel, nous supprimons d'abord l'image du système de fichiers en utilisant `Storage::delete($photo->path);`.

Ensuite, nous supprimons la ressource de la base de données `$photo->delete();` et redirigeons l'utilisateur en arrière `return to_route('admin.photos');` comme nous l'avons fait dans la route précédente.

Maintenant, nous devons ajouter un bouton de suppression au tableau que nous avons créé dans l'une des étapes précédentes pour afficher toutes les photos.

À l'intérieur de la section template du composant `Admin/Photos.vue` dans la boucle `v-for`, nous pouvons ajouter ce bouton Jetstream :

```html

<jet-danger-button @click="delete_photo(photo)">
    Delete
</jet-danger-button>

```

Trouvez la cellule du tableau qui a le commentaire `ACTIONS` et remplacez le texte `DELETE` par le bouton ci-dessus.

Ainsi, le code final sera :

```html
<td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
    <a href="#" class="text-indigo-600 hover:text-indigo-900">
    View - Edit - 

    <jet-danger-button @click="delete_photo(photo)">
        Delete
    </jet-danger-button>
    </a>
</td>
```

Comme vous pouvez le voir, il y a un écouteur d'événement `@click` sur le bouton. Il appelle une méthode `delete_photo(photo)` que nous devons définir ainsi qu'un ensemble d'autres méthodes pour avoir une belle fenêtre modale qui s'ouvre pour demander confirmation à l'utilisateur.

Tout d'abord, importez la fonction d'assistance Inertia useForm :

```js
// 0. Importer la classe useForm en haut de la section script avec tous les composants requis
import { useForm } from '@inertiajs/inertia-vue3';
import JetDangerButton from '@/Jetstream/DangerButton.vue'
import { ref } from "vue";
```

N'oubliez pas d'enregistrer le composant `JetDangerButton` dans l'objet components avant de continuer.

Ensuite, ajoutez la fonction `setup()` dans la section script et implémentez la logique requise pour soumettre le formulaire et afficher une fenêtre modale. Les commentaires dans le code vous guideront tout au long des étapes.

```js
// 1. ajouter la fonction setup
setup() {
    // 2. déclarer une variable form et lui assigner la fonction d'assistance useForm() d'Inertia 
    const form = useForm({
        // 3. remplacer la méthode du formulaire pour faire une requête DELETE
        _method: "DELETE",
    });
    // 4. définir un objet réactif avec les propriétés show_modal et photo
    // cela sera utilisé pour déterminer quand afficher la fenêtre modale et les valeurs de la publication sélectionnée
    const data = ref({
        show_modal: false,
        photo: {
            id: null,
            path: null,
            description: null,
        }
    })

    // 5. définir la fonction delete_photo et mettre à jour les valeurs des propriétés show_modal et photo
    // de l'objet réactif défini ci-dessus. Cette méthode est appelée par le bouton de suppression et enregistrera les détails 
    // de la publication sélectionnée
    const delete_photo = (photo) => {
        //console.log(photo);
        //console.log(photo.id, photo.path, photo.description);
        data.value = {
            photo: {
                id: photo.id,
                path: photo.path,
                description: photo.description
            },
            show_modal: true
        };
    }
    // 6. définir la méthode qui sera appelée lorsque notre formulaire de suppression sera soumis
    // le formulaire sera créé ensuite
    const deleting_photo = (id) => {
        form.post(route('admin.photos.delete', id))
        closeModal();
    }
    // 7. déclarer une méthode pour fermer la fenêtre modale en définissant show_modal sur false
    const closeModal = () => {
        data.value.show_modal = false;
    }
    // 8. n'oubliez pas de retourner de la fonction setup toutes les variables et méthodes que vous souhaitez exposer 
    // au template.
    return { form, data, closeModal, delete_photo, deleting_photo }

}
```

Enfin, en dehors de la boucle `v-for`, ajoutez la fenêtre modale en utilisant le code suivant. Vous pouvez placer cela où vous voulez mais pas à l'intérieur de la boucle.

```html

 <JetDialogModal :show="data.show_modal">
    <template #title>
        Photo {{ data.photo.description.slice(0, 20) + '...' }}
    </template>
    <template #content>
        Are you sure you want to delete this photo?

    </template>
    <template #footer>
        <button @click="closeModal" class="px-4 py-2">Close</button>
        <form @submit.prevent="deleting_photo(data.photo.id)">
            <jet-danger-button type="submit">Yes, I am sure!</jet-danger-button>
        </form>
    </template>
</JetDialogModal>

```

Voici notre code JavaScript final :

```js
import { defineComponent } from "vue";
import AppLayout from "@/Layouts/AppLayout.vue";
import TableComponent from "@/Components/TableComponent.vue";
import { Link } from '@inertiajs/inertia-vue3';
import { useForm } from '@inertiajs/inertia-vue3';
import JetDialogModal from '@/Jetstream/DialogModal.vue';
import JetDangerButton from '@/Jetstream/DangerButton.vue'
import { ref } from "vue";
export default defineComponent({
    components: {
        AppLayout,
        Link,
        TableComponent,
        JetDialogModal,
        JetDangerButton
    },
    props: {
        photos: Array,
    },

    setup() {

        const form = useForm({
            _method: "DELETE",
        });
        const data = ref({
            show_modal: false,
            photo: {
                id: null,
                path: null,
                description: null,
            }

        })


        const delete_photo = (photo) => {
            //console.log(photo);
            console.log(photo.id, photo.path, photo.description);
            data.value = {
                photo: {
                    id: photo.id,
                    path: photo.path,
                    description: photo.description
                },
                show_modal: true
            };
        }
        const deleting_photo = (id) => {
            form.post(route('admin.photos.delete', id))
            closeModal();
        }

        const closeModal = () => {
            data.value.show_modal = false;


        }

        return { form, data, closeModal, delete_photo, deleting_photo }

    }
});
</script>
```

Et voici le HTML :

```html
<template>
    <app-layout title="Dashboard">
        <template #header>
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">Photos</h2>
        </template>

         <div class="py-12">
            <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
              <!-- Tous les posts vont ici -->
              <h1 class="text-2xl">Photos</h1>
              <a class="px-4 bg-sky-900 text-white rounded-md" href>Create</a>
              <div class="flex flex-col">
                  <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                          <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
                              <table class="min-w-full divide-y divide-gray-200">
                                  <thead class="bg-gray-50">
                                      <tr>
                                          <th
                                              scope="col"
                                              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                                          >ID</th>
                                          <th
                                              scope="col"
                                              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                                          >Photos</th>
                                          <th
                                              scope="col"
                                              class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                                          >Description</th>
                                          <th scope="col" class="relative px-6 py-3">
                                              <span class="sr-only">Edit</span>
                                          </th>
                                      </tr>
                                  </thead>
                                  <tbody class="bg-white divide-y divide-gray-200">
                                      <tr v-for="photo in photos" :key="photo.id">
                                          <td class="px-6 py-4 whitespace-nowrap">
                                              <div
                                                  class="text-sm text-gray-900"
                                              >{{ photo.id }}</div>
                                          </td>

                                          <td class="px-6 py-4 whitespace-nowrap">
                                              <div class="flex items-center">
                                                  <div class="flex-shrink-0 h-10 w-10">
                                                      <img
                                                          class="h-10 w-10 rounded-full"
                                                          :src="photo.path"
                                                          alt
                                                      />
                                                  </div>
                                              </div>
                                          </td>

                                          <td class="px-6 py-4 whitespace-nowrap">
                                              <div class="text-sm text-gray-900">
                                                {{ photo.description.slice(0, 100) + '...' }}
                                              </div>
                                          </td>
                                        <!-- ACTIONS -->
                                         <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                            <a href="#" class="text-indigo-600 hover:text-indigo-900">
                                            View - Edit - 

                                            <jet-danger-button @click="delete_photo(photo)">
                                                Delete
                                            </jet-danger-button>
                                            </a>
                                        </td>
                                      </tr>
                                  </tbody>
                              </table>
                          </div>
                      </div>
                  </div>
                </div>
            </div>
        </div>
         <JetDialogModal :show="data.show_modal">
            <template #title>
                Photo {{ data.photo.description.slice(0, 20) + '...' }}
            </template>
            <template #content>
                Are you sure you want to delete this photo?

            </template>
            <template #footer>
                <button @click="closeModal" class="px-4 py-2">Close</button>
                <form @submit.prevent="deleting_photo(data.photo.id)">
                    <jet-danger-button type="submit">Yes, I am sure!</jet-danger-button>
                </form>
            </template>
        </JetDialogModal>
    </app-layout>
</template>

```

C'est tout. Si vous avez tout fait correctement, vous devriez être en mesure de voir toutes les photos, de créer de nouvelles photos ainsi que de les modifier et de les supprimer.

Je vais vous laisser un peu de travail à faire. Pouvez-vous déterminer comment implémenter les liens de visualisation et d'édition avant le bouton de suppression dans la section ci-dessous ?

```html
<!-- ACTIONS -->
<td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
    <a href="#" class="text-indigo-600 hover:text-indigo-900">
    View - Edit - 

    <jet-danger-button @click="delete_photo(photo)">
        Delete
    </jet-danger-button>
    </a>
</td>
```



## Conclusion et prochaines étapes

Au cours de ce guide, nous avons fait nos premiers pas et appris à construire une application monopage en utilisant Laravel comme framework backend et Vue3 pour le frontend. Nous les avons collés ensemble avec Inertia js et construit une application photo simple qui permet à un utilisateur de gérer des photos. 

Nous ne sommes qu'au début d'un voyage fantastique. Apprendre de nouvelles technologies n'est pas facile, mais grâce à leur documentation exhaustive, nous pouvons suivre et construire des applications incroyables. 

Votre prochaine étape pour maîtriser Laravel, Vue3, Inertia et toutes les technologies que nous avons utilisées jusqu'à présent est de consulter leur documentation et de continuer à apprendre. Utilisez l'application que nous avons construite si vous le souhaitez, et améliorez-la ou recommencez depuis le début. 

Gardez simplement à l'esprit que coder est amusant, alors détendez-vous et profitez-en.

%[https://youtube.com/playlist?list=PL-qez5yxvgfgRDUG7P850dMAmwGZLlJj3]

## Conclusion

Ce n'est qu'un aperçu de la manière dont je construirais une application monopage en utilisant ces technologies.

Si vous êtes familier avec le routage côté serveur et Vuejs, alors vous apprécierez la construction d'une application monopage avec Laravel, Inertia et Vuejs. La courbe d'apprentissage n'est pas si raide et vous avez une excellente documentation pour vous aider.

J'espère que vous avez apprécié ce guide. Si c'est le cas, faites-le moi savoir et envisagez de vous abonner à ma chaîne YouTube et de me suivre sur Twitter. Et si vous êtes bloqué, contactez-moi pour obtenir de l'aide.

Vous pouvez trouver le code source de ce guide [ici](https://bitbucket.org/fbhood/spa-with-laravel-9/src/master/).

[Suivez-moi sur Twitter](https://twitter.com/Fab_Sky_Walker)
[Rejoignez-moi sur slack](https://join.slack.com/t/fabiopacificicom/shared_invite/zt-rf4vwvcm-esx1RkokwrJ93yyr1rPpVQ)