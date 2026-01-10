---
title: Comment créer une documentation avec docs.page – Un tutoriel pour débutants
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2025-05-06T18:31:39.403Z'
originalURL: https://freecodecamp.org/news/how-to-create-documentation-with-docspage
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746471569068/23f70d3e-a76e-4287-a6a9-579c23a4fcb2.png
tags:
- name: documentation
  slug: documentation
- name: Beginner Developers
  slug: beginners
seo_title: Comment créer une documentation avec docs.page – Un tutoriel pour débutants
seo_desc: 'One of the most tedious tasks for every startup, company, and open-source
  project is often building and managing documentation – especially for medium to
  large-scale documentation websites.

  docs.page is an open-source documentation tool that helps yo...'
---

L'une des tâches les plus fastidieuses pour chaque startup, entreprise et projet open-source est souvent la création et la gestion de la documentation – surtout pour les sites web de documentation de moyenne à grande échelle.

[**docs.page**](http://docs.page) est un outil de documentation open-source qui vous aide à créer des sites web de documentation instantanés, rapides, beaux et réactifs avec une configuration minimale. Il s'agit d'un projet open-source développé par Invertase, une entreprise connue pour créer des outils et des SDK pour développeurs.

docs.page est conçu pour rationaliser le processus de publication de la documentation en obtenant du contenu directement à partir de dépôts GitHub publics.

### Fonctionnalités clés :

* Configuration zéro : vous créez un fichier 'docs.json' et un répertoire 'docs'. À l'intérieur du répertoire docs, vous pouvez créer des fichiers en utilisant l'extension .mdx, et docs.page générera votre site de documentation.
    
* Personnalisable : docs.page vous permet d'ajouter votre logo, des liens sociaux, un thème, des analyses, une navigation, et plus encore via un simple fichier de configuration.
    
* Prévisualisations en direct : permet de visualiser la documentation pour toute branche, pull request ou commit spécifique, facilitant la collaboration et la révision en temps réel.
    
* Rechargement à chaud : la fonctionnalité de rechargement à chaud fournit des prévisualisations en temps réel des modifications de la documentation lors de l'édition de fichiers Markdown (.mdx). Cette fonctionnalité améliore le flux de travail de développement local, permettant des mises à jour instantanées sans rafraîchissements ou reconstructions manuels.
    
* Intégration du bot GitHub : fournit un bot GitHub qui génère automatiquement des URL pour les prévisualisations de documentation des pull requests.
    
* Support MDX : vous pouvez écrire de la documentation en Markdown pour utiliser MDX, ce qui vous permet d'utiliser des composants React, tels que des onglets, des cartes, des tweets et des étapes, directement dans votre fichier Markdown.
    
* Fonctionnalité de recherche : s'intègre avec DocSearch pour offrir des capacités de recherche en texte intégral dans votre documentation.
    
* Conception réactive : garantit que votre documentation est accessible et visuellement attrayante sur une gamme d'appareils et de tailles d'écran.
    
* Mode sombre/clair : offre une personnalisation du thème pour basculer entre les modes sombre et clair.
    
* Mise en évidence des blocs de code : fournit une mise en évidence de la syntaxe et des fonctionnalités de copie de contenu pour les blocs de code.
    

Consultez le code [disponible dans mon dépôt GitHub](https://github.com/officialrajdeepsingh/docs-page-demo).

## **Table des matières :**

* [Comment fonctionne](#heading-comment-fonctionne-docspage) [docs.page](http://docs.page) [?](#heading-comment-fonctionne-docspage)
    
* [Comment activer la prévisualisation en direct dans](#heading-comment-activer-la-previsualisation-en-direct-dans-docspage) [docs.page](http://docs.page)
    
* [Comment configurer](#heading-comment-configurer-docspage) [docs.page](http://docs.page)
    
* [Comment utiliser les composants pré-construits dans](#heading-comment-utiliser-les-composants-pre-construits-dans-docspage) [docs.page](http://docs.page)
    
* [Comment diagnostiquer les erreurs dans](#heading-comment-diagnostiquer-les-erreurs-dans-docspage) [docs.page](http://docs.page)
    
* [Comment utiliser le Frontmatter](#heading-comment-utiliser-le-frontmatter)
    
* [Comment ajouter des actifs à vos docs](#heading-comment-ajouter-des-actifs-a-vos-docs)
    
* [Comment publier votre site web de documentation](#heading-comment-publier-votre-site-web-de-documentation)
    
* [Comment prévisualiser en direct vos prochaines modifications sur votre site web de documentation ?](#heading-comment-previsualiser-en-direct-vos-prochaines-modifications-sur-votre-site-web-de-documentation)
    
* [Conclusion](#heading-conclusion)
    

## Comment fonctionne docs.page ?

Vous pouvez facilement commencer à créer votre page de documentation en utilisant [docs.page CLI](https://use.docs.page/cli). Il vous aide à configurer un projet de documentation local en exécutant la commande suivante :

```bash
pnpm dlx @docs.page/cli init docs.page
```

La sortie de la commande apparaît comme suit :

```bash
pnpm dlx @docs.page/cli init docs.page
? Êtes-vous sûr de vouloir configurer et installer docs.page dans /home/officialrajdeepsingh/medium/docs.page ? oui
Fichiers créés :
 - docs.json : Fichier de configuration pour votre site de documentation
 - docs/index.mdx : La page d'accueil de votre site de documentation
 - docs/next-steps.mdx : Une page pour vous aider à commencer avec docs.page

Initialisation terminée. Pour prévisualiser votre site de documentation, visitez https://docs.page/preview dans votre navigateur.
```

Après avoir créé votre projet avec docs.page CLI, la structure de votre projet devrait apparaître comme suit :

```bash
.
├── docs
│   ├── index.mdx
│   └── next-steps.mdx
└── docs.json

2 répertoires, 3 fichiers
```

Le dossier `docs` contient le fichier Markdown pour votre documentation, et le fichier `docs.json` inclut la configuration pour votre site web, telle que l'en-tête, la barre latérale, le logo, le thème et d'autres paramètres.

## Comment activer la prévisualisation en direct dans docs.page

Vous pouvez configurer la prévisualisation en direct de votre documentation locale en temps réel dans le navigateur – mais c'est un peu différent : vous n'avez pas besoin d'exécuter des commandes de développement sur votre ordinateur portable ou votre machine.

Pour ouvrir la prévisualisation en direct de votre documentation locale, visitez d'abord [https://docs.page](https://docs.page) et cliquez sur le bouton **Local Preview**.

![Prévisualisez votre documentation locale en direct directement dans le navigateur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745671253187/c2e6ce0b-aedb-4e7e-b680-68e590fc4018.png align="center")

Ensuite, sélectionnez le projet de documentation sur votre ordinateur portable ou votre machine et cliquez sur le bouton "**Select Directory**".

![cliquez sur le bouton "Select Directory" et sélectionnez le répertoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1745664832273/fc03e2d5-02c0-4bce-b40c-a2599ef72195.png align="center")

Après avoir cliqué sur le bouton "Select Directory", une nouvelle fenêtre s'ouvrira en fonction de votre système d'exploitation. Son interface utilisateur peut apparaître différente. Ensuite, vous devez sélectionner le projet.

![Sélectionnez le répertoire](https://cdn.hashnode.com/res/hashnode/image/upload/v1745664861969/39a31043-22e8-4d6b-a883-19be0a59ca4d.png align="center")

Après avoir sélectionné le dossier, vous verrez le message d'alerte suivant dans le navigateur ("Autoriser le site à voir les fichiers ?"). Pour voir la prévisualisation en direct de votre site web de documentation, cliquez sur le bouton "View files".

![Cliquez sur le bouton View files](https://cdn.hashnode.com/res/hashnode/image/upload/v1745664971450/8ec6f635-a2e4-401e-8fa8-cf49c4e06b9a.png align="center")

Maintenant, vous pouvez voir une prévisualisation en direct locale du site web de documentation dans le navigateur, et toute modification que vous apportez localement se reflétera instantanément dans le navigateur. Par défaut, votre site web de documentation devrait apparaître comme suit :

![Prévisualisez votre site web de documentation dans le navigateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1745674174727/dd4f1820-ce04-4244-b395-b055bb8d236a.png align="center")

Ensuite, vous apprendrez à configurer le logo, le thème, l'en-tête, les liens sociaux, la barre latérale, le SEO, la recherche et plus encore sur vos docs. Vous apprendrez également à utiliser les composants pré-construits, le Front Matter et les actifs sur docs.page, et enfin, comment déployer votre site web de documentation.

## Comment configurer docs.page

![Configurez docs.page dans le fichier docs.json.](https://cdn.hashnode.com/res/hashnode/image/upload/v1745834873075/6c9dd17b-20e2-40dc-87a1-39cc27cf9a20.png align="center")

Le fichier `docs.json` est le fichier principal pour configurer votre documentation. Ci-dessous se trouve une [liste de toutes les options de configuration disponibles](https://use.docs.page/configuration), que vous pouvez utiliser pour modifier les logos, le thème, les analyses, et plus encore sur vos docs.

### **Propriétés**

* Propriétés de base
    
* Logo
    
* Thème
    
* En-tête
    
* Ancre
    
* Liens sociaux
    
* SEO
    
* Variables
    
* Recherche
    
* Scripts
    
* Contenu
    
* Onglets
    
* Barre latérale
    

Il y a tant de choses que vous pouvez configurer avec docs.page – mais dans ce tutoriel, nous nous concentrerons sur certaines des options les plus importantes :

* [Propriétés](#heading-proprietes)
    
* [Propriétés de base](#heading-proprietes-de-base)
    
* [Logo](#heading-logo)
    
* [Thème](#heading-theme)
    
* [En-tête](#heading-en-tete)
    
* [Liens sociaux](#heading-liens-sociaux)
    
* [SEO](#heading-seo)
    
* [Recherche](#heading-recherche)
    
* [Onglets](#heading-onglets)
    
* [Barre latérale](#heading-barre-laterale)
    

### Propriétés de base

![Propriétés de base telles que le nom, la description et la favicon](https://cdn.hashnode.com/res/hashnode/image/upload/v1745915741849/802ba7e3-ae6b-4628-856f-0d78aa4e1bfc.png align="center")

docs.page inclut des propriétés de base courantes, telles que le nom, la description et la favicon, qui sont très importantes pour le SEO.

* nom (string) : Le nom de votre projet. Il apparaît dans l'en-tête et est utilisé pour des choses comme les métadonnées SEO.
    
* description (string) : Un résumé de votre projet. Cela est utilisé dans les balises méta et les images de prévisualisation sociale.
    
* favicon (string | objet Favicon) : Spécifie la favicon affichée dans l'onglet du navigateur. Vous pouvez fournir soit une URL de chaîne unique, soit utiliser un objet Favicon pour définir différentes icônes pour les modes clair et sombre :
    
    * light (string) : URL de la favicon en mode clair.
        
    * dark (string) : URL de la favicon en mode sombre.
        

```json
// docs.json
{
  "name": "Docs.page",
  "description": "Livrez de la documentation, comme vous livrez du code",
  "favicon": "https://static.invertase.io/assets/docs.page/docs-page-logo.png",
   # ou
  "favicon": {
    "light": "https://cdn-icons-png.flaticon.com/24/9664/9664027.png",
    "dark": "https://cdn-icons-png.flaticon.com/24/9643/9643115.png"
  }
}
```

### Logo

![Configurez le logo pour votre documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1745750725706/1f3f2775-91d8-4365-88b4-1a43160d12c3.png align="center")

Il est maintenant temps de configurer le logo pour votre documentation, qui apparaîtra dans l'en-tête et sera utilisé pour les images de prévisualisation sociale.

La hauteur minimale du logo doit être de 24px. Vous pouvez fournir des URL pour un logo clair et un logo sombre. Si vous ne fournissez qu'un logo clair ou sombre, et qu'il ne fonctionne pas, vous pourriez rencontrer des problèmes où votre logo n'apparaît pas sur le site web lorsque vous basculez le thème.

Vous pouvez ajouter le logo à la documentation de deux manières :

* Première manière :
    

```json
// docs.json
{
  "name": "My Docs",
  "logo": "https://cdn-icons-png.flaticon.com/24/2702/2702154.png",
}
```

* Deuxième manière :
    

```json
// docs.json
{
  "name": "My Docs",
  "logo": {
    "light": "https://cdn-icons-png.flaticon.com/24/2702/2702154.png",
    "dark": "https://cdn-icons-png.flaticon.com/24/2702/2702172.png"
  }
}
```

### Thème

Configurer le thème dans votre documentation est facile. Si vous ne fournissez pas de thème, le thème par défaut sera utilisé dans votre documentation.

docs.page inclut une propriété de thème dans docs.json, qui contient un objet Thème comme valeur avec les propriétés `defaultTheme`, `primary`, `primaryLight`, `backgroundLight` et `backgroundDark`.

* `defaultTheme` : Vous pouvez sélectionner un thème, sombre ou clair.
    
* `primary` : La couleur primaire est utilisée pour les liens, les boutons et autres éléments interactifs.
    
* `primaryLight` : L'option de couleur `primaryLight` est utilisée en mode clair. Si votre option de couleur primaire claire n'est pas spécifiée dans le fichier `docs.json`, alors la couleur primaire sera utilisée.
    
* `primaryDark` : L'option de couleur `primaryDark` est utilisée en mode sombre. Si votre option `primaryDark` n'est pas spécifiée dans le fichier `docs.json`, alors la couleur primaire sera utilisée.
    
* `backgroundLight` : L'option `backgroundLight` est utilisée pour spécifier la couleur de fond de votre documentation en mode clair.
    
* `backgroundDark` : L'option `backgroundDark` est utilisée pour spécifier la couleur de fond de votre documentation en mode sombre.
    

```json
// docs.json
{
  "theme": {
    "defaultTheme": "dark",
    "primary": "#de40eb",
    "primaryLight": "#BFA213",
    "backgroundLight": "#e0cfff",
    "backgroundDark": "#00101f"
  },
}
```

### En-tête

![configuration de l'en-tête dans votre documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1745912602721/2430492a-8d58-4f4b-bc4c-e22f8cb7b52f.png align="center")

Configurer l'en-tête dans votre documentation inclut les propriétés suivantes : `showName`, `showThemeToggle`, `showGitHubCard` et links.

* `showName` : L'option `showName` affiche le nom de la documentation à côté du logo dans l'en-tête et par défaut elle est vraie.
    
* `showThemeToggle` : L'option `showThemeToggle` affiche le bouton de basculement de thème dans l'en-tête (et par défaut à vrai).
    
* `showGitHubCard` : L'option `showGitHubCard` affiche la carte GitHub dans l'en-tête et par défaut à vrai.
    
* Links : L'option links contient un tableau d'objets Link pour afficher une navigation dans l'en-tête de votre documentation.
    

```json
// docs.json
{
  "header": {
    "showName": false,
    "showGitHubCard": false,
    "links": [
      {
        "title": "GitHub",
        "href": "https://github.com/officialrajdeepsingh/docs-page-demo"
      },
      {
        "title": "X",
        "href": "https://x.com/Official_R_deep"
      },
      {
        "title": "Linkedin",
        "href": "https://www.linkedin.com/in/officalrajdeepsingh"
      }
    ]
  }
}
```

### Liens sociaux

![configuration des liens sociaux dans votre documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1745910990442/f48a4b34-d20f-4155-b19a-d8af8a202801.png align="center")

L'option sociale contient un objet de paires clé-valeur où la clé représente la plateforme sociale et la valeur correspond au nom d'utilisateur ou à l'ID. Voici comment vous pouvez les ajouter :

```json
// docs.json
{
  "social": {
    "github": "officialrajdeepsingh/docs-page-demo",
    "x": "@Official_R_deep",
    "linkedin": "officalrajdeepsingh"
  }
}
```

### SEO

L'option SEO configure les paramètres SEO pour votre documentation. L'option noindex indique aux moteurs de recherche de ne pas indexer votre documentation, et elle est par défaut à false.

```json
// docs.json
{
  noindex: true
}
```

### Recherche

![configuration de la recherche dans votre documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1745909928336/a85c4f21-712d-4096-be08-15d605668a68.png align="center")

Pour activer la fonctionnalité de recherche sur votre site de documentation, vous pouvez intégrer Algolia DocSearch en configurant l'objet docsearch dans votre fichier `docs.json` comme ceci :

```json
// docs.json
{
 "search": {
    "docsearch": {
      "appId": "YOUR_APP_ID",
      "apiKey": "YOUR_API_KEY",
      "indexName": "YOUR_INDEX_NAME"
    }
  }
}
```

### Onglets

![configuration de l'onglet dans votre documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1745909877477/9248bfa7-ed16-4d2a-9d2a-6624d4690123.png align="center")

Les onglets sont un tableau d'objets affichés en haut de votre site web de documentation.

#### Propriétés

Chaque objet Tab inclut les propriétés suivantes :

* id (string, requis) : Un identifiant unique pour l'onglet.
    
* title (string, requis) : L'étiquette de texte affichée sur l'onglet.
    
* href (string, requis) : L'URL à laquelle naviguer lorsque l'onglet est cliqué.
    
* locale (string, optionnel) : Si défini, cet onglet est affiché uniquement lors de la visualisation de la documentation pour la locale spécifiée.
    

Voici un exemple de quelques onglets :

```json
{
  "tabs": [
    {
      "id": "root",
      "title": "Documentation",
      "href": "/"
    },
    {
      "id": "components",
      "title": "Composants",
      "href": "/components"
    }
  ],
}
```

### Barre latérale

Pour afficher la barre latérale sur votre site web, vous pouvez la configurer ou la définir dans le fichier `docs.json` de votre documentation, qui apparaîtra dans la barre latérale de votre site.

![configuration de la barre latérale dans votre documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1745911338226/f3404a5d-b715-4e26-97c9-ce8169fe8d6b.png align="center")

Essentiellement, une barre latérale est une liste de liens qui apparaît sur le côté de votre documentation. Vous pouvez organiser les liens en utilisant des groupes et des pages en fournissant un tableau d'objets de barre latérale.

#### Options :

* pages : L'option pages prend une liste de liens de page à afficher dans la barre latérale. Elle accepte les options suivantes :
    
    * title (requis) : Le titre de l'élément de la barre latérale.
        
    * href (requis) : L'URL à laquelle lier lorsque l'élément de la barre latérale est cliqué.
        
    * icon (optionnel) : L'icône à afficher à côté de l'élément de la barre latérale.
        

* group (string) : Le titre du groupe sous lequel l'élément de la barre latérale sera affiché. Si non fourni, l'élément apparaîtra au niveau supérieur de la barre latérale.
    
* href (string) : L'URL à laquelle l'élément de la barre latérale liera lorsqu'il sera cliqué.
    
* icon (string) : Le nom de l'icône à afficher à côté de l'élément de la barre latérale.
    
* tab (string) : Si défini, l'élément de la barre latérale ne sera affiché que lorsqu'un onglet spécifique (correspondant à l'ID de l'onglet fourni) est actif.
    

```json
// docs.json
{
"sidebar": [
    {
      "pages": [
        {
          "title": "Aperçu",
          "href": "/",
          "icon": "book"
        },
        {
          "title": "Configuration",
          "href": "/configuration",
          "icon": "gear"
        }
      ]
    },
    {
      "group": "Composants",
      "icon": "grip",
      "pages": [
        {
          "title": "Prise en main",
          "href": "/components",
          "icon": "rocket"
        },
        {
          "title": "Accordéon",
          "href": "/components/accordion",
          "icon": "square-caret-down"
        },
        {
          "title": "Appels",
          "href": "/components/callouts",
          "icon": "bullhorn"
        },
        {
          "title": "Cartes",
          "href": "/components/cards",
          "icon": "square-full"
        }
      ]
    }
  ]
}
```

Si vous souhaitez en savoir plus à ce sujet, consultez la [documentation ici](https://use.docs.page/configuration#sidebar).

## Comment utiliser les composants pré-construits dans docs.page

docs.page est livré avec [15 composants pré-construits](https://use.docs.page/components), vous n'avez donc pas besoin d'importer des composants dans votre fichier MDX. Vous pouvez les utiliser directement dans votre fichier MDX.

Dans l'exemple suivant, j'utilise le composant Info Callout directement dans le fichier MDX, sans l'importer.

```markdown
// index.mdx
---
title: Bienvenue sur docs.page!
description: Commencez avec docs.page
---

Bienvenue sur docs.page! La commande init que vous venez d'exécuter a créé une structure de fichiers de base dans votre projet pour vous aider à commencer.

## Guide

### Configuration

À la racine de votre répertoire, un nouveau fichier `docs.json` a été créé. Ce fichier est utilisé pour configurer votre site de documentation. Vous pouvez personnaliser le nom, la description, la barre latérale, le thème, les logos et plus encore en utilisant ce fichier.


<Info>Voici un exemple de base de ce à quoi ressemble le fichier : </Info>
```

## Comment diagnostiquer les erreurs dans docs.page

Si vous rencontrez des erreurs sur votre site web de documentation, vous pouvez voir toutes les erreurs en cliquant sur le bouton de diagnostic.

![diagnostiquer l'erreur dans docs.page](https://cdn.hashnode.com/res/hashnode/image/upload/v1745863994785/16ec2f9a-86e6-4808-abdb-73513a54d428.png align="center")

## Comment utiliser le Frontmatter

Le front matter est un bloc de YAML placé au début d'un fichier Markdown, enfermé entre des lignes de triple tiret `(---)`.

Le frontmatter est un moyen de personnaliser la page de métadonnées directement dans vos fichiers Markdown, et surtout, le frontmatter est utilisé pour le SEO.

```markdown
# docs/getting-started.mdx
---
title: Bienvenue dans le projet Awesome
description: Une documentation géniale !
---

# Bienvenue !
```

Ci-dessous se trouve une liste de certaines des [propriétés importantes du frontmatter](https://use.docs.page/frontmatter) dans docs.page, y compris leur type et leurs valeurs par défaut :

* `title` (string) : Le titre de la page utilisé dans les métadonnées, les cartes sociales et affiché comme en-tête principal.
    
* `description` (string) : Un résumé de la page apparaît dans les métadonnées pour le SEO et les aperçus de liens.
    
* `image` (string) : URL d'un actif utilisé dans les cartes sociales et (si activé) affiché en haut de la page.
    
* `redirect` (string) : Une URL pour rediriger les visiteurs. Lorsqu'elle est définie, le contenu de la page est contourné.
    
* `showPageTitle` (boolean) : Basculer si le titre de la page apparaît comme un en-tête en haut.
    
* `showPageImage` (boolean) : Basculer si l'image du front-matter est rendue en haut.
    
* `noindex` (boolean) : Si vrai, indique aux moteurs de recherche de ne pas indexer la page.
    

[Consultez la documentation](https://use.docs.page/frontmatter) pour plus de détails et d'autres informations sur les propriétés du frontmatter.

## Comment ajouter des actifs à vos docs

Vous pouvez inclure des actifs, tels que des images et des vidéos, dans votre documentation. Vous pouvez ajouter des actifs distants et locaux.

### Actifs distants

Pour ajouter des actifs distants à votre documentation, vous pouvez les référencer directement dans vos fichiers markdown.

Par exemple, pour inclure une image à partir d'une URL :

```markdown
# getting-started.mdx
---
title: Bienvenue pour commencer
description: Une documentation géniale !
---

# Bienvenue !

![Natural](https://cdn.pixabay.com/photo/2023/04/19/19/11/lake-7938396_960_720.jpg)
```

### Actifs locaux

Pour utiliser des actifs locaux dans votre documentation, créez un dossier `assets` à l'intérieur du répertoire `docs/`. Ensuite, ajoutez des images et des vidéos au dossier assets et référencez-les dans vos fichiers Markdown.

Consultez ce qui suit pour mieux comprendre :

```bash
docs/
  assets/
    natural.png
  index.mdx
```

Dans votre fichier markdown, vous pouvez référencer l'image en utilisant un chemin relatif :

```markdown
![Description](/assets/natural.png)
```

### Différence entre les actifs locaux et distants

Les actifs locaux (PNG, JPG, PDF, etc.) sont des fichiers stockés dans le dossier public de votre projet, tandis que les actifs distants sont des fichiers hébergés sur un serveur externe. Vous pouvez accéder à vos actifs locaux en utilisant l'URL de votre domaine.

```markdown
![Natural](./assets/logo.png)
```

D'autre part, les actifs distants sont stockés sur un serveur différent (hébergement d'images), comme je l'ai mentionné. Vous pouvez accéder aux actifs distants avec une URL complète.

Les meilleurs exemples d'actifs distants incluent des images provenant d'Unsplash, Pixabay et Pexels qui peuvent être utilisées directement dans votre fichier MDX.

```markdown
![Natural](https://images.unsplash.com/photo-1728044849236-5e8a061e1895)
```

Vous pouvez utiliser des actifs distants et locaux en fonction de vos exigences – les deux ont des avantages et des inconvénients. Avec les actifs distants, vous pouvez ajouter une image directement dans votre fichier mdx. Lorsque vous utilisez des actifs locaux, vous ajoutez une image au dossier public, puis vous la référencez dans votre fichier mdx.

## Comment publier votre site web de documentation

Avec docs.page, vous pouvez facilement publier votre site web de documentation. Aucune configuration n'est requise – une fois que votre site web de documentation est prêt, vous pouvez simplement pousser votre code local vers un dépôt GitHub.

Vous pouvez maintenant accéder à votre site web de documentation immédiatement via le domaine docs.page.

Par exemple, si votre dépôt GitHub est officialrajdeepsingh/docs-page-demo, votre documentation sera disponible à l'adresse [https://docs.page/officialrajdeepsingh/docs-page-demo](https://docs.page/officialrajdeepsingh/docs-page-demo).

![publiez votre site web de documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1745849817613/c1b7b095-121d-4b64-bd7b-a834ca87f8b5.png align="center")

## Comment prévisualiser en direct les prochaines modifications de votre site web de documentation

Vous pouvez visualiser les prévisualisations des prochaines modifications de votre documentation avant de les rendre publiques. À mesure que votre site web de documentation grandit, utilisez l'application [docs.page Github](https://github.com/apps/docs-page) – toute pull request que vous créez dans votre dépôt Github génère automatiquement une URL de prévisualisation en direct unique.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746278906018/0a299083-ff0a-4aea-a94e-95f94741e9af.png align="center")

Pour configurer la page docs de l'application GitHub dans votre dépôt, suivez ces étapes :

1. Allez sur [https://github.com/apps/docs-page](https://github.com/apps/docs-page)
    
2. Cliquez sur le bouton d'installation.
    
3. Sélectionnez le compte GitHub
    
4. Sélectionnez Tout et un seul dépôt.
    
5. Cliquez sur le bouton d'installation
    
6. Ensuite, entrez le mot de passe et l'OTP.
    
7. Maintenant, si votre application est réussie, installez-la dans votre dépôt.
    

![Crée des prévisualisations en direct dans votre dépôt github](https://cdn.hashnode.com/res/hashnode/image/upload/v1746280111575/06d449cd-917a-4908-8d5e-db90cffd3c0f.gif align="center")

Chaque fois que vous ou un autre développeur créez une pull request dans votre dépôt, l'application docs page crée des prévisualisations en direct pour vous.

## **Conclusion**

docs.page est un projet gratuit et open-source qui vous permet de créer une documentation instantanée, rapide et belle sans nécessiter de configuration.

Je pense que docs.page offre la meilleure solution pour la documentation. Vous pouvez facilement configurer et déployer votre site web de documentation avec l'aide du service cloud docs.page.

Pour l'instant, il est complètement gratuit de déployer un site web de documentation avec [docs.page](http://docs.page), et j'espère qu'il en restera ainsi.

Si [docs.page](http://docs.page) décide un jour de facturer leurs services, cela pourrait être problématique. Espérons que, dans ce cas, ils fourniront un guide clair sur la façon de déployer votre site web sur une autre plateforme cloud.