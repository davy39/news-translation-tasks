---
title: Une introduction à la programmation orientée objet avec Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T03:29:08.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-object-oriented-programming-with-ruby-73531e2b8ddc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YCQfbNxV9hutPmznUcRA4Q.jpeg
tags:
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction à la programmation orientée objet avec Ruby
seo_desc: 'By Nishant Mishra

  As a computer science student, I spend a lot of time learning and playing with new
  languages. Every new language has something unique to offer. Having said that, most
  beginners start off their programming journey with either procedu...'
---

Par Nishant Mishra

En tant qu'étudiant en informatique, je passe beaucoup de temps à apprendre et à jouer avec de nouveaux langages. Chaque nouveau langage a quelque chose d'unique à offrir. Cela dit, la plupart des débutants commencent leur voyage en programmation soit avec des langages procéduraux comme C, soit avec des langages orientés objet comme JavaScript et C++.

Par conséquent, il est logique de passer en revue les bases de la programmation orientée objet afin que vous puissiez comprendre les concepts et les appliquer facilement aux langages que vous apprenez. Nous utiliserons le langage de programmation Ruby comme exemple.

Vous vous demandez peut-être, pourquoi Ruby ? Parce qu'il est "conçu pour rendre les programmeurs heureux" et aussi parce que presque tout en Ruby est un objet.

### Comprendre le paradigme orienté objet (OOP)

En OOP, nous identifions les "choses" que notre programme gère. En tant qu'êtres humains, nous pensons aux choses comme à des objets avec des attributs et des comportements, et nous interagissons avec les choses en fonction de ces attributs et comportements. Une chose peut être une voiture, un livre, etc. De telles choses deviennent des classes (les plans des objets), et nous créons des objets à partir de ces classes.

Chaque instance (objet) contient des variables d'instance qui représentent l'état de l'objet (attributs). Les comportements des objets sont représentés par des méthodes.

Prenons l'exemple d'une voiture. Une voiture est une chose qui en ferait une **classe**. Un type spécifique de voiture, disons BMW, est un **objet** de la classe Car. Les **attributs/propriétés** d'une BMW, comme la couleur et le numéro de modèle, peuvent être stockés dans des variables d'instance. Et si vous souhaitez effectuer une opération sur l'objet, comme conduire, alors "drive" décrit un comportement qui est défini comme une **méthode**.

### Une leçon rapide de syntaxe

* Pour terminer une ligne dans un programme Ruby, un point-virgule (;) est facultatif (mais généralement non utilisé)
* Une indentation de 2 espaces pour chaque niveau imbriqué est encouragée (non requise, comme c'est le cas en Python)
* Aucune accolade `{}` n'est utilisée, et le mot-clé **end** est utilisé pour marquer la fin d'un bloc de contrôle de flux
* Pour commenter, nous utilisons le symbole `#`

La manière dont les objets sont créés en Ruby est en appelant une méthode **new** sur une classe, comme dans l'exemple ci-dessous :

```
class Car  def initialize(name, color)    @name = name    @color = color  end
```

```
  def get_info    "Name: #{@name}, and Color: #{@color}"  endend
```

```
my_car = Car.new("Fiat", "Red")puts my_car.get_info
```

Pour comprendre ce qui se passe dans le code ci-dessus :

* Nous avons une classe nommée `Car` avec deux méthodes, `initialize` et `get_info`.
* Les variables d'instance en Ruby commencent par `@` (par exemple `@name`). La partie intéressante est que les variables ne sont pas déclarées initialement. Elles apparaissent à l'existence lorsqu'elles sont utilisées pour la première fois, et après cela, elles sont disponibles pour toutes les méthodes d'instance de la classe.
* L'appel de la méthode `new` provoque l'invocation de la méthode `initialize`. `initialize` est une méthode spéciale qui est utilisée comme constructeur.

#### Accéder aux données

Les variables d'instance sont privées et ne peuvent pas être accessibles depuis l'extérieur de la classe. Afin d'y accéder, nous devons créer des méthodes. Les méthodes d'instance ont un accès public par défaut. Nous pouvons limiter l'accès à ces méthodes d'instance comme nous le verrons plus tard dans cet article.

Afin d'obtenir et de modifier les données, nous avons besoin de méthodes "getter" et "setter", respectivement. Regardons ces méthodes en prenant le même exemple d'une voiture.

```
class Car  def initialize(name, color) # "Constructeur"    @name = name    @color = color  end
```

```
  def color    @color  end
```

```
  def color= (new_color)    @color = new_color  endend
```

```
my_car = Car.new("Fiat", "Red")puts my_car.color # Red
```

```
my_car.color = "White"puts my_car.color # White
```

En Ruby, le "getter" et le "setter" sont définis avec le même nom que la variable d'instance que nous traitons.

Dans l'exemple ci-dessus, lorsque nous disons `my_car.color`, cela appelle en réalité la méthode `color` qui retourne à son tour le nom de la couleur.

_Note : Faites attention à la manière dont Ruby permet un espace entre le_ `color` _et le **signe égal** lors de l'utilisation du setter, même si le nom de la méthode est_ `color=`

L'écriture de ces méthodes getter/setter nous permet d'avoir plus de contrôle. Mais la plupart du temps, obtenir la valeur existante et définir une nouvelle valeur est simple. Il devrait donc y avoir une manière plus facile au lieu de définir réellement des méthodes getter/setter.

#### La manière plus facile

En utilisant la forme `attr_*` à la place, nous pouvons obtenir la valeur existante et définir une nouvelle valeur.

* `attr_accessor` : pour le getter et le setter
* `attr_reader` : pour le getter uniquement
* `attr_writer` : pour le setter uniquement

Regardons cette forme en prenant le même exemple d'une voiture.

```
class Car  attr_accessor :name, :colorend
```

```
car1 = Car.newputs car1.name # => nil
```

```
car1.name = "Suzuki"car1.color = "Gray"puts car1.color # =&gt; Gray
```

```
car1.name = "Fiat"puts car1.name # =&gt; Fiat
```

De cette manière, nous pouvons sauter les définitions getter/setter complètement.

#### Parlons des bonnes pratiques

Dans l'exemple ci-dessus, nous n'avons pas initialisé les valeurs pour les variables d'instance `@name` et `@color`, ce qui n'est pas une bonne pratique. De plus, comme les variables d'instance sont définies à nil, l'objet `car1` n'a aucun sens. Il est toujours bon de définir les variables d'instance en utilisant un constructeur comme dans l'exemple ci-dessous.

```
class Car  attr_accessor :name, :color    def initialize(name, color)    @name = name    @color = color  endend
```

```
car1 = Car.new("Suzuki", "Gray")puts car1.color # =&gt; Gray
```

```
car1.name = "Fiat"puts car1.name # =&gt; Fiat
```

### Méthodes de classe et variables de classe

Les méthodes de classe sont invoquées sur une classe, et non sur une instance de classe. Celles-ci sont similaires aux méthodes **statiques** en Java.

_Note : `self` en dehors de la définition de méthode fait référence à l'objet de classe. Les variables de classe commencent par `@@`_

Il existe en réalité trois façons de définir des méthodes de classe en Ruby :

#### À l'intérieur de la définition de classe

1. En utilisant le mot-clé self avec le nom de la méthode :

```
class MathFunctions  def self.two_times(num)    num * 2  endend
```

```
# Aucune instance crééeputs MathFunctions.two_times(10) # =&gt; 20
```

2. En utilisant `<<`; self

```
class MathFunctions  class << self    def two_times(num)      num * 2    end  endend
```

```
# Aucune instance crééeputs MathFunctions.two_times(10) # =&gt; 20
```

#### À l'extérieur de la définition de classe

3. En utilisant le nom de classe avec le nom de méthode

```
class MathFunctionsend
```

```
def MathFunctions.two_times(num)  num * 2end
```

```
# Aucune instance crééeputs MathFunctions.two_times(10) # =&gt; 20
```

### Héritage de classe

En Ruby, chaque classe hérite implicitement de la classe Object. Regardons un exemple.

```
class Car  def to_s    "Car"  end
```

```
  def speed    "Top speed 100"  endend
```

```
class SuperCar < Car  def speed # Redéfinition    "Top speed 200"  endend
```

```
car = Car.newfast_car = SuperCar.new
```

```
puts "#{car}1 #{car.speed}" # =&gt; Car1 Top speed 100puts "#{fast_car}2 #{fast_car.speed}" # => Car2 Top speed 200
```

Dans l'exemple ci-dessus, la classe `SuperCar` redéfinit la méthode `speed` qui est héritée de la classe `Car`. Le symbole `&`lt; désigne l'héritage.

_Note : Ruby ne supporte pas l'héritage multiple, et donc les mix-ins sont utilisés à la place. Nous en discuterons plus tard dans cet article._

### Modules en Ruby

Un module Ruby est une partie importante du langage de programmation Ruby. C'est une caractéristique majeure orientée objet du langage et supporte l'héritage multiple indirectement.

Un module est un conteneur pour les classes, méthodes, constantes, ou même d'autres modules. Comme une classe, un module ne peut pas être instancié, mais sert deux principaux objectifs :

* Espace de noms
* Mix-in

#### Modules comme espace de noms

Beaucoup de langages comme Java ont l'idée de la structure de package, juste pour éviter les collisions entre deux classes. Regardons un exemple pour comprendre comment cela fonctionne.

```
module Patterns  class Match    attr_accessor :matched  endend
```

```
module Sports  class Match    attr_accessor :score  endend
```

```
match1 = Patterns::Match.newmatch1.matched = "true"
```

```
match2 = Sports::Match.newmatch2.score = 210
```

Dans l'exemple ci-dessus, comme nous avons deux classes nommées `Match`, nous pouvons les différencier et prévenir les collisions en les encapsulant simplement dans différents modules.

#### Modules comme Mix-in

Dans le paradigme orienté objet, nous avons le concept d'Interfaces. Mix-in fournit un moyen de partager du code entre plusieurs classes. Non seulement cela, mais nous pouvons également inclure les modules intégrés comme `Enumerable` et rendre notre tâche beaucoup plus facile. Regardons un exemple.

```
module PrintName  attr_accessor :name  def print_it    puts "Name: #{@name}"  endend
```

```
class Person  include PrintNameend
```

```
class Organization  include PrintNameend
```

```
person = Person.newperson.name = "Nishant"puts person.print_it # =&gt; Name: Nishant
```

```
organization = Organization.neworganization.name = "freeCodeCamp"puts organization.print_it # =&gt; Name: freeCodeCamp 
```

Les mix-ins sont extrêmement puissants, car nous écrivons le code une seule fois et pouvons ensuite les inclure où nous le souhaitons.

### Portée en Ruby

Nous verrons comment la portée fonctionne pour :

* variables
* constantes
* blocs

#### Portée des variables

Les méthodes et les classes définissent une nouvelle portée pour les variables, et les variables de portée externe ne sont pas transmises à la portée interne. Voyons ce que cela signifie.

```
name = "Nishant"
```

```
class MyClass  def my_fun    name = "John"    puts name # =&gt; John  end
```

```
puts name # =&gt; Nishant
```

La variable `name` externe et la variable `name` interne ne sont pas les mêmes. La variable `name` externe n'est pas transmise à la portée interne. Cela signifie que si vous essayez de l'imprimer dans la portée interne sans la redéfinir, une exception serait levée — **aucune telle variable n'existe**

#### Portée des constantes

Une portée interne peut voir les constantes définies dans la portée externe et peut également remplacer les constantes externes. Mais il est important de se souvenir que même après avoir remplacé la valeur de la constante dans la portée interne, la valeur dans la portée externe reste inchangée. Voyons cela en action.

```
module MyModule  PI = 3.14  class MyClass    def value_of_pi      puts PI # =&gt; 3.14      PI = "3.144444"      puts PI # => 3.144444    end  end  puts PI # =&gt; 3.14end
```

#### Portée des blocs

Les blocs héritent de la portée externe. Comprenons cela en utilisant un exemple fantastique que j'ai trouvé sur Internet.

```
class BankAccount  attr_accessor :id, :amount  def initialize(id, amount)    @id = id    @amount = amount  endend
```

```
acct1 = BankAccount.new(213, 300)acct2 = BankAccount.new(22, 100)acct3 = BankAccount.new(222, 500)
```

```
accts = [acct1, acct2, acct3]
```

```
total_sum = 0accts.each do |eachAcct|  total_sum = total_sum + eachAcct.amountend
```

```
puts total_sum # =&gt; 900
```

Dans l'exemple ci-dessus, si nous utilisons une méthode pour calculer le `total_sum`, la variable `total_sum` serait une variable totalement différente à l'intérieur de la méthode. C'est pourquoi parfois l'utilisation de blocs peut nous faire gagner beaucoup de temps.

Cela dit, une variable créée à l'intérieur du bloc n'est disponible que pour le bloc.

### Contrôle d'accès

Lors de la conception d'une classe, il est important de réfléchir à la quantité que vous exposerez au monde. Cela est connu sous le nom d'**Encapsulation**, et signifie généralement masquer la représentation interne de l'objet.

Il existe trois niveaux de contrôle d'accès en Ruby :

* **Public** - aucun contrôle d'accès n'est appliqué. Tout le monde peut appeler ces méthodes.
* **Protected** - peut être invoqué par des objets des classes définissantes ou de ses sous-classes.
* **Private** - ne peut être invoqué sauf avec un récepteur explicite.

Regardons un exemple d'Encapsulation en action :

```
class Car  def initialize(speed, fuel_eco)    @rating = speed * comfort  end
```

```
  def rating    @rating  endend
```

```
puts Car.new(100, 5).rating # =&gt; 500
```

Maintenant, comme les détails de la manière dont la note est calculée sont conservés à l'intérieur de la classe, nous pouvons la changer à tout moment sans aucun autre changement. De plus, nous ne pouvons pas définir la note depuis l'extérieur.

En parlant des moyens de spécifier le contrôle d'accès, il y en a deux :

1. Spécifier public, protected ou private et tout jusqu'au prochain mot-clé de contrôle d'accès aura ce niveau de contrôle d'accès.
2. Définir la méthode régulièrement, puis spécifier les niveaux d'accès public, private et protected et lister les méthodes séparées par des virgules (,) sous ces niveaux en utilisant des symboles de méthode.

#### Exemple de la première manière :

```
class MyClass  private    def func1      "private"    end  protected    def func2      "protected"    end  public    def func3      "Public"    endend
```

#### Exemple de la deuxième manière :

```
class MyClass  def func1    "private"  end  def func2    "protected"  end  def func3    "Public"  end  private :func1  protected :func2  public :func3end
```

_Note : Les contrôles d'accès public et private sont les plus utilisés._

### Conclusion

Ce sont les bases de la programmation orientée objet en Ruby. Maintenant, en connaissant ces concepts, vous pouvez approfondir et les apprendre en construisant des choses cool.

N'oubliez pas d'applaudir et de suivre si vous avez aimé ! Restez en contact avec moi [ici](https://www.instagram.com/nishantmishra02/).