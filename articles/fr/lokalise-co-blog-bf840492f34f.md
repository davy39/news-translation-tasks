---
title: Le guide complet de l'internationalisation Rails (i18n)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-23T11:17:13.000Z'
originalURL: https://freecodecamp.org/news/lokalise-co-blog-bf840492f34f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oNjw5BDpdjHzMGKwIyWmQA.jpeg
tags:
- name: internationalization
  slug: internationalization
- name: localization
  slug: localization
- name: Ruby on Rails
  slug: ruby-on-rails
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Le guide complet de l'internationalisation Rails (i18n)
seo_desc: 'By Anastasia

  In this article you are going to learn how to translate your Rails application into
  multiple languages, work with translations, localize datetime, and switch locales.
  We are going to see all these aspects in action by creating a sample a...'
---

Par Anastasia

Dans cet article, vous allez apprendre à traduire votre [application Rails](https://rubyonrails.org/) en plusieurs langues, travailler avec des traductions, localiser la date et l'heure, et changer de locales. Nous allons voir tous ces aspects en action en créant une application d'exemple et en l'améliorant étape par étape. À la fin de l'article, vous aurez toutes les connaissances nécessaires pour commencer à implémenter ces concepts dans des projets réels.

### Préparation de votre application Rails

Comme je l'ai déjà dit, nous allons voir tous les concepts en action, donc créons une nouvelle application Rails en exécutant :

```
rails new SampleApp
```

Pour ce tutoriel, j'utilise _Rails 5.2.1_, mais la plupart des concepts décrits s'appliquent également aux versions plus anciennes.

Maintenant, générons un `StaticPagesController` qui aura une action `index` (notre page principale) :

```
rails g controller StaticPages index
```

Modifiez la vue `views/static_pages/index.html.erb` en ajoutant un contenu d'exemple :

```
<h1>Bienvenue !</h1> <p>Nous offrons des services sophistiqués à des <em>bonnes personnes</em>.</p>
```

J'aimerais également ajouter une page de Feedback où nos utilisateurs pourront partager leur opinion (espérons-le, positive) sur l'entreprise. Chaque feedback aura un nom d'auteur et le message réel :

```
rails g scaffold Feedback author message
```

Nous nous intéresserons uniquement à deux actions : `new` (qui va rendre le formulaire pour poster un avis et lister également tous les avis existants) et `create` (pour valider et persister les avis). Bien sûr, idéalement, les avis devraient être pré-moderés, mais nous ne nous en occuperons pas aujourd'hui.

Modifiez l'action `new` pour récupérer tous les avis de la base de données et les trier par date de création :

```
# feedbacks_controller.rb # ... def new @feedback = Feedback.new @feedbacks = Feedback.order created_at: :desc end
```

J'aimerais également rediriger l'utilisateur vers la page de Feedback lorsque le formulaire est traité et que le nouvel enregistrement est persistant :

```
# feedbacks_controller.rb # ... def create @feedback = Feedback.new(feedback_params) if @feedback.save redirect_to new_feedback_path else @feedbacks = Feedback.order created_at: :desc render :new end end
```

Rendez la collection de feedbacks sur la page `new` :

```
<!-- views/feedbacks/new.html.erb --> <!-- autre code ici... --> <%= render @feedbacks %>
```

Enfin, créez un partial pour un feedback individuel :

```
<!-- views/feedbacks/_feedback.html.erb --> <article> <em> <%= tag.time feedback.created_at, datetime: feedback.created_at %><br> Posté par <%= feedback.author %> </em> <p> <%= feedback.message %> </p> <hr> </article>
```

Occupez-vous des routes :

```
# config/routes.rb Rails.application.routes.draw do resources :feedbacks root 'static_pages#index' end
```

Enfin, ajoutez un menu global au layout :

```
<!-- views/layouts/application.html.erb --> <!-- autre code ici... --> <nav> <ul> <li><%= link_to 'Accueil', root_path %></li> <li><%= link_to 'Feedback', new_feedback_path %></li> </ul> </nav>
```

Maintenant, exécutez les migrations et démarrez le serveur :

```
rails db:migrate rails s
```

Naviguez vers `http://locahost:3000` et assurez-vous que tout est correct. Maintenant que nous avons quelque chose avec quoi travailler, procédons à la partie principale et localisons notre application.

### Un peu de configuration

Avant de réaliser des traductions, nous devons décider quelles langues seront supportées. Vous pouvez choisir n'importe lesquelles, mais je vais me limiter au russe et à l'anglais, ce dernier étant défini comme langue par défaut. Reflétez cela dans le fichier `config/application.rb` :

```
# ... config.i18n.available_locales = [:en, :ru] config.i18n.default_locale = :en
```

Ajoutez également le gem [rails-i18n](https://github.com/svenfuchs/rails-i18n) qui contient des données de locale pour [différentes langues](https://github.com/svenfuchs/rails-i18n#available-locales). Par exemple, il contient des noms de mois traduits, des règles de pluriel, et d'autres choses utiles.

```
# Gemfile # ... gem 'rails-i18n'
```

Installez simplement ce gem et vous êtes prêt à partir :

```
bundle install
```

### Stocker les traductions

Maintenant que tout est configuré, occupons-nous de la page d'accueil et traduisons le texte qui s'y trouve.

La manière la plus simple de faire cela est d'utiliser des [vues localisées](https://guides.rubyonrails.org/i18n.html#localized-views). Tout ce que vous avez à faire est de créer des vues nommées `index.CODE_LANGUE.html.erb`, où le `CODE_LANGUE` correspond à l'une des langues supportées. Donc, dans cette démonstration, nous devrions créer deux vues : `index.en.html.erb` et `index.ru.html.erb`. À l'intérieur, placez simplement le contenu pour les versions anglaise et russe du site, et Rails choisira automatiquement la vue appropriée en fonction de la locale actuellement définie. Pratique, n'est-ce pas ?

Cette approche, cependant, n'est pas toujours réalisable. Une autre manière serait de stocker vos chaînes traduites dans un fichier séparé, et de rendre une version appropriée de la chaîne en fonction de la langue choisie. Par défaut, Rails utilise des [fichiers YAML](https://en.wikipedia.org/wiki/YAML) qui doivent être stockés dans le répertoire `config/locales`. Les traductions pour différentes langues sont stockées dans des fichiers séparés, et chaque fichier est nommé d'après cette langue.

Ouvrez le dossier `config/locales` et notez qu'il y a déjà un fichier `en.yml` à l'intérieur qui contient quelques données d'exemple :

```
en: hello: "Hello world"
```

Donc, `en` est une clé de premier niveau représentant la langue pour laquelle ces traductions sont destinées. Ensuite, il y a une paire clé-valeur imbriquée, où `hello` est la _clé de traduction_, et `Hello world` est la chaîne traduite réelle. Remplaçons cette paire par le contenu suivant :

```
en: welcome: "Bienvenue !"
```

C'est juste un message de bienvenue de notre page d'accueil. Maintenant, créez un fichier `ru.yml` dans le dossier `config/locales` et fournissez également un message de bienvenue traduit :

```
ru: welcome: "Добро пожаловать!"
```

Nous venons de créer une traduction pour notre première chaîne, ce qui est vraiment génial.

### Réaliser des traductions simples

Maintenant que nous avons peuplé les fichiers YAML avec quelques données, voyons comment employer les chaînes traduites dans les vues. En fait, c'est aussi simple que d'utiliser la méthode `translate` qui est aliasée en `t`. Cette méthode a un argument requis : le nom de la clé de traduction :

```
<!-- views/static_pages/index.html.erb --> <h1><%= t 'welcome' %></h1>
```

Lorsque la page est demandée, Rails recherche la chaîne qui correspond à la clé fournie, et la rend. Si la traduction demandée ne peut pas être trouvée, Rails rendra simplement la clé à l'écran (et la transformera en une forme plus lisible).

Les clés de traduction peuvent être nommées comme vous le souhaitez (eh bien, presque n'importe quoi), mais il est bien sûr conseillé de leur donner des noms significatifs afin que vous puissiez comprendre à quel texte elles correspondent.

Occupons-nous du deuxième message :

```
en: welcome: "Bienvenue !" services_html: "Nous offrons des services sophistiqués à des <em>bonnes personnes</em>."
```

```
ru: welcome: "Добро пожаловать!" services_html: "Мы предоставляем различные услуги для <em>хороших людей</em>."
```

Pourquoi avons-nous besoin de ce suffixe `_html` ? Eh bien, comme vous pouvez le voir, notre chaîne contient du balisage HTML, et par défaut Rails rendra la balise `em` comme du texte brut. Tant que nous ne voulons pas que cela se produise, nous marquons la chaîne comme étant du « HTML sûr ».

Maintenant, utilisez simplement la méthode `t` à nouveau :

```
<!-- views/static_pages/index.html.erb --> <!-- ... ---> <p><%= t 'services_html' %></p>
```

### Plus sur les clés de traduction

Notre page d'accueil est maintenant localisée, mais arrêtons-nous un instant et réfléchissons à ce que nous avons fait. Après tout, nos clés de traduction ont des noms significatifs, mais que se passe-t-il si nous allons avoir, disons, 500 messages dans l'application ? Ce nombre n'est en fait pas si grand, et les grands sites Web peuvent avoir des milliers de traductions.

Si toutes nos paires clé-valeur sont stockées directement sous la clé `en` (ou `ru`) sans aucun autre regroupement, cela conduit à deux problèmes principaux :

* Nous devons nous assurer que toutes les clés ont des noms uniques. Cela devient de plus en plus complexe à mesure que votre application grandit.
* Il est difficile de localiser toutes les traductions liées (par exemple, les traductions pour une seule page ou fonctionnalité).

Par conséquent, il serait bon de regrouper davantage vos traductions sous des clés arbitraires. Par exemple, vous pouvez faire quelque chose comme ceci :

```
en: main_page: header: welcome: "Le message de bienvenue va ici"
```

Le niveau de nesting n'est pas limité (mais vous devez être raisonnable à ce sujet), et les clés dans différents groupes peuvent avoir des noms identiques.

Cependant, il est bénéfique de suivre la structure de dossiers de vos vues (dans un instant, nous verrons pourquoi). Par conséquent, modifiez les fichiers YAML de la manière suivante :

```
en: static_pages: index: welcome: "Bienvenue !" services_html: "Nous offrons des services sophistiqués à des <em>bonnes personnes</em>."
```

```
ru: static_pages: index: welcome: "Добро пожаловать!" services_html: "Мы предоставляем различные услуги для <em>хороших людей</em>."
```

Généralement, vous devez fournir le chemin complet de la clé de traduction lorsque vous y faites référence dans la méthode `t` :

```
<!-- views/static_pages/index.html.erb --> <h1><%= t 'static_pages.index.welcome' %></h1> <p><%= t 'static_pages.index.services_html' %></p>
```

Cependant, il existe également une recherche « paresseuse » disponible. Si vous effectuez une traduction dans une vue ou un contrôleur, et que les clés de traduction sont correctement namespacées en suivant la structure des dossiers, vous pouvez omettre les namespaces. Ainsi, le code ci-dessus devient :

```
<!-- views/static_pages/index.html.erb --> <h1><%= t '.welcome' %></h1> <p><%= t '.services_html' %></p>
```

Notez que le point initial est requis ici.

Traduisons également notre menu global et namespacons correctement les traductions :

```
en: global: menu: home: "Accueil" feedback: "Feedback"
```

```
ru: global: menu: home: "Главная" feedback: "Отзывы"
```

Dans ce cas, nous ne pouvons pas profiter de la recherche paresseuse, donc fournissez le chemin complet :

```
<!-- views/layouts/application.html.erb --> <!-- ... ---> <nav> <ul> <li><%= link_to t('global.menu.home'), root_path %></li> <li><%= link_to t('global.menu.feedback'), new_feedback_path %></li> </ul> </nav>
```

### Traduire les modèles

Maintenant, procédons à la page de Feedback et occupons-nous du formulaire. La première chose que nous devons traduire est les étiquettes des champs. Il semble que Rails nous permette de fournir des traductions pour les attributs du modèle, et elles seront automatiquement utilisées selon les besoins. Tout ce que vous avez à faire est de namespacer correctement ces traductions :

```
en: activerecord: attributes: feedback: author: "Votre nom" message: "Message"
```

```
ru: activerecord: attributes: feedback: author: "Ваше имя" message: "Сообщение"
```

Les étiquettes seront maintenant traduites automatiquement. Quant au bouton « submit », vous pouvez fournir une traduction pour le modèle lui-même en disant :

```
en: activerecord: models: feedback: "Feedback"
```

Mais honnêtement, je n'aime pas le texte « Create Feedback » sur ce bouton, alors restons avec un mot générique « Submit » :

```
en: global: forms: submit: Submit
```

```
ru: global: forms: submit: Отправить
```

Maintenant, utilisez cette traduction :

```
<!-- views/feedbacks/_form.html.erb --> <!-- ... ---> <%= form.submit t('global.forms.submit') %>
```

### Messages d'erreur

Probablement, nous ne voulons pas que les visiteurs postent des messages de feedback vides, donc fournissez quelques règles de validation simples :

```
# models/feedback.rb # ... validates :author, presence: true validates :message, presence: true, length: {minimum: 5}
```

Mais qu'en est-il des messages d'erreur correspondants ? Comment les traduisons-nous ? Il semble que nous n'ayons rien à faire du tout, car le gem rails-i18n sait déjà comment localiser les erreurs courantes. Par exemple, [ce fichier](https://github.com/svenfuchs/rails-i18n/blob/master/rails/locale/ru.yml#L133) contient des messages d'erreur pour la locale russe. Si vous voulez vraiment modifier les messages d'erreur par défaut, alors [consultez la documentation officielle](https://guides.rubyonrails.org/i18n.html#error-message-scopes) qui explique comment y parvenir.

Un problème avec le formulaire, cependant, est que le sous-titre des messages d'erreur (celui qui dit « _N_ erreurs ont empêché ce feedback d'être sauvegardé : ») n'est pas traduit. Corrigons cela maintenant et parlons également de la pluralisation.

### Règles de pluralisation

Puisque potentiellement il peut y avoir une ou plusieurs erreurs, le mot « erreur » dans le sous-titre doit être pluralisé en conséquence. En anglais, les mots sont généralement pluralisés en ajoutant un suffixe « s », mais pour le russe, les règles sont un peu plus complexes.

J'ai déjà mentionné que le gem rails-i18n contient des règles de pluralisation pour toutes les langues supportées, donc nous n'avons pas besoin de nous soucier de les écrire à partir de zéro. Tout ce que vous avez à faire est de fournir la clé appropriée pour chaque cas possible. Donc, pour l'anglais, il n'y a que deux cas possibles : une erreur ou plusieurs erreurs (bien sûr, il peut ne pas y avoir d'erreurs, mais dans ce cas, le message ne sera pas affiché du tout).

```
en: global: forms: submit: Submit messages: errors: one: "Une erreur a empêché ce feedback d'être sauvegardé" other: "%{count} erreurs ont empêché ce feedback d'être sauvegardé"
```

Le `%{count}` ici est une interpolation – nous prenons la valeur passée et la plaçons directement dans la chaîne.

Maintenant, occupez-vous de la locale russe qui a plus de cas possibles :

```
ru: global: forms: submit: Отправить messages: errors: one: "Не удалось сохранить отзыв! Найдена одна ошибка:" few: "Не удалось сохранить отзыв! Найдены %{count} ошибки:" many: "Не удалось сохранить отзыв! Найдено %{count} ошибок:" other: "Не удалось сохранить отзыв! Найдена %{count} ошибка:"
```

Ayant cela en place, utilisez simplement ces traductions :

```
<!-- views/feedbacks/_form.html.erb --> <!-- ... ---> <%= form_with(model: feedback, local: true) do |form| %> <% if feedback.errors.any? %> <div id="error_explanation"> <h2><%= t 'global.forms.messages.errors', count: feedback.errors.count %></h2> <!-- erreurs... --> </ul> </div> <% end %> <!-- champs du formulaire --> <% end %>
```

Notez que dans ce cas, nous passons la clé de traduction ainsi que la valeur pour la variable `count`. Rails prendra la variante de traduction appropriée en fonction de ce nombre. De plus, la valeur de `count` sera interpolée dans chaque espace réservé `%{count}`.

Notre prochaine étape est le partial `_feedback.html.erb`. Ici, nous devons localiser deux chaînes : « Posté par... » et la date et l'heure (`created_at`). Pour « Posté par... », utilisons simplement l'interpolation à nouveau :

```
en: global: feedback: posted_by: "Posté par %{author}"
```

```
ru: global: feedback: posted_by: "Автор: %{author}"
```

```
<!-- views/feedbacks/_feedback.html.erb --> <article> <em> <%= tag.time feedback.created_at, datetime: feedback.created_at %><br> <%= t 'global.feedback.posted_by', author: feedback.author %> </em> <p> <%= feedback.message %> </p> <hr> </article>
```

Mais qu'en est-il de `created_at` ? Pour en prendre soin, nous pouvons tirer parti de la méthode `localize` aliasée simplement `l`. Elle est très similaire à `strftime` de Ruby, mais produit une version traduite de la date (spécifiquement, les noms des mois sont traduits correctement). Utilisons un [format prédéfinis](https://github.com/svenfuchs/rails-i18n/blob/master/rails/locale/ru.yml#L265) appelé `:long` :

```
<!-- views/feedbacks/_feedback.html.erb --> <article> <em> <%= tag.time l(feedback.created_at, format: :long), datetime: feedback.created_at %><br> <%= t 'global.feedback.posted_by', author: feedback.author %> </em> <!--... --> </article>
```

Si vous souhaitez ajouter votre propre format, c'est également possible [comme expliqué ici](https://guides.rubyonrails.org/i18n.html#adding-date-time-formats).

### Changer de locales

Donc, notre application est maintenant entièrement traduite... mais il y a une toute petite chose : nous ne pouvons pas changer de locale ! À y réfléchir, c'est en fait un problème assez majeur, alors corrigeons-le maintenant.

Il existe [plusieurs façons possibles](https://guides.rubyonrails.org/i18n.html#managing-the-locale-across-requests) de définir et de persister la locale choisie à travers les requêtes. Nous allons nous en tenir à l'approche suivante :

* Nos URL auront un paramètre optionnel `:locale`, et donc elles ressembleront à `[http://localhost:3000/en/some_page](http://localhost:3000/en/some_page)`
* Si ce paramètre est défini et que la locale spécifiée est supportée, nous traduisons l'application dans la langue correspondante
* Si ce paramètre n'est pas défini ou si la locale n'est pas supportée, définissez une locale par défaut

Cela semble simple ? Alors plongeons dans le code !

Tout d'abord, modifiez le `routes.rb` en incluant une `scope` :

```
# config/routes.rb scope "(:locale)", locale: /#{I18n.available_locales.join("|")}/ do # vos routes ici... end
```

Ici, nous validons le paramètre spécifié en utilisant une RegEx pour nous assurer que la locale est supportée (notez que les caractères d'ancrage comme `\A` ne sont pas autorisés ici).

Ensuite, définissez un `before_action` dans le `ApplicationController` pour vérifier et définir la locale à chaque requête :

```
# application_controller.rb # ... before_action :set_locale private def set_locale I18n.locale = extract_locale || I18n.default_locale end def extract_locale parsed_locale = params[:locale] I18n.available_locales.map(&:to_s).include?(parsed_locale) ? parsed_locale : nil end
```

De plus, afin de persister la locale choisie à travers les requêtes, définissez les `default_url_options` :

```
# application_controller.rb # ... private def default_url_options { locale: I18n.locale } end
```

Cela va inclure le paramètre `locale` dans chaque lien généré avec les helpers Rails.

La dernière étape est de présenter deux liens pour changer de locales :

```
<!-- views/layouts/application.html.erb --> <!-- ... --> <nav> <ul> <li><%= link_to t('global.menu.home'), root_path %></li> <li><%= link_to t('global.menu.feedback'), new_feedback_path %></li> </ul> <ul> <li><%= link_to 'English', root_path(locale: :en) %></li> <li><%= link_to 'Русский', root_path(locale: :ru) %></li> </ul> </nav>
```

En guise d'exercice, vous pouvez rendre ces liens plus élégants et, par exemple, rediriger l'utilisateur vers la page qu'il consultait.

### Simplifiez votre vie avec Lokalise

Maintenant, vous pensez probablement que supporter plusieurs langues sur un grand site web est probablement une corvée. Et, honnêtement, vous avez raison. Bien sûr, les traductions peuvent être namespacées, et [même divisées en plusieurs fichiers YAML](https://guides.rubyonrails.org/i18n.html#organization-of-locale-files) si nécessaire, mais vous devez toujours vous assurer que toutes les clés sont traduites pour chaque locale.

Heureusement, il existe une solution à ce problème : la plateforme Lokalise qui [rend le travail avec les fichiers de localisation beaucoup plus simple](https://lokalise.co/features). Laissez-moi vous guider à travers la configuration initiale qui n'est vraiment pas complexe.

* Pour commencer, [obtenez votre essai gratuit](https://lokalise.co/signup)
* [Installez Lokalise CLI](https://docs.lokalise.co/api-and-cli/lokalise-cli-tool) qui sera utilisé pour télécharger et téléverser des fichiers de traduction
* Ouvrez votre [page de profil personnel](https://lokalise.co/profile), naviguez jusqu'à la section « API tokens », et générez un jeton de lecture/écriture
* Créez un nouveau projet, donnez-lui un nom, et définissez l'anglais comme langue de base
* Sur la page du projet, cliquez sur le bouton « More » et choisissez « Settings ». Sur cette page, vous devriez voir l'ID du projet
* Maintenant, depuis la ligne de commande, exécutez simplement `lokalise --token <token> import <project_id> --lang_iso en --file config/locales/en.yml` en fournissant votre jeton généré et l'ID du projet (sur Windows, vous devrez peut-être également fournir le chemin complet du fichier). Cela devrait téléverser la traduction anglaise vers Lokalise. Exécutez la même commande pour la locale russe.
* Naviguez de nouveau vers la page d'aperçu du projet. Vous devriez voir toutes vos clés et valeurs de traduction là. Bien sûr, il est possible de les éditer, de les supprimer, ainsi que d'en ajouter de nouvelles. Ici, vous pouvez également filtrer les clés et, par exemple, trouver celles qui ne sont pas traduites, ce qui est vraiment pratique.
* Après avoir terminé l'édition des traductions, téléchargez-les en exécutant `lokalise --token <token> export <project_id> --type yaml --bundle_structure %LANG_ISO%.yml --unzip_to E:/Supreme/docs/work/lokalise/rails/SampleApp/config/locales/`. Super !

Lokalise a de nombreuses autres fonctionnalités, y compris le support de dizaines de plateformes et de formats, la possibilité de commander des traductions auprès de professionnels, et même la possibilité de téléverser des captures d'écran afin de lire les textes qui s'y trouvent. Donc, restez avec Lokalise et facilitez-vous la vie !

### Conclusion

Dans cet article, nous avons discuté en détail de la manière d'introduire le support de l'internationalisation dans les applications Rails et nous l'avons implémenté nous-mêmes. Vous avez appris comment et où stocker les traductions, comment les rechercher, ce que sont les vues localisées, comment traduire les messages d'erreur et les éléments liés à ActiveRecord, ainsi que comment changer de locales et persister la locale choisie parmi les requêtes. Pas mal pour aujourd'hui, n'est-ce pas ?

Bien sûr, il est impossible de couvrir tous les tenants et aboutissants de Rails I18n dans un seul article, et je vous recommande donc de consulter [le guide officiel](https://guides.rubyonrails.org/i18n.html) qui donne des informations plus détaillées sur le sujet et fournit des exemples utiles.

_Publié à l'origine sur [blog.lokalise.co](https://blog.lokalise.co/rails-i18n/) le 23 août 2018._