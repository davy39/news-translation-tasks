---
title: Comment ajouter des catégories à une application Ruby on Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-01T23:31:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-categories-to-ruby-on-rails-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/fcccat.png
tags:
- name: blog
  slug: blog
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: Comment ajouter des catégories à une application Ruby on Rails
seo_desc: 'By Sampurna Chapagain

  Creating a category page is essential for most web applications these days. Different
  kinds of applications like blogs, ecommerce sites, movie streaming platforms, and
  many others have category features.

  This article will show h...'
---

Par Sampurna Chapagain

La création d'une page de catégorie est essentielle pour la plupart des applications web de nos jours. Différents types d'applications comme les blogs, les sites e-commerce, les plateformes de streaming de films et bien d'autres ont des fonctionnalités de catégorie.

Cet article montrera comment ajouter des catégories aux applications Ruby on Rails.

Ce tutoriel est adapté aux débutants, donc vous pouvez suivre même si vous avez des connaissances très basiques de Ruby on Rails.

## Comment générer le Blog Scaffold

Commençons par créer un nouveau projet Rails. Ici, nous utiliserons Rails version 6.1.7 et Ruby version 3.0. Vous pouvez créer le nouveau projet Rails en utilisant la commande suivante :

```ruby
rails new blog_categories
```

Maintenant, créons le nouveau blog scaffold en utilisant la commande suivante :

```ruby
rails g scaffold blogs title:string description:text
```

Cette commande créera tous les fichiers nécessaires pour travailler avec les opérations `CRUD` du blog avec deux champs de base de données `title` et `description`. Ici, `title` est le champ `string` et `description` est le champ `text`.

Vous devez maintenant exécuter la migration avec la commande `rails db:migrate`.

Maintenant, dirigez-vous vers votre terminal, démarrez le serveur et visitez la page `/blogs`. Vous pouvez voir le résultat suivant sur le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/blog.gif)
_création de blogs_

## Comment générer le Categories Scaffold

Nous en arrivons maintenant à la partie principale du tutoriel qui consiste à ajouter des catégories à nos articles de blog.

Pour cela, créons maintenant le scaffold des catégories avec la commande suivante :

```ruby
rails g scaffold categories name:string
```

Cette commande créera le `CRUD` pour les `categories`.

Vous devrez également exécuter `rails db:migrate` pour mettre à jour le schéma.

### Comment ajouter une association entre les modèles blog et category

Ensuite, vous devez ajouter une association entre les modèles `blog` et `category`.

Dans `Blog.rb` :

```ruby
class Blog < ApplicationRecord
    belongs_to :category
end
```

Et dans `Category.rb` :

```ruby
class Category < ApplicationRecord
    has_many :blogs
end
```

Maintenant, vous devez ajouter `category_id` à la table `blogs` puisque chaque blog est associé à une catégorie. Vous pouvez aller dans votre terminal et ajouter la migration suivante :

```ruby
rails g migration add_category_id_to_blogs
```

Cela créera une nouvelle migration. Vous devez ajouter le code suivant dans ce fichier de migration :

```ruby
add_column :blogs, :category_id, :integer
```

Rails a son propre ensemble de conventions et de règles. Et il est assez intelligent pour reconnaître que cette migration est destinée à ajouter une nouvelle colonne de base de données nommée `category_id` à la table `blogs`.

Vous devez maintenant passer `category_id` comme paramètre fort dans le contrôleur `blogs`.

```ruby
def blog_params
	params.require(:blog).permit(:title, :content, :category_id)
end
```

Maintenant, créons quelques catégories depuis le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/categories.gif)
_création de catégories depuis le navigateur_

Vous pourriez également ajouter une validation lors de la création de la catégorie. Pour cela, vous pouvez mettre à jour le fichier `category.rb` avec le code suivant :

```ruby
class Category < ApplicationRecord
    validates :name, presence: true, uniqueness: true
    has_many :blogs
end
```

Cela ajoutera quelques validations comme montré dans le GIF ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/validations.gif)
_ajout de validations lors de la création de catégories_

### Comment afficher les catégories sous forme de liste déroulante dans la page des nouveaux blogs

Maintenant que vous pouvez créer des blogs et des catégories, vous devrez afficher toutes les catégories sous forme de liste déroulante lorsque quelqu'un visite la page du nouveau blog.

Le code pour cela est montré ci-dessous :

```ruby
<div>
    <%= form.label :category %>
    <%= form.select :category_id, options_for_select(Category.all.map { |category| [category.name, category.id]})%>
</div>
```

La balise `select` crée la boîte de sélection déroulante. `options_for_select` prend quelques arguments. 

Tout d'abord, il parcourt toutes les catégories et retourne un tableau de `[c.category, c.id]`. Le `name` de la catégorie s'affiche sous forme de liste déroulante et l'`id` de la catégorie que l'utilisateur sélectionne est passé au contrôleur. Le contrôleur effectue ensuite l'insertion dans la base de données pour les blogs. 

Vous pouvez vous rendre à l'URL des nouveaux blogs et créer des blogs avec des catégories.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/blog1-1.gif)
_création de blogs avec des catégories_

### Lister les blogs de chaque catégorie

La partie suivante de ce tutoriel vous montrera comment lister toutes les catégories et tous les blogs associés à chaque catégorie. Nous afficherons cela sur la page d'index des catégories.

Pour cela, vous devez ajouter du code dans la vue d'index des catégories.

```ruby
<p id="notice"><%= notice %></p>

<h1>Catégories</h1>

<table>
  <thead>
    <tr>
      <th>Nom</th>
      <th>Blogs</th>
      <th colspan="3"></th>
    </tr>
  </thead>

  <tbody>
    <% @categories.each do |category| %>
      <tr>
        <td><%= category.name %></td>
        <% category.blogs.each do |blog| %>
          <td><%= blog.title %></td>
        <% end %>
      </tr>
    <% end %>
  </tbody>
</table>

<br>

<%= link_to 'Nouvelle Catégorie', new_category_path %>
```

Ici, il parcourt toutes les catégories afin d'afficher le nom de chaque catégorie. Une fois que nous avons terminé l'affichage du nom de la catégorie, la partie suivante consiste à afficher tous les blogs associés à chaque catégorie. Vous pouvez donc parcourir `category.blogs` à partir duquel vous pouvez obtenir les enregistrements de blog. 

Si vous visitez la route `/category`, vous pouvez voir toutes les catégories avec leurs blogs comme affiché dans le GIF ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/cat_blogs.gif)
_lister chaque catégorie avec les blogs_

## Conclusion

Dans ce tutoriel, vous avez appris comment ajouter des catégories dans vos applications Ruby on Rails en utilisant des associations un-à-plusieurs.

Si vous avez aimé cet article, envisagez de [m'offrir un café](https://www.buymeacoffee.com/SamChapagain) 💕.

Vous pouvez me trouver sur [Twitter](https://twitter.com/saam_codes) pour divers contenus liés au développement web.

Merci d'avoir lu.

Bon codage.