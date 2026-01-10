---
title: Comment utiliser Gatsby pour créer votre blog et y travailler depuis votre
  téléphone
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T09:46:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-blog-using-gatsby-from-your-phone-e92a99851a04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YFDeSO9ljiYaszZk1FXm8Q.jpeg
tags:
- name: blog
  slug: blog
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Gatsby pour créer votre blog et y travailler depuis votre
  téléphone
seo_desc: 'By Hu Chen

  Recently, I decided to migrate my blog to Gatsby. Gatsby is a blazing fast static
  site generator based on React.

  The Issue

  Why do people love to write on platforms like Medium rather than using static site
  generator?

  There are two kinds of...'
---

Par Hu Chen

Récemment, j'ai décidé de migrer mon blog vers [Gatsby](https://www.gatsbyjs.org/). Gatsby est un générateur de site statique ultra-rapide basé sur React.

### **_Le Problème_**

#### **_Pourquoi les gens aiment-ils écrire sur des plateformes comme Medium plutôt que d'utiliser un générateur de site statique ?_**

Il existe deux types de personnes : celles qui écrivent sur des plateformes comme Medium et celles qui codent leur blog elles-mêmes en utilisant des générateurs de sites statiques.

Il y a de nombreux avantages à écrire sur des plateformes publiques comme Medium plutôt que sur des générateurs de sites statiques. Si vous écrivez sur des plateformes publiques, vous pouvez écrire sur un ordinateur portable et éditer sur votre téléphone. Une fois que vous avez terminé d'écrire, il vous suffit de cliquer sur le bouton "Publier". Tout est fait, votre blog est en ligne et vous pouvez atteindre votre audience immédiatement.

D'un autre côté, si vous écrivez un blog avec un générateur de site statique, vous devrez vous souvenir de tous les scripts, prévisualiser le blog sur `localhost`, construire le blog pour la production, commiter et pousser vos changements sur GitHub, et déployer votre site en public. Si quelque chose ne va pas, vous devrez peut-être répéter certaines étapes et attendre quelques minutes jusqu'à ce que le blog en ligne soit ce que vous voulez.

Vous finirez par passer beaucoup plus de temps à faire des choses sans importance plutôt qu'à écrire réellement.

#### **_Pourquoi devriez-vous écrire sur Gatsby plutôt que sur des plateformes publiques ?_**

Je suppose que c'est pourquoi les gens finissent par abandonner l'écriture en utilisant un générateur de site statique et écrivent sur Medium à la place. Mais il y a quelque chose que Medium ou Wordpress ne peuvent pas fournir : plus vous écrivez, plus vous voulez garder vos écrits dans un endroit sécurisé, dans un format simple, tout comme vous pourriez garder vos journaux intimes pendant des années.

Mais imaginez qu'un jour vous voulez migrer tout ce que vous avez écrit de Medium vers un autre endroit. C'est à ce moment-là que vous espérez avoir écrit tout en Markdown et avoir un site hébergeant ces fichiers Markdown.

#### **_Mais comment puis-je rendre l'écriture dans Gatsby aussi facile que l'écriture sur Medium ?_**

Écrire en utilisant un générateur de site statique ne doit pas être difficile. Je crois toujours que plus il est facile d'écrire et de publier votre blog, plus vous écrirez. Après avoir essayé et recherché différentes configurations, je suis assez satisfait du résultat.

Dans ma configuration avec Travis CI, `git push` est le nouveau bouton "Publier". Tout ce que vous avez à faire est de commiter et pousser votre code. Et je vais aussi partager comment éditer le blog sur votre téléphone.

J'ai divisé cet article en cinq sections :

1. **Comment créer un blog Gatsby**
2. **Configurer Github Pages pour héberger votre blog**
3. **Configurer Travis pour le déploiement automatique**
4. **Ajouter un nouveau blog et le publier**
5. **Bonus : Comment écrire un blog sur votre téléphone**

### 1. Comment créer un blog Gatsby

Il existe [beaucoup](https://scotch.io/tutorials/zero-to-deploy-a-practical-guide-to-static-sites-with-gatsbyjs) de [tutoriels](https://www.gatsbyjs.org/tutorial/) sur la façon de configurer un blog en utilisant Gatsby qui discutent de toutes les fonctionnalités puissantes que Gatsby fournit. Cet article ne se concentrera pas sur cela, mais je montrerai tout de même quelques étapes de base pour mettre votre blog en route.

Je suppose que vous êtes déjà un développeur JavaScript et que vous connaissez quelques bases de `npm`, `yarn`, et de l'intégration continue. Pour ce tutoriel, j'utiliserai `yarn` mais n'hésitez pas à utiliser `npm`.

Tout d'abord, installez `gatsby-cli` et créez un nouveau dépôt en utilisant le modèle de blog officiel de Gatsby.

```
$ yarn global add gatsby-cli
```

```
$ gatsby new gatsby-blog https://github.com/gatsbyjs/gatsby-starter-blog
```

```
$ cd gatsby-blog
```

```
$ gatsby develop
```

Maintenant, ouvrez `localhost:8000` dans votre navigateur et vous devriez voir le blog généré dans votre navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/my9H4GVkyo4urZ6OjGV1GKGkVRFniTSMJZZu)

### 2. Configurer Github Pages pour héberger votre blog

Maintenant, hébergeons le blog publiquement.

Il existe de nombreuses options pour héberger votre site gratuitement, mais je préfère mettre à la fois le code source et le code de production dans un seul endroit. Puisque je commite mon code sur GitHub, je préfère héberger mon site en utilisant [GitHub Pages](https://pages.github.com). Mais n'hésitez pas à utiliser d'autres services pour héberger votre site statique.

> Note : Plus tard, j'aurai besoin d'utiliser [Travis CI](https://travis-ci.org/) pour déployer automatiquement le site web après chaque commit, vous devrez donc peut-être vérifier quelles [plateformes ils supportent](https://docs.travis-ci.com/user/deployment/) pour le déploiement.

Maintenant, créez un dépôt nommé **username.github.io**. Ce sera le dépôt à la fois du code source de votre site et de la version de production générée.

Parce que GitHub Page sert le contenu depuis la branche `master`, vous devrez déployer le contenu du dossier `public` généré par la commande `yarn build` vers la branche `master`. Nous devrons mettre notre code source dans une autre branche. Nous l'appellerons `develop`.

Créons un commit initial et renommons la branche en `develop`.

```
$ git init
```

```
$ git add .
```

```
$ git commit -m "Initial Commit"
```

```
$ git branch -m develop
```

Maintenant, nous devons pousser notre code vers GitHub. Si vous avez déjà créé le dépôt nommé **username.github.io**, poussez votre code dans le dépôt.

```
$ git remote add origin git@github.com:username/username.github.io.git
```

```
$ git push -u origin develop
```

Assurez-vous qu'il n'y a pas de branche `master` dans votre dépôt GitHub, et que la branche par défaut est définie sur `develop`.

### 3. Configurer Travis pour le déploiement automatique

C'est une étape importante. Bien que nous puissions utiliser `yarn deploy` pour déployer, cela représente trois étapes supplémentaires : générer le dossier public, déployer vers GitHub Page, attendre et vérifier en ligne.

Mais nous pouvons nous débarrasser de ces étapes avec [Travis CI](https://travis-ci.org/). Travis CI est un service d'intégration continue hébergé et distribué, utilisé pour construire et tester des projets logiciels hébergés sur GitHub.

Si votre projet est public sur GitHub, Travis CI est gratuit. Maintenant, créez un compte Travis en vous connectant à votre GitHub et ajoutez votre dépôt dans Travis.

#### Créer un fichier .`travis.yml` à la racine du projet

```
language: node_js
```

```
cache:
```

```
  directories:
```

```
    - ~/.npm
```

```
notifications:
```

```
  email:
```

```
    recipients:
```

```
      - chen@huchen.me
```

```
    on_success: always
```

```
    on_failure: always
```

```
node_js:
```

```
  - '9'
```

```
git:
```

```
  depth: 3
```

```
script:
```

```
  - yarn build
```

```
deploy:
```

```
  provider: pages
```

```
  skip-cleanup: true
```

```
  keep-history: true
```

```
  github-token: $GITHUB_TOKEN
```

```
  local-dir: public
```

```
  target-branch: master
```

```
  on:
```

```
    branch: develop
```

Vous pouvez également consulter [Gist](https://gist.github.com/huchenme/fc3afa589cd64d6cdedad92fb7d70851). Laissez-moi expliquer cette configuration :

* **notifications** : J'ai demandé à Travis de m'envoyer un email en cas de succès ou d'échec de la construction. Par défaut, il n'envoie un email que si le statut change (par exemple, s'il était réussi mais passe à échoué, ou s'il était échoué et passe à corrigé). Mais je voulais recevoir un email même en cas de succès pour pouvoir double-vérifier en ligne.
* **git:depth:3** : J'ai demandé à Travis d'utiliser une profondeur de `3` lors du clonage du projet, car cela aidera à rendre la construction plus rapide.
* **script** : Le script que Travis doit exécuter est `yarn build`, qui crée des fichiers statiques dans le dossier `public` pour un déploiement ultérieur.
* **deploy** : J'ai demandé à Travis de déployer sur GitHub Pages après le succès du script `yarn build`. Il utilise le `$GITHUB_TOKEN` que j'ai défini dans les paramètres du dépôt Travis (j'y viendrai ensuite), pousse le contenu du dossier `public` dans la branche `master` de GitHub, et ne doit déclencher le déploiement que sur la branche `develop`. Cliquez [ici](https://docs.travis-ci.com/user/deployment/pages/) pour en savoir plus sur la configuration de déploiement.

#### Créer un token pour que Travis puisse pousser vers GitHub

Vous devrez [générer un token d'accès personnel](https://help.github.com/articles/creating-an-access-token-for-command-line-use/) avec le scope `public_repo` ou `repo` (repo est requis pour les dépôts privés) pour permettre à Travis de pousser du code vers le dépôt GitHub. Cela est nécessaire car Travis exécute `yarn build` et doit pousser le dossier `public` dans la branche `master` où GitHub Pages est servi.

![Image](https://cdn-media-1.freecodecamp.org/images/C1S4VhjIRO8g3RHkXUZClU-1I7oSQAW9JE87)

Une fois le token créé, vous devrez le **copier et coller** dans les paramètres de votre dépôt Travis.

![Image](https://cdn-media-1.freecodecamp.org/images/qKfFkOcgYCXlEwmPeghLMQiBiGsIqYtSj22J)

Maintenant, ajoutez `.travis.yml` dans git et poussez les changements vers GitHub.

```
$ git add .travis.yml
```

```
$ git commit -m "Add Travis config file"
```

```
$ git push origin develop
```

Maintenant, vous pouvez vérifier le statut sur Travis. Vous devriez voir le statut de Travis passer à jaune (en cours d'exécution). Si tout est correct, il passera au vert dans quelques minutes, et vous devriez recevoir un email concernant la construction réussie. Vous pouvez visiter `https://username.github.io` pour voir votre blog que vous venez de créer.

![Image](https://cdn-media-1.freecodecamp.org/images/tybmW8vB9ePsasJiyCPD-yrEwvDN27VIRZYg)

### 4. Ajouter un nouveau blog et le publier

Voici la partie amusante. Maintenant, je vais démontrer à quel point il est facile de publier un nouveau blog en utilisant ce processus.

Maintenant, ajoutons un nouveau blog.

1. Créez un fichier `index.md` dans `src/pages/new-blog;` . Vous devrez également créer un nouveau dossier `new-blog`.
2. Mettez un contenu simple dans `index.md`.

```
---
```

```
title: Bonjour Nouveau Blog
```

```
date: "20180416T23:46:37.121Z"
```

```
---
```

```
Bonjour le Monde
```

3. Commitez ce nouveau fichier et poussez-le vers GitHub

```
$ git add .
```

```
$ git commit -m "Add a new blog"
```

```
$ git push origin develop
```

4. Attendez que Travis termine et vérifiez en ligne. Après avoir reçu un email quelques minutes plus tard, vous pouvez vérifier `https://username.github.io` à nouveau. Vous devriez voir votre nouveau blog dans la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/7fBP55Hcdm30UdOefXqsvJmnleiZTzyYDfaw)

### 5. Bonus : comment écrire le blog depuis votre téléphone

Je veux supprimer une autre barrière à l'écriture de votre blog. Je ne pouvais écrire mon blog que lorsque j'étais avec mon ordinateur portable, mais je me suis demandé : pourrais-je utiliser mon téléphone pour élaborer des idées et éditer ?

Cela s'est avéré être assez facile. Tout ce que vous avez à faire est d'[ajouter vos fichiers Desktop et Documents à iCloud Drive](https://support.apple.com/en-sg/HT206985) et de mettre votre dépôt soit dans Desktop soit dans Documents. Cela peut prendre un certain temps initialement, mais une fois que tout est téléchargé, les mises à jour sont instantanées et je peux voir mes modifications sur mon ordinateur portable, mon iPhone et mon iPad en même temps sans aucun problème.

Il existe de nombreuses applications markdown sur iPhone. Personnellement, je trouve que [IA Writer](https://ia.net/writer) est la meilleure : elle supporte toutes les plateformes, elle est élégante et axée sur l'écriture, et elle supporte très bien iCloud Drive.

Bien que je puisse également configurer mon iPhone pour effectuer des commits et des pushes git, je pense que ce n'est pas nécessaire. Si la partie la plus difficile de l'écriture d'un blog est déjà faite, utiliser un ordinateur portable pour faire la vérification finale et commiter le code n'est pas un gros problème pour moi. `git push` est aussi simple que de cliquer sur le bouton "Publier" sur Medium.

### C'est tout !

Nous sommes arrivés à la fin de ce tutoriel. Merci d'avoir lu jusqu'ici.

Cet article n'est que la partie émergée de l'iceberg des fonctionnalités de Gatsby. Je suis impressionné par sa flexibilité et ses fonctionnalités puissantes. Vous devriez définitivement consulter son [tutoriel officiel](https://www.gatsbyjs.org/tutorial/).