---
title: Créez votre portfolio de développeur et votre blog de toutes pièces avec Svelte
  et GraphCMS – Un guide complet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-06T16:12:00.000Z'
originalURL: https://freecodecamp.org/news/build-your-developer-portfolio-from-scratch-with-sveltekit-and-graphcms
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/simon-abrams-k_T9Zj3SE8k-unsplash.jpg
tags:
- name: GitHub
  slug: github
- name: graphcms
  slug: graphcms
- name: portfolio
  slug: portfolio
- name: projects
  slug: projects
- name: Svelte
  slug: svelte
- name: Web Development
  slug: web-development
seo_title: Créez votre portfolio de développeur et votre blog de toutes pièces avec
  Svelte et GraphCMS – Un guide complet
seo_desc: "By Scott Spence\nA developer portfolio is a great way to showcase your\
  \ current skill level to potential employers. \nThis guide will go from hello world\
  \ to a fully-featured portfolio project to show your current projects with images\
  \ and links to source..."
---

Par Scott Spence

Un portfolio de développeur est un excellent moyen de présenter votre niveau de compétence actuel à des employeurs potentiels.

Ce guide ira du « hello world » à un projet de portfolio complet pour afficher vos projets actuels avec des images et des liens vers le code source. Vous construirez également un blog d'accompagnement où vous pourrez détailler ce que vous avez appris en cours de route.

Salut 👋, je m'appelle [Scott](https://scottspence.com), et je blogue sur mon parcours dans le développement web depuis juillet 2016.

Je suis un ancien élève de freeCodeCamp – j'ai commencé mon parcours freeCodeCamp en 2016 – et je suis développeur professionnel depuis mars 2018.

J'ai déjà écrit sur [la façon de construire un blog Gatsby de toutes pièces par le passé](https://www.freecodecamp.org/news/build-a-developer-blog-from-scratch-with-gatsby-and-mdx/) et je veux vous accompagner pour refaire la même chose, cette fois avec Svelte !

C'est un guide assez complet (33 sections !), j'ai donc ajouté une table des matières pour vous aider à naviguer dans l'article :

* [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
* [À qui s'adresse ce guide ?](#heading-a-qui-sadresse-ce-guide)
* [La stack (quelle technologie nous utiliserons)](#heading-la-stack-quelle-technologie-nous-utiliserons)
* [Qu'est-ce que Svelte ?](#heading-questce-que-svelte)
* [Qu'est-ce que SvelteKit ?](#heading-questce-que-sveltekit)
* [Qu'est-ce que Vite ?](#heading-questce-que-vite)
* [Qu'est-ce que GraphQL ?](#heading-questce-que-graphql)
* [Qu'est-ce que GraphCMS ?](#heading-questce-que-graphcms)
* [Comment configurer GraphCMS](#heading-comment-configurer-graphcms)
* [Comment requêter du contenu](#heading-comment-requeter-du-contenu)
* [Comment créer votre projet Svelte](#heading-comment-creer-votre-projet-svelte)
* [Comment afficher les données GraphQL sur la page d'accueil](#heading-comment-afficher-les-donnees-graphql-sur-la-page-daccueil)
* [Comment ajouter le balisage pour la page d'accueil](#heading-comment-ajouter-le-balisage-pour-la-page-daccueil)
* [Comment construire le premier composant Svelte](#heading-comment-construire-le-premier-composant-svelte)
* [Comment styliser dans Svelte](#heading-comment-styliser-dans-svelte)
* [Comment styliser avec Tailwind et daisyUI](#heading-comment-styliser-avec-tailwind-et-daisyui)
* [Comment styliser le composant Projets](#heading-comment-styliser-le-composant-projets)
* [Comment utiliser le fichier `__layout` de SvelteKit](#heading-comment-utiliser-le-fichier-layout-de-sveltekit)
* [Comment construire la page de destination avec la liste des projets](#heading-comment-construire-la-page-de-destination-avec-la-liste-des-projets)
* [Comment utiliser le routage SvelteKit](#heading-comment-utiliser-le-routage-sveltekit)
* [Comment construire le blog](#heading-comment-construire-le-blog)
* [Comment construire les composants Navbar et Footer](#heading-comment-construire-les-composants-navbar-et-footer)
* [Comment ajouter un sélecteur de thème](#heading-comment-ajouter-un-selecteur-de-theme)
* [Comment ajouter la page À propos](#heading-comment-ajouter-la-page-a-propos)
* [Comment créer un sitemap](#heading-comment-creer-un-sitemap)
* [Robots.txt](#heading-robotstxt)
* [Génération de flux RSS](#heading-generation-de-flux-rss)
* [Inscription par e-mail avec Revue](#heading-inscription-par-email-avec-revue)
* [Déploiement continu avec Vercel](#heading-deploiement-continu-avec-vercel)
* [Google Search Console](#heading-google-search-console)
* [Ressources](#heading-ressources)
* [Ce que nous avons accompli](#heading-ce-que-nous-avons-accompli)

## **Ce que nous allons construire**

Nous allons construire un portfolio et un blog complets avec le Framework qui a pris la première place des frameworks les plus appréciés dans l'enquête des développeurs Stack Overflow en 2021 – Svelte.

Utiliser Svelte avec GraphCMS signifie que vous pouvez contrôler l'ajout et la suppression de contenu sur votre site sans avoir besoin de pousser des modifications sur Git.

Fonctionnalités :

* Page de destination avec liste de projets
* Blog
* Sélecteur de thème
* Sitemap
* Génération de flux RSS
* Robots.txt
* Déploiement continu avec Vercel
* Intégrations de build pour publier et construire le site lors des changements de contenu

Il y a aussi une section facultative d'inscription par e-mail avec des ressources mentionnées, mais ce n'est pas essentiel pour le projet que nous allons commencer. Vous trouverez des ressources pour cela vers la fin.

Une chose qui n'est généralement pas couverte par des guides comme celui-ci est le déploiement réel et l'indexation de votre site sur les moteurs de recherche comme Google. Mais ici, je vais passer en revue tout le processus pour que vous puissiez avoir quelque chose dont vous serez fier à la fin.

Si vous voulez aller plus loin avec l'analytique, consultez mon guide sur la configuration d'un projet Svelte avec Fathom Analytics, le fournisseur d'analytique respectueux de la vie privée. Mais je ne l'ai pas inclus ici, car c'est une fonctionnalité payante et hors du cadre gratuit.

### **Prérequis**

Ce guide suppose quelques connaissances de la part du lecteur :

* Une compréhension du HTML, du CSS et du JavaScript (la sainte trinité du développement web)
* Un compte GitHub ou similaire (GitLab ou Bitbucket). Ce n'est pas indispensable mais certains services d'hébergement exigent que vous connectiez un dépôt Git.
* Un environnement de développement, Node.js installé sur votre machine (version 14+), un terminal et un éditeur de texte comme VS Code.
* Il existe des options par navigateur comme [GitHub codespaces](https://github.com/features/codespaces) ou [Gitpod](https://www.gitpod.io/) si vous n'avez pas ces éléments configurés.

Si vous n'avez pas d'environnement de développement configuré, ne vous inquiétez pas – vous pouvez utiliser Gitpod pour lancer un environnement avec ce lien : [http://gitpod.io/#https://github.com/spences10/sveltekit-skeleton](http://gitpod.io/#https://github.com/spences10/sveltekit-skeleton)

Cela vous permettra de démarrer avec le squelette SvelteKit qui est créé lorsque vous utilisez le CLI pour créer un nouveau projet SvelteKit.

J'utiliserai [Visual Studio Code](https://code.visualstudio.com/) (VS Code) de Microsoft ainsi que le client Git intégré à VS Code.

Il y aura un Git Commit à la fin de chaque section. C'est facultatif mais cela aide à prendre l'habitude de committer régulièrement. C'est également utile lorsque vous voudrez déployer le projet à la fin.

## **À qui s'adresse ce guide ?**

Si vous progressez bien dans le programme de freeCodeCamp et que vous voulez avoir quelque chose à montrer pour prouver votre niveau de compétence actuel, ce guide sera un excellent compagnon.

Ce guide vous donnera tout ce dont vous avez besoin pour commencer avec Svelte et vous donnera la confiance nécessaire pour commencer à créer vos propres projets avec.

## La stack (quelle technologie nous utiliserons)

Bien que j'aie mentionné une grande partie de la technologie que nous utiliserons, je profite de l'occasion pour lister ce que nous utiliserons tout au long de ce guide.

* SvelteKit – le Framework que nous utiliserons pour créer les pages et les composants
* Tailwind + daisyUI – comment nous styliserons le projet
* Tailwind CSS Typography pour s'occuper du style du contenu textuel
* Marked pour convertir le contenu Markdown en HTML
* GraphCMS – où nous stockerons le contenu pour les détails du projet et les articles de blog
* graphql-request – utilisé pour requêter les données de l'API GraphCMS

## **Qu'est-ce que Svelte ?**

Svelte est un framework de composants qui vous permet d'écrire des pages et des composants dans ce dont vous avez l'habitude – HTML, CSS et JavaScript. C'est un compilateur front-end open-source créé par [Rich Harris](https://twitter.com/Rich_Harris) et maintenu par les membres de l'équipe centrale de Svelte.

Notez qu'il s'agit d'un compilateur. Cela signifie que tout le HTML, le CSS et le JavaScript sont construits à l'avance en modules JavaScript autonomes, ce qui réduit la charge sur le client (le navigateur).

Il est compilé, plutôt que d'envoyer un moteur d'exécution JavaScript au navigateur comme React ou Vue. Cela produit un projet beaucoup plus léger expédié au navigateur.

## Qu'est-ce que SvelteKit ?

SvelteKit est un Framework qui a le langage Svelte en son cœur avec quelques fonctionnalités ajoutées. Celles-ci incluent le routage basé sur les fichiers, les endpoints et les layouts, pour n'en citer que quelques-unes.

Les endpoints dans SvelteKit sont des modules que vous pouvez écrire en JavaScript pour créer des méthodes HTTP (get, post, delete), qui peuvent être consultées dans SvelteKit via l'API fetch de SvelteKit. Plus d'informations à ce sujet plus tard.

## Qu'est-ce que Vite ?

Vite est l'outil de build que vous utilisez pour compiler les projets SvelteKit. Vite a été créé par Evan You, le créateur de Vue. Vite est agnostique vis-à-vis des frameworks et constitue un excellent ajout à la boîte à outils SvelteKit.

## **Qu'est-ce que GraphQL ?**

GraphQL est un langage de requête pour les API, offrant aux utilisateurs et aux clients la flexibilité de demander les données dont ils ont besoin quand ils en ont besoin.

Une requête GraphQL ressemble à ceci :

![Une requête GraphQL affichant la requête à gauche et les résultats à droite](https://www.freecodecamp.org/news/content/images/2021/12/image-1.png)
_Une requête GraphQL affichant la requête à gauche et les résultats à droite_

À gauche se trouve la `query` qui concerne le champ name dans le modèle project, les `"data"` étant renvoyées dans la requête résultante à droite.

La requête renvoyée en JavaScript Object Notation (JSON) est ce qui peut être consommé par le client (un navigateur, une application mobile, un écran en magasin ou un réfrigérateur).

## **Qu'est-ce que GraphCMS ?**

GraphCMS est un système de gestion de contenu (CMS) headless basé sur GraphQL qui vous permettra de mettre en place rapidement un back-end pour la diffusion de votre contenu.

Vous pouvez le faire en quelques minutes en cliquant sur un bouton à partir de l'un des templates fournis ou vous pouvez construire votre propre schéma avec l'interface utilisateur (UI) simple.

## **Comment configurer GraphCMS**

L'équipe de GraphCMS a créé un template pour cela, donc la configuration du backend pour ce projet se fait en un clic.

Vous devrez d'abord vous connecter à [GraphCMS](https://auth.graphcms.com/). Vous pouvez vous connecter avec votre compte GitHub ou vous authentifier par d'autres moyens.

Une fois connecté, vous verrez votre tableau de bord GraphCMS. Si c'est la première fois que vous utilisez GraphCMS, vous pouvez faire défiler la page jusqu'à « Developer Portfolio & Blog » dans la section « Create a new project ». Sélectionnez « Developer Portfolio & Blog » et cliquez sur « + Create project ».

On nous demande ensuite de donner un nom à notre projet. Je vais l'appeler « Portfolio and Blog », et la description peut rester vide pour l'instant. Vous pouvez choisir le centre de données le plus proche de chez vous pour l'hébergement de votre projet. Je suis au Royaume-Uni, donc je vais choisir le centre de données du Royaume-Uni.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-5.png)
_Choisissez votre centre de données_

Notez que si vous ajoutez votre propre contenu, activez l'option « Include template content? ».

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-6.png)
_Laissez cette option activée si vous comptez ajouter votre contenu plus tard._

En passant, tout le contenu de GraphCMS est servi à partir d'un CDN distribué mondialement, il n'y a donc pas lieu de s'inquiéter de la latence pour les utilisateurs qui ne sont pas proches de votre centre de données spécifié.

Cliquez sur le bouton « Create project » en bas de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-21.png)

Une fois que le projet a fini d'être provisionné, on vous présente le forfait que vous souhaitez utiliser. Choisissez le forfait communautaire « Free forever ».

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-22.png)

Une autre invite vous demandera si vous souhaitez inviter des coéquipiers. Sélectionnez simplement « Invite later ».

Le tableau de bord GraphCMS ressemblera à ceci. Toutes les sections du projet se trouvent sur le panneau de gauche. Dans la section suivante, nous y jetterons un œil.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-24.png)
_Le tableau de bord GraphCMS avec des flèches pointant vers les sections Schema, Content, Assets et API Playground._

## Comment requêter du contenu

Faisons notre première requête GraphQL. Il s'agira d'une liste de tous les projets ajoutés au CMS qui se trouvent dans le modèle project.

Allez dans l'API playground et entrez la requête GraphQL suivante dans l'onglet « New Query ».

```graphql
query GetProjects {
  projects {
    name
    slug
    description
    demo
    sourceCode
    image {
      url
    }
  }
}
```

Cette requête sélectionne le modèle `projects` puis chaque champ contenu dans ce modèle.

## **Comment créer votre projet Svelte**

Si vous utilisez Gitpod, vous pouvez passer directement à la création d'un fichier `.env`. Si vous configurez localement, commençons. Depuis le terminal, nous pouvons créer notre projet avec la commande `npm` suivante :

```bash
npm init svelte@next my-developer-portfolio
```

Depuis le CLI, je choisirai les options suivantes :

```bash
? Which Svelte app template? › - Use arrow-keys. Return to submit.
    SvelteKit demo app
❯   Skeleton project
? Use TypeScript? › No
? Add ESLint for code linting? › No
? Add Prettier for code formatting? › Yes
```

Je suivrai le reste des instructions du CLI. Si vous regardez la sortie du CLI, vous remarquerez également quelques autres fonctionnalités dont nous profiterons bientôt. Voici à quoi ressemble ma sortie :

```bash
Your project is ready!
✔ Prettier
  https://prettier.io/docs/en/options.html
  https://github.com/sveltejs/prettier-plugin-svelte#options

Install community-maintained integrations:
  https://github.com/svelte-add/svelte-adders

Next steps:
  1: cd my-developer-portfolio
  2: npm install (or pnpm install, etc)
  3: git init && git add -A && git commit -m "Initial commit" (optional)
  4: npm run dev -- --open

To close the dev server, hit Ctrl-C

Stuck? Visit us at https://svelte.dev/chat
```

Notez la section « Install community-maintained integrations » avec Svelte Adders – nous en utiliserons une plus tard pour ajouter Tailwind.

Maintenant, changez de répertoire (CD) pour entrer dans le dossier du projet, initialisez un dépôt Git et installez les dépendances :

```bash
# se déplacer dans le répertoire du projet
cd my-developer-portfolio
# initialiser un nouveau dépôt git et effectuer le premier commit
git init && git add -A && git commit -m "Initial commit"
# installer les dépendances
npm install # ou 'npm i' pour faire court
```

J'ouvrirai mon éditeur de texte et vérifierai le projet. J'ai VS Code installé, donc utiliser la commande `code` l'ouvrira et le `.` spécifie le répertoire actuel :

```bash
code .
```

Il est temps de vérifier que tout fonctionne comme prévu, alors lançons le serveur de développement :

```bash
# démarrer le serveur de développement
npm run dev
```

Maintenant que nous avons validé que tout fonctionne comme prévu, il est temps de créer un fichier `.env`. C'est là que l'URL de l'API GraphQL va résider. Vous pouvez créer le fichier avec l'interface utilisateur (UI) de votre éditeur de texte si vous le souhaitez. J'utiliserai la commande suivante à la racine de mon projet pour créer le fichier :

```bash
# Ctrl-c pour arrêter le serveur de développement
touch .env
echo VITE_GRAPHQL_API= >> .env
```

Cette commande depuis le terminal crée un fichier `.env` puis ajoute `VITE_GRAPHQL_API=` dans ce fichier.

Dans le fichier `.env`, ajoutez l'URL « Content API » de votre projet GraphCMS.

Le panneau des paramètres est accessible depuis la barre latérale :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-7.png)
_Paramètres du projet GraphCMS_

Puis « API access » :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-8.png)

Ensuite, cliquez sur l'URL « Content API ». Cela la copiera dans votre presse-papiers :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-9.png)
_Sélectionner l'URL de l'API de contenu_

Maintenant, ajoutez cela au fichier `.env`. Il devrait maintenant ressembler à ceci :

```env
VITE_GRAPHQL_API=https://api-region.graphcms.com/v2/projectid/master
```

## Comment afficher les données GraphQL sur la page d'accueil

Faisons notre première requête à notre API GraphQL !

Tout d'abord, pour obtenir des données sur la page, nous allons faire la requête à l'API GraphQL depuis la page d'accueil.

Pour ce faire, nous devrons installer quelques dépendances, `graphql-request` et `graphql`. `graphql-request` est ce que nous utiliserons pour envoyer nos requêtes GraphQL à l'API GraphQL. `graphql` est l'implémentation JavaScript du langage GraphQL.

```bash
npm i -D graphql-request graphql
```

Notez le `-D` dans la commande d'installation. C'est parce que Svelte n'a pas besoin de dépendances d'exécution car il compile le code à l'avance avant de l'envoyer au navigateur.

Commençons par ajouter un bloc script avec le contexte de module `<script context="module">` et importons la balise `gql` et le `GraphQLClient` de `graphql-request`.

Nous définirons également une fonction load de SvelteKit. C'est pour que nous puissions récupérer les données de l'API avant que la page ne se monte (se charge).

```svelte
<script context="module">
  import { gql, GraphQLClient } from 'graphql-request'

  export const load = async () => {

  }
</script>

```

À l'intérieur de la fonction `load` de SvelteKit, nous pouvons ensuite définir un nouveau client GraphQL. Le client accepte une URL (l'URL de l'API GraphCMS) et un objet d'options.

Nous allons y mettre la variable `VITE_GRAPHQL_API` que nous avons créée plus tôt. Notez que la variable commence par `VITE_`, ce qui signifie que Vite peut utiliser cette variable. Nous devrons l'importer avec `import.meta.env`, et cela devrait ressembler à ceci :

```svelte
<script context="module">
  import { gql, GraphQLClient } from 'graphql-request'

  export const load = async () => {
    const client = new GraphQLClient(
      import.meta.env.VITE_GRAPHQL_API
    )
</script>

```

Maintenant que le client est défini, nous pouvons l'utiliser pour passer une requête à l'API GraphQL de GraphCMS.

En reprenant la requête que nous avons faite plus tôt pour interroger tous les projets, nous pouvons l'ajouter à une variable `query` à utiliser avec le client GraphQL que nous avons défini.

La requête utilise la balise de langage GraphQL `gql` à l'intérieur de backticks `` gql` ` ``. Ensuite, nous pouvons déstructurer les projets de la réponse `await`ée que nous recevons du client GraphQL :

```svelte
<script context="module">
  import { gql, GraphQLClient } from 'graphql-request'

  export const load = async () => {
    const client = new GraphQLClient(
      import.meta.env.VITE_GRAPHQL_API
    )

    const query = gql`
      query GetProjects {
        projects {
          name
          slug
          description
          demo
          sourceCode
          image {
            url
          }
        }
      }
    `

    const { projects } = await client.request(query)
  }
</script>

```

Maintenant que le client a la requête, nous pouvons renvoyer les données de la réponse du client `projects` et les retourner comme props pour que la page les utilise.

Les données de l'API GraphQL peuvent maintenant être transmises à la page en tant que `props` dans le retour de la fonction `load` :

```svelte
<script context="module">
  import { gql, GraphQLClient } from 'graphql-request'

  export const load = async () => {
    const client = new GraphQLClient(
      import.meta.env.VITE_GRAPHQL_API
    )

    const query = gql`
      query GetProjects {
        projects {
          name
          slug
          description
          demo
          sourceCode
          image {
            url
          }
        }
      }
    `

    const { projects } = await client.request(query)

    return {
      props: {
        projects,
      },
    }
  }
</script>

```

Maintenant que les données sont renvoyées, nous devons les intégrer dans la page.

Nous pouvons le faire dans les balises `<script>` de la page. Donc oui, il y a deux ensembles de balises script – le premier `<script context="module">` pour exécuter la fonction `load` de SvelteKit avant le chargement (ou le montage) de la page, puis les balises `<script>` régulières pour définir tout JavaScript nécessaire sur le fichier `index.svelte` et aussi pour accepter les `props` qui sont `projects`.

Dans cette dernière section, nous acceptons les `projects` renvoyés par la fonction `load` avec `export let projects` dans les balises `<script>`. Maintenant, cette variable peut être utilisée dans la page.

À des fins d'illustration, j'ajoute la variable `projects` dans une balise `<pre>` et je convertis les résultats en chaîne avec `{JSON.stringify(projects, null, 2)}`. C'est temporaire afin que nous puissions valider et visualiser les données arrivant sur la page.

```svelte
<script context="module">
  import { gql, GraphQLClient } from 'graphql-request'

  export const load = async () => {
    const client = new GraphQLClient(
      import.meta.env.VITE_GRAPHQL_API
    )

    const query = gql`
      query GetProjects {
        projects {
          name
          slug
          description
          demo
          sourceCode
          image {
            url
          }
        }
      }
    `

    const { projects } = await client.request(query)

    return {
      props: {
        projects,
      },
    }
  }
</script>

<script>
  export let projects
</script>

<pre>{JSON.stringify(projects, null, 2)}</pre>

```

Il est temps de démarrer le serveur de développement et de voir à quoi ressemblent les choses maintenant :

```bash
npm run dev
```

Voici la sortie qui ressemble beaucoup à la sortie GraphQL de Projects dans le playground GraphQL que nous avons faite plus tôt :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-48.png)
_sortie localhost après avoir exécuté `npm run dev`_

Je sais que je vous ai vraiment guidé à travers chaque étape de celle-ci. C'est pour mettre en évidence les différentes sections de ce que nous faisons.

Ce sera un modèle similaire pour le reste du projet.

Les étapes suivantes ressembleront à ceci :

1. Créer une requête GraphQL pour définir les données nécessaires.
2. Donner cette requête au client GraphQL.
3. Travailler avec les données renvoyées par le client dans la page.

### Refactoriser le client GraphQL

Comme nous utiliserons le client GraphQL dans plus d'une page, il est temps de le déplacer dans son propre fichier afin qu'il puisse être réutilisé dans tout le projet.

Svelte a un dossier `lib` pour les fichiers qui sont réutilisés dans tout le projet, mais il n'y a pas encore de dossier (ou répertoire si vous préférez ce terme) pour cela – il est donc temps d'en créer un. Nous pouvons créer un fichier `graphql-client.js` pour y placer le client GraphQL :

```bash
# créer le dossier
mkdir src/lib
# créer le fichier
touch src/lib/graphql-client.js
```

Maintenant, déplaçons le client de la page d'accueil vers le fichier `src/lib/graphql-client.js` nouvellement créé :

```js
import { GraphQLClient } from 'graphql-request'
const GRAPHQL_ENDPOINT = import.meta.env.VITE_GRAPHQL_API

export const client = new GraphQLClient(GRAPHQL_ENDPOINT)

```

Dans le `src/routes/index.svelte`, je peux supprimer l'initialisation du client et importer le client depuis son fichier nouvellement créé dans le dossier lib.

Voici la différence. Si vous n'êtes pas familier avec un Git diff, les `+` et `-` à côté des lignes signifient que ces lignes sont ajoutées (`+`) ou supprimées (`-`) :

```git
<script context="module">
+  import { client } from '$lib/graphql-client'
-  import { gql, GraphQLClient } from 'graphql-request'
+  import { gql } from 'graphql-request'

  export const load = async () => {
-   const client = new GraphQLClient(import.meta.env.VITE_GRAPHQL_API)

    const query = gql`
      query GetProjects {
        projects {
          name
          slug
          description
          demo
          sourceCode
          image {
            url
          }
        }
      }
    `

    const { projects } = await client.request(query)

    return {
      props: {
        projects,
      },
    }
  }
</script>

<script>
  export let projects
</script>

<pre>{JSON.stringify(projects, null, 2)}</pre>
```

Cela fait, nous pouvons commencer à utiliser le client refactorisé dans notre page d'accueil.

Committons nos changements sur Git avant de passer à la section suivante :

```git
git add .
git commit -m "Show GraphQL data on index page"
```

## Comment ajouter le balisage pour la page d'accueil

Jusqu'à présent, nous n'avons réellement affiché les données de l'endpoint de l'API que dans une balise pre. Il est temps de changer cela en divisant les données renvoyées par l'API GraphQL en sections sur la page d'accueil.

Commençons par supprimer la balise `<pre>`, ajoutons un `<h1>` pour le titre de la page, puis dans un `<div>`, nous pouvons utiliser l'une des expressions Svelte pour boucler sur les données avec Svelte `{#each}`.

L'expression each prend l'objet `projects`. Ensuite, vous pouvez travailler avec une variable pour cela, disons `project`, et vous pouvez référencer les différentes propriétés sur cette variable.

Voici un exemple de ce à quoi cela pourrait ressembler :

```svelte
{#each projects as project}
  <div>
    <img src={project.image[0].url} alt={project.name} />
    <a href={`/projects/${project.slug}`}>
      <div>
        <h2>{project.name}</h2>
        <p>
          {project.description.slice(0, 80)}...
        </p>
      </div>
    </a>
  </div>
{/each}
```

Pour aller plus loin, nous pouvons déstructurer les propriétés de cette partie de la boucle afin qu'il ne soit pas nécessaire de référencer les propriétés spécifiques de `project`.

Notez que `image.url` est également déstructuré ici.

Ainsi, au lieu de `{#each projects as project}`, nous pouvons faire ceci `{#each projects as { name, slug, description, image }}`.

Voici à quoi devrait ressembler le fichier `src/routes/index.svelte` maintenant :

```svelte
<script context="module">
  import { client } from '$lib/graphql-client'
  import { gql } from 'graphql-request'

  export const load = async () => {
    const query = gql`
      query GetProjects {
        projects {
          name
          slug
          description
          tags
          demo
          sourceCode
          image {
            url
          }
        }
      }
    `
    const { projects } = await client.request(query)

    return {
      props: {
        projects,
      },
    }
  }
</script>

<script>
  export let projects
</script>

<h1>Recent Projects by Me</h1>

<div>
  {#each projects as { name, slug, description, image }}
    <div>
      <img src={image[0].url} alt={name} />
      <a href={`/projects/${slug}`}>
        <div>
          <h2>{name}</h2>
          <p>
            {description.slice(0, 80)}...
          </p>
        </div>
      </a>
    </div>
  {/each}
</div>

```

## Comment construire le premier composant Svelte

Ce que nous allons faire maintenant, c'est créer notre premier composant Svelte. Ce sera pour la carte de projet que nous avons faite dans le dernier bloc de code.

C'est pour que nous puissions réutiliser ce code dans d'autres parties du projet. Donc, ce sera tout ce qui se trouve à l'intérieur de la boucle `{#each}` que nous avons faite pour afficher chaque projet sur la page d'accueil, cette section ici :

```svelte
<div>
  <img src={image[0].url} alt={name} />
  <a href={`/projects/${slug}`}>
    <div>
      <h2>{name}</h2>
      <p>
        {description.slice(0, 80)}...
      </p>
    </div>
  </a>
</div>
```

Créons un dossier `lib` et un composant `project-card.svelte` à placer dans ce dossier :

```bash
# créer le dossier des composants
mkdir src/lib/components
# créer le fichier du composant
touch src/lib/components/project-card.svelte
```

Dans ce fichier, nous pouvons maintenant ajouter le balisage pour la carte de projet :

```svelte
<div>
  <img src={image[0].url} alt={name} />
  <a href={`/projects/${slug}`}>
    <div>
      <h2>{name}</h2>
      <p>
        {description.slice(0, 80)}...
      </p>
    </div>
  </a>
</div>
```

Le balisage contient pour le moment les variables pour l'URL de l'image, le nom du projet et la description. Actuellement, cela ne fonctionnera pas car ces variables ne sont référencées nulle part.

À l'intérieur de balises `<script>`, nous pouvons définir les variables attendues par le composant.

```svelte
<script>
  export let url = ''
  export let name = ''
  export let slug = ''
  export let description = ''
</script>

<div>
  <img src={url} alt={name} />
  <a href={`/projects/${slug}`}>
    <div>
      <h2>{name}</h2>
      <p>
        {description.slice(0, 80)}...
      </p>
    </div>
  </a>
</div>

```

Le composant étant maintenant prêt à accepter les variables pour le projet, nous pouvons les lui passer sur la page d'accueil.

```svelte
<script context="module">
  import ProjectCard from '$lib/components/project-card.svelte'
  import { client } from '$lib/graphql-client'
  import { gql } from 'graphql-request'

  export const load = async () => {
    const query = gql`
      query GetProjects {
        projects {
          name
          slug
          description
          tags
          demo
          sourceCode
          image {
            url
          }
        }
      }
    `
    const { projects } = await client.request(query)

    return {
      props: {
        projects,
      },
    }
  }
</script>

<script>
  export let projects
</script>

<h1>Recent Projects by Me</h1>

<div>
  {#each projects as { name, slug, description, image }}
    <ProjectCard {name} {description} url={image[0].url} {slug} />
  {/each}
</div>

```

Le composant est importé entre les balises `<script>`, puis les variables individuelles de la boucle lui sont transmises.

Jetons un coup d'œil rapide aux variables transmises. Elles pourraient être définies comme ceci :

```svelte
<ProjectCard
  name={name}
  description={description}
  url={image[0].url}
  slug={slug}
/>
```

Comme les props attendues sur le composant sont les mêmes que celles qui sont transmises, il n'est pas nécessaire de nommer les props. Voici donc ce que nous pouvons utiliser :

```svelte
<ProjectCard {name} {description} url={image[0].url} {slug} />
```

Notez que la propriété `image` est un tableau (car le projet peut comporter plusieurs images), nous référençons donc le premier index de ce tableau.

Committons cela avant de passer à la section suivante :

```git
git add .
git commit -m "Add first component"
```

## Comment styliser dans Svelte

Svelte étant un sur-ensemble du HTML, cela signifie que vous pouvez styliser vos fichiers `.svelte` de la même manière que vous le feriez dans des fichiers HTML.

Ajouter des balises `<style>` en bas du fichier signifie que vous pouvez styliser les éléments de la page :

```svelte
<p>Hello Svelte</p>

<style>
  p {
    color: red;
    font-size: 2rem;
  }
</style>
```

Cela stylisera tous les éléments `<p>` de ce fichier avec une police rouge et une taille de police de 2rem.

Vous obtenez beaucoup de contrôle de cette façon, vous permettant de spécifier des styles uniquement pour ce fichier.

Ceci n'est qu'un exemple, et ce n'est pas ainsi que je ferai le stylisme pour ce projet. J'opte plutôt pour Tailwind CSS.

## Comment styliser avec Tailwind et daisyUI

Le stylisme est un sujet très subjectif et personnel, donc ce que je vais faire peut ne pas correspondre à ce que vous avez en tête.

Pour cette raison, je limiterai le stylisme au minimum et j'essaierai de ne pas trop m'y attarder.

J'utiliserai [Tailwind CSS](https://tailwindcss.com/) et [daisyUI](https://daisyui.com/) pour la rapidité avec laquelle je peux créer des composants et des styles. Si cela ne vous convient pas, vous pouvez continuer à styliser comme suggéré dans la section précédente.

Je vais utiliser `svelte-add` pour configurer le projet afin d'utiliser TailwindCSS. Le projet Svelte Adders que j'ai mentionné plus tôt fait toute la configuration pour vous avec une commande `npm` :

```bash
npx svelte-add@latest tailwindcss
# installer les dépendances configurées
npm i
```

La commande `svelte-add` a configuré le projet pour l'utilisation de Tailwind. Elle a également ajouté un fichier dans `src/routes` appelé `__layout.svelte` – nous y reviendrons bientôt. Pour l'instant, sachez qu'il est là et que nous l'utiliserons dans une section à venir.

Je vais également utiliser quelques plugins TailwindCSS – il s'agit de daisyUI et du plugin TailwindCSS Typography.

daisyUI est une excellente ressource pour des composants pré-faits, et vous pouvez en choisir un certain nombre sur le site. C'est ce que je ferai pour les composants d'en-tête et de pied de page.

Tailwind CSS Typography est vraiment utile pour styliser le contenu que nous recevons de l'API. C'est un excellent ensemble de valeurs par défaut de l'équipe Tailwind Labs.

Je vais les installer via le terminal :

```bash
npm i -D @tailwindcss/typography daisyui
```

Ensuite, je peux les configurer dans le fichier `tailwind.config.cjs` :

```js
plugins: [
  require('@tailwindcss/typography'),
  require('daisyui'),
],
```

Une configuration supplémentaire est nécessaire pour le plugin TailwindCSS Typography afin de supprimer la largeur maximale. Voici à quoi ressemble le fichier `tailwind.config.cjs` complet :

```js
const config = {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            maxWidth: null,
          },
        },
      },
    },
  },

  plugins: [require('@tailwindcss/typography'), require('daisyui')],
}

module.exports = config

```

Lançons le serveur de développement et validons l'installation. La police du projet sera différente maintenant.

Committez les changements et nous passerons à la section suivante :

```git
git add .
git commit -m "Add Tailwind CSS and daisyUI"
```

## Comment styliser le composant Projets

Ok, maintenant je peux ajouter quelques styles pour le fichier `src/components/project-card.svelte`.

Ceci utilise plusieurs classes Tailwind, et ce sera probablement le maximum de ce que nous dévierons des classes pré-packagées que nous obtenons de daisyUI :

```svelte
<script>
  export let url = ''
  export let name = ''
  export let slug = ''
  export let description = ''
</script>

<div class="relative group card shadow-2xl col-span-2">
  <img src={url} alt={name} class="object-cover h-full" />
  <a href={`/projects/${slug}`}>
    <div
      class="absolute bottom-0 left-0 right-0 lg:opacity-0 group-hover:opacity-100 bg-primary p-4 duration-300 text-primary-content"
    >
      <h2 class="font-bold lg:text-xl">{name}</h2>
      <p class="text-sm lg:text-xl">
        {description.slice(0, 80)}...
      </p>
    </div>
  </a>
</div>

```

Sur le div conteneur, nous ajoutons une position `relative` puis nous utilisons la classe Tailwind `group` pour appliquer le `group-hover` sur le div contenant le contenu de la description.

Comme le div conteneur a une position `relative`, nous pouvons alors positionner de manière `absolute` le div de description au bas du div conteneur avec `bottom-0`, `left-0` et `right-0` afin qu'il s'étende sur tout le bas du div conteneur.

La classe `lg:` est là pour que lorsque l'utilisateur est sur un écran plus petit, le div s'affiche quel que soit le survol de la souris.

Committons cela sur Git et passons à la section suivante :

```git
git add .
git commit -m "Style Projects component"
```

## Comment utiliser le fichier `__layout` de SvelteKit

Pour les styles globaux, nous pouvons utiliser le fichier spécial `__layout.svelte` de SvelteKit. Nous pouvons l'utiliser pour contrôler les styles globaux et aussi pour obtenir des informations externes que vous souhaitez transmettre à toutes les pages ou composants utilisés dans le projet.

Pour l'instant, ajoutons quelques classes de conteneur pour les tailles d'écran réactives :

```svelte
<script>
  import '../app.css'
</script>

<main class="container max-w-3xl mx-auto px-4 mb-20">
  <slot />
</main>

```

Committez cela sur Git, puis passez à la section suivante :

```git
git add .
git commit -m "Add layout container CSS classes"
```

## **Comment construire la page de destination avec la liste des projets**

Commençons par la page de destination. Sur la page de destination, nous allons vouloir afficher des informations sur l'Auteur et les Projets.

Nous avons déjà la requête des projets définie et utilisée sur la page `src/routes/index.svelte`. Nous allons également vouloir obtenir des données du modèle `author` pour les utiliser dans la page d'accueil.

Ce que nous allons devoir faire, c'est créer une autre requête GraphQL pour l'auteur dans la fonction load de la page `src/routes/index.svelte`. Allons sur le playground GraphQL de GraphCMS et définissons cela maintenant :

```graphql
query GetAuthors {
  authors {
    name
    intro
    bio
    slug
    picture {
      url
    }
  }
}
```

Ok, nous avons donc une requête pour les projets et une requête pour les auteurs. Passons maintenant à la récupération des données avec ces deux requêtes !

Pour y parvenir, nous allons utiliser la méthode JavaScript `[Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all)` pour obtenir les données des deux endpoints et les renvoyer pour utilisation dans le projet.

```svelte
<script context="module">
  import ProjectCard from '$lib/components/project-card.svelte'
  import { client } from '$lib/graphql-client'
  import { gql } from 'graphql-request'

  export const load = async () => {
    const authorsQuery = gql`
      query GetAuthors {
        authors {
          name
          intro
          bio
          slug
          picture {
            url
          }
        }
      }
    `
    const projectsQuery = gql`
      query GetProjects {
        projects {
          name
          slug
          description
          tags
          demo
          sourceCode
          image {
            url
          }
        }
      }
    `
    const [authorReq, projectsReq] = await Promise.all([
      client.request(authorsQuery),
      client.request(projectsQuery),
    ])
    const { authors } = authorReq
    const { projects } = projectsReq

    return {
      props: {
        projects,
        authors,
      },
    }
  }
</script>

<script>
  export let projects
  export let authors
</script>

<h1 class="font-bold text-center mb-20 text-5xl">
  Welcome to my Portfolio
</h1>

{#each authors as { name, intro, picture: { url } }}
  <div class="flex mb-40 items-end">
    <div class="mr-6">
      <h2 class="text-3xl mb-4 font-bold tracking-wider">{name}</h2>
      <p class="text-xl mb-4">{intro}</p>
    </div>

    <img class="mask mask-squircle h-48" src={url} alt={name} />
  </div>
{/each}

<div
  class="grid gap-10 md:grid-cols-4 md:px-10 lg:grid-cols-6 lg:-mx-52"
>
  {#each projects as { name, slug, description, image }}
    <ProjectCard {name} {description} url={image[0].url} {slug} />
  {/each}
</div>

```

Wow ! Il y a beaucoup de choses ici maintenant.

Ces deux requêtes GraphQL prennent vraiment beaucoup de place dans cette fonction load. Prenons une minute pour les refactoriser afin qu'elles puissent être utilisées ailleurs. Cela aidera également à nettoyer cette page car elle devient un peu encombrée avec les requêtes GraphQL qui occupent la majeure partie du fichier.

### Comment refactoriser les requêtes GraphQL

Récupérons ces deux requêtes en haut du fichier, ces deux-là :

```js
const authorsQuery = gql`
  query GetAuthors {
    authors {
      name
      intro
      bio
      slug
      picture {
        url
      }
    }
  }
`
const projectsQuery = gql`
  query GetProjects {
    projects {
      name
      slug
      description
      tags
      demo
      sourceCode
      image {
        url
      }
    }
  }
`

```

Et ajoutons-les à leur propre fichier JavaScript. Créons-le maintenant :

```bash
# créer le fichier graphql-queries.js
touch src/lib/graphql-queries.js
```

Ensuite, nous pouvons prendre les requêtes du fichier `src/routes/index.svelte` et les y ajouter :

```js
import { gql } from 'graphql-request'

export const authorsQuery = gql`
  query GetAuthors {
    authors {
      name
      intro
      bio
      slug
      picture {
        url
      }
    }
  }
`

export const projectsQuery = gql`
  query GetProjects {
    projects {
      name
      slug
      description
      tags
      demo
      sourceCode
      image {
        url
      }
    }
  }
`

```

Notez qu'elles ont maintenant `export` devant le `const`. C'est pour qu'elles puissent être exportées de ce fichier pour être utilisées dans le fichier `src/routes/index.svelte`.

Dans le `src/routes/index.svelte`, je peux maintenant importer ces requêtes, ce qui nettoie un peu le fichier en supprimant tout le bruit des requêtes dans la fonction load. Voici à quoi cela devrait ressembler maintenant :

```svelte
<script context="module">
  import ProjectCard from '$lib/components/project-card.svelte'
  import { client } from '$lib/graphql-client'
  import { authorsQuery, projectsQuery } from '$lib/graphql-queries'

  export const load = async () => {
    const [authorReq, projectsReq] = await Promise.all([
      client.request(authorsQuery),
      client.request(projectsQuery),
    ])
    const { authors } = authorReq
    const { projects } = projectsReq

    return {
      props: {
        projects,
        authors,
      },
    }
  }
</script>

<script>
  export let projects
  export let authors
</script>

<svelte:head>
  <title>My Portfolio project</title>
</svelte:head>

<h1 class="font-bold text-center mb-20 text-5xl">
  Welcome to my Portfolio
</h1>

{#each authors as { name, intro, picture: { url } }}
  <div class="flex mb-40 items-end">
    <div class="mr-6">
      <h2 class="text-3xl mb-4 font-bold tracking-wider">{name}</h2>
      <p class="text-xl mb-4">{intro}</p>
    </div>

    <img class="mask mask-squircle h-48" src={url} alt={name} />
  </div>
{/each}

<div
  class="grid gap-10 md:grid-cols-4 md:px-10 lg:grid-cols-6 lg:-mx-52"
>
  {#each projects as { name, slug, description, image }}
    <ProjectCard {name} {description} url={image[0].url} {slug} />
  {/each}
</div>

```

Whoa ! Que fait ce `<svelte:head>` ici ?

L'[API Svelte Head](https://svelte.dev/docs#template-syntax-svelte-head) nous permet d'ajouter des métadonnées HTML au projet – donc, des balises comme le titre de la page comme dans l'exemple ci-dessus, mais aussi des balises meta pour Google, Facebook et Twitter. Également pour la [monétisation](https://webmonetization.org/).

Cette implémentation donnera à l'onglet du navigateur le titre « My Portfolio project ».

En dehors du composant head ajouté ici, nous utilisons également les données de la requête `authors` pour afficher les données du modèle authors sur GraphCMS.

Committez les changements sur Git :

```git
git add .
git commit -m "Landing page with projects listed"
```

Ok, super – notre page de destination est prête.

## Comment utiliser SvelteKit Routing

Nous avons maintenant une belle page de destination avec des liens vers les projets. Mais cliquer sur un lien nous mènera à une page 404. C'est parce que la route pour cette page n'existe pas encore.

Créons-la maintenant. Nous utiliserons le [routage basé sur les fichiers](https://kit.svelte.dev/docs#routing-pages) de SvelteKit pour ce faire.

Nous devrons créer un fichier qui prendra le `slug` de la carte des projets et l'utilisera pour le chemin du projet. Créons d'abord le fichier :

```bash
# créer le dossier projects
mkdir src/routes/projects
# créer le fichier [slug].svelte
touch src/routes/projects/'[slug]'.svelte

```

Dans le `src/routes/projects/[slug].svelte`, nous pouvons définir une fonction load de SvelteKit qui reçoit une variable context. Regardons d'abord ce que nous obtenons dans la variable context :

```js
<script context="module">
  export const load = async context => {
    console.log('=====================')
    console.log('context', context)
    console.log('=====================')
    return {}
  }
</script>
```

Actualiser la route pour [`localhost:3000/projects/survey-form`](http://localhost:3000/projects/survey-form) donnera une sortie dans le terminal comme celle-ci :

```text
=====================
context {
  url: URL {
    href: 'http://localhost:3000/projects/survey-form',
    origin: 'http://localhost:3000',
    protocol: 'http:',
    username: '',
    password: '',
    host: 'localhost:3000',
    hostname: 'localhost',
    port: '3000',
    pathname: '/projects/survey-form',
    search: '',
    searchParams: URLSearchParams {},
    hash: ''
  },
  params: { slug: 'survey-form' },
  props: {},
  session: [Getter],
  fetch: [AsyncFunction: fetch],
  stuff: {}
}
=====================
```

Ce qui nous intéresse ici, c'est la propriété `params.slug` que nous pouvons utiliser pour faire une requête à l'API GraphQL.

Allons sur le playground GraphQL dans notre projet GraphCMS. Là, nous allons faire une requête pour filtrer sur un projet où le `slug` correspond à ce qui est renvoyé par la fonction load de SvelteKit ici :

![Requête GraphQL pour interroger un projet où le slug correspond à "survey-form"](https://www.freecodecamp.org/news/content/images/2021/12/image-42.png)
_Requête GraphQL pour interroger un projet où le slug correspond à "survey-form"_

Dans l'image, j'ai défini ici une requête pour filtrer sur le champ `slug` où `"survey-form"` est passé à la requête.

C'est très bien pour cette requête unique, mais nous voulons un moyen de passer des variables à la requête pour chaque slug de projet individuel que nous avons. Jetons un coup d'œil à l'utilisation des variables dans GraphQL maintenant.

J'ajouterai des parenthèses à la fin du nom de la requête, et dans ces parenthèses je définirai une variable `query GetProject($slug: String!) {`. Le `$` indique qu'il s'agit d'une variable tandis que `: String!` indique le type de données de la variable.

Comme GraphQL est fortement typé, cela doit être défini pour que GraphQL sache comment il peut utiliser la variable. Le point d'exclamation `!` à la fin indique que la variable est requise pour que la requête fonctionne.

Maintenant, je peux utiliser la variable à la place de la valeur codée en dur `"survey-form"` que j'utilisais précédemment :

```graphql
query GetProject($slug: String!) {
  project(where: {slug: $slug}) {
    name
    description
    tags
    demo
    sourceCode
    image {
      url
    }
  }
}
```

Si j'essaie d'exécuter cette requête maintenant, j'obtiens l'erreur suivante :

```json
{
  "errors": [
    {
      "message": "variable 'slug' must be defined"
    }
  ],
  "data": null,
}
```

Donc, pour faire fonctionner cela dans le playground GraphQL ici, je peux utiliser le panneau « QUERY VARIABLES » que vous avez peut-être remarqué dans la dernière image. Cliquer dessus ouvrira le panneau et je pourrai y ajouter la valeur de la variable :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-43.png)

Maintenant, avec la variable slug définie dans le panneau de requête, je suis en mesure d'exécuter la requête.

Ok, c'est super ! Comment utiliser cela dans le projet ?

Bonne question ! Je veux un moyen de passer cette variable de requête au client GraphQL avec la requête.

Nous pouvons le faire à peu près de la même manière que pour la page d'accueil. C'est le même modèle répétitif maintenant – et cette fois nous allons accepter la variable `slug` à utiliser dans la requête que j'ai définie.

Avant d'en arriver là, ajoutons cette requête de projet au fichier `src/lib/graphql-queries.js` :

```js
import { gql } from 'graphql-request'

export const authorsQuery = gql`
  query GetAuthors {
    authors {
      name
      intro
      bio
      slug
      picture {
        url
      }
    }
  }
`

export const projectsQuery = gql`
  query GetProjects {
    projects {
      name
      slug
      description
      tags
      demo
      sourceCode
      image {
        url
      }
    }
  }
`

export const projectQuery = gql`
  query GetProject($slug: String!) {
    project(where: { slug: $slug }) {
      name
      slug
      description
      tags
      demo
      sourceCode
      image {
        url
      }
    }
  }
`
```

Il y a donc un peu de répétition dans ce fichier, maintenant, avec `name`, `slug`, `description`, `tags`, `demo`, `sourceCode` et `image.url` répétés dans les requêtes `Projects` et `Project`.

Nous pouvons utiliser un [fragment GraphQL](https://graphql.org/learn/queries/#fragments) ici pour réutiliser les champs du modèle. Voici à quoi cela ressemble :

```js
const PROJECT_FRAGMENT = gql`
  fragment ProjectDetails on Project {
    name
    slug
    description
    tags
    demo
    sourceCode
    image {
      url
    }
  }
`
```

Tous les champs sont dans une seule requête maintenant, le fragment est nommé `ProjectDetails` et il est `on` (sur) le modèle `Project`. Maintenant, cela peut être utilisé dans les requêtes `Projects` et `Project` en propageant (`...`) le `ProjectDetails` dans les requêtes :

```js
import { gql } from 'graphql-request'

export const authorsQuery = gql`
  query GetAuthors {
    authors {
      name
      intro
      bio
      slug
      picture {
        url
      }
    }
  }
`

const PROJECT_FRAGMENT = gql`
  fragment ProjectDetails on Project {
    name
    slug
    description
    tags
    demo
    sourceCode
    image {
      url
    }
  }
`

export const projectsQuery = gql`
  ${PROJECT_FRAGMENT}
  query GetProjects {
    projects {
      ...ProjectDetails
    }
  }
`

export const projectQuery = gql`
  ${PROJECT_FRAGMENT}
  query GetProject($slug: String!) {
    project(where: { slug: $slug }) {
      ...ProjectDetails
    }
  }
`
```

Une chose que je vais devoir faire maintenant, avant d'aller plus loin, est d'utiliser une dépendance pour le contenu Markdown de la description du projet.

Il s'agit de prendre le contenu Markdown de la description du projet et de le transformer en HTML afin qu'il puisse être présenté sur la page. Je vais utiliser `marked` ici :

```bash
npm i -D marked
```

Maintenant que la requête est définie, nous pouvons l'utiliser dans le fichier `src/routes/projects/[slug].svelte` :

```svelte
<script context="module">
  import { client } from '$lib/graphql-client'
  import { projectQuery } from '$lib/graphql-queries'
  import { marked } from 'marked'

  export const load = async ({ params }) => {
    const { slug } = params
    const variables = { slug }
    const { project } = await client.request(projectQuery, variables)

    return {
      props: {
        project,
      },
    }
  }
</script>

<script>
  export let project
</script>

<svelte:head>
  <title>My Portfolio | {project.name}</title>
</svelte:head>

<div class="sm:-mx-5 md:-mx-10 lg:-mx-20 xl:-mx-38 mb-5">
  <img
    class="rounded-lg"
    src={project.image[0].url}
    alt={project.title}
  />
</div>

<h1 class="text-4xl font-semibold mb-5">{project.name}</h1>

<div class="mb-5 flex justify-between">
  <div>
    {#if project.tags}
      {#each project.tags as tag}
        <span
          class="badge badge-primary mr-2 hover:bg-primary-focus cursor-pointer"
          >{tag}</span
        >
      {/each}
    {/if}
  </div>
</div>

<div
  class="mb-5 prose flex prose-a:text-primary hover:prose-a:text-primary-focus"
>
  <a class="mr-5" href={project.demo}>Demo</a>
  <a href={project.sourceCode}>Source Code</a>
</div>

<article class="prose prose-xl">
  {@html marked(project.description)}
</article>

```

Dans le fichier `src/routes/projects/[slug].svelte`, nous faisons pratiquement la même chose que pour le fichier `src/routes/index.svelte`, sauf que nous utilisons `params: { slug }` pour passer la valeur du slug au client GraphQL afin d'obtenir les données relatives à ce slug.

`{@html}` est utilisé pour afficher le contenu en tant que HTML. Utilisez ceci avec prudence si vous ne faites pas confiance à la source du HTML – mais dans notre cas, nous savons que nous pouvons faire confiance au HTML car c'est nous qui l'avons mis là ! 😊

Committons cela sur Git avant de continuer :

```git
git add .
git commit -m "Add project page using SvelteKit routing"
```

### Comment construire la page d'index des projets

Maintenant, créons un index pour les projets. C'est un peu comme la page de destination, mais cette fois c'est uniquement pour lister les projets.

Je vais créer un index pour la route projects :

```bash
touch src/routes/projects/index.svelte
```

Maintenant, naviguer vers `localhost:3000/projects` affichera ce fichier.

Il est temps de répéter le modèle utilisé pour obtenir la liste des projets sur la page d'accueil, mais sans les informations sur l'auteur :

```svelte
<script context="module">
  import ProjectCard from '$lib/components/project-card.svelte'
  import { client } from '$lib/graphql-client'
  import { projectsQuery } from '$lib/graphql-queries'

  export const load = async () => {
    const { projects } = await client.request(projectsQuery)

    return {
      props: {
        projects,
      },
    }
  }
</script>

<script>
  export let projects
</script>

<svelte:head>
  <title>My Portfolio projects</title>
</svelte:head>

<h1 class="font-bold mb-20 text-center text-5xl">
  Recent Projects by Me
</h1>

<div
  class="grid gap-10 md:grid-cols-4 md:px-10 lg:grid-cols-6 lg:-mx-52"
>
  {#each projects as { name, slug, description, image }, index}
    <ProjectCard
      {name}
      {description}
      url={image[0].url}
      {index}
      {slug}
    />
  {/each}
</div>

```

Super ! Maintenant, naviguer vers `localhost:3000/projects` nous donne une page dédiée aux projets.

Passons à la répétition de ces modèles que nous avons appris pour la page d'index du blog et les articles de blog individuels.

Committez sur Git les changements actuels avant de continuer :

```git
git add .
git commit -m "Add projects index page"
```

## **Comment construire le blog**

C'est au tour du blog maintenant. C'est à peu près la même approche que pour les projets, mais reprenons le processus.

1. Créer une requête GraphQL pour définir les données nécessaires.
2. Donner cette requête au client GraphQL.
3. Travailler avec les données renvoyées par le client dans la page.

Créez une requête GraphQL pour les articles. Comme nous suivrons le même modèle que pour les projets (requête pour tous les projets et filtrage pour un projet spécifique), nous pouvons créer un fragment GraphQL pour les données que nous voulons obtenir, à la fois sur tous les articles et sur un seul article.

```js
const POST_FRAGMENT = gql`
  fragment PostDetails on Post {
    title
    slug
    date
    content
    tags
    coverImage {
      url
    }
    authors {
      name
    }
  }
`
```

Nous pouvons ensuite utiliser le même modèle qu'auparavant où nous utilisons le fragment dans une requête Posts et Post :

```js
export const postsQuery = gql`
  ${POST_FRAGMENT}
  query GetPosts {
    posts {
      ...PostDetails
    }
  }
`

export const postQuery = gql`
  ${POST_FRAGMENT}
  query GetPost($slug: String!) {
    post(where: { slug: $slug }) {
      ...PostDetails
    }
  }
`
```

Avec le `POST_FRAGMENT`, `postsQuery` et `postQuery` ajoutés au fichier `src/lib/graphql-queries.js`, nous pouvons créer une route posts puis ajouter un fichier `[slug].svelte` et un fichier `index.svelte`.

```bash
mkdir src/routes/posts
touch src/routes/posts/{'[slug]'.svelte,index.svelte}
```

Traitons d'abord la page d'index des articles, puis nous pourrons passer aux articles individuels avec le fichier slug.

La première section, nous l'avons faite plusieurs fois maintenant : définir une fonction load de SvelteKit puis utiliser le client GraphQL pour interroger les articles :

```svelte
<script context="module">
  import { client } from '$lib/graphql-client'
  import { postsQuery } from '$lib/graphql-queries'
  import { marked } from 'marked'

  export const load = async () => {
    const { posts } = await client.request(postsQuery)

    return {
      props: {
        posts,
      },
    }
  }
</script>

<script>
  export let posts
</script>

<svelte:head>
  <title>Portfolio | Blog</title>
</svelte:head>
```

Maintenant, nous devons ajouter le balisage pour la page. En utilisant les classes de cartes daisyUI, nous pouvons définir une carte assez élégante, puis boucler sur les tags des articles et enfin faire un lien vers la page de l'article.

```svelte
<h1 class="text-4xl mb-10 font-extrabold">Blog posts</h1>

{#each posts as { title, slug, content, coverImage, tags }}
  <div class="card text-center shadow-2xl mb-20">
    <figure class="">
      <img
        class=""
        src={coverImage.url}
        alt={`Cover image for ${title}`}
      />
    </figure>
    <div class="card-body prose">
      <h2 class="title">{title}</h2>
      {@html marked(content).slice(0, 150)}
      <div class="flex justify-center mt-5 space-x-2">
        {#each tags as tag}
          <span class="badge badge-primary">{tag}</span>
        {/each}
      </div>
      <div class="justify-center card-actions">
        <a href={`/posts/${slug}`} class="btn btn-outline btn-primary"
          >Read &rArr;</a
        >
      </div>
    </div>
  </div>
{/each}

```

Il est temps de répéter ce modèle à nouveau !

Fonction load de SvelteKit utilisant le client GraphQL en passant la requête post et la variable provenant des paramètres de la page :

```svelte
<script context="module">
  import { client } from '$lib/graphql-client'
  import { postQuery } from '$lib/graphql-queries'
  import { marked } from 'marked'

  export const load = async ({ params }) => {
    const { slug } = params
    const variables = { slug }
    const { post } = await client.request(postQuery, variables)

    return {
      props: {
        post,
      },
    }
  }
</script>

<script>
  export let post

  const { title, date, tags, content, coverImage } = post
</script>

<svelte:head>
  <title>Blog | {title}</title>
</svelte:head>
```

Ensuite, pour le balisage sur la page, en utilisant les classes Tailwind CSS Typography ici pour un beau balisage :

```svelte
<div class="sm:-mx-5 md:-mx-10 lg:-mx-20 xl:-mx-38 mb-5">
  <img
    class="rounded-xl"
    src={coverImage.url}
    alt={`Cover image for ${title}`}
  />
</div>

<div class="prose prose-xl">
  <h1>{title}</h1>
</div>

<p class="text-secondary text-xs tracking-widest font-semibold">
  {new Date(date).toDateString()}
</p>

<div class="mb-5 flex justify-between">
  <div>
    {#if tags}
      <div class="mt-5 space-x-2">
        {#each tags as tag}
          <span class="badge badge-primary">{tag}</span>
        {/each}
      </div>
    {/if}
  </div>
</div>

<article div class="prose prose-lg">
  {@html marked(content)}
</article>
```

Committons nos changements maintenant :

```git
git add .
git commit -m "Add posts index page and slug page"
```

Ok, nous avons maintenant beaucoup de pages sur le site à regarder, mais aucun moyen de naviguer entre elles pour l'instant.

## Comment construire les composants Navbar et Footer

Je vais maintenant récupérer quelques composants pré-faits de daisyUI pour le [footer](https://daisyui.com/components/footer) et la [navbar](https://daisyui.com/components/navbar). Créons d'abord les fichiers avant d'aller sur le site de daisyUI pour les récupérer :

```bash
touch src/lib/components/{footer.svelte,navbar.svelte}
```

Ces accolades dans cette commande créent les deux fichiers pour nous.

### Comment créer le composant Footer

Tout d'abord, nous pouvons faire le composant footer. J'utiliserai le deuxième des composants `footer footer-center` de la section footer des composants daisyUI. Voici à quoi il ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-49.png)

Et voici le balisage pour ce composant :

```svelte
<footer class="p-10 footer bg-base-200 text-base-content footer-center">
  <div class="grid grid-flow-col gap-4">
    <a class="link link-hover">About us</a> 
    <a class="link link-hover">Contact</a> 
    <a class="link link-hover">Jobs</a> 
    <a class="link link-hover">Press kit</a>
  </div> 
  <div>
    <div class="grid grid-flow-col gap-4">
      <a>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-current">
          <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
        </svg>
      </a> 
      <a>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-current">
          <path d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
        </svg>
      </a> 
      <a>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-current">
          <path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
        </svg>
      </a>
    </div>
  </div> 
  <div>
    <p>Copyright © 2021 - All right reserved by ACME Industries Ltd</p>
  </div>
</footer>

```

Une chose à noter ici : si vous n'aimez pas les SVG directement dans le HTML ici, ils peuvent être extraits dans leurs propres composants et importés dans le fichier footer. Comme Svelte est un sur-ensemble du HTML, cela rend possible la division de gros fichiers en composants gérables.

Faisons cela maintenant pour réduire la taille du fichier et le rendre plus facile à analyser. Donc, je vais d'abord créer les fichiers d'icônes :

```bash
touch src/lib/components/{twitter-icon.svelte,you-tube-icon.svelte,facebook-icon.svelte}
```

Maintenant, je peux supprimer les balises `<svg>` du composant footer et les ajouter à leurs fichiers respectifs.

Voici à quoi ressemble celui de Twitter. Vous pouvez répéter cela pour les composants restants :

```svelte
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  class="fill-current"
>
  <path
    d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"
  />
</svg>
```

Il y a quelques éléments que nous voulons changer avant de l'utiliser dans notre projet ici.

Dans l'élément footer, changez l'arrière-plan de `bg-base-200` à `bg-primary` et changez `text-base-content` à `text-primary-content`.

```svelte
<footer
  class="p-10 footer bg-primary text-primary-content footer-center"
>
```

Ensuite, il y a les liens à ajouter dans la section suivante :

```svelte
<div class="grid grid-flow-col gap-4">
  <a class="link link-hover" href="/projects">Portfolio</a>
  <a class="link link-hover" href="/posts">Blog</a>
  <a class="link link-hover" href="/about">About</a>
</div>
```

Vous pouvez ajouter les liens directs vers les fournisseurs sociaux pour l'instant. Bien qu'ils soient disponibles dans le modèle Social.

Pour la section copyright à la fin du fichier, j'ajouterai du JavaScript pour obtenir l'année en cours afin qu'il n'y ait pas besoin de s'inquiéter de mettre cela à jour à nouveau.

```svelte
<p>
  Copyright &copy; {`${new Date().getFullYear()}`} - All right reserved
  by ME
</p>
```

Voici le fichier ajusté maintenant :

```svelte
<script>
  import FacebookIcon from './facebook-icon.svelte'
  import TwitterIcon from './twitter-icon.svelte'
  import YouTubeIcon from './you-tube-icon.svelte'
</script>

<footer
  class="p-10 footer bg-primary text-primary-content footer-center"
>
  <div class="grid grid-flow-col gap-4">
    <a class="link link-hover" href="/projects">Portfolio</a>
    <a class="link link-hover" href="/posts">Blog</a>
    <a class="link link-hover" href="/about">About</a>
  </div>
  <div>
    <div class="grid grid-flow-col gap-4">
      <a href="https://twitter.com">
        <TwitterIcon />
      </a>
      <a href="https://youtube.com">
        <YouTubeIcon />
      </a>
      <a href="https://facebook.com">
        <FacebookIcon />
      </a>
    </div>
  </div>
  <div>
    <p>
      Copyright &copy; {`${new Date().getFullYear()}`} - All right reserved
      by ME
    </p>
  </div>
</footer>

```

Avec les SVG importés, il y a beaucoup de bruit supprimé du fichier et il est beaucoup plus agréable à lire.

Maintenant que nous avons notre composant footer, nous allons vouloir qu'il persiste lors des changements de route (page). Le fichier `__layout.svelte` est l'endroit idéal pour cela, alors allons l'y ajouter :

```svelte
<script>
  import Footer from '$lib/components/footer.svelte'
  import '../app.css'
</script>

<main class="container max-w-3xl mx-auto px-4 mb-20">
  <slot />
</main>
<Footer />

```

Committons notre composant footer sur Git puis passons à la section suivante :

```git
git add .
git commit -m "Add footer component"
```

### Comment créer le composant Navbar

Maintenant pour le composant navbar, j'utiliserai l'avant-dernier des composants `navbar` de la section navbar des composants daisyUI. Voici à quoi il ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-50.png)

Il y a beaucoup de SVG dans cet exemple que je ne vais pas utiliser, je vais donc les supprimer. Gardez-les si vous préférez, mais par souci de lisibilité, je les supprimerai. Il suffit vraiment d'avoir des liens pour la page Portfolio, la page Blog et la page À propos.

Voici à quoi ressemble le balisage avec les SVG supprimés :

```svelte
<div
  class="navbar mb-2 shadow-lg bg-neutral text-neutral-content rounded-box"
>
  <div class="flex-1 px-2 mx-2">
    <span class="text-lg font-bold">Portfolio and Blog</span>
  </div>
  <div class="flex-none hidden px-2 mx-2 lg:flex">
    <div class="flex items-stretch">
      <a class="btn btn-ghost btn-sm rounded-btn" href="/projects">
        Portfolio
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/posts"
        >Blog</a
      >
      <a class="btn btn-ghost btn-sm rounded-btn" href="/about"
        >About</a
      >
    </div>
  </div>
</div>

```

Notez que j'ai ajouté des balises `href` ici pour pointer vers les différentes pages du projet.

Nous devrions ajouter cela au même endroit que le footer dans le fichier `__layout.svelte` afin que nous puissions voir les changements au fur et à mesure que nous construisons ce composant :

```svelte
<script>
  import Footer from '$lib/components/footer.svelte'
  import Navbar from '$lib/components/navbar.svelte'
  import '../app.css'
</script>

<Navbar />
<main class="container max-w-3xl mx-auto px-4 mb-20">
  <slot />
</main>
<Footer />
```

Quelques changements supplémentaires à ajouter maintenant : je vais augmenter `mb-2` jusqu'à `mb-16`, et je vais également supprimer `rounded-box` et le remplacer par une classe sticky afin que la navbar persiste lors du défilement de pages longues `sticky top-0 z-10`.

Une dernière chose à faire est de remplacer la balise `<span>` contenant « Portfolio and Blog » par une balise `a` afin que nous puissions revenir à la page d'accueil en cliquant dessus :

```svelte
<a class="text-lg font-bold" href="/">Portfolio and Blog</a>
```

Voici à quoi ressemble le fichier maintenant :

```svelte
<div
  class="navbar mb-16 shadow-lg bg-neutral text-neutral-content sticky top-0 z-10"
>
  <div class="flex-1 px-2 mx-2">
    <a class="text-lg font-bold" href="/">Portfolio and Blog</a>
  </div>

  <div class="flex-none hidden px-2 mx-2 lg:flex">
    <div class="flex items-stretch">
      <a class="btn btn-ghost btn-sm rounded-btn" href="/projects">
        Portfolio
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/posts"
        >Blog</a
      >
      <a class="btn btn-ghost btn-sm rounded-btn" href="/about"
        >About</a
      >
    </div>
  </div>
</div>

```

Très bien ! Mais attendez – qu'en est-il des tailles d'écran plus petites ? Vous avez peut-être remarqué que si vous êtes sur un écran plus petit, les liens pour Portfolio, Blog et About manquent.

Dans la classe du div conteneur des liens `flex-none hidden px-2 mx-2 lg:flex`, cela va masquer les éléments jusqu'à ce que la taille de l'écran atteigne le point d'arrêt large (`lg:`), puis l'affichage sera réglé sur `flex`.

Utilisons quelques classes daisyUI supplémentaires de la section dropdown pour les afficher lorsque la taille de l'écran est inférieure à `lg:` :

```svelte
<div class="dropdown dropdown-left lg:hidden">
  <div tabindex="0" class="m-1 btn">Links</div>
  <ul
    tabindex="0"
    class="bg-neutral rounded-box shadow text-neutral-content p-2 w-52 menu dropdown-content "
  >
    <a class="btn btn-ghost btn-sm rounded-btn" href="/projects">
      Portfolio
    </a>
    <a class="btn btn-ghost btn-sm rounded-btn" href="/posts">
      Blog
    </a>
    <a class="btn btn-ghost btn-sm rounded-btn" href="/about">
      About
    </a>
  </ul>
</div>
```

Ainsi, lorsque la taille de l'écran est inférieure au point d'arrêt Tailwind `lg:`, les classes `dropdown` ci-dessus seront affichées.

Voici à quoi ressemble le fichier complet :

```svelte
<div
  class="navbar mb-16 shadow-lg bg-neutral text-neutral-content sticky top-0 z-10"
>
  <div class="flex-1 px-2 mx-2">
    <a class="text-lg font-bold" href="/">Portfolio and Blog</a>
  </div>

  <div class="dropdown dropdown-left lg:hidden">
    <div tabindex="0" class="m-1 btn">Links</div>
    <ul
      tabindex="0"
      class="bg-neutral rounded-box shadow text-neutral-content p-2 w-52 menu dropdown-content "
    >
      <a class="btn btn-ghost btn-sm rounded-btn" href="/projects">
        Portfolio
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/posts">
        Blog
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/about">
        About
      </a>
    </ul>
  </div>

  <div class="flex-none hidden px-2 mx-2 lg:flex">
    <div class="flex items-stretch">
      <a class="btn btn-ghost btn-sm rounded-btn" href="/projects">
        Portfolio
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/posts"
        >Blog</a
      >
      <a class="btn btn-ghost btn-sm rounded-btn" href="/about"
        >About</a
      >
    </div>
  </div>
</div>

```

Génial ! Nous avons maintenant un menu de navigation réactif pour les utilisateurs mobiles.

Il est temps de committer les changements que nous avons faits sur Git :

```git
git add .
git commit -m "Add navbar component"
```

Footer et navbar réglés, passons maintenant au sélecteur de thème.

## **Comment ajouter un sélecteur de thème**

Tous les sites modernes ont un sélecteur de thème, alors jetons un coup d'œil à l'implémentation de cela sur notre site. Saadeghi (le créateur de daisyUI) a créé un package vraiment sympa pour s'occuper de cela pour nous appelé [`theme-change`](https://github.com/saadeghi/theme-change), nous devrions donc l'installer maintenant :

```bash
npm i -D theme-change
```

Maintenant, nous pouvons l'utiliser dans le fichier `__layout.svelte` comme ceci :

```svelte
<script>
  import Footer from '$lib/components/footer.svelte'
  import Navbar from '$lib/components/navbar.svelte'
  import { onMount } from 'svelte'
  import { themeChange } from 'theme-change'
  import '../app.css'

  onMount(async () => {
    themeChange(false)
  })
</script>

<Navbar />
<main class="container max-w-3xl mx-auto px-4 mb-20">
  <slot />
</main>
<Footer />
```

Décomposons cela et voyons ce qui se passe ici. Le `onMount` est un code exécuté une fois que la page est visible dans le navigateur (une fois qu'elle est chargée/montée). Une fois la page chargée, nous initialisons `themeChange`. Cela changera le `data-act-class` pour le thème souhaité.

Actuellement, il n'y a aucun moyen de le définir, changeons cela maintenant sur le fichier `src/app.html` :

```html
<!DOCTYPE html>
<html lang="en" data-theme="dracula">
  <head>
    <meta charset="utf-8" />
    <meta name="description" content="" />
    <link rel="icon" href="/favicon.png" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1"
    />
    %svelte.head%
  </head>
  <body>
    <div id="svelte">%svelte.body%</div>
  </body>
</html>

```

Ici, nous ajoutons le thème par défaut Dracula sur le `html` conteneur pour tout le projet avec `data-theme="dracula"`. Vous pouvez jouer avec cela avec tous les thèmes fournis par daisyUI – essayez de changer `dracula` en `corporate` et voyez-le changer !

Ok, c'est bien, mais comment puis-je le changer ? C'est vrai – faisons cela maintenant. Plutôt que de remplir l'article avec plus de code, je vais faire un lien vers un dépôt GitHub qui l'a déjà packagé pour nous dans [SvelteKit theme switch](https://github.com/spences10/sveltekit-theme-switch/blob/main/src/lib/theme-select.svelte). Ce composant est un élément select HTML qui liste tous les thèmes daisyUI.

Copiez le contenu de ce fichier et ajoutez-le à un composant `theme-select.svelte`, qui n'existe pas encore – alors, créons-le maintenant :

```bash
touch src/lib/components/theme-select.svelte
```

Supprimez le `class="mb-8"` du div conteneur et ajoutez quelques styles supplémentaires à l'élément select. Voici le diff :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/image-55.png)

Maintenant que nous avons un composant de sélection de thème, nous devrions l'ajouter quelque part accessible dans tout le projet. Où pensez-vous que cela devrait aller ? Vous l'avez deviné – le fichier `navbar.svelte` :

```svelte
<script>
  import ThemeSelect from './theme-select.svelte'
</script>

<div
  class="navbar mb-16 shadow-lg bg-neutral text-neutral-content sticky top-0 z-10"
>
  <div class="flex-1 px-2 mx-2">
    <a class="text-lg font-bold" href="/"> Portfolio and Blog </a>
  </div>

  <div class="dropdown dropdown-left lg:hidden">
    <div tabindex="0" class="m-1 btn">Links</div>
    <ul
      tabindex="0"
      class="bg-neutral rounded-box shadow text-neutral-content p-2 w-52 menu dropdown-content "
    >
      <a class="btn btn-ghost btn-sm rounded-btn" href="/projects">
        Portfolio
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/posts">
        Blog
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/about">
        About
      </a>
    </ul>
  </div>

  <div class="flex-none hidden px-2 mx-2 lg:flex">
    <div class="flex items-stretch">
      <a class="btn btn-ghost btn-sm rounded-btn" href="/projects">
        Portfolio
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/posts">
        Blog
      </a>
      <a class="btn btn-ghost btn-sm rounded-btn" href="/about">
        About
      </a>
      <div class="px-4">
        <ThemeSelect />
      </div>
    </div>
  </div>
</div>

```

Ici, nous importons le composant `ThemeSelect` et ajoutons un div conteneur pour la sélection du thème à la fin de notre liste de pages.

Vous pouvez également l'ajouter pour qu'il soit disponible sur la vue mobile si vous le souhaitez.

Committez les changements sur Git :

```git
git add .
git commit -m "Add theme select to navbar"
```

## Comment ajouter la page À propos

Ajoutons cette page à propos vers laquelle nous faisons un lien dans la navbar.

```bash
touch src/routes/about.svelte
```

Dans cette page, nous pouvons utiliser la requête `authorsQuery` que nous avons créée pour la page d'accueil afin d'afficher les informations sur l'auteur. Voici le fichier complet :

```svelte
<script context="module">
  import { client } from '$lib/graphql-client'
  import { authorsQuery } from '$lib/graphql-queries'
  import { marked } from 'marked'

  export const load = async () => {
    const { authors } = await client.request(authorsQuery)

    return {
      props: {
        authors,
      },
    }
  }
</script>

<script>
  export let authors
  const {
    name,
    intro,
    bio,
    picture: { url },
  } = authors[0]
</script>

<svelte:head>
  <title>My Portfolio project | About {name}</title>
</svelte:head>

<h1 class="font-bold text-center mb-20 text-5xl">About Me</h1>

<div class="flex mb-40 items-end">
  <div class="mr-6">
    <h2 class="text-3xl mb-4 font-bold tracking-wider">{name}</h2>
    <p class="text-xl mb-4">{intro}</p>
  </div>

  <img class="mask mask-squircle h-48" src={url} alt={name} />
</div>

<article div class="prose prose-lg">
  {@html marked(bio)}
</article>
```

Maintenant, committez ces changements sur Git :

```git
git add .
git commit -m "Add about page"
```

## Comment créer un sitemap

**FACULTATIF** : Informez les moteurs de recherche de ce qui se trouve sur votre site. Un sitemap aidera les robots d'indexation à connaître le contenu de votre site.

J'ai écrit un [article détaillé](https://scottspence.com/posts/make-a-sitemap-with-sveltekit) sur la façon de créer un sitemap avec SvelteKit si vous voulez regarder cela plus en détail.

Il s'agit d'un endpoint SvelteKit qui renverra un fichier XML détaillant le contenu du site.

Si vous voulez en créer un, créez un fichier pour cela :

```bash
touch src/routes/sitemap.xml.js
```

Voici le fichier complet :

```js
import { client } from '$lib/graphql-client'
import { gql } from 'graphql-request'

const website = 'https://www.myporfolioproject.com'

export const get = async () => {
  const query = gql`
    query Posts {
      posts {
        title
        slug
      }
    }
  `
  const { posts } = await client.request(query)
  const pages = [`about`]
  const body = sitemap(posts, pages)

  const headers = {
    'Cache-Control': 'max-age=0, s-maxage=3600',
    'Content-Type': 'application/xml',
  }
  return {
    headers,
    body,
  }
}

const sitemap = (
  posts,
  pages
) => `<?xml version="1.0" encoding="UTF-8" ?>
<urlset
  xmlns="https://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:news="https://www.google.com/schemas/sitemap-news/0.9"
  xmlns:xhtml="https://www.w3.org/1999/xhtml"
  xmlns:mobile="https://www.google.com/schemas/sitemap-mobile/1.0"
  xmlns:image="https://www.google.com/schemas/sitemap-image/1.1"
  xmlns:video="https://www.google.com/schemas/sitemap-video/1.1"
>
  <url>
    <loc>${website}</loc>
    <changefreq>daily</changefreq>
    <priority>0.7</priority>
  </url>
  ${pages
    .map(
      page => `
  <url>
    <loc>${website}/${page}</loc>
    <changefreq>daily</changefreq>
    <priority>0.7</priority>
  </url>
  `
    )
    .join('')}
  ${posts
    .map(
      post => `
  <url>
    <loc>${website}/posts/${post.slug}</loc>
    <changefreq>daily</changefreq>
    <priority>0.7</priority>
  </url>
  `
    )
    .join('')}
</urlset>`

```

Ceci est une version simplifiée pour générer un sitemap. Si vous voulez la version complète, vous pouvez consulter le [code source du projet](https://github.com/GraphCMS/graphcms-sveltekit-portfolio-and-blog-starter).

Un peu plus de détails sur ce fichier maintenant. De la même manière que nous pouvons avoir des pages et des composants dans SvelteKit, nous pouvons également avoir des endpoints. Les endpoints dans SvelteKit peuvent gérer des méthodes HTTP comme get, post et delete.

Une petite note sur la notation du fichier ici : le `.xml.js` peut sembler un peu étrange. C'est pour que SvelteKit puisse comprendre le type de retour de l'endpoint. Dans ce cas, nous voulons renvoyer du XML, mais il existe d'autres types que vous pouvez utiliser, comme le JSON.

Dans cette fonction, nous définissons une fonction `get`, ajoutons une requête GraphQL pour les articles, puis renvoyons les articles de la requête pour les utiliser dans le XML.

### Comment utiliser un endpoint SvelteKit

Maintenant que nous avons défini notre endpoint dans `src/routes/sitemap.xml.js`, nous pouvons accéder aux données immédiatement. En allant sur cette route dans le navigateur, nous pouvons voir les données renvoyées par cet endpoint.

Depuis le navigateur, allez sur `localhost:3000/sitemap.xml` – cela nous donnera les données provenant de l'API GraphQL de notre projet GraphCMS.

## **Robots.txt**

**FACULTATIF** : Informez les robots des moteurs de recherche de ce qu'il faut indexer. Cela indique aux robots d'indexation comme le Googlebot ce qu'il faut indexer ou non sur votre site.

Les pages que vous pourriez ne pas vouloir indexer pourraient être des choses comme un panneau d'administration ou une page de paramètres.

Le robots.txt peut aller dans le dossier static. Créons le fichier maintenant :

```bash
touch static/robots.txt
```

Dans le cas de ce projet, il n'y a pas de problème à ce que le Googlebot explore tout. Notre fichier `robots.txt` peut donc ressembler à ceci :

```txt
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:
```

Cela indique au robot d'indexation d'indexer tout ce qui se trouve sur le site.

## **Génération de flux RSS**

**FACULTATIF** : Permettez aux utilisateurs de voir les modifications apportées à votre site dans leurs applications RSS. Encore une fois, je vous laisse le soin de l'implémenter. De la même manière que le sitemap a été créé, vous pouvez implémenter un endpoint SvelteKit pour générer le XML nécessaire à un flux RSS.

```bash
touch src/routes/rss.xml.js
```

Voici un exemple de fichier :

```js
import { client } from '$lib/graphql-client'
import { gql } from 'graphql-request'

const name = 'My Portfolio'
const website = 'https://myportfolio.com'

export const get = async () => {
  const query = gql`
    query Posts {
      posts {
        title
        slug
      }
    }
  `
  const { posts } = await client.request(query)
  const body = xml(posts)

  const headers = {
    'Cache-Control': 'max-age=0, s-maxage=3600',
    'Content-Type': 'application/xml',
  }
  return {
    headers,
    body,
  }
}

const xml =
  posts => `<rss xmlns:dc="https://purl.org/dc/elements/1.1/" xmlns:content="https://purl.org/rss/1.0/modules/content/" xmlns:atom="https://www.w3.org/2005/Atom" version="2.0">
  <channel>
    <title>${name}</title>
    <link>${website}</link>
    <description>This is my portfolio!</description>
    ${posts
      .map(
        post =>
          `
        <item>
          <title>${post.title}</title>
          <description>This is my portfolio!</description>
          <link>${website}/posts/${post.slug}/</link>
          <pubDate>${new Date(post.date)}</pubDate>
          <content:encoded>${post.previewHtml} 
            <div style="margin-top: 50px; font-style: italic;">
              <strong>
                <a href="${website}/posts/${post.slug}">
                  Keep reading
                </a>
              </strong>  
            </div>
          </content:encoded>
        </item>
      `
      )
      .join('')}
  </channel>
</rss>`

```

Il y a beaucoup à déballer là-dedans, j'ai donc écrit un article détaillé sur la [configuration d'un flux RSS sur votre site SvelteKit](https://scottspence.com/posts/make-an-rss-feed-with-sveltekit). Cela vous donnera toutes les informations dont vous avez besoin pour vous lancer.

## **Inscription par e-mail avec Revue**

**FACULTATIF** : Si vous voulez aller plus loin avec les endpoints, vous pouvez ajouter une page d'inscription à la newsletter en utilisant l'API Revue. J'ai [détaillé cela dans un article](https://scottspence.com/posts/email-form-submission-with-sveltekit) si vous voulez prendre cette voie.

Il y a aussi une excellente [vidéo de WebJeda](https://www.youtube.com/watch?v=mBXEnakkUIM) sur la collecte de données de formulaires Google dans un projet SvelteKit si vous préférez cette option.

## **Déploiement continu avec Vercel**

Si vous avez suivi jusqu'ici (merci d'ailleurs 🙏), vous vous demandez peut-être pourquoi nous avons fait des Git Commits à la fin de chaque section. Eh bien, tout cela menait à cette section.

J'utiliserai [Vercel](https://vercel.com) pour le déploiement. Si vous n'avez pas encore de compte, vous pouvez vous [inscrire](https://vercel.com/signup) avec votre fournisseur préféré – j'utiliserai GitHub.

Si vous voulez déployer votre site tel quel, dès maintenant, vous pouvez utiliser le CLI Vercel en utilisant :

```bash
npx vercel
```

Pas besoin d'installer le CLI, car tout est fait pour vous avec la commande npx. Vous serez guidé tout au long du déploiement par le CLI.

Voici la sortie de l'exécution de la commande en sélectionnant la valeur par défaut pour chaque question (entrée) :

```bash
? Set up and deploy “~/repos/my-developer-portfolio”? [Y/n] y
? Which scope do you want to deploy to? Scott Spence
? Link to existing project? [y/N] n
? What’s your project’s name? my-developer-portfolio
? In which directory is your code located? ./
Auto-detected Project Settings (SvelteKit):
- Build Command: svelte-kit build
- Output Directory: public
- Development Command: svelte-kit dev --port $PORT
? Want to override the settings? [y/N] n
🔗 Linked to spences10/my-developer-portfolio (created .vercel and added it to .gitignore)
🔍 Inspect: https://vercel.com/spences10/my-developer-portfolio/78bRRjiweZsipYbu8Q4Bg9JRmvGR [2s]
```

Maintenant, en allant sur l'URL du CLI indiquée par `🔍 Inspect`, je peux regarder le projet en cours de construction sur Vercel. Super, notre site est opérationnel ! Il s'agit cependant d'un déploiement ponctuel, donc s'il y a des changements futurs, je devrai à nouveau utiliser le CLI.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-10.png)
_Page de prévisualisation du déploiement Vercel_

Vous avez peut-être remarqué sur la page de prévisualisation du déploiement sur Vercel qu'il y a une section qui dit « No repository ».

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-11.png)

Nous pouvons ajouter un dépôt GitHub afin que tous les changements futurs apportés au projet soient construits lorsque les modifications sont poussées sur GitHub.

Donc, tout d'abord, nous devons ajouter notre projet sur GitHub – faisons cela maintenant. Si vous êtes déjà connecté à GitHub, vous pouvez aller sur le [lien du nouveau dépôt](https://github.com/new) que vous pouvez obtenir en cliquant sur l'icône plus dans le coin supérieur droit de GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-12.png)
_Lien vers le nouveau dépôt_

Dans la nouvelle page, ajoutez les détails du projet :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-13.png)
_Nouveau projet GitHub avec description_

Ensuite, cliquez sur le bouton « Create repository » :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-14.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-15.png)

L'écran suivant vous donnera les commandes Git dont vous avez besoin. Comme le projet est déjà créé, je peux utiliser le deuxième ensemble de commandes :

```bash
git remote add origin git@github.com:spences10/my-developer-portfolio.git
git branch -M main
git push -u origin main
```

Notez que si vous suivez, vous devrez prendre les commandes qui vous sont données sur la page de votre dépôt plutôt que d'utiliser celles mentionnées ici, car celles-ci pointeront vers mon GitHub `spences10`.

Maintenant que le dépôt est créé sur GitHub, je peux le connecter à Vercel. Depuis la page de prévisualisation du déploiement, je peux sélectionner le projet en cliquant sur le nom du projet dans l'en-tête :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-16.png)

Cela m'amènera au tableau de bord du projet :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-17.png)
_Tableau de bord du projet Vercel_

De là, je peux cliquer sur le bouton « Connect Git repository » qui m'amènera à la section Git dans les paramètres du projet :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-18.png)
_Connecter un dépôt Git dans le menu des paramètres Vercel_

Cliquer sur GitHub affichera une liste de projets :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-19.png)
_Sélectionner le dépôt GitHub à lier_

Cliquer sur le bouton « Connect » connectera le dépôt. Vous avez peut-être également remarqué le paramètre « Domains » ici. Vous pouvez configurer votre domaine ici ou changer le nom actuel avec un domaine `.vercel.app`.

Une autre chose à noter ici est la section « Environment Variables » dans les paramètres. Il faudra y ajouter la variable d'environnement `VITE_GRAPHQL_API` :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-20.png)
_Ajouter la variable d'environnement VITE_GRAPHQL_API dans les paramètres Vercel_

Maintenant, chaque fois que des modifications sont poussées sur GitHub, Vercel construira le site.

## Comment publier et construire sur les changements de contenu

Plutôt que de devoir pousser un changement sur GitHub pour créer un nouveau build du projet lorsque seul le contenu a changé, vous pouvez le faire avec une intégration GraphCMS.

Depuis le panneau Settings de GraphCMS, allez dans la section integrations :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-21.png)
_Sélectionner la section des intégrations dans le panneau des paramètres_

Cliquez sur l'intégration Vercel – il existe également des intégrations pour Netlify et Gatsby Cloud :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-26.png)
_Cliquer sur l'intégration Vercel_

Cliquez sur « Enable » pour l'intégration Vercel :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-23.png)
_Activer l'intégration Vercel_

Cliquez sur le bouton « Connect to Vercel » lorsque vous y êtes invité :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-24.png)

Cliquez sur « Authorise GraphCMS » pour effectuer des déploiements pour vous sur Vercel :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-25.png)

Dans la section « Build projects », sélectionnez votre projet Vercel dans la liste déroulante. Le « Display name » est ce qui apparaîtra dans le panneau latéral de vos pages de contenu. Le nom de la branche est la branche à partir de laquelle vous voulez déployer sur Vercel depuis GitHub – j'utilise `main` pour la branche de production.

Il existe également une option pour spécifier les modèles sur lesquels vous souhaitez activer l'intégration. Dans ce cas, je les utilise tous, donc je sélectionne « Select all » puis je clique enfin sur le bouton « Enable » :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-28.png)

Si je vais maintenant dans la section content du projet GraphCMS et que je sélectionne un modèle de contenu pour modifier une entrée, il y a un bouton « Start building Production » qui lancera un nouveau build chaque fois qu'il sera cliqué.

Voici le modèle Author et l'intégration Vercel sur le panneau de droite :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-29.png)

## Google Search Console

**FACULTATIF** : C'est une étape facultative si vous possédez votre propre domaine. Un bon moyen de faire classer votre site sur les moteurs de recherche est d'utiliser la Google Search Console.

[https://search.google.com/search-console](https://search.google.com/search-console)

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-32.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-33.png)

Ajoutez l'enregistrement TXT à votre domaine en utilisant le CLI Vercel. Vous pouvez également l'ajouter manuellement dans la section domains de Vercel :

```bash
vercel dns add my-developer-portfolio.com @ TXT google-site-verification=g99pqa_kSHiq6AzLtk4HF00tyJhQVt1gGzfUoJQrTPQ
```

Une fois votre site vérifié, vous pouvez ajouter votre sitemap et cliquer sur le bouton submit.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-34.png)
_Ajouter le sitemap à la Google Search Console_

C'est tout ! Vous devrez maintenant attendre que le Googlebot fasse son travail et indexe votre site. Vous devriez commencer à voir des requêtes de recherche arriver au fil du temps.

## **Ressources**

Voici quelques-unes des ressources que j'ai utilisées pour créer le contenu du blog que j'ai créé tout au long de ce guide.

* Images avec [Lorem.space - générateur d'images de remplacement](https://lorem.space/api)
* Markdown avec [Lorem Markdownum (jaspervdj.be)](https://jaspervdj.be/lorem-markdownum/)
* Génération de biographie avec [Character Biography Generator (character-generator.org.uk)](https://www.character-generator.org.uk/bio/)
* Tailles idéales des images de couverture : [The Ideal Cover Photo Size for Each of the Major Social Media Platforms (buffer.com)](https://buffer.com/library/ideal-cover-photo-size/)

Vous pouvez consulter ces liens pour plus d'informations sur Svelte et SvelteKit

* [https://kit.svelte.dev/docs](https://kit.svelte.dev/docs)
* [https://svelte.dev/docs](https://svelte.dev/docs)

Si vous voulez le code source de ce projet, vous pouvez consulter le dépôt GitHub [pour tout le code](https://github.com/GraphCMS/graphcms-sveltekit-portfolio-and-blog-starter). Si vous rencontrez des problèmes, n'hésitez pas à ouvrir une issue ou à me contacter sur [Twitter](https://twitter.com/spences10).

## Ce que nous avons accompli

Il est temps de récapituler ce que nous avons accompli ici. Nous sommes allés du « hello world » jusqu'à un portfolio et un blog complets !

Nous avons couvert la récupération de données à partir d'une API GraphQL et l'affichage de ces données sur une page du projet. Nous avons ensuite implémenté un client GraphQL pour ne récupérer que les données dont nous avions besoin.

Nous avons ajouté le sitemap, si important pour que le site puisse être découvert et indexé par les moteurs de recherche comme Google.

Une touche facultative a été d'ajouter un flux RSS afin que toute personne utilisant un lecteur RSS puisse être informée de tout nouveau contenu ajouté au site.

Enfin, nous avons déployé notre projet terminé sur Vercel pour que le monde entier puisse le voir.

## Merci

Merci beaucoup d'avoir pris le temps de parcourir ce guide. J'espère qu'il vous a donné tout ce dont vous avez besoin pour commencer à créer vos propres projets avec Svelte.

Si vous aimez le contenu, vous pouvez en découvrir beaucoup plus de ma part sur mon [blog](https://scottspence.com) ou vous pouvez me suivre sur [Twitter](https://twitter.com/spences10).