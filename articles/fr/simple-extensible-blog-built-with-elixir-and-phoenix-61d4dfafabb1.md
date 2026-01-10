---
title: Comment créer un blog simple et extensible avec Elixir et Phoenix
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-28T18:06:58.000Z'
originalURL: https://freecodecamp.org/news/simple-extensible-blog-built-with-elixir-and-phoenix-61d4dfafabb1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*qT3nBMIsmRiQa4nc
tags:
- name: Elixir
  slug: elixir
- name: Phoenix framework
  slug: phoenix
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un blog simple et extensible avec Elixir et Phoenix
seo_desc: 'By Raman Sah

  In this post, we’ll discuss how to build a boilerplate Phoenix web app with user
  authentication and an admin panel, along with image upload in Elixir.

  TodoMVC has become a de facto tool to compare various JavaScript-based MV* frameworks....'
---

Par Raman Sah

Dans cet article, nous allons discuter de la création d'une application web Phoenix de base avec authentification utilisateur et un panneau d'administration, ainsi que le téléchargement d'images en Elixir.

[TodoMVC](http://todomvc.com/) est devenu un outil de facto pour comparer divers frameworks MV* basés sur JavaScript. Dans la même veine, je pense qu'une application de blog peut être un critère décisif dans le choix d'un nouveau framework backend ou API.

Alors, commençons et construisons-en un avec Phoenix. Nous suivrons la configuration par défaut, c'est-à-dire Phoenix connecté à Ecto fonctionnant sur PostgreSQL.

Voici les écrans finaux pour vous donner une idée de l'apparence de l'application à la fin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x59piiG96eAfObns-aPzvQ.png)

La page d'accueil affichera tous les blogs publiés dans une disposition de cartes. Une carte peut être cliquée pour afficher ce post particulier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mxWIdSAc-p9elJI3x2yQKw.png)

Nous aurons un tableau de bord qui affichera les statistiques en bref. L'accès à cette page nécessite une connexion d'utilisateur administrateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xwuFgK253CAjphO0IVu8Ow.png)

Il y aura une section séparée qui donnera un aperçu de tous les posts. Ici, vous pouvez publier/modifier/supprimer des posts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fkzXp5iJjFJPzyk-bu1NFg.png)

Ceci est la disposition de l'éditeur de posts présentant un éditeur markdown ainsi qu'un sélecteur de fichiers pour l'image de couverture.

> _Note : Le code complet et fonctionnel est hébergé sur [GitHub](https://github.com/ramansah/cms). Il y a de nombreux fichiers dans le projet qui ne peuvent pas être partagés dans un seul blog. J'ai donc expliqué ceux qui, selon moi, sont critiques._

Gardons le nom du projet comme CMS pour l'instant. Nous commencerons donc par créer un nouveau projet avec `mix phx.new cms`. Exécutez `mix deps.get` pour installer les dépendances.

Générez un fichier de migration pour les utilisateurs et les posts, respectivement.

```
# Fichier de migration utilisateur
```

```
mix phx.gen.schema Auth.User users name:string email:string password_hash:string is_admin:boolean
```

```
# Fichier de migration des posts
```

```
mix phx.gen.schema Content.Post posts title:string body:text published:boolean cover:string user_id:integer slug:string
```

Deux tables doivent être créées dans la base de données qui représentent les utilisateurs et les posts. Je l'ai gardé plutôt simple, en ne gardant que les champs requis et en les développant lorsque le besoin se fait sentir.

Par la suite, nous pouvons définir des changesets et des méthodes supplémentaires dans les schémas utilisateur et post.

**user.ex**

**post.ex**

```
@derive {Phoenix.Param, key: :slug}
```

Puisque nous voulons que les posts aient une structure d'URL lisible et conviviale pour le SEO, nous informons les helpers de route de référencer `slug` au lieu de `id` dans l'espace de noms de l'URL.

Les routes sont décrites ici :

Les ressources spécifiques à la section admin sont regroupées et assignées à un pipeline qui force l'authentification.

Pendant ce temps, les routes globales sont traitées avec une authentification passive. Les détails de l'utilisateur sont récupérés si une session est présente, mais les pages restent accessibles. Les pages de connexion et d'accueil appartiennent à cette catégorie.

L'exécution de `mix phx.routes` me donne cette sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C0G1-utBGFbtv8332dWFfA.png)

La vue est divisée en trois sections logiques :

1. Barre de navigation
2. Barre latérale
3. Contenu principal

Alors que la barre de navigation est toujours visible, la barre latérale n'apparaît que si un utilisateur administrateur est connecté. La navigation dans le contenu se fera dans le contexte admin. Les liens dans la barre latérale augmenteront au fur et à mesure que l'application évoluera.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UkNS-kHZ4Dpo9lgMpzqSdA.png)

Le contrôleur Admin.Post suit l'architecture CRUD typique et inclut une action pour basculer l'état de publication d'un post donné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xwuFgK253CAjphO0IVu8Ow.png)

De nombreux contrôles résident dans la page d'index de la section des posts de l'admin. Ici, les posts peuvent être supprimés, publiés et modifiés.

**templates/admin/post/index.html.eex**

Pour garder le modèle épuré, nous pouvons définir des helpers de vue pratiques comme le formatage de l'heure, etc., séparément.

**views/admin/post_view.ex**

Arc, ainsi qu'arc_ecto, fournit des capacités de téléchargement de fichiers prêtes à l'emploi. Puisque un post présente une image de couverture, nous devons définir une configuration arc dans notre application.

Chaque post dans notre blog nécessite deux versions d'images de couverture — l'originale, visible dans la vue spécifique du post, et une version miniature avec une empreinte plus petite pour remplir les cartes. Pour l'instant, utilisons une résolution de 250x250 pour la version miniature.

Revenons à la page d'accueil de l'application, elle abritera les cartes de tous les posts publiés. Et chaque post sera accessible via le slug formé.

```
controllers/page_controller.ex
```

Ce projet explore Phoenix — comment une application Phoenix est structurée et comment démanteler un projet basé sur Phoenix. J'espère que vous avez appris quelque chose et que vous l'avez apprécié !

L'application complète et fonctionnelle est sur GitHub : [https://github.com/ramansah/](https://github.com/ramansah/votex)cms. N'hésitez pas à cloner ? et à applaudir si vous trouvez ce blog utile ?