---
title: Ruby on Rails Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/ruby-on-rails-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cff740569d1a4ca3552.jpg
tags:
- name: Ruby
  slug: ruby
- name: Ruby on Rails
  slug: ruby-on-rails
- name: toothbrush
  slug: toothbrush
seo_title: Ruby on Rails Expliqué
seo_desc: 'Ruby on Rails is a server-side framework (gem) built on the Ruby language
  to make websites. It includes everything you need to build web applications and
  has a big community.

  Ruby on Rails is an opinionated framework, and emphasizes the use of conven...'
---

[Ruby on Rails](http://rubyonrails.org/) est un framework côté serveur (gem) construit sur le langage Ruby pour créer des sites web. Il inclut tout ce dont vous avez besoin pour construire des applications web et dispose d'une grande communauté.

Ruby on Rails est un framework opinionné, et met l'accent sur l'utilisation de la convention plutôt que la configuration (CoC), et ne vous répétez pas (DRY) pratiques. Rails peut être décrit comme un framework modèle-vue-contrôleur (MVC), et fournit des valeurs par défaut et des structures sensées pour un développement rapide d'applications. Récemment, Rails a intégré un module API pour rendre la création de services web plus rapide et plus facile.

Ruby on Rails a été créé par David Heinemeier Hansson et est actuellement à sa 6ème version.

## **Comment installer Rails**

Rails est téléchargé de la même manière que n'importe quelle autre gem Ruby : avec la commande `gem install`. Avant de le télécharger, nous devrons [télécharger Ruby](https://www.ruby-lang.org/). Ensuite, nous ne sommes plus qu'à trois mots de commencer avec Ruby on Rails :

```shell
$ gem install rails
```

Rails est livré avec sqlite3 comme base de données par défaut, qui est un simple fichier sur disque. Vous devez installer MySQL ou PostgreSQL si vous voulez utiliser quelque chose de plus robuste.

## **Comment créer une application Rails**

1. Après avoir installé Ruby on Rails, il est très simple de créer une toute nouvelle application, nous n'aurons besoin que de trois mots de plus :

```shell
$ rails new votre_nom_d_application
```

2. Si vous voulez utiliser MySQL :

```shell
$ rails new <nom_application> -d mysql
```

3. Si vous voulez utiliser Postgres :

```shell
$ rails new <nom_application> -d postgresql
```

4. Cette commande créera un dossier avec le _votre_nom_d_application_ que vous avez indiqué dans la dernière commande. L'étape suivante est d'aller dans le nouveau répertoire que vous venez de créer :

```shell
$ cd votre_nom_d_application
```

5. Obtenez les gems et les paquets logiciels nécessaires avant d'exécuter votre application :

```shell
$ bundle install
```

6. Pour exécuter le serveur rails et voir si tout s'est bien passé, c'est aussi rapide :

```shell
$ rails server
```

Ce ne pourrait pas être plus simple ! Eh bien, ce n'est pas tout à fait vrai à 100 %, nous pourrions le rendre encore plus petit en réduisant la commande `rails server` à :

```shell
$ rails s
```

7. Maintenant, avec votre navigateur préféré, allez sur `http://localhost:3000` et vous verrez : « Yay! You're on Rails! »

### **Méthode alternative pour créer une application Rails**

1. Créez un nouveau répertoire :

```shell
$ mkdir <nom_application>
```

2. Allez dans le nouveau répertoire :

```shell
$ cd <nom_application>
```

3. Créez l'application Rails en utilisant la notation par point Unix. Cela permet d'assigner le nom du répertoire à la nouvelle application :

```shell
$ rails new .
```

4. Commencez à explorer le framework de l'application que vous venez de créer. Pour voir un tableau utile de la structure des dossiers, consultez [Getting Started with Rails](https://guides.rubyonrails.org/getting_started.html).

## **Convention plutôt que Configuration**

_Convention plutôt que Configuration_ signifie qu'un développeur n'a besoin de spécifier que les aspects non conventionnels de l'application. Par exemple, si il y a une classe `Sale` dans le modèle, la table correspondante dans la base de données est appelée `sales` par défaut. Ce n'est que si l'on s'écarte de cette convention, comme appeler la table « produits vendus », que le développeur doit écrire du code concernant ces noms. Généralement, les conventions de Ruby on Rails conduisent à moins de code et moins de répétition.

## **Qu'est-ce que MVC ?**

Modèle (Active record) contient la logique métier et interagit avec la base de données. Vues (Action views) tous les fichiers HTML et la structure. Contrôleur (Action controller) interagit avec les vues et le modèle pour diriger les actions de l'application.

## **DRY - Ne vous répétez pas**

_Ne vous répétez pas_ signifie que l'information est située en un seul endroit, sans ambiguïté. Par exemple, en utilisant le module ActiveRecord de Rails, le développeur n'a pas besoin de spécifier les noms des colonnes de la base de données dans les définitions de classe. Au lieu de cela, Ruby on Rails peut récupérer cette information à partir de la base de données en fonction du nom de la classe.

## **Ruby on Rails est open source**

Non seulement il est gratuit à utiliser, mais vous pouvez également aider à l'améliorer. Plus de 4 500 personnes ont déjà contribué au code de [Rails](https://github.com/rails/rails). C'est plus facile que vous ne le pensez pour devenir l'un d'eux.