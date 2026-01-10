---
title: Outils puissants pour la visualisation et l'analyse des données Elasticsearch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T17:00:00.000Z'
originalURL: https://freecodecamp.org/news/powerful-tools-for-elasticsearch-data-visualization-analysis
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/Copy-of-designing-a-scandinavian-style-home--1--1.png
tags:
- name: big data
  slug: big-data
- name: data analytics
  slug: data-analytics
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Developer Tools
  slug: developer-tools
- name: elasticsearch
  slug: elasticsearch
- name: NoSQL
  slug: nosql
- name: Web Development
  slug: web-development
seo_title: Outils puissants pour la visualisation et l'analyse des données Elasticsearch
seo_desc: 'By Veronika Rovnik


  The goal is to turn data into information, and information into insight.

  ―Carly Fiorina


  About Kibana


  Kibana is a piece of data visualization software that provides a browser-based interface
  for exploring Elasticsearch data and n...'
---

Par Veronika Rovnik

> Le but est de transformer les données en informations, et les informations en perspectives.

> — Carly Fiorina

# À propos de Kibana

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Kibana-Color-Lockup.png)

[Kibana](https://www.elastic.co/products/kibana/?r=fr4) est un logiciel de **visualisation de données** qui fournit une interface basée sur un navigateur pour _explorer les données Elasticsearch_ et _naviguer dans l'Elastic Stack_ — une collection de produits open-source (Elasticsearch, Logstash, Beats, et autres).

Alors que Logstash et Beats livrent les données à Elasticsearch, **Kibana** _ouvre une fenêtre sur l'Elastic Stack_, vous permettant de suivre la _santé de votre cluster_, d'effectuer des _analyses de logs_ et de _séries temporelles_, de détecter des anomalies dans les données avec l'_apprentissage automatique non supervisé_, de découvrir des relations à l'aide de _graphes_ et, surtout, d'extraire des insights des données Elasticsearch avec des **visualisations** qui peuvent être combinées dans un _tableau de bord interactif personnalisé_.

Aujourd'hui, j'aimerais vous montrer comment créer un superbe **tableau de bord** et un rapport tabulaire **report** basé sur les données Elasticsearch.

Retroussez vos manches et commençons !

# Par où commencer

La page **Accueil** est l'endroit où tout commence.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_fpQgMCmvLqiFhur2.png)

Ici, vous pouvez décider des actions à entreprendre ensuite. Les fonctionnalités disponibles peuvent être divisées en deux sections logiques :

* **Visualisation** et **exploration** des données. Ici, vous pouvez créer un nouveau tableau de bord, une visualisation ou une présentation, construire un modèle d'apprentissage automatique, analyser les relations dans vos données à l'aide de **graphes**, et plus encore.
* **Gestion** de l'**Elastic Stack** : configurer vos espaces, analyser les logs d'une application, configurer les paramètres de sécurité, etc.

Nous nous concentrerons sur le processus de création de visualisations et leur ajout au tableau de bord.

# Comment créer un tableau de bord dans Kibana

Permettez-moi de vous donner une idée de la facilité avec laquelle vous pouvez configurer un _tableau de bord riche et commencer à rapporter_.

La première étape essentielle consiste à _importer vos données_ dans Kibana. Plusieurs options pour ajouter des données sont à votre disposition — vous pouvez choisir celle qui vous convient le mieux :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_sRsqKuv7Ptw0Clt1.png)

À des fins de démonstration, j'ai sélectionné les données d'exemple.

Pour concevoir vos premières visualisations de données et les combiner dans le tableau de bord, ouvrez la page **Visualiser**. Ici, vous pouvez créer, modifier et visualiser les visualisations existantes.

Ce qui vous frappera immédiatement, c'est l'abondance des **types de visualisation** parmi lesquels vous pouvez choisir.

Après avoir sélectionné celui dont vous avez besoin, choisissez un modèle d'index comme source afin d'informer Kibana de votre index. Choisissons `kibana_sample_data_flights` et commençons à créer un graphique à barres horizontales.

Vous pouvez maintenant appliquer une agrégation de métriques pour l'axe Y et une agrégation de buckets pour l'axe X. Voici une [liste](https://www.elastic.co/guide/en/kibana/7.1/xy-chart.html) de toutes les agrégations disponibles pour les graphiques.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/HorizontalBarChartKibana.gif)
_Création d'un graphique à barres horizontales dans Kibana_

Facultativement, vous pouvez personnaliser les couleurs de la visualisation.

Le **filtrage** est une autre fonctionnalité puissante d'Elasticsearch et de Kibana. Il offre un moyen de visualiser uniquement un sous-ensemble sélectionné de documents.

Voyez comment vous pouvez appliquer des filtres aux champs en fonction de conditions logiques :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/FilteringBarChartKibana.gif)

Comme vous le voyez, Kibana offre une manière simple de filtrer les données via une interface conviviale. De plus, vous pouvez choisir comment filtrer les données — soit en utilisant le **langage de requête Kibana** (une syntaxe de requête simplifiée) ou **Lucene**.

Pour permettre aux utilisateurs finaux de filtrer les données de manière interactive, vous pouvez ajouter des widgets de **contrôle** — des éléments spéciaux du tableau de bord qui permettent de filtrer les données simplement en cliquant dessus.

Une autre fonctionnalité que je souhaite mettre en avant est le **filtrage avancé par dates** et la possibilité de définir des intervalles de temps pour rafraîchir les données dans le tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0_dO63HLLppucTAw4M.png)

Le bon point est que les visualisations sont **réutilisables**. Après l'avoir créée, vous pouvez **sauvegarder votre résultat** et l'ajouter au tableau de bord à tout moment ainsi que le **partager** avec vos collègues, à condition qu'ils aient accès à votre instance Kibana.

![Image](https://miro.medium.com/max/38/0*sIPxndN5TdA8xOEH?q=20)
_Sauvegarde d'une visualisation dans Kibana_

Après avoir disposé tous les éléments de visualisation sur une seule page, vous pouvez exporter le tableau de bord final au format **PNG** ou **PDF**. C'est ce qui rend les tableaux de bord portables — il est facile de les partager entre les départements en un rien de temps.

Regardons un exemple de tableau de bord que vous pouvez créer :

![Image](https://miro.medium.com/max/38/0*N3TOSp4x8RObP9O-?q=20)
_Interaction avec le tableau de bord dans Kibana_

À mon avis, les principales caractéristiques qui rendent chaque tableau de bord spécial sont l'**interactivité** et l'**expressivité**. Avec cela, vous pouvez communiquer efficacement les métriques commerciales.

# Impression personnelle

Les visualisations dans Kibana remplissent idéalement les tâches pour lesquelles elles sont conçues. De plus, toutes les visualisations sont **attrayantes** et vous pouvez les adapter selon vos idées de design. L'ensemble du processus de création d'un tableau de bord dans Kibana est conçu pour être _rapide_ et _efficace_ — et c'est le cas grâce à l'interface conviviale et intuitive de Kibana.

D'un autre côté, j'ai senti qu'il manquait certaines fonctionnalités ici.

Lorsqu'on travaille avec des données, l'une des techniques exploratoires efficaces que vous pouvez appliquer est le **découpage** et le **dés** de vos données avant de savoir quels aspects des données méritent votre attention. À mon avis, le widget de tableau de données n'est pas la meilleure option — il présente les données dans un tableau plat qui ne supporte pas une vue multidimensionnelle des données. Mais jouer avec les données devrait se faire de manière interactive et rapide.

Et c'est là qu'un **contrôle de tableau croisé dynamique** entre en jeu. Après avoir recherché les solutions disponibles, mon choix s'est porté sur un **plugin** open-source appelé [Flexmonster](https://www.flexmonster.com/?r=fr4). Il gère la connexion à l'_index Elasticsearch_ et permet de créer des **rapports tabulaires** basés sur les données de ses documents. De plus, l'intégration avec Kibana est fluide — la seule chose requise pour commencer est d'installer un plugin en exécutant une ligne de code dans la ligne de commande. Vous pouvez trouver plus de détails sur [GitHub](https://github.com/flexmonster/pivot-kibana). Avant de l'utiliser, je recommande de vous assurer que vos instances Kibana et Elasticsearch sont de la même version.

Une fois que vous avez configuré l'outil, vous êtes prêt à utiliser toutes les fonctionnalités disponibles pour rechercher des insights approfondis.

# Fonctionnalités pour l'analyse et la création de rapports

Flexmonster Pivot offre un accès rapide aux fonctionnalités de création de rapports les plus essentielles. Sa barre d'outils permet de se connecter à la source de données, de charger des rapports précédemment sauvegardés, d'exporter des rapports en **PDF**, **Excel**, **HTML**, **CSV**, et en images. De plus, j'ai réussi à basculer rapidement entre deux modes différents — la grille et les graphiques. Les options de formatage des cellules incluent le **formatage conditionnel** et le **formatage des nombres**. La liste des champs mérite une attention particulière — ici, vous pouvez sélectionner des hiérarchies pour les lignes, les colonnes, les mesures et les filtres de rapport. Il y a également le _champ de saisie de recherche_ qui est utile si l'index a une longue liste de champs.

L'une des fonctionnalités que je souhaite mettre en avant est la possibilité de **glisser-déposer** les hiérarchies directement sur la grille. Ainsi, vous pouvez changer complètement la tranche via l'interface utilisateur.

Une autre est la fonctionnalité de **forage** — elle aide à savoir quels enregistrements se cachent derrière les valeurs agrégées.

# Travailler avec un tableau croisé dynamique

Permettez-moi de vous montrer comment créer un rapport basé sur les données Elasticsearch :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/ReportInKibanaDevTo2.gif)

Lors du test de l'outil, j'ai réussi à _agréger_ et _filtrer_ les données, à _trier_ les valeurs sur la grille et à sauvegarder les résultats pour continuer à travailler avec le rapport plus tard. De plus, l'exportation fonctionne bien — il est facile de partager les rapports avec les membres de l'équipe.

# Tout mettre ensemble

Aujourd'hui, j'ai couvert les avantages que Kibana offre pour la visualisation des données Elasticsearch. Vous avez pu vous assurer de la manière dont les tableaux de bord peuvent renforcer le processus d'analyse.

À mon avis, un tableau croisé dynamique est un bon outil qui vous permet de tirer parti de l'exploration des données avant de trouver les réponses à des questions complexes.

Flexmonster complète bien les fonctionnalités disponibles de Kibana — les rapports que vous créez avec sont perspicaces, personnalisables et peuvent être facilement partagés entre les départements.

En travaillant ensemble, les deux outils ont tout le potentiel pour stimuler votre narration.

Je vous encourage à essayer une telle combinaison.

## Qu'est-ce qui suit ?

* [Création de rapports avec Kibana](https://www.elastic.co/products/stack/reporting/?r=fr4)
* [Créer une visualisation dans Kibana](https://www.elastic.co/guide/en/kibana/current/createvis.html)
* [Tableau croisé dynamique pour Elasticsearch](https://www.flexmonster.com/demos/connect-elasticsearch/?r=fr4)
* [Comment ajouter un tableau croisé dynamique à Kibana](https://www.flexmonster.com/blog/new-pivot-table-for-kibana/?r=fr4)