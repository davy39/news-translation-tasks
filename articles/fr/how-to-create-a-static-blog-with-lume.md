---
title: Guide Lume SSG – Comment créer un blog statique avec Lume
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2022-11-18T17:06:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-static-blog-with-lume
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Create-a-Static-Blog-with-Lume.png
tags:
- name: Deno
  slug: deno
- name: Static Site Generators
  slug: static-site-generators
seo_title: Guide Lume SSG – Comment créer un blog statique avec Lume
seo_desc: "Lume is a new static site generator based on Deno. Deno is a JavaScript-based\
  \ run-time environment that supports TypeScript. \nLume is not built around any\
  \ specific language. It supports Markdown, Nunjucks, TypeScript, and JavaScript\
  \ by default. Lume ..."
---

Lume est un nouveau générateur de site statique basé sur Deno. Deno est un environnement d'exécution basé sur JavaScript qui supporte TypeScript. 

Lume n'est pas construit autour d'un langage spécifique. Il supporte Markdown, Nunjucks, TypeScript et JavaScript par défaut. Lume supporte également les plugins. Certains plugins sont préinstallés par défaut. C'est pourquoi Lume lui-même est agnostique en matière de langage de template.

Avant d'en apprendre davantage sur Lume, discutons de Deno et considérons quelques fonctionnalités importantes de Deno.

## Qu'est-ce que Deno ?

Deno est une alternative à Node.js construite par [Ryan Dahl](https://en.wikipedia.org/wiki/Ryan_Dahl) (qui a également développé Node). Deno est basé sur le langage de programmation Rust, et le deuxième composant principal de Deno est le moteur JavaScript V8 pour WebAssembly.

Deno possède de nombreuses fonctionnalités intéressantes – il est rapide, sécurisé par défaut, compatible avec web assembly et supporte TypeScript, possède des outils de développement intégrés, et plus encore. Deno supporte également les API Node.js, vous pouvez donc utiliser tous les packages npm avec Deno.

Dans Deno, vous n'avez pas besoin de créer un fichier de configuration pour exécuter un simple programme. Vous déployez simplement votre site web instantanément avec un réseau de deuxième niveau. Mais ma fonctionnalité préférée est le nouveau dossier `node_modules` dans l'espace de travail. Deno met en cache tous les packages localement et les utilise, ce qui est très rapide par rapport à Node.

Vous pouvez consulter le [site web de démonstration du blog ici,](https://minimalist-blog.deno.dev/) et tout le [code est disponible sur GitHub ici](https://github.com/officialrajdeepsingh/Minimalist-blog).

Maintenant, plongeons dans le tutoriel.

## Table des matières

1. [Lume + Markdown](#heading-lume-markdown)
2. [Pourquoi Lume est-il spécial ?](#heading-pourquoi-lume-est-il-special)
3. [Comment Lume se compare-t-il aux autres générateurs de sites statiques ?](#heading-comment-lume-se-compare-t-il-aux-autres-generateurs-de-sites-statiques)
4. [Comment démarrer un nouveau projet avec Lume](#heading-comment-demarrer-un-nouveau-projet-avec-lume)
5. [Structure des dossiers de Lume](#heading-structure-des-dossiers-de-lume)
6. [Dossiers supplémentaires](#additional-folders)
7. [Comment créer des données globales](#heading-comment-creer-des-donnees-globales)
8. [Comment créer une page dynamique](#heading-comment-creer-une-page-dynamique)
9. [Comment créer une page d'accueil et de pagination](#heading-comment-creer-une-page-daccueil-et-de-pagination)
10. [Comment construire une page d'articles](#heading-comment-construire-une-page-darticles)
11. [Comment générer une page de catégorie](#heading-comment-generer-une-page-de-categorie)
12. [Comment générer une page de tag](#heading-comment-generer-une-page-de-tag)
13. [Comment activer la fonctionnalité de recherche](#heading-comment-activer-la-fonctionnalite-de-recherche)
14. [Comment installer page find](#heading-comment-installer-page-find)
15. [SEO de Lume](#heading-lume-seo)
16. [Plan du site de Lume](#heading-lume-sitemap)
17. [Plugins de Lume](#heading-lume-plugins)
18. [Comment activer les commentaires](#heading-comment-activer-les-commentaires)
19. [Comment utiliser Netlify CMS avec Lume](#heading-comment-utiliser-netlify-cms-avec-lume)
20. [Comment déployer votre blog avec Deno Deploy](#heading-comment-deployer-votre-blog-avec-deno-deploy)
21. [Pages GitHub](#github-pages)
22. [Conclusion](#heading-conclusion)

## Lume + Markdown

Lume est un nouveau générateur de site statique basé sur Deno créé et maintenu par [Óscar Otero](https://github.com/oscarotero). Lume utilise **markdown-it** comme markdown par défaut. Vous pouvez utiliser le [plugin remark](https://lume.land/plugins/remark/) pour changer le markdown par défaut.  

Markdown est un langage qui aide à écrire des documents, des fichiers readme et des blogs sur internet. [John Gruber](https://en.wikipedia.org/wiki/John_Gruber) a créé markdown en 2004.

**Markdown-it** est similaire au [GitHub-flavored Markdown](https://github.github.com/gfm/) (GFM) markdown. GFM et [markdown-it](https://github.com/markdown-it/markdown-it) suivent tous deux les spécifications exactes de [markdown](https://commonmark.org/). 

Si vous avez travaillé avec GitHub et écrit des fichiers README, cela signifie que vous êtes probablement familier avec le markdown GFM. Si vous n'aimez pas le markdown par défaut (markdown-it), vous pouvez changer le markdown avec le plugin remark.

Il existe de nombreux générateurs de sites statiques. Alors pourquoi Lume est-il spécial ? Que fournit-il par rapport aux autres générateurs de sites statiques ? Découvrons-le.

## Pourquoi Lume est-il spécial ?

Comme vous le savez, Lume est construit sur Deno, et Deno est une alternative à Node.js – c'est pourquoi Lume fournit de nombreuses fonctionnalités dès le départ. 

Lume fonctionne de manière similaire à un fichier readme GitHub. Si vous êtes familier avec l'écriture de l'un de ceux-ci (et l'utilisation de markdown), vous n'avez pas besoin d'apprendre autre chose pour écrire des articles et de la documentation avec Lume.

Voici quelques avantages de Lume :

1. Lume supporte plusieurs moteurs de template comme Markdown, [Nunjucks](https://lume.land/plugins/nunjucks/), [Eta](https://lume.land/plugins/eta/), [JSX](https://lume.land/plugins/jsx/), [Liquid](https://lume.land/plugins/liquid/), ou [Pug](https://lume.land/plugins/pug/).
2. Il supporte plusieurs auteurs
3. Il a la coloration syntaxique du code
4. Il y a un excellent support SEO
5. Lume supporte plusieurs langues
6. Il a le support de Windi CSS
7. Il y a la pagination et le support des composants
8. Il supporte la minification de JavaScript, HTML, CSS et SASS
9. Il a le support des relations
10. Il y a la fonctionnalité de recherche intégrée
11. Il supporte Netlify CMS
12. Il supporte les images et les SVGs
13. Il y a le support du plugin Remark.js
14. Vous pouvez déployer avec Netlify, Vercel, GitLab Pages et la page GitHub.

## Comment Lume se compare-t-il aux autres générateurs de sites statiques ?

Lume est un nouveau générateur de site statique par rapport aux autres, mais il vient avec de nombreuses options de configuration, et vous pouvez tout faire avec. Vous n'avez même pas besoin d'utiliser des plugins tiers. 

Avec les processeurs et préprocesseurs de Lume, vous pouvez facilement manipuler le code HTML avec l'API DOM JavaScript. Les autres générateurs de sites statiques supportent quelques moteurs de template, mais Lume supporte de nombreux moteurs de template comme JavaScript, JSX, Nunjucks, Eta, JSX, Liquid et Pug.

Notez que Lume peut sembler difficile à prendre en main pour les débutants. Mais si vous suivez mon article, assurez-vous simplement d'[ouvrir le code](https://github.com/officialrajdeepsingh/Minimalist-blog) ce qui rendra les choses beaucoup plus claires pour vous.

## Comment démarrer un nouveau projet avec Lume

Vous pouvez configurer un nouveau projet avec l'interface de ligne de commande de Lume avec cette commande :

```bash
deno run -Ar https://deno.land/x/lume/init.ts
```

![Démo d'installation de Lume](https://www.freecodecamp.org/news/content/images/2022/11/lume-installation-low.gif)
_Démo d'installation de Lume_

#### Suivez ces étapes :

1. Tout d'abord, créez un dossier de projet vide `mkdir lume-deno`.
2. Ensuite, exécutez la commande lume `init.ts`.
3. Sélectionnez un plugin disponible dans la liste.

Et vous devriez être opérationnel.

## Structure des dossiers de Lume

Après la fin de l'installation, nous avons vu trois fichiers :

1. Le fichier `_config` est utilisé pour configurer Lume.
2. `deno.json` est un script ou une tâche définie pour Deno.
3. `import_map.json` est pour vous aider à importer un package Deno depuis internet.

![structure des dossiers par défaut de lume](https://www.freecodecamp.org/news/content/images/2022/11/folder-struture-1.png)
_structure des dossiers par défaut de lume_

### Comment exécuter le serveur Lume

Pour exécuter un serveur de développement local, vous utiliserez la commande `deno task lume --serve`. Pour construire un site web, exécutez la commande `deno task build`.

Si vous rencontrez une erreur 404 - non trouvé, vous pouvez créer un fichier `index.njk` dans le dossier racine.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/lume404-1.png)

Dans le fichier `index.njk`, collez le code suivant.

```nunjucks
---
title: "bonjour"
---
bonjour le monde
```

Et vous verrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/hello-world-lume-2.png)
_Lume bonjour le monde_

### Dossiers supplémentaires :

1. Le dossier `posts` n'est pas un dossier obligatoire. Il contient tous les fichiers markdown de vos articles.
2. Le dossier `pages` n'est pas un dossier obligatoire. Il contient tous les fichiers markdown de vos pages.
3. Le dossier `author` n'est pas un dossier obligatoire. Il contient tous les fichiers markdown de vos auteurs.
4. Le dossier `_components` est un dossier **obligatoire**. Il contient tous vos composants.
5. Le dossier `_includes` est un dossier **obligatoire**. Il contient vos mises en page et templates pour votre site.
6. Le dossier `images` n'est pas un dossier obligatoire. Il contient toutes vos images.

Les dossiers posts, pages, auteurs et images sont optionnels. Vous pouvez renommer ces dossiers selon vos souhaits. Les dossiers `_components` et `_includes` sont obligatoires et vous ne pouvez pas les renommer.

La différence entre les composants, la mise en page et le template est la suivante :

* Les composants sont du code réutilisable
* La mise en page et le template ne sont pas réutilisables comme les composants.

## Comment créer des données globales

Dans Lume, vous pouvez créer une variable de données, qui a accès à l'ensemble du site web par tous les moteurs de template.

```javascript
// Définir une variable
site.data("post_per_page", 10);

// Définir une fonction
site.data("randomNumber", function () {
  return Math.random();
});
```

#### Comment créer des fichiers markdown pour les articles, les pages et les auteurs

Vous créez des dossiers pour les articles, les pages et les auteurs dans le dossier racine. Ensuite, à l'intérieur de chaque dossier, vous écrivez des fichiers markdown.

Vous pouvez accéder à tous les articles, pages et auteurs par nom de fichier dans le navigateur :

1. `localhost:3000/posts/your-title.html`
2. `localhost:3000/pages/your-pages.html`
3. `localhost:3000/author/your-author.html`

Supposons que vous avez besoin d'un article de démonstration, de pages et d'un auteur markdown pour un projet ou un template. Alors, vous pouvez utiliser [demo-markdown posts](https://github.com/officialrajdeepsingh/Demo-markdown-posts) pour votre projet. Il est gratuit et open source, et vous pouvez créer votre propre template.

### Comment créer une page dynamique

Dans Lume, les extensions `.tmpl.js` et `.tmpl.ts` utilisent JS et TS comme [moteurs de template](https://lume.land/plugins/modules/). Vous pouvez les utiliser avec des pages régulières ou des pages dynamiques pour créer des catégories, des tags, une pagination, etc. pour votre site web.

### Comment créer une page d'accueil et de pagination

La page d'accueil est basée sur la pagination, et la pagination est basée sur les articles. Lume génère dynamiquement la pagination. 

Dans Lume, j'ai choisi nunjucks et JavaScript pour créer mon site web de démonstration. Nunjucks est le moteur de template par défaut. Vous pouvez facilement changer le moteur de template Nunjucks par défaut avec un autre moteur de template avec un code copier-coller.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Home-page-1.png)
_page d'accueil_

Lume fournit une fonction de template JavaScript qui aide à créer des pages web dynamiques. Si vous créez une page d'accueil pour le site, vous devez créer un fichier `index.tmpl.js` dans votre dossier racine ou src. Lume supporte également un dossier src pour organiser votre projet. Dans mon projet de démonstration, je n'utilise pas le dossier `src`.

Le `*.tmpl.js` est une extension d'un [template JavaScript](https://lume.land/plugins/modules/#creating-pages) qui aide à créer des pages dynamiques pour les sites web. Il est préinstallé dans Lume avec le [plugin modules](https://lume.land/plugins/modules/).

Par exemple, le code suivant crée une pagination pour votre site web. Mais la mise en page provient du dossier `_includes`.

```javascript
// index.tmpl.js

// titre pour le SEO
export const title = "Blog minimaliste"
// description pour le SEO
export const description = "Le thème de blog minimaliste est léger et fonctionne avec lume."

export default function* ({ search, paginate }) {

//  Obtenir tous les articles de type article.
  const posts = search.pages("type=article", "date=desc");

  // Configuration pour la pagination
  const options = {
    // La page 1 est la page d'accueil, définir "/" comme url
    url: (n) => n === 1 ? "/" : `/page/${n}/`,
    // par page articles
    size: 7,
  };

  // Générer les pages, mais l'index a besoin d'une mise en page différente
  for (const page of paginate(posts, options)) {

    //  si page d'accueil, utiliser une mise en page différente "/"
    if (page.pagination.page === 1) {
      page.menu = {visible: true, order: 1, title:"Accueil" }
      page.title = "Page d'accueil"

      //  provient du dossier _includes

      page.layout = "layouts/home.njk";
    } else {
      // Rendre une mise en page différente si ce n'est pas la page d'accueil "/page/2","/page/3",etc
      page.title = "Page de pagination"

      page.layout = "layouts/home.njk";
    }
    
    yield page;
  }

}
```

Lume dispose d'un [plugin de recherche](https://lume.land/plugins/search/) qui vous aide à rechercher des pages. Dans mon blog de démonstration, je recherche toutes les pages en fonction du type. 

Dans mon dossier de tous les articles, tous les articles sont définis dans `type=article`, l'auteur est décrit dans `type=author`, et les pages sont définies dans `type=page`. Le plugin de recherche est préinstallé avec Lume.

Dans le fichier `index.tmpl.js`, vous pouvez obtenir toutes les pages qui ont le type "article" (`type=article`) en utilisant le code suivant : `const posts = search.pages("type=article", "date=desc");`. La fonction `search.pages("type=article", "date=desc")` ne retourne que celles qui ont `type=article`.

Le fichier de mise en page `layouts/base.njk` contient une base HTML et inclut un en-tête et un pied de page pour le site web.

```nuckjunks
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <meta name="description" content="{{ description or site.description }}">
   </head>
  <body>

    {% include "layouts/header.njk" %}

    <main class="{{ bodyClass }}">
      {{ content | safe }}
    </main>

    {% include "layouts/footer.njk" %}

  </body>
</html>
```

À l'intérieur de `{{ content | safe }}`, Lume rend d'autres HTML, comme des cartes, des articles, des templates d'accueil, des pages de tags et de catégories, etc.

```javascript
// reste du code ...
  for (const page of paginate(posts, options)) {
  }
// reste du code ...
```

J'ai utilisé la boucle for dans le fichier `index.tmp.js` qui aide à obtenir tous les articles et à les envoyer au fichier `layouts/home.njk` et au fichier `layouts/home.njk`. Vous obtenez tous les articles à partir du résultat, puis vous les passez au template `card.njk`.

```nunjucks
---
layout: layouts/base.njk
---

{% for post in results %}
    {% include "templates/card.njk" %}
{% else %}
    <h2> Les articles sont vides </h2>
{% endfor %}

{% include "templates/pagnation.njk" %}
```

Le fichier `templates/card.njk` s'exécute pour tous les blogs et génère du HTML pour chaque blog. Votre carte ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/card.njk-1.png)
_card.njk_

Dans le template `card.js`, vous pouvez y accéder en utilisant les accolades `{{}}`. Obtenez le titre en utilisant `{{post.data.title}}` et `{{post.data.description}}`.

Dans mon blog de démonstration, je n'obtiens que la première catégorie à afficher à l'intérieur de la carte. J'utilise donc un filtre défini dans `_config.ts` et je l'utilise avec les symboles `|`. À l'intérieur de `card.njk`, nous obtenons un index zéro ou une première valeur dans les catégories avec le code suivant : `{{ post.data.category | category }}`.

Pour obtenir l'auteur sur `card.njk`, je définis la [relation](https://lume.land/plugins/relations/) entre l'article et le type d'auteur, que vous pouvez apprendre à partir de la documentation.

```nuckjunks
<div class="container px-6 py-10 mx-auto">

    <div class="mt-8 lg:-mx-6 lg:flex lg:items-center">

        <img class="object-cover border-none w-full lg:mx-6 lg:w-1/2 rounded-xl h-72 lg:h-96" src="{{ post.data.image }}" alt="{{ post.data.title }}">

        <div class="mt-6 lg:w-1/2 lg:mt-0 lg:mx-6 ">

            <a class="text-sm text-blue-500 uppercase" href="/category/{{ post.data.category | category }}" >
                {{ post.data.category | category }}
            </a>

            <a href="{{ post.data.url }}" class="block mt-4 text-2xl font-semibold text-gray-800 hover:text-gray-500 dark:text-white md:text-3xl">{{ post.data.title }}</a>

            <p class="mt-3 text-sm text-gray-500 dark:text-gray-300 md:text-sm">
                {{ post.data.description }}
            </p>

            <a href="{{  post.data.url }}" class="inline-block p-2 bg-blue-700 mt-4 text-white hover:bg-blue-500">Lire la suite</a>


            <div class="flex items-center mt-6">

                {% if post.data.author.length <= 2 %}

                    {% for author in post.data.author %}

                        <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ author.image}}" alt="{{ author.author_name}}">

                        <div class="mx-4">
                            <a href="{{author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
                                {{ author.author_name}}</a>
                            <p class="text-sm text-gray-500 dark:text-gray-400">
                                {{author.job}}
                            </p>
                        </div>
                    {% endfor %}
                {% else %}

                    <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ post.data.author.image}}" alt="{{ post.data.author.name}}">

                    <div class="mx-4">
                        <a href="{{ post.data.author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
                            {{ post.data.author.author_name}}</a>
                        <p class="text-sm text-gray-500 dark:text-gray-400">
                            {{post.data.author.job}}
                        </p>
                    </div>
                {% endif %}

            </div>
        </div>
    </div>
</div>
```

Le `{{ title }}` et `{{description}}` montrent tous deux le titre et la description du fichier markdown. Pour afficher la catégorie, j'ai utilisé un filtre pour afficher une seule catégorie sur la page de l'article et définir le filtre dans le fichier `_config.ts`. J'affiche également un ou plusieurs auteurs avec une boucle For. Chaque carte a sa propre propriété `post.data.url`, après que l'utilisateur clique sur le bouton lire la suite, l'utilisateur est redirigé vers la page de lecture de l'article respectif. Pour afficher l'image, j'ai utilisé la propriété `{{ post.data.image }}`. J'affiche également un ou plusieurs auteurs avec une boucle For dans le fichier `card.njk`.

## Comment construire une page d'articles

Je sais que la page contenant le contenu de l'article est l'une des plus importantes pour un blog. C'est là que les lecteurs devraient passer la plupart de leur temps plutôt que sur la page d'accueil du site web.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/random-blog-title-lume-1.png)

```markdown
---
category:
  - Blog
date: 2022-03-20T13:09:24Z
description: Dolor excepteur ad ad fugiat Lorem consectetur velit excepteur duis qui.
image: /images/dice.jpg
tags:
  - npm
  - npm cli
  - npm install command
title: Titre aléatoire de blog pour markdown.
draft: false
author_id: 1
type: article
layout: templates/article.njk
---

Laboris consequat elit ad excepteur. Ipsum duis amet dolore voluptate dolore consequat ullamco incididunt ullamco. Dolore laborum cupidatat dolor ipsum reprehenderit excepteur cupidatat dolore.

## Premier
Cupidatat non amet irure esse quis aute qui enim. Est qui ullamco proident consequat aute reprehenderit eiusmod nisi. Laboris ullamco fugiat sint occaecat.

## Second 
Irure fugiat officia non esse esse irure eu sint commodo quis amet. Dolor culpa non amet elit adipisicing exercitation ex anim velit ipsum.

## conclusion
Culpa irure eiusmod labore ut proident sit enim laborum nulla voluptate eu. Id tempor velit cillum pariatur est laboris ipsum ad. Sint nostrud nostrud laboris Lorem consequat tempor voluptate dolore velit. Commodo elit nulla commodo pariatur. Deserunt ipsum fugiat id ipsum pariatur cupidatat magna ex. Fugiat aliquip nisi laboris aliquip velit velit id quis eu reprehenderit excepteur fugiat.

```

J'ai créé un article dans le dossier posts sous `type=article`. Le `author_id` définit la relation entre l'auteur et l'article.

J'ai utilisé `templates/article.njk` comme mise en page pour ma page d'articles. Vous pouvez concevoir la vôtre selon vos besoins. Vous pouvez concevoir le titre de l'article, la description, la carte de l'auteur et les tags également. 

```nuckjunks
---
layout: layouts/base.njk
---
<article class="container mx-auto p-2">
  <div class="flex flex-col">

    <h1 class="text-2xl text-black mt-3">{{ title }}</h1>
    <p class="text-xl mt-1 text-gray-600">{{ description }}</p>

    {% if author %}
      <div class="flex flex-row mt-4">
        
        
        {% if author.length <= 2 %}

          {% for author in author %}

            <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ author.image}}" alt="{{ author.author_name}}">

            <div class="mx-4">
              <a href="{{author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
                {{ author.author_name}}</a>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                {{author.job}}
              </p>
            </div>
          {% endfor %}

        {% else %}
        
          <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ author.image}}" alt="{{ author.name}}">

          <div class="mx-4">
            <a href="{{ author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
              {{ author.author_name}}</a>
            <p class="text-sm text-gray-500 dark:text-gray-400">
              {{ author.job}}
            </p>
          </div>
        {% endif %}

      </div>

    {% endif %}

      <nav class="flex flex-row my-5">
        {% for tag in tags %}
          <a href="/tag/{{ tag.trim().toLowerCase().split(' ').join("-") }}/" class=" bg-blue-500 text-black p-2  mx-1">{{ tag }}</a>
        {% endfor %}
      </nav>

    <time class="mt-2" datetime="{{ date | date('DATETIME') }}">
      {{ date | date('HUMAN_DATE') }}
    </time>


  </div>

  <div class="mt-4">
    {{ content | safe }}
  </div>
</article>

{%- set previousPost = search.previousPage(url, "type=article") %}

{% if previousPost %}
  <ul class="flex flex-row w-full mt-10 justify-between p-4">
    {%- if previousPost %}
      <li class="w-6/12 text-left">
       2190 Précédent : <a href="{{ previousPost.data.url }}" rel="prev">{{ previousPost.data.title }}</a>
      </li>
    {% endif %}

    {%- set nextPost = search.nextPage(url, "type=article") %}
    {%- if nextPost %}
      <li class="w-6/12 text-right">
        <strong>Suivant : <a href="{{ nextPost.data.url }}" rel="next">{{ nextPost.data.title }}</a>  2192</strong>
      </li>
    {% endif %}
  </ul>
{% endif %}

<div class="container p-2 mx-auto mt-6"> 

{# ==== #}
{#  Ajout du script de commentaire Utteranc #}
{# ==== #}

<h1 class="text-center text-2xl my-3"> Commentaire </h1> 

<script src="https://utteranc.es/client.js"
        repo="officialrajdeepsingh/Minimalist-blog"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
</div>
```

Le fichier `layouts/base.njk` est le fichier de base pour notre blog (que j'ai déjà expliqué). Le `{{ title }}` et `{{description}}` montrent tous deux le titre et la description du fichier markdown. 

Pour afficher les tags sur la page de l'article, j'ai utilisé une boucle for. J'ai également affiché un ou plusieurs auteurs avec la boucle for. 

Pour convertir la date en un format lisible par l'homme, j'ai utilisé le plugin de date de Lume et l'ai enveloppé avec un filtre de date qui ressemble à ceci : `{{ date | date('HUMAN_DATE') }}`. Pour afficher tous les paragraphes markdown, j'ai utilisé `{{ content | safe }}`. 

Pour la pagination, j'ai utilisé le plugin de pagination de Lume, et avec la fonction `search.previousPage(url, "type=article")`, j'ai affiché les articles suivants et précédents sur la page de l'article. Pour les commentaires, j'ai utilisé [utteranc.es](#heading-comment-activer-les-commentaires).

## Comment générer une page de catégorie

Dans Lume, vous créez une catégorie dynamique basée sur le type d'article. Lume fournit également une fonctionnalité intégrée appelée moteur de template JavaScript qui vous aide à créer une page dynamique. Cela est similaire à la création de la fonctionnalité de pagination.

Dans Lume, il y a un fichier spécial appelé `.tmpl.js` qui vous aide à créer une catégorie dynamique.

```nunjucks
export const layout = "layouts/category.njk";

export default function* (props) {


  const { search }= props

  for (const category of search.values("category") ) {

    yield {
      url: `/category/${category}/`,
      title: `Catégorie ${category}`,
      type:"category",
      category,
    };
    
  }

}

```

Dans lume `search.values()` a une fonction qui vous aide à trouver une catégorie en utilisant les méta-tags markdown et envoie les données dans le fichier `layout/category.njk`. Il générera toutes les catégories avec les URL suivantes comme `/category/android/`, `/category/android-phone/`, `/category/human/` et ainsi de suite.

## Comment générer une page de tag

La génération d'une page de tags dynamique est similaire à une catégorie. Lume fournit une fonction spéciale `search.tags()` pour générer des tags :

```nunjucks
export const layout = "layouts/tag.njk";

export default function* ({ search }) {

  for (const tag of search.tags()) {
    yield {
      url: `/tag/${tag}/`,
      title: `Taggé ${tag}`,
      type: "tag",
      tag,
    };
  }
}
```

Le code suivant génère tous les tags avec les URL suivantes comme `/tag/android/`, `/tag/android-phone/`, `/tag/human/` et ainsi de suite.

## Comment activer la fonctionnalité de recherche

Lume dispose de nombreux plugins intégrés qui offrent une excellente expérience de développement. Vous pouvez résoudre de nombreux problèmes avec les plugins Lume, et ils vous permettent d'ajouter et de supprimer des fonctionnalités facilement.

Lume fournit une fonctionnalité de recherche intégrée pour le site. Vous l'activez avec le plugin de recherche de page lume.

![Ajouter une barre de recherche dans lume](https://www.freecodecamp.org/news/content/images/2022/11/lume-serachbar-1.png)
_Ajouter une barre de recherche dans lume_

### Comment installer Page Find

Le plugin de recherche de page Lume vous fournit une barre de recherche. Copiez simplement le code suivant et collez-le dans le fichier `_config.ts`, puis redémarrez votre serveur.

```javascript
import pagefind from "lume/plugins/pagefind.ts";
```

#### Comment configurer le plugin page find

Vous configurez le plugin dans le fichier `_config.ts`. Vous pouvez également changer la configuration par défaut.

```
// reste du code ...
import lume from "lume/mod.ts";
import pagefind from "lume/plugins/pagefind.ts";

const site = lume();

// configurer le plugin pagefind avec la configuration par défaut
site.use(pagefind());

 // ou 

// changer la configuration par défaut dans le plugin pagefind
site.use(pagefind({
  ui: {
    containerId: "search",
    showImages: false,
    showEmptyFilters: true,
    resetStyles: true,
  },
}));

export default site;
```

## SEO de Lume

Lume dispose d'un plugin pour aider au SEO appelé metas. Avec le plugin, vous pouvez facilement ajouter diverses configurations conviviales pour le SEO.

### Comment installer metas

Vous installez tous les plugins dans le fichier `config.ts`. Copiez le code suivant et collez-le dans le fichier `config.ts`, puis redémarrez le serveur.

```javascript
import metas from "lume/plugins/metas.ts";
```

#### Comment configurer metas

Vous pouvez configurer metas de diverses manières dans le fichier `_config.ts`. Voir les commentaires ci-dessous :

```
import lume from "lume/mod.ts";

// installer le plugin metas pour le SEO
import metas from "lume/plugins/metas.ts";

const site = lume();

// configurer le plugin metas avec la configuration par défaut
site.use(metas());

ou

// ajouter une configuration personnalisée 
site.use(metas({
  defaultPageData: {
    title: "title", // Utiliser la valeur `title` comme solution de repli.
  },
}));


export default site;
```

### Comment utiliser le plugin SEO Metas dans Lume

Pour utiliser le plugin SEO metas, vous devrez créer un fichier `_data.yml` à la racine du dossier du projet et y coller le code suivant :

```
metas:
  site: Blog minimaliste
  twitter: "@Official_R_deep"
  icon: /images/icon.png
  lang: en
  generator: true

mergedKeys:
  metas: object
```

Le code suivant vous aide à créer toutes les diverses balises SEO pour votre site web, et vous pouvez facilement l'étendre avec le [plugin metas](https://lume.land/plugins/metas/) dans Lume.

### Plan du site de Lume

Lume dispose d'un plugin appelé [sitemap](https://lume.land/plugins/sitemap/). Ce plugin vous aide à créer des plans de site pour votre blog. Avec Lume 13, vous n'avez pas besoin de créer un plan de site manuellement. 

#### Comment installer le plugin sitemap

Vous installez tous les plugins dans le fichier `config.ts`. Copiez le code suivant et collez-le dans le fichier `config.ts`, puis redémarrez le serveur.

```javascript
import sitemap from "lume/plugins/sitemap.ts";

```

#### Comment configurer le plugin sitemap

Vous pouvez configurer le plugin sitemap de diverses manières dans le fichier `_config.ts`. Voir les commentaires ci-dessous :

```javascript
import lume from "lume/mod.ts";
import sitemap from "lume/plugins/sitemap.ts";

const site = lume();

site.use(sitemap());

// ou

// ajouter une configuration personnalisée 
site.use(sitemap({
  filename: "my-sitemap.xml", // pour changer le nom du fichier sitemap
  query: "indexable=true", // Sélectionner uniquement les pages avec l'attribut indexable comme vrai
  sort: "date=desc", // Pour trier par date dans l'ordre ascendant
}));

export default site;
```

### Comment utiliser le plugin sitemap dans Lume

Vous n'avez pas besoin de fichier spécial pour utiliser le plugin de plan de site. Il vous suffit d'ajouter le plugin après avoir appelé le plugin dans `config.ts` et il commencera à fonctionner sur votre site. Cela crée le fichier `sitemap.xml` et vous pouvez changer le nom du fichier avec une configuration personnalisée dans le fichier `_config.ts`.

### Comment accéder au plan du site sur le site web

Vous pouvez accéder au plan du site avec le nom du fichier, par exemple par défaut en localhost `[http://localhost:3000/sitemap.xml](http://localhost:3000/sitemap.xml)` et en production `[http://my-domain-name/sitemap.xml](http://localhost:3000/sitemap.xml)`. 

## Plugins de Lume

Lume est livré avec des [plugins intégrés](https://lume.land/plugins/?status=all), mais vous pouvez facilement ajouter ou supprimer des fonctionnalités selon vos besoins. Vous n'avez pas besoin de tout sur votre site – vous pouvez configurer tout comme vous le souhaitez. 

Vous pouvez ajouter plus de moteurs de template, minifier HTML, CSS et JavaScript avec des plugins, activer la coloration syntaxique du code, la manipulation de dates, la manipulation d'images, le support SVG, et plus encore. 

Vous pouvez également facilement créer vos propres plugins avec lume. [Lume fournit également une excellente documentation](https://lume.land/docs/advanced/plugins/) où vous pouvez en apprendre davantage.

## Comment activer les commentaires

Pour ajouter des commentaires sur votre site Lume, je pense que [utteranc.es](https://utteranc.es/) est le meilleur choix pour tous les générateurs de sites statiques. utteranc.es est un système de commentaires open source basé sur GitHub. Cela ressemble à ceci :

![Activer les commentaires dans lume](https://www.freecodecamp.org/news/content/images/2022/11/enable-coments-on-minimalist-blog.deno-1.png)
_Activer les commentaires_

Si vous souhaitez activer les commentaires sur le site, la première étape consiste à installer une [application utterances](https://github.com/apps/utterances) sur GitHub. Ensuite, copiez et collez le code suivant dans le fichier de lecture de l'article ou là où vous affichez les commentaires sur le site. 

```javascript
<script src="https://utteranc.es/client.js"
        repo="officialrajdeepsingh/Minimalist-blog"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
```

Ensuite, vous devrez modifier le script de commentaire utterance. Le premier changement dans le dépôt `repo="votre-dépôt-github"` est obligatoire. Les autres ne le sont pas. Vous pouvez ajuster selon vos besoins – par exemple, changer le thème, le terme de l'issue, etc. 

Pour en savoir plus sur utterance, voici [un excellent article écrit par Josh Collinsworth](https://joshcollinsworth.com/blog/add-blog-comments-static-site).

La meilleure approche est d'ajouter des commentaires utterance dans lume, puis de lire la [discussion GitHub](https://github.com/lumeland/lume/discussions/312).

## Comment utiliser Netlify CMS avec Lume

Netlify CMS est un système de gestion de contenu open source. Vous pouvez facilement intégrer Netlify avec Lume en utilisant le [plugin netllify_cms](https://lume.land/plugins/netlify_cms/). Il est fourni par Lume, et vous devez simplement l'installer et copier/coller le code.

### Comment installer le plugin Netlify

Importez le plugin Netlify dans votre fichier `_config.ts` pour l'utiliser comme ceci :

```javascript
import lume from "lume/mod.ts";
import netlifyCMS from "lume/plugins/netlify_cms.ts";

const site = lume();

site.use(netlifyCMS());

export default site;
```

Pour le configurer, vous devrez créer un fichier `/_data/netlify_cms.yml` au niveau racine, puis coller le code suivant après avoir redémarré votre serveur :

```yml
backend:
  name: git-gateway
  branch: master

media_folder: statics

collections:
  - label: Posts
    name: posts
    description: Liste des posts
    folder: posts
    extension: md
    create: true
    fields:
      - label: Title
        name: title
        widget: string
      - label: Content
        name: body
        widget: markdown
```

Netlify vous demandera des permissions pour le proxy CMS. Tapez `npx netlify-cms-proxy-server` dans un terminal, appuyez sur entrée ou `type y`, et votre Netlify CMS commencera à fonctionner localement sur l'URL [http://localhost:3000/admin](http://localhost:3000/admin). Maintenant, votre blog Lume est prêt pour le déploiement sur Netlify. 

## Comment déployer votre blog avec Deno Deploy

Vous pouvez déployer Lume sur diverses plateformes telles que Deno Deploy, GitHub Pages, Gitlab Pages, Netlify, Vercel, Fleek, AWS Amplify et Cloudflare Pages. Lume fournit également [une excellente documentation sur le déploiement](https://lume.land/docs/advanced/deployment/). 

Dans cet article, je déploie mon blog Lume avec Deno Deploy (et nous verrons également comment le faire avec GitHub pages). Deno Deploy est une plateforme officielle construite par l'équipe Deno pour déployer des applications basées sur Deno.

Avant de déployer votre blog Lume sur Deno Deploy, assurez-vous de créer un fichier `server.ts` au niveau racine.

```javascript

import Server from "lume/core/server.ts";

const server = new Server({
  port: 8000,
  root: `${Deno.cwd()}/_site`,
});

server.start();

console.log("Écoute sur http://localhost:8000");

```

#### Étapes de déploiement :

1. Créez un compte sur Deno Deploy.
2. Poussez votre code local vers GitHub, puis sélectionnez le fichier `server.ts`. Deno Deploy crée automatiquement un site basé sur le fichier `server.ts`.
3. Assurez-vous de créer d'abord un fichier `server.ts` personnalisé. Puis passez à l'étape suivante.
4. La manière la plus simple de déployer votre site est avec GitHub Actions. Créez un nouveau fichier `.github/workflows/deno.yml` au niveau racine de votre projet et collez le code suivant dedans :

```yml
name: Deploy
on: [push]

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    permissions:
      id-token: write # Nécessaire pour l'authentification avec Deno Deploy
      contents: read # Nécessaire pour cloner le dépôt

    steps:
      - name: Cloner le dépôt
        uses: actions/checkout@v3

      # TODO: ajouter une étape de construction ici

      - name: Upload vers Deno Deploy
        uses: denoland/deployctl@v1
        with:
          project: "minimalist-blog"
          entrypoint: "./serve.ts" 

```

## Comment déployer votre blog avec GitHub Pages

Les GitHub Pages sont des sites statiques gratuits que vous pouvez utiliser pour héberger des pages. Vous pouvez également déployer votre blog Lume dessus. Le processus de déploiement est assez facile. 

Pour déployer Lume sur GitHub pages, vous devez avoir GitHub Actions configuré. 

#### Étapes de déploiement

1. Il est préférable d'avoir un dépôt GitHub afin de pouvoir convertir votre site web local en GitHub Pages.
2. Créez un nouveau dépôt et poussez tout votre code local dedans.
3. Créez un nouveau `.github/workflows/deno.yml` au niveau racine de votre projet, puis collez le code suivant dedans et poussez-le dans le dépôt GitHub. L'action GitHub s'exécute en fonction de l'action `github.yml` et elle génère une GitHub page. 

```yml
name: Publier sur GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Cloner le dépôt
        uses: actions/checkout@v3

      - name: Configurer l'environnement Deno
        uses: denoland/setup-deno@v1
        with:
          deno-version: v1.x

      - name: Construire le site
        run: deno task build

      - name: Déployer
        uses: crazy-max/ghaction-github-pages@v3
        with:
          build_dir: _site
        env:
          GITHUB_TOKEN: ${{ secrets.MY_GITHUB_TOKEN_PAGE }}
```

Vous avez besoin d'un token GitHub pour déployer votre site web Lume sur GitHub pages. C'est une partie requise de la configuration. J'ai trouvé [un excellent article écrit par Davide](https://dev.to/github/the-githubtoken-in-github-actions-how-it-works-change-permissions-customizations-3cgp) qui peut vous aider à en apprendre davantage sur les actions GitHub et comment en créer une.

Les actions GitHub prennent deux ou trois minutes pour terminer l'hébergement de votre site web sur GitHub Pages. 

Consultez le [dépôt GitHub](https://github.com/officialrajdeepsingh/minimalist-blog-github-page) pour apprendre comment configurer le flux de travail GitHub pour les pages GitHub. Vous pouvez également voir une démonstration en direct du [site web sur la page GitHub](https://officialrajdeepsingh.github.io/minimalist-blog-github-page/).

Une note rapide : si vous déployez votre site Lume sur GitHub pages et que votre image ne s'affiche pas sur le site web, il y a deux raisons possibles à cela :

1. Si tous les noms d'images ne sont pas en minuscules, vous pourriez obtenir une erreur. Pour résoudre l'erreur, convertissez les noms de vos images en minuscules avec cette commande : `votre.github.com/votre-nom-de-depot/images/mon-image.png`
2. Si vous utilisez les plugins `base_path` et `relative_urls` de Lume dans votre projet et que `relative_urls` est redondant, vous devrez alors supprimer le plugin `relative_urls` dans votre projet. Votre image devrait maintenant fonctionner correctement.

## Conclusion

Lume est un générateur de site statique facile à apprendre et riche en fonctionnalités. Vous pouvez faire tout ce que vous imaginez avec. Lume vous donne beaucoup de liberté avec le code.

La communauté Lume n'est pas aussi grande que celles de Hugo, 11ty, Jekyll et autres outils. Mais les mainteneurs de Lume répondent activement à tous ceux qui commentent dans la discussion GitHub. Sans une communauté forte, cet outil devrait être en mesure de créer un impact fort.

Un défi avec Lume est qu'il est difficile à prendre en main pour les débutants et est plus adapté aux développeurs intermédiaires et avancés. Si vous vous lancez directement dans l'utilisation de Lume en tant que débutant, vous pourriez avoir du mal avec un manque de connaissances de base sur le fonctionnement des générateurs de sites statiques. 

Pour cette raison, il est utile d'avoir **un peu de connaissances** sur Nuckjunks, JSX et d'autres moteurs de template qui fonctionnent sur la base de markdown. Une fois que vous avez acquis cette expérience, vous pourrez alors facilement utiliser Lume pour concevoir votre blog basé sur markdown. 

Je recommande d'utiliser le [plugin lume MDX](https://lume.land/plugins/mdx/) pour markdown. Vous pouvez utiliser des composants basés sur JSX dans le fichier markdown, et vous pouvez créer de beaux blocs de code, des blocs de conseils, etc.

Je recommande vivement à tous les développeurs d'essayer Lume. Si vous avez des problèmes avec Lume, vous pouvez contacter son créateur sur la [discussion GitHub](https://github.com/lumeland/lume/discussions) et le [serveur Discord](https://discord.com/invite/YbTmpACHWB). 

Si votre cours porte sur l'informatique, la bioinformatique et la biotechnologie, vous pouvez rejoindre ma newsletter gratuite [newsletter](https://www.getrevue.co/profile/officialrajdeepsingh).