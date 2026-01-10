---
title: Outils puissants pour la visualisation des données MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-11T14:28:52.000Z'
originalURL: https://freecodecamp.org/news/mongodb-data-visualization-tools-565000c7309
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OUB8k2i29fHzusm5H5lW0Q.png
tags:
- name: data analysis
  slug: data-analysis
- name: MongoDB
  slug: mongodb
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Outils puissants pour la visualisation des données MongoDB
seo_desc: 'By Veronika Rovnik

  With a myriad of visualization tools available, it is hard to find the right one
  for MongoDB data which has out-of-the-box functionality.

  Today, I want to tell you about my experience in exploring such visualization tools.

  My goal ...'
---

Par Veronika Rovnik

Avec une myriade d'outils de visualisation disponibles, il est difficile de trouver celui qui convient pour les données MongoDB avec une fonctionnalité prête à l'emploi.

Aujourd'hui, je souhaite vous parler de mon expérience dans l'exploration de tels outils de visualisation.

Mon objectif était d'analyser un ensemble de données provenant d'une base de données MongoDB. Je voulais élaborer un flux de travail pour l'analyse de données qui combine la gestion de base de données, l'agrégation de données et la visualisation de données.

Voici les outils que j'ai choisis :

* [Compass](https://www.mongodb.com/products/compass/?r=m3) est une application GUI pour l'analyse approfondie et la visualisation des données MongoDB et du schéma des collections. Il offre une vue en temps réel de vos données. L'interface intuitive m'a aidé à me concentrer sur la signification des données.
* [Flexmonster Pivot Table](https://www.flexmonster.com/?r=m3) est un outil pour le reporting web avancé et l'analyse. Alors que Compass est une application autonome, j'ai découvert que Flexmonster est intégré directement dans le projet web. J'ai réussi à l'intégrer dans mon application Angular 4 et je l'ai utilisé pour l'analyse de données.

La première partie du processus de visualisation consiste à établir une connexion à une base de données MongoDB avec Compass. Ensuite, vous pouvez explorer les fonctionnalités offertes par Compass et les analyses que vous pouvez effectuer avec cet outil.

La deuxième partie est dédiée à l'analyse approfondie des données MongoDB. Nous allons charger les données dans un tableau croisé dynamique et explorer les possibilités offertes.

En tant que source de données pour ma recherche, j'ai choisi un [ensemble de données sur 120 ans d'histoire et de résultats olympiques](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/?r=m3).

Cet ensemble de données a une structure JSON typique qui diffère du format requis par MongoDB. Pour importer cela dans MongoDB, j'ai exécuté la commande suivante dans le CLI :

```bash
mongoimport\u200a-\u200adb <db-name>\u200a-\u200acollection athletes\u200a-\u200atype json\u200a-\u200afile athletes.json
\u200a-\u200ajsonArray
```

### Comprendre les données avec Compass

Tout d'abord, je mentionnerai quelques fonctionnalités de gestion de base de données.

Compass est capable de générer des histogrammes pour représenter la fréquence des données. Cela m'a aidé à analyser la présence de documents, les types de données et la distribution des valeurs pour des champs spécifiques au sein de la collection.

Tout d'abord, je me suis connecté à l'instance MongoDB en cours d'exécution sur localhost en utilisant l'application Compass.

Sur la page principale de la collection "athletes", j'ai vérifié les informations sur la collection, édité les données en mode interactif et essayé des requêtes simples et complexes.

Un outil de visualisation de schéma m'a aidé à comprendre mes données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mlw7BqAOwmKGK0LylRtOsA.gif)

Ici, j'ai vérifié les statistiques sur les types de données des champs : le pourcentage de types de données utilisés pour ce champ dans tous les documents de la collection.

J'ai identifié que j'avais des types de données mixtes pour certains champs. Dans mon exemple, j'ai un type numérique pour 'Height' dans 80 % des documents, mais un type chaîne apparaît dans 20 % des cas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8_VabJnhX1qDKbAqtg_LiQ.gif)

Pour moi, cela signifiait qu'il y avait un écart dans mon ensemble de données. La taille est stockée différemment entre les athlètes.

### Agrégation avec Compass

Quelles fonctionnalités rendent MongoDB et Compass si populaires parmi les analystes de données qui travaillent souvent avec des données semi-structurées et non structurées ?

MongoDB est utile pour l'analyse en temps réel car il prend en charge les pipelines d'agrégation. Ceux-ci peuvent inclure des opérations de tri et de filtrage, et le regroupement des données.

Alors que Compass prend en charge la construction de requêtes en temps réel pour l'agrégation.

Pour me concentrer sur des portions spécifiques des données, j'ai filtré les documents par le champ 'Age'.

Pour afficher uniquement les athlètes de moins de 22 ans, j'ai sélectionné la zone nécessaire sur l'histogramme pour construire une requête sur le champ 'Age'. En conséquence, les documents correspondants ont été retournés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nudvk6OBTCbPWu3OEB73QA.gif)

De la même manière, j'ai filtré par plage de valeurs. Ensuite, j'ai trié les données par 'Age' dans l'ordre croissant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1_Apj6daGZhK3b6fE0CTtg.gif)

Mais pour construire des étapes dans le pipeline d'agrégation et regrouper les données, j'ai dû utiliser mes connaissances du langage de requête MongoDB. Cela a été plus facile à faire dans le tableau croisé dynamique.

### Analyser les données avec Flexmonster Pivot Table

Dans mes projets web, j'utilise Angular. J'ai donc suivi un [tutoriel Angular](https://www.flexmonster.com/doc/integration-with-angular/?r=m3) pour intégrer le tableau croisé dynamique. Pour obtenir les données de ma base de données, j'ai utilisé [ce tutoriel](https://www.flexmonster.com/doc/connecting-to-database-with-node-js/?r=m3).

Je me suis connecté à MongoDB depuis mon application et j'ai récupéré les données sur les athlètes. Les données ont été compressées puis transmises au tableau croisé dynamique pour visualisation.

Après avoir chargé les données d'exemple sur les athlètes dans le tableau croisé dynamique, j'ai voulu analyser l'âge minimum et maximum parmi les athlètes. De plus, je voulais définir les meilleures équipes de l'histoire en fonction de leur quantité totale de médailles.

Pour commencer l'analyse des données, j'ai sélectionné des champs pour les colonnes et les lignes.

Pour travailler avec le champ 'Medal', je l'ai sélectionné pour les mesures et j'ai obtenu les résultats suivants :

1. J'ai filtré les enregistrements par valeur pour afficher les 5 meilleures équipes avec la plus grande quantité de médailles
2. J'ai appliqué un formatage conditionnel pour mon rapport afin de mettre en évidence les équipes qui ont plus de 185 médailles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yx0TrC9X_j8sWSKFOpkqiw.gif)

3. Ensuite, j'ai sélectionné 'Age' et analysé l'âge maximum parmi les athlètes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*C8lcD5ZnabihXmSpb7SmxQ.gif)

4. Puis j'ai basculé vers les graphiques croisés dynamiques et analysé les données de manière plus visuelle pour en savoir plus sur les meilleures équipes de la saison estivale :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LaVrjAbGNQ2Ey-W5TznK0g.gif)

### Conclusion

Ainsi, aujourd'hui j'ai partagé mon expérience d'utilisation de Compass et de Flexmonster Pivot Table. À mon avis, ces deux outils sont capables d'aider à créer une histoire visuelle créative et à analyser les données de manière intelligente.

J'espère que vous avez trouvé utile la lecture de mon expérience et que vous êtes maintenant sur la bonne voie pour une analyse réussie des données MongoDB.

Je serais ravie d'entendre vos retours sur cet aperçu. Veuillez donner votre opinion dans les commentaires. Quels outils pour la **visualisation des données MongoDB** pourriez-vous recommander ? Gèrent-ils et traitent-ils bien vos données ?