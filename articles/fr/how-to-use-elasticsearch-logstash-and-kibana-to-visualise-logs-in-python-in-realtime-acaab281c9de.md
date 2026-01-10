---
title: Comment utiliser Elasticsearch, Logstash et Kibana pour visualiser les logs
  en Python en temps réel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T17:04:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-elasticsearch-logstash-and-kibana-to-visualise-logs-in-python-in-realtime-acaab281c9de
coverImage: https://cdn-media-1.freecodecamp.org/images/0*-sOdBVARaJLNvu17.png
tags:
- name: logging
  slug: logging
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment utiliser Elasticsearch, Logstash et Kibana pour visualiser les
  logs en Python en temps réel
seo_desc: 'By Ritvik Khanna

  What is logging?

  Let’s say you are developing a software product. It works remotely, interacts with
  different devices, collects data from sensors and provides a service to the user.
  One day, something goes wrong and the system is not...'
---

Par Ritvik Khanna

### Qu'est-ce que le logging ?

Imaginons que vous développez un produit logiciel. Il fonctionne à distance, interagit avec différents appareils, collecte des données à partir de capteurs et fournit un service à l'utilisateur. Un jour, quelque chose ne va pas et le système ne fonctionne pas comme prévu. Il se peut qu'il ne reconnaisse pas les appareils ou qu'il ne reçoive aucune donnée des capteurs, ou qu'il ait simplement rencontré une erreur d'exécution due à un bug dans le code. Comment pouvez-vous en être sûr ?

Maintenant, imaginez s'il y avait des points de contrôle dans le code du système où, si le système retourne un résultat inattendu, il le signale simplement et notifie le développeur. C'est le concept de logging.

Le logging permet aux développeurs de comprendre ce que le code fait réellement et comment se déroule le flux de travail. Une grande partie de la vie des développeurs de logiciels consiste à surveiller, résoudre des problèmes et déboguer. Le logging rend ce processus beaucoup plus facile et fluide.

### Visualisation des logs

![Image](https://cdn-media-1.freecodecamp.org/images/0*-sOdBVARaJLNvu17.png)
_[source](https://www.datalabsagency.com/wp-content/uploads/2014/11/Interactive-Data-Visualisation-Service.png" rel="noopener" target="_blank" title=")_

Maintenant, si vous êtes un développeur expert qui développe et crée des logiciels depuis un certain temps, vous pourriez penser que le logging n'est pas un gros problème et que la plupart de notre code est inclus avec une instruction `**Debug.Log('____')**`. C'est bien, mais il y a d'autres aspects du logging que nous pouvons utiliser.

La visualisation de données spécifiques loguées présente les avantages suivants :

* Surveiller les opérations du système à distance.
* Communiquer des informations clairement et efficacement via des graphiques statistiques, des tracés et des infographies.
* Extraire des connaissances à partir des données visualisées sous forme de différents graphiques.
* Prendre les mesures nécessaires pour améliorer le système.

Il existe de nombreuses façons de visualiser des données brutes. Il existe de nombreuses bibliothèques dans les langages de programmation Python et R qui peuvent aider à tracer des graphiques. Vous pouvez en apprendre davantage à ce sujet [**ici**](https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f). Mais dans cet article, je ne vais pas discuter des méthodes mentionnées ci-dessus. Avez-vous déjà entendu parler de la [**pile ELK**](https://www.elastic.co/elk-stack) ?

### Pile ELK

E — [**Elasticsearch**](https://www.elastic.co/products/elasticsearch), L — [**Logstash**](https://www.elastic.co/products/logstash)**,** K — [**Kibana**](https://www.elastic.co/products/kibana)

Permettez-moi de vous donner une brève introduction. La pile ELK est une collection de trois logiciels open source qui aident à fournir des informations en temps réel sur des données qui peuvent être structurées ou non structurées. On peut rechercher et analyser des données en utilisant ses outils avec une grande facilité et efficacité.

[**Elasticsearch**](https://www.elastic.co/products/elasticsearch) est un moteur de recherche et d'analyse distribué, RESTful, capable de résoudre un nombre croissant de cas d'utilisation. Au cœur de la pile Elastic, il stocke centralement vos données afin que vous puissiez découvrir l'attendu et découvrir l'inattendu. Elasticsearch vous permet d'effectuer et de combiner de nombreux types de recherches — structurées, non structurées, géo, métriques, etc. Il est construit sur le langage de programmation Java, ce qui permet à Elasticsearch de s'exécuter sur différentes plateformes. Il permet aux utilisateurs d'explorer de très grandes quantités de données à très haute vitesse.

[**Logstash**](https://www.elastic.co/products/logstash) est un pipeline de traitement de données côté serveur, open source, qui ingère des données à partir de multiples sources simultanément, les transforme, puis les envoie à votre "stash" préféré (comme Elasticsearch). Les données sont souvent dispersées ou cloisonnées dans de nombreux systèmes sous de nombreux formats. Logstash prend en charge une variété d'entrées qui récupèrent des événements à partir de nombreuses sources courantes, toutes en même temps. Ingestez facilement à partir de vos logs, métriques, applications web, magasins de données et divers services AWS, le tout en continu, en flux continu. Logstash dispose d'un framework pluggable avec plus de 200 plugins. Mélangez, associez et orchestrez différentes entrées, filtres et sorties pour travailler en harmonie dans le pipeline.

[**Kibana**](https://www.elastic.co/products/kibana) est une plateforme d'analyse et de visualisation open source conçue pour fonctionner avec Elasticsearch. Vous utilisez Kibana pour rechercher, visualiser et interagir avec les données stockées dans les index Elasticsearch. Vous pouvez facilement effectuer des analyses de données avancées et visualiser vos données sous forme de divers graphiques, tableaux et cartes. Kibana facilite la compréhension de grandes quantités de données. Son interface simple, basée sur un navigateur, vous permet de créer et de partager rapidement des tableaux de bord dynamiques qui affichent les modifications des requêtes Elasticsearch en temps réel.

Pour avoir une meilleure idée du flux de travail de la manière dont les trois logiciels interagissent les uns avec les autres, reportez-vous au diagramme suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OHP01Lidop3GQZbnwg9s4Q.jpeg)
_[source](http://Howtodoinjava.com" rel="noopener" target="_blank" title=")_

### Implémentation

#### Logging en Python

Ici, j'ai choisi d'expliquer l'implémentation du logging en Python car c'est le langage le plus utilisé pour les projets impliquant la communication entre plusieurs machines et l'internet des objets. Cela vous aidera à avoir une idée générale de son fonctionnement.

Python fournit un système de logging dans le cadre de sa bibliothèque standard, vous pouvez donc rapidement ajouter du logging à votre application.

```py
import logging
```

En Python, le logging peut être effectué à 5 niveaux différents qui indiquent chacun le type d'événement. Ils sont les suivants :

* **Info** — Désigne des messages informatifs qui mettent en évidence la progression de l'application à un niveau granulaire.
* **Debug** — Désigne des événements informatifs à grain fin qui sont les plus utiles pour déboguer une application.
* **Warning** — Désigne des situations potentiellement dangereuses.
* **Error** — Désigne des événements d'erreur qui peuvent encore permettre à l'application de continuer à fonctionner.
* **Critical** — Désigne des événements d'erreur très graves qui entraîneront probablement l'arrêt de l'application.

Par conséquent, en fonction du problème qui doit être logué, nous utilisons le niveau défini en conséquence.

> **Note** : Info et Debug ne sont pas logués par défaut, car seuls les logs de niveau Warning et au-dessus sont logués.

Maintenant, pour donner un exemple et créer un ensemble d'instructions de log à visualiser, j'ai créé un script Python qui logue des instructions de format spécifique et un message.

```py
import logging
import random

logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
for i in xrange(0,15):
    x=random.randint(0,2)
    if(x==0):
        logging.warning('Log Message')
    elif(x==1):
        logging.critical('Log Message')
    else:
        logging.error('Log Message')
```

Ici, les instructions de log seront ajoutées à un fichier nommé _logFile.txt_ dans le format spécifié. J'ai exécuté le script pendant trois jours à différents intervalles de temps, créant un fichier contenant des logs aléatoires comme ci-dessous :

```
2019-01-09 09:01:05,333 ERROR-Log Message
2019-01-09 09:01:05,333 WARNING-Log Message
2019-01-09 09:01:05,333 ERROR-Log Message
2019-01-09 09:01:05,333 CRITICAL-Log Message
2019-01-09 09:01:05,333 WARNING-Log Message
2019-01-09 09:01:05,333 ERROR-Log Message
2019-01-09 09:01:05,333 ERROR-Log Message
2019-01-09 09:01:05,333 WARNING-Log Message
2019-01-09 09:01:05,333 WARNING-Log Message
2019-01-09 09:01:05,333 ERROR-Log Message
2019-01-09 09:01:05,333 CRITICAL-Log Message
2019-01-09 09:01:05,333 CRITICAL-Log Message
2019-01-09 09:01:05,333 CRITICAL-Log Message
2019-01-09 11:07:05,333 ERROR-Log Message
2019-01-09 11:07:05,333 WARNING-Log Message
2019-01-09 11:07:05,333 ERROR-Log Message
2019-01-09 11:07:05,333 ERROR-Log Message
2019-01-09 11:07:05,333 WARNING-Log Message
2019-01-09 11:07:05,333 CRITICAL-Log Message
2019-01-09 11:07:05,333 WARNING-Log Message
2019-01-09 11:07:05,333 ERROR-Log Message
```

#### Installation d'Elasticsearch, Logstash et Kibana

Tout d'abord, téléchargeons les trois logiciels open source depuis leurs liens respectifs [[elasticsearch](https://www.elastic.co/downloads/elasticsearch)],[[logstash](https://www.elastic.co/downloads/logstash)]et[[kibana](https://www.elastic.co/downloads/kibana)]. Décompressez les fichiers et placez les trois dans le dossier du projet.

Commençons.

**Étape 1** — Installez Kibana et Elasticsearch sur le système local. Nous exécutons Kibana avec la commande suivante dans le dossier bin de Kibana.

```bash
bin\kibana
```

De même, Elasticsearch est installé comme suit :

```bash
bin\elasticsearch
```

Maintenant, dans les deux terminaux séparés, nous pouvons voir les deux modules en cours d'exécution. Pour vérifier que les services sont en cours d'exécution, ouvrez **localhost:5621** et **localhost:9600**_._

Après que les deux services sont en cours d'exécution, nous utilisons Logstash et des programmes Python pour analyser les données de log brutes et les transmettre à Elasticsearch à partir duquel Kibana interroge les données.

**Étape 2**— Passons maintenant à Logstash. Avant de démarrer Logstash, un fichier de configuration Logstash est créé dans lequel les détails du fichier d'entrée, de l'emplacement de sortie et des méthodes de filtrage sont spécifiés.

```
input{
 file{
 path => "full/path/to/log_file/location/logFile.txt"
 start_position => "beginning"
 }
}
filter
{
 grok{
 match => {"message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:log-level}-%{GREEDYDATA:message}"}
 }
    date {
    match => ["timestamp", "ISO8601"]
  }
}
output{
 elasticsearch{
 hosts => ["localhost:9200"]
 index => "index_name"}
stdout{codec => rubydebug}
}
```

Ce fichier de configuration joue un rôle majeur dans la pile ELK. Regardez la ligne **filter{grok{}}**. Il s'agit d'un plugin de filtre Grok. Grok est un excellent moyen d'analyser les données de log non structurées en quelque chose de structuré et interrogeable. Cet outil est parfait pour les logs syslog, apache et autres logs de serveurs web, les logs mysql, et en général, tout format de log qui est généralement écrit pour les humains et non pour la consommation par ordinateur. Ce motif grok mentionné dans le code indique à Logstash comment analyser chaque entrée de ligne dans notre fichier de log.

Maintenant, enregistrez le fichier dans le dossier Logstash et démarrez le service Logstash.

```bash
bin\logstash -f logstash-simple.conf
```

> Pour en savoir plus sur la configuration de logstash, cliquez [[**ici**](https://www.elastic.co/guide/en/logstash/current/configuration.html)].

**Étape 3** — Après cela, les données analysées à partir des fichiers de log seront disponibles dans la gestion de Kibana à **localhost:5621** pour créer différentes visualisations et tableaux de bord. Pour vérifier si Kibana reçoit des données, dans l'onglet de gestion de Kibana, exécutez la commande suivante :

```bash
localhost:9200/_cat/indices?v
```

Cela affichera tous les index. Pour chaque visualisation, un nouveau motif d'index doit être sélectionné à partir des outils de développement, après quoi diverses techniques de visualisation sont utilisées pour créer un tableau de bord.

#### Tableau de bord utilisant Kibana

Après avoir tout configuré, il est maintenant temps de créer des graphiques afin de visualiser les données de log.

Après avoir ouvert la page d'accueil de gestion de Kibana, on nous demandera de créer un nouveau motif d'index. Entrez `index_name*` dans le champ **Index pattern** et sélectionnez **@timestamp** dans le menu déroulant **Time Filter field** name.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vgcx_wyDnpKiHuQNQZn_pw.png)

Maintenant, pour créer des graphiques, nous allons dans l'onglet **Visualize**.

Sélectionnez une nouvelle visualisation, choisissez un type de graphique et un nom d'index, et en fonction de vos exigences d'axe, créez un graphique. Nous pouvons créer un histogramme avec l'**axe y** comme **count** et l'**axe x** avec le **mot-clé log-level** ou le **timestamp**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yt0dS1APsC5DRb33SkcDYA.gif)
_Création d'un graphique_

Après avoir créé quelques graphiques, nous pouvons ajouter toutes les visualisations requises et créer un **Tableau de bord**, comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sLN0wwMyVaK0YtWB3aI8TQ.png)

> Note — Chaque fois que les logs dans le fichier de log sont mis à jour ou ajoutés aux logs précédents, tant que les trois services sont en cours d'exécution, les données dans Elasticsearch et les graphiques dans Kibana seront automatiquement mis à jour selon les nouvelles données.

#### Conclusion

Le logging peut être une aide pour lutter contre les erreurs et déboguer les programmes au lieu d'utiliser une instruction print. Le module de logging divise les messages selon différents niveaux. Cela permet une meilleure compréhension du code et du flux d'appel sans interrompre le programme.

La visualisation des données est une étape nécessaire dans les situations où une énorme quantité de données est générée chaque instant. Les outils et techniques de visualisation de données offrent aux cadres et autres travailleurs du savoir de nouvelles approches pour améliorer considérablement leur capacité à saisir les informations cachées dans leurs données. L'identification rapide des logs d'erreurs, la compréhension facile des données et les visualisations de données hautement personnalisables sont quelques-uns des avantages. C'est l'une des méthodes les plus constructives pour organiser les données brutes.

> Pour plus de références, vous pouvez consulter la documentation officielle ELK à partir d'ici — [https://www.elastic.co/learn](https://www.elastic.co/learn) et sur le logging en Python — [https://docs.python.org/2/library/logging.html](https://docs.python.org/2/library/logging.html)