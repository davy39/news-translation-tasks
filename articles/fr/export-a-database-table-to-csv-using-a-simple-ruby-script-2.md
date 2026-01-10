---
title: Comment exporter une table de base de données vers un fichier CSV à l'aide
  d'un script Ruby simple
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2019-08-19T05:28:00.000Z'
originalURL: https://freecodecamp.org/news/export-a-database-table-to-csv-using-a-simple-ruby-script-2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0cc740569d1a4ca4ada.jpg
tags:
- name: Ruby
  slug: ruby
seo_title: Comment exporter une table de base de données vers un fichier CSV à l'aide
  d'un script Ruby simple
seo_desc: If you have a Rails project and want to export a table as a CSV, without
  having to go to all the trouble of finding a gem, installing and using it, then
  uninstalling it when it’s no longer needed, I have some good news. Here’s an easy
  and quick way t...
---

Si vous avez un projet Rails et que vous souhaitez exporter une table au format CSV, sans avoir à chercher un gem, l'installer et l'utiliser, puis le désinstaller lorsqu'il n'est plus nécessaire, j'ai une bonne nouvelle. Voici une méthode simple et rapide pour exporter une table spécifique de votre base de données vers un fichier CSV.

Voici le [code](https://gist.github.com/foxumon/fdb30349545944eee58c7858e6bab23c) que vous devez exécuter. Vous pouvez le placer dans une tâche Rake et l'exécuter, ou l'exécuter d'une autre manière.

Comme vous pouvez le voir, nous commençons par importer `CSV` — nous en avons besoin pour écrire le fichier CSV avec les données de la base de données. Ensuite, nous choisissons l'emplacement et le nom du fichier que nous voulons exporter, qui dans notre cas sera un fichier nommé *data.csv* inclus dans le répertoire *public*.

Ensuite, nous définissons la table que nous voulons exporter et commençons à écrire. Nous pourrions également modifier les attributs que nous voulons exporter — nous n'avons pas à tous les inclure tels qu'ils sont dans la base de données.

C'est tout ! C'est aussi simple que cela et pourtant très utile.

*Cet article a été initialement publié sur* [*Medium*](https://medium.com/better-programming/export-a-database-table-to-csv-using-a-simple-ruby-script-5577a0914eb0?source=friends_link&sk=6debc0a92a8679247534b2e60a42f516)