---
title: 'Apprendre Ruby : De Zéro à Héros'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-12T22:26:52.000Z'
originalURL: https://freecodecamp.org/news/learning-ruby-from-zero-to-hero-90ad4eecc82d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sZSVVtdP9TE3mUoGh4GoYA.png
tags:
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Apprendre Ruby : De Zéro à Héros'
seo_desc: 'By TK


  “Ruby is simple in appearance, but is very complex inside, just like our human body.”
  — Matz, creator of the Ruby programming language


  Why learn Ruby?

  For me, the first reason is that it’s a beautiful language. It’s natural to code
  and it alw...'
---

Par TK

> « Ruby est simple en apparence, mais est très complexe à l'intérieur, tout comme notre corps humain. » — [Matz](https://twitter.com/yukihiro_matz), créateur du langage de programmation Ruby

Pourquoi apprendre Ruby ?

Pour moi, la première raison est que c'est un langage magnifique. Il est naturel à coder et il exprime toujours mes pensées.

La deuxième — et principale — raison est _Rails_ : le même framework que Twitter, Basecamp, Airbnb, Github, et tant d'autres entreprises utilisent.

### Introduction/Histoire

Ruby est « Un langage de programmation dynamique et open source avec un accent sur la simplicité et la productivité. Il a une syntaxe élégante qui est naturelle à lire et facile à écrire. » — [ruby-lang.org](https://www.ruby-lang.org/)

Commençons avec quelques bases !

### Variables

Vous pouvez penser à une variable comme un mot qui stocke une valeur. C'est aussi simple que cela.

En Ruby, il est facile de définir une variable et de lui attribuer une valeur. Imaginez que vous voulez stocker le nombre 1 dans une variable appelée one. Faisons-le !

```rb
one = 1
```

C'était simple, n'est-ce pas ? Vous venez d'attribuer la valeur 1 à une variable appelée one.

```rb
two = 2
some_number = 10000
```

Vous pouvez attribuer une valeur à n'importe quelle variable que vous voulez. Dans l'exemple ci-dessus, une variable _two_ stocke un entier de 2 et _some_number_ stocke 10 000.

En plus des entiers, nous pouvons également utiliser des booléens (vrai/faux), des chaînes de caractères, des [symboles](http://rubylearning.com/satishtalim/ruby_symbols.html), des flottants, et d'autres types de données.

```rb
# booléens
true_boolean = true
false_boolean = false

# chaîne de caractères
my_name = "Leandro Tk"

# symbole
a_symbol = :my_symbol

# flottant
book_price = 15.80
```

### Instructions Conditionnelles : Contrôle de Flux

Les instructions conditionnelles évaluent vrai ou faux. Si quelque chose est vrai, cela exécute ce qui est à l'intérieur de l'instruction. Par exemple :

```rb
if true
  puts "Hello Ruby If"
end

if 2 > 1
  puts "2 est plus grand que 1"
end
```

2 est plus grand que 1, donc le code _puts_ est exécuté.

Cette instruction else sera exécutée lorsque l'expression if est fausse :

```rb
if 1 > 2
  puts "1 est plus grand que 2"
else
  puts "1 n'est pas plus grand que 2"
end
```

1 n'est pas plus grand que 2, donc le code à l'intérieur de l'instruction else sera exécuté.

Il y a aussi l'instruction elsif. Vous pouvez l'utiliser comme ceci :

```rb
if 1 > 2
  puts "1 est plus grand que 2"
elsif 2 > 1
  puts "1 n'est pas plus grand que 2"
else
  puts "1 est égal à 2"
end
```

Une façon que j'aime vraiment pour écrire en Ruby est d'utiliser une instruction if après le code à exécuter :

```rb
def hey_ho?
  true
end

puts "let's go" if hey_ho?
```

C'est si beau et naturel. C'est du Ruby idiomatique.

### Boucles/Itérateurs

En Ruby, nous pouvons itérer de tant de façons différentes. Je vais parler de trois itérateurs : while, for et each.

Boucle While : Tant que l'instruction est vraie, le code à l'intérieur du bloc sera exécuté. Donc ce code imprimera les nombres de 1 à 10 :

```rb
num = 1

while num <= 10
  puts num
  num += 1
end
```

Boucle For : Vous passez la variable num au bloc et l'instruction for l'itérera pour vous. Ce code imprimera la même chose que le code while : de 1 à 10 :

```rb
for num in 1...10
  puts num
end
```

Itérateur Each : J'aime vraiment l'itérateur each. Pour un tableau de valeurs, il itérera une par une, en passant la variable au bloc :

```rb
[1, 2, 3, 4, 5].each do |num|
  puts num
end
```

Vous pourriez vous demander quelle est la différence entre l'itérateur each et la boucle for. La principale différence est que l'itérateur each ne maintient la variable qu'à l'intérieur du bloc d'itération, tandis que la boucle for permet à la variable de vivre en dehors du bloc.

```rb
# for vs each

# boucle for
for num in 1...5
  puts num
end

puts num # => 5

# itérateur each
[1, 2, 3, 4, 5].each do |num|
  puts num
end

puts num # => variable locale ou méthode `n' non définie pour main:Object (NameError)
```

### Tableau : Collection/List/Structure de Données

Imaginez que vous voulez stocker l'entier 1 dans une variable. Mais peut-être que maintenant vous voulez stocker 2. Et 3, 4, 5...

Ai-je un moyen de stocker tous les entiers que je veux, mais pas dans des millions de variables ? Ruby a une réponse !

Un tableau est une collection qui peut être utilisée pour stocker une liste de valeurs (comme ces entiers). Alors utilisons-le !

```rb
my_integers = [1, 2, 3, 4, 5]
```

C'est vraiment simple. Nous avons créé un tableau et l'avons stocké dans _my_integer_.

Vous pourriez vous demander, « Comment puis-je obtenir une valeur de ce tableau ? » Bonne question. Les tableaux ont un concept appelé index. Le premier élément obtient l'index 0 (zéro). Le deuxième obtient 1, et ainsi de suite. Vous avez compris l'idée !

![Image](https://cdn-media-1.freecodecamp.org/images/1*HmGUFmEI1w7ClqD6YCSmJQ.png)

En utilisant la syntaxe Ruby, c'est simple à comprendre :

```rb
my_integers = [5, 7, 1, 3, 4]
print my_integers[0] # 5
print my_integers[1] # 7
print my_integers[4] # 4
```

Imaginez que vous voulez stocker des chaînes de caractères au lieu d'entiers, comme une liste des noms de vos parents. La mienne serait quelque chose comme ceci :

```rb
relatives_names = [
  "Toshiaki",
  "Juliana",
  "Yuji",
  "Bruno",
  "Kaio"
]

print relatives_names[4] # Kaio
```

Fonctionne de la même manière que pour les entiers. Bien !

Nous venons d'apprendre comment fonctionnent les indices de tableau. Maintenant, ajoutons des éléments à la structure de données de tableau (éléments à la liste).

Les méthodes les plus courantes pour ajouter une nouvelle valeur à un tableau sont push et <<.

Push est super simple ! Vous devez simplement passer l'élément (The Effective Engineer) comme paramètre de push :

```rb
bookshelf = []
bookshelf.push("The Effective Engineer")
bookshelf.push("The 4 hours work week")
print bookshelf[0] # The Effective Engineer
print bookshelf[1] # The 4 hours work week
```

La méthode << est juste légèrement différente :

```rb
bookshelf = []
bookshelf << "Lean Startup"
bookshelf << "Zero to One"
print bookshelf[0] # Lean Startup
print bookshelf[1] # Zero to One
```

Vous pourriez demander, « Mais elle n'utilise pas la notation par point comme les autres méthodes. Comment pourrait-ce être une méthode ? » Bonne question ! Écrire ceci :

```rb
bookshelf << "Hooked"
```

... est similaire à écrire ceci :

```rb
bookshelf.<<("Hooked")
```

Ruby est si génial, n'est-ce pas ?

Bon, assez de tableaux. Parlons d'une autre structure de données.

### Hash : Structure de Données Clé-Valeur/Collection de Dictionnaire

Nous savons que les tableaux sont indexés avec des nombres. Mais que faire si nous ne voulons pas utiliser des nombres comme indices ? Certaines structures de données peuvent utiliser des indices numériques, des chaînes de caractères, ou d'autres types d'indices. La structure de données hash en est une.

Hash est une collection de paires clé-valeur. Cela ressemble à ceci :

```rb
hash_example = {
  "key1" => "value1",
  "key2" => "value2",
  "key3" => "value3"
}
```

La clé est l'index pointant vers la valeur. Comment accédons-nous à la valeur du hash ? En utilisant la clé !

Voici un hash à propos de moi. Mon nom, mon surnom et ma nationalité sont les clés du hash.

```rb
hash_tk = {
  "name" => "Leandro",
  "nickname" => "Tk",
  "nationality" => "Brazilian"
}

print "My name is #{hash_tk["name"]}" # My name is Leandro
print "But you can call me #{hash_tk["nickname"]}" # But you can call me Tk
print "And by the way I'm #{hash_tk["nationality"]}" # And by the way I'm Brazilian
```

Dans l'exemple ci-dessus, j'ai imprimé une phrase à propos de moi en utilisant toutes les valeurs stockées dans le hash.

Une autre chose cool à propos des hash est que nous pouvons utiliser n'importe quoi comme valeur. J'ajouterai la clé « age » et mon âge entier réel (24).

```rb
hash_tk = {
  "name" => "Leandro",
  "nickname" => "Tk",
  "nationality" => "Brazilian",
  "age" => 24
}

print "My name is #{hash_tk["name"]}" # My name is Leandro
print "But you can call me #{hash_tk["nickname"]}" # But you can call me Tk
print "And by the way I'm #{hash_tk["age"]} and #{hash_tk["nationality"]}" # And by the way I'm 24 and Brazilian

```

Apprenons comment ajouter des éléments à un hash. La clé pointant vers une valeur est une grande partie de ce qu'est un hash — et il en va de même lorsque nous voulons ajouter des éléments.

```rb
hash_tk = {
  "name" => "Leandro",
  "nickname" => "Tk",
  "nationality" => "Brazilian"
}

hash_tk["age"] = 24
print hash_tk # { "name" => "Leandro", "nickname" => "Tk", "nationality" => "Brazilian", "age" => 24 }

```

Nous devons simplement attribuer une valeur à une clé de hash. Rien de compliqué ici, n'est-ce pas ?

### Itération : Boucler à travers les Structures de Données

L'itération de tableau est très simple. Les développeurs Ruby utilisent couramment l'itérateur each. Faisons-le :

```rb
bookshelf = [
  "The Effective Engineer",
  "The 4 hours work week",
  "Zero to One",
  "Lean Startup",
  "Hooked"
]

bookshelf.each do |book|
  puts book
end
```

L'itérateur each fonctionne en passant les éléments du tableau comme paramètres dans le bloc. Dans l'exemple ci-dessus, nous imprimons chaque élément.

Pour la structure de données hash, nous pouvons également utiliser l'itérateur each en passant deux paramètres au bloc : la clé et la valeur. Voici un exemple :

```rb
hash = { "some_key" => "some_value" }
hash.each { |key, value| puts "#{key}: #{value}" } # some_key: some_value
```

Nous avons nommé les deux paramètres key et value, mais ce n'est pas nécessaire. Nous pouvons les nommer comme nous voulons :

```rb
hash_tk = {
  "name" => "Leandro",
  "nickname" => "Tk",
  "nationality" => "Brazilian",
  "age" => 24
}

hash_tk.each do |attribute, value|
  puts "#{attribute}: #{value}"
end
```

Vous pouvez voir que nous avons utilisé attribute comme paramètre pour la clé du hash et cela fonctionne correctement. Super !

### Classes & Objets

En tant que langage de programmation orienté objet, Ruby utilise les concepts de classe et d'objet.

« Classe » est un moyen de définir des objets. Dans le monde réel, il existe de nombreux objets du même type. Comme les véhicules, les chiens, les vélos. Chaque véhicule a des composants similaires (roues, portes, moteur).

Les « Objets » ont deux caractéristiques principales : les données et le comportement. Les véhicules ont des données comme le nombre de roues et le nombre de portes. Ils ont également un comportement comme accélérer et s'arrêter.

En programmation orientée objet, nous appelons les données « attributs » et le comportement « méthodes ».

Données = Attributs

Comportement = Méthodes

### Mode de Programmation Orientée Objet Ruby : Activé

Comprenons la syntaxe Ruby pour les classes :

```rb
class Vehicle
end
```

Nous définissons Vehicle avec l'instruction class et terminons avec end. Facile !

Et les objets sont des instances d'une classe. Nous créons une instance en appelant la méthode .new.

```rb
vehicle = Vehicle.new
```

Ici, _vehicle_ est un objet (ou instance) de la classe Vehicle.

Notre classe vehicle aura 4 attributs : Roues, type de réservoir, capacité d'assise et vitesse maximale.

Définissons notre classe Vehicle pour recevoir des données et l'instancier.

```rb
class Vehicle
  def initialize(number_of_wheels, type_of_tank, seating_capacity, maximum_velocity)
    @number_of_wheels = number_of_wheels
    @type_of_tank = type_of_tank
    @seating_capacity = seating_capacity
    @maximum_velocity = maximum_velocity
  end
end
```

Nous utilisons la méthode initialize. Nous l'appelons une méthode constructeur afin que lorsque nous créons l'objet vehicle, nous puissions définir ses attributs.

Imaginez que vous adorez la Tesla Model S et que vous voulez créer ce type d'objet. Elle a 4 roues. Son type de réservoir est l'énergie électrique. Elle a de la place pour 5 sièges et une vitesse maximale de 250 km/h (155 mph). Créons l'objet tesla_model_s ! :)

```rb
tesla_model_s = Vehicle.new(4, 'electric', 5, 250)
```

4 roues + réservoir électrique + 5 sièges + vitesse maximale de 250 km/h = tesla_model_s.

```rb
tesla_model_s
# => <Vehicle:0x0055d516903a08 @number_of_wheels=4, @type_of_tank="electric", @seating_capacity=5, @maximum_velocity=250>

```

Nous avons défini les attributs de la Tesla. Mais comment y accédons-nous ?

Nous envoyons un message à l'objet pour lui demander. Nous appelons cela une méthode. C'est le comportement de l'objet. Implémentons-le !

```rb
class Vehicle
  def initialize(number_of_wheels, type_of_tank, seating_capacity, maximum_velocity)
    @number_of_wheels = number_of_wheels
    @type_of_tank = type_of_tank
    @seating_capacity = seating_capacity
    @maximum_velocity = maximum_velocity
  end

  def number_of_wheels
    @number_of_wheels
  end

  def set_number_of_wheels=(number)
    @number_of_wheels = number
  end
end
```

Ceci est une implémentation de deux méthodes : number_of_wheels et set_number_of_wheels. Nous l'appelons « getter » et « setter ». D'abord, nous obtenons la valeur de l'attribut, et ensuite, nous définissons une valeur pour l'attribut.

En Ruby, nous pouvons faire cela sans méthodes en utilisant attr_reader, attr_writer et attr_accessor. Voyons cela avec du code !

* attr_reader : implémente la méthode getter

```rb
class Vehicle
  attr_reader :number_of_wheels

  def initialize(number_of_wheels, type_of_tank, seating_capacity, maximum_velocity)
    @number_of_wheels = number_of_wheels
    @type_of_tank = type_of_tank
    @seating_capacity = seating_capacity
    @maximum_velocity = maximum_velocity
  end
end

tesla_model_s = Vehicle.new(4, 'electric', 5, 250)
tesla_model_s.number_of_wheels # => 4
```

* attr_writer : implémente la méthode setter

```rb
class Vehicle
  attr_writer :number_of_wheels

  def initialize(number_of_wheels, type_of_tank, seating_capacity, maximum_velocity)
    @number_of_wheels = number_of_wheels
    @type_of_tank = type_of_tank
    @seating_capacity = seating_capacity
    @maximum_velocity = maximum_velocity
  end
end

# number_of_wheels equals 4
tesla_model_s = Vehicle.new(4, 'electric', 5, 250)
tesla_model_s # => <Vehicle:0x0055644f55b820 @number_of_wheels=4, @type_of_tank="electric", @seating_capacity=5, @maximum_velocity=250>

# number_of_wheels equals 3
tesla_model_s.number_of_wheels = 3
tesla_model_s # => <Vehicle:0x0055644f55b820 @number_of_wheels=3, @type_of_tank="electric", @seating_capacity=5, @maximum_velocity=250>

```

* attr_accessor : implémente les deux méthodes

```rb
class Vehicle
  attr_accessor :number_of_wheels

  def initialize(number_of_wheels, type_of_tank, seating_capacity, maximum_velocity)
    @number_of_wheels = number_of_wheels
    @type_of_tank = type_of_tank
    @seating_capacity = seating_capacity
    @maximum_velocity = maximum_velocity
  end
end

# number_of_wheels equals 4
tesla_model_s = Vehicle.new(4, 'electric', 5, 250)
tesla_model_s.number_of_wheels # => 4

# number_of_wheels equals 3
tesla_model_s.number_of_wheels = 3
tesla_model_s.number_of_wheels # => 3
```

Nous avons donc appris comment obtenir les valeurs des attributs, implémenter les méthodes getter et setter, et utiliser attr (reader, writer et accessor).

Nous pouvons également utiliser des méthodes pour faire d'autres choses — comme une méthode « make_noise ». Voyons cela !

```rb
class Vehicle
  def initialize(number_of_wheels, type_of_tank, seating_capacity, maximum_velocity)
    @number_of_wheels = number_of_wheels
    @type_of_tank = type_of_tank
    @seating_capacity = seating_capacity
    @maximum_velocity = maximum_velocity
  end

  def make_noise
    "VRRRRUUUUM"
  end
end
```

Lorsque nous appelons cette méthode, elle retourne simplement une chaîne de caractères « VRRRRUUUUM ».

```rb
v = Vehicle.new(4, 'gasoline', 5, 180)
v.make_noise # => "VRRRRUUUUM"
```

### Encapsulation : Masquer les Informations

L'encapsulation est un moyen de restreindre l'accès direct aux données et méthodes des objets. En même temps, elle facilite les opérations sur ces données (méthodes des objets).

> L'encapsulation peut être utilisée pour masquer les membres de données et les fonctions membres... L'encapsulation signifie que la représentation interne d'un objet est généralement cachée de la vue extérieure à la définition de l'objet.
> — [Wikipedia](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))

Ainsi, toute la représentation interne d'un objet est cachée de l'extérieur, seul l'objet peut interagir avec ses données internes.

En Ruby, nous utilisons des méthodes pour accéder directement aux données. Voyons un exemple :

```rb
class Person
  def initialize(name, age)
    @name = name
    @age  = age
  end
end
```

Nous venons d'implémenter cette classe Person. Et comme nous l'avons appris, pour créer l'objet person, nous utilisons la méthode new et passons les paramètres.

```rb
tk = Person.new("Leandro Tk", 24)
```

J'ai donc créé moi-même ! :) L'objet [_tk_](https://medium.com/@leandrotk_/) ! En passant mon nom et mon âge. Mais comment puis-je accéder à ces informations ? Ma première tentative est d'appeler les méthodes name et age.

```rb
tk.name
> NoMethodError: méthode non définie `name' pour #<Person:0x0055a750f4c520 @name="Leandro Tk", @age=24>
```

Nous ne pouvons pas le faire ! Nous n'avons pas implémenté la méthode name (et age).

Vous vous souvenez quand j'ai dit « En Ruby, nous utilisons des méthodes pour accéder directement aux données ? » Pour accéder au nom et à l'âge de tk, nous devons implémenter ces méthodes dans notre classe Person.

```rb
class Person
  def initialize(name, age)
    @name = name
    @age  = age
  end
  
  def name
    @name
  end
  
  def age
    @age
  end
end
```

Maintenant, nous pouvons accéder directement à ces informations. Avec l'encapsulation, nous pouvons nous assurer que l'objet (tk dans ce cas) est uniquement autorisé à accéder au nom et à l'âge. La représentation interne de l'objet est cachée de l'extérieur.

### Héritage : Comportements et Caractéristiques

Certains objets ont quelque chose en commun. Comportement et caractéristiques.

Par exemple, j'ai hérité de certaines caractéristiques et comportements de mon père — comme ses yeux et ses cheveux. Et des comportements comme l'impatience et l'introversion.

En programmation orientée objet, les classes peuvent hériter de caractéristiques communes (données) et de comportements (méthodes) d'une autre classe.

Voyons un autre exemple et implémentons-le en Ruby.

Imaginez une voiture. Le nombre de roues, la capacité d'assise et la vitesse maximale sont tous des attributs d'une voiture.

```rb
class Car
  attr_accessor :number_of_wheels, :seating_capacity, :maximum_velocity

  def initialize(number_of_wheels, seating_capacity, maximum_velocity)
    @number_of_wheels = number_of_wheels
    @seating_capacity = seating_capacity
    @maximum_velocity = maximum_velocity
  end
end
```

Notre classe Car est implémentée ! :)

```rb
my_car = Car.new(4, 5, 250)
my_car.number_of_wheels # 4
my_car.seating_capacity # 5
my_car.maximum_velocity # 250
```

Instanciée, nous pouvons utiliser toutes les méthodes créées ! Bien !

En Ruby, nous utilisons l'opérateur < pour montrer qu'une classe hérite d'une autre. Une classe ElectricCar peut hériter de notre classe Car.

```rb
class ElectricCar < Car
end
```

C'est aussi simple que cela ! Nous n'avons pas besoin d'implémenter la méthode initialize ni aucune autre méthode, car cette classe l'a déjà (héritée de la classe Car). Prouvons-le !

```rb
tesla_model_s = ElectricCar.new(4, 5, 250)
tesla_model_s.number_of_wheels # 4
tesla_model_s.seating_capacity # 5
tesla_model_s.maximum_velocity # 250
```

Magnifique !

### Module : Une Boîte à Outils

Nous pouvons penser à un module comme une boîte à outils qui contient un ensemble de constantes et de méthodes.

Un exemple de module Ruby est Math. Nous pouvons accéder à la constante PI :

```rb
Math::PI # > 3.141592653589793 
```

Et à la méthode .sqrt :

```rb
Math.sqrt(9) # 3.0
```

Et nous pouvons implémenter notre propre module et l'utiliser dans des classes. Nous avons une classe RunnerAthlete :

```rb
class RunnerAthlete
  def initialize(name)
    @name = name
  end
end
```

Et implémentons un module Skill pour avoir la méthode average_speed.

```rb
module Skill
  def average_speed
    puts "My average speed is 20mph"
  end
end
```

Comment ajoutons-nous le module à nos classes pour qu'il ait ce comportement (méthode average_speed) ? Nous l'incluons simplement !

```rb
class RunnerAthlete
  include Skill

  def initialize(name)
    @name = name
  end
end
```

Voyez le « include Skill » ! Et maintenant nous pouvons utiliser cette méthode dans notre instance de la classe RunnerAthlete.

```rub
mohamed = RunnerAthlete.new("Mohamed Farah")
mohamed.average_speed # "My average speed is 20mph"
```

Hourra ! Pour terminer avec les modules, nous devons comprendre ce qui suit :

* Un module ne peut pas avoir d'instances.
* Un module ne peut pas avoir de sous-classes.
* Un module est défini par module...end.

### Conclusion !

Nous avons appris BEAUCOUP de choses ici !

* Comment fonctionnent les variables Ruby
* Comment fonctionnent les instructions conditionnelles Ruby
* Comment fonctionnent les boucles et itérateurs Ruby
* Tableau : Collection | Liste
* Hash : Collection Clé-Valeur
* Comment nous pouvons itérer à travers ces structures de données
* Objets & Classes
* Attributs comme données des objets
* Méthodes comme comportement des objets
* Utilisation des getters et setters Ruby
* Encapsulation : masquer les informations
* Héritage : comportements et caractéristiques
* Modules : une boîte à outils

### C'est tout

Félicitations ! Vous avez terminé ce contenu dense sur Ruby ! Nous avons appris beaucoup ici. J'espère que vous l'avez aimé.

Amusez-vous, continuez à apprendre et codez toujours !

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☺