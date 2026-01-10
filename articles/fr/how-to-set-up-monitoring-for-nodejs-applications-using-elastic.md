---
title: Comment configurer la surveillance des performances des applications pour les
  applications Node.js en utilisant Elastic
subtitle: ''
author: Tamerlan Gudabayev
co_authors: []
series: null
date: '2023-08-07T20:57:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-monitoring-for-nodejs-applications-using-elastic
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/pexels-taras-makarenko-593172.jpg
tags:
- name: node js
  slug: node-js
- name: performance
  slug: performance
seo_title: Comment configurer la surveillance des performances des applications pour
  les applications Node.js en utilisant Elastic
seo_desc: "Building features is half the equation of creating a successful product.\
  \ \nThe other half is making something scalable and maintainable. One aspect of\
  \ that is the ability to monitor your services. \nThis is what we will learn today\
  \ using the help of so..."
---

Créer des fonctionnalités est la moitié de l'équation pour créer un produit réussi. 

L'autre moitié consiste à créer quelque chose de scalable et de maintenable. Un aspect de cela est la capacité à surveiller vos services. 

C'est ce que nous allons apprendre aujourd'hui avec l'aide du logiciel fourni par Elastic. Il s'agit de l'entreprise qui a initialement créé [ElasticSearch](https://www.elastic.co/), mais qui propose désormais une suite d'outils différents pour la recherche, l'observabilité, la journalisation et bien plus encore. 

Pour cet article, nous utiliserons spécifiquement l'outil [Elastic Application Performance Monitoring](https://www.elastic.co/observability/application-performance-monitoring) (APM). 

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Pourquoi devriez-vous surveiller vos services ?](#heading-why-should-you-monitor-your-services)
* [Qu'est-ce que Elastic Application Performance Monitoring ?](#heading-what-is-elastic-application-performance-monitoring)
* [Comment configurer APM](#heading-how-to-set-up-apm)
* [Conclusion](#heading-conclusion)

## Prérequis

Cet article traite strictement d'Elastic APM. Je suppose donc que vous souhaitez simplement le connecter à votre application Node.js. 

Je suppose également que vous avez Docker et Docker Compose installés localement et que vous savez comment les utiliser. 

Vous pouvez trouver le code de cet article [ici](https://github.com/TamerlanG/node-elastic-demo). 

## Pourquoi devriez-vous surveiller vos services ?

Si votre logiciel est réussi (c'est-à-dire que vous avez des utilisateurs), alors vous voudrez peut-être surveiller vos services pour quelques raisons. 

Passons-les en revue dans les sections suivantes. 

### Vous voulez connaître l'état de vos services 

Si vos services sont indisponibles, vous voulez être le premier informé. Vous ne voulez pas que ce soient vos utilisateurs qui vous en informent. 

Pour vous aider, vous pouvez ajouter des alertes basées sur certains critères, tels que :

* S'il y a plus de 10 erreurs de code d'état 500 au cours des 5 dernières minutes. 
* Si la latence de vos services dépasse un certain seuil (par exemple, 1 seconde). 

### Vous ne pouvez pas améliorer quelque chose que vous ne mesurez pas. 

Si vous voulez optimiser quelque chose, alors vous devez d'abord le mesurer. 

Trouvez les points chauds et corrigez-les. Mais pour pouvoir les trouver, vous devez d'abord surveiller vos services. 

Cela vous bénéficiera de deux manières :

La première manière est que vous pouvez définir vos SLO (Service Level Objectives), qui sont des objectifs que vous souhaitez avoir pour vos services. 

Par exemple :

* **Objectifs de disponibilité** – Je veux que mes services soient disponibles 99,9 % du temps. 
* **Objectifs de latence** – Je veux que le P99 (99e percentile) de mes requêtes soit complété en moins d'une seconde. 

Les SLO vous aident ensuite à définir vos SLA (Service Level Agreements) qui sont des promesses que vous faites à vos clients. Ces promesses augmentent la valeur que vous leur apportez. 

Exemples de SLA incluent :

* **Garantie de disponibilité** – Nos services seront disponibles 99,9 % du temps. Sinon, nous vous rembourserons (chaque entreprise a son propre modèle de remboursement – par exemple, AWS donnera des crédits pour tout le temps affecté, tandis que d'autres entreprises vous rembourseront simplement).
* **Garantie de latence** – Notre P99 est inférieur à 200 ms. Sinon, il y aura des répercussions. 

Passons à notre dernier point. 

### Les métriques ne doivent pas toujours être techniques 

Nous pouvons mesurer le comportement des utilisateurs. 

Des choses comme le temps qu'ils passent sur une page spécifique ou des choses au niveau du domaine qui sont spéciales pour l'entreprise. 

Ces métriques nous permettent de prendre des décisions basées sur les données. 

Par exemple, si vous voyez que vos utilisateurs ne remplissent pas un certain type de formulaire, alors vous déciderez qu'il y a quelque chose qui ne va pas et vous le corrigerez. 

Un autre exemple serait que si votre page de destination ne génère pas beaucoup de ventes, alors vous déciderez de faire quelque chose à ce sujet. 

## Qu'est-ce que Elastic Application Performance Monitoring ?

Elastic Application Performance Monitoring (APM) est un outil utilisé pour surveiller votre application construite sur la base de l'Elastic Stack. 

Voici quelques-unes de ses fonctionnalités :

* **Surveillance en temps réel** – APM collecte des métriques à la volée, afin que vous puissiez voir l'état de vos services en temps réel. 
* **Surveillance détaillée** – APM collecte des informations détaillées sur les requêtes telles que le temps de réponse, les requêtes de base de données, les appels aux caches, les requêtes HTTP externes, et plus encore. 
* **Métriques système** – APM récupère automatiquement les métriques de base au niveau de l'hôte et les métriques spécifiques à l'agent, comme les métriques .NET de l'agent .NET. Il collecte également des métriques telles que l'utilisation du CPU et plus encore. 
* **Collecte des erreurs** – APM collecte automatiquement les erreurs et exceptions non gérées. Elles sont regroupées en fonction de la trace de la pile, afin que vous puissiez identifier les nouvelles erreurs dès qu'elles apparaissent. 
* **Tracing** – APM vous permet de tracer les requêtes à travers les microservices qui ont APM configuré. 
* **Support** – APM supporte presque tous les langages de programmation et frameworks populaires. 

## Comment configurer APM 

Maintenant que nous savons ce qu'est APM et comment il fonctionne, configurons-le avec un agent Node localement. Pour cela, nous devons passer par deux étapes. 

### Étape 1 : Configurer ELK localement

Configurer l'Elastic Stack (ELK) localement peut être fastidieux. Il y a tant de services différents et vous devez les configurer tous pour qu'ils fonctionnent ensemble. 

Heureusement, d'autres personnes ont remarqué ce problème et ont créé une configuration Docker préconfigurée pour ELK. 

Pour les informations les plus à jour, suivez le guide [ici](https://github.com/sherifabdlnaby/elastdocker). 

Voici une version TLDR :

1. `git clone https://github.com/sherifabdlnaby/elastdocker.git`
2. `cd elastdocker`
3. `make setup`
4. `make all`

À ce stade, vous devriez avoir tous les services requis en cours d'exécution. Les trois plus importants sont notamment :

* ElasticSearch, qui est le cœur de tout cela, fonctionne sur le port 9200. 
* Kibana, qui est notre tableau de bord, fonctionne sur le port 5601. 
* Le serveur APM, qui collecte les métriques, fonctionne sur le port 8200. 

Si vous souhaitez vous connecter à Kibana, voici les identifiants :

* Nom d'utilisateur : `elastic`
* Mot de passe : `changeme`

### Étape 2 : Configurer l'agent Node 

D'accord, maintenant que nous avons configuré ELK, configurons les choses du côté client. 

La première étape consiste à ajouter le package de l'agent Node APM. Installez-le en utilisant la commande suivante :

`npm install elastic-apm-node --save`

Voici une note importante. **L'agent doit être démarré avant tous vos autres modules.** 

Donc, très probablement, vous devrez le démarrer dans le fichier principal de votre application (généralement `index.js`, `server.js` ou `app.js`) en haut. 

Voici un exemple pour une application Express : 

```javascript
const apm = require('elastic-apm-node').start({
  serviceName: 'node-application',
  secretToken: 'secrettokengoeshere',
  verifyServerCert: false,
  serverUrl: 'https://127.0.0.1:8200',
})

const app = require('express')()

app.get('/', function (req, res) {
  res.send('Hello World!')
})

app.listen(3000)
```

Décomposons la configuration :

* `serviceName` : nom de votre application.
* `secretToken` : jeton requis pour authentifier l'application auprès du serveur APM. (Le jeton par défaut qui est préconfiguré à partir de nos fichiers docker-compose est `secrettokengoeshere`)
* `verifyServerCert` : comme nous exécutons cela localement, nous ne voulons pas vérifier les certificats. 
* `serverUrl` : URL de notre serveur APM. 

Il ne reste plus qu'à exécuter votre application et à l'utiliser un peu pour qu'elle envoie quelques métriques. 

Ensuite, allez sur Kibana à l'adresse [https://localhost:5601/](https://localhost:5601/). 

Sous Observabilité, cliquez sur APM. 

Vous trouverez votre application et elle ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-8.png)
_Tableau de bord Elastic APM_

## Conclusion

En résumé : créer des fonctionnalités est la moitié de la bataille – l'autre moitié consiste à les surveiller et à les maintenir. 

Vous pouvez utiliser la solution prête à l'emploi d'Elastic, l'outil Application Performance Monitoring, pour surveiller votre application. 

J'espère que vous avez appris quelque chose aujourd'hui et si vous avez des questions, n'hésitez pas à me les poser sur Twitter (ou X) [@tamerlan_dev](https://twitter.com/tamerlan_dev). 

Merci d'avoir lu.