---
title: 'Comprendre les bases de Ruby on Rails : les bases de données SQL et leur fonctionnement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-02T16:53:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-basics-of-ruby-on-rails-sql-databases-and-how-they-work-7a628cd42073
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iIiiKaJKg8k9aRU8iWxCxA.jpeg
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
seo_title: 'Comprendre les bases de Ruby on Rails : les bases de données SQL et leur
  fonctionnement'
seo_desc: 'By TK

  After learning about Ruby, the first step we took was to understand how the web
  and the Ruby on Rails request-response cycle work.

  Now it’s time to learn about databases and how they connect with Ruby on Rails.
  Basically, the answer is the Mode...'
---

Par TK

Après [avoir appris Ruby](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d), la première étape que nous avons franchie a été de comprendre comment fonctionnent [le web et le cycle requête-réponse de Ruby on Rails](https://medium.com/the-renaissance-developer/ruby-on-rails-http-mvc-and-routes-f02215a46a84).

Il est maintenant temps d'apprendre les bases de données et comment elles se connectent avec Ruby on Rails. Basiquement, la réponse est le Modèle : le `M` de `MVC`, comme nous l'avons appris [ici](https://medium.com/the-renaissance-developer/ruby-on-rails-http-mvc-and-routes-f02215a46a84).

Avant d'apprendre le développement web avec Rails, je recommande vraiment d'apprendre d'abord [**Ruby**](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d).

Commençons !

### Qu'est-ce qu'une base de données ?

Hmmm… La première pensée qui me vient à l'esprit est quelque chose qui stocke des données.

Mais cette définition est assez imprécise ! Un tableau, un hachage, une liste chaînée, ou toute structure de données peut être quelque chose capable de stocker des données.

Lorsque vous éteignez l'ordinateur, vous perdez toutes les valeurs de données qui étaient stockées dans ce tableau (de même que toutes les structures de données). Il n'est donc pas judicieux de stocker toutes mes `données précieuses`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p1Yw2imC4HhUPaEfssliXw.gif)
_MES DONNÉES PRÉCIEUSES_

Nous devons résoudre deux problèmes ici :

1. Stocker des données et les récupérer à tout moment.
2. Stocker des données de manière organisée et structurée, afin de pouvoir les récupérer facilement.

Dois-je stocker toutes les données dans un bloc-notes ? Il suffit de mettre toutes les informations à l'intérieur, séparées par des virgules, d'enregistrer le `fichier txt`, et c'est fait. Maintenant, je peux l'ouvrir et obtenir toutes les données que je veux. Nous pouvons stocker des données et les récupérer à tout moment… problème résolu !

Nous avons résolu ce problème, mais nous avons manqué l'autre. Maintenant, toutes les données sont stockées et nous ne les perdrons pas. Mais elles ne sont pas bien structurées dans le fichier. Nous avons besoin d'une règle pour stocker et récupérer des données de manière organisée et bien structurée.

Réfléchissons à la manière dont nous pouvons organiser les données de manière bien structurée.

**Et si nous organisions toutes les données dans des tables ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QzMTJf39jdsi_alIWlGxig.jpeg)

Ainsi, voici ce que nous avons : l'en-tête de la table (_noms des colonnes : Prénom, Nom, Adresse, etc_) contenant les valeurs que nous allons stocker. Par exemple, si nous voulons stocker la **_chaîne "Mickey"_** _(la valeur)_, elle sera stockée dans la colonne **_"Prénom"_**.

* **Table** : disons **_Personnes_**
* **Colonnes** : **_Prénom_**, **Nom**, **Adresse**, etc
* **Lignes** : dans ce cas, nous pouvons dire qu'une ligne peut être une **_personne_** avec, par exemple, le prénom "_Mickey_" et le nom "_Mouse_", l'adresse "123 _Fantasy Way_", etc.
* **Champs** : toutes les données stockées dans la base de données.

Et maintenant, nous avons une manière bien structurée de stocker des données : dans une Table !

### Comment obtenir, supprimer, insérer et mettre à jour des données ?

Nous utiliserons le langage SQL (_je ne mentionnerai pas le monde NoSQL !_) pour manipuler les données. Commençons par les bases.

1. **SELECT** : si nous voulons obtenir toutes les données (**_personne_**) de la table **Personnes**, nous devons les sélectionner à partir de cette table.

Le symbole (*****) signifie qu'il sélectionnera toutes les colonnes de la table **Personnes**. Si nous pouvons obtenir toutes les colonnes, nous pouvons spécifier quelles colonnes nous avons besoin pour cette sélection.

2. **DELETE** : nous voulons supprimer toutes les données de notre table **Personnes**.

Mais il n'est pas courant de supprimer toutes les données d'une table. Nous utilisons généralement une condition pour supprimer, comme "Je veux supprimer toutes les personnes de moins de 21 ans." Nous apprendrons comment faire cela plus tard dans cet article !

3. **INSERT** : nous allons insérer/stocker des données dans la table.

Ou nous pouvons spécifier dans quelles colonnes nous voulons insérer des données.

4. **UPDATE** : nous avons stocké les données, mais nous voulons les mettre à jour.

### Utilisation de conditions dans nos requêtes

Maintenant, nous pouvons utiliser le langage SQL pour interroger (sélectionner, supprimer, insérer, mettre à jour) des données.

* Mais que faire si nous voulons supprimer uniquement les enregistrements avec le nom de famille **_Kinoshita_** ?
* Ou si nous voulons mettre à jour une personne spécifique avec le prénom **_Leandro_** et le nom de famille **_Kinoshita_** ?
* Ou simplement sélectionner toutes les données de la table des personnes et les trier par âge du plus jeune au plus âgé ?

Oui, nous utilisons des conditions comme **where** et **order by**, et des opérateurs comme **or** et **and**. Voici quelques exemples :

* Suppression de tous les enregistrements de la table des personnes avec le nom de famille **_Kinoshita_**.

* Mise à jour de tous les enregistrements de la table des personnes avec le prénom **_Leandro_** et le nom de famille **_Kinoshita_**.

* Sélection de tous les enregistrements de la table des personnes mais en les triant par âge (par ordre croissant → ASC).

#### Relation entre les tables

Nous savons comment exécuter des requêtes (avec ou sans conditions). Comprenons comment fonctionnent les relations entre les tables.

* **Un à Un (1-1)** : il s'agit d'une relation entre deux tables dans laquelle l'une ne peut appartenir qu'à l'autre. **ex.** Une personne a un passeport et ce passeport appartient à cette personne spécifique. Dans cet exemple, nous avons la table Personnes, la table Passeports et une relation 1-1.
* **Un à Plusieurs (1-n)** : il s'agit d'une relation entre deux tables dans laquelle un enregistrement d'une table peut référencer plusieurs enregistrements d'une autre. **ex.** Imaginez une plateforme de commerce électronique : utilisateurs, commandes, produits, paiements, etc. Un utilisateur peut avoir plusieurs commandes, et chaque commande appartient à cet utilisateur spécifique. Dans cet exemple, nous avons la table Utilisateurs, la table Commandes et une relation 1-n.
* **Plusieurs à Plusieurs (n-n)** : il s'agit d'une relation entre deux tables dans laquelle un enregistrement d'une table peut référencer plusieurs enregistrements d'une autre. Et un enregistrement d'une autre peut également référencer plusieurs enregistrements de la première. **ex.** Nous avons à nouveau la plateforme de commerce électronique : nous divisons les produits en catégories. Une catégorie a plusieurs produits (la catégorie Technologie a plusieurs produits comme des téléphones cellulaires, des ordinateurs portables, etc.) et un produit peut appartenir à plusieurs catégories (le produit Téléphone cellulaire appartient aux catégories Technologie et Électronique). Dans cet exemple, nous avons la table Produits, la table Catégories et une relation n-n.

### Mode Rails ON

Nous comprenons maintenant la signification des bases de données, nous avons essayé quelques requêtes de base et avons parlé de la relation entre les tables. Mais comment pouvons-nous utiliser ces connaissances dans le **_monde du développement web et de Ruby on Rails_** ?

Tout d'abord : **Rails** _est_ **Rails**. La **Base de données** _est_ **Base de données**. Est-ce évident ? Mais les gens se confondent généralement à ce sujet.

Un modèle _User_ **peut** représenter une table _Users_. Mais le modèle n'est pas la table.

* Dans la **_base de données_**, nous avons des _tables_ et des _lignes_.
* Dans **_Rails_**, nous avons des _modèles (classes)_ et des _objets_.

Imaginez un site de blog. Le blog a besoin d'un auteur pour chaque article. Nous créons donc une table **Authors** avec quelques colonnes (first_name, last_name, etc) :

Dans la migration, nous ajoutons les colonnes `first_name`, `last_name`, `email`, `birthday`, `created_at` et `updated_at`. (`created_at` et `updated_at` sont créés par le code `t.timestamps`).

Nous créons donc une migration (code Ruby), exécutons la commande `rake db:migrate` dans le terminal, et cela génère une table `**Authors**` avec les colonnes `first_name`, `last_name`, `email`, `birthday`, `created_at` et `updated_at`.

Retour à Rails — nous pouvons créer un modèle `**Author**` :

Nous avons donc une table `Authors` avec quelques colonnes et un modèle `Author`.

#### Utilisation de la console Rails

Ouvrez le terminal et tapez `bundle exec rails c`. N'oubliez pas, nous sommes dans la console **RAILS**, nous avons donc des classes, des objets, des attributs, etc.

### Relations dans Rails

Nous avons créé une table/modèle `Authors`. Ce dont nous avons besoin maintenant est une table/modèle `Posts`. Un auteur a plusieurs articles et un article appartient à un auteur spécifique. La relation ici est **un à plusieurs** (**1-n**). Vous vous souvenez ?

Ainsi, lorsque nous créons une table `Posts`, nous devons stocker une référence à l'auteur de l'article (colonne **author_id** dans la table **Posts**). C'est ce qu'on appelle la `Foreign Key`.

Et comment relions-nous les modèles ?

#### author `has_many` posts

#### post belongs_to an author

#### Utilisation de la console Rails

* Explication rapide sur `has_many` et `belongs_to`. Les deux `codes` sont des méthodes définies sur la classe `ActiveRecord`. Vous pouvez voir que nous créons nos modèles en héritant de `ActiveRecord::Base`.

Souvenez-vous dans mon article [Ruby Foundation](https://medium.freecodecamp.org/learning-ruby-from-zero-to-hero-90ad4eecc82d) que nous avons appris la programmation orientée objet, la partie sur l'héritage ? C'est pourquoi nous pouvons utiliser les méthodes `has_many` et `belongs_to` sans les définir nulle part dans notre application. Rails s'en charge pour nous.

Si vous voulez comprendre ce concept en profondeur, clonez le [dépôt Rails](https://github.com/rails/rails) ou consultez [Behind the Scenes of the 'Has Many' Active Record Association](http://callahan.io/blog/2014/10/08/behind-the-scenes-of-the-has-many-active-record-association/).

### Requêtes dans Rails

Nous pouvons interroger en utilisant les méthodes ActiveRecord :

* **all** : Obtenir tous les objets d'un modèle spécifique.

En coulisses, cela exécute la requête `SELECT * FROM posts`.

* **find** : En utilisant find, nous pouvons obtenir l'objet par l'_id_ (clé primaire).

En coulisses, cela exécute la requête `SELECT * FROM posts WHERE id = 1`.

* **where** : Obtenir les objets qui passent les conditions.

En coulisses, cela exécute la requête `SELECT * FROM posts WHERE title = 'Database & Rails'`.

* **order** : Trier tous les objets en fonction d'une colonne.

En coulisses, cela exécute la requête `SELECT * FROM posts ORDER BY created_at DESC`.

### C'est tout !

Nous avons appris beaucoup ici. J'espère que vous appréciez le contenu et en apprenez davantage sur le fonctionnement des bases de données et des modèles Rails.

C'est une étape de plus dans mon parcours pour apprendre et maîtriser Rails et le développement web. Vous pouvez voir la documentation de mon parcours complet ici sur ma publication [**Renaissance Developer**](https://medium.com/the-renaissance-developer).

Si vous voulez un cours complet sur [Ruby](https://onemonth.com/courses/ruby?mbsy=lG6tt&mbsy_source=97541b09-e3ab-45d7-a9b1-dbc77028e008&campaignid=33446&discount_code=TKRuby1) et [Rails](https://onemonth.com/courses/rails?mbsy=lG6tz&mbsy_source=d2442db6-e764-401a-a394-a9c081468830&discount_code=TKRuby1&campaignid=33448), apprendre des compétences de codage du monde réel et construire des projets, essayez [**_One Month Ruby Bootcamp_**](https://onemonth.com/courses/ruby?mbsy=lG6tt&mbsy_source=97541b09-e3ab-45d7-a9b1-dbc77028e008&campaignid=33446&discount_code=TKRuby1) et [**_Rails Bootcamp_**](https://onemonth.com/courses/rails?mbsy=lG6tz&mbsy_source=d2442db6-e764-401a-a394-a9c081468830&discount_code=TKRuby1&campaignid=33448). À bientôt ☺

Amusez-vous bien, et continuez à apprendre et à coder.

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☺