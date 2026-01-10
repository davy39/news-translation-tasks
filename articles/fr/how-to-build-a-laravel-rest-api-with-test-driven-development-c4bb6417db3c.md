---
title: Comment construire une API REST Laravel avec le Test-Driven Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-21T16:35:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-laravel-rest-api-with-test-driven-development-c4bb6417db3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LdQEEDzAhDhjpgsJbK4s2w.jpeg
tags:
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Comment construire une API REST Laravel avec le Test-Driven Development
seo_desc: 'By Kofo Okesola

  There is a famous quote by James Grenning, one of the pioneers in TDD and Agile
  development methodologies:


  If you’re not doing test-driven development, you’re doing debug-later development
  - James Grenning


  Today we’ll be going on a ...'
---

Par Kofo Okesola

Il y a une citation célèbre de [James Grenning](https://wingman-sw.com/about), l'un des pionniers du TDD et des méthodologies de développement Agile :

> Si vous ne faites pas de développement piloté par les tests, vous faites du développement avec débogage plus tard - James Grenning

Aujourd'hui, nous allons entreprendre un voyage Laravel piloté par les tests. Nous allons créer une API REST Laravel complète avec authentification et fonctionnalités CRUD sans ouvrir Postman ou un navigateur. ?

> **Note :** Ce guide suppose que vous comprenez les concepts de base de [Laravel](https://laravel.com/docs/5.7) et [PHPUnit](https://phpunit.de/documentation.html). Si vous avez cela en tête ? Commençons.

#### Installation du projet

Commencez par créer un nouveau projet Laravel avec `composer create-project --prefer-dist laravel/laravel tdd-journey`.

Ensuite, nous devons exécuter le générateur d'authentification que nous allons utiliser, allez-y et exécutez `php artisan make:auth` puis `php artisan migrate`.

Nous n'allons pas réellement utiliser les routes et les vues générées. Pour ce projet, nous allons utiliser [jwt-auth](https://github.com/tymondesigns/jwt-auth). Alors allez-y et [installez-le](https://github.com/tymondesigns/jwt-auth/wiki/Installation) dans votre application.

> **Note :** Si vous avez des erreurs avec la commande `generate` de JWT, vous pouvez suivre [ce](https://github.com/tymondesigns/jwt-auth/issues/1298#issuecomment-330458018) correctif jusqu'à ce qu'il soit ajouté à la version stable.

Enfin, vous pouvez supprimer `ExampleTest` dans les dossiers `tests/Unit` et `tests/Feature` afin qu'il n'interfère pas avec nos résultats de test et nous sommes prêts à partir.

#### **Écrire le code**

1. Commencez par configurer votre `auth` pour utiliser le pilote JWT par défaut :

Ajoutez ensuite ce qui suit à votre fichier `routes/api.php` :

2. Maintenant que notre pilote est configuré, configurez votre modèle d'utilisateur de la même manière :

Ce que nous avons fait, c'est simplement implémenter `JWTSubject` et ajouter les méthodes requises.

3. Ensuite, nous devons ajouter nos méthodes d'authentification dans le contrôleur.

Exécutez `php artisan make:controller AuthController` et ajoutez les méthodes suivantes :

Cette étape est assez simple, tout ce que nous faisons est d'ajouter les méthodes `authenticate` et `register` à notre contrôleur. Dans la méthode `authenticate`, nous validons l'entrée, tentons une connexion et retournons le token si elle est réussie. Dans la méthode register, nous validons l'entrée, créons un nouvel utilisateur avec l'entrée et générons un token pour l'utilisateur basé sur cela.

4. Passons maintenant à la bonne partie. Testons ce que nous venons d'écrire. Générez les classes de test en utilisant `php artisan make:test AuthTest`. Dans le nouveau `tests/Feature/AuthTest`, ajoutez ces méthodes :

Les commentaires dans le code ci-dessus décrivent assez bien le code. Une chose à noter est la façon dont nous créons et supprimons l'utilisateur dans chaque test. L'idée est que les tests doivent être indépendants les uns des autres et de l'état de la base de données, idéalement.

Exécutez maintenant `$vendor/bin/phpunit` ou `$ phpunit` si vous l'avez installé globalement. L'exécution de cela devrait vous donner des assertions réussies. Si ce n'était pas le cas, vous pouvez consulter les logs, corriger et retester. C'est le beau cycle du TDD.

5. Maintenant que notre authentification fonctionne, ajoutons l'élément pour le CRUD. Pour ce tutoriel, nous allons utiliser des recettes de cuisine comme éléments CRUD, parce que, pourquoi pas ?

Commencez par créer notre migration `php artisan make:migration create_recipes_table` et ajoutez ce qui suit :

Ensuite, exécutez la migration. Maintenant, ajoutez le modèle en utilisant `php artisan make:model Recipe` et ajoutez ceci à notre modèle.

Ensuite, ajoutez cette méthode au modèle `user`.

6. Maintenant, nous avons besoin d'endpoints pour gérer nos recettes. Tout d'abord, nous allons créer le contrôleur `php artisan make:controller RecipeController`. Ensuite, modifiez le fichier `routes/api.php` et ajoutez l'endpoint `create`.

Dans le contrôleur, ajoutez également la méthode create

Générez le test de fonctionnalité avec `php artisan make:test RecipeTest` et modifiez le contenu comme suit :

Le code est assez explicite. Tout ce que nous faisons est de créer une méthode qui gère l'enregistrement d'un utilisateur et la génération de token, puis nous utilisons ce token dans la méthode `testCreate()`. Notez l'utilisation du trait `RefreshDatabase`, le trait est la manière pratique de Laravel de réinitialiser votre base de données après chaque test, ce qui est parfait pour notre petit projet.

OK, donc pour l'instant, tout ce que nous voulons vérifier est le statut de la réponse, allez-y et exécutez `$ vendor/bin/phpunit`.

Si tout se passe bien, vous devriez recevoir une erreur. ?

```
Il y a eu 1 échec :
```

```
1) Tests\Feature\RecipeTest::testCreateStatut attendu 200 mais reçu 500.Échec de l'assertion que false est true.
```

```
/home/user/sites/tdd-journey/vendor/laravel/framework/src/Illuminate/Foundation/Testing/TestResponse.php:133/home/user/sites/tdd-journey/tests/Feature/RecipeTest.php:49
```

```
ÉCHECS ! Tests : 3, Assertions : 5, Échecs : 1.
```

En regardant les fichiers de log, nous pouvons voir que le coupable est la relation `publisher` et `recipes` dans les classes `Recipe` et `User`. Laravel essaie de trouver une colonne `user_id` dans la table et de l'utiliser comme clé étrangère, mais dans notre migration, nous avons défini `publisher_id` comme clé étrangère. Maintenant, ajustez les lignes comme suit :

```
// Fichier Recipe
public function publisher(){
    return $this->belongsTo(User::class, 'publisher_id');
}
```

```
// Fichier User
public function recipes(){
    return $this->hasMany(Recipe::class, 'publisher_id');
}
```

Puis ré-exécutez le test. Si tout se passe bien, nous obtenons tous les tests en vert ! ?

```
...                                                                 3 / 3 (100%)
```

```
...
```

```
OK (3 tests, 5 assertions)
```

Maintenant, nous devons encore tester la création de la recette. Pour cela, nous pouvons vérifier le nombre de recettes de l'utilisateur. Mettez à jour votre méthode `testCreate` comme suit :

Nous pouvons maintenant remplir le reste de nos méthodes. Il est temps pour quelques changements. D'abord, notre `routes/api.php`

Ensuite, nous ajoutons les méthodes au contrôleur. Mettez à jour votre classe `RecipeController` de cette manière.

Le code et les commentaires expliquent déjà la logique de manière assez détaillée.

Enfin, notre `test/Feature/RecipeTest`

Outre le test supplémentaire, la seule autre différence était l'ajout d'un fichier utilisateur à l'échelle de la classe. Ainsi, la méthode `authenticate` ne génère pas seulement un token, mais elle définit le fichier utilisateur pour les opérations ultérieures.

Exécutez maintenant `$ vendor/bin/phpunit` et vous devriez avoir tous les tests en vert si tout est fait correctement.

#### Conclusion

Espérons que cela vous a donné un aperçu de la façon dont le TDD fonctionne dans Laravel. C'est définitivement un concept beaucoup plus large que cela, qui n'est pas lié à une méthode spécifique.

Bien que cette méthode de développement puisse sembler plus longue que la procédure habituelle **debug later**, elle est parfaite pour détecter les erreurs tôt dans votre code. Bien qu'il y ait des cas où une approche non-TDD est plus utile, c'est toujours une compétence et une habitude solides à adopter.

_L'ensemble du code pour ce guide est disponible sur Github [ici](https://github.com/kofoworola/tdd-journey). N'hésitez pas à jouer avec._

Santé !