---
title: Couvrez votre package NPM avec Jest et Codecov ☂️
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T17:54:02.000Z'
originalURL: https://freecodecamp.org/news/get-your-npm-package-covered-with-jest-and-codecov-9a4cb22b93f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HVSEe7dPPG_hCmRD_ENoxw.jpeg
tags: []
seo_title: Couvrez votre package NPM avec Jest et Codecov ☂️
seo_desc: 'By Carl-Johan Kihl

  Introduction

  Let’s talk about code coverage, and how you can do coverage reports in Jest and
  Codecov.

  What is Code Coverage?

  If you’re familiar with testing. You know its main purpose:


  Tests gives the developers freedom to make ch...'
---

Par Carl-Johan Kihl

### Introduction

Parlons de la couverture de code et de la façon dont vous pouvez générer des rapports de couverture dans [Jest](https://jestjs.io/) et [Codecov](https://codecov.io/).

### Qu'est-ce que la couverture de code ?

Si vous êtes familier avec les tests, vous connaissez leur objectif principal :

> _Les tests donnent aux développeurs la liberté d'apporter des modifications et de refactoriser le code avec la confiance que tout devrait fonctionner correctement tant que tous les tests automatisés passent._

Cependant, si les tests unitaires ne couvrent pas tous les scénarios, il reste une chance que vos modifications puissent casser quelque chose. C'est pourquoi nous avons la couverture de code : la mesure de **combien** de la base de code est couverte par des tests automatisés.

**Sans analyse de la couverture de code, vos tests ont perdu leur objectif principal.**

Cela est important lorsque votre projet grandit et que de nombreux développeurs sont impliqués.

✅ Nous pouvons maintenir la qualité de nos tests lorsque du nouveau code est ajouté.   
✅ Nous obtenons une compréhension plus approfondie des tests existants.  
✅ Donner aux développeurs la confiance de refactoriser le code sans s'inquiéter de casser des choses.   
✅ Nous pouvons attraper les flux non testés **avant** qu'ils ne causent des problèmes.

D'accord, maintenant que nous savons ce qu'est la couverture de code, mettons-la en œuvre ! ?

### Prérequis

Pour garder cet article court et concis, je vais commencer ici : [Step by Step Building and Publishing and NPM Typescript Package](http://bit.ly/2zAC2nK).

Ce qui a été fait jusqu'à présent :

✅ Configuration d'un package de base [NPM](https://github.com/caki0915/my-awesome-greeter/tree/basic-package)  
✅ Ajout de tests avec [Jest](https://jestjs.io/)  
✅ Écriture d'un test de base

Si votre projet est déjà configuré avec Jest, vous êtes prêt à partir. ? Sinon, je vous recommande de cloner ou de fork le dépôt pour cet article afin de commencer à partir d'une base de [package NPM](https://github.com/caki0915/my-awesome-greeter) :

```
git clone git@github.com:caki0915/my-awesome-greeter.git && cd my-awesome-greeter &&git checkout basic-package && npm install
```

Si vous êtes intéressé par la construction de packages NPM, je vous recommande [mon article précédent ici](http://bit.ly/2zAC2nK).

Très bien, maintenant que tout est configuré, c'est parti !

### Créer des rapports de couverture dans Jest

Créer des rapports de couverture dans Jest est facile. Il suffit d'ajouter cette ligne dans votre fichier de configuration Jest :

```
"collectCoverage":true
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jvqy8Brvr_VLF0GOOv-odA.png)
_C'est à quoi ressemble mon fichier de configuration Jest (jestconfig.json)_

**collectCoverage :** Doit être défini sur true si vous voulez que Jest collecte des informations de couverture lors de l'exécution de vos tests. _(Les tests s'exécuteront un peu plus lentement, donc c'est false par défaut.)_

Assurez-vous que votre commande de script `test` dans votre fichier **package.json** exécute Jest avec votre fichier de configuration.

```
"test": "jest --config jestconfig.json"
```

Très bien ! Exécutez `npm test` dans votre terminal, et voilà ! Vous aurez un nouveau dossier avec des fichiers de couverture de code générés pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8eP9WhWo1VrmS_kUg7LssA.png)
_Exécutez npm test dans le terminal_

![Image](https://cdn-media-1.freecodecamp.org/images/1*x4dsZDfiBpu_C_NjXR3NBg.png)
_Données de couverture de code générées pour vous !_

N'oubliez pas d'ajouter le dossier de couverture à `.gitignore`. Nous ne voulons pas de fichiers de build dans notre dépôt. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*k9TVX54mc_hPWfmoRQj9kg.png)

### Faire quelque chose d'utile avec vos rapports

D'accord, c'est cool, nous avons généré un dossier avec quelques fichiers, mais que devons-nous faire avec ces informations ? ?

Tout d'abord, vous pouvez examiner manuellement le rapport de couverture sur une page HTML générée. Ouvrez `/coverage/lcov-report/index.html` dans votre navigateur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3siDGI3_o1etjgGgL93vEQ.png)
_coverage/lcov-report/index.html_

D'accord, c'est bien, mais devons-nous VRAIMENT examiner manuellement les rapports à chaque build ??

Non, vous ne devriez pas. Vous devriez publier les rapports en ligne pour en faire quelque chose d'utile. Dans cet article, nous allons utiliser un outil de rapport de couverture appelé [codecov.io](http://codecov.io).

**Codecov** est gratuit pour les projets open-source. Il porte les rapports de couverture de code au niveau supérieur. Avec Codecov, nous pouvons également générer automatiquement des badges et l'exécuter sur des builds d'intégration continue. _(Plus d'informations à ce sujet plus tard.)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*LDkR3IU8CgySEN9eRUlxRg.png)
_Un badge de couverture avec un lien vers un rapport de couverture sur **codecov.io dans un README.md de package_

Inscrivez-vous sur [https://codecov.io/](https://codecov.io/) et suivez le guide pour vous connecter à Github et à votre dépôt. Après cela, vous devriez voir un écran comme celui-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5LmuJfwbiEFLzM5Iv5wZgQ.png)

Bien ! Pour l'instant, cette page sera vide puisque vous n'avez pas encore téléchargé de rapports, alors corrigeons cela. Dans le terminal, exécutez :

```
npm install --save-dev codecov
```

Normalement, vous voulez télécharger les rapports à la fin d'une build d'intégration continue, mais pour cet article, nous allons télécharger les rapports depuis notre machine locale. Dans le terminal, exécutez :   
_(Remplacez <Votre token> par votre token de dépôt trouvé dans codecov.io)

```
./node_modules/.bin/codecov --token="<Votre token>"
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*npeviaPBYnSHbbiZ0-iCzQ.png)

Succès ! Maintenant, vous pouvez voir votre rapport en ligne sur codecov.io. ? ?

```
https://codecov.io/gh/<Nom d'utilisateur Github>/<Nom du dépôt>/
```

### Ajouter un badge à votre README.md

Les badges sont importants, surtout pour les packages NPM. Ils donnent une première impression de haute qualité lorsque vous voyez un beau badge de couverture de code dans [npmjs](https://www.npmjs.com/) et [Github](https://github.com/).

Dans votre **README.md**, ajoutez la ligne suivante :  
_(Remplacez <Nom d'utilisateur Github>, <Nom du dépôt> et <Nom de la branche> par vos informations)

```
[![Codecov Coverage](https://img.shields.io/codecov/c/github/<Nom d'utilisateur Github>/<Nom du dépôt>/<Nom de la branche>.svg?style=flat-square)](https://codecov.io/gh/<Nom d'utilisateur Github>/<Nom du dépôt>/)
```

Dans mon cas, cela ressemblera à ceci :

```
[![Codecov Coverage](https://img.shields.io/codecov/c/github/caki0915/my-awesome-greeter/coverage.svg?style=flat-square)](https://codecov.io/gh/caki0915/my-awesome-greeter/)
```

Super ! Maintenant, vous pouvez montrer au reste du monde que vous utilisez des tests unitaires et des rapports de couverture de code ! ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*pgmvJpcddTB5QGExR3kfag.png)
_Un badge de couverture avec un lien vers votre rapport d'analyse de couverture._

### Résumé

Si vous utilisez des tests, la génération de rapports de couverture de code est un must et elle devrait s'exécuter chaque fois que vous faites une pull-request ou que vous apportez des modifications à vos branches.

Vous pouvez trouver mon [package de démarrage NPM ici sur Github.](https://github.com/caki0915/my-awesome-greeter)  
C'est une base éducative pour les meilleures pratiques de développement de packages NPM. Les commentaires, les forks et les PR sont les bienvenus. ?

### Qu'est-ce qui suit ?

Si vous n'utilisez pas encore l'intégration continue (CI), il est temps de la configurer.   
Dans mon prochain article, je vais couvrir l'intégration continue avec la couverture de code pour les packages NPM.

Si vous trouvez cet article utile, veuillez lui donner quelques applaudissements et me suivre pour plus d'articles sur le développement.

#### Bonne chance pour la construction de votre package génial ! ? ?