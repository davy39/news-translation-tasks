---
title: Un aperçu de la communication dans les microservices Kubernetes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T15:31:03.000Z'
originalURL: https://freecodecamp.org/news/communication-in-kubernetes-microservices-bf0a2af06551
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JsNkOMxwSlxFNW44eFBdqg.jpeg
tags:
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: Microservices
  slug: microservices
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: Un aperçu de la communication dans les microservices Kubernetes
seo_desc: 'By Adam Henson

  The “service” concept and a Node.js example


  Chico Hailing a Cab

  Based on complexity, a layer of microservices can require a variety of communication.
  Kubernetes provides a rich set of features in managing services, load balancing,
  and...'
---

Par Adam Henson

#### Le concept de "service" et un exemple Node.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*JsNkOMxwSlxFNW44eFBdqg.jpeg)
_Chico Hailing a Cab_

En fonction de la complexité, une couche de microservices peut nécessiter divers types de communication. Kubernetes offre un ensemble riche de fonctionnalités pour gérer les services, l'équilibrage de charge et la mise en réseau.

Cet article vise à fournir un exemple simple. Pour une vue d'ensemble approfondie, consultez [la documentation officielle sur les Services](https://kubernetes.io/docs/concepts/services-networking/service/).

### Services

> Un `Service` Kubernetes est une abstraction qui définit un ensemble logique de `Pods` et une politique pour y accéder - parfois appelé un micro-service. ~ [Kubernetes Docs](https://kubernetes.io/docs/concepts/services-networking/service/)

Comme documenté, nous avons plusieurs options pour exposer et communiquer avec les services. Examinons le DNS de Kubernetes. Les détails sur la nomenclature DNS peuvent être trouvés [ici](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#what-things-get-dns-names).

### Un exemple simple

Considérons un ensemble de microservices qui doivent communiquer entre eux via le protocole HTTP. Par exemple, supposons que nous devons créer un travail cron pour ping un endpoint de vérification de santé depuis un autre pod et logger le code de statut de la réponse.

Nous avons une application Node.js Express.

D'accord, cette application peut recevoir des requêtes HTTP GET à "/healthcheck" et répondre avec du JSON.

Très bien, créons maintenant une petite application cron pour exécuter des requêtes vers cet endpoint à 8h00 chaque jour.

Très bien, très bien... rien d'extraordinaire ici. Attendez une minute, examinons de plus près la ligne ci-dessous qui définit l'endpoint à récupérer.

```
const apiUrl = 'http://api:3000/healthcheck';
```

En utilisant le DNS de Kubernetes, communiquer avec d'autres pods est aussi simple que cela ! Notre configuration de service pour notre première application ci-dessus (l'application Express) pourrait être aussi simple que ci-dessous.

Notre application cron pourrait ressembler à ce qui précède. La configuration des pods est hors du cadre de cet article, mais vous pouvez lire comment le faire en utilisant [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

### Conclusion

Kubernetes offre une multitude de fonctionnalités et de documentation soutenant divers moyens de communication interne et d'exposition au monde extérieur. Nous pouvons obtenir une grande efficacité simplement avec le DNS.