---
title: Comment utiliser les associations polymorphiques dans Ruby on Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-26T18:40:39.000Z'
originalURL: https://freecodecamp.org/news/polymorphic-association-ruby-on-rails
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Add-a-subheading--2-.png
tags:
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: Comment utiliser les associations polymorphiques dans Ruby on Rails
seo_desc: 'By Sampurna Chapagain

  Polymorphic association in Ruby on Rails refers to the type of active record association.
  From the Rails Guide, it allows a single model to belong to more than one other
  model on a single association.

  This tutorial assumes that ...'
---

Par Sampurna Chapagain

L'association polymorphique dans Ruby on Rails fait référence au type d'association de registre actif. Selon le [Guide Rails](https://guides.rubyonrails.org/association_basics.html#polymorphic-associations), elle permet à un seul modèle d'appartenir à plus d'un autre modèle sur une seule association.

Ce tutoriel suppose que vous avez quelques connaissances sur certaines associations dans Rails comme les associations `belongs_to`, `has_one` et `has_many`.

Il s'agit d'un type d'association légèrement plus avancé, mais il est parfait lorsque vous souhaitez connecter un modèle à plusieurs autres modèles.

## Le problème de ne pas utiliser les associations polymorphiques

Supposons que vous souhaitiez créer une application avec des fonctionnalités comme des publications, un forum et une fonctionnalité d'événement.

Dans la phase initiale de votre application, vous pourriez prévoir d'ajouter une fonctionnalité de commentaire uniquement au modèle de publications. Mais à mesure que votre application grandit, vous pourriez vouloir ajouter une fonctionnalité de commentaire similaire aux modèles de forum et d'événement également (peut-être pour d'autres modèles également).

Voyons à quoi cela ressemblerait dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Comment--1-.jpg)
_Passer des commentaires aux modèles de posts, d'événements et de forum_

Chaque fois que vous souhaitez ajouter quelque chose qui a des commentaires dans l'application, vous devez ajouter une clé étrangère à la table des commentaires. Vous finirez par écrire beaucoup de code répétitif dans ce processus.

Cela ne pose peut-être pas de problème pour les petites applications, mais à mesure que votre application grandit, cela peut devenir un énorme problème. Et c'est là que les associations polymorphiques deviennent super pratiques.

## Comment les associations polymorphiques aident à résoudre ce problème

La solution au problème ci-dessus est d'utiliser des associations polymorphiques dans Rails. Cela vous permet de définir un seul modèle qui peut appartenir à d'autres modèles différents sans avoir à écrire de code répété.

En considérant l'exemple ci-dessus, vous n'avez pas à ajouter la clé étrangère à la table des commentaires chaque fois que vous devez ajouter des commentaires à d'autres modèles.

Avec les associations polymorphiques, vous pouvez ajouter simplement deux colonnes dans la table des commentaires, ce qui est très simple. Voyons comment cela fonctionne dans la section suivante de cet article.

## Comment implémenter les associations polymorphiques

Pour créer le nouveau modèle `PolyComment`, nous utiliserons la commande suivante :

`rails g model PolyComment content:text commentable:references{polymorphic}`

Vérifions maintenant le modèle `PolyComment` :

``` ruby
class PolyComment < ApplicationRecord
  belongs_to :commentable, polymorphic: true
end


Le fichier de migration ressemblera à ceci :

```ruby
class CreatePolyComments < ActiveRecord::Migration[6.1]
  def change
    create_table :poly_comments do |t|
      t.text :content
      t.references :commentable, polymorphic: true, null: false

      t.timestamps
    end
  end
end


Maintenant, exécutons la migration en utilisant la commande `rails db:migrate` pour mettre à jour le `schema` qui aura deux colonnes supplémentaires intéressantes.

```ruby
create_table "poly_comments", force: :cascade do |t|
    t.text "content"
    t.string "commentable_type", null: false
    t.integer "commentable_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["commentable_type", "commentable_id"], name: "index_poly_comments_on_commentable"
  end

Les colonnes `commentable_type` et `commentable_id` aident à configurer les associations polymorphiques.

`commentable_type` stocke le nom des modèles comme `Event`, `Post` ou `Forum` dans ce cas. Et `commentable_id` stocke l'`id` qui correspond à ce modèle.

Maintenant, générons les trois modèles avec les commandes suivantes :

`rails g model Post title`

`rails g model Event title`

`rails g model Forum title`

Maintenant, nous devons ajouter des relations `has_many` dans ces trois modèles :

Post.rb
```ruby
class Post < ApplicationRecord
    has_many :poly_comments, as: :commentable
end

Event.rb
```ruby
class Event < ApplicationRecord
    has_many :poly_comments, as: :commentable
end


Forum.rb
```ruby
class Forum < ApplicationRecord
    has_many :poly_comments, as: :commentable
end


Vous pouvez ajouter des commentaires à autant de modèles que vous le souhaitez en fonction de la logique ci-dessus.

### Comment le tester dans la console

Maintenant, jouons avec la console pour tester les résultats :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-from-2023-01-23-20-08-00.png)
_Création d'un nouveau post_

Ici, nous avons créé un nouveau Post.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-from-2023-01-23-20-08-25-3.png)
_Ajout de commentaire au Post_

Ici, vous pouvez voir que la valeur de `commentable_type` est `Post` (sous forme de chaîne) puisqu'il est associé au modèle `Post`. De plus, la valeur de `commentable_id` est `1` puisqu'elle correspond à l'`id` de l'objet respectif.

C'est ainsi que vous pouvez ajouter des commentaires pour tous les modèles que vous souhaitez.

## Conclusion

Les associations polymorphiques rendent votre code DRY (Don't repeat yourself) et sans bug. Si vous souhaitez connecter un modèle à plusieurs autres modèles, alors les associations polymorphiques seront un excellent choix. En utilisant cette approche, vous n'avez pas à définir une association séparée pour chaque modèle.

Si vous avez aimé cet article, envisagez de [m'offrir un café](https://www.buymeacoffee.com/SamChapagain) 💕.

Vous pouvez me trouver sur [Twitter](https://twitter.com/saam_codes) pour divers contenus liés au développement Web.

Bon codage !