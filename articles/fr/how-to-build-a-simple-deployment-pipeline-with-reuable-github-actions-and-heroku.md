---
title: Comment créer un pipeline de déploiement simple avec des actions GitHub réutilisables
  et Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-31T17:25:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-deployment-pipeline-with-reuable-github-actions-and-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/AdobeStock_131006414-1.jpeg
tags:
- name: deployment
  slug: deployment
- name: GitHub Actions
  slug: github-actions
- name: Heroku
  slug: heroku
seo_title: Comment créer un pipeline de déploiement simple avec des actions GitHub
  réutilisables et Heroku
seo_desc: "By Liz Johnson\nIf you've been using GitHub for a while, you've probably\
  \ heard of or used GitHub actions. \nIf you haven't heard of Github Actions or used\
  \ them before, you can use them for automating your build, test, or deployment pipelines.\
  \ You can c..."
---

Par Liz Johnson

Si vous utilisez GitHub depuis un certain temps, vous avez probablement entendu parler ou utilisé les actions GitHub. 

Si vous n'avez jamais entendu parler des actions GitHub ou ne les avez jamais utilisées, sachez que vous pouvez les utiliser pour automatiser vos pipelines de build, de test ou de déploiement. Vous pouvez créer des workflows qui seront déclenchés lors de certaines actions, comme l'ouverture d'une pull request ou le push vers une branche. 

Ces actions sont utiles pour créer des pipelines de build qui automatisent les déploiements. Elles aident également à maintenir l'intégrité des branches en exécutant des tests sur tous les pushes/pull-requests.

Voici un workflow simple qui exécuterait des tests chaque fois que vous poussez des branches ou ouvrez des pull-requests dans GitHub :

```
---
name: Exécuter les tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Configuration et exécution des tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec
```

Le déclencheur est listé après le tag "on". Ce workflow est déclenché lors des pushes vers le dépôt distant. Ci-dessous, vous verrez des exemples où il y a plusieurs déclencheurs pour le workflow. Si vous avez plusieurs déclencheurs, vous pouvez les lister dans des crochets comme un tableau. 

Ensuite, vous avez votre tag jobs. Sous ce tag, vous pouvez lister les différents jobs que vous souhaitez exécuter. Vous pouvez avoir quelques jobs de test différents pour les tests unitaires, les tests d'intégration, et peut-être un job de build pour construire une image qui est poussée vers un dépôt distant. 
  
Dans le job, vous avez diverses étapes. La première étape est généralement l'étape de checkout. Les actions GitHub vont lancer un runner de machine virtuelle pour exécuter vos jobs, vous voudrez donc inclure toutes les étapes nécessaires pour configurer cette machine virtuelle pour votre application. 

Cela signifie que la première chose que vous voudrez faire est de récupérer le code sur la machine virtuelle. Cela se fait avec l'étape de checkout ci-dessus. 

Ensuite, votre job doit donner à GitHub des instructions sur la façon d'exécuter des choses comme les tests. Le workflow ci-dessus exécute tout via Docker. Le runner GitHub peut voir le fichier docker-compose lorsqu'il checke le projet. Ensuite, il peut exécuter les trois étapes Docker listées ci-dessus pour lancer un conteneur et ensuite exécuter les tests unitaires à l'intérieur de ce conteneur.  
  
Avec ce workflow, si vous ouvriez une pull-request dans GitHub et que la branche avait des tests échouant, vous recevriez une alerte vous indiquant que vous introduisez des changements cassants avec une sortie comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-189.png)
_Exemple d'alerte GitHub Actions_

Ces workflows peuvent parfois devenir complexes et très impliqués. Dans ce tutoriel, je vais expliquer quelques moyens simples pour nettoyer vos workflows afin d'éviter de copier-coller des configurations yaml. 

Je vais ensuite expliquer comment vous pouvez créer un pipeline de déploiement simple qui impose qu'un job réussisse avant que l'autre ne s'exécute.

## Où vous pourriez trouver des jobs dupliqués

Supposons que vous avez un job qui exécute vos tests, et que ce job doit être exécuté dans plusieurs workflows différents. Vous voulez exécuter des tests sur toutes les pull-requests. Vous voulez également les exécuter sur les merges vers main d'une manière qui bloque l'étape de build/déploiement de production si les tests ne passent pas.

Peut-être que votre première idée ici est de construire deux workflows, l'un nommé test et l'autre nommé deploy. Le workflow de test aurait un job : configurer et exécuter tous les tests unitaires. Dans l'autre workflow, vous pouvez copier le yaml du job de test dans le workflow de test et le coller comme premier job dans votre workflow de déploiement. 

Votre workflow de test ressemblerait à quelque chose comme ceci :

```
---
name: Exécuter les tests
on: pull-request

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Configuration et exécution des tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec

```

Et votre workflow de déploiement ressemblerait à quelque chose comme ceci :

```
---
name: Déployer
on:
  push:
    branches: [main]

jobs:
  tests:
  	runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Configuration et exécution des tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec
  deploy:
    name: deploy
    runs-on: ubuntu-latest
    steps:
      - run: echo 'Le workflow de déclenchement a réussi, déploiement en cours'
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.13 # Cette action
        with:
          usedocker: true

```

Le workflow de déploiement permet aux deux jobs (test et deploy) de s'exécuter lors des merges vers main, mais il n'empêchera pas réellement le job de déploiement de s'exécuter si les tests échouent. 

Mais nous pouvons améliorer cela de deux manières : la première est d'utiliser des actions GitHub réutilisables afin que nous puissions éliminer le copier-coller du yaml du job. La seconde est d'utiliser le mot-clé "needs" de GitHub afin que nous puissions rendre notre job de déploiement dépendant de la réussite de notre job de test.

J'ai construit cela [ici](https://github.com/lizzypy/base-app-liz) et je vais passer en revue cet exemple. 

## Comment créer des actions GitHub réutilisables

GitHub a [un article de blog sur les workflows réutilisables](https://github.blog/2022-02-10-using-reusable-workflows-github-actions/) que je recommande. Il va un peu plus loin que ce que je vais faire ici. Mais l'information importante pour nous est l'explication de ce qu'est un workflow réutilisable. Un workflow réutilisable est celui où vous créez un job à un endroit et puis vous l'appelez dans un workflow séparé.

Si je voulais que mon workflow de test soit réutilisable, je devrais ajouter un déclencheur étiqueté "workflow_call". Je veux également que mon workflow soit déclenché sur push et pull-requests. Donc mes déclencheurs ressembleraient à quelque chose comme ceci :

```
---
name: Exécuter le processus CI pour l'application
on: [workflow_call, push, pull_request, workflow_dispatch]
```

Et le workflow complet ressemblerait à ceci :

```
---
name: Exécuter les tests
on: [workflow_call, push, pull_request, workflow_dispatch]


jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Configuration et exécution des tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec
```

Pour réutiliser le workflow de test dans un workflow de déploiement (où je veux exécuter des tests et déployer mon application), je pourrais faire quelque chose comme ceci :

```
jobs:
    test:
        uses:./.github/workflows/test.yml
```

Cela permettrait au job de test d'être exécuté dans un workflow séparé sans avoir à copier le yaml associé au job de test d'un workflow à un autre.

## Jobs dépendants

C'est bien, mais nous ne voulons pas seulement que notre job de test soit réutilisé dans notre workflow de déploiement. Si le job de test échoue dans le workflow de déploiement, nous voulons que cela _bloque_ le déploiement.

Maintenant, nous pouvons examiner le mot-clé "needs" qui est documenté [ici](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions). En utilisant "needs", nous pouvons exiger que le job de déploiement ne s'exécute même pas à moins que le job de test ne soit réussi.

Avant de plonger dans l'utilisation du tag "needs", laissez-moi expliquer brièvement ce que fait le job de déploiement. 

J'ai déployé l'application d'exemple en utilisant Heroku. Au lieu d'utiliser le dépôt distant Heroku Git, j'ouvre des pull-requests contre une branche main. Lors des merges vers main, j'utilise cette [action GitHub open source](https://github.com/AkhileshNS/heroku-deploy) pour déployer la branche main vers Heroku.  

Mon job de déploiement ressemblerait à quelque chose comme ceci :

```
deploy:
    name: deploy
    runs-on: ubuntu-latest
    steps:
      - run: echo 'Le workflow de déclenchement a réussi, déploiement en cours'
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.13 # Cette action
        with: 
            usedocker: true
```

Le tag "usedocker" ci-dessus spécifie que je veux déployer cette application sur Heroku en construisant et en poussant une image docker vers le Heroku Container Registry. Si vous parcourez le code source de l'action de déploiement Heroku qui est référencée ci-dessus, vous verrez que lorsque je définis "usedocker" sur "true", il exécutera cette commande :

`heroku container:push`

Cela peut être vu [ici](https://github.com/AkhileshNS/heroku-deploy/blob/master/index.js#L76).

Si nous voulons que ce job nécessite une exécution réussie des tests avant d'exécuter le job de déploiement, nous pouvons ajouter un job de test à notre workflow qui référence notre job de test réutilisable que nous avons créé :

```
---
name: Déployer
on:
  push:
    branches: [main]

jobs:
  tests:
    uses: ./.github/workflows/test.yml 
```

Maintenant, nous pouvons ajouter le tag `needs` à notre action de déploiement et notre fichier yaml de workflow complet ressemblerait à quelque chose comme ceci :

```
---
name: Déployer
on:
  push:
    branches: [main]

jobs:
  tests:
    uses: ./.github/workflows/test.yml
  deploy:
    name: deploy
    needs: [ tests ]
    runs-on: ubuntu-latest
    steps:
      - run: echo 'Le workflow de déclenchement a réussi, déploiement en cours'
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.13 # Cette action
        with:
          usedocker: true
```

Et c'est tout ! Maintenant, lorsque nous fusionnons des branches vers main, GitHub nous donne une visualisation de nos jobs dépendants qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-159.png)

  
Si nous avions un workflow plus complexe, nous pourrions voir exactement quel job échoue. 

## Conclusion

Avec ces étapes, nous pouvons nettoyer nos fichiers yaml de workflow pour référencer des jobs/workflows existants lorsque cela est possible. Nous pouvons également construire un pipeline simple d'actions dépendantes où une étape dépend du succès d'une étape précédente.  

Ce sont les débuts d'un pipeline CI/CD qui peut permettre des déploiements fréquents. À son tour, cela nous permettra de fournir de nouvelles fonctionnalités et des correctifs aux utilisateurs plus rapidement.