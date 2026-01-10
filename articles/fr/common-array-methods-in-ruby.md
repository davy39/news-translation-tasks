---
title: Les méthodes Ruby Array les plus courantes que vous devriez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T23:54:00.000Z'
originalURL: https://freecodecamp.org/news/common-array-methods-in-ruby
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d5f740569d1a4ca376c.jpg
tags:
- name: arrays
  slug: arrays
- name: Ruby
  slug: ruby
- name: toothbrush
  slug: toothbrush
seo_title: Les méthodes Ruby Array les plus courantes que vous devriez connaître
seo_desc: 'Common Array Methods

  Ruby Arrays form a core foundation in programming in Ruby, and most languages in
  fact. It is used so much that it would be beneficial to know and even memorize some
  of the most commonly used methods for arrays. If you want to kno...'
---

## **Méthodes courantes des tableaux**

Les tableaux Ruby forment une base essentielle en programmation Ruby, et en fait dans la plupart des langages. Ils sont si fréquemment utilisés qu'il serait bénéfique de connaître et même de mémoriser certaines des méthodes les plus couramment utilisées pour les tableaux. Si vous souhaitez en savoir plus sur les tableaux Ruby, nous avons [un article à leur sujet](https://guide.freecodecamp.org/ruby/ruby-arrays).

Pour les besoins de ce guide, notre tableau sera le suivant :

```ruby
array = [0, 1, 2, 3, 4]
```

#### **.length**

La méthode .length compte le nombre d'éléments dans votre tableau et retourne le total :

```ruby
array.length
=> 5
```

#### **.first**

La méthode .first accède au premier élément du tableau, l'élément à l'index 0 :

```ruby
array.first
=> 0
```

#### **.last**

La méthode .last accède au dernier élément du tableau :

```ruby
array.last
=> 4
```

#### **.take**

La méthode .take retourne les n premiers éléments du tableau :

```ruby
array.take(3)
=> [0, 1, 2]
```

#### **.drop**

La méthode .drop retourne les éléments après les n premiers éléments du tableau :

```ruby
array.drop(3)
=> [3, 4]
```

#### **index du tableau**

Vous pouvez accéder à un élément spécifique dans un tableau en accédant à son index. Si l'index n'existe pas dans le tableau, nil sera retourné :

```ruby
array[2]
=> 2

array[5]
=> nil
```

#### **.pop**

La méthode .pop supprimera définitivement le dernier élément d'un tableau :

```ruby
array.pop
=> [0, 1, 2, 3]
```

#### **.shift**

La méthode .shift supprimera définitivement le premier élément d'un tableau et retournera cet élément :

```ruby
array.shift
=> 0  
array
=> [1, 2, 3, 4]
```

#### **.push**

La méthode .push vous permettra d'ajouter un élément à la fin d'un tableau :

```ruby
array.push(99)
=> [0, 1, 2, 3, 4, 99]
```

#### **.unshift**

La méthode .unshift vous permettra d'ajouter un élément au début d'un tableau :

```text
array = [2, 3]
array.unshift(1)
=> [1, 2, 3]
```

#### **.delete**

La méthode .delete supprime un élément spécifié d'un tableau de manière permanente :

```ruby
array.delete(1)
=> [0, 2, 3, 4]
```

#### **.delete_at**

La méthode .delete_at vous permet de supprimer définitivement un élément d'un tableau à un index spécifié :

```ruby
array.delete_at(0)
=> [1, 2, 3, 4]
```

#### **.reverse**

La méthode .reverse inverse le tableau mais ne le mute pas (le tableau original reste inchangé) :

```ruby
array.reverse
=> [4, 3, 2, 1, 0]
```

#### **.select**

La méthode .select itère sur un tableau et retourne un nouveau tableau qui inclut tous les éléments qui retournent vrai pour l'expression fournie.

```ruby
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array.select { |number| number > 4 }
=> [5, 6, 7, 8, 9, 10]
array
=> [5, 6, 7, 8, 9, 10]
```

#### **.include?**

La méthode include? vérifie si l'argument donné est inclus dans le tableau :

```ruby
array = [1, 2, 3, 4, 5]
=> [1, 2, 3, 4, 5]
array.include?(3)
=> true

#### .flatten
La méthode flatten peut être utilisée pour prendre un tableau qui contient des tableaux imbriqués et créer un tableau unidimensionnel :

``` ruby
array = [1, 2, [3, 4, 5], [6, 7]]
array.flatten
=> [1, 2, 3, 4, 5, 6, 7]
```

#### **.join**

La méthode .join retourne une chaîne de tous les éléments du tableau séparés par un paramètre séparateur. Si le paramètre séparateur est nil, la méthode utilise une chaîne vide comme séparateur entre les chaînes.

```ruby
array.join
=> "1234"
array.join("*")
=> "1*2*3*4"
```

#### **.each**

La méthode .each itère sur chaque élément du tableau, vous permettant d'effectuer des actions sur eux.

```ruby
array.each do |element|
  puts element
end
=> 
0
1
2
3
4
```

#### **.map**

La méthode .map est la même que la méthode .collect. Les méthodes .map et .collect itèrent sur chaque élément du tableau, vous permettant d'effectuer des actions sur eux. Les méthodes .map et .collect diffèrent de la méthode .each en ce sens qu'elles retournent un tableau contenant les éléments transformés.

```ruby
array.map { |element| element * 2 }
  puts element
end
=> 
0
2
4
6
8
```

#### **.uniq**

La méthode .uniq prend un tableau contenant des éléments dupliqués, et retourne une copie du tableau contenant uniquement des éléments uniques — tous les éléments dupliqués sont supprimés du tableau.

```ruby
array = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8]
array.uniq
=> [1, 2, 3, 4, 5, 6, 7, 8]
```

#### **.concat**

La méthode .concat ajoute les éléments d'un tableau au tableau original. La méthode .concat peut prendre plusieurs tableaux comme argument, ce qui ajoutera plusieurs tableaux au tableau original.

```ruby
array = [0, 1, 2, 3, 4]
array.concat([5, 6, 7], [8, 9, 10])
=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## **Plus d'informations**

* [Documentation Ruby Array](http://ruby-doc.org/core-2.5.1/Array.html)
* [Six méthodes Ruby array que vous devez connaître](https://www.freecodecamp.org/news/six-ruby-array-methods-you-need-to-know-5f81c1e268ce/)
* [Apprendre Ruby - de Zéro à Héros](https://www.freecodecamp.org/news/learning-ruby-from-zero-to-hero-90ad4eecc82d/)