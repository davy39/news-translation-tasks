---
title: 'Comprendre les bases de Ruby on Rails : HTTP, MVC et Routes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-02T16:28:33.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-basics-of-ruby-on-rails-http-mvc-and-routes-359b8d809c7a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KK61kGXrkaFBDfY7uWukyQ.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Comprendre les bases de Ruby on Rails : HTTP, MVC et Routes'
seo_desc: 'By TK

  After learning your first programming language, you may ask what can you do with
  programming: AI/Machine Learning? Hardware development? Mobile apps? Or maybe you
  want to start developing web applications! :)

  Here we’ll understand the basics of...'
---

Par TK

Après avoir appris votre [**premier langage de programmation**](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d), vous pourriez vous demander ce que vous pouvez faire avec la programmation : IA/Apprentissage automatique ? Développement matériel ? Applications mobiles ? Ou peut-être voulez-vous commencer à développer des applications web ! :)

Ici, nous allons comprendre les bases du fonctionnement du web, des routes et de l'architecture MVC en utilisant le framework web Ruby on Rails. Plongeons dans le monde du web.

Avant d'apprendre le développement web avec Rails, je recommande vraiment d'apprendre d'abord [**Ruby**](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d).

### Comment fonctionne le web ?

Le web comporte plusieurs couches ([Application, TCP, Internet, Hardware layers](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)) qui sont toutes connectées. Mais fondamentalement, il fonctionne grâce au **HTTP** (_Hypertext Transfer Protocol_).

> Le **Hypertext Transfer Protocol** (**HTTP**) est un protocole d'application pour les systèmes d'information hypermédia distribués et collaboratifs. — [Wikipedia](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)

Le **HTTP** fonctionne comme un cycle de _requête — réponse_ dans le modèle _client — serveur_.

Nous avons un navigateur web (Google Chrome, par exemple). Nous tapons l'URL `www.google.com`, et le _client_ soumet la _requête HTTP_ (message de requête) au _serveur_. Le _serveur_ retourne la _réponse HTTP_ (message de réponse — dans ce cas, la réponse est le HTML du site web de Google).

![Image](https://cdn-media-1.freecodecamp.org/images/1*0HsqvxES_m9Serhg8xW2Xg.png)

Le _client_ effectue la _requête_ et reçoit la _réponse_ du _serveur_. Le client gère l'interface utilisateur et les interactions utilisateur. Sur le serveur, nous pouvons stocker et récupérer des données (dans des bases de données), traiter la logique en arrière-plan (workers/jobs), et bien d'autres choses.

Si vous souhaitez comprendre cela en profondeur, je vous suggère quelques ressources. Je suis un grand fan des articles de [Preethi](https://www.freecodecamp.org/news/understanding-the-basics-of-ruby-on-rails-http-mvc-and-routes-359b8d809c7a/undefined). Voici une série en **3 parties** :

* [Une introduction pour les nouveaux venus dans le développement web](https://medium.freecodecamp.org/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c)
* [Modèle Client-Serveur & la Structure d'une Application Web](https://medium.freecodecamp.org/how-the-web-works-part-ii-client-server-model-the-structure-of-a-web-application-735b4b6d76e3)
* [HTTP & REST](https://medium.freecodecamp.org/how-the-web-works-part-iii-http-rest-e61bc50fa0a)

### L'architecture MVC et les Routes de Rails

![Image](https://cdn-media-1.freecodecamp.org/images/1*eDPWR3lYGm1ogbef2beyHA.png)

Maintenant que nous comprenons comment le Web fonctionne, nous allons étudier l'architecture MVC et les Routes de Rails.

MVC signifie Modèle, Vue et Contrôleur.

Dans cette architecture, nous avons la "séparation des préoccupations" parmi les _Modèles, Vues_ et _Contrôleurs_. Chaque partie a sa propre responsabilité. Plongeons dans chaque partie.

#### Modèle

> "Maintenir la relation entre l'Objet et la Base de données et gérer la validation, l'association, les transactions"

Cela signifie que le modèle maintiendra une relation étroite avec la _Base de données_. Chaque modèle (peut) représenter une table de base de données (dans le cas des bases de données SQL). Cet objet modèle acquiert des capacités (héritées de _ActiveRecord —_ classe Rails) pour récupérer, sauvegarder, modifier et supprimer des données de la table de la base de données. Nous utilisons des objets modèles comme une couche entre notre application et la base de données.

Outre cette relation avec la base de données, le _modèle_ peut créer des **_validations_** et des **_associations_** entre les modèles.

#### Vue

> "Une présentation des données dans un format particulier, déclenchée par la décision d'un contrôleur de présenter les données."

C'est la présentation de la _réponse de la requête_. Cette présentation peut être dans plusieurs formats : _PDF, HTML, JSON_, etc. Le résultat final d'une vue sera probablement l'interface utilisateur (UI) — Partie du "Client".

Pour la plupart des pages sur le web, les vues seront un HTML stylisé avec CSS et JS. Mais nous pouvons également implémenter des PDFs du comportement des utilisateurs sur un [produit numérique de voyage](https://www.worldpackers.com/) pour montrer à tous les employés comment les gens utilisent leur site web.

#### Contrôleur

> "La facilité au sein de l'application qui dirige le trafic, d'une part en interrogeant les modèles pour des données spécifiques, et d'autre part en organisant ces données (recherche, tri) sous une forme qui répond aux besoins d'une vue donnée."

Le contrôleur est le "Maestro". Il s'occupe du flux : utilise les modèles pour effectuer des requêtes, analyse les données et prend des décisions sur le format dans lequel vous présenterez les données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KK61kGXrkaFBDfY7uWukyQ.png)

### Cycle MVC & Routes dans une application Rails

Imaginez que nous travaillons dans une [Startup de Voyage](https://www.worldpackers.com). Une partie du produit consiste à présenter une [liste de grands articles sur les histoires et conseils de voyage](https://www.worldpackers.com/articles) aux voyageurs.

Pensez simplement du point de vue du voyageur. Vous allez sur `[www.worldpackers.com/articles](http://www.worldpackers.com/articles)` et vous voyez une belle page listant une série de grands articles.

Lorsque vous tapez cette URL dans le navigateur, il effectue une requête vers le serveur. Sur le serveur, nous avons l'application web Rails. Le routeur Rails vérifie s'il existe une entrée correspondant à l'URL demandée.

Nous devons simplement configurer les routes pour cette ligne :

Cela créera des routes RESTful pour les articles. Si nous exécutons `bundle exec rake routes`, il affichera la liste des chemins créés.

Le verbe HTTP peut être `GET`, `POST`, `PATCH`, `PUT` ou `DELETE`. Et nous savons comment Rails mappe chaque `PATH` au bon `controller` et `action`. Lisez plus [ici](http://guides.rubyonrails.org/routing.html).

Dans notre cas, le serveur recevra le chemin `/articles` et `GET` comme verbe HTTP. Il le mappera à `ArticlesController` et à l'action `index`.

Dans le **_contrôleur_** `ArticlesController`, nous utilisons le **_modèle_** `Article` pour obtenir tous les articles dans la base de données et rendre la **_vue_** `index.html.erb` comme _réponse du serveur_ (l'UI).

Par convention, ce contrôleur rendra la vue dans `views/articles/index.html.erb`. Basiquement, c'est un fichier HTML simple alimenté par Ruby.

Le cycle requête-réponse de Rails est l'un des premiers concepts que vous devez comprendre lorsque vous commencez à apprendre le développement web.

L'utilisateur fait des choses (requête au serveur), l'application Rails a le routeur pour mapper le chemin de l'URL au bon contrôleur. Dans le contrôleur, nous pouvons faire toutes sortes de choses avec un modèle (ou plus d'un modèle) — ce qui signifie obtenir, sauvegarder, modifier, supprimer des données — et rendre une vue à l'utilisateur.

### C'est tout !

Nous avons appris beaucoup ici. J'espère que vous appréciez le contenu et en apprenez davantage sur le fonctionnement de l'architecture MVC et du routage sur Rails.

C'est une étape de plus dans mon parcours pour apprendre et maîtriser Rails et le développement web. Vous pouvez voir la documentation de mon parcours complet ici sur ma publication [**Renaissance Developer**](https://medium.com/the-renaissance-developer).

Si vous voulez un cours complet sur [Ruby](https://onemonth.com/courses/ruby?mbsy=lG6tt&mbsy_source=97541b09-e3ab-45d7-a9b1-dbc77028e008&campaignid=33446&discount_code=TKRuby1) et [Rails](https://onemonth.com/courses/rails?mbsy=lG6tz&mbsy_source=d2442db6-e764-401a-a394-a9c081468830&discount_code=TKRuby1&campaignid=33448), apprendre des compétences de codage réelles et construire des projets, essayez [**_One Month Ruby Bootcamp_**](https://onemonth.com/courses/ruby?mbsy=lG6tt&mbsy_source=97541b09-e3ab-45d7-a9b1-dbc77028e008&campaignid=33446&discount_code=TKRuby1) et [**_Rails Bootcamp_**](https://onemonth.com/courses/rails?mbsy=lG6tz&mbsy_source=d2442db6-e764-401a-a394-a9c081468830&discount_code=TKRuby1&campaignid=33448). À bientôt ☺

Amusez-vous bien, et continuez à apprendre et à coder.

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☺