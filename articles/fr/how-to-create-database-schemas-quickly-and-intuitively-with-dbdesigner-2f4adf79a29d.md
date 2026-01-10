---
title: Comment créer des schémas de base de données rapidement et intuitivement avec
  DBDesigner
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2018-08-06T16:30:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-database-schemas-quickly-and-intuitively-with-dbdesigner-2f4adf79a29d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6Y5Szhl_pNIkjhu0Uo3rEw.png
tags:
- name: coding
  slug: coding
- name: database
  slug: database
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer des schémas de base de données rapidement et intuitivement
  avec DBDesigner
seo_desc: One of the most important parts of developing a project is having a clear
  picture in mind of the end goal. We need to know the target audience for the project,
  as well as the features it will include. This means that we need to be as informed
  as poss...
---

L'une des parties les plus importantes du développement d'un projet est d'avoir une image claire de l'objectif final. Nous devons connaître le public cible du projet, ainsi que les fonctionnalités qu'il inclura. Cela signifie que nous devons être aussi informés que possible sur la logique métier, puis implémenter toutes les fonctionnalités selon les besoins.

[DBDesigner](http://dbdesigner.net/) est un excellent outil lorsqu'il s'agit de créer des schémas de base de données pour votre application. Il vous permet de créer autant de tables que vous le souhaitez (pour autant que je sache). Vous pouvez ajouter n'importe quel attribut de type de données à n'importe quelle table que vous avez créée. Vous pouvez également avoir certains attributs servir de clés étrangères. Ainsi, lorsque vous configurez les clés primaires et les clés étrangères respectivement, vous pouvez voir les relations entre les tables de la base de données que vous essayez de créer.

Vous pouvez utiliser votre email et créer de nombreux projets, et y revenir chaque fois que vous le souhaitez. Vous pouvez également inviter vos collègues par email et les faire collaborer avec vous dans la préparation de ce schéma.

Lorsque vous avez une version initiale de votre schéma de base de données, vous pouvez ensuite l'exporter en tant que script SQL pour les technologies de base de données suivantes : PostgreSQL, SQLite, MySQL, MSSql et Oracle.

### **Démonstration**

Commençons par créer un nouveau schéma de base de données pour démontrer comment cela fonctionne en pratique.

Nous pouvons soit commencer avec un nouveau modèle vide, soit utiliser l'un des nombreux modèles préexistants disponibles.

Nous allons démontrer un modèle vide ici, juste pour que nous puissions voir certaines des fonctionnalités incluses. Sinon, vous ne les remarquerez peut-être pas en utilisant des modèles existants.

Tout d'abord, nous devons créer un nouveau schéma. Notre exemple utilise le type de base de données « Generic », et nous l'appellerons « library ».

Nous devons donc aller dans *Schema* &g\_t;\_ New et nous verrons une nouvelle fenêtre apparaître :

![Image](https://cdn-media-1.freecodecamp.org/images/dKGQLARUrZNYsvQzfxx65r0lfDNqFe2fTsiu align="left")

Voici l'image que nous devrions voir après cela :

![Image](https://cdn-media-1.freecodecamp.org/images/3evdVmxCEoqv6npUjobnLH1v-1RJA7qTrIS5 align="left")

Ensuite, nous devons ajouter de nouvelles tables à notre schéma, ce que nous pouvons faire en cliquant avec le bouton droit n'importe où sur la grille et en sélectionnant l'option « Table » :

![Image](https://cdn-media-1.freecodecamp.org/images/JdF6W8rIb5S1G6s0mItsmb0rRpBhRJaZIGIS align="left")

Maintenant, nous devons ajouter des champs à la table. Tout ce que nous avons à faire est d'aller dans *Add field*, après quoi une nouvelle fenêtre apparaîtra. Dans celle-ci, vous pouvez choisir le type et également configurer quelques contraintes pour votre nouvelle colonne de table :

![Image](https://cdn-media-1.freecodecamp.org/images/SiFU1HH-YjlF8zl2LL3Bo-Lwo-LIqAzImh76 align="left")

Voici à quoi cela ressemble après avoir ajouté quelques colonnes :

![Image](https://cdn-media-1.freecodecamp.org/images/8JJt351B9ZkdPyeWdRDBgf3rcykpCz1c8h9R align="left")

Ensuite, nous pouvons ajouter des relations entre les tables. Nous prendrons l'exemple de la création d'une relation *many-to-many* entre deux tables : *Authors* et *Books*. Pour cela, nous devons initialement créer une nouvelle table appelée *AuthorBooks*, dans laquelle nous ajoutons des clés étrangères qui référencent la table *Authors* et la table *Books*, respectivement :

![Image](https://cdn-media-1.freecodecamp.org/images/9QbhYFaIoE9xEMDnINK5-MsqMlMP85NCEOAa align="left")

Voici la connexion avec la table *Books* :

![Image](https://cdn-media-1.freecodecamp.org/images/RUzIA5zXMBg8rQufWIb43FIkfiBp8E0HR0H- align="left")

Après avoir terminé cela, nous devrions voir un schéma similaire au suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/kx7-qxvknuSAt85PbjOU37BP-XiHDSEe9vev align="left")

Une fonctionnalité vraiment géniale de *dbdesigner* est la flexibilité qu'il vous offre pour déplacer vos tables autour de la grille comme vous le souhaitez :

![Image](https://cdn-media-1.freecodecamp.org/images/EstgpMYYjO7hwLR7ug5pwniVvUV54uif2KQn align="left")

Nous pouvons également partager le schéma avec jusqu'à cinq collaborateurs dans la version gratuite. Nous devons simplement aller dans \_Schema &gt; Sha\_re et une nouvelle fenêtre apparaîtra, comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/yMNJVmGA6UCGGRUGNFMlAKqxdtG97Vhcb9r1 align="left")

Nous pouvons enregistrer ce schéma en tant qu'image en allant dans : \_Export &gt; Im\_age.

Nous pouvons également générer le script SQL correspondant de la manière suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/pQz9K1zslWpL3MFBUwCqqmEpmOvU7MVMPEHZ align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/lcpubCJYZNuusWp1YfBjkmUxu7dyMYviPN62 align="left")

![Image](https://cdn-media-1.freecodecamp.org/images/ftc3d8sSxITbljXkA7z4gjJ2Tv-UcuhKkEb9 align="left")

Nous pouvons également importer notre propre SQL dans le schéma et le voir représenté graphiquement :

![Image](https://cdn-media-1.freecodecamp.org/images/imO4ID01-K3ANkILlUQ-hSNHvIq9R9JYJueT align="left")

### Conclusion

J'ai entendu parler de cet outil lorsque je faisais du pair-programming avec un collègue, et je l'ai trouvé vraiment utile. J'espère que vous en bénéficierez également.

[DBDesigner](https://www.dbdesigner.net/designer/schema/187386) a d'autres fonctionnalités, et je vous recommande définitivement de les essayer.