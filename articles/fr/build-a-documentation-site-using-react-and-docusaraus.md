---
title: Comment créer un site de documentation avec React et Docusaurus
subtitle: ''
author: Chisom Uma
co_authors: []
series: null
date: '2024-10-09T16:56:14.844Z'
originalURL: https://freecodecamp.org/news/build-a-documentation-site-using-react-and-docusaraus
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728407506914/49f6f7cd-af92-405e-ac89-d71bd74e3f18.avif
tags:
- name: docusaurus
  slug: docusaurus
- name: documentation
  slug: documentation
- name: 'Technical writing '
  slug: technical-writing-1
- name: React
  slug: reactjs
seo_title: Comment créer un site de documentation avec React et Docusaurus
seo_desc: Having a properly designed and comprehensive documentation site is important
  for any project. But creating good documentation can be challenging, and problems
  like poor user onboarding experience and increased support tickets can become daily
  hassles...
---

Avoir un site de documentation bien conçu et complet est important pour tout projet. Mais créer une bonne documentation peut être difficile, et des problèmes comme une mauvaise expérience d'intégration des utilisateurs et une augmentation des tickets de support peuvent devenir des tracas quotidiens pour une équipe.

C'est pourquoi des outils de documentation comme Docusaurus sont excellents pour vous aider à créer des sites de documentation visuellement époustouflants en environ 5 minutes.

Dans ce tutoriel, je vais vous montrer comment créer un site de documentation en utilisant React et Docusaurus.

Si vous êtes nouveau dans Docusaurus, vous vous demandez probablement, "pourquoi React ?, pourquoi pas un autre framework comme Next.js ?", Ne vous inquiétez pas - je vais également répondre à cette question dans ce guide.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que Docusaurus ?](#heading-questce-que-docusaurus)
    
* [Prise en main et installation](#heading-prise-en-main-et-installation)
    
    * [Structure du projet](#heading-structure-du-projet)
        
* [Comment démarrer votre site Docusaurus](#heading-comment-demarrer-votre-site-docusaurus)
    
* [Comment créer une documentation (Aperçu)](#heading-comment-creer-une-documentation-apercu)
    
* [MDX et composants React](#heading-mdx-et-composants-react)
    
    * [Onglets](#heading-onglets)
        
    * [Alertes ou avertissements](#heading-alertes-ou-avertissements)
        
    * [Blocs de code](#heading-blocs-de-code)
        
* [Blog Docusaurus](#heading-blog-docusaurus)
    
* [Pages personnalisées](#heading-pages-personnalisees)
    
* [Style dans Docusaurus](#heading-style-dans-docusaurus)
    
* [Déploiement](#heading-deploiement)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre ce guide, vous devez avoir :

* **Node.js** version 18.0 ou supérieure installée
    
* Connaissance de base de React et Markdown
    
* IDE (de préférence VSCode)
    

## Qu'est-ce que Docusaurus ?

[Docusaurus](https://docusaurus.io/) a été publié par l'équipe Meta Open Source en 2017 pour aider les développeurs à créer, déployer et maintenir des sites web de documentation facilement et rapidement. L'autre objectif du projet était d'améliorer la vitesse des développeurs et des utilisateurs finaux en utilisant le modèle [PRPL](https://web.dev/articles/apply-instant-loading-with-prpl).

Certaines de ses fonctionnalités intéressantes incluent la recherche et la localisation, alimentées par [Algolia](https://www.algolia.com/) (recherche) et [Crowdin](https://crowdin.com/) (support linguistique et internationalisation).

Maintenant, parlons de pourquoi nous utilisons React pour ce tutoriel. Eh bien, Docusaurus est construit sur React, ce qui le rend facile à personnaliser. De plus, Docusaurus supporte Markdown et MDX (qui vous permet d'utiliser React JSX dans votre contenu Markdown).

En tant que rédacteur technique, j'aime que cet outil supporte Markdown, avec lequel je suis assez familier. Il me permet de me concentrer sur la création de documentation utile sans m'inquiéter de convertir le texte dans d'autres formats de texte.

## Prise en main et installation

Commencer avec Docusaurus est assez simple. La première chose à faire est de vous rendre dans votre terminal et d'exécuter la commande suivante :

```plaintext
npx create-docusaurus@latest my-website classic
```

**Note :** L'équipe Docusaurus recommande le modèle `classic` car il est plus facile de commencer rapidement. Il contient également `@docusaurus/preset-classic` - qui inclut une documentation standard, un blog, des pages personnalisées et un framework CSS (avec support du mode sombre).

### Structure du projet

Après l'installation, voici à quoi devrait ressembler la structure de votre nouveau projet Docusaurus :

```plaintext
📦my-website
├── 📁blog
│   ├── 📁2021-08-26-welcome
│   │   ├── 📄docusaurus-plushie-banner.jpeg
│   │   └── 📄index.md
│   ├── 📄2019-05-28-first-blog-post.md
│   ├── 📄2019-05-29-long-blog-post.md
│   ├── 📄2021-08-01-mdx-blog-post.mdx
│   ├── 📄authors.yml
│   └── 📄tags.yml
├── 📁docs
│   ├── 📁tutorial-basics
│   │   ├── 📄congratulations.md
│   │   ├── 📄create-a-blog-post.md
│   │   ├── 📄create-a-document.md
│   │   ├── 📄create-a-page.md
│   │   ├── 📄deploy-your-site.md
│   │   ├── 📄markdown-features.mdx
│   │   └── 📄_category_.json
│   ├── 📁tutorial-extras
│   │   ├── 📁img
│   │   │   ├── 📄docsVersionDropdown.png
│   │   │   └── 📄localeDropdown.png
│   │   ├── 📄manage-docs-versions.md
│   │   ├── 📄translate-your-site.md
│   │   └── 📄_category_.json
│   └── 📄intro.md
├── 📁src
│   ├── 📁components
│   │   └── 📁HomepageFeatures
│   │       ├── 📄index.js
│   │       └── 📄styles.module.css
│   ├── 📁css
│   │   └── 📄custom.css
│   └── 📁pages
│       ├── 📄index.js
│       ├── 📄index.module.css
│       └── 📄markdown-page.md
├── 📁static
│   ├── 📁img
│   │   ├── 📄docusaurus-social-card.jpg
│   │   ├── 📄docusaurus.png
│   │   ├── 📄favicon.ico
│   │   ├── 📄logo.svg
│   │   ├── 📄undraw_docusaurus_mountain.svg
│   │   ├── 📄undraw_docusaurus_react.svg
│   │   └── 📄undraw_docusaurus_tree.svg
│   └── 📄.nojekyll
├── 📄.gitignore
├── 📄babel.config.js
├── 📄docusaurus.config.js
├── 📄package.json
├── 📄README.md
└── 📄sidebars.js
```

Maintenant, explorons certains des principaux répertoires :

* `blog/` : C'est là que vous stockez vos articles de blog
    
* `docs/` : Comme son nom l'indique, c'est là que vos projets de documentation sont conservés
    
* `src/` : Ce répertoire vous permet de personnaliser davantage votre site web en utilisant du code React.
    
* `static` : Ici, vous stockez des fichiers statiques comme des images, des logos, des favicons, etc.
    

Un fichier très important est le fichier `docusaurus.config.js`, qui agit comme le fichier de configuration principal de votre site web.

## Comment démarrer votre site Docusaurus

Pour exécuter votre site web localement, ouvrez d'abord un nouveau terminal dans votre IDE et exécutez la commande suivante pour démarrer le serveur de développement :

```plaintext
cd my-website

npm i

npx docusaurus start
```

Après avoir exécuté la commande ci-dessus, le navigateur compile les fichiers React et Markdown et démarre un serveur de développement local à l'adresse [http://localhost:3000/](http://localhost:3000/). Docusaurus active le rechargement à chaud, vous pouvez donc voir les modifications apportées à vos fichiers React, Markdown et MDX automatiquement - sans recharger toute votre application.

Voici à quoi ressemble le site sur votre navigateur :

![Site Docusaurus initialisé](https://cdn.hashnode.com/res/hashnode/image/upload/v1728389930307/b0bd7810-dea2-458b-85a1-e10b9a7b3028.png align="center")

Dans l'image ci-dessus, vous êtes d'abord accueilli sur un site web intuitif et facilement navigable. Dans le coin supérieur gauche du site web, vous verrez les sections "**Tutoriel**" et "**Blog**".

* **Tutoriel** : C'est là que les utilisateurs peuvent voir la version live de votre documentation.
    
* **Blog** : C'est là que les utilisateurs peuvent voir la version live de votre blog.
    

Le lien vers le dépôt GitHub Open Source de Docusaurus et l'icône pour basculer votre site web entre les modes clair et sombre se trouvent dans le coin supérieur droit du site.

Alternativement, vous pouvez utiliser [docusaurus.new](https://docusaurus.io/docs/playground) pour tester Docusaurus rapidement dans un bac à sable sans avoir à passer par le processus d'installation. Ici, vous avez la possibilité de choisir entre [CodeSandbox](https://codesandbox.io/) et [StackBlitz](https://stackblitz.com/).

## Comment créer une documentation (Aperçu)

Examinons de plus près notre dossier `docs`. Si nous retournons à notre site local et cliquons sur "**Tutoriel**", nous verrons quelques pages de documentation pré-construites, comme montré ci-dessous :

![Aperçu de la documentation sur le site](https://cdn.hashnode.com/res/hashnode/image/upload/v1728390116953/ec281a01-5b0c-413a-83b9-36d0352f3e03.png align="center")

Ces pages de documentation sont reflétées dans le dossier `docs` situé dans votre IDE. Lorsque nous ouvrons la page `category.json`, nous pouvons ajuster le nom ou la position de chaque page. Cela signifie que vous n'avez pas à nommer les dossiers de la même manière que le nom de la page, puisque le nom du fichier sera l'URL de la page.

Pour créer notre nouvelle documentation, utilisons les étapes suivantes :

1. Supprimez tous les fichiers dans le dossier docs. Votre navigateur et terminal afficheront généralement une erreur après cela.
    
    ![Erreur due aux fichiers supprimés](https://cdn.hashnode.com/res/hashnode/image/upload/v1728390294195/5a59bdc4-7a79-4b17-9e85-630867c6c3ec.png align="center")
    
    Cela est dû au fait que nous avons besoin d'au moins une page dans le dossier docs.
    
2. Créez un nouveau fichier dans le dossier docs, que vous pouvez nommer comme vous le souhaitez, mais dans notre cas, je l'ai nommé [single-page.md](http://single-page.md). Vous devriez voir ce changement immédiatement reflété lorsque vous allez sur votre site web local. Voici ce que vous verrez dans la section des pages de documentation :
    
    ![Page unique](https://cdn.hashnode.com/res/hashnode/image/upload/v1728390512797/90b86f29-8b03-414b-acff-18842cd4c462.png align="center")
    

À l'intérieur de ce fichier nouvellement créé, vous pouvez créer votre documentation de manière transparente. L'image ci-dessus montre le petit contenu Markdown que j'ai créé disant "Single Page" en H1 et "This is a single page" en texte brut.

Disons que vous souhaitez créer une structure de contenu plus organisée, mais que vous ne savez pas comment commencer. Voici quelques étapes simples sur la façon de le faire :

1. Créez un nouveau dossier à l'intérieur du dossier `docs`, nommé "Getting Started"
    
2. Créez de nouveaux fichiers Markdown à l'intérieur du dossier "Getting started", et nommez-les comme vous le souhaitez. Pour les besoins de ce tutoriel, nommons-le [`API-docs.md`](http://API-docs.md) et [`Session-replay.md`](http://Session-replay.md).
    
3. Écrivez votre documentation en Markdown
    

Voici à quoi devrait ressembler la structure des fichiers sur votre IDE :

```plaintext
📦docs
├── 📁Getting started
│   ├── 📄Open-replay.md
│   └── 📄Session-replay.md
└── 📄single-page.md
```

Voici un simple GIF pour démontrer comment cela fonctionne sur le site de documentation local.

![GIF montrant le site de documentation local](https://cdn.hashnode.com/res/hashnode/image/upload/v1728390784981/9eed8cbf-c6dc-4508-9d75-401d87673cf7.gif align="center")

Maintenant, essayons de créer une page séparée dans le dossier `doc`. Pour ce faire, créons une page `category.json` dans le dossier `Getting started`. À l'intérieur du fichier `category.json`, nous inclurons le texte JSON suivant :

```json
{
  "label": "Titre personnalisé",
  "position": 2,
  "link": {
    "type": "generated-index",
    "description": "Ceci est une description personnalisée"
  }
}
```

* L'objet `link` crée une page séparée pour le dossier.
    
* La propriété `type` est définie sur generated-index, ce qui signifie qu'elle générera les pages avec toutes les sous-pages.
    
* La propriété `description` est une description de la page qui apparaîtra sous le titre.
    

Lorsque vous consultez votre site de documentation hébergé localement, vous verrez que le libellé a changé et qu'une page séparée a été créée pour le dossier.

Dans cette section, je vais vous montrer un exemple de comment les titres et les tables des matières fonctionnent dans Docusaurus.

La première chose que j'ai faite a été de créer un fichier [`markdown.md`](http://markdown.md). Ensuite, j'ai collé quelques titres au format texte Markdown directement dans le fichier, comme ceci :

```markdown
---
title: Markdown de base
sidebar_position: 1
---

# Titre 1

## Titre 2

### Titre 3

#### Titre 4

##### Titre 5

###### Titre 6
```

Lorsque nous retournons à notre site web, nous pouvons voir que seuls les titres de niveau 2 et 3 sont automatiquement ajoutés, comme montré ci-dessous :

![Image montrant les en-têtes](https://cdn.hashnode.com/res/hashnode/image/upload/v1728391234366/1ba2a824-3d31-4fd2-bd3e-8fcb9547e073.png align="center")

Nous pouvons modifier pour nous assurer que tous les titres apparaissent. Pour ce faire, créez d'abord un fichier [`table-of-contents.md`](http://table-of-contents.md), puis collez le Markdown suivant :

```markdown
---
title: Table des matières
sidebar_position: 2
toc_min_heading_level: 2
toc_max_heading_level: 6
---

import TOCInline from '@theme/TOCInline';

<TOCInline toc={toc} minHeadingLevel={2} maxHeadingLevel={6} />

## Titre 2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.

### Titre 3

Du contenu ici.

#### Titre 4

Du contenu ici.

##### Titre 5

Du contenu ici.

###### Titre 6

Du contenu ici.

## Titre 2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.

### Titre 3

Du contenu ici.

#### Titre 4

Du contenu ici.

##### Titre 5

Du contenu ici.

###### Titre 6

Du contenu ici.

## Titre 2

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.

### Titre 3

Du contenu ici.

#### Titre 4

Du contenu ici.

##### Titre 5

Du contenu ici.

###### Titre 6

Du contenu ici.
```

J'ai ajouté une propriété TOC et défini les niveaux de titre minimum et maximum avec `toc_min_heading_level: 2` et `toc_max_heading_level: 6`. Nous avons également ajouté une table des matières en ligne en important d'abord `TOCInline` depuis `@theme/TOCInline`. Ensuite, nous avons créé un composant TOCInline (qui peut être placé n'importe où vous voulez que votre TOC apparaisse).

Maintenant, tous les titres apparaissent dans la partie table des matières du site web :

![Image montrant la table des matières et les en-têtes](https://cdn.hashnode.com/res/hashnode/image/upload/v1728398728652/37595594-3dbc-42bc-853c-f5b5ba9714c4.png align="center")

Magnifique, n'est-ce pas ?

## MDX et composants React

Maintenant, parlons de l'une des fonctionnalités les plus passionnantes de Docusaurus : MDX et les composants React.

Vous pourriez demander - comment Docusaurus peut-il utiliser `TOC` ou `import` dans le fichier Markdown ? Eh bien, c'est parce que Docusaurus utilise MDX, qui est essentiellement Markdown avec JSX.

Pour démontrer cela, créons un nouveau fichier Markdown à l'intérieur de notre dossier `Getting started` intitulé [`MDX.md`](http://MDX.md), puis créons un fichier séparé à l'intérieur du dossier `src` > `components` et nommons le fichier `Tag.js`. Ensuite, nous collons le code suivant :

```javascript
import React from 'react';

export default function Tag({ children, color }) {
  return (
    <span
      style={{
        backgroundColor: color,
        borderRadius: '4px',
        color: '#fff',
        padding: '0.2rem 0.5rem',
        fontWeight: 'bold',
      }}
    >
      {children}
    </span>
  );
}
```

Ici, nous avons d'abord importé la bibliothèque principale React, puis nous avons défini un composant fonctionnel appelé Tag, qui prend deux props en entrée : `children` et `color`. Dans notre instruction return, nous avons inclus nos styles CSS pour l'élément `span`.

À l'intérieur du fichier [MDX.md](http://MDX.md), collez le code ci-dessous :

```markdown
---
title: MDX
sidebar_position: 3
---

import Tag from '@site/src/components/Tag';

<Tag color="#FF5733">Important</Tag> information: This is an <Tag color="#3399FF">Exciting</Tag> example of custom components!

I can write **Markdown** alongside my _JSX_!
```

Ici, nous importons `Tag` depuis notre dossier de composants. Voici à quoi cela ressemble :

![Image montrant comment fonctionne MDX](https://cdn.hashnode.com/res/hashnode/image/upload/v1728398996580/a826b80c-1862-46f4-b111-dc6366dd13db.png align="center")

**Note :** Parce que nous utilisons MDX, Docusaurus vient avec des composants pré-construits comme les onglets, les alertes, les blocs de code, et plus encore. Vérifions-les dans les sous-sections suivantes.

### Onglets

Dans cette sous-section, nous allons parler des onglets en tant que composant pré-construit dans Docusaurus. Plongeons-nous directement !

Pour commencer, créons un nouveau fichier Markdown appelé [`tabs.md`](http://tabs.md) et collons le code suivant :

```markdown
---
title: Onglets dans Markdown
sidebar_position: 4
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="book" label="Livre" default>
    Plongez dans le monde du savoir avec un livre captivant 📚
  </TabItem>
  <TabItem value="painting" label="Peinture">
    Admirez les coups de pinceau artistiques sur une belle peinture 🎨
  </TabItem>
  <TabItem value="music" label="Musique">
    Laissez les mélodies apaisantes de la musique vous transporter 🎶
  </TabItem>
</Tabs>

Je suis un texte qui n'appartient à aucun onglet. Donc je suis toujours visible.
```

Nous avons importé `Tabs` depuis `@theme/Tabs` et `TabItem` depuis `@theme/TabItem`. Ensuite, nous avons créé un composant Tabs, qui est le conteneur, et le composant `TabItem` est l'onglet lui-même. La propriété `value` est la valeur de l'onglet, tandis que la propriété `label` est le libellé de l'onglet. La propriété default définit quel onglet est ouvert par défaut - dans ce cas, l'onglet "Livre".

Voici à quoi cela ressemble :

![Image montrant comment fonctionnent les onglets](https://cdn.hashnode.com/res/hashnode/image/upload/v1728399214390/edece46f-3357-4b96-8672-a462a8a8916b.png align="center")

Chaque onglet est cliquable et la transition est fluide.

### Alertes ou avertissements

Docusaurus vient avec des alertes ou avertissements pré-construits. Pour créer une alerte, vous enveloppez simplement le texte avec trois deux-points et vous le suivez avec le type d'alerte que vous voulez que le lecteur ait à l'esprit.

Créons un nouveau fichier Markdown appelé [alerts.md](http://alerts.md) et collons le Markdown suivant :

```markdown
---
title: Alertes ou avertissements
sidebar_position: 5
---

:::note

Voici quelques **informations** avec un style _Markdown_.

:::

:::tip

Voici un **conseil utile** avec du texte _formaté_.

:::

:::info

Voici quelques **informations utiles** présentées de manière claire.

:::

:::caution

Veuillez faire **attention** avec cette note importante.

:::

:::danger

Ceci est une **situation dangereuse** dont vous devez être conscient.

:::

:::note Ceci est un _titre personnalisé_

Et vous pouvez également ajouter des images.

![texte alternatif](https://picsum.photos/600/400)

:::
```

Les différents types d'alertes, comme montré dans le Markdown ci-dessus, sont :

* `note`
    
* `tip`
    
* `info`
    
* `caution`
    
* `danger`
    

Voici à quoi cela ressemble sur le site web :

![Image montrant comment fonctionnent les alertes et avertissements](https://cdn.hashnode.com/res/hashnode/image/upload/v1728402667575/cc10af2d-e417-4426-985b-4aad81a082db.png align="center")

Les alertes et avertissements sont assez courants dans les sites de documentation. Donc, si vous vous êtes déjà demandé comment cela a été fait, eh bien, c'est ça ! C'est assez simple.

### Blocs de code

Comme nous le savons déjà, Docusaurus supporte MDX, ce qui nous permet d'inclure des blocs de code dans nos fichiers. Les blocs de code sont des blocs de texte entourés de chaînes de trois backticks. Vous pouvez ajouter le nom du langage après le dernier des trois backticks.

Créons un fichier [`codeblocks.md`](http://codeblocks.md) et collons le code JSX suivant :

````javascript
---
title: Blocs de code
sidebar_position: 6
---

```jsx title="Bloc de code"
function Greeting(props) {
  return <p>Bienvenue, {props.userName} !</p>;
}

export default Greeting;
```

```jsx title="Mettre en surbrillance les lignes"
function HighlightText(highlight) {
  if (highlight) {
    // highlight-next-line
    return 'Ce texte est mis en surbrillance !';
  }
  return 'Rien en surbrillance';
}

function HighlightMoreText(highlight) {
  // highlight-start
  if (highlight) {
    return 'Cette plage est mise en surbrillance !';
  }
  // highlight-end
  return 'Rien en surbrillance';
}
```

```jsx title="Numéros de ligne" showLineNumbers
import React from 'react';

function UserProfile(props) {
  const { username, email, isAdmin } = props;

  return (
    <div>
      <h1>Profil de l'utilisateur</h1>
      <p>Nom d'utilisateur : {username}</p>
      <p>Email : {email}</p>
      {isAdmin && <p>Utilisateur administrateur</p>}
    </div>
  );
}

export default UserProfile;
```

```jsx title="Numéros de ligne avec surbrillance" {4,9-11} showLineNumbers
import React from 'react';

function UserProfile(props) {
  const { username, email, isAdmin } = props;

  return (
    <div>
      <h1>Profil de l'utilisateur</h1>
      <p>Nom d'utilisateur : {username}</p>
      <p>Email : {email}</p>
      {isAdmin && <p>Utilisateur administrateur</p>}
    </div>
  );
}

export default UserProfile;
````

Voici à quoi ressemblent les blocs de code :

![Image montrant comment fonctionnent les blocs de code](https://cdn.hashnode.com/res/hashnode/image/upload/v1728402852316/4873fccd-d4b7-45d7-8d4f-49fea5a3da49.png align="center")

Vous pouvez facilement copier le code en survolant votre curseur sur les blocs de code et en cliquant sur l'icône de copie en haut à droite du bloc de code.

**Note :** Par défaut, Docusaurus utilise `Prism` pour la coloration syntaxique.

Si vous souhaitez également mettre en surbrillance certaines lignes de code, vous pouvez le faire en ajoutant un commentaire comme ceci :

```javascript
    // highlight-next-line
    return 'Ce texte est mis en surbrillance !';
  }
  return 'Rien en surbrillance';
}

function HighlightMoreText(highlight) {
  // highlight-start
  if (highlight) {
    return 'Cette plage est mise en surbrillance !';
  }
  // highlight-end
```

* `highlight-next-line` : vous permet de mettre en surbrillance une seule ligne de code
    
* `highlight-start et highlight-end` : vous permet de mettre en surbrillance une plage de lignes
    

## Blog Docusaurus

Le blog Docusaurus est également inclus par défaut avec le modèle `classic`. Si vous n'avez pas de blog, vous pouvez ajouter les lignes suivantes à votre fichier `docusaurus.config.js` :

```javascript
{
  label: 'Blog',
  to: '/blog',
}
```

Généralement, cette ligne devrait déjà être dans votre fichier de configuration après avoir installé Docusaurus pour la première fois.

Le blog Docusaurus est très simple à comprendre. Accédez au dossier blog dans l'explorateur de projet, et vous verrez tous les articles de blog, qui sont des fichiers MDX. La date de l'article de blog doit être incluse dans le nom du fichier comme montré ci-dessous :

![Image montrant le dossier blog](https://cdn.hashnode.com/res/hashnode/image/upload/v1728403567052/c60d665d-f29b-433e-bd10-b86542d0063e.png align="center")

Lorsque vous ouvrez l'un des articles de blog, vous voyez quelque chose comme ceci :

```markdown
---
slug: long-blog-post
title: Long Blog Post
authors: yangshun
tags: [hello, docusaurus]
---

This is the summary of a very long blog post,

Use a `<!--` `truncate` `-->` comment to limit blog post size in the list view.

<!-- truncate -->

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque elementum dignissim ultricies. Fusce rhoncus ipsum tempor eros aliquam consequat. Lorem ipsum dolor sit amet
```

* `slug` : Vous pouvez ajouter un slug à l'URL de l'article de blog
    
* `title` : Titre de l'article de blog
    
* `authors` : Les auteurs de l'article de blog
    
* `tags` : Tags liés à l'article de blog
    

Dans l'article de blog, nous pouvons également utiliser toutes les fonctionnalités Markdown plus JSX comme nous l'avons vu précédemment.

## Pages personnalisées

Techniquement, Docusaurus n'est pas seulement un générateur de site de documentation sophistiqué avec un blog. C'est un générateur de site statique standard - ce qui signifie que vous pouvez créer n'importe quelle page que vous voulez.

Pour voir comment la création d'une page personnalisée dans Docusaurus fonctionne, créons un fichier about.js dans le dossier `src` **>** `pages` et incluons le code suivant :

```javascript
import React from 'react';
import Layout from '@theme/Layout';
import Head from '@docusaurus/Head';

export default function About() {
  return (
    <Layout>
      <Head>
        <title>À propos</title>
        <meta name="description" content="Ceci est la page à propos" />
      </Head>

      <div>
        <h1 className="red-text">À propos</h1>
        <p>Ceci est la page à propos.</p>
      </div>
    </Layout>
  );
}
```

Lorsque vous allez sur [http://localhost:3000/about](http://localhost:3000/about), vous devriez voir quelque chose comme ceci :

![Image montrant comment fonctionnent les pages personnalisées](https://cdn.hashnode.com/res/hashnode/image/upload/v1728404291897/394ee43b-2b30-43f8-a8cf-ff260d51e82a.png align="center")

Nous pouvons également ajouter la page à la barre de navigation en allant dans le fichier docusaurus.config.js et en ajoutant un nouvel élément au tableau de la barre de navigation. L'élément ressemble à ceci :

```json
{to: 'about', label: 'À propos', position: 'left'},
```

Il apparaît alors dans le menu de navigation de la page d'accueil comme ceci :

![Image montrant comment fonctionnent les pages personnalisées](https://cdn.hashnode.com/res/hashnode/image/upload/v1728404457186/25545cf0-a5bf-4561-8dc8-49045c3cfc9d.png align="center")

Vous pouvez maintenant styliser et personnaliser le fichier `about.js` de la manière que vous préférez en utilisant React.

## Style dans Docusaurus

Examinons comment vous pouvez styliser votre site dans Docusaurus. Le moyen le plus simple est de personnaliser le fichier `custom.css` à l'intérieur du fichier `css` **>** `custom.css`. Voici à quoi ressemble le fichier :

![Image montrant comment effectuer le style](https://cdn.hashnode.com/res/hashnode/image/upload/v1728404914713/bd2c8b65-52f9-43d4-b0c8-d09ec9562865.png align="center")

Ici, vous pouvez changer le schéma de couleur entier du site et différents styles dans ce fichier.

Vous pouvez **en lire plus** dans la documentation [Docusaurus styling and layout](https://docusaurus.io/docs/styling-layout).

## SEO dans Docusaurus

Docusaurus prend le SEO très au sérieux. Par défaut, Docusaurus ajoute automatiquement une description de titre, des liens d'URL canoniques et d'autres métadonnées utiles à chaque page. Cela peut être configuré comme montré ci-dessous :

```markdown
---
title: Notre première page
sidebar_position: 1

description: Une courte description de cette page
image: ../static/img/docusaurus-social-card.jpg
keywords: [mots-clés, décrivant, les principaux sujets]
---

# Page unique

Ceci est une page unique.
```

Vous pouvez **en lire plus** dans la documentation [Docusaurus SEO](https://docusaurus.io/docs/seo).

## Déploiement

Le déploiement est assez facile avec Docusaurus. Puisqu'il s'agit d'un site statique, vous pouvez le déployer sur n'importe quel service d'hébergement de site statique. Pour ce faire, exécutez la commande `npm run build` sur votre CLI. Cela crée un dossier build comme celui ci-dessous :

![Image montrant le dossier build pour le déploiement](https://cdn.hashnode.com/res/hashnode/image/upload/v1728405905725/a7633e46-cb10-4220-bce8-7b12545a124f.png align="center")

Ensuite, vous pouvez télécharger le contenu du dossier build sur votre service d'hébergement.

## Conclusion

Dans cet article, nous avons couvert comment créer une documentation à partir de zéro, comment créer, personnaliser et styliser des pages, et le pouvoir SEO impressionnant de Docusaurus.

Docusaurus est convivial pour les développeurs et les rédacteurs techniques. En tant que développeur, vous pouvez vous concentrer sur la personnalisation du site, tandis qu'en tant que rédacteur technique, vous pouvez vous concentrer sur la rédaction de la documentation.

Je recommande vivement cet outil pour les startups et les entreprises établies cherchant à créer des sites de documentation époustouflants.

Ce guide n'est pas exhaustif, mais couvre tout ce que vous devez savoir sur les bases de la création d'un site de documentation avec React et Docusaurus.

J'espère que vous l'avez trouvé utile :)

Voici le lien vers mon [code GitHub](https://github.com/ChisomUma/docusaurus-project) pour des suivis.

Et voici la documentation principale de Docusaurus [documentation](https://docusaurus.io/docs/docs-introduction) si vous souhaitez approfondir.