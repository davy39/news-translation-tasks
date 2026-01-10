---
title: Un aperçu rapide d'Action Text pour Rails 6.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T09:51:36.000Z'
originalURL: https://freecodecamp.org/news/quick-look-at-action-text-in-rails-6-0-12a8f9f7597f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0-LAOoPHs63XCSd3VDJ2Eg.png
tags:
- name: Rails 6
  slug: rails-6
- name: Action Text
  slug: action-text
- name: rich text editor
  slug: rich-text-editor
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: Un aperçu rapide d'Action Text pour Rails 6.0
seo_desc: 'By Arun Mathew Kurian

  Rails 6.0 is almost here. The stable version will be released on April 30. The Rails
  6.0 beta1 was released on January 15. As Rails releases always are, Rails 6.0 is
  also action-packed. There are two major frameworks newly intro...'
---

Par Arun Mathew Kurian

[Rails 6.0](https://weblog.rubyonrails.org/) est presque là. La version stable sera publiée le 30 avril. La version bêta 1 de Rails 6.0 a été publiée le 15 janvier. Comme toujours avec les versions de Rails, Rails 6.0 est également rempli de nouvelles fonctionnalités. Deux nouveaux frameworks majeurs ont été introduits, [Action Mailbox](https://weblog.rubyonrails.org/2018/12/13/introducing-action-mailbox-for-rails-6/) et [Action Text](https://weblog.rubyonrails.org/2018/10/3/introducing-action-text-for-rails-6/). Dans cet article, prenons un aperçu rapide d'Action Text en l'utilisant dans une petite application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0-LAOoPHs63XCSd3VDJ2Eg.png)
_courtoisie:wikipedia_

#### Action Text

Action Text nous permet d'apporter du contenu et de l'édition de texte riche à Rails. Cela signifie que nous pouvons effectuer des opérations telles que la mise en forme de texte, l'intégration d'images, la mise en forme de liens, l'ajout de listes et d'autres fonctionnalités similaires à un éditeur dans un champ de texte.

Cela est réalisé en incluant l'éditeur [Trix](https://github.com/basecamp/trix) dans le framework. Le contenu RichText généré par l'éditeur Trix est enregistré dans son propre modèle RichText qui est associé à n'importe quel modèle Active Record existant dans l'application. Toutes les images intégrées ou autres pièces jointes sont automatiquement stockées en utilisant [Active Storage.](https://edgeguides.rubyonrails.org/active_storage_overview.html)

Commençons à construire notre application Rails qui sera une application de blog. L'application est créée dans Rails 6.0, donc la version de Ruby doit être >2.5.

Dans le terminal, tapez

```
rails new blog --edge
```

Le drapeau --edge récupère la dernière version de Rails ou la version edge de Rails.

Action Text nécessite que web packer et ActiveStorage soient installés. Le stockage actif est déjà présent dans l'application Rails. Nous avons donc besoin de

```
gem "image_processing", "~> 1.2" #décommentez depuis le Gemfile
gem 'webpacker'
```

dans le fichier Gemfile.

Maintenant, exécutez

```
bundle install
```

Ensuite, nous devons créer un fichier config/webpacker.yml :

```
bundle exec rails webpacker:install
```

Maintenant, démarrons notre serveur Rails.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YXa6Y6mfxGa2E2m5hnwuug.png)

Super, construisons rapidement notre application. L'application n'aura qu'un seul modèle Article.

Créons un contrôleur pour les articles :

```
rails g controller Articles index new create show edit update destroy --no-helper --no-test-frameworks
```

Puis, configurons nos routes :

```
Rails.application.routes.draw do
  resources :articles
end
```

Ensuite, nous devons créer notre modèle. Notre modèle Articles aura deux champs : **title** et **text**. Le champ text doit être celui qui accepte le format de texte riche. Donc dans la migration, nous devons ajouter uniquement le champ title. Le champ text sera géré par ActionText.

Générons le modèle

```
rails g model Articles title:string --no-test-framework
```

et exécutons les migrations :

```
rails db:migrate
```

Maintenant, ajoutons la partie ActionText. Pour cela, exécutez d'abord

```
rails action_text:install
```

Cela ajoutera toutes les dépendances requises par Action Text. Plus particulièrement, cela ajoutera un nouveau fichier **javascript/packs/application.js** et deux migrations de stockage d'action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1nE9nc8I6E2jC-EnEy394A.png)

Exécutez à nouveau les migrations en utilisant

```
rails db:migrate
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*AzLR2ezD1weUwRXHKghCTQ.png)

Maintenant, nous pouvons ajouter la partie texte de notre modèle. Allez dans **app/models/article.rb** et ajoutez la ligne suivante

`has_rich_text :text`

text est le nom de champ que nous fournissons. Il peut être n'importe quoi comme body ou content, etc.

Notre modèle devient maintenant

```
class Article < ApplicationRecord
  has_rich_text :text
end
```

Avant de construire notre formulaire, créons la logique de notre contrôleur pour la création d'articles :

```
class ArticlesController < ApplicationController
  def create
    @article = Article.new(article_params)
    @article.save
    redirect_to @article
  end
```

```
  private
  def article_params
    params.require(:article).permit(:title, :text)
  end
```

```
end
```

Nous pouvons maintenant créer le formulaire pour le blog. Dans **app/views/articles/new.html.erb**, ajoutez le code de formulaire suivant :

```
<%= form_with scope: :article, url: articles_path, local: true do |form| %>
```

```
  <p>
    <%= form.label :title %><br>
    <%= form.text_field :title %>
  </p>
  <p>
    <%= form.label :text %><br>
    <%= form.rich_text_area :text %>
  </p>
  <p>
    <%= form.submit %>
  </p>
<% end %>
```

Remarquez que pour le champ texte, nous utilisons **form.rich_text_area** qui est fourni par Action Text.

Rendons notre page :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zpL22oO9exBtJqvJ75dFPw.png)

Génial !

Nous avons maintenant un éditeur de texte génial pour créer notre article.

Avant de commencer à utiliser l'éditeur, implémentons rapidement la fonctionnalité **show** du blog, afin que nous puissions voir les articles que nous avons créés.

Dans **app/controllers/articles_controller.rb**, ajoutez la fonction suivante :

```
  def show
    @article = Article.find(params[:id])
  end
```

De plus, nous devons créer une vue pour cela.

Créez le fichier **app/views/articles/show.html.erb** et ajoutez le code suivant :

```
<p>Titre de l'article : <strong><%= @article.title %></strong></p>
<p>Texte de l'article : <strong><%= @article.text %></strong></p>
```

```
<%= link_to 'Créer un nouveau', new_article_path %>
```

C'est tout. Notre application est terminée. Maintenant, vérifions les différentes fonctionnalités disponibles dans l'éditeur de texte fourni par ActionText.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_tH1tezWuI8khKwrieWjZw.png)

Nous pouvons voir qu'ActionText fournit presque toutes les fonctionnalités d'un éditeur de texte riche normal comme la mise en forme du texte en gras, en italique, l'ajout de barrés, de citations, de liens, le glisser-déposer d'images, etc.

Après avoir enregistré cela, nous pouvons voir le message enregistré à partir de la page show.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QD3WpW9992Wzo9a1yPyHgw.png)

Génial !

Ceci est un exemple très petit qui montre le potentiel d'ActionText. J'espère que cela a été utile. N'hésitez pas à l'essayer.

Une grande majorité des applications web traitent du contenu riche d'une manière ou d'une autre. Je crois donc que cette nouvelle fonctionnalité de Rails peut faciliter la vie de nombreux développeurs.

Félicitations à DHH et à toutes les personnes formidables derrière cela.

[https://github.com/amkurian/Rails-6.0_action_text_demo](https://github.com/amkurian/Rails-6.0_action_text_demo)

Quelques liens utiles :

[**Aperçu d'Action Text - Guides Ruby on Rails**](https://edgeguides.rubyonrails.org/action_text_overview.html)
[_Aperçu d'Action TextCe guide vous fournit tout ce dont vous avez besoin pour commencer à gérer le contenu de texte riche.Après…_edgeguides.rubyonrails.org](https://edgeguides.rubyonrails.org/action_text_overview.html)