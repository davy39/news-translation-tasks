---
title: Six méthodes de tableau Ruby que vous devez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-20T19:02:33.000Z'
originalURL: https://freecodecamp.org/news/six-ruby-array-methods-you-need-to-know-5f81c1e268ce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9AjPziZ4KGGEcq52iLMcPA.jpeg
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Six méthodes de tableau Ruby que vous devez connaître
seo_desc: 'By Amber Wilkie

  Arrays are one of the fundamental structures of programming. Being able to quickly
  manipulate and read data out of them is vital to success in building stuff with
  computers. Here are six methods you can’t do without.

  Map/Each

  These tw...'
---

Par Amber Wilkie

Les tableaux sont l'une des structures fondamentales de la programmation. Pouvoir manipuler rapidement et lire des données à partir de ceux-ci est vital pour réussir à construire des choses avec des ordinateurs. Voici six méthodes que vous ne pouvez pas ignorer.

### Map/Each

Ces deux méthodes sont très similaires. Elles vous permettent de parcourir "chaque" élément d'un tableau et de faire quelque chose avec.

Regardez un peu de code :

```ruby
array = [1, 2, 3]
effects = array.each{|x| # créer un enregistrement à partir de x }
added = array.map{ |x| x + 2 }
```

Si nous lisons `added`, nous obtiendrons `[3, 4, 5]`. Si nous lisons `effects`, nous obtiendrons toujours `[1, 2, 3]`. Voici la différence entre ces deux méthodes : `.map` retournera un **nouveau** tableau modifié, tandis que `.each` retournera le tableau original.

#### Effets secondaires dans map

Si vous êtes habitué à la programmation fonctionnelle, le `.map` de Ruby peut sembler très étrange. Regardez cet exemple. J'ai une simple classe `Event` dans mon projet :

```ruby
# nous créons un tableau d'enregistrements
2.3.0 :025 > array = [e, e2, e3]
 => [#<Event id: 1, name: nil>, #<Event id: 2, name: nil">, #<Event id: 3, name: nil>]
# jusqu'à présent tout va bien
2.3.0 :026 > new_array = array.map{|e| e.name = "a name"; e}
 => [#<Event id: 1, name: "a name">, #<Event id: 2, name: "a name">, #<Event id: 3, name: "a name">]
# oh-oh, ce n'est pas correct
2.3.0 :027 > array
 => [#<Event id: 1, name: "a name">, #<Event id: 2, name: "a name">, #<Event id: 3, name: "a name">]
```

Nous pourrions nous attendre à travailler avec une sorte de copie de nos enregistrements dans le tableau, mais ce n'est pas le cas. Tout cela pour dire : soyez prudent. Vous pouvez facilement créer des effets secondaires dans vos fonctions `.map`.

Ok, détendez-vous, c'était la partie difficile. À partir de maintenant, c'est plus facile.

### Select

`.select` vous permet de "trouver" un élément dans un tableau. Vous devez donner à `.select` une fonction qui retourne vrai ou faux, afin qu'il sache s'il doit "garder" un élément du tableau ou non.

```
2.3.0 :028 > array = ['hello', 'hi', 'goodbye']
2.3.0 :029 > array.select{|word| word.length > 3}
 => ["hello", "goodbye"]
```

Un exemple légèrement plus complexe, probablement plus proche de la manière dont vous l'utiliseriez réellement. Ajoutons `.map` à la fin pour faire bonne mesure :

```ruby
2.3.0 :030 > valid_colors = ['red', 'green', 'blue']
2.3.0 :031 > cars = [{type: 'porsche', color: 'red'}, {type: 'mustang', color: 'orange'}, {type: 'prius', color: 'blue'}]
2.3.0 :032 > cars.select{ |car| valid_colors.include?(car[:color]) }.map{ |car| car[:type]}
=> ["porsche", "prius"]
```

Oui, mes amis, vous pouvez combiner ces méthodes pour obtenir un pouvoir inimaginable. D'accord, vous pouvez probablement l'imaginer, mais c'est toujours cool.

#### Syntaxe encore plus propre : .map(&:method)

Si nous avions travaillé avec des objets voiture et pas seulement un simple hash, nous aurions pu utiliser une syntaxe plus propre. Je vais utiliser un exemple différent pour plus de brièveté. Peut-être préparons-nous cette liste de voitures pour l'envoyer dans une API et devons générer du JSON. Nous pouvons utiliser la méthode `.to_json` :

```ruby
# en utilisant la syntaxe map régulière
2.3.0 :047 > cars.select{ |car| valid_colors.include?(car[:color]) }.map{|car| car.to_json}
 => ["{\"type\":\"porsche\",\"color\":\"red\"}", "{\"type\":\"prius\",\"color\":\"blue\"}"]
# en utilisant la syntaxe plus propre
2.3.0 :046 > cars.select{|car| valid_colors.include?(car[:color]) }.map(&:to_json)
 => ["{\"type\":\"porsche\",\"color\":\"red\"}", "{\"type\":\"prius\",\"color\":\"blue\"}"]
```

### Reject

Reject est le yin au yang de `.select` :

```ruby
2.3.0 :048 > cars.reject{|car| valid_colors.include?(car[:color]) }.map{|car| car[:type]}
 => ["mustang"]
```

Au lieu de **sélectionner** les éléments de tableau que nous voulons, nous allons **rejeter** tout ce qui ne fait pas retourner vrai par notre fonction. Rappelez-vous que la **fonction à l'intérieur de notre reject** est ce qui détermine si l'élément du tableau sera retourné ou non — si c'est vrai, l'élément est retourné, sinon non.

### Reduce

Reduce a une structure plus complexe que nos autres méthodes de tableau, mais elle est généralement utilisée pour des choses assez simples en Ruby — surtout des calculs mathématiques. Nous allons prendre un tableau, puis exécuter une fonction sur chaque élément de ce tableau. Cette fois, nous nous intéressons à ce qui est retourné par les _autres éléments du tableau_. Typiquement, nous additionnons un tas de nombres :

```ruby
2.3.0 :049 > array = [1, 2, 3]
2.3.0 :050 > array.reduce{|sum, x| sum + x}
 => 6
```

Notez que nous pouvons travailler avec des chaînes de caractères de la même manière :

```ruby
2.3.0 :053 > array = ['amber', 'scott', 'erica']
2.3.0 :054 > array.reduce{|sum, name| sum + name}
 => "amberscotterica"
```

Cela peut être utile si nous regardons un tas de fiches de travail. Si nous devons additionner le total des heures travaillées, ou si nous voulons connaître la somme de toutes les donations du mois dernier. Une dernière note sur `.reduce`. Si vous travaillez avec autre chose que de simples nombres (ou chaînes de caractères), vous devrez inclure une valeur de départ comme argument :

```ruby
array = [{weekday: 'Monday', pay: 123}, {weekday: 'Tuedsay', pay: 244}]
array.reduce(0) {|sum, day| sum + day[:pay]}
 => 367
array.reduce(100) {|sum, day| sum + day[:pay]}
 => 467
```

Il existe, bien sûr, des façons plus avancées d'utiliser `.reduce`, mais cela est suffisant pour vous lancer.

### Join

Je vous offre `.join` en bonus parce que c'est tellement utile. Utilisons à nouveau nos voitures :

```ruby
2.3.0 :061 > cars.map{|car| car[:type]}.join(', ')
 => "porsche, mustang, prius"
```

`.join` est très similaire à `.reduce` sauf qu'il a une syntaxe super-propre. Il prend un argument : une chaîne qui sera insérée entre tous les éléments du tableau. `.join` crée une longue chaîne à partir de ce que vous lui donnez, même si votre tableau est composé de choses non-chaines :

```ruby
2.3.0 :062 > cars.join(', ')
 => "{:type=>\"porsche\", :color=>\"red\"}, {:type=>\"mustang\", :color=>\"orange\"}, {:type=>\"prius\", :color=>\"blue\"}"
2.3.0 :065 > events.join(', ')
 => "#<Event:0x007f9beef84a08>, #<Event:0x007f9bf0165e70>, #<Event:0x007f9beb5b9170>"
```

### Pourquoi ne pas tout combiner

Utilisons **toutes** les méthodes de tableau de cet article ensemble ! Dix jours de corvées, et le temps que chacune prend est aléatoire. Nous voulons savoir le temps total que nous passerons sur les corvées. Cela suppose que nous traîons et ignorons tout ce qui prend plus de 15 minutes. Ou que nous reportons à un autre jour tout ce qui peut être fait en moins de 5 minutes :

```ruby
days = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days.map{|day| day.odd? ? 
  {task: 'dishes', minutes: Random.rand(20)} :
  {task: 'sweep', minutes: Random.rand(20)}}
  .select{|task| task[:minutes] < 15}
  .reject{|task| task[:minutes] < 5}
  .reduce(0) {|sum, task| sum + task[:minutes]}
```

Ma réponse n'est pas pertinente car vous obtiendrez des minutes aléatoires différentes pour vos tâches. Si quelque chose ici est nouveau ou confus, lancez une console Ruby et essayez.

PS : Cette affaire `? :` sur `.map` s'appelle un `ternary`. Ce n'est qu'une instruction if-else. Je ne l'utilise ici que pour être élégant et tout mettre sur "une" ligne. Vous devriez éviter un ternaire aussi compliqué dans votre propre base de code.

À la prochaine !