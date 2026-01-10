---
title: Comment j'ai établi un bon processus de publication en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T16:38:37.000Z'
originalURL: https://freecodecamp.org/news/how-i-established-a-good-release-process-in-javascript-b93e57e247e1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S2X4yWrBgveACTHLsHNZoA.jpeg
tags:
- name: Git
  slug: git
- name: npm
  slug: npm
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai établi un bon processus de publication en JavaScript
seo_desc: 'By Dafna Rosenblum

  With Git Workflows, NPM, and 3rd party libraries

  Lately, I’ve sat down to define the release procedures for my team. I went through
  git workflows, best practices for versioning, and methods to upgrade external libraries.
  I wanted t...'
---

Par Dafna Rosenblum

#### Avec les flux de travail Git, NPM et les bibliothèques tierces

Récemment, je me suis assise pour définir les procédures de publication pour mon équipe. J'ai passé en revue les flux de travail git, les meilleures pratiques pour le versionnage, et les méthodes pour mettre à jour les bibliothèques externes. Je voulais avoir tout mon apprentissage en un seul endroit, car je sais que je reviendrai à cela dans le futur. J'espère que vous le trouverez utile également.

Dans cet article, je vais expliquer comment combiner le _flux de travail git, semver,_ et NPM pour créer une gestion saine des bibliothèques et une intégration continue en JavaScript. Cela a commencé à me déranger lorsque mon équipe est devenue plus grande et que nous avons dû créer un meilleur processus qui fonctionnait pour tout le monde et sur lequel nous étions tous d'accord. J'ai lu environ 20 articles pour créer ce résumé combiné élaboré de différentes pratiques et recommandations officielles.

![Image](https://cdn-media-1.freecodecamp.org/images/XFE9iGMgzhbROIYWY9eErb7cz9FC3HBTfLM2)
_Photo par [Unsplash](https://unsplash.com/photos/1Z15APktAiY?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com/search/photos/flow?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### GIT FLOW

Il existe différentes façons d'utiliser Git. Les modèles dictent quels types de branches existeront dans le projet, leurs conventions de nommage, quand utiliser chaque type, etc. Le modèle le plus connu est Git Flow.

[GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) est comme Agile — tout le monde utilise _une certaine_ version de celui-ci.

Il a été créé en janvier 2010 par [Vincent Driessen](https://nvie.com/about/). Il a été largement utilisé depuis, bien qu'il y ait beaucoup de critiques à son sujet. Je vais élaborer sur leur perspective après avoir expliqué la méthodologie elle-même.

Je recommande vivement de le lire entièrement et d'utiliser le résumé ci-dessous uniquement comme une aide-mémoire (il contient également quelques informations supplémentaires).

### Deux types de branches

#### Branches à durée de vie infinie : _master_ et _develop_

* origin/master est toujours prêt pour la production.
* origin/develop inclut toujours les derniers changements livrés pour la prochaine publication. Lorsqu'il est prêt, il est fusionné avec master et les changements sont étiquetés avec un numéro de version.

#### Branches à durée de vie limitée

* Branches de fonctionnalités
* Branches de publication
* Branches de correction rapide

Examinons chacun de ces types plus en détail.

#### Branches de fonctionnalités

* Créées à partir de _develop_ et fusionnées à nouveau avec _develop_.
* Convention de nommage : tout sauf _master_, _develop_, _release-*_, ou _hotfix-*_. J'aime utiliser le préfixe `feature/`, par exemple `feature/fix-texts`.

Lors de la fusion avec _develop_, Vincent recommande d'utiliser le drapeau `--no-ff`, qui crée toujours un nouveau commit pour la fusion. Cela permet d'avoir une meilleure compréhension du suivi de l'historique et de savoir quels commits ont été publiés ensemble en tant que fonctionnalité. Cela simplifie également l'annulation d'une fonctionnalité.

#### Branches de publication

* Créées à partir de _develop_ et fusionnées à nouveau avec _develop_ et _master_.
* Convention de nommage : _release-*_, par exemple : _release-1.2._
* Objectif : modifications de dernière minute, afin que develop soit prêt à recevoir les modifications pour la prochaine publication.

Jusqu'à la création de la branche de publication, les modifications pour la prochaine publication ne peuvent pas être fusionnées avec _develop_. Le numéro de version est défini lors de la création de la branche de publication et utilisé comme son nom.

#### npm-version

Après avoir créé la branche de publication, vous devez exécuter `./bump-version.sh`. Il s'agit d'un script fictif qui met à jour le numéro de version du projet. Comme je l'ai mentionné, l'article sur Git Flow date de janvier 2010. C'est également le mois où [NPM a été publié pour la première fois](https://en.wikipedia.org/wiki/Npm_(software)) (coïncidence ?), et je préfère utiliser [npm-version](https://docs.npmjs.com/cli/version.html) comme suit :

```
> npm version patch
```

La sortie sera le nouveau numéro de version. Un commit sera ajouté à la branche avec le nouveau numéro de version mis à jour dans les fichiers _package.json_ et _package-lock.json_.

Exécutez `git log -1` puis `git show <commit hash>` pour voir les modifications.

Pour modifier la version _minor_ ou _major_, utilisez `npm version minor` ou `npm version major`, respectivement.

Utilisez le drapeau `-m` pour ajouter un message de commit, sinon ce sera le numéro de la nouvelle version.

Si _preversion, version,_ ou _postversion_ sont dans la propriété _scripts_ du package.json — ils seront également exécutés.

Il créera également une [étiquette git](https://git-scm.com/book/en/v2/Git-Basics-Tagging). Vous pouvez le voir en exécutant `git tag` avant et après l'exécution de `npm version patch`, et noter la différence.

Comme expliqué dans la documentation sur les _étiquettes git_, par défaut, la commande `git push` ne transfère pas les étiquettes vers les serveurs distants. Vous devrez explicitement pousser les étiquettes vers un serveur partagé après les avoir créées. Ce processus est similaire au partage des branches distantes. Vous pouvez exécuter `git push origin v1.5.1`. Il est également possible de supprimer et de vérifier les étiquettes locales et distantes.

Une alternative à npm-version est l'outil populaire [release-it](https://www.npmjs.com/package/release-it), qui peut incrémenter la version, créer des étiquettes et des publications, et plus encore.

#### Retour aux branches de publication

Vous avez donc créé une branche de publication, exécuté `npm version patch` et poussé. Peut-être avez-vous également ajouté des corrections de bugs mineurs. L'étape suivante consiste à fusionner avec master et à publier.

#### Création d'une publication à partir d'une étiquette

Comme expliqué dans la [documentation de GitHub](https://help.github.com/articles/creating-releases/), lors de la création d'une publication, vous devez taper un numéro de version pour celle-ci. Les versions sont basées sur les étiquettes Git. Sous la zone de saisie de la version, vous verrez le texte : _Choisissez une étiquette existante ou créez une nouvelle étiquette lors de la publication._ Vous pouvez choisir de pousser l'étiquette créée par `npm-version` puis de la taper à nouveau lors de la création de la publication, ou vous pouvez choisir de ne pas la pousser et de la taper lors de la création de la publication. Bien sûr, vous pouvez [créer une publication automatique](https://developer.github.com/v3/repos/releases/#create-a-release) au lieu d'utiliser manuellement le site web de GitHub.

#### Fusion avec _develop_

N'oubliez pas de fusionner la branche de publication avec develop. Ensuite, la branche de publication peut être supprimée. Vous pourriez rencontrer des conflits de fusion ici, alors corrigez-les simplement et validez.

### Branches de correction rapide

* Contiennent des corrections pour des bugs de production urgents.
* Créées à partir de _master_, et fusionnées à nouveau avec _develop_ et _master_.
* Convention de nommage : `hotfix-*`.

Comme les branches de publication, elles sont destinées à préparer une nouvelle publication, et le processus de création de la branche et de sa finalisation est exactement le même.

Si vous travaillez avec des branches de publication et qu'une branche de publication existe, essayez de ne pas la fusionner avec develop, mais avec la branche de publication, qui sera fusionnée avec develop plus tard.

### Est-ce vraiment le cas ?

C'est la méthode Git Flow. Elle fonctionnera mieux avec une méthodologie en cascade. La méthode recommandée aujourd'hui est le déploiement continu — être entièrement couvert par des tests, ne pas avoir de branche _develop_, fusionner les branches de fonctionnalités avec master et déployer immédiatement.

Mais le type de produit et de marché peut parfois dicter un processus de déploiement différent. Par exemple, dans le domaine de la _santé_, il n'est pas toujours possible d'avoir un déploiement continu, en raison des réglementations. Dans l'industrie du jeu, il y a des dates de sortie pour les jeux et ils ne fonctionnent souvent pas avec l'intégration et la livraison continues.

### OPPOSANTS

Si vous cherchez "ne pas utiliser gitflow" sur Google, vous pouvez trouver beaucoup d'articles. Voici les principaux points de certains d'entre eux :

#### #1

Dans son blog ["End Of Line"](https://www.endoflineblog.com/gitflow-considered-harmful), [Adam Ruka](https://www.endoflineblog.com/about) affirme que l'utilisation du drapeau _--no-ff_ entraîne des "cartes de train git" (voir photo), qui sont très difficiles à suivre rétrospectivement. Il recommande vivement d'utiliser _rebase_ à la place.

Il affirme également que la méthodologie est trop complexe et qu'il est impossible pour les développeurs de ne pas faire d'erreurs et de fusionner depuis/vers la mauvaise branche.

Bien que je sois d'accord avec le premier point, je pense que l'automatisation des builds (comme l'étiquetage automatique) et des branches bien configurées sur GitHub peuvent résoudre la plupart des erreurs humaines. Il propose une approche différente de Git Flow dans [cet](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow) article.

![Image](https://cdn-media-1.freecodecamp.org/images/1xunh5h8GWxWG6inkEfCaWoUR3mBpR2r5zk0)
_Photo du grand projet [https://github.com/vbarbaresi/MetroGit](https://github.com/vbarbaresi/MetroGit" rel="noopener" target="_blank" title=")_

#### #2

Dans son article ["Git : Comment je l'utilise et pourquoi je n'utilise pas GitFlow"](https://medium.com/@matt.dekrey/git-how-i-use-it-and-why-i-dont-use-gitflow-8688f255fef2), [Matthew DeKrey](https://medium.com/@matt.dekrey) dit à propos de la branche _develop_ :

> "Avoir du code dans un endroit commun où il n'est pas entièrement testé et ne travaille pas nécessairement vers une fonctionnalité à publier finit par être une ville fantôme d'architectures à moitié terminées et de fonctionnalités non publiées si l'équipe est jamais occupée."

Je pense qu'avec un peu de discipline et une CI décente, l'équipe fusionnera (ou rebasera) avec `develop` uniquement les fonctionnalités qui sont prêtes et ont passé les tests unitaires et les tests d'intégration, puis la suite de tests nocturne (ou les tests système) peut s'exécuter sur develop et s'assurer que les fonctionnalités fonctionnent ensemble.

L'autre problème qu'il mentionne est la prise en charge des anciennes versions : _"une fois que vous avez publié la version v1.2, vous ne pouvez plus corriger v1.1"_. Et dans cet article, vous pouvez également trouver sa méthode recommandée pour travailler avec les branches Git.

#### #3

Dans son article [GitHub workflows inside of a company](https://humanwhocodes.com/blog/2013/05/21/github-workflows-inside-of-a-company/), Nicholas C. Zakas dit :

> _"Le sentiment général est que git-flow fonctionne bien pour les produits dans un modèle de publication plus traditionnel, où les publications sont faites une fois toutes les quelques semaines, mais que ce processus se décompose considérablement lorsque vous publiez une fois par jour ou plus."_

Un an et demi après la publication de Git Flow, Scott Chacon, un ingénieur qui a aidé à lancer GitHub, a publié [GitHub flow](http://scottchacon.com/2011/08/31/github-flow.html), qui est une version plus simple de Git Flow qui fonctionne mieux pour les projets CD.

### QUE CHOISIR ALORS ?

L'un des problèmes auxquels nous sommes confrontés dans l'industrie aujourd'hui est de lutter contre la perception qu'il n'y a qu'une seule façon de faire les choses correctement. Nous ignorons le fait que différentes équipes, produits et marchés nécessitent des solutions différentes.

Bien sûr, avant de choisir une technologie ou un modèle, l'équipe doit comprendre les avantages et les inconvénients de son utilisation. Mais il n'y a pas de "solution unique pour tous". Dans [cet article recommandé](https://www.atlassian.com/git/tutorials/comparing-workflows#feature-branch-workflow) d'Atlassian (BitBucket), ils passent en revue certains flux de travail Git possibles et disent :

> _"N'oubliez pas que ces flux de travail sont conçus pour être des lignes directrices plutôt que des règles concrètes. Nous voulons vous montrer ce qui est possible, afin que vous puissiez mélanger et assortir des aspects de différents flux de travail pour répondre à vos besoins individuels. Lors de l'évaluation d'un flux de travail pour votre équipe, il est surtout important que vous considériez la culture de votre équipe."_

Plus tard, ils ajoutent :

> _"Il n'y a pas de flux de travail Git unique. Il est important de développer un flux de travail Git qui est une amélioration de la productivité pour votre équipe. En plus de la culture de l'équipe, un flux de travail doit également compléter la culture de l'entreprise. Les fonctionnalités de Git comme les branches et les étiquettes doivent compléter le calendrier de publication de votre entreprise."_

Ils recommandent de travailler vers des branches de courte durée et de viser à minimiser et simplifier les retours en arrière.

### Commits écrasés ou non ?

Une autre question à laquelle je réfléchissais est de savoir ce qui est mieux : avoir un commit par fonctionnalité ou avoir de petits commits, afin que vous puissiez regarder l'annotation de certaines lignes et comprendre exactement pourquoi ce changement spécifique a été fait.

Maintenant que je me suis éduquée avec l'approche saine de l'article d'Atlassian mentionné ci-dessus, je pense que cela dépend fortement du projet. Pour les projets open source, avec beaucoup de contributeurs distants, il est préférable d'écraser, pour garder la vision de haut niveau du projet.

Pour les organisations stables dans lesquelles au moins une partie de l'équipe continue de travailler sur le projet à tout moment, il est préférable d'élaborer et de garder de petits commits, mais seulement si deux conditions sont remplies :

1. Avec des messages indicatifs et non "wip", "fix", etc.
2. Chaque commit en lui-même ne casse pas le build ou le produit, c'est-à-dire, si une fonctionnalité contient 3 commits, et que nous annulons 2 d'entre eux, le produit est stable et fonctionne bien.

### SEMVER

![Image](https://cdn-media-1.freecodecamp.org/images/ZQdKwHJylcIaBf6krUn2ueKOdoswkdDdPT3v)
_Le lien vers semver se trouve dans la page de publication de GitHub (coin inférieur droit)_

Semver, ou Semantic Versioning, est une spécification de convention de nommage pour les versions de projets de code. Vous pouvez trouver le [lien](https://semver.org/) sur la page de publication de GitHub.

L'idée est que chaque nouvelle publication aura un numéro de version de la forme x.y.z, par exemple : 1.1.2. Le x est incrémenté lorsqu'une version **majeure** est publiée — c'est-à-dire lorsqu'une API est rompue. Le y — **mineure** — nouvelle fonctionnalité mais les changements de l'API sont compatibles avec les versions précédentes, et le z — **correctif** — est incrémenté lors de la correction d'un bug de manière compatible avec les versions précédentes.

[C'est un outil NPM pour le vérifier](https://www.npmjs.com/package/semver).

#### Versionnage JavaScript

NPM [encourage](https://docs.npmjs.com/about-semantic-versioning) les développeurs JavaScript à respecter la méthodologie Semver. C'est définitivement quelque chose à prendre en considération lors de la création de votre propre flux de travail git.

### La mise à jour des bibliothèques externes ne doit pas faire partie de votre flux de travail Git

Lors de l'utilisation de NPM, si vous ne modifiez pas votre configuration par défaut, l'installation de nouveaux packages les installera avec un circonflexe : ^. Vous verrez quelque chose comme ceci dans votre package.json :

```
"dependencies": {    "my_dep": "^1.0.0",}
```

Si vous ne voulez pas avoir le circonflexe et que vous voulez utiliser une version fixe, vous pouvez installer comme ceci :

```
npm install foobar --save --save-exact
```

Ou mieux, vous pouvez le définir dans votre fichier de configuration `.npmrc`, comme ceci :

```
npm config set save=true
```

```
npm config set save-exact=true
```

Ce qui précède provient de l'article [Heroku's _Best Practices for Node.js Development_](https://devcenter.heroku.com/articles/node-best-practices#use-a-smart-npmrc). Mais pourquoi est-ce recommandé ?

Pour comprendre cela, je recommande vivement de lire [Pinning Dependencies and Lock Files](https://renovatebot.com/docs/dependency-pinning/#pinning-dependencies-and-lock-files) par Renovate. Pour résumer les principaux points :

* "Un fichier de verrouillage [package-lock.json] verrouillera les dépendances exactes et les _sous_-dépendances que votre projet utilise, afin que tout le monde exécutant `npm install` installe exactement les mêmes dépendances que la personne qui a mis à jour le fichier de verrouillage pour la dernière fois." Vous pouvez voir pourquoi il est problématique de ne pas utiliser votre fichier de verrouillage — les choses peuvent se casser en production en raison d'un changement dans une dépendance, et il sera très difficile de suivre le problème, car vous aurez une version différente de cette dépendance dans votre environnement local.
* Un fichier de verrouillage n'est pas fait pour être lisible par l'homme. Au cas où une nouvelle version d'une bibliothèque tierce que vous utilisez est publiée, et qu'elle se trouve dans la plage des versions autorisées dans le fichier package.json, le package-lock.json s'assurera que tout le monde utilise simplement la version fixe qui a été définie lors de sa dernière mise à jour. Par exemple, dans votre package.json, vous avez cette définition :

```
"dependencies": {    "my_dep": "^1.0.0",}
```

Maintenant, si l'équipe de `my_dep` publie une nouvelle version majeure, 2.0.0, elle ne sera jamais utilisée par votre application, sauf si vous la mettez à jour manuellement.

Mais si elles publient une version mineure, 1.2.0, alors elle ne sera pas utilisée par votre application non plus, dans aucun environnement, car le fichier de verrouillage s'assure qu'une version fixe est utilisée — celle qui était dans la plage la dernière fois qu'elle a été mise à jour.

Cependant, si vous mettez à jour votre fichier de verrouillage (en exécutant `npm update`, qui met à jour le fichier de verrouillage selon la règle définie dans le fichier package.json), 1.2.0 deviendra votre version fixe qui est définie dans le fichier de verrouillage, et il sera difficile de suivre cela.

* La recommandation habituelle est d'utiliser un fichier de verrouillage, que vous épingliez les dépendances ou non, et d'épingler même si vous avez un fichier de verrouillage.

Au cas où vous choisissez d'épingler les dépendances, vous avez besoin d'un mécanisme automatique pour les mettre à jour, afin que les corrections de sécurité et autres nouvelles fonctionnalités utiles ne vous surprennent pas tout le temps et n'interfèrent pas avec votre plan de produit. Renovate est une solution pour cela, et [Dependabot](https://dependabot.com/) est également une bonne option. Je suis sûr que vous pouvez en trouver d'autres. Je pense que c'est une excellente solution même si vous n'épinglez pas les versions, car il y a toujours de nouvelles versions qui peuvent être en dehors de la plage.

### Résumé

1. Il est important pour tout ingénieur de connaître différents flux de travail Git et de comprendre la méthodologie semver et comment utiliser les fichiers de verrouillage.
2. Différentes équipes ont besoin de différents flux de travail. Cela dépend du marché et de l'équipe, et le flux de travail doit rendre la vie aussi facile que possible pour les ingénieurs qui l'utilisent, leur permettant de publier du code stable rapidement.
3. Je pense que le flux de travail le plus proche de ce avec quoi je veux travailler est décrit dans cet article — [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow).
4. Il est agréable d'utiliser _semver_ et des versions fixes, avec un service qui aide à mettre à jour les bibliothèques tierces.
5. Je suis une grande fan des modèles de conception et j'ai adoré lire les différents modèles pour travailler avec Git.