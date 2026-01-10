---
title: Comment configurer la recherche par géolocalisation dans votre application
  avec Elasticsearch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-07T17:12:37.000Z'
originalURL: https://freecodecamp.org/news/geolocation-search-elasticsearch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd644e7e6787e098393e278.jpg
tags:
- name: database
  slug: database
- name: elasticsearch
  slug: elasticsearch
- name: geolocation
  slug: geolocation
- name: search
  slug: search
seo_title: Comment configurer la recherche par géolocalisation dans votre application
  avec Elasticsearch
seo_desc: 'By Pramono Winata

  Location-based features are pretty common in apps nowadays. These features might
  seem complicated, but they can actually be implemented quite easily with Elasticsearch.

  Elasticsearch is a NoSQL database with a document-based structu...'
---

Par Pramono Winata

Les fonctionnalités basées sur la localisation sont assez courantes dans les applications de nos jours. Ces fonctionnalités peuvent sembler compliquées, mais elles peuvent en réalité être implémentées assez facilement avec Elasticsearch.

Elasticsearch est une base de données NoSQL avec une structure basée sur des documents. Elle est souvent utilisée comme moteur de recherche. Elle fournit également sa propre syntaxe et de nombreux outils pour rendre votre recherche aussi flexible que possible.

Dans cet article, je vais vous montrer une manière simple de rechercher par géolocalisation en obtenant une liste de villes par plage de coordonnées.

## Comment installer Elasticsearch

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1-4thJErMA9UpuP1jEBLRWFQ.png)

Vous pouvez trouver un guide d'installation facile à suivre sur le site web d'Elasticsearch : [guide d'installation](https://www.elastic.co/guide/en/elasticsearch/reference/7.4/install-elasticsearch.html). Au moment où j'écris cet article, j'utilise la version 7.4.2 d'Elasticsearch.

Gardez simplement à l'esprit qu'Elasticsearch a apporté de nombreux changements dans les versions récentes, dont l'un est la [suppression des types de mapping](https://www.elastic.co/guide/en/elasticsearch/reference/master/removal-of-types.html). Donc, si vous utilisez une autre version d'Elasticsearch, certaines choses ici pourraient ne pas fonctionner complètement.

Après avoir terminé votre installation, n'oubliez pas de lancer votre service Elasticsearch, ce qu'ils soulignent clairement dans leur guide d'installation (pour Linux, faites ceci : `./bin/elasticsearch`).

**Assurez-vous que votre Elasticsearch est en cours d'exécution** en utilisant une requête GET sur le port 9200 de votre machine locale, comme ceci : [`GET http://localhost:9200`](http://localhost:9200)

## Comment créer votre index Elasticsearch

Un index est similaire à une table dans une base de données régulière. Pour cet exemple, créons un index nommé `cities` qui contiendra nos données.

Définissons également un modèle simple pour nos données :

* `id` : `keyword` pour notre identifiant
* `name` : `text` pour le nom de la ville
* `coordinate` : `geo_point` pour stocker les coordonnées de nos villes (pratique, ils ont déjà ce type de données)

Dans Elasticsearch, nous créons l'index en faisant un curl vers une API. Dans notre cas, notre requête sera comme ceci :

```
PUT http://localhost:9200/cities
```

```json
{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "id": {
                "type": "keyword"
            },
            "name": {
                "type": "text"
            },
            "coordinate": {
                "type": "geo_point"
            }
        }
    }
}
```

Lorsque vous utilisez ce curl, vous devriez obtenir une réponse comme ceci pour vérifier que votre index a été créé :

```json
{
    "acknowledged": true,
    "shards_acknowledged": true,
    "index": "cities"
}

```

Bien joué ! Maintenant, votre index est prêt à être utilisé. Continuons et amusons-nous avec notre nouvel index.

## Comment peupler les données Elasticsearch

Nous allons maintenant remplir notre index Elasticsearch avec des documents. Si vous n'êtes pas familier avec ce terme, sachez simplement qu'il est très similaire aux lignes dans une base de données SQL.

Dans Elasticsearch, il est possible de stocker des données qui ne correspondent pas à notre schéma prédéfinis. Mais nous ne ferons pas cela ici – au lieu de cela, nous insérerons des données qui correspondent à notre schéma prédéfinis.

Puisque nous allons insérer plusieurs données à la fois, nous utiliserons l'API [bulk](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html) qu'Elasticsearch fournit et qui permet plusieurs insertions en un seul appel d'API.

Dans l'exemple ci-dessous, je vais insérer 9 villes dans mon index. N'hésitez pas à en ajouter plus si vous le souhaitez.

`POST '[http://localhost:9200/cities/_bu](http://localhost:9200/cities/_bu)lk`

```json
{ "index":{"_index": "cities" } }
{ "id": 1, "name": "Jakarta", "coordinate": {  "lat": -6.2008, "lon": 106.8456}}
{ "index":{"_index": "cities" } }
{ "id": 2, "name": "Tokyo", "coordinate": {  "lat": 35.6762, "lon": 139.6503} }
{ "index":{"_index": "cities" } }
{ "id": 3, "name": "Hong Kong", "coordinate": {  "lat": 22.3193, "lon": 114.1694} }
{ "index":{"_index": "cities" } }
{ "id": 4, "name": "New York", "coordinate": {  "lat": 40.7128, "lon": -74.0060} }
{ "index":{"_index": "cities" } }
{ "id": 5, "name": "Paris", "coordinate": {  "lat": 48.8566, "lon": 2.3522} }
{ "index":{"_index": "cities" } }
{ "id": 6, "name": "Bali", "coordinate": {  "lat": -8.3405, "lon": 115.0920} }
{ "index":{"_index": "cities" } }
{ "id": 7, "name": "Berlin", "coordinate": {  "lat": 52.5200, "lon": 13.4050} }
{ "index":{"_index": "cities" } }
{ "id": 8, "name": "San Fransisco", "coordinate": {  "lat": 37.7749, "lon": -122.4194} }
{ "index":{"_index": "cities" } }
{ "id": 9, "name": "Beijing", "coordinate": {  "lat": 39.9042, "lon": 166.4074} }

```

La charge utile peut sembler étrange car elle est dans un format JSON incorrect, mais ne vous inquiétez pas – elle est supposément conçue de cette manière.

Vous devriez alors recevoir une réponse similaire à celle-ci :

```
{
    "took": 72,
    "errors": false,
    "items": [
        //contient un élément pour chaque donnée insérée
        ...
    ]
}
```

## Comment interroger vos documents Elasticsearch

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-276.png)
_Photo par [Unsplash](https://unsplash.com/@chrislawton?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Chris Lawton</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Voici la partie intéressante. Nous allons effectuer quelques requêtes avec les documents que nous avons insérés précédemment.

Elasticsearch prend en charge de nombreux types de syntaxe pour la recherche de requêtes. Il dispose également de la recherche par type de géolocalisation avec laquelle nous allons jouer aujourd'hui.

Nous pouvons simplement commencer à rechercher nos villes avec curl comme ceci :

`POST '[http://localhost:9200/cities/_sear](http://localhost:9200/cities/_sear)ch`

```json
{
  "query": {
    "bool": {
      "filter": {
        "geo_distance": {
          "distance": "10km",
          "coordinate": {
            "lat": 37.76,
            "lon": -122.42
          }
        }
      }
    }
  }
}
```

Cette requête devrait me donner San Francisco, et les coordonnées 37.7749 et -122.4194 devraient être à l'intérieur d'un rayon de distance de 10 km de nos coordonnées (grâce à Google).

```
{
    "took": 7,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 1,
            "relation": "eq"
        },
        "max_score": 0.0,
        "hits": [
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "eKPspHYBivyIhfWHb2vl",
                "_score": 0.0,
                "_source": {
                    "id": 8,
                    "name": "San Fransisco",
                    "coordinate": {
                        "lat": 37.7749,
                        "lon": -122.4194
                    }
                }
            }
        ]
    }
}
```

Félicitations ! Maintenant, vous avez votre propre moteur de recherche de localisation.   
Mais expérimentons un peu plus. Supposons que vous souhaitez obtenir plus de villes à cet endroit.

Essayons d'étendre la distance à 4500 km en modifiant la charge utile :

```json
{
  "query": {
    "bool": {
      "filter": {
        "geo_distance": {
          "distance": "4500km",
          "coordinate": {
            "lat": 37.76,
            "lon": -122.42
          }
        }
      }
    }
  }
}
```

Et vous devriez obtenir cette réponse :

```
{
    "took": 8,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 0.0,
        "hits": [
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "dKPspHYBivyIhfWHb2vl",
                "_score": 0.0,
                "_source": {
                    "id": 4,
                    "name": "New York",
                    "coordinate": {
                        "lat": 40.7128,
                        "lon": -74.0060
                    }
                }
            },
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "eKPspHYBivyIhfWHb2vl",
                "_score": 0.0,
                "_source": {
                    "id": 8,
                    "name": "San Fransisco",
                    "coordinate": {
                        "lat": 37.7749,
                        "lon": -122.4194
                    }
                }
            }
        ]
    }
}
```

Il donne deux résultats : New York et San Fransisco. Les résultats semblent corrects, mais le positionnement peut être un peu étrange. San Fransisco devrait normalement apparaître en premier car il est plus proche, n'est-ce pas ?

Eh bien, pas exactement, car ce que nous faisons est simplement du filtrage. Notre requête se contente de filtrer et ne se soucie pas de savoir lequel est le plus proche de vous. 

Mais que faire si nous voulons effectuer un calcul pour montrer quels emplacements pourraient être les plus proches ? Ne vous inquiétez pas, Elasticsearch peut le faire aussi. Nous pouvons utiliser un type de requête appelé requête de score de fonction.

### Comment utiliser une requête de score de fonction dans Elasticsearch

Elasticsearch calcule (scores) les documents qu'il montrera à l'utilisateur. En utilisant des [requêtes de score de fonction](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html), nous pouvons modifier ce score afin de déterminer quels documents doivent être retournés.

Ici, nous utiliserons la [fonction de décroissance de la requête](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html#function-decay). Il existe trois types de fonctions de décroissance : exp, linéaire et gauss. Chacune d'elles a des comportements différents.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/decay_2d.png)
_Image [source](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html#function-decay)_

Celle que nous utiliserons ici est la fonction de type linéaire. Nous spécifierons également les coordonnées ainsi que le décalage et l'échelle.

`POST '[http://localhost:9200/cities/_sear](http://localhost:9200/cities/_sear)ch`

```
{
  "query": {
    "function_score": {
      "functions": [
        {
          "linear": {
            "coordinate": {
              "origin": "37, -122",
              "offset": "100km",
              "scale":"2500km"
            }
          }
        }
      ],
       "min_score":"0.1"
    }
  }
}
```

Maintenant, nous devrions obtenir nos résultats classés par le score le plus élevé.

```
{
    "took": 32,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 1.0,
        "hits": [
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "eKPspHYBivyIhfWHb2vl",
                "_score": 1.0,
                "_source": {
                    "id": 8,
                    "name": "San Fransisco",
                    "coordinate": {
                        "lat": 37.7749,
                        "lon": -122.4194
                    }
                }
            },
            {
                "_index": "cities",
                "_type": "_doc",
                "_id": "dKPspHYBivyIhfWHb2vl",
                "_score": 0.19508117,
                "_source": {
                    "id": 4,
                    "name": "New York",
                    "coordinate": {
                        "lat": 40.7128,
                        "lon": -74.0060
                    }
                }
            }
        ]
    }
}
```

Et c'est tout !

## Conclusion

Dans cet article, nous avons couvert comment implémenter la recherche basée sur la localisation avec Elasticsearch. Mais ce n'est pas la fin – ce que je vous ai montré ici n'est que la surface de ce que vous pouvez faire. 

J'espère que vous avez trouvé cet article intéressant et utile. Si c'est le cas, continuez à en apprendre davantage et essayez d'expérimenter en combinant le score de fonction. Ce sera amusant, je vous le promets.

> Soyez toujours curieux et vous apprendrez quelque chose de nouveau.