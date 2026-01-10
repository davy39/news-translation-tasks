---
title: 'Hugo vs Jekyll : une bataille épique des thèmes de générateurs de sites statiques'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-04-27T13:42:00.000Z'
originalURL: https://freecodecamp.org/news/hugo-vs-jekyll-battle-of-static-site-generator-themes
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/cover-2.png
tags:
- name: Hugo
  slug: hugo
- name: JAMstack
  slug: jamstack
- name: jekyll
  slug: jekyll
- name: Static Site Generators
  slug: static-site-generators
- name: themes
  slug: themes
- name: website development,
  slug: website-development
seo_title: 'Hugo vs Jekyll : une bataille épique des thèmes de générateurs de sites
  statiques'
seo_desc: 'In this article, we''ll compare the nuances of creating themes for the
  top two static site generators.

  I recently took on the task of creating a documentation site theme for two projects.
  Both projects needed the same basic features, but one uses Jeky...'
---

Dans cet article, nous allons comparer les nuances de la création de thèmes pour les deux principaux générateurs de sites statiques.

J'ai récemment entrepris la tâche de créer un thème de site de documentation pour deux projets. Les deux projets avaient besoin des mêmes fonctionnalités de base, mais l'un utilise Jekyll tandis que l'autre utilise Hugo.

Avec la rationalité typique d'un développeur, il était clair qu'il n'y avait qu'une seule option. J'ai décidé de créer le même thème dans les deux frameworks, et de vous offrir, cher lecteur, une comparaison côte à côte.

Cet article n'est pas un guide complet pour la création de thèmes, mais il est plutôt destiné à vous familiariser avec le processus de création d'un thème dans l'un ou l'autre générateur. Voici ce que nous allons couvrir :

* Comment les fichiers de thème sont organisés
* Où placer le contenu
* Comment fonctionne le templating
* Créer un menu de premier niveau avec l'objet `pages`
* Créer un menu avec des liens imbriqués à partir d'une liste de données
* Assembler le template
* Créer des styles
* Comment configurer et déployer sur GitHub Pages

Voici un wireframe approximatif du thème que je vais créer.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/wireframe.jpg)

Si vous prévoyez de construire en parallèle, il peut être utile de servir le thème localement au fur et à mesure que vous le construisez – et les deux générateurs offrent cette fonctionnalité. Pour Jekyll, exécutez `jekyll serve`, et pour Hugo, `hugo serve`.

Il y a deux éléments principaux : la zone de contenu principale et le menu de la barre latérale, tout aussi important. Pour les créer, vous aurez besoin de fichiers de template qui indiquent au générateur de site comment générer la page HTML. Pour organiser les fichiers de template de thème de manière sensée, vous devez d'abord connaître la structure de répertoire attendue par le générateur de site.

## Comment les fichiers de thème sont organisés

Jekyll supporte les thèmes basés sur des gems, que les utilisateurs peuvent installer comme n'importe quelle autre gem Ruby. Cette méthode cache les fichiers de thème dans la gem, donc pour les besoins de cette comparaison, nous n'utilisons pas de thèmes basés sur des gems.

Lorsque vous exécutez `jekyll new-theme <name>`, Jekyll va échafauder un nouveau thème pour vous. Voici à quoi ressemblent ces fichiers :

```sh
.
├── assets
├── Gemfile
├── _includes
├── _layouts
│   ├── default.html
│   ├── page.html
│   └── post.html
├── LICENSE.txt
├── README.md
├── _sass
└── <name>.gemspec

```

Les noms de répertoires sont appropriés et descriptifs. Le répertoire `_includes` est destiné aux petits morceaux de code que vous réutilisez à différents endroits, de la même manière que vous mettriez du beurre sur tout. (Juste moi ?)

Le répertoire `_layouts` contient des templates pour différents types de pages sur votre site. Le dossier `_sass` est destiné aux fichiers [Sass](https://sass-lang.com/documentation/syntax) utilisés pour construire la feuille de style de votre site.

Vous pouvez échafauder un nouveau thème Hugo en exécutant `hugo new theme <name>`. Il contient ces fichiers :

```sh
.
├── archetypes
│   └── default.md
├── layouts
│   ├── 404.html
│   ├── _default
│   │   ├── baseof.html
│   │   ├── list.html
│   │   └── single.html
│   ├── index.html
│   └── partials
│       ├── footer.html
│       ├── header.html
│       └── head.html
├── LICENSE
├── static
│   ├── css
│   └── js
└── theme.toml

```

Vous pouvez voir quelques similitudes. Les fichiers de template de page de Hugo sont rangés dans `layouts/`. Notez que le type de page `_default` a des fichiers pour un `list.html` et un `single.html`.

Contrairement à Jekyll, Hugo utilise ces noms de fichiers spécifiques pour distinguer entre les [pages de liste](https://gohugo.io/templates/lists/) (comme une page avec des liens vers tous vos articles de blog) et les [pages simples](https://gohugo.io/templates/single-page-templates/) (comme l'un de vos articles de blog). Le répertoire `layouts/partials/` contient les morceaux réutilisables, et les fichiers de feuille de style ont une place réservée dans `static/css/`.

Ces structures de répertoires ne sont pas gravées dans le marbre, car les deux générateurs de site permettent une certaine mesure de personnalisation. Par exemple, Jekyll vous permet de définir des [collections](https://jekyllrb.com/docs/collections/), et Hugo utilise des [bundles de pages](https://gohugo.io/content-management/page-bundles/). Ces fonctionnalités vous permettent d'organiser votre contenu de plusieurs manières, mais pour l'instant, regardons où placer quelques pages simples.

## Où placer le contenu

Pour créer un menu de site qui ressemble à ceci :

```md
Introduction
    Getting Started
    Configuration
    Deploying
Advanced Usage
    All Configuration Settings
    Customizing
    Help and Support

```

Vous aurez besoin de deux sections (« Introduction » et « Advanced Usage ») contenant leurs sous-sections respectives.

Jekyll n'est pas strict avec l'emplacement de son contenu. Il attend les pages à la racine de votre site et construira tout ce qui s'y trouve. Voici comment vous pourriez organiser ces pages dans la racine de votre site Jekyll :

```sh
.
├── 404.html
├── assets
├── Gemfile
├── _includes
├── index.markdown
├── intro
│   ├── config.md
│   ├── deploy.md
│   ├── index.md
│   └── quickstart.md
├── _layouts
│   ├── default.html
│   ├── page.html
│   └── post.html
├── LICENSE.txt
├── README.md
├── _sass
├── <name>.gemspec
└── usage
    ├── customizing.md
    ├── index.md
    ├── settings.md
    └── support.md


```

Vous pouvez changer l'emplacement de la source du site dans votre [configuration Jekyll](https://jekyllrb.com/docs/configuration/default/).

Dans Hugo, tout le contenu rendu est attendu dans le dossier `content/`. Cela empêche Hugo d'essayer de rendre les pages que vous ne voulez pas, comme `404.html`, en tant que contenu du site. Voici comment vous pourriez organiser votre répertoire `content/` dans Hugo :

```sh
.
├── _index.md
├── intro
│   ├── config.md
│   ├── deploy.md
│   ├── _index.md
│   └── quickstart.md
└── usage
    ├── customizing.md
    ├── _index.md
    ├── settings.md
    └── support.md

```

Pour Hugo, `_index.md` et `index.md` signifient des choses différentes. Il peut être utile de savoir quel type de [Page Bundle](https://gohugo.io/content-management/page-bundles/) vous voulez pour chaque section : Leaf, qui n'a pas d'enfants, ou Branch.

Maintenant que vous avez une idée de l'endroit où mettre les choses, regardons comment construire un template de page.

## Comment fonctionne le templating

Les templates de pages Jekyll sont construits avec le [langage de templating Liquid](https://jekyllrb.com/docs/liquid/). Il utilise des accolades pour sortir le contenu variable sur une page, comme le titre de la page : `{{ page.title }}`.

Les templates de Hugo utilisent également des accolades, mais ils sont construits avec [Go Templates](https://gohugo.io/templates/introduction/). La syntaxe est similaire, mais différente : `{{ .Title }}`.

Liquid et Go Templates peuvent tous deux gérer la logique. Liquid utilise la syntaxe des _tags_ pour désigner les opérations logiques :

```liquid
{% if user %}
  Hello {{ user.name }}!
{% endif %}

```

Et Go Templates place ses fonctions et arguments dans sa syntaxe d'accolades :

```go
{{ if .User }}
    Hello {{ .User }}!
{{ end }}

```

Les langages de templating vous permettent de construire un squelette HTML, puis de dire au générateur de site de mettre le contenu variable dans les zones que vous définissez. Comparons deux templates de page `default` possibles pour Jekyll et Hugo.

Le thème `default` échafaudé de Jekyll est nu, donc nous allons regarder leur thème de démarrage [Minima](https://github.com/jekyll/minima). Voici `_layouts/default.html` dans Jekyll (Liquid) :

```html
<!DOCTYPE html>
<html lang="{{ page.lang | default: site.lang | default: "en" }}">

  {%- include head.html -%}

  <body>

    {%- include header.html -%}

    <main class="page-content" aria-label="Content">
      <div class="wrapper">
        {{ content }}
      </div>
    </main>

    {%- include footer.html -%}

  </body>

</html>


```

Voici le thème échafaudé de Hugo `layouts/_default/baseof.html` (Go Templates) :

```html
<!DOCTYPE html>
<html>
    {{- partial "head.html" . -}}
    <body>
        {{- partial "header.html" . -}}
        <div id="content">
        {{- block "main" . }}{{- end }}
        </div>
        {{- partial "footer.html" . -}}
    </body>
</html>

```

Syntaxe différente, même idée. Les deux templates incluent des morceaux réutilisables pour `head.html`, `header.html`, et `footer.html`. Ces éléments apparaissent sur de nombreuses pages, il est donc logique de ne pas avoir à se répéter.

Les deux templates ont également un emplacement pour le contenu principal, bien que le template Jekyll utilise une variable (`{{ content }}`) tandis que Hugo utilise un bloc (`{{- block "main" . }}{{- end }}`). Les [blocs](https://gohugo.io/templates/base/#readout) sont simplement une autre façon pour Hugo de vous permettre de définir des morceaux réutilisables.

Maintenant que vous savez comment fonctionne le templating, vous pouvez construire le menu de la barre latérale pour le thème.

## Créer un menu de premier niveau avec l'objet `pages`

Vous pouvez créer un menu de premier niveau à partir de vos pages. Il ressemblera à ceci :

```md
Introduction
Advanced Usage

```

Commençons par Jekyll. Vous pouvez afficher des liens vers les pages du site dans votre template Liquid en itérant à travers l'objet `site.pages` que Jekyll fournit et en construisant une liste :

```html
<ul>
    {% for page in site.pages %}
    <li><a href="{{ page.url | absolute_url }}">{{ page.title }}</a></li>
    {% endfor %}
</ul>

```

Cela retourne toutes les pages du site, y compris celles que vous ne voulez peut-être pas, comme `404.html`. Vous pouvez filtrer les pages que vous voulez réellement avec quelques balises supplémentaires, comme inclure conditionnellement les pages si elles ont un paramètre `section: true` défini :

```html
<ul>
    {% for page in site.pages %}
    {%- if page.section -%}
    <li><a href="{{ page.url | absolute_url }}">{{ page.title }}</a></li>
    {%- endif -%}
    {% endfor %}
</ul>

```

Vous pouvez obtenir le même effet avec un peu moins de code dans Hugo. Parcourez l'objet `.Pages` de Hugo en utilisant l'action [`range`](https://golang.org/pkg/text/template/#hdr-Actions) de Go Template :

```html
<ul>
{{ range .Pages }}
    <li>
        <a href="{{.Permalink}}">{{.Title}}</a>
    </li>
{{ end }}
</ul>

```

Ce template utilise l'objet `.Pages` pour retourner toutes les pages de premier niveau dans `content/` de votre site Hugo. Comme Hugo utilise un dossier spécifique pour le contenu du site que vous voulez rendre, il n'est pas nécessaire de filtrer davantage pour construire un menu simple des pages du site.

## Créer un menu avec des liens imbriqués à partir d'une liste de données

Les deux générateurs de site peuvent utiliser une liste de données de liens définie séparément pour rendre un menu dans votre template. Cela est plus adapté pour créer des liens imbriqués, comme ceci :

```md
Introduction
    Getting Started
    Configuration
    Deploying
Advanced Usage
    All Configuration Settings
    Customizing
    Help and Support

```

Jekyll supporte les [fichiers de données](https://jekyllrb.com/docs/datafiles/) dans plusieurs formats, y compris YAML. Voici la définition du menu ci-dessus dans `_data/menu.yml` :

```yml
section:
  - page: Introduction
    url: /intro
    subsection:
      - page: Getting Started
        url: /intro/quickstart
      - page: Configuration
        url: /intro/config
      - page: Deploying
        url: /intro/deploy
  - page: Advanced Usage
    url: /usage
    subsection:
      - page: Customizing
        url: /usage/customizing
      - page: All Configuration Settings
        url: /usage/settings
      - page: Help and Support
        url: /usage/support

```

Voici comment rendre les données dans le template de la barre latérale :

```html
{% for a in site.data.menu.section %}
<a href="{{ a.url }}">{{ a.page }}</a>
<ul>
    {% for b in a.subsection %}
    <li><a href="{{ b.url }}">{{ b.page }}</a></li>
    {% endfor %}
</ul>
{% endfor %}

```

Cette méthode vous permet de construire un menu personnalisé, avec deux niveaux de nesting. Les niveaux de nesting sont limités par les boucles `for` dans le template. Pour une version récursive qui gère d'autres niveaux de nesting, voir [Navigation en arbre imbriqué avec récursion](https://jekyllrb.com/tutorials/navigation/#scenario-9-nested-tree-navigation-with-recursion).

Hugo fait quelque chose de similaire avec ses [templates de menu](https://gohugo.io/templates/menu-templates/#section-menu-for-lazy-bloggers). Vous pouvez définir des liens de menu dans votre [configuration de site Hugo](https://gohugo.io/getting-started/configuration/), et même ajouter des propriétés utiles que Hugo comprend, comme le poids. Voici une définition du menu ci-dessus dans `config.yaml` :

```yml
sectionPagesMenu: main

menu:  
  main:
    - identifier: intro
      name: Introduction
      url: /intro/
      weight: 1
    - name: Getting Started
      parent: intro
      url: /intro/quickstart/
      weight: 1
    - name: Configuration
      parent: intro
      url: /intro/config/
      weight: 2
    - name: Deploying
      parent: intro
      url: /intro/deploy/
      weight: 3
    - identifier: usage
      name: Advanced Usage
      url: /usage/
    - name: Customizing
      parent: usage
      url: /usage/customizing/
      weight: 2
    - name: All Configuration Settings
      parent: usage
      url: /usage/settings/
      weight: 1
    - name: Help and Support
      parent: usage
      url: /usage/support/
      weight: 3

```

Hugo utilise l'`identifier`, qui doit correspondre au nom de la section, ainsi que la variable `parent` pour gérer le nesting. Voici comment rendre le menu dans le template de la barre latérale :

```html
<ul>
    {{ range .Site.Menus.main }}
    {{ if .HasChildren }}
    <li>
        <a href="{{ .URL }}">{{ .Name }}</a>
    </li>
    <ul class="sub-menu">
        {{ range .Children }}
        <li>
            <a href="{{ .URL }}">{{ .Name }}</a>
        </li>
        {{ end }}
    </ul>
    {{ else }}
    <li>
        <a href="{{ .URL }}">{{ .Name }}</a>
    </li>
    {{ end }}
    {{ end }}
</ul>

```

La fonction `range` itère sur les données du menu, et la variable `.Children` de Hugo gère les pages imbriquées pour vous.

## Assembler le template

Avec votre menu dans votre morceau de barre latérale réutilisable (`_includes/sidebar.html` pour Jekyll et `partials/sidebar.html` pour Hugo), vous pouvez l'ajouter au template `default.html`.

Dans Jekyll :

```html
<!DOCTYPE html>
<html lang="{{ page.lang | default: site.lang | default: "en" }}">

{%- include head.html -%}

<body>
    {%- include sidebar.html -%}

    {%- include header.html -%}

    <div id="content" class="page-content" aria-label="Content">
        {{ content }}
    </div>

    {%- include footer.html -%}

</body>

</html>

```

Dans Hugo :

```html
<!DOCTYPE html>
<html>
{{- partial "head.html" . -}}

<body>
    {{- partial "sidebar.html" . -}}

    {{- partial "header.html" . -}}
    <div id="content" class="page-content" aria-label="Content">
        {{- block "main" . }}{{- end }}
    </div>
    {{- partial "footer.html" . -}}
</body>

</html>

```

Lorsque le site est généré, chaque page contiendra tout le code de votre `sidebar.html`.

## Créer une feuille de style

Les deux générateurs de site acceptent Sass pour créer des feuilles de style CSS. Jekyll [a le traitement Sass intégré](https://jekyllrb.com/docs/assets/), et Hugo utilise [Hugo Pipes](https://gohugo.io/hugo-pipes/scss-sass/). Les deux options ont quelques particularités.

### Sass et CSS dans Jekyll

Pour traiter un fichier Sass dans Jekyll, créez vos définitions de style dans le répertoire `_sass`. Par exemple, dans un fichier à `_sass/style-definitions.scss` :

```scss
$background-color: #eef !default;
$text-color: #111 !default;

body {
  background-color: $background-color;
  color: $text-color;
}

```

Jekyll ne générera pas directement ce fichier, car il ne traite que les fichiers avec front matter. Pour créer le chemin de fichier final pour la feuille de style de votre site, utilisez un placeholder avec un front matter vide là où vous voulez que le fichier `.css` apparaisse. Par exemple, `assets/css/style.scss`. Dans ce fichier, importez simplement vos styles :

```scss
---
---

@import "style-definitions";

```

Cette configuration plutôt hackish a un avantage : vous pouvez utiliser des balises de template Liquid et des variables dans votre fichier placeholder. C'est une bonne façon de permettre aux utilisateurs de définir des variables à partir du fichier `_config.yml` du site, par exemple.

La feuille de style CSS résultante dans votre site généré a le chemin `/assets/css/style.css`. Vous pouvez y faire référence dans le `head.html` de votre site en utilisant :

```html
<link rel="stylesheet" href="{{ "/assets/css/style.css" | relative_url }}" media="screen">

```

### Sass et Hugo Pipes dans Hugo

Hugo utilise [Hugo Pipes](https://gohugo.io/hugo-pipes/scss-sass/) pour traiter Sass en CSS. Vous pouvez y parvenir en utilisant la fonction de traitement d'actifs de Hugo, `resources.ToCSS`, qui attend une source dans le répertoire `assets/`. Elle prend le fichier SCSS comme argument.

Avec vos définitions de style dans un fichier Sass à `assets/sass/style.scss`, voici comment obtenir, traiter et lier votre Sass dans le `head.html` de votre thème :

```html
{{ $style := resources.Get "/sass/style.scss" | resources.ToCSS }}
<link rel="stylesheet" href="{{ $style.RelPermalink }}" media="screen">

```

Le traitement des actifs Hugo [nécessite Hugo étendu](https://gohugo.io/troubleshooting/faq/#i-get-tocss--this-feature-is-not-available-in-your-current-hugo-version), que vous n'avez peut-être pas par défaut. Vous pouvez obtenir Hugo étendu à partir de la [page des versions](https://github.com/gohugoio/hugo/releases).

## Configurer et déployer sur GitHub Pages

Avant que votre générateur de site puisse construire votre site, il a besoin d'un fichier de configuration pour définir certains paramètres nécessaires. Les fichiers de configuration se trouvent dans le répertoire racine du site. Parmi d'autres paramètres, vous pouvez déclarer le nom du thème à utiliser lors de la construction du site.

### Configurer Jekyll

Voici un fichier `_config.yml` minimal pour Jekyll :

```yml
title: Votre titre génial
description: >- # cela signifie ignorer les nouvelles lignes jusqu'à "baseurl:"
  Écrivez une description géniale pour votre nouveau site ici. Vous pouvez modifier cette
  ligne dans _config.yml. Elle apparaîtra dans le méta de l'en-tête de votre document (pour
  les résultats de recherche Google) et dans la description de votre site feed.xml.
baseurl: "" # le sous-chemin de votre site, par exemple /blog
url: "" # le nom d'hôte de base et le protocole pour votre site, par exemple http://example.com
theme: # pour les thèmes basés sur des gems
remote_theme: # pour les thèmes hébergés sur GitHub, lorsqu'ils sont utilisés avec GitHub Pages

```

Avec `remote_theme`, tout [thème Jekyll hébergé sur GitHub peut être utilisé](https://help.github.com/en/github/working-with-github-pages/adding-a-theme-to-your-github-pages-site-using-jekyll#adding-a-jekyll-theme-in-your-sites-_configyml-file) avec des sites hébergés sur GitHub Pages.

Jekyll a une [configuration par défaut](https://jekyllrb.com/docs/configuration/default/), donc tout paramètre ajouté à votre fichier de configuration remplacera les valeurs par défaut. Voici [des paramètres de configuration supplémentaires](https://jekyllrb.com/docs/configuration/options/).

### Configurer Hugo

Voici un exemple minimal du fichier `config.yml` de Hugo :

```yml
baseURL: https://example.com/ # Le domaine complet où votre site vivra
languageCode: en-us
title: Site de documentation Hugo
theme: # nom du thème

```

Hugo ne fait aucune supposition, donc si un paramètre nécessaire est manquant, vous verrez un avertissement lors de la construction ou du service de votre site. Voici [tous les paramètres de configuration pour Hugo](https://gohugo.io/getting-started/configuration/#all-configuration-settings).

### Déployer sur GitHub Pages

Les deux générateurs construisent votre site avec une commande.

Pour Jekyll, utilisez `jekyll build`. Voir [d'autres options de construction ici](https://jekyllrb.com/docs/configuration/options/#build-command-options).

Pour Hugo, utilisez `hugo`. Vous pouvez exécuter `hugo help` ou voir [d'autres options de construction ici](https://gohugo.io/getting-started/usage/#test-installation).

Vous devrez choisir la source de votre site GitHub Pages. Une fois cela fait, votre site sera mis à jour à chaque fois que vous pousserez une nouvelle construction. Bien sûr, vous pouvez également automatiser la construction de votre site GitHub Pages en utilisant GitHub Actions. En voici un pour [construire et déployer avec Hugo](https://github.com/victoriadrake/hugo-latest-cd), et un autre pour [construire et déployer Jekyll](https://github.com/victoriadrake/jekyll-cd).

## C'est l'heure du spectacle !

Toutes les différences substantielles entre ces deux générateurs sont sous le capot. Quoi qu'il en soit, jetons un coup d'œil aux thèmes finis, dans deux variations de couleur.

Voici Hugo :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/ogd_hugo.png)

Et voici Jekyll :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/ogd_jekyll.png)

## Attendez, qui a gagné ?

?

Hugo et Jekyll ont tous deux leurs particularités et leurs commodités.

Du point de vue de ce développeur, Jekyll est un choix viable pour des sites simples sans besoins organisationnels compliqués. Si vous cherchez à rendre quelques posts sur une seule page dans un [thème disponible](https://jekyllrb.com/docs/themes/) et à héberger avec GitHub Pages, Jekyll vous fera démarrer assez rapidement.

Personnellement, j'utilise Hugo. J'aime les capacités organisationnelles de ses Page Bundles, et il est soutenu par une équipe dédiée et consciencieuse qui semble vraiment s'efforcer de faciliter la vie de leurs utilisateurs. Cela est évident dans les nombreuses fonctions de Hugo, et les astuces pratiques comme le [traitement d'images](https://gohugo.io/content-management/image-processing/) et les [shortcodes](https://gohugo.io/content-management/shortcodes/). Ils semblent publier de nouvelles corrections et versions à peu près aussi souvent que je fais une nouvelle tasse de café - ce qui, selon votre cas d'utilisation, peut être fantastique ou ennuyeux.

Si vous ne pouvez toujours pas décider, ne vous inquiétez pas. Le [thème de documentation OpenGitDocs](https://github.com/opengitdocs) que j'ai créé est disponible pour Hugo et Jekyll. Commencez avec l'un, basculez plus tard si vous le souhaitez. C'est l'avantage d'avoir des options.