---
title: Un aperçu des validations personnalisées dans Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T16:33:30.000Z'
originalURL: https://freecodecamp.org/news/a-quick-look-at-rails-custom-validation-9ab7e0f1af81
coverImage: https://cdn-media-1.freecodecamp.org/images/1*otuQiVYDCBjZee9xZ0UnvA.jpeg
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
seo_title: Un aperçu des validations personnalisées dans Rails
seo_desc: 'By Raymond Blessed

  I recently started working with Ruby (almost 2 months now) and Ruby on Rails (a
  little over 3 weeks). Working with Rails’ Active Record framework is one of my favorite
  things about Ruby on Rails. In this post, we will be looking at...'
---

Par Raymond Blessed

J'ai récemment commencé à travailler avec Ruby (il y a presque 2 mois) et Ruby on Rails (un peu plus de 3 semaines). Travailler avec le framework Active Record de Rails est l'une de mes choses préférées à propos de Ruby on Rails. Dans cet article, nous allons examiner les validations dans Active Record, en particulier les validations personnalisées. Voici une brève introduction à Active Record avant de passer aux choses sérieuses.

Active Record est l'une des gemmes principales qui composent Ruby on Rails. C'est la partie du framework qui gère les bases de données.

Il s'agit d'un framework ORM (Object Relational Mapping) qui vous permet de construire un schéma pour une base de données en utilisant du Ruby pur et il est basé sur le modèle de conception Active Record décrit par [Martin Fowler](https://martinfowler.com/). Ainsi, avec Active Record, vous créez votre base de données, créez des tables, stockez, récupérez et supprimez des données en utilisant Ruby, ce qui se traduit par du SQL en coulisses.

### Introduction rapide

Supposons que nous ayons un modèle d'étudiant avec les propriétés prénom et nom. Pour utiliser Active Record, nous devons simplement étendre **ApplicationRecord** et lorsque nous exécutons `rails db:migrate`, cela nous donne l'instruction SQL correspondante.

Pour interagir avec la base de données, nous utilisons des méthodes héritées de la superclasse ApplicationRecord.

Il prend également en charge les associations et autres fonctionnalités de base de données.

Pour une introduction détaillée à Active Record, consultez le guide officiel de Ruby on Rails.

### Validation

Parce que nous écrivons des applications web pour des utilisateurs autres que nous-mêmes, nous ne pouvons pas être sûrs que les utilisateurs entreront toujours des données valides dans la base de données. Pour imposer cela, Active Record nous fournit un mini-framework de validation qui garantit la présence de données, l'unicité de certains champs, et ainsi de suite.

Examinons notre table d'étudiants ci-dessus. Nous ne voudrions pas créer un utilisateur sans prénom ou nom, ce qui est actuellement possible. Pour remédier à cela, nous devons simplement modifier notre classe Student comme suit :

Avec cette modification, lorsque vous créez une instance de Student sans les attributs prénom ou nom, il s'agit d'un étudiant invalide et Active Record ne le persistera pas dans la base de données.

Active Record nous fournit également des méthodes pour vérifier si nos données sont valides ou invalides :

Avec cela, nous n'avons même pas besoin d'essayer d'enregistrer les données.

En plus de simplement empêcher les données d'être persistées, Active Record fournit également une liste d'erreurs qui contient les attributs qui ont échoué aux validations et des messages conviviaux à présenter aux utilisateurs. Ces erreurs peuvent être accessibles comme montré dans l'extrait ci-dessous.

Il y a beaucoup plus à dire sur la validation, mais ce n'est pas le sujet de cet article. Pour une plongée en profondeur, vous pouvez obtenir une explication détaillée dans le chapitre du guide Ruby on Rails sur la Validation.

### Validation personnalisée

Parfois, nous pouvons vouloir utiliser certaines validations qui vont au-delà de la simple vérification de la présence d'un attribut, de la longueur, de l'unicité, ou de l'un des helpers fournis par Active Record. Heureusement, Active Record nous permet de définir nos propres validations personnalisées, ce qui est le point de cet article.

Supposons donc que pour notre modèle Student, nous avons une colonne de numéro d'inscription obligatoire. Elle doit être remplie à partir du formulaire d'inscription (je sais que cela peut être généré automatiquement) et doit toujours commencer par l'année d'inscription. Maintenant, Active Record ne fournit pas ce type de validation prêt à l'emploi, mais il nous permet de la définir et de l'utiliser.

Il existe principalement deux façons de définir votre propre logique de validation :

* Validateur personnalisé
* Méthodes personnalisées

#### **Validateur personnalisé**

Pour valider en utilisant un validateur personnalisé, vous devez simplement définir votre logique de validation dans une classe qui étend **ActiveModel::Validator** et implémente la méthode validate, qui prend l'enregistrement à valider comme argument.

Si la validation échoue, elle ajoute l'attribut au tableau des erreurs avec son message d'erreur. Donc, dans notre cas, nous aurons RegNumValidator comme vu ci-dessous :

Pour utiliser ce validateur dans le modèle Student, nous utilisons la méthode `validates_with` :

Avec cela, lorsque l'utilisateur essaie de créer un étudiant avec un mauvais numéro d'inscription, la création de l'enregistrement échoue et un message d'erreur peut être affiché.

#### **Méthodes personnalisées**

Pour utiliser des méthodes personnalisées pour la validation, vous devez simplement définir une méthode à utiliser pour la validation dans votre classe de modèle et l'appeler comme vous appelleriez l'une des validations intégrées — en utilisant `validate`. En utilisant la même logique que ce que nous avions ci-dessus, notre modèle ressemblerait à ceci :

### Conclusion

J'espère que cet article vous a donné les connaissances nécessaires pour commencer à explorer les validations d'Active Record et en particulier les validations personnalisées. Chaque fois que vous avez une règle de validation qui ne fait pas partie de l'API de validation d'Active Record existante, vous pouvez en écrire une vous-même.

[**Validations Active Record — Guides Ruby on Rails**](https://guides.rubyonrails.org/active_record_validations.html)  
[_Les validations sont utilisées pour s'assurer que seules les données valides sont enregistrées dans votre base de données. Par exemple, il peut être important de...guides.rubyonrails.org](https://guides.rubyonrails.org/active_record_validations.html)