---
title: Comment publier un site web sans code en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-28T20:59:47.000Z'
originalURL: https://freecodecamp.org/news/publish-a-no-code-website-in-10-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/igor-miske-Px3iBXV-4TU-unsplash.jpg
tags:
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
- name: github pages
  slug: github-pages
- name: Hugo
  slug: hugo
- name: No Code
  slug: no-code
- name: Static Site Generators
  slug: static-site-generators
- name: web
  slug: web
seo_title: Comment publier un site web sans code en 10 minutes
seo_desc: 'In this article, I''ll introduce a no-code, no-software and no-cost solution
  to publishing sophisticated web sites managed by non-technical people. The full
  codebase is on GitHub here.

  Sir Issac Newton discovered the law of gravity when practicing “so...'
---

Dans cet article, je vais vous présenter une solution sans code, sans logiciel et sans coût pour publier des sites web sophistiqués gérés par des personnes non techniques. Le code source complet est [disponible sur GitHub ici](https://github.com/second-state/hugo-website).

Sir Isaac Newton a découvert la loi de la gravité en pratiquant le "social distancing" pendant la peste. Que ferez-VOUS ? Un côté positif de la quarantaine est que tout ce temps libre fait ressortir l'esprit entrepreneurial et la créativité en nous.

Cependant, surtout à cause de la quarantaine, maintenant plus que jamais, toute nouvelle idée ou projet doit avoir un site web. Les solutions CMS traditionnelles comme Wordpress, Squarespace ou Wix sont difficiles à utiliser, ont un look dépassé, sont chères, ou tout cela à la fois !

Nous voulions créer un site web qui ait un look et une sensation sophistiqués, tout en étant facile à personnaliser. Une personne non technique devrait être capable de modifier les fichiers sources et de voir les changements apparaître sur le site web en direct en quelques minutes. Idéalement, il devrait également être gratuit (gratuit pour toujours, pas seulement gratuit pour l'instant), et pouvoir évoluer pour gérer des millions de visiteurs s'il devient populaire.

Est-ce possible ?

Dans cet article court, je vais vous guider à travers une solution basée sur le framework Hugo, GitHub Pages et GitHub Actions. Vous pouvez avoir votre nouveau site web opérationnel d'ici la fin de cet article.

> C'est si facile que mon fils de 9 ans l'a fait. Il gère maintenant un site web pour son pays fictif appelé [Arenztopia](https://www.arenztopia.com/). Découvrez [l'histoire](https://medium.com/@michaelyuan_88928/welcome-to-arenztopia-95cc85253163).

## TL;DR

Si vous voulez simplement commencer avec un site web opérationnel dès que possible, assurez-vous d'abord d'avoir un compte GitHub gratuit.

Allez sur [ce dépôt GitHub](https://github.com/second-state/hugo-website), et cliquez sur le bouton "Fork" en haut à droite, et **forkez-le** vers votre propre compte.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_edHfJdOu6Ppjiyd-M4tMJQ.png align="left")

Allez dans votre dépôt forké, et cliquez sur l'onglet Actions. Vous verrez un message comme celui de l'image ci-dessous. **Cliquez sur** le bouton "I understand my workflows ...".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_nCrYAyGhCmLeFC2PMbUBEA.png align="left")

Allez dans l'onglet Paramètres de votre dépôt, puis faites défiler jusqu'à GitHub Pages. **Re-sélectionnez** `gh-pages` dans le menu déroulant pour construire le site web.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_K4qXL2CN2rtMonI4dXRWnA.png align="left")

Allez dans l'onglet Code du dépôt, ouvrez le fichier `config.toml`, et modifiez-le. **Changez** son attribut `title` en quelque chose d'autre, et cliquez sur le bouton "Commit changes" en bas. Nous avons besoin de cette étape pour déclencher le workflow dans le nouveau dépôt.

Attendez quelques minutes, allez à l'adresse web "published at" sur GitHub Pages et vous verrez le site web template.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_WRQaxyvCqagRMfsN6T1B_A.png align="left")

Ensuite, vous pouvez personnaliser le site en modifiant le fichier `config.toml` et les fichiers dans le dossier `content`. Allez à la section "Ajoutez votre propre contenu" à la fin de cet article pour voir comment. Vous pouvez consulter [les instructions pour le thème Ananke ici](https://github.com/budparr/gohugo-theme-ananke#getting-started).

C'est tout pour le démarrage rapide ! Dans les prochaines sections, je vais expliquer plus en détail les concepts et les processus.

## Les bases de Hugo

Les solutions CMS de l'ancienne génération comme Wordpress sont trop difficiles à adapter aux nouveaux designs de sites web, et les solutions hébergées commercialement comme SquareSpace sont trop chères et pas assez flexibles. Les générateurs de sites web statiques comme Hugo offrent un bon équilibre entre fonctionnalités, flexibilité et facilité de création.

* Les sites web Hugo peuvent être personnalisés et modifiés via des fichiers de configuration.

* Les nouvelles pages et sections de contenu peuvent être écrites en markdown au lieu de HTML. Cela rend la création de contenu beaucoup plus facile.

* Il existe de nombreux thèmes de design modernes parmi lesquels choisir.

* Le résultat de Hugo est un site web statique HTML qui peut être déployé sur n'importe quel fournisseur d'hébergement à faible coût.

* Ensemble avec les services d'hébergement de sites web statiques comme GitHub Pages et Netlify, ils peuvent offrir une solution complètement gratuite.

La distribution logicielle Hugo est [disponible](https://gohugo.io/getting-started/installing/) sur tous les principaux systèmes d'exploitation. Vous pouvez [en apprendre davantage ici](https://gohugo.io/getting-started/quick-start/). Mais, puisque nous allons utiliser GitHub Actions pour construire automatiquement nos sites web Hugo, nous n'avons pas réellement besoin d'installer le logiciel Hugo ici.

Voici comment faire.

## Créer un site web template

Tout d'abord, sélectionnez un thème Hugo. Il y en a [beaucoup](https://themes.gohugo.io/). Certains sont orientés vers des sites web avec une ou plusieurs pages de contenu, tandis que d'autres sont optimisés pour des sites de type blog avec des articles datés.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_CjWlyVScCKNkxDIxshwYTQ.png align="left")

*Thèmes Hugo*

Trouvez celui que vous aimez, téléchargez un package zip ou clonez un dépôt GitHub, et décompressez le thème dans un dossier. Supposons que la distribution du thème est décompressée dans un dossier appelé `my-theme`. Les commandes suivantes sont pour un terminal Linux. Vous pourriez utiliser l'application Terminal sur Mac ou PowerShell sur Windows.

Ensuite, créez le répertoire de votre projet de site web sur votre ordinateur.

```javascript
$ mkdir -r my-site/themes
```

Copiez le dossier du thème dans votre projet.

```javascript
$ cp -r my-theme my-site/themes
```

Ensuite, copiez l'`exampleSite` du thème dans le répertoire de premier niveau du projet.

```javascript
$ cd my-site
$ cp -r themes/my-theme/exampleSite/* ./
```

Modifiez le `config.toml` dans le répertoire racine du projet `my-site/` pour pointer vers le bon thème.

```javascript
baseURL = "/"themesDir = "themes"theme = "my-theme"
```

Ensuite, créez un dépôt GitHub appelé `my-site`, et poussez le répertoire `my-site` sur sa branche `master`. Voici les étapes pour [téléverser des fichiers depuis l'interface web de GitHub](https://help.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository). Maintenant, nous sommes prêts à publier le site exemple du thème.

Pour qu'un système basé sur Hugo soit utilisable par une personne non développeuse (ou un jeune développeur qui n'a pas encore maîtrisé les outils en ligne de commande), nous devons automatiser le processus de construction et de déploiement du site web statique.

## Automatiser le déploiement

Dans le projet GitHub, allez dans Paramètres et activez GitHub Pages. Sélectionnez la source comme étant la branche `gh-pages`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_TrbrZti-GFpVBK0HtrezcA.png align="left")

*Paramètres, GitHub Pages*

Ensuite, nous créons un workflow GitHub Actions pour exécuter la commande Hugo sur les fichiers sources de la branche `master`, et pousser les fichiers HTML générés vers la branche `gh-pages` pour publication. À partir de l'onglet Actions du projet, cliquez sur le bouton "set up a workflow yourself".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_b5UuewhfFq2Gfa0vwJ8bqw.png align="left")

*Configurer un workflow vous-même*

Le workflow est stocké dans la branche `master` sous le fichier `.github/workflows/main.yml`. Le contenu du fichier est le suivant.

```yaml
name: github pages

on:
  push:
    branches:
      - master

jobs:
  deploy:
    runs-on: ubuntu-18.04
    steps:
      - uses: actions/checkout@v1  # v2 does not have submodules option now
        # with:
        #   submodules: true

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.62.2'
          extended: true

      - name: Build
        run: hugo

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

Ce qui se passe ici, c'est que les auteurs et éditeurs du site web vont modifier le contenu et les fichiers sur la branche `master`. Chaque fois que du nouveau contenu est poussé vers la branche `master`, le workflow automatisé GitHub Actions va [configurer le logiciel Hugo](https://github.com/peaceiris/actions-hugo/blob/master/README.md), exécuter la commande `hugo`, et transformer ces fichiers en fichiers HTML pour un site web statique.

Les fichiers HTML sont [poussés](https://github.com/peaceiris/actions-gh-pages/blob/master/README.md) vers la branche `gh-pages` du même dépôt. Ils seront publiés sur l'adresse web spécifiée par GitHub Pages comme configuré.

Remarquez l'attribut `cname` dans la dernière ligne. C'est le [nom de domaine personnalisé](https://help.github.com/en/github/working-with-github-pages/configuring-a-custom-domain-for-your-github-pages-site) que nous avons configuré avec GitHub Pages. Si vous n'avez pas de nom de domaine personnalisé, supprimez simplement cette ligne, et vous pourrez accéder à votre site web à l'adresse fournie par GitHub Pages.

Maintenant, allez sur le site web, et vous devriez voir la page web par défaut du thème.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_fkJkt7YXYEZX96Qv3v5u8A.png align="left")

*Le template HugoSerif pour l'un de nos sites web.*

## Ajoutez votre propre contenu

Pour changer le site web par défaut du thème en votre propre contenu, vous devez simplement modifier les fichiers sur la branche `master`. Veuillez vous référer à la [documentation](https://gohugo.io/content-management/organization/) de votre thème sélectionné. En général, les templates Hugo fonctionnent comme ceci :

* Les pages web sont créées au format markdown et les fichiers `md` se trouvent dans le dossier `content`.

* Chaque fichier `md` a une section d'en-tête avec des propriétés telles que le placement du menu de la page, la priorité, l'horodatage, l'extrait, etc.

* La configuration globale, telle que les éléments de menu et les propriétés utilisées par plusieurs pages, est stockée dans le dossier `data`.

* Le contenu statique tel que les fichiers HTML bruts, les fichiers JavaScript et les fichiers image peuvent être placés dans le dossier `static`.

En particulier, voici comment vous personnalisez le thème Ananke qui accompagne notre template :

* Le fichier [config.toml](https://github.com/second-state/hugo-website/blob/master/config.toml) vous permet de configurer le titre du site web, les icônes sociales sur toutes les pages, et la grande image en vedette sur la page d'accueil.

* Toutes les images doivent être téléversées dans le dossier [static/images](https://github.com/second-state/hugo-website/tree/master/static/images).

* Le fichier [content/\_index.md](https://github.com/second-state/hugo-website/blob/master/content/_index.md) contient le texte pour la page d'accueil.

* Pour ajouter des pages au site, vous pouvez simplement créer des fichiers [markdown](https://guides.github.com/features/mastering-markdown/) dans le dossier [content](https://github.com/second-state/hugo-website/tree/master/content). Un exemple est le fichier [contact.md](https://github.com/second-state/hugo-website/blob/master/content/contact.md). Remarquez qu'en haut du fichier, il y a des attributs pour contrôler si cette page doit être dans le menu du site web.

* Pour ajouter des articles au site, vous pouvez créer des fichiers markdown dans le dossier [content/post](https://github.com/second-state/hugo-website/tree/master/content/post). Ce sont des articles de contenu de type blog qui ont des dates et des titres en haut. Les deux articles les plus récents apparaîtront sur la page d'accueil.

Si vous êtes intéressé à en apprendre davantage et à voir comment nous l'avons fait, vous pouvez suivre notre progression sur :

* Le Pays d'Arenztopia [[GitHub](https://github.com/juntao/arenztopia)] [[Site web](https://www.arenztopia.com/)]

* Le blog de Second State [[GitHub](https://github.com/second-state/blog)] [[Site web](https://blog.secondstate.io/categories/en/)]

Bonne chance et restez en bonne santé !

## À propos de l'auteur

Le Dr. Michael Yuan est l'[auteur de 5 livres](http://www.michaelyuan.com/) sur le génie logiciel. Son dernier livre [Building Blockchain Apps](https://www.buildingblockchainapps.com/) a été publié par Addison-Wesley en décembre 2019. Le Dr. Yuan est le co-fondateur de [Second State](https://www.secondstate.io/), une startup financée par des capitaux-risqueurs qui apporte les technologies WebAssembly et Rust aux applications [cloud](https://www.secondstate.io/articles/why-webassembly-server/), [blockchain](https://docs.secondstate.io/), et [IA](https://github.com/second-state/rust-wasm-ai-demo/blob/master/README.md). Elle permet aux développeurs de déployer des fonctions Rust rapides, sûres, portables et serverless [sur Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/).

<iframe src="https://webassemblytoday.substack.com/embed" width="480" height="320" style="border:1px solid #EEE;background:white"></iframe>

Avant Second State, le Dr. Yuan était un contributeur de longue date à l'open source chez Red Hat, JBoss et Mozilla. En dehors du logiciel, le Dr. Yuan est un Investigateur Principal aux National Institutes of Health, avec plusieurs prix de recherche sur le cancer et la santé publique. Il est titulaire d'un doctorat en astrophysique de l'Université du Texas à Austin.