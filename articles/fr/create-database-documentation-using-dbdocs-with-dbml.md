---
title: Comment créer une documentation de base de données en utilisant dbdocs avec
  DBML
subtitle: ''
author: Truong-Phat Nguyen
co_authors: []
series: null
date: '2024-10-14T15:56:30.047Z'
originalURL: https://freecodecamp.org/news/create-database-documentation-using-dbdocs-with-dbml
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728620241328/79515009-0fa3-4fcd-a4ce-e1ec2d5609f8.png
tags:
- name: Databases
  slug: databases
- name: Devops
  slug: devops
- name: ci-cd
  slug: ci-cd
- name: data
  slug: data
seo_title: Comment créer une documentation de base de données en utilisant dbdocs
  avec DBML
seo_desc: 'Database documentation plays a crucial role in maintaining and scaling
  systems. Clear and well-organized documentation can significantly improve communication
  between team members and enhance project longevity.

  One of the most efficient ways to docum...'
---

La documentation de base de données joue un rôle crucial dans la maintenance et la mise à l'échelle des systèmes. Une documentation claire et bien organisée peut améliorer considérablement la communication entre les membres de l'équipe et renforcer la longévité du projet.

L'une des méthodes les plus efficaces pour documenter une base de données est d'utiliser [**dbdocs**](https://dbdocs.io/) et [**DBML**](https://dbml.dbdiagram.io/home) - un langage de balisage de base de données open source.

Dans ce guide, je vais vous montrer comment créer une documentation de base de données en utilisant ces outils, étape par étape.

# **Qu'est-ce que dbdocs ?**

[**dbdocs**](https://dbdocs.io/) est une plateforme qui génère une documentation de base de données à partir de votre schéma, facilement partageable via un lien. En utilisant [**DBML**](https://dbml.dbdiagram.io/home) **(Database Markup Language)**, vous pouvez créer une documentation claire, partageable et mise à jour de votre structure de base de données.

## **Prérequis**

Avant de commencer, assurez-vous d'avoir les éléments suivants :

* Des connaissances de base sur les bases de données et SQL.

* Un schéma de base de données à documenter (nous utiliserons un exemple PostgreSQL dans ce guide).

## **Étape 1 : Installer DBML CLI et dbdocs**

Commencez par installer le **DBML CLI**, qui aide à convertir votre schéma de base de données au format DBML. Vous avez également besoin du **dbdocs CLI** pour générer et publier votre documentation.

```bash
npm install -g dbdocs
```

## **Étape 2 : Exporter votre schéma de base de données vers DBML**

![Diagramme de base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1728615902517/20974a9d-729e-4b3a-997c-0b89e944a6cd.png align="center")

Si vous travaillez avec une base de données existante, vous pouvez exporter le schéma au format DBML en utilisant l'outil DBML CLI.

Pour PostgreSQL, exécutez la commande suivante :

```bash
$ dbdocs db2dbml postgres <connection-string> -o database.dbml

✓ Connexion à la base de données <db-name>... terminée.
✓ Génération du DBML... terminée.
✓ Écriture dans database.dbml
```

![Extraire le code DBML à partir de la connexion à la base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1728615885904/9f68f18b-fa14-4e88-b58b-bd90d292ef31.gif align="center")

Cette commande exportera votre schéma de base de données et l'enregistrera dans un fichier nommé `database.dbml`.

Voici un exemple de ce à quoi un fichier DBML généré pourrait ressembler :

```bash
Table users {
  id int [pk, increment]
  username varchar(50) [not null]
  email varchar(100) [not null, unique]
  created_at timestamp [not null]
}

Table orders {
  id int [pk, increment]
  user_id int [not null, ref: > users.id]
  total decimal [not null]
  created_at timestamp [not null]
}
```

**Dans cet exemple :**

• Les tables users et orders sont définies.

• Les champs sont annotés avec des types et des contraintes.

• La relation entre `orders.user_id` et `users.id` est établie en utilisant `ref`.

## **Étape 3 : Modifier et ajouter des notes au fichier DBML**

Vous pouvez souhaiter nettoyer le fichier ou ajouter une documentation supplémentaire comme des descriptions de tables et de champs pour communiquer avec les autres membres de l'équipe.

![Ajouter des notes au code DBML généré](https://cdn.hashnode.com/res/hashnode/image/upload/v1728615980279/8e1851a8-2e38-4ded-8b6a-c873d6b395b8.gif align="center")

## **Étape 4 : Générer la documentation avec dbdocs**

Une fois votre fichier DBML prêt, l'étape suivante consiste à générer la documentation en utilisant dbdocs. Tout d'abord, vous devez vous connecter à dbdocs :

```bash
dbdocs login
```

Après vous être connecté, publiez le fichier DBML :

```bash
dbdocs build database.dbml
```

![Générer la documentation de la base de données à partir du fichier DBML](https://cdn.hashnode.com/res/hashnode/image/upload/v1728616039961/0ef67db3-8a86-495a-b42f-3fad0fead933.gif align="center")

Cette commande générera un lien de documentation partageable que vous pourrez accéder via la plateforme dbdocs. Vous pouvez également définir des permissions d'accès et collaborer avec votre équipe.

Ce flux de travail transparent garantit que votre documentation reflète toujours l'état le plus récent de votre base de données.

# **Avantages de l'utilisation de dbdocs avec DBML**

* **Simplicité** : La syntaxe [DBML](https://dbml.dbdiagram.io/home) est simple et facile à apprendre, ce qui en fait un choix parfait pour les équipes.

* **Automatisation** : Vous pouvez [automatiser les mises à jour de votre documentation de base de données](https://docs.dbdocs.io/features/generate-dbml-from-db) dans le cadre de votre [pipeline CI/CD](https://docs.dbdocs.io/features/ci-integration).

* **Collaboration** : Partagez facilement des [liens de documentation](https://docs.dbdocs.io/features/project-access-control) avec votre équipe ou vos parties prenantes pour un accès et une discussion faciles.

* **Contrôle de version** : Utilisez le [journal des modifications de schéma](https://docs.dbdocs.io/features/schema-changelog) pour suivre les changements de schéma de base de données au fil du temps.

* **Visualisation** : dbdocs offre une interface propre pour visualiser votre schéma de base de données, ses relations et ses annotations. [Essayez cette démonstration](https://dbdocs.io/Holistics/Ecommerce) pour en savoir plus.

# **Conclusion**

Dans ce tutoriel, nous avons exploré comment exporter un schéma de base de données, le personnaliser et générer une documentation partageable en utilisant dbdocs.

En intégrant ce flux de travail dans votre processus de développement, vous améliorerez la collaboration de votre équipe, renforcerez la scalabilité de votre projet et vous assurerez que tout le monde reste sur la même longueur d'onde. Bonne documentation !