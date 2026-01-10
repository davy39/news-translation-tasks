---
title: Comment ajouter un moteur de recherche puissant à votre backend Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-27T17:36:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-powerful-search-engine-to-your-rails-backend-57bced889032
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u98adouc8-eKxM34eqi5Lw.jpeg
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment ajouter un moteur de recherche puissant à votre backend Rails
seo_desc: 'By Domenico Angilletta

  In my experience as a Ruby on Rails Developer, I often had to deal with adding search
  functionality to web applications. In fact, almost all applications I worked on
  at some point needed search engine capabilities, while many o...'
---

Par Domenico Angilletta

En tant que développeur Ruby on Rails, j'ai souvent dû ajouter des fonctionnalités de recherche à des applications web. En fait, presque toutes les applications sur lesquelles j'ai travaillé avaient besoin à un moment donné de capacités de moteur de recherche, et beaucoup d'entre elles avaient un moteur de recherche comme fonctionnalité principale la plus importante.

De nombreuses applications que nous utilisons quotidiennement seraient inutiles sans un bon moteur de recherche. Par exemple, sur Amazon, vous pouvez trouver un produit particulier parmi les [plus de 550 millions](https://www.scrapehero.com/many-products-amazon-sell-january-2018/) de produits disponibles sur le site en quelques secondes — tout cela grâce à une recherche en texte intégral combinée avec des filtres de catégorie, des facettes et un système de recommandation.

Sur Airbnb, vous pouvez rechercher un appartement en combinant une recherche géospatiale avec des filtres sur les caractéristiques de la maison, comme la dimension, le prix, les dates disponibles, etc.

Et Spotify, Netflix, Ebay, Youtube… tous dépendent fortement d'un moteur de recherche.

Dans cet article, je vais décrire comment développer un backend API Ruby on Rails 5 avec Elasticsearch. [Selon le classement DB Engines](https://db-engines.com/en/ranking/search+engine), Elasticsearch est actuellement la plateforme de recherche open source la plus populaire.

Cet article ne rentrera pas dans les détails d'Elasticsearch et comment il se compare à ses concurrents comme Sphinx et Solr. Au lieu de cela, ce sera un guide étape par étape sur la façon d'implémenter un backend API JSON avec Ruby on Rails et Elasticsearch, en utilisant une approche de développement piloté par les tests.

Cet article couvrira :

1. Configuration d'Elasticsearch pour les environnements de test, de développement et de production
2. Configuration de l'environnement de test Ruby on Rails
3. Indexation des modèles avec Elasticsearch
4. Point d'accès API de recherche

Comme dans mon article précédent, [Comment booster vos performances avec une architecture serverless](https://medium.freecodecamp.org/serverless-image-preprocessing-using-aws-lambda-42d58e1183f5), je couvrirai tout dans un tutoriel étape par étape. Ensuite, vous pourrez l'essayer vous-même et avoir un exemple simple et fonctionnel sur lequel construire quelque chose de plus complexe.

L'application exemple sera un moteur de recherche de films. Elle aura un seul point d'accès API JSON qui permet de faire une recherche en texte intégral sur les titres et les aperçus de films.

### 1. Configuration d'Elasticsearch

> [Elasticsearch](https://www.elastic.co/products/elasticsearch) est un moteur de recherche et d'analyse distribué, RESTful, capable de résoudre un nombre croissant de cas d'utilisation. Au cœur de la pile Elastic, il stocke centralement vos données afin que vous puissiez découvrir l'attendu et découvrir l'inattendu. — [www.elastic.co/products/elasticsearch](https://www.elastic.co/products/elasticsearch)

Selon le classement des moteurs de recherche de DB-Engines, Elasticsearch est de loin la plateforme de moteur de recherche la plus populaire aujourd'hui (en avril 2018). Et cela depuis la fin de 2015, lorsque [Amazon a annoncé le lancement d'AWS Elasticsearch Service](https://aws.amazon.com/blogs/aws/new-amazon-elasticsearch-service/), un moyen de démarrer un cluster Elasticsearch à partir de la console de gestion AWS.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-28.png)
_[Tendance du classement des moteurs de recherche DB Engines](https://db-engines.com/en/ranking_trend/search+engine" rel="noopener nofollow)_

Elasticsearch est open source. Vous pouvez télécharger votre version préférée depuis [leur site web](https://www.elastic.co/downloads/past-releases) et l'exécuter où vous voulez. Bien que je suggère d'utiliser le service AWS Elasticsearch pour les environnements de production, je préfère avoir Elasticsearch en cours d'exécution sur ma machine locale pour les tests et le développement.

Commençons par télécharger la version la plus récente d'Elasticsearch (6.2.3) et la décompresser. Ouvrez un terminal et exécutez

```bash
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.3.zip

$ unzip elasticsearch-6.2.3.zip
```

Alternativement, vous pouvez télécharger Elasticsearch depuis votre navigateur [ici](https://www.elastic.co/downloads/past-releases/elasticsearch-6-2-3) et le décompresser avec votre programme préféré.

### 2. Configuration de l'environnement de test

Nous allons construire une application backend avec Ruby on Rails 5 API. Elle aura un modèle qui représente les films. Elasticsearch les indexera, et ils seront recherchables via un point d'accès API.

Tout d'abord, créons une nouvelle application Rails. Dans le même dossier où vous avez téléchargé Elasticsearch auparavant, exécutez la commande pour générer une nouvelle application Rails. Si vous êtes nouveau dans Ruby on Rails, veuillez vous référer à ce [guide de démarrage](http://guides.rubyonrails.org/v5.1/getting_started.html) pour configurer votre environnement d'abord.

```bash
$ rails new movies-search --api; cd movies-search
```

Lorsque vous utilisez l'option « api », tous les middlewares utilisés principalement pour les applications navigateur ne sont pas inclus. Exactement ce que nous voulons. Lisez plus à ce sujet directement sur le [guide ruby on rails](http://guides.rubyonrails.org/v5.0/api_app.html).

Maintenant, ajoutons tous les Gems dont nous aurons besoin. Ouvrez votre Gemfile et ajoutez le code suivant :

```rb
# Gemfile

...
# Intégration Elasticsearch
gem 'elasticsearch-model'
gem 'elasticsearch-rails'

group :development, :test do
  ...
  # Framework de test
  gem 'rspec'
  gem 'rspec-rails'
end

group :test do
  ...
  # Nettoyer la base de données entre les tests
  gem 'database_cleaner'
  # Démarrer et arrêter ES pour les tests de manière programmatique
  gem 'elasticsearch-extensions'
end
...
```

Nous ajoutons deux Gems Elasticsearch qui fourniront toutes les méthodes nécessaires pour indexer notre modèle et exécuter des requêtes de recherche dessus. rspec, rspec-rails, database_cleaner et elasticsearch-extensions sont utilisés pour les tests.

Après avoir sauvegardé votre Gemfile, exécutez **bundle install** pour installer tous les Gems ajoutés.

Maintenant, configurons Rspec en exécutant la commande suivante :

```bash
rails generate rspec:install
```

Cette commande créera un dossier _spec_ et ajoutera _spec_helper.rb_ et _rails_helper.rb_. Ils peuvent être utilisés pour personnaliser rspec selon les besoins de votre application.

Dans ce cas, nous ajouterons un bloc DatabaseCleaner à _rails_helper.rb_ afin que chaque test s'exécute dans une base de données vide. De plus, nous modifierons _spec_helper.rb_ afin de démarrer un serveur de test Elasticsearch chaque fois que la suite de tests est démarrée, et de l'arrêter une fois la suite de tests terminée.

Cette solution est basée sur l'article de [Rowan Oulton](https://www.freecodecamp.org/news/how-to-add-a-powerful-search-engine-to-your-rails-backend-57bced889032/undefined) [Testing Elasticsearch in Rails](https://medium.com/@rowanoulton/testing-elasticsearch-in-rails-22a3296d989). Beaucoup d'applaudissements pour lui !

Commençons par DatabaseCleaner. À l'intérieur de _spec/rails_helper.rb_, ajoutez le code suivant :

```rb
# spec/rails_helper.rb
...
RSpec.configure do |config|
  ...
  
config.before(:suite) do
    DatabaseCleaner.strategy = :transaction
    DatabaseCleaner.clean_with(:truncation)
  end
  
config.around(:each) do |example|
    DatabaseCleaner.cleaning do
      example.run
    end
  end
end
```

Ensuite, réfléchissons à la configuration du serveur de test Elasticsearch. Nous devons ajouter des fichiers de configuration afin que Rails sache où trouver notre exécutable Elasticsearch. Cela lui indiquera également sur quel port nous voulons qu'il s'exécute, en fonction de l'environnement actuel. Pour ce faire, ajoutez un nouveau fichier yaml de configuration à votre dossier config :

```yml
# config/elasticsearch.yml

development: &default
  es_bin: '../elasticsearch-6.2.3/bin/elasticsearch'
  host: 'http://localhost:9200'
  port: '9200'
test:
  es_bin: '../elasticsearch-6.2.3/bin/elasticsearch'
  host: 'http://localhost:9250'
  port: '9250'
staging:
  <<: *default
production:
  es_bin: '../elasticsearch-6.2.3/bin/elasticsearch'
  host: 'http://localhost:9400'
  port: '9400'
```

Si vous n'avez pas créé l'application Rails dans le même dossier où vous avez téléchargé Elasticsearch, ou si vous utilisez une version différente d'Elasticsearch, vous devrez ajuster le chemin es_bin ici.

Ajoutez maintenant un nouveau fichier à votre dossier _initializers_ qui lira la configuration que nous venons d'ajouter :

```rb
# config/initializers/elasticsearch.rb

if File.exists?("config/elasticsearch.yml")
   config = YAML.load_file("config/elasticsearch.yml")[Rails.env].symbolize_keys
   Elasticsearch::Model.client = Elasticsearch::Client.new(config)
end
```

Et enfin, modifions _spec_helper.rb_ pour inclure la configuration de test Elasticsearch. Cela signifie démarrer et arrêter un serveur de test Elasticsearch et créer/supprimer des index Elasticsearch pour notre modèle Rails.

```rb
# spec/spec_helper.rb

require 'elasticsearch/extensions/test/cluster'
require 'yaml'

RSpec.configure do |config|
  ...
  # Démarrer un cluster en mémoire pour Elasticsearch si nécessaire
  es_config = YAML.load_file("config/elasticsearch.yml")["test"]
  ES_BIN = es_config["es_bin"]
  ES_PORT = es_config["port"]
  
config.before :all, elasticsearch: true do
    Elasticsearch::Extensions::Test::Cluster.start(command: ES_BIN, port: ES_PORT.to_i, nodes: 1, timeout: 120)  unless Elasticsearch::Extensions::Test::Cluster.running?(command: ES_BIN, on: ES_PORT.to_i)
  end
  
# Arrêter le cluster elasticsearch après l'exécution des tests
  config.after :suite do
    Elasticsearch::Extensions::Test::Cluster.stop(command: ES_BIN, port: ES_PORT.to_i, nodes: 1) if Elasticsearch::Extensions::Test::Cluster.running?(command: ES_BIN, on: ES_PORT.to_i)
  end
  
# Créer des index pour tous les modèles élastiques recherchables
  config.before :each, elasticsearch: true do
    ActiveRecord::Base.descendants.each do |model|
      if model.respond_to?(:__elasticsearch__)
        begin
          model.__elasticsearch__.create_index!
          model.__elasticsearch__.refresh_index!
        rescue => Elasticsearch::Transport::Transport::Errors::NotFound
          # Cela supprime les erreurs "Index does not exist" écrites dans la console
        rescue => e
          STDERR.puts "Il y a eu une erreur lors de la création de l'index elasticsearch pour #{model.name}: #{e.inspect}"
        end
      end
    end
  end
  
# Supprimer les index pour tous les modèles élastiques recherchables pour assurer un état propre entre les tests
  config.after :each, elasticsearch: true do
    ActiveRecord::Base.descendants.each do |model|
      if model.respond_to?(:__elasticsearch__)
        begin
          model.__elasticsearch__.delete_index!
        rescue => Elasticsearch::Transport::Transport::Errors::NotFound
          # Cela supprime les erreurs "Index does not exist" écrites dans la console
        rescue => e
          STDERR.puts "Il y a eu une erreur lors de la suppression de l'index elasticsearch pour #{model.name}: #{e.inspect}"
        end
      end
    end
  end
  
end
```

Nous avons défini quatre blocs :

1. un bloc before(:all) qui démarre un serveur de test Elasticsearch, sauf s'il est déjà en cours d'exécution
2. un bloc after(:suite) qui arrête le serveur de test Elasticsearch, s'il est en cours d'exécution
3. un bloc before(:each) qui crée un nouvel index Elasticsearch pour chaque modèle configuré avec Elasticsearch
4. un bloc after(:each) qui supprime tous les index Elasticsearch

L'ajout de _elasticsearch: true_ garantit que seuls les tests marqués avec _elasticsearch_ exécuteront ces blocs.

Je trouve que cette configuration fonctionne très bien lorsque vous exécutez tous vos tests une fois, par exemple avant un déploiement. En revanche, si vous utilisez une approche de développement piloté par les tests et que vous exécutez vos tests très souvent, vous devrez probablement modifier légèrement cette configuration. Vous ne voulez pas démarrer et arrêter votre serveur de test Elasticsearch à chaque exécution de test.

Dans ce cas, vous pourriez commenter le bloc after(:suite) où le serveur de test est arrêté. Vous pouvez l'arrêter manuellement, ou en utilisant un script, chaque fois que vous n'en avez plus besoin.

```rb
require 'elasticsearch/extensions/test/cluster'
es_config = YAML.load_file("config/elasticsearch.yml")["test"]
ES_BIN = es_config["es_bin"]
ES_PORT = es_config["port"]
Elasticsearch::Extensions::Test::Cluster.stop(command: ES_BIN, port: ES_PORT.to_i, nodes: 1)
```

### 3. Indexation des modèles avec Elasticsearch

Maintenant, nous commençons à implémenter notre modèle de film avec des capacités de recherche. Nous utilisons une approche de développement piloté par les tests. Cela signifie que nous écrivons d'abord les tests, voyons qu'ils échouent, puis écrivons le code pour les faire passer.

Tout d'abord, nous devons ajouter le modèle de film qui a quatre attributs : un titre (String), un aperçu (Text), une image_url (String) et une valeur de vote moyenne (Float).

```bash
$ rails g model Movie title:string overview:text image_url:string vote_average:float

$ rails db:migrate
```

Maintenant, il est temps d'ajouter Elasticsearch à notre modèle. Écrivons un test qui vérifie que notre modèle est indexé.

```rb
# spec/models/movie_spec.rb
require 'rails_helper'

RSpec.describe Movie, elasticsearch: true, :type => :model do
  it 'should be indexed' do
     expect(Movie.__elasticsearch__.index_exists?).to be_truthy
  end
end
```

Ce test vérifiera si un index elasticsearch a été créé pour Movie. N'oubliez pas qu'avant que les tests ne commencent, nous créons automatiquement un index elasticsearch pour tous les modèles qui répondent à la méthode __elasticsearch__. Cela signifie pour tous les modèles qui incluent les modules elasticsearch.

Exécutez le test pour le voir échouer.

```bash
bundle exec rspec spec/models/movie_spec.rb
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-29.png)

La première fois que vous exécutez ce test, vous devriez voir que le serveur de test Elasticsearch est en cours de démarrage. Le test échoue, car nous n'avons pas encore ajouté de module Elasticsearch à notre modèle Movie. Corrigons cela maintenant. Ouvrez le modèle et ajoutez le module Elasticsearch suivant à inclure :

```rb
# app/models/movie.rb

class Movie < ApplicationRecord
  include Elasticsearch::Model
end
```

Cela ajoutera certaines méthodes Elasticsearch à notre modèle Movie, comme la méthode manquante ___elasticsearch___ (qui a généré l'erreur dans l'exécution du test précédent) et la méthode _search_ que nous utiliserons plus tard.

Exécutez le test à nouveau et voyez-le réussir.

```bash
bundle exec rspec spec/models/movie_spec.rb
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-30.png)

Super. Nous avons un modèle de film indexé.

Par défaut, Elasticsearch::Model configura un index avec tous les attributs du modèle, en déduisant automatiquement leurs types. Habituellement, ce n'est pas ce que nous voulons. Nous allons maintenant personnaliser l'index du modèle pour qu'il ait le comportement suivant :

1. Seuls le titre et l'aperçu doivent être indexés
2. La lemmatisation doit être utilisée (ce qui signifie que la recherche de « acteurs » doit également retourner les films qui contiennent le texte « acteur », et vice-versa)

Nous voulons également que notre index soit mis à jour chaque fois qu'un film est ajouté, mis à jour ou supprimé.

Traduisons cela en tests en ajoutant le code suivant à _movie_spec.rb_

```rb
# spec/models/movie_spec.rb
RSpec.describe Movie, elasticsearch: true, :type => :model do
  ...
  
describe '#search' do
    before(:each) do
      Movie.create(
        title: "Roman Holiday",
        overview: "A 1953 American romantic comedy films ...",
        image_url: "wikimedia.com/Roman_holiday.jpg",
        vote_average: 4.0
      )
      Movie.__elasticsearch__.refresh_index!
    end
    it "should index title" do
      expect(Movie.search("Holiday").records.length).to eq(1)
    end
    it "should index overview" do
      expect(Movie.search("comedy").records.length).to eq(1)
    end
    it "should not index image_path" do
      expect(Movie.search("Roman_holiday.jpg").records.length).to eq(0)
    end
    it "should not index vote_average" do
      expect(Movie.search("4.0").records.length).to eq(0)
    end
  end
  
end
```

Nous créons un Movie avant chaque test, car nous avons configuré DatabaseCleaner de sorte que chaque test soit isolé. _Movie.__elasticsearch__.refresh_index!_ est nécessaire pour être sûr que le nouvel enregistrement de film est immédiatement disponible pour la recherche.

Comme avant, exécutez le test et voyez-le échouer.

![Image](https://cdn-media-1.freecodecamp.org/images/hBHAsDeOfCGgK1yL3h4Be9DJfM71fiyF4vBJ)

Il semble que notre film ne soit pas indexé. C'est parce que nous n'avons pas encore dit à notre modèle quoi faire lorsque les données du film changent. Heureusement, cela peut être corrigé en ajoutant un autre module à notre modèle Movie :

```rb
class Movie < ApplicationRecord
  include Elasticsearch::Model
  include Elasticsearch::Model::Callbacks
end
```

Avec _Elasticsearch::Model::Callbacks_, chaque fois qu'un film est ajouté, modifié ou supprimé, son document sur Elasticsearch est également mis à jour.

Voyons comment la sortie du test change.

![Image](https://cdn-media-1.freecodecamp.org/images/gpShemjWeele16xaHXxR1NuEKbF9-86FXcUq)

D'accord. Maintenant, le problème est que notre méthode de recherche retourne également des requêtes qui correspondent aux attributs _vote_average_ et _image_url_. Pour corriger cela, nous devons configurer le mappage de l'index Elasticsearch. Nous devons donc dire à Elasticsearch spécifiquement quels attributs de modèle indexer.

```rb
# app/models/movie.rb

class Movie < ApplicationRecord
  include Elasticsearch::Model
  include Elasticsearch::Model::Callbacks
  
# Index ElasticSearch
  settings index: { number_of_shards: 1 } do
    mappings dynamic: 'false' do
      indexes :title
      indexes :overview
    end
  end
end
```

Exécutez le test à nouveau et voyez-le réussir.

![Image](https://cdn-media-1.freecodecamp.org/images/K4poOG6jNnEwWwXXAi8zeO1aLrvtlSz1FEZ9)

Cool. Maintenant, ajoutons un stemmer pour qu'il n'y ait pas de différence entre « acteur » et « acteurs ». Comme toujours, nous allons d'abord écrire le test et le voir échouer.

```rb
describe '#search' do
    before(:each) do
      Movie.create(
        title: "Roman Holiday",
        overview: "A 1953 American romantic comedy films ...",
        image_url: "wikimedia.com/Roman_holiday.jpg",
        vote_average: 4.0
      )
      Movie.__elasticsearch__.refresh_index!
    end
    
...

it "should apply stemming to title" do
      expect(Movie.search("Holidays").records.length).to eq(1)
    end
    
it "should apply stemming to overview" do
      expect(Movie.search("film").records.length).to eq(1)
    end
end
```

Notez que nous testons les deux sens : Holidays devrait également retourner Holiday, et Film devrait également retourner Films.

![Image](https://cdn-media-1.freecodecamp.org/images/cH6SSsE20qS5FAQDPnahffP31Ezo6ULIhkhI)

Pour faire passer ces tests à nouveau, nous devons modifier le mappage de l'index. Cette fois, nous allons le faire en ajoutant un analyseur anglais aux deux champs :

```rb
class Movie < ApplicationRecord
  include Elasticsearch::Model
  include Elasticsearch::Model::Callbacks
  
# Index ElasticSearch
  settings index: { number_of_shards: 1 } do
    mappings dynamic: 'false' do
      indexes :title, analyzer: 'english'
      indexes :overview, analyzer: 'english'
    end
  end
end
```

Exécutez vos tests à nouveau pour les voir réussir.

![Image](https://cdn-media-1.freecodecamp.org/images/qTHYsfwiB6X1LGOHatnN209o5oyfiI0p4Sdm)

Elasticsearch est une plateforme de recherche très puissante, et nous pourrions ajouter beaucoup de fonctionnalités à notre méthode de recherche. Mais cela ne fait pas partie du cadre de cet article. Nous allons donc nous arrêter ici et passer à la construction de la partie contrôleur de l'API JSON à travers laquelle la méthode de recherche est accessible.

### 4. Point d'accès API de recherche

L'API de recherche que nous construisons devrait permettre aux utilisateurs de faire une recherche en texte intégral sur la table des films. Notre API a un seul point d'accès défini comme suit :

```
Url :
 GET /api/v1/movies
 
Params :
 * q=[string] requis
 
Exemple d'url :
 GET /api/v1/movies?q=Roma
 
Exemple de réponse :
[{"_index":"movies","_type":"movie","_id":"95088","_score":11.549209,"_source":{"id":95088,"title":"Roma","overview":"A virtually plotless, gaudy, impressionistic portrait of Rome through the eyes of one of its most famous citizens.", "image_url":"https://image.tmdb.org/t/p/w300/rqK75R3tTz2iWU0AQ6tLz3KMOU1.jpg","vote_average":6.6,"created_at":"2018-04-14T10:30:49.110Z","updated_at":"2018-04-14T10:30:49.110Z"}},...]
```

Ici, nous définissons notre point d'accès selon certaines bonnes pratiques de conception d'API RESTful :

1. L'URL doit encoder l'objet ou la ressource, tandis que l'action à entreprendre doit être encodée par la méthode HTTP. Dans ce cas, la ressource est les _movies_ (collection) et nous utilisons la méthode HTTP **GET** (parce que nous demandons des données à la ressource sans produire d'effet secondaire). Nous utilisons des paramètres d'URL pour définir davantage comment ces données doivent être obtenues. Dans cet exemple, q=[string], qui spécifie une requête de recherche. Vous pouvez lire plus sur la façon de concevoir des API RESTful sur l'article de [Mahesh Haldar](https://www.freecodecamp.org/news/how-to-add-a-powerful-search-engine-to-your-rails-backend-57bced889032/undefined) [RESTful API Designing guidelines — The best practices](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9).
2. Nous ajoutons également une version à notre API en ajoutant _v1_ à notre URL de point d'accès. La version de votre API est très importante, car elle vous permet d'introduire de nouvelles fonctionnalités qui ne sont pas compatibles avec les versions précédentes sans casser tous les clients qui ont été développés pour les versions précédentes de votre API.

D'accord. Commençons l'implémentation.

Comme toujours, nous commençons par des tests qui échouent. À l'intérieur du dossier spec, nous allons créer la structure de dossiers qui reflète la structure de l'URL de notre point d'accès API. Cela signifie controllers → api → v1 → movies_spec.rb

![Image](https://cdn-media-1.freecodecamp.org/images/UDUKtuyclu53rn5x7RkEvAD2XlAKYIboq4ZR)

Vous pouvez le faire manuellement ou depuis votre terminal en exécutant :

```bash
mkdir -p spec/controllers/api/v1 && \
touch spec/controllers/api/v1/movies_spec.rb
```

Les tests que nous allons écrire ici sont des tests de contrôleur. Ils n'ont pas besoin de vérifier la logique de recherche définie dans le modèle. Au lieu de cela, nous testerons trois choses :

1. Une requête GET à /api/v1/movies?q=[string] appellera Movie.search avec [string] comme paramètre
2. La sortie de Movie.search est retournée au format JSON
3. Un statut de succès est retourné

> Un test de contrôleur doit tester le comportement du contrôleur. Un test de contrôleur ne doit pas échouer à cause de problèmes dans le modèle.
>   
> (Prescription 20 — Rails 4 Test Prescriptions. [Noel Rappin](https://www.freecodecamp.org/news/how-to-add-a-powerful-search-engine-to-your-rails-backend-57bced889032/undefined))

Transformons cela en code. À l'intérieur de _spec/controllers/api/v1/movies_spec.rb_, ajoutez le code suivant :

```rb
# spec/controllers/api/v1/movies_spec.rb
require 'rails_helper'
RSpec.describe Api::V1::MoviesController, type: :request do
  # Rechercher un film avec le texte movie-title
  describe "GET /api/v1/movies?q=" do
    let(:title) { "movie-title"}
    let(:url) { "/api/v1/movies?q=#{title}"}
    
it "appele Movie.search avec les bons paramètres" do
      expect(Movie).to receive(:search).with(title)
      get url
    end
    
it "retourne la sortie de Movie.search" do
      allow(Movie).to receive(:search).and_return({})
      get url
      expect(response.body).to eq({}.to_json)
    end
    
it 'retourne un statut de succès' do
      allow(Movie).to receive(:search).with(title)
      get url
      expect(response).to be_successful
    end
  end
end
```

Le test échouera immédiatement car Api::V1::MoviesController n'est pas défini, alors faisons cela d'abord. Créez la structure de dossiers comme avant et ajoutez le contrôleur movies.

```bash
mkdir -p app/controllers/api/v1 && \
touch app/controllers/api/v1/movies_controller.rb
```

Maintenant, ajoutez le code suivant à _app/controllers/api/v1/movies_controller.rb_ :

```rb
# app/controllers/api/v1/movies_controller.rb
module Api
  module V1
    class MoviesController < ApplicationController
      def index;end
    end
  end
end
```

Il est temps d'exécuter notre test et de le voir échouer.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-31.png)

Tous les tests échouent car nous devons encore ajouter une route pour le point d'accès. À l'intérieur de config/routes.rb, ajoutez le code suivant :

```rb
# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :movies, only: [:index]
    end
  end
end
```

Relancez vos tests et voyez ce qui se passe.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-32.png)

La première erreur nous indique que nous devons ajouter un appel à Movie.search à l'intérieur de notre contrôleur. La deuxième se plaint de la réponse. Ajoutons le code manquant au movies_controller :

```rb
# app/controllers/api/v1/movies_controller.rb
module Api
  module V1
    class MoviesController < ApplicationController
      def index
        response = Movie.search params[:q]
        render json: response
      end
    end
  end
end
```

Exécutez le test et voyez si nous avons terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/GqmPo8HFTdXbQj9qBP1bzwjtHV35WojIL6zA)

Oui. C'est tout. Nous avons complété une application backend vraiment basique qui permet aux utilisateurs de rechercher un modèle via une API.

[Vous pouvez trouver le code complet sur mon dépôt GitHub ici](https://github.com/domangi/movies-search.git). Vous pouvez remplir votre table Movie avec des données en exécutant rails db:seed afin de voir l'application en action. Cela importera environ 45k films à partir d'un [Dataset téléchargé depuis Kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset). Jetez un coup d'œil au Readme pour plus de détails.

*Si vous avez aimé cet article, veuillez le partager sur les réseaux sociaux. Merci !*