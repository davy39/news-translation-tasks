---
title: Comment utiliser les facades dans Laravel
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-12-08T19:32:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-facades-in-laravel
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95ff740569d1a4ca0f32.jpg
tags:
- name: framework
  slug: framework
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: Comment utiliser les facades dans Laravel
seo_desc: 'Facades are one of the key things you should understand when learning Laravel.

  It took me a considerable amount of time to figure out how facades work, and I''m
  writing this to help anyone who is having trouble wrapping their heads around the
  concept....'
---

Les facades sont l'une des choses clés que vous devez comprendre lorsque vous apprenez Laravel.

Il m'a fallu un temps considérable pour comprendre comment fonctionnent les facades, et j'écris ceci pour aider toute personne qui a du mal à saisir le concept.

Dans cet article, nous allons couvrir ce que sont les facades, comment elles sont utilisées dans Laravel, comment vous pouvez créer votre propre facade simple, et plus encore.

## Qu'est-ce qu'une facade ? Et qu'est-ce qu'un wrapper ?

Une facade dans Laravel est un wrapper autour d'une fonction non statique qui la transforme en une fonction statique.

Le mot "wrapper" peut également être utilisé lors de la description des design patterns. Envelopper un objet pour fournir une interface simplifiée est souvent décrit comme le pattern "facade".

Donc, en résumé, le [wrapper](https://en.wikipedia.org/wiki/Wrapper_function) est la facade.

Avant de plonger plus profondément dans les facades, il est important de comprendre ce que sont les fonctions statiques et non statiques en PHP.

### Méthodes statiques

Dans les méthodes statiques, nous ne sommes pas obligés de créer une instance de classe pour y faire référence. Les méthodes statiques utilisent des doubles deux-points (::) lors de l'accès aux propriétés ou méthodes d'une classe :

```php
<?php
class Calc {
    const GOLDEN_RATIO = '1.618';
}

echo Calc::GOLDEN_RATIO;  //1.618


```

Les mots-clés réservés comme `self`, `static` et `parents` sont utilisés pour référencer les propriétés ou méthodes au sein d'une classe :

```php
<?php
class backend {
	private const language = "php";
	public static function language() {
    	echo self::language;
  	}
}

backend::language();  //php


```

### Méthodes non statiques

Les méthodes non statiques nécessitent qu'une classe donnée soit instanciée. En d'autres termes, elles nécessitent une instance de la classe pour s'exécuter :

```php
<?php
class backend{

	public function language($name){
		
		echo $name;
	}

}


$test = new backend; //création d'une instance de la classe

$test->language('php'); //php
```

Maintenant que nous avons passé en revue les méthodes statiques et non statiques, nous pouvons plonger plus profondément dans les facades dans Laravel.

## Les facades Laravel

Dans le répertoire `vendors > laravel > framework > src > illuminate > support > Facades`, il y a une liste de fichiers qui sont les différentes facades fournies par défaut avec Laravel.

Voici une capture d'écran de ce à quoi ressemble la structure du répertoire dans notre éditeur :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-26-at-01.06.09.png)

Utilisons le code fonctionnel de `Log.php` pour examiner les facades plus en détail – la même explication devrait s'appliquer à toutes les facades dans toute application Laravel.

### La facade Log de Laravel

Voici le code pour la facade `Log` de Laravel :

```php
<?php

namespace Illuminate\Support\Facades;

class Log extends Facade
{
    /**
     * Obtenir le nom enregistré du composant.
     *
     * @return string
     */
    protected static function getFacadeAccessor()
    {
        return 'log';
    }
}

```

`Log` est une classe qui étend la facade de base qui provient de l'espace de noms ci-dessus.

Au sein de la classe `Log`, nous avons un modificateur d'accès protégé, `getFacadeAccessor`, et ce que cette méthode fait, c'est qu'elle retourne simplement `log`.

Le nom de cette facade, `log`, est retourné afin que nous puissions accéder à la facade nommée n'importe où dans l'application Laravel sans l'initialiser. Ainsi, nous pouvons faire quelque chose comme `Log::info('hello there');` n'importe où très facilement.

Comme vous pouvez le voir, les facades rendent le code plus facile à lire, plus organisé, et rendent les tests 10 fois plus faciles.

Depuis que j'ai appris à connaître `Log` grâce à l'un de mes collègues, c'est devenu mon outil de débogage préféré.

## Comment créer une facade dans Laravel

Dans cette section, nous allons implémenter notre propre facade. L'objectif principal ici est d'aider les apprenants à comprendre comment fonctionnent les facades Laravel.

Nous allons le faire en créant une StudentFacade qui étendra les propriétés d'une base Facade qui retourne une propriété de nom après qu'elle ait été résolue. Cette propriété de nom sera de type string et elle sera retournée chaque fois que nous instancions la classe comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-05-at-21.13.39.png)

Curieux de savoir comment nous allons y parvenir ? Suivez-moi car je vais vous guider à travers les étapes.

Nous ne créerons pas notre facade en utilisant la convention Laravel normale où nous avons un `.php file` dans `app > facade` et ensuite un autre dans les `providers` avant de finir par l'enregistrer dans le `config > app`.

Au lieu de cela, nous utiliserons le `web.php` à l'intérieur des `routes` pour cette illustration puisque nous essayons simplement de voir comment les facades fonctionnent sous le capot dans une application Laravel typique.

Commençons par ceci dans `web.php` :

```php
<?php 
class Student{
    public function students(){
        return 'Sean';
    }
}

 app()->bind('student', function(){
 	return new Student;   
 }); 
```

Nous avons créé une classe `Student`, et à l'intérieur, nous avons une méthode non statique `students` qui retourne un tableau d'étudiants.

Ensuite, nous appelons la méthode _bind_ pour qu'elle instancie toujours `new Student` afin que nous n'ayons plus besoin de le faire manuellement.

Ensuite, créons une classe de base `Facade` toujours dans le même `web.php` :

```php
 class Facade{
    public static function __callStatic($name, $args){
        return app()->make(static::getFacadeAccessor())->$name();
    }
    
    protected static function getFacadeAccessor(){
        //override take place 
    }
}
```

Toute facade que nous pourrions créer plus tard étendra les propriétés de cette facade de base.

Au sein de la classe `Facade`, nous avons une méthode magique `__callStatic` qui nous aide à résoudre le `static::getFacadeAccessor()` à partir du conteneur avec `app()->make()`. Et avec ceux-ci, nous sommes capables d'accéder à la propriété `$name`.

```php
class StudentFacade extends Facade {
	protected static function getFacadeAccessor(){
    	return 'student';
    }
}
```

Ici, `StudentFacade` hérite des propriétés de la facade de base. Ensuite, nous remplaçons `getFacadeAccessor()` et définissons la valeur de retour pour qu'elle soit ce que nous avons chaque fois que nous instancions dans le bind ci-dessus `student`.

```php
StudentFacade::students(); //output "Sean"
```

Lorsque nous essayons d'appeler la facade que nous avons créée, elle retourne "Sean" comme prévu. Maintenant, dans l'étape finale, nous devons mettre toutes ces étapes ensemble :

```php
<?php

class Student{
    public function students(){
        return 'Sean';
    }
}

 app()->bind('student', function(){
    return new Student;   
 }); 
 
 
 class Facade{
    public static function __callStatic($name, $args){
        return app()->make(static::getFacadeAccessor())->$name();
    }
    
    protected static function getFacadeAccessor(){
        //override take place 
    }
}

class StudentFacade extends Facade {
    protected static function getFacadeAccessor(){
        return 'student';
    }
}

//log or die it to the output
dd(StudentFacade::students());
```



![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screenshot-2020-12-05-at-21.13.39-1.png)

## Conclusion

J'espère qu'à la fin de cette leçon, vous avez pu élargir vos connaissances sur le fonctionnement des facades. Si vous avez des questions ou souhaitez continuer la conversation, n'hésitez pas à me tweeter.

### Références

[Tutoriel Laravel pour débutants](https://www.youtube.com/watch?v=zD2VJhOdI5c) - Bitfumes

[Qu'est-ce qu'un WRAPPER en programmation, à quoi cela aide-t-il ?](https://stackoverflow.com/questions/3293752/where-and-how-is-the-term-used-wrapper-in-programming-what-does-it-help-to-do) - Stackoverflow