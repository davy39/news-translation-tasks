---
title: 'Le tutoriel ultime Ruby on Rails de niveau intermédiaire : Créons une application
  complète !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-16T21:57:00.000Z'
originalURL: https://freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f
coverImage: https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_UH-HEG_VCXKMShU5iRbtFw-2.png
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: 'Le tutoriel ultime Ruby on Rails de niveau intermédiaire : Créons une
  application complète !'
seo_desc: 'By Domantas G


  There are plenty tutorials online which show how to create your first app. This
  tutorial will go a step further and explain line-by-line how to create a more complex
  Ruby On Rails application.

  Throughout the whole tutorial, I will grad...'
---

### Par Domantas G

![Image](https://s3.amazonaws.com/cdn-media-1.freecodecamp.org/ghost/2019/05/1_UH-HEG_VCXKMShU5iRbtFw-1.png)

Il existe de nombreux tutoriels en ligne qui montrent comment créer votre première application. Ce tutoriel ira un peu plus loin et expliquera ligne par ligne comment créer une application Ruby On Rails plus complexe.

Tout au long de ce tutoriel, j'introduirai progressivement de nouvelles techniques et de nouveaux concepts. L'idée est qu'à chaque nouvelle section, vous appreniez quelque chose de nouveau.

Les sujets suivants seront abordés tout au long de ce guide :

* Les bases de Ruby On Rails
* Refactorisation : helpers, partiels, concerns, patrons de conception (design patterns)
* Tests : TDD/BDD (RSpec & Capybara), Factories (Factory Girl)
* Action Cable
* Active Job
* CSS, Bootstrap, JavaScript, jQuery

#### **Alors, de quoi va parler l'application ?**

Il s'agira d'une plateforme où vous pourrez rechercher et rencontrer des personnes partageant les mêmes idées.

Principales fonctionnalités que l'application possédera :

* Authentification (avec Devise)
* Possibilité de publier des articles, de les rechercher et de les catégoriser
* Messagerie instantanée (fenêtres contextuelles et un messenger séparé), avec la possibilité de créer des conversations privées et de groupe.
* Possibilité d'ajouter des utilisateurs aux contacts
* Notifications en temps réel

**Vous pouvez voir à quoi ressemblera l'** [**application complète**](https://www.youtube.com/watch?time_continue=10&v=KkgJRe7df04)**.**

**Et vous pouvez trouver le code source complet du projet sur** [**GitHub**](https://github.com/domagude/collabfield)**.**

**Table des matières**

1. **[Introduction et Installation](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#alors-de-quoi-va-parler-lapplication)** [Prérequis](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#prérequis) [Installation](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#installation) [Créer une nouvelle application](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#créer-une-nouvelle-application)
2. **[Mise en page](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#mise-en-page)** [Page d'accueil](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#page-daccueil) [Bootstrap](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#bootstrap) [Barre de navigation](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#barre-de-navigation) [Feuilles de style](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#feuilles-de-style)
3. **[Articles](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#articles)** [Authentification](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#authentification) [Helpers](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#helpers) [Tests](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#tests) [Flux principal](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#flux-principal) [Article unique](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#article-unique) [Branches spécifiques](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#branches-spécifiques) [Service objects](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#service-objects) [Créer un nouvel article](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#créer-un-nouvel-article)
4. **[Messagerie instantanée](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#messagerie-instantanée)** [Conversation privée](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#conversation-privée) [Contacts](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#contacts) [Conversation de groupe](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#conversation-de-groupe) [Messenger](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#messenger)
5. **[Notifications](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#notifications)** [Demandes de contact](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#demandes-de-contact) [Conversations](https://www.freecodecamp.org/news/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f/#conversations)

### Prérequis

J'essaierai d'expliquer chaque ligne de code et comment j'en suis arrivé aux solutions. Je pense qu'il est tout à fait possible pour un débutant complet de suivre ce guide. Mais gardez à l'esprit que ce tutoriel couvre certains sujets qui vont au-delà des bases.

Donc, si vous êtes un débutant total, ce sera plus difficile, car votre courbe d'apprentissage sera assez raide. Je fournirai des liens vers des ressources où vous pourrez obtenir des informations supplémentaires sur chaque nouveau concept que nous aborderons.

Idéalement, il est préférable que vous connaissiez les bases de :

* [HTML](https://www.w3schools.com/html/), [CSS](https://www.w3schools.com/css/), [Bootstrap](https://getbootstrap.com/docs/3.3/getting-started/), [JavaScript](https://www.w3schools.com/js/), [jQuery](https://www.w3schools.com/jquery/)
* [Ruby](https://www.tutorialspoint.com/ruby/), [Ruby On Rails](http://guides.rubyonrails.org/getting_started.html)
* [Git](https://www.tutorialspoint.com/git/git_quick_guide.htm)

### Installation

Je suppose que vous avez déjà configuré votre environnement de développement Ruby On Rails de base. Sinon, consultez [RailsInstaller](http://railsinstaller.org/en).

J'ai développé sur Windows 10 pendant un certain temps. Au début, c'était correct, mais après un certain temps, j'en ai eu assez de surmonter des obstacles mystiques causés par Windows. Je devais sans cesse trouver des solutions de contournement pour faire fonctionner mes applications. J'ai réalisé que cela n'en valait pas la peine. Surmonter ces obstacles ne m'apportait aucune compétence ou connaissance précieuse. Je passais juste mon temps à bricoler l'installation de Windows 10.

Je suis donc passé à une [machine virtuelle](https://en.wikipedia.org/wiki/Virtual_machine) à la place. J'ai choisi d'utiliser [Vagrant](https://www.vagrantup.com/) pour créer un environnement de développement et [PuTTY](http://www.putty.org/) pour me connecter à la machine virtuelle. Si vous voulez aussi utiliser Vagrant, voici le [tutoriel](https://www.youtube.com/watch?v=qjCMtR2Z-kA&t=) que j'ai trouvé utile.

### Créer une nouvelle application

Nous allons utiliser PostgreSQL comme base de données. C'est un choix populaire au sein de la communauté Ruby On Rails. Si vous n'avez pas encore créé d'applications Rails avec PostgreSQL, vous voudrez peut-être consulter ce [tutoriel](https://www.digitalocean.com/community/tutorials/how-to-setup-ruby-on-rails-with-postgres).

Une fois que vous êtes familiarisé avec PostgreSQL, naviguez vers le répertoire où vous gardez vos projets et ouvrez une invite de commande.

Pour générer une nouvelle application, exécutez cette ligne :

```bash
rails new collabfield --database=postgresql
```

`**Collabfield**`, c'est ainsi que notre application va s'appeler. Par défaut, Rails utilise SQlite3, mais comme nous voulons utiliser PostgreSQL comme base de données, nous devons le spécifier en ajoutant :

```bash
--database=postgresql
```

Maintenant, nous devrions avoir généré avec succès une nouvelle application.

Naviguez vers le répertoire nouvellement créé en exécutant la commande :

```bash
cd collabfield
```

Et maintenant, nous pouvons lancer notre application en saisissant :

```bash
rails s
```

Nous venons de démarrer notre application. Nous devrions maintenant pouvoir voir ce que nous avons jusqu'à présent. Ouvrez un navigateur et allez sur [http://localhost:3000](http://localhost:3000/). Si tout s'est bien passé, vous devriez voir la page d'accueil signature de Rails.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-58.png)

## Mise en page

Il est temps de coder. Par où commencer ? Eh bien, nous pouvons commencer où nous voulons. Quand je construis un nouveau site web, j'aime commencer par créer une sorte de structure visuelle de base, puis construire tout le reste autour de cela. Faisons exactement cela.

### Page d'accueil

Lorsque nous allons sur [http://localhost:3000](http://localhost:3000/), nous voyons la page d'accueil de Rails. Nous allons remplacer cette page par défaut par notre propre page d'accueil. Pour ce faire, générez un nouveau contrôleur appelé `Pages`. Si vous n'êtes pas familier avec les contrôleurs Rails, vous devriez parcourir rapidement [Action Controller](http://guides.rubyonrails.org/action_controller_overview.html) pour avoir une idée de ce qu'est un contrôleur Rails. Exécutez cette ligne dans votre invite de commande pour générer un nouveau contrôleur.

```bash
rails g controller pages
```

Ce générateur Rails devrait avoir créé quelques fichiers pour nous. La sortie dans l'invite de commande devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-59.png)

Nous allons utiliser ce `PagesController` pour gérer nos pages spéciales et statiques. Maintenant, ouvrez le projet Collabfield dans un éditeur de texte. J'utilise [Sublime Text](https://www.sublimetext.com/), mais vous pouvez utiliser celui que vous voulez.

Ouvrez le fichier `pages_controller.rb` :

```rb
app/controllers/pages_controller.rb
```

Nous définirons notre page d'accueil ici. Bien sûr, nous pourrions définir la page d'accueil dans un contrôleur différent et de différentes manières. Mais généralement, j'aime définir la page d'accueil à l'intérieur du `PagesController`.

Quand nous ouvrons `pages_controller.rb`, nous voyons ceci :

```rb
class PagesController < ApplicationController
end
```

C'est une classe vide, nommée `PagesController`, qui hérite de la classe `ApplicationController`. Vous pouvez trouver le code source de cette classe dans `app/controllers/application_controller.rb`.

Tous nos contrôleurs, que nous allons créer, vont hériter de la classe `ApplicationController`. Ce qui signifie que toutes les méthodes définies à l'intérieur de cette classe seront disponibles dans tous nos contrôleurs.

Nous allons définir une méthode publique nommée `index`, afin qu'elle puisse être appelée en tant qu'action :

```rb
class PagesController < ApplicationController

  def index
  end

end
```

Comme vous l'avez peut-être lu dans [Action Controller](https://guides.rubyonrails.org/action_controller_overview.html), le routage détermine quel contrôleur et quelle méthode publique (action) appeler. Définissons une route pour que, lorsque nous ouvrons la page racine de notre site web, Rails sache quel contrôleur et quelle action appeler. Ouvrez le fichier `routes.rb` dans `config/routes.rb`.

Si vous ne savez pas ce que sont les routes Rails, c'est le moment idéal pour vous familiariser en lisant le Rails Routing.

Insérez cette ligne :

```rb
root to: 'pages#index'
```

Votre fichier `routes.rb` devrait ressembler à ceci :

```rb
Rails.application.routes.draw do
  root to: 'pages#index'
end
```

Le symbole dièse `#` en Ruby représente une méthode. Comme vous vous en souvenez, une action est juste une méthode publique, donc `pages#index` signifie « appelle le `PagesController` et sa méthode publique (action) `index` ».

Si nous allions sur notre chemin racine [http://localhost:3000](http://localhost:3000/), l'action index serait appelée. Mais nous n'avons pas encore de templates à afficher. Créons donc un nouveau template pour notre action `index`. Allez dans `app/views/pages` et créez un fichier `index.html.erb` à l'intérieur de ce répertoire. Dans ce fichier, nous pouvons écrire notre code HTML régulier + [Embedded Ruby](https://www.tutorialspoint.com/ruby-on-rails/rails-and-html-erb.htm). Écrivez simplement quelque chose dans le fichier pour que nous puissions voir le template rendu dans le navigateur.

```html
<h1>Page d'accueil</h1>
```

Maintenant, quand nous allons sur [http://localhost:3000](http://localhost:3000), nous devrions voir quelque chose comme ceci au lieu de la page d'information par défaut de Rails.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-60.png)

Nous avons maintenant un point de départ très basique. Nous pouvons commencer à introduire de nouvelles choses sur notre site web. Je pense qu'il est temps de créer notre premier commit.

Dans votre invite de commande, exécutez :

```bash
git status
```

Et vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-61.png)

Si vous ne le savez pas déjà, lorsque nous générons une nouvelle application, un nouveau dépôt git local est initialisé.

Ajoutez toutes les modifications actuelles en exécutant :

```bash
git add -A
```

Ensuite, commitez tous les changements en exécutant :

```bash
git commit -m "Generate PagesController. Initialize Home page"
```

Si nous exécutions ceci :

```bash
git status
```

Nous verrions qu'il n'y a rien à commiter, car nous venons de commiter avec succès tous les changements.

![Image](https://www.freecodecamp.org/news/content/images/2019/05/image-4.png)

### Bootstrap

Pour la barre de navigation et le système de grille responsive, nous allons utiliser la bibliothèque [Bootstrap](https://getbootstrap.com/). Pour utiliser cette bibliothèque, nous devons installer la gem [bootstrap-sass](https://github.com/twbs/bootstrap-sass). Ouvrez le `Gemfile` dans votre éditeur.

```bash
collabfield/Gemfile
```

Ajoutez la gem `bootstrap-sass` au Gemfile. Comme l'indique la documentation, vous devez vous assurer que la gem `sass-rails` est également présente.

```
...
gem 'bootstrap-sass', '~> 3.3.6'
gem 'sass-rails', '>= 3.2'
...
```

Enregistrez le fichier et exécutez ceci pour installer les gems nouvellement ajoutées :

```bash
bundle install
```

Si vous exécutez toujours l'application, redémarrez le serveur Rails pour vous assurer que les nouvelles gems sont disponibles. Pour redémarrer le serveur, arrêtez-le simplement en appuyant sur `Ctrl + C` et exécutez à nouveau la commande `rails s` pour démarrer le serveur.

Allez dans `assets` pour ouvrir le fichier `application.css` :

`app/assets/stylesheets/application.css`

Sous tout le texte commenté, ajoutez ceci :

```css
...
@import "bootstrap-sprockets";
@import "bootstrap";
```

Maintenant, changez le nom de `application.css` en `application.scss`. C'est nécessaire pour utiliser la bibliothèque Bootstrap dans Rails, et cela nous permet également d'utiliser les fonctionnalités de [Sass](https://sass-lang.com/).

Nous voulons contrôler l'ordre dans lequel tous les fichiers `.scss` sont rendus, car à l'avenir, nous pourrions vouloir créer des variables Sass. Nous voulons nous assurer que nos variables seront définies avant de les utiliser.

Pour ce faire, supprimez ces deux lignes du fichier `application.scss` :

```scss
*= require_self
*= require_tree .
```

Nous sommes presque en mesure d'utiliser la bibliothèque Bootstrap. Il reste encore une chose à faire. Comme l'indique la documentation de [bootstrap-sass](https://github.com/twbs/bootstrap-sass), le JavaScript de Bootstrap dépend de la bibliothèque jQuery. Pour utiliser jQuery avec Rails, vous devez ajouter la gem [jquery-rails](https://github.com/rails/jquery-rails).

```bash
gem 'jquery-rails'
```

Exécutez...

```bash
bundle install
```

...à nouveau, et redémarrez le serveur.

La dernière étape consiste à requérir Bootstrap et jQuery dans le fichier JavaScript de l'application. Allez dans `application.js` :

```
app/assets/javascripts/application.js
```

Ajoutez ensuite les lignes suivantes dans le fichier :

```js
//= require jquery
//= require bootstrap-sprockets
```

Commitez les changements :

```bash
git add -A
git commit -m "Add and configure bootstrap gem"
```

### Barre de navigation

Pour la barre de navigation, nous utiliserons le [composant navbar](https://getbootstrap.com/docs/3.3/components/#navbar) de Bootstrap comme point de départ, puis nous le modifierons pas mal. Nous stockerons notre barre de navigation dans un [template partiel](https://guides.rubyonrails.org/layouts_and_rendering.html#using-partials).

Nous faisons cela parce qu'il est préférable de garder chaque composant de l'application dans des fichiers séparés. Cela permet de tester et de gérer le code de l'application beaucoup plus facilement. De plus, nous pouvons réutiliser ces composants dans d'autres parties de l'application, sans dupliquer le code.

Naviguez vers :

```
views/layouts
```

Créez un nouveau fichier :

```bash
_navigation.html.erb
```

Pour les partiels, nous utilisons le préfixe underscore, afin que le framework Rails puisse le distinguer comme un partiel. Maintenant, copiez et collez le composant navbar de la documentation Bootstrap et enregistrez le fichier. Pour voir le partiel sur le site web, nous devons le rendre quelque part. Naviguez vers `views/layouts/application.html.erb`. C'est le fichier par défaut où tout est rendu.

À l'intérieur du fichier, nous voyons la méthode suivante :

```
<%= yield %>
```

Elle rend le template demandé. Pour utiliser la syntaxe ruby à l'intérieur du fichier HTML, nous devons l'envelopper avec `<% %>` (l'ERB nous permet de faire cela). Pour apprendre rapidement les différences entre les syntaxes ERB, consultez cette [réponse StackOverflow](https://stackoverflow.com/questions/7996695/what-is-the-difference-between-and-in-erb-in-rails).

Dans la [section Page d'accueil](https://medium.com/free-code-camp/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f#page-daccueil), nous avons défini la [route](https://medium.com/free-code-camp/lets-create-an-intermediate-level-ruby-on-rails-application-d7c6e997c63f#1faf) pour reconnaître l'URL racine. Ainsi, chaque fois que nous envoyons une [requête GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) pour aller à la page racine, l'action `index` du `PagesController` est appelée. Et cette action respective (dans ce cas l'action `index`) répond avec un template qui est rendu avec la méthode `yield`. Comme vous vous en souvenez, notre template pour la page d'accueil se trouve dans `app/views/pages/index.html.erb`.

Comme nous voulons avoir une barre de navigation sur toutes les pages, nous allons rendre notre barre de navigation à l'intérieur du fichier `application.html.erb` par défaut. Pour rendre un fichier partiel, utilisez simplement la méthode `render` et passez le chemin du partiel comme argument. Faites-le juste au-dessus de la méthode `yield` comme ceci :

```rb
...
<%= render 'layouts/navigation' %>
<%= yield %>
...
```

Maintenant, allez sur [http://localhost:3000](http://localhost:3000/) et vous devriez pouvoir voir la barre de navigation.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-62.png)

Comme mentionné ci-dessus, nous allons modifier cette barre de navigation. Commençons par supprimer tous les éléments `<li>` et `<form>`. À l'avenir, nous créerons nos propres éléments ici. Le fichier `_navigation.html.erb` devrait ressembler à ceci maintenant.

```rb
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Brand</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
      </ul>

      <ul class="nav navbar-nav navbar-right">
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```

Nous avons maintenant une barre de navigation responsive de base. C'est le bon moment pour créer un nouveau commit. Dans l'invite de commande, exécutez les commandes suivantes :

```bash
git add -A
git commit -m "Add a basic navigation bar"
```

Nous devrions changer le nom de la barre de navigation de `Brand` à `collabfield`. Comme `Brand` est un élément de lien, nous devrions utiliser une méthode `[link_to](https://apidock.com/rails/ActionView/Helpers/UrlHelper/link_to)` pour générer des liens. Pourquoi ? Parce que cette méthode nous permet de générer facilement des chemins URI. Ouvrez une invite de commande et naviguez vers le répertoire du projet. Exécutez la commande suivante :

```bash
rails routes
```

Cette commande affiche nos routes disponibles, qui sont générées par le fichier `routes.rb`. Comme nous le voyons :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-63.png)

Actuellement, nous n'avons qu'une seule route, celle que nous avons définie auparavant. Si vous regardez les routes données, vous pouvez voir une colonne `Prefix`. Nous pouvons utiliser ces préfixes pour générer un chemin vers une page souhaitée. Tout ce que nous avons à faire est d'utiliser un nom de préfixe et d'y ajouter `_path`. Si nous écrivions `root_path`, cela générerait un chemin vers la page racine. Utilisons donc la puissance de la méthode `link_to` et des routes.

Remplacez cette ligne :

```html
<a class="navbar-brand" href="#">Brand</a>
```

Par cette ligne :

```html
<%= link_to 'collabfield', root_path, class: 'navbar-brand' %>
```

N'oubliez pas que chaque fois que vous ne comprenez pas tout à fait comment fonctionne une méthode particulière, il vous suffit de la chercher sur Google et vous trouverez probablement sa documentation avec une explication. Parfois, les documentations sont mal écrites, vous voudrez donc peut-être chercher un peu plus sur Google et vous pourriez trouver un blog ou une réponse StackOverflow qui vous aiderait.

Dans ce cas, nous passons une chaîne de caractères comme premier argument pour ajouter la valeur de l'élément `<a>`, le deuxième argument est nécessaire pour un chemin, c'est là que les routes nous aident à le générer. Le troisième argument est facultatif, il est accumulé dans le hash des options. Dans ce cas, nous devions ajouter la classe `navbar-brand` pour que notre barre de navigation alimentée par Bootstrap fonctionne.

Faisons un autre commit pour ce petit changement. Dans la section suivante, nous commencerons à modifier le design de notre application, en commençant par la barre de navigation.

```bash
git add -A
git commit -m "Change navigation bar's brand name from Brand to collabfield"
```

### Feuilles de style

Laissez-moi vous présenter comment je structure mes fichiers de feuilles de style. D'après ce que je sais, il n'y a pas de conventions fortes sur la façon de structurer vos feuilles de style dans Rails. Tout le monde le fait un peu différemment.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-64.png)

C'est ainsi que je structure habituellement mes fichiers.

* **Répertoire Base** — C'est ici que je garde les variables Sass et les styles qui sont utilisés dans toute l'application. Par exemple, les tailles de police par défaut et les styles des éléments par défaut.
* **Partiels** — La plupart de mes styles vont ici. Je garde tous les styles pour les composants et les pages séparés dans ce répertoire.
* **Responsive** — Ici, je définis différentes règles de style pour différentes tailles d'écran. Par exemple, des styles pour un écran de bureau, un écran de tablette, un écran de téléphone, etc.

Tout d'abord, créons une nouvelle branche de dépôt en exécutant ceci :

```bash
git checkout -b "styles"
```

Nous venons de créer une nouvelle [branche git](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) et nous y avons automatiquement basculé. À partir de maintenant, c'est ainsi que nous allons implémenter les nouveaux changements au code.

La raison de faire cela est que nous pouvons isoler notre version actuellement fonctionnelle (branche master) et écrire un nouveau code à l'intérieur d'une copie du projet, sans avoir peur d'endommager quoi que ce soit.

Une fois que nous avons terminé l'implémentation, nous pouvons simplement fusionner les changements dans la branche `master`.

Commencez par créer quelques répertoires :

```
app/assets/stylesheets/partials/layout
```

À l'intérieur du répertoire layout, créez un fichier `navigation.scss` et à l'intérieur du fichier ajoutez :

```scss
.navbar-default, .navbar-toggle:focus, .collapsed, button.navbar-toggle {
  background: $navbarColor !important;
  border: none;
  a {
    color: white !important;
  }
}
```

Avec ces lignes de code, nous changeons la couleur de fond et des liens de la barre de navigation. Comme vous l'avez peut-être remarqué, le sélecteur `a` est imbriqué dans un autre bloc de déclaration. Sass nous permet d'utiliser cette fonctionnalité. `!important` est utilisé pour remplacer strictement les styles par défaut de Bootstrap. La dernière chose que vous avez peut-être remarquée est qu'au lieu d'un nom de couleur, nous utilisons une variable Sass. La raison en est que nous allons utiliser cette couleur plusieurs fois dans l'application. Définissons cette variable.

Créez d'abord un nouveau dossier :

```
app/assets/stylesheets/base
```

À l'intérieur du répertoire base, créez un nouveau fichier `variables.scss`. À l'intérieur du fichier, définissez une variable :

```scss
$navbarColor: #323738;
```

Si vous essayiez d'aller sur [http://localhost:3000](http://localhost:3000/), vous ne remarqueriez aucun changement de style. La raison en est que dans la [section Bootstrap](#bootstrap), nous avons supprimé ces lignes :

```
*= require_self
*= require_tree .
```

de `application.scss`, pour ne pas importer automatiquement tous les fichiers de style.

Cela signifie que nous devons maintenant importer nos fichiers nouvellement créés dans le fichier `application.scss` principal. Le fichier devrait ressembler à ceci maintenant :

```scss
// ...commentaires par défaut

// Bootstrap
@import "bootstrap-sprockets";
@import "bootstrap";

// Variables
@import "base/variables";

// Partiels - fichiers css principaux
@import "partials/layout/*";
```

La raison de l'importation du fichier `variables.scss` en haut est de s'assurer que les variables sont définies avant de les utiliser.

Ajoutez un peu plus de CSS en haut du fichier `navigation.scss` :

```scss
nav {
  .navbar-header {
    width: 100%;
    button, .navbar-brand {
      transition: opacity 0.15s;
    }
    button {
      margin-right: 0;
    }
    button:hover, .navbar-brand:hover {
      opacity: 0.8;
    }
  }
}
```

Bien sûr, vous pouvez mettre ce code au bas du fichier si vous le souhaitez. Personnellement, j'ordonne et je groupe le code CSS en fonction de la [spécificité des sélecteurs CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity). Encore une fois, tout le monde le fait un peu différemment. Je place les sélecteurs moins spécifiques au-dessus et les sélecteurs plus spécifiques en dessous. Ainsi, par exemple, les sélecteurs de type vont au-dessus des sélecteurs de classe et les sélecteurs de classe vont au-dessus des sélecteurs d'ID.

Commettons les changements :

```bash
git add -A
git commit -m "Add CSS to the navigation bar"
```

Nous voulons nous assurer que la barre de navigation est toujours visible, même lorsque nous faisons défiler vers le bas. Pour l'instant, nous n'avons pas assez de contenu pour faire défiler vers le bas, mais nous en aurons à l'avenir. Pourquoi ne pas donner cette fonctionnalité à la barre de navigation dès maintenant ?

Pour ce faire, utilisez la classe Bootstrap `navbar-fixed-top`. Ajoutez cette classe à l'élément `nav`, afin qu'il ressemble à ceci :

```html
<nav class="navbar navbar-default navbar-fixed-top">
```

Nous voulons également que `collabfield` soit aligné sur les limites du côté gauche du [système de grille de Bootstrap](https://getbootstrap.com/docs/3.3/css/#grid). Pour l'instant, il est aligné sur les limites du côté gauche de la fenêtre d'affichage, car notre classe est actuellement `container-fluid`. Pour changer cela, changez la classe en `container`.

Cela devrait ressembler à ceci :

```html
<div class="container">
```

Commitez les changements :

```bash
git add -A 
git commit -m "
- in _navigation.html.erb add navbar-fixed-top class to nav. 
- Replace container-fluid class with container"
```

Si vous allez sur [http://localhost:3000](http://localhost:3000/), vous voyez que le texte `Home page` est caché sous la barre de navigation. C'est à cause de la classe `navbar-fixed-top`. Pour résoudre ce problème, poussez le corps vers le bas en ajoutant ce qui suit à `navigation.scss` :

```scss
body {
 margin-top: 50px;
}
```

À ce stade, l'application devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-65.png)

Commitez le changement :

```bash
git add -A
git commit -m "Add margin-top 50px to the body"
```

Comme vous vous en souvenez, nous avons créé une nouvelle branche auparavant et nous y avons basculé. Il est temps de retourner sur la branche `master`.

Exécutez la commande :

```bash
git branch
```

Vous pouvez voir la liste de nos branches. Actuellement, nous sommes dans la branche `styles`.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-66.png)

Pour revenir à la branche `master`, exécutez :

```bash
git checkout master
```

Pour fusionner tous nos changements, que nous avons faits dans la branche `styles`, exécutez simplement :

```bash
git merge styles
```

La commande a fusionné ces deux branches et nous pouvons maintenant voir le résumé des changements que nous avons faits.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-67.png)

Nous n'avons plus besoin de la branche `styles`, nous pouvons donc la supprimer :

```bash
git branch -D styles
```

## Articles

C'est presque le bon moment pour commencer à implémenter la fonctionnalité des articles. Comme l'objectif de notre application est de permettre aux utilisateurs de rencontrer des personnes partageant les mêmes idées, nous devons nous assurer que les auteurs des articles peuvent être identifiés. Pour y parvenir, un système d'authentification est requis.

### Authentification

Pour un système d'authentification, nous allons utiliser la [gem devise](https://github.com/plataformatec/devise). Nous pourrions créer notre propre système d'authentification, mais cela demanderait beaucoup d'efforts. Nous allons choisir une voie plus facile. C'est aussi un choix populaire au sein de la communauté Rails.

Commencez par créer une nouvelle branche :

```bash
git checkout -b authentication
```

Comme pour toute autre gem, pour la configurer, nous suivrons sa documentation. Heureusement, elle est très facile à configurer.

Ajoutez à votre `Gemfile` :

```
gem 'devise'
```

Exécutez ensuite les commandes :

```bash
bundle install
rails generate devise:install
```

Vous voyez probablement des instructions dans l'invite de commande. Nous n'utiliserons pas de mailers dans ce tutoriel, donc aucune configuration supplémentaire n'est nécessaire.

À ce stade, si vous ne connaissez rien aux modèles Rails, vous devriez vous familiariser avec eux en parcourant les documentations [Active Record](http://guides.rubyonrails.org/active_record_basics.html) et [Active Model](http://guides.rubyonrails.org/active_model_basics.html).

Utilisons maintenant un générateur devise pour créer un modèle `User`.

```bash
rails generate devise User
```

Initialisez une base de données pour l'application en exécutant :

```bash
rails db:create
```

Exécutez ensuite cette commande pour créer de nouvelles tables dans votre base de données :

```bash
rails db:migrate
```

C'est tout. Techniquement, notre système d'authentification est configuré. Nous pouvons maintenant utiliser les méthodes fournies par Devise et créer de nouveaux utilisateurs. Commitez le changement :

```bash
git add -A
git commit -m "Add and configure the Devise gem"
```

En installant la gem Devise, nous obtenons non seulement la fonctionnalité back-end, mais aussi des vues par défaut. Si vous listez vos routes en exécutant :

```bash
rails routes
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-68.png)

Vous pouvez voir que vous avez maintenant un tas de nouvelles routes. Rappelez-vous, nous n'avions qu'une seule route racine jusqu'à présent. Si quelque chose semble confus, vous pouvez toujours ouvrir la [documentation de devise](https://github.com/plataformatec/devise/wiki) et obtenir vos réponses. N'oubliez pas non plus que beaucoup de gens se posent les mêmes questions. Il y a de fortes chances que vous trouviez la réponse en cherchant aussi sur Google.

Essayez certaines de ces routes. Allez sur [localhost:3000/users/sign_in](http://localhost:3000/users/sign_in) et vous devriez voir une page de connexion.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-69.png)

Si vous alliez sur [localhost:3000/users/sign_up](http://localhost:3000/users/sign_up), vous verriez également une page d'inscription. Nom de Dieu ! comme dit Noob Noob. Si vous regardez le répertoire `views`, vous voyez qu'il n'y a pas de répertoire Devise que nous pourrions modifier. Comme l'indique la documentation de Devise, pour modifier les vues Devise, nous devons les générer avec un générateur devise. Exécutez :

```bash
rails generate devise:views
```

Si vous vérifiez le répertoire `views`, vous verrez un répertoire devise généré à l'intérieur. Ici, nous pouvons modifier l'apparence des pages d'inscription et de connexion. Commençons par la page de connexion, car dans notre cas, ce sera une implémentation plus simple. Avec la page d'inscription, en raison de la fonctionnalité souhaitée, un effort supplémentaire sera nécessaire.

**Page de connexion**

Naviguez vers et ouvrez `app/views/devise/sessions/new.html.erb`.

C'est ici que sont stockées les vues de la page de connexion. Il n'y a qu'un formulaire de connexion à l'intérieur du fichier. Comme vous l'avez peut-être remarqué, la méthode `[form_for](http://api.rubyonrails.org/v5.1/classes/ActionView/Helpers/FormHelper.html)` est utilisée pour générer ce formulaire. C'est une méthode Rails pratique pour générer des formulaires. Nous allons modifier le style de ce formulaire avec bootstrap. Remplacez tout le contenu du fichier par :

```rb
<%= bootstrap_form_for(resource, 
                       as: resource_name, 
                       url: session_path(resource_name)) do |f| %>

    <%= f.email_field :email, 
                      autofocus: true, 
                      class: 'form-control', 
                      placeholder: 'email' %>

    <%= f.password_field  :password, 
                          autocomplete: "off", 
                          class: 'form-control',
                          placeholder: 'password' %>


  <% if devise_mapping.rememberable? -%>
     <%= f.check_box :remember_me %>
  <% end -%>

   <%= f.submit "Log in", class: 'form-control login-button' %>
<% end %>
```

Rien d'extraordinaire ici. Nous avons juste modifié ce formulaire pour qu'il soit un formulaire bootstrap en changeant le nom de la méthode en `bootstrap_form_for` et en ajoutant des classes `form-control` aux champs.

Regardez comment les arguments à l'intérieur des méthodes sont stylisés. Chaque argument commence sur une nouvelle ligne. La raison pour laquelle j'ai fait cela est d'éviter d'avoir de longues lignes de code. Habituellement, les lignes de code ne devraient pas dépasser 80 caractères, cela améliore la lisibilité. Nous allons styliser le code ainsi pour le reste du guide.

Si nous visitons [localhost:3000/users/sign_in](http://localhost:3000/users/sign_in), nous verrons qu'il nous donne une erreur :

```
undefined method 'bootstrap_form_for'
```

Pour utiliser les formulaires bootstrap dans Rails, nous devons ajouter une gem [bootstrap_form](https://github.com/bootstrap-ruby/rails-bootstrap-forms). Ajoutez ceci au `Gemfile` :

```bash
gem 'bootstrap_form'
```

Exécutez ensuite :

```bash
bundle install
```

À ce moment, la page de connexion devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-70.png)

Commitez les changements :

```bash
git add -A
git commit -m "Generate devise views, modify sign in form 
and add the bootstrap_form gem."
```

Pour donner le système de grille de bootstrap à la page, enveloppez le formulaire de connexion avec le conteneur bootstrap.

```html
<div class="container">
  <div class="row">
    <div class="col-sm-6 col-sm-offset-3">
      <h2 class="text-center">Connexion</h2>
      
      <!-- COLLEZ LE FORMULAIRE DE CONNEXION ICI -->
      
    </div>
  </div> 
</div>
```

La largeur du formulaire de connexion est de 6 colonnes sur 12. Et le décalage (offset) est de 3 colonnes. Sur les appareils plus petits, le formulaire prendra toute la largeur de l'écran. C'est ainsi que fonctionne la [grille bootstrap](https://getbootstrap.com/docs/3.3/css/#grid).

Faisons un autre commit. Un changement assez mineur, n'est-ce pas ? Mais c'est ainsi que je fais habituellement mes commits. J'implémente un changement défini dans une zone, puis je le commite. Je pense que faire ainsi aide à suivre les changements et à comprendre comment le code a évolué.

```bash
git add -A
git commit -m "wrap login form in the login page with a boostrap container"
```

Il serait préférable que nous puissions simplement accéder à la page de connexion en allant sur `/login` au lieu de `/users/sign_in`. Nous devons changer la route. Pour ce faire, nous devons savoir où se trouve l'action qui est appelée lorsque nous allons sur la page de connexion. Les contrôleurs Devise sont situés à l'intérieur de la gem elle-même. En lisant la documentation de Devise, nous pouvons voir que tous les contrôleurs sont situés dans le répertoire `devise`. Pas vraiment surpris par la découverte, pour être honnête U_U. En utilisant la méthode `devise_scope`, nous pouvons simplement changer la route. Allez dans le fichier `routes.rb` et ajoutez :

```rb
devise_scope :user do
  get 'login', to: 'devise/sessions#new'
end
```

Commitez le changement :

```bash
git add -A
git commit -m "change route from /users/sign_in to /login"
```

Pour l'instant, laissez la page de connexion telle quelle.

**Page d'inscription**

Si nous naviguions vers [localhost:3000/users/sign_up](http://localhost:3000/users/sign_up), nous verrions la page d'inscription par défaut de Devise. Mais comme mentionné ci-dessus, la page d'inscription nécessitera un effort supplémentaire. Pourquoi ? Parce que nous voulons ajouter une nouvelle colonne `:name` à la table `users`, afin qu'un objet User puisse avoir l'attribut `:name`.

Nous sommes sur le point d'apporter quelques modifications au fichier `schema.rb`. À ce stade, si vous n'êtes pas tout à fait familier avec les modifications de schéma et les migrations, je vous recommande de lire la documentation sur les [Migrations Active Record](http://guides.rubyonrails.org/active_record_migrations.html).

Tout d'abord, nous devons ajouter une colonne supplémentaire à la table `users`. Nous pourrions créer un nouveau fichier de migration et utiliser une méthode `change_table` pour ajouter une colonne supplémentaire. Mais nous n'en sommes qu'à l'étape du développement, notre application n'est pas encore déployée. Nous pouvons simplement définir une nouvelle colonne directement dans le fichier de migration `devise_create_users`, puis recréer la base de données. Naviguez vers `db/migrate` et ouvrez le fichier `*DATE_DE_CRÉATION*_devise_create_users.rb` et ajoutez `t.string :name, null: false, default: ""` à l'intérieur de la méthode `create_table`.

Maintenant, exécutez les commandes pour supprimer et créer la base de données, et lancer les migrations.

```bash
rails db:drop
rails db:create
rails db:migrate
```

Nous avons ajouté une nouvelle colonne à la table users et modifié le fichier `schema.rb`.

Pour pouvoir envoyer un attribut supplémentaire afin que le contrôleur Devise l'accepte, nous devons apporter quelques modifications au niveau du contrôleur. Nous pouvons modifier les contrôleurs Devise de différentes manières. Nous pouvons utiliser le générateur devise et générer les contrôleurs. Ou nous pouvons créer un nouveau fichier, spécifier le contrôleur et les méthodes que nous voulons modifier. Les deux méthodes sont bonnes. Nous allons utiliser la seconde.

Naviguez vers `app/controllers` et créez un nouveau fichier `registrations_controller.rb`. Ajoutez le code suivant au fichier :

```rb
class RegistrationsController < Devise::RegistrationsController

  private

  def sign_up_params
    params.require(:user).permit( :name, 
                                  :email, 
                                  :password, 
                                  :password_confirmation)
  end

  def account_update_params
    params.require(:user).permit( :name, 
                                  :email, 
                                  :password, 
                                  :password_confirmation, 
                                  :current_password)
  end
end
```

Ce code écrase les méthodes `sign_up_params` et `account_update_params` pour accepter l'attribut `:name`. Comme vous le voyez, ces méthodes sont dans le `RegistrationsController` de Devise, nous l'avons donc spécifié et avons modifié ses méthodes. Maintenant, dans nos routes, nous devons spécifier ce contrôleur pour que ces méthodes puissent être écrasées. Dans `routes.rb`, changez :

```
devise_for :users
```

en

```
devise_for :users, :controllers => {:registrations => "registrations"}
```

Commitez les changements.

```bash
git add -A
git commit -m "
- Add the name column to the users table. 
- Include name attribute to sign_up_params and account_update_params 
  methods inside the RegistrationsController"
```

Ouvrez le fichier `new.html.erb` :

```
app/views/devise/registrations/new.html.erb
```

Encore une fois, supprimez tout sauf le formulaire. Convertissez le formulaire en un formulaire bootstrap. Cette fois, nous ajoutons un champ de nom supplémentaire.

```rb
<%= bootstrap_form_for(resource, 
                       :as => resource_name, 
                       :url => registration_path(resource_name)) do |f| %>

  <%= f.text_field :name, 
	           placeholder: 'nom d\'utilisateur (sera affiché publiquement)', 
	           class: 'form-control' %>
  <%= f.text_field :email, 
	           placeholder: 'email', 
	           class: 'form-control' %>
  <%= f.password_field :password, 
                       placeholder: 'mot de passe', 
                       class: 'form-control' %>
  <%= f.password_field :password_confirmation, 
                       placeholder: 'confirmation du mot de passe', 
                       class: 'form-control' %>
  <%= f.submit 'S\'inscrire', class: 'btn sign-up-button' %>
<% end %>
```

Commitez le changement.

```bash
git add -A
git commit -m "
Delete everything from the signup page, except the form. 
Convert form into a bootstrap form. Add an additional name field"
```

Enveloppez le formulaire avec un conteneur bootstrap et ajoutez du texte.

```html
<div class="container" id="sign-up-form">
  <div class="row">
    <h1>Entrez en contact avec des personnes partageant les mêmes idées</h1>
    <h3>Créez, étudiez, accomplissez des objectifs ensemble</h3>

    <div class="col-sm-offset-4 col-sm-4">
      <h3>S'inscrire <small>c'est gratuit !</small></h3> 

        <!-- COLLEZ LE FORMULAIRE ICI -->
		
    </div>
  </div>
</div>
```

Commitez le changement.

```bash
git add -A
git commit -m "
Wrap the sign up form with a bootstrap container. 
Add informational text inside the container"
```

Tout comme pour la page de connexion, il serait préférable que nous puissions simplement ouvrir une page d'inscription en allant sur `/signup` au lieu de `users/sign_up`. Dans le fichier `routes.rb`, ajoutez le code suivant :

```rb
devise_scope :user do
  get 'signup', to: 'devise/registrations#new'
end
```

Commitez le changement.

```bash
git add -A
git commit -m "Change sign up page's route from /users/sign_up to /signup"
```

Appliquons quelques changements de style avant de continuer. Naviguez vers `app/assets/stylesheets/partials` et créez un nouveau fichier `signup.scss`. À l'intérieur du fichier, ajoutez le CSS suivant :

```scss
#sign-up-form {
  margin-top: 100px;
  h1 {
    font-size: 36px !important;
    font-size: 3.6rem !important;
  }
  text-align: center;
  padding-bottom: 20px; 
}
```

De plus, nous n'avons pas importé les fichiers du répertoire `partials` dans le fichier `application.scss`. Faisons-le dès maintenant. Naviguez vers `application.scss` et juste au-dessus de `@import partials/layout/*`, importez tous les fichiers du répertoire `partials`. `application.scss` devrait ressembler à ceci :

```scss
...

// Partiels - fichiers css principaux
@import "partials/*";
@import "partials/layout/*";
```

Commettons les changements.

```bash
git add -A
git commit -m "
- Create a signup.scss and add CSS to the sign up page
- Import all files from partials directory to the application.scss"
```

Ajoutez quelques autres changements de style à l'aspect général du site web. Naviguez vers `app/assets/stylesheets/base` et créez un nouveau fichier `default.scss`. À l'intérieur du fichier, ajoutez le code CSS suivant :

```scss
* {
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
}

body {
  background: $backgroundColor;
  font-size: 14px;
  font-size: 1.4rem;
}

h1 {
  font-size: 24px;
  font-size: 2.4rem;
}

i {
  width: 26px;
}

ul {
  list-style-type: none;
}

a:hover, a:active, a:link, a:visited {
  text-decoration: none;
}

.control-label {
  display: none;
}
```

Ici, nous appliquons quelques changements de style généraux pour l'ensemble du site web. La taille de la police (`font-size`) est fixée à `62.5%`, de sorte que l'unité `1 rem` puisse représenter `10px`. Si vous ne savez pas ce qu'est l'unité rem, vous voudrez peut-être lire ce [tutoriel](https://www.sitepoint.com/understanding-and-using-rem-units-in-css/). Nous ne voulons pas voir de texte de label sur les formulaires bootstrap, c'est pourquoi nous avons défini ceci :

```scss
.control-label {
  display: none;
}
```

Vous avez peut-être remarqué que la variable `$backgroundColor` est utilisée. Mais cette variable n'est pas encore définie. Faisons-le en ouvrant le fichier `variables.scss` et en ajoutant ceci :

```
$backgroundColor: #f0f0f0;
```

Le fichier `default.scss` n'est pas importé dans `application.scss`. Importez-le sous les variables, le fichier `application.scss` devrait ressembler à ceci :

```scss
...

// Variables
@import "base/variables";

// Styles par défaut
@import "base/default";

...
```

Commettons les changements.

```bash
git add -A
git commit -m "
Add CSS and import CSS files inside the main file
- Create a default.scss file and add CSS 
- Define $backgroundColor variable 
- Import default.scss file inside the application.scss"
```

**Mise à jour de la barre de navigation**

Pour l'instant, nous avons trois pages différentes : accueil, connexion et inscription. C'est une bonne idée de les relier toutes ensemble, afin que les utilisateurs puissent naviguer sur le site sans effort. Nous allons mettre des liens vers les pages d'inscription et de connexion sur la barre de navigation. Naviguez vers et ouvrez le fichier `_navigation.html.erb`.

```
app/views/layouts/_navigation.html.erb
```

Nous allons ajouter du code supplémentaire ici. À l'avenir, nous en ajouterons encore plus. Cela conduira à un fichier avec beaucoup de code, difficile à gérer et à tester. Afin de gérer plus facilement un code long, nous allons commencer à diviser le code plus volumineux en morceaux plus petits. Pour y parvenir, nous utiliserons des partiels. Avant d'ajouter du code supplémentaire, divisons déjà le code actuel de `_navigation.html.erb` en partiels.

Laissez-moi vous présenter rapidement comment notre barre de navigation va fonctionner. Nous aurons deux parties majeures. Sur une partie, les éléments seront affichés tout le temps, quelle que soit la taille de l'écran. Sur l'autre partie de la barre de navigation, les éléments ne seront affichés que sur les écrans plus grands et repliés sur les plus petits.

Voici à quoi ressemblera la structure à l'intérieur de l'élément `.container` :

```html
<div class="row">

  <!-- Éléments visibles tout le temps -->
  <div class="col-sm-7">
  </div><!-- col-sm-7 -->

  <!-- Éléments repliés sur les appareils plus petits -->
  <div class="col-sm-5">
  </div><!-- col-sm-5 -->

</div><!-- row -->
```

À l'intérieur du répertoire layouts :

```
app/views/layouts
```

Créez un nouveau répertoire `navigation`. À l'intérieur de ce répertoire, créez un nouveau fichier partiel `_header.html.erb`.

```
app/views/layouts/navigation/_header.html.erb
```

Depuis le fichier `_navigation.html.erb`, coupez toute la section `.navbar-header` et collez-la dans le fichier `_header.html.erb`. À l'intérieur du répertoire `navigation`, créez un autre fichier partiel nommé `_collapsible_elements.html.erb`.

```
app/views/layouts/navigation/_collapsible_elements.html.erb
```

Depuis le fichier `_navigation.html.erb`, coupez toute la section `.navbar-collapse` et collez-la dans `_collapsible_elements.html.erb`. Maintenant, rendons ces deux partiels à l'intérieur du fichier `_navigation.html.erb`. Le fichier devrait ressembler à ceci maintenant.

```html
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="row">

      <!-- Éléments visibles tout le temps -->
      <div class="col-sm-7">
        <%= render 'layouts/navigation/header' %>
      </div><!-- col-sm-7 -->

      <!-- Éléments repliés sur les appareils plus petits -->
      <div class="col-sm-5">
        <%= render 'layouts/navigation/collapsible_elements' %>
      </div><!-- col-sm-5 -->

    </div><!-- row -->
  </div><!-- container -->
</nav>
```

Si vous alliez sur [http://localhost:3000](http://localhost:3000/) maintenant, vous ne remarqueriez aucune différence. Nous avons juste nettoyé un peu notre code et l'avons préparé pour un développement ultérieur.

Nous sommes prêts à ajouter des liens à la barre de navigation. Naviguez vers et ouvrez à nouveau le fichier `_collapsible_elements.html.erb` :

```
app/views/layouts/navigation/_collapsible_elements.html.erb
```

Remplissons ce fichier avec des liens, remplacez le contenu du fichier par :

```html
<!-- Collect the nav links, forms, and other content for toggling -->
<div class="collapse navbar-collapse navbar-right" id="navbar-collapsible-content">
  <ul class="nav navbar-nav ">
    <% if user_signed_in? %>
      <li class="dropdown pc-menu">
        <a id="user-settings" class="dropdown-toggle" data-toggle="dropdown" href="#">
          <span id="user-name"><%= current_user.name %></span>
          <span class="caret"></span>
        </a>

        <ul class="dropdown-menu" role="menu">
          <li><%= link_to 'Modifier le profil', edit_user_registration_path %></li>
          <li><%= link_to 'Déconnexion', destroy_user_session_path, method: :delete %></li>
        </ul>
      </li>

      <li class="mobile-menu">
        <%= link_to 'Modifier le profil', edit_user_registration_path %>
      </li>
      <li class="mobile-menu">
        <%= link_to 'Déconnexion', destroy_user_session_path, method: :delete %>
      </li>

    <% else # l'utilisateur n'est pas connecté %>
      <li ><%= link_to 'Connexion', login_path %></li>
      <li ><%= link_to 'S\'inscrire', signup_path %></li>
    <% end # si l'utilisateur est connecté %>
  </ul>
</div><!-- navbar-collapse -->
```

Laissez-moi vous expliquer brièvement ce qui se passe ici. Tout d'abord, à la deuxième ligne, j'ai changé l' `id` de l'élément en `navbar-collapsible-content`. C'est nécessaire pour rendre ce contenu repliable. C'est une fonctionnalité de bootstrap. L' `id` par défaut était `bs-example-navbar-collapse-1`. Pour déclencher cette fonction, il y a le bouton avec l'attribut `data-target` à l'intérieur du fichier `_header.html`. Ouvrez `views/layouts/navigation/_header.html.erb` et changez l'attribut `data-target` en `data-target="#navbar-collapsible-content"`. Maintenant, le bouton déclenchera le contenu repliable.

Ensuite, à l'intérieur du fichier `_collapsible_elements.html.erb`, vous voyez une logique `if else` avec la méthode Devise `user_signed_in?`. Cela affichera différents liens selon qu'un utilisateur est connecté ou non. Laisser de la logique, comme des instructions `if else`, à l'intérieur des vues n'est pas une bonne pratique. Les vues devraient être assez « bêtes » et se contenter de cracher l'information, sans « réfléchir » du tout. Nous refactoriserons cette logique plus tard avec des Helpers.

La dernière chose à noter dans le fichier sont les classes CSS `pc-menu` et `mobile-menu`. Le but de ces classes est de contrôler la façon dont les liens sont affichés sur différentes tailles d'écran. Ajoutons du CSS pour ces classes. Naviguez vers `app/assets/stylesheets` et créez un nouveau répertoire `responsive`. À l'intérieur du répertoire, créez deux fichiers, `desktop.scss` et `mobile.scss`. Le but de ces fichiers est d'avoir des configurations différentes pour différentes tailles d'écran. Dans le fichier `desktop.scss`, ajoutez :

```scss
@media screen and (min-width: 767px) {
  .mobile-menu {
    display: none !important;
  }
}
```

Dans le fichier `mobile.scss`, ajoutez :

```scss
@media screen and (max-width: 767px) {
  .pc-menu {
    display: none !important;
  }
}
```

Si vous n'êtes pas familier avec les requêtes média CSS, lisez [ceci](https://www.w3schools.com/css/css_rwd_mediaqueries.asp). Importez les fichiers du répertoire `responsive` à l'intérieur du fichier `application.scss`. Importez-le au bas du fichier, de sorte que `application.scss` ressemble à ceci :

```scss
...

// Requêtes média pour un design responsive
@import "responsive/*";
```

Naviguez vers et ouvrez le fichier `navigation.scss` :

```
app/assets/stylesheets/partials/layout/navigation.scss
```

et faites quelques ajustements stylistiques à la barre de navigation en ajoutant ce qui suit à l'intérieur du sélecteur de l'élément `nav` :

```scss
.col-sm-5, .col-sm-7 {
  padding: 0;
}
```

Et à l'extérieur de l'élément `nav`, ajoutez le code CSS suivant :

```scss
.pc-menu {
  margin-right: 10px;
}

.mobile-menu {
  i {
    color: white;
  }
  ul {
    padding: 0px;
  }
  a {
    display: block;
    padding: 10px 0px 10px 25px !important;
  }
  a:hover {
    background: white !important;
    color: black !important;
    i {
      color: black;
    }
  }
}

.icon-bar {
  background-color: white !important;
}

.active a {
  background: $navbarColor !important;
  border-bottom: solid 5px white;
}

.dropdown-toggle, .dropdown-menu {
  background: $navbarColor !important;
  border: none;
}

.dropdown-menu a:hover {
  color: black !important;
  background: white !important;
}
```

À ce moment, notre application devrait ressembler à ceci lorsqu'un utilisateur n'est pas connecté :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-71.png)

Comme ceci lorsqu'un utilisateur est connecté :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-73.png)

Et comme ceci lorsque la taille de l'écran est plus petite :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-74.png)

Commitez les changements.

```bash
git add -A
git commit -m "
Update the navigation bar
- Add login, signup, logout and edit profile links on the navigation bar 
- Split _navigation.scss code into partials 
- Create responsive directory inside the stylesheets directory and add CSS. 
- Add CSS to tweak navigation bar style"
```

Nous avons maintenant une fonctionnalité d'authentification de base. Elle répond à nos besoins. Fusionnons donc la branche `authentication` avec la branche `master`.

```bash
git checkout master
git merge authentication
```

Nous pouvons voir à nouveau le résumé des changements. La branche d'authentification n'est plus nécessaire, supprimez-la.

```
git branch -D authentication
```

### Helpers

Lorsque nous travaillions sur le fichier `_collapsible_elements.html.erb`, j'ai mentionné que les vues Rails ne sont pas le bon endroit pour la logique. Si vous regardez à l'intérieur du répertoire `app` du projet, vous voyez qu'il y a un répertoire appelé `helpers`. Nous allons extraire la logique des vues Rails et la mettre dans le répertoire `helpers`.

```
app/views/pages
```

Créons nos premiers helpers. Tout d'abord, créez une nouvelle branche et basculez dessus.

```
git checkout -B helpers
```

Naviguez vers le répertoire `helpers` et créez un nouveau fichier `navigation_helper.rb` :

```
app/helpers/navigation_helper.rb
```

À l'intérieur des fichiers de helpers, les helpers sont définis comme des [modules](https://www.tutorialspoint.com/ruby/ruby_modules.htm). À l'intérieur de `navigation_helper.rb`, définissez le module.

```rb
module NavigationHelper
end
```

Par défaut, Rails charge tous les fichiers de helpers dans toutes les vues. Personnellement, je n'aime pas cela, car les noms des méthodes de différents fichiers de helpers pourraient entrer en conflit. Pour passer outre ce comportement par défaut, ouvrez le fichier `application.rb` :

```
config/application.rb
```

À l'intérieur de la classe `Application`, ajoutez cette configuration :

```
config.action_controller.include_all_helpers = false
```

Maintenant, les helpers ne sont disponibles que pour les vues du contrôleur correspondant. Ainsi, si nous avons le `PagesController`, tous les helpers à l'intérieur du fichier `pages_helper.rb` seront disponibles pour tous les fichiers de vue à l'intérieur du répertoire `pages`.

Nous n'avons pas de `NavigationController`, donc les méthodes de helper définies à l'intérieur du module `NavigationHelper` ne seront disponibles nulle part. La barre de navigation est disponible sur l'ensemble du site web. Nous pouvons inclure le module `NavigationHelper` à l'intérieur de l' `ApplicationHelper`. Si vous n'êtes pas familier avec le chargement et l'inclusion de fichiers, lisez cet [article](https://prograils.com/posts/ruby-methods-differences-load-require-include-extend) pour avoir une idée de ce qui va se passer.

À l'intérieur du fichier `application_helper.rb`, requérez le fichier `navigation_helper.rb`. Nous avons maintenant accès au contenu du fichier `navigation_helper.rb`. Injectons donc le module `NavigationHelper` à l'intérieur du module `ApplicationHelper` en utilisant une méthode `include`. L' `application_helper.rb` devrait ressembler à ceci :

```rb
require 'navigation_helper.rb'

module ApplicationHelper
  include NavigationHelper
end
```

Maintenant, les méthodes de helper de `NavigationHelper` sont disponibles dans toute l'application.

Naviguez vers et ouvrez le fichier `_collapsible_elements.html.erb` :

```
app/views/layouts/navigation/_collapsible_elements.html.erb
```

Nous allons diviser le contenu à l'intérieur des instructions `if else` en partiels. Créez un nouveau répertoire `collapsible_elements` à l'intérieur du répertoire `navigation`.

```
app/views/layouts/navigation/collapsible_elements
```

À l'intérieur du répertoire, créez deux fichiers : `_signed_in_links.html.erb` et `_non_signed_in_links.html.erb`. Maintenant, coupez le contenu des instructions `if else` du fichier `_collapsible_elements.html.erb` et collez-le dans les partiels correspondants. Les partiels devraient ressembler à ceci :

```html
<li class="dropdown pc-menu">
  <a id="user-settings" class="dropdown-toggle" data-toggle="dropdown" href="#">
    <span id="user-name"><%= current_user.name %></span>
    <span class="caret"></span>
  </a>

  <ul class="dropdown-menu" role="menu">
    <li><%= link_to 'Modifier le profil', edit_user_registration_path %></li>
    <li><%= link_to 'Déconnexion', destroy_user_session_path, method: :delete %></li>
  </ul>
</li>

<li class="mobile-menu">
  <%= link_to 'Modifier le profil', edit_user_registration_path %>
</li>
<li class="mobile-menu">
  <%= link_to 'Déconnexion', destroy_user_session_path, method: :delete %>
</li>
```

```html
<li ><%= link_to 'Connexion', login_path %></li>
<li ><%= link_to 'S\'inscrire', signup_path %></li>
```

Maintenant, à l'intérieur du fichier `_collapsible_elements.html.erb`, au lieu des instructions `if else`, ajoutez la méthode `render` avec la méthode de helper `collapsible_links_partial_path` comme argument. Le fichier devrait ressembler à ceci :

```html
<!-- Collect the nav links, forms, and other content for toggling -->
<div class="collapse navbar-collapse navbar-right" id="navbar-collapsible-content">
  <ul class="nav navbar-nav ">
    <%= render collapsible_links_partial_path %>
  </ul>
</div><!-- navbar-collapse -->
```

`collapsible_links_partial_path` est la méthode que nous allons définir à l'intérieur de `NavigationHelper`. Ouvrez `navigation_helper.rb` :

```
app/helpers/navigation_helper.rb
```

et définissez la méthode à l'intérieur du module. Le fichier `navigation_helper.rb` devrait ressembler à ceci :

```rb
module NavigationHelper

  def collapsible_links_partial_path
    if user_signed_in?
      'layouts/navigation/collapsible_elements/signed_in_links'
    else
      'layouts/navigation/collapsible_elements/non_signed_in_links'
    end
  end
  
end
```

La méthode définie est assez simple. Si un utilisateur est connecté, elle renvoie le chemin d'un partiel correspondant. Si un utilisateur n'est pas connecté, elle renvoie le chemin d'un autre partiel.

Nous avons créé notre première méthode de helper et extrait la logique des vues vers une méthode de helper. Nous allons faire cela pour le reste du guide, chaque fois que nous rencontrerons de la logique à l'intérieur d'un fichier de vue. En faisant cela, nous nous rendons service, car tester et gérer l'application devient beaucoup plus facile.

L'application devrait avoir le même aspect et fonctionner de la même manière.

Commitez les changements.

```bash
git add -A
git commit -m "Configure and create helpers
- Change include_all_helpers config to false 
- Split the _collapsible_elements.html.erb file's content into 
  partials and extract logic from the file into partials"
```

Fusionnez la branche `helpers` avec la branche `master` :

```bash
git checkout master
git merge helpers
```

### Tests

À ce stade, l'application possède quelques fonctionnalités. Même s'il n'y a pas encore beaucoup de fonctions, nous devons déjà passer un certain temps à tester manuellement l'application si nous voulons nous assurer que tout fonctionne. Imaginez si l'application avait 20 fois plus de fonctionnalités qu'actuellement. Quelle frustration ce serait de vérifier que tout fonctionne bien à chaque fois que nous apportons des modifications au code. Pour éviter cette frustration et des heures de tests manuels, nous allons implémenter des [tests automatisés](https://en.wikipedia.org/wiki/Test_automation).

Avant de plonger dans l'écriture des tests, permettez-moi de vous présenter comment et ce que je teste. Vous pouvez également lire [A Guide to Testing Rails Applications](http://guides.rubyonrails.org/testing.html) pour vous familiariser avec les techniques de test Rails par défaut.

**Ce que j'utilise pour les tests**

* **Framework :** [RSpec](https://relishapp.com/rspec/) Quand j'ai commencé à tester mes applications Rails, j'utilisais le framework par défaut [Minitest](http://guides.rubyonrails.org/testing.html#rails-meets-minitest). Maintenant, j'utilise RSpec. Je ne pense pas qu'il y ait un bon ou un mauvais choix ici. Les deux frameworks sont excellents. Je pense que cela dépend d'une préférence personnelle. J'ai entendu dire que RSpec est un choix populaire au sein de la communauté Rails, j'ai donc décidé de lui donner sa chance. Maintenant, je l'utilise la plupart du temps.
* **Données d'échantillon :** [factory_girl](https://github.com/thoughtbot/factory_girl) Encore une fois, au début, j'ai essayé la méthode Rails par défaut — les [fixtures](http://guides.rubyonrails.org/testing.html#the-low-down-on-fixtures), pour ajouter des données d'échantillon. J'ai trouvé que c'est un cas différent de celui des frameworks de test. Le choix du framework de test est probablement une préférence personnelle. À mon avis, ce n'est pas le cas pour les données d'échantillon. Au début, les fixtures étaient correctes. Mais j'ai remarqué qu'une fois que les applications deviennent plus grandes, le contrôle des données d'échantillon avec les fixtures devient difficile. Peut-être que je les utilisais de la mauvaise manière. Mais avec les factories, tout a été agréable et paisible tout de suite. Peu importe si une application est plus petite ou plus grande — l'effort pour configurer les données d'échantillon est le même.
* **Tests d'acceptation :** [Capybara](https://github.com/teamcapybara/capybara) Par défaut, Capybara utilise le pilote rack_test. Malheureusement, ce pilote ne supporte pas JavaScript. Au lieu du pilote par défaut de Capybara, j'ai choisi d'utiliser [poltergeist](https://github.com/teampoltergeist/poltergeist). Il supporte JavaScript et, dans mon cas, c'était le pilote le plus facile à configurer.

**Ce que je teste**

Je teste toute la logique que j'ai écrite. Cela peut être :

* Les Helpers
* Les Modèles
* Les Jobs
* Les Patrons de conception (Design Patterns)
* Toute autre logique écrite par moi

En plus de la logique, j'enveloppe mon application avec des tests d'acceptation en utilisant Capybara, pour m'assurer que toutes les fonctionnalités de l'application fonctionnent correctement en simulant l'interaction d'un utilisateur. De plus, pour aider mes tests de simulation, j'utilise des [tests de requête](https://relishapp.com/rspec/rspec-rails/docs/request-specs/request-spec) pour m'assurer que toutes les requêtes renvoient des réponses correctes.

C'est ce que je teste dans mes applications personnelles, car cela répond pleinement à mes besoins. Évidemment, les normes de test peuvent être différentes d'une personne à l'autre et d'une entreprise à l'autre.

Les contrôleurs, les vues et les gems n'ont pas été mentionnés, pourquoi ? Comme le disent de nombreux développeurs Rails, les contrôleurs et les vues ne devraient pas contenir de logique. Et je suis d'accord avec eux. Dans ce cas, il n'y a pas grand-chose à tester. À mon avis, les tests de simulation d'utilisateur sont suffisants et efficaces pour les vues et les contrôleurs. Et les gems sont déjà testées par leurs créateurs. Je pense donc que les tests de simulation sont suffisants pour s'assurer que les gems fonctionnent correctement aussi.

**Comment je teste**

Bien sûr, j'essaie d'utiliser l'approche TDD chaque fois que cela est possible. Écrire un test d'abord, puis implémenter le code. Dans ce cas, le flux de développement devient plus fluide. Mais parfois, vous n'êtes pas sûr de ce à quoi ressemblera la fonctionnalité terminée et quel type de résultat attendre. Vous pourriez être en train d'expérimenter avec le code ou simplement d'essayer différentes solutions d'implémentation. Dans ces cas-là, l'approche « test d'abord et implémentation plus tard » ne fonctionne pas vraiment.

Avant (parfois après, comme discuté ci-dessus) chaque morceau de logique que j'écris, j'écris un test isolé pour celui-ci, c'est-à-dire un [test unitaire](https://en.wikipedia.org/wiki/Unit_testing). Pour m'assurer que chaque fonctionnalité d'une application fonctionne, j'écris des tests d'acceptation (simulation d'utilisateur) avec Capybara.

**Configurer un environnement de test**

Avant d'écrire nos premiers tests, nous devons configurer l'environnement de test.

Ouvrez le `Gemfile` et ajoutez ces gems au groupe de test :

```bash
gem 'rspec-rails', '~> 3.6'
gem 'factory_girl_rails'
gem 'rails-controller-testing'
gem 'headless'
gem 'capybara'
gem 'poltergeist'
gem 'database_cleaner'
```

Comme discuté ci-dessus, la gem `rspec` est un framework de test, `factory_girl` sert à ajouter des données d'échantillon, `capybara` sert à simuler l'interaction d'un utilisateur avec l'application et le pilote `poltergeist` apporte le support JavaScript à vos tests.

Vous pouvez utiliser un autre pilote qui supporte JavaScript s'il est plus facile pour vous de le configurer. Si vous décidez d'utiliser la gem `poltergeist`, vous aurez besoin de PhantomJS installé. Pour installer PhantomJS, lisez la [documentation de poltergeist](https://github.com/teampoltergeist/poltergeist).

La gem `headless` est requise pour supporter les pilotes headless. `poltergeist` est un pilote headless, c'est pourquoi nous avons besoin de cette gem. La gem `rails-controller-testing` sera requise lorsque nous testerons les requêtes et les réponses avec les [request specs](https://relishapp.com/rspec/rspec-rails/docs/request-specs/request-spec). Plus d'informations à ce sujet plus tard.

`database_cleaner` est nécessaire pour nettoyer la base de données de test après les tests où du JavaScript a été exécuté. Normalement, la base de données de test se nettoie d'elle-même après chaque test, mais lorsque vous testez des fonctionnalités qui contiennent du JavaScript, la base de données ne se nettoie pas automatiquement. Cela pourrait changer à l'avenir, mais au moment de l'écriture de ce tutoriel, après l'exécution de tests avec JavaScript, la base de données de test n'est pas nettoyée automatiquement. C'est pourquoi nous devons configurer manuellement notre environnement de test pour nettoyer la base de données de test après chaque test JavaScript également. Nous allons configurer quand exécuter la gem `database_cleaner` dans un instant.

Maintenant que le but de ces gems est couvert, installons-les en exécutant :

```bash
bundle install
```

Pour initialiser le répertoire `spec` pour le framework RSpec, exécutez ce qui suit :

```bash
rails generate rspec:install
```

D'une manière générale, spec signifie un test unique dans le framework RSpec. Lorsque nous lançons nos specs, cela signifie que nous lançons nos tests.

Si vous regardez à l'intérieur du répertoire `app`, vous remarquerez un nouveau répertoire appelé `spec`. C'est ici que nous allons écrire les tests. Vous avez peut-être aussi remarqué un répertoire appelé `test`. C'est là que les tests sont stockés lorsque vous utilisez une configuration de test par défaut. Nous n'utiliserons pas du tout ce répertoire. Vous pouvez simplement le supprimer du projet c(x_X)b.

Comme mentionné ci-dessus, nous devons configurer le `database_cleaner` pour les tests qui incluent du JavaScript. Ouvrez le fichier `rails_helper.rb` :

```
spec/rails_helper.rb
```

Changez cette ligne :

```
config.use_transactional_fixtures = true
```

en

```
config.use_transactional_fixtures = false
```

et en dessous, ajoutez le code suivant :

```rb
  config.before(:suite) do
    DatabaseCleaner.clean_with(:truncation)
  end
 
  config.before(:each) do
    DatabaseCleaner.strategy = :transaction
  end
 
  config.before(:each, :js => true) do
    DatabaseCleaner.strategy = :truncation
  end
 
  config.before(:each) do
    DatabaseCleaner.start
  end
 
  config.after(:each) do
    DatabaseCleaner.clean
  end

```

J'ai pris cet extrait de code de ce [tutoriel](http://www.virtuouscode.com/2012/08/31/configuring-database_cleaner-with-rails-rspec-capybara-and-selenium/).

La dernière chose que nous avons à faire est d'ajouter quelques configurations. À l'intérieur des configurations du fichier `rails_helper.rb`, ajoutez les lignes suivantes :

```rb
  require 'capybara/poltergeist'
  require 'factory_girl_rails'
  require 'capybara/rspec'

  config.include Devise::Test::IntegrationHelpers, type: :feature
  config.include FactoryGirl::Syntax::Methods
  Capybara.javascript_driver = :poltergeist
  Capybara.server = :puma 
```

Décomposons un peu le code.

Avec les méthodes `require`, nous chargeons les fichiers des nouvelles gems ajoutées, afin de pouvoir utiliser leurs méthodes ci-dessous.

```bash
config.include Devise::Test::IntegrationHelpers, type: :feature
```

Cette configuration nous permet d'utiliser les méthodes `devise` à l'intérieur des tests `capybara`. Comment ai-je trouvé cette ligne ? Elle était fournie dans la [documentation de Devise](https://github.com/plataformatec/devise).

```
config.include FactoryGirl::Syntax::Methods
```

Cette configuration permet d'utiliser les méthodes de la gem `factory_girl`. Encore une fois, j'ai trouvé cette configuration dans la documentation de la gem.

```rb
Capybara.javascript_driver = :poltergeist 
Capybara.server = :puma
```

Ces deux configurations sont nécessaires pour pouvoir tester le JavaScript avec `capybara`. Lisez toujours la documentation en premier lorsque vous voulez implémenter quelque chose que vous ne savez pas faire.

La raison pour laquelle je vous ai présenté la plupart des gems de test et des configurations d'un coup, et non progressivement au fur et à mesure que nous rencontrons un problème particulier, est de vous donner une image claire de ce que j'utilise pour les tests. Maintenant, vous pouvez toujours revenir à cette section et vérifier la majorité des configurations en un seul endroit. Plutôt que de sauter d'un endroit à l'autre et d'assembler les gems avec les configurations comme les pièces d'un puzzle.

Commettons les changements et mettons enfin la main à la pâte avec les tests.

```bash
git add -A
git commit -m "
Set up the testing environment
- Remove test directory
- Add and configure rspec-rails, factory_girl_rails, 
  rails-controller-testing, headless, capybara, poltergeist,
  database_cleaner gems"
```

**Helper specs**

À propos de chaque type de specs (tests), vous pouvez trouver des informations générales en lisant la [documentation de rspec](https://relishapp.com/rspec) et la [documentation de sa gem](https://github.com/rspec/rspec-rails). Les deux sont assez similaires, mais vous pouvez trouver quelques différences entre elles.

Créez et basculez vers une nouvelle branche :

```bash
git checkout -b specs
```

Jusqu'à présent, nous n'avons créé qu'une seule méthode de helper. Testons-la.

Naviguez vers le répertoire `spec` et créez un nouveau répertoire appelé `helpers`.

```
spec/helpers
```

À l'intérieur du répertoire, créez un nouveau fichier `navigation_helper_spec.rb` :

```
spec/helpers/navigation_helper_spec.rb
```

À l'intérieur du fichier, écrivez le code suivant :

```rb
require 'rails_helper'

RSpec.describe NavigationHelper, :type => :helper do
  
end
```

`require 'rails_helper'` nous donne accès à toutes les configurations et méthodes de test. `:type => :helper` traite nos tests comme des specs de helper et nous fournit des méthodes spécifiques.

Voici à quoi devrait ressembler le fichier `navigation_helper_spec.rb` lorsque la méthode `collapsible_links_partial_path` est testée :

```rb
require 'rails_helper'

RSpec.describe NavigationHelper, :type => :helper do

  context 'utilisateur connecté' do
    before(:each) { helper.stub(:user_signed_in?).and_return(true) }

    context '#collapsible_links_partial_path' do
      it "renvoie le chemin du partiel signed_in_links" do
        expect(helper.collapsible_links_partial_path).to (
          eq 'layouts/navigation/collapsible_elements/signed_in_links'
        )
      end
    end
  end

  context 'utilisateur non connecté' do
    before(:each) { helper.stub(:user_signed_in?).and_return(false) }
    
    context '#collapsible_links_partial_path' do
      it "renvoie le chemin du partiel non_signed_in_links" do
        expect(helper.collapsible_links_partial_path).to (
          eq 'layouts/navigation/collapsible_elements/non_signed_in_links'
        )
      end
    end
  end

end
```

Pour en savoir plus sur `context` et `it`, lisez la documentation sur la [structure de base](https://relishapp.com/rspec/rspec-core/v/3-6/docs/example-groups/basic-structure-describe-it). Ici, nous testons deux cas — quand un utilisateur est connecté et quand un utilisateur n'est pas connecté. Dans chaque contexte d' `utilisateur connecté` et d' `utilisateur non connecté`, nous avons des [hooks before](https://relishapp.com/rspec/rspec-core/v/2-0/docs/hooks/before-and-after-hooks). À l'intérieur du contexte correspondant, ces hooks (méthodes) s'exécutent avant chacun de nos tests. Dans notre cas, avant chaque test, nous exécutons la méthode [stub](https://relishapp.com/rspec/rspec-mocks/v/2-4/docs/method-stubs/stub-with-a-simple-return-value), afin que `user_signed_in?` renvoie la valeur que nous lui disons de renvoyer.

Et enfin, avec la méthode [expect](https://relishapp.com/rspec/rspec-expectations/docs/built-in-matchers), nous vérifions que lorsque nous appelons la méthode `collapsible_links_partial_path`, nous obtenons une valeur de retour attendue.

Pour lancer tous les tests, exécutez simplement :

```
rspec spec
```

Pour lancer spécifiquement le fichier `navigation_helper_spec.rb`, exécutez :

```
rspec spec/helpers/navigation_helper_spec.rb
```

Si les tests ont réussi, la sortie devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-75.png)

Commettons les changements.

```bash
git add -A
git commit -m "Add specs to NavigationHelper's collapsible_links_partial_path method"
```

**Factories**

Ensuite, nous aurons besoin de quelques données d'échantillon pour effectuer nos tests. La gem `factory_girl` nous donne la possibilité d'ajouter des données d'échantillon très facilement, chaque fois que nous en avons besoin. Elle fournit également une documentation de bonne qualité, ce qui rend l'expérience globale assez agréable. Le seul objet que nous pouvons créer avec notre application jusqu'à présent est l' `User`. Pour définir la factory user, créez un répertoire `factories` à l'intérieur du répertoire `spec`.

```
spec/factories
```

À l'intérieur du répertoire factories, créez un nouveau fichier `users.rb` et ajoutez le code suivant :

```rb
FactoryGirl.define do 
  factory :user do
    sequence(:name) { |n| "test#{n}" }
    sequence(:email) { |n| "test#{n}@test.com" }
    password '123456'
    password_confirmation '123456'
  end
end
```

Maintenant, à l'intérieur de nos specs, nous pouvons facilement créer de nouveaux utilisateurs dans la base de données de test, chaque fois que nous en avons besoin, en utilisant les méthodes de la gem `factory_girl`. Pour un guide complet sur la façon de définir et d'utiliser les factories, consultez la documentation de la gem `factory_girl`.

Notre factory définie, `user`, est assez simple. Nous avons défini les valeurs que les objets `user` posséderont. Nous avons également utilisé la méthode `sequence`. En lisant la documentation, vous pouvez voir qu'avec chaque enregistrement `User` supplémentaire, la valeur `n` est incrémentée de un. C'est-à-dire que le nom du premier utilisateur créé sera `test0`, celui du second `test1`, etc.

Commettons les changements :

```bash
git add -A
git commit -m "add a users factory"
```

**Feature specs**

Dans les [feature specs](https://relishapp.com/rspec/rspec-rails/docs/feature-specs/feature-spec), nous écrivons du code qui simule l'interaction d'un utilisateur avec une application. Les feature specs sont alimentées par la gem `capybara`.

La bonne nouvelle est que nous avons tout configuré et que nous sommes prêts à écrire nos premières feature specs. Nous allons tester les fonctionnalités de connexion, de déconnexion et d'inscription.

À l'intérieur du répertoire `spec`, créez un nouveau répertoire appelé `features`.

```
spec/features
```

À l'intérieur du répertoire `features`, créez un autre répertoire appelé `user`.

```
spec/features/user
```

À l'intérieur du répertoire `user`, créez un nouveau fichier appelé `login_spec.rb`.

Voici à quoi ressemble le test de connexion :

```rb
require "rails_helper"

RSpec.feature "Login", :type => :feature do
  let(:user) { create(:user) }

  scenario 'l\'utilisateur navigue vers la page de connexion et se connecte avec succès', js: true do
    user
    visit root_path
    find('nav a', text: 'Connexion').click
    fill_in 'user[email]', with: user.email
    fill_in 'user[password]', with: user.password
    find('.login-button').click
    expect(page).to have_selector('#user-settings')
  end

end
```

Avec ce code, nous simulons une visite sur la page de connexion, en partant de la page d'accueil. Ensuite, nous remplissons le formulaire et le soumettons. Enfin, nous vérifions si nous avons l'élément `#user-settings` sur la barre de navigation, qui n'est disponible que pour les utilisateurs connectés.

`feature` et `scenario` font partie de la syntaxe de Capybara. `feature` est identique à `context`/`describe` et `scenario` est identique à `it`. Vous trouverez plus d'informations dans la documentation de Capybara, [Using Capybara With Rspec](https://github.com/teamcapybara/capybara#using-capybara-with-rspec).

La méthode `[let](https://relishapp.com/rspec/rspec-core/v/2-5/docs/helper-methods/let-and-let)` nous permet d'écrire des méthodes mémorisées que nous pourrions utiliser dans toutes les specs à l'intérieur du contexte où la méthode a été définie.

Ici, nous utilisons également notre factory `users` créée et la méthode `create`, qui vient avec la gem `factory_girl`.

L'argument `js: true` permet de tester des fonctionnalités qui impliquent du JavaScript.

Comme toujours, pour voir si un test réussit, lancez un fichier spécifique. Dans ce cas, il s'agit du fichier `login_spec.rb` :

```
rspec spec/features/user/login_spec.rb
```

Commettons les changements.

```bash
git add -A
git commit -m "add login feature specs"
```

Nous pouvons maintenant tester la fonctionnalité de déconnexion. À l'intérieur du répertoire `user`, créez un nouveau fichier nommé `logout_spec.rb` :

```
spec/features/user/logout_spec.rb
```

Le test implémenté devrait ressembler à ceci :

```rb
require "rails_helper"

RSpec.feature "Logout", :type => :feature do
  let(:user) { create(:user) }

  scenario 'l\'utilisateur se déconnecte avec succès', js: true do
    sign_in user
    visit root_path
    find('nav #user-settings').click
    find('nav a', text: 'Déconnexion').click
    expect(page).to have_selector('nav a', text: 'Connexion')
  end

end
```

Le code simule un utilisateur cliquant sur le bouton de déconnexion, puis s'attend à voir les liens de l'utilisateur non connecté sur la barre de navigation.

La méthode `sign_in` est l'une des méthodes de helper de Devise. Nous avons inclus ces méthodes de helper dans le fichier `rails_helper.rb` précédemment.

Lancez le fichier pour voir si le test réussit.

Commettons les changements.

```bash
git add -A
git commit -m "add logout feature specs"
```

La dernière fonctionnalité que nous avons est la possibilité de créer un nouveau compte. Testons-la. À l'intérieur du répertoire `user`, créez un nouveau fichier nommé `sign_up_spec.rb`. Voici à quoi devrait ressembler le fichier avec le test à l'intérieur :

```rb
require "rails_helper"

RSpec.feature "Sign up", :type => :feature do
  let(:user) { build(:user) }

  scenario 'l\'utilisateur navigue vers la page d\'inscription et s\'inscrit avec succès', js: true do
    visit root_path
    find('nav a', text: 'S\'inscrire').click
    fill_in 'user[name]', with: user.name
    fill_in 'user[email]', with: user.email
    fill_in 'user[password]', with: user.password
    fill_in 'user[password_confirmation]', with: user.password_confirmation
    find('.sign-up-button').click
    expect(page).to have_selector('#user-settings')
  end

end
```

Nous simulons un utilisateur naviguant vers la page d'inscription, remplissant le formulaire, soumettant le formulaire et enfin, nous nous attendons à voir l'élément `#user-settings` qui n'est disponible que pour les utilisateurs connectés.

Ici, nous utilisons la méthode `build` de Devise au lieu de `create`. De cette façon, nous créons un nouvel objet sans l'enregistrer dans la base de données.

Nous pouvons lancer toute la suite de tests et voir si tous les tests réussissent.

```
rspec spec
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-76.png)

Commettons les changements.

```bash
git add -A
git commit -m "add sign up features specs"
```

Nous en avons fini avec nos premiers tests. Fusionnons donc la branche `specs` avec la branche `master`.

```bash
git checkout master
git merge specs
```

La branche specs n'est plus nécessaire. Supprimez-la q__o.

```bash
git branch -D specs
```

### Flux principal

Sur la page d'accueil, nous allons créer un flux d'articles. Ce flux va afficher tous les types d'articles sous forme de cartes.

Commencez par créer une nouvelle branche :

```bash
git checkout -b main_feed
```

Générez un nouveau modèle appelé `Post`.

```bash
rails g model post
```

Ensuite, nous aurons besoin d'un modèle `Category` pour catégoriser les articles :

```bash
rails g model category
```

Créons maintenant quelques associations entre les modèles `User`, `Category` et `Post`.

Chaque article va appartenir à une catégorie et à son auteur (utilisateur). Ouvrez les fichiers des modèles et ajoutez les associations.

```rb
class Post < ApplicationRecord
  belongs_to :user
  belongs_to :category
end
class User < ApplicationRecord
  ...
  has_many :posts, dependent: :destroy       
end

class Category < ApplicationRecord
  has_many :posts
end
```

L'argument `dependent: :destroy` signifie que lorsqu'un utilisateur est supprimé, tous les articles que l'utilisateur a créés seront également supprimés.

Maintenant, nous devons définir les colonnes de données et les associations à l'intérieur des fichiers de migration.

```rb
class CreatePosts < ActiveRecord::Migration[5.1]
  def change
    create_table :posts do |t|
      t.string :title
      t.text :content
      t.belongs_to :category, index: true
      t.belongs_to :user, index: true
      t.timestamps
    end
  end
end
```

```rb
class CreateCategories < ActiveRecord::Migration[5.1]
  def change
    create_table :categories do |t|
      t.string :name
      t.string :branch
    end
  end
end
```

Maintenant, lancez les fichiers de migration :

```bash
rails db:migrate
```

Commettons les changements :

```bash
git add -A
git commit -m "
- Generate Post and Category models. 
- Create associations between User, Post and Category models. 
- Create categories and posts database tables."
```

**Specs**

Nous pouvons tester les modèles nouvellement créés. Plus tard, nous aurons besoin de données d'échantillon pour les tests. Comme un article appartient à une catégorie, nous avons également besoin de données d'échantillon pour les catégories afin de configurer les associations.

Créez une factory `category` à l'intérieur du répertoire `factories`.

```rb
FactoryGirl.define do 
  factory :category do
    sequence(:name) { |n| "name#{n}" }
    sequence(:branch) { |n| "branch#{n}" }
  end
end
```

Créez une factory `post` à l'intérieur du répertoire `factories` :

```
spec/factories/posts.rb
```

```rb
FactoryGirl.define do 
  factory :post do
    title 'a' * 20
    content 'a' * 20
    user
    category
  end
end
```

Comme vous le voyez, il est très facile de configurer une association pour les factories. Tout ce que nous avions à faire pour configurer les associations `user` et `category` pour la factory `post`, c'est d'écrire les noms des factories à l'intérieur de la factory `post`.

Commettons les changements.

```bash
git add -A
git commit -m "Add post and category factories"
```

Pour l'instant, nous ne testerons que les associations, car c'est la seule chose que nous avons écrite jusqu'à présent dans les modèles.

Ouvrez `post_spec.rb` :

```bash
spec/models/post_spec.rb
```

Ajoutez des specs pour les associations, afin que le fichier ressemble à ceci :

```rb
require 'rails_helper'

RSpec.describe Post, type: :model do
  context 'Associations' do
    it 'appartient à user' do
      association = described_class.reflect_on_association(:user).macro
      expect(association).to eq :belongs_to
    end

    it 'appartient à category' do
      association = described_class.reflect_on_association(:category).macro
      expect(association).to eq :belongs_to
    end
  end
end
```

Nous utilisons la méthode `[described_class](https://relishapp.com/rspec/rspec-core/docs/metadata/described-class)` pour obtenir la classe du contexte actuel. Ce qui revient essentiellement à écrire `Post` dans ce cas. Ensuite, nous utilisons la méthode `[reflect_on_association](https://apidock.com/rails/v2.3.2/ActiveRecord/Reflection/ClassMethods/reflect_on_association)` pour vérifier qu'elle renvoie une association correcte.

Faites de même pour les autres modèles.

```rb
require 'rails_helper'

RSpec.describe Category, type: :model do
  context 'Associations' do
    it 'possède plusieurs posts' do
      association = described_class.reflect_on_association(:posts)
      expect(association.macro).to eq :has_many
    end
  end
end
```

```rb
require 'rails_helper'

RSpec.describe User, type: :model do

  context 'Associations' do
    it 'possède plusieurs posts' do
      association = described_class.reflect_on_association(:posts)
      expect(association.macro).to eq :has_many
      expect(association.options[:dependent]).to eq :destroy
    end
  end
end
```

Commettons les changements.

```bash
git add -A
git commit -m "Add specs for User, Category, Post models' associations"
```

**Mise en page de la page d'accueil**

Actuellement, la page d'accueil ne contient rien, seulement le texte factice « Page d'accueil ». Il est temps de créer sa mise en page avec bootstrap. Ouvrez le fichier de vue de la page d'accueil `views/pages/index.html.erb` et remplacez le contenu du fichier par le code suivant pour créer la mise en page de la page :

```html
<div class="container">
  <div class="row">
    <div id="side-menu"  class="col-sm-3">
    </div><!-- side-menu -->

    <div id="main-content" class="col-sm-9">
    </div><!-- main-content -->

  </div><!-- row -->
</div><!-- container -->
```

Ajoutez maintenant du CSS pour définir le style des éléments et le comportement responsive.

À l'intérieur du répertoire `stylesheets/partials`, créez un nouveau fichier `home_page.scss` :

```
assets/stylesheets/partials/home_page.scss
```

Dans le fichier, ajoutez le CSS suivant :

```scss
#main-content {
  background: white;
  min-height: 800px;
  margin: 0;
  padding: 10px 0 0 0;
}

#side-menu {
  padding: 0;
  #links-list {
    margin-top: 20px;
    padding: 0;
    font-size: 14px;
    font-size: 1.4rem;
    a {
      display: block;
      padding: 5px 15px;
      margin: 2px 0;
    }
    li {
      min-width: 195px;
      max-width: 195px;
    }
    li, li a {
      color: black;
      text-decoration: none;
    }
    li:hover {
      border-radius: 50px;
      background: $navbarColor;
    }
    li:hover a, li:hover i {
      color: white;
    }
  }
}
```

À l'intérieur de la requête média `max-width: 767px` du fichier `mobile.scss`, ajoutez :

```scss
#side-menu {
  display: none !important;
}
```

Maintenant, la page d'accueil devrait ressembler à ceci sur les écrans plus grands :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-77.png)

et à ceci sur les écrans plus petits :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-78.png)

Commettons les changements.

```bash
git add -A
git commit -m "
- Add the bootstrap layout to the home page 
- Add CSS to make home page layout's stylistic and responsive design changes"
```

**Seeds**

Pour afficher des articles sur la page d'accueil, nous devons d'abord les avoir dans la base de données. Créer des données manuellement est ennuyeux et prend du temps. Pour automatiser ce processus, nous utiliserons des seeds. Ouvrez le fichier `seeds.rb` :

```
db/seeds.rb
```

Ajoutez le code suivant :

```rb
def seed_users
  user_id = 0
  10.times do 
    User.create(
      name: "test#{user_id}",
      email: "test#{user_id}@test.com",
      password: '123456',
      password_confirmation: '123456'
    )
    user_id = user_id + 1
  end
end


def seed_categories
  hobby = ['Arts', 'Artisanat', 'Sports', 'Sciences', 'Collection', 'Lecture', 'Autre']
  study = ['Arts et Humanités', 'Sciences Physiques et Ingénierie', 'Mathématiques et Logique',
          'Informatique', 'Science des Données', 'Économie et Finance', 'Affaires',
          'Sciences Sociales', 'Langues', 'Autre']
  team = ['Étude', 'Développement', 'Arts et Loisirs', 'Autre']

  hobby.each do |name|
    Category.create(branch: 'hobby', name: name)
  end

  study.each do |name|
    Category.create(branch: 'study', name: name)
  end

  team.each do |name|
    Category.create(branch: 'team', name: name)
  end
end

def seed_posts
  categories = Category.all

  categories.each do |category|
    5.times do
      Post.create(
        title: Faker::Lorem.sentences[0], 
        content: Faker::Lorem.sentences[0], 
        user_id: rand(1..9), 
        category_id: category.id
      )
    end
  end
end

seed_users
seed_categories
seed_posts
```

Comme vous le voyez, nous créons les méthodes `seed_users`, `seed_categories` et `seed_posts` pour créer des enregistrements `User`, `Category` et `Post` dans la base de données de développement. De plus, la gem [faker](https://github.com/stympy/faker) est utilisée pour générer du texte factice. Ajoutez la gem `faker` à votre `Gemfile` :

```
gem 'faker'
```

et

```bash
bundle install
```

Pour peupler les données en utilisant le fichier `seeds.rb`, lancez la commande :

```bash
rails db:seed
```

Commettons les changements.

```bash
git add -A
git commit -m "
- Add faker gem 
- Inside the seeds.rb file create methods to generate 
  User, Category and Post records inside the development database"
```

**Affichage des articles**

Pour afficher les articles, nous aurons besoin d'un répertoire `posts` à l'intérieur des vues.

Générez un nouveau contrôleur appelé `Posts`, afin qu'il crée automatiquement un répertoire `posts` à l'intérieur des vues également.

```bash
rails g controller posts
```

Comme dans notre application, le `PagesController` est responsable de la page d'accueil, nous devrons interroger les données à l'intérieur de l'action `index` du fichier `pages_controller.rb`. À l'intérieur de l'action `index`, récupérez quelques enregistrements de la table `posts`. Assignez les enregistrements récupérés à une variable d'instance, afin que les objets récupérés soient disponibles dans les vues de la page d'accueil.

* Si vous n'êtes pas familier avec les variables ruby, lisez ce [guide](https://www.tutorialspoint.com/ruby/ruby_variables.htm).
* Si vous n'êtes pas familier avec la récupération d'enregistrements dans la base de données avec Rails, lisez le guide [Active Record Query Interface](http://guides.rubyonrails.org/active_record_querying.html).

L'action `index` devrait ressembler à ceci maintenant :

```rb
def index
  @posts = Post.limit(5)
end
```

Naviguez vers le template de la page d'accueil :

```
views/pages/index.html.erb
```

et à l'intérieur de l'élément `.main-content`, ajoutez :

```
<%= render @posts %>
```

Cela affichera tous les articles qui ont été récupérés dans l'action `index`. Comme les objets `post` appartiennent à la classe `Post`, Rails essaie automatiquement de rendre le template partiel `_post.html.erb` qui se trouve dans :

```
views/posts/_post.html.erb
```

Nous n'avons pas encore créé ce fichier partiel, alors créez-le et ajoutez le code suivant à l'intérieur :

```html
<div class="col-sm-3 single-post-card" id=<%= post_path(post.id) %>>
  <div class="card">
    <div class="card-block">
      <h4 class="post-text">
        <%= truncate(post.title, :length => 60) %>
      </h4>
      <div class="post-content">
        <div class="posted-by">Posté par <%= post.user.name %></div>
        <h3><%= post.title %></h3> 
        <p><%= post.content %></p>
        <%= link_to "Je suis intéressé", post_path(post.id), class: 'interested' %>
      </div>
    </div>
  </div><!-- card -->
</div><!-- col-sm-3 -->
```

J'ai utilisé un composant [bootstrap card](https://v4-alpha.getbootstrap.com/components/card/) ici pour obtenir le style souhaité. Ensuite, j'ai simplement stocké le contenu de l'article et son chemin à l'intérieur de l'élément. J'ai également ajouté un lien qui mènera à l'article complet.

Jusqu'à présent, nous n'avons pas défini de routes pour les articles. Nous en avons besoin maintenant, alors déclarons-les. Ouvrez le fichier `routes.rb` et ajoutez le code suivant à l'intérieur des routes :

```rb
resources :posts do
  collection do
    get 'hobby'
    get 'study'
    get 'team'
  end
end
```

Ici, j'ai utilisé une méthode [resources](http://guides.rubyonrails.org/routing.html#resource-routing-the-rails-default) pour déclarer des routes pour les actions `index`, `show`, `new`, `edit`, `create`, `update` et `destroy`. Ensuite, j'ai déclaré quelques routes de `collection` personnalisées pour accéder aux pages avec plusieurs instances de `Post`. Ces pages seront dédiées à des branches séparées, nous les créerons plus tard.

Redémarrez le serveur et allez sur [http://localhost:3000](http://localhost:3000/). Vous devriez voir les articles rendus à l'écran. L'application devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-79.png)

Commettons les changements.

```bash
git add -A
git commit -m "Display posts on the home page
- Generate Posts controller and create an index action.
  Inside the index action retrieve Post records
- Declare routes for posts
- Create a _post.html.erb partial inside posts directory
- Render posts inside the home page's main content"
```

Pour commencer à styliser les articles, créez un nouveau fichier scss dans le répertoire `partials` :

```
assets/stylesheets/partials/posts.scss
```

et à l'intérieur du fichier, ajoutez le CSS suivant :

```scss
.single-post-card {
  min-height: 135px;
  max-height: 135px;
  box-shadow: 1px 1px 4px rgba(0,0,0, 0.3);
  color: black;
  padding: 10px;
  text-align: left;
  transition: border 0.1s, background 0.5s;
  .post-text {
    overflow: hidden;
  }
  a, a:active, a:hover {
    color: black;
  }
  &:hover {
    cursor: pointer;
    background: white;
    box-shadow: none;
    border-radius: 1%;
  }
}

.post-content {
  display: none;
}

```

La page d'accueil devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-80.png)

Commitez le changement.

```bash
git add -A
git commit -m "Create a posts.scss file and add CSS to it"
```

**Stylisation avec JavaScript**

Actuellement, le design du site est assez terne. Pour créer du contraste, nous allons colorer les articles. Mais au lieu de simplement les colorer avec du CSS, colorons-les avec différents motifs de couleurs chaque fois qu'un utilisateur rafraîchit le site web. Pour ce faire, nous utiliserons du JavaScript. C'est probablement une idée idiote, mais c'est amusant c(o_u)?

Naviguez vers le répertoire `javascripts` à l'intérieur de vos `assets` et créez un nouveau répertoire appelé `posts`. À l'intérieur du répertoire, créez un nouveau fichier appelé `style.js`. De plus, si vous le souhaitez, vous pouvez supprimer les fichiers `.coffee` générés par défaut dans le répertoire `javascripts`. Nous n'utiliserons pas CoffeeScript dans ce tutoriel.

```
assets/javascripts/posts/style.js
```

À l'intérieur du fichier `style.js`, ajoutez le code suivant.

```js
$(document).on('turbolinks:load', function() {
    if ($(".single-post-card").length) {
        // définit un style de couleur de fond unie
        if (mode == 1) {
            $(".single-post-card").each(function() {
                $(this).addClass("solid-color-mode");
                $(this).css('background-color', randomColor());
            });
        }
        // définit un style de couleur de bordure
        else {
            $(".single-post-card").each(function() {
                $(this).addClass("border-color-mode");
                $(this).css('border', '5px solid ' + randomColor());
            });
        }	
    }


    $('#feed').on( 'mouseenter', '.single-post-list', function() {
        $(this).css('border-color', randomColor());	
    });

    $('#feed').on( 'mouseleave', '.single-post-list', function() {
        $(this).css('border-color', 'rgba(0, 0 , 0, 0.05)');	
    });

});

var colorSet = randomColorSet();
var mode = Math.floor(Math.random() * 2);

// Renvoie aléatoirement un schéma de couleurs
function randomColorSet() {
    var colorSet1 = ['#45CCFF', '#49E83E', '#FFD432', '#E84B30', '#B243FF'];
    var colorSet2 = ['#FF6138', '#FFFF9D', '#BEEB9F', '#79BD8F', '#79BD8F'];
    var colorSet3 = ['#FCFFF5', '#D1DBBD', '#91AA9D', '#3E606F', '#193441'];
    var colorSet4 = ['#004358', '#1F8A70', '#BEDB39', '#FFE11A', '#FD7400'];
    var colorSet5 = ['#105B63', '#FFFAD5', '#FFD34E', '#DB9E36', '#BD4932'];
    var colorSet6 = ['#04BFBF', '#CAFCD8', '#F7E967', '#A9CF54', '#588F27'];
    var colorSet7 = ['#405952', '#9C9B7A', '#FFD393', '#FF974F', '#F54F29'];
    var randomSet = [colorSet1, colorSet2, colorSet3, colorSet4, colorSet5, colorSet6, colorSet7];
    return randomSet[Math.floor(Math.random() * randomSet.length )];
}

// Renvoie aléatoirement une couleur d'un tableau de couleurs
function randomColor() {
    var color = colorSet[Math.floor(Math.random() * colorSet.length)];
    return color;
}
```

Avec ce morceau de code, nous définissons aléatoirement l'un des deux modes de style lorsqu'un navigateur est rafraîchi, en ajoutant des attributs aux articles. Un style n'a que des bordures colorées, un autre style a des articles de couleur unie. À chaque changement de page et rafraîchissement du navigateur, nous recolorons également les articles de manière aléatoire. À l'intérieur de la fonction `randomColorSet()`, vous pouvez voir des schémas de couleurs prédéfinis.

Les gestionnaires d'événements `mouseenter` et `mouseleave` seront nécessaires à l'avenir pour les articles dans des pages spécifiques. Là-bas, le style des articles sera différent de celui des articles de la page d'accueil. Lorsque vous survolerez un article, sa couleur de bordure inférieure changera légèrement. Vous verrez cela plus tard.

Commettons les changements.

```bash
git add -A
git commit -m "Create a style.js file and add js to create posts' style"
```

Pour compléter le style, ajoutez du CSS. Ouvrez le fichier `posts.scss` :

```bash
assets/stylesheets/partials/posts.scss
```

et ajoutez le CSS suivant :

```scss
...
.solid-color-mode, .border-color-mode {
  .post-text {
    text-align: center;
  }
}

.solid-color-mode {
  .post-text {
    padding: 10px;
    background-color: white;
    border-radius: 25px;
  }
}

.border-color-mode {
  background-color: white;
}
```

De plus, à l'intérieur de `mobile.scss`, ajoutez le code suivant pour corriger les problèmes de texte trop grand sur les écrans plus petits :

```scss
@media screen and (max-width: 1000px) {
  .solid-color-mode, .border-color-mode {
    .post-text {
      font-size: 16px;  
    }
  }
}
```

La page d'accueil devrait ressembler à ceci maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-81.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-82.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-83.png)

Commettons les changements.

```bash
git add -A
git commit -m "Add CSS to posts on the home page
- add CSS to the posts.scss file"
- ajouter du CSS au fichier mobile.scss pour corriger les problèmes de texte trop grand sur les petits écrans"
```

**Fenêtre modale**

Je veux pouvoir cliquer sur un article et voir son contenu complet, sans changer de page. Pour réaliser cette fonctionnalité, j'utiliserai le [composant modal](https://v4-alpha.getbootstrap.com/components/modal/) de Bootstrap.

À l'intérieur du répertoire `posts`, créez un nouveau fichier partiel `_modal.html.erb` :

```
views/posts/_modal.html.erb
```

et ajoutez le code suivant :

```html
<!-- Modal -->
<div  class="modal myModal" 
      tabindex="-1" 
      role="dialog" 
      aria-labelledby="myModalLabel">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <span class="posted-by"></span>
        <button type="button" 
                class="close" 
                data-dismiss="modal" 
                aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
        <div class="modal-body">
          <div class="loaded-data">
            <h3></h3>
            <p></p>
            <div class="interested"><a href="">Je suis intéressé</a></div>
          </div><!-- loaded-data -->
        </div><!-- modal-body -->
    </div>
  </div>
</div>
```

Il s'agit simplement d'un composant Bootstrap légèrement modifié pour accomplir cette tâche particulière.

Rendez ce partiel en haut du template de la page d'accueil.

```html
<%= render 'posts/modal' %>
...
```

Pour rendre cette fenêtre modale fonctionnelle, nous devons ajouter du JavaScript. À l'intérieur du répertoire `posts`, créez un nouveau fichier `modal.js` :

```
assets/javascripts/posts/modal.js
```

À l'intérieur du fichier, ajoutez le code suivant :

```js
$(document).on('turbolinks:load', function() {
  // lorsqu'on clique sur un article, affiche son contenu complet dans une fenêtre modale
  $("body").on( "click", ".single-post-card, .single-post-list", function() {
    var posted_by = $(this).find('.post-content .posted-by').html();
    var post_heading = $(this).find('.post-content h3').html();
    var post_content = $(this).find('.post-content p').html();
    var interested = $(this).find('.post-content .interested').attr('href');
    $('.modal-header .posted-by').text(posted_by);
    $('.loaded-data h3').text(post_heading);
    $('.loaded-data p').text(post_content);
    $('.loaded-data .interested a').attr('href', interested);
    $('.myModal').modal('show');
  });
});
```

Avec ce code JS, nous stockons simplement les données de l'article sélectionné dans des variables et remplissons les éléments de la fenêtre modale avec ces données. Enfin, avec la dernière ligne de code, nous rendons la fenêtre modale visible.

Pour améliorer l'apparence de la fenêtre modale, ajoutez du CSS. Mais avant d'ajouter le CSS, effectuons une petite tâche de gestion dans le répertoire `stylesheets`.

À l'intérieur du répertoire `partials`, créez un nouveau répertoire appelé `posts` :

```
assets/stylesheets/partials/posts
```

À l'intérieur du répertoire `posts`, créez un nouveau fichier `home_page.scss`. Coupez tout le code du fichier `posts.scss` et collez-le dans le fichier `home_page.scss`. Supprimez le fichier `posts.scss`. Nous faisons cela pour une meilleure gestion du code CSS. Il est plus clair d'avoir plusieurs petits fichiers CSS avec un but distinct, plutôt qu'un seul gros fichier où tout est mélangé.

Également à l'intérieur du répertoire `posts`, créez un nouveau fichier `modal.scss` et ajoutez le CSS suivant :

```scss
.modal-content {
  h3 {
    text-align: center;
  }
  p {
    margin: 50px 0;
  }
  .posted-by {
    color: rgba(0,0,0,0.5);
  }
}

.modal-content {
  .loaded-data {
    h3, p {
      overflow: hidden;
    }
    padding: 0 10px;
    .posted-by {
      margin: 0;
    }
  }
}

.interested {
  text-align: center;
  a {
    background-color: $navbarColor;
    padding: 10px;
    color: white;
    border-radius: 10px;
    &:hover {
      background-color: black;
      color: white;
    }
  }
}
```

Maintenant, lorsque nous cliquons sur l'article, l'application devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-84.png)

Commettez les changements.

```bash
git add -A
git commit -m "Add a popup window to show a full post's content
- Add bootstrap's modal component to show full post's content
- Render the modal inside the home page's template
- Add js to fill the modal with post's content and show it
- Add CSS to style the modal"
```

Fusionnez également la branche `main_feed` avec `master` :

```bash
git checkout master
git merge main_feed
```

Supprimez la branche `main_feed` :

```bash
git branch -D main_feed
```

**Article individuel**

Basculez vers une nouvelle branche :

```bash
git checkout -b single_post
```

**Afficher un article individuel**

Si vous essayez de cliquer sur le bouton `Je suis intéressé`, vous obtiendrez une erreur. Nous n'avons pas encore créé le template `show.html.erb` ni l'action correspondante dans le contrôleur. En cliquant sur le bouton, je veux être redirigé vers la page de l'article sélectionné.

À l'intérieur du `PostsController`, créez une action `show`, puis interrogez et stockez un objet d'article spécifique dans une variable d'instance :

```rb
...
  def show
    @post = Post.find(params[:id])
  end
...
```

Le bouton `Je suis intéressé` redirige vers un article sélectionné. Il possède un attribut `href` avec le chemin vers l'article. En envoyant une requête `GET` pour obtenir un article, Rails appelle l'action `show`. À l'intérieur de l'action `show`, nous avons accès au paramètre `id`, car en envoyant une requête `GET` pour obtenir un article spécifique, nous avons fourni son `id`. Par exemple, en allant sur le chemin `/posts/1`, nous enverrions une requête pour obtenir l'article dont l'id est `1`.

Créez un template `show.html.erb` à l'intérieur du répertoire `posts` :

```
views/posts/show.html.erb
```

À l'intérieur du fichier, ajoutez le code suivant :

```html
<div id="single-post-content" class="container">
  <div class="row">
    <div class="col-sm-6 col-sm-offset-3">
      <div class="posted-by">Posté par <%= @post.user.name %></div>
      <h3><%= @post.title %></h3>
      <p><%= @post.content %></p>
    </div>
  </div><!-- row -->
</div>
```

Créez un fichier `show.scss` à l'intérieur du répertoire `posts` et ajoutez du CSS pour styliser l'apparence de la page :

```scss
#single-post-content {
  background: white;
  height: calc(100vh - 50px);

  h3 { 
    text-align: center;
  }
  p {
    margin: 50px 0;
  }
  .posted-by {
    font-size: 12px;
    font-size: 1.2rem;
    margin: 20px 0;
    color: rgba(0,0,0,0.5);
  }
}
```

Ici, j'ai défini la hauteur de la page à `100vh-50px`, afin que le contenu de la page occupe toute la hauteur de la fenêtre d'affichage (viewport). Cela permet au conteneur d'être coloré en blanc sur toute la hauteur du navigateur, qu'il y ait assez de contenu ou non. La propriété `vh` signifie hauteur du viewport, donc une valeur de `100vh` signifie que l'élément s'étire sur 100 % de la hauteur du viewport. `100vh-50px` est nécessaire pour soustraire la hauteur de la barre de navigation, sinon le conteneur serait trop étiré de `50px`.

Si vous cliquez sur le bouton `Je suis intéressé` maintenant, vous serez redirigé vers une page qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-85.png)

Nous ajouterons des fonctionnalités supplémentaires au template `show.html.erb` plus tard. Maintenant, commettez les changements.

```bash
git add -A
git commit -m "Create a show template for posts
- Add a show action and query a post to an instance variable
- Create a show.scss file and add CSS"
```

**Tests (Specs)**

Au lieu de vérifier manuellement que cette fonctionnalité d'apparition de la fenêtre modale et de redirection vers un article sélectionné fonctionne, couvrons tout cela avec des tests. Nous allons utiliser Capybara pour simuler l'interaction d'un utilisateur avec l'application.

À l'intérieur du répertoire `features`, créez un nouveau répertoire appelé `posts` :

```
spec/features/posts
```

À l'intérieur du nouveau répertoire, créez un nouveau fichier `visit_single_post_spec.rb` :

```
spec/features/posts/visit_single_post_spec.rb
```

Et ajoutez un test de fonctionnalité (feature spec) à l'intérieur. Le fichier ressemble à ceci :

```rb
require "rails_helper"

RSpec.feature "Visit single post", :type => :feature do
  let(:user) { create(:user) }
  let(:post) { create(:post) }

  scenario "User goes to a single post from the home page", js: true do
    post
    visit root_path
    page.find(".single-post-card").click
    expect(page).to have_selector('body .modal')
    page.find('.interested a').click
    expect(page).to have_selector('#single-post-content p', text: post.content)
  end

end
```

Ici, j'ai défini toutes les étapes que j'effectuerais manuellement. Je commence par aller sur la page d'accueil, je clique sur l'article, je m'attends à voir la fenêtre modale apparaître, je clique sur le bouton `Je suis intéressé`, et enfin, je m'attends à être redirigé vers la page de l'article et à voir son contenu.

Par défaut, les matchers RSpec `have_selector`, `have_css`, etc. renvoient vrai si un élément est réellement visible pour un utilisateur. Ainsi, après avoir cliqué sur un article, le framework de test s'attend à voir une fenêtre modale visible. Si vous ne vous souciez pas de savoir si un utilisateur voit l'élément ou non et que vous vous souciez uniquement de la présence d'un élément dans le DOM, passez un argument supplémentaire `visible: false`.

Essayez de lancer le test :

```
rspec spec/features/posts/visit_single_post_spec.rb
```

Commettez les changements.

```bash
git add -A
git commit -m "Add a feature spec to test if a user can go to a
single post from the home page"
```

Fusionnez la branche `single_post` avec `master`.

```bash
git checkout master
git merge single_post
git branch -D single_post
```

**Branches spécifiques**

Chaque article appartient à une branche particulière. Créons des pages spécifiques pour les différentes branches.

Basculez vers une nouvelle branche :

```bash
git checkout -b specific_branches
```

**Menu latéral de la page d'accueil**

Commencez par mettre à jour le menu latéral de la page d'accueil. Ajoutez des liens vers des branches spécifiques. Ouvrez le fichier `index.html.erb` :

```
views/pages/index.html.erb
```

Nous allons placer quelques liens à l'intérieur de l'élément `#side-menu`. Divisez le contenu du fichier en partiels, sinon il deviendra très vite encombré. Coupez les éléments `#side-menu` et `#main-content`, et collez-les dans des fichiers partiels séparés. À l'intérieur du répertoire `pages`, créez un répertoire `index`, et à l'intérieur de ce répertoire, créez les fichiers partiels correspondants aux éléments. Les fichiers devraient ressembler à ceci :

```html
<div id="side-menu"  class="col-sm-3">
</div><!-- side-menu -->
```

```html
<div id="main-content" class="col-sm-9">
  <%= render @posts %>
</div><!-- main-content -->
```

Rendez ces fichiers partiels à l'intérieur du template de la page d'accueil. Le fichier devrait ressembler à ceci :

```html
<%= render 'posts/modal' %>

<div class="container">
  <div class="row">
    <%= render 'pages/index/side_menu' %>
    <%= render 'pages/index/main_content' %>
  </div><!-- row -->
</div><!-- container -->
```

Commettez les changements.

```bash
git add -A
git commit -m "Split home page template's content into partials"
```

À l'intérieur du partiel `_side_menu.html.erb`, ajoutez une liste de liens, de sorte que le fichier ressemble à ceci :

```html
<div id="side-menu"  class="col-sm-3">
  <ul id="links-list">
    <%= render 'pages/index/side_menu/no_login_required_links' %>
  </ul>
</div><!-- side-menu -->
```

Une liste non ordonnée a été ajoutée. À l'intérieur de la liste, nous rendons un autre partiel avec des liens. Ces liens seront disponibles pour tous les utilisateurs, qu'ils soient connectés ou non. Créez ce fichier partiel et ajoutez les liens.

À l'intérieur du répertoire `index`, créez un répertoire `side_menu` :

```
views/pages/index/side_menu
```

À l'intérieur du répertoire, créez un partiel `_no_login_required_links.html.erb` avec le code suivant :

```html
<li id="hobby">
  <%= link_to hobby_posts_path do %>
    <i class="fa fa-user-circle-o" aria-hidden="true"></i> Trouver un partenaire de loisirs
  <% end %>
</li>

<li id="study">
  <%= link_to study_posts_path do %>
    <i class="fa fa-graduation-cap" aria-hidden="true"></i> Trouver un partenaire d'étude
  <% end %>
</li>

<li id="team">
  <%= link_to team_posts_path do %>
    <i class="fa fa-users" aria-hidden="true"></i> Trouver un membre d'équipe
  <% end %>
</li>
```

Ici, nous avons simplement ajouté des liens vers des branches spécifiques d'articles. Si vous vous demandez comment nous avons des chemins tels que `hobby_posts_path`, etc., regardez le fichier `routes.rb`. Précédemment, nous avons ajouté des routes de `collection` imbriquées dans la déclaration `resources :posts`.

Si vous faites attention aux attributs des éléments `i`, vous remarquerez les classes `fa`. Avec ces classes, nous déclarons des icônes [Font Awesome](http://fontawesome.io/icons/). Nous n'avons pas encore configuré cette bibliothèque. Heureusement, c'est très facile à mettre en place. À l'intérieur de l'élément `head` du fichier principal `application.html.erb`, ajoutez la ligne suivante :

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
```

Le menu latéral devrait maintenant être présent.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-86.png)

Commettez les changements.

```bash
git add -A
git commit -m "Add links to the home page's side menu"
```

Sur les écrans plus petits, où la largeur est comprise entre `767px` et `1000px`, le conteneur de Bootstrap est peu esthétique, il semble trop compressé. Étirons-le donc pour ces largeurs. À l'intérieur du fichier `mobile.scss`, ajoutez le code suivant :

```scss
...
@media only screen and (min-width:767px) and (max-width: 1000px) {
  .container {
     width: 100% !important;
  }
}
```

Commettez le changement.

```bash
git add -A
git commit -m "set .container width to 100% 
when viewport's width is between 767px and 1000px"
```

**Page de branche**

Si vous essayez de cliquer sur l'un de ces liens du menu latéral, vous obtiendrez une erreur. Nous n'avons pas configuré les actions dans le `PostsController` ni créé de templates pour cela.

À l'intérieur du `PostsController`, définissez les actions `hobby`, `study` et `team`.

```rb
...  
  def hobby
    posts_for_branch(params[:action])
  end

  def study
    posts_for_branch(params[:action])
  end

  def team
    posts_for_branch(params[:action])
  end
...
```

À l'intérieur de chaque action, la méthode `posts_for_branch` est appelée. Cette méthode renverra les données pour la page spécifique, en fonction du nom de l'action. Définissez la méthode dans la portée `private`.

```rb
...
private

def posts_for_branch(branch)
  @categories = Category.where(branch: branch)
  @posts = get_posts.paginate(page: params[:page])
end
...
```

Dans la variable d'instance `@categories`, nous récupérons toutes les catégories pour une branche spécifique. Par exemple, si vous allez sur la page de la branche hobby, toutes les catégories appartenant à la branche hobby seront récupérées.

Pour obtenir et stocker les articles dans la variable d'instance `@posts`, la méthode `get_posts` est utilisée, puis elle est enchaînée avec une méthode `paginate`. La méthode `paginate` provient de la gem [will_paginate](https://github.com/mislav/will_paginate). Commençons par définir la méthode `get_posts`. À l'intérieur de la portée `private` du `PostsController`, ajoutez :

```rb
...
def get_posts
  Post.limit(30)
end
...
```

Pour l'instant, la méthode `get_posts` récupère simplement n'importe quels 30 articles, sans critère spécifique, afin que nous puissions avancer et nous concentrer sur la suite du développement. Nous reviendrons sur cette méthode prochainement.

Ajoutez la gem `will_paginate` pour pouvoir utiliser la pagination.

```
gem 'will_paginate', '~> 3.1.0'
```

Exécutez :

```bash
bundle install
```

Tout ce qui nous manque maintenant, ce sont les templates. Ils vont être similaires pour toutes les branches, donc au lieu de répéter le code, créez un partiel avec une structure générale pour une branche. À l'intérieur du répertoire `posts`, créez un fichier `_branch.html.erb`.

```html
<div id="branch-main-content" class="container">
  <div class="row">
    <h1 class="page-title"><%= page_title %></h1>
    <%= render 'posts/branch/create_new_post', branch: branch %>
  </div><!-- row -->

  <div class="row">
    <%= render 'posts/branch/categories', branch: branch %>
  </div>

  <div class="row">
    <div class="col-sm-12" id="feed">
      <%= render @posts %>
      <%= render no_posts_partial_path %>		
    </div>
  </div><!-- row -->	

  <div class="infinite-scroll">
    <%= will_paginate @posts %>
  </div>
</div><!-- container -->
```

Tout d'abord, vous voyez une variable `page_title` affichée sur la page. Nous passerons cette variable comme argument lorsque nous rendrons le partiel `_branch.html.erb`. Ensuite, un partiel `_create_new_post` est rendu pour afficher un lien qui mènera à une page où un utilisateur pourra créer un nouvel article. Créez ce fichier partiel à l'intérieur d'un nouveau répertoire `branch` :

```html
<div class="col-sm-12">
  <div class="col-sm-8 col-sm-offset-2">
    <%= render create_new_post_partial_path, branch: branch %>
  </div><!-- col-sm-8 -->	
</div><!-- col-sm-12 -->
```

Ici, nous utiliserons une méthode helper `create_new_post_partial_path` pour déterminer quel fichier partiel rendre. À l'intérieur du fichier `posts_helper.rb`, implémentez la méthode :

```rb
...  
  def create_new_post_partial_path
    if user_signed_in?
      'posts/branch/create_new_post/signed_in'
    else
      'posts/branch/create_new_post/not_signed_in'
    end
  end
...
```

Créez également ces deux partiels correspondants à l'intérieur d'un nouveau répertoire `create_new_post` :

```html
<div class="new-post-button-parent">
  <span>Vous ne trouvez personne ? Essayez de : </span>
  <%= link_to "Créer un nouvel article", 
              new_post_path(branch: branch), 
              :class => "new-post-button" %>
</div>
```

```html
<div class="text-center login-branch">
  Pour créer un nouvel article, vous devez vous 
  <%= link_to 'Connecter', 
              login_path, 
              class: 'login-button login-button-branch' %>
</div>
```

Ensuite, à l'intérieur du fichier `_branch.html.erb`, nous rendons une liste de catégories. Créez un fichier partiel `_categories.html.erb` :

```html
<% branch_path_name = "#{params[:action]}_posts_path" %>

<div class="col-sm-12">
  <ul class="categories-list">
    <%= render all_categories_button_partial_path, 
               branch_path_name: branch_path_name %>
    <% @categories.each do |category| %>
      <li class="category-item">
        <%= link_to category.name, 
                    send(branch_path_name, category: category.name), 
                    :class => ("selected-item" if params[:category] == category.name) %>
      </li>
    <% end %>
  </ul>
</div><!-- col-sm-12 -->
```

À l'intérieur du fichier, nous avons une méthode helper `all_categories_button_partial_path` qui détermine quel fichier partiel rendre. Définissez cette méthode à l'intérieur du fichier `posts_helper.rb` :

```rb
...
   def all_categories_button_partial_path
    if params[:category].blank?
      'posts/branch/categories/all_selected'
    else
      'posts/branch/categories/all_not_selected'
    end
  end
...
```

Toutes les catégories vont être sélectionnées par défaut. Si `params[:category]` est vide, cela signifie qu'aucune catégorie n'a été sélectionnée par l'utilisateur, ce qui signifie que la valeur par défaut `all` (tout) est actuellement sélectionnée. Créez les fichiers partiels correspondants :

```html
<li class="category-item">
  <%= link_to "Tout", 
              send(branch_path_name), 
              :class => "selected-item"  %>
</li>
```

```html
<li class="category-item">
  <%= link_to "Tout", send(branch_path_name) %>
</li>
```

La méthode [send](https://apidock.com/ruby/Object/send) est utilisée ici pour appeler une méthode en utilisant une chaîne de caractères, ce qui permet d'être flexible et d'appeler des méthodes dynamiquement. Dans notre cas, nous générons différents chemins en fonction de l'action actuelle du contrôleur.

Ensuite, à l'intérieur du fichier `_branch.html.erb`, nous rendons les articles et appelons la méthode helper `no_posts_partial_path`. Si aucun article n'est trouvé, la méthode affichera un message.

À l'intérieur de `posts_helper.rb`, ajoutez la méthode helper :

```rb
...
def no_posts_partial_path
  @posts.empty? ? 'posts/branch/no_posts' : 'shared/empty_partial'
end
...
```

Ici, j'utilise un [opérateur ternaire](https://www.w3resource.com/ruby/ruby-ternary-operator.php), afin que le code soit un peu plus propre. S'il y a des articles, je ne veux afficher aucun message. Comme vous ne pouvez pas passer une chaîne vide à la méthode `render`, je passe à la place un chemin vers un partiel vide dans les cas où je ne veux rien rendre.

Créez un répertoire `shared` à l'intérieur des vues, puis créez un partiel vide :

```
views/shared/_empty_partial.html.erb
```

Maintenant, créez un partiel `_no_posts.html.erb` pour le message à l'intérieur du répertoire `branch` :

```html
<div class="text-center">Il n'y a actuellement aucun article publié</div>
```

Enfin, nous utilisons la méthode `will_paginate` de la gem pour diviser les articles en plusieurs pages s'il y en a beaucoup.

Créez des templates pour les actions `hobby`, `study` et `team`. À l'intérieur de ceux-ci, nous rendrons le fichier partiel `_branch.html.erb` et passerons des variables locales spécifiques.

```html
<%= render 'posts/modal' %>
<%= render partial: 'posts/branch', locals: { 
    branch: 'hobby',
    page_title: 'Trouver une personne ayant le même loisir',
    search_placeholder: 'Ex: jouer de la guitare, programmation, cuisine'
  } %>
```

```html
<%= render 'posts/modal' %>
<%= render partial: 'posts/branch', locals: { 
    branch: 'study',
    page_title: 'Trouver une personne qui étudie le même domaine que vous',
    search_placeholder: 'Ex: nutrition, calcul, astrophysique'
  } %>
```

```html
<%= render 'posts/modal' %>
<%= render partial: 'posts/branch', locals: { 
    branch: 'team',
    page_title: 'Trouver une personne ayant des intérêts similaires aux vôtres pour votre équipe',
    search_placeholder: 'Ex: musicien pour un groupe, développeur pour un projet'
  } %>
```

Si vous allez sur l'une de ces pages de branche, vous verrez quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-87.png)

De plus, si vous faites défiler vers le bas, vous verrez que nous avons maintenant une pagination :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-88.png)

Nous avons accompli pas mal de travail pour créer ces pages de branche. Commettez les changements :

```bash
git add -A
git commit -m "Create branch pages for specific posts

- Inside the PostsController define hobby, study and team actions.
  Define a posts_for_branch method and call it inside these actions
- Add will_paginate gem
- Create a _branch.html.erb partial file
- Create a _create_new_post.html.erb partial file
- Define a create_new_post_partial_path helper method
- Create a _signed_in.html.erb partial file
- Create a _not_signed_in.html.erb partial file
- Create a _categories.html.erb partial file
- Define a all_categories_button_partial_path helper method
- Create a _all_selected.html.erb partial file
- Create a _all_not_selected.html.erb partial file
- Define a no_posts_partial_path helper method
- Create a _no_posts.html.erb partial file
- Create a hobby.html.erb template file
- Create a study.html.erb template file
- Create a team.html.erb template file"
```

**Tests (Specs)**

Couvrons les méthodes helper avec des tests. Le fichier `posts_helper_spec.rb` devrait ressembler à ceci :

```rb
require 'rails_helper'

RSpec.describe PostsHelper, :type => :helper do

  context '#create_new_post_partial_path' do
    it "returns a signed_in partial's path" do
      helper.stub(:user_signed_in?).and_return(true)
      expect(helper.create_new_post_partial_path). to (
        eq 'posts/branch/create_new_post/signed_in'
      )
    end

    it "returns a signed_in partial's path" do
      helper.stub(:user_signed_in?).and_return(false)
      expect(helper.create_new_post_partial_path). to (
        eq 'posts/branch/create_new_post/not_signed_in'
      )
    end
  end

  context '#all_categories_button_partial_path' do
    it "returns an all_selected partial's path" do
      controller.params[:category] = ''
      expect(helper.all_categories_button_partial_path).to (
        eq 'posts/branch/categories/all_selected'
      )
    end

    it "returns an all_not_selected partial's path" do
      controller.params[:category] = 'category'
      expect(helper.all_categories_button_partial_path).to (
        eq 'posts/branch/categories/all_not_selected'
      )
    end
  end

  context '#no_posts_partial_path' do
    it "returns a no_posts partial's path" do
      assign(:posts, [])
      expect(helper.no_posts_partial_path).to (
        eq 'posts/branch/no_posts'
      )
    end

    it "returns an empty partial's path" do
      assign(:posts, [1])
      expect(helper.no_posts_partial_path).to (
        eq 'shared/empty_partial'
      )
    end
  end
end
```

Encore une fois, les tests sont assez simples ici. J'ai utilisé la méthode `stub` pour définir les valeurs de retour des méthodes. Pour définir les paramètres, j'ai sélectionné le contrôleur et je l'ai simplement défini comme ceci `controller.params[:param_name]`. Et enfin, j'ai assigné des variables d'instance en utilisant une méthode [assign](https://relishapp.com/rspec/rspec-rails/docs/helper-specs/helper-spec#helper-method-that-accesses-an-instance-variable).

Commettez les changements :

```bash
git add -A
git commit -m "Add specs for PostsHelper methods"
```

**Changements de design**

Dans ces pages de branche, nous voulons avoir un design d'articles différent. Sur la page d'accueil, nous avons le design en cartes. Dans les pages de branche, créons un design en liste, afin qu'un utilisateur puisse voir plus d'articles et les parcourir plus efficacement.

À l'intérieur du répertoire `posts`, créez un répertoire `post` avec un partiel `_home_page.html.erb` à l'intérieur :

```
posts/post/_home_page.html.erb
```

Coupez le contenu du partiel `_post.html.erb` et collez-le dans le fichier partiel `_home_page.html.erb`. À l'intérieur du fichier partiel `_post.html.erb`, ajoutez la ligne de code suivante :

```html
<%= render post_format_partial_path, post: post %>
```

Ici, nous appelons la méthode helper `post_format_partial_path` pour décider quel design d'article rendre, en fonction du chemin actuel. Si un utilisateur est sur la page d'accueil, rendez le design d'article pour la page d'accueil. Si un utilisateur est sur la page de branche, rendez le design d'article pour la page de branche. C'est pourquoi nous avons découpé le contenu du fichier `_post.html.erb` dans le fichier `_home_page.html.erb`.

À l'intérieur du répertoire `post`, créez un nouveau fichier `_branch_page.html.erb` et collez ce code pour définir le design des articles pour la page de branche :

```html
<div class="single-post-list" id=<%= post_path(post.id) %>>
  <%= truncate(post.title, :length => 60) %>
  <div class="post-content">
    <div class="posted-by">Posté par <%= post.user.name %></div>
    <h3><%= post.title %></h3> 
    <p><%= post.content %></p>
    <%= link_to "Je suis intéressé", post_path(post.id), class: 'interested' %> 
  </div>
</div>
```

Pour décider quel fichier partiel rendre, définissez la méthode helper `post_format_partial_path` à l'intérieur de `posts_helper.rb` :

```rb
def post_format_partial_path
  current_page?(root_path) ? 'posts/post/home_page' : 'posts/post/branch_page'
end
```

La méthode helper `post_format_partial_path` ne sera pas disponible dans la page d'accueil, car nous rendons les articles à l'intérieur du template de la page d'accueil, qui appartient à un contrôleur différent. Pour avoir accès à cette méthode à l'intérieur du template de la page d'accueil, incluez `PostsHelper` à l'intérieur de `ApplicationHelper` :

```
include PostsHelper
```

**Tests (Specs)**

Ajoutez des tests pour la méthode helper `post_format_partial_path` :

```rb
...
context '#post_format_partial_path' do
  it "returns a home_page partial's path" do
    helper.stub(:current_page?).and_return(true)
    expect(helper.post_format_partial_path).to (
      eq 'posts/post/home_page'
    )
  end

  it "returns a branch_page partial's path" do
    helper.stub(:current_page?).and_return(false)
    expect(helper.post_format_partial_path).to (
      eq 'posts/post/branch_page'
    )
  end
end
...
```

Commettez les changements :

```bash
git add -A
git commit -m "Add specs for the post_format_partial_path helper method"
```

**CSS**

Décrivez le style des articles dans les pages de branche avec du CSS. À l'intérieur du répertoire `posts`, créez un nouveau fichier de feuille de style `branch_page.scss` :

```scss
.single-post-list {
  min-height: 45px;
  max-height: 45px;
  padding: 10px 20px 10px 0px;
  margin: 0 10px;
  border-bottom: solid 3px rgba(0, 0 , 0, 0.05);
  border-bottom-right-radius: 10%;
  transition: border-color 0.1s;
  overflow: hidden;
  &:hover {
    cursor: pointer;
  }
}

.page-title {
  margin: 30px 0;
  text-align: center;
  background-color: white !important;
  font-weight: bold;
  a {
    color: black;
  }
  a:hover {
    text-decoration: underline;
  }
}

.categories-list {
  margin: 10px 0;
  padding: 0;
}

.category-item {
  display: inline-block;
  margin: 15px 0;
  a {
    font-size: 16px;
    font-size: 1.6rem;
    color: rgba(0,0,0,0.7);
    border: solid 2px rgba(0,0,0,0.4);
    border-radius: 8%;
    padding: 10px;
  }
  a:hover, .selected-item {
    background: $navbarColor;
    color: white;
    border: solid 2px white;
    border-radius: 0px;
  }
}

.new-post-button-parent {
  text-align: right;
  span {
    font-size: 12px;
    font-size: 1.2rem;
  }
}

.new-post-button {
  display: inline-block;
  background: $navbarColor;
  color: white;
  padding: 8px;
  border-radius: 10px;
  font-weight: bold;
  border: solid 2px $navbarColor;
  margin: 10px 0;
  &:hover, &:active, &:focus {
    background: white;
    color: black;
  }
}

.login-branch {
  margin: 10px 0;
}

.login-button-branch {
  padding: 5px 10px;
  border-radius: 10px;
  &:hover, &:active, &:visited, &:link {
    color: white;
  }
}

#branch-main-content {
  background: white;
  height: calc(100vh - 50px);
}

#feed {
  background-color: white;
}
```

À l'intérieur de `base/default.scss`, ajoutez :

```scss
...
.login-button, .sign-up-button {
  background-color: $navbarColor;
  color: white !important;
}
```

Pour corriger les problèmes de style sur les appareils plus petits, à l'intérieur de `responsive/mobile.scss`, ajoutez :

```scss
...
@media screen and (max-width: 550px) {
  .page-title {
      font-size: 20px;
      font-size: 2rem;
  }
  .new-post-button-parent {
    text-align: center;
    span {
      display: none !important;
    }
  }
  .post-button {
    padding: 5px;
  }
  .category-item {
    a {
      padding: 5px;
    }
  }
}

@media screen and (max-width: 767px) {
  .single-post-list {
    min-height: 65px;
    max-height: 65px;
    padding: 10px 0;
  }
}
...
```

Maintenant, les pages de branche devraient ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-89.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-90.png)

Commettez les changements :

```bash
git add -A
git commit -m "Describe the posts style in branch pages

- Create a branch_page.scss file and add CSS
- Add CSS to the default.scss file
- Add CSS to the mobile.scss file"
```

#### **Barre de recherche**

Nous voulons non seulement pouvoir parcourir les articles, mais aussi en rechercher des spécifiques. À l'intérieur du fichier partiel `_branch.html.erb`, au-dessus de la ligne `categories`, ajoutez :

```html
...
<div class="row">
  <%= render  'posts/branch/search_form', 
              branch: branch,
              search_placeholder: search_placeholder %>
</div><!-- row -->
...
```

Créez un fichier partiel `_search_form.html.erb` à l'intérieur du répertoire `branch` et ajoutez le code suivant à l'intérieur :

```html
<div class="col-sm-12">
  <%= form_tag(send("#{branch}_posts_path"), 
               :method => "get", 
               id: "search-form") do %>
    <i class="fa fa-search" aria-hidden="true"></i>
    <%= text_field_tag  :search, 
                        params[:search], 
                        placeholder: search_placeholder, 
                        class: "form-control" %>
    <%= render category_field_partial_path %>
  <% end %>
</div><!-- col-sm-12 -->
```

Ici, avec la méthode `send`, nous générons dynamiquement un chemin vers une action spécifique du `PostsController`, en fonction de la branche actuelle. Nous envoyons également un champ de données supplémentaire pour la catégorie si une catégorie spécifique est sélectionnée. Si un utilisateur a sélectionné une catégorie spécifique, seuls les résultats de recherche de cette catégorie seront renvoyés.

Définissez la méthode helper `category_field_partial_path` à l'intérieur de `posts_helper.rb` :

```rb
...  
  def category_field_partial_path
    if params[:category].present?
      'posts/branch/search_form/category_field'
    else
      'shared/empty_partial'
    end
  end
...
```

Créez un fichier partiel `_category_field.html.erb` et ajoutez le code :

```html
<%= hidden_field_tag :category, params[:category] %>
```

Pour donner du style au formulaire de recherche, ajoutez du CSS au fichier `branch_page.scss` :

```scss
.fa-search {
  position:absolute; 
  bottom:14px; 
  left:10px; 
  width:20px; 
  height:10px;
}

#search-form {
  position:relative;
  input {
    border: solid 2px rgba(0,0,0,0.2);
    border-radius: 10px;
    box-shadow: none;
    outline: 0;
  }
  input:focus {
    border: solid 2px rgba(0,0,0,0.35);
  }
  input#search {
    padding: 15px;
    width: 100%;
    height:20px; 
    margin: 10px 0; 
    padding-left: 30px;
  }
}
```

Le formulaire de recherche, dans les pages de branche, devrait maintenant ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-91.png)

Commettez les changements :

```bash
git add -A
git commit -m "Add a search form in branch pages
- Render a search form inside the _branch.html.erb
- Create a _search_form.html.erb partial file
- Define a category_field_partial_path helper method in PostsHelper
- Create a _category_field.html.erb partial file
- Add CSS for the the search form in branch_page.scss"
```

Actuellement, notre formulaire n'est pas vraiment fonctionnel. Nous pourrions utiliser des gems pour obtenir une fonctionnalité de recherche, mais nos données ne sont pas compliquées, nous pouvons donc créer notre propre moteur de recherche simple. Nous utiliserons des [scopes](http://guides.rubyonrails.org/active_record_querying.html#scopes) à l'intérieur du modèle `Post` pour rendre les requêtes chaînables et une certaine logique conditionnelle à l'intérieur du contrôleur (nous l'extrairons dans un objet de service dans la section suivante pour rendre le code plus propre).

Commencez par définir les scopes à l'intérieur du modèle `Post`. Pour vous échauffer, définissez le `default_scope` à l'intérieur du fichier `post.rb`. Cela trie les articles par ordre décroissant de date de création, les articles les plus récents étant en haut.

```rb
...
default_scope -> { includes(:user).order(created_at: :desc) }
...
```

Commettez le changement :

```bash
git add -A
git commit -m "Define a default_scope for posts"
```

Assurez-vous que le `default_scope` fonctionne correctement en le couvrant par un test. À l'intérieur du fichier `post_spec.rb`, ajoutez :

```rb
context 'Scopes' do
  it 'default_scope orders by descending created_at' do
    first_post = create(:post)
    second_post = create(:post)
    expect(Post.all).to eq [second_post, first_post]
  end
end
```

Commettez le changement :

```bash
git add -A
git commit -m "Add a spec for the Post model's default_scope"
```

Maintenant, rendons la barre de recherche fonctionnelle. À l'intérieur de `posts_controller.rb`, remplacez le contenu de la méthode `get_posts` par :

```rb
def get_posts
  branch = params[:action]
  search = params[:search]
  category = params[:category]

  if category.blank? && search.blank?
    posts = Post.by_branch(branch).all
  elsif category.blank? && search.present?
    posts = Post.by_branch(branch).search(search)
  elsif category.present? && search.blank?
    posts = Post.by_category(branch, category)
  elsif category.present? && search.present?
    posts = Post.by_category(branch, category).search(search)
  else
  end
end
```

Comme je l'ai mentionné un peu plus tôt, la logique, tout comme dans les vues, n'est pas vraiment à sa place dans les contrôleurs. Nous voulons qu'ils restent propres. Nous allons donc extraire la logique de cette méthode dans la section suivante.

Comme vous le voyez, il y a une certaine logique conditionnelle. Selon la requête de l'utilisateur, les données sont interrogées différemment à l'aide de scopes.

À l'intérieur du modèle `Post`, définissez ces scopes :

```rb
...
  scope :by_category, -> (branch, category_name) do 
    joins(:category).where(categories: {name: category_name, branch: branch}) 
  end

  scope :by_branch, -> (branch) do
    joins(:category).where(categories: {branch: branch}) 
  end

  scope :search, -> (search) do
    where("title ILIKE lower(?) OR content ILIKE lower(?)", "%#{search}%", "%#{search}%")
  end
...
```

La méthode `[joins](http://guides.rubyonrails.org/active_record_querying.html#joins)` est utilisée pour interroger des enregistrements à partir des tables associées. De plus, la syntaxe SQL de base est utilisée pour trouver des enregistrements basés sur les chaînes de caractères fournies.

Maintenant, si vous redémarrez le serveur et retournez sur l'une de ces pages de branche, la barre de recherche devrait fonctionner ! De plus, vous pouvez maintenant filtrer les articles en cliquant sur les boutons de catégorie. Et aussi, lorsque vous sélectionnez une catégorie particulière, seuls les articles de cette catégorie sont interrogés lorsque vous utilisez le formulaire de recherche.

Commettez les changements :

```bash
git add -A
git commit -m "Make search bar and category filters 
in branch pages functional
- Add by_category, by_branch and search scopes in the Post model
- Modify the get_posts method in PostsController"
```

Couvrons ces scopes avec des tests. À l'intérieur du contexte `Scopes` du fichier `post_spec.rb`, ajoutez :

```rb
...
  it 'by_category scope gets posts by particular category' do
    category = create(:category)
    create(:post, category_id: category.id)
    create_list(:post, 10)
    posts = Post.by_category(category.branch, category.name)
    expect(posts.count).to eq 1
    expect(posts[0].category.name).to eq category.name
  end

  it 'by_branch scope gets posts by particular branch' do
    category = create(:category)
    create(:post, category_id: category.id)
    create_list(:post, 10)
    posts = Post.by_branch(category.branch)
    expect(posts.count).to eq 1
    expect(posts[0].category.branch).to eq category.branch
  end

  it 'search finds a matching post' do
    post = create(:post, title: 'awesome title', content: 'great content ' * 5)
    create_list(:post, 10, title: ('a'..'c' * 2).to_a.shuffle.join)
    expect(Post.search('awesome').count).to eq 1
    expect(Post.search('awesome')[0].id).to eq post.id
    expect(Post.search('great').count).to eq 1
    expect(Post.search('great')[0].id).to eq post.id
  end
...
```

Commettez les changements :

```bash
git add -A
git commit -m "Add specs for Post model's 
by_branch, by_category and search scopes"
```

#### **Défilement infini (Infinite scroll)**

Lorsque vous allez sur l'une de ces pages de branche, vous voyez la pagination en bas de la page :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-92.png)

Lorsque vous cliquez sur le lien suivant, cela vous redirige vers une autre page avec des articles plus anciens. Au lieu de rediriger vers une autre page, nous pouvons créer une fonctionnalité de défilement infini, similaire au flux de Facebook et Twitter. Vous faites simplement défiler vers le bas et, sans aucune redirection ni rechargement de page, les articles plus anciens sont ajoutés au bas de la liste. Étonnamment, c'est très facile à réaliser. Tout ce que nous avons à faire est d'écrire un peu de JavaScript. Chaque fois qu'un utilisateur atteint le bas de la page, une requête [AJAX](https://www.w3schools.com/xml/ajax_intro.asp) est envoyée pour obtenir les données de la page `suivante` et ces données sont ajoutées au bas de la liste.

Commencez par configurer la requête AJAX et ses conditions. Lorsqu'un utilisateur dépasse un certain seuil en faisant défiler vers le bas, la requête AJAX est déclenchée. À l'intérieur du répertoire `javascripts/posts`, créez un nouveau fichier `infinite_scroll.js` et ajoutez le code :

```js
$(document).on('turbolinks:load', function() {
  var isLoading = false;
  if ($('.infinite-scroll', this).size() > 0) {
    $(window).on('scroll', function() {
      var more_posts_url = $('.pagination a.next_page').attr('href');
      var threshold_passed = $(window).scrollTop() > $(document).height() - $(window).height() - 60;
      if (!isLoading && more_posts_url && threshold_passed) {
        isLoading = true;
        $.getScript(more_posts_url).done(function (data,textStatus,jqxhr) {
          isLoading = false;
        }).fail(function() {
          isLoading = false;
        });
      }
    });
  }
});
```

La variable `isLoading` garantit qu'une seule requête est envoyée à la fois. Si une requête est actuellement en cours, d'autres requêtes ne seront pas initiées.

Tout d'abord, vérifiez si la pagination est présente, s'il y a d'autres articles à rendre. Ensuite, obtenez un lien vers la page suivante, c'est là que les données seront récupérées. Définissez ensuite un seuil pour appeler une requête AJAX, dans ce cas, le seuil est de `60px` du bas de la fenêtre. Enfin, si toutes les conditions sont remplies avec succès, chargez les données de la page `suivante` en utilisant la fonction `[getScript()](https://api.jquery.com/jquery.getscript/)`.

Comme la fonction `getScript()` charge le fichier JavaScript, nous devons spécifier quel fichier rendre à l'intérieur du `PostsController`. À l'intérieur de la méthode `posts_for_branch`, spécifiez les formats `respond_to` et les fichiers à rendre.

```rb
respond_to do |format|
  format.html
  format.js { render partial: 'posts/posts_pagination_page' }
end
```

Lorsque le contrôleur tente de répondre avec le fichier `.js`, le template `posts_pagination_page` est rendu. Ce fichier partiel ajoute les articles nouvellement récupérés à la liste. Créez ce fichier pour ajouter de nouveaux articles et mettre à jour l'élément de pagination.

```js
$('#feed').append('<%= j render @posts %>');
<%= render update_pagination_partial_path %>
```

Créez une méthode helper `update_pagination_partial_path` à l'intérieur de `posts_helper.rb` :

```rb
def update_pagination_partial_path
  if @posts.next_page
    'posts/posts_pagination_page/update_pagination'
  else
    'posts/posts_pagination_page/remove_pagination'
  end
end
```

Ici, la méthode `next_page` de la gem `will_paginate` est utilisée pour déterminer s'il y a encore des articles à charger à l'avenir ou non.

Créez les fichiers partiels correspondants :

```js
$('.pagination').replaceWith('<%= j will_paginate @posts %>');
```

```js
$(window).off('scroll');
$('.pagination').remove();
```

Si vous allez sur l'une des pages de branche et faites défiler vers le bas, les articles plus anciens devraient être automatiquement ajoutés à la liste.

De plus, nous n'avons plus besoin de voir le menu de pagination, cachez-le donc avec du CSS. À l'intérieur du fichier `branch_page.scss`, ajoutez :

```scss
...
.infinite-scroll {
  display: none;
}
...
```

Commettez les changements :

```bash
git add -A
git commit -m "Transform posts pagination into infinite scroll
- Create an infinite_scroll.js file
- Inside PostController's posts_for_branch method add respond_to format
- Define an update_pagination_partial_path
- Create _update_pagination.js.erb and _remove_pagination.js.erb partials
- hide the .infinite-scroll element with CSS"
```

**Tests (Specs)**

Couvrons la méthode helper `update_pagination_partial_path` avec des tests :

```rb
context '#update_pagination_partial_path' do
  it "returns an update_pagination partial's path" do
    posts = double('posts', :next_page => 2)
    assign(:posts, posts)
    expect(helper.update_pagination_partial_path).to(
      eq 'posts/posts_pagination_page/update_pagination'
    )
  end

  it "returns a remove_pagination partial's path" do
    posts = double('posts', :next_page => nil)
    assign(:posts, posts)
    expect(helper.update_pagination_partial_path).to(
      eq 'posts/posts_pagination_page/remove_pagination'
    )
  end
end
```

Ici, j'ai utilisé un `double` de test pour simuler la variable d'instance `posts` et sa méthode enchaînée `next_page`. Vous pouvez en apprendre davantage sur les Mocks RSpec [ici](https://relishapp.com/rspec/rspec-mocks/docs).

Commettez les changements :

```bash
git add -A
git commit -m "Add specs for the update_pagination_partial_path
helper method"
```

Nous pouvons également écrire des tests de fonctionnalité pour nous assurer que les articles sont bien ajoutés après avoir fait défiler vers le bas. Créez un fichier `infinite_scroll_spec.rb` :

```rb
require "rails_helper"

RSpec.feature "Infinite scroll", :type => :feature do
  Post.per_page = 15  

  let(:check_posts_count) do
    expect(page).to have_selector('.single-post-list', count: 15)
    page.execute_script("$(window).scrollTop($(document).height())")
    expect(page).to have_selector('.single-post-list', count: 30)
  end

  scenario "User scrolls down the hobby page 
            and posts list will be appended with older posts", js: true do      
    create_list(:post, 30, category: create(:category, branch: 'hobby'))     
    visit hobby_posts_path
    check_posts_count
  end

  scenario "User scrolls down the study page 
            and posts list will be appended with older posts", js: true do      
    create_list(:post, 30, category: create(:category, branch: 'study'))        
    visit study_posts_path
    check_posts_count
  end

  scenario "User scrolls down the team page 
            and posts list will be appended with older posts", js: true do      
    create_list(:post, 30, category: create(:category, branch: 'team'))      
    visit team_posts_path
    check_posts_count
  end

end
```

Dans le fichier de test, toutes les pages de branche sont couvertes. Nous nous assurons que cette fonctionnalité fonctionne sur les trois pages. `per_page` est une méthode de la gem `will_paginate`. Ici, le modèle `Post` est sélectionné et le nombre par défaut d'articles par page est défini.

La méthode `check_posts_count` est définie pour réduire la quantité de code dans le fichier. Au lieu de répéter le même code encore et encore dans différents tests, nous l'avons extrait dans une seule méthode. Une fois la page visitée, on s'attend à voir 15 articles. Ensuite, la méthode `execute_script` est utilisée pour exécuter du JavaScript, qui fait défiler la barre de défilement jusqu'au bas du navigateur. Enfin, après le défilement, on s'attend à voir 15 articles supplémentaires. Au total, il devrait y avoir 30 articles sur la page.

Commettez les changements :

```bash
git add -A
git commit -m "Add feature specs for posts' infinite scroll functionality"
```

**Mise à jour de la page d'accueil**

Actuellement, sur la page d'accueil, nous ne pouvons voir que quelques articles aléatoires. Modifiez la page d'accueil pour que nous puissions voir quelques articles de toutes les branches.

Remplacez le contenu du fichier `_main_content.html.erb` par :

```html
<div id="main-content" class="col-sm-9">
  <h3 class="page-name"><%= link_to 'Loisirs', hobby_posts_path %></h3>
  <div class="row">
    <%= render @hobby_posts %>
    <%= render no_posts_partial_path(@hobby_posts) %>
  </div><!-- row -->

  <h3 class="page-name"><%= link_to 'Études', study_posts_path %></h3>
  <div class="row">
    <%= render @study_posts %>
    <%= render no_posts_partial_path(@study_posts) %>
  </div><!-- row -->

  <h3 class="page-name"><%= link_to 'Membre d\'équipe', team_posts_path %></h3>
  <div class="row">
    <%= render @team_posts %>
    <%= render no_posts_partial_path(@team_posts) %>
  </div><!-- row -->
</div><!-- main_content -->
```

Nous avons créé des sections avec des articles pour chaque branche.

Définissez les variables d'instance à l'intérieur de l'action `index` du `PagesController`. L'action devrait ressembler à ceci :

```rb
  def index
    @hobby_posts = Post.by_branch('hobby').limit(8)
    @study_posts = Post.by_branch('study').limit(8)
    @team_posts = Post.by_branch('team').limit(8)
  end
```

Nous avons la méthode helper `no_posts_partial_path` d'avant, mais nous devrions la modifier un peu pour la rendre plus réutilisable. Actuellement, elle ne fonctionne que pour les pages de branche. Ajoutez un paramètre `posts` à la méthode, afin qu'elle ressemble maintenant à ceci :

```rb
def no_posts_partial_path(posts)
  posts.empty? ? 'posts/shared/no_posts' : 'shared/empty_partial'
end
```

Ici, le paramètre `posts` a été ajouté, la variable d'instance a été changée en une variable simple et le chemin du partiel a également été modifié. Déplacez donc le fichier partiel `_no_posts.html.erb` de :

```
posts/branch/_no_posts.html.erb
```

vers :

```
posts/shared/_no_posts.html.erb
```

De plus, à l'intérieur du fichier `_branch.html.erb`, passez la variable d'instance `@posts` à la méthode `no_posts_partial_path` comme argument.

Ajoutez quelques changements de style. À l'intérieur du fichier `default.scss`, ajoutez :

```scss
...
.container {
  padding: 0;
}

.row {
  margin: 0;
}
```

Et à l'intérieur de `home_page.scss`, ajoutez :

```scss
.page-name {
  margin: 15px 0px 15px 0px;
  text-align: center;
  background-color: white !important;
  font-weight: bold;
  a {
    color: black;
  }
  a:hover {
    text-decoration: underline;
  }
}
...
```

La page d'accueil devrait ressembler à ceci maintenant :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-93.png)

Commettez les changements :

```bash
git add -A
git commit -m "Add posts from all branches in the home page
- Modify the _main_content.html.erb file
- Define instance variables inside the PagesController’s index action
- Modify the no_posts_partial_path helper method to be more reusable
- Add CSS to style the home page"
```

#### Objets de service (Service objects)

Comme je l'ai mentionné précédemment, si vous mettez de la logique à l'intérieur des contrôleurs, ils deviennent très vite compliqués et pénibles à tester. C'est pourquoi il est judicieux d'extraire la logique de ceux-ci ailleurs. Pour ce faire, j'utilise des patrons de conception (design patterns), plus précisément des objets de service (services).

Actuellement, à l'intérieur du `PostsController`, nous avons cette méthode :

```rb
def get_posts
  branch = params[:action]
  search = params[:search]
  category = params[:category]

  if category.blank? && search.blank?
    posts = Post.by_branch(branch).all
  elsif category.blank? && search.present?
    posts = Post.by_branch(branch).search(search)
  elsif category.present? && search.blank?
    posts = Post.by_category(branch, category)
  elsif category.present? && search.present?
    posts = Post.by_category(branch, category).search(search)
  else
  end
end
```

Elle contient beaucoup de logique conditionnelle que je veux supprimer en utilisant des services. Le patron de conception des objets de service (services) est simplement une [classe Ruby](https://www.tutorialspoint.com/ruby/ruby_classes.htm) de base. C'est très simple, nous passons simplement les données que nous voulons traiter et appelons une méthode définie pour obtenir une valeur de retour souhaitée.

En Ruby, nous passons les données à la méthode `initialize` de la classe, connue dans d'autres langages sous le nom de `constructeur`. Ensuite, à l'intérieur de la classe, nous créons simplement une méthode qui gérera toute la logique définie. Créons cela et voyons à quoi cela ressemble dans le code.

À l'intérieur du répertoire `app`, créez un nouveau répertoire `services` :

```
app/services
```

À l'intérieur du répertoire, créez un nouveau fichier `posts_for_branch_service.rb` :

```rb
class PostsForBranchService
  def initialize(params)
    @search = params[:search]
    @category = params[:category]
    @branch = params[:branch]
  end

  # obtenir les articles en fonction de la requête
  def call
    if @category.blank? && @search.blank?
      posts = Post.by_branch(@branch).all
    elsif @category.blank? && @search.present?
      posts = Post.by_branch(@branch).search(@search)
    elsif @category.present? && @search.blank?
      posts = Post.by_category(@branch, @category)
    elsif @category.present? && @search.present?
      posts = Post.by_category(@branch, @category).search(@search)
    else
    end
  end

end
```

Ici, comme décrit ci-dessus, il s'agit simplement d'une classe Ruby ordinaire avec une méthode `initialize` pour accepter les paramètres et une méthode `call` pour gérer la logique. Nous avons repris cette logique de la méthode `get_posts`.

Maintenant, créez simplement un nouvel objet de cette classe et appelez la méthode `call` à l'intérieur de la méthode `get_posts`. La méthode devrait ressembler à ceci maintenant :

```rb
  def get_posts
    PostsForBranchService.new({
      search: params[:search],
      category: params[:category],
      branch: params[:action]
    }).call
  end
```

Commettez les changements :

```bash
git add -A
git commit -m "Create a service object to extract logic
from the get_posts method"
```

**Tests (Specs)**

L'avantage des patrons de conception comme les services est qu'il est facile d'écrire des tests unitaires pour eux. Nous pouvons simplement écrire des tests pour la méthode `call` et tester chacune de ses conditions.

À l'intérieur du répertoire `spec`, créez un nouveau répertoire `services` :

```
spec/services
```

À l'intérieur du répertoire, créez un nouveau fichier `posts_for_branch_service_spec.rb` :

```rb
require 'rails_helper'
require './app/services/posts_for_branch_service.rb'

describe PostsForBranchService do

  context '#call' do
    let(:not_included_posts) { create_list(:post, 2) }
    let(:category) { create(:category, branch: 'hobby', name: 'arts') }
    let(:post) do
      create(:post,
              title: 'a very fun post', 
              category_id: category.id)
    end
    it 'returns posts filtered by a branch' do
      not_included_posts
      category
      included_posts = create_list(:post, 2, category_id: category.id)
      expect(PostsForBranchService.new({branch: 'hobby'}).call).to(
        match_array included_posts
      )
    end

    it 'returns posts filtered by a branch and a search input' do
      not_included_posts
      category
      included_post = [] << post
      expect(PostsForBranchService.new({branch: 'hobby', search: 'fun'}).call).to(
        eq included_post
      )
    end

    it 'returns posts filtered by a category name' do
      not_included_posts
      category
      included_post = [] << post
      expect(PostsForBranchService.new({branch: 'hobby', category: 'arts'}).call).to(
        eq included_post
      )
    end

    it 'returns posts filtered by a category name and a search input' do
      not_included_posts
      category
      included_post = [] << post
      expect(PostsForBranchService.new({name: 'arts', 
                                        search: 'fun', 
                                        branch: 'hobby'}).call).to eq included_post
    end
  end
end
```

En haut du fichier, le fichier `posts_for_branch_service.rb` est chargé, puis chacune des conditions de la méthode `call` est testée.

Commettez les changements :

```bash
git add -A
git commit -m "Add specs for the PostsForBranchService"
```

#### Créer un nouvel article

Jusqu'à présent, les articles étaient créés artificiellement, en utilisant des seeds. Ajoutons une interface utilisateur pour cela, afin qu'un utilisateur puisse créer des articles.

À l'intérieur du fichier `posts_controller.rb`, ajoutez les actions `new` et `create`.

```rb
...
  def new
    @branch = params[:branch]
    @categories = Category.where(branch: @branch)
    @post = Post.new
  end

  def create
    @post = Post.new(post_params)
    if @post.save 
      redirect_to post_path(@post) 
    else
      redirect_to root_path
    end
  end
...
```

À l'intérieur de l'action `new`, nous définissons quelques variables d'instance pour le formulaire de création de nouveaux articles. Dans la variable d'instance `@categories`, les catégories pour une branche spécifique sont stockées. La variable d'instance `@post` stocke un objet d'un nouvel article, ce qui est nécessaire pour le formulaire Rails.

À l'intérieur de la variable d'instance `@post` de l'action `create`, nous créons un nouvel objet `Post` et le remplissons avec des données, en utilisant la méthode `post_params`. Définissez cette méthode dans la portée `private` :

```rb
...
def post_params
  params.require(:post).permit(:content, :title, :category_id)
                       .merge(user_id: current_user.id)
end
...
```

La méthode `[permit](https://apidock.com/rails/ActionController/Parameters/permit)` est utilisée pour mettre en liste blanche les attributs de l'objet, de sorte que seuls ces attributs spécifiés sont autorisés à être passés.

De plus, en haut du `PostsController`, ajoutez la ligne suivante :

```rb
...
before_action :redirect_if_not_signed_in, only: [:new]
...
```

Le `before_action` est l'un des [filtres](http://guides.rubyonrails.org/action_controller_overview.html#filters) de Rails. Nous ne voulons pas permettre aux utilisateurs non connectés d'avoir accès à une page où ils peuvent créer de nouveaux articles. Ainsi, avant d'appeler l'action `new`, la méthode `redirect_if_not_signed_in` est appelée. Nous aurons besoin de cette méthode dans d'autres contrôleurs également, définissez-la donc à l'intérieur du fichier `application_controller.rb`. Une méthode pour rediriger les utilisateurs connectés serait également utile à l'avenir. Définissez-les donc toutes les deux.

```rb
...
def redirect_if_not_signed_in
  redirect_to root_path if !user_signed_in?
end

def redirect_if_signed_in
  redirect_to root_path if user_signed_in?
end
...
```

Maintenant, le template `new` est requis pour qu'un utilisateur puisse créer de nouveaux articles. À l'intérieur du répertoire `posts`, créez un fichier `new.html.erb` :

```html
<div class="container new-post">
  <div class="row">
    <div class="col-sm-6 col-sm-offset-3">
      <h1>Créer un nouvel article</h1>
        <%= render 'posts/new/post_form' %>
    </div>
  </div>
</div>
```

Créez un répertoire `new` et un fichier partiel `_post_form.html.erb` à l'intérieur :

```html
<%= bootstrap_form_for(@post) do |f| %>
  <%= f.text_field  :title, 
                    maxlength: 100, 
                    placeholder: 'Titre', 
                    class: 'form-control',
                    required: true, 
                    minlength: 5,
                    maxlength: 100 %>
  <%= f.hidden_field :branch, :value => @branch %>
  <%= f.text_area :content, 
                  rows: 6,
                  required: true, 
                  minlength: 20,
                  maxlength: 1000,
                  placeholder: 'Décrivez ce que vous recherchez. Ex: intérêts spécifiques, niveau d\'expertise, etc.', 
                  class: 'form-control' %>
  <%= f.collection_select :category_id, @categories, :id, :name, class: 'form-control' %>
  <%= f.submit "Créer un article", class: 'form-control' %>
<% end %>
```

Le formulaire est assez simple. Les attributs des champs sont définis et la méthode `collection_select` est utilisée pour permettre de sélectionner l'une des catégories disponibles.

Commettez les changements :

```bash
git add -A
git commit -m "Create a UI to create new posts
- Inside the PostsController: 
  define new and create actions
  define a post_params method
  define a before_action filter
- Inside the ApplicationController:
  define a redirect_if_not_signed_in method
  define a redirect_if_signed_in method
- Create a new template for posts"
```

Nous pouvons tester si le formulaire fonctionne en écrivant des tests. Commencez par écrire des [tests de requête (request specs)](https://relishapp.com/rspec/rspec-rails/docs/request-specs/request-spec), pour vous assurer que nous obtenons les réponses correctes après avoir envoyé des requêtes particulières. À l'intérieur du répertoire `spec`, créez quelques répertoires :

```
spec/requests/posts
```

Et un fichier `new_spec.rb` à l'intérieur :

```rb
require 'rails_helper'
include Warden::Test::Helpers
RSpec.describe "new", :type => :request do

  context 'non-signed in user' do
    it 'redirects to a root path' do
      get '/posts/new'
      expect(response).to redirect_to(root_path)
    end
  end

  context 'signed in user' do
    let(:user) { create(:user) }
    before(:each) { login_as user }

    it 'renders a new template' do
      get '/posts/new'
      expect(response).to render_template(:new)
    end
  end

end
```

Comme mentionné dans la documentation, les tests de requête fournissent une fine couche autour des tests d'intégration. Nous testons donc si nous obtenons les réponses correctes lorsque nous envoyons certaines requêtes. La ligne `include Warden::Test::Helpers` est requise pour utiliser la méthode `login_as`. Cette méthode connecte un utilisateur.

Commettez le changement :

```bash
git add -A
git commit -m "Add request specs for a new post template"
```

Nous pouvons même ajouter d'autres tests de requête pour les pages que nous avons créées précédemment.

À l'intérieur du même répertoire, créez un fichier `branches_spec.rb` :

```rb
require 'rails_helper'
include Warden::Test::Helpers
RSpec.describe "branches", :type => :request do

  shared_examples 'render_templates' do
    it 'renders a hobby template' do
      get '/posts/hobby'
      expect(response).to render_template(:hobby)
    end

    it 'renders a study template' do
      get '/posts/study'
      expect(response).to render_template(:study)
    end

    it 'renders a team template' do
      get '/posts/team'
      expect(response).to render_template(:team)
    end
  end

  context 'non-signed in user' do
    it_behaves_like 'render_templates'
  end

  context 'signed in user' do
    let(:user) { create(:user) }
    before(:each) { login_as user }

    it_behaves_like 'render_templates'
  end

end
```

De cette façon, nous vérifions que tous les templates des pages de branche sont rendus avec succès. De plus, `[shared_examples](https://relishapp.com/rspec/rspec-core/docs/example-groups/shared-examples)` est utilisé pour réduire le code répétitif.

Commettez le changement :

```bash
git add -A
git commit -m "Add request specs for Posts branch pages' templates"
```

Nous pouvons également nous assurer que le template `show` se rend avec succès. À l'intérieur du même répertoire, créez un fichier `show_spec.rb` :

```rb
require 'rails_helper'
include Warden::Test::Helpers
RSpec.describe "show", :type => :request do

  shared_examples 'render_show_template' do
    let(:post) { create(:post) }
    it 'renders a show template' do
      get post_path(post)
      expect(response).to render_template(:show)
    end
  end

  context 'non-signed in user' do
    it_behaves_like 'render_show_template'
  end

  context 'signed in user' do
    let(:user) { create(:user) }
    before(:each) { login_as user }

    it_behaves_like 'render_show_template'
  end

end
```

Commettez les changements :

```bash
git add -A
git commit -m "Add request specs for the Posts show template"
```

Pour s'assurer qu'un utilisateur est capable de créer un nouvel article, écrivez des tests de fonctionnalité pour tester le formulaire. À l'intérieur du répertoire `features/posts`, créez un nouveau fichier `create_new_post_spec.rb` :

```rb
require "rails_helper"

RSpec.feature "Create a new post", :type => :feature do
  let(:user) { create(:user) }
  before(:each) { sign_in user }

  shared_examples 'user creates a new post' do |branch|
    scenario 'successfully' do
      create(:category, name: 'category', branch: branch)
      visit send("#{branch}_posts_path")
      find('.new-post-button').click
      fill_in 'post[title]', with: 'a' * 20
      fill_in 'post[content]', with: 'a' * 20
      select 'category', from: 'post[category_id]' 
      click_on 'Create a post'
      expect(page).to have_selector('h3', text: 'a' * 20)
    end
  end

  include_examples 'user creates a new post', 'hobby'
  include_examples 'user creates a new post', 'study'
  include_examples 'user creates a new post', 'team'
end
```

Commettez les changements :

```bash
git add -A
git commit -m "Create a create_new_post_spec.rb file with feature specs"
```

Appliquez un peu de design au template `new`.

Dans le répertoire suivant :

```
assets/stylesheets/partials/posts
```

Créez un fichier `new.scss` :

```scss
.new-post {
  height: calc(100vh - 50px);
  background-color: white;
  h1 {
    text-align: center;
    margin: 25px 0;
  }
  input, textarea, select {
    width: 100%;
  }
}
```

Si vous allez sur le template dans un navigateur maintenant, vous devriez voir un formulaire de base :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-94.png)

Commettez les changements :

```bash
git add -A
git commit -m "Add CSS to the Posts new.html.erb template"
```

Enfin, nous voulons nous assurer que tous les champs sont remplis correctement. À l'intérieur du modèle `Post`, nous allons définir quelques [validations](http://guides.rubyonrails.org/active_record_validations.html). Ajoutez le code suivant au modèle `Post` :

```rb
...
validates :title, presence: true, length: { minimum: 5, maximum: 255 }
validates :content, presence: true, length: { minimum: 20, maximum: 1000 }
validates :category_id, presence: true
...
```

Commettez les changements :

```bash
git add -A
git commit -m "Add validations to the Post model"
```

Couvrons ces validations avec des tests. Allez dans le fichier de test du modèle `Post` :

```
spec/models/post_spec.rb
```

Puis ajoutez :

```rb
context 'Validations' do
  let(:post) { build(:post) }

  it 'creates succesfully' do 
    expect(post).to be_valid
  end

  it 'is not valid without a category' do 
    post.category_id = nil
    expect(post).not_to be_valid
  end

  it 'is not valid without a title' do 
    post.title = nil
    expect(post).not_to be_valid
  end

  it 'is not valid  without a user_id' do
    post.user_id = nil
    expect(post).not_to be_valid
  end

  it 'is not valid  with a title, shorter than 5 characters' do 
    post.title = 'a' * 4
    expect(post).not_to be_valid
  end

  it 'is not valid  with a title, longer than 255 characters' do 
    post.title = 'a' * 260
    expect(post).not_to be_valid
  end

  it 'is not valid without a content' do 
    post.content = nil
    expect(post).not_to be_valid
  end

  it 'is not valid  with a content, shorter than 20 characters' do 
    post.content = 'a' * 10
    expect(post).not_to be_valid
  end

  it 'is not valid  with a content, longer than 1000 characters' do 
    post.content = 'a' * 1050
    expect(post).not_to be_valid
  end
end 
```

Commettez les changements :

```bash
git add -A
git commit -m "Add specs for the Post model's validations"
```

Fusionnez la branche `specific_branches` avec `master` :

```bash
git checkout -b master
git merge specific_branches
git branch -D specific_branches
```

### Messagerie instantanée

Les utilisateurs peuvent publier des articles et lire les articles d'autres utilisateurs, mais ils n'ont aucune possibilité de communiquer entre eux. Nous pourrions créer un système de boîte mail simple, qui serait beaucoup plus facile et rapide à développer. Mais c'est une façon très ancienne de communiquer avec quelqu'un. La communication en temps réel est beaucoup plus excitante à développer et confortable à utiliser.

Heureusement, Rails dispose d'[Action Cable](http://edgeguides.rubyonrails.org/action_cable_overview.html) qui rend l'implémentation de fonctionnalités en temps réel relativement facile. Le concept central derrière Action Cable est qu'il utilise un [protocole WebSockets](https://fr.wikipedia.org/wiki/WebSocket) au lieu du [HTTP](https://fr.wikipedia.org/wiki/Hypertext_Transfer_Protocol). Et le concept central des WebSockets est qu'il établit une connexion client-serveur et la maintient ouverte. Cela signifie qu'aucun rechargement de page n'est requis pour envoyer et recevoir des données supplémentaires.

#### Conversation privée

L'objectif de cette section est de créer une fonctionnalité opérationnelle qui permettrait d'avoir une conversation privée entre deux utilisateurs.

Basculez vers une nouvelle branche :

```bash
git checkout -B private_conversation
```

**Espaces de noms (Namespacing) des modèles**

Commencez par définir les modèles nécessaires. Nous aurons besoin de deux modèles différents pour l'instant, un pour les conversations privées et un autre pour les messages privés. Nous pourrions les nommer `PrivateConversation` et `PrivateMessage`, mais vous pourriez rapidement rencontrer un petit problème. Bien que tout fonctionnerait bien, imaginez à quoi commencerait à ressembler le répertoire `models` après avoir créé de plus en plus de modèles avec des préfixes de noms similaires. Le répertoire deviendrait difficilement gérable en un rien de temps.

Pour éviter une structure chaotique à l'intérieur des répertoires, nous pouvons utiliser une technique d'espace de noms (namespacing).

Voyons à quoi cela ressemblerait. Un modèle ordinaire pour une conversation privée s'appellerait `PrivateConversation` et son fichier s'appellerait `private_conversation.rb`, et serait stocké dans le répertoire `models` :

```
models/private_conversation.rb
```

Pendant ce temps, la version avec espace de noms s'appellerait `Private::Conversation`. Le fichier s'appellerait `conversation.rb` et serait situé à l'intérieur du répertoire `private` :

```
models/private/conversation.rb
```

Voyez-vous comment cela peut être utile ? Tous les fichiers avec le préfixe `private` seraient stockés à l'intérieur du répertoire `private`, au lieu de s'accumuler à l'intérieur du répertoire principal `models` et de le rendre difficile à lire.

Comme d'habitude, Rails rend le processus de développement agréable. Nous pouvons créer des modèles avec espace de noms en spécifiant un répertoire dans lequel nous voulons placer un modèle.

Pour créer le modèle `Private::Conversation` avec espace de noms, lancez la commande suivante :

```
rails g model private/conversation
```

Générez également le modèle `Private::Message` :

```
rails g model private/message
```

Si vous regardez le répertoire `models`, vous verrez un fichier `private.rb`. Ceci est nécessaire pour ajouter un préfixe aux noms des tables de la base de données, afin que les modèles puissent être reconnus. Personnellement, je n'aime pas garder ces fichiers à l'intérieur du répertoire `models`, je préfère spécifier le nom d'une table à l'intérieur d'un modèle lui-même. Pour spécifier le nom d'une table à l'intérieur d'un modèle, vous devez utiliser `self.table_name =` et fournir le nom d'une table sous forme de chaîne de caractères. Si vous choisissez de spécifier les noms des tables de base de données de cette façon, comme je le fais, alors les modèles devraient ressembler à ceci :

```rb
class Private::Conversation < ApplicationRecord
  self.table_name = 'private_conversations'
end
```

```rb
class Private::Message < ApplicationRecord
  self.table_name = 'private_messages'
end
```

Le fichier `private.rb`, à l'intérieur du répertoire `models`, n'est plus nécessaire, vous pouvez le supprimer.

Un utilisateur pourra avoir de nombreuses conversations privées et les conversations auront de nombreux messages. Définissez ces associations à l'intérieur des modèles :

```rb
...
has_many :messages, 
         class_name: "Private::Message", 
         foreign_key: :conversation_id
belongs_to :sender, foreign_key: :sender_id, class_name: 'User'
belongs_to :recipient, foreign_key: :recipient_id, class_name: 'User'
...
```

```rb
...
  belongs_to :user
  belongs_to :conversation, 
             class_name: 'Private::Conversation',
             foreign_key: :conversation_id
...
```

```rb
...
has_many :private_messages, class_name: 'Private::Message'
has_many  :private_conversations, 
          foreign_key: :sender_id, 
          class_name: 'Private::Conversation'
...
```

Ici, la méthode `class_name` est utilisée pour définir le nom d'un modèle associé. Cela permet d'utiliser des noms personnalisés pour nos associations et de s'assurer que les modèles avec espace de noms sont reconnus. Un autre cas d'utilisation de la méthode `class_name` serait de créer une relation avec lui-même, ce qui est utile lorsque vous voulez différencier les données d'un même modèle en créant des sortes de hiérarchies ou des structures similaires.

Le `foreign_key` est utilisé pour spécifier le nom de la colonne d'association dans une table de base de données. Une colonne de données dans une table n'est créée que du côté de l'association `belongs_to`, mais pour rendre la colonne reconnaissable, nous devons définir le `foreign_key` avec les mêmes valeurs sur les deux modèles.

Les conversations privées vont se dérouler entre deux utilisateurs, ici ces deux utilisateurs sont `sender` (expéditeur) et `recipient` (destinataire). Nous aurions pu les nommer `user1` et `user2`. Mais il est pratique de savoir qui a initié une conversation, donc le `sender` ici est le créateur d'une conversation.

Définissez les tables de données à l'intérieur des fichiers de migration :

```rb
class CreatePrivateConversations < ActiveRecord::Migration[5.1]
  def change
    create_table :private_conversations do |t|
      t.integer :recipient_id
      t.integer :sender_id

      t.timestamps
    end
    add_index :private_conversations, :recipient_id
    add_index :private_conversations, :sender_id
    add_index :private_conversations, [:recipient_id, :sender_id], unique: true
  end
end
```

La table `private_conversations` va stocker les ids des utilisateurs, ce qui est nécessaire pour que les associations `belongs_to` et `has_many` fonctionnent et bien sûr pour créer une conversation entre deux utilisateurs.

```rb
class CreatePrivateMessages < ActiveRecord::Migration[5.1]
  def change
    create_table :private_messages do |t|
      t.text :body
      t.references :user, foreign_key: true
      t.belongs_to :conversation, index: true
      t.boolean :seen, default: false
      
      t.timestamps
    end
  end
end
```

À l'intérieur de la colonne de données `body`, le contenu d'un message va être stocké. Au lieu d'ajouter des index et des colonnes d'id pour faire fonctionner les associations entre deux modèles, nous avons utilisé ici la méthode `references`, qui a simplifié l'implémentation.

Lancez les fichiers de migration pour créer les tables à l'intérieur de la base de données de développement :

```
rails db:migrate
```

Commettez les changements :

```bash
git add -A
git commit -m "Create Private::Conversation and Private::Message models
- Define associations between User, Private::Conversation
  and Private::Message models
- Define private_conversations and private_messages tables"
```

**Une fenêtre de conversation privée non temps réel**

Nous avons un endroit pour stocker les données des conversations privées, mais c'est à peu près tout. Par où devrions-nous commencer maintenant ? Comme mentionné dans les sections précédentes, personnellement, j'aime créer le côté visuel de base d'une fonctionnalité, puis écrire de la logique pour la rendre fonctionnelle. J'aime cette approche car lorsque j'ai un élément visuel que je veux rendre fonctionnel, ce que je veux accomplir est plus évident. Une fois que vous avez une interface utilisateur, il est plus facile de commencer à décomposer un problème en étapes plus petites, car vous savez ce qui doit se passer après un certain événement. Il est plus difficile de programmer quelque chose qui n'existe pas encore.

Pour commencer à construire l'interface utilisateur des conversations privées, créez un contrôleur `Private::Conversations`. Une fois que je mets quelque chose dans un espace de noms dans l'application, j'aime rester cohérent et mettre également dans un espace de noms toutes ses autres parties liées. Cela permet de comprendre et de naviguer dans le code source de manière plus intuitive.

```
rails g controller private/conversations
```

Le générateur Rails est plutôt génial. Il a créé un modèle avec espace de noms et des vues avec espace de noms, tout est prêt pour le développement.

**Créer une nouvelle conversation**

Nous avons besoin d'un moyen d'initier une nouvelle conversation. Dans le cas de notre application, il est logique que vous vouliez contacter une personne qui a des intérêts similaires aux vôtres. Un endroit pratique pour cette fonctionnalité se trouve à l'intérieur de la page d'un article individuel.

À l'intérieur du template `posts/show.html.erb`, créez un formulaire pour initier une nouvelle conversation. Sous la ligne `<p><%= @post.content %></p>`, ajoutez :

```html
...
<%= render contact_user_partial_path %>
...
```

Définissez la méthode helper à l'intérieur de `posts_helper.rb` :

```rb
...
def contact_user_partial_path
  if user_signed_in?
    @post.user.id != current_user.id ? 'posts/show/contact_user' : 'shared/empty_partial'
  else 
    'posts/show/login_required'
  end
end
...
```

Ajoutez des tests pour la méthode helper :

```rb
...
context '#contact_user_partial_path' do
  before(:each) do
    @current_user = create(:user, id: 1)
    helper.stub(:current_user).and_return(@current_user)
  end

  it "returns a contact_user partial's path" do
    helper.stub(:user_signed_in?).and_return(true)
    assign(:post, create(:post, user_id: create(:user, id: 2).id))
    expect(helper.contact_user_partial_path).to(
      eq 'posts/show/contact_user' 
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:user_signed_in?).and_return(true)
    assign(:post, create(:post, user_id: @current_user.id))

    expect(helper.contact_user_partial_path).to(
      eq 'shared/empty_partial'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:user_signed_in?).and_return(false)
    expect(helper.contact_user_partial_path).to(
      eq 'posts/show/login_required'
    )
  end
end
...
```

Créez un répertoire `show` et les fichiers partiels correspondants :

```html
<div class="contact-user">
  <%= render leave_message_partial_path %>
</div><!-- contact-user -->
```

```html
<div class="text-center">
  Pour contacter l'utilisateur, vous devez vous <%= link_to 'Connecter', login_path %> 
</div>
```

Définissez la méthode helper `leave_message_partial_path` à l'intérieur de `posts_helper.rb` :

```rb
...
def leave_message_partial_path
  if @message_has_been_sent
    'posts/show/contact_user/already_in_touch'
  else
    'posts/show/contact_user/message_form'
  end
end
...
```

Ajoutez des tests pour la méthode :

```rb
...
context '#leave_message_partial_path' do
  it "returns an already_in_touch partial's path" do
    assign('message_has_been_sent', true)
    expect(helper.leave_message_partial_path).to(
      eq 'posts/show/contact_user/already_in_touch'
    )
  end

  it "returns an already_in_touch partial's path" do
    assign('message_has_been_sent', false)
    expect(helper.leave_message_partial_path).to(
      eq 'posts/show/contact_user/message_form'
    )
  end
end
...
```

Nous définirons la variable d'instance `@message_has_been_sent` à l'intérieur du `PostsController` dans un instant, elle déterminera si un message initial a déjà été envoyé à un utilisateur ou non.

Créez les fichiers partiels, correspondant à la méthode helper `leave_message_partial_path`, à l'intérieur d'un nouveau répertoire `contact_user` :

```html
<div class="contacted-user">
  Vous êtes déjà en contact avec cet utilisateur
</div>
```

```html
<%= form_tag({controller: "private/conversations", action: "create"},
              method: "post",
              remote: true) do %>
  <%= hidden_field_tag(:post_id, @post.id)  %>
  <%= text_area_tag(:message_body,
                    nil,
                    rows: 3,
                    class: 'form-control', 
                    placeholder: 'Envoyer un message à l\'utilisateur') %>
  <%= submit_tag('Envoyer un message', class: 'btn send-message-to-user') %>
<% end %>
```

Maintenant, configurez l'action `show` du `PostsController`. À l'intérieur de l'action, ajoutez :

```rb
...
if user_signed_in?
  @message_has_been_sent = conversation_exist?
end
...
```

À l'intérieur de la portée `private` du contrôleur, définissez la méthode `conversation_exist?` :

```rb
...
def conversation_exist?
  Private::Conversation.between_users(current_user.id, @post.user.id).present?
end
...
```

La méthode `between_users` interroge les conversations privées entre deux utilisateurs. Définissez-la comme un scope à l'intérieur du modèle `Private::Conversation` :

```rb
...
scope :between_users, -> (user1_id, user2_id) do
  where(sender_id: user1_id, recipient_id: user2_id).or(
    where(sender_id: user2_id, recipient_id: user1_id)
  )
end
...
```

Nous devons tester si le scope fonctionne. Avant d'écrire les tests, définissez une factory `private_conversation`, car nous aurons besoin de données d'exemple à l'intérieur de la base de données de test.

```rb
FactoryGirl.define do
  factory :private_conversation, class: 'Private::Conversation' do
    association :recipient, factory: :user
    association :sender, factory: :user

    factory :private_conversation_with_messages do
      transient do
        messages_count 1
      end

      after(:create) do |private_conversation, evaluator|
        create_list(:private_message, evaluator.messages_count, 
                     conversation: private_conversation)
      end
    end
  end
end
```

Nous voyons ici une factory imbriquée, ce qui permet de créer une factory avec la configuration de son parent puis de la modifier. De plus, comme nous allons créer des messages avec la factory `private_conversation_with_messages`, nous devons également définir la factory `private_message` :

```rb
FactoryGirl.define do 
  factory :private_message, class: 'Private::Message' do
    body 'a' * 20
    association :conversation, factory: :private_conversation
    user
  end
end
```

Maintenant, nous avons tout ce qu'il faut pour tester le scope `between_users` avec des tests :

```rb
...
context 'Scopes' do
  it 'gets a conversation between users' do
    user1 = create(:user)
    user2 = create(:user)
    create(:private_conversation, recipient_id: user1.id, sender_id: user2.id)
    conversation = Private::Conversation.between_users(user1.id, user2.id)
    expect(conversation.count).to eq 1
  end
end
...
```

Définissez l'action `create` pour le contrôleur `Private::Conversations` :

```rb
...
def create
  recipient_id = Post.find(params[:post_id]).user.id
  conversation = Private::Conversation.new(sender_id: current_user.id, 
                                           recipient_id: recipient_id)
  if conversation.save
    Private::Message.create(user_id: recipient_id, 
                            conversation_id: conversation.id, 
                            body: params[:message_body])
    respond_to do |format|
      format.js {render partial: 'posts/show/contact_user/message_form/success'}
    end
  else
    respond_to do |format|
      format.js {render partial: 'posts/show/contact_user/message_form/fail'}
    end
  end
end
...
```

Ici, nous créons une conversation entre l'auteur d'un article et l'utilisateur actuel. Si tout se passe bien, l'application créera un message, écrit par l'utilisateur actuel, et donnera un retour en rendant un partiel JavaScript correspondant.

Créez ces partiels :

```js
$('.contact-user').replaceWith('\
    <div class="contact-user">\
        <div class="contacted-user">Le message a été envoyé</div>\
    </div>');
```

```js
$('.contact-user').replaceWith('<div>Le message n\'a pas été envoyé</div>');
```

Créez des routes pour les contrôleurs `Private::Conversations` et `Private::Messages` :

```rb
...
namespace :private do 
  resources :conversations, only: [:create] do
    member do
      post :close
    end
  end
  resources :messages, only: [:index, :create]
end
...
```

Pour l'instant, nous n'aurons besoin que de quelques actions, c'est là que la méthode `only` est pratique. La méthode `namespace` permet de créer facilement des routes pour les contrôleurs avec espace de noms.

Testez les performances globales du formulaire `.contact-user` avec des tests de fonctionnalité :

```rb
require "rails_helper"

RSpec.feature "Contact user", :type => :feature do
	let(:user) { create(:user) }
	let(:category) { create(:category, name: 'Arts', branch: 'hobby') }
	let(:post) { create(:post, category_id: category.id) }

  context 'logged in user' do
    before(:each) do
      sign_in user 
    end

    scenario "successfully sends a message to a post's author", js: true do
      visit post_path(post)
      expect(page).to have_selector('.contact-user form')

      fill_in('message_body', with: 'a' * 20)
      find('form .send-message-to-user').trigger('click')

      expect(page).not_to have_selector('.contact-user form')
      expect(page).to have_selector('.contacted-user', 
                                      text: 'Le message a été envoyé')
    end

    scenario 'sees an already contacted message' do
      create(:private_conversation_with_messages, 
              recipient_id: post.user.id, 
              sender_id: user.id)
      visit post_path(post)
      expect(page).to have_selector(
        '.contact-user .contacted-user', 
        text: 'Vous êtes déjà en contact avec cet utilisateur')
    end
  end

  context 'non-logged in user' do
    scenario 'sees a login required message to contact a user' do
      visit post_path(post)
      expect(page).to have_selector('div', text: 'Pour contacter l\'utilisateur, vous devez vous')
    end
  end
end
```

Commettez les changements :

```bash
git add -A
git commit -m "Inside a post add a form to contact a user
- Define a contact_user_partial_path helper method in PostsHelper. 
  Add specs for the method
- Create _contact_user.html.erb and _login_required.html.erb partials
- Define a leave_message_partial_path helper method in PostsHelper.
  Add specs for the method
- Create _already_in_touch.html.erb and _message_form.html.erb 
  partial files
- Define a @message_has_been_sent in PostsController's show action
- Define a between_users scope inside the Private::Conversation model
  Add specs for the scope
- Define private_conversation and private_message factories
- Define routes for Private::Conversations and Private::Messages
- Define a create action inside the Private::Conversations
- Create _success.js and _fail.js partials
- Add feature specs to test the overall .contact-user form"
```

Changez un peu le style du formulaire en ajoutant du CSS au fichier `branch_page.scss` :

```scss
...
.send-message-to-user {
  background-color: $navbarColor;
  padding: 10px;
  color: white;
  border-radius: 10px;
  margin-top: 10px;
  &:hover {
    background-color: black;
    color: white;
  }
}

.contact-user {
  text-align: center;
}

.contacted-user {
  display: inline-block;
  border-radius: 10px;
  padding: 10px;
  background-color: $navbarColor;
  color: white;
}
...
```

Lorsque vous visitez un article individuel, le formulaire devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-95.png)

Lorsque vous envoyez un message à l'auteur d'un article, le formulaire disparaît :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-96.png)

Voici à quoi cela ressemble lorsque vous êtes déjà en contact avec un utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-97.png)

Commettez les changements :

```bash
git add -A
git commit -m "Add CSS to style the .contact-user form"
```

**Rendre une fenêtre de conversation**

Nous avons envoyé un message et créé une nouvelle conversation. C'est notre seul pouvoir pour l'instant, nous ne pouvons rien faire d'autre. Quel pouvoir inutile jusqu'à présent. Nous avons besoin d'une fenêtre de conversation pour lire et écrire des messages.

Stockez les ids des conversations ouvertes dans la session. Cela permet de garder les conversations ouvertes dans l'application jusqu'à ce qu'un utilisateur les ferme ou détruise la session.

À l'intérieur de l'action `create` du `Private::ConversationsController`, appelez une méthode `add_to_conversations unless already_added?` si une conversation est enregistrée avec succès. Définissez ensuite la méthode dans la portée `private` :

```rb
...
private

def add_to_conversations
  session[:private_conversations] ||= []
  session[:private_conversations] << @conversation.id
end
```

Cela stockera l'id de la conversation dans la session. Et la méthode privée `already_added?` va s'assurer que l'id de la conversation n'est pas déjà ajouté dans la session.

```rb
def already_added?
  session[:private_conversations].include?(@conversation.id)
end
```

Et enfin, nous aurons besoin d'un accès à la conversation à l'intérieur des vues, donc convertissez la variable `conversation` en une variable d'instance.

Nous pouvons maintenant commencer à construire un template pour la fenêtre de conversation. Créez un fichier partiel pour la fenêtre :

```html
<% @recipient = private_conv_recipient(conversation) %>
<% @is_messenger = false %>
<li class="conversation-window" 
    id="pc<%= conversation.id %>" 
    data-pconversation-user-name="<%= @recipient.name %>" 
    data-turbolinks-permanent>
  <div class="panel panel-default" data-pconversation-id="<%= conversation.id %>">
    <%= render 'private/conversations/conversation/heading', 
                conversation: conversation %>

    <!-- Contenu de la fenêtre de conversation -->
    <div class="panel-body">
      <%= render 'private/conversations/conversation/messages_list', 
                  conversation: conversation %>
      <%= render 'private/conversations/conversation/new_message_form', 
                  conversation: conversation,
                  user: user %>
    </div><!-- panel-body -->
  </div>
</li><!-- conversation-window -->
```

Ici, nous obtenons le destinataire de la conversation avec la méthode `private_conv_recipient`. Définissez la méthode helper à l'intérieur de `Private::ConversationsHelper` :

```rb
...
# obtenir l'autre utilisateur de la conversation
def private_conv_recipient(conversation)
  conversation.opposed_user(current_user)
end
...
```

La méthode `opposed_user` est utilisée. Allez dans le modèle `Private::Conversation` et définissez la méthode :

```rb
...
def opposed_user(user)
  user == recipient ? sender : recipient
end
...
```

Cela renverra l'utilisateur opposé d'une conversation privée. Assurez-vous que la méthode fonctionne correctement en la couvrant par des tests :

```rb
...
context 'Methods' do
  it 'gets an opposed user of the conversation' do
    user1 = create(:user)
    user2 = create(:user)
    conversation = create(:private_conversation,
                           recipient_id: user1.id,
                           sender_id: user2.id)
    opposed_user = conversation.opposed_user(user1)
    expect(opposed_user).to eq user2
  end
end
...
```

Ensuite, créez les fichiers partiels manquants pour le fichier `_conversation.html.erb` :

```html
<div class="panel-heading conversation-heading">
  <span class="contact-name-notif"><%= @recipient.name %></span>  
</div> <!-- conversation-heading -->

<!-- Bouton de fermeture de la conversation -->
<%= link_to "X", 
            close_private_conversation_path(conversation), 
            class: 'close-conversation', 
            title: 'Fermer', 
            remote: true, 
            method: :post %>
```

```html
<div class="messages-list">
  <%= render load_private_messages(conversation), conversation: conversation %>
  <div class="loading-more-messages">
    <i class="fa fa-spinner" aria-hidden="true"></i>
  </div>
  <!-- messages -->
  <ul>
  </ul>
</div>
```

À l'intérieur de `Private::ConversationsHelper`, définissez la méthode helper `load_private_messages` :

```rb
...
# si la conversation a des messages non affichés, affiche un bouton pour les obtenir
def load_private_messages(conversation)
  if conversation.messages.count > 0 
    'private/conversations/conversation/messages_list/link_to_previous_messages'
  else
    'shared/empty_partial'
  end 
end
...
```

Cela ajoutera un lien pour charger les messages précédents. Créez un fichier partiel correspondant à l'intérieur d'un nouveau répertoire `messages_list` :

```html
<%= link_to "Charger les messages", 
            private_messages_path(:conversation_id => conversation.id, 
                                  :messages_to_display_offset => @messages_to_display_offset,
                                  :is_messenger => @is_messenger),
            class: 'load-more-messages', 
            remote: true %>
```

N'oubliez pas de vous assurer que tout va bien avec la méthode et d'écrire des tests pour celle-ci :

```rb
...
context '#load_private_messages' do
  let(:conversation) { create(:private_conversation) }

  it "returns load_messages partial's path" do
    create(:private_message, conversation_id: conversation.id)
    expect(helper.load_private_messages(conversation)).to eq (
      'private/conversations/conversation/messages_list/link_to_previous_messages'
    )
  end

  it "returns empty partial's path" do
    expect(helper.load_private_messages(conversation)).to eq (
      'shared/empty_partial'
    )
  end
end
...
```

Comme les fenêtres de conversations vont être rendues dans toute l'application, cela signifie que nous aurons besoin d'un accès aux méthodes helper de `Private::ConversationsHelper`. Pour avoir accès à toutes ces méthodes dans toute l'application, à l'intérieur de `ApplicationHelper`, ajoutez :

```
include Private::ConversationsHelper
```

Ensuite, créez le dernier fichier partiel manquant pour le formulaire de nouveau message de la conversation :

```html
<form class="send-private-message">
  <input name="conversation_id" type="hidden" value="<%= conversation.id %>">
  <input name="user_id" type="hidden" value="<%= user.id %>">
  <textarea name="body" rows="3" class="form-control" placeholder="Tapez un message..."></textarea>
  <input type="submit" class="btn btn-success send-message">
</form>
```

Nous rendrons ce formulaire fonctionnel un peu plus tard.

Maintenant, créons une fonctionnalité pour que, après qu'un utilisateur a envoyé un message via un article individuel, la fenêtre de conversation soit rendue sur l'application.

À l'intérieur du fichier `_success.js.erb` :

```
posts/show/contact_user/message_form/_success.js.erb
```

ajoutez :

```
<%= render 'private/conversations/open' %>
```

Le but de ce fichier partiel est d'ajouter une fenêtre de conversation à l'application. Définissez le fichier partiel :

```js
var conversation = $('body').find("[data-pconversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
var chat_windows_count = $('.conversation-window').length + 1;

if (conversation.length !== 1) {
  $('body').append("<%= j(render 'private/conversations/conversation',\
                                  conversation: @conversation,\
                                  user: current_user) %>");
  conversation = $('body').find("[data-conversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
}

// Basculer la fenêtre de conversation après sa création
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   .conversation-heading').click();
// marquer comme vu en cliquant dessus
setTimeout(function(){ 
  $('.conversation-window:nth-of-type(' + chat_windows_count + ')').click();
 }, 1000);
// focus sur le textarea
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   form\
   textarea').focus();

// repositionne toutes les fenêtres de conversation
positionChatWindows();
```

Ce fichier partiel de rappel va être réutilisé dans plusieurs scénarios. Pour éviter de rendre la même fenêtre plusieurs fois, avant de rendre une fenêtre, nous vérifions si elle existe déjà sur l'application. Ensuite, nous agrandissons la fenêtre et mettons automatiquement le focus sur le formulaire de message. Au bas du fichier, la fonction `positionChatWindows()` est appelée pour s'assurer que toutes les fenêtres de conversations sont bien positionnées. Si nous ne les positionnions pas, elles seraient simplement rendues au même endroit, ce qui serait bien sûr inutilisable.

Maintenant, dans le répertoire `assets`, créez un fichier qui s'occupera de la visibilité et du positionnement des fenêtres de conversations :

```js
$(document).on('turbolinks:load', function() { 
    chat_windows_count = $('.conversation-window').length;
    // si la dernière fenêtre de chat visible n'est pas définie et que des fenêtres de conversation existent
    // définir la variable last_visible_chat_window
    if (gon.last_visible_chat_window == null && chat_windows_count > 0) {
        gon.last_visible_chat_window = chat_windows_count;
    }
    // si gon.hidden_chats n'existe pas, définir sa valeur
    if (gon.hidden_chats == null) {
        gon.hidden_chats = 0;
    }
    window.addEventListener('resize', hideShowChatWindow);

    positionChatWindows();
    hideShowChatWindow();
});

function positionChatWindows() {
    chat_windows_count = $('.conversation-window').length;
    // si une nouvelle fenêtre de conversation a été ajoutée, 
    // la définir comme la dernière fenêtre de conversation visible
    // afin que la fonction hideShowChatWindow puisse la cacher ou l'afficher, 
    // selon la largeur du viewport
    if (gon.hidden_chats + gon.last_visible_chat_window !== chat_windows_count) {
        if (gon.hidden_chats == 0) {
            gon.last_visible_chat_window = chat_windows_count;
        }
    }

    // lorsqu'une nouvelle fenêtre de chat est ajoutée, la positionner le plus à gauche de la liste
    for (i = 0; i < chat_windows_count; i++ ) {
        var right_position = i * 410;
        var chat_window = i + 1;
        $('.conversation-window:nth-of-type(' + chat_window + ')')
            .css('right', '' + right_position + 'px');
    }
}

// Cache la dernière fenêtre de conversation chaque fois qu'elle est proche du côté gauche du viewport
function hideShowChatWindow() {
    // s'il n'y a pas de fenêtres de conversation, arrêter la fonction
    if ($('.conversation-window').length < 1) {
        return;
    }
    // obtenir un décalage de la fenêtre de conversation la plus à gauche
    var offset = $('.conversation-window:nth-of-type(' + gon.last_visible_chat_window + ')').offset();
    // si le décalage gauche de la fenêtre de conversation est inférieur à 50, 
    // cacher cette fenêtre de conversation
    if (offset.left < 50 && gon.last_visible_chat_window !== 1) {
        $('.conversation-window:nth-of-type(' + gon.last_visible_chat_window + ')')
            .css('display', 'none');
        gon.hidden_chats++;
        gon.last_visible_chat_window--;
    }
    // si le décalage de la fenêtre de conversation la plus à gauche est supérieur à 550 
    // et qu'il y a une conversation cachée, afficher la conversation cachée
    if (offset.left > 550 && gon.hidden_chats !== 0) {
        gon.hidden_chats--;
        gon.last_visible_chat_window++;
        $('.conversation-window:nth-of-type(' + gon.last_visible_chat_window + ')')
            .css('display', 'initial');
    }
}
```

Au lieu de créer nos propres fonctions pour définir et obtenir des cookies ou une méthode similaire pour gérer les données entre JavaScript, nous pouvons utiliser la gem [gon](https://github.com/gazay/gon). Une utilisation originale de cette gem est d'envoyer des données du côté serveur vers JavaScript. Mais je la trouve également utile pour garder une trace des variables JavaScript dans toute l'application. Installez et configurez la gem en lisant les instructions.
Nous suivons la largeur du viewport avec un écouteur d'événements. Lorsqu'une conversation s'approche du côté gauche du viewport, elle est masquée. Une fois qu'il y a assez d'espace libre pour une fenêtre de conversation masquée, l'application l'affiche à nouveau.

Lors de la visite d'une page, nous appelons les fonctions de positionnement et de visibilité pour nous assurer que toutes les fenêtres de conversation sont aux bonnes positions.

Nous utilisons le composant panel de Bootstrap pour agrandir et réduire facilement les fenêtres de conversation. Par défaut, elles seront réduites et pas du tout interactives. Pour les rendre basculables, créez un nouveau fichier `toggle_window.js` dans le répertoire `javascripts` :

```js
$(document).on('turbolinks:load', function() { 

    // quand on clique sur l'en-tête de la conversation, on bascule l'affichage
    $('body').on('click', 
    	         '.conversation-heading, .conversation-heading-full', 
    	         function(e) {
        e.preventDefault();
        var panel = $(this).parent();
        var panel_body = panel.find('.panel-body');
        var messages_list = panel.find('.messages-list');

        panel_body.toggle(100, function() {
        }); 
    });
});
```

Créez un nouveau fichier `conversation_window.scss` :

```
assets/stylesheets/partials/conversation_window.scss
```

Et ajoutez le CSS pour styliser les fenêtres de conversation :

```scss
textarea {
  resize: none;
}

.panel {
  margin: 0;
  border: none !important;
}

.panel-heading {
  border-radius: 0;
}

.panel-body {
  position: relative;
  display: none;
  padding: 0 0 5px 0;
}

.conversation-window, .new_chat_window {
  min-width: 400px;
  max-width: 400px;
  position: fixed;
  bottom: 0;
  right: 0;
  list-style-type: none;
}

.conversation-heading, .conversation-heading-full, .new_chat_window {
  background-color: $navbarColor !important;
  color: white !important;
  height: 40px;
  border: none !important;
  a {
    color: white !important;
  }

}

.conversation-heading, .conversation-heading-full {
  padding: 0 0 0 15px;
  width: 360px;
  display: inline-block;
  vertical-align: middle;
  line-height: 40px;
}

.close-conversation, .add-people-to-chat, .add-user-to-contacts, .contact-request-sent {
  color: white;
  float: right;
  height: 40px;
  width: 40px;
  font-size: 20px;
  font-size: 2.0rem;
  border: none;
  background-color: $navbarColor;
}

.close-conversation, .add-user-to-contacts {
  text-align: center;
  vertical-align: middle;
  line-height: 40px;
  font-weight: bold;
}

.close-conversation {
  &:hover {
    border: none;
    background-color: white;
    color: $navbarColor !important;
  }
  &:visited, &:focus {
    color: white;
  }
}

.form-control[disabled] {
  background-color: $navbarColor;
}

.send-private-message, .send-group-message {
  textarea {
    border-radius: 0;
    border: none;
    border-top: 1px solid rgba(0, 0, 0, 0.2);
  }
}

.loading_svg {
  display: none;
}

.loading_svg {
  text-align: center;
}

.messages-list {
  z-index: 1;
  min-height: 300px;
  max-height: 300px;
  overflow-y: auto;
  overflow-x: hidden;
  ul {
    padding: 0;
  }
}

.message-received, .message-sent {
  max-width: 300px;
  word-wrap: break-word;
  z-index: 1;
}

.message-sent {
  position: relative;
  background-color: white;
  border: 1px solid rgba(0, 0, 0, 0.5);
  border-radius: 5px;
  margin: 5px 5px 5px 50px;
  padding: 10px;
  float: right;
}

.message-received {
  background-color: $backgroundColor;
  border-color: #EEEEEE;
  border-radius: 5px;
  margin: 5px 50px 5px 5px;
  padding: 10px;
  float: left;
}

.messages-date {
  width: 100%; 
  text-align: center; 
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  line-height: 1px; 
  line-height: 0.1rem;
  margin: 20px 0 20px;
  span {
    background: #fff; 
    padding: 0 10px; 
  }
  
}

.load-more-messages {
  display: none;
}

.loading-more-messages {
  font-size: 20px;
  font-size: 2.0rem;
  padding: 10px 0;
  text-align: center;
}

.send-message {
  display: none;
}
```

Vous avez peut-être remarqué qu'il y a des classes qui n'ont pas encore été définies dans un fichier HTML. C'est parce que les futurs fichiers que nous créerons dans le répertoire `views` partageront le CSS avec des éléments HTML déjà existants. Au lieu de faire des allers-retours incessants vers les fichiers CSS après avoir ajouté chaque petit élément HTML, j'ai inclus dès maintenant certaines classes définies dans les futurs éléments HTML. N'oubliez pas que vous pouvez toujours consulter les feuilles de style pour analyser le fonctionnement d'un style particulier.

Précédemment, nous avons enregistré l'ID d'une conversation nouvellement créée dans la session. Il est temps d'en profiter et de garder la fenêtre de conversation ouverte jusqu'à ce qu'un utilisateur la ferme ou détruise la session. Dans l'`ApplicationController`, définissez un filtre :

```
before_action :opened_conversations_windows
```

puis définissez la méthode `opened_conversations_windows` :

```rb
...
def opened_conversations_windows
  if user_signed_in?
    # conversations ouvertes
    session[:private_conversations] ||= []
    @private_conversations_windows = Private::Conversation.includes(:recipient, :messages)
                                      .find(session[:private_conversations])
  else
    @private_conversations_windows = []
  end
end
...
```

La méthode `[includes](https://apidock.com/rails/ActiveRecord/QueryMethods/includes)` est utilisée pour inclure les données des tables de base de données associées. Dans un futur proche, nous chargerons les messages d'une conversation. Si nous n'utilisions pas la méthode `includes`, nous n'aurions pas chargé les enregistrements de messages d'une conversation avec cette requête. Cela conduirait à un [problème de requête N + 1](https://secure.phabricator.com/book/phabcontrib/article/n_plus_one/). Si nous ne chargions pas les messages avec la requête, une requête supplémentaire serait déclenchée pour chaque message. Cela impacterait considérablement les performances de l'application. Maintenant, au lieu de 100 requêtes pour 100 messages, nous n'avons qu'une seule requête initiale pour n'importe quel nombre de messages.

Dans le fichier `application.html.erb`, juste en dessous de la méthode `yield`, ajoutez :

```html
...
<%= render 'layouts/application/private_conversations_windows' %>
...
```

Créez un nouveau répertoire `application` et à l'intérieur, créez le fichier partiel `_private_conversations_windows.html.erb` :

```html
<% private_conversations_windows.each do |conversation| %>
  <%= render partial: "private/conversations/conversation",
             locals: { conversation: conversation, 
                       user: current_user } %>
<% end %>
```

Désormais, lorsque nous naviguons dans l'application, nous voyons les conversations ouvertes en permanence, quelle que soit la page où nous nous trouvons.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-98.png)

Validez les modifications (commit) :

```bash
git add -A
git commit -m "Afficher une fenêtre de conversation privée sur l'application
- Ajouter les conversations ouvertes à la session
- Créer un fichier _conversation.html.erb dans private/conversations
- Définir une méthode helper private_conv_recipient dans private/conversations_helper.rb
- Définir une méthode opposed_user dans le modèle Private::Conversation et ajouter des specs
- Créer les fichiers _heading.html.erb et _messages_list.html.erb dans private/conversations/conversation
- Définir load_private_messages dans private/conversations_helper.rb et ajouter des specs
- Créer un fichier _new_message_form.html.erb dans private/conversations/conversation
- Créer un fichier _open.js.erb dans private/conversations
- Créer un fichier position_and_visibility.js dans assets/javascripts/conversations
- Créer un fichier conversation_window.scss dans assets/stylesheets/partials
- Définir une méthode helper opened_conversations_windows dans ApplicationController
- Créer un fichier _private_conversations_windows.html.erb dans layouts/application"
```

**Fermer une conversation**

Le bouton de fermeture de la conversation n'est pas encore fonctionnel. Mais nous avons tout ce qu'il faut pour qu'il le devienne. Dans le `Private::ConversationsController`, définissez une action `close` :

```rb
...
def close
  @conversation_id = params[:id].to_i
  session[:private_conversations].delete(@conversation_id)

  respond_to do |format|
    format.js
  end
end
...
```

Lorsque le bouton de fermeture est cliqué, cette action sera appelée. L'action supprime l'ID de la conversation de la session, puis répond avec un fichier partiel JS identique au nom de l'action. Créez le fichier partiel :

```js
$('body')
    .find("[data-pconversation-id='" + "<%= @conversation_id %>" + "']")
    .parent()
    .remove();
positionChatWindows();
```

Il supprime la fenêtre de conversation du DOM et repositionne le reste des fenêtres de conversation.

Validez les modifications :

```bash
git add -A
git commit -m "Rendre le bouton de fermeture de conversation fonctionnel
- Définir une action close dans le Private::ConversationsController
- Créer un fichier close.js.erb dans private/conversations"
```

**Afficher les messages**

Actuellement, dans la liste des messages, nous voyons une icône de chargement sans aucun message. C'est parce que nous n'avons pas créé de templates pour les messages. Dans le répertoire `views/private`, créez un répertoire `messages`. À l'intérieur de ce répertoire, créez un nouveau fichier :

```html
<%= render private_message_date_check(message, previous_message),
           locals: { message: message } %>
<li title="<%= message.created_at.to_s(:time) %>">
  <div class="row">   
    <div class="<%= sent_or_received(message, user) %> <%= seen_or_unseen(message) %>">
      <%= message.body %>
    </div>
  </div>
</li>
```

La méthode helper `private_message_date_check` vérifie si ce message a été écrit le même jour qu'un message précédent. Si ce n'est pas le cas, elle affiche une ligne supplémentaire avec une nouvelle date. Définissez la méthode helper dans `Private::MessagesHelper` :

```rb
module Private::MessagesHelper 
  
  def private_message_date_check(message, previous_message)
    if defined?(previous_message) && previous_message.present? 
      # si les messages ne sont pas créés le même jour
      if previous_message.created_at.to_date != message.created_at.to_date
        @message = message
        'private/messages/message/new_date'
      else
        'shared/empty_partial'
      end 
    else
      'shared/empty_partial'
    end 
  end
end
```

Dans l'`ApplicationHelper`, incluez le `Private::MessagesHelper`, afin que nous puissions y avoir accès dans toute l'application :

```
include Private::MessagesHelper
```

Écrivez les specs pour la méthode. Créez un nouveau fichier `messages_helper_spec.rb` :

```rb
require 'rails_helper'
RSpec.describe Private::MessagesHelper, :type => :helper do
  context '#private_message_date_check' do
    let(:message) { create(:private_message) }
    let(:previous_message) { create(:private_message) }

    it "returns new_date partial's path" do
      message.update(created_at: 2.days.ago)
      expect(helper.private_message_date_check(message, previous_message)).to(
        eq 'private/messages/message/new_date'
      )
    end

    it "returns an empty partial's path" do
      expect(helper.private_message_date_check(message, previous_message)).to(
        eq 'shared/empty_partial'
      )
    end

    it "returns an empty partial's path" do
      previous_message = nil
      expect(helper.private_message_date_check(message, previous_message)).to(
        eq 'shared/empty_partial'
      )
    end
  end
end
```

Dans un nouveau répertoire `message`, créez un fichier `_new_date.html.erb` :

```html
<div class="messages-date">
  <span><%= @message.created_at.to_date %></span> 
</div>
```

Ensuite, dans le fichier `_message.html.erb`, nous avons les méthodes helper `sent_or_received` et `seen_or_unseen`. Elles renvoient différentes classes selon les cas. Définissez-les dans `Private::MessagesHelper` :

```rb
...
def sent_or_received(message, user)
  user.id == message.user_id ? 'message-sent' : 'message-received'
end

def seen_or_unseen(message)
  message.seen == false ? 'unseen' : ''
end
...
```

Écrivez les specs pour celles-ci :

```rb
...
context '#sent_or_received' do
  let(:user) { create(:user) }
  let(:message) { create(:private_message) }
  it 'returns message-sent' do
    message.update(user_id: user.id)
    expect(helper.sent_or_received(message, user)).to eq 'message-sent'
  end

  it 'returns message-received' do
    expect(helper.sent_or_received(message, user)).to eq 'message-received'
  end
end

context '#seen_or_unseen' do
  let(:message) { create(:private_message) }
  it 'returns unseen' do
    message.update(seen: false)
    expect(helper.seen_or_unseen(message)).to eq 'unseen'
  end

  it 'returns nothing' do
    message.update(seen: true)
    expect(helper.seen_or_unseen(message)).to eq ''
  end
end
...
```

Maintenant, nous avons besoin d'un composant pour charger les messages dans la liste des messages. De plus, ce composant va ajouter les messages précédents en haut de la liste lorsqu'un utilisateur fait défiler vers le haut, jusqu'à ce qu'il n'y ait plus de messages dans une conversation. Nous allons mettre en place un mécanisme de défilement infini pour les messages, similaire à celui que nous avons dans les pages de posts.

Dans le répertoire `views/private/messages`, créez un fichier `_load_more_messages.js.erb` :

```js
<% @id_type = 'pc' %>
<%= render append_previous_messages_partial_path %>
<%= render replace_link_to_private_messages_partial_path %>
```

La variable d'instance `@id_type` détermine le type de conversation. À l'avenir, nous pourrons créer non seulement des conversations privées, mais aussi des conversations de groupe. Cela conduit à des méthodes helper et des fichiers partiels communs entre les deux types.

Dans le répertoire `helpers`, créez un répertoire `shared`. Créez un fichier `messages_helper.rb` et définissez une méthode helper :

```rb
module Shared::MessagesHelper

  def append_previous_messages_partial_path
    'shared/load_more_messages/window/append_messages' 
  end

end
```

Pour l'instant, la méthode est assez rudimentaire. Elle renvoie simplement le chemin d'un partiel. Nous lui donnerons un peu plus d'intelligence plus tard, lorsque nous construirons des fonctionnalités supplémentaires pour notre système de messagerie. Pour l'instant, nous n'aurons pas accès aux méthodes helper définies dans ce fichier dans d'autres fichiers. Nous devons les inclure dans d'autres fichiers helper. Dans `Private::MessagesHelper`, incluez les méthodes de `Shared::MessagesHelper` :

```bash
require 'shared/messages_helper'
include Shared::MessagesHelper
```

Dans le répertoire `shared`, créez quelques nouveaux répertoires :

```
shared/load_more_messages/window
```

Ensuite, créez un fichier `_append_messages.js.erb` :

```js
// supprimer temporairement le lien de chargement de plus de messages
// pour qu'il ne puisse pas être cliqué si les nouveaux messages ne sont pas encore rendus
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
    .replaceWith('<span class="load-more-messages"></span>');
// rendre les messages précédents
$('#<%= @id_type %><%= @conversation.id %> .messages-list ul')
    .prepend('<%= j render "#{@type}/conversations/messages" %>');
// après l'ajout des nouveaux messages, laisser un espace en haut de la barre de défilement
$('#<%= @id_type %><%= @conversation.id %> .messages-list').scrollTop(400);
```

Ce code veille à ce que les messages précédents soient ajoutés en haut de la liste des messages. Définissez ensuite une autre méthode helper, encore une fois pas très complexe, dans `Private::MessagesHelper` :

```rb
def replace_link_to_private_messages_partial_path
  'private/messages/load_more_messages/window/replace_link_to_messages'
end
```

Créez les répertoires correspondants dans le répertoire `private/messages` et créez un fichier `_add_link_to_messages.js.erb` :

```js
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
    .replaceWith('\
        <%= j render partial: "private/conversations/conversation/messages_list/link_to_previous_messages",\
                     locals: { conversation: @conversation } %>\
    ');
```

Ce fichier va mettre à jour le lien qui charge les messages précédents. Une fois les messages précédents ajoutés, le lien est remplacé par un lien mis à jour pour charger des messages encore plus anciens.

Maintenant que nous avons tout ce système pour ajouter les messages précédents en haut de la liste, si nous essayions d'aller sur l'application et d'ouvrir une fenêtre de conversation, nous ne verrions aucun message rendu. Pourquoi ? Parce que rien ne déclenche le lien pour charger les messages précédents. Lorsque nous ouvrons une fenêtre de conversation pour la première fois, nous voulons voir les messages les plus récents. Nous pouvons programmer la fenêtre de conversation de manière à ce qu'une fois agrandie, le lien de chargement de plus de messages soit déclenché pour charger les messages les plus récents. Cela initie le premier cycle d'ajout de messages précédents et de remplacement du lien de chargement par un lien mis à jour.

Dans le fichier `toggle_window.js`, mettez à jour la fonction `toggle` pour faire exactement ce qui est décrit ci-dessus :

```js
panel_body.toggle(100, function() {
    var messages_visible = $('ul', this).has('li').length;

    // Charger les 10 premiers messages si la liste des messages est vide
    if (!messages_visible && $('.load-more-messages', this).length) {
        $('.load-more-messages', this)[0].click(); 
    }
}); 
```

Créez un gestionnaire d'événements pour que, chaque fois qu'un utilisateur fait défiler vers le haut et atteint presque le haut de la liste des messages, le lien de chargement de plus de messages soit déclenché.

```js
$(document).on('turbolinks:load ajax:complete', function() {
    var iScrollPos = 0;
    var isLoading = false;
    var currentLoadingIcon;

    $(document).ajaxComplete(function() {
        isLoading = false;
        // cacher l'icône de chargement
        if (currentLoadingIcon !== undefined) {
            currentLoadingIcon.hide();
        }
    });

    $('.messages-list', this).scroll(function () {
        var iCurScrollPos = $(this).scrollTop();
        
        if (iCurScrollPos > iScrollPos) {
            // Défilement vers le bas
        } else {
           // Défilement vers le haut
           if (iCurScrollPos < 300 && isLoading == false && $('.load-more-messages', this).length) {
                // déclencher le lien, qui charge 10 messages de plus
                $('.load-more-messages', this)[0].click();
                isLoading = true;

                // sélectionner l'icône de chargement de la fenêtre de conversation et l'afficher
                currentLoadingIcon = $('.loading-more-messages', this);
                currentLoadingIcon.show();
           }
        }
        iScrollPos = iCurScrollPos;
    });
});
```

Lorsque le lien de chargement de plus de messages sera cliqué, l'action `index` du `Private::MessagesController` sera appelée. C'est le chemin que nous avons défini pour le lien de chargement des messages précédents. Créez le contrôleur et son action `index` :

```rb
class Private::MessagesController < ActionController::Base
  include Messages

  def index
    get_messages('private', 10)
    @user = current_user
    @is_messenger = params[:is_messenger]
    respond_to do |format|
      format.js { render partial: 'private/messages/load_more_messages' }
    end
  end
end
```

Ici, nous incluons les méthodes du module `Messages`. Le module est stocké dans le répertoire `concerns`. [ActiveSupport::Concern](http://api.rubyonrails.org/classes/ActiveSupport/Concern.html) est l'un des endroits où vous pouvez stocker des modules que vous pourrez utiliser plus tard dans des classes. Dans notre cas, nous incluons des méthodes supplémentaires à notre contrôleur à partir du module. La méthode `get_messages` provient du module `Messages`. La raison pour laquelle elle est stockée dans le module est que nous utiliserons cette même méthode dans un autre contrôleur un peu plus tard. Pour éviter la duplication de code, nous rendons la méthode plus réutilisable.

J'ai vu certaines personnes se plaindre d'`ActiveSupport::Concern` et suggérer de ne pas l'utiliser du tout. Je défie ces personnes de m'affronter dans l'octogone. Je plaisante :D. C'est une application indépendante et nous pouvons créer notre application comme nous le souhaitons. Si vous n'aimez pas les `concerns`, il existe de nombreuses autres façons de créer des méthodes réutilisables.

Créez le module :

```rb
require 'active_support/concern'

module Messages
  extend ActiveSupport::Concern

  def get_messages(conversation_type, messages_amount)
    # convertir une chaîne en constante, afin que les modèles puissent être appelés dynamiquement
    model = "#{conversation_type.capitalize}::Conversation".constantize
    @conversation = model.find(params[:conversation_id])
    # obtenir les messages précédents de la conversation
    @messages = @conversation.messages.order(created_at: :desc)
                                      .limit(messages_amount)
                                      .offset(params[:messages_to_display_offset].to_i)
    # définir une variable pour obtenir d'autres messages précédents de la conversation
    @messages_to_display_offset = params[:messages_to_display_offset].to_i + messages_amount

    @type = conversation_type.downcase
    # si les messages sont les derniers de la conversation, marquer la variable à 0
    # pour que le lien de chargement de plus de messages soit supprimé
    if @conversation.messages.count < @messages_to_display_offset
      @messages_to_display_offset = 0
    end
  end

end
```

Ici, nous demandons `active_support/concern` puis nous étendons notre module avec `ActiveSupport::Concern`, afin que Rails sache qu'il s'agit d'un concern.

Avec la méthode `[constantize](https://apidock.com/rails/String/constantize)`, nous créons dynamiquement un nom de constante en saisissant une valeur de chaîne. Nous appelons les modèles dynamiquement. La même méthode sera utilisée pour les modèles `Private::Conversation` et `Group::Conversation`.

Une fois que la méthode `get_messages` a défini toutes les variables d'instance nécessaires, l'action `index` répond avec le fichier partiel `_load_more_messages.js.erb`.

Enfin, après l'ajout des messages en haut de la liste, nous voulons supprimer l'icône de chargement de la fenêtre de conversation. Au bas du fichier `_load_more_messages.js.erb`, ajoutez :

```
<%= render remove_link_to_messages %>
```

Définissez maintenant la méthode helper `remove_link_to_messages` dans `Shared::MessagesHelper` :

```rb
# s'il n'y a plus de messages précédents
def remove_link_to_messages
  if @is_messenger == 'false'
    if @messages_to_display_offset != 0
      'shared/empty_partial'
    else
      'shared/load_more_messages/window/remove_more_messages_link' 
    end
  else
    'shared/empty_partial'
  end
end
```

Essayez d'écrire les specs pour cette méthode par vous-même.

Créez le fichier partiel `_remove_more_messages_link.js.erb` :

```js
$('#<%= @id_type %><%= @conversation.id %> .loading-more-messages')
    .replaceWith('');
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
.replaceWith('');
```

Désormais, dans le cas où il ne reste plus de messages précédents, le lien vers les messages précédents et l'icône de chargement seront supprimés.

Si vous essayez de contacter un utilisateur maintenant, une fenêtre de conversation s'affichera avec le message que vous avez envoyé à l'intérieur. Nous sommes capables de rendre les messages via des requêtes AJAX.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-99.png)

Validez les modifications.

```bash
git add -A
git commit -m "Afficher les messages avec AJAX

- Créer un fichier _message.html.erb dans private/messages
- Définir une méthode helper private_message_date_check dans Private::MessagesHelper et écrire les specs
- Créer un fichier _new_date.html.erb dans private/messages/message
- Définir les méthodes helper sent_or_received et seen_or_unseen dans Private::MessagesHelper et écrire les specs
- Créer un fichier _load_more_messages.js.erb dans private/messages
- Définir une méthode helper append_previous_messages_partial_path dans Shared::MessagesHelper
- Créer un fichier _append_messages.js.erb dans shared/load_more_messages/window
- Définir replace_link_to_private_messages_partial_path dans Private::MessagesHelper
- Créer un fichier _add_link_to_messages.js.erb dans private/messages/load_more_messages/window
- Créer un fichier toggle_window.js dans javascripts/conversations
- Créer un fichier messages_infinite_scroll.js dans assets/javascripts/conversations
- Définir une action index dans le Private::MessagesController
- Créer un fichier messages.rb dans controllers/concerns
- Définir remove_link_to_messages dans helpers/shared
- Créer un fichier _remove_more_messages_link.js.erb dans shared/load_more_messages/window"
```

#### **Fonctionnalité en temps réel avec Action Cable**

Les fenêtres de conversation ont déjà une allure soignée. Et elles ont aussi des fonctionnalités intéressantes. Mais il leur manque la fonctionnalité la plus importante — la capacité d'envoyer et de recevoir des messages en temps réel.

Comme nous l'avons brièvement évoqué précédemment, [Action Cable](http://guides.rubyonrails.org/action_cable_overview.html) nous permettra d'obtenir la fonctionnalité de temps réel souhaitée pour les conversations. Vous devriez parcourir rapidement la documentation pour comprendre comment tout cela fonctionne.

La première chose à faire est de créer une connexion WebSocket et de s'abonner à un canal spécifique. Heureusement, les connexions WebSocket sont déjà prises en charge par la configuration par défaut de Rails. Dans le répertoire `app/channels/application_cable`, vous voyez les fichiers `channel.rb` et `connection.rb`. La classe `Connection` s'occupe de l'authentification et la classe `Channel` est une classe parente pour stocker la logique partagée entre tous les canaux.

La connexion est définie par défaut. Nous avons maintenant besoin d'un canal de conversation privée auquel s'abonner. Générez un canal avec un espace de noms :

```
rails g channel private/conversation
```

Dans le `Private::ConversationChannel` généré, nous voyons les méthodes `subscribed` et `unsubscribed`. Avec la méthode `subscribed`, un utilisateur crée une connexion au canal. Avec la méthode `unsubscribed`, un utilisateur détruit évidemment la connexion.

Mettez à jour ces méthodes :

```rb
...
def subscribed
  stream_from "private_conversations_#{current_user.id}"
end

def unsubscribed
  stop_all_streams
end
...
```

Ici, nous voulons que chaque utilisateur ait son propre canal unique. À partir de ce canal, un utilisateur recevra et enverra des données. Comme les IDs des utilisateurs sont uniques, nous rendons le canal unique en ajoutant l'ID de l'utilisateur.

Il s'agit de la connexion côté serveur. Nous devons maintenant créer une connexion côté client également.

Pour créer une instance de la connexion côté client, nous devons écrire du JavaScript. En fait, Rails l'a déjà créée avec le générateur de canal. Naviguez vers `assets/javascripts/channels/private` et, par défaut, Rails génère des fichiers `CoffeeScript`. Je vais utiliser du JavaScript ici. Renommez donc le fichier en `conversation.js` et remplacez son contenu par :

```js
App.private_conversation = App.cable.subscriptions.create("Private::ConversationChannel", {
    connected: function() {},
    disconnected: function() {},
    received: function(data) {}
});
```

Redémarrez le serveur, allez sur l'application, connectez-vous et vérifiez le log du serveur.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-100.png)

Nous avons la connexion. Le cœur de la communication en temps réel est en place. Nous avons une connexion client-serveur constamment ouverte. Cela signifie que nous pouvons envoyer et recevoir des données du serveur sans redémarrer la connexion ou rafraîchir le navigateur, les amis ! C'est une chose vraiment puissante quand on y pense. À partir de maintenant, nous allons construire le système de messagerie autour de cette connexion.

Validez les modifications.

```bash
git add -A
git commit -m "Créer un canal de conversation privée unique et s'y abonner"
```

Rendons fonctionnel le formulaire de nouveau message de la fenêtre de conversation. Au bas du fichier `assets/javascripts/channels/private/conversations.js`, ajoutez cette fonction :

```js
...
$(document).on('submit', '.send-private-message', function(e) {
    e.preventDefault();
    var values = $(this).serializeArray();
    App.private_conversation.send_message(values);
    $(this).trigger('reset');
});
```

La fonction va récupérer les valeurs du formulaire de nouveau message et les transmettre à une fonction `send_message`. La fonction `send_message` va appeler une méthode `send_message` côté serveur, qui s'occupera de la création d'un nouveau message.

Notez également que le gestionnaire d'événements se trouve sur un bouton de soumission, mais sur la fenêtre de conversation, nous n'avons aucun bouton de soumission visible. C'est un choix de design. Nous devons programmer la fenêtre de conversation de manière à ce que le bouton de soumission soit déclenché lorsque la touche Entrée est cliquée sur un clavier. Cette fonction sera utilisée à l'avenir par d'autres fonctionnalités, créez donc un fichier `conversation.js` dans le répertoire `assets/javascripts/conversations` :

```js
$(document).on('turbolinks:load', function() { 
    
    // laisser un espace en haut de la barre de défilement des fenêtres de conversation
    $('.messages-list').scrollTop(500);

    // envoyer un message lors du clic sur la touche Entrée et laisser le textarea dans son état d'origine
    $(document).on('keydown', 
                   '.conversation-window, .conversation',
                   function(event) {
        if (event.keyCode === 13) {
            // si la fenêtre du textarea n'est pas vide
            if ($.trim($('textarea', this).val())) {
                $('.send-message', this).click();
                event.target.value = "";
                event.preventDefault();
            }  
        }
    });

});

function calculateUnseenConversations() {
    var unseen_conv_length = $('#conversations-menu').find('.unseen-conv').length;
    if (unseen_conv_length) {
        $('#unseen-conversations').css('visibility', 'visible');
        $('#unseen-conversations').text(unseen_conv_length);
    } else {
        $('#unseen-conversations').css('visibility', 'hidden');
        $('#unseen-conversations').text('');
    }
}
```

Dans ce fichier, nous décrivons certains comportements généraux pour les fenêtres de conversation. Le premier comportement est de maintenir la barre de défilement éloignée du haut, afin que les messages précédents ne soient pas chargés quand ce n'est pas nécessaire. La deuxième fonction s'assure que le bouton de soumission est déclenché lors du clic sur la touche Entrée, puis réinitialise la valeur de l'entrée à une chaîne vide.

Commencez par créer la fonction `send_message` à l'intérieur de l'objet `private_conversation`. Ajoutez-la sous la fonction de rappel `received` :

```js
...
send_message: function(message) {
    return this.perform('send_message', {
        message: message
    });
}
```

Ceci appelle la méthode `send_message` côté serveur et transmet la valeur du message. La méthode côté serveur doit être définie dans le `Private::ConversationChannel`. Définissez la méthode :

```rb
...
def send_message(data)
  message_params = data['message'].each_with_object({}) do |el, hash|
    hash[el['name']] = el['value']
  end
  Private::Message.create(message_params)
end
```

Ceci s'occupera de la création d'un nouveau message. Le paramètre `data`, que nous obtenons de l'argument passé, est un hash imbriqué. Ainsi, pour réduire cette complexité imbriquée en un seul hash, la méthode `[each_with_object](https://apidock.com/rails/Enumerable/each_with_object)` est utilisée.

Si vous essayez d'envoyer un nouveau message dans une fenêtre de conversation, un nouvel enregistrement de message sera effectivement créé. Il n'apparaîtra pas encore instantanément sur la fenêtre de conversation, seulement lorsque vous rafraîchirez le site. Il apparaîtrait, mais nous n'avons rien configuré pour diffuser les messages nouvellement créés vers le canal d'une conversation privée. Nous allons implémenter cela dans un instant. Mais avant de continuer et de valider les changements, récapitulons rapidement comment fonctionne le système de messagerie actuel.

1. Un utilisateur remplit le formulaire de nouveau message et soumet le message.
2. Le gestionnaire d'événements dans `javascripts/channels/private/conversations.js` récupère les données d'une fenêtre de conversation, un ID de conversation et une valeur de message, et déclenche la fonction `send_message` des instances de canal côté client.

3. La fonction `send_message` côté client appelle la méthode `send_message` côté serveur et lui transmet les données.

4. La méthode `send_message` côté serveur traite les données fournies et crée un nouvel enregistrement `Private::Message`.

Validez les modifications.

```bash
git add -A
git commit -m "Rendre fonctionnel le formulaire de nouveau message d'une fenêtre de conversation privée
- Ajouter un gestionnaire d'événements dans javascripts/channels/private/conversation.js pour déclencher le bouton de soumission
- Définir un comportement commun parmi les fenêtres de conversation dans assets/javascripts/conversations/conversation.js
- Définir une fonction send_message sur les deux côtés, client et serveur"
```

**Diffuser un nouveau message**

Après la création d'un nouveau message, nous voulons le diffuser d'une manière ou d'une autre vers le canal correspondant. Eh bien, les [Callbacks Active Record](http://guides.rubyonrails.org/active_record_callbacks.html) nous arment de nombreuses méthodes de rappel utiles pour les modèles. Il existe une méthode de rappel `after_create_commit`, qui s'exécute chaque fois qu'un nouvel enregistrement de modèle est créé. Dans le fichier du modèle `Private::Message`, ajoutez :

```rb
...
after_create_commit do 
  Private::MessageBroadcastJob.perform_later(self, previous_message)
end

def previous_message
  previous_message_index = self.conversation.messages.index(self) - 1
  self.conversation.messages[previous_message_index]
end
...
```

Comme vous le voyez, après la création d'un enregistrement, `Private::MessageBroadcastJob.perform_later` est appelé. Et qu'est-ce que c'est ? C'est une tâche de fond (background job), qui gère les opérations back-end. Elle permet d'exécuter certaines opérations quand nous le souhaitons. Cela peut être immédiatement après un événement particulier, ou être programmé pour s'exécuter un certain temps après un événement. Si vous n'êtes pas familier avec les tâches de fond, consultez [Active Job Basics](http://guides.rubyonrails.org/active_job_basics.html).

Ajoutez des specs pour la méthode `previous_message`. Si vous essayez de lancer les specs maintenant, commentez la méthode `after_create_commit`. Nous n'avons pas encore défini le `Private::MessageBroadcastJob`, donc actuellement les specs lèveraient une erreur de constante non définie.

```rb
...
context 'Methods' do
  it 'gets a previous message' do
    conversation = create(:private_conversation)
    message1 = create(:private_message, conversation_id: conversation.id)
    message2 = create(:private_message, conversation_id: conversation.id)
    expect(message2.previous_message).to eq message1
  end
end
...
```

Nous pouvons maintenant créer une tâche de fond qui diffusera un message nouvellement créé vers le canal d'une conversation privée.

```
rails g job private/message_broadcast
```

Dans le fichier, nous voyons une méthode `perform`. Par défaut, lorsque vous appelez un job, cette méthode est appelée. Maintenant, à l'intérieur du job, traitez les données fournies et diffusez-les aux abonnés du canal.

```rb
class Private::MessageBroadcastJob < ApplicationJob
  queue_as :default

  def perform(message, previous_message)
    sender = message.user
    recipient = message.conversation.opposed_user(sender)

    broadcast_to_sender(sender, recipient, message, previous_message)
    broadcast_to_recipient(sender, recipient, message, previous_message)
  end

  private

  def broadcast_to_sender(sender, recipient, message, previous_message)
    ActionCable.server.broadcast(
      "private_conversations_#{sender.id}",
      message: render_message(message, previous_message, sender),
      conversation_id: message.conversation_id,
      recipient_info: recipient
    )
  end

  def broadcast_to_recipient(sender, recipient, message, previous_message)
    ActionCable.server.broadcast(
      "private_conversations_#{recipient.id}",
      recipient: true,
      sender_info: sender,
      message: render_message(message, previous_message, recipient),
      conversation_id: message.conversation_id
    )
  end

  def render_message(message, previous_message, user)
    ApplicationController.render(
      partial: 'private/messages/message',
      locals: { message: message, 
                previous_message: previous_message, 
                user: user }
    )
  end
end
```

Ici, nous rendons un message et l'envoyons aux deux abonnés du canal. Nous transmettons également des paires clé-valeur supplémentaires pour afficher correctement le message. Si nous essayions d'envoyer un nouveau message, les utilisateurs recevraient les données, mais le message ne serait pas ajouté à la liste des messages. Aucun changement visible ne serait effectué.

Lorsque les données sont diffusées vers un canal, la fonction de rappel `received` côté client est appelée. C'est là que nous avons l'opportunité d'ajouter des données au DOM. Dans la fonction `received`, ajoutez le code suivant :

```js
...
received: function(data) {
    // si un lien vers la conversation dans la liste du menu des conversations existe
    // déplacer le lien vers le haut de la liste du menu des conversations
    var conversation_menu_link = $('#conversations-menu ul')
                                     .find('#menu-pc' + data['conversation_id']);
    if (conversation_menu_link.length) {
        conversation_menu_link.prependTo('#conversations-menu ul');
    }
    
    // définir les variables
    var conversation = findConv(data['conversation_id'], 'p');
    var conversation_rendered = ConvRendered(data['conversation_id'], 'p');
    var messages_visible = ConvMessagesVisiblity(conversation);

    if (data['recipient'] == true) {
        // marquer la conversation comme non vue, après la réception d'un nouveau message
        $('#menu-pc' + data['conversation_id']).addClass('unseen-conv');
        // si la fenêtre de conversation existe
        if (conversation_rendered) {
            if (!messages_visible) {
            // changer le style de la fenêtre de conv lorsqu'il y a des messages non vus
            // ajouter une classe supplémentaire à la fenêtre de la conversation ou autre chose
            }
            conversation.find('.messages-list').find('ul').append(data['message']);
        }
        calculateUnseenConversations();
    }
    else {
        conversation.find('ul').append(data['message']);
    }

    if (conversation.length) {
        // après l'ajout d'un nouveau message, faire défiler jusqu'au bas de la fenêtre de conversation
        var messages_list = conversation.find('.messages-list');
        var height = messages_list[0].scrollHeight;
        messages_list.scrollTop(height);
    }
}
...
```

Ici, nous voyons que l'expéditeur et le destinataire sont traités un peu différemment.

```
// changer le style de la fenêtre de conv lorsqu'il y a des messages non vus
// ajouter une classe supplémentaire à la fenêtre de la conversation ou autre chose
```

J'ai créé cela intentionnellement, afin que chaque fois qu'une conversation a des messages non vus, vous puissiez styliser sa fenêtre comme vous le souhaitez. Vous pouvez changer la couleur d'une fenêtre, la faire clignoter, ou tout ce que vous voulez.

De plus, les fonctions `findConv`, `ConvRendered`, `ConvMessagesVisibility` sont utilisées. Nous utiliserons ces fonctions pour les deux types de chats, privés et de groupe.

Créez un répertoire `shared` :

```
assets/javascripts/channels/shared
```

Créez un fichier `conversation.js` dans ce répertoire :

```js
// trouve une conversation dans le DOM
function findConv(conversation_id, type) {
    // si une conversation actuelle est ouverte dans le messenger
    var messenger_conversation = $('body .conversation');
    if (messenger_conversation.length) {
        // la conversation est ouverte dans le messenger
        return messenger_conversation;
    } else { 
        // la conversation est ouverte dans une fenêtre contextuelle (popup)
        var data_attr = "[data-" + type + "conversation-id='" + 
                         conversation_id + 
                         "']";
        var conversation = $('body').find(data_attr);
        return conversation;
    }
}

// vérifie si une fenêtre de conversation est rendue et visible sur un navigateur
function ConvRendered(conversation_id, type) {
    // si une conversation actuelle est ouverte dans le messenger
    if ($('body .conversation').length) {
        // la conversation est ouverte dans le messenger
        // cela signifie donc automatiquement qu'elle est visible
        return true;
    } else { 
        // la conversation est ouverte dans une fenêtre contextuelle
        var data_attr = "[data-" + type + "conversation-id='" + 
                         conversation_id + 
                         "']";
        var conversation = $('body').find(data_attr);
        return conversation.is(':visible');
    }
}

function ConvMessagesVisiblity(conversation) {
    // si la conversation actuelle est ouverte dans le messenger
    if ($('body .conversation').length) {
        // la conversation est ouverte dans le messenger
        // cela signifie donc automatiquement que les messages sont visibles
        return true;
    } else {
        // la conversation est ouverte dans une fenêtre contextuelle
        // vérifier si la fenêtre est réduite ou agrandie
        var visibility = conversation
                             .find('.panel-body')
                             .is(':visible');
        return visibility;
    }
}
```

Un messenger est mentionné assez souvent dans le code et nous n'avons pas encore de messenger. Le messenger sera un moyen distinct d'ouvrir des conversations. Pour éviter de nombreux petits changements à l'avenir, j'ai inclus les cas avec le messenger dès maintenant.

C'est tout, la fonctionnalité en temps réel devrait fonctionner. Les deux utilisateurs, l'expéditeur et le destinataire, devraient recevoir et voir s'afficher les nouveaux messages sur le DOM. Lorsque nous envoyons un nouveau message, nous devrions le voir instantanément ajouté à la liste des messages. Mais il y a un petit problème maintenant. Nous n'avons qu'une seule façon de rendre une fenêtre de conversation. Elle n'est rendue que lorsqu'une conversation est créée. Nous ajouterons d'autres moyens de rendre les fenêtres de conversation dans un instant. Mais avant cela, récapitulons comment les données atteignent les abonnés du canal.

1. Après la création d'un nouvel enregistrement `Private::Message`, la méthode `after_create_commit` est déclenchée, ce qui appelle la tâche de fond.
2. `Private::MessageBroadcastJob` traite les données fournies et les diffuse aux abonnés du canal.
3. Côté client, la fonction de rappel `received` est appelée, ce qui ajoute les données au DOM.

Validez les modifications.

```bash
git add -A
git commit -m "Diffuser un nouveau message
- Dans Private::Message, définir une méthode de rappel after_create_commit.
- Créer un Private::MessageBroadcastJob
- Définir une fonction received dans assets/javascripts/channels/private/conversation.js
- Créer un fichier conversation.js dans assets/javascripts/channels/shared"
```

#### **Mise à jour de la barre de navigation**

Sur la barre de navigation, nous allons afficher une liste des conversations de l'utilisateur. Lorsqu'une liste de conversations est ouverte, nous voulons voir les conversations triées par les derniers messages. Les conversations avec les messages les plus récents seront en haut de la liste. Cette liste doit être accessible dans toute l'application. Ainsi, dans l'`ApplicationController`, stockez les conversations triées de l'utilisateur dans une variable d'instance. La façon dont je suggère de le faire est de définir une méthode `all_ordered_conversations` dans le contrôleur :

```rb
def all_ordered_conversations 
  if user_signed_in?
    @all_conversations = OrderConversationsService.new({user: current_user}).call
  end
end
```

Ajoutez un filtre `before_action`, afin que la variable d'instance `@all_conversations` soit disponible partout.

```
before_action :all_ordered_conversations
```

Et créez ensuite un `OrderConversationsService` pour s'occuper de la requête et du tri des conversations.

```rb
class OrderConversationsService

  def initialize(params)
    @user = params[:user]
  end

  # obtenir et trier les conversations par les dates des derniers messages par ordre décroissant
  def call
    all_private_conversations = Private::Conversation.all_by_user(@user.id)
                                                     .includes(:messages)
    return all_conversations = all_private_conversations.sort{ |a, b| 
      b.messages.last.created_at <=> a.messages.last.created_at
    }
  end

end
```

Actuellement, ce service ne traite que les conversations privées, c'est le seul type de conversations que nous avons développé jusqu'à présent. À l'avenir, nous mélangerons les conversations privées et de groupe, et nous les trierons par leurs derniers messages. La méthode `[sort](https://apidock.com/ruby/Array/sort)` est utilisée pour trier un tableau de conversations. Encore une fois, si nous n'utilisions pas la méthode `includes`, nous serions confrontés à un problème de requête N + 1. Car lorsque nous trions les conversations, nous vérifions les dates de création des derniers messages de chaque conversation et nous les comparons. C'est pourquoi, avec la requête, nous avons inclus les enregistrements des messages.

L'opérateur `<=>` évalue quelle valeur `created_at` est la plus élevée. Si nous utilisions `a <=> b`, cela trierait un tableau donné par ordre croissant. Lorsque vous évaluez les valeurs dans le sens opposé, `b <=> a`, cela trie un tableau par ordre décroissant.

Nous n'avons pas encore défini le scope `all_by_user` dans le modèle `Private::Conversation`. Ouvrez le modèle et définissez le scope :

```rb
...
scope :all_by_user, -> (user_id) do
  where(recipient_id: user_id).or(where(sender_id: user_id))
end
...
```

Écrivez les specs pour le service et le scope :

```rb
context 'Scopes' do
  it "gets all user's conversations" do
    create_list(:private_conversation, 5)
    user = create(:user)
    create_list(:private_conversation, 2, recipient_id: user.id)
    create_list(:private_conversation, 2, sender_id: user.id)
    conversations = Private::Conversation.all_by_user(user.id)
    expect(conversations.count).to eq 4
  end 
end
```

```rb
require 'rails_helper'
require './app/services/order_conversations_service.rb'

describe OrderConversationsService do
  context '#call' do
    it 'returns ordered conversations in descending order' do
      user = create(:user)
      conversation1 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversation2 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversations = [conversation2, conversation1]
      expect(OrderConversationsService.new({user: user}).call).to eq conversations
    end
  end
end
```

Validez les modifications.

```bash
git add -A
git commit -m "
- Créer un OrderConversationsService et ajouter des specs
- Définir un scope all_by_user dans le modèle Private::Conversation et ajouter des specs"
```

Désormais, dans les vues, nous avons accès à un tableau de conversations triées. Affichons une liste de leurs liens. Chaque fois qu'un utilisateur clique sur l'un d'eux, une fenêtre de conversation s'affiche sur l'application. Si vous vous souvenez bien, notre barre de navigation comporte deux composants majeurs. Dans l'un, les éléments sont affichés en permanence. Dans l'autre, les éléments se réduisent sur les petits appareils. Ainsi, dans l'en-tête de la navigation, où les composants sont visibles tout le temps, nous allons créer un menu déroulant de conversations. Comme d'habitude, pour éviter d'avoir un fichier de vue trop volumineux, divisez-le en plusieurs plus petits.

Ouvrez le fichier `_header.html.erb` de la navigation et remplacez son contenu par ce qui suit :

```html
<div class="navbar-header">
  <% nav_header_content_partials.each do |partial_path| %>
    <%= render partial: partial_path %>
  <% end %>
</div><!-- navbar-header -->
```

Créez maintenant un répertoire `header` avec un fichier `_toggle_button.html.erb` à l'intérieur :

```html
<button type="button" 
        class="navbar-toggle collapsed" 
        data-toggle="collapse" 
        data-target="#navbar-collapsible-content" 
        aria-expanded="false">
  <span class="sr-only">Toggle navigation</span>
  <span class="icon-bar"></span>
  <span class="icon-bar"></span>
  <span class="icon-bar"></span>
</button>
```

Il s'agit du bouton de bascule qui se trouvait auparavant dans le fichier `_header.html.erb`. Créez un autre fichier dans le répertoire `header` :

```html
<%= link_to 'collabfield', root_path, class: 'navbar-brand' %>
<%= link_to root_path, class: 'navbar-brand brand-mobile' do %>
	<i class="fa fa-home" aria-hidden="true"></i>
<% end %>
```

Et voici le bouton d'accueil du `_header.html.erb`. Il y a aussi un lien supplémentaire ici. Sur les petits appareils, nous allons afficher une icône au lieu du nom de l'application.

Revenez au fichier `_header.html.erb`. Il y a une méthode helper `nav_header_content_partials`, qui renvoie un tableau de chemins de partiels. La raison pour laquelle nous ne nous contentons pas de rendre les partiels un par un est que le tableau différera selon les cas. Dans le `NavigationHelper`, définissez la méthode :

```rb
# rendre le contenu de l'en-tête de navigation
def nav_header_content_partials
  partials = []
  if params[:controller] == 'messengers' 
    partials << 'layouts/navigation/header/messenger_header'
  else # le contrôleur n'est pas messengers  
    partials << 'layouts/navigation/header/toggle_button'
    partials << 'layouts/navigation/header/home_button'
    partials << 'layouts/navigation/header/dropdowns' if user_signed_in?
  end
  partials
end
```

Écrivez les specs pour les méthodes dans `navigation_helper_spec.rb` :

```rb
context '#nav_header_content_partials' do
  it "returns messenger_header partial's path" do
    controller.params[:controller] = 'messengers'
    partials = ['layouts/navigation/header/messenger_header']
    expect(helper.nav_header_content_partials).to eq partials
  end

  it "returns partials' paths for buttons without dropdowns" do
    controller.params[:controller] = 'not_messengers'
    view.stub(:user_signed_in?).and_return(false)
    partials = ['layouts/navigation/header/toggle_button']
    partials << 'layouts/navigation/header/home_button'
    expect(helper.nav_header_content_partials).to eq partials
  end

  it "returns partials' paths for buttons and dropdowns" do
    controller.params[:controller] = 'not_messengers'
    view.stub("user_signed_in?").and_return(true)
    partials = ['layouts/navigation/header/toggle_button']
    partials << 'layouts/navigation/header/home_button'
    partials << 'layouts/navigation/header/dropdowns'
    expect(helper.nav_header_content_partials).to eq partials
  end
end
```

Créez maintenant les fichiers nécessaires pour afficher les menus déroulants sur la barre de navigation. Commencez par créer un fichier `_dropdowns.html.erb` :

```html
<div class='pull-right' id ='conversations-menu'>
  <%= render 'layouts/navigation/header/dropdowns/conversations' %>
</div>
```

Créez un répertoire `dropdowns` avec un fichier `_conversations.html.erb` à l'intérieur :

```html
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
  <i class="fa fa-envelope-o" aria-hidden="true">
    <span id="unseen-conversations"></span>
  </i>
</a>

<ul class="dropdown dropdown-menu" role="menu">
  <% @all_conversations.each do |conversation| %>
    <%= render partial: conversation_header_partial_path(conversation),
               locals: { conversation: conversation, 
                         user_id: current_user.id } %>
  <% end %>
</ul><!-- dropdown-menu -->
```

C'est ici que nous utilisons la variable d'instance `@all_conversations`, définie précédemment dans le contrôleur, et que nous rendons les liens pour ouvrir les conversations. Les liens pour les différents types de conversations vont différer. Nous devrons créer deux versions différentes de liens pour les conversations privées et de groupe. Définissez d'abord la méthode helper `conversation_header_partial_path` dans le `NavigationHelper` :

```rb
# renvoyer le chemin d'un partiel d'en-tête de conversation
def conversation_header_partial_path(conversation)
  if conversation.class == Private::Conversation
    'layouts/navigation/header/dropdowns/conversations/private_conversation'
  else
    'layouts/navigation/header/dropdowns/conversations/group_conversation'
  end  
end
```

Écrivez les specs pour cela :

```rb
context '#conversation_header_partial_path' do
  it "returns a partial's path for a private conversation's header" do
    conversation = create(:private_conversation)
    expect(helper.conversation_header_partial_path(conversation)). to eq(
      'layouts/navigation/header/dropdowns/conversations/private'
    )
  end

  it "returns a partial's path for a group conversation's header" do
    conversation = create(:group_conversation)
    expect(helper.conversation_header_partial_path(conversation)). to eq(
      'layouts/navigation/header/dropdowns/conversations/group'
    )
  end
end
```

Bien sûr, nous n'avons encore rien fait avec les conversations de groupe. Vous devez donc commenter la partie sur les conversations de groupe dans les specs pendant un certain temps pour éviter les échecs.

Créez un fichier pour les liens des conversations privées :

```html
<% recipient = private_conv_recipient(conversation) %>
<% seen_status = private_conv_seen_status(conversation) %>
<li id="menu-pc<%= conversation.id %>" 
    class="<%= seen_status %>"
    data-id="<%= conversation.id %>"
    data-type="private">
    <%= link_to recipient.name, 
                open_private_conversation_path(id: conversation.id), 
                remote: true, 
                method: :post,
                class: 'bigger-screen-link' %>
</li>
```

Définissez la méthode helper `private_conv_seen_status` dans un nouveau `Shared::ConversationsHelper` :

```rb
module Shared::ConversationsHelper

  def private_conv_seen_status(conversation) 
    # si le dernier message d'une conversation n'est pas créé par current_user
    # et qu'il n'est pas vu, renvoyer une valeur unseen-conv
    not_created_by_user = conversation.messages.last.user_id != current_user.id
    unseen = conversation.messages.last.seen == false
    not_created_by_user && unseen ? 'unseen-conv' : ''
  end
end
```

Ajoutez ce module au `Private::ConversationsHelper` :

```rb
include Shared::ConversationsHelper
```

Dans les specs, créez un répertoire `shared` avec un fichier `conversations_helper_spec.rb` pour tester la méthode helper `private_conv_seen_status` :

```rb
require 'rails_helper'

RSpec.describe Shared::ConversationsHelper, :type => :helper do

  context '#private_conv_seen_status' do
    it 'returns an empty string' do
      current_user = create(:user)
      conversation = create(:private_conversation)
      create(:private_message, 
              conversation_id: conversation.id,
              seen: false, 
              user_id: current_user.id)
      view.stub(:current_user).and_return(current_user)
      expect(helper.private_conv_seen_status(conversation)).to eq ''
    end

    it 'returns an empty string' do
      current_user = create(:user)
      recipient = create(:user)
      conversation = create(:private_conversation)
      create(:private_message, 
              conversation_id: conversation.id,
              seen: true, 
              user_id: recipient.id)
      view.stub(:current_user).and_return(current_user)
      expect(helper.private_conv_seen_status(conversation)).to eq ''
    end

    it 'returns unseen-conv status' do
      current_user = create(:user)
      recipient = create(:user)
      conversation = create(:private_conversation)
      create(:private_message, 
              conversation_id: conversation.id,
              seen: false, 
              user_id: recipient.id)
      view.stub(:current_user).and_return(current_user)
      expect(helper.private_conv_seen_status(conversation)).to eq(
        'unseen-conv'
      )
    end
  end

end
```

Lorsqu'un lien vers une conversation est cliqué, l'action `open` du contrôleur `Private::Conversation` est appelée. Définissez une route vers cette action. Dans le fichier `routes.rb`, ajoutez un membre `post :open` à l'intérieur des ressources `private_conversations` avec espace de noms, juste en dessous de `post :close`.

Bien sûr, n'oubliez pas de définir l'action elle-même dans le contrôleur :

```rb
def open
  @conversation = Private::Conversation.find(params[:id])
  add_to_conversations unless already_added?
  respond_to do |format|
    format.js { render partial: 'private/conversations/open' }
  end
end
```

Maintenant, une fenêtre de conversation devrait s'ouvrir lorsque vous cliquez sur son lien. La barre de navigation est actuellement désordonnée, nous devons nous occuper de son design. Pour styliser les menus déroulants, ajoutez du CSS au fichier `navigation.scss` :

```scss
.brand-mobile {
  font-size: 20px;
  font-size: 2.0rem;
}

.navigation-items {
  position: absolute;
  top: 0;
  left: 50%;
}

.navbar-header {
  .open {
    width: 36px;
  }
}

.non-user-nav-links {
  display: inline-block;
  height: 50px;
  line-height: 50px;
  vertical-align: middle;
  padding-right: 20px;
}

#conversations-menu, #contacts-requests {
  font-size: 20px;
  font-size: 2.0rem;
  height: 50px;
  line-height: 50px;
  padding-right: 10px;

  ul {
    margin: 0;
    position: relative;
    top: 50px;
    right: 200px;
    border-radius: 0 0 5px 5px;
    height: 300px;
    overflow: scroll;
    overflow-x: hidden;
    li {
      a {
        width: 100%;
      }
    }
  }
  .unseen-conv {
    a {
      background: $backgroundColor;
      color: black !important;
    }
  }
}

#unseen-conversations, #unresponded-contact-requests {
  visibility: hidden;
  padding: 1px;
  position: absolute;
  // color: white;
  font-size: 13px;
  font-size: 1.3rem;
}

#unseen-conversations {
  right: 5px;
  background: #E92F2F;
}

#conversations-menu {
  i {
    position: relative;
  }
}

#conversations-list {
  position: fixed;
  bottom: 0;
  right: 0;
  padding: 0;
  .col-sm-2 {
    padding: 0;
  }
}
```

Mettez à jour la requête média `max-width: 767px` dans `mobile.scss` :

```scss
@media screen and (max-width: 767px) {
  .col-sm-10 {
    display: none;
    padding: 0 !important;
    .conversation {
      padding: 50px 0 0 0;
    }
    .private-conversation .messages-list {
      width: 100%;
      right: 0;
    }
    .group-conversation .messages-list {
      width: 100%;
      left: 0;
    }
    .send-private-message, .send-group-message {
      position: fixed;
      bottom: 0;
    }
  }
  .pc-menu {
    display: none !important;
  }
  .single-post-list {
    min-height: 65px;
    max-height: 65px;
    padding: 10px 0;
  }
  .bigger-screen-link, .brand-bigger-screen {
    display: none !important;
  }
  .smaller-screen-link {
    padding: 10px 20px !important;
  }
  .conversation-window {
    display: none !important;
  }
  .navbar-brand {
    margin: 0 !important;
  }
  .mobile-menu {
    i {
      color: white;
    }
    ul {
      padding: 0px;
    }
    a {
      display: block;
      padding: 10px 0px 10px 25px !important;
    }
    a:hover {
      background: white !important;
      color: black !important;
      i {
        color: black;
      }
    }
  }
  .navbar-header {
    #conversations-menu, #messages-page-name {
      a {
        float: left;
      }
      ul {
        position: absolute;
        left: 0;
        width: 100%;
      }
    }
    #conversations-menu {
      width: 40%;
    }
    #messages-page-name  {
      width: 50%;
    }
    #contacts-requests {
      ul {
        position: absolute;
        left: 0;
        width: 100%;
      }
    }
  }
  #side-menu {
    display: none !important;
  }
  #feed {
    padding: 0;
  }
}
```

Mettez à jour la requête média `min-width: 767px` dans `desktop.scss` :

```scss
@media screen and (min-width: 767px) {
  // stylisation de la barre de défilement
  ::-webkit-scrollbar-track
  {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    // border-radius: 10px;
    background-color: #F5F5F5;
  }
  ::-webkit-scrollbar
  {
    width: 12px;
    background-color: #F5F5F5;
  }
  ::-webkit-scrollbar-thumb
  {
    // border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    background-color: $navbarColor;
  }
  body nav {
    display: initial !important;
  }
  .smaller-screen-link {
    display: none !important;
  }
  .brand-mobile {
    display: none;
  }
  .mobile-menu {
    display: none !important;
  }
  #conversations-menu, #contacts-requests {
    ul {
      width: 400px;
      top: 0;
    }
  }
}
```

L'application ressemble maintenant à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-101.png)

Ensuite, vous pouvez agrandir la liste des conversations :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-102.png)

En cliquant sur l'un des liens du menu, une fenêtre de conversation devrait apparaître sur l'application :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-103.png)

Si vous essayez de réduire la taille du navigateur, les conversations devraient être masquées une par une :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-104.png)

Notez également qu'au lieu du logo collabfield, nous avons maintenant l'icône de la page d'accueil. Et la liste des conversations est toujours disponible sur les petits écrans. Eh bien, si les fenêtres de conversation sont masquées sur les petits appareils, comment les utilisateurs vont-ils communiquer sur les appareils mobiles ? Nous allons créer un messenger qui s'ouvrira à la place d'une fenêtre de conversation.

Validez les modifications :

```bash
git add -A
git commit -m "Afficher un menu déroulant de liens de conversations
- diviser le contenu du fichier layouts/navigation/_header.html.erb en partiels
- Créer un _toggle_button.erb.html dans layouts/navigation/header
- Créer un _home_button.html.erb dans layouts/navigation/header
- Définir nav_header_content_partials dans NavigationHelper et écrire les specs
- Créer un _dropdowns.html.erb dans layouts/navigation/header
- Créer un _conversation.html.erb dans layouts/navigation/header/dropdowns
- Définir conversation_header_partial_path dans NavigationHelper et écrire les specs
- Créer un _private.html.erb dans layouts/navigation/header/dropdowns/conversations
- Définir private_conv_seen_status dans Shared::ConversationsHelper et écrire les specs
- Définir une action open dans le contrôleur Private::Conversations
- ajouter du CSS pour styliser les menus déroulants sur la barre de navigation dans navigation.scss, mobile.scss et desktop.scss"
```

C'est le bon moment pour s'assurer que toutes les fonctionnalités de la messagerie en temps réel fonctionnent correctement.

Comme nous ajoutons des éléments au DOM de manière dynamique, il arrive que les éléments soient ajoutés trop tard et que Capybara pense qu'un élément n'existe pas, car le temps d'attente par défaut n'est que de 2 secondes. Pour éviter ces échecs, dans le fichier `rails_helper.rb`, changez le temps d'attente pour une valeur comprise entre 5 et 10 secondes :

```rb
Capybara.default_max_wait_time = 5
```

Dans le dossier `spec/features/private/conversations`, créez un fichier `window_spec.rb` :

```rb
require "rails_helper"

RSpec.feature "window", :type => :feature do
  let(:user) { create(:user) }
  let(:conversation) { create(:private_conversation, sender_id: user.id) }
  let(:open_window) do
    sign_in user
    visit root_path
    find('#conversations-menu .dropdown-toggle').trigger('click')
    find('#conversations-menu li a').click
    expect(page).to have_selector('.conversation-window')
  end
  before(:each) do 
    conversation
    create(:private_message, conversation_id: conversation.id, user_id: user.id)
  end

  scenario 'user opens a conversation', js: true do
    open_window
  end

  scenario 'user closes a conversation', js: true do 
    open_window
    find('.conversation-window .close-conversation').click
    expect(page).not_to have_selector('.conversation-window')
  end

  scenario 'user sends a message', js: true do 
    open_window
    expect(page).to have_selector('.conversation-window .messages-list li', count: 1)
    find('.conversation-window').fill_in 'body', with: 'hey, mate'
    find('.conversation-window form .send-message', visible: false).trigger('click')
    expect(page).to have_selector('.conversation-window .messages-list li', count: 2)
  end

  scenario 'user collapses and expands a conversation window', js: true do
    open_window
    find('.conversation-window .conversation-heading').click
    expect(page).not_to have_selector('.conversation-window .messages-list')
  end
end
```

Ici, je n'ai pas défini de specs pour tester si un utilisateur destinataire reçoit des messages en temps réel. Essayez de comprendre comment écrire de tels tests par vous-même.

Validez les modifications :

```bash
git add -A
git commit -m "Ajouter des specs pour tester la fonctionnalité de la fenêtre de conversation"
```

Si vous vous connectiez à un compte ayant reçu des messages, vous remarqueriez une conversation marquée comme non vue :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-105.png)

Pour l'instant, il n'y a aucun moyen de marquer les conversations comme vues. Par défaut, un nouveau message a une valeur non vue. Programmez l'application de manière à ce que lorsqu'une fenêtre de conversation est ouverte ou cliquée, ses messages soient marqués comme vus. Notez également qu'actuellement, nous ne voyons les conversations non vues en surbrillance que lorsque le menu déroulant est agrandi. À l'avenir, nous créerons une fonctionnalité de notifications, afin que les utilisateurs sachent qu'ils ont reçu de nouveaux messages sans avoir à agrandir quoi que ce soit.

Attaquons-nous au premier problème. Lorsqu'une conversation est déjà rendue sur l'application, mais qu'elle est réduite, et qu'un utilisateur clique sur le lien du menu déroulant pour ouvrir cette conversation, rien ne se passe. Cette conversation réduite reste réduite. Nous devons ajouter du JavaScript pour que, dans le cas d'un clic sur le lien du menu déroulant, la conversation s'agrandisse et mette le focus sur sa zone de nouveau message.

Ouvrez le fichier ci-dessous et ajoutez le code du Gist pour y parvenir :

```
assets/javascripts/conversations/toggle_window.js
```

```js
// quand le lien pour ouvrir une conversation est cliqué
// et que la fenêtre de conversation existe déjà sur la page
// mais qu'elle est réduite, on l'agrandit
$('#conversations-menu').on('click', 'li', function(e) {
    // obtenir l'ID de la fenêtre de conversation
    var conv_id = $(this).attr('data-id');
    // obtenir le type de conversation
    if ($(this).attr('data-type') == 'private') {
        var conv_type = '#pc';
    } else {
        var conv_type = '#gc';
    }
    var conversation_window = $(conv_type + conv_id);

    // si la fenêtre de conversation existe 
    if (conversation_window.length) {
        // si la fenêtre est réduite, on l'agrandit
        if (conversation_window.find('.panel-body').css('display') == 'none') {
            conversation_window.find('.conversation-heading').click();
        }
        // marquer comme vu en cliquant dessus et mettre le focus sur le textarea
        conversation_window.find('form textarea').click().focus();
    }
});
```

Lorsque vous cliquez sur un lien pour ouvrir une fenêtre de conversation, qu'une conversation soit déjà présente sur l'application ou non, elle sera agrandie.

Nous avons maintenant besoin d'un gestionnaire d'événements. Après qu'une fenêtre de conversation contenant des messages non vus a été cliquée, le côté client de la conversation privée doit déclencher une fonction de rappel. Tout d'abord, définissez un gestionnaire d'événements à l'intérieur du côté client de la conversation privée, au bas du fichier :

```js
$(document).on('click', '.conversation-window, .private-conversation', function(e) {
    // si le dernier message d'une conversation n'est pas un message de l'utilisateur et n'est pas vu
    // marquer les messages non vus comme vus
    var latest_message = $('.messages-list ul li:last .row div', this);
    if (latest_message.hasClass('message-received') && latest_message.hasClass('unseen')) {
        var conv_id = $(this).find('.panel').attr('data-pconversation-id');
        // si conv_id n'existe pas, cela signifie que la conversation est ouverte dans le messenger
        if (conv_id == null) {
            var conv_id = $(this).find('.messages-list').attr('data-pconversation-id');
        }
        // marquer la conversation comme vue dans la liste du menu des conversations
        latest_message.removeClass('unseen');
        $('#menu-pc' + conv_id).removeClass('unseen-conv');
        calculateUnseenConversations();
        App.private_conversation.set_as_seen(conv_id);
    }
});

$(document).on('turbolinks:load', function() {
    calculateUnseenConversations();
});
```

Le cas de l'existence du messenger est déjà inclus dans cet extrait de code.

Ensuite, définissez la fonction de rappel à l'intérieur de l'instance `private_conversation`, juste en dessous de la fonction `send_message` :

```js
set_as_seen: function(conv_id) {
    return this.perform('set_as_seen', { conv_id: conv_id });
}
```

Enfin, définissez cette méthode côté serveur :

```rb
def set_as_seen(data)
  # trouver une conversation et marquer tous ses messages non vus comme vus
  conversation = Private::Conversation.find(data["conv_id"].to_i)
  messages = conversation.messages.where(seen: false)
  messages.each do |message|
    message.update(seen: true)
  end
end
```

Dès qu'un utilisateur clique sur un lien pour ouvrir une fenêtre de conversation ou clique directement sur une fenêtre de conversation, ses messages non vus seront marqués comme vus.

Validez les modifications :

```bash
git add -A
git commit -m "Ajouter la possibilité de marquer les messages non vus comme vus
- Ajouter un gestionnaire d'événements pour agrandir les fenêtres de conversation dans assets/javascripts/conversations/toggle_window.js
- Ajouter un gestionnaire d'événements pour marquer les messages non vus comme vus dans assets/javascripts/channels/private/conversation.js
- Définir une méthode set_as_seen pour Private::ConversationChannel"
```

Assurez-vous que tout fonctionne comme prévu en écrivant les specs.

#### Contacts

Pour rester en contact avec les personnes rencontrées sur l'application, vous devez pouvoir les ajouter à vos contacts. Cette fonctionnalité nous manque pour l'instant. De plus, le fait d'avoir une fonctionnalité de contacts ouvre de nombreuses possibilités pour créer d'autres fonctionnalités que seuls les utilisateurs acceptés comme contact pourraient effectuer.

Générez un modèle `Contact` :

```
rails g model contact
```

Définissez les associations, la validation et une méthode pour trouver un enregistrement de contact en fournissant les IDs des utilisateurs.

```rb
class Contact < ApplicationRecord
  belongs_to :user
  belongs_to :contact, class_name: "User"

  validates_uniqueness_of :user_id, scope: :contact_id

  def self.find_by_users(user_id, contact_id)
    where('user_id = ? AND contact_id = ?', user_id, contact_id).or(
           where('user_id = ? AND contact_id = ?', contact_id, user_id)
         )[0]
  end
end
```

Définissez la table des contacts :

```rb
class CreateContacts < ActiveRecord::Migration[5.1]
  def change
    create_table :contacts do |t|
      t.belongs_to :user, index: true
      t.belongs_to :contact, index: true
      t.boolean :accepted, default: false

      t.timestamps
    end
  end
end
```

Une factory pour les contacts sera nécessaire. Définissez-la :

```rb
FactoryGirl.define do 
  factory :contact do
    association :user, factory: :user
    association :contact, factory: :user
  end
end
```

Écrivez les specs pour tester le modèle :

```rb
require 'rails_helper'

RSpec.describe Contact, type: :model do

  let(:contact) { build(:contact) }

  context 'Associations' do
    it 'belongs_to user' do
      association = described_class.reflect_on_association(:user)
      expect(association.macro).to eq :belongs_to
    end

    it 'belongs_to contact' do
      association = described_class.reflect_on_association(:contact)
      expect(association.macro).to eq :belongs_to
      expect(association.options[:class_name]).to eq 'User'
    end
  end

  context 'Validations' do
    it 'is valid to create a new contact' do
      expect(contact).to be_valid
    end

    it 'is not valid with the same user' do
      contact = create(:contact)
      duplicate_contact = contact.dup
      expect(duplicate_contact).not_to be_valid
    end
  end

  context 'Methods' do
    it 'finds by users' do
      user1 = create(:user)
      user2 = create(:user)
      contact = create(:contact, user_id: user1.id, contact_id: user2.id)
      expect(Contact.find_by_users(user1.id, user2.id)).to eq contact
    end
  end

end
```

Validez les modifications :

```bash
git add -A
git commit -m "Créer un modèle Contact et écrire les specs correspondantes"
```

Dans le fichier du modèle `User`, nous devons définir les associations appropriées et également définir certaines méthodes pour aider aux requêtes de contacts.

```rb
has_many :contacts
has_many :all_received_contact_requests,  
          class_name: "Contact", 
          foreign_key: "contact_id"

has_many :accepted_sent_contact_requests, -> { where(contacts: { accepted: true}) }, 
          through: :contacts, 
          source: :contact
has_many :accepted_received_contact_requests, -> { where(contacts: { accepted: true}) }, 
          through: :all_received_contact_requests, 
          source: :user
has_many :pending_sent_contact_requests, ->  { where(contacts: { accepted: false}) }, 
          through: :contacts, 
          source: :contact
has_many :pending_received_contact_requests, ->  { where(contacts: { accepted: false}) }, 
          through: :all_received_contact_requests, 
          source: :user


# récupère tous vos contacts
def all_active_contacts
  accepted_sent_contact_requests | accepted_received_contact_requests
end

# récupère vos contacts en attente, envoyés et reçus
def pending_contacts
  pending_sent_contact_requests | pending_received_contact_requests
end

# récupère un enregistrement Contact
def contact(contact)
  Contact.where(user_id: self.id, contact_id: contact.id)[0]
end
```

Couvrez les associations et les méthodes avec des specs :

```rb
context 'Associations' do

  ...
  
  it 'has_many contacts' do
    association = described_class.reflect_on_association(:contacts)
    expect(association.macro).to eq :has_many
  end

  it 'has_many all_received_contact_requests' do
    association = described_class.reflect_on_association(:all_received_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:class_name]).to eq 'Contact'
    expect(association.options[:foreign_key]).to eq 'contact_id'
  end

  it 'has_many accepted_sent_contact_requests' do
    association = described_class.reflect_on_association(:accepted_sent_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :contacts
    expect(association.options[:source]).to eq :contact
  end

  it 'has_many accepted_received_contact_requests' do
    association = described_class.reflect_on_association(:accepted_received_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :all_received_contact_requests
    expect(association.options[:source]).to eq :user
  end

  it 'has_many pending_sent_contact_requests' do
    association = described_class.reflect_on_association(:pending_sent_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :contacts
    expect(association.options[:source]).to eq :contact
  end

  it 'has_many pending_received_contact_requests' do
    association = described_class.reflect_on_association(:pending_received_contact_requests)
    expect(association.macro).to eq :has_many
    expect(association.options[:through]).to eq :all_received_contact_requests
    expect(association.options[:source]).to eq :user
  end
end

context 'Methods' do
  let(:user) { build(:user) }
  let(:contact_requests) do
    @user = create(:user)
    create_list(:contact, 2)
    create_list(:contact, 2, accepted: true)
    create(:contact, user_id: @user.id)
    create(:contact, user_id: @user.id, accepted: true)
    create(:contact, contact_id: @user.id)
    create(:contact, contact_id: @user.id, accepted: true)
  end

  it 'accepted_sent_contact_requests gets only accepted requests' do
    contact_requests
    expect(@user.accepted_sent_contact_requests.count).to eq 1
  end

  it 'accepted_received_contact_requests gets only accepted requests' do
    contact_requests
    expect(@user.accepted_received_contact_requests.count).to eq 1
  end

  it 'pending_sent_contact_requests gets only unaccepted requests' do
    contact_requests
    expect(@user.pending_sent_contact_requests.count).to eq 1
  end

  it 'pending_received_contact_requests gets only unaccepted requests' do
    contact_requests
    expect(@user.pending_received_contact_requests.count).to eq 1
  end
end
```

Validez les modifications :

```bash
git add -A
git commit -m "Ajouter des associations et des méthodes helper au modèle User
- Créer une relation entre les modèles User et Contact
- Les méthodes aident à interroger les enregistrements Contact"
```

Générez un contrôleur `Contacts` et définissez ses actions :

```
rails g controller contacts
```

```rb
class ContactsController < ApplicationController

  def create
    @contact = current_user.contacts.create(contact_id: params[:contact_id])
    respond_ok
  end

  def update
    @contact = Contact.find_by_users(params[:id], current_user.id)
    @contact.update(accepted: true)
    respond_ok
  end

  def destroy
    @contact = Contact.find_by_users(params[:id], current_user.id)
    @contact.destroy
    respond_ok
  end

  private

  def respond_ok
    respond_to do |format|
      format.json  { head :ok } 
    end
  end

end
```

Comme vous le voyez, les utilisateurs pourront créer un nouvel enregistrement de contact, mettre à jour son statut (accepter un utilisateur dans leurs contacts) et supprimer un utilisateur de leur liste de contacts. Comme toutes les actions sont appelées via AJAX et que nous ne voulons pas rendre de templates en réponse, nous répondons avec une réponse de succès. De cette façon, Rails n'a pas à se demander quoi répondre.

Définissez les routes correspondantes :

```rb
resources :contacts, only: [:create, :update, :destroy]
```

Validez les modifications.

```bash
git add -A
git commit -m "Créer un ContactsController et définir les routes vers ses actions"
```

#### **Mise à jour de la fenêtre de conversation privée**

La façon dont les utilisateurs vont pouvoir envoyer et accepter des demandes de contact se fera via une fenêtre de conversation privée. Plus tard, nous ajouterons un moyen supplémentaire d'accepter les demandes via un menu déroulant de la barre de navigation.

Créez un nouveau répertoire `heading` :

```
private/conversations/conversation/heading
```

C'est ici que nous garderons les options supplémentaires pour une fenêtre de conversation privée. Dans le répertoire, créez un fichier `_add_user_to_contacts.html.erb` :

```html
<%= link_to contacts_path(contact_id: @recipient), 
            method: :post, 
            remote: true, 
            class: 'add-user-to-contacts add-user-to-contacts-notif' do %>
  <i class="fa fa-user-plus" aria-hidden="true" title="Ajouter aux contacts"></i>
<% end %>
```

Au bas du fichier `_heading.html.erb`, affichez l'option pour ajouter l'utilisateur opposé de la conversation aux contacts :

```html
<%= render add_to_contacts_partial_path(@contact) %>
```

Définissez la méthode helper et les méthodes supplémentaires dans un scope privé :

```rb
# décider d'afficher une option ou non
def add_to_contacts_partial_path(contact)
  if recipient_is_contact? 
    'shared/empty_partial'
  else 
    non_contact(contact)
  end 
end

private

def recipient_is_contact?
  # vérifier si le destinataire est un contact de l'utilisateur
  contacts = current_user.all_active_contacts
  contacts.find {|contact| contact['id'] == @recipient.id}.present?
end

def non_contact(contact)
  # si la demande de contact a été envoyée par l'utilisateur ou le destinataire 
  if unaccepted_contact_exists(contact)
    'shared/empty_partial'
  else 
    # les demandes de contact n'ont été envoyées par aucun utilisateur 
    'private/conversations/conversation/heading/add_user_to_contacts' 
  end
end

def unaccepted_contact_exists(contact)
  # obtenir un statut de contact avec le destinataire
  if contact.present?
    # vérifier si un contact non accepté entre un utilisateur et un destinataire existe
    contact.accepted ? false : true
  else
    false
  end
end
```

Écrivez les specs pour ces méthodes helper :

```rb
context '#add_to_contacts_partial_path' do
  let(:contact) { create(:contact) }

  it "returns an empty partial's path" do
    helper.stub(:recipient_is_contact?).and_return(true)
    expect(helper.add_to_contacts_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end

  it "returns add_user_to_contacts partial's path" do
    helper.stub(:recipient_is_contact?).and_return(false)
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.add_to_contacts_partial_path(contact)).to eq(
      'private/conversations/conversation/heading/add_user_to_contacts' 
    )
  end
end

context 'private scope' do
  let(:current_user) { create(:user) }
  let(:recipient) { create(:user) }

  context '#unaccepted_contact_exists' do
    it 'returns false' do
      contact = create(:contact, accepted: true)
      expect(helper.instance_eval {
        unaccepted_contact_exists(contact)
      }).to eq false
    end

    it 'returns false' do
      contact = nil
      expect(helper.instance_eval {
        unaccepted_contact_exists(contact)
      }).to eq false
    end

    it 'returns true' do
      contact = create(:contact, accepted: false)
      expect(helper.instance_eval {
        unaccepted_contact_exists(contact)
      }).to eq true
    end
  end

  context '#recipient_is_contact?' do
    it 'returns false' do
      helper.stub(:current_user).and_return(current_user)
      assign(:recipient, recipient)
      create_list(:contact, 2, user_id: current_user.id, accepted: true)
      expect(helper.instance_eval { recipient_is_contact? }).to eq false
    end

    it 'returns true' do
      helper.stub(:current_user).and_return(current_user)
      assign(:recipient, recipient)
      create_list(:contact, 2, user_id: current_user.id, accepted: true)
      create(:contact, 
              user_id: current_user.id, 
              contact_id: recipient.id, 
              accepted: true)
      expect(helper.instance_eval { recipient_is_contact? }).to eq true
    end
  end
end
```

La méthode `instance_eval` est utilisée pour tester des méthodes dans un scope privé.

Comme nous allons afficher des options sur l'élément d'en-tête de la fenêtre de conversation, nous devons nous assurer que les options supplémentaires s'intègrent parfaitement sur l'en-tête. Dans le fichier `_heading.html.erb`, remplacez la classe `conversation-heading` par `<%= conv_heading_class(@contact) %>`, pour déterminer quelle classe ajouter.

Définissez la méthode helper :

```rb
# décider quel style d'en-tête de conversation afficher
def conv_heading_class(contact)
  # afficher un en-tête de conversation sans ou avec options
  if unaccepted_contact_exists(contact)
   'conversation-heading-full'
  else
   'conversation-heading'
  end
end
```

Écrivez les specs pour la méthode :

```rb
context '#conv_heading_class' do
  let(:contact) { create(:contact) }

  it 'returns a conversation-heading-full class' do
    contact.update(accepted: false)
    expect(helper.conv_heading_class(contact)).to eq 'conversation-heading-full'
  end

  it 'returns a conversation-heading class' do
    contact.update(accepted: true)
    expect(helper.conv_heading_class(contact)).to eq 'conversation-heading'
  end
end
```

Les options pour envoyer ou accepter une demande de contact ne seront pas encore affichées. D'autres éléments doivent être ajoutés. Ouvrez le fichier `_conversation.html.erb` :

```
private/conversations/_conversation.html.erb
```

En haut du fichier, définissez une variable d'instance `@contact`, afin qu'elle soit accessible dans tous les partiels :

```html
<% @contact = get_contact_record(@recipient) %>
```

Définissez la méthode helper `get_contact_record` :

```rb
def get_contact_record(recipient)
  contact = Contact.find_by_users(current_user.id, recipient.id)
end
```

Couvrez la méthode avec des specs :

```rb
context '#get_contact_record' do
  it 'returns a Contact record' do
    contact = create(:contact, user_id: current_user.id, contact_id: recipient.id)
    helper.stub(:current_user).and_return(current_user)
    expect(helper.get_contact_record(recipient)).to eq contact
  end
end
```

Précédemment, nous utilisions les méthodes `let` de `current_user` et `recipient` uniquement dans le contexte d'un scope privé. Maintenant, nous avons besoin d'y accéder à la fois sur les méthodes privées et publiques. Coupez-les et placez-les en dehors du contexte du scope privé.

En haut de l'élément `.panel-body`, affichez un fichier partiel qui montrera une fenêtre de message supplémentaire pour accepter ou refuser une demande de contact :

```html
<%= render 'private/conversations/conversation/request_status' %>
```

Créez le fichier `_request_status.html.erb` :

```html
<%= render unaccepted_contact_request_partial_path(@contact) %>
<%= render not_contact_no_request_partial_path(@contact) %>
```

Définissez les méthodes helper nécessaires :

```rb
# afficher le statut d'une demande de contact non acceptée, le cas échéant
def unaccepted_contact_request_partial_path(contact)
  if unaccepted_contact_exists(contact) 
    if request_sent_by_user(contact)
      "private/conversations/conversation/request_status/sent_by_current_user"  
    else
      "private/conversations/conversation/request_status/sent_by_recipient" 
    end
  else
    'shared/empty_partial'
  end
end

# afficher un lien pour envoyer une demande de contact
# si l'utilisateur opposé n'est pas dans les contacts et qu'aucune demande n'existe
def not_contact_no_request_partial_path(contact)
  if recipient_is_contact? == false && unaccepted_contact_exists(contact) == false
    "private/conversations/conversation/request_status/send_request"
  else
    'shared/empty_partial'
  end
end

private

def request_sent_by_user(contact)
  # vrai si la demande de contact a été envoyée par current_user 
  # faux si elle a été envoyée par un destinataire
  contact['user_id'] == current_user.id
end
```

Écrivez les specs pour les méthodes helper :

```rb
context '#unaccepted_contact_request_partial_path' do
  let(:contact) { contact = create(:contact) }

  it "returns sent_by_current_user partial's path" do
    helper.stub(:unaccepted_contact_exists).and_return(true)
    helper.stub(:request_sent_by_user).and_return(true)
    expect(helper.unaccepted_contact_request_partial_path(contact)).to eq(
      'private/conversations/conversation/request_status/sent_by_current_user' 
    )
  end

  it "returns sent_by_recipient partial's path" do
    helper.stub(:unaccepted_contact_exists).and_return(true)
    helper.stub(:request_sent_by_user).and_return(false)
    expect(helper.unaccepted_contact_request_partial_path(contact)).to eq(
      'private/conversations/conversation/request_status/sent_by_recipient'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.unaccepted_contact_request_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end
end

context '#not_contact_no_request' do
  let(:contact) { contact = create(:contact) }

  it "returns send_request partial's path" do
    helper.stub(:recipient_is_contact?).and_return(false)
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.not_contact_no_request_partial_path(contact)).to eq(
      'private/conversations/conversation/request_status/send_request'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:recipient_is_contact?).and_return(true)
    helper.stub(:unaccepted_contact_exists).and_return(false)
    expect(helper.not_contact_no_request_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end

  it "returns an empty partial's path" do
    helper.stub(:recipient_is_contact?).and_return(false)
    helper.stub(:unaccepted_contact_exists).and_return(true)
    expect(helper.not_contact_no_request_partial_path(contact)).to eq(
      'shared/empty_partial'
    )
  end
end

context 'private scope' do
  context '#request_sent_by_user' do
    it 'returns true' do
      contact = create(:contact, user_id: current_user.id)
      helper.stub(:current_user).and_return(current_user)
      expect(helper.instance_eval { request_sent_by_user(contact) }).to eq true
    end

    it 'returns false' do
      contact = create(:contact, user_id: recipient.id)
      helper.stub(:current_user).and_return(current_user)
      expect(helper.instance_eval { request_sent_by_user(contact) }).to eq false
    end
  end
end
```

Créez le répertoire `request_status` puis créez les fichiers partiels `_send_request.html.erb`, `_sent_by_current_user.html.erb` et `_sent_by_recipient.html.erb` :

```html
<div class="contact-request-status">
  <div class="add-user-to-contacts-message">
    <div>
      <%= @recipient.name %> n'est pas dans vos contacts
    </div>
    <div>
      <%= link_to "Ajouter aux contacts", 
                  contacts_path(contact_id: @recipient), 
                  remote: true, 
                  method: :post, 
                  class: 'add-user-to-contacts-notif' %>
    </div>
  </div>   
</div>
```

```html
<div class="contact-request-status">
  <div class="pending-request">
    La demande de contact est en attente
  </div>
</div>
```

```html
<div class="contact-request-status" 
     data-user-name="<%= @recipient.name %>">
  <div class="contact-name">
    <%= @recipient.name %> vous a envoyé une demande de contact
  </div>
  <div class="request-response">
    <span class="accept-request">
      <%= link_to "Accepter",  
          contact_path(id: @recipient.id), 
          remote: true, 
          method: "put" %>
    </span>  
    <span class="decline-request">
      <%= link_to "Refuser", 
                  contact_path(id: @recipient.id), 
                  remote: true, 
                  method: :delete %>
    </span>              
  </div>
</div>
```

Validez les modifications :

```bash
git add -A
git commit -m "Ajouter un bouton sur la fenêtre de conversation privée
pour ajouter un destinataire aux contacts"
```

Implémentez les changements de design et réglez les problèmes de style qui apparaissent en raison des éléments supplémentaires sur la fenêtre de conversation. Ajoutez du CSS au fichier `conversation_window.scss` :

```scss
.add-user-to-contacts {
  display: none;
  i {
    opacity: 0.8;
    &:hover {
      opacity: 1;
    }
  }
  &:hover {
    color: white;
  }
}

.add-user-to-contacts-message {
  text-align: center;
  padding: 10px 0;
}

.add-people-to-chat, .contact-request-sent {
  display: none;
  margin: 0;
  padding: 0;
  div {
    width: 40px;
    height: 40px;
    display: table;
    i {
      display: table-cell;
      text-align: center;
      vertical-align: middle;
    }
  }
}

.add-people-to-chat {
  i {
    opacity: 0.8;
    transition: opacity 0.15s;
  }
  &:hover i {
    opacity: 1;
  }
}

.contact-request-status {
  position: relative;
  left: 0;
  top: 0;
  width: 400px;
  text-align: center;
  background-color: white;
  z-index: 2;
  .pending-request {
    padding: 10px 0;
  }
  .request-response {
    padding: 10px 0;
  }
  .accept-request, .decline-request {
    a {
      padding: 10px 0;
    }
  }
  .contact-name {
    padding: 10px 0 0 0;
  }
  .accept-request {
    margin-right: 10px;
    a {
      color: green;
    }
  }
  .decline-request {
    a {
      font-weight: bold;
      color: red;
    }
  }
}
```

Validez les modifications :

```bash
git add -A
git commit -m "Ajouter du CSS à conversation_window.scss pour styliser les boutons d'option"
```

Lorsqu'une fenêtre de conversation est réduite, il serait préférable de ne voir aucune option. C'est un design plus pratique de ne voir les options que lorsque la fenêtre de conversation est agrandie. Pour y parvenir, dans la fonction toggle du fichier `toggle_window.js`, juste en dessous de la variable `messages_visible`, ajoutez :

```js
// si la fenêtre est réduite, masquer les options du menu de conversation
if ( panel_body.css('display') == 'none' ) {
    panel.find('.add-people-to-chat,\
                .add-user-to-contacts,\
                .contact-request-sent').hide();
    conversation_heading = panel.find('.conversation-heading');
    conversation_heading.css('width', '360px');

} else { // afficher les options du menu de conversation
    conversation_heading = panel.find('.conversation-heading');
    conversation_heading.css('width', '320px');
    panel.find('.add-people-to-chat,\
                .add-user-to-contacts,\
                .contact-request-sent').show();
    // focus textarea
    $('form textarea', this).focus();
}
```

Maintenant, la fenêtre réduite ressemble à ceci, elle n'a plus d'options visibles :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-106.png)

La fenêtre agrandie a une option pour ajouter un utilisateur aux contacts. Il y a aussi un message qui suggère de le faire :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-107.png)

En fait, vous pouvez envoyer et accepter une demande de contact dès maintenant en cliquant sur une icône dans l'en-tête de la conversation ou en cliquant sur le lien `Ajouter aux contacts`. Pour l'instant, il n'y a aucune réponse après avoir cliqué sur ces liens et boutons. Nous ajouterons un retour d'information et un système de notification en temps réel un peu plus tard. Mais techniquement, vous pouvez ajouter des utilisateurs à vos contacts, ce n'est juste pas encore très convivial.

Après avoir envoyé une demande de contact, le côté de l'utilisateur opposé ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-108.png)

Validez les modifications :

```bash
git add -A
git commit -m "Ajouter du JS dans toggle_window.js pour afficher et masquer les options supplémentaires"
```

#### Actuellement, les utilisateurs peuvent discuter en privé, avoir des conversations en tête-à-tête. Comme l'application est axée sur la collaboration, il serait logique d'avoir également des conversations de groupe.

Commencez par générer un nouveau modèle :

```
rails g model group/conversation
```

Plusieurs utilisateurs pourront participer à une même conversation. Définissez les associations et la table de base de données :

```rb
class Group::Conversation < ApplicationRecord
  self.table_name = 'group_conversations'
  
  has_and_belongs_to_many :users
  has_many :messages, 
           class_name: "Group::Message",
           foreign_key: 'conversation_id', 
           dependent: :destroy
end
```

```rb
has_many :group_messages, class_name: 'Group::Message'
has_and_belongs_to_many :group_conversations, class_name: 'Group::Conversation'
```

Une [table de jointure](http://guides.rubyonrails.org/active_record_migrations.html#creating-a-join-table) va être utilisée pour suivre qui appartient à quelle conversation de groupe.

Ensuite, générez un modèle pour les messages :

```bash
rails g model group/message
```

```rb
class Group::Message < ApplicationRecord
  serialize :seen_by, Array
  serialize :added_new_users, Array
  self.table_name = "group_messages"

  belongs_to  :conversation,
              class_name: 'Group::Conversation',
              foreign_key: 'conversation_id'
  belongs_to :user

  validates :content, presence: true
  validates :user_id, presence: true
  validates :conversation_id, presence: true

  default_scope { includes(:user) }

  # obtenir un message précédent d'une conversation
  def previous_message
    previous_message_index = self.conversation.messages.index(self) - 1
    self.conversation.messages[previous_message_index]
  end
end
```

Nous stockerons les IDs des utilisateurs ayant vu un message dans un tableau. Pour créer et gérer des objets, tels qu'un tableau, à l'intérieur d'une colonne de base de données, une méthode `serialize` est utilisée. Un scope par défaut, pour minimiser le nombre de requêtes, et quelques validations sont ajoutés.

La façon dont nous construisons les conversations de groupe est assez similaire aux conversations privées. En fait, le style et certaines parties seront communs aux deux types de conversations.

Écrivez les specs pour les modèles. De plus, une factory pour les messages de groupe sera nécessaire :

```rb
FactoryGirl.define do 
  factory :group_message, class: 'Group::Message' do
    content 'a' * 20
    association :conversation, factory: :group_conversation
    user
  end
end
```

```rb
it 'has_many group_messages' do 
  association = described_class.reflect_on_association(:group_messages)
  expect(association.macro).to eq :has_many
  expect(association.options[:class_name]).to eq 'Group::Message'
end

it 'has_and_belongs_to_many group_conversations' do
  association = described_class.reflect_on_association(:group_conversations)
  expect(association.macro).to eq :has_and_belongs_to_many
  expect(association.options[:class_name]).to eq 'Group::Conversation'
end
```

```rb
require 'rails_helper'

RSpec.describe Group::Conversation, type: :model do
```
  let(:conversation) { build(:group_conversation) }

  context 'Associations' do
    it 'has_and_belongs_to_many users' do
      association = described_class.reflect_on_association(:users)
      expect(association.macro).to eq :has_and_belongs_to_many
    end

    it 'has_many messages' do
      association = described_class.reflect_on_association(:messages)
      expect(association.macro).to eq :has_many
      expect(association.options[:class_name]).to eq 'Group::Message'
      expect(association.options[:foreign_key]).to eq 'conversation_id'
      expect(association.options[:dependent]).to eq :destroy
    end
  end

end
```

```rb
require 'rails_helper'

RSpec.describe Group::Message, type: :model do

  let(:message) { build(:group_message) }

  context 'Associations' do
    it 'belongs_to group_conversation' do
      association = described_class.reflect_on_association(:conversation)
      expect(association.macro).to eq :belongs_to
      expect(association.options[:class_name]).to eq 'Group::Conversation'
      expect(association.options[:foreign_key]).to eq 'conversation_id'
    end
  end

  context 'Validations' do
    it "is not valid without a content" do 
      message.content = nil
      expect(message).not_to be_valid 
    end

    it "is not valid without a conversation_id" do 
      message.conversation_id = nil
      expect(message).not_to be_valid 
    end

    it "is not valid without a user_id" do 
      message.user_id = nil
      expect(message).not_to be_valid 
    end
  end

  context 'Methods' do
    it 'gets a previous message of a conversation' do
      conversation = create(:group_conversation)
      message1 = create(:group_message, conversation_id: conversation.id)
      message2 = create(:group_message, conversation_id: conversation.id)
      expect(message2.previous_message).to eq message1
    end
  end
 
end
```

Définissez les fichiers de migration

```rb
class CreateGroupConversations < ActiveRecord::Migration[5.1]
  def change
    create_table :group_conversations do |t|
      t.string :name
      t.timestamps
    end
  end
end
```

```rb
class CreateGroupConversationsUsersJoinTable < ActiveRecord::Migration[5.1]
  def change
    create_table :group_conversations_users, id: false do |t|
      t.integer :conversation_id
      t.integer :user_id
    end
    add_index :group_conversations_users, :conversation_id
    add_index :group_conversations_users, :user_id
  end
end
```

```rb
class CreateGroupMessages < ActiveRecord::Migration[5.1]
  def change
    create_table :group_messages do |t|
      t.string :content
      t.string :added_new_users
      t.string :seen_by
      t.belongs_to :user, index: true
      t.belongs_to :conversation, index: true
      t.timestamps
    end
  end
end
```

Les bases de la conversation de groupe sont posées.

Commitez les changements

```bash
git add -A
git commit -m "Create Group::Conversation and Group::Message models
- Define associations
- Write specs"
```

**Créer une conversation de groupe**

Comme mentionné précédemment, le processus de création de la fonctionnalité de conversation de groupe sera similaire à ce que nous avons fait pour la conversation privée. Commencez par créer un contrôleur et une interface utilisateur de base.

Générez un contrôleur avec espace de noms

```bash
rails g controller group/conversations
```

À l'intérieur du contrôleur, définissez une action `create` et les méthodes privées `add_to_conversations`, `already_added?` et `create_group_conversation` :

```rb
class Group::ConversationsController < ApplicationController

  def create
    @conversation = create_group_conversation
    add_to_conversations unless already_added?

    respond_to do |format|
      format.js
    end
  end
  
  private

  def add_to_conversations
    session[:group_conversations] ||= []
    session[:group_conversations] << @conversation.id
  end
 
  def already_added?
    session[:group_conversations].include?(@conversation.id)
  end

  def create_group_conversation
    Group::NewConversationService.new({
      creator_id: params[:creator_id],
      private_conversation_id: params[:private_conversation_id],
      new_user_id: params[:group_conversation][:id]
    }).call
  end
  
end
```

La création d'une nouvelle conversation de groupe implique une certaine complexité, nous allons donc l'extraire dans un objet service. Ensuite, nous avons les méthodes privées `add_to_conversations` et `already_added?`. Si vous vous souvenez, nous les avons également dans le `Private::ConversationsController`, mais cette fois, elles stockent les IDs des conversations de groupe dans la session.

Maintenant, définissez le `Group::NewConversationService` dans un nouveau répertoire `group` :

```rb
class Group::NewConversationService

  def initialize(params)
    @creator_id = params[:creator_id]
    @private_conversation_id = params[:private_conversation_id]
    @new_user_id = params[:new_user_id]
  end

  def call
    creator = User.find(@creator_id)
    pchat_opposed_user = Private::Conversation.find(@private_conversation_id)
                           .opposed_user(creator)
    new_user_to_chat = User.find(@new_user_id)
    new_group_conversation = Group::Conversation.new
    new_group_conversation.name = '' + creator.name + ', ' + 
                                  pchat_opposed_user.name + ', ' + 
                                  new_user_to_chat.name 
    if new_group_conversation.save
      arr_of_users_ids = [creator.id, pchat_opposed_user.id, new_user_to_chat.id]
      # ajouter les utilisateurs à la conversation
      creator.group_conversations << new_group_conversation
      pchat_opposed_user.group_conversations << new_group_conversation
      new_user_to_chat.group_conversations << new_group_conversation
      # créer un message initial avec des informations sur la conversation
      create_initial_message(creator, arr_of_users_ids, new_group_conversation)
      # retourner la conversation
      new_group_conversation
    end
  end

  private

  def create_initial_message(creator, arr_of_users_ids, new_group_conversation)
    message = Group::Message.create(
      user_id: creator.id, 
      content: 'Conversation created by ' + creator.name, 
      added_new_users: arr_of_users_ids , 
      conversation_id: new_group_conversation.id
    )
  end
end
```

La création d'une nouvelle conversation de groupe se fera en réalité via une conversation privée. Nous créerons bientôt cette interface comme une option sur la fenêtre de conversation privée. Avant cela, assurez-vous que l'objet service fonctionne correctement en le couvrant avec des specs. Dans `services`, créez un nouveau répertoire `group` avec un fichier `new_conversation_service_spec.rb` à l'intérieur :

```rb
require 'rails_helper'
require './app/services/group/new_conversation_service.rb'

describe Group::NewConversationService do
  let(:user1) { create(:user) }
  let(:user2) { create(:user) }
  let(:new_user) { create(:user) }
  let(:private_conversation) { create(:private_conversation,
                                       sender_id: user1.id,
                                       recipient_id: user2.id) }
  context '#call' do
    it 'returns a new created group conversation' do
      new_conversation = Group::NewConversationService.new({
                           creator_id: user1.id,
                           private_conversation_id: private_conversation.id,
                           new_user_id: new_user.id
                         }).call
      last_conversation = Group::Conversation.last
      expect(new_conversation).to eq last_conversation
      expect(last_conversation.messages.count).to eq 1
    end
  end
end
```

Commitez les changements

```bash
git add -A
git commit -m "Create back-end for creating a new group conversation
- Create a Group::ConversationsController
  Define a create action and add_to_conversations, 
  create_group_conversation and already_added? private methods inside
- Create a  Group::NewConversationService and write specs for it"
```

Définissez les routes pour la conversation de groupe et ses messages

```rb
namespace :group do 
  resources :conversations do
    member do
      post :close
      post :open
    end
  end
  resources :messages, only: [:index, :create]
end
```

Commitez les changements

```bash
git add -A
git commit -m "Define specs for Group::Conversations and Messages"
```

Actuellement, nous ne gérons que les conversations privées dans l'`ApplicationController`. Seules les conversations privées sont ordonnées et seuls leurs IDs, après qu'un utilisateur les a ouvertes, sont disponibles dans toute l'application. Dans l'`ApplicationController`, mettez à jour la méthode `opened_conversations_windows` :

```rb
def opened_conversations_windows
  if user_signed_in?
    # conversations ouvertes
    session[:private_conversations] ||= []
    session[:group_conversations] ||= []
    @private_conversations_windows = Private::Conversation.includes(:recipient, :messages)
                                         .find(session[:private_conversations])
    @group_conversations_windows = Group::Conversation.find(session[:group_conversations])
  else
    @private_conversations_windows = []
    @group_conversations_windows = []
  end
end
```

Comme l'ordonnancement des conversations se fait à l'aide de l'`OrderConversationsService`, nous devons mettre à jour ce service :

```rb
# récupérer et ordonner les conversations par date des derniers messages par ordre décroissant
def call
  all_private_conversations = Private::Conversation.all_by_user(@user.id)
                                                   .includes(:messages)
  all_group_conversations = @user.group_conversations.includes(:messages)
  all_conversations = all_private_conversations + all_group_conversations

  return all_conversations = all_conversations.sort{ |a, b| 
    b.messages.last.created_at <=> a.messages.last.created_at
  }
end
```

Auparavant, nous n'avions que le tableau des conversations privées et nous le triions par date de création des derniers messages. Maintenant, nous avons des tableaux de conversations privées et de groupe, puis nous les fusionnons en un seul tableau et le trions de la même manière qu'avant.

Mettez également à jour les specs :

```rb
describe OrderConversationsService do
  context '#call' do
    it 'returns ordered conversations in descending order' do
      user = create(:user)
      conversation1 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversation2 = create(:group_conversation,
                              users: [user],
                              messages: [create(:group_message)])
      conversation3 = create(:private_conversation,
                              sender_id: user.id,
                              messages: [create(:private_message)])
      conversations = [conversation3, conversation2, conversation1]
      expect(OrderConversationsService.new({user: user}).call).to eq conversations
    end
  end
end
```

Commitez les changements

```bash
git add -A
git commit -m "Get data for group conversations in ApplicationController
- Update the opened_conversations_windows method
- Update the OrderConversationsService"
```

Dans un instant, nous devrons passer des données d'un contrôleur à JavaScript. Heureusement, nous avons déjà installé la gem `gon`, qui nous permet de le faire facilement. Dans l'`ApplicationController`, dans une portée `private`, ajoutez :

```rb
def set_user_data
  if user_signed_in?
    gon.group_conversations = current_user.group_conversations.ids
    gon.user_id = current_user.id
    cookies[:user_id] = current_user.id if current_user.present?
    cookies[:group_conversations] = current_user.group_conversations.ids
  else
    gon.group_conversations = []
  end
end
```

Utilisez le filtre `before_action` pour appeler cette méthode :

```rb
before_action :set_user_data
```

Commitez les changements

```bash
git add -A
git commit -m "Define a set_user_data private method in ApplicationController"
```

Techniquement, nous pouvons maintenant créer une nouvelle conversation de groupe, mais les utilisateurs n'ont pas d'interface pour le faire. Comme mentionné, ils le feront via une conversation privée. Créons cette option sur la fenêtre de conversation privée.

Dans le répertoire

```bash
views/private/conversations/conversation/heading
```

créez un nouveau fichier :

```html
<!-- Bouton pour ajouter plus de contacts au chat -->
<div class="add-people-to-chat" title="Create a group chat">
  <div>
    <i class="fa fa-plus" aria-hidden="true" data-toggle="dropdown"></i>
  </div>
</div>
<!-- sélection des utilisateurs à ajouter à la conversation -->
<div class="select-users-to-chat">
  <%= form_for(Group::Conversation.new, remote: true, class: 'form-group') do |f| %>
    <%= hidden_field_tag :creator_id, current_user.id %>
    <%= hidden_field_tag :private_conversation_id, conversation.id %>
    <%= f.collection_select(:id, 
                            contacts_except_recipient(@recipient), 
                            :id, 
                            :name, 
                            {}, 
                            {:class=>'form-control select-users-dropdown'}) %>
    <%= f.submit 'Start a conversation', class: 'form-control select-users-button' %>
  <% end %>
</div>
```

Une méthode `[collection_select](https://apidock.com/rails/ActionView/Helpers/FormOptionsHelper/collection_select)` est utilisée pour afficher une liste d'utilisateurs. Seuls les utilisateurs figurant dans les contacts seront inclus dans la liste. Définissez la méthode helper `contacts_except_recipient` :

```rb
def contacts_except_recipient(recipient)
  contacts = current_user.all_active_contacts
  # retourner tous les contacts, sauf l'autre utilisateur du chat
  contacts.delete_if {|contact| contact.id == recipient.id }
end
```

Écrivez les specs pour la méthode :

```rb
context '#contacts_except_recipient' do
  it 'return all contacts, except the opposite user of the chat' do
    contacts = create_list(:contact, 
                            5, 
                            user_id: current_user.id, 
                            accepted: true)

    contacts << create(:contact, 
                        user_id: current_user.id, 
                        contact_id: recipient.id,
                        accepted: true)
    helper.stub(:current_user).and_return(current_user)
    expect(helper.contacts_except_recipient(recipient)).not_to include recipient
  end
end
```

Rendez le partial au bas de `_heading.html.erb` :

```html
<%= render create_group_conv_partial_path, conversation: conversation %>
```

Définissez la méthode helper :

```rb
def create_group_conv_partial_path(contact)
  if recipient_is_contact?
    'private/conversations/conversation/heading/create_group_conversation'
  else
    'shared/empty_partial'
  end
end
```

Couvrez-la avec des specs :

```rb
context '#create_group_conv_partial_path' do
  let(:contact) { create(:contact) }

  it "returns a create_group_conversation partial's path" do 
    helper.stub(:recipient_is_contact?).and_return(true)
    expect(helper.create_group_conv_partial_path(contact)).to(
      eq 'private/conversations/conversation/heading/create_group_conversation'
    )
  end

  it "returns an empty partial's path" do 
    helper.stub(:recipient_is_contact?).and_return(false)
    expect(helper.create_group_conv_partial_path(contact)).to(
      eq 'shared/empty_partial'
    )
  end
end
```

Commitez les changements.

```bash
git add -A
git commit -m "Add a UI on private conversation to create a group conversations"
```

Ajoutez du CSS pour styliser le composant qui permet de créer une nouvelle conversation de groupe :

```scss
.select-users-to-chat {
  padding: 5px 0 5px 5px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 40px;
  background-color: white;
  display: none;
  height: 45px;
  width: 100%;
  z-index: 2;
}

.select-users-dropdown, .select-users-button {
  border: none;
  display: inline-block;
  margin: 0;
  height: 35px;
}

.select-users-dropdown {
  width: 55%;
  border: 1px solid rgba(0, 0, 0, 0.2);
}

.select-users-button {
  width: 40%;
  background-color: $navbarColor;
  color: white;
  border: 1px solid $navbarColor;
}
```

Une sélection de contacts est masquée par défaut. Pour ouvrir la sélection, un utilisateur doit cliquer sur le bouton. Le bouton n'est pas encore interactif. Créez un fichier `options.js` avec du JavaScript à l'intérieur pour rendre la liste de sélection basculable.

```js
$(document).on('turbolinks:load', function() { 

  // quand le bouton d'ajout de contacts à une conversation est cliqué
  // basculer la sélection des contacts
  $('body').on('click', '.add-people-to-chat', function(e) {
      $(this).next().toggle(100, 'swing');
  });

});
```

Désormais, une fenêtre de conversation avec un destinataire qui est un contact ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-109.png)

Il y a un bouton qui ouvre une liste de contacts avec lesquels vous pouvez créer une conversation de groupe lorsque vous cliquez dessus :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-110.png)

Commitez les changements.

```bash
git add -A
git commit -m "
- Describe style for the create a group conversation option
- Make the option toggleable"
```

Nous avons maintenant une liste de conversations ordonnées, incluant les conversations de groupe, qui seront affichées dans le menu déroulant de la barre de navigation. Si vous vous souvenez, nous avons spécifié différents partials pour différents types de conversations. Lorsque l'application tente de rendre un lien pour ouvrir une conversation de groupe, elle cherchera un fichier différent de celui d'une conversation privée. Le fichier n'est pas encore créé.

Créez un fichier `_group.html.erb` :

```html
<% seen_status = group_conv_seen_status(conversation, current_user) %>
<li id="menu-gc<%= conversation.id %>" class="<%= seen_status %>">
  <%= link_to truncate(conversation.name, :length => 40), 
              open_group_conversation_path(id: conversation.id), 
              remote: true, 
              method: :post, 
              class: 'bigger-screen-link' %>
</li>
```

Définissez la méthode helper `group_conv_seen_status` à l'intérieur de `Shared::ConversationsHelper` :

```rb
def group_conv_seen_status(conversation, current_user)
  # si current_user est nil, cela signifie que le helper est appelé depuis le service
  # retourner une chaîne vide
  if current_user == nil
    ''
  else
    # si le dernier message de la conversation n'est pas créé par cet utilisateur
    # et n'est pas vu, retourner une valeur unseen-conv
    not_created_by_user = conversation.messages.last.user_id != current_user.id
    seen_by_user = conversation.messages.last.seen_by.include? current_user.id
    not_created_by_user && seen_by_user == false ? 'unseen-conv' : ''
  end
end
```

Écrivez les specs pour la méthode :

```rb
context '#group_conv_seen_status' do
  it 'returns unseen-conv status' do
    conversation = create(:group_conversation)
    create(:group_message, conversation_id: conversation.id)
    current_user = create(:user)
    view.stub(:current_user).and_return(current_user)
    expect(helper.group_conv_seen_status(conversation)).to eq(
      'unseen-conv'
    )
  end

  it 'returns an empty string' do
    user = create(:user)
    conversation = create(:group_conversation)
    create(:group_message, conversation_id: conversation.id, user_id: user.id)
    view.stub(:current_user).and_return(user)
    expect(helper.group_conv_seen_status(conversation)).to eq ''
  end

  it 'returns an empty string' do
    user = create(:user)
    conversation = create(:group_conversation)
    message = build(:group_message, conversation_id: conversation.id)
    message.seen_by << user.id
    message.save
    view.stub(:current_user).and_return(user)
    expect(helper.group_conv_seen_status(conversation)).to eq ''
  end
end
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a link on the navigation bar to open a group conversation"
```

Rendez les fenêtres de conversations de groupe sur l'application, de la même manière que nous avons rendu les conversations privées. Dans `application.html.erb`, juste en dessous des conversations privées rendues, ajoutez :

```html
<%= render 'layouts/application/group_conversations_windows' %>
```

Créez le fichier partial pour rendre les fenêtres de conversations de groupe une par une :

```html
<% @group_conversations_windows.each do |conversation| %>
  <%= render partial: "group/conversations/conversation",
            locals: { conversation: conversation, 
                      user: current_user } %>
<% end %>
```

Commitez le changement.

```bash 
git add -A
git commit -m "Render group conversations' windows inside the
application.html.erb"
```

Nous avons un mécanisme pour créer et rendre les conversations de groupe sur l'application. Maintenant, construisons la fenêtre de conversation elle-même.

Dans le répertoire `group/conversations`, créez un fichier `_conversation.html.erb`.

```html
<% add_people_to_conv_list = add_people_to_group_conv_list(conversation) %>
<% @is_messenger = false %>
<li class="conversation-window" id="gc<%= conversation.id %>" data-turbolinks-permanent>
  <div class="panel panel-default" data-gconversation-id="<%= conversation.id %>">
    <%= render  'group/conversations/conversation/heading',
                conversation: conversation %> 
    <%= render  'group/conversations/conversation/select_users',
                conversation: conversation,
                add_people_to_conv_list: add_people_to_conv_list %>
    <div class="panel-body">
      <%= render  'group/conversations/conversation/messages_list',
                  conversation: conversation %>
      <%= render  'group/conversations/conversation/new_message_form',
                  conversation: conversation,
                  user: user %> 
    </div><!-- panel-body -->
  </div><!-- panel -->
</li>
```

Définissez la méthode helper `add_people_to_group_conv_list` :

```rb
module Group::ConversationsHelper
  def add_people_to_group_conv_list(conversation)
    contacts = current_user.all_active_contacts
    users_in_conv = conversation.users
    add_people_to_conv_list = []
    contacts.each do |contact|
      # si le contact est déjà dans la conversation, le retirer de la liste
      if !users_in_conv.include?(contact)
        add_people_to_conv_list << contact
      end
    end
    add_people_to_conv_list
  end
end
```

Écrivez les specs pour le helper :

```rb
context '#add_people_to_group_conv_list' do
  let(:conversation) { create(:group_conversation) }
  let(:current_user) { create(:user) }
  let(:user) { create(:user) }
  before(:each) do
    create(:contact, 
            user_id: current_user.id, 
            contact_id: user.id,
            accepted: true)
  end

  it 'a user is not included in a list' do
    conversation.users << current_user
    conversation.users << user
    helper.stub(:current_user).and_return(current_user)
    expect(helper.add_people_to_group_conv_list(conversation)).not_to include user
  end

  it 'a user is included in a list' do
    conversation.users << current_user
    helper.stub(:current_user).and_return(current_user)
    expect(helper.add_people_to_group_conv_list(conversation)).to include user
  end
end
```

Tout comme pour les conversations privées, les conversations de groupe seront accessibles dans toute l'application, donc évidemment, nous avons également besoin d'accéder aux méthodes du `Group::ConversationsHelper` partout. Ajoutez ce module dans l'`ApplicationHelper` :

```rb
include Group::ConversationsHelper
```

Commitez les changements.

```bash
git add -A
git commit -m "
- Create a _conversation.html.erb inside the group/conversations
- Define a add_people_to_group_conv_list and write specs for it"
```

Créez un nouveau répertoire `conversation` avec un fichier `_heading.html.erb` à l'intérieur :

```html
<div class="panel-heading conversation-heading">
  <%= truncate(conversation.name, :length => 40) %>
</div>

<!-- Bouton de fermeture de la conversation -->
<%= link_to "X", 
            close_group_conversation_path(conversation), 
            class: 'close-conversation', 
            title: 'Close', 
            remote: true, 
            method: :post %>

<!-- Bouton pour ajouter plus de contacts à la conversation -->
<div class="add-people-to-chat" title="Add people to chat">
  <div>
    <i class="fa fa-plus" aria-hidden="true" data-toggle="dropdown"></i>
  </div>
</div>
```

Commitez le changement.

```bash
git add -A
git commit -m "Create a _heading.html.erb inside the
group/conversations/conversation"
```

Ensuite, nous avons les fichiers partials `_select_user.html.erb` et `_messages_list.html.erb`. Créez-les :

```html
<div class="select-users-to-chat">
  <%= form_tag  group_conversation_path(conversation), 
                method: 'put', 
                class: 'form-group' do %>
    <%= hidden_field_tag :added_by, current_user.id %>
    <%= collection_select(:user, 
                          :id, 
                          add_people_to_conv_list, 
                          :id, 
                          :name, 
                          {}, 
                          {:class=>'form-control select-users-dropdown'}) %>
    <%= submit_tag 'Add the user', class: 'form-control select-users-button' %>
  <% end %>
</div>
```

```html
<div class="messages-list">
  <%= render partial: load_group_messages_partial_path(conversation),
             locals: { conversation: conversation, messenger_boolean: false } %>
  <div class="loading-more-messages">
    <i class="fa fa-spinner" aria-hidden="true"></i>
  </div>
  <!-- messages -->
  <ul>
  </ul>
</div>
```

Définissez la méthode helper `load_group_messages_partial_path` :

```rb
def load_group_messages_partial_path(conversation)
  if conversation.messages.count > 0
    'group/conversations/conversation/messages_list/load_messages'
  else
    'shared/empty_partial'
  end
end
```

Couvrez-la avec des specs :

```rb
context '#load_group_messages_partial_path' do
  let(:conversation) { create(:group_conversation) }
  it "returns load_messages partial's path" do
    create_list(:group_message, 2, conversation_id: conversation.id)
    expect(helper.load_group_messages_partial_path(conversation)).to eq(
      'group/conversations/conversation/messages_list/link_to_previous_messages'
    )
  end

  it "returns an empty partial's path" do
    expect(helper.load_group_messages_partial_path(conversation)).to eq(
      'shared/empty_partial'
    )
  end
end
```

Commitez les changements.

```bash
git add -A
git commit -m "
- Create _select_user.html.erb and _messages_list.html.erb inside
  group/conversations/conversation
- Define a load_group_messages_partial_path helper method 
  and write specs for it"
```

Créez un fichier `_link_to_previous_messages.html.erb`, pour avoir un lien qui charge les messages précédents :

```html
<%= link_to "Load messages", 
            group_messages_path(:conversation_id => conversation.id, 
                                :messages_to_display_offset => @messages_to_display_offset,
                                :is_messenger => @is_messenger), 
            class: 'load-more-messages', 
            remote: true %>
```

Commitez le changement.

```bash
git add -A
git commit -m "Create a _load_messages.html.erb inside the
group/conversations/conversation/messages_list"
```

Créez un formulaire de nouveau message :

```html
<form class="send-group-message">
  <input  name="conversation_id" 
          type="hidden" 
          value="<%= conversation.id %>">
  <input  name="user_id" 
          type="hidden" 
          value="<%= user.id %>">
  <textarea name="content" 
            rows="3" 
            class="form-control" 
            placeholder="Type a message..."></textarea>
  <input type="submit" class="btn btn-success send-message">
</form>
```

Commitez le changement.

```bash
git add -A
git commit -m "Create a _new_message_form.html.erb inside the 
group/conversations/conversation/"
```

L'application est maintenant capable de rendre également les fenêtres de conversations de groupe.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-111.png)

Mais elles ne sont pas encore fonctionnelles. Tout d'abord, nous devons charger les messages. Nous avons besoin d'un contrôleur pour les messages et de vues. Générez un contrôleur `Messages` :

```bash
rails g controller group/messages
```

Incluez le module `Messages` des `concerns` et définissez une action `index` :

```rb
class Group::MessagesController < ApplicationController
  include Messages
  
  def index
    get_messages('group', 15)
    @user = current_user
    @is_messenger = params[:is_messenger]
    respond_to do |format|
      format.js { render partial: 'group/messages/load_more_messages' }
    end
  end
end
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a Group::MessagesController and define an index action"
```

Créez un fichier `_load_more_messages.js.erb` :

```js
<% @id_type = 'gc' %>
<%= render append_previous_messages_partial_path %>
<%= render replace_link_to_group_messages_partial_path %>
<%= render remove_link_to_messages %>
```

Nous avons déjà défini les méthodes helper `append_previous_messages_partial_path` et `remove_link_to_messages` plus tôt. Il ne nous reste plus qu'à définir la méthode helper `replace_link_to_group_messages_partial_path` :

```rb
def replace_link_to_group_messages_partial_path
  'group/messages/load_more_messages/window/replace_link_to_messages'   
end 
```

Encore une fois, cette méthode, tout comme du côté privé, va devenir plus "intelligente" une fois que nous aurons développé le messenger.

Créez le fichier `_replace_link_to_messages.js.erb` :

```js
$('#<%= @id_type %><%= @conversation.id %> .load-more-messages')
    .replaceWith('\
        <%= j render partial: "group/conversations/conversation/messages_list/link_to_previous_messages",\
                     locals: { conversation: @conversation } %>\
        ');
```

Ajoutez également le `Group::MessagesHelper` à l'`ApplicationHelper` :

```rb
include Group::MessagesHelper
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a _load_more_messages.js.erb inside the group/messages"
```

La seule façon d'ouvrir des conversations de groupe pour le moment est après leur initialisation. Évidemment, ce n'est pas idéal, car une fois la session détruite, il n'y a aucun moyen de rouvrir la même conversation. Créez une action `open` à l'intérieur du contrôleur.

```rb
def open
  @conversation = Group::Conversation.find(params[:id])
  add_to_conversations unless already_added?
  respond_to do |format|
    format.js { render partial: 'group/conversations/open' }
  end
end
```

Créez le fichier partial `_open.js.erb` :

```js
var conversation = $('body').find("[data-gconversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
var chat_windows_count = $('.conversation-window').length + 1;


if (conversation.length !== 1) {
  $('body').append("<%= j(render 'group/conversations/conversation',\
                                  conversation: @conversation,\
                                  user: current_user) %>");
  conversation = $('body').find("[data-gconversation-id='" + 
                                "<%= @conversation.id %>" + 
                                "']");
}

// Basculer la fenêtre de conversation après sa création
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   .conversation-heading').click();
// marquer comme vu en cliquant dessus
setTimeout(function(){ 
  $('.conversation-window:nth-of-type(' + chat_windows_count + ')').click();
 }, 1000);
// focus sur le textarea
$('.conversation-window:nth-of-type(' + chat_windows_count + ')\
   form\
   textarea').focus();

var messages_list = conversation.find('.messages-list');
var height = messages_list[0].scrollHeight;
messages_list.scrollTop(height);

// repositionne toutes les fenêtres de chat
positionChatWindows();
```

Nous pouvons maintenant ouvrir des conversations en cliquant sur les liens du menu déroulant de la barre de navigation. Essayez de tester cela avec des feature specs par vous-même.

Commitez les changements.

```bash
git add -A
git commit -m "Add ability to open group conversations
- Create an open action in the Group::ConversationsController
- Create an _open.js.erb inside the group/conversations"
```

L'application tentera de rendre les messages, mais nous n'avons pas créé de templates pour eux. Créez un `_message.html.erb` :

```html
<%= render partial: group_message_date_check_partial_path(message, 
                                                          previous_message),
           locals: { message: message } %>
<li class="group-message">
  <div class="row <%= seen_by_user? %>" data-seen-by="<%= group_message_seen_by(message) %>">
    <%= render partial: message_content_partial_path(user, message, previous_message),
               locals: { user: user, message: message } %>
  </div>
</li>
```

Définissez les méthodes helper `group_message_date_check_partial_path`, `group_message_seen_by` et `message_content_partial_path` :

```rb
def group_message_date_check_partial_path(new_message, previous_message)
  # si un message précédent existe
  if defined?(previous_message) && previous_message.present?
    # si la date est différente entre le message précédent et le nouveau
    if previous_message.created_at.to_date != new_message.created_at.to_date
      'group/messages/message/new_date'
    else
      'shared/empty_partial'
    end
  else
    'shared/empty_partial'
  end
end

def group_message_seen_by(message)
  seen_by_names = []
  # Si quelqu'un a vu le message
  if message.seen_by.present?
    message.seen_by.each do |user_id|
      seen_by_names << User.find(user_id).name
    end
  end
  seen_by_names
end

def message_content_partial_path(user, message, previous_message)
  # si le message précédent existe
  if defined?(previous_message) && previous_message.present?
    # si le nouveau message est créé par le même utilisateur que le précédent
    if previous_message.user_id == user.id
      'group/messages/message/same_user_content'
    else
      'group/messages/message/different_user_content'
    end
  else
    'group/messages/message/different_user_content'
  end
end

def seen_by_user?
  @seen_by_user ? '' : 'unseen'
end
```

La méthode `group_message_seen_by` retournera une liste d'utilisateurs ayant vu un message. Cette petite information nous permet de créer des fonctionnalités supplémentaires, comme montrer aux participants de la conversation qui a vu les messages, etc. Mais dans notre cas, nous utiliserons cette information pour déterminer si un utilisateur actuel a vu un message ou non. Si ce n'est pas le cas, après que l'utilisateur l'aura vu, le message sera marqué comme vu.

De plus, nous aurons besoin des méthodes helper du module `Shared`. À l'intérieur du `Group::MessagesHelper`, ajoutez le module :

```rb
require 'shared/messages_helper'
include Shared::MessagesHelper
```

Couvrez les méthodes helper avec des specs :

```rb
context '#group_message_seen_by' do
  let(:message) { create(:group_message) }
  it 'returns an array with users' do
    users = create_list(:user, 2)
    users.each do |user|
      message.seen_by << user.id
    end
    message.save
    users.map! { |user| user.name }
    expect(helper.group_message_seen_by(message)).to eq users
  end

  it 'returns an empty array' do
    users = []
    expect(helper.group_message_seen_by(message)).to eq users
  end
end

context '#message_content_partial_path' do
  let(:user) { create(:user) }
  let(:message) { create(:group_message) }
  let(:previous_message) { create(:group_message) }

  it "returns same_user_content partial's path" do
    previous_message.update(user_id: user.id)
    expect(helper.message_content_partial_path(user, 
                                               message, 
                                               previous_message)).to eq(
      'group/messages/message/same_user_content'
    )
  end

  it "returns different_user_content partial's path" do
    expect(helper.message_content_partial_path(user, 
                                               message, 
                                               previous_message)).to eq(
      'group/messages/message/different_user_content'
    )
  end

  it "returns different_user_content partial's path" do
    previous_message = nil
    expect(helper.message_content_partial_path(user, 
                                               message, 
                                               previous_message)).to eq(
      'group/messages/message/different_user_content'
    )
  end
end

context '#group_message_date_check_partial_path' do
  let(:new_message) { create(:group_message) }
  let(:previous_message) { create(:group_message) }

  it "returns a new_date partial's path" do
    new_message.update(created_at: 2.days.ago)
    expect(helper.group_message_date_check_partial_path(new_message, 
                                                        previous_message)).to eq(
      'group/messages/message/new_date'
    )
  end

  it "returns an empty partial's path" do
    expect(helper.group_message_date_check_partial_path(new_message, 
                                                        previous_message)).to eq(
      'shared/empty_partial'
    )
  end

  it "returns an empty partial's path" do
    previous_message = nil
    expect(helper.group_message_date_check_partial_path(new_message, 
                                                        previous_message)).to eq(
      'shared/empty_partial'
    )
  end
end
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a _message.html.erb inside group/messages
- Define group_message_date_check_partial_path,
  group_message_seen_by and message_content_partial_path helper
  methods and write specs for them"
```

Créez les fichiers partials pour le message :

```html
<div class="messages-date">
  <span><%= message.created_at.to_date %></span>
</div>
```

```html
<span class="message-author"><%= user.name %></span>
<span class="message-time"><%= message.created_at.to_s(:time) %></span>
<p class="message-content">
  <%= message.content %>
</p>
```

```html
<div class="message-time hidden-item"><%= message.created_at.to_s(:time) %></div> 
<p class="message-content">
  <%= message.content %>
</p>
```

Commitez les changements.

```bash
git add -A
git commit -m "Create _new_date.html.erb,
_different_user_content.html.erb and _same_user_content.html.erb
inside the group/messages/message/"
```

Nous avons maintenant besoin d'un mécanisme qui rendra les messages un par un. Créez un fichier partial `_messages.html.erb` :

```html
<% previous_message = nil %>
<% @messages.reverse.each do |message| %>
  <%= render  partial: 'group/messages/message', 
              locals: { user: message.user, 
                        conversation_id: @conversation.id,
                        message: message, 
                        previous_message: previous_message } %>
  <% previous_message = message %>
<% end %>
```

Commitez le changement.

```bash
git add -A
git commit -m "Create _messages.html.erb inside group/conversations"
```

Ajoutez le style pour les messages de groupe :

```scss
.group-message {
  padding: 0 10px;
  word-wrap: break-word;
  z-index: 1;
  .row {
    position: relative;
  }
  .hidden-item {
    position: absolute; 
    left: 0; 
    vertical-align: middle;
    line-height: 20px;
    visibility: hidden;
  }
  .message-content {
    margin-left: 40px;
  }
  &:hover {
    background-color: rgb(250, 250, 250);
  }
  p {
    margin: 0;
  }
  .message-author, .message-time {
    font-size: 12px;
    font-size: 1.2rem;
  }
  .message-author {
    margin-left: 40px;
    font-weight: bold;
  }
  .message-time {
    padding-left: 2px;
    color: rgba(0,0,0,0.5);
  }
  &:hover .message-time {
    visibility: visible;
  }
}
```

Commitez le changement.

```bash
git add -A
git commit -m "Add CSS for group messages in conversation_window.scss"
```

Rendez le bouton de fermeture fonctionnel en définissant une action `close` à l'intérieur du `Group::ConversationsController` :

```rb
def close
  @conversation = Group::Conversation.find(params[:id])

  session[:group_conversations].delete(@conversation.id)

  respond_to do |format|
    format.js
  end
end
```

Créez le fichier template correspondant :

```js
$('body').find("[data-gconversation-id='" + "<%= @conversation.id %>" + "']")
    .parent()
    .remove();
positionChatWindows();
```

Commitez les changements.

```bash
git add -A
git commit -m "Add a close group conversation window functionality
- Define a close action inside the Group::ConversationsController
- Create a close.js.erb inside the group/conversations"
```

**Communiquer en temps réel**

Tout comme pour les conversations privées, nous voulons pouvoir avoir des conversations en temps réel avec plusieurs utilisateurs dans la même fenêtre. Le processus pour réaliser cette fonctionnalité sera assez similaire à ce que nous avons fait pour les conversations privées.

Générez un nouveau canal pour les conversations de groupe :

```bash
rails g channel group/conversation
```

```rb
class Group::ConversationChannel < ApplicationCable::Channel
  def subscribed
    if belongs_to_conversation(params[:id])
      stream_from "group_conversation_#{params[:id]}"
    end
  end

  def unsubscribed
    stop_all_streams
  end

  def set_as_seen(data)
    # trouver une conversation et définir son dernier message comme vu
    conversation = Group::Conversation.find(data['conv_id'])
    last_message = conversation.messages.last 
    last_message.seen_by << current_user.id
    last_message.save
  end

  def send_message(data)
    message_params = data['message'].each_with_object({}) do |el, hash|
      hash[el['name']] = el['value']
    end
    message = Group::Message.new(message_params)
    if message.save
      previous_message = message.previous_message
      Group::MessageBroadcastJob.perform_later(message, previous_message, current_user)
    end
  end

  private

  # vérifie si un utilisateur appartient à une conversation
  def belongs_to_conversation(id)
    conversations = current_user.group_conversations.ids
    conversations.include?(id)
  end

end
```

Cette fois, nous vérifions si un utilisateur appartient à une conversation avant d'établir la connexion, avec la méthode `belongs_to_conversation`. Dans les conversations privées, nous diffusions à partir d'un canal unique en fournissant l'ID du `current_user`. Dans le cas des conversations de groupe, l'ID d'une conversation est transmis depuis le côté client. Avec la méthode `belongs_to_conversation`, nous vérifions que les utilisateurs n'ont pas fait de manipulations et n'ont pas essayé de se connecter à un canal auquel ils n'appartiennent pas.

Commitez le changement

```bash
git add -A
git commit -m "Create a Group::ConversationChannel"
```

Créez le `Group::MessageBroadcastJob` :

```bash
rails g job group/message_broadcast
```

```rb
class Group::MessageBroadcastJob < ApplicationJob
  queue_as :default

  def perform(message, previous_message, current_user)
    # diffuser le message à tous les participants de la conversation
    conversation_id = message.conversation_id
    ActionCable.server.broadcast(
      "group_conversation_#{conversation_id}",
      message: render_message(message, previous_message),
      conversation_id: conversation_id,
      user_id: message.user_id
    )
  end

  def render_message(message, previous_message)
    ApplicationController.render(
      partial: 'group/messages/message',
      locals: { message: message, 
                previous_message: previous_message, 
                user: message.user }
    )
  end

end
```

Commitez le changement.

```bash
git add -A
git commit -m "Create a Group::MessageBrodcastJob"
```

La dernière pièce manquante du puzzle — le côté client :

```js
for (i = 0; i < gon.group_conversations.length; i++) {
    subToGroupConversationChannel(gon.group_conversations[i]);
}

function subToGroupConversationChannel(id) {
    App['group_conversation_' + id]  = App.cable.subscriptions.create(
        {
            channel: 'Group::ConversationChannel',
            id: id
        },
        {
            connected: function() {},
            disconnected: function() {},
            received: function(data) {
                console.log('sawp');
                // ajouter le lien vers la conversation 
                // en haut de la liste du menu des conversations
                modifyConversationsMenuList(data['conversation_id']);

                // définir les variables
                var conversation = findConv(data['conversation_id'], 'g');
                var conversation_rendered = ConvRendered(data['conversation_id'], 'g');
                var messages_visible = ConvMessagesVisiblity(conversation);

                // si le message n'est pas envoyé par l'utilisateur, 
                // marquer la conversation comme non vue
                MarkGroupConvAsUnseen(data['user_id'], data['conversation_id']);

                // ajouter le nouveau message
                appendGroupMessage(conversation_rendered, 
                                   messages_visible, 
                                   conversation,
                                   data['message']);

                // si la fenêtre de conversation est rendue
                if (conversation_rendered) {
                    // après l'ajout du nouveau message 
                    // défiler jusqu'au bas de la fenêtre de conversation
                    var messages_list = conversation.find('.messages-list');
                    var height = messages_list[0].scrollHeight;
                    messages_list.scrollTop(height);
                }
                
            },
            send_message: function(message) {
                return this.perform('send_message', {
                    message: message
                });
            },
            set_as_seen: function(conv_id) {
                return this.perform('set_as_seen', { conv_id: conv_id });
            }
        }
    );
}

$(document).on('submit', '.send-group-message', function(e) {
    e.preventDefault();
    var id = $(this).find('input[name=conversation_id]').val();
    var message_values = $(this).serializeArray();
    App['group_conversation_' + id].send_message(message_values);
});

// si le dernier message de la conversation n'est pas vu par l'utilisateur
// marquer les messages non vus comme vus
$(document).on('click', '.conversation-window, .group-conversation', function(e) {
    var latest_message = $('.messages-list ul li:last .row', this);
    var unseen_by_user = latest_message.hasClass('unseen');
    // si non vu par l'utilisateur
    if (unseen_by_user) {
        var conv_id = $(this).find('.panel').attr('data-gconversation-id');
        // si conv_id n'existe pas, cela signifie que le message a été vu dans le messenger
        if (conv_id == null) {
            var conv_id = $(this).find('.messages-list').attr('data-gconversation-id');
        }
        // marquer la conversation comme vue dans la liste du menu des conversations
        $('#menu-gc' + conv_id).removeClass('unseen-conv');
        latest_message.removeClass('unseen');
        calculateUnseenConversations();
        App['group_conversation_' + conv_id].set_as_seen(conv_id);
    }
});

function MarkGroupConvAsUnseen(message_user_id, conversation_id) {
     // si le message n'est pas envoyé par l'utilisateur, marquer la conversation comme non vue
    if (message_user_id != gon.user_id) {
        newGroupConvMenuListLink(conversation_id);

        // marquer la conversation comme non vue après la réception du nouveau message
        $('#menu-gc' + conversation_id).addClass('unseen-conv');
        calculateUnseenConversations();
    }
                  
}

// ajouter le lien vers la conversation en haut de la liste du menu des conversations
function modifyConversationsMenuList(conversation_id) {
    // si le lien de la conversation dans la liste du menu des conversations existe
    // déplacer le lien de la conversation en haut de la liste du menu des conversations
    var conversation_menu_link = $('#conversations-menu ul')
                                     .find('#menu-gc' + conversation_id);
    if (conversation_menu_link.length) {
        conversation_menu_link.prependTo('#conversations-menu ul');
    }
}

// ajouter le nouveau message à la liste
function appendGroupMessage(conversation_rendered, 
                            messages_visible, 
                            group_conversation,
                            message) {
    if (conversation_rendered) {
        // si la conversation est réduite
        if (!messages_visible) {
            // marquer la couleur de son en-tête
        }
        // ajouter le nouveau message à la liste
        group_conversation
            .find('.messages-list')
            .find('ul')
            .append(message);
    }

}

// si le lien de la conversation dans la liste du menu des conversations n'existe pas
// créer un nouveau lien avec le nom du destinataire et l'ajouter en haut de la liste
function newGroupConvMenuListLink(conversation_id) {
    var id_attr = '#menu-gc' + conversation_id;
    var conversation_menu_link = $('#conversations-menu ul').find(id_attr);
    if (conversation_menu_link.length == 0) {
        var list_item = '<li class="conversation-window">\
                             <a data-remote="true"\
                                rel="nofollow"\
                                data-method="post"\
                                href="/group_conversations?group_conversation_id=' +  conversation_id + '">\
                                    group conversation\
                             </a>\
                         </li>';
        $('#conversations-menu ul').prepend(list_item);
    }
}
```

Essentiellement, c'est très similaire au fichier `.js` de la conversation privée. La structure du code est un peu différente. La principale différence est la possibilité de passer l'ID de la conversation à un canal et une boucle en haut du fichier. Avec cette boucle, nous connectons un utilisateur à tous les canaux de ses conversations de groupe. C'est la raison pour laquelle nous avons utilisé la méthode `belongs_to_conversation` côté serveur. Les IDs des conversations sont transmis depuis le côté client. Cette méthode côté serveur s'assure qu'un utilisateur appartient réellement à une conversation fournie.

Quand on y pense, nous aurions pu simplement créer cette boucle côté serveur et ne pas avoir à gérer tout ce processus de confirmation. Mais voici la raison pour laquelle nous passons l'ID d'une conversation depuis le côté client. Lorsque de nouveaux utilisateurs sont ajoutés à une conversation de groupe, nous voulons les connecter immédiatement au canal de la conversation, sans nécessiter le rechargement d'une page. L'ID de conversation transmissible nous permet d'y parvenir sans effort. Dans la section suivante, nous créerons un canal unique pour chaque utilisateur afin de recevoir des notifications en temps réel. Lorsque de nouveaux utilisateurs seront ajoutés à une conversation de groupe, nous appellerons la fonction `subToGroupConversationChannel`, via leurs canaux de notification uniques, et les connecterons au canal de la conversation de groupe. Si nous ne permettions pas de passer l'ID d'une conversation à un canal, les connexions aux nouveaux canaux n'auraient eu lieu qu'après un rechargement de page. Nous n'aurions aucun moyen de connecter de nouveaux utilisateurs à un canal de conversation de manière dynamique.

Nous sommes maintenant capables d'envoyer et de recevoir des messages de groupe en temps réel. Essayez de tester l'ensemble des fonctionnalités avec des specs par vous-même.

Commitez les changements.

```bash
git add -A
git commit -m "Create a conversation.js inside the
assets/javascripts/channels/group"
```

Dans le `Group::ConversationsController`, définissez une action `update` :

```rb
def update
  Group::AddUserToConversationService.new({
    conversation_id: params[:id],
    new_user_id: params[:user][:id],
    added_by_id: params[:added_by]
  }).call
end
```

Créez le `Group::AddUserToConversationService`, qui va s'occuper d'ajouter un utilisateur sélectionné à une conversation :

```rb
class Group::AddUserToConversationService

  def initialize(params)
    @group_conversation_id = params[:group_conversation_id]
    @new_user_id = params[:new_user_id]
    @added_by_id = params[:added_by_id]
  end

  def call
    group_conversation = Group::Conversation.find(@group_conversation_id)
    new_user = User.find(@new_user_id)
    added_by = User.find(@added_by_id)
    if new_user.group_conversations << group_conversation
      create_info_message(new_user, added_by)
    end
  end

  private

  def create_info_message(new_user, added_by)
    message = Group::Message.new(
      user_id: added_by.id, 
      content: '' + new_user.name + ' added by ' + added_by.name, 
      added_new_users: [new_user.id], 
      group_conversation_id: @group_conversation_id)
    if message.save
      Group::MessageBroadcastJob.perform_later(message, nil, nil)
    end
  end

end
```

Testez le service avec des specs :

```rb
require 'rails_helper'
require './app/services/group/add_user_to_conversation_service.rb'

describe Group::AddUserToConversationService do
  context '#call' do
    let(:user) { create(:user) }
    let(:new_user) { create(:user) }
    let(:conversation) { create(:group_conversation, users: [user]) }
    let(:add_user_to_conversation) do
      Group::AddUserToConversationService.new({
        conversation_id: conversation.id,
        new_user_id: new_user.id,
        added_by_id: user.id
      }).call
    end

    it 'adds user to a group conversation' do
      add_user_to_conversation
      conversation_users = Group::Conversation.find(conversation.id).users
      expect(conversation_users).to include new_user
    end

    it 'creates an informational message' do
      add_user_to_conversation
      group_conversation = Group::Conversation.find(conversation.id)
      expect(group_conversation.messages.count).to eq 1
    end
  end
end
```

Nous avons maintenant des conversations privées et de groupe fonctionnelles. Quelques nuances manquent encore, que nous implémenterons plus tard, mais la fonctionnalité de base est là. Les utilisateurs peuvent communiquer en tête-à-tête ou, s'ils le souhaitent, construire une salle de chat entière avec plusieurs personnes.

Commitez les changements.

```bash
git add -A
git commit -m "Create a Group::AddUserToConversationService and test it"
```

#### Messenger

Quel est l'intérêt d'avoir un messenger ? Sur les écrans mobiles, au lieu d'ouvrir une fenêtre de conversation, l'application chargera le messenger. Sur les écrans plus grands, les utilisateurs pourront choisir où discuter, sur la fenêtre de conversation ou sur le messenger. Si le messenger remplit toute la fenêtre du navigateur, il devrait être plus confortable pour communiquer.

Comme nous utiliserons les mêmes données et modèles, nous avons juste besoin d'ouvrir les conversations dans un environnement différent. Générez un nouveau contrôleur pour gérer les requêtes d'ouverture d'une conversation à l'intérieur du messenger.

```bash
rails g controller messengers
```

```rb
class MessengersController < ApplicationController
  before_action :redirect_if_not_signed_in

  def index
    @users = User.all.where.not(id: current_user)
  end

  def get_private_conversation
  	conversation = Private::Conversation.between_users(current_user.id, params[:id])
  	@conversation = conversation[0]
  	respond_to do |format|
      format.js { render 'get_private_conversation'}
    end
  end

  def get_group_conversation
    @conversation = Group::Conversation.find(params[:group_conversation_id])
    respond_to do |format|
      format.js { render 'get_group_conversation'}
    end
  end

  def open_messenger
    @type = params[:type]
    @conversation = get_conversation
  end

  private

    def get_conversation
      ConversationForMessengerService.new({
          conversation_type: params[:type],
          user1_id: current_user.id,
          user2_id: params[:id],
          group_conversation_id: params[:group_conversation_id]
        }).call
    end
  
end
```

Les actions `get_private_conversation` et `get_group_conversation` récupéreront la conversation sélectionnée par l'utilisateur. Les templates de ces actions vont ajouter la conversation sélectionnée à l'emplacement réservé à la conversation. Chaque fois qu'une nouvelle conversation est sélectionnée pour être ouverte, l'ancienne est supprimée et remplacée par la nouvelle.

Définissez les routes pour les actions :

```rb
get 'messenger', to: 'messengers#index'
get 'get_private_conversation', to: 'messengers#get_private_conversation'
get 'get_group_conversation', to: 'messengers#get_group_conversation'
get 'open_messenger', to: 'messengers#open_messenger'
```

Commitez les changements.

Dans le contrôleur se trouve une action `open_messenger`. Le but de cette action est d'aller de n'importe quelle page directement au messenger et de rendre une conversation sélectionnée. Sur les écrans plus petits, les utilisateurs vont discuter via le messenger au lieu des fenêtres de conversation. Dans un instant, nous allons changer les liens pour les écrans plus petits afin d'ouvrir les conversations à l'intérieur du messenger.

Créez un template pour l'action `open_messenger` :

```html
<div class="container-fluid messenger">
  <div class="row">
    <div class="col-sm-2">
      <ul>
      </ul>
    </div>
    <div class="col-sm-10">
      <div class="conversation">
        <%= render partial: "messengers/#{@type}_conversation",
                      locals: { conversation: @conversation, 
                                user: current_user } %>
      </div>
    </div>
  </div>
</div>

<script>
  $('body nav').hide();
  $('.messenger .col-sm-2').hide();
  $('.messenger .col-sm-10').show();
  $('body').css('margin', '0 0 0 0');
  $('.messenger').css('height', '100vh');
</script>
```

```bash
git add -A
git commit -m "Create an open_messenger.html.erb in the /messengers"
```

Ensuite, nous voyons le `ConversationForMessengerSerivce`, il récupère l'objet de la conversation sélectionnée. Créez le service :

```rb
class ConversationForMessengerService
  def initialize(params)
    @conversation_type = params[:conversation_type]
    @user1_id = params[:user1_id] || nil
    @user2_id = params[:user2_id] || nil
    @group_conversation_id = params[:group_conversation_id] || nil
  end

  def call
    if @conversation_type == 'private'
      Private::Conversation.between_users(@user1_id, @user2_id)[0]
    else
      Group::Conversation.find(@group_conversation_id) 
    end
  end

end
```

Ajoutez des specs pour le service :

```rb
require 'rails_helper'
require './app/services/conversation_for_messenger_service.rb'

describe ConversationForMessengerService do
  let(:user1) { create(:user) }
  let(:user2) { create(:user) }
  let(:group_conversation) { create(:group_conversation) }
  let(:private_conversation) do 
    create(:private_conversation,
            sender_id: user1.id,
            recipient_id: user2.id)
  end

  context '#call' do
    it 'returns a group conversation' do
      expect(ConversationForMessengerService.new({
        conversation_type: 'group',
        group_conversation_id: group_conversation.id
      }).call).to eq group_conversation
    end

    it 'returns a private conversation' do
      private_conversation
      expect(ConversationForMessengerService.new({
        conversation_type: 'private',
        user1_id: user1.id,
        user2_id: user2.id
      }).call).to eq private_conversation
    end
  end

end
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a ConversationForMessengerSerivce and add specs for it"
```

Créez un template pour l'action index :

```html
<div class="container-fluid messenger">
  <div class="row">
    <%= render 'messengers/index/conversations_list' %>
    <%= render 'messengers/index/conversation' %>
  </div><!-- row -->
</div>
```

Ce sera le messenger lui-même. À l'intérieur du messenger, nous pourrons voir une liste des conversations de l'utilisateur et une conversation sélectionnée. Créez les fichiers partials :

```html
<div class="col-sm-2">
  <ul>
    <% @all_conversations.each do |conversation| %>
      <%= render partial: conversations_list_item_partial_path(conversation),
                 locals: { conversation: conversation } %>
    <% end %>
  </ul>
</div>
```

Définissez la méthode helper :

```rb
module MessengersHelper
  def conversations_list_item_partial_path(conversation)
    # s'il s'agit d'une conversation privée
    if conversation.class == Private::Conversation
      'messengers/index/conversations_list_item/private'
    else # c'est une conversation de groupe
      'messengers/index/conversations_list_item/group'
    end
  end
end
```

Essayez de le tester vous-même avec des specs.

Créez les fichiers partials pour les liens d'ouverture des conversations :

```html
<% recipient = private_conv_recipient(conversation) %>
<% seen_status = private_conv_seen_status(conversation) %>
<li id="menu-pc<%= conversation.id %>" class="<%= seen_status %>">
  <%= link_to recipient.name, 
              get_private_conversation_path(id: recipient.id), 
              remote: true  %>
</li>
```

```html
<% seen_status = group_conv_seen_status(conversation, current_user) %>
<li id="menu-gc<%= conversation.id %>" class="<%= @seen_by_user %>">
    <%= link_to conversation.name, 
                get_group_conversation_path(group_conversation_id: conversation.id), 
                remote: true %>
</li>
```

Maintenant, créez un partial pour l'espace de conversation, les conversations sélectionnées y seront rendues :

```html
<div class="col-sm-10">
  <div class="conversation">
    <div class="start-conversation">
      <div>
        <i class="fa fa-inbox" aria-hidden="true"></i><br>
        Open a conversation
      </div>
    </div>
  </div>
</div>
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a template for the MessengersController's index action"
```

Créez un template pour l'action `get_private_conversation` :

```js
$('.conversation').replaceWith('<div class="conversation private-conversation"></div>');
$('.conversation').append("<%= j(render partial: 'messengers/private_conversation',\
                                        locals: { conversation: @conversation,\
                                                  user: current_user}) %>");
```

Créez un fichier `_private_conversation.html.erb` :

```html
<% @recipient = private_conv_recipient(conversation) %>
<% @contact = get_contact_record(@recipient) %>
<% @is_messenger = true %>
<%= render 'private/conversations/conversation/request_status' %>
<%= render 'messengers/private_conversation/details' %>
<%= render 'private/conversations/conversation/messages_list', 
            conversation: conversation %>
<%= render  'private/conversations/conversation/new_message_form', 
            conversation: conversation,
            user: user %>
```

Ce fichier rendra une conversation privée à l'intérieur du messenger. Notez également que nous réutilisons certains partials des vues de conversation privée. Créez le partial `_details.html.erb` :

```html
<div class="conversation-details">
  <%= link_to :back do %>
    <i class="fa fa-arrow-left back-to-chats-main" aria-hidden="true"></i>
  <% end %>
  <div class="conversation-name">
    <%= @recipient.name %>
  </div>
</div>
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a template for the MessengersController's
get_private_conversation action"
```

Lorsque nous allons sur le messenger, il est préférable de ne pas voir les menus déroulants sur la barre de navigation. Pourquoi ? Nous ne voulons pas rendre les fenêtres de conversation à l'intérieur du messenger, sinon cela paraîtrait chaotique. Une fenêtre de conversation et le messenger en même temps pour discuter avec la même personne. Ce serait une conception très défectueuse.

Dans un premier temps, interdisez le rendu des fenêtres de conversations sur la page du messenger. Ce n'est pas si difficile à faire. Pour le contrôler, rappelez-vous comment les fenêtres de conversations sont rendues sur l'application. Elles sont rendues à l'intérieur du fichier `application.html.erb`. Ensuite, nous avons les variables d'instance `@private_conversations_windows` et `@group_conversations_windows`. Ces variables sont des tableaux de conversations. Au lieu de simplement rendre les conversations de ces tableaux, définissez des méthodes helper pour décider de donner ces tableaux aux utilisateurs ou non, selon la page sur laquelle ils se trouvent. Si les utilisateurs sont sur la page du messenger, ils recevront un tableau vide et aucune fenêtre de conversation ne sera rendue.

Remplacez ces variables d'instance par les méthodes helper `private_conversations_windows` et `group_conversations_windows`. Maintenant, définissez-les à l'intérieur de l'`ApplicationHelper` :

```rb
def private_conversations_windows
  params[:controller] != 'messengers' ? @private_conversations_windows : []
end

def group_conversations_windows
  params[:controller] != 'messengers' ? @group_conversations_windows : []
end
```

Couvrez-les avec des specs :

```rb
require 'rails_helper'

RSpec.describe ApplicationHelper, :type => :helper do
  context '#private_conversations_windows' do
    let(:conversations) { conversations = create_list(:private_conversation, 2) }
    
    it 'returns private conversations' do
      assign(:private_conversations_windows, conversations)
      controller.params[:controller] = 'not_messengers'
      expect(helper.private_conversations_windows).to eq conversations
    end

    it 'returns an empty array' do
      assign(:private_conversations_windows, conversations)
      controller.params[:controller] = 'messengers'
      expect(helper.private_conversations_windows).to eq []
    end
  end

  context '#group_conversations_windows' do
    let(:conversations) { create_list(:group_conversation, 2) }

    it 'returns group conversations' do
      assign(:group_conversations_windows, conversations)
      controller.params[:controller] = 'not_messengers'
      expect(helper.group_conversations_windows).to eq conversations
    end

    it 'returns an empty array' do
      assign(:group_conversations_windows, conversations)
      controller.params[:controller] = 'messengers'
      expect(helper.group_conversations_windows).to eq []
    end
  end
end
```

Commitez les changements

```bash
git add -A
git commit -m "
Define private_conversations_windows and group_conversations_windows
helper methods inside the ApplicationHelper and test them"
```

Ensuite, créez un fichier partial alternatif pour l'en-tête de navigation, afin que les menus déroulants ne soient pas rendus. Dans le `NavigationHelper`, nous avons défini précédemment la méthode helper `nav_header_content_partials`. Elle détermine quel en-tête de navigation rendre.

Dans le répertoire

```bash
layouts/navigation/header
```

créez un fichier `_messenger_header.html.erb` :

```html
<%= link_to 'collabfield', root_path, class: 'navbar-brand' %>
<div class="pull-right" id="messages-page-name">Messages</div>
```

Stylisez le messenger. Créez un fichier `messenger.scss` dans le répertoire `partials` :

```scss
.messenger {
  z-index: 2;
  padding: 0;
  background-color: white;
  height: calc(100vh - 50px);
  .conversation-details {
    z-index: 3;
    background-color: white;
    position: fixed;
    top: 0;
    width: 100%;
    text-align: center;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
    .back-to-chats-main, .conversation-name {
      height: 50px;
      line-height: 50px;
      vertical-align: middle;
      color: $navbarColor;
    }
    .back-to-chats-main {
      position: absolute;
      left: 10px;
      font-size: 24px;
      font-size: 2.4rem;
    }
    .conversation-name {
      display: inline-block;
      font-size: 20px;
      font-size: 2.0rem;
    }
  }
  .row {
    height: 100%;
  }
  .col-sm-2, .col-sm-10, .conversation {
    height: 100%;
  }
  .conversation {
    position: relative;
    .contact-request-sent {
      display: none !important;
    }
    .start-conversation {
      height: 100%;
      display: table;
      margin: 0 auto;
      div {
        display: table-cell;
        vertical-align: middle;
        text-align: center;
        i {
          font-size: 40px;
          font-size: 4.0rem;
        }
      }
    }
  }
  .col-sm-2 {
    padding: 0;
    background-color: $navbarColor;
    ul {
      padding: 20px 0 0 0;
      background-color: $navbarColor;
      li a {
        color: white;
        display: inline-block;
        padding: 10px 0 10px 10px;
        width: 100%;
        border-bottom: 1px solid rgba(255,255,255,0.4);
        &:hover {
          background-color: white;
          color: black;
        }
      }
    }
    border-right: 1px solid $navbarColor;
  }
  .messages-list {
    min-height: 100%;
    height: 100%;
  }
  .send-private-message, .send-group-message {
    z-index: 3;
    position: absolute;
    width: 100%;
    bottom: 7px;
  }
  .contact-request-status {
    width: 100%;
  }
}
```

Commitez le changement

```bash
git add -A
git commit -m "Create a messenger.scss inside the partials"
```

Dans `desktop.scss`, à l'intérieur de `min-width: 767px`, ajoutez :

```scss
.messenger {
  .col-sm-2 {
    display: initial !important;
  }
  .col-sm-2, .col-sm-10 {
    display: initial;
  }
  .conversation {
    padding: 0 0 60px 0;
    .conversation-details {
      display: none;
    }
  }
}
```

Lorsque nous cliquons sur une conversation pour l'ouvrir, nous voulons pouvoir charger les messages précédents d'une manière ou d'une autre. Nous pourrions ajouter un lien visible pour les charger. Ou nous pouvons charger automatiquement une certaine quantité de messages jusqu'à ce que la barre de défilement apparaisse, afin qu'un utilisateur puisse charger les messages précédents en faisant défiler vers le haut. Créez une méthode helper qui s'en chargera :

```rb
# dans le messenger, charger les messages précédents jusqu'à ce que la barre de défilement apparaisse
def autoload_messenger_messages
  if @is_messenger == 'true'
    # si des messages précédents existent, les charger
    if @messages_to_display_offset != 0
      'shared/load_more_messages/messenger/load_previous_messages'
    else 
      # supprimer le lien de chargement des messages précédents 
      'shared/load_more_messages/messenger/remove_previous_messages_link'
    end 
  else
    'shared/empty_partial'
  end
end
```

Testez-le avec des specs par vous-même. Créez les fichiers partials :

```js
var scrollbar_visible = $('.conversation .messages-list').scrollTop();
if (scrollbar_visible == 0) {
    $('.conversation .messages-list .load-more-messages').click();
}
```

```js
$('body .conversation .messages-list .loading-more-messages')
    .replaceWith('');
$('body .conversation .messages-list .load-more-messages')
.replaceWith('');
```

Commitez les changements

```bash
git add -A
git commit -m "Define an autoload_messenger_messages in the
Shared::MessagesHelper"
```

Utilisez la méthode helper à l'intérieur du fichier `_load_more_messages.js.erb`, juste au-dessus de `<%= render remove_link_to_messages %>` :

```js
<%= render autoload_messenger_messages %>
```

Nous avons maintenant les méthodes helper `append_previous_messages_partial_path` et `replace_link_to_private_messages_partial_path` que nous devrions mettre à jour pour les rendre compatibles avec le messenger :

```rb
def append_previous_messages_partial_path
  # si une conversation est ouverte dans le messenger
  if @is_messenger == 'true'
    'shared/load_more_messages/messenger/append_messages' 
  else 
    'shared/load_more_messages/window/append_messages' 
  end 
end
```

Créez un fichier partial manquant :

```js
// supprimer temporairement le lien de chargement de plus de messages 
// afin qu'il ne puisse pas être cliqué si les nouveaux messages ne sont pas encore rendus
$('body .conversation .messages-list .load-more-messages')
    .replaceWith('<span class="load-more-messages"></span>');
// rendre les messages précédents
$('body .conversation .messages-list ul')
    .prepend('<%= j render "#{@type}/conversations/messages" %>');
// après l'ajout des nouveaux messages, laisser un espace en haut de la barre de défilement
$('body .conversation .messages-list').scrollTop(400);
```

Mettez à jour une autre méthode :

```rb
def replace_link_to_private_messages_partial_path
  if @is_messenger == 'true'
    'private/messages/load_more_messages/messenger/replace_link_to_messages'
  else
    'private/messages/load_more_messages/window/replace_link_to_messages'
  end
end
```

Créez le fichier partial :

```js
$('.conversation .load-more-messages')
    .replaceWith('\
        <%= j render partial: "private/conversations/conversation/messages_list/link_to_previous_messages",\
                     locals: { conversation: @conversation } %>\
        ');
```

Testez les méthodes helper avec des specs par vous-même.

Commitez les changements.

```bash
git add -A
git commit -m "
- Update the append_previous_messages_partial_path helper method in
  Shared::MessagesHelper
- Update the replace_link_to_private_messages_partial_path method in
  Private::MessagesHelper"
```

Maintenant, après un clic initial sur le lien de chargement des messages, l'application continuera automatiquement à charger les messages précédents jusqu'à ce qu'il y ait une barre de défilement sur la liste des messages. Pour que le clic initial se produise, ajoutez du JavaScript :

```js
$(document).on('turbolinks:load ajax:complete', function() {
    var messages_visible = $('.conversation .messages-list ul', this)
                               .has('li').length;
    var previous_messages_exist = $('.conversation .messages-list .load-more-messages', this).length;
    // Charger les messages précédents si la liste des messages est vide && la barre de défilement n'existe pas
    if (!messages_visible && previous_messages_exist) {
        $('.load-more-messages', this)[0].click();
        $('.conversation .messages-list .loading-more-messages').hide();
    }
});
```

Lorsque vous visitez le chemin `/messenger`, vous voyez le messenger :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-112.png)

Vous pouvez ensuite ouvrir n'importe laquelle de vos conversations.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-113.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-114.png)

Commitez les changements.

Maintenant, sur les écrans plus petits, lorsque les utilisateurs cliquent sur le lien de la barre de navigation pour ouvrir une conversation, leur conversation doit être ouverte dans le messenger au lieu d'une fenêtre de conversation. Pour rendre cela possible, nous devons créer des liens différents pour les écrans plus petits.

À l'intérieur du partial `_private.html.erb` de la navigation, qui stocke un lien pour ouvrir une conversation privée, ajoutez un lien supplémentaire pour les appareils à petit écran. Ajoutez ce lien juste en dessous du lien `open_private_conversation_path` dans le fichier :

```html
<%= link_to recipient.name, 
        open_messenger_path(id: recipient.id, 
                            smaller_device: true, 
                            type: 'private'), 
        class: 'smaller-screen-link' %> 
```

Sur les écrans plus petits, ce lien sera affiché à la place du précédent, dédié aux écrans plus grands. Ajoutez également un lien supplémentaire pour ouvrir les conversations de groupe :

```html
<%= link_to truncate(conversation.name, :length => 40), 
          open_messenger_path(group_conversation_id: conversation.id, 
          smaller_device: true, type: 'group'), 
          class: 'smaller-screen-link' %> 
```

La raison pour laquelle nous voyons différents liens sur différentes tailles d'écran est que nous avons précédemment défini le CSS pour les classes `bigger-screen-link` et `smaller-screen-link`.

Commitez les changements.

```bash
git add -A
git commit -m "Inside _private.html.erb and _group.html.erb, in the 
layouts/navigation/header/dropdowns/conversations, add alternative
links for smaller devices to open conversations"
```

Les versions du messenger sur ordinateur et sur appareils mobiles vont différer un peu. Écrivez du JavaScript dans `messenger.js` afin qu'après qu'un utilisateur a cliqué pour ouvrir une conversation, le js détermine s'il doit afficher une version mobile ou non.

```js
// si le messenger est ouvert sur un appareil à petit écran
// afficher la version du messenger pour les appareils mobiles
$(".messenger .col-sm-2 ul").on( "click", "a", function() {
    var col_2_width = $('.messenger .col-sm-2').css('width');
    var window_width = '' + $('.messenger').width() + 'px';
    // vérifier si les colonnes bootstrap sont empilées (la page est ouverte sur un petit appareil)
    if (col_2_width == window_width) {
        $('body nav').hide();
        $('.messenger .col-sm-2').hide();
        $('.messenger .col-sm-10').show();
        $('body').css('margin', '0 0 0 0');
        $('.messenger').css('height', '100vh');
    }
});
```

Maintenant, lorsque vous ouvrez une conversation sur un appareil mobile, cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-115.png)

Commitez le changement.

```bash
git add -A
git commit -m "Add JavaScript to messenger.js to show a different
messenger's version on mobile devices"
```

Maintenant, rendez les conversations de groupe fonctionnelles sur le messenger. La majeure partie du travail avec le messenger est déjà faite, donc la mise en place des conversations de groupe sera beaucoup plus facile. Si vous regardez à nouveau dans le `MessengersController`, nous avons l'action `get_group_conversation`. Créez un fichier template pour celle-ci :

```js
$('.conversation').replaceWith('<div class="conversation group-conversation"></div>');
$('.conversation').append("<%= j(render 'messengers/group_conversation',\
                                         conversation: @conversation) %>");
```

Ensuite, créez un fichier pour rendre une conversation de groupe dans le messenger :

```html
<% @is_messenger = true %>
<%= render 'messengers/group_conversation/details', 
            conversation: conversation %>
<%= render 'group/conversations/conversation/messages_list', 
            conversation: conversation %>
<%= render 'messengers/group_conversation/new_message_form', 
            conversation: conversation %>
```

Créez ses partials :

```html
<div class="conversation-details">
  <%= link_to :back do %>
    <i class="fa fa-arrow-left back-to-chats-main" aria-hidden="true"></i>
  <% end %>
  <div class="conversation-name">
    <%= conversation.name %>
  </div>
</div>
```

```html
<form class="send-group-message">
  <input  name="conversation_id" 
          type="hidden" 
          value="<%= conversation.id %>">
  <input name="user_id" type="hidden" value="<%= current_user.id %>">
  <textarea name="content" 
            rows="2" 
            class="form-control" 
            placeholder="Type a message..."></textarea>
  <input type="submit" class="btn btn-success send-message">
</form>
```

Commitez les changements :

```bash
git add -A
git commit -m "Create a get_group_conversation.js.erb template and 
its partials inside the messengers"
```

Voici à quoi ressemblent les conversations de groupe dans le messenger :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-116.png)

### 5. Notifications

L'application dispose déjà de toutes les fonctionnalités fondamentales. Dans cette section, nous allons concentrer notre énergie sur l'amélioration de ces fonctionnalités vitales. Des notifications instantanées, lorsque d'autres utilisateurs tentent de vous contacter, offrent une meilleure expérience utilisateur. Faisons en sorte que les utilisateurs soient avertis chaque fois qu'ils reçoivent une mise à jour de demande de contact ou qu'ils rejoignent une conversation de groupe.

#### Demandes de contact

Générez un canal de notification qui gérera toutes les notifications de l'utilisateur.

```bash
rails g channel notification
```

```rb
class NotificationChannel < ApplicationCable::Channel
  def subscribed
    stream_from "notifications_#{current_user.id}"
  end

  def unsubscribed
    stop_all_streams
  end

  def contact_request_response(data)
    receiver_user_name = data['receiver_user_name']
    sender_user_name = data['sender_user_name']
    notification = data['notification']
    receiver = User.find_by(name: receiver_user_name)

    ActionCable.server.broadcast(
      "notifications_#{receiver.id}",
      notification: notification,
      sender_user_name: sender_user_name,
    )

  end
end
```

Commitez le changement.

```bash
git add -A
git commit -m "Create a NotificationChannel"
```

Chaque utilisateur aura son propre canal de notification unique. Ensuite, nous avons le `ContactRequestBroadcastJob`, qui diffusera les demandes de contact et les réponses.

Générez le job.

```bash
rails g job contact_request_broadcast
```

```rb
class ContactRequestBroadcastJob < ApplicationJob
  queue_as :default

  def perform(contact_request)

    sender = User.find(contact_request.user_id)
    receiver = User.find(contact_request.contact_id)
    ActionCable.server.broadcast(
      "notifications_#{receiver.id}",
      notification: 'contact-request-received',
      sender_name: sender.name,
      contact_request: render_contact_request(sender, contact_request)
    )

  end

  private

  def render_contact_request(sender, contact_request)
    ApplicationController.render(
      partial: 'contacts/contact_request',
      locals: { sender: sender }
    )
  end

end
```

Créez un partial `_contact_request.html.erb`, qui sera utilisé pour ajouter des demandes de contact dans le menu déroulant de la barre de navigation. Dans ce cas, nous ajouterons ces demandes de manière dynamique avec le `ContactRequestBroadcastJob` :

```html
<li class="contact-request" data-user-name="<%= sender.name %>">
  <div class="sixty-percent">
    <span class="contact-name"><%= sender.name %></span> 
  </div>
  <div class="forty-percent">
    <span class="accept-request">
      <%= link_to "Accept",  
                  contact_path(id: sender.id), 
                  remote: true, 
                  method: "put" %>
    </span> 
    <span class="decline-request">
      <%= link_to "Decline",
                  contact_path(id: sender.id), 
                  remote: true, 
                  method: :delete %>
    </span>
  </div>
</li>
```

Lancez le job chaque fois qu'un nouvel enregistrement `Contact` est créé :

```rb
after_create_commit { ContactRequestBroadcastJob.perform_later(self) }
```

Commitez les changements.

```bash
git add -A
git commit -m "Create a ContactRequestBroadcastJob"
```

Ensuite, créez le menu déroulant lui-même sur la barre de navigation :

```html
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
  <i class="fa fa-user-o" aria-hidden="true">
    <span id="unresponded-contact-requests"></span>
  </i>
</a>
<ul class="dropdown dropdown-menu" role="menu">
  <%= render nav_contact_requests_partial_path %>
</ul><!-- dropdown-menu -->
```

Définissez la méthode helper `nav_contact_requests_partial_path` :

```rb
def nav_contact_requests_partial_path
  # si des demandes de contact existent
  if current_user.pending_received_contact_requests.present? 
    'layouts/navigation/header/dropdowns/contact_requests/requests' 
  else # les demandes de contact n'existent pas 
    'layouts/navigation/header/dropdowns/contact_requests/no_requests'
  end
end
```

Couvrez la méthode avec des specs, puis créez les fichiers partials :

```html
<% current_user.pending_received_contact_requests.each do |user| %>
  <%= render partial: "layouts/"\
                      "navigation/"\
                      "header/"\
                      "dropdowns/"\
                      "contact_requests/"\
                      "request", 
             locals: { user: user } %>
<% end %>
```

```html
<li class="no-requests">You have no new requests</li>
```

À l'intérieur du fichier `_dropdowns.html.erb`, rendez le `_contact_requests.html.erb`, juste en dessous des conversations. Ainsi, nous pourrons voir un menu déroulant des demandes de contacts sur la barre de navigation :

```html
<div class='pull-right' id='contacts-requests'>
  <%= render 'layouts/navigation/header/dropdowns/contact_requests' %>
</div>
```

Commitez les changements.

```bash
git add -A
git commit -m "
- Create a _contact_requests.html.erb inside the
  layouts/navigation/header/dropdowns
- Define a nav_contact_requests_partial_path in NavigationHelper"
```

Créez également un fichier partial pour une seule demande de contact :

```html
<li class="contact-request" data-user-name="<%= user.name %>">
  <div class="sixty-percent">
    <span class="contact-name"><%= user.name %></span> 
  </div>
  <div class="forty-percent">
    <span class="accept-request">
      <%= link_to "Accept",  
                  contact_path(id: user.id), 
                  remote: true, 
                  method: "put" %>
    </span> 
    <span class="decline-request">
      <%= link_to "Decline",
                  contact_path(id: user.id), 
                  remote: true, 
                  method: :delete %>
    </span>
  </div>
</li><!-- contact-request -->
```

Commitez le changement.

```bash
git add -A
git commit -m "Create a _request.html.erb inside the
layouts/navigation/header/dropdowns"
```

Ajoutez du CSS pour styliser et positionner le menu déroulant des demandes de contact :

```scss
#contacts-requests {
  li {
    color: black;
    background-color: $backgroundColor;
    border-bottom: 1px solid $navbarColor;
  }
  i {
    position: relative;
  }
  .sixty-percent {
    display: inline-block;
    width: 60%;
  }
  .forty-percent {
    display: inline-block;
    float: right;
    width: 40%;
  }
  .contact-request, .contact-request-responded {
    .contact-name {
      padding-left: 10px;
      padding-right: 20px;
    }
    .accept-request, .decline-request {
      a {
        border: 2px solid $navbarColor;
        padding: 5px;
      }
      &:hover a {
        border-color: black;
      }
      transition: 0.15s border-color;
      transition: 0.15s background-color;
    }
    .accept-request {
      a:hover {
        background-color: black !important;
      }
      a {
        background-color: $navbarColor;
        color: white !important;
      }
    }
    .decline-request {
      a {
        background-color: $backgroundColor;
        color: black !important;
      }
      a:hover, &:hover {
        background-color: white !important;
      }
    }
    .accepted-request {
      background: $navbarColor;
      color: white;
      padding: 5px;
    }
  }
  .no-requests {
    text-align: center;
  }
}

#unresponded-contact-requests {
  top: 0;
  right: 5px;
  background: #3F4EBF;
}
```

Commitez les changements.

```bash
git add -A
git commit -m "Add CSS in navigation.scss to style and position the
contact requests drop down menu"
```

Sur la barre de navigation, nous pouvons maintenant voir un menu déroulant pour les demandes de contact.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-117.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-118.png)

Nous avons le canal de notifications et le job pour diffuser les mises à jour des demandes de contact. Maintenant, nous devons créer une connexion côté client, afin que les utilisateurs puissent envoyer et recevoir des données en temps réel.

```js
App.notification = App.cable.subscriptions.create("NotificationChannel", {
  connected: function() {},
  disconnected: function() {},
  received: function(data) {
    // si une demande de contact a été acceptée
    if (data['notification'] == 'accepted-contact-request') {

    }
    // si une demande de contact a été refusée
    if (data['notification'] == 'declined-contact-request') {
      
    }
    // si une demande de contact a été reçue
    if (data['notification'] == 'contact-request-received') {
      conversation_window = $('body').find('[data-pconversation-user-name="' + data["sender_name"] + '"]');
      has_no_contact_requests = $('#contacts-requests ul').find('.no-requests');
      contact_request = data['contact_request'];

      if (has_no_contact_requests.length) {
        // supprimer le message indiquant qu'il n'y a pas de demande de contact
        has_no_contact_requests.remove();
      }

      if (conversation_window.length) {
        // supprimer le bouton d'ajout d'utilisateur aux contacts
        conversation_window.find('.add-user-to-contacts-message').parent().remove();

        conversation_window.find('.add-user-to-contacts').remove();
        conversation_window.find('.conversation-heading').css('width', '360px');
      }

      // ajouter une nouvelle demande de contact
      $('#contacts-requests ul').prepend(contact_request);
      calculateContactRequests();
    }

  },
  contact_request_response: function(sender_user_name, receiver_user_name, notification) {
    return this.perform('contact_request_response', {
      sender_user_name: sender_user_name,
    	receiver_user_name: receiver_user_name,
    	notification: notification
    });
  }
});
```

Notez que les instructions `if`, où une demande de contact a été acceptée et refusée, ont des blocs de code vides. Vous pouvez vous amuser à y ajouter votre propre code.

Créez également un fichier `contact_requests.js` pour effectuer des modifications du DOM après certains événements et diffuser les actions effectuées à l'utilisateur opposé, en utilisant la fonction de rappel `contact_request_response` :

```js
$(document).on('turbolinks:load', function() {
    // quand une demande de contact est acceptée, la marquer comme acceptée
    $('body').on('click', '.accept-request a', function() {
        var sender_user_name = $('nav #user-name').html();
        var receiver_user_name = $(this)
                                    .parents('[data-user-name]')
                                    .attr('data-user-name');
                                    
        var requests_menu_item = $('#contacts-requests ul');
        requests_menu_item = requests_menu_item
                                 .find('\
                                       [data-user-name="' + 
                                       receiver_user_name + 
                                       '"]');
        var conversation_window_request_status = $('.conversation-window')
                                                    .find('[data-user-name="' + 
                                                           receiver_user_name + 
                                                           '"]');
        // si une conversation est ouverte dans le messenger                                            
        if(conversation_window_request_status.length == 0) {
          conversation_window_request_status = $('.contact-request-status');
        }   
        requests_menu_item.find('.decline-request').remove();
        requests_menu_item
            .find('.accept-request')
            .replaceWith('<span class="accepted-request">Accepted</span>');
        requests_menu_item
            .removeClass('contact-request')
            .addClass('contact-request-responded');
        conversation_window_request_status
            .replaceWith('<div class="contact-request-status">\
                              Request has been accepted\
                          </div>');
        calculateContactRequests();
        // mettre à jour l'utilisateur opposé avec votre réponse à la demande de contact
        App.notification.contact_request_response(sender_user_name, 
                                                  receiver_user_name, 
                                                  'accepted-contact-request');
    });
    
    // quand une demande de contact est refusée, la marquer comme refusée
    $('body').on('click', '.decline-request a', function() {
        var sender_user_name = $('nav #user-name').html();
        var receiver_user_name = $(this)
                                    .parents('[data-user-name]')
                                    .attr('data-user-name');
        var requests_menu_item = $('#contacts-requests ul')
                                    .find('[data-user-name="' + 
                                           receiver_user_name + 
                                           '"]');
        var conversation_window_request_status = $('.conversation-window')
                                                    .find('[data-user-name="' + 
                                                           receiver_user_name + 
                                                           '"]');
        // si une conversation est ouverte dans le messenger                                            
        if(conversation_window_request_status.length == 0) {
          conversation_window_request_status = $('.contact-request-status');
        }   
        requests_menu_item.find('.accept-request').remove();
        requests_menu_item
            .find('.decline-request')
            .replaceWith('<span class="accepted-request">Declined</span>');
        requests_menu_item
            .removeClass('contact-request')
            .addClass('contact-request-responded');
        conversation_window_request_status
            .replaceWith('<div class="contact-request-status">\
                              Request has been declined\
                          </div>');
        calculateContactRequests();
        // mettre à jour l'utilisateur opposé avec votre réponse à la demande de contact
        App.notification.contact_request_response(sender_user_name, 
                                                  receiver_user_name, 
                                                  'declined-contact-request');
    });

    // quand une demande de contact est envoyée
    $('body').on('click', '.add-user-to-contacts-notif', function() {
        var sender_user_name = $('nav #user-name').html();
        var receiver_user_name = $(this)
                                    .parents('.conversation-window')
                                    .find('.contact-name-notif')
                                    .html();
        App.notification.contact_request_response(sender_user_name, 
                                                  receiver_user_name, 
                                                  'contact-request-received');
    });

    calculateContactRequests();
});

function calculateContactRequests() {
  var unresponded_requests = $('#contacts-requests ul')
                                .find('.contact-request')
                                .length;
  if (unresponded_requests) {
    $('#unresponded-contact-requests').css('visibility', 'visible');
    $('#unresponded-contact-requests').text(unresponded_requests);
  } else {
    $('#unresponded-contact-requests').css('visibility', 'hidden');
    $('#unresponded-contact-requests').text('');
  }
}
```

De plus, après l'envoi d'une nouvelle demande de contact depuis une fenêtre de conversation, supprimez l'option d'envoi de la demande à nouveau. Dans le fichier `options.js` de la conversation, ajoutez ce qui suit :

```js
// lors du clic sur le lien add-user-to-contacts
// supprimer le lien et notifier que la demande a été envoyée
$(document).on('click', 
               '.add-user-to-contacts, .add-user-to-contacts-notif', 
               function(e) {
    var conversation_window = $(this).parents('.conversation-window,\
                                               .conversation');
    conversation_window
        .find('.add-user-to-contacts')
        .replaceWith('<div class="contact-request-sent"\
                           style="display: block;">\
                          <div>\
                              <i class="fa fa-question"\
                                 aria-hidden="true"\
                                 title="Contact request sent">\
                              </i>\
                          </div>\
                      </div>');
    conversation_window.find('.add-user-to-contacts-message').remove();
    conversation_window
        .find('.messages_list ul')
        .append('<div class="add-user-to-contacts-message">\
                     Contact request sent\
                 </div>');
});
```