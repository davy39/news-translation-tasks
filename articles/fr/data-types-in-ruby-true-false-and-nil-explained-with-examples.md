---
title: Types de données en Ruby - True, False et Nil expliqués avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/data-types-in-ruby-true-false-and-nil-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf8740569d1a4ca352a.jpg
tags:
- name: Boolean
  slug: boolean
- name: Ruby
  slug: ruby
- name: toothbrush
  slug: toothbrush
seo_title: Types de données en Ruby - True, False et Nil expliqués avec des exemples
seo_desc: "true, false, and nil are special built-in data types in Ruby. Each of these\
  \ keywords evaluates to an object that is the sole instance of its respective class.\n\
  true.class\n => TrueClass\nfalse.class\n => FalseClass\nnil.class\n => NilClass\n\
  \ntrue and false ..."
---

`true`, `false` et `nil` sont des types de données intégrés spéciaux en Ruby. Chacun de ces mots-clés évalue un objet qui est la seule instance de sa classe respective.

```ruby
true.class
 => TrueClass
false.class
 => FalseClass
nil.class
 => NilClass
```

`true` et `false` sont les valeurs booléennes natives de Ruby. Une valeur booléenne est une valeur qui ne peut être que l'une des deux valeurs possibles : vrai ou non vrai. L'objet `true` représente la vérité, tandis que `false` représente le contraire. Vous pouvez assigner des variables à `true` / `false`, les passer à des méthodes et généralement les utiliser comme vous le feriez avec d'autres objets (tels que des nombres, des chaînes de caractères, des tableaux, des hachages).

`nil` est une valeur spéciale qui indique l'absence de valeur – c'est la manière de Ruby de se référer à « rien ». Un exemple où vous rencontrerez l'objet `nil` est lorsque vous demandez quelque chose qui n'existe pas ou ne peut pas être trouvé :

```ruby
chapeaux = ["beret", "sombrero", "beanie", "fez", "flatcap"]

chapeaux[0]
 => "beret" # le chapeau à l'index 0
chapeaux[2]
 => "beanie" # le chapeau à l'index 2
chapeaux[4]
 => "flatcap" # le chapeau à l'index 4
chapeaux[5]
 => nil # il n'y a pas de chapeau à l'index 5, l'index 5 ne contient rien (nil)
```

Zéro n'est pas rien (c'est un nombre, ce qui est quelque chose). De même, les chaînes de caractères vides, les tableaux et les hachages ne sont pas rien (ce sont des objets, qui se trouvent être vides). Vous pouvez appeler la méthode `nil?` pour vérifier si un objet est nil.

```ruby
0.nil?
 => false
"".nil?
 => false
[].nil?
 => false
{}.nil?
 => false
nil.nil?
 => true
 # à partir de l'exemple ci-dessus
chapeaux[5].nil?
 => true
```

Chaque objet en Ruby a une valeur booléenne, ce qui signifie qu'il est considéré soit vrai soit faux dans un contexte booléen. Ceux considérés comme vrais dans ce contexte sont « truthy » et ceux considérés comme faux sont « falsey ». En Ruby, seuls `false` et `nil` sont « falsey », tout le reste est « truthy ».

## Plus d'informations :

* [Apprendre Ruby : de zéro à héros](https://www.freecodecamp.org/news/learning-ruby-from-zero-to-hero-90ad4eecc82d/)
* [Ruby idiomatique : écrire du beau code](https://www.freecodecamp.org/news/idiomatic-ruby-writing-beautiful-code-6845c830c664/)
* [Comment exporter une table de base de données vers CSV en utilisant un script Ruby simple](https://www.freecodecamp.org/news/export-a-database-table-to-csv-using-a-simple-ruby-script-2/)