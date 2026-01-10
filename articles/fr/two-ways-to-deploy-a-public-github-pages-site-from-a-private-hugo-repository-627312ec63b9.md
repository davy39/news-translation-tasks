---
title: Deux façons de déployer un site public GitHub Pages à partir d'un dépôt privé
  Hugo
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-04-30T22:19:46.000Z'
originalURL: https://freecodecamp.org/news/two-ways-to-deploy-a-public-github-pages-site-from-a-private-hugo-repository-627312ec63b9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*PIWDprt12aR7QsJ8.jpg
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Deux façons de déployer un site public GitHub Pages à partir d'un dépôt
  privé Hugo
seo_desc: 'Keep your drafts out of the public eye by making use of continuous deployment
  tools to publish your public GitHub Pages site — from a separate private repository.

  Tools like Travis CI and Netlify offer some pretty nifty features, like seamlessly
  depl...'
---

#### Gardez vos brouillons hors de la vue du public en utilisant des outils de déploiement continu pour publier votre site public GitHub Pages — à partir d'un dépôt privé séparé.

Des outils comme Travis CI et Netlify offrent des fonctionnalités assez ingénieuses, comme le déploiement transparent de votre site GitHub Pages lorsque des modifications sont poussées vers son dépôt. Associé à un générateur de site statique comme Hugo, maintenir un blog à jour est assez indolore.

J'utilise Hugo pour construire mon site depuis des années, mais jusqu'à la semaine dernière, je n'avais jamais connecté mon dépôt Pages à un service de déploiement. Pourquoi ? Parce qu'utiliser un outil qui construit mon site avant de le déployer semblait nécessiter d'avoir toute la recette au même endroit — et si vous utilisez GitHub Pages avec la version gratuite de GitHub, [cet endroit est public](https://help.github.com/en/articles/configuring-a-publishing-source-for-github-pages). Cela signifie que toutes mes idées brillantes à trois heures du matin et mes brouillons inachevés (et pas drôles) seraient publics — et aucune quantité de commodité continue ne allait me convaincre de faire cela.

J'ai donc gardé les choses séparées, avec le désordre derrière les scènes de Hugo dans un dépôt Git local, et le dossier généré `public/` poussé vers mon dépôt distant GitHub Pages. Chaque fois que je voulais déployer mon site, je devais me connecter à mon ordinateur portable et exécuter `hugo` pour construire mon site, puis `cd public/ && git add . && git commit`... etc. Tout allait bien, sauf pour le sentiment tenace qu'il y avait une meilleure façon de faire cela.

J'ai écrit un autre article il y a quelque temps sur [l'utilisation de GitHub et Working Copy](https://victoria.dev/verbose/a-remote-sync-solution-for-ios-and-linux-git-and-working-copy/) pour apporter des modifications à mes dépôts sur mon iPad lorsque je suis en déplacement. Il me semblait étrange que je puisse tout faire sauf déployer mon site depuis mon iPad, alors j'ai décidé de changer cela.

Quelques idées brillantes à trois heures du matin et un jeton d'accès révoqué plus tard (oops), j'ai maintenant non pas une mais _deux_ façons de déployer vers mon dépôt public GitHub Pages à partir d'un dépôt GitHub entièrement séparé et privé. Dans cet article, je vais vous montrer comment y parvenir avec [Travis CI](https://travis-ci.com/) ou en utilisant [Netlify](http://netlify.com/) et [Make](https://www.gnu.org/software/make/).

Il n'y a rien de bidouillage là-dedans — mon dépôt public GitHub Pages a toujours la même apparence que lorsqu'il était poussé localement depuis mon terminal. Maintenant, je peux tirer parti de quelques excellents outils de déploiement pour mettre à jour le site chaque fois que je pousse vers mon dépôt privé, que je sois sur mon ordinateur portable ou en déplacement avec mon iPad.

![Image](https://cdn-media-1.freecodecamp.org/images/BWGFKiySx83s7T-PKOSYkuokL5FLBYVDLZ10)
_#YouDidNotPushFromThere_

Cet article suppose que vous avez une connaissance pratique de Git et de GitHub Pages. Sinon, vous pourriez aimer ouvrir quelques onglets de navigateur à partir de mes articles sur [l'utilisation de GitHub et Working Copy](https://victoria.dev/verbose/a-remote-sync-solution-for-ios-and-linux-git-and-working-copy/) et [la construction d'un site avec Hugo et GitHub Pages](https://victoria.dev/verbose/how-i-ditched-wordpress-and-set-up-my-custom-domain-https-site-for-almost-free/) d'abord.

Faisons-le !

### Déploiement de GitHub Pages privé vers public avec Travis CI

Travis CI a la capacité intégrée (♬) de [déployer vers GitHub Pages](https://docs.travis-ci.com/user/deployment/pages/) après une construction réussie. Ils font un travail décent dans la documentation pour expliquer comment ajouter cette fonctionnalité, surtout si vous avez déjà utilisé Travis CI... ce que je n'avais pas fait. Ne vous inquiétez pas, j'ai fait le gros du travail de compréhension pour vous.

* Travis CI obtient toutes ses instructions à partir d'un fichier de configuration à la racine de votre dépôt appelé `.travis.yml`
* Vous devez fournir un [jeton d'accès personnel GitHub](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) en tant que variable chiffrée sécurisée, que vous pouvez générer en utilisant `travis` sur la ligne de commande
* Une fois que votre script a terminé avec succès ce que vous lui avez dit de faire (pas nécessairement ce que vous _voulez_ qu'il fasse, mais c'est un autre article de blog), Travis déployera votre répertoire de construction vers un dépôt que vous pouvez spécifier avec la variable de configuration `repo`.

#### Configuration du fichier de configuration Travis

Créez un nouveau fichier de configuration pour Travis avec le nom de fichier `.travis.yml` (notez le "." initial). Ces scripts sont très personnalisables et j'ai eu du mal à trouver un exemple pertinent à utiliser comme point de départ - heureusement, vous n'avez pas ce problème !

Voici mon `.travis.yml` de base :

```
git:
 depth: false

env:
 global:
 - HUGO_VERSION="0.54.0"
 matrix:
 - YOUR_ENCRYPTED_VARIABLE

install:
 - wget -q https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
 - tar xf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
 - mv hugo ~/bin/

script:
 - hugo --gc --minify

deploy:
 provider: pages
 skip-cleanup: true
 github-token: $GITHUB_TOKEN
 keep-history: true
 local-dir: public
 repo: gh-username/gh-username.github.io
 target-branch: master
 verbose: true
 on:
 branch: master
```

Ce script télécharge et installe Hugo, construit le site avec les drapeaux de collecte des déchets et de minification, puis déploie le répertoire `public/` vers le `repo` spécifié - dans cet exemple, votre dépôt public GitHub Pages. Vous pouvez lire à propos de chaque option de configuration de `deploy` [ici](https://docs.travis-ci.com/user/deployment/pages/#further-configuration).

Pour [ajouter le jeton d'accès personnel GitHub en tant que variable chiffrée](https://docs.travis-ci.com/user/environment-variables#defining-encrypted-variables-in-travisyml), vous n'avez pas besoin de modifier manuellement votre `.travis.yml`. Les commandes `travis` ci-dessous chiffreront et ajouteront la variable pour vous lorsque vous les exécuterez dans le répertoire de votre dépôt.

Tout d'abord, installez `travis` avec `sudo gem install travis`.

Ensuite, [générez votre jeton d'accès personnel GitHub](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line), copiez-le (il n'apparaît qu'une seule fois !) et exécutez les commandes ci-dessous à la racine de votre dépôt, en substituant votre jeton aux kisses :

```
travis login --pro --github-token xxxxxxxxxxxxxxxxxxxxxxxxxxx
travis encrypt GITHUB_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxx --add env.matrix
```

Votre jeton chiffré apparaît magiquement dans le fichier. Une fois que vous avez commis `.travis.yml` dans votre dépôt privé Hugo, Travis CI exécutera le script et, si la construction réussit, déployera votre site vers votre dépôt public GitHub Pages. Magie !

Travis exécutera toujours une construction chaque fois que vous pousserez vers votre dépôt privé. Si vous ne voulez pas déclencher ce comportement avec un commit particulier, [ajoutez la commande `skip` à votre message de commit](https://docs.travis-ci.com/user/customizing-the-build/#skipping-a-build).

_Yo c'est cool mais je préfère Netlify._

D'accord, très bien.

### Déploiement vers un dépôt séparé avec Netlify et Make

Nous pouvons faire en sorte que Netlify fasse notre travail en utilisant un Makefile, que nous exécuterons avec la commande de construction de Netlify.

Voici à quoi ressemble notre `Makefile` :

```
SHELL:=/bin/bash
BASEDIR=$(CURDIR)
OUTPUTDIR=public
.PHONY: all
all: clean get_repository build deploy
.PHONY: clean
clean:
@echo "Suppression du répertoire public"
rm -rf $(BASEDIR)/$(OUTPUTDIR)
.PHONY: get_repository
get_repository:
@echo "Récupération du dépôt public"
git clone https://github.com/gh-username/gh-username.github.io.git public
.PHONY: build
build:
@echo "Génération du site"
hugo --gc --minify
.PHONY: deploy
deploy:
@echo "Préparation du commit"
@cd $(OUTPUTDIR) \
 && git config user.email "you@youremail.com" \
 && git config user.name "Your Name" \
 && git add . \
 && git status \
 && git commit -m "Déploiement via Makefile" \
 && git push -f -q https://$(GITHUB_TOKEN)@github.com/gh-username/gh-username.github.io.git master
@echo "Poussé vers le dépôt distant"
```

Pour préserver l'historique Git de notre dépôt GitHub Pages séparé, nous allons d'abord le cloner, construire notre nouveau site Hugo dedans, puis le pousser vers le dépôt Pages. Ce script supprime d'abord tout dossier `public/` existant qui pourrait contenir des fichiers ou un historique Git. Il clone ensuite notre dépôt Pages vers `public/`, construit notre site Hugo (essentiellement en mettant à jour les fichiers dans `public/`), puis s'occupe de commiter le nouveau site vers le dépôt Pages.

Dans la section `deploy`, vous remarquerez des lignes commençant par `&&`. Ce sont des commandes enchaînées. Puisque Make [invoque un nouveau sous-shell pour chaque ligne](https://www.gnu.org/software/make/manual/html_node/Execution.html#Execution), il recommence avec chaque nouvelle ligne depuis notre répertoire racine. Pour que notre `cd` persiste et éviter d'exécuter nos commandes Git dans le répertoire racine du projet, nous enchaînons les commandes et utilisons le caractère backslash pour [casser les longues lignes](http://clarkgrubb.com/makefile-style-guide#breaking-long-lines) pour une meilleure lisibilité.

En enchaînant nos commandes, nous sommes en mesure de [configurer notre identité Git](https://stackoverflow.com/questions/6116548/how-to-tell-git-to-use-the-correct-identity-name-and-email-for-a-given-project), ajouter tous nos fichiers mis à jour, et créer un commit pour notre dépôt Pages.

De manière similaire à l'utilisation de Travis CI, nous devrons passer un [jeton d'accès personnel GitHub](https://github.com/settings/tokens) pour pousser vers notre dépôt public GitHub Pages — sauf que Netlify ne fournit pas de moyen simple de chiffrer le jeton dans notre Makefile.

Au lieu de cela, nous utiliserons les [Variables d'Environnement de Construction](https://www.netlify.com/docs/continuous-deployment/#build-environment-variables) de Netlify, qui résident en toute sécurité dans les paramètres de notre site dans l'application Netlify. Nous pouvons ensuite appeler notre variable de jeton dans le Makefile. Nous l'utilisons pour pousser (silencieusement, pour éviter d'imprimer le jeton dans les logs) vers notre dépôt Pages en [le passant dans l'URL distante](https://stackoverflow.com/questions/44773415/how-to-push-a-commit-to-github-from-a-circleci-build-using-a-personal-access-tok).

Pour éviter d'imprimer le jeton dans les logs de Netlify, nous supprimons [l'écho de la recette](https://www.gnu.org/software/make/manual/html_node/Echoing.html#Echoing) pour cette ligne avec le caractère `@` initial.

Avec votre Makefile à la racine de votre dépôt privé GitHub, vous pouvez configurer Netlify pour l'exécuter pour vous.

#### Configuration de Netlify

La configuration avec Netlify via l'[interface web](https://app.netlify.com/) est simple. Une fois que vous vous êtes connecté avec GitHub, choisissez le dépôt privé GitHub où se trouve votre site Hugo. La page suivante à laquelle Netlify vous amène vous permet d'entrer les paramètres de déploiement :

![Image](https://cdn-media-1.freecodecamp.org/images/w6TKS71OtIM1jgkarOqfuRpAu-WnEQzz4ZoM)
_Créer une nouvelle page de site sur Netlify_

Vous pouvez spécifier la commande de construction qui exécutera votre Makefile (`make all` pour cet exemple). La branche à déployer et le répertoire de publication n'ont pas trop d'importance dans notre cas spécifique, puisque nous nous préoccupons uniquement de pousser vers un dépôt séparé. Vous pouvez entrer la branche de déploiement `master` typique et le répertoire de publication `public`.

Sous "Paramètres de construction avancés", cliquez sur "Nouvelle variable" pour ajouter votre jeton d'accès personnel GitHub en tant que variable d'environnement de construction. Dans notre exemple, le nom de la variable est `GITHUB_TOKEN`. Cliquez sur "Déployer le site" pour faire la magie.

Si vous avez déjà configuré votre dépôt avec Netlify, trouvez les paramètres pour le déploiement continu sous Paramètres > Construction et déploiement.

Netlify construira votre site chaque fois que vous pousserez vers le dépôt privé. Si vous ne voulez pas qu'un commit particulier déclenche une construction, [ajoutez `[skip ci]` dans votre message de commit Git](https://www.netlify.com/docs/continuous-deployment/#skipping-a-deploy).

#### Même chose mais différent

Un effet de l'utilisation de Netlify de cette manière est que votre site sera construit en deux endroits : l'un est le dépôt GitHub Pages public séparé vers lequel le Makefile pousse, et l'autre est votre site Netlify qui se déploie sur leur CDN à partir de votre dépôt privé GitHub lié. Ce dernier est utile si vous allez jouer avec les [Aperçus de Déploiement](https://www.netlify.com/blog/2016/07/20/introducing-deploy-previews-in-netlify/) et d'autres fonctionnalités de Netlify, mais celles-ci sont hors du cadre de cet article.

Le point principal est que votre site GitHub Pages est maintenant mis à jour dans votre dépôt public. Hourra !

### Allez-y et déployez sans crainte

J'espère que l'effet de cette nouvelle information est que vous vous sentez plus capable de mettre à jour vos sites, où que vous soyez. Les possibilités sont infinies — à la maison sur votre canapé avec votre ordinateur portable, en déplacement avec votre iPad, ou au milieu d'un premier rendez-vous sur votre téléphone. Infinies !

![Image](https://cdn-media-1.freecodecamp.org/images/HXM8dI8xKrzd7oA9wLXqjdOSzrWdXKOWmAt8)
_Ne faites pas de choses sur votre téléphone lorsque vous êtes en rendez-vous. Pas si vous voulez un deuxième, en tout cas._