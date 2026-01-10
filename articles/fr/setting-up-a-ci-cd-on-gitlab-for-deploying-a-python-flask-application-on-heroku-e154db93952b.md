---
title: Configuration de CI/CD sur GitLab pour déployer une application Python Flask
  sur Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-13T04:31:28.000Z'
originalURL: https://freecodecamp.org/news/setting-up-a-ci-cd-on-gitlab-for-deploying-a-python-flask-application-on-heroku-e154db93952b
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb550740569d1a4cad5db.jpg
tags:
- name: Flask Framework
  slug: flask
- name: GitLab
  slug: gitlab
- name: Heroku
  slug: heroku
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: Configuration de CI/CD sur GitLab pour déployer une application Python
  Flask sur Heroku
seo_desc: 'By Bharath Kallur

  Recently I came across a challenge to deploy a Python Flask web application to Heroku.
  The code of the App was hosted in GitLab.

  Heroku supports deploying an App from GitHub, Dropbox along with the usual Heroku
  git. It had been quit...'
---

Par Bharath Kallur

Récemment, j'ai été confronté à un défi : déployer une application web Python Flask sur Heroku. Le code de l'application était hébergé sur GitLab.

Heroku prend en charge le déploiement d'une application à partir de GitHub, Dropbox ainsi que le git Heroku habituel. Cela faisait un moment que je n'avais pas utilisé Heroku. Je me demandais si je pouvais déployer le code directement depuis mon dépôt GitLab au lieu d'utiliser l'une des sources mentionnées ci-dessus.

Je n'ai pas trouvé d'informations ou de documentation sur le déploiement d'applications hébergées dans un dépôt GitLab vers [Heroku](https://devcenter.heroku.com/categories/deployment). J'ai un peu navigué sur GitLab et il s'avère que, outre l'aide pour tester et construire votre projet, GitLab CI peut également vous aider à [déployer](https://docs.gitlab.com/ce/ci/environments.html) votre application sur votre infrastructure d'hébergement. J'étais maintenant intrigué.

Avant de me plonger dans la manière dont j'ai déployé l'application, j'aimerais expliquer les avantages de l'utilisation de GitLab ou GitHub lorsque vous pouvez facilement faire les choses avec Heroku Git.

1. **Maintenance du code plus facile** - Avec des services d'hébergement de dépôts de code comme GitHub et GitLab, la maintenance du code est facile.
2. **Personnalisation des pipelines** - Avec GitLab, nous pouvons écrire notre propre fichier [yaml](http://yaml.org/) et inclure les bibliothèques nécessaires pour exécuter notre application.
3. **Pour une meilleure compréhension de l'intégration continue et du développement continu (CI/CD)** - Pour les débutants, cette configuration vous aide à comprendre le flux de travail de codage de test -> contrôle de version -> maintenance du code -> déploiement de l'application.

Voici les étapes nécessaires pour déployer votre application hébergée sur GitLab vers Heroku. Les étapes ici supposent que vous avez déjà une bonne compréhension de Python, Flask, du contrôle de version, de GitLab et de Heroku. Ce guide est également utile pour quelqu'un qui commence tout juste. Je l'ai gardé aussi simple que possible pour que les choses fonctionnent rapidement.

### Téléchargement du projet sur GitLab

1. Créez un environnement virtuel Python pour que nous puissions l'utiliser. Accédez à l'environnement virtuel.
2. Créez une application Python Flask exemple sur votre machine.
3. Vérifiez que tout fonctionne correctement.
4. Exécutez la commande `pip freeze > requirements.txt` depuis le dossier principal de l'application pour capturer toutes les dépendances nécessaires à l'exécution de votre application.
5. Créez un Procfile qui est utilisé par Heroku pour déclarer quelles commandes sont exécutées par votre application sur la plateforme Heroku. Le Procfile contient généralement le serveur web utilisé pour exécuter l'application. Dans notre cas, utilisons Gunicorn, le serveur WSGI HTTP Python par défaut. Le contenu de votre Procfile sera `web: gunicorn <nom du fichier app.py>:<nom-de-l-app>` où nom-de-l-app est généralement "app". Placez ce fichier dans le dossier principal de l'application.
6. Maintenant, connectez-vous (ou inscrivez-vous) à GitLab et créez un projet. Dès que vous faites cela, vous recevrez un ensemble standard d'instructions sur la façon de "lier" votre code sur votre machine de développement au projet GitLab. Suivez simplement les commandes, et après cela, vous pouvez faire un git push ou git pull vers/depuis ce projet. C'est une étape un peu élaborée et votre dernière instruction devrait ressembler à quelque chose comme `git push -u origin master`. Une fois terminé, en actualisant la page du projet sur GitLab, vous devriez voir tout votre code apparaître dans GitLab.

![Image](https://cdn-media-1.freecodecamp.org/images/ZR0E8T-GwjFxcxSIqt-Hwe75YUHsM70s6kMG)
_Dépôt du projet dans GitLab_

### Liaison entre GitLab et Heroku

1. Connectez-vous au [portail web Heroku](https://www.heroku.com) et créez une application. Donnez-lui un nom et sélectionnez un runtime.
2. Maintenant, dans le dossier my_app sur votre machine de développement, créez un fichier appelé « .gitlab-ci.yaml » (notez le « . » au début).
3. Ce fichier yaml aura la structure suivante.

```
my_app_file_name:
 script:
  apt-get update -qy
  apt-get install -y python-dev python-pip
  pip install -r requirements.txt
  export MONGOHQ_URL=$MONGO_URL
 
production:
 type: deploy
 script:
  apt-get update -qy
  apt-get install -y ruby-dev
  gem install dpl
  dpl  provider=heroku  app=task-mgmt-app  api-key=$HEROKU_SECRET_KEY
 only:
  master
```

1. Changez my_app_file_name par le nom de fichier de votre application Flask. Vous devez définir la variable HEROKU_SECRET_KEY dans les variables du projet. Vous obtiendrez cette clé dans le [tableau de bord Heroku](https://dashboard.heroku.com/). Pour la définir dans votre projet GitLab, allez dans **Paramètres > Pipelines CI/CD** et recherchez **Variables secrètes**. Lors de l'utilisation de ces variables dans le yaml, nous devons préfixer la variable avec le signe « $ ». Il est bon de ne pas partager les clés secrètes avec qui que ce soit et de restreindre également l'accès à celles-ci dans le projet.
2. Vous y êtes presque. Exécutez la commande `git add .gitlab-ci.yml` et `git commit -m <msg>` et `git push -u origin master`. Vous verrez le fichier dans le dépôt GitLab maintenant.
3. Sur la page « Mon tableau de bord » de GitLab, cliquez sur **Pipelines > Jobs** pour voir le job qui a commencé à s'exécuter.
4. Au cas où vous utilisez une base de données dans votre application, vous pourriez vouloir la lier à l'application en plaçant les détails dans le fichier .gitlab-ci.yaml. Veuillez consulter [ici](https://gitlab.com/bharathkallurs/tasks/blob/master/.gitlab-ci.yml) pour un exemple. J'ai utilisé MongoDB dans mon application. Heroku fournit l'ajout d'un ensemble de bibliothèques/applications gratuites à votre application. Il existe un [lien mLab](https://devcenter.heroku.com/articles/mongolab) pour ajouter MongoDB.

![Image](https://cdn-media-1.freecodecamp.org/images/C3IGAaKXdfqtg4z1tVXvomMnTo3vQepyewix)
_Liste des jobs dans le Pipeline_

![Image](https://cdn-media-1.freecodecamp.org/images/p79aifr4r3f4LDcoXJ0qEgUyeIKRnGvYvg16)
_Un job en cours d'exécution. Capture d'écran liée à my_app_file_name dans yaml._

![Image](https://cdn-media-1.freecodecamp.org/images/ZYTyYC9SiR0klvctSE8HMVEPgdNHm0UwUPt3)
_Déploiement réussi de l'application sur Heroku_

Hourra ! Vous avez maintenant réussi à intégrer votre GitLab avec Heroku avec une configuration CI/CD. Effectuez toutes les modifications de code que vous souhaitez dans votre dépôt, poussez-les vers le projet GitLab et voyez un job démarrer à chaque fois qu'il y a un push de code. Pour la configuration actuelle, j'ai utilisé les runners publics GitLab disponibles [ici](http://gitlab.com/ci). Vous pouvez configurer un runner GitLab personnalisé et définir une configuration appropriée.

### Liens utiles :

1. [Création d'une télécommande heroku](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote)
2. [Configuration de CI/CD depuis GitLab sur Heroku](https://docs.gitlab.com/ce/ci/examples/test-and-deploy-python-application-to-heroku.html)
3. [Une application de gestion des tâches - dépôt : GitLab, déployée sur Heroku](https://gitlab.com/bharathkallurs/tasks/tree/master)