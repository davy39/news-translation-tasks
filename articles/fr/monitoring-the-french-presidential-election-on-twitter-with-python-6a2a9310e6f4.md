---
title: Surveillance de l'élection présidentielle française sur Twitter avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-12T09:19:26.000Z'
originalURL: https://freecodecamp.org/news/monitoring-the-french-presidential-election-on-twitter-with-python-6a2a9310e6f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gm6Q_bRGS6yJWRuESpPx5w.png
tags:
- name: Neo4j
  slug: neo4j
- name: politics
  slug: politics
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Surveillance de l'élection présidentielle française sur Twitter avec Python
seo_desc: 'By Romain Thalineau

  A while ago I read this nice article from Laurent Luce where he explained how he
  implemented a system that collected the tweets related to the 2012 French presidential
  election. The article is very well written, and I highly recom...'
---

Par Romain Thalineau

Il y a quelque temps, j'ai lu [cet excellent article](http://www.laurentluce.com/posts/python-twitter-statistics-and-the-2012-french-presidential-election/) de Laurent Luce où il expliquait comment il avait implémenté un système qui collectait les tweets liés à l'élection présidentielle française de 2012. L'article est très bien écrit, et je vous recommande vivement de le lire.

Cela m'a donné l'idée d'implémenter quelque chose de similaire pour l'élection de 2017. Mais je voulais ajouter quelques fonctionnalités :

* Au lieu d'utiliser une base de données SQL pour stocker les données, je voulais utiliser une base de données de graphes. La raison principale était d'expérimenter avec un tel système, mais il est assez facile de voir comment cela convient bien aux données des réseaux sociaux.
* Je voulais pouvoir surveiller les données en temps réel. En pratique, cela signifie que les données doivent être traitées dès leur arrivée. Cela impliquerait également de servir les données analysées à un site web avec des visualisations de données.
* Idéalement, je voulais effectuer une analyse de sentiment sur les tweets. J'entraînerais un algorithme d'apprentissage et je l'implémenterais le long du pipeline de données pour servir ses résultats en temps réel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y9G8AIt2rJnWwhjdv_Zn0w.png)
_[Analyse des séries temporelles](https://www.auguratech.com/#/twitter/time_series" rel="noopener" target="_blank" title=")_

Eh bien, j'ai réussi à construire tout cela. Vous pouvez voir à quoi cela ressemble sur [mon site personnel](https://www.auguratech.com/#/twitter). Jusqu'à présent, il y a deux analyses simples :

* [La première](https://www.auguratech.com/#/twitter/time_series) est une analyse de séries temporelles, qui montre le nombre de tweets par candidat en fonction de la date. En plus de pouvoir sélectionner la date de début/fin et la période, vous pouvez également afficher uniquement les candidats que vous souhaitez voir en cliquant sur leurs noms dans la visualisation.
* [La deuxième analyse](https://www.auguratech.com/#/twitter/geospatial) affiche la géolocalisation des tweets. Les options sont relativement similaires à la première analyse.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G8iD7P81--DVJf1NTDTmbA.png)
_[Analyse de la géolocalisation des tweets](https://www.auguratech.com/#/twitter/geospatial" rel="noopener" target="_blank" title=")_

Pour collecter les données de Twitter, j'ai utilisé une approche similaire à celle de Laurent Luce. Au lieu de me concentrer sur les similitudes, je vais vous montrer les approches que j'ai prises et qui étaient différentes.

#### Stocker les tweets dans une base de données de graphes

Comme je l'ai dit, je voulais stocker les données dans une base de données de graphes. J'ai choisi d'utiliser [Neo4J](https://neo4j.com/). Dans une base de données de graphes, les données sont modélisées à l'aide d'une combinaison de structures de nœuds, d'arêtes et de propriétés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XlHtECBpilVo7Jk7ujcCbA.png)
_[Crédit image](http://network.graphdemos.com/" rel="noopener" target="_blank" title=")_

Dans notre cas, les nœuds peuvent représenter un tweet, un utilisateur ou même un hashtag. Ils peuvent être distingués en utilisant une étiquette. La relation entre les nœuds est gérée en les connectant à travers des arêtes. Par exemple, un nœud utilisateur peut être connecté à un nœud tweet via une relation POSTS.

Les relations sont directionnelles. Un tweet ne peut pas POST un utilisateur, mais il peut MENTIONNER un utilisateur.

Enfin, les nœuds et les arêtes (relations) peuvent tous deux contenir des propriétés. Par exemple, un utilisateur a un nom et un tweet a du texte.

Lors de l'interaction avec une base de données de graphes, les Object Graph Mapper (OGM) sont particulièrement utiles. Dans ce projet, j'ai utilisé [Neomodel](https://github.com/robinedwards/neomodel). Il expose une API relativement similaire à l'API des modèles Django. Vous définissez vos modèles comme suit :

Comme vous pouvez le voir, les propriétés et les relations sont définies. Je vous invite à vérifier le fichier des modèles dans [mon dépôt github](https://github.com/romaintha/twitter/blob/master/twitter/models.py) pour voir la définition complète du modèle de données.

Neo4J étant une base de données NoSQL, elle utilise un langage de requête non-SQL appelé Cypher. C'est un langage assez simple. Par exemple, la requête suivante retournera tous les tweets postés par un utilisateur qui contiennent le mot "fillon" (l'un des candidats) :

```
MATCH (u:User)-[:POSTS]->(t:Tweet) WHERE t.text contains "fillon" return t
```

Neomodel étant un OGM, il fournit une API afin que vous n'ayez pas à écrire beaucoup de requêtes manuellement. Vous pouvez obtenir les mêmes résultats que ci-dessus en exécutant :

```
Tweet.nodes.filter(text__contains="fillon")
```

#### Streaming depuis Twitter

Twitter propose deux façons d'obtenir leurs données. La première est via une API REST standard. Chaque accès à un endpoint est limité, donc ce n'est pas la solution préférée dans notre cas.

Heureusement, Twitter propose également une API de streaming. En définissant un filtre, nous pouvons recevoir tous les tweets qui passent ce filtre (avec une limite de 1% du nombre global de tweets publiés à l'instant t). La bibliothèque [Tweepy](https://github.com/tweepy/tweepy) facilite ce processus.

Comme vous pouvez le voir dans [mon dépôt](https://github.com/romaintha/twitter/blob/master/twitter/streaming_api.py), vous devez définir une classe Listener, qui déclenchera certaines actions pendant le streaming. Par exemple, la méthode "on_status" est appelée chaque fois qu'un tweet est streamé.

En outre, j'ai défini une classe Streaming dont les responsabilités sont de s'authentifier auprès de Twitter, d'instancier un stream Tweepy avec le Listener ci-dessus, et d'exposer une méthode pour démarrer le streaming. La méthode "start_streaming" accepte un argument "to_track", qui est une liste de mots sur lesquels vous souhaitez filtrer.

Vous devez instancier la classe Streaming avec un ensemble d'arguments. En plus des identifiants de l'API Twitter, vous avez besoin des arguments "pipeline" et "batch_size". Ce dernier est un nombre spécifiant la quantité de tweets qui sont traités à la fois.

Étant donné que le traitement d'un tweet implique de le sauvegarder dans Neo4J, le faire un par un est une opération très coûteuse. Les sauvegarder par lots de 100 (ou même plus dans certains cas) améliore considérablement les performances.

L'argument "pipeline" doit être une référence à une fonction, qui recevra le lot de tweets. À l'intérieur de celle-ci, vous êtes libre de faire ce que vous voulez. J'ai fourni un exemple dans le module [utils.py](https://github.com/romaintha/twitter/blob/master/twitter/utils.py).

Comme vous pouvez le voir, cette fonction fait un appel à une tâche Celery asynchrone définie dans le module [tasks.py](https://github.com/romaintha/twitter/blob/master/twitter/tasks.py). [Celery](http://www.celeryproject.org/) est une bibliothèque de file d'attente de tâches distribuées Python. Je l'ai utilisé avec [RabbitMQ](https://www.rabbitmq.com/) comme courtier de messages. Alors, comment cela fonctionne-t-il ? Revenons à la fonction "streaming_pipeline" dans le module [utils.py](https://github.com/romaintha/twitter/blob/master/twitter/utils.py), et concentrons-nous sur cette ligne :

```
bulk_parsing.delay(users_attributes, tweets_attributes)
```

Lorsque cette ligne est traitée, au lieu de traiter la fonction "bulk_parsing" de manière synchrone, un message sera publié vers un courtier (ici RabbitMQ). Cela permet aux consommateurs (workers) de récupérer ces messages, et donc de traiter la tâche "bulk_parsing" de manière asynchrone et en parallèle. Pourquoi ? Parce que cela permet une mise à l'échelle horizontale du traitement des tweets. Si les messages s'accumulent plus vite que vous ne pouvez les traiter, vous pouvez ajouter plus de workers pour aider à les consommer.

Une dernière remarque. Je voulais que le processus soit aussi polyvalent que possible, dans le sens où si le traitement devait être changé — ou si quelque chose devait être ajouté — cela doit être facile à faire. Dans ce cas, je peux simplement changer la fonction "streaming_pipeline" et ajouter quelques tâches asynchrones. C'est rapide et facile à modifier.

Merci d'avoir lu !

* Assurez-vous de vérifier le code [dans mon dépôt Github](https://github.com/romaintha/twitter).
* Vous pouvez voir tout cela en action [sur mon site](http://network.graphdemos.com/), où je l'ai utilisé pour alimenter certaines analyses.