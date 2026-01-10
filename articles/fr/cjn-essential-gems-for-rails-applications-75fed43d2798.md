---
title: Gemmes Essentielles pour les Applications Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T22:30:05.000Z'
originalURL: https://freecodecamp.org/news/cjn-essential-gems-for-rails-applications-75fed43d2798
coverImage: https://cdn-media-1.freecodecamp.org/images/0*cw0oHjOoBMDeba6_.jpg
tags:
- name: Apps
  slug: apps-tag
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
seo_title: Gemmes Essentielles pour les Applications Rails
seo_desc: 'By Clark Jason Ngo

  Gems are located in the Gemfile inside your project folder. Let’s have a look at
  some you’ll want to have.

  will_paginate

  Adds pagination to your app

  Installation

  Add to Gemfile

  gem ''will_paginate''

  Install

  bundle install

  Usage

  In a ...'
---

Par Clark Jason Ngo

Les gemmes sont situées dans le Gemfile à l'intérieur de votre dossier de projet. Examinons quelques-unes que vous voudrez avoir.

### **will_paginate**

**Ajoute la pagination à votre application**

#### **Installation**

Ajoutez au `Gemfile`

```
gem 'will_paginate'
```

Installez

```
bundle install
```

**Utilisation**

Dans un fichier .html.erb, rendez les liens de page dans la vue :

```erb
<%= will_paginate @places %>
  <% @places.each do |place| %>
    <h1><%= place.name %></h1>
    <br />
  <% end %>
<%= will_paginate @places %>
```

Dans votre contrôleur, vous pouvez définir combien d'entrées par page vous voulez afficher. Dans l'exemple ci-dessous, il listera 3 entrées par page.

```ruby
def index
  @places = Place.all.paginate(page: params[:page], per_page: 3)
end
```

Source : [https://github.com/mislav/will_paginate](https://github.com/mislav/will_paginate)

### **simple_form**

**Formulaires simplifiés !**

#### **Installation**

Ajoutez au `Gemfile`

```
gem 'simple_form'
```

Installez

```
bundle install
```

Exécutez le générateur

```
rails generate simple_form:install
```

**Utilisation**

Dans un fichier `.html.erb` :

```ruby
<%= simple_form_for @place do |f| %>
  <%= f.input :name %>
  <%= f.input :address %>
  <%= f.input :description %>
  <br />
  <%= f.submit 'Créer', class: 'btn btn-primary' %>
<% end %>
```

Source : [https://github.com/plataformatec/simple_form](https://github.com/plataformatec/simple_form)

### **devise**

**Ajoute la gestion des utilisateurs**

#### **Installation**

Ajoutez au `Gemfile`

```ruby
gem 'devise'
```

Installez

```ruby
bundle install
```

Exécutez le générateur

```ruby
rails generate devise:install
```

Configurez devise dans _config/environments/development.rb_

Ajoutez cette ligne :

```ruby
config.action_mailer.default_url_options = { host: 'localhost', port: 3000 } 
```

Modifiez le code dans _app/views/layouts/application.html.erb_

Ajoutez ces lignes :

```ruby
<% if notice %>
  <p class="alert alert-success"><%= notice %></p>
<% end %>
<% if alert %>
  <p class="alert alert-danger"><%= alert %></p>
<% end %>
```

Ajoutez les liens d'inscription et de connexion dans _app/views/layouts/application.html.erb_

```ruby
<p class="navbar-text pull-right">
<% if user_signed_in? %>
  Connecté en tant que <strong><%= current_user.email %></strong>.
  <%= link_to 'Modifier le profil', edit_user_registration_path, :class => 'navbar-link' %> |
  <%= link_to "Déconnexion", destroy_user_session_path, method: :delete, :class => 'navbar-link'  %>
<% else %>
  <%= link_to "S'inscrire", new_user_registration_path, :class => 'navbar-link'  %> |
  <%= link_to "Connexion", new_user_session_path, :class => 'navbar-link'  %>
<% end %>
</p>
```

Forcez l'utilisateur à être redirigé vers la page de connexion s'il n'est pas connecté.

Modifiez dans _app/controllers/application_controller.rb_

```ruby
before_action :authenticate_user!
```

Source : [https://guides.railsgirls.com/devise](https://guides.railsgirls.com/devise)

### **geocoder**

**Ajoute le géocodage depuis l'API Google**

#### **Installation**

Ajoutez au `Gemfile`

```ruby
gem 'geocoder'
```

Installez

```
bundle install
```

Créez un fichier de migration, exécutez ceci dans votre terminal :

```
rails generate migration AddLatitudeAndLongitudeToModel latitude:float longitude:float
```

```
rake db:migrate
```

Exemple de fichier de migration ajoutant des colonnes de latitude et de longitude pour une table Places existante :

```ruby
class AlterPlacesAddLatAndLng < ActiveRecord::Migration[5.0]
  def change
    add_column :places, :latitude, :float
    add_column :places, :longitude, :float
  end
end
```

Ajoutez ces lignes dans votre `app/model/place.rb`

```ruby
geocoded_by :address
after_validation :geocode
```

Ajoutez ce script dans _`show.html.erb`_

```js
<script>
<% if @place.latitude.present? && @place.longitude.present? %>
  function initMap() {
  var myLatLng = {lat: <%= @place.latitude %>, lng: <%= @place.longitude %>};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: myLatLng
  });
  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Bonjour le monde !'
  });
}
</script>
```

Source : [https://www.rubydoc.info/gems/geocoder/1.3.7](https://www.rubydoc.info/gems/geocoder/1.3.7)

### **figaro**

**Configurez facilement vos API dans le déploiement Heroku**

#### **Installation**

Ajoutez au `Gemfile`

```
gem 'figaro'
```

Installez et créez un fichier `config/application.yml` commenté et ajoutez-le à votre `.gitignore`

```
bundle exec figaro install
```

Mettez à jour vos clés API dans `config/application.yml`

Pour mettre à jour les clés API dans heroku, allez dans votre terminal :

```
figaro heroku:set -e productionheroku restart
```

Source : [https://github.com/laserlemon/figaro](https://github.com/laserlemon/figaro)

### carrierwave

**Uploader d'images**

#### **Installation**

Ajoutez au `Gemfile`

```
gem 'carrierwave'
```

Installez

```
bundle install
```

Dans votre terminal

```
rails generate uploader Image
```

Cela générera ceci :

```
app/uploaders/image_uploader.rb
```

Créez un fichier de migration

```
rails g migration add_image_to_courses image:string
```

Exécutez le fichier de migration

```
rake db:migrate
```

Dans votre modèle

```ruby
class User < ApplicationRecord  mount_uploader :image, ImageUploaderend
```

Ajoutez à un `html.erb` par exemple `app/views/instructor/courses/new.html.erb`

```ruby
<%= f.input :image %>
```

Ajoutez au contrôleur `app/controllers/instructor/courses_controller.rb`

```ruby
params.require(:course).permit(:title, :description, :cost, :image)
```

Ajoutez à `show.html.erb` par exemple `app/views/instructor/courses/show.html.erb`

```ruby
<%= image_tag @course.image, class: 'img-fluid' %>
```

Mettez également à jour les fichiers suivants :

* `app/views/courses/show.html.erb`
* `app/views/courses/index.html.erb`
* `app/views/instructor/courses/show.html.erb`

#### **Résolution d'image avec ImageMagick, plus sur carrierwave**

Carrierwave montre que `MiniMagick` et `RMagick` peuvent être utilisés

Cela est montré ici `app/uploaders/image_uploader.rb`

```ruby
class ImageUploader < CarrierWave::Uploader::Base
  # Inclure le support RMagick ou MiniMagick :
  # include CarrierWave::RMagick
  # include CarrierWave::MiniMagick
```

#### **Installation d'ImageMagick**

Nous devons mettre à jour la base de données des programmes de notre environnement de développement pour nous assurer que lorsque nous installons un programme, nous obtenons la dernière version.

```
$ sudo apt-get update
```

Installez ImageMagick

```
$ sudo apt-get install imagemagick
```

Installation de MiniMagick

Ajoutez au `Gemfile`

```
gem 'mini_magick'
```

Installez

```
bundle install
```

Décommentez MiniMagick dans `app/uploaders/image_uploader.rb`

```ruby
class ImageUploader < CarrierWave::Uploader::Base
  # Inclure le support RMagick ou MiniMagick :
  # include CarrierWave::RMagick
  include CarrierWave::MiniMagick
```

Cette ligne donne à CarrierWave la capacité de communiquer avec le programme ImageMagick que nous avons installé sur notre programme, via la gemme MiniMagick. Cela nous permettra de redimensionner l'image.

Déverrouille les capacités de redimensionnement d'image telles que `resize_to_fill`, `resize_to_fit`, `resize_and_pad`, et `resize_to_limit`.

Ajoutez ceci dans `app/uploaders/image_uploader.rb`

```ruby
# Traiter les fichiers lors de leur téléchargement :
process resize_to_fill: [800, 350]
```

### Intégration d'Amazon S3 pour les téléchargements de vidéos

#### **Installation**

Ajoutez cette ligne au `Gemfile` de votre application :

```
gem 'carrierwave-aws'
```

Exécutez la commande bundle depuis votre shell pour l'installer :

```
bundle install
```

#### Étape 1 : Configuration de l'initialiseur

Normalement, nous installerions notre gemme en premier, cependant, pour éviter les bugs lors du passage de fog à AWS, nous devons d'abord mettre à jour notre initialiseur.

Vous pouvez lire les détails sur la façon de configurer la gemme carrierwave-aws [dans la section Utilisation de la documentation](https://github.com/sorentwo/carrierwave-aws#usage). En suivant le modèle qu'ils spécifient, nous devons mettre à jour `config/initializers/carrierwave.rb` pour qu'il ressemble à ceci :

```ruby
# config/initializers/carrierwave.rb
CarrierWave.configure do |config|
  config.storage    = :aws
  config.aws_bucket = ENV["AWS_BUCKET"]
  config.aws_acl    = "public-read"
  config.aws_credentials = {
      access_key_id:     ENV["AWS_ACCESS_KEY"],
      secret_access_key: ENV["AWS_SECRET_KEY"],
      region:            ENV["AWS_REGION"]
  }
end
```

Enregistrez le fichier.

#### Étape 2 : Mise à jour de notre Gemfile

Ajoutez la gemme `carrierwave-aws` [comme décrit par la documentation](https://github.com/sorentwo/carrierwave-aws#installation). Modifiez le `Gemfile` pour qu'il ressemble à ceci :

```
gem 'carrierwave'gem 'mini_magick'gem 'carrierwave-aws'
```

Enregistrez le fichier et exécutez la commande pour installer la gemme.

```
$ bundle install
```

Puis redémarrez votre serveur.

#### Étape 3 : Ajout de la région à application.yml

Nous devons ajouter une région à notre fichier `application.yml`. Ouvrez votre `config/application.yml` et ajoutez cette ligne pour spécifier la région que nous voulons utiliser :

```
# config/application.yml
AWS_ACCESS_KEY: "Votre-clé-d'accès"
AWS_SECRET_KEY: "Votre-clé-secrète"
AWS_BUCKET:     "Votre-bucket"
AWS_REGION:     "us-east-1"
```

Enregistrez le fichier.

#### Étape 4 : Mise à jour de l'uploader

Si vous vous souvenez, nous avons spécifié à l'intérieur du fournisseur de stockage pour l'uploader d'utiliser `:fog`. Plutôt que cela, nous devons le changer pour `:aws`.

```ruby
# encoding: utf-8
class ImageUploader < CarrierWave::Uploader::Base
  # Inclure le support RMagick ou MiniMagick :
  # include CarrierWave::RMagick
  include CarrierWave::MiniMagick
  # Choisir quel type de stockage utiliser pour cet uploader :
  #storage :file
  storage :aws
  # Beaucoup plus de commentaires ici....
end
```

Enregistrez le fichier.

Une dernière chose que nous devrons faire est de re-synchroniser le localhost avec heroku. Pour cela, nous devons exécuter une simple commande :

```
$ figaro heroku:set -e production
```

Assurez-vous que les téléchargements continuent de fonctionner en téléchargeant une image pour un cours et assurez-vous qu'elle passe avec succès.

### **VideoJS**

Ajoutez le fichier css avant `</head>`

```js
<link href="http://vjs.zencdn.net/5.12.6/video-js.css" rel="stylesheet">
```

Ajoutez les fichiers JavaScript avant `</body>`

```
<script src="http://vjs.zencdn.net/5.12.6/video.js"></script>
```

```js
<script src="http://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js"></script>
```

Note : Vous devez placer les balises `script` de videoJS en bas du body, sinon vous aurez des problèmes de chargement du lecteur vidéo à cause de Turbolinks.

Merci d'avoir lu ! J'espère que cela a été utile.