---
title: Comment déployer des applications Next.js sur GitHub Pages
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-01-24T22:46:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-next-js-app-to-github-pages
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Splash.png
tags:
- name: deployment
  slug: deployment
- name: GitHub Actions
  slug: github-actions
- name: github pages
  slug: github-pages
- name: Next.js
  slug: nextjs
seo_title: Comment déployer des applications Next.js sur GitHub Pages
seo_desc: "In this article, I will walk you through the process of publishing a Next.js\
  \ application on GitHub Pages. \nWhat makes this guide particularly helpful is that\
  \ I'll teach you how to integrate with GitHub Actions, too. This means your application\
  \ will b..."
---

Dans cet article, je vais vous guider à travers le processus de publication d'une application Next.js sur GitHub Pages. 

Ce qui rend ce guide particulièrement utile, c'est que je vais vous apprendre à intégrer GitHub Actions. Cela signifie que votre application sera automatiquement déployée chaque fois que vous pousserez du code vers votre dépôt GitHub.

Nous nous concentrerons uniquement sur le déploiement plutôt que sur la construction de l'ensemble de l'application Next.js à partir de zéro. Pour notre projet d'exemple, nous utiliserons celui d'un article précédent que j'ai écrit sur freeCodeCamp dans mon article [Comment construire le jeu 2048 en React](https://www.freecodecamp.org/news/how-to-make-2048-game-in-react/). J'ai récemment mis à jour le code pour utiliser React 18 et ajouté le framework Next.js.

Si vous souhaitez voir le résultat final avant de lire l'article complet, vous pouvez [le consulter ici](https://mateuszsokola.github.io/2048-in-react/).

Comme je l'ai mentionné ci-dessus, nous utilisons un projet que j'ai créé dans mon tutoriel précédent – et pour que vous puissiez l'utiliser ici, vous pouvez trouver son [code source sur GitHub](https://github.com/mateuszsokola/2048-in-react/). N'hésitez pas à cloner ou forker ce dépôt, et suivez simplement les étapes du tutoriel pour le faire avec moi. 

## Prérequis

Avant de commencer, assurez-vous de connaître un peu React et Next.js. Nous utiliserons également GitHub, il est donc important de comprendre quelques bases. Vous n'avez pas besoin d'être un expert, il suffit d'avoir une expérience de base avec ces technologies.

## Brève introduction

Aujourd'hui, nous allons explorer deux nouvelles choses – GitHub Actions et GitHub Pages. Si vous n'en avez pas entendu parler, laissez-moi vous expliquer rapidement :  
  
**GitHub Actions** sont comme de petits workflows qui peuvent effectuer des tâches sur vos projets. C'est comme avoir un assistant qui fait automatiquement ce que vous lui dites de faire. Vous pouvez utiliser Actions pour exécuter des tests, des vérifications de qualité, ou pour construire votre application. Dans notre cas, nous allons utiliser ces workflows pour publier mon [jeu 2048](https://mateuszsokola.github.io/2048-in-react/) sur GitHub Pages.

Maintenant, qu'est-ce que **GitHub Pages** ? Imaginez-les comme une option d'hébergement web pour les développeurs et les projets open source. Vous pouvez utiliser GitHub Pages pour partager vos portfolios, héberger des sites web de vos projets open source, ou simplement publier vos projets personnels comme nous le faisons aujourd'hui.  
  
Si vous souhaitez en savoir plus, vous pouvez lire davantage sur leurs sites officiels :

* [GitHub Actions](https://github.com/features/actions)
* [GitHub Pages](https://pages.github.com/)

Maintenant, mettons-nous au travail.

## Étape 1 – Activer GitHub Pages pour votre dépôt

Pour publier notre application Next.js, nous devons activer GitHub Pages pour notre dépôt. Naviguons vers l'onglet Paramètres (1 dans l'image ci-dessous), sélectionnons _Pages_ dans le menu de gauche (2), et trouvons le menu déroulant qui nous permet de spécifier la source de déploiement _Source_ (3).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/GH-Pages---Step-1a.png)
_Paramètres du projet GitHub_

Maintenant, changeons la source de déploiement _Source_ en _GitHub Actions_.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/GH-Pages---Step-1b.png)
_Paramètres du projet GitHub – Configuration de GitHub Pages_

À partir de maintenant, notre projet a une page dédiée. Nous devons simplement créer une action qui publiera le contenu là-bas.

## Étape 2 – Configurer le processus de construction de Next.js

Avant de déployer l'application Next.js, il est important de changer la sortie de construction. Par défaut, Next.js utilise Node.js pour exécuter l'application, ce qui est incompatible avec GitHub Pages. 

GitHub Pages est conçu pour héberger des fichiers statiques, ce qui signifie que nous ne pouvons publier que du HTML, du CSS, du JavaScript (et d'autres fichiers statiques) là-bas. Nous devons donc activer la génération de pages statiques dans Next.js. 

Pour ce faire, nous allons changer le mode de sortie en `export` dans `next.config.js` :

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "export",  // <=== active les exports statiques
  reactStrictMode: true,
};

module.exports = nextConfig;
```

Maintenant, après avoir exécuté `next build`, Next.js générera un dossier `out` contenant les actifs statiques de notre application. Dans les étapes suivantes, nous prendrons ce répertoire et le téléverserons sur GitHub Pages.

Note pour les développeurs expérimentés de Next.js : vous pouvez utiliser [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) et [`getStaticPaths`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths) pour générer des fichiers statiques pour chaque page dans votre répertoire `pages`.

## Étape 3 – Configurer le chemin de base pour corriger les images manquantes

GitHub publie les Pages sous un sous-chemin d'un domaine et prend le nom du projet comme sous-chemin. Cela semble confus, alors prenons l'URL de mon jeu 2048 comme exemple :

```bash
https://mateuszsokola.github.io/2048-in-react/
```

Comme vous pouvez le voir, GitHub m'a assigné un sous-domaine dédié appelé _mateuszsokola_ (d'après mon nom d'utilisateur). Mais le projet est publié sous le sous-chemin, qui dans mon cas est `/2048-in-react`. Malheureusement, cela entraînera des problèmes avec les images et les styles manquants. 

Par défaut, Next.js mappe tous les actifs statiques au domaine. Cela signifie que le fichier `favicon.ico` sera résolu en `mateuszsokola.github.io/favicon.ico` au lieu de `mateuszsokola.github.io/2048-in-react/favicon.icon`. 

Pour corriger cela, nous pouvons configurer un préfixe de chemin en ajoutant `basePath` dans le fichier `next.config.js` :

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  basePath: "/2048-in-react",
  output: "export",
  reactStrictMode: true,
};

module.exports = nextConfig;
```

Dans mon cas, c'est `/2048-in-react` puisque mon projet s'appelle `2048-in-react`.   
**N'oubliez pas d'inclure le (`/`) au début du chemin.**

## Étape 4 – Configurer GitHub Actions

Maintenant, il est temps de configurer GitHub Actions pour le déploiement de Next.js. La réutilisabilité est une bonne pratique, donc j'ai divisé le déploiement en deux actions distinctes :

* Action `setup-node` – Cette action est responsable de la configuration de Node.js et de l'installation de toutes les dépendances. Avoir une action autonome pour la configuration de Node.js nous permet de la réutiliser pour d'autres pipelines. Par exemple, dans mon jeu 2048, j'ai des pipelines qui exécutent un [linter de code](https://github.com/mateuszsokola/2048-in-react/blob/master/.github/workflows/lint.yml) et des [tests](https://github.com/mateuszsokola/2048-in-react/blob/master/.github/workflows/test.yml). Vous aurez probablement plus d'une action également.
* Action `publish` – Cette action gère le processus de construction et publie l'application Next.js sur GitHub Pages chaque fois que nous fusionnons du code dans la branche `main`.

Maintenant, vous pouvez comprendre pourquoi il est bénéfique de diviser le déploiement en deux actions. 

Commençons par expliquer l'action `setup-node`. Voici le code :

```yml
# Fichier : .github/workflows/setup-node/action.yml
name: setup-node
description: "Configurer Node.js \u2699\ufe0f - Mettre en cache les dépendances \u26a1 - Installer les dépendances \ud83d\udd27"
runs:
  using: "composite"
  steps:
    - name: Configurer Node.js \u2699\ufe0f
      uses: actions/setup-node@v4
      with:
        node-version: 20

    - name: Mettre en cache les dépendances \u26a1
      id: cache_dependencies
      uses: actions/cache@v3
      with:
        path: node_modules
        key: node-modules-${{ hashFiles('package-lock.json') }}

    - name: Installer les dépendances \ud83d\udd27
      shell: bash
      if: steps.cache_dependencies.outputs.cache-hit != 'true'
      run: npm ci
```

**Important** : Placez ce fichier dans le répertoire `.github/workflows/setup-node` de votre projet. Assurez-vous de nommer le fichier `action.yml`.

Que fait ce code ?

* Il déclare une action `composite`. L'action `composite` vous permet de regrouper plusieurs étapes de workflow en une seule action, combinant plusieurs commandes d'exécution en une seule action réutilisable.
* Il crée un nouvel environnement de construction et configure Node.js 20.
* Il installe les dépendances npm et utilise un mécanisme de mise en cache pour accélérer ce processus.

Ce sont les parties les plus importantes de l'action `setup-node`. Passons maintenant à la dernière action, qui est `publish`.

```yml
# Fichier : .github/workflows/publish.yml
name: publish-to-github-pages
on:
  push:
    branches:
      - master

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout \ud83d\udece\ufe0f
        uses: actions/checkout@v4

      - name: Configurer Node.js \u2699\ufe0f - Mettre en cache les dépendances \u26a1 - Installer les dépendances \ud83d\udd27
        uses: ./.github/workflows/setup-node

      - name: Configurer Pages \u2699\ufe0f
        uses: actions/configure-pages@v4
        with:
          static_site_generator: next

      - name: Construire avec Next.js \ud83c\udfd7\ufe0f
        run: npx next build

      - name: Télécharger l'artefact \ud83d\udce1
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./out

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    runs-on: ubuntu-latest
    needs: build

    steps:
      - name: Publier sur GitHub Pages \ud83d\ude80
        id: deployment
        uses: actions/deploy-pages@v4
```

Placez ce fichier dans le répertoire `.github/workflows` de votre projet. Vous pouvez nommer le fichier comme vous le souhaitez – je l'ai appelé `publish.yml`.

Que fait ce code ?

* Cette action est exécutée lorsque du code est poussé ou fusionné dans la branche `main`.
* Elle utilise l'action `setup-node` pour configurer l'environnement.
* L'action a deux étapes : dans la première étape, l'application Next.js est bundlée. Dans la deuxième étape, nous téléchargeons les artefacts de la première étape vers GitHub Pages.

Ce sont les aspects les plus importants du pipeline de déploiement. J'ai sauté la configuration des permissions et de la concurrency car elles restent inchangées pour tous les déploiements. 

Maintenant, votre action est prête à être utilisée.

## Commit et Push 

Après avoir commité et poussé vos changements vers la branche `main`, GitHub lancera automatiquement le déploiement vers GitHub Pages. 

Pour inspecter le processus, naviguez vers l'onglet _Actions_ (1 dans l'image ci-dessous), et sélectionnez l'action _publish-to-github-pages_ dans le menu de gauche (2). Vous verrez tous vos déploiements à l'écran (ils sont appelés _workflows_).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/GH-Pages---Summary.png)
_GitHub Actions – Workflows responsables de la publication sur GitHub Pages_

Maintenant, nous devons sélectionner le premier de ces workflows, et vous verrez un déploiement en deux étapes. Dans l'étape _deploy_, vous pouvez trouver un lien vers votre site web sur GitHub Pages.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/GH-Pages---SummaryCI.png)
_Workflow du projet GitHub – Déploiement réussi_

## **Conclusion**

GitHub Pages n'est pas suffisant pour héberger des sites web avec des millions de vues. Mais c'est un excellent choix pour construire votre portfolio ou héberger un site web pour votre projet open source. 

De nos jours, il existe de nombreuses options gratuites pour héberger nos sites web, mais je voulais vous montrer cette alternative. GitHub Pages est construit par des développeurs pour des développeurs – vous pouvez le considérer comme l'habitat naturel d'un développeur. Je pense que chaque développeur devrait être familier avec cela.

J'espère que cet article sera une douce poussée vers l'apprentissage de GitHub Actions. N'hésitez pas à expérimenter différentes approches et essayez de créer les vôtres. Chaque application doit être livrée et considérez cet article comme un point de départ.

Voici les ressources :

* [Jeu 2048 sur GitHub Pages](https://mateuszsokola.github.io/2048-in-react/)
* [Code source sur GitHub](https://github.com/mateuszsokola/2048-in-react/). Cela signifierait beaucoup pour moi si vous mettez une étoile \u2b50 à ce dépôt.

Si cet article vous a aidé, faites-le moi savoir sur [Twitter](https://twitter.com/msokola). Les éducateurs, comme moi, ont souvent l'impression de parler dans le vide et que personne ne se soucie de ce que nous enseignons. Un simple "shoutout" montre que cela valait l'effort et m'inspire à travailler encore plus dur pour créer plus de contenu comme celui-ci.

N'hésitez pas à partager cet article sur vos réseaux sociaux. 

Merci.

Si vous souhaitez en savoir plus sur moi – Je m'appelle Matéush. Je suis ingénieur logiciel et nomade numérique. Je peux dire que j'ai une carrière extraordinaire. J'ai vécu dans trois pays différents et travaillé dans divers environnements, des startups aux grandes entreprises. 

Récemment, j'ai commencé à partager des conseils sur [la croissance d'une carrière de développeur logiciel](https://www.mateu.sh/?ref=freecodecamp.org). Je crois avoir créé mon blog pour mon moi plus jeune – un peu perdu, motivé à devenir l'un des meilleurs développeurs, et cherchant un chemin vers le monde de la "big tech".