---
title: Comment créer un blog statique Markdown avec Deno et le déployer
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2022-09-13T16:46:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-blog-with-deno
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Create-a-Static-Markdown-Blog-with-Deno--1-.png
tags:
- name: blog
  slug: blog
- name: Deno
  slug: deno
- name: JavaScript
  slug: javascript
- name: markdown
  slug: markdown
- name: TypeScript
  slug: typescript
seo_title: Comment créer un blog statique Markdown avec Deno et le déployer
seo_desc: 'Deno is a runtime for JavaScript and TypeScript. The creator of Node.js
  built it, and while Node is built with C and C++, Deno is built with the Rust language.

  You might be wondering what some of the main differences between Node and Deno are.
  Well, ...'
---

Deno est un environnement d'exécution pour JavaScript et TypeScript. Le créateur de Node.js l'a construit, et tandis que Node est construit avec C et C++, Deno est construit avec le langage Rust.

Vous vous demandez peut-être quelles sont les principales différences entre Node et Deno. Eh bien, Rust est un langage de bas niveau similaire à C et Java. Il aide à rendre Deno super rapide, et Deno est également plus sécurisé que Node.

Dans cet article, nous allons construire un blog statique markdown avec Deno en moins de cinq minutes. À la fin, nous déployerons le blog markdown avec Deno deploy.

Nous utiliserons le package tiers [blog package](https://deno.land/x/blog) de Deno créé par Ryan Dahl et un autre contributeur pour le blog.

Avec le module de blog Deno, vous pouvez créer un blog fantastique ultra-rapide. Ensuite, vous pouvez configurer et déployer le blog avec deux lignes de code. Et il faut moins de cinq minutes pour le configurer.

### Qu'est-ce que le markdown ?

[Markdown](https://en.wikipedia.org/wiki/Markdown) est un langage de balisage léger. Il aide à créer du texte formaté de manière cohérente. Pour commencer à travailler en markdown, vous avez besoin d'un IDE qui supporte le markdown et vous devrez créer un fichier avec une extension `.md`. Le markdown supporte généralement les documents écrits, les blogs, et ainsi de suite.

Quelques exemples de documents écrits en Markdown sont les README de GitHub et npm, React.js, et bien d'autres.

Le module de blog Deno (Package) vient avec le support markdown et vous permet de créer un blog statique. Ce module vient avec de nombreuses fonctionnalités, comme :

1. Support Markdown.
2. Rafraîchissement automatique. Toute modification dans un fichier markdown construit et recharge automatiquement votre site web dans le navigateur.
3. Vous pouvez personnaliser l'en-tête et ajouter des commentaires et une section de pied de page.
4. Il supporte le SEO, le balisage SEO, et un flux intégré (sitemap).
5. Support des iFrames avec les fichiers markdown.
6. Il a un support intégré pour Preact, TypeScript, et Tailwind CSS.
7. Il permet plusieurs auteurs.
8. Il a un support de middleware et de redirections de chemin.
9. Il vient avec un support côté serveur pour Google Analytics.

Voici une [démo du blog que nous allons construire et déployer :](https://deno-markdown-blog.deno.dev/)

![démo du blog deno](https://www.freecodecamp.org/news/content/images/2022/09/denoblogdemo.gif)
_démo du blog deno_

Tout le code est [disponible sur GitHub](https://github.com/officialrajdeepsingh/deno-markdown-blog).

### Voici les étapes que nous allons suivre :

1. Comment installer et configurer le blog
2. Comment comprendre la structure des dossiers
3. Comment démarrer le serveur de développement local
4. Comment ajouter plus de configuration au blog.
5. Comment déployer avec Deno

## Comment installer et configurer le blog

Tout d'abord, vous devrez installer le module de blog Deno. Le module de blog vient avec la commande init pour créer une nouvelle configuration de blog. Cela ressemble à ceci :

```
deno run -r --allow-read --allow-write https://deno.land/x/blog/init.ts my-deno-demo-blog-name
```

![Créer une configuration de blog avec le module de blog deno](https://www.freecodecamp.org/news/content/images/2022/09/create-deno-blog.png)
_Créer une configuration de blog avec le module de blog deno_

## Comment comprendre la structure des dossiers

La beauté de Deno est que vous n'avez besoin que de quelques fichiers pour démarrer un projet. Pour le blog markdown, vous n'avez besoin que de quatre fichiers :

![structure des dossiers deno](https://www.freecodecamp.org/news/content/images/2022/09/deno-blog-folder-structure--1-.png)
_structure des dossiers deno_

Passons en revue chaque fichier dans la structure de dossiers ci-dessus :

* Dans le fichier `deno.jsonc`, vous ajoutez des tâches et le fichier importMap. Les tâches sont similaires aux scripts dans Node, et dans la section importMap, vous passez un fichier JSON qui contient tous vos packages d'importation de Deno.
* Le fichier `import_map.json` contient les imports de tous les packages dont vous avez besoin pour exécuter votre projet.
* Le dossier `posts` contient tous les fichiers markdown.
* Le fichier `main.tsx` contient toutes les configurations pour le module de blog.

## Comment démarrer le serveur de développement local

Une fois l'installation terminée, exécutez le serveur de développement local avec la commande `deno task dev`.

![Exécuter le serveur de développement local deno](https://www.freecodecamp.org/news/content/images/2022/09/run-deno-blog.png)
_Exécuter le serveur de développement local deno_

## Comment ajouter plus de configuration au blog

Le module de blog par défaut vient avec la configuration suivante dans le fichier `main.tsx`. Vous pouvez facilement changer les configurations du blog selon vos besoins.

```typescript
// main.tsx

import blog, { ga, redirects, h } from "blog";

blog({
  title: "Mon Blog",
  description: "Ceci est mon nouveau blog.",
  // header: <header>Votre en-tête personnalisé</header>,
  // section: <section>Votre section personnalisée</section>,
  // footer: <footer>Votre pied de page personnalisé</footer>,
  avatar: "https://deno-avatar.deno.dev/avatar/blog.svg",
  avatarClass: "rounded-full",
  author: "Un auteur",

  // middlewares: [

    // Si vous voulez configurer Google Analytics, collez votre clé GA ici.
    // ga("UA-XXXXXXXX-X"),

    // Si vous voulez fournir des redirections, vous pouvez les spécifier ici,
    // le chemin spécifié dans une clé redirigera vers le chemin dans la valeur.
    // redirects({
    //  "/hello_world.html": "/hello_world",
    // }),

  // ]
});
```

### Configuration personnalisée

![Démo de la configuration personnalisée](https://www.freecodecamp.org/news/content/images/2022/09/denoblog.png)
_Démo de la configuration personnalisée_

Avec une configuration personnalisée, vous pouvez faire en sorte que votre site web ait l'apparence que vous souhaitez – même comme l'exemple ci-dessus. De plus, vous pouvez rapidement ajouter plus de configurations personnalisées à votre blog.

Par exemple, vous pouvez changer l'en-tête par défaut, le pied de page, le titre, l'auteur, le thème, le style personnalisé, les liens, la section, et ainsi de suite. Voici un exemple de code pour le faire :

```javascript
// main.tsx

/** @jsx h */
import blog, { h } from "blog";
import { Section } from './components/Section.jsx';

blog({
  author: "Rajdeep singh",
  title: "Bonjour, je m'appelle Rajdeep Singh",
  description: "Ravi de vous rencontrer",
  avatar:"assets/logos/profile.jpg",
  avatarClass: "rounded-full",
  coverTextColor:"white",
  links: [
    { title: "Email", url: "mailto:officialrajdeepsingh@gmail.com" },
    { title: "GitHub", url: "https://github.com/officialrajdeepsingh" },
    { title: "Twitter", url: "https://twitter.com/Official_R_deep" },
    { title: "Linkedin", url: "https://www.linkedin.com/in/officalrajdeepsingh/" },
  ],
  lang: "en",
  favicon: "favicon.ico",
  section: <Section/>,
  theme:"auto",
  cover:"assets/logos/backgroundbanner.png",
  ogImage: {
    url: "http://localhost:8000/assets/logos/Frame.png",
    twitterCard:  "summary_large_image" 
  },
  style:".markdown-body ul, .markdown-body ol { list-style: disc !important;}"
});
```

Les fichiers Markdown supportent divers types de frontMatter. Les types de frontMatter les plus courants et largement utilisés sont :

1. YAML : YAML est identifié par l'ouverture et la fermeture `---`.
2. JSON : JSON est identifié par `{` et `}`.
3. TOML : TOML est identifié par l'ouverture et la fermeture `+++`.

Le frontMatter le plus courant est [YAML](https://yaml.org/). Le support de frontMatter YAML pour les fichiers markdown est partout. Mais **le module de blog Deno ne supporte que le frontMatter yml**.

![exemple de front matter yml](https://www.freecodecamp.org/news/content/images/2022/09/markdownfile.png)
_exemple de front matter yml_

Le fichier Markdown est divisé en deux sections. La première section est l'en-tête (frontMatter), et la seconde est la section du corps.

La section d'en-tête contient toutes les métadonnées de l'article. Toutes les métadonnées sont écrites à l'intérieur de trois tirets (`---`) à la fois pour l'ouverture et la fermeture – par exemple, le titre de l'article, le tag, la description, la date de publication, et ainsi de suite.

Enfin, dans la section du corps, vous écrivez le corps de votre article et l'expliquez.

```markdown
// hello-world.md

---
author : "Rajdeep Singh"
publish_date : "2020-11-10T11:42:46Z"
description : "Easy Ways Add CSS in Next.js #SeriesPart2"
og:image : "assets/images/next.js-add-css-code.jpg"
tags : ["Next.js", "Next", "Next.js Framework", "Next.js Tutorial", "React.js", "react.js tutorial"]
title : "How To Add CSS In Next js?"
allow_iframes: true
cover_html: <img src="assets/images/next.js-add-css-code.jpg" alt="How To Add CSS In Next js" />
pathname: "hello-world"
---

Premier article de blog créé avec le package de blog Deno. C'est un package incroyable que vous pouvez utiliser pour créer des blogs markdown avec Tailwind CSS.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3NR9Spj0DmQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


```javascript
console.log("hello world")
```

```

Le module de blog Deno supporte les champs YML FrontMatter suivants dans un fichier markdown :

1. author (string) : L'`author` contient les noms des auteurs. Par exemple, `author : "Rajdeep singh , deno"`
2. publish_date(Date) : La `publish_date` est requise pour l'article.
3. description (string) : La `description` est requise pour la description.
4. og:image(string) : L'`og:image` n'est pas requis. Il est utilisé pour `<meta property="og:image" content="assets/images/Title-tag-In-HTML-5.jpg">`
5. tags(string[]) : Les `tags` sont juste des mots-clés utilisés pour le SEO. Ils ne sont pas obligatoires.
6. title(string) : Le `title` est requis pour le titre.
7. allow_iframes( boolean ) : `allow_iframes` vous permet d'utiliser `iframe` HTML.
8. pathname( string ) : pathname n'est pas requis. Par exemple, `http://yourdomain.com/hello-world` après votre domaine `hello-world` est votre pathname
9. cover_html(string) : Le `cover_html` contient le HTML pour le blog.

```
author : "Rajdeep Singh , Rajvinder singh"
publish_date : "2022-03-20T13:09:24Z"
description : "Npm install command help to install package from npmjs.org"
og:image : "assets/images/npm-init-command-1.png"
tags : ["npm-test", "npm-cli", "npm install command"]
title : "What is the npm install command?"
allow_iframes: true
pathname:"/how-is-npm-install-command"
cover_html: <img src="assets/images/npm-init-command-1.png" alt="npm command" />
```

Ce sont tous les champs supportés par YML frontMatter pour les fichiers markdown :

```
title, author, publish_date, description, og:image, tags, allow_iframes, pathname, cover_html
```

C'est le champ requis pour les fichiers markdown :

```
title
```

Sans un champ de titre, le module de blog produit une erreur `Uncaught TypeError: Cannot read properties of undefined (reading 'snippet')`.

![erreur : Uncaught TypeError: Cannot read properties of undefined (reading 'snippet')](https://www.freecodecamp.org/news/content/images/2022/09/undefiend-snippet-error.png)
_Erreur : Uncaught TypeError: Cannot read properties of undefined (reading 'snippet')_

## Comment déployer votre blog avec Deno

La dernière étape consiste à déployer notre blog statique dans Deno. Actuellement, le module de blog Deno ne supporte que Deno pour le déploiement. Mais Deno deploy fournit une interface similaire à Netlify et Vercel. Vous pouvez donc facilement comprendre le tableau de bord si vous avez déjà travaillé avec ces outils.

Pour déployer un nouveau blog sur Deno, vous avez besoin de deux choses. La première est un compte sur [Deno deploy](https://deno.com/deploy), et la seconde est un compte GitHub. Avec un dépôt GitHub pour vous aider à gérer vos articles, c'est un processus simple similaire à [Vercel](https://vercel.com/) et [Netlify](https://www.freecodecamp.org/news/p/00c3cfd3-6447-48dc-a915-804b26bf056e/netlify.com).

### Étapes de déploiement :

Voici les étapes pour déployer votre blog avec Deno deploy (nous passerons en revue chacune d'elles en détail ci-dessous) :

1. Tout d'abord, connectez-vous à votre compte sur Deno deploy
2. Cliquez pour créer un nouveau projet
3. Configurez le dépôt GitHub et les variables d'environnement
4. Déployez le blog statique

### Connectez-vous à votre compte sur Deno deploy

Tout d'abord, allez sur le site [Deno deploy](https://deno.com/deploy) et créez un nouveau compte si vous n'en avez pas déjà un. Si vous en avez un, connectez-vous à votre compte.

![site web deno deploy](https://www.freecodecamp.org/news/content/images/2022/09/deno-deploy-dashboard.png)
_site web deno deploy_

### Cliquez pour créer un nouveau projet

Après vous être connecté avec succès, vous pouvez maintenant accéder au tableau de bord Deno et cliquer sur le bouton "+ **nouveau projet**".

![créer un nouveau projet avec deno deploy](https://www.freecodecamp.org/news/content/images/2022/09/create-project-with-deno.png)
_Créer un nouveau projet avec deno deploy_

### Configurez le dépôt GitHub et les variables d'environnement

Après avoir cliqué sur le bouton **nouveau projet**, vous serez redirigé vers la page de configuration du projet. Votre page de projet ressemblera à ceci. Remplissez simplement tous les détails :

![Remplir la nouvelle configuration du projet et lier github](https://www.freecodecamp.org/news/content/images/2022/09/fillinfoindeno.png)
_Remplissez la nouvelle configuration de votre projet et liez-la à GitHub_

La première fois, cliquez sur le bouton GitHub. Après cela, Deno deploy demande la permission pour un compte GitHub. Après avoir accordé toutes les permissions, votre page de projet ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/clicktolinkbuttontodeployblogondeno.png)
_Après avoir terminé les informations_

1. Après avoir ouvert la page du projet, vous remplissez toutes les informations requises.
2. Ensuite, dans la deuxième étape, sélectionnez le dépôt GitHub.
3. Après avoir sélectionné le dépôt GitHub, sélectionnez une branche, puis choisissez le fichier `main.tsx`.
4. Donnez un nom de projet, mais assurez-vous que votre nom est en lettres minuscules – par exemple, my-new-website. Sinon, vous obtiendrez une erreur de majuscule.
5. Cliquez sur la variable d'environnement et ajoutez un environnement (si vous en avez un – sinon, passez cette étape).

Et c'est tout – vous avez terminé toutes les configurations avec succès. Cliquez maintenant sur le bouton de lien.

### Le déploiement est terminé

Après la fin du déploiement, vous verrez le tableau de bord du site web. Cliquez sur le bouton de vue pour voir votre site web prêt pour la production.

![Votre tableau de bord de site web avec deno ressemble à ceci après le déploiement réussi du site web](https://www.freecodecamp.org/news/content/images/2022/09/denowebsitedashborad.png)
_Votre tableau de bord de site web avec deno ressemble à ceci après le déploiement réussi du site web._

Voici un conseil pour vous aider à gérer tous vos fichiers markdown et accélérer votre travail d'écriture. L'éditeur de code VS Code a une extension gratuite et open-source [FrontMatter VS Code extension](https://frontmatter.codes/). C'est un excellent outil pour gérer tous vos fichiers markdown à l'intérieur de VS Code avec le tableau de bord FrontMatter.

![gérer les fichiers markdown avec l'extension vscode](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-from-2022-09-13-18-18-32.png)
_Gérer les fichiers markdown avec l'extension VS Code_

## Conclusion

Le module de blog Deno est une excellente bibliothèque pour créer un blog personnel en cinq minutes et le déployer avec Deno. Le déploiement Deno est très rapide. Il prend moins de dix secondes.

Je pense que le module de blog Deno est le meilleur pour un usage personnel car vous n'avez pas besoin de personnaliser beaucoup de choses. Vous ne personnalisez que l'en-tête, le pied de page et diverses sections.

Merci d'avoir lu !

### Références pour vous aider à configurer votre blog :

* [https://deno.land/](https://deno.land/)
* [https://deno.com/deploy](https://deno.com/deploy)
* [https://deno.land/x/blog](https://deno.land/x/blog@0.5.0)
* [https://deno.land/x/dotenv](https://deno.land/x/dotenv)
* [https://frontmatter.codes/](https://frontmatter.codes/)



---