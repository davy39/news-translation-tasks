---
title: Comment gérer les changements de rupture pour les API et les schémas d'événements
subtitle: ''
author: Tim Kleier
co_authors: []
series: null
date: '2023-10-19T14:18:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-breaking-changes
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/7115374283_30d07f11c3_c-2.jpg
tags:
- name: api
  slug: api
- name: Microservices
  slug: microservices
- name: schema
  slug: schema
- name: versioning
  slug: versioning
seo_title: Comment gérer les changements de rupture pour les API et les schémas d'événements
seo_desc: "Several years ago while designing APIs for an ecommerce company, I discovered\
  \ the importance of API versioning. So I wrote about it in a freeCodeCamp article\
  \ entitled How to Version a REST API. \nNow I find myself designing event schemas\
  \ for sending m..."
---

Il y a plusieurs années, alors que je concevais des API pour une entreprise de commerce électronique, j'ai découvert l'importance du versionnage des API. J'ai donc écrit un article sur [freeCodeCamp](https://www.freecodecamp.org/news) intitulé [Comment versionner une API REST](https://www.freecodecamp.org/news/how-to-version-a-rest-api/).

Aujourd'hui, je me retrouve à concevoir des schémas d'événements pour envoyer des messages à travers un système distribué. C'est un problème très similaire avec des points de douleur et des solutions comparables. Le respect des contrats de données est crucial pour éviter de frustrer les abonnés aux événements ou de faire tomber les systèmes.

Le versionnage des API est transposable au versionnage des schémas d'événements, mais si vous pouvez faire évoluer les schémas de manière efficace, vous n'avez pas réellement besoin de versionnage. L'évolution efficace des schémas revient à éviter les changements de rupture.

Bien que j'en aie brièvement parlé dans l'article ci-dessus, je souhaite ici aborder en profondeur les changements de rupture et proposer davantage de solutions pour les éviter.

## Qu'est-ce qu'un changement de rupture ?

Essentiellement, un changement de rupture dans un schéma (dans un contexte d'API ou d'événement) est tout ce qui nécessite qu'un consommateur effectue une mise à jour de son côté. C'est un changement qui force le changement. Les schémas évolueront, mais une fois qu'un schéma est utilisé en production, vous devez être très prudent pour ne pas rompre le contrat de données.

Supprimer un format d'événement ou modifier la structure de base d'un événement constitue un changement de rupture. Mais les détails se situent au niveau des attributs (le champ ou la propriété).

### Changements de rupture structurels

Voici une liste des changements de rupture structurels pour les attributs de schéma :

* **Renommage des attributs** – Les modifications du nom d'un attribut, même s'il s'agit simplement de changer la casse (par exemple, de camelCase à TitleCase), constituent un changement de rupture.
* **Suppression d'attributs** – Retirer un attribut d'un schéma.
* **Changements de types de données** – Modifier les types de données, même si le changement semble compatible.
* **Rendre les attributs obligatoires** – Chaque fois que vous marquez un attribut (même un nouveau) comme obligatoire alors qu'il ne l'était pas avant, c'est un changement de rupture.

|Type|Exemple|
|------|-------|
|Renommage des attributs|`name` en `firstName`|
|Suppression d'attributs|Introduction de `firstName` mais suppression de `name`|
|Changements de type de données|Changement de `productSKU` de `integer` à `string`|
|Rendre les attributs obligatoires|Maintenant, un `customerID` est requis|

### Changements de rupture sémantiques

L'autre catégorie principale de changements de rupture au niveau des attributs concerne les changements dans la signification des données, ou changements sémantiques. Ils forcent les consommateurs à réinterpréter les données qu'ils reçoivent.

Ils sont les suivants :

* **Changements de format** – Tout changement dans le format d'un attribut.
* **Changements de signification** – Lorsque la signification déclarée ou implicite des données change.
* **Contraintes plus strictes** – Lorsque des exigences d'attributs sont ajoutées ou rendues plus restrictives.

|Type|Exemple|
|------|------|
|Changements de format|Date de `mm/dd/yyyy` à `yyyy-mm-dd`|
|Changements de signification|Changement d'un enum, changement de `providerCost` de dollars à cents
|Contraintes plus strictes|Ajout d'un maximum de `percentage` de 100

Il est important de noter que ce qui compte comme un "changement de rupture" peut être plus nuancé. Changer un `amount` de dollars à cents force toujours un changement par les abonnés aux événements, en interprétant la _signification_ des données envoyées. Soyez prudent avec ceux-ci, car ils ne sont pas toujours évidents.

## Qu'est-ce que les changements non rupture ?

Nous pouvons généralement décrire les changements non rupture comme étant additifs ou permissifs. Ce sont des changements qui ne nécessitent pas de modification pour les consommateurs.

Voici une liste des changements d'attributs non rupture :

* **Ajout d'un nouvel attribut** – Dans tous les contextes de schéma, l'ajout d'un nouvel attribut est un changement non rupture, à condition qu'il ne soit pas obligatoire (par exemple, pour une requête POST).
* **Rendre un attribut non obligatoire** – Lorsqu'un attribut était obligatoire mais que les nouvelles versions du schéma ne l'exigent plus.
* **Contraintes plus souples** – Des choses comme des plages d'entiers plus permissives (min et max) ou permettre une plus grande précision décimale. Soyez prudent et communiquez avec les consommateurs, car ils peuvent dépendre de contraintes plus strictes.

|Type|Exemple|
|------|------|
|Ajout d'un nouvel attribut|Ajout de `firstName` à côté de `name`|
|Rendre un attribut non obligatoire|`customerID` n'est plus requis|
|Contraintes plus souples|Max de pourcentage augmenté de 100 à 200|

Les changements non rupture peuvent souvent être évités. Mais faire évoluer les schémas de manière efficace peut être un défi et nécessiter beaucoup de réflexion pour ne pas rompre les schémas et la confiance des consommateurs.

## Comment faire évoluer les schémas

Malheureusement, la liste des changements de rupture est plus longue que celle des changements non rupture. Mais il existe certaines stratégies pour faire évoluer les schémas de manière non rupture.

1. **Connaissance du domaine** – Comprendre le domaine aidera à garantir que vous ne vous retrouvez pas avec des attributs mal nommés, des attributs sur le mauvais objet ou des types de données incorrects.
2. **Noms d'attributs spécifiques** – Plutôt que de changer le nom, le type de données ou le format d'un attribut, introduisez un nouvel attribut avec un nom plus spécifique et corrigez le type de données ou le format.
3. **Noms d'attributs avec intention** – Utilisez des noms d'attributs qui reflètent leur format ou leur intention. Par exemple, les consommateurs ne savent peut-être pas si `providerCost` serait en dollars ou en cents, alors spécifiez avec `providerCostInDollars` ou `providerCostInCents`. Cela empêchera également un changement de rupture si vous avez des problèmes de précision de calcul avec les dollars et décidez de fournir le coût en cents.
4. **Schéma et attributs en brouillon** – Utilisez extensivement le "mode brouillon" au niveau du schéma, obtenez des commentaires sur les attributs dans des environnements simulés avant qu'ils ne soient en direct en production. Pour les schémas qui sont utilisés en production, vous pourriez introduire un objet `draftedAttributes` et y mettre des attributs expérimentaux (non prêts pour la production). Communiquez avec les consommateurs que ces attributs sont en cours d'affinement – ils doivent donc s'attendre à des changements de rupture – et seront déplacés vers le schéma principal lorsqu'ils seront prêts.
5. **Prise en charge des attributs existants** – Laissez les anciens attributs dans le schéma. Ne supprimez pas les anciens attributs sauf si vous avez pu coordonner une stratégie de dépréciation/abandon avec les consommateurs.
6. **Versionnage** – Si nécessaire, versionnez vos schémas. Bien que cela puisse devenir assez difficile à maintenir, le versionnage de vos schémas est un moyen de permettre la compatibilité ascendante tout en avançant avec un nouveau schéma. Vous pouvez faire un versionnage de haut niveau (par exemple, v1 et v2) ou un versionnage sémantique plus granulaire (par exemple, v1.0.1). Il est préférable de versionner chaque schéma indépendamment, afin de ne pas avoir à, par exemple, copier tous les endpoints API v1 vers v2.

## Conclusion

Les changements de rupture sont un moyen rapide de rompre la confiance de tout consommateur d'API ou abonné à des événements. J'espère que les directives ci-dessus fourniront plus d'informations sur ce qui constitue un changement de rupture par rapport à un changement non rupture, et comment faire évoluer les schémas de manière efficace.

Si vous ne pouvez pas éviter les changements de rupture, **assurez-vous de coordonner avec tous les consommateurs**. Vous pouvez en fait gagner plus de confiance avec vos consommateurs si vous faites évoluer les schémas de manière efficace et communiquez les changements de rupture lorsqu'ils sont nécessaires.