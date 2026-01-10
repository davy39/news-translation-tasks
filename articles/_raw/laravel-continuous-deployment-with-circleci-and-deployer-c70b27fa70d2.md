---
title: Laravel Continuous Deployment With CircleCI and Deployer
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
seo_title: null
seo_desc: 'By Bryan Lee

  There are many deployment solutions out there with deploying Laravel, ranging from
  SSH’ing into your machine and git pulling the files (?) to time-savers like Envoyer
  or rolling your own with Deployer. I personally love Deployer as it is...'
---

By Bryan Lee

There are many deployment solutions out there with deploying Laravel, ranging from SSH’ing into your machine and `git pull`ing the files (?) to time-savers like [Envoyer](https://envoyer.io/) or rolling your own with Deployer. I personally love Deployer as it is free, very flexible and can support your projects from infancy to when you scale to multiple machines.

Deployer works by running your deployment scripts locally and we can make this even more convenient by integrating Deployer into your CI pipeline. For a recent project, I used CircleCI to run all my tests and automatically deploy.

### Setup Deployer Locally

To save time, I will highly recommend that you have [Deployer](https://deployer.org/) installed locally and configured and working for your app. This saves a lot of time in having to do debugging on your Deployer config when your CircleCI build fails.

### Laravel and CircleCI

If you already have CircleCI setup for your Laravel project tests, skip to the next section. Otherwise, I assume that you at least already have a CircleCI account and a basic project created inside.

Create a `.circleci/config.yml` and with the below

```yml

version: 2
jobs:
  build:
    docker:
      # Specify the version you desire here
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
          name: Install PHP exts
          command: |
            sudo docker-php-ext-install zip
            sudo docker-php-ext-install pdo_mysql
            sudo apt install -y mysql-client
      - run: sudo composer self-update

      # Download and cache dependencies
      - restore_cache:
          keys:
          - v1-dependencies-{{ checksum "composer.json" }}
          # fallback to using the latest cache if no exact match is found
          - v1-dependencies-

      - run: composer install -n --prefer-dist

      - save_cache:
          paths:
            - ./vendor
          key: v1-dependencies-{{ checksum "composer.json" }}

      - run:
          name: Setup Laravel stuffs
          command: |
            php artisan migrate --force
      - run: ./vendor/bin/phpunit

workflows:
  version: 2
  notify_deploy:
    jobs:
      - build
```

This is a very basic `config.yml` for Laravel. It will install PHP, MySQL and run PHPunit tests. Feel free to modify this to suit your needs.

### CircleCI Deployment

After our tests are run, we want CircleCI to automatically start deploying to our server. Remember that Deployer uses SSH, so in our remote server, we want to create a SSH keypair `ssh-keygen -t rsa -b 4096 -C “your@email.com"`. We want to add this key we created into CircleCI as a [deployment key](https://circleci.com/docs/2.0/add-ssh-key/). Take note of the fingerprint, as we will need to add this into our config file later.

Let’s create a new job in our config file:

```
jobs:
  build: ... # from above
  
  deploy:
    docker:
      - image: circleci/php:7.2-browsers
    working_directory: ~/laravel
    steps:
      - checkout
```

This tells CircleCI that we have a new job called `deploy` and to build it based on the php-7.2-browsers docker image.

Remember the fingerprint that we took note of when we added it into CircleCI? We need to reference this in in our config so that the SSH key will be present in our container.

```
jobs:
  build: ... # from above
  
  deploy:
    docker:
      - image: circleci/php:7.2-browsers
    working_directory: ~/laravel
    steps:
      - checkout
      - add_ssh_keys:
          fingerprints:
            - "YOUR_FINGERPRINT"
```

So now, CircleCI knows to add this key via the fingerprint into the docker container and this will allow us to run Deployer and SSH into our remote server to deploy.

```
jobs:
  build: ... # from above
  
  deploy:
    docker:
      - image: circleci/php:7.2-browsers
    working_directory: ~/laravel
    steps:
      - checkout
      - add_ssh_keys:
          fingerprints:
            - "YOUR_FINGERPRINT"
      - run:
          name: Install Deployer
          command: |
            curl -LO https://deployer.org/deployer.phar
            sudo mv deployer.phar /usr/local/bin/dep
            sudo chmod +x /usr/local/bin/dep
      - run:
          name: Deploy
          command: |
            dep deploy www.your_server.com
```

With the `deploy` job defined, the last step would be to tell CircleCI to run it after our tests pass. That’s simple, we already have a basic workflow named `notify_deploy` that we can build upon.

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

This tells CircleCI that in our `notify_deploy` workflow, aside from running `build`, we want to run `deploy` after it is finished, and to only do it on the `master` branch.

With everything done, we can now push the config file to our git repository and watch it test and deploy on its own. Do you use a different way of deploying Laravel? Let me know, I’d love to hear about it!

