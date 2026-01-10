---
title: Comment simplifier l'analyse des logs des conteneurs Docker avec Elastic Stack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T06:25:00.000Z'
originalURL: https://freecodecamp.org/news/docker-container-log-analysis-with-elastic-stack-53d5ec9e5953
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ytyp7c9adYtnLbTUqDl-DA.png
tags:
- name: coding
  slug: coding
- name: Docker
  slug: docker
- name: elasticsearch
  slug: elasticsearch
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Comment simplifier l'analyse des logs des conteneurs Docker avec Elastic
  Stack
seo_desc: 'By Ravindu Fernando

  Logging is an essential component within any application. Logs enable you to analyze
  and sneak a peak into what’s happening within your application code like a story.
  Software developers spend a large part of their day to day live...'
---

Par Ravindu Fernando

La journalisation est un composant essentiel au sein de toute application. Les logs vous permettent d'analyser et de jeter un coup d'œil à ce qui se passe dans votre code d'application comme une histoire. Les développeurs logiciels passent une grande partie de leur vie quotidienne à surveiller, dépanner et déboguer des applications, ce qui peut parfois être un cauchemar. La journalisation permet aux développeurs logiciels de rendre ce processus mouvementé beaucoup plus facile et fluide.

![Image](https://cdn-media-1.freecodecamp.org/images/EMv0ZRmR82v5oUZ4ZNllx29LNYgqZoUwjua-)

Si vous avez conteneurisé votre application avec une plateforme de conteneurs comme Docker, vous êtes peut-être familier avec **_docker logs_** qui vous permet de voir les logs créés dans votre application s'exécutant à l'intérieur de votre conteneur Docker. Pourquoi alors penser à Elastic Stack pour analyser vos logs ? Eh bien, il y a principalement deux problèmes brûlants ici :

* Imaginez que vous avez des dizaines, des centaines, voire des milliers de conteneurs générant des logs — se connecter en SSH à tous ces serveurs et extraire les logs ne fonctionnera pas bien.
* De plus, les conteneurs sont immuables et éphémères, ce qui signifie qu'ils ont une durée de vie plus courte. Donc, une fois que vos conteneurs ont disparu et sont remplacés par de nouveaux conteneurs, tous vos logs d'application liés aux anciens conteneurs sont perdus.

La solution ultime à cela est donc de créer un composant de journalisation centralisé pour collecter tous vos logs de conteneurs en un seul endroit. C'est là qu'intervient Elastic Stack.

[Elastic Stack](https://www.elastic.co/products/) se compose principalement de quatre composants majeurs :

* **Beats** est le nouveau membre qui a fait passer la pile ELK à Elastic Stack. Les Beats sont des expéditeurs de données de logs légers qui peuvent pousser les logs vers la pile ELK. Pour cet article, j'utiliserai Filebeats, un membre de la famille Beats, qui offre un moyen léger de collecter, transférer et centraliser les logs et les fichiers.
* **Logstash** est un composant qui agrège, modifie et transfère les logs de plusieurs emplacements d'entrée vers Elasticsearch.
* **Elasticsearch** est un moteur de recherche et d'analyse distribué, basé sur JSON, qui stocke et indexe les données (les entrées de log dans ce cas) de manière scalable et gérable.
* **Kibana** est une interface utilisateur enrichie pour analyser et accéder facilement aux données dans Elasticsearch.

Dans cet article, nous allons voir comment utiliser les composants mentionnés ci-dessus et implémenter un analyseur de logs centralisé pour collecter et extraire les logs des conteneurs Docker.

Pour les besoins de cet article, j'ai utilisé deux instances AWS EC2 t2.small, exécutant Ubuntu 18.04 avec Docker et Docker Compose installés. L'instance 1 exécute une application web Tomcat et l'instance 2 exécute la pile ELK (Elasticsearch, Logstash, Kibana).

Dans Linux, par défaut, les logs Docker peuvent être trouvés à cet emplacement :
**_/var/lib/docker/containers/<container-id>/<container-id&_**gt;-json.log

Tous les logs Docker seront collectés via Filebeat s'exécutant à l'intérieur de la machine hôte en tant que conteneur. Filebeat sera installé sur chaque machine hôte Docker (nous utiliserons un fichier Docker Filebeat personnalisé et une unité systemd pour cela, ce qui sera expliqué dans la section Configurer Filebeat.)

Notre application web Tomcat écrira les logs à l'emplacement ci-dessus en utilisant le pilote de journalisation Docker par défaut. Filebeat extraira ensuite les logs de cet emplacement et les poussera vers Logstash.

Une autre chose importante à noter est que, outre les logs générés par l'application, nous avons également besoin des métadonnées associées aux conteneurs, telles que le nom du conteneur, l'image, les tags, l'hôte, etc. Cela nous permettra d'identifier spécifiquement l'hôte exact et le conteneur générant les logs. Ces données peuvent également être envoyées facilement par Filebeat avec les entrées de log de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/A1VVz9CNOB6-hJSBisBPdHQflklU7eHXAUyQ)
_Architecture de haut niveau — Instance 1 [Gauche] | Instance 2 [Droite]_

En faisant ce type d'implémentation, les conteneurs en cours d'exécution n'ont pas à se soucier du pilote de journalisation, de la manière dont les logs sont collectés et poussés. Filebeat s'en occupera. Cela est souvent connu sous le nom de **_principe de responsabilité unique._**

#### **Configurer Filebeat**

> Pour cette section, les fichiers filebeat.yml et Dockerfile ont été obtenus à partir du [dépôt github sample-filebeat-docker-logging](https://github.com/bcoste/sample-filebeat-docker-logging) de [Bruno COSTE](https://medium.com/@bcoste). Un grand merci pour son travail génial.

> Mais comme j'ai apporté plusieurs modifications à filebeat.yml selon les exigences de cet article, je les ai hébergés avec filebeat.service (fichier systemd) séparément sur mon propre dépôt. Vous pouvez accéder au dépôt [ici](https://github.com/rav94/filebeat-demo).

En tant qu'étape initiale, vous devez mettre à jour votre fichier filebeat.yml qui contient les configurations de Filebeat. Voici un exemple de fichier filebeat.yml que vous pouvez utiliser. Notez la ligne 21, le champ output.logstash et le champ hosts. Je l'ai configuré avec l'adresse IP du serveur sur lequel j'exécute ma pile ELK, mais vous pouvez le modifier si vous exécutez Logstash sur un serveur séparé. Par défaut, Logstash écoute Filebeat sur le port 5044.

> Pour en savoir plus sur les paramètres de configuration Docker de Filebeat, [consultez ici](https://www.elastic.co/guide/en/beats/filebeat/master/filebeat-input-docker.html).

Après cela, vous pouvez créer votre propre image Docker Filebeat en utilisant le Dockerfile suivant.

Une fois l'image construite, vous pouvez la pousser dans votre dépôt Docker. Maintenant que vous avez la capacité d'exécuter Filebeat en tant que conteneur Docker, il ne reste plus qu'à exécuter le conteneur Filebeat sur vos instances hôtes exécutant des conteneurs. Voici la commande docker run.

```
docker run -v '/var/lib/docker/containers:/usr/share/dockerlogs/data:ro' -v '/var/run/docker.sock:/var/run/docker.sock' --name filebeat ${YOUR_FILEBEAT_DOCKER_IMAGE}:latest
```

Dans la commande Docker ci-dessus, notez les deux paramètres de montage de liaison : /var/lib/docker/containers est le chemin où les logs Docker existent dans la machine hôte, et il a été lié au chemin /usr/share/dockerlogs/data dans le conteneur Filebeat avec un accès en lecture seule. Dans le deuxième argument de montage de liaison, /var/run/docker.sock est lié au démon Docker du conteneur Filebeat. Il s'agit du socket Unix sur lequel le démon Docker écoute par défaut et il peut être utilisé pour communiquer avec le démon depuis un conteneur. Cela permet à notre conteneur Filebeat d'obtenir les métadonnées Docker et d'enrichir les entrées de log des conteneurs avec les métadonnées et de les pousser vers la pile ELK.

Si vous souhaitez automatiser ce processus, j'ai écrit un fichier d'unité Systemd pour gérer Filebeat en tant que service.

#### **Configurer la pile ELK**

Pour cela, j'utiliserai ma deuxième instance EC2, où j'exécute la pile ELK. Vous pouvez le faire simplement en installant Docker Compose et en consultant ce dépôt génial [deviantony/docker-elk](https://github.com/deviantony/docker-elk) et en exécutant simplement **_docker-compose up -d_**

> Notez que toutes vos règles de pare-feu permettent le trafic entrant vers Logstash, Elasticsearch et Kibana.

Avant d'exécuter la pile ELK, vous devez vous assurer que votre fichier logstash.conf est correctement configuré pour écouter les logs entrants de Beats sur le port 5044 et que les logs sont correctement ajoutés à l'hôte Elasticsearch. Vous devez également vous assurer d'ajouter un paramètre d'index à votre Elasticsearch pour identifier les logs générés par Filebeat de manière unique.

Dans votre dépôt docker-elk, vous pouvez trouver votre fichier logstash.conf en suivant le chemin docker-elk/logstash/pipeline. Il s'agit du fichier de configuration pour configurer les paramètres de Logstash. Vous devez le mettre à jour comme suit :

Une fois cela fait, vous pouvez accéder à votre tableau de bord Kibana sur le port 5601 par défaut, comme défini dans le fichier docker-compose.yml du dépôt [deviantony/docker-elk](https://github.com/deviantony/docker-elk).

![Image](https://cdn-media-1.freecodecamp.org/images/V3snsitA4b770QQT-iJZaIs2CXxAgyFkwst9)
_Tableau de bord Kibana_

Sous l'onglet de gestion, vous pouvez créer un modèle d'index pour les logs Filebeat. Cela doit être fait avant de pouvoir visualiser les logs sur le tableau de bord Kibana.

![Image](https://cdn-media-1.freecodecamp.org/images/E1ZmKKsFfxdBIytNreN-2rpR1NfwaBo8ze-X)
_Configuration du modèle d'index Filebeat sur le tableau de bord Kibana_

Si vos conteneurs poussent correctement les logs vers Elasticsearch via Logstash, et que vous avez créé avec succès le modèle d'index, vous pouvez aller à l'onglet Discover du tableau de bord Kibana et visualiser les logs de votre application de conteneur Docker ainsi que les métadonnées Docker sous le modèle d'index filebeat*.

![Image](https://cdn-media-1.freecodecamp.org/images/cr6q8RtvQNdx2oselNrwjfL3DCzZKK5T3MC3)
_Découvrir les logs de l'application du conteneur Docker ainsi que les métadonnées de l'hôte Docker dans le tableau de bord Kibana_

**Références**

1. [https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-getting-started.html](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-getting-started.html)
2. [https://medium.com/@bcoste/powerful-logging-with-docker-filebeat-and-elasticsearch-8ad021aecd87](https://medium.com/@bcoste/powerful-logging-with-docker-filebeat-and-elasticsearch-8ad021aecd87)
3. [https://www.elastic.co/guide/en/logstash/current/configuration.html](https://www.elastic.co/guide/en/logstash/current/configuration.html)
4. [https://medium.com/lucjuggery/about-var-run-docker-sock-3bfd276e12fd](https://medium.com/lucjuggery/about-var-run-docker-sock-3bfd276e12fd)