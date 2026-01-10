---
title: Méthodes de nombres et opérations numériques en Ruby (avec exemples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-21T23:10:00.000Z'
originalURL: https://freecodecamp.org/news/ruby-number-methods-integer-and-float-methods-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c76740569d1a4ca3253.jpg
tags:
- name: Ruby
  slug: ruby
- name: toothbrush
  slug: toothbrush
seo_title: Méthodes de nombres et opérations numériques en Ruby (avec exemples)
seo_desc: 'Number methods in Ruby

  Ruby provides a variety of built-in methods you may use on numbers. The following
  is an incomplete list of integer and float methods.

  Even:

  Use .even? to check whether or not an integer is even. Returns a true or false boolean....'
---

## Méthodes de nombres en Ruby

Ruby fournit une variété de méthodes intégrées que vous pouvez utiliser sur les nombres. Voici une liste non exhaustive des méthodes pour les [entiers](https://ruby-doc.org/core-2.2.0/Integer.html) et les [flottants](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil).

### [Pair](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-even-3F):

Utilisez `.even?` pour vérifier si un [**entier**](https://ruby-doc.org/core-2.2.0/Integer.html) est pair. Retourne un **booléen** `true` ou `false`.

```ruby
    15.even? #=> false
    4.even?  #=> true
```

### [Impair](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-odd-3F):

Utilisez `.odd?` pour vérifier si un [**entier**](https://ruby-doc.org/core-2.2.0/Integer.html) est impair. Retourne un **booléen** `true` ou `false`.

```ruby
    15.odd? #=> true
    4.odd?  #=> false
```

### [Plafond](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil):

La méthode `.ceil` arrondit les [**flottants**](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil) **vers le haut** au nombre le plus proche. Retourne un [**entier**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    8.3.ceil #=> 9
    6.7.ceil #=> 7
```

### [Plancher](https://ruby-doc.org/core-2.2.0/Float.html#method-i-floor):

La méthode `.floor` arrondit les [**flottants**](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil) **vers le bas** au nombre le plus proche. Retourne un [**entier**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    8.3.floor #=> 8
    6.7.floor #=> 6
```

### [Suivant](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-next):

Utilisez `.next` pour retourner l'**entier** consécutif suivant.

```ruby
    15.next #=> 16
    2.next  #=> 3
    -4.next #=> -3
```

### [Précédent](https://ruby-doc.org/core-1.8.7/Integer.html#method-i-pred):

Utilisez `.pred` pour retourner l'**entier** consécutif précédent.

```ruby
    15.pred #=> 14
    2.pred  #=> 1
    (-4).pred #=> -5
```

### [Vers Chaîne](https://ruby-doc.org/core-2.4.2/Object.html#method-i-to_s):

Utiliser `.to_s` sur un nombre ([**entier**](https://ruby-doc.org/core-2.2.0/Integer.html), [**flottant**](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil), etc.) retourne une [chaîne](https://ruby-doc.org/core-2.2.0/String.html) de ce nombre.

```ruby
    15.to_s  #=> "15"
    3.4.to_s #=> "3.4"
```

### [Plus Grand Commun Diviseur](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-gcd):

La méthode `.gcd` fournit le plus grand diviseur commun (toujours positif) de deux nombres. Retourne un [**entier**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    15.gcd(5) #=> 5
    3.gcd(-7) #=> 1
```

### [Arrondi](http://ruby-doc.org/core-2.2.0/Integer.html#method-i-round):

Utilisez `.round` pour retourner un [**entier**](https://ruby-doc.org/core-2.2.0/Integer.html) ou un [**flottant**](https://ruby-doc.org/core-2.2.0/Float.html) arrondi.

```ruby
    1.round        #=> 1
    1.round(2)     #=> 1.0
    15.round(-1)   #=> 20
```

### [Fois](http://ruby-doc.org/core-2.2.0/Integer.html#method-i-times):

Utilisez `.times` pour itérer le bloc donné `int` fois.

```ruby
    5.times do |i|
      print i, " "
    end
    #=> 0 1 2 3 4
```

## Opérations mathématiques en Ruby

En Ruby, vous pouvez effectuer toutes les opérations mathématiques standard sur les nombres, y compris : l'addition `+`, la soustraction `-`, la multiplication `*`, la division `/`, trouver les restes `%`, et travailler avec les exposants `**`.

### Addition:

Les nombres peuvent être additionnés ensemble en utilisant l'opérateur `+`.

```ruby
15 + 25 #=> 40
```

### Soustraction:

Les nombres peuvent être soustraits les uns des autres en utilisant l'opérateur `-`.

```ruby
25 - 15 #=> 10
```

### Multiplication:

Les nombres peuvent être multipliés ensemble en utilisant l'opérateur `*`.

```ruby
10 * 5 #=> 50
```

### Division:

Les nombres peuvent être divisés les uns par les autres en utilisant l'opérateur `/`.

```ruby
10 / 5 #=> 2
```

### Restes:

Les restes peuvent être trouvés en utilisant l'opérateur de modulus `%`.

```ruby
10 % 3 #=> 1 # car le reste de 10/3 est 1
```

### Exposants:

Les exposants peuvent être calculés en utilisant l'opérateur `**`.

```ruby
2 ** 3 #=> 8 # car 2 à la puissance troisième, ou 2 * 2 * 2 = 8
```