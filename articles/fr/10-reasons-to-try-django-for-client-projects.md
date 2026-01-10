---
title: À quoi sert Python's Django ? 5 raisons clés pour lesquelles j'utilise le framework
  Django pour les projets clients
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-08T17:51:04.000Z'
originalURL: https://freecodecamp.org/news/10-reasons-to-try-django-for-client-projects
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95fc740569d1a4ca0f26.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: À quoi sert Python's Django ? 5 raisons clés pour lesquelles j'utilise
  le framework Django pour les projets clients
seo_desc: "By Gwendolyn Faraday\nIf you had told me a few years ago that I would pick\
  \ Python's Django as my number one framework of choice for client projects, I would\
  \ not have believed you. \nBack then, I preferred lightweight frameworks like Flask\
  \ and Express f..."
---

Par Gwendolyn Faraday

Si vous m'aviez dit il y a quelques années que je choisirais Python's Django comme **mon framework de prédilection pour les projets clients**, je ne vous aurais pas cru.

À l'époque, je préférais les frameworks légers comme Flask et Express pour leur flexibilité et le contrôle supplémentaire qu'ils m'offraient.

Qu'est-ce qui a changé ?

En partie, c'est parce que j'ai été embauchée pour travailler avec Django ! L'autre partie, c'est que j'en avais marre de configurer les mêmes fonctionnalités encore et encore à partir de zéro pour différentes entreprises – ORM pour la base de données, migrations, systèmes d'authentification, emails, et ainsi de suite. Il est chronophage de configurer et de faire fonctionner correctement toutes ces fonctionnalités.

Eh bien, Django me fournit tout cela avec une configuration minimale dès la sortie de la boîte. Oui, c'est génial.

Avec Django, je peux construire des applications beaucoup plus rapidement sans sacrifier les fonctionnalités. L'expérience du développeur est également assez bonne – et pas seulement parce que Python est génial. C'est aussi parce qu'il y a de bons outils de débogage, que la journalisation est déjà configurée, et qu'il y a un serveur qui redémarre automatiquement avec les changements de fichiers.

Je pourrais parler sans fin de toutes les bonnes fonctionnalités de Django, mais ici je vais simplement lister mes 5 préférées. J'espère que cela piquera votre curiosité afin que vous souhaitiez essayer Django pour vos propres entreprises et projets.

## Interface d'administration de Django

Je place cela en premier car c'est ma fonctionnalité préférée intégrée à Django.

De nombreux clients ont besoin d'avoir une vue sur leur application afin qu'ils puissent gérer les utilisateurs, les données ou le contenu des pages. Habituellement, le client ne sera pas technique ou n'aura pas assez de temps pour plonger dans le code réel et faire des changements.

Alors, quelle est la meilleure façon de gérer cette situation ?

L'interface d'administration de Django est une excellente solution. Sans aucune configuration supplémentaire, vous obtenez une zone d'administration puissante, entièrement personnalisable et protégée par login qui affiche toutes les données de votre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screen-Shot-2021-01-31-at-9.43.58-PM.png)
_Image de [Stack Overflow](https://stackoverflow.com/questions/37572343/django-count-todays-logged-in-users)_

Les données dans cette zone d'administration incluent toutes les tables que vous souhaitez lister ainsi que toutes les tables des packages tiers comme les bibliothèques d'authentification.

## Django a une authentification intégrée

Un certain type d'authentification est nécessaire dans presque toutes les applications, donc le marché propose de nombreux outils, services et bibliothèques à utiliser. Parce qu'il y a tant d'options, il peut être difficile d'en choisir une. Même si vous utilisez un service géré, le connecter n'est pas toujours facile.

Eh bien, Django vient avec une authentification intégrée via des sessions. Et si vous voulez utiliser des tokens ? Il suffit d'installer la bibliothèque Django REST Framework (DRF) qui vient avec l'authentification par token.

Personnellement, j'aime utiliser DRF avec la bibliothèque supplémentaire [dj-rest-auth](https://github.com/jazzband/dj-rest-auth) pour des fonctionnalités supplémentaires comme les tokens expirants. Dans tous les cas, toutes ces pièces fonctionnent de manière transparente ensemble dans l'écosystème Django et nécessitent très peu de configuration.

_[Voici un exemple de dépôt Django](https://github.com/freecodeschoolindy/student-management-system) où j'ai configuré l'authentification par token (et GitHub) dans Django avec Django REST Framework._

Tout système d'authentification que vous utilisez dans un projet Django utilisera également l'ORM. Alors, parlons de certains des avantages de cela ensuite.

## ORM

Avez-vous déjà essayé de configurer manuellement un ORM pour connecter votre base de données à votre application ? Par exemple, SQLAlchemy, TypeORM ou Sequelize. Même avec une bonne documentation, ce n'est pas facile. Vous devez faire fonctionner différents types de requêtes, ainsi que les migrations, le seeding, et bien plus encore.

Django fournit tout cela pour vous dès la sortie de la boîte. Il suffit de brancher les identifiants de votre base de données préférée - Postgres, MySQL, Mongo, et ainsi de suite - et Django gère le reste. Vous créez des modèles et interagissez avec eux via la même interface Python, quelle que soit la base de données que vous choisissez.

_Juste une note ici : sauf si vous êtes un maître de SQL ou avez un cas très spécial, vous devriez utiliser un ORM pour interagir avec les bases de données dans chaque application._

Toutes les fonctionnalités listées jusqu'à présent ne sont pas exclusives à Python's Django seul. La différence est que la plupart des frameworks vous permettent de configurer votre propre ORM, authentification, et ainsi de suite. Django fait tout cela avec très peu d'effort. Cela signifie que vous pouvez livrer des fonctionnalités, des MVPs et des applications plus rapidement.

## Vitesse de développement

Python est un langage couramment utilisé pour prototyper et construire rapidement des applications. Django vous offre la vitesse et la puissance de Python avec de nombreuses fonctionnalités intégrées supplémentaires pour vous aider à construire des applications web et des APIs beaucoup plus rapidement.

Prendre des décisions et rechercher des outils et des bibliothèques prend beaucoup de temps loin de l'écriture réelle de code. Django a des façons bien documentées de faire les choses, ce qui élimine tout le temps supplémentaire que vous pourriez passer à trouver une bonne solution par vous-même.

De l'initialisation d'un projet pour vous, à la création de requêtes complexes, et au déploiement de votre application, Django vous couvre avec une [excellente documentation](https://docs.djangoproject.com/en/3.1/) et une [grande communauté](https://forum.djangoproject.com/) pour vous aider si vous êtes bloqué.

Ce ne sont pas seulement les bibliothèques principales de Django qui peuvent vous aider à construire des applications plus rapidement, cependant. Django dispose également de milliers de plugins avec une API commune afin que vous puissiez avoir certaines attentes sur la façon d'utiliser l'un d'eux dans votre projet.

## Plugins Django

Vous voulez construire un CMS ? Django a un plugin pour cela. En fait, assez quelques-uns. Si vous recherchez sur Github et [DjangoPackages.org](https://djangopackages.org/), vous trouverez une pléthore de solutions pour presque tous les cas d'utilisation.

Voici quelques-uns de mes préférés :

* [Django Rest Framework](https://www.django-rest-framework.org/) : Routeurs, sérialiseurs et autres outils pour rendre la construction d'APIs simple.
* [Django Graphene](https://github.com/graphql-python/graphene-django) : Facilite l'ajout de fonctionnalités GraphQL aux applications Django.
* [Wagtail](https://wagtail.io/) : Ajoute une belle interface de style CMS à Django avec de nombreuses fonctionnalités intégrées pour les cas d'utilisation courants des CMS.
* [Django Crispy Forms](https://github.com/django-crispy-forms/django-crispy-forms) : Si vous construisez des applications full-stack, ce package rend le travail avec les formulaires à l'intérieur des templates beaucoup plus propre et plus facile.
* [Django Debug Toolbar](https://pypi.org/project/django-debug-toolbar/) : C'est un must pour les projets Django. Vous pouvez déboguer tout, des requêtes SQL aux templates en utilisant cet outil.

J'espère vous avoir donné suffisamment un avant-goût de Django pour que vous souhaitiez l'essayer par vous-même. Faites-moi savoir comment cela se passe :)

Je travaille avec une grande équipe en tant que développeur logiciel senior chez [RocketBuild](https://rocketbuild.com/) ! Nous construisons beaucoup de projets cool en Django, React et d'autres technologies.

Si vous voulez voir plus de contenu sur Django, Python et JavaScript, consultez ma chaîne YouTube, [Faraday Academy](https://www.youtube.com/c/FaradayAcademy). Ou, entrez en contact avec moi sur Twitter, [@faradayacademy](https://twitter.com/faradayacademy).