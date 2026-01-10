---
title: Méthodes de chaîne Ruby expliquées - Longueur, Vide et autres méthodes intégrées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/ruby-string-methods-explained-length-empty-and-other-built-in-methods
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf1740569d1a4ca350a.jpg
tags:
- name: Ruby
  slug: ruby
- name: toothbrush
  slug: toothbrush
seo_title: Méthodes de chaîne Ruby expliquées - Longueur, Vide et autres méthodes
  intégrées
seo_desc: 'Ruby has many built in methods to work with strings. Strings in Ruby by
  default are mutable and can be changed in place or a new string can be returned
  from a method.

  Length

  The .length property returns the number of characters in a string including ...'
---

Ruby dispose de nombreuses méthodes intégrées pour travailler avec les chaînes de caractères. Les chaînes en Ruby sont par défaut mutables et peuvent être modifiées en place ou une nouvelle chaîne peut être retournée par une méthode.

## Longueur

La propriété `.length` retourne le nombre de caractères dans une chaîne, y compris les espaces blancs.

```ruby
"Hello".length #=> 5
"Hello World!".length #=> 12
```

## Vide

La méthode `.empty?` retourne `true` si une chaîne a une longueur de zéro.

```ruby
"Hello".empty? #=> false
"!".empty?     #=> false
" ".empty?     #=> false
"".empty?      #=> true
```

## Compter

La méthode `.count` compte le nombre de fois qu'un ou plusieurs caractères spécifiques sont trouvés dans une chaîne.

Cette méthode est sensible à la casse.

```ruby
"HELLO".count('L') #=> 2
"HELLO WORLD!".count('LO') #=> 1
```

## Insérer

La méthode `.insert` insère une chaîne dans une autre chaîne avant un index donné.

```ruby
"Hello".insert(3, "hi5") #=> Helhi5lo # "hi5" est inséré dans la chaîne juste avant le second 'l' qui est à l'index 3
```

## Majuscules

La méthode `.upcase` transforme toutes les lettres d'une chaîne en majuscules.

```ruby
"Hello".upcase #=> HELLO
```

## Minuscules

La méthode `.downcase` transforme toutes les lettres d'une chaîne en minuscules.

```ruby
"Hello".downcase #=> hello
```

## Inverser la casse

La méthode `.swapcase` transforme les lettres majuscules d'une chaîne en minuscules et les lettres minuscules en majuscules.

```ruby
"hELLO wORLD".swapcase #=> Hello World
```

## Capitaliser

La méthode `.capitalize` met la première lettre d'une chaîne en majuscule et le reste de la chaîne en minuscules.

```ruby
"HELLO".capitalize #=> Hello
"HELLO, HOW ARE YOU?".capitalize #=> Hello, how are you?
```

_Notez que la première lettre n'est capitalisée que si elle est au début de la chaîne._ `ruby "-HELLO".capitalize #=> -hello "1HELLO".capitalize #=> 1hello`

## Inverser

La méthode `.reverse` inverse l'ordre des caractères dans une chaîne.

```ruby
"Hello World!".reverse #=> "!dlroW olleH"
```

## Diviser

La méthode `.split` prend une chaîne et la _divise_ en un tableau, puis retourne le tableau.

```ruby
"Hello, how are you?".split #=> ["Hello,", "how", "are", "you?"]
```

La méthode par défaut divise la chaîne en fonction des espaces blancs, sauf si un séparateur différent est fourni (voir le deuxième exemple).

```ruby
"H-e-l-l-o".split('-') #=> ["H", "e", "l", "l", "o"]
```

## Supprimer le dernier caractère

La méthode `.chop` supprime le dernier caractère de la chaîne.

Une nouvelle chaîne est retournée, sauf si vous utilisez la méthode `.chop!` qui modifie la chaîne originale.

```ruby
"Name".chop #=> Nam
```

```ruby
name = "Batman"
name.chop
name == "Batma" #=> false
```

```ruby
name = "Batman"
name.chop!
name == "Batma" #=> true
```

## Supprimer les espaces

La méthode `.strip` supprime les espaces blancs au début et à la fin des chaînes, y compris les tabulations, les nouvelles lignes et les retours chariot (`\t`, `\n`, `\r`).

```ruby
"  Hello  ".strip #=> Hello
```

## Supprimer la fin de ligne

La méthode `.chomp` supprime le dernier caractère d'une chaîne, uniquement s'il s'agit d'un retour chariot ou d'une nouvelle ligne (`\r`, `\n`).

Cette méthode est couramment utilisée avec la commande `gets` pour supprimer les retours de l'entrée utilisateur.

```ruby
"hello\r".chomp #=> hello
"hello\t".chomp #=> hello\t # car les tabulations et autres espaces blancs restent intacts lors de l'utilisation de `chomp`
```

## Convertir en entier

La méthode `.to_i` convertit une chaîne en entier.

```ruby
"15".to_i #=> 15 # entier
```

## Remplacer

`gsub` remplace chaque référence du premier paramètre par le deuxième paramètre dans une chaîne.

```ruby
"ruby is cool".gsub("cool", "very cool") #=> "ruby is very cool"
```

`gsub` accepte également des motifs (comme les _expressions régulières_) comme premier paramètre, permettant des opérations comme :

```ruby
"ruby is cool".gsub(/[aeiou]/, "*") #=> "r*by *s c**l"
```

## Concaténation

Ruby implémente plusieurs méthodes pour concaténer deux chaînes ensemble.

La méthode `+` :

```ruby
"15" + "15" #=> "1515" # chaîne
```

La méthode `<<` :

```ruby
"15" << "15" #=> "1515" # chaîne
```

La méthode `concat` :

```ruby
"15".concat "15" #=> "1515" # chaîne
```

## Index

La méthode `index` retourne la position d'index de la première occurrence de la sous-chaîne ou de la correspondance du motif d'expression régulière dans une chaîne. Si aucune correspondance n'est trouvée, `nil` est retourné.

Un deuxième paramètre optionnel indique à quelle position d'index dans la chaîne commencer la recherche d'une correspondance.

```ruby
"information".index('o') #=> 3
"information".index('mat') #=> 5
"information".index(/[abc]/) #=> 6
"information".index('o', 5) #=> 9
"information".index('z') #=> nil
```

## Effacer

Supprime le contenu de la chaîne.

```ruby
a = "abcde"
a.clear    #=> ""
```