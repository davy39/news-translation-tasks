---
title: Comment déployer une application Rails 5.2 PostgreSQL sur AWS Elastic Beanstalk
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-rails-5-2-postgresql-app-on-aws-elastic-beanstalk-34e5cec3a984
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OciaQvyAjhVdws2DUeYgCw.jpeg
tags:
- name: AWS
  slug: aws
- name: deployment
  slug: deployment
- name: postgres
  slug: postgres
- name: Rails
  slug: rails
- name: 'tech '
  slug: tech
seo_title: Comment déployer une application Rails 5.2 PostgreSQL sur AWS Elastic Beanstalk
seo_desc: 'By Evrim Persembe

  It’s official, using Heroku for all my Rails projects so far has spoiled me rotten.
  After receiving some AWS credits thanks to a pitch competition, I decided to deploy
  my latest project on Elastic Beanstalk (AWS’ Heroku competitor)....'
---

Par Evrim Persembe

C'est officiel, utiliser [Heroku](https://heroku.com/) pour tous mes projets Rails jusqu'à présent m'a complètement gâté. Après avoir reçu des crédits AWS grâce à un concours de pitch, j'ai décidé de déployer mon dernier projet sur [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) (le concurrent d'[AWS](https://aws.amazon.com/) à Heroku). Tout ce que je peux dire, c'est que Heroku me manque.

Hélas, si vous êtes dans une situation similaire, voici des instructions étape par étape pour déployer votre application Rails 5.2 / PostgreSQL sur Elastic Beanstalk.

### Installation de l'interface de ligne de commande Elastic Beanstalk

Nous utiliserons le terminal dans ce tutoriel. Commençons par installer l'« Elastic Beanstalk Command Line Interface ». Voici comment faire sur macOS en utilisant [Homebrew](https://brew.sh/) :

```
brew install awsebcli
```

Si vous utilisez une autre plateforme, une recherche Google sur « comment installer awsebcli sur [votre plateforme] » devrait vous guider dans la bonne direction.

### Initialisation d'Elastic Beanstalk

Je vais supposer que vous avez déjà un compte Amazon Web Services, sinon allez-y et créez-en un. Maintenant, allez dans le répertoire de votre projet et initialisez Elastic Beanstalk :

```
cd my_project
eb init
```

Ensuite, l'interface de ligne de commande EB vous posera quelques questions pour initialiser l'application Elastic Beanstalk. La partie initialisation est simple. Si vous êtes bloqué quelque part, vous pouvez consulter la page [« Configure the EB CLI »](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html) de la documentation.

### Création d'un nouvel environnement

Comme vous le savez déjà, votre application peut avoir plusieurs environnements (considérez-les comme différentes configurations). Par exemple, vous pouvez avoir un environnement « production ». C'est l'environnement que vous utilisez pour la version de votre application accessible aux utilisateurs. Mais vous pouvez vouloir avoir un autre environnement nommé « staging ». C'est là que vous essayez de nouvelles versions de votre application avant de les pousser vers l'environnement de production.

Nous pouvons créer un environnement en utilisant la commande suivante :

```
eb create production
```

### Déploiement sur Elastic Beanstalk

En supposant que vous utilisez Git, validez vos changements avant de déployer votre application. L'interface de ligne de commande EB déploie votre dernier commit. Si vous déployez avant de valider, vous déployerez une version antérieure de votre application.

Après avoir validé vos changements, déployez en utilisant ce qui suit :

```
eb deploy
```

Jusqu'à présent, tout va bien, maintenant nous devons configurer quelques choses avant que notre application ne commence vraiment à fonctionner.

### Configuration de la clé principale

Vous pouvez utiliser l'interface de ligne de commande à cette fin également, mais je préfère utiliser le panneau web pour cela. Voici comment faire :

1. Allez sur AWS, choisissez « Services -> Elastic Beanstalk », puis cliquez sur votre environnement.
2. Ouvrez l'onglet « Configuration », et cliquez sur « Modifier » sous la boîte intitulée « Software ».
3. Sous « Environment properties », ajoutez une nouvelle clé nommée `RAILS_MASTER_KEY`. Définissez sa valeur sur le contenu de votre fichier « master.key ». Vous pouvez trouver ce fichier dans le répertoire « config » de votre application Rails.
4. Cliquez sur le bouton « Apply » en bas de la page.

### Configuration d'une base de données PostgreSQL

Elastic Beanstalk fournit un moyen facile de configurer une base de données, que vous pouvez atteindre via « Configuration -> Database ». Je préfère ne pas utiliser cela car si vous devez reconstruire votre environnement Elastic Beanstalk, votre base de données sera supprimée. Nous allons donc configurer la base de données séparément de notre environnement Elastic Beanstalk.

#### Création d'une base de données PostgreSQL sur RDS

1. Allez sur AWS, choisissez « Services -> RDS ».
2. Choisissez « Create database ».
3. Choisissez « PostgreSQL », et cliquez sur « Next ».
4. Sélectionnez votre cas d'utilisation, « Production » ou « Dev/Test », et cliquez sur « Next ».
5. Ici, vous pouvez essayer différentes options et voir quels sont les coûts mensuels estimés. Choisissez quelque chose qui est dans votre budget. Vous pouvez commencer avec une instance `db.t2.micro`, sans déploiement multi-AZ et un SSD à usage général.
6. Choisissez un identifiant d'instance, c'est une sorte de « namespace ».
7. Choisissez un nom d'utilisateur et un mot de passe, gardez-les à portée de main pour l'instant, cliquez sur « Next ».
8. Dans la section « Configure advanced settings », l'élément important est les groupes de sécurité. Sélectionnez « Choose existing VPC security groups », et sélectionnez le groupe de sécurité qui ressemble à « ...-AWSEBSecurityGroup-... »
9. Choisissez un nom de base de données, comme `my_app_production`.
10. Cliquez sur « Create database », cela prendra un certain temps.

#### Autorisation de l'accès à la base de données

En attendant, ajoutons l'accès Postgres à votre groupe de sécurité :

1. Allez sur AWS, choisissez « Services -> EC2 ».
2. Cliquez sur « Security Groups » dans le panneau de gauche.
3. Choisissez le groupe de sécurité de la section précédente.
4. Allez dans l'onglet « Inbound », et cliquez sur « Edit ».
5. Cliquez sur « Add Rule ». Pour « Type », choisissez « PostgreSQL », et pour « Source », tapez l'ID du groupe de sécurité auquel vous ajoutez cette règle. Il devrait être juste au-dessus de l'onglet « Inbound » et devrait ressembler à `sg-*`.
6. Cliquez sur « Save ».

#### Configuration de la base de données de production

Maintenant, dans votre répertoire Rails, ouvrez `config/database.yml`. Modifiez-le comme suit :

```
# ...
```

```
production:  <<: *default  database: <%= ENV['RDS_DB_NAME'] %>  username: <%= ENV['RDS_USERNAME'] %>  password: <%= ENV['RDS_PASSWORD'] %>  host: <%= ENV['RDS_HOSTNAME'] %>  port: <%= ENV['RDS_PORT'] %>
```

#### Ajout des variables d'environnement pertinentes à Elastic Beanstalk

Nous avons dit à Rails de récupérer les informations pour la base de données de production en utilisant les variables d'environnement ci-dessus. Maintenant, nous devons nous assurer que notre environnement Elastic Beanstalk inclut ces variables :

1. Allez sur AWS, choisissez « Services -> Elastic Beanstalk », puis cliquez sur votre environnement.
2. Ouvrez l'onglet « Configuration », et cliquez sur « Modifier » sous la boîte intitulée « Software ».
3. Sous « Environment properties », ajoutez les paires clé-valeur suivantes :
4. `RDS_DB_NAME` : Nom de la base de données que vous avez choisi lors de la configuration de votre base de données.
5. `RDS_USERNAME` : Nom d'utilisateur que vous avez choisi lors de la configuration de votre base de données.
6. `RDS_PASSWORD` : Mot de passe que vous avez choisi lors de la configuration de votre base de données.
7. `RDS_HOSTNAME` : Allez dans « Services -> RDS », et vous pouvez trouver cette information sous la section « Connect » de la page d'informations de votre instance de base de données. Elle est appelée « Endpoint ».
8. `RDS_PORT` : Définissez cela sur 5432.
9. Cliquez sur le bouton « Apply » en bas de la page.

Après cela, validez à nouveau votre répertoire d'application Rails et exécutez `eb deploy`. Vous pouvez vouloir attendre quelques minutes avant de faire cela car Elastic Beanstalk fait certaines choses en arrière-plan après la mise à jour des variables d'environnement.

Après ces étapes, votre application Rails « devrait » fonctionner.

### Toujours pas de fonctionnement ?

S'il y a des problèmes, vous pouvez aller dans votre environnement EB sur le panneau web AWS, cliquer sur « Logs », et choisir « Request Logs -> Last 100 Lines » pour voir les logs. Mais avant de faire cela, je recommande d'essayer d'exécuter votre application Rails en utilisant l'environnement de production sur votre machine locale en utilisant la commande `rails s RAILS_ENV=production`.

Je serai le premier à admettre que je ne suis pas la personne la plus expérimentée en matière de déploiement. Comme je l'ai dit, j'ai toujours utilisé Heroku dans le passé, et je l'utiliserai probablement pour mes futurs projets également. Ces étapes ont fonctionné pour moi après quelques jours de réflexion pour configurer mon application Rails sur Elastic Beanstalk, donc je voulais les partager dans l'espoir de faire gagner du temps aux personnes qui sont dans la même situation que moi. Donc, prenez tout cela avec des pincettes, et bonne chance !

Si vous aimez cet article, [suivez-moi sur Twitter](https://twitter.com/evrimfeyyaz) ou [inscrivez-vous à ma newsletter](https://evrim.us12.list-manage.com/subscribe/post?u=7d6b207df0db42f6bfcff3322&id=70b8425aa4) pour être informé lorsque j'écris de nouveaux articles. J'écris sur les logiciels et les startups.

**Si vous cherchez un développeur Rails, je suis actuellement disponible pour du travail à distance. N'hésitez pas à me contacter à hi{at}evrim.io.**

_Publié à l'origine sur [evrim.io](https://evrim.io/deploying-a-rails-52-postgresql-app-on-aws-elastic-beanstalk/) le 28 novembre 2018._