---
title: Comment configurer un flux CI/CD léger et agnostique avec GitHub Actions
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-10-29T12:13:14.000Z'
originalURL: https://freecodecamp.org/news/a-lightweight-tool-agnostic-ci-cd-flow-with-github-actions
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/cover-3.png
tags:
- name: continuous delivery
  slug: continuous-delivery
- name: Continuous Integration
  slug: continuous-integration
- name: GitHub
  slug: github
- name: tools
  slug: tools
seo_title: Comment configurer un flux CI/CD léger et agnostique avec GitHub Actions
seo_desc: 'Agnostic tooling is the clever notion that you should be able to run your
  code in various environments. With many continuous integration and continuous development
  (CI/CD) apps available, agnostic tooling gives developers a big advantage: portability...'
---

L'outil agnostique est le concept ingénieux selon lequel vous devriez pouvoir exécuter votre code dans divers environnements. Avec de nombreuses applications d'intégration continue et de développement continu (CI/CD) disponibles, l'outil agnostique offre aux développeurs un grand avantage : la portabilité.

Bien sûr, faire fonctionner votre CI/CD _partout_ est un défi de taille. Les applications CI populaires pour les dépôts GitHub utilisent à elles seules une multitude de langages de configuration couvrant [Groovy](https://groovy-lang.org/syntax.html), [YAML](https://yaml.org/), [TOML](https://github.com/toml-lang/toml), [JSON](https://json.org/), et plus encore... tous avec des syntaxes différentes, bien sûr. Porter les workflows d'un outil à un autre est plus qu'un processus d'une tasse de café.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/cover-2.png)

L'introduction de [GitHub Actions](https://github.com/features/actions) a le potentiel d'ajouter un autre outil au mélange ; ou, pour la bonne configuration, de simplifier considérablement un workflow CI/CD.

Avant cet article, j'accomplissais mon flux CD avec plusieurs applications assemblées. J'utilisais AWS Lambda pour déclencher les builds du site selon un calendrier. J'avais Netlify qui construisait sur les déclencheurs de push, ainsi que l'optimisation des images, puis poussait mon site vers le dépôt public Pages. J'utilisais Travis CI dans le dépôt public pour tester le HTML. Tout cela fonctionnait en conjonction avec GitHub Pages, qui héberge réellement le site.

Je n'utilise maintenant que la version bêta de GitHub Actions pour accomplir toutes les mêmes tâches, avec un [Makefile portable](https://victoria.dev/blog/a-portable-makefile-for-continuous-delivery-with-hugo-and-github-pages/) d'instructions de build, et sans aucune autre application CI/CD.

## Apprécier le shell

Que ont la plupart des outils CI/CD en commun ? Ils exécutent vos instructions de workflow dans un environnement shell ! C'est merveilleux, car cela signifie que la plupart des outils CI/CD peuvent faire tout ce que vous pouvez faire dans un terminal... et vous pouvez faire presque _n'importe quoi_ dans un terminal.

Surtout pour un cas d'utilisation contenu comme la construction de mon site statique avec un générateur comme Hugo, tout exécuter dans un shell est une évidence. Pour dire à la boîte magique quoi faire, nous devons simplement écrire des instructions.

Bien qu'un script shell soit certainement l'option la plus portable, j'utilise le toujours très portable [Make](https://en.wikipedia.org/wiki/Make_(software)) pour écrire mes instructions de processus. Cela me fournit certains avantages par rapport au simple script shell, comme l'utilisation de variables et de [macros](https://en.wikipedia.org/wiki/Make_(software)#Macros), et la modularité des [règles](https://en.wikipedia.org/wiki/Makefile#Rules).

Je suis entré dans les [détails de mon Makefile dans mon dernier article](https://victoria.dev/blog/a-portable-makefile-for-continuous-delivery-with-hugo-and-github-pages/). Regardons comment faire fonctionner GitHub Actions pour l'exécuter.

## Utiliser un Makefile avec GitHub Actions

Pour notre point sur la portabilité, mon Makefile magique est stocké directement à la racine du dépôt. Puisqu'il est inclus avec le code, je peux exécuter le Makefile localement sur n'importe quel système où je peux cloner le dépôt, à condition de définir les variables d'environnement. Utiliser GitHub Actions comme mon outil CI/CD est aussi simple que de faire fonctionner Make.

J'ai trouvé le [guide de syntaxe des workflows GitHub Actions](https://help.github.com/en/articles/workflow-syntax-for-github-actions) assez simple, bien que long sur les options. Voici la configuration nécessaire pour exécuter le Makefile.

Le fichier de workflow à `.github/workflows/make-master.yml` contient ce qui suit :

```
name: make-master

on:
  push:
    branches:
      - master
  schedule:
    - cron: '20 13 * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
        with:
          fetch-depth: 1
      - name: Exécuter le Makefile
        env:
          TOKEN: ${{ secrets.TOKEN }}
        run: make all
```

Je vais expliquer les composants qui font fonctionner cela.

## Déclencher le workflow

Actions prend en charge plusieurs [déclencheurs pour un workflow](https://help.github.com/en/articles/events-that-trigger-workflows). En utilisant la syntaxe `on`, j'ai défini deux déclencheurs pour le mien : un [événement push](https://help.github.com/en/articles/workflow-syntax-for-github-actions#onpushpull_requestbranchestags) vers la branche `master` uniquement, et un travail `cron` [planifié](https://help.github.com/en/articles/events-that-trigger-workflows#scheduled-events-schedule).

Une fois le fichier `make-master.yml` dans votre dépôt, l'un de vos déclencheurs fera en sorte qu'Actions exécute votre Makefile. Pour voir comment s'est déroulée la dernière exécution, vous pouvez également [ajouter un badge amusant](https://help.github.com/en/articles/configuring-a-workflow#adding-a-workflow-status-badge-to-your-repository) au README.

### Une chose un peu bidouillée

Parce que le Makefile s'exécute à chaque push vers `master`, je recevais parfois des erreurs lorsque le build du site n'avait aucun changement. Lorsque Git, via [mon Makefile](https://victoria.dev/blog/a-portable-makefile-for-continuous-delivery-with-hugo-and-github-pages/), tentait de commiter vers le dépôt Pages, aucun changement n'était détecté et le commit échouait de manière ennuyeuse :

```
nothing to commit, working tree clean
On branch master
Your branch is up to date with 'origin/master'.
nothing to commit, working tree clean
Makefile:62: recipe for target 'deploy' failed
make: *** [deploy] Error 1
##[error]Process completed with exit code 2.
```

J'ai trouvé des solutions qui proposaient d'utiliser `diff` pour vérifier si un commit devait être fait, mais cela peut ne pas fonctionner pour [des raisons](https://github.com/benmatselby/hugo-deploy-gh-pages/issues/4). En tant que solution de contournement, j'ai simplement ajouté [l'heure UTC actuelle](https://gohugo.io/functions/format/#use-local-and-utc) à ma page d'index afin que chaque build contienne un changement à commiter.

## Environnement et variables

Vous pouvez définir l'[environnement virtuel](https://help.github.com/en/github/automating-your-workflow-with-github-actions/virtual-environments-for-github-hosted-runners#supported-runners-and-hardware-resources) pour votre workflow à exécuter en utilisant la syntaxe `runs-on`. Le choix évident et le meilleur que j'ai fait est Ubuntu. Utiliser `ubuntu-latest` me donne la version la plus à jour, quelle qu'elle soit lorsque vous lisez ceci.

GitHub définit certaines [variables d'environnement par défaut](https://help.github.com/en/github/automating-your-workflow-with-github-actions/using-environment-variables#default-environment-variables) pour les workflows. L'[action `actions/checkout`](https://github.com/actions/checkout) avec `fetch-depth: 1` crée une copie du dernier commit de votre dépôt dans la variable `GITHUB_WORKSPACE`. Cela permet au workflow d'accéder au Makefile à `GITHUB_WORKSPACE/Makefile`. Sans utiliser l'action de checkout, le Makefile ne sera pas trouvé, et j'obtiens une erreur qui ressemble à ceci :

```
make: *** No rule to make target 'all'.  Stop.
Running Makefile
##[error]Process completed with exit code 2.
```

Bien qu'il existe un [jeton `GITHUB_TOKEN` secret par défaut](https://help.github.com/en/github/automating-your-workflow-with-github-actions/authenticating-with-the-github_token), ce n'est pas celui que j'ai utilisé. Le jeton par défaut n'est valable que localement pour le dépôt actuel. Pour pouvoir pousser vers mon dépôt GitHub Pages séparé, j'ai créé un [jeton d'accès personnel](https://github.com/settings/tokens) avec un accès `public_repo` et je le transmets en tant que variable chiffrée `secrets.TOKEN`. Pour un guide étape par étape, voir [Création et utilisation de secrets chiffrés](https://help.github.com/en/github/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets).

## Outillage portable

Le point positif de l'utilisation d'un simple Makefile pour définir la majeure partie de mon processus CI/CD est qu'il est complètement portable. Je peux exécuter un Makefile n'importe où j'ai accès à un environnement, ce qui est le cas de la plupart des applications CI/CD, des instances virtuelles, et, bien sûr, sur ma machine locale.

L'une des raisons pour lesquelles j'aime GitHub Actions est que faire fonctionner mon Makefile a été assez simple. Je pense que la syntaxe est bien faite - facile à lire, et intuitive lorsqu'il s'agit de trouver une option que vous recherchez. Pour quelqu'un utilisant déjà GitHub Pages, Actions offre une expérience CD assez transparente ; et si cela devait changer, je peux exécuter mon Makefile ailleurs. \_(\_)_/