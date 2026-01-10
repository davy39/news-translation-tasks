---
title: Comment migrer d'Elasticsearch 1.7 à 6.8 avec zéro temps d'arrêt
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-25T09:45:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-migrate-from-elasticsearch-1-7-to-6-8-with-zero-downtime
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/es-3.png
tags:
- name: availability
  slug: availability
- name: data migration
  slug: data-migration
- name: Devops
  slug: devops
- name: elasticsearch
  slug: elasticsearch
- name: Python
  slug: python
seo_title: Comment migrer d'Elasticsearch 1.7 à 6.8 avec zéro temps d'arrêt
seo_desc: 'By dor sever

  My last task at BigPanda was to upgrade an existing service that was using Elasticsearch
  version 1.7 to a newer Elasticsearch version, 6.8.1.

  In this post, I will share how we migrated from Elasticsearch 1.6 to 6.8 with harsh
  constraints...'
---

Par dor sever

Ma dernière tâche chez [BigPanda](https://www.bigpanda.io) était de mettre à niveau un service existant qui utilisait Elasticsearch version 1.7 vers une version plus récente, 6.8.1.

Dans cet article, je vais partager comment nous avons migré d'Elasticsearch 1.6 à 6.8 avec des contraintes strictes comme zéro temps d'arrêt, aucune perte de données et zéro bug. Je vais également vous fournir un script qui effectue la migration pour vous.

Cet article contient 6 chapitres (et l'un est optionnel) :

* Qu'est-ce que cela m'apporte ? --> Quelles étaient les nouvelles fonctionnalités qui nous ont poussés à mettre à niveau notre version ?
* Les contraintes --> Quelles étaient nos exigences commerciales ?
* Résolution de problèmes --> Comment avons-nous abordé les contraintes ?
* Avancer --> Le plan.
* [Chapitre optionnel] --> Comment avons-nous géré le problème d'explosion de mapping ?
* Enfin --> Comment effectuer la migration des données entre les clusters.

# Chapitre 1 — Qu'est-ce que cela m'apporte ?

Quels avantages attendions-nous en mettant à niveau notre stockage de données ?

Il y avait plusieurs raisons :

1. Problèmes de performance et de stabilité — Nous subissions un grand nombre de pannes avec un MTTR long qui nous causait beaucoup de maux de tête. Cela se traduisait par des latences élevées fréquentes, une utilisation élevée du CPU et d'autres problèmes.
2. Support inexistant dans les anciennes versions d'Elasticsearch — Il nous manquait certaines connaissances opérationnelles dans Elasticsearch, et lorsque nous avons cherché des conseils externes, on nous a encouragés à migrer vers une version plus récente pour recevoir du support.
3. Mappings dynamiques dans notre schéma — Notre schéma actuel dans Elasticsearch 1.7 utilisait une fonctionnalité appelée mappings dynamiques qui faisait exploser notre cluster à plusieurs reprises. Nous voulions donc résoudre ce problème.
4. Mauvaise visibilité sur notre cluster existant — Nous voulions une meilleure vue sous le capot et avons vu que les versions ultérieures avaient de grands outils d'exportation de métriques.

# Chapitre 2 — Les contraintes

* Migration avec ZÉRO temps d'arrêt — Nous avons des utilisateurs actifs sur notre système, et nous ne pouvions pas nous permettre que le système soit indisponible pendant la migration.
* Plan de récupération — Nous ne pouvions pas nous permettre de "perdre" ou "corrompre" des données, peu importe le coût. Nous devions donc préparer un plan de récupération en cas d'échec de notre migration.
* Zéro bug — Nous ne pouvions pas changer la fonctionnalité de recherche existante pour les utilisateurs finaux.

# Chapitre 3 — Résolution de problèmes et élaboration d'un plan

Abordons les contraintes de la plus simple à la plus difficile :

## Zéro bug

Pour répondre à cette exigence, j'ai étudié toutes les requêtes possibles que le service reçoit et leurs sorties. Ensuite, j'ai ajouté des tests unitaires là où c'était nécessaire.

En outre, j'ai ajouté plusieurs métriques (à l'`Elasticsearch Indexer` et au `nouvel Elasticsearch Indexer`) pour suivre la latence, le débit et la performance, ce qui m'a permis de valider que nous les avons uniquement améliorés.

## Plan de récupération

Cela signifie que je devais aborder la situation suivante : j'ai déployé le nouveau code en production et les choses ne fonctionnaient pas comme prévu. Que puis-je faire alors ?

Puisque je travaillais sur un service qui utilisait [l'event-sourcing](https://www.youtube.com/watch?v=STKCRSUsyP0), je pouvais ajouter un autre écouteur (diagramme joint ci-dessous) et commencer à écrire dans un nouveau cluster Elasticsearch sans affecter le statut de production.

## Migration avec zéro temps d'arrêt

Le service actuel est en mode live et ne peut pas être "désactivé" pendant des périodes plus longues que 5 à 10 minutes. Le truc pour réussir cela est le suivant :

* Stocker un journal de toutes les actions que votre service traite (nous utilisons Kafka en production)
* Démarrer le processus de migration hors ligne (et garder une trace de l'offset avant de commencer la migration)
* Lorsque la migration se termine, démarrer le nouveau service contre le journal avec l'offset enregistré et rattraper le retard
* Lorsque le retard est terminé, changer votre frontend pour interroger le nouveau service et vous avez terminé

# Chapitre 4 — Le plan

Notre service actuel utilise l'architecture suivante (basée sur la transmission de messages dans Kafka) :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/indxr2.jpeg)

1. Le `Event topic` contient des événements produits par d'autres applications (par exemple, `UserId 3 créé`)
2. Le `Command topic` contient la traduction de ces événements en commandes spécifiques utilisées par cette application (par exemple : `Ajouter userId 3`)
3. Elasticsearch 1.7 — Le datastore du `command Topic` lu par l'`Elasticsearch Indexer`.

Nous avons prévu d'ajouter un autre consommateur (`nouvel Elasticsearch Indexer`) au `command topic`, qui lira les mêmes messages exacts et les écrira en parallèle dans Elasticsearch 6.8.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/indxr.jpeg)

# Par où commencer ?

Pour être honnête, je me considérais comme un nouvel utilisateur d'Elasticsearch. Pour me sentir confiant pour effectuer cette tâche, j'ai dû réfléchir à la meilleure façon d'aborder ce sujet et de l'apprendre. Voici quelques choses qui m'ont aidé :

1. Documentation — C'est une ressource incroyablement utile pour tout ce qui concerne Elasticsearch. Prenez le temps de la lire et de prendre des notes (ne manquez pas : [Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html) et [QueryDsl](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)).
2. API HTTP — tout ce qui se trouve sous l'API [CAT](https://www.elastic.co/guide/en/elasticsearch/reference/current/cat.html). Cela a été super utile pour déboguer les choses localement et voir comment Elasticsearch répond (ne manquez pas : santé du cluster, indices cat, recherche, supprimer l'index).
3. Métriques (❤️) — Dès le premier jour, nous avons configuré un nouveau tableau de bord avec beaucoup de métriques (prises de [_elasticsearch-exporter-for-Prometheus_](https://github.com/justwatchcom/elasticsearch_exporter)) qui ont aidé et nous ont poussés à comprendre davantage sur Elasticsearch.

# Le code

Notre base de code utilisait une bibliothèque appelée [elastic4s](https://github.com/sksamuel/elastic4s) et utilisait la version la plus ancienne disponible dans la bibliothèque — une très bonne raison de migrer ! La première chose à faire était donc de migrer les versions et de voir ce qui était cassé.

Il existe quelques tactiques pour effectuer cette migration de code. La tactique que nous avons choisie était d'essayer de restaurer la fonctionnalité existante d'abord dans la nouvelle version d'Elasticsearch sans réécrire tout le code depuis le début. En d'autres termes, atteindre la fonctionnalité existante mais sur une version plus récente d'Elasticsearch.

Heureusement pour nous, le code contenait déjà une couverture de test presque complète, ce qui a rendu notre tâche beaucoup plus simple, et cela a pris environ 2 semaines de temps de développement.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/you_need_some_tests_yo.jpg)

_Il est important de noter que, si ce n'avait pas été le cas, nous aurions dû investir du temps pour combler cette couverture. Seulement alors aurions-nous pu migrer puisque l'une de nos contraintes était de ne pas casser la fonctionnalité existante._

# Chapitre 5 — Le problème d'explosion de mapping

Décrivons notre cas d'utilisation plus en détail. Voici notre modèle :

`class InsertMessageCommand(tags: Map[String,String])`

Et par exemple, une instance de ce message serait :

`new InsertMessageCommand(Map("name"->"dor","lastName"->"sever"))`

Et étant donné ce modèle, nous devions supporter les exigences de requête suivantes :

1. Requête par valeur
2. Requête par nom de tag et valeur

La façon dont cela était modélisé dans notre schéma Elasticsearch 1.7 était en utilisant un schéma de modèle dynamique (puisque les clés de tag sont dynamiques et ne peuvent pas être modélisées à l'avance).

Le modèle dynamique nous a causé plusieurs pannes en raison du problème d'explosion de mapping, et le schéma ressemblait à ceci :

```bash
curl -X PUT "localhost:9200/_template/my_template?pretty" -H 'Content-Type: application/json' -d '
{
    "index_patterns": [
        "your-index-names*"
    ],
    "mappings": {
            "_doc": {
                "dynamic_templates": [
                    {
                        "tags": {
                            "mapping": {
                                "type": "text"
                            },
                            "path_match": "actions.tags.*"
                        }
                    }
                ]
            }
        },
    "aliases": {}
}'  

curl -X PUT "localhost:9200/your-index-names-1/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "actions": {
    "tags" : {
        "name": "John",
        "lname" : "Smith"
    }
  }
}
'

curl -X PUT "localhost:9200/your-index-names-1/_doc/2?pretty" -H 'Content-Type: application/json' -d'
{
  "actions": {
    "tags" : {
        "name": "Dor",
        "lname" : "Sever"
  }
}
}
'

curl -X PUT "localhost:9200/your-index-names-1/_doc/3?pretty" -H 'Content-Type: application/json' -d'
{
  "actions": {
    "tags" : {
        "name": "AnotherName",
        "lname" : "AnotherLastName"
  }
}
}
'

```

```bash

curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match" : {
            "actions.tags.name" : {
                "query" : "John"
            }
        }
    }
}
'
# retourne 1 correspondance (doc 1)


curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match" : {
            "actions.tags.lname" : {
                "query" : "John"
            }
        }
    }
}
'
# retourne zéro correspondance

# recherche par valeur
curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "query_string" : {
            "fields": ["actions.tags.*" ],
            "query" : "Dor"
        }
    }
}
'

```

## Solution de documents imbriqués

Notre premier instinct pour résoudre le problème d'explosion de mapping était d'utiliser des documents imbriqués.

Nous avons lu le tutoriel sur le type de données imbriquées dans la documentation Elastic et avons défini le schéma et les requêtes suivants :

```bash
curl -X PUT "localhost:9200/my_index?pretty" -H 'Content-Type: application/json' -d'
{
        "mappings": {
            "_doc": {
            "properties": {
            "tags": {
                "type": "nested" 
                }                
            }
        }
        }
}
'

curl -X PUT "localhost:9200/my_index/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "tags" : [
    {
      "key" : "John",
      "value" :  "Smith"
    },
    {
      "key" : "Alice",
      "value" :  "White"
    }
  ]
}
'


# Requête par clé et valeur de tag
curl -X GET "localhost:9200/my_index/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "nested": {
      "path": "tags",
      "query": {
        "bool": {
          "must": [
            { "match": { "tags.key": "Alice" }},
            { "match": { "tags.value":  "White" }} 
          ]
        }
      }
    }
  }
}
'

# Retourne 1 document


curl -X GET "localhost:9200/my_index/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "nested": {
      "path": "tags",
      "query": {
        "bool": {
          "must": [
            { "match": { "tags.value":  "Smith" }} 
          ]
        }
      }
    }
  }
}
'

# Requête par valeur de tag
# Retourne 1 résultat

```

Et cette solution a fonctionné. Cependant, lorsque nous avons essayé d'insérer des données réelles de clients, nous avons vu que le nombre de documents dans notre index a augmenté d'environ 500 fois.

Nous avons pensé aux problèmes suivants et avons cherché une meilleure solution :

1. Le nombre de documents que nous avions dans notre cluster était d'environ 500 millions de documents. Cela signifiait que, avec le nouveau schéma, nous allions atteindre deux cent cinquante milliards de documents (soit 250 000 000 000 documents ?).
2. Nous avons lu cet excellent article de blog — [https://blog.gojekengineering.com/elasticsearch-the-trouble-with-nested-documents-e97b33b46194](https://blog.gojekengineering.com/elasticsearch-the-trouble-with-nested-documents-e97b33b46194) qui souligne que les documents imbriqués peuvent causer une latence élevée dans les requêtes et des problèmes d'utilisation de la mémoire.
3. Test — Puisque nous convertissions 1 document dans l'ancien cluster en un nombre inconnu de documents dans le nouveau cluster, il aurait été beaucoup plus difficile de suivre si le processus de migration a fonctionné sans aucune perte de données. Si notre conversion était de 1:1, nous aurions pu affirmer que le nombre dans l'ancien cluster était égal au nombre dans le nouveau cluster.

## Éviter les documents imbriqués

Le vrai truc ici était de se concentrer sur les requêtes supportées que nous exécutions : recherche par valeur de tag, et recherche par clé et valeur de tag.

La première requête ne nécessite pas de documents imbriqués puisqu'elle fonctionne sur un seul champ. Pour la seconde, nous avons fait le truc suivant. Nous avons créé un champ qui contient la combinaison de la clé et de la valeur. Chaque fois qu'un utilisateur interroge sur une correspondance clé, valeur, nous traduisons sa requête en texte correspondant et interrogeons ce champ.

Exemple :

```bash
curl -X PUT "localhost:9200/my_index_2?pretty" -H 'Content-Type: application/json' -d'
{
    "mappings": {
        "_doc": {
            "properties": {
                "tags": {
                    "type": "object",
                    "properties": {
                        "keyToValue": {
                            "type": "keyword"
                        },
                        "value": {
                            "type": "keyword"
                        }
                    }
                }
            }
        }
    }
}
'


curl -X PUT "localhost:9200/my_index_2/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "tags" : [
    {
      "keyToValue" : "John:Smith",
      "value" : "Smith"
    },
    {
      "keyToValue" : "Alice:White",
      "value" : "White"
    }
  ]
}
'

# Requête par clé, valeur
# L'utilisateur interroge pour la clé : Alice, et la valeur : White, nous interrogeons ensuite elastic avec cette requête :

curl -X GET "localhost:9200/my_index_2/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
        "bool": {
          "must": [ { "match": { "tags.keyToValue": "Alice:White" }}]
  }}}
'

# Requête par valeur uniquement
curl -X GET "localhost:9200/my_index_2/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
        "bool": {
          "must": [ { "match": { "tags.value": "White" }}]
  }}}
'

```

# Chapitre 6 — Le processus de migration

Nous avons prévu de migrer environ 500 millions de documents avec zéro temps d'arrêt. Pour cela, nous avions besoin :

1. D'une stratégie sur la façon de transférer les données de l'ancien Elasticsearch vers le nouveau Elasticsearch
2. D'une stratégie sur la façon de combler le retard entre le début de la migration et la fin de celle-ci

Et nos deux options pour combler le retard :

1. Notre système de messagerie est basé sur Kafka. Nous aurions pu simplement prendre l'offset actuel avant le début de la migration, et après la fin de la migration, commencer à consommer à partir de cet offset spécifique. Cette solution nécessite quelques ajustements manuels des offsets et d'autres choses, mais elle fonctionnera.
2. Une autre approche pour résoudre ce problème était de commencer à consommer les messages depuis le début du topic dans Kafka et de rendre nos actions sur Elasticsearch idempotentes — c'est-à-dire, si le changement était déjà "appliqué", rien ne changerait dans le stockage Elastic.

Les requêtes faites par notre service contre Elastic étaient déjà idempotentes, donc nous avons choisi l'option 2 car elle ne nécessitait aucun travail manuel (pas besoin de prendre des offsets spécifiques, puis de les définir ensuite dans un nouveau groupe de consommateurs).

## Comment pouvons-nous migrer les données ?

Voici les options que nous avons envisagées :

1. Si notre Kafka contenait tous les messages depuis le début, nous aurions pu simplement jouer depuis le début et l'état final serait égal. Mais puisque nous appliquons une rétention à nos topics, ce n'était pas une option.
2. Dump des messages sur disque puis les ingérer directement dans Elastic — Cette solution semblait un peu étrange. Pourquoi les stocker sur disque au lieu de les écrire directement dans Elastic ?
3. Transférer les messages entre l'ancien Elasticsearch et le nouveau Elasticsearch — Cela signifiait écrire une sorte de "script" (quelqu'un a dit Python ? ?) qui se connecterait à l'ancien cluster Elasticsearch, interrogerait les éléments, les transformerait dans le nouveau schéma et les indexerait dans le cluster.

Nous avons choisi la dernière option. Voici les choix de conception que nous avions en tête :

1. N'essayons pas de penser à la gestion des erreurs à moins que nous en ayons besoin. Essayons d'écrire quelque chose de super simple, et si des erreurs se produisent, essayons de les résoudre. En fin de compte, nous n'avons pas eu besoin de résoudre ce problème puisque aucune erreur ne s'est produite pendant la migration.
2. C'est une opération ponctuelle, donc tout ce qui fonctionne en premier / KISS.
3. Métriques — Puisque les processus de migration peuvent prendre des heures à des jours, nous voulions dès le premier jour avoir la capacité de surveiller le nombre d'erreurs et de suivre la progression actuelle et le taux de copie du script.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/python.gif)

Nous avons longuement réfléchi et choisi Python comme notre arme de choix. La version finale du code est ci-dessous :

```yml
dictor==0.1.2 - pour copier et transformer nos documents Elasticsearchelasticsearch==1.9.0 - pour se connecter à l'ancien Elasticsearchelasticsearch6==6.4.2 - pour se connecter au nouvel Elasticsearchstatsd==3.3.0 - pour rapporter les métriques
```

```python
from elasticsearch import Elasticsearch
from elasticsearch6 import Elasticsearch as Elasticsearch6
import sys
from elasticsearch.helpers import scan
from elasticsearch6.helpers import parallel_bulk
import statsd

ES_SOURCE = Elasticsearch(sys.argv[1])
ES_TARGET = Elasticsearch6(sys.argv[2])
INDEX_SOURCE = sys.argv[3]
INDEX_TARGET = sys.argv[4]
QUERY_MATCH_ALL = {"query": {"match_all": {}}}
SCAN_SIZE = 1000
SCAN_REQUEST_TIMEOUT = '3m'
REQUEST_TIMEOUT = 180
MAX_CHUNK_BYTES = 15 * 1024 * 1024
RAISE_ON_ERROR = False


def transform_item(item, index_target):
    # implémentez votre logique de transformation ici
    transformed_source_doc = item.get("_source")
    return {"_index": index_target,
            "_type": "_doc",
            "_id": item['_id'],
            "_source": transformed_source_doc}


def transformedStream(es_source, match_query, index_source, index_target, transform_logic_func):
    for item in scan(es_source, query=match_query, index=index_source, size=SCAN_SIZE,
                     timeout=SCAN_REQUEST_TIMEOUT):
        yield transform_logic_func(item, index_target)


def index_source_to_target(es_source, es_target, match_query, index_source, index_target, bulk_size, statsd_client,
                           logger, transform_logic_func):
    ok_count = 0
    fail_count = 0
    count_response = es_source.count(index=index_source, body=match_query)
    count_result = count_response['count']
    statsd_client.gauge(stat='elastic_migration_document_total_count,index={0},type=success'.format(index_target),
                        value=count_result)
    with statsd_client.timer('elastic_migration_time_ms,index={0}'.format(index_target)):
        actions_stream = transformedStream(es_source, match_query, index_source, index_target, transform_logic_func)
        for (ok, item) in parallel_bulk(es_target,
                                        chunk_size=bulk_size,
                                        max_chunk_bytes=MAX_CHUNK_BYTES,
                                        actions=actions_stream,
                                        request_timeout=REQUEST_TIMEOUT,
                                        raise_on_error=RAISE_ON_ERROR):
            if not ok:
                logger.error("got error on index {} which is : {}".format(index_target, item))
                fail_count += 1
                statsd_client.incr('elastic_migration_document_count,index={0},type=failure'.format(index_target),
                                   1)
            else:
                ok_count += 1
                statsd_client.incr('elastic_migration_document_count,index={0},type=success'.format(index_target),
                                   1)

    return ok_count, fail_count


statsd_client = statsd.StatsClient(host='localhost', port=8125)

if __name__ == "__main__":
    index_source_to_target(ES_SOURCE, ES_TARGET, QUERY_MATCH_ALL, INDEX_SOURCE, INDEX_TARGET, BULK_SIZE,
                           statsd_client, transform_item)

```

# Conclusion

Migrer des données dans un système de production en direct est une tâche compliquée qui nécessite beaucoup d'attention et de planification minutieuse. Je recommande de prendre le temps de travailler à travers les étapes énumérées ci-dessus et de déterminer ce qui fonctionne le mieux pour vos besoins.

En règle générale, essayez toujours de réduire vos exigences autant que possible. Par exemple, une migration avec zéro temps d'arrêt est-elle nécessaire ? Pouvez-vous vous permettre une perte de données ?

![Image](https://www.freecodecamp.org/news/content/images/2019/12/enjoy-the-ride.gif)

La mise à niveau des magasins de données est généralement un marathon et non un sprint, alors prenez une profonde inspiration et essayez de profiter du voyage.

* L'ensemble du processus énuméré ci-dessus m'a pris environ 4 mois de travail
* Tous les exemples Elasticsearch qui apparaissent dans cet article ont été testés contre la version 6.8.1