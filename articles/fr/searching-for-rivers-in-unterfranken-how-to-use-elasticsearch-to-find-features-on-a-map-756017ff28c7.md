---
title: 'Recherche de rivières en Basse-Franconie : comment utiliser Elasticsearch
  pour trouver des éléments sur une carte'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T23:25:16.000Z'
originalURL: https://freecodecamp.org/news/searching-for-rivers-in-unterfranken-how-to-use-elasticsearch-to-find-features-on-a-map-756017ff28c7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H2M5xGnz5mqH_y760kT7-g.jpeg
tags: []
seo_title: 'Recherche de rivières en Basse-Franconie : comment utiliser Elasticsearch
  pour trouver des éléments sur une carte'
seo_desc: 'By 24ma13wg

  One of the great things about working remotely is that I can work from wherever
  I want to. So, this month I have swapped my city desk in London for one in the spa
  town of Bad Kissingen, Germany.

  I’ve also had fun building search engines w...'
---

Par 24ma13wg

L'un des grands avantages du travail à distance est que je peux travailler d'où je veux. Ce mois-ci, j'ai donc échangé mon bureau en ville à Londres contre un autre dans la ville thermale de Bad Kissingen, en Allemagne.

J'ai également pris plaisir à construire des moteurs de recherche avec [Elasticsearch](https://www.elastic.co/). Dans cet article, je vais explorer comment il peut être utilisé pour rechercher des éléments sur une carte.

### Index de recherche

Assis ici à mon nouveau bureau, je feuillette un vieux manuel scolaire. À la fin, il y a un index. Il m'indique sur quelles pages apparaissent certains mots-clés. Ainsi, si je veux lire quelque chose de spécifique, je peux trouver rapidement les numéros de page pertinents. Sans l'index, je devrais parcourir toutes les pages du livre pour trouver ce qui m'intéresse.

De même, lorsque nous recherchons des choses sur Internet — bien que nous n'en soyons peut-être pas conscients — nous utilisons probablement également un index (plus sophistiqué) pour rendre notre recherche rapide. Nous posons des questions à l'index et obtenons des réponses en retour. Plus précisément, en ce qui concerne Elasticsearch, nous interrogeons l'index en envoyant des requêtes RESTful API, sous forme de [JSON](https://www.json.org/). Les résultats sont retournés.

### La famille JSON

JSON est un format couramment utilisé pour structurer les données. En termes simples, il exprime les données sous forme de groupes de paires nom/valeur, dans une chaîne de texte. Par exemple :

```
{  "ville": "Erlangen",  "pays": "Allemagne"},{  "ville": "Würzburg",  "pays": "Allemagne"}
```

Minifié, notre exemple ressemble à ceci :

```
{"ville":"Erlangen","pays":"Allemagne"},{"ville":"Würzburg","pays":"Allemagne"}
```

Souvent, nous nous intéressons à l'indexation de champs de données, comme un enregistrement de produit, ou de texte intégral, comme un article de blog. Elasticsearch gère très bien ces cas. Il peut également indexer des données spatiales : des éléments de carte, tels que des lieux et des frontières. Nous utilisons un type spécial de JSON pour décrire les éléments de carte, appelé [GeoJSON](http://geojson.org/). Cela ressemble à ceci :

```
{  "type": "Feature",  "geometry": {    "type": "Point",    "coordinates": [49.792762, 9.939119]  },  "properties": {    "ville": "Würzburg",    "pays": "Allemagne"  }}
```

Un type de géométrie peut être un : `Point`, `LineString`, ou `Polygon`. Il existe des types multi pour ceux-ci : `MultiPoint`, `MultiLineString`, et `MultiPolygon`. Plusieurs éléments, comme l'emplacement ci-dessus, peuvent être contenus dans un `FeatureCollection`.

Bad Kissingen est l'une des nombreuses communautés de la région de Basse-Franconie (_Unterfranken_ en allemand). Comme beaucoup de ses voisins, une rivière la traverse : la Fränkische Saale. La frontière de la communauté forme une seule forme ; elle correspond au type de géométrie `Polygon`. Les cours d'eau qui composent la rivière peuvent être imaginés comme une série de lignes jointes ensemble. Ils correspondent au type `MultiLineString`.

J'ai trouvé des cartes de Basse-Franconie en ligne. Je peux traiter toutes les rivières et communautés de la région en [NDJSON](http://ndjson.org/) (délimité par des sauts de ligne — une autre variation de JSON). Je crée un index Elasticsearch et charge les données dedans. Maintenant, je suis prêt à rechercher. _Gut, wir machen einen Test!_

### Recherche de rivières

Une simple requête de terme me dit qu'il y a 22 rivières et 360 communautés en Basse-Franconie. Il y a beaucoup plus de cours d'eau dans les données téléchargées, mais seulement 22 sont définis comme des rivières. Il est temps d'essayer des requêtes plus complexes. Je vais commencer par la principale rivière de la région, le Main, qui se prononce _Mine_ en allemand. Je me demande combien de communautés elle traverse ? La requête que j'envoie à mon index ressemble à ceci :

```
GET lower_franconia/default/_search{  "query": {    "bool": {      "filter": [        {          "term": {            "feature": "community"          }        },         {          "geo_shape": {            "geometry": {              "indexed_shape": {                "index": "lower_franconia",                "type": "default",                "id": "12",                "path": "geometry"              },              "relation": "intersects"            }          }        }      ]    }  }}
```

Cette requête est exécutée dans un contexte de `filtre`. Cela signifie que les scores de pertinence ne sont pas calculés. Je ne m'intéresse pas à la qualité des correspondances, mais plutôt à savoir si une correspondance existe ou non. Dans ce contexte, je spécifie un tableau de deux éléments.

Dans le premier élément, je spécifie une clé `term` avec les éléments de communauté comme contrainte. Cela signifie que seuls les documents de mon index qui ont une valeur de `community` dans le champ `feature` seront retournés.

Dans le deuxième élément du tableau, j'ai une requête `geo_shape` spécifiant le document numéro `12` (ce document décrit la rivière Main) et une relation de `intersects` comme contraintes.

En termes simples, faire correspondre toutes les formes de communauté qui intersectent avec une ligne de rivière particulière.

J'obtiens 91 résultats. Un quart de toutes les communautés sont sur le Main. Le résultat est formaté en — oui, vous l'avez deviné — JSON. Bien que le JSON soit assez lisible, il n'est pas facile à comprendre d'un coup d'œil. Mieux vaut créer une visualisation de données avec [d3.js](https://d3js.org/) afin que les résultats puissent être compris instantanément.

![Image](https://cdn-media-1.freecodecamp.org/images/fO0y5H9ExU-h5xOB5lPQFK3GcVKhEn2OdHCJ)
_Hé Elasticsearch, quelles communautés la rivière Main traverse-t-elle ?_

Pour plus de détails sur la manière dont cela est fait, voir mon précédent article sur la cartographie de pages web.

[**Un ours brun, un ours noir et un ours polaire pourraient-ils se rencontrer ?**](https://towardsdatascience.com/could-a-brown-bear-a-black-bear-and-a-polar-bear-meet-9b82f4a9948d)
[_La cartographie de pages web peut nous montrer où_towardsdatascience.com](https://towardsdatascience.com/could-a-brown-bear-a-black-bear-and-a-polar-bear-meet-9b82f4a9948d)

Ensuite, combien de rivières sont à proximité ? Si je veux me promener au bord d'une rivière ce soir, mais que je ne veux pas voyager, disons plus de dix kilomètres, quelles sont mes options ?

![Image](https://cdn-media-1.freecodecamp.org/images/-Slqcj8PvbRjm1UJLTAEwli3-xnpz24uUbNZ)
_Combien de rivières se trouvent à moins de dix kilomètres de mon bureau ?_

Quatre résultats reviennent : les rivières Aschach, Fränkische Saale, bien sûr, Thulba, et Premich. Cette requête est légèrement différente de la précédente. Cette fois, je ne veux que des rivières en retour. De plus, je spécifie une nouvelle forme qui n'existe pas dans l'index. Un cercle qui est centré sur ma position actuelle avec un rayon de dix kilomètres.

Une de plus. Où ne devrais-je pas aller si je veux me promener au bord d'une rivière ? Pour cette requête, j'utilise une clé `must_not` pour filtrer les communautés qui intersectent avec l'une des 22 rivières. J'obtiens 199 résultats — juste un peu plus de la moitié des communautés de Basse-Franconie n'ont pas de rivière.

![Image](https://cdn-media-1.freecodecamp.org/images/3gwAiE6woLLZ88N9f8-Ln3IALfcyMCScjWFQ)
_Quelles communautés n'ont pas de rivière ?_

### Application dans le monde réel

J'ai utilisé les rivières et les communautés de Basse-Franconie comme un exemple simple pour illustrer comment les éléments de carte peuvent être indexés avec Elasticsearch, et les résultats de la requête visualisés avec d3.js.

Pourrait-il avoir une application pratique ? Eh bien, l'index pourrait être utilisé, par exemple, pour savoir quelles communautés avertir si une alerte d'inondation était émise pour une rivière particulière. Peut-être pourrait-il être utilisé, dans une région plus sèche, pour prédire où les sécheresses pourraient causer des problèmes pour l'agriculture.

Bien sûr, nous ne sommes pas limités aux cours d'eau et aux frontières des communautés. Toute combinaison d'éléments de carte peut être cartographiée et indexée et, par conséquent, il existe de nombreuses applications possibles.

_Données : [OpenStreetMap](https://www.geofabrik.de) + [Open Data Portal des Freistaats Bayern](https://opendata.bayern.de)_

_Publié à l'origine sur [24ma13wg.github.io](https://24ma13wg.github.io/searching-for-rivers-in-unterfranken/page.html)._