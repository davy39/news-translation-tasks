---
title: Ce que vous devez savoir pour devenir un développeur full-stack serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-17T06:34:20.000Z'
originalURL: https://freecodecamp.org/news/what-you-need-to-become-a-full-stack-serverless-developer
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/serverlesssStuff-1.png
tags:
- name: full stack
  slug: full-stack
- name: serverless
  slug: serverless
- name: serverless framework
  slug: serverless-framework
seo_title: Ce que vous devez savoir pour devenir un développeur full-stack serverless
seo_desc: 'By Sam Williams

  The are the 4 areas of development you need to know to call yourself a full-stack
  developer

  Becoming a full-stack developer is the goal of a lot of developers. Being able to
  create a complete software product, getting to understand ho...'
---

Par Sam Williams

## Voici les 4 domaines de développement que vous devez connaître pour vous appeler développeur full-stack

Devenir développeur full-stack est l'objectif de nombreux développeurs. Pouvoir créer un produit logiciel complet, comprendre le fonctionnement de l'ensemble du système et l'augmentation de salaire très intéressante (plus de £5 500**) sont autant de raisons pour lesquelles les gens veulent améliorer leurs compétences et devenir développeur full-stack.

Le problème est que l'apprentissage de toutes les compétences nécessaires peut prendre beaucoup de temps. Nous allons couvrir les 4 domaines de développement que vous devez connaître et discuter des meilleures façons de les apprendre.

# Front End / Hébergement de site web

Lorsque vous construisez une application, elle doit avoir un front end. C'est ce que vos utilisateurs verront et comment ils interagiront avec votre produit.

C'est souvent la première compétence serverless que les développeurs acquièrent, souvent sans s'en rendre compte. Cela se fait souvent via GitHub Pages ou un service d'hébergement.

Bien que ces services soient excellents pour l'hébergement rapide et simple de projets, vous aurez besoin de quelque chose de plus robuste pour un hébergement web serverless plus grand et plus technique.

### Ce que vous devrez être capable de faire

* Pouvoir héberger les fichiers nécessaires à une application front end.
* Pouvoir servir ces fichiers sur une URL donnée à grande échelle
* Pointer un nom de domaine enregistré vers ces fichiers

### Comment faire cela avec Serverless ?

* Héberger les fichiers sur Amazon S3 (système de stockage de fichiers)
* Créer une distribution CloudFront pour servir les fichiers à grande échelle
* Utiliser Route 53 pour enregistrer un nom de domaine et le pointer vers la distribution CloudFront

### Pourquoi Serverless est la meilleure façon de faire cela

S3, CloudFront et Route 53 s'adaptent automatiquement, vous n'avez donc pas à deviner combien de visiteurs votre site recevra

* Vous n'avez pas besoin de configurer ou de maintenir les serveurs
* Vous n'avez pas besoin de configurer le DNS, les serveurs de noms ou autre chose pour mettre le site en ligne sur votre URL. Route 53 gère tout cela.

# Créer une API

Toute application a besoin d'API pour que le front end puisse interagir avec le back end (bases de données, stockage, email, etc.), ce qui est la source de la plupart de la puissance d'une application full-stack.

### Ce que vous devrez être capable de faire

* Pouvoir créer des endpoints d'API RESTful
* Pouvoir accéder à vos bases de données
* Pouvoir accéder à d'autres services (stockage, SMS, email, autres API)
* Protéger vos endpoints avec des clés API

### Comment faire cela ?

* Utiliser API Gateway pour construire les endpoints d'API
* Créer des fonctions Lambda pour exécuter votre logique et accéder à d'autres services (accès à la base de données, SMS, email, etc.)
* Créer des clés API qui fournissent l'accès à vos endpoints d'API

### Pourquoi Serverless est la meilleure façon de faire cela

* Chaque endpoint est une fonction isolée, donc si l'une tombe en panne, cela n'affecte pas les autres
* Vous avez un accès très facile au reste des services serverless via l'aws-sdk, réduisant le code et accélérant le développement
* Vous pouvez facilement créer, limiter et supprimer des clés API pour vous assurer que les bonnes personnes peuvent invoquer vos endpoints d'API.

# Bases de données

Tous les services full-stack ont besoin d'un moyen de stocker des données sur les utilisateurs, les produits et tout le reste. Cela peut être dans une base de données relationnelle ou non relationnelle, mais vous devez stocker les données quelque part de manière organisée.

### Ce que vous devrez être capable de faire

* Créer une base de données non relationnelle ou relationnelle scalable
* Accéder à cette base de données

### Comment faire cela ?

* Créer une base de données DynamoDB (non relationnelle) ou Aurora (relationnelle)
* Accéder à vos tables dans vos Lambdas d'API en utilisant les outils intégrés dans l'AWS SDK

### Pourquoi Serverless est la meilleure façon de faire cela

* Vos tables s'adaptent automatiquement et ont une redondance intégrée, éliminant le besoin de gérer et de synchroniser plusieurs copies de bases de données
* Vous pouvez facilement accéder aux bases de données avec l'AWS SDK sans avoir à les exposer au monde extérieur.

# Déploiement et maintenance

Une fois que vous avez conçu et construit tous vos systèmes, vous devez les déployer dans un environnement de production, les maintenir et les mettre à jour.

### Ce que vous devrez être capable de faire

* Déployer toutes les ressources dont nous avons parlé jusqu'à présent
* Fournir une configuration contrôlée par version pour toutes les ressources
* Maintenir et mettre à jour le logiciel et le matériel sur lesquels vos systèmes s'exécutent

### Comment faire cela ?

* Créer les ressources en utilisant le framework Serverless

### Pourquoi Serverless est la meilleure façon de faire cela

* Lorsque vous créez votre fichier serverless.yml, vous définissez toutes les ressources dont vous avez besoin pour faire fonctionner votre application
* Ce fichier serverless.yml peut être contrôlé par version pour suivre les changements au fil du temps
* Vous pouvez déployer toute votre architecture en quelques minutes avec une seule commande
* Tout le logiciel et le matériel sous-jacents sont maintenus, mis à jour et améliorés par votre fournisseur de services (AWS), vous n'avez donc pas à vous en soucier

---

Si vous avez aimé cet article et que vous souhaitez commencer à apprendre comment devenir développeur full-stack, j'ai un cours vidéo gratuit en 3 parties sur la façon de construire et de déployer votre propre API serverless.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/course.png)
_[Découvrez le cours ici](https://courses.completecoding.io/p/build-a-serverless-api/)_

** Développeur front end à Londres (£42 994) vs Développeur full-stack à Londres (48 767)