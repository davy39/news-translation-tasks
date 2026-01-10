---
title: 'Ruby idiomatique : écrire un beau code'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-28T21:07:27.000Z'
originalURL: https://freecodecamp.org/news/idiomatic-ruby-writing-beautiful-code-6845c830c664
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9hd_8qR0CMZ8L0pVbFLjDw.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Ruby idiomatique : écrire un beau code'
seo_desc: 'By TK

  Ruby is a beautiful programming language.

  According to Ruby’s official web page, Ruby is a:


  “dynamic, open source programming language with a focus on simplicity and productivity.
  It has an elegant syntax that is natural to read and easy to wr...'
---

Par TK

Ruby est un langage de programmation magnifique.

Selon la [page officielle de Ruby](http://www.ruby-lang.org/en/), Ruby est un :

> ****_langage de programmation dynamique et open source avec un accent sur la simplicité et la productivité. Il a une syntaxe élégante qui est naturelle à lire et facile à écrire._

Ruby a été créé par [Yukihiro Matsumoto](https://twitter.com/yukihiro_matz), un ingénieur logiciel japonais. Depuis 2011, il est le concepteur en chef et ingénieur logiciel pour Ruby chez [Heroku](https://www.heroku.com/).

Matsumoto a souvent dit qu'il essayait **de rendre Ruby naturel, pas simple**, d'une manière qui reflète la vie.

> Ruby est simple en apparence, mais est très complexe à l'intérieur, tout comme notre corps humain — Yukihiro Matsumoto

Je ressens la même chose à propos de Ruby. C'est un langage de programmation complexe mais très naturel, avec une syntaxe belle et intuitive.

Avec un code plus intuitif et plus rapide, nous sommes capables de construire de meilleurs logiciels. Dans cet article, je vais vous montrer comment j'exprime mes pensées (alias code) avec Ruby, en utilisant des extraits de code.

### Exprimer mes pensées avec les méthodes de tableau

#### Map

Utilisez la méthode **map** pour simplifier votre code et obtenir ce que vous voulez.

La méthode **map** retourne un nouveau tableau avec les résultats de l'exécution d'un bloc une fois pour chaque élément dans enum.

Essayons :

```rb
an_array.map { |element| element * element }
```

Simple comme bonjour.

Mais lorsque vous commencez à coder avec Ruby, il est facile d'utiliser toujours l'itérateur **each**.

L'itérateur **each** comme montré ci-dessous

```rb
user_ids = []
users.each { |user| user_ids << user.id }
```

Peut être simplifié avec **map** en une seule belle ligne de code :

```rb
user_ids = users.map { |user| user.id }
```

Ou encore mieux (et plus rapide) :

```rb
user_ids = users.map(&:id)
```

#### Select

Et lorsque vous êtes habitué à coder avec **map**, parfois votre code peut ressembler à ceci :

```rb
even_numbers = [1, 2, 3, 4, 5].map { |element| element if element.even? } # [ni, 2, nil, 4, nil]
even_numbers = even_numbers.compact # [2, 4]
```

Utiliser **map** pour sélectionner uniquement les nombres pairs retournera également l'objet **nil**. Utilisez la méthode **compact** pour supprimer tous les objets **nil**.

Et voilà, vous avez sélectionné tous les nombres pairs.

Mission accomplie.

Allons, nous pouvons faire mieux que ça ! Avez-vous entendu parler de la méthode **select** du module enumerable ?

```rb
[1, 2, 3, 4, 5].select { |element| element.even? }
```

Juste une ligne. Code simple. Facile à comprendre.

#### **Bonus**

```rb
[1, 2, 3, 4, 5].select(&:even?)
```

#### Sample

Imaginez que vous devez obtenir un élément aléatoire d'un tableau. Vous venez de commencer à apprendre Ruby, donc votre première pensée sera, Utilisons la méthode **random**, et c'est ce qui se passe :

```rb
[1, 2, 3][rand(3)]
```

Bien, nous pouvons comprendre le code, mais je ne suis pas sûr que ce soit suffisant. Et si nous utilisions la méthode **shuffle** ?

```rb
[1, 2, 3].shuffle.first
```

Hmm. Je préfère en fait utiliser **shuffle** plutôt que **rand**. Mais lorsque j'ai découvert la méthode **sample**, cela avait beaucoup plus de sens :

```rb
[1, 2, 3].sample
```

Vraiment, vraiment simple.

Assez naturel et intuitif. Nous demandons un **sample** à un tableau et la méthode le retourne. Maintenant, je suis heureux.

Et vous ?

### Exprimer mes pensées avec la syntaxe Ruby

Comme je l'ai mentionné précédemment, j'adore la manière dont Ruby me permet de coder. C'est vraiment naturel pour moi. Je vais vous montrer des parties de la belle syntaxe Ruby.

#### Retour implicite

Toute instruction en Ruby retourne la valeur de la dernière expression évaluée. Un exemple simple est la méthode **getter**. Nous appelons une méthode et attendons une valeur en retour.

Voyons :

```rb
def get_user_ids(users)
  return users.map(&:id)
end
```

Mais comme nous le savons, Ruby retourne toujours la dernière expression évaluée. Pourquoi utiliser l'instruction **return** ?

Après avoir utilisé Ruby pendant 3 ans, je me sens bien en utilisant presque toutes les méthodes sans l'instruction **return**.

```rb
def get_user_ids(users)
  users.map(&:id)
end
```

#### Assignations multiples

Ruby me permet d'assigner plusieurs variables en même temps. Lorsque vous commencez, vous pouvez coder comme ceci :

```rb
def values
  [1, 2, 3]
end

one   = values[0]
two   = values[1]
three = values[2]
```

Mais pourquoi ne pas assigner plusieurs variables en même temps ?

```rb
def values
  [1, 2, 3]
end

one, two, three = values
```

Assez génial.

#### Méthodes qui posent des questions (aussi appelées prédicats)

Une fonctionnalité qui a attiré mon attention lorsque j'apprenais Ruby était la méthode **point d'interrogation (?)** , aussi appelée les méthodes **prédicats**. C'était étrange à voir au début, mais maintenant cela a beaucoup de sens. Vous pouvez écrire du code comme ceci :

```rb
movie.awesome # => true
```

Ok... rien de mal avec cela. Mais utilisons le point d'interrogation :

```rb
movie.awesome? # => true
```

Ce code est beaucoup plus expressif, et je m'attends à ce que la réponse de la méthode retourne soit une valeur **true** ou **false**.

Une méthode que j'utilise couramment est **any?** C'est comme demander à un tableau s'il a **quelque chose** à l'intérieur.

```rb
[].any? # => false
[1, 2, 3].any? # => true
```

#### Interpolation

Pour moi, l'interpolation de chaînes est plus intuitive que la concaténation de chaînes. Point. Voyons cela en action.

Un exemple de concaténation de chaînes :

```rb
programming_language = "Ruby"
programming_language + " is a beautiful programming_language" # => "Ruby is a beautiful programming_language"
```

Un exemple d'interpolation de chaînes :

```rb
programming_language = "Ruby"
"#{programming_language} is a beautiful programming_language" # => "Ruby is a beautiful programming_language"
```

Je préfère l'interpolation de chaînes.

Qu'en pensez-vous ?

#### L'instruction if

J'aime utiliser l'instruction **if** :

```rb
def hey_ho?
  true
end

puts "let's go" if hey_ho?
```

Assez agréable de coder comme ça.

Cela semble vraiment naturel.

#### La méthode try (avec le mode Rails activé)

La méthode **try** appelle la méthode identifiée par le symbole, en lui passant tous les arguments et/ou le bloc spécifié. Cela est similaire à **Object#send** de Ruby. Contrairement à cette méthode, **nil** sera retourné si l'objet receveur est un objet **nil** ou **NilClass**.

Utilisation de l'instruction conditionnelle **if and unless** :

```rb
user.id unless user.nil?
```

Utilisation de la méthode **try** :

```rb
user.try(:id)
```

Depuis Ruby 2.3, nous pouvons utiliser l'opérateur de navigation sécurisée de Ruby **(&.)** au lieu de la méthode **try** de Rails.

```rb
user&.id
```

#### Double pipe égal (**||=)** / mémoisation

Cette fonctionnalité est tellement C-O-O-L. C'est comme mettre en cache une valeur dans une variable.

```rb
some_variable ||= 10
puts some_variable # => 10

some_variable ||= 99
puts some_variable # => 10
```

Vous n'avez pas besoin d'utiliser l'instruction **if**. Il suffit d'utiliser le double pipe égal **(||=)** et c'est fait.

Simple et facile.

#### Méthode statique de classe

Une manière que j'aime pour écrire des classes Ruby est de définir une méthode **statique** (méthode de classe).

```rb
GetSearchResult.call(params)
```

Simple. Beau. Intuitif.

Qu'est-ce qui se passe en arrière-plan ?

```rb
class GetSearchResult
  def self.call(params)
    new(params).call
  end

  def initialize(params)
    @params = params
  end

  def call
    # ... votre code ici ...
  end
end
```

La méthode **self.call** initialise une instance, et cet objet appelle la méthode **call**. Le [**modèle de conception Interactor**](https://github.com/collectiveidea/interactor) l'utilise.

#### Getters et setters

Pour la même classe **GetSearchResult**, si nous voulons utiliser les params, nous pouvons utiliser @params

```rb
class GetSearchResult
  def self.call(params)
    new(params).call
  end

  def initialize(params)
    @params = params
  end

  def call
    # ... votre code ici ...
    @params # faire quelque chose avec @params
  end
end
```

Nous définissons un **setter** et un **getter** :

```rb
class GetSearchResult
  def self.call(params)
    new(params).call
  end

  def initialize(params)
    @params = params
  end

  def call
    # ... votre code ici ...
    params # faire quelque chose avec la méthode params ici
  end

  private

  def params
    @params
  end

  def params=(parameters)
    @params = parameters
  end
end
```

Ou nous pouvons définir **attr_reader**, **attr_writer**, ou **attr_accessor**

```rb
class GetSearchResult
  attr_reader :param

  def self.call(params)
    new(params).call
  end

  def initialize(params)
    @params = params
  end

  def call
    # ... votre code ici ...
    params # faire quelque chose avec la méthode params ici
  end
end
```

Bien.

Nous n'avons pas besoin de définir les méthodes **getter** et **setter**. Le code vient de devenir plus simple, exactement ce que nous voulons.

#### Tap

Imaginez que vous voulez définir une méthode **create_user**. Cette méthode va instancier, définir les paramètres, sauvegarder et retourner l'utilisateur.

Faisons-le.

```rb
def create_user(params)
  user       = User.new
  user.id    = params[:id]
  user.name  = params[:name]
  user.email = params[:email]
  # ...
  user.save
  user
end
```

Simple. Rien de mal ici.

Alors maintenant, implémentons-le avec la méthode **tap**

```rb
def create_user(params)
  User.new.tap do |user|
    user.id    = params[:id]
    user.name  = params[:name]
    user.email = params[:email]
    # ...
    user.save
  end
end
```

Vous devez simplement vous soucier des paramètres de l'utilisateur, et la méthode **tap** vous retournera l'objet utilisateur.

### C'est tout

Nous avons appris que j'écris du Ruby idiomatique en codant avec

* les méthodes de tableau
* la syntaxe

Nous avons également appris comment Ruby est beau et intuitif, et s'exécute même plus rapidement.

Et c'est tout, les gars ! Je mettrai à jour et inclurai plus de détails sur mon [blog](https://medium.com/@leandrotk_). L'idée est de partager du bon contenu, et la communauté aide à améliorer cet article ! ☂

J'espère que vous avez apprécié le contenu et appris à programmer un beau code (et de meilleurs logiciels).

Si vous voulez un cours complet sur Ruby, apprendre des compétences de codage du monde réel et construire des projets, essayez [**_One Month Ruby Bootcamp_**](https://onemonth.com/courses/ruby?mbsy=lG6tt&mbsy_source=97541b09-e3ab-45d7-a9b1-dbc77028e008&campaignid=33446&discount_code=TKRuby1). À bientôt ☂

Cet article est apparu en premier [**ici**](https://medium.com/the-renaissance-developer/idiomatic-ruby-1b5fa1445098) sur ma [**publication Renaissance Developer**](https://medium.com/the-renaissance-developer).

Amusez-vous, continuez à apprendre, et continuez toujours à coder !

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☂