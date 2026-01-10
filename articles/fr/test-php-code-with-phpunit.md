---
title: Comment tester du code PHP avec PHPUnit
subtitle: ''
author: Zubair Idris Aweda
co_authors: []
series: null
date: '2022-03-09T01:15:45.000Z'
originalURL: https://freecodecamp.org/news/test-php-code-with-phpunit
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/120480919-metal-bolts-nuts-group-drawing-technical-drafting-steel-screws-threaded-parts-with-hexagonal-head-bl--1-.png
tags:
- name: PHP
  slug: php
- name: Software Testing
  slug: software-testing
- name: unit testing
  slug: unit-testing
seo_title: Comment tester du code PHP avec PHPUnit
seo_desc: 'There are many different ways to test your software application, and unit
  testing is an important one.

  So what is unit testing and how can you do it? You''ll learn that and more in this
  article.

  What is Unit Testing?


  Unit testing is a software develo...'
---

Il existe de nombreuses façons de tester votre application logicielle, et les tests unitaires en sont un élément important.

Alors, qu'est-ce qu'un test unitaire et comment en réaliser ? Vous apprendrez cela et bien plus encore dans cet article.

## Qu'est-ce que le test unitaire ?

> Le test unitaire est un processus de développement logiciel dans lequel les plus petites parties testables d'une application, appelées unités, sont examinées individuellement et indépendamment pour le fonctionnement du processus. - [SearchSoftwareQuality](https://searchsoftwarequality.techtarget.com/definition/unit-testing#:~:text=Unit%20testing%20is%20a%20software,developers%20and%20sometimes%20QA%20staff.)

En termes simples, le test unitaire signifie que vous décomposez votre application en ses éléments les plus simples et que vous testez ces petits morceaux pour vous assurer que chaque partie est exempte d'erreurs (et sécurisée).

Ces tests sont automatisés et écrits par des ingénieurs logiciels dans le cadre de leur processus de développement. C'est une étape très importante pendant le développement car elle aide les développeurs à créer de meilleures applications avec moins de bugs.

## Qu'est-ce que PHPUnit ?

Vous pouvez effectuer des tests unitaires en PHP avec [PHPUnit](https://phpunit.de), un Framework de test orienté programmeur pour PHP. PHPUnit est une instance de l'architecture xUnit pour les frameworks de tests unitaires. Il est très facile à installer et à prendre en main.

## Installation de PHPUnit

Vous pouvez installer PHPUnit globalement sur votre serveur. Vous pouvez également l'installer localement, par projet, au moment du développement en tant que dépendance de votre projet à l'aide de composer. Cet article expliquera comment l'utiliser par projet.

Pour commencer, créez et initialisez un nouveau projet avec composer en utilisant ces commandes :

```bash
$ mkdir test-project
$ cd test-project
$ composer init
```

La première commande crée un dossier dans votre répertoire actuel, `test-project`, et la seconde commande s'y déplace. La dernière commande lance un shell interactif.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-at-11.08.39.png)
_Invite de commande composer init_

Suivez l'invite, en remplissant les détails comme requis (les valeurs par défaut conviennent). Vous pouvez définir la description du projet, le nom de l'auteur (ou les noms des contributeurs), la stabilité minimale pour les dépendances, le type de projet, la licence et définir vos dépendances.

Vous pouvez ignorer la partie sur les dépendances, car nous n'en installons aucune. PHPUnit est censé être une `dev-dependency` car les tests dans leur ensemble ne devraient avoir lieu que pendant le développement.

Maintenant, quand l'invite demande `Would you like to define your dev dependencies (require-dev) interactively [yes]?`, appuyez sur entrée pour accepter. Tapez ensuite `phpunit/phpunit` pour installer PHPUnit en tant que `dev-dependency`.

Acceptez les autres valeurs par défaut et procédez à la génération du fichier `composer.json`. Le fichier généré devrait ressembler à ceci actuellement :

```json
{
    "name": "zubair/test-project",
    "require-dev": {
        "phpunit/phpunit": "^9.5"
    },
    "autoload": {
        "psr-4": {
            "Zubair\\TestProject\\": "src/"
        }
    },
    "authors": [
        {
            "name": "Idris Aweda Zubair",
            "email": "zubairidrisaweda@gmail.com"
        }
    ],
    "require": {}
}
```

Pour apprendre à installer PHPUnit globalement sur votre serveur, lisez [ici](https://phpunit.readthedocs.io/en/9.5/installation.html#).

## Comment écrire des tests dans PHPUnit

Écrire des tests dans PHPUnit est assez simple. Voici quelques conventions pour vous aider à démarrer :

* Pour tester une classe en PHP, vous créerez une classe de test nommée d'après cette classe. Par exemple, si j'avais une classe `User`, la classe de test s'appellerait `UserTest`.
* La classe de test, `UserTest`, héritera généralement de la classe `PHPUnit\\Framework\\TestCase`.
* Les tests individuels sur la classe sont des méthodes publiques nommées avec `test` comme préfixe. Par exemple, pour tester une méthode `sayHello` sur la classe `User`, la méthode sera nommée `testSayHello`.
* À l'intérieur de la méthode de test, par exemple `testSayHello`, vous utilisez une méthode de PHPUnit comme `assertSame` pour vérifier qu'une méthode renvoie une valeur attendue.

Une convention populaire consiste à placer tous les tests dans un répertoire `tests` et tout le code source dans le répertoire `src`.

## Exemple de test PHPUnit

Pour aider à comprendre cet article, voici un exemple de classe `User` avec des méthodes simples qui seront testées :

```php
<?php

namespace Zubair\TestProject;

use InvalidArgumentException;

class User
{
    public int $age;
    public array $favorite_movies = [];
    public string $name;

    /**
     * @param int $age
     * @param string $name
     */
    public function __construct(int $age, string $name)
    {
        $this->age = $age;
        $this->name = $name;
    }

    public function tellName(): string
    {
        return "My name is " . $this->name . ".";
    }

    public function tellAge(): string
    {
        return "I am " . $this->age . " years old.";
    }

    public function addFavoriteMovie(string $movie): bool
    {
        $this->favorite_movies[] = $movie;

        return true;
    }

    public function removeFavoriteMovie(string $movie): bool
    {
        if (!in_array($movie, $this->favorite_movies)) throw new InvalidArgumentException("Unknown movie: " . $movie);

        unset($this->favorite_movies[array_search($movie, $this->favorite_movies)]);

        return true;
    }
}

```

Cette classe utilisateur pourrait être la classe `User` de votre application de streaming de films. L'utilisateur a un nom, un âge et une liste de films favoris qui peut être mise à jour. Pour le reste de l'article, nous allons tester que toutes ces fonctionnalités fonctionnent comme prévu.

Créez une classe `UserTest` dans le dossier `tests`. Collez ceci pour commencer :

```php
<?php

namespace Zubair\TestProject;

use PHPUnit\Framework\TestCase;

final class UserTest extends TestCase
{
    // Les tests iront ici
}
```

### Tester le constructeur

Normalement, vous ne testeriez pas la méthode `__construct`. Cependant, comme nous y définissons des valeurs, il est logique de s'assurer que les valeurs sont correctement définies.

Cela semble être une chose très mineure à tester, mais c'est tout l'intérêt des tests unitaires – s'assurer que les plus petites parties de votre application fonctionnent comme prévu.

Créez une méthode `testClassConstructor` pour tester le constructeur :

```php
public function testClassConstructor()
{
    $user = new User(18, 'John');

    $this->assertSame('John', $user->name);
    $this->assertSame(18, $user->age);
    $this->assertEmpty($user->favorite_movies);
}
```

Faisons maintenant une petite pause pour voir comment exécuter les tests.

## Comment exécuter les tests dans PHPUnit

Vous pouvez exécuter tous les tests d'un répertoire en utilisant le binaire PHPUnit installé dans votre dossier vendor.

```bash
$ ./vendor/bin/phpunit --verbose tests
```

Vous pouvez également exécuter un seul test en fournissant le chemin vers le fichier de test.

```bash
$ ./vendor/bin/phpunit --verbose tests/UserTest.php
```

Vous utilisez le drapeau `--verbose` pour obtenir plus d'informations sur l'état du test.

Maintenant, nous pouvons exécuter le test et voir le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-at-13.17.54.png)
_Résultat du test_

Le résultat montre que nous avons exécuté 1 test et y avons fait 3 assertions. Nous voyons également combien de temps il a fallu pour exécuter le test, ainsi que la quantité de mémoire utilisée.

Ces assertions sont ce que PHPUnit utilise pour comparer les valeurs renvoyées par les méthodes à leur valeur attendue.

Cet exemple utilise `assertSame` pour vérifier si les propriétés `name` et `age` de l'objet utilisateur correspondent aux valeurs saisies. Il utilise également `assertEmpty` pour vérifier que le tableau `favorite_movies` est vide.

Pour voir une liste de toutes ces assertions, vous pouvez consulter la documentation de PHPUnit [ici](https://phpunit.readthedocs.io/en/9.5/assertions.html#appendixes-assertions).

Modifiez le code pour vérifier si l'âge de l'utilisateur est égal à _21_.

```php
public function testClassConstructor()
{
    $user = new User(18, 'John');

    $this->assertSame('John', $user->name);
    $this->assertSame(21, $user->age);
    $this->assertEmpty($user->favorite_movies);
} 
```

L'exécution du test à nouveau donne cette fois-ci ce résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-08-at-13.24.20.png)
_Résultat d'une assertion échouée_

Le résultat montre maintenant que nous avons exécuté 1 test, avec 2 assertions réussies, et aussi une échouée. Nous pouvons voir une explication de l'échec, montrant la valeur attendue, la valeur obtenue et la ligne d'où provient l'erreur.

### Tester tellName et tellAge

Ensuite, nous pouvons tester la méthode `tellName`. Cette méthode indique le nom d'un utilisateur sous forme de phrase. Nous pouvons donc écrire le test pour vérifier :

* Si la valeur renvoyée est une chaîne de caractères.
* Si la chaîne renvoyée contient le nom de l'utilisateur (avec ou sans sensibilité à la casse).

```php
public function testTellName()
{
    $user = new User(18, 'John');

    $this->assertIsString($user->tellName());
    $this->assertStringContainsStringIgnoringCase('John', $user->tellName());
}
```

Le test utilise les assertions `assertIsString` et `assertStringContainsStringIgnoringCase` pour vérifier respectivement que la valeur de retour est une chaîne et qu'elle contient la chaîne _John_.

La méthode `tellAge` est très similaire à `tellName` et utilise la même logique. Son test sera similaire au précédent :

```php
public function testTellAge()
{
    $user = new User(18, 'John');

    $this->assertIsString($user->tellAge());
    $this->assertStringContainsStringIgnoringCase('18', $user->tellAge());
}
```

### Tester addFavoriteMovie

Nous pouvons également tester cette méthode. Cette méthode ajoute un film à la liste des films. Pour la tester, nous pouvons vérifier si le film nouvellement ajouté est dans la liste, et si le nombre d'éléments dans la liste a effectivement augmenté.

Ce dernier point permet de confirmer que les éléments ne sont pas déplacés. De plus, comme la fonction renvoie une valeur à la fin, nous pouvons vérifier que cette valeur est également correcte.

```php
public function testAddFavoriteMovie()
{
    $user = new User(18, 'John');

    $this->assertTrue($user->addFavoriteMovie('Avengers'));
    $this->assertContains('Avengers', $user->favorite_movies);
    $this->assertCount(1, $user->favorite_movies);
}
```

Ici, nous utilisons quelques nouvelles assertions – `assertTrue`, `assertContains` et `assertCount` – pour vérifier que la valeur renvoyée est vraie, qu'elle contient la chaîne nouvellement ajoutée et que le tableau contient désormais un élément.

### Tester removeFavoriteMovie

Enfin, we can test that the method to remove a movie works.

```php
public function testRemoveFavoriteMovie()
{
    $user = new User(18, 'John');

    $this->assertTrue($user->addFavoriteMovie('Avengers'));
    $this->assertTrue($user->addFavoriteMovie('Justice League'));

    $this->assertTrue($user->removeFavoriteMovie('Avengers'));
    $this->assertNotContains('Avengers', $user->favorite_movies);
    $this->assertCount(1, $user->favorite_movies);
}
```

Ici, nous ajoutons quelques films à la liste. Ensuite, nous en supprimons un et confirmons que la fonction a renvoyé vrai. Ensuite, nous confirmons la suppression en vérifiant que la valeur n'est plus dans la liste. Enfin, nous confirmons que nous n'avons qu'un seul film dans la liste, au lieu de deux.

## Conclusion

Vous savez maintenant comment configurer PHPUnit dans vos projets et comment tester et vous assurer que vous construisez des logiciels de classe mondiale. Vous pouvez trouver tout le code de cet article [ici](https://github.com/Zubs/php-testing).

Si vous avez des questions ou des conseils pertinents, n'hésitez pas à me contacter pour les partager.

To read more of my articles or follow my work, you can connect with me on [LinkedIn](https://www.linkedin.com/in/idris-aweda-zubair-5433121a3/), [Twitter](https://twitter.com/AwedaIdris), and [Github](https://github.com/Zubs). It’s quick, it’s easy, and it’s free!