---
title: Ce qui se passe lorsque vous créez un nouveau projet Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-08T01:12:00.000Z'
originalURL: https://freecodecamp.org/news/what-happens-when-you-run-rails-new
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca107740569d1a4ca4c41.jpg
tags:
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: Ce qui se passe lorsque vous créez un nouveau projet Rails
seo_desc: 'By Travis Fantina

  The first time you open your terminal and write rails new the sheer number of files
  and folders that are created can be overwhelming. You may even work on numerous
  Rails projects without ever opening many of these folders - so what ...'
---

Par Travis Fantina

La première fois que vous ouvrez votre terminal et écrivez `rails new`, le nombre impressionnant de fichiers et de dossiers créés peut être écrasant. Vous pouvez même travailler sur de nombreux projets Rails sans jamais ouvrir la plupart de ces dossiers - alors, que sont-ils exactement ? Que font-ils en coulisses ?

Eh bien, la vérité est que vous n'avez pas besoin de la plupart d'entre eux et Rails dispose de plusieurs options intégrées dans la commande `new` qui vous permettent de créer un nouveau projet sans certaines des valeurs par défaut de Rails (pour en savoir plus, tapez simplement `rails new —help`). Cela dit, pour la plupart des projets, vous exécuterez `rails new` et créerez un dossier de projet imposant.

Dans cet article, je vais passer en revue chaque fichier et dossier d'un nouveau projet Rails 6. N'hésitez pas à utiliser cela comme référence lorsque vous travaillez sur votre nouveau projet Rails pour comprendre certains des dossiers les plus obscurs. Marquez cette page et revenez-y chaque fois que vous vous sentez perdu dans un nouveau projet Rails.

Alors, commençons :

`rails new example-project`

Wow, c'est beaucoup !

Tout d'abord, Rails crée tous les fichiers et dossiers requis par une nouvelle application Rails. Ensuite, il récupère les gems et les regroupe ; ce sont les dépendances dont Rails a besoin pour exécuter votre site web dans son itération la plus simple. Cela semble beaucoup ? Dans une certaine mesure, c'est le cas, mais ces gems ajoutent la fonctionnalité qui rend un projet Rails si facile à démarrer. Essentiellement, tout ce que vous avez à faire maintenant est d'exécuter `rails server` et vous avez une application web qui s'exécute localement : c'est assez puissant et ce n'est pas quelque chose que vous pouvez obtenir si facilement /sans/ tout ce code standard.

Plongeons dans tous ces dossiers :

```shell
  create README.md
   create Rakefile
   create .ruby-version
   create config.ru
   create .gitignore
   create Gemfile
     run git init from "."
Initialized empty Git repository in /Users/tfantina/Documents/Code/FileStructure/.git/
   create package.json
   create app
   create app/assets/config/manifest.js
   create app/assets/stylesheets/application.css
   create app/channels/application_cable/channel.rb
   create app/channels/application_cable/connection.rb
   create app/controllers/application_controller.rb
   create app/helpers/application_helper.rb
   create app/javascript/channels/consumer.js
   create app/javascript/channels/index.js
   create app/javascript/packs/application.js
   create app/jobs/application_job.rb
   create app/mailers/application_mailer.rb
   create app/models/application_record.rb
   create app/views/layouts/application.html.erb
   create app/views/layouts/mailer.html.erb
   create app/views/layouts/mailer.text.erb
   create app/assets/images/.keep
   create app/controllers/concerns/.keep
   create app/models/concerns/.keep
   create bin
   create bin/rails
   create bin/rake
   create bin/setup
   create bin/yarn
   create config
   create config/routes.rb
   create config/application.rb
   create config/environment.rb
   create config/cable.yml
   create config/puma.rb
   create config/spring.rb
   create config/storage.yml
   create config/environments
   create config/environments/development.rb
   create config/environments/production.rb
   create config/environments/test.rb
   create config/initializers
   create config/initializers/application_controller_renderer.rb
   create config/initializers/assets.rb
   create config/initializers/backtrace_silencers.rb
   create config/initializers/content_security_policy.rb
   create config/initializers/cookies_serializer.rb
   create config/initializers/cors.rb
   create config/initializers/filter_parameter_logging.rb
   create config/initializers/inflections.rb
   create config/initializers/mime_types.rb
   create config/initializers/new_framework_defaults_6_0.rb
   create config/initializers/wrap_parameters.rb
   create config/locales
   create config/locales/en.yml
   create config/master.key
   append .gitignore
   create config/boot.rb
   create config/database.yml
   create db
   create db/seeds.rb
   create lib
   create lib/tasks
   create lib/tasks/.keep
   create lib/assets
   create lib/assets/.keep
   create log
   create log/.keep
   create public
   create public/404.html
   create public/422.html
   create public/500.html
   create public/apple-touch-icon-precomposed.png
   create public/apple-touch-icon.png
   create public/favicon.ico
   create public/robots.txt
   create tmp
   create tmp/.keep
   create tmp/cache
   create tmp/cache/assets
   create vendor
   create vendor/.keep
   create test/fixtures
   create test/fixtures/.keep
   create test/fixtures/files
   create test/fixtures/files/.keep
   create test/controllers
   create test/controllers/.keep
   create test/mailers
   create test/mailers/.keep
   create test/models
   create test/models/.keep
   create test/helpers
   create test/helpers/.keep
   create test/integration
   create test/integration/.keep
   create test/channels/application_cable/connection_test.rb
   create test/test_helper.rb
   create test/system
   create test/system/.keep
   create test/application_system_test_case.rb
   create storage
   create storage/.keep
   create tmp/storage
   create tmp/storage/.keep

```

Plongeons dedans :

```
cd example-project
code . 

```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0DE7CF47-259B-4346-8FB4-DEE2EE74709B.png)
_Dans VSCode, voici ce que nous avons_

Nous allons procéder dans l'ordre où Rails les organise, pour la plupart, je vais parler de chaque dossier et fichier, pour les fichiers répétés (comme .keep) je ne les mentionnerai qu'une fois. Vous remarquerez beaucoup de conventions dans Rails telles que « application_[framework]s » (`application_controller.rb`, `application_helper.rb`, `application_job.rb`, etc). Dans de tels cas, je couvrirai le dossier en détail afin que vous sachiez ce qui va à l'intérieur, sachez simplement que le fichier existant « application_[...].rb » est une classe parente dont les autres classes que vous créez dans le dossier hériteront.

# Le dossier app

C'est là que se déroulera la majorité de votre travail de développement. /app contient les Modèles, Vues et Contrôleurs qui seront servis aux utilisateurs lorsqu'ils seront demandés par le navigateur.

### app/assets

Stocke les ressources pour le Rails Asset Pipeline. Le Asset Pipeline rassemble les ressources (JavaScript, CSS et images) dans un projet et les sert au client de la manière la plus efficace possible. Il le fait en concaténant et en minifiant les ressources. Il précompile également les ressources écrites en Sass et CoffeeScript.
Plus d'informations : [The Asset Pipeline — Ruby on Rails Guides](https://guides.rubyonrails.org/asset_pipeline.html)

### app/assets/config

Voir ci-dessous

#### app/assets/config/manifest.js

Le Asset Pipeline mentionné ci-dessus est géré par une gem Ruby appelée « Sprockets-rails » qui fait tout ce qui précède. « Sprockets-rails » dispose de certaines gems d'assistance associées telles que « sass-rails », « uglifier » et « coffee-rails ». Coffee-rails et Sass-rails précompilent votre Sass et CoffeeScript en CSS et JavaScript tandis qu'Uglifier minifie ces ressources. Manifest.js vous permet de définir spécifiquement ce qui sera précompilé.
Pour plus d'informations sur ce fichier spécifique, voir : [eileen.codes | Rails 5: The Sprockets 4 Manifest](https://eileencodes.com/posts/the-sprockets-4-manifest/)

### app/assets/images

Les ressources d'images, telles que les icônes et les SVGs pour le Asset Pipeline, peuvent être placées ici.

#### .keep

C'est le premier des nombreux fichiers .keep que vous verrez dans un nouveau projet Rails. Ce ne sont pas des fichiers Rails mais des fichiers pour Git qui ne suivront normalement pas les dossiers vides. Le fichier keep. dit simplement « quelqu'un est ici ». Tout ce qui contient un fichier .keep sera suivi par Git. Vous n'avez pas besoin de .keep si vous mettez autre chose dans le dossier.

### app/assets/stylesheets

Le dossier stylesheets est l'endroit où vous placerez les styles associés à votre application. Vous pouvez écrire des feuilles de style en CSS ou SASS, le Asset Pipeline précompilera toutes les feuilles de style pour vous.

#### app/assets/stylesheets/application.css

Contient tous les styles qui seront inclus dans le Asset Pipeline. Les styles globaux peuvent être écrits dans Application.css mais vous pouvez également écrire des feuilles de style spécifiques au contrôleur (lorsque vous exécutez la commande `rails g` pour créer un nouveau contrôleur, il créera une feuille de style associée. `=require_tree .` est la manière de Rails d'inclure tous les dossiers associés à l'intérieur d'un répertoire afin que tout autre fichier CSS à l'intérieur de ce projet soit inclus lors de la compilation. `=require_self` inclura tout CSS que vous écrivez à l'intérieur du fichier Application.css lui-même, cet emplacement est spécifique donc le CSS à l'intérieur de Application.css sera exécuté /après/ les autres dossiers qui sont inclus par `require_tree .`

## .app/channels

Rails dispose de nombreux frameworks internes plus petits. ActionCable est un framework qui vous permet d'utiliser WebSockets pour créer des fonctionnalités en temps réel dans votre application comme des chats et des « abonnements » auto-mis à jour aux notifications et au nouveau contenu. Si vous n'allez pas implémenter de fonctionnalités en temps réel, vous n'avez pas à vous soucier des dossiers ActionCable. Le dossier channels contient les fichiers Ruby côté serveur pour créer ces connexions.
Vous pouvez tout lire sur ActionCable ici : [Action Cable Overview — Ruby on Rails Guides](https://guides.rubyonrails.org/action_cable_overview.html)

### app/channels/application_cable

Application_cable contient les fichiers de canal et de connexion pour créer de nouvelles fonctionnalités en temps réel dans votre application.

#### app/channels/application_cable/channel.rb

Chaque fonctionnalité en temps réel individuelle de votre application serait encapsulée dans un canal individuel. Par exemple, une fonctionnalité de chat pourrait être un canal. Un système de notification pour le nouveau contenu publié serait un canal séparé. Ce dossier contient tous les canaux de votre application.

#### app/channels/application_cable/connection.rb

Les connexions sont l'authentification entre l'utilisateur et le serveur. Elles ne gèrent aucune logique (c'est ce que font les canaux), mais vérifient simplement que l'utilisateur actuel est autorisé à s'abonner aux divers canaux de votre application. Dans la plupart des cas, il s'agit d'une simple vérification que l'utilisateur est connecté.

## app/controllers

La partie « C » du modèle « MVC » (Modèle Vue Contrôleur). Les contrôleurs agissent comme un intermédiaire entre le modèle et la vue. En fonction de la demande de l'utilisateur, le contrôleur récupère les données associées du modèle et les transmet à la vue qui est affichée à l'utilisateur. Par exemple, si un utilisateur navigue vers la page localhost:3000/posts, le contrôleur déterminera quelle vue lui est affichée ainsi que les enregistrements associés du modèle.

### app/controllers/concerns

Les concerns sont un moyen de réduire vos modèles, plutôt que d'écrire une grande quantité de méthodes réutilisables dans un seul modèle, vous pouvez placer ces méthodes dans des concerns où elles peuvent être facilement réutilisées dans vos contrôleurs.

### app/controllers/application_controller.rb

Les contrôleurs sont simplement des classes Ruby qui héritent d'une classe appelée ActionController. À mesure que vous ajoutez plus de modèles à votre projet, vous aurez plus de contrôleurs à gérer. application_controller.rb est requis pour tout projet Rails car il hérite de `ActionController::Base` et tous les futurs contrôleurs héritent à leur tour de celui-ci, leur donnant la fonctionnalité des contrôleurs.
Vous verrez beaucoup de fichiers « application_[insérer le titre relatif ici].rb » : application_controller.rb, application_helper.rb, application_record.rb. Dans la plupart des cas, ceux-ci représentent une manière globale d'interagir avec l'application, un intermédiaire qui hérite d'une classe de base et est ensuite hérité par des classes futures ou les deux. Je ne discuterai pas des fonctions de ces fichiers dans tous les cas.

## app/helpers

Les helpers sont un moyen de garder vos vues propres. Les vues doivent simplement se préoccuper d'afficher les informations en HTML à l'utilisateur. Si vous trouvez que vos fichiers html.erb sont encombrés de nombreux petits calculs ou de logique, vous devriez déplacer ce code dans des méthodes d'assistance.

### app/helpers/application_helper.rb

Fournit un endroit pour écrire des helpers globaux, à mesure que vous créez plus de contrôleurs, vous aurez plus de helpers pour travailler avec des contrôleurs et des vues spécifiques.

## app/javascript

Ce dossier est un endroit pratique pour mettre tout le JavaScript que vous utilisez dans votre application. Le Rails Asset Pipeline les inclura à partir de ce dossier dans toutes les pages où ils s'appliquent (le Asset Pipeline sait où les scripts appartiennent car les fichiers, normalement, suivent une convention de nommage du contrôleur auquel ils s'appliquent).

### app/javascript/channels

Nous avons déjà examiné les canaux d'ActionCable ci-dessus, mais ce dossier contient le JavaScript spécifique côté client pour créer des connexions WebSocket en temps réel.

#### app/javascript/channels/consumer.js

Les consommateurs sont les clients d'une connexion WebSocket ; les utilisateurs finaux qui s'abonnent au canal. Ce script connectera ces consommateurs au canal côté client.

#### app/javascript/channels/index.js

Une application peut avoir plusieurs canaux (chat, alertes, nouveaux messages, etc.). index.js est un répertoire côté client de tous les canaux de votre application.

#### app/javascript/packs/application.js

Webpacker est une gem Ruby qui vous permet d'utiliser Webpack, le bundler JavaScript dans votre projet Rails. Il fonctionne en conjonction avec le Asset Pipeline et est destiné aux grands frameworks JavaScript, pas aux petits scripts ou autres ressources comme le CSS ou les images (que Webpack gère généralement dans un projet JavaScript). Cependant, Webpacker est flexible et ceci n'est que la configuration par défaut. Vous pouvez faire en sorte que Webpack gère les images et les petits JavaScripts en contournant complètement le Asset Pipeline si vous le souhaitez. Vous pouvez spécifier cela dans ce dossier en requérant différentes ressources. Les ressources par défaut qui sont packagées sont :

```js
*require("@rails/ujs").start()*
*require("turbolinks").start()*
*require("@rails/activestorage").start()*
*require("channels")*


```

### app/jobs

Les jobs sont des tâches en arrière-plan que vous exécutez pendant que les utilisateurs continuent d'utiliser votre application. Chaque fois que vous avez une opération qui impliquera beaucoup de traitement, suffisamment pour ralentir considérablement l'expérience de l'utilisateur et faire « planter » votre application, vous devriez créer un job en arrière-plan qui exécutera la tâche en coulisses, permettant à l'utilisateur de continuer à utiliser votre site sans interruption.
Pour plus d'informations sur les Jobs, voir : [Rails Active Job Tutorial: How to Use activejob | Codeship | via @codeship](https://blog.codeship.com/how-to-use-rails-active-job/)

#### app/assets/jobs/application_job.rb

Voir ci-dessus.

## app/mailers

Vous pouvez considérer les mailers comme des contrôleurs pour les emails. Vous pouvez créer un nouveau mailer avec `Rails generate mailer`. Cela vous donnera l'équivalent d'un Modèle et d'un Contrôleur pour envoyer des emails à vos utilisateurs.

### app/mailers/application_mailer.rb

Voir ci-dessus.

## app/models

Le « M » de MVC ; un Modèle est un template pour les données stockées dans votre base de données. Généralement, toute table est considérée comme un « Modèle ». Les modèles courants peuvent être `User`, `Post` ou `Comment`. Notez que ces choses sont au singulier plutôt qu'au pluriel, cela fait référence à la nature prototypique d'un modèle. Cela contraste avec les Contrôleurs qui, par convention, sont au pluriel car les Contrôleurs font référence à plusieurs enregistrements.

### app/models/concerns

Les concerns sont des modules - de petits morceaux de code réutilisable généralement extraits des Modèles lorsqu'ils deviennent trop volumineux. Le dossier Concerns fait partie d'un framework interne de Rails appelé ActiveSupport qui facilite la gestion des modules.

Pour plus d'informations, voir les [guides de Rails sur les concerns](https://api.rubyonrails.org/classes/ActiveSupport/Concern.html).

### app/models/application_record.rb

Application_record.rb hérite de `ActiveRecord::Base`, tous les modèles ultérieurs de votre application hériteront de `ApplicationRecord`, similaire à la manière dont Application_controller rend la fonctionnalité de `ActionController` disponible pour tous les autres Contrôleurs.

## app/views

La dernière partie du modèle MVC est les Vues. Le dossier Vues contient tout ce que l'utilisateur verra dans son navigateur, principalement sous forme de HTML avec Ruby intégré (ERB) ou .Haml qui est un langage de templating pour Ruby. Les nouveaux contrôleurs auront probablement un dossier de vue associé avec le même nom (sauf si vous créez une API). En général, chaque méthode dans le Contrôleur aura une Vue associée.

### app/views/layouts

Votre nouvelle application Rails aura un dossier Layouts avec **application.html.erb**, **mailer.html.erb** et **mailer.text.erb**, ceux-ci définissent les mises en page globales pour l'application Rails dans divers domaines tels que le navigateur et la boîte de réception. Vous pouvez souhaiter ajouter d'autres composants d'une mise en page dans ce dossier, par exemple, un **_header.html.erb**, mais la plupart de vos vues seront organisées dans des dossiers de Vue spécifiques à leur Contrôleur. **Application.html.erb** est le modèle principal de votre application, ce fichier crée les balises HTML principales `<head>` et `<body>` pour votre application avec les vues elles-mêmes affichées dans `<%= yield %>`. Yield est simplement un peu de code Ruby qui ajoute la vue appropriée pour la page que l'utilisateur consulte. Avoir un fichier **Application.html.erb** garde votre code DRY puisque vous n'avez pas à déclarer à plusieurs reprises un type de document, des éléments de tête ou à inclure des scripts et des feuilles de style, pour chaque page dans la Vue. Rails et le Asset Pipeline s'en occupent pour vous. Les trois fichiers dans ce dossier, comme indiqué ci-dessus, sont :

* app/views/layouts/application.html.erb
* app/views/layouts/mailer.html.erb
* app/views/layouts/mailer.text.erb

# dossier bin

Le dossier bin aide à configurer l'application Rails afin qu'elle et les commandes associées puissent s'exécuter correctement.

## bin/bundle

Assure que le Gem Bundler fonctionne correctement.

## bin/rails

Spring est un préchargeur qui maintient Rails en cours d'exécution en arrière-plan pendant que vous travaillez (il y a certains cas où vous devez redémarrer le serveur, mais pour la plupart, les modifications apportées aux Vues ou aux Contrôleurs seront chargées automatiquement et immédiatement dans votre application en cours d'exécution dans un environnement de développement). Ce fichier charge spring lorsque vous démarrez l'application Rails.

## bin/rake

Rake signifie Ruby Make et est utilisé pour exécuter plusieurs commandes qui configureront et mettront à jour le serveur.

## bin/setup

Vous permet d'écrire des commandes qui s'exécuteront lorsque votre application sera démarrée pour la première fois.

## bin/spring

Permet à Spring de s'exécuter sans utiliser le Bundler pour regrouper toutes vos gems, cela permet à Spring de recharger rapidement vos pages en développement chaque fois que vous apportez une modification.

## bin/webpack

Comme discuté ci-dessus, Rails utilise Webpack pour regrouper certains JavaScripts par opposition au AssetPipeline, ce fichier nécessite la configuration nécessaire puis exécute Webpack.

## bin/webpack-dev-server

Vous permet de personnaliser le serveur de développement de Webpack, ce que vous pouvez souhaiter faire si vous ne voulez pas que certaines ou toutes vos ressources soient regroupées dans votre environnement de développement.

## bin/yarn

Yarn est un gestionnaire de paquets JavaScript similaire à NPM. Vous pouvez utiliser l'un ou l'autre avec les projets Rails.

# config

Config, comme son nom l'indique, contient des fichiers pour configurer votre application Rails dans différents environnements ; développement et test.

## config/environments

Ce dossier vous permet de configurer comment votre application fonctionnera dans les environnements de développement, de production et de test. Par exemple, vous pouvez souhaiter vous assurer que votre action_mail est configurée pour envoyer des emails via un service de messagerie en production mais pas en développement.

## config/initializers

Ce dossier vous permet de définir des initialiseurs granulaires pour définir comment votre application Rails se comportera. Il y a de fortes chances que vous ne passiez pas trop de temps ici, surtout lorsque vous travaillez sur vos premières applications Rails.

### config/initializers/application_controller_renderer.rb

Permet aux contrôleurs de rendre en dehors de leur portée. Pour plus d'informations, voir : [Upgrading to Ruby on Rails 5.0 from Rails 4.2 - application use case - Running with Ruby](https://mensfeld.pl/2015/12/upgrading-to-ruby-on-rails-5-0-from-rails-4-2-application-use-case/)

### config/initializers/assets.rb

Relatif au Asset Pipeline ; qui, vous vous en souviendrez, sert les pages dans votre application Rails avec les ressources spécifiques (CSS, JS, etc.) dont elles ont besoin. Ici, vous pouvez ajouter des ressources au chemin de chargement comme node_modules.

### config/initializers/backtrace_silencers.rb

Les backtraces sont un outil de débogage qui vous permet de voir ce qui se passe dans votre application Rails, particulièrement utile lorsque les choses explosent et que vous pouvez localiser la zone spécifique de l'échec. Configurez ce que les backtraces montrent en déterminant quelles bibliothèques sont autorisées à montrer des backtraces dans ce fichier.

### config/initializers/content_security_policy.rb

De Mozilla : « L'en-tête de réponse HTTP _Content-Security-Policy_ permet aux administrateurs de sites web de contrôler les ressources que l'agent utilisateur est autorisé à charger pour une page donnée. Avec quelques exceptions, les politiques impliquent principalement la spécification des origines du serveur et des points de terminaison des scripts. » [Content-Security-Policy - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy). En essence, cela contrôle les données autorisées à circuler dans votre application et depuis quelles sources externes. Par exemple, le lien vers des scripts externes, des polices ou des images en dehors de votre application.

### config/initializers/cookies_serializer.rb

Détermine le format des cookies, par défaut, il s'agit de `:json`

### config/initializers/filter_parameter_logging.rb

Nous discuterons de la journalisation ci-dessous, mais il existe certains paramètres (entrées utilisateur acceptées) comme les mots de passe ou les données sensibles de l'utilisateur que vous ne souhaitez pas voir apparaître dans votre journal, vous pouvez les ajouter ici. filter_parameter_logging est en quelque sorte comme .gitignore pour les paramètres.

### config/initializers/inflections.rb

Comme discuté dans l'explication du Modèle, Rails a des conventions de nommage pour ce qui est singulier et pluriel. Basé sur les locales (paramètres de langue pour votre application, voir le dossier Locales ci-dessous), vous pouvez mettre à jour ces inflexions dans cet initialiseur, bien que ce ne soit probablement pas une bonne idée sauf si c'est absolument nécessaire.

### config/initializers/mime_types.rb

Types MIME - Multipurpose Internet Mail Extensions spécifient le format des pièces jointes des emails.
[MIME - Wikipedia](https://en.wikipedia.org/wiki/MIME)

### config/initializers/wrap_parameters.rb

Par défaut, Rails enveloppe tous les paramètres en JSON, mais vous pouvez spécifier d'autres formats en utilisant le hachage `wrap_parameters`. [ActionController::ParamsWrapper](https://api.rubyonrails.org/classes/ActionController/ParamsWrapper.html)

## config/locales

Se chargera généralement avec en.yml comme seul fichier. Si votre application va avoir plusieurs options de langue, vous pouvez inclure toutes les traductions sous forme de fichiers YML ici.

## config/webpack

```
Vous permet de configurer les paramètres de Webpack en fonction de l'environnement.

```

### config/webpack/development.js

### config/webpack/environment.js

### config/webpack/production.js

### config/webpack/test.js

### config/application.rb

Exécutera le fichier boot.rb si vous utilisez Passenger. Il intègre toutes les gems que vous avez requises dans le fichier gem dans votre projet et crée une classe `Application` qui hérite de `Rails::Application`

## config/boot.rb

Crée une variable d'environnement `BUNDLE_GEMFILE` définie sur l'emplacement du fichier gem de votre projet, c'est ainsi que Rails saura où intégrer les dépendances ou les Gems, dont il y a environ 2 douzaines dans une installation Rails par défaut.

## config/cable.yml

Similaire à database.yml (voir ci-dessous), cable.yml définit les adaptateurs de développement, de test et de production pour ActionCable, qui, vous vous en souviendrez, est la manière de Rails d'implémenter des fonctionnalités en temps réel dans votre application.

## config/credentials.yml.enc

credentials.yml remplace secrets.yml comme emplacement des clés secrètes. Ce fichier est chiffré afin que personne ne puisse lire vos clés secrètes et n'est déchiffré que par la clé principale (voir ci-dessous).

## config/database.yml

Vous pouvez définir une base de données par défaut (pour rendre votre code un peu plus DRY) ainsi que des bases de données spécifiques pour le développement, les tests et la production.

## config/environment.rb

L'initialisation de l'application Rails sur le serveur nécessite de nombreuses étapes, selon que vous utilisez `rails server` ou Passenger, ces étapes peuvent être légèrement différentes, mais une fois que environment.rb est chargé, l'application est initialisée et commence à s'exécuter.

## config/master.key

Jetez cela dans votre fichier .gitignore immédiatement (voir ci-dessous), c'est la clé principale qui déchiffre credentials.yml.enc dans Rails et personne ne devrait l'avoir. Pour plus d'informations, vous pouvez lire cet article brillant : [Rails 5.2 credentials – cedarcode – Medium](https://medium.com/cedarcode/rails-5-2-credentials-9b3324851336)

## config/puma.rb

Puma est un serveur web pour Ruby et est le serveur web par défaut pour l'environnement de développement de Rails. Vous pouvez configurer Puma via ce dossier en modifiant des éléments comme le nombre de threads et le port par défaut sur lequel Puma écoutera les requêtes entrantes (par défaut, il s'agit du port 3000).

## config/routes.rb

Les routes sont la carte routière autour de vos contrôleurs. Les routes prennent les requêtes entrantes vers le serveur et les dirigent vers le contrôleur correct. Contrairement à la plupart des autres fichiers dans le dossier config, vous passerez beaucoup de temps ici à configurer les routes au fur et à mesure que vous construisez votre application.

## config/spring.rb

Comme discuté dans le dossier bin, Spring est un préchargeur, ce fichier indique en réalité à Spring quels fichiers et dossiers doivent déclencher un redémarrage.

## config/storage.yml

ActiveStorage est un framework introduit dans Rails 5.2 pour le téléchargement et le stockage de ressources telles que des images. Vous avez besoin d'un endroit pour mettre ces choses comme une instance AWS, vous spécifiez cet emplacement dans ce fichier.

## config/webpacker.yml

Vous permet d'ajouter des environnements supplémentaires à Webpacker.

# db

## db/seeds

Les seeds vous permettent de remplir une base de données avec des données. Supposons que vous souhaitiez voir votre fonctionnalité de pagination en action ; vous pourriez créer 11 messages à la main ou vous pourriez simplement utiliser une gem comme Faker pour créer 11 messages aléatoires pour vous et les insérer directement dans votre base de données.

## lib

Lib est défini par les guides Rails comme « Modules étendus pour votre application ». Si cela semble vague, vous n'êtes pas le seul à le penser. Ce qui va spécifiquement dans le dossier lib est quelque peu controversé : voir [What goes in Rails lib/ – Extreme Programming – Medium](https://medium.com/extreme-programming/what-goes-in-rails-lib-92c74dfd955e) et [What code goes in the lib/ directory?](https://codeclimate.com/blog/what-code-goes-in-the-lib-directory/) mais le consensus général est que lib devrait être réservé au code qui ne s'intègre pas dans le dossier app, qui pourrait être facilement extrait pour une utilisation dans d'autres applications. Il a deux sous-dossiers : assets et tasks

## lib/assets

De Ruby on Rails Guides :

> « lib/assets est destiné au code des bibliothèques propres qui ne s'intègre pas vraiment dans le cadre de l'application ou à ces bibliothèques qui sont partagées entre les applications. »

## lib/tasks

Vous pouvez écrire des tâches `rake` personnalisées et les mettre dans ce dossier. Ce n'est pas un emplacement très couramment utilisé.

# log

La journalisation est un moyen important de voir comment votre application se comporte et de trouver et résoudre les problèmes. Par défaut, ce dossier sera vide. Vous pouvez initialiser divers loggers dans le dossier config/environments avec une commande comme : `config.log_level = :info`, à partir de là, lorsque vous exécutez votre application, le fichier de journalisation sera créé. Pour plus d'informations détaillées, voir cet excellent article de Datadog : [How to collect, customize, and manage Rails application logs](https://www.datadoghq.com/blog/managing-rails-application-logs/)

Inclus dans le dossier Log :

* log/development.log

# node_modules

Tout package node que vous utilisez dans votre projet (comme Webpack et Babel) dépendra de dizaines, voire de centaines d'autres packages node. Un gestionnaire de packages comme NPM ou Yarn gérera ces packages pour vous. Vous ne devriez pas entrer dans ce dossier ou modifier quoi que ce soit à l'intérieur.

# public

Le dossier public contient des ressources qui sont externes et peuvent être accessibles en dehors de la structure normale de votre application, comme favicon, apple-touch-icons, robots.txt et bien sûr les pages d'erreur. Des pages comme : 404, 422 et 500. Si l'application en production rencontre une sorte d'erreur, ces pages HTML seront servies automatiquement en contournant les routes, les contrôleurs ou toute vue spécifique. Ces pages ne font pas partie du Rails Asset Pipeline, vous devrez donc écrire tous les styles en ligne.

## public/robots.txt

Vous permet de spécifier comment les moteurs de recherche explorent votre site web.

# storage

Rails 5.2 a introduit ActiveStorage qui a remplacé des gems comme PaperClip et permet à Rails d'interfacer directement avec des services cloud comme AWS ou Google.

# test

Rails a des tests intégrés dès le départ ! La suite de tests par défaut dans Rails est MiniTest, vous trouverez donc que tous ces dossiers sont prêts à l'emploi avec MiniTest. Il y a des dossiers où vous pouvez tester des contrôleurs, des helpers, des modèles, des mailers spécifiques ainsi que écrire des tests d'intégration qui fonctionnent sur plusieurs contrôleurs et recréent quelque chose de similaire à l'expérience utilisateur réelle. Pour plus d'informations sur ce qui constitue un test de contrôleur par rapport à un test d'intégration, je recommande cet article de ([Jason Swett](https://www.codewithjason.com/difference-integration-tests-controller-tests-rails/))

## test/channels

#### test/channels/application_cable/connection_test.rb

Tests pour les connexions ActionCable, comme tout ce qui concerne ActionCable, vous n'aurez besoin de cela que si vous utilisez des canaux dans votre application.

## test/controllers

Vous pouvez tester vos contrôleurs ici, ces tests examinent généralement à quel point votre contrôleur fonctionne entre le modèle et la vue, ils sont plus larges en portée que les tests de modèle mais plus petits en portée que les tests d'intégration.

## test/fixtures

Ce n'est pas un endroit pour écrire des tests mais pour générer des données de test factices. À l'intérieur du dossier fixtures, vous pouvez ajouter n'importe quel nombre de fichiers YML avec des données prédéfinies. Vous pouvez extraire ces données dans vos tests pour vous assurer que vos modèles fonctionnent correctement et interagissent avec l'application comme prévu.

### test/fixtures/files

Maintenant que Rails a la gestion de fichiers intégrée avec ActiveStorage, non seulement vous pouvez tester les données des modèles, mais vous pouvez également tester les fichiers.

## test/helpers

Vous pouvez écrire des tests spécifiques pour les helpers que vous avez dans app/helpers. Tester les helpers n'est pas très courant, mais vous pouvez le faire si un helper est trop complexe ou semble fragile.

## test/integration

Les tests d'intégration vous permettent de tester les interactions entre les contrôleurs et offrent une option de test plus proche de l'expérience utilisateur réelle.

## test/mailers

Vous pouvez même écrire des tests pour vos mailers, pour vous assurer que les emails sont envoyés correctement et formatés correctement.

## test/models

L'un des tests les plus granulaires ; vous pouvez vous assurer qu'un enregistrement est sauvegardé correctement, que la base de données a été mise à jour, etc.

## test/system

Les tests système sont un moyen de tester votre application dans un vrai navigateur en générant des captures d'écran pour vous montrer comment tout se présente en action. Les tests système testeront également le JavaScript, ce qui ne signifie pas que vous devez utiliser les tests système MiniTest comme remplacement pour une bonne bibliothèque de tests JavaScript comme Jest. Cependant, les tests système vous permettront de voir comment votre JavaScript fonctionne dans le navigateur.

## test/application_system_test_case.rb

Ce fichier contient les valeurs par défaut pour vos tests système, vous pouvez changer de navigateurs, de pilotes ou de résolution d'écran.

## test/test_helper.rb

Test helper intègre des données externes et des bibliothèques nécessaires pour les tests. Vous remarquerez que dès le départ, `fixtures :all` est importé. Cela donne à vos tests l'accès aux fixtures. Vous pourriez configurer une multitude d'autres suites de tests et frameworks à partir de test_helper.rb pour inclure leurs fonctions et DSL tels que Capybara, FactoryBot et Faker.

# tmp

Temporaire - ce dossier contient des caches et des sessions, il peut être vidé de temps en temps, soit manuellement, soit lors du déploiement (selon la manière dont vous déployez votre application).

# vendor

Le dossier vendor est un endroit pour le code tiers, un peu comme les Gems. Les Gems, cependant, sont un peu plus autonomes, tandis que le dossier vendor peut contenir des scripts spécifiques non regroupés en gems. Pour plus d'informations ainsi que certains des avantages, voir [How to Vendor Gem a Gem](http://fuzzyblog.io/blog/ruby/2014/08/22/how-to-vendor-gem-a-gem.html).

# .browserslistrc

Browserslist est un outil pour cibler des versions spécifiques de navigateurs pour les outils NPM tels que Babel. Définis sur « defaults » par défaut, il garantit que

# .gitignore

Comme pour tout autre projet, votre contrôle de version ignorera tout fichier ou dossier que vous spécifiez ici.

# .ruby-version

Contient simplement la version de Ruby sous laquelle le projet fonctionne, RVM peut lire ce fichier et définir la version correcte de Ruby sur votre ordinateur (si vous avez plusieurs versions de Ruby installées).

# babel.config.js

Babel est un compilateur JavaScript qui vous permet d'utiliser les dernières et meilleures fonctionnalités de JavaScript et les compile pour qu'elles soient compatibles avec les navigateurs web qui n'ont pas encore adopté ces fonctionnalités. Pour plus d'informations sur la configuration de Babel, consultez leur [documentation officielle](https://babeljs.io/docs/en/).

# config.ru

Rack (le serveur Ruby populaire) utilise ce fichier pour démarrer l'application.

# gemfile

À l'intérieur du gemfile, vous stockez toutes les dépendances de votre application, comme vous l'avez vu, la commande Rails New installe beaucoup de gems, mais à mesure que vous ajoutez plus de fonctionnalités à votre application, vous entrerez et sortirez souvent de ce fichier.

# gemfile.lock

Similaire à package-lock.json pour les projets Node, ce fichier est mis à jour lorsque vous exécutez `bundle install` ou `bundle update` et résout toutes les dépendances de gems au-delà de ce que vous avez inclus manuellement dans le fichier gem. Ne touchez pas à ce fichier, il est mis à jour automatiquement.

# package.json

Établit les dépendances NPM pour les modules JavaScript, ceux-ci seront packagés avec Webpacker.

# postscss.config.js

PostCSS vous offre beaucoup de fonctionnalités modernes avec CSS, de l'ajout automatique de préfixes de fournisseurs à l'inclusion de modules CSS. Pour plus d'informations sur cet outil, consultez-le.

# rakefile

Encore une fois, Rake signifie « Ruby Make ». Rails dispose de plusieurs commandes intégrées qui nécessitent Rake, comme `rake routes` (vous montrant toutes les routes de votre application), `rake db:migrate` pour ajouter de nouveaux modèles et colonnes à votre base de données. Parmi d'autres, vous pouvez ajouter des commandes rake personnalisées ici.

# README.md

Il s'agit du fichier Readme de votre projet, il sera affiché sur la page Github de votre projet, incluez toutes les informations que vous jugez utiles pour les autres qui enquêtent ou travaillent avec votre projet.

# yarn.lock

Tout comme package.json, Yarn est le gestionnaire de paquets par défaut de Webpacker. Il s'agit d'un fichier de verrouillage, donc comme Gemfile.lock, il sera mis à jour automatiquement et vous ne devez pas le modifier manuellement.

Vous avez réussi ! Félicitations !

<iframe src="https://giphy.com/embed/LVWQ9iBwkpLmU" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/reactiongifs-LVWQ9iBwkpLmU">via GIPHY</a></p>

---

# Ressources supplémentaires

Helpers([The Beginner’s Guide to Rails Helpers - Mix & Go](https://mixandgo.com/learn/the-beginners-guide-to-rails-helpers))  
Info sur les fichiers Keep ([StackOverflow keep files](https://stackoverflow.com/questions/29183372/rails-why-is-there-keep-file-in-every-directory))  
Initialisation de Rails ([The Rails Initialization Process — Ruby on Rails Guides](https://guides.rubyonrails.org/initialization.html))  
Création de l'application Blog([Getting Started with Rails — Ruby on Rails Guides](https://guides.rubyonrails.org/getting_started.html#creating-the-blog-application))

---

Je réalise que c'est assez écrasant, mais laissez-moi simplifier un peu. 99 % de Rails est là pour vous permettre de personnaliser votre projet au n-ième degré, c'est pourquoi Rails continue de bien fonctionner pour les grandes entreprises et les startups ; vous pouvez facilement ajuster et tweaker presque n'importe quelle partie de votre application avec très peu d'effort. Cela dit, pour la plupart des débutants, des projets personnels et même une quantité décente de projets d'entreprise, vous utiliserez très peu de cette fonctionnalité.

Puisque les Modèles, les Vues et les Contrôleurs représentent le cœur d'une application Rails, vous passerez la plupart de votre temps de développement dans le dossier app. Vous utiliserez le fichier routes.rb assez souvent dans le dossier config pendant que vous configurez comment les utilisateurs navigueront dans votre application et à mesure que vous ajoutez de nouvelles actions de Contrôleur. Assurez-vous de toujours écrire une couverture de test appropriée pour vos applications. Si vous le faites, vous passerez beaucoup de temps dans le dossier de test. Le gemfile est un dernier endroit que vous visiterez souvent pour ajouter et mettre à jour les gems selon les besoins.

Bien qu'il y ait une tonne de fichiers et de dossiers créés dans chaque nouveau `rails new`, vous ne devriez pas être submergé par cela ; si vous vous perdez jamais, cet article vous couvre.

#