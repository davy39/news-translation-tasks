---
title: Polymorphisme avec les classes abstraites et les interfaces
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T22:18:00.000Z'
originalURL: https://freecodecamp.org/news/polymorphism-using-abstract-class-and-interface
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e02740569d1a4ca3ad9.jpg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: toothbrush
  slug: toothbrush
seo_title: Polymorphisme avec les classes abstraites et les interfaces
seo_desc: 'In this article, you''ll learn how to share and enforce code with polymorphism
  using abstract classes and interfaces.

  We will dive deeper into Object Oriented Programming and try to think in terms of
  Design Patterns to share and enforce our code using...'
---

Dans cet article, vous apprendrez à partager et à imposer du code avec le polymorphisme en utilisant des classes abstraites et des interfaces.

Nous approfondirons la programmation orientée objet et essaierons de penser en termes de modèles de conception pour partager et imposer notre code en utilisant le polymorphisme.

### **Classe Abstraite**

Supposons que nous avons une classe appelée `Man` avec certaines propriétés (`name`, `age`, `height`, `fav_drinks` et `fav_sports`) et méthodes (`giveFirmHandshakes`, `beStubborn` et `notPutToiletPaper`).

```php
<?php
 
class Man
{
    public $name;
    public $age;
    public $height;
    public $fav_sports;
    public $fav_drinks;
    
    public function __construct($name, $age, $height)
    {
        $this->name = $name;
        $this->age = $age;
        $this->height = $height;
    }
    
    public function giveFirmHandshakes()
    {
        return "I give firm handshakes.";
    }
 
    public function beStubborn()
    {
        return "I am stubborn.";
    }
 
    public function notPutToiletPaper()
    {
        return "It's not humanly possible to remember to put toilet paper rolls when they are finished";
    }
}
```

Nous devons spécifier le nom, l'âge et la taille pour instancier cette classe comme requis par le constructeur.

```php
<?php
$jack = new Man('Jack', '26', '5 Feet 6 Inches');

echo sprintf('%s - %s - %s', $jack->name, $jack->age, $jack->height);
// => Jack - 26 - 5 Feet 6 Inches
```

Maintenant, supposons que nous voulons ajouter une nouvelle méthode à cette classe appelée `isActive`.

Cette méthode vérifie si la propriété `active` est définie et retourne le message approprié en fonction de la valeur de `active`, avec une valeur par défaut de `false`. Nous pouvons la définir à `true` pour les hommes qui sont actifs.

```php
<?php
 
class Man
{
    public $name;
    public $age;
    public $height;
    public $fav_sports;
    public $fav_drinks;
    public $active = false;
    
    .....
    .....
    
    public function isActive()
    {
        if ($this->active == true) {
            return "I am an active man.";
        } else {
            return "I am an idle man.";
        }
    }
}

$jack = new Man('Jack', '26', '5 Feet 6 Inches');
$jack->active = true;
echo $jack->isActive();
// => I am an active man.

$jake = new Man('Jake', '30', '6 Feet');
echo "\n" . $jake->isActive();
// => I am an idle man.
```

Et si un homme n'est pas JUSTE actif ou inactif ?

Et s'il y a une échelle de 1 à 4 qui mesure à quel point un homme est actif (1 – inactif, 2 – légèrement actif, 3 – modérément actif, 4 – très actif) ?

Nous pouvons avoir une instruction `if..elseif..else` comme ceci :

```php
<?php

public function isActive()
{
    if ($this->active == 1) {
        return "I am an idle man.";
    } elseif ($this->active == 2) {
        return "I am a lightly active man.";
    } elseif ($this->active == 3) {
        return "I am a moderately active man.";
    } else {
        return "I am a very active man.";
    }
}
```

Maintenant, allons plus loin.

Et si la propriété `active` de `Man` n'est pas juste un entier (1, 2, 3, 4, etc) ? Et si la valeur de `active` est « athletic » ou « lazy » ?

Ne devons-nous pas ajouter plus d'instructions `elseif` pour chercher une correspondance avec ces chaînes ?

Les classes abstraites peuvent être utilisées pour un tel scénario.

Avec les classes abstraites, vous définissez essentiellement la classe comme abstraite et les méthodes que vous souhaitez imposer comme abstraites sans réellement mettre de code à l'intérieur de ces méthodes.

Ensuite, vous créez une classe enfant qui étend la classe abstraite parente et implémente les méthodes abstraites dans cette classe enfant.

De cette façon, vous imposerez à toutes les classes enfants de définir leur propre version des méthodes abstraites. Voyons comment nous pouvons définir notre méthode `isActive()` comme abstraite.

## 1 : Définir la classe comme abstraite.

```php
<?php
abstract class Man
{
.....
.....
}
```

## 2 : Créer une méthode abstraite pour la méthode que vous souhaitez imposer à l'intérieur de la classe abstraite.

```php
<?php
abstract class Man
{
.....
.....
abstract public function isActive();
}
```

## 3 : Créer une classe enfant qui étend la classe abstraite.

```php
<?php

class AthleticMan extends Man
{
.....
.....
}
```

## 4 : Implémenter la méthode abstraite à l'intérieur de la classe enfant.

```php
<?php
class AthleticMan extends Man
{
    public function isActive()
    {
        return "I am a very active athlete.";
    }
}
```

## 5 : Instancier la classe enfant (PAS la classe abstraite).

```php
<?php
$jack = new AthleticMan('Jack', '26', '5 feet 6 inches');
echo $jack->isActive();
// => I am a very active athlete.
```

Code complet de définition et d'implémentation de la classe abstraite :

```php
<?php
 
abstract class Man
{
    public $name;
    public $age;
    public $height;
    public $fav_sports;
    public $fav_drinks;
    
    public function __construct($name, $age, $height)
    {
        $this->name = $name;
        $this->age = $age;
        $this->height = $height;
    }
    
    public function giveFirmHandshakes()
    {
        return "I give firm handshakes.";
    }
 
    public function beStubborn()
    {
        return "I am stubborn.";
    }
 
    public function notPutToiletPaper()
    {
        return "It's not humanly possible to remember to put toilet paper rolls when they are finished";
    }
    
    abstract public function isActive();
}

class AthleticMan extends Man
{
    public function isActive()
    {
        return "I am a very active athlete.";
    }
}

$jack = new AthleticMan('Jack', '26', '5 feet 6 inches');
echo $jack->isActive();
// => I am a very active athlete.
```

Dans ce code, vous remarquerez que la méthode abstraite `isActive()` est définie à l'intérieur de la classe abstraite `Man` et est implémentée à l'intérieur de la classe enfant `AthleticMan`.

Maintenant, la classe `Man` ne peut pas être instanciée directement pour créer un objet.

```php
<?php
$ted = new Man('Ted', '30', '6 feet');
echo $ted->isActive();
// => Fatal error:  Uncaught Error: Cannot instantiate abstract class Man
```

De plus, chaque classe enfant de la classe abstraite (classe `Man`) doit implémenter toutes les méthodes abstraites. Le manque d'une telle implémentation entraînera une erreur fatale.

```php
<?php
class LazyMan extends Man
{
    
}

$robert = new LazyMan('Robert', '40', '5 feet 10 inches');
echo $robert->isActive();
// => Fatal error:  Class LazyMan contains 1 abstract method 
// => and must therefore be declared abstract or implement 
// => the remaining methods (Man::isActive)
```

En utilisant des classes abstraites, vous pouvez imposer certaines méthodes à être implémentées individuellement par les classes enfants.

## Interface

Il existe un autre concept de programmation orientée objet qui est étroitement lié aux classes abstraites appelé Interface.

La seule différence entre les classes abstraites et les interfaces est que dans les classes abstraites, vous pouvez avoir un mélange de méthodes définies (`giveFirmHandshakes()`, `isStubborn()`, etc.) et de méthodes abstraites (`isActive()`) à l'intérieur de la classe parente. Mais dans les interfaces, vous ne pouvez définir (et non implémenter) que les méthodes à l'intérieur de la classe parente.

Voyons comment nous pouvons convertir la classe abstraite `Man` ci-dessus en une interface.

## 1 : Définir l'interface avec toutes les méthodes (utiliser `interface` au lieu de `class`).

```php
<?php
interface Man
{
    public function __construct($name, $age, $height);
    
    public function giveFirmHandshakes();
 
    public function beStubborn();
 
    public function notPutToiletPaper();
    
    public function isActive();
}
```

## 2 : Créer une classe qui implémente l'interface (utiliser `implements` au lieu de `extends`).

Cette classe doit implémenter TOUTES les méthodes définies à l'intérieur de l'interface, y compris la méthode constructeur.

```php
<?php
class AthleticMan implements Man
{
    public $name;
    public $age;
    public $height;
    
    public function __construct($name, $age, $height)
    {
        $this->name = $name;
        $this->age = $age;
        $this->height = $height;
    }
    
    public function giveFirmHandshakes()
    {
        return "I give firm handshakes.";
    }
    
    public function beStubborn()
    {
        return "I am stubborn.";
    }
 
    public function notPutToiletPaper()
    {
        return "It's not humanly possible to remember to put toilet paper rolls when they are finished";
    }
    
    public function isActive()
    {
        return "I am a very active athlete.";
    }
}
```

## 3 : Instancier la classe d'implémentation (`AthleticMan`)

```php
<?php
$jack = new AthleticMan('Jack', '26', '5 feet 6 inches');
echo $jack->isActive();
// => I am a very active athlete.
```

Avec les interfaces, vous devez garder à l'esprit que :

* Les méthodes ne peuvent pas être implémentées à l'intérieur de l'interface.
* Les variables (propriétés) ne peuvent pas être définies à l'intérieur de l'interface.
* Toutes les méthodes définies à l'intérieur de l'interface doivent être implémentées dans la classe enfant (implémentation).
* Toutes les variables nécessaires doivent être définies à l'intérieur de la classe enfant.
* L'interface `Man` impose à ses classes d'implémentation d'implémenter toutes les méthodes de l'interface.

Alors, à quoi servent les interfaces ?

Ne pouvons-nous pas simplement créer une nouvelle classe `AthleticMan` et créer toutes les méthodes au lieu d'implémenter l'interface ?

C'est là que les _modèles de conception_ entrent en jeu.

Les interfaces sont utilisées lorsqu'il y a une classe de base (`Man`) qui veut vous imposer de faire des choses (construire un objet, `giveFirmHandshakes`, `beStubborn`, `notPutToiletPaper` et vérifier si vous êtes actif) mais ne veut pas vous dire exactement comment le faire.

Vous pouvez simplement créer des classes d'implémentation avec des implémentations comme vous le jugez approprié.

Tant que toutes les méthodes sont implémentées, l'interface `Man` ne se soucie pas de la manière dont cela est fait.

Nous avons vu comment et quand utiliser les classes abstraites et les interfaces en PHP. L'utilisation de ces concepts de POO pour avoir des classes avec des fonctionnalités différentes partageant le même « plan » de base (classe abstraite ou interface) s'appelle le polymorphisme.