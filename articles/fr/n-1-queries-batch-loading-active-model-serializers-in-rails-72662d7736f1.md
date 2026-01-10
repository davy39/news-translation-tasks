---
title: Comment optimiser vos requêtes pour résoudre les goulots d'étranglement courants
  de scalabilité dans Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-04T19:18:58.000Z'
originalURL: https://freecodecamp.org/news/n-1-queries-batch-loading-active-model-serializers-in-rails-72662d7736f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ph_m9KGrsfJPHGwpfXA8nQ.png
tags:
- name: Batch Loading
  slug: batch-loading
- name: General Programming
  slug: programming
- name: Rails
  slug: rails
- name: REST API
  slug: rest-api
- name: 'tech '
  slug: tech
seo_title: Comment optimiser vos requêtes pour résoudre les goulots d'étranglement
  courants de scalabilité dans Rails
seo_desc: 'By Usama Ashraf

  The (perfect) solution for the N+1 problem


  The n+1 query problem is one of the most common scalability bottlenecks. It involves
  fetching a list of resources from a database that includes other associated resources
  within them. This m...'
---

Par Usama Ashraf

#### La solution (parfaite) pour le problème N+1

![Image](https://cdn-media-1.freecodecamp.org/images/Csu1xKKjVyRarXO3zKOQi-PwvPuR750NjwYt)

Le problème des requêtes N+1 est l'un des goulots d'étranglement de scalabilité les plus courants. Il implique de récupérer une liste de ressources d'une base de données qui inclut d'autres ressources associées. Cela signifie que nous devons peut-être interroger les ressources associées séparément. Donc, si vous avez une liste de n objets parents, _n autres requêtes devront être exécutées pour récupérer les ressources associées_. Essayons de nous débarrasser de ce dilemme O(n).

Si vous êtes à l'aise avec Rails, [Active Model Serializers](https://github.com/rails-api/active_model_serializers), et que vous avez déjà une bonne idée de ce que sera notre problème, alors peut-être pouvez-vous passer directement au code [ici](https://gist.github.com/UsamaAshraf/95b0c8d0d64ee193148342a931c0a423).

#### Un exemple concret

Disons que vous récupérez un tableau d'objets **Post** à un point de terminaison GET. Vous souhaitez également charger les auteurs respectifs des posts, en intégrant un objet **author** dans chacun des objets post. Voici une manière naïve de le faire :

```
class PostsController < ApplicationController    def index        posts = Post.all              render json: posts    endend
```

```
class Post  belongs_to :author, class_name: 'User'end
```

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details
```

```
  belongs_to :author end
```

Pour chacun des n objets **Post** rendus, une requête sera exécutée pour récupérer l'objet **User** correspondant. Ainsi, nous exécuterons un total de n+1 requêtes. C'est désastreux. Et voici comment le corriger en chargeant de manière anticipée l'objet **User** :

```
class PostsController < ApplicationController    def index        # Exécute une jointure SQL avec la table des utilisateurs.    posts = Post.includes(:author).all              render json: posts    endend
```

#### Quand une simple jointure n'est pas possible

Jusqu'à présent, il n'y a eu absolument rien de nouveau pour les vétérans.

Mais compliquons cela. _Supposons que les utilisateurs du site ne sont pas stockés dans le même RDMS que les posts. Plutôt, les utilisateurs sont des documents stockés dans MongoDB (pour une raison quelconque)._ Comment modifions-nous notre **Post** serializer pour récupérer l'utilisateur maintenant, de manière optimale ? Cela nous ramènerait à la case départ :

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details, :author
```

```
  # Exécutera n requêtes Mongo pour n posts rendus.  def author    User.find(object.author_id)  endend
```

```
# Ceci est maintenant un document Mongoid, pas un modèle ActiveRecord.class User    include Mongoid::Document    include Mongoid::Timestamps    # ...end
```

Le prédicament que nos utilisateurs résident maintenant dans une base de données Mongo peut être substitué par, par exemple, l'appel à un service HTTP tiers pour récupérer les utilisateurs ou les stocker dans un RDMS complètement différent. _Notre problème essentiel reste qu'il n'y a aucun moyen de « joindre » le datastore des utilisateurs avec la table des posts et d'obtenir la réponse que nous voulons en une seule requête._

Bien sûr, nous pouvons faire mieux. Nous pouvons récupérer l'ensemble de la réponse en deux requêtes :

* Récupérer tous les posts sans l'attribut **author** (1 requête SQL).
* Récupérer tous les auteurs correspondants en exécutant une requête where-in avec les IDs d'utilisateurs extraits du tableau de posts (1 requête Mongo avec une clause IN).

```
posts      = Post.allauthor_ids = posts.pluck(:author_id)authors    = User.where(:_id.in => author_ids)
```

```
# Passer d'une manière ou d'une autre les objets auteur au serializer de post et# les mapper aux bons objets post. Impossible d'imaginer à quoi cela ressemblerait exactement, mais probablement pas joli.render json: posts, pass_some_parameter_maybe: authors
```

#### Entrez Batch Loader

Donc, notre problème d'optimisation original a été réduit à « comment rendre ce code lisible et maintenable ». Les gens chez [Universe](https://www.universe.com/about) ont trouvé une véritable perle (trop évident ?). [Batch Loader](https://github.com/exAspArk/batch-loader) m'a été incroyablement utile récemment.

`gem 'batch-loader'`

`bundle install`

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details, :author
```

```
  def author    object.get_author_lazily  endend
```

```
class Post  def get_author_lazily    # L'objet post actuel est ajouté au lot ici,    # qui est finalement traité lorsque le bloc s'exécute.       BatchLoader.for(self).batch do |posts, batch_loader|          
```

```
      author_ids = posts.pluck(:author_id)        User.where(:_id.in => author_ids).each do |user|        post = posts.detect { |p| p.author_id == user._id.to_s }        #'Assigner' l'objet utilisateur au bon post.        batch_loader.call(post, user)            end        end    endend
```

Si vous êtes familier avec les Promesses JavaScript, pensez à la méthode `get_author_lazily` comme retournant une Promesse qui est évaluée plus tard. C'est une analogie décente, je pense, puisque `BatchLoader` utilise [des objets Ruby lazy](https://ruby-doc.org/core-2.4.1/Enumerable.html#method-i-lazy). Par défaut, `BatchLoader` met en cache les valeurs chargées, et donc pour garder les réponses à jour, vous devriez ajouter ceci à votre `config/application.rb` :

```
config.middleware.use BatchLoader::Middleware
```

C'est tout ! Nous avons résolu une version avancée du problème des requêtes n+1 tout en gardant notre code propre et en utilisant Active Model Serializers de la bonne manière.

#### Utilisation d'AMS pour les ressources imbriquées

Un problème cependant. Si vous avez un **User** serializer (Active Model Serializers fonctionne également avec Mongoid), celui-ci _ne sera pas_ appelé pour les objets **author** chargés de manière paresseuse, contrairement à avant. Pour corriger cela, nous pouvons utiliser un bloc Ruby et serializer les objets **author** avant qu'ils ne soient « assignés » aux posts.

```
class PostSerializer < ActiveModel::Serializer    attributes :id, :title, :details, :author
```

```
  def author    object.get_author_lazily do |author|      # Serialiser l'auteur après qu'il ait été chargé.           ActiveModelSerializers::SerializableResource                             .new(author)                             .as_json[:user]    end  endend
```

```
class Post  def get_author_lazily    # L'objet post actuel est ajouté au lot ici,    # qui est finalement traité lorsque le bloc s'exécute.       BatchLoader.for(self).batch do |posts, batch_loader|
```

```
      author_ids = posts.pluck(:author_id)      User.where(:_id.in => author_ids).each do |user|        modified_user = block_given? ? yield(user) : user        post = posts.detect { |p| p.author_id == user._id.to_s }          # 'Assigner' l'objet utilisateur au bon post.        batch_loader.call(post, modified_user)            end        end    endend
```

[Voici](https://gist.github.com/UsamaAshraf/95b0c8d0d64ee193148342a931c0a423) le code complet. Bon amusement !