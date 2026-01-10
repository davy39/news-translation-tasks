---
title: Comment exécuter Laravel sur Google Cloud Run avec Intégration Continue - un
  guide étape par étape
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-14T20:04:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-laravel-6-on-google-cloud-run-with-continuous-integration-ci-step-by-step
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/laravel6-on-gcr-f.jpg
tags:
- name: Devops
  slug: devops
- name: google cloud
  slug: google-cloud
- name: google cloud run
  slug: google-cloud-run
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
- name: Software Engineering
  slug: software-engineering
- name: Web Development
  slug: web-development
seo_title: Comment exécuter Laravel sur Google Cloud Run avec Intégration Continue
  - un guide étape par étape
seo_desc: 'By Geshan Manandhar

  Laravel has soared in popularity over the last few years. The Laravel community
  even says that Laravel has made writing PHP more enjoyable instead of a pain. Laravel
  6 has some interesting new features. Getting a super scaleable w...'
---

Par Geshan Manandhar

Laravel a connu une popularité fulgurante ces dernières années. La communauté Laravel affirme même que Laravel a rendu l'écriture en PHP plus agréable plutôt qu'une corvée. Laravel 6 propose certaines nouvelles fonctionnalités intéressantes. Obtenir une URL super scalable pour votre application prend des heures, voire des jours. Configurer quelque chose comme Kubernetes est une tâche énorme. C'est là que Google Cloud Run brille : vous pouvez obtenir une URL HTTPS fonctionnelle pour n'importe laquelle de vos applications conteneurisées en quelques minutes.

[Google Cloud Run](https://cloud.google.com/run/) est serverless et entièrement géré par Google. Vous bénéficiez d'une super scalabilité, d'une facturation à la seconde, d'URLs HTTPS et de la cartographie de votre propre domaine. Si vous souhaitez exécuter des conteneurs sans état, Cloud Run est sans conteste la manière la plus simple de le faire. Dans cet article, je vais détailler comment faire fonctionner votre application Laravel 6 sur Google Cloud Run avec Intégration Continue (CI).

## Prérequis

* Vous êtes familier avec PHP/Composer et connaissez Laravel (si vous êtes arrivé ici, je suppose que c'est le cas)
* Vous savez utiliser Git depuis la CLI
* Votre code est hébergé sur GitHub pour le CI/CD et vous êtes familier avec GitHub
* Vous connaissez bien Docker, peut-être même les builds multi-étapes
* Vous avez un compte Google Cloud fonctionnel (ils vous offrent [300 $ de crédit](https://cloud.google.com/free/) gratuitement pour 1 an, aucune raison de ne pas avoir de compte)

## **Pourquoi Cloud Run est une excellente option pour les débutants ?**

Pour deux raisons principales :

1. Apprendre les meilleures pratiques et les logiciels comme Docker et CI/CD
2. Mettre en place les bases ne nécessite que de cliquer sur un bouton, de sélectionner 2 éléments, d'attendre 5 minutes, et vous obtenez une URL HTTPS fonctionnelle. Peut-on faire plus simple ? :)

## **Étapes de déploiement**

Voici les étapes pour configurer et déployer Laravel 6 sur Cloud Run :

### **1. Cloner Laravel ou créer un nouveau projet Laravel**

Commencez par cloner Laravel ou utiliser Composer ou la CLI Laravel comme indiqué dans le guide officiel d'[installation](https://laravel.com/docs/5.8/installation). J'utilise Composer pour obtenir la dernière version de Laravel comme suit :

#### **Commande**

J'ai exécuté la commande suivante pour obtenir la dernière version de Laravel :

```bash
composer create-project --prefer-dist laravel/laravel laravel6-on-google-cloud-run

```

![Installation de Laravel avec Composer](https://geshan.com.np/images/laravel6-on-google-cloud-run/01install-laravel.jpg)
_Création d'un nouveau projet Laravel avec Composer_

### **2. Testez-le localement d'abord**

Ensuite, exécutez `cd laravel6-on-google-cloud-run` puis `php artisan serve` pour voir si cela fonctionne. Pour moi, tout était correct lorsque je suis allé sur `http://localhost:8000` dans un navigateur web. J'avais PHP 7.2 installé localement.

![Exécution de Laravel localement](https://geshan.com.np/images/laravel6-on-google-cloud-run/02running-laravel.jpg)
_Laravel s'exécutant localement sans Docker_

### **3. Créez un nouveau dépôt GitHub**

Créez un nouveau dépôt sur GitHub comme suit :

![Création d'un dépôt pour Laravel sur GitHub](https://geshan.com.np/images/laravel6-on-google-cloud-run/03github-repo.jpg)
_Créer un nouveau dépôt public sur GitHub_

Vous pouvez utiliser n'importe quel fournisseur d'hébergement Git, mais pour cet exemple, j'utiliserai [GitHub Actions](https://github.com/features/actions) pour exécuter les tests (et GitHub est l'outil d'hébergement git le plus populaire).

### **4. Ajoutez le dépôt, poussez le readme**

Maintenant que vous avez créé le dépôt, ajoutez-le à votre copie locale de Laravel et poussez le fichier Readme. Pour cela, exécutez les commandes suivantes sur votre CLI :

```
git init
code . # J'ai utilisé VS code pour modifier le readme
git add readme.md
git commit -m "Initial commit -- App Readme"
git remote add origin git@github.com:geshan/laravel6-on-google-cloud-run.git
git push -u origin master

```

#### **Après avoir exécuté les commandes ci-dessus, j'avais ceci sur mon dépôt GitHub**

![Après le premier push, le dépôt ressemble à ceci](https://geshan.com.np/images/laravel6-on-google-cloud-run/04initial-push.jpg)
_Dépôt après avoir poussé le readme sur la branche master_

### **5. Ajoutez Laravel complet, ouvrez une PR**

Maintenant, ajoutons toute l'application en tant que PR au dépôt GitHub en exécutant les commandes suivantes :

```
git checkout -b laravel6-full-app
git add .gitignore
git add .
git commit -m "Add the whole Laravel 6 app"
git push origin laravel6-full-app

```

Après cela, allez ouvrir une Pull Request (PR), sur le dépôt comme [celle-ci](https://github.com/geshan/laravel6-on-google-cloud-run/pull/1). Vous pourriez penser que je suis le seul à travailler dessus, pourquoi ai-je besoin d'une PR ? Eh bien, il est toujours préférable de faire les choses méthodiquement même si une seule personne travaille sur le projet :).

Après cela, fusionnez votre pull request.

### **6. Configurez les tests avec [GitHub Actions](https://github.com/features/actions)**

Maintenant, la partie amusante : après avoir fusionné votre PR, GitHub sait que c'est un projet Laravel. Cliquez sur l'onglet `Actions` sur la page de votre dépôt et vous devriez voir quelque chose comme ci-dessous :

![Cliquez sur l'onglet Actions pour voir les options](https://geshan.com.np/images/laravel6-on-google-cloud-run/05github-actions.jpg)
_Configurer le workflow CI pour Laravel avec GitHub Actions_

Cliquez sur `Set up this workflow` sous `Laravel`, puis sur la page suivante, cliquez sur le bouton `Start commit` en haut à droite. Après cela, ajoutez un message de commit comme ci-dessous et cliquez sur `Commit new file`.

![Ajoutez l'action de test Laravel](https://geshan.com.np/images/laravel6-on-google-cloud-run/06gh-actions-ci.jpg)
_Étapes pour configurer le workflow CI avec GitHub Actions_

Et voilà, vous avez configuré votre CI. Les tests par défaut de Laravel s'exécuteront à chaque push git maintenant. N'était-ce pas facile ? Merci GitHub pour cette grande intelligence. Plus besoin de créer des fichiers `.myCIname.yml` :).

### **7. Ajoutez Docker et docker-compose pour exécuter l'application localement**

Maintenant, ajoutons Docker et docker-compose pour exécuter l'application localement sans PHP ou artisan serve.

Nous aurons besoin du conteneur pour exécuter Laravel sur Google Cloud Run également. Cette partie est inspirée de l'article [Laravel on Google Cloud Run](https://nsirap.com/posts/010-laravel-on-google-cloud-run/) de Nicolas. Si vous souhaitez en savoir plus sur [Docker](https://www.docker.com/) et Laravel, veuillez vous référer à cet [article](https://geshan.com.np/blog/2015/10/getting-started-with-laravel-mariadb-mysql-docker/).

Exécutez d'abord les commandes suivantes pour mettre à jour votre branche master car nous avons ajouté le fichier `workflow` depuis l'interface GitHub :

```
git checkout master
git fetch
git pull --rebase origin master # car nous avons ajouté le fichier workflow depuis l'interface github
git checkout -b docker

```

Ajoutez une clé au fichier `.env.example`. Copiez-la depuis le fichier `.env` comme suit :

```
APP_NAME=Laravel
APP_ENV=local
APP_KEY=base64:DJkdj8L5Di3rUkUOwmBFCrr5dsIYU/s7s+W52ClI4AA=
APP_DEBUG=true
APP_URL=http://localhost

```

Comme il s'agit simplement d'une démonstration, cela est acceptable. Pour une application réelle, soyez toujours prudent avec les secrets. Pour les applications prêtes pour la production, désactivez le débogage et autres éléments liés au développement.

Ajoutez le `Dockerfile` suivant à la racine du projet :

```
FROM composer:1.9.0 as build
WORKDIR /app
COPY . /app
RUN composer global require hirak/prestissimo && composer install

FROM php:7.3-apache-stretch
RUN docker-php-ext-install pdo pdo_mysql

EXPOSE 8080
COPY --from=build /app /var/www/
COPY docker/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY .env.example /var/www/.env
RUN chmod 777 -R /var/www/storage/ && \
    echo "Listen 8080" >> /etc/apache2/ports.conf && \
    chown -R www-data:www-data /var/www/ && \
    a2enmod rewrite

```

Ensuite, ajoutez le fichier suivant à `docker/000-default.conf`

```
<VirtualHost *:8080>

  ServerAdmin webmaster@localhost
  DocumentRoot /var/www/public/

  <Directory /var/www/>
    AllowOverride All
    Require all granted
  </Directory>

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

```

Après cela, ajoutez le `docker-compose.yml` suivant

```
version: '3'
services:
  app:
    build:
      context: ./
    volumes:
      - .:/var/www
    ports:
      - "8080:8080"
    environment:
      - APP_ENV=local

```

#### **Résumons les points principaux**

Si vous essayez de comprendre tout ici, cela peut être accablant, alors laissez-moi résumer les parties principales :

1. Nous utilisons l'image Docker officielle PHP Apache pour exécuter Laravel, qui a la version PHP 7.3.
2. Nous utilisons une construction multi-étapes pour obtenir les dépendances avec Composer, puis nous les copions dans l'image Docker principale qui a PHP 7.3 et Apache.
3. Comme Google Cloud Run nécessite que le serveur web écoute sur le port `8080` et que nous utilisons `000-default.conf` pour configurer cela
4. Pour faciliter l'exécution avec la commande unique `docker-compose up`, nous utilisons docker-compose.
5. Maintenant que vous avez lu jusqu'ici, exécutez `docker-compose up` à la racine, puis après que tout soit exécuté, allez sur `http://localhost:8080` pour voir que Laravel 6 s'exécute localement sur Docker. Voici la sortie de mon `docker-compose up` vers la fin :

![Docker compose exécutant Laravel avec PHP 7.3 et Apache](https://geshan.com.np/images/laravel6-on-google-cloud-run/07docker-compose-output.jpg)
_Docker compose s'exécutant avec succès sur la machine locale_

Comme Laravel s'exécute bien avec Docker, ouvrons une PR comme [celle-ci](https://github.com/geshan/laravel6-on-google-cloud-run/pull/2/files) pour ajouter Docker à notre projet. J'ai exécuté les commandes suivantes à la racine du projet avant d'ouvrir la Pull Request (PR) :

```
git status

```

Cela devrait vous donner quelque chose comme ci-dessous :

```
On branch docker
Untracked files:
  (use "git add <file>..." to include in what will be committed)

  Dockerfile
  docker-compose.yml
  docker/

nothing added to commit but untracked files present (use "git add" to track)

```

Maintenant, exécutez les commandes suivantes :

```
git add .
git commit -m "Add docker and docker compose"
git push origin docker

```

En bonus, cela exécutera le test par défaut de Laravel lors du push, comme vous pouvez le voir ci-dessous :

![À chaque push, les tests unitaires PHP s'exécuteront](https://geshan.com.np/images/laravel6-on-google-cloud-run/08test-running-gh.jpg)
_Tests par défaut de Laravel s'exécutant avec GitHub Actions_

Seul le propriétaire du dépôt a accès à l'onglet `Actions`, donc les autres personnes n'ont pas nécessairement besoin de connaître les résultats de vos builds de test :).

### **8. Ajoutez le déploiement vers le [bouton Google Cloud](https://github.com/GoogleCloudPlatform/cloud-run-button)**

Maintenant, déployons cette configuration Laravel sur Google Cloud Run de manière facile. Étant donné que vous avez fusionné votre PR depuis la branche `docker`, exécutons les commandes suivantes :

```
git checkout master
git fetch
git pull --rebase origin master
git checkout -b cloud-run-button

```

Ensuite, ajoutez ce qui suit à votre fichier `readme.md` :

```
### Exécuter sur Google Cloud Run

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/geshan/laravel6-on-google-cloud-run.git)

```

Soyez prudent et remplacez la dernière partie par l'URL `HTTPS` de votre dépôt. Par exemple, si votre dépôt est à `https://github.com/ghaleroshan/laravel6-on-google-cloud-run`, ce sera `https://github.com/ghaleroshan/laravel6-on-google-cloud-run.git`, puis validez et poussez. Votre PR devrait ressembler à [celle-ci](https://github.com/geshan/laravel6-on-google-cloud-run/pull/3/files).

### **9. Déployez sur Google Cloud Run**

Après avoir fusionné votre Pull Request (PR), allez sur la page de votre dépôt et cliquez sur le bouton `Run on Google Cloud`.

![Cliquez sur le bouton bleu pour déployer l'application](https://geshan.com.np/images/laravel6-on-google-cloud-run/09cloud-run-button.jpg)
_GitHub readme après avoir ajouté le bouton Run on Google Cloud_

Après cela, si vous êtes connecté à votre compte Google et avez configuré Google Cloud avec 1 projet, cliquez sur « Proceed ». Vous devrez peut-être attendre un peu, puis

1. Choisissez le projet – « Choose a project to deploy this application »
2. Choisissez la région – « Choose a region to deploy this application », je choisis généralement « us-central-1 »
3. Attendez ensuite que le conteneur soit construit et déployé. Vous pouvez voir mon processus ci-dessous :

Si tout se passe bien sur votre « Google Cloud Shell », vous verrez l'URL HTTPS que vous pouvez utiliser pour voir votre application Laravel en cours d'exécution comme ci-dessous :

![Accédez à l'URL donnée pour voir qu'elle fonctionne](https://geshan.com.np/images/laravel6-on-google-cloud-run/10laravel-running-gcr.jpg)
_Écran de déploiement de Google Cloud Shell pour Laravel 6 sur Cloud Run_

Ce qui vient de se passer ci-dessus est :

1. Après avoir choisi la région, le script a construit une image de conteneur Docker à partir du `Dockerfile` dans le dépôt
2. Ensuite, il a poussé l'image construite vers [Google Container Registry](https://cloud.google.com/container-registry/)
3. Après cela, en utilisant la CLI [gcloud](https://cloud.google.com/sdk/gcloud/), il a déployé l'image construite sur Cloud Run, qui a renvoyé l'URL.

### **10. Hourra, votre application fonctionne**

Après avoir obtenu l'URL, vous devriez voir votre application fonctionner sur Google Cloud Run comme ci-dessous :

![Laravel s'exécutant sur Google Cloud Run](https://geshan.com.np/images/laravel6-on-google-cloud-run/11laravel-url.jpg)
_Laravel s'exécutant sur Google Cloud Run avec une URL HTTPS Serverless :)_

Si vous souhaitez déployer une autre version, vous pouvez fusionner votre PR vers master et cliquer à nouveau sur le bouton pour déployer.

## **Plus d'informations sur Google Cloud Run**

Le [tarif](https://cloud.google.com/run/pricing) pour Google Cloud Run est très généreux. Vous pouvez exécuter n'importe quelle application conteneurisée ou application web sur Google Cloud Run. J'ai exécuté un projet personnel qui a reçu ~ 1 requête par minute et je n'ai rien eu à payer.

En coulisses, il utilise [Knative](https://cloud.google.com/knative/) et [Kubernetes](https://kubernetes.io/). Il peut également être exécuté sur votre cluster Kubernetes, mais qui choisirait de gérer un cluster K8s si vous pouvez simplement pousser et obtenir une application serverless scalable entièrement gérée :).

## **TLDR**

Pour exécuter Laravel 6 sur Google Cloud Run rapidement, suivez les étapes ci-dessous :

1. Assurez-vous d'être connecté à votre [compte Google Cloud](https://console.cloud.google.com/)
2. Allez sur [https://github.com/geshan/laravel6-on-google-cloud-run](https://github.com/geshan/laravel6-on-google-cloud-run)
3. Cliquez sur le bouton bleu « Run On Google Cloud »
4. Sélectionnez votre projet
5. Sélectionnez votre région
6. Attendez et obtenez l'URL de votre application Laravel comme ci-dessous, profitez-en !

![Accédez à l'URL donnée pour voir qu'elle fonctionne](https://geshan.com.np/images/laravel6-on-google-cloud-run/10laravel-running-gcr.jpg)
_Journal de déploiement du bouton Cloud Run pour déployer Laravel sur Google Cloud Run_

---

![Laravel s'exécutant sur Google Cloud Run](https://geshan.com.np/images/laravel6-on-google-cloud-run/11laravel-url.jpg)
_Laravel s'exécutant avec succès sur Google Cloud Run_

## **Conclusion**

Et voilà – exécuter une application Laravel sur Google Cloud Run était assez facile. Vous avez même des tests qui s'exécutent sur GitHub avec GitHub Actions. J'espère que cela aide. Pour une approche CI/CD, vous pouvez consulter cet [article](https://medium.com/google-cloud/simplifying-continuous-deployment-to-cloud-run-with-cloud-build-including-custom-domain-setup-ssl-22d23bed5cd6). Il montre le déploiement en utilisant Cloud Build. Comme le même conteneur s'exécute pour les environnements local et de production (Google Cloud Run), vous n'avez pas besoin d'apprendre un nouveau framework pour passer au Serverless.

> Toute application web conteneurisée peut être exécutée sur Google Cloud Run, c'est un excellent service. Vous pouvez en lire plus sur https://geshan.com.np