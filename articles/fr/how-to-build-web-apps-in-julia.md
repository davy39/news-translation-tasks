---
title: Comment construire votre première application Web en Julia avec Genie.jl 🧞‍♂️
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-01T21:33:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-web-apps-in-julia
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Web-applications-in-Julia.png
tags:
- name: Julialang
  slug: julialang
- name: Julia
  slug: julia
- name: Web Applications
  slug: web-applications
- name: Web Development
  slug: web-development
seo_title: Comment construire votre première application Web en Julia avec Genie.jl
  🧞‍♂️
seo_desc: "By Logan Kilpatrick\nJulia is a high-level, dynamic, and open-source programming\
  \ language. It's designed to be as easy to use as Python while remaining as performant\
  \ as C or C++. \nMany early use cases for Julia were in the scientific domains where\
  \ mas..."
---

Par Logan Kilpatrick

Julia est un langage de programmation haut niveau, dynamique et open-source. Il est conçu pour être aussi facile à utiliser que Python tout en restant aussi performant que C ou C++. 

De nombreux premiers cas d'utilisation de Julia étaient dans les domaines scientifiques où un traitement computationnel massif était et est encore requis. Mais à mesure que le langage continue de croître, de plus en plus de cas d'utilisation gagnent en popularité (indice : développement web). 

Si vous êtes totalement nouveau dans Julia et que vous souhaitez maîtriser la syntaxe avant de vous lancer dans la création de votre première application web, [consultez cet article sur freeCodeCamp](https://www.freecodecamp.org/news/learn-julia-programming-language/).

Il couvre les bases, comment installer Julia, les étapes pour installer des packages, et bien plus encore ! 

Nous allons nous concentrer dans ce tutoriel sur toutes les étapes nécessaires pour construire votre première application web en Julia à partir de zéro. Alors commençons par consulter le site web de Genie : [https://genieframework.com](https://genieframework.com).

## Qu'est-ce que Genie.jl ? 🧠

Genie est un framework web moderne et hautement productif écrit en Julia. Selon les propres mots du projet :

> Genie est un framework web full-stack qui fournit un flux de travail rationalisé et efficace pour développer des applications web modernes. Il s'appuie sur les forces de Julia (haut niveau, haute performance, dynamique, compilé JIT), exposant une API riche et un ensemble d'outils puissant pour un développement web productif.

Genie est très similaire au [Projet Django](https://www.djangoproject.com) en ce sens que Genie est plus qu'un simple framework. Au lieu de cela, il s'agit d'un écosystème entier avec des extensions et autres. 

Mais pourquoi avons-nous besoin de Genie ? La réponse simple est que, à mesure que Julia continue de gagner en popularité, de plus en plus de développeurs cherchent à exploiter Julia dans toute leur stack. Genie fournit la capacité de déployer des sites web avec du code Julia s'exécutant côté serveur afin que vous puissiez faire des choses comme déployer des modèles de machine learning dans le cadre de votre application Genie.

Avant de plonger dans la prise en main de Genie, vous pourriez vouloir consulter une application Genie déployée en direct pour avoir une idée de ce qui est possible : [https://pkgs.genieframework.com](https://pkgs.genieframework.com). 

Ce projet est une ressource communautaire où vous pouvez interroger le nombre de téléchargements de packages pendant une certaine période pour un package spécifique. Tapez "genie" pour voir le nombre de téléchargements quotidiens.

Vous pourriez également être intéressé à en apprendre davantage sur d'autres frameworks de développement GUI et web en Julia. Pour en savoir plus sur l'écosystème, [consultez cet article]( https://towardsdatascience.com/6-julia-frameworks-to-create-desktop-guis-and-web-apps-9ae1a941f115).

## Comment installer Genie ⤴️

Pour installer Genie, tout ce que nous avons à faire est d'ouvrir le REPL de Julia et de taper `] add Genie`. Cela s'occupera de tout ce dont vous avez besoin. Si tout fonctionne, vous devriez pouvoir faire :

```julia
julia> using Genie

```

sans aucun problème. Vous êtes maintenant prêt à commencer à essayer Genie.

## Comment mapper les URL aux fonctions Julia 🎯

Une partie centrale du framework Genie est l'idée d'un routeur. Les routeurs prennent l'action de l'utilisateur de visiter une URL spécifique et l'associent à l'appel d'une fonction Julia.

Regardons un exemple simple de cela. Dans le REPL, tapez ce qui suit :

```julia
julia> using Genie, Genie.Router

julia> route("/hello") do
           "Hello freeCodeCamp"
       end
[GET] /hello => #5 | :get_hello
```

Dans cet exemple, nous avons défini l'URL "/hello" pour retourner le texte "Hello freeCodeCamp". Nous pouvons vérifier que cela fonctionne en démarrant le serveur :

```julia
julia> up() # start server
┌ Info: 
└ Web Server starting at http://127.0.0.1:8000 
Genie.AppServer.ServersCollection(Task (runnable) @0x000000011c5c5bb0, nothing)
```

Maintenant que le serveur est en cours d'exécution, nous pouvons visiter [`http://127.0.0.1:8000`](http://127.0.0.1:8000) dans notre navigateur. Vous remarquerez que nous obtenons une page 404, ce qui est attendu puisque la seule route que nous avons définie était "/hello". Alors ajoutons cela à l'URL et voyons ce que nous obtenons :

![Fenêtre du navigateur montrant rien d'autre que le texte "Hello freeCodeCamp"](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-29-at-8.25.53-AM.png)

Et voilà ! Notre première étape vers la construction d'une application web entièrement fonctionnelle est terminée. Nous pouvons également confirmer que la page se charge correctement en vérifiant le REPL qui montre ceci :

```julia
julia> ┌ Error: GET / 404
└ @ Genie.Router ~/.julia/packages/Genie/UxbVJ/src/Router.jl:163
┌ Error: GET /favicon.ico 404
└ @ Genie.Router ~/.julia/packages/Genie/UxbVJ/src/Router.jl:163
[ Info: GET /hello 200
```

Nous voyons la première tentative où le résultat était une erreur 404 et lors de la deuxième tentative où nous avons réussi à obtenir la réponse (le message 200 signifie que tout est correct).

Maintenant que nous avons un exemple de base qui fonctionne, essayons de construire quelque chose de plus approfondi. 

Pour ce faire, nous allons créer un nouveau fichier. J'utiliserai VS Code, mais vous êtes libre d'utiliser l'IDE que vous trouvez utile. Avant de regarder le prochain morceau de code, nous devons nous assurer d'arrêter le serveur en tapant `down()` dans le REPL. 

D'accord, passons à l'exemple suivant :

```julia
using Genie, Genie.Router
using Genie.Renderer, Genie.Renderer.Html, Genie.Renderer.Json

route("/") do
    html("Hey freeCodeCamp")
end

route("/hello.html") do
  html("Hello freeCodeCamp (in html)")
end

route("/hello.json") do
  json("Hi freeCodeCamp (in json)")
end

route("/hello.txt") do
   respond("Hiya freeCodeCamp (in txt format)", :text)
end

# Launch the server on a specific port, 8002
# Run the task asynchronously
up(8002, async = true)
```

Beaucoup de choses se passent dans cet exemple, alors parcourons ce qui se passe. 

Nous commençons par charger les packages que nous voulons. Ensuite, nous définissons 4 routes différentes. La première est la route d'index. Ainsi, lorsque l'utilisateur visite [`http://127.0.0.1:8002`](http://127.0.0.1:8002), il verra "Hey freeCodeCamp". Les routes après l'index mettent en évidence le fait que chaque route peut donner une sortie personnalisée. Dans certains cas, il peut s'agir de HTML, dans d'autres, il pourrait s'agir de JSON ou de texte brut. 

La dernière ligne de cet exemple présente le code de lancement du serveur. Comme le précise le commentaire, nous pouvons définir le numéro de port spécifique et choisir si nous voulons que les routes s'exécutent de manière asynchrone ou non. Nous avons maintenant créé avec succès notre premier [Script Genie](https://genieframework.com/docs/tutorials/Getting-Started.html#developingasimplegeniescript) ! 

## Comment créer un service web de base 🔮

Maintenant que nous avons mis les mains dans le cambouis avec les bases, nous allons maintenant commencer à nous rapprocher de la construction d'une application web complète. 

Avant d'aller jusqu'au bout, nous allons faire le premier pas qui consiste à créer un service web de base. Pour ce faire, nous allons entrer dans le REPL et changer notre répertoire actuel pour un répertoire facilement accessible. J'utiliserai mon bureau dans ce tutoriel :

```julia
shell> cd Desktop
/Users/logankilpatrick/Desktop
```

Pour entrer en mode shell comme montré ci-dessus, il suffit de taper un ";" dans le REPL. Maintenant que nous avons notre répertoire actif défini sur le bureau dans mon cas, nous allons utiliser la fonction génératrice pratique pour créer le service :

```julia
julia> Genie.newapp_webservice("freeCodeCampApp")

[ Info: Done! New app created at /Users/logankilpatrick/Desktop/freeCodeCampApp
[ Info: Changing active directory to /Users/logankilpatrick/Desktop/freeCodeCampApp
    /var/folders/tc/519vfm453fj_x5bmd8pwx9480000gn/T/jl_bO1R8h/FreeCodeCampApp/Project.toml
[ Info: Project.toml has been generated
[ Info: Installing app dependencies
...
```

La fonction `newapp_webservice` est une fonction très utile qui crée automatiquement toutes les pièces dont nous avons besoin pour notre premier service web. Maintenant que nous avons un projet créé, nous devons l'ouvrir dans un IDE (dans mon cas, VS Code). Vous devriez voir ce qui suit si vous ouvrez le bon dossier :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-30-at-7.39.23-PM.png)

Il y a beaucoup de fichiers créés automatiquement pour nous. Le principal que nous allons examiner est `routes.jl` qui est utilisé pour créer des routes comme nous l'avons fait dans la section ci-dessus. 

La fonction que nous avons appelée pour générer ces dossiers démarre automatiquement le serveur, alors jetons un rapide coup d'œil à la page d'accueil existante en visitant [http://127.0.0.1:8000](http://127.0.0.1:8000) :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-30-at-7.51.16-PM.png)

Comme vous pourriez le remarquer, ma page semble un peu différente de la vôtre car je suis allé modifier la page `welcome.html` trouvée dans le dossier public. 

Comme vous pouvez le voir dans `routes.jl`, lorsque l'utilisateur visite l'URL principale `/`, nous le redirigeons vers la page de bienvenue. Nous pouvons ajouter des routes supplémentaires comme nous l'avons fait dans la section ci-dessus et étendre cela. Vous êtes libre de faire une pause ici et de jouer un peu. Nous avons déjà un site web assez robuste configuré.

Si vous jetez un coup d'œil dans certains des autres dossiers comme `config/env`, vous verrez des détails sur la définition du port, de l'URL de l'hôte et d'autres paramètres pertinents. Encore une fois, n'hésitez pas à jouer avec cela, mais nous n'entrerons pas dans tous les détails de ces fichiers dans ce tutoriel. 

Avant de plonger dans le prochain sujet, jetons un coup d'œil à quelques-uns des autres fichiers générés pour notre service web de base :

* Le dossier public contient tous les fichiers front-end (HTML et CSS)
* Le dossier `src` contient le point d'entrée du service web (dans mon cas `freeCodeCampApp.jl`)
* bin contient quelques dépendances supplémentaires que nous ignorerons à nouveau
* Manifest.toml et Project.toml sont les fichiers clés de Julia qui nous permettent de maintenir nos dépendances Julia. Lorsque vous avez créé le service web, le script a automatiquement activé votre environnement de projet actuel (qui est l'application que nous venons de créer). Vous pouvez vérifier cela en tapant "]" dans le REPL, ce qui montrera l'espace actif en bleu :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-30-at-7.59.49-PM.png)

Cela signifie simplement que si nous essayons d'ajouter un package, il l'ajoutera au fichier de projet et de manifest spécifique à ce projet, au lieu de celui partagé globalement.

## Comment créer une application web entièrement fonctionnelle avec une base de données 📽

Maintenant que nous avons exploré les bases, nous allons plonger dans une application web complète. Encore une fois, Genie fournit quelques fonctions utiles pour nous aider à démarrer. Avant de la créer, nous devrons revenir au bureau :

```julia
shell> pwd
/Users/logankilpatrick/Desktop/freeCodeCampApp

shell> cd ..
/Users/logankilpatrick/Desktop

shell> 
```

Rappelez-vous, vous pouvez taper `;` pour entrer en mode shell et backspace pour quitter le mode shell. Maintenant, créons l'application :

```julia
julia> Genie.newapp_mvc(Genie.newapp_mvc("freeCodeCampMVC"))
   Resolving package versions...
   ...
```

Vous serez invité à choisir un backend de base de données. Pour cet exemple, nous utiliserons SQLite :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-30-at-8.08.31-PM.png)

Si vous souhaitez utiliser un autre backend de base de données, n'hésitez pas à le faire également. Mais notez que vous devrez créer le fichier de base de données automatiquement. Genie ne crée qu'un fichier SQLite pour vous. 

Nous avons maintenant une application MVC créée. Mais vous pourriez vous demander, qu'est-ce qu'un MVC ? 

Le paradigme Modèle-Vue-Contrôleur est très courant dans le développement d'applications. Dans l'intérêt de ne pas entrer dans les détails, je vous [renvoie à cet article](https://www.freecodecamp.org/news/mvc-architecture-what-is-a-model-view-controller-framework/) où vous pouvez lire les détails. Du point de vue des développeurs, il n'y a pas beaucoup d'impact. 

Tout comme nous l'avons fait lorsque nous avons créé le dernier projet, nous devons l'ouvrir à nouveau dans l'IDE :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-01-at-6.44.21-AM.png)

Encore une fois, nous verrons beaucoup des mêmes éléments qu'auparavant avec l'ajout du dossier `app` qui contiendra beaucoup de code critique. Nous pouvons voir à quoi ressemble le nouveau projet en tapant :

```julia
julia> loadapp()

julia> up()
```

et en naviguant ensuite vers : [http://127.0.0.1:8000](http://127.0.0.1:8000).

Ensuite, nous devrons connecter notre base de données à l'application web que nous avons créée. Pour ce faire, rendez-vous dans `db/connection.yml` et modifiez la section suivante :

```yml
env: ENV["GENIE_ENV"]

dev:
  adapter: SQLite
  database: db/freeCodeCamp_courses.sqlite
```

Vous pouvez laisser les autres champs vides pour l'instant. Ensuite, nous devons exécuter :

```julia
julia> include(joinpath("config", "initializers", "searchlight.jl"))
```

ce qui chargera la configuration de la base de données. Ensuite, nous allons continuer à configurer la base de données de manière à pouvoir sauvegarder les données de notre application dans un stockage persistant.

Nous commençons ce processus en créant une nouvelle ressource :

```julia
julia> Genie.newresource("course")
```

Une fois que nous avons défini une ressource, l'étape suivante consiste à aller modifier la table des migrations de la base de données qui se trouve dans `db/migrations/2022020115190055_create_table_courses.jl` dans mon cas. 

Par défaut, la table est déjà remplie avec un texte de remplissage basé sur les dernières commandes que nous avons exécutées. Elle devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-01-at-7.22.35-AM.png)

Nous allons modifier le fichier pour qu'il corresponde au schéma spécifique que nous voulons. Cela dépendra entièrement de l'application elle-même. Puisque je crée des cours sur ce site, je vais entrer tous les détails des cours comme suit :

```julia
module CreateTableCourses

import SearchLight.Migrations: create_table, column, columns, pk, add_index, drop_table, add_indices

function up()
  create_table(:courses) do
    [
      pk()
      column(:title, :string, limit = 200)
      column(:authors, :string, limit = 250)
      column(:year, :integer, limit = 4)
      column(:rating, :string, limit = 10)
      column(:categories, :string, limit = 100)
      column(:description, :string, limit = 1_000)
      column(:cost, :float, limit = 1000)
    ]
  end

  add_index(:courses, :title)
  add_index(:courses, :authors)
  add_index(:courses, :categories)
  add_index(:courses, :description)

end

function down()
  drop_table(:courses)
end

end
```

Encore une fois, ceux-ci sont arbitraires et peuvent être ce que vous voulez qu'ils soient. 

Il est intéressant de noter que l'ajout de l'index est facultatif. La raison pour laquelle vous l'ajouteriez est qu'il accélère les requêtes, mais il y a d'autres compromis et vous ne pouvez pas réellement charger toutes les colonnes en tant qu'index. Vous pouvez en lire plus sur certains de ces compromis [ici](https://stackoverflow.com/questions/5447987/why-cant-i-simply-add-an-index-that-includes-all-columns/5448055#5448055) et [ici](https://stackoverflow.com/questions/107132/what-columns-generally-make-good-indexes).

Maintenant que nous avons mis à jour la table de la base de données, nous devons propager ces mises à jour. Pour ce faire, nous allons utiliser `SearchLight.jl` qui fonctionne comme le système de migration de notre application :

```julia
julia> using SearchLight

julia> SearchLight.Migration.create_migrations_table()
┌ Info: 2022-02-01 07:37:11 CREATE TABLE `schema_migrations` (
│       `version` varchar(30) NOT NULL DEFAULT '',
│       PRIMARY KEY (`version`)
└     )
[ Info: 2022-02-01 07:37:11 Created table schema_migrations

julia> SearchLight.Migration.status()
[ Info: 2022-02-01 07:37:20 SELECT version FROM schema_migrations ORDER BY version DESC
|   | Module name & status                     |
|   | File name                                |
|---|------------------------------------------|
|   |                 CreateTableCourses: DOWN |
| 1 | 2022020115190055_create_table_courses.jl |

julia> SearchLight.Migration.last_up()
[ Info: 2022-02-01 07:37:29 SELECT version FROM schema_migrations ORDER BY version DESC
[ Info: 2022-02-01 07:37:29 CREATE TABLE courses (id INTEGER PRIMARY KEY , title TEXT  , authors TEXT  , year INTEGER (4) , rating TEXT  , categories TEXT  , description TEXT  , cost FLOAT (1000) )
[ Info: 2022-02-01 07:37:29 CREATE  INDEX courses__idx_title ON courses (title)
[ Info: 2022-02-01 07:37:29 CREATE  INDEX courses__idx_authors ON courses (authors)
[ Info: 2022-02-01 07:37:29 CREATE  INDEX courses__idx_categories ON courses (categories)
[ Info: 2022-02-01 07:37:29 CREATE  INDEX courses__idx_description ON courses (description)
[ Info: 2022-02-01 07:37:29 INSERT INTO schema_migrations VALUES ('2022020115190055')
[ Info: 2022-02-01 07:37:29 Executed migration CreateTableCourses up
```

Nous avons maintenant terminé avec succès les migrations. Si vous deviez apporter une modification au schéma, vous devriez relancer les commandes ci-dessus pour que ces modifications de base de données prennent effet. 

La dernière étape de ce processus consiste à définir notre modèle. Cela nous permettra de créer des objets dans le code Julia et de les sauvegarder dans la base de données que nous venons de définir. Nous devons naviguer vers `app/resources/courses/Courses.jl` ou le chemin équivalent pour apporter ces dernières mises à jour : 

```julia
module Courses

import SearchLight: AbstractModel, DbId
import Base: @kwdef

export Course

@kwdef mutable struct Course <: AbstractModel
  id::DbId = DbId()
  title::String = ""
  authors::String = ""
  year::Int = 0
  rating::String = ""
  categories::String = ""
  description::String = ""
  cost::Float64 = 0.0
end

end
```

Encore une fois, cela devrait être le même que le contenu que vous avez précédemment défini. Pour vous assurer que cela a fonctionné, nous pouvons faire :

```julia
julia> using Courses
[ Info: 2022-02-01 07:43:51 Precompiling Courses [top-level]
```

et ensuite essayer de créer un cours via :

```julia

julia> c = Course(title = "Web dev with Genie.jl", authors="Logan Kilpatrick")
Course
| KEY                 | VALUE                 |
|---------------------|-----------------------|
| authors::String     | Logan Kilpatrick      |
| categories::String  |                       |
| cost::Float64       | 0.0                   |
| description::String |                       |
| id::DbId            | NULL                  |
| rating::String      |                       |
| title::String       | Web dev with Genie.jl |
| year::Int64         | 0                     |
```

Nous avons créé avec succès notre premier objet ! Mais il n'est pas sauvegardé dans la base de données tout de suite. Nous pouvons vérifier cela en faisant :

```julia
julia> ispersisted(c)
false
```

nous devons donc exécuter :

```julia
julia> save(c)
[ Info: 2022-02-01 07:47:04 INSERT  INTO courses ("title", "authors", "year", "rating", "categories", "description", "cost") VALUES ('Web dev with Genie.jl', 'Logan Kilpatrick', 0, '', '', '', 0.0) 
[ Info: 2022-02-01 07:47:04 ; SELECT CASE WHEN last_insert_rowid() = 0 THEN -1 ELSE last_insert_rowid() END AS LAST_INSERT_ID
true

```

et maintenant le cours est sauvegardé ! Mais pour vraiment tester cela, nous devons permettre à l'utilisateur de créer un cours. Retournons à `routes.jl` et activons cela :

```julia
using Genie, Genie.Router, Genie.Renderer.Html, Genie.Requests
using Courses

form = """
<form action="/" method="POST" enctype="multipart/form-data">
  <input type="text" name="name" value="" placeholder="What's the course name?" />
  <input type="text" name="author" value="" placeholder="Who is the course author?" />

  <input type="submit" value="Submit" />
</form>
"""

route("/") do
  html(form)
end

route("/", method = POST) do
  c = Course(title=postpayload(:name, "Placeholder"), authors=postpayload(:author, "Placeholder"))
  save(c)
  "Course titled $(c.title) created successfully!"
end
```

Nous avons commencé par définir un simple formulaire HTML (rien de nouveau ou d'excitant ici), puis, nous avons fait en sorte que la route par défaut `/` rende le formulaire HTML. Enfin, nous créons une autre route pour l'URL `/`, mais spécifiquement pour la méthode POST. À l'intérieur de cette route, nous créons un nouveau cours en extrayant les informations que nous voulons du formulaire à partir de la charge utile via `postpayload`. 

Vous pouvez essayer cela en naviguant vers : [http://127.0.0.1:8000](http://127.0.0.1:8000)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screen-Shot-2022-02-01-at-8.11.38-AM.png)

Vous pouvez essayer d'entrer certains des détails et ensuite appuyer sur soumettre. Pour vous assurer que les soumissions ont fonctionné, vous pouvez faire :

```julia
julia> all(Course)
[ Info: 2022-02-01 08:10:19 SELECT "courses"."id" AS "courses_id", "courses"."title" AS "courses_title", "courses"."authors" AS "courses_authors", "courses"."year" AS "courses_year", "courses"."rating" AS "courses_rating", "courses"."categories" AS "courses_categories", "courses"."description" AS "courses_description", "courses"."cost" AS "courses_cost" FROM "courses" ORDER BY courses.id ASC
┌ Warning: 2022-02-01 08:10:19 Unsupported SQLite declared type INTEGER (4), falling back to Int64 type
└ @ SQLite ~/.julia/packages/SQLite/aDggE/src/SQLite.jl:416
┌ Warning: 2022-02-01 08:10:19 Unsupported SQLite declared type FLOAT (1000), falling back to Float64 type
└ @ SQLite ~/.julia/packages/SQLite/aDggE/src/SQLite.jl:416
3-element Vector{Course}:
 Course
| KEY                 | VALUE                 |
|---------------------|-----------------------|
| authors::String     | Logan Kilpatrick      |
| categories::String  |                       |
| cost::Float64       | 0.0                   |
| description::String |                       |
| id::DbId            | 1                     |
| rating::String      |                       |
| title::String       | Web dev with Genie.jl |
| year::Int64         | 0                     |

 Course
| KEY                 | VALUE       |
|---------------------|-------------|
| authors::String     | Logan K     |
| categories::String  |             |
| cost::Float64       | 0.0         |
| description::String |             |
| id::DbId            | 2           |
| rating::String      |             |
| title::String       | Test course |
| year::Int64         | 0           |
```

ce qui devrait montrer que les entrées ont été sauvegardées dans la base de données.

## Conclusion 🎁

Wow, c'était beaucoup. Nous avons couvert une quantité énorme de terrain dans ce seul tutoriel. 

Cela dit, il y a encore plus à apprendre sur Genie. Je vous suggère vivement de consulter [la documentation ici](https://genieframework.com/docs/tutorials/Overview.html), qui contient de nombreux autres tutoriels sur des sujets comme les API REST, l'authentification, et bien plus encore. 

## Obtenir de l'aide avec Genie.jl 🚨

Si vous rencontrez des problèmes avec ce tutoriel ou lors de l'utilisation de Genie, veuillez poser une question sur Stack Overflow avec les tags `genie.jl` et `julia` ou sur le [Julia Discourse](https://discourse.julialang.org). Après cela, n'hésitez pas à tweeter le lien vers la question à mon attention et je ferai de mon mieux pour aider : [https://twitter.com/OfficialLoganK](https://twitter.com/OfficialLoganK).