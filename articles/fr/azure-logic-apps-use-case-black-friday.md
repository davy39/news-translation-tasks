---
title: Cas d'utilisation d'Azure Logic Apps - Black Friday
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-04T04:25:56.000Z'
originalURL: https://freecodecamp.org/news/azure-logic-apps-use-case-black-friday
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/black-friday-Banner-image.png
tags:
- name: Azure
  slug: azure
- name: Logic Apps
  slug: logic-apps
- name: Middleware
  slug: middleware
- name: use-cases
  slug: use-cases
seo_title: Cas d'utilisation d'Azure Logic Apps - Black Friday
seo_desc: 'By Nadeem Ahamed

  This blog gives an overview of how Azure Serverless technologies came to rescue
  when the custom-built integration system went down. Also, it shows the high-level
  architecture solution built using Azure Serverless services like Logic ...'
---

Par Nadeem Ahamed

Cet article donne un aperçu de la manière dont les technologies serverless d'Azure sont venues à la rescousse lorsque le système d'intégration personnalisé est tombé en panne. Il montre également la solution d'architecture de haut niveau construite en utilisant les services serverless d'Azure comme Logic Apps, Service Bus Queue et Topics, etc. pour remplacer le système hérité.

Cet article a été initialement publié sur [Serverless360.com](https://www.serverless360.com)

## Comment tout a commencé ?

![Système hérité](https://www.serverless360.com/wp-content/uploads/2019/06/1-Legacy-system.png)

Il y a environ trois ans, Northwind, une entreprise qui opère dans l'espace B2B, souhaitait étendre son activité au B2C. Ainsi, l'entreprise voulait ouvrir une boutique en ligne (SaaS). Étant une entreprise spécialisée dans le B2B, il n'y avait ni entrepôt ni service de transport pour servir efficacement les clients. L'entreprise a choisi de travailler avec un LSP (Logistics Service Provider). Le système hérité a été construit en utilisant un middleware pour connecter la boutique en ligne et le LSP. Plus tard, le système hérité a été intégré au système de messagerie. La complexité du système a augmenté avec l'ouverture de plusieurs succursales (boutiques en ligne) à travers le monde.

Un jour, tout le système est tombé en panne, et l'entreprise a commencé à perdre des centaines de commandes. L'entreprise a alors fait appel à une équipe d'experts pour réparer leur middleware.

### **Exigences à prendre en compte**

* Stabilité – le système doit être suffisamment stable pour gérer un grand nombre de commandes.
* Surveillance – le système doit être surveillé pour alerter le personnel opérationnel en cas de problème.
* Gérer 10 000 commandes par heure.
* Nouvelle boutique en ligne SaaS

## La Solution

![Middleware serverless](https://www.serverless360.com/wp-content/uploads/2019/06/2-serverless-middleware.png)

L'équipe d'experts a remplacé le middleware en utilisant les technologies serverless d'Azure. Principalement, Logic Apps et d'autres entités serverless comme Azure Functions, Service Bus Queues et Topics ont été utilisées. Le middleware avec état a été transformé en un système sans état en utilisant une approche basée sur les événements.

## Qu'est-ce que le Serverless ?

![qu'est-ce que le serverless](https://www.serverless360.com/wp-content/uploads/2019/06/3-what-is-serverless.png)

**L'abstraction du serveur, de la plateforme et du runtime** – Il n'est pas nécessaire de provisionner ou de maintenir des serveurs. Il n'y a pas de logiciel ou de runtime à installer, maintenir ou administrer.

**Mise à l'échelle pilotée par les événements** – C'est l'une des caractéristiques importantes du serverless, vous n'avez pas à vous soucier de la mise à l'échelle de votre solution si la demande augmente.

**Micro-facturation** – Lorsque votre code est exécuté, vous payez par exécution. Typiquement, les fournisseurs calculent cela en fonction de la consommation de mémoire et du temps nécessaire pour l'exécution.

### Avantages

**Gérer des applications, pas des serveurs** – L'avantage significatif du serverless est que l'utilisateur ne gère pas les serveurs, mais les fournisseurs de services cloud le font.

**DevOps réduit** – Cela réduit les coûts DevOps car l'infrastructure est maintenue par le CSP.

**Temps de mise sur le marché plus rapide** – Cela réduit le temps de mise sur le marché car la technologie serverless prépare le terrain et permet au développeur de se concentrer sur la logique.

## Azure Logic Apps

> _Vous pouvez exécuter un workflow métier dans Azure en utilisant le service Logic App._

Logic App est un conteneur logique pour un workflow que vous pouvez définir en utilisant des déclencheurs et des actions. Un déclencheur peut instancier un workflow, qui peut consister en une ou plusieurs activités (actions). Par exemple, vous pouvez déclencher un workflow en envoyant une requête HTTP ou planifier un workflow toutes les heures pour récupérer des données depuis un site web public. Il existe plus de 200 connecteurs prêts à l'emploi disponibles pour l'intégration d'entreprise.

### Avantages

* Les connecteurs prêts à l'emploi réduisent les défis d'intégration
* Connecter et intégrer des données depuis le cloud vers les locaux
* Messagerie B2B et d'entreprise dans le cloud
* Un puissant concepteur de workflows basé sur le web

## Tarification d'Azure Logic Apps

![Tarification d'Azure Logic Apps](https://www.serverless360.com/wp-content/uploads/2019/06/4-logic-Apps-pricing.png)

La tarification est très simple. Elle fonctionne sur le modèle pay-as-you-go, elle ne vous coûtera que quelques centimes. Par exemple, si vous traitez 1000 messages de bus de service par jour, avec un workflow de cinq actions, cela vous coûtera environ 4,62 EUR. Pour exécuter une action normale, cela coûtera 0,000025 $ et pour un connecteur standard, cela vous coûtera 0,000125 $. Même le connecteur d'entreprise ne vous coûtera que 0,001 $. Pour plus d'informations, consultez la page de tarification [ici](https://azure.microsoft.com/en-in/pricing/details/logic-apps/).

## Solution d'architecture de base

![Solution d'architecture de base](https://www.serverless360.com/wp-content/uploads/2019/06/5-Basic-architecture-solution.png)

Initialement, il y a une boutique en ligne connectée à l'application logique Webshop Publisher via Webhook. Les applications logiques Webshop Publisher agissent comme l'orchestrateur du workflow. Les données de la boutique en ligne sont converties en entité canonique et transmises à l'application logique Canonical Order Mapper. Par la suite, le flux de contrôle passe au CE Publisher où la traduction de l'objet se produit. Ensuite, l'objet traduit est envoyé au Service Bus Topic. Les abonnements aux sujets fournissent une forme de communication un-à-plusieurs, selon un modèle de publication/abonnements. Découvrez les règles d'abonnement aux sujets [ici](https://www.serverless360.com/blog/manage-azure-topic-subscription-rules). En fonction du filtre, les commandes sont envoyées à l'abonné LSP et à l'abonné MS (Marketing System).

## Impressionnante scalabilité d'Azure Logic Apps

![Scalabilité impressionnante](https://www.serverless360.com/wp-content/uploads/2019/06/6-impressive-scalability.png)

En exécutant le workflow ci-dessus, il a pu traiter 73 120 commandes en 20 minutes. Chaque commande était traitée en moins de 3 secondes et le taux de réussite était supérieur à 98 %. Le journal ci-dessus montre qu'il y a eu 73 120 exécutions complétées, dont 72 972 ont été réussies et 148 ont échoué.

## Vue des entités dans un groupe de ressources

![Vue des entités](https://www.serverless360.com/wp-content/uploads/2019/06/7-view-of-entities.png)

L'image ci-dessus représente comment les entités seront listées dans un groupe de ressources. Pour une meilleure gestion des entités, utilisez l'étiquette Display Name. Cela aide l'utilisateur à déboguer le workflow en cas d'échec.

## Application logique Webshop Publisher

![Application logique Webshop Publisher](https://www.serverless360.com/wp-content/uploads/2019/06/8-webshop-publisher-logic-app.png)

Prêt à l'emploi, il y a un déclencheur HTTP qui initie l'application logique et envoie une réponse 201 directement pour le message reçu. La réponse 201 représente que la requête a été remplie et a abouti à la création d'une ou plusieurs nouvelles ressources. Par la suite, envoie le message de commande à l'autre application logique (Mapper la commande à la commande canonique) et à Publier la commande canonique.

### Propriétés suivies

Dans l'action « Réponse 201 directe », les propriétés suivantes sont suivies

* Email du client
* Flux
* ID de commande
* ID de boutique

## Mapper de commande canonique

![Mapper de commande canonique](https://www.serverless360.com/wp-content/uploads/2019/06/9canonical-order-mapper.png)

L'application logique est déclenchée par la réception de la requête HTTP. Ensuite, le message est transmis aux actions de l'opération de données pour composer les éléments de commande canonique et créer les données de référence de la boutique. Par la suite, compose la commande canonique en utilisant l'action de l'opération de données et renvoie la réponse.

## Explorateur de Service Bus

Pour une gestion facile des entités, utilisez l'explorateur de Service Bus. Il fournit une option de filtre pour le sujet Service Bus à l'aide de laquelle le message peut être envoyé aux abonnements définis (LSP). Le message sera filtré en fonction des propriétés définies dans le sujet Service Bus. [Voici comment Serverless360 fait une meilleure option pour l'explorateur de Service Bus.](https://www.serverless360.com/compare-service-bus-explorer)

## Surveillance

![Log Analytics](https://www.serverless360.com/wp-content/uploads/2019/06/10-Log-Analytics.png)

L'image ci-dessus montre le tableau de bord Log Analytics. Il fournit une représentation graphique et une capacité de surveillance pour les entités associées à Log Analytics. À l'intérieur de Log Analytics, l'utilisateur peut exécuter des requêtes puissantes et inspecter la base de données si quelque chose ne va pas.

## Démo – commande payée

Pour tester la nouvelle architecture de solution, envoyez la commande de test, utilisez l'outil Postman pour envoyer un message POST à l'application logique. Après l'envoi de la commande réussie, vous pouvez voir la réponse 201 en bas à gauche de l'outil Postman. À la réception de la commande, les applications logiques sont déclenchées et enfin, le message de commande atteint l'un des LSP respectifs.

## Pipeline CI/CD

![Pipeline CI/CD](https://www.serverless360.com/wp-content/uploads/2019/06/10-CICD-pipeline.png)

L'image ci-dessus représente l'architecture du pipeline CI/CD. Il y a trois blocs, à savoir le contexte du développeur, Azure DevOps et l'abonnement Azure. Le contexte du développeur contient PowerShell, les IDE, etc. Une fois que le développeur valide le code, il est validé dans le dépôt. En activant l'option de build, le pipeline de build déploie le code dans le stockage Blob. Une fois que le pipeline de build a terminé son travail, le pipeline de release se lance et indique à ARM de refléter les changements dans les environnements de développement, de test et de production.

### Avantages

* Aucune étape manuelle requise pour déployer le code.
* Le contrôle de qualité peut être effectué
* L'organisation peut avoir une équipe de développement plus grande

### **Défis**

* Beaucoup de maintenance est requise autour des modèles ARM.
* Les choses deviennent complexes si un modèle ARM tombe en panne. Car l'échec ne peut être détecté que lors de la release.
* Le rythme des changements de service est rapide

## Principaux enseignements de la solution ci-dessus

* Temps de mise sur le marché plus rapide : Il n'y avait que trois développeurs et ils ont pu terminer le projet en 3 mois.
* Résilient et scalable : Comme nous l'avons vu ci-dessus, l'application était hautement scalable. Elle pouvait gérer environ 73 mille commandes en 20 minutes.
* Il est particulièrement adapté aux systèmes critiques pour les entreprises

Cet article est un extrait de la session « Black Friday ? Logic Apps à la rescousse » présentée par [Aarjan Meirink](https://twitter.com/aarjanmeirink) lors de MSBuild 2019.