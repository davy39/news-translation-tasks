---
title: Qu'est-ce qu'une passerelle API et pourquoi est-elle utile ?
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-12-11T21:40:25.000Z'
originalURL: https://freecodecamp.org/news/what-are-api-gateways
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/cover.png
tags:
- name: api
  slug: api
seo_title: Qu'est-ce qu'une passerelle API et pourquoi est-elle utile ?
seo_desc: APIs are often referred to as the front-door for applications to access
  data and business logic from backend services. As explained here, an API is essentially
  the interface that a piece of software presents to other humans or programs, allowing
  them...
---

Les API sont souvent appelées la porte d'entrée pour que les applications accèdent aux données et à la logique métier des services backend. Comme expliqué [ici](https://lightcloud.substack.com/p/api-integration-patterns), une API est essentiellement l'*interface* qu'un logiciel présente à d'autres humains ou programmes, leur permettant d'interagir avec ce logiciel.

Lors de la création d'une API, vous devez choisir un langage de programmation (Java, Python, PHP, etc.) dans lequel écrire la logique de l'API. Vous devez également déployer l'API sur un serveur et surveiller l'API pour vous assurer que votre infrastructure a suffisamment de capacité pour gérer un grand nombre de requêtes.

Les passerelles API abstraient ces étapes. Vous n'avez pas à écrire beaucoup de code ou à vous soucier de la gestion de l'infrastructure sous-jacente. Vous créez simplement des points de terminaison d'API auxquels les clients peuvent envoyer des requêtes.

Les principaux fournisseurs de cloud proposent tous un service de passerelle API entièrement géré :

1. [AWS API Gateway](https://aws.amazon.com/api-gateway/)

2. [GCP API Gateway](https://cloud.google.com/api-gateway)

3. [Azure API Management](https://azure.microsoft.com/en-gb/products/api-management)

Cet article expliquera pourquoi vous devriez utiliser une passerelle API, comment elles fonctionnent, et nous examinerons un exemple réel d'une passerelle API en action.

### Ce que nous allons couvrir :

1. [Pourquoi utiliser une passerelle API ?](#heading-pourquoi-utiliser-une-passerelle-api)

2. [Comment fonctionne une passerelle API](#heading-comment-fonctionne-une-passerelle-api)
   - [Validation des requêtes](#heading-validation-des-requetes)
   - [Autorisation et authentification](#heading-autorisation-et-authentification)
   - [Limitation de débit](#heading-limitation-de-debit)
   - [Routage des requêtes](#heading-routage-des-requetes)
   - [Transformation des requêtes et des réponses](#heading-transformation-des-requetes-et-des-reponses)

3. [Exemple concret](#heading-exemple-concret)

4. [Synthèse](#heading-synthese)

## Pourquoi utiliser une passerelle API ?

Une passerelle API est un service entièrement géré qui facilite la création, la publication, la maintenance, la surveillance et la sécurisation des API à presque n'importe quelle échelle.

Le terme « entièrement géré » dans le contexte du cloud computing signifie que les responsabilités de maintenance et de gestion du service sont prises en charge par le fournisseur de cloud. Cela signifie que l'infrastructure sous-jacente, les mises à jour logicielles, la sécurité, la scalabilité, la disponibilité et la reprise après sinistre sont toutes gérées par le fournisseur de cloud.

Cette abstraction facilite principalement la vie des développeurs, car ils n'ont besoin de se concentrer que sur le développement du service au lieu de s'inquiéter de sa gestion. Ce n'est cependant pas toujours le cas, car chaque abstraction a un prix.

Dans ce cas, le prix de cette abstraction est une perte de flexibilité. La plupart des passerelles API proposées par les fournisseurs de cloud ont une limite stricte sur le nombre de requêtes par seconde (RPS) qu'elles peuvent gérer.

Il y a également le coût plus élevé du cloud pour l'utilisation d'un service géré comme une passerelle API, qui doit être mis en balance avec le nombre plus élevé de jours-développeurs (nombre de développeurs * nombre de jours travaillés) nécessaires pour construire une API à partir de zéro.

Pour vraiment comprendre les avantages de l'utilisation d'une passerelle API, examinons les étapes que vous devez suivre pour concevoir, écrire et déployer une API traditionnelle :

### Étape 1 : Définir les exigences et le périmètre

* Comprendre les besoins des utilisateurs ou systèmes cibles.

* Déterminer les données et fonctionnalités que l'API exposera.

### Étape 2 : Concevoir l'API

* Définir les points de terminaison et les méthodes de l'API (GET, POST, PUT, DELETE).

* Concevoir le format des requêtes et des réponses (généralement JSON ou XML).

* Spécifier les modèles de données et les ressources avec lesquelles l'API interagira.

* Prévoir la gestion des erreurs et les codes d'état.

### Étape 3 : Développer l'API

* Choisir un langage de programmation et un framework.

* Implémenter les points de terminaison de l'API comme défini dans la phase de conception.

* Intégrer avec des bases de données ou d'autres services si nécessaire.

* S'assurer que les pratiques de sécurité sont implémentées, comme la validation des entrées et la limitation de débit.

### Étape 4 : Déployer l'API

* Choisir une solution d'hébergement (fournisseur de cloud, serveurs sur site).

* Configurer l'environnement de déploiement.

* Déployer l'API sur le serveur.

### Étape 5 : Surveiller et maintenir l'API

* Surveiller l'API pour le temps de fonctionnement, les performances et les erreurs.

* Mettre régulièrement à jour l'API pour corriger les bugs et patcher les vulnérabilités de sécurité.

Avec une passerelle API, vous devez principalement vous concentrer sur l'étape 1, l'étape 2 et des parties de l'étape 3. Les autres étapes sont principalement abstraites et gérées par la passerelle API.

La principale raison d'utiliser une passerelle API est de simplifier le processus de développement et de maintenance d'une API.

## Comment fonctionne une passerelle API

Une passerelle API fait beaucoup de choses en même temps.

Pour comprendre comment fonctionne une passerelle API, considérons une analogie avec un restaurant.

Une passerelle API est comme le maître d'hôtel (en français, maître d', plus ou moins). Le maître d' se trouve généralement dans les restaurants haut de gamme, bien que ce soit une profession en voie de disparition.

Le maître d' sert de liaison entre les clients et le personnel du restaurant, et est responsable de :

1. **Accueil et placement des clients** : Le maître d' est souvent la première personne que les clients rencontrent lorsqu'ils arrivent au restaurant. Il accueille chaleureusement les clients, s'enquiert des réservations et les aide à s'installer à leur table, en tenant compte de leurs préférences et demandes spéciales.

2. **Réservations** : Le maître d' est responsable de la gestion des réservations et s'assure que les tables sont allouées efficacement. Il suit les tables disponibles et les heures de réservation, en faisant les ajustements nécessaires pour accueillir les clients.

3. **Gestion des temps d'attente** : Pendant les périodes chargées, le maître d' gère les temps d'attente des clients en fournissant des estimations et en offrant des alternatives, comme s'asseoir au bar ou dans une zone d'attente.

4. **Résolution des problèmes** : Si des problèmes ou des préoccupations surviennent pendant le repas d'un client, le maître d' intervient pour les résoudre rapidement et s'assurer que le client est satisfait.

5. **Gestion des demandes spéciales** : Si les clients ont des demandes spéciales ou des restrictions alimentaires, le maître d' communique celles-ci à la cuisine et s'assure que les besoins du client sont satisfaits.

En bref, le maître d' est une personne aux multiples talents et responsabilités dans un restaurant. D'après l'image ci-dessous, nous pouvons voir comment le maître d' sert de communicateur entre les clients et tout ce dont ils pourraient avoir besoin.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81489f0d-0f66-4b18-b59b-6debb17341e5_1754x1064.png align="left")

*Un maître d' sert de communicateur entre les clients et tout ce dont ils pourraient avoir besoin.*

Une passerelle API fonctionne de manière similaire. Elle agit comme le communicateur entre les clients et les nombreux services auxquels ils peuvent avoir besoin d'accéder. Une vue simplifiée de cela est montrée ci-dessous.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c4cf127-4e90-4beb-9987-80998211e7cf_1768x916.png align="left")

*La passerelle API sert d'intermédiaire entre les clients et les nombreux services auxquels ils peuvent avoir besoin d'accéder.*

Examinons plus en détail ce qu'une passerelle API peut faire.

### **Validation des requêtes**

Cela implique de vérifier les requêtes entrantes pour confirmer qu'elles répondent à des critères prédéfinis avant de les transmettre aux services backend.

Cela peut inclure la vérification de la structure de la requête, la validation des types de données, la vérification que les paramètres requis sont présents, et la validation des paramètres de requête, des en-têtes et du corps de la requête par rapport à un schéma.

En faisant cela, la passerelle API agit comme une première ligne de défense, empêchant les requêtes malformées ou malveillantes d'atteindre les systèmes backend.

En utilisant notre analogie avec le restaurant, cela est similaire au maître d'hôtel attendant à l'entrée du restaurant pour accueillir les clients à leur arrivée. Mais n'oubliez pas, il s'agit d'un restaurant haut de gamme. Donc le maître d'hôtel s'assure que les clients sont habillés selon le code vestimentaire du restaurant – similaire à la validation de la requête API entrante par rapport à un schéma prédéfini.

### Autorisation et authentification

L'authentification est le processus de vérification de l'identité d'un utilisateur ou d'un service faisant une requête, souvent par le biais de credentials comme un nom d'utilisateur et un mot de passe, des tokens, ou des clés API.

Une fois authentifié, l'autorisation détermine quelles ressources ou opérations l'entité authentifiée a la permission d'accéder ou d'exécuter.

Les passerelles API s'intègrent souvent avec des fournisseurs d'identité et supportent divers mécanismes d'authentification et d'autorisation comme [OAuth](https://oauth.net/), [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token), les clés API, etc. Elles s'assurent que seules les requêtes légitimes et autorisées sont autorisées à atteindre les services backend.

L'authentification concerne le « qui » tandis que l'autorisation concerne les « permissions ».

Pour le maître d'hôtel attendant les clients à leur arrivée au restaurant, l'authentification impliquerait que les clients prouvent qu'ils sont bien ceux qu'ils prétendent être, généralement en montrant une forme d'identification avec une photo qui peut être comparée à leur visage.

L'autorisation impliquera de vérifier qu'ils ont une réservation, c'est-à-dire qu'ils ont la permission d'entrer dans le restaurant et de commander un repas.

### Limitation de débit

La limitation de débit implique de contrôler le nombre de requêtes qu'un utilisateur ou un service peut faire dans un laps de temps spécifié, généralement défini comme une limite sur le nombre de requêtes par seconde (RPS).

La limitation de débit aide à éviter la surcharge des services backend, assurant qu'ils restent [disponibles](https://lightcloud.substack.com/i/59017006/high-availability). La limitation de débit est également utilisée comme partie d'une stratégie de contrôle des coûts, puisque vous paierez pour chaque requête envoyée à la passerelle API.

Les passerelles API peuvent appliquer différentes politiques de limitation de débit en fonction de l'utilisateur, du service ou du point de terminaison accédé.

En utilisant notre analogie avec le restaurant, imaginez notre restaurant avec des clients à l'intérieur, qui ont tous été validés, authentifiés et autorisés à entrer dans le restaurant. Mais les clients ont particulièrement faim et soif et continuent de commander repas après repas et boisson après boisson. À un certain point, cela devient ingérable pour le restaurant. Les cuisiniers et les serveurs sont surchargés et n'ont plus la capacité de prendre de nouvelles commandes, les assiettes et les couverts sont tous utilisés, et la nourriture dans la cuisine commence à manquer.

Le maître d'hôtel peut intervenir et limiter le nombre de commandes que les clients passent. Par exemple, en limitant le nombre de plats principaux ou de bouteilles de vin qui peuvent être commandés chaque heure. La limitation de débit garantit que le restaurant n'est pas surchargé de commandes et est toujours en mesure de servir de nouveaux clients.

### Routage des requêtes

Les passerelles API gèrent le routage des requêtes entrantes vers les services backend appropriés en fonction de divers critères comme le chemin de l'URL, la méthode HTTP, les en-têtes ou les paramètres de requête. C'est intégral pour les architectures de microservices où différents services gèrent différentes parties de l'API.

De retour à notre analogie avec le restaurant, en fonction de ce pour quoi les clients sont là, le maître d'hôtel les dirige vers la personne ou le lieu approprié – les dîners vers un serveur, les clients qui ne veulent qu'une boisson au bar, et ceux qui s'enquièrent de la réservation d'événements dans le restaurant vers le coordinateur d'événements.

### Transformation des requêtes et des réponses

Cela implique de modifier les requêtes et les réponses lorsqu'elles passent par la passerelle API.

Pour les requêtes, cela peut signifier ajouter, supprimer ou modifier des en-têtes, réécrire des URL, ou même changer le corps de la requête. Pour les réponses, cela peut impliquer de changer le code d'état, de modifier des en-têtes, ou de transformer le corps.

Cette capacité permet à la passerelle API de servir d'intermédiaire qui peut transformer les requêtes et les réponses pour répondre aux besoins des clients et des services backend.

Les services backend peuvent également effectuer cette transformation des requêtes et des réponses. La décision sur quel composant (passerelle API ou un service backend) effectue la transformation est subjective. Mais une passerelle API est souvent un endroit idéal pour centraliser une telle transformation avec un effort minimal, au lieu d'avoir des transformations personnalisées dans chaque service backend.

Si un client dans un restaurant est intolérant au gluten, par exemple, ses commandes doivent être transformées pour s'assurer que son repas ne contient pas de gluten.

La logique de cette transformation de commande peut être gérée par le maître d'hôtel en appelant explicitement quels ingrédients doivent être exclus du plat avant d'envoyer la commande au chef. Cette transformation peut également être gérée dans la cuisine par le maître d'hôtel en disant simplement au chef que le client a commandé un plat sans gluten et en le laissant modifier la commande en conséquence.

## Exemple concret

Une architecture de microservices est une approche de développement de logiciels qui décompose une grande application en composants plus petits et indépendants appelés microservices. Chaque microservice est une unité autonome avec une fonction ou une responsabilité spécifique au sein de l'application plus large.

La figure ci-dessous montre une architecture de microservices simple pour une application de commerce électronique de base.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F62394846-1dc8-4f0f-a4b0-0db079c1ddcd_1794x916.png align="left")

*Une passerelle API utilisée dans une architecture de microservices pour un site de commerce électronique*

* **Clients** : Ce sont différents clients qui interagissent avec la plateforme de commerce électronique. Ils peuvent être une application mobile, un navigateur web, ou toute autre application tierce.

* **Passerelle API** : Elle sert de point d'entrée unique pour tous les types de clients. Elle achemine les requêtes vers les microservices appropriés en fonction de la nature de la requête (liée à l'utilisateur, au produit, à la commande).

* **Services** : Ce sont des exemples de microservices spécifiques à un site de commerce électronique. Chaque service gère un aspect différent de la logique métier comme les profils utilisateurs, le catalogue de produits et le traitement des commandes.

* **Bases de données** : Chaque microservice a sa propre base de données dédiée, assurant l'isolation des données et l'indépendance des services.

Dans cet exemple, la passerelle API :

1. S'assure que chaque requête client est **validée**

2. S'assure que les clients sont **authentifiés et autorisés** avant de pouvoir effectuer certaines actions comme passer une commande ou écrire un avis pour un produit

3. **Limite le débit** des requêtes pour s'assurer que les services ne sont pas mis hors ligne par des acteurs malveillants envoyant un grand nombre de requêtes

4. **Achemine les requêtes clients** vers les services backend appropriés en fonction de divers critères comme le chemin de l'URL, la méthode HTTP, les en-têtes ou les paramètres de requête.

5. Gère la **transformation des requêtes et des réponses**. Par exemple, la réponse du service de produits peut être dans un format complexe avec des détails étendus. La passerelle API prend cette réponse et la transforme dans un format plus adapté à l'application mobile. Cela peut impliquer de simplifier les données, de les convertir dans un format plus léger, ou d'extraire uniquement les informations essentielles nécessaires à l'application mobile.

## Synthèse

Une passerelle API est un service entièrement géré qui facilite la création, la publication, la maintenance, la surveillance et la sécurisation des API à presque n'importe quelle échelle. Étant entièrement géré, il abstrait l'effort nécessaire pour gérer et maintenir l'infrastructure sous-jacente – cela est géré par le fournisseur de cloud offrant le service.

La passerelle API agit comme l'intermédiaire entre les clients et les nombreux services auxquels ils peuvent avoir besoin d'accéder. Elle gère la validation des requêtes, l'authentification et l'autorisation, la limitation de débit, le routage des requêtes, et la transformation des requêtes/réponses.

Elle est particulièrement utile dans les architectures de microservices en tant que point d'entrée central pour gérer, traiter et router les requêtes entrantes vers les microservices appropriés. Elle joue un rôle crucial dans la simplification de l'interaction côté client et fournit une interface centrale pour un groupe de microservices.