---
title: Comment stocker les traductions dans une base de données avec Globalize
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T10:01:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-store-translations-inside-a-database-with-globalize-63cd033e29e6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m8n4yc-F8Ln4EcnbL3H-CQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Rails
  slug: rails
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: translation
  slug: translation
seo_title: Comment stocker les traductions dans une base de données avec Globalize
seo_desc: 'By Anastasia

  In one of my previous articles, I talked about the process of internationalizing
  Rails applications. That article explained all I18n basics, but it was revolving
  around placing all translations inside YAML files. There is nothing wrong w...'
---

Par Anastasia

Dans l'un de mes articles précédents, j'ai parlé du processus d'[internationalisation des applications Rails](https://blog.lokalise.co/rails-i18n/). Cet article expliquait tous les [basics de I18n](https://guides.rubyonrails.org/i18n.html), mais il tournait autour du placement de toutes les traductions dans des fichiers YAML. Il n'y a rien de mal avec cette approche, mais malheureusement, elle ne fonctionne pas toujours.

Supposons que votre site web contient beaucoup de contenu généré par les utilisateurs qui doit être adapté à différentes langues. Je propose de _stocker vos traductions dans la base de données_. Pourquoi les fichiers YAML ne fonctionneront-ils pas dans ce cas ?

* Le contenu lui-même peut être assez volumineux et il serait peu pratique de le stocker dans un fichier
* Le contenu est dynamique et les utilisateurs doivent pouvoir créer des versions traduites eux-mêmes, sans l'aide du développeur du site

Il semble que le module I18n [vous permet de définir un backend personnalisé](https://guides.rubyonrails.org/i18n.html#using-different-backends) qui, par exemple, peut être alimenté par ActiveRecord. Heureusement, il n'est pas nécessaire de créer votre propre solution car il en existe déjà une : [Globalize](https://github.com/globalize/globalize). Globalize est une bibliothèque éprouvée caractérisée comme « bibliothèque standard de fait pour la traduction de modèles/données ActiveRecord dans Rails I18n ». Avec son aide, vous pouvez facilement traduire les attributs de modèle, les étendre, introduire des replis, et ainsi de suite.

Donc, dans cet article, nous allons parler de Globalize et le voir en action en créant une application Rails d'exemple. Commençons-nous ?

### Préparation de l'application

Commençons par générer une nouvelle application Rails :

```
rails new GlobalizeSample
```

Je vais supposer que vous utilisez _Rails 5.2.1_ pour cette démonstration, mais les concepts décrits s'appliquent également aux versions antérieures.

Supposons que nous construisons une [boutique en ligne internationale](https://www.shopify.com/plus) présentant divers produits. Ces produits seront ajoutés par l'administrateur, et nous ne pouvons donc pas savoir à l'avance quel sera le contenu. Cela signifie que la méthode traditionnelle d'utilisation des fichiers YAML pour stocker les traductions ne fonctionnera pas. Notre gestionnaire de contenu n'aura accès qu'au CMS, et nous préférerions ne pas lui donner accès au code source de l'application (j'en frémis rien que d'y penser !).

Mais, ne craignez rien, dans la section suivante, nous surmonterons facilement ce problème. Pour l'instant, cependant, occupons-nous des bases.

### Administration des produits

Utilisez le générateur de code et créez un nouveau scaffold pour le `Product` :

```
rails g scaffold Product title:string description:text
```

Cela devrait créer un modèle, un contrôleur, des routes et des vues pour les produits. N'oubliez pas d'exécuter la migration :

```
rails db:migrate
```

Maintenant, démarrez le serveur :

```
rails s
```

Visitez le chemin `http://localhost:3000/products` et assurez-vous de pouvoir ajouter, modifier et supprimer les produits.

### Changer de langue

Pour voir la bibliothèque Globalize en action, nous aurons besoin d'un moyen de changer la locale de l'application. Je ne couvrirai pas ce processus en détail (car nous avons un [article séparé sur le sujet](https://blog.lokalise.co/rails-i18n/)) alors faisons-le rapidement.

Tout d'abord, ajoutez la liste des locales prises en charge à `config/application.rb` :

```
# ... config.i18n.available_locales = [:en, :ru]
```

Je vais prendre en charge l'anglais et le russe, mais vous pouvez choisir d'autres langues.

Ensuite, modifiez le fichier `config/routes.rb` et enveloppez la ressource produit avec une portée. De plus, pendant que nous y sommes, ajoutez une route racine :

```
scope "(:locale)", locale: /#{I18n.available_locales.join("|")}/ do # <== ajoutez ceci resources :products root 'products#index' # <== ajoutez ceci end # <== ajoutez ceci
```

Après cela, modifiez le fichier `application_controller.rb` :

```
# ... before_action :set_locale private def set_locale I18n.locale = extract_locale || I18n.default_locale end def extract_locale parsed_locale = params[:locale] I18n.available_locales.map(&:to_s).include?(parsed_locale) ? parsed_locale : nil end def default_url_options { locale: I18n.locale } end
```

Ce code définira la locale à chaque requête tout en s'assurant que la langue choisie est effectivement prise en charge. De plus, il ajoutera un paramètre GET `locale` à chaque lien généré avec l'aide `link_to`.

Enfin, ajoutez deux liens à la disposition de l'application :

```
<!-- views/layouts/application.html.erb --> <ul> <li><%= link_to 'English', root_path(locale: :en) %></li> <li><%= link_to 'Русский', root_path(locale: :ru) %></li> </ul>
```

Pour vous assurer que cette nouvelle fonctionnalité fonctionne, ajoutez une traduction pour le titre de la page des produits :

```
# config/locales/en.yml en: products: index: title: Our Products
```

```
# config/locales/ru.yml ru: products: index: title: Наши продукты
```

Maintenant, utilisez simplement ces traductions dans `views/products/index.html.erb` :

```
<!-- ... --> <h1><%= t '.title' %></h1> <!-- ... -->
```

Notez que nous pouvons tirer parti de la « recherche paresseuse » car les clés de traduction ont été nommées de la manière appropriée.

Traduisez d'autres contenus statiques si nécessaire, puis rechargez le serveur et assurez-vous que la locale peut être correctement changée. Super !

### Globalize, Globalize it Hard !

#### Définition des attributs pour la traduction

D'accord, le travail de base est terminé et nous pouvons passer à la partie suivante. Avant que Globalize puisse entrer en jeu, il doit être ajouté au `Gemfile` :

```
# ... gem 'globalize', git: 'https://github.com/globalize/globalize'
```

Au moment de la rédaction de cet article, la version stable n'était pas encore compatible avec Rails 5.2, nous devons donc installer directement depuis la branche `master`. Notez également que la dernière version stable ne prend pas en charge ActiveRecord 4.1 et versions antérieures, donc [consultez la documentation](https://github.com/globalize/globalize#installation) pour savoir quelle version de Globalize utiliser pour les versions plus anciennes d'AR.

Ensuite, vous devez décider quels attributs de modèle seront traduits avec Globalize. Nous allons traduire à la fois `:title` et `:description`, alors listez-les dans le modèle de la manière suivante :

```
# models/products.rb # ... translates :title, :description
```

Cela vous permettra de stocker les traductions dans la base de données par locale. Pour que cela fonctionne, cependant, vous devez également créer une _table de traduction_ spéciale.

#### Table de traduction

Donc, si vous créez un nouveau modèle et une migration, les choses sont aussi simples que d'utiliser une méthode `create_translation_table!` comme [expliqué ici](https://github.com/globalize/globalize#creating-translation-tables). Notre cas est un peu plus complexe, car nous avons déjà une table `products` avec certaines données. Par conséquent, il est nécessaire de déplacer ces données vers la table de traduction. Commencez par générer une nouvelle migration :

```
rails g migration translate_products
```

Maintenant, complétez-la avec le code suivant :

```
# db/migrate/xyz_translate_products.rb class TranslateProducts < ActiveRecord::Migration[5.2] def change reversible do |dir| # <=== 1 dir.up do Product.create_translation_table!({ # <=== 2 title: :string, # <=== 3 description: :text }, { migrate_data: true, # <=== 4 remove_source_columns: true # <=== 5 }) end dir.down do Product.drop_translation_table! migrate_data: true # <=== 6 end end end end
```

J'ai mis en évidence les principales choses à noter sur ce code :

1. Cela va être une migration réversible.
2. Nous créons une table de traduction pour le `Product`.
3. Listez soigneusement tous les champs qui doivent être traduits ainsi que leurs types. Comme vous vous en souvenez, ces champs ont été passés à la méthode `translates` à l'intérieur du modèle.
4. N'oubliez pas de fournir l'option `migrate_data` qui doit préserver vos enregistrements de base de données d'origine.
5. `remove_source_columns` garantira que les colonnes d'origine (`:title` et `:description`) seront supprimées de la table `products`. Vous pouvez également effectuer cette étape plus tard dans une migration séparée.
6. C'est l'action à effectuer lorsque la migration est annulée. Les données doivent également être préservées.

Exécutez la migration :

```
rails db:migrate
```

Après que cette commande ait terminé son travail, vous verrez une nouvelle table `product_translations` :

Comme vous le voyez, il y a une colonne `product_id` qui établit une relation avec le produit, et aussi un champ `locale` pour désigner la langue de cette traduction. Lorsque vous migrez vos données d'origine, elles seront associées à la locale par défaut de l'application (qui est l'anglais dans notre cas). Surchargez ce comportement en utilisant une méthode `with_locale`, par exemple :

```
I18n.with_locale(:ru) do Post.create_translation_table!(...) end
```

Si vous devez ajouter plus de champs traduits à la table plus tard, utilisez une méthode `add_translation_fields!` [comme montré dans cet exemple](https://github.com/globalize/globalize#adding-additional-fields-to-the-translation-table). De plus, n'oubliez pas de définir ces nouveaux champs dans le modèle.

#### Essayez-le !

À ce stade, Globalize est intégré à notre application et prêt à fonctionner ! Effectuez les étapes suivantes pour le voir en action :

* Rechargez votre serveur et essayez de créer un nouveau produit : son titre et sa description seront fournis pour la locale actuellement définie uniquement (anglais dans mon cas).
* Passez à la locale russe et assurez-vous que le titre et la description sont manquants pour le nouveau produit.
* Modifiez ce produit et entrez les valeurs pour la version russe du produit.

En résultat, vous devriez voir deux traductions stockées dans la table `product_translations` :

Excellent travail !

### Quelques fonctionnalités supplémentaires de Globalize

#### Replis

Que se passe-t-il si Globalize ne trouve pas d'attributs traduits pour la locale donnée ? Comme nous l'avons vu dans la section précédente, par défaut, il retournera des valeurs vides (qui sont en fait des `nil`). Cependant, il est possible d'activer les [replis I18n](https://github.com/globalize/globalize#i18n-fallbacks-for-empty-translations) et d'afficher les valeurs d'attributs d'une autre locale. Pour ce faire, activez simplement les replis dans le fichier `config/application.rb` :

```
# ... config.i18n.fallbacks = true
```

Maintenant, lorsque l'attribut traduit est `nil`, Globalize essaiera de charger les valeurs d'une autre locale. Pour vous assurer que cette fonctionnalité fonctionne, rechargez le serveur, créez un nouveau produit, puis passez à une autre langue. Le titre et la description doivent revenir à une autre locale.

Si vous souhaitez utiliser des replis lorsque les valeurs de traduction sont également vides (non `nil`), définissez l'option `fallbacks_for_empty_translations` sur `true` :

```
# models/product.rb # ... translates :title, :description, fallbacks_for_empty_translations: true
```

Notez également qu'il est possible de définir une chaîne de replis personnalisée globalement de la manière suivante :

```
# quelque part dans un initialiseur Globalize.fallbacks = {:en => [:de, :ru]}
```

#### Portée et Contexte

Globalize fournit une portée de modèle spéciale appelée `with_translations` qui peut être utilisée pour charger les traductions pour une langue donnée. Dans cet exemple, nous chargeons toutes les traductions pour la locale anglaise uniquement :

```
Product.with_translations('en')
```

En plus de cela, il est possible d'afficher la traduction pour une locale souhaitée dans vos vues. Pour ce faire, utilisez une méthode `with_locale` :

```
<% Globalize.with_locale(:en) do %> <!-- rendre votre contenu ici... --> <% end %>
```

#### Interpolation

Ce qui est intéressant, c'est que Globalize prend même en charge l'interpolation dans les attributs traduits. Cela fonctionne de la même manière que l'interpolation dans les fichiers de traduction YAML :

```
product.title = "Product for %{someone}" product.title someone: "John" # => "Product for John"
```

Donc, le placeholder ici est `%{someone}`. Pour fournir sa valeur, passez simplement un hash à l'attribut de modèle approprié. Vraiment pratique !

### Conclusion

Dans cette section, nous avons vu comment stocker les traductions dans une base de données avec l'aide de la solution Globalize. Nous avons discuté de ses bases, vu comment l'installer et le configurer, comment migrer les données correctement, comment définir les traductions, fournir des replis et utiliser les portées. Dans l'ensemble, nous avons couvert presque tout ce que Globalize a à offrir, et vous pouvez maintenant appliquer ces concepts en pratique ! De plus, n'oubliez pas que Globalize peut fonctionner en toute sécurité avec les fichiers YAML, vous pouvez donc mélanger et assortir ces approches comme vous le jugez approprié.

Quelle solution utilisez-vous pour internationaliser le contenu généré par les utilisateurs ? Donnerez-vous une chance à Globalize ? Partagez vos pensées dans la section des commentaires !

### Facilitez-vous la vie avec Lokalise

Prendre en charge plusieurs langues sur un grand site web peut devenir un vrai casse-tête. Vous devez vous assurer que toutes les clés sont traduites pour chaque locale. Heureusement, il existe une solution à ce problème : la plateforme Lokalise qui [rend le travail avec les fichiers de localisation beaucoup plus simple](https://lokalise.co/features). Laissez-moi vous guider à travers la configuration initiale qui n'est vraiment pas complexe.

* Pour commencer, [obtenez votre essai gratuit](https://lokalise.co/signup)
* Créez un nouveau projet, donnez-lui un nom et définissez l'anglais comme langue de base
* Cliquez sur « Upload Language Files »
* Téléchargez les fichiers de traduction pour toutes vos langues
* Passez au projet et modifiez vos traductions selon vos besoins
* Vous pouvez également contacter un traducteur professionnel pour faire le travail à votre place
* Ensuite, téléchargez simplement vos fichiers
* Profitez !

Lokalise a de nombreuses autres fonctionnalités, y compris la prise en charge de dizaines de plateformes et de formats, et même la possibilité de télécharger des captures d'écran afin de lire les textes à partir de celles-ci. Donc, restez avec Lokalise et facilitez-vous la vie !

*Publié à l'origine sur [blog.lokalise.co](https://blog.lokalise.co/store-translations-inside-database-globalize/) le 16 novembre 2018.*