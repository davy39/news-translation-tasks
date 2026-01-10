---
title: Comment effectuer la localisation dans les applications Phoenix avec Gettext
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-27T06:46:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-localization-in-phoenix-applications-with-gettext-c38bb0f01bef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9FLnNCwPgLPZBvQ4pfwnzg.jpeg
tags:
- name: localization
  slug: localization
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: translation
  slug: translation
seo_title: Comment effectuer la localisation dans les applications Phoenix avec Gettext
seo_desc: 'By Anastasia

  In my previous tutorial, we discussed how to introduce support for I18n into Rails
  apps. Today we will continue covering back-end frameworks and talk about localization
  of Phoenix applications with the help of Gettext.

  You might not have...'
---

Par Anastasia

Dans mon précédent tutoriel, nous avons discuté de [comment introduire le support de l'I18n dans les applications Rails](https://blog.lokalise.co/rails-i18n/). Aujourd'hui, nous allons continuer à couvrir les frameworks backend et parler de la _localisation des applications Phoenix_ avec l'aide de _Gettext_.

Vous n'avez peut-être jamais entendu parler de [Phoenix](http://phoenixframework.org/) auparavant, alors laissez-moi en dire quelques mots. Il s'agit d'un framework MVC côté serveur écrit en [Elixir](https://elixir-lang.org/), qui est un langage de programmation fonctionnelle fonctionnant sur la [machine virtuelle Erlang](https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine)). Le framework lui-même est assez jeune, mais il est très prometteur grâce aux fonctionnalités d'Erlang et d'Elixir. Il est très rapide, scalable et orienté concurrency, ce qui est vraiment important pour les applications fortement chargées.

[Gettext](https://www.gnu.org/software/gettext/manual/gettext.html#Why), quant à lui, est un outil I18n maintenu par GNU qui peut être utilisé pour les applications web, de bureau et même dans les systèmes d'exploitation.

Tout au long de cet article, nous allons localiser un projet de démonstration Phoenix et voir Gettext en action. Nous discuterons également de la manière d'introduire le support pour le changement de locale et de persister les préférences de l'utilisateur tout au long des requêtes. Avant de passer à la partie principale du tutoriel, vous pourriez également vouloir apprendre les recommandations communes [qui sont listées dans notre récent article](https://blog.lokalise.co/localization-5-focus-points/).

### Bonjour, Gettext !

D'accord, plongeons directement dans le code et observons la localisation des applications Phoenix en pratique. Créez un nouveau projet sans SGBD par défaut et changez de répertoire pour le projet :

```
mix phx.new lokalise_demo --no-ecto cd lokalise_demo
```

Il semble que Phoenix ait un support pour Gettext dès le départ : vous n'avez pas besoin d'installer de bibliothèques tierces. De plus, si vous naviguez vers le fichier `demo/lib/demo_web/templates/page/index.html.eex`, vous remarquerez la ligne de code suivante :

```
<h2><%= gettext "Welcome to %{name}!", name: "Phoenix" %></h2>
```

Que se passe-t-il ici ? Eh bien, `gettext` [est une fonction](https://hexdocs.pm/gettext/Gettext.html#gettext/2) qui tente de charger la traduction pour la chaîne `"Welcome to %{name}!"`. `%{name}` ici est un [espace réservé qui sera remplacé](https://hexdocs.pm/gettext/Gettext.html#module-interpolation) par une chaîne `"Phoenix"` comme dicté par le deuxième argument `name: "Phoenix"` (cet argument contient les dites _bindings_).

Par défaut, les applications Phoenix ont l'anglais comme locale par défaut, et aucune autre locale n'est supportée. Cependant, vous pouvez facilement changer cela en ajoutant une nouvelle ligne au fichier `config/config.exs` :

```
config :lokalise_demo, LokaliseDemoWeb.Gettext, locales: ~w(en ru)
```

Maintenant, nous supportons les locales anglais et russe.

L'étape suivante consiste à fournir des traductions pour la chaîne passée à la fonction `gettext` à l'intérieur du fichier `index.html.eex`. Le moyen le plus simple de le faire est d'extraire toutes les chaînes de traduction dans des fichiers séparés automatiquement :

```
mix gettext.extract mix gettext.merge priv/gettext mix gettext.merge priv/gettext --locale ru
```

Ces commandes vont créer trois nouveaux fichiers dans le dossier `priv/gettext`. Par conséquent, arrêtons-nous une seconde et parlons un peu plus de ces fichiers.

### Types de fichiers Gettext

La première commande ci-dessus, `mix gettext.extract`, recherche tous les messages Gettext qui nécessitent une traduction et les place dans le fichier `priv/gettext/default.pot`. POT signifie « portable object template », et ces fichiers servent de modèles pour les traductions spécifiques à une langue. Notre `default.pot` a le contenu suivant :

```
## This file is a PO Template file. ## ## msgid here are often extracted from source code. ## Add new translations manually only if they're dynamic ## translations that can't be statically extracted. ## ## Run mix gettext.extract to bring this file up to ## date. Leave msgstr empty as changing them here as no ## effect: edit them in PO (.po) files instead. msgid "" msgstr "" #, elixir-format #: lib/lokalise_demo_web/templates/page/index.html.eex:2 msgid "Welcome to %{name}!" msgstr ""
```

Le modèle montre commodément les lignes où se trouvent les messages extraits. `msgid` est la chaîne à traduire (certains développeurs peuvent s'y référer comme une « clé »). `msgstr` est, bien sûr, la traduction réelle.

Le nom du fichier POT — `default` — est également un [_nom de domaine_](https://hexdocs.pm/gettext/Gettext.html#module-domains) qui sert d'espace de noms. Initialement, il n'y a qu'un seul espace de noms, mais pour les grands sites avec des centaines de traductions, il peut être judicieux de créer plusieurs domaines et, par conséquent, de séparer les traductions dans différents fichiers.

La commande `mix gettext.merge priv/gettext --locale LOCALE_CODE_HERE` crée [des fichiers de traduction](https://hexdocs.pm/gettext/Gettext.html#module-translations) pour la langue donnée basée sur le modèle. Ces fichiers de traduction ont l'extension `.po` (« portable object ») et se trouvent dans le dossier `priv/gettext/LOCALE_CODE_HERE/LC_MESSAGES`. N'oubliez pas que pour fournir des traductions pour les messages, vous devez éditer ces fichiers PO, et non les modèles directement !

### Domaines Gettext

Comme mentionné précédemment, Gettext supporte plusieurs domaines ou espaces de noms. Lorsque vous utilisez la fonction `gettext/4`, vous supposez toujours un domaine `default`. Si vous souhaitez utiliser un espace de noms différent, utilisez la [fonction](https://hexdocs.pm/gettext/Gettext.html#dngettext/6) `[dgettext/6](https://hexdocs.pm/gettext/Gettext.html#dngettext/6)` à la place, qui accepte le domaine, le message, les bindings optionnels et quelques autres arguments :

```
<%= dgettext "custom_domain", "message is ${placeholder}", placeholder: "my binding" %>
```

Maintenant, la commande `mix gettext.extract` va créer un nouveau fichier `custom_domain.pot`. De même, l'exécution de `mix gettext.merge` crée un fichier `custom_domain.po` basé sur le modèle.

Notez une fois de plus que pour les petits sites, l'utilisation de plusieurs domaines est généralement excessive. Cependant, leur utilisation pour les grandes ressources est très recommandée car ainsi vous ne vous retrouvez pas avec des centaines de traductions dans un seul fichier. Une autre raison est la possibilité d'avoir les mêmes clés de traduction sous différents espaces de noms.

### Fournir des traductions

Ainsi, après avoir discuté de certains aspects internes de Gettext, nous pouvons maintenant traduire la chaîne `Welcome to %{name}!` en russe (ce message est déjà en anglais, donc bien sûr aucune traduction n'est nécessaire pour cette langue). Modifiez le fichier `priv/gettext/ru/LC_MESSAGES/default.po` comme suit :

```
# ... some other stuff goes here ... #, elixir-format #: lib/lokalise_demo_web/templates/page/index.html.eex:2 msgid "Welcome to %{name}!" msgstr "412430441 43f440438432435442441442432443435442 %{name}"
```

C'est tout ! Actuellement, nous n'avons aucun mécanisme pour changer de langue, donc définissez le russe comme [locale par défaut](https://hexdocs.pm/gettext/Gettext.html#module-default-locale) :

```
# config/config.exs config :lokalise_demo, LokaliseDemoWeb.Gettext, locales: ~w(en ru), default_locale: "ru" # <== modifiez cette ligne
```

Maintenant, démarrez le serveur en exécutant :

```
mix phx.server
```

Ouvrez la page `http://localhost:4000` dans votre navigateur et assurez-vous que le message traduit est affiché !

### Pluralisation avec Gettext

Une autre fonctionnalité importante que je souhaite couvrir est la [pluralisation](https://hexdocs.pm/gettext/Gettext.html#module-pluralization). Différentes langues ont différentes règles de pluralisation, et Gettext en supporte beaucoup dès le départ. Cependant, c'est à nous de fournir des traductions appropriées pour tous les cas potentiels.

Comme exemple très simple, disons combien de pommes l'utilisateur a. Supposons que nous ne connaissons pas la quantité exacte, ce qui signifie que la phrase peut se lire comme « 1 pomme » ou « X pommes ». Pour supporter la pluralisation, nous devons utiliser la [fonction](https://hexdocs.pm/gettext/Gettext.html#ngettext/5) `[ngettext/5](https://hexdocs.pm/gettext/Gettext.html#ngettext/5)` :

```
ngettext "You have 1 apple", "You have %{count} apples", 2
```

Cette fonction accepte les formes singulière et plurielle de la phrase, ainsi que le `count`. Sous le capot, Gettext prend ce compte et choisit la traduction appropriée basée sur les règles de pluralisation.

Ensuite, vous pouvez mettre à jour les fichiers POT et PO avec les commandes suivantes :

```
mix gettext.extract --merge priv/gettext mix gettext.extract --merge priv/gettext --locale=ru
```

Vous trouverez quelques nouvelles lignes dans les fichiers Gettext :

```
msgid "You have 1 apple" msgid_plural "You have %{count} apples" msgstr[0] "" msgstr[1] ""
```

`msgstr[0]` et `msgstr[1]` contiennent les traductions pour les formes singulière et plurielle respectivement. Pour l'anglais, nous n'avons pas besoin de faire autre chose, mais la langue russe nécessite quelques étapes supplémentaires :

```
msgid "You have one message" msgid_plural "You have %{count} messages" msgstr[0] "423 432430441 43e43443d43e 44f43143b43e43a43e" msgstr[1] "423 432430441 %{count} 44f43143b43e43a430" msgstr[2] "423 432430441 %{count} 44f43143b43e43a"
```

Les règles de pluralisation dans ce cas sont un peu plus complexes, donc nous devons fournir non pas deux, mais trois options possibles. Vous pouvez trouver plus d'informations sur le sujet [dans la documentation officielle](https://hexdocs.pm/gettext/Gettext.Plural.html).

### Choisir la locale de l'application

Comme je l'ai déjà mentionné précédemment, actuellement il n'y a aucun moyen de basculer entre les locales lors de la navigation dans l'application. C'est une fonctionnalité importante, alors ajoutons-la maintenant !

En fin de compte, nous avons deux solutions potentielles :

* Utiliser une solution tierce, par exemple le plug [set_locale](https://github.com/smeevil/set_locale) (la manière facile)
* Tout écrire à partir de zéro (la manière du guerrier)

Si vous choisissez de rester avec le plug tierce, les choses seront très simples en effet. Vous devez effectuer [seulement trois étapes rapides](https://github.com/smeevil/set_locale#setup) :

1. Installer le package
2. Ajouter un nouveau plug au fichier `router.ex`
3. Ajouter un nouveau `:locale` routing scope

Après cela, la [locale sera déduite](https://github.com/smeevil/set_locale#fallback-chain-and-precedence) de l'URL, des cookies, ou de l'en-tête de requête `accept-language`. Simple.

Cependant, dans ce tutoriel, je propose de choisir une manière plus complexe et d'écrire cette fonctionnalité à partir de zéro.

### Lire la locale à partir de l'URL

La manière la plus courante de spécifier la locale souhaitée est via l'URL. Le code de la langue peut faire partie du nom de domaine, ou faire partie du chemin :

* `[http://en.example.com/some/path](http://en.example.com/some/path)`
* `[http://example.com/en/some/path](http://example.com/en/some/path)`
* `[http://example.com/some/path?locale=en](http://example.com/some/path?locale=en)`

Restez avec la dernière option et fournissez la locale comme paramètre GET. Pour lire la valeur de la locale et faire quelque chose à ce sujet, nous avons besoin d'un [plug personnalisé](https://hexdocs.pm/phoenix/plug.html#module-plugs). Créez un nouveau fichier `lib/lokalise_demo_web/plugs/set_locale_plug.ex` avec le contenu suivant :

```
defmodule LokaliseDemoWeb.Plugs.SetLocale do import Plug.Conn # 1 @supported_locales Gettext.known_locales(LokaliseDemoWeb.Gettext) # 2 def init(_options), do: nil # 3 def call(%Plug.Conn{params: %{"locale" => locale}} = conn, _options) when locale in @supported_locales do # 4 end def call(conn, _options), do: conn # 5 end
```

Discutons de cet extrait de code :

1. Sur cette ligne, nous importons un comportement. Il nous oblige à remplir un certain contrat (voir ci-dessous).
2. Il s'agit de l'attribut de module avec une liste des locales supportées
3. Il s'agit de la réalisation réelle du contrat : un callback qui est invoqué automatiquement. Il peut retourner des options passées à la fonction `call/2`, ou simplement `nil`
4. Le `call/2` est initialisé avec tous les paramètres GET de la requête. Nous ne sommes intéressés que par la partie `locale` et la récupérons en utilisant le mécanisme de correspondance de motifs. Également sur cette ligne, nous avons une clause de garde qui garantit que la langue choisie est effectivement supportée
5. Il s'agit de la clause de repli qui est invoquée lorsque la locale passée n'est pas supportée. Dans ce cas, nous retournons simplement la connexion sans aucune modification.

La dernière chose que nous devons faire est de développer la première clause de la fonction `call/2`. Elle doit simplement définir la locale choisie comme locale actuelle :

```
def call(%Plug.Conn{params: %{"locale" => locale}} = conn, _options) when locale in @supported_locales do LokaliseDemoWeb.Gettext |> Gettext.put_locale(locale) conn end
```

Notez que la `conn` doit être retournée par la fonction `call/2` !

Le plug est prêt, et vous pouvez le placer à l'intérieur du pipeline `:browser` :

```
# lib/router.ex # ... pipeline :browser do plug :accepts, ["html"] plug :fetch_session plug :fetch_flash plug :protect_from_forgery plug :put_secure_browser_headers plug LokaliseDemoWeb.Plugs.SetLocale end
```

Maintenant, rechargez le serveur et naviguez vers `http://localhost:4000/?locale=en`. Le message de bienvenue devrait être en anglais, ce qui signifie que le plug personnalisé fonctionne comme prévu !

### Stocker la locale dans un cookie

Notre prochaine tâche est de persister la locale choisie parmi les requêtes afin que l'utilisateur n'ait pas besoin de la fournir à chaque fois. Le candidat parfait pour une telle persistance serait les cookies : de petits fichiers texte stockés sur l'ordinateur de l'utilisateur. Phoenix a effectivement un support pour les cookies dès le départ, alors utilisez simplement une [fonction](https://hexdocs.pm/plug/Plug.Conn.html#put_resp_cookie/4) `[put_resp_cookies/4](https://hexdocs.pm/plug/Plug.Conn.html#put_resp_cookie/4)` à l'intérieur de votre plug :

```
def call(%Plug.Conn{params: %{"locale" => locale}} = conn, _options) when locale in @supported_locales do LokaliseDemoWeb.Gettext |> Gettext.put_locale(locale) conn |> put_resp_cookie "locale", locale, max_age: 365*24*60*60 end
```

Nous modifions la connexion en stockant un cookie nommé `"locale"`. Il a une durée de vie de 1 an, ce qui signifie effectivement l'éternité en termes de web.

La dernière étape ici est de lire la locale choisie à partir du cookie. Malheureusement, nous ne pouvons plus utiliser une clause de garde pour cette tâche, alors remplaçons les deux clauses de la fonction `call/2` par une seule :

```
def call(conn, _options) do case fetch_locale_from(conn) do nil -> conn locale -> LokaliseDemoWeb.Gettext |> Gettext.put_locale(locale) conn |> put_resp_cookie "locale", locale, max_age: 365*24*60*60 end end
```

En fin de compte, la logique reste la même : nous récupérons la locale, la vérifions, puis soit nous ne faisons rien, soit nous la stockons comme locale actuelle.

Ajoutez deux fonctions privées pour finaliser cette fonctionnalité :

```
defp fetch_locale_from(conn) do (conn.params["locale"] || conn.cookies["locale"]) |> check_locale end defp check_locale(locale) when locale in @supported_locales, do: locale defp check_locale(_), do: nil
```

Ici, nous lisons la locale soit à partir du paramètre GET, soit du cookie, puis nous vérifions si la langue souhaitée est supportée. Ensuite, nous retournons soit le code de cette langue, soit simplement `nil`. Excellent travail !

Une autre manière assez courante de définir la locale est d'utiliser l'en-tête HTTP `Accept-Language`. Si vous souhaitez implémenter ce mécanisme, essayez d'utiliser [le code du plug set_locale](https://github.com/smeevil/set_locale/blob/fd35624e25d79d61e70742e42ade955e5ff857b8/lib/headers.ex) qui fournit déjà toutes les RegEx nécessaires et autres éléments sophistiqués.

### Contrôle de changement de locale

Ainsi, le plug `SetLocale` est prêt, mais nous n'avons toujours pas fourni de contrôles pour choisir la langue du site web. Par conséquent, affichons deux liens en haut de la page. Définissez un nouvel assistant dans le fichier `lib/views/layout_view.ex` :

```
defmodule LokaliseDemoWeb.LayoutView do use LokaliseDemoWeb, :view def new_locale(conn, locale, language_title) do "<a href=\"#{page_path(conn, :index, locale: locale)}\">#{language_title}</a>" |> raw end end
```

Appelez cet assistant à partir du modèle `templates/layout/app.html.eex` :

```
<body> <div class="container"> <header class="header"> <%= new_locale @conn, :en, "English" %> <%= new_locale @conn, :ru, "Russian" %> </header> <!-- other stuff --> </div> </body>
```

Rechargez la page et essayez de basculer entre les locales. Tout devrait fonctionner correctement, ce qui signifie que la tâche est terminée !

### Simplifiez votre vie avec Lokalise

À ce stade, vous pensez probablement que supporter plusieurs langues sur un grand site web est probablement une douleur. Et, honnêtement, vous avez raison. Bien sûr, les traductions peuvent être organisées en espaces de noms à l'aide de domaines. Mais vous devez toujours vous assurer que toutes les clés sont traduites pour chaque locale. Heureusement, il existe une solution à ce problème : la plateforme Lokalise qui [rend le travail avec les fichiers de localisation beaucoup plus simple](https://lokalise.co/features). Laissez-moi vous guider à travers la configuration initiale qui n'est vraiment pas complexe.

* Pour commencer, [obtenez votre essai gratuit](https://lokalise.co/signup)
* Créez un nouveau projet, donnez-lui un nom et définissez l'anglais comme langue de base
* Cliquez sur « Upload Language Files »
* Téléchargez les fichiers PO pour toutes vos langues
* Passez au projet et modifiez vos traductions selon vos besoins
* Vous pouvez également contacter un traducteur professionnel pour faire le travail à votre place
* Ensuite, téléchargez simplement vos fichiers PO et remplacez-les dans le dossier `priv/gettext`
* Profitez !

Lokalise a beaucoup plus de fonctionnalités, y compris le support pour des dizaines de plateformes et de formats, et même la possibilité de télécharger des captures d'écran afin de lire les textes à partir de celles-ci. Alors, restez avec Lokalise et simplifiez votre vie !

### Conclusion

Dans le tutoriel d'aujourd'hui, nous avons vu comment effectuer la localisation des applications Phoenix avec l'aide de Gettext. Nous avons discuté de ce qu'est Gettext et des bonnes choses qu'il a à offrir. Nous avons vu comment extraire les traductions, générer des modèles et créer des fichiers PO basés sur ces modèles. Vous avez également appris ce que sont les domaines et comment introduire le support pour la pluralisation. En plus de cela, nous avons créé avec succès notre plug personnalisé pour récupérer et persister la locale choisie basée sur les préférences de l'utilisateur. Pas mal pour un article !

Pour en savoir plus sur l'I18n de Phoenix, je vous encourage à consulter [le guide officiel](https://hexdocs.pm/gettext/Gettext.html) qui fournit à la fois des explications générales, ainsi que de la documentation pour les fonctions individuelles. Pour en savoir plus sur Gettext et ses fonctionnalités en détail, référez-vous à la [documentation de GNU](https://www.gnu.org/software/gettext/manual/gettext.html). Et, bien sûr, si vous avez des questions, n'hésitez pas à les poster dans les commentaires !

_Publié à l'origine sur [blog.lokalise.co](https://blog.lokalise.co/localization-of-phoenix-applications/) le 27 septembre 2018._