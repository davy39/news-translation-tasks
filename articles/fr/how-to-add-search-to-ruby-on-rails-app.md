---
title: Comment ajouter une fonctionnalité de recherche à une application Ruby on Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-13T18:22:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-search-to-ruby-on-rails-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/markus-winkler-afW1hht0NSs-unsplash.jpg
tags:
- name: Ruby on Rails
  slug: ruby-on-rails
- name: search
  slug: search
seo_title: Comment ajouter une fonctionnalité de recherche à une application Ruby
  on Rails
seo_desc: 'By Sampurna Chapagain

  Nowadays, most web applications have a search feature. Users can use the search
  feature in order to navigate websites more easily.

  Implementing a search feature in Ruby on Rails is very easy. By using only a few
  lines of code yo...'
---

Par Sampurna Chapagain

De nos jours, la plupart des applications web disposent d'une fonction de recherche. Les utilisateurs peuvent utiliser la fonction de recherche afin de naviguer plus facilement sur les sites web.

Implémenter une fonction de recherche dans Ruby on Rails est très facile. En utilisant seulement quelques lignes de code, vous pouvez la configurer.

Ce tutoriel suppose que vous avez des connaissances de base sur Ruby on Rails. Si vous avez besoin d'une introduction au framework, [consultez ce cours](https://www.freecodecamp.org/news/learn-ruby-on-rails-video-course/).

### Ce que nous allons créer

À la fin de cet article, nous aurons une application web avec une fonction de recherche qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/searchresults.gif)
_Démonstration de l'application_

## Comment générer le Post Scaffold

Ici, nous utilisons Ruby version 3.0 et Rails version 6.1.7.

Rails scaffold fait référence à la génération automatique de fichiers qui forment la structure de base du projet Rails. Ces fichiers incluent les contrôleurs, les vues, les modèles, les routes et les migrations.

Maintenant, générons le post en utilisant la commande suivante :

`rails g scaffold post title description:text`

Maintenant, vous devez exécuter la migration afin de mettre à jour le schéma en utilisant la commande `rails db:migrate`.

Si vous lancez le serveur maintenant, vous pouvez effectuer toutes les opérations CRUD dans le projet.

## Comment ajouter Haml au projet

Vous allez utiliser haml dans les vues au lieu de erb. Vous pouvez le faire en ajoutant simplement `gem 'haml', '~> 6.1', '>= 6.1.1'` dans le Gemfile. Vous pouvez obtenir toutes les gems depuis le site [https://rubygems.org/](https://rubygems.org/).

Haml utilise l'indentation et son but principal est de rendre le balisage beau.

Maintenant, vous pouvez utiliser l'extension haml dans les vues au lieu de erb. Vous pouvez donc renommer application.html.erb en application.html.haml. Vous pouvez également utiliser des [outils de conversion html vers haml](https://awsm-tools.com/html-to-haml) pour convertir les fichiers erb en haml.

## Comment construire le formulaire de recherche

Une fois cela fait, vous êtes à la partie principale du tutoriel. Ajoutons donc le formulaire dans le fichier application.html.haml.

```ruby
%body
    %form{action: "/search"}
      %input{placeholder: "Rechercher", name: "key", type: "text"}
      %button{type: "submit"} Rechercher
    = yield

Ce code générera un formulaire dans toute l'application.

Ici, vous passez l'attribut action qui redirigera vers la page de recherche lorsque le formulaire sera soumis. Vous passez également la clé comme attribut name pour l'élément input.

Si vous soumettez le formulaire maintenant, vous obtiendrez l'erreur de routage suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/searcherror.gif)
_Enregistrement d'écran montrant l'erreur de routage._

### Comment ajouter les routes Root et Search

Ajoutons quelques routes dans le fichier routes.rb.

```ruby
root "posts#index"

get '/search', to: "posts#search"

La première route fait de la vue index la page racine.

La deuxième route ajoute la route de recherche en tant que méthode get. Vous devez donc créer une action search avec quelques requêtes SQL dans le contrôleur posts.

### Comment ajouter l'action Search dans le contrôleur

Dans la route ci-dessus, la route de recherche cherche une action search dans le contrôleur posts. Créons-la donc.

```ruby
def search
    key = "%#{params[:key]}%"
    @posts = Post.where("name LIKE ?", key)
end

Ici, dans l'action search, la variable `key` contient la valeur de `params[:key]`. Vous obtenez la valeur de `params[:key]` après la soumission du formulaire.

Le symbole `%` correspond à zéro, un ou plusieurs caractères. Le code ci-dessus utilise deux symboles `%` avant et après `params[:key]` pour faire correspondre la valeur de `params[:key]` présente à n'importe quelle position avec les enregistrements de la colonne `name` dans la base de données.

Il utilise l'opérateur `LIKE` avec une clause `where` afin d'effectuer une recherche. `?` est une valeur de remplacement dans les requêtes et est remplacée par les arguments passés – par exemple, `key` dans ce cas.

De plus, vous pouvez également utiliser l'opérateur `or` pour rechercher plusieurs colonnes dans la base de données.

`@posts = Post.where("name LIKE ? or description LIKE ?", key, key)`

Vous pouvez rechercher à la fois les enregistrements `name` et `description` en utilisant le code ci-dessus.

### Comment ajouter les vues nécessaires

Ensuite, vous devez ajouter un fichier search.html.haml. Mais avant cela, créons un nouveau partial appelé _post.html.haml afin de réutiliser le code. Le partial post ressemblera à ceci :

```ruby

%tbody
  -@posts.each do |post|
    %tr
      %td= post.name
      %td= post.description
      %td= link_to 'Afficher', post
      %td= link_to 'Modifier', edit_post_path(post)
      %td= link_to 'Supprimer', post, method: :delete, data: { confirm: 'Êtes-vous sûr ?' }
%br/
= link_to 'Nouveau Post', new_post_path


Voici à quoi ressemblera le fichier search.html.haml :

```ruby

%h1 Résultats de recherche
%p#notice= notice
%h1 Posts
%table
    %thead
        %tr
            %th Nom
            %th Description
            %th{colspan: "3"}
    =render "post"


Et vous devez également mettre à jour le fichier index.html.haml.

```ruby

%p#notice= notice
%h1 Posts
%table
    %thead
        %tr
            %th Nom
            %th Description
            %th{colspan: "3"}
    = render "post"


En faisant cela, vous utilisez le partial post dans les vues index et search.

Enfin, la fonction de recherche fonctionne comme prévu.

Vous pouvez trouver le code source complet de ce projet dans ce [dépôt GitHub](https://github.com/SampurnaC/search_demo_app_fcc).

## Conclusion

Voici comment vous pouvez créer une fonction de recherche dans une application Rails.

Si vous avez aimé cet article, envisagez de [m'offrir un café](https://www.buymeacoffee.com/SamChapagain) ☕.

Vous pouvez me trouver sur [Twitter](https://twitter.com/saam_codes) pour divers contenus liés au développement web.

Merci d'avoir lu.