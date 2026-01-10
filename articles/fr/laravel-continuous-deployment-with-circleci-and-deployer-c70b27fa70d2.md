---
title: Déploiement Continu Laravel avec CircleCI et Deployer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T19:21:13.000Z'
originalURL: https://freecodecamp.org/news/laravel-continuous-deployment-with-circleci-and-deployer-c70b27fa70d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FM9PcX3sA-6NyQtKujjblQ.jpeg
tags:
- name: CircleCI
  slug: circleci
- name: Laravel
  slug: laravel
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Déploiement Continu Laravel avec CircleCI et Deployer
seo_desc: 'By Bryan Lee

  There are many deployment solutions out there with deploying Laravel, ranging from
  SSH’ing into your machine and git pulling the files (?) to time-savers like Envoyer
  or rolling your own with Deployer. I personally love Deployer as it is...'
---

Par Bryan Lee

Il existe de nombreuses solutions de déploiement pour Laravel, allant de la connexion SSH à votre machine et de l'exécution de `git pull` (?) à des solutions d'économie de temps comme [Envoyer](https://envoyer.io/) ou à la création de votre propre solution avec Deployer. Personnellement, j'adore Deployer car il est gratuit, très flexible et peut soutenir vos projets dès leur début jusqu'à ce que vous passiez à plusieurs machines.

Deployer fonctionne en exécutant vos scripts de déploiement localement et nous pouvons rendre cela encore plus pratique en intégrant Deployer dans votre pipeline CI. Pour un projet récent, j'ai utilisé CircleCI pour exécuter tous mes tests et déployer automatiquement.

### Installation de Deployer en Local

Pour gagner du temps, je vous recommande vivement d'avoir [Deployer](https://deployer.org/) installé localement et configuré pour votre application. Cela permet de gagner beaucoup de temps en évitant de devoir déboguer votre configuration Deployer lorsque votre build CircleCI échoue.

### Laravel et CircleCI

Si vous avez déjà configuré CircleCI pour les tests de votre projet Laravel, passez à la section suivante. Sinon, je suppose que vous avez au moins déjà un compte CircleCI et un projet de base créé.

Créez un fichier `.circleci/config.yml` avec le contenu suivant :

```yml

version: 2
jobs:
  build:
    docker:
      # Spécifiez la version souhaitée ici
      - image: circleci/php:7.1-browsers
      - image: circleci/mysql:5.7
        environment:
          MYSQL_ALLOW_EMPTY_PASSWORD: yes
          MYSQL_USER: root
          MYSQL_ROOT_PASSWORD: ''
          MYSQL_DATABASE: laravel

    working_directory: ~/laravel

    steps:
      - checkout
      - run:
          name: Installer les extensions PHP
          command: |
            sudo docker-php-ext-install zip
            sudo docker-php-ext-install pdo_mysql
            sudo apt install -y mysql-client
      - run: sudo composer self-update

      # Télécharger et mettre en cache les dépendances
      - restore_cache:
          keys:
          - v1-dependencies-{{ checksum "composer.json" }}
          # basculer vers l'utilisation du dernier cache si aucune correspondance exacte n'est trouvée
          - v1-dependencies-

      - run: composer install -n --prefer-dist

      - save_cache:
          paths:
            - ./vendor
          key: v1-dependencies-{{ checksum "composer.json" }}

      - run:
          name: Configurer les éléments Laravel
          command: |
            php artisan migrate --force
      - run: ./vendor/bin/phpunit

workflows:
  version: 2
  notify_deploy:
    jobs:
      - build
```

Il s'agit d'un fichier `config.yml` très basique pour Laravel. Il installera PHP, MySQL et exécutera les tests PHPunit. N'hésitez pas à modifier cela pour répondre à vos besoins.

### Déploiement avec CircleCI

Après l'exécution de nos tests, nous voulons que CircleCI commence automatiquement à déployer sur notre serveur. N'oubliez pas que Deployer utilise SSH, donc sur notre serveur distant, nous voulons créer une paire de clés SSH `ssh-keygen -t rsa -b 4096 -C "votre@email.com"`. Nous voulons ajouter cette clé que nous avons créée dans CircleCI en tant que [clé de déploiement](https://circleci.com/docs/2.0/add-ssh-key/). Prenez note de l'empreinte, car nous devrons l'ajouter à notre fichier de configuration plus tard.

Créons un nouvel emploi dans notre fichier de configuration :

```
jobs:
  build: ... # ci-dessus
  
  deploy:
    docker:
      - image: circleci/php:7.2-browsers
    working_directory: ~/laravel
    steps:
      - checkout
```

Cela indique à CircleCI que nous avons un nouvel emploi appelé `deploy` et de le construire sur la base de l'image docker php-7.2-browsers.

Vous souvenez-vous de l'empreinte que nous avons notée lorsque nous l'avons ajoutée dans CircleCI ? Nous devons la référencer dans notre configuration afin que la clé SSH soit présente dans notre conteneur.

```
jobs:
  build: ... # ci-dessus
  
  deploy:
    docker:
      - image: circleci/php:7.2-browsers
    working_directory: ~/laravel
    steps:
      - checkout
      - add_ssh_keys:
          fingerprints:
            - "VOTRE_EMPREINTE"
```

Ainsi, CircleCI sait ajouter cette clé via l'empreinte dans le conteneur docker et cela nous permettra d'exécuter Deployer et de nous connecter en SSH à notre serveur distant pour déployer.

```
jobs:
  build: ... # ci-dessus
  
  deploy:
    docker:
      - image: circleci/php:7.2-browsers
    working_directory: ~/laravel
    steps:
      - checkout
      - add_ssh_keys:
          fingerprints:
            - "VOTRE_EMPREINTE"
      - run:
          name: Installer Deployer
          command: |
            curl -LO https://deployer.org/deployer.phar
            sudo mv deployer.phar /usr/local/bin/dep
            sudo chmod +x /usr/local/bin/dep
      - run:
          name: Déployer
          command: |
            dep deploy www.votre_serveur.com
```

Avec l'emploi `deploy` défini, la dernière étape consiste à dire à CircleCI de l'exécuter après que nos tests réussissent. C'est simple, nous avons déjà un workflow de base nommé `notify_deploy` sur lequel nous pouvons construire.

```
workflows:
  version: 2
  notify_deploy:
    jobs:
      - build
      - deploy:
          requires:
            - build
          filters:
            branches:
              only: master
```

Cela indique à CircleCI que dans notre workflow `notify_deploy`, en plus d'exécuter `build`, nous voulons exécuter `deploy` après sa fin, et de ne le faire que sur la branche `master`.

Avec tout cela fait, nous pouvons maintenant pousser le fichier de configuration vers notre dépôt git et regarder les tests et le déploiement se faire automatiquement. Utilisez-vous une méthode différente pour déployer Laravel ? Faites-le moi savoir, j'adorerais en entendre parler !